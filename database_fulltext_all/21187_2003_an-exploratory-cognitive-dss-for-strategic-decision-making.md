---
otero_id: 21187
otero_key: "5GW3TT8Y"
title: "An exploratory cognitive DSS for strategic decision making"
authors: "Jim Q. Chen; Sang M. Lee"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00139-2"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An exploratory cognitive DSS for strategic decision making

Jim Q. Chen <sup>a,</sup>\*, Sang M. Lee <sup>b</sup>

<sup>a</sup>Herberger College of Business, St. Cloud State University, St. Cloud, MN 56301, USA <sup>b</sup>College of Business Administration, University of Nebraska-Lincoln, Lincoln, NE 68588-0491, USA

Accepted 1 July 2002

## Abstract

Research on decision support systems (DSS)/executive information systems (EIS) has been primarily concerned with the behavioral aspect of managerial work and has largely ignored the cognitive aspect of decision support. Rather than focusing on the manager’s information need on ‘‘critical success factors’’ and the need for supporting specific decision making, this research emphasizes the need to support the decision maker’s general thinking processes to reduce cognitive biases in decision making. This paper reports the design, development, and exploratory assessment of a prototype cognitive decision support system (CDSS).

<sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Managerial cognition; Cognitive decision support; Strategic decision making

## 1. Introduction

Decision support systems (DSS) were envisioned to be ‘‘executive mind-support systems’’ that seek to establish a symbiosis of human mind and computer by allowing for a high degree of human –computer interaction [29,30]. Up to now, this grand vision has yet to become a reality. Most of today’s computer-based decision support has focused on support for the behavioral aspects of decision making and extensions of the analytical capabilities of decision makers. For example, executive information systems (EIS) provide executives with information on critical business success factors in a timely and user-friendly fashion.

Various decision support systems provide their users quantitative modeling tools and easy data access. The cognitive aspect of decision support, however, has received relatively little research, although it has long been recognized as an important consideration of decision support systems design.

Cognitive orientation or mental models play a very important role in a decision maker’s understanding of business environments and ill-structured problems. Donaldson and Lorsch [3] conducted an exploratory study on the goal formulation and strategic decisionmaking processes of top executives in 12 Fortune 500 companies. They found that corporate executives are constrained not only by objective financial goals and constituency demands, but also by an elusive set of psychological constructs of their own beliefs. They observed that ‘‘these interrelated beliefs act as a filter through which management perceives the reality facing its firm. Thus, psychological constructs serve two essential and significant functions. One is to simplify: to translate a world that can be overwhelmingly complex and ambiguous into comprehensible and familiar terms. The other is to provide continuity and stability when change threatens to undermine the lessons of experience’’ [p. 79]. Similarly, Porac and Thomas [18] suggest that a mental model—a set of deeply held assumptions and beliefs—provides a useful conceptual tool for decision makers to simplify complex business environments and to impose order on volatile competitive conditions to reduce uncertainty.

On the other hand, outmoded assumptions and beliefs are detrimental to the survival of today’s firms in the turbulent business environment. Senge [24] observed that many good strategies in business fail to get implemented and systemic insights never find their way into operating policies because they conflict with executives’ deeply held assumptions of how the world works. These assumptions limit decision makers to familiar ways of thinking and acting [p. 174]. Gilad [6] cited many business downfalls as a result of obsolete mental models and business blind spots held by the executives in these firms.

Research progress in the cognitive aspect of decision support has been slow because of our limited understanding of executive cognitive processes and the fact that computer technology does not lend itself easily to cognitive support. However, new generation of computer technology and our increased understanding of managerial cognition in recent years have created a renewed research interest in this area. Traditional decision support systems and executive information systems have been successful in helping executives build mental models about their business reality by providing layered information. But they provide little direct aid in detecting and unlearning outmoded mental models. An ideal decision support system should be a part of a human–computer collaborative learning environment where the computer plays a more active role in facilitating the decision maker’s creative thinking and providing tools to surface tacit assumptions and beliefs, and aid his or her forward thinking.

This paper reports on a research project that looks into the cognitive process of strategic decision making to identify some cognitive simplification processes that decision makers employ in dealing with complex decision-making situations. Then, a set of IS functions is designed to aid the decision maker’s cognitive processes. The paper is organized as follows. In the next two sections, a review on the cognitive aspect of executive work and cognitive simplification processes is presented. Then, a Web-based system architecture for multi-participant cognitive decision support systems (CDSS) is proposed. The design, implementation, and evaluation of an exploratory prototype system are discussed. Finally, conclusions and future research are presented.

## 2. Managerial cognition and IS support

Mintzberg [15] identified not only 10 roles of top executives but also recognized the importance of mental models in executive work. Mental models are commonly referred to as deeply held assumptions and beliefs that enable individuals to make inferences and predictions. They can be represented in many forms: tokens, spatial relations between entities, temporal or causal relations among events. Mintzberg contends that executives use the information they collect to develop a series of mental models of the internal working of their organizations, the behaviors of their subordinates, the trends in the organization’s environment, and so on. When dealing with complex issues, executives use their mental models to simplify the decision process and test alternatives. He even concludes that the effectiveness of the manager’s decision is determined to a large extent by the quality of his or her mental models.

