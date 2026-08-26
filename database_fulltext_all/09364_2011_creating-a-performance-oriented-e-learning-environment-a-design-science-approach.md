---
otero_id: 9364
otero_key: "ETHQPNFC"
title: "Creating a performance-oriented e-learning environment: A design science approach"
authors: "Minhong Wang; Doug Vogel; Weijia Ran"
year: "2011"
journal: "Information & Management"
doi: "10.1016/j.im.2011.06.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Creating a performance-oriented e-learning environment: A design science approach

Minhong Wang <sup>a,</sup>\*, Doug Vogel <sup>b</sup>, Weijia Ran <sup>a,c</sup>

<sup>a</sup> Faculty of Education, The University of Hong Kong, Hong Kong

<sup>b</sup> Department of Information Systems, City University of Hong Kong, Hong Kong

<sup>c</sup> College of Computing and Information, State University of New York, Albany, NY, United States

## A R T I C L E I N F O

Article history: Received 12 July 2010 Received in revised form 15 February 2011 Accepted 5 June 2011 Available online 5 July 2011

Keywords: E-learning Design science Workplace Performance Ontology Intelligent agent

## A B S T R A C T

E-learning is now being used by many organizations as an approach for enhancing the skills of knowledge workers. However, most applications have performed poorly in motivating employee learning, being perceived as less effective due to a lack of alignment of learning with work performance. To help solve this problem, we developed a performance-oriented approach using design science research methods. It uses performance measurement to clarify organizational goals and individual learning needs and links them to e-learning applications. The key concept lies in a Key Performance Indicator model, where organizational mission and vision are translated into a set of targets that drive learning towards a goal of improving work performance. We explored the mechanisms needed to utilize our approach and examined the necessary conceptual framework and implementation details. To demonstrate the effectiveness of the approach, a prototype workplace e-learning system was developed and used to evaluate the effectiveness of our approach.

\- 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Organizations face a permanent changing environment due to new challenges such as globalization, economic pressures, and the changing nature of work. To be successful, employees must learn to cope with such changes. E-learning is being used by many organizations, especially SMEs but most applications are performing poorly and employees are not motivated to learn new methods. Thus significant gaps exist between corporate interests and learner needs when e-learning is provided. Individuals generally do not feel that e-learning is helpful since the knowledge learned does not help improve their work performance. Indeed, e-learning is generally implemented without considering the organizational vision and mission. As a result, most e-learning applications fail to meet user needs and ultimately fail to serve the organization’s quest for success in the knowledge economy.

Moreover, e-learning systems tend to focus on technical issues and ignore pedagogical and organizational issues necessary for effective e-learning. Most applications lack a sound pedagogical underpinning and fail to understand the learning behavior in an organizational and social context [14]. The dominance of technology-oriented approaches makes e-learning practice less goal-oriented, and thus they are perceived as being poor in quality.

A further review of the root cause of the problem reveals that much e-learning research is based on formal courses in educational institutions. Corporations as learning arenas are different from schools, although educational institutions are extending their reach to workplaces by introducing new pedagogical models such as problem-based learning, project learning, and case studies. Workplace learning is built on practical tasks and work situations that meet organizational goals. Learning in the workplace takes place in the context of use and application, and the result often remains implicit and embedded in work practices. Moreover, learning is more collaborative in workplace settings, where sharing individual knowledge with co-workers is an important part of the learning environment.

To solve this problem, pedagogical principles and organizational learning theories should provide the basis for the design and implementation of e-learning applications in work environments; indeed a systematic and rational approach is vital. This underscores the need for structuring learning activities to meet corporate interests, individual needs, work performance, and the social context. The development of e-learning in the workplace should consider the alignment of individual and organizational learning needs, the integration of learning and work, and communication between individuals.

In our study, we provided a performance-oriented approach intended to improve e-learning development in the workplace. We used performance measurement to clarify organizational goals and individual learning needs, and linked them to e-learning applications. The key idea lay in a Key Performance Indicator (KPI) model, where the organizational mission and vision were translated into a set of performance targets that drive learning towards the goal of improving work performance. The model therefore helps an employee identify performance measures for his/her position, capabilities needed to be developed to improve performance, knowledge about the capability, and learning resources needed. This conceptualization helps accomplish organizational goals by showing a clear picture of what is important and what is needed to learn it.

To implement the KPI-oriented learning environment, ontology- and intelligent agent-based functionalities were added to the e-learning system. Ontology is a formal representation of a set of concepts and their relationships in a domain; it uses machine languages and semantic annotations to achieve this [8]. We used ontology for an explicit representation of the KPI model, as a foundation for guiding performance-oriented learning. Intelligent agents act autonomously and perform tasks that depend on the context and user preferences. A set of intelligent agents was developed in our study to assist learners perform adaptive learning activities. With the support of these technologies, real-time personalized instructions and recommendations were continuously generated and sent to participants to facilitate and direct their learning processes to improve their work performance. The KPI model can also be used to identify each individual’s work context, expertise, and proficiency, as well as to organize knowledge assets, with a view to facilitating knowledge sharing and social networking in a learning community.

