---
otero_id: 25532
otero_key: "YTEHWNY4"
title: "Sustainability Design Principles for a Wildlife Management Analytics System: An Action Design Research"
authors: "Shan L. Pan; Mingwei Li; L.G. Pee; M.S. Sandeep"
year: "2021"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2020.1811786"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Sustainability Design Principles for a Wildlife Management Analytics System: An Action Design Research

Shan L. Pan , Mingwei Li , L.G. Pee & M.S. Sandeep

To cite this article: Shan L. Pan , Mingwei Li , L.G. Pee & M.S. Sandeep (2020): Sustainability Design Principles for a Wildlife Management Analytics System: An Action Design Research, European Journal of Information Systems, DOI: 10.1080/0960085X.2020.1811786

To link to this article: https://doi.org/10.1080/0960085X.2020.1811786

![](/api/attachments/YTEHWNY4/fulltext/images/7988adb3f93ef8bc062261d4173efdbcdd77af6d11cb2bce10b97c24e57da73f.jpg)

Published online: 06 Sep 2020.

![](/api/attachments/YTEHWNY4/fulltext/images/a0c2b25c94bb0e59b9324ff6293d7065b4dcf35baf6eb415cccf44b58dc6bd8e.jpg)

Submit your article to this journal

![](/api/attachments/YTEHWNY4/fulltext/images/ed28b8d6cb2c9fa76782d094fbcfec39d9c6bcfac310eef45ac85f77e4408da5.jpg)

View related articles

![](/api/attachments/YTEHWNY4/fulltext/images/67b1af778dacc9989c1eed5eccca0574e7ab8e8daf2214e3369344256244bef4.jpg)

View Crossmark data CrossMark

EMPIRICAL RESEARCH

Check for updates

# Sustainability Design Principles for a Wildlife Management Analytics System: An Action Design Research

Shan L. Pan<sup>a</sup>, Mingwei Li <sup>b</sup>, L.G. Pee <sup>c</sup> and M.S. Sandeep <sup>a</sup>

<sup>a</sup>School of Information Systems and Technology Management, The University of New South Wales, Sydney, Australia; <sup>b</sup>Qingdao University, Business Shool, Qingdao, China; <sup>c</sup>Wee Kim Wee School of Communication and Information, Nanyang Technological University, Singapore, Singapore

## ABSTRACT

Wildlife management is becoming increasingly critical to improving the sustainability of biodiversity and the welfare of human beings. This paper uses afordance as a lens to explore the design of information systems that can assist in managing wildlife in protected areas. Through an action design research (ADR) study with a forest department, we develop and test design principles for a class of wildlife management analytics system (WMAS). We identify the initial design principles, including elements of the action potential, materiality, and boundary condition, and iteratively refine them based on an instantiation of WMAS through two iterations of design and implementation cycles. Through our work, we contribute to design knowledge by abstracting the artefacts, design principles in particular, and the ADR approach by generalising two new activities and corresponding principles when designing analytical models. Our findings can also be used to address a class of similar problems and systems in practice.

ARTICLE HISTORY Received 25 May 2019 Accepted 29 July 2020

KEYWORDS Wildlife management; analytics system; afordance; elaborated action design research

ACCEPTING EDITOR Pär Ågerfalk

ASSOCIATE EDITOR Tuure Tuunanen

## 1. Motivation

Wildlife, as a renewable natural resource, plays significant roles not only in the safeguard of ecological health but also in the creation of economic value through ecotourism development and cultural heritage (Weisenborn, 2018). However, wildlife is currently facing serious threats, especially from those produced by human beings, such as overexploitation, climate change, and urbanisation (Karanth et al., 2012; Samson & Knopf, 1993). All these threats have caused and are still causing wildlife population decline. Wildlife loss is one of the most compelling challenges worldwide and has dramatic impacts on the sustainability of biodiversity and the welfare of human beings (Karanth et al., 2012).

In our research context, forest departments established by the Indian government in each of its 29 states play a vital role in managing wildlife in protected areas. The departments are responsible for planning and implementing wildlife-related programmes such as wildlife monitoring, anti-poaching and human-wildlife conflict management. Since 2014, one of the forest departments (henceforth, “the department”) has been gathering wildlife-related data through information technologies (e.g., hand-held satellite location devices). As the volume of data continued to increase, the department hoped to create an information system through which they could uncover useful information embedded in their data to manage wildlife efectively. An opportunity arose when one of the authors conducted a field study to understand the use of information technology by the department and eventually co-created a novel analytics system for the region of interest.

The information system (IS) community has been concerned with creating new and innovative artefacts (Arnott & Pervan, 2012; Ågerfalk & Wiberg, 2018; Gregor & Hevner, 2013; Hevner et al., 2004), which have important impacts on practice (Pan & Pee, 2020). A growing number of both practical reports and academic studies have recognised the potential of big data analytics (BDA) in the wildlife management domain (Hampton et al., 2013; Norouzzadeh et al., 2018); however, little prescriptive knowledge exists on how such an analytics system should be designed. The lack of constructive knowledge is not only unconducive to the accumulation and evolution of design knowledge in this domain but also limits practitioners’ capability to derive insights from wildlife-related data. In design science research, the design principle is one of the main forms of design knowledge (Chandra et al., 2015). Accordingly, we consider the following research question:

● What are the appropriate design principles for an analytics system that afords wildlife management?

Therefore, the objective of the paper is to develop and test design principles for a class of wildlife management analytics system (WMAS). To achieve this objective, we attempt to co-create an instantiation of WMAS with an Indian forest department based on the guidelines of the elaborated action design research (ADR) approach (Mullarkey et al., 2019). When designing IT artefacts for humans in practice, we use the concept of afordance, which helps us clarify the relations among designers, artefacts, and users. First, we conceptualise our initial design principles consisting of action, materiality, and boundary conditions (Chandra et al., 2015). Next, we demonstrate and refine these design principles based on an instantiation of WMAS through two iterations of design and implementation elaborated ADR cycles. Two evaluations of the design principles are also conducted within the implementation cycle. Finally, we discuss our results in the form of artefact abstractions.

Through our ADR project, we contribute to research and practice in several ways. First, this study advances the understanding of the problem space (of wildlife management) in terms of three required afordances (i.e., assessing, anticipating, and practising afordances) that were identified from related research and practices. Second, we also contribute to the solution space by developing a set of design principles for the WMAS, which can be used to guide actions for similar problems and systems in a wider range of applications. Third, when designing analytics systems for practice, we contribute to the ADR approach by generalising two new activities of data preparation and algorithm design. Two related principles (i.e., multi-source data integration and human complementing algorithm) in the activities are also elaborated. In practice, the outputs of our research can enhance the capabilities of practitioners in wildlife management.

Our study is structured as follows. In section 2, we provide the theoretical background that focuses on wildlife management, afordance as a lens to study information system design, and analytics and its implications for wildlife management. In section 3, we describe the elaborated ADR approach and the ADR project setting. In section 4, we diagnose the general design requirements of the analytics system in wildlife management. In section 5, we ready our data through the extract, transform, and load (ETL) process. In sections 6 and 7, we describe two iterations of design and implementation cycles, during which both the initial design principles and system features are refined and evaluated. In section 8, we discuss the theoretical and practical contributions of our study, its limitations, and future research directions. Finally, a conclusion is provided.

## 2. Theoretical background

## 2.1. Wildlife management

Wildlife management as an interdisciplinary subject can be defined as the sound management of wildlife species to sustain their populations and habitat over time (Fao, 2014; Sandhyarani, 2018). Generally, there are two main forms of wildlife management: manipulative type and custodial type (Sandhyarani, 2018). In the former, direct (e.g., gamekeeping) or indirect (e.g., altering food supply and habitat) means are adopted to maintain population growth at a sustainable rate (Sandhyarani, 2018). The latter is to protect wildlife populations and their habitats by reducing the external influences caused by humans. It is appropriate for the protected areas such as national parks or reserves, where activities of poaching and grazing are forbidden (Sandhyarani, 2018). Our research context concerns wildlife management in protected areas of India and thus corresponds to the custodial type.

Understanding how to design analytics systems for wildlife management requires the understanding of the background domain, particularly activities that the system should support. To achieve this goal, we explored literature published in biology conservation and management journals. By reviewing the related literature, we identified three main categories of activities in wildlife management, namely, understanding wildlife conditions, identifying external threats from human beings, and patrolling in protected areas. Table 1 summarises these three types of activities.

The three categories of activities demonstrate three key aspects of wildlife management in terms of status, threat, and response. The first type of activity involves understanding the wildlife status, such as the number of remaining wildlife and their distribution (Singh & Kumara, 2006). These activities are the basis of wildlife management because understanding wildlife status can arouse practitioners’ attention to plan their next move. The second type of activity involves identifying the external threats that may cause changes in wildlife status, especially those from humans, such as hunting, poaching, and snaring (Critchlow et al., 2015). The third activity involves patrolling in protected areas. Patrolling is a commonly used way to implement wildlife monitoring and protection tasks. The traditional patrol approach involves walking or driving in a specific area of the nature reserve. Recently, owing to their convenience and eficiency in field investigations, technologies such as camera traps have been widely adopted to assist practitioners in conducting patrol tasks (Tobler et al., 2008).

The biology conservation and management field has made considerable efort to investigate the activities in wildlife management. These studies developed specific solutions in the realm of wildlife status, threat, and response. For example, Singh and Kumara (2006) estimate that approximately 550 grey wolves are distributed within an area of 123,330 square kilometres in India by using the data of wolf dependence and its prey density from a three-year survey. Critchlow et al. (2015) propose a Bayesian hierarchical model that leverages illegal activity data collected by ranger patrols in Uganda to predict their trend and distribution. Tobler et al. (2008) evaluate the eficiency of camera traps in two field experiments. They also provide suggestions on how to make the best use of camera traps under diferent conditions. Recently, some researchers have begun to discuss the potential and applications of big data analytics in wildlife management (Lewis et al., 2018). While these studies contain detailed descriptions of specific solutions to specific activities in wildlife management, they lack generalisable knowledge that can be used to address a class of problems. Our study attempts to generalise design knowledge through the elaborated ADR approach to fill this gap. In doing so, we use the concept of afordance as a lens to design our artefact.

Table 1. Activities in wildlife management and the related literature.

