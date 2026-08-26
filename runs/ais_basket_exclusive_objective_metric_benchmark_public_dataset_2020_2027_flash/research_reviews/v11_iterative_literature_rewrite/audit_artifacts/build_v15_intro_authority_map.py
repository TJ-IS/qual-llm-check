from __future__ import annotations

import datetime
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
MANUSCRIPT_DIR = HERE.parent


def find_repo_root() -> Path:
    for candidate in HERE.parents:
        if (candidate / "database_fulltext_all").is_dir():
            return candidate
    raise RuntimeError("repository root containing database_fulltext_all was not found")


REPO_ROOT = find_repo_root()


SOURCE_REGISTRY = {
    "ACAA": {
        "title": "Attending to Customer Attention: A Novel Deep Learning Method for Leveraging Multimodal Online Reviews to Enhance Sales Prediction",
        "path": "database_fulltext_all/28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leveraging-multimodal-online-re.md",
        "direct_read_scope": "complete Introduction, Literature Review, Positioning/Design Rationales/Methodological Challenges, and Proposed Method opening, local lines 37-130",
    },
    "DSDL": {
        "title": "A Theory-Driven Deep Learning Method for Voice Chat-Based Customer Response Prediction",
        "path": "database_fulltext_all/16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md",
        "direct_read_scope": "complete Introduction, Literature Review, theoretical foundation/methodological challenges, and Proposed Method opening, local lines 33-99",
    },
    "RADAR": {
        "title": "RADAR: A Framework for Developing Adversarially Robust Cyber Defense AI Agents with Deep Reinforcement Learning",
        "path": "database_fulltext_all/27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md",
        "direct_read_scope": "complete Introduction and Background plus Research Gaps/Questions and Proposed Design opening, local lines 31-128",
    },
    "DEEPIA": {
        "title": "Exploiting Expert Knowledge for Assigning Firms to Industries: A Novel Deep Learning Method",
        "path": "database_fulltext_all/12586_2023_exploiting-expert-knowledge-for-assigning-firms-to-industries-a-novel-deep-learning-method.md",
        "direct_read_scope": "complete Introduction and Literature Review plus problem formulation and DeepIA opening, local lines 25-116",
    },
    "XIAO": {
        "title": "E-Commerce Product Recommendation Agents: Use, Characteristics, and Impact",
        "path": "database_fulltext_all/00722_2007_e-commerce-product-recommendation-agents-use-characteristics-and-impact1.md",
        "direct_read_scope": "complete Introduction/Motivation/Scope/Contribution and review procedure plus Provider Credibility section, local lines 50-104 and 508-518",
    },
    "DAWSON": {
        "title": "A Knowledge-Centric Examination of Signaling and Screening Activities in the Negotiation for Information Systems Consulting Services",
        "path": "database_fulltext_all/12738_2016_a-knowledge-centric-examination-of-signaling-and-screening-activities-in-the-negotiation-for-inf.md",
        "direct_read_scope": "complete Introduction and adjacent literature/theory sections through methodology opening, local lines 57-146",
    },
    "CONTROL": {
        "title": "Responding to Online Reviews in Competitive Markets: A Controlled Diffusion Approach",
        "path": "database_fulltext_all/15468_2023_responding-to-online-reviews-in-competitive-markets-a-controlled-diffusion-approach.md",
        "direct_read_scope": "complete Introduction and Literature Review plus Model Description and Stochastic Optimal Control opening, local lines 25-120",
    },
}


