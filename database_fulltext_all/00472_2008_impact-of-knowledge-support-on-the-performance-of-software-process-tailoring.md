---
otero_id: 472
otero_key: "ZMJ5DKVE"
title: "Impact of Knowledge Support on the Performance of Software Process Tailoring"
authors: "Peng Xu; Balasubramaniam Ramesh"
year: "2008"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222250308"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/ZMJ5DKVE/fulltext/images/0349b2050450888f0c659e4ebb099e38d8f40f768a686c406920cb293805cca3.jpg)

# Impact of Knowledge Support on the Performance of Software Process Tailoring

## Peng Xu & Balasubramaniam Ramesh

To cite this article: Peng Xu & Balasubramaniam Ramesh (2008) Impact of Knowledge Support on the Performance of Software Process Tailoring, Journal of Management Information Systems, 25:3, 277-314

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222250308

![](/api/attachments/ZMJ5DKVE/fulltext/images/da1af28f2def492cce20f2f12c218e59a2401c7a78d6c11e278dfe7c429f2d48.jpg)

Published online: 08 Dec 2014.

![](/api/attachments/ZMJ5DKVE/fulltext/images/e2031992a93e598207d0e2fc1785040add7ec0b669eae6f4a439c191f93b4a68.jpg)

Submit your article to this journal

Article views: 2

![](/api/attachments/ZMJ5DKVE/fulltext/images/f631e3693330ea4d3839009cfc0fbbbc6094398df73c3c06c6c279b6c346d3f4.jpg)

View related articles

# Impact of Knowledge Support on the Performance of Software Process Tailoring

Pen g Xu and Balas ub ramani am Rames h

Peng Xu is an Assistant Professor at the Department of Management Science and Information Systems of the University of Massachusetts Boston. She received her Ph.D. in Computer Information Systems from Georgia State University in 2004. Her research areas are knowledge management, software process, software engineering, and process agility. Her work has appeared in journals such as the Journal of Management Information Systems, Requirements Engineering Journal, Communications of the ACM, and Information and Management, and conference proceedings such as the Workshop on Information Technologies and Systems (WITS) and the Hawaii International Conference on System Sciences (HICSS).

Balasub ramaniam Ramesh is Board of Advisors Professor of Computer Information Systems at Georgia State University. His research interests include supporting complex organizational processes such as requirements management, agile software development, and business process management with decision support and knowledge management systems and methods. His research has appeared in several leading journals, including the MIS Quarterly, Journal of Management Information Systems, IEEE Transactions on Software Engineering, Annals of Software Engineering, Communications of the ACM, Journal of the AIS, IEEE Computer, IEEE Software, IEEE Internet Computing, IEEE Intelligent Systems, Requirements Engineering Journal, and Decision Support Systems. His work has been funded by several leading government and private industry sources such as the National Science Foundation, Defense Advanced Research Projects Agency, Office of Naval Research, Army Research Laboratory, and Accenture and has been incorporated in several computer-aided systems engineering tools.

Ab stract: The use of a well-defined process is a widely recognized approach to increasing quality and productivity in software development. Building software processes from scratch each time is expensive and risky. Therefore, they are often created by tailoring existing processes and standards. Process tailoring is a knowledge-intensive activity. This research explores the link between knowledge support and software process tailoring performance under different levels of tailoring task complexity. It theoretically develops and tests how the fit between knowledge (generalized and contextualized) and software tailoring task complexity influences process tailoring performance. Process tailoring performance is conceptualized in terms of effectiveness and efficiency. The results from an experiment and a protocol analysis show that contextualized knowledge outperforms generalized knowledge in improving tailoring performance, and that such improvement in performance is greater in complex process tailoring tasks when compared to simple tasks.

Key words and phrases: contextualized knowledge, generalized knowledge, knowledge management, software process, software process tailoring.

A well-designed software process<sup>1</sup> is critical to improving productivity and quality in software development projects. A software process identifies major tasks that need to be performed in a software project, people who perform these tasks, and inputs and outputs of each task. Pursuing software development with an inappropriate process may result in poorly designed architecture and code, expensive redevelopment, delay, or even total project failure [28]. The importance of a well-defined software process has motivated the development of process standards such as the IEEE/EIA 12207 [27] and frameworks such as Rational Unified Process (RU P<sup>®</sup>) [28] that specify the phases (e.g., requirements gathering, system analysis and design, etc.) in a software development process, the activities (e.g., modeling business processes, identifying user requirements, etc.) that need to be performed in each phase, the sequence in which the phases and activities are carried out, the roles of various stakeholders (e.g., system analysts, system architect, etc.) involved in each phase and activity, and the artifacts (e.g., business model, use case model, etc.) that are used or produced by the activities in each phase.

These “standard” processes need to be tailored before they can be adopted in a project. The practice of adjusting processes for differences across environments is called software process tailoring [64]. It involves adjusting the formality, frequency, granularity, and scope of process components such as activities, artifacts, and roles [19]. A software process is tailored to suit the unique characteristics of a project such as business domain, customer requirements, technology, etc. [4, 64]. The fit between the process used and the characteristics of the project is a major determinant of project success. Both the extant literature and industry standards such as IEEE/EIA 12207 and RU P<sup>®</sup> have emphasized the importance of software process tailoring in ensuring project success [28].

Tailoring a process for a project is a knowledge-intensive activity. Although major process frameworks such as RU P<sup>®</sup> seek to be tailorable, the tailoring guidelines provided by them are too coarse-grained to be of specific help to process designers. These guidelines can be used to perform first-level tailoring (i.e., adapt the process to a given application area such as aviation, health care, and defense). For example, RU P<sup>®</sup> tailoring guidelines that are detailed in white papers address only the general issues faced in particular types of projects (e.g., small projects [43]) and Web-based applications [36]). Similarly, the IEEE standards identify major activities in process tailoring (e.g., “identify project environment,” “solicit inputs,” “select processes”), but do not provide any details on how to implement these activities [27] or include guidance on how to achieve second-level tailoring—that is, tailoring the standards for a specific project [27, 28].

The use of knowledge repositories that codify past experiences for improving performance in knowledge-intensive tasks is well established [5, 20]. Recent research suggests that leveraging experience gained from successful software processes can significantly increase the effectiveness and efficiency in future projects [24]. Therefore, an effective way to facilitate process tailoring is to provide access to knowledge gained from past experiences in process tailoring. However, beyond an abstract framework, current research does not provide detailed implementation guidelines in terms of how to build repositories of past knowledge. Specifically, it does not provide any strate gies for codifying past experience that can improve software process tailoring. Few studies have focused on the types of knowledge that may be managed in knowledge repositories and their impact on the tasks supported.

## Theory Development

Our study theoretically develops and tests how cognitive fit between two types of knowledge (generalized and contextualized) and software tailoring task complexity influences process tailoring performance. Cognitive fit theory proposes that only when cognitive fit exists between task support and the task to be performed, task support can demonstrate a positive influence on task performance [51]. We argue that these two types of knowledge support cognitively fit (or match) software process tailoring tasks, and therefore can improve tailoring task performance. Further, Nickerson and Zenger [38] suggest that different types or classes of problems that need to be solved call for different types of strategies. Similarly, cognitive fit theory also suggests that task characteristics can moderate the relationship between task support and task performance [56]. One important task characteristic that can influence the use of knowledge support is task complexity [38]. Therefore, in our study, we also examine the moderating effect of process tailoring task complexity on the use of these two types of knowledge in solving tailoring tasks. We study the two dimensions of task performance—effectiveness of tailoring decisions and efficiency of tailoring decisions. Effectiveness of software process tailoring is defined as the quality of tailoring decisions [14, 42]. Efficiency of process tailoring is defined as effort needed for process tailoring [7, 60].

## Cognitive Fit in Knowledge Support

Based on information processing theory, Vessey [61] proposes cognitive fit theory and Vessey and Galletta state that cognitive fit is “a cost–benefit characteristic that suggests that for most effective and efficient problem solving to occur, the problem and any tools or aids employed should all support the strategies (methods or processes) required to perform that task” [62, p. 64]. This theory was used to explore the effects of graphical and tabular representations on decision-making performance. This theory suggests that task performance is an outcome of the interaction between two elements—problem representation and problem-solving tasks. When the information presented in these two elements match (i.e., emphasizing the same type of information), the process to act on the problem presentation is consistent with the process to complete the task. Therefore, decision makers can easily deploy consistent problem-solving processes to form a mental representation of the problem and produce results. However, a mismatch in these two elements usually results in extra effort in transforming inconsistent cognitive processes and leads to poor task performance. This theory has been widely used to guide studies on information/knowledge representation, technology support, and problem solving (see Table 1).

<table><tr><td colspan="4">Cognitive fit</td></tr><tr><td>Task</td><td>Task support</td><td>Fit type</td><td>References</td></tr><tr><td>Spatial task and symbolic task</td><td>Information representation (graphical and tabular)</td><td>Fit as matching</td><td>[61, 62]</td></tr><tr><td>Geographic tasks where there are adjacency relationships among the geographic areas versus geographic tasks where there are no adjacency relationships</td><td>Information representation (map-based versus tabular)</td><td></td><td></td></tr><tr><td rowspan="2">Software function-oriented maintenance tasks versus control flow maintenance tasks</td><td rowspan="2">Mental representation of the software (domain model focuses on software functionality versus program model relying on the understanding of programming language)</td><td>Fit as matching</td><td>[13]</td></tr><tr><td>Fit as matching</td><td>[48]</td></tr><tr><td>Recursion programming tasks versus iteration programming tasks</td><td>Programming tools (LISP versus PASCAL)</td><td>Fit as matching</td><td>[51]</td></tr><tr><td>Object-oriented requirement modeling tasks versus process-oriented requirement modeling tasks</td><td>Object-oriented methodology and process-oriented methodology</td><td>Fit as matching</td><td>[2]</td></tr><tr><td>Syntactic and semantic comprehension tasks versus schema-based problem-solving tasks</td><td>Application domain knowledge (low versus high)</td><td>Fit as matching</td><td>[29]</td></tr><tr><td>Low complexity decision-making tasks versus high complexity decision-making tasks</td><td>Query interface (visual versus text-based)</td><td>Fit as moderation</td><td>[54]</td></tr><tr><td>Viewing virtually high experiential product tasks versus virtually low experiential product tasks</td><td>Virtual reality technology versus no virtual reality technology support</td><td>Fit as moderation</td><td>[56]</td></tr></table>

