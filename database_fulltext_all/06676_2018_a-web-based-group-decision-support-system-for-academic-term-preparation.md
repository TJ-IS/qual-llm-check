---
otero_id: 6676
otero_key: "FMFXSCZC"
title: "A web-based group decision support system for academic term preparation"
authors: "Atiq W. Siddiqui; Syed Arshad Raza; Zeeshan Muhammad Tariq"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.08.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

A web-based group decision support system for academic term preparation

Atiq W. Siddiqui, Syed Arshad Raza, Zeeshan Muhammad Tariq

![](/api/attachments/FMFXSCZC/fulltext/images/8c1240d0faa5b347e8b95cc6a619d040c1d8c57f3e8b716dd076013fbcf9a57f.jpg)

<table><tr><td>PII:</td><td>S0167-9236(18)30126-X</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2018.08.005</td></tr><tr><td>Reference:</td><td>DECSUP 12979</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>30 October 2017</td></tr><tr><td>Revised date:</td><td>4 August 2018</td></tr><tr><td>Accepted date:</td><td>5 August 2018</td></tr></table>

Please cite this article as: Atiq W. Siddiqui, Syed Arshad Raza, Zeeshan Muhammad Tariq , A web-based group decision support system for academic term preparation. Decsup (2018), doi:10.1016/j.dss.2018.08.005

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# A Web-Based Group Decision Support System for Academic Term Preparation

Atiq W. Siddiqui<sup>1</sup> College of Business Administration, Imam Abdulrahman bin Faisal University, Saudi Arabia awsiddiqui@iau.edu.sa

Syed Arshad Raza College of Business Administration, Imam Abdulrahman bin Faisal University, Saudi Arabia saraza@iau.edu.sa

Zeeshan Muhammad Tariq College of Business Administration, Imam Abdulrahman bin Faisal University, Saudi Arabia zeeshanmt@iau.edu.sa

2<sup>nd</sup> Revision Submitted to: Decision Support Systems August 2018

# A Web-Based Group Decision Support System for Academic Term Preparation

In this paper, we present a web-based group decision support system for the Academic Term Preparation problem faced at a business school of a large Middle Eastern university. This multi-stage problem involves several stakeholders that need to coordinate for the course offerings, instructor assignments, and the preparation of the relevant timetables. This coordination is facilitated through a web application that implements all stages of the workflow. It further automates the timetabling task through an optimization module using a new multi-objective mixed integer programming model. The model is based on curriculum and student sectioning requirements; academic and administrative policies; and, the present capacity situation. The new system replaces a semi-automated spread sheet tool, resulting in improved quality of timetables, efficient workflow coordination, customized reporting, significantly reduced lead times, and eradication of human errors.

Keywords: University Timetabling, Student Sectioning, Web-based Group Decision Support System, Group Decision Making, Multi-Objective Optimization, Education Planning

## 1. Introduction

Managing university teaching terms e.g., semesters, is a challenging problem that involves administrative functions related to resource and financial management. It helps resolve problems of course offerings, timetabling, student and course registration. While these tasks are facilitated through computer-based information systems to maintain required performance, the overall process undergoes a pre-term preparation and an in-term operational management phases.

This research focuses on the preparation of course offering and timetabling tasks, which starts with the determination of courses to offer, classrooms and instructors. It also requires policy formulation on teaching times, instructor assignments and rooms assignments. Course offerings are then prepared, considering teaching staff expertise, curriculum requirements or alternatively the student choices [1]. This is followed by the preparation of timetables, where offered courses are assigned to different instructors, time slots and classrooms. Timetables are primarily driven by the objectives of different stakeholders i.e., university management, instructors and students including better resource utilization, meeting teaching time preferences, and timetable co ess [2, 3]. This is also governed by common constraints including timetable completeness, non-contradictoriness, lecture sequencing, timetable uniformity, instructor and classroom availability, and classroom size/type appropriateness [2-6]. Several unique constraints also frequently occur due to institutional or academic policies, program requirements, and/or even local or cultural settings. Irrespective of the objectives or constraints, the resulting timetabling task is a highly combinatorial NP-hard optimization problem [2, 7]. Consequently, manual solutions are inefficient or yet impossible for even fairly small-sized problems, needing computationally efficient solution approaches.

Conceivably, the abovementioned course offering and timetabling preparation phase, henceforth referred to as Academic Term Preparation or ATP tasks, is a multi-stage coordinated process comprising tasks and decisions taken by the related stakeholders. While ATP involves stakeholder coordination and solving a highly combinatorial timetabling problem, the academic literature primarily focuses on the latter [7]. To our knowledge, none of the previously reported works is a decision support system which implements end-to-end solution to all aspects of ATP. This is generally attributed to a lack of organizational commitment, motivation, incentives and multidisciplinary expertise; negative perception about system’s ease of use; resistance to change; adoption of new systems; and, additional training needs [6, 8-10].

In this paper, we present a web-based group decision support system (GDSS): ATP Scheduler or ATPS, developed in-house at a business college of a major Middle Eastern university to support its complete ATP phase. The college started seven years back and offers three degree programs with unique timetabling and curriculum requirements (details in section 3). The college initially managed the ATP tasks manually, but due to rapid growth in enrollment the practice proved inefficient leading to problems pertaining to coordination and timetable generation. Eventually, ATPS was developed inhouse that helps in coordinating course offering decisions and preparing timetables using a multiobjective mixed integer programming timetabling model (MMILP). It is worth noting that timetabling problems in the literature are classified as Curriculum-based Course Timetabling (CCT), underpinned by curriculum requirements; and, Post-Enrollment based Cou tabling (PECT), involving a set of events such as trainings to be scheduled based on stu choices. A variant of PECT – the student sectioning (SS) problem is also reported that further considers splitting courses into sections [1]. While the proposed MMILP is primarily based on CCT i.e., students taking courses as per curriculum requirements, it is different in two ways as compared to the extant literature. Firstly, all the required courses are offered in multiple sections and several feasible combinations of course sections are generated for students to choose from. Hence the model can be viewed as a combination of CCT and SS i.e., CCTSS. Secondly, it incorporates several unique constraints including separate management of male and female course sections, and the consideration of custom requirements of individuals and groups of students and instructors (details in section 3).

The instant benefits resulting from ATPS include reduction in lead times in course offering due to face-to-face meetings replaced by asynchronous web-based coordination. The timetabling MMILP model generated solutions leading to higher instructor and student satisfaction; reduced solution times from weeks to minutes; eliminated recurrent human errors; and obtained feasible solutions that were impossible to get with the manual process.

The rest of the paper is organized as follows: section 2 presents the literature review; section 3 gives the problem description, whereas the proposed system details are presented in section 4. A numerical analysis on the performance of the MMILP is presented in section 5, whereas the mathematical model is presented in Appendix (section 7). Finally, the conclusions are presented in section 6.

## 2. Literature Review

The inception of computer-supported timetabling dates back to 1960’s followed by a magnitude of works [2, 11]. The reader is referred to [7, 12-14] for a detailed overview of these early developments. In this section, we focus on the two strands of university timetabling problem identified earlier as CCT and PECT, discussing problem nature and solution approaches. Moreover, we also provide a DSS perspective on these studies (section 2.3), identifying research gaps, and the need and merits of our research.

## 2.1. Studies based on CCT:

The early solution approaches to CCT problems applied rule based timetabling [15], simple integer programming (IP) and network flow models covering only course to room and course to room and instructor assignments respectively [16, 17]. An IP based DSS (SAPHIR) was presented by Ferland and Fleurent [18] aiming at concurrent assignment of classes-to-timeslot and groups of students to multiple sections. For a similar problem, Burke, et al. [19] applied genetic algorithm (GA) to solve the IP model. Later, Burke, et al. [4] reported solutions to the same problem using tabu search (TS), simulated annealing (SA), constraint logic programming, GAs and memetic algorithms. Considering teaching preferences, Stallaert [20] modeled the same problem as a quadratic assignment problem. Another DSS (SlotManager) was developed by Foulds and Johnson [21], which used a rule based approach. Other IP-based models to early CCT variants included Dimopoulou and Miliotis [22], Dimopoulou and Miliotis [23] and Daskalaki, et al. [3]. Daskalaki and Birbas [24] applied two-stage relaxation procedure on [4] by considering faculty and student days/time preferences.

More recently, Sarin, et al. [25] presented a benders decomposition solution to an IP model where constraints include meeting course requirements, faculty time preferences, completeness and non-

# ACCEPTED MANUSCRIPT

contradictoriness. Another system (eClasSkedular) was implemented by Miranda [26] that considered a unique scenario of varying courses length and commencement dates; time windows for course start dates. The benefits included efficient classroom usage with a reduction in the rental costs of off-site classrooms. Following this, a web-based DSS called udpSkeduler was reported by Miranda, et al. [6], who proposed an IP model to the problem. In another study, Abdullah and Turabieh [27] implemented a memetic based procedure considering room capacity, stability and lecture spread. Later, Cacchiani, et al. [28] presented a column generation based solution to IP model of a standard CCT problem. Recently, Domenech and Lusa [29] considered maximizing teachers’ preferences alongside their load balancing using a multi-objective MILP formulation. Vermuyten, et al. [30] considered optimization of student walking flows across rooms while maintaining compactness in student schedules. Akkan and Gülcü [31] presented a hybrid multi-objective GA for CCT robustness problem due to last minute changes in the timetables.

## 2.2. Studies based on PECT:

The solutions to PECT is primarily dominated by multi-stage meta heuristics. Carter [32] used a decomposition based greedy heuristic to assign times to sections, and a Lagrangian relaxation algorithm to assign classrooms. A GA implementation was reported by Jat and Yang [33], which was later modified as a hybrid TS and GA using a local search (LS) strategy [34]. In 2012, several PECT studies were reported including van den Broek and Hurkens [35] using an IP-based heuristic; a constraint programming and LS approach by Cambazard, et al. [36]; a SA method by Ceschia, et al. [37]; an adapted SA method by Lewis [38]; and an ant colony optimization by Nothegger, et al. [39]. A novel hybrid artificial bee colony algorithm was implemented by Bolaji, et al. [40] in which initial feasible solutions are first generated using the combination of saturation degree and backtracking algorithm. Later, a hill climbing optimizer is embedded within the employed bee operator to enhance the local exploitation ability of the original algorithm. Another hybrid GA and LS algorithm used events i.e. lectures, tutorials and seminars for student grouping was reported by Badoni, et al. [41]. More recently, an iterated local search algorithm hybridized with a hyper-heuristic was implemented by Soria-Alcaraz, et al. [42]. Re-usability, modularity and flexibility are some of the key features of the proposed approach. A timetabling problem arising from a real-world application in a private university in Buenos Aires, Argentina was resolved by Méndez-Díaz, et al. [43] through an integer linear programming based heuristic, which showed promising results.

