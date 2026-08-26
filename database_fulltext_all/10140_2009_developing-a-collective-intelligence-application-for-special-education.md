---
otero_id: 10140
otero_key: "AUG82B5B"
title: "Developing a collective intelligence application for special education"
authors: "Dawn Gregg"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.04.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Developing a collective intelligence application for special education

Dawn Gregg ⁎

Information Systems University of Colorado Denver, PO Box 173364, Campus Box 165, Denver, CO 80217-3364, United State

## a r t i c l e i n f o

Article history: Received 28 September 2007 Received in revised form 3 March 2009 Accepted 15 April 2009 Available online 22 April 2009

Keywords: Special education Data-based decision making Computer supported cooperative care Collective intelligence Collaboration Distributed asynchronous groups

## a b s t r a c t

This research uses an action research methodology to develop a web based collective intelligence application, DDtrac. DDtrac allows special education practitioners to collect data and share insights related to student performance during educational tasks and social interactions and can be used to assess special education student progress and improve decision making. A survey of 40 special education professionals and a four year case study using a single subject both indicate that educators, clinicians, families, parents, or other professionals that work with individuals with developmental disabilities achieve tangible bene<sup>fi</sup>t from the real time data tracking and decision support provided by the DDtrac application. The development of the DDtrac application and subsequent end-user evaluation is used to develop a set of six requirements for collective intelligence applications. These requirements can be used to guide future developers seeking to create web based applications that harness the collective intelligence of groups.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Across America, the number of developmentally disabled children is increasing every year with 6.8 million students enrolled in special education programs nationwide [67]. Research has demonstrated that students learn more when educators perform systematic data collection and analysis to monitor progress [17,61]. This has resulted in increasing pressure for practitioners to demonstrate the unequivocal short- and long-term bene<sup>fi</sup>ts of special education interventions for children with disabilities. In fact, the Individuals with Disabilities Education Act of 2004 (IDEA 2004) now requires that schools document special education students' Response to Intervention (RTI)<sup>1</sup> [46].

The increased focus on progress monitoring has resulted in the development of numerous computer-based tools that can be used to regularly probe student knowledge in selected areas and can automatically graph the progress of individual students [73]. However, commercially available tools are targeted at the at-risk students for whom academic progress is delayed by one to three years. Although the importance of using data collection and analysis procedures to monitor academic, social and behavior progress of the 5% of students with intensive needs is well documented in special education literature [e.g., 18,24,39,66], there are no commercial tools available that assist special education teachers in monitoring their daily progress.<sup>2</sup> Currently, data collection for these students uses paper and pencil making it dif<sup>fi</sup>cult (and time consuming) to perform meaningful data analysis.

Information systems researchers have only begun to address the progress monitoring needs of students with intensive needs. This paper uses an action research methodology to design, implement, and test DDtrac a special education collective intelligence application that utilizes student-speci<sup>fi</sup>c data to support decision making, collaboration and an improved understanding of the unique education needs of individual students. The primary goal of the DDtrac system is to reduce the amount of time individuals spend collecting and analyzing data and to improve their ability to use data to make treatment decisions. The special education domain is ideal for studying the development of collective intelligence applications because special education students often have many people involved in their education and therapy team across a wide variety of settings. These practitioners rarely have time to communicate details related to student progress which can lead to an inef<sup>fi</sup>cient duplication of effort, gaps in treatment, or team members working towards con<sup>fl</sup>icting goals. A collective intelligence application provides the special education team with the opportunity to harness the knowledge of these practitioners to identify patterns of behavior and best practices for both individual students as well as groups of students with similar disabilities.

To date there has been limited research on the design and implementation of web based virtual collaboration or collective intelligence applications designed for specialized application domains. This study examines how specialized collective intelligence applications might be developed and implemented. The development of the DDtrac special education collective intelligence application and subsequent end-user evaluation is used to develop a set of requirements that collective intelligence should adhere to. These requirements can be used to guide future developers seeking to create web based collective intelligence applications for a variety of domains.

The remainder of the paper is organized as follows. Section 2 discusses related work on computer supported cooperative work, collaboration software, and collective intelligence applications. Section 3 describes the action research methodology used for this study. Section 4 provides a description of the diagnosing processes undertaken to understand the unique needs of the special education domain. The <sup>fi</sup>fth section describes the design and development of the DDtrac application. The sixth section describes the longitudinal trial and survey used to validate that the software meets the needs of the target user population. Finally the discussion and conclusions sections describe how the results of this study can be used by future application developers to improve their ability to develop collective intelligence applications.

## 2. Related work

The explosion of the Internet and the emergence of new web based applications have led to a number of predictions about how computer systems will change in the coming decades. Experts predict web technologies will be used to create a tenfold increase in the capabilities of collaborative technologies by 2012 [43]. Others have gone further and called for a new discipline called “Web Science” that focuses on the Internet as a platform for decentralized information systems that empower individuals, invigorate collaboration, promotes social creativity and are dedicated to universal usability [9,64]. The increase in the ability of groups to collaborate virtually has the potential to have a dramatic impact on the nature of interaction within and across organizations and on the shape of organizations themselves [74].

These future web based collaboration platforms have their foundation in computer-supported cooperative work research conducted over the past 20 years. Computer-supported cooperative work is the use of computers for communication within and among work groups [36]. This research includes work on virtual teams [14,15,20,44,45,69], group support systems [17,19,21,50,51,57] and knowledge management [1,5,32,37,54].

Collaboration software consists of components and services that enable individuals to <sup>fi</sup>nd the information they need and to be able to communicate and work together to achieve common goals. The common elements found in many collaboration platforms include technologies to improve transactive memory and the situational awareness of the group [15,47]. Research on asynchronous virtual teams suggests that participants in asynchronous groups rely heavily on task-speci<sup>fi</sup>c representations of situations and goals to enable them to quickly spot changes and remember what is going on in the group [48,59]. This suggests that collaboration is improved when it utilizes software tailored to the speci<sup>fi</sup>c needs of the group.

One of the primary goals of collaboration systems is to enable the effective, ef<sup>fi</sup>cient sharing of information among group members. The predominant examples of applications that support virtual collaboration and information sharing have been labeled as “Web 2.0” [53]. These applications do more than allow collaboration among distributed users, they are targeted at harnessing the collective intelligence of many people to improve understanding and decision making. Collective intelligence can be de<sup>fi</sup>ned as an intelligence that emerges from the collaboration and competition of many individuals [3,38,60]. It is suggested that collective intelligence can help overcome ‘groupthink’ and individual cognitive bias and can result in enhanced intellectual performance [3].

Collective intelligence has been gaining momentum as new tools supporting collaboration have become available. For example, Web 2.0 technologies support collective intelligence by enabling users to quickly, easily, and securely share their ideas with others, combining <sup>fl</sup>exibility with the ability to control and manage parts of the interaction [68]. The three technologies receiving the most recent attention as a medium for promoting the collective intelligence of groups are discussion forums, blogs, and wikis [4].

The concept of collective intelligence is now receiving attention from researchers and practitioners interested in tackling problems in a variety of domains. One study has examined the use of corporate wikis to enhance customer relationship management [68]. Other studies have examined the use of blogging by organizations. One of these studies examined blogs as a mechanism for decentralized, informal knowledge management [13] and another examined the motivations that drive individuals to contribute to blogs [49]. Collective intelligence applications are also being explored by businesses interested in using it for collaborative innovation [23] and by researchers interested in addressing systemic problems like climate change [42]. These studies help us understand how existing collective intelligence tools can be used to further the information management activities of organizations but do little to illustrate how these tools can be utilized to create the new application forms that will drive “Web science” in the future.