Rockart and De Long [21] provided a solid analysis of executive work. One of the perspectives they discussed is Isenberg’s ‘‘Manager as Sense-maker’’ view. This conception focuses on how executives impose cognitive structures on their environments. A key role of top executives in today’s dynamic organizational environments has become provision of making sense of ambiguous information. The role is often seen as critical to the success and even the survival of organizations, chiefly because of its implications for influencing action alternatives and subsequent outcomes. Similarly, Porac and Thomas [18] suggest that mental models provide a useful conceptual tool for decision makers to simplify complex business environments and to impose order on volatile competitive conditions to reduce uncertainty. In an article concerning competitor definition, they described how decision makers organized their business competitors into cognitive taxonomies. They argued that by placing the organization within the context of a cognitive taxonomic system, the decision maker makes sense of his or her organization’s activities in relation to others within the environment [p. 231].

Jaques [9] provided a cognitive view of management through his stratified systems theory of organizations. According to his theory, the structure of any bureaucratic system can be stratified into seven levels of abstraction. The first three levels involve concrete tasks performed by departmental and front-line managers. The time span of their tasks ranges from 1 day to no more than 1 year. However, tasks at the fourth level and up become increasingly abstract and cognitively demanding. The time span of such tasks can run from 2 years to more than 20 years. Examples of such tasks include providing an overall corporate strategic direction, creating strategy and translating it into business goals, and redefining goals and determining field operations. These tasks are unstructured and cannot be foreseen in concrete terms. In Jaques’s words, ‘‘the project (task) can not be completely constructed. It remains a combination of a conscious subjective pic ture, incomplete in itself, whose specific total forms and content are unconsciously intuitively sensed but can not quite be consciously grasped.’’ [p. 149]. To carry out the tasks, the executive has to rely on his or her prior knowledge and experience, but at the same time achieve a detachment from such experience.

The cognitive differences between lower and higher level management suggest that executive support should be somewhat different from lower level management support. In fact, some researchers have observed that senior executive decision behaviors are quite different from those behaviors traditionally supported through decision support systems. Executives do not usually make major decisions by choosing from a set of predetermined alternatives. On the contrary, executives heavily rely on their intuition and seldom think in ways that one might simplistically view as ‘‘rational’’ [8,21]. Furthermore, Zmud [30] made the following observations:

<sub>x</sub> senior executives manage issues, instead of managing people or resources.

senior executives create decision situations, instead of reacting to decision situations.

<sub>x</sub> senior executives work through networks of people, instead of working through decision models.

<sub>x</sub> senior executives implement decisions, instead of making decisions.

Zmud [30] thus argues that IS support should focus on executives’ thought support in problem and opportunity recognition and diagnosis instead of providing support for the evaluation and choice phase of the decision-making process.

Executive thought processes are highly inferential, intuitive, opportunistic, qualitative, and right-brain [8,19]. Researchers in strategic decision making observed that when an executive makes strategic decisions, he or she is involved in two kinds of thinking: looking backward to understand the past and looking forward to predict the future [4]. Torbert [25] also observed that the quality of a great leader’s mind is its capability to think back and forth between the immediate situation and the historical overview. Bateman and Zeithaml [1] argue that strategic decisions are outcomes of a variety of contextual influences arising from past events, present circumstances, and perspectives on the future.

It appears that decision support should focus on the cognitive modeling. More specifically, a decision support system should address the following issues: (1) consciously helping enrich the decision maker’s mental models; (2) facilitating mental model validation and integration; (3) supporting the decision maker’s backward and forward thinking; (4) mitigating judgmental errors due to human limited information processing capabilities. A few recent research projects started addressing some of these issues.

Carlson and Ram [2] describes a hypermedia system, SPRINT, which can be used by an executive to organize his or her thoughts while forming a plan. The system provides IS functions that facilitate a user’s creation of concept nodes and relationship links among nodes, which describe his or her understanding of the strategic issues, impacting the strategic plan. The user can also specify the resources that are required to achieve the plan and the relationship that those resources hold with regard to the strategies. Their work represents a step closer toward conscious thought support.

More recently, Yadav and Khazanchi [28] report a ‘‘Cognitive Lens Support System’’ for aiding decision makers in understanding ill-structured problems. Their assertion is that IS support provided to managers through their ‘‘cognitive orientations’’ might facilitate understanding of ill-structured problems. They propose three inquiry modes: introspective, dialectic, and eclectic. The three modes operate on the cognitive lens stored and maintained in a ‘‘Cognitive Lens Support System.’’ Their system, however, was not empirically validated.

## 3. Cognitive simplification process

Research in cognitive psychology, behavioral decision theory, and strategic decision making has identified several cognitive simplification processes or heuristics which decision makers use when they deal with complex, ambiguous, and uncertain decision situations [14,20,23]. These processes include availability, adjustment and anchoring, prior hypothesis, and reasoning by analogy. Although they are useful in some circumstances, they are also the causes for several types of judgment errors and biases.

