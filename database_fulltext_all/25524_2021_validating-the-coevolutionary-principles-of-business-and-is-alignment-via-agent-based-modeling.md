---
otero_id: 25524
otero_key: "88S2MFZR"
title: "Validating the coevolutionary principles of business and IS alignment via agent-based modeling"
authors: "Mengmeng Zhang; Honghui Chen; Kalle Lyytinen"
year: "2021"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2020.1801360"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Validating the coevolutionary principles of business and IS alignment via agent-based modeling

Mengmeng Zhang , Honghui Chen & Kalle Lyytinen

To cite this article: Mengmeng Zhang , Honghui Chen & Kalle Lyytinen (2020): Validating the coevolutionary principles of business and IS alignment via agent-based modeling, European Journal of Information Systems, DOI: 10.1080/0960085X.2020.1801360

To link to this article: https://doi.org/10.1080/0960085X.2020.1801360

![](/api/attachments/88S2MFZR/fulltext/images/9f484045c66d501e8578cc607a242976070b0f46ba6b34ab60b838ff2a4be60d.jpg)

Published online: 09 Aug 2020.

![](/api/attachments/88S2MFZR/fulltext/images/2d4de66f9a3ab8249212ce8fa693b73d9f9c3c752bf1d3e1f29ff5e8204f3fa7.jpg)

Submit your article to this journal

![](/api/attachments/88S2MFZR/fulltext/images/6100868e10eb0e9bfd0b09762c9f6b85c1acc7e9b786431393802df715dead1a.jpg)

View related articles

![](/api/attachments/88S2MFZR/fulltext/images/6f8f577d7903bc2e3e8270186afc6c6882ed32ecccdd8507fae57d83c6abff5a.jpg)

View Crossmark data CrossMark

Check for updates

# Validating the coevolutionary principles of business and IS alignment via agent-based modeling

Mengmeng Zhang <sup>a,b</sup>, Honghui Chen<sup>a</sup> and Kalle Lyytinen<sup>b</sup>

<sup>a</sup>National University of Defense Technology, Changsha, China; <sup>b</sup>Department of Design and Innovation, Case Western Reserve University Weatherhead School of Management, Cleveland, OH, USA

## ABSTRACT

This paper provides theoretical and practical implications for the application of agent-based models (ABMs) to address the issue of coevolutionary business-IS alignment. The implications stem from the following arguments: (a) the alignment issue can be modelled by an ABM to describe the features of complex adaptive systems (CAS); (b) the coevolutionary principles of business and IS alignment stipulate individual behaviours and guide organisational order; (c) ABM development and experimentation ofer guidance to better explain how organisations control the alignment trajectory with coevolutionary principles. To extend the extant coevolutionary research on alignment, this paper develops an ABM for a hierarchical organisational structure and validates three coevolutionary principles.

ARTICLE HISTORY Received 2 October 2018 Accepted 21 July 2020

EDITOR Ojelanki Ngwenyama

ASSOCIATE EDITOR Kweku-Muata Osei-Bryson

KEYWORDS Coevolutionary principles; business-IS alignment; ABM; CAS

## 1. Introduction

Reviewing the research history of business-IS alignment, two distinct conceptualisations have grown from diferent areas of complexity. The first is situated in the region of order (Tanriverdi & Lim, 2017), where alignment exhibits high degrees of order and stability. A great deal of research has been conducted to establish such an alignment with multiple types (Gerow et al., 2015; Henderson & Venkatraman, 1993; Sabherwal et al., 2001), levels (Avison et al., 2004; Wagner & Weitzel, 2012), and dimensions (Chan & Reich, 2007; Schlosser et al., 2012). Although these viewpoints diferentiate between static and dynamic alignment in this region, they all view alignment as a balanced (Sabherwal et al., 2001), cause-and-efect deterministic logic (Benbya & McKelvey, 2006a). The second conceptualisation is situated in the region of emergent complexity, which represents the high diversity, adaptiveness, connectedness, and mutual dependency of firms (Page, 2009). The alignment in this region of complexity moves away from equilibrium and exhibits features such as emergence, nonlinearity, self-organisation, and coevolution (Tanriverdi & Lim, 2017). As a result, the performance advantages of firms start changing fast through the business and IS coevolution.

The second conceptualisation of alignment, which binds a higher level of complexity, goes beyond the traditional alignment assumptions and challenges of prior methods and models. A coevolutionary theory is deemed a superior way to address the research challenges (Benbya & McKelvey, 2006a; Peppard & Breu, 2003; Tanriverdi et al., 2010). This theory expresses alignment as a coevolutionary process that reconciles top-down rational control and bottom-up emergent adaptation (Benbya & McKelvey, 2006a). Beyond the intended planning of alignment, the coevolution approach seeks to coordinate business and IS through continuous adaptation and learning (Peppard & Breu, 2003). Through nearly two decades of research on business and IS coevolution, the literature has frequently studied the coevolutionary phenomenon (Simpson et al., 2016; Tanriverdi et al., 2010) and the coevolutionary conception (Benbya & McKelvey, 2006a; Peppard & Breu, 2003). Coevolutionary principles (e.g., mutual communication (Baker & Singh, 2015), knowledge sharing (Simpson et al., 2016), and modular design (Nassim & Robert, 2010)) have been introduced to control the alignment trajectories.

In our previous work, we have classified the extant coevolutionary research on alignment from several dimensions such as focus, framework (conceptual, theoretical, practical), level (strategic, operational, individual), method (non-empirical, qualitative, quantitative), and phase (sensing, sensemaking, improving, implementing) (Zhang, Chen, et al., 2019a). As a result, the extant coevolutionary research has abundant theoretical studies but inadequate practical solutions, such as empirical studies (Zhang, Chen, et al., 2019b). Additionally, ten coevolutionary principles were gathered and combined in a systems dynamic model (Zhang, Chen, et al., 2019a). The literature argued that the computational analysis of coevolutionary alignment is inadequate in validation and verification of coevolution principles. As Hedström and Ylikoski (2010) claimed, given the limitations of experimental methods and the complexity of social phenomena, computational analysis is important for this kind of endeavour, as this analysis allows the systematic exploration of the consequences of modelling assumptions and creates the possibility of modelling much more complex phenomena than was possible earlier. To date, coevolutionary principles have seldom been validated, and a long-term coevolutionary process has rarely been controlled and shaped by guiding principles (Amarilli et al., 2016, 2017). The validation and application of coevolutionary principles can help organisations such as firms, departments, or armies manage individual behaviours and maintain competitive advantages and agile superiority in their operation and evolution.

To extend the extant research from analysing and validating coevolutionary principles, this paper aims to test three important coevolutionary principles (mutual communication, knowledge sharing, and intelligence) via an agent-based model (ABM). All three principles have often been described in the literature (Allen & Varga, 2006; Tanriverdi & Lim, 2017) but have rarely been considered in the region of emergent complexity to explain their bottom-up impacts on holistic coevolution. An ABM is a microscale model that simulates the operations and interactions of multiple agents to create and predict the appearance of complex phenomena (Allen & Varga, 2006). As a bottom-up modelling method, an ABM describes behaviours at the individual level and predicts organisational behaviours as a cumulative outcome of individual behaviours (Nan & Tanriverdi, 2017). An ABM can thus efectively capture the emergent complexity of alignment. Scholars have claimed that ABMs are a suitable way to understand, validate, and further refine the theory implications of organisational coevolution (Benbya et al., 2006b; Tanriverdi & Lim, 2017; Vidgen & Wang, 2006). Therefore, the research question of this paper is: to pursue the coevolution of business and IS alignment, how can we validate the coevolutionary principles and then guide the individual-level behaviours with an ABM?

This paper helps to embrace social uncertainty of alignment and to explore coevolutionary landscape through emergent adapting. We first explain the above three principles and formalise them as four propositions. Then, we develop an ABM of a hierarchical organisational structure and verify the propositions. Layered organisations are commonly studied in the literature, such as governments, armies, and firms. This study aims to describe the coevolutionary landscape by theorising and modelling, how individual-level actions can induce turbulence in the firm-level strategy with bottom-up paths, how firm-level strategy can cultivate individual-level behaviours with top-down paths, and how these interaction paths can create nonlinear efects that impact the responses of a firm to dynamic changes (Nan & Tanriverdi, 2017).