Although cognitive fit theory was first proposed in the context of information representation, it has been adopted to study the fit between tasks and problem-solving support such as programming tools [51], software development methodology [2], knowledge support in software maintenance [29], and virtual technology [56]. Also, a recent study [51] finds that the fit between a task and its problem-solving support is more important than the fit between the task and problem representation. Cognitive fit theory proposes a general problem-solving concept that can be applied in various problem-solving scenarios, that is, the impact of task support is contingent upon the types and nature of tasks; only when cognitive fit exists between task support and the task to be performed, task support has a positive influence on task performance.

Prior research has shown the importance of cognitive fit between application domain knowledge and comprehension tasks in information systems (IS) development [29]. In our research, using cognitive fit theory, we investigate the effectiveness of knowledge support in improving performance in software process tailoring tasks. We propose two types of knowledge that can be used to facilitate process tailoring—generalized knowledge and contextualized knowledge. We argue that these two types of knowledge support match the needs of tasks involved in tailoring a software process for a project and, therefore, improve tailoring performance measured by tailoring effectiveness and efficiency.

Although the majority of studies on cognitive fit concentrate on the match between task support and tasks, prior research also demonstrates that cognitive fit also affects the degree of influence of task support on task performance when performing different tasks [56]. Speier and Morris [54] show that task complexity and spatial ability of decision makers can moderate the influence of query interface on decision outcomes. Suh and Lee [56] show that while virtual reality technology can influence consumer learning in general, its positive impact is moderated by the types of products involved. The effect is more pronounced when viewing virtually high experiential products. In similar spirit, we also investigate whether the degree of influence of two types of knowledge support on process tailoring tasks is moderated by different tailoring tasks. We focus on task complexity, which is recognized as an important factor that influences task performance [37, 54]. In the following sections, we describe two types of knowledge support that can be used in software process tailoring, their impact on tailoring tasks, and the moderating effect of task complexity.

## Knowledge Support in Software Process Tailoring

As a multifaceted concept, knowledge has been classified based on its nature, format, content, domain, and so forth [41, 45]. For example, based on its content, knowledge can be classified as declarative knowledge that describes factual knowledge and procedural knowledge that describes knowledge exercised in the performance of some task [3, 45]. Knowledge can also be classified as general knowledge and specific knowledge based on the specificity of knowledge [46]. Nonaka [41] classified knowledge into two types—tacit and explicit. Knowledge that can be codified and transmitted in written forms is called explicit knowledge, whereas knowledge that roots in action and is not yet externalized and formalized is tacit knowledge. One of the key modes of knowledge creation is externalization that converts tacit knowledge to explicit [3, 41]. In fact, prior research on software development favors this method by suggesting that knowledge gained from prior experiences needs to be abstracted and stored for future reuse [5]. In this study, we investigate the role of two types of externalized knowledge—generalized knowledge and contextualized knowledge—in supporting software process tailoring tasks. Appendix A gives some examples of generalized and contextualized knowledge.

Knowledge is embedded in the action and memory of individuals, which collectively can construct the organizational knowledge base. Individual memory consists of skill-based, semantic, and episodic memory [25, 55]. The skill-based memory keeps information about a process that is used to perform a task such as riding a bicycle [45, 55]. Semantic memory is independent of any specific events and settings, and is stored as a network of concepts built from events individuals have experienced over time [25, 55]. Episodic memory contains information about specific experiences, including the context of the events [25, 30, 55]. The latter two types of memory jointly can be called declarative memory [45, 55]. Because software process tailoring mainly involves evaluating the environment of a project, assessing resources, and making decisions, knowledge about software process tailoring is influenced by both semantic memory and episodic memory. Prior research calls for the need to externalize such memory to construct knowledge bases [55]. We recognize that externalization of both types of memory can help problem solving in process tailoring. Both of these two types have high domain specificity. The difference between them is in their contextual specificity. Externalized semantic memory has low contextual specificity, whereas externalized episodic memory has high contextual specificity.

## Generalized Knowledge

Semantic memory generalizes knowledge across specific experiences [25]. We refer to externalized semantic memory as generalized knowledge [25, 30]. Different from general knowledge defined in Sabherwal and Becerra-Fernandez [46] as knowledge with low technical and contextual specificity, generalized knowledge is defined in our study as knowledge that is high in domain knowledge specificity but low in contextual knowledge specificity. Sabherwal defines a knowledge type called technology specific knowledge as “knowledge of the particular scientific or theoretical discipline” [46, p. 303]. We extend this definition to accommodate other domain knowledge involved in software process tailoring such as managerial and process knowledge and refer to it as generalized knowledge [25, 30]. Prior research in the fields of artificial intelligence (AI) and decision support systems (DSS) establishes the value of extracting knowledge from experts’ semantic memory and representing it in a general form to facilitate knowledge transfer and improve problem solving [21, 45].

In software development, semantic memory of experts can be externalized and represented in generalized forms such as algorithms, mathematical models, and general rules. Formal knowledge such as algorithms and mathematical models that mainly rely on mathematical symbols to represent information is too restrictive to represent the knowledge used in process tailoring. Prior research has shown that generalized knowledge about process tailoring can be adequately represented as rules that define a set of conditions under which a project is required to execute specific activities or implement certain tailoring strategies [23].

Generalized knowledge represented as general rules match the requirements of process tailoring tasks. In other words, there is cognitive fit between generalized knowledge and process tailoring tasks and this fit will improve tailoring task performance. When tailoring a process for a project, the effectiveness of tailoring strategies used is contingent upon the environment of the project. Environmental factors such as project size and team experience influence the challenges or problems faced by the project (e.g., evolving requirements, unfamiliar technology, etc.). Process tailoring involves the choice of appropriate tailoring strategies to address these challenges or problems [64]. With process tailoring strategies coded as problem–solution pairs, a process designer can easily match current problems with the preconditions of stored problem–solution pairs and retrieve appropriate tailoring strategies. For example, the following rule relates evolving requirements to a specific process step. Specifically, it suggests that when a project faces evolving requirements, the use of multiple iterations allows a team to deliver functionalities in successively refined versions so that the team can frequently obtain feedback from users and jointly discover and negotiate a set of requirements [53, 64]:

## If requirements are evolving, then adopt multiple iterations.

Prior research suggests that generalized knowledge can improve the problem-solving process in software process tailoring. A problem solver tends to relate task-related information to his or her own knowledge stored in memory and seeks rules to guide him or her in problem solving [12]. Bounded rationality theory suggests that a person’s effort in the process of searching for solutions is constrained by resources (such as knowledge) that are at his or her disposal [50]. Individuals who lack relevant knowledge can generate fewer or even inappropriate solutions, thus leading to poor performance. By supplementing the knowledge of decision makers involved in process tailoring, generalized knowledge can improve their performance.

When solving a problem, one needs to formulate the problem, evaluate alternatives, and follow the appropriate reasoning process in solving the problem [42]. Generalized knowledge, coded as problem–solution pairs, can help formulate the problem by suggesting the characteristics of the problem that needs to be solved, and possible tailoring strategies that can address these problems and, thus, matches the needs of software process tailoring tasks. By providing access to knowledge about tailoring strategies that are appropriate to the problem, generalized knowledge can help decision makers avoid potential mistakes and misjudgments, and thus improve effectiveness in process tailoring tasks. Therefore, we propose:

Hypothesis 1: Users with access to generalized knowledge support will perform better in terms of process tailoring effectiveness than those who do not have knowledge support.

The cognitive fit between generalized knowledge and tailoring tasks can also improve the efficiency of tailoring decisions by reducing the cognitive effort required to process information and generate solutions [14, 21]. Generalized knowledge can help decision makers quickly identify appropriate issues and select relevant tailoring strategies. In the absence of such knowledge support, decision makers have to either rely on their (often limited) prior experiences or seek help from outside resources such as coworkers or consultants or extant literature. These activities, if successful at all, require more time and effort [42]. Therefore, we argue that users with access to generalized knowledge will make decisions more efficiently.

Hypothesis 2: Users with access to generalized knowledge support will perform better in terms of process tailoring efficiency than those who do not have knowledge support.

## Contextualized Knowledge

Knowledge is embedded in not only semantic memory but also in episodic memory. Episodic memory records not only rules/generalized knowledge used in prior cases but also the context under which knowledge was created or applied [25, 30, 55]. Episodic memory consists of a set of cases or events from the past [31]. It plays an important role in analogical learning, an effective way to transfer knowledge and enhance learning [18]. In analogical learning, people solve a new problem by transferring knowledge from a learned situation to the new situation by mapping commonalities between the two [34]. Analogical learning is exemplified in the use of case studies in teaching where real-world cases are discussed and analyzed to improve knowledge and skills of students. It has been argued that learning occurs more quickly if knowledge is placed in appropriate contexts such as real-life experiences [25].

In this study, we argue that knowledge embedded in episodic memory is valuable in providing knowledge support in software process tailoring. Following Kolodner [30] and Ma [34], we refer to externalized episodic memory as contextualized knowledge. Prior research on case-based reasoning [30] and knowledge transfer [10] recognize that knowledge is situated in context and that it is important to understand the context of knowledge in knowledge sharing. Sabherwal and Beccerra-Fernandez [46] define context- and technology-specific knowledge as knowledge that is high in both technical knowledge and contextual knowledge. In the similar spirit, we extend this definition to accommodate other domain and contextual knowledge involved in software process tailoring such as managerial and process knowledge and refer to it as contextualized knowledge [30, 34], which has both high domain specificity and high contextual knowledge specificity. In software development, contextualized knowledge is especially important because the lack of contextualized knowledge may lead to poor system quality and project performance [45].

To provide cognitive fit with software process tailoring tasks and effectively improve tailoring task performance, contextualized knowledge needs to include three components. First, it needs to explicitly provide information cues that help users easily see the similarities and differences between a prior tailoring problem and the current one to facilitate knowledge identification [18]. Prior studies on software project management and process management show that software processes need to be tailored to suit various environmental factors that characterize a project and challenges that are faced by it [39, 64]. In other words, since these factors and challenges describe the problem involved in software process tailoring, they should be included in contextualized knowledge as information cues. The second key component of contextualized knowledge is strategic knowledge [14, 37] representing the tailoring strategies used.

