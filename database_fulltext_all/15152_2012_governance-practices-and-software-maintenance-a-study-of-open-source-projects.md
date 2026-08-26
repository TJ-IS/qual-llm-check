---
otero_id: 15152
otero_key: "DWKWSKRP"
title: "Governance practices and software maintenance: A study of open source projects"
authors: "Vishal Midha; Anol Bhattacherjee"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.03.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Governance practices and software maintenance: A study of open source projects

Vishal Midha <sup>a,</sup>⁎, Anol Bhattacherjee b

<sup>a</sup> University of Texas-Pan American, United States

<sup>b</sup> University of South Florida, United States

## a r t i c l e i n f o

Article history: Received 7 June 2011 Received in revised form 27 February 2012 Accepted 12 March 2012 Available online 3 April 2012

Keywords: Software maintenance Governance Participation management Responsibility management Open source software

## a b s t r a c t

We have proposed a two-dimensional taxonomy of open source project governance, namely participation management and responsibility management. We have then formulated four hypotheses by linking the two dimensions to software maintenance time. These hypotheses were tested using maintenance data from 352 open source software projects. This study contributes to open source software maintenance literature by demonstrating the effects of the two governance dimensions on open source software maintenance outcomes.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Software products are different from most other products in the amount of effort, resources, and cost incurred during the maintenance phase of their life cycle. Through a meta-analysis approach, Rashid et al. [47] show that the total cost of software maintenance has been increasing from 35 to 40% to over 90% over the last few decades. Similar observations have been recorded in various other studies such as [33,46]. Consequently, the software industry has devoted a lot of attention to reducing maintenance costs and improving maintenance performance.

Software maintenance is de<sup>fi</sup>ned as “the correction of errors, and the implementation of modi<sup>fi</sup>cations needed to allow an existing system to perform new tasks, and to perform old ones under new conditions” [14]. The three types of maintenance efforts highlighted in this de<sup>fi</sup>nition – identifying and correcting errors, adding new functional capabilities, and modifying the software to meet changing technological or user needs – are called corrective maintenance, adaptive maintenance, and perfective maintenance respectively. Given the critical importance and enormous costs of software maintenance, most software <sup>fi</sup>rms manage the maintenance process using formally trained project managers, who are entrusted with the responsibility of coordinating teams of software programmers working on different maintenance activities. Governance, or overseeing, coordinating, and managing the job of individual software programmers, is therefore a critical component of the software maintenance process.

The role of governance has recently been examined within the context of software development. For instance, Tiwana [57] reports that governance practices, in the form of decision control rights, in<sup>fl</sup>uence ef<sup>fi</sup>ciency and effectiveness outcomes in traditional software development projects. But to the best of our knowledge, the role of governance in software maintenance has not yet been investigated. Our research addresses this gap in the maintenance literature by studying two aspects of governance practices — participation management and responsibility management in the open source software (OSS) maintenance context. We hypothesize how these practices in<sup>fl</sup>uence maintenance performance, and test those hypotheses within the context of open source software projects using maintenance data from 352 projects from the SourceForge database.

Initial research on open source software has focused on understanding why expert developers contribute valuable time and effort to open source projects without any overt incentives [54]. Reasons suggested include altruism, need for accomplishment, and status in the developer community (e.g., [40,48]). A second stream of research has explored software and process characteristics that may contribute to the success of open source projects. These characteristics include source code complexity, program modularity, task interdependence, and feedback opportunities (e.g., [42–44]). However, to the best of our knowledge, little attention has been devoted to understanding the role of governance practices in open source software maintenance. Our paper focuses on this gap in the open source literature by asking the research question: how do governance practices in<sup>fl</sup>uence open source software maintenance? Speci<sup>fi</sup>cally, we address the following research questions:

R1: Does participation management in OSS projects impact the maintenance tasks' productivity?

R2: Does responsibility management in OSS projects impact the maintenance tasks' productivity?

R3: Do these impacts differ across the different types of maintenance tasks?

This paper contributes to the software engineering literature by theorizing and empirically demonstrating the role of governance on software maintenance. It proposes a two-dimensional taxonomy for governance mechanisms for OSS projects. Secondly, it shows that software maintenance can be in<sup>fl</sup>uenced by re-aligning the governance policies, and that different types of project level governance-task type combinations can enhance the performance of OSS maintenance. Speci<sup>fi</sup>cally, it contributes to the open source literature by suggesting ways in which volunteer groups of contributors can be managed more effectively to maintain complex software products over their entire life cycle. Collectively, the proposed taxonomy and <sup>fi</sup>ndings of the study signi<sup>fi</sup>cantly extend the theoretical body of nascent and exploratory research stream of IT governance [38], and provide a direct practical solution to improve developers' productivity in software maintenance tasks.

The rest of the paper proceeds as follows. Section 2 presents the theoretical background and develops research hypotheses for empirical testing. Research methods employed for testing our hypotheses are described in Section 3. Data analytic techniques and <sup>fi</sup>ndings are presented in Section 4, following by a discussion of these <sup>fi</sup>ndings in Section 5. The paper concludes with a summary of its theoretical and practical implications.

## 2. Theory and hypotheses development

## 2.1. Software maintenance

Prior research on software maintenance can be broadly categorized into two groups. The <sup>fi</sup>rst group has focused on estimation models for software maintenance efforts. For example, Belady and Lehman [5] present a model to estimate the effort required to update an old version of a software product. Using six datasets from different contexts, Shepperd et al. [51] demonstrate estimation by analogy as an appropriate technique for estimating the staf<sup>fi</sup>ng needs for software maintenance. Fioravanti and Nesi [17] propose a generalized model for adaptive maintenance effort prediction for object oriented systems. Ahn et al. [1] propose an effort estimation model for software maintenance projects based on function points. Lucia et al. [37] use multiple regression analysis to construct corrective maintenance effort estimation models and validate them against real maintenance project data. These analyses suggest that maintenance effort can be estimated more accurately if the different types of maintenance tasks are taken into account.

The second group of research has examined techniques that can help improve software maintenance efforts and outcomes. For example, Mens and Tourwe [41] demonstrate how “refactoring” can bene<sup>fi</sup>t software maintenance by improving the internal structure of software code without altering its external behavior. Other factors that in<sup>fl</sup>uence software maintenance efforts are system size, system age, number of input/output data items, application type, and programming language [1,3–5,20,43]. Research has also shown that software maintenance can be improved by changing con<sup>fi</sup>guration management procedures, aligning maintenance rewards to organizational performance, predicting and prioritizing maintenance requests, developing guidelines for modifying and testing software, and implementing and integrating modern software engineering practices such as CASE and JAD [2,21].

Even though anecdotal evidence suggests that effective governance practices improves software maintenance outcomes [39], effective management of software developers has eluded much of the prior literature. For instance, there is no prior research that we are aware of that has examined how managing developer participation or allocation of responsibilities among developers in<sup>fl</sup>uences the outcomes of software maintenance projects. Certainly, developers are a critical resource in any software project, and the way they are managed is central to the success of any software project. This is more so for open source projects where they act in a voluntary capacity. Our research focuses on this gap in the literature by speci<sup>fi</sup>cally examining participation and responsibility management aspects of software project governance and their effects on open source software maintenance outcomes.

## 2.2. Open source software

Open source software projects have recently gained a lot of prominence in personal computing and business computing, as well as in the Internet computing space [26]. For example, the open source Apache server software runs more than half of all web servers today (Netcraft.com 2009), and over 75% of all domain name servers (DNS) use the open source Berkeley Internet Name Domain (BIND) program [63]. Open source software are available today across a wide range of computing domains such as operating systems (e.g., Linux), web browsers (e.g., Mozilla Firefox), of<sup>fi</sup>ce productivity suites (e.g., OpenOf<sup>fi</sup>ce), programming languages (e.g., Perl, PHP), database servers (e.g., PostgreSQL), enterprise resource planning systems (e.g., Compiere), content management systems (e.g., Joomla), security <sup>fi</sup>rewalls (e.g., Firestarter), customer relationship management systems (e.g., SugarCRM), personal <sup>fi</sup>nance software (e.g., TurboCASH), remote access software (e.g., OpenVPN), and many others. The popularity of the open source movement has expanded to new and unexpected domains such as pharmaceutical development, biological research, movie production, space exploration, education, and even developing recipes for open-cola [35]. To take advantage of this growing trend, major industry participants, such as IBM Corporation, Hewlett-Packard, and Sun Microsystems are increasingly dedicating signi<sup>fi</sup>cant resources to open source projects and/or release the source code for their previously closed source software.