<table><tr><td>Categories</td><td>Activities</td><td>Literature</td></tr><tr><td rowspan="3">Understand wildlife status</td><td>Estimate wildlife population size and wildlife distribution by field investigation</td><td>Singh and Kumara (2006)</td></tr><tr><td>Identify wildlife species automatically</td><td>Norouzzadeh et al. (2018)</td></tr><tr><td>Estimate wildlife population trend and seasonal population density</td><td>Kiffner et al. (2020)</td></tr><tr><td rowspan="3">Identify external threats from human beings</td><td>Assess patterns of human-wildlife conflicts</td><td>Karanth et al. (2012)</td></tr><tr><td>Predict the occurrence of illegal activities</td><td>Critchlow et al. (2015)</td></tr><tr><td>Predict the potential poaching areas</td><td>Xu et al. (2020)</td></tr><tr><td rowspan="3">Conduct patrol in the protected areas</td><td>Identify potential wildlife habitats</td><td>Danks and Klein (2002)</td></tr><tr><td>Instal camera traps to aid rangers&#x27; patrol tasks</td><td>Tobler et al. (2008)</td></tr><tr><td>Make patrol routes through simulation</td><td>Xu et al. (2020)</td></tr></table>

## 2.2. Afordance as a lens to study information system design

The original concept of afordance was proposed by Gibson (1977) in ecological psychology. This concept describes how animals perceive their environment. For example, humans perceive a chair in terms of what it can enable them to do (e.g., support) rather than its properties (e.g., made out of wood). This perception process can be seen as an interactive system (Maier & Fadel, 2009). In the system, there are two entities: animals and the environment. Afordance is a relational concept that depends on both entities. In the IS community, most scholars conceptualise afordance as the potential for behaviours arising from relations between technical objects and goal-oriented actors (Markus & Silver, 2008; Volkof & Strong, 2017). Some studies analyse its promise to the IS community and investigate its use in information systems implementation and adoption at both the individual and organisational levels (Du et al., 2019; Strong et al., 2014; Tim et al., 2018). Recently, the concept of afordance has become a popular lens to investigate information system design and development for organisational practices (Krancher & Luther, 2015; Seidel et al., 2017).

Following design-oriented IS research (Seidel et al., 2017), we adopt a duality view to conceptualise the afordance as 1) the action potentials between the IT artefacts and goal-oriented actors and 2) the material properties of the information system that allow for these potentials (Fayard & Weeks, 2014; Seidel et al., 2017). This conceptualisation of afordance captures both its relational (i.e., afordance is a relation between the actor and artefact) and dispositional (i.e., afordance is a property of the artefact) characteristics, which are highlighted in many studies (Fayard & Weeks, 2014; Maier & Fadel, 2009; Volkof & Strong, 2017). In synthesising the literature, we identify two advantages of afordance that could be used as a suitable lens to guide the design of IS artefacts. First, afordance as a relational concept is useful to address the interactions among designers, artefacts, and users. In any design activity, there are three fundamental entities: the designer, the artefact, and the user. In addition, there is an entangled relationship between the three entities (Maier & Fadel, 2009). This entanglement originates from the self-reference relationship in the designer-artefact-user system (Maier & Fadel, 2009). Specifically, the designers design artefacts that determine how the users use it, while how the designers determine artefacts is motivated by the users’ requirements. The concept of afordance, which captures the relations between actors and objects, can better address the complex interactions among designers, artefacts, and users.

Second, afordance serves IS researchers using the design science method extremely well. Design science research is a constructive process that “focuses on what reality might look like in the future – and recognises that the outcome is not preordained” (Volkof & Strong, 2017). As we mentioned before, afordance is also a process that transforms the input state (e.g., user uses the artefact) to an output state (e.g., realised outcome) in a nondeterministic way (Fayard & Weeks, 2014). Therefore, it is helpful for IS researchers to construct and explore diferent artefacts during design.

In our research, we follow a relational design model, named the afordance-based design model, to address the interactions among designers, artefacts, and users (Maier & Fadel, 2009). The model indicates three types of interactions (see Figure 1). First, the nature of the interaction between designers and users is that designers need to identify a set of user-required afordances. Second, the nature of the interaction between designers and artefacts is that designers develop the artefact features that provide these required afordances. Third, the nature of the interaction between users and artefacts is that the afordances of the artefact determine how it can be used by users. This model is in line with Seidel et al. (2017)’s approach to design science research, in which they indicate that when designing an information system for practice, IS researchers need to identify all the required afordances and purposefully design them, which can then be realised by certain users in certain use cases.

![](/api/attachments/YTEHWNY4/fulltext/images/fa3d355e83662fdef018148240ef80bc914dc7a377178359cd5188a392487cdf.jpg)  
Figure 1. Afordance-related interaction in designer-artefact-user systems (Maier & Fadel, 2009).

In the previous section, we summarised three categories of activities concerning the understanding of wildlife status, identification of external threats, and conduction of patrol tasks. According to the activities summarised from the literature (as seen in Table 1) and practices from our research department, we identified three main categories of assessing (i.e., assess wildlife population size and assess wildlife distribution), anticipating (i.e., identify the threat of poaching on wildlife and identify the threat of human-wildlife conflict on wildlife), and practising (i.e., optimise patrol routes and locate the best sites for camera traps) afordances. We detail the three main categories of afordances in the diagnosis cycle of the ADR project.

## 2.3. Analytics and its implications for wildlife management

The concept of analytics is not a new term. Analytics refers to data analysis applications performed by using computer-reasoning techniques such as statistical methods, regression, machine learning, and simulation (Müller et al., 2016; Watson, 2014). With the increase in the amount of data, “the key to deriving value from big data is the use of analytics” (Watson, 2014). Therefore, the concept of BDA emerged by combining the concepts of big data and analytics. Specifically, BDA can be defined as utilising analytics techniques to derive the useful information and patterns that are embedded in large-scale datasets with a high volume, velocity, and variety (Müller et al., 2016; Watson, 2014). Through reviewing the extant literature, we found that BDA techniques can be classified into three hierarchical yet overlapping categories, namely, descriptive, predictive, and prescriptive (Watson, 2014). These three types of analytics are helpful in providing the required afordances in wildlife management.

Descriptive analytics involves the use of techniques such as statistics and data visualisation (Watson, 2014). These analytics can be used to summarise and describe the historical or current state of an activity situation and answer the question of “what happened”.

Descriptive analytics are useful in summarising wildlife demographic indicators (e.g., population size and distribution) and visualising the related results, thus allowing wildlife practitioners to assess wildlife status.

Predictive analytics mainly consists of regression methods and machine learning (Watson, 2014). These techniques can be used to anticipate future possibilities to answer the question of “what is likely to happen in the future”. Such analytics are suitable for identifying potential risk areas by uncovering patterns in these activities, such as poaching and humanwildlife conflicts. In a related study, Critchlow et al. (2015) suggest that the historical location of illegal activity is a useful predictor for the future occurrence of such incidents.

Prescriptive analysis mainly includes the techniques of simulation and decision modelling (Watson, 2014). These techniques can be used to improve the current management process according to the simulated results and answer the question of “what actions should be taken”. In our study, such analytics are suitable for deriving actionable insights to optimise the ranger patrol tasks because they can simulate wildlife pathways in a virtual environment based on historical locations. The simulated wildlife pathways can be used as a helpful reference for rangers to track wildlife and locate the best camera trap sites.

To summarise, the literature pertaining to analytics highlights important implications regarding the design of the analytics system that allows for the required afordances in wildlife management. In our research, the WMAS can be defined as an advanced form of business intelligence (BI) and an advanced form of decision support system (DSS) because the term “analytics” is rooted in DSS and evolved from BI (Watson, 2014). We developed and tested a set of design principles for the WMAS. In this manner, we contributed to the research about how this specific information system should be designed in the wildlife management domain.

## 3. Research approach

The goal of the paper is to develop and test design principles for analytics systems that support wildlife management. These design principles, as a nascent design theory, capture a general solution in a class of artefacts (Baskerville et al., 2018), which can be used to guide actions in a wider range of problems and systems (Hevner et al., 2004). These principles are important theoretical contributions to the IS community (Baskerville et al., 2018) and can be considered valuable outcomes for practitioners to design similar artefacts (Sein et al., 2011).

This study followed the elaborated action design research (ADR) method (Mullarkey et al., 2019), which summarises from the authors’ experience when conducting a real-world ADR project. The elaborated ADR approach unpacks the process of building-intervention-evaluation (BIE) from Sein et al. (2011) seminal work into the separate diagnosis, design, implementation, and evolution cycles. Each of these intervention cycles contains activities of problem formulation (P), artefact creation (A), evaluation (E), reflection (R), and learning (L). Mullarkey et al. (2019) also added a new principle of abstraction, which indicates that researchers can introduce diferent artefacts through an appropriate level of abstraction in each of the four cycles. For instance, artefact abstraction in the diagnosis cycle may be requirement definitions and the artefact abstraction in the design cycle may be architectures or a set of design principles.

The elaborated ADR approach also allows the customised use of iterative cycles of diagnosis, design, implementation, and evolution to generate and refine the design of the artefact. This approach difers from the traditional stage-gate design science research model (Cooper et al., 2002) in that it emphasises the activities of artefact co-creation and real intervention. This approach also emphasises guide emergence because the initial designed artefact is continuously refined by reflecting on its use in real organisational settings (Mullarkey et al., 2019; Sein et al., 2011). Since the ADR approach links practice with theory and thinking with doing (Sussman, 1983), it is suitable for our research to develop and test the design principles for WMAS.

## 3.1. ADR intervention cycles and activities

The research design of our ADR project is adapted from the elaborated ADR approach of Mullarkey et al. (2019). In our study, we adopted diagnosis, design, and implementation cycles from the authors’ seminal work. We also extended Mullarkey & Hevner’s guidelines by adding an additional cycle of data preparation, which prepares all the wildlife data prior to the design cycle. The elaborated ADR cycles and main activities in each cycle are summarised in Figure 2. The activities in each cycle are introduced in Appendix A. First, the ADR project starts with a diagnosis cycle. The entry point of the project is problem-centred, i.e., designing a novel system to derive useful information and insights embedded in wildlife-related data. Accordingly, we identified the preliminary requirements of stakeholders to develop a WMAS. When designing information systems for practitioners, we aim to design action potentials (Seidel et al., 2017) – in our study, we attempt to provide actionable guidance for practitioners to manage wildlife in the protected areas. Thus, following an afordance-based design model, we identified three categories of afordances (i.e., assessing, anticipating, and practising) by reviewing the literature on biology management. In this cycle, we further refined the preliminary requirement into the general requirements in terms of required afordances that the WMAS should support.

![](/api/attachments/YTEHWNY4/fulltext/images/5d59f2e90fbca423cf2aaedbaa3895b857a81aa65149533e6fd956bc8bbc5fec.jpg)  
Figure 2. The elaborated ADR cycles based on.Mullarkey et al. (2019)