The third component is causal knowledge [3]—that is, the rationale behind knowledge application. This component is concerned with facilitating knowledge transfer from a learned situation to a new problem. The critical steps in analogical learning include understanding how knowledge was used in prior cases and why, identifying transferable knowledge elements, and even modifying them before applying them to the new problem. Without a clear understanding of the rationale behind how a decision was made in the past, it is usually difficult for knowledge seekers to recognize knowledge transfer opportunities and act on them [57]. Further, when knowledge is presented independent of its rationale, possible different interpretations and incomplete understanding of the context pose problems in knowledge transfer. Therefore, prior research has called for “translating knowledge”; that is, making tacit knowledge explicit and transferring context-specific aspects of knowledge along with knowledge itself [10].

Drawing from these results, we identify the following knowledge components of contextualized knowledge that match the needs of software process tailoring tasks and therefore improve performance in software process tailoring:

•	 Problem: the process tailoring problem that needs to be solved (e.g., the choice of a specific mechanism for documenting project status) [18]

•	 Information cues: knowledge elements that describe the context of the problem (e.g., environmental factors and challenges considered) [18, 64]

•	 Strategic knowledge: knowledge about tailoring strategies [14, 37]

•	 Causal knowledge: the reasons and justifications behind the use of specific process tailoring strategies [3]

Based on the above discussion, we argue that contextualized knowledge provides the knowledge elements needed in tailoring a process along with the context in which these elements can be applied. It can help quickly identify transferable knowledge elements and facilitate knowledge application. Therefore, it can improve tailoring effectiveness and reduce cognitive effort.

Hypothesis 3: Users with access to contextualized knowledge support will perform better in terms of process tailoring effectiveness than those who do not have knowledge support.

Hypothesis 4: Users with access to contextualized knowledge support will perform better in terms of process tailoring efficiency than those who do not have knowledge support.

The Relative Effects of Generalized Versus Contextualized Knowledge on Process Tailoring

The codification of knowledge as generalized knowledge does not guarantee efficient dissemination and effective use [3]. Although generalized knowledge codifies best practices, the context and rationale underlying this knowledge are missing. Effective use of this knowledge requires knowledge users to understand it, reconstruct the context in which it can be applied, and eventually solve a problem using it. Thus, there is an implicit assumption in using generalized knowledge that the knowledge creator and the knowledge user share enough common knowledge ground. However, this assumption is often invalid, especially with novice knowledge users, who need knowledge support the most. Applying generalized knowledge without being aware of the appropriate context in which it may be used can be problematic since it may not be applicable in all contexts [3, 41, 55]. Inappropriate knowledge application will negatively influence decision quality and increase decision effort [34]. Therefore, we argue that generalized knowledge only provides limited support when compared to contextualized knowledge.

Contextualized knowledge, in contrast, provides adequate contextual information for knowledge users to not only understand it but also learn the context in which it was applied. Contextualized knowledge can positively affect effectiveness of process tailoring by improving understanding and minimizing any mismatch between the knowledge and the current context. It can also reduce the effort of knowledge users in their attempt to reconstruct the context in which it is applicable. Therefore, we propose:

Hypothesis 5: Users with access to contextualized knowledge support will perform better in terms of process tailoring effectiveness than those with generalized knowledge.

Hypothesis 6: Users with access to contextualized knowledge support will perform better in terms of process tailoring efficiency than those with generalized knowledge.

## Task Complexity and Knowledge Support

Cognitive fit theory indicates that knowledge support in software process tailoring needs to match the nature of tailoring tasks. Further, prior research also establishes that the degree of the impact of task support on task performance can be moderated by different tasks [56]. In this study, we focus on a critical dimension of software process tailoring tasks—task complexity. Task complexity has been established as an important factor that influences task performance [9, 54]. Complex tasks share a set of common characteristics. Wood [63] proposes a model that analyzes task complexity along three dimensions—component complexity, coordination complexity, and dynamic complexity. Component complexity of a task is a direct function of the number of distinct acts executed and the number of distinct information cues processed in the task. Coordinative complexity derives from the relationships between the inputs and the products of the task. Dynamic complexity refers to the uncertainty of environment. Campbell [9] concludes that four fundamental attributes characterize complex tasks—multiple paths, multiple outcomes, conflicting interdependence among paths, and uncertain or probabilistic linkage. Multiple paths refer to the fact that there may be more than one possible way to arrive at a desired outcome. Multiple outcomes refer to the multiple outputs produced by the task. Conflicting interdependence among paths exists if pursuing a desired outcome conflicts with the pursuit of another desired outcome. Information processing requirements will increase substantially if the solutions are uncertain, thereby increasing task complexity. Both Campbell [9] and Wood [63] show that complex tasks have more information cues to process, more alternatives/ paths, conflicting interdependency among decisions, and high uncertainty.

A software process tailoring task involves understanding the characteristics of a project, resources, schedule, development teams, technologies used, organizational environment, market, and so forth [39, 64]. These factors are information cues that are processed and used when tailoring a software process. Simple tasks typically have low information load and exhibit a relatively straightforward relationship between inputs (information cues) and outputs (possible solutions). The low level of interaction among knowledge elements and information cues needed for solving a simple tailoring problem demands low cognitive effort [38]. In such tasks, access to knowledge support has limited impact on users’ task performance.

On the other hand, complex tailoring problems involve a high level of interaction among knowledge elements and a large number of information cues needed for solving the task [38]. In a complex tailoring task, problems and issues that need to be considered can be overwhelming and hidden in the large amount of data. With multiple alternatives, conflicting choices, and complex interdependence among numerous information cues and decisions, it is very challenging for decision makers to quickly identify appropriate tailoring strategies. In such a circumstance, more guidance and knowledge support are needed. Therefore, access to knowledge support is likely to improve process tailoring performance significantly. Therefore, we propose:

Hypothesis 7: The positive effect of knowledge support (both generalized knowledge and contextualized knowledge) on process tailoring effectiveness will be greater when the process tailoring task is complex than when it is simple.

Hypothesis 8: The positive effect of knowledge support (both generalized knowledge and contextualized knowledge) on process tailoring efficiency will be greater when the process tailoring task is complex than when it is simple.

Figure 1 summarizes the research model.

## Research Methodology

We conducted an exp eriment to test the eight hypotheses presented above. Two types of knowledge support and two levels of task complexity were used to study their impact on process tailoring.

![](/api/attachments/ZMJ5DKVE/fulltext/images/b7f91cd006e47bb5fea51ac377e2f452b7ff87c8b4edfa2ed3ac7ca782807a56.jpg)  
Figure 1. The Research Model

## Experimental Design and Tasks

A 3 × 2 factorial experimental design was implemented. The independent variables are the types of knowledge support and the complexity of process tailoring tasks. Subjects were randomly assigned to three groups—a group without knowledge support, a group with generalized knowledge, and a group with contextualized knowledge. Each subject was given a case study on the development of a management information system and a “base process” that was used in this case. They were also given a new scenario for which a new process needs to be designed. The subjects were asked to tailor the base process for the new scenario. The control group received only the tailoring tasks. One experimental group was provided with the generalized knowledge that is applicable to each of the tailoring decisions described in the base process. Another experimental group received the contextualized knowledge used in the base process.

The case study and the base process were adopted from the RU P<sup>®</sup> framework. One task asks the participants to decide whether certain process steps are needed for the project. The other task asks the participants to plan iterations for the project. These represent typical software process tailoring tasks that are commonly observed in practice. The case and the base process were made available on a Web site. Where applicable, generalized or contextualized knowledge was provided through hyperlinks so that subjects could easily access relevant knowledge. Two experts were invited to review and evaluate the cases, tasks, and the knowledge provided. Modifications were made to this material based on their feedback.

In order to control the impact on tailoring efficiency caused by unfamiliarity with the format of the case and the base process, subjects were provided an additional task as training before they performed the experimental tasks. The order of the simple and complex tasks was randomized to control order effects. To conduct a manipulation check, after finishing the tasks, each subject was asked whether they used the knowledge provided to ensure the treatment was appropriately received. If the treatment was not properly received (i.e., knowledge was not used), the data were removed from the study. The cases, the base process, and the process tailoring tasks are described in Appendix B.

## Subjects

One hundred thirty-two subjects participated in the final experiment. They were students enrolled in the computer information system program at a large urban university in the United States. Participation in the experiment was voluntary. All of the subjects had attended a common set of three courses on software development and management. They all had relevant work experience or had received training in software development and software process. Table 2 profiles the subjects who participated in the final experiment. Data on demographics of the subjects in the study were collected to test for differences in past experience with software process development and tailoring.

## Operationalization of Constructs

The types of knowledge support and task complexity are categorical variables. Three groups with different types of knowledge support are used to operationalize the independent variable. Simple and complex tasks are designed to operationalize task complexity. Tailoring performance is measured by multiple items derived from relevant literature, employing seven-point Likert scales ranging from “strongly agree” to “strongly disagree.” Appendix C lists the items used for these constructs.

## Independent Variable: Knowledge Support

Both generalized knowledge and contextualized knowledge were developed and constructed by the researchers and a group of expert practitioners. Generalized knowledge was represented in the form of rules that identify how various factors influence process tailoring strategies [23].<sup>2</sup> Contextualized knowledge includes descriptions of the tailoring problems, information cues, strategic knowledge, and causal knowledge. As well-established in prior research in the field of software engineering, an argumentation model was used to represent contextual knowledge used in decision making [32, 44]. Argumentation models represent the reasoning process in a structured way, covering the four components of contextualized knowledge. In our study, we used the Issue Based Information Systems (IBIS) model [11], a popular argumentation model, to represent this knowledge.<sup>3</sup> The IBIS model consists of issues, positions, and arguments as its primitives. Positions represent resolutions to issues. Each issue can have many positions. Each position may have one or more arguments that either support that position or object to it. The model was used to represent all four aspects of contextualized knowledge.

## Moderating Variable: Task Complexity

Tasks used in the experiment were evaluated on the basis of the attributes of complex tasks discussed in Campbell [9]. The complexity of each task was evaluated by three independent experts. The selected tasks are representative of common tailoring tasks faced in IS practice. In the simple task, the subjects are asked to select activities in the requirement analysis phase for the new project (i.e., whether the specific activities should be performed for the new project; if they need to be performed, should the new project increase or decrease the time allocated to each activity). The complex task requires subjects to make decisions on an iteration plan for the new process. Appendix B provides details on how the complexity for both simple and complex tasks was computed.

