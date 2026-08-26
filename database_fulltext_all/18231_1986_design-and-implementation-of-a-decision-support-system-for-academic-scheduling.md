---
otero_id: 18231
otero_key: "FK7BP4ZM"
title: "Design and implementation of a decision support system for academic scheduling"
authors: "Suleiman K. Kassicieh; Donald K. Burleson; Rodrigo J. Lievano"
year: "1986"
journal: "Information & Management"
doi: "10.1016/0378-7206(86)90035-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Design and Implementation of a Decision Support System for Academic Scheduling

Suleiman K. Kassicieh, Donald K. Burleson and Rodrigo J. Lievano

R.O. Anderson Schools of Management, The University of New Mexico, Albuquerque, New Mexico 87131, USA

The task of scheduling, especially when it affects the performance of people, is a very complex endeavor. Satisfying a variety of needs and requirements while maintaining standards for efficiency and effectiveness is difficult due to political pressures exerted by those who are scheduled. The assignment of courses to professors, timeblocks, and classrooms impacts strategic planning issues such as the need for new buildings, expansion of course offerings and admission policies. This paper describes an interactive computer system made of three interrelated subsystems: the database which stores the course, professor, and classroom information; the modeling subsystem which includes all of the mathematical models used to produce the schedules, and the dialog subsystem which is designed to allow the user to change the database, execute the models to change assignments at any time, and input priorities or other subjective inputs to produce schedules. This paper also describes analysis, design, and implementation issues that arose during the creation of a Decision Support System (DSS) to aid administrators in course scheduling activities. The constraining effects of the political environment upon decision-making and DSSs are treated through the discussion of policies and their effect on DSS design. Examples from the Spring 1985 schedule of the Anderson Schools are used to expound on the issues.

Keywords: DSS, Scheduling, Implementation.

## 1. Introduction

Academic scheduling is the set of activities for assigning faculty to courses, courses to timeblocks,

![](/api/attachments/FK7BP4ZM/fulltext/images/8b6c4cb765b091e3553b72825f8788c6dedfe48955f68cec40677d4e8b35ba4a.jpg)

Suleiman K. Kassicieh is Director of the Management Systems Computer Center and Associate Professor of Management Information Systems and Management Science at the Anderson Schools of Management at the University of New Mexico. He holds a BS in Mathematics, and MBA in Finance and a Ph.D. in Operations Research. Dr. Kassicieh's teaching and research interests are in the areas of decision support systems, mathematical modeling and expert systems. Dr. Kassicieh has numerous articles in journals such as Operations Research, California Management Review, Journal of Operations Management, Large Scale Systems and Information Processing & Management.

![](/api/attachments/FK7BP4ZM/fulltext/images/a939504203d210c0c02fc2a2a956074b440e4ec89b7be74e06f33fb5f3f6dec3.jpg)  
Donald Burleson holds a BA in Experimental Psychology and an MBA in Information Systems from the University of New Mexico. He is currently the Database Architect for Shepard's/McGraw-Hill in Colorado, Springs, Colorado.

![](/api/attachments/FK7BP4ZM/fulltext/images/38003e1e7428ccda8bad2969ccf0371b7148ba7e0f6460b82701bf60dd6ec2ef.jpg)

Rodrigo J. Lievano is Associate Dean and Associate Professor of Management Science/Information Systems at the R.O. Anderson Graduate School of Management, University of New Mexico. Professor Lievano received his Ph.D. in Management Science-Statistics at the University of Houston in 1975. After serving as a National Science Foundation Research Associate and visiting professor of Finance at Houston, he joined the Anderson School faculty in 1976. He has authored various publications in energy models and information systems, and has served as an energy consultant to the states of Texas, New Mexico, and Mississippi. Other interests and publications concern robust estimation, time-series methods, and statistics in law.