Second, we added a new cycle of data preparation because the large-scale wildlife data in our ADR project needed to be processed and analysed. In this cycle, we detailed the data we used and prepared these data for readiness through an extracting, transforming, and loading (ETL) procedure, which is a common process in multi-source data collection and integration.

Third, we iterated the first round of the design and implementation cycle. In the design cycle, we conceptualised the initial set of design principles. The design principles were formulated by following a design principle form proposed by Chandra et al. (2015). In the implementation cycle, we instantiated the initial design principles into a prototype system. We detailed the material properties (i.e., algorithm and interface) that support the required afordances in wildlife management. Next, we conducted an interim evaluation within the ADR team and collected qualitative feedback from system users. Through data analysis, we found that the interim evaluation revealed both expected and unexpected consequences. We used the expected consequences to evaluate the feasibility of our initial design. The unexpected consequences informed the refinement of the initial design principles.

Fourth, we integrated these unexpected findings into the second round of design and implementation cycles. In the design cycle, we used the unexpected findings of the first-round evaluation to revise these initial design principles. Based on these changes, we instantiated a new version of the prototype system in the implementation cycle. In the new version, we explored alternative or additional system features that might create the required afordances. This new system version was deployed in a field test with practitioners from the department, and a second evaluation was executed to show improvements in three operational scenarios of wildlife management (i.e., understanding wildlife status, identifying threat on wildlife, and patrolling) before and after the introduction of the WMAS.

During these elaborated ADR cycles, we iteratively abstracted the requirements through the diagnosis cycle, the data needed through the data preparation cycle, the design principles, and the system features through the design and implementation cycles. These abstracted artefacts, the design principles, in particular, are our main theoretical contributions, which are elaborated in the discussion section. In this section, we also present our reflections on the ADR approach when designing data analytics systems for practice and its practical implications.

## 3.2. ADR project setting

Our ADR project was initiated along with the department in August 2018. The department in our study is one that has taken a leading role in wildlife management practice through the use of information technologies. The department is located in a biologically diverse region of India. The department is responsible for implementing wildlife management programmes among the state’s dozens of national parks, reserves, and sanctuaries and has piloted an information system to help rangers collect wildlife-related data through patrols and surveys. As the size of the data has increased, the department hoped to explore the large-scale dataset to derive useful information for their management practices.

In the ADR project, we identified the management department (state-level bureaucrats) and the implementation department (local-level oficers and rangers) as the two main stakeholders. The management department is responsible for the administration eforts (e.g., implementation of new programmes) within the entire range of each protected area. The implementation department is responsible for executing these programmes to monitor and manage wildlife in the field. In our ADR project, together with the data analysts and researchers from the IS community, representatives from the two stakeholders formed the “ADR team”.

The wildlife practitioners on the ADR team performed two key roles in the project. The practitioners from the management department introduced the data collection process and key fields in these data, which helped us understand the background of this project. Moreover, they also provided two wildlife indicators (i.e., number of wildlife sightings and spatial position locations) that are widely used in their practices to approximately estimate wildlife population size and wildlife distribution. The suggestions were accepted and implemented in the prototype system. Practitioners from the implementation department played significant roles in implementing and testing the system. Table 2 summarises the responsibilities of the ADR team members.

## 4. Diagnosis cycle

In the diagnosis cycle, we have two tasks: understanding both the problem domain and the solution domain and defining the requirements of the analytics system. First, we positioned our ADR project within the domain of wildlife management in protected areas. To design a system for such practices, we needed to understand the problem space and the solution space. To do so, we conducted a thorough investigation of the literature on biology conservation and management. We found that there is a rich body of knowledge concerning wildlife management. Specifically, we found that some studies focus on the investigation of three categories of wildlife management activities (i.e., understanding wildlife status, identifying external threats, and conducting patrol tasks) and related solutions.

Second, we specified the requirements for the artefact to be built. Based on participant observation and semi-structured interviews in the department, we found that it is inadequate to manipulate the largescale data with spreadsheets. Moreover, it was dificult for the department to conduct exploratory wildlife data analysis. We thus diagnosed that the preliminary requirement of the department was to design a WMAS, through which practitioners can derive insights embedded in the data.

Next, we refined the preliminary requirements into a general set of requirements in the forms of required afordances. Just as the afordance-based design indicates, when developing an artefact, we identified all the required afordances that the system should allow for and purposely designed them. In our study, we identified three main categories of assessing, anticipating, and practising afordances in wildlife management (as seen in Table 3), which are summarised from the literature and practices of the department. The assessing afordances refer to the assessment of the wildlife status, the anticipating afordances refer to the identification of the threats to the wildlife in advance, and the practising afordances refer to the optimisation of the patrol work. In addition, we identified two categories of assessing afordances (i.e., assessing wildlife population size and assessing wildlife distribution), two categories of anticipating afordances (i.e., identifying threats of poaching on wildlife and identifying threats of human-wildlife conflicts on wildlife), and two categories of practising afordances (i.e., optimising patrol routes and locating the best sites for camera traps).

We can take a process view to understand the relationships among the three main afordances. Wildlife practitioners attempt to assess wildlife status through demographic indicators, identify these potential threats that may cause changes in wildlife status, and optimise rangers’ patrol work to monitor these threatened wildlife. Thus, the process-oriented view of wildlife management gives us the general requirements for action potentials in wildlife management that the system should support.

## 5. Data preparation cycle

Data preparation is a process of cleaning and transforming raw data prior to analysis. This process is necessary for a data analytics project because the raw data are rarely ready to use. In our ADR project, these raw data mainly consist of five data types pertaining to wildlife sighting, wildlife evidence, wildlife mortality, poaching, and human-wildlife conflict. The latest datasets we obtained comprise more than 1.8 million wildlife-related data points from 87 thousand patrol tasks, spanning a period of 40 months from January 2015 to April 2018 (see Table 4 and more detail see Appendix B). These datasets were derived from multiple sources. Based on diferent data sources and characteristics, we classified these five data types into three groups: wildlife data, poaching data, and human-wildlife conflict data. Wildlife data pertaining to wildlife sighting and wildlife evidence were collected by rangers during their daily patrol tasks, poaching data pertaining to poaching activities and wildlife mortality were collected by rangers in anti-poaching camps during their daily patrol tasks, and human-wildlife conflict data pertaining to human-wildlife conflict were collected by rangers who interviewed and surveyed the afected villagers living near core areas of the forest.

Table 2. Responsibilities of the ADR team members.

<table><tr><td>Team member</td><td>Responsibilities</td></tr><tr><td>Management department</td><td>-Provide information regarding the current management situation-Provide advice about the domain understanding, data processing and system design-Organise wildlife officers and rangers to implement the intervention-Evaluate the conformance between problems and artefact design</td></tr><tr><td>Implementation department</td><td>-Use the wildlife management analytics system-Provide feedback about the system use</td></tr><tr><td>IS researchers</td><td>-Identify the research opportunity and generalise the problem instance-Identify the requirements for the analytics system-Develop an initial set of design principles-Collect and analyse system use information-Reflect on the initial design and refine the design principles-Generalise the solution instances</td></tr></table>

Table 3. The required afordances and related definitions.

<table><tr><td>Affordance category</td><td>Affordance construct</td><td>Definition</td></tr><tr><td rowspan="2">Assessing affordances</td><td>Assess wildlife population size</td><td>Population size is one of the main wildlife demographics, which is widely used in wildlife research and practice. This affordance, if realised, enables actors to assess the wildlife status in terms of population size.</td></tr><tr><td>Assess wildlife distribution</td><td>The geographical distribution is another commonly used indicator in wildlife management. This affordance, if realised, enables actors to assess the wildlife status in terms of distribution.</td></tr><tr><td rowspan="2">Anticipating affordances</td><td>Identify threats of poaching on wildlife</td><td>Poaching is one of the main threats to the extinction of wildlife. This affordance, if realised, enables actors to identify the risk areas where poaching incidents are more likely to occur.</td></tr><tr><td>Identify threats of human-wildlife conflict on wildlife</td><td>Human-wildlife conflict is another main threat to both the wildlife and the local people. This affordance, if realised, enables actors to identify risk areas where human-wildlife incidents are more likely to occur.</td></tr><tr><td rowspan="2">Practising affordances</td><td>Optimise the patrol routes</td><td>The rangers&#x27; work in wildlife management is to patrol the protected areas. This affordance, if realised, enables actors to optimise the current patrol routes to monitor these wildlife effectively.</td></tr><tr><td>Locate the best sites for camera traps</td><td>Camera traps are useful tools in monitoring the wildlife for their convenience and efficiency in field investigations. This affordance, if realised, enables actors to locate camera traps in the right places to aid rangers&#x27; patrol work.</td></tr></table>

According to the previous data classification, we readied our data using the procedure of extract, transform, and load (ETL). ETL is a common process of data management that accesses and migrates multisource data into a data warehouse. The ETL procedure mainly involves two key activities: data integration and data cleaning. First, the same type of data with diferent fields was integrated. For example, the wildlife sighting records, and wildlife evidence records were integrated into the same dataset (i.e., wildlife data) because the two types of records are both concerning wildlife-related information but use diferent data fields. Wildlife mortality and poaching activities were also integrated because the death of wildlife may be caused by poaching or snaring incidents. The fields of the data were normalised (see column 3, Table 4) when we integrated them.

Second, the data were cleaned because the collected data were fraught with errors caused by the rangers, such as erroneous records and duplicate records. Collaborating with the practitioners, the researchers examined the data for all types of errors and made the related rules to address each error type, such as removal of records with no value and setting the threshold to screen records with extreme values. According to these rules, the analysts developed SQL commands to handle all these error types and produced a clean dataset. After the data preparation cycle, the data were transformed from their original form into a usable form. These prepared data were loaded into a target SQL database.

## 6. The first round of design and implementation cycle

In this section, we detail the first iteration of the design and implementation cycles, which occurred during April 2018 and August 2018.

## 6.1. Design cycle

In the design cycle of our ADR project, we focused on the identification of the initial design principles. The design principles are prescriptive knowledge, which describe “what and how to build an artefact in order to achieve a predefined design goal” (Chandra et al., 2015). These principles can be used in similar problems to guide the design of purposeful IS artefacts. We formulated our design principles by following a widely used design principle template (Chandra et al., 2015) that contains three types of information: action potentials (i.e., afordance) through the use of an artefact, the artefacts that make these actions possible, and the boundary conditions. The template is demonstrated as follows.

Table 4. Wildlife-related data.

