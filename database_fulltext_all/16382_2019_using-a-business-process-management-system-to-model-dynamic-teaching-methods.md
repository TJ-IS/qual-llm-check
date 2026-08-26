---
otero_id: 16382
otero_key: "5JS7S5UD"
title: "Using a business process management system to model dynamic teaching methods"
authors: "Fernando Enríquez; José A. Troyano; Luisa M. Romero-Moreno"
year: "2019"
journal: "The Journal of Strategic Information Systems"
doi: "10.1016/j.jsis.2018.07.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using a business process management system to model dynamic teaching methods

Fernando Enríquez<sup>⁎</sup>, José A. Troyano, Luisa M. Romero-Moreno

University of Seville, Department of Computer Languages and Systems, ETS Ingeniería Informática, Av. Reina Mercedes s/n, 41012 Sevilla, Spain

A R TLCLE LN EO

Keywords: Business process management Organizational change Educational technology system Rubric Gamification

## A B S T R A C T

Enterprise Information Systems are enjoying an extensive trajectory in the optimization of organizations worldwide, of which predominantly the Business Process Management (BPM) sys tems stand out for their great <sup>fl</sup>exibility. BPM models describe business work<sup>fl</sup>ows and are highly useful in detecting errors and bottlenecks and in identifying possible improvements. On the other hand, educational management software tools o<sup>f</sup>er a large number of functionalities, but have yet to take advantage of these techniques. Our main objective is to perform an empirical analysis in this unexplored area to evaluate the advantages of applying BPM in the implementation of innovative and dynamic teaching activities.

Using this methodology, we have designed RubricaSoft, a BPM system focused on providing dynamic educational processes. It automates multiple tasks, including peer evaluation, information integration and the management of deadlines. The results have been very promising from the point of view of the three axes upon which the evaluation has been carried out: satisfaction of students, improvement in academic results and increase in the productivity of teachers. In one of the processes, the time spent by the teacher has been reduced by 80% and student participation increased by 41%.

## 1. Introduction

The use of computer systems in education has provided a broad set of solutions in many areas. From speci<sup>fi</sup>c tasks such as simulators (Rutten et al., 2012) to global Learning Management Systems (LMS) (Watson and Watson, 2007), it has represented a major step forward for many educational environments, including primary schools, higher education establishments, and enterprise training programs. Although basic learning processes can be carried out without any technological help, it seems obvious that these tools o<sup>f</sup>er new opportunities, and represent a key element for the improvement of quality in education institutions (Tarí and Dick, 2016).

In the educational literature multiple contributions can be found regarding technology and education. Learning Management Systems such as Moodle<sup>1</sup> and Blackboard<sup>2</sup> are being broadly used, and, as in the Computer Supported Collaborative Learning (CSCL) area, didactic forums, calendars, electronic boards and knowledge storage are just a few of the core elements they o<sup>f</sup>er. All of these features are relevant to students and teachers, but there are also important drawbacks and limitations. A large majority of teachers have their own recipe to reach their goals, which may include small variations of typical learning activities, but can also involve innovative new approaches that can be considered disruptive. Due to their lack of <sup>fl</sup>exibility, LMSs either fail to allow or make it very di<sup>fi</sup>cult to create new processes or customize those already included. This forces teachers to perform tasks manually or use other external tools that provide partial solutions to the problem that arises, which negatively a<sup>f</sup>ects their productivity due to the time they have to dedicate to the management of these processes. The best alternative in the educational sector in this sense is probably LAMS (Learning Activity Management System),<sup>3</sup> which de<sup>fi</sup>nes a new terminology and notation to create sequences of learning activities. Although it is a good tool that focuses on the issue that concerns us, we consider it much more productive to apply the knowledge and powerful tools that have been developed in the business <sup>fi</sup>eld, thereby taking advantage of their <sup>fl</sup>exibility and capacity for optimization and integration, instead of creating a completely new ecosystem from scratch. Our contribution is an attempt to bring closer the educational needs that are usually catered for with tools that are hard to customize, and the highly adaptable enterprise systems that have been developed over decades to optimize all kinds of organizations worldwide.

The tool we are presenting in this paper is being designed and used as part of an innovation project in an Enterprise Information Systems (EIS) course at the University of Seville (Spain). One of the topics covered is the evolution of Information Systems (IS) and IT trends throughout recent decades (Merali et al., 2012), including Business Process Re-engineering (BPR) (Earl, 1994; Mumford, 1994; Coombs and Hull, 1995; Willcocks and Smith, 1995). We noticed the management of this course would be a good scenario to apply BPR, and started to design a new management system to enable new learning processes and optimize the existing learning processes using IT. Organizations are often easily optimized through the implementation of management systems with no or few adjustments to their out-of-the-box features; learning activities, however, present great diversity in the way each teacher can put them into practice. These variations can be crucial in achieving the learning goals that educators pursue, and even simple processes need a high level of <sup>fl</sup>exibility to enable educators to take control of the <sup>fi</sup>nal work<sup>fl</sup>ow. To the best of our knowledge, the educational literature has not yet explored the use of Business Process Management (BPM) techniques to administer and optimize learning processes, and our main goal is to perform an empirical analysis to evaluate the advantages of the use of BPM in this academic <sup>fi</sup>eld.

Therefore, after an initial design phase to model the processes, our BPM tool would be capable of assigning the appropriate task to each user depending on their role in the process, at the right time, and integrating di<sup>f</sup>erent types of information, such as time events, validation tasks, noti<sup>fi</sup>cations, and assessments. Furthermore, at the beginning of this project several strategic challenges were detected that we wanted to address. Firstly, course management should be more e<sup>fi</sup>cient and agile, thereby reducing costs in terms of the amount of time teachers need to spend supervising these tasks, and allowing faster and easier deployment of new educational activities. Secondly, we also wanted to help teachers visualize the current status of the course and access the progression of each and every student, in an e<sup>fi</sup>cient and e<sup>f</sup>ortless way. This would provide the teacher with the opportunity to intervene in the case where a student undergoes a slowdown or a steep drop in productivity. Finally, an improvement in student engagement was clearly a key goal, although probably the most di<sup>fi</sup>cult to achieve, especially with a high number of students per class.

As an illustration of the kind of activities we wanted to be able to put into practice, one of the learning processes included in our course to complement the lectures is brie<sup>fl</sup>y described. The goal was to increase collaboration and engagement, thereby encouraging our students to be proactive and take the initiative. One of our ideas was to allow two short presentations per day in each group, in which any student could talk about a topic of interest related with the course. The student would have to submit a proposal in advance, and, once approved, it would be assigned a date for presentation. The teacher would assess this activity, as would the classmates and even the speaker him/herself, resulting in a mathematical formula for the calculation of the <sup>fi</sup>nal mark using di<sup>f</sup>erent weights for each type of evaluation. For the sake of brevity, the descriptions of many other details are omitted here, but, after much time and e<sup>f</sup>ort, we were able to implement this process using online forms, cloud <sup>fi</sup>le storage, our email clients, very complex Exce worksheets and plenty of manual work to integrate all the information and supervise the work<sup>fl</sup>ow, which in its entirety resulted in a highly time-consuming process. Performing this process using the LMS deployed in our institution was simply not possible, but RubricaSoft made it possible with a reduction of 80% in the time spent by the teacher. We believe this can be seen as a convergent change (Tushman and Romanelli, 1985) in an organization with a stable structure, where we want to improve our e<sup>fi</sup>ciency and e<sup>f</sup>ectiveness by changing certain processes without altering our business model. Subsequently, more features were added, such as the automatic checking of the attendance of evaluators, the detection of outlier assessments that should be discarded as errors or malicious attempts to worsen the results, and gami<sup>fi</sup>cation to motivate students.

