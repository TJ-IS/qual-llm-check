---
otero_id: 548
otero_key: "R9HNQ87R"
title: "The Vicious Circles of Skill Erosion: A Case Study of Cognitive Automation"
authors: "Tapani Rinta-Kahila; Esko Penttinen; Antti Salovaara; Wael Soliman; Joona Ruissalo"
year: "2023"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00829"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
2023

# The Vicious Circles of Skill Erosion: A Case Study of Cognitive Automation

Tapani Rinta-Kahila , t.rintakahila@uq.edu.au

Esko Penttinen , esko.penttinen@aalto.fi

Antti Salovaara , antti.salovaara@aalto.fi

Wael Soliman , wael.soliman@uia.no

Joona Ruissalo , joona.ruissalo@aalto.fi

Follow this and additional works at: https://aisel.aisnet.org/jais

Recommended Citation Rinta-Kahila, Tapani; Penttinen, Esko; Salovaara, Antti; Soliman, Wael; and Ruissalo, Joona (2023) "The Vicious Circles of Skill Erosion: A Case Study of Cognitive Automation," , 24(5), 1378-1412. DOI: 10.17705/1jais.00829 Available at: https://aisel.aisnet.org/jais/vol24/iss5/2

ISSN 1536-9323

# The Vicious Circles of Skill Erosion: A Case Study of Cognitive Automation

Tapani Rinta-Kahila,<sup>1</sup> Esko Penttinen,<sup>2</sup> Antti Salovaara,<sup>3</sup> Wael Soliman,<sup>4</sup> Joona Ruissalo<sup>5</sup>

<sup>1</sup>The University of Queensland Business School, Australia, t.rintakahila@uq.edu.au <sup>2</sup>Aalto University School of Business, Finland, esko.penttinen@aalto.fi <sup>3</sup>Aalto University / University of Helsinki, Finland, antti.salovaara@aalto.fi <sup>4</sup>University of Agder, Norway / University of Jyväskylä, Finland, wael.soliman@uia.no <sup>5</sup>Aalto University School of Business, Finland, joona.ruissalo@aalto.fi

## Abstract

Cognitive automation powered by advanced intelligent technologies is increasingly enabling organizations to automate more of their knowledge work tasks. Although this often offers higher efficiency and lower costs, cognitive automation exacerbates the erosion of human skill and expertise in automated tasks. Accepting the erosion of obsolete skills is necessary to reap the benefits of technology—however, the erosion of essential human expertise is problematic if workers remain accountable for tasks for which they lack sufficient understanding, rendering them incapable of responding if the automation fails. Though the phenomenon is widely acknowledged, the dynamics behind such undesired skill erosion are poorly understood. Thus, taking the perspective of sociotechnical systems, we conducted a case study of an accounting firm that had experienced skill erosion over a number of years due to reliance on their software’s automated functions. We synthesized our findings using causal loop modeling based on system dynamics. The resulting dynamic model explains skill erosion via an interplay between humans’ automation reliance, complacency, and mindful conduction. It shows how increasing reliance on automation fosters complacency at both individua and organizational levels, weakening workers’ mindfulness across three work task facets (activity awareness, competence maintenance, and output assessment), resulting in skill erosion. Such skil erosion may remain obscure, acknowledged by neither workers nor managers. We conclude by discussing the implications for theory and practice and identifying directions for future research.

Keywords: Cognitive Automation, Skill Erosion, Deskilling, Knowledge Work, Artificial Intelligence, Accounting, System Dynamics, Case Study

Walter Fernandez was the accepting senior editor. This research article was submitted on August 17, 2021 and underwent three revisions.

## 1 Introduction

“When you have it automated, you don’t really start to contemplate the deep origin of things.” (An accountant who experienced skill erosion)

While machinery has been employed to automate various agricultural and industrial processes for centuries, knowledge-intensive work has long been considered an exclusively human domain when it involves manipulating abstract symbols and interpretative abilities. The emergence of cognitive technologies (Davenport & Ronanki, 2018) began to change this: enterprise systems with advanced features, robotic process automation (RPA), artificial intelligence (AI), and other technologies are taking over knowledge work procedures of a progressively unstructured and complex nature (Brynjolfsson & McAfee, 2014). Where industrial automation freed human workers’ bodies from the burden of physical labor, cognitive automation<sup>1</sup> now enables humans to “offload” their cognitive burden to machines. It provides an attractive proposition for managers: by taking over complex or otherwise repetitive knowledge work tasks that are susceptible to human error or biases, cognitive automation can result in improvements to organizational performance (Asatiani et al., 2021), innovativeness (Lou & Wu 2021), competitiveness (Davenport & Ronanki 2018), and profitability (Strich et al., 2021).

Indeed, the benefit of offloading tasks to cognitive automation is that it frees humans’ cognitive capacity for other, ideally more meaningful tasks that require different skill sets (e.g., management or IT-related skills). A typical consequence of this is that humans gradually lose understanding of the tasks they no longer manually execute, eventually becoming unable to operate without the automatic systems. This is not a problem when technologies render the lost skills truly obsolete (e.g., computer typing replacing cursive writing, or automatic transmissions for manual gearshifting in cars), but it becomes pronounced in cases where humans’ expertise is still valuable. This phenomenon is commonly referred to as skill erosion or deskilling<sup>2</sup> (Arnold & Sutton, 1998; Strich et al., 2021). For instance, the aviation field has identified pilots’ skill erosion as a key reason underlying tragic crashes, because of their inability to take appropriate action when automatic systems fail (Oliver et al., 2017). Likewise, numerous reports exist on automated GPS-based navigation systems leading to an erosion of humans’ navigation skills, leading people to become prone to getting lost when a GPS signal or automated guidance is not available (e.g., Carr, 2015; McKinlay, 2016). Especially in the context of knowledge work, many warnings have emerged about businesses rushing too quickly to automate their processes with cognitive technologies (Carr, 2015) as skill erosion can compromise the quality of service in professions such as healthcare (Goddard et al., 2012, 2014), auditing (Arnold et al., 2018; Sutton et al., 2018), and financing (Mayer et al., 2020; Strich et al., 2021). In all such domains, experts’ decreasing ability to exercise critical judgment in their work tasks exposes organizations to the risk of significant negative outcomes when automatic systems malfunction or fail to respond adequately to changes in their environment. Such situations can lead to financial losses and legal repercussions and may even cost human lives (see, e.g., Oliver et al., 2017). In addition, an organization may jeopardize its long-term competitiveness by letting its most important resource—knowledge capital—erode and stop growing (Martin De Holan et al., 2004). The concerns stated above are more troubling when cognitive automation is based on complex AI models that operate in an inscrutable manner (Asatiani et al., 2021; Lebovitz et al., 2022).

Thus, organizations are faced with the complex managerial challenge of harnessing the benefits of cognitive automation while preserving crucial human knowledge and skills. To this end, scholars have argued for the importance of striking a balance between using cognitive technologies to substitute for humans (full automation, taking humans out of the loop) and complementing humans (augmenting humans, keeping them in the loop) (Asatiani et al., 2019; Grønsund & Aanestad, 2020; Krakowski et al., 2022; Raisch & Krakowski, 2021). In the context of AI systems, Raisch and Krakowski (2021) suggested that while complementing humans with AI tends to be difficult to organize and often fails, full reliance on automation (i.e., substitution) is also problematic: it can lead to a process where essential human skills are lost over a course of time from lack of practice (p. 199). Such processes are called vicious circles—chains of effects when actions meant to improve overall performance end up hurting the organization in the long run (Garud & Kumaraswamy, 2005; Maruyama, 1963; Masuch, 1985). Senge (2006) described such situations as exhibiting dynamic complexity, which is arguably also the case in managing technology’s effect on skills. The counterpart to a vicious circle is the virtuous circle, which refers to increasingly positive effects, such as increasing wealth or the accumulation of knowledge (e.g., Maruyama, 1963).

A crucial aspect of understanding skill erosion involves unpacking the dynamic complexity related to cognitive automation’s effects on skills and revealing the potential vicious circles it may stimulate. Notwithstanding the clear relevance of this problem for information systems (IS) scholars, the discipline has not addressed it empirically; thus, skill erosion and its organizational implications remain poorly understood (Newell & Marabelli, 2015). While accounting research has attempted to measure the effect of intelligent decision aids on auditor skills (e.g., Dowling et al., 2008; Mascha & Smedley, 2007; McCall et al., 2008), it has not produced dynamic causal explanations for how cognitive technologies contribute to skill erosion in the sociotechnical context of an organization (Axelsen, 2014; Sutton et al., 2018). Such explanations would help managers recognize when skill erosion occurs in their organization, which aspects of human competence are affected the most, and what this means for the organization. With such awareness, they could consciously manage the inevitable trade-off between leveraging cognitive automation, preserving skills, and minimizing negative implications.

Against this background, we asked, (1) How does leveraging cognitive automation contribute to the erosion of skills in knowledge workers, and (2) how might such skill erosion affect organizations? For answers to these questions, we conducted an in-depth case study in a company whose reliance on an accounting software with sophisticated cognitive automation rendered its accountants—and consequently the organization as a whole—unable to perform a specific accounting process without this software. An organizational disruption ensued when the software was replaced with another, less automated one. To unfold the dynamic complexity of skill erosion, we approach the topic from the perspective of system dynamics (SD), which emerged as a suitable sensemaking device during our research process. This approach (e.g., Baker & Singh, 2019; Fang et al., 2018; Senge, 2006) allows for capturing processes and feedback loops among various sociotechnical elements within an organization and in its environment (i.e., people, work tasks, technology, legislation, etc.) that give rise to both vicious and virtuous circles related to leveraging cognitive automation in an organizational context. The vital contribution here lies in developing a new dynamic model, via the synthesis of novel findings and prior concepts, that explains how skill erosion unfolds. We validated this model by subjecting it to applicability checks (Rosemann & Vessey, 2008) with professional accountants.

## 2 Literature Review

## 2.1 Skill Erosion

Skills are often conceptualized in terms of two types of knowledge: declarative and procedural (Anderson, 1993). Declarative knowledge describes “what” a person knows, as in the ability to offer correct definitions, rules, and examples (McCall et al., 2008), while procedural knowledge is a person’s knowledge on “how” to perform a task, referring to the tacit ability to carry out that task. As such, skill erosion refers to decreases in either or both types of knowledge. Considering that skill requirements for a task may change over time, skill erosion can also refer to the inhibited development of relevant knowledge (Arnold & Sutton, 1998; Axelsen, 2014).

As a phenomenon, technology-induced skill erosion is as old as human history. Whenever humans adopt new technologies that make tasks easier—be it tools, machinery, or cooking with fire—their cognitive capacity is relieved and can be applied to new functions (Tomasello, 1999). The transitions from hunter-gatherer societies to agricultural ones accelerated skill erosion through the exponential advancement of technology and the consequent societal shifts toward increasing specializations. Although this made humans more skillful as a collective, skill erosion manifested strongly at the individual level (Harari, 2014). Later on, the widespread availability of electricity enabled unprecedented levels of industrial automation in manufacturing operations. This incentivized managers to streamline production and reduce costly human errors by automating repetitive manual work (Wallace & Kalleberg, 1982). Such “rationalization” of the labor process has been referred to as the deskilling of work because automation technologies enable organizations to achieve cost savings by hiring less skilled workers (Braverman, 1974; Wallace & Kalleberg, 1982). Although concerns about worker displacement have been raised, the subsequent rapid growth of the service sector and information economy quickly created new kinds of professions that could not be automated (Brynjolfsson & McAfee, 2014).

Indeed, skill erosion has not been considered to be problematic when technological innovations make certain skills truly obsolete (Tushman & Rosenkopf, 1992). In such cases, continuing to maintain irrelevant skills consumes limited resources and may limit one’s ability to obtain new, more relevant skills. “Reskilling” or “upskilling” (McGuinness et al., 2019) often manifests as the development of entirely different types of skills, such as those related to management or social interactions (Agnew et al. 1997; Schuppan, 2014), IT use (Bravo, 2015), and analytics (Zuboff, 1988). However, in contexts where both traditional manual skills and new technological skills are required, domain experts may face difficult trade-offs regarding the skills they choose to develop and maintain given their time constraints (see Beane, 2019).

## 2.2 Skill Erosion and Cognitive Automation

The emergence of cognitive automation has further complicated the picture by encroaching into the territory of knowledge work, where human cognition has traditionally reigned supreme. Cognitive technologies like expert systems, RPA, and AI enable effective automation of a growing pool of tasks requiring interpretation and abstract thinking (Davenport & Ronanki, 2018). However, algorithms that provide intelligent decision support or transfer decision-making processes entirely from humans to IT have been found to disrupt knowledge workers’ role identity, engendering concerns among workers about losing their expert status and becoming irrelevant (Davis & Hufnagel, 2007; Strich et al., 2021).

Such concerns are warranted—research on auditing support systems suggests that a high reliance on intelligent decision aids can lead to the unintended erosion of skills even among highly experienced auditors (Arnold & Sutton, 1998; Axelsen, 2012; Dowling et al., 2008; Mascha & Smedley, 2007). This reliance, referred to as “technology dominance,” typically emerges when the work task is complex, and the user is familiar with the system and perceives it to be a good cognitive fit (Arnold & Sutton, 1998, p. 183). The intelligent system takes over the detail-oriented work that helps humans develop and maintain their expertise. Hence, a “degeneration effect” emerges in which one’s accumulated expertise gradually disappears (Carr, 2015). Similar effects have been found in healthcare (Goddard et al., 2014), insolvency proceedings (Arnold et al., 2006), knowledge management (McCall et al., 2008), and word processing (Galletta et al., 2005).

Concerns related to skill erosion have become particularly evident in high-reliability contexts, such as aviation and healthcare, where cognitive automation brings reliability benefits but human experts remain responsible for outcomes. For instance, advanced cockpit automation systems have been linked to aircraft crashes as continued reliance on these systems may contribute to pilots’ skill erosion, manifesting in impaired situational awareness and a muted ability to respond to crises in real time (Oliver et al., 2017). Further, scholars have observed “automation bias” in various contexts—a tendency to favor the system’s suggestions when faced with contradictory evidence (Goddard et al., 2012, 2014; Jussupow et al., 2021; Parasuraman & Manzey, 2010; Skitka et al., 2000). Because these systems are generally reliable, their operators’ trust in them can grow so strong that it manifests as complacency: the assumption that “all is well” without understanding the actual state of the matter (Merritt et al., 2019; Parasuraman & Manzey, 2010) or “a feeling of calm satisfaction with your own abilities or situation that prevents you from trying harder” (Cambridge Dictionary, 2023).

The discussion above suggests that skill erosion is more likely to occur when IT use echoes mindlessness, i.e., “a state of reduced attention that tends to lead to mechanically employing cognitively and emotionally rigid, rule-based behaviors” (Fiol & O’Connor, 2003, p. 58). Presumably, skill erosion could be mitigated through mindfulness, i.e., a cognitive state that reflects alertness, dynamic awareness, and attention to detail (Butler & Gray, 2006; Langer, 1989). In the context of IT, a mindful state involves being conscious about one’s IT use and exploring and exploiting the full spectrum of an IT’s capabilities (e.g., explanations, see Arnold et al., 2006) instead of becoming rutted in the same patterns (Thatcher et al., 2018). Although users’ reliance on cognitive automation like intelligent decision aids has been studied (e.g., Hampton, 2005), the extent of associated mindfulness/mindlessness has not been specifically considered in relation to skill erosion. In general, only a few empirical studies have investigated the extent to which reliance leads to skill erosion (Sutton et al., 2018; Triki & Weisner, 2014). Thus, the causal mechanisms that determine how skill erosion happens over time as a result of automation remain largely unexplored (Axelsen, 2014).

