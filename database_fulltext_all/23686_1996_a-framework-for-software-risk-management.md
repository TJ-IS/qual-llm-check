---
otero_id: 23686
otero_key: "7PRWGQ8X"
title: "A Framework for software risk management"
authors: "Kalle Lyytinen; Lars Mathiassen; Janne Ropponen"
year: "1996"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1996.2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Journal of Information Technology (1996) 11, 275–285

# A framework for software risk management

KALLE LYYTINEN

Department of Computer Science and Information Systems, University of Jyväskylä, 40100 Jyväskylä, Finland

LARS MATHIASSEN

Institute for Electronic Systems, Aalborg University, 9220 Aalborg, Denmark

JANNE ROPPONEN

Nokia Telecommunications, Cellular Systems, Network Management Systems, 33100 Tampere, Finland

We present a simple, but powerful framework for software risk management. The framework synthesizes, refines, and extends current approaches to managing software risks. We illustrate its usefulness through an empirical analysis of two software development episodes involving high risks. The framework can be used as an analytical device to evaluate and improve risk management approaches and as a practical tool to shape the attention and guide the actions of risk managers.

## Introduction

Considerable hopes in improving the performance in software development have been placed in techniques and guidelines that identify, analyse and tackle software risks (Alter and Ginzberg, 1978; Davis, 1982; McFarlan, 1982; Burns and Dennis, 1985; Boehm, 1989; Boehm, 1991; Fairly, 1994). Software risks are incidents that endanger a successful development process leading to wrong or inadequate software operation, software rework, implementation difficulty, delay or uncertainty (Boehm, 1991). They involve the concept of a consequence which incurs losses, is uncertain and introduces choice (Boehm, 1989; Charette, 1989; Barki et al., 1993).

Research on software risk management has primarily focused on crafting guidelines for specific tasks (Alter and Ginzberg, 1978; McFarlan, 1982; Boehm, 1989; Charette, 1989). This has led to a number of problems. First we have little empirical evidence of the practical usefulness of risk management. Second, risk management approaches shape the attention and guide the actions of risk managers in quite different and ad hoc ways. Third, risk management approaches have largely ignored the organizational environment in which they are used and their impact on management performance.

Our research on software risk management attempts to address these issues. We have studied risk management practices (Ropponen, 1993; Ropponen and Lyytinen, 1993); see also (Van de Swede and Van Vliet, 1993; Neo and Leong, 1994;) and we have conducted experiments with risk management approaches (Mathiassen et al., 1995); see also (Boehm et al., 1984). In addition, we have evaluated and compared classical approaches to risk management (Lyytinen et al., 1994). This paper is based on the insights from these studies with the goal to present a general characterization of software risk management as a distinct form of organizational behaviour. The framework we present is general enough to cover the entire development process and comprehensive enough to integrate all types of software risks and it can be used both as an analytical device to evaluate, compare and develop risk management approaches and as a practical tool for software risk managers.

The paper is organized as follows. First, we introduce three complementary organizational views on software development. These are synthesized into a framework for software risk management. We use the framework to analyse software risk management and to provide a general understanding of the literature on risk-based software management. We then present two real-life software episodes to illustrate the value of the framework in making sense, organizing and re-interpreting software management practices. Finally, we discuss some implications for research and practice in software risk management.

## Organizational perspectives on software development

Contemporary approaches to software risk management share a number of fundamental weaknesses (Lyytinen et al., 1994). First, they rely on simplistic environmental models and make no distinctions between different types of risk-generating contexts.

Second, they guide action through ad hoc lists of risk resolution techniques that provide a rather weak understanding of the nature of risk management behaviour. Third, they shape the attention of risk managers through specialized or narrowly focused lists of risk factors. We introduce three complementary organizational perspectives on software development. Each perspective is designed to overcome one of these weaknesses.

## A hierarchical view of software development

Software development embraces three environments: the system environment in which the software system is to operate, the development environment in which the development takes place, and the management environment which shapes software management activities. The development process is generated within the development environment. Its purpose is to inquire into the system environment, anticipate effective ways to use software and thereafter implement the software system. The software management process forms a second-order process that manages the software development process and its environment. It is generated within the management environment. The concern of this process is to design and sustain an effective development environment so that the first-order process meets its goals. The practical reasons for introducing the three environments and the two related processes are: the dynamics of organizational learning, the management of complexity through separation of organizational concerns, and the management of organizational uncertainty.

Software risks are borne: 1) within the system environment, e.g., users might have no experience using the kind of software being developed (Alter and Ginzberg, 1978; McFarlan, 1982); 2) within the development environment, e.g., developers lack experience in analysing this kind of system environment (Alter and Ginzberg, 1978; Davis, 1982; Barki et al., 1993); or 3) within the management environment due to managers' bias, laziness, ignorance or inaction which leads to ignoring available information (Keil, 1995).