<table><tr><td>Dataset group</td><td>Dataset</td><td>Fields in dataset</td><td>Number of data points</td></tr><tr><td rowspan="2">Wildlife data</td><td>Wildlife Sighting</td><td>User ID, animal name, location (e.g., longitude, latitude), number, time</td><td rowspan="5">1,820,410</td></tr><tr><td>Wildlife Evidence</td><td>User ID, animal name, location (e.g., longitude, latitude), animal evidence (e.g., scratch, sound), time</td></tr><tr><td rowspan="2">Poaching data</td><td>Wildlife Mortality</td><td>User ID, animal name, cause of death (e.g., poaching or natural), location (e.g., longitude, latitude), vegetation type, terrain type</td></tr><tr><td>Poaching Activities</td><td>User ID, animal name, type (e.g., hunting, poaching, or snaring), location (e.g., longitude, latitude), vegetation type, terrain type</td></tr><tr><td>Human-wildlife conflict data</td><td>Human-Wildlife Conflict</td><td>Animal name, magnitude (e.g., small, medium, or large), region (e.g., branch), photos</td></tr></table>

Provide the system with [material property – in terms of form and function] in order for users to [activity of users – in terms of action], given that [boundary conditions – user group’s characteristics or implementation settings].

In our study, our design principles resulted from a construction process where we identified the WMAS by previous biology management research, the concept of afordance, and the capabilities of analytics techniques in processing large-scale data. Next, we introduce how our initial design principles were formulated (see Table 5).

First, the assessing afordances consist of two constructs: assess wildlife population size and assess wildlife distribution. To allow for these two required afordances, the wildlife management system should provide information related to wildlife population size and wildlife distribution. In the department, wildlife practitioners usually use two metrics (i.e., number of wildlife sightings and map-recorded wildlife locations) to approximately estimate the two wildlife demographical indicators (i.e., population size and distribution). Based on the two metrics from departmental practices, we design two system features to allow for the two afordances. The feature1-a is to visualise the number of wildlife sightings. The feature1-b is to map the wildlife spatial locations.

Second, the anticipating afordances consist of two constructs: identify the threat of poaching on wildlife and identify the threat of human-wildlife conflict on wildlife. To identify poaching incidents in advance, we design system feature2-a to map the historical poaching areas because the previous poaching spatial locations are useful to predict the occurrence of poaching in the future (Critchlow et al., 2015). Human-wildlife conflicts, ranging from crop damage to human safety, have been occurring with an increasing frequency in protected areas. These conflicts are also one of the main threats to both wildlife species and local people (Karanth et al., 2012). To identify human-wildlife conflicts, we design system feature2-b to compare the number of human-wildlife conflicts among diferent regions.

Third, the practising afordance consists of two constructs: optimise the patrol routes and locate the best sites for camera traps. The traditional foot patrol is time-consuming and ineficient because rangers always conduct their tasks in pre-planned routes. To optimise rangers’ patrol work, we provide feature3-a to simulate wildlife pathways. The simulated results can provide a useful reference for rangers to track wildlife in their patrol tasks. Camera traps are widely used to aid ranger patrols in monitoring wildlife. However, it is still challenging to locate the best camera trap sites that can monitor wildlife efectively (Tobler et al., 2008). Therefore, to achieve this goal, we design feature3-b to identify these key points in the simulated wildlife pathways.

## 6.2. Implementation cycle

In the implementation cycle, collaborating with the practitioners in the ADR team, we instantiated the initial set of the design principles into a prototype system (for the architecture, see Figure 3). The architecture of the system mainly consists of three parts: database, analytics techniques in forms of algorithms and graphic user interface such as the histogram, geographic map, time selection box, and drop-down menu. As we mentioned before, we identified three categories of afordances (i.e., assessing, anticipating, and practising), each of which has two afordance constructs. We thus designed three analytics modules (i.e., wildlife status, threat identification, and patrol), each of which has two system features, to support the afordance constructs. The algorithms are the key material properties in these system features. The details of the algorithms are presented in Appendix C. The structure of the interface is introduced in Appendix D. In the subsequent section, we mainly describe the six system features and their functions.

Table 5. The initial set of design principles.

<table><tr><td>Design principles (DP)</td><td>Affordances</td><td>Features</td></tr><tr><td>DP1-a: Provide features to visualise the number of wildlife sightings [material property], so that the system can afford the users to assess wildlife population size [action potential] in wildlife management [boundary conditions].</td><td>-Assess wildlife population size-Assess wildlife distribution</td><td>-Feature1-a: visualise the number of wildlife sightings- Feature1-b: Map the wildlife spatial locations</td></tr><tr><td>DP1-b: Provide features to map the wildlife spatial locations [material property], so that the system can afford users to assess wildlife distribution [action potential] in wildlife management [boundary conditions].</td><td></td><td></td></tr><tr><td>DP2-a: Provide features to map the historical poaching areas [material property], so that the system can afford the users to identify threat of poaching on wildlife [action potential] in wildlife management [boundary conditions].</td><td>-Identify threat of poaching on wildlife-Identify threat of human-wildlife conflict on wildlife</td><td>- Feature2-a: Map the historical poaching areas- Feature2-b: Compare the number of human-wildlife conflicts in different regions</td></tr><tr><td>DP-b: Provide features to compare of the number of human-wildlife conflicts in different regions [material property], so that the system can afford the users to identify threat of human-wildlife conflict on wildlife [action potential] in wildlife management [boundary conditions].</td><td></td><td></td></tr><tr><td>DP3-a: Provide features to simulate the wildlife pathways [material property], so that the system can afford the users to optimise patrol routes [action potential] in wildlife management [boundary conditions].</td><td>-Optimise patrol routes-Locate the best camera trap sites</td><td>- Feature3-a: Simulate the wildlife pathways-Feature3-b: Identify the key points in the simulated wildlife pathways</td></tr><tr><td>DP3-b: Provide features to identify the key points in the simulated wildlife pathways [material property], so that the system can afford the users to locate the best camera trap sites [action potential] in wildlife management [boundary conditions].</td><td></td><td></td></tr></table>

![](/api/attachments/YTEHWNY4/fulltext/images/12c30d42bf2d024f9efc0ec0ee645d87b8d58f03c4705abe0417cedee9f89e4e.jpg)  
Figure 3. Architecture of the analytics system.

To aford assessing of wildlife population size (DP1-a), we provide system features to visualise the number of wildlife sightings. Figure 4-a displays an example of this feature, which demonstrates the number of wildlife sightings through a bar chart. In this figure, the horizontal axis denotes the wildlife, and the vertical axis denotes the numeric values of the animals observed in a month. Each coloured bar represents a specific wild animal that can be seen in the right-side legend. For instance, the pink bar represents leopard. This feature also has a sidebar panel, which consists of a drop-down menu with various wild animal options. To aford assessing of wildlife distribution (DP1-b), the analytics system displays the wildlife spatial locations through a scatter point map (see Figure 4-b). The sidebar panel of this feature consists of a drop-down menu with wild animal options. A user can use the dropdown to select one or more animals to check the population size and distribution. The results are updated by the front-end system in real time according to the users’ option.

To aford identifying the threat of poaching on wildlife (DP2-a), the analytics system provides features to map the poaching-prone areas in a scatter point map (see Figure 5-a), in which each node denotes a historical poaching-prone area. The sidebar panel of the feature consists of a drop-down menu with the threat options. To aford identifying the threat of human-wildlife conflict on wildlife (DP2- b), the analytics system provides features to compare the number of conflicts among diferent regions through a bar chart (see Figure 5-b). In this figure, the horizontal axis describes diferent regions, and the vertical axis shows the numerical values of the humanwildlife conflicts. Each coloured bar represents a specific human-wildlife conflict that can be seen in the right-side legend. For instance, the orange bar represents the conflicts between black bucks and humans.

To aford optimisation of the patrol routes (DP3-a), the analytics system provides the simulated wildlife pathways by using ArcGIS software, which is a professional geographic information system for mapping and spatial reasoning. We used the functions in ArcGIS software to simulate the potential wildlife pathways. Specifically, the data of wildlife spatial locations (i.e., longitude and latitude) are used as inputs to infer the optimal wildlife pathways, which cover the majority of the spatial locations. The results of the digital pathways form a network by overlaying the map of a specific area (see Figure 6-a). This network represents the potential wildlife movement corridors in a specific area and can be further analysed to locate the best sites for camera traps (DP3-b). In the simulated networks, the interactions among multiple wildlife pathways are viewed as the wildlife regular transit points and hence identified as the critical locations to instal camera traps (see Figure 6-b).

![](/api/attachments/YTEHWNY4/fulltext/images/cfab555223a5441a1b1f371b9d7a8b1fac00aea0d3ab6ec5133c6b6a63677bb2.jpg)  
Figure 4. Initial features for the assessing afordances.

![](/api/attachments/YTEHWNY4/fulltext/images/b1472e735c96680169014b7723773c24e4a1e1a1420a675d4d77d3afa6f322c0.jpg)  
(a) Scatter point map of poaching areas

![](/api/attachments/YTEHWNY4/fulltext/images/64f8f0a609710e9686a6c0e6bd0210d4e8074bcfedd4804835d5152d170fa302.jpg)  
(b) Bar chart of human-wildlife conflicts  
Figure 5. Initial features for the anticipating afordances.

## 6.3. Evaluation

The first evaluation was an interim evaluation that was conducted in the implementation cycle. Practitioners and researchers from the ADR team were involved in this interim evaluation. The test of the initial system occurred between July 2018 and August 2018. After that, we conducted four workshops, each including 3–4 practitioners and 1–2 researchers and lasting 1 hour, because the workshop allowed more freedom of expression and discussion. In the workshops, we discussed the theme of “what does the system features allow you to do”. The aim of the discussions was to see whether the intended designed afordance was perceived by users. In doing so, we found that the evaluation revealed both the expected consequences and unexpected consequences (see Table 6). In this section, we used these expected consequences to evaluate the feasibility of our initial designs.

For the instantiation of DP1-a and DP1-b, we found that the system features efectively converted the wildlife data into two useful wildlife metrics. The users valued the eficiency of the system in processing the larger data because it reduced their human workload. In addition, we also found that the results from the system could be used in their monthly report to meet the practitioners’ needs in assessing wildlife conditions.

For the instantiation of DP2-a and DP2-b, we found that the system facilitated the identification of the poaching-prone areas by mapping previous poaching locations. In this test, users identified two potential poaching hotspots by combining the analysis results and their experience from the field poaching investigation. The evidence also suggested that the bar chart is useful for observing and comparing the number of conflicts in diferent regions, which enables practitioners to identify the places where conflicts are more likely to occur.

