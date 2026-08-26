---
otero_id: 8842
otero_key: "FDURDEKP"
title: "Balancing Affordances and Constraints: Designing Enterprise Social Media for Organizational Knowledge Work"
authors: "Hani Safadi"
year: "2024"
journal: "MIS Quarterly"
doi: "10.25300/misq/2023/16499"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# BALANCING AFFORDANCES AND CONSTRAINTS: DESIGNING ENTERPRISE SOCIAL MEDIA FOR ORGANIZATIONAL KNOWLEDGE WORK<sup>1</sup>

Hani Safadi Terry College of Business, University of Georgia Athens, Georgia, USA {hanisaf@uga.edu}

Enterprise social media (ESM) is changing how knowledge workers interact and share information; however, a debate persists as to whether ESM is an adequate knowledge management system. ESM provides a rich set of affordances for organizational knowledge work, such as improved organizational memory, but also constrains knowledge work performance because of digital interruptions. Extending and complementing existing scholarship, this study asks the following research question: How can organizations design ESM to realize its knowledge work benefits? Using a computational agent-based model that incorporates the design features of ESM, workers’ attitudes, and resulting ESM-use affordances and constraints, this study shows how ESM-use outcomes are contingent both on the design of and users’ attitudes toward ESM. Specifically, the negative effects of ESM interactivity are mitigated when employees have a low transparency preference and access ESM without posting as much. The study further unpacks asymmetric engagement as the mechanism that leads low transparency configurations to be more resilient to the negative effects of interruptions driven by ESM interactivity. Asymmetric engagement—learning from posted content without interacting often—enables the gradual creation of organizational memory while maintaining a broad user base by minimizing interruptions. These results ultimately contribute a multilevel model of ESM use and knowledge work outcomes, enhancing the theoretical understanding of previously studied mechanisms such as communication visibility and providing implications for organizations designing ESM.

Keywords: Enterprise social media, interactivity, visibility, transparency, ambient awareness, socialization, knowledge work, digital interruptions, asymmetric engagement, agent-based model

## Introduction

In recent years, the use of enterprise social media (ESM) has become increasingly popular in organizations to facilitate communication, collaboration, and knowledge sharing among employees. ESM platforms such as Jive, Yammer, Chatter, and Connections afford a rich set of communication, sharing, and socialization capabilities (Kane, 2015; Leonardi & Vaast, 2017; Majchrzak et al., 2013). Accordingly, there has been a growing scholarly interest in the potential of ESM to support knowledge work in various contexts (Leonardi, 2014; Van Osch & Steinfield, 2018). At the same time, recent research has highlighted the debilitating effects of digital interruptions and technostress resulting from the pervasiveness of workplace technologies like email and ESM (Addas & Pinsonneault, 2015; Brooks & Califf, 2017; Chen & Karahanna, 2018; Magni et al., 2022; Tams et al., 2020).

The current study is motivated by the need to incorporate the theoretical underpinnings and empirical findings from the two streams of work that respectively emphasize the enabling and constraining aspects of ESM on knowledge work. The research question guiding this work—How can organizations design ESM to realize its knowledge work benefits?— emphasizes that in designing ESM, organizations can promote a variety of its affordances while mitigating some of its constraints (Kane et al., 2014; Kietzmann et al., 2011). Prior studies of how ESM can enable and constrain knowledge work thus provide a context for investigating this question. Studies on the enabling side show that ESM communication visibility results in improved organizational memory and better knowledge-sharing practices (Leonardi, 2014, 2015) while studies on the constraining side show that ESM creates digital interruptions (Stohl et al., 2016; Van Osch & Steinfield, 2018) and provokes employees’ privacy and accountability concerns (Gibbs et al., 2013; Treem, 2015).

Balancing these affordances and constraints is challenging because of their interdependence. For example, visible communication enables better knowledge sharing while raising privacy concerns. Further, many individual and organizational contingencies affect the outcomes of ESM implementation including users’ roles, the nature of the content, group size, and group openness (Bulgurcu et al., 2018; Sutanto et al., 2018; van Osch & Bulgurcu, 2020). Finally, employees’ attitudes and use behaviors vary and are becoming more sensitive to the tradeoffs of the benefit and cost implications of workplace technologies (Bernstein, 2012; Hafermalz, 2020).

Survey research on ESM implementations supports the existence of these challenges. On the one hand, ESM use is associated with a higher perception of organizational transparency and higher employee engagement (Men et al., 2020), ESM increases workplace integration which decreases employee turnover intention and increases job satisfaction (Moqbel et al., 2020), and ESM use promotes employee agility via enhanced metaknowledge (Wei et al., 2020). On the other hand, ESM implementations are still not widely adopted by employees (30-50%) or executives (less than 10%) (Charki et al., 2018; Li, 2015), many employees still report traditional communication channels to be more effective than ESM even though younger employees are more likely to adopt ESM (Cardon & Marshall, 2015), and even when adopted, ESM faces engagement challenges from employees (Liu & Bakici, 2019).

Building on this prior body of work, I develop an agent-based computational model that incorporates the design features of ESM (visibility and interactivity), workers’ attitudes toward transparency and interruption, and resulting ESM-use affordances and constraints. Specifically, the model focuses on how ESM benefits collective knowledge work through increasing socialization and improving workers’ metaknowledge while, at the same time, considers how digital interruptions resulting from excessive ESM use negatively affect users’ adoption.

This study uses over half a million simulation runs to provide new insights into how ESM could promote knowledge work. The results confirm and generalize prior findings: While using ESM promotes metaknowledge accuracy, which generally leads to increased performance, ESM interactivity also increases the number of interruptions, which hurts adoption and performance. These findings shed light on the mechanisms driving these outcomes. In particular, they show how ESM-use outcomes are contingent both on the design of ESM and users’ attitudes toward ESM. That is, the results show how a low preference for transparency regulates users’ ability to realize their learned metaknowledge. This attitude results in asymmetric engagement that reduces the number of interruptions of all users even when communication is visible and ESM is designed to be highly interactive. Ultimately, these results contribute to a better understanding of how ESM could improve knowledge work and have implications for organizations implementing ESM. In addition, this study provides a methodological contribution to studying affordances by modeling technology design and users’ attitudes in a computational model. In this paper, I review work related to ESM and its affordances for knowledge work, describe the model and experiments, and discuss the results and their implications.

## ESM and Knowledge Work

This work is motivated by this example: Alice checks her workplace ESM daily. Many co-workers are posting and sharing information. Some of this information is useful because some of these co-workers seem to be working on related problems or have expertise relevant to Alice’s work. After reviewing the newsfeed, Alice decides to join the conversation by posting and interacting with a co-worker on a topic of shared interest. Like Alice, Bob checks the ESM newsfeed every day. Bob, however, does not like posting in public, so while he reads through others’ postings, he only occasionally interacts with others on ESM. Bob likes being able to passively “listen” to ESM conversations. Recently, both Bob and Alice have been struggling with whether to maintain ESM use, taking into consideration how much time such use consumes during the work day. Should they spend time browsing the ESM in the hopeful pursuit of some useful knowledge or disengage altogether?

In this scenario, the knowledge workers are interested in accruing work-related benefits from using the ESM. Granted, some users may want to use ESM for recreational purposes, but for them, the extent to which ESM use crowds out other work activities is less important. From the organization’s perspective and notwithstanding the intrinsic value of social interactions, ESM interactions that align with work relationships are advantageous for knowledge work. Because the organization may not know all work dependencies among workers (Clement & Puranam, 2018), ESM provides a forum for workers to discover workplace synergies such as relevant expertise or shared interests. Thus, the time spent on ESM can indirectly improve knowledge work performance (Leonardi, 2014).

This example highlights the challenges of understanding the outcomes of using ESM. As with other information systems (IS), the use of ESM depends on the attitude of users and their perception of the technology as useful (Davis, 1989), yet the myriad affordances of ESM use are not all effective for knowledge work (Burton-Jones & Volkoff, 2017; Majchrzak & Markus, 2013). In this example, Alice uses ESM to learn and interact with others while Bob uses it mostly to learn from others’ interactions. In what follows, I review ESM features, relevant user attitudes toward ESM, and ESM affordances for organizational work (Leonardi & Vaast, 2017).

## ESM Features: Visibility and Interactivity

ESM is structured around the public sharing of content that includes communication, user profiles, and social network relations (Kane et al., 2014). Content shared on ESM usually defaults to public access. Even when ESM provides more granular visibility, shared content targets a large participant group, and it is often hard for the content’s originator to assess its target audience. Another key feature of ESM is its interactivity. Unlike the previous generation of knowledge management systems (Alavi & Leidner, 2001), ESM is focused not only on archiving content but also on continuously presenting it and inviting further participation (Majchrzak et al., 2013). Accordingly, ESM triggers participants’ attention and engagement through a variety of design features such as endlessly scrolling newsfeeds to present content and elicit interactions, the opportunity to participate in these public interactions, and constant notifications to elicit further engagement. While ESM implementations vary in their exact specifications (Kietzmann et al., 2011), visibility and interactivity are two underlying design features. Across the board, ESM platforms are designed to constantly grab users’ attention and encourage their continuous engagement (Seaver, 2019; Wu, 2017). The extent to which these two features translate to use depends on users’ attitudes toward transparency and interruption.

## ESM Users’ Attitudes

The adoption and use of ESM among employees depend on a variety of factors including legal obligation, organizational norms, and social awareness (Levordashka & Utz, 2016; Stohl et al., 2016). Unlike other organizational systems whose usage is often mandated (Lapointe & Rivard, 2005), ESM is conceived as a tool for informal communication that supports existing systems such as email (Kane, 2015). Thus, the adoption of ESM, and conversely its avoidance, depends on users’ attitudes toward it. More importantly, like other IS, ESM use cannot be represented by the simple binary of use and nonuse (Burton-Jones & Volkoff, 2017); rather, use manifests on a spectrum according to the degree—and intensity—to which users actualize the affordances of ESM (Gibbs et al., 2013; Strong et al., 2014). Prior work on ESM points to two user attitudes that can determine its use patterns: transparency preference and interruption tolerance.

## Transparency Preference

Because ESM communication is mostly visible, communication and interaction are transparent to other knowledge co-workers. According to prior research, this transparency is met with different attitudes by users. While many digital natives born and raised in the “social media era” are accustomed to transparency and have a positive attitude toward it (Hafermalz, 2020; Moran, 2020), other workers take issue with transparency because it requires increased accountability for shared content (Arazy & Gellatly, 2012; Treem, 2015) and decreases privacy (Adjerid et al., 2018; Bernstein, 2012). Studies have found that workers using ESM often exhibit avoidance behavior to reestablish privacy: for example, some workers make their visible work opaque by mixing it with irrelevant information to distract potential observers (Stohl et al., 2016). Attitudes toward transparency thus dictate how workers use ESM. Workers with a high transparency preference post and interact with others publicly. In contrast, workers with a low transparency preference may browse ESM, learning from others’ interactions, but seldom interact with others (Ellison et al., 2015; Gibbs et al., 2013; Laitinen & Sivunen, 2021).

## Interruption Tolerance

While sharing and interacting through ESM can benefit users, some shared content can be superficial or irrelevant to a broad audience (Bulgurcu et al., 2018; Gibbs et al., 2013). Because ESM is interactive, posted content and social interactions are not passive but drive further user engagement (e.g., through interactive features such as notifications and newsfeeds). In turn, these digital interruptions can disrupt the flow of work (Chen & Karahanna, 2018; Luqman et al., 2021; Weinert et al., 2022), overload workers with irrelevant information, cause stress due to loss of focus, and demand further user involvement to convert information into an actionable form (Addas & Pinsonneault, 2015). Users have different tolerances for such interruptions (De Alwis et al., 2022; Luqman et al., 2021). For example, generational differences play a role in perceiving and handling interruptions (Baham et al., 2023). Those with a high degree of tolerance will maintain their engagement with ESM despite interruptions, while those with a low degree of interruption tolerance adapt their usage or abandon ESM altogether (Gibbs et al., 2013; Van Osch & Steinfield, 2018). Depending on users’ attitudes, the two features of visibility and interactivity manifest in two essential affordances for knowledge work: metaknowledge learning and social interaction.

## ESM Affordance 1: Metaknowledge Learning

Studies of organizational learning have shown that informal communication, socialization, and personal relationships play an enabling role in facilitating knowledge work. One mechanism through which socialization promotes knowledge work is the development of better organizational memory, also known as a transactive memory system (Wegner, 1987). Transactive memory holds information about other organizational members’ knowledge, also referred to as metaknowledge (Ren & Argote, 2011). This metaknowledge, in turn, plays a facilitating role in collaborative knowledge work because it enables workers to identify others who can provide valuable input and create synergies (Argote & Guo, 2016; Hansen, 2002; Zahra et al., 2020).