Our study aimed at improving organizational performance through the design and implementation of an IT artifact for elearning in the workplace. Two research questions were examined: (1) how should an e-learning system be designed to align learning with work performance in the workplace? and (2) to what extent is such an e-learning system effective for learning in the workplace?

## 2. Literature review

## 2.1. E-learning

E-learning focuses on the use of computer and network technologies to create and deliver a rich learning environment that includes a broad array of instruction, information resources and solutions, with a goal of enhancing individual and organizational performance. Here we use the term e-learning to encompass Computer-Based Learning, Computer-Based Training, Technology-Enhanced Learning, Technology-Mediated Learning, Web-Based Education, or Virtual Learning Environment. E-learning has attracted considerable interest by providing a variety of benefits to learners, education institutions, and organizations by: removing barriers of time and space in the development of knowledge and skill; providing just-in-time learning, convenient access, and flexible learning processes; enabling real-time content updating while avoiding information overload; reducing travel, off-site training costs and time away-from-the-job; and facilitating the interconnectivity of people for knowledge transfer [11].

Many schools have been using course management software (e.g., Blackboard, WebCT, and Moodle) to complement traditional classroom-based instruction. Many empirical studies have been conducted to demonstrate how IT supports learning by improving students’ learning outcomes, enhancing information literacy of students, and increasing effectiveness of education management. Despite the variation in research findings, there has been a consensus that substantial gains in student attainment are achievable if the use of IT in schools is planned, structured, and integrated effectively.

To improve existing e-learning applications, smart learning environments must, however, to provide personal services to help a learner use, manage, and interact with the learning system. A number of studies have investigated the use of intelligent tutoring techniques, such as personalized learning interfaces and adaptive learning. These efforts have generally emphasized technology development but had little concern for effective instruction or pedagogy to enhance learning performance.

## 2.2. Workplace learning

This field – also known as Training and Development, Human Resource Development, Corporate Training, and Work and Learning – can be defined as the means, processes, and activities in the workplace by which employees learn basic skills, high technology, and management practice that can be immediately applied to their jobs, duties, and roles in the firm. Indeed, to compete and keep up with changes, organizations require effective ways to update their workforce’s skills and knowledge.

The rapid development of ICTs has made it necessary for organizations to provide new ways of developing workforce competence and enhancing human resource management [6]. However, most e-learning applications have been developed primarily for school learning programs, and ignore the special features that are needed in work situations. Generally the complexities of interaction between e-learning and organizations have been underestimated. To leverage the potential of e-learning for sustaining effective change, a sound business and peoplecentered strategy is essential.

## 3. Design science research methodology

The objective of our study was to design, implement, and evaluate a KPI-oriented e-learning system that could address the special problems of existing workplace situations. A design science research methodology was adopted to investigate this designbased problem. Design research creates, builds, and evaluates innovative artifacts to help solve identified problems [5]. The goal of design researchers then moves beyond offering explanations of phenomena to designing interventions for solving problems [10]. Design science research is increasingly recognized as a companion to behavioral research in business [4] and education fields [1].

Design-based research is a systemic but flexible methodology aimed at improving practices through iterative analysis, design, development, and implementation in real-world settings. It has been welcomed in education, especially in technology-enhanced learning environments [1]. Learning scientists move beyond simply observing to becoming involved in using developing technological tools and curriculum models to improve courseware and generate evidence-based facts about learning. Such research becomes important in situations where complex and ambitious educational reform policies are ill specified and where the implementation process is uncertain.

Design-based research requires identification of a relevant organizational problem, development and presentation of an artifact, its evaluation to assess its utility,articulation of the value added tothe knowledge base, and explaining its implications. It requires not a single, but a series of methodological approaches such as surveys, case studies, interviews, evaluations, and comparative analyses.

Since it is infeasible to develop a learning system applicable to all business organizations, we used a case study approach in our research to investigate the mechanism of developing the artifact from both an understanding-oriented and an action-oriented perspective. The development was conducted in a real-world setting, with close collaboration with the stakeholders.

## 4. Analysis of requirements

## 4.1. Understanding workplace e-learning and its requirement

The four fundamental elements of a workplace learning environment are: the learners, the learning content, the social context, and other major stakeholders such as the organization and the society. An effective workplace learning application should take into consideration these elements and their interactions.

First, employees are adult learners with distinct learning characteristics. Even when assigned an identical job position, employees have different learning needs and expectations due to their different educational backgrounds, work history, and learning performance.

Second, learning is linked to organizational goals and needs. It depends on organizational systems, structures, policies, and institutional forms of knowledge.

Third, learning content is contextual and dynamic because knowledge in the workplace is disseminated within the organization and arises from employees’ daily activities and interaction with the work environment.