The philosophy underlying open source software is to allow users free access to, and use of, software products and their source code, using an open network such as the Internet, under a public license. Users and developers are allowed to adapt, modify, and redistribute the software and/or its code in its original or modi<sup>fi</sup>ed form for their own use or that of others. Typically, such projects start when an individual (or group) feels a need for new software or a new feature in existing software to solve a personal or work-related problem, writes a software code to meet that need, and decides to release the software and code openly in the public domain [42]. Once released, the user community can modify the source code or customize it to their local needs, identify and report errors in the software, suggest new features and modi<sup>fi</sup>cations, and submit <sup>fi</sup>xes to existing bugs or new enhancements. Any such code <sup>fi</sup>xes or enhancement is reviewed by the core group of that open source project before it is integrated back into the kernel source code and released as a new version under the same public license. This process of program re<sup>fi</sup>nement and maintenance continues iteratively until the project has accomplished its goals, reached a stable state, or is otherwise abandoned.

Due to the long-term and iterative nature of its development, open source software requires signi<sup>fi</sup>cant long-term investments in maintenance. As an example, such continued maintenance efforts grew the open source Linux operating system from 176,000 lines of code in its <sup>fi</sup>rst version (released in March 1994) to over 12 million lines of code in its recent version released in September 2009 (Wikipedia, History of Linux). Maintenance activities for open source software, such as modi<sup>fi</sup>cation requests, bug <sup>fi</sup>xes, and new enhancements, are documented at SourceForge, the largest repository of open source software projects on the Internet. Software testing, code <sup>fi</sup>xing, and potential extensions and modi<sup>fi</sup>cations are often performed by highly skilled experts who invest a considerable amount of their personal time into these projects without any direct monetary rewards. Scattered across the globe, these open source programmers rarely meet face-to-face, interact solely via the Internet, and are brought together by their shared interest in software development. The work of these volunteer programmers is coordinated and managed by a core group of experts who review code modi<sup>fi</sup>cation requests and submitted code <sup>fi</sup>xes, decide on which modi<sup>fi</sup>cations to accept and in which order, and integrate them into the core kernel. Governing the work of open source programmers is a key aspect of open source software maintenance. In fact, governance may be more challenging for open source projects than for traditional proprietary software, because developers involved in open source maintenance are freelancers and volunteers who are not bound by the traditional chains of command typical of hierarchical <sup>fi</sup>rms, are geographically dispersed, and lack face-to-face interaction with other developers.

## 2.3. Governance

Markus [39] de<sup>fi</sup>ned governance as the means of achieving the direction, control, and coordination of wholly or partially autonomous individuals and organizations on behalf of an open source project to which they jointly contribute. Though this de<sup>fi</sup>nition was conceptualized within an open source context, it appears to be equally applicable to software maintenance efforts at large. The basic intent of governance is to establish and consistently manage policies, procedures, and decision rights for ef<sup>fi</sup>cient and effective functioning of the members and working efforts of a community of users within and outside an organization.

Prior research on IT governance has been concentrated at the IT function level (e.g., [9,49]), rather than at the project level. Function-level governance practices are generally managed by a senior IT executive, such as a Chief Information Of<sup>fi</sup>cer, and apply across a wide range of IT activities, including operations, support, software development, and maintenance. Research in this area indicates that an IT organization's performance is positively in<sup>fl</sup>uenced by its IT governance practices [59,60]. It has been suggested that better IT governance can yield 20% higher return on assets in organizations than average governance [59].

Function-level governance is often far too abstract and removed to be of differential value in understanding why some projects are more successful than others within the same organization, and tend to obscure the subtleties surrounding project-level governance [38]. Clearly, software project managers exercise considerable discretion in tailoring governance practices to the unique needs of projects under their supervision, such as setting the rules of communication and collaboration among project members, allocation of decision rights and responsibilities, allocating resources to the project, and so forth, even in traditional, proprietary software development environments. This is more so in the case of open source software projects, where, in the absence of traditional chains of command typical of hierarchical <sup>fi</sup>rms, all of the governance takes place at project level. Prior research has examined many aspects of project management, such as change management, con<sup>fi</sup>guration management, and release management, but not how to manage developers, which are often the most critical resource in software maintenance efforts [16,45]. Given this gap in the literature, we focused our study on how to manage software developers, namely participation management and responsibility management.

Participation management is a process of overseeing and vetting who can be involved in an open source project and in what capacity [40]. Though an open source community is open, there is still a notion of membership in the core development/maintenance team based on the skill sets and experience of the volunteer programmers [13]. Individual developers often start participating as an external observer, whereby they observe ongoing discussions on mailing lists and learn about the project [29]. Some of these observers may gradually become a bug reporter, a developer, and eventually, a core developer. To be a core developer, an individual must both acquire project-speci<sup>fi</sup>c knowledge and technical skills, and earn the reputation of the community by demonstrating these skills by the way of corrective, adaptive, or perfective maintenance [8]. The progress of a given user from being an observer to a developer or core developer depends on the governance practices of the project. For example, Apache observers are allowed to work on a project for a number of months, following which their work quality is assessed, and their formal participation as a developer is determined by a consensus vote of core Apache Foundation members. The key goal of participation management is to ensure quality control of the open source software developers, since participation management can potentially restrict large and possibly unquali<sup>fi</sup>ed observers from becoming project developers or core developers. Divitini et al. [13] suggested that moving from external participation status to developer status often requires a strong political effort either directly or through the acceptance of artifacts created by that user. Participation management may be formal with explicit speci<sup>fi</sup>cation of roles and access rights, or informal without such well-de<sup>fi</sup>ned speci<sup>fi</sup>cations. Furthermore, the degree of formalization may change as a project matures with time and/or new project needs or concerns emerge.

Responsibility management refers to the allocation of responsibilities for various tasks in an open source software project among its community members. Distribution of responsibility is often associated with role division [12,34]. Usually, the initial software developer maintains a lead role and is responsible for ongoing development and distribution of open source products. The leader then delegates the responsibility of generating and advancing the software code for project maintenance to other programmers. Some members are assigned responsibility for documentation and task-speci<sup>fi</sup>c responsibilities such as <sup>fi</sup>xing bugs and new feature addition. Most open source projects use an online tracking system for assigning, managing, and tracking responsibilities for various tasks [25]. An example of such an online tracking system is SourceForge's Concurrent Versioning System (CVS), which generates reports displaying whether an issue has been assigned to a programmer, all issues assigned to a given programmer, and so forth [25]. However, not all tasks must be delegated [31]; some tasks are not assigned and left open for any community member to work on. Furthermore, programmers may sometimes opt to perform certain tasks and take responsibility for such tasks. Though assigning responsibility does not assure task completion, it does enhance the likelihood that an assigned tasks will be attended to and resolved in due time by a volunteer programmer.

## 2.4. Maintenance types

Swanson [56] categorized software maintenance activities into three types: corrective, adaptive, and perfective maintenance. Adaptive maintenance is the addition of new functionalities, features, and capabilities to existing software, to take advantage of new technology, upgrades, new requirements, or new problems. The goal is to adapt the software to changing user needs, technologies, or computing environments. Corrective maintenance seeks to remove software defects that can result from design errors, logic errors, or coding errors. Perfective maintenance involves enhancing software performance without changing functionality by improving the system's ef<sup>fi</sup>ciency, reliability, security, usability, or maintainability, often in response to user or system personnel requests.