## 2.3 Skill Erosion as a Managerial and Sociotechnical Challenge

Recent IS literature has highlighted skill erosion as a critical managerial challenge of our times (Burton-Jones, 2014; Faraj et al., 2018; Mayer et al., 2020; Newell & Marabelli, 2015; Rinta-Kahila et al., 2021; Strich et al., 2021), exploring how to harness the transformative benefits of emerging IT, on the one hand, and how to ensure the maintenance of critical human skills on the other. The ways this can be managed are still unknown due to the narrow scope of prior empirical research. Sutton et al. (2018) noted that we have little understanding of how a technology’s dominance “takes hold, how technology affects expertise development. The how and why are critical pieces that are needed if we are to have a chance to counteract these effects and keep the human relevant in professional decision-making environments” (p. 17, emphasis added). Previous empirical studies on skill erosion (e.g., Dowling et al., 2008; Mascha & Smedley, 2007; McCall et al., 2008) have been fairly reductionistic, mainly considering the direct effects of task characteristics (e.g., task complexity) and the perceptions of individual workers (e.g., familiarity and cognitive fit with the technological aid) via onedirectional factor-based models. While these studies have scoped out the contextual origins of such factors, organizational policies, and the role of technological agency, this ignores the nature of skill erosion as a dynamically complex phenomenon: it occurs gradually over time and is often unacknowledged by its subject until it is too late.

Professional decision-making environments are sociotechnical in nature, as they incorporate both social (e.g., work processes, people, hierarchies) and technical (e.g., data, IT system) elements (Alter, 2013; Lyytinen & Newman, 2008; Sarker et al., 2019). The interaction among these elements (e.g., workers using technologies to accomplish work tasks) reflects a “work system” that produces outputs and is shaped by surrounding organizational and environmental conditions (Alter, 2013). This view highlights that IS use phenomena should be investigated by probing the dynamic interactions among human and machine participants occurring within an organizational setting.

The consideration of machine agency—the fact that technologies have a degree of autonomy in performing work tasks—is especially important in capturing the ways in which humans may become reliant on cognitive automation (and thus be subject to skill erosion; Arnold & Sutton, 1998). Related to this idea, human workers are seen as part of the organizational work systems that generate business results instead of just as users of technology. Similarly, work tasks and processes are interacting parts of the work system, rather than merely the context in which a technology is being used. In essence, the elements are dynamically interrelated rather than having only one-way relations. Their interactions are not static but “evolve over time through a combination of planned change and emergent (unplanned) change” (Alter, 2013, p. 76), which is congruent with the gradually evolving and latent nature of skill erosion. Accounts of feedback loops that yield negative progressive effects, such as the loss of situational awareness (Parasuraman & Manzey, 2010) or the fragmentation of organizational knowledge (Garud & Kumaraswamy, 2005), indicate the use of a systems perspective (Burton-Jones et al., 2015; Senge, 2006) in relation to the topic of skill erosion. Hence, to capture the phenomenon’s dynamic and emergent aspects, we turn to the systems perspective to analyze mutually influencing, time-delayed interactions among different sociotechnical elements.

## 3 Theoretical Underpinnings

## 3.1 The Systems Perspective

The systems perspective has its roots in general systems theory and cybernetics (Ashby, 1957; Von Bertalanffy, 1968; Boulding, 1956), which postulate that virtually all phenomena exist in a network of interrelated and interdependent elements, together forming a system that exhibits common patterns, behaviors, and properties. It goes beyond one-directional or sequential views of the effects of entities, factors, and events reflected in variance- and process-oriented research to consider how wholes and their parts interact in a dynamic and nonlinear manner (Boulding, 1956; Burton-Jones et al., 2015). A system may refer to a human-made technical system (e.g., an IT system), a biological system (e.g., human immune system), a work system (e.g., a department in an organization), or a societal system (e.g., a political or economic system), to name a few. IS-use phenomena tend to take place in open systems—such as organizations— which continuously interact with their environment and other systems, making them dynamically complex (Fang et al., 2018, p. 1305). Open systems consist of concepts such as input, output, and feedback, which, in organizations, are reflected as sociotechnical elements, such as goals, decisions, behaviors, work processes, and technologies (Alter, 2013; Sterman, 2001).

Senge (2006) suggests that the systems perspective is particularly helpful for understanding complex managerial problems. Building on these ideas on why well-meaning managerial actions (e.g., augmenting workers with cognitive technology) produce unintended negative outcomes (e.g., skill erosion), he argues that with dynamically complex phenomena the effects of the system are emergent. Thus, the same action may have dramatically different effects in the short and long term and the consequences of the action are different in different parts of the system (Senge, 2006, p. 71). If managers fail to acknowledge this, they may resort to obvious or easy solutions that improve things in the short run but end up backfiring in the long run (see, e.g., Drummond, 2008; Rinta-Kahila et al., 2022). A key challenge for managers, then, lies in identifying “leverage points” in the system, where small changes “lead to lasting, significant improvement” (p. 64). These ideas resonate with the complex, latent, and gradually occurring nature of skill erosion. The systems perspective has yielded various different strands of approaches and methodologies, and the IS field has a long tradition with many of them (Burton-Jones et al., 2015). Senge’s work draws on system dynamics, a methodology to understand, model, and analyze complex and systemic social and managerial issues.

## 3.2 System Dynamics

System dynamics (SD) was initially employed for generating mathematical models and simulations (Forrester, 1961) but has since become a popular theorizing approach among IS and management researchers (e.g., Baker & Singh, 2019; Fang et al., 2018; Martinez-Moyano et al., 2014; Rinta-Kahila et al., 2023). These disciplines have applied SD especially for “conceptual (non-mathematical) modeling to ... represent findings from interpretive case research” (Baker & Singh, 2019, p. 4). Similarly, it emerged as a suitable sensitizing lens during our research process as we attempted to integrate the emerging findings from our case study.

SD reflects the structural principles of general systems theory. It posits that dynamic processes in sociotechnical systems function via feedback loops among different elements, expressing “reciprocal (i.e., circular) and temporal (i.e., time variant) causality” (Fang et al., 2018, p. 1305). The trajectories of a sociotechnical system’s processes may be captured in “state variables” (e.g., the accrual or erosion of skills). This accumulated history (e.g., an individual’s skill level) has implications for the system’s future behavior.

In SD, a system is represented as a causal loop diagram with reinforcing (i.e., self-sustaining) and/or balancing (i.e., self-limiting) effects between system elements (Senge, 2006). While balancing loops correct for the system’s deviation from its initial state, reinforcing loops escalate the deviation and push the system further away from its original state. This progressively generates positive or negative effects, depending on the direction of the change (increase vs. decrease) and what is considered to be an optimal system state. Several generic system structures—system archetypes—exist that serve as a basis for modeling systemic behaviors (Kim, 1992; Senge, 2006). As one prominent example, the Limits to Growth archetype (Meadows et al. 1972) demonstrates how growth in population and capital (a reinforcing loop) cannot go on indefinitely due to the limited resources and endurance of the natural world (a balancing loop).

We believe that SD principles and existing system archetypes (Kim, 1992; Senge, 2006) present a potentially fruitful basis for explaining and addressing organizational skill erosion. Hence, in this paper, we operationalize Senge’s (2006) SD approach, in particular, building on an archetype called Shifting the Burden (Kim, 1992; Senge, 2006), shown in Figure 1.

This archetype involves an underlying problem that generates problem symptoms that call for attention. However, addressing this problem is difficult, “because it is obscure or costly to confront” (Senge, 2006, p. 103). Therefore, people innocently “shift the burden” to alternative, so-called symptomatic solutions—easy fixes which seem highly efficient but come with two negative side effects (Kim, 1992, p. 22). First, symptomatic solutions divert attention away from the underlying problem. Second, they “cause the viability of the fundamental solution to deteriorate over time, reinforcing the perceived need for more of the symptomatic solution” (Kim, 1992, p. 22). Over time, the system loses its ability to address the underlying problem. One example is using caffeine to resolve the problem of insufficient energy. By relying on a symptomatic solution in the short term through caffeine intake, this solution diverts attention away from more fundamental solutions to energy deficiency that require more effort and do not immediately show results (e.g., physical exercise or good sleep hygiene), making one increasingly dependent on caffeine. In the language of SD, the two alternative solutions (i.e., symptomatic and fundamental solutions) represent balancing loops (B1 and B2) that compete for dominance. The symptomatic solution gives rise to a reinforcing loop (R1), which weakens the fundamental solution.

Senge (2006, p. 110-112) recognizes that “symptomatic” and “fundamental” should be considered as relative terms that help to identify different ways of addressing a given problem. As such, symptomatic solutions are not purely negative and are, in fact, sometimes needed. But they should always be combined with fundamental solutions (e.g., drinking caffeine moderately while exercising sufficiently). Moreover, Senge acknowledges that generic system archetypes serve as a mere starting point for understanding the unfolding of complex phenomena— they need to be adapted in the context of the topic being studied. Our SD approach is sociotechnical in the sense that it assumes that knowledge work activities take place in organizational settings and involve dynamic and reciprocal interactions among human (social) and machine (technical) participants that influence (and are influenced by) organizational and environmental elements. Humans may perceive their work tasks and cognitive technologies in certain ways and these perceptions may guide their behavior, further influencing perceptions via the feedback effect.

![](/api/attachments/R9HNQ87R/fulltext/images/b9ac72a3b5cb5b56da64762c181b26f4f20290debd140def892a4431af3ce92c.jpg)  
Figure 1. Shifting the Burden Archetype

## 4 Research Methods

Research into the interactions between emerging IT and knowledge workers’ skills involves several empirical challenges. Firstly, it can prove challenging to examine skill erosion with “a traditional scientific method” (Arnold & Sutton, 1998, p. 192) such as a survey, because one cannot directly observe cognitive skills and processes, let alone their changes over time. Cognition and skills may, however, be determined through retrospective accounts gathered in welldesigned case studies (Hansen et al., 2019). Furthermore, the implication of skill erosion for an organization’s perceived competence and reputation may render many organizations reluctant to collaborate with researchers and disclose information about its occurrence. However, we were fortunate to gain access to an organization amid a disruption wherein workers, whose skills had eroded through years of relying on an automatic system, were struggling to carry out their tasks manually in the wake of the decommissioning of that system. The existence of this erosion appeared as an unexpected finding during a more general inquiry we were conducting into the effect of automation on knowledge work. We followed this revealing thread by carrying out a case study at this organization, focused on the topic of skill erosion. Conducting a case study using a single-case research design can be valuable if the case is “revelatory”: if it provides the researcher with access to a phenomenon previously inaccessible to scientific inquiry (Yin, 2018, p. 50). The serendipitous emergence of this topic during the initial interviews afforded unique access for examining skill erosion that had already occurred and produced tangible consequences for the organization—the sort of phenomenon that managers would be wary of disclosing frankly to any external parties. Furthermore, a single-case study is an ideal method for investigating complex research questions that deal with the processes and underlying reasons for the research phenomenon (here, skill erosion) in combination with interactions between human, organizational, and technical factors in a well-defined work context.

## 4.1 The Case Organization

AccComp<sup>3</sup> is an international accounting firm based in Northern Europe with nearly 1,000 employees and annual revenues of around €130 million. Founded in the 1960s, it specializes in the development of digital business solutions and financial processes. The case site was AccComp’s Finance Process Services (FPS) Center, a unit handling consolidated support activities that include the delivery of outsourced accounting services to a broad client base, comprising organizations in several industries (energy companies with complex accounting needs are especially prominent clients). Given AccComp’s strong reputation for providing technical consulting and highquality services, and the generally rapid pace at which accounting tasks are being automated, this company’s shared-services center was a highly suitable context for our case study.

We initially set out to learn about the challenges that accountants face in their work, how automation addresses these challenges, and how accounting professionals perceive the effects of these developments on their professional identity and skills (see Appendix A, Inquiry 1). We found that after seven years of benefiting from FAMSyst—a software application specifically designed to automate fixed asset management (FAM) tasks—AccComp decided to decommission the system to simplify and improve the uniformity of its IT architecture. The accountants were lamenting the reduction of process automation in the organization since this resulted in an increase in their workloads. Because the accountants had forgotten how to perform manual fixed asset accounting, the organization enforced a laborious process of learning by doing to regain that lost competence. This revelation led us to focus more closely on the phenomenon of skill erosion in the context of fixed asset management.

## 4.2 Fixed Asset Management

Fixed asset management (FAM) accounting in the country where AccComp is based is notoriously complex due to substantial differences in reporting practices between organizations’ accounting and taxation domains. Reporting for the latter involves several tax forms whose completion logic varies case by case. This makes tracking and matching depreciations especially challenging. The possibility of differences in depreciation sums between a company’s accounting and tax reporting elucidates FAM’s complexity: when such differences accumulate over a number of years without adjustment, a significant accounting mismatch may result, and this is difficult to trace back to the source when rectification is finally attempted. The FAM legislation and tax-agency regulations provide little practical guidance regarding the depreciation figures required for tax forms and how these align with accounting figures. Rather, competence comes from practical experience. According to Daniel, a domain expert, FAM skills are essential to professional accountants: “managing depreciation … in principle, every accountant should be able to handle that.” Although some companies choose to carry out FAM manually, software automation such as FAMSyst becomes an attractive option when the number of fixed asset items is large.

## 4.3 Data Collection

The case study involved 25 semi-structured interviews, with 16 participants in all, and the collection of secondary data online. The data-collection process can be divided into four overlapping lines of inquiry over the course of the study. Table 1 summarizes the collected interview data and Appendix A provides the interview protocols.

Inquiry 1: Identification of the research problem and general orientation to the organizational context. In November 2016, we conducted initial interviews with 13 informants at AccComp, including accountants and managers involved in accounting. Guided by a semi-structured interview protocol, our conversational-style interviews with 13 informants involved discussion about how the informants perceive accounting automation and what implications leveraging automation has on maintaining skills. These interviews sensitized us to the trade-offs between leveraging automation and preserving domain skills. Further, to our surprise, they revealed that skill erosion had already taken place in the company: three experienced accountants told us they were now struggling to perform FAM tasks without the help of automation. These accountants alluded to lacks in their declarative and/or procedural knowledge; one of them (Sue) reflected about “feeling uncertain regarding how one should carry out the task” after automation was no longer accessible.