These attempts help capture the issues of strategic planning and enterprise transformation in the coevolutionary process. Research in this context can facilitate further practical research.

## 2. Theoretical foundation

## 2.1. Business and IS alignment becomes a complex adaptive system

With the increasing complexity of alignment issues, we deem that the alignment of business and IS presents features of complex adaptive systems (CAS). As a branch of complexity science, CAS provide a way of thinking about systems as being composed of agents that interact with each other and behave according to defined rules (Onik et al., 2017). CAS act as a medium to produce the emergent complexity of an organisation. In general, CAS are nonlinear in that agent interactions make holistic behaviours more complex than can be predicted by summing individual behaviours (Tivnan, 2005). In addition, CAS present diversity because each agent is diferent from the others, and system performance depends on the other agents and the system itself (Tivnan, 2005). However, CAS can still be self-organised in that new behaviour patterns appear as consequences of agent interactions (Nan & Tanriverdi, 2017). Although posing between regions of order and chaos, CAS create order in the process of evolution (Benbya et al., 2006b). CAS theory has been widely applied to the domains of organisation (Holland, 1995; Tivnan, 2005) and IS (Benbya et al., 2006b).

Recently, scholars have argued that the alignment of business and IS displays the features of CAS (Tanriverdi et al., 2010; Vessey & Ward, 2013). This kind of alignment requires firms’ IS strategies, goals, and technologies to be harmonious with business strategies and goals, which is beneficial for firm performance. The firm’s alignment issue becomes unapproachable as firms face the challenges of “dancing rugged” markets (Tanriverdi et al., 2010), pervasive digital technologies (Yoo et al., 2012), and manifold interdependent relationships (Allen & Varga, 2006). Uncertainties and nonlinearity have been imposed on the alignment issue. For example, bottom-level informal behaviours, such as human inertia and unpredictable errors, make organisations hard to manage (Benbya & McKelvey, 2006a). Instead of pursuing a fixed alignment solution, potential deviations from intended plans need to be “captured” and “tamed” (Tanriverdi & Lim, 2017). Due to the IT’s subversive efectiveness, a temporary state of misalignment may also have beneficial efects (e.g., the IT ecosystem) (Baker & Singh, 2015). Faced with unpredictable changes, alignment order is more dificult to emerge than traditional alignment situations (Tanriverdi & Lim, 2017).

Coevolution is a principal order-creation mechanism (Lewin & Volberda, 1999; McKelvey, 1999). Whether for an external or internal organisation, coevolution aims to capture its fitness landscape and to seek dynamic suitable positions (Kaufman, 1993). The business and IS coevolution forms “a coevolutionary process that reconciles top-down ‘rational designs’ and bottom-up ‘emergent processes of coherently interrelating all components of the business/IS relationships in order to contribute to an organisation‘s performance over time” (Benbya & McKelvey, 2006a). Similar to the nature selection process (variation, selection, retention) (Cecez-Kecmanovic & Kay, 2001) and the dynamic capability process (sensing, seizing, transforming) (Teece, 2009, 2014), coevolution theory helps to illustrate how the coevolutionary process can shape the long-term alignment trajectory and create order with the help of coevolutionary principles.

## 2.2. Establishing complex adaptive systems with agent-based models

Exploring the holistic efects of CAS from individual behaviours is beneficial for capturing and controlling complex phenomena. In general, CAS theory relies on three key constructs to describe nonlinear causality: agents, interactions of agents, and an environment (Nan & Tanriverdi, 2017). Specifically, each agent exhibits its behaviour rules to continuously reconfigure itself according to what is rewarded by its surroundings (Nan & Tanriverdi, 2017). An ABM ofers exactly such a model, requiring each agent to behave in a stochastic, nonlinear manner, and possess a nonlinear capacity to adapt over time (Tivnan, 2005). As a “bottom-up” modelling method, an ABM describes emergent behaviours on the individual level (also called the bottom level in this paper), and all organisational behaviours can emerge as a cumulative outcome of individual behaviours. An ABM explains the actions and interactions of agents with a view towards assessing their efects on the system as a whole, such as in the Kaufman NK model (Kaufman, 1993).

Due to the ABM’s capability of analysing agent behaviours and environment, we claim that the coevolutionary principles can be symbolised by ABM, in order to express the alignment’s CAS characteristics. The bottom level of an organisation in this paper, in contrast to top-level strategy planning, refers to individual behaviours and interactions. As Peppard and Breu (2003) argued, the bottom level can be explained by the ways in which actors, individual people or groups of people interrelate with each other and their surroundings. Benbya and McKelvey (2006a) examined the interactions among individuals, between individuals and IS, and between individuals and the environment. Currently, the individual behaviours in the bottom level are dificult to capture and control, which becomes a key factor in misalignment. We deem that the development of an ABM can help explain bottom-level behaviours. For example, Merali et al. (2012) focuses on the interactions among IS agents to explain how coevolution at a higher level emerges and posits that the ABM represents an appropriate investigation for understanding bottom-level behaviours. Considering that organisations are flooded with the interactions of agents (Allen & Varga, 2006; Vessey & Ward, 2013), some scholars have claimed that ABMs are a suitable way to understand, validate, and further refine the theoretical ideas of organisational coevolution (Benbya et al., 2006b; Tanriverdi & Lim, 2017; Vidgen & Wang, 2006). Furthermore, an agent-based framework is proposed to define the mechanisms that are necessary for successful coevolution (Allen & Varga, 2006).

To the best of the authors’ knowledge, none of the extant coevolutionary studies of alignment have developed a specific ABM to explain bottomlevel behaviours and their impacts on corporate strategies. To validate prior theoretical outcomes, we develop an ABM of an assumed organisation and analyse three important coevolutionary principles (mutual communication, knowledge sharing, intelligence). These principles are widely discussed in the field of business and IS alignment. To verify the principles’ efects at a micro level, exterior changes from the environment can be absorbed by agents’ behaviour rules, and by tracing the impacts of the above principles on how individuals perform while tackling changes, we can gain insights into the overall coevolutionary processes.

The above theoretical foundation helps to form the research method of this paper. As Bygstad et al. (2016) argued, a stepwise research framework should involve the following contents, which are adopted to embody our research approach: (a) a description of events and issues that constitute the phenomenon of interest and corresponds to the business and IS alignment problem in this paper; (b) the identification of key entities, which involves alignment elements such as business strategy, business structure, IS strategy, and IS structure; (c) a theoretical redescription, which relates to the coevolution theory adopted to explain and analyse the alignment complexity; (d) the identification of candidate afordances, which refers to the coevolutionary principles in the pursuit of an alignment roadmap; (e) an analysis of the set of afordances and associated mechanisms, which can be mapped by four propositions and a validation approach with an ABM; and (f) an assessment of explanatory power, which refers to the performance measurement of our ABM. Overall, a proposition validation method will be conducted in combination with ABM development.

## 3. Proposition development

Given the CAS features of the alignment issue, the coevolutionary principles should be analysed from agents, interactions, and behaviour rules. We build propositions by mapping coevolutionary principles (mutual communication, knowledge sharing, and intelligence) to CAS concepts (a layered organisational structure composed of multilevel agents).

## 3.1. Mutual communication