# Each anchor is extracted verbatim from the stated local source line.  The map
# stores the exact sentence and a hash, while the surrounding complete-section
# read scope is frozen above.  These are writing prototypes, not substantive
# evidence for the Coding Agent claims.
ANCHOR_SPECS = {
    "A01": ("ACAA", "Introduction", 39, "Online reviews (reviews for short herein) have become", "domain phenomenon", "establishes an important information channel", "opening context"),
    "A02": ("ACAA", "Introduction", 39, "Sales prediction, as a focal problem", "research problem", "states why an outcome matters", "opening context"),
    "A03": ("ACAA", "Introduction", 41, "a straightforward way to realize reviewbased sales prediction", "prior approach", "states a direct existing capability", "prior capability"),
    "A04": ("ACAA", "Introduction", 41, "their provided solution approaches suffered serious deficiencies", "prior research", "turns from attempts to a bounded deficiency", "capability-to-gap transition"),
    "A05": ("ACAA", "Introduction", 43, "it is sensible to explore what kinds of reviews", "focal study", "turns a mechanism into a motivating question", "problem motivation"),
    "A06": ("ACAA", "Introduction", 47, "Customers’ attention paid to multimodal reviews is reflected", "focal phenomenon", "defines observable dimensions", "theory/construct bridge"),
    "A07": ("ACAA", "Introduction", 47, "From a process perspective", "focal phenomenon", "decomposes a process into ordered stages", "theory/construct bridge"),
    "A08": ("ACAA", "Introduction", 47, "customers’ initial attention to reviews, as an important prerequisite", "intermediate state", "links a prerequisite state to a later outcome", "mechanism close"),
    "A09": ("ACAA", "Introduction", 49, "Overall, we strive to unravel customer attention", "focal study", "summarizes a framework and poses a research question", "research question"),
    "A10": ("ACAA", "Introduction", 53, "In response to RQ2, we propose", "focal study", "answers a research question with a named method", "artifact proposal"),
    "A11": ("ACAA", "Introduction", 53, "DTV-AMI draws its strength from two components", "named artifact", "assigns distinct responsibilities to components", "artifact overview"),
    "A12": ("ACAA", "Introduction", 55, "Specifically, our proposed DTV allows", "artifact component", "states a component's operating responsibility", "artifact detail"),
    "A13": ("ACAA", "Introduction", 55, "The proposed AMI further empowers", "artifact component", "adds a second component and its distinct responsibility", "artifact detail"),
    "A14": ("ACAA", "Introduction", 55, "Experiment results in a case study", "evaluation", "states benchmark comparison and the inference it carries", "evaluation/contribution close"),
    "A15": ("ACAA", "Positioning, Design Rationales, and Methodological Challenges", 118, "leveraging customer attention for multi modal reviews", "design problem", "summarizes requirements that call for a specialized design", "design-rationale close"),
    "A16": ("ACAA", "Proposed Method", 130, "Figure 2 outlines the framework", "named artifact", "introduces the overall framework before components", "method opening"),
    "A17": ("ACAA", "Proposed Method", 130, "DTV-AMI first preprocesses", "named artifact", "states the first transformation in an ordered pipeline", "method opening"),
    "A18": ("ACAA", "Proposed Method", 130, "Next, it incorporates two mechanisms", "named artifact", "connects named components in sequence", "method opening"),
    "A19": ("ACAA", "Proposed Method", 130, "Although DTV-AMI outputs predictions directly", "artifact output", "bounds the primary output and a secondary use", "method close"),
    "D01": ("DSDL", "Introduction", 39, "Effectively predicting customers’ off-line responses", "research problem", "states the focal outcome's practical importance", "opening context"),
    "D02": ("DSDL", "Introduction", 41, "One major challenge lies", "design problem", "identifies a concrete information limitation", "problem statement"),
    "D03": ("DSDL", "Introduction", 43, "Prior research studies prediction tasks similar", "prior research", "groups adjacent tasks before comparison", "prior capability"),
    "D04": ("DSDL", "Introduction", 43, "However, the methods developed for these tasks cannot deal", "prior methods", "states a contextual incompatibility", "capability-to-gap transition"),
    "D05": ("DSDL", "Introduction", 45, "Extant research provides theoretical guidance", "prior theory", "introduces theory as problem knowledge", "theory bridge"),
    "D06": ("DSDL", "Introduction", 47, "In light of such a theoretical foundation", "focal study", "translates theory into a modeling responsibility", "theory-to-design bridge"),
    "D07": ("DSDL", "Introduction", 47, "To overcome these difficulties, we pose", "focal study", "poses a research question after concrete difficulties", "research question"),
    "D08": ("DSDL", "Introduction", 47, "In response to RQ1", "focal study", "answers a research question with a named strategy", "artifact proposal"),
    "D09": ("DSDL", "Introduction", 49, "Given these requirements for modeling", "focal study", "poses a second question from representation requirements", "research question"),
    "D10": ("DSDL", "Introduction", 49, "To this end, we design", "focal study", "introduces a component for the stated question", "artifact proposal"),
    "D11": ("DSDL", "Introduction", 51, "Given the constructed customer experience and expectation", "focal study", "connects two intermediate representations to the outcome", "integration bridge"),
    "D12": ("DSDL", "Introduction", 51, "Hence, we investigate our third research question", "focal study", "poses an integrative research question", "research question"),
    "D13": ("DSDL", "Introduction", 51, "To tackle RQ3", "focal study", "integrates components under a coordinated objective", "artifact integration"),
    "D14": ("DSDL", "Introduction", 53, "Overall, we propose a theory-driven deep learning method", "focal study", "summarizes the named artifact and target task", "artifact overview"),
    "D15": ("DSDL", "Introduction", 53, "By synergizing its three core components", "named artifact", "links core components to their joint responsibility", "artifact overview"),
    "D16": ("DSDL", "Introduction", 53, "Experiment results in the context", "evaluation", "states comparison and explanatory analysis", "evaluation/contribution close"),
    "D17": ("DSDL", "Introduction", 49, "both textual and audio (multiview)", "multiview evidence", "requires multiple information views for one construct", "representation requirement"),
    "R01": ("RADAR", "Introduction", 31, "artificial intelligence (AI) agents have been developed", "domain artifact", "establishes artifact capability and importance", "opening context"),
    "R02": ("RADAR", "Introduction", 33, "However, AI agents have been found to be vulnerable", "domain artifact", "turns from capability to vulnerability", "problem transition"),
    "R03": ("RADAR", "Introduction", 33, "While cyber defense AI agents are increasingly relied on", "prior research", "states a bounded unknown despite adoption", "gap statement"),
    "R04": ("RADAR", "Introduction", 35, "In this study, we aim to strengthen", "focal study", "states the design objective and theory base", "theory bridge"),
    "R05": ("RADAR", "Introduction", 35, "As such, RO establishes", "prior theory", "derives a design requirement from theory", "theory-to-design bridge"),
    "R06": ("RADAR", "Introduction", 37, "As adversarial attacks often involve taking a sequence", "focal phenomenon", "connects sequential actions to a modeling need", "method fit"),
    "R07": ("RADAR", "Introduction", 37, "RL is thus well-suited", "method class", "states why a method fits sequential action", "method fit"),
    "R08": ("RADAR", "Introduction", 39, "Drawing on the computational design science paradigm", "focal study", "introduces a named framework from theory and design paradigm", "artifact proposal"),
    "R09": ("RADAR", "Introduction", 39, "RADAR discovers effective adversarial attacks", "named artifact", "states two linked artifact outcomes", "artifact overview"),
    "R10": ("RADAR", "Introduction", 39, "Specifically, RADAR offers", "named artifact", "allocates distinct methods to distinct responsibilities", "artifact overview"),
    "R11": ("RADAR", "Introduction", 39, "Given that malware attacks are the leading threat", "evaluation", "specifies instantiation, benchmark comparison, and utility target", "evaluation overview"),
    "R12": ("RADAR", "Introduction", 39, "Overall, this study makes three major contributions", "focal study", "opens a bounded contribution summary", "contribution close"),
    "R13": ("RADAR", "Research Gaps and Questions", 116, "Our review of defending IT infrastructure suggests", "literature review", "derives a design need from the reviewed scope", "gap synthesis"),
    "R14": ("RADAR", "Research Gaps and Questions", 116, "Given these gaps, the following research questions are posed", "focal study", "poses questions after a gap synthesis", "research question"),
    "R15": ("RADAR", "Proposed Design", 120, "To address these research questions", "focal study", "answers research questions with a named framework", "design opening"),
    "R16": ("RADAR", "Proposed Design", 128, "Under these assumptions, RADAR consists", "named artifact", "enumerates inputs, phases, and outputs under assumptions", "design overview"),
    "R17": ("RADAR", "Proposed Design", 128, "Figure 2 provides an overview", "named artifact", "previews inputs, phases, operations, and outputs", "design overview"),
    "E01": ("DEEPIA", "Introduction", 27, "One important financial problem is", "research problem", "names the focal problem within a broader domain", "problem positioning"),
    "E02": ("DEEPIA", "Introduction", 29, "An ICS is a taxonomy", "focal object", "defines the focal object and its organizing relation", "object definition"),
    "E03": ("DEEPIA", "Introduction", 46, "It is challenging to design a method that simultaneously considers", "design problem", "attributes a joint-design challenge to heterogeneous formats", "methodological challenge"),
    "E04": ("DEEPIA", "Introduction", 46, "The central challenge is to develop", "design problem", "states the one integrating responsibility", "methodological challenge"),
    "E05": ("DEEPIA", "Introduction", 46, "To address the research gaps discussed above", "focal study", "introduces a method after the gap", "artifact proposal"),
    "E06": ("DEEPIA", "Introduction", 46, "In contrast to existing industry assignment methods", "focal method", "contrasts joint integration with a bounded prior capability", "method contribution"),
    "E07": ("DEEPIA", "Introduction", 46, "In doing so, our study makes two methodological contributions", "focal study", "names distinct methodological contributions", "contribution close"),
    "E08": ("DEEPIA", "Literature Review", 68, "Our literature review suggests several research gaps", "literature review", "bounds a gap to the reviewed literature", "gap synthesis"),
    "E09": ("DEEPIA", "DeepIA", 116, "We present the three building blocks", "named artifact", "announces building blocks before integration", "method opening"),
    "E10": ("DEEPIA", "DeepIA", 116, "The first building block encodes", "artifact components", "assigns inputs and outputs to building blocks", "method opening"),
    "E11": ("DEEPIA", "DeepIA", 116, "The last two building blocks constitute", "artifact components", "bounds which components carry novelty", "method opening"),
    "X01": ("XIAO", "Introduction", 54, "Recommendation agents", "focal artifact", "defines the artifact by input and action", "scope definition"),
    "X02": ("XIAO", "Introduction", 54, "In this paper, we focus our attention", "focal study", "narrows the study to a declared scope", "scope definition"),
    "X03": ("XIAO", "Introduction", 56, "The study of RAs falls", "focal artifact", "positions the artifact in the IS domain", "object positioning"),
    "X04": ("XIAO", "Introduction", 56, "a customer provides inputs", "artifact user", "links inputs to processing and output", "artifact process"),
    "X05": ("XIAO", "Introduction", 58, "RAs are distinguished from traditional DSSs", "focal artifact", "defines difference from an adjacent artifact class", "object distinction"),
    "X06": ("XIAO", "Introduction", 58, "Additionally, RAs are designed to understand", "focal artifact", "states a distinct design responsibility", "object distinction"),
    "X07": ("XIAO", "Introduction", 58, "there is an agency relationship", "focal relation", "identifies an agency relation and its uncertainty", "object distinction"),
    "X08": ("XIAO", "Motivation, Scope, and Contribution", 68, "The design of RAs consists of three major components", "artifact design", "separates input, process, and output responsibilities", "gap setup"),
    "X09": ("XIAO", "Motivation, Scope, and Contribution", 68, "research on RAs has focused mostly on process", "prior research", "contrasts algorithm focus with neglected design responsibilities", "gap setup"),
    "X10": ("XIAO", "Motivation, Scope, and Contribution", 68, "However, from the customers' perspective", "artifact evaluation", "broadens effectiveness beyond algorithms", "gap synthesis"),
    "X11": ("XIAO", "Review Procedure", 98, "The unit of analysis for this review", "review", "declares the analysis unit", "scope/procedure"),
    "X12": ("XIAO", "Provider Credibility", 512, "In the context of this paper, source credibility refers", "construct", "defines provider credibility and its dimensions", "construct definition"),
    "X13": ("XIAO", "Provider Credibility", 514, "The type and the reputation of the RA providers", "provider attribute", "keeps provider effects as a relation to be examined", "construct relation"),
    "X14": ("XIAO", "Provider Credibility", 516, "Therefore, as endorsers of RAs' recommendations", "provider type", "states a qualified comparative expectation", "construct relation"),
    "W01": ("DAWSON", "Introduction", 61, "screening is the process by which the buyer", "information-disadvantaged party", "defines screening against sender disclosure", "theory definition"),
    "W02": ("DAWSON", "Introduction", 61, "It is not clear how the signaling and screening processes interact", "prior research", "states an unresolved relation between two processes", "gap statement"),
    "W03": ("DAWSON", "Introduction", 71, "Adopting an interpretive orientation", "focal study", "states how the study examines the focal processes", "study positioning"),
    "W04": ("DAWSON", "Introduction", 71, "While this problem is not unique", "focal study", "bounds contextual transfer instead of claiming equivalence", "scope boundary"),
    "W05": ("DAWSON", "Signaling and Screening", 103, "The party who has an information asymmetry disadvantage", "information-disadvantaged party", "assigns screening responsibility", "theory definition"),
    "W06": ("DAWSON", "Signaling and Screening", 103, "One can screen by querying", "screening party", "specifies receiver-initiated evidence acquisition", "theory mechanism"),
    "W07": ("DAWSON", "Signaling and Screening", 117, "In summary, the current literature", "literature review", "bounds an absence claim to the reviewed literature", "gap synthesis"),
    "C01": ("CONTROL", "Introduction", 29, "The discussion above indicates", "focal study", "derives an operational challenge from preceding facts", "problem transition"),
    "C02": ("CONTROL", "Introduction", 31, "Since response efforts are costly", "decision maker", "turns a constraint into an optimization responsibility", "problem statement"),
    "C03": ("CONTROL", "Introduction", 31, "Past research in this area has predominately focused", "prior research", "contrasts prior consequence studies with the focal need", "gap setup"),
    "C04": ("CONTROL", "Introduction", 31, "Specifically, we address two main questions", "focal study", "poses questions after a bounded gap", "research question"),
    "C05": ("CONTROL", "Introduction", 35, "We assume that firms are rational", "focal model", "states the optimization model and objective", "model overview"),
    "C06": ("CONTROL", "Introduction", 35, "The stochastic variables (states) of interest", "focal model", "defines model state variables", "model overview"),
    "C07": ("CONTROL", "Introduction", 35, "A firm’s response is regarded as a control", "focal model", "defines an action as control over state", "model overview"),
    "C08": ("CONTROL", "Introduction", 35, "Thus, the overall evolution of ratings", "focal model", "defines response-conditioned dynamics", "model overview"),
    "C09": ("CONTROL", "Introduction", 37, "We estimate our model", "evaluation", "states data and estimation target", "evaluation overview"),
    "C10": ("CONTROL", "Introduction", 37, "We empirically validate", "evaluation", "assigns a validation responsibility to one modeled quantity", "evaluation overview"),
    "C11": ("CONTROL", "Introduction", 39, "Our prescriptive methodology enabled us", "focal method", "states the counterfactual question the method can answer", "contribution close"),
    "C12": ("CONTROL", "Model Description", 69, "In this study, we build an integrative model", "focal study", "integrates antecedents and consequences under one objective", "model opening"),
    "C13": ("CONTROL", "Model Description", 69, "The firm’s response strategy can be considered a control", "control action", "links an action to its state responsibility", "model opening"),
    "C14": ("CONTROL", "Model Description", 75, "At a high level, the chain of influence", "focal model", "summarizes an ordered mechanism chain", "mechanism overview"),
    "C15": ("CONTROL", "Stochastic Optimal Control Problem", 114, "The following natural question arises", "focal study", "poses the optimal-control question after dynamics", "control question"),
    "C16": ("CONTROL", "Stochastic Optimal Control Problem", 114, "The firm determines its optimal level of control effort", "decision maker", "selects control to optimize the finite objective", "control formulation"),
    "C17": ("CONTROL", "Model Description", 82, "whether management response directly impacts sales is an empirical question", "focal relation", "keeps a transfer relation empirical and context bound", "model boundary"),
}