Inquiry 2: Contextual understanding of the environment, task, and automation technology from the angle of skill erosion. The abovementioned revelatory thread led us to specifically focus our investigation on how skill erosion had occurred in the organization. Considering the organizational setting of our study, previous writings on sociotechnical systems (Alter, 2013; Lyytinen & Newman, 2008) along with prior research on skill erosion (e.g., Arnold & Sutton, 1998) sensitized us to relevant concepts. First, we wanted to understand what makes FAM tasks and activities (and the information within) complicated enough to create a market demand for customized FAM software (i.e., technology). To study how FAMSyst automatically handled the relevant processes, we prepared a semi-structured interview protocol for interviewing managers at FAMComp, the IT solution provider behind FAMSyst and related services. At this stage of inquiry, we also collected nine documents from FAMComp’s website (28 pages of text) and watched online videos that illustrate how FAMSyst works. Subsequently, we strengthened our understanding of the task by interviewing another domain specialist, the director of the member services of the National Association of Accounting Firms, about FAM skills that accountants should possess.

Inquiry 3: Focus on the RQ: How did skill erosion occur via the interaction of the task, technology, and participants in the studied context? We then returned to AccComp in search of an explanation for the accountants’ skill erosion. We developed a semi-structured interview protocol to capture relevant organizational policies and practices related to FAMSyst’s use at AccComp, the evolution of accountants’ perceptions of the automated operations and their work tasks over time, events and issues that occurred before FAMSyst was implemented, events and issues arising during its use, and the accountants’ postdiscontinuance experiences. We requested follow-up interviews with interviewees who had been affected by FAMSyst’s decommissioning. We conducted a second interview with the two accountants (Sue and Amy). We also held additional interviews with their team leader (John) and the head of AccComp’s FPS center (Carol), who managed this unit. Both John and Carol had hands-on fixed asset management experience and were able to offer a more holistic, managerial perspective on the events of interest. This afforded triangulation by “member checking” (Trauth & Jessup, 2000). This time we tried to specifically probe the informants’ perceptions about whether cognitive automation had impacted their skills. We did this unassumingly and did not bring up the term “skill erosion” until or unless the informants did so (e.g., John acknowledging that “our skills had eroded”). To complement our understanding, we retrieved two press releases describing the latest system replacement (from AccComp’s and the system provider’s website).

Inquiry 4: Finer-grained understanding and validation of conclusions. Following numerous iterations of analyzing data gathered in Inquiries 1, 2, and 3 and after reflecting on the findings in light of the literature, we conducted additional follow-up interviews to validate our findings, informed by the system-dynamics lens that had emerged during the analytical process. We interviewed the team leader again and the two accountants from the previous round, along with an accountant (Mary) who had taken part in the first round of interviews. Thus, we gained a deeper understanding of the events and could further triangulate the findings, increasing our confidence in their validity.

Most interviews were held on the case company’s premises, but intervening events necessitated handling some interviews over Skype in the latter stages of the research. Every interview was recorded and transcribed. In total, the data-gathering process yielded 156,802 words of transcribed interviews and 11 online documents.

Table 1. The Interviews and Participants

<table><tr><td>Organization</td><td>Interviewee</td><td>Participated in Inquiry # *</td><td>Role</td><td>Tenure at AccComp</td><td>Interview time and length</td></tr><tr><td rowspan="13">AccComp (subject of Inquiries 1, 3, and 4)</td><td>Sue</td><td>1, 3, 4</td><td>FAM accountant</td><td>15 years</td><td>Nov. 2016 (75 min)Mar. 2017 (55 min)Sep. 2020 (62 min)</td></tr><tr><td>Amy</td><td>1, 3, 4</td><td>FAM accountant</td><td>8 years</td><td>Nov. 2016 (87 min)Mar. 2017 (51 min)Aug. 2020 (26 min)</td></tr><tr><td>Mary</td><td>1, 4</td><td>Accountant (with some FAM duties)</td><td>5 years</td><td>Nov. 2016 (82 min)Aug. 2020 (55 min)</td></tr><tr><td>Donna</td><td>1</td><td>Accountant (with some FAM duties)</td><td>1 year</td><td>Nov. 2016 (67 min)</td></tr><tr><td>Betty</td><td>1</td><td>Accountant (with some FAM duties)</td><td>2 years</td><td>Nov. 2016 (75 min)</td></tr><tr><td>Susan</td><td>1</td><td>Accountant</td><td>4.5 years</td><td>Nov. 2016 (72 min)</td></tr><tr><td>Patricia</td><td>1</td><td>Accountant</td><td>15 years</td><td>Nov. 2016 (62 min)</td></tr><tr><td>Jennifer</td><td>1</td><td>Accountant</td><td>1 year</td><td>Nov. 2016 (68 min)</td></tr><tr><td>Linda</td><td>1</td><td>Accountant</td><td>1 year</td><td>Nov. 2016 (69 min)</td></tr><tr><td>John</td><td>1, 3, 4</td><td>Team leader; FAM accountant</td><td>9 years</td><td>Nov. 2016 (70 min)Apr. 2017 (48 min)Apr. 2020 (76 min)May 2020 (61 min)</td></tr><tr><td>Carol</td><td>1, 3</td><td>Head of FPS</td><td>3 years</td><td>Nov. 2016 (56 min)Jun. 2017 (46 min)</td></tr><tr><td>Sara</td><td>1</td><td>Manager</td><td>4.5 years</td><td>Nov. 2016 (85 min)</td></tr><tr><td>Roger</td><td>1</td><td>Manager</td><td>4.5 years</td><td>Nov. 2016 (55 min)</td></tr><tr><td rowspan="2">FAMComp (subject of Inquiry 2)</td><td>James</td><td>2</td><td>Sales manager</td><td>N/A</td><td>Mar. 2017 (30 min)</td></tr><tr><td>Mark</td><td>2</td><td>CEO/owner</td><td>N/A</td><td>Mar. 2017 (25 min)</td></tr><tr><td>National Association of Accounting Firms (subject of Inquiry 2)</td><td>Daniel</td><td>2</td><td>Director of Member Services</td><td>N/A</td><td>Apr. 2020 (32 min)</td></tr><tr><td>Totals:</td><td>16 informants</td><td></td><td></td><td></td><td>25 interviews (1,490 min)</td></tr><tr><td colspan="6">*Inquiry #1: Identification of the research problem and general orientation to the organizational context.Inquiry #2: Contextual understanding of the environment, task, and automation technology from the angle of skill erosion.Inquiry #3: Focus on the RQ: how did skill erosion occur via the interaction of the task, technology, and participants in the studied context?Inquiry #4: Finer-grained understanding and validation of conclusions</td></tr></table>

## 4.4 Data Analysis and Theory Generation

Our analytical approach reflected an abductive sensemaking process where we leaped between data and existing theory seeking plausible explanations for the phenomenon (Van Maanen, 1979; Mees-Buss et al., 2020; Sætre & Van de Ven, 2021). We iteratively read the data, coded it, looked for themes and patterns in the data, and wrote a narrative that faithfully conveyed our interpretation of what was going on in the data. First, two of the authors performed open coding (Corbin & Strauss, 2015) of the data in Atlas.ti software by assigning descriptive codes to portions of the corpus. Capturing relevant events and the informants’ reflections on them allowed us to construct a rich narrative (Pentland, 1999) of the events that influenced skill erosion at AccComp. Figure 2 provides a timeline of the case events.

The two coders reviewed each other’s codes, compared them, and discussed potential themes potentially arising within them. They then presented the codes along with exemplary quotes from the data and analytical interpretations to the rest of the team. We reflected and debated the emerging concepts in light of existing literature on skill erosion and prior conceptualizations of sociotechnical elements (Alter, 2013; Sarker et al., 2019).

![](/api/attachments/R9HNQ87R/fulltext/images/dec9ddd665c21604299565b8b9e079a2d3a697c57269ddf7f0aa8a59210de198.jpg)  
Figure 2. Timeline of Events

We found that some concepts resonated with those familiar from previous theories (e.g., “complacency,” “task complexity,” and “coping”), while others appeared to be novel. For instance, we inductively identified three distinct facets of the FAM process that required conscious effort from workers. We labeled these facets “activity awareness,” “competence maintenance,” and “output assessment,” i.e., modes of working where the worker is consciously engaged in the task. Through an abductive process, we connected these facets to the concept of mindfulness in action, which we termed mindful conduction.<sup>4</sup> Moreover, drawing on the notion of machine agency (Alter, 2013), we conceptualized automation reliance as the extent to which the three facets were dependent on cognitive automation (e.g., John on activities: “FAMSyst provided readily calculated depreciation differences and everything else, you just input the information correctly and it did all that for you”)<sup>5</sup>.

Further, we analyzed the relationships among different sociotechnical elements. We found a connection between skill erosion and a decrease in each facet of mindful conduction. For instance, one accountant described having assessed FAMSyst’s outputs at “an approximate level only, and mainly just trusting that they will be correct” and pondered whether such a cursory involvement could have resulted in their inability to diagnose issues that emerged later. Vice versa, there was also a connection between the skillrecovery process and becoming mindful of each of the three facets: another accountant explained how manual validation of tax report figures via Excel was “painstaking” but helped provide “clarity to the entire FAM process” and reduced the need to rely on the software’s “readily formatted statements.”

Considering the latent and often unconscious nature of skill erosion, we maintained a healthy suspicion of the informants’ statements. Throughout the data collection process, and especially during the final round of inquiry, we carefully raised any inconsistencies or logical dilemmas that we had identified in the informants’ prior accounts. The suspicious mindset concerned our own interpretations too: as concepts emerged, we debated them among ourselves and tested them against the dataset, oftentimes in an attempt to falsify them. Via the online documents, we were able to triangulate the informants’ testimony about the system’s functionality and some key events discussed in the interviews. Interim analysis results were reported and discussed in meetings among the authors until we settled on a final coding structure that faithfully reflected the data and communicated our interpretations (see Appendix B).

mindlessly. Similarly, automation reliance can be high in terms of what responsibilities are handed off to automation, yet people may still be highly mindful and scrutinize what the automation is doing.

In striving to integrate the emerging concepts, we produced various provisional models and theories, which we then tested by going back into the data. We held workshops in which all the authors drew diagrams of possible cause-effect relationship networks that could explain the phenomenon of skill erosion in a way that was plausible and faithful to the empirical data. We ultimately integrated our concepts using SD, as it helped us capture the feedback loops and emergent outcomes apparent in the data. During an abductive process (Sætre & Van de Ven, 2021), we deemed the Shifting the Burden archetype (Senge, 2006) to be a potentially fitting basis for our theorization. We thus engaged in a systematic process of SD model construction following Senge’s (2006) guidelines on applying system archetypes, resulting in a model that presents an explanation for the latent skill erosion in the sociotechnical work system of an organization.

To ensure that the SD model holds relevance for practice and exhibits applicability beyond the limits of our empirical case, we conducted applicability checks in line with Rosemann and Vessey’s (2008) guidelines (see Appendix E for details). Through applicability checks, researchers can subject their theories, models, frameworks, or other research outputs under evaluation to checks by practitioners knowledgeable about the phenomenon of study. The model passed these checks, indicating that it addresses a problem that is important for practitioners in an understandable manner and provides insights that are applicable to their work.

## 5 Findings

Following the lens of SD, we explain the basic skill erosion mechanism via the Shifting the Burden archetype. We then expand this to a more comprehensive model by incorporating the effects stemming from various sociotechnical elements. In line with Alter (2013), we consider the overall work system as encompassing work processes and activities, participants, information, technologies, services to customers, organizational policies, and the external environment—all of them in interaction with each other.

## 5.1 The Problem Symptom: The Burdensomeness of Fixed Asset Management

For the decade prior to 2008, AccComp’s business unit managed fixed assets via a customized module linked to its commercial enterprise resource planning system. Since the overall system was not designed to meet the national FAM requirements, and because accounting practices and the national taxation principles are in many ways incompatible (cf. Section 4.2), the management of fixed assets required extensive and time-consuming manual work from accountants. This problem symptom—the burdensomeness of the (manual) FAM task—formed the prime mover for two basic solutions of the Shifting the Burden archetype.

## 5.2 The Fundamental Solution: Reducing Work Burden via Mindful Conduction

We identified “mindful conduction” as the fundamental solution to the problem symptom. A complex and time-taking task calls for mindful conduction to ensure accurate execution and accountability, such as attention to task activities, brushing up on domain competence, and critical examination of task outputs. Accountant Donna discussed the importance of such mindfulness in FAM: “matching [accounts] and verifying [figures] is the necessary part of this work, while not always enjoyable, it makes you [notice mistakes] like ‘oh damn, why have I done it in this way.’”

Specifically, three facets of mindful conduction in FAM tasks emerged from the interviews: activity awareness, competence maintenance, and output assessment. Activity awareness involved the execution and supervision of task activities, including optimizing depreciations between accounting and taxation and keeping track of the differences over time. Competence maintenance, in turn, reflected upholding domain competence, which involved maintaining an understanding of the current tax legislation to make interpretations of acceptable depreciations. Finally, output assessment involved ensuring that reports were correct and compliant with the legislation before sending them to the tax office.

Embracing mindful conduction via the three facets represents a fundamental solution to the burdensomeness symptom because, while it requires effort and does not offer short-term benefits, one becomes increasingly skilled over time and through repetition. This creates a positive feedback loop, where a delay appears due to the time needed for learning. As the skill level increases, the task becomes “automatic” (Senge, 2006, p. 153) to carry out, which alleviates the task’s burdensomeness. For instance, as accountants build and maintain their skills by gathering experience in the mindful interpretation of different depreciation scenarios, they become increasingly fast and proficient in forming judgments about new scenarios that emerge. This solution to FAM’s burdensomeness involves consciously executing or supervising the process and assessing its outputs as well as obtaining, processing, and sharing relevant domain knowledge (i.e., activities and information). As an SD component, mindful conduction represents a balancing mindfulness loop (B1) which reduces task burdensomeness via the accrual of skill.

## 5.3 The Symptomatic Solution: Shifting the Work Burden via Reliance on Automation

While mindful conduction is desirable from the skill maintenance standpoint, it alone may not represent a practical solution to task burdensomeness in an increasingly automated world. Roger, the vice president of AccComp, stated: “Artificial intelligence and automation are important sources of business efficiency … we need people who want to leverage these new technologies, that’s the name of the game today.”

Indeed, performing FAM manually posed a significant burden on the accountants and ate up the organization’s resources. When AccComp implemented a new accounting system (MainSyst) in 2008, they decided to alleviate the FAM burden by complementing the new system with a specialized fixed asset management software, FAMSyst. AccComp entrusted the transitioning project’s management to team leader John, an experienced accounting-outsourcing specialist who had just commenced working at AccComp. Having a good FAM understanding and awareness of the task’s complexity, he was enthusiastic about FAMSyst: “We were excited to find out that there exists a system that could do all this for us, freeing up time for other things.”

With FAMSyst, accountants specified the depreciation methods in the system and fed in the acquisition prices of the company’s fixed assets (IT items, cars, buildings, machinery, etc.). FAMSyst calculated their depreciation and produced reports for accounting, taxation, and auditing. Though FAMSyst took over the execution of some key task activities, it included an explanation function for user support, through which it displayed the logic by which the fixed asset data was processed. This functionality provided the accountants with a means to observe and understand the automatically conducted task activities. Furthermore, swift software updates in response to legislative changes kept the system automatically up to date. To support its human users’ domain competency, FAMSyst informed them of such updates and the reasons for them; also, FAMComp provided training for its clients. Moreover, the reports that FAMSyst produced were readily compliant with national standards and legislation—they were even formatted to resemble the actual tax form. The system’s output presented further information to aid in tax report verification, in the form of answers to potential tax office inquiries. In sum, although FAMSyst invited its users to rely on it on various fronts of the work task, it also provided explanation functionalities that supported its users’ mindful conduction. AccComp’s leaders had some awareness of the importance of maintaining adequate domain expertise internally. To ensure that accountants retained their mindfulness of the task while leveraging FAMSyst, they appointed one accountant as the FAMSyst key user, responsible for making sure the other