and the faculty-course-timeblock combinations to classrooms. A course scheduling system serves several long-term objectives other than the obvious operational one of providing course, section, time, place, and instructor information to interested parties. These objectives are broader in scope and serve to provide the boundaries for performing the operational tasks leading to the course schedule. At the top level (e.g., the university administration), the objectives relate to effective and efficient resource utilization. Policies at this level are established on broad, resource-related issues, such as operating times, available facilities, and energy usage. At the next level (e.g., colleges, schools, departments), the objectives are varied and complex, seeking to balance often-conflicting administrative, faculty, and student perspectives. Policies are established to determine priorities regarding courses, times, and instructors to aid in reconciling the different perspectives. Finally, the process of scheduling is where these policies are implemented and supported by maintaining a relevant, timely, and accurate flow of data.

A variety of papers [1,3,6,12] have examined the use of mathematical modeling to perform the first step of a multiple allocation scheme, namely that of assigning faculty to courses. Panwalkar and Iskander [11], Baker [2], Godin [4], and Hill et al. [7] discussed one-stage one-criterion scheduling techniques that utilize optimization whereas Krajewski and Ritzman [9] and Uskup and Smith [15] covered single and multiple-stage disaggregation techniques in manufacturing and service industry scheduling. This paper describes the design and implementation of a decision support system (DSS) as defined by Keen and Morton [8] and Sprague and Carlson [14] to aid in the academic scheduling activities at the Anderson Schools of Management at the University of New Mexico. The Anderson Schools have 37 full time faculty and several part time faculty and several part time faculty with an offering of about 400 sections per academic year. Satisfying faculty and student demands for times, courses, and other characteristics such as a seminar room setup, audiovisual equipment, computer terminals and maps is difficult to perform by manual methods, because the changes weigh heavily on the decision makers' intuition and mental storage capabilities. The nature of the problem is one where altering the time in which one course is offered affects the classroom allocation and creates problems in the scheduling process due to the difficulty in assessing the sensitivity of changes.

This paper discusses the political issues of allocation as set by policies or the informal organization and how the success of the design and implementation of systems depends on adherence to these policies but at the same time providing the decision-maker with the flexibility and information to effect changes when these changes become necessary.

## 2. The Scheduling Environment

Meador, Guyote and Keen [10] indicated that a “political fit” between the DSS and the environment in which it will be used is an important factor in the success of the DSS. The scheduling environment is an important issue in the design and implementation of the scheduling system. The political system determines the methods by which assignments are made. The assignment of professors to courses and courses to times may be based on such criteria. The elusiveness and the subjectivity of the criteria are apparent as in multiple criteria desicion-making, except that in this situation the principle of “bounded rationality” prevents the exposition of all the relevant criteria. The main idea still remains that the DSS designer has to take the policies and procedures common to the department or college into consideration and would therefore have to design the system to accommodate these policies and procedures.

At the University of New Mexico, course scheduling is a decentralized activity. Individual academic units are free to allocate their resources as they see fit. The only externally-imposed constraints are official university time-periods, and the scheduling of classrooms outside of the academic unit's control. At the Anderson Schools of Management (ASM), the major objective that guides course scheduling is the maintenance of balance between the desires of students and professors. This goal is implemented by fixing the days and times for undergraduate and graduate core courses, and by allowing time flexibility in the scheduling of elective courses. In this manner, a large proportion of classes can be scheduled based on student needs and desires (these are periodically reviewed), while permitting professors to balance their schedule by selecting times for their elective courses. A secondary goal at the ASM is to develop and maintain the student's identification with the schools by scheduling as many courses as possible in the school's building. Since the number of classrooms is limited, priorities must be established. Priority is given to graduate courses, since the graduate programs are self-contained (all required courses are offered by the ASM), whereas over half of the undergraduate program courses are offered by other academic units. Currently, no other scheduling constraints are imposed but the system allow priorities for certain courses, groups of courses, individual professors or professorial ranks.

The Anderson Schools have seven semi-autonomous areas: Human Resources Management (HRM), Marketing (MKT), Finance (FIN), Operations Research/MIS (MIS), Economics, Environment, and Policy (EEP), International Management (INT) and Accounting (ACT).