Yuen [64] noted that the three types of maintenance tasks described above are rooted in two distinct causes, and follow two different behavioral patterns. Adaptive and perfective maintenance tasks are induced by environmental changes, such as changes in technologies or user needs, while corrective maintenance tasks are induced by product de<sup>fi</sup>ciencies. Because adaptive and perfective maintenance are both directed at product enhancement, they may be jointly labeled as “enhancive maintenance.” Furthermore, corrective maintenance tends to take more programmer effort and time than adaptive or perfective maintenance because <sup>fi</sup>xing existing bugs requires programmers to thoroughly review and understand existing source code that was presumably written by a different programmer [55]. Graves and Mockus [23] found that the effort required for corrective maintenance is about 1.8 times greater than that of a comparably sized perfective maintenance task. Subsequent software maintenance researchers have accepted the dichotomy of corrective and enhancive maintenance (e.g. [3,10,11,64]), and hence, this revised typology of software maintenance is employed in this study.

Some research works have also mentioned preventive maintenance as a fourth type of software maintenance. Preventive maintenance was, however, not included in our study as (i) preventive maintenance tasks account for less than 4% of the total maintenance tasks, and (ii) the original three maintenance types can be considered to be “mutually exclusive and exhaustive” [36].

Finally, it is important to note that though prior studies have distinguished between different types of software maintenance tasks, none have attempted to examine the differential impacts of these tasks on maintenance outcomes. These differential impacts are developed further in the next section, while our proposed research model is summarized in Fig. 1.

## 2.5. Hypotheses

In open source software projects, whenever a new bug is reported or a new feature is requested by a member of the user community, depending upon the governance practices of that project, the task to ful<sup>fi</sup>ll the request is either delegated to one particular (set of) developer(s) or not delegated to anyone in particular. In the latter instance, the responsibility for software maintenance is left open for anyone or everyone in the community to accept. This example of not assigning formal responsibilities to maintenance tasks can be referred to as open responsibility, while formal delegation of responsibility can be termed as delegated responsibility. It is important to note that irrespective of responsibility allocation, given the voluntary nature of contribution in open source projects, programmers have complete freedom to decide how much effort to invest in an assigned or nonassigned maintenance task.

Dymo [15] noted that most open source developers prefer to work on enhancive (adaptive or perfective) maintenance, rather than corrective maintenance. These <sup>fi</sup>ndings were also supported by [43]. Enhancive maintenance is more attractive to open source programmers as it brings more visibility in the open source community, and it demands less time and resources compared to corrective maintenance, which requires debugging and understanding the source code written by someone else [15,23,55]. Hence, in the case of open responsibility, open source participants tend to focus their attention on new additions and enhancements compared to correcting errors in the existing source code. In the absence of delegated responsibility, it is possible that more than one individual may work on the same enhancive maintenance task. Because the person completing the task <sup>fi</sup>rst gets all of the credit in terms of personal grati<sup>fi</sup>cation and peer recognition, programmers attempting enhancive maintenance are motivated to complete their tasks as quickly as possible. Reputation gained from task completion may eventually translate into developer or core developer status in the project or create additional opportunities for the programmer beyond the con<sup>fi</sup>nes of the open source project [52]. Therefore, open source projects that adhere to open responsibility practices are expected to experience higher productivity in the completion of enhancive maintenance tasks.

![](/api/attachments/DWKWSKRP/fulltext/images/c7096f8ebc3a11acb00ea1e92c9844cfc4b95c0f9b188b59b3d9b1530e5899b0.jpg)  
Fig. 1. Research model.

In contrast, we propose that open source programmers with delegated responsibility will be more productive in the performance of corrective maintenance tasks. Given the higher level of projectspeci<sup>fi</sup>c knowledge and programming skills needed to complete corrective maintenance tasks [23], such tasks are generally delegated to senior or more experienced developers. However, once delegated to a speci<sup>fi</sup>c corrective task, developers have an incentive to complete it quickly because an irresponsible act of not completing the assigned task in the timely manner can have negative consequences for the programmers' reputation, and in the worst case, can eventually lead to loss of developer status or exclusion from developer status [40]. Hence, open source software projects that delegate responsibility tend to exhibit higher developer productivity for corrective maintenance tasks. Based on the above arguments, we propose the following hypotheses:

H1. Developers' productivity for enhancive maintenance tasks for an open source project is positively (negatively) associated with the degree of delegated (open) responsibility of that project.

H2. Developers' productivity for corrective maintenance tasks for an open source project is positively (negatively) associated with the degree of open (delegated) responsibility of that project.

Just as delegation of responsibility may have differential effects on software maintenance outcomes depending on the nature of the maintenance task, similar effects can be inferred for participation management. As noted before, programmers participate in open source software projects in various capacities: as observers, bug reporters, developers, or core developers. As participants transition from observer to core developer status, they perform various activities, such as identifying bugs, requesting new features, <sup>fi</sup>xing bugs, developing software patches, and also general tasks, such as web site maintenance and release management. Engaging in such activities allows participants to build relationships and trust with other community members and gain familiarity and expertise with the software project. If these programmers are able to demonstrate their software maintenance expertise by contributing meaningfully to the open source project, they are often recognized as “registered developers” of that project [18,29]. The notion of registered developers is interesting because some open source projects restrict code contributions to registered developers only, who can then go on to become core developers, while others are open to contributions from the entire community at large. Based on these two participation management styles, we classify community members who are registered as a developer for a given project as internal participants, and the others (who are not registered) as external participants.

Whether or not an open source participant is an internal or external participant has important rami<sup>fi</sup>cations for efforts invested in corrective and enhancive maintenance tasks, and the outcomes of those efforts. By virtue of their more immersive experience with a project, internal participants tend to be more familiarized with the inner workings of a software project than external participants. Consequently, internal participants will take less time to complete a corrective maintenance task, which requires thorough understanding of the source code, than would external participants. Hence, open source projects with higher level of internal participation should exhibit higher programmer productivity in the completion of corrective maintenance tasks.

On the other hand, enhancive maintenance tasks, which bring more visibility within the open source community, become the priority of external participants targeting to become internal participants of the software project. In order to gain recognition from other members of the project, external participants attempt to complete the tasks as quickly as possible, which translates into higher level of productivity for enhancive maintenance tasks. Based on these arguments, we propose the following hypotheses:

H3. Developers' productivity for the enhancive maintenance tasks for an open source project is positively (negatively) associated with the degree of external (internal) participation in that project.

H4. Developers' productivity for the corrective maintenance tasks for an open source project is positively (negatively) associated with the degree of internal (external) participation in that project.

In the four hypotheses described above, we suggest that open versus delegated responsibility and internal versus external participation are not dichotomies, but rather bipolar ends of continuous scales. It is possible for open source software projects to have mixed responsibility and participation, or more of one type of governance than another. Whether or not those projects exhibit performance improvement in software maintenance tasks, depends on the relative proportion of community programmers with open versus delegated responsibility, or internal versus external participation. Furthermore, just as a community participant may transition from being an observer to a developer or core developer, transitions can also occur in the reverse direction. For example, a core developer may resign and become an observer instead or even leave the project entirely, due to other commitments or con<sup>fl</sup>icts with core developers or the project team. Such reverse transitions are generally idiosyncratic, are based on personal circumstances, and are therefore excluded from consideration in this study.

## 3. Empirical study

## 3.1. Methods

Empirical data for testing the hypotheses described above was collected from SourceForge — the primary hosting site for open source projects on the Internet, currently hosting about 90% of all open source projects. For each project, SourceForge provides a webpage with description of the software, links to its download page and pages offering detailed information, a history of the project's releases, and logs of maintenance activities. Despite concerns regarding the collection and maintenance of the SourceForge data, this data has previously been used in prior research on open source software (e.g., [24,50,58]). For this study, we used projects that were registered at SourceForge prior to the year 2006. Restricting our analysis to projects registered before 2006 allowed us the opportunity to examine at least two years of maintenance activities for these projects, by examining all reported bugs and requested features for these projects during the years 2006 and 2007. Several sampling strategies were employed to control for the possible extraneous effects of confounding variables and to increase the internal validity of our <sup>fi</sup>ndings. We attempted to improve the homogeneity of data in our sample by restricting our observations to projects that were targeted to either end users or developers, written wholly or partially using the C++ programming language, and those designed for the Microsoft Windows operating system. Prior <sup>fi</sup>ndings report that coders' choice of programming language in<sup>fl</sup>uences program size [30] and program complexity [62], and hence code written in different programming languages are not directly comparable. Software written in “low” level programming languages tend to have more lines of code and take longer to understand, correct, or extend than those written in “high” level languages. Likewise, programming efforts tend to vary with the operating system of the project. We chose the Windows operating system because of its widespread deployment and popularity and because of the large number of open source projects directed at this computing platform.