## Software development as satisfying behaviour

Software development is concerned with designing artifacts. Such design activities fall short of completely rational behaviour in which knowledge of the environments is certain and consequences of all acts can be calculated (Simon, 1979; Parnas and Clemens, 1986). A software developer can at best try to discover satisfactory solutions in relation to some aspiration levels and adjust designs on the basis of his or her information about the environments and available heuristics at hand. Alternatives are neither given or readily at hand and the concept of search governed by heuristics is, as a consequence, essential in understanding design and management activities.

Software risks are created by limited resources, skills or information. These handicaps prevent designers successfully seeking or selecting design alternatives, estimating their usefulness, or implementing them effectively. Risk-based management is a means to derive more information about the three environments. Thereby actors decrease environmental uncertainty (i.e., increase actors' knowledge) so as to decide which alternative actions to pursue (i.e., increase actors' intelligence), and dynamically set the aspiration levels (i.e., increase design adaptability). Risk management methods specify search procedures for information gathering, organization and interpretation to simplify complex decisions under conditions of bounded rationality (Simon, 1983).

## The structure and dynamics of the environments

Whilst the concept of satisfying behaviour is intuitively appealing it does not help much in characterizing the content, size and the structure of search spaces. We need to describe the structure and dynamics of the three environments of software development. We use Leavitt's model of organizational change (1964) to frame the scope and structure of Simonian search spaces in the context of software development. Leavitt's presentation is appealing since it addresses organizational change and uncertainty in a general, but simple manner. Leavitt argues that organizations are multivariate systems consisting of four interacting variables – task, structure, actor, and technology. Leavitt uses the term task to denote organizational raison d'être such as manufacturing and servicing. By structure Leavitt means systems of communication, systems of authority and systems of work flow. Actors refer to those participants involved that carry out tasks, and technology is defined as any technical means, know-how and tools to carry out tasks. According to Leavitt, these four variables are highly interdependent and a change in one variable will result in changes in the others.

Software risks arise whenever unexpected threatening or conflicting states occur in or between the four components in any of the three environments so as to increase the likelihood of major loss (Lyytinen et al., 1994). Likewise, a risk reduction strategy can change any of the four variables in the environments. Leavitt's model suggests a systematic way to organize risk identification and resolution activities which is an improvement over earlier, mostly ad hoc check lists (e.g., Alter and Ginzberg et al., 1978; Davis, 1982; McFarlan,

1982; Boehm, 1989; Barki et al., 1993). It also articulates some necessary and sufficient features of organizations that effectively cope with software risks. Finally, it clarifies the nature of software risks by relating them to the turbulence and the lack of equilibrium in the socio-technical system.

## A framework for software risk management

By marrying the Simonian model of behaviour (process view) with the Leavittian model of an organization (structural view) in the context of the hierarchical software development model we obtain the framework depicted in Figure 1. It meets some of the requirements we have set for a framework for software risk management: it is simple, general and comprehensive (cf., Lyytinen et al., 1994).

The framework describes the three software development environments symmetrically in terms of the Leavittian model: on each level we distinguish a qualitatively distinct set of tasks, technology, actors and structures. Their constellations can either create or reduce software risks depending on how they are pasted together and what types of behaviours they are able to portray. The differences in the Leavittian components on each level are exhibited by the use of distinct names for the components as exhibited by the terms 'system', 'project', and 'management', respectively. The model recognizes that the three layers of socio-technical systems are closely intertwined by the two change processes that share properties of bounded rationality: the development process and the risk-based management process.

The risk-based management process deals with questions like: do software developers have any experience with the technological platform of the project? It thereby conducts a risk analysis of states and events that may affect the capability of the development environment to carry out the software development task within the set aspiration level (Boehm, 1989; Charette, 1989; Boehm, 1991). It can (often unconsciously) change the development environment by enacting heuristics. For example, it can launch experiments with the technological platform. Through such risk resolution activities (Boehm, 1989; Charette, 1989) one or all of the environments will change (Boehm, 1989).

Software risks can be seen to condense into project specific risk profiles. Such profiles are continually shaped by component interactions and changes introduced by the risk-based management process. In different project stages risk profiles vary, and at each development stage the risk profile contains several incidents which can prevent the project from meeting its aspiration levels and thus incur losses.

![](/api/attachments/7PRWGQ8X/fulltext/images/8f77d7b956b8d4212afb7013a23fbb159fd7bb9cd66e1695fbcaa09fb17168ce.jpg)  
Figure 1 A framework for software risk management