ESM promotes metaknowledge not only through socialization but also through disclosing interactions publicly. Such visible communication creates ambient awareness through which workers can learn about others without necessarily interacting with them (Leonardi, 2014, 2015). Metaknowledge ultimately improves work performance as workers benefit from better knowledge sharing, knowledge recombination, and reduced knowledge duplication (Leonardi, 2014, 2015; Sun et al., 2019; Utz & Levordashka, 2017). That is, ESM is like a leaky pipe (Leonardi et al., 2013), and knowledge leakiness facilitates knowing more about others and therefore identifying the location of expertise within the organization (Fulk & Yuan, 2013; Leonardi, 2017). Metaknowledge learning thus depends on both the design of ESM for publicly visible communication and a positive attitude toward transparency held by the users who create and share knowledge publicly.

## ESM Affordance 2: Social Interaction

Socialization promotes the creation of an environment in which users can share knowledge and expertise (Brown & Duguid, 1991; Faraj et al., 2016). Social interaction and content creation are intertwined in ESM. Sharing content via ESM has a major social element because of the large number of social tagging features used to identify the source of the content as well as invite its intended audience to participate in the discussion (Majchrzak et al., 2013). Social interaction through ESM offers an opportunity to foster informal work relationships. These online social ties can complement existing social ties and facilitate knowledge work. Online ties, too, are less likely to be redundant and therefore facilitate finding distant knowledge (Leonardi et al., 2013; Majchrzak et al., 2013). These ties are also less likely to be controlled by the organization and therefore may help identify work dependencies not known by the organization’s designer (Clement & Puranam, 2018). Social interaction depends on the design of ESM to be interactive to constantly elicit social interactions (e.g., through newsfeeds), as well as its users’ positive attitude toward transparency to disclose their content and social interactions to others.

These two affordances require workers to expend time and effort to interact with others and examine others’ previous interactions to learn from them. Engaging in and with these interactions creates a digital exhaust for everyone. Accordingly, accruing the benefits of ESM is associated with an increase in digital interruptions in the workplace.

## ESM Constraint: Digital Interruptions

Most scholarly studies of ESM have focused on its affordances for knowledge work (Leonardi & Vaast, 2017). Recent studies, however, point to the many downsides of ESM (Sun et al., 2021) that are consistent with the pitfalls of other workplace technologies and related to issues of privacy (Bernstein, 2012), security (Gibbs et al., 2013), and accountability (Stohl et al., 2016; Treem, 2015). While I recognize these important issues, I focus on one critical constraint for work performance in the current study: digital interruptions (Addas & Pinsonneault, 2015; Chen & Karahanna, 2018; Newport, 2021). The continuous, interactive nature of ESM means that it can potentially be a source of constant interruption for workers (Luqman et al., 2021). Working in such an environment can disrupt knowledge work and lead to reduced productivity and lower organizational performance (Sun et al., 2021). Research has shown that digital interruptions can harm task performance, particularly when they necessitate multitasking or switching attention between tasks (Chen & Karahanna, 2018). ESM may also make workers feel overwhelmed by the amount of information they encounter, such that processing it all effectively becomes a struggle (Zeldes et al., 2007). This can further contribute to reduced productivity and lower organizational performance. Rampant digital interruptions also mean that the voluntary adoption of ESM may remain low especially when workers are sensitive to interruptions and their impact on working conditions (Charki et al., 2018; Li, 2015).

## Synthesis: ESM and Knowledge Work Performance

The overarching research question of this work asks: “How can organizations design ESM to realize its knowledge work benefits?” In setting out to answer this question, I assume that the organization is interested in the collective performance resulting from workers using ESM for knowledge work and that it can tweak the ESM’s design features. However, the organization may not be able to fully assess the outcome of improving knowledge work performance, at least in the short term. Furthermore, given conflicting empirical accounts about ESM, the design features and processes needed to achieve this outcome remain unclear. I also assume that, unlike other workplace technologies such as email, ESM is a complementary technology, which means its use is voluntary. Thus, when knowledge workers decide not to use ESM, the organization does not reap its promised potential benefits. Ultimately, I leverage the extant scholarly work on ESM affordances (Leonardi & Vaast, 2017) and the constraints of workplace technologies (Addas & Pinsonneault, 2015; Chen & Karahanna, 2018) to explicate how design features interact with workers’ attitudes to actualize affordances and constraints and drive performance (Figure 1).

Balancing the benefits of ESM affordances with the costs of digital interruptions is key to maximizing the impact of ESM on organizational performance, and users’ attitudes toward ESM can play a significant role in driving use and subsequently realizing affordances. Like in other instances of open collaboration (Levine & Prietula, 2014), some ESM users can benefit without contributing. Still, ultimately realizing the benefits of ESM requires a certain level of buyin and adoption. Assuming that workers are interested in using ESM to improve their work performance, the costs associated with using it, along with their attitudes toward transparency and interruption, determine whether and the extent to which they use it. These factors and their interdependencies make predicting the outcomes of ESM implementation challenging. They also suggest that empirical studies cover a small number of ESM implementation scenarios. Because these factors are hard to encounter in an observational study and are very expensive to create experimentally, agent-based models are well suited for the purpose of this study (Prietula, 2011).

## Agent-Based Modeling of ESM

Agent-based models (ABM) are computational tools used to study complex social and organizational phenomena in which the outcomes emerge from the interactions of interdependent and diverse agents (Miller & Page, 2007; Prietula, 2011). Agents are computational entities with properties and rules of behavior (Wilensky & Rand, 2015). By simulating agents’ behavior over time, agent-based modeling can generate the macro system behavior from the microlevel behavior of agents (Schelling, 1978). ABMs are used to study a variety of phenomena in IS (Brunswicker et al., 2019; Haki et al., 2020; Nan, 2011; Sturm et al., 2021), online communities (Oh et al., 2016; Ren et al., 2007), open collaboration (Levine & Prietula, 2014), organization innovation (Lazer & Friedman, 2007; Siggelkow & Rivkin, 2006), and organizational knowledge sharing (Levine & Prietula, 2012; Ren et al., 2006). These computational models are superior to other analytical models when the modeled phenomenon is complex and involves multiple interdependencies among its parts (Prietula, 2011). I start with prior scholarship using ABM to study organizational and knowledge work and then discuss how ABM can be used to study ESM use specifically.

## Computational Modeling of Organizational Work

Organizations are goal-directed collectives of individuals (March & Simon, 1958) often structured as hierarchies (Coase, 1937; Williamson, 1975) to guide how individuals collaborate and coordinate to achieve the organization’s collective goals. One view that exploits the hierarchic nature of the organization is the microstructural view (Puranam, 2018). A microstructural view of organizations focuses on patterns of ordered and unordered subsystem interactions in the organization (Puranam, 2018, Chapter 1). For this study’s context, a microstructural perspective is appropriate because it focuses on the outcomes of dyadic interactions among workers using ESM to communicate and collaborate. I draw from several prior models of organizations in representing organization memory, organization structure, and knowledge work processes (Raveendran et al., 2022; Ren et al., 2006).

Organizational work involves coordination among organizational members. To achieve the collective goal, some pairs of workers need to work together to execute their tasks. Other workers are independent and do not require any collaboration to complete their tasks. The nature of the work and the goal of the organization determine what collaborations are needed and when.

![](/api/attachments/FDURDEKP/fulltext/images/83c1ec7e75cd7226770b864a61af04715b1a0717018b819d5602205b279700e3.jpg)

Accordingly, I assume an exogenous set of true dependencies among workers although these dependencies may not be fully known to the workers and the organization’s designers (Clement & Puranam, 2018). I represent true dependencies among workers with the binary matrix ?? of size $m \times m ,$ where ?? is the number of workers in the organization. The value $W _ { i j }$ represents worker ??’s dependency with worker ??. Two workers are interdependent if the value of one performing her tasks depends on collaborating with the other worker (Puranam et al., 2012). I further assume that these interdependencies are symmetrical and complementary. If one worker A depends on another B, then B depends on A, and the value of A and B when they collaborate is greater than the value of either one without collaborating with the other. This assumption fits the context of knowledge work where knowledge is non-rivalrous and additive (Clement & Puranam, 2018). Figure 2 offers an illustration. In it, a solid line represents work dependencies, Workers 1 and 2 are dependent on each other, as are Workers 1 and 3, and Workers 2 and 3 are independent.

While it seems natural that workers should be aware of their dependencies, ??, this may not always be feasible. Clement and Puranam (2018) differentiate between organizational work that focuses on the search for solutions where tasks are stable and workers search for the best way to accomplish them (Ethiraj & Levinthal, 2004), and organizational work that focuses on the search for a structure where tasks are novel and workers need to discover the valuable patterns of interaction with others to increase their task performance. Similarly, in knowledge work, many dependencies represent untapped synergies (von Hippel, 1994). Knowledge work includes two modes of problem solving: coordinated and uncoordinated. In coordinated problem solving, experts from multiple domains of knowledge need to come together to solve a problem (Faraj & Xiao, 2006; Shore et al., 2015). In uncoordinated problem solving, problem solvers are interdependent and many tasks are addressed by single problem solvers (Jeppesen & Lakhani, 2010; von Hippel, 1994). As an example of coordinated knowledge work, consider trauma surgeons operating on a patient (Faraj & Xiao, 2006). Each surgical team member brings their expertise and knowledge to the problem-solving process and must coordinate their efforts to achieve the collective goal. As an example of uncoordinated knowledge work, consider an engineering firm that engages in multiple international projects (Haas et al., 2015). While each project demands coordinated work, synergies can be gained when engineers share knowledge across the projects. To achieve this goal, the firm leverages a community platform for engineers to interact with each other.

These two modes of problem solving, however, are not mutually exclusive. Uncoordinated problem solving does not rule out teamwork. For knowledge workers, a degree of work decomposition allows them to focus on independent tasks and collectively integrate later (Baldwin & Clark, 2000; Raveendran et al., 2016). In coordinated work, the organization is likely to have dedicated structures and technologies for provisioning information needed for coordination and not rely on general purpose tools like ESM. Thus, I focus on uncoordinated knowledge work where every worker has a task to complete but can benefit from knowledge spillovers and synergies by interacting with others.

If work dependencies are not known ex ante, how can workers learn about them? One mechanism is “problemistic search” (Posen et al., 2018), where workers explore new interactions with others when their performance falls below a certain aspirational level. Over time, this search leads workers to find truly valuable interdependencies (Clement & Puranam, 2018). Workers can also learn about work dependencies by using organizational information systems (Alavi & Leidner, 2001; Haas et al., 2015). This knowledge of the work environment is part of the organization’s metaknowledge and is essential for organizational work (Argote & Miron-Spektor, 2011; Ren et al., 2006; Wegner, 1987). Complementing prior work that examined how workers can learn about work structures (Clement & Puranam, 2018), I focus on the enabling role of organizational IS such as ESM, as discussed in the next section.

I adopted a representation of metaknowledge based on the ORGMEM ABM (Ren et al., 2006). Metaknowledge is represented with the matrix ?? of size ?? × ??. Each row in this matrix represents a worker’s mental representation of their dependencies on others. The value $K _ { i j }$ represents worker ??’s knowledge about her dependency with worker ??. This value can be -1, 0, or 1, representing the lack of knowledge, knowledge of the absence of the dependency, and knowledge of the existence of the dependency, respectively. Two kinds of representation errors are possible: assuming a dependency exists when it does not and assuming a dependency does not exist when it does. In Figure 2, metaknowledge is represented with the cloud bubble as well as the matrix ??. Worker 3 lacks knowledge of her dependency on Worker 1 and lacks knowledge of her independence from Worker 2. Worker 1 knows about his dependency on Worker 2 but does not know about his dependency on Worker 3. Worker 2, on the other hand, has incorrect metaknowledge: she thinks she depends on Worker 3 when she does not, and she thinks she does not depend on Worker 1 when indeed she does.

Workers’ mental representations guide their decisions to interact with each other. Here I assume that worker incentives are aligned with the organization’s goal (Clement & Puranam, 2018). Workers would want to engage in interactions that promote the organization’s collective objective. These interactions are represented in the matrix ?? of size ?? × ??. The value $I _ { i j }$ represents worker ?? initiating an interaction with worker ??. In this example, Worker 1 initiates an interaction with Worker 2 based on his knowledge of their dependency. Similarly, Worker 2 initiates an interaction with Worker 3 based on her (incorrect) knowledge of their dependency.

Interactions have consequences in terms of promoting knowledge work when they are aligned with workers’ true dependencies. In this example, Workers 1 and 3 did not interact but it would have been advantageous if they had. In contrast, Workers 2 and 3 interacted when they should not have.<sup>2</sup> Thus, based on ?? and ??, I operationalize the organizational performance (p) as their alignment—that is, realized social interactions among co-dependent workers. One premise of ESM, and other novel organizational and workplace information technologies, is that it enables workers to learn about others by observing their interactions (improving K), which can improve p when workers know who to interact with (guiding I) (Leonardi, 2014).