After preparing a list of the projects, we developed a web crawler to download the HTML <sup>fi</sup>les, including the log <sup>fi</sup>les from the versioning system and bug tracking <sup>fi</sup>les, containing registration information as well as the maintenance data for all the projects. From the downloaded <sup>fi</sup>les, we extracted various data elements such as the date on which a bug is submitted, date on which the bug was <sup>fi</sup>xed, identi<sup>fi</sup>cation of which programmer <sup>fi</sup>xed the bug, and so forth. While examining our selected open source projects, we noticed that several of the projects had a small number of bug reports and feature requests and a few projects even had zero maintenance requests. Also, the bug reports and feature requests for some projects were not closed by the end of 2007. Too few maintenance requests or open requests for these projects could be due to a systematic reason such as lack of user interest, which may contribute to less coder motivation for software maintenance. To avoid any potential biasing effects of such problems, we further restricted our sample to only those projects that had (i) at least 10 bug reports and/or feature requests, and (ii) more than 90% of the bugs and feature requests closed at the time of study. Finally, because not all projects allowed public access to maintenance tracking data, our sample was limited to those projects for which maintenance data were publicly available in SourceForge's maintenance tracking system — the Concurrent Versioning System (CVS). The above selection criteria led to a <sup>fi</sup>nal sample size of 352 projects.

## 3.2. Measures

Prior studies on proprietary software maintenance have typically conceptualized performance in terms of outcomes such as whether the budget, schedule, and functionality goals of the project were met [28]. However, such measures are of little value for open source software projects because these projects typically have no a priori budget, schedule, or prede<sup>fi</sup>ned requirements. Likewise, other software engineering metrics such as post release defect rates or conformance to quality standards may only be applied toward the end of the systems development life cycle, in contrast to open source projects where demonstrating incremental performance outcomes during the earlier stages is important because many projects end before delivering a <sup>fi</sup>nished product. Evaluating only those projects that have reached a steady state would introduce a signi<sup>fi</sup>cant selection bias and inhibit understanding of how some projects are able to reach that steady state.

Mockus et al. [44] suggest using responses to modi<sup>fi</sup>cation requests as indicators of work accomplishment in open source software studies, and have done so successfully for Apache and Mozilla software. Following this work, we operationalize maintenance productivity as time taken to complete corrective (CorrectiveTime) or enhancive (EnhanciveTime) maintenance tasks for open source projects. This variable was measured as the total number of days logged on SourceForge to complete projects' maintenance tasks. The longer it takes to complete a maintenance task; the lower is the maintenance productivity. The number of days was viewed as an appropriate measure, because personnel time is the most expensive and scarce resource in software maintenance [22], and in traditional software maintenance, clients are charged by the amount of time spent on their projects. For corrective maintenance, we recorded the time at which a bug was reported to SourceForge's bug tracking system, and the time at which the bug was reported as closed or <sup>fi</sup>xed. The time taken to complete corrective maintenance tasks, CorrectiveTime, was then computed as the average number of days taken to <sup>fi</sup>x reported bugs in that open source project. Likewise, the time taken to complete enhancive maintenance tasks, EnhanciveTime, was calculated as the average number of days taken to add requested features for that project since the date of that request.

For our responsibility management construct, we calculated the variable OpenResponsibility as the fraction of the number of tasks not assigned to any programmer over the total number of tasks listed during the time frame of interest. DelegatedResponsibility, representing the fraction of the number of tasks assigned to a speci<sup>fi</sup>c community programmer over the total number of tasks listed, was measured as the additive inverse of OpenResponsibility.

For participation management, we computed the variable InternalParticipation as the fraction of the number of internal participants over the total number of participants that contributed to that project. Participants were considered internal if they were registered as a developer for a given project. ExternalParticipation, representing the fraction of the number of external participants of a project to the total number of participants, was measured as the additive inverse of InternalParticipation.

## 3.3. Control variables

## 3.3.1. Project age

The age of an open source project may be indicative of the legitimacy and popularity of the software. Popular software attract more developers and hence, older software tend to have higher number of contributions from their community members. A project's age was measured as the number of months since the project's inception at SourceForge at the time of data collection.

## 3.3.2. Project size

Larger software is likely to experience more bugs or feature requests than smaller software, as larger software embeds more functionalities and features that are subject to change. Hence, larger software also tend to have more errors. To control for the possible effects of project size, this variable was captured by the number of lines of code (in C++).

## 3.3.3. Installed base

Raymond [48] suggests that open source software projects leverage the law of large numbers for bug identi<sup>fi</sup>cation and <sup>fi</sup>xing. Given enough eyeballs, all bugs are shallow. A large user base for certain open source software such as Linux or Apache implies that the software will be implemented and tested in numerous different environments. Such testing will lead to surfacing of more bugs, which can then be communicated to the developers or core developers for correction. Projects with a smaller installed user base are less likely to identify and rectify software bugs. Since our dataset comprised software of varying installed base, to isolate the possible effect of this variable on maintenance outcomes, the number of cumulative downloads, InstBase, was used as a control variable.

## 3.3.4. Project sponsorship

While programmers in proprietary software projects work primarily for monetary compensation, those in open source projects work for indirect bene<sup>fi</sup>ts such as personal grati<sup>fi</sup>cation, community reputation, and expertise signaling. However, an increasing number of open source projects are now receiving monetary donations from organizations and users. Although some projects choose to allocate part or all of the incoming donations to SourceForge, other projects use this monetary support to compensate maintenance efforts and/or recruit key personnel or resources that are necessary for project continuation. Programmers receiving monetary bene<sup>fi</sup>ts in open source projects are likely to have stronger incentive to devote extra time and effort into their maintenance efforts. To control for the potential effect of project sponsorship, we tabulated AcceptSponsors as a dummy variable denoting whether a project accepted external funds or paid personnel time from industry sponsors (1 if yes, and 0 otherwise).

## 3.3.5. Project maturity

The developmental stage or maturity of a project may also in<sup>fl</sup>uence its maintenance efforts. Projects in the early stages of development tend to have more undetected errors than those in the late stages, which would require more maintenance on the part of its community members. Since our sample included projects at different stages of development, we employed DevStatus as a control variable to isolate this effect. DevStatus, determined by the developer in charge of SourceForge projects, is assigned a value from 1 to 6, depending on whether the focal project is in the planning, pre-alpha, alpha, beta, production/stable, or mature stage of development respectively. A larger value is indicative of a more mature project.

## 4. Model estimation and results

## 4.1. Statistical assumptions

Our four hypotheses of interest were tested via linear regression analysis performed using the PASW/SPSS 18.0 software. Regression analysis requires data to be normally distributed, error terms to have constant variance (homoscedascity), and error terms to be uncorrelated (no multicollinearity). Initial investigations indicated that the dependent variable and many of the independent variables were not normally distributed, in which case, linear regression analysis might yield biased and non interpretable parameter estimates. Therefore, as suggested by Gelman and Hill [19], logarithmic transformations were performed on the non-normally distributed dependent and independent variables. It may also be noted that re<sup>fl</sup>ected logarithmic transformations<sup>1</sup> were performed on external participation and delegated responsibility as these two variables exhibited negative skew. Log transformed variables are represented by a pre<sup>fi</sup>x ‘ln’ and re<sup>fl</sup>ected log transformed variables by ‘rln’ in front of the variable name in the regression equations that follow. Following log transformations, the normality of the variables were con<sup>fi</sup>rmed graphically by using residual plots of the transformed variables. A non-signi<sup>fi</sup>cant p-value for Kolmogorov–Smirnov test for all the models con<sup>fi</sup>rmed the normal distributions of error terms.