## 2.3. DSS Perspective:

DSS are composed of three interrelated basic modules viz. database (input module), model base (optimization model(s)) and a user interface which comprises dialogue management, and reporting modules [44]. In this section, we first analyze those systems from the above literature which were implemented as DSS. A summary of all studies is then presented in Table 1 from a DSS perspective besides mentioning problem type and modeling approach. Considering the trends identified in DSS evolution [45], the nature of user access (i.e., standalone/LAN/internet/web) is also identified. Finally, we positioned our work and highlighted its distinct contributions in this context.

Kassicieh, et al. [15] was amongst the pioneering works on DSS where their system was reported having a database containing data on program areas, professors, courses, timeslots, available classrooms and their size; a modeling subsystem; and dialog subsystem with a menu-driven interface. A system was later reported by Dinkel, et al. [17] having problem generator, network optimizer and report writer components. It first generated an MPS-formatted problem file compatible to IBM 1979 using data extracted from various files. The MPS file was passed to the network optimizer, while its output sent to report writer which produced faculty timetables and summary reports on room and time utilization.

A DSS named SAPHIR was developed by Ferland and Fleurent [18] with a pop-up menu-based interface that provided access to data handling, automatic optimization, interactive optimization, report generation and parameter setting functions. The interactive tool enabled modification of solutions and parameters alongside report generation. SlotManager – a user-friendly menu-driven DSS was developed by Foulds and Johnson [21]. The system was implemented in MS Access. The system featured menu driven user-interface, a modeling base and a database. The system could generate a wide variety of reports on timetables. Another MS Access based DSS was reported by Dimopoulou and Miliotis [22], which was composed of database, a control system module (user interface), an optimization module using Xpress-MP solver, a report generator and an evaluation module to examine the quality of the timetables produced. Another menu driven MS Access and internet based DSS was developed by Dimopoulou and Miliotis [23] that allowed remote user access from multiple departments to a centralized database. The timetables were produced by each department separately, which were then forwarded to appropriate nodes of the network for viewing.

More recently, Miranda, et al. [6] developed udpSkeduler – a pioneering web architecture-based DSS for course timetabling. It comprises five modules: user interface module for managing system's parameters and information; data input module for storing data in a relational database; time availability module with a web access to instructors to enter their personal time availabilities; IP based optimization module that uses CPLEX as a solver; and the report module, which produces a series of management reports. This system is the first implementation of a web architecture based DSS reported in the literature, which also provides a basis to our DSS.

While we discuss the DSS proposed in the literature, we also summarize the progression of research in course timetabling in Table 1 from a DSS perspective besides identifying problem type and the modeling approaches. It is worth noting that there has been very limited progress (except some early works) in the development of software functionality related to accessibility, interface and over all supported solvers with standalone access. Notably, there are only two studies that provide multi-user access via internet, with only one providing web interface. This identifies a big void despite the opportunities provided by DSS for single as well as group decision making [45, 46].

Based on the above analysis and the current and emerging trends in DSS [45], we contribute in this direction by presenting a web-based GDSS that not only focuses on managing the timetabling process, but also supports end-to-end coordination and interaction between all the stakeholders. As discussed in section 1, we also report the development of a new MMILP model that combines the features of standard CCT and SS problems, which can be referred to as Curriculum-based Course Timetabling with Student Sectioning or CCTSS problem.

## ACCEPTED MANUSCRIPT

<table><tr><td rowspan="2">Research Article</td><td rowspan="2">Year</td><td rowspan="2">Problem</td><td rowspan="2">Modeling Approach</td><td rowspan="2">Data Source</td><td colspan="2">Interface</td><td>Access</td></tr><tr><td>Interactive Tool</td><td>Reporting Capability</td><td>Standalone/LAN/Internet/Web</td></tr><tr><td>Kassicieh, et al. [15]</td><td>1986</td><td>CCT</td><td>Rule based</td><td>File</td><td>✓</td><td>✓</td><td>Standalone</td></tr><tr><td>Glassey and Mizrach [16]</td><td>1986</td><td>CCT</td><td>Integer programming</td><td>File</td><td>✓</td><td>✓</td><td>Standalone</td></tr><tr><td>Chahal and De Werra [47]</td><td>1989</td><td>CCT</td><td>Network flow</td><td></td><td>✓</td><td>✓</td><td>Standalone</td></tr><tr><td>Dinkel, et al. [17]</td><td>1989</td><td>CCT</td><td>Capacitated network flow</td><td>File</td><td>✓</td><td>✓</td><td>Standalone</td></tr><tr><td>Ferland and Fleurent [18]</td><td>1994</td><td>CCT</td><td>heuristic algorithm</td><td>File</td><td>✓</td><td>✓</td><td>Standalone</td></tr><tr><td>Burke, et al. [19]</td><td>1994</td><td>CCT</td><td>Genetic algorithm</td><td>Spreadsheet</td><td>✓</td><td>✓</td><td>Standalone</td></tr><tr><td>Burke, et al. [4]</td><td>1997</td><td>CCT</td><td>Genetic algorithm</td><td></td><td>✓</td><td>✓</td><td>Standalone</td></tr><tr><td>Stallaert [20]</td><td>1997</td><td>CCT</td><td>Gen. quadratic assign. problem</td><td>File</td><td>✓</td><td>✓</td><td>Standalone</td></tr><tr><td>Foulds and Johnson [21]</td><td>2000</td><td>CCT</td><td>Rule based</td><td>DBMS $^{1}$ </td><td>✓</td><td>✓</td><td>LAN</td></tr><tr><td>Carter [32]</td><td>2000</td><td>PECT</td><td>Decomposition/greedy heuristic</td><td></td><td></td><td></td><td>LAN</td></tr><tr><td>Dimopoulou and Miliotis [22]</td><td>2001</td><td>CCT</td><td>Integer programming</td><td>DBMS</td><td>✓</td><td>✓</td><td>Standalone</td></tr><tr><td>Dimopoulou and Miliotis [23]</td><td>2004</td><td>CCT</td><td>Integer programming</td><td>DBMS</td><td>✓</td><td>✓</td><td>Internet</td></tr><tr><td>Daskalaki, et al. [3]</td><td>2004</td><td>CCT</td><td>Integer programming</td><td></td><td></td><td></td><td></td></tr><tr><td>Daskalaki and Birbas [24]</td><td>2005</td><td>CCT</td><td>Integer programming</td><td></td><td></td><td></td><td></td></tr><tr><td>Jat and Yang [33]</td><td>2009</td><td>PECT</td><td>Genetic algorithm</td><td></td><td></td><td></td><td></td></tr><tr><td>Sarin, et al. [25]</td><td>2010</td><td>CCT</td><td>Integer programming</td><td></td><td></td><td></td><td></td></tr><tr><td>Miranda [26]</td><td>2010</td><td>CCT</td><td>Integer programming</td><td>DBMS</td><td>✓</td><td>✓</td><td>Standalone</td></tr><tr><td>Jat and Yang [34]</td><td>2011</td><td>PECT</td><td>Hybrid genetic algorithm and tabu search</td><td></td><td></td><td></td><td></td></tr><tr><td>van den Broek and Hurkens [35]</td><td>2012</td><td>PECT</td><td>LP/Column generation-based heuristic</td><td></td><td></td><td></td><td></td></tr><tr><td>Ceschia, et al. [37]</td><td>2012</td><td>PECT</td><td>Simulated annealing</td><td></td><td></td><td></td><td></td></tr><tr><td>Miranda, et al. [6]</td><td>2012</td><td>CCT</td><td>Integer programming</td><td>DBMS</td><td>✓</td><td>✓</td><td>Web</td></tr><tr><td>Abdullah and Turabieh [27]</td><td>2012</td><td>CCT</td><td>Tabu-based memetic approach</td><td></td><td></td><td></td><td></td></tr><tr><td>Lewis [38]</td><td>2012</td><td>PECT</td><td>Simulated annealing</td><td></td><td></td><td></td><td></td></tr><tr><td>Cambazard, et al. [36]</td><td>2012</td><td>PECT</td><td>Local search and constraint programming</td><td></td><td></td><td></td><td></td></tr><tr><td>Nothegger, et al. [39]</td><td>2012</td><td>PECT</td><td>Any colony optimization</td><td></td><td></td><td></td><td></td></tr><tr><td>Cacchiani, et al. [28]</td><td>2013</td><td>CCT</td><td>Integer programming/Column generation</td><td></td><td></td><td></td><td></td></tr><tr><td>Bolaji, et al. [40]</td><td>2014</td><td>PECT</td><td>Hybrid artificial bee colony</td><td></td><td></td><td></td><td></td></tr><tr><td>Badoni, et al. [41]</td><td>2015</td><td>PECT</td><td>Genetic algorithm with local search</td><td></td><td></td><td></td><td></td></tr><tr><td>Domenech and Lusa [29]</td><td>2016</td><td>CCT</td><td>Mixed integer linear programming</td><td></td><td></td><td></td><td></td></tr><tr><td>Méndez-Díaz, et al. [43]</td><td>2016</td><td>PECT</td><td>Integer linear programming</td><td></td><td></td><td></td><td></td></tr><tr><td>Vermuyten, et al. [30]</td><td>2016</td><td>CCT</td><td>two-stage integer programming</td><td></td><td></td><td></td><td></td></tr><tr><td>Soria-Alcaraz, et al. [42]</td><td>2016</td><td>PECT</td><td>Iterated local search</td><td></td><td></td><td></td><td></td></tr><tr><td>Akkan and Gülcü [31]</td><td>2018</td><td>CCT</td><td>hybrid multi-objective genetic algorithm</td><td></td><td></td><td></td><td></td></tr></table>

Table 1: Timetabling Research from DSS Perspective

# ACCEPTED MANUSCRIPT

## 3. Problem Description

The ATPS was developed for a new business college in a large Middle Eastern university. The college was established seven years ago, where it started to offer three separate bachelor degree programs in Accounting, Finance & Economics and Management Information Systems (MIS). Each program consists of 122 credit hours to be taken in eight full semesters or four years. During these four years, the students take 39 courses of 3 credit hours each during the first seven semesters, while the last semester is reserved for industry training. Of these, 12 are major related courses taken within the three specializations. The remaining courses are common to all students. Each program is housed in a separate department with its own set of instructors. While offering program specific courses, these departments also offer college-level courses. The course offerings during a semester are driven by the program curriculum requirements. Three other support departments of Management & Marketing, Business Law and Quantitative Methods were also established that offer general college-level courses. Current enrollment in the college is over 1300 students easing trend. All courses offered to students in any of these programs are distributed in eral course-sections to facilitate the large enrollment, whereas each section is generally rest 25-35 students. Furthermore, additional courses are also offered to repeating students. All of these courses normally require two 90 minutes lectures sessions during a week on separate days. policy, lectures for all the above courses are delivered in the same room and at the same time on a prescribed days combination as set by the college (Table 2). For example, a course section may have classes on ST or Sundays and Tuesdays between 8:00AM and 9:30AM, while another section of the same course may be scheduled on MTh between 12:30PM-2:00PM. In terms of sessions on a given day, considering 90 minutes class lengths, lecture start times are always 8:00AM, 9:30AM, 11:00AM, 12:30PM and 2:00PM.