<sub>scription</sub> <sub>of</sub> <sub>Subjects</sub> <sub>Participating</sub> <sub>in</sub> <sub>the</sub> E

<table><tr><td rowspan="2">Group/complexity</td><td rowspan="2">Number of subjects</td><td colspan="2">Ave Exp1 (months)</td><td colspan="2">Ave Exp2 (months)</td><td colspan="2">Ave Exp3 (months)</td></tr><tr><td>Mean</td><td>Standard deviation</td><td>Mean</td><td>Standard deviation</td><td>Mean</td><td>Standard deviation</td></tr><tr><td>No knowledge</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Simple</td><td>44</td><td>23.36</td><td>20.86</td><td>7.23</td><td>7.53</td><td>16.19</td><td>17.11</td></tr><tr><td>Complex</td><td>44</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Generalized knowledge</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Simple</td><td>44</td><td>27.07</td><td>22.30</td><td>8.30</td><td>10.77</td><td>14.84</td><td>12.64</td></tr><tr><td>Complex</td><td>44</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Contextualized knowledge</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Simple</td><td>44</td><td>30.07</td><td>25.01</td><td>12.14</td><td>14.33</td><td>20.34</td><td>11.97</td></tr><tr><td>Complex</td><td>44</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="8">Notes: Ave Exp1: Average work experience in system development. Ave Exp2: Average work experience in software project management. Ave Exp3: Average work experience in software process. One-tailed tests.</td></tr></table>

## Dependent Variable: Tailoring Performance

Effectiveness of software process tailoring is defined as the quality of tailoring decisions [14, 42]. Potential answers are provided as choices for each task. Subjects were required to provide justifications for their answers. Prior research has shown that in order to effectively measure problem-solving quality, it is necessary to examine whether decision makers follow appropriate problem-solving procedures such as considering relevant issues, gathering complete information, and applying correct knowledge [15]. These justifications show how the subjects reached their answers and demonstrate work procedures. They can be used to effectively measure decision quality [15]. In our study, effectiveness in process tailoring is measured by the soundness of solutions, appropriateness of justifications, and completeness of justifications. Efficiency of process tailoring is defined as effort needed for process tailoring [7, 60]. Efficiency is measured by collecting data on how much effort was needed in completing each task [7].

## Instrument Validation

A pretest was conducted to ensure the content validity of the measures. In the pretest, the instruments were subjected to a qualitative testing of validity. Two experts were invited to evaluate the tasks and the instruments. On the basis of their feedback, the scenarios and the instruments were changed slightly to improve clarity. After the pretest, a pilot study was conducted. Forty subjects participated in the pilot study. Factor analysis was performed to assess the validity of the instruments. Based on the results and feedback obtained in the pilot study, the instruments were slightly modified before the final experiment was executed.

One hundred thirty-two subjects participated in the final experiment. The results from the factor analysis performed to assess the validity of instruments are shown in Appendix C. All indicators have clean loadings on their factors. All items have loadings above the cutoff value of 0.7 suggested in the literature [22]. Cronbach’s alphas are all well above the recommended value of 0.75 [22].

The effectiveness of process tailoring is measured by evaluating the quality of the answers. In order to remove researcher bias, two independent experts graded the responses. The correct answers and grading criteria were discussed among the researchers and the two raters. To ensure measurement reliability, interrater reliability was examined. The correlations of each effectiveness item graded by two raters were examined [49]. The correlations of items ranged from 0.81 to 0.91. The high correlation indicates that the measurements are reliable. The average ratings for each effectiveness indicator were used in the final data analysis.

## Results

The data on three covariates were collected in a survey at the end of the experiment. They are the subject’s experience in software development, experience in project management, and experience in software process. Table 3 shows the results of the multiple analysis of covariance (MANCOVA) test that was used to test the influences of the three covariates and remove the variation in the dependent variables associated with these covariates. The performance of process tailoring (effectiveness and efficiency) is significant for the main effect of knowledge support and the interaction effect between knowledge support and complexity $( p < 0 . 0 1$ and $p < 0 . 0 1$ , respectively). The observed power for the two observations is quite high, too—that is, 1.000 and 0.796, respectively, satisfying the recommended level of 0.8 [22]. In the following sections, each dependent variable is further examined.

Table 4 shows the tests of between-subject effects of the two dependent variables. Removing the variation in the dependent variables associated with these covariates, the results of MANCOVA indicate that the main effects of knowledge support are significant on the two dependent variables—that is, tailoring effectiveness $( p < 0 . 0 1 )$ ) and tailoring efficiency $( p < 0 . 0 1 )$ . However, the interaction effect of knowledge support and task complexity is only significant for tailoring effectiveness $( p < 0 . 0 1 )$

To further examine the differences between each group, post hoc tests were conducted. Table 5 shows the results of post hoc multiple comparison tests described below.

## Process Tailoring Effectiveness

Multiple comparisons show that the tailoring effectiveness of the group with contextualized knowledge is significantly better than that of the other two groups $( p < 0 . 0 1 )$ . However, the difference between the group with no knowledge and the group with generalized knowledge is not significant. The results verify the positive effects of contextualized knowledge, but do not support a similar effect with generalized knowledge.

Figure 2 shows the means for effectiveness for both the simple and complex tasks for each group, demonstrating the interaction effects of various types of knowledge support on process tailoring. When using contextualized knowledge, the improvement in tailoring effectiveness is more dramatic with complex tasks than with simple tasks. It suggests that the positive effect of contextualized knowledge on process tailoring effectiveness is greater when the process tailoring task is complex than when it is simple. However, the interaction effect of generalized knowledge with task complexity is not supported.

<sub>e</sub> <sub>3.</sub> M<sup>ultivariate</sup> <sup>T</sup>

<table><tr><td>Effect</td><td>Value</td><td>F</td><td>Hypothesis df</td><td>Error df</td><td>Significance</td><td>Observed power</td></tr><tr><td>Intercept</td><td>0.94</td><td>2,108.47</td><td>2.00</td><td>254.00</td><td>0.00*</td><td>1.00</td></tr><tr><td>Exp1</td><td>0.01</td><td>1.41</td><td>2.00</td><td>254.00</td><td>0.13</td><td>0.13</td></tr><tr><td>Exp2</td><td>0.00</td><td>0.37</td><td>2.00</td><td>254.00</td><td>0.35</td><td>0.03</td></tr><tr><td>Exp3</td><td>0.02</td><td>2.40</td><td>2.00</td><td>254.00</td><td>0.06</td><td>0.25</td></tr><tr><td>Knowledge support</td><td>0.46</td><td>38.35</td><td>4.00</td><td>510.00</td><td>0.00*</td><td>1.00</td></tr><tr><td>Complexity</td><td>0.33</td><td>63.48</td><td>2.00</td><td>254.00</td><td>0.00*</td><td>1.00</td></tr><tr><td>Group * complexity</td><td>0.06</td><td>3.67</td><td>4.00</td><td>510.00</td><td>0.01*</td><td>0.80</td></tr><tr><td colspan="7">Notes: EXP1: experience in system development. EXP2: experience in software project management. EXP3: experience in software process. * Significant at the 0.01 level (one-tailed test).</td></tr></table>

<table><tr><td>Source</td><td>Dependent variable</td><td>Type III sum of squares</td><td>Degrees of freedom</td><td>Mean square</td><td>F</td><td>Significance</td><td>Observed power</td></tr><tr><td rowspan="2">Corrected model</td><td>Effectiveness</td><td> $522.42^1$ </td><td>8</td><td>65.30</td><td>38.590</td><td>0.00*</td><td>1.00</td></tr><tr><td>Efficiency</td><td> $282.72^2$ </td><td>8</td><td>35.34</td><td>19.60</td><td>0.00*</td><td>1.00</td></tr><tr><td rowspan="2">exp1</td><td>Effectiveness</td><td>2.56</td><td>1</td><td>2.56</td><td>1.51</td><td>0.11</td><td>0.09</td></tr><tr><td>Efficiency</td><td>4.06</td><td>1</td><td>4.06</td><td>2.25</td><td>0.07</td><td>0.14</td></tr><tr><td rowspan="2">exp2</td><td>Effectiveness</td><td>1.26</td><td>1</td><td>1.26</td><td>0.75</td><td>0.20</td><td>0.04</td></tr><tr><td>Efficiency</td><td>0.20</td><td>1</td><td>0.20</td><td>0.11</td><td>0.37</td><td>0.01</td></tr><tr><td rowspan="2">exp3</td><td>Effectiveness</td><td>7.94</td><td>1</td><td>7.94</td><td>4.69</td><td>0.02</td><td>0.34</td></tr><tr><td>Efficiency</td><td>2.02</td><td>1</td><td>2.02</td><td>1.12</td><td>0.15</td><td>0.06</td></tr><tr><td rowspan="2">Group</td><td>Effectiveness</td><td>304.97</td><td>2</td><td>152.48</td><td>90.11</td><td>0.00*</td><td>1.00</td></tr><tr><td>Efficiency</td><td>169.26</td><td>2</td><td>84.63</td><td>46.94</td><td>0.00*</td><td>1.00</td></tr><tr><td rowspan="2">Complexity</td><td>Effectiveness</td><td>190.49</td><td>1</td><td>190.49</td><td>112.56</td><td>0.00*</td><td>1.00</td></tr><tr><td>Efficiency</td><td>94.28</td><td>1</td><td>94.28</td><td>52.30</td><td>0.00*</td><td>1.00</td></tr><tr><td rowspan="2">Group * complexity</td><td>Effectiveness</td><td>22.26</td><td>2</td><td>11.13</td><td>6.58</td><td>0.00*</td><td>0.76</td></tr><tr><td>Efficiency</td><td>1.69</td><td>2</td><td>0.84</td><td>0.47</td><td>0.32</td><td>0.04</td></tr><tr><td colspan="8">Notes:  $^1$ R-squared of effectiveness = 0.55 (adjusted R-squared = 0.53).  $^2$ R-squared of efficiency = 0.38 (adjusted R-squared = 0.36). * Significant at the 0.01 level (one-tailed test).</td></tr></table>

<sub>The</sub> <sub>Tests</sub> <sub>of</sub> <sub>Bet</sub>w<sup>een-Subject</sup>