Each area coordinator has the responsibility of submitting their faculty course and time preferences. At the onset of the scheduling process, which is usually about six months before the start of the semester being scheduled, area coordinators usually send their faculty a list of core and elective courses to be offered. Since the times for the MBA and BBA core courses have been set, whereas the times for the elective courses are open, the area coordinator will check for possible time conflicts of elective courses usually taken in the same semester by students. When faculty in any area prefer to teach the same core or elective course, the area coordinator usually asks the faculty members to discuss the issue and reach a consensus of how to allocate the courses between them using the pooled interdependent decision-making process described by Hackathorn and Keen [5]. Courses that require part-time or adjunct faculty are designated as “Staff” courses until the area coordinator decides who will be teaching them.

The final schedule for each area is submitted to the administration for scheduling the professor-course-timeblocks (P-C-Ts) to classrooms at the Anderson School which has ten classroom that are preferred by the faculty over classrooms outside the school.

In the six month period between the submission of the first trial schedule and the first day of classes, faculty often change their preference for courses and times. These changes, as well as the original assignment of P-C-Ts, used to take hundreds of hours to perform.

The scheduling environment described above have some common elements:

1. Some characteristics in both object and destination are intuitive and thus require subjective inputs.

2. The assessment of the sensitivity of changes is a time-constrained task and is difficult to perform without the aid of a computer.

3. Even with a modest number of objects and destinations, the search space for feasible solutions is very large.

4. The scheduling environment is a typical resource allocation environment that is sensitive to the informal political pressures.

Keen and Morton [15] describe decision support systems as interactive systems that allow the decisionmaker to model data retrieved from a database and to examine the sensitivity of the results in an unstructured or semi-structured environment. The decisionmaking environment is defined as unstructured by Simon [22] if the problems encountered therein have time constraints, a need for intuitive inputs, large search or uncertainty about some parameters. The need for decision support systems in the above scheduling environment is apparent.

A simple illustration will provide an example of the influence of political pressures on scheduling. Suppose that university professors prefer a Tuesday-Thursday (TR) schedule to all other schedules such as a Monday-Wednesday-Friday (MWF) or a MTWRF schedule. Since utilization of classrooms, students and probably the board of regents require that a number of course to be offered on MWF, administrators are faced with the problem of who is assigned to the TR courses. A fair method is alternating professors between a TR schedule one semester and a MWF the next. Political pressures through the use of the informal organization play a role however in using many other allocation schemes to always schedule some professors to TR courses whereas others get MWF schedules consistently. The DSSs used by the administrators should be able to take the realities of the environment into consideration and allow the user to define the allocation scheme that best suits their situation. The DSS should also allow the decisionmaker to alter schedules based on intuitive judgements that are subjective in nature.

## 3. The Database Subsystem

The database used by the system was designed to contain data about areas, professors, courses, acceptable university course time blocks, available classrooms, and their size. When the P-C-Ts are entered, the professor's name and area are validated by examining the database. Course numbers and course descriptions are related to the areas that offer these courses and to the semester in which the course is offered. Figure 1 shows the Fall MIS core courses and the spring elective accounting courses. Data on core courses contains the course number, description, and time offered. Elective course data has only the course number and description. The database has also the allowed time blocks. Classroom size data is necessary to check the assignment of P-C-Ts to classrooms of appropriate size: this helps guide the making of assignments. The classrooms at the Anderson schools are described as “large” with a capacity for 40 to 60 students, “medium” for 10 to 40 students or “small” for seminars with 10 or less students.

The database of P-C-Ts is built by prompting for a professor's name and courses one course at a time. The system then identifies the area and finds out whether the course is core or elective. If it is a core course, the predetermined time is assigned to the P-C-T. For electives, the system prompts for the time. As the P-C-Ts are entered, the user is informed whether a course has been assigned to another professor. The user then has the option of assigning the course to either of the professors, or tagging the course with a "STAFF" instructor until the conflict is resolved. This feature of the DSS allows the user to either decide to whom the course will be assigned, or, if a mechanism for conflict resolution exists in the political process, to postpone the decision and return with the resolution.