As the actual number of course offerings differ each semester due to changing enrollment and the available number and expertise of instructors, the number of courses typically offered are around 45 with over 220 course-sections. These are taught by over 50 instructors (full and part time from industry). A course may be taught by a single or multiple instructor(s) depending upon the available expertise and the number of sections offered. It is worth noting that the enrollment during last few years is steadily on the rise and the number of offerings is expected to increase during upcoming years. This growth trend is further substantiated by the fact that the college is planning to open new programs during the upcoming years.

<table><tr><td>Type</td><td>Lecture Days</td><td>Lecture Length</td></tr><tr><td>1 or ST</td><td>Sundays/Tuesdays</td><td>90 Minutes each</td></tr><tr><td>2 or MW</td><td>Mondays/Wednesdays</td><td>90 Minutes each</td></tr><tr><td>3 or MTh</td><td>Mondays/Thursdays</td><td>90 Minutes each</td></tr></table>

Table 2: Period Types or Days in Which Classes are schedules

Another important consideration to this is that few of the courses in the curriculum (all programs) have additional labs or tutorials that are taken by the same instructors teaching the course. For example, Database management in MIS and Computer Application in Finance in Finance & Economics have labs in their course requirements. These labs or tutorials are also to be scheduled appropriately during the week comprising a single session of 90 minutes; where labs are given at a specialized location and tutorials in regular classrooms. In ter of infrastructure, the college currently has two separate nearby buildings in which 30 cla rooms in one building and 11 in the other) and 4 labs are currently available that are departments. Not all classrooms are of equal capacity, and hence this becomes a major consideration during the scheduling of classes.

There are also two cultural and policy factors unique to our program that play important role in both the course offerings and the timetabling tasks. First, both male and female students use different buildings for taking lectures. These lectures are to be planned separately for male and female students, however, taught by the same instructors. Due to much larger female enrollment, the larger building is reserved for female students. There are also access restrictions on instructors that are assigned to certain classrooms. Second, policy factor is based on the issues mentioned earlier mentioned for multi-sectioned courses that are taught by multiple instructors. While student must follow a course plan, college allows students a choice in selecting the sections of a course that they need to take. By policy, college aims to schedule course sections of all the courses in a way that several feasible combinations of the required course sections are available to students to choose from. Hence, the college assumes that students of a particular program in a specific year are divided into cohorts. For each of these cohorts, one section each must be available of all the needed courses. Students can thus opt to join a cohort of their preference and consequently pick a complete combination of courses with one section each available. The cohort size is determined based on several factors that include nature of courses, typical classroom sizes available and the enrollment in a program. One thing that complicates this approach is when, due to limited number of sections in a certain course, sections are to be shared across the cohorts and thus time conflicts and classroom size situation becomes quite challenging.

To manage the above scenario, the college management employs a process where they first set the period and start time polices (i.e., period days as in Table 2 and period start times). The management also evaluates room capacity situation and the enrollment by year and degree programs and make available any additional classrooms as needed. The college then requests all academic departments to evaluate the course requirements based on the enrollment numbers provided and consult with its instructors for teaching choices. Departments make part timers available as needed in their course offerings. Departments then present a proposal to the college which includes courses to offer, number of sections for each course offered, and the names of instructors teaching these courses. The college then evaluates the proposal in coordination with the departments to finalize and approve the course offerings.

Once all the proposals are approved, a dedicated timetabling unit comprising two people within the college prepares the corresponding timetables, which after approval by the college management are offered to students for registration. The timetables are generated as a single master schedule in an Excel spreadsheet manually, carrying course sections and instructor names in appropriate time and classroom slots. The same Excel file contains several additional sheets which can extract specific timetables for instructors or cohorts from the master schedule sheet. While timetabling unit takes into consideration the standard requirements such as course sections assigned to a single classroom in prescribed period types (Table 2) and time slots, they also ensure that that sections in a cohort are without any time conflicts. Moreover, it is ensured that no more than 2 classes (or 3 hours) can be assigned in a row to any instructor or to a cohort to avoid overloading. It also includes keeping free slots by college, department or male/female wise to facilitate non-academic activities. Moreover, specific instructors’ requests such as from part timers or professors to avoid or keep particular days or times are also met. While some of these are optional and are enforced depending upon attaining feasible solution, others are considered essential (mainly related to part timers with specific days/times requirements due to external commitments) – as decided by the college management.

In terms of objectives, there are two key considerations. First, for instructors on any given day, the time difference between the time teaching start and end times are minimized, while the same approach is considered for cohorts, whereas on a day the difference in the class start and end times are tried to be minimized. This was done manually with casual visual evaluation only till the enrollment increased to large numbers and the utilization of the Excel tool became impractical due to exponentially increasing problem complexity and the corresponding lead times. Moreover, human errors were also frequent. The college initially searched for an off-the-shelf product, however, due to its unique requirements, it eventually decided to develop a complete decision support system inhouse to support the entire workflow of the ATP process. Consequently, ATPS was developed, which is now being fully integrated by the college to manage its ATP.

## 4. System Description

This section initially describes the nature, scope and ATPS process workflow in terms multiple stakeholder involvement for course scheduling, followed by the details related to ATPS system architecture and implementation.

## 4.1. Nature and scope

ATPS is essentially a web-based multi-stage asynchronous group decision support system (GDSS) for generating optimal course schedules. ATPS provides access to multiple stakeholders which play dedicated roles at various stages of the ATP workflow. This arguably results in major communication, coordination and information access challenges, and our choice of a web-based GDSS approach to the ATP problem is due to its efficacy in such scenarios [48-50]. ATPS thus functions both as a communication and a model driven system [51]. The stakeholders comprise college management, timetabling unit, academic departments, instructors and students, each having different roles and levels of engagement in the process, as shown in Table 3, whereas their corresponding reports are also listed.

<table><tr><td>User</td><td>Web App.Access</td><td>Timetablingengine Access</td><td>Access Level</td><td>Reports</td></tr><tr><td>Student</td><td>Yes</td><td>No</td><td>Restricted</td><td>Cohort Timetables</td></tr><tr><td rowspan="2">Instructor</td><td rowspan="2">Yes</td><td rowspan="2">No</td><td rowspan="2">Restricted</td><td>Term-wise teachingtimetable</td></tr><tr><td>History of course taught</td></tr><tr><td>Department</td><td>Yes</td><td>No</td><td>Moderate (Input Departmental course offerings)</td><td>Instructors /Dept. level timetables</td></tr><tr><td>College Management</td><td>Yes</td><td>No</td><td>High (Course offering approvals and Adjustments)</td><td>All above reports</td></tr><tr><td>Timetabling Unit</td><td>Yes</td><td>Yes</td><td>Full</td><td>All above reports</td></tr></table>

Table 3: User Access Levels, Roles and Reports

## 4.2. ATPS Process Workflow

It is clear from the above discussion that the effectiveness of the ATPS depends entirely upon the mapping of ATP process tasks to the stakeholder roles, access levels, and their involvement over time. Consequently, an ATP work flow was outlined in consultation and coordination with the key stakeholders to ensure its validity. Figure 1 shows the complete ATP workflow, which served as the basis of ATPS design and development.

![](/api/attachments/FMFXSCZC/fulltext/images/4cd80b5216681a42634ba2a5692adf334f625f251fd279bbbc3da2a3d429438e.jpg)  
Figure 1: ATP Process Workflow

# ACCEPTED MANUSCRIPT

As depicted in Figure 1, the ATP process is initiated by the college management, which first defines the required polices and determines (in conjunction with the timetabling unit) the number of cohorts needed; requests departments to prepare course offerings (as per instructor preferences); which then provide a proposal for college approval; after which, the timetabling unit prepares the timetables. Once ready, the relevant timetables are provided to departments, instructors and students for viewing and/or registration respectively. This worth noting that while the general focus of academic literature remains solely on timetabling problem resolution, implementation of ATPS using ATP workflow provides a holistic approach which in addition to considering an efficient model development, allowed better understanding of a multi-stage system, its technology requirements and implementation challenges.

## 4.3. ATPS Architecture

The architecture consists of four modules viz. user interface module; data input module; optimization module and a report generation module. These modules are arranged and synchronized in tiers comprising a presentation layer; timetabling logic layer; and a data layer, as shown in Figure 2.

![](/api/attachments/FMFXSCZC/fulltext/images/fadb19041b92c07f34f35fed19bad07aba6e96e53413c9b3b5dd5963a1454760.jpg)  
Figure 2: ATPS Architecture

