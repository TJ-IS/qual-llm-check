---
otero_id: 962
otero_key: "QGVU72FR"
title: "Understanding key issues in designing and using knowledge flow networks: An optimization-based managerial benchmarking approach"
authors: "Su Dong; Monica Johar; Ram Kumar"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.04.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Understanding key issues in designing and using knowledge <sup>fl</sup>ow networks: An optimization-based managerial benchmarking approach

Su Dong, Monica Johar, Ram Kumar ⁎

Belk College of Business, University of North Carolina at Charlotte, NC 28223, United States

## a r t i c l e i n f o

Article history: Received 29 July 2011 Received in revised form 20 February 2012 Accepted 29 April 2012 Available online 5 May 2012

Keywords: Knowledge management Knowledge sharing Optimization Organization design

## a b s t r a c t

There is an increasing recognition that knowledge can be an organization's source of competitive advantage. Hence, knowledge management (KM) has been extensively researched. Prior knowledge management research has recognized the importance of making individual knowledge available throughout the organization. Most KM research, however, has thus far focused on a technology-based KM strategy with relatively little discussion on how knowledge can be effectively shared using organizational social relationships. This paper focuses on how knowledge-intensive organizations can design and use “knowledge <sup>fl</sup>ow networks (KFNs)” in order to facilitate knowledge sharing. Designing and using KFNs to maximize knowledge sharing is a complex problem. We formulate a mixed integer programming model (MIP), and present a heuristic in order to facilitate systematic analysis and understanding of effective KFNs. We consider organizations that support multiple skills and have workers with varying levels of competence who are connected through IT-facilitated organizational social relationships. Our results, based on computational experiments, provide several interesting insights and intelligence into the design of an effective KFN. First, our results highlight that average workers play a vital bridging role in knowledge sharing. Second, social networking concepts of ties and cohesiveness are used to better understand the dynamics of knowledge sharing. The importance of indirect relationships between expert workers and the network effects due to indirect relationships are illustrated. For effective KM, we also illustrate how organizations can reduce the total number of ties required in a multi-skill environment. In our model extensions, we study the impact of worker turnover and knowledge depreciation on the design and use of effective KFNs. Managerial implications of these results are discussed. The model and solution procedure proposed in this paper can serve as a managerial benchmarking framework for effective management of KFNs.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

There is a growing recognition that employees' knowledge is an organization's most valuable asset, particularly in knowledge-intensive environments such as consulting, research, and IT service delivery [16,18,19]. Such organizations consider knowledge creation [43] and knowledge application [23] to be vital to organizational performance. Knowledge management research has recognized the concept of “a knowledge-creating company” [43]. The concept of “knowledge reservoirs” has also been proposed as a source of long-term competitive advantage [2]. Prior research has recognized that “making personal knowledge available to others is the central activity of the knowledgecreating company. It takes place continuously and at all levels of the organization” [43]. Hence, <sup>fi</sup>rms are increasingly investing in Knowledge Management (KM) projects expecting to improve employees' knowledge levels [22].

Most KM research has thus far focused on information technologies [13,15], with relatively little discussion on how knowledge can be shared effectively among employees using organizational social relationships [39]. In practice, however, organizations are <sup>fi</sup>nding that employees often prefer to consult their peers and colleagues (organizational social relationships) in order to acquire knowledge, rather than access electronic knowledge bases [13]. Recognizing the importance of using organizational social relationships to transfer knowledge, an increasing number of Chief Knowledge Of<sup>fi</sup>cers (CKOs) are moving from a technologicalbased KM strategy to a socialization-based KM strategy [42]. Such a strategy uses organizational information <sup>fl</sup>ow networks (IFNs) to facilitate knowledge sharing [42]. Such IFNs use ties (or information <sup>fl</sup>ow connections) between individuals in order to transfer knowledge. Recent research [18] has illustrated that the structure of IFNs and associated knowledge sharing behavior signi<sup>fi</sup>cantly impact organizational performance and employees' knowledge level.

Knowledge management research has only recently begun to focus on designing effective “knowledge <sup>fl</sup>ow networks” (KFNs) [25,36,53]. In this paper, we use the term KFNs to refer to organizational IFNs that facilitate knowledge sharing. KFNs can be studied from two perspectives. First, organizations are increasingly interested in using existing