When completed, the database can be used to make the assignments creating a schedule to be used later when changes are made. The only difference between the database of P-C-Ts and the schedule is a new field in the database indicating the classroom to which the course was assigned

<table><tr><td>291-001</td><td>Business Stat Lab</td><td>M</td><td>10:00-10:50</td></tr><tr><td>291-002</td><td>Business Stat Lab</td><td>W</td><td>10:00-10:50</td></tr><tr><td>291-003</td><td>Business Stat Lab</td><td>F</td><td>10:00-10:50</td></tr><tr><td>291-004</td><td>Business Stat Lab</td><td>T</td><td>03:30-04:20</td></tr><tr><td>300-001</td><td>Oper Resch/Mgt Sci</td><td>T T</td><td>09:30-10:45</td></tr><tr><td>300-002</td><td>Oper Resch/Mgt Sci</td><td>M W F</td><td>10:00-10:50</td></tr><tr><td>300-003</td><td>Oper Resch/Mgt Sci</td><td>M W F</td><td>09:00-09:50</td></tr><tr><td>301-001</td><td>Comp Based Info Sys</td><td>T T</td><td>09:30-10:45</td></tr><tr><td>301-002</td><td>Comp Based Info Sys</td><td>T T</td><td>11:00-12:15</td></tr><tr><td>301-003</td><td>Comp Based Info Sys</td><td>M W F</td><td>10:00-10:50</td></tr><tr><td>500-001</td><td>Quant Anal I</td><td>T T</td><td>05:00-05:50</td></tr><tr><td>501-001</td><td>Stat Anal Mgt Decis</td><td>T T</td><td>05:00-06:15</td></tr><tr><td>520-001</td><td>Oper Resch &amp; Prod Mgt</td><td>T T</td><td>06:30-07:45</td></tr></table>

```csv
SPRING ELECTIVE ACCOUNTING COURSES
101-001 Fundamentals of Acct
101-002 Fundamentals of Acct
101-003 Fundamentals of Acct
343-001 Income Tax Acctg II
348-001 Legal Concepts-Accts
444-001 Acctg not for Profit
546-001 Sem in Controllershp
547-001 Sem in Adv Tax Acctg
```  
Fig. 1. Fall MIS Core Courses File and Spring ACT Elective Courses.

## 4. The Dialog Subsystem

The system is menu driven. After the proper logging and password procedures, the user is greeted with an explanation screen and then given the choices shown in Figure 2.

Option 1 allows the user to update the database files as shown in Figure 3. In option 2, the user enters P-C-Ts data. Option 3 modifies the priorities of courses and professors by sorting entries in rank order of priority. Option 4 schedules courses to classrooms whereas option 5 presents the user with the modification menu shown in Figure 4. Option 6 of the master menu produces the schedule in three different formats and option 7 of the master menu terminates the session.

## 5. The Modeling Subsystem

The P-C-T data is developed in two transformations. The first process pairs the professors to courses; the next pairs the professor-course entries to the times. The database may be entered over many terminal sessions and modifications may be performed at any time. The database (see Figure

```txt
The Anderson Schools Scheduling System
The following operations can be performed. Please indicate the number of your choice:
1. Update the database
2. Enter professor name, courses and times
3. Alter priorities of professors or courses
4. Schedule courses to classrooms
5. Modify the existing schedule
6. Print the current schedule
7. Exit this program and stop
```  
Fig. 2. The Scheduling DSS Main Menu.

5) is used to make the allocations of P-C-Ts to classrooms.

The Anderson school has 1 small, 5 medium, and 6 large classrooms. The individual courses are classified according to the size of classroom necessary for the course. This capacity characteristic is considered to be uniform across all sections of a course, so that the roomsize file need only contain the course number, and the classroom where the search should start. It should be noted that assignment arrays are sorted by size; thus, to assign a course requiring a medium-sized classroom, the system will begin the search using the medium-sized classrooms. If a classroom that would satisfy the required capacity of a particular P-C-T is not found, the course will be assigned to a larger classroom.