AccComp accountants’ knowledge of the applicable FAM rules remained up to date. The key user participated in external training sessions and then shared the new knowledge with the rest of the team, via internal training.

The accountants were delighted to find that FAMSyst performed its job impeccably. Sue, a seasoned accountant with extensive fixed asset experience and 15 years with AccComp, lauded the system’s abilities: “It produced a form that is exactly like the tax-office one, precisely the same numbers, so you didn’t have to think about anything at all … everything came out ready-prepared.” Communication with tax authorities, which previously had been a routine part of the accountants’ work, diminished to a minimum after the system’s uptake, because FAMSyst eliminated (previously frequent) errors and unclear elements in reports. In the absence of negative performance consequences, the accountants’ reliance on the system increased. John noted: “We had extremely solid trust in it, and it was pretty much the case that if the software showed that this is how you need to report [something], then we would not start to question that.” FAMSyst indeed did everything correctly, irrespective of whether its users understood what it was doing:

Since the basic use is pretty simple and you can count on the software [being correct], it might be the case that someone would use it without really understanding much of what is happening … The software makes it possible that one could use it even with quite limited [FAM] knowledge. (FAMComp’s sales manager, James)

Against this background, we identified automation reliance as a symptomatic solution: shifting the burden to automation immediately alleviated the problem symptom of (perceived) task burdensomeness although it did not address workers’ fundamental need to master the task. Informants across the board spoke on the importance of being mindful while relying on automation, Jennifer stated that: “[Automation] is good for routine work. But it does not remove the need [for human workers] to keep checking what is going on.” In the same vein, Susan reflected: “[with automation] you have more time to analyze the figures instead of being encumbered by manual work … With the time saved [from relying on automation], you could develop a better in-depth understanding about the subject matter.”

Still, reliance may become excessive when automation yields benefits such as the reduction of errors or time savings, affording better or faster services to (internal or external) customers. The more that workers rely on automation, the less burden they experience from the task. Therefore, automation reliance represents the archetype’s competing balancing loop, which we refer to as the reliance loop (B2), an alternative or complementary pathway for reducing task burdensomeness.

## 5.4 The Side Effect: Complacency

FAMSyst provided significant time savings and allowed accountants to focus their efforts on other tasks. Now, more could be achieved with the same human resources. Unfortunately, symptomatic solutions tend to come with negative side effects. While the accountants’ work satisfaction improved via FAMSyst’s introduction, heavy reliance on the system lulled the accountants into what could be characterized as automation complacency. The potential danger of becoming growingly reliant on the system did not strike them as a cause for concern. Sue stressed that “there was no danger, because [FAMSyst] worked. It worked!” Another accountant, Amy, stated: “No, I was not [concerned]—no worries whatsoever.” Complacency had implications for the extent of mindfulness the accountants exhibited in their task performance/completion. This manifested in three ways, each one related to a facet of mindful conduction: (1) the accountants’ awareness of the task activities decreased, (2) their motivation to maintain and improve their domain competence deteriorated, (3) and the previously rigorous approach to assessing outputs evaporated.

First, regarding the activity awareness facet, once the accountants had gotten used to their new automated tool, they found little need to consider what was happening beyond the software interface: “You could trust the software to do things right, even though you wouldn’t always understand everything. … You can be more relaxed when you know that you don’t really have to check whether you are doing it correctly” (Sue). The accountants rarely utilized FAMSyst’s user-support function since they did not perceive much practical value in it. Operating without a full understanding of the system’s procedures did not seem problematic to them at the time, as Amy noted: “Surely you give up thinking about things for yourself; you don’t need to, when they are already thought out behind the software.” In retrospect, John stated, “We should have used it [the user-support function] more.” Without having to execute the task’s core activities, the accountants found the information available via the FAMSyst interface to be less meaningful, and motivation to exploit its explanation resources evaporated quickly. This development eventually black-boxed the system’s activities from the accountants.

Second, concerning the competence maintenance facet, the accountants gave up their efforts to keep up with relevant domain knowledge. Amy and Mary had started working at the department around the time of FAMSyst’s deployment. Although possessing significant experience in standard fixed asset depreciation scenarios, their FAM knowledge had not grown as deep as that of Sue’s. In contrast, mastering the finer points of FAM required learning by doing, as highlighted in Mark’s comment above. Automatic handling of those nuanced elements left Amy and Mary with little incentive to learn, even though they had legal responsibility for numerous clients’ FAM records. Amy recalled often tuning out during internal trainings, as she did not feel like the learnings concerned the accountants—after all, the content was already “thought out behind the software.” Mary pointed out that “the software could take into account almost all alternatives that [national] tax legislation entails for fixed assets. … When the software ‘understands’ everything, you don’t really need to know that much yourself.” The presence of such adaptable automation blurred the boundaries between the skills formally required of expert FAM accountants and the less advanced set of skills needed with FAMSyst in operation.

Third, related to the output verification facet, although scrutiny of FAMSyst’s outputs was their responsibility, the accountants began to take FAMSyst’s reports at face value, submitting them to the tax agency without further examination. The same pattern was visible when the agency responded with questions about unclear items, as Mary recounted not thinking very deeply about FAMSyst’s automatic suggestions on how to respond: “I just copy-pasted the text [from FAMSyst output] when responding [to these inquiries].” Thus, the accountants minimized their assessment of the output too, confident that the system’s helpful statements relieved them of the need to validate reports for which they were legally responsible.

Hence, we identified automation complacency as a potential negative side effect of automation reliance, as it reduces workers’ incentives to engage in mindful conduction based on the assumption that “all is well” and there is no cause for concern (Moray, 2003; Parasuraman & Manzey, 2010).

## 5.5 Skill Erosion as a Consequence of Complacency

Our analysis suggests that decreasing mindful conduction erodes individual workers’ skills over time because the lack of attention to the task (1) causes them to forget what they have learned and (2) prevents them from developing their skills in response to environmental changes. Although relying on automation appears to simplify the work task, workers’ complacency-born lack of mindful conduction actually makes the work task increasingly complex over time, should the workers be faced with the need to understand it. The state of complacency predetermines that skill erosion will happen latently as long as the skills are not immediately needed; it becomes apparent only if such need emerges (e.g., when automation becomes unavailable).

Such a need emerged at AccComp in 2015, when the company’s upper management decided to improve the uniformity of the company’s IS architecture by pruning out peripheral systems and bringing all functions under one central accounting system. To this end, the managers chose to decommission both MainSyst and FAMSyst and replace them with a consolidated system—ConsoSyst— for managing a wide variety of accounting-related processes. Manager Roger explained, “We want to have a standardized platform; we will get efficiency benefits when everybody uses the same system.”

At the time, the managers were not fully aware of the extent to which FAM functionality was embedded in the software nor did they understand how much the accountants had grown to rely on it over the preceding seven years. While FAMSyst had reduced manual fixed asset management tasks to a minimum, ConsoSyst did not include any FAM-specific functionality. As accountant Betty explained, automation “had been taken so far that you used to get a tax report compiled at a single push of a button. This is not the case with ConsoSyst.” Therefore, the accountants who were responsible for FAM had to transition back to much more manual work, in which the assets’ depreciation and related procedures now had to be managed via Microsoft Excel. John stated: “You could not rely on the system anymore.” The FAMSyst key user was displeased about this decision and left AccComp soon after. Because other accountants had largely lost their FAM expertise, this departure represented a critical knowledge loss for the organization. At this point, John began to understand the extent of skill erosion that had taken place.

Indeed, some months after the system transition, the tax agency and AccComp clients started asking about mismatches in AccComp-produced balance sheets. The reason for the errors was that no one had allocated depreciation differentials for the fixed assets— something FAMSyst had done automatically: “We kind of didn’t even know [that FAMSyst] did this and that, and that it is something that should be done” (Amy). As had become clear by this point, in John’s words, “the skills had eroded.” AccComp had to call FAMComp consultants to help, who were able to trace back the depreciation differential using an Excel model and then produce correct tax reports. Donna recalled: “They [the client] were asking us: ‘How can we trust your figures now, how can you guarantee they are correct?’ … So, we got it fixed … otherwise AccComp would have gotten sanctions.”

The accountants pleaded for the integration of automatic FAM functionality into ConsoSyst, but their words had little effect since the managers felt that the capabilities should be possessed by the accountants rather than by any IT system. The FPS director, Carol, was highly proficient in FAM. She was surprised to discover that the accountants now lacked FAM know-how: “So when I asked one of the accountants where some particular numbers in the tax report come from, they would say, ‘Well, they come from the [FAMSyst] report’ [laughs]. … That is completely against my principles.” The accountants were thus shaken out of their complacency as they struggled to adapt to the world of manual FAM after years of automated operations, with John explaining that with this change “you really needed to know how to handle the transactions … Those were really excruciating times.”

In sum, the effects of increasing complacency and subsequently decreasing mindful conduction constitute a reinforcing (R) loop which we term the individual skill-erosion loop (R1), as it ends up latently increasing the burdensomeness of a work task via skill erosion. If enough erosion occurs, the workers will struggle to perform the task or even make sense of it. Jennifer summed it up: “If automation carries out a task for me, and if I don’t get involved in it, I will ultimately forget how to do the task.” Based on the above, we follow Senge’s (2006) guidelines and construct a basic skill erosion model depicted in Figure 3.

![](/api/attachments/R9HNQ87R/fulltext/images/30dfc2f7daab5136f8a001cc9bd046499e4f3f9286ae9fcc63188a84ae5e1ec9.jpg)  
Figure 3. A Basic System-Dynamics Model of Skill Erosion

Next, we consider how other factors in the organization’s sociotechnical surroundings interact with the basic model’s core work-system elements and influence the three feedback loops.

## 5.6 Environment, Organization, and Technology

Our analysis shows that legislation complexity was a key contributor to the burdensomeness of FAM work, as FAM legislation changes frequently and requires interpretation. Linda elaborated: “[This is an issue] especially in the long run when regulations change, which happens yearly. So, if you don’t keep up with these, you get left out pretty quickly.” Further, customer complexity stemming from customers owning large and complex fixed assets that require careful accounting added to this burden. These two external factors increased the burdensomeness of the task, creating thrust for B1 and/or B2 to address the burden.

As a general tendency, managers may be concerned about organizational operations becoming mindless due to automation (Salovaara et al., 2019). Therefore, they may set up mechanisms to ensure workers’ mindful conduction by defining and enforcing organizational policies aimed at maintaining skills. While AccComp did this to an extent, the enforcement and comprehensiveness of these policies fell short.

As individual workers’ reliance on automation manifested itself as performance benefits<sub>—</sub>by minimizing FAM’s burdensomeness and freeing time for other productive activities—the organization gained performance benefits too. This contributed to complacency at the organizational level too: Having learned that the system increased efficiency without producing any (visible) adverse consequences, AccComp did not find it necessary to enforce its skill maintenance policies. While the key user took part in external training, other accountants were merely encouraged (instead of required) to do so, and their FAM skills were not assessed in any way. John recalled: “We did not recognize [the possibility of skill erosion] back then. All was well as long as we had FAMSyst in use.” Concentrating the responsibility for knowledge maintenance on one key user was not seen as a major issue at the time: “We were mainly concerned about getting [FAM] right,” said John.

In a state of complacency, an organization is unlikely to enforce stricter skill maintenance measures, as there is no obvious business case for doing so. In this way, FAM skills at AccComp were allowed to erode and be concentrated in few hands. Therefore, a chain of causal links exists where automation reliance increases organizational performance, which in turn gives rise to complacency at the organizational level. The organizational complacency decreases the enforcement of skill maintenance mechanisms, which finally reduces individual workers’ mindful conduction. We refer to this vicious circle as the organizational skill-erosion loop (R2), a reinforcing loop fueled by organizational complacency.

We acknowledge that, while this was not the case in our study, organizational enforcement of skill maintenance may receive counterbalancing pressure from the environment (legislative, normative, or other) in contexts that require strict maxims of professionalism (e.g., hospitals facing societal pressure to retain their mindfulness and competence in treating patients). In such cases, environmental pressures can outweigh organizational complacency.

Finally, when considering automation technology (FAMSyst’s technical capabilities), our analysis shows that workers’ extreme and mindless reliance on automation was enabled and facilitated by (1) technology’s high reliability in performing its tasks (i.e., it rarely failed) and (2) its impressive ability to handle task complexity (i.e., it was able to operate on each key facet of the work task). Additionally, (3) the technology’s explanation functions (incl. technical design features, FAMComp’s customer support and training offerings, etc.), reassured the accountants that explanations for the automatic operations were available and could be retrieved when needed, enabling them to rely on FAMSyst. Indeed, previous research suggests that a lack of explanations may entirely prevent domain experts’ reliance on cognitive automation (Lebovitz et al., 2022). These three features amplified the reliance loop (B2) at the expense of the mindfulness loop (B1). In balance, FAMSyst’s explanation features had been designed to support workers’ mindful conduction in various ways, which could have empowered B1 when utilized (though AccComp did not). Appendix C summarizes the ways in which FAMSyst fostered both automation reliance and mindful conduction.

We thus incorporated environmental factors, technological elements, and organizational context to construct a comprehensive, sociotechnical model of skill erosion depicted in Figure 4. Detailed explanations for the model’s relationships are provided in Appendix D.

In sum, AccComp essentially shifted the burden of FAM to an IT system, resulting in undesired long-term consequences on workers’ skills. Next, we discuss how the aforementioned negative dynamics can be reversed through narrating how AccComp addressed issues resulting from skill erosion.

![](/api/attachments/R9HNQ87R/fulltext/images/44d021ac1b80538966f19e2605fddeb51d7fee8e1544c158b10b96e46d7a0943.jpg)  
Figure 4. A Comprehensive System-Dynamics Model of Skill Erosion

## 5.7 Coping and Restoration of Skills

Facing an urgent need to restore their FAM skills, the accountants were forced to become more mindful about the FAM process. To understand how FAMSyst had calculated depreciations, they accessed old customer account materials still available in FAMSyst’s offline interface for longstanding clients. Also, the accountants extracted Excel forms from the system whereby they could attempt to reverse-engineer FAMSyst’s execution logic. These actions helped them resolve some relatively simple cases. To elevate their domain understanding, the accountants started selfstudying the FAMSyst manual and various literature and legal regulations pertaining to the reporting of fixed asset depreciation. They also connected to colleagues across different departments to gain further insights into how to interpret tax law. At an organizational level, AccComp arranged internal workshops centered on example cases to solve and sent its accountants to undergo Chamber of Commerce training. This time, having awakened from organization-level complacency, the managers made attendance mandatory. Accountants were directed to produce FAM manuals so that the knowledge they had (re)gained would be available for future reference. The organization began slowly reaping the rewards of this onerous skill (re)acquisition process, and FAM skill levels were manifesting a clear upward trend in mid-2017. In other words, though the reliance loop (B2) had previously dominated, now the mindfulness loop (B1) was gaining prominence via mindful conduction. Mary elaborated how increasing mindful conduction ultimately decreased the FAM task’s burdensomeness: “[as our skills improved] the whole process became clearer, and you no longer needed to check things from instructions all the time.”

