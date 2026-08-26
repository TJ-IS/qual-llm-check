---
otero_id: 25316
otero_key: "SZ83RE4H"
title: "Integrating Collaborative Processes and Quality Assurance Techniques: Experiences from Requirements Negotiation"
authors: "PAUL GRÜNBACHER; MICHAEL HALLING; STEFAN BIFFL; BARRY W. BOEHM"
year: "2004"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2004.11045784"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Integrating Collaborative Processes and Quality Assurance Techniques: Experiences from Requirements Negotiation

PAUL GRÜNBACHER , MICHAEL HALLING , STEFAN BIFFL , STEFAN BIFFL & BARRY W. BOEHM

To cite this article: PAUL GRÜNBACHER , MICHAEL HALLING , STEFAN BIFFL , STEFAN BIFFL & BARRY W. BOEHM (2004) Integrating Collaborative Processes and Quality Assurance Techniques: Experiences from Requirements Negotiation, Journal of Management Information Systems, 20:4, 10-30

To link to this article: http://dx.doi.org/10.1080/07421222.2004.11045784

![](/api/attachments/SZ83RE4H/fulltext/images/b20df7d76b50d144169fc765159eaa9540dac3f33d4da007d972dd80980f2879.jpg)

Published online: 08 Dec 2014.

![](/api/attachments/SZ83RE4H/fulltext/images/6b85cd086daec99714d3a1f2b668aba76f7d06ac74933d1c469a8adb90cb8c98.jpg)

Submit your article to this journal

![](/api/attachments/SZ83RE4H/fulltext/images/a380c3489f229da52d1fe109337a0a0e13e40def97192f14596bc0bd7910bd5b.jpg)

Article views: 12

![](/api/attachments/SZ83RE4H/fulltext/images/1ab303322258cde48daf328e56a6cf42315c75181b0e4fe196ca79e1cc2e9836.jpg)

View related articles

# Integrating Collaborative Processes and Quality Assurance Techniques: Experiences from Requirements Negotiation

PAUL GRÜNBACHER, MICHAEL HALLING, STEFAN BIFFL, HASAN KITAPCI, AND BARRY W. BOEHM

PAUL GRÜNBACHER is an Associate Professor at Johannes Kepler University Linz (Austria) and a research associate of the Center for Software Engineering (University of Southern California, Los Angeles). His research interests include collaborative technology in software engineering, particularly in requirements engineering and methods for software process improvement. He received an M.S. and a Ph.D. in Business Informatics from the University of Linz.

MICHAEL HALLING is an Assistant Professor at the University of Vienna (Austria) and a research associate at the Johannes Kepler University of Linz (Austria). His research interests include software quality assurance techniques and decision theory in software engineering and project management. He holds an M.S. in Finance from the University of Vienna, an M.S. in Computer Science from the Vienna University of Technology, and a Ph.D. from the Vienna University of Technology.

STEFAN BIFFL is an Associate Professor of software engineering at the Vienna University of Technology. His research interests include project and quality management in software engineering. He received an M.S. and Ph.D. in computer science from the Vienna University of Technology and an M.S. in social and economic sciences from the University of Vienna. He is a member of the ACM and IEEE.

HASAN KITAPCI is a doctoral student at the University of Southern California’s Center for Software Engineering. His research interests include requirements elicitation and specification, formalizing requirements, and formal methods. He received an M.S. in Computer Science from USC.

BARRY W. BOEHM is the TRW Professor of Software Engineering and Director of the Center for Software Engineering at the University of Southern California. He was previously in technical and management positions at General Dynamics, Rand Corporation, TRW, and the Office of the Secretary of Defense as the director of Defense Research and Engineering Software and Computer Technology Office. Professor Boehm originated the spiral model, the Constructive Cost Model (COCOMO), and the stakeholder win-win approach to software management and requirements negotiation.

ABSTRACT: Collaboration is essential in many mission-critical activities. Consequently, numerous methods and tools are available supporting collaborative processes such as strategic planning, risk management, requirements definition, and so on. These methods typically emphasize the collaborative, value-creating activities, but there is often less emphasis on quality aspects. Quality assurance (QA) techniques have been wellknown in engineering for a long time, and their effectiveness and efficiency has been empirically evaluated in many domains. In this paper, we propose to integrate repeatable QA techniques and collaborative processes. We evaluate our idea in the context of a collaborative process for requirements negotiation. We propose pre-process techniques to be used before the actual negotiation, in-process techniques for checking quality during a negotiation, as well as post-process inspection techniques. These techniques help a project team reduce unnecessary complexity and to mitigate risks stemming from defects in requirements negotiation results. We present the results of a feasibility study we conducted to test our approach.

KEY WORDS AND PHRASES: collaboration engineering, group support systems, quality assurance techniques, requirements negotiation.

COLLABORATIVE PROCESSES ARE ESSENTIAL in many mission-critical activities and there are numerous methods and tools available for different collaborative processes such as strategic planning, risk management, requirements definition, and so on. The quality of the work products in these processes is of utmost importance. However, quality is often insufficient due to limited meeting time, unavailable stakeholders, cognitive overhead during meetings, and so on.

Collaboration engineering is an approach for the design and deployment of collaborative technologies and processes to support mission-critical tasks [8]. In this paper, we argue that quality assurance (QA) techniques should become essential building blocks in collaboration engineering and propose their stronger adoption and integration with collaborative processes.

In software and systems engineering, for example, getting the requirements right is crucial for project planning, architectural design, and, ultimately, to achieve customer satisfaction. Requirements acquired from the stakeholders represent the starting point for actual development and provide rationale for the stakeholder needs. The agreed requirements should therefore be as clear, correct, and complete as possible with respect to a defined negotiation purpose. Ensuring high-quality requirements is not a single-person effort, but always requires the participation and collaboration of numerous heterogeneous stakeholders with different roles. Designing repeatable QA techniques and using them in concert with proven collaborative processes becomes critical for requirements negotiation, as the identification and elimination of defects helps to mitigate risks and to avoid unnecessary complexity in systems engineering. In our previous work on collaborative processes for requirements negotiation [5], we have learned that rapid quality checks can be applied during a negotiation, but additional QA activities should be done before and after a collaborative process.