Risk profiles can be attacked in two ways: actively and skillfully where actors carefully scan the environments, feel responsible and committed, and willfully change aspiration levels; or passively by ignoring risks due to lack of accountability, insufficient organizational commitment, incompetence, information overload, stress, opportunism or laziness. In the latter situation the aspiration levels decreased de facto and ex post with-out introducing an explicit choice. These two extreme strategies to deal with software risks – an active and systematic one, and a passive, laissez-faire and ad hoc one – are highly dependent on how the actors, technology and structure in the management environment are joined together.

## Project task

The system environment constitutes the context in which one has to understand the project task. The task is to describe a system environment in relation to stakeholders' expectations and – within specific time and cost constraints – to develop and implement a new software system by changing the necessary components of the system environment. Task related risk resolution techniques should not just address the project task as an abstract formulation of the project outcome and its aspiration level. Instead, a full repertoire of heuristics should be available to probe system environment components and their interactions. Some typical questions asked during risk identification are summarized in Table 1 (Mumford, 1983; Lyytinen and Hirschheim, 1987; Boehm and Ross, 1989; Lyytinen et al. 1994).

Table 1 Project task relates to system environment risk factors

<table><tr><td>System task</td><td>Is the task well understood?Is the task unstructured with many exceptions?How many tasks are included?What is the impact on user tasks?Will actors be critically dependent on the system?Is there much unarticulated, tacit knowledge involved?What is the extent of tasks?How much variation and flexibility are involved in the tasks?</td></tr><tr><td>System structure</td><td>Is the structure of the organization fit for the system?Does the system span over several organizational units?Does the system structure change rapidly?Do power relations change?Is the structure in harmony with the tasks?</td></tr><tr><td>System technology</td><td>Is the technology appropriate for the tasks?Is the technology well-proven and reliable?What is the life-span of the technology?Is the technology new in this organization?Is the technology standardized or changing fast?Is the cost of the technology prohibitive?</td></tr><tr><td>System actors</td><td>Do the actors have experience with the technology?Are their earlier experiences with IT bad?How knowledgeable are the actors?Are their expectations realistic?Do actors personally benefit from the change?</td></tr></table>

## Project structure

This component refers to the systems of communication, authority and work flow. Systems of communication specify who should be communicating with whom, when, how frequently communications take place, and how formal communications are (Andersen et al., 1990; Davis et al., 1990). Risks transpire when actors communicate ineffectively, when the appropriate actors are not involved in communications, or when the scope of communications is limited (Curtis, et al., 1988; Heiskanen, 1994). The systems of authority define lines of responsibility between project actors and groups. The more unclear and inappropriate the allocation of responsibilities, the more risks are produced (Lyytinen et al., 1994); if the selected organizational form is in disagreement with the actors' expectations and the nature of the task new risks are created (Constantine, 1993); in addition, the risk profile changes when the work flow structure does not match the task.

## Project technology

Project technology includes available methods, tools and infrastructure to design the software system and eventually to implement it. System development methods, quality assurance systems, computers, software, and other equipment are examples of such technologies (Cooprider and Henderson, 1991). Technological shortcomings and the dynamic nature of the technology are indisputable sources of risk. Typically, the technological conditions under which the task is carried out change and these changes amplify existing weaknesses in the technology including its inadequate functionality, reliability, efficiency, or user-friendliness.

## Project actors

Project actors cover all stakeholders who are involved in the process or can set forward claims to or benefit from the project. Thus, all participating persons, groups, and other stakeholders including customers, managers, maintainers, development groups and users (Boehm et al., 1989) need to be included into the actor set. Actors exhibit several prominent properties that influence a project's risk profile: knowledge and skills, experience, expectations and commitments, and beliefs and values. All these can very from one actor (group) to another. Moreover they can vary relative to an actor's task, and his or her connection to the project structure and technology.

## Project component interactions

Second order considerations examine interactions between task, structure, technology, and actors as major sources of risks. Examples of such considerations are: actors' ability and shortcomings in performing the task, the appropriateness of the structure and the technology in relation to the task, the effectiveness with which the structural arrangements support and utilize the actors' abilities, skills and experience in using the technology, and finally the fit between technology and structural arrangements (Lyytinen et al., 1994).

Table 2 Generic questions to support risk-based management

<table><tr><td></td><td>System</td><td>Project</td><td>Management</td></tr><tr><td>Task</td><td>Which tasks are the software system supporting?</td><td>What are the requirements to the system and its environment?</td><td>What is an appropriate project environment?</td></tr><tr><td>Structure</td><td>Which organization is the software system part of?</td><td>How is the project organized?</td><td>How are the management activities organized?</td></tr><tr><td>Technology</td><td>Which technical platform is the software system implemented on?</td><td>Which technologies are used to develop the software system?</td><td>Which technologies are used to manage the project?</td></tr><tr><td>Actor</td><td>Who are using the software system or affected by it?</td><td>Who are involved in or affected by the project?</td><td>Who are involved in managing the project?</td></tr><tr><td>Relations</td><td>How is the fit and what is the dynamics between components?</td><td>How is the fit and what is the dynamics between components?</td><td>How is the fit and what is the dynamics between components?</td></tr></table>