## 3.1. Availability

People tend to assign more importance (weight) to recent events or knowledge because they are easy to recall and imagine from memory. Executives rely heavily on their past experiences and knowledge to make decisions. Their limited ability to retrieve past cases may cause them to make biased judgments and decisions.

## 3.2. Adjustment and anchoring

In strategic decision making, executives often make initial judgments about certain decision variables and adjust the initial judgments when new data become available. However, the adjustments are typically insufficient. The final judgment is biased toward the initial estimate [23]. When executives plan for the uncertain future, they anchor on past experience. Past experience may be misleading and inappropriate for prediction of the future, especially when there is a major discontinuity in social trends or technological breakthroughs.

## 3.3. Prior hypothesis bias

Individuals tend to seek and use information consistent with their beliefs rather than information that is inconsistent. Jervis [10] made the following observation:

We ignore information that does not fit, twist it so that it confirms, or at least does not contradict, our beliefs, and deny its validity. Confirming evidence, by contrast, is quickly and accurately noted. [p. 143]

This bias explains why sometimes individuals make bad decisions based on erroneous assumptions even though numerous evidences show that the assumptions were wrong. An effective cognitive decision support system should do more than passively present information to executives. It should actively engage in the executive’s thinking process and provide both flexibility and guidance in decision support.

## 3.4. Reasoning by analogy

Decision makers often reason by analogy. When making judgments and decisions under uncertainty, decision makers often compare new problems with past cases or experiences from which useful information, strategies, and courses of action can be derived. This process can greatly benefit effective decision making. Reasoning by analogy has also been shown to be effective in generating creative solutions to problems. However, reasoning by analogy is also problematic. For example, human beings have difficulty retrieving past experiences. The associations between existing circumstances and past events can be inappropriate and misleading at times.

In strategic decision making, reasoning by analogy typically involves the application of analogies from simpler situations to complex strategic problems, which helps reduce the uncertainty perceived in the environment. However, the use of simple analogies may mislead the decision maker into an overly simplistic view of the situation [23].

## 3.5. Overconfidence

Researchers have shown that people have a tendency to be overconfident in their beliefs and judgments [5,17]. Overconfidence can be dangerous. It indicates that people often do not know how little they know and how much additional information they need. Many business blind spots can be attributed to the overconfidence of top management. For example, IBM was too confident about its dominant ability in the computer industry to pay attention to changing customer demands [6]. The causes of overconfidence seem closely related to availability, adjustment and anchoring, and prior hypothesis biases discussed above. Decision makers tend to rely on recent information or information that is easy to recall from memory when making decision (availability bias). When information is abundant, decision makers tend to anchor on prior hypothesis or beliefs and seek confirming information (prior hypotheses bias). These biases are likely to cause decision makers to ignore important information and become overconfident about their judgments. Furthermore, decision makers have difficulty in imagining all of the possible ways that events can unfold. Because they fail to envision important pathways in the complex net of future events, they become unduly confident about predictions based on the few pathways they actually do consider [22].

## 4. A cognitive approach to decision support systems design

A conceptual model is proposed based on the discussions in Section 3. The model shown in Table 1 consists of three supporting modes: retrospective, introspective, and prospective. DSS functions are proposed for each mode. Case Memory provides the user with tools to manage business cases, his or her experience, the opinions of others, speculations, and even rumors. Personal experience, speculations, and rumors are termed ‘‘soft’’ information, which is often used in strategic decision making [27]. Case Memory reduces the user’s tendency to use most recent information by making the past events and cases in the system’s case base equally accessible. It aids the user in recalling the circumstances under which an event occurred or a decision was made, which may help to avoid inappropriate association between current circumstances and past events.

Cognitive mapping has been used extensively in the area of foreign policy analysis and strategic management to explore and represent an individual’s assumptions and belief systems. A cognitive map represents a decision maker’s understanding of the causal relationships among interacting factors. It has two basic types of elements: concepts (nodes) and causal assertions (links). The concepts are treated as variables and assertions are viewed as relationships among variables. A person’s cognitive map is relatively stable and might be used to derive explanations of the past, make predictions for the future, and choose policies in the present. It is a good way for group members to share, negotiate, and build upon their aggregate wisdom.

Summary of the three-mode conceptual model

<table><tr><td>Supporting mode</td><td>DSS supporting functions</td><td>Possible cognitive aid</td></tr><tr><td>RetrospectiveRecall past experience and cases.Analogical thinking.</td><td>Case MemoryAid storage, retrieval, and management of personal experience and cases.</td><td>Memory aidReduce availability biasAnalogical cases aid creative thinking.</td></tr><tr><td>IntrospectiveReflect on and examine the assumptions and belief system.</td><td>Cognitive MappingAid graphical representation of assumptions/belief systems (cognitive maps)Deduce the impact on specific construct through inferenceManage and manipulate belief systems.</td><td>Surface and examine explicit and implicit assumptions.Overcome blind spots.Increase self-assurance.</td></tr><tr><td>ProspectiveEnvision future state of business environments.Understand possible consequences of decisions.</td><td>Scenario BuildingAid multiple scenarios construction process.Assist multiple scenarios management and manipulation.</td><td>Reduce overconfidence.Reduce anchoring effect.Reduce availability bias.Change frame of reference.</td></tr></table>