ATPS offers a web interface to its input and reporting functionalities as well as for MMILP model execution. Implemented as a web application using Java Server Pages (JSP) and its JSTL tags library, it is hosted on Apache Tomcat 8.0.27 server (http://tomcat.apache.org/). The web application currently runs on the university’s local area network (planned to be available via internet in future). Based on the roles/access (Table 3), the application uses an authenticated login. The user is then directed to various ATPS functionalities as per user access roles. Through this interface, the relevant users (i.e., department and college management) can define course characteristics and faculty assignments, do approvals and access relevant reports.

The data input module stores all the information necessary for generating the course schedules in a relational database, implemented using MySQL version 5.7 (https://www.mysql.com/). The entity relationship diagram (ERD) of the complete data model is depicted in Figure 3.

![](/api/attachments/FMFXSCZC/fulltext/images/8c69495328ca256a71f729e0910e8258453ae93484d58ce983c6cd7272b09840.jpg)  
Figure 3: Entity Relationship Diagram of ATPS Database

The database contains twelve tables, whereas the User table stores all user-related personal information and defines a user access role as a Privilege (as defined in Table 3). Each user belongs to only one Department, headed by a department head. Course information is stored in Course table, which is further used to define course offerings for a specific term distinguished by the attribute Offering\_ID in Curr\_Course\_Offering table. Instructors assigned to these offerings are listed in the

Teaching\_Assign table. Cohort IDs and course-sections associations are managed through Cohort and Cohort\_section\_Link tables. While Room\_List, Period\_Type and Session tables contain data related to infrastructure and timetabling policies. Note that the management of different versions of timetables and offerings are maintained through Offering\_Admin table and the linked Timetable\_ID and Offering\_ID keys in different tables.

The Timetable table plays a central role in storing the details of timetables as it receives cohort-related information from the Cohort table, while information related to rooms, sessions and period types comes from the Room\_List, Session and Period\_Type tables respectively. The Cohort table is linked to the Timetable table through the bridge table Cohort\_Section\_Link. Each course offering is distinguished within the Timetable entity with the attributes of Timetable\_ID, Course\_ID and Section\_ID as a composite primary key, which gives each timetable, course and its sections a unique identity and supports in archiving previous timetable information as historical data.

The optimization module is powered by the timetabling engine which comprises a Processor computer program that employs Python (version 3.5 64 bit) component which reads details of current PyMySQL 0.7.11 connector, https://pypi.python.org/pypi/PyMySQL), writes the MMILP model (section 7.2), invokes the solver (Gurobi 7.1, http://www.gurobi.com/), reads the solver output solution, decodes this output and writes the solution (i.e., master timetable) to the Timetable table in the database. The report generation module, accessible via interface, is used for generating several customized reports (listed in Table 3) through DML queries. For example, an instructor may see his/her personal level teaching timetable and teaching history as shown in Figure 4 and Figure 5. Please note that actual user information as well as ATP scheduler logo is removed (greyed) for privacy purposes. A similar example is presented in Figure 6 for a department head, which shows the course offering input module screen shots; i.e. Figure 6 (left) for adding a new course including the course, its male and female sections and instructors; while Figure 6 (right) shows the list of entered courses and links to delete or update an offering. Similarly, a comprehensive department instructors timetable (for a dept. head) is shown in Figure 7.

![](/api/attachments/FMFXSCZC/fulltext/images/c2dff944506c2a30419a45e419c7ab4122a03e74ccf48cb2ecf49473a2e89046.jpg)

<table><tr><td></td><td>Sunday</td><td>Monday</td><td>Tuesday</td><td>Wednesday</td><td>Thursday</td></tr><tr><td>8:00 - 9:30</td><td></td><td>ACCT203-1033033(CBA)</td><td></td><td></td><td>ACCT203-1033033(CBA)</td></tr><tr><td>9:30 - 11:00</td><td>ACCT520-4011007(CBA)</td><td>ACCT203-1013033(CBA)</td><td>ACCT520-4011007(CBA)</td><td></td><td>ACCT203-1013033(CBA)</td></tr><tr><td>11:00 - 12:30</td><td>ACCT435-4011006(CBA)</td><td></td><td>ACCT435-4011006(CBA)</td><td></td><td></td></tr><tr><td>12:30 - 02:00</td><td></td><td>ACCT203-1021010(CBA)</td><td></td><td></td><td>ACCT203-1021010(CBA)</td></tr></table>

## Figure 4: An ATPS Example of an Instructor Timetable

![](/api/attachments/FMFXSCZC/fulltext/images/bc77eda13759b5743190595f67f6c0ea40b0b01ba8876b06974996e8e2b9396b.jpg)  
MY REPoRTS: | Courses I Taught Previously | My Schedule

<table><tr><td>Term</td><td>Course Code</td><td>Course Name</td></tr><tr><td>200171801</td><td>ACCT203</td><td>Principles of Financial Accounting</td></tr><tr><td>200171801</td><td>ACCT435</td><td>Corporate Governance</td></tr><tr><td>200171801</td><td>ACCTS20</td><td>Auditing II</td></tr></table>

Figure 5: An ATPS Example of an Instructor Teaching History

<table><tr><td colspan="13">Add a NEW course offering for term</td></tr><tr><td>Course ID:</td><td colspan="12">MIS206: PMIS</td></tr><tr><td>Number of Male Sections:</td><td colspan="12">0</td></tr><tr><td>Number of Female Sections:</td><td colspan="12">0</td></tr><tr><td>Year Offered to:</td><td colspan="12">1</td></tr><tr><td>Course Nature:</td><td colspan="12">Sp</td></tr><tr><td rowspan="6">Faculty Assignment</td><td>Faculty</td><td>Male</td><td>Female</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>- select an option --</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>- select an option --</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>- select an option --</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>- select an option --</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>- select an option --</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Add Course</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Figure 6: Course Offering Management in ATPS: Left) Offering input, Right) Offering Report

![](/api/attachments/FMFXSCZC/fulltext/images/437ff70357d509bab089c5bffbaddad04212826351d2399314cf36e6649a5c72.jpg)  
Figure 7: A Screenshot of a Department’s Instructor Timetables Page

## 4.3.1. The Optimization Model

This section details a new curriculum driven multi-objective mixed integer programming timetabling model (MMILP). The model is dealt in the system by the processor, which reads the input data from the database; converts it into an optimization model that is solved by the solver; then the processor decodes the solver output (i.e., the comprehensive timetable), and finally stores it into the database.

The mathematical details of this timetable model are presented in Appendix (section 7). All the needed notations in the model are also presented in Appendix, where first two key binary decision variables are related to: 1) sections to room, period and session assignment i.e., $X _ { { } _ { r b d q } } ^ { s c a } = 1$ if section s of course c department a is assigned to room r in building b, days d and session q; and, 2) instructor to section, days and session assignment i.e., $Y _ { i d q } ^ { s c a } = 1$ if instructor i is assigned to section s of course c department a on days d and session q.

The model follows the problem presented in section 3. The model requirements or constraints are divided in six types for ease of exposition, where the first type is related to room assignments. In this, constraints (1)-(3) ensure that all male and female sections are assigned a single room in the appropriate buildings on any allowable day and session combination. The second set of constraints (4) -(8) are labeled as instructor assignments, which enforce that each course section is allotted to exactly one instructor, who is also assigned to teach that course. This is done is a way that all instructors teaching the course must not get more female or male sections than what is assigned to them. These constraints also ensure that an instructor is assigned to at most one section during a session on any given day and that each instructor must not teach more than 2 sections in a row on a day. Constraints (9) link the room and instructor assignments.

The third set belongs to cohort groups, which are represented by constraints (10)-(12), which ensure that for each male or female cohort group belonging to a year and program there are no time conflicts and have a maximum of two classes in a row on any given day. Also, it is ensured that rooms assigned to the cohort groups are large enough to hold the maximum number of students in the cohort group.

The fourth group of the constraints deal with custom requests received by the timetabling unit. These requests are valid to individual instructors or groups of certain students. It is easy to see that generalization is not possible and custom constraints are to be introduced manually in the processor and solving the models. In general, we see constraints where the units need to block or enforce a period type or sessions or both for an individual or group of students or instructors. Similarly, a request may require a part time instructor to be available at the college during certain days and time. Or, an academic department requiring all its instructor to be free for meetings. Examples of some of these typical constraints are provided under the custom constraints heading in Appendix. Variable types are defined in the sixth group.

Finally, as mentioned in section 3, the two objectives of the timetabling exercise are that time difference between the start and end of the teaching day for the instructors and students are to be minimized. It is also stated that it was done only by casually looking at the respective schedules. When we started ATPS, we formally defined two metrics, one each for the objectives representing a lack of compactness i.e., $V _ { i } ^ { e }$ and $U _ { g y p } ^ { e }$ for instructors and cohort groups schedules respectively that are to be minimized. These measures are defined through (18) and (19), where in both a point is scored if the two sessions on a day have classes in a row, a score of 2 if classes are in the first and the third session and so on. Consequently, the largest score is assigned when on any given day classes start first class in the morning and ends the last class of the day. A more elaborate example of score calculation is also provided in Appendix. Furthermore, as we have two objective functions, we take the weighted average to convert it to single objective function. While in section 5.2, we study the effects of weights, we note that after a discussion with college management the weights  and 1- are both set to 0.5 to get equal weightage to both the instructors and the cohort groups objective functions.

We also comment here that finding a feasible solution is a must for a term to become operational. The model infeasibility is mainly rooted in the lack of rooms or instructors or time slots in our problem. The availability of all these are the responsibility of the college management, which makes additional rooms, or part time instructors available as needed, or in some cases change the time policy by extending the teaching hours. consequently, any infeasibility is always dealt with at the pretimetabling level.

## 5. Computational Study

In this section, we first present a base-case example (section 5.1), that is based on the ATP performed using ATPS in the latest semester. However, some key information (e.g., course codes, instructor names etc.) is replaced with dummy representatives for privacy purposes. Following the base-case, we also present the details of the study performed to test the computational performance of the MMILP model (section 5.2).

## 5.1. Base Case Example

As stated, we now present a base-case example based on the ATP performed in the last semester. For this ATP, the infrastructure data is presented in Table 4. Here, Building A is dedicated to teaching female students, who have an enrollment close to 900 students, while building B is dedicated to teaching male students (enrollment: 400 students). There are 52 instructors which commute between the two buildings for teaching.

<table><tr><td>Building</td><td>Rooms</td><td>Capacity</td></tr><tr><td>A</td><td>17 Rooms</td><td>45</td></tr><tr><td>A</td><td>2 Rooms</td><td>25</td></tr><tr><td>B</td><td>7 Rooms</td><td>45</td></tr><tr><td>B</td><td>4 Rooms</td><td>25</td></tr></table>

Table 4: College Infrastructure Details

The course offering by the departments are based on the study plan requirements of students, student enrollment in different levels (i.e., 1<sup>st</sup>, 2<sup>nd</sup>, 3<sup>rd</sup> or 4<sup>th</sup> years) of respective programs, and the instructors’ teaching preferences. Please note that we’ll refer to the three programs offered by the college as Programs A, B & C and correspondingly departments A-F, with the first three offering the programs. In terms of the study plans, in their first three semesters students do not join any specific program (i.e., 1<sup>st</sup> year and first semester of the $2 ^ { \mathrm { n d } }$ year) and stay with the college to take some general courses. At this stage, mainly the support departments (D, E & F) offer courses, while some program-based departments also offer courses to these students. Once students choose a program, their study programs change accordingly and then the departments must offer them specialized courses besides some college level courses. A summary of course offerings is presented in Table 5. Please note that each of the course is multi-section with more sections offered to female students as compared to male students due to difference in enrollment sizes.

Recall the notion of cohort groups introduced earlier (sections 1 and 2). In this sense, there are 6 cohorts each in the first and the second year, and 4, 3 and 3 cohort each in programs A-C respectively in years 3 and 4.

The above problem is solved using ATPS, where the problem size and computational details are provided in Table 6 below. The model is generated using a Python based timetabling engine processor in 12.03 seconds, whereas the solver used is Gurobi (through Python interface) on a computer running Windows 7 (64bit), and having intel i7 processor, 64GB RAM and using 8 threads. The model is solved to optimality in 14.47 seconds. The weights and 1- on the two objective functions (shown in (21)) are set to 0.5.