Fourth, learning can be understood as social networking between learners, which allows transfer and sharing of knowledge among individuals, groups, and organizations.

Thus learning activities in the workplace should follow corporate interests, individual needs, work environment, and the social context; workplace learning applications should consider the alignment of individual and organizational needs, the integration of learning and work context, and the interaction among peers.

## 4.2. Proposed performance-oriented approach

We decided to adopt a performance-oriented approach in our study. We noted at the start that there is no doubt that the goal of e-learning in the workplace is to enhance individual and organizational performance, but that there is a lack of concrete strategy or approach for achieving this goal.

In our study, we used a KPI-based approach. Performance measurement in an organization is used to improve the overall performance by setting objectives, assessing performance, analyzing performance data, and utilizing performance results. KPIs are metrics used to help the organization define and measure progress towards organizational goals. A set of KPIs involve the measures of all aspects of organizational and individual performance that are critical to the success of the organization.

KPI can help employees set up rational learning objectives according to their knowledge gap. It can be used as a systematic way of organizing and managing learning resources and activities with work context and performance requirements. Further, KPI can be used to identify each individual’s work context and expertise to support social learning and knowledge sharing to improve work performance.

## 4.3. Related work

Studies refer to competency-based learning, in which learning is driven by developing specific competencies for dealing with needs and challenges. This method seeks to identify the combination of skills and knowledge needed to perform specific tasks, and is intended to facilitate communication between education and labour markets. While the competency-based method is being introduced into e-learning system applications, current work has been limited to organizing learning content around the competencies that are usually specified on an ad hoc basis, without consideration of performance as its outcome. Current work has also underestimated the complexity of the interactions between employees and organizations in learning [3]. Our study therefore goes beyond learning content by integrating individual and organizational learning needs and performance measurement in e-learning applications using a KPI-oriented learning model.

## 5. System design

We developed a workplace e-learning system for use in our study. Organizational strategy, structure, and job system were incorporated into the system design. As it was infeasible to make the design applicable to all company situations, we used a case study approach to determine the mechanism needed to develop the approach. The system was designed for the Testing Unit of PEANUT SOFTWARE, a medium-sized company in Mainland China, which sells and markets technology products including consumer electronics, computing, and communication products. There are four departments in the company: Development, Customer Service, Consulting, and Back Office. The Development department consists of two units: R&D and Testing. Testing is, of course, essential for evaluating the quality of software products by identifying defects and problems. The design of the system is based on discussion with the stakeholders (software testers, the manager of the Testing Unit, its training manager, and company executives).

## 5.1. The agent-based system architecture

To support and enhance e-learning environments, artificial intelligence and cognitive science have been included in developing modern systems. There is increasing interest in the use of intelligent agent technology [9] to support the user in carrying out such tasks as information retrieval, activity scheduling, and adaptive decision making; these differ from conventional programs because they can act autonomously and perform tasks with consideration given to context and user preference [15]. In learning environments, intelligent agents are a set of tools linked with other applications and databases running within one or more computer environments. They may support learning processes as personal tutors, academic counselors, mentors, or peers. They play a major role in making e-learning suit the needs of learners by customizing the learning content and process based on the learners’ background, needs, and preferences [2].

An intelligent learning system typically has four parts: the domain expert, learner, pedagogical, and interface modules. Thus, the system in our study consisted of a set of agents: the Learner, Training Manager, Domain Expert, and Instruction Agents, as shown in Fig. 1.

The Learner Agent enables a learner to maintain personal information, assess his or her performance, access and evaluate learning resources, share materials, etc. The Domain Expert Agent enables an expert to maintain the KPI model, process and maintain materials, generate and update objects based on the materials, and coordinate discussions. The Training Manager Agent enables the training manager to maintain learners’ profiles and the assessment base, define instructional rules, etc. The Instruction Agent guides individual learning processes according to the learner’s performance gap and progress in reducing it. Its functionalities include measuring and analyzing performance, managing and monitoring learning processes, adapting learning activities and resources to individuals, and delivering personalized learning instructions and alerts.

The design of the Instruction Agent involves the following modules:

\- The ‘‘domain knowledge’’ which states the goal of learning and can be used to evaluate the knowledge gap of an individual learner.

\- The ‘‘learner module’’ which captures or detects the learner’s background, learning goal, and current knowledge status. It is essential in providing personalized learning advice to individuals.

![](/api/attachments/ETHQPNFC/fulltext/images/75279b087d8823410e451794c90e625b48b4e6128fa6e7ceab749a8e3b9cd921.jpg)  
Fig. 1. Agent-based system architecture.

\- The ‘‘pedagogical module’’ which gives the strategies and instructions to guide or coach learners.

For interactions between the user (learner, expert, or training manager) and the software agents in the learning system, relevant interfaces must be developed.

## 5.2. The ontology-based semantic learning environment