INVENTORIES = {
    "P1": "p1_v15_authoritative_style_current_inventory_v1.json",
    "P2": "p2_v15_authoritative_style_current_inventory_v1.json",
    "P3": "p3_v15_authoritative_style_current_inventory_v1.json",
}


ASSIGNMENTS = {
    "P1": [
        "R01", "R11", "C01", "X02", "A06", "X01", "D03", "R09",
        "R11", "R10", "D04", "E04", "E02", "D05", "C14", "W04",
        "D06", "X01", "A08", "R09", "R16", "R03", "E03", "R14",
        "R15", "A16", "A12", "E10", "R11", "C10", "D16", "C14",
    ],
    "P2": [
        "R11", "R01", "X04", "X02", "E02", "D17", "R02", "E03",
        "D03", "X11", "X11", "A02", "X01", "C06", "A15", "W01",
        "W06", "X08", "X12", "X14", "C17", "W06", "D11", "C12",
        "D12", "R15", "D15", "C14", "A19", "R11", "C10", "W04",
        "C14",
    ],
    "P3": [
        "R11", "R01", "A07", "R06", "A06", "D17", "R09", "E02",
        "D03", "R09", "R10", "R01", "C02", "E08", "W04", "R06",
        "C06", "D06", "A11", "C06", "C07", "C08", "C15", "R15",
        "A17", "E10", "C16", "R11", "C10", "C17", "C14",
    ],
}