The Cognitive Mapping provides the user with a graphical tool to represent and analyze his mental models. The user can visually inspect their reasoning process, and query a complex cognitive map to obtain explanation on a specific issue. The mapping tool also allows its user to retrieve and compare his or her cognitive map with those of others. This capability gives the user an opportunity to get a different point of view on the same issue.

Scenario Building provides the user aids in forward thinking by making a set of tools available for him to create and manage future scenarios. Executives frequently deal with highly complex situations involving many interacting factors and unpredictable future. Scenario Building is a valuable technique to plan for the uncertain future. For more detailed discussions on the model, the reader is referred to Ref. [13].

## 4.1. A web-based architecture for multi-participant cognitive decision support systems

The three-mode cognitive decision support system is envisioned to be a multi-participant decision support system running on the Intranet in an organization. According to Holsapple and Whinston [7], a multi-participant decision support system (MDSS) consists of four subsystems: (1) a language system which can handle both private and public messages; (2) a problem processing system (PPS) which is capable of knowledge acquisition, selection, and derivation; (3) a knowledge system which can store both private and public domain knowledge for multiparticipants; and (4) a presentation system. The CDSS architecture shown in Fig. 1 is based on the MDSS framework by Holsapple and Whinston [7,p,611]. The architecture is composed of the following components: CDSS Graphic User Interface, Problem Processing System (Case Memory Subsystem, Cognitive Mapping Subsystem, and Scenario Builder), Knowledge Management System (Case Base, Cognitive Map Base, Scenario Base, and Trends and Uncertainties).

## 4.2. Graphic user interface

The CDSS is intended to run on an organization’s Intranet. The standard Web browsers can be used to access the system residing on the application server. The system provides a complete graphical user interface for the users.

## 4.3. Problem processing system

The PPS consists of three modules: Case Memory, Cognitive Mapping, and Scenario Building. Upon a user’s log on to the CDSS, a process is initiated along with a chunk of working memory allocated to the user. The knowledge acquisition and selection are accomplished through user interactions with the three modules. Knowledge is processed in working memory and transferred to the knowledge management system for storage. The system knowledge [7] such as how to create cognitive maps and scenarios is hard-programmed into PPS.

## 4.3.1. Case memory subsystem

The Case Memory Subsystem is intended to provide its user with a set of tools to record and retrieve business cases and any type of ‘‘soft’’ information such as rumors, speculations, and personal experience. The user has the freedom to keep any number of his or her cases as private or public. Public cases can be accessed by all participants of a decision-making team.

All the cases are stored in the Case Base. To facilitate case retrieval, cases are classified according to two schemes: the type of industry and the type of problems or decisions. A typical case is composed of six parts:

1. Problem: description of the problem.

2. Solution of the problem.

3. Results (optional).

4. Key words: three or more key words describing the main nature of the case.

5. Source.

6. Personal notes: relevance of the case to the user’s business or problems; insights gained from the case.

The case base is designed as a detachable component of the system to facilitate independent case base supply. Given the important roles of knowledge management in organizations, there has been a increasing number of business case studies, lessons, and industry best practices published in various journals and books in recent years. With a well-defined case writing standard, cases can be obtained from independent case suppliers. In a typical situation, CDSS comes with an initial case base with cases adopted from journals, books, and magazines. The user adds new cases, personal insights and anecdotes as time goes. For busy top executives, their experience and stories can be captured in a palm-sized voice recorder and later be transcribed into case memory by an executive assistant.

![](/api/attachments/5GW3TT8Y/fulltext/images/1efcc471f23467d2e36f556dcc45b0d5493c8b4f05d1b080229f5eb507f60af1.jpg)  
Fig. 1. CDSS system architecture.

## 4.3.2. Cognitive mapping subsystem

This subsystem is intended to provide the decision maker with a set of tools to construct, modify, and query his or her own causal reasoning concerning a particular issue. It supports comparison of one’s own causal map with someone else’s on the same issue.

Maps in the Cognitive Map Base are organized and stored by specific issues. For example, a sub-map base may contain all divisional managers’ causal reasoning on the ‘‘loss of sales’’ issue or the ‘‘rising operating cost’’ problem. The user can easily retrieve and compare his or her cognitive map with that of others’. A visual comparison between one’s own reasoning and that of others’ can help one gain a better understanding of the nature and complexity of the issue. It allows the user an opportunity to understand the reasoning behind an opposite view on an issue. The construct function guides the manager in creating a new cognitive map by eliciting the nodes and relationships relevant to a problem domain. See Fig. 2 for a sample screen of constructing a new cognitive map. The user clicks on Caused by or Causes buttons to create the next node. When no more nodes are identified, a click on the Map button will generate the cognitive map. Fig. 3 shows Mr. Davis’ cognitive map on the loss of sale problem. In addition, removing or adding a new node or link is done by the dragand-drop operation.