For the instantiation of DP3-a and DP3-b, the users recognised that it is reasonable to simulate the wildlife pathways by using wildlife spatial locations because wildlife usually travel along their preferred routes. The users also acknowledged the advantage of locating the best camera trap sites by a data-driven approach because choosing the right sites is challenging work in field wildlife investigations, and in most situations, these decisions are often dependent on practitioners experience.

![](/api/attachments/YTEHWNY4/fulltext/images/ed6f4636e27e4cd4a0f6e4fe5991de2afa24f195ae6ba7a342af7fda20b07783.jpg)  
Figure 6. Initial features for practising afordances.

Table 
6. Expected and unexpected consequences.

<table><tr><td>Design principles (DP)</td><td>Expected consequences</td><td>Unexpected consequence</td></tr><tr><td>DP1-a</td><td>Useful to meet practitioners&#x27; needs of understanding wildlife population size.</td><td>The initial designs neglect the dynamics of the wildlife population size.</td></tr><tr><td>DP1-b</td><td>Useful to meet practitioners&#x27; needs of understanding wildlife distribution.</td><td>The initial designs neglect the dynamics of the wildlife distribution.</td></tr><tr><td>DP2-a</td><td>Useful for practitioners to identify poaching hotspots in geographic map.</td><td>The initial designs neglect the environmental characteristics around the incident sites.</td></tr><tr><td>DP2-b</td><td>Useful for practitioners to identify places where human-wildlife conflicts are more likely to occur.</td><td>The initial designs neglect the conflict magnitude in a specific region.</td></tr><tr><td>DP3-a</td><td>Helpful in optimising the patrol routes through the simulated wildlife pathways.</td><td>Provide potential wildlife channels within a certain range.</td></tr><tr><td>DP3-b</td><td>Practitioners acknowledged the advantage of locating camera trap sites through a data-driven approach.</td><td>The initial simulated results are not applicable in the real context because they neglect landscape factors such as slopes.</td></tr></table>

The interim evaluation also revealed some unexpected consequences. Researchers should be sensitive to these signals during implementation (Sein et al., 2011) because they often inform the refine of the IS artefact. Next, we initiated a second round of the design and implementation cycle by reflecting on these unexpected consequences.

## 7. The second round of the design and implementation cycle

In this section, we detail the second iteration of the design and implementation cycles, which occurred during September 2018 and March 2019.

## 7.1. Design cycle

In this design cycle, we refined the initial sets of design principles by reflecting on the unexpected consequences. For the instantiation of DP1-a and DP1-b, we found that the initial designs neglected the change of wildlife status (i.e., population size and distribution). In practice, it is essential to understand the wildlife status dynamics in wildlife management, particularly in the protection of these endangered species. If the situation of continual population size decline can’t be discovered timely, practitioners will not be able to prevent the situation from deteriorating even further. Therefore, we redesigned the initial features to reflect the changes in the two wildlife indicators:

DP1-a: Provide features to visualise the change in wildlife sightings number [material property], so that the system can aford the users to assess the wildlife population size [action potential] in wildlife management [boundary conditions].

DP1-b: Provide features to map the change in wildlife spatial locations [material property], so that the system can aford the users to assess the wildlife distribution [action potential] in wildlife management [boundary conditions].

For the instantiation of DP2-a and DP2-b, the findings of the evaluation indicated that only mapping the poaching-prone areas is not enough for identifying the potential threats; the system should also provide features to demonstrate the characteristics of the surrounding environments, such as the vegetation and terrain types near the poaching sites. These factors are helpful in analysing the potential environment where poaching incidents often occur and are thus important to predict the occurrence of these incidents in the future. Correspondingly:

DP2-a: Provide features to map the poaching areas and demonstrate the vegetation type and terrain type around the poaching sites so that the system can aford users to identify the threat of poaching on wildlife [action potential] in wildlife management [boundary conditions].

We also found that it is not enough to know the places where human-wildlife conflicts are more likely to occur; users also need more information about the magnitude of these conflicts in a specific region because those more serious incidents present a greater threat to both wildlife and humans. Correspondingly:

DP2-b: Provide features to compare the number of human-wildlife conflicts in diferent regions and demonstrate the magnitude of the conflicts [material property], so that the system can aford the users to identify the threat of human-wildlife conflict on wildlife [action potential] in wildlife management [boundary conditions].

For the instantiation of DP3-a and DP3-b, the wildlife practitioners suggested that the wild species usually walk in a certain range of channels, and thus, setting a specific width of the channels is helpful in tracking these wildlife:

DP3-a: Provide features to simulate wildlife channels with a 50-metre bufer [material property] so that the system can aford users to optimise patrol routes [action potential] in wildlife management [boundary conditions].

The findings also indicated that the results of simulated camera trap locations might not be applicable in the real context because the practitioners pointed out that some of the sites are quite steep and may not be suitable for installing camera traps. Thus, we re-simulated these candidate sites by considering factors of landscape constraint such as the slope. Correspondingly:

DP3-b: Provide features to identify the key points in the simulated wildlife pathways by considering the landscape constraints [material property] so that the system can aford users to locate the best sites for camera traps [action potential] in wildlife management [boundary conditions].

## 7.2. Implementation cycle

In this section, we operationalised the revised design principles to refine the initial system features to better support the required afordances. Specifically, for assessing afordances, we revised the bar chart to a dotted line to show the change in wildlife sighting number (see Figure 7-a). In this figure, the horizontal axis is the timeline, and the vertical axis describes the number of observed wild species. We also added a drop-down menu with date options in the sidebar panel. The users can use this menu to select a time period to observe the change in the number of a specific wild animal. In the wildlife distribution feature, a drop-down menu with data options was also added (see Figure 7-b). The users can use this menu to check the dynamics of wildlife distribution at diferent time periods.

For the anticipating afordances, we improved the features of the poaching map by adding two pie charts of vegetation type and terrain type, which demonstrated the environmental characteristics of the poaching areas (see Figure 8-a). The first pie chart shows the terrain type where poaching incidents often occur are plain (46.9%), hilly (25%), and undulating (21.9%). The second pie chart shows the vegetation type where poaching incidents often occur are semi-evergreen (46.9%) and moist deciduous (21.9%). In the conflicting feature, we added a pie chart to show the proportion of the conflict magnitude in a specific area (see Figure 8-b). In the figure, there are four levels of human-wildlife conflict magnitude (i.e., medium, small, very small and marginal) in the area of Bel. The users also can select other region options through the drop-down menu to see the corresponding magnitude proportion of the human-wildlife conflicts.

For the practising afordances, we also operationalised the two revised design principles. Specifically, for the first feature, we simulated the wildlife pathways with a 50-metre bufer (see Figure 9-a). For the second feature, the candidate camera trap sites were further filtered by considering the factor of the landscape slope (see Figure 9-b). The new results show that camera traps should be installed in flat forest areas rather than steep mountain areas. This improvement also reflects that the algorithm results should be refined by human intelligence. Although analytics techniques can simulate the optimal results in a virtual environment, they may neglect some critical factors from real-world situations. Therefore, human expertise is needed to complement the algorithms for solving complex problems, especially those under dynamic and unforeseen conditions.

## 7.3. Evaluation

We conducted the second evaluation in the implementation cycle. In this test, the refined prototype system was implemented in a wider range of the department through a comprehensive evaluation. To ensure this evaluation, a system instruction was provided. It consisted of a 20-page document in which we specified the structures, interfaces, and functions of the system. We also performed training activities in the department about how to use these system features so that staf could obtain knowledge and skill to perform the data analysis accurately.

![](/api/attachments/YTEHWNY4/fulltext/images/7d3977c94d7dfbe42fabb7e30f0463dbf6281f800a0930d19366e5b3536c97d3.jpg)

![](/api/attachments/YTEHWNY4/fulltext/images/64cf7d746025c24e760de7c81dffaadfcd4a54e44cb97843fc99fbcdf96d72de.jpg)  
(a) The dotted line of wildlife sightings  
(b) Scatter point map of wildlife distribution

Figure 7. Revised features for the assessing afordances.  
![](/api/attachments/YTEHWNY4/fulltext/images/8440c578096941615edd735b95e18ad94b424e69f06d46c956ba14b9a15478c6.jpg)  
(a) Pie chart of the surrounding environment

![](/api/attachments/YTEHWNY4/fulltext/images/84e6ad04d249cb258235081a06765ca61a341f54342a76f40eac30cbf305b6a0.jpg)  
(b) Pie chart of conflict magnitude

Figure 8. Revised features for the anticipating afordances.  
![](/api/attachments/YTEHWNY4/fulltext/images/03d7bdd14ea7f64fe9932884eba02ef3a23de5b350ae995c0bda57fbcc7347e0.jpg)  
Figure 9. Revised features for the practising afordances.

This evaluation occurred between November 2018 and February 2019. After that, one of our authors went to the department to collect usage data. A total of seven semi-structured interviews were conducted with six representative system users, of whom four informants were from the management department and the other two informants were from the implementation department. These interviews, each of which lasted 1 hour, created an open atmosphere that allowed more discussions with the interviewees. We mainly asked the informants two types of openended questions: “what are the main activities in wildlife management before the introduction of the WMAS” and “what are the changes in these activities after the introduction of the WMAS”. All the interviews were digitally recorded and transcribed. Through analysing the transcripts, we compared the improvements in three operational scenarios in wildlife management before and after the introduction of the WMAS to evaluate our intervention (see Table 7).

The first operational scenario of the department is to understand wildlife status. Before introduction of the WMAS, wildlife data were generated in disaggregated form, and standard reports of wildlife status were being produced by a third-party systems developer. These reports were typically generated centrally and cascaded down the hierarchy of the implementation department for their perusal. As manager A mentioned,

“We never quite did know what was happening in the jungles . . . an informational gap continued to persist – there wasn’t a centralised way of looking at all the data that was coming in from the field – tinker with it and generate customised reports to meet local needs.”

Table 7. Operational scenarios before and after intervention of the WMAS.

<table><tr><td>Scenarios</td><td>Before intervention</td><td>After intervention</td></tr><tr><td>Understanding wildlife status</td><td>- Understand wildlife status through reports provided by a third-party system developer- Decision-making lags behind the wildlife status changes</td><td>- Generate wildlife population size and distribution through the WMAS- Take seasonable measures according to the change of wildlife status</td></tr><tr><td>Identifying threat on wildlife</td><td>- The poaching data are collected but not analysed- The present information system cannot allow for uncovering human-wildlife conflict patterns</td><td>- Get the capabilities to address some concerned problems in poaching identification- Uncover useful patterns for taking preventive measures to mitigate risks of human-wildlife conflict</td></tr><tr><td>Patrolling</td><td>- Make patrol routes in an inflexible way- Instal camera traps to aid patrol based on practitioners&#x27; experience</td><td>- Map out new patrol routes flexibly- Instal camera traps through combining data-driven results and practitioners&#x27; experience</td></tr></table>

