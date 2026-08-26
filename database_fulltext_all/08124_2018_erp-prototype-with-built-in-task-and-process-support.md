---
otero_id: 8124
otero_key: "Y5YTHBDK"
title: "ERP prototype with built-in task and process support"
authors: "Tamara Babaian; Jennifer Xu; Wendy Lucas"
year: "2018"
journal: "European Journal of Information Systems"
doi: "10.1057/s41303-017-0060-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
RESEARCH ESSAY

# ERP prototype with built-in task and process support

Tamara Babaian, Jennifer Xu and Wendy Lucas

Bentley University, 175 Forest Street, Waltham, MA 02452, USA

Correspondence: Tamara Babaian, Bentley University, 175 Forest Street, Waltham,

MA 02452, USA

E-mail: tbabaian@bentley.edu

## Abstract

Several recent studies of ERP system interfaces have confirmed that their poor usability hinders worker productivity, despite the huge investments companies make in user training and support. Usability challenges arise from the complexity of ERP systems, which are designed as a universal tool for a plethora of organizational practices and contexts. Learning to operate within an excessively vast terrain of ERP task pages and parameters is a significant challenge for most ERP users. Our proposed solution relies on the system itself to share task and process information in order to guide users through learning and performing their business tasks with the system. This perspective arises from employing the human–computer collaboration approach to the design of user interfaces, which we apply as a guiding framework for our research. In this paper, we present two interface components for providing ERP system users with task and process guidance: Automated Playback and Interactive Process Visualization. The novelty of our approach comes from using the history of past interactions to dynamically compose animated demonstrations of task interfaces and to provide an interactive graphical map of the current process being worked on by the user.

Keywords: ERP usability; collaboration theory; dynamic and interactive visualizations

## Introduction

Mainstream enterprise resource planning (ERP) systems are difficult to master, take inordinate amounts of training (Beatty & Williams, 2006; Koh et al, 2009; Scott, 2005; Topi et al, 2005), increase anxiety levels in an already overstressed workforce (Love et al, 2007), and can stymie even the most sophisticated of users. Usage issues identified in earlier studies included unwieldy menus that hamper navigation, inadequate task support, lack of support in error situations, and outputs that are difficult to interpret (Bishu et al, 2001; Parks, 2012; Rettig, 2007; Scholtz et al, 2010; Singh & Wesson, 2009). Studies by Lambeck et al (2014a, b) have confirmed that many of these issues persist today and continue to plague ERP users long after the conversion phase and training periods have ended. Also noteworthy is that challenges in identifying and accessing the required functionality remain a problem across all levels of user experience. Overall system complexity can be damaging not only to employee morale and productivity (Iansiti, 2016; Matthews, 2016) but also to the bottom line, as incorrectly entered data flowing through an enterprise-wide system can lead to a host of operational issues (Babaian et al, 2010; Topi et al, 2006; Parks, 2012).

Despite the widespread recognition of ERP usability issues and the havoc they can wreak, there has been a profound lack of significant progress in improving upon the design of these systems. A recent Gartner report notes that ERP vendors are using social media in new product releases to enhance the user experience (Ganly & Montgomery, 2015), but such advances will not impact the usability of the system itself. Much attention has been focused on applying process mining for process discovery in enterprise systems (van der Aalst, 2011), but the aim is typically to evaluate and optimize processes rather than improve usability. There has been some headway in applying process visualizations for benefiting end user understanding (Hipp et al, 2012; Kolb & Reichert, 2013), but such approaches have not been integrated into ERP systems for interactive use.

The need for new approaches for improving the usability of ERP systems motivated the work presented here. In this paper, we present novel user interface components for supporting end users of ERP systems during system– user interaction. The two components, Automated Playback and Interactive Process Visualization, target two of the largest hurdles facing ERP users: (1) how to actually use the system to perform a specific task (for new users or experienced ones accessing an unfamiliar or infrequently used part of the system), and (2) how the tasks performed by different people are related to each other within the overall business context. The aforementioned field studies have revealed that this type of knowledge is essential for making successful use of an ERP system.

The Automated Playback component, an earlier version of which appeared in Babaian and Lucas (2012), presents users with on-demand, automated demonstrations of how to execute any task that has been previously performed with the system. This demonstration is constructed in real time based on the logged history of system–user interac tions. Automated Playback is a powerful tool for avoiding system atrophy, in which use of the system wanes due to a lack of knowledge transfer and retention concerning system usage. Furthermore, this method is much more cost- and time-effective than the typically recommended approach of avoiding declining use by delivering periodic, post-implementation training on a continual basis (Babaian et al, 2007; Norton et al, 2013).

The Interactive Process Visualization component, first introduced in Lucas et al (2013), consists of two graphbased views of the process encompassing the user’s current task: a general schema of the process (the Process Graph), and the way the current instance has been executed so far (the Process Instance Graph). Both graphs are interactive and convey additional contextual information, such as the typical order of tasks and the users and documents that are involved at each step. These visualizations also reduce the likelihood of system atrophy while diminishing the need for ongoing training by revealing how processes are implemented within the system and providing information that can be difficult to discover without considerable expertise.

This work is part of a broader research project focusing on improving the usability of enterprise systems by evaluating and reengineering the way they interact with users. The framework underlying our approach is based on the human–computer collaboration (HCC) paradigm (Grosz, 1996, 2005; Shieber, 1996; Terveen, 1995), which is grounded in the idea of creating systems that act as an effective partner to a human user rather than just a comprehensive tool. To achieve effective system–user collaboration requires addressing the demands imposed by the collaborative model of system–user interaction early on, starting from the analysis of the requirements. We have used collaboration theory (Bratman, 1992; Grosz & Kraus, 1996) as a unifying theory and a guide in all stages of this research, ranging from field studies to design principles to artifact development and evaluation methodologies (see, for example, Babaian et al, 2014, 2010; Cooprider et al, 2010; Lucas & Babaian, 2012; Topi et al, 2005).

In the next section, we discuss the current state of related work and provide background on collaboration theory. We then describe the design science-based research framework for creating ERP systems that collaborate with users. This is followed by descriptions of Automated Playback and Interactive Process Visualization. Next, we present and interpret findings from an empirical evaluation of these components. We conclude with a discussion of our research contributions and directions for future research.

## Related work

## ERP usability

The International Organization for Standardization defines usability as the extent to which a system helps a user achieve specific goals in a specific context effectively, efficiently, and with satisfaction (ISO, 1998). Designing usable software systems is one of the central research objectives of the field of human–computer interaction (HCI) (Nielsen, 1993; Sears & Jacko, 2008).

Despite their widespread adoption by organizations and enterprises around the world, ERP systems have long been criticized for poor usability (Calisir & Calisir, 2004; Hestermann, 2009; Iansiti, 2016; Rettig, 2007). Several studies have reported a number of usability problems in a variety of ERP systems using different research methods (see Table 1). Although there has been some progress in improving ERP usability in the past decade, recent studies confirm that many of the fundamental usability challenges still exist.