Improving the ability to share and understand special education data has received only limited attention from researchers to date. Several projects have explored the use of video to improve assessment of children with special needs. These projects have included Walden Monitor [71], and Abaris [33–35]. The Abaris system, for example, is an automated capture application and decision support system which includes a web cam for capturing video and audio data, a high-quality wireless microphone for voice recognition, and a digital pen for writing grades on the specially printed paper [33–35]. The Abaris system is designed speci<sup>fi</sup>cally to automate the capture of data related to “applied behavior analysis”<sup>3</sup> for young children with autism.<sup>4</sup> Researchers have also investigated the use of video for capturing and understanding student behaviors [27]. These tools are focused on the acquisition and analysis of rich data which can be used to provide a detailed understanding of speci<sup>fi</sup>c students. However, processing and understanding video data can be a very time consuming process and is not appropriate (or feasible) in many special education environments.

This research is interested in creating a special education application that can be used with students with different disabilities and across a wide range of settings (including those where video capture is infeasible). It focuses on the creation of a collective intelligence application that reduces the amount of time required to collect and analyze daily progress data and improves understanding of the individual student's special needs, and decisions regarding education and treatment. The opportunities for using collective intelligence applications in education are enormous. Schools are responsible for managing student education for 12 to 14 years, across multiple developmental milestones and multiple teachers teaching different subjects. This creates the need for asynchronous virtual collaboration tools to create a meaningful history for the student. This is especially true for the 15% of students that are at-risk and the 5% of students that require intensive special education support [2].

![](/api/attachments/AUG82B5B/fulltext/images/47e5f38f46148de978d9c8b17806535dc74d7454b98213720c78aaa2eb4de78b.jpg)  
Fig. 1. Action research cycle [7].

## 3. Research methodology

The study uses an action research methodology in which the community under study actively participates in the research [7,8,72]. Action research is a cyclic process of investigation that includes diagnosing a problem, planning of actions, taking action, evaluating results and specifying learning. The goal of action research is to produce solutions to the current problem and also to advance knowledge about the problem domain under investigation, thus producing exceedingly relevant research <sup>fi</sup>ndings [7,8]. Fig. 1 illustrates the basic action research process.

The project was divided into several major phases as illustrated in Fig. 2. In the project de<sup>fi</sup>nition phase the basic requirements for a data capture application were identi<sup>fi</sup>ed by the researcher working in collaboration with therapists with experience in both home and school based interventions. A design was created and a stand-alone prototype system was developed (See Fig. 2). The stand-alone version of the DDtrac system was deployed and used in a home therapy program for more than two years, then the system was evaluated and shortcomings were identi<sup>fi</sup>ed. A web based prototype was then developed to provide more support for distributed teams and to address other shortcomings identi<sup>fi</sup>ed in the stand-alone system.

The initial web based system was used for two years, again exclusively in a home therapy setting. The software was installed on a secure web server and users were provided access to the tool, both when interacting with the student and elsewhere for reviewing progress and creating reports. The decision to revise the web based prototype centered on the desire to make it available to a larger population of students. Interviews were conducted with school administrators and special education teachers to help identify additional features necessary for the multi-student system. Several additional features were added to the system based on feedback provided by the special education practitioners. The software was then evaluated by the users and through surveys given to special education practitioners from a variety of settings. The revised system was redeployed and used, not only in the home therapy program, but also in the special education classroom at the individual student's school and at several other special education sites (with 275 students in all).

This study involved working with the special education community to gather data, and design and implement a solution to improve the ability of educators and therapists to capture daily student data and assist special education practitioners in determining appropriate interventions for their students. The study actively involved some of the participants in the design, deployment, and implementation of the resulting system. They also participated in discussing the impact of the project on their ability to effectively work with the children they serve.

## 4. Understanding special education data needs

There has been little prior work investigating how information technology could be used to support special education practitioners in documenting student progress (as mandated in IDEA 2004 and No Child Left Behind). The <sup>fi</sup>rst step to understanding special education data management needs was to diagnose the needs of special education teachers, therapists, and parents in terms of types of data collected, communication needs, work<sup>fl</sup>ow patterns, and perceived limitations of current approaches to data collection and analysis. This process served two primary purposes. First, it helped to determine the functionality necessary for the system being developed. Second, it is a reference that can be used for evaluating future technologies applied to special education progress monitoring. The diagnosis process included the following activities conducted prior to the development of the initial prototype:

• Reviewing special education literature to identify the primary education and therapy interventions conducted in home therapy, clinical settings and at schools [e.g., 11,18,22,25,29,39,62,65,66].

• Attending and participating in more than 500 Discrete Trial Applied Behavior Analysis (ABA), Speech Therapy, Occupational Therapy, Music Therapy and Relationship Development Intervention (RDI) therapy sessions and group meetings for an autistic child (participation involved working in tandem with a trained therapist). Thirty of the ABA and RDI therapy sessions were video recorded.

![](/api/attachments/AUG82B5B/fulltext/images/b6396f642ad879a9a2e8c6787a16eba2c87e1edea89a7b255ca9af9b2645a137.jpg)  
Fig. 2. Project activity <sup>fl</sup>owchart.

• Consulting with individuals from the “Lovaas Institute for Early Intervention” at UCLA, “Project Pace” in Oregon, and “The Connections Center” in Houston. The consultations included training to perform ABA and RDI interventions as well as detailed discussions of the data collection and evaluation processes recommended for each intervention.

The diagnosis process also included additional activities conducted prior to designing the revised web-prototype:

• Interviewing 21 special education teachers, therapists and administrators from local school districts and in private practice;

• Reviewing a variety of sample Individual Education Programs (IEP) available on the Internet and from connections within local school districts. Over 4000 IEP objectives were reviewed as a part of this process [6,41,52].

The diagnosis was primarily undertaken to provide a detailed understanding of the data collection and analysis needs of individuals working with children with intensive needs. A hermeneutic interpretation of the documentary artifacts was used to provide a detailed understanding of the special education domain [e.g., 10]. Methodologically, the different sources of data were analyzed using a selective reading approach. Each document was read several times by a single researcher asking: “what parts of this document illustrates the need for information related to student performance,” and “is the way performance is measured clearly de<sup>fi</sup>ned in this document?” If the performance measurement was not clearly de<sup>fi</sup>ned in the document then a third question was asked: “how could data be taken to meet the performance measurement need described in this document?” Conversational interviews were then conducted with special education practitioners to verify that the researcher's perceptions of data collection needs were viewed similarly by practitioners working in the <sup>fi</sup>eld. The process was cyclic, in that documentary evidence was examined, some interviews were conducted, additional documentary evidence was obtained and the process was repeated until the variance between interpretations of the researcher and the practitioners was minimized. The hermeneutic evaluation helped create an understanding of the basic data collection practices, communication mechanisms, and analysis needs of practitioners working in a variety of special education <sup>fi</sup>elds.