While there are several individual schedules in the solution generated (i.e., 52 individual instructor schedules and 38 schedules for cohort groups) that all comply to the given policies, we show below (Table 7) a case of two female $4 ^ { \mathrm { t h } }$ year cohorts belonging to program C. In this table the entry notations e.g., C502-C1 are read as: C502 being the course code offered by department C, whereas C1 and C2 are the two cohort groups. Referring to Table 5, we note that while both cohorts are independent in terms of course sections (other than resource availability pertaining to rooms and instructors), it does share two course sections. That is, both cohorts will have to gather in the same location to a same instructor for both course sections. All other courses may be at taken at different times. These two courses are highlighted by light and dark grey colors respectively. Also note that the two timetables comply to all the other listed polices. Similar timetables are generated for all the other 38 cohorts and 52 instructors and were found to be of similar forms.

<table><tr><td rowspan="2">Level</td><td rowspan="2">Offering</td><td colspan="2">Number of Sections per Course</td><td rowspan="2">Offered by</td></tr><tr><td>Female</td><td>Male</td></tr><tr><td> $1^{st}$ year – college</td><td>5 courses</td><td>6 each</td><td>3 each</td><td>1 Course Each by Department A, B, D, E, &amp; F</td></tr><tr><td> $2^{nd}$ year – college</td><td>5 courses</td><td>6 each</td><td>3 each</td><td>1 Course Each by Department A &amp; E and 3 Courses by Department D</td></tr><tr><td> $3^{rd}$ year - program A</td><td>3 courses</td><td>3 each</td><td>1 each</td><td>All by Department A</td></tr><tr><td> $3^{rd}$ year - program B</td><td>3 courses</td><td>2 each</td><td>1 each</td><td>All by Department B</td></tr><tr><td> $3^{rd}$ year - program C</td><td>3 courses</td><td>2 each</td><td>1 each</td><td>All by Department C</td></tr><tr><td> $3^{rd}$ year – college</td><td>2 courses</td><td>6 each</td><td>3 each</td><td>Both by Department D</td></tr><tr><td> $4^{th}$ year - program A</td><td>4 courses</td><td>3 each</td><td>1 each</td><td>All by Department A</td></tr><tr><td> $4^{th}$ year - program B</td><td>4 courses</td><td>2 each</td><td>1 each</td><td>All by Department B</td></tr><tr><td> $4^{th}$ year - program C</td><td>4 courses</td><td>2 each for 3 courses/1 section for the  $3^{rd}$  course</td><td>1 each</td><td>All by Department C</td></tr><tr><td> $4^{th}$ year – college</td><td>1 courses</td><td>6 each</td><td>3 each</td><td>Department D</td></tr></table>

Table 5: Course offerings

<table><tr><td>Integer (Binary)</td><td>Constraints</td><td>Model Generation time (secs)</td><td>Gap</td><td>Solution Time (secs)</td></tr><tr><td>37967 (37236)</td><td>23767</td><td>12.03</td><td>0%</td><td>14.47</td></tr></table>

Table 6: Base Case Problem Size and Computational Performance

<table><tr><td></td><td>Sunday</td><td>Monday</td><td>Tuesday</td><td>Wednesday</td><td>Thursday</td></tr><tr><td>Session 1</td><td>C501-C1Instructor 1Build. A, Room 8</td><td></td><td>C501-C1Instructor 1Build. A, Room 8</td><td></td><td></td></tr><tr><td>Session 2</td><td>C502-C1/C2Instructor 4Build. A, Room 6</td><td></td><td></td><td>C502-C1/C2Instructor 4Build. A, Room 6</td><td></td></tr><tr><td>Session 3</td><td></td><td>C450-C1Instructor 2Build. A, Room 10</td><td></td><td></td><td>C450-C1Instructor 2Build. A, Room 10</td></tr><tr><td>Session 4</td><td>D305-C1/C2Instructor 5Build. A, Room 13</td><td>C470-C1Instructor 3Build. A, Room 13</td><td>D305-C1/C2Instructor 5Build. A, Room 13</td><td></td><td>C470-C1Instructor 3Build. A, Room 13</td></tr><tr><td></td><td>Sunday</td><td>Monday</td><td>Tuesday</td><td>Wednesday</td><td>Thursday</td></tr><tr><td>Session 1</td><td>C450-C2Instructor 2Build. A, Room 10</td><td></td><td>C450-C2Instructor 2Build. A, Room 10</td><td></td><td></td></tr><tr><td>Session 2</td><td>C502-C1/C2Instructor 4Build. A, Room 6</td><td>C501-C2Instructor 1Build. A, Room 11</td><td></td><td>C502-C1/C2Instructor 4Build. A, Room 6</td><td>C501-C2Instructor 1Build. A, Room 11</td></tr><tr><td>Session 3</td><td></td><td>C470-C2Instructor 3Build. A, Room 9</td><td></td><td></td><td>C470-C2Instructor 3Build. A, Room 9</td></tr><tr><td>Session 4</td><td>D305-C1/C2Instructor 5Build. A, Room 13</td><td></td><td>D305-C1/C2Instructor 5Build. A, Room 13</td><td></td><td></td></tr></table>

Table 7: Schedule of Two Cohorts Sharing a Course Section

# ACCEPTED MANUSCRIPT

## 5.2. Computational Performance

We also performed some computational tests to evaluate the performance of the MMILP model when the problem scales to different levels under different parameter settings (Table 8). Here problem 7, is the base case example discussed in section 5.1. In all these cases, the infrastructure (buildings and rooms) is the same across all problems; however, number of sessions (q) vary between 4 and 5 for a particular setting of course offerings (C<sup>a</sup>), instructors teaching in that term (I), the corresponding number of sections (S(C<sup>a</sup>)) and cohorts (G). There are five such settings tested which is to cover from smaller to larger sized problems. Problems 1-2 are where there is only one batch of students in 1<sup>st</sup> year taking 5 courses (9 sections each – 45 sections) and taught by 15 instructors. Similarly, problems 3-4 are where there are two batches (in 1<sup>st</sup> and 2<sup>nd</sup> years), problems 5-6 where there are three batches (in 1<sup>st</sup>, 2<sup>nd</sup> and 3<sup>rd</sup> years), and the rest have all the four batches $( \mathrm { i . e . , 1 ^ { s t } }$ to 4<sup>th</sup> year). Problem 9-10 is where we considered scenario with 4 batches but with increased number of sections. For all these problems, the model size in mentioned where number of integer (and binary) variables and the number of constraints is reported. We also report the model generation time by the timetabling engine as well as the solution time by the solver for all the problems. Note that there are three problems for which we had the data where the timetables are done manually by the unit earlier. And hence we also report the % decrease in objective function value (last column, Table 8) when the same problems were solved by the new model.

<table><tr><td>#</td><td>b</td><td>r</td><td>q</td><td>d</td><td> $C^a$ </td><td> $S(C^a)$ </td><td>G</td><td>I</td><td>integers (binary)</td><td>constraints</td><td>Model Gen. time</td><td>Gap</td><td>solution time</td><td>%Δ on manual soln.</td></tr><tr><td>1</td><td>2</td><td>26</td><td>4</td><td>3</td><td>5</td><td>45</td><td>9</td><td>15</td><td>6,018 (5,856)</td><td>3,989</td><td>1.383</td><td>0%</td><td>0.34</td><td>-8.1%</td></tr><tr><td>2</td><td>2</td><td>26</td><td>5</td><td>3</td><td>5</td><td>45</td><td>9</td><td>15</td><td>7,504 (7,320)</td><td>4,537</td><td>1.657</td><td>0%</td><td>0.51</td><td>-</td></tr><tr><td>3</td><td>2</td><td>26</td><td>4</td><td>3</td><td>15</td><td>94</td><td>19</td><td>39</td><td>13,100 (12,712)</td><td>8,674</td><td>2.795</td><td>0%</td><td>2.16</td><td></td></tr><tr><td>4</td><td>2</td><td>26</td><td>5</td><td>3</td><td>15</td><td>94</td><td>19</td><td>39</td><td>16,330 (15,890)</td><td>9,882</td><td>3.621</td><td>0%</td><td>1.25</td><td>-13.6%</td></tr><tr><td>5</td><td>2</td><td>26</td><td>4</td><td>3</td><td>29</td><td>138</td><td>28</td><td>46</td><td>17,888 (17,408)</td><td>11,724</td><td>4.339</td><td>0%</td><td>3.14</td><td>-</td></tr><tr><td>6</td><td>2</td><td>26</td><td>5</td><td>3</td><td>29</td><td>138</td><td>28</td><td>46</td><td>19,800 (19,260)</td><td>12,139</td><td>5.43</td><td>0%</td><td>8.03</td><td>-14.6%</td></tr><tr><td>7</td><td>2</td><td>26</td><td>4</td><td>3</td><td>34</td><td>186</td><td>38</td><td>52</td><td>37,967 (37,236)</td><td>23,767</td><td>8.679</td><td>0%</td><td>14.47</td><td>-</td></tr><tr><td>8</td><td>2</td><td>26</td><td>5</td><td>3</td><td>34</td><td>186</td><td>38</td><td>52</td><td>47,393 (46,545)</td><td>27,924</td><td>11.982</td><td>0%</td><td>11.13</td><td>-</td></tr><tr><td>9</td><td>2</td><td>26</td><td>4</td><td>3</td><td>34</td><td>201</td><td>41</td><td>58</td><td>43,120 (42,300)</td><td>29,969</td><td>11.649</td><td>0%</td><td>160.72</td><td>-</td></tr><tr><td>10</td><td>2</td><td>26</td><td>5</td><td>3</td><td>34</td><td>201</td><td>41</td><td>58</td><td>53,827 (52,875)</td><td>35,340</td><td>15.546</td><td>0%</td><td>29.00</td><td>-</td></tr></table>

Table 8: Computational Performance of the ATP MMILP Model

The model generation times turn out to be quite reasonable ranging between 1.39 seconds to 15.6 seconds; while solution times (to optimality in all cases) also turn out to quite reasonable ranging between 0.34 second for problem 1 to maximum of 160.72 seconds for problem 9. Note, that the solution times for problem 7 and 9 turn out to be larger than their counterparts 8 and 10. In both cases, with problems 7 and 9 the number of sessions is 4 as compared to 5 in problems 8 and 10. While the model sizes are bigger in problems 8 and 10, in problems 7 and 9, the detailed analysis of solutions revealed that the flexibility was minimal with almost all of the time slots for all the available rooms were full and the solver took longer to converge to optimal solution. Finally, we note that the comparison with the old manual solution revealed an improvement of approximately 8 to 14.6%. The numbers are expected given only 4-5 timeslots available in a day.