The user of the system has the option of changing the priorities of courses or professors. At the Anderson Schools, MBA classes are given priority for Anderson Schools classrooms, because the faculty felt that it is imperative to hold MBA courses there to foster the School's professional image. In other situations, other priorities could be implemented. The entries with the highest priorities are moved to the top of the database; thus since the allocation routine uses the database sequentially,

## The Anderson Schools Scheduling System

this guarantees that highest priority courses will be held in the Anderson School classrooms. Similarly high priority professors are given the same treatment at the request of the user.

The assignment of P-C-Ts to classroom is performed using the following procedure:

When the database is read, the system locates the course in the roomsize file and goes to the proper position in the scheduling array to search for a classroom. The system then scans through all classrooms of the size specified by the roomsize file. The search ends if the course has found a room or if there are no more classrooms of the proper size available. In the latter case, the system assigns the P-C-T to a larger classroom or, if none is available in the school, a classroom satisfying the size requirement in another building.

Cancelled courses are ignored in the allocation process, but the P-C-T appears in the preliminary run output and will be ignored for the schedule of classes published by the university. Courses with “arranged” meeting times are similarly handled, except that they appear in the final output and in the university schedule of classes as in figure 8.

## The Anderson Schools Scheduling System

The following changes to the schedule can be performed. Please indicate the number of your choice:

Fig. 3. The Scheduling DSS Database Modification Menu.  
```txt
1. Cancel a class  
2. Change the classroom allocated to a course  
3. Change the time that a course is offered  
4. Change the section number of a class  
5. Assign a different instructor to a class  
6. Change the name of a class  
7. Exit this program and return to the master menu
```  
Fig. 4. The Scheduling DSS Schedule Modification Menu.

<table><tr><td>BULLERS</td><td>537-001</td><td>Database Sys</td><td>M W</td><td>05:00-06:15</td></tr><tr><td>PETERS</td><td>501-001</td><td>Stat Anal Mgt Decsn</td><td>M W</td><td>05:00-06:15</td></tr><tr><td>REID</td><td>520-001</td><td>Oper Resch &amp; Prod Mgt</td><td>T T</td><td>02:00-03:15</td></tr><tr><td>REID</td><td>530-001</td><td>Gen Systems Analysis</td><td>T</td><td>03:30-06:15</td></tr><tr><td>LIEVANO</td><td>531-001</td><td>Multivariate Anal</td><td>W</td><td>03:30-06:15</td></tr><tr><td>KASSICIEH</td><td>535-001</td><td>Info Sys A &amp; D</td><td>T</td><td>05:00-07:45</td></tr><tr><td>YEAKEL</td><td>502-001</td><td>Acct-Mgt Info Sys I</td><td>T T</td><td>05:00-06:15</td></tr><tr><td>ELLIOTT</td><td>547-001</td><td>Sem in Adv Tax Acctg</td><td>T</td><td>03:30-06:15</td></tr><tr><td>PHILIPS</td><td>541-001</td><td>Adv Acctg Theory</td><td>M W</td><td>04:30-05:45</td></tr><tr><td>HEYMAN</td><td>543-001</td><td>Sem in Bus Tax Plan</td><td>T</td><td>03:30-06:15</td></tr><tr><td>ROGERS</td><td>580-001</td><td>Res for Mrktg Mgt</td><td>T T</td><td>02:00-03:15</td></tr><tr><td>ROBLES</td><td>584-001</td><td>Sales &amp; Procurement</td><td>M W</td><td>03:00-04:15</td></tr><tr><td>SHAMA</td><td>522-001</td><td>Marketing Management</td><td>T T</td><td>05:00-06:15</td></tr><tr><td>SHAMA</td><td>581-001</td><td>Strategic Mktg Plan</td><td>T T</td><td>03:30-04:45</td></tr><tr><td>FINSTON</td><td>566-001</td><td>Human Relations Lab</td><td>T</td><td>03:30-06:15</td></tr><tr><td>JEHENSON</td><td>507-001</td><td>Org Behavior II</td><td>T T</td><td>03:30-04:45</td></tr><tr><td>MANN</td><td>572-001</td><td>Fin Plan &amp; Cap Bdgts</td><td>M W</td><td>05:00-06:15</td></tr></table>