![](/api/attachments/5GW3TT8Y/fulltext/images/1053612a6358f4a39f9e5ef6d8850272a7a1acce669eba2eee94f65235238580.jpg)  
Fig. 2. A sample screen of cognitive mapping process.

The query function in the module allows its user to ask questions of the following types:

Q1. What are the causes of a particular problem (e.g., declining sales) ?

Q2. What are the consequences of a particular problem ?

When a causal map becomes too big, this query function may be an alternative way to understand the cause-and-effect relationships of an issue. However, the query function can only be used to query a causal map that does not contain a circular causal relationship. In other words, the query function will not work when a map contains such causal relationships as ‘‘A’’ causes ‘‘B’’, ‘‘B’’ causes ‘‘C’’, and ‘‘C’’ causes ‘‘A’’.

The automatic case search function allows the user to search cases relevant to a particular issue in a cognitive map. For example, when the user constructs a causal map regarding the causes of declining sales, he or she may want to review past cases relevant to this problem. The user can conduct the case search without leaving the current working module. This function provides an automatic link between the Cognitive Mapping module and the Case Memory module.

## 4.3.3. Scenario builder

This subsystem supports the user in constructing and retrieving business scenarios. The system draws on the knowledge from the Trends and Uncertainties knowledge base to interacts with the user to identify the economic, political, societal, technological, and industry trends as well as key uncertainties. The user’s insights and opinions are elicited and stored in the knowledge base. Fig. 4 shows a snapshot of the scenario building process. Based on the input from the user and the knowledge base, the system automatically generates three scenario outlines: best, worst, and most likely. The best scenario outline is created from the favorable outcomes of key environmental uncertainties. The worst scenario assumes just the opposite. The most likely scenario is based on the outcomes

![](/api/attachments/5GW3TT8Y/fulltext/images/5aa16159c227252574d9ca9375e6c4cf86800bbf40a966652d7b2c7d1fbdfdd5.jpg)  
Fig. 3. Mr. Davis’s cognitive map on loss of sales problem.

which the user ranked as most likely to occur. There are two steps involved in this process. First, the system will generate three alternative future developments of the trends and key uncertainties. Secondly, a consistency check is conducted. The consistency check identifies the possible inconsistencies among the outcome combinations of key uncertainties. For example, full employment and zero inflation do not go together, so these two outcomes should not appear in the same scenario. After the consistency check, the scenario outline is placed in a scenario editor for further editing. The three scenarios serve as a starting point for the user to explore other possibilities.

![](/api/attachments/5GW3TT8Y/fulltext/images/cd09f0bff9f56c33a3c30e1cc3126caaa14cb6ffd9ca81decd211aca2c933bb8.jpg)  
Fig. 4. A snapshot of scenario building process.

The scenario retrieval function allows the user to retrieve a scenario either by name or by key words. The decision maker can review the scenarios created by others and easily modify or delete a scenario.

## 4.4. Domain knowledge management system

The domain knowledge management system provides the user tools to maintain and manipulate domain knowledge in the forms of cases, cognitive maps, and scenarios. Domain knowledge is divided into private and public knowledge [7]. Private knowledge can only be accessed by a particular user. This division is very important in the multi-participant CDSS because decision makers need time to reflect on their cases, cognitive maps, and scenarios before making them public. Both private and public knowledge is stored in Case Base, Cognitive Map Base, and Scenario Base.

The Trend & Uncertainty Base contains major trends and key uncertainties that may have a significant impact on a particular industry. It consists of the following six categories of knowledge:

1. Economic trends

2. Political trends

3. Societal trends

4. Technological trends

5. Industrial trends

6. Key uncertainties

For the prototype system, the personal computer industry is selected as the domain for building the Trends and Uncertainties knowledge base. The sources of the knowledge are case studies, published surveys, and academic articles. During the scenario generation process, the trends and uncertainties are retrieved from the knowledge base and the user’s assessments of these trends and uncertainties are elicited and recorded. The user may add or delete an uncertainty. For each new uncertainty added, three possible outcomes are elicited from the user and added to the knowledge base.

## 5. Exploratory assessment

The validation of most decision support systems has been a challenging task [11,16]. The difficulty in this research lies in the assessment of the cognitive impact of using the prototype system. There are many factors that may affect the decision maker’s thinking. It is extremely difficult to separate and control these factors. A laboratory study may provide a controlled environment, but the lack of a real-world setting will make the study results less useful. Nevertheless, an exploratory two-phased case study was conducted to collect feedback from real business decision makers on the proposed system.

## 5.1. Interviews with three small business executives

In the first phase case study, three small business executives (the Vice-president of a marketing consulting firm, the President of a computer consulting firm, and the Vice-president of a steel mills and blast furnaces manufacturing company) were interviewed to elicit their comments on the proposed systems.