The observation of actual therapy sessions and group meetings revealed that special education teams engage in two primary decision making tasks. The <sup>fi</sup>rst is a daily decision making task to help decide what needs to be focused on during a given day or an individual work session. This requires reviewing past data, deciding which targets are mastered, determining the objectives that need the most work (or have not been worked on recently) and reading notes from other practitioners working with the child. If the daily review suggests that the student should be working on an objective that the staff member is unfamiliar with, the staff member also needs to check the detailed description of the objective to determine how it is being taught.

The second type of decision making task is performed weekly, biweekly or monthly (depending on the needs of the child) to determine if the child is making adequate progress towards his/her objectives and make any necessary adjustments to help the child learn more effectively. Using manual data collection procedures often involves transferring some of the paper-based data to spreadsheets to allow it to be charted as well as reading the daily notes taken by individuals actually working with the child. The remainder of this section describes the types of data used to support these two types of decision making tasks.

## 4.1. Performance data

The diagnosing process revealed there are three primary classes of performance data collected to support the education of individuals with intensive needs: instructional data, social data and behavioral data. Instructional data represented students' measurable performance on academic or other structured tasks (e.g., life skills). The data used to evaluate student performance on instructional tasks varies depending on the type of instructional objective being learned and are summarized in Table 1.

Social data is used to track social behaviors that are encouraged during social interactions with teachers, therapists, or other students but that do not have speci<sup>fi</sup>c instructional tasks associated with its completion. Unlike instructional data, social data is taken based on observation of spontaneous, or structured social interactions in which the student participated (e.g., [25]).

Frequently special education students with intensive needs also have associated emotional and behavioral disorders [24]. Prior research has identi<sup>fi</sup>ed 34 problem behaviors frequently tracked for children with developmental disabilities [30]. Behavioral data collection is driven by two factors. First, it is necessary to track behavior episodes to determine if efforts to minimize problem behaviors are effective (e.g., [56]). Second, if a behavior episode results in an injury to a child or staff there are certain reporting requirements that must be met to comply with legal mandates. Typically behavioral data collection includes a wide variety of quantitative information documenting the behavior episode including: the behaviors exhibited by the student, the duration of the behavior, the context that resulted in the occurrence of the behavior (trigger and location), interventions used to stop the behavior, and any consequences the student received as a result of the behavior. The emphasis in data scale selection is on operationally de<sup>fi</sup>ning behaviors or performance in a detailed enough fashion so that independent observers can measure change in performance on instructional tasks or of speci<sup>fi</sup>ed behaviors [63].

## 4.2. Daily communication data

Usually special education students have many people involved in their education and therapy team. Students can receive these services in school, in home therapy programs, and in clinical outpatient environments. Education teams can also include consultants from other regions of the country, especially in areas where there are limited numbers of local professionals available. This can lead to major logistical problems, trying to keep all providers working towards the same goals and modifying those goals in response to the child's progress. Even in environments where a student receives all services in the same school, therapists frequently travel from school to school and have limited time to consult with other members of the education team regarding each student they may see.

In manual data collection environments daily communication needs are met through daily notes [28]. These notes are used to describe student mood and overall performance on tasks. Any major dif<sup>fi</sup>culties are mentioned as are any successes or breakthroughs [12,40]. Frequently daily notes can include questions to other team members or suggestions for revising the way speci<sup>fi</sup>c tasks are accomplished. This qualitative data is usually the only way to capture and communicate the complexity of the student's performance or behavior in context [63].

Data collection types.

<table><tr><td></td><td>Source</td></tr><tr><td>Correct/incorrect</td><td>Hayes et al. [28]Sundberg and Partington [64]</td></tr><tr><td>Discrete trial scale (correct/incorrect, correct/incorrect with prompt, non response)</td><td>Calouri and Hamblen [12]Lovaas and Smith [40]</td></tr><tr><td>Record verbal, physical or visual prompts given</td><td>Calouri and Hamblen [12]Frost and Bondy [22]</td></tr><tr><td>Likert scales</td><td>Observation of practiceOregon Department of Ed [52]</td></tr><tr><td>Scores</td><td>Hosp and Hosp [31]Oregon Department of Ed [52]</td></tr><tr><td>Time spent</td><td>Hayes et al. [28]Hosp and Hosp [31]Oregon Department of Ed [52]Scattone et al. [62]</td></tr><tr><td>Counts or tallies</td><td>Brownell [11]Scattone et al. [62]</td></tr></table>

## 4.3. Objective data

Research indicates that children with intensive needs learn best in highly structured environments where objectives and targets are taught in a consistent fashion [40,58]. This requires the special education team to document all aspects of how a particular objective will be taught, including the instruction(s) given when a child is asked to perform the objective (e.g., “Do this”), the acceptable response, and what cues are to be given to assist the child in providing the correct response [70].

In schools speci<sup>fi</sup>c information on what is being taught is documented in the student's Individual Education Program (IEP), which establishes long-term goals and short-term objectives tailored to the needs of the individual student. These documents are referred to when questions about what is being taught arise. Interviews with teachers and therapists revealed that many of them also develop additional documentation describing in greater detail how best to work with the student on particular objectives.

## 5. Design and development of the DDtrac application

DDtrac is an information system designed to collect and summarize information that is used to improve decisions related to education and therapy options for special needs children. Similar to Web 2.0 applications, it allows teachers to quickly, easily, and securely share their ideas with other members of the education team. It combines <sup>fl</sup>exibility and control with the ability to share and analyze domain speci<sup>fi</sup>c data. Fig. 3 shows the current DDtrac system architecture, which follows a basic hierarchical structure with functionality grouped into four major areas: data entry, creating goals and objectives, data analysis, and administration.

The DDtrac application began by supporting instructional and behavioral data entry and instructional goals for a single student. It allowed for data entry on a PC. As the therapists in the longitudinal trial used the initial system two primary limitations emerged. First, access to the system was restricted to a single PC located in the therapy room, making it dif<sup>fi</sup>cult to evaluate student progress when not working with the student. It also made it dif<sup>fi</sup>cult to take data in other locations (something that became more important as the student grew older). In addition, the initial prototype did not support all of the types of data and analysis tools necessary to effectively monitor the student's progress (e.g., social data collection, charts and reports). The application was revised to make it web based and to add the additional functionality that was perceived as missing in the initial system.

A year later the web based prototype was revised to make it suitable for a larger population of students. This required a revision of the data model, the addition of a number of administrative features, and support for additional types of data. The current DDtrac system has evolved into a web based program capable of supporting the functionality described in this section, which can track data for hundreds of students, and which allows data input from a Mac, a PC or a PDA with a connection to the Internet. The section below describes its functionality in more detail.

## 5.1. Data entry

The primary purpose of DDtrac is to support the sharing of data between therapists working with special education students. It supports data collection for instructional objective and targets, observed social interactions, behaviors and narrative observations. DDtrac also supports commenting, which allows special education practitioners to provide insights on how best to work with a particular student.

## 5.1.1. Quantitative data entry

All of the data entry (except for the narrative comments) utilizes checkboxes, radio buttons, and dropdown lists to minimize the amount of time the user spends on data entry. As shown in Fig. 3, data entry is divided into three areas, instructional, social and behavior. Fig. 4 illustrates a typical data collection process used when collecting instructional data. DDtrac supports all of the data collection types identi<sup>fi</sup>ed in Table 1.