Fig. 5. Part of the Database of P-C-Ts.

At the end of the initial allocation, the user can invoke the modification routine through the master menu. This allows the user to make changes. When changing the classroom assigned to a particular P-C-T, the procedure validates the new classroom choice and then assigns it to the P-C-T. The system then scans the schedule and reassigns the displaced P-C-Ts according to their priorities. This might have a domino-effect on the whole schedule so that all the P-C-Ts are rescheduled because courses can be scheduled for 150 minutes, 75 or 50 minutes. The nice feature about this method is that the user can make substantial alterations of an existing schedule without much effort, since the system handles the “what-if” scenario analysis.

The system produces the final assignments in three forms. The first shown in Figure 6 is required by the central scheduling department at the University of New Mexico and is sorted by ascending course number order. The second is the classroom utilization chart (see Figure 7) that allows the user to scan for vacant classrooms during a specified time period. The third shown in Figure 8 presents the course assignments in each of the seven areas. This form is used by administrators to communicate the results of the scheduling process to area coordinators.

```txt
KASSICIEH 510-001 Intro to Info Proc M W 02:00-02:50 ROOM 100
SHAMA 522-001 Marketing Management T T 05:00-06:15 ROOM 112
PANTON 526-001 Financial Management T T 06:30-07:45 ROOM 100
SCHULTZ 492-001 Special Topics: MS CANCELLED
LIEVANO 531-001 Multivariate Anal W 03:30-06:15 ROOM 122
KASSICIEH 535-001 Info Sys A & D T 05:00-07:45 ROOM 287
BULLERS 537-001 Database Sys M W 05:00-06:15 ROOM 279
PHILIPS 541-001 Adv Acctg Theory M W 04:30-05:45 ROOM 100
YEAKEL 548-001 International Acctg ARRANGED
HEYMAN 543-001 Sem in Bus Tax Plan T 03:30-06:15 ROOM 122
```  
Fig. 6. PCTs with Room Assignments.

The area coordinators send the form to faculty to determine whether changes of P-C-Ts are warranted. Note the inclusion of “release time” entries that appear in this schedule but are omitted from all others output; this was added so that the area coordinators could see which professors have reduced teaching loads so as to engage in research or administrative duties. The summary of staff entries for each area shows all of the P-C-Ts for which an instructor has not yet been assigned. As the area coordinators find qualified instructors, the information is forwarded to the administrators who make these changes through the use of the modification sub-menu. The system is designed to allow the user to make changes whenever necessary. It is not uncommon for a schedule to be modified over a period of months before the final draft is complete.

## 6. Implementation and Results

Keen and Morton [5] discuss at length the importance of the political climate in system implementation. DSSs are no exception. They are, by definition, a support tool that help the user in solving semi-structured problems by inputing intuitive judgments and then manipulating data. Scheduling in a university setting is a semi-structured task with political connotations that require intuitive subjective information. For instance, conflict resolution of a variety of issues (such as who teaches a certain course, who teaches a 2 or 3-day schedule or who gets certain classrooms for their courses) is a very difficult process because there are many factors to consider. These are not always easily measured or quantified. Some of the references propose models for the assignment of fa