<table><tr><td>Dependent variable</td><td>(I) Group</td><td>(J) Group</td><td>Mean difference (I-J)</td><td>Standard error</td><td>Significance</td></tr><tr><td rowspan="6">Effectiveness</td><td>2</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>0.48</td><td>0.28</td><td>0.12</td><td></td></tr><tr><td></td><td>3</td><td>-1.98</td><td>0.20</td><td>0.00*</td></tr><tr><td>3</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>2.47</td><td>0.23</td><td>0.00*</td><td></td></tr><tr><td></td><td>2</td><td>1.96</td><td>0.20</td><td>0.00*</td></tr><tr><td rowspan="6">Efficiency</td><td>2</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>-0.76</td><td>0.20</td><td>0.00*</td><td></td></tr><tr><td></td><td>3</td><td>1.26</td><td>0.22</td><td>0.00*</td></tr><tr><td>3</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>-2.01</td><td>0.24</td><td>0.00*</td><td></td></tr><tr><td></td><td>2</td><td>-1.26</td><td>0.22</td><td>0.00*</td></tr><tr><td colspan="6">Notes: Group 1: No knowledge. Group 2: Generalized knowledge. Group 3: Contextualized knowledge. * Significant at the 0.01 level (one-tailed test).</td></tr></table>

<sub>5.</sub> M<sup>ultiple</sup> <sup>Compari</sup>

![](/api/attachments/ZMJ5DKVE/fulltext/images/ccd802ab45eed45e6fc3ea9acddf5d2fdde73568717ba7002f1c20d9f6cacd39.jpg)  
Figure 2. Process Tailoring Effectiveness for Different Treatments

## Process Tailoring Efficiency

The post hoc tests also examined the differences in tailoring efficiency among the groups. Table 5 shows the effects of knowledge support on tailoring efficiency. The results indicate that the presence of different types of knowledge support influences tailoring efficiency $( p < 0 . 0 1 )$ . Subjects with contextualized knowledge were more efficient than the other two groups. Subjects with generalized knowledge support also outperformed those with no knowledge support in terms of tailoring efficiency.

## Task Order Effect

Each participant finished two tasks, a simple one and a complex one. To remove task order effect and repeated measures effect, the order of the tasks was randomized. The effect of task order was further examined. The main effect and interaction effects of task order in multivariate analysis of variance (MANOVA) were found to be not significant. The test results confirm that there is no task order effect in the study. Appendix D lists the results of the test that examines order effect.

## Understanding the Role of Knowledge Support Through Protocol Analysis

analysis with developers experienced in process tailoring. In this study, the participants performed the same tailoring tasks that were used in the experimental study.

Protocol analysis uses data obtained by recording verbalized responses of subjects to instructions. The participants are asked to perform specific tasks and are requested to think aloud. The process of verbalizing the thought process reveals assumptions and problems that the participants face while performing the given task [16]. Verbal protocol analysis has been widely used, especially to study problem solving [35] and system development tasks [26]. In our study, we use protocol analysis to examine the cognitive processes followed by the participants engaged in process tailoring activities. The study design, subjects, experimental procedures, and analysis procedures are described in Appendix E. The detailed presentation of the study is beyond the scope of this paper, but the primary results are described in this section.

## Differences in Efficiency

While performing process tailoring tasks, the subjects with no knowledge took longer (averaging 75 minutes) than the group with generalized (averaging 60 minutes), which in turn took more time compared to the group with contextualized knowledge (averaging 45 minutes). The self-reported efforts also conform to this observation. A closer examination of how the subjects in each group spent their time revealed interesting differences. Even though all of the groups spent a similar amount of effort in understanding the tailoring tasks, their problem-solving behavior differed significantly when looking for potential tailoring strategies. Subjects with no access to knowledge had to rely on their past experience to identify tailoring strategies. When solving the simple task, they finished the task relatively faster and were more confident of their solutions. However, when faced with complex tailoring tasks, they seemed overwhelmed by the multiple issues that had to be considered and the potential conflicts among the alternative tailoring strategies that appeared relevant. The subjects spent much of their time and effort in evaluating trade-offs in finalizing the solution. By referring to generalized knowledge that was represented as problem–solution pairs, the group with generalized knowledge could quickly focus on the key problems involved in the tailoring tasks, and select generic tailoring strategies as suggested by generalized knowledge. However, they had to spend much of their effort evaluating the applicability of the various generic rules and figure out how to use these rules in the tailoring tasks at hand. In this process, they often relied on their own prior experiences to complement the generalized knowledge. This in itself was a challenging activity to these subjects. In contrast, the group with access to contextualized knowledge was able to more easily and quickly identify tailoring strategies that are applicable in the problem context. Although they had to spend a little more time in reviewing the more detailed contextualized knowledge, they could quickly identify the similarities and differences between the tailoring task at hand and the available knowledge. This helped the subjects identify the appropriate tailoring strategies and apply them to the specific problems. The above observations help understand the differences in the relative effort spent by the three groups in the tailoring tasks.

## Difference in Effectiveness

The observed differences in the problem-solving behavior of the subjects also helps explain the differences in the quality of the solutions developed by them. Because the subjects with no access to knowledge had to rely on their own experiences in performing the tailoring task, their solutions were not as effective as those produced by subjects with contextualized knowledge. The problem-solving behavior of subjects with access to generalized knowledge helped understand the somewhat surprising finding from the experimental study that their solutions were not significantly more effective when compared to those with no access to knowledge. As noted earlier, these subjects also had to rely on their judgment rather than concrete evidence to complement the generalized knowledge in evaluating generalized rules, dealing with conflicts among solutions suggested by different rules, and applying rules to the tasks at hand. The protocol analysis study suggests that this is indeed challenging and, therefore, even with access to generalized knowledge, the performance of the subjects does not improve significantly. In contrast, subjects with access to contextualized knowledge could identify appropriate tailoring strategies and repercussions of their decisions aided by the fine-grained descriptions of issues, alternate solutions, and arguments for and against each of these alternatives that are part of this knowledge. Therefore, developers with contextualized knowledge are able to perform the tasks more completely and accurately.

## Role of Complexity

The positive impact of contextualized knowledge was more pronounced in the case of complex tasks. When performing the complex task, the participants with access to contextualized knowledge demonstrated a more thorough understanding compared to the other two groups, thus producing far superior solutions. In contrast, the participants in the other two groups seemed overwhelmed by the amount of information cues, choices, and their interactions. Subjects with access to generalized knowledge faced difficulties in establishing the applicability of generalized rules. When performing the complex task, the subjects with contextualized knowledge spent a lot of effort in carefully reviewing the provided knowledge, comparing two cases, and assessing various alternatives, whereas the subjects with generalized knowledge had to rely on their past experience in these activities. This is a plausible reason for the insignificant interaction effect of knowledge support and complexity on efficiency.

In summary, the protocol analysis study confirms the findings from the experimental study. In addition, it provides additional insights on the roles of generalized and contextualized knowledge in process tailoring tasks.

## Discussions and Conclusions

Building on cognitive fit theory, we empirically compared the impact of the two types of knowledge (i.e., generalized knowledge and contextualized knowledge) in support ing software process tailoring. Table 6 summarizes the results of the experiment.

Table 6. Findings of the Experiment

<table><tr><td>Hypotheses</td><td>Results</td></tr><tr><td>H1: Generalized knowledge versus no knowledge support → tailoring effectiveness</td><td>Not supported</td></tr><tr><td>H2: Generalized knowledge versus no knowledge support → tailoring efficiency</td><td>Supported</td></tr><tr><td>H3: Contextualized knowledge versus no knowledge support → tailoring effectiveness</td><td>Supported</td></tr><tr><td>H4: Contextualized knowledge versus no knowledge support → tailoring efficiency</td><td>Supported</td></tr><tr><td>H5: Contextualized knowledge versus generalized knowledge → tailoring effectiveness</td><td>Supported</td></tr><tr><td>H6: Contextualized knowledge versus generalized knowledge → tailoring efficiency</td><td>Supported</td></tr><tr><td>H7: Moderating effect of task complexity on tailoring effectiveness</td><td>Contextualized knowledge effect supported</td></tr><tr><td>H8: Moderating effect of task complexity on tailoring efficiency</td><td>Not supported</td></tr></table>

## Discussion

The results show that contextualized knowledge support can significantly improve process tailoring effectiveness. At the same time, both generalized knowledge and contextualized knowledge can reduce decision-making effort. These findings confirm prior research that knowledge support can increase performance and positively affect users’ performance [14, 21]. These findings are also supported by the observations in the protocol analysis.

An important finding of this study is the differences in the impact of two types of explicit knowledge in software process tailoring. The results suggest that contextualized knowledge represents a higher level of knowledge support than generalized knowledge. It confirms that the presence of contextualized knowledge may lead to more learning and that generalized knowledge is limited to providing help when solving ill-structured, complex tailoring tasks. The results are consistent with prior research that proposes that contextualized knowledge is more important early in the learning process and it encourages users in linking information to their knowledge from past experiences [25]. The findings suggest that although contextualized knowledge is more expensive to obtain and requires more information processing, this increased need for processing is well justified because it can expand the bounded rationality of decision makers. On the other hand, the help provided by generalized knowledge is relatively limited when compared with contextualized knowledge. The effort needed to access this knowledge is lower than with contextualized knowledge due to its simplicity. However, the effort needed for knowledge application is relatively high when compared with contextualized knowledge. The results of our study indicate that contextualized knowledge is more effective than generalized knowledge in supporting process tailoring by helping reduce the complexity of problem solving in process tailoring.

The interaction effect of task complexity and contextualized knowledge support on process tailoring effectiveness shows that contextualized knowledge is extremely important when performing more complex tasks that usually demand more effort. It confirms the cognitive fit theory in the context of knowledge support for process tailoring, that is, knowledge support for process tailoring needs to match the complexity of tailoring tasks.

The interaction effect is not found for generalized knowledge. It may be due to the fact that the simplicity of generalized knowledge provides limited help in complex tasks. The interaction effect is not as strong as that of contextualized knowledge. The interaction effect on efficiency is not significant. The observations in the protocol analysis indicate that decision makers need to spend much of their effort in absorbing and applying knowledge, and evaluating potential solutions. However, because the statistical power of these results on the moderating effect is fairly low (0.037 for efficiency), further studies are needed.

## Implications for Research

## Implications for Cognitive Fit Theory in IS Literature