This paper introduces QA techniques and discusses how they can be used in concert with collaborative processes. We discuss pre-process, in-process, and post-process techniques and demonstrate them in the context of the EasyWinWin requirements negotiation process. We show how preparation activities, quality checks applied during the groupware-supported negotiation process, and inspections can be used to improve the negotiation results.

## Quality Assurance for Collaborative Processes

BOEHM [4] AND GLASS [13] REPORT that, in software development, up to 50 percent of all labor-hours are spent on detecting and correcting defects rather than on developing new software. QA techniques are thus necessary to assess work products and to reduce defects in mission-critical activities. In software engineering, the most widely applied QA techniques are testing and inspection. Testing is limited to executable software products and thus typically applied later in development where finding and correction of defects is much more expensive compared to earlier stages. Inspection, on the other hand, can be applied to all software development products as soon as they are available. In this paper, we will present inspections for post-process quality assurance.

Inspections are well established both in research and practice as one of the most effective and efficient defect reduction techniques [28]. Glass [13] states that inspections, by all accounts, find more defects than competing approaches and that the cost per found defect is lower. Further empirical studies have demonstrated the effectiveness and efficiency of inspections [17, 20, 24]. Inspections are also recognized as the most effective means of finding defects in documentation [4, 30]. Inspections address quality control as a method for detecting defects. They address QA by collecting statistics that may be used to determine the confidence level in the inspection object’s quality. Following Laitenberger et al. [25], we consider inspection as an approach involving a well-defined and disciplined process in which qualified personnel analyze a software product using a reading technique for the purpose of defect detection. This definition of an inspection is broader in scope than the definition originally provided by Fagan [10]. Note that this definition of software inspections is sometimes also referred to as formal technical review (FTR). Inspections require (1) that participants follow a defined process, (2) participants of inspections apply some defect detection technique and are trained to find defects, and (3) inspections yield defect data and data on the quality of the performed inspection [3].

Most organizations using inspections follow a three-step procedure of preparation (individual defect detection), defect collection, and defect repair [10, 12]. In software engineering, there has long been a focus on source code inspection complementing test efforts [10]. In the meantime, researchers found that inspecting documents, such as requirements specifications, increases the benefits of inspection due to earlier defect removal and saved rework. Empirical studies [2, 11, 17, 18, 20, 25] demonstrate the benefits of software inspections.

Applying quality techniques in concert with collaborative processes requires a detailed understanding of collaborative processes and the capabilities of quality techniques: constraints to make QA support collaboration, not disrupt it; these constraints usually limit who can conduct QA and the effort available for QA steps.

We propose that each collaborative process should be accompanied by a QA activity (see Figure 1). Collaborative processes typically have three phases: a preparation phase, a value-creation phase, and a finalization phase. For each activity in a collaborative process, we suggest a QA activity to make sure that the collaborative process is on track. In order to select an appropriate QA technique for each activity, it is important to understand the characteristics of each activity.

• In the preparation phase (P0), the facilitator of a collaborative process defines the purpose of the process, selects stakeholders, and conducts specific tailoring activities. The output of the phase is a plan for the workshop, including invitations to the stakeholders, and so on. For the preparation phase, we suggest a preprocess QA activity (QA0) to make sure that the fundamental assumptions hold, the process purpose is clearly defined, and the right set of stakeholders has been selected. It is especially important to perform this quality check in order to ensure that the collaborative activity can yield the desired result. As collaborative processes are usually especially expensive due to the participation of different stakeholders, it is important to ensure appropriate quality of all input material. As the responsible person in this phase is usually an experienced facilitator, it is sufficient to support the organizer with a checklist containing all necessary steps and typical defects that may occur. Going through the list, the organizer can gather issues or potential risks to the current process and plan how to mitigate these risks. In the end, the organizer has to decide whether the preparations are sound enough to proceed with the workshop.

• The preparation phase is followed by a value-creation phase (P1), where stakeholders create the work products defined by the collaborative process, such as a moderated workshop, based on the plans from P0. For the value-creation phase, we suggest joint in-process quality checks during the collaborative process. The value-creation phase usually is a highly dynamic and interactive process. Therefore little time is available for careful QA checks. During this process phase, it is especially important that the quality checks do not constrain the collaborative activities in any case. Therefore we propose to use joint informal and rapid checks by giving the stakeholders feedback in the value-creation process to ensure the desired quality level. In the workshop, only the authors and facilitator are available, further time is usually too short for comprehensive extra work. Thus a full inspection is often not feasible. In many cases, the moderator can extend the converge steps [8] of the collaborative process with extra checking activities, for example, cross-checks to ensure consistency among several work products. This allows the facilitator to train stakeholders in what to look for and motivates them to raise and address issues immediately or to mark them for later resolution.

• Finally, there is a finalization phase (P2) to produce reports, document lessonslearned, and so on. For this phase, we suggest systematic and detailed postprocess QA activities. As the results of the collaborative activity are stable in this phase, it is possible to conduct a full inspection, in which inspectors may take several roles to scrutinize the final deliverables with reading techniques, for example, perspective-based reading from the viewpoint of a project manager or software engineer. Another important dimension of post-process QA is to not only analyze the quality of the output documents but also the quality of the collaborative process. Post-process QA can generate important input for further improvements to the collaborative processes based on the issues and defects found during the three QA activities.