![](/api/attachments/FDURDEKP/fulltext/images/bbcec1b9a167d6d6c6237cd11beae633ceb9f9c1c77bf06fdd1d218c1385ca08.jpg)  
Figure 3. Example of Simulation Dynamics Using ESM for Knowledge Work

## Computational Modeling of ESM

Building on the above model for organizational knowledge work, I consider an organization of ?? workers implementing ESM. Workers in the organization choose to adopt and use ESM or not. Workers’ adoption of ESM is represented with a binary vector ?? of size ??. A value of 1 represents use whereas a value of 0 represents non-use. ESM users both interact and observe others’ interactions. Furthermore, users reconsider their use preferences in each time step (Figure 3). Four other vectors of size ?? encode workers’ attitudes and behaviors. ?? is the transparency preference vector that encodes each worker’s transparency preference value. This value determines the maximum number of public interactions a worker can engage in through ESM in a particular time period. ?? is the interruption tolerance vector. Each worker’s value represents the maximum number of interruptions the worker can tolerate before leaving the ESM and abandoning its use. The number of interruptions in a particular period is stored in the vector ??. Finally, vector ?? holds information about workers who interacted publicly through ESM. This vector models the social media wall where those who interacted publicly can draw further interaction and engagement from other users in the future.

In addition to these vectors, the following matrices of size (?? × ??) were used as explained in the previous section (Figure 2). ?? is the task matrix, encoding workers’ true dependencies. This matrix remained unchanged throughout the simulation. ?? is the worker interaction matrix, representing workers’ interactions in each time period. ?? is the metaknowledge matrix, encoding each worker’s knowledge of their dependencies with other workers. This matrix was updated in each time period based on ESM observations and interactions.

Finally, to promote transparency and reproducibility (Burton-Jones et al., 2021), I implemented the model using the Python programming language, provided pseudo-code in the Appendix, and made all other source code files, data, and analyses available at both Github<sup>3</sup> and OSF.<sup>4</sup>

## Simulation Dynamics

The simulation matrices and vectors were initialized with the following parameters and procedures. W was initialized based on the worker dependency parameter that controls the density of the W matrix. K was initialized based on the initial metaknowledge accuracy parameter. This parameter controls the percentage of true dependencies (W) revealed in K. The non-revealed values were encoded as -1 to represent the lack of knowledge. I was initialized with a 0 (m×m) matrix. M initially encoded workers who chose to adopt ESM right after its implementation and was initialized by the initial ESM adoption variable, which reflects the organization’s capacity to create buy-in for using ESM after implementation. Later M changed based on users leaving the ESM throughout the simulation. The vectors T and U were initialized based on the worker transparency preference and worker interruption tolerance parameters, respectively. These two parameters were used as values of λ in Poisson processes and remained constant throughout the simulation. Higher values of the λ parameters translated to overall higher values of workers’ preferences and more variation in these values. The cost vector C represented the number of interruptions and is initially 0 (m). The vector A of interacting users was initialized with one randomly selected worker as 1 and the rest as zeroes, modeling the start of ESM with one welcome message to bootstrap the process of further interaction and engagement as detailed below (Figure 3). Finally, the number of periods in the simulation was controlled by the simulation time variable, representing the number of business days. In each time period (i.e., business day), the following process unfolds:

## Assessing ESM Use Behavior

ESM users evaluate whether to continue using ESM based on their use patterns in the previous time step. Two factors come under consideration: workers’ interruption tolerance ?? and the number of interruptions ?? they encountered during the last period. Each worker has an interruption threshold. If they are interrupted more than this threshold, they become non-users, $M = | M - ( C > U ) |$ . Here, the number of interruptions represents workers’ loss of utility due to ESM use.

## Observing ESM Interactions

ESM users (M = 1) observe the interactions of other users. The observed interactions depend on ESM interactivity and those who interacted recently (A = 1). These interactions depend on ESM interactivity. Specifically, ESM interactivity controls the percentage of prior interactions (A) that are disclosed for others to observe. I assume that ESM interactions reveal information that helps their observers assess their dependencies on the participants involved in these visible interactions. Observing these interactions results in both being interrupted and improving metaknowledge. I refer to such interruptions resulting from spending time and effort reading through prior interactions to learn from the useful ones as indirect interruptions.

Bearing the cost of indirect interruptions: ESM users update their cost in vector C based on the number of indirect interruptions. I assume that an indirect interruption has a similar cost to a direct interruption because both include the need to read and process a post. In the case of a direct interruption, the post is directed to the user whereas an indirect interruption requires the user to read through the newsfeed’s many posts.

Improving metaknowledge: Observing others’ interactions gives cues to the observer about their true dependency on those they observe. Thus, metaknowledge improves through the observations of others. Here, depending on ESM interactivity, a percentage of prior interactions are revealed to all users. Each user learns their true dependency on the observed workers (e.g., through reading these interactions and teasing out the skills and expertise of these workers). ESM users update their metaknowledge in vector K about others based on what they observe. Specifically, true dependency overrides existing metaknowledge, so observers adjust their metaknowledge about participants to be equal to the true dependencies: $K _ { i j } = W _ { i j } ,$ for i observers, j observed.

## Interacting with Others

Workers use ESM to interact with others. Specifically, users find potential interactions with other users (M = 1) who have posted on ESM in the past (A = 1). In addition, assuming that workers’ incentives for using ESM are aligned with the organization’s goal, users want to interact with others they know they depend on and avoid interacting with others they know they do not depend on (K = 1).<sup>5</sup> Given workers’ different preferences for transparency, not all potential interactions are realized. Each worker selects up to the worker’s T value from these potential interactions to interact with. These interactions, in turn, generate interruptions and leave digital exhaust.

Interrupting others: Given the purposeful nature of interactions, users targeted by interactions are inevitably interrupted, which increases their cost in vector C. For example, when these users get a notification and need to read the posted message, their work is directly interrupted.

Leaving digital exhaust: Interactions leave a digital exhaust by recording the interacting workers for the next step (updating their value in vector A).

Promoting work performance: Organizational performance resulting from using ESM is the extent to which interactions align with workers’ dependencies. In this step, I calculated the collective performance (p), which represents the collective organizational performance. Increasing this measure was the primary objective of the organization implementing ESM.

## Theoretical Validation

Following the guidelines for presenting computational modeling of organizations (Prietula, 2011), I draw on the model assumptions rooted in theories of organizational design, knowledge management, and social media affordances (Table 1).

## Experimental Setup

This study aimed to find out how organizations can design ESM to capitalize on its knowledge work benefits. I assumed that organizations want to see collective performance gains as a result of using ESM for knowledge work and that they can change the design features of ESM. This organizational outcome, however, might not be immediately seen, and its pursuit varies based on workers’ attitudes and individual knowledge gains. Therefore, I focused on how design features (interactivity and visibility) interact with workers’ attitudes (transparency preference and interruption tolerance) in driving knowledge work. Without a loss of generality, I assumed that ESM communication had public visibility, which is typical for many ESM tools (Leonardi, 2017), and focused on ESM interactivity as the main design feature that the organization can vary.

To answer the research question, I performed three experiments: the first focused on eliciting, under varying ESM interactivity settings, how ESM affordances and constraints drive knowledge work performance (main experiment); the second focused on validating and generalizing these findings across various configurations (extended experiment); and the third focused on relaxing some of the assumptions about workers’ behavior and metaknowledge (alternative assumptions). Collectively, the three experiments spanned 55,485 configurations resulting from varying simulation parameters (Table 2). To mitigate randomness due to differences in the initial conditions, I performed 10 independent simulation runs for each configuration, resulting in 554,850 simulation runs.

## Organizational Outcomes

I considered the following collective outcomes of using ESM, which have been examined in prior work. First, knowledge work performance is the primary outcome of interest and is calculated with the percentage of work dependencies (W) that are reflected in the realized social interactions through ESM (I). Second, ESM adoption is the percentage of knowledge workers using ESM. Finally, metaknowledge accuracy is the relative overlap between metaknowledge (K) and workers’ dependencies (W). This measure assumes that there are no self-dependencies.

## Main Experiment

The main experiment focused on explicating the overall system behavior and the mechanisms driving it. I simulated an organization of 100 workers for a total of 30 time periods. Because I was interested in understanding the role of ESM, I assumed a low initial metaknowledge accuracy. If metaknowledge is accurate, technologies like ESM may not bring about much change in knowledge work performance. I further assumed low worker dependencies to align with my focus on uncoordinated knowledge work, for which some unknown synergies exist among workers. I also assumed a high initial ESM adoption where the organization initially created strong buy-in for the ESM. The organization could vary ESM interactivity across a broad range of values. Finally, I focused on low and high configurations of workers’ attitudes. I used the values of 1 and 10 for transparency preference following recent surveys reporting an average of 4-5 posts on social media for business purposes (Hill, 2023). Regarding interruption tolerance, I chose the values of 25 and 75. Because I could not find data on ESM interruption tolerance, I used email as a benchmark. Recent surveys have indicated the average office worker receives about 120 emails per day (Templafy, 2020) and that most workers consider 50 emails the most they can handle (Heussner, 2010).

<table><tr><td colspan="3">Table 1. Model Assumptions and Theoretical Validation</td></tr><tr><td>Assumption</td><td>Model representation</td><td>Prior related work</td></tr><tr><td colspan="3">Knowledge work</td></tr><tr><td>Workers depend on each other</td><td>Work dependency matrix W</td><td>Residual and integrative dependencies in uncoordinated knowledge work are well documented (Baldwin &amp; Clark, 2000; Lindberg et al., 2016; Raveendran et al., 2016)</td></tr><tr><td>Workers&#x27; dependencies are not always known</td><td>Metaknowledge matrix K, takes values -1 for unknown</td><td>Studies of transactive memory systems show workers&#x27; incomplete knowledge of others improves through observation and interaction (Ren &amp; Argote, 2011; Wenger, 1998)</td></tr><tr><td>Workers&#x27; dependencies are symmetric and complementary</td><td>W is symmetricPerformance is the alignment between workers&#x27; dependencies and workers&#x27; interactions</td><td>Knowledge often sticks within the organization (von Hippel, 1994)Knowledge transfer results in competitive advantage (Argote &amp; Ingram, 2000)Organizational learning requires knowledge retention and knowledge transfer (Argote, 1999; Argote &amp; Miron-Spektor, 2011)</td></tr><tr><td>Organizational performance is promoted when interactions are aligned with workers&#x27; dependencies</td><td>Performance is the percentage of work dependencies that are reflected in the realized social interactions</td><td>Organizational structure drives organizational performance (Csaszar, 2012)Knowledge work performance results from the correspondence between the task structure and the social interaction structure (Clement &amp; Puranam, 2018)</td></tr><tr><td colspan="3">Enterprise social media affordances</td></tr><tr><td>Varying transparency preferences</td><td>The degree of interaction varies among ESM users</td><td>Social media use depends on a variety of factors including demographics (Levordashka &amp; Utz, 2016)Younger employees are more likely to actively use ESM (Cardon &amp; Marshall, 2015)</td></tr><tr><td>Visible communication</td><td>ESM communication is public</td><td>ESM communication is largely public (Stohl et al., 2016; Treem, 2015)Users are not sure of the accessibility of ESM content even when transparency settings are implemented (Gibbs et al., 2013)</td></tr><tr><td>ESM social interactions disclose metaknowledge</td><td>ESM users reflect their domains of expertise in their ESM communicationESM users develop social ties using ESM</td><td>ESM is a leaky channel of knowledge (Leonardi, 2017) that combines work-related and informal communication (Leonardi, 2014)ESM has multiple allocentric affordances that enable users to establish and maintain social ties with others (Karahanna et al., 2018)</td></tr><tr><td>Metaknowledge learning</td><td>ESM users observe ESM communication and enhance their mental representation K</td><td>Employees enhance their metaknowledge by observing ESM communication (Leonardi, 2015)</td></tr><tr><td colspan="3">Enterprise social media dynamics</td></tr><tr><td>The organization sets ESM features</td><td>Varying ESM interactivity values</td><td>It is possible to tweak the ESM design (Kane et al., 2014; Majchrzak et al., 2013)</td></tr><tr><td>Observe and build metaknowledge</td><td>ESM users learn from observing others&#x27; interactions, based on ESM interactivity</td><td>Ambient awareness enables all to learn about others; ESM is a leaky pipe (Leonardi, 2017)</td></tr><tr><td>Socialization</td><td>ESM users interact with other users by engaging with prior interactions</td><td>ESM provides extensive affordances for socialization (boyd &amp; Ellison, 2007; Kane et al., 2014; Karahanna et al., 2018)</td></tr><tr><td>Socialization is motivated by work dependency</td><td>ESM users interact with users with whom a knowledge of true dependency exists</td><td>Innovators search for knowledge by accessing their metaknowledge of the organization (Majchrzak et al., 2004).</td></tr><tr><td>Determine future ESM use</td><td>Users determine if they continue using ESM based on the number of interruptions and their tolerance to them</td><td>Workers determine their degree of use based on the benefits and concerns of using ESM (Gibbs et al., 2013)Workers curb visibility to their advantage (Van Osch &amp; Steinfield, 2018)</td></tr></table>