The study makes several novel contributions to the IS literature. The study extends cognitive fit theory to the context of knowledge support. Although this theory has been used in other contexts (see Table 1), our study is novel in the use of this theory to investigate cognitive fit in knowledge support in the context of software process tailoring. In our study, we propose two types of knowledge that fit software process tailoring tasks to improve task performance. We also extend cognitive fit theory to show that the degree of influence of the two types of knowledge support on process tailoring can also be moderated by different characteristics of tailoring tasks. Our results show that the presence of contextualized knowledge is important when performing complex tailoring tasks. Since task complexity is a significant consideration in the development of knowledge support tools, this finding highlights the need to consider cognitive fit in their development.

## Implications for Knowledge Management in Information

## Systems Development

This study also contributes to the literature on the role of knowledge management in information systems development (ISD). The important role of knowledge in achieving success in ISD is widely recognized. For example, prior research has investigated knowledge management at the team level focusing on interpersonal interaction and coordination [17, 58]. Recent research calls for treating each ISD effort as an experiment from which information technology (IT) professionals can learn [33]. However, theoretically and empirically grounded research on the specific types of knowledge gained from prior experience that will enhance performance is scant [5, 33]. Although recent studies recognize that knowledge is situated in context and that to overcome stickiness of knowledge, it is important to capture and share the context, especially across users and domain boundaries [10, 45], research on specific mechanisms to achieve this goal has received scant attention. Our study represents the first effort in studying knowledge management in the context of a knowledge intensive and critical task—namely, software process tailoring. It complements prior research by investigating how externalized knowledge, especially generalized and contextualized knowledge, improves performance in software process tailoring.

## Implications for Software Project and Process Management

Performance of a software project depends considerably on the quality of software process [40]. Prior research [40] argues that effectively managing system development project needs two distinct modes of control—that is, standardization and decentralized control. The former emphasizes a priori specification of process standards while the latter permits team members to make decisions with respect to the adaption of a process to the local context. While the important role of knowledge from prior experience has been recognized and efforts have been made to study software process management from a knowledge transfer perspective [52], much of the prior research on software process management and improvement mainly takes a “macro” view that focuses on improving or managing software processes at the organization level. However, the dynamic nature of business environment and emergent nature of a software process require project team members to make numerous “micro”-level tailoring decisions as the project unfolds. The quality of tailoring decisions made by these individuals affects the quality of the process and therefore project outcomes. Our study complements the literature on software process management, especially software process tailoring, by taking a “micro” approach at the individual level. Our study establishes that two types of knowledge (contextualized and general) can enhance individual decision-making process in software process tailoring, thus improving the quality of the software process.

In the context of project management, the current literature provides little guidance on the role of critical inputs such as prior knowledge. Although our study mainly focuses on a specific project management activity—software process tailoring—the findings from our study can be extended to improve the effectiveness of strategies used in other software project management activities such as project control and estimation.

## Implications for Practice

The results can be used to inform the development of guidelines for process tailoring by practitioners. It provides suggestions on the types of knowledge that need to be acquired and how it may be represented in knowledge repositories. It shows that although constructing contextualized knowledge is time-consuming, it is valuable especially when performing complex tasks. Software development organizations can significantly improve tailoring effectiveness and efficiency by creating repositories of contextualized knowledge.

## Limitations and Future Work

The study has two limitations that may pose challenges to external validity. They are the use of an experiment rather than a field study and the use of students as subjects. First, the experimental tasks and the cases used in the experiment were developed from documentation on RU P<sup>®</sup>, which is a popular process framework commonly used in the industry. Although the use of experimental settings may lack the rich context of a real-life software project environment, past research has demonstrated the appropriateness of using experimental settings for studying decision making in software project management tasks [1, 47, 60].

Second, the use of students instead of professionals also poses challenges to the generalizability of the results. The participants are students who majored in Computer Information Systems at a U.S. university. Most of the participants have work experience in software development, project management, and process management. Their average experience in software development is 27 months, average experience in project management is nine months, and average experience in software process management is 17 months. They represent novices in software process tailoring who need knowledge support the most. However, we also note that the concept of tailorable processes is rather new in IS practice and a majority of practitioners have very limited experience in process tailoring. Further, using students in a controlled setting can ensure homogeneous responses, which are critical in theory testing [8], in contrast to field settings, which can be confounded by unique, unmeasured contextual factors [6]. Previous studies also demonstrate that there is little difference between using students and using professionals in decision-making situations, especially in studies on the execution of cognitive tasks [6].

However, the generalizability of our study is constrained by the use of controlled settings and the participants, who may be treated as novices in process tailoring. The results may not generalize to experts in process tailoring. Future research involving professionals is encouraged to investigate the differences, if any, between these two groups. It should be noted, however, that even among users of popular frameworks such as RU P<sup>®</sup>, process tailoring experience is difficult to obtain and, therefore, the results generalize to a significant proportion of software development professionals. The interaction effect of various knowledge supports and task complexity on tailoring efficiency was not found to be significant in this study. More research is needed to further explore this performance construct. As a knowledge-intensive task, software process tailoring involves a great deal of interactions among team members and requires effective knowledge integration among team members. Therefore, the examination of the dynamic aspects of knowledge transfer and integration and their impact on project performance requires further examination. Team dynamics and knowledge integration in software process tailoring are interesting topics that deserve careful study in future research.

## Notes

1. In this paper, consistent with the current literature, we use the term software process to refer to software development process.

2. An example of generalized knowledge is provided in Appendix A.

3. An example of contextualized knowledge is provided in Appendix A.

## References

1. Abdel-Hamid, T.K.; Sengupta, K.; and Swett, C. The impact of goals on software project management: An experimental investigation. MIS Quarterly, 23, 4 (1999), 531–555.

2. Agarwal, R.; Sinha, A.P.; and Tanniru, M.R. Cognitive fit in requirements modeling: A study of object and process methodologies. Journal of Management Information Systems, 13, 2 (Fall 1996), 137–162.

3. Alavi, M., and Leidner, D.E. Knowledge management and knowledge management systems: Conceptual foundations and research issues. MIS Quarterly, 25, 1 (2001), 107–136.

4. Barki, H.; Rivard, S.; and Talbot, J. An integrative contingency model of software project risk management. Journal of Management Information Systems, 17, 4 (Spring 2001), 37–69.

5. Basili, V.R.; Caldiera, G.; and Rombach, D.H. The experience factory. In J.J. Marciniak (ed.), Encyclopedia of Software Engineering, vol. 1. New York: John Wiley, 1994, pp. 469–476.

6. Bettenhausen, K.L. Five years of group research: What we have learned and what needs to be addressed. Journal of Management, 17, 2 (1991), 345–381.

7. Bettman, J.R.; Johnson, E.J.; and Payne, J.W. A componential analysis of cognitive effort in choice. Organizational Behavior and Human Decision Processes, 45, 1 (1990), 111–139.

8. Calder, B.J.; Phillips, L.W.; and Tybout, A.M. Designing research for application. Journal of Consumer Research, 8, 2 (1981), 187–207.

9. Campbell, D.J. Task complexity: A review and analysis. Academy of Management Review, 13, 1 (1988), 40–52.

10. Carlile, P.R. Transferring, translating, and transforming: An integrative framework for managing knowledge across boundaries. Organization Science, 15, 5 (2004), 555–568.

11. Conklin, J., and Begeman, M.L. gIBIS: A hypertext tool for exploratory policy discussion. ACM Transactions on Office Information Systems, 6, 4 (1988), 303–331.

12. d’Apollonia, S.T.; Charles, E.S.; and Boyd, G.M. Acquisition of complex systemic thinking: Mental models of evolution. Educational Research and Evaluation, 10, 4–6 (2004), 499–521.

13. Dennis, A.R., and Carte, T.A. Using geographical information systems for decision making: Extending cognitive fit theory to map-based presentations. Information Systems Research, 9, 2 (1998), 194–203.

14. Dhaliwal, J.S., and Benbasat, I. The use and effects of knowledge-based system explanations: Theoretical foundations and a framework for empirical evaluation. Information Systems Research, 7, 3 (1996), 342–362.

15. Ebel, R.L., and Frisbie, D.A. Essentials of Educational Measurement, 5th ed. Englewood Cliffs, NJ: Prentice Hall, 1991.

16. Ericsson, A., and Simon, H. Protocol Analysis: Using Verbal Reports as Data. Cambridge, MA: MIT Press, 1993.

17. Espinosa, J.A.; Slaughter, S.A.; Kraut, R.E.; and Herbsleb, J.D. Team knowledge and coordination in geographically distributed software development. Journal of Management Information Systems, 24, 1 (Summer 2007), 135–169.

18. Gick, M.L., and Holyoak, K.J. Analogical problem solving. Cognitive Psychology, 12, 3 (1980), 306–355.

19. Ginsberg, M.P., and Quinn, L.H. Process tailoring and the software capability maturity model. Technical Report CMU/SEI-94-TR-024, Software Engineering Institute, Pittsburgh, PA, November 1995.

20. Gray, P.H., and Durcikova, A. The role of knowledge repositories in technical support environments: Speed versus learning in user performance. Journal of Management Information Systems, 22, 3 (Winter 2005–6) 159–190.

21. Gregor, S., and Benbasat, I. Explanations from intelligent systems: Theoretical foundations and implications for practice. MIS Quarterly, 23, 4 (1999), 497–530.

22. Hair, J.F.; Anderson, R.E.; Tatham, R.L.; and Black, W.C. Multivariate Data Analysis, 5th ed. Upper Saddle River, NJ: Prentice Hall, 1998.

23. Henninger, S. An environment for reusing software processes. In Proceedings of Fifth International Conference on Software Reuse. Las Alamitos, CA: IEEE Computer Society, 1998, pp. 103–112.

24. Henninger, S. Turning development standards into repositories of experiences. Software Process: Improvement and Practice, 6, 3 (2001), 141–155.

25. Herbert, D.M., and Burt, J.S. What do students remember? Episodic memory and the development of schematization. Applied Cognitive Psychology, 18, 1 (2004), 77–88.

26. Hughes, J., and Parkes, S. Trends in the use of verbal protocol analysis in software engineering research. Behavior and Information Technology, 22, 2 (2003), 127–140.

27. IEEE/EIA. Industry implementation of international standard ISO/IEC 12207.0:1995, IEEE/EIA, New York, 1998.

28. Jacobson, I.; Booch, G.; and Rumbaugh, J. The Unified Software Development Process. Boston: Addison-Wesley Professional, 1999.