Mutual communication uses interacting methods to exchange ideas, information, and knowledge among business and IS individuals (Luftman et al., 2017). There is ample evidence in the literature that mutual communication facilitates alignment (Chan & Reich, 2007; Reich & Benbasat, 2000; Wagner, 2014). As Peppard (2014) argued, mutual communication is beneficial for the development of relationships, knowledge sharing and collaboration. This principle is widely considered in the alignment fields of maturity measurement (Luftman, 2004), social alignment (Reich & Benbasat, 2000), and sustainable analysis (Wagner, 2014). Furthermore, mutual communication is also a beneficial way to embrace emergent complexity. Frequent mutual communication reduces human inertia (e.g., negative emotions due to threat perception, stickiness due to norms and value re-enactment), which can be caused by short-term success but would lead to suboptimal conditions in the long term (Besson & Rowe, 2012). With forehand knowledge stored through communications, agents may absorb changes easily. Moreover, diferent kinds of internal changes such as unpredictable deviations (Baker & Singh, 2015), unforeseen errors (Benbya & McKelvey, 2006a), or significant restrictions (Tanriverdi & Lim, 2017) can be sensed earlier through mutual communication activities. Consequently, clear communication motivates actors intending to align to do so smoothly (Baker & Singh, 2015). Nevertheless, scholars also claim that communication in which every aspect of the meaning is delivered to others is possible in theory but unlikely in practice due to the risk of clear sending and accurate receiving.

In this article, we take a hierarchical organisational structure as an illustrative example. This structure is assumed to have layers of presidents, business/IS managers, and business/IS actors. Generally, the structure can recognise and handle changes through reporting and commanding flows among layers (represented as the thick, solid arrow in Figure 1). Under this situation, the mutual communications between businesses and IS managers or businesses and IS actors may not be highly probable (Simpson et al., 2016). Inadequate mutual communication forces the organisation to depend greatly on the reporting and commanding flows to absorb changes, which may result in a slow coevolutionary process. According to the literature, strengthening mutual communication is beneficial for disseminating knowledge of changes in the organisation and thus implementing the coevolution of business and IS (see P1 in Figure 1).

![](/api/attachments/88S2MFZR/fulltext/images/b1b8083ad73780d644789c7912cde87d1aaaf8f020cd74eb3f60ce213d4700ea.jpg)  
Figure 1. Overview of our theoretical model.

Proposition 1 (P1): Enhancing the mutual communication of business and IS domains in an organisation embraces changes and helps to form coevolutionary processes.

## 3.2. Knowledge sharing

Currently, knowledge constitutes a valuable and intangible asset for creating and sustaining the competitive advantages of organisations (Cabrera & Cabrera, 2002). Knowledge sharing, which is more purposeful than mutual communication, aims to share information, skills, or expertise directionally. Similarly, this principle is emphasised by both traditional and coevolutionary alignment. Reich and Benbasat (2000) identified that knowledge sharing is an antecedent for long-term alignment. Kearns and Albert (2003) explained how knowledge sharing can create trust among people and develop competitive advantages for firms. Like the mutual communication principle, knowledge sharing helps actors sense unpredictable changes and execute transformation actions. Agents can build consensus about the shared reality of the organisation (Peppard & Breu, 2003; Simpson et al., 2016). However, knowledge sharing sometimes faces major challenges in practice. Some agents tend to resist sharing their knowledge with the rest of the organisation, or they display inertia due to previously formed knowledge (Ciborra & Patriota, 1998).

Generally, knowledge sharing activities represent two diferent contexts: interpersonal or databaseoriented (Bordia et al., 2006; Haas & Hansen, 2007). The interpersonal context refers to face-to-face communication, whereas the database context can occur when sharing knowledge through searching and inquiring. Concerning the illustrative organisational structure (Figure 1), knowledge sharing activities can occur in each separate domain or among diferent domains. They can not only help individuals obtain knowledge from databases (see P2 in Figure 1) but also help them convey knowledge on the basis of mutual communication (see P3 in Figure 1).

Proposition 2 (P2): Encouraging knowledge sharing activities through databases embraces changes and helps to form coevolutionary processes.

Proposition 3 (P3): Encouraging knowledge sharing activities through mutual communication embraces changes and helps to form coevolutionary processes.

## 3.3. Intelligence

Intelligence, which refers to individuals’ capability to proactively sense unpredictable cases with external information, is a necessary principle to capture uncertain situations (Peppard and Breu, 2003; Tanriverdi & Lim, 2017). For example, ubiquitous online media provide a new way to sense changes and learn knowledge instead of sharing in organisations. As Nan and Tanriverdi (2017) argued, enabling intelligence in a company helps to reduce its uncertainties and increase agility. Intelligence also helps increase internal complexity within companies and accelerate future change rates (Kandjani et al., 2014). This capability is one of the requisite conditions for a company to survive in turbulent environments (Tanriverdi & Lim, 2017). Each agent may acquire knowledge of markets with external information, help the whole organisation sense which product markets are rising and which ones are falling, and then adopt timely and feasible strategies.

The intelligence capability is represented as the learning activities of agents. Through continuous learning, agents can adapt their behaviours and sense future changes. This capability appears to be a bottomlevel behaviour. Through sensing external potential changes in advance and learning knowledge over time, an agent can expand its absorption ability (Pepparda nd Breu, 2003; Benbya & McKelvey, 2006a). This capability occurs in any domains of an organisation (see P4 in Figure 1).

Proposition 4 (P4): Encouraging intelligence capability through learning embraces changes and helps to form coevolutionary processes.

## 4. Quantitative theorisation via an ABM

The ABM development and analysis processes are conducted in this section. With regard to a design science problem, Hevner et al. (2004) argued that design science research requires the creation of an innovative, purposeful artefact for a specified problem domain, and thorough verifying and evaluating the artefact, in order to be presented efectively both to technology-oriented and management-oriented audiences.

With regard to ABM research, the ABM artefact in this paper should be developed with the following steps (Crooks et al., 2017): (a) model preparation, which defines the research question and determines the aim and purpose of the model, has been explained in detail in the sections above; (b) model design, which comprehensively plans the characteristics and behaviours of the agents, designs the environment, and defines the possible interactions, will be mainly discussed in this section; (c) model implementation, which refers to the modelling approaches, is executed by the Netlogo toolkit in this paper; (d) model validation, which refers to the process of ensuring that the model implementation corresponds to the model design, is conducted with a sensitivity analysis; and (e) model analysis and prediction, which completes the process of evaluating a model by testing it with data simulations, will be applied to the efort of validating the four propositions in this paper. The above steps will be discussed in an orderly manner.

## 4.1. ABM design

Our ABM design is based on a well-established approach that uses strings of digits to represent the behaviours of agents. Figure 2 depicts the key components of our model (environment, agents, behavioural rules, and performance outcomes), which are described in detail below.

## (1) Environment

Currently, organisations operate in a world that is increasingly permeated with digital technologies (Yoo et al., 2012). The pervasive digital innovations (e.g., component IT innovations or architectural IT innovations) are radically changing the nature of products and services (Gawer & Cusumano, 2014) and have toppled the traditional assumptions of partnerships, supply chains, and interfirm collaborations. For example, the IOS operating system drives convergent and generative IT trends in the literature (Yoo et al., 2012). Consequently, business and IT environments have become hyperturbulent and unpredictable. In such a dynamic environment, changes may occur in any layers of the organisation. For the sake of simplicity, multilevel changes are immediately added to our ABM. To explain the changes’ impacts on agents, we argue that a knowledge set (Joseph et al., 2014) is applied to afected agents. In this article, we assume that each change can bring 5 new knowledge points (one knowledge set). This knowledge set needs to be spread to and accepted by all of the agents and thus makes the business and IS domains coevolve.

## (2) Agents

We view all of the presidents, business/IS managers, and business/IS actors as agents. In this article, we assume that the illustrative organisation consists of 1 president, 10 business managers, 10 IS managers, 50 business actors, and 50 IS actors. Additionally, we divide the managers and actors of each domain into 3 groups, and the group of business or IS actors is in charge of its higher-level group of business or IS managers. To express changes, each agent’s attributes are characterised by a bundle of knowledge points that describe its understanding about the changes. For example, if one change occurred in the field of business actors, one of the agents of business actors may display its attributes as [1 1 1 1 1], while the attributes of other agents may be [0 0 0 0 0]. A value of 0 indicates that the agent has not grasped the knowledge point, while a value of 1 indicates the contrary. In our ABM, we assume there will be 5 changes that separately occur in the 5 fields. Therefore, the length of any agents’ attributes is 25. In terms of the above explanation, the numbers of agents, groups, changes, and the length of one knowledge set are not meant to represent reality in a strictly quantitative sense; instead, they are chosen for their efectiveness in generating theoretical insights (see sensitivity analysis in Table A1).