<table><tr><td colspan="4">Table 2. Simulation Configuration and Outcome Variables</td></tr><tr><td></td><td colspan="3">Parameter values</td></tr><tr><td>Simulation parameters</td><td>Main experiment</td><td>Extended experiment</td><td>Alternative assumptions</td></tr><tr><td>Organization size (m)</td><td>100</td><td>50, 100, 150</td><td>Same as main</td></tr><tr><td>Simulation time</td><td>30</td><td>10, 30, 90</td><td>Same as main</td></tr><tr><td>Initial metaknowledge accuracy</td><td>0.0, 0.1, 0.2</td><td>0.0, 0.1, 0.2, 0.3, 0.4</td><td>Same as main</td></tr><tr><td>Worker dependency</td><td>0.1, 0.2, 0.3</td><td>0.1, 0.2, 0.3, 0.4, 0.5</td><td>Same as main</td></tr><tr><td>Initial ESM adoption</td><td>0.8, 0.9, 1.0</td><td>0.6, 0.7, 0.8, 0.9, 1.0</td><td>Same as main</td></tr><tr><td>ESM interactivity</td><td>0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,0.9</td><td>0.1, 0.3, 0.5, 0.7, 0.9</td><td>Same as main</td></tr><tr><td>Worker interruption tolerance</td><td>25, 75</td><td>25, 75, 100</td><td>Same as main</td></tr><tr><td>Worker transparency preference</td><td>1,10</td><td>1, 10, 25</td><td>Same as main</td></tr><tr><td>Metaknowledge decay rate</td><td>0.0</td><td>Same as main</td><td>0.2, 0.8</td></tr><tr><td>Worker aspiration</td><td>1.0</td><td>Same as main</td><td>0.2, 0.8</td></tr><tr><td># of configurations</td><td>972</td><td>50,625</td><td>3,888</td></tr><tr><td># of runs</td><td>9,720</td><td>506,250</td><td>38,880</td></tr><tr><td>Outcome variables</td><td>Definition</td><td colspan="2">Operationalization</td></tr><tr><td>Performance</td><td>The percentage of work dependencies that are reflected in the realized social interactions</td><td colspan="2"> $\sum I \times W / \sum W$ </td></tr><tr><td>Adoption</td><td>The percentage of knowledge workers using the ESM</td><td colspan="2"> $\sum M/m$ </td></tr><tr><td>Metaknowledge accuracy</td><td>The relative overlap between metaknowledge (K) and workers&#x27; dependencies (W)</td><td colspan="2"> $((\sum K = W) - m)/(m - 1)^{2}$ </td></tr></table>

## Extended Experiment

The extended experiment focused on validating the results of the main experiment and generalizing them over a larger range of parameter values and configurations.

## Alternative Assumptions Experiment

I expanded the main analysis by relaxing two assumptions. In the main experiment, I assumed that workers always interact when it is advantageous to do so. In other words, the workers’ goals are always aligned with the organization’s goals (Clement & Puranam, 2018). I relaxed this assumption so that some workers may decide not to interact even when it is advantageous to do so and when interacting does not violate their transparency preference. This behavior is controlled by the worker aspiration parameter, which determines the percentage of potential advantageous interactions the worker realizes. Second, while I assumed that learned metaknowledge is retained permanently, people are forgetful and both knowledge and metaknowledge are prone to be forgotten (Ren et al., 2006). Thus, I relaxed this assumption by implementing a “forget step” in the simulation, where a percentage of learned metaknowledge was “forgotten” by being reset to -1. The percentage of forgotten metaknowledge in each step was controlled by the metaknowledge decay rate parameter.

## Results

Below, I visually present the findings. These plots show the average values across all runs in the selected configurations. The differences discussed in the text are all statistically significant at a p-value of < 0.05.

## Main Experiment

I examined the results from cross-sectional and longitudinal perspectives. In the cross-sectional examination, I examined the outcomes at the end of the simulation under various configurations of ESM interactivity and worker attitudes: interruption tolerance across Columns (a) and (b) and transparency preference with different line styles (Figure 4). The figure plots the average value of these outcomes under the selected configurations (i.e., for all other parameters). To ensure that the results were not an artifact of such averaging, I reproduced the figure for one selected configuration in the Appendix (Figure 7) and a similar pattern emerged. In the longitudinal analysis, I examine how the outcomes vary and unfold through the simulation (Figure 5). Like the crosssectional analysis, the values plotted are the averages over the runs in the remaining configurations. Similarly, the plot is reproduced with one configuration in the Appendix to ensure that the results are not artifacts of aggregating values across configurations (Figure 8).

## Cross-Sectional Analysis

Comparing the lines in Figure 4 across different values of worker interruption tolerance (i.e., across the left and right columns), I notice that when workers have a low interruption tolerance (left column), increased ESM interactivity results in lower performance (a) and lower adoption (c). This effect is shared across the two configurations of transparency tolerance. On the other hand, when workers have a high interruption tolerance (right column), increased ESM interactivity generally results in higher performance (b). In the case of a low transparency preference, performance steadily increases with ESM interactivity. Adoption is constant, although it drops slightly in high levels of ESM interactivity (d). In the case of a high transparency preference, increasing ESM interactivity increases performance up to a certain point, beyond which it declines steadily (b). Similarly, ESM adoption is almost constant up to that phase transition point. Beyond it, adoption declines rapidly (d). Interestingly, metaknowledge accuracy increases with ESM interactivity in all four configurations (e and f).

When comparing charts across transparency preferences (i.e., comparing the lines within the charts), I notice that a low transparency preference yields lower performance but higher adoption compared to a high transparency preference. Further, performance is less sensitive to changes in ESM interactivity in the low transparency configuration. Finally, and generally, a high transparency preference results in higher metaknowledge accuracy than a low transparency preference, and the gap further increases in the high interruption tolerance configuration.

In sum, examining performance across multiple configurations of ESM interactivity, worker interruption tolerances, and worker transparency preferences shows that the ESM effect on performance is contingent on worker attitudes and the degree of interactivity the ESM enables. Table 3 summarizes these contingent effects, which are not fully explained by metaknowledge as prior work suggests (e.g., Leonardi, 2014, 2015). The longitudinal analyses, discussed below, unpack what drives these contingent outcomes.

## Longitudinal Analysis

To dive deeper into the drivers of outcomes, I examined performance and adoption longitudinally as they unfolded during the simulation runs (Figure 5). The plots were created with ESM interactivity equal to 0.5 across the different configurations of worker interruption tolerance and worker transparency preference.

Low interruption tolerance (left column): Focusing on low interruption tolerance (left column), I notice an initial rise in performance followed by a quick decline (a) as well as a synchronous substantial decline in adoption (c). These corresponding declines in performance and adoption resulted from an increasing number of interruptions that ultimately exceeded most workers’ interruption tolerance (e). For the high transparency preference specifically, the average number of interruptions per worker was about 30, which exceeded the number most workers can tolerate (25). In turn, many workers left the ESM, and adoption declined sharply, dropping to 20%. In the case of the low transparency preference, the interruption average did not exceed 20 (e). While some workers left the ESM, adoption only decreased to about 40%, an outcome that resulted in higher performance for the low transparency preference compared to the high transparency preference (c).

Thus, a low transparency preference reduced the number of digital interruptions and enabled the ESM to function. Why? A plausible hypothesis based on prior work is that a low transparency preference may reduce the accuracy of metaknowledge and thus drive less interaction and interruptions. Levels of metaknowledge accuracy in the current study, however, are comparable across low and high transparency preferences (g). The reason for this similarity is that workers with a low transparency preference still often interact with others and reveal themselves; however, because interactions in ESM result from continuous engagement, fewer interactions provide fewer opportunities for others to engage with less transparent workers (e). In other words, although workers learn about others, they do not interact with them often.

To further explicate this phenomenon, I plot the ratio of interactions divided by all potential interactions that can be realized from the current state of metaknowledge (i). I refer to this measure as realized metaknowledge. While realized metaknowledge spikes to 50% for the high transparency preference, it tapers to less than 20% for the low transparency preference. On average, 10-20% of metaknowledge is “converted” into interactions for the low transparency preference compared to 40-50% for the high transparency preference (i).

Table 3. The Effect of Increasing ESM Interactivity on Knowledge Work Performance

<table><tr><td></td><td>Low interruption tolerance</td><td>High interruption tolerance</td></tr><tr><td>Low transparency preference</td><td>\ decreasing performance</td><td>/ increasing performance</td></tr><tr><td>High transparency preference</td><td>\ decreasing performance</td><td>∩ curvilinear</td></tr></table>

![](/api/attachments/FDURDEKP/fulltext/images/ff2bc577461fda9caf1a1f3bbb811f10f098c2cef121a1c3128e46fb58497fd7.jpg)

Figure 4. Outcomes at the End of Simulation Time under Various Configurations of ESM Interactivity and Worker Attitudes (Interruption Tolerance and Transparency Preference)

![](/api/attachments/FDURDEKP/fulltext/images/0ac8714bf4fe0dc1b5e7d86fe0016073613d875b6d958399d6eebe837bcba08a.jpg)

Figure 5. Outcomes throughout the Simulation under Various Configurations of ESM Interactivity and Worker Attitudes (Interruption Tolerance and Transparency Preference)

Thus, the analysis shows that what drives the low transparency configuration to be more resilient to the deleterious effect of interruptions resulting from ESM interactivity is the asymmetry between workers learning metaknowledge (g) and acting or being able to act on it (i). To further support this conclusion, I consider leakiness, or the percentage of ESM users who interacted in the previous time step (ΣA / ΣM), and thus invite others to interact with them (k). Less leakiness means that workers have fewer opportunities to interact with other workers, even if they know about them. Like its effect on realized metaknowledge, a low transparency preference almost halves the leakiness of ESM, thereby reducing the number of ESM-related interruptions and interactions. The temporarily reduced performance of the low transparency configuration “pays” out in the long term because ESM is less likely to see a massive exodus of members.

High interruption tolerance (right column): Focusing on high interruption tolerance (right column), I notice similar patterns in the first few time steps of the simulation. The main difference, however, is that the peak number of interruptions falls below the phase transition point for both high and low transparency preference configurations (f). Given that performance represents the interactions aligning with workers’ dependencies, more interactions are beneficial even if they generate more interruptions provided that these interruptions do not disturb the adoption of ESM. Accordingly, adoption does not drop significantly, and performance increases (d and b). In contrast to the left column, the low leakiness of the low transparency preference configuration results in lower performance throughout the simulation (b). Since interruptions do not threaten adoption, more interactions can also be beneficial. Here, a high transparency preference yields better performance simply because it generates more interactions. I notice similar patterns in realized metaknowledge and ESM leakiness (j and l) such that a high transparency preference results in more leakiness and more realized metaknowledge yet without the downside thanks to a high worker interruption tolerance.

In summary, a longitudinal examination of ESM performance and adoption shows that, as expected, metaknowledge accuracy increases over time, in turn driving increased performance. At the same time and given that organizational performance is measured as interactions aligning with workers’ dependencies, more interactions result in more interruptions. These interruptions come from two sources: indirect interruptions resulting from the digital exhaust of ESM that others need to read through and direct interruptions as workers are targeted for interactions. Because ESM interactions beget more interactions, a high transparency preference drives up both types of interruptions for everyone since each interaction invites up to m – 1 further interaction. Thus, in a way, workers with a low preference for transparency not only generate fewer interactions but also moderate the number of interactions of others who might have a higher preference for transparency. These workers do not, however, affect the capabilities of others to improve their metaknowledge since most workers still interact at times.

The asymmetric impact of some users to regulate everyone’s ability to realize their learned metaknowledge drives down interactions, performance, and interruptions. In the low interruption tolerance configuration, this is crucial for the success of ESM since a phase transition exists beyond which the platform is abandoned. Complementing the findings of the cross-sectional analysis, the findings of this longitudinal analysis suggest that metaknowledge accuracy alone does not drive ESM knowledge performance; rather, the effects of metaknowledge accuracy are contingent on users attitudes (Table 4).

## Extended Experiment

The extended experiment expanded the range of parameters and also varied the organization size and simulation time. To systematically compare the results across the main experiment and the extended experiment, I performed an ordinary least squares (OLS) regression analysis with performance as the dependent variable and the experiment parameters as independent variables. I further incorporated the interaction effects among ESM interactivity and worker attitudes.