AccComp then tried to enhance ConsoSyst with greater abilities to assist with the more repetitive FAM activities (enabling automation reliance to a certain extent). Director Sara spoke on the importance of leveraging automation in conjunction with strong domain skills: “We need people who understand accounting legislation and the latest interpretations on tax governance and value-added tax. But additionally, they should have experience in accounting automation and possess vision and drive to develop it.” Though cognitive automation can help address the problem of burdensomeness, our informants confirmed that maintaining current and comprehensive understanding of FAM is expected from accountants who are responsible for the task. Hence, the organization’s leaders wanted to make sure that skill erosion would be prevented this time around. This involved a change in how teams shared knowledge:

[We] changed the way of operating, such that the team leader’s role is not to be always there saying, “This is right, and that is wrong, and this is how it is done.” Rather, the team leader should be the last link who can help if someone cannot manage, while the know-how should come from within the team. That is the goal. (Carol)

In other words, while the organization continued to embrace cognitive automation, it had become conscious of the risk of skill erosion and actively sought to strike a balance between automation reliance (B2) and mindfulness (B1) without falling prey to complacency (R1 and R2).

## 6 Discussion and Conclusions

Our case analysis identifies emergent and latent developments, unintended outcomes, and complex relationships among different sociotechnical elements, which collectively reflect dynamic complexity (Senge, 2006). The dynamic interactions between different elements were found to produce vicious circles (Masuch, 1985) that push the sociotechnical system away from skillfulness toward skill erosion through escalating reliance on automation. As a response to our first research question, the SD model in Figure 4 uncovers dynamic mechanisms of latent skill erosion in an organization’s sociotechnical work system. It shows the competing dynamics of automation reliance and mindful conduction in addressing problem symptoms stemming from cognitively taxing work tasks. On the one hand, while minimizing or eliminating automation reliance (abstaining from the use of cognitive automation) supports mindfulness and the accountability of operations, it can cause the organization to lose efficiency and miss out on opportunities presented by emerging ITs, potentially causing it to be left behind by the competition. On the other hand, allowing heavy reliance on cognitive automation is problematic due to the latent individual and organizational skill erosion loops (R1 and R2). They reinforce skill erosion in that neither the individual worker nor the organization ends up questioning or otherwise problematizing the use of the automated system and further facilitate skill erosion by fostering complacency at both levels. This pushes the work system further from the ideal state. Hence, a trade-off between mindfulness and reliance (loops B1 and B2) exists, which requires careful balancing. Our conclusion is that the key leverage point lies in the way in which mindful conduction is managed.

With regard to the second research question concerning the organizational implications of skill erosion, our findings show how skill erosion makes an organization’s operations mindless and fully reliant on IT systems. When the system’s operations incorporate large quantities of domain-specific contextual knowledge (Strich et al., 2021), and updates in response to context changes are rapid, human workers tend to lose motivation for maintaining competence—they perceive the domain knowledge as still being present, just accessible elsewhere. In our case study, knowledge resided with the automation vendor and was accessible via cloud-based system updates. Further, as workers’ skills erode, the organization’s domain competence deteriorates. The erosion makes the organization increasingly dependent on the IT system’s provider, exposing it to different kinds of risks: The organization’s control over its own operations decreases and the IT provider gains a higher bargaining power over the deskilled organization. Situations in which the organization decides to reduce its dependence on the IT provider or remove the system for other reasons may result in disruptions to the organization’s operations and among its people (as was shown in our case). In such a state, disruptions may arise unexpectedly (as at AccComp) if the organization has not acknowledged the existence of skill erosion and has thus not prepared for it.

Our study answers the recent calls for seeking a deeper understanding of the frequently detrimental effects of cognitive automation on humans’ skills (Newell & Marabelli, 2015; Strich et al., 2021; Sutton et al., 2018). By elaborating on the dynamic interactions of different elements in a sociotechnical context, our work has the following implications for both theory and practice.

## 6.1 Theoretical Implications

Our results come with implications crucial for understanding the individual and organizational implications of IT use, skill erosion, and AI management. First, we enrich the conceptual understanding of the underlying mechanisms of skill erosion. Second, our conceptualization of mindful conduction sheds light on how skill erosion can be detected. Third, our dynamic model provides a holistic view on managing the automation-augmentation trade-off.

First, recent IS literature has acknowledged skill erosion as a potentially harmful aspect of IT-enabled cognitive automation (Burton-Jones, 2014; Faraj et al., 2018; Mayer et al., 2020; Newell & Marabelli, 2015; Strich et al., 2021) that warrants empirical inquiry. Though other domains have taken some steps to empirically probe the topic, they have done so using models with singledirection factor effects (Dowling et al., 2008; Galletta et al., 2005; Mascha & Smedley, 2007), leaving its theoretical mechanisms and organizational implications unknown (Sutton et al., 2018). Our empirical study and the resulting dynamic model (Figure 4) contribute to theory by crystallizing how skill erosion can unfold latently over time through vicious circles of automation complacency that diminish mindful conduction. Consideration of such dynamic loops will enrich scholarly understanding of the latent nature of skill erosion, and the applicability checks we conducted (Appendix E) indicate that the SD model provides a valuable contribution to knowledge in this previously poorly understood area.

Second, our three-faceted conceptualization of mindful conduction answers the recent calls for a more holistic understanding of automation’s skill-eroding and dependency-inducing effects and their detection and management (Newell & Marabelli, 2015). The degree to which humans vs. systems either do or do not carry out relevant activities (on the facets of activity awareness, competence maintenance, and output assessment) suggests how “warning signs” of skill erosion may be detected on different fronts. Because skills are difficult to measure, it may be more feasible to probe the extent of mindfulness at each facet of the work task and use it to predict skill level. For instance, examining the extent to which a worker shows awareness of their work activities or performs output assessments can reveal existing or potential gaps in skills. Our case study revealed how certain features of automated technology can make the system appear as if it is mindfully, autonomously engaging with the work task (e.g., handling task activities, updating its own functionality, and readily producing specified and generated outputs) while also performing functions designed specifically to support humans’ mindfulness (explanatory ones clarifying its activity and output, inclusion of the provider’s user training for competence, etc.). Relinquishing mindful maintenance of domain competence is similar to the kind of transactive memory process in IT use that Sparrow et al. (2011) identified, where human memory adapts to computing and communication technology: people learn what the computer “knows” and let this “knowing of knowing” replace their own conception of the actual object known. Such a process, which bears a resemblance to the “cognitive offloading” discussed by Hansen et al. (2019), may explain the latency that seems to typify skill erosion (Oliver et al., 2017; Stone, 2007). Clearly, this kind of adaptation is problematic in settings that demand retaining human responsibility and accountability.

Third, we find that our model provides a powerful analytical device for managing AI systems, shedding light on how to balance augmentation and automation (Krakowski et al., 2022; Raisch & Krakowski, 2021). Augmenting human work with AI tends to assume that humans remain in the loop by, e.g., continuously interrogating the AI system’s knowledge claims and integrating any valid insights into their own decisions (Lebovitz et al., 2022). Such augmentation reflects a healthy balance between our SD model’s mindfulness (B1) and reliance (B2) loops, which, if sustained, should yield positive performance outcomes while preventing (harmful) skill erosion. Our model sheds light on the reasons why successful augmentation tends to be difficult in practice (Raisch & Krakowski, 2021). It also accounts for the influence of AI explanations on this balancing act, which has become an increasingly important consideration due to the black-boxed nature of advanced AI systems (Asatiani et al., 2021). On one hand, if you emphasize mindful conduction too much and refuse to consider AI’s input (B1 is active while B2 is passive), AI’s full potential is left untapped. Lebovitz et al. (2022) term such lack of AI use as unengaged “augmentation”: no actual augmentation was achieved in cases where humans just overrode AI’s input due to the lack of explanations. On the other hand, if one allows too much reliance to occur, complacency creeps in to sabotage humans’ and organizations’ efforts to stay mindful, leading to skill erosion (B2 gains momentum at the expense of B1). Our SD model helps future studies conceptualize and measure how organizations manage their AI systems in terms of automation vs. augmentation.

## 6.2 Managerial Implications

Although the case company could have tried harder to avoid skill erosion—by such means as investing in stronger control mechanisms and emphasizing knowledge/skill retention in employees’ performance reviews—the larger process by which skill erosion occurred proceeded along understandable lines: Environmental factors gave rise to high task complexity. An institutional logic prioritized efficiency over skill maintenance, while individuallevel factors too (complacency despite one’s identification as a skilled professional) made it all the more natural for events to unfold in this manner. Consistent with other studies (e.g., Drummond, 2008; Garud & Kumaraswamy, 2005; Rinta-Kahila et al., 2022), our case-study findings indicate that prioritizing IT-enabled short-term efficiency gains over organizational learning may culminate in detrimental long-term outcomes. This points to a practical lesson: Organizations should preemptively devise effective strategies for human-plus-automation partnerships (Asatiani et al., 2019; Raisch & Krakowski, 2021; Rinta-Kahila et al., 2021). The models presented in Figures 3 and 4 provide a potentially useful tool for doing this by helping managers recognize relevant factors that are at play regarding skills and automation use. By probing those factors, managers may be able to determine which cycle—mindless or mindful—is dominant in their organization. The applicability checks reported in Appendix E support this assertion.

Considering automation in light of the three facets of mindful conduction can help managers find ways to automate work tasks in a more informed fashion. For example, they could increase their efforts to notice the “warning signs” of skill erosion that we mentioned in the second implication above. They should also assess what level of automation is safe regarding different facets of work tasks and consider the possibility that procuring and implementing an IT system might entail externalizing the organization’s collective understanding of the process. Recognizing the specific facets of the work task and the ways in which both humans and IT systems can be engaged in them could sensitize managers to critical aspects of skill maintenance.

## 6.3 Limitations and Avenues for Future Research

There are certain limitations of this study that must be acknowledged. First, it was impossible for us to conduct a real-time longitudinal study that would have let us directly observe workers’ skill maintenance and development (or lack thereof). Instead, we had to rely on the combination of cross-sectional interviews (Inquiries 1 and 2) and retrospective longitudinal accounts (Inquiries 3 and 4) by informants when uncovering the skill-erosion mechanisms and reconstructing the narrative of the events. To offset threats to validity and reliability, we conducted follow-up interviews with the key informants, collected complementary data from stakeholder organizations, and triangulated for solid findings (Trauth & Jessup, 2000). Further, we acknowledge that our final sample included only four employees who had experienced skill erosion firsthand. We note that these individuals’ accounts were convergent and also in line with other informants from AccComp. The two applicability checks (Appendix E) strengthen our confidence in the presented conclusions. However, there may be explanations for skill erosion in addition to what is described here. For a more thorough understanding of the phenomenon, bringing In other, thus far unheard “voices” (e.g., other managers, system developers, legal experts, and tax agency officials) could be valuable (Trauth & Jessup, 2000).

Also, while our analysis produced a holistic systemsoriented view of the phenomenon, we were not able to pull apart the process of skill erosion with finer granularity. Therefore, while our research uncovered why and how workers’ skills erode, we cannot provide a detailed answer as to precisely when this happens beyond the presented general mechanisms. One would expect the ongoing use of automatic systems to comprise several stages, which could aid in explaining the transition from understanding the task to having no real sense of it. Future research may be able to delve more deeply into the temporal dimension of the skillerosion process and further break down the actions, decisions, states, and interactions through which skills are lost. One potentially fruitful approach might be to survey workers in a case organization repeatedly over time, to examine changes in skills more systematically. However, it must be noted that assessing a skillset over time will always be difficult, as the skill requirements for any given task tend to change in response to the advancement of technology and various contextspecific changes.

Finally, as our study focused on understanding the dynamics that underlie skill erosion, devising mechanisms to manage such erosion remains a challenge for future research. An interesting extension to our research would be to conduct case studies that examine the effectiveness of technological and/or organizational mechanisms specifically designed for maintaining workers’ mindfulness and inhibiting their skill erosion. Our conceptualization of mindful conduction with its three facets offers a starting point.

## Acknowledgments

We wish to thank the SE and three anonymous reviewers for their insightful and supportive feedback throughout the review process. Further, we remain forever indebted to the anonymous case organizations and informants for participating in our study and providing us access to unique data. We are grateful for the valuable feedback from the participants of research seminars held at The University of Auckland, UNSW Sydney, UQ Business School, and Aalto University School of Business. In addition, we express our special thanks to Andrew Burton-Jones, Kalle Lyytinen, Sirkka Jarvenpaa, Micheal Axelsen, Chee-Wee Tan, Elena Karahanna, and Matti Mäntymäki for providing helpful comments on earlier versions of this paper, and to Anna Shefl and Gaia Anjali RC for helping with proofreading. All remaining errors are ours. Antti Salovaara received financial support for this work from the Academy of Finland (grant 298879) and Esko Penttinen and Tapani Rinta-Kahila from the Jenny and Antti Wihuri Foundation (Grants 190277 and 180315, respectively).

## References

Agnew, A., Forrester, P., Hassard, J., & Procter, S. (1997). Deskilling and reskilling within the labour process: The case of computer integrated manufacturing. International Journal of Production Economics, 52(3), 317-324.

Allen, R. T., & Choudhury, P. (2022). Algorithmaugmented work and domain experience: The countervailing forces of ability and aversion. Organization Science, 33(1), 149-169.

Alter, S. (2013). Work system theory: Overview of core concepts, extensions, and challenges for the future. Journal of the Association for Information Systems, 14(2), 72-121.

Anderson, J. R. (1993). Rules of the mind. Lawrence Erlbaum Associates.

Arnold, V., Clark, N., Collier, P. A., Leech, S. A., & Sutton, S. G. (2006). The differential use and effect of knowledge-based system explanations in novice and expert judgment decisions. MIS Quarterly, 30(1), 79-97.

Arnold, V., Collier, P., Leech, S. A., Rose, J. M., & Sutton, S. G. (2018). Can knowledge based systems be designed to counteract deskilling effects? (Working paper).

Arnold, V., & Sutton, S. G. (1998). The theory of technology dominance: Understanding the impact of intelligent decision aids on decision maker’s judgments. Advances in Accounting Behavioral Research, 1(3), 175-194.

Asatiani, A., Malo, P., Nagbøl, P. R., Penttinen, E., Rinta-Kahila, T., & Salovaara, A. (2021). Sociotechnical envelopment of artificial intelligence: an approach to organizational deployment of inscrutable artificial intelligence systems. Journal of the Association for Information Systems, 22(2), 325-352.

Asatiani, A., Penttinen, E., Rinta-Kahila, T., & Salovaara, A. (2019). Implementation of automation as distributed cognition in knowledge work organizations: Six recommendations for managers. Proceedings of the 40th International Conference on Information Systems.

Ashby, W. R. (1957). An introduction to cybernetics. Chapman & Hall.

Axelsen, M. (2012). Continued use of intelligent decision aids and auditor knowledge: qualitative evidence. Proceedings of the 18<sup>th</sup> Americas Conference on Information Systems.