We used ontology-based technologies to implement the concept of performance-oriented e-learning. Ontology provides a formal and explicit specification of a shared view of a domain; it creates a machine-readable mechanism for communication between humans and computers by providing a semantic annotation of the learning resources and activities, reusing and combining course materials, and enabling better searching and navigation. E-learning materials annotated with semantic tags enable an intelligent agent to reason about e-learning content and organize it into customized courses according to the learner’s profile and needs.

In our study, ontology was used to translate the KPI-oriented learning environment into a machine-readable format. KPI was used as a systematic scheme to direct learning targets and activities and organize and manage learning resources within the work context. The main concepts in this scheme include Position, KPI, Capability, and Knowledge Component (KC). Based on these four and their relations, the KPI learning ontology was constructed. As shown in Fig. 2, an employee in a Position is assessed by a set of KPIs required by the organization; to improve the performance relevant to a specific KPI, the employee must have (or learn) all relevant Capabilities, represented as a number of KCs. In addition, recursive relationships between different KCs and different positions are determined. For example, one KC can be linked to another because it has a relation such as ‘‘part of’’, ‘‘sequential’’, or ‘‘inhibitor’’; a position (e.g., junior tester) can occur before another position (e.g., senior tester). These relationships are labeled as (a), (b), (c), (d), (e), (f), and (g), with specifications and illustrations provided in Table 1.

## 5.3. Design of KPI-oriented learning ontology

To develop the proposed system, a KPI-oriented learning ontology was developed for the Testing Unit of PEANUT SOFTWARE. For performance measurement to be effective in workplace learning, the measures or indicators themselves must be understood, accepted, and used by the employees as well as their managers. Therefore, the building of the KPI-oriented system needed integration of several strategies as well as tight cooperation among managers and employees at different position levels. The construction of the ontology in this study was based on intensive collaboration between the system designers, training managers, and domain experts of the company. IEEE standards for software testing were used in developing the ontology.

The KPI framework was designed to coincide with the organization’s structure and job system. It consisted of three levels: the organization; the business unit; and the position. KPIs at the organizational level were defined according to the business goals and strategies of the organization. Based on these organizational KPIs, the unit level KPIs for each business unit were derived. Then the KPIs at the position level for each job position within the unit were defined. Here we focus on KPIs at the position level.

![](/api/attachments/ETHQPNFC/fulltext/images/50cb29c3d335b8ac4c7f687d43f01cb1c2eb4c566b75c808436fbc2034c05db5.jpg)  
Fig. 2. Main concepts with relation cardinalities.

Table 1  
Concepts and their relationships.

<table><tr><td>Label in Fig. 2</td><td>Name of relation</td><td>Presentation of relation</td><td>Description of relation</td></tr><tr><td>(a)</td><td>Prior position</td><td>Prp (a,b)</td><td>Position a is a prior position of Position b</td></tr><tr><td>(b)</td><td>Has indicator</td><td>Hind (a,b)</td><td>Position a has a KPI b for performance assessment</td></tr><tr><td>(c)</td><td>Needs capability</td><td>Cap (a,b)</td><td>To improve KPI a, capability b is needed</td></tr><tr><td>(d)</td><td>Requires knowledge component</td><td>Rkc (a,b)</td><td>To develop capability a, KC b is required</td></tr><tr><td>(e)</td><td>Part of</td><td>Par (a,b)</td><td>KC a is a part of KC b</td></tr><tr><td>(f)</td><td>Sequential</td><td>Seq (a,b)</td><td>KC a is a prerequisite of KC b</td></tr><tr><td>(g)</td><td>Inhibitor</td><td>Inh (a,b)</td><td>If KC a is learned, then KC b need not be learned, and vice versa</td></tr></table>

![](/api/attachments/ETHQPNFC/fulltext/images/955830055b177dbb6c97e4a10c79625e353f8d6f6511fc1dd9cef501b6684cc9.jpg)  
Fig. 3. Learning ontology for the Testing Unit.

PEANUT SOFTWARE defined Productivity, Quality, and Organizational Capacity Construction as its three organizational KPIs. The Testing Unit must evaluate the quality and find bugs in its software products. Therefore, the Testing Unit defined Bug Found and Bug Returned as two unit KPIs dealing with Productivity, Quality, and Organizational Capacity Construction. Based on the defined unit KPIs, the manager and experts of the Testing Unit defined KPIs for each position (Junior Tester, Senior Tester, Test Specialist, and Lead Test Specialist).

Bug Found and Bug Returned were specified as the KPI items for the Junior Tester position. To improve their performance on Bug Found, the employees needed to develop the capabilities such as Bug Reporting, etc. To develop this capability, the employees had to know or learn relevant knowledge, such as Test Fundamentals and Defect-based Metrics. The main responsibility of a Senior Tester was to design test cases, therefore the corresponding KPIs were defined as Test Coverage and Reusable Test Case Rate. In order to improve the performance of Test Coverage, employees had to develop capabilities about Programming and Test Case Design. To develop the capability of Test Case Design, employees had to have or learn knowledge about Specification-based Design, Black-box Design, etc. Fig. 3 presents such details only for the Junior Tester and Lead Test Specialist positions.