Table 5 shows the regression analysis results. Overall, the coefficient sizes, signs, and statistical significance are consistent across the main and extended experiments. The only difference is the interaction effect between ESM interactivity and worker interruption tolerance. Finally, the extended experiment shows that performance tends to improve with simulation time (duration of ESM use) and decrease in larger organizations. This decrease is expected because larger organizations foster fewer chances for realizing useful interactions among workers.

Results of the extended analysis support generalized statements about ESM that complement the cross-sectional findings of the main experiment. Overall, (1) ESM interactivity degrades knowledge work performance, (2) interruption tolerance improves performance, (3) transparency preference improves performance, (4) interruption tolerance and transparency preferences are complements, and (5) transparency preference is less beneficial in high interactivity.

<table><tr><td colspan="3">Table 4. The Effect of Increased Metaknowledge Accuracy on ESM Knowledge Performance</td></tr><tr><td></td><td>Low metaknowledge accuracy</td><td>High metaknowledge accuracy</td></tr><tr><td>Low interruption tolerance</td><td>Lower performance</td><td>Contingent on transparency preference• Low transparency preference → higher performance• High transparency preference → lower performance</td></tr><tr><td>High interruption tolerance</td><td>Lower performance</td><td>Higher performance</td></tr></table>

<table><tr><td colspan="5">Table 5. OLS Regression to Compare the Main and Extended Experiments (differences shaded)</td></tr><tr><td></td><td>Main</td><td>Extended</td><td>Main with interaction effects</td><td>Extended with interaction effects</td></tr><tr><td>ESM interactivity</td><td>-0.1110***(0.0045)</td><td>-0.0701***(0.0009)</td><td>0.0742***(0.0092)</td><td>-0.0852***(0.0018)</td></tr><tr><td>Worker interruption tolerance</td><td>0.0021***(0.0000)</td><td>0.0025***(0.0000)</td><td>0.0007***(0.0001)</td><td>-0.0002***(0.0000)</td></tr><tr><td>Worker transparency preference</td><td>0.0106***(0.0003)</td><td>0.0086***(0.0000)</td><td>0.0053***(0.0005)</td><td>0.0006***(0.0001)</td></tr><tr><td>ESM interactivity × Worker interruption tolerance</td><td></td><td></td><td>-0.0010***(0.0002)</td><td>0.0014***(0.0000)</td></tr><tr><td>ESM Interactivity × Worker transparency preference</td><td></td><td></td><td>-0.0249***(0.0009)</td><td>-0.0067***(0.0001)</td></tr><tr><td>Worker interruption tolerance× Worker transparency preference</td><td></td><td></td><td>0.0004***(0.0000)</td><td>0.0002***(0.0000)</td></tr><tr><td>Initial metaknowledge accuracy</td><td>0.3526***(0.0144)</td><td>0.2404***(0.0017)</td><td>0.3526***(0.0133)</td><td>0.2404***(0.0016)</td></tr><tr><td>Worker dependency</td><td>-0.1920***(0.0155)</td><td>-0.1741***(0.0018)</td><td>-0.1920***(0.0143)</td><td>-0.1741***(0.0017)</td></tr><tr><td>Initial ESM adoption</td><td>0.0382***(0.0144)</td><td>0.2117***(0.0018)</td><td>0.0382***(0.0132)</td><td>0.2117***(0.0017)</td></tr><tr><td>Organization size</td><td></td><td>-0.0016***(0.0000)</td><td></td><td>-0.0016***(0.0000)</td></tr><tr><td>Simulation time</td><td></td><td>0.0001***(0.0000)</td><td></td><td>0.0001***(0.0000)</td></tr><tr><td>Intercept</td><td>-0.0691***(0.0134)</td><td>-0.0971***(0.0018)</td><td>-0.0636***(0.0129)</td><td>0.0467***(0.0017)</td></tr><tr><td>R-squared</td><td>0.3347</td><td>0.4101</td><td>0.4529</td><td>0.4747</td></tr><tr><td>R-squared adj.</td><td>0.3343</td><td>0.4101</td><td>0.4524</td><td>0.4746</td></tr><tr><td>N</td><td>9720</td><td>506250</td><td>9720</td><td>506250</td></tr></table>

Note: DV is Performance. Robust standard errors are in parentheses. \* $p < 0 . 1$ \*\* $p < 0 . 0 5 ,$ $^ { \star \star \star } p < 0 . 0 1$ 5

## Alternative Assumptions Experiment

Just as with the extended experiment, I used an OLS regression analysis to compare the main experiment with the alternative assumptions experiment (Table 6). Relaxing the two assumptions (that metaknowledge is always retained and that workers always interact when it is advantageous for the organization) revealed similar effects of the simulation parameters on performance. First, the coefficients of metaknowledge decay rate and worker aspiration are what I expected: forgetting decreases performance while aspiration increases it. Second, the main difference across the two experiments is that of ESM interactivity, where the coefficient changes from -0.1110\*\*\* to 0.0029\*\*\*. The overall new neutral effect of ESM interactivity (almost 0) shows that in some cases, ESM interactivity becomes less important in driving knowledge work performance. For example, when the metaknowledge decay rate is high or when worker aspiration is low, ESM use would be expected not to drive meaningful interactions among workers. I observed a similar change in the worker dependency parameter.

<table><tr><td colspan="3">Table 6. OLS Regression to Compare the Main and Alternative Assumption Experiments (differences shaded)</td></tr><tr><td></td><td>Main</td><td>Alternative assumptions</td></tr><tr><td>ESM interactivity</td><td>-0.1110*** (0.0045)</td><td>0.0029*** (0.0008)</td></tr><tr><td>Worker interruption tolerance</td><td>0.0021*** (0.0000)</td><td>0.0007*** (0.0000)</td></tr><tr><td>Worker transparency preference</td><td>0.0106*** (0.0003)</td><td>0.0030*** (0.0001)</td></tr><tr><td>Initial metaknowledge accuracy</td><td>0.3526*** (0.0144)</td><td>0.0822*** (0.0032)</td></tr><tr><td>Worker dependency</td><td>-0.1920*** (0.0155)</td><td>-0.0044 (0.0033)</td></tr><tr><td>Initial ESM adoption</td><td>0.0382*** (0.0144)</td><td>0.0200*** (0.0032)</td></tr><tr><td>Metaknowledge decay rate</td><td></td><td>-0.0139*** (0.0009)</td></tr><tr><td>Worker aspiration</td><td></td><td>0.0541*** (0.0009)</td></tr><tr><td>Intercept</td><td>-0.0691*** (0.0134)</td><td>-0.0778*** (0.0031)</td></tr><tr><td>R-squared</td><td>0.3347</td><td>0.2263</td></tr><tr><td>R-squared adj.</td><td>0.3343</td><td>0.2262</td></tr><tr><td>N</td><td>9720</td><td>38880</td></tr></table>

Note: DV is Performance. Robust standard errors are in parentheses. \* $p < 0 . 1$ \*\* $p < 0 . 0 5 ,$ $^ { \star \star \star } p < 0 . 0 1$

## Findings Summary and Empirical Validation

The results of this study validate prior findings about ESM in knowledge work environments, generalize these findings, and shed light on the mechanisms driving them. First, the results show that public interaction through ESM is generally advantageous for facilitating knowledge work and helping workers realize synergistic interactions in the workplace. This finding corresponds with the results of prior empirical studies investigating communication visibility and its role in promoting metaknowledge (Leonardi, 2014, 2015). In addition, the findings of the current study extend this prior work by showing that the benefits of ESM are contingent on both its design and users’ attitudes. Specifically, increased ESM interactivity promotes metaknowledge but negatively impacts knowledge work because of the increased number of interruptions (Addas & Pinsonneault, 2015; Chen & Karahanna, 2018), a finding that combines the research streams on metaknowledge and interruptions. In particular, performance increases with interactivity only when workers have a high interruption tolerance and a low transparency preference. Although no prior empirical work has examined this specific proposition, prior studies have reported on workarounds to curb transparency when ESM is highly interactive (Gibbs et al., 2013; Van Osch & Steinfield, 2018). This finding suggests that ESM may not be the best technology to support highly interactive communication (van Osch & Bulgurcu, 2020).

Second, while metaknowledge has been proposed as the mechanism that improves knowledge work through ESM (Leonardi, 2017; Wei et al., 2020), the results of this study show that performance is not simply a matter of improving metaknowledge accuracy. Metaknowledge can be a doubleedged sword because it promotes more interactions when workers are aware that these interactions are beneficial. What promotes knowledge and work performance is paradoxically both metaknowledge and the (in)ability to act on it. This is achieved through the asymmetric engagement of ESM such that many users decide not to interact with others even when they can and when it is advantageous to do so. In this case, the decision not to interact is driven by a low transparency preference given the ESM’s public visibility. Such a preference may result from privacy and accountability concerns (Sun et al., 2019; Treem, 2015) or can be just a personal communication preference (Hafermalz, 2020). The results show that workers with a low preference for transparency generate fewer interactions, and this negatively impacts the ability of everyone to realize their learned metaknowledge and drives down the number of interruptions. These findings relate to prior empirical work showing the negative effect of excessive socialization: in particular, ESM results in stratification when a group of chatty users takes the stage while others disengage (Bulgurcu et al., 2018). Moreover, when workers have a low interruption preference, the computational model predicts adoption of 20% to 40%, a finding that aligns with prior empirical work showing that ESM adoption ranges from 30% to 50% for employees and falls under 10% for executives (Charki et al., 2018; Li, 2015).

Third, the results show several contingencies and boundary conditions of ESM benefits, including the role of the work environment (worker dependency), the organization’s capacity to create initial buy-in (initial ESM adoption), and workers’ aspiration to use ESM to improve their work. Table 7 summarizes some of the findings of this study that have been empirically tested.

<table><tr><td colspan="2">Table 7. Summary of Findings and Empirical Validation</td></tr><tr><td>Finding</td><td>Similar empirical findings</td></tr><tr><td>ESM visibility promotes knowledge work performance</td><td>Leonardi, 2017; Wei et al., 2020</td></tr><tr><td>High ESM interactivity hurts knowledge work performance</td><td>Gibbs et al., 2013; Treem, 2015</td></tr><tr><td>High ESM interactivity hurts the adoption of ESM</td><td>Bulgurcu et al., 2018; Van Osch &amp; Steinfield, 2018</td></tr><tr><td>ESM adoption remains low when workers are concerned about interruptions</td><td>Charki et al., 2018; Li, 2015</td></tr><tr><td>Metaknowledge accuracy is a mechanism through which ESM use translates to knowledge work performance</td><td>Leonardi, 2014, 2015</td></tr></table>

## Discussion

In modern enterprises, IS play a pivotal role in organizing and coordinating work. The COVID-19 global pandemic highlighted the role of information technology in enabling distance knowledge work and creating virtual environments to replace face-to-face interactions. Implementations of workplace technologies are accelerating (Costello, 2019; Kane, 2017). The new wave of these technologies is characterized by richness and interactivity—and makes room for informal chatter and socialization (Leonardi & Vaast, 2017; Vaast & Kaganer, 2013). Modeled after public social media, ESM allows workers in an organization to interact, observe others’ communication, and archive and search that communication (Leonardi et al., 2013). Today, many organizations have embraced ESM to organize content, promote sharing, and foster socialization (Kane, 2015; Leonardi & Neeley, 2017).

The findings show that ESM outcomes are contingent on its design and users’ attitudes and provide insights into the mechanisms driving these outcomes. In particular, user attitudes regulate the outcome of ESM use. A low transparency preference makes it possible for ESM users to gain benefits while minimizing ESM-related interruptions. While some users opt to use ESM actively by posting and interacting, some will post and interact less while still benefiting from learning metaknowledge. Because users with a low transparency preference share the same metaknowledge learning benefits as highly transparent users, they regulate the number of digital interruptions for everyone. Their asymmetric engagement does not negatively affect the metaknowledge learning affordance but significantly reduces others’ social interaction affordance and the resulting interruptions. Finally, inevitably, some users will eventually decide to stop using ESM. These results help explain prior findings about the lackluster adoption of ESM (Charki et al., 2018; Liu & Bakici, 2019). Indeed, such low adoption (20%-40%) is not disadvantageous as long as it permits the system to sustain itself for the remaining users without triggering a mass exodus.

## Scholarly Contributions