29. Khatri, V.; Vessey, I.; Ramesh, P.C.; and Park, S.-J. Understanding conceptual schemas: Exploring the role of application and IS domain knowledge. Information Systems Research, 17, 1 (2006), 81–99.

30. Kolodner, J.L. Case-Based Reasoning. San Mateo, CA: Morgan Kaufmann, 1993.

31. Kolodner, J.L.; Owensby, J.N.; and Guzdial, M. Case-based learning aids. In H. Jonassen (ed.), Handbook of Research on Educational Communications and Technology: A Project of the Association for Educational Communications and Technology. Mahwah, NJ: Lawrence Erlbaum, 2003, pp. 829–861.

32. Lee, J., and Lai, K.-Y. What’s in design rationale? In T.P. Moran and J.M. Carroll (eds.), Design Rationale: Concepts, Techniques, and Use. Mahwah, NJ: Lawrence Erlbaum, 1996, pp. 21–51.

33. Lyytinen, K., and Robey, D. Learning failure in information systems development. Information Systems Journal, 9, 2 (1999), 85–101.

34. Ma, Y. Exploring faculty perceptions of a case library as an online teaching resource. Ph.D. dissertation, College of Education, Georgia State University, Atlanta, 2005.

35. Mao, J.-Y., and Benbasat, I. The use of explanations in knowledge-based systems: Cognitive perspectives and a process-tracing analysis. Journal of Management Information Systems, 17, 2 (Fall 2000), 153–179.

36. McIntosh, M. Content management using the Rational Unified Process<sup>®</sup>. White Paper, Rational Software, Cupertino, CA, 2002.

37. Mennecke, B.E.; Crossland, M.D.; and Killingsworth, B.L. Is a map more than a picture? The role of SDSS technology, subject characteristics, and problem complexity on map reading and problem solving. MIS Quarterly, 24, 4 (2000), 601–629.

38. Nickerson, J.A., and Zenger, T.R. A knowledge-based theory of the firm—The problemsolving perspective. Organization Science, 15, 6 (2004), 617–632.

39. Nidumolu, S.R. A comparison of the structural contingency and risk-based perspectives on coordination in software development projects. Journal of Management Information Systems, 13, 2 (Fall 1996), 77–113.

40. Nidumolu, S.R., and Subramani, M.R. The matrix of control: Combining process and structure approaches to managing software development. Journal of Management Information Systems, 20, 3 (Winter 2002–3), 159–196.

41. Nonaka, I. A dynamic theory of organizational knowledge creation. Organization Science, 5, 1 (1994), 14–37.

42. Parikh, M.; Fazlollahi, B.; and Verma, S. The effectiveness of decisional guidance: An empirical evaluation. Decision Sciences, 32, 2 (2001), 303–331.

43. Pollice, G. Using the Rational Unified Process for small projects: Expanding upon eXtreme Programming. White Paper, Rational Software, Cupertino, CA, 2001.

44. Ramesh, B., and Jarke, M. Toward reference models for requirements traceability. IEEE Transactions on Software Engineering, 27, 1 (2001), 58–93.

45. Robillard, P.N. The role of knowledge in software development. Communications of the ACM, 42, 1 (1999), 87–92.

46. Sabherwal, R., and Becerra-Fernandez, I. Integrating specific knowledge: Insights from the Kennedy Space Center. IEEE Transactions on Engineering Management, 52, 3 (2005), 301–315.

47. Sengupta, K.; Abdel-Hamid, T.K.; and Bosley, M. Coping with staffing delays in software project management: An experimental investigation. IEEE Transactions on Systems, Man, and Cybernetics—Part A: Systems and Humans, 29, 1 (1999), 77–91.

48. Shaft, T., and Vessey, I. The role of cognitive fit in the relationship between software comprehension and modification. MIS Quarterly, 30, 1 (2006), 29–55.

49. Shrout, P.E., and Fleiss, J.L. Intraclass correlations: Uses in assessing rater reliability. Psychological Bulletin, 86, 2 (1979), 420–428.

50. Simon, H.A. A behavioral model of rational choice. Quarterly Journal of Economics, 69, 1 (1955), 99–118.

51. Sinha, A.P., and Vessey, I. Cognitive fit: An empirical study of recursion and iteration. IEEE Transactions on Software Engineering, 18, 5 (1992), 368–379.

52. Slaughter, S.A., and Kirsch, L.J. The effectiveness of knowledge transfer portfolios in software process improvement: A field study. Information Systems Research, 17, 3 (2006), 301–320.

53. Smith, R.P., and Eppinger, S.D. Identifying controlling features of engineering design iteration. Management Science, 43, 3 (1997), 276–293.

54. Speier, C., and Morris, M.G. The influence of query interface design on decision-making performance. MIS Quarterly, 27, 3 (2003), 397–423.

55. Stein, E.W., and Zwass, V. Actualizing organizational memory with information systems. Information Systems Research, 6, 2 (1995), 85–117.

56. Suh, K.-S., and Lee, Y.E. The effects of virtual reality on consumer learning: An empirical investigation. MIS Quarterly, 29, 4 (2005), 673–697.

57. Szulanski, G. The process of knowledge transfer: A diachronic analysis of stickiness. Organizational Behavior and Human Decision Processes, 82, 1 (2000), 9–27.

58. Tiwana, A., and McLean, E.R. Expertise integration and creativity in information systems development. Journal of Management Information Systems, 22, 1 (Summer 2005), 13–43.

59. Todd, P., and Benbasat, I. Process tracing methods in decision support systems. MIS Quarterly, 11, 4 (1987), 493–512.

60. Todd, P., and Benbasat, I. Evaluating the impact of DSS, cognitive effort, and incentives on strategy selection. Information Systems Research, 10, 4 (1999), 356–374.

61. Vessey, I. Cognitive fit: A theory-based analysis of the graphs versus table literature. Decision Sciences, 22, 2 (1991), 219–230.

62. Vessey, I., and Galletta, D. Cognitive fit: An empirical study of information acquisition. Information Systems Research, 2, 1 (1991), 63–84.

63. Wood, R.E. Task complexity: Definition of a construct. Organizational Behavior and Human Decision Processes, 37, 1 (1986), 60–82.

64. Xu, P., and Ramesh, B. Software process tailoring: An empirical investigation. Journal of Management Information Systems, 24, 2 (Fall 2007), 293–328.

## Appendix A

Partial Examples for Generalized Knowledge and Contextualized Knowledge

Task Description

In the inception phase, requirement analysts stabilize the major system requirements. The project manager develops the project schedule and cost estimates.

## Partial Example of Generalized Knowledge

If schedule is short, resource risk is high.

If resource risk is high, reduce/remove activities and iterations.

If access to stakeholders is limited, then communication risk is high.

If communication risk is high, then use formal document to communicate and allocate more time.

## Partial Example of Contextualized Knowledge

Factors considered and risks evaluated:

•	 Schedule: Nine months (short)

•	 Stakeholder (end-user) background: Users have used the old management information system (MIS). They are very knowledgeable about their requirements for the new system.

•	 Access to stakeholders (end users): This is an in-house development project. The development team has easy access to stakeholders (end users) through informal and formal channels.

•	 Requirements characteristics: Two-thirds of the functions do not need to be changed. Only one-third of the function needs to be improved. Most requirements are clearly defined.

•	 Requirement stability: The legacy system can be used as a starting point. Requirements can be expected to be stable.

•	 Team experience: The team is very experienced with requirements analysis technology and tools. But they do not have adequate experience with the .Net framework.

Issue

How many iterations should the inception phase have?

Alternative considered:

One iteration.

## Supporting Arguments

1. Inception phase focuses on requirements analysis.

2. Since the available time is short, resource risk (i.e., time) is high. There is not enough time for including many iterations in this project. Also, this project requires more iterations in a later phase (i.e., construction phase) as it has high technical risks caused by the use of a new technology for implementation (.Net). So, the inception phase cannot have many iterations.

3. Since it is easy to access end users and most functions are not changed, requirement management risks are low. Low requirement management risk and low technical risk in the requirement discipline suggest that a small number of iterations in the inception phase should be fine.

4. Since it is easy to access end users, communication risk is low. Low communication risk and low requirements management risk with end users suggest that there will not be many changes in the requirements and that it is easy to have the requirements validated by the end users. Therefore, we do not need many iterations to accommodate changes to requirements and stabilize requirements.

## Decision

This project will use one iteration for the inception phase.

## Appendix B

## Experimental Tasks

## The Case

NewAge Company has an old management information system (MIS) (referred to as the legacy system) that supports administrative functions such as data processing and report processing in the sales and marketing departments. The system was built using a third-generation language, COBOL. The CIO of NewAge wanted to reimplement the legacy system using the newest technology and had selected the .Net framework. The new system was developed in-house. Two-thirds of the functions (25 functions) in the current MIS were reimplemented without any change. A new Web-based user interface was developed and one-third of the functions (12 functions) were enhanced with major changes. The IT department of NewAge Company developed the system. The development team consisted of ten people. There were four requirements analysts, five designers and programmers, and one test engineer. All had prior experience with developing similar management information systems. But they did not have much experience in the .Net technology as it was fairly new. The total duration for the project was nine months.

## Base Process

Table B1 lists detailed tasks that need to be done in the requirement discipline in the first iteration for the inception phase. It also lists the schedule for each task, and input and output artifacts for each task. Table B2 displays the iteration plan for the four phases of the project.

## New Scenario

Consider the scenario where another company, Fly Corp., wants to implement a new MIS to manage operational data and produce management reports. Currently, it does not have any legacy MIS to support its daily operations or its own software development team. For the development of this system, it hires InternetSpeed Corp., where you are employed.

As a member of the team developing the MIS for Fly Corp., you are asked to define the process to be followed in this project. Before joining InternetSpeed, you were with NewAge Company and had detailed knowledge of the process followed by NewAge Company when it developed the MIS. You want to use this knowledge as the basis for defining the process for the new project.

At NewAge Company you had developed a new MIS based on a system currently in operation (i.e., a legacy system). The details on the process followed by the NewAge Company are described in the project Web site.

## Tailoring Tasks

## Simple Task

Review Table B1 and consider four tasks listed in the table (understand legacy system, validate legacy system requirements, document business rules for the system, elicit stakeholder new requests).

The four choices are listed for each of the four tasks in Table B3. Choose the appropriate changes and justify your choices.

## Complex Task