![](/api/attachments/SZ83RE4H/fulltext/images/00e0e608dbc60711ccffbfebb4d0f5ebbfff66a37ec6f743385a65191d291cd1.jpg)  
<sub>Process</sub> <sub>Track</sub> <sub>and</sub> <sub>Q</sub>A <sup>Track</sup> <sup>(in</sup> <sup>IDEF0</sup>

## Quality Issues in Requirements Negotiation

WE WILL EMPHASIZE THE NEED FOR QUALITY TECHNIQUES by discussing quality issues we observed in facilitating collaborative processes for requirements negotiations with EasyWinWin [5, 9, 16]. Applying quality techniques to requirements is important as it has been shown in many studies that defects and failures in the requirements have severe negative effects on project success [32]. A requirement is “a condition or capability needed by a user to solve a problem or achieve an objective” [22]. In contrast to detailed requirements described in a requirements document, prerequirements are tangible artifacts produced and exchanged in requirements production [14]. Numerous techniques are available for capturing and modeling prerequirements. Examples are the IBIS (Issue-Based Information System) [23], DRL (Decision Representation Language) [26], Toulmin’s model of argumentation [33], QOC (question, option, and criteria) [27], the Potts and Burns model [29], and the WinWin negotiation model [6] that is adopted in EasyWinWin.

EasyWinWin helps success-critical stakeholders to jointly discover, elaborate, and negotiate their requirements [5]. It adopts the WinWin negotiation model [6] and captures requirements of success-critical stakeholders as win conditions, issues, options, and agreements. Important negotiation results are negotiation topics organized in a taxonomy, the glossary of project-specific terms, and the WinWin tree, which organizes win conditions, issues, options, and agreements in a hierarchy (see shaded rectangles in Figure 2). These results are used in a project to develop crucial deliverables, such as a project plan, requirements specifications, or contracts to name but a few. EasyWinWin uses a group support system (GSS) and is based on stakeholder involvement and interaction to elicit their preferences. The GSS tools enable structured communication among the negotiation participants, help to elicit often tacit values and knowledge, and create a common vision among the stakeholders [16].

An EasyWinWin negotiation is typically carried out in a series of co-located or dispersed sessions involving the identified success-critical stakeholders. A facilitator moderates the negotiation process following detailed guidelines [15]. The use of a technographer in charge of handling the groupware tools has proven to increase efficiency. One inherent trade-off in a real-world negotiation situation is precision for speed: a major challenge for the facilitator is therefore to watch the trade-off between generating many ideas and delivering consistent high-quality negotiation results. It is also important to keep the participants focused on the right level of detail according to the negotiation purpose in order to elicit as complete and consistent information as possible in a given negotiation situation. Our lessons learned during real-world negotiations show that it is not effective to dampen the enthusiasm of stakeholders and the creative flow of ideas during a meeting with techniques that emphasize detailed wordsmithing, correctness, consistency, and so on [5]. Although the outcome of a WinWin negotiation is typically not a complete, consistent, traceable, and testable requirements specification, it comprises jointly developed and agreed prerequirements, potential risks and constraints, and important project-specific terms.

![](/api/attachments/SZ83RE4H/fulltext/images/4adcae2c3733252672fca1129f8a437551d2cf62488dca6c946e2556f5284d85.jpg)  
Figure 2. EasyWinWin Activities and Work Products with Relationships to Important Work Products in the Life Cycle.

## The EasyWinWin Negotiation Process

The activities of the EasyWinWin process are summarized in Figure 2 (for a detailed description, please refer to [5, 7, 15, 16]). The results of each activity in the process is a well-defined deliverable: (1) negotiation topics organized in a domain taxonomy, (2) a glossary defining key project terms, (3) agreements providing the foundation for further plans, (4) open issues addressing constraints, conflicts, and known problems, and (5) further rationale showing the negotiation history (comments, win conditions, issues, options, etc.).

Major results of the negotiation process are a list of agreements and a list of unresolved issues (e.g., caused by stakeholder dissent) that have to be managed as potential projects risks. Agreements of success-critical stakeholders are input to the project contract and to refinement during requirements engineering activities. The WinWin tree shows how agreements and open issues can be traced back to stakeholder win conditions.

## Typical Defects

Defects in a requirements negotiation can be found in individual statements or on the negotiation level. Typical faults we experienced are vague or ambiguous statements, missing information, wrong level of detail, or inconsistencies. All defects have to be interpreted with respect to the defined negotiation purpose, which states the context and the desired level of detail.

Statement-Level Defects. Negotiation artifacts are statements written in natural language and therefore error-prone. Table 1 shows some examples of defects that we identified in individual statements.

Negotiation-Level Defects. A challenge of the EasyWinWin process lies in understanding a large number of interrelated artifacts and their relation to the overall negotiation purpose. The quality criteria completeness and consistency relate the negotiation results to a set of expectations (what should be in the negotiation results) and span multiple statements. An example of a severe defect is the incomplete coverage of the negotiation purpose statement or the agreed negotiation topics (see Table 2).

## Quality Assurance Techniques for EasyWinWin

AN EASYWINWIN NEGOTIATION RESULTS in a significantly higher number of artifacts compared to traditional paper- or blackboard-based approaches: Our experience shows that typical negotiations about system requirements with 10+ stakeholders result in 300+ brainstorming ideas, 100+ win conditions, 50+ issues, 50+ options, and 100+ agreements. Due to this size and complexity, systematic QA techniques become even more important because defects in the prerequirements might ultimately cause even more defects in the final product. Although the impact of a defect in the prerequirements is typically rather minor and local initially, it can become more serious in later phases, since more rework is necessary and more people are involved to fix the defects. For example, an ill-defined capability defect that can be easily fixed during requirements negotiation could become a major problem if it cannot be realized with the chosen system architecture. Consequently, before refining the negotiation results to other life-cycle artifacts, such as contracts, specification, project plans, or architectural models, defects should be eliminated to reduce both the effort and probability of rework stemming from undetected defects.

Table 1. Statement-Level Defects (Examples).

<table><tr><td>Statement</td><td>Defect Type</td><td>Defect Description</td></tr><tr><td>Win condition: List search results in alphabetical order.</td><td>Unclear term/statement or missing information.</td><td>Unclear by which fields search results should be sorted.</td></tr><tr><td>Glossary definition: ISBN is the abbreviation of International Standard Book Number. Every journal has a unique ISBN.</td><td>Incorrect statement.</td><td>Journals have an ISSN (unlike books).</td></tr><tr><td>Win condition: User interface should be simple and straightforward.</td><td>Unverifiable statement.</td><td>This statement is not measurable and testable.</td></tr><tr><td>Win condition: The administrator is responsible for changing data formats.</td><td>Ambiguous term.</td><td>The term administrator is ambiguous, as different types of administrators exist in this context (e.g., system administration, database administration).</td></tr></table>

Table 2. Negotiation-Level Defects (Examples).

<table><tr><td>Statement</td><td>Defect Type</td><td>Defect Description</td></tr><tr><td>Win condition: Non-full text journals&#x27; information will not be in the journal title searchable database (categorized as a system capability).</td><td>Incorrect relationship of statement to topic.</td><td>This is not a system capability, but a goal describing the intended use of the system.</td></tr><tr><td>Win condition: Use tool X to build the [..] database.</td><td>Inconsistency.</td><td>Conflict with overall project constraint that tool Y should be used.</td></tr></table>

According to the quality strategy outlined in the second section, we have developed QA techniques for EasyWinWin that can be applied before negotiations (see the “Pre-Process Quality Assurance” subsection), during negotiations (see the “In-Process Quality Assurance” subsection), and after negotiations (see the “Post-Process Quality Assurance” subsection).

Figure 3 shows the three phases of QA that accompany the EasyWinWin process. I. Pre-process QA follows the steps in the “Pre-Process Quality Assurance” subsection (see the work products project context, mission statement, and stakeholders, as well as system environment and interfaces). QA uses a checklist and conducts risk analysis to decide whether the preparation of the workshop is good enough to proceed. This is typically not an inspection, as the QA person is the same person who does the preparation work, but, if desired, an inspection would be possible (and considerably more costly) to conduct with separate QA personnel.

![](/api/attachments/SZ83RE4H/fulltext/images/37ba105869917b733f414dd3f8c38e92d0f523a540e252fffee1c6d58c44d675.jpg)  
Figure 3. QA Processes and Work Products Before, During, and After the Collaborative Activity.

II. In-process QA follows the steps in the “In-Process Quality Assurance” subsection: in Figure 3 there is a tag with the number of the respective checking step near work products that get checked. The setting is a facilitated workshop, and QA is conducted by the authors and also guided by the moderator. The issue is to provide a big picture to participants without interrupting the workshop. Thus, a full inspection process cannot be conducted during the workshop. Instead, the authors apply plausibility checks, which, nevertheless, often detect inconsistencies and errors from previous steps.

III. Post-process QA follows the steps in the “Post-Process Quality Assurance” subsection. QA is here an in-depth inspection with cross-checks on the documents that result from the EasyWinWin process: project context, project glossary, agreements, and open risks. The inspection employs reading techniques for project managers and technical reviewers.

Please note that pre-process QA and in-process QA activities are described in more detail in the EasyWinWin Moderator’s Guidebook [15].

## Pre-Process Quality Assurance

The facilitator has the responsibility to check that the preconditions of a negotiation are satisfied. It is crucial to develop a statement summarizing the major purpose of the negotiation, context information, and major objectives of the system to be developed.

The second central issue is to make sure that all success-critical stakeholders are identified. A success-critical stakeholder is any individual whose interests must be accommodated in order for the project to succeed [31]. Success-critical stakeholders are people who can make agreements about the requirements, and make those agreements stick. Typical categories of stakeholders that should be considered successcritical are people designing and developing a system, people interested in system use (e.g., end users or customers), people having a financial interest, or people responsible for system introduction and maintenance.

There are some additional criteria for selecting stakeholders: They should be empowered and have the official authority or legal power to negotiate agreements. Stakeholders should be committed to the decisions that are jointly developed. Stakeholders should be representative when serving as a delegate or agent for a team or organization. They should be collaborative and have the willingness and perceptiveness required for developing mutually satisfactory solutions in a team process. Stakeholders should also be knowledgeable and well informed about the negotiation domain.

## In-Process Quality Assurance

EasyWinWin uses two types of collaborative activities. During “diverging” activities, the primary goal of the process is to produce new content. During “converging” activities, the results are consolidated and also checked for defects [9]. This separation avoids confusion from switching the context between production and consolidation/ analysis processes.

For local defects on the statement level (see the “Typical Defects” subsection), a simple form of alleviating the effects of imperfect products is to check each individual statement. Beyond such simple checks, we have developed joint rapid checking activities to be performed by a team to spot and resolve defects during a negotiation. At certain points in the process, all participants step back from the negotiation and check the quality of the products developed so far to eliminate local defects that have been identified. Fixing defects in the process is typically straightforward, as it is possible to clarify issues with the author. The process is not an inspection, as the participants (and authors) themselves review the products. The list of checking activities is in Table 3 and explained in detail below.

Table 3. In-Process Checking Activities in EasyWinWin.

<table><tr><td>Activity</td><td>Checking focus</td></tr><tr><td>Review negotiation topics</td><td>Context and negotiation topics</td></tr><tr><td>Capture a glossary of terms</td><td>Initial set of win conditions and glossary terms</td></tr><tr><td>Identify issues and options</td><td>WinWin tree</td></tr><tr><td>Negotiate agreements</td><td>Completeness of negotiation results</td></tr><tr><td>Negotiate agreements</td><td>Completeness of documentation</td></tr></table>

Step 1: Check the context and negotiation topics. The moderator and the stakeholders check the list of negotiation topics with respect to the mission statement and statement of negotiation purpose. The negotiation topics shall be consistent with the scope and boundaries of the system as defined in the mission statement. In addition, they shall sufficiently address the system environment and interfaces; functions and nominal and off-nominal cases; risks, technical and organizational constraints and conditions; system quality issues, level of service, and performance; and project issues, such as budget, time, resources, economic constraints, and conditions.

Step 2: Check the initial set of win conditions and glossary terms. The next check in the process is after converging on win conditions and defining glossary terms. Important conditions to be checked are:

• All win conditions express a stakeholder goal and are related to a specific negotiation topic. Further, they must be within the scope of the mission statement. If a win condition covers more than one topic, it should be split up.

• All important and possibly ambiguous or unclear terms in the win conditions are defined in the glossary.

Step 3: Check the WinWin tree. After the identification of issues, options, and agreements the checks from the preceding stages can be repeated. Rules for describing agreements, risks, and glossary terms include:

• All win conditions and options are defined as complete, active, and positive sentences.

• An issue states a risk, constraint, or uncertainty on a win condition, and not a solution or alternative.

• An option states a solution or an alternative to overcome an issue.

• An agreement is either derived from a win condition not raising any issues or from an option.

• Important and possibly unclear terms in the issues, options, or agreements are defined in the glossary.

• Agreements and potential risks can be traced back to the initial win conditions in the WinWin tree.

Step 4: Check the completeness of negotiation results. At the end of the negotiation, agreements and potential risks are organized by negotiation topics. Sorted and reduced results are checked for completeness and comprehensibility.

• Agreements express goals that can be more general than requirements.

• Potential risks are open issues that could not be resolved during the negotiation.

• The glossary defines all potentially unclear terms in an unambiguous way (e.g., does not contain undefined terms).

Step 5: Check the completeness of documentation. The completeness of the documentation can be checked for project management and requirements engineering purposes at the end of a negotiation:

• For each negotiation topic, there is at least one win condition. Otherwise, the list of negotiation topics should be revised or missing win conditions should be identified.

• The set of agreements should provide a useful basis for developing plan, contract, requirements document, and so on.

## Post-Process Quality Assurance

In addition to the joint and rapid checks performed by the stakeholders described in the preceding section, we will now present an inspection technique following the standard inspection process [12] consisting of the following stages:

1. Inspection preparation to check the entry criteria of completeness and sufficient quality for understanding the inspection context.

2. Individual reading supported with reading techniques optimized for negotiation results.

3. Meeting of inspectors or some other form of defect collection.

4. Report and rework to clarify the issues raised with the author if possible, or to document the problem and the resolution in a traceable way. Possible rework strategies depend on defect severity.

In this section, we describe the first two steps of the process; that is, preparation and individual reading. The main differences to the checks described in the “In-Process Quality Assurance” subsection are that (1) only consolidated results and no temporary work products get checked and (2) the inspectors might have no knowledge of the negotiation process, so traceability in the results and clear definition of important terms are of specific importance. The inspectors are not necessarily system stakeholders but can also be independent expert reviewers whose purpose is to expedite the transition from quickly determined top-level stakeholder agreements to more clear, correct, complete, and consistent requirements with respect to the defined negotiation purpose. Thus, the inspection can also support stakeholders who did not participate in the negotiation and who need to understand the negotiation results.

Our inspection approach adopts a reading technique. Reading is a key activity in defect detection to understand a given software artifact and compare it to a set of expectations regarding structure, content, and desired qualities. Ad hoc inspections depend largely on inspector experience and do not facilitate a repeatable process. Defect detection should thus be supported with repeatable reading techniques [1], guiding the inspectors through the inspected document and instructing them what target defect classes to uncover and how to perform quality checking. An example of a general reading technique is a checklist showing all defect types or symptoms to look for in a particular document type, usually independent from a specific notation.

Perspective-based reading [1] exploits different viewpoints such as users, designers, or testers. For each perspective, there can be a scenario, which describes procedures (e.g., to produce a model such as a user’s manual for the user’s view, high-level design sequence diagrams for the designer’s view, or test cases for the tester’s view). These models can be analyzed to answer questions based on the particular perspective’s qualities. The underlying assumption is that the union of perspectives provides extensive coverage of the range of defects present, while each reader is responsible for a narrowly focused view of the document, which is supposed to result in a more indepth analysis of potential defects in the document.

## Planning and Preparation for Inspection

The inspection leader has to make sure that the material is complete and has sufficient quality on the superficial level to start the inspection: Negotiation results should state agreements with clear responsibilities as well as open issues and how they are going to be resolved. Also, the importance and feasibility of the agreements should be available. The negotiation results are then organized, and the inspection object with the following outline is prepared:

• context and overview: mission statement for the negotiation (to assess level of details of negotiation contributions), statement of negotiation purpose, reference material, list of identified stakeholders, their roles, and acronyms;

• a list of agreements together with the thread of win conditions, issues, and options leading to each agreement organized by negotiation topics;

• a list of potential risks, that is, unresolved issues sorted by negotiation topics; and

• a glossary of terms, that is, definitions for the language used in the project/ domain.

Further, the inspection manager has to check whether all success-critical stakeholders participated in the negotiation to ensure commitment to agreements and potential risks. If a stakeholder could not participate, it is crucial to inform him or her about the negotiation and solicit information missing in the prerequirements. Candidates for inspectors are either expert reviewers or success-critical stakeholders who were not present at the workshop. Performing an inspection of the prerequirements by the stakeholder is an excellent preparation for follow-up activities and an opportunity to strengthen stakeholder involvement.

## Reading Technique for Management and Technical Perspectives

For individual reading, we suggest to use several perspectives to minimize the overlap between the inspectors and to exploit different stakeholder viewpoints [1]. Therefore, this should include persons covering the management perspective (e.g., a project manager) as well as the technical focus (e.g., a requirements engineer). The perspectives give general guidelines (relevant for all readers) to check for clarity, and specific content focus to (1) the project manager on project and process management parts and (2) requirements engineers on technical content and external understandability.

Each inspector is asked to perform the following defect detection procedure individually and independently. The procedure aims at preparing the inspector with an overview and then continuing with detailed checks for clarity, correctness, completeness, and consistency in consecutive stages. The strategy is to support the inspector with easily digestible steps to avoid cognitive overload.

In the following, we present a condensed description of the steps from the operational version of the reading technique.

Getting an Overview. Inspectors are asked to get an overview on the material handed over to them and check it for completeness; that is, availability of a mission statement, negotiation topics, a list of agreements, a list of potential risks (open issues), and a glossary describing all terms, which may be unclear or have a special meaning in the project (other than usual in general, in the profession, or in the organization).

Understanding the Introduction. In this task, inspectors are asked (1) to read the mission statement to understand the main project and negotiation goals and (2) to list important information they would expect to find in the negotiation results. This list of expected information is later compared with actually available information. Furthermore, they quickly scan through the lists of agreements and potential risks, and mark the portions of text that are of particular interest to their point of view (project manager versus requirements engineer) with respect to the project goals. Inspectors also check the list of negotiation topics for clarity and completeness by comparing it to a standard requirements engineering reference.

Checking for Clarity. Inspectors check each statement and mark potentially unclear/ambiguous terms and statements. They look up unclear terms in the glossary, and report missing definitions. Inspectors further report unclear statements and mark win conditions belonging to several negotiation topics or listed under the wrong negotiation topic.

Checking for Correctness and Completeness. Inspectors check each statement relevant for their perspective and mark incorrect statements. They also check whether each win condition really presents a goal, each issue really is a constraint or objection, and each option really suggests a solution. Furthermore, they mark statements that do not describe a goal (e.g., a design solution) and list missing information by comparing the actual negotiation to the things they expected to find (see above).

Checking for Consistency. In this task, inspectors mark statements that contradict each other and any other forms of inconsistency (e.g., win condition versus glossary definition; defects in the structure of a WinWin tree).

Checking the Glossary. Each entry in the glossary is checked for clarity and correctness of the definition, especially whether unclear terms in the definition are explained appropriately.

## Automating the Quality Assurance Techniques

We have been defining and automating pre-process techniques, in-process QA techniques, and post-process inspections. Pre-process and in-process techniques are described in the EasyWinWin process guide [15]. The guidebook also shows how groupware tools can be used to support the checking activities. In order to provide appropriate tool support for the inspection technique, we customized the GroupSystems.com’s GSS suite for post-process defect collection and inspection support [21]. The major benefits of using a GSS for inspections are as follows:

• its flexibility allows customizing it to different inspection process designs (e.g., different reading techniques, perspectives);

• the inspection process can be continuously monitored, which allows the inspection manager to continuously optimize the process [19];

• it supports both individual defect detection tasks as well as inspection meetings;

• it can be integrated with the EasyWinWin methodology;

• it supports different inspector roles, that is, inspectors performing different defect detection tasks.

## Feasibility Study

THIS SECTION DISCUSSES QUALITATIVE EXPERIENCES we gained in a feasibility study carried out to evaluate the usefulness of the post-process inspections. Please note that the presented study has some limitations due to the small number of participating subjects: (1) it exclusively focuses on post-process inspection and does not evaluate pre-process and in-process QA techniques, (2) it cannot provide quantitative results for detailed statistical analysis, and (3) it does not compare multiple alternative inspection techniques. However, the qualitative results presented in the following sections yield interesting insights into the benefits, costs, and challenges of the proposed inspection technique for prerequirements documents.

## Study Process

We used negotiation results from projects carried out in fall 2000 at the University of Southern California, and asked ten persons to inspect them using the inspection process described in the “Post-Process Quality Assurance” subsection. Neither the designers of the inspection technique nor the inspectors were familiar with the selected negotiations before the actual inspection. The inspectors included experienced project managers, researchers, professional developers, and students.

Table 4. Number of Inspectors (I) per Perspective and Mean Number of Normal/ Major/Critical Defects Found (N, M, C) for Each Inspection Object.

<table><tr><td rowspan="2">Perspective</td><td colspan="4">Inspection object 1</td><td colspan="4">Inspection object 2</td></tr><tr><td>I</td><td>N</td><td>M</td><td>C</td><td>I</td><td>N</td><td>M</td><td>C</td></tr><tr><td>Project manager</td><td>3</td><td>6.7</td><td>2.7</td><td>3.3</td><td>3</td><td>5.3</td><td>2</td><td>3.3</td></tr><tr><td>Requirements engineer</td><td>7</td><td>6.6</td><td>1.6</td><td>1</td><td>7</td><td>6.7</td><td>0.9</td><td>0.6</td></tr></table>

The two selected inspection objects dealt with Web-based library systems so that inspector familiarity and domain knowledge could be assumed. Inspection object 1 contained 41 agreements and 27 glossary entries. Inspection object 2 contained 39 agreements and 15 glossary entries. Both EasyWinWin negotiation documents followed the structure described in the “Post-Process Quality Assurance” subsection. A smaller negotiation document was used during a tutorial explaining the structure of negotiation results and examples of possible defects. All inspectors received a short tutorial on EasyWinWin, the overall inspection process, and the reading techniques. During the tutorial, the inspectors were asked to practice reading techniques for both stakeholder views. After this dry run, we clarified arising questions, assigned a stakeholder perspective to each inspector, and had them proceed with the inspection. Each inspector inspected two EasyWinWin negotiations and completed a feedback questionnaire. After the real inspection, the experiment team analyzed the defect reports, determined the number of true defects, and assigned defect types.

## Study Results

Table 4 provides the average number of defects found in the inspection objects for different defect severities. The defect severity (normal, major, and critical) depends on an estimate of effort required to fix the defect later on during development if it is not detected and removed at this stage. Although the selected documents are relatively small, inspectors identified a considerable number of defects. Because of the small sample size, we do not provide sophisticated statistical measures, but focus on qualitative results instead.

Inspector Experience. A qualitative result we expected is that experience with a certain reading perspective has a strong impact on inspection effectiveness. It turns out that detecting defects is more difficult in requirements negotiation results than in requirements specifications or designs where defect types can be defined more precisely. Our results show that experienced inspectors found more true defects and, at the same time, also needed more time for inspection. Inexperienced inspectors reported difficulties to clearly identify defects and to assess defect severity.

Defect Types. The most frequent defect type detected by experienced inspectors was missing or unclear information. Experienced inspectors started the inspection with higher expectations (i.e., they were checking if certain important topics were addressed adequately) compared to inexperienced inspectors. An interesting result is, however, that inexperienced inspectors did a better job in finding inconsistencies.

Effort. The effort required to perform the inspections was relatively low. The mean effort for project managers/requirements engineers for inspection object 1 was 43/76 minutes. The mean effort for project managers/requirements engineers for inspection object 2 was 48/66 minutes. This also confirms our expectations that requirements engineers who had to take a more thorough look at the entire document (as defined in the reading technique) needed considerably more time than project managers.

As the focus of this feasibility study was put upon qualitative feedback, we used a questionnaire and interviews to collect feedback data. Main qualitative results regarding the EasyWinWin negotiation results are:

Acceptance of Inspection Objects. The acceptance of the negotiation document structure was very high. All inspectors agreed on the usefulness of EasyWinWin for negotiating and documenting requirements.

Varying Level of Detail. The main problem reported when inspecting a results document was the varying level of detail in the investigated artifacts. Some aspects are discussed and presented in great detail, while other aspects of the project are not touched at all or only on a superficial level. We have, meanwhile, updated the EasyWinWin facilitation guidelines [15] to address this problem.

Interdependencies. Inspectors also reported that they had difficulties in dealing with similar or overlapping agreements, that negatively affected the readability of the document. We have updated the EasyWinWin process guide to better address interdependencies among agreements and other artifacts.

Main experiences regarding the inspection process include the following:

Acceptance of Inspection Technique Effectiveness. There was a strong consensus among inspectors that the inspection process and the reading technique are suitable for the inspection objects and that they support the detection of defects. Inspectors also agreed that the EasyWinWin results were considerably improved through fixing the detected defects.

Assessment of Defect Severity. The assessment of defect severity turned out to be difficult due to the broad and large variety of topics addressed. Often, fairly general information is included and details are left for further analysis steps, which make it often hard to estimate defect severity.

Precision. The defect detection technique to quickly mark all parts of a negotiation that are relevant for a specific stakeholder perspective seems to favor overlooking defects. Participants reported that important information might easily be overlooked.

Project Size. Some inspectors argued that the reading technique might be inefficient for small and simple inspection objects (such as the tutorial document), as the separation of different defect types via reading techniques might lead to redundant defect detection tasks thus creating overhead. However, the complexity of EasyWinWin results we typically find in practice justify a well-structured, systematic defect detection approach.

IN THIS PAPER, WE DISCUSSED THE IMPORTANCE of repeatable quality assurance techniques for collaborative processes and presented QA techniques complementing the EasyWinWin requirements negotiation approach. We believe that, although the process is currently optimized for EasyWinWin, it can also be tailored with little effort to other collaborative processes.

As requirements negotiation results represent valuable information for all successcritical stakeholders, it is important to ensure that they are of high quality to expedite the development of other crucial life-cycle deliverables, such as specifications, plans, and so on. It is essential to remove defects from requirements negotiation results to increase the chance to finish the project successfully on time and within budget. Therefore, we provide a set of structured and well-defined techniques aiming at defect reduction.

In a feasibility study, we show that the post-process inspection of requirements negotiation results with reading techniques is feasible and effective, as the inspection reveals numerous defects. Compared to the inspection of other documents [2], the efficiency of prerequirements inspection is high. We believe that our approach helps to improve communication, trust, and shared vision, where detailed issues and conflicts may, of course, occur, but in a well-set framework, rather than in an unclear context.

QA techniques, as discussed in this paper, also rely on different modes of collaboration. Whereas pre-process QA is typically done by the process leader, in-process QA is perform by the team of stakeholder during a facilitated session. Post-process QA requires the integrating of the inspection results from different inspectors collaborating in an asynchronous and dislocated manner. Thus, although some of the QA processes are also done in a collaborative manner (e.g., in-process QA), they rely, to a large extent, on individual work of inspectors and facilitators.

Further work will focus on using and evaluating the described techniques in industry projects. We also identified potential improvements for the EasyWinWin tools (e.g., improved formatting support). Such relatively simple support would allow a moderator to focus even more on QA activities and would also prevent defects.

Beyond that, we will concentrate on extracting valuable information on the importance of system features for project and quality planning from high-quality negotiation results. Project managers could, for example, select those working products (e.g., specific sections of requirements or design documents) for inspection, which represent major sources of risk in a project. It is also important to apply inspection techniques in order to ensure that working products created during development comply with agreements made earlier during requirements negotiation.

has been supported by the Austrian Science Fund, Grant P-14128-COSIMIS. Stefan Biffl has been funded in part under the Austrian Science Fund Grant J-1948-INF.

## REFERENCES

1. Basili, V.; Green, S.; Laitenberger, O.; Lanubile, F.; Shull, F.; Soerumgaard, S.; and Zelkowitz, M. The empirical investigation of perspective-based reading. Empirical Software Engineering: An International Journal, 1, 2 (1996), 133–164.

2. Biffl, S., and Halling, M. Software product improvement with inspection. In F. Vajda (ed.), Euromicro 2000 Conference Software Product and Process Improvement Track. Los Alamitos, CA: IEEE Computer Society Press, 2000, pp. 262–269.

3. Bisant, D.B., and Lyle, J.R. A two-person inspection method to improve programming productivity. IEEE Transactions on Software Engineering, 15, 10 (1989), 1294–1304.

4. Boehm, B.W. Industrial software metrics top ten list. IEEE Software, 4, 5 (1987), 84–85.

5. Boehm, B.W.; Grünbacher, P.; and Briggs, R.O. Developing groupware for requirements negotiation: Lessons learned. IEEE Software, 18, 3 (May–June 2001): pp. 46–55.

6. Boehm, B.W.; Bose, P.; Horowitz, E.; and Lee, M.J. Software requirements as negotiated win conditions. In First International Conference on Requirements Engineering. Los Alamitos, CA: IEEE Computer Society Press, 1994, pp. 74–83.

7. Briggs, R.O., and Grünbacher, P. EasyWinWin: Managing complexity in requirements negotiation with GSS. In R.H. Sprague, Jr. (ed.), Proceedings of the Thirty-Fifth Hawaii International Conference on System Sciences, Volume 1. Los Alamitos, CA: IEEE Computer Society Press, 2002 (available at csdl.computer.org/comp/proceedings/hicss/2002/1435/01/ 14350021babs.htm).

8. Briggs, R.O.; de Vreede, G.J.; and Nunamaker, J.F., Jr. Collaboration engineering with thinkLets to pursue sustained success with group support systems. Journal of Management Information Systems, 19, 4 (Spring 2003), 31–63.

9. Briggs, R.O.; de Vreede, G.J.; Nunamaker, J.F., Jr.; and Tobey, D.H. ThinkLets: Achieving predictable, repeatable patterns of group interaction with group support systems (GSS). In R.H. Sprague, Jr. (ed.), Proceedings of the Thirty-Fourth Hawaii International Conference on System Sciences. Los Alamitos, CA: IEEE Computer Society Press, 2001 (available at csdl.computer.org/comp/proceedings/hicss/2001/0981/01/09811057abs.htm).

10. Fagan, M. Design and code inspections to reduce errors in program development. IBM Systems Journal, 15, 3 (1976), 182–211.

11. Genuchten, M.; Dijk, C.; Scholten, H.; and Vogel, D. Industrial experience in using group support systems for software inspections. IEEE Software, 18, 3 (2001), 60–65.

12. Gilb, T., and Graham, D. Software Inspection. Boston: Addison-Wesley Professional, 1993.

13. Glass, R.L. Inspections—Some surprising findings. Communications of the ACM, 42, 4 (1999), 17–19.

14. Gotel, O., and Finkelstein, A. Contribution structures. In Second IEEE International Symposium on Requirements Engineering. Los Alamitos, CA: IEEE Computer Society Press, 1995, pp. 100–107.

15. Grünbacher, P. EasyWinWin OnLine: Moderator’s guidebook, a methodology for negotiating software requirements. GroupSystems.com, Linz, Austria, 2000.

16. Grünbacher, P., and Briggs, R.O. Surfacing tacit knowledge in requirements negotiation: Experiences using EasyWinWin. In R.H. Sprague, Jr. (ed.), Proceedings of the Thirty-Fourth Hawaii International Conference on System Sciences. Los Alamitos, CA: IEEE Computer Society Press, 2001 (available at csdl.computer.org/comp/proceedings/hicss/2001/0981/01/ 09811062abs.htm).

17. Grünbacher, P.; Halling, M.; and Biffl, S. An empirical study on groupware support for software inspection meetings. In Eighteenth IEEE International Conference on Automated Software Engineering. Los Alamitos, CA: IEEE Computer Society Press, 2003, pp. 4–11.

18. Halling, M., and Biffl, S. Using reading techniques to focus inspection performance. In Proceedings of the Twenty-Seventh Euromicro Conference 2001: A Net Odyssey (Euromicro’01). Los Alamitos, CA: IEEE Computer Society Press, 2001, pp. 248–257.

19. Halling, M.; Biffl, S.; and Grünbacher, P. A groupware-supported inspection process for active inspection management. In M. Fernandez, I. Crnkovic, G. Fohler, C. Griwodz, T. Plagemann, and P. Grünbacher (eds.), Proceedings of the Twenty-Eights Euromicro Conference 2002. Los Alamitos, CA: IEEE Computer Society Press, 2002, pp. 251–258.

20. Halling, M.; Biffl, S.; and Grünbacher, P. An experiment family to investigate the defect detection effect of tool-support for requirements inspection. In Ninth IEEE International Software Metrics Symposium. Los Alamitos, CA: IEEE Computer Society Press, 2003, pp. 278–285.

21. Halling, M.; Grünbacher, P.; and Biffl, S. Tailoring a COTS group support system for software requirements inspection. In Sixteenth IEEE International Conference on Automated Software Engineering. Los Alamitos, CA: IEEE Computer Society Press, 2001, pp. 201–210.

22. IEEE. IEEE Standard Glossary of Software Engineering Terminology. Los Alamitos, CA: Institute of Electrical and Electronics Engineers, 1990.

23. Kunz, W., and Rittel, H. Issues as elements of information systems. Center for Planning and Development Research, University of California, Berkeley, 1970.

24. Laitenberger, O. Cost-effective detection of software defects through perspective-based inspections. University of Kaiserslautern, Germany, 2000.

25. Laitenberger, O., and DeBaud, J.-M. An encompassing life cycle centric survey of software inspection. Journal of Systems and Software, 50, 1 (2000), 5–31.

26. Lee, J., and Lai, K.Y. A comparative analysis of design rationale representations. Center for Coordination Science, MIT, Cambridge, MA, 1991.

27. MacLean, A.; Young, R.M.; and Moran, T.P. Design rationale: The argument behind the artifact. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems: Wings for the Mind. New York: ACM Press, 1989, pp. 247–252.

28. Parnas, D., and Lawford, M. Special issue on inspection. IEEE Transactions on Software Engineering, 29, 8 (2003), 674–676.

29. Potts, C., and Burns, G. Recording the reasons for design decisions. In Tenth International Conference on Software Engineering. Los Alamitos, CA: IEEE Computer Society Press, 1988, pp. 418–427.

30. Redmill, F. Fagan’s inspection: Achieving quality in code and documentation; Built-in gauge of effectiveness. Managing System Development, 13, 3 (1993), 1–5.

31. Sharp, H.; Finkelstein, A.; and Galal, G. Stakeholder identification in the requirements engineering process. In Tenth International Workshop on Database & Expert Systems Applications. Los Alamitos, CA: IEEE Computer Society Press, 1998, pp. 387–391.

32. StandishGroup. CHAOS Report. West Yarmouth, MA, 1994.

33. Toulmin, S. The Uses of Argument. Cambridge: Cambridge University Press, 1958.