KFNs effectively for KM [25,53]. This is the use perspective. Second, organizations are also interested in designing effective KFNs as a part of organization design initiatives [36]. Leading consulting organizations such as IBM recognize the importance of optimizing social networks in the context of KM. For example, “IBM Global Business Services — offers a social network analysis (SNA) service designed to help reveal a multitude of underlying personnel issues, such as where collaboration falls apart, where talent and expertise could be better used, where decision-making gets bogged down, and where opportunities for innovation are being lost…..While SNA can pinpoint problems and improvement opportunities, social network optimization (SNO) provides decision support for what to do next” (http://domino.watson.ibm.com/odis/odis.nsf/pages/ board.13.html). Understanding effective KFNs allows organizations to compare their existing KFNs with effective KFNs. This, in turn, provides managerial guidance on what to do next. Hence, design and use of effective KFNs is an important problem, with signi<sup>fi</sup>cant real-world interest. However, academic research on this problem is limited.

We focus on the following research question: how should knowledgeintensive organizations design and use their KFNs in order to maximize employees' knowledge level (over a planning horizon) through sharing under different organizational environments? In order to answer this question, we examine organizations that support multiple skills and have workers with varying levels of knowledge in these skills. These workers are connected to each other through IT-facilitated organizational social relationships. Designing and using KFNs to maximize knowledge sharing is a complex problem. We formulate a Mixed Integer Programming Model (MIP), and present a heuristic in order to facilitate systematic analysis and understanding of the above research question. In summary, the model and solution procedure proposed in this paper can serve as a managerial benchmarking framework for effective management of KFNs.

Our computational results provide several interesting insights and intelligence into the design of an effective KFN. First, our results highlight the important role of average workers. In contrast to the common practice of encouraging knowledge sharing between experts and novices, we <sup>fi</sup>nd that most knowledge sharing happens between average and expert workers, followed by knowledge sharing between average and novice workers. Second, the value of a direct tie is signi<sup>fi</sup>cantly enhanced by indirect ties. Cohesive groups of experts allow less competent workers to access more experts through indirect ties. Such cohesive groups are less important for lower skilled worker groups. Third, we examine the impact of number of skills supported by an organization on an effective KFN. Organizations supporting multiple skills need to create direct ties between workers with complementary skill sets, particularly between experts. Such ties tend to be used extensively, which reduces the number of direct ties needed as the number of skills supported by the organization increases. In our model extensions, we study the impact of worker turnover and knowledge depreciation on the design and use of effective KFNs. We <sup>fi</sup>nd that for effective KM, organizations need to compensate for high worker turnover and high knowledge depreciation by encouraging the creation of more direct ties and creating more cohesive groups of workers.

The rest of this paper is organized as follows. Section 2 discusses related literature that serves as the foundation for our research. The mathematical model of KFNs and solution procedure to solve this model is discussed in Sections 3 and 4, respectively. Design of the simulation-based experiments is described in Section 5. Computational results are the focus of Section 6. Section 7 discusses the performance of the proposed Heuristic. Model extensions are presented in Section 8. Sections 9, 10, and 11 focus on managerial implications and conclusions, limitations and future research, and conclusions respectively.

## 2. Literature review

Our research integrates concepts from prior research on using and creating organizational social relationships, knowledge management using organizational social relationships, and social network measures.

## 2.1. Using and creating organizational social relationships

Prior research on knowledge management shows that the strength of organizational social relationships (ties) signi<sup>fi</sup>cantly impacts the ef-<sup>fi</sup>ciency of knowledge sharing [7,13]. We use the term “tie” in order to refer to relationships resulting from sustained information exchange due to repeat interactions. We consider two types of ties between workers that have been identi<sup>fi</sup>ed in prior research as being likely to be used for knowledge transfer: strong ties and weak ties [6,24,38,47]. Strong ties occur between workers who know each other directly through organizational relationships. Workers connected by weak ties do not know each other directly, but have strong ties with another (intermediate) worker. A common worker plays a bridging role that allows the two workers to get acquainted and to share knowledge with each other. Direct ties (strong ties) are more ef<sup>fi</sup>cient than indirect ties (weak and performative ties) when used to transfer knowledge [26]. However, indirect ties allow workers to access larger number of colleagues as compared to direct ties [11,26]. In addition, it is important to note that all direct ties are not equally ef<sup>fi</sup>cient and their ef<sup>fi</sup>ciency often depends on the strength of the relationship. In order to develop strong ties between workers, considerable amount of time and effort is required, while weak ties could exist between acquaintances who share common contacts [11,26].

There is a growing body of research on understanding factors that in-<sup>fl</sup>uence the formation of social ties. Workers are required to spend time in cultivating such direct ties [26]. For example, workers may need to frequently meet with each other and attend common meetings. Kotlarsky and Oshri [33] present two case studies at SAP and LeCroy to illustrate the importance of establishing social ties for knowledge sharing among distributed IS development teams. They recommend face-to-face interactions and frequent communications (via email or instant messaging) as an effective mechanism for creating social relationships. In addition, organizations could also facilitate desired ties via reporting relationships, colocation, project experience, etc. [www.orgnet.com, 24,47].

There is a growing body of research on mining social networks and expertise pro<sup>fi</sup>ling. Social networks can be mined from different types of organizational data including email, wikis, blogs [24,50], and social network information [31]. For example, Pass It Along is a system developed by IBM to help organizations take a collaborative approach to knowledge sharing based on social network information (www. ibm.com/developerworks/web/library/wa-piabeta/index.html). Expertise pro<sup>fi</sup>ling is possible using commercially available tools such as KIN and Tacit Systems EKG [13], Collaboration-and-Expertise-Networks (www.autonomy.com), Knowledge Xchanger (http://www.comintell. com), and Iknow (http://www.iknow.us.com/Pages/Expertise.asp) or in-house developed tools such as Microsoft SPUD [15]. Other tools capable combining social network mining with expertise pro<sup>fi</sup>ling include SABA Social (www.saba.com/enterprise-social-networking) and IBMGBS Practitioner Portal [3].

This stream of literature is relevant since business intelligence regarding social networks and expertise pro<sup>fi</sup>ling is critical for designing optimal KFNs.

## 2.2. Knowledge management using organizational social relationships

IS researchers are increasingly interested in knowledge management using social relationships [1]. In addition, prior research on social networking and organizations has recognized that “the ability of a <sup>fi</sup>rm to be productive depends not only on the talents of its employees but largely on the way in which they interact” [28].

Cowan and Jonard [12] use simulation to study the impact of different types of network structures in the context of knowledge diffusion across organizations. Levine and Prietula [39] use agent-based simulation to study the impact of different types of ties between workers on knowledge sharing. They illustrate that having some performative ties in an organization improves average task completion times. Dong et al. [18] propose a model integrating social network information, employee knowledge, and employee availability to benchmark and manage the performance of knowledge‐intensive service organizations. Their objective is to maximize the organizational <sup>fi</sup>nancial performance for a given social network. Practitioners are also recognizing the importance of using social network information as well as employee information to facilitate knowledge sharing, and have built tools in order to do so. Examples of such tools include SABA Social (www.saba.com/enterprise-socialnetworking) and IBMGBS Practitioner Portal [3]. The focus of these tools is on integration of worker characteristics and social network information rather than on systematic design and use of KFN's. Existing research as well as practice discussed above has mostly focused on effectively using existing organizational social networks for different objectives. They assume the social network to be pre-de<sup>fi</sup>ned and static. In contrast, in this research our focus is on the design of optimal KFN's, with an objective to maximize the overall knowledge level of the organization.

More recently, researchers have begun to focus on the design of organizational social networks with an objective to improve knowledge management in organizations. Leung and Glissmann [36] study the optimal design of organizational social networks to improve employee skill development. They adopt a clustering approach which connects employees based on their attributes and resources. Their clustering approach does not consider the dynamic nature of employee's knowledge and does not consider indirect relationships between workers and any overhead associated with knowledge provision. Hansen [26] examines knowledge sharing across organizational subunits and <sup>fi</sup>nds that establishing direct relationships between workers in different subunits facilitates effective knowledge transfer. Zhuge [53] proposes a framework that is, perhaps, most closely related to our work. His framework combines social relationships of employees with their knowledge level and knowledge sharing (creation) capability, to facilitate the design of a knowledge <sup>fl</sup>ow network. His framework uses trial and error and does not maximize the overall knowledge level for the organization. In addition, it does not consider indirect ties between workers, the overhead associated with providing help, the strength of a relationship, or the time associated with knowledge sharing, in determining the desired social network. In this research, we propose a model and solution procedure which can serve as a managerial benchmarking framework for KFN optimization and management. This research is different from the ones discussed above since we allow organizations to create social ties to manage the KFNs with an objective to maximize the overall knowledge level for the organization. In our model, we consider: different types of social ties (direct and indirect), strength of a relationship, the cost of providing knowledge, an organization that supports multiple skills, a heterogeneous workforce with different levels of knowledge in each skill, and workers who differ in terms of the importance they have for each skill. The proposed model can be used to facilitate understanding of what constitutes an effective (optimal) KFN. It integrates and further develops ideas from prior research that has modeled knowledge sharing.

## 2.3. Social network measures for knowledge management

Social Network Analysis (SNA) has recently been used to “visualize and understand the myriad of relationships that can either facilitate or impede knowledge creation and transfer” [29]. SNA can be used to study bottlenecks, isolation, and subgroups in organizational environments [29]. A variety of social network measures have been proposed to facilitate SNA. Everett and Borgatti [20] categorize them into individual measures and group measures. Individual measures such as degree centrality allow organizations to identify key players in the organization. Group measures allow organizations to study the dynamics within and between groups. The rest of this section focuses on social network measures appropriate for studying KFNs.

Group measures are increasingly being used to understand knowledge sharing in organizations. Hansen [25] introduces the concept of knowledge networks to understand the asymmetry in knowledge sharing among subunits (groups) of a <sup>fi</sup>rm. He <sup>fi</sup>nds that the external connections of a subunit (between group centrality) and the extent of similarity between subunits impact knowledge sharing and performance. In addition, Hansen [26] proposes that types of ties between groups (sub units) also play an important role. Another important group measure considered in SNA is group cohesiveness. Bajaj and Russell [4] have focused on optimizing group cohesiveness when allocating work<sup>fl</sup>ows to improve group performance. They argue that group cohesiveness contributes to organizational performance, job satisfaction, and worker motivation. Low group cohesiveness could negatively impact team's capability to create knowledge. They measure group cohesiveness as the number of links between members of the subgroups, divided by the theoretical maximum number of links possible between the members.

Cross et al. [13] examine factors that support knowledge creation and knowledge sharing in social networks. They <sup>fi</sup>nd that the ability to get timely access to a knowledge worker possessing the desired knowledge is critical for effective knowledge sharing. Note that, knowledge workers may not be always willing (based on the type of relationship) and available to share knowledge. Additionally, knowledge level of workers' changes overtime, causing the value of the knowledge sharing relationships to also change over time. Therefore, we propose that, in addition to the standard individual and group measures, it is important to measure the extent to which the relationships (between individuals and groups) are actually used for knowledge sharing over a planning horizon.

Organizations ability to create knowledge is also signi<sup>fi</sup>cantly impacted by “the value system that evaluates, justi<sup>fi</sup>es, and determines the quality of knowledge” [43]. Therefore, we use cumulative knowledge level, knowledge diffusion, and workforce heterogeneity, as important measures of an organization's competitive advantage. We de<sup>fi</sup>ne workforce heterogeneity as the variation in knowledge across the workforce. Organizations that create and apply knowledge would strive to encourage knowledge diffusion, in order to maximize knowledge levels and minimize knowledge variability. Knowledge diffusion can be measured as the change in the cumulative knowledge level and knowledge variability of the workforce over time.

## 3. Model development

We model the problem of designing optimal knowledge <sup>fl</sup>ow networks within a <sup>fi</sup>rm for effective knowledge management. The use of KFNs for effective knowledge management is illustrated in Fig. 1. We consider an organization with a heterogeneous workforce that supports multiple skills. These workers are connected with each other via organizational ties. Since organizations hire workers for particular jobs (such as <sup>fi</sup>nancial consulting, business analyst) they expect each worker to have competencies in skill sets that match the job descriptions. Financial consultants might be expected to have a high level of knowledge in <sup>fi</sup>nancial skills and some computer skills. Similarly, business analysts might be expected to have a mix of computer skills and business functional knowledge. Organizations might weight computer skills more highly in the case of business analysts. We model this scenario by assuming that each worker has a set of skills, a level of knowledge for each skill, and a weight for each skill, as illustrated in Fig. 1. The <sup>fi</sup>rm needs to facilitate knowledge transfer between selected pairs of workers during each period in a planning horizon, which is comprised of multiple time periods. Our model identi<sup>fi</sup>es the best set of knowledge transfers in each period, in order to maximize the total weighted knowledge level of the organization over a planning horizon. It is important to note that the length of each period is context-speci<sup>fi</sup>c and could be one day, one week, one month, etc. During any period, a worker may or may not be identi<sup>fi</sup>ed to transfer or acquire knowledge. Moreover, workers may provide and acquire knowledge in the same period. Note that we treat knowledge transfer over direct and indirect relationships as directional. For example, if worker B transfers knowledge to worker A, it does not suggest any reverse knowledge <sup>fl</sup>ow from A to B.

![](/api/attachments/QGVU72FR/fulltext/images/74b7335fc145da8a5d2e1c1d6e74eac38691ecf24cc2a425b6bb5b03608f792c.jpg)  
In this example, in period t, worker B is identified to transfer knowledge to worker A in skill two using an existing direct tie between A and B. It takes one period for worker B to complete the knowledge transfer. At the same time, worker A is identified to transfer knowledge to worker C in skill one using an indirect tie between A and C. It takes two periods for worker A to complete the knowledge transfer since indirect ties are less efficient. In period t + 1, worker B finishes knowledge transfer to worker A, and worker A's knowledge in skill two is updated However, worker A requires one more period to transfer knowledge to worker C as a result of assignments made in period t. In period t + 1, worker C is identified as the best candidate to transfer knowledge to worker D, in skill two. Since there is no existing direct tie, a direct tie between workers C and D needs to be created. In this example it takes 5 time periods for establishing the direct tie, while it only takes one period for worker C to transfer knowledge after the tie is created. Thus, the total time that worker D takes to receive knowledge from worker C sums up to six periods (time to create a direct tie plus the time to transfer knowledge).  
Fig. 1. Creating and using KFNs to transfer knowledge.In this example, in period t, worker B is identi<sup>fi</sup>ed to transfer knowledge to worker A in skill two using an existing direct tie between A and B. It takes one period for worker B to complete the knowledge transfer. At the same time, worker A is identi<sup>fi</sup>ed to transfer knowledge to worker C in skill one using an indirect tie between A and C. It takes two periods for worker A to complete the knowledge transfer since indirect ties are less ef<sup>fi</sup>cient. In period t+1, worker B <sup>fi</sup>nishes knowl edge transfer to worker A, and worker A's knowledge in skill two is updated. However, worker A requires one more period to transfer knowledge to worker C as a result of assignments made in period t. In period t+1, worker C is identi<sup>fi</sup>ed as the best candidate to transfer knowledge to worker D, in skill two. Since there is no existing direct tie, a direct tie between workers C and D needs to be created. In this example, it takes 5 time periods for establishing the direct tie, while it only takes one period for worker C to transfer knowledge after the tie is created. Thus, the total time that worker D takes to receive knowledge from worker C sums up to six periods (time to create a direct tie plus the time to transfer knowledge).

As mentioned earlier, direct ties occur between workers who know each other directly through organizational relationships. Examples of such direct relationships include of<sup>fi</sup>ce mates, close friends, team members, etc. In Fig. 1, in period t, workers A–B, B–C, and A–D, have direct relationships with each other. Workers connected by indirect relationships do not know each other directly, but have direct relationships with one or more (common) workers. Common workers play a bridging role that allows the two workers to get acquainted and share knowledge with each other. In Fig. 1, in period t, workers A–C, and B–D, have indirect ties with each other. We model the ef<sup>fi</sup>ciency of knowledge transfer process as a function of the type of tie and the strength of the relationship. In general, direct ties are more ef<sup>fi</sup>cient than indirect ties. The strength of individual direct ties is lower for newer relationships (the width of the line indicates the strength of a tie in Fig. 1). Knowledge transfer ef<sup>fi</sup>ciency is also affected by the status of the worker. That is, we consider reduced knowledge acquisition ef<sup>fi</sup>ciency (overhead cost) for workers who acquire and provide knowledge at the same time. The time to transfer knowledge between a pair of workers, for a given skill, depends on the knowledge transfer ef<sup>fi</sup>ciency and the amount of knowledge been transferred in that skill (which depends on knowledge difference between the workers). A detailed example of knowledge sharing using organizational ties is illustrated in Fig. 1.

The mechanism for creating and using KFNs to transfer knowledge is based on the following concepts: expertise pro<sup>fi</sup>ling, identi<sup>fi</sup>cation of existing social networks, identi<sup>fi</sup>cation of workers who can transfer knowledge, identi<sup>fi</sup>cation of ties (parts of the KFN) to be used in transferring knowledge, creation of new ties (if required). The concepts of expertise pro<sup>fi</sup>ling and identi<sup>fi</sup>cation of existing social networks are empirically grounded as mentioned in Section 2.1. Identifying workers and ties for knowledge transfer (social network use), and creation of new ties (KFN design) are often ad hoc. Practitioners have recognized that “there has been little effort put into systematic ways of leveraging knowledge that is embedded in people and relationships” [14]. Hence, the need for a systematic approach for recommending which existing ties to use and which new ties to create, in order to maximize knowledge sharing. It is important to note that these recommendations are dynamic and vary over time. The following model section describes our proposed approach to social network optimization.

## 3.1. Model formulation

Mathematical modeling is a useful tool to understand key variables that describe a problem and their relationships. The model variables described in Table 1 represent the different elements of the problem of designing KFNs. In addition, mathematical modeling helps understand the relationships between different variables, and produces a solution that can serve as a benchmark. Understanding the relationship between the current state of an organization and the managerial benchmark produced by the model facilitates organizational change [40]. This approach is appropriate in the context of a knowledge management problem where the goal is to design optimal KFNs that maximize the overall knowledge level of the organization. We model the problem of designing KFNs using mixed integer programming (MIP). This approach is appropriate in scenarios where some variables (such as assigning a worker to participate in knowledge sharing) are binary and others (such as worker knowledge levels) are continuous in value.

Major model assumptions and their justi<sup>fi</sup>cations are summarized in Table 2. We consider the planning horizon to be divided into a set of discrete periods $t { \in } \{ 1 , . . , T \} .$ . The length of each period represents a context speci<sup>fi</sup>c unit of time after which the organization re-assesses the knowledge levels of its workers. In each period, the organization may create new direct ties or use existing direct and indirect ties, for effective knowledge management.

Table 1  
Major model variables and decision variable.

<table><tr><td>Symbol</td><td>Definition</td><td>Type</td></tr><tr><td> $X_{kls\_i}^{t}$ </td><td>=1 if worker k transfers knowledge in skill s to worker l using tie i during period t; =0 otherwise. k, l∈{1, 2,..., K}. Note that  $X_{kls\_i}^{t}$  and  $X_{kls\_i}^{l}$  are two different variables.</td><td>Decision variable</td></tr><tr><td>K</td><td>Total number of workers</td><td rowspan="2">Exogenous variables</td></tr><tr><td>T</td><td>Planning horizon</td></tr><tr><td>S</td><td>Total number of skills supported by the organization</td><td></td></tr><tr><td> $\beta_{ks}$ </td><td>Relative importance of worker k&#x27;s knowledge in skill s to the organization, with  $\beta_{ks} \in (0, 1), \sum \beta_{ks} = 1$ </td><td></td></tr><tr><td> $\alpha_{k\_i\_busy}$ </td><td>Efficiency of acquiring knowledge $^s$ using tie i (i=0, 1 represent direct, indirect ties respectively).</td><td></td></tr><tr><td> $\alpha_{k\_i\_idle}$ </td><td>Workers experience a reduced knowledge acquisition efficiency when simultaneously providing and acquiring knowledge i.e.,  $\alpha_{k\_i\_busy} < \alpha_{k\_i\_idle}$ .</td><td></td></tr><tr><td> $\varpi_{is}$ </td><td>(Time coefficient) Time taken to transfer a unit of knowledge in skill s using tie i (i=0,1 represent direct, indirect ties respectively)</td><td></td></tr><tr><td>θ</td><td>Time to create direct ties</td><td></td></tr><tr><td> $W_{ks}^{t}$ </td><td>Worker k&#x27;s knowledge level in skill s at the beginning of period t, with  $W_{ks}^{t} \in [W_{sMin}, W_{sMax}], W_{sRange} = W_{sMin} - W_{sMax}. (W_{ks}^{1} \text{ are exogenous variables, and } W_{ks}^{1} \forall t \in \{2, ..., T\} \text{ are derived variables})$ </td><td>Derived variables</td></tr><tr><td> $D_{kl}^{t}$ </td><td>=1 if there is a direct tie between worker k and l in period t (could be existing tie, or new tie created during period t), =0 otherwise.</td><td></td></tr><tr><td> $V_{kl}^{t}$ </td><td>=1 if there is an indirect tie between worker k and l (worker k and l share at least one common co-worker connected by direct tie) in period t; =0 otherwise.</td><td></td></tr><tr><td> $M_{kls}^{t}$ </td><td>=1 if worker k&#x27;s knowledge in skill s is better than worker l&#x27;s at the beginning of period t; =0 otherwise.</td><td></td></tr><tr><td> $G_{kls}^{t}$ </td><td>The amount of knowledge that can be transferred from worker k to worker l in skill s during period t.</td><td></td></tr><tr><td> $H_{kl\_i}^{t}$ </td><td>The time incurred by worker k in providing knowledge to worker l in period t using a tie of type i.</td><td></td></tr><tr><td> $Z_{k}^{t}$ </td><td>=1 if worker k is busy with transferring knowledge to other workers in period t (as a result of assignments in previous periods), =0 otherwise.</td><td></td></tr><tr><td> $F_{kl}^{t,m}$ </td><td>=1 if till the beginning of period t, worker k has finished transferring knowledge to worker l as a result of assignments made in period m, =0 otherwise.</td><td></td></tr><tr><td> $J_{kl}^{t,m}$ </td><td>=1 if during period t-1, worker k finishes transferring knowledge to worker l (as a result of assignments made in period m) and becomes available to provide knowledge to other workers in period t, =0 otherwise.</td><td></td></tr></table>

Table 2  
Major model assumptions and their justi<sup>fi</sup>cations.

<table><tr><td>Model assumptions</td><td>Theory and supporting research</td></tr><tr><td>The strength of a direct relationship increases with the length (time) of the relationship. Worker skill levels can be measured and classified into different levels.</td><td>The length of the relationship moderates the strength of the association by increasing trust and hence knowledge sharing [37]. Microsoft has adopted an expertise profiling system that categorizes workers&#x27; knowledge in a specific skill into multiple levels [3]. New York State Information Technology Workforce Skills Assessment Statewide Survey has categorized workers knowledge level in a particular skill into multiple levels [17]. Examples of expertise profiling systems include KIN and Tacit Systems EKG [13], and Iknow (http://www.iknow.us.com).</td></tr><tr><td>Providing and acquiring knowledge at the same time will reduce efficiency.</td><td>Teasley et al. [49], Dong et al. [18], and Heerwagen et al. [27] discuss efficiency loss associated with distractions, interruptions and time spent in communication with others.</td></tr><tr><td>The time to transfer knowledge is a function of the amount and complexity of knowledge being transferred between workers.</td><td>It has been recognized that it is easier to transfer small amounts of knowledge [5] as well as less complex knowledge [44].</td></tr><tr><td>Time is required to facilitate a direct relationship between a pair of workers.</td><td>In this context, Williams and Kessler [52], Hansen [26], and Goh et al. [22] discuss that each worker pair needs to incur a one-time effort to establish the mutual understanding needed to work effectively.</td></tr><tr><td>Knowledge transfer is sequential.</td><td>We assume that the knowledge provision is sequential since workers are heterogeneous in skills that they possess and the knowledge level in each skill. We believe concurrent knowledge transfer would be appropriate in training scenarios which is not the focus of this paper.</td></tr></table>

We assume an organization that supports S skills and has K workers. We assume a heterogeneous workforce where workers could have varying levels of knowledge in each skill. This skill set (set of knowledge levels in the S skills) for a worker is de<sup>fi</sup>ned as the knowledge vector of a worker. In our model, ${ W _ { k s } ^ { t } { \in } } [ W _ { s M i n } , ~ W _ { s M a x } ]$ , represents worker k's knowledge in skill s at the beginning of period t. Larger (smaller) values indicate an expert (novice) worker. Here, $W _ { s M i n } ( W _ { s M a x }$ )represents the minimum (maximum) knowledge level in skill s. In addition, as mentioned earlier, we assume that workers vary in terms of the importance (weight) they have for each skill, based on the types of tasks required of them. We use $\beta _ { k s } \biggl ( \in [ 0 , 1 ] , \sum _ { s = 1 } ^ { S } \beta _ { k s } = 1 \biggr )$ to capture the relative impor-<sup>¼</sup>tance of skill s for worker k. Therefore, the total knowledge of worker $k ,$ in period t, weighted by the importance of different skills is given by, $\sum _ { s = 1 } ^ { S } W _ { k s } ^ { t } \beta _ { k s } .$

The <sup>fi</sup>rm's objective is to maximize the cumulative weighted knowledge level of all workers, across all skills supported by the organization, over the planning horizon. This is given by, $M a x \sum _ { t = 1 } ^ { T } \sum _ { k = 1 } ^ { K } \sum _ { s = 1 } ^ { S } \beta _ { k s } W _ { k s } ^ { t }$

Next, we discuss additional details.

## 3.1.1. Time required to transfer knowledge

We assume that the total time taken by worker k to transfer knowledge to worker l depends on: (a) amount of knowledge being transferred, which depends upon the knowledge difference between workers k and l, (b) type of tie between workers k and l and, (c) work load of the worker providing help.

The maximum amount of knowledge that worker k can transfer to worker l at the beginning of period t is the difference in their knowledge at time t, in skill $s ,$ which is given by, $G _ { k l s } ^ { t } \in [ 0 , W _ { s M a x } ]$ . In our model, $\varpi _ { i s }$ represents the time taken by a worker to transfer a unit of knowledge, over a tie of type i, in skill s. We expect the time to transfer knowledge to be higher for complex skills. Therefore, the total time taken by worker k to transfer knowledge to worker l, in skill $s ,$ in period t, is given by, $\boldsymbol { G } _ { k l s } ^ { t } \boldsymbol { X } _ { k l s \_ i } ^ { t } \boldsymbol { \varpi } _ { i s } .$ Here $X _ { k l s \_ i } ^ { t }$ (decision variable) is equal to one if worker l is assigned to acquire knowledge from worker k, in period t, in skill s, over a tie of type i. It is important to note that knowledge transfer is directional, i.e., worker k transferring knowledge to worker l does not imply any knowledge <sup>fl</sup>ow from l to k $( X _ { k l s \_ i } ^ { t } \neq X _ { l k s \_ i } ^ { t } )$

In each period t, workers can share knowledge using existing direct or indirect ties, or create new direct ties. Since direct ties are more ef<sup>fi</sup>- cient than indirect ties, we assume $\varpi _ { 1 s } 2 \varpi _ { 0 s }$ , where 0 and 1 represent direct and indirect ties, respectively. $D _ { k l } ^ { t } \forall t { \in } \{ 1 , . . , T \}$ (derived variable) is equal to one if there is a direct tie between worker k and l during period t, and zero otherwise. Therefore, $( D _ { k l } ^ { t } - D _ { k l } ^ { ( t - 1 ) } = 1 )$ indicates the absence of pre-existing direct ties between workers l and $k ,$ in period t. In the absence of pre-existing direct ties between workers, organizations need to facilitate direct ties between workers, in order to effectively transfer knowledge. Since the creation of new direct ties requires time (effort), we introduce a set up coef<sup>fi</sup>cient (θ) to capture the time required to facilitate a direct relationship between a pair of workers. Note that, the relationships between worker k and l are bidirectional i.e. $, D _ { k l } ^ { t } = D _ { l k } ^ { t }$ . Similarly, $V _ { k l } ^ { t } \forall t \in \{ 1 , . . , T \}$ (derived variable) is equal to one if there is an indirect tie between worker k and l during period t, and zero otherwise. Note that workers do not incur a setup cost when using indirect ties since these are by-products of creating direct ties. Thus, the knowledge transfer time from worker k to worker l using direct ties, in period t, is given by, $H _ { k l _ { - } 0 } ^ { t } = \theta \Big ( D _ { k l } ^ { t } { - } D _ { k l } ^ { t - 1 } \Big ) + \sum _ { s = 1 } ^ { S } G _ { k l s } ^ { t } X _ { k l s _ { - } 0 } ^ { t } \varpi _ { 0 s } .$ Along the same lines, the knowledge transfer time using indirect relationships is given by, $H _ { k l \_ 1 } ^ { t } = \sum _ { s = 1 } ^ { S } G _ { k l s } ^ { t } X _ { k l s \_ 1 } ^ { t } \varpi _ { 1 s } ,$ . For details please refer to constraints (A.1)–(A.3) of the formulation.

It is important to note that multiple workers may be assigned to the same worker for knowledge acquisition, at the same time. However, a worker can acquire knowledge from at most one worker in any period. We assume that acquisition requests are queued and the knowledge transfer process is sequential, based on the order in which the requests are made. Hence, workers might incur a waiting time in the queue before knowledge acquisition starts. In addition, the time to transfer knowledge should also depend on the work-status of the worker providing help. However, we assume that all workers are equally busy and hence do not differentiate between workers based on their work-status.

Therefore, the total time to transfer knowledge is the sum of knowledge transfer time and waiting time.<sup>1</sup>

## 3.1.2. Knowledge diffusion using direct and indirect ties

We model the extent of knowledge gained by worker k, as a result of consulting co-worker l, as depending on: (a) knowledge difference between worker k and worker l at the beginning of the knowledge transfer process (G<sup>t</sup> ), (b) the knowledge provision load of worker l (number of other workers assigned to acquire knowledge from worker l), and (c) the strength of the direct relationship between worker k and worker l.

It is important to note that workers are allowed to provide and acquire knowledge in the same period. However, when a worker is providing and acquiring knowledge at the same time, it affects his knowledge acquisition ef<sup>fi</sup>ciency. We model this overhead as reduced knowledge acquisition ef<sup>fi</sup>ciency in periods where the worker is simultaneously providing and acquiring knowledge i.e., $\alpha _ { l \_ i \_ b u s y } { < } \alpha _ { l \_ i \_ i d l e }$ , where i is equal to zero (one) for direct(indirect) ties. Note that, it can take multiple periods for worker l to acquire knowledge. Therefore, the average knowledge acquisition ef<sup>fi</sup>ciency for worker l between periods m and $q ,$ over a tie of type i, is given by, $( \sum _ { r = m } ^ { q - 1 } \big ( \alpha _ { l \_ 0 \_ b u s y } Z _ { l } ^ { r } + \alpha _ { l \_ 0 \_ i d l e } \big ( 1 - Z _ { l } ^ { r } \big ) \big ) / ( q - m ) )$ . As mentioned in Section 2.1, not all direct ties are the same and their strength can vary based on age of the relationship between two workers. In our model, $\sum _ { u = 1 } ^ { m } D _ { k l } ^ { u }$ indicates the age of the direct relationship between workers k and l, in period m. Thus, $\sum _ { u = 1 } ^ { m } D _ { k l } ^ { u } / T$ represents ef<sup>fi</sup>ciency of knowledge transfer between workers k and l, in period m. Therefore, the net ef<sup>fi</sup>ciency to transfer knowledge using direct ties is given by, $\sum _ { u = 1 } ^ { m } D _ { k l } ^ { u } / T \sum _ { r = m } ^ { q - 1 } \big ( \alpha _ { l _ { - } 0 _ { - } b u s y } Z _ { l } ^ { r } + \alpha _ { l _ { - } 0 _ { - } i d l e } \big ( 1 - Z _ { l } ^ { r } \big ) \big ) / ( q - m )$ . And, the ef<sup>fi</sup>ciency of indirect ties is given by, $\sum _ { r = m } ^ { q - 1 } \big ( \alpha _ { l _ { - } 1 \_ b u s y } Z _ { l } ^ { r } + \alpha _ { l _ { - } 1 \_ i d l e } \big ( 1 - Z _ { l } ^ { r } \big ) \big ) / ( q - m ) .$

<sup>¼</sup>The amount of knowledge acquired, in any period t, is modeled as the product of the knowledge difference between the two workers sharing knowledge $\left( G _ { k l s } ^ { t } \right)$ and the ef<sup>fi</sup>ciency of knowledge transfer. W<sup>1</sup>represents worker $l ^ { \prime } s$ initial knowledge level (at the beginning of the planning horizon). Therefore, in period t, worker l's updated knowledge, in skill s, as a result of knowledge acquisition from coworkers, using direct and indirect ties, is given by,

$$
\begin{array}{l}W _ {l s} ^ {t} = W _ {l s} ^ {1} + \sum_ {q = 1} ^ {t - 1} \sum_ {m = 1} ^ {q - 1} \sum_ {k = 1; k \neq l} ^ {K} J _ {k l} ^ {q, m} X _ {k l s, 0} ^ {m} G _ {k l s} ^ {m} \left(\left(\sum_ {u = 1} ^ {m - 1} D _ {k l} ^ {u} / T\right) r = m \sum_ {\alpha_ {l, 0 \_ b u s y}} Z _ {l} ^ {r} + \alpha_ {l, 0 \_ i d l e} (1 - Z _ {l} ^ {r})\right) / (q - m)\left. \right)\\+ \sum_ {q = 1} ^ {t - 1} \sum_ {m = 1} ^ {q - 1} \sum_ {k = 1; k \neq l} ^ {K} J _ {k l} ^ {q, m} X _ {k l s, 1} ^ {m} G _ {k l s} ^ {m} \sum_ {r = m} ^ {q - 1} \left(\alpha_ {l, 1 \_ b u s y} Z _ {l} ^ {r} + \alpha_ {l, 1 \_ i d l e} (1 - Z _ {l} ^ {r})\right)\\\quad / (q - m) \forall l \in \{1,, K \}, \forall s \in \{1,, S \}, \forall t \in \{2,, T \}\end{array}
$$

Finally, the KFN optimization problem can be formulated as, Objective function:

$$
M a x \sum_ {t = 1} ^ {T} \sum_ {k = 1} ^ {K} \sum_ {s = 1} ^ {S} \beta_ {k s} W _ {k s} ^ {t}
$$

Knowledge Sharing Relationship Constraints:

$$
\begin{array}{l l} D _ {k l} ^ {t} \leq D _ {k l} ^ {(t - 1)} + \sum_ {s = 1} ^ {S} \Big (X _ {k l s \_ 0} ^ {t} + X _ {l l s \_ 0} ^ {t} \Big) & \forall k, l \in \{1, 2,.., K \}, k \neq l, \forall t \in \{2,.., T \} \\ D _ {k l} ^ {t} \geq 0. 5 D _ {k l} ^ {(t - 1)} + \sum_ {s = 1} ^ {S} \Big (X _ {k l s \_ 0} ^ {t} + X _ {l l s \_ 0} ^ {t} \Big) / (2 S) & \forall k, l \in \{1, 2,.., K \}, k \neq l, \forall t \in \{2,.., T \} \\ D _ {k l} ^ {t} = D _ {l k} ^ {t} & \forall k, l \in \{1, 2,.., K \}, k \neq l, \forall t \in \{2,.., T \} \end{array}\tag{A.1}
$$

$D _ { k l } ^ { t } = 1$ if there is a direct tie between worker k and l in period t (could be tie facilitated in previous periods, or a new tie is created during period $t ) , = 0$ otherwise.

$$
\begin{array}{l l} V _ {k l} ^ {t} \leq \sum_ {\substack {u = 1 \\ u \neq k, l}} ^ {K} D _ {k u} ^ {t} D _ {l u} ^ {t} & \forall k, l \in \{1, 2,.., K \}, k \neq l, \forall t \in \{1,.., T \} \\ V _ {k l} ^ {t} \geq \left(\sum_ {\substack {u = 1 \\ u \neq k, l}} ^ {K} D _ {k u} ^ {t} D _ {l u} ^ {t}\right) / (K - 2) & \forall k, l \in \{1, 2,.., K \}, k \neq l, \forall t \in \{1,.., T \} \end{array}\tag{A.2}
$$

$V _ { k l } ^ { t } = 1$ if there is an indirect tie between worker k and l in period $t ; = 0$ otherwise.

$$
\begin{array}{l} X _ {k l s \_ 1} ^ {t} \leq V _ {k l} ^ {(t - 1)}   \forall k, l \in \{1, 2,.., K \}, k \neq l, \forall s \in \{1, 2,.., S \}, \forall t \in \{2,.., T \} \\ X _ {k l s \_ 1} ^ {t} \leq 1 - D _ {k l} ^ {t}   \forall k, l \in \{1, 2,.., K \}, k \neq l, \forall s \in \{1, 2,.., S \}, \forall t \in \{2,.., T \} \end{array}\tag{A.3}
$$

Worker l can acquire knowledge from k, in skill s, in period t, using an indirect tie only if, there is an existing indirect tie in period $t - 1$ and there is no direct tie between k and l.

Knowledge sharing assignment constraints:

$$
\sum_ {i = 0} ^ {1} \sum_ {k = 1; k \neq l} ^ {K} \sum_ {s = 1} ^ {S} X _ {k l s \_ i} ^ {t} + \sum_ {m = 1} ^ {t - 1} \sum_ {k = 1} ^ {K} F _ {k l} ^ {t \_ m} \leq 1 \quad \forall l \in \{1, 2,.., K \}, \forall t \in \{1, 2,.., T \}\tag{B.1}
$$

Worker l can acquire knowledge from at most one worker in period t

$$
\sum_ {i = 0} ^ {1} \sum_ {l = 1; k \neq l} ^ {K} \sum_ {s = 1} ^ {S} X _ {k l s \_ i} ^ {t} \leq 1 \quad \forall k \in \{1, 2,.., K \}, \forall t \in \{1, 2,.., T \}\tag{B.2}
$$

Worker k can provide knowledge to at most one worker in period t.

$$
T - \sum_ {t = 1} ^ {T} \sum_ {l = 1; l \neq k} ^ {K} \sum_ {i = 0} ^ {1} H _ {k l - i} ^ {t} - \sum_ {t = 1} ^ {T} \left(1 - Z _ {k} ^ {t}\right) \geq 0 \quad \forall k \in \{1,.., K \}\tag{B.3}
$$

Total time spent by worker k in knowledge provision and staying idle cannot exceed the planning horizon T.

Other knowledge sharing constraints:

$$
\begin{array}{l l} M _ {k l s} ^ {t} \geq \left(W _ {k s} ^ {t} - W _ {l s} ^ {t}\right) / W _ {s R a n g e} & \forall k, l \in \{1, 2,.., K \}, k \neq l, \forall s \in \{1, 2,.., S \}, \forall t \in \{1, 2,.., T \} \\ M _ {k l s} ^ {t} <   \left(W _ {k s} ^ {t} - W _ {l s} ^ {t}\right) / W _ {s R a n g e} + 1 & \forall k, l \in \{1, 2,.., K \}, k \neq l, \forall s \in \{1, 2,.., S \}, \forall t \in \{1, 2,.., T \} \end{array}\tag{C.1}
$$

$M _ { k l s } ^ { t } = 1$ if worker k is better than worker l, in skill s, at the beginning of period $t ; = 0$ otherwise.

$$
G _ {k l s} ^ {t} = M _ {k l s} ^ {t} \left(W _ {k s} ^ {t} - W _ {l s} ^ {t}\right) \quad \forall k, l \in \{1, 2,.., K \}, k \neq l, \forall s \in \{1, 2,.., S \}, \forall t \in \{1, 2,.., T \}\tag{C.2}
$$

$G _ { k l s } ^ { t }$ is the amount of knowledge that can be transferred from worker k to worker l, in skill s, during period t.

$$
\begin{array}{l} H _ {k l \_ 0} ^ {t} = \theta \left(D _ {k l} ^ {t} - D _ {k l} ^ {t - 1}\right) + \sum_ {s = 1} ^ {S} G _ {k l s} ^ {t} X _ {k l s \_ 0} ^ {t} \varpi_ {0 s} \\ H _ {k l \_ 1} ^ {t} = \sum_ {s = 1} ^ {S} G _ {k l s} ^ {t} X _ {k l s \_ 1} ^ {t} \varpi_ {1 s} \quad \forall k, l \in \{1, 2,.., K \}, k \neq l, \forall t \in \{1,.., T \} \end{array}\tag{C.3}
$$

$H _ { k l _ { - } } ^ { t }$ is the time incurred by worker k in providing knowledge to worker l, in period t, using a tie of type i.

$$
\begin{array}{l} Z _ {k} ^ {t} \left(t - \sum_ {m = 1} ^ {t - 1} \sum_ {l = 1; l \neq k} ^ {K} \sum_ {i = 0} ^ {1} H _ {k l, i} ^ {m} - \sum_ {m = 1} ^ {t - 1} (1 - Z _ {k} ^ {m})\right) \geq 0 \quad \forall k \in \{1, 2,.., K \}, \forall t \in \{1,.., T \} \\ Z _ {k} ^ {t} \geq \left(t - \sum_ {m = 1} ^ {t - 1} \sum_ {l = 1; l \neq k} ^ {K} \sum_ {i = 0} ^ {1} H _ {k l, i} ^ {m} - \sum_ {m = 1} ^ {t - 1} (1 - Z _ {k} ^ {m})\right) / T \quad \forall k \in \{1, 2,.., K \}, \forall t \in \{1,.., T \} \end{array}\tag{C.4}
$$

$Z _ { k } ^ { t } = 1$ if worker k is busy with transferring knowledge to other workers (as a result of assignments in previous periods) in period $t , = 0$ otherwise.

$$
\begin{array}{l} F _ {k l} ^ {t \_ m} \left(t - \sum_ {q = 1} ^ {m - 1} \sum_ {r = 1, r \neq k} ^ {K} \sum_ {i = 0} ^ {1} H _ {k r \_ i} ^ {q} - \sum_ {i = 0} ^ {1} H _ {k l \_ i} ^ {m} - \sum_ {q = 1} ^ {m - 1} (1 - Z _ {k} ^ {q})\right) \geq 0 \\ F _ {k l} ^ {t \_ m} \geq \left(t - \sum_ {q = 1} ^ {m - 1} \sum_ {r = 1, r \neq k} ^ {K} \sum_ {i = 0} ^ {1} H _ {k r \_ i} ^ {q} - \sum_ {i = 0} ^ {1} H _ {k l \_ i} ^ {m} - \sum_ {q = - 1} ^ {m - 1} (1 - Z _ {k} ^ {q})\right) / T \\ \forall k, l \in \{1, 2,.., K \}, k \neq l, \forall t, m \in \{1,.., T \}, m <   t \end{array}\tag{C.5}
$$

$F _ { k l } ^ { t } { } ^ { m } = 1$ if till the beginning of period t, worker k has <sup>fi</sup>nished transferring knowledge to worker l as a result of assignments made in period $m , = 0$ otherwise.

$$
J _ {k l} ^ {t \_ m} = F _ {k l} ^ {t \_ m} - F _ {k l} ^ {(t - 1) \_ m} \quad \forall t \in \{2,.., T \}, \forall m \in \{1,.., T \}, m <   t\tag{C.6}
$$

$J _ { k l } ^ { t _ { - } m } = 1$ if during period t-1, worker k <sup>fi</sup>nishes transferring knowledge to worker l (as a result of assignments made in period m) and becomes available to provide knowledge to other workers in period $t , = 0$ otherwise.

$$
\begin{array}{l} W _ {l s} ^ {t} = W _ {l s} ^ {1} + \sum_ {q = 1} ^ {t - 1} \sum_ {m = 1 k} ^ {q - 1} \sum_ {k = 1, k \neq l} ^ {K} \left(\sum_ {u = 1} ^ {m - 1} D _ {k l} ^ {u} / T\right) J _ {k l} ^ {q - m} X _ {k l s \_ 0} ^ {m} G _ {k l s} ^ {m} \sum_ {r = m} ^ {q - 1} \Big (\alpha_ {l \_ 0 \_ b u s y} Z _ {l} ^ {r} + \alpha_ {l \_ 0 \_ i d l e} \big (1 - Z _ {l} ^ {r} \big) \Big) / (q - m) \\ + \sum_ {q = 1} ^ {t - 1} \sum_ {m = 1} ^ {q - 1} \sum_ {k = 1, k \neq l} ^ {K} J _ {k l} ^ {q - m} X _ {k l s \_ 1} ^ {m} G _ {k l s} ^ {m} \sum_ {r = m} ^ {q - 1} \Big (\alpha_ {l \_ 1 \_ b u s y} Z _ {l} ^ {r} + \alpha_ {l \_ 1 \_ i d l e} \big (1 - Z _ {l} ^ {r} \big) \Big) / (q - m) \\ \forall l \in \{1, 2,.., K \},   \forall s \in \{1, 2,.., S \},   \forall t \in \{2,.., T \} \end{array}\tag{C.7}
$$

$\boldsymbol { W _ { l s } ^ { t } }$ is worker l's knowledge, in skill s, at the beginning of period t. ■

## 4. Solution procedure: connection based heuristic (CBH)

The complexity of the KFN optimization problem prohibits problems to be solved in a reasonable amount of time. Hence, we propose a heuristic that uses connection based assignments at discrete points in time in order to solve the problem.

The KFN optimization problem can be solved for each period successively. In other words, we <sup>fi</sup>rst determine the knowledge sharing assignments and the optimal knowledge gain in the <sup>fi</sup>rst period. Next, we set up the problem for the second period. To achieve this, we use knowledge transfer information from the <sup>fi</sup>rst period and determine each worker's knowledge provision load and availability to acquire knowledge at the beginning of the second period. In addition, we update their knowledge level based on knowledge transfer assignments in the <sup>fi</sup>rst period. The desired worker-to-worker knowledge transfer assignments for the second period can be obtained by using the above information. Similarly, the knowledge transfer assignments for the second period then sets up the problem for the third period, and so on. In order ensure that CBH is not greedy in determining the knowledge sharing transactions in each period, we consider the impact of knowledge sharing decisions made in the current period on future periods.

First, we consider the potential bene<sup>fi</sup>ts to other workers connected to the worker acquiring knowledge. Particularly, we consider the extent of knowledge that can, overtime, diffuse to other workers connected to the worker acquiring knowledge. Second, we consider the opportunity cost for the worker providing knowledge. That is, we consider the fact that once a worker is assigned to provide knowledge he becomes temporarily unavailable to other workers. Fig. 2 illustrates the <sup>fl</sup>ow of the CBH. For the details of the CBH refer to Appendix A of the online supplement.

## 5. Experiment design

The complexity of the problem precludes analytical solution and requires us to use simulation. Other studies in IS have used simulation with synthetic data to provide insights into relationships between key variables. This approach is appropriate in cases where the underlying phenomenon is complex and real‐world data is dif<sup>fi</sup>cult to obtain. Examples of such studies include knowledge management [10], electronic markets [30], the performance of IS teams [46], benchmarking of service systems [18], and security portfolios [34]. The value of our model is to provide generalized insights and facilitate managerial benchmarking of KFN.

The simulation experiment starts by creating an organization with an initial con<sup>fi</sup>guration of workers. This initial con<sup>fi</sup>guration is described in Section 5.1. Section 5.2 describes the design of simulation experiments including, key parameters and their estimation. Fifty replications of each sample path were used, and average values of system performance measures were calculated. Simulations were extremely computationintensive. Experiments were run on a cluster of 160 Intel Xeon CPUs on Dell blade servers with Red Hat Enterprise Linux operating system. The average time for running each replication of a sample path was 1 h.

![](/api/attachments/QGVU72FR/fulltext/images/07f0dde030047107643e243206e83d3b1a65e93c626fe33bb7996ebaa8875d76.jpg)  
Fig. 2. Connection based heuristic (CBH).

## 5.1. Initial configuration

At the beginning of the planning horizon, we consider a population of 100 workers. A network with an average of two ties per worker was created using the Watts and Strogatz algorithm [51]. Each worker has multiple skills. Workers' knowledge level in each skill at the beginning of the planning horizon $( W _ { k s } ^ { 1 } )$ is initialized by selecting from a normal distribution. Workers are categorized into three groups – expert, average, and novice – based on their average initial knowledge level across skills. Based on prior research, workers with an average knowledge level $( \sum _ { s = 1 } ^ { S } W _ { k s } ^ { 1 } / S )$ between 0 and 2 are de<sup>fi</sup>ned as Novices, between <sup>¼</sup>2 and 3 as average workers, and between 3 and 5 as experts [35]. Each worker is set to be specialized in a random skill ^s, such that $\beta _ { k \hat { s } } = 3 \beta _ { k s } \forall s \in \{ 1 , . . , S \} , s \neq \hat { s }$ . At the beginning of the planning horizon, <sup>¼ f g</sup>each worker shares knowledge with a randomly selected worker. This represents the organization's initial condition.

## 5.2. Simulation parameters

Table 3 describes the numerical values and justi<sup>fi</sup>cations for parameters used in our simulation experiments. We have tried to base the parameter values on ranges that are encountered in practice and/or prior research. These parameters can be divided into three categories: organizational, worker, and knowledge sharing parameters. In our opinion, organizational, and worker parameters can be estimated relatively easily. Knowledge sharing parameters included in our model can be estimated approximately or varied in experiments and help sensitize the organization to KFN optimization issues that involve these parameters.

## 5.2.1. Organizational parameters

A knowledge sharing environment was simulated for a planning horizon of 100 time periods. Note that the actual value of each time period is context sensitive. We assume 100 workers (K) and up to 5 skills (S) for our simulations.

## 5.2.2. Worker parameters

We use two worker-related parameters: relative importance of worker k's knowledge in skill $: ( \beta _ { k s } )$ , and worker k's initial knowledge in skill $s ~ ( W _ { k s } ^ { 1 } )$ . The relative importance of worker k's knowledge in skill $: ( \beta _ { k s } \in ( 0 , 1 ) , \sum _ { s = 1 } ^ { S } \beta _ { k s } = 1 )$ were chosen to be comparable to the <sup>¼</sup>range of values encountered in practice. We chose a range of 0–5 for worker knowledge for each skill. In addition, consistent with prior research on worker cross-training, a normal distribution of worker knowledge was used. Empirical research on the operation of IT environments has illustrated the presence of considerable workforce heterogeneity [32]. A mean of 2.5 was chosen to allow for a normal distribution of worker knowledge in the range 0–5. Relative importance of different skills for each worker $( \beta _ { k s } )$ can be based on the department that the worker belongs to or her expected workload based on the job description. As mentioned in Section 2.1, knowledge level of workers $( W _ { k s } ^ { t } )$ can be captured and documented effectively using tools.

## 5.2.3. Knowledge sharing parameters

The ef<sup>fi</sup>ciency of acquiring knowledge $( \alpha _ { k \_ i } )$ , the time coef<sup>fi</sup>cient of providing knowledge $\left( \varpi _ { i s } \right)$ , and the time coef<sup>fi</sup>cient of creating direct ties (θ), are parameters designed to capture the characteristics of the

## Table 3

Experiment parameter values.

<table><tr><td>Type</td><td>Parameter</td><td>Values</td><td>Justification</td></tr><tr><td rowspan="2">System</td><td>100</td><td>environment</td><td>K</td></tr><tr><td>S</td><td>2/3/4/5</td><td>Cowan and Jonard [12] use a 5-category knowledge vector for each agent. Prabhakar et al. [45] use 5 skills (Programming Skills, Operating System Skills, Database, ERP, and e-Commerce Server Skills). Dong et al. [18] use 4 skills for each knowledge worker.</td></tr><tr><td>T</td><td>100</td><td>Assuming that each time period is a day.</td><td></td></tr><tr><td rowspan="2">Worker related</td><td> $\beta_{ks}$ </td><td>Each worker is randomly specialized in one skill</td><td>Our parameter values are consistent with Geel et al. [21].</td></tr><tr><td> $W_{ks}^{1}$ </td><td>Follows Normal Distribution: N(2.5, 0.8) /N(2.5, 1.0) / N(2.5, 1.2)</td><td>Lester [35] proposed five categories to assess an employee&#x27;s skill level. In addition, a normal distribution of worker knowledge is consistent with prior research [48]. This assumption also has some empirical support. Dawes et al. [17] and Bulgiba et al. [8] have reported that IT skills follow a normal distribution.</td></tr><tr><td rowspan="4">Knowledge transfer</td><td> $\alpha_{k\_i\_busy}$ </td><td> $\alpha_{k\_0\_idle}$ : 0.8/0.6/0.4</td><td rowspan="2">Cowan and Jonard [12] uses values in the range 0.5–1 for direct ties and recognize that high values close to 1 are unrealistic. Baum and Berta [6], Hansen [25], and Levine and Kurzban [38] discuss the fact that values depend on the type of tie.</td></tr><tr><td> $\alpha_{k\_i\_idle}$ </td><td> $\alpha_{k\_0\_busy}$ : 0.6/0.45/0.3 $\alpha_{k\_1\_idle}$ : 0.4/0.3/0.2 $\alpha_{k\_1\_busy}$ : 0.2/0.15/0.1</td></tr><tr><td> $\varpi_{is}$ </td><td> $\varpi_{0s}$ :6/10/14/18, $\varpi_{1s}$ :10/15/20/25 $\forall s\in\{1,...,S\}$ </td><td>We experiment with different values of  $\varpi_{0s}$  and  $\varpi_{1s}$  such that  $\varpi_{0s}<\varpi_{1s}$ . Prior research [25,39,41] suggests that knowledge transfer using direct ties takes less time as compared to using indirect ties.</td></tr><tr><td>θ</td><td>5/10/15/20</td><td>We experiment with a range of values in order to study the sensitivity of our results.</td></tr></table>

knowledge sharing environment. The ef<sup>fi</sup>ciency of acquiring knowledge has been extensively researched [9]. This parameter is a function of the type of tie between workers [6,25,38]. Cowan and Jonard [12] uses values in the range 0.5–1 for direct ties and recognize that high values close to 1 are unrealistic. The values chosen by us are in this range.

The time coef<sup>fi</sup>cient of providing knowledge (ϖ ) captures an individual's cost of providing help that depends on the type of tie [41] and the complexity of the skill being shared. Since direct ties are more ef<sup>fi</sup>cient in terms of communication [25,39], we assume that time coef<sup>fi</sup>cient of providing knowledge is the smaller for direct ties than for indirect ties. Exact parameter estimation may be dif<sup>fi</sup>cult. However, the intent is not to be able to estimate these parameters accurately, but to force organizations to consider whether these parameters are low or high and explore ways to enhance their value. Such an approach is consistent with prior simulation-based knowledge management research [10].

The time coef<sup>fi</sup>cient of creating direct ties forces organizations to think about organizational culture and <sup>fl</sup>exibility in terms of creating and using KFNs to share knowledge [9,25]. We experiment with a range of values for this parameter.

## 6. Results and discussion

We present selected results from our experiments to illustrate the properties of effective KFNs and how these properties are impacted by system environment parameters, worker related parameters, and knowledge sharing parameters.<sup>2</sup> The following sets of results are presented in this section: (a) the structure of effective KFNs, (b) knowledge diffusion and knowledge sharing using KFNs.

## 6.1. The structure of effective knowledge flow networks (KFNs)

As discussed in Section 5.2, we consider three different groups of workers (experts, average and novice workers) in the organization. We seek to understand the similarities and differences between these groups of workers in terms of the KFNs they belong to, using social network structural measures.

## 6.1.1. Impact of knowledge acquisition efficiency and workforce heterogeneity on KFN structure

We expect novice workers to create ties with expert and average workers to acquire knowledge. However, the relative importance and roles of different types of workers is not always clear. Our results indicate average workers have a crucial intermediary role to play in facilitating knowledge <sup>fl</sup>ow. In other words, average workers allow novice workers to get indirect access to experts in the system. Table 4 indicates that the highest number of direct and indirect ties (highest degree centrality between groups) occurs between experts and average workers, followed by the ties between average workers and novices, and then between experts and novices, irrespective of number of skills and workforce heterogeneity. In addition, Fig. 3-a shows that the average number of times a direct tie is used is highest between the expert-average worker pair, followed by the average-novice worker, and expert-novice worker pairs. However, the amount of knowledge transferred (and hence knowledge transfer time) per tie is the least, between expert-average worker pair, followed by the average-novice worker and expert-novice worker pairs, in that order (Fig. 3-b). This result suggests that effective knowledge transfer tends to take place in short bursts (frequent knowledge transfers of short duration) between workers who do not have very high knowledge differences. Such knowledge transfers ensure that worker knowledge levels are updated more frequently. This allows the worker providing knowledge and the worker gaining knowledge, to become available relatively quickly for additional knowledge provision and/or knowledge acquisition. In addition, such a knowledge transfer pattern makes workers connected by new direct ties to become available to other workers via indirect ties, relatively quickly.

Note that, on average, the between-group knowledge heterogeneity is higher than the within group knowledge heterogeneity. Since knowledge transfers occur in short, on average there are more direct ties within groups than between groups (Fig. 3-c). Table 4 also suggests that expert worker groups are more cohesive than average worker groups, followed by novice worker groups, irrespective of workforce heterogeneity. High group cohesiveness is attributed to reciprocity of knowledge sharing relationships within the group. In a multi-skill environment, an expert worker (who has a high average knowledge level) often has a high variance in knowledge across skills. Hence, a worker who has a high knowledge level in one skill needs to consult another expert (within the group) to improve knowledge level in another low valued skill. Therefore, within expert worker groups, it is likely that reciprocal knowledge exchange (in different skills) takes place. In comparison, such reciprocal knowledge <sup>fl</sup>ow is unlikely within novice worker groups. In addition, high cohesiveness between experts allows average workers to have access to a larger number of indirect ties with experts, using the same number of direct ties. Similarly, high cohesiveness between average workers allows novice workers to get indirect access to a larger number of average workers.

We also observe that the number of direct ties created over the plan ning horizon increases as workforce heterogeneity increases (Fig. 3-d). This can be attributed to larger knowledge transfer times associated with increased workforce heterogeneity. Larger knowledge transfer times reduce the availability of knowledgeable workers, over the planning horizon (since worker expertise is updated less frequently). Hence, new ties have to be created in order to facilitate knowledge diffusion. In Fig. 3-d, we also observe that the number of direct ties created decreases as the knowledge acquisition ef<sup>fi</sup>ciency increases. High acquisition ef<sup>fi</sup>- ciency increases the amount of knowledge acquired in each knowledge transfer, which in turn results in better knowledge diffusion. This, in turn, increases the pool of competent workers who can provide help over the planning horizon, reducing the need to create direct ties to facilitate knowledge diffusion.

## 6.1.2. Impact of cost coefficients on KFN structure

We also study the impact of various cost coef<sup>fi</sup>cients on the number of direct ties created during the planning horizon. Three types of cost coef<sup>fi</sup>cients are examined: cost (time) to create direct ties, cost (time) to transfer knowledge using direct ties, and cost (time) to transfer knowledge using indirect ties. Recall from Section 3.1 that although direct ties are more ef<sup>fi</sup>cient than indirect ties for knowledge transfer, it takes several time periods to create direct ties. Therefore, it is bene<sup>fi</sup>cial to create new direct ties only if the knowledge gain can offset the cost of creating new ties, and existing indirect or direct ties are unavailable or incompetent. Moreover, it may be desirable to create direct ties if there is opportunity to reuse them later in the planning horizon. This explains why, in Fig. 3-e, the number of direct ties created decreases as the time to create direct ties increases. Consistent with Fig. 3-d, we also see that the number of direct ties created increases with increase in workforce heterogeneity. However, this increase reduces as the time to create direct ties increases.

In Fig. 3-f we study the impact of knowledge transfer time (cost coef-<sup>fi</sup>cient) on the total number of direct ties created. Interestingly, we <sup>fi</sup>nd that as knowledge transfer time increases, the number of direct ties created increases, regardless of workforce heterogeneity. An increase in the knowledge transfer time increases the time that workers are engaged in individual knowledge sharing transactions. This reduces access to competent workers connected by existing direct ties, for additional knowledge sharing transactions. As a result, additional (new) direct ties need to be created to facilitate knowledge exchange.

Table 4  
Group cohesiveness and normalized degree centrality between groups.<sup>1</sup>

<table><tr><td rowspan="3">Problem class</td><td rowspan="3">Workforce hetero-geneity</td><td rowspan="3"># of skills</td><td colspan="6">Normalized degree centrality between groups</td><td colspan="3">Group cohesiveness</td></tr><tr><td colspan="2">Expert-average</td><td colspan="2">Expert-novice</td><td colspan="2">Average-novice</td><td rowspan="2">Expert</td><td rowspan="2">Average</td><td rowspan="2">Novice</td></tr><tr><td>D</td><td>I</td><td>D</td><td>I</td><td>D</td><td>I</td></tr><tr><td>1</td><td>Low</td><td>2</td><td>0.43</td><td>0.84</td><td>0.21</td><td>0.43</td><td>0.31</td><td>0.50</td><td>0.047</td><td>0.026</td><td>0.021</td></tr><tr><td>2</td><td>Med</td><td>2</td><td>0.47</td><td>0.95</td><td>0.27</td><td>0.56</td><td>0.37</td><td>0.63</td><td>0.043</td><td>0.027</td><td>0.023</td></tr><tr><td>3</td><td>High</td><td>2</td><td>0.50</td><td>1.01</td><td>0.31</td><td>0.69</td><td>0.40</td><td>0.69</td><td>0.040</td><td>0.028</td><td>0.023</td></tr><tr><td>4</td><td>Low</td><td>3</td><td>0.34</td><td>0.60</td><td>0.14</td><td>0.27</td><td>0.26</td><td>0.39</td><td>0.045</td><td>0.024</td><td>0.023</td></tr><tr><td>5</td><td>Med</td><td>3</td><td>0.41</td><td>0.76</td><td>0.20</td><td>0.41</td><td>0.33</td><td>0.53</td><td>0.043</td><td>0.025</td><td>0.022</td></tr><tr><td>6</td><td>High</td><td>3</td><td>0.46</td><td>0.87</td><td>0.24</td><td>0.50</td><td>0.37</td><td>0.63</td><td>0.041</td><td>0.026</td><td>0.025</td></tr><tr><td>7</td><td>Low</td><td>4</td><td>0.27</td><td>0.44</td><td>0.09</td><td>0.20</td><td>0.20</td><td>0.29</td><td>0.046</td><td>0.023</td><td>0.022</td></tr><tr><td>8</td><td>Med</td><td>4</td><td>0.34</td><td>0.59</td><td>0.17</td><td>0.32</td><td>0.29</td><td>0.43</td><td>0.042</td><td>0.024</td><td>0.021</td></tr><tr><td>9</td><td>High</td><td>4</td><td>0.41</td><td>0.72</td><td>0.22</td><td>0.41</td><td>0.34</td><td>0.55</td><td>0.038</td><td>0.024</td><td>0.022</td></tr><tr><td>10</td><td>Low</td><td>5</td><td>0.20</td><td>0.32</td><td>0.08</td><td>0.13</td><td>0.15</td><td>0.22</td><td>0.040</td><td>0.023</td><td>0.021</td></tr><tr><td>11</td><td>Med</td><td>5</td><td>0.31</td><td>0.50</td><td>0.13</td><td>0.24</td><td>0.24</td><td>0.35</td><td>0.034</td><td>0.024</td><td>0.023</td></tr><tr><td>12</td><td>High</td><td>5</td><td>0.37</td><td>0.63</td><td>0.18</td><td>0.31</td><td>0.29</td><td>0.45</td><td>0.036</td><td>0.024</td><td>0.023</td></tr></table>

<sup>1</sup> Differences between groups are statistical signi<sup>fi</sup>cant using multiple paired t-tests, pb 0.05.

6.1.3. Impact of number of skills supported by the organization on KFN structure

Here we study how the number of skills supported by the organization impacts the KFN structure. As number of skills increase, workers need to improve knowledge in multiple skills based on their knowledge and relative importance (weight) for each skill. Interestingly, we <sup>fi</sup>nd that the total number of direct ties created decreases with increase in number of skills (Fig. 3-g). This is because, the likelihood of using an existing tie for knowledge exchange increases with increase in number of skills. In other words, same tie may be utilized for knowledge provision and acquisition of multiple skills, decreasing the need to create new ties. This also explains why, in Table 4, group cohesiveness decreases as the number of skills increases.

## 6.2. Knowledge diffusion and knowledge sharing using KFNs

This section facilitates a deeper understanding of the dynamics of knowledge sharing and diffusion.

## 6.2.1. Impact of knowledge acquisition efficiency and workforce heterogeneity on knowledge diffusion and sharing

In Fig. 4-a, as expected, we <sup>fi</sup>nd that high knowledge acquisition ef<sup>fi</sup>ciency results in better knowledge diffusion (as measured by total cumulative weighted knowledge gain over the planning horizon). Interestingly, we also <sup>fi</sup>nd that knowledge diffusion over the planning horizon decreases as workforce heterogeneity increases. Note that, the knowledge of a worker who acquires knowledge is updated after each knowledge acquisition transaction, which may last for multiple time periods. Recall that the overall knowledge transfer time increases with workforce heterogeneity. This affects the availability and knowledge acquisition ef<sup>fi</sup>ciency of existing direct ties (since workers who are engaged in knowledge provision are less ef<sup>fi</sup>cient in acquiring knowledge). Due to this, the knowledge of workers acquiring knowledge, as well as the pool of workers available for consultation, is updated infrequently. Therefore, the overall diffusion is lower for high values of workforce heterogeneity (Fig. 4-a). This also explains why the total number of times existing direct and indirect (not shown) ties are used decreases as workforce heterogeneity increases (Fig. 4-b). An increase in the knowledge acquisition ef<sup>fi</sup>ciency increases knowledge diffusion, reducing the knowledge heterogeneity of the workforce. Thus, as the knowledge acquisition ef<sup>fi</sup>ciency increases, the number of times existing direct (and indirect) ties are used increases (Fig. 4-b).

Next, we focus on the pattern in which different types of ties are used, over the planning horizon. At the beginning of the planning horizon, there are relatively fewer direct ties and it takes time to establish new direct ties. This limits access to competent workers via direct ties at the beginning of the planning horizon. On the other hand, indirect ties are relatively abundant and provide better access to competent workers, although they are less ef<sup>fi</sup>cient than direct ties. This explains why at the beginning of the planning horizon, indirect tie usage is slightly larger than direct tie usage (Fig. 4-c). Over time, direct ties are systematically created to transfer knowledge and facilitate knowledge diffusion. Moreover, the strength of direct ties increases with time, increasing the difference in knowledge sharing ef<sup>fi</sup>ciency between direct and indirect ties. In addition, knowledge diffusion results in improved access to competent workers via direct ties. Hence, we observe in Fig. 4-c that the use of direct ties signi<sup>fi</sup>cantly exceeds the use of indirect ties over time (time period greater than 60).

6.2.2. Impact of number of skills supported by the organization on knowledge diffusion and sharing

Next we study how the number of skills supported by an organization affects knowledge diffusion. As mentioned earlier, as number of skills increase, workers need to improve knowledge in multiple skills based on their current knowledge and relative importance (weight) for each skill. Hence, the number of times each tie is utilized increases with increase in number of skills (Fig. 5-a). However, the relative importance (weight) for each skill decreases, as the number of skills supported increases (sum of weights over all skills always add up to one). Also, the time that each worker can spend on acquiring knowledge in each skill decreases as the number of skills supported increases. This reduces knowledge diffusion in each skill, reducing the rate at which workers become competent. Therefore, the extent of knowledge acquired in each help seeking transaction is lower. This explains why the cumulative weighted knowledge gain decreases with increase in number of skills (Fig. 5-b), even though the total number of times direct and indirect ties are utilized increases.

## 7. Performance evaluation

To evaluate the performance of our heuristic, we solve the MIP formulation using CPLEX for small problem instances and compare it against the solution using CBH. This methodology is consistent with prior research [4,18,34]. Particularly, we compare the CPEX gap (% difference between CPLEX solution and CPLEX upper bound) to the CBH gap (% difference between CBH solution and CPLEX upper bound (or optimal solution, where applicable)). We design our experiments such that several model parameters that can affect the heuristic performance are varied, while staying within limits of reasonable problem size and complexity for CPLEX. We observe that maximum gap between the CPLEX solution and the CBH solution (CBH Gap) is about 7% for the problems solved using CPLEX . The performance of our CBH is comparable with existing research adopting this methodology [4,18,34]. Please refer to Appendix B for details of the CBH performance evaluation.

![](/api/attachments/QGVU72FR/fulltext/images/6205e5ad45baee19c23e33be694f5fab5bf1710626f52d7c809d2b2840ae75fb.jpg)

![](/api/attachments/QGVU72FR/fulltext/images/514bd6c445a919d1ef79a9a869ffb8ca3abb35350c096ae963a6aa676158d04e.jpg)

c  
![](/api/attachments/QGVU72FR/fulltext/images/1fa334bc4d6df6a5e5c961ccc331268fbba8f2c7418bdd2f8ce247d4db54f3b5.jpg)

d  
![](/api/attachments/QGVU72FR/fulltext/images/76cc6877ccca03a8f2a4daf98e929e0b515c33a393025764a0a0ee8bec719e8b.jpg)

e  
![](/api/attachments/QGVU72FR/fulltext/images/6ff2d0e844bb34cb24a49d9b7a7993b37cca1450b5a4e807f83118aa8775f2c3.jpg)  
f

![](/api/attachments/QGVU72FR/fulltext/images/e4232e3a1b1ec63f5304ba136722400440bd2c5b96280e7921bbe1777d83c371.jpg)

g  
![](/api/attachments/QGVU72FR/fulltext/images/166c735e3155a4dcb9be3a9bafc24e806df3df3dddcf1b92128a1e6a8b90a1d3.jpg)  
Fig. 3. a. Average number of times a direct tie (between Groups) is usedb. Amount of knowledge transferred per tiec. Normalized degree centrality for different values of workforce heterogeneityd. Number of direct ties created for different values of workforce heterogeneitye. Number of direct ties created for different values of time to create direct tiesf. Number of direct ties created for different knowledge transfer time (direct tie) g. Number of direct ties created for different values of pumber of skills

## 8. Model extensions

## 8.1. A model incorporating worker turnover rate

In the model developed in Section 3. we assume the workforce to be constant over the planning horizon. However, in certain environments, organizations may need to consider employee turnover rate in designing their KFNs. Although vacant positions can often be <sup>fi</sup>lled with new competent workers, worker turnover can signi<sup>fi</sup>cantly disrupt existing KFNs within the organization. In this model extension, we assume that, in each period, any worker can quit the <sup>fi</sup>rm with a certain probability. We study how worker turnover rate impacts knowledge diffusion in KFNs. In addition, we compare the performance of the KFNs created using CBH with

KFNs created using a Random Connection Policy (RCP). In RCP, direct ties are randomly created over the course of the planning horizon.<sup>3</sup>

We observe that as the employees turnover rate increases, average weighted knowledge level of the workforce signi<sup>fi</sup>cantly decreases for KFNs created using CBH and RCP (Fig. 6-a). However, KFNs created using CBH signi<sup>fi</sup>cantly outperforms ones created using RCP. This implies that KFNs created using CBH are able to better mitigate the damage caused by labor turnover. In addition, lower workforce heterogeneity using CBH indicates better knowledge diffusion in comparison with RCP (Fig. 6-b). Overall, we found that the structural properties of effective

![](/api/attachments/QGVU72FR/fulltext/images/405bbd6f23087aaa8142e5d40634def42929c5e0e3d9020cde31b7a4c04314ac.jpg)

![](/api/attachments/QGVU72FR/fulltext/images/e486358520a13f3260172f761f488831eb96a64d774ff054b4374bca77659801.jpg)

![](/api/attachments/QGVU72FR/fulltext/images/b6da556c9133b1c22bc31fc6607cf38718cee4115333df11dda18188646e4e79.jpg)  
Fig. 4. a. Percentage difference in knowledge gain for different values of workforce heterogeneity. b. Number of times direct ties are used for different values of workforce heterogeneity.c. Number of ties used over time for low workforce heterogeneity.

KFNs, in the presence of turnover, are qualitatively similar to the ones discussed in Section 6. However, we <sup>fi</sup>nd that organizations tend to compensate for high turnover rate by increasing the number of direct ties and creating more cohesive groups of workers.

## 8.2. A model incorporating knowledge depreciation

In the model discussed in Section 3, we assume that knowledge depreciation is negligible. In this section, we develop a model where we allow a worker's knowledge to depreciate over the course of the planning horizon. That is, during every period, we allow skills that are not being utilized (for provision or acquisition) to depreciate at a certain rate. As expected, we <sup>fi</sup>nd that average weighted knowledge level decreases as knowledge depreciation increases (Fig. 7-a). Additionally, we <sup>fi</sup>nd that the rate of decrease increases with number of skills. This is because with increase in number of skills, the amount of time workers can devote to updating each skill reduces. This also reduces the overall knowledge diffusion rate, which causes the knowledge heterogeneity to increase, with increase in number of skills (Fig. 7-b). Overall, we found that the structural properties of effective KFNs, in the presence of knowledge depreciation, are qualitatively similar to the ones discussed in Section 6. However, knowledge depreciation increases the need for knowledge sharing, due to which organizations encourage the creation of new direct ties and create more cohesive groups of workers, when knowledge depreciation is high.

![](/api/attachments/QGVU72FR/fulltext/images/37b76f1b5733be121c93f9e7107d5ea5c843061cb3acb5f58a33434320776e49.jpg)

![](/api/attachments/QGVU72FR/fulltext/images/0f71923bca5133610af9726c84b9280bac2bfdd2f0be0fb4001936399cb7d959.jpg)  
Fig. 5. a. Number of times direct ties are used for different values of number of skills. b. Cumulative weighted knowledge gain % difference for different values of number of skills.

## 9. Managerial implications

Our results have interesting implications for managers interested in designing effective KFNs. Understanding characteristics of effective KFNs can help managers design or improve KFNs in their organizations. Some important characteristics are discussed below.

Our results indicate that organizations could use expertise pro<sup>fi</sup>ling to classify workers into experts, average workers, and novices for effective knowledge <sup>fl</sup>ow networks. We observe that most knowledge sharing happens between average and expert workers, followed by knowledge sharing between average and novice workers. This result has important managerial implications. Organizations need to recognize that increasing number of experts alone will not necessarily increase knowledge diffusion. Average workers play a useful bridging role in facilitating knowledge transfer. We <sup>fi</sup>nd that organizations seem to bene<sup>fi</sup>t from knowledge transfer between workers who do not have very high knowledge differences. Such knowledge transfer allows workers who are sharing knowledge to become available relatively quickly for additional knowledge provision and/or knowledge acquisition. This <sup>fi</sup>nding is contrary to the common practice of encouraging knowledge sharing between experts and novices. Our results also indicate that for a given average knowledge level of the workforce, knowledge diffusion is slower in organizations with higher workforce heterogeneity.

![](/api/attachments/QGVU72FR/fulltext/images/6987faaa09e6d4f583a7ecafaa34db7f41676c4cb5daac2525ca236adfce484f.jpg)

![](/api/attachments/QGVU72FR/fulltext/images/d143c0da80ff943d5891c2ddea2dead4fe6f7edae06753f3f553a78f8c0a55bd.jpg)  
Fig. 6. a. Average weighted knowledge level for different values of labor turnover rate. b. Workforce heterogeneity for different values of labor turnover rate.

![](/api/attachments/QGVU72FR/fulltext/images/50a443dd580f9c46a47f48bdcad5481550e8c6abbfd369d8e3098f934c89b1cb.jpg)

![](/api/attachments/QGVU72FR/fulltext/images/ccb3d650870dac2abc7c4c53bf0479b56c4acf02c0fb5dfe155c71f8feb491ba.jpg)  
Fig. 7. a. Average weighted knowledge level for different values of knowledge depreciation rate. b. Workforce heterogeneity for different values of knowledge depreciation rate.

It is important to note that the value of a direct tie is signi<sup>fi</sup>cantly enhanced by indirect ties (network effect). Hence, connections to more cohesive groups of workers are more valuable (have more indirect ties per worker). As discussed earlier, groups of workers with higher average knowledge (such as experts) are more cohesive in effective KFNs. Hence, organizations seeking to create effective KFNs should create cohesive groups of experts. Cohesive groups could be created through direct tie creation using one of the techniques described earlier. In addition, by involving experts in hiring other experts, the hiring process could be used to increase group cohesiveness. Creating such cohesive groups is less important for lower skilled groups such as novices. Our results also have interesting implications in an environment that supports multiple skills. Creating direct ties between workers with complementary skill sets results in effective KFNs. Such ties are particularly valuable between experts, due to the network effects discussed above. Such ties tend to be used extensively, and having such ties reduces the number of direct ties needed as the number of skills supported by the organization increases. We also <sup>fi</sup>nd that under environments of high worker turnover or high knowledge depreciation, organizations need to encourage the creation of more direct ties and create more cohesive groups of workers, for effective knowledge exchange.

## 10. Limitations and future research

This research assumes that knowledge is transferred from only one worker to another worker at a time. Future research could study KFNs that allow knowledge to be transferred among a group of employees. For example, knowledge can be transferred through seminars provided by co-workers to share their expertise with other team members, group discussions between multiple members in the same of<sup>fi</sup>ce, and other group related techniques. This extension would involve further exploration about group knowledge sharing dynamics, and is likely to be more complex. This research also assumes that all workers are equally busy, on average, over the planning horizon, when identifying optimal knowledge sharing transactions. Scenarios when each worker has a different task pro<sup>fi</sup>le could be studied in future research.

## 11. Conclusions

“Knowledge intensive service providers are highly dependent on human workers who possess specialized knowledge and skills.” [36]. Such companies are increasingly interested organizational design for knowledge work [36]. While there is extensive prior research on using technology for storing and retrieving knowledge, the concept of knowledge sharing using organizational social relationships is relatively new. Organizational design to facilitate knowledge sharing is an under researched topic. This research aims to facilitate the design of effective KFNs. The model and results presented in this paper facilitate managerial benchmarking. Managers can use this model to understand important factors to consider when designing and using KFNs. Identifying such factors and their interrelationships allows managers to compare (benchmark) their organizations with effective KFNs and facilitates organizational change [40]. The model and solution procedure proposed in this paper can be used either as a starting point for organizational design or as a means of benchmarking existing organizations that create or apply knowledge.

## Acknowledgment

This research was funded in‐part by a grant from the Belk College of Business, UNC‐Charlotte.

## Appendix A. Supplementary material

Supplementary data to this article can be found online at http:// dx.doi.org/10.1016/j.dss.2012.04.007.

## References

[1] R. Agarwal, A.K. Gupta, R. Kraut (Eds.), Special Issue: The Interplay Between Digital and Social Networks, Information Systems Research, 19, 4, September 2008.

[2] L. Agrote, P. Ingram, Knowledge transfer: a basis for competitive advantage in <sup>fi</sup>rms Organizational Behavior and Human Decision Processes 82 (1) (May 2000) 150–169.

[3] APQC, Using Knowledge: Advances in Expertise Location and Social Networking. Available: ftp://public.dhe.ibm.com/services/us/gbs/bus/hcm/rbtt/expertiselocation. pdf 2010.

[4] A. Bajaj, R. Russell, AWSM: allocation of work<sup>fl</sup>ows utilizing social network metrics, Decision Support Systems 50 (1) (December 2010) 191–202.

[5] D. Bartholomew, Sharing knowledge. Available: http://www.knowledgeboard com/download/2520/SharingKnowledge1.pdf 2005.

[6] J.A.C. Baum, W.B. Berta, Sources, dynamics and speed: population-level learning by organizations in a longitudinal behavioral simulation, in: A.S. Miner, P. Anderson (Eds.), Population-Level Learning and Industry Change, Advances in Strategic Management, JAI Press, Stamford CT, 1999, pp. 155–184

[7] S.P. Borgatti, R. Cross, A relational view of information seeking and learning in social networks, Management Science 49 (4) (2003) 432–445.

[8] A.M. Bulgiba, M.H. Noran, IT usage, perceptions and literacy of medical students, Asia Paci<sup>fi</sup>c Journal of Public Health 15 (2) (2003) 127–134.

[9] A. Cabrera, E. Cabrera, Knowledge sharing dilemmas, Organization Studies 23 (5) (September 2002) 687–710.

[10] N.K. Chen, T. Edgington, Assessing value in organizational knowledge creation: considerations for knowledge workers, MIS Quarterly 29 (2) (June 2005) 279–309.

[11] D. Constant, L. Sproull, S. Kiesler, The kindness of strangers: the usefulness of electronic weak ties for technical advice, Organization Science 7 (2) (1996) 119–135.

[12] R. Cowan, N. Jonard, Network structure and the diffusion of knowledge, Journal of Economic Dynamics and Control 28 (2004) 1557-1575

[13] R. Cross, A. Parker, L. Prusak, S.P. Borgatti, Knowing what we know: supporting knowledge creation and sharing in social networks, Organizational Dynamics 30 (2) (2001) 100–120.

[14] R. Cross, A. Parker, S. Borgatti, A Bird's-eye View: Using Social Network Analysis to Improve Knowledge Creation, and Sharing., Available: http://www ischoolutexas edu/\~i385q/readings/Cross. 2002, using, social network,pdf 2002

[15] T.H. Davenport, L. Prusak, Working Knowledge, Harvard Business School Press, Boston, 1998.

[16] T.H. Davenport, D.W. DeLong, M.C. Beers, Building Successful Knowledge Management Projects, Center for Business Innovation Working Paper, 1997.

[17] S.S. Dawes, N. Helbig, R. Hassan, J.R. Gil-Garcia, New York State IT Workforce Skills Assessment Statewide Survey Results. Available: http://www.ctg.albany.edu publications/reports/nysit\_statewidesurvey/nysit\_statewidesurvey.pdf 2006.

[18] S. Dong, M. Johar, R. Kumar, A benchmarking model for management of knowledgeintensive service delivery networks, Journal of Management Information Systems 28 (3) (2012) 127–160.

[19] J.H. Dyer, K. Nobeoka, Creating and managing a high-performance knowledgesharing network: the Toyota case, Strategic Management Journal 21 (2000) 345–367.

[20] M.G. Everett, S.P. Borgatti, The centrality of groups and classes, Journal of Mathematical Sociology 22 (3) (1999) 181–201.

[21] R. Geel, J. Mure, U. Backes-Gellner, Speci<sup>fi</sup>city of Occupational Training and Occupational Mobility: An Empirical Study Based on Lazear's Skill-Weights Approach, Economics of Education Working Paper Series, 2008 Available: http://ideas.repec. org/p/iso/educat/0038.html.

[22] S.C. Goh, Managing effective knowledge transfer: an integrative framework and some practice implications, Journal of Knowledge Management 6 (1) (2002) 23–30.

[23] R.M. Grant, Toward a knowledge-based theory of the <sup>fi</sup>rm, Strategic Management Journal 17 (Winter 1996) 109–122.

[24] I. Guy, M. Jacovi, E. Shahar, N. Meshulam, V. Soroka, S. Farrell, Harvesting with SONAR — the value of aggregating social network information, in: M. Burnett, M. Costabile, T. Catarci, B. Ruyter, D. Tan, M. Czerwinski, A. Lund (Eds.), Online Social Networks. Proceeding of the twenty-sixth annual SIGCHI conference on Human factors in computing systems, ACM Press, New York, 2008, pp. 1017–1026.

[25] M.T. Hansen, Knowledge networks: explaining effective knowledge sharing in multiunit companies, Organization Science 13 (3) (2002) 232–248.

[26] M.T. Hansen, The search-transfer problem: the role of weak ties in sharing knowledge across organization subunits, Administrative Science Quarterly 44 (1) (March 1999) 82–111.

[27] J. Heerwagen, K. Kampschroer, K. Powell, V. Loftness, Collaborative knowledge work environments, Building Research and Information 32 (6) (2004) 510–528.

[28] C.A. Hidalgo, The value in the links: networks and the evolution of organizations. Available: http://www.chidalgo.org/Papers/Hidalgo\_SageChapter\_2010.pdf 2010.

[29] IBM, Improving workplace collaboration: Social network analysis Available: http:// domino.watson.ibm.com/odis/odis.nsf/pages/solution.13.html 2006

[30] J.L. Jones, R.F. Easley, G.J. Koehler, Market segmentation within consolidated emarkets: a generalized combinatorial auction approach, Journal of Management Information Systems 23 (1) (Summer 2006) 161–182.

[31] M. Kilduff, W. Tsai, Social Networks and Organizations, Sage Publications Ltd, London, 2003.

[32] Y. Kim, R. Krishnan, L. Argote, The Learning Curve of IT Knowledge Workers in a Computing Call Center, Paper presented at the INFORMS Annual Meeting, San Francisco, CA, November 12–15 2005.

[33] J. Kotlarsky, I. Oshri, Social ties, knowledge sharing and successful collaboration in globally distributed system development projects, European Journal of Information Systems 14 (1) (2005) 37–48.

[34] R.L. Kumar, S. Park, C. Subramaniam, understanding the value of countermeasure portfolios in information systems security, Journal of Management Information Systems 25 (2) (Fall 2008) 241–280.

[35] S. Lester, Novice to Expert: the Dreyfus model of skill acquisition. Available: http:// www.sld.demon.co.uk/dreyfus.pdf 2005.

[36] Y.T. Leung, S.M. Glissmann, A clustering approach to the design of knowledgeintensive service providers. Available: http://domino.research.ibm.com/library/ cyberdig.nsf/papers/58C6B1D509E8DCA68525780000603960 December 2011.

[37] D.Z. Levin, E.M. Whitener, R. Cross, Perceived trustworthiness of knowledge sources: the moderating impact of relationship length, Journal of Applied Psy chology 91 (5) (2006) 1163–1171.

[38] S.S. Levine, R. Kurzban, Explaining clustering in social networks: towards an evolutionary theory of cascading bene<sup>fi</sup>ts, Managerial and Decision Economics 27 (2–3) (March-May 2006) 173–187.

[39] S.S. Levine, M. Prietula, Towards a Contingency Theory of Knowledge Exchange in Organizations, Academy of Management Best Paper Proceedings, Atlanta, GA, 2006.

[40] M. Liberatore, A. Hatchuel, B. Weil, A. Stylianou, An organizational change perspective on modeling, European Journal of Operational Research 125 (2000) 184–194.

[41] P.V. Marsden, K.E. Campbell, Measuring tie strength, Social Forces 63 (2) (December 1984) 482–501.

[42] R. Nicolas, Knowledge management impacts on the decision-making process, Journal of Knowledge Management 8 (1) (2004) 20–31.

[43] I. Nonaka, R. Toyama, A. Nagata, A <sup>fi</sup>rm as a knowledge-creating entity: a new perspective on the theory of the <sup>fi</sup>rm, Industrial and Corporate Change 9 (1) (2000) 1–20.

[44] F.G.W.C. Paas, Training strategies for attaining transfer of problem-solving skill in statistics: a cognitive load approach, Journal of Educational Psychology 84 (4) (1992) 429–434.

[45] B. Prabhakar, C.R. Litecky, K. Arnett, IT skills in a tough job market, Communications of the ACM 48 (10) (October 2005) 91-94

[46] H.R. Rao, A. Chaudhury, M. Chakka, Modeling team processes: issues and a specific example, Information Systems Research 6 (3) (September 1995) 255–285.

[47] N. Sahoo, R. Krishnan, J. Callan, Formation of citation and reply ties over intraorganizational blog network, CIST Proceedings Washington D.C, 2008.

[48] S. Sayın, S. Karabatı, Assigning cross-trained workers to departments: a two-stage optimization model to maximize utility and skill improvement, European Journal of Operational Research 176 (3) (February 2007) 1643–1658.

[49] S. Teasley, L. Covi, M.S. Krishnan, J.S. Olson, How does radical collocation help a team succeed? Proceedings of CSCW, 2000, pp. 339–346.

[50] W.M.P. Van Der Aalst, H.A. Reijers, M. Song, Discovering social networks from event logs, Computer Supported Cooperative Work 14 (6) (December 2005) 549–593.

[51] D.J. Watts, S.H. Strogatz, Collective dynamics of small-world networks, Nature 393 (June 1998) 440–442.

[52] L. Williams, R. Kessler, Pair Programming Illuminated, Addison-Wesley, Bonston, 2003.

[53] H. Zhuge, Knowledge <sup>fl</sup>ow network planning and simulation, Decision Support Systems 42 (2006) 571–592

Su Dong is a doctoral student in the Belk College of Business Administration, UNC Charlotte. He has a degree in MIS from University of Shanghai for Science and Technology, China. His research interests include knowledge management strategies, and knowledge sharing in online communities. His research has been accepted by Workshop on Information Technologies and Systems, and Workshop on eBusiness.

Monica S Johar is currently an Assistant Professor of Management Information Systems at University of North Carolina at Charlotte. She received a PhD in Management Science with a concentration in MIS from University of Texas at Dallas in 2006. Her research interests include optimal software development methodologies, content delivery systems, knowledge management and web personalization. She is an active member of the Association of Information Systems and INFORMS. She has several publications in leading IS journals such as Information Systems Research and conferences like Workshop on Information Technologies and Systems, Conference on Information Systems and Technology, and Workshop on e-Business.

Ram L. Kumar is Professor in Belk College of Business Administration, UNC-Charlotte. He received his Ph.D. in Information Systems from the University of Maryland. He worked for maior multinational corporations such as Fujitsu before entering academics. His re: search has been funded by organizations such as the U.S. Department of Commerce, and organizations in the <sup>fi</sup>nancial services and energy industries. His current research interests include techniques for evaluating and managing portfolios of IT investments, Service Science, and, Knowledge Management Systems. His research has been published in Communications of the ACM, Computers and Operations Research, Decision Sciences, Decision Support Systems, International Journal of Electronic Commerce, International Journal of Production Research, Journal of MIS, and others. He has advised organizations such as the U.S. Department of Energy and other organizations in the private sector on evaluation of R&D Projects and IT Portfolios.