![](/api/attachments/AUG82B5B/fulltext/images/b14e35967e966101551e1af7a0fcb9cc025bfb9931db6927436391f0b7117522.jpg)  
Fig. 3. DDTrac architecture.

![](/api/attachments/AUG82B5B/fulltext/images/aa0db4cb44fbf0c0d10ef4ef028244e898f58ffef869f6c3ecb309ca1f6513a6.jpg)  
Fig. 4. DDTrac instructional data entry.<sup>6</sup>

## 5.1.2. Qualitative data entry

Qualitative data is an important part of the information exchanged in many collective intelligence environments, including special education. Observational comments re<sup>fl</sup>ect the special educator's attempt to create a written account of what he or she hears, sees, experiences, and thinks in the course of observing the child in a particular context.

DDtrac utilizes a student centric “blog”to capture qualitative data related to a student's daily performance, mood, and behavior. These qualitative observations are an important mechanism for communicating recent changes in the child and in the child's educational programs between distributed team members. The student centric blog allows parents and other practitioners to make comments on the observations of other team members allowing them to share insights related to the observations. This facilitates the use of the collective intelligence of the entire group to solve problems arising for speci<sup>fi</sup>c students. The student centric blog also allows the semantic tagging of the narrative comments. The semantic tags are keywords chosen by users that create overlapping associations between observations that can be used for later retrieval and analysis of the qualitative data.

## 5.2. Goals, objectives and targets

One of the important characteristics of the education programs for special needs students is that they are highly individualized. As such, practitioners need a tool that can be customized to the needs of individual students. This includes the ability to de<sup>fi</sup>ne details related to how the speci<sup>fi</sup>c objective is being taught (e.g., the instructions are given to the student and any prompts that are given), what response is expected, what type of data is collected, and what level of performance the student must demonstrate in order to meet their goals.

DDtrac allows three different types of goals to be de<sup>fi</sup>ned: instructional goals, social goals, and behavior goals. The descriptions of these goals are under the complete control of the education team. Team members can view the goals at any time in order to determine how the goal is currently being taught.

## 5.3. Data analysis

DDtrac makes it easier for special educators to better meet the needs of their special education students. First, the data tracking portion of DDtrac was designed to highlight the objectives and targets students need to work on most (See Fig. 4). Each objective shows the last date data was collected for it, as does each individual target. It also shows the student's recent average performance on the target. Mastery of each target is computed automatically. This allows the student's progress towards goals to be maintained by staff with limited intervention from the special education teacher.

In addition, DDtrac's reporting and charting features allow special education teachers and therapists to examine student progress and modify student's objectives and targets to maximize a student's learning outcomes. There are several types of reports and charts available in DDtrac which allow teachers to interpret progress in a variety of different ways (e.g., rate of mastery, current performance levels). Fig. 5 shows three of the charts provided by DDtrac to allow assessment of student progress. The stacked bar chart shows how individual behaviors contribute to the overall number or duration of behaviors observed for a student. The line chart show a student is performing on multiple instructional or social targets. Finally, the mastery chart shows the rate a student is mastering targets as they progress towards their IEP goal.

## 5.4. Administration

Additional functionality was added to the <sup>fi</sup>nal web based prototype to meet other identi<sup>fi</sup>ed needs. For example, the <sup>fi</sup>nal web based system includes access restrictions that control which users can see a student's data (and what level of access they are granted), password protection, an encrypted database, and secure data transfer so that the privacy of student data can be maintained. In addition, because data related to individual students can be available in other student databases, an ability to import and export all student data was included in the <sup>fi</sup>nal system.

![](/api/attachments/AUG82B5B/fulltext/images/e3bff4c3cdf6640b3fa82a91051a934833bf8301c0a4bbc6e674a29ba6958b98.jpg)  
Fig. 5. DDTrac charts.

## 6. Evaluation of DDtrac

Once the prototype DDtrac system was developed, it was evaluated using a multi-year <sup>fi</sup>eld trial with a single child with autism involved in both home therapy and special education in school. The initial web based system was also evaluated through short hands-on demonstrations with 48 special education practitioners.

## 6.1. Longitudinal field trial results

Following the initial systems development, DDtrac was deployed in a multi-year trial with one student with autism. The autism home therapy domain is ideal for studying collective intelligence because best practices dictates that very detailed data be shared between all participants so that the children can be taught in exactly the same way by all individuals working with them [39,40,66]. The parents and therapists working with the student all had a history of sharing data in paper form before taking part in this study and actively participated in the design, evaluation and redesign of the DDtrac system. The DDtrac system was used as the exclusive data collection and analysis tool for more than four years<sup>5</sup> (1260 work sessions), with over 85,000 individual quantitative data points collected.

Numerous methods were used to evaluate the DDtrac system throughout the longitudinal trial. This included observing and video recording 30 therapy sessions to determine how the system was being used for their daily data collection (e.g., how often the system was referred to prior to an educational task and when data was entered into the system). It also included attending 45 group meetings and observing how the data analysis tools were used to understand and adapt the student's therapy goals. Counts of the frequency and timing of these activities were made by a single researcher. The longitudinal trial participants were also asked to evaluate the system using questions derived from a measure of small business user satisfaction with information technology [55]. This evaluation showed how the application was being used to support therapists and improve understanding of the student's learning patterns.

The longitudinal trial participants indicated that the DDtrac application reduced the amount of time they spent taking data (self-reported). They primarily took instructional data during or immediately following the speci<sup>fi</sup>c instructional activity. Feedback from the therapists and the evaluation of the instructional data taken revealed that the automatic computation of mastery, the sorting of goals and the display of dates when objectives last had data collected did help them prioritize what they worked on daily. Behavior and social data, by contrast, was generally taken following a behavior episode or a social interaction. This was primarily because the interaction with the student during problem behavior or social “play” time made it dif<sup>fi</sup>cult to concurrently take data. Therapists left narrative comments in 81.5% of the sessions. While the majority of these comments were short (they averaged 52 words) the therapists felt they were very useful for communicating information about how student mood, speci<sup>fi</sup>c instructions, and other intangible factors impacted performance. The therapists reported the narrative comments were an essential communication mechanism that allowed them to provide more consistent, effective education to the student.

The participants all indicated that they appreciated the tool's ability to communicate progress in group meetings, the ability to use the reporting and charting features to meet their mandated reporting requirements, and the overall usefulness of the tool in assessing student progress. Observations of the 45 group meetings supported this, showing that DDtrac reports and charts were the primary tool used for understanding progress and adapting objectives in 100% of the meetings. All participants felt the information provided by DDtrac was clear and useful. However, the longitudinal trial participants did not all feel the system did all it could to improve their productivity. One participant commented that the lack of standards surrounding writing goals and objectives for special education students and differing reporting requirements for agencies and school districts meant she often had to rewrite the goals and reprocess the data for each of her different target audiences.

The biggest bene<sup>fi</sup>t reported by all of the study participants was the ability to analyze long-term educational and behavior patterns, something they could not do prior to adopting DDtrac. For example, the student had received numerous interventions over the four years covered by the longitudinal trial (e.g., changes to medication, diet, and types of educational interventions used) and the data provided by DDtrac enabled the team to have an unbiased measure of whether or not a particular intervention had an impact either on the educational outcomes or on the behaviors of the student. Other bene<sup>fi</sup>ts the therapists reported included an improved ability to assess progress and make changes to the child's instructional goals and an improved view of the data which helped them know what needed to be worked on during therapy sessions.