This research started as a quest to reconcile extant findings about ESM in organizational knowledge work. Scholarly studies of ESM have examined its rich affordances for knowledge work (Leidner et al., 2018; Leonardi & Vaast, 2017; Majchrzak et al., 2013). Visibility seems to be the inescapable consequence of using modern digital technologies and IS in particular (Hernandez, 2020; Leonardi & Treem, 2020). In addition to visibility, the interactive nature of these systems has been considered both an advantage and a disadvantage in the literature. Within the context of knowledge work, a lot has been written about the role of visibility and interactivity in nurturing organizational memory in such a way that is useful for knowledge work (Leonardi, 2014; Sun et al., 2020; Treem et al., 2020; Treem & Leonardi, 2012). More recent studies have started to examine the downsides of visibility, mainly in light of accountability and privacy concerns (Gibbs et al., 2013; Stohl et al., 2016; Treem, 2015; Van Osch & Steinfield, 2018). At the same time, many studies have noted the drag on productivity caused by digital interruptions generated by modern technologies including workplace communication tools like email (Addas & Pinsonneault, 2015; Chen & Karahanna, 2018; Magni et al., 2022; Tams et al., 2020; Weinert et al., 2022).

One way to reconcile these two streams of work is to acknowledge that ESM, like other technologies, has pros and cons. A deeper attempt could take a contingency approach to examine the context in which ESM is implemented and used, such as the nature of work and norms in the organization. In a way, this study implements both of these approaches, focusing on the balance of advantages and disadvantages and taking into consideration multiple extant contingencies. In turn, this study goes a step further to examine how the outcomes of ESM use ultimately depend on knowledge workers’ attitudes and resulting use affordances. Contrary to common wisdom, a conservative attitude toward transparency can be advantageous, especially when ESM is highly interactive. The key to this finding is the interactive nature of ESM. Because each interaction begets more interactions, one user’s deliberate choice not to interact can have cascading effects. This study thus contributes to the notion of asymmetric engagement as the mechanism leading to this outcome.

Beyond ESM, asymmetric engagement translates to asymmetric system use in other IS. That is, system use is not a monolithic construct (Burton-Jones & Volkoff, 2017), and this study shows how the selective use of some features to actualize some affordances (e.g., metaknowledge learning) but not others (e.g., social interaction) can have important consequences on the outcomes of use for everyone. Going back to the example of Alice and Bob introduced in the “ESM and Knowledge Work” section, whereas Alice engaged with other coworkers through ESM, Bob used ESM asymmetrically by using different features and actualizing different affordances of metaknowledge learning and social interaction. Both Alice and Bob were suffering from increased digital interruptions. Contrary to the mainstream assumption that engagement is desirable, this work shows that Bob’s attitude toward engagement (his transparency preference) is desirable. Of course, it takes more than one worker to shape the collective outcome of using ESM. The model precisely shows the contingencies in which asymmetric engagement leads to better organizational-level outcomes in terms of knowledge work performance and user adoption.

The role of users’ attitudes in system use behavior is one of the bedrocks of IS (Davis, 1989). However, in contrast to older technologies, new information technologies are highly social and interactive. An individual’s decision to use a certain technology is no longer separable from a collective one. Such network effects have been well studied at the firm level and in system implementation literature (e.g., Lapointe & Rivard, 2005; Parker et al., 2017), as well as from an affordance perspective in large-scale collaborations (Ellison et al., 2015; Vaast et al., 2017). However, these effects have not been investigated in the context of understanding individual use outcomes in domains like organizational knowledge work. This study integrates the role of users’ attitudes and technology design considerations and contributes a multilevel model of ESM use and knowledge work outcomes. Use patterns of individual users are interconnected, affect each other, and collectively drive organization-level outcomes. Asymmetry in system use extends beyond the if-aspect of use: the decision of some users to use the system or not (e.g., Lapointe & Rivard, 2005). Use asymmetry resulting from the interaction of user attitudes with technology design also determines of the how-aspect of use: what affordances and constraints are actualized (Burton-Jones & Volkoff, 2017). As this study points out, IS use asymmetry plays an important role when considering the multilevel outcomes of IS implementations.

The IS field has pioneered studying user traits, perceptions, attitudes, and beliefs to understand IS adoption and use (Davis et al., 1989). Research on technology affordances expands on this early work and adds more richness to examining people’s behaviors when interacting with and using IS (Majchrzak & Markus, 2013). At the same time, affordances are more challenging to study because they are relational concepts and require careful attention to both the system’s design and user behaviors (Burton-Jones & Volkoff, 2017). This work shows how ABM can be used to study IS affordances by modeling user attitudes and behaviors and IS features. Such a method offers a broader range of possibilities for varying these factors and understanding their implications on both resulting affordances and constraints and downstream IS use outcomes. As this study demonstrates, this method can complement other research methods by generalizing them and uncovering their underlying mechanisms. This modeling technique also enables studying affordances before system implementation and use, which can be a useful tool for designing and theorizing an IS artifact (Gregor & Hevner, 2013).

Finally, this study contributes to organizational memory literature, where little attention has been paid to the dynamics of transactive memory systems (Zahra et al., 2020). For example, work that considers why group members contribute to the creation of metaknowledge is addressed in the IS literature by examining the role of IS in building organizational memory (e.g., Leonardi, 2015). In organizational memory research, meanwhile, the importance of informal socialization in the creation of metaknowledge for formal work is stressed (Leonardi, 2014). The current study extends both research streams by unpacking the spillover between the formal and informal processes through which transactive memory systems are created and used. Importantly, this work shows that transactive memory can not only be learned but also be used in informal contexts. Whereas prior work on organizational memory has found the accuracy of a transactive memory system advantageous for knowledge work (Argote & Guo, 2016), this work suggests that too much accuracy can be disadvantageous when collaborating workers have many opportunities to interact, for instance through pervasive IS like social media.

## Practical Implications

The findings show that ESM benefits are contingent upon the structure of knowledge work and that a wholesale approach to ESM implementation may thus not be the right strategy (Kane, 2015). Like prior work on knowledge management systems (Levine & Prietula, 2012; Sutanto et al., 2018), this work shows that predicting ESM outcomes requires understanding the complex relationship between the work environment, workers’ attitudes, and technology design.

High public newsletters original Twitter Visibility <sup>blogs</sup> modern Twitter group messaging premium newsletters social media wall email Low Interactivity High

Figure 6. Visibility and Interactivity as Two Design Features of Social Media and Other Communication Technologies

The findings suggest that the successful implementation of ESM needs to consider relevant users’ attitudes in the organization (Table 3 and Table 4). The design features of ESM (interactivity in the model) interact with users attitudes (transparency preference and interruption tolerance), and understanding their contingencies is crucial to realizing ESM’s promised benefits. The findings also emphasize management’s role in promoting ESM use, especially early on. At the same time, a lack of participation and engagement may not necessarily be a bad outcome as long as a certain level of participation is maintained. Further, ESM implementations should prioritize maintaining broad adoption over high engagement to succeed in the long run. Finally, the new notion of asymmetric engagement of ESM can help organizations identify user segments with different attitudes towards ESM and tailor the system design to their needs. In the context of ESM, this can be done by finetuning the visibility settings from the default public (Figure 6).

## Limitations and Future Work

As digital technologies become more enmeshed with personal and professional life, their effects broaden (Forman et al., 2014), and thus examining these effects becomes increasingly important. Documented negative aspects of digital technology include addiction (Turel et al., 2011; Vaghefi et al., 2017), the circulation of false and antisocial content (Cheng et al., 2015; Herring et al., 2002), and technostress (Tams et al., 2020). In researching the effect of ESM on performance, I assumed that workers are using ESM mindfully though I recognize that many of the above issues apply to ESM and other workplace technologies. Further work could examine the role of technology design in promoting workers’ well-being and work-life balance (Leidner & Tona, 2021).

Second, while I focused on uncoordinated knowledge work, ESM may be useful in coordinated knowledge work because workers can use ESM to complement the organization’s formal structures. Although the focus on uncoordinated work limits the external generalizability of findings to organizations with structural relationships not accounted for here (e.g., teams and workgroups), the agreement with findings from prior studies involving a mix of coordinated and uncoordinated work (Table 7) provides some confidence that the results, especially the negative outcomes of excessive socialization and transparency, generalize to coordinated knowledge work contexts (Gibbs et al., 2013; van Osch & Bulgurcu, 2020; Van Osch & Steinfield, 2018).

Third, this work focused on two affordances related to knowledge work: metaknowledge learning and social interaction. ESM has more affordances for organizations beyond knowledge work (Leonardi & Vaast, 2017; Majchrzak et al., 2013). Workers can strategize how to socialize to improve their work, for example, when they “decide where structural holes might exist, where an individual’s special expertise may fit, and where bridging ties may be productively developed” (Majchrzak et al., 2013, p. 44). Organizations can inform their hiring, promotion, and team formation decisions from knowledge learned through ESM, as well (Leidner et al., 2018).

Finally, this work focuses on interactivity as the overarching design feature, with communication set to public visibility. Additional communication design configurations could be considered (Karahanna et al., 2018; Kietzmann et al., 2011). For example, communication visibility can be tweaked from a public setting to a more limited one, including restricting visibility to a group (Van Osch & Steinfield, 2018) or to other users involved in the communication. Together, visibility and interactivity afford various modalities of communication (Figure 6). Future work could expand on the model developed in this work to incorporate both ESM communication interactivity and communication visibility as variables.

## Acknowledgments

I highly appreciate the engagement and support of the editors and reviewers during the review process. I am grateful for inputs from my colleagues Aaron Schecter, Amrit Tiwana, and Elena Karahanna, who provided friendly feedback on earlier versions of this work. I acknowledge financial support from the Terry-Sanford Research Award.

## References

Addas, S., & Pinsonneault, A. (2015). The many faces of information technology interruptions: A taxonomy and preliminary investigation of their performance effects. Information Systems Journal, 25(3), 231-273. https://doi.org/10.1111/isj.12064

Adjerid, I., Peer, E., & Acquisti, A. (2018). Beyond the privacy paradox: Objective versus relative risk in privacy decision making. MIS Quarterly, 42(2), 465-488. https://doi.org/ 10.25300/MISQ/2018/14316

Alavi, M., & Leidner, D. E. (2001). Review: Knowledge management and knowledge management systems: Conceptual foundations and research issues. MIS Quarterly, 25(1), 107-136.

Arazy, O., & Gellatly, I. (2012). Corporate wikis: The effects of owners’ motivation and behavior on group members’ engagement. Journal of Management Information Systems, 29(3), 87-116. https://doi.org/10.2753/MIS0742-1222290303

Argote, L. (1999). Organizational learning: Creating, retaining, and transferring knowledge. Springer.

Argote, L., & Guo, J. M. (2016). Routines and transactive memory systems: Creating, coordinating, retaining, and transferring knowledge in organizations. Research in Organizational Behavior, 36, 65-84. https://doi.org/10.1016/j.riob.2016.10.002

Argote, L., & Ingram, P. (2000). Knowledge transfer: A basis for competitive advantage in firms. Organizational Behavior and Human Decision Processes, 82(1), 150-169. https://doi.org/ 10.1006/obhd.2000.2893

Argote, L., & Miron-Spektor, E. (2011). Organizational learning: From experience to knowledge. Organization Science, 22(5), 1123-1137.

Baham, C., Kalgotra, P., Nasirpouri Shadbad, F., & Sharda, R. (2023). Generational differences in handling technology interruptions: a qualitative study. European Journal of Information Systems, 32(5)858-878. https://doi.org/10.1080 0960085X.2022.2070557

Baldwin, C. Y., & Clark, K. B. (2000). Design rules: The power of modularity (Vol. 1). MIT Press.

Bernstein, E. S. (2012). The transparency paradox: A role for privacy in organizational learning and operational control. Administrative Science Quarterly, 57(2), 181-216. https://doi. org/10.1177/0001839212453028

boyd, d., & Ellison, N. B. (2007). Social network sites: Definition, history, and scholarship. Journal of Computer Mediated Communication, 13(1), 210-230.

Brooks, S., & Califf, C. (2017). Social media-induced technostress: Its impact on the job performance of IT professionals and the moderating role of job characteristics. Computer Networks, 114, 143-153. https://doi.org/10.1016/j.comnet.2016.08.020

Brown, J. S., & Duguid, P. (1991). Organizational learning and communities-of-practice: Toward a unified view of working,

learning, and innovation. Organization Science, 2(1), 40-57. https://doi.org/10.1287/orsc.2.1.40

Brunswicker, S., Almirall, E., & Majchrzak, A. (2019). Optimizing and satisficing: The interplay between platform architecture and producers’ design strategies for platform performance. MIS Quarterly, 43(4). https://doi.org/10.25300/MISQ/2019/13561

Bulgurcu, B., Van Osch, W., & Kane, G. C. (2018). The rise of the promoters: User classes and contribution patterns in enterprise social media. Journal of Management Information Systems, 35(2), 610-646. https://doi.org/10.1080/07421222.2018.1451960

Burton-Jones, A., Boh, W. F., Oborn, E., & Padmanabhan, B. (2021). Editor’s comments: Advancing research transparency at MIS Quarterly: A pluralistic approach. MIS Quarterly, 45(2), iii-xviii.