## Risk-based software management

The performance of the management environment (cf., Figure 1) depends on how actors, structure and technology in the management environment are assembled. Such performance is defined by the available information processing capability to find out critical incidents, to suggest alternatives, to calculate consequences and thereby to resolve software risks.

## Management task

The risk-based management task is to search for incidents that can prevent the development environment from performing in a satisfactory manner and to modify the development process by intervening into the development environment. This is indicated by the big arrow pointing downwards from the management environment in Figure 1. Software risks are born in all three environments. Table 2 offers a set of generic questions that can be used to search for specific risks in a software project. Table 1 offers more specific questions focusing on the system environment and hence related to the project task.

The risk-based management task is dynamic: it differs through project phases and between development projects and it involves a feedback loop indicated by the small arrow. Through this loop managers become more competent and experienced, the organization integrates new experiences and schemes into its systems of interpretation (Weick and Daft, 1983), and new methods, codifications of procedures, and decision making rules are adopted.

We can observe a large variation in how the risk management task is formulated and accomplished. Sometimes risk-based management forms an integral part of the project management activities. This corresponds to the continuous view of risk management advocated by Boehm (1989); Boehm and Ross (1989); Boehm (1991); and Alter and Ginzberg (1978). Sometimes risk-based management forms a discrete event which relates only to the very early phases of a software project. This corresponds to the discrete view risk management presented by David (1982) and McFarlan (1982).

## Management actor

Risk managers are expected to take deliberate actions to tackle risks. Usually this role is assigned to a project manager. But other project members and groups such as project committees can also carry out risk management tasks. Risk managers form a proactive part of the management environment: they decide what actions should be taken, what risk management technologies should be used, and how the management structure should be organized. They also set the aspiration levels that are honoured during searches and consequent risk resolutions.

Finding skilful, open-minded software managers is instrumental in improving the risk management capability (Boehm, 1989; Van de Swede et al., 1993). Actors' attitudes, psychological make-up and cognitive bias can drastically affect the way in which they deal with software risks. This has been pointed out by such actor features as 'escalating commitment' (Keil, 1995), 'no-problem syndrome' (Weinberg, 1986), 'group think', and 'inaction' (Weick, 1979). Actors' capability can be improved by increasing their awareness of risk management methods, improving their ability to use the methods, and forging values and preferences that deliberately recognize risks, esteem high quality and the lack of errors (cf., Boehm and Ross, 1989; Roberts, 1993; Keil, 1995).

## Management technology

Risk management methods offer heuristics to identify risks, compose a risk profile, evaluate its significance and attack it accordingly. These methods form the Simonian ‘intelligence’ that can be transformed from one environment to another. Most of these methods are codified representations of good management practices. Willcocks and Margetts (1994) convincingly demonstrate that conventional risk management technologies tend to ignore external factors that affect the risk management capability. These include: history like the past performance that shapes actors’ expectations; external structural factors like external pressures, constraints, and omissions; internal structural factors like the misfit between the organizational and IS management structure; and actor related features like past experience, culture and climate (Keil, 1995).

## Management structure

Communication lines, the structure of authority, and lines of accountability are significant in organizing the risk-based management process. It is important to effectively communicate risks to everyone involved and to reward reporting of omissions and errors (Keil, 1995). It is also necessary to define systems of authority for tactical considerations on which risk resolution strategies to apply when (Boehm and Ross 1989). The management structure is also important to create a sense and discipline of accountability, i.e., that quality makes a difference and that actors are accountable for what they are doing (Rochlin, 1993). At the same time, the management structure must be organized to provide adequate and reliable information and a management structure which favours openness and does not punish voicing of problems and concerns (Keil, 1995).

## Interactions and improvements

The intrinsic and complex relations between the four Leavittian elements are expressed in questions like: how do technologies relate to specific management tasks? what level of experience and competence do the involved actors have in using these technologies? who is responsible for managing these risks and when? Software organizations' effectiveness can be nurtured over time by perfecting the quality of some, or all components, in the management and development environments. Such developments, however, are not the subject of project management, but one important target in managing and orchestrating the larger environment for software delivery (Earl, 1989). Analysis of such changes has taken place in discussions of evolutionary models of IT diffusion (Lyytinen, 1991). These models are often called maturity models. The weakness of such models is their primary focus on well-defined processes of managing complexity and what could be called lubrication of the organizational machine. As a consequence they tend to ignore the importance of an organic focus to deal effectively with high levels of complexity and uncertainty. But despite their weaknesses, maturity models have a definite value in distinguishing successive levels of how the development capability can mature over time (Nolan, 1973; Humphrey, 1989; Galliers and Sutherland, 1991). Thereby, through successive trials of analysis of weaknesses, maturity models can be used to diagnose what organizations have learned (i.e., their current level of intelligence in Simonian terms) in managing software risks, and to point out that organizations must continually improve their risk management capability (i.e., the necessity to learn to learn (March et al., 1991).