The use of information technology should always be preceded by an in-depth analysis to justify the implementation of the project (Gunasekaran et al., 2006), and hence we started the project re<sup>fl</sup>ecting on new ways to achieve our goals (Mircea, 2010), by primarily focusing on the usefulness of our new approach (Mahmood et al., 2001). During this phase other EISs were also considered, such as Customer Relationship Management (CRM) and Knowledge Management (KM) systems, which also o<sup>f</sup>er interesting features (see Hrnjic, 2016 and Wing Chu, 2016), but the most important part was the optimization of the business processes, which forms the core of BPM tools. The incorporation of rubrics to clarify the weight of each activity in the marks of the students led to the RubricaSoft system, which, to the best of our knowledge, constitutes the <sup>fi</sup>rst system to merge these two concepts: BPM and rubrics.

In Section 2 the concept of ‘rubric’ is explained and the BPMN notation utilised to model the processes is introduced. In Section 3 the terminology used by the system is explained and some examples of its functionality are shown. The bene<sup>fi</sup>ts of using the system are studied by analyzing a satisfaction survey and several indicators after one year of usage in Section 4. Finally, we summarize the main aspects to take into account when designing an educational system based on our proposal in Section 5, and our <sup>fi</sup>nal conclusions are drawn in Section 6.

## 2. Background

There are two important concepts that need to be introduced before the description is given of features and processes implemented in RubricaSoft: <sup>fi</sup>rst, the rubric concept, as we consider it very important to make learning processes easier to understand for the people involved, especially for students; and second, the Business Process Management Notation (BPMN) that made this development possible by providing a way to model the processes using a BPM design framework.

## 2.1. Rubrics

Information quality is considered the key mediator between system quality and organizational impact (Gorla et al., 2010), thus it is of the utmost importance to provide access to the most relevant content, in the right format.

The word rubric comes from the Latin word rubrica, which means red. In the Middle Ages, the rules for the conduct of liturgical services were usually written in red, so this term has been historically used to refer to a set of instructions or rules. Since the mid nineties, in an educational environment, rubric has referred to a scoring guide created by the teacher to specify how the learning activities are evaluated (see Popham, 1997; Allen and Tanner, 2006). This helps the students plan their work during the academic term and brings transparency to the assessment process, by clarifying the marks that can be obtained for each activity.

In a system such as RubricaSoft, where di<sup>f</sup>erent processes have been deployed, several of which involve multiple activities and the possibility of accumulating numerous minor marks for various concepts, it was necessary to implement a mechanism for the clari<sup>fi</sup>cation of the evaluation process itself.

Within the process of viewing the student marks, the system also shows a compilation of all the activities con<sup>fi</sup>gured for the course and the maximum values that the student can obtain by completing any speci<sup>fi</sup>c task (see Section 3.1). The students can consult this rubric at any time to verify the calculations performed by the system and hopefully resolve any doubt regarding the evaluation methods. We believe this information is crucial in reducing the resistance to change that usually appears in EIS implementation projects (Allen and Kern, 2001).

## 2.2. Business Process Management Notation

The BPM <sup>fi</sup>eld is concerned with designing, controlling and optimizing the business processes of a company (see Lee and Dale, 1998; Hammer, 2010). It is primarily focused on improving the e<sup>fi</sup>ciency of the organization through the automation of tasks and the elimination of bottlenecks among other strategies.

In a normal scenario, the specialist analyzes the current state of the processes (with the so-called as-is model), in an e<sup>f</sup>ort to detect any room for improvement, and then designs a new version of these processes (the to-be model) to solve the problems. These models are usually described using a graphical representation created for this purpose and called Business Process Management Notation (BPMN).<sup>5</sup> Its latest version, BPMN 2.0, was released in January, 2011, and describes all the elements that can be used to model a business process, including activities, <sup>fl</sup>ows, gateways, events and many others.

Nowadays, there are multiple software systems that assist the BPM specialists in designing and deploying digital business processes, such as the Bonitasoft framework<sup>6</sup> that is used here. These systems facilitate the creation, testing and execution of the models, and usually support the majority of elements de<sup>fi</sup>ned in the notations. The BonitaSoft software was selected for several reasons:

• It is a high-quality framework, included in the Gartner iBPMS (Intelligent Business Process Management Suites) magic quadrant, and it is Open Source. which allows free design and deplovment.

It o<sup>f</sup>ers a complete BPMS framework, covering all the necessary phases to deploy a new system, from process modelling and form design, to the production platform with the execution engine and user management.

The programming language in which the framework is based, Groovy, provides the versatility of the Java platform and the simplicity of a scripting language, and is therefore suitable for rapid application design

It is based on the popular development framework Eclipse,<sup>7</sup> and automates several implementation steps, generating code and using default values, which increases developer productivity.

By considering the educational processes from this point of view, it is possible to apply the same principles to optimize the way teachers manage the courses and the learning processes involved in these courses, and this formed our business case for the development of RubricaSoft

There have also been specialists that argue that BPMN models reduce organizational <sup>fl</sup>exibility as an important drawback, while they are supposed to increase it (de Albuquerque and Christ, 2015). In our case, this <sup>fl</sup>exibility is pursued by means of using process parameters, course con<sup>fi</sup>gurations, the possibility to design and deploy new processes to adapt the system functionality to new approaches, and the implicit <sup>fl</sup>exibility provided by the BPMN components (such as parallel work<sup>fl</sup>ows, and complex data types).

## 3. RubricaSoft

RubricaSoft is an educational process management system developed with the community version of Bonita BPM framework. Using the BPMN notation, it enables processes to be modelled, and the forms to be designed that can be <sup>fi</sup>lled out by users to interact with the system by introducing (and retrieving) information. Using this software, we have been able to focus on the processes we want to implement, without having to worry about user authentication, task assignments, version control and many other features that are already handled by the framework. The initial design e<sup>f</sup>orts are quickly paid o<sup>f</sup> as soon as teachers start using the optimized processes deployed, thereby saving a large proportion of the time spent on course management during the academic term. This is also an open platform and there is always the possibility of including new learning processes into the system, either based on existing processes or starting from scratch.

The three main concepts in a BPM system are:

Process: de<sup>fi</sup>nes a <sup>fl</sup>ow of tasks that need to be carried out in order to achieve a prede<sup>fi</sup>ned goal. For example, a process to manage teamwork in class could include tasks to submit a proposal, to accept or deny said proposal, to submit an assignment or, for the teacher, to assess team members activities.

Case: each time a process is initiated, an associated case is created. While the process is a general description, a case is a particular instance of a process, with its data and actors that may vary between cases of the same process.

Task: a process is de<sup>fi</sup>ned using various components (such as tasks, gates, and events). The main component is a task, which is a step in a process that can be completed by humans via data forms (human tasks) or by the system executing certain code (service and script tasks).

Another key concept in a BPM system is the Organization, which is a digital version of the composition and structure of the company sta<sup>f</sup>. It is de<sup>fi</sup>ned using:

• Groups: it can be used to de<sup>fi</sup>ne departments, teams or any other set of users that exist in the company. For example, in our case, we create a group for each course and several subgroups to distinguish between those students that come to either morning or evening classes

• Roles: not all actors play the same role in a process, and hence the roles have to be de<sup>fi</sup>ned for all users in each group where they belong. For example, in RubricaSoft, we have the roles of coordinator, teacher, student and technical user.

Users: everyone that interacts with the system has to be registered in the organization and needs a username and password in order to log in. In our case, the username is the Virtual username of the University of Seville (Usuario Virtual de la Universidad de Sevilla (UVUS)), which is a unique digital identi<sup>fi</sup>er assigned to each member in the institution. Other data, such as the emai address, is essential for communication with the user at certain points of the processes.

Two good examples of interesting features that the system allows us to apply to our courses in a simple manner are those of peer evaluation and the gami<sup>fi</sup>cation options that we have implemented. These features are explained once the list of learning processes that are currently available is described.

## 3.1. Educational processes

In addition to certain auxiliary processes (such as those to enable the users to change their password or email address), there have been four types of educational processes hitherto implemented. Each process relies on several BPMN processes and subprocesses and has its own section in the rubrics, where the marks for each activity involved in the process are shown.