Based on this KPI framework, each employee was required to meet a set of KPI values in assessing his or her job performance; to improve their KPI values, each employee assessed his or her knowledge status according to his or her position by taking tests or quizzes; based on the these results, the system recommended necessary personalized learning resource or activities. For impartiality and objectivity reasons, the company used 360 degree feedback to assess the employee’s performance. Thus a set of KPI values was calculated to evaluate the employee’s work performance.

## 5.4. The performance-oriented learning process

The goal of performance-oriented learning can be achieved by setting up rational learning objectives, accessing relevant knowledge artifacts, and directing individual learning processes through an appropriate reasoning mechanism. The ontology helps the employee identify KPIs required by the organization for his/her position, relevant capabilities needed by him or her to improve the performance, and the KCs to be learned to achieve success. Thus the learner’s knowledge gap should be based on expected results. In addition, relevant learning instructions should be specified to allow flexibility in using the system. The performance-oriented learning process is outlined in Fig. 4.

An employee’s job performance is evaluated and recorded as a set of KPI values. If any KPI value does not reach its required level, an improvement is suggested. Based on the learning ontology, the relevant KCs to be improved are generated and a customized assessment package is produced to test the employee’s knowledge. If the assessment results are consistent with the KPI values, a personalized learning syllabus is generated for the employee; otherwise, he or she will be told to consult a domain expert. A number of relevant learning objects are thus recommended to the employee and quizzes are provided for self-assessment. If the employee is not able to pass the required quiz within a reasonable time frame, additional learning objects or suggestions are provided.

In addition to the individual learning process, social networking is also provided. Learners are able to share and evaluate the learning resources, discuss their problems or experiences at fora, and conduct peer evaluation of work performance. Each employee is provided with a set of KPI values that indicates his/her expertise and proficiency level, stored in his or her profile. Learners and domain experts can reach one another based on KPI identifications and contribution to the learning community.

## 6. System implementation

To demonstrate the effectiveness of our approach, we built a prototype of the workplace e-learning system. A set of screenshots is presented in Fig. 5. The learning ontology is shown as a graph for easy communication of the learning context (lower left). By clicking on the KC in this graph, the learner is able to locate the learning objects linked to a specific KC. These, associated with the organizational structure and position system, are created and maintained by the training manager or domain experts (upper left). Based on the ontology and the learner’s situation (position, KPI values, and assessment result) the Instruction Agent may suggest a learning syllabus with a corresponding learning process (center). The learner then takes a quiz to assess his/her knowledge needed for a specific KC (lower right). Moreover, learners are able to contribute, share, and evaluate learning resources as well as participate in group discussions or communications (upper right). During social communications, learners are able to locate peer learners or experts, each profiled by their background, expertise, and contribution to the community.

![](/api/attachments/ETHQPNFC/fulltext/images/433f74c255f3560c2a0e3a5929c25a85b4af4e9283d99c36950c8f169b9b709c.jpg)  
Fig. 4. The performance-oriented learning process of the Instruction Agent

![](/api/attachments/ETHQPNFC/fulltext/images/966094c9581f5b13232a5d97808e9606a06f625a8d2e215f32811e6efb892289.jpg)  
Fig. 5. Screenshots of the prototype.

In this prototype, OWL-DL (IBM’s OWL Description Language) was used to define the KPI-based learning ontology. To support the reasoning process, instruction rules were bound to the ontology using DL safe SWRL (Semantic Web Rule Language), via using OWL-API to access Pellet [12].

To implement the ontology, Prote´ge´ together with ‘‘SWRL tab’’ and ‘‘Jambalaya tab’’ plug-in were employed in this study. Prote´ge´ is a free open-source ontology editor developed by Stanford Medical Informatics. Prote´ge´ holds a library of plug-ins that adds more functionality to the environment. ‘‘SWRL tab’’ is a plug-in for Prote´ge´, which provides a SWRL Editor that supports the editing of SWRL rules. ‘‘Jambalaya tab’’ is another plug-in for Prote´ge´ to help visualize the OWL ontology.

## 7. Evaluation

Our evaluation focused on the effectiveness of the proposed approach. Therefore, we used experimental and comparative analysis. Experiments were conducted to compare the developed KPI-oriented e-learning system (System A) with a traditional e-learning system (System B), which has similar functions in terms of user management, learning resources, assessment management, and communication tools, but without KPI-oriented facilities. The interfaces of the two systems were also similar to ensure that no other design-related factors affect usage and perception of the systems.

The evaluation examined the effectiveness of an e-learning system developed for a workplace setting. We evaluated it based on the Kirkpatricks’ model [7], which evaluates a training program at four levels:

– Reaction measures how participants react to the training program (their satisfaction with the system). This is the commonly used measure of training effectiveness.

– Learning measures the learner’s improved knowledge or enhanced skills from attending the training program.

– Behavior measures the change of behavior caused by the training program.

– Result measures organizational and individual outcome due to the training program, such as increased production, improved quality, shortened processing time, and decreased cost. Since we had no opportunity to measure the results to the company in our study, we asked the learners and managers about their anticipated results.

To evaluate the developed system, 24 employees were invited to participate in the experiments. To collect data on system evaluation, tests, questionnaires, and interviews were used, The data included learning-outcomes obtained through pre-tests and post-tests, as well as participants’ perceptions obtained through questionnaires and interviews.

Questionnaire items were developed based mainly on the Kirkpatricks’ model, as outlined in Table 2. The participants evaluation of the system was mainly based on their perception as measured on a Likert scale (from 1 strongly disagree to 7 strongly agree). Pre-test and post-test questions were based on certification examinations from software testing articles as adjusted by the domain experts.

Table 2 Evaluation framework.

<table><tr><td>Level</td><td>Aspect</td></tr><tr><td>Reaction</td><td>The system meets my learning requirementThe system provides satisfactory functionalities for learning</td></tr><tr><td>Learning</td><td>The system improves knowledge learning and skill developmentPre-test score and Post-test score</td></tr><tr><td>Behavior</td><td>The system helps integrate learning with work performanceThe system supports social learning with peers</td></tr><tr><td>Result</td><td>The system helps improve my work performanceThe company gets benefits from using this system for employee training</td></tr></table>

## 7.1. Participants

24 employees who were working or had previously worked with the Testing Unit of the company participated in the experiments. Some had been involved in the early stage of the project, providing suggestions on system design. They were divided into two groups of 12—the treatment group used the KPI-based system while the control group used the traditional system. 58.8% of the participants had worked for less than 5 years, and 35.3% from 5 to 10 years; 29.4% of them had used one e-learning system, 5.9% had used more than three, and 29.4% had used none. There was no significant difference between the groups in their software industry work experience and number of e-learning systems previously used.

## 7.2. Procedures

In view of tight schedules of the employees and the company, the evaluation focused primarily on users’ perception towards the system based on their use of it during the experiment period. It has been found that learner reaction has a large impact on learning in technology-mediated learning environments [13]. While employees may continue to use the system after the experiments, it takes longer to ascertain the effect of the system on learners and the company.

Since there were only a small number of participants, the findings from questionnaires may not be generalizable. Interviews were therefore arranged in an attempt to provide qualitative and interpretive analysis. Moreover, a supplemental experiment was added by swapping the systems between the two groups of participants and asking them to give their preference.

Due to the tight schedule, the time for the participation was limited to four weeks for the main and two weeks for the supplemental experiment, plus another two weeks for pre-test, post-test, surveys, and interviews. Before this, several months had been spent on communication and discussion with the participants for analysis of user requirements in system design and development.

The evaluation process was divided into four stages. First, all the participants finished the pre-test. Second, after using the system for four weeks, participants completed the post-test and the main questionnaire for evaluation of the system on Reaction, Learning, Behavior, and Result level. Third, the two groups were asked to swap systems and use the systems for two weeks; at the end of the stage, the supplemental questionnaire was used to determine participants’ preference towards the two systems concerning all the aspects of the system. Finally, interviews were conducted for qualitative feedback from the participants.

![](/api/attachments/ETHQPNFC/fulltext/images/53c070aef269552915bff415f6610703de7b7d3025782e11a9c0826f7f5689ff.jpg)  
Fig. 6. Evaluation of the learning systems (main evaluation).

## 7.3. Results and findings

The results obtained from the main experiment are shown in Fig. 6. The KPI-oriented system was perceived to be more effective in terms of meeting individual learning requirement and functional support for learning (Reaction). It was perceived to be more helpful to learners in obtaining knowledge and skill (Learning), and was perceived to be more helpful in enabling learners to integrate learning into practice and transform individual learning into collaborative learning (Behavior), while being perceived to lead to better outcomes in improving work performance and bringing benefits to the company (Result). On the other hand, the pre-test and post-test scores indicated that there was no difference between the two groups. In addition, the KPI-oriented system was not perceived as being more effective than the other system.

The supplemental evaluation was conducted on 20 of 24 participants. The result of this test is presented in Fig. 7. A majority of the participants preferred the KPI-oriented learning system for all its aspects. Follow-up discussions with the participants showed that many of them felt that they would be able to make a more appropriate evaluation after comparing both systems.

## 7.4. Findings from the interviews

The 20 final participants were interviewed. The interview question involved the participant’s reaction towards the KPIoriented e-learning system. Each participant was interviewed individually via telephone or Windows Live Messenger. The interview lasted approximately half an hour. To ensure reliability, we conducted 2–3 interviews with each participant. The findings from the interviews were organized in terms of the role of the interviewee (employee, expert, or training manager).