The interviewees showed great interest in the proposed system and provided valuable comments which helped the subsequent development of the prototype system. They thought that the boundaries of the three modes (retrospective, introspective, and prospective) were somewhat vague. One of them commented that his thinking was mostly back (past) and forth (future), he seldom had time to do introspective or reflective thinking, although he agreed that introspective thinking is very important to surface hidden business assumptions and to understand complex business problems. All interviewees agreed that the case retrieval and scenario building tools were of great value to most business executives. They emphasized the importance of being able to retrieve quickly whatever information or cases that were in need. However, they seemed to be uncertain about the cognitive mapping tool. This might be attributed to the uncommon use of the technique in the business world. Without actually using the tool, it was difficult for them to see how the technique could improve their thinking.

5.2. Preliminary survey results from six small business executives

For the second phase of the case study, three more real business decision makers participated in the study. They are the President of the same marketing consulting firm involved in the first phase study, the IS Project Manager from Foundation for Educational Funding, and the Assistant Manager of MIS from a group grocery supermarket. Among the six participants, one was female. The average length of time they have worked in their companies is 10.7 years.

The six participants were requested to test using the prototype system for about 2 weeks. Then they filled out a survey form designed to assess the system’s usefulness. In most cases, the researchers had to call the participant and offered any help they might need in using the program. After the questionnaires were collected, follow-up phone calls were made to thank them for their participation in the study.

The average ratings and standard deviations are given in Table 2. Each question is rated on five scales: 1—Strongly disagree, 2—Disagree, 3—Neutral, 4— Agree, 5—Strongly agree. The overall average rating of the system was 4.1. The system was considered to be user-friendly and the system response time is fast. The participants all agreed that the Case Memory module could help them quickly retrieve and record business cases and personal experience (rating = 4.3), and aid them in creative problem solving (rating = 4). They also agreed that the Cognitive Mapping helped them think more clearly about the causal relationships among interacting factors (rating = 4.43), and the system supported them construct and retrieve cognitive maps quickly (rating = 4.1). Most participants agreed that the scenario building process helped them gain a better understanding of the general business environments (rating = 3.85) and the system helped them create scenarios quickly (rating = 3.78).

Among the three modules, the Cognitive Mapping module received the highest average rating (4.03) and the Scenario module received the lowest average rating (3.81). One possible explanation for the low rating of the Scenario module is that none of the participants in the case studies had experience with the scenario planning technique. This lack of experience might have reduced these participants’ appreciation of the aids provided by the system.

Table 2  
Average ratings for CDSS performance

<table><tr><td>Questionnaire items</td><td>Average ratings</td><td>S.D.</td></tr><tr><td>1. The system is easy to start up.</td><td>4.71</td><td>0.487</td></tr><tr><td>2. The system is user-friendly.</td><td>4.10</td><td>0.377</td></tr><tr><td>3. The system’s response time is fast.</td><td>4.57</td><td>0.534</td></tr><tr><td>4. With the Case Memory module, I can quickly record and retrieve business cases, personal experience, etc.</td><td>4.30</td><td>0.487</td></tr><tr><td>5. Case Memory (reviewing past cases) helps me make better decision.</td><td>3.43</td><td>0.534</td></tr><tr><td>6. Case Memory helps me find creative solutions to my problems.</td><td>4.00</td><td>0</td></tr><tr><td>7. The cognitive map may help me think more clearly about the causal relationships among interacting factors concerning a particular policy issue.</td><td>4.43</td><td>0.534</td></tr><tr><td>8. With the Cognitive Mapping module, I can easily create, retrieve, and modify causal maps.</td><td>4.10</td><td>0.690</td></tr><tr><td>9. With the Cognitive Mapping module, I explored more interacting factors than I do without it.</td><td>3.57</td><td>0.534</td></tr><tr><td>10. With the Scenario module, I can construct scenarios quickly.</td><td>3.78</td><td>0.698</td></tr><tr><td>11. Going through the scenario building process helps me gain a better understanding of general business environments.</td><td>3.85</td><td>0.690</td></tr><tr><td>Average rating</td><td>4.10</td><td>0.506</td></tr></table>

## 6. Comparison of CDSS with typical DSS/ESS

The main purpose of this research was to investigate a new way of decision support. The proposed system is meant to enhance current DSS/ESS. Table 3 shows the comparison between current DSS/ESS systems and the CDSS. The system capabilities in the table are based on Turban [26] and Young [29].

The technical features of a DSS/ESS can be divided into three groups: information retrieval (features 3 through 6), quantitative modeling (feature 7 through feature 9), and qualitative modeling (features 10 and 12). The information retrieval is the fundamental feature of ESS. The quantitative modeling extends the user’s analytical abilities and reflects the recent trend toward the integration of ESS and DSS. The qualitative modeling capability that this research attempts to provide assists the user in modeling their assumptions and beliefs (introspective) and supports their retrospective thinking (case memory) and prospective thinking (scenario building). In contrast to quantitative modeling, the qualitative modeling supports its users at a higher conceptual level.

Table 3  
Comparison between the prototype CDSS and current DSS/ESS