The best process to illustrate the virtues of the system is probably that of the teamwork, which involves di<sup>f</sup>erent actors, tasks, timers and other interesting features, such as the cyclic execution work<sup>fl</sup>ow which allows the repetition of the ‘submission-presentation-assessment’ loop, thereby de<sup>fi</sup>ning as many milestones as needed to complete the work. The steps (shown in Fig. 1) are outlined below (the main actor is shown in brackets):

1. Send proposal [student]: any student can send a proposal to form a new team, by indicating a name to identify it, a summary of what they intend to do and the members of the team.

2. Proposal validation [teacher]: the teachers receive the proposal and one of them decides whether to accept or reject it.

3. Con<sup>fi</sup>rm teammates [teammates]: if the proposal is accepted, then the team members listed in it receive a task to con<sup>fi</sup>rm their participation.

4. Register team [automatic]: once the proposal has been accepted and all the team members have con<sup>fi</sup>rmed that they wish to be part of this team, then it is <sup>fi</sup>nally registered in the system database.

5. Obtain milestone data [automatic]: before the <sup>fi</sup>rst milestone is reached (and before each of the following milestones), the system calculates when the next task should be sent to the team members, based on the deadlines and other parameters de<sup>fi</sup>ned by the coordinator.

6. Submit milestone <sup>fi</sup>le [teammates]: when the previously calculated time comes, one of the team members should submit the <sup>fi</sup>le with the milestone work completed.

7. Evaluation [teacher]: one of the teachers evaluates the milestone <sup>fi</sup>le received.

![](/api/attachments/5JS7S5UD/fulltext/images/7002e06f498f866b6a664d272f92e33cf544875954bd28b42a115ef7692304ad.jpg)  
Fig. 1. Simpli<sup>fi</sup>ed version of the teamwork process model.

8. Peer evaluation [classmates]: if the coordinator has con<sup>fi</sup>gured this feature, then all the students receive a task to evaluate the work completed by their classmates.

9. Check attendance of evaluators [teacher]: the teachers can check if there is any student that evaluated a milestone presented in class without having attended that day.

10. Register marks [automatic]: the system <sup>fi</sup>nally calculates the mark to be registered for the team members by considering both peer and teacher evaluations with all the weights previously de<sup>fi</sup>ned by the coordinator.

However, this teamwork process is just one of the four educational processes we have implemented, which are:

Attendance: this process provides the mechanism for the teachers to monitor which students attend each class. The aim is to be able to use this information when calculating the total mark of each student and also to detect fraudulent actions in other processes. For example, it can be used to discover whether a student <sup>fi</sup>lls out a form to assess an activity developed in the classroom without that student having attended that day.

Exercises: there must also be a way to register o<sup>f</sup>-line activities that modify the mark of the student. This can be performed by introducing the assessments associated with a certain activity. The teacher registers as many activities or courseworks as needed, naming them in such a way as to enable the identi<sup>fi</sup>cation of each component when students consult their course marks.

Teamwork: the best scenario to test a BPM system in a teaching environment is probably that of the realization of some kind of joint project, thanks to the presence of multiple actors that are involved and the di<sup>f</sup>erent tasks that can be assigned to these actors, along with the time control needed. This process was outlined earlier in this section.

‘Miniwork’: this is initiated with a proposal submitted by an individual student, who describes the topic and work to be carried out individually. It continues with a validation task where the teacher either accepts or rejects the proposal. If it is accepted, then the system waits for the student to send the <sup>fi</sup>le with the work and automatically assigns a date for its oral presentation in the classroom. Finally, the teacher, and optionally also the classmates, can assess the work and submit their ratings once the presentation has taken place.

When students execute the option to see their marks, they can see the summary containing the total and subtotals for each educational process, or access a detail page with the amounts accumulated for each concept included in the rubrics shown in Figs. 2–5.

These processes imply the development of multiple subprocesses to simplify the representation, but can be perceived as a single model from a practical point of view. They have been selected because the course that became the <sup>fi</sup>rst to be managed using RubricaSoft manually implemented these processes in the past. All the activities that were evaluated with the old methods (manually integrating various tools or performed directly by hand) are now available, in RubricaSoft. However, the implementation has been carried out while considering many possible con<sup>fi</sup>gurations in order to make the processes useful for many other courses with similar learning methods. Of course, if a teacher needs an alternative work<sup>fl</sup>ow, then a new process can be modelled and added to the system.

<table><tr><td colspan="2">Attendance</td></tr><tr><td colspan="2">Maximum grade per group</td></tr><tr><td>Group</td><td>Maximum grade</td></tr><tr><td>LABS</td><td>0.4</td></tr><tr><td>THEORY</td><td>0.4</td></tr><tr><td colspan="2">Total number of sessions per group</td></tr><tr><td>Group</td><td>Number of sessions</td></tr><tr><td>LABS</td><td>13</td></tr><tr><td>THEORY</td><td>16</td></tr><tr><td colspan="2">Threshold to calculate grades</td></tr><tr><td colspan="2">Double fixed threshold (see image below)</td></tr></table>

Fig. 2. Attendance rubrics information.

<table><tr><td colspan="3">ExercisesOff-line exercises registered</td></tr><tr><td>Name</td><td>Description</td><td>Maximum grade</td></tr><tr><td>BonitaBPM evaluation</td><td>Evaluation of lab sessions dedicated to BonitaBPM</td><td>0.50</td></tr><tr><td>Magento evaluation</td><td>Evaluation of lab sessions dedicated to Magento</td><td>0.50</td></tr><tr><td>Odoo evaluation</td><td>Evaluation of lab sessions dedicated to Odoo</td><td>0.50</td></tr><tr><td>SugarCRM evaluation</td><td>Evaluation of lab sessions dedicated to SugarCRM</td><td>0.50</td></tr></table>

Fig. 3. Exercise rubrics information.

## 3.2. Peer evaluation and feedback

All the presentations carried out by students in the classroom, due to a milestone of the teamwork process or as the <sup>fi</sup>nal step of the ‘miniwork’ process, can be evaluated by their classmates if the teacher con<sup>fi</sup>gures the processes with this option. This makes students part of the evaluation process and they therefore become aware of its di<sup>fi</sup>culty.

The students receive a task for the assessment, where they can specify a numeric mark, from 0 to 10, and also write feedback to help the speaker improve for the next presentation. This is a good example of a task that previously consumed a substantial amount of time of the teacher and is now performed automatically by the system. The comments are anonymized so that students can express their opinions freely without fear of reprisal.

Once the peer evaluation time interval has <sup>fi</sup>nished (this is another con<sup>fi</sup>guration parameter), the system checks the attendance of all those students who have evaluated the presentation in order to discard those that fraudulently submitted the form without actually having attended that day. Once again, this is an automatic check that requires the supervision of the teacher only when there is an exclusion to be con<sup>fi</sup>rmed. The system also detects outliers among the evaluations by calculating the standard deviation. Therefore, we also strive to avoid evaluations from students whose personal relationships would otherwise a<sup>f</sup>ect the ratings by distorting the marks derived from these activities.

Technically, this implies a multi-instantiated task that calls the subprocess that handles the collection of an individual assessment. This task receives a list of the target users (the classmates) and generates a new instance of the call for each user, and adds the result

<table><tr><td colspan="4">Teamwork</td></tr><tr><td>No.</td><td>Description</td><td>Peer evaluated?</td><td>Maximum grade (from the teacher)</td></tr><tr><td>1</td><td>Initial presentation: Set the work objectives and its context.</td><td>yes</td><td>1</td></tr><tr><td>2</td><td>Final presentation: Explain the goals that have been reached or not.</td><td>yes</td><td>1.5</td></tr><tr><td>3</td><td>Final report: Text document describing the work done.</td><td>no</td><td>1.8</td></tr><tr><td colspan="4">Grades obtained by the team due to the peer evaluations</td></tr><tr><td colspan="3">Concept</td><td>Maximum grade</td></tr><tr><td colspan="3">Average mark from classmates</td><td>0.6</td></tr><tr><td colspan="3">Autoevaluation</td><td>0.1</td></tr><tr><td colspan="3">Autoevaluation-Teacher marks concordance</td><td>0.1</td></tr><tr><td colspan="3">Autoevaluation-Classmates marks concordance</td><td>0.1</td></tr><tr><td colspan="4">Grades obtained by evaluators in peer evaluations</td></tr><tr><td colspan="3">Concept</td><td>Maximum grade</td></tr><tr><td colspan="3">Concordance with teacher&#x27;s mark</td><td>0.06</td></tr><tr><td colspan="3">Concordance with classmates&#x27; marks</td><td>0.04</td></tr></table>