After introduction of the WMAS, the managers could obtain the indicators of wildlife population size and distribution through the system. The results of wildlife status and its dynamics were not only used to generate a customised report to meet practical needs but were also helpful in taking seasonable measures for efective wildlife management. As manager B mentioned,

“Computation of prey and predator distribution and their visualisation has helped us gain crucial actionable insights into conservation eforts. For instance, areas of low prey density on the map indicates to us that perhaps we need to create more “salt licks” (to attract prey). Similarly, areas of low predator density indicate the need for further investigation eventuating in more patrolling routes covering those areas.”

The second operational scenario of the department is to identify threat on wildlife (i.e., anti-poaching and human-wildlife conflict management). Before introduction of the WMAS, instances of poaching, or in other terminology, “illegal activities”, which also include harvesting forest produce, are recorded by forest rangers during their patrols. Information was being captured in a digital form, but again, there were no systematic ways of looking at aggregated data. This made the process of identifying at-risk areas cumbersome. Typically, human-wildlife conflict cases were reported by afected people in villages surrounding the parks or in other places of close proximity. Although there was a systematic and centralised way of gathering the data, the present system did not allow for creative analysis of understanding conflict patterns.

After introduction of the WMAS, the practitioner obtains the ability to address some problems in poaching identification that could not be solved before. As manager C mentioned,

“Illegal activities are now mappable to geo-locations. Having this capability gives us the opportunity to come up with interesting analysis of our data. Questions such as ‘Are there certain areas frequented by trespassers, if so, then what is the terrain type, do they have a preference?’ can now be answered. Additionally, the system also enables us to view illegal activities data in conjunction with a host of other data such as time data and season data.

The practitioners also used the system to uncover useful patterns for taking preventive measures to mitigate risks of conflicts. As manager D mentioned,

“We now have the flexibility to look at the same data using diferent lenses. Now, for example, by creating a timeline of human-animal conflict cases, we can understand seasonality of conflicts. There are some months where the conflicts are high, some when they are low – this allows us to act proactively to mitigate risks of conflict.”

The third operational scenario of the department is patrolling. The activities in patrolling consist of making patrol routes and conducting patrol tasks. Before introduction of the WMAS, we found that patrol routes have been around for a long time and have not changed much. There are a number of set routes that forest rangers follow on a day-to-day basis. Each day typically begins with the “next route that has not yet been covered”, or it is more purposedriven if an incident (of conflict or animal mortality) needs to be investigated further. We also found that camera trapping decisions (i.e., locations of camera traps) were usually made by the department based on the experience of forest rangers and inputs from naturalists and wildlife behaviour experts. However, the decision-making did not consider data on animal sightings and the landscape information that was already gathered systematically by the application.

After introduction of the WMAS, the practitioners made some new patrol routes based on the simulated results. As mentioned by ranger A and ranger B,

“With the system, we can map out new patrol routes, considering its feasibility. For instance, there is little sense in creating an optimised patrol route if it is going through dificult terrain. With the new system, we can visualise patrol routes which are created based on historical data and highly local habitat information.”

“We can discern which patrol routes observe or sight more wildlife. Such visualisations can also reveal spatial blind spots. If there are certain geographical areas that aren’t been covered, we can figure that out too.

The simulated camera trap locations also led to a better understanding of the installation of camera traps in practice. As manager D mentioned,

“Camera traps are an important information source. The quality of this information is as good as the quality of the location of the camera trap. Having a rigorous way of understanding and identifying key locations helps us be more strategic about installing camera traps. Eventually, this leads to a better understanding of the inhabitants of the forests and leads to better conservation outcomes in the long run.

Through comparing the changes in operational scenarios, we found some concrete evidence of the viability and usefulness of our artefact design. The practitioners also reinforced our core design decisions of the WMAS.

## 8. Discussion

## 8.1. Theoretical contribution

First, our study contributes to descriptive knowledge concerning the problem space by identifying three main categories of afordances in wildlife management. To the best of our knowledge, there is no prior IS research dedicated to the design of an analytics system in wildlife management. Thus, a detailed understanding of the problem space is essential (Vom Brocke et al., 2019). By abstracting the diagnosis cycle, we identify a general set of requirements for wildlife management in terms of three categories of assessing, anticipating, and practising afordances, which are derived from related literature and practice. In addition, we also contribute to the problem space by taking a process-oriented view to understand the practices that the analytics system should aford: assess wildlife status, identify threats that may afect the status, and optimise patrol tasks to protect threatened wildlife.

Second, our study contributes to prescriptive knowledge concerning the solution space by ofering a set of design principles for analytics system design. By abstracting the design cycle, we identify our initial design principles, which reflect knowledge of action potentials (i.e., afordance), material properties (i.e., system features), and boundary conditions (i.e., application context). By abstracting the implementation cycle, our initial design is further refined and evaluated. Table 8 (changes are in bold) summarises the final set of design principles. These design principles reflect the ensemble nature of the IS artefact, which results from the ongoing refinement from both the researchers and the real-world context. The design principles as a nascent design theory constitute the major contribution of our study. This prescriptive knowledge not only enhances the understanding of the solution domain but also provides concrete guidelines that can be used to address a class of similar problems for future wildlife management projects.

The design principles are generalisable to a class of similar problems and systems. On the one hand, we diagnose a set of general requirements for the IS artefact to be built through a comprehensive review of biology management literature. These general requirements cover three main aspects of wildlife management that are widely considered by researchers and practitioners. Through several design and implementation iterations, we abstracted our design process to design principles that address these general requirements. On the other hand, data are available for other stakeholders in wildlife management. We find that wildlife-related data (e.g., observed number, locations, and poaching) are collected not only in the Indian wildlife department but also in many Southeast Asian and African countries (Critchlow et al., 2015; Xu et al., 2020). These wildlife data are critical resources to initiate the analytics projects. The availability of wildlife data will further increase the generalisability of our design principles for the WMAS.

Third, another major contribution of our study is the generalisation of two activities of data preparation and algorithm design when designing analytics systems through the ADR approach. In our project, wildlife data are collected from diverse sources. Thus, we need to classify and integrate the raw data according to their diferences and similarities. Furthermore, these data are usually fraught with various types of errors and thus need to be cleaned. The failure to manage and process large-scale datasets can result in ineficient data analysis (Müller et al., 2016). Therefore, we argue that data preparation is essential for the design of an analytics system. In addition, as the volume of the data increases, the traditional manipulation method using spreadsheets is no longer adequate. The algorithm plays a critical role in processing the large dataset and uncovering useful information embedded in these data (Günther et al., 2017). Therefore, we argue that the capabilities of the algorithm are also essential in the design of an analytics system.

Table 8. The revised set of design principles.

<table><tr><td>Affordance</td><td>Revised design principles for WMAS</td></tr><tr><td>Assessing affordances</td><td>DP1-a: Provide features to visualise the change in wildlife sightings number [material property], so that the system can afford the users to assess wildlife population size [action potential] in wildlife management [boundary conditions].DP1-b: Provide features to map the change in wildlife spatial locations [material property], so that the system can afford the users to assess wildlife distribution [action potential] in wildlife management [boundary conditions].</td></tr><tr><td>Anticipating affordances</td><td>DP2-a: Provide features to map the poaching areas and demonstrate the vegetation type and terrain type around the incident sites, so that the system can afford the users to identify threat of poaching on wildlife [action potential] in wildlife management [boundary conditions].DP2-b: Provide features to compare the number of human-wildlife conflicts in different regions and demonstrate the magnitude of the conflicts [material property], so that the system can afford the users to identify threat of human-wildlife conflict on the wildlife [action potential] in wildlife management [boundary conditions].</td></tr><tr><td>Practising affordances</td><td>DP3-a: Provide features to simulate wildlife channels with a 50-metre buffer [material property], so that the system can afford users to optimise patrol routes [action potential] in wildlife management [boundary conditions].DP3-b: Provide features to identify the key points in the simulated wildlife pathways by considering the landscape constraints [material property], so that the system can afford users to locate the best sites for camera traps [action potential] in wildlife management [boundary conditions].</td></tr></table>

We also contribute to the ADR approach by adding two principles of multi-source data integration and human complementing algorithm that can be used to guide these two new activities. The principle of multisource data integration indicates that researchers should collect and integrate the data from multiple sources to ensure the comprehensiveness of the dataset. For example, we collected information regarding poaching incidents from two diferent sources: poaching detection and wildlife mortality. In our research, we fused the two datasets because the mortality of wildlife may also be caused by poaching. If we only used one type of data, a considerable amount of useful information pertaining to poaching may be lost. The principle of the human complementing algorithm indicates that the algorithm should be supplemented with human experiences and domain knowledge (Günther et al., 2017). Algorithms exhibit considerable potential in processing large-scale datasets, uncovering useful information, and automatically making operational decisions (Markus, 2015). However, some studies indicate that human expertise is still needed when solving these complex problems, especially in examining the data (Seddon et al., 2017) and refining the insights (Sharma et al., 2014). For example, in our study, the initial simulated results may not be applicable in practice because they neglect some constraints in a real context. Thus, only complementing algorithm intelligence with human intelligence can derive useful information and insights for management practices.

## 8.2. Practical contribution

Our study has important practical implications for designing analytics systems that address wildlife management. Our artefacts that consist of required afordances, design principles, and system features are usable in wider practical applications because wildlife management is one of the most significant challenges not only in India but around the world. Although the artefacts of our study are co-created and abstracted from a singular setting, we believe that these results are generalisable and can be used by other stakeholders in a wide range of similar applications. Here, we provide two potential applications of how these artefacts can be used in future practice and research. First, stakeholders with the same type of data collected by ranger patrols can adopt our analytics system prototype. By using the system features, practitioners can obtain wildlife-related indicators in a timely and accurate manner, which can heighten their work eficiency. Second, the stakeholders, who hope to customise their own analytics system, can start to identify their own desired afordances and explore material properties to purposely design them by following our design principles.

## 8.3. Limitations and future research directions