## 6.2. Survey results

Surveys were administered to groups of practitioners from local school districts and local special education schools. A total of 48 people participated in the demonstration/survey sessions and 40 of the participants returned questionnaires (See Appendix A). The survey was used to determine if the revisions to the DDtrac system met the needs of a larger segment of the special education community. All survey participants heard a 15 min presentation on DDtrac and then interacted with the system for 45 min. The survey respondents indicated that they anticipated the system would provide signi<sup>fi</sup>cant bene<sup>fi</sup>ts in their ability to collect analyze and communicate data (see Table 2). One of the largest problems expressed by the survey participants was a perceived need to collect data on paper and then transfer the data to DDtrac (which impacted productivity responses). Most participants agreed that access to a handheld device or a laptop would eliminate this problem. None of the respondents were aware of a comparable product that could be used to collect and analyze special education data.

## 6.3. Specification of learning

The results of the longitudinal trial and the survey suggest that collective intelligence applications should support the following six design patterns:

## 1. Task speci<sup>fi</sup>c representations of situations and goals:

Consistent with prior research on asynchronous virtual teams [e.g., 48,59] results of this study suggests that it is important that the system support views of the task that are tailored to the particular domain. In this case, practitioners in the longitudinal trial had speci<sup>fi</sup>c information that they needed to understand about the specialized needs of individual children in order to work with them effectively. Both the therapists in the longitudinal trial and the survey participants found the interface intuitive and easy to use. Familiarity with the terminology and the domain enabled most survey participants to begin “playing” with the application before any instructions on how to use it were given. In addition, most participants (72%) indicated that the program would be useful to tracking data for their current students and for communicating progress to parents (91%). Without an interface that was customized to the domain it would have been dif<sup>fi</sup>cult for the system to satisfy their data communication needs.

Table 2  
Bene<sup>fi</sup>ts of using DDtrac.

<table><tr><td></td><td>Percent perceiving benefit</td><td>Chi square</td><td>Sig.</td></tr><tr><td>Enhance ability to assess student performance</td><td>81%</td><td>26.63</td><td>&lt;0.001</td></tr><tr><td>Useful for tracking data for current students</td><td>72%</td><td>37.14</td><td>&lt;0.001</td></tr><tr><td>Intend to use DDtrac (if provided access)</td><td>72%</td><td>16.56</td><td>0.011</td></tr><tr><td>Printable reports and charts are useful</td><td>100%</td><td>95.31</td><td>&lt;0.001</td></tr><tr><td>Useful for communicating student progress to parents</td><td>91%</td><td>37.42</td><td>&lt;0.001</td></tr><tr><td>Increase my productivity</td><td>66%</td><td>13.03</td><td>0.043</td></tr><tr><td>Easy to use</td><td>65%</td><td>9.56</td><td>0.144</td></tr></table>

## 2. Sharing of different types of data:

Collective intelligence applications need to support the sharing of information and ideas such that the group's understanding of the problem domain is improved allowing for better decisions to be made [53]. Thus, a collective intelligence application needs to support the capture of all of the information necessary to understand and evaluate the speci<sup>fi</sup>c problem. In the special education domain this included capturing detailed daily quantitative data related to the student's performance on educational tasks as well as qualitative data related to the student's mood and other background information that could help others in the education team to understand what factors might have in<sup>fl</sup>uenced the student's performance on that particular day.Subjects in the longitudinal trial used all of the data collection capabilities of DDtrac on a daily basis and found the different types of data enabled them to work more effectively with the child. Quantitative data was essential for determining how the student was progressing and for moving the student's program forward. However, the qualitative data was equally important because it enabled team members to communicate with each other about how best to work with the child. The longitudinal trial participants indicated that both types of data contributed to their understanding of the student and how best to work with him.

## 3. Exchange of ideas among team members:

Collective intelligence applications are targeted at domains where groups create the information necessary to understand the intricacies of the problems faced and where the ability of group members to interact face-to-face is limited or nonexistent. In these environments it is essential that the application support the seamless sharing and commenting on ideas and experiences shared by others. This enables group members to learn from each other between meetings (or without meetings). In the DDtrac application this is seen in the ability of other team members to comment on narrative observations of others. This enables teachers to comment on the problems raised by the paraprofessionals or regular education teachers working with the students they serve.

Analysis of the daily narrative comments taken during the longitudinal trial reveals that they were frequently used to communicate ideas between therapists. For example, in the longitudinal trial one therapist asked “When we are asking \_\_\_\_\_ what his name is are you showing him his own picture; nothing at all; or a variety of pictures? What about for ‘How are you?/How are you feeling?’.” Another therapist commented back “I am showing \_\_\_ his picture …” The student centric blog also allows parents the opportunity to comment on home experiences that might be relevant to the teacher – but which were dif<sup>fi</sup>cult to share before. The longitudinal trial participants agreed that the ability to exchange ideas through DDtrac enabled them to more quickly determine which educational practices worked best in speci<sup>fi</sup>c situations.

## 4. Multiple means of retrieving and analyzing data:

Frequently, data needs to be examined from a variety of different perspectives to determine if appropriate progress is being made or if progress could be improved by approaching the problem (or in this case teaching) in different ways. The DDtrac system provides a variety of charts and reports to allow practitioners to analyze data in a variety of different ways, by allowing for semantic tagging of the observation comments to allow for retrieval and analysis of qualitative data, and by allowing for the downloading of data so that users could perform their own analysis of the data.

Subjects participating in the longitudinal trial reported that when the charting capabilities were added to the system their ability to understand how the child was progressing was dramatically improved. The parents indicated that the charts were the principle tool they used to communicate progress to other people working with their child (e.g., doctors and dieticians). Results of this study indicate that the ability to understand and remix data in surprising ways is one of the biggest bene<sup>fi</sup>ts of collective intelligence applications.

5. Incorporate user feedback into and about the system:

The action research methodology utilized in this research was critical to the success of this project. The iterative process of incorporating changes in the application as the users suggested them enabled the resulting application to better meet the needs of the target population. Central to the success of this approach was the use of lightweight programming models that allowed extensions to the system to be added almost as soon as they were conceived. Using the web–page as the primary delivery unit allows new pages to be added and the system to grow as new needs were identi<sup>fi</sup>ed – without impacting other parts of the system. It also allowed new features to be available to the entire user community immediately instead of waiting for the next release. This <sup>fi</sup>nding is consistent with recommendations made for developing Web 2.0 applications, which have many of the same design goals as the collective intelligence applications being presented here [53].

## 6. Universal usability:

The <sup>fi</sup>nal requirement for collective intelligence applications is universal usability. This is one of the requirements proposed for the new “Web science” discipline [9] that is equally important in the special education domain [26]. Users in the longitudinal trial performed data entry using different hand held devices (a palm device and a Nova mini tablet PC) and data analysis on both Windows and Macintosh devices. The availability of the system anywhere and the usability of the system on different devices were central to the success of the project.

## 7. Discussion

This research focuses on the creation of a collective intelligence application that allows for the easy collection and summary of special education data. It can also be used to help information systems developers gain a better understanding of the requirements of collective intelligence applications in general. There were also lessons learned about how best to approach the development of such a system.

## 7.1. Implications for research and practice