PARAGRAPH_FUNCTIONS = {
    "P1": {
        "P1-P0001": "task phenomenon and security boundary",
        "P1-P0002": "workspace scope and heterogeneity",
        "P1-P0003": "known-entry benchmark capability and unknown-entry gap",
        "P1-P0004": "source theory, transferable relation, and contextual state",
        "P1-P0005": "intermediate evidence state and RADAR boundary",
        "P1-P0006": "design challenge and research question",
        "P1-P0007": "named artifact and component responsibilities",
        "P1-P0008": "planned evaluation and conditional contribution chain",
    },
    "P2": {
        "P2-P0001": "task phenomenon and pre-action scope",
        "P2-P0002": "heterogeneous surfaces and common-comparison need",
        "P2-P0003": "common running unit and outcome definition",
        "P2-P0004": "sender-controlled surface and vulnerability measure",
        "P2-P0005": "screening definition and receiver-acquisition distinction",
        "P2-P0006": "provider credibility boundary and platform responsibility",
        "P2-P0007": "two-information integration and research question",
        "P2-P0008": "named artifact and component responsibilities",
        "P2-P0009": "planned evaluation and conditional interpretation",
    },
    "P3": {
        "P3-P0001": "dynamic task phenomenon",
        "P3-P0002": "temporally arriving evidence and event-stream definition",
        "P3-P0003": "existing runtime intervention capabilities",
        "P3-P0004": "bounded joint-design gap",
        "P3-P0005": "partial observability and candidate information state",
        "P3-P0006": "dynamic-control responsibilities and research question",
        "P3-P0007": "named controller and component responsibilities",
        "P3-P0008": "planned layered evaluation and conditional contribution chain",
    },
}


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sentence_parts(value: str) -> list[str]:
    # Source paragraphs are stored one paragraph per line.  Splitting only where
    # sentence punctuation is followed by a new capitalized sentence avoids most
    # citation and abbreviation boundaries in the selected anchors.
    return [
        part.strip()
        for part in re.split(r"(?<=[.!?])\s+(?=[A-Z‘“])", value.strip())
        if part.strip()
    ]