## Two cases

In the following, we use the framework to structure and interpret two software development episodes involving considerable risks. In case Alpha, risk management techniques were actively applied and the management environment was organized accordingly. In case Beta, no conscious risk management strategy was followed. We analysed both cases using published written descriptions (Gjesing, 1993; Markus and Keil, 1994; Keil, 1995). In addition, we have communicated with the original authors and checked that our interpretations are authentic and valid. Our primary goal is to illustrate the value of the framework in making sense, organizing and re-interpreting software risk management practices.

In case Beta, the risk profile was never fully established. The system environment was, however, a major

## Software risk management

source of risks and continued to be so throughout the project. At the same time a management structure was installed that did not match with the risk levels and it was populated with actors that were cognitively and emotionally biased. Accordingly, the management environment was never in equilibrium with the risk based management task and it was handled with an inappropriate assembly of actors, management structure and technology. In contrast, risk management was carried out consciously as a kind of one-shot strategy in case Alpha. Risk information was sought, structured and at the end analysed using quantitative tools. This activity was carried out by an individual project manager. Risks arising from all three environments were systematically detected and planned for and, despite initially high levels of risks, the development process could be managed better than usual.

## Case Alpha: advanced banking system

The project task was to develop a general filing and retrieval system for a large bank which would facilitate coordination between bank employees while working on the same customer case (Gjesing, 1993). Another goal was to establish homogeneous working procedures for dealing with customer cases. The overall task was of medium size (approximately 12 man years) and it involved a fair amount of technological novelty and complexity.

The system environment is a large bank. Relevant system actors are the entire bank personnel who are eventually going to use the system. The system structure reflects the division of work and employed coordination mechanisms to manage customer cases. The system (task) stores and retrieves files on customer cases on which the personnel are currently working. The system technology consists of the bank's existing computing facilities supplemented with a new file management system and an electronic mail system.

The development process was split into two stages because of the newness of technology components and the necessary changes in system structure. The timing and quality constraints for the task were tight. During the project's first year a prototype was to be developed and tested within a limited functional area. Based on the experiences gained from this prototype a full-scale system was then to be developed over a period of another two years. The first experimental stage was, as a consequence, crucial for the success of the whole project as further developments depended on the outcomes of this initial stage.

The development environment covers part of the bank's IS department, an organization with about 800 employees operating at two different sites. Both sites develop and maintain the same computing infrastructure and no clear functional division had been made between the sites. The project actors in this case were the project manager accompanied by other project members and user representatives. Overall the project was staffed by 10 full time members. The project structure forms a complex organizational web, because the project members had to be obtained from two departments representing both sites of the IS department, and user representatives from several functional areas. The project technology consisted of the system technology and a new object oriented methodology and a new CASE tool. The project task, in the first stage of the project, was to develop the prototype, to garner sufficient experiences from the design, implementation and use of it, and to produce information for making decisions regarding the continuation of the project.

The project manager worked in a specific management environment. He conducted a risk analysis and managed the development process based on this information. The project manager was inexperienced with managing projects of this size but he was willing to follow risk management principles and committed to the management process. Parts of the risk analysis were conducted in team meetings using the risk analysis steps suggested by Boehm (1989). The risk management technology was the method suggested by Boehm (1989, 1991) and the management structure was based on traditional project management principles.

The project manager saw several threats including new technology, complex project organization, and a new application area. Therefore he executed risk-based project planning in two steps (Boehm, 1989, 1991): 1) risk assessment step – consisting of risk identification, risk analysis, and risk prioritization; and 2) risk control step – consisting of risk management planning, risk resolution, and risk monitoring. During risk assessment, a list of 29 risk items were compiled using Boehm's top-ten list. It was supplemented with informal discussions with colleagues, the use of rich pictures (Checkland, 1981), soliciting past project experience, and conducting a detailed analysis of the system requirements and success factors. Each risk was further analysed carefully in relation to the short term goals of the project and assessed quantitatively.

The risk profile included risks associated with: the project task (insufficient requirements, generality of the design); project technology (new CASE tool, difficulty in the implementation of the basic file system and electronic mail system, inefficient automatically generated code); project actors (inexperienced project manager); project structure (technical subcontracts, considerable coordination effort, tight schedule), and actor-technology fit (project members inexperienced with object oriented methodology). Subsequently, risk control activities were carried out with emphasis on risk management planning. Risk resolution tactics were evaluated, further designed, and integrated into the project plan.