The homoscedasticty assumption was tested using White test. All the models con<sup>fi</sup>rmed $\mathrm { \bar { n } ^ { * } R ^ { 2 } } < \mathrm { \bar { \chi } } ^ { 2 }$ implying homoscedasticity. Homoscedasticity was also con<sup>fi</sup>rmed using hettest command in Stata. The non-signi<sup>fi</sup>cant p-value for all the models con<sup>fi</sup>rmed that the error variances are all equal. Lastly, mulitcollinearity was tested by computing the Variance In<sup>fl</sup>ation Factor (VIF). The VIF values for the different variables in the regression analyses are reported in Table 1, and in no case exceed 1.196, which are below the recommended value of 10 [53]. Condition index also con<sup>fi</sup>rmed the absence of any concerns of multicollinearity. Tables 1 and 2 show the summary statistics of the data.

## 4.2. Model estimation and results

For the dependent measure, EnhanciveTime, the impacts of open responsibility (Hypothesis H1) and external participation (Hypothesis H3) were examined by estimating the parameters in the following regression models:

Descriptive statistics of key variables (n = 352).

<table><tr><td>Variable</td><td>Min</td><td>Mean</td><td>Max</td><td>Std dev</td></tr><tr><td>Enhancive time $^{a}$ </td><td>1.039</td><td>2.910</td><td>5.043</td><td>0.953</td></tr><tr><td>Corrective time $^{a}$ </td><td>1.079</td><td>2.804</td><td>4.934</td><td>0.884</td></tr><tr><td>Open responsibility $^{a}$ </td><td>0.000</td><td>0.293</td><td>0.680</td><td>0.193</td></tr><tr><td>Delegated responsibility $^{b}$ </td><td>1.000</td><td>1.386</td><td>1.680</td><td>0.193</td></tr><tr><td>Internal participation $^{a}$ </td><td>0.000</td><td>0.435</td><td>0.660</td><td>0.135</td></tr><tr><td>External participation $^{b}$ </td><td>1.000</td><td>1.229</td><td>1.660</td><td>0.135</td></tr><tr><td>Project age</td><td>156.0</td><td>1009.5</td><td>1800</td><td>344.5</td></tr><tr><td>Project size $^{a}$ </td><td>7.510</td><td>9.316</td><td>12.65</td><td>1.168</td></tr><tr><td>Installed base $^{a}$ </td><td>1.100</td><td>6.065</td><td>10.97</td><td>1.670</td></tr><tr><td>Sponsorship</td><td>0.000</td><td>0.193</td><td>1.000</td><td>0.395</td></tr><tr><td>Project maturity</td><td>1.000</td><td>3.665</td><td>6.000</td><td>1.470</td></tr></table>

<sup>a</sup> Natural log transformed variables.  
b Re<sup>fl</sup>ected natural log transformed variables.

Model 1 (H1).

$$
\begin{array}{c} \text {InEnhanciveTime} = a + \beta_ {1} \text {InOpenResponsibility} + \beta_ {3} \text {Age} + \beta_ {4} \text {InSize} \\ + \beta_ {5} \text {InInstBase} + \beta_ {6} \text {AcceptSponsor} + \beta_ {7} \text {DevStatus} \end{array}
$$

Model 3 (H3).

$$
\begin{array}{c} \text {InEnhanciveTime} = a + \beta_ {2} r \text {InExternalParticipation} + \beta_ {3} A g e + \beta_ {4} \text {InSize} \\ + \beta_ {5} \text {InInstBase} + \beta_ {6} \text {AcceptSponsor} + \beta_ {7} \text {DevStatus} \end{array}
$$

Both Models 1 and 3 show good <sup>fi</sup>t with the data (F=7.202, $\mathtt { p } { < } 0 . 0 1 ; \ \mathtt { F } = 7 . 3 4 4 , \ \mathtt { p } { < } 0 . 0 1 ;$ ). Negative and signi<sup>fi</sup>cant estimates of parameters $\beta _ { 1 }$ and $\beta _ { 2 }$ indicate that the average time to perform enhancive maintenance tasks decreases as open responsibility and external participation increase. The standardized parameter estimates for external participation and open responsibility were −0.109 and −0.101, which were both signi<sup>fi</sup>cant at the 0.05 signi<sup>fi</sup>cance level. These <sup>fi</sup>ndings provide empirical support for our Hypotheses H1 and H3 respectively. Among our control variables, project sponsorship and installed base had signi<sup>fi</sup>cant effects on enhancive maintenance performance in both Models 1 and 3, while project size had signi<sup>fi</sup>cant effect in Model 3 only. We also conducted analysis on the effects of the control variables alone (as a base model), and compared that model with the corresponding regression models. Change in F-statistics con<sup>fi</sup>rmed that the main variable of interest, open responsibility and external participation, contributed signi<sup>fi</sup>cantly over the base model. The results of the regression models and the F-statistics are shown in Table 3.

For the dependent measure, CorrectiveTime, the impacts of delegated responsibility and internal participation were estimated using the following regression models:

Model 2 (H2).

$$
\begin{array}{l} \text {InCorrectiveTime} = a + \beta_ {1} r \text {InDelegatedResponsibility} + \beta_ {3} A g e \\ \quad + \beta_ {4} \text {InSize} + \beta_ {5} \text {InInstBase} + \beta_ {6} A c c e p t S p o n s o r \\ \quad + \beta_ {7} D e v S t a t u s \end{array}
$$

Model 4 (H4).

$$
\begin{array}{c} \text {InCorrectiveTime} = a + \beta_ {2} \text {InInternalParticipation} + \beta_ {3} \text {Age} + \beta_ {4} \text {InSize} \\ + \beta_ {5} \text {InInstBase} + \beta_ {6} \text {AcceptSponsor} + \beta_ {7} \text {DevStatus} \end{array}
$$

Both Models 2 and 4 show good <sup>fi</sup>t with the data $( \mathrm { F } = 9 . 4 0 0 ,$ $\mathrm { p } { < } 0 . 0 1 ; \ \mathrm { F } = 8 . 7 7 8 , \ \mathrm { p } { < } 0 . 0 1 )$ ). Negative and signi<sup>fi</sup>cant estimates of parameters $\beta _ { 1 }$ and $\beta _ { 2 }$ indicate that the average time to perform corrective maintenance tasks decreases with increasing delegated responsibility and internal participation. The standardized estimate of beta coef<sup>fi</sup>cient for delegated responsibility −0.125 was signi<sup>fi</sup>cant at the 0.05 level, while the beta coef<sup>fi</sup>cient of −0.091 for internal participation was insigni<sup>fi</sup>cant at the 0.05 level. Hence, Hypothesis H2 was validated using our data sample, but Hypothesis H4 was not. Among the control variables, only project sponsorship had a signi<sup>fi</sup>cant effect on corrective maintenance performance in Models 2 and 4. Change in F-statistics also showed similar results.

To test for the robustness of our <sup>fi</sup>ndings, we re-estimated maintenance times after deleting two in<sup>fl</sup>uential observations identi<sup>fi</sup>ed using the Belsley–Kuh–Welsch [6] criteria. The sign and signi<sup>fi</sup>cance of the beta estimates in the revised regression are not signi<sup>fi</sup>cantly different from those in the original model. Our results hold good even for a conservative Belsley–Kuh–Welsch criteria of deleting ten in<sup>fl</sup>uential observations. Additionally, we recomputed the beta estimates using robust estimation in Stata 11.1. Both analyses con<sup>fi</sup>rmed that the results reported in our original regression analysis were indeed robust.

## 4.3. Limitations

The <sup>fi</sup>ndings of our study should be interpreted in light of its limitations. The <sup>fi</sup>rst limitation is our sole focus on the developer management dimension of project governance practices in terms of participation and responsibility management. In light of our narrow focus, our <sup>fi</sup>ndings may be generalized only to instances of developer management in open source and proprietary software development, but not to other aspects of project governance.

The second limitation of our study is our reliance on SourceForge data. SourceForge provides the largest publicly available database of open source projects, but the utility of the metrics collected in its concurrent versioning system, as well as how consistently these metrics are computed across different open source projects maintained by different groups of core developers may be questionable. We attempted to alleviate this concern by relying solely on objective measures, such as number of days between bug reporting and bug <sup>fi</sup>xing and proportion of maintenance tasks with open versus delegated responsibility, for our analysis. Furthermore, while we had a large enough sample size to ensure statistical validity, a still larger sample size might have increased the statistical power to detect the marginal effects reported in this study.