Fig. 4. Teamwork rubrics information

<table><tr><td>Date: if presented after...(mm/dd/aaaa)</td><td>Maximum grade</td></tr><tr><td>02/09/2016</td><td>1</td></tr><tr><td>03/07/2016</td><td>0.5</td></tr><tr><td colspan="2">Rules to calculate the maximum grade depending on the number of previous presentations of the student</td></tr><tr><td>No. of previous miniworks: If greater than or equal to...</td><td>Maximum grade</td></tr><tr><td>3</td><td>0.7</td></tr><tr><td>4</td><td>1</td></tr><tr><td colspan="2">Grades obtained by the speaker due to the peer evaluation</td></tr><tr><td>Concept</td><td>Maximum grade</td></tr><tr><td>Average mark from classmates</td><td>0.3</td></tr><tr><td>Autoevaluation</td><td>0.1</td></tr><tr><td>Autoevaluation-Teacher marks concordance</td><td>0.06</td></tr><tr><td>Autoevaluation-Classmates marks concordance</td><td>0.04</td></tr><tr><td colspan="2">Grades obtained by the evaluators due to the peer evaluation</td></tr><tr><td>Concept</td><td>Maximum grade</td></tr><tr><td>Concordance with teacher&#x27;s mark</td><td>0.06</td></tr><tr><td>Concordance with classmates&#x27; marks</td><td>0.04</td></tr></table>

Fig. 5. ‘Miniwork’ rubrics information.

to a <sup>fi</sup>nal data structure that contains all the assessments.

The speakers may also submit a mark for themselves, which is treated in a di<sup>f</sup>erent manner: as an auto-evaluation rating with its own individual weighting in the calculation of the <sup>fi</sup>nal mark.

In order to encourage students to participate in this evaluation process, peer evaluators also receive a small increment in their own marks based on their correlation with respect to the teacher assessment and the average of all the evaluations from the other students.

![](/api/attachments/5JS7S5UD/fulltext/images/5f82ffab7bf19b052dded59d48cd59714c342175d7126a7dafdf1d01c5b3dca3.jpg)  
Fig. 6. Top-10 ranking.

## 3.3. Gamification

Motivation is a key factor that should be taken into account when striving to improve the performance of the students (Bikfalvi et al., 2012). In general, gami<sup>fi</sup>cation (Burke, 2014) consists of the application of typical elements of game-playing to other areas, such as business activities. This is a global trend in the enterprise context and involves a range of mechanisms and techniques.

In the learning context, many platforms have already included elements related to gami<sup>fi</sup>cation (Domínguez et al., 2013), such as badges given to students who successfully complete certain tasks. In our case, we have focused on the competitive factor, generating a top-10 ranking of the course attendees (see Fig. 6) based on the marks accumulated at that time by all the students. The names of three best students appear in gold, silver and bronze, and for the other 7 students in the top-10 ranking, the name is highlighted in light blue. Students can consult the ranking at any time, following the philosophy of every cloud service. Although they can only see their own speci<sup>fi</sup>c marks, the ranking allows them to identify which 10 classmates are doing the best, thereby promoting a competitive attitude that positively a<sup>f</sup>ects their overall performance.

In addition to the ranking, we also generate another graph which reports the evolution of the marks obtained by the student in a line chart. Two versions of the graph are generated, one for the teacher showing a series for every student and a legend to identify them; and an individual version, without the legend and highlighting the evolution of the student who is consulting the chart (see Fig. 7). In the student version, the student s data is shown alongside the anonymized data of the rest of the class, thereby aiding in the evaluation of that student’s performance. In the teacher version, a legend identi<sup>fi</sup>es each line with the corresponding student. In this way, if a student has a problem in the middle of the term that a<sup>f</sup>ects his or her performance, then the teacher could detect it and attempt to solve that problem before it is too late.

## 3.4. Summary of advantages

The management of our courses through RubricaSoft o<sup>f</sup>ers a series of advantages in respect to other methods and tools:

Flexibility and innovation: unlike other similar tools, our system bene<sup>fi</sup>ts from the representational power of the Business Process Management Notation (BPMN), which allows us to model virtually any learning process imaginable. This presents the opportunity to design new processes and add them to the current o<sup>f</sup>ering, thereby letting other teachers use them in their courses. Thus, it can be considered a tool for innovation. One good example of an application could be for processes that include activities in two or more courses in order to maximize collaboration across university degrees. The integration capabilities of the framework, via a broad set of available connectors, have enabled us to modernize our previous methods and to include new functionalities using external tools (such as Talend scripts<sup>8</sup> and Jasper reports<sup>9</sup>). The inclusion of other connectors or the implementation of new connectors could further extend that which could be modelled in the future.

![](/api/attachments/5JS7S5UD/fulltext/images/4e6c485f41023f0a580339e6977a373968c49e2c746fb6fb0ef9a827878e055a.jpg)  
Fig. 7. Evolution of the marks of the students during the academic term.

Task-centred and proactive approach: every user has only one task list, where all pending activities are shown in order of their due date, regardless of whether the activities are from di<sup>f</sup>erent courses. This makes it more di<sup>fi</sup>cult for a student to forget a deadline or for a teacher to forget a validation task. The system is also proactive in that it communicates important events by email, if necessary, in order to prevent oversights.

Information and knowledge: in every EIS, including BPM systems such as RubricaSoft, the main goal is to manage information e<sup>fi</sup>ciently and to provide what is needed to convert data into knowledge. For example, in processes that involve peer evaluation, each classmate is encouraged to send feedback to other students about their work so that they can improve themselves for future presentations. The evolution line chart (showing the marks obtained) provides highly useful information both for students, who can therefore compare themselves with the rest of the class, and for teachers, who can detect a decrease in the performance of any student and can therefore take action before it is too late.

Transparency and self-service: the implemented rubrics that let every student know how the activities will be evaluated in detail, allow us to include complex processes in the system without harming the confidence of the students. The modelling of the di<sup>f</sup>erent processes and the rubrics also standardize the terminology used by a variety of teachers, who would otherwise sometimes di<sup>f</sup>er in their choice of terms thereby causing confusion among students. The fact that these processes and rubrics are always available on the Internet and accessible via numerous devices, facilitates their engagement and use of the system. The ability of the students to consult their current status whenever they need it is highly important to the students, and teachers can also complete their tasks from their o<sup>fi</sup>ce or anywhere else if they prefer.

Gamification: further to the evolution line chart that allows students to compare themselves with other classmates, we have also implemented a simple top-10 ranking based on accumulated marks, which is updated in real time. This ranking seems a simple approach to gami<sup>fi</sup>cation, which brings game techniques to non-game situations, but after several years of its implementation (before and after deploying RubricaSoft) it has proven to be very e<sup>f</sup>ective. The goal is to motivate students by provoking health competition among those who aspire to be the best in each class.

## 4. Experimental analysis

After our <sup>fi</sup>rst experience using RubricaSoft, time was dedicated to the analysis of the results while focusing on two elements: the satisfaction of the users and their interactions with the system. To this end, our students were sent a survey at the end of the term to

Table 1  
Data on the respondents of the satisfaction survey.

<table><tr><td colspan="2">Total number of respondents</td><td>59</td></tr><tr><td rowspan="2">Gender</td><td>Male</td><td>48</td></tr><tr><td>Female</td><td>11</td></tr><tr><td rowspan="2">Nationality</td><td>Spanish</td><td>56</td></tr><tr><td>Other</td><td>3</td></tr><tr><td rowspan="2">Age</td><td>Range</td><td>[20...32]</td></tr><tr><td>Average</td><td>24</td></tr></table>