Axelsen, M. (2014). Technology impeded knowledge acquisition and retention: The effects of longterm use of intelligent decision aids on auditor professional knowledge [Unpublished doctoral thesis]. The University of Queensland.

Baker, J., & Singh, H. (2019). The roots of misalignment: Insights on strategy implementation from a system dynamics perspective. The Journal of Strategic Information Systems, 28(4), Article 101576.

Beane, M. (2019). Shadow learning: Building robotic surgical skill when approved means fail. Administrative Science Quarterly, 64(1), 87- 123.

Von Bertalanffy, L. (1968). General system theory: Foundations, development, applications (Revised ed.). George Braziller.

Boulding, K. E. (1956). General systems theory: The skeleton of science. Management Science, 2(3), 197-208.

Braverman, H. (1974). Labor and monopoly capital: The degradation of work in the twentieth century. Monthly Review Press.

Bravo, E. R. (2015). Automation and substitution of human knowledge: Assessment within the information system context. Proceedings of the Pacific Asia Conference on Information Systems.

Brynjolfsson, E., & McAfee, A. (2014). The second machine age: Work, progress, and prosperity in a time of brilliant technologies. Norton.

Burton-Jones, A. (2014). What have we learned from the smart machine? Information and Organization 24(2), 71-105.

Burton-Jones, A., McLean, E. R., & Monod, E. (2015). Theoretical perspectives in IS research: From variance and process to conceptual latitude and conceptual fit. European Journal of Information Systems 24(6), 664-679.

Butler, B. S., & Gray, P. H. (2006). Reliability, mindfulness, and information systems. MIS Quarterly, 30(2), 211-224.

Cambridge Dictionary. (n.d.). Meaning of complacency in English. In Cambridge dictionary. Retrieved in 2023 from https://dictionary.cambridge.org/us/dictionary/ english/complacency.

Carr, N. (2015). The glass cage: How our computers are changing us (1st ed.). Norton.

Corbin, J., & Strauss, A. (2015). Basics of qualitative research: Techniques and Procedures for developing a grounded theory (4th ed.). SAGE.

Davenport, T. H., & Ronanki, R. (2018, January-February). Artificial intelligence for the real world. Harvard Business Review. https://hbr.org/2018/01/artificial-intelligencefor-the-real-world

Davis, C. J., & Hufnagel, E. M. (2007). Through the eyes of experts: A socio-cognitive perspective on the automation of fingerprint work. MIS Quarterly, 31(4), 681-703.

Dowling, Leech, & Moroney. (2008). Audit support system design and the declarative knowledge of long-term users. Journal of Emerging Technologies in Accounting, (5), 99-108.

Drummond, H. (2008). The Icarus paradox: An analysis of a totally destructive system. Journal of Information Technology, 23(3), 176-184.

Fang, Y., Lim, K. H., Qian, Y., & Feng, B. (2018). System dynamics modeling for information systems research: Theory development and practical application. MIS Quarterly, 42(4), 1303-1329.

Faraj, S., Pachidi, S., & Sayegh, K. (2018). Working and organizing in the age of the learning algorithm. Information and Organization, 28(1), 62-70.

Fiol, C.-M., & O’Connor, E. J. (2003). Waking up! Mindfulness in the face of bandwagons. Academy of Management Review, 28(1), 54-70.

Forrester, J. W. (1961). Industrial dynamics. MIT Press.

Galletta, D. F., Durcikova, A., Everard, A., & Jones, B. M. (2005). Does spell-checking software need a warning label? Communications of the ACM, 48(7), 82-86.

Garud, R., & Kumaraswamy, A. (2005). Vicious and virtuous circles in the management of knowledge: The case of Infosys Technologies. MIS Quarterly, 29(1), 9-33.

Goddard, K., Roudsari, A., & Wyatt, J. C. (2012). Automation bias: A systematic review of frequency, effect mediators, and mitigators. Journal of the American Medical Informatics Association, 19(1), 121-127.

Goddard, K., Roudsari, A., & Wyatt, J. C. (2014). Automation bias: Empirical results assessing influencing factors. International Journal of Medical Informatics, 83(5), 368-375.

Grønsund, T., & Aanestad, M. (2020). Augmenting the algorithm: Emerging human-in-the-loop work configurations. The Journal of Strategic Information Systems, 29(2), 101614.

Hampton, C. (2005). Determinants of reliance: An empirical test of the theory of technology dominance. International Journal of Accounting Information Systems, 6(4), 217- 240.

Hansen, S. W., Gogan, J. L., Baxter, R. J., & Garfield, M. J. (2019). Informed collaboration in health care: An embedded-cases study in geriatric telepsychiatry. Information Systems Journal, 29(2), 514-547.

Harari, Y. N. (2014). Sapiens: A brief history of humankind. Harvill Secker.

Jussupow, E., Spohrer, K., Heinzl, A., & Gawlitza, J. (2021). Augmenting medical diagnosis decisions? An investigation into physicians’ decision-making process with artificial intelligence. Information Systems Research, 32(3), 713-735.

Kim, D. H. (1992). System archetypes I: Diagnosing systemic issues and designing high-leverage interventions. Pegasus Communications.

Kozlowski, S. W. J., & Klein, K. J. (2000). A Multilevel approach to theory and research in organizations: Contextual, temporal, and emergent processes. In K. J. Klein & S. W. J. Kozlowski (Eds.), Multilevel theory, research and methods in organizations: Foundations, extensions, and new directions (pp. 3-90). Jossey-Bass.

Krakowski, S., Luger, J., & Raisch, S. (2022). Artificial intelligence and the changing sources of competitive advantage. Strategic Management Journal, 44(6), 1425-1452.

Langer, E. J. (1989). Mindfulness. Perseus.

Lebovitz, S., Lifshitz-Assaf, H., & Levina, N. (2022). To engage or not to engage with AI for critical judgments: How professionals deal with opacity when using AI for medical diagnosis. Organization Science, 33(1), 126-148.

Lou, B., & Wu, L. (2021). AI on drugs: Can artificial intelligence accelerate drug development? evidence from a large-scale examination of biopharma firms. MIS Quarterly, 45(3), 1451- 1482.

Lyytinen, K., & Newman, M. (2008). Explaining information systems change: A punctuated socio-technical change model. European Journal of Information Systems, 17(6), 589- 613.

Van Maanen, J. (1979). The fact of fiction in organizational ethnography. Administrative Science Quarterly, 24(4), 539-550.

Martin De Holan, P., Phillips, N., & Lawrence, T. B. (2004, January 15). Managing organizational forgetting. MIT Sloan Management Review. https://sloanreview.mit.edu/article/managingorganizational-forgetting

Martinez-Moyano, I. J., McCaffrey, D. P., & Oliva, R. (2014). Drift and adjustment in organizational rule compliance: Explaining the “regulatory pendulum” in financial markets. Organization Science, 25(2), 321-338.

Maruyama, M. (1963). The second cybernetics: Deviation-amplifying mutual causal processes. American Scientist, 51(2), 164-179.

Mascha, M. F., & Smedley, G. (2007). Can computerized decision aids do “damage”? A case for tailoring feedback and task complexity based on task experience. International Journal of Accounting Information Systems, 8(2), 73- 91.

Masuch, M. (1985). Vicious circles in organizations. Administrative Science Quarterly, 30(1), 14-33.

Mayer, A., Strich, F., & Fiedler, M. (2020). Unintended consequences of introducing AI systems for decision making. MIS Quarterly Executive, 19(4), 239-257.

McCall, H., Arnold, V., & Sutton, S. G. (2008). Use of knowledge management systems and the impact on the acquisition of explicit knowledge. Journal of Information Systems, 22(2), 77-101.

McGuinness, S., Pouliakas, K., & Redmond, P. (2019). Skills-displacing technological change and its impact on jobs: Challenging technological alarmism? (IZA DP No. 12541). IZA Institute of Labor Economics.

McKinlay, R. (2016). Technology: Use or lose our navigation skills. Nature, 531, 573–575.

Meadows, D. H., Meadows, D. L., Randers, J., & Behrens III, W. W. (1972). The limits to growth: A report for the club of rome's project on the predicament of mankind. Universe Books.

Mees-Buss, J., Welch, C., & Piekkari, R. (2020). From templates to heuristics: How and why to move beyond the Gioia methodology. Organizational Research Methods, 26(2). https://doi.org/ 10.1177/1094428120967716

Merritt, S. M., Ako-Brew, A., Bryant, W. J., Staley, A., McKenna, M., Leone, A., & Shirase, L. (2019). Automation-induced complacency potential: Development and validation of a new scale. Frontiers in Psychology, 10, Article 225.

Moray, N. (2003). Monitoring, complacency, scepticism and eutactic behaviour. International Journal of Industrial Ergonomics, 31(3), 175-178.

Newell, S., & Marabelli, M. (2015). Strategic opportunities (and challenges) of algorithmic decision-making: A call for action on the longterm societal effects of “datification.” The Journal of Strategic Information Systems, 24(1), 3-14.

Oliver, N., Calvard, T., & Potočnik, K. (2017). Cognition, technology, and organizational limits: Lessons from the Air France 447 disaster. Organization Science, 28(4), 729-743.

Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. Human Factors, 52(3), 381-410.

Pentland, B. T. (1999). Building process theory with narrative: From description to explaination. Academy of Management Review, 24(4), 711- 724.

Raisch, S., & Krakowski, S. (2021). Artificial intelligence and management: The automationaugmentation paradox. Academy of Management Review, 46(1), 192-210.

Rinta-Kahila, T., Penttinen, E., & Lyytinen, K. (2021). Organizational transformation with intelligent automation: Case Nokia Software. Journal of Information Technology Teaching Cases, 11(2), 101-109.

Rinta-Kahila, T., Penttinen, E., & Lyytinen, K. (2023). Getting trapped in technical debt: Sociotechnical analysis of a legacy system’s replacement. MIS Quarterly, 47(1), 1-32.

Rinta-Kahila, T., Someh, I., Gillespie, N., Indulska, M., & Gregor, S. (2022). Algorithmic decisionmaking and system destructiveness: A case of automatic debt recovery. European Journal of Information Systems, 31(3), 313-338.

Rosemann, M., & Vessey, I. (2008). Toward improving the relevance of information systems research to practice: Rhe role of applicability checks. MIS Quarterly, 32(1), 7-22.

Sætre, A. S., & Van de Ven, A. H. (2021). Generating theory by abduction. Academy of Management Review, 46(4), 684-701.

Salovaara, A., Lyytinen, K., & Penttinen, E. (2019). High reliability in digital organizing: mindlessness, the frame problem, and digital operations. MIS Quarterly, 43(2), 555-578.

Sarker, S., Chatterjee, S., Xiao, X., & Elbanna, A. (2019). The sociotechnical axis of cohesion for the IS discipline: Its historical legacy and its continued relevance. MIS Quarterly, 43(3), 695-719.

Scheepers, R., Lacity, M. C., & Willcocks, L. P. (2018). Cognitive automation as part of Deakin University’s digital strategy. MIS Quarterly Executive, 17(2), 89-107.

Schuppan, T. (2014). E-government at work level: Skilling or de-skilling? Proceedings of the 47th Hawaii International Conference on System Sciences (pp. 1927-1934).

Senge, P. M. (2006). The fifth discipline: The art & practice of the learning organization (2nd ed.). Crown Books.

Skitka, L. J., Mosier, K., & Burdick, M. D. (2000). Accountability and automation bias. International Journal of Human Computer Studies, 52(4), 701-717.

Sparrow, B., Liu, J., & Wegner, D. M. (2011). Google effects on memory: Cognitive consequences of having information at our fingertips. Science, 333(6043), 776-778.

Sterman, J. D. (2001). System dynamics modeling: Tools for learning in a complex world. California Management Review, 43(4), 8-25.

Stone, G. D. (2007). Agricultural deskilling and the spread of genetically modified cotton in Warangal. Current Anthropology, 48(1), 67-87.

Strich, F., Mayer, A. S., & Fiedler, M. (2021). What do I do in a world of artificial intelligence? Investigating the impact of substitutive decision-making AI systems on employees’ professional role identity. Journal of the Association for Information Systems, 22(2), 304-324.

Sutton, S. G., Arnold, V., & Holt, M. (2018). How much automation is too much? Keeping the human relevant in knowledge work. Journal of Emerging Technologies in Accounting, 15(2), 15-25.

Thatcher, J. B., Wright, R. T., Sun, H., Zagenczyk, T. J., & Klein, R. (2018). Mindfulness in information technology use: Definitions, distinctions, and a new measure. MIS Quarterly, 42(3), 831-847.

Tomasello, M. (1999). The cultural origins of human cognition. Harvard University Press.

Trauth, E. M., & Jessup, L. M. (2000). Understanding computer-mediated discussions: positivist and interpretive analyses of group support system use. MIS Quarterly, 24(1), 43-78.

Triki, A., & Weisner, M. M. (2014). Lessons from the literature on the theory of technology dominance: Possibilities for an extended research framework. Journal of Emerging Technologies in Accounting, 11(1), 41-69.

Tushman, M. L., & Rosenkopf, L. (1992). Organizational determinants of technological change: Toward a sociology of technological evolution. Research in Organizational Behavior, (14), 311-347.

Wallace, M., & Kalleberg, A. L. (1982). Industrial transformation and the decline of craft: The decomposition of skill in the printing industry. American Sociological Review, 47(3), 307-324.

Yin, R. K. (2018). Case study research and applications: Design and methods (6th ed.). SAGE.

Zuboff, S. (1988). In the age of the smart machine: The future of work and power. Basic Books.

## Appendix A: The Interview Protocols

## Inquiry 1 (AccComp)

## Background Information

• Age and education

• Previous work experience

• Your previous work tasks at AccComp

• Your current work tasks at AccComp

## Daily Work and Systems

• Could you please describe your typical workday?

• Which work tasks do you especially enjoy?

• Which systems are you currently using in your work, and for what purposes?

• How has your work changed since the recent system implementation?

• Which accounting processes are you currently involved in? (We provide a list of processes)

• Please describe each process in detail: how you feed in data to the system, what kinds of problems may arise, what part is of a routine nature and what requires mindful concentration, etc.

• Do you transfer data between separate systems manually?

Do you encounter unexpected events in your work that require conscious deliberation? Are you able to handle such situations by yourself, or do you need someone to help you? Please describe how you would resolve a problematic situation in the accounting system or your work in general.

• How many clients are you currently handling? Do you feel that you have enough time for your work tasks without being overloaded?

• Have you noticed that small mistakes could lead to problematic situations?

[If so] Could you give an example?

## Automation in Accounting

• What are your thoughts and sentiments about accounting automation systems?

• Do you see automation as a positive or negative thing for your work? Why?

• Do you find that decreasing, or even removing, the repetitive and mechanical parts of your work task as a positive thing? Why or why not?

• If some parts of your work tasks were automated, what would you do with the time freed up by automation?

• If some parts of your work tasks were automated, would it be more difficult to maintain the skills required for the work?

## Inquiry 2 (FAMComp)

## The System

• What does FAMSyst do?

• What kind of data go in, and what comes out?

• What exactly does FAMSyst automate?

## Users

• Who are the users of FAMSyst?

• What skills are required from the users?