Most of the employees were concerned about the learning objective, learning content, social interaction, and communication functions supported by the KPI-oriented system. In terms of learning objective, the participants expressed strong preference to the KPI-oriented system. They felt that learning objectives were clearly set up in the system, in line with the hierarchy of the job system. This provided them with information about different job positions at junior and senior levels and key capabilities required for these positions. One participant said ‘‘With the help of the system, it became very convenient for me to check my job requirements.’’ In terms of learning content, they felt that comprehensive and abundant learning materials (cases, work tips, and experiences) were crucial to an e-learning system.

![](/api/attachments/ETHQPNFC/fulltext/images/2ff1f24c91c1b8a79353dc5fc77d10ffc090623dc00121b2b0f7d303a7724f68.jpg)  
Fig. 7. Preference on the learning systems (supplemental evaluation).

Further, most participants reported that a clear and flexible classification scheme of learning materials was very important. For example, some participants recommended that learning materials be organized around actual projects and be updated for new projects. One participant said ‘‘We always need to learn something when there is a new project. Today, I may need the knowledge relevant to multi-language testing, but tomorrow, I probably have to search for knowledge in biology, if we receive an order from a biological company.’’ In terms of social interaction and communication functions, participants felt that they can motivate learners. All employees stated that they had more opportunity to learn from others by attending discussions and querying experts via the system. One participant said ‘‘Once I had done something really well, there was a way for me to contribute and share.’

The experts were more concerned about how an e-learning system could help employees learn, especially in a social context. They felt that defining the capabilities needed for each job position, identifying the knowledge gap of individuals, and providing timely and useful help to learners were most important components. This would help decrease the e-learning quit rate of employees. Moreover, they stressed the importance of providing convenient and instant help in solving learning problems. In view of social learning context in the workplace, the experts preferred the system as it supported knowledge sharing to improve work performance.

They believed that the construction of the capability framework was an evolving process and that cooperation was needed from both designers and users of the learning system. They suggested that system designers should first define the initial framework of the capabilities required for the positions in the workplace and refer to existing industrial standards. Then experts in the workplace should modify the framework according to their experience and the context of the workplace. Finally, the framework should be continuously reviewed and modified.

With respect to the training managers, their greatest issue was cost. They expressed their preference of e-learning systems to traditional training in classrooms as saving the expense on formal training programs. The managers said ‘‘We don’t have many senior experts and have to control the training budget. Therefore, we put effort into learning from each other in the department.’’ One manager said ‘‘I think the prototype system can satisfy our training requirements.’’ Training managers also favored the proposed performance-oriented approach. They said that the assessment information of employees was helpful for managers to check employees’ learning status and provide support.

## 8. Conclusion

The use of technology to deliver learning has become a trend in industry, and has been termed ‘e-learning.’ Our study addresses the problem by recommending that workplace e-learning should consider: (a) the alignment of individual needs and organizational interests, (b) the connection between learning and work performance, and (c) the communication between individuals in a social learning context.

To achieve this, we considered the design and evaluation of a performance-oriented approach for developing e-learning systems. To demonstrate and evaluate our approach we developed a

KPI-based learning system. Using it, experiments were conducted to evaluate the effectiveness of the approach. The results indicated positive feedback and comments from learners, experts, and training managers.

For technology-oriented audiences, the key contribution of this work is investigating the underlying mechanism of a performanceoriented e-learning environment by modeling and implementing the KPI framework, as well as by reasoning and guiding individual and social learning processes according to the learner’s performance gap and learning progress.

For management-oriented audiences, this study has presented the importance of understanding and aligning the needs and requirements towards learning technology from the viewpoints of both organizations and employees. Although e-learning provides a new way to deliver training programs, it cannot remain that way if it is not able to support the stakeholder’ needs. To leverage the potential of e-learning, a sound business and people-centered strategy is essential. We proposed a performance-oriented approached using KPI to clarify and align the learning needs of organizations and employees and drive the learning process towards a goal of improving performance.

The generalizability of our findings should be noted that the study was conducted in a software company and within the software testing section; however, the approach can be applied to other organizational contexts. The construction of performanceoriented learning ontology needs shared conceptualization of the stakeholders and professional knowledge from domain experts.

There are, of course, limitations that must be noted: the evaluation of the system was mainly on users’ perception of the system based on surveys and interviews. Although learner reaction was found to have an impact on learning, the final outcome reflected in individual and organizational performance requires more than a case study such as this, with a sizable system and many more participants.

## Acknowledgements

The authors thank the editor and reviewers of Information & Management for their constructive comments on this paper. This researchis supported byaUGCGRFGrant(No.717708)fromtheHong Kong SAR Government, a Seeding Fund for Basic Research (No. 200911159142), and a seed Fund for Applied Research (No. 201002160030) from The University of Hong Kong. The authors also thank Professor Haijing Jiang for his valuable support to this project.