assess several aspects of the system and a log <sup>fi</sup>le was generated with the information of each interaction with the system during the course (in every human task of the processes). These two perspectives and the subsequent analysis are explained below in more detail.

## 4.1. Satisfaction survey

A few weeks before the end of the term, a satisfaction survey was sent to all the students following the recommendations found in Graells (2002). This was performed using RubricaSoft, and it appeared just like any other entry in their pending task list. This allowed us to con<sup>fi</sup>gure the time we wanted it to be available, send an email automatically to those that had not completed it within 48 h, and, <sup>fi</sup>nally, associate it with the process that shows the marks of the students, thereby making it inaccessible until the survey was completed. A few days later we had collected the answers from the 59 students of our course (see Table 1 for details of the sample).

The questions were classi<sup>fi</sup>ed into three groups as shown in Table 2. Fig. 8 shows a graphical representation of the average ratings per group, and <sup>fi</sup>nally, Table 3 contains the descriptive statistics for all the responses in the survey. The results clearly show that the students liked the activities modelled and the options we designed (the resources obtained almost 9 out of 10 points), although the tool involves certain drawbacks that need to be addressed in future versions (the technical features obtained 6.62 points). Several of the problems came from the underlying framework. For example, the free version we used failed to o<sup>f</sup>er a responsive design, although it was possible to access from smartphones and tablets with certain limitations, and users could not use the Firefox browser due to a software bug that has since been resolved. A small economic investment by the organization would eliminate the small technical limitations of the free version of the framework, thereby helping to achieve a greater degree of satisfaction in the technica section. The system was also under continuous improvement from its deployment, and solved various issues during the academic term. The most important was probably the <sup>fi</sup>rst version of the menu processes that forced the user to complete an excessive number

Table 2  
Questions of the satisfaction survey.

<table><tr><td>Educational and functional</td><td>1. Ease of access and use2. Teaching effectiveness (facilitates the achievement of its goals)3. Relevance of content4. Ability to adapt to different courses5. Ability to adapt to different devices6. Ability to adapt to different learning styles and rates7. Motivational skills (attractive, interest, etc.)8. Adequacy of the content to recipients9. Adequacy of the activities to recipients10. Support services offered11. Communication environments available12. Evaluation system13. Promoting initiative and self-learning</td></tr><tr><td>Technical</td><td>14. Quality and structure of contents15. Navigation and structure of the activities16. Interaction with activities: dialogue, responses analysis17. Reliable execution, adequate access speed18. Originality and use of advanced technology</td></tr><tr><td>Resources</td><td>19. ‘Miniwork’ proposals20. Calendar of ‘miniworks’ (consult assigned dates)21. Notification of pending tasks22. Consultation of marks and rubrics23. Mark evolution charts24. Communication system (messages, surveys, complaints, etc.)25. Selection of subgroups in order of preference26. Information on ‘miniworks’ and teamworks proposals27. Cast tasks for collaborative activities28. Peer comments on presentations in class</td></tr></table>

![](/api/attachments/5JS7S5UD/fulltext/images/6511556d94d2f85cd820f5dbb406bd4795c7b449cfbb5e6191c376bf496f06c8.jpg)  
Fig. 8. Average ratings for each group of questions in the satisfaction survey.

Table 3  
Descriptive statistics of the satisfaction survey (count = 59 and maximum = 10 for all the rows).

<table><tr><td>Question No.</td><td>Mean</td><td>Std. Error</td><td>Median</td><td>Mode</td><td>Std. Deviation</td><td>Sample Variance</td><td>Kurtosis</td><td>Skewness</td><td>Range</td><td>Minimum</td><td>Sum</td><td>Confidence (95%)</td></tr><tr><td>1</td><td>6.07</td><td>0.21</td><td>6</td><td>6</td><td>1.62</td><td>2.62</td><td>1.11</td><td>0.54</td><td>8</td><td>2</td><td>358</td><td>0.42</td></tr><tr><td>2</td><td>6.78</td><td>0.21</td><td>6</td><td>6</td><td>1.58</td><td>2.49</td><td>-0.36</td><td>0.05</td><td>6</td><td>4</td><td>400</td><td>0.41</td></tr><tr><td>3</td><td>6.68</td><td>0.20</td><td>6</td><td>6</td><td>1.51</td><td>2.29</td><td>0.91</td><td>-0.17</td><td>8</td><td>2</td><td>394</td><td>0.39</td></tr><tr><td>4</td><td>6.61</td><td>0.24</td><td>6</td><td>6</td><td>1.83</td><td>3.35</td><td>0.19</td><td>-0.24</td><td>8</td><td>2</td><td>390</td><td>0.48</td></tr><tr><td>5</td><td>5.56</td><td>0.28</td><td>6</td><td>6</td><td>2.14</td><td>4.56</td><td>-0.42</td><td>0.28</td><td>8</td><td>2</td><td>328</td><td>0.56</td></tr><tr><td>6</td><td>6.41</td><td>0.18</td><td>6</td><td>6</td><td>1.38</td><td>1.90</td><td>0.36</td><td>0.36</td><td>6</td><td>4</td><td>378</td><td>0.36</td></tr><tr><td>7</td><td>6.44</td><td>0.28</td><td>6</td><td>6</td><td>2.17</td><td>4.70</td><td>-0.83</td><td>0.05</td><td>8</td><td>2</td><td>380</td><td>0.56</td></tr><tr><td>8</td><td>6.54</td><td>0.23</td><td>6</td><td>6</td><td>1.74</td><td>3.01</td><td>0.36</td><td>-0.40</td><td>8</td><td>2</td><td>386</td><td>0.45</td></tr><tr><td>9</td><td>6.85</td><td>0.18</td><td>6</td><td>6</td><td>1.40</td><td>1.96</td><td>0.05</td><td>0.44</td><td>6</td><td>4</td><td>404</td><td>0.36</td></tr><tr><td>10</td><td>6.47</td><td>0.24</td><td>6</td><td>6</td><td>1.87</td><td>3.50</td><td>0.13</td><td>0.02</td><td>8</td><td>2</td><td>382</td><td>0.49</td></tr><tr><td>11</td><td>6.31</td><td>0.25</td><td>6</td><td>6</td><td>1.92</td><td>3.70</td><td>-0.23</td><td>0.41</td><td>8</td><td>2</td><td>372</td><td>0.50</td></tr><tr><td>12</td><td>7.66</td><td>0.23</td><td>8</td><td>6</td><td>1.75</td><td>3.06</td><td>-1.10</td><td>0.02</td><td>6</td><td>4</td><td>452</td><td>0.46</td></tr><tr><td>13</td><td>7.69</td><td>0.25</td><td>8</td><td>6</td><td>1.89</td><td>3.56</td><td>-0.25</td><td>-0.32</td><td>8</td><td>2</td><td>454</td><td>0.49</td></tr><tr><td>14</td><td>6.07</td><td>0.24</td><td>6</td><td>6</td><td>1.82</td><td>3.31</td><td>0.42</td><td>0.64</td><td>8</td><td>2</td><td>358</td><td>0.47</td></tr><tr><td>15</td><td>5.19</td><td>0.25</td><td>6</td><td>6</td><td>1.90</td><td>3.60</td><td>0.57</td><td>0.54</td><td>8</td><td>2</td><td>306</td><td>0.49</td></tr><tr><td>16</td><td>6.10</td><td>0.22</td><td>6</td><td>6</td><td>1.72</td><td>2.95</td><td>0.32</td><td>0.41</td><td>8</td><td>2</td><td>360</td><td>0.45</td></tr><tr><td>17</td><td>6.78</td><td>0.21</td><td>6</td><td>6</td><td>1.58</td><td>2.49</td><td>-0.36</td><td>0.05</td><td>6</td><td>4</td><td>400</td><td>0.41</td></tr><tr><td>18</td><td>6.95</td><td>0.19</td><td>8</td><td>8</td><td>1.46</td><td>2.12</td><td>-0.22</td><td>-0.19</td><td>6</td><td>4</td><td>410</td><td>0.38</td></tr><tr><td>19</td><td>9.27</td><td>0.18</td><td>10</td><td>10</td><td>1.39</td><td>1.94</td><td>-0.09</td><td>-1.38</td><td>3</td><td>7</td><td>547</td><td>0.36</td></tr><tr><td>20</td><td>8.42</td><td>0.27</td><td>10</td><td>10</td><td>2.09</td><td>4.35</td><td>-0.05</td><td>-0.97</td><td>7</td><td>3</td><td>497</td><td>0.54</td></tr><tr><td>21</td><td>9.32</td><td>0.19</td><td>10</td><td>10</td><td>1.49</td><td>2.21</td><td>3.83</td><td>-2.10</td><td>7</td><td>3</td><td>550</td><td>0.39</td></tr><tr><td>22</td><td>9.66</td><td>0.13</td><td>10</td><td>10</td><td>1.02</td><td>1.03</td><td>5.50</td><td>-2.70</td><td>3</td><td>7</td><td>570</td><td>0.26</td></tr><tr><td>23</td><td>8.87</td><td>0.21</td><td>10</td><td>10</td><td>1.59</td><td>2.53</td><td>-1.57</td><td>-0.70</td><td>3</td><td>7</td><td>523</td><td>0.41</td></tr><tr><td>24</td><td>8.53</td><td>0.23</td><td>10</td><td>10</td><td>1.78</td><td>3.17</td><td>-0.92</td><td>-0.60</td><td>7</td><td>3</td><td>503</td><td>0.46</td></tr><tr><td>25</td><td>9.04</td><td>0.21</td><td>10</td><td>10</td><td>1.64</td><td>2.70</td><td>0.96</td><td>-1.40</td><td>7</td><td>3</td><td>533</td><td>0.43</td></tr><tr><td>26</td><td>8.81</td><td>0.22</td><td>10</td><td>10</td><td>1.72</td><td>2.97</td><td>-0.17</td><td>-1.00</td><td>7</td><td>3</td><td>520</td><td>0.45</td></tr><tr><td>27</td><td>8.31</td><td>0.27</td><td>10</td><td>10</td><td>2.09</td><td>4.36</td><td>-0.27</td><td>-0.84</td><td>7</td><td>3</td><td>490</td><td>0.54</td></tr><tr><td>28</td><td>9.15</td><td>0.24</td><td>10</td><td>10</td><td>1.81</td><td>3.29</td><td>3.56</td><td>-2.09</td><td>7</td><td>3</td><td>540</td><td>0.47</td></tr></table>