Today's online collective intelligence applications (e.g., online discussion forums, wikis and blogs) do a good job of encouraging people to share their ideas and contribute to the knowledge of a larger community. However, these systems are not very good for capturing and analyzing domain speci<sup>fi</sup>c data. This project demonstrated the usefulness of a custom collective intelligence application that combined task speci<sup>fi</sup>c data collection and analysis features with a student centric blog that facilitates information sharing between users. This synthesis of traditional data capture and analysis with emerging Web 2.0 type solutions represents an emerging area of application development.

The process of building a specialized collective intelligence application begins with understanding how data is used in a particular domain. It then requires developers to create an application that not only captures the necessary data, but also has the functionality necessary to harness the collective intelligence of the ultimate system users. The six requirements of collective intelligence applications presented in this paper can serve as a design pattern that can be used to help developers achieve this goal.

## 7.2. Lessons learned

There were a number of lessons learned that could improve future projects. First, although a detailed understanding of the problem domain is essential to a successful project, it is impossible to understand all of the requirements or desirable features of such a system before implementation of the initial system prototype. It is important to design the system such that it is easily extensible when new features are identi<sup>fi</sup>ed. The initial system developed in this project only resembled the <sup>fi</sup>nal one in the most super<sup>fi</sup>cial sense. The screens were different, the data models changed and the feature set was dramatically expanded. The ability of the system to evolve represented an important aspect of the overall system design.

Although an action research methodology was used, it was impossible for the system developers to meet all of the unique needs of the user population. This suggests it is important to design some level of customizability into the system itself. For example, it was good that DDtrac allowed users to create reports and charts using the available data. It would have been better if the system allowed users to design their own reports and charts containing only the data they were interested in and allowing them to format the output to conform to different reporting requirements. Subjects participating in the longitudinal trial and surveys indicted that it was good that DDtrac supported the different data collection modes suggested in prior research [e.g., 11,22,40,62,65]. However, several subjects indicated they would have liked to see modi<sup>fi</sup>cations to some of the scales provided, to better meet their individual data collection styles or needs. This suggests that it would have been better if the system would allow users to add their own data collection mode based on the unique needs of their students.

Finally, it is clear that user involvement in the project was essential to its success. Users reported bugs and usability problems to the development team and generated the ideas that were responsible of most of the enhancements to the system. On this project the developers encouraged users to report problems they found with the system and regularly asked users what parts of the system caused them the most dif<sup>fi</sup>culties. This process not only resulted in added features, it also allowed usability issues to be identi<sup>fi</sup>ed and improved for the entire user population.

## 7.3. Limitations

The DDtrac project did not include medication, nutrition, and physical <sup>fi</sup>tness data, which are frequently tracked for children with a variety of special needs. Adding this type of data into future special education applications has the potential to improve the ability of special education teams to understand student progress.

This is a single, detailed action research case carrying limitations on its proven generalizability. For example, although the participants in the longitudinal <sup>fi</sup>eld study were very willing (and even enthusiastic) about using collective intelligence applications in their work, the study used participants already accustomed to sharing data and collaborating in the educational process. Thus, this study did not allow for user resistance to the use of these kinds of (potentially) invasive technologies to be assessed. The survey of practitioners working in a variety of special education environments suggested that the majority of these practitioners (72%) would be highly inclined to use the DDtrac application. However, these practitioners did not have the opportunity to use the system to collect and analyze real-world data for their students. Thus, their actual use of the system and willingness to share data could not be measured. Future research is necessary to assess issues surrounding the adoption and use of collective intelligence applications by a wider population of special education practitioners including: how teachers feel about using these kind technologies; how these technologies change information sharing between parents, administrators, and teachers; and how these technologies impact educational decision making.

## 8. Conclusions

The primary objective of the DDtrac project was to develop and evaluate a collective intelligence application that supports the unique needs of the special education sector. The project included the design, development, distribution, and evaluation of such technologies through a longitudinal trial and a series of surveys. The methodology used involved detailed analysis to special education data collection and analysis needs and practitioner participation in the design process. Thus, choice of functionality and the design of the user interface were based on a thorough understanding of the coordination, administrative, and technological issues facing special education teachers and therapists.

Special education programs may be viewed as a decentralized “virtual” organization characterized by an unstable network structure, in the sense that most special education students have many practitioners working with them and frequently these education teams turnover every year. This may jeopardize sharing of knowledge and cause loss of learning about how best to work with the individual student [16]. Without the ability to learn from the past many opportunities to improve student outcomes could be lost. One way to improve knowledge transfer between teachers and therapists and across time is to use a collective intelligence system like DDtrac to provide practitioners with critical information that will allow them to do the best possible job with each student they serve.

The DDtrac system improves collective intelligence by storing goals and objectives, historic performance data, and behavior trends and triggers. With DDtrac, practitioners can easily share information about student performance and share practices that work well. This simple but effective way of improving access to organizational memory may contribute to the practitioners' ability to make better decisions. It also improves the information <sup>fl</sup>ow among the parents, therapists, and teachers involved in the longitudinal trial and improves the overall consistency of the child's education programs. The system developed as a part of this project is currently being used with 275 students in four states. Thus, it can be claimed that some of the goals of the project have been achieved.

It is clear that the practitioners involved in the longitudinal trial found the improved <sup>fl</sup>ow of information has affected their way of working by reducing the amount of time they spend collecting and analyzing data allowing them more time to focus on the child being served. The result has been more/better information available for group meetings resulting in more substantive discussions as opposed to bare information exchange.

The <sup>fi</sup>ndings of this study show strong support for the use of a collective intelligence system like DDtrac to manage the large amounts of data associated with special education interventions. The results indicate that this type of long-term data is useful for monitoring speci<sup>fi</sup>c educational outcomes and behavior outcomes. In addition, the focus on improving access to and use of data analysis allows education decision makers to better assess progress and helps ful<sup>fi</sup>ll the ultimate goal of improving outcomes for special needs children.

## Appendix A. Survey questionnaire

Please use the following scale for these questions: 1=strongly disagree, 2=moderately disagree, 3=somewhat disagree, 4=neutral (neither disagree nor agree), 5=somewhat agree, 6=moderately agree, and 7=strongly agree.

1. Assuming I have access to DDtrac, I intend to use it.

2. Using DDtrac at my job will increase my productivity.

3. I <sup>fi</sup>nd DDtrac easy to use.

4. DDtrac will enhance my ability to assess student performance.

5. DDtrac will be useful for communicating student progress to parents.

6. DDtrac will be useful for tracking data for current students.

7. I would use DDtrac \_\_\_\_\_ times per day for each student.

8. The ability to print reports & charts directly from DDtrac is very useful.

## References

[1] M. Alavi, D. Leidner, Knowledge management and knowledge management systems: conceptual foundations and research issues, MIS Quarterly 25 (1) (2001) 117–136.

[2] Anonymous, Responsiveness to Intervention in the SLD Determination Process, National Research Center on Learning Disabilities (NRCLD), 2005 Available at: http://www.osepideasthatwork.org/toolkit/pdf/RTI\_SLD.pdf).

[3] T. Atlee, R. Zubizarreta, The Tao of Democracy: Using Co-intelligence to Create a World That Works for All, Writers' Collective, New York, 2003.