<table><tr><td>Major ESS features</td><td>Explanations</td><td>Typical DSS/ESS</td><td>CDSS</td></tr><tr><td>1. User-friendly interface</td><td></td><td>X</td><td>X</td></tr><tr><td>2. Short response time</td><td></td><td>X</td><td>X</td></tr><tr><td>3. Access to aggregate information</td><td></td><td>X</td><td></td></tr><tr><td>4. Drill down capability</td><td>Producing information at various levels of details</td><td>X</td><td></td></tr><tr><td>5. Critical success factors</td><td>Information organized around critical factors vital for attaining the organization&#x27;s goals</td><td>X</td><td></td></tr><tr><td>6. Exceptional reports</td><td></td><td>X</td><td></td></tr><tr><td>7. Trend analysis</td><td>Graphs shows trend, ratios, and deviations</td><td>X</td><td></td></tr><tr><td>8. What-if analysis</td><td>Simulation analysis</td><td>X</td><td></td></tr><tr><td>9. Forecasting</td><td>Quantitative forecasting, e.g., sales forecasting</td><td>X</td><td></td></tr><tr><td>10. Access to Case Memory</td><td>Record and retrieve business cases, lesson learned, personal experience, rumors, and speculations</td><td></td><td>X</td></tr><tr><td>11. Modeling assumptions</td><td>Surfacing, representing, comparing assumptions and beliefs. Organizing and synthesizing individual knowledge.</td><td></td><td>X</td></tr><tr><td>12. Scenario building</td><td>Modeling future business environments</td><td></td><td>X</td></tr></table>

## 7. Applicability issues

The prototype presented in this paper serves as an experimental vehicle to explore cognitive decision support. Consequently, it does not address all the issues of its applicability to practice. More research and development are needed to prove the system’s practical usefulness. However, we believe that as computer hardware and software technology continues to advance and more and more managers become computer savvy, the chance of its successful applications in real world will be improved.

The new technology affords us new ways of delivering three-mode supports in a user-friendly fashion. For example, virtual reality and visual computer simulation can be used to implement the scenario-building process. Multimedia technology can be used to store and present successful and failed business decisionmaking cases. Corporate Intranet and Extranet provide an effective implementation platform for sharing case memory, mental models, and scenarios among organizational members. The advance of natural language understanding processors and wireless networking technology will help managers capture and transfer knowledge regardless of the time and spatial constraints.

The proposed CDSS can be used as a management training tool. There are several advantages of using it for training over traditional seminar-type training:

1. Self-paced training without time and geographical constraints associated with seminar-type training.

2. Training in retrospective, introspective, and prospective thinking.

3. A large number of historical business success cases and lessons are available to the user at a few key strokes.

4. Access to colleagues’ thinking on a variety of issues in the form of cognitive maps without disruption of their work. This is possible because CDSS can be deployed in a network environment such as a corporate Intranet.

5. The process of building scenarios, which requires the user’s active cognitive engagement, is an excellent learning process.

## 8. Conclusion

The prototype system reported in this research adopts a design focus that is different from that of the current decision support systems. Rather than focusing on the executive’s information need on ‘‘critical success factors’’ and the need for specific decision support, this research emphasizes the need to support the executives’ thinking process. The threemode prototype system was tested in a two-phase case study involving six small business executives. The findings provide some initial evidence that the system could be a valuable cognitive support tool after further development.

This research is only an initial investigation into the cognitive aspect of decision support. The applicability issues need to be addressed further. The preliminary assessment reported here does not allows us to draw a confident conclusion due to the small sample size from small businesses.

The prototype system is not robust enough to handle all aspects of the proposed conceptual model. The obvious limitations of the prototype system include the following: (1) When the number of cases increases dramatically, the searching time for a case is likely to become quite long. The current key word search function employs a single-level index search method. When a user enters a key word, the system will conduct a comprehensive search for that word among all available cases. more efficient search method should be used in future development. (2) The number of constructs (nodes) that can be handled by the Cognitive Mapping subsystem should be increased from current 10. (3) The consistency check in the scenario subsystem requires the user to answer a series of questions, which is a cognitively demanding task on the user. Future research should look into the possibility of adding a knowledge base and having the system conduct an intelligent consistency check. It is worth noting that the traditional approach to the scenario consistency problem is to calculate scenario probabilities using cross-impact analysis [12]. The approach requires the user to assess a large number of conditional probabilities on event occurrences, which is both inaccurate and cognitively demanding on the user.

Additional future research opportunities include: (a) incorporating multimedia and virtual reality tech nology into case presentation and scenario building, (b) incorporating a case-based reasoning capability into the Case Memory subsystem, and (c) developing an intelligent agent for case retrieval.

## References

[1] T.S. Bateman, C.R. Zeithaml, The psychological context of strategic decisions: a model and convergent experimental findings, Strategic Management Journal 10 (1989) 59 – 74.

[2] D.A. Carlson, S. Ram, HyperIntelligence: the next frontier, Communications of the ACM 33 (3) (March 1990) 311 – 321.

[3] G. Donaldson, J.W. Lorsch, Decision Making at the Top: The Shaping of Strategic Direction, Basic Books, New York, 1983.

[4] H.J. Einhorn, R.M. Hogarth, Decision making: going forward in reverse, Harvard Business Review 65 (Jan. – Feb. 1987) 66 – 70.