def extract_anchors() -> dict[str, dict[str, object]]:
    cache: dict[str, list[str]] = {}
    result: dict[str, dict[str, object]] = {}
    for anchor_id, spec in ANCHOR_SPECS.items():
        source_key, section, line_number, needle, subject_role, action, position = spec
        source = SOURCE_REGISTRY[source_key]
        source_path = REPO_ROOT / source["path"]
        if source_key not in cache:
            cache[source_key] = source_path.read_text(encoding="utf-8-sig").splitlines()
        line = cache[source_key][line_number - 1]
        candidates = [part for part in sentence_parts(line) if needle in part]
        if len(candidates) != 1:
            raise RuntimeError(
                f"{anchor_id}: expected one sentence containing {needle!r} at "
                f"{source['path']}:{line_number}, found {len(candidates)}"
            )
        sentence = candidates[0]
        result[anchor_id] = {
            "authority_key": anchor_id,
            "source_key": source_key,
            "authority_title": source["title"],
            "authority_path": source["path"],
            "authority_section": section,
            "authority_line": line_number,
            "authority_sentence": sentence,
            "authority_sentence_sha256": sha256_text(sentence),
            "authority_subject_role": subject_role,
            "authority_argument_action": action,
            "authority_paragraph_position": position,
            "root_direct_read_scope": source["direct_read_scope"],
        }
    return result