• How does using FAMSyst affect the know-how of its users?

## Competitive Advantage

• Are there competing alternatives to your software?

• What is the main advantage of FAMSyst over the old (i.e., non-automated) way of handling FAM?

• What is the advantage of FAMSyst relative to generic systems such as ConsoSyst?

## Customer Discontinuation of FAMSyst

[Replies are in general terms since disclosing customer information specific to AccComp is not allowed]

• What was your impression of AccComp’s decision to decommission FAMSyst?

• How have you consulted with former users of FAMSyst at AccComp (since its discontinuance)?

• Are there companies that have made similar decisions to discontinue the use of FAMSyst?

• What do you see as the current trend in FAM: more automation or something else?

## Inquiry 3 (AccComp)

## The Use of FAMSyst

1. When was the first time you used FAMSyst?

• Was it at AccComp or somewhere else?

• What did you do with FAMSyst while it was in use?

2. What did FAMSyst do?

• What kind of information did you input to the system?

• How was FAMSyst integrated with other systems?

• How did the data flow between systems?

• How did FAMSyst process information: what did it do with the information fed to it?

3. What were the positive and negative sides of FAMSyst? Please indicate the most relevant ones.

4. FAMSyst has an education function (pressing F1 produces additional information about the process). Did you use this? Did other accountants use it?

5. How much did you trust FAMSyst to function reliably? Why?

## The Effect of FAMSyst on Skills

6. What was the effect of FAMSyst on accounting skills related to FAM?

• Did the system teach you something new? Did the system make you forget something?

• Did FAMSyst help you to understand FAM better, or the other way around?

## The Discontinuance of FAMSyst

7. Who decided that FAMSyst would be discontinued?

8. How did you perceive the discontinuance decision…

• Before discontinuance, after discontinuance, and now?

9. What kind of feedback did the discontinuance decision stimulate?

• Was there passive or active resistance?

• Did you try to influence the decision?

10. How is the process that FAMSyst used to have automated being handled currently?

• What is the official way?

• Are there alternative ways?

## Coping and Recovery

11. How did you navigate through the disruption caused by the discontinuance of FAMSyst?

12. How did relearning take place?

• Were training sessions arranged? Did you participate?

13. Did the amount of manual work increase, or were you able to automate the process in other ways? • Excel macros, for example?

14. When was external consultation used?

• Services of consultants from FAMComp?

• What did they do?

15. What is your current level of FAM know-how?

• Have you returned to the level of know-how you possessed before FAMSyst?

• Have you learned something useful?

16. Are there other employees who used FAMSyst?

## Inquiry 4 (AccComp)

## The Introduction of FAMSyst

1. There can be various motives behind implementing automation. What were the main reasons to implement FAMSyst?

[After hearing the answer to this open question, ask the following if relevant]

• To get by with fewer accountants, saving costs? If so, were there staffing reductions?

• To free the existing accountants’ time for other tasks, increasing capacity?

• To ease the accountants’ work burden or make their work more meaningful?

• To reduce human error in the FAM process?

2. Did anyone oppose FAMSyst’s introduction?

3. How did the accountants react to FAMSyst initially?

• Did they learn its use easily?

• Was there any user resistance?

4. Did FAMSyst change the tasks and responsibilities of the accountants?

## FAMSyst’s Effect on the Execution of Work Tasks

5. We have learned that the accountants developed solid trust in FAMSyst over the years, so…

• Do you remember signs of this trust forming? How did it happen?

6. Were the accountants expected to retain their mastery of FAM?

• If so, how were they expected to do that?

• Was this expectation communicated to the accountants? How?

• Is it possible to retain a solid conception of FAM task activities by maintaining one’s knowledge (via training and study) and scrutinizing outputs (tax reports) when automation is executing the process?

7. Why did your organization fail to actively maintain FAM skills?

• Did the loss of motivation occur gradually?

• Was the participation in FAM training low to begin with, or did it decrease through use of FAMSyst? If it decreased, did that happen gradually, or was there a specific point when they dropped the training?

• Did the key user try to share FAM knowledge? How was this done?

## Erosion of Skills

8. Why did FAMSyst cause a decrease in the accountants’ ability to handle complex cases?

9. Were you ever worried by the erosion of skills over the years, or did it come as a complete surprise after FAMSyst was discontinued?

10. What if FAMSyst had remained in place indefinitely?

• Do you think skill erosion would have become a problem?

11. Could you assess the gravity of the knowledge loss from the following perspectives?

• The accountants no longer knew what needs to be done (definitions, categories)

• The accountants no longer knew how to do things (steps, process, interpretation)

12. What could have been done to prevent skills’ erosion?

• Was skill erosion inevitable with FAMSyst? How feasible would it have been to retain the skills after implementation of such a system?

• Could different organizational practices have prevented skill erosion?

• Could an alternative design for FAMSyst have prevented skill erosion?

## Conclusion

13. [We explain our interpretation of the case] Finally, …

• Does this interpretation reflect what took place in your organization?

• Can you tell us anything more about how conceptions of FAM eroded?

• Have we missed any relevant aspects?

## Appendix B: The Coding

Table B1. The Coding

<table><tr><td>First-order concepts</td><td>Themes (second order)</td><td>Aggregate dimensions</td></tr><tr><td>FAM seen as an unpleasant taskThe complexity of optimizing fixed asset depreciations for taxationFAM requires the ability to interpret legislationTax accounting is the most challenging part of FAM</td><td>Task complexity</td><td rowspan="2">Burdensomeness of work task</td></tr><tr><td>Manual FAM is time-takingNeed to check repeatedly that everything is going correctlyFAM requires learning by doing</td><td>Time-consuming task</td></tr><tr><td>National FAM legislation changes oftenNo clear answers written in the legislation</td><td>FAM legislation complexity</td><td rowspan="3">Environmental context</td></tr><tr><td>Energy production industryCustomers with massive fixed assetsSome FAM activities occur rarely (e.g., wrecking)</td><td>Customer complexity</td></tr><tr><td>All accountants need at least basic FAM skillsThere can be no blind trust in automation</td><td>Maxims of professionalism</td></tr><tr><td>FAMSyst executes depreciation calculationFAMSyst matches accounting and taxationFAMSyst enables time savingsFAMSyst produces a readymade report for tax accounting</td><td>Handing off task activities to automation</td><td rowspan="3">Automation reliance</td></tr><tr><td>No need to be a FAM expert to use FAMSystThings readily "thought out" in FAMSystRelying on FAMComp consultancy services in difficult casesFAMSyst reduces task complexity</td><td>Relying on external competence</td></tr><tr><td>No need to check the correctness of FAMSyst's outputDifficult to assess outputs without understanding the processCopying FAMSyst's figures and statements directly to the tax form</td><td>Relying on automation's outputs</td></tr><tr><td>Understanding the FAM process stepsUnderstanding what FAMSyst is (or was) doingManual calculation of figures in Excel</td><td>Activity awareness</td><td rowspan="3">Mindful conduction</td></tr><tr><td>Attending external and internal trainingsProducing documentation of learningsSelf-studying legislation and guild guidelines</td><td>Competence maintenance</td></tr><tr><td>Scrutinizing outputs before sending them to the tax officeReverse-engineering FAMSyst's figuresInterpreting the tax implications of reported depreciations</td><td>Output assessment</td></tr><tr><td>Accountants unable to retrieve correct figures for tax reportsStruggling to conduct FAM manuallyUncertainty about "what to do"Deep understanding of "how to do it" has disappearedAccountants shocked when FAMSyst is decommissionedUncertainty about the correctness of figures</td><td>Skill erosion</td><td rowspan="3">Skill level</td></tr><tr><td>Becoming aware of skill erosionSkills improve through manual conductionKnowledge accrual through independent studying</td><td>Skill recovery</td></tr><tr><td>Trade-off between automating tasks and preserving skillsFAMSyst use resulted in skill erosion over timeFAMSyst inhibited skill acquisition/developmentOrganization possessed sufficient skills prior to FAMSyst introduction</td><td>Automation's effects on skills</td></tr><tr><td>FAMSyst considered to be trustworthy"It always worked correctly"No complaints from internal assessmentNo complaints from the tax officeFAMSyst's readily prepared statements satisfy the tax office's follow-up queries</td><td>Reliability</td><td>Cognitive automation technology</td></tr><tr><td>FAMSyst's reports correspond to tax form no. 62FAMSyst built specifically around the national tax legislationFAMSyst "anticipates" tax office's follow-up queriesLegislative changes automatically updated into FAMSystA user-friendly system</td><td>Ability to handle task complexity</td><td rowspan="2"></td></tr><tr><td>F1 button reveals the process steps for a given actionExplanations about FAMSyst's outputsFAMSyst provides "easy access" for understanding a complex taskUser manual provides explanations about processFAMComp holds user trainings</td><td>Explanation features</td></tr><tr><td>No need to think about where the figures for the tax report come fromFeeling relaxed because all knowledge is embedded in FAMSystNo motivation to pay attention during internal trainingsNot trying to understand the statements copied from FAMSyst output to tax formNot using the F1 button "enough"</td><td>Individual complacency</td><td rowspan="2">Automation complacency</td></tr><tr><td>Managers did not recognize the risk of skill erosion"All is well [at AccComp] as long as FAMSyst is in use"Bringing up the possibility of skill erosion but not acting on it</td><td>Organizational complacency</td></tr><tr><td>Key user to share FAM knowledge within the organizationArranging internal trainingsKey user helps others when neededKey user produces documentation</td><td>Key user</td><td rowspan="3">Enforcement of skill maintenance</td></tr><tr><td>Participation in external trainings mandatory only for the key userNo targeted/conscious efforts to maintain FAM competenceConcentration of FAM knowledge in few hands</td><td>Lack of enforcement</td></tr><tr><td>Mandating participation in trainingsSending accountants to Chamber of Commerce trainingsHolding workshopsChanging the role compositions (decentralizing knowledge)</td><td>Systematic reskilling efforts</td></tr></table>

## Appendix C: The Facets of Mindful Conduction

“Activity awareness” refers to attention to the concrete procedures that the work task encompasses, such as the series of steps in calculating depreciation values for assets, connecting these to the correct accounts, and producing reports for taxation and accounting purposes. It thus accrues and maintains one’s procedural knowledge and skills in performing a task (Anderson, 1993). Activity awareness may be exercised either via hands-on execution of those steps or by studying or supervising their execution by another agent. The latter technique becomes relevant when automation takes over some of the task’s activities. “Competence maintenance” refers to the domain knowledge considered both prerequisite to performing the work task and the foundation of formal expertise. This knowledge is mainly declarative in nature: it assigns meanings to information, answering the “what” question (Anderson, 1993). Competence maintenance may manifest via gaining new domain knowledge or brushing up on one’s existing knowledge (e.g., internalizing professional guidelines and regulations), and it can be achieved independently or via external training. Finally, “output assessment” denotes the work process’s deliverables with assessable quality and correctness, such as tax reports. This facet of mindful conduction draws chiefly on declarative knowledge and encompasses scrutinizing and verifying the output of the task (e.g., by means of judgment and interpretation of output validity).

Table C1 summarizes how FAMSyst’s features gave rise to both automation reliance and mindful conduction at AccComp.

Table C1. Automation Reliance vs Mindful Conduction

<table><tr><td>Facet of work task</td><td>Operations carried out automatically (enabling automation reliance)</td><td>Illustrative quotes</td><td>System features supporting humans&#x27; mindful conduction</td><td>Illustrative quotes</td></tr><tr><td>Task activities (execution of activities; awareness of activities)</td><td>Calculation of depreciationAllocation of depreciation valuesProduction of reports</td><td>“[FAMSyst] masters all kinds of fixed asset depreciations [and] produces the necessary records that can be taken to accounting with the help of versatile interfaces.” (Online material)“[FAMSyst] also includes a user-friendly report generator.” (Online material)</td><td>FAMSyst provides visibility of the system&#x27;s processing logic via user-support functionalityFAMSyst provides explanations of how a specific depreciation value has been calculated, via an extraction function</td><td>“If you wanted to drill into a particular item, you could go check that ‘this is how it is being handled’; it was understandable and logical.” (Sue)“You get to see how a contractual change has been calculated, by extracting an [explanatory] Excel form.” (Online material)</td></tr><tr><td>Domain competence</td><td>Updates to system functionality, prompted by changes in legislationUpdates to system functionality in response to cases the system&#x27;s calculations could not initially handle</td><td>“If the tax office made changes, they were always automatically updated.” (Sue)“We constantly develop the software, through [meeting needs that arise from] new customer projects.” (Mark)</td><td>FAMSyst informs users of changes; the online user manual gets updated in response to legislative changesFAMComp arranges training when system functionality changes</td><td>“We received updated instructions from the system when the tax legislation changed ... and [FAMSyst] contained a user manual that was really clear.” (Sue)“We organize regular training seminars regarding the application and its topic domain.” (FAMSyst online material)</td></tr><tr><td>Output assessment</td><td>Reports meeting various standards and legislative requirementsReports formatted to correspond to the tax agency forms</td><td>“[FAMSyst] produces depreciation receipts, sales receipts ... for both FAS-compliant accounting and IFRS-compliant monitoring.” (Online material)“It produced a form that is exactly like the tax-office one, precisely the same numbers.” (Sue)</td><td>FAMSyst provides supporting statements that help to validate reports and address potential tax agency inquiries</td><td>“Okay, the tax office is asking about this special case, which is already opened up for us in the [FAMSyst] output.” (Amy)“I was glad to get a quick answer [from the system output].” (Mary)</td></tr></table>

## Appendix D: The Dynamic Relationships among the Constructs

Table D1. The Balancing Loops of Mindfulness (B1) and Reliance (B2)

<table><tr><td>Causal construct</td><td>Description</td><td>Response construct</td><td>Dynamic relationship</td></tr><tr><td>Burdensomeness of work task</td><td>The burden caused by a work task&#x27;s complexity, uncertainty, and/or time-intensiveness.</td><td>(+) Mindful conduction</td><td>The burdensomeness of work task triggers the need to be mindful when executing or supervising it to ensure the task gets executed correctly.</td></tr><tr><td>Mindful conduction</td><td>Performing work tasks mindfully, i.e., in a state that reflects alertness and dynamic awareness (Langer, 1989). It may manifest via three modes of working: (1) being consciously aware of the activities being executed, (2) maintaining one&#x27;s domain competence, and (3) critically assessing outputs.</td><td>(+) Skill level</td><td>Workers perform the work task mindfully by paying attention to task activities, keeping their domain competence up to date, and assessing outputs. Over time, this builds up their declarative and procedural knowledge of the task, making them more skillful. On the contrary, if workers lack mindfulness, they fail to acquire and retain both types of knowledge, which causes their skills to stagnate (Axelsen, 2012; Dowling et al., 2008; McCall et al., 2008).</td></tr><tr><td>Skill level</td><td>Skill level is reflected by workers&#x27; knowledge and ability to perform the task at hand. It could be measured in terms of declarative and procedural knowledge (Dowling et al., 2008; McCall et al., 2008).</td><td>(-) Burdensomeness of work task</td><td>As one becomes increasingly skillful in performing a task, executing it becomes easier, almost “automatic” (Senge, 2006, p. 153), eventually alleviating the task&#x27;s burdensomeness.</td></tr><tr><td>Burdensomeness of work task</td><td>The burden caused by a work task&#x27;s complexity, uncertainty, and/or time-intensiveness.</td><td>(+) Automation reliance</td><td>High task burdensomeness incentivizes workers to reduce the task&#x27;s complexity, uncertainty, or time-intensiveness by handing off different facets of task performance to cognitive automation.</td></tr><tr><td>Automation reliance</td><td>Human workers relying on cognitive automation to fulfill various task responsibilities that would otherwise be fulfilled manually by workers.</td><td>(-) Burdensomeness of work task</td><td>Shifting the burden of task performance to automation will immediately alleviate the (perceived) burdensomeness of the task (although it does not address workers&#x27; fundamental need to master the task).</td></tr></table>