<table><tr><td colspan="6">Classroom 287</td></tr><tr><td></td><td>Monday</td><td>Tuesday</td><td>Wednesday</td><td>Thursday</td><td>Friday</td></tr><tr><td>1:45</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2:00</td><td></td><td>444-001</td><td></td><td>444-001</td><td></td></tr><tr><td>2:15</td><td></td><td>----</td><td></td><td>----</td><td></td></tr><tr><td>2:30</td><td></td><td>----</td><td></td><td>----</td><td></td></tr><tr><td>2:45</td><td></td><td>----</td><td></td><td>----</td><td></td></tr><tr><td>3:00</td><td>329-001</td><td>----</td><td>329-001</td><td>----</td><td></td></tr><tr><td>3:15</td><td>----</td><td>----</td><td>----</td><td>----</td><td></td></tr><tr><td>3:30</td><td>----</td><td></td><td>----</td><td>566-001</td><td></td></tr><tr><td>3:45</td><td>----</td><td></td><td>----</td><td>----</td><td></td></tr><tr><td>4:00</td><td>----</td><td></td><td>----</td><td>----</td><td></td></tr><tr><td>4:15</td><td>----</td><td></td><td>----</td><td>----</td><td></td></tr><tr><td>4:30</td><td></td><td></td><td></td><td>----</td><td></td></tr><tr><td>4:45</td><td></td><td></td><td></td><td>----</td><td></td></tr><tr><td>5:00</td><td></td><td>535-001</td><td></td><td>----</td><td></td></tr><tr><td>5:15</td><td></td><td>----</td><td></td><td>----</td><td></td></tr><tr><td>5:30</td><td></td><td>----</td><td></td><td>----</td><td></td></tr><tr><td>5:45</td><td></td><td>----</td><td></td><td>----</td><td></td></tr><tr><td>6:00</td><td></td><td>----</td><td></td><td>----</td><td></td></tr><tr><td>6:15</td><td></td><td>----</td><td></td><td>----</td><td></td></tr><tr><td>6:30</td><td>589-001</td><td>----</td><td></td><td></td><td></td></tr><tr><td>6:45</td><td>----</td><td>----</td><td></td><td></td><td></td></tr><tr><td>7:00</td><td>----</td><td>----</td><td></td><td></td><td></td></tr><tr><td>7:15</td><td>----</td><td>----</td><td></td><td></td><td></td></tr><tr><td>7:30</td><td>----</td><td>----</td><td></td><td></td><td></td></tr><tr><td>7:45</td><td>----</td><td>----</td><td></td><td></td><td></td></tr></table>

Fig. 7. Classroom Utilization Chart.

culty to courses using different criteria. It is difficult, however, to insure the objectivity of the data used in these models. We are not trying to render judgement on political systems in universities, but rather to point out the need to consider the political climate in the decision-making process and thus in the design of DSSs. The DSS presented here took into consideration the environment at the Anderson School. Similar systems in other institutions should reflect the environmental constraints that are placed on the allocation system by the people that use or are affected by their system.

Thus a DSS should allow the user flexibility to resolve issues by intuition and familiarity with their institution. If the user prefers to use other models in assigning faculty to courses then its addition is an easy task but this decision should be left to the administrators, since they usually have more information about their environment. In the Anderson School, the system of allowing the area coordinator to resolve conflicts before the

![](/api/attachments/FK7BP4ZM/fulltext/images/4c079a7ad2f1e2ed1ba3a0370f8a9fa949ec1768103005c696b28fb9ec7fbefd.jpg)  
Fig. 8. Area Faculty Summary.

P-C-Ts are submitted for scheduling has worked well. In other institutions the style of management might not work.

The motivation for the development of the DSS at the Anderson Schools was rather typical of applications development. The Schools have been experiencing rapid growth, and the manual system in use was inefficient and ineffective. Some of the deficiencies of the old system were:

1. Long lead times due to the slow preparation of initial schedule.

2. Lack of standardization in procedures and inputs.

3. High incidence of clerical errors.

4. Difficulty in making changes.

5. Difficulty in using databases for other purposes.

6. Involvement of high-level administrators in details

Clearly, those deficiencies are not all a result of the manual method used previously but are indicators that the system needed formalization. The DSS served that purpose by establishing the mechanics of schedule preparation, review and modification in a timely manner. The DSS was ideal for merging a set of demanding tasks, a large database, a set of policies into a system that allowed changes, evaluated options and satisfied the political environment.