We also evaluated the effect of weights on the base case example problem setting. The weights  (and 1- ) in objective function in (21) is varied between 1 and zero (step 0.1) (vice-versa with (1- )) and the results are shown in Figure 8. The objective function related to cohort groups seems to be a bit more sensitive to its weight than the objective function related to instructors, where the range of the objective function value for the first one is 34 points vs. 20 points for the second. In general, we compact, however, it did not affect all of the cohort timetables. This is explainable as the number of time slots in a day are only 5; additionally, there are other constraints such as maximum continuous sessions limited to 2 on any day keep the room for loosing compactness to very small. The effects, of the change of weight related to instructors i.e., 1- is seen to be small as very few instructors are heavily loaded with most instructors ranging with a teaching load of 9 to 12 contact hours.

![](/api/attachments/FMFXSCZC/fulltext/images/43f9143d73f44a919e74837c3f35bd24d59c22854ba2eaa9e65bdbfa987a7884.jpg)  
Figure 8: Pareto Front of Base Case Example

## 6. Conclusions

In this work, we presented a web-based group DSS i.e., ATPS, that solves the faced timetabling scenario using a multi-objective mixed integer programming model. The task was undertaken due to significant and consistent growth in student enrollment where use of earlier semi-automated timetabling mechanism became infeasible. While the ATPS supports the timetabling management, it also facilitates the entire term planning work flow using a web application. The ATP scenario faced is primarily Curriculum-based Course Timetabling; however, with multi-section course offerings that allows students to choose across sections, our problem can be viewed as Curriculum-based Course Timetabling with Student Sectioning or CCTSS. An important concept used here is that of cohort groups that allows several feasible options to students.

The general feedback from all the stakeholders suggests several benefits including 1) improvement in the overall quality of the timetables; 2) increased efficiency in the ATP coordination through a web interface; 3) extensive customized (role-based) reporting with access to historical data that helps in record keeping as well as planning; 4) significantly reduced timetabling lead times; and most importantly, 5) eradication of human errors in timetabling solutions.

While we solved all the considered problem scenarios to optimality, besides considerably increasing in the college enrollment, there are plans to start several new graduate programs as well. Consequently, work is already under way in terms of increasing capacity i.e., increasing classrooms as well as hiring new instructors. In this sense, we see a possibility of solution challenges. We thus have started working on methodologies that allow feasible solutions to much larger problems.

## 7. Appendix: Modeling Framework

In this section, we present the modeling framework for the timetabling problem presented in section 2. We first present modeling notations in section 7.1, while the model is presented in section 7.2.

## 7.1. Notations

Following are the notation used in developed optimization model:

## Sets and indices:

y : Year of study (For a four-year program $y = 1 , 2 , 3 , 4 )$ q: Session index b: Building index r: Room index d: Period type index (Table 2) a: Academic unit or department index

D: Set of period types, index d

Q: Set of sessions available per day, indexed q Set of academic units, indexed a

$D ^ { c a }$ <sup>:</sup> Set of period types associated with a course c of department a, indexed $d ^ { c a }$

$P$ : Set of degree programs offered by corresponding academic units, indexed $p$

B: Set of buildings, indexed b

$R ^ { b }$ : Set of classrooms in building b, where $R F ^ { b } \subseteq R ^ { b }$ and $R M ^ { b } \subseteq R ^ { b }$ are male/female classrooms respectively

$C ^ { a }$ : Set of courses offered by academic unit a, indexed ca

$S ^ { c a }$ : Set of sections of courses c of department a indexed sca, where $S F ^ { c a } \subseteq S ^ { c a }$ and $S M ^ { c a } \subseteq S ^ { c a }$ are female/male sections respectively

$I C _ { i } .$ Set of courses taught by instructor i

$I ^ { c a }$ <sup>:</sup> Set of instructors belonging to courses c department a, indexed $i ^ { c a }$ , where $I F ^ { c a } \subseteq T ^ { c a }$ and $I M ^ { c a } \subseteq T ^ { c a }$ are instructors of male/female sections and I the set of all instructors

${ \overline { { f s } } } _ { i } ^ { c a } , { \overline { { m s } } } _ { i } ^ { c a }$ : Number of female and male sections taught by instructor i of course c, department a

$G _ { _ y } ^ { p }$ : Set of cohort groups related to year y of major $p .$ Here, $G F _ { y } ^ { a } \in G _ { y } ^ { a }$ and $G M _ { _ y } ^ { a } \in G _ { _ y } ^ { a }$ are sets of female/male cohort groups for each $y , p .$

$H _ { _ y } ^ { p }$ <sup>:</sup> Set of student capacity associated with a cohort group, indexed $h _ { \ y } ^ { p }$

## Parameters and Variables:

$C A P ^ { r b }$ : Capacity of room r in building b

$q ^ { \prime \prime }$ : Maximum number of continuous sessions allowed in a day for a cohort group or an instructor

## Decision Variables:

$\begin{array} { r l } { X _ { r b d q } ^ { s c a } } & { { } = \left\{ \begin{array} { l l } { 1 } \\ { 0 } \end{array} \right. } \end{array}$ if section  is assigned to roomsca $^ { r b , }$ period type $d ,$ session q otherwise

$\begin{array} { r l } { Y _ { i d q } ^ { s c a } } & { { } = \biggl \{ \begin{array} { l l } { 1 } \\ { 0 } \end{array} } \end{array}$ if section   is assigned to  instructor sca $i ,$ period type $d ,$ session q otherwise

$U _ { _ { g y p } } ^ { e }$ <sub>:</sub> Schedule compactness measure for cohort gpy on day e (defined in section 7.2.2)

$V _ { i } ^ { e }$ Schedule compactness measure for instructor i on day e (defined in section 7.2.2)

## 7.2. Model:

We first define constraints in section 7.2.1, followed by objective function in section 7.2.2.

## 7.2.1. Constraints:

For expositional reasons, we group the constraints of similar nature i.e., room assignments, instructor assignments, cohort groups, custom constraints and variable types:

Room Assignments:

$$
\sum \sum \sum X _ {r b d q} ^ {s c a} = 1
$$

$$
\forall s c a \in S F ^ {c a}, \text {   where   } r \text {   in   } b \in R F ^ {b} (a)
$$

$$
\sum_ {q \in Q} ^ {q \in Q} \sum_ {d \in D ^ {c a}} \sum_ {r} ^ {r} X _ {r b d q} ^ {s c a} = 1
$$

$$
\forall s c a \in S M ^ {c a}, \text {   where   } r \text {   in   } b \in R M ^ {b} (b)\tag{1}
$$

$$
\sum X _ {r b d q} ^ {s c a} \leq 1
$$

$$
\forall r \text {in} b \in R F ^ {b}, d, q (a) ^ {2}
$$

$$
\sum_ {s c a \in S M ^ {c a}} ^ {s c a \in S F ^ {c a}} X _ {r b d q} ^ {s c a} \leq 1
$$

$$
\forall r \text {   in   } b \in R M ^ {b}, d, q (b)\tag{2}
$$

$$
\sum_ {s c a \in S F ^ {c a}} X _ {r b d q} ^ {s c a} + X _ {r b d ^ {\prime} q} ^ {s c a} \leq 1
$$

$$
\forall r \text {   in   } b \in R F ^ {b}, q, d = 2, d ^ {\prime} = 3 (a)
$$

$$
\sum_ {s c a \in S M ^ {c a}} X _ {r b d q} ^ {s c a} + X _ {r b d ^ {\prime} q} ^ {s c a} \leq 1
$$

$$
\forall r \text {   in   } b \in R M ^ {b}, q, d = 2, d ^ {\prime} = 3 (b)\tag{3}
$$

Instructor Assignments:

$$
\begin{array}{l} \sum_ {q \in Q} \sum_ {d \in D ^ {c a}} \sum_ {i \in I F ^ {c a}} Y _ {i d q} ^ {s c a} = 1 \\ \sum_ {q \in Q} \sum_ {d \in D ^ {c a}} \sum_ {i \in I M ^ {c a}} Y _ {i d q} ^ {s c a} = 1 \end{array}
$$

$$
\forall s ^ {c a} \in S F ^ {c a} (a)
$$

$$
\forall s ^ {c a} \in S M ^ {c a} (b)\tag{4}
$$

$$
\sum_ {q \in Q} \sum_ {d \in D ^ {c a}} \sum_ {\forall s c a \in S F ^ {c a}} Y _ {i d q} ^ {s c a} \leq \overline {{f s}} _ {i} ^ {c a}
$$

teachingi $c a \in I C _ { _ i }$ ( )a

$$
\sum_ {i = 0} ^ {\infty} \sum_ {s a + 1} \sum_ {m} Y _ {i d q} ^ {s c a} \leq \overline {{m s _ {i}}} ^ {c a}\tag{5}
$$

teachingi $c a \in I C _ { _ i }$ ( )b

$$
\sum_ {s c a} Y _ {i d q} ^ {s c a} \leq 1
$$

$$
\forall i \text {   teaching   } c a \in I C _ {i}, d \in D ^ {c a}, q\tag{6}
$$

$$
\sum_ {s c a} Y _ {i d q} ^ {s c a} + Y _ {i d ^ {\prime} q} ^ {s c a} \leq 1
$$

$$
\forall i \text {   teaching   } c a \in I C _ {i}, q, d = 2, d ^ {\prime} = 3\tag{7}
$$

$$
\sum_ {q = \hat {q}} ^ {\hat {q} + q ^ {\prime \prime}} \sum_ {s c a} Y _ {i d q} ^ {s c a} \leq q ^ {\prime \prime}
$$

$$
\forall i \text {   teaching   } c a \in I C _ {i}, \hat {q} = 1, 2,..., | Q | - q ^ {\prime \prime}, d = 1 (a)\tag{8}
$$

$$
\sum_ {q = \hat {q}} ^ {\hat {q} + q ^ {\prime \prime}} \sum_ {s c a} Y _ {i d q} ^ {s c a} + Y _ {i d ^ {\prime} q} ^ {s c a} \leq q ^ {\prime \prime}
$$

$$
\forall i \text {   teaching   } c a \in I C _ {i}, \hat {q} = 1, 2,..., | Q | - q ^ {\prime \prime} d = 2, d ^ {\prime} = 3 (b)
$$

$$
\sum_ {r b \in R F ^ {\prime b}} X _ {r b d q} ^ {s c a} - \sum_ {i \in I} Y _ {i d q} ^ {s c a} = 0
$$

$$
\forall s c a \in S F ^ {c a}, d, q\tag{9}
$$

## Cohort Groups:

$$
\sum_ {r ^ {b} \in R F ^ {b}} \sum_ {s c a} X _ {r b d q} ^ {s c a} \leq 1
$$

$$
\forall c a \in (g _ {y} ^ {p} \in G _ {y} ^ {p}), q, d = 1\tag{a}
$$

$$
\sum_ {r b \in R F ^ {b}} \sum_ {s c a} X _ {r b d q} ^ {s c a} + X _ {r b d ^ {\prime} q} ^ {s c a} \leq 1\tag{10}
$$

$$
\forall c a \in (g _ {y} ^ {p} \in G _ {y} ^ {p}), q, d = 2, d ^ {\prime} = 3 (b)
$$

$$
\sum_ {q = \hat {q}} ^ {\hat {q} + q ^ {\prime \prime}} \sum_ {s c a \in g _ {u} ^ {p}} X _ {r b d q} ^ {s c a} \leq q ^ {\prime \prime}
$$

$$
\forall g _ {y} ^ {p} \in G _ {y} ^ {p}, \hat {q} = 1, 2, \dots , | Q | - q ^ {\prime \prime}, d = 1 (a)\tag{11}
$$

$$
\sum_ {q = \hat {q}} ^ {\hat {q} + q ^ {\prime \prime}} \sum_ {s c a \in g _ {y} ^ {p}} X _ {r b d q} ^ {s c a} + X _ {r b d ^ {\prime} q} ^ {s c a} \leq q ^ {\prime \prime}
$$

$$
\forall g _ {y} ^ {p} \in G _ {y} ^ {p}, \hat {q} = 1, 2, \dots , | Q | - q ^ {\prime \prime}, d = 2, d ^ {\prime} = 3 (b)
$$

$$
\sum_ {d} \sum_ {q} h _ {y} ^ {p} X _ {r b d q} ^ {s c a} \leq C A P ^ {r b}
$$

$$
\forall r \text { in } b \in R F ^ {b} \text { or } R M ^ {b}, s c a \in G _ {y} ^ {p}\tag{12}
$$

Here, constraints set (1)(a)/(b) ensures that all female/male sections of course ca be assigned exactly to one room r in allowable building $b , \ \mathsf { s e s s i o n } \ q$ of period type d. Similarly, constraints (2)(a)/(b) ensure that at most one female/male section be assigned to any eligible room r at a time, during any session $q ,$ period type d. It is important to note that since Mondays are overlapped for period types 2 and 3 (Table 2), for any session q, during these period types, only one course section can be scheduled in a room between these period types; this is ensured through (3).

To ensure that each section is assigned to an instructor teaching that course, we employ (4)(a)/(b). Constraints set (5)(a)/(b) are to ensure that all instructors teaching a course c of department a must not get more female/male sections than assigned. Similarly, to ensure that an instructor is assigned at most one section during any session q for period type d, constraints (6) are set; for overlapping period types 2 and 3, at most one corresponding session q is assigned between the two types through (7). Constraints (8)(a)/(b), ensure that each instructor teaches a maximum of $q ^ { \prime \prime }$ sections in a row during period type 1; and jointly types 2 and 3 respectively. Constraints (9) are technical constraints linking the corresponding $X _ { r b d q } ^ { s c a }$ and $Y _ { i d q } ^ { s c a }$ variables.

Since for any cohort group $g _ { y } ^ { p } \in G F _ { y } ^ { p } / G M _ { y } ^ { p }$ , we need to ensure that during any session q belonging to period type d=1 and d=2,3 respectively there are no parallel class sessions for the same group, we set (10)(a)/(b). Maximum continuous sessions in a row $( \mathrm { i } . \mathrm { e } . \leq q ^ { \prime \prime } )$ on any particular day for a cohort group $g _ { y } ^ { p } \in G F _ { y } ^ { p } / G M _ { y } ^ { p }$ is enforced through (11)(a)/(b). Constraints (12) ensures assignment of groups in rooms with appropriate capacities.

## Custom Constraints:

Timetabling unit at the college also deals with custom requests – request that are only valid to generalization is not possible and each time custom constraints are to be introduced individually to the model for fulfilling these requests manually to the model. Examples of such constraints include (13), which blocks or disallows students belonging to program 1 in year 2 from taking classes on d=2 and sessions 1,2.

$$
\sum_ {s c a \in (g _ {y} ^ {p} \in G _ {y} ^ {p})} X _ {r b d q} ^ {s c a} = 0
$$

$$
\forall p = 1; y = 2; d = 2, 3; q = 1, 2\tag{13}
$$

$$
\sum Y _ {i d q} ^ {s c a} \leq 0
$$

$$
\forall i \text {   teaching   } c ^ {a} \in I C _ {i}, \text {   where   } a = 1; d = 2; q = 2\tag{a}
$$

$$
\sum_ {s c a} ^ {s c a} Y _ {i d q} ^ {s c a} \leq 0\tag{14}
$$

$$
\forall i \text {   teaching   } c ^ {a} \in I C _ {i}, \text {   where   } a = 1... 7; d = 2; q = 4 (b)
$$

$$
\sum_ {q \in Q} \sum_ {s c a} Y _ {i d q} ^ {s c a} \leq 0
$$

$$
\forall i = 4, 6, 8 \text {   teching   } c ^ {a} \in I C _ {i}; a = 1; d = 2, 3\tag{15}
$$

$$
X _ {r b d q} ^ {s c a} + Y _ {i d q} ^ {s c a} = 2
$$

$$
s = 1, c = 2, a = 3, r = 3, b = 1, d = 1, q = 2, i = 5\tag{16}
$$

Similarly, (14) (a) is an example where all faculty belonging to the department a=1 are prevented from teaching on Wednesdays (d=2) for session 2 only due to their departmental meetings; while in (14) (b) all faculty member are blocked for teaching on Wednesday (d=2) for session 4 due to college wide non-teaching activities. Constraints set (15) is an example where instructor 4,6,8 are disallowed to teach on days d=2,3 (but still allowed to teach on d=1). Similarly, we can preset a particular section in a particular room $r ^ { b } , d , q$ for a particular faculty, as shown in (16).

Variable types:

$$
X _ {r b d q} ^ {s c a} \in \{0, 1 \}
$$

$$
\forall s, c, a, r, b, d, q\tag{a}
$$

$$
Y _ {i d q} ^ {s c a} \in \{0, 1 \}
$$

$$
\forall s, c, a, i,, d, q\tag{b}
$$

(17)

Finally, (17) define the variable types.

## 7.2.2. Objective Function:

There are two main objectives related to our problem. These are timetable compactness for students and instructors, which are defined using lack of compactness measures $U _ { g p y } ^ { e }$ and $\mathbf { \alpha } _ { | V _ { i } ^ { e } } ^ { | \it { V } ^ { e } }$ being minimized over all the cohort groups and instructors on each day e of the week. Here, it is important to note that d index on variables of type $X _ { _ { r b d q } } ^ { s c a }$ is always a function of e. That is, considering Table 2 scenario, $d { = } 1$ when $e { = } 1 , 3$ or Sundays and Tuesdays; d=2,3 for $e { = } 2$ or Mondays; $d { = } 2$ for $e { = } 4$ or Wednesdays; and $d { = } 3$ for $e { = } 5$ or Thursdays. This lack of compactness factor is defined through constraints (18), which mainly puts a higher score on used sessions by a cohort group which are far apart from each other. For example, if total sessions in a day are 6, and if both session 1 and 6 are used then the weight value is $( \hat { q } - q ) = 6 - 1 = 5$ , and th easure $( U _ { g p y } ^ { e } )$ value will be 5(1+1) = 10; similarly, if session 1 is used but not sixth we have $5 ( 1 + 0 ) = 5 . \ \mathrm { S i m i l a r l y }$ , for instructors, in the same manner, we define (19), which estimates the lack of compactness in the same way.

$$
\begin{array}{l l} U _ {g p y} ^ {e} = \sum_ {q = 1} ^ {| Q | - 1} \sum_ {\hat {q} = q + 1} ^ {| Q |} \sum_ {r b} \sum_ {\forall s c a \in g _ {y} ^ {p}} (\hat {q} - q) (X _ {r b d q} ^ {s c a} + X _ {r b d \hat {q}} ^ {s c a}) & \quad \forall g _ {y} ^ {p} \in G _ {y} ^ {a}, d \text {   corresponding   to   e   } = 1, 3, 4, 5 (a) \\ U _ {g p y} ^ {e} = \sum_ {q = 1} ^ {| Q | - 1} \sum_ {\hat {q} = q + 1} ^ {| Q |} \sum_ {\forall s c a \in g _ {y} ^ {p}} (\hat {q} - q) (X _ {r b d q} ^ {s c a} + X _ {r b d ^ {\prime} q} ^ {s c a} \\ \quad + X _ {r b d \hat {q}} ^ {s c a} + X _ {r b d ^ {\prime} \hat {q}} ^ {s c a}) & \quad \forall g _ {y} ^ {p} \in G _ {y} ^ {a}, d = 2, d ^ {\prime} = 3, e = 2 \quad (b) \end{array}\tag{18}
$$

$$
\begin{array}{l} V _ {i} ^ {e} = \sum_ {q = 1} ^ {| Q | - 1} \sum_ {\hat {q} = q + 1} ^ {| Q |} \sum_ {s c a} (\hat {q} - q) Y _ {i d q} ^ {s c a} + Y _ {i d \hat {q}} ^ {s c a} \qquad \forall i \text {teaching} c a \in I C _ {i}, d \text {corresponding to} e = 1, 3, 4, 5 (a) \\ V _ {i} ^ {e} = \sum_ {q = 1} ^ {| Q | - 1} \sum_ {\hat {q} = q + 1} ^ {| Q |} \sum_ {s c a} (\hat {q} - q) (Y _ {i d q} ^ {s c a} + Y _ {i d ^ {\prime} q} ^ {s c a} \\ \qquad \qquad \qquad \qquad \qquad + Y _ {i d \hat {q}} ^ {s c a} + Y _ {i d ^ {\prime} \hat {q}} ^ {s c a}) \quad \forall i \text {teaching} c a \in I C _ {i}, d = 2, d ^ {\prime} = 3, e = 2 (b) \end{array}\tag{19}
$$

Thus, the two objective functions can be defined as follows:

$$
\begin{array}{l} M i n \sum_ {e} \sum_ {g p y} U _ {g p y} ^ {e} \\ M i n \sum_ {e} \sum_ {\forall i \in I} V _ {i} ^ {e} \end{array}\tag{20}
$$

Converting this bi-objective problem into a single weighted objective function, where  and 1- are the weights associated with the two objective functions respectively, we have:

$$
\text { Min } \alpha \sum_ {e} \sum_ {g p y} U _ {g p y} ^ {e} + (1 - \alpha) \sum_ {e} \sum_ {\forall i \in I} V _ {i} ^ {e}\tag{21}
$$

## 8. Acknowledgement

The authors would like to thank the anonymous reviewer and the editor-in-chief for their constructive feedback and detailed comments that helped improve this article to its present form.

## 9. References

[1] B. McCollum, A. Schaerf, B. Paechter, P. McMullan, R. Lewis, A.J. Parkes, L.D. Gaspero, R. Qu, E.K. Burke, Setting the research agenda in automated timetabling: The second international timetabling competition, INFORMS Journal on Computing, 22 (2010) 120-130.

[2] V.A. Bardadym, Computer-aided school and university timetabling: The new wave, Practice and theory of automated timetabling, Springer1996, pp. 22-45.

[3] S. Daskalaki, T. Birbas, E. Housos, An integer programming formulation for a case study in university timetabling, European Journal of Operational Research, 153 (2004) 117-135.

[4] E. Burke, K. Jackson, J.H. Kingston, R. Weare, Automated university timetabling: The state of the art, The computer journal, 40 (1997) 565-571.

[5] G. Post, L. Di Gaspero, J.H. Kingston, B. McCollum, A. Schaerf, The third international timetabling competition, Annals of Operations Research, 239 (2016) 69-75.

[6] J. Miranda, P.A. Rey, J.M. Robles, udpSkeduler: A Web architecture based decision support system for course and classroom scheduling, Decision Support Systems, 52 (2012) 505-513.

[7] R. Lewis, A survey of metaheuristic-based techniques for university timetabling problems, OR spectrum, 30 (2008) 167-190.

[8] R. Barkhi, Y.-C. Kao, Evaluating decision making performance in the GDSS environment using data envelopment analysis, Decision Support Systems, 49 (2010) 162-174.

[9] S.H. Chan, Q. Song, S. Sarker, R.D. Plumlee, Decision support system (DSS) use and decision performance: DSS motivation and its antecedents, Information & Management, 54 (2017) 934-947.

[10] S. Arshad Raza, C. Standing, Towards a systemic model on information systems' adoption using critical systems thinking, Journal of Systems and Information Technology, 12 (2010) 196-209.

[11] D. de Werra, An introduction to timetabling, European journal of operational research, 19 (1985) 151-162.

[12] A. Schaerf, A survey of automated timetabling, Artificial intelligence review, 13 (1999) 87-127.

[13] R. Qu, E.K. Burke, B. McCollum, L.T. Merlot, S.Y. Lee, A survey of search methodologies and automated system development for examination timetabling, Journal of scheduling, 12 (2009) 55-89.

[14] H. Babaei, J. Karimpour, A. Hadidi, A survey of approaches for university course timetabling problem, Computers & Industrial Engineering, 86 (2015) 43-59.

[15] S.K. Kassicieh, D.K. Burleson, R.J. Lievano, Design and implementation of a decision support system for academic scheduling, Information & Management, 11 (1986) 57-64.

[16] C.R. Glassey, M. Mizrach, A decision support system for assigning classes to rooms, Interfaces, 16 (1986) 92-100.

[17] J.J. Dinkel, J. Mote, M. Venkataramanan, OR Practice—An Efficient Decision Support System for Academic Course Scheduling, Operations Research, 37 (1989) 853-864.

[18] J.A. Ferland, C. Fleurent, SAPHIR: A decision support system for course scheduling, Interfaces, 24 (1994) 105-115.

[19] E. Burke, D. Elliman, R. Weare, A genetic algorithm based university timetabling system, East-West Conference on Computer Technologies in Education, Crimea, Ukraine pp35-40, 1994.

[20] J. Stallaert, Automated timetabling improves course scheduling at UCLA, Interfaces, 27 (1997) 67-81.

[21] L.R. Foulds, D.G. Johnson, SlotManager: a microcomputer-based decision support system for university timetabling, Decision Support Systems, 27 (2000) 367-381.

[22] M. Dimopoulou, P. Miliotis, Implementation of a university course and examination timetabling system, European Journal of Operational Research, 130 (2001) 202-213.

[23] M. Dimopoulou, P. Miliotis, An automated university course timetabling system developed in a 147.

[24] S. Daskalaki, T. Birbas, Efficient solutions for a university timetabling problem through integer programming, European Journal of Operational Research, 160 (2005) 106-120.

[25] S.C. Sarin, Y. Wang, A. Varadarajan, A university-timetabling problem and its solution using Benders’ partitioning—a case study, Journal of Scheduling, 13 (2010) 131-141.

[26] J. Miranda, eClasSkeduler: a course scheduling system for the Executive Education Unit at the Universidad de Chile, Interfaces, 40 (2010) 196-207.

[27] S. Abdullah, H. Turabieh, On the use of multi neighbourhood structures within a Tabu-based memetic approach to university timetabling problems, Information Sciences, 191 (2012) 146-168.

[28] V. Cacchiani, A. Caprara, R. Roberti, P. Toth, A new lower bound for curriculum-based course timetabling, Computers & Operations Research, 40 (2013) 2466-2477.

[29] B. Domenech, A. Lusa, A MILP model for the teacher assignment problem considering teachers’ preferences, European Journal of Operational Research, 249 (2016) 1153-1160.

[30] H. Vermuyten, S. Lemmens, I. Marques, J. Beliën, Developing compact course timetables with optimized student flows, European Journal of Operational Research, 251 (2016) 651-661.

[31] C. Akkan, A. Gülcü, A Bi-criteria Hybrid Genetic Algorithm with Robustness Objective for the Course Timetabling Problem, Computers & Operations Research, 90 (2018) 22-32.

[32] M.W. Carter, A comprehensive course timetabling and student scheduling system at the University of Waterloo, International Conference on the Practice and Theory of Automated Timetabling, Springer, 2000, pp. 64-82.

[33] S.N. Jat, S. Yang, A guided search genetic algorithm for the university course timetabling problem, DOI (2009).

[34] S.N. Jat, S. Yang, A hybrid genetic algorithm and tabu search approach for post enrolment course timetabling, Journal of Scheduling, 14 (2011) 617-637.

[35] J. van den Broek, C.A. Hurkens, An IP-based heuristic for the post enrolment course timetabling problem of the ITC2007, Annals of Operations Research, 194 (2012) 439-454.

[36] H. Cambazard, E. Hebrard, B. O’Sullivan, A. Papadopoulos, Local search and constraint programming for the post enrolment-based course timetabling problem, Annals of Operations Research, 194 (2012) 111-135.

[37] S. Ceschia, L. Di Gaspero, A. Schaerf, Design, engineering, and experimental analysis of a simulated annealing approach to the post-enrolment course timetabling problem, Computers & Operations Research, 39 (2012) 1615-1624.

[38] R. Lewis, A time-dependent metaheuristic algorithm for post enrolment-based course timetabling, Annals of Operations Research, 194 (2012) 273-289.

[39] C. Nothegger, A. Mayer, A. Chwatal, G.R. Raidl, Solving the post enrolment course timetabling problem by ant colony optimization, Annals of Operations Research, 194 (2012) 325-339.

[40] A.L.a. Bolaji, A.T. Khader, M.A. Al-Betar, M.A. Awadallah, University course timetabling using hybridized artificial bee colony with hill climbing optimizer, Journal of Computational Science, 5 (2014).

[41] R.P. Badoni, D.K. Gupta, P. Mishra, A new hybrid algorithm for university course timetabling problem using events based on groupings of students, Computers & Industrial Engineering, 78 (2015) 12-25.

[42] J.A. Soria-Alcaraz, E. Özcan, J. Swan, G. Kendall, M. Carpio, Iterated local search using an add and delete hyper-heuristic for university course timetabling, Applied Soft Computing, 40 (2016) 581- 593.

[43] I. Méndez-Díaz, P. Zabala, J.J. Miranda-Bront, An ILP based heuristic for a generalization of the post-enrollment course timetabling problem, Computers & Operations Research, 76 (2016) 195-207.

[44] T.-P. Liang, Integrating model management with data management in decision support systems, Decision Support Systems, 1 (1985) 221-232.

[45] J.P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision support systems, 33 (2002) 111-126.

[46] T.-P. Liang, C.-C. Lee, E. Turban, Model management and solvers for decision support, Handbook on Decision Support Systems 1, Springer2008, pp. 231-258.

[47] N. Chahal, D. De Werra, An interactive system for constructing timetables on a PC, European Journal of Operational Research, 40 (1989) 32-37.

[48] H.K. Bhargava, D.J. Power, D. Sun, Progress in Web-based decision support technologies, Decision Support Systems, 43 (2007) 1083-1095.

[49] D.J. Power, Web-based and model-driven decision support systems: concepts and issues, AMCIS 2000 Proceedings, Association for Information Systems, 2000, pp. 352-387.

[50] M. Chen, Y. Liou, C.-W. Wang, Y.-W. Fan, Y.-P.J. Chi, TeamSpirit: Design, implementation, and evaluation of a Web-based group decision support system, Decision Support Systems, 43 (2007) 1186-1202.

[51] D.J. Power, R. Sharda, Model-driven decision support systems: Concepts and research directions, Decision Support Systems, 43 (2007) 1044-1061.

# ACCEPTED MANUSCRIPT

## Biographical Notes

Atiq Waliullah Siddiqui currently works as an assistant professor of MIS at the College of Business Administration, Imam Abdulrahman bin Faisal University, Saudi Arabia. He holds a PhD in Operations & Information Management, a Master’s degree in Systems Engineering and a Bachelor’s degree in Mechanical Engineering. His main research interests include scheduling, transportation reviewed journals including Risk Analysis, Computers & Education, Applied Mathematical Modeling, Transportation Research Part D: Transport and Environment, Computers & Industrial Engineering, and International Journal of Production Research.

Syed Arshad Raza currently works as an assistant professor of MIS at the College of Business Administration, Imam Abdulrahman bin Faisal University, Saudi Arabia. He completed his PhD in Management Information Systems from Edith Cowan University, Australia. He holds a Master’s degree in Information and Computer Science from King Fahd University of Petroleum and Minerals, Saudi Arabia, and bachelors in Mechanical Engineering from NED University of Engineering and Technology, Pakistan. His research interests include data/information visualization, iterative heuristics, information systems analysis and design, web development and e-commerce. He has published his research in a number of international peer reviewed journals including Computers and Industrial Engineering, Systemic Practice and Action Research and Journal of Systems and Information Technology.

Zeeshan Muhammad Tariq currently works as a lecturer of MIS at the College of Business Administration, Imam Abdulrahman bin Faisal University, Saudi Arabia. He has completed his postgraduation in Computer Science & holds a Bachelor’s degree in Software Engineering. He has spent almost a decade working in Telecommunication industry where he has worked at operational, as well as mid-managerial level for one of the leading international telecommunication firms. Holding best paper award in Multimedia Conference MISAA-08, his research area includes network management, SIP Attacks, IMS Security, databases & GIS.

# A Web-Based Group Decision Support System for Academic Term Preparation

Highlights:

 Curriculum and student sectioning based course timetabling

 A multi-objective mixed integer programming timetabling model

 A web-based group decision support system for academic term planning

 Decision support system supporting the entire multi-stage workflow

 Improved timetables and efficient planning coordination amongst all stakeholders