Table D2. The Reinforcing Loops of Individual Skill Erosion (R1) and Organizational Skill Erosion (R2)

<table><tr><td>Causal construct</td><td>Description</td><td>Response construct</td><td>Dynamic relationship</td></tr><tr><td>Automation reliance</td><td>Human workers relying on cognitive automation to fulfill various task responsibilities that would otherwise be fulfilled manually by workers.</td><td>(+) Individual complacency</td><td>Individual workers experience the benefits of cognitive automation (e.g., cognitive offloading and a lower workload; see Hansen et al., 2019) and do not perceive any problems caused by automatic systems' failure or their own lack of competence. This gives rise to complacency at the level of the individual as they grow overly confident in their abilities (Parasuraman &amp; Manzey, 2010).</td></tr><tr><td>Individual complacency</td><td>A feeling of calm satisfaction with one's abilities or situation that prevents one from trying harder (Cambridge Dictionary, 2023); blind trust in automation and lack of concern over the state of one's own abilities (Merritt et al., 2019; Parasuraman &amp; Manzey, 2010)</td><td>(-) Mindful conduction</td><td>Workers' complacency decreases their mindful conduction (i.e., lowering activity awareness, competence maintenance, and output assessment), as they begin to blindly trust automation. They assume that there is no cause for concern and no reason to expend any additional effort.</td></tr><tr><td>Automation reliance</td><td>Human workers relying on cognitive automation to fulfill various task responsibilities that would otherwise be manually fulfilled by workers.</td><td>(+) Organizational performance</td><td>Individual workers' extensive reliance on automation in one task frees their time for other tasks. This creates organizational performance benefits, materializing as positive impacts on organizational key performance indicators (KPIs), such as efficiency, productivity, and return on investment. Such a bottom-up effect reflects a compilationprocess (Kozlowski &amp; Klein, 2000): while higher performance at the individual level (due to automation reliance) should contribute to the level of organizational performance, the strength of this effect depends on the individual worker, their role, and the context in which the organization operates.</td></tr><tr><td>Organizational performance</td><td>The performance of organizational operations in terms of, e.g., efficiency, productivity, consistency, and profitability.</td><td>(+) Organizational complacency</td><td>The organization's management experiences the benefits of automation (e.g., profits and efficiency) and does not observe any apparent negative consequences of its use. Therefore, complacency arises at the organization level as the larger entity becomes oblivious to the potential dangers that automation poses for its knowledge capital.</td></tr><tr><td>Organizational complacency</td><td>The organization's lack of attention to the potential long-term hazards that workers' reliance on automation presents to its knowledge capital and a consequent lack of sufficient management policies to preserve the skills</td><td>(-) Enforcement of skill maintenance</td><td>Organizational complacency decreases management's motivation and propensity to invest in enforcing its workers' mindful conduction and skills because there is no obvious business case to do so, and the consequences of skill erosion are not perceivable in the short term.</td></tr><tr><td>Enforcement of skill maintenance</td><td>Organizational measures to ensure that workers are mindfully engaged with their work duties and are preserving their skills. For instance, setting up mandatory or voluntary knowledge maintenance and development programs (e.g., training, workshops, conferences) or other mechanisms.</td><td>(+) Mindful conduction</td><td>Setting up and enforcing mechanisms aimed at skill maintenance should mandate and/or incentivize workers' activity awareness, competence maintenance, and output assessment. From a multilevel perspective (Kozlowski &amp; Klein, 2000), such policies would typically unfold via a top-down effect wherein a higher-level unit (management) influences a lower-level unit (worker) directly (e.g., mandating training activities).</td></tr></table>

Table D3. Cognitive Automation Technology

<table><tr><td>Causal construct</td><td>Description</td><td>Response construct</td><td>Dynamic relationship</td></tr><tr><td>Reliability</td><td>Cognitive automation technology&#x27;s ability to performing its tasks consistently without errors or malfunctioning.</td><td>(+) Automation reliance</td><td>If the technology operates reliably, workers feel confident about its ability to carry out the task consistently and entrust it with carrying out various task activities (Parasuraman &amp; Manzey, 2010).</td></tr><tr><td>Ability to handle task complexity</td><td>Cognitive automation technology&#x27;s ability to respond to various requirements of a complex work task.</td><td>(+) Automation reliance</td><td>If the technology is able to handle task complexity well, workers feel confident about its ability to respond to task requirements and entrust it with carrying out various task activities.</td></tr><tr><td>Explanation features</td><td>Cognitive automation technology&#x27;s ability to display the logic by which the system runs and performs its tasks (e.g., how it translates inputs to outputs). Explanation features provide the users with a means observe and understand the task activities that are being conducted automatically (Arnold et al., 2006).</td><td>(+) Automation reliance</td><td>If workers can access and understand the logic by which the cognitive automation technology operates, they are more likely to rely on the technology to an extent and entrust it to conduct task activities (Arnold et al., 2006). This can manifest e.g., as accepting an intelligent decision aid&#x27;s recommendation. Contrariwise, if the system is inscrutable, workers may exhibit aversion to the technology and refuse to rely on it (Allen &amp; Choudhury, 2022; Lebovitz et al., 2022).</td></tr><tr><td>Explanation features</td><td>This dimension points to the automation&#x27;s ability to display the logic by which the system runs and performs its tasks. In essence, these features provide the users with a means observe and understand the task activities that are being conducted automatically.</td><td>(+) Mindful conduction</td><td>Having access to explanation features enables workers to observe and study the logic that guides automatic task executions. This should enhance their mindfulness about the task by enabling and increasing activity awareness, competence maintenance, and/or output assessment. For instance, explanations may elevate workers&#x27; domain competence by revealing previously unknown factors that influence its processes or decisions (Arnold et al., 2006).</td></tr></table>

Table D4. Environmental Context

<table><tr><td>Causal construct</td><td>Description</td><td>Response construct</td><td>Dynamic relationship</td></tr><tr><td>Legislation complexity</td><td>Complexity stemming from legislative requirements and guidelines regarding a work task. This can manifest as legislation changing frequently, being difficult to interpret, and/or involving various layers or exceptions to rules.</td><td>(+) Burdensomeness of work task</td><td>Legislation complexity requires workers to spend efforts to address the complex requirements of the work task (e.g., by conducting detailed cross-checking of accounts and reports against sections of the law) to ensure the operations can stand legal scrutiny. This increases the burden workers experience from performing the task.</td></tr><tr><td>Customer complexity</td><td>Complexity stemming from the characteristics or circumstances of an organization&#x27;s customer(s). For instance, large amounts of fixed assets contribute to customer complexity from an accounting service provider&#x27;s perspective.</td><td>(+) Burdensomeness of work task</td><td>Customer complexity increases the efforts workers need to spend on ensuring they are responding to the customer&#x27;s requirements and providing a sufficient level of service quality. This increases the burden workers experience from performing the task.</td></tr><tr><td>Maxims of professionalism</td><td>External pressures in an industry that oblige the practitioners of the profession to sustain certain standard skills and knowledge. These can materialize as, for instance, workers&#x27; guild guidelines.</td><td>(+) Enforcement of skill maintenance</td><td>In contexts that manifest strict maxims of professionalism, related environmental pressures can prompt organizations to enforce skill maintenance programs among their workers. For instance, a national defense organization may continuously test and retrain its subjects to ensure that the nation is perceived to have a credible defense and is able to respond to aggression.</td></tr></table>

## Appendix E: Applicability Checks

To assess the SD model’s (Figure 4) concepts, mechanisms, and applicability in practice, we conducted two focus group sessions following the guidelines outlined by Rosemann and Vessey (2008). The focus groups were held in November 2022 and January 2023 in two accounting companies in Northern Europe (referred to as Company A and Company B, neither was AccComp). Participants were chosen based on their availability, their experience in working with cognitive automation systems in contexts similar to that of our case study, and their interest in the phenomenon of skill erosion.

We prepared a three-page research summary that included a description of the phenomenon (skill erosion) and our motivation to study it, an illustration of the basic SD model of skill erosion (Figure 3) with environmental context added, and explanations of the model’s concepts and relationships. In addition, we provided three sample interview questions. This summary was sent to the participants ahead of the focus group sessions. The first session included two senior accountants in Company A and was held face-to-face on the company’s premises. The second session was conducted with two participants from Company B—the head of development and the business development expert— also on-site but with one of the participants attending the meeting virtually. The sessions were conducted in Finnish.

Table E1. Data Collection for Applicability Checks.

<table><tr><td>Applicability check</td><td>Place</td><td>Participants</td><td>Session length</td></tr><tr><td>Session 1</td><td>Company A</td><td>Senior accountant 1 (in person)Senior accountant 2 (in person)</td><td>60 min</td></tr><tr><td>Session 2</td><td>Company B</td><td>Head of Development (in person)Business Development Expert (virtually)</td><td>90 min</td></tr></table>

We began both sessions with a short meet-and-greet after which we explained the session’s objectives and proceedings. After verifying that the participants had read the research summary and familiarized themselves with the model, we asked some probing questions to form an initial understanding of how they had interpreted the model and if there were some areas that would need further elaboration. We continued by illustrating the SD model in a staged manner using MS PowerPoint for visualization. We started from the components and relationships of the basic version (Figure 3) and gradually built up to the full model (Figure 4). After this, the participants were asked to share their thoughts about the model, its concepts, and relationships. Rich discussions ensued as the informants shared their reflections and built on each other’s perceptions. Finally, the informants were asked specific questions aimed at evaluating the full SD model’s applicability along the dimensions of accessibility, importance, and suitability:

## Accessibility

Is the skill erosion model easy to understand?

Are the model’s concepts easy to understand?

Are the relationships between the concepts easy to understand?

## Importance

Is skill erosion a real problem in financial accounting practice?

Does this model address a real problem in financial accounting practice?

## Suitability

Does the skill erosion model provide new insights into your own practice?

Does the skill erosion model depict comprehensively how skill erosion occurs due to automation?

The sessions lasted 60 and 90 minutes, respectively. Both were audio-recorded with the participants’ permission, yielding 19,471 words of transcribed text. We analyzed the transcriptions in ATLAS.ti by first conducting open coding and then coding the data top-down along the dimensions of accessibility, importance, and suitability. The analysis resulted in 96 unique open codes that were applied to 141 excerpts.

All the participants regarded skill erosion as a relevant, timely topic that had already come up in discussions among their colleagues, and they felt that practitioners should pay more attention to it. They found the skill erosion model an important access point to comprehend the phenomenon and suitable for depicting how complacency and skill erosion can take hold:

I found it [the SD model] illuminating … it captures incredibly important aspects about skills and learning. … from the financial viewpoint, we are experiencing a push to automate as much as possible. But on the other hand, our professional credibility and people’s competence are at stake, so you need to somehow strike a balance. I think [the SD model] gives a lot in this regard. (Head of Development)

The participants considered the model as accessible too. In the words of the business development expert: “The model was pretty clear, and it made me think … it’s not only about getting people to use and understand the technology but also to consider that they may cease learning.” However, the participants did not have prior exposure to SD models and hence noted that the model alone could have been difficult to understand without a summary providing explanations of each concept and mechanism.

In addition to the discussion related to the three dimensions of applicability, the informants confirmed many of the concepts and relationships proposed in the model. For instance, the concept of mindful conduction resonated with Senior Accountant 1: “Yeah, about mindful conduction … it shows that even if a machine does things for you, it’s better to be aware of what it is doing so that you know to intervene if it makes a mistake. … While you should be able to trust it, you shouldn’t get totally complacent.” As supplementary insights to the model, the informants brought up possible humanistic outcomes of automation use, e.g., some degree of reliance on automation allowing to focus on more meaningful work tasks and how this helps to alleviate overall work pressure instead of just the onerousness of a particular work task. While this lends support to our model, it also represents an avenue for further research. In conclusion, the applicability checks provided further evidence for the validity and relevance of our model and theorizing.

## About the Authors

Tapani Rinta-Kahila is a lecturer of business information systems at The University of Queensland Business School. His research focuses on issues around the implementation and management of artificial intelligence systems in organizations, unintended consequences of IT use, and decommissioning of organizational IT systems. Tapani obtained his doctoral degree from Aalto University School of Business in 2018 with an award-winning dissertation. Rinta-Kahila’s research has appeared in top IS journals, including MIS Quarterly, Journal of the Association for Information Systems, European Journal of Information Systems, Information & Management, and MIS Quarterly Executive. His work has also informed practice through industry reports co-authored with The SAP Institute for Digital Government.

Esko Penttinen is an associate professor (tenured) of information systems at the Aalto University School of Business. Penttinen holds a DSc in information systems science and an MSc in economics from the Helsinki School of Economics. Penttinen’s research helps organizations understand the intricacies related to the design and implementation of various forms of artificial intelligence, harnessing its benefits and avoiding the pitfalls. Penttinen is an avid student of the interplay between humans and machines, curious to generate insights on how to coordinate work tasks efficiently between the two. Penttinen’s research has also addressed the more traditional information systems topics such as organizational governance issues related to outsourcing and virtual work. Penttinen’s main practical expertise lies in the assimilation and economic implications of interorganizational information systems, focusing on application areas such as electronic financial systems, government reporting, and electronic invoicing. Penttinen’s research has appeared in leading IS outlets such as MIS Quarterly, Journal of the Association for Information Systems, Information Systems Journal, Journal of Information Technology, International Journal of Electronic Commerce, MIS Quarterly Executive, and Electronic Markets.

Antti Salovaara is a senior university lecturer in the Aalto University Department of Design and an adjunct professor in the Department of Computer Science at the University of Helsinki. His research interests include human-AI collaboration, online trolling, and combining futures studies methods and theories with user studies methodology. His research has been published both in human-computer interaction and information systems journals and conferences, including CHI, Human-Computer Interaction, and International Journal of Human-Computer Studies, as well as MIS Quarterly, Journal of the Association for Information Systems, and European Journal of Information Systems.

Wael Soliman is an associate professor of information systems at the University of Agder. His research interests include information systems use lifecycle, cyber security, as well as philosophical discussions on research methods in IS. His work has been published in various journals, including Journal of the Association for Information Systems, Information Systems Journal, Information & Management, The Data Base for Advances in Information Systems, and European Journal of Innovation Management, among others.

Joona Ruissalo is a doctoral researcher in information systems science at the Aalto University School of Business. His research explores how the design, development, and use of cognitive technologies such as robotic process automation and artificial intelligence transform professional knowledge-intensive work. He currently studies these sociotechnical issues in the domain of financial accounting.

Copyright © 2023 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