In executing this project, we followed the elaborated Action Design Research guidelines (Mullarkey et al., 2019) and adapted it to our specific context. In the last evaluation cycle of the instantiated analytics system, we conducted a before-after analysis to gauge the change visà-vis the three types of WMAS afordances, namely assessing, anticipating, and practising afordances. The evaluation was based on qualitative interviews with key stakeholders who recounted how their practice had been impacted by the new system. However, in our evaluation process, we did not capture quantitative indicators to gauge the efectiveness of the system – and we acknowledge that this is a key limitation. Defining evaluation metrics for the system can contribute to the continuous refinement of the system. Future studies can extend our work by defining a set of monitoring and evaluation criteria for WMAS. We propose the following metrics in Table 9 to initiate the conversation. We believe that monitoring and evaluating the above metrics can help the project team continuously refine the system.

Another limitation of the study relates to the frequency with which the current data sets are refreshed. As noted in Appendix B, data are not being uploaded to the server in a timely manner due to existing infrastructure constraints. This limits the capabilities of the analytics in terms of the recency of analysis and reporting. Future research can also explore how more real time data analysis can be achieved in such a constrained environment.

Table 9. Monitoring and evaluation metrics.

<table><tr><td>Affordance</td><td>Monitoring and evaluation metric</td></tr><tr><td>Assessing affordances</td><td>1) Year-on-year trend of wild animal population in the region</td></tr><tr><td>Anticipating affordances</td><td>1) Reduction in number of poaching incidents from month-to-month2) Reduction in the number of human-animal conflict from month-to-month</td></tr><tr><td>Practising affordances</td><td>1) Month-to-month trend of the number of active patrols due to optimisation of routes2) Month-to-month trend of abandoned patrols3) Year-on-year trend of camera traps</td></tr></table>

## 9. Conclusion

Wildlife management is becoming increasingly critical under the circumstances of increasing global pressures. In this study, by collaborating with a wildlife department in India, we adopt the elaborated ADR approach to investigate how an analytics system should be designed in the wildlife management domain. A set of design principles for the WMAS is developed and tested through the cooperation of practitioners and researchers in several ADR intervention cycles. The output of our study is feasible and practical and can produce observable societal impacts in practice. Gholami et al. (2016) implore that the IS community should engage in impactful research and help create a green and sustainable world. We responded to this call by ofering a general IS solution in the wildlife management domain because a sustainable world means not only environmental sustainability but also the sustainability of biodiversity. Through our study, we hope to provide a springboard for more research to contribute to the understanding of how a broad class of information systems for sustainable wildlife management should be designed.

## Disclosure statement

No potential conflict of interest was reported by the authors.

## ORCID

Mingwei Li http://orcid.org/0000-0002-0805-6477 L.G. Pee http://orcid.org/0000-0003-3042-9011 M.S. Sandeep http://orcid.org/0000-0002-0241-5352

## References

Ågerfalk, P. J., & Wiberg, M. (2018). Pragmatizing the normative artifact: Design science research in scandinavia and beyond. Communications of the Association for Information Systems, 43, 68–77. https://doi.org/10. 17705/1CAIS.04304

Arnott, D., & Pervan, G. (2012). Design science in decision support systems research: An assessment using the Hevner, March, Park, and Ram Guidelines. Journal of the Association for Information Systems, 13(11), 923–949. https://doi.org/10.17705/1jais.00315

Baskerville, R., Baiyere, A., Gergor, S., Hevner, A., & Rossi, M. (2018). Design Science Research Contributions: Finding a Balance between Artifact and Theory. Journal of the Association for Information Systems, 19(5), 358–376. https://doi.org/10.17705/1jais. 00495

Chandra, L., Seidel, S., & Gregor, S. (2015). Prescriptive knowledge in IS research: Conceptualizing design principles in terms of materiality, action, and boundary conditions. 2015 48th Hawaii International Conference on System Sciences. https://doi.org/10.1109/HICSS.2015.485

Critchlow, R., Plumptre, A. J., Driciru, M., Rwetsiba, A., Stokes, E. J., Tumwesigye, C., Wanyama, F., & Beale, C. (2015). Spatiotemporal trends of illegal activities from

ranger-collected data in a Ugandan national park. Conservation Biology, 29(5), 1458–1470. https://doi.org/ 10.1111/cobi.12538

Cooper, R.G., Edgett, S.J., Kleinschmidt, E.J. (2002). Optimizing the stage-gate process: what best-practice companies do—I. Research-Technology Management,45 (5) 21–27. https://doi.org/10.1080/08956308.2002. 11671518

Danks, F., & Klein, D. (2002). Using GIS to predict potential wildlife habitat: A case study of muskoxen in northern Alaska. International Journal of Remote Sensing, 23(21), 4611–4632. https://doi.org/10.1080/01431160110113890