## (3) Behavioural rules

Behavioural rules control an agent’s search for the desired understanding of input changes by preserving or changing values of digits in its string (Nan & Tanriverdi, 2017). According to the propositions, we introduce 5 behavioural rules that could absorb the knowledge points of changes. The data presented in this section have also been validated through sensitivity analysis.

The first behavioural rule of any agent is its communications with other agents. In each simulating tick, an agent could select partners and, by communicating, pass one knowledge point he or she knows (digits that are 1) or receive one knowledge point his or her partners know. If ignoring P1 and P3, we believe that agents in the same group demonstrate a higher probability of knowledge exchange $( \mathtt { p } = 0 . 8 )$ than those in the same domain $( \mathtt { p } = 0 . 4 )$ and are even higher than those in diferent domains $( \mathtt { p } = 0 . 1 )$ . However, if the organisation encourages mutual communication or knowledge sharing activities, the probabilities of knowledge exchange among diferent domains will rise. Furthermore, we also consider the path dependency factor, which means that if two agents have successfully exchanged knowledge before, their probability of knowledge exchange for the next time will increase by 0.1; conversely, if they have failed to pass knowledge before, the corresponding probability will decrease by 0.1 for the next time.

![](/api/attachments/88S2MFZR/fulltext/images/779531829421d77d61e594b597bf73d792593b242fd1d46dcb3bf85a05d06563.jpg)  
Figure 2. Overview of our ABM design.

The second behavioural rule of an agent is obtaining knowledge points from databases. We assume that each agent’s initial probability of knowledge elicitation from databases is 0.1 in our ABM. If the organisation encourages knowledge sharing activities from databases (P2), this probability will rise. Similar to the first rule, every successful knowledge elicitation from databases will increase the agent’s probability by 0.1, while every failure to elicit knowledge will decrease it by 0.1.To obtain the knowledge proactively of other domains, there is another rule about learning from external information. With additional information, an agent is likely to sense the future actions caused by the other domains. We assume that each agent’s probability of knowledge acquisition by learning is 0.1, but this probability will rise if an organisation enhances the intelligence capability (P4). The knowledge acquisition probability will also be increased or decreased on the basis of the previous records.

The other two behavioural rules of agents are reporting action and commanding action. The reporting action refers to transferring the knowledge points of changes to an agent of the upper layer. The precondition of this action is that all of the agents in one group of the lower layer should have grasped the knowledge set of one change. For example, if a change occurred in the field of one business actor group, this group should report this change to one superior business manager only after this group has totally grasped the knowledge points of this change. The commanding action refers to the transfer of the knowledge points of changes to all of the agents in the lower layer. A precondition is that one change has been totally understood by the upper layer. It is worth noting that the acceptance rates of the commands are diferent with agents. In our ABM, the agent who has previously obtained knowledge points of one change could accept the corresponding command more easily than those agents who didn’t grasp the change.

## (4) Performance outcomes

Performance outcomes stem from evaluation metrics within the ABM. The performance complexity induced by multilevel changes may be captured by the overall distribution of knowledge strings in our ABM. To embody this performance, we introduce three indices from diferent viewpoints. The first is misalignment, which refers to the ineficiencies, dificulties, and inabilities concerning the alignment of business and IS (Carvalho & Sousa, 2008; Őri, 2014). Scholars have argued that organisations are continually sufering from misalignment while they address alignment achievement (Carvalho & Sousa, 2008; Chen et al., 2005; Őri, 2014). A misalignment state may damage overall performance advantages (Őri, 2014). From the viewpoint of knowledge, we view misalignment as the knowledge distance between the business domain and IS domain of the organisation, which is similar to the matching and moderation approach (De & Wim, 2015) in traditional alignment research. The formula of this metric is as follows, where n shows the number of changes and 60 is the number of agents in the business domain or IS domain.

$$
\text { Misalignment } = \sqrt {\sum_ {i = 1} ^ {5 n} ((\sum_ {j = 1} ^ {6 0} B _ {i j}) / 6 0 - (\sum_ {k = 1} ^ {6 0} I S _ {i k}) / 6 0) ^ {2}}\tag{1}
$$

However, according to the emergent complexity, displaying a misalignment does not always result in a decrease in organisational performance and occasionally may even result in the opposite (El Sawy et al., 2010). Scholars have started to question the fidelity of alignment in performance improvement (Liang et al., 2017; Tallon & Pinsonneault, 2011). Baker and Singh (2015) argued that practitioners should carefully consider the benefits that innovations ofer, even though they lead to a temporary misalignment. Therefore, we assume that the impact that changes (e.g., IS innovations) bring to an organisation can be displayed by a performance growth curve. This means that the competitive advantages of firms may increase initially and then stabilise with input innovations. A typical growth curve formula is adopted in our ABM (Zwietering et al., 1990). Moreover, we also consider the misalignment factor in this metric. We argue that the misalignment state may influence the growth curve and increase its uncertainty. This metric is called adaptation, which represents the adaptive capability of the organisation. According to formula 2, the numerator depicts a growth curve that depends on the number of changes (n), and T refers to the simulation time. Because the misalignment value may be 0, we consider an exponent in the denominator. With this formula, the changes can increase the performance while the misalignment may cause adverse results.

$$
A d a p t a t i o n = \left(\frac {5 n}{1 + 1 0 e ^ {- 0 . 5 T}}\right) / e ^ {\text { Misalignment }}\tag{2}
$$

We also consider the cost expended in the organisation’s evolutionary process. This factor should always be noticed when analysing the alignment issue (Kearns & Albert, 2003; Luftman, 2004). In our ABM, each kind of behavioural rule may produce a cost. Knowledge dissemination in the organisation comes at the expense of various forms of resource consumption, such as media, printing, and labour. Reasonably, we assume that the costs of the reporting and commanding actions (cost = 20) are higher than those of the other three rules. With regard to the communication rule, we believe that the communication cost in one group (cost = 1) is lower than that in one domain (cost = 2) and lower than that between diferent domains (cost = 4). Furthermore, the cost of sharing knowledge (cost = 1) is lower than the cost of learning knowledge (cost = 3). These data have been validated by sensitivity analysis. The overall cost can be acquired by continuously executing the behavioural rules. Considering the cost metric, the organisation may restrict its adoption of the three principles.

In general, the alignment issue could be defined in terms of strategic alignment, structural alignment, social alignment, and so on. Social alignment refers to the mutual understanding of business and IT executives and their commitment to plans, objectives and missions. According to the above modelling components, our ABM describes the social aspect of business and IS alignment, which is the most unapproachable and unpredictable factor in the long run of organisational evolution. Our ABM aims to capture individual behaviours and explore how to control these behaviours to reach a superior coevolutionary process.

## 4.2. ABM implementation

All of the agents were created at the beginning of a simulation session. Their group numbers were randomly determined. Their attributes were also initialised according to the input changes. A simulation session may take hundreds of clock ticks until the organisation totally absorbs the input changes. Each clock tick includes two specific steps. First, each agent has an opportunity to pursue knowledge points by randomly executing the first three behavioural rules. Based on the behaviour rules, this step mainly determined the probabilities of knowledge acquisition of the agents. Second, the organisation determined whether to execute the reporting actions or commanding actions. Three performance metrics were calculated at the end of each clock tick. As our ABM ran through a sequence of clock ticks, we obtained a time path of performance ranking changes. The three kinds of time paths help us analyse the performance diferences under various conditions. The ABM was implemented using the NetLogo toolkit (Nan & Tanriverdi, 2017).

Table 1. Experimental treatments (each condition includes 30 simulation sessions).