[5] B. Fichhoff, P. Slovic, S. Lichtenstein, Knowing with certainty: the appropriateness of extreme confidence, Journal of Experimental Psychology: Human Perception and Performance 3 (1977) 552–564.

[6] B. Gilad, Business Blindspots, Probus Publishing, Chicago, 1994.

[7] C.W. Holsapple, A.B. Whinston, Decision support systems: a knowledge-based approach, West Publishing, St. Paul, MN, 1996.

[8] D.J. Isenberg, How senior manager think, Harvard Business Review (Nov. –Dec. 1984) 82–90.

[9] E. Jaques, A General Theory of Bureaucracy, Gower Publishing, Hampshire, England, 1976.

[10] R. Jervis, Perception and Misperception in International Politics, Princeton Univ. Press, Princeton, NJ, 1976.

[11] P.G.W. Keen, Value Analysis: Justifying Decision Support Systems, MIS Quarterly (March 1981) 1 – 16.

[12] C.W. Kirkwood, S.M. Pollack, Multiple Attribute Scenarios, Bounded Probabilities, and Threats of Nuclear Theft, Future 14 (6) (December 1982) 545 – 553.

[13] S.M. Lee, J.Q. Chen, A conceptual model for executive support systems, Logistics Information Management 10 (4) (1997) 154– 159.

[14] D. Michael, On Learning to Plan and Planning to Learn, Jossey-Bass, San Francisco, 1973.

[15] H. Mintzberg, The Nature of Managerial Work, Harper & Row, New York, 1973.

[16] A. Money, D. Tromp, T. Wegner, The quantification of decision support benefits within the context of value analysis, MIS Quarterly (June 1988) 222 – 236.

[17] S. Oskamp, Overconfidence in case-study judgments, in: D. Kahneman, P. Slovic, A. Tversky (Eds.), Judgment Under Uncertainty: Heuristics and Biases, Cambridge Univ. Press, New York, 1982.

[18] J.F. Porac, H. Thomas, Taxonomic mental models in competitor definition, Academy of Management Review 15 (2) (1990) 224 – 240.

[19] K.I. Primozic, E.A. Primozic, J. Leben, Strategic Choices, McGraw-Hill, New York, 1991.

[20] A. Ramaprasad, Cognitive processes as a basis for MIS and DSS design, Management Science 33 (2) (Feb. 1987) 139 – 148.

[21] J.F. Rockart, D.W. De Long, Executive Support Systems, Dow Jones Irwin, Homewood, IL, 1988.

[22] E. Russo, P.J.M. Schoemaker, Managing overconfidence, Sloan Management Review (Winter 1992) 7 – 17.

[23] C.R. Schwenk, Cognitive simplification processes in strategic decision making, Strategic Management Journal 5 (1984) 111 –128.

[24] P.M. Senge, The Fifth Discipline, DouleDay and Currency, New York, 1990.

[25] W. Torbert, The executive mind: an interview, Planning Review (Sept. 1985) 24 – 27.

[26] E. Turban, Decision Support and Expert Systems, 4th ed., Prentice Hall, Upper Saddle River, NJ, 1995.

[27] H.J. Watson, C.G. Harp, G.G. Kelly, M.T. O’Hara, Soften up, Computerworld 26 (42) (1992) 103.

[28] S.B. Yadav, D. Khazanchi, Subjective understanding in strategic decision making, Decision Support Systems 8 (1992) 55 – 71.

[29] L.F. Young, Right-brained decision support systems, Database 14 (4) (1983) 28 – 36.

[30] R.W. Zmud, Supporting senior executive through decision support technologies: a review and directions for future research, in: E.R. McLean, H.G. Sol (Eds.), Decision Support Systems: A Decade in Perspective, Elsevier Science Publishers, North-Holland, Amsterdam, 1986.

![](/api/attachments/5GW3TT8Y/fulltext/images/77a92b96c9cef052f77b0bacea92f8e0397a9b527e30af82873b58d78339550f.jpg)

Jim Q. Chen is an associate professor of Business Computer Information Systems at St. Cloud State University. His current research interests include Web application development methodologies, E-commerce, and executive decision support systems. His recent publications appeared in Journal of Internet Commerce, Information Systems Management, Marketing Management Journal, Logistics Information Management, Journal of Computer Information Systems,

Review of Accounting Information Systems, Total Quality Management, among other journals.

![](/api/attachments/5GW3TT8Y/fulltext/images/8287e8847d729c0ab1df08b82c10b7a3a4eed5648581b7b09e1f02e54143fbe4.jpg)

Sang M. Lee is currently the University Eminent Scholar and Management Department Chair at the University of Nebraska-Lincoln. His research interests include IT-supported knowledge management infrastructure, competitive strategies in the digital economy, global business, and multiple objective decision support. He has published more than 50 books and 180 journal articles, mostly in MIS, POM, global business, and management science. He is a Fellow of the Academy

of Management, Decision Sciences Institute, and Pan-Pacific Business Association. He served as President of DSI and is currently President of the Pan-Pacific Business Association.