Burton-Jones, A., & Volkoff, O. (2017). How can we develop contextualized theories of effective use? A demonstration in the context of community-care electronic health records. Information Systems Research, 28(3), 468-489.

Cardon, P. W., & Marshall, B. (2015). The hype and reality of social media use for work collaboration and team communication. International Journal of Business Communication, 52(3), 273- 293. https://doi.org/10.1177/2329488414525446

Charki, M. H., Boukef, N., & Harrison, S. (2018). Maximizing the impact of enterprise social media. MIT Sloan Management Review. https://sloanreview.mit.edu/article/maximizing-the-impact-ofenterprise-social-media/

Chen, A., & Karahanna, E. (2018). Life interrupted: The effects of technology-mediated work interruptions on work and nonwork outcomes. MIS Quarterly, 42(4), 1023-1042. https://doi.org/ 10.25300/MISQ/2018/13631

Cheng, J., Danescu-Niculescu-Mizil, C., & Leskovec, J. (2015). Antisocial behavior in online discussion communities. In Proceedings of the 9th International Conference on Web and Social Media, 61-70. http://www.aaai.org/ocs/index.php/ ICWSM/ICWSM15/paper/view/10469

Clement, J., & Puranam, P. (2018). Searching for structure: Formal organization design as a guide to network evolution. Management Science, 64(8), 3879-3895. https://doi.org/ 10.1287/mnsc.2017.2807

Coase, R. H. (1937). The nature of the firm. Economica, 4(16), 386-405.

Costello, K. (2019). Gartner says worldwide social software and collaboration revenue to nearly double by 2023. Gartner. https://www.gartner.com/en/newsroom/press-releases/09-24- 2019-gartner-says-worldwide-social-software-andcollaboration-revenue-to-nearly-double-by-2023

Csaszar, F. A. (2012). Organizational structure as a determinant of performance: Evidence from mutual funds. Strategic Management Journal, 33(6), 611-632. https://doi.org/10.1002 smj.1969

Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly, 13(3), 319-340.

Davis, F. D., Bagozzi, R. P., & Warshaw, P. R. (1989). User acceptance of computer technology: A comparison of two theoretical models. Management Science, 35(8), 982-1003.

De Alwis, S., Hernwall, P., & Adikaram, A. S. (2022). “It is ok to be interrupted; it is my job”: Perceptions on technology-mediated work-life boundary experiences; a sociomaterial analysis. Qualitative Research in Organizations and Management: An International Journal, 17(5), 108-134. https://doi.org/10.1108/ QROM-01-2021-2084

Ellison, N. B., Gibbs, J. L., & Weber, M. S. (2015). The use of enterprise social network sites for knowledge sharing in distributed organizations: The role of organizational affordances. American Behavioral Scientist, 59(1), 103-123. https://doi.org/ 10.1177/0002764214540510

Ethiraj, S. K., & Levinthal, D. (2004). Bounded rationality and the search for organizational architecture: An evolutionary perspective on the design of organizations and their evolvability. Administrative Science Quarterly, 49(3), 404-437.

Faraj, S., von Krogh, G., Monteiro, E., & Lakhani, K. R. (2016). Online community as space for knowledge flows. Information Systems Research, 27(4), 668-684. https://doi.org/10.1287/ isre.2016.0682

Faraj, S., & Xiao, Y. (2006). Coordination in fast-response organizations. Management Science, 52(8), 1155-1169.

Forman, C., King, J. L., & Lyytinen, K. (2014). Special section introduction: Information, technology, and the changing nature of work. Information Systems Research, 25(4), 789-795. https://doi.org/10.1287/isre.2014.0551

Fulk, J., & Yuan, Y. C. (2013). Location, motivation, and social capitalization via enterprise social networking. Journal of Computer-Mediated Communication, 19(1), 20-37. https://doi. org/10.1111/jcc4.12033

Gibbs, J. L., Rozaidi, N. A., & Eisenberg, J. (2013). Overcoming the “Ideology of Openness”: Probing the affordances of social media for organizational knowledge sharing. Journal of Computer-Mediated Communication, 19(1), 102-120. https://doi.org/ 10.1111/jcc4.12034

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. MIS Quarterly, 37(2), 337-355.

Haas, M. R., Criscuolo, P., & George, G. (2015). Which problems to solve? Online knowledge sharing and attention allocation in organizations. Academy of Management Journal, 58(3), 680- 711. https://doi.org/10.5465/amj.2013.0263

Hafermalz, E. (2021). Out of the panopticon and into exile: Visibility and control in distributed new culture organizations. Organization Studies, 42(5), 697-717. https://doi.org/10.1177/ 0170840620909962

Haki, K., Beese, J., Aier, S., & Winter, R. (2020). The evolution of information systems architecture: An agent-based simulation model. MIS Quarterly, 44(1), 155-184. https://doi.org/10.25300 MISQ/2020/14494

Hansen, M. T. (2002). Knowledge networks: Explaining effective knowledge sharing in multiunit companies. Organization Science, 13(3), 232-248.

Hernandez, K. (2020). Even if you’re working from home, your employer is still keeping track of your productivity—here’s what you need to know. CNBC. https://www.cnbc.com/2020/03/19/ when-working-from-home-employers-are-watching---hereswhat-to-know.html

Herring, S., Job-Sluder, K., Scheckler, R., & Barab, S. (2002). Searching for safety online: Managing “trolling” in a feminist forum. The Information Society, 18(5), 371-384. https://doi.org/ 10.1080/01972240290108186

Heussner, K. M. (2010). Tech stress: How many emails can you handle a day? ABC News. https://abcnews.go.com/Technology/ tech-stress-emails-handle-day/story?id=11201183

Hill, C. (2023). How often to post on social media. Sproutsocial. https://sproutsocial.com/insights/how-often-to-post-on-social-

media/

Jeppesen, L. B., & Lakhani, K. (2010). Marginality and problemsolving effectiveness in broadcast search. Organization Science, 21(5), 1016-1033. https://doi.org/10.1287/orsc.1090.0491

Kane, G. C. (2015). Enterprise social media: Current capabilities and future possibilities. MIS Quarterly Executive, 14(1), 1-15.

Kane, G. C. (2017). The evolutionary implications of social media for organizational knowledge management. Information and Organization, 27(1), 37-46. https://doi.org/10.1016/j.infoandorg. 2017.01.001

Kane, G. C., Alavi, M., Labianca, G. J., & Borgatti, S. P. (2014). What’s different about social media networks? A framework and research agenda. MIS Quarterly, 38(1), 275-304.

Karahanna, E., Xin Xu, S., Xu, Y., & Zhang, N. (A.). (2018). The needs-affordances-features perspective for the use of social media. MIS Quarterly, 42(3), 737-756. https://doi.org/10.25300 MISQ/2018/11492

Kietzmann, J. H., Hermkens, K., McCarthy, I. P., & Silvestre, B. S. (2011). Social media? Get serious! Understanding the functional building blocks of social media. Business Horizons, 54(3), 241- 251. https://doi.org/10.1016/j.bushor.2011.01.005

Laitinen, K., & Sivunen, A. (2021). Enablers of and constraints on employees’ information sharing on enterprise social media. Information Technology and People, 34(2), 642-665. https://doi. org/10.1108/ITP-04-2019-0186

Lapointe, L., & Rivard, S. (2005). A multilevel model of resistance to information technology implementation. MIS Quarterly, 29(3), 461-491.

Lazer, D., & Friedman, A. (2007). The network structure of exploration and exploitation. Administrative Science Quarterly, 52(4), 667-694.

Leidner, D. E., Gonzalez, E., & Koch, H. (2018). An affordance perspective of enterprise social media and organizational socialization. The Journal of Strategic Information Systems, 27(2), 117-138.

Leidner, D. E., & Tona, O. (2021). The CARE theory of dignity amid personal data digitalization. MIS Quarterly, 45(1), 343-370. https://doi.org/10.25300/MISQ/2021/15941

Leonardi, P. M. (2014). Social media, knowledge sharing, and innovation: Toward a theory of communication visibility. Information Systems Research, 25(4), 796-816. https://doi.org/ 10.1287/isre.2014.0536

Leonardi, P. M. (2015). Ambient awareness and knowledge acquisition: Using social media to learn “who knows what” and “who knows whom.” MIS Quarterly, 39(4), 747-762.

Leonardi, P. M. (2017). The social media revolution: Sharing and learning in the age of leaky knowledge. Information and Organization, 27(1), 47-59. https://doi.org/10.1016/j.infoandorg. 2017.01.004

Leonardi, P. M., Huysman, M., & Steinfield, C. (2013). Enterprise social media: Definition, history, and prospects for the study of social technologies in organizations. Journal of Computer-Mediated Communication, 19(1), 1-19. https://doi.org/10.1111/ jcc4.12029

Leonardi, P. M., & Neeley, T. (2017). What managers need to know about social tools. Harvard Business Review, 95(6), 118-126.

Leonardi, P. M., & Treem, J. W. (2020). Behavioral visibility: A new paradigm for organization studies in the age of digitization, digitalization, and datafication. Organization Studies, 41(12), 1601-1625. https://doi.org/10.1177/0170840620970728

Leonardi, P. M., & Vaast, E. (2017). Social media and their affordances for organizing: A review and agenda for research. Academy of Management Annals, 11(1), 150-188. https://doi.org/ 10.5465/annals.2015.0144

Levine, S. S., & Prietula, M. J. (2012). How knowledge transfer impacts performance: A multilevel model of benefits and liabilities. Organization Science, 23(6), 1748-1766. https://doi. org/10.1287/orsc.1110.0697

Levine, S. S., & Prietula, M. J. (2014). Performance open collaboration for innovation: Principles and performance. Organization Science, 25(5), 1414-1433. https://doi.org/ 10.1287/orsc.2013.0872

Levordashka, A., & Utz, S. (2016). Ambient awareness: From random noise to digital closeness in online social networks. Computers in Human Behavior, 60, 147-154. https://doi.org/ 10.1016/j.chb.2016.02.037

Li, C. (2015). Why no one uses the corporate social network. Harvard Business Review. https://hbr.org/2015/04/why-no-oneuses-the-corporate-social-network.

Lindberg, A., Berente, N., Gaskin, J., & Lyytinen, K. (2016). Coordinating interdependencies in online communities: A study of an open source software project. Information Systems Research, 27(4), 751-772. https://doi.org/10.1287/isre.2016.0673

Liu, Y., & Bakici, T. (2019). Enterprise social media usage: The motives and the moderating role of public social media experience. Computers in Human Behavior, 101, 163-172. https://doi.org/10.1016/j.chb.2019.07.029

Luqman, A., Talwar, S., Masood, A., & Dhir, A. (2021). Does enterprise social media use promote employee creativity and well-being? Journal of Business Research, 131, 40-54. https://doi.org/10.1016/j.jbusres.2021.03.051

Magni, M., Ahuja, M. K., & Trombini, C. (2022). Excessive mobile use and family-work conflict: A resource drain theory approach to examine their effects on productivity and well-being. Information Systems Research, 34(1), 253-274. https://doi.org 10.1287/isre.2022.1121

Majchrzak, A., Cooper, L. P., & Neece, O. E. (2004). Knowledge reuse for innovation. Management Science, 50(2), 174-188. https://doi.org/10.1287/mnsc.1030.0116

Majchrzak, A., Faraj, S., Kane, G. C., & Azad, B. (2013). The contradictory influence of social media affordances on online communal knowledge sharing. Journal of Computer-Mediated Communication, 19(1), 38-55. https://doi.org/10.1111/jcc4.12030

Majchrzak, A., & Markus, M. L. (2013). Technology affordances and constraints theory (of MIS). In E. H. Kessler (Ed.), Encyclopedia of management theory (pp. 832-836). SAGE. https://doi.org/10.4135/9781452276090.n256

March, J. G., & Simon, H. (1958). Organizations. Wiley.

Men, L. R., O’Neil, J., & Ewing, M. (2020). Examining the effects of internal social media usage on employee engagement. Public Relations Review, 46(2), Article 101880. https://doi.org/10.1016/ j.pubrev.2020.101880

Miller, J. H., & Page, S. E. (2007). Complex adaptive systems: An introduction to computational models of social life. Princeton University Press.

Moqbel, M., Bartelt, V. L., Topuz, K., & Gehrt, K. L. (2020). Enterprise social media: Combating turnover in businesses. Internet Research, 30(2), 591-610. https://doi.org/10.1108 INTR-09-2018-0439

Moran, R. E. (2020). Subscribing to transparency: Trust-building

within virtual newsrooms on Slack. Journalism Practice, 15(10), 1-17. https://doi.org/10.1080/17512786.2020.1778507