Review Table B2 in the base case. In Table B4, choose the appropriate number of iterations for each of the phases (second column) and the total time that should be spent on each phase (third column) from among the options listed for the new project. Please provide justifications for your decisions.

T<sup>ask</sup> <sup>Schedule</sup> <sup>for</sup> <sup>the</sup> <sup>Iteration</sup> <sup>in</sup> <sup>the</sup> <sup>Incep</sup>

<table><tr><td>Task name</td><td>Duration</td><td>Start</td><td>Finish</td><td>Input artifact</td><td>Output artifact</td></tr><tr><td>Understand legacy system</td><td>20 days</td><td>March 4</td><td>March 23</td><td>Legacy system</td><td>Stakeholder requests</td></tr><tr><td>Validate legacy system requirements</td><td>20 days</td><td>March 8</td><td>March 27</td><td>Legacy system, stakeholder requests</td><td>Stakeholder requests</td></tr><tr><td>Document business rules for the system</td><td>24 days</td><td>March 7</td><td>March 30</td><td></td><td>Business rules</td></tr><tr><td>Elicit stakeholder new requests</td><td>15 days</td><td>March 16</td><td>March 30</td><td></td><td>Stakeholder requests</td></tr><tr><td colspan="6">Table B2. Iteration Plan for the Four Phases</td></tr><tr><td>Phase</td><td>Inception phase</td><td>Elaboration phase</td><td colspan="2">Construction phase</td><td>Transition phase</td></tr><tr><td>Number of iterations</td><td>1 iteration</td><td>1 iteration</td><td colspan="2">3 iterations</td><td>1 iteration</td></tr><tr><td>Efforts (time)</td><td>30 days</td><td>45 days</td><td colspan="2">160 days</td><td>35 days</td></tr><tr><td rowspan="3">Included discipline</td><td>Requirement(25 days)</td><td>Requirement(15 days)</td><td colspan="2">Analysis and design(20 days)</td><td>Testing(15 days)</td></tr><tr><td>Analysis and design(5 days)</td><td>Analysis and design(30 days)</td><td colspan="2">Implementation(125 days)</td><td>Deployment(20 days)</td></tr><tr><td></td><td></td><td colspan="2">Testing (15 days)</td><td></td></tr><tr><td colspan="6">Table B3. Simple Tailoring Task Description</td></tr><tr><td colspan="2">Task description provided to the subjects</td><td colspan="4">Task complexity calculation (not provided to the subjects)</td></tr><tr><td>Name of the task</td><td>Proposed changes to the task</td><td>Information cues (environmental factors that need to be considered) [63]</td><td>Multiple paths and conflicting interdependence among paths [9]</td><td colspan="2">Uncertainty of solution [9]</td></tr><tr><td>Understand legacy system</td><td>a. Remove the taskb. Increase time for this taskc. Decrease the time for this taskd. Do not change</td><td>Total cues: 3Application typeRequirement characteristicsAccess to stakeholders</td><td>No.</td><td colspan="2">Low</td></tr><tr><td>Validate legacy system requirements</td><td>a. Remove the taskb. Increase time for this taskc. Decrease the time for this taskd. Do not change</td><td>Total cues: 2Application typeAccess to stakeholders</td><td>No.</td><td colspan="2">Low</td></tr><tr><td>Document business rules for the system</td><td>a. Remove the taskb. Increase time for this taskc. Decrease the time for this taskd. Do not change</td><td>Total cues: 1Application type</td><td>No.</td><td colspan="2">Low</td></tr><tr><td>Elicit stakeholders' new requests</td><td>a. Remove the taskb. Increase time for this taskc. Decrease the time for this taskd. Do not change</td><td>Total cues: 2Application typeAccess to stakeholders</td><td>No.</td><td colspan="2">Low</td></tr></table>

<table><tr><td colspan="3">Task description provided to the subjects</td><td colspan="3">Task complexity calculation (not provided to the subjects)</td></tr><tr><td>Phase</td><td>Number of Iterations</td><td>Total time estimated for the phase</td><td>Information cues (environmental factors that need to be considered) [63]</td><td>Multiple paths and conflicting interdependence among paths [9]</td><td>Uncertainty of solution [9]</td></tr><tr><td>Inception phase</td><td>a. 1b. 2c. 3d. 4</td><td>a. 20–30 daysb. 40–60 daysc. 70–90 days</td><td>Total cues: 6Team experienceRequirement characteristicsStakeholders’ backgroundRequirement stabilityScheduleAccess to stakeholders</td><td>Yes</td><td>High</td></tr><tr><td>Elaboration phase</td><td>a. 1b. 2c. 3d. 4</td><td>a. 20–30 daysb. 35–45 daysc. 50–60 days</td><td>Total cues: 5Team experienceTeam sizeApplication typeRequirement stabilitySchedule</td><td>Yes</td><td>High</td></tr><tr><td>Construction phase</td><td>a. 1b. 2c. 3d. 4</td><td>a. 100–110 daysb. 150–160 daysc. 170–180 days</td><td>Total cues: 2Team experienceRequirement characteristics</td><td>Yes</td><td>High</td></tr><tr><td>Transition phase</td><td>a. 1b. 2c. 3d. 4</td><td>a. 20–30 daysb. 35–45 daysc. 55–65 days</td><td>Total cues: 3Team experienceStakeholders’ experiencesApplication type</td><td>Yes</td><td>High</td></tr></table>

Appendix C

<table><tr><td colspan="4">Table C1. Indicators Measuring Process Tailoring</td></tr><tr><td rowspan="2">Constructs</td><td rowspan="2">Items</td><td colspan="2">Factors</td></tr><tr><td>Effectiveness (Cronbach&#x27;s alpha: 0.99)</td><td>Efficiency (Cronbach&#x27;s alpha: 0.96)</td></tr><tr><td rowspan="9">Effectiveness</td><td>Q1: “Decision is sound”</td><td>0.91</td><td>0.35</td></tr><tr><td>Q2: “Justification is correct”</td><td>0.93</td><td>0.32</td></tr><tr><td>Q3: “Justification is complete”</td><td>0.93</td><td>0.31</td></tr><tr><td>Q4_Inverse: “Some statements are not correct”</td><td>0.94</td><td>0.31</td></tr><tr><td>Q5: “Justification sufficiently explains the reason”</td><td>0.94</td><td>0.31</td></tr><tr><td>Q6: “Justification covers all aspects”</td><td>0.94</td><td>0.31</td></tr><tr><td>Q7: “The overall accuracy”</td><td>0.92</td><td>0.35</td></tr><tr><td>Q8: “Overall completeness”</td><td>0.94</td><td>0.31</td></tr><tr><td>Q9: “Overall quality”</td><td>0.93</td><td>0.33</td></tr><tr><td rowspan="4">Efficiency</td><td>E1: “It took too long to perform”</td><td>0.32</td><td>0.88</td></tr><tr><td>E2: “It requires a lot of time”</td><td>0.34</td><td>0.90</td></tr><tr><td>E3: “It requires a lot of thought”</td><td>0.29</td><td>0.88</td></tr><tr><td>E4: “I spent a lot of effort”</td><td>0.28</td><td>0.90</td></tr></table>

## Covariates: Subjects’ Experience

1. Past experience with software development: \_\_\_\_\_\_years \_\_\_\_\_\_ months

2. Past experience with software project management: \_\_\_\_\_\_ years months

3. Past experience with software development process: \_\_\_\_\_\_ years months

## Appendix D

## Order Effects

Table D1. Multivariate Tests to Examine Order Effects

<table><tr><td>Effect</td><td>Value</td><td>F</td><td>Hypothesis df</td><td>Error df</td><td>Significance</td></tr><tr><td>task_order</td><td>0.00</td><td>0.30</td><td>2.00</td><td>248.00</td><td>0.37</td></tr><tr><td>Group * task_order</td><td>0.01</td><td>0.51</td><td>4.00</td><td>498.00</td><td>0.37</td></tr><tr><td>complexity * task_order</td><td>0.00</td><td>0.02</td><td>2.00</td><td>248.00</td><td>0.50</td></tr><tr><td>Group * complexity * task_order</td><td>0.00</td><td>0.15</td><td>4.00</td><td>498.00</td><td>0.50</td></tr></table>

## Appendix E

## Details on the Protocol Analysis Study

## Study Design

The study was designed similar to the exp erimental study reported in the experiment. We used a 3 × 2 design in which two levels of complexity (low and high) and access to two types of knowledge (generalized and contextualized) and no knowledge were used. The subjects were assigned to each of the groups in the same manner as in the experimental study. Twelve experienced software developers with an average of four years of experience in software process tailoring and 12 years in software development participated in the study. They were drawn from the software development division of a very large IT organization that employs over 2,000 personnel. The participants were routinely engaged in tailoring a standardized process to meet the unique needs of various products carried out by the IT organization. Given the volume and the richness of qualitative data generated even from a few subjects, sample sizes of between 2 and 20 subjects is typical.

## Procedures

The subjects were asked to perform the same tasks that were used in the experiment. The participants were requested to think aloud, verbalizing their thoughts while performing these tasks. When there was a pause of more than 20 seconds, the subjects were prompted to verbalize their thoughts. Concurrent verbal reports were recorded and transcribed. In order to familiarize the subjects with verbalizing their thought process, two sample exercises were provided at the beginning of the study. While the participants were not given any specific time constraints, each subject spent about 40 to 90 minutes on the task.

## Data Analysis

Following Todd and Benbasat [59], we used coding schemes for breaking down segments of data to specific categories that are explicated “a priori.” Utterances that are irrelevant to the tasks at hand were coded as “irrelevant.” Two coders coded the segments by assigning them to categories. Each of the 2,200 utterance units was assigned to the categories discussed above. The interrater agreement was 96 percent (kappa = 0.96). This data analysis technique was followed by identifying specific categories, breaking down the protocols into small segments, and assigning these segments to specific categories. As suggested by Ericsson and Simon [16], to minimize the contamination of data by ad hoc theory, development of coding categories was done a priori, prior to accepting input for encoding. The codes were drawn from prior research on process tailoring which identified knowledge elements and steps used by experts in process tailoring. Here, knowledge elements represent the knowledge the subjects used (e.g., process goals and tailoring strategies). Operator elements represent the occurrence of an activity (e.g., assessing tailoring strategies and exploring prior experience). Further, the relationships between knowledge elements and operator elements were identified using an iterative and subjective process.