The project manager found that this approach shed light on the instrumental role of the risk management technology in improving searches, finding useful information, and in structuring the information. He also identified a number of weaknesses: the approach is based on a pessimistic world view and important risks can be neglected because they are mentioned so often (the wolf-is-coming-effect); there is no mechanism for dealing with time; there is no support for which risk resolution strategy to apply and when. These problems indicate weaknesses in pasting together the management environment: actors' cognitive bias (the-wolf-is-coming-effect), poor commitment (pessimistic worldview), lack of structure (time dimension), and poor heuristics (no support for strategy choice). Finally, the project manager argues that these weaknesses can be avoided if one is aware of them (by finding an appropriate technology-actor fit).

## Case Beta: expert system to support sales representatives

The project task was to design and implement an advanced expert system that could be used by the sales force to configure error-free computer systems while drafting customer orders (Markus and Keil, 1994; Keil, 1995). The project was originally welcomed with big fanfare, promised staggering return on investment, had great visibility in the organization's business strategy, and obtained early management commitment. Moreover, the project had good resources, had good technical expertise at hand, and relied on a careful project planning and user participation strategy during the system roll out (Mumford and McDonald, 1989). It also had a number of risk factors that were well recognized from the start such as untried system technology, unique application area, and inexperienced users. The project task was large in size (over 100 man years), its complexity was high, and its implementation scope was broad (Mumford and McDonald, 1989).

The system environment is part of a large computer vendor. The relevant system actors are mainly the vendor's sales-representatives who were expected to use the system as a tool to configure the systems they sold. The idea originated from the manufacturing department which realized that most configuration errors are borne in sales and that their expert system used in configuring the manufactured systems could be leveraged also to provide configuration support for sales. The sales department, however, showed little interest in the project originally and was during the initiation of the project developing its price quotation system which it saw as a strategic application (Markus and Keil, 1994). The system structure reflects the traditional division of work in the sales organization. The system task is to prompt a series of questions about the system being sold and thereafter to configure it correctly by looking for mismatched items and components, to lay out processors and other components in cabinets, to lay out the floor plan, and to do the cabling. The system technology consists of standard hardware available from the vendor, proprietary expert system software to build up the data and rule base, and telecommunication facilities available for the sales-offices. Part of the system technology was not tested before.

The development process consisted of the initial design and implementation phase which lasted from late 1980 to end of 1983. During that period the system was designed, implemented and piloted among a number of our user representatives. Piloting was found necessary to test out the technology and to get users involved. The second, roll out, phase lasted from late 1983 until late 1992. During this period the system was continually adapted and modified and its deficiencies and implementation hurdles were attacked through several larger or smaller implementation measures. After a solid start the project faced chronic implementation problems, despite several extensions and improvements in software, until it was abandoned.

The development environment includes the company's sales offices and representatives and during its peak the project staff consisted of 26 technical specialists and management staff. The project structure is complex. It involves the management of the technical system implementation, users through user design teams and coordination with changes in company's organization, product lines, strategy, sales channels and campaigns. The project technology is basically the same as the system technology mentioned above. It was familiar to the technical implementors. The initial project task was to finish the project by December 1982 (Keil, 1995).

The management actors are the project managers and other managers involved in making decisions. Most of these were not knowledgeable in developing this kind of system. Those who had experience had not been involved in a similar type of development effort. The management structure was designed so that few people controlled both the development resources and the auditing of system outcomes (Keil, 1995). The management structure did not specify responsibilities and lines of communication clearly which later led to ignoring available information and misinforming higher levels of management. The organization had, however, experience in successfully managing projects of this size. In addition, the project strategy suggested active user participation in designing the use of the system. The project was, in summary, not specifically badly managed when compared to other more successful projects in the organization.

Nonetheless, the project did not apply any risk management technologies and management actors constantly ignored available signals on system risks. A project risk profile was never systematically constructed though some risks were identified such as the novelty of the system technology and organizational implementation difficulty. No specific plans to reduce these risks were devised. During the course of the development process new risks emerged including wrong understanding of sales-representatives' work, poor or lacking functionality, an inadequate and cumbersome user-interface, poor data quality, slow performance, need for linkages with other company's applications and too tight deadlines (Keil, 1995; Markus and Keil, 1994). Some of these – especially lack of linkages to other applications, lacking functionality and the inappropriate fit between the system structure and system task (Markus and Keil, 1994) – were, at the end, fatal for the system.

## Conclusion

We have presented a framework for software risk management and we have used it to: i) describe the nature of software risk management, ii) provide a general understanding of the literature on risk-based software management, iii) interpret software episodes involving high risks, and iv) provide generic checklists covering the space in which software risks are born. The framework should not be seen as a traditional testable model. Instead, the framework presents, in relation to the published literature so far, a wider and more systematic way to organize software risk considerations.