The design of the system was guided by a set of objective established by the Schools' administrators and the faculty. The primary difficulty in establishing these objectives was related to the need to formalize the informal rules and procedure. This formalization requires specificity which puts it at odds with the political nature of the decisions. The objections were overcome by establishing rules via democratic process, building flexibility into the system and allowing the assignment of courses to instructors to be outside the boundaries of the DSS.

The scheduling DSS has been used at the Anderson Schools for the last three semesters. Due to the adaptive nature of DSSs, it has undergone some changes. We have described the latest version of the DSS. The benefits that have resulted are:

1. Reduction in time spent in producing the initial schedule and in making changes.

2. Increased effectiveness due to increased communication between the user and faculty and due to the elimination of errors.

3. Continuity from one scheduling period to another in terms of data and schedules.

4. Decrease in time spent on conflict resolution due to the quick evaluation of possible alternatives.

## References

[1] Andrew, G.M. and Collins R., “Matching Faculty to Courses,” College and University, Vol. 46, No. 2 (Winter 1971), pp. 83–89.

[2] Baker, K.R., "Workforce Allocation in Cyclical Scheduling Problems: A Survey," Operational Research Quarterly, Vol. 27, No. 1 (January 1976), pp. 155-167.

[3] Dyer, J.S. and Mulvey, J.H., "An Integrated Optimization/Information System for Academic Planning," Management Science, Vol. 22, No. 12 (August 1976), pp. 1332-1341.

[4] Godin, V.B., “Interactive Scheduling: Historical Survey and State of the Art,” AIIE Transactions, Vol. 10, No. 3 (September 1978), pp. 331–337.

[5] Hackathorn, R. and Keen, P., “Organizational Strategies for Personal Computing in Decision Support Systems,” MIS Quarterly, Vol. 5, No. 3 (September 1981), pp. 21–27.

[6] Harwood, G.B. and Lawless, R.W., "Optimizing Organizational Goals in Assigning Faculty Teaching Schedules," Decision Sciences, Vol. 6, No. 3 (July 1975), pp. 513–524.

[7] Hill, A.V.; Naumann, J.D. and Chervany, N.L., “SCAT and SPAT: Large-Scale Computer-Based Optimization Systems for the Personnel Assignment Problem,” Decision Sciences, Voll. 14, No. 2 (April 1983), pp. 207–220.

[8] Keen, P.G.W. and Morton, M.S.S. Decision Support Systems: An Organizational Perspective. Reading, MA: Addison-Wesley, 1978.

[9] Krajewski, L.J. and Ritzman, L.P., “Disaggregation in Manufacturing and Service Organizations: Survey of Problems and Research,” Decision Sciences, Vol. 8, No. 1 (January 1977), pp. 1–18.

[10] Meador, C.L.; Guyote, M.J. and Keen, P.G.W., “Setting Priorities for DSS Development,” MIS Quarterly, Vol. 8, No. 2 (June 1984), pp. 117–129.

[11] Panwalkar, S.S. and Iskander, W., "A survey of Scheduling Rules," Operations Research, Vol. 25, No. 1 (January-February 1977), pp. 45–61.

[12] Shih, W. and Sullivan, J.A., "Dynamic Course Scheduling for College Faculty Via Zero-One Programming," Decision sciences, Vol. 8, No. 4 (October 1977), pp. 711-721.

[13] Simon, H.A. The New Science of Management Decisions. N.Y., N.Y.: Harper&Row, 1960.

[14] Sprague, R.H. Jr. and Carlson, E.D. Building Effective Decision Support Systems. Englewood Cliffs, N.J.: Prentice Hall, 1982.

[15] Uskup, E. and Smith, S.B., "A Branch-and-Bound Algorithm for Two-Stage Production-Sequencing Problems," Operations Research, Vol. 22, No. 1 (January-February 1975), pp. 118–136.