of steps, which caused many complaints until a new optimized version was deployed. The next big step forward for RubricaSoft wil be the implementation of a customized user interface. which will leave behind the standard web portal behind in order to focus on usability, whereby the particular features of our business processes are considered.

## 4.2. System usage

Another advantage of BPM systems is the opportunity that they present for the study of the data generated by the system usage, which is usually registered in log <sup>fi</sup>les (Sapunar et al., 2016). From 3rd February to 8th July, the system automatically registered the information about all 12,974 interactions that took place. We call interaction to every human task (a web form with one or more pages) that is initiated. From all these interactions, only those belonging to the menu processes are omitted, since we consider them simply a way to reach other processes.

![](/api/attachments/5JS7S5UD/fulltext/images/61ff0181f36d067fcd8aabc4377127565e20535230205ce2c1a3c4305eeb19e3.jpg)  
Fig. 9. Number of interactions per day.

A course is analyzed consisting of two classes per week (on Tuesdays for theory and on Fridays for laboratory work), broken down into two and four groups respectively. In Fig. 9 the total number of interactions per day can be observed, which features a weekly pattern of double peaks that matches the frequency of the classes. There are <sup>fi</sup>ve points labelled with the number of interactions that correspond to the days of the highest level of usage. Peer evaluation is the event that causes these e<sup>f</sup>ects, since every student accesses the system within a short time window. The <sup>fi</sup>rst four cases are related with the teamwork process. Each milestone con<sup>fi</sup>gured by the coordinator for peer evaluation require the presentations of the 21 teams to be completed within two weeks. The last labelled point is associated with the last class of theory (31st May), when all ‘miniworks’ that were waiting in the queue were presented and then peer evaluated the same day. The rest of the smaller peaks are due to the sum of the peer evaluations of the ‘miniworks’ presented weekly (4 maximum) and to the access to the ‘Consult my marks’ process, which is the most commonly used feature, as explained below. A dotted line representing the polynomial tendency also shows the evolution of this line chart with a small trough in the middle of the term.

If all the processes are analyzed individually (see Fig. 10), it is found that the process with by far the highest number of interactions is ‘Consult my marks’. This shows the accumulated marks in detail together with the rubrics, and also presents the top-10 ranking and the evolution charts. We believe this process to be an important element of the system, since it helps us motivate students during the course. It is followed by the peer evaluation processes of teamworks and ‘miniworks’ and the main operative processes of these two educational activities. In order to simplify Fig. 10, those processes with fewer than 40 interactions have been removed.

In Fig. 11, it can be observed how most of the interactions come from the operative processes (60%), followed by the information options o<sup>f</sup>ered by the system (35%). The remaining (5%) is for communication and con<sup>fi</sup>guration processes that are used sporadically; the latter only at the beginning of the course.

If focus is shifted onto the four educational processes that we have implemented (see Section 3.1), it can be found, as shown in Fig. 12, that 93% of the interactions are related with activities of the teamwork or ‘miniwork’ processes (46% and 47% respectively), either carried out by students or teachers, depending on the task. With tasks that are assigned exclusively to teachers, another 6% is associated with student attendance (to generate the attendance sheet and register the data in the system) and the remaining 1% with the o<sup>f</sup>-line exercises (in its creation and evaluation).

In Fig. 13 the evolution over time of the number of interactions is shown, but this time the interactions are grouped in terms of educational process. It can be clearly observed how the course has been con<sup>fi</sup>gured, with ‘miniworks’ every week and the two

![](/api/attachments/5JS7S5UD/fulltext/images/88b6f13f4debd2b4676f18da92e2ed1d7b7c6914fd8665e422bea370fb3d99b8.jpg)  
Fig. 10. Number of interactions per process.

Journal of Strategic Information Systems xxx (xxxx) xxx–xxx

![](/api/attachments/5JS7S5UD/fulltext/images/13e589bfb3e8d0807fee69a398f608b4a5758e057d6961c8bce24367c1313245.jpg)  
Fig. 11. Percentage of interactions per process category.

![](/api/attachments/5JS7S5UD/fulltext/images/f851c3035ed208beb632e149d3f88bdc2e6abfe7ee604019dc811bae6daf1008.jpg)  
Fig. 12. Percentage of interactions per educational process.

milestones of the teamwork taking two weeks each. In the holiday period on 22nd March and 12nd April, the line chart shows very little activity.

In relation to the number of interactions of each student, we also found that there is certain correlation between this number and the <sup>fi</sup>nal mark of the student as shown by the tendency dotted line in Fig. 14. In this case, only the operative processes have been considered and the Pearson and Spearman coe<sup>fi</sup>cients have also been calculated (0.37 and 0.39 respectively). It can be concluded that simply using the system itself is insu<sup>fi</sup>cient for students to attain good marks, although it does help them organize their work.

## 4.3. Improvements using RubricaSoft

Once having shown a detailed view of the functionalities of the tool, its satisfaction levels and several statistics of its usage, we then compared the situation before and after the deployment of RubricaSoft. First of all, the average mark of the course was alread high before using RubricaSoft. Nevertheless, it still increased by almost half a point reaching 7.95 points out of 10. Other important indicators that can represent the bene<sup>fi</sup>ts of using RubricaSoft were also studied.

![](/api/attachments/5JS7S5UD/fulltext/images/eac8d5946e2a5fa636a5db0fe7264da9caf790fd333e6ff04dc9753c07d963b0.jpg)  
Fig. 13. Number of interactions per day grouped by educational process.