Correlation matrix for corrective data.

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Delegated responsibilitya(1)</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Internal participationb(2)</td><td>-0.082</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Project ageb(3)</td><td>-0.027</td><td>-0.113</td><td>1.000</td><td></td><td></td><td></td><td></td></tr><tr><td>Sponsorshipb(4)</td><td>-0.001</td><td>-0.115</td><td>-0.045</td><td>1.000</td><td></td><td></td><td></td></tr><tr><td>Project maturityb(5)</td><td>-0.046</td><td>0.089</td><td>-0.097</td><td>0.033</td><td>1.000</td><td></td><td></td></tr><tr><td>Project sizeb(6)</td><td>0.029</td><td>-0.217</td><td>0.199</td><td>-0.117</td><td>-0.074</td><td>1.000</td><td></td></tr><tr><td>Installed baseb(7)</td><td>0.050</td><td>-0.213</td><td>0.320</td><td>0.048</td><td>-0.178</td><td>0.191</td><td>1.000</td></tr></table>

<sup>a</sup> Re<sup>fl</sup>ected natural log transformed variables.  
b Natural log transformed variables.

Table 3 Regression results.

<table><tr><td rowspan="2">Parameters</td><td colspan="3">Model 1: enhancive Hypothesis H1</td><td colspan="3">Model 2: corrective Hypothesis H2</td><td colspan="3">Model 3: enhancive Hypothesis H3</td><td colspan="3">Model 4: corrective Hypothesis H4</td></tr><tr><td> $\beta$ </td><td>Sig.</td><td>VIF</td><td> $\beta$ </td><td>Sig.</td><td>VIF</td><td> $\beta$ </td><td>Sig.</td><td>VIF</td><td> $\beta$ </td><td>Sig.</td><td>VIF</td></tr><tr><td>Open respon</td><td>-0.101</td><td>0.046*</td><td>1.01</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Delegated respon</td><td></td><td></td><td></td><td>-0.125</td><td>0.013*</td><td>1.01</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Ext. participation</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-0.109</td><td>0.042*</td><td>1.07</td><td></td><td></td><td></td></tr><tr><td>Int. participation</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-0.091</td><td>0.065</td><td>1.11</td></tr><tr><td>Project age</td><td>0.031</td><td>0.574</td><td>1.15</td><td>0.033</td><td>0.534</td><td>1.15</td><td>0.028</td><td>0.600</td><td>1.14</td><td>0.037</td><td>0.485</td><td>1.14</td></tr><tr><td>Project size</td><td>0.100</td><td>0.059</td><td>1.08</td><td>0.091</td><td>0.079</td><td>1.08</td><td>0.123</td><td>0.022*</td><td>1.12</td><td>0.070</td><td>0.185</td><td>1.12</td></tr><tr><td>Installed base</td><td>-0.158</td><td>0.004*</td><td>1.17</td><td>-0.085</td><td>0.118</td><td>1.08</td><td>-0.136</td><td>0.014*</td><td>1.20</td><td>0.106</td><td>0.055</td><td>1.20</td></tr><tr><td>Sponsorship</td><td>-0.249</td><td>0.001*</td><td>1.02</td><td>-0.309</td><td>0.001*</td><td>1.02</td><td>-0.235</td><td>0.001*</td><td>1.04</td><td>-0.321</td><td>0.001*</td><td>1.04</td></tr><tr><td>Project maturity</td><td>-0.061</td><td>0.237</td><td>1.04</td><td>-0.075</td><td>0.141</td><td>1.04</td><td>-0.070</td><td>0.174</td><td>1.04</td><td>-0.066</td><td>0.201</td><td>1.04</td></tr><tr><td>Model F-statistic</td><td>7.20</td><td>0.001</td><td></td><td>9.40</td><td>0.001</td><td></td><td>7.34</td><td>0.001</td><td></td><td>8.78</td><td>0.001</td><td></td></tr><tr><td>F-changea</td><td>3.99</td><td>0.046*</td><td></td><td>6.25</td><td>0.013*</td><td></td><td>4.16</td><td>0.042*</td><td></td><td>2.98</td><td>0.085</td><td></td></tr></table>

<sup>a</sup> Change over base model (with only control variables in the model).  
\* Signi<sup>fi</sup>cant at the 0.05 level.

Third, duplication in bug reports and feature requests have been reported as a concern for open source projects as well as data validity for statistical testing [7,61]. However, SourceForge's concurrent versioning systems and bug tracking systems help bug reporters minimize this duplication. Additionally, we carefully inspected our data for keywords such as ‘duplicate’, ‘rejected’, and ‘invalid’ in the report status and excluded such data from our analysis [7,61].

Fourth, it should be noted that some of the maintenance requests were not completed, and some of the projects had too little maintenance requests indicating low user interest. This is a typical problem with open source projects given the open ended nature of such projects and the voluntary nature of their usage and developer contributions. To minimize this concern, we selected only those projects that had at least 10 maintenance requests and had at least 90% of those request closed at the time of study. We selected 10 requests as our threshold, because we felt that at least 10 such requests will be indicative of a relatively mature project. Further, most SourceForge projects are small and of limited scope. If we increased the minimum bug count to 20, our sample size would shrink considerably since many of the smaller projects will fall out of the sample, decreasing the statistical power of our analysis.

Fifth, we investigated how only participation management and responsibility management effect developers' performance. There could be other factors, such as severity of bugs and complexity of projects, which may in<sup>fl</sup>uence developers' motivations, and, in turn, performance, to <sup>fi</sup>x bugs.

Sixth, we used a combination of adaptive and perfective maintenance as enhancive maintenance. Though there is a valid reason and precedence for such combination [64], it is also possible that adaptive and perfective maintenance may demonstrate signi<sup>fi</sup>cantly different patterns that may have been obfuscated by combining the two maintenance types.

## 5. Discussion and implications

This study employed data from 352 open source software projects to analyze the impact of governance practices on software maintenance performance (de<sup>fi</sup>ned in terms of the time taken to complete maintenance tasks). The two governance practices investigated are participation and responsibility management, with participation management operationalized along a continuum from internal to external participation, and responsibility management operationalized from open to delegated responsibility. In this section, we provide answers to our three research questions, and describe our key <sup>fi</sup>ndings and their implications for open source software maintenance research and practice.

Our empirical <sup>fi</sup>ndings con<sup>fi</sup>rm our theoretical expectations that the time taken to perform enhancive (adaptive and perfective) maintenance decreases as the degree of open responsibility increases, while the time taken for corrective maintenance decreases as the degree of delegated responsibility increases.

For the effect of participation, although the decrease in time taken for enhancive tasks was signi<sup>fi</sup>cant at the 0.05 level, the decrease in time for corrective tasks was not signi<sup>fi</sup>cant at the 0.05 level. The meritocratic philosophy of open source software projects may be the rationale for the signi<sup>fi</sup>cant impact of external participation. External participants, who want to join a project's core development team, have a strong motivation to complete maintenance tasks as quickly as possible in order to gain the attention and acceptance of the core development team. More challenging enhancements attract more attention among programmers because completing technically critical tasks are viewed as high value contributions by the open source community, and higher as the reputational rewards in terms of peer recognition and attention from core developers. Dymo [15] noticed that developers tend to work more on enhancive maintenance tasks as such tasks that bring more visibility, which, in turn, are correlated with higher reputation rewards. The net effect of this competitive phenomenon leads to shorter turnaround time for enhancive maintenance.

On the other hand, internal participation was not found to be signi<sup>fi</sup>cant in explaining the time taken for corrective maintenance tasks. It could be argued that these tasks tend to be of lower visibility and are often performed by a small number of core developers [32,44]. This small group of developers often tends to get overloaded with requests for bug <sup>fi</sup>xes, causing overall delay in corrective maintenance tasks.