[4] S. Baker, and H. Green, Blogs will change your business. BusinessWeek (May 2, 2005), 56 – 67.

[5] S. Bandyopadhyay, P. Pathak, Knowledge sharing and cooperation in outsourcing projects — a game theoretic analysis, Decision Support Systems 43 (2) (March 2007) 349–358.

[6] N.B. Bar-Lev, Examples and Tips of Making IEP Annual Goals Measurable, Wisconsin Cooperative Education Service #7. November 29 1999, Available at http://www.specialed.us/issues-IEPissues/writingiep/GoalsMeasurable.html.

[7] R.L. Baskerville, Investigating information systems with action research, Communications of the AIS, vol. 2, November 1999, (3es), Article No. 4.

[9] T. Berners-Lee, W. Hall, J. Hendler, N. Shadbolt, D. Weitzner, Creating a science of the web, Science 313 (11) (August 2006) 769–771.

[10] R.J. Boreland, Information system uses as a hermeneutic process, in: H.E. Nissen, H.K. Klein, R. Hirschheim (Eds.), Information Systems Research: Contempo rary Approaches and Emergent Traditions, North-Holland, New York, NY, 1991, pp. 439–458.

[11] M.D. Brownell, Musically adapted social stories to modify behaviors in students with autism: four case studies, Journal of Music Therapy 39 (2) (Summer 2002) 117–144.

[12] K.A. Calouri, E. Hamblen, Drill Book, Project Pace, Inc., Oregon, 1996.

[13] S. Cayzer, Semantic blogging and decentralized knowledge management, Communications of the ACM 47 (12) (December 2004) 47–52.

[14] M. Chen, Y. Liou, C. Wang, Y. Fan, Y. Chi, TeamSpirit: design, implementation, and evaluation of a Web based group decision support system, Decision Support Systems 43 (4) (August 2007) 1186–1202.

[15] C.D. Cramton, The mutual knowledge problem and its consequences for dispersed collaboration, Organization Science 12 (3) (2001) 346–371.

[16] W.H. Davidow, M.S. Malone, The Virtual Corporation, Harper Collins, New York, NY, 1992.

[17] A.R. Dennis, J.S. Valacich, J.F. Nunamaker Jr., An experimental investigation of small, medium, and large groups in an electronic meeting system environment, IEEE System, Man and Cybernetics 20 (5) (1990) 1049–1057.

[18] S.L. Deno, Developments in curriculum-based measurement, Journal of Special Education 37 (3) (March 2003) 184–192.

[19] G. DeSanctis, R.B. Gallupe, A foundation for the study of group decision support systems, Management Science 33 (22) (1987) 589–609

[20] C.M. Fiol, E.J. O ' Conner, Identi<sup>fi</sup>cation in face-to-face, hybrid, and pure virtual teams: untangling the contradictions, Organization Science 16 (1) (2005) 19–32.

[21] J. Fjermestdad, and S.R. Hiltz, An Assessment of Group Support Systems Experimental Research: Methodology and Results, Journal of Management Information Systems, 15 (3) (Winter98/99), 7–149.

[22] L.A. Frost, A.S. Bondy, The Picture Exchange Communication System: Training Manual, Pyramid Educational Consultants, Newark, DE, 1994.

[23] P.A. Gloor, S.M. Cooper, The new principles of a swarm business, MIT Sloan Management Review 48 (3) (Spring 2007) 81–84.

[24] P.L. Gunter, K. Callicott, R.K. Denny, B.L. Gerber, Finding a place for data collection in classrooms for students with emotional behavioral disorders, Preventing School Failure 47 (1) (Fall 2003) 4–8.

[25] S. Gutstein, R.K. Sheely, Relationship Development Intervention with Young Children: Social and Emotional Development Activities for Asperger Syndrome, Autism, PDD and NLD, Jessica Kingsley, Philadelphia, PA, 2002.

[26] T.S. Hasselbring, A possible future of special education technology, Journal of Special Education Technology 16 (4) (Fall 2001) 15–21.

[27] G.R. Hayes, L.M. Gardere, G.D. Abowd, K.N. Truong, “CareLog: a selective archiving tool for behavior management in schools,” CHI 2008, Florence, Italy, April 2008, pp. 685–694.

[28] G.R. Hayes, J.A. Kientz, K.N. Truong, D.R. White, G.D. Abowd, T. Pering, Designing capture applications to support the education of children with autism, Proceedings of the 6th international conference on Ubiquitous Computing, Springer-Verlag: Nottingham, United Kingdom, 2004, pp. 161–178.

[29] L.J. He<sup>fl</sup>in, R.L. Simpson, Interventions for children and youth with autism: prudent choices in a world of exaggerated claims and empty promises. Part I: Intervention and treatment option review, Focus on Autism and Other Developmental Disabilities 13 (4) (1998) 194–211.

[30] R.H. Horner, E.G. Carr, P.S. Strain, A.W. Todd, H.K. Reed, Problem behavior interventions for young children with autism: a research synthesis, Journal of Autism and Developmental Disorders 32 (5) (October 2002) 423–446.

[31] M.K. Hosp, J.L. Hosp, Curriculum based measurement for reading, spelling and math: how to do it and why, Preventing School Failure 48 (1) (Fall 2003) 10–17.

[32] A. Kankanhalli, B.C.Y. Tan, K.K. Wei, Contributing knowledge to electronic knowledge repostitories: an empirical investigation, MIS Quarterly 29 (1) (2005) 113-143

[33] J.A. Kientz, G.R. Hayes, G.D. Abowd, R.E. Grinter, Lending a helping hand: using technology to assist: from the war room to the living room: decision support for

home-based therapy teams, Proceedings of the 2006 Conference on Compute Supported Cooperative Work CSCW '06, November 2006, pp. 209–218.

[34] J.A. Kientz, S. Boring, G.D. Abowd, G.R. Hayes, Abaris: evaluating automated capture applied to structured autism interventions, Lecture Notes In Compute Science, Springer, 2005, pp. 323–339.

[35] J.A. Kientz, G.R. Hayes, T.L. Westeyn, T. Starner, G.D. Abowd, Pervasive computing and autism: assisting caregivers of children with autism, Pervasive Computing 6 (1) (January-March 2007) 28–35.

[36] J.K. Kies, R.C. Williges, M.B. Rosson, Coordinating computer-supported cooperative work: a review of research issues and strategies, Journal of the American Society for Information Science 49 (9) (1998) 776–791.

[37] U.R. Kulkarni, S. Ravindran, and R.A. Freeze, Knowledge Management Success Model: Theoretical Development and Empirical Validation. Journal of Management Information Systems, 23 (3) (Winter2006/2007), 309–347.

[38] P. Levy, R. Bononno, Collective Intelligence: Mankind's Emerging World in Cyberspace, Plenum Publishing Corporation, New York, NY, 1997.

[39] O.I. Lovaas, Behavioral treatment and normal educational and intellectual functioning in young autistic children, Journal of Consulting and Clinical Psychology 55 (1) (February 1987) 3–9.

[40] O.I. Lovaas, T. Smith, Intensive behavioral treatment for young autistic children, in: B.B. Lahey, A.E. Kazdin (Eds.), Advances in clinical child psychology, vol. 11, Plenum Press, New York, 1988, pp. 285–324.

[41] Littleton Public Schools, SMART Goals: A Process for Goal Setting, Littleton Public Schools, Littleton, CO, 2004.

