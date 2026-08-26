---
otero_id: 8230
otero_key: "E8DM53UW"
title: "Redesigning Reengineering Through Measurement-Driven Inference"
authors: "Mark Nissen"
year: "1990"
journal: "MIS Quarterly"
doi: "10.2307/249553"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Redesigning Reengineering Through Measurement-Driven Inference\*

By: Mark E. Nissen
Systems Management Department
Naval Postgraduate School
555 Dyer Road, Code SM/Ni
Monterey, CA 93943-5000
U.S.A.
MNissen@nps.navy.mil

## Abstract

This first decade of business process reengineering (BPR) is blemished by sporadic success, pathological performance, and inefficiency. Reengineering inefficiency is driven in part by cost and cycle time for process redesign, a process itself that requires deep reengineering knowledge and specialized expertise. However, such knowledge and expertise are not addressed by extant, first-generation redesign tools, so these intellectual activities must be performed manually at present, or provided through expensive BPR consulting services. Knowledge-based systems (KBS) address the requirements for knowledge and expertise directly, and they can augment first-generation tools to reduce redesign cost and cycle time, and hence increase reengineering efficiency. This study employs the methods and tools of reengineering recursively, to redesign the process of process redesign itself. Using measurement-driven inference, a second-generation KBS redesign tool called

KOPeR is developed to automate three key intellectual activities required for process redesign—process measurement, pathology diagnosis, and transformation matching. This KBS tool is used in the laboratory to redesign a commercial process from the reengineering literature and then employed in the field to redesign operational procurement processes in the context of an “industrial strength” reengineering project. The study finds that KOPeR-supported redesign enables new reengineering efficiencies in terms of direct automation effects and indirect knowledge effects. Results of this investigation highlight new opportunities available to the IS manager—such as improving the return on investment from BPR, enhancing the capability for knowledge management and organizational memory, and achieving competitive advantage through knowledge integration—opportunities that do not necessarily require KBS automation to seize. This investigation also lays a research cornerstone and foundation for development of process redesign theory and investigation of reengineering effectiveness.

Keywords: Business process reengineering, expert systems, knowledge-based systems, metrics, process measurement, process redesign.

ISRL Categories: AF10, AI0101, AL04, HA04, HB14

## Redesigning Reengineering