<table><tr><td>Proposition</td><td>Experimental treatment</td></tr><tr><td>None</td><td>1 condition:The probability of knowledge transferring through mutual communication: 0.1The probability of knowledge eliciting through databases: 0.1The probability of knowledge transferring through knowledge sharing on the basis of mutual communication: 0The probability of knowledge eliciting through learning: 0.1</td></tr><tr><td>P1</td><td>5 conditions:The probability of knowledge transferring through mutual communication: increases from 0.2 to 0.6The other kinds of probabilities are the same with condition “None”</td></tr><tr><td>P2</td><td>9 conditions:The probability of knowledge eliciting through databases: increases from 0.2 to 1.0The other kinds of probabilities are the same with condition “None”</td></tr><tr><td>P3</td><td>5 conditions:The probability of knowledge transferring through knowledge sharing on the basis of mutual communication: increases from 0.6 to 1.0The other kinds of probabilities are the same with condition “None”</td></tr><tr><td>P4</td><td>9 conditions:The probability of knowledge eliciting through learning: increases from 0.2 to 1.0The other kinds of probabilities are the same with condition “None”</td></tr></table>

## 4.3. ABM validation and proposition analysis

According to the literature, validating an ABM is always dificult but necessary (Fioretti, 2013). Before subjecting our ABM design to proposition testing, we conducted sensitivity tests of the simulation results (see Appendix A for details). The sensitivity tests focus on the diferent numbers of agents, layers, probabilities, costs, and so on to analyse the holistic efects of alignment coevolution. Once we gained suficient confidence in the validity of our model, we performed diferent experimental conditions of the theoretical model. Table 1 provides an overview of the experimental treatments implemented in our ABM. To validate the propositions, we adjust the diferent kinds of probabilities of knowledge exchange. Because P3 is based on P1, we assume that the knowledge sharing probability of P3 is higher than that of P1. We conduct the simulations with these conditions.

## 5. Findings

After simulating each condition 30 times, the average time path of misalignment, adaptation, and cost under each condition can be drawn. Comparing the graph of each condition with that of the “None” situation, the overall trends (e.g., peak value, stability, time returning to alignment) can be analysed with the data, which provides evidence for the propositions of this article.

## 5.1. Mutual communication (P1)

Figure 3 shows the time paths of varied conditions (case “None” and critical conditions of P1) resulting from the ABM experiment. According to the left part of Figure 3, the peak value of misalignment decreases and the overall trend becomes steady when increasing the mutual communication probability. These results illustrate that a higher probability of mutual communication helps the business/IS domains acquire knowledge points from the IS/business domains. Given the shared knowledge points, the business/IS domains are more likely to accept the commands from the upper layer. As a result, the time for returning to alignment comes earlier. For example, IS actors may communicate with business actors and acquire the knowledge points that business changes have brought, which prompts IS actors to accept the commands that IS managers may order to receive business changes. The adaptation curve exhibits similar results. The right part of Figure 3 explains that the adaptation values are continuously afected by the misalignment level. The growth rate of the adaptation is diferent based on the varied conditions. The rates here increase according to the rise in the mutual communication probability.

![](/api/attachments/88S2MFZR/fulltext/images/7a2162462e8488fe5777b9205a90766e1627ffa6e64280f1d268a479a04d9bf4.jpg)

Figure 4 shows the overall costs of varied conditions. The costs associated with the 5 conditions of P1 are higher than that of condition “None”, indicating that an extra cost is produced by executing mutual communication activities. At the same time, the extra cost is narrowed when increasing the probability of P1. This can be explained by reducing the commanding cost. Taking the business changes as an example, if the majority of IS actors have obtained the knowledge points of business changes by mutual communication, these IS actors are likely to easily accept the orders of the upper layer, which reduces the commanding times and the commanding cost. According to the above explanation, we argue that P1 is partly supported by our simulation results.

![](/api/attachments/88S2MFZR/fulltext/images/bf844c5ad290dd0972619b37a6ee8ef6b2df730f63eae3012f40d4f608bb6c07.jpg)  
Figure 3. Performance trends associated with diferent probabilities of P1.

![](/api/attachments/88S2MFZR/fulltext/images/f50a60158e11abc97377bf6e65c0300246cdb1cbbf17dca6bf7f877adfe1b2d8.jpg)  
Figure 4. Overall costs associated with the diferent probabilities under each proposition.

## 5.2. Knowledge sharing through databases (P2)

Figure 5 displays the evolutionary trends of misalignment and adaptation with varied P2 conditions. According to the misalignment graph, it is obvious that a higher probability of knowledge sharing produces a larger peak value and a more drastic evolutionary trajectory. This is because the knowledge sharing activities in the domain where changes occurred are more intensive than those in the other domain, which increases the knowledge distance. Furthermore, a higher knowledge sharing probability tends to cause the misalignment curve to fall faster, and the duration time of returning to alignment state comes earlier. This can be explained in the following example. If one business change occurs on the part of business managers, this group of actors may share the knowledge points of this change through communicating and knowledge sharing activities. At the same time, this group of actors may report this business change earlier to the president layer. When the president layer requires IS managers to accept this change, the majority of IS managers may understand the business change quickly, and the organisation may thus exhibit a sudden decrease in its overall misalignment state. The results can also be reflected in the adaptation curve. According to the right part of Figure $^ { 5 , }$ a higher probability of knowledge sharing displays slower adaptability early but faster adaptability later.

![](/api/attachments/88S2MFZR/fulltext/images/ed97c4fc88eb36902b85eacd57e98b8b171293c2cc853134d98eb573460903a8.jpg)  
Figure 5. Performance trends associated with diferent probabilities of P2.

![](/api/attachments/88S2MFZR/fulltext/images/ba9d83a5b0c917d074c31ab0d3a09d46d98775c21c7d1db158502b336cddc737.jpg)  
Figure 6. Performance trends associated with diferent probabilities of P3.

From the perspective of cost, the overall costs of the P2 conditions are less than the costs of condition “None” and become less when the knowledge sharing probability increases. Although sharing knowledge from databases produces an extra cost, we argue that the lower layer where changes have occurred may report the changes to the upper layer quickly, thus indirectly reducing further communication costs and commanding costs. Overall, P2 is partly supported by our simulation results.

## 5.3. Knowledge sharing through mutual communication (P3)

According to Figure 6, the overall trends of P3 are similar to those of P1. By directing knowledge sharing about mutual communication activities, more knowledge points can be sent and received among domains. As a result, the misalignment curve becomes smoother with increasing probability. At the same time, the rate of adaptation becomes faster, and the time needed to achieve the fitness value comes earlier. According to the results, these trends illustrate that knowledge sharing activities facilitate firm performance.

![](/api/attachments/88S2MFZR/fulltext/images/6bdca84775324237f5dda46d098d7c9f5d01dde2c544090bc18562efc5b2e38c.jpg)

![](/api/attachments/88S2MFZR/fulltext/images/bfa3198602805ba40a55b6ecd0f6f7edf12b6833687cc24e423c3d4cc6adbaa9.jpg)

Furthermore, the overall costs of P3 are less than that of condition “None”. Similar to P1, the reduction in commanding costs helps to explain this result. Generally, the upper layer may dictate new decisions to mitigate the changes that impact the lower layer. Due to inertia or other unpredictable situations (Mitleton-Kelly & Papaefthimiou, 2000; Benbya, McKelvey & Jacucci, 2006b), these decisions may be accepted by the lower layer after receiving multiple commandments (Simpson et al., 2016), which produce a high commanding cost. However, according to the above explanation, the lower layer may have obtained forehand knowledge from prior knowledge sharing between lower layers. Consequently, the overall commanding cost would be reduced due to the few command attempts. In short, P3 is entirely supported by our simulation results.

## 5.4. Intelligence (P4)

Intelligence capability refers to the exploration actions of agents with external information. This capability forces the agents of the business/IS domain to learn the knowledge points of the IS/business domain in advance. According to the misalignment curve in Figure 7, a higher learning probability results in a larger misalignment and an earlier alignment time. This illustrates that the speed of sharing knowledge in the domain that is changing falls behind the speed of learning knowledge in the other domain. A misalignment state may thus be caused by overlearning, which consequently produces slower adaptability in the early evolutionary stage. However, learning activities help the lower layers receive commands from the upper layers. The whole organisation may adapt to the input changes earlier.