![](/api/attachments/5JS7S5UD/fulltext/images/af8593cd04dd41b24eeec1f02bf08bb350e47b1dab2d6e491caf3e2e2be60d5c.jpg)  
Fig. 14. Number of interactions per student, ordered by <sup>fi</sup>nal mark.

Table 4  
Results of the quality survey conducted by the University of Seville.

<table><tr><td>Question</td><td>Course</td><td>Area</td><td>Degree</td></tr><tr><td>Q1</td><td>4.16</td><td>3.99</td><td>3.99</td></tr><tr><td>Q2</td><td>3.98</td><td>3.90</td><td>3.93</td></tr><tr><td>Q3</td><td>4.34</td><td>3.94</td><td>3.84</td></tr><tr><td>Q4</td><td>4.02</td><td>3.77</td><td>3.74</td></tr><tr><td>Q5</td><td>4.22</td><td>3.91</td><td>3.87</td></tr><tr><td>Q6</td><td>4.11</td><td>3.62</td><td>3.73</td></tr><tr><td>Q7</td><td>4.16</td><td>4.05</td><td>4.05</td></tr></table>

Best value in each row are in bold.

## 4.3.1. Quality survey

Table 4 shows an extract of the results obtained in a quality survey commissioned by the University of Seville to an external company after RubricaSoft had been used in our course. This table presents the average rating (in the 0–5 range) given by students to the following statements related to the learning methods:

1. The teaching methods are well organized

2. The media employed to impart the teaching are suitable for my learning

3. It encourages a climate of work and participation

4. It motivates the students to be interested in the subject

5. The teaching methods are helping me to achieve the objectives of the course

6. The criteria and evaluation systems seem suitable for the evaluation of my learning

7. In general, I am satis<sup>fi</sup>ed with the teaching performance developed by the teacher

## Table 5

Participation in the ‘miniwork’ activity during 2015 (previous scenario) and during 2016 (using RubricaSoft).

<table><tr><td></td><td>2015</td><td>2016</td></tr><tr><td>Total number of ‘miniworks’</td><td>47</td><td>77</td></tr><tr><td>Number of students participating</td><td>24 (46.15%)</td><td>38 (64.41%)</td></tr><tr><td>Average number of ‘miniworks’ per student</td><td>0.9</td><td>1.3</td></tr></table>

This survey not only re<sup>fl</sup>ects the satisfaction of the students regarding our course, but it also re<sup>fl</sup>ects the average ratings considering the area and the degree, thereby allowing us to compare our performance.

## 4.3.2. Participation

As explained earlier, in RubricaSoft we have implemented the same activities as those previously managed manually. Several of these activities are mandatory, such as the participation in a teamwork, and hence the new tool must manage the same volume of work in these cases; the ‘miniwork’, however, is an optional activity where students are allowed to send zero or more proposals at their discretion. Does the new tool motivate students to participate more in the course? Table 5 shows how participation has been clearly improved (41% increase in the number of ‘miniworks’ per student), probably as an e<sup>f</sup>ect of the simplicity brought about by RubricaSoft, and of other features, such as the evolution graphs, etc.

## 4.3.3. Cost savings and course statistics

By considering the same ‘miniwork' process analyzed in the previous section, we can also estimate the cost savings derived from the automation of several steps. In the previous scenario, the teacher had to periodically check for new proposals using the online Form tool, which took around 15 min per week even if there were no proposals. After validation of those new proposals (10 min), the teacher updated their status in a list accessible by students (5 min), so that they could see whether the proposals had been approved. When students sent the ‘miniwork’ ready for presentation, the teacher had to manually assign a date in the appropriate group (15 min) and prepare the online form that students complete for peer evaluation (15 min). Finally, the teacher had to collect the feedback from the classmates and send it to the speaker via email (15 min). Using RubricaSoft, the system noti<sup>fi</sup>es the teacher when there is a new proposal to validate, and except for the validation task, which remains the same, the remaining tasks (status update, date assignment, peer evaluation forms and feedback) become automatic and require no intervention by the teacher. In Table 6 the di<sup>f</sup>erence is shown in terms of time (minutes) between the two scenarios, before and after RubricaSoft, assuming a duration of the course of 15 weeks and a limit of 52 papers presented (4 per week excluding the <sup>fi</sup>rst 2 weeks). The result is nearly an 80% reduction in the time spent on this process alone, which is time the teacher can now spend on tasks of a more valuable nature.

If the working day of a teacher lasts 8 h, then 600 h will be accumulated during those 15 weeks, and hence using the system means dedicating only 2% of the total time to managing this process instead of 10%. This result can also be interpreted as an economic saving of 8% of the salary of the teacher, on considering only the process analyzed.

## 5. Discussion

Educational software has greatly evolved during the last decades and almost every educational institution uses one of these systems nowadays. In our case, we have a system considered one of the best available, but many of our colleagues cannot <sup>fi</sup>nd in it the right tool for developing the desired educational process, and students often log in only to download or access to teaching material.

What we have done in our proposed system, named RubricaSoft, is to focus on a Business Process Management System, which is the best type of Enterprise Information System for all those organizations whose aim is to optimize the business processes they rely on. Adding simple gami<sup>fi</sup>cation features, a simple integrated interface and considering what is most important for our “customers”, has given us very promising results. With this solution, we also have direct access to the processes we want to deploy via the BPMN notation, removing all the design restrictions imposed by traditional LMS.

## Table 6

Time spent (in minutes) on administering the ‘miniwork’ activity.

<table><tr><td>Steps</td><td>Pre-RubricaSoft</td><td>With RubricaSoft</td></tr><tr><td>Check for new proposals</td><td>225</td><td>0</td></tr><tr><td>Validate and update status</td><td>1155</td><td>770</td></tr><tr><td>Assign dates</td><td>780</td><td>0</td></tr><tr><td>Prepare peer evaluation form</td><td>780</td><td>0</td></tr><tr><td>Collect, process and send feedback</td><td>780</td><td>0</td></tr><tr><td>Total</td><td>3720</td><td>770</td></tr></table>

Regarding gami<sup>fi</sup>cation, a simple ranking motivated our best students drawing the best of them competing to reach the <sup>fi</sup>rst place, and showing key performance indicators warned lagging students so they could react in time. Usability features, such as the simplicity of the forms or a quick access to all the menu options, have proven to be important factors to be taken into account. We implemented a new version of the menu processes after receiving feedback from our students saying too many clicks were needed to perform the desired task.

Setting a proactive perspective in all the processes designed in the system was also very well received by the students, because the accumulation of tasks in di<sup>f</sup>erent courses can easily lead to one of them not being delivered on time, which can harm the student’s performance. RubricaSoft orders the list of tasks based on their due date, sends messages when the user attention is needed and only to interested parties and performs many other calculations and system tasks automatically. From the teacher perspective, this greatly reduced the time spent in management tasks and in our case it meant a signi<sup>fi</sup>cant improvement in productivity.

From our point of view, an educational system should be designed with the process design as the core component and paying the utmost attention to two aspects: simplicity and <sup>fl</sup>exibility. With an underlying framework that allows the implementation of whatever educational process a teacher can think of, there will not be any technical restrictions to innovate with new activities that require di<sup>f</sup>erent types of tasks, actors or iterations. Once this is achieved, a simple interface and improving usability will reduce the resistance to change and promote the system usage.

## 6. Conclusions

Despite the existence of software tools speci<sup>fi</sup>cally designed to manage educational institutions, none of them o<sup>f</sup>er the <sup>fl</sup>exibility and adaptability needed by teachers to easily de<sup>fi</sup>ne dynamic and innovative learning activities. In contrast, business information systems, and speci<sup>fi</sup>cally BPM by means of the BPMN notation, specialize in the modelling of complex processes in an optimal way. Our main goal is to perform an empirical analysis to evaluate the advantages of the use of BPM techniques in the educational <sup>fi</sup>eld, which remains a relatively unexplored area.