As the 10-year mark approaches for business process reengineering (BPR)—based on seminal articles by Davenport and Short (1990) and Hammer (1990)—the phenomenon has lost much of the hyperbole and attention in the management press that surrounded its early years. Yet few would argue the opportunities for performance improvement have been exhausted, or the need for process redesign has diminished. Rather, the same kinds of hypercompetitive pressures (D'Aveni 1994), global operations, and intensive customer demands that existed in the early 1990s continue to represent compelling forces for change today, and one can argue such forces are even stronger today than when the decade began. Although many in the management press have proclaimed BPR is “dead” (e.g., Harari 1996), others in academics and industry describe a “second wave” of reengineering (Caron et al. 1994), in which BPR assumes a broader role in the enterprise, even redefining business scope (Venkatraman 1994).

Research cautions that “first generation reengineering has been and remains very difficult to perform and to succeed,” and indicates the second generation of reengineering will be even more challenging than the first (Cypress 1994). Despite many redesign exemplars achieving dramatic, order of magnitude performance improvements (e.g., see Davenport 1993, Hammer and Champy 1993), reengineering has been blemished by sporadic success and pathological performance. The common “failure of many promising reengineering efforts” is noted (Davenport and Stoddard 1994), and research has found that roughly half of the redesign projects must be redone (Caron et al. 1994). Moreover, the second wave of BPR presents today’s manager with new information technologies and capabilities (e.g., mobile intelligent agents, virtual organizations, electronic markets, etc.) to consider when redesigning organizational processes, and the ever closer integration of enterprises’ supply-chain activities now has teams of customers, vendors, and suppliers working together on interorganizational process redesign. Process redesign with advanced technologies across organizational boundaries can represent a more difficult management problem than even the most radical and aggressive reengineering projects within a single firm.

Research to date has addressed several important reengineering questions. For example, we now have the benefit of results such as "preconditions for success" (Bashein et al. 1994), "tactics for managing radical change" (Stoddard and Jarvenpaa 1995), revelations of "reengineering myths" (Davenport and Stoddard 1994), and greater insight into implementation problems (Clemons et al. 1995; Grover et al. 1995). But questions pertaining to reengineering efficiency are relatively unexplored. "Efficiency" is defined as cost-effectiveness—the relative investment required to achieve acceptable efficacy or return on a BPR project. Reengineering inefficiency is driven in part by cost and cycle time for the redesign phase of the BPR life cycle (Guha et al. 1994). For example, estimates of annual reengineering costs to industry reach \$30 billion, including internal expenses for process redesign (Hammer and Stanton 1995), and BPR experience routinely involves redesign projects with million-dollar budgets, requiring a year or more to complete (see Burlton 1996). As has been noted,

"This timeframe is not consistent with the short-term cultures of American and Western businesses, and the consequent impatience of senior executives for measurable results. (Davenport 1995)"

Indeed, the high costs and long cycle times required for reengineering make the process of process redesign an attractive target for process redesign.

However, process redesign is a very knowledge-intensive endeavor, the kind that has proven difficult to redesign effectively (Davenport 1995). It requires deep, often distributed knowledge and specialized expertise—frequently provided by external BPR consultants—to perform the key intellectual activities required for effectiveness, and first-generation methods and tools are deemed inadequate for redesign today (Cypress 1994). Although CASE tools, process-diagramming applications, simulation packages, activity-based costing products, and similar information technology (IT) are routinely employed for redesign support, such tools do not address knowledge and expertise, hence they fail to automate and support key intellectual factors that drive redesign cost and cycle time.

The research described in this article is focused on using knowledge-based systems' (KBS) to redesign the process of process redesign. KBSs address deep, distributed knowledge and specialized expertise directly (Rich and Knight 1991) and they can augment first-generation tools to reduce reengineering time and expense (Hamscher 1994). Building upon proven KBS implementations such as MYCIN, SOPHIE, and the Articulator for automated diagnostics, this article defines a number of reengineering metrics from the literature and shows how these diagnostics and metrics can be used to automate and support the key intellectual activities required for effective redesign. Specifically, it employs the technique of measurement-driven inference—in both the laboratory and an “industrial strength” reengineering field project—in conjunction with a second-generation redesign tool to demonstrate opportunities to effect the same kinds of order-of-magnitude performance improvements generally sought through BPR on BPR. The article highlights new opportunities available to the information systems (IS) manager and lays a research cornerstone and foundation for development of process redesign theory and investigation of reengineering effectiveness.

## Measurement-Driven Inference

The term measurement-driven inference implies the use of metrics for automated reasoning. This section outlines a general redesign process as delineated in Figure 1 and describes how it is redesigned through measurement-driven inference and KBS support. To show how this second-generation approach addresses the redesign problems of deep knowledge and specialized expertise, it is employed in a pilot study to redesign a commercial reengineering case from the literature, using a proof-of-concept KBS called "KOPeR." The KOPeR architecture is described in Appendix A to outline its technical basis and structure.

The sequence of process-redesign activities delineated in Figure 1 represents a blend of expert reengineering methodologies—particularly those of Andrews and Stalick (1994), Davenport (1993), Hammer and Champy (1993), Harrington (1991), and Johansson et al. (1993)—synthesized to compose an analytical method supporting measurement. The path through these steps is delineated as a spiral in the figure, which represents a common notation for evolutionary processes (see Boehm 1988 for a discussion pertaining to software engineering). Step one is to identify a target process for redesign. Next, a model is constructed to represent the baseline (i.e., "as is") configuration of this process, and configuration measurements then drive the diagnosis of process pathologies. The diagnostic results are used in turn to match the appropriate redesign transformations available to "treat" pathologies that are detected. This sequence of analytical activities leads systematically to the generation of one or more redesign alternatives, which most experts argue should be tested through some mechanism (especially simulation) prior to selection of a preferred alternative for implementation. This baseline process is characteristic of first-generation redesign methods and tools, through which the three key intellectual activities—process measurement, pathology diagnosis, and transformation matching—are performed manually at present. These three redesign steps are specifically targeted for automation by KOPeR.

![](/api/attachments/E8DM53UW/fulltext/images/1fd34ee2f1ad82d7dd387968f0227c23d307a0aa585848d3cc6a41d54919994b.jpg)  
Figure 1. General Redesign Process

## Identify process for redesign

Reengineering experts (such as Davenport 1993, p. 27) advise that "major processes" with "strategic relevance" should be targeted for redesign, and (according to Hammer and Champy 1993, p. 122) heuristics for process selection include factors such as "dysfunction," "importance" and "redesign feasibility." Although this redesign study does not address the process-identification step per se, KBSs are oriented toward processes that involve knowledge application and information flows (e.g., "office work"). This orientation imposes two requirements: (1) that the process is stable and (2) that the constituent work activities are understood well enough to support representation in terms of a process model. Thus, if a process is not repeatable (e.g., ad hoc or single-shot work activities) or participants are unable to describe how the process is performed in terms of its constituent tasks (e.g., creative work, scientific discovery), it is probably inappropriate for measurement-driven inference.

## Develop process model

Development of a process model represents a standard reengineering practice recommended by experts (e.g., see Davenport 1993; Harrington 1991) and process modeling is well-supported by first-generation redesign tools. This research takes advantage of the fact that most process models developed in practice are now graphical and computer-based (see Curtis et al. 1992). A graphical process model represents the starting point for measurement-driven inference. Figure 2 illustrates an example process model used by KOPeR. This process involves four tasks (A, B, C, D) and three work objects (doc1, doc2, doc3). Each process task is represented by a node in the graph, which is linked by a directed edge to exactly one other task in a simple, linear process flow. Process attributes are shown below each activity node. For example, Task A has three attributes shown: (1) activity name ("Check"), (2) role of the assigned agent ("Check-agent"), and (3) IT resource used for support ("DBMS"). The same follows for the other three process activities.

## Redesign Modeling Example

An example from the reengineering literature is introduced for the pilot study. The particular example delineated in Figure 2 represents a snippet of workflow activities adapted from the well-known credit financing process (described by Hammer and Champy 1993, pp. 36–39). Here the first task is associated with performing a credit check and is accomplished by a specialist (denoted by a specific role: Checkagent) supported by a database (DBMS). Similarly, another specialist agent (Priceagent) performs the pricing task using a decision support system (DSS), followed by a third specialist (Terms-agent) who composes the appropriate terms and conditions for financing using a word processor. A manager agent is included at the end of this example to review the financing package, and a feedback or quality loop is indicated to denote a path for rework. This notation also indicates that a separate document is created at each of the first three task nodes (e.g., doc1 is created at Task A; doc2 is created at Task B; etc.) and that all three documents flow to the end node at Task D. This pilot example continues throughout the section.

![](/api/attachments/E8DM53UW/fulltext/images/e01cd10ca9d8c60e386fd422e0b619cba04f9d762f973548cf1fd8b2fe78db90.jpg)  
Figure 2. Example Process Model

## Measure process configuration

Process measurement, which must be performed manually at present, represents the first redesign activity targeted for KOPeR automation. To develop a set of process measures, this article draws from two classic diagnostic rule-based systems called SOPHIE (see Brown et al. 1982) and MYCIN (see Shortliffe 1976). SOPHIE uses system measurements to drive automated diagnosis of faults in electronic circuits, and MYCIN similarly employs blood-cell counts to diagnose bacterial infections in people. The deep knowledge and expert-level performance of these KBS are similar to key intellectual requirements for process redesign. Adapting techniques from SOPHIE and MYCIN development, available domain theory is examined to develop a set of empirical measures to drive problem diagnosis and reach beyond the theory-sparse reengineering domain (see Saharia et al. 1994). Process measures are drawn from fields such as Statics (e.g., measures including length, breadth, and depth), Artificial Intelligence (e.g., variables such as problem size, parallelism/decomposability, and feedback/cycles), Information Systems (e.g., uses of IT such as support, communication, and automation) and others (e.g., Coordination Theory, Organizational Behavior, Total Quality Management (TQM)). Notice these fields are independent from reengineering-specific methods and cases. Such independence is stressed as a knowledge engineering technique to increase the robustness of KOPeR. A detailed description of this measure-development process can be found in Nissen (1996).

It should be noted that this set of measures is not intended to be complete at this point in the exploratory investigation. Rather, the idea is to develop a relatively small, fundamental set and examine the use of such measures to drive redesign inference, particularly in terms of their heuristic value for diagnosing process pathologies. Nonetheless, the ability of a few, fundamental measures to support the development of a robust analytical capability is well known. In the physical sciences, for example, nearly all measurement in physics, engineering, and like disciplines can be traced to a set of just six fundamental measures—charge, temperature, mass, length, time, and angle (Krantz et al. 1971).

Automated measurement requires each process measure to be operationalized explicitly using the node, edge, and attribute constructs from above. For instance, process length is defined as the number of task nodes connected together in the longest path through the process model, process breadth is defined as the number of distinct paths through the representation, and so forth. Procedures for dealing with branch nodes, cycles, and multiple levels of decomposition are straightforward (e.g., count the longest OR branch for measuring process length; count the steps associated with a cycle once; etc.). Consistency of application represents a more important factor than selecting any one procedure over another (especially to support comparative process analysis). A set of example process measures is presented in Table 1 along with their corresponding graph-based definitions.

Table 1. Example Process Measures

<table><tr><td>Measure</td><td>Graph-Based Definition</td></tr><tr><td>Process Length</td><td>Number of nodes in longest path</td></tr><tr><td>Process Breadth</td><td>Number of distinct paths</td></tr><tr><td>Process Depth</td><td>Number of process levels</td></tr><tr><td>Process Size</td><td>Number of nodes in process model</td></tr><tr><td>Process Feedback</td><td>Number of cycles in graph</td></tr><tr><td>Parallelism</td><td>Process Size divided by Length</td></tr><tr><td>IT Support</td><td>Number of IT-support attributes</td></tr><tr><td>IT Communication</td><td>Number of IT-communication attributes</td></tr><tr><td>IT Automation</td><td>Number of IT-automation attributes</td></tr><tr><td>Organizational Roles</td><td>Number of unique agent role attributes</td></tr><tr><td>Process Handoffs</td><td>Number of interrole edges</td></tr><tr><td>Organizations</td><td>Number of unique agent organization attributes</td></tr><tr><td>Value Chains</td><td>Number of unique activity Value Chain attributes</td></tr></table>

![](/api/attachments/E8DM53UW/fulltext/images/70eaccad10f9a2930271219a3191f3e51e3db91100907868995dd00871e110c9.jpg)  
Figure 3. Example Process Measurements

## Redesign Measurement Example

The credit financing model from above is continued in Figure 3, this time with example process measurements based on definitions from the table. For instance, the process is seen as four steps long (i.e., length = 4), has one path through it (i.e., breadth = 1), and is represented at a single hierarchical level (i.e., depth = 1). Process size (4) accounts for the four activities, and the one feedback loop is counted (feedback = 1). Interestingly, the parallelism measurement (1.00 = 4/4) represents a theoretical minimum for this measure. Notice how this minimum parallelism (i.e., maximum linearity) reflects the serial layout and linear appearance of the process. The IT measurements are taken from corresponding IT attributes in the model (e.g., the DBMS, DSS, and word processor each count toward the IT-support value of 3). Using this example, the article shows how such process measures can be used to drive the automatic diagnosis of pathologies.

## Diagnose process pathologies

Pathology diagnosis represents the second redesign activity targeted for KOPeR automation. To develop a measurement-driven diagnostic capability, a taxonomy of process pathologies to be used for classification of problems and shortcomings is introduced. This taxonomy formalizes some of the deep reengineering knowledge required for process redesign. The idea is to use process configuration measurements to detect and classify a variety of common process pathologies. The taxonomy is constructed from the BPR literature, as classes and instances of pathologies are synthesized from the various process problems and shortcomings noted in the expert reengineering methodologies from above (e.g., Andrews and Stalick 1994; Davenport 1993). The problematic conditions described in the many published redesign cases (e.g., Goldstein 1986; King and Konsynski 1990; Stoddard and Meadows 1992; Talebzadeh et al. 1995) are similarly used to organize and populate the taxonomy. As with the set of candidate process measures above, the present taxonomy is intended to be representative and extensible, not necessarily complete. The class-level taxonomy of process pathologies is presented in Table 2 along with a sample instance from each of the 10 classes.

Table 2. Taxonomy of Process Pathologies

<table><tr><td>Pathology Class</td><td>Sample Instance</td></tr><tr><td>Problematic process structure</td><td>Sequential process flows</td></tr><tr><td>Bureaucratic organization</td><td>Job specialization</td></tr><tr><td>Fragmented process flows</td><td>Process friction</td></tr><tr><td>IT infrastructure</td><td>Manual process</td></tr><tr><td>“Checking” approach to quality</td><td>Review-intensive process</td></tr><tr><td>Centralized authority</td><td>Long decision chains</td></tr><tr><td>Under-utilized human potential</td><td>Training emphasis</td></tr><tr><td>Inhibitive leadership</td><td>Directive supervision</td></tr><tr><td>Centralized information</td><td>Central database architecture</td></tr><tr><td>Deficient core competency</td><td>Low IT expertise</td></tr></table>

Many of the process measures from above can be used to detect pathologies set forth in this taxonomy. For example, the first listed class, "problematic process structure," refers to problems stemming from the layout of process workflows. The corresponding sample instance, "sequential process flows," is widely noted in the reengineering literature as problematic (e.g., Hammer and Champy 1993, p.54), particularly with the associated implications in terms of cycle time for a process. Notice from above the parallelism measure can be used to detect this process pathology; that is, a (low) parallelism measurement quantifies the extent to which a process structure is laid out in terms of sequential workflows.

As another example, the bureaucratic organization is likewise widely noted in the reengineering (and quality) literature as problematic (e.g., Flood 1993; Hammer and Stanton 1995; Hoffherr et al. 1994). Bureaucratic problems are noted as being particularly severe in terms of maintaining a specialized workforce (i.e., "job specialization") and cycle-time delays associated with fragmented work handed-off from one functional organization to another (i.e., "process friction"). The organizational roles and process handoffs measures from above can be used to detect these respective process pathologies; that is, a (high) roles measurement quantifies the extent to which an organizational design reflects job specialization and a (high) handoffs measurement similarly signals fragmented process flows and the associated friction. As a third example, inadequate IT infrastructure is probably the most widely noted process pathology in the reengineering literature, as deficiencies in this area such as low IT support (i.e., "manual processes") and paper-based communications have implications that include cost, cycle time, quality, and many other performance objectives. Notice from above that the IT support and IT communication measures can be used to detect these process pathologies.

Despite the promising diagnostic potential seen in these three examples, however, not all pathologies correspond to measures that offer the same level of diagnostic capability. This is because the taxonomy and associated measures are developed independently and from separate sources of literature. As two cases in point, measures that offer such potential to detect the “training emphasis” and “directive supervision” pathologies listed in Table 2 have yet to be developed. This highlights a weakness of measurement-driven inference: not all heuristically valuable diagnostic concepts can be operationalized in terms of graph-based measures.

## Redesign Diagnosis Example

Referring back to Figure 3, it was noted that the parallelism measurement (1.00) reflects the serial layout and linear appearance of the process and indicated that its unit value represents a theoretical minimum; that is, the graph-based measure is defined such that a process cannot have measured parallelism lower than unity. This implies that a process with unit parallelism is absolutely linear or sequential, by definition. Thus, KOPeR can infer a process measured with unit parallelism suffers from the pathology “sequential process flows,” an instance of the class “problematic process structure.” This example is representative of the measurement-driven diagnostic approach employed by KOPeR. Inference based on other measures and pathologies is performed in a like manner and can be accomplished by KOPeR through straightforward, rule-based reasoning. For example, using structured English for clarity, a simple IF-THEN rule can be written to classify this pathology directly.

$$
\text { IF   parallelism } = 1. 0 0
$$

$$
\text { THEN   pathology } = \text { ``sequential   process   flows'' }
$$

A more interesting situation arises when the measured value for a dimension does not correspond exactly to an extremum, as would be the case with a parallelism value above this minimum (e.g., 2.00, 3.37, etc.). In such a situation, benchmarking or like information that is specific to a particular domain, industry, or process family is required to calibrate the measurement gauge. For example, a measured parallelism value of 2.00 certainly indicates a process that is more parallel than the one diagrammed in the figure above, and it can even be said that such a process has twice the parallelism using a ratio scale (see Roberts 1979 for discussion, Nissen 1996a for proof). But for diagnostic purposes, whether this degree of parallelism is pathological or not needs to be known for the specific process being analyzed by KOPeR (i.e., credit financing in this case). This is where the domain-specific benchmarking information is employed. In the case of credit financing, for example, say best organizational performance in the industry corresponds to parallelism of 3.37. The rule from above can be extended to incorporate such benchmarking information.

$$
\text { IF   parallelism } <   3. 3 7
$$

$$
\text { AND   process   family } = \text { ``credit   financing'' }
$$

$$
\text { THEN   pathology } = \text { ``sequential   process   flows'' }
$$

Similar rules can be developed to extend the approach to other domains, industries, and process families, and this quantitative measurement scheme can be used to detect and interpret both "high" and "low" measured values for configuration variables (analogous to the "two-tailed test" in statistics). For example, the same rule set above can be augmented to detect too much parallelism, as well as too little, through the addition of a rule such as the following.

$$
I F \text { parallelism } > 6
$$

$$
\text { AND   process   family } = \text { ``credit   financing'' }
$$

$$
\text { THEN   pathology } = \text { “chaotic   process   flows” }
$$

Application of the other process measurements to classify pathologies follows a similar approach. It is important to re-emphasize that the graph-based measures are developed independently from the taxonomy of process pathologies. This represents a strength of the approach, in that the general set of measures should be relatively robust to the idiosyncrasies and differences associated with specific process instances and allow for extension and refinement of the taxonomy. However, it should also be emphasized that the measurements are used heuristically and are in no way guaranteed to be useful in terms of classifying pathologies. Use of heuristic problem solving highlights another limitation of the approach.

## Match redesign transformations

Transformation matching represents the final redesign activity targeted for KOPeR automation. To develop a measurement-driven matching capability, a taxonomy of redesign transformations is introduced to be used for matching with pathologies. This taxonomy formalizes additional, deep reengineering knowledge required for process redesign. The idea is to use the measurement-driven, diagnostic information from the steps above to match appropriate transformations. This taxonomy is also constructed by drawing from the BPR literature, as classes and instances of redesign transformations are synthesized from the various enabling technologies, organizational changes, workflow modifications, and like interventions noted in the expert reengineering methodologies. Redesign transformations described in the many published BPR cases are similarly used to organize and populate the taxonomy. The class-level taxonomy of redesign transformations is presented in Table 3 along with a sample instance from each of the seven classes.

The first class of redesign transformations is labeled "workflow reconfiguration." This class pertains to process changes that simply rearrange the layout of workflows; in other words, they affect the sequencing of process activities and flow of work, but not how or by whom the activities are performed. Process de-linearization—rearranging serial process activities to be performed more in parallel—represents one example of a transformation from this class. The addition of a "triage step" (see Hammer and Champy 1993, p. 55), for example, would also fall into this class. Similarly, a shared database system represents an instance from the IT transformation class, as are decision support systems, local area networks, and like information systems and their associated infrastructure. In fact, most of the IT-based enabling technologies cited throughout the reengineering literature (e.g., see Hammer and Champy 1993, pp. 92-99) would fall into this second class of transformations. Other transformations, such as organizational design changes associated with instituting a case manager position, follow the same class-instance structure of the taxonomy.

Table 3. Taxonomy of Redesign Transformations

<table><tr><td>Transformation Class</td><td>Sample Instance</td></tr><tr><td>Workflow reconfigurationInformation technologyOrganizational designHuman resourceInformation availabilityInter-organizational allianceManagement &amp; culture</td><td>Process de-linearizationShared database systemCase managerTeam-based compensationInformate agentsSupplier-managed inventoryEmployee stock ownership</td></tr></table>

## Redesign Matching Example

Referring again to the measures presented in Figure 3, it is noted that the unit parallelism measurement drives inference to diagnose the pathology “sequential process flows.” As above, a straightforward rule can be written to match this pathology with an appropriate transformation. The relevant diagnostic measurement is noted next to this rule for reference.

```txt
IF pathology = "sequential process flows" (parallelism = 1.00)
THEN redesign transformation = "delinearization"
```

Other pathologies and recommended redesign transformations for the credit financing case follow from similar rules. It is interesting to note several of these latter transformations correspond to the redesign interventions actually recommended and employed in the case. For example, the “case manager” recommendation can be obtained directly from KOPeR.

```toml
IF pathology = "job specialization"
(roles = 4)
AND pathology = "process friction"
```

(handoffs = 3)

THEN redesign transformation = "case manager"

As another example, the “shared database system” recommendation in the case is independently considered by KOPeR, but the KBS “disagrees” with the BPR experts and consultants in the case (i.e., about the shared database approach). KOPeR suggests instead to link the three, separate IT-supported activities through e-mail. Had the IT-support measurement (3) been lower, KOPeR would have also recommended the database transformation implemented in the case.

```txt
IF pathology = "paper-based process"
(IT communication = 0)
AND pathology = "process friction"
(handoffs = 3)
THEN redesign transformation =
"e-mail system"
(IT support = 3)
```

It is important to re-emphasize the diagnostic measures are developed with complete independence from this or any other specific case. The deep reengineering knowledge formalized through taxonomies and specialized redesign expertise effected through rule-based reasoning enable KOPeR to perform key intellectual activities required to redesign this case, independently and autonomously. Thus, KOPeR should be expected to perform with comparable knowledge and expertise when redesigning any process involving similar kinds of knowledge and information work.

Generate, test, and select redesign alternatives

Regarding generation of alternatives, each redesign transformation from above is tantamount to a consultant-like recommendation for process change. Applying one or more of the redesign transformations matched by KOPeR produces the corresponding alternative (i.e., "to be") process models intended to improve process performance. For example, a redesign alternative generated by KOPeR for credit financing is shown in Figure 4 as the result of applying the "delinearize" transformation to tasks B and C (serially independent). It should be noted that cycle-time reducing transformation is not even mentioned in the case.

Simulation-based testing is useful to compare the relative performance associated with multiple, competing redesign alternatives—prior to implementation—and it represents a powerful analytical method that is particularly useful for evaluating alternatives that are either too expensive or time-consuming to test physically (Law and Kelton 1982). Simulation represents a well-established area of study, supported by an abundance of methods, tools, and experience. And when care is taken to validate simulation models against the performance of their physical counterparts in operational processes, the results can be quite dependable (see Bitauld et al. 1997; van Mael 1993; van Mael et al. 1995). An even greater abundance of decision methods, tools, and experience is available to guide and support the selection of a preferred redesign from multiple alternatives, the final redesign step.

![](/api/attachments/E8DM53UW/fulltext/images/9fa6b8fca8858c0bf6dbea5f4236706564050405603d86115ba69bd2f3333e4f.jpg)  
Figure 4. Redesign Alternative ("to be") Model

To summarize, through KOPeR, deep reengineering knowledge and specialized redesign expertise is captured and formalized, and a second-generation KBS tool to automate three time-consuming intellectual redesign activities—process measurement, pathology diagnosis and transformation matching—is developed. In this pilot project, it can be seen how KOPeR applies its knowledge and expertise to redesign a credit financing process and noted that KOPeR-generated recommendations match several of the redesign transformations actually employed in the case. KOPeR even recommends promising transformations (e.g., delinearizing sequential activities) not mentioned in the case. This KBS automation should contribute directly to reduce cost and cycle time for process redesign in the field, and hence increase redesign efficiency.

## Redesign in the Field

This section summarizes the results of employing KOPeR in an “industrial strength” reengineering context to redesign the procurement processes performed at a large, multi-site military enterprise on the West Coast of the U.S.. This field example demonstrates the operational capability and performance of KOPeR and enables identification of a number of efficiency effects achieved through KBS-supported redesign. This section concentrates on high-level redesign results. Field study details are provided in Appendix B to describe the reengineering context and procurement processes in greater depth.

## Redesign performance

This section begins by summarizing the performance of KOPeR-supported redesign in the field and focuses on justification and approval (J&A), a relatively small but complex procurement process that is insightful for discussion.

The J&A process is involved with all sole-source or “other than full and open competition” procurements in the government, is expressly required by regulation, and has been identified by senior procurement officials as particularly important and dysfunctional. The J&A process model is comprised of 31 activities. KOPeR’s measurement-driven inference results in the generation of the eight redesign alternatives listed in Table 4, along with the matching pathologies shown for reference (see Appendix B for details such as process models, measurements, and diagnoses).

Each of the redesign alternatives is subsequently assessed by a team of process experts on the basis of feasibility, implementability, and perceived benefit, and two KOPeR-generated alternatives—a joint J&A review process and an automated contracts workflow system—are deemed by the experts to be “preferred” (i.e., superior). The team of process experts expresses satisfaction with the appropriateness, number, and diversity of redesign alternatives that are generated, and this group is unable to identify an additional, substantive alternative that they also deem to be feasible. Through a series of discussions and project reviews, the procurement experts and managers indicate that KOPeR demonstrates an “acceptable” level of effectiveness through its redesign recommendations, and its redesign analysis is deemed to be “quite complete" by the redesign team (Project Reviews 1995).

Simulation results (see Appendix B for a discussion of the validation and simulation procedures) for the two preferred J&A redesign alternatives are presented in Table 5. From the table entries, it is seen (coincidentally) that both KOPeR-generated redesigns produce a two-thirds reduction in simulated cycle time, which exceeds a performance-doubling threshold established for the field study. This threshold is intended to differentiate between “dramatic” performance improvements (i.e., as sought through BPR) and “incremental” gains (i.e., reflecting more of a TQM approach). Based on this threshold, the simulated cost improvements are negligible to modest, however. Nonetheless, the quantum cycle-time reductions are deemed by the procurement managers to represent “impressive” opportunities for performance improvement. The managers also indicate cycle-time reduction represents their most critical performance goal for this reengineering engagement.

Based in part on the recommendations from KOPeR and these simulated performance results, the managers select the contracts workflow system for implementation in the organization. Moreover, several other (manual, paper-based, high-friction) procurement processes investigated through this study turn out to suffer from the same pathologies. Thus, it can be inferred that the workflow system transformation can leverage its performance gains across an entire class of processes. Indeed, such leverage extends even beyond the specific, military enterprise examined in this investigation. Since the time of the field investigation, this contracts workflow system transformation has subsequently been selected for defense-wide implementation at over 900 sites around the world, and a system provider is now under contract to adapt a commercial workflow product to support military procurement.

Table 4. Redesign Alternatives

<table><tr><td>Diagnosed Pathology</td><td>Recommended Transformation</td><td>Redesign Alternative</td></tr><tr><td>Sequential process flows + review-intensive process</td><td>Delinearize (approvals)</td><td>1. Concurrent reviews</td></tr><tr><td>Sequential process flows + review-intensive process</td><td>Delinearize (approvals)</td><td>2. Joint reviews</td></tr><tr><td>Manual process + paper-based process + process friction</td><td>Shared database + e-mail</td><td>3. E-document infrastructure</td></tr><tr><td>Manual process + paper-based process + process friction + labor-intensive process</td><td>Workflow management system</td><td>4. Contracts workflow system</td></tr><tr><td>Job specialization + process friction</td><td>Case manager</td><td>5. J&amp;A case team</td></tr><tr><td>Job specialization</td><td>Empowerment (3)</td><td>6-8. CS and KO job enlargement</td></tr></table>

Bold denotes "preferred" redesign alternative.

Table 5. Redesign Simulation Results

<table><tr><td>Redesign Alternative</td><td>Cycle Time Reduction</td><td>Cost Reduction</td></tr><tr><td>Joint Reviews</td><td>67%*</td><td>28%</td></tr><tr><td>Contracts Workflow System</td><td>67%*</td><td>nil</td></tr></table>

\* Denotes performance-doubling.

## Redesign efficiency

The basis for comparison of KOPeR-supported redesign is relative efficiency with respect to the same, analytical redesign process performed without KBS support. The primary redesign efficiency effects resulting from this study are summarized in Table 6 and discussed in turn.

## Automation Effects

As the name implies, automation effects accrue directly from the automation of manual tasks accomplished by KOPeR. They include the kinds of “automational” impacts (especially speed-up of work) generally expected from using IT to transform manual activities (see Davenport 1993, p. 51). Recall the general redesign process delineated in Figure 1 and the reports from the BPR practice of million-dollar budgets and redesign projects requiring a year or more to complete. KOPeR automates three of these activities—process measurement, pathology diagnosis, and transformation matching—each of which must be performed manually without KOPeR. This reduces cost and cycle time required for process redesign directly.

For example, using the proof-of-concept KOPeR implementation in this study, the redesign team requires roughly two hours to perform these three, intellectual activities for a particular process. For the purpose of comparison, cycle times for the same team to accomplish this analysis manually range from several days for a small process like the J&A to several weeks for a large process. $^{3}$ Further, recall from Figure 1 the use of a spiral to delineate the evolutionary nature of the redesign process. Experience shows that management is rarely satisfied with the first redesign analysis completed by a team, and it is not unusual for these analytical steps to be repeated many times during the course of a redesign project. These KOPeR gains (i.e., two hours vs. days to weeks) apply to each iteration of the redesign process. Moreover, KOPeR uses as input exactly the same, graphical process models that are generated for manual analysis, and its output recommendations provide the basis for the same simulated performance comparisons that are required to evaluate manually generated redesign alternatives. In other words, KOPeR-supported redesign requires no additional process activities and it automates three analytical steps that are known to be time consuming.

Table 6. Redesign Efficiency Effects

<table><tr><td>Automation Effects+ Speed-up manual redesign work- KOPeR maintenance</td><td>Knowledge Effects+ Analytical consistency &amp; completeness+ Formalization &amp; distribution of BPR knowledge+ Integrate knowledge from multiple BPR experts</td></tr></table>

Also noted is a minor efficiency loss associated with the need to maintain KOPeR. As with most information systems, KOPeR requires periodic support to follow technological advances (e.g., computer hardware upgrades), port to different platforms (e.g., UNIX to Windows migration), and like maintenance activities, which are not required for a manual redesign process. Additionally, KOPeR's knowledge and expertise must be kept current, and each application to a new domain, industry, or process family requires a corresponding knowledge update. Likewise, KOPeR must keep up with advances in IT and redesign techniques to remain effective. And although it is not difficult to use the system, at least one person in the organization must be trained to redesign with the KOPeR tool. These factors cannot be quantified at present, but KOPeR maintenance negatively impacts redesign efficiency to some extent.

Nonetheless, from the KOPeR usage observations and estimates for the manual redesign process, the net efficiency gains derived from KOPeR-supported redesign reflect improvement of an order of magnitude or more for the three intellectual activities automated through KOPeR. When combined with the redesign activities unaffected by KOPeR use, the cost and cycle time required for KOPeR-supported process redesign are noticeably lower than the levels required to redesign manually. For example, KOPeR enables the redesign of three military procurement processes to be completed through this study in roughly four months. As noted, "Even the fastest [single] project involves roughly six months to assemble a team, decide what to do, and then create a new design" (Davenport 1995).

## Knowledge Effects

Knowledge effects accrue indirectly through the support of redesign tasks provided by KOPeR. They include the kinds of “informational,” “analytical,” and “intellectual” impacts described by Davenport (pp. 51-54), who notes, for example, “information can be used not just to eliminate human labor from a process, but also to augment it.” In this study, three noteworthy examples of this knowledge effect are identified: (1) analytical consistency and completeness, (2) formalization and distribution of reengineering knowledge, and (3) integration of knowledge from multiple experts.

"Analytical consistency" here means the reliability and traceability of "consultant" analyses and recommendations across various redesign instances, projects, or engagements. For example, management says it prefers consistent reasoning and analysis for the redesign of different processes—regardless whether conducted by the same or different individuals—and it demands consistency between successive redesigns of the same process at different times (e.g., successive redesign iterations). Because KOPeR employs a known and documented knowledgebase (e.g., rule set, taxonomies, measures), it follows the same, understandable and explainable reasoning steps regardless of the specific process being redesigned (e.g., small or large, simple or complex, etc.) and produces the same results when redesigning any particular process at different points in time. KOPeR recommendations are also independent of the specific individual who uses the tool, and the system does not suffer from inter-rater or interapplication bias the way a person or group can. "Analytical completeness" means the ability to include all appropriate redesigns in a set of generated alternatives. Again, measurement-driven inference follows a known set of rules and inferential mechanics, so KOPeR is complete in its generation of redesign alternatives, up to the level of its formal knowledge; that is, if KOPeR "knows" that a particular redesign alternative offers potential as an appropriate transformation (i.e., resident in the knowledgebase), then it is guaranteed to "remember" (i.e., match) that alternative.

In the operational redesign context, it is possible to observe how analytical consistency and completeness improve efficiency through a reduction in managerial oversight required for the redesign engagement. For example, it is found that once the procurement managers learn to understand KOPeR's measurement-driven inference and gain a degree of confidence in its reliability, predictability, and completeness, they reduce the number of time-consuming status briefings, reviews, and like meetings (pejoratively referred to as "dog and pony shows" by the redesign participants) required for subsequent redesigns. This result is despite the fact that processes redesigned subsequent to the J&A are substantially larger and more complex. Although this managerial "comfort level" would be expected to increase during the course of any multi-process redesign engagement, the managers describe an "additional degree of confidence" associated with KOPeR use.

The “formalization and distribution of knowledge” means the ability to capture and formalize expert-level knowledge and make it available to augment the redesign performance of non-experts in the organization. The efficiency effect follows from the ability to employ less-experienced people (presumably at lower salary/fee levels) to redesign processes internally, to reduce the need for external BPR consulting services, and to support multiple redesign projects simultaneously, even at remote locations. In the case of the military sponsor of this study, its list of personnel does not include a reengineering expert and it cannot afford to hire one. Neither can it afford the services of an external BPR consultant. Yet the command recognizes the need to redesign several important processes and anticipates process redesign as an enduring enterprise requirement. The managers indicate they do not want to hire BPR experts and train them to understand procurement. Rather, they expect some of their best procurement professionals to participate in redesign projects, in addition to their normal duties. KOPeR enables these procurement professionals to analyze and redesign multiple operational processes, without the need for external consulting services, and to do so across several geographically dispersed sites with effective redesign performance.

Finally, the impact of knowledge integration from multiple experts can also play an important role in terms of redesign efficiency. Using an instance of a more mature application from the chess domain for comparison, the fact that a KBS called Deep Blue recently beat the world chess champion provides evidence that the performance of a machine endowed with knowledge from multiple experts can exceed that of even the best expert individually. This evidence is even stronger when one considers that the world chess champion did not participate on the team that implemented Deep Blue, and that none of the people who did participate possessed the skill to beat the champion individually. In this present research, recall that the reengineering publications of multiple experts were integrated and used to formalize redesign knowledge, and this integrated knowledge was employed to endow KOPeR with the ability to automate key intellectual activities required for process redesign. At the time of this writing, KOPeR certainly possesses greater reengineering knowledge and expertise than any of the procurement professionals who are involved with the redesigns, and for the military command investigated in this study, the second-generation redesign tool suffices in lieu of external BPR consulting services. Compounding the automation and knowledge effects from above, this increases reengineering efficiency even further.

## Management and Research Opportunities

BPR is far from “dead.” Rather, a “second wave” of reengineering is being observed that promises to be broader in scope and more challenging than BPR experience to date, and the phenomenon is changing already. Largely gone, for example, is the reckless, somewhat frenzied pursuit of “radical change” (see especially Hammer 1990) and the “Greenfield approach” (see Kettinger et al. 1995 for characterization), which neglects analysis of a process baseline before reengineering. Instead, a more sober, methodical approach predicated upon baseline analysis to support systematic process redesign is now observed. But process redesign, a costly and time-consuming driver of reengineering inefficiency, is itself a process that requires deep reengineering knowledge and specialized expertise. Such knowledge and expertise are not addressed by extant, first-generation redesign tools, so these intellectual activities must be performed manually at present, or provided through expensive BPR consulting services. Knowledge-based systems address the requirements for knowledge and expertise directly.

This study employed the methods and tools of reengineering recursively, to redesign process redesign. Using measurement-driven inference, a second-generation KBS tool called KOPeR is developed to automate three key intellectual activities required for process redesign—process measurement, pathology diagnosis, and transformation matching. One finding is that KOPeR-supported redesign enables new reengineering efficiencies in terms of direct, automation effects and indirect, knowledge effects. The results of this investigation highlight new opportunities available to the IS manager, opportunities that do not necessarily require KBS automation to seize. Three such opportunities are explored in terms of actionable managerial recommendations, and two promising topics are explored in terms of future research.

## Re-examine the process of process redesign in your organization

The redesign efficiencies noted above are not limited to the military-procurement context of this study. Process redesign is similar to other important knowledge-work processes in that it suffers from serious pathologies such as low IT automation. By refocusing the methods and tools of redesign—even first-generation—to analyze and transform the process of redesign itself, efficiencies in terms of decreased cost and cycle time may be realizable in any organization's reengineering projects. If reengineering is here to stay, and it promises to be even more challenging in the future, an efficient redesign process may make the difference between good return on investment from BPR or continuing the tradition of sporadic success and pathological performance.

## Capture reengineering knowledge and expertise in your enterprise

For many enterprises, knowledge capital is as critical as financing or plant and equipment. A KBS is not required to capture and formalize knowledge. For example, even though the knowledge taxonomies and diagnostic measures are developed in this study for automated problem solving by KOPeR, there is no reason why a person cannot apply this formalized knowledge to redesign a process manually. Indeed, this article explains the redesign of a credit financing process step by step, in a manner that supports analysis by hand as well as automated inference. The formalization of reengineering knowledge and expertise even if effected through non-automated means such as a searchable intranet—presents opportunities to augment the ability of less-experienced personnel, reduce the need for external BPR consulting expenses, and support multiple, geographically dispersed projects simultaneously. These benefits can accrue in addition to enhancing an enterprise's capability for knowledge management and organizational memory, both of which appear critical in the information-based organization of today (see Drucker 1988).

## Integrate enterprise knowledge from other domains

The knowledge effects identified through this investigation need not be limited to the reengineering domain. Any intellectual activities involving knowledge application and information flows offer potential for enhancement through the same kind of knowledge integration achieved in this study. Logical candidates include processes such as software management, new-product development, market analysis, consulting, and similar knowledge-intensive activities, for which experience exists and experts are able to articulate the problem-solving tactics associated with their work. In addition to the benefits above, recall from the Deep Blue example that integrated knowledge from multiple experts can enable performance levels that exceed any of the experts' capabilities individually. As intellectual capital and knowledge creation play increasingly important roles in tomorrow's economy (see Forbes 1997), the ability to employ integrated knowledge in the core competencies of an enterprise may provide an unprecedented basis for competitive advantage.

## Investigate reengineering effectiveness

The line of research begun with this article need not be limited to investigating reengineering efficiency. Several aspects of the knowledge-based approach to process redesign—whether automated or performed manually—also offer promise to enhance BPR effectiveness, particularly through the knowledge effects discussed above. For example, in addition to the cost and time savings noted, one can argue knowledge effects such as analytical consistency and completeness also improve the quality of process redesign, and the effect of formalizing and distributing knowledge through an enterprise may increase the reengineering performance level as well. Moreover, the potential associated with knowledge integration has clear implications in terms of reengineering efficacy. The IS literature is silent on these efficacy questions at present.

## Develop process redesign theory

Through this research, a new knowledge in terms of process redesign is developed. For example, the KOPeR taxonomies capture chunks of reengineering knowledge from disparate sources and organize them in terms of a hierarchical scheme that supports classification. The graph-based measurement approach operationalizes a number of important reengineering concepts in a manner that enables novel, empirical description and quantitative analysis. Moreover, the rules developed for KOPeR expressly formalize the redesign expertise required to diagnose process pathologies and match appropriate transformations for performance improvement. This reengineering knowledge provides conceptual and analytical linkages between an empirically measurable process configuration and the enabling technologies or other transformations able to dramatically improve performance. These linkages can provide a conceptual grist for development of process redesign theory. Such theory would augment current, descriptive capabilities (e.g., to describe diverse enterprise processes and redesign transformations) with new power to explain why certain BPR projects succeed where similar ones fail and predict which transformations are likely to produce the best return on investment in BPR. Capabilities such as explanation and prediction represent fundamental objectives of theory building (Bacharach 1989) and do not exist today in the reengineering domain. One objective of this research was to lay a cornerstone for development of such theory.

## Endnotes

1 The preference here is to use the more general term knowledge-based systems to acknowledge that performance of an intelligent system need not be at the level of an “expert” in order for the application to be effective.

$^{2}$ KOPeR (pronounced “cope-er”) is short for Knowledge-based Organizational Process Redesign.

$^{3}$ Processes investigated through this field research range in size from 31 to 842 modeled activities. Manual cycle times are estimated by the redesign team.

## References

Andrews, D. C., and Stalick, S. K. Business Reengineering: the Survival Guide,

Yourdon Press Computing Series, New York, 1994.

Bacharach, S. B. "Organizational Theories: Some Criteria for Evaluation," Academy of Management Review (14:4), 1989, pp. 496–515.

Bashein, B. J., Markus, M. L., and Riley, P. "Preconditions for BPR Success: And How to Prevent Failures," Information Systems Management (11:2), Spring 1994, pp. 7–13.

Bitauld, P., Burch, K., El-Taji, D., Fanucci, E., Montevecchi, M., Ohlsson, J., Palella, A., Rushmeier, R., and Snowdon, J. "Journey Management," OR/MS Today (24:5), October 1997, pp. 30–33.

Boehm, B. "A Spiral Model of Software Development and Enhancement," Computer (21:5), 1988, pp. 61–72.

Brown, J. S., Burton, R. R., and de Kleer, J. "Pedagogical, Natural Language and Knowledge Engineering Techniques in SOPHIE I, II and III," in Intelligent Tutoring Systems, D. Sleeman and J.S. Brown (eds.), Academic Press, London, UK, 1982.

Burlton, R. National Business Process Reengineering Conference Proceedings, Washington, DC, 1996.

Caron, J. R., Jarvenpaa, S. L., and Stoddard, D. B. "Business Reengineering at CIGNA Corporation: Experiences and Lessons Learned from the First Five Years," MIS Quarterly (18:3), September 1994, pp. 233–250.

Clemons, E. K., Thatcher, M. E., and Row, M. C. "Identifying Sources of Reengineering Failures: A Study of the Behavioral Factors Contributing to Reengineering Risks," Journal of Management Information Systems (12:2), 1995, pp. 9–36.

Curtis, B., Kellner, M. I., and Over, J. "Process Modeling," Communications of the ACM (35:9), September 1992, pp. 75–90.

Cypress, H.L. “Reengineering—MS/OR Imperative: Make Second Generation of Business Process Improvement Mode Work,” OR/MS Today (21:1), 1994, pp. 18–29.

D'Aveni, R.A. Hypercompetition: Managing the Dynamics of Strategic Maneuvering, Free Press, New York, NY, 1994.

Davenport, T. H. Process Innovation: Reengineering Work through Information

Technology, Harvard Press, Boston, MA, 1993.

Davenport, T. H. "Business Process Reengineering: Where It's Been, Where It's Going," in Business Process Change: Reengineering Concepts, Methods and Technologies, V. Grover and W. Kettinger (eds.), Idea Publishing, Middletown, PA, 1995, pp. 1–13.

Davenport, T. H., and Short, J.E. "The New Industrial Engineering: Information Technology and Business Process Redesign," Sloan Management Review (31:4), summer 1990, pp. 11–27.

Davenport, T. H., and Stoddard, D. B. "Reengineering: Business Change of Mythic Proportions?" MIS Quarterly (18:2), 1994, pp. 121–127.

Drucker, P. "The Coming of the New Organization," Harvard Business Review (66:1), January–February 1988, pp. 45–53.

Flood, R. L. Beyond TQM, Wiley, New York, NY, 1993.

Forbes, Special Focus on Intellectual Capital, Forbes ASAP, April 7, 1997.

Georgakopoulos, D., Hornick, M., and Sheth, A. "An Overview of Workflow Management: From Process Modeling to Workflow Automation Infrastructure," Distributed and Parallel Databases (3:2), 1995, pp. 119–153.

Goldstein, D. K. "Hallmark Cards," Harvard Business School Case No. 9-186-044, July 1986.

Grover, V., Jeong, S. R., Kettinger, W. J., and Teng, J. T. C. "The Implementation of Business Process Reengineering," Journal of Management Information Systems (12:1), 1995, pp. 109–144.

Guha, S., Kettinger, W. J., and Teng, J. T. C. "Business Process Reengineering: Building a Comprehensive Methodology," Information Systems Management (10:3), Summer 1993, pp. 13–22.

Hammer, M. "Reengineering Work: Don't Automate, Obliterate" Harvard Business Review (68:4), July–August 1990, pp. 104–112.

Hammer, M., and Champy J. Reengineering the Corporation: A Manifesto for Business Revolution, Harper Business Press, New York, NY, 1993.

Hammer, M., and Stanton S. The Reengineering Revolution: A Handbook, Harper Business Press, New York, NY, 1995.

Hamscher, W. "AI in Business Process Reengineering: A Report on the 1994 Workshop," AI Magazine (15:4), Winter 1994, pp. 71–72.

Harari, O. "Why Did Reengineering Die?" Management Review (85:6), June 1996, pp. 49–52.

Harrington, H.J. Business Process Improvement: the Breakthrough Strategy for Total Quality, Productivity, and Competitiveness, McGraw-Hill, New York, NY, 1991.

Hoffherr, G. D., Moran, J. D., and Nadler, G. Breakthrough Thinking in Total Quality Management, Prentice-Hall, Englewood Cliffs, NJ, 1994.

Jackson, P. Introduction to Expert Systems (2nd ed.), Addison-Wesley, Wokingham, UK, 1990.

Johansson, H. J., McHugh, P., Pendlebury, A. J., and Wheeler, W. A. III, Business Process Reengineering: Breakpoint Strategies for Market Dominance, Wiley, Chickster, UK, 1993.

Kettinger, W. J., Guha, S., and Teng, J. T. C. "The Process Reengineering Life Cycle Methodology: A Case Study," in Business Process Change: Reengineering Concepts, Methods and Technologies, V. Grover and W. Kettinger (eds.), Idea Publishing, Middletown, PA, 1995, pp. 211–244.

King, J. L., and Konsynski, B. "Singapore Tradenet: A Tale of One City," Harvard Business School Case No. 9-191-009, 1990.

Kling, R., and Scacchi, W. "The Web of Computing: Computer Technology as Social Organization," in Advances in Computers (21), M. Yovits (ed.), Academic Press, New York, NY, 1982, pp. 3–85.

Krantz, D. H., Luce, R. D. Suppes, P., and Tversky, A. Foundations of Measurement, Volume I: Additive and Polynomial Representations, Academic Press, New York, NY, 1971.

Law, A. M., and Kelton, W. D. Simulation Modeling and Analysis, McGraw-Hill, New York, NY, 1982.

Mi, P. Modeling and Analyzing the Software Process and Breakdowns, unpublished doctoral dissertation, University of Southern California, 1992.

Mi, P., and Scacchi, W. "A Knowledge-Based Environment for Modeling and Simulating Software Engineering Processes," IEEE Transactions on Knowledge and Data Engineering (2:3), 1990, 283–294.

Mi, P., and Scacchi, W. "Modeling, Integrating, and Enacting Complex Organizational Processes," Proceedings of the Fifth International Symposium on Intelligent Systems in Finance, Accounting and Management, Volume 1, Stanford University, December 1993.

Mi, P., and Scacchi, W. "Modeling and Simulation of the Accounts Payable Process," University of Southern California ATRIUM Lab Technical Report, 1994.

Mi, P., and Scacchi, W. "A Meta-Model for Formulating Knowledge-Based Models of Software Development," Decision Support Systems (17:4), 1995, pp. 313–330.

Nissen, M. E. Knowledge-Based Organizational Process Redesign: Using Process Flow Measures to Transform Procurement, doctoral dissertation, University of Southern California, 1996.

Nissen, M. E. "Reengineering Support through Measurement-Driven Inference," International Journal of Intelligent Systems in Accounting, Finance and Management (6:2) 1997, pp. 109–120.

Project Reviews. Series of formal and informal reviews with procurement managers, experts and knowledge workers, China Lake, CA and Los Angeles, CA, 1995.

Rich, E., and Knight, K. Artificial Intelligence (2nd ed.), McGraw-Hill, New York, NY, 1991.

Roberts, F. S. Measurement Theory: with Applications to Decisionmaking, Utility, and the Social Sciences, Addison-Wesley, Reading, MA, 1979.

Saharia, A. N., Barron, T. M., Davenport, T. J., Ho, J. K., and Mendelson, H. "Is There a Theory of Reengineering?" in Proceedings of the Fifteenth International Conference on Information Systems, J. DeGross, S. Huff and M. Munro (eds.), Vancouver, Canada, 1994.

Shortliffe, E.H. Computer-Based Medical Consultations: MYCIN, Elsevier, New York, NY, 1976.

Stoddard, D. B., and Jarvenpaa, S. L. "Business Process Redesign: Tactics for Managing Radical Change," Journal of Information Management Systems (12:1), 1995, pp. 81–107.

Stoddard, D. B., and Meadows, C. J. "Capital Holding Corporation—Reengineering the Direct Response Group," Harvard Business School Case No. 9-192-001, 1992.

Talebzadeh, H., Mandutianu, S., and Winner, C. F. "Countrywide Loan-Underwriting Expert System," Al Magazine (16:1), 1995, pp. 51–64.

van Mael, J. W. The Dynamics of Business Engineering: Reflections on two Case Studies within the Amsterdam Municipal Police Force, unpublished doctoral dissertation, Delft University of Technology, 1993.

van Mael, J. W., Bots, P. W. G., and Sol, H. G. "Lessons Learned from Business Engineering with the Amsterdam Police Force—Dynamic Modeling," in Business Process Change: Reengineering Concepts, Methods and Technologies, V. Grover and W. Kettinger (eds.), Idea Publishing, Middletown, PA, 1995, pp. 402–424.

Venkatraman, N. "IT-Enabled Business Transformation: From Automation to Business Scope Redefinition," Sloan Management Review (35:2), Winter 1994, pp. 73–87.

Yin, R.K. Case Study Research: Design and Methods (2nd ed.), 1994, Thousand Oaks, CA.

## About the Author

Mark E. Nissen is assistant professor of information systems and acquisition management at the Naval Postgraduate School. His research focuses on the application of knowledge systems to change-management problems in areas such as process innovation, electronic commerce, and knowledge management. Recently he has been specializing in the development of knowledge-based systems to innovate processes in the domain of defense acquisition and is currently working on intelligent acquisition agents. Before earning his Ph.D. in information systems, he acquired over a dozen years' management experience in the aerospace industry and served as a supply officer in the Naval Reserve.

## Appendix A

## KOPeR Architecture

In this appendix, a high-level overview of the KOPeR architecture is provided. KOPeR builds heavily upon a KBS called the Articulator, which is discussed first to provide necessary background to the KOPeR overview.

## Articulator Architecture

The Articulator is an implemented KBS that automatically diagnoses generic process breakdowns and generates strategies for their repair (Mi 1992). It employs the ontology developed through the Web of

Computing Model (Kling and Scacchi 1982) for process representation and analyzes a modeled process structure (i.e., configuration) to support automated reasoning about breakdowns and repairs (Mi and Scacchi 1993). KOPeR follows development of the Articulator through its taxonomic approach to knowledge representation and rule-based problem-solving method. The Articulator also provides the KBS architecture from which KOPeR is designed.

![](/api/attachments/E8DM53UW/fulltext/images/9d0a7b1aad3055ea9ecae892a4984d0249a8a1ea0d21630ecd95e852d5ec89d4.jpg)  
Figure A1. Articulator Architecture (Adapted from Mi 1992 and Scacchi 1995)

The high-level Articulator architecture is diagrammed in Figure A1 to show the orientation of four modules that are relevant to our purposes: (1) process models, (2) inference engine, (3) rules/taxonomies, and (4) utilities. The first module contains a repository of computer-based models used to represent the various processes to be analyzed (e.g., from the domains of software engineering, finance, and accounting). These are predicated on the process ontology from above and they supply the information or "facts" pertaining to a process structure that are used to support automated reasoning. The inference engine performs several methods of reasoning (e.g., forward and backward chaining), which are driven by rules for both the general diagnosis (i.e., classification) of process breakdowns and the general repair (i.e., matching articulation strategies) of processes. A number of bridge interfaces (e.g., to support graphical process modeling), LISP functions (e.g., graph-based counting routines), and utility rules (e.g., semantic process verification) are included in the Articulator. The entire system operates within a "KC" environment (labeled for the KnowledgeCraft product used for its development). The interested reader can consult Mi (1992) and Mi and Scacchi (1995) for the many details.

Inference in the Articulator is supported by the integration of two primary elements of knowledge: (1) taxonomies of process breakdowns and repairs and (2) production rules for matching classes of breakdowns with general repair strategies. The two knowledge taxonomies—one for process breakdowns, another for repairs—are each organized into class-subclass hierarchies. The idea of the first taxonomy is to organize (into a hierarchical class structure) most of the known manners in which processes can break down and to use this hierarchy to support automatic classification of breakdown instances that occur. Similarly, the second taxonomy provides a hierarchical structure that organizes most of the known repair strategies useful for correcting process breakdowns. The knowledge required to identify and organize these “known” breakdowns and repairs derives from the literature review and analysis accomplished in this prior work. The production rules formalize knowledge about the relationships between breakdowns and repairs and are integrated with the taxonomic knowledge to perform class-level or heuristic problem solving (see Jackson 1990). The integration of twin taxonomies with rules supports automated reasoning about a wide variety of process breakdowns (Mi 1992 provides clear examples).

## KOPeR Architecture

KOPeR is a proof-of-concept KBS designed to perform measurement-driven inference. Building on the Articulator implementation, the KOPeR design integrates one taxonomy of process pathologies with another taxonomy of redesign transformations. Both taxonomies are organized into classes and subclasses of problems/transformations to support classification and matching. Like the Articulator and other KBS exemplars discussed above, inference in KOPeR is predicated on production rules. Such rules are used in conjunction with knowledge taxonomies and diagnostic measures developed in this article. Specifically, rules are used to interpret empirical measurements, diagnose process pathologies, and match such diagnoses with appropriate redesign transformations. The high-level KOPeR architecture is presented in Figure A2. Based on the Articulator foundation, the initial implementation runs on a UNIX workstation and is accessible across an open network. As such, process models can be developed and analyzed remotely, from any personal computer or workstation with network access and compatibility. KOPeR is being reimplemented in G2 and extended to provide a web interface for process redesign.

![](/api/attachments/E8DM53UW/fulltext/images/30e3ab7d695ca65dfb134c3acb994f9f0d4bd3452eafcc77342824688fa5051a.jpg)  
Figure A2. KOPeR Architecture

The reader can readily observe the same four Articulator modules from above—process models, inference engine, rules/taxonomies, and utilities—in Figure A2. The KBS extensions effected through KOPeR are emphasized by italic print in the figure and separated by dotted lines. For example, to the existing set of process models (i.e., software, finance, accounting), the present research adds a set developed from the procurement domain. The J&A process examined in this study represents one instance from this procurement set. To the Articulator's twin taxonomies and rules for general process articulation, KOPeR adds taxonomies of process pathologies and redesign transformations that are specific to the reengineering domain, as well as production rules for classification and matching, extracted from the reengineering literature. This combination of taxonomic and rule-based knowledge is brought to bear on problem solving through two new utilities, one for diagnostic measurement and another for matching (i.e., recommending) redesign transformations. This present KOPeR work does not address the Articulator's existing utilities or inference engine at all, although it takes great advantage of this KBS infrastructure.

A new box is also included in Figure A2 to depict the relationship of commercial simulation software (WITNESS in this case) used to support KOPeR and measurement-driven inference. The interface is shown between the simulation package and the process models in the diagram. With this initial implementation, however, the interface is completely manual; that is, the capability to automatically generate simulation models from KOPeR/Articulator does not exist in the initial proof-of-concept KBS. This represents one limitation of the initial implementation and a reason for selecting reimplementation in G2 (i.e., the seamless integration of its KBS development environment with a simulation engine). The interested reader can drill-down through the references for detailed information pertaining to the Articulator (see especially Mi 1992; Mi and Scacchi 1993; 1995) and KOPeR (see especially Nissen 1996, 1997).

## Appendix B

## Field Study Details

This appendix details the “industrial strength” example of KOPeR employed to redesign the operational procurement processes of a major military command. The two sections that follow provide additional detail and discussion pertaining to the redesign activities performed through the field study. The J&A process redesign analysis is first described in greater depth and then the key redesign results are further elaborated.

## J&A Process Redesign

The J&A process is involved with all sole-source or “other than full and open competition” procurements in the government, and is expressly required by regulation. Although not a large process, it is quite complex and has been identified by senior procurement officials as particularly important and dysfunctional. Recall that factors such as importance and dysfunction are noted as useful heuristics for identifying processes to be redesigned. A level-1 baseline process model for J&A is presented in Figure B1.

![](/api/attachments/E8DM53UW/fulltext/images/17e57345b80e03b694815a6b35e7ba8b7c9e1cf5ece43f9072ad8f51862f37bb.jpg)  
Figure B1. J&A Level-1 Baseline Process Model

At this top level, the process is comprised of five tasks: (1) customer assistance, (2) J&A documentation, (3) contract specialist (CS) assignment, (4) approvals, and (5) J&A filing. Notice the process is entirely sequential, with each activity following a single predecessor in linear fashion. A feedback or quality loop is used to represent rework that results from disapproval of a J&A documentation package. Several familiar process attributes (e.g., agent, organization, IT tools) and values are listed below the "J&A doc" task in the figure, for instance. These attributes correspond to those discussed in the context of the credit financing case. The figure also includes some KOPeR extensions (e.g., inputs, outputs, communication) to the set discussed above. In this representation, the circle icons represent atomic tasks that are not decomposable, and the square icons represent decomposable workflows that are comprised of lower-level subprocesses. Both the customer assistance and the approvals tasks are comprised of lower-level workflows in this manner. In fact, the approvals workflow has two hierarchical levels beneath it (for a total process depth of three levels; not shown).

![](/api/attachments/E8DM53UW/fulltext/images/94f9a2b30bbb891d616acbe2acc997fa5ae2044ace8c261ace64c955eed561c4.jpg)  
Figure B2. J&A Level-2 Baseline Process Model—Approvals

Figure B2 depicts the level-2 baseline process model comprising the approvals workflow. Here the figure represents an annotated “screendump” from the Articulator. The Articulator is used by KOPeR as a platform for graphical process model representation. As can be seen from the level-2 approvals diagram, the workflow consists of four sequential J&A reviews. Briefly, the J&A documentation is first reviewed by an agent from the Legal Department, who may or may not approve it. If approved, the J&A package proceeds to the next review, whereas in the latter case it is returned for rework. After Legal approval, the J&A package is reviewed by the Contracting Officer (KO), who similarly may either approve it or remand it for rework, and so forth for competition advocates from the requiring activity (RACA) and procurement activity (PACA). The study noted that the review by one agent (e.g., the KO) is not dependent upon the results of the preceding review (e.g., Legal). A conditional branch in the workflow demarcates an additional process step required to obtain senior management approval of J&As above a certain dollar threshold.

Some of the more illustrative configuration measurements are summarized in Table B1 for the J&A process, along with the corresponding diagnoses. Note the "small" size does not represent a pathology per se. The process size (31), organizational roles (7), and parallelism (1.00) measurements are computed in the same manner described for the credit financing example, as are the familiar length (31), breadth (1), depth (3), and other parameters (not shown). The roles measurement (7) receives the same interpretation (i.e., narrowly defined job scope) as in the credit financing case. Alternatively, the three IT "fractions" differ somewhat from the corresponding IT "counts" analyzed in the credit financing case. Specifically, these fractional measurements are calculated by dividing process-size (31) into the counts for IT-based support (1), communication (0) and automation (0), respectively. Such scaling (e.g., dividing IT counts by process size) improves interprocess comparability and makes the measurement-driven method more robust to differences in process size. For instance, the same KOPeR rules that are used for diagnosing the J&A process (i.e., with size of 31) apply equally well to the Large Contracted Procurement (LCP; i.e., with over 800 modeled process tasks). Note the values for parallelism and these measured IT fractions are at or near their theoretical minima (extrema are denoted by asterisks in the table). This indicates the baseline J&A process configuration is not only sequential, but highly manual, paper-based, and labor-intensive as well. Likewise, the feedback fraction (0.35) highlights the review-intensive nature of the process, and the handoff fraction (0.58) similarly underscores the substantial process friction.

Table B1. J&A Configuration Measurements and Diagnoses

<table><tr><td>Configuration Measure</td><td>Value</td><td>Diagnosis</td></tr><tr><td>Process Size</td><td>31</td><td>Small process</td></tr><tr><td>Organizational roles</td><td>7</td><td>Job specialization</td></tr><tr><td>Parallelism</td><td>1.00*</td><td>Sequential process flows</td></tr><tr><td>IT-Support fraction</td><td>0.03</td><td>Manual process</td></tr><tr><td>IT-Communication fraction</td><td>0.00*</td><td>Paper-based process</td></tr><tr><td>IT-Automation fraction</td><td>0.00*</td><td>Labor-intensive process</td></tr><tr><td>Feedback fraction</td><td>0.35</td><td>Review-intensive process</td></tr><tr><td>Handoffs fraction</td><td>0.58</td><td>Process friction</td></tr></table>

\* Denotes theoretical extremum for a measure.

The eight KOPeR-recommended redesign alternatives are summarized again in Table B2 for reference, along with the matching pathologies. Notice several of these pathology-transformation combinations correspond to similar measurement-driven inference discussed in the context of credit financing. For example, the pathology “sequential process flows” is matched with the delinearize redesign transformation. Notice in the present instance that the delinearization transformation is targeted explicitly toward the approvals workflow. This targeting results from the high feedback-fraction measurement, which helps KOPeR to focus on the approvals portion of the process.

The delinearization transformation is used in turn to generate two similar but distinct redesign alternatives: (1) concurrent reviews and (2) joint reviews. The first alternative involves asynchronous reviews conducted in parallel as opposed to serially (e.g., each reviewer receives an identical J&A documentation package from the CS), whereas the second alternative requires contemporaneous (i.e., joint) meetings by the participants to review the J&A documentation. Likewise, low IT support for a frictional, document-based process drives the same shared database transformation implemented in the credit financing example, this time in conjunction with electronic mail. The corresponding redesign alternative (number 3) is labeled "e-document infrastructure" to denote the non-paper-based nature of the proposed process change. The fourth redesign alternative, "contracts workflow system," is generated from a similar but more sophisticated transformation to automate "routine workflows" (see Georgakopoulos et al. 1995) associated with contracts work. This latter KOPeR recommendation is driven by the same pathologies noted above, with the addition of "labor-intensive process" (i.e., negligible IT automation).

Continuing down the table entries, the same case manager transformation (i.e., from the credit financing example) is found to be matched consistently with the job specialization and process friction pathologies. This redesign transformation is used to generate a "J&A case team" redesign, which envisions an integrated team (e.g., including the CS, KO, RACA, PACA, and Legal representative) working together through the entire J&A process. The job specialization pathology also matches with three empowerment transformations—two oriented toward expanding CS responsibilities and one that includes enlarging the KO job scope. Basically, these eight redesign alternatives result from the same application of diagnostic measures, knowledge taxonomies, and rule-based inference that are described in terms of the credit financing example, except they are applied here in the field to an operational J&A process from the military procurement domain. The redesign results are now further elaborated.

Table B2. Redesign Alternatives

<table><tr><td>Diagnosed Pathology</td><td>Recommended Transformation</td><td>Redesign Alternative</td></tr><tr><td>Sequential process flows + review-intensive process</td><td>Delinearize (approvals)</td><td>1. Concurrent reviews</td></tr><tr><td>Sequential process flows + review-intensive process</td><td>Delinearize (approvals)</td><td>2. Joint reviews</td></tr><tr><td>Manual process + paper-based process + process friction</td><td>Shared database + e-mail</td><td>3. E-document infrastructure</td></tr><tr><td>Manual process + paper-based process + process friction + labor-intensive process</td><td>Workflow management system</td><td>4. Contracts workflow system</td></tr><tr><td>Job specialization + process friction</td><td>Case manager</td><td>5. J&amp;A case team</td></tr><tr><td>Job specialization</td><td>Empowerment (3)</td><td>6-8. CS and KO job enlargement</td></tr></table>

Bold denotes "preferred" redesign alternative.

## J&A Redesign Results

It was noted that simulation is used to assess the relative performance of redesign alternatives. To help reduce the number of simulation models required for this field study, the support of process experts is enlisted to refine the set of redesign alternatives generated from KOPeR-recommended transformations. Combining their in-depth process knowledge with evaluation criteria such as process feasibility, implementability, and projected benefit, this team identifies a subset of the redesign alternatives from above as "preferred" (emphasized by bold print in Table B2). For example, the experts predict the joint reviews alternative (number 2) will produce greater benefit than its concurrent-reviews counterpart (number 1). They express a similar preference for the contracts workflow system (number 4) over its e-document counterpart (number 3). The experts also assess these first four redesign alternatives to be both feasible and implementable in the current organization.

In contrast, although the experts can foresee good potential for the case manager and empowerment alternatives (numbers 5 through 8), and they similarly view them as feasible transformations, their judgment is the required organizational changes are not implementable at the present time. This use of process experts to augment KBS reasoning represents a powerful combination of human and machine inference. As a result of the expert analysis, only the two preferred redesign alternatives (i.e., the subset selected by the experts) are simulated for the field investigation. This approach is actually recommended by the process managers as a way to expedite the analysis, and it may represent a prudent use of analytical resources in other reengineering engagements as well.

For this analysis, the simulated cost and cycle time of each redesign alternative are compared with those of the J&A process baseline. The baseline J&A simulation model is first validated using recent performance data (e.g., process cost, cycle time, throughput), reviewed by process experts and subjected to other validation techniques. For example, construction of the simulation model itself is homomorphic (see Roberts 1979) to the baseline KOPeR process model; that is, each of the same agents, tasks, and resources used to represent the baseline J&A process diagrammed above is also used in the dynamic simulation model.

A commercial software package (WITNESS) is employed to simulate the performance of the J&A baseline and each “preferred” redesign alternative. In this study, activity-based cost and cycle time are used to measure process performance. Other measures such as throughput, rework, agent-utilization, and the like are also informative, but cost and cycle time are the output measures of interest in this efficiency study. This is consistent with a similar emphasis on cost and cycle time found in the reengineering literature. To compare the relative performance of the redesign alternatives, each simulated process is run for the equivalent of one steady-state fiscal year; that is, the dynamic model is allowed to “warm up” and stabilize before simulated performance for the fiscal year is measured.

Simulation results for the J&A process are summarized again in Table B3 for reference. From the table entries, it can be seen that the joint-reviews transformation results in a 28% (simulated) cost improvement over the baseline, primarily due to a reduction in rework enabled by the joint-meeting format. More impressive, this redesign alternative results in a two-thirds reduction in cycle time for performance of the J&A process. The reduction in rework contributes in part to this result, but the decreased cycle time is driven primarily by concurrent review (i.e., parallel vs. sequential performance). The asterisks in the table are used to denote results that exceed the performance-doubling threshold established for the field study. This threshold is intended to differentiate between “dramatic” performance improvements (i.e., as sought through BPR) and “incremental” gains (i.e., reflecting more of a TQM approach).

Interestingly (and coincidentally), the contracts workflow system matches this two-thirds reduction in cycle time, but it produces negligible savings in terms of cost. The reduced friction associated with eliminating J&A paper handoffs (e.g., work sitting in in-boxes and out-boxes, awaiting assignment, pausing for review and approval, etc.) contributes toward this dramatic cycle-time improvement, as does the decreased transportation time between process activities. The absence of cost savings is attributable to the fact that the process tasks themselves remain fundamentally unchanged with the workflow system; that is, the J&A work itself remains the same, as only the interface and communication between activities are automated through the workflow management system. This effect has been colorfully referred to as “paving the cowpaths” in the reengineering literature (Hammer 1990).

It is also important to note these two redesign alternatives are generated independently; that is, KOPeR recommends each transformation be applied to redesign the J&A process individually, but it does not yet possess the inferential capability to recommend them in combination. Thus, a person can elect to combine these two (or any other) transformations and attempt to produce even more dramatic gains in performance. However, each such combination requires a separate simulation, for the individual results (especially cycle time) are unlikely to be additive.

Table B3. Redesign Simulation Results

<table><tr><td>Redesign Alternative</td><td>Cost Reduction</td><td>Cycle Time Reduction</td></tr><tr><td>Joint Reviews</td><td>28%</td><td>67%*</td></tr><tr><td>Contracts Workflow System</td><td>nil</td><td>67%*</td></tr></table>

\* Denotes performance doubling.