The framework sheds light on areas to improve software production. Organizations should be attentive to risky incidents that can help to change behaviours and beliefs and the use of risk management methods should be encouraged. Risk management considerations should cover all the four components – task, structure, technology and actor – in all three environments. Table 2 offers a survey of key generic questions that define the space in which specific software risks are born, and Table 1 provides more specific questions related to the identification of risks in the system environment.

Such checklists and other risk management methods provide a fast approach to improve the risk management ability of a software organization. Changes in the other components of the management environment are outcomes of evolutions unfolding over longer periods of time: hiring new people, changing organizations' competencies, skills and beliefs, or restructuring the management and development practices. Such drastic interventions pay off only over longer periods of time but then, in most cases, they do pay off more handsomely.

## Acknowledgements

The authors are thankful for useful comments from the editors and reviewers and for discussions with Michael Gjesing, Mark Keil, Karleen Roberts, and Roy Schmidt.

## References

Alter, A. and Ginzberg, M. (1978) Managing uncertainty in MIS implementation. Sloan Management Review, Fall 20(1), 23–31.

Andersen, N. E., Kensing, F., Lundin, J., Mathiassen, L., Munk-Madsen, A., Rasbech, M. and Sørgaard, P. (1990) Professional Systems Development: Experience, Ideas and Action, (Prentice Hall, Hemel Hempstead, Hertfordshire).

Barki, H., Rivard, S. and Talbot, J. (1993) Toward an assessment of software development risk. Journal of Management Information Systems, 10 (2), 203–25.

Boehm, B. W. (1989) Software Risk Management. Tutorial, IEEE Computer Society Press, Los Alamitos, California.

Boehm, B. W. (1991) Software risk management: principles and practices. IEEE Software, January 12, 32–41.

Boehm, B. W., Gray, T. and Seewaldt, T. (1984) Prototyping versus specifying: a multiproject experiment. IEEE Transactions on Software Engineering, 10 (3).

Boehm, B. W. and Ross, R. (1989), Theory-W software project management: principles and examples IEEE Transactions on software engineering, 15 (7), 902–16.

Burns, R. and Dennis, A. (1985) Selecting an appropriate application development Database, Fall, 17, 19–23.

Charette, R. N. (1989) Software Engineering Risk Analysis and Management (Intertext Publications, McGraw-Hill, New York).

Checkland, P. (1981) Systems Thinking, Systems Practice (John Wiley, Chichester).

Constantine, L. (1993) Work organization: paradigms for project management and organization Communications of the ACM, 36 (10), 32–43.

Cooprider, J. G. and Henderson, J. C. (1991) Technology – process fit: perspectives on achieving prototyping effectiveness. Journal of Management Information Systems, 7(3), 67–87.

Curtis, B., Krasner, H. and Iscoe, N. (1988) A field study of the software design process for large systems. Communications of the ACM, 31 (11), 1268–87.

Davis, G. B. (1982) Strategies for information requirements determination. IBM Systems Journal, 21 (1), 4–30.

Davis, G. B., Lee, A. S., Nickles, K. R., Chatterjee, S., Hartung, R. and Wu, Y. (1990) Diagnosis of an Information System Failure: A Framework and Interpretive Process, Management Information Systems Research Centre, WP-01-06, University of Minnesota.

Earl, M. (1989) Management Strategies for Information Technology (Prentice Hall, London).

Fairly, R. (1994) Risk management for software projects. IEEE Software, 11 (3), 57–67.

Galliers, R. D. and Sutherland, A. R. (1991) Information systems management and strategy formulation: the 'stages of growth' model revisited. Journal of Information Systems 1 (2).

Gjesing, M. V. (1993) Risk-based Project Management-An example. The Danish Bank Academy (in Danish).

Heiskanen, A. (1994) Issues and Factors Affecting the Success and Failure of a Student Record System Development Process - a Longitudinal Investigation Based on Reflection-in-Action. PhD Dissertation, Department of Computer Science, University of Tampere.

Humphrey, W. S. (1989) Managing the Software Process. Software Engineering Institute, The SEI Series in Software Engineering (Addison-Wesley, Reading, Mass., USA).

Keil, M. (1995) Pulling the plug: software project management and the problem of project escalation. MISQ 19(4), 421–47.

Leavitt, H. J. (1964) Applied organization change in industry: structural, technical and human approaches in, Leavitt, H. J. (ed), New Perspectives in Organizational Research (John Wiley, Chichester), 55–71.

Lyytinen, K. (1991) Penetration of information technology in organizations: a comparative study using stage models and transaction costs. Scandinavian Journal of Information Systems, 3, 87–109.