With respect to answering our three research questions, our <sup>fi</sup>ndings show that both participation management and responsibility management impact developers' productivity for maintenance tasks. As discussed above, our <sup>fi</sup>ndings also show that these impacts vary across the different types of maintenance tasks.

The effects of control variables in our study present some interesting and unexpected <sup>fi</sup>ndings. For instance, project sponsorship had a strong effect on the time taken to complete both corrective and enhancive maintenance tasks. Installed base (number of downloads) had signi<sup>fi</sup>cant effects on the time taken for enhancive tasks but not for corrective tasks. Furthermore, project size was found to have signi<sup>fi</sup>cant effects for only Model 3 of enhancive maintenance tasks.

Open source projects receiving money from corporate or individual sponsors increase programmers' rewards on maintenance outcomes either directly in the form of monetary compensation or indirectly, by sustaining the life of an open source project and consequently programmers' reputation in that community. Consequently, sponsored open source projects attract more programmer attention and consume less time in maintenance tasks. Henkel [27] observed a similar relationship between external sponsorship and development of Linux applications, especially given that many contributors to Linux projects are salaried or contract developers employed by commercial <sup>fi</sup>rms interested in the Linux platform. Sponsored open source projects are somewhat close to proprietary projects, and hence, our understanding of monetary incentives as motivators in proprietary projects may therefore be extended to sponsored open source projects. Many commercial software manufacturers are realizing this, with Google Summer of Code using sponsorship to attract volunteer programmers to build Google applications (http://code.google.com/soc/2008). Programmers participating in this project can also advertise their skills to Google, a potential employer. However, the success of the program is yet to be determined.

It is often argued that program size is strongly correlated to its maintenance efforts, leading to multicollinearity concerns. We tested for multicollinearity by computing variance in<sup>fl</sup>ation factors, which were found to be within permissible limits, suggesting that multicollinearity was possibly not a signi<sup>fi</sup>cant problem in our study. Project size had a signi<sup>fi</sup>cant impact on the time required for enhancive tasks at the 0.05 level in Model 3 and had an insigni<sup>fi</sup>cant impact in Model 1. The impact of project size was found to be insigni<sup>fi</sup>cant for both the models for corrective tasks. Mockus et al. [44] suggest that majority of the corrective tasks are performed by core developers. In order for a programmer to become a core developer, the programmer had to work his way up by gaining experience and trust of the other project members by demonstrating his skills and project-speci<sup>fi</sup>c knowledge. By the time the programmer becomes a core developer, he is very familiar with the project, which may explain why project size no longer has a signi<sup>fi</sup>cant impact on their ability to complete corrective tasks.

## 5.1. Implications

This study makes important implications for software maintenance literature and practice. To the best of our knowledge, this is the <sup>fi</sup>rst study to investigate the impact of developer management practices of project governance on software maintenance outcomes. Strong empirical support for our hypothesized relationships suggests that developer management is indeed important for software maintenance projects, particularly for open source projects that tend to have less rigorous governance practices compared to proprietary software projects. We demonstrate that responsibility management and participation management in<sup>fl</sup>uence the outcome of software maintenance tasks, and more interestingly, have differential impacts depending on whether the task involves corrective or enhancive maintenance. These <sup>fi</sup>ndings have at least three immediate implications for open source software project managers. First, they must delegate responsibility to improve software maintenance performance, and more so, if the maintenance is corrective in nature. Enhancive tasks are completed in lesser time when the responsibility is not assigned to anyone, whereas the corrective tasks take lesser time when the responsibility is delegated. Second, project managers should solicit more external participation from programmers of other projects, which may help improve the performance of enhancive maintenance tasks. Third, they should encourage more internal participation among programmers in order to improve the turnaround time for corrective maintenance tasks.

Lastly, though we examined time taken to complete maintenance tasks as a measure of maintenance performance, it also has interesting implications for software quality research. Number of bugs in a software project is a commonly used measure of software quality. However, the time taken to <sup>fi</sup>x a bug is also indicative of software quality. Well designed software should theoretically take less time to correct bugs. Hence, it is possible that participation and responsibility management may also help improve software quality. We leave such investigation as an option for future research.

## Acknowledgment

The work of the second author was partially supported by Sogang Business School's World Class University Program (R1-20002) funded by the Korea Research Foundation.

## References

[1] Y. Ahn, J. Suh, S. Kim, H. Kim, The software maintenance project effort estimation model based on function points, Journal of Software Maintenance and Evolution: Research and Practice 15 (2003) 71–85.

[2] D. Andrews, N. Leventhal, Fusion: Integrating IE, CASE and JAD: A Handbook for Reengineering Systems Organizations, Prentice Hall, 1993.

[3] R.K. Bandi, V.K. Vaishnavi, D.E. Turk, Predicting maintenance performance using object-oriented design complexity metrics, IEEE Transactions on Software Engineering 29 (1) (Jan. 2003) 77–87.

[4] L. Baresi, S. Morasca, Three empirical studies on estimating the design effort of web applications, ACM Transactions on Software Engineering and Methodology 16 (4).(September 2007).15

[5] L. Belady, M.M. Lehman, An introduction to program growth dynamics, Statistical Computer Performance Evaluation, Academic Press, New York NY, 1972, pp. 503–511.

[6] D.A. Belsley, E. Kuh, R.E. Welsch, Regression Diagnostics, John Wiley and Sons, New York, 1980.

[7] N. Bettenburg, R. Premraj, T. Zimmermann, S. Kim, Duplicate bug reports considered harmful. Really? ICSM '08: Proceedings of the 24th IEEE International Conference on Software Maintenance, September 2008.

[8] C. Bird, A. Gourley, P. Devanbu, A. Swaminathan, G. Hsu, Open borders? Immigration in open source projects, Proceedings of the Fourth International Workshop on Mining Software Repositories. 2007

[9] C.V. Brown, Examining the emergence of hybrid IS governance solutions: evidence from a single case site, Information Systems Research 8 (1) (1997) 69–94.

[10] E. Capra, Chiara Francalanci, Francesco Merlo, An empirical study on the relationship between software design quality, development effort and governance in open source projects, IEEE Transactions on Software Engineering 34 (6) (Nov/Dec 2008) 765–782.

[11] T. Chan, S. Chung, T.H. Ho, An economic model to estimate software rewriting and replacement times, IEEE Transactions on Software Engineering 22 (8) (1996) 580–598.

[12] P. de Laat, Governance of open source software: state of the art, Journal of Management and Governance 11 (2007) 165–177.

[13] M. Divitini, L. Jaccheri, E. Montiero, H. Traetteberg, Open source processes: no place for politics? In taking stock of the bazaar, Proceedings of the 3rd Workshop on Open Source Software Engineering, Portland, Oregon, 2003, pp. 39–43.

[14] J. Dvorak, Conceptual entropy and its effect on class hierarchies, IEEE Computer 27 (6) (1994) 59–63.

[15] A. Dymo, Open source software engineering, II Open Source World Conference, February 15–17 2006, Málaga.

[16] S.G. Eick, T.L. Graves, A.F. Karr, J.S. Marron, A. Mockus, Does code decay? Assessing the evidence from change management data, IEEE Transactions on Software Engineering 27 (1) (2001) 1–12.

[17] F. Fioravanti, P. Nesi, Estimation and prediction metrics for adaptive maintenance effort of object-oriented systems, IEEE Transactions on Software Engineering 27 (12) (Dec. 2001) 1062–1084.

[18] C. Gacek, B. Arief, The many meanings of open source, IEEE Software 21 (1) (2004) 34–40.

[19] A. Gelman, J. Hill, Data Analysis Using Regression and Multilevel/Hierarchical Models, Cambridge University Press, 2007.

[20] M. Ghods, K.M. Nelson, Contributors to quality during software maintenance, Decision Support Systems 23 (4) (October 1998) 361–369.

[21] R.L. Glass, R.A. Noiseux, Software Maintenance Guidebook, Prentice-Hall, 1981.

[22] G.W. Grammas, J.R. Klein, Software productivity as a strategic variable, Interfaces 15 (3) (1985) 116–126.

[23] T.L. Graves, A. Mockus, Inferring change effort from con<sup>fi</sup>guration management data, Proceedings of the Fifth International Symposium on Software Metrics, Bethesda, MD, 1998, pp. 267–273.

[24] R. Grewal, G.L. Lilien, G. Mallapragada, Location, location, location: how network embeddedness affects project success in open source systems, Management Science 52 (7) (2006) 1043–1056.

[25] C. Gutwin, R. Penner, K. Schneider, Group awareness in distributed software development, Proceedings of the ACM Conference on Computer-Supported Cooperative Work, 2004.

[26] K.L. Gwebu, J. Wang, Adoption of open source software: the role of social identi<sup>fi</sup>cation, Decision Support Systems 51 (1) (April 2011) 220–229.

[27] J. Henkel, Selective revealing in open innovation processes: the case of embedded Linux, Research Policy 35 (7) (2006) 953–969.

[28] J.A. Hoffer, J.F. George, J.S. Valacich, Modern Systems Analysis & Design, Third ed. Prentice Hall, New Jersey, 2002.

[29] C. Jensen, W. Scacchi, Role migration and advancement processes in OSSD projects: a comparative case study, Paper presented at the 29th International Conference on Software Engineering (ICSE).2007

[30] T.C. Jones, Programming Productivity, McGraw-Hill, Inc., New York, 1986.

[31] T. Koponen, V. Hotti, Open source software maintenance process framework, Proceedings of the Fifth Workshop on Open Source Software Engineering (St. Louis, Missouri, May 17–17, 2005). 5-WOSSE, ACM Press, New York, NY, 2005, pp. 1–5.

[32] S. Krishnamurthy, Cave or community? An empirical examination of 100 mature open source projects, 2002 First Monday.

[33] V.G. Kulkarni, S. Kumar, V. Mookerjee, S.P. Sethi, Optimal allocation of effort to software maintenance: a queuing theory approach, Production and Operations Management 18 (5) (2009) 506–515.

[34] C. Lattemann, S. Stieglitz, Framework for governance in open source communities, Proc. of the 38th Hawaii International Conference on Systems Sciences, 2005.

[35] G. Lawton, The great giveaway. New scientist, 2002 http://www.newscientist. com/article/mg17323284.600-the-great-giveaway.html Accessed Nov 22, 2009.

[36] B.P. Lientz, E.B. Swanson, Software Maintenance Management: A Study of the Maintenance of Computer Application Software in 487 Data Processing Organizations, Addison-Wesley Publishing Company, Reading MA, 1980.

[37] A. Lucia, E. Pompella, S. Stefanucci, Assessing effort estimation models for corrective software maintenance through empirical studies, Information and Software Technology 47 (1) (2005) 3–15.

[38] Mähring, M. 2002. IT project governance. Doctoral thesis, Economic Research Institute, Stockholm

[39] L. Markus, The governance of free/open source software projects: monolithic, multidimensional or con<sup>fi</sup>gurationally? Journal of Management and Governance 11.(2007).151-163

[40] M.L. Markus, B. Manville, C.E. Agres, What makes a virtual organization work? Sloan Management Review (2000) 13–26.

[41] T. Mens, T. Tourwe, Survey of software refactoring, IEEE Transactions on Software Engineering 30 (2004) 126–138.

[42] V. Midha, P. Palvia, Factors affecting the success of open source software, Journal of Systems and Software 85 (4) (April 2012) 895–905.

[43] V. Midha, “Does Complexity Matter? The impact of change in structural complexity on software maintenance & new developers' contributions in open source software”, ICIS 2008 Proceedings, 2008.

[44] A. Mockus, R. Fielding, J. Herbsleb, Two case studies of open source software development: Apache and Mozilla, ACM Transactions on Software Engineering and Methodology 11 (3) (2002) 309–346.

[45] L.G.P. Murta, C.M.L. Werner, J. Estublier, The con<sup>fi</sup>guration management role in collaborative software engineering, in: I. Mistrík, J. Grundy, A. Hoek, J. van der Whitehead (Eds.), Collaborative Software Engineering, Part 2, 2010, pp. 179–194.

[46] T. Pigoski, Practical Software Maintenance, Wiley computer publishing, 1997.

[47] A. Rashid, W.Y.C. Wang, D. Dorner, Gauging the differences between expectation and systems support: the managerial approach of adaptive and perfective software maintenance, 4th International Conference on Cooperation and Promotion of Information Resources in Science and Technology, 2009.

[48] E.S. Raymond, The Cathedral & the Bazaar. O'Reilly, 2001.

[49] V. Sambamurthy, R.W. Zmud, Factors in<sup>fl</sup>uencing information technology management architectures in organizations: a theory of multiple contingencies, MIS Quarterly 23 (2) (1999) 261–290.

[50] R. Sen, S.S. Singh, S. Borle, Open source software success: measures and analysis, Decision Support Systems 52 (2) (January 2012) 364–372.

[51] M. Shepperd, C. Scho<sup>fi</sup>eld, B. Kitchenham, Effort estimation using analogy, Proceedings of the 18th International Conference on Software Engineering, ACM Press, New York NY, 1996, pp. 170–178.

[52] D. Stewart, Social status in an open-source community, American Sociologica Review 70 (5) (Oct., 2005) 823–842.

[53] A. Studenmund, Using Econometrics: A Practical Guide, Harper Collins, New York, NY, 1992.

[54] C. Subramaniam, R. Sen, M.L. Nelson, Determinants of OSS project success: a longitudinal study, Decision Support Systems 46 (2) (January 2009) 576–585.

[55] M. Sullivan, R. Chillarege, Software defects and their impact on system availability — a study of <sup>fi</sup>eld failures in operating systems, Proceedings of the 1991 IEEE Symposium on Fault-Tolerant Computing (FTCS-21), 1991, (Montreal, P. Q., Canada).

[56] E.B. Swanson, The dimensions of software maintenance, Proceedings of the 2nd IEEE International Conference on Software Engineering, 1976, pp. 492–497.

[57] A. Tiwana, Governance-knowledge <sup>fi</sup>t in systems development projects, Information Systems Research 20 (2) (2009) 180–197.

[58] E. von Hippel, G. von Krogh, Open source software and the “private-collective” innovation model: issues for organization science, Organization Science 14 (2) (2003) 209–225.

[59] P. Weill, Don't just t lead, govern: how top-performing <sup>fi</sup>rms govern IT, MIS Quarterly Executive 8 (1) (2004).

[60] P. Weill, M. Broadbent, Leveraging the New Infrastructure: How Market Leaders Capitalize on IT, Harvard Business School Press, Boston, 1998

[61] C. Weiss, R. Premraj, T. Zimmermann, A. Zeller, How long will it take to <sup>fi</sup>x this bug? Proceedings of the Fourth International Workshop on Mining Software Repositories, May 20–26, 2007, p. 1.

[62] E.J. Weyuker, Evaluating software complexity measures, IEEE Transactions on Software Engineering 14 (9) (1988) 1357–1365.

[63] S. Wheeler, Open source software / free software (OSS/FS, FLOSS, or FOSS)? Look at the numbers! http://www.dwheeler.com/oss\_fs\_why.html 2007.

[64] C.H. Yuen, Differences in types of software maintenance work: an empirical study, Proceedings of the International Conference on Software Maintenances, Orlando, IEEE CS Press, 1989, pp. 106–115.

Vishal Midha is an Assistant Professor of Computer Information Systems at th University of Texas–Pan American. He received his Ph.D. in MIS from the University of North Carolina at Greensboro. His current other research interests include open source software development, information privacy concerns, and internet frauds. He has published in Communications of AIS, International Journal of Electronic Commerce, Electronic Markets, Journal of CIS, and many national and international conferences, including the International Conference of Information Systems. and Americas Conference on Information Systems. Presently, he also serves as an Associate Editor in the International Journal of Information Security and Privacy.

Anol Bhattacheriee is a professor of information systems at the University of South Florida. He has Ph.D. and MBA degrees from the University of Houston and B.S, and M.S. degrees from the Indian Institute of Technology (India). His prior research has been published in MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Decision Sciences, Decision Support Systems, IEEE Transactions of Systems, Man, and Cybernetics, Data Base, Information & Management, and several other refereed journals and conference proceedings