[42] T. Malone, M. Kleinm, Harnessing collective intelligence to address global climate change, Innovations: Technology, Governance, Globalization 2 (3) (July 2007) 15–26.

[43] M.E. Mangelsdorf, Beyond enterprise 2.0, Sloan Management Review 48 (3) (Spring 2007) 50–55.

[44] A. Majchrzak, A. Malhotra, R. John, Perceived individual collaboration know-how development through information technology-enabled contextualization: evidence from distributed teams, Information Systems Research 16 (1) (2005) 9–27.

[45] A. Majchrzak, R.E. Rice, A. Malhotra, N. King, S. Ba, Technology adaptation: the case of a computer-supported inter-organizational virtual team, MIS Quarterly 24 (4) (2000) 569–600.

[46] D. Mellard, Understanding Responsiveness to Intervention in Learning Disabilities Determination, National Research Center on Learning Disabilities, May 2005 Available at: http://nrcld.org/publications/papers/mellard.shtml.

[47] R.L. Moreland, L. Myaskovsky, Explaining the performance bene<sup>fi</sup>ts of group training: transactive memory or improved communication? Organizational Behavior and Human Decision Processes 82 (1) (2000) 117–133.

[48] J.H. Morris, C.M. Neuwirth, S.H. Regli, R. Chandhok, G. Wenger, Interface issues in computer support for asynchronous communication, ACM Computing Surveys 31 (2) (June 1999) paper 11.

[49] B. Nardi, D. Schiano, M. Gumbrecht, L. Swartz, Why we blog, Communications of the ACM 47 (12) (December 2004) 41–46.

[50] J.F. Nunamaker Jr., A.R. Dennis, J.S. Valacich, D.R. Vogel, Information technology for negotiating groups: generating options for mutual gain, Management Science 37 (10) (1991) 1325–1345.

[51] J.F. Nunamaker Jr., A.R. Dennis, J.S. Valacich, D.R. Vogel, J.F. George, Electronic meetings to support group work, Communications of the ACM 34 (7) (1991) 40–61.

[52] Oregon Department of Education, Oregon, IEP Goals and Objectives Bank, Oregon Department of Education, Redmond, Oregon, 2005 Available at: http://www. bridges4kids.org/IEP/iep.goal.bank.pdf.

[53] T. O'Reilly, What Is Web 2.0: Design Patterns and Business Models for the Next Generation of Software, O'Reilly Media, Inc., Sebastopol, CA, September 30 2005 Available at: http://www.oreillynet.com/pub/a/oreilly/tim/news/2005/09/30/ what-is-web-20.html

[54] R.S. Poston, C. Speier, Effective use of knowledge management systems: a process model of content ratings and credibility indicators, MIS Quarterly 29 (2) (2005) 221–244.

[55] P.C. Palvia, A model and instrument for measuring small business user satisfaction with information technology, Information & Management 31 (3) (December 1996) 151-163.

[56] M.M. Quinn, R.A. Gable, R.B. Rutherford, C.M. Nelson, K.W. Howell, Assessing student problem behavior, The Center for Effective Collaboration and Practice, January 16, 1998, Available at: http://cecp.air.org/fba/problembehavior/funcanal.pdf.

[57] G.R. Rao, M. Turoff, A hypermedia-based group decision support system to support collaborative medical decision-making, Decision Support Systems 30 (2) (December 2000) 187–216.

[58] P. Reed, P., L.A. Osborne, and M. Corness, Brief Report: Relative Effectiveness of Different Home-based Behavioral Approaches to Early Teaching Intervention, Journal of Autism and Developmental Disorders, forthcoming 2007.

[59] S.H. Regli, C.M. Neuwirth, J.H. Morris, R. Chandhok, P. Erion, G. Wenger, Task-driven design for asynchronous communication, SIGGROUP Bulletin 20 (2) (August 1999) 40–44.

[60] P. Russell, The Global Brain Awaken, Global Brain Inc, New York, 1995

[61] N. Safer, S. Fleischman, Research matters: how student progress monitoring improves instruction, How Schools Improve 62 (5) (February 2005) 81–83.

[62] D. Scattone, S.M. Wilczynski, R.P. Edwards, B. Rabian, Decreasing disruptive behaviors of children with autism using social stories, Journal of Autism and Developmental Disorders 32 (6) (2002) 535–543.

[63] I.S. Schwartz, L.B. Olswang, Evaluating child behavior change in natural settings: exploring alternative strategies for data collection, Topics in Early Childhood Special Education 16 (1) (Spring 1996) 82–101.

[64] B. Shneiderman, Web science: a provocative invitation to computer science, Communications of the ACM 50 (6) (June 2007) 25–27.

[65] M.L. Sundberg, J.W. Partington, Teaching Language to Children with Autism or Other Developmental Disabilities, Behavior Analysts, Inc, Pleasant Hill, CA, 1998.

[66] T. Smith, Discrete trial training in the treatment of autism, Focus on Autism and Other Developmental Disabilities 16 (2) (2001) 86–92.

[67] U.S. Of<sup>fi</sup>ce of Special Education Programs, OSEP State Reported IDEA Data, 2006 Available at: https://www.ideadata.org/arc\_toc7.asp.

[68] C. Wagner, A. Majchrzak, Enabling customer-centricity using wikis and the wiki way, Journal of Management Information Systems 23 (3) (2007) 17–43.

[69] M. Weiser, J. Morrison, Project memory: information management for project teams, Journal of Management Information Systems 14 (4) (Spring 1998) 149–166.

[70] M. Wolery, A.N. Gar<sup>fi</sup>nkle, Measures in intervention research with young children who have autism, Journal of Autism and Developmental Disorders 32 (5) (October 2002) 463–478

[71] D.R. White, J.A. Camacho-Guerrero, K.N. Truong, G.D. Abowd, M.J. Morrier, P.C. Vekaria, D. Gromala, Mobile capture and access for assessing language and social development in children with autism, Extended Abstracts of the 5th international conference on Ubiquitous Computing, 2003, Seattle, Washington, USA.

[72] W.F. Whyte, Participatory Action Research, Sage Publications, Newbury Park, CA, 1990.

[73] J. Woodward, H. Rieth, A historical review of technology research in special education, Review of Education Research 67 (4) (Winter 1997) 503–636.

[74] R.F. Zammuto, T.L. Grif<sup>fi</sup>th, A. Majchrzak, D.J. Dougherty, and S. Faraj, Information Technology and the Changing Fabric of Organization, Organization Science, forthcoming (2007).

![](/api/attachments/AUG82B5B/fulltext/images/e3d97550f11ac1082e182da8e50347e3fd651fc3b99b161dd0eab13023f7c1f0.jpg)  
Dawn G. Gregg is an Associate Professor of information systems at the University of Colorado, Denver and Health Sciences Center. She received her Ph.D. in Computer Information Systems and her M.S. in Information Management from Arizona State University her M.B.A. from Arizona State University West, and her B.S, in Mechanical Engineering from the University of California at Irvine. Her current research seeks to improve the quality and usability of Web based information. Her work has been published in journals including MIS Quarterly, International Journal of Electronic Commerce, IEEE Transactions on Systems Man and Cybernetics. Communications of the ACM, and Decision Support Systems. Dr. Gregg is a co-founder of Developing Minds Software.