Lyytinen, K. and Hirschheim, R. (1987) Information systems failures – a survey and classification of the empirical literature. Oxford surveys in Information Technology Vol 4., (Oxford University Press, Oxford), 257–309.

Lyytinen, K., Mathiassen, L. and Ropponen, J. (1996), Attention shaping and software risk – A categorical analysis of four classical approaches, submitted for publication.

March, J., Sproull, L. and Tamuz, M. (1991) Learning from samples of one or fewer. Organization Science, 2 (1), 1–13.

McFarlan, W. (1982) Portfolio approach to information systems. Journal of Systems Management, January 33(1), 12–19.

Markus, L. and Keil, M. (1994) If we build it, they will come: designing information systems that users want to use. Sloan Management Review.

Mathiassen, L. Seewaldt, T. and Stage, J. (1995) Prototyping and specifying: principles and practices of a mixed approach. Scandinavian Journal of Information Systems, 7(1), 55–72.

Mumford, E. (1983) Designing Human Systems (Manchester Business School, Manchester).

Mumford, E. and McDonald, B. W. (1989) XSEL's progress – the continuing journey of an expert system (John Wiley, Chichester).

Neo, B. S. and Leong, K. S. (1994) Managing risks in information technology projects: a case study of TradeNet. Journal of Information Technology Management, May 5(3), 29–45.

Nolan, R. L. (1973), Managing the computer resource: a stage hypothesis. Communications of the ACM, 16 (7), 399–405.

Parnas, R. and Clemens, P. (1986) A rational design process: how and why to fake it. IEEE transactions on Software Engineering, SE-12, (2), 251–7.

Roberts, K. ed. (1993) New Challenges to Understanding Organizations, (Macmillan, New York).

Rochlin, G. (1993) Defining ‘high reliability’ organizations in practice: a taxo-nomic prologue, in New Challenges to Understanding Organizations, Roberts, K. (ed) (Macmillan), 11–32.

Ropponen, J. (1993) Risk Management in Information System Development, Licentiate thesis, Department of Computer Science and Information Systems, University of Jyväskylä, Finland.

Ropponen, J. and Lyytinen, K. (1996) How Software Risk Management Can Improve Systems Development: An exploratory Study, accepted for publication in European Journal of Information Systems.

Simon, H. (1979) Rational decision making in business organizations. American Economic Review, 69 (4), 493–513.

Simon, H. (1983) Theories of Bounded Rationality, Behavioural Economics and Business Organization, Vol. 1–2 (MITT Press, Cambridge), 160–176.

Willcocks, L. and Margetts, H. (1994) Risk assessment and information systems. European Journal of Information Systems, 3 (2).

Weick, K. (1979) The Social Psychology of Organizing (Addison-Wesley, Reading, MASS).

Weick, K. and Daft, R. (1983) The effectiveness of interpretation systems, in Organizational Effectiveness: A Comparison of Multiple Models, Cameron K. and Whetten D. (eds) (Academic Press, New York).

Weinberg, G. M. (1986) Becoming A Technical Leader - An Organic Problem Solving Approach (Dorset House Publishing).

Van de Swede, V. and van Vliet, J. (1994) Consistent development: results of a first empirical study on the relation between the project scenario and success, in Proceedings of the 6th CAiSE conference, Wijers, G. and Brinkkemper, S. (eds), (Springer Verlag, Uttrecht, The Netherlands), 80–93.

## Biographical notes

Kalle Lyytinen is a professor in Information Systems at the University of Jyväskylä, Finland. He currently serves on the editorial boards of Information Systems Journal, European Journal of Information Systems, Accounting, Management and Information Technology, MIS Quarterly, Information Systems Research, Information Technology & People, Requirements Engineering Journal and Journal of Strategic

## Software risk management

Information Systems. He has published over 70 articles and edited or written six books. His research interests include information system theories, system design methods and tools, information system management, electronic commerce, computer supported cooperative work and diffusion of complex standardized technologies.

Janne Ropponen holds a masters degree in computer science and information systems and a licentiate degree in economic sciences from the University of Jyväskylä. His research activities centre around information technology projects and especially managing software development risks. These form the topic of his dissertation work. He currently works as a senior process development engineer at Nokia Telecommunications Ltd where he is responsible for requirements and risk management practices and their improvement.

Lars Mathiassen is computer science professor at University of Aalborg, Denmark. His research areas are software engineering and information systems, and he has published articles and books on theories, methods and practices related to the development of computer-based information systems. Recently, he has co-authored “Computers in Context – The Philosophy and Practice of Systems Design”, Blackwell 1993, together with professor Bo Dahlbom.

Address for correspondence: Kalle Lyytinen, Department of Computer Science and Information Systems, University of Jyväskylä, 40100 Jyväskylä, Finland.