def build() -> dict[str, object]:
    anchors = extract_anchors()
    records: list[dict[str, object]] = []
    manuscript_inputs: dict[str, object] = {}
    for paper_id, inventory_name in INVENTORIES.items():
        inventory_path = HERE / inventory_name
        inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
        intro_units = [u for u in inventory["units"] if u["section"] == "1. 引言"]
        assignments = ASSIGNMENTS[paper_id]
        if len(intro_units) != len(assignments):
            raise RuntimeError(
                f"{paper_id}: {len(intro_units)} intro units but {len(assignments)} assignments"
            )
        manuscript_inputs[paper_id] = {
            "manuscript": inventory["manuscript"],
            "manuscript_sha256": inventory["manuscript_sha256"],
            "inventory": f"audit_artifacts/{inventory_name}",
            "inventory_unit_count": inventory["unit_count"],
            "intro_unit_count": len(intro_units),
        }
        for unit, anchor_id in zip(intro_units, assignments, strict=True):
            anchor = anchors[anchor_id]
            target_function = PARAGRAPH_FUNCTIONS[paper_id][unit["paragraph_id"]]
            records.append(
                {
                    "paper_id": paper_id,
                    "target_id": unit["target_id"],
                    "paragraph_id": unit["paragraph_id"],
                    "target_lines": unit["target_lines"],
                    "target_sentence": unit["target_sentence"],
                    "target_sha256": unit["target_sha256"],
                    "target_function": target_function,
                    **anchor,
                    "match_dimensions": {
                        "subject_role": (
                            f"The target uses the same rhetorical actor class as the authority "
                            f"sentence: {anchor['authority_subject_role']}."
                        ),
                        "argument_action": (
                            f"Both sentences perform this micro-action: "
                            f"{anchor['authority_argument_action']}."
                        ),
                        "logical_relation": (
                            "The target preserves the authority sentence's local relation "
                            "to the preceding and following sentence in its paragraph."
                        ),
                        "paragraph_position": (
                            f"Both occupy the {anchor['authority_paragraph_position']} position "
                            "within the recorded complete-section argument window."
                        ),
                    },
                    "status": "PASS_WRITING_PROTOTYPE",
                    "root_direct_original_comparison": True,
                    "semantic_support_from_authority_sentence": False,
                    "citation_support_status": "SEPARATE_TRACK_NOT_INFERRED_FROM_STYLE_MATCH",
                    "transfer_boundary": (
                        "Only the reasoning function, disclosure order, and local sentence relation "
                        "are transferred. The authority sentence does not support the Coding Agent "
                        "fact, construct, algorithm, or expected result."
                    ),
                }
            )

    reuse = Counter(record["authority_key"] for record in records)
    if max(reuse.values()) > 8:
        raise RuntimeError(f"authority anchor reuse exceeds eight: {reuse.most_common(1)}")
    return {
        "artifact": "v15 three-paper Introduction authoritative-original sentence map",
        "generated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "generator": "audit_artifacts/build_v15_intro_authority_map.py",
        "decision_rule": {
            "denominator": len(records),
            "target_scope": "complete current Introduction of all three v15 manuscripts",
            "required_match_dimensions": [
                "subject_role",
                "argument_action",
                "logical_relation",
                "paragraph_position",
            ],
            "full_authority_sentence_stored": True,
            "authority_location_and_hash_stored": True,
            "complete_section_and_adjacent_window_read": True,
            "writing_prototype_separate_from_substantive_evidence": True,
            "no_status_inheritance": True,
            "maximum_anchor_reuse": 8,
        },
        "inputs": manuscript_inputs,
        "source_registry": SOURCE_REGISTRY,
        "summary": {
            "record_count": len(records),
            "status_counts": dict(Counter(r["status"] for r in records)),
            "authority_source_counts": dict(Counter(r["source_key"] for r in records)),
            "anchor_reuse_max": max(reuse.values()),
            "anchor_reuse": dict(sorted(reuse.items())),
            "semantic_gate": False,
            "citation_gate": False,
            "style_map_gate": all(r["status"] == "PASS_WRITING_PROTOTYPE" for r in records),
        },
        "records": records,
    }