Nan, N. (2011). Capturing bottom-up information technology use processes: A complex adaptive systems model. MIS Quarterly, 35(2), 505-532. https://doi.org/10.2307/23044054

Newport, C. (2021). Email and Slack have locked us in a productivity paradox. Wired. https://www.wired.com/story/email-slackproductivity-paradox

Oh, W., Moon, J. Y., Hahn, J., & Kim, T. (2016). Research note— Leader influence on sustained participation in online collaborative work communities: A simulation-based approach. Information Systems Research, 27(2), 383-402. https://doi.org 10.1287/isre.2016.0632

Parker, G., Van Alstyne, M., & Jiang, X. (2017). Platform ecosystems: How developers invert the firm. MIS Quarterly, 41(1), 255-266. https://doi.org/10.25300/MISQ/2017/41.1.13

Posen, H. E., Keil, T., Kim, S., & Meissner, F. D. (2018). Renewing research on problemistic search: A review and research agenda. Academy of Management Annals, 12(1), 208-251. https://doi.org/ 10.5465/annals.2016.0018

Prietula, M. J. (2011). Thoughts on complexity and computational models. In B. McKelvey, P. Allen, & S. Maguire (Eds.), The Sage handbook of complexity and management (pp. 93-110). SAGE.

Puranam, P. (2018). The microstructure of organizations. Oxford University Press.

Puranam, P., Raveendran, M., & Knudsen, T. (2012). Organization design: The epistemic interdependence perspective. Academy of Management Review, 37(3), 419-440. https://doi.org/10.5465 amr.2010.0535

Raveendran, M., Puranam, P., & Warglien, M. (2016). Object salience in the division of labor: Experimental evidence. Management Science, 62(7), 2110-2128. https://doi.org/10.1287/ mnsc.2015.2216

Raveendran, M., Puranam, P., & Warglien, M. (2022). Division of labor through self-selection. Organization Science, 33(2), 810- 830. https://doi.org/10.1287/orsc.2021.1449

Ren, Y., & Argote, L. (2011). Transactive memory systems 1985— 2010: An integrative framework of key dimensions, antecedents, and consequences. The Academy of Management Annals, 5(1), 189-229.

Ren, Y., Carley, K. M., & Argote, L. (2006). The contingent effects of transactive memory: When is it more beneficial to know what others know? Management Science, 52(5), 671-682. https:// doi.org/10.1287/mnsc.1050.0496

Ren, Y., Kraut, R., & Kiesler, S. (2007). Applying common identity and bond theory to the design of online communities. Organization Studies, 28(3), 377-408.

Schelling, T. (1978). Micromotives and macrobehavior. Norton.

Seaver, N. (2019). Captivating algorithms: Recommender systems as traps. Journal of Material Culture, 24(4), 421-436. https://doi. org/10.1177/1359183518820366

Shore, J., Bernstein, E., & Lazer, D. (2015). Facts and figuring: An experimental investigation of network structure and performance in information and solution spaces. Organization Science, 26(5), 1432-1446. https://doi.org/10.1287/orsc.2015.0980

Siggelkow, N., & Rivkin, J. W. (2006). When exploration backfires: Unintended consequences of multilevel organizational search. Academy of Management Journal, 49(4), 779-795. https://doi.org/10.5465/AMJ.2006.22083053

Stohl, C., Stohl, M., & Leonardi, P. M. (2016). Managing opacity:

Information visibility and the paradox of transparency in the digital age. International Journal of Communication, 10(1), 123- 137.

Strong, D. M., Johnson, S. A., Tulu, B., Trudel, J., Volkoff, O., Pelletier, L. R., Bar-On, I., & Garber, L. (2014). A theory of organization-EHR affordance actualization. Journal of the Association for Information Systems, 15(2), 53-85.

Sturm, T., Gerlach, J., Pumplun, L., Mesbah, N., Peters, F., Tauchert, C., Nan, N., & Buxmann, P. (2021). Coordinating human and machine learning for effective organizational learning. MIS Quarterly, 45(3b), 1581-1602. https://doi.org/10.25300/MISQ 2021/16543

Sun, Y., Ding, Z., Zhang, Z. (Justin), & Gauthier, J. (2020). The sustainable positive effects of enterprise social media on employees: The visibility and vicarious learning lens. Sustainability, 12(7), 2855. https://doi.org/10.3390/su12072855

Sun, Y., Liu, Y., Zhang, J. Z., Fu, J., Hu, F., Xiang, Y., & Sun, Q. (2021). Dark side of enterprise social media usage: A literature review from the conflict-based perspective. International Journal of Information Management, 61(December), Article 102393. https://doi.org/10.1016/j.ijinfomgt.2021.102393

Sun, Y., Zhou, X., Jeyaraj, A., Shang, R.-A., & Hu, F. (2019). The impact of enterprise social media platforms on knowledge sharing: An affordance lens perspective. Journal of Enterprise Information Management, 32(2), 233-250. https://doi.org/ 10.1108/JEIM-10-2018-0232

Sutanto, J., Liu, Y., Grigore, M., & Lemmik, R. (2018). Does knowledge retrieval improve work efficiency? An investigation under multiple systems use. International Journal of Information Management, 40(June), 42-53. https://doi.org/10.1016/j.ijinfomgt. 2018.01.009

Tams, S., Ahuja, M., Thatcher, J., & Grover, V. (2020). Worker stress in the age of mobile technology: The combined effects of perceived interruption overload and worker control. Journal of Strategic Information Systems, 29(1), Article 101595. https://doi.org/10.1016/j.jsis.2020.101595

Templafy. (2020). How many emails are sent every day? Top email statistics for businesses. Templafy. https://www.templafy.com/ blog/how-many-emails-are-sent-every-day-top-email-statisticsyour-business-needs-to-know/

Treem, J. W. (2015). Social media as technologies of accountability: Explaining resistance to implementation within organizations. American Behavioral Scientist, 59(1), 53-74. https://doi.org/ 10.1177/0002764214540506

Treem, J. W., & Leonardi, P. M. (2012). Social media use in organizations: Exploring the affordances of visibility, editability, persistence, and association. Communication Yearbook, 36, 143-189.

Treem, J. W., Leonardi, P. M., & van den Hooff, B. (2020). Computermediated communication in the age of communication visibility. Journal of Computer-Mediated Communication, 25(1), 44-59. https://doi.org/10.1093/jcmc/zmz024

Turel, O., Serenko, A., & Giles, P. (2011). Integrating technology addiction and use: An empirical investigation of online auction users. MIS Quarterly, 35(4), 1043-1061.

Utz, S., & Levordashka, A. (2017). Knowledge networks in social media. In S. Schwan & U. Cress (Eds.), The psychology of digital learning: Constructing, exchanging, and acquiring knowledge with digital media (pp. 171-186). Springer. https://doi.org 10.1007/978-3-319-49077-9\_9

Vaast, E., & Kaganer, E. (2013). Social media affordances and

governance in the workplace: An examination of organizational policies. Journal of Computer-Mediated Communication, 19, 78- 101. https://doi.org/10.1111/jcc4.12032

Vaast, E., Safadi, H., Lapointe, L., & Negoita, B. (2017). Social media affordances for connective action: An examination of microblogging use during the Gulf of Mexico oil spill. MIS Quarterly, 41(4), 1179- 1205. https://doi.org/10.25300/MISQ/2017/41.4.08

Vaghefi, I., Lapointe, L., & Boudreau‐Pinsonneault, C. (2017). A typology of user liability to IT addiction. Information Systems Journal, 27(2), 125-169.

van Osch, W., & Bulgurcu, B. (2020). Idea generation in enterprise social media: Open versus closed groups and their network structures. Journal of Management Information Systems, 37(4), 904-932. https://doi.org/10.1080/07421222.2020.1831760

van Osch, W., & Steinfield, C. W. (2018). Strategic visibility in enterprise social media: Implications for network formation and boundary spanning. Journal of Management Information Systems, 35(2), 647-682. https://doi.org/10.1080/07421222. 2018.1451961

von Hippel, E. (1994). “Sticky information” and the locus of problem solving: Implications for innovation. Management Science, 40(4), 429-439. https://doi.org/10.1287/mnsc.40.4.429

Wegner, D. M. (1987). Transactive memory: A contemporary analysis of the group mind. In B. Mullen & G. R. Goethals (Eds.), Theories of group behavior (pp. 185-208). Springer.

Wei, C., Pitafi, A. H., Kanwal, S., Ali, A., & Ren, M. (2020). Improving employee agility using enterprise social media and digital fluency: Moderated mediation model. IEEE Access, 8, 68799-68810. https://doi.org/10.1109/ACCESS.2020.2983480

Weinert, C., Maier, C., Laumer, S., & Weitzel, T. (2022). Repeated IT interruption: Habituation and sensitization of user responses. Journal of Management Information Systems, 39(1), 187-217. https://doi.org/10.1080/07421222.2021.2023411

Wenger, E. (1998). Communities of practice: Learning, meaning, and identity. Cambridge University Press.

Wilensky, U., & Rand, W. (2015). An introduction to agent-based modeling: Modeling natural, social, and engineered complex systems with NetLogo. MIT Press.

Williamson, O. E. (1975). Markets and hierarchies. The Free Press.

Wu, T. (2017). The attention merchants: The epic scramble to get inside our heads. Vintage.

Zahra, S. A., Neubaum, D. O., & Hayton, J. (2020). What do we know about knowledge integration: Fusing micro-and macroorganizational perspectives. Academy of Management Annals, 14(1), 160-194. https://doi.org/10.5465/annals.2017.0093

Zeldes, N., Sward, D., & Louchheim, S. (2007). Infomania: Why we can’t afford to ignore it any longer. First Monday, 12(8). https://doi.org/10.5210/fm.v12i8.1973

## About the Author

Hani Safadi is an associate professor at the Terry College of Business, University of Georgia. He is interested in online communities, social media, health IT, information systems development, and the application of computational techniques in management research. His research has been published in outlets such as MIS Quarterly, where he serves as an associate editor, Information Systems Research, Organization Science, and Journal of Medical Internet Research.

## Appendix

## Simulation Pseudo Code

Given the simulation parameters:

\- organization\_size: number of workers in the organization

\- simulation\_time: number of simulation periods

\- initial\_metaknowledge\_accuracy: initial accuracy of metaknowledge

\- worker\_dependency: density of the work dependency matrix

\- initial\_esm\_adoption: percentage of workers using ESM at the beginning

\- esm\_interactivity: level of interaction among workers using ESM

worker\_interruption\_tolerance: workers' ability to tolerate interruptions

\- worker\_transparency\_preference: workers' preference for transparency

Initialize the simulation matrices and vectors:

\- W: the task matrix encoding workers' dependencies (density == organization\_size)

\- I: ESM interaction matrix (initially 0)

\- C: worker cost vector (initially 0)

\- K: metaknowledge matrix, or knowledge of W (initialized with initial\_metaknowledge\_accuracy)

\- M: ESM adoption and use vector (density == initial\_esm\_adoption)

\- T: transparency preference vector (with a random Poisson of λ ==

worker\_transparency\_preference)

\- U: interruption tolerance vector (with a random Poisson of λ ==

worker\_transparency\_preference)

\- A: ESM users who posted recently, initiated with one (welcome) message

While t < simulation\_time, progress simulation by one time-step where each worker:

If the worker is ESM user:

\- (1) Consider behavior change based on the last period

\- (2) Observe ESM interactions of the last period and learn new knowledge

\- (3) Initiate new interactions and learn new knowledge

(1) Consider behavior change

Identify ESM users whose interruption cost exceeds their tolerance (C > U)

\- Change these users to non-users by flipping their M (M = |M - (C > U)|)

Reset the cost vector C (set C = 0) for the next period

(2) Observe ESM interactions and learn new knowledge

\- Select a subset of prior interaction (A) based on esm\_interactivity

The observer learns true dependency with the observed workers (set K = W)

\- The observer bears the cost of observation by increasing C with # observations

(3) Initiate new interactions and learn new knowledge

Select potential interactions based on who posted in the last period (A == 1)

\- Select useful interactions where knowledge of dependency exists (K == 1)

\- Select up to T workers from potential interactions and interact with them (set I = 1)

Add the cost for direct interaction to the target cost (set C = C + 1)

\- Update ESM wall A to indicate which workers are interacting

![](/api/attachments/FDURDEKP/fulltext/images/0d2db9282fbebfffffe63c157c19e504306323ec0f02007b61e12a5868f9cbf8.jpg)  
Robustness Checks  
Figure 7. Performance at t = 30 for One Configuration. Initial Metaknowledge Accuracy = 0.0, Worker Dependency = 0.3, Initial ESM Adoption = 1.0

![](/api/attachments/FDURDEKP/fulltext/images/c6a09f7c57273222e9a974a5ad10c366b48ae5d54bdcea7156d6e726f86a02ee.jpg)