![](/api/attachments/88S2MFZR/fulltext/images/aff25bf3b2bfbb6004150bb82c7191105786ca82cb3bb324fbdeed4fa440a246.jpg)  
Figure 7. Performance trends associated with diferent probabilities of P4.

Similarly, by producing extra learning costs but reducing the further commanding costs in the evolutionary process, the overall cost of P4 represents a descending trend with increasing learning probability. Furthermore, it is obvious that the overall costs of P2 are always less than those of P4 (see Figure 4), which may be because the learning cost of each agent is larger than its knowledge-sharing cost. According to the results of three metrics, we argue that P4 can partly support the coevolution of business and IS.

## 5.5. Comparative analysis

To integrate the above analysis, we select the middle probabilities of each proposition and compare their performance outcomes with the “None” situation. According to the overall evolutionary time, we identify that all of the propositions are positive in achieving the coevolution of business and IS. In Figure 8, P2 and P4 are likely to represent slower reactions in the early stage. Conversely, P1 and P3 are relatively mild and easy to control, although P1 tends to produce a higher cost. Considering all three metrics, we argue that P3 performs more persuasively than the other three propositions.

## 6. Discussions

In this section, we return to our research question: in order to pursue the coevolution of business and IS alignment, how can we validate the coevolutionary principles and then guide the individual level behaviours with an ABM? An organisational ABM has been developed to explore the combination of topdown management and bottom-up control through validating coevolutionary principles. By answering the research question, we provide two contributions.

The first is theoretical and concerns how ABM testing improves our understanding of coevolutionary principles. The ABM exhibits top-down planning (reporting and commanding actions) and bottom-up adaptation (three principles), which provides guidance as to how organisations can control the coevolution trajectory, create alignment orders, and survive in the potentially irreversible discontinuities of markets. Four propositions based on three coevolutionary principles are proposed and validated in the ABM. The findings are listed as follows: P1, P2, and P4 are partly supported by our simulation results, while P3 is entirely supported by our simulation results. We have identified that all of the principles have positive efects on the coevolution of business and IS, although several exhibit higher costs or slower adaptability. These findings explain the advantages of the above three principles and how the organisation can apply principles in pursuing business and IS alignment. Furthermore, this paper studies coevolutionary research from a quantitative view, which helps improve the precision of prior theoretical development.

![](/api/attachments/88S2MFZR/fulltext/images/25a9ebbf08c9e8c68cb035f66eebe4b979acc5492202908742ecd28330ab8f32.jpg)

Second, the computational analysis of our ABM paves a practical way of alignment application. ABM exploration can be applied to both further theoretical research (e.g., the validation of other principles) and practical applications (e.g., the application of principles). Stakeholders of organisations, such as CEOs, CIOs, and enterprise architects, should pay more attention to individual behaviours with regard to coevolutionary principles, an approach that can complement traditional top-down planning strategies. The findings and implications can be applied to various kinds of organisations, such as firms, governments, and armies.

Our ABM still presents limitations. First, according to the literature of coevolution, several other coevolutionary principles (e.g., modularity) need to be validated. Taking modularity as an example, knowledge points may be composed as a module that can be sent or received at the same time, due to the cohesion of knowledge points. Second, synergistic or conflicting relationships may exist between the changes, which may influence the compositions of agent attributes and the dissemination of knowledge points in our model. Third, our ABM needs to consider other performance metrics (e.g., alignment maturity) or other alignment dimensions (e.g., structural alignment) when incorporating traditional alignment research.

Although discussing emergent complexity in this paper, we argue that the achievements of traditional alignment research should be combined when searching for the coevolution of business and IS. Though markets have become hyperturbulent in recent years, organisations should take into account balanced alignment and unbalanced coevolution in the long run. Therefore, a sensing capability should be considered to identify the regions of complexity in advance (Tanriverdi & Lim, 2017). If the complexity of organisations or markets is low, traditional alignment mechanisms, models, and performance metrics should be adopted to seek sustainable competitive advantages. If the complexity is high, coevolutionary principles and models should be introduced to address the nonlinearity and uncertainties. Organisations need to pursue temporary and fleeting advantages in rugged landscapes.

![](/api/attachments/88S2MFZR/fulltext/images/c7c0eed83cfa2d533f6640c12e3c04a9a8f51894c1a305510c0e64392fc14571.jpg)  
Figure 8. Performance trends associated with diferent propositions.

Overall, with the advent of emerging technologies and associated dynamic strategies, complexity is likely to pose a long-term challenge in analysing alignment. Recent research on coevolution has expanded our research horizons. The theoretical and ABM developments here provide a bridge for researchers to integrate theory into practical applications so that practitioners can eventually achieve business success with the help of dynamic business and IS alignment.

## 7. Conclusion

Currently, coevolutionary principles of business and IS alignment have seldom been validated, and a long-term coevolutionary process has rarely been controlled and shaped by the principles. The validation and application of coevolutionary principles can help organisations manage individual behaviours and keep competitive advantages and agile superior in their running and evolving. To extend the extant research from analysing and validating coevolutionary principles, this paper aims to test three important coevolutionary principles (mutual-communication, knowledge sharing, and intelligence) via an agent-based model (ABM). We first explain the above three principles and formalise them into four propositions. Then, we develop an ABM of a hierarchical organisational structure and verify the propositions. The above four propositions are validated in the ABM, which has been identified that all of the principles have positive efects on the coevolution of business and IS, although several have exhibited higher costs or slower adaptability. These findings explain the advantages of the above three principles and how the organisation can apply principles in pursuing business and IS alignment. Through exploring the influences and applications of coevolutionary principles in organisations, we claim that it is beneficial to extend the alignment theoretical research and to drive organisation evolving and transforming practically.

![](/api/attachments/88S2MFZR/fulltext/images/3612f30743b315194fa35fbbb90978adefe3cec42d5bbf7d318299c28122aedf.jpg)

## Disclosure statement

No potential conflict of interest was reported by the authors.

## Funding

This work was supported by the National Natural Science Foundation of China [71571189].

## ORCID

Mengmeng Zhang http://orcid.org/0000-0001-7705- 2608

## References

Allen, P. M., & Varga, L. (2006). A co-evolutionary complex systems perspective on information systems. Journal of Information Technology, 21(4), 229–238. https://doi.org 10.1057/palgrave.jit.2000075

Amarilli, F., van Vliet, M., & Van den Hoof, B. (2017). An explanatory study on the co-evolutionary mechanisms of business it alignment. The 38th International Conference on Information Systems (pp. 1–21).

Amarilli, F., Van Vliet, M., & Van den Hoof, B. (2016). Business IT alignment through the lens of complexity science. The 37th international conference on information systems (pp. 1–16).

Avison, D., Jones, J., Powell, P., & Wilson, D. (2004). Using and validating the strategic alignment model. The Journal of Strategic Information Systems, 13(3), 223–246. https:/ doi.org/10.1016/j.jsis.2004.08.002

Baker, J., & Singh, H. (2015). The roots of misalignment: Insights from a system dynamics perspective. The JAIS theory development workshop Fort Worth (pp. 1–37).

Benbya, H., & McKelvey, B. (2006a). Using coevolutionary and complexity theories to improve IS alignment: A multi-level approach. Journal of Information Technology, 21(4), 284–298. https://doi.org/10.1057/palgrave.jit. 2000080

Benbya, H., McKelvey, B., & Jacucci, E. (2006b). Toward a complexity theory of information systems development. Information Technology & People, 19(1), 12–34. https:/ doi org/10 1108/09593840610649952

Besson, P., & Rowe, F. (2012). Strategizing information systems-enabled organizational transformation:

A transdisciplinary review and new directions. The Journal of Strategic Information Systems, 21(2), 103–124. https://doi.org/10.1016/j.jsis.2012.05.001

Bordia, P., Bernd, E. I., & David, A. (2006). Diferences in sharing knowledge interpersonally and via databases: The role of evaluation apprehension and perceived benefits. European Journal of Work and Organizational Psychology, 15(3), 262–280. https:// doi.org/10.1080/13594320500417784

Bygstad, B., Munkvold, B. E., & Volkof, O. (2016). Identifying generative mechanisms through afordances: A framework for critical realist data analysis. Journal of Information Technology, 31(1), 83–96. https://doi.org/10.1057/jit.2015.13