Research on ERP systems in the Information Systems (IS) literature has been focused on the success and failure factors for ERP implementations in organizations (Botta-Genoulaz et al, 2005; Grossman & Walsh, 2004; Sarker & Less, 2003; Siau, 2004; Snider et al, 2009) and the psychological determinants of the end users’ intentions to adopt ERP systems (Amoako-Gyampah, 2007; Bueno &

Table 1 Usability issues identified in ERP user studies

<table><tr><td>References</td><td>Data sample</td><td>Methodology</td><td>System</td><td>Usability issues</td></tr><tr><td>Topi et al (2005)</td><td>Nine ERP system users, one non-user</td><td>In-depth, semi-structured interviews</td><td>Confidential</td><td>Difficulty in identifying and accessing needed information and functionsCumbersome error-handling mechanismsTransaction execution problemsSystem complexityTerminology problems</td></tr><tr><td>Matthews (2008)</td><td>250 customers of an enterprise application company and 100 non-customers</td><td>Survey</td><td>Unspecified</td><td>Difficulty in finding information and understanding how to navigate through the systemChore for any one person to learn portion of application that will be used on a daily basisDifficult to navigate beyond small part of system with which user is familiarIssues with using other parts of the system, as they work differently, have different types of interaction</td></tr><tr><td>Singh &amp; Wesson (2009)</td><td>Three usability experts</td><td>Heuristic evaluation</td><td>SAP business one</td><td>Navigation and access to informationPresentation of screen outputAppropriateness of task supportAbility to customize</td></tr><tr><td>Scholtz et al (2010)</td><td>21 CS students in an MIS course</td><td>Case study with electronic time diaries, surveys, and usability questionnaires</td><td>SAP R/3</td><td>Navigation issues, including finding functions in menus and difficulty in searchingPresentation problems, including complexity and abundance of tabs, information overload</td></tr><tr><td>Parks (2012)</td><td>38 participants, 19 of whom performed the test procedure as part of their normal work</td><td>Series of 42 controlled experiments</td><td>PeopleSoftTM</td><td>Complex, dense screensDifficult to navigateLack of support for navigation and data entry</td></tr><tr><td>Lambeck et al (2014a, b)</td><td>184 users of ERP systems small- and medium-size companies</td><td>Survey</td><td>SAP (28.26%)plus broad range of other systems</td><td>High level od system complexityProvides more information and details than is neededDifficulties with locating required functionality</td></tr><tr><td>Wong et al (2015)</td><td>127 users (questionnaire), 24 of those for interviews</td><td>System Usability Scale (SUS) questionnaire and semi-structured interviews</td><td>SAP</td><td>Lack of system communicativeness (i.e., effectiveness in communicating to the user the purpose it was developed for and how to use it</td></tr></table>

Salmeron, 2008). Little research has delved more deeply into the design characteristics that affect end user perceptions of system usability.

## Process visualization

The concept of a business process is central to ERP systems. Efforts to help users understand and visualize processes go back to the 1990s, with the publication of the event-driven process models underlying SAP R/3 (Keller & Teufel, 1998). Cutting-edge strategies of ERP vendors include developing enterprise business process analysis (eBPA) tools, such as SAP Process Orchestration and SAP Operational Process Intelligence, which help define and monitor business processes for the postmodern enterprise landscape. Current enterprise solutions often span multiple platforms and include applications from different vendors, some of which are delivered via cloud services (Hostmann et al, 2015; Phelan, 2015).

Many business process management (BPM) and workflow management systems automatically extract and visualize business process models from the event logs of

ERP systems. Depending on the purpose of the visualization, different forms of process models can be discovered (van der Aalst, 2011), such as control flow (van der Aalst, 2010), data flow (Sun et al, 2006), organizational structure, and social networks (van der Aalst et al, 2007). For example, the Disco system constructs a business process map by mining system event logs (Fluxicon, 2016). Research in this area focuses on tackling several key challenges, such as laying out complex graphs. Some BPM packages address the graph complexity problem by presenting data at varying levels of granularity (Streit et al, 2005) and from different user perspectives (Bobrik et al, 2007; Jablonski & Goetz, 2008).

Most process visualization techniques are designed to facilitate process discovery, analysis, and evaluation for management purposes rather than for usability improvement. They have not been integrated into enterprise systems to support end users in their daily operations (van der Aalst et al, 2010). The Compass system (Hipp et al, 2012) supports workers in automotive engineering by helping them navigate large process spaces and keep track of process-related documents at varying levels of detail. Differently from our approach, this system runs outside of the enterprise tools involved in those processes and uses process model descriptions that are external to those tools.

Compared to the above research, our work is unique in that (1) we instrument user interface solutions to usability problems, embed them within an ERP system prototype, and evaluate them with users; (2) processrelated user support is generated by the enterprise system itself using the data stored within it; and (3) we use collaboration theory as a guide in designing these solutions.

## Human–computer collaboration

The human–computer collaboration (HCC) paradigm of system–user interaction defines collaboration as ‘‘a process in which two or more agents work together to achieve shared goals’’ (Terveen, 1995, p. 67). In HCC, the two agents (a.k.a. parties) are a computer system and a human user. The HCC paradigm proposes to fundamentally shift our view of the relationship between a human user and a computer system (Grosz & Kraus, 1996; Grosz, 2005; Rich et al, 2001; Terveen, 1995) from that of master–servant to partner-to-partner (Grosz, 1996; Shieber, 1996). Consequential to that shift, the division of labor and the models of human–computer interaction may change, placing a greater focus on the system’s role in the success of the overall process and outcome. Notably, throughout our whole project we do not seek any human-like qualities in the system; instead, we employ the human-complementary approach (Terveen, 1995), which stipulates that people and computers have very different strengths, and the allocation of tasks between them must be done according to the natural strengths of each.

HCC is grounded in human collaboration theory (e.g., Bratman, 1992), which has been developed into logicbased mathematical models (Grosz & Sidner, 1990; Grosz & Kraus, 1996). To summarize its theoretical underpinnings, collaboration requires its parties to share a goal as well as the group and individual plans for achieving that goal. The goal (sometimes referred to as the collaborative activity) and the associated plan may be initially incomplete and undergo decomposition, refinement and revision as the parties progress in the process of working on the activity. Plan development and execution require that the parties communicate, sharing the relevant details regarding their plans and their progress as needed. For such communication to be effective, the parties should maintain a shared context regarding their joint activity. Furthermore, collaboration requires mutual responsiveness and mutual support between partners. These two aspects motivate collaborators to learn and adapt to each other, help a partner that is having a problem performing his/her part, and engage in other helpful behaviors caused by their commitment to the shared goal.

HCC has been applied to the development of user interfaces that illustrate this paradigm. These include the COLLAGEN system (Rich et al, 2001), which supports collaborative planning, and Writers Aid (Babaian et al, 2002), which assists authors by automatically finding and inserting needed references in scientific manuscripts. Both are based on the SharedPlans model of collaboration (Grosz & Sidner, 1990; Grosz & Kraus, 1996). While there has been a noticeable movement toward smarter, more collaborative applications in recent years, these advances have yet to reach the domain of complex enterprise software. To the best of our knowledge, there has been no other research on improving usability via strengthening the collaborative capabilities of large-scale enterprise systems.

## Other related approaches

Existing approaches most closely related to Automated Playback and Interactive Process Visualization include task recommender and tutorial systems that are derived from an embedded model of the system’s functionality combined with the recorded history of prior use. Examples include the OWL recommender system (Linton et al, 2000) and the ADAPTS system (Brusilovsky & Cooper, 2002). Other related examples include CoScripter, which allows users to record, replay, and share scripts implementing web-based enterprise processes (Leshed et al, 2008), and SmartAide\`, which dynamically composes context-aware, step-by-step instructions (Ramachandran & Young, 2005).

The capture-and-replay approach is also used for automating software quality assurance purposes in the field (Joshi & Orso, 2006; Saff et al, 2005). What distinguishes our Automated Playback feature from these and other such tools (e.g., tools reviewed in Jovic et al, 2010) is that it is presented to the user as a tutorial rather than being used for software testing or other development purposes.

## Methods

In this section, we further motivate and explain how the two components presented in this paper were developed within the scope of a larger research project on designing collaborative ERP systems for improving usability.

A key aspect of design research lies in its relevance to practice (Hevner et al, 2004; Zimmerman et al, 2007). Poor ERP usability is a widely reported problem, and designing effective user interfaces for complex systems has been acknowledged as the next frontier for usability research and methods (Redish, 2007). The complexity of ERP and other enterprise systems stems from the need to support a very broad range of business tasks and users with varying expertise. Enterprise tasks are highly interdependent, yet relationships between them are largely hidden from the users. Furthermore, each task interface is implemented using a multitude of parameters in order to accommodate industry-wide, rather than companyspecific, business practices. When exposed to the vast set of generic options, users often feel overwhelmed, confused, and lost within the maze-like landscape of the innumerable task interfaces (Lambeck et al, 2014b).

![](/api/attachments/Y5YTHBDK/fulltext/images/a88a69d4749810abe3b6c1be4dbc01bcf43580de6216303b2c5dfab40e8fcf5e.jpg)  
Figure 1 Designing collaborative ERP systems – research map.

We follow design science research frameworks (Hevner et al, 2004; Peffers et al, 2007), including one formulated specifically for HCI research (Zimmerman et al, 2007). As done by Rosenkranz et al (2016), our research is grounded in theory from the start and throughout all stages. We have combined theory, field research, and engineering practices in a novel way to develop innovative artifacts and derive new knowledge. In our evaluation, we examined artifact features in relationship to specific goals and measures, as advocated by Niehaves and Ortbach (2016). Figure 1 shows a variation of Hevner et al’s Information Systems Research Framework for Design Research (2004, p. 80). It presents a map of our research in improving the usability of ERP systems. The artifacts and contributions that are the subject of this paper appear in italics.

In our earlier work, we (1) detailed the theory behind the human–computer collaboration paradigm, which serves as a guiding theory to our research, and (2)

conceptually and empirically linked collaborative properties of systems with system usability, thus motivating and justifying our collaboration-based approach to tackling the inadequate usability of complex systems (Babaian et al, 2006; Topi et al, 2006). To apply the HCC paradigm in the context of ERP systems, we first needed to identify the usability problems experienced by users in the field. We thus developed a set of interview questions for eliciting information regarding usability issues. These questions address the behaviors of the ERP system and its users in the context of usability problems and collaboration theory (as outlined in the ‘‘Human–computer collaboration’’ section).

We conducted 43 field interviews and observations in four different companies that used three different ERP systems. These companies were from different industry sectors (engineering, IT, property management, and medical device manufacturing), and the interviewees represented a broad sample of users with varying ERP experience, company tenure, and job roles. The interviews were semi-structured, and the 24 interview questions were pre-designed and pilot-tested to gather users’ experience with the ERP systems. More than 1500 pages

## On performing individual tasks

I have a little checklist, so when I do ACH payments, I just have screen charts and just little directions that I need to go back in and redo it. I have just directions on step-by-step with the screen chart. This was just so much easier.

[When entering a sales order], there is nothing that is going to tell you you've entered in the header and now you go into the line item and you update this and you update that. The system doesn't do any of that It's more of its user having to know the steps.

They memorized it. They've memorized what needs to happen too. So, you need to know the screens. And you need to be trained in what the process is.

On relating ERP tasks to the overall process

There's a transaction for A’, transaction for "B” and transaction for C” and nothing links them...

[ERP] doesn't tell you what steps to take next. You have to basically, like I said, know what the next step is for your process, for what your job title is to do

I went to three-weeks-worth of [ERP] training, passed the certification exam, came back to my desk and started my project and literally did not know how to start. There's another gentleman on my team who I brought with me. We sat down at our desks on that first Monday back; and we didn't know how to get started. So we had a [ERP] consultant join us; and he worked with us for two days a week.

On system as a collaborator

So with the system, it's somebody that just smirks at you...And that's the frustrating part about it that again is the biggest pain in the backside. So, I would say, it's not a good partner, I feel like it's an impassive sometimes uncooperative coworker

Figure 2 Selected quotes from interviews of ERP field users.

of transcribed interview data were collected for analysis. Four members of our research group were divided into two groups of coders. One group was responsible for coding the collaboration aspect and the other for coding the system usability aspect. The two groups worked independently. Within each group, the two coders coded each interview transcript independently, with over 70% inter-coder reliability. Discrepancies in coding were identified and addressed by the coders by means of correspondence and face-to-face meetings. During the coding, each transcript was divided into multi-sentence chunks, each of which was assigned to zero, one, or multiple coding categories that were developed based on collaboration theory (Bratman, 1992) or the ISO definition of usability (ISO, 1998).

We analyzed the coded data, categorizing usability issues and other observed phenomena based on the principles of collaboration. This analysis confirmed that all usability breakdowns could be explained as violations of one or more tenets of collaboration, sometimes on the part of the user, but overwhelmingly by the system. Importantly, the same phenomena were present regardless of the company size or the type of ERP system. A detailed description of these findings is the subject of previously published work (Babaian et al, 2010; Cooprider et al, 2010).

As an illustration, consider the quotes from interviews with ERP system users in Figure 2. They convey the complexity of the system and the need for built-in task and process-level support, which is clearly lacking. Even after extensive training, users have to memorize step-bystep procedures or turn to checklists or manuals in order to perform their tasks.

To summarize, our key finding was that the lack of system support for helping users understand relationships between individual system components (e.g., tasks within a business process as well as related data and interface components) is one of the biggest obstacles to the productive use of ERP systems. Considering these observations through the lens of collaboration theory, we concluded that:

DP1 The user interface should provide a mechanism for customizing the vocabulary of terms used by the system in its communication to the user, the composition of business transactions, and the content of the system's informational output to match the practices of the organization. There should be a mechanism for incorporating the customizations from an earlier version of the system to a later one.

DP2 The system should provide navigational and progress guidance to a user performing a transaction, indicating the broader context of each interaction in terms of the related business process components and specifying the completed and remaining parts. A sufficiently competent user should be able to turn off this guidance if it becomes a distraction.

DP3When the system detects a problem, it should identify the possible causes and ways of resolving it. If the fix is obvious, the system should inform the user and perform it. If it isn't obvious, the possible causes and resolution scenarios should be presented to the user and be readily executable. If the system is unable to identify resolution strategies, it should present the user with the relevant data and transactions.

DP4 In presenting selection choices, the system should utilize what it knows about the user, the organization, the task, and the context, and provide faster access to the more likely choices than the less likely ones. Where the choice of data or action is obvious, the system should have an option of not waiting for the user to enact it. The user should have an option to replace/cancel the system's provided choice of data/action.

Figure 3 Design principles for collaborative ERP systems.

• Users cannot be expected to know all of the relationships between the different system components because of their number and complexity.

• Since these components comprise the ERP system, the system itself is responsible for sharing its knowledge with the user in an understandable and actionable way.

Field studies were followed by the formulation of design principles for creating ERP systems that overcome the usability challenges we identified (Babaian et al, 2010). These design principles were derived by analyzing the findings of the field studies within the context of ERP systems, with collaboration theory serving as a guide. Design principles DP1 through DP4 (see Figure 3) do not mandate a specific implementation, which can and should vary, but outline the system properties and behaviors that strengthen its collaborative capabilities and, thus, can be expected to lead to greater usability.

For the system to guide the user in an effective, context-aware way, it needs to keep track of the context of each interaction and be able to determine what information is relevant and should be shared. Therefore, the design of the system must support reasoning about the system’s functional components and their relationship to the business tasks in the context of the current interaction. In addition, having information regarding users and their past interactions would enable the guidance to be adjusted, based on specific user experiences. Common usage patterns could be discovered and used to further improve the effectiveness of the interactions.

We have designed and implemented the task–interface–logging (TIL) model, which represents this knowledge in a relational database (see Figure 4). The TIL model contains specifications of tasks; their input and output data; their composition from interface pages and lower-level interface components; and their aggregation into business processes (Lucas and Babaian, 2012). The logging module captures both task- and key-press level details of system–user interactions. The TIL model is an integral part of the novel interface components we are presenting here; the data it contains enable quick reconstruction and querying of detailed histories of performed tasks and processes in real time.

Task guidance and navigational support must be provided at both the task and process levels, since users experience significant challenges in learning the details of an individual transaction as well as in understanding its role within a broader business process (refer to Figure 2). In this context, a task is a basic unit within a business process and may require the completion of several steps spread across several pages or screens, each of which prompts for a number of parameter values. The order entry task, for example, comprises at least three pages for entering the order header, customer information, and order line details. At the process level, a business process usually consists of a set of related tasks for a specific business or organizational goal. The order fulfillment process involves order entry, handling, packing, and shipping tasks. Furthermore, tasks in a business process may be performed by different users from different business departments at different times. The complexity of the interfaces often imposes a great cognitive burden on users, as they have to learn and memorize the task steps as well as discover and understand the mostly invisible relationships between their own tasks and the rest of the process. To address these problems, we designed and implemented two novel interface components for the prototype: Automated Playback and Interactive Process Visualization. The former component provides operational guidance at the task level, and the latter provides navigational and progress guidance at the process level.

![](/api/attachments/Y5YTHBDK/fulltext/images/113baa02f4b56c546834e3cc818455bc4267d61454f1f0229c6dfd39f29d93c1.jpg)  
Figure 4 Entity–relationship diagram of the TIL model (figure from an earlier paper).

Both the TIL model and the components that we present next underwent a number of revisions, following tests of their pilot versions for performance and usability characteristics. The laboratory user studies of the two components are presented in the ‘‘Evaluation’’ section.

## The ERP prototype

In our ERP prototype, Automated Playback (Babaian and Lucas, 2012) is a type of animated tutorial that allows a user to select a previously completed task or process and see it replayed step by step, just as it had been executed, in order to learn or recall how to perform it. Interactive Process Visualization (Lucas et al, 2013) is displayed alongside the regular task screen. It consists of graphbased visualizations of the performed process and the current process instance, with detailed contextual information displayed in a separate pane. The two components illustrate how to provide the kind of guidance mandated by design principle DP2, while adhering to the guidelines of DP4 (see Figure 3).

## Automated Playback

The Automated Playback component provides operational guidance at the task level by allowing a user to view the animation of a previously completed task. It is often a memorization challenge to perform ERP tasks, since many require that the user fills out multiple pages, each containing fields for many parameters. For new or unfamiliar tasks, the user typically seeks help from colleagues or supervisors, as the built-in help functions in most ERP systems are often unhelpful. The Automated Playback feature thus serves as a dynamic, online tutorial to assist user learning and training. By watching the replayed task execution, the user can get needed guidance regarding:

• The steps required for completing a task

• The mandatory fields on each page

• The parameter values that are expected in each field

• How to search and find values for parameters

The user can request a playback within any task page by clicking on the Show Me button. In response, the system presents an interface for selecting a particular task instance to replay (Figure 5). This interface allows for filtering out task instances based on the task name, the user who performed it, a time window, or a specific business document that the task produced (e.g., an order #35). The left side of the task instance selection screen in Figure 5 displays a list of task instances completed within the user-chosen time interval. The right side presents a visualization of the business process context of the selected task instance, in accordance with design principle DP4. The contextual information includes the tasks preceding the selected one in the business process instance (described in detail in the subsections that follow).

Upon the user submitting a selection, the system dynamically constructs a script demonstrating the steps performed while completing the selected task instance. Those steps are then replayed on the interface, with traces showing mouse movements and mouse clicks as well as all data entry. A video demonstration of the Automated Playback feature can be accessed at http://cis. bentley.edu/ERP/demos/playbackdemo.avi.

## Interactive Process Visualization

The second component visualizes task- and processrelated information using two types of graphs. A process graph defines how a process is carried out in general through a series of related tasks. A process instance graph tracks the actual execution of a process by visualizing a specific instance of that process. Important contextual information conveyed by this visualization includes:

![](/api/attachments/Y5YTHBDK/fulltext/images/2680b9b1ec0c6895e4385a044ed5b6357191cb252f2fe1dc12104d2945d45429.jpg)  
Figure 5 Task instance selection screen for Automated Playback.

• Which tasks make up a process (the graph structure)

• How tasks relate to each other (the document flow and frequency of transitions between tasks)

• What comes next (future tasks)

• How a process is executed in a specific case (the process instance)

• Who is involved in a process instance (the users)

• What has been done (the status and progress)

Figure 6a presents the overview of our ERP prototype’s user interface for this component. It contains three panes: the left pane (task pane) is the task page, the upper right pane displays the visualizations, and the bottom-right pane (process details pane) presents detailed information regarding the graph. Figure 6b displays a view of only the right side. We will be using a purchasing process example to illustrate how a process’s contextual information is visualized.

## Process Graph

Which tasks make up a process A business process is rendered as a connected graph in which each node represents a task. A node is labeled by its task name. In Figure 6b, the purchasing process consists of six tasks (nodes): Add Master Data, Add Purchase Requisition, Add Purchase Order, Edit Purchase Requisition, Edit Purchase Order, and Add Goods Receipt. The system highlights the current task that the user is working on, which is Add Purchase Order in this example. Different borders are used to distinguish between required (solid) and optional (dashed) tasks. A yellow, rounded box represents a master data task (e.g., adding materials or vendors). Clicking on a task will turn its node green and will show the task name, the output document type, whether it is optional or not, and the pages or screens that must be filled out in the bottom-right process details pane.

How tasks relate to each other Tasks are connected in the graph by directed links (arrows). These links represent the document flow between tasks. For example, the arrow from Add Purchase Requisition to Add Purchase Order means that the output document (i.e., a purchase requisition) produced by the first task is an input document to the second task. Additionally, a round link means that a task (e.g., Edit Purchase Requisition and Edit Purchase Order) may be performed repeatedly. The thickness of each link is proportional to the frequency of the document flow it represents. If clicked, a link will be highlighted in green and its detailed information (from task, to task, data flow, and frequency) will be displayed in the process details pane.

![](/api/attachments/Y5YTHBDK/fulltext/images/7e1102bd4db8d6caca11ea89841eb82a6ddd4ddfda11aac662355f656ac8e4d2.jpg)  
Figure 6 Interactive Process Visualization component. a ERP prototype with the Interactive Process Visualization component on the right, b enlarged fragment of a, showing the Process Graph and process details panes of the Interactive Process Visualization.

What comes next Tasks that may follow the current one can be found by following the links from that task. Figure 6a shows that, of the two tasks that may follow Add Purchase Order, Add Goods Receipt is more likely to be performed next, as the link to it from Add Purchase Order is thicker than the link to Edit Purchase Order.

## Process Instance Graph

How a process is executed in a specific case A process instance graph tracks process execution history by showing all the previous task instances (represented by nodes) related to the current task. Figure 7 displays the process instance graph for the Add Goods Receipt task instance after the Process Instance Graph tab on the upper right pane has been clicked. Each node is labeled by task name and output document number. This graph shows that this instance of the purchasing process started with one material (#135) being added to the system. The material was included in the purchase requisition (#30), which was edited to include another material (#133). A purchase order (#26) was created and later edited three times, with a material (#138) being added. This purchasing process instance will be completed when the current goods receipt (#34) is added to the system.

Who is involved in a process instance The system can retrieve user information for each task instance. Clicking on a task instance node in the process instance graph causes the process details pane to display the names of the users who have worked on the task instance and when each started and finished working on it.

What has been done At the process level, a process instance graph indicates progress information by showing all the task instances in the execution history. Furthermore, task status and output information are displayed in the Process Details window when the user clicks on any specific task instance node. For example, in Figure 7, the status of the highlighted task is Completed.

## Supporting infrastructure

Both the playback and visualization components are supported by a backend infrastructure that automatically logs all system–user interactions and records them in the

TIL model (Figure 4). Since this model captures information on users, tasks, task instances, processes, interaction events, data entered, etc., the system is able to dynam ically assemble contextual information about processes and tasks as well as the past executions of tasks. This is what makes the functionality demonstrated by the two components possible.

We have developed several algorithms and database procedures for efficient composition of the process instance graph (Lucas & Babaian, 2012). At the time of the completion of a task instance, the system finds the previous task instances that produced the input documents that were used and creates and saves the links between them. The current task instance is then added to the representation of the process instance that includes the currently performed task. This design speeds up the runtime construction of process instance graphs. Similarly, the frequencies of task transitions are updated each time a task interface is opened.

## Evaluation

We have designed two laboratory experiments and one expert user study as part of a summative evaluation of the developed artifacts. Their purpose is to verify whether the developed prototypes meet their design goals and evaluate their usefulness and effectiveness in providing task and process support to ERP users (Gregor and Hevner, 2013). The two laboratory experiments followed the traditional HCI practice of user performance evaluation (Lam et al, 2012). Since the developed artifacts do not have any analogs in existing practice, we did not have any control interfaces with which to compare Automated Playback and Interactive Process Visualization. We focused on user success rate in using the evaluated interfaces to complete a set of tasks for which they were intended. The expert user evaluation served as a point of reference for establishing if the information supplied by the Interactive Process Visualization is available to the users of traditional ERPs; it constitutes a type of usage scenario study (Sedlmair et al, 2012). The choice of these evaluations corresponds to the Technical Risk and Efficacy strategy in Venable et al.’s Framework for Evaluation in Design Science Research (Venable et al, 2016), in which a considerable part of the evaluation activities must be conducted in an artificial, laboratory environment before moving into a more naturalistic setting. We also conducted both formative and summative laboratory pilot studies prior to the evaluations presented below.

The two experiments involved user studies of Automated Playback and Interactive Process Visualization, each conducted with 12 participants recruited from the graduate student population of a business school. The expert user’s experience includes over five years as a super-user in charge of system configuration, diagnostics, and training material preparation at a university. See Table 2 for demographic data.

![](/api/attachments/Y5YTHBDK/fulltext/images/e93a685efb361314c0ef3321c11644c870509e61019be312fb1e427e46548a5b.jpg)  
Figure 7 Process Instance Graph and process details panes of the Interactive Process Visualization.

In the two user experiments, the participants were first shown a short video tutorial to familiarize them with the prototype’s functionality. The tutorials utilized ERP tasks that were different from the one used in the experiments. Each user session in the experiments was captured via screen capture software.

The expert user study was conducted to provide a baseline for judging the effectiveness of our prototype compared to existing mainstream ERP systems. It involved an expert SAP user performing the same task as the one given to participants in the second experiment but with SAP instead of our prototype.

## Experiment 1: Evaluation of Automated Playback

The main goal behind Automated Playback is to provide the user with an easy way to learn/review/recall how to use a specific ERP task interface by viewing how a task was performed in the past. For this evaluation, we designed a laboratory assignment that required that participants find and replay a specific ERP task instance in order to successfully complete their assignment. The participants were asked to create a sales quotation but were given an incomplete set of parameters. This quotation was similar to one previously created by a fictional colleague from the same department. The known parameters described information on the customer and the quoted items. The six missing parameters described company and department-specific information; the correct values for those parameters would be the same ones that had been entered by the fictional colleague. These values could only be accessed by replaying the appropriate instance of the Add Sales Quotation task.

Table 2 Summary of participant demographics

<table><tr><td>Experiments</td><td># of participants</td><td># of native English speakers</td><td>Average experience with enterprise software</td></tr><tr><td>Automated Playback</td><td>12 (6 males, 6 females)</td><td>2</td><td>10 months</td></tr><tr><td>Interactive Process Visualization</td><td>12 (6 males, 6 females)</td><td>3</td><td>12 months</td></tr><tr><td>Expert user study</td><td>1 (female)</td><td>1</td><td>15 years</td></tr></table>

Table 3 Correctness of the outcome of user work in the Automated Playback experiment

<table><tr><td rowspan="2"></td><td colspan="2">Hidden parameters</td></tr><tr><td>Correct</td><td>Incorrect</td></tr><tr><td colspan="3">Specified parameters</td></tr><tr><td>Correct</td><td>5</td><td>1</td></tr><tr><td>Incorrect</td><td>3</td><td>3</td></tr></table>

A secondary goal of the evaluation was to assess if the interface provides an intuitive and easy-to-use mechanism for selecting a specific task instance. Thus, the Add Sales Quotation instance that users needed to review was identified only indirectly, via a combination of the task/document name and the document number.

All 12 participants were able to access the playback interface and correctly identify the instance of the Add Sales Quotation task to play back, although it took some users more than one attempt to find it. All were also able to complete the Add Sales Quotation task upon reviewing the prior interaction in Playback. The resulting sales quotations were analyzed for correctness. Eight out of 12 participants had correct values for all six unidentified parameters and, of those eight, five participants had completed a perfect sales quotation. Of the other four participants, one made mistakes only in the hidden parameters and three had errors in both the specified parameters and the hidden ones. The errors in specified parameters resulted from them entering material or customer data from the colleague’s quotation and were not due to a lack of understanding of how to complete a sales quotation. Table 3 presents a summary of the correctness results.

Upon completion of the assignment, participants were asked to answer open response questions regarding their opinion of the Automated Playback interface. In answering the question on how helpful they found it, all but one user gave positive assessments ranging from ‘‘very help ful’’ to ‘‘relatively helpful.’’ The comments included ‘‘it is very helpful, since I didn’t use this system before,’’ ‘‘demonstration helped in verifying correctness of the approach,’’ and ‘‘ability to go through step-by-step was useful.’’ One user reported ‘‘not liking’’ the feature, preferring to be given a ‘‘form shown [sic] everything I need’’. However, this user responded positively to the question, ‘‘Would you use a feature like this? If yes, under what circumstances?’’ by answering ‘‘sometimes yes, only when I was not familiar with the process.’’ Other reasons for using the system included ‘‘if I was [sic] unclear and wanted to make sure my work was absolutely correct,’’ ‘‘in the case I can’t figure out something, having the process flow and demo would be very valuable,’’ and ‘‘When training new employees.’’ Suggestions for improvement included adding ways to pause, control the speed of the replay, and move back and forth within the demonstration.

The results of this experiment suggest that the Automated Playback feature provides users with sufficient guidance for completing a task on their first try without consulting a manual. Although 58% of participants made at least one mistake in the entered data, those mistakes are at least partially attributable to a misunderstanding of or lack of attention to the goal of the assignment. The users’ assessment of the usefulness of the interface was overwhelmingly positive and included some very practical suggestions for improving the Playback feature.

## Experiment 2: Evaluation of Interactive Process Visualization

The goal of our second experiment was to ascertain if the participants could effectively use the Interactive Process Visualization component to (1) learn about the composition of business processes from tasks, the data flow between the tasks, and common patterns in task sequencing, and (2) discern the details of the execution of a specific instance of a business process. We designed an assignment in which the participants had to create a purchase order and answer questions regarding the purchasing process. The questions (see Table 4) concerned the purchasing process overall as well as the details of a concrete instance. With the exception of Question 10, the questions could only be answered by reviewing and interacting with the process and Process Instance Graphs. All study participants were first-time users of the prototype.

Table 4 Summary of user responses from the Interactive Process Visualization evaluation

<table><tr><td>Question</td><td>Correct answer</td><td>Information source</td><td>Correct</td><td>Incomplete</td><td>Incorrect</td></tr><tr><td>1. What is the name of the process that includes the Add Purchase Order task you are working on now?</td><td>Purchasing</td><td>Process Graph</td><td>5</td><td>0</td><td>7</td></tr><tr><td>2. Is the Add Purchase Order task required or optional in this process?</td><td>Required</td><td>Process Graph</td><td>12</td><td>0</td><td>0</td></tr><tr><td>3. What are the tasks that may immediately precede the Add Purchase Order task?</td><td>Add Purchase Requisition, Edit Purchase Requisition, Add Master Data</td><td>Process Graph</td><td>1</td><td>8</td><td>3</td></tr><tr><td>4. How many screens does the Add Purchase Order task consist of? What are the names of those screens?</td><td>Two, enter header and defaults and enter PO line items</td><td>Process Graph details</td><td>5</td><td>0</td><td>7</td></tr><tr><td>5. What type of documents is used as a basis for creating the purchase order that you are working on?</td><td>Purchase requisition</td><td>Process Graph</td><td>2</td><td>0</td><td>10</td></tr><tr><td>6. Who was the first user to work on that document?</td><td>user4</td><td>Process instance details</td><td>7</td><td>0</td><td>5</td></tr><tr><td>7. Which user edited that document?</td><td>user7</td><td>Process instance details</td><td>10</td><td>0</td><td>2</td></tr><tr><td>8. On what date was that document completed?</td><td>Nov 26</td><td>Process instance details</td><td>8</td><td>0</td><td>4</td></tr><tr><td>9. Which users executed the Add Material Task for the materials specified within the purchase order?</td><td>user2 and user6</td><td>Process instance details</td><td>7</td><td>3</td><td>2</td></tr><tr><td>10. What is the number of the purchase order that you are working on?</td><td>PO #7</td><td>Process Instance Graph and the task pane header</td><td>11</td><td>0</td><td>1</td></tr><tr><td>11. Which task is most likely to follow the Add Purchase Order task you are working on now?</td><td>Add Goods Receipt</td><td>Process Graph details</td><td>9</td><td>0</td><td>3</td></tr><tr><td></td><td></td><td>Total</td><td>77</td><td>11</td><td>44</td></tr></table>

A summary of the results is presented in Table 4, including a count of correct, incomplete, and incorrect responses. A response was judged as incomplete if it did not contain wrong information but did not answer the question fully. Overall, out of 132 answers, 77 (58.3%) were correct, 11 (8.3%) were incomplete, and 44 (33.3%) contained an error.

Analysis of the results reveals that all but four of the first-time users of the system were able to correctly answer most of the questions. Questions 1 and 5 resulted in the greatest number of incorrect responses. The errors in Question 1 were mostly due to users conflating the terms ‘‘task’’ and ‘‘process.’’ Question 3, which had the highest count of incomplete answers, required users to examine the Process Graph carefully in order to identify tasks with links to the Add Purchase Order task. To improve readability of the graph in this respect, we envision augmenting it with an interactive option for highlighting the immediately preceding and following tasks in a different color. Mistakes in Questions 4 and 5 were due, respectively, to misunderstanding what is meant by ‘‘screens’’ (some users identified them as separate panes in a single screen) and by the ‘‘basis’’ for a purchase order.

The correctness rate was much higher in Questions 6 through 11, all of which regard the concrete instance of the process. This is likely due to the conceptual simplicity of the process instance graph, which only depicts the steps that have already been performed or are in progress and leaves out the tasks that may follow.

## Expert user study

To verify the usefulness of the Interactive Process Visualizations in comparison to the standard approaches used by mainstream ERP vendors, we gave the same assignment and questions from the second experiment to an expert user of SAP (see demographic information in Table 2).

For Questions 1, 2, 3, and 11, the expert could not pinpoint where the answers could be found within SAP even after searching system help documentation. These questions have to do with process structure and task sequencing. Figuring out how many screens would be involved for adding a purchase order (PO) (Question 4) required exploring the interface and depended on the user’s expertise with the system. Answers to Questions 5 and 6 regarding the purchase requisition number and the identity of the document creator, respectively, were found among more than a dozen fields within the PO interface page. Answering Questions 7–9 required navigating one or more steps away from the current transaction screen. The resulting PO number (Question 10) showed up when the PO task was completed. In the opinion of our expert user, many of these answers would be beyond the reach of a novice user.

The expert user study demonstrated that first-time, and even experienced, users of SAP would most likely be unable to find the information required to answer many of the questions from Table 4. Some of the questions, such as those on process structure and task sequencing, can only be answered by having knowledge of the process that comes from long and somewhat broad experience in working with SAP. Other answers can be found within the system but are spread across multiple interfaces, most of which require knowing how to navigate to them. A recent study (Lambeck et al, 2014b) revealed that the ‘‘ability to locate desired enterprise functionality remains a general usability problem across different levels of experience’’ and the ‘‘availability of useful visualizations improves perception of complexity’’ reported by the users. Collecting and visualizing the process-related information within a dedicated, interactive pane displayed alongside the task interface, as in our Interactive Process Visualization, should improve the users’ ability to access and learn from it.

## Discussion and conclusion

In this paper, we have presented the design and laboratory evaluation of two novel interface components for task and process guidance in ERP systems: Automated Playback and Interactive Process Visualization. These artifacts were developed as part of a larger research project dedicated to improving ERP usability by designing systems that act as a user’s collaborative partner. Automated Playback works as a learning tool for users seeking to learn or recall how to perform a specific task. It provides a dynamically and automatically composed demonstration of task interfaces, based on prior usage of the system. Interactive Process Visualization offers a means for process navigation support and guidance by visualizing the composition of tasks into business processes. It informs the user of the structure, usage patterns, and important details of the business process surrounding the current task. It is the first process visualization component we know of to be integrated within an ERP system for the purpose of supporting end users.

Both components were developed as illustrative implementations of design principles DP2 and DP4 (Figure 3), which were formulated earlier from field studies of ERP systems using collaboration theory as the design guide. These components rely on the availability of data from the TIL model (Figure 4) as a core part of the system. The TIL model represents information on user interface components, tasks, processes, documents, users, and usage logs; it enables the quick reconstruction of usage history and provides contextual information regarding tasks and processes. The novelty of the presented approach to user support and guidance comes from (1) including the components as an integral part of the ERP system design and (2) using the TIL model to dynamically compose these operational and navigational aids. The designs of the Automated Playback and Interactive Process Visualization components are also unique to research literature and practice, due to the combination of features they provide.

Our laboratory experiments show that these components meet their design goals of unobtrusively aiding users in learning to perform specific tasks as well as understanding how individual tasks fit within the encompassing business process. The usefulness of the Interactive Process Visualization is further demonstrated by the expert study with a state-of-the-art commercial ERP system.

## Implications for theory

Our research makes contributions to the scholarship in Design Science, the HCC paradigm, and usability. First, the work presented here demonstrates both the process and product of a multi-phased and multi-methodological design research project (Figure 1). The process consists of a series of scientific activities, including field studies, design and development of artifacts, and evaluation. Within the overarching design science framework, we have employed a number of rigorous methodologies (qualitative interviews and observations, system development, quantitative experiments, and user studies) to investigate the key problem we tackle – the lack of ERP usability. The products of this process are a set of design artifacts, including four design principles for collaborative ERP systems, the TIL model for enhanced usage logs, and the proof-of-concept prototype with novel user support and guidance components.

Two factors were critical to our success in applying the design research methodology:

• Problem-driven and theory-guided design processes. Our research is motivated by the inadequacy of ERP usability – a real problem facing most organizational end users – and is guided by collaboration theory. Unlike many existing usability heuristics that focus only on specific user interface features (e.g., Nielsen, 1993; Norman, 1983), collaboration theory offers a holistic approach to examining the problem and instrumenting a solution by considering the system’s overall collaborative capabilities.

• Systematically implemented and empirically evaluated design products. Our prototype, which was implemented based on design principles and evaluated by users, provides a tangible test bed for assessing the feasibility and potential utility of our design innovations.

Our project is the first to apply the HCC paradigm to the design of enterprise systems. Compared with other design paradigms proposed in HCI (e.g., user-centered design), it has been studied less. Our research presents a showcase for applying the HCC paradigm for improving the usability of complex enterprise systems. The evaluation results presented here lend evidence to the proposition that improving the collaborative capability of software yields greater usability.

Finally, our research offers an alternative theoretical lens for examining the task of improving ERP usability. As we have discovered, usability challenges experienced by ERP users can be attributed to the lack of a collaborative relationship between the system and its users. A greater degree of collaboration, however, cannot be achieved by simply adjusting superficial aspects of the system’s fac¸ade; it requires underlying support in the form of data and algorithms. Providing the system with capabilities for reasoning about its own interface components, tasks, users, and usage history, as achieved by the TIL data model and its associated algorithms, enables a range of useful collaborative enhancements. Automated Playback and Interactive Process Visualization present two outcomes from designing for collaboration.

## Implications for practice

This research contributes to the practice of ERP system design and development. We have demonstrated two novel interface components for providing system-generated, dynamic user support. The playback feature addresses many of the usability issues identified in Table 1 as well as other negative factors associated with ERP system usage, including:

• Difficulties with locating and accessing the required functionality.

• Inadequate guidance concerning how to execute the steps required for performing a business process.

• The heavy cognitive burden associated with learning and memorizing system interfaces and parameters.

• The tremendous amount of stress that can result from working with these systems.

• The high costs of user training.

• The high risk of system non-use resulting from the lack of organizational learning and knowledge retention.

The graph visualizations preserve organizational practices while addressing issues related to inadequate support for navigation, overly complex interfaces, and lack of support in process execution. By guiding the user through a process, they improve user understanding of tasks and their relationships to each other, the document flow between tasks, and the progression of an ongoing business process instance. Moreover, the readily available process instance information is useful in identifying and resolving problems in error situations. The use of the TIL model as a backend infrastructure demonstrates how embedding TIL data greatly expands the potential repertoire of system functionality related to user support.

Our prototype presents a design exemplar, illustrating how design principles DP2 and DP4 can be implemented. Intended as generic design guidance, these principles do not prescribe any specific implementation. Designers, developers, and vendors of enterprise systems may leverage the TIL model, design principles, and interface components made available by our research for use in other systems and domains.

It is worth noting that incorporating a comprehensive set of collaborative features into enterprise systems may increase both the complexity of the system’s design and the concomitant costs. However, we believe this is more than counterbalanced by the benefits described above. No static help manual or training document can provide those same benefits, even if users were willing to make use of them, which they typically are not (see Ceaparu et al, 2004; Novick & Ward, 2006).

## Limitations and future work

The greatest limitation of the research presented in this paper is that the developed novel approaches are implemented within a proof-of-concept prototype that does not in its breadth match the scope of a real ERP system. Replicating full ERP functionality for academic research purposes is not feasible, and embedding Automated Playback and Interactive Process Visualization into an existing ERP system is not possible because the TIL model data are not being readily available in commercial implementations. Thus, evaluations were conducted with a prototype in a laboratory setting. Although possibilities for field testing the Automated Playback and Interactive Process Visualization are limited, we are planning on presenting these approaches to ERP users for comments and further evaluation.

A second limitation is that the laboratory study participants were all graduate students in the same business school. None had prior experience with the two interface components under study and all received the same training on their use. Additionally, the participants had limited experience with enterprise systems. The homogeneity of this population in terms of education, age ranges, and experience levels supports the internal validity of this study, which was our main goal. These same factors are a limitation from the perspective of external validation, which will be addressed by the field studies noted above.

Another limitation is that only one user participated in the expert study. Having more expert users would have provided for a more thorough assessment. One reason the expert study was necessitated was because it would not have been possible for users with limited expertise in enterprise systems to perform the same tasks with SAP, the commercially available ERP system to which we have access. As our expert study showed, answers to some of the process-related questions we asked participants to answer were not even available to users of SAP. A second reason for requiring an expert study is that objects used in comparison studies should not differ in more than one factor so that findings can be traced to that origin. As far as we know, our interface components have no counterparts in commercially available ERP systems, making it impossible to conduct a comparison study with them.

In the future, we plan on continuing to fine-tune the two interface components presented here through further user studies and observations. We will continue to develop artifacts illustrating possible implementations of the design principles DP1 through DP4.

## About the Authors

Tamara Babaian is an Associate Professor of Computer Information Systems at Bentley University. She received her Ph.D. in Computer Science from Tufts University. Tamara’s research in intelligent and collaborative systems focuses on the design and evaluation of system–user interactions as well as algorithms and representations that support human–computer collaboration. Her work has been published in conference proceedings and journals such as International Journal of Human–Computer Interaction, European Journal of Information Systems, Journal of Database Management, Intelligent User Interfaces, ACM Computer–Human Interaction, and others.

Jennifer Xu is an Associate Professor of Computer Information Systems at Bentley University. She received her Ph.D. in Management Information Systems from the University of Arizona. Her research interests include business intelligence, data mining, business analytics, social network analysis, human–computer interaction, and enterprise systems, with a particular interest in mining networks for knowledge management and business intelligence purposes. She has published more than

## References

AMOAKO-GYAMPAH K (2007) Perceived usefulness, user involvement and behavioral intention: an empirical study of ERP implementation. Computers in Human Behavior 23(3), 1232–1248.

B T, G BJ and S SM (2002) A writer’s collaborative assistant. In Proceedings of the 7th International Conference on Intelli gent User Interfaces, pp 7–14 ACM, San Francisco, CA.

BABAIAN T and LUCAS W (2012) Composing interface demonstrations automatically from usage logs. in: Enterprise Information Systems - 14th International Conference, ICEIS 2012, Revised Selected Papers, pp 376–392, Lecture Notes in Business Information Processing (LNBIP). Springer.

BABAIAN T, LUCAS W and TOPI H (2006) Improving ERP usability through user-system collaboration. International Journal of Enterprise Informa tion Systems 2(3), 10–23.

BABAIAN T, LUCAS W and TOPI H (2007) Visualizing the process: a graphbased approach to enhancing system–user knowledge sharing. In Proceedings of the International Conference on Enterprise Information Systems (ICFIS-2007). pp 123–128

BABAIAN T, LUCAS W, XU J and TOPI H (2010) Usability through system–user collaboration. In Global Perspectives on Design Science Research, Proceedings of the 5th International Conference, DESRIST 2010, pp 394–409, Switzerland, June 2010, Lecture Notes in Computer Science (LNCS). Springer.

## Acknowledgements

We are grateful to the anonymous reviewers, the Associate Editor and the Special Issue Editor for their valuable comments that helped improve this paper. We thank Taylor Gordon, an undergraduate student at Bentley University, for his contribution to the development of the prototype.

50 articles in Information Systems journals, books, and conference proceedings. She is currently serving on the editorial board of Journal of Security Informatics.

Wendy Lucas is a Professor of Computer Information Systems at Bentley University. Her research interests include evaluating system usability, designing collaborative interfaces, and developing new languages and tools for information visualization. In recent years, Wendy’s research has focused on the usability of enterprise resource planning systems. Her research has been published in journals and conference proceedings that include the International Journal of Human–Computer Interaction, the Journal of Database Management, the European Journal of Information Systems, the ACM Computer–Human Interaction conference, and the Design Science Research in Information Systems and Technologies conference.

BABAIAN T, XU J and LUCAS W (2014) Applying design principles for enhancing enterprise system usability. In Proceedings of the 9th International Conference on Software Engineering and Applications (ICSOFT-EA 2014), pp 162–169.

B W and W C (2006) ERP II: best practices for successful implementing an ERP upgrade. Communications of the ACM 49(3), 105–109.

BISHU RR, KLEINER BM and DRURY CG (2001) Ergonomic concerns in enterprise resource planning (ERP) systems and its implementations. In Proceedings of the IFIP TC5 WG5.3/5.7/5.12 Fourth International Conference on the Design of Information Infrastructure Systems for Manufacturing: Global Engineering, Manufacturing and Enterprise Networks, pp 146–155. Deventer, The Netherlands.

B R, R M and B T (2007) Parameterizable Views for Process Visualization. Centre for Telematics and Information Technology, University of Twente, Enschede.

B -G V, M P-A and G B (2005). A survey on the recent research literature on ERP systems. Computers in Industry 56(6), 510-522.

BRATMAN ME (1992) Shared cooperative activity. The Philosophical Review 101(2), 327–341.

BRUSILOVSKY P and COOPER DW (2002). Domain, task, and user models for an adaptive hypermedia performance support system. In Proceedings

of the 7th International Conference on Intelligent User Interfaces, pp 23–30, ACM, San Francisco, CA.

BUENO S and SALMERON JL (2008). TAM-based success modeling in ERP. Interacting with Computers 20(6), 515–523.

CALISIR F and CALISIR F (2004). The relation of interface usability characteristics, perceived usefulness, and perceived ease of use to end-user satisfaction with enterprise resource planning (ERP) systems. Computers in Human Behavior 20(4), 505–515.

CEAPARU I, LAZAR J, BESSIERE K, ROBINSON J and SHNEIDERMAN B (2004) Determining causes and severity of end-user frustration. International Journal of Human-Computer Interaction 17(3), 333–356.

COOPRIDER J, TOPI H, XU J, DIAS M, BABAIAN T and LUCAS W (2010) A collaboration model for ERP user–system interaction. In System Sciences (HICSS), 2010 43rd Hawaii International Conference, pp 1–9, IEEE.

FLUXICON (2016) Disco: discovery your processes. https://fluxicon.com/ disco/. Accessed January 25, 2016.

GANLY D and MONTGOMERY N (2015) Hype Cycle for ERP. Gartner, Stamford, CT.

GREGOR S and HEVNER AR (2013) Positioning and presenting design science research for maximum impact. MIS Quarterly 37(2), 337–355.

GROSSMAN J and WALSH J (2004) Avoiding the pitfalls of ERP system implementation. Information Systems Management 21(2), 38–42.

G BJ and S C (1990) Plans for discourse. In Intentions in Communications (COHEN P, MORGAN J and POLLACK M, (Eds), pp 417–444, MIT Press, Cambridge.

GROSZ BJ (1996) Collaborative systems: AAAI presidential address. AI Magazine 17(2), 67–85.

GROSZ BJ (2005) Beyond mice and menus. Proceedings of the American Philosophical Society 149(4), 529–543.

GROSZ BJ and KRAUS S (1996) Collaborative plans for complex group action. Artificial Intelligence 86(2), 269–357.

HESTERMANN C (2009) Key Issues for Enterprise Resource Planning 2009. Gartner, Stamford, CT.

HEVNER A, MARCH S, PARK J and RAM S (2004) Design science in information systems research. MIS Quarterly 28(1), 75–105.

HOSTMANN W ET AL. (2015) Vendor Rating: SAP. Gartner, CT.

HIPP M, MUTSCHLER B and REICHERT M (2012). Navigating in Complex Business Processes. Database and Expert Systems Applications, pp 466–480, Springer, Berlin.

IANSITI M (2016) ERP end-user business productivity: a field study of SAP & Microsoft. http://download.microsoft.com/download/4/2/7/ 427edce8-351e-4e60-83d6-28bbf2f80d0b/ KeystoneERPAssessmentWhitepaper.pdf. Accessed February 23, 2016.

ISO (1998). ISO 9241-11: ergonomic requirements for office work with visual display terminals (VDTs)—Part 11: guidance on usability. https://www.iso.org/standard/16883.html. Accessed July 20, 2017.

JABLONSKI S and GOETZ M (2008) Perspective oriented business process visualization. In Proceedings of the 2007 International Conference on Business Process Management, pp 144–155, Brisbane, Australia.

JOSHI S and ORSO A (2006) Capture and Replay of User Executions to Improve Software Quality. Technical Report, Georgia Institute of Technology.

JOVIC M, ADAMOLI A, ZAPARANUKS D and HAUSWIRTH M (2010) Automating performance testing of interactive java applications. In Proceedings of the 5th Workshop on Automation of Software Test, pp 8–15.

K G and T T (1998) SAP R/3 Process Oriented Implementation. Addison-Wesley Longman Publishing, Boston.

KOH SCL, GUNASEKARAN A and COOPER JR (2009) The demand for training and consultancy investment in SME-specific ERP systems implementation and operation. International Journal of Production Economics 122(1), 241–254.

K J and R M (2013) Data flow abstractions and adaptations through updatable process views. In Proceedings of the 28th Annual ACM Symposium on Applied Computing, pp 1447–1453, ACM.

LAM H, BERTINI E, ISENBERG P, PLAISANT C, and CARPENDALE S (2012) Empirical studies in information visualization: seven scenarios. İEEE Transactions on Visualization and Computer Graphics 18(9), 1520–1536.

LAMBECK C, FOHRHOLZ C, LEYH C, S<sup>ˇ</sup>U¯PULNIECE I and MULLER R (2014a) Commonalities and contrasts: an investigation of ERP usability in a comparative user study. In Proceedings of the 22nd European Conference on Information Systems (ECIS 2014), pp 1–15, Israel, Tel Aviv.

LAMBECK C, MULLER R, FOHRHOLZ C and LEYH C (2014b) (Re-) evaluating user interface aspects in ERP systems: an empirical user study. In Proceedings of the 47th Hawaii International Conference on System Science, pp 396–405, Waikoloa, HI.

LESHED G, HABER EM, MATTHEWS T and LAU T (2008) Coscripter: automating & sharing how-to knowledge in the enterprise. In Proceedings of the 26th Annual SIGCHI Conference on Human Factors in Computing Systems, pp 1719–1728, Florence, Italy.

LINTON F, JOY D, SCHAEFER H-P and CHARRON A (2000) Owl: a recommender system for organization-wide learning. Journal of Educational Technology & Society 3(1), 62–76.

LOVE PED, IRANI Z, STandING C AND THEMISTOCLEOUS M (2007) Influence of job demands, job control and social support on information systems professionals’ psychological well-being. International Journal of Manpower 28(6), 513–528.

LUCAS W and BABAIAN T (2012) Implementing design principles for collaborative ERP systems. In Proceedings of the 7th International Conference on Design Science Research in Information Systems and Technology, DESRIST’12, pp 88–107, Las Vegas, NV, May 2012, Lecture Notes in Computer Science (LNCS), Springer.

LUCAS W, XU J and BABAIAN T (2013) Visualizing ERP usage logs in real time. In Proceedings of the 15th International Conference on Enterprise Information Systems (ICEIS 2013), pp 83–90, SciTePress.

MATTHEWS D (2008) Usability as an ERP selection criteria. http:// hosteddocs.ittoolbox.com/wpusability.pdf. Accessed July 20, 2017.

NIEHAVES B and ORTBACH K (2016) The inner and the outer model in explanatory design theory: the case of designing electronic feedback systems. European Journal of Information Systems 25(4), 303–316.

NIELSEN J (1993). Usability Engineering. Morgan Kaufman, Boston, MA.

NORMAN DA (1983) Design principles for human-computer interfaces. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, pp 1–10, Boston, MA.

NORTON AL, COULSON-THOMAS YM, COULSON-THOMAS CJ and ASHURST C (2013). Ensuring benefits realisation from ERP II: the CSF phasing model. Journal of Enterprise Information Management 26(3), 218–234.

NOVICK DG and WARD K (2006) Why don’t people read the manual? In Proceedings of the 24th Annual ACM International Conference on Design of Communication (SIGDOC’06), pp 11–18, Myrtle Beach, CA.

PARKS NE (2012) Testing & quantifying ERP usability. In Proceedings of The 13th Annual Conference on Information Technology Education, pp 31–36, Calgary, Canada.

PEFFERS K, TUUNANEN T, ROTHENBERGER MA and CHATTERJEE S (2007) A design science research methodology for information systems research. Journal of management information systems 24(3), 45–77.

PHELAN P (2015) Use Enterprise Business Process Analysis to Improve Postmodern ERP Execution. Gartner, Stamford.

RAMACHANDRAN A and YOUNG RM (2005) Providing intelligent help across applications in dynamic user and environment contexts. In Proceedings of the 10th International Conference on Intelligent User Interfaces (IUI’05), pp 269–271, San Diego, CA.

REDISH JG (2007) Expanding usability testing to evaluate complex systems. Journal of Usability Studies 2(3), 102–111.

RETTIG C (2007) The trouble with enterprise software. Sloan Management Review 49(1), 21–27.

RICH C, SIDNER CL and LESH N (2001) Collagen: applying collaborative discourse theory to human-computer interaction. AI magazine 22(4), 15–26.

R C, H R, R¨ M and B W (2016) Supporting the design of data integration requirements during the development of data warehouses: a communication theory-based approach. European Journal of Information Systems 26(1), 84–115.

S D, A S, P JH and E MD (2005) Automatic test factoring for Java. In Proceedings of the 20th IEEE/ACM International Conference on Automated Software Engineering, pp 114–123.

SARKER S and LESS AS (2003) Using a case study to test the role of three key social enablers in ERP implementation. Information & Management 40(8), 813–829.

SCHOLTZ B, CILLIERS C and CALITZ A (2010) Qualitative techniques for evaluating enterprise resource planning (ERP) user interfaces. In

Proceedings of the 2010 Annual Research Conference of the South African Institute of Computer Scientists and Information Technologists, pp 284–293, New York, NY.

SCOTT JE (2005) Post-implementation usability of ERP training materials: the user’s perspective. Information Systems Management 22(2), 67–77.

SEARS A and JACKO JA (2008) The Human–Computer Interaction Handbook: Fundamentals, Evolving Technologies and Emerging Applications. Lawr ence Erlbaum Associates, New York City, NY.

SEDLMAIR M, MEYER M, and MUNZNER T (2012) Design study methodology: reflections from the trenches and the stacks. IEEE Transactions on Visualization and Computer Graphics 18(12), 2431–2440.

SHIEBER SM (1996) A call for collaborative interfaces. ACM Computing Surveys 28(A(electronic)), 143.

SIAU K (2004) Enterprise resource planning (ERP) implementation methodologies. Journal of Database Management 15(1), 1–6.

SINGH A and WESSON J (2009) Evaluation criteria for assessing the usability of ERP systems. In Proceedings of South African Institute of Computer Scientists and Information Technology, Riverside, Vanderbijlpark, South Africa.

SNIDER B, DA SILVEIRA GJC and BALAKRISHNAN J (2009) ERP implementation at SMEs: analysis of five Canadian cases. International Journal of Opera tions & Production Management 29(1), 4–29.

STREIT AT, PHAM BL and BROWN RA (2005) Visualization support for managing large business process specifications. In Proceedings of the 3rd International Conference on Business Process Management (BPM2005), Nancy, France.

SUN SX, ZHAO JL, NUNAMAKER JF and SHENG ORL (2006) Formulating the data-flow perspective for business process management. Information Systems Research 17(4), 374–391.

TERVEEN L (1995) An overview of human–computer collaboration. Knowledge-Based Systems 8(2–3), 67–81.

TOPI H, LUCAS W and BABAIAN T (2005) Identifying usability issues with an ERP implementation. In Proceedings of the International Conference on Enterprise Information Systems (ICEIS-2005), pp 128–133.

TOPI H, LUCAS W and BABAIAN T (2006) Using informal notes for sharing corporate technology know-how. European Journal of Information Systems 15(5), 486–499.

VAN DER AALST WMP ET AL. (2007) Business process mining: an industrial application. Information Systems 32(5), 713–732.

VAN DER AALST WMP (2010) Process discovery: capturing the invisible. IEEE Computational Intelligence Magazine 5(1), 28-41.

VAN DER AALST WMP, PESIC M and SONG M (2010) Beyond process mining: from the past to present and future. In Proceedings of the 22nd International Conference on Advanced Information Systems Engineering, pp 38–52, Hammamet, Tunisia.

VAN DER AALST WMP (2011) Process Mining: Discovery, Conformance, and Enhancement of Business Processes. Springer, Heidelberg.

VENABLE J, PRIES-HEJE J and BASKERVILLE R (2016) FEDS: a framework for evaluation in design science research. European Journal of Information Systems 25(1), 77–89.

WONG W-P, VENEZIANO V and MAHMUD I (2015) Usability of enterprise resource planning software systems: an evaluative analysis of the use of SAP in the textile industry in Bangladesh. Information Development 32(4), 1027–1041.

ZIMMERMAN J, FORLIZZ J and EVENSON S (2007) Research through design as a method for interaction design research in HCI. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, pp 493–502.