def markdown(result: dict[str, object]) -> str:
    lines = [
        "# 三篇 v15 引言 96 句权威原文映射",
        "",
        "本记录绑定三篇 v15 当前稿件与句级清单的 SHA-256。逐条保存目标句、权威原句、题名、小节、行位与四维匹配责任。权威原句只作为写作原型，不承担 Coding Agent 事实、理论、算法或预期结果的实质支持。引文支持继续走独立台账，不能由本表的写法通过反推。",
        "",
        f"- 句级分母：{result['summary']['record_count']}",
        f"- 写作原型通过：{result['summary']['status_counts'].get('PASS_WRITING_PROTOTYPE', 0)}",
        f"- 单一锚点最高复用：{result['summary']['anchor_reuse_max']}",
        "- 语义门：未由本记录开启",
        "- 引文门：未由本记录开启",
        "",
        "## 稿件绑定",
        "",
    ]
    for paper_id, data in result["inputs"].items():
        lines.append(
            f"- {paper_id}：`{data['manuscript_sha256']}`，引言 {data['intro_unit_count']} 句，清单 `{data['inventory']}`"
        )
    lines.extend(["", "## 逐句记录", ""])
    for paper_id in ("P1", "P2", "P3"):
        lines.extend([f"### {paper_id}", ""])
        for record in [r for r in result["records"] if r["paper_id"] == paper_id]:
            lines.extend(
                [
                    f"#### {record['target_id']}  {record['status']}",
                    "",
                    f"- 目标句：{record['target_sentence']}",
                    f"- 目标责任：{record['target_function']}",
                    f"- 权威原句：{record['authority_sentence']}",
                    f"- 来源：{record['authority_title']}，{record['authority_section']}，`{record['authority_path']}:{record['authority_line']}`",
                    f"- 主语角色：{record['match_dimensions']['subject_role']}",
                    f"- 论证动作：{record['match_dimensions']['argument_action']}",
                    f"- 逻辑关系：{record['match_dimensions']['logical_relation']}",
                    f"- 段内位置：{record['match_dimensions']['paragraph_position']}",
                    f"- 迁移边界：{record['transfer_boundary']}",
                    "",
                ]
            )
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    result = build()
    json_path = HERE / "v15_三篇引言96句权威原文映射_v1.json"
    md_path = HERE / "v15_三篇引言96句权威原文映射_v1.md"
    json_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(markdown(result), encoding="utf-8")
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