Cabrera, A., & Cabrera, E. F. (2002). Knowledge-sharing Dilemmas. Organization Studies, 23(5), 687–710. https:// doi.org/10.1177/0170840602235001

Carvalho, R., & Sousa, P. (2008). Business and Information Systems MisAlignment Model (BISMAM): An holistic model leveraged on misalignment and medical sciences approaches. Proceedings of BUSITAL, 8, 105. http://dx. doi.org/

Cecez-Kecmanovic, D., & Kay, R. (2001). IS-organization coevolution: The future of information systems. The 22th International Conference on Information Systems (pp. 41–51).

Chan, Y. E., & Reich, B. H. (2007). IT alignment: What have we learned? Journal of Information Technology, 22(4), 297–315. https://doi.org/10.1057/palgrave.jit.2000109

Chen, H. M., Kazman, R., & Garg, A. (2005). BITAM: An engineering-principled method for managing misalignments between business and IT architectures. Science of Computer Programming, 57(1), 5–26. https://doi.org/10. 1016/j.scico.2004.10.002

Ciborra, C. U., & Patriota, G. (1998). Groupware and teamwork in R&D: Limits to learning and innovation. R&D Management, 28(1), 1–10. https://doi.org/10.1111/1467- 9310.00080

Crooks, A., Heppenstall, A. J., & Malleson, N. (2017). Agent-Based modeling. Reference Module in Earth Systems and Environmental Sciences. https://doi.org/10.1016/B978- 0-12-409548-9.09704-9

De, H. S., & Wim, V. G. (2015). Enterprise governance of information technology. Achieving Alignment and Value, Featuring COBIT 5.

El Sawy, O. A., Malhotra, A., Park, Y., & Pavlou, P. A. (2010). Research commentary -seeking the configurations of digital ecodynamics: It takes three to tango. Information Systems Research, 21(4), 835–848. https:// doi.org/10.1287/isre.1100.0326

Fioretti, G. (2013). Agent-based simulation models in organization science. Organizational Research Methods, 16(2), 227–242. https://doi.org/10.1177/1094428112470006

Gawer, A., & Cusumano, M. A. (2014). Industry platforms and ecosystem innovation. Journal of Product Innovation Management, 31(3), 417–433. https://doi.org/10.1111/ jpim.12105

George, G., Osinga, E., Lavie, D., & Scott, B. A. (2016). Big data and data science methods for management research. Academy of Management Journal, 59(5), 1493–1507. https://doi.org/10.5465/amj.2016.4005

Gerow, J. E., Thatcher, J. B., & Grover, V. (2015). Six types of IT-business strategic alignment: An investigation of the constructs and their measurement. European Journal of

Information Systems, 24(5), 465–491. https://doi.org/10. 1057/ejis.2014.6

Haas, M. R., & Hansen, M. T. (2007). Diferent knowledge, diferent benefits: Toward a productivity perspective on knowledge sharing in organizations. Strategic Management Journal, 28(11), 1133–1153. https://doi. org/10.1002/smj.631

Hedström, P., & Ylikoski, P. (2010). Causal mechanisms in the social sciences. Annual Review of Sociology, 36(1), 49– 67. https://doi.org/10.1146/annurev.soc.012809.102632

Henderson, J. C., & Venkatraman, H. (1993). Strategic alignment: Leveraging information technology for transforming organizations. IBM Systems Journal, 32(1), 472–484. https://doi.org/10.1147/sj.382.0472

Hevner, A. R., Salvatore, T. M., Jinsoo, P., Sudha R. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75–105. https://doi.org/10.2307 25148625

Holland, J. (1995). Hidden order: How adaptation builds complexity. Addison-Wesley.

Joseph, K., Morgan, G., Martin, M., & Carley, K. (2014). On the coevolution of stereotype, culture, and social relationships: An agent-based model. Social Science Computer Review, 32(3), 295–311. https://doi.org/10.1177 0894439313511388

Kandjani, H., Tavana, M., Bernus, P., & Nielsen, S. (2014). Co-Evolution Path Model (CePM): Sustaining enterprises as complex systems on the edge of Chaos. Cybernetics and Systems, 45(7), 547–567. https://doi.org/10.1080 01969722.2014.945315

Kaufman, S. (1993). The origins of order: Selforganization and selection in evolution. Oxford University Press.

Kearns, G. S., & Albert, L. L. (2003). A resource-based view of strategic IT alignment: How knowledge sharing creates competitive advantage. Decision Sciences, 34(1), 1–29. https://doi.org/10.1111/1540-5915.02289

Lewin, A. Y., & Volberda, H. W. (1999). Coevolution of strategy and new organizational forms. Special Issue of Organization Science, 10(5), 519–534. doi:10.1287/ orsc.10.5.535

Liang, H., Wang, N., Xue, Y., & Ge, S. (2017). Unraveling the alignment paradox: How does business—IT alignment shape organizational agility? Information Systems Research, 28(4), 863–879. https://doi.org/10.1287/isre. 2017.0711

Luftman, J. (2004). Assessing business-IT allignment maturity. Strategies for Information Technology Governance, 99–128. doi:10.4018/9781878289872.ch006

Luftman, J., Lyytinen, K., & Ben Zvi, T. (2017). Enhancing the measurement of information technology business alignment and its influence on company performance. Journal of Information Technology, 32(1), 26–46. https:/ doi.org/10.1057/jit.2015.23

McKelvey, B. (1999). Avoiding complexity catastrophe in coevolutionary pockets. Organization Science, 10(3), 294–321. https://doi.org/10.1287/orsc.10.3.294

Merali, Y., Papadopoulos, T., & Nadkarni, T. (2012). Information systems strategy: Past, present, future? The Journal of Strategic Information Systems, 21(2), 125–153. https://doi.org/10.1016/j.jsis.2012.04.002

Mitleton-Kelly, E., & Papaefthimiou, M. C. (2000). Coevolution and an enabling infrastructure: A solution to legacy? Systems Engineering for Business Process Change, 164–181. doi:10.1007/978-1-4471-0457-5\_14

Nan, N., & Tanriverdi, H. (2017). Unifying the role of IT in hyperturbulence and competitive advantage via

a multilevel perspective of IS strategy. MIS Quarterly, 41 (3), 937–958. https://doi.org/10.25300/MISQ/2017/41.3.12

Nassim, B., & Robert, F. (2010). IS Alignment improved with co-evolutionary principles: An Open Source approach. The 43rd Hawaii International Conference on System Sciences (pp. 1–10).

Onik, M. F. A., Fielt, E., & Gable, G. G. (2017). Towards a complex adaptive systems roadmap for information systems research. Proceedings of the 21st Pacific Asia Conference on Information Systems (pp. 106).

Őri, D. (2014). Misalignment symptom analysis based on enterprise architecture model assessment. IADIS International Journal on Computer Science & Information Systems, 9(2), 146–158. Retrieved from www.iadisportal.org/ijcsis/papers/2014170210.pdf

Page, S. E. (2009). Understanding Complexity. Teaching Company.

Peppard, J., & Breu, K. (2003). Beyond alignment: A coevolutionary view of the information systems strategy process. The 24th International Conference on Information Systems (pp. 61–69).

Reich, B. H., & Benbasat, I. (2000). Factors that influence the social dimension of alignment between business and information technology objectives. MIS Quarterly, 24 (1), 81–113. https://doi.org/10.2307/3250980

Sabherwal, R., Hirschheim, R., & Goles, T. (2001). The dynamics of alignment: Insights from a punctuated equilibrium model. Organization Science, 12(2), 179–197. https://doi.org/10.1287/orsc.12.2.179.10113

Schlosser, F., Wagner, H. T., & Coltman, T. (2012). Reconsidering the dimensions of business-IT alignment. 45th Hawaii International Conference on System Science (pp. 5053–5061). IEEE.

Simpson, J. R., Wilkin, C. L., Campbell, J., Keating, B. W., & Moore, S. (2016). Iterate wildly: Is user-centred design and prototyping the key to strategic alignment? The 24th European Conference on Information Systems (pp. 1–12).