Du, W. (., Pan, S. L., Leidner, D. E., & Ying, W. (2019). Afordances, experimentation and actualization of FinTech: A blockchain implementation study. The Journal of Strategic Information Systems, 28(1), 50–65. https://doi.org/10.1016/j.jsis.2018.10.002

Fao. (2014). Sustainable wildlife management and biodiversity. Food and Agriculture Organization of the United Nations. Retrieved Date Accessed, 2014 from https:// www.cifor.org/library/5397/

Fayard, A.-L., & Weeks, J. (2014). Afordances for practice. Information and Organization, 24(4), 236–249. https:// doi.org/10.1016/j.infoandorg.2014.10.001

Gellert, A., Florea, A., Fiore, U., Palmieri, F., & Zanetti, P. (2019). A study on forecasting electricity production and consumption in smart cities and factories. International Journal of Information Management, 24(1), 39–54. https://doi.org/10.1016/j.ijinfomgt.2019.01.006

Gholami, R., Watson, R. T., Hasan, H., Molla, A., & Bjørn-Andersen, N. (2016). Information systems solutions for environmental sustainability: How can we do more? Journal of the Association for Information Systems, 17 (8), 521–536. https://doi.org/10.17705/1jais.00435

Gibson, J. J. (1977). The theory of afordances. In R. Shaw & J. Bransford (Eds.), Perceiving, Acting and Knowing: Toward an Ecological Psychology (pp. 67–82). Lawrence Erlbaum Associates.

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. Mis Quarterly, 37(2), 337–355. https://doi.org/10.25300/ MISQ/2013/37.2.01

Günther, W. A., Mehrizi, M. H. R., Huysman, M., & Feldberg, F. (2017). Debating big data: A literature review on realizing value from big data. The Journal of Strategic Information Systems, 26(3), 191–209. https://doi.org/10. 1016/j.jsis.2017.07.003

Hampton, S. E., Strasser, C. A., Tewksbury, J. J., Gram, W. K., Budden, A. E., Batcheller, A. L., Duke, C. S., & Porter, J. H. (2013). Big data and the future of ecology. Frontiers in Ecology and the Environment, 11 (3), 156–162. https://doi.org/10.1890/120103

Hevner, H., March, M., Park, P., & Ram, R. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75–105. https://doi.org/10.2307/25148625

Karanth, K. K., Gopalaswamy, A. M., DeFries, R., Ballal, N., & Gratwicke, B. (2012). Assessing patterns of human-wildlife conflicts and compensation around a central Indian protected area. PloS One, 7(12), p e50433. https://doi.org/10.1371/journal.pone.0050433

Kifner, C., Binzen, G., Cunningham, L., Jones, M., Spruiell, F., & Kioko, J. (2020). Wildlife population trends as indicators of protected area efectiveness in northern Tanzania. Ecological Indicators, 110. https://doi.org/10. 1016/j.ecolind.2019.105903

Krancher, O., & Luther, P. (2015). Software Development in the Cloud: Exploring the Afordances of Platform-as-

a-Service. Proceedings of the 36th International Conference of Information Systems, Texas, USA.

Lewis, K. P., Wal, E. V., & Fifield, D. A. (2018). Wildlife biology, big data, and reproducible research. Wildlife Society Bulletin, 42(1), 172–179. https://doi.org/10.1002 wsb.847

Maier, J. R., & Fadel, G. (2009). Afordance based design: A relational theory for design. Research in Engineering Design, 20(1), 13–27. https://doi.org/10.1007/s00163-008- 0060-3

Markus, M. L. (2015). New games, new rules, new scoreboards: The potential consequences of big data. Journal of Information Technology, 30(1), 58–59. https://doi.org/10. 1057/jit.2014.28

Markus, M. L., & Silver, M. S. (2008). A foundation for the study of IT efects: A new look at DeSanctis and Poole’s concepts of structural features and spirit. Journal of the Association for Information Systems, 9(10), 609–632. https://doi.org/10.17705/1jais.00176

Mullarkey, M. T., Hevner, A. R., & Ågerfalk, P. (2019). An elaborated action design research process model. European Journal of Information Systems, 28(1), 6–20. https://doi.org/10.1080/0960085X.2018.1451811

Müller, O., Junglas, I., Brocke, J., & Debortoli, S. (2016). Utilizing big data analytics for information systems research: Challenges, promises and guidelines. European Journal of Information Systems, 25(4), 289–302. https:/ doi.org/10.1057/ejis.2016.2

Norouzzadeh, M. S., Nguyen, A., Kosmala, M., Swanson, A., Palmer, M. S., Packer, C., & Clune, J. (2018). Automatically identifying, counting, and describing wild animals in camera-trap images with deep learning. Proceedings of the National Academy of Sciences, 115 (25), 5716–5725. https://doi.org/10.1073/pnas. 1719367115

Pan, S. L., & Pee, L. G. (2020). Usable, in-use, and useful research: A 3U framework for demonstrating practice impact. Information Systems Journal, 30(2), 403–426. https://doi.org/10.1111/isj.12274

Samson, F. B., & Knopf, F. L. (1993). Managing biological diversity. Wildlife Society Bulletin (1973-2006), 21(4), 509–514. https://www.jstor.org/stable/3783428

Sandhyarani, N. (2018). Essential Elements of Successful Wildlife Management. Retrieved Date Accessed, 2018 from https://animalsake.com/wildlife-management

Seddon, P. B., Constantinidis, D., Tamm, T., & Dod, H. (2017). How does business analytics contribute to business value? Information Systems Journal, 27(3), 237–269. https://doi.org/10.1111/isj.12101

Seidel, S., Chandra Kruse, L., Székely, N., Gau, M., Stieger, D., Pefers, K., Tuunanen, T., Niehaves, B., & Lyytinen, K. (2017). Design principles for sensemaking support systems in environmental sustainability transformations. European Journal of Information Systems, 27(2), 221–247. https://doi.org/10.1057/s41303- 017-0039-0

Sein, S., Henfridsson, H., Purao, P., Rossi, R., & Lindgren, L. (2011). Action Design Research. MIS Quarterly, 35(1), 37–56. https://doi.org/10.2307/23043488

Sharma, R., Mithas, S., & Kankanhalli, A. (2014). Transforming Decision-making Processes: A Research Agenda for Understanding the Impact of Business Analytics on Organisations. European Journal of Information Systems, 23(4), 433–441. https://doi.org/10. 1057/ejis.2014.17

Singh, M., & Kumara, H. (2006). Distribution, status and conservation of Indian gray wolf (Canis lupus pallipes) in Karnataka, India. Journal of Zoology, 270(1), 164–169. https://doi.org/10.1111/j.1469-7998.2006.00103.x

Strong, D. M., Volkof, O., Johnson, S. A., Pelletier, L. R., Tulu, B., Bar-On, I., Trudel, J., & Garber, L. (2014). A theory of organization-EHR afordance actualization. Journal of the Association for Information Systems, 15(2), 53–85. https://doi.org/10.17705/1jais.00353

Sussman, G. (1983). Action Research: A Sociotechnical Perspective. In G. Morgan (Ed.), Beyond Method: Strategies for Social Research, (pp. 95–113). Sage Publications.

Tim, Y., Pan, S. L., Bahri, S., & Fauzi, A. (2018). Digitally enabled afordances for community-driven environmental movement in rural Malaysia. Information Systems Journal, 28(1), 48–75. https://doi.org/10.1111/isj.12140

Tobler, M. W., Carrillo-Percastegui, S. E., Pitman, R. L., Mares, R., & Powell, G. (2008). An evaluation of camera traps for inventorying large- and medium-sized terrestrial rainforest mammals. Animal Conservation, 11(3), 169–178. https://doi.org/10.1111/j.1469-1795.2008. 00169.x

Volkof, O., & Strong, D. M. (2017). Afordance theory and how to use it in IS research. In Galliers R.D. & Stein, M., (Eds), The Routledge Companion to Management Information Systems. Routledge Handbooks Online. doi: 10.4324/9781315619361.ch16

Vom Brocke, J., Winter, R., Hevner, A., & Maedche, A. (2019). Accumulation and evolution of design knowledge in design science research: A journey through time and space. Journal of the Association for Information Systems, 29(3), 379–385. doi: 10.17705/1jais.00611

Watson, H. J. (2014). Tutorial: Big Data Analytics: Concepts, Technologies, and Applications. Communications of the Association for Information Systems, 34(1), 1247–1268. https://doi.org/10.17705/1CAIS.03465

Weisenborn, G. (2018). United Nations Sustainable Development Goals. United Nations.

Xu, L., Gholami, S., Mc Carthy, S., Dilkina, B., Plumptre, A., Tambe, M., Singh, R., Nsubuga, M., Mabonga, J., Driciru, M., Wanyama, F., Rwetsiba, A., Okello, T., Enyel, E. (2020). Stay Ahead of Poachers: Illegal Wildlife Poaching Prediction and Patrol Planning Under Uncertainty with Field Test Evaluations. IEEE 36th International Conference on Data Engineering, Dallas, TX, USA, 1898–1901, doi:DOI: 10.1109/ICDE48307.2020.00198

## Appendix A

Table A1. Elaborate ADR cycles and activities in each cycle

<table><tr><td></td><td>Diagnosis</td><td>Data preparation</td><td>Design</td><td>Implementation</td></tr><tr><td>Problem formulation (P)</td><td>-Identify the research opportunity-Formulate the research question- Conduct literature review to understand the wildlife management domain (i.e., problem space and solution space)</td><td>- Understand the data collection process</td><td>- Examine research that informs the conceptualisation of design principles</td><td>- Examine research on analytics techniques</td></tr><tr><td>Artefact creation (A)</td><td>- Identify the preliminary requirements for the analytics system- Refine these preliminary requirements</td><td>- Data integration- Data cleaning</td><td>- Identify the initial design principles- Revise the initial design principles</td><td>- Instantiate the initial design principles into a prototype system, which consists of algorithms and user interface- Revise the prototype system</td></tr><tr><td>Evaluation (E)</td><td>- Evaluate whether the requirements meet user needs</td><td>- Evaluate the data preparation process</td><td>- Evaluate adherence between the initial design principles and the real-world problems</td><td>-Conduct field test with practitioners-Analyse the system usage data</td></tr><tr><td>Reflection (R)</td><td>- Reflect on the diagnosis cycle to refine the preliminary requirements</td><td>- Optimise data preparation process</td><td>- Reflect on the design cycle to refine the initial design principles</td><td>- Reflect on the implementation cycle to refine the initial system features</td></tr><tr><td>Learning (L)</td><td>- Abstract the learning into a general set of requirements- Share outcome with practitioners</td><td>- Abstract a new activity of data preparation in analytics ADR project- Share outcome with practitioners</td><td>- Abstract the learning into a set of design principles for a class of problems- Share outcome with practitioners</td><td>- Abstract a new activity of algorithm design in analytics ADR project- Share outcome with practitioners</td></tr></table>

## Appendix B

![](/api/attachments/YTEHWNY4/fulltext/images/5b0777af3837a0b63974d2390b2994c2a47c2be39460b85a2318068c4f4dee93.jpg)  
Figure A1. The data collection and data use

Data pertaining to wildlife are collected by using an information system. The information system mainly consists of an Android-based application and a database server. The typical use of the system is shown in Figure A1 above. The left part of the figure shows the process of using the Android-based application to collect wildlife-related data such as wildlife presence, wildlife mortality, and illegal human activities. Every workday, patrol rangers from the implementation department set out to collect wildlife-related data on their patrol routes. At the same time, they open the application and document signs of th wildlife information they observe. The information mainly includes animal name, number, time, location, vegetation type, terrain type, and human-wildlife conflict magnitude (e.g., small or medium). Once rangers complete their patrol, they stop the application and save the collected data. These saved data will be uploaded to the system server as and when the team is able to access data connection. Typically, once a week, someone from the team drives outside the perimeter of the “core forest” area to access mobile data signals and upload the data (as mobile phone towers are prohibited inside the core area). The right part of the figure shows the use of these data. Once data from all the teams are received, staf from a third-party system developer will clean and analyse the data – a process that can take anywhere between a week to two weeks depending on the timeliness of incoming patrol data from diferent teams. In the current system, the staf only prepares a monthly report for the use of the management department. The report is usually generated by summarising key metrics such as the number of wildlife sightings and geographic visualisation of the wildlife. This report enables the management to track rangers’ patrolling work in protected areas and to understand the wildlife status of the investigated areas.

## Appendix C

Algorithms are the key material properties of the WMAS, which are important to support the function of system features that allow for the required afordances in wildlife management. Table A2 summarises these system features, used data and corresponding algorithms or analytics tools. We also demonstrate one example of the algorithms for wildlife distribution by mapping wildlife spatial locations (see Figure A2).

Table A2. Data and algorithms used in the features

<table><tr><td>System features</td><td>Used data</td><td>Algorithms or analytics tools to support the features</td></tr><tr><td>Feature1-a: Visualise the number of wildlife sightings</td><td>Fields of animal name, number of wildlife sighting, and time in the wildlife data</td><td>A statistical algorithm is developed by using R programming (a free software environment for statistical computing and graphics) for subtotalling the number of different wildlife sightings at a specific time period.</td></tr><tr><td>Feature1-b: Map the wildlife spatial locations</td><td>Fields of animal name, location (e.g., longitude and latitude), terrain type, and vegetarian type in the wildlife data</td><td>An algorithm is developed using R programming to integrate the two types of information (i.e., wildlife spatial locations and Indian geographic data) into visualisations by using maps.</td></tr><tr><td>Feature2-a: Map the historical poaching areas</td><td>Fields of threat type (e.g., hunting, poaching, or snaring) and location (e.g., longitude, latitude) in the poaching data</td><td>An algorithm is developed using R programming to integrate the two types of information (i.e., poaching spatial locations and Indian geographic data) into visualisations by using maps.</td></tr><tr><td>Feature2-b: Compare the human-wildlife conflicts in different regions</td><td>Fields of animal name, magnitude (e.g., small, medium, or large), and region in the human-wildlife conflict data</td><td>A statistical algorithm is developed by using R programming for subtotalling the number of human-wildlife conflicts in different regions.</td></tr><tr><td>Feature3-a: Simulate the wildlife pathways</td><td>Fields of animal name and location (e.g., longitude, latitude) in the wildlife data</td><td>The wildlife pathways are simulated by using the ArcGIS software, a professional geographic information system for mapping and spatial reasoning.</td></tr><tr><td>Feature3-b: Identify the key points in the simulated wildlife pathways</td><td>Fields of animal name and location (e.g., longitude, latitude) in the wildlife data</td><td>The potential camera trap sites are recommended based on the simulated wildlife pathways through using the ArcGIS software.</td></tr></table>

```r
#######1.2 algorithm for mapping the wildlife spatial locations
output$insighting <- renderPlotly({
#access data
animal_geo <- plot_mapbox(mode = 'scattermapbox')
realsighting <- realsighting[which(realsighting$AnimalName %in% input$select_animal),]
data <- realsighting
#process data
animal_geo <- animal_geo %>%
add tickers(
data = data, x = ~long_Degrees, y = ~lat_Degrees, split = ~AnimalName,
size = 8,
hoverinfo = "text", alpha = 0.5
) %>%
#visualise results
layout(title = 'Geographic Location Visualization',
font = list(color = 'black'),
plot_bgcolor = 'light', paper_bgcolor = 'light',
mapbox = mymapbox,
legend = list(orientation = 'h',
font = list(size = 15)),
margin = list(l = 25, r = 25,
b = 25, t = 25,
pad = 2))
animal_geo
})
```  
Figure A2. Algorithm for mapping the wildlife spatial locations

We use the scatter plots on maps (see https://plotly.com/r/maps/) in R programming to design the algorithm for wildlife distribution (Feature1-b). This algorithm consists of three main instructions: access wildlife data (lines 4–6), process wildlife location data (lines 8–13), and visualise results on maps (lines 15–23). The function of the three instructions is to make scatter plots on maps to demonstrate the wildlife spatial distribution.

![](/api/attachments/YTEHWNY4/fulltext/images/180fea75be8376166034b1f71e057c9659d606fa86f924bf104dbcedf89fa104.jpg)  
Figure A3. Login page of the wildlife management analytics system

Figure A3 shows the login page of the WMAS. The users log in the system by their username and password.  
![](/api/attachments/YTEHWNY4/fulltext/images/fe58b1ea56bb54e9a5b6c5558e21b6556760a6e35a9df26af53fbf8d39182eb1.jpg)  
Figure A4. User interface for the wildlife status

The user interface mainly consists of four parts (see Figure A4).

① Tab panel (e.g., wildlife status)

② System features (e.g., wildlife distribution and population size)

③ Result interface

④ Sidebar panel