Using our new system named RubricaSoft, users are organized into groups (courses, morning or evening classes, etc.) and roles (student, teacher and coordinator) and previously designed learning processes composed of di<sup>f</sup>erent types of tasks, time events, noti<sup>fi</sup>cations, etc. can be executed. There are currently four types of processes implemented, related with attendance, o<sup>f</sup>-line exercises, teamwork and individual ‘miniworks’. This system is especially useful when implementing dynamic processes that involve multiple actors, with di<sup>f</sup>erent responsibilities, such as a teamwork with several milestones and peer evaluation. Its main features can be summarized as follows:

Flexibility and innovation: the BPMN notation along with the integration capabilities allows us to model virtually any learning process, thereby creating a space for creativity and innovation.

• Task-centred and proactive approach: a uni<sup>fi</sup>ed interface is employed for all courses, where every user can easily track the pending tasks ordered by due date, and system noti<sup>fi</sup>cations are made by email to avoid oversights.

Information and knowledge: every process has been designed to show only relevant information to the user for each task, with text or graphics when needed, with the goal of converting data into knowledge whenever possible.

Transparency and self-service: users can access the system at anytime and from anywhere to consult information (marks, rubrics,…) or complete the tasks.

Gamification: with a simple top-10 ranking and with line charts showing student evolution during the course compared with the rest of the class, we generate a competitive atmosphere to motivate our students and improve their performance.

After having described certain technical details to further clarify how RubricaSoft works, we <sup>fi</sup>nally revealed very promising results from the point of view of the three axes upon which the evaluation has been carried out: satisfaction of the students, improvement in the academic results and increase in the productivity of the teachers. Among other indicators, not only was a reduction of 80% found in the time spent by teachers on administering the ‘miniwork’ activity but an increase of 40% was also produced in student participation during the implementation of this learning process.

This system has improved our e<sup>fi</sup>ciency and has been positively rated by the users, due to its successful completion of the refreeze and optimization phases in Lewin s extended organizational change model, as described in Lewin (1951) and Besson and Rowe (2012). All our strategic goals have been addressed. First, it has rendered course management more e<sup>fi</sup>cient and agile, and has reduced the time spent on interventions by all actors. This system also enables the fast and easy deployment of new versions of the educational activities, by means of selecting the corresponding options from the application menu. Second, our evolution graphs provide the visualization of the current status of the course and of the evolution of individual students, and supplies access to all the details so that both teachers and students alike can assess the ongoing learning process, all in an e<sup>fi</sup>cient and e<sup>f</sup>ortless manner. Finally, the problem of student engagement has been tackled largely through adopting gami<sup>fi</sup>cation techniques, which have shown very good results, and rubrics provide con<sup>fi</sup>dence to the students in that they help to prevent resistance to change

We believe the use of BPM technology in the educational <sup>fi</sup>eld can provide teachers with the <sup>fl</sup>exibility to design new innovative learning activities. Its ability to organize tasks assigned to multiple actors has proven to be very useful in this area, and the possibility of using a standard notation such as BPMN opens the door to collaboration between BPM consultants and educators. The application of this approach for the creation of new processes that enhance the current ecosystem of learning management systems would be ver useful for educational institutions and business training programs.

## Acknowledgements

This work was supported by projects 2132 and 3424 from Plan Propio de Docencia (University of Seville) and by project TIN2017- 82113-C2-1-R of the Ministry of Economy and Competitiveness (Spain).

## References

Allen, D., Kern, T., 2001. Enterprise resource planning implementation: stories of power, politics, and resistance. In: Realigning Research and Practice in Information Systems Development. Springer, pp. 149–162.

Allen, D., Tanner, K., 2006. Rubrics: tools for making learning goals and evaluation criteria explicit for both teachers and learners. CBE-Life Sci. Edu. 5 (3), 197 203.

Besson, P., Rowe, F., 2012. Strategizing information systems-enabled organizational transformation: a transdisciplinary review and new directions. J. Strateg. Inf. Syst. 21 (2), 103–124.

Bikfalvi, A., Simon, A., Villar, E., 2012. Intentional change and motivation to change. Exploring competence assessment and development in higher education. In: INTED2012 Proceedings, pp. 943–952.

Burke, B., 2014. Gamify: How Gami<sup>fi</sup>cation Motivates People to Do Extraordinary Things.

Coombs, R., Hull, R., 1995. Bpr as it-enabled organizational change: an assessment. New Technol. Work Emp. 10 (2), 121 131.

de Albuquerque, J.P., Christ, M., 2015. The tension between business process modelling and <sup>fl</sup>exibility: revealing multiple dimensions with a sociomaterial approach. J. Strateg. Inf. Syst. 24 (3), 189 202.

Domínguez, A., Saenz-De-Navarrete, J., De-Marcos, L., Fernández-Sanz, L., Pagés, C., Martínez-Herráiz, J.-J., 2013. Gamifying learning experiences: practical implications and outcomes. Comput. Edu. 63, 380 392.

Earl, M.J., 1994. The new and the old of business process redesign. J. Strateg. Inf. Syst. 3 (1), 5–22.

Gorla, N., Somers, T.M., Wong, B., 2010. Organizational impact of system quality, information quality, and service quality. J. Strateg. Inf. Syst. 19 (3), 207–228.

Graells, P.M., 2002. Evaluación y selección de software educativo. Las nuevas tecnologías en la respuesta educativa a la diversidad, Universidad Autónoma de Barcelona 115.

Gunasekaran, A., Ngai, E.W., McGaughey, R.E., 2006. Information technology and systems justi<sup>fi</sup>cation: a review for research and applications. Eur. J. Oper. Res. 173 (3). 957-983.

Hammer, M., 2010. What is Business Process Management. Springer, Berlin, Heidelberg, pp. 3–16.

Hrnjic, A., 2016. The transformation of higher education: evaluation of crm concept application and its impact on student satisfaction. Eurasian Bus. Rev. 6 (1), 53–77.

Lee, R., Dale, B., 1998. Business process management: a review and evaluation. Bus. Process Manage. J. 4 (3), 214–225. https://doi.org/10.1108 14637159810224322

Lewin, K., et al., 1951. Field theory in social science.

Mahmood, M.A., Hall, L., Swanberg, D.L., 2001. Factors a<sup>f</sup>ecting information technology usage: a meta-analysis of the empirical literature. J. Org. Comput. Electron. Comm. 11 (2), 107–130.

Merali, Y., Papadopoulos, T., Nadkarni, T., 2012. Information systems strategy: past, present, future? J. Strateg. Inf. Syst. 21 (2), 125–153.

Mircea, M., 2010. Soa, bpm and cloud computing: Connected for innovation in higher education. In: 2010 International Conference on Education and Management Technology (ICEMT). IEEE, pp. 456-460.

Mumford, E., 1994. New treatments or old remedies: is business process reengineering really socio-technical design? J. Strateg. Inf. Syst. 3 (4), 313–326.

Popham, W.J., 1997. What’s wrong-and what’s right-with rubrics. Educ. Leadership 55, 72–75

Rutten, N., van Joolingen, W.R., van der Veen, J.T., 2012. The learning e<sup>f</sup>ects of computer simulations in science education. Comput. Educ. 58 (1), 136–153.

Sapunar, D., Grković, I., Lukšić, D., Marušić, M., 2016. The business process management software for successful quality management and organization: a case study from the university of split school of medicine. Acta medica academica 45 (1), 26.

Tarí, J.J., Dick, G., 2016. Trends in quality management research in higher education institutions. J. Service Theory Pract. 26 (3), 273–296

Tushman, M., Romanelli, E., 1985. Organizational evolution: a metamor-phosis model of convergence and reorientation. In: Staw, B., Cummings, L.L. (Eds.), Research in Organizational Behavior. Jai press, Greenwich, CT, pp. 7.

Watson, W.R., Watson, S.L., 2007. What are learning management systems, what are they not, and what should they become. TechTrends 51 (2), 29

Willcocks, L., Smith, G., 1995. It-enabled business process reengineering: organizational and human resource dimensions. J. Strateg. Inf. Syst. 4 (3), 279–301.

Wing Chu, K., 2016. Beginning a journey of knowledge management in a secondary school. J. Knowl. Manage. 20 (2), 364 385