Tallon, P. P., & Pinsonneault, A. (2011). Competing perspectives on the link between strategic information technology alignment and organizational agility: Insights from a mediation model. MIS Quarterly, 35(2), 463–486. https://doi.org/10.2307/23044052

Tanriverdi, H., & Lim, S. Y. (2017). How to survive and thrive in complex, hypercompetitive, and disruptive ecosystems? The roles of IS-enabled capabilities. The 38th International Conference on Information Systems (pp. 1–21).

Tanriverdi, H., Rai, A., & Venkatraman, N. (2010). Research commentary—reframing the dominant quests of information systems strategy research for complex adaptive business systems. Information Systems Research, 21(4), 822–834. https://doi.org/10.1287/isre.1100.0317

Teece, D. J. (2009). Dynamic capabilities and strategic management: Organizing for innovation and growth. Oxford University.

Teece, D. J. (2014). The foundations of enterprise performance: Dynamic and ordinary capabilities in an (economic) theory of firms. Academy Management Perspective, 24(4), 328–352. https://doi.org/10.5465/amp. 2013.0116

Tivnan, B. F. (2005). Coevolutionary dynamics and agent-based models in organization science. Proceedings of the 37th conference on Winter simulation conference (pp. 1013–1021).

Vessey, I., & Ward, K. (2013). The dynamics of sustainable IS alignment: The case for IS adaptivity. Journal of the

Association for Information Systems, 14(6), 283–311. https://doi.org/10.17705/1jais.00336

Vidgen, R., & Wang, X. (2006). From business process management to business process ecosystem. Journal of Information Technology, 21(4), 262–271. https://doi.org 10.1057/palgrave.jit.2000076

Wagner, H. T. (2014). Evolvement of business-IT alignment over time: A situated change perspective. 2014 47th Hawaii International Conference on System Sciences (pp. 4366–4375). IEEE.

Wagner, H. T., & Weitzel, T. (2012). How to achieve operational business-IT Alignment: Insights from a global aerospace firm. MIS Quarterly Executive, 11(1), 25–36. https://aisel.aisnet.org/misqe/vol11/iss1/5

Yoo, Y., Boland, R. J., Jr, Lyytinen, K., & Majchrzak, A. (2012). Organizing for innovation in the digitized

world. Organization Science, 23(5), 1398–1408. https:// doi.org/10.1287/orsc.1120.0771

Zhang, M., Chen, H., & Lyytinen, K. (2019a). Principles of Organizational Co-evolution of Business and IT A Complexity Perspective. Proceedings of the 27th European Conference on Information Systems (ECIS2019).

Zhang, M., Chen, H., Lyytinen, K., & Li, X. (2019b). A co-evolutionary perspective on business and IT alignment: A review and research agenda. Proceedings of the 52nd Hawaii International Conference on System Sciences (HICSS-52).

Zwietering, M., Jongenburger, I., Rombouts, F. M., & Van, T. (1990). Modeling of bacterial growth curve. Applied and Environmental Microbiology, 56(6), 1875–1881. https://doi.org/10.1128/AEM.56.6.1875- 1881.1990

## Appendix A

Table A1. Summary of sensitivity tests.

<table><tr><td>Parameters</td><td>Values tested</td><td>Results</td></tr><tr><td rowspan="2">Number of knowledge points in one knowledge set</td><td>2</td><td rowspan="2">Varied number of knowledge points has no systematic effect on coevolutionary trends. The evolutionary time increases with the increasing of this number.</td></tr><tr><td>10</td></tr><tr><td rowspan="2">Number of the organisation structure&#x27;s layers</td><td>2</td><td rowspan="2">The evolutionary time increases slightly with the number. The time paths of the metrics are similar.</td></tr><tr><td>4</td></tr><tr><td rowspan="2">Number of presidents</td><td>2</td><td rowspan="2">The evolutionary time increases slightly with the number.</td></tr><tr><td>3</td></tr><tr><td rowspan="2">Number of business/IS managers</td><td>5</td><td rowspan="2">Same as the above.</td></tr><tr><td>15</td></tr><tr><td rowspan="2">Number of business/IS actors</td><td>40</td><td rowspan="2">Same as the above.</td></tr><tr><td>60</td></tr><tr><td rowspan="2">Number of groups</td><td>2</td><td rowspan="2">The evolutionary trends are similar, but the performance outcomes are more rugged with the number.</td></tr><tr><td>4</td></tr><tr><td rowspan="3">Number of changes in president layer</td><td>0</td><td rowspan="3">The evolutionary trends are similar, but the evolutionary time increases with the number.</td></tr><tr><td>2</td></tr><tr><td>3</td></tr><tr><td rowspan="3">Number of changes in business managers&#x27; domain</td><td>0</td><td rowspan="3">Same as the above.</td></tr><tr><td>2</td></tr><tr><td>3</td></tr><tr><td rowspan="3">Number of changes in IS managers&#x27; domain</td><td>0</td><td rowspan="3">Same as the above.</td></tr><tr><td>2</td></tr><tr><td>3</td></tr><tr><td rowspan="3">Number of changes in business actors&#x27; domain</td><td>0</td><td rowspan="3">Same as the above.</td></tr><tr><td>2</td></tr><tr><td>3</td></tr><tr><td rowspan="3">Number of changes in IS actors&#x27; domain</td><td>0</td><td rowspan="3">Same as the above.</td></tr><tr><td>2</td></tr><tr><td>3</td></tr><tr><td rowspan="2">Communicating probability in one group</td><td>0.7</td><td rowspan="2">The evolutionary time decreases slightly with the number but has no effect on overall trends.</td></tr><tr><td>0.9</td></tr><tr><td rowspan="2">Communicating probability in one domain</td><td>0.3</td><td rowspan="2">Same as the above.</td></tr><tr><td>0.5</td></tr><tr><td rowspan="2">Communicating probability between different domains</td><td>0.05</td><td rowspan="2">Same as the above.</td></tr><tr><td>0.15</td></tr><tr><td rowspan="2">Initial learning probability</td><td>0.05</td><td rowspan="2">The evolutionary trend is more drastic with the increasing number. The number has no effect on overall trends.</td></tr><tr><td>0.15</td></tr><tr><td rowspan="2">Path dependency increment</td><td>0.05</td><td rowspan="2">The evolutionary time decreases with the increasing number. The number has no effect on overall trends.</td></tr><tr><td>0.15</td></tr><tr><td rowspan="2">Communicating cost in one group</td><td>0.5</td><td rowspan="2">Varied number of costs has no systematic effect on coevolutionary trends, only changes the overall cost value.</td></tr><tr><td>1.5</td></tr><tr><td rowspan="2">Communicating cost in one domain</td><td>1.5</td><td rowspan="2">Same as the above.</td></tr><tr><td>2.5</td></tr><tr><td rowspan="2">Communicating cost in different domains</td><td>3.5</td><td rowspan="2">Same as the above.</td></tr><tr><td>4.5</td></tr><tr><td rowspan="2">Knowledge sharing cost</td><td>0.5</td><td rowspan="2">Same as the above.</td></tr><tr><td>1.5</td></tr><tr><td rowspan="2">Learning cost</td><td>2.5</td><td rowspan="2">Same as the above.</td></tr><tr><td>3.5</td></tr><tr><td rowspan="2">Reporting cost</td><td>15</td><td rowspan="2">Same as the above.</td></tr><tr><td>25</td></tr><tr><td rowspan="2">Commanding cost</td><td>15</td><td rowspan="2">Same as the above.</td></tr><tr><td>25</td></tr><tr><td>Parameters in the growth curve formula</td><td>Randomly set the parameters</td><td>These parameters mainly influence the evolutionary time and the process of achieving the peak value. The data selected aligns with the evolutionary trends.</td></tr><tr><td rowspan="2">Number of simulation sessions in each condition</td><td>10</td><td rowspan="2">Number of simulation sessions has no systematic impact on overall evolutionary trends of performance outcomes.</td></tr><tr><td>50</td></tr></table>