## References

[1] S. Barab, K. Squire, Design-based research: putting a stake in the ground, The Journal of the Learning Sciences 13 (1), 2004, pp. 1–14.

[2] M.B. Blake, J.D. Butcher-Green, Agent-customized training for human learning performance enhancement, Computers and Education 53 (3), 2009, pp. 966–976.

[3] B. Cheng, M. Wang, S.J.H. Yang, J. Kinshuk, Peng, Acceptance of competency-based workplace E-learning systems: effects of individual and peer learning support, Computers and Education 57 (1), 2011, pp. 1317–1333

[4] S. Gregor, D. Jones, The anatomy of a design theory, Journal of the Association of Information Systems 8 (5), 2007, pp. 312–335.

[5] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information research MIS Quarterly 28 (1), 2004, pp. 75–105.

[6] Z. Hussain, J. Wallace, N.E. Cornelius, The use and impact of human resource information systems on human resource management professionals, Information and Management 44 (1), 2007, pp. 74–89.

[7] D.L. Kirkpatrick. I.D. Kirkpatrick. Évaluating Training Programs. 3rd ed., Berrett-Koehler Publishers, Inc., San Francisco, CA, 2006.

[8] C. Knight, D. Gasˇevic´, G. Richards, An ontology-based framework for bridging learning design and learning content, Educational Technology and Society 9 (1), 2006, pp. 23–37.

[9] X. Li, A.R. Montazemi, Y. Yuan, Agent-based buddy-finding methodology for knowledge sharing, Information and Management 43 (3), 2006, pp. 283–296.

[10] S.T. March, V. Storey, Design science in the information systems discipline: an introduction to the special edition on design science research, MIS Quarterly 32 (4), 2008, pp. 725–729.

[11] O.Z. Ozdemir, J. Abrevaya, Adoption of technology-mediated distance education: a longitudinal analysis, Information and Management 44 (5), 2007, pp. 467–479.

[12] E. Sirin, B. Parsia, B.C. Grau, A. Kalyanpur, Y. Katz, Pellet: a practical OWL-DL reasoner, Journal of Web Semantics 5 (2), 2007, pp. 51–53.

[13] T. Sitzmann, K. Brown, W.J. Casper, K. Ely, R.D. Zimmerman, A review and metaanalysis of the nomological network of trainee reactions, Journal of Applied Psychology 93 (2), 2008, pp. 280–295.

[14] P. Tynja¨la¨, P. Ha¨kkinen, E-learning at work: theoretical underpinnings and pedagogical challenges, The Journal of Workplace Learning 17 (5/6), 2005, pp. 318–336.

[15] M. Wang, H. Wang, From process logic to business logic—a cognitive approach to business process management, Information and Management 43 (2), 2006, pp. 179–193.

![](/api/attachments/ETHQPNFC/fulltext/images/4b7a7a03f808a985a75e8ff89ba043168b07b436b24136c965f6e13b278c1afb.jpg)

Minhong Wang is an Assistant Professor in the Faculty of Education, The University of Hong Kong. She received her Ph.D. in Information Systems from City University of Hong Kong in 2005. Her current research interests include e-learning, Web-based training and professional development, knowledge management, complex process management, and information systems. She has pub lished papers in Information & Management, Computers & Education, IEEE TransactionsonEducation,Educational Technology & Society, Expert Systems with Applications, Knowledge-based Systems, Journal of Knowledge Man agement, among others. She is the Editor-in-Chief of Knowledge Management & E-Learning: an Internationa

Journal (KM&EL), and serves on the Editorial Board of several international journals More details can be found at http://web3.edu.hku.hk/magwang/.

![](/api/attachments/ETHQPNFC/fulltext/images/62246726fe97f303f462299e9bae56dbb9f52ac3ed7174ab9d499afb9dc1d28d.jpg)

![](/api/attachments/ETHQPNFC/fulltext/images/c9095d72afb758e16717693aeeb5481021453e97b46abddda4588abd6266c334.jpg)

Doug Vogel is chair professor of information systems at the City University of Hong Kong and an AIS Fellow. He received his MS in computer science from U.C.L.A. in 1972 and his Ph.D. in information systems from the University of Minnesota in 1986. Professor Vogel’ research interests bridge the business and academic communities in addressing questions of the impact of information systems on aspects of interpersonal communication, group problem solving, cooperative learning, e-commerce and multi-cultural team produc tivity and knowledge sharing. Additional detail can be found at http://www.is.cityu.edu.hk/staff/isdoug/cv/.

Weijia Ran is a Research Associate at the Lab fo Knowledge Management & E-Learning, The University of Hong Kong. She received her M.Phil. degree from The University of Hong Kong. She is now pursuing her Ph.D. in State University of New York at Albany. Her research interests include e-learning in the workplace, knowledge management, and information systems in organizations.
