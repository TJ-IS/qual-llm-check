---
otero_id: 10416
otero_key: "9HCN5WQU"
title: "Identimod: Modeling and managing brand value using soft computing"
authors: "Manuel Chica; Óscar Cordón; Sergio Damas; Valentín Iglesias; José Mingot"
year: "2016"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2016.06.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Manuel Chica<sup>a,</sup>\*, Óscar Cordón<sup>b</sup>, Sergio Damas<sup>c</sup>, Valentín Iglesias<sup>d</sup>, José Mingot<sup>d</sup>

<sup>a</sup>Department of Computer Science-IN3, Open University of Catalonia, 08018 Barcelona, Spain

<sup>b</sup>DECSAI and CITIC-UGR, University of Granada, 18071, Granada, Spain

<sup>c</sup>Department of Software Engineering, University of Granada, 18071, Granada, Spain

<sup>d</sup>RØD Brand Consultants, 28001 Madrid, Spain

## A R T I C L E I N F O

Article history: Received 15 October 2015 Received in revised form 18 April 2016 Accepted 4 June 2016 Available online 27 June 2016

Keywords: Branding Marketing Decision support systems Soft computing

## A B S T R A C T

Brands are one of the most important of a firm’s assets. Brand-managing activities are typically related to brand positioning and integration with marketing campaigns, and can involve complex decisions. The branding of an organization is indeed a dynamic system with many cause-effect relationships as well a intangible and heterogeneous variables. In order to help brand managers and marketers, we propose a decision support system, named Identimod, for modeling and evaluating branding strategies. Identimod uses non-linear dynamic modeling and soft computing to identify the branding system from different data sources through a linguistic user interface, and to provide advanced methods for diagnostics and validation. Identimod steps through a participatory, cyclic, and iterative process consisting of four different modules to increase the confidence and validity of the model, which should facilitate its acceptance by managers and stakeholders. Throughout this paper we demonstrate the modeling process and managerial benefits of Identimod by forming and answering the marketing questions for a real rebranding case of a seafood company in Spain.

© 2016 Elsevier B.V. All rights reserved

## 1. Introduction

For companies, branding is a top management priority as brands are one of the most valuable intangible assets that firms have [1, 2, 23, 25]. The decisions made by marketers, especially frequent ones, must be aligned with the brand management of the company, which involve tasks such as developing brand positioning, integrating marketing activities, assessing brand performance, and strategically growing the brand [25]. The brand image management of an organization is a process that regularly includes group decision making, managers’ experience, intuition, and judgment, and so is complex because it generates a high level of uncertainty and ambiguity [31].

Managing brands requires studying and anticipating the effects of complex dynamic interactions between a company, the business environments, and all the stakeholders. Managerial decisions usually involve intangible variables related to the brand, called brand intangibles, which are aspects of a product/service that do not involve physical or concrete attributes/benefits and play an important role for building the brand image and reputation of a firm [25, 26]. Marketers also need to integrate strategies built on intangible brand variables with marketing activities, which affect the brand positioning and equity of the company [25].

The main goal of the presented work is to propose a decision support system (DSS) to help marketers and stakeholders when modeling branding systems that have intangible variables. This work contributes to existing literature by defining the architecture and implementing a DSS with a new way of dealing with intangible branding variables and their relationships. The proposed DSS is able to handle branding variables and their complex relationships with linguistic interfaces, and is designed to facilitate the iterative nature of the modeling process. It also highlights the need for a complete model validation process and provides the DSS user with tools to do it [43]. Another important feature of the DSS is the use of a participatory modeling process to involve stakeholders and promote better marketing decisions [51], meaning that both modelers and decision makers contribute to the modeling process. The stakeholders’ participation is a key requirement for appropriate model development and promotes the final adoption of the model's results.

Identimod is the name of our proposed DSS, whose methodology is based on Vester’s sensitivity model (VSM) [49, 50], a semiquantitative modeling tool using system dynamics [17] and fuzzy logic [52]. This methodology has already been applied to different problems [22, 44]. Broadly speaking, system dynamics is a modeling tool appropriate for brand value management [2] because brands can be considered a dynamic system where all their components are treated as resources which grow or erode over time [36]. Beyond the VSM approach, we also incorporate soft computing [9] techniques into Identimod to better cope with the branding complexity. The branding complexity occurs when dealing with many managerial problems, in part caused by the presence of a heterogeneous group of stakeholders who need to make decisions [31, 51]. This participatory modeling needs methods able to deal with human feelings, perceptions, and their corresponding uncertainty [51]. Extending VSM with soft computing techniques in Identimod allows managers to easily model the uncertainty present in branding and marketing systems by defining linguistic variables, effects, and simulation cases with a human-centric interface [20].

The proposed DSS aims to promote the discussion and improvement of the branding models by identifying their structure, validating the model with respect to the brand in reality, and run what-if scenarios to test marketing actions. Identimod relies on an iterative and cyclic modeling process, and its DSS architecture is divided into four modules: (i) a generation module, where modelers identify the variables of the branding system and their relationships with respect to the stated goals with the collaboration of stakeholders; (ii) a diagnostics module, where modelers make use of diagnostics tools to ease the analysis of the branding model structure; (iii) a validation module, to check the validity of the model using a set of tools such as automatic model calibration with respect to the historical brand evolution; and (iv) a utilization module, to forecast the values of the branding variables to evaluate the most convenient marketing policies for different scenarios.

Previous studies already pointed out the successful use of soft computing and DSSs for strategic marketing [30, 31]. The use of soft computing, specifically fuzzy logic and computing with words [53], has important advantages when dealing with human perceptions and uncertainty. Fuzzy logic enables the use of natural language structures by computing with words to convey decision making. In essence, computing with words is a methodology for reasoning, computing, and decision-making with information described in natural language. The use of linguistic information in decision making demands computing processes using words to solve the related decision problems. A wide group of DSSs based on computing with words is reviewed in [32]. Identimod includes another soft computing technique, evolutionary algorithms [7], that have the ability to search for optimal solutions to complex problems and in a reasonable amount of time [7, 19].

In this paper, we initially present the background motivation for our work (Section 2). Later, Section 3 describes the architecture of the DSS, and Section 4 details the modules, processes, and stages in detail. Finally, we apply the Identimod framework and its four modules for a brand management case study of a real Spanish seafood company. This company produces and sells fish and seafood products (e.g., elver and surimi). Managers of the company wanted to prepare the brand for the upcoming launch of more products and a diversification of its product portfolio. Section 5 explains how Identimod can be used to model and answer the latter marketing questions for this real branding problem, from the use of data and expert knowledge for building validated models, to the simulation of three different scenarios. A final discussion about the managerial impact of Identimod and future areas for improvement is given in Section 6.

## 2. Background

There are different modeling methodologies for building complex business problems with the involvement of stakeholders [51]. These methodologies use non-linear dynamic models to characterize realworld, complex systems and the relationships of their elements. They are also particularly suited to building systems with a high number of interrelated variables and with scarce and/or uncertain data [38]. An important feature of the stated methodologies is they provide simulation tools to compare alternative business strategies and better assist decision makers with their managerial decisions [51].

A prominent example among the set of existing methodologies is system dynamics, which presents a theoretical framework with tools and techniques for developing mathematical models of complex systems for social, biological, and economic scenarios [17, 45]. System dynamics is intended to solve more strategic-level problems rather than other methodologies such as discrete-event simulations [47]. It is a methodology aimed at studying the structures of social or organizational systems by representing the causal relationships among their elements and the evolution of a system over time. System dynamics promotes the ongoing dialog among modelers and managers regarding strategy formation and its evaluation, and have been successfully applied to a diverse set of applications [4, 14, 41]. Among this diverse set of applications, few are used for branding. Crescitelli and Figueiredo [13] analyzed the brand equity evolution using system dynamics, and Chan and Ip [11] constructed a model for predicting the customer equity value for new product development. Gani and Groessler [18] conceptualized the linkage between brand equity and customer equity in a system dynamics model to provide insights on how these two concepts interact with each other. Finally, Mukherjee and Roy [36] developed a model for managing the brand equity and reputation of an Indian television show.

Brand value management can be seen as a complex, adaptive, and dynamic environment. The environment is usually a system with a high number of variables and contains non-linearities, inertia, delays, and bi-directional network feedback loops. System dynamics is an ideal methodology for such complex feedback systems, like brand management [36]. As pointed out by Crossland et al. [15], system dynamics allows brand managers to evaluate both the structure and the dynamic relationships between components of a brand management system, but traditional system dynamics lack the humancentric modeling features [20] necessary when modeling branding systems. Examples of these features are the inclusion of uncertainty into the model and linguistic definitions of the variables and the relationships among them.

One of the existing system dynamics variants is Vester’s sensitivity model (VSM) [49, 50], which offers a semi-quantitative system dynamics modeling tool based on fuzzy logic [52], and has been applied to different fields of research such as environmental management and tourism [22, 44]. Its main advantages are the ease of use when discussing results with stakeholders and the utilization of feedback analysis as the core component of the modeling process. Structurally, VSM can be seen as a fuzzy cognitive map as it consists of nodes (or concepts), which are the variables, connected by edges that represent the fuzzy causal relationships between the concepts. A relationship (name effect) can be either positive (when growth of a concept stimulates growth in another) or negative (when growth of a concept inhibits growth in another).

Fuzzy logic is well known for its ability to model linguistic concepts (computing with words) [53] and it can formalize, either as an approximation or with more precision, vague concepts. The use of fuzzy sets and systems lets us move from computing with numbers to computing with perceptions [53] and it becomes natural moving from traditional system identification to more advanced identification such as in business, where product attributes and their relationships cannot be easily measurable and are defined imprecisely [34].

Fuzzy logic is a part of soft computing [9], an area of artificial intelligence focused on the design of intelligent systems to process uncertain, imprecise, and incomplete information from real-world problems. Soft computing methods frequently offer more robust, tractable, and less costly solutions compared to those obtained by conventional mathematical techniques [24]. The set of soft computing techniques is diverse in their typology and areas of application. In addition to fuzzy logic, evolutionary algorithms [7] are another outstanding soft computing technique which include biologically-inspired algorithms to solve complex optimization problems. Genetic algorithms (GAs) [19] are the most representative evolutionary algorithm. GAs are general-purpose search algorithms that evolve a population of chromosomes representing candidate solutions to the optimization problem towards better solutions through a competitive and iterative process. We can find many studies where fuzzy logic and/or evolutionary algorithms were applied to the design of DSSs in the marketing field [5, 29, 30].

## 3. General description of the DSS

## 3.1. Architecture and main components

The DSS architecture and four main modules of Identimod are shown in Fig. 1. This architecture diagram shows the core computational techniques used in each module, the principal participants of the modules, and the marketing data used for building the models. There is not a strictly linear order in a participatory modeling process but an iterative process [51], because branding modelers and stakeholders need to go back through again several times, depending on the goal of the study and the gained marketing insights. Although modelers, marketers, and managers must be involved in all the stages of the modeling process, each module has a main participant role who has the most important involvement and is in charge of its output (see the main participant roles in Fig. 1). We briefly describe the four modules of the DSS architecture below, although the specific details of each are later explained in Section 4:

Generation module: This module comprises two main stages: variable identification and structure definition by means of effects between the variables. During variable identification, modelers identify the goals of the model and collect data and expert knowledge from the company, in collaboration with marketers and stakeholders. Then a discussion is needed to choose the main variables of the branding system, taking into account the goal of the model and the available data. To facilitate this task, each variable of the branding system is defined using fuzzy linguistic terms with free semantics [6] and several fuzzy behavioral rules. Section 4.1.1 shows how to include and specify the variables of the model in Identimod. Once all the main variables are identified, the aim of the structure definition stage is to build the fuzzy causal diagram of the branding model by mimicking the effects between variables. Identimod facilitates a linguistic effect editor and visual graphs to easily build the diagram for the branding dynamics (see Section 4.1.2 for the complete description).

Diagnostics module: Identimod provides modelers with two processes to diagnose the causal diagram that is built when generating the branding model. First, there is a feedback analysis tool to study the structural branding dynamics. This tool helps modelers verify the structure of the model and the type of system they are working with. Second, there is an automatic key variable detection algorithm that uncovers the variables of the model generating the most significant changes on the system. Sections 4.2.1 and 4.2.2 describe these two diagnostic stages to analyze the model structure. The generation and diagnostics modules are closely related and are used together to refine and re-model the system.

Validation module: Identimod primarily does model calibration, which is the process of estimating the model parameters to achieve a reasonably accurate relationship between observed and simulated structures and behaviors [37, 43]. To do this, Identimod provides an automatic calibration tool based on GAs. Together with calibration, sensitivity analysis is crucial and further validates the model by exploring its sensitivity to a particular set of parameter values and inputs [37], being key ingredients to the quality of a model-based study [42]. Sensitivity analysis also reveals those parameters to which the model behavior is highly sensitive [42]. Sections 4.3.1 and 4.3.2 detail the capabilities of calibration and sensitivity analysis, respectively.

![](/api/attachments/9HCN5WQU/fulltext/images/b1be70c32498baebfe7d42f2ab6bd0c21f9b8fac46cac2e2bbac498a79c351a0.jpg)  
Fig. 1. Architecture diagram with the four modules of Identimod, their stages, main actors, and marketing databases to generate and validate the branding models.

Utilization module: The variables and effects of the branding model represent a dynamic system whose evolution over time provides branding insights for marketers and managers. The simulation engine is based on handling fuzzy variables and effects of the model, and propagates these events in a discrete simulation for a given period of time. In addition, modelers can define and run what-if scenarios using the validated model and strategic actions associated with variables in order to increase the brand equity, brand loyalty, and/or purchase consideration, or to answer other branding questions. Once discussed with the involved decision makers and marketers, the results of the strategies can be transformed into decisions. Identimod’s simulation and strategies within what-if scenarios are given in Section 4.4.

As can be seen in the architecture diagram of Fig. 1, the computational techniques presented in Identimod (e.g., VSM, fuzzy logic, computing with words, and GAs) are independent from the specific goals of the modules. Such a modular DSS architecture can ease the deployment of new computational techniques or the further improvement of the existing ones for each of the four modules. These changes to the used techniques will not have a significant impact on the modules of DSS if they follow the basic principles of Identimod.

## 3.2. Linguistic modeling and validation tools for identifying the branding system

When dealing with a branding problem, different and heterogeneous data sources are provided by the company. In the absence of structured data and in the presence of diverse sources of precise numerical data, linguistic information, questionnaires, customers’ panels, and expert knowledge, there is no model structure assumed and virtually any system can be represented by a model [6, 12]. The architecture and advanced methods included in Identimod facilitate a participatory modeling and validation scheme to help with system identification (i.e., main branding variables and their relationships and causal effects) in light of the available data from the company.

Even with having numerical data for all the branding variables, the identification of a linguistic model is not straightforward because one has to estimate the linguistic variables and their relationships [6, 12]. For Identimod we have considered a linguistic modeling approach where variables, when identified, do not take any a priori defined linguistic values but are customizable and agreed on by modelers and stakeholders from the available numerical data, linguistic information, and expert knowledge. To check the validity of the built model, Identimod incorporates the diagnostics and validation modules to provide numerical, graphical, and assisted validation tools to help with the analysis of the model consistency and whether its results are correct or not [43].

The use of linguistic terms in Identimod does not limit but instead facilitates the interaction between stakeholders in crosscultural market situations. Generally, experts are more comfortable with expressing themselves using words instead of numbers since humans usually deal with concepts by describing them in words [35]. The specific linguistic values of each branding variable can be customizable depending on the marketing and cultural context to facilitate the modeling dialog. Besides, it is important to mention that the DSS internally uses numerical values for the linguistic terms and the DSS modeler can always make them visible instead of the linguistic values.

## 3.3. DSS implementation details

Existing studies applying system dynamics to branding problems used standard commercial tools and generic graphical simulation programs, like iThink, Powersim, and Vensim [11, 13, 18, 36]. These commercial tools help to evaluate the structure and run simulations. However, they are problem-generic and lack flexibility when creating a DSS that deals with complex environments where uncertainty, vagueness, linguistic descriptions, and intangible variables are crucial for adequately solving the problem. In addition, DSSs usually consist of three subsystems: a user interface, a database, and a model processing [35].

Identimod aims to bridge that gap by considering these three subsystems for an ad hoc implementation for managing branding problems based on a client–server architecture. A remote database stores all the models, their users, and their associated roles (i.e., modeler, marketer, manager), and each software client accesses the database manager (e.g., Microsoft SQL Server) via a Web server (e.g., IIS Microsoft Windows Server on an Amazon Web Services machine). The software client uses C++ for the computational and processing techniques for each module, and Microsoft Visual Studio C# for the graphical user interface. In order to facilitate the modular architecture and computational techniques update, a model-viewcontroller approach is used for the software architecture.

## 4. Module description

## 4.1. Generation module

In this module, the branding variables and their relationships are defined, and in particular the variable identification stage (Section 4.1.1) aims to determine the main variables of the system. Once they are identified, the structure definition of the system aims to describe the causal diagram of the branding system by means of its effects (Section 4.1.2).

## 4.1.1. Branding variable identification using linguistic terms

According to the description of VSM, it is possible to deliver a fairly appropriate description of a system’s behavior even with a small amount of data, or with fuzzy, estimated, or missing data, as long as the dataset satisfies the criteria necessary for understanding a systemic pattern of interactions [49]. The key lies in aggregating details in essential model variables. The first step to modeling a branding system is to identify the variables that dynamically interact with each other to generate the model behavior. These branding variables can fall under measurements of brand value [1, 2] (i.e., brand interest, loyalty, perceived quality, and brand associations) and factors that affect them (marketing activities, word-of-mouth, or brand competition).

We have modeled these intangible and tangible variables using fuzzy terms [53]. This is due to the linguistic nature of both the variables and the record source, which consists of qualitative information and expert knowledge in unstructured natural language. Fig. 2 shows the graphical interface where the modeler can define a variable. Identimod includes fields such as the variable name, description, optimal criteria, current linguistic value, and limitation of the variable value when simulating the system. Although the DSS screenshot shows a slider-bar with linguistic terms, Identimod internally represents each variable i of a system composed of N variables with a numerical value $\nu _ { i } \in [ 0 , 1 0 0 ]$ which is transparent to the DSS user. Identimod also allows the modeler to specify more advanced rules for each branding variable (see Rules panel of Fig. 2):

When the variable can be used for a marketing strategy: If it is negative, this variable is locked when defining strategies in Identimod. This type of “non-actionable” variable corresponds to external factors that may have an important influence in the model but that modelers cannot modify and can only account for them. See Section 4.4 for more details about strategies.

![](/api/attachments/9HCN5WQU/fulltext/images/ff1f91a0d56057a5339b68236e8bf1047be0124917fe407a81f1f487724809a9.jpg)  
Fig. 2. Identimod linguistic creation of the intangible brand awareness variable.

When the variable includes a self-loop (i.e., an effect where the source and target are the variable itself): At this stage in Identimod, no more details are provided about the self-loop as modelers and/or stakeholders provide a general description of the branding system. Thus, the details of the self-loop are specified during the structural modeling stage.

When the variable has a random behavior: Identimod will run stochastic simulations where at least one random variable is defined together with its random noise level. For more details about the simulation consequences of declaring a random variable, see the description of the simulation engine in Section 4.4.

## 4.1.2. Building the system structure by using linguistic effects

Once the model variables are identified, modelers need to define the dynamics of the branding system by building a causal diagram of variables and the relationships between them, which are defined by a fuzzy effect (i.e., an edge between a source and a target variable that denotes a structural influence). Identimod provides a visual interface to represent and modify the directed graph of variables and fuzzy effects between them. In a first step, effects between variables are drawn by only specifying if they are direct (a change in the source variable modifies the target directly and proportionally) or inverse (a change in the source variable modifies the target variable inversely proportional to the source). The latter consideration is needed for the feedback analysis of the diagnostics module (see Section 4.2.1). When modelers and stakeholders agree on the causal diagram of the branding problem, modelers can specify the details of each effect in a second step. Identimod follows an iterative process when specifying the system variables and effects (as well as with other steps of the branding system generation). For instance, it might happen that new variables are identified during the discussions of the causal diagram. The modeler will thus go back to the system identification phase and create the required variable.

Unlike traditional system dynamics techniques, Identimod offers a linguistic interface to easily define the attributes of an effect in a human-centric approach [20]. We use a fuzzy effect editor to define qualitative relationships between every two variables by means of a fuzzy effect. The modeler can modify five qualitative attributes by using graphical sliders to define the effect through the editor (see Fig. 3). Again internally, Identimod stores each of the five sliders that define an effect e as a value between [ 100, 100] where 0 means no effect on the target variable and 100 mean the highest decrease and increase in the target variable. The specific effect value to be applied changes depending on the current value of the source variable. Internally, a complete interpolated effect function is internally built by using these five qualitative attributes and is then applied when running a simulation (see Section 4.4 for more details about the simulation engine and effects application). The rest of the components of the effect that can be defined by the Identimod effect editor are the following:

Intensity: regulates the quantitative value of the effect change. This value is one of the most dificult to define for a modeler and therefore, Identimod allows the modeler to automatically calibrate the intensities of all the effects in order to adjust the behavior of the model to the historical data of brand changes over time. See the calibration process in Section 4.3.1.

Delay: an effect that has a delay for its application. It represents the number of months the application of the effect will be postponed during a simulation. This component is interesting because some branding variables and factors (e.g., marketing campaigns) do not have an immediate effect but need a certain period of time for it to affect the brand.

Confidence level: modelers can associate their confidence when defining the effect. This confidence comes from data analysis and/or information provided by stakeholders and marketers through interviews, questionnaires, and/or surveys. Given the dificulty to accurately define the details of the effects, the calibration engine is devoted to adjust them to match the system with the brand in reality. The calibration engine, which belongs to the validation module (see Section 4.3.1), uses the confidence level to set a higher or lower importance level on the adjustment of the effect parameters. If the confidence level is very high, the calibration engine will slightly adjust the intensity of the effect. If modelers and stakeholders do not have enough certainty about the effect, the confidence is set to low and the calibration engine will be allowed to drastically modify the effect parameters to match the historical trends of the branding system.

![](/api/attachments/9HCN5WQU/fulltext/images/5367a3d185f78eb085e51925e72da03728f1ef7a7396c797bc8532a77bf71366.jpg)  
Fig. 3. Linguistic definition of a direct effect between two branding variables: brand afinity and customers’ recommendation.

## 4.2. Diagnostics module

In this section we detail the two main components of the second module of Identimod. Their purpose is to diagnose the causal diagram of the branding model to help the modeler with their evaluation. First, we present the analysis of the feedback loops (Section 4.2.1) and second, the automatic detection of key variables for the system (Section 4.2.2).

## 4.2.1. Feedback analysis

One of the most important components of system dynamics and VSM is the feedback loops that embody the information feedback structure of the system [45, 50]. The reason for emphasizing the feedback analysis is that it is often necessary to consider feedback within management systems in order to understand what is causing the patterns of behavior [27]. Specifically, feedback loops form the core of the structure that enables growth or erosion of brand value [36]. A feedback is a closed sequence of causes and effects, that is, a closed path of action and information [27], or more formally, a feedback f is a synonym of elementary cycle in a directed graph. There are several classical algorithms that enumerate the full list of elementary cycles in directed graphs. One of the most well-known is Tiernan’s algorithm [48], which enumerates all the feedback loops in graph models and is used in Identimod to return the set of all the feedback loops F of the casual diagram of the branding model.

A feedback loop can be of two types: balancing or reinforcing. In balancing feedback, an initial variation in a variable of the loop changes the variable in the opposite direction, mitigating the initial change. In reinforcing feedback, the initial change in a variable of the loop is reinforced through the feedback process. Feedback is considered as balancing or reinforcing by counting the number of direct and inverse effects that make up the loop [27, 45]. Specifically, a feedback loop is called reinforcing if it contains an even number of inverse causal effects. A feedback loop is called balancing if it contains an odd number of inverse causal effects.

The rationale is that an even number of inverse effects will provoke an uncontrolled increase or decrease of the values of the variables. When we have a feedback with one, three or more odd numbers of inverse effects, all the effects are counteracted. Consider a model example with four branding variables (A, B, C, and D), three inverse effects $( A \mathrm { ~ -- ~ }  \mathrm { ~ } B , B \mathrm { ~ -- ~ }  \mathrm { ~ } C ,$ , and $C \mathrm { ~ -- ~ }  \mathrm { ~ } D )$ , and one single direct effect $( D \to A )$ . If an external change were to make A fall, B would rise (i.e., move in the opposite direction as A), C would fall (i.e., move in the opposite direction as B), D would rise (i.e., move in the opposite direction as C), and A would rise (i.e., move in the same direction as D). The rise in A after the initial change propagates around the feedback loop, acts to stabilize the system and thus, is counteracted by the branding system’s response.

When a branding model has more balancing than reinforcing feedback loops, the system is more stabilized and changes are smooth. To summarize the stated model features and develop additional feedback analysis, Identimod does not only show the set of total feedback loops F, balancing B or reinforcing R, but also calculates several metrics to reveal the structure of the branding system. These metrics are computed from the list of enumerated feedback loops as follows:

self-organizing $( \lambda \in [ 0 , \infty ) ) \colon$ measures the ratio between the number of feedback loops ( F ) and the number of variables of the system (N) by $\begin{array} { r } { \lambda \ = \ \frac { | F | } { N } } \end{array}$ . When k is high, the system has self-organized behavior. In the case of few feedback loops, the model may have dependency on external factors [50].

elasticity $( \epsilon \in [ 1 , \infty ) ) \colon$ computed as the average length of all the feedback loops F, weighted by the number of variables N , and taking into account the amount of delay for each effect (adding from 0 to 12 months). Small 4 values mean short cycles and therefore swift reactions to strategies. When a branding system shows a high structural elasticity, modelers must check if the long feedback loops are mitigating or reinforcing in order to anticipate abrupt or extremely slow behavior [50].

stability $( \sigma \in [ - 1 , 1 ] )$ : defined as the ratio between the number of balancing (B) and reinforcing feedback loops (R) by $\sigma =$ B R This ratio yields positive results when $| B | \ > \ | R |$ and B + R means structural stability of the branding system. This ratio is 0 when we have the same number of balancing and reinforcing feedback $( | B | = | R | )$ . Stability returns 1 when there is no feedback $\langle | R | = | B | = 0 \rangle$ and stability is maximum. I $\dot { \mathbf { \theta } } | R | > | B | , \sigma$ is negative and the system may have drastic changes.

## 4.2.2. Automatic key variable detection

A key variable of a system dynamics model is defined as a variable able to generate significant changes in the whole system (i.e., the whole set of variables of the model) [8]. The identification of key variables provides the modeler with descriptive information about the model’s dynamics and constitutes an additional boundary and structure verification test for the model [37, 39]. The identification of key variables is also useful for modelers to better focus their strategic actions on what-if scenarios.

However, it is usually dificult to visually identify these variables in models with a large number of variables; we can easily find up to 40 variables in branding management problems. Therefore, the goal of this diagnostic tool is to automatically detect the set of key variables of an Identimod branding model, following a similar approach to the one proposed in [8]. First, the detection algorithm computes a quality metric for every variable of the graph structure of the branding model. This quality metric can be seen as an indicator of the level of its relevance or importance. Then, the algorithm ranks the variables according to their metric values and finally returns the highest ranked variables to the DSS user.

The most important step within the key variable detection algorithm is the computation of the quality metric, which makes use of the network-based properties of the model structure. Its computation is based on social network analysis [10] and specifically on centrality metrics that provide structural local measurements. These metrics share the common objective of identifying key actors in social networks and they are considered as a measure of centrality or prestige. For instance, they have already been used in DSS to locate influencers in customer networks [28].

A well-known centrality metric is the closeness centrality that measures how close a node is to all the other nodes in a social network. In our approach, we extend it to include information about how many variables are reached directly or indirectly by proposing a new metric called elastic distance (ED). This ED also considers the delay of each effect of the branding model by adding it as the weight (effect delay) of the edges of the graph. The ED is computed as the average of the shortest weighted distances from the variable being evaluated to all the remaining variables of the system. Distances to non-reachable variables are fixed to a suficiently large value, defined by a maximum distance constant M:

$$
E D (i) = \frac {1}{n} \sum_ {j = 1} ^ {n} d (i, j), \forall i \neq j,\tag{1}
$$

where $d ( i , j ) = M$ when there is not any path between variables i and j of the branding model.

Once the ED metric is calculated for all the variables of the branding system, the detection algorithm ranks them in ascending order.

Later, the algorithm sets a threshold to only return a subset of the variables with the highest rank and only those variables with a metric value below this threshold are returned to the DSS user. The calculation of the threshold is based on the best and worst quality metric values, $E D _ { m i n }$ and $E D _ { m a x }$ respectively. Mathematically, a variable i of the system is selected as a key variable if and only if:

$$
E D (i) \leq \alpha (E D _ {m a x} - E D _ {m i n}) + E D _ {m i n},
$$

where a is a user parameter to restrict the size of the set of key variables. When $\alpha = 0 ,$ , only the highest-ranked variable is returned.

## 4.3. Validation module

One of the decisive and iterative steps when modeling with system dynamics is model validation and testing [37]. The validation of non-linear models for real-world problems such as those created by Identimod is not straightforward, and can be seen as a learning process where the modelers’ understanding is enhanced through their interaction with the formal and mental models. As models are used, they are adapted as a function of feedback from the real world [45], and as they are tested, modelers fit them to the properties of the phenomenon to be modeled. We include two main validation tools in Identimod to assist modelers in validating their branding systems: first, an automated calibration engine based on genetic algorithms (GAs) [7] (Section 4.3.1), and second, an automated sensitivity analysis [37, 42] that assesses changes of the model behavior given a systematic variation of input parameters (Section 4.3.2).

## 4.3.1. Automatic calibration of the system effects

Model calibration is the process of estimating the model parameters to obtain a match between observed and simulated structures and behaviors [37, 43]. Automated calibration is a useful tool for model validation that is mainly based on gradient search and soft computing methods such as evolutionary algorithms [7]. This calibration process can be seen as an optimization problem where the optimal values of the model parameters are searched for by comparing the outputs of the model with historical data [37].

Identimod offers a calibration tool to select both the objective variables that fit their historical trends and the effects (i.e., their intensities) to be calibrated. Within this calibration tool we can manually select the effects to calibrate or to choose a complete effects calibration where all the system effects are adjusted by the calibration method at once. This module of the DSS also shows the temporal evolution of the selected variables to be calibrated (before and after calibrating) together with their historical trends as well as a numerical deviation measure.

Methodologically, GAs are one of the most-used optimization methods to calibrate non-linear models [16]. Miller [33] was the first to use GAs for model calibration as they provide a more powerful search than classical methods and show some additional advantages, in particular their capability to explore wider ranges of parameters and parameter settings (with a higher resolution), as well as to consider potentially non-linear interactions between those parameters [46]. Therefore, we use a GA as the calibration engine of Identimod to automatically adjust the parameters of the effects with the goal of tuning some objective variable trends.

Specifically, Identimod uses a generational GA with a population of 100 chromosomes, a k-tournament selection mechanism $( k = 3 ) ,$ and a stopping criteria of 20,000 chromosome evaluations. The GA design has weak elitism, i.e., the best chromosome is always preserved at every generation, and uses a single-objective fitness function which evaluates how good a chromosome (solution) is by measuring the Euclidean distance between the branding variable model’s output and the available empirical data (model fitting).<sup>1</sup> The chromosomes are integer-based and have a fixed length where their genes’ values are subject to the interval-based constraints of the decision variables (effect parameters to be calibrated). During its execution, all the feasible values $\nu _ { i }$ of an effect parameter i can be assigned to the i -th gene of the chromosome.

The GA initialization of the chromosome consists of creating a list of possible values for each gene and selecting one of them uniformly at random. The crossover operator is applied with a probability $p _ { c } = 1 .$ It generates two offspring from two chromosome parents by combining genes using a modified version of the BLX-a real-coded crossover operator [21], which is adapted for an integer representation scheme. The crossover operator truncates the selected values over the gene set of feasible values after randomly selecting the new value from interval $[ c _ { m i n } - I \alpha , c _ { m a x } + I \alpha ]$ , where $c _ { m a x } = m a x \left( \boldsymbol { \nu } _ { i } ^ { 1 } , \boldsymbol { \nu } _ { i } ^ { 2 } \right)$ $c _ { m i n } = m i n \ : ( \nu _ { i } ^ { 1 } , \nu _ { i } ^ { 2 } )$ and $I = c _ { m a x } - c _ { m i n } .$ v<sup>1</sup> and $\nu _ { i } ^ { 2 }$ are the feasible decoded values from the genes of the parents. The variable a is the exploration parameter of the operator and is set to 0.5. Additionally, the mutation operator mutates the genes of the chromosomes of the population by a probability $p _ { m } = 0 . 1$ (per gene). If a gene is to be mutated, the operator generates a new value for it by running a uniform random distribution over the feasible values of its corresponding model parameter.

## 4.3.2. Sensitivity analysis and condition tests

Sensitivity analysis reveals those parameters to which the model behavior is highly sensitive [42]. Together with calibration, sensitivity analysis is crucial to further validate the model by exploring its sensitivity to a particular set of parameter values and inputs [37], being key ingredients of the quality of a model-based study [42]. Despite its importance, sensitivity analysis is a practice that is often ignored by practitioners. Moreover, it often covers only a few parameters or it neglects potential non-linear interactions between parameters when it is performed [46].

Identimod incorporates a tool for running sensitivity analysis in which the modeler can see potential non-linear interactions among a large number of parameters. It is thus possible to determine the confidence intervals for the parameter estimates by performing direct sensitivity analysis. In some models we can only observe the best behavior when parameter ranges are constrained to very specific configurations, but the sensitivity tool of Identimod can run several changes in variables and ease the observation of the results when simulating the branding system. Finally, Identimod also allows the modeler to run another structural validity test, called extreme condition tests [40]. Such tests involve setting the majority of the variables to their medium values and some of them to either their maximum or minimum values. By simulating the model under these conditions we can compare the output with the expected behavior of the brand.

## 4.4. Utilization module

A simulation engine is needed to assist marketers in making a better decision as soon as the model behavior passes the validation process. Its aim is to understand the effects of what-if scenarios and apply new marketing strategies through the definition of strategic actions. To set up a simulation, Identimod initially considers the model built by the graph of variables with interconnected effects and user-defined initial conditions such as the simulation length (in months), the period of time of the strategy as well as initial conditions of the scenario. The modeler can freely modify the scenario to focus their analysis on partial scenarios of the global branding system.

Identimod offers a graphical interface to change the initial conditions of the scenario, simulate the branding system, and observe the simulation outputs. Additionally, marketers and modelers can specify a management strategy to be applied to the current scenario by the definition of a set of strategic actions. Every action, assigned to a variable of the defined scenario, should be defined on an “actionable” variable (unlocked). The screenshot of Fig. 4 shows the components of an Identimod simulation with user-defined branding strategies.

In addition to the period of time for its application, the strategy includes a list of actions to be applied to the selected variables of the scenario. The user of the DSS can define the change in the variable and how this change is implemented during the simulation if: a) there is a delay in its application, b) the total change in the variable is split up into different changes by cycles, and c) there are application restrictions with respect to the variable value limits and the period of time of the strategy. The list of defined marketing actions for the scenario is always editable and visible from the simulation view (strategy section in the screenshot of Fig. 4). In the next sub-sections we will explain how Identimod internally manages the simulations.

## 4.4.1. Pre-processing the simulation

The output of a simulation is an array of the state of the N variables for all the months of the simulation scenario (M). For each step of the simulation (each month m) and after applying the input effects on variable v<sup>i</sup>, Identimod needs to calculate the updated value of the variable, $\nu _ { m } ^ { i } ,$ from the previous step value $\nu _ { m - 1 } ^ { i } .$ . When the current step m finishes, all the input effect changes on variable v<sup>i</sup> are applied synchronously to obtain ${ \nu _ { m } ^ { i } . ^ { 2 } }$

The first step of the simulation engine is to get the active variables and effects (only active items are received as inputs by the simulation engine) of the scenario as inputs and pre-process the list of effects and strategies. The internal infrastructure of the list of effects is based on a queue policy; for instance, when an effect has a delay, the engine pre-computes the effect updates by setting its change to the queue for future application after the specified months of delay. For each active effect, Identimod creates a complete mapping correspondence between all the values of the source and target variables by using four linear functions between the four consecutive pairs of linguistic terms from the fuzzy effect editor.

## 4.4.2. Application of strategic actions

When a simulation contains strategic actions, these actions are assigned to the queue of temporal events. Generally, all the updates given by strategic actions are also pre-computed during the preprocessing stage to be applied at the corresponding month. These updates are stored as an absolute change in value without taking into account any other change produced by the graph of effects or by the random behavior of the variables.

The simplest action is a variable change which has neither delay nor cycle; i.e., it is atomic and immediately applied at the beginning of the simulation. However a strategic action can be extended with a delay and/or a cycle. The value of the delay in a strategic action defines the month when the action is applied for the first time. As said, when there is no delay, strategic actions are applied between months 0 and 1; but an action with a delay of d months is applied between months d and $d + 1$ . The maximum delay must be strictly lower than total strategy length $( S _ { l e n g t h } )$ ).

![](/api/attachments/9HCN5WQU/fulltext/images/7eaf308f5814995a8602fbdb2cb765123a65485228b784ccdc2f1311768f3068.jpg)  
Fig. 4. Causal diagram and simulation view. The graphical interface shows the simulation output and a list of the strategic actions to be applied when simulating the branding system.

The other temporal factor of a strategic action is the cycle, which determines if the value update is applied in a single round, monthly, quarterly, or biannually. If the action is cyclic, the change in the strategic action variable is then evenly distributed as partial updates with respect to this cycle. By default, the partial updates to reach the desired value of the actionable variable are computed and limited to the total strategy length $S _ { l e n g t h }$ minus the specified delay, if it exists. However, the modeler can specify if a cyclic action can exceed the strategy period of time (see the corresponding option in the action dialog in Fig. 4).

## 4.4.3. Effect propagation and output generation

Once the previous steps are finished, the simulation engine starts a loop to iterate all the months sequentially. Starting with the values of the variables in the previous month $\nu _ { m - 1 } ^ { i } \left( \nu _ { 0 } ^ { i } \right.$ in the case of the first month), the simulation engine performs the following three steps for each of the M months of the simulation:

1. Application of the pre-processed strategic actions. These actions modify the corresponding variables by changing their values according to the strategic action rules.

2. Random noise generation for variables with a random behavior. A random noise generator performs two decisions in a random variable. Both of them depend on the randomness weight of the variable $\omega ^ { i } \in ( 0 , 1 ] ,$ , defined by the DSS user in the variable editor, as shown in Section 4.1.1. First, the generator decides whether or not the noise should be applied at the current month. The randomness weight y<sup>i</sup> is used as a threshold of a uniform random distribution for the decision to apply the random noise to variable v<sup>i</sup> at month m. If the decision is positive, the noise is computed and the random weight y<sup>i</sup> of the variable also influences how strong the random noise is. We use a normal distribution with mean $\mu = 0$ and standard deviation $\sigma ^ { i } = M A X _ { n o i s e } * \omega ^ { i }$ to change the value of the variable; where $M A X _ { n o i s e }$ was empirically set to 0.1 to specify a maximum possible 10% noise variable perturbation at each month m.

3. Application of the effects. An effect is computationally defined by the interpolated functions from the five slider values and its fuzzy intensity (Fig. 3). Each effect computes the change in the target values, taking into account the value of the source variable. All the effect changes are applied independently and use absolute changes to the target variable.

## 5. Application to a branding case of a seafood company

Our case study involves a Spanish seafood company that produces and sells fish and seafood products (e.g., elver and surimi). Even though the seafood products offered by the company had a good reputation and perceived quality by customers, the awareness of the main company brand was not high. Marketers wanted to evaluate three different options: a) keep the current brand image for all the offered products, b) re-brand and create a new image for the whole portfolio, and c) re-style the current brand image of the company. We used a brand architecture called brand relationship spectrum [3] for the definition of the system and scenarios. This methodology helps marketers create and evaluate coherent and effective brand architectures with sub-brands, endorsed brands, and other alternatives.

## 5.1. Generation module: identifying the variables and their effects

After studying the current branding state and the goals of the case study with the managers and stakeholders of the company, we collected all the available data. Five data sources provided by the company were used to identify and define the set of variables:

D1: Spanish seafood brand monitoring and research provided by an independent consulting company. This research contains quantitative and qualitative studies. They run eight panel groups in groups of two customers and in six different Spanish locations for the qualitative study. For the brand health quantitative study, they ran 1600 on-line interviews of 15 min in 2015 and 2016.

D2: Report with brands’ annual sales of the seafood sector in Spain in 2015 and 2016.

D3: Media and ad monitoring from an independent consulting agency.

D4: Internal reports and expert knowledge from stakeholders about the brand situation and creative quality of the brand.

D5: Kantar World Panel about seafood products manufactured by the company.

We used Identimod to define the set and to discuss with marketers the branding variables that are applicable to this specific case. Fig. 5 shows a diagram with the agreed 23 variables together with their definition, current linguistic values, and the data source used to model and define them. Our case study model uses all 23 variables, which are also related to the set of five brand equity components defined by Aaker [1]: brand loyalty, brand awareness, perceived quality, brand associations, and other proprietary assets (e.g., competitive advantage).

Fig. 6 shows the causal diagram (with nodes and names in two views) of the seafood company case with 23 variables and 47 direct and inverse effects. Direct effects are represented by continuous arrows and inverse effects by dashed arrows. Each node of the graph (variable of the branding system) is also colored according to its current linguistic value.

## 5.2. Diagnostics module: feedback loops and key variables

The diagnostics user interface shows the feedback analysis for the seafood company system. This case study has 129 feedback loops, composed of 72 balancing and 57 reinforcing. It means the case is stable (s = 0.1162) as there are more balancing than reinforcing loops. The model is adequately self-organized because the number of feedback loops is almost the double of the number of variables (k = 5.6086). When the general analysis of the system is done, the modeler must examine the feedback loops and the variables involved. For instance, we see that variables Brand extension and Brand strength are involved in more than 100 feedback loops each, and this set has more balancing than reinforcing feedback loops. This fact means that these variables are central in the model and well connected to the whole system. More importantly, it is not easy to change their value as they correspond to a lot of balancing feedback loops and are regulated through the dynamics of the branding system. In general, as happened for this case, increasing the brand strength needs time to show its strength in a competitive situation (i.e., market share, perceived leadership, and price premium) [23].

The Name of the brand and Brand vision variables are the key variables returned by the automatic detection algorithm of Identimod, and were assigned values of 5.6818 and 6.9545, respectively. The importance of the first variable resides in its direct and rapid connection to central branding variables such as Personality, Authenticity, Brand image and Brand afinity. The second key variable, Brand vision, has direct effects to Brand positioning, Brand extension and Brand elasticity. Both key variables are related to the brand equity of the company and have easy access to the central variables and high indegree. The key variable analysis also shows that this set of variables

![](/api/attachments/9HCN5WQU/fulltext/images/ed73bd42611a1fa386e1db770cc825b7c77e680834953d68b8bfe2de8b459663.jpg)  
Data sources used for defining the variables:  
Color of current linguistic value of the variables denotes distance to its optimal value (from far to close).

(quantitative and qualitative studies from independent consultancy).

D2: Annual sales report of the sector in Spain.

D3: Media and ads monitoring (independent consultancy).

D4: Internal reports and expert knowledge from stakeholders.

Fig. 5. List of the identified variables of the seafood company case. Source data and current value of the variables are included in the diagram.

D5: Kantar World Panel about fish products and its sector could be good candidates for performing strategic actions to obtain quick changes in the system. Generally in Identimod, the key variable diagnostic tool can also help modelers detect inconsistencies in the model, because the key variables of the model might match the key aspects of the brand reality of the case. Once detected, the model can be further refined through the iterative modeling process.

![](/api/attachments/9HCN5WQU/fulltext/images/454f8f54ab23afc6e95bb03f3aa1b0c3b4098621f602ece42beaa9cc2f385627.jpg)  
Fig. 6. Structure of the seafood company model using Identimod in two views: one with graph nodes (left) and other with variable names (right)

## 5.3. Validation module: replicating historical brand trends

Product image (13), Brand image (14), and Brand awareness (15) are the objective variables with historical data selected to calibrate the system. In the case of these variables, historical data for the Product image was obtained from Kantar World Panel on fish products in Spain (data source D5), and historical data for Brand image and Brand awareness was collected from the qualitative and quantitative brand tracking studies of an independent company (data source D1). Additionally, the objective variables to be fitted must be involved in the most important dynamics of the system to modify their value when the genetic algorithm (GA) automatically adjusts the effects of the system. The feedback analysis of the diagnostics module can be used to identify those variables involved in a high number of feedback loops.

By running the GA algorithm of the calibration tool, the three objective variables achieve a combined fitting value of 96.2% (98.1% for variable Product image, 95.9% for Brand image, and 94.6% for Brand awareness). This is done by adjusting the parameters of the effects that have low confidence for modelers and marketers, however, the use of the calibration tool must be iterative since the modeler must also determine if the dynamics and trends of the variables are correct. Although the automated calibration is a useful tool for modeling this kind of system, the calibration results should be analyzed with caution [37]. The modeler must carefully analyze the calibration results, check the entire model, and study if it is possible to better fit the historical trend by modifying the system or if it is an acceptable calibration for the model. When the DSS user is satisfied with the calibration results, they can consolidate the modified model parameters to be used in the iterative Identimod modeling process.

Fig. 7 shows a screenshot of a sensitivity analysis for the case, where the modeler is able to test variable changes to an independent variable (Leadership) and the final simulation effects on the dependent variable (Competitive advantages). In this example, we observe how the results are logical; when Leadership is decreasing, the Competitive advantages of the fish products brand with respect to competitors decreases as it also affects the Brand positioning (variable 9). When running the analysis, the rest of the model and its variables keep their values, then the modeler must analyze the sensitivity analysis results and see if the impact, sign of the change, and speed of change are appropriate.

## 5.4. Utilization module: evaluating three branding strategies

Managers of the company wanted to know the best option to establish a house of brands [3] for their portfolio of products. They defined three main strategies: a) keep the current brand image, b) rebrand the company, and c) restyle the current brand. In order to accomplish this set of scenarios in Identimod we defined the three simulation scenarios for a time span of four years. We also defined the needed strategic actions for each scenario as having a strategy duration of one year. The strategic actions are applied to a set of six linguistic model variables depending on the scenario. These actions are shown in Table 1.

Performing a rebranding of the seafood company directly implies the brand awareness fall to a zero value (variable 15, Brand awareness). Then, it is necessary to increase the customers’ awareness by marketing and advertisement campaigns. In the case of a re-styling, the brand awareness fall is less important. For all the three scenarios we define the same costs for the marketing campaign by including a strategic action to variable Ad investment that increases its linguistic value to High (i.e., 1,5 million euros). Also, the action for the design of the packaging (increase variable Packaging design to Attractive) is equal for the three scenarios because of the lack of differences in keeping, rebranding, or re-styling the company. Finally, strategic actions on Personality, Name of the brand, and Brand identity codes differ on the three scenarios as both rebranding and re-styling look to increase and change the current brand values. However, when rebranding the company, the new linguistic values of these three variables are closer to their optima.

Fig. 8 shows the simulation outputs in Identimod for the evolution of variables Brand image, Brand awareness, Purchase consideration, and Brand extension when applying the set of strategic actions for keeping the brand (left image) and rebranding it (right image). We can see how the ad investment quickly increases the value of the Brand awareness with the current brand (plot on the left of the image). We can also see how the branding system increases the values of Brand image and Purchase consideration when the awareness variable is above 75% of its optimum value.

![](/api/attachments/9HCN5WQU/fulltext/images/68ea4c4d3e8c5934b266a8fa5a11c2fc0dad7cc01122bc1fdb00bf8e58fbd85b.jpg)  
Fig. 7. Sensitivity analysis in Identimod for the seafood company case. This window shows the evolution of Competitive advantages when different actions are performed on Leadership.

In the marketing scenario of totally rebranding the company (right plot of Fig. 8), changing the awareness of the brand from a very low value is dificult even with high ad investment from the company. The reset of the obtained brand awareness by rebranding the company penalizes the values of the Brand image and Purchase consideration during the four-year simulation.

Fig. 9 shows the same plots for comparing the current brand scenario and a re-styling of the brand. In the case of re-styling the brand, there is a decrease on the brand awareness (variable 15) and its value is recovered after one year of ad investment (represented by a vertical blue line on the graph). The same applies for Brand image and Purchase consideration which only improve their values after one year. The influence of the brand in terms of Purchase consideration is also slightly better when keeping the current brand with respect to a brand re-styling.

To sum up, the simulations and strategic actions on what-if scenarios in Identimod suggested that, for this validated case study, the most recommendable strategy is to keep the current brand and only act on less internal branding variables such as Personality (e.g., value, mission), Brand identity codes (e.g., colors, fonts, icons), and an improvement on the Packaging design. In a four year time span, a focus on a deeper branding change is not worth the investment. However, a re-styling of the brand could also be positive for the company in a longer term scenario, since it seems to reinforce the Brand image and Brand awareness of the seafood company.

## 6. Final discussion and future work

In this paper we have proposed Identimod, a new methodology and DSS to model branding problems. Identimod is based on soft computing and Vester’s sensitivity model (VSM) which are appropriate techniques to deal with the intangible variables, uncertainty, linguistic terms, and the complexity that can be found in this type of managerial problem. This paper does not just present the DSS but provides the complete modeling process for branding, divided into four different modules. These modules range from the initial identification of the intangible fuzzy variables to the utilization of the final validated model by marketers and decision makers.

We highlighted the importance of involving stakeholders in the brand modeling for its acceptance, and Identimod is therefore designed to support the stakeholders’ discussion and the model agreement in a participatory modeling process through the stages of the four modules. These modules follow an iterative and cyclic process needed to create, diagnose, validate, and simulate branding applications. The DSS incorporates the linguistic definition of variables and effects, along with visual graphs and straightforward simulation tools. In addition, Identimod provides the modeler with specific tools for studying the structure of the model and validating it by means of automatic methods. These methods also represent novel applications of advanced computational techniques; for instance, genetic algorithms (GAs) for automatic calibration of VSM, and social network analysis metrics for key variable detection.

Strategic actions on the linguistic branding variables for the three scenarios.

<table><tr><td>Variable</td><td>Keep brand image</td><td>Rebrand the company</td><td>Restyle the company</td></tr><tr><td>(3) Personality</td><td>Slightly increase above Generic</td><td>Increase to Very defined</td><td>Increase to Defined</td></tr><tr><td>(4) Name of the brand</td><td>N/A</td><td>Move to Symbolic</td><td>Move to Toponymic</td></tr><tr><td>(15) Brand awareness</td><td>N/A</td><td>Decrease to Very low</td><td>Decrease to Medium low</td></tr><tr><td>(18) Ad investment</td><td></td><td>Ad investment to High from Very low</td><td></td></tr><tr><td>(19) Brand identity codes</td><td>Slightly increase above Low differentiation</td><td>Increase to Very distinguishable</td><td>Increase to Distinguishable</td></tr><tr><td>(20) Packaging design</td><td></td><td>Increase design up to Attractive</td><td></td></tr></table>

![](/api/attachments/9HCN5WQU/fulltext/images/394b33bb162a09f8ac09971c2c5fa16a2adf486f56da9a1385cc7083fd268df8.jpg)  
Fig. 8. Identimod simulation outputs a list of strategic actions when comparing the current scenario (left image) and a rebranding strategy (right image).

We applied Identimod to the branding problem and to marketing data from a seafood company in Spain. The case demonstrated that, by using Identimod, marketers are able to answer some of the most important and dificult questions of the branding problem of an organization [25]. Some of the questions that can be analyzed by Identimod for real branding problems are:

How stable is the brand equity of the organization?

How does the effectiveness of marketing drivers of brand equity change over time?

Which attributes of the product are the most stable and beneficial for a brand over time?

What is the relative impact of company actions, agents, and customers on brand equity?

The managerial benefits of Identimod are clear. The DSS helps modelers defend their model with the different stakeholders of the firm. As pointed out by Voinov and Bousquet [51], only by including stakeholders and managers within the modeling phase can we ensure the results’ adoption. Stakeholders and marketers are also able to learn about the interactions within their system and likely consequences of their decisions when using a type of DSS like Identimod. Another managerial benefit of Identimod is its intensive use of validation tools and diagnostics, which increases the model confidence level and thus facilitates its adoption by decision makers. To our knowledge, this is the first DSS for branding problems that put emphasis on the stated key aspects.

![](/api/attachments/9HCN5WQU/fulltext/images/7c0fbcf446f635ed7701a2f7e3168a49471d3fbf975a885d2ffe3c50ab16abfa.jpg)  
Fig. 9. Identimod simulation outputs and list of strategic actions when comparing the current scenario (left image) and a re-styling strategy (right image).

However, the presented work has some limitations. Although Identimod works with fuzzy variables and effects, the internal simulation engine does not use fuzzy reasoning but instead precise values. One future improvement is to work on the simulation engine of Identimod by considering more sophisticated simulations based on fuzzy logic. Additionally, the utilization module of Identimod is lacking automatic methods, which would reduce modeler efforts. Along these same lines, an optimization method based on soft computing and evolutionary algorithms, able to find the best branding strategy in an automatic way, could add more value to the DSS. The stated automatic strategy generator could also incorporate the specific costs of the different marketing actions to provide managers with a DSS that can balance the benefits of the strategic actions and their implementation costs.

## Acknowledgments

This work has been supported by RØD Brand Consultants (ZIO research contract) and the Spanish Ministerio de Economía y Competitividad under NEWSOCO project (ref. TIN2015-67661), including European Regional Development Funds (ERDF). We also thank José Barranquero (jose.barranquero@novelti.io) for his software development.

## References

[1] D.A. Aaker, Managing Brand Equity the Free Press, NY, New York, 1991.

[2] D.A. Aaker, Measuring brand equity across products and markets, California Management Review 38 (1996) 102–120.

[3] D.A. Aaker, E. Joachimsthaler, The brand relationship spectrum: the key to the brand architecture challenge, California Management Review 42 (2000) 8–23.

[4] M.D. Ahmed, D. Sundaram, Sustainability modelling and reporting: from roadmap to implementation, Decision Support Systems 53 (2012) 611–624.

[5] G. Alexouda, A user-friendly marketing decision support system for the product line design using evolutionary algorithms, Decision Support Systems 38 (2005) 495–509.

[6] R. Babuška, Fuzzy modeling for control, vol.12. Springer Science & Business Media. 2012

[7] T. Back, D.B. Fogel, Z. Michalewicz, Handbook of Evolutionary Computation, IOP Publishing Ltd., Bristol (UK), 1997.

[8] J. Barranquero, M. Chica, O. Cordón, S. Damas, Detecting key variables in system dynamicsmodellingbyusingsocialnetworkmetrics,in:F.Amblard,F.J.Miguel,A. Blanchet, B. Gaudou (Eds.), Advances in Artificial Economics, Lect. Notes in Econ. and Math. Syst. vol. 676, Springer International Publishing. 2015, pp. 207–217.

[9] P.P. Bonissone, Soft computing: the convergence of emerging reasoning technologies. Soft computing-A fusion of foundations, Methodologies and Applications 1 (1997) 6–18.

[10] P.I. Carrington, I. Scott, Wasserman, Models and methods in social network analysis. Cambridge University Press, S., 2010.

[11] S.Chan,W.Ip,Adynamicdecisionsupportsystemtopredictthevalueofcustomer for new product development, Decision Support Systems 52 (2011) 178–188.

[12] O.Cordón,F.Herrera,Identificationoflinguisticfuzzymodelsbymeansofgenet algorithms, Fuzzy Model Identification, Springer. 1997, pp. 215–250. in:.

[13] E. Crescitelli, J.B. Figueiredo, Brand equity evolution: a system dynamics model, Brazilian Administration Review 6(2009) 101-117

[14] A. Crespo, C. Blanchar, A decision support system for evaluating operations investments in high-technology business, Decision Support Systems 41 (2006) 472–487.

[15] P. Crossland, Value creation in fine arts: a system dynamics model of inverse demand and information cascades, Strategic Management Journal 23 (2002) 417–434.

[16] C Eksin, Genetic algorithms for multi-obiective optimization in dynamic systems Proceedings of the 26Th International System Dynamics Conference 2008

[17] J.W. Forrester, Industrial Dynamics, MIT Press. 1961.

[18] A. Gani,A. Groessler, Linking brand equity and customer equity: a system dynamics perspective, Proceedings of the 32nd International Conference of the System Dynamics Society, Delft, Netherlands, 2014.

[19] D.E. Goldberg, Genetic algorithms in search, Optimization andMachine Learning, Addison-Wesley Publishing. 1989,

[20] P. Guo, w. Pedrycz, Human-centric Decision-making Models for Social Sciences, Springer. 2014

[21] F. Herrera, M. Lozano, J.L. Verdegay, Tackling real-coded genetic algorithms: operators and tools for behavioural analysis, Artificial Intelligence Review 12 (1998) 265–319.

[22] S.L. Huang, C.T. Yeh, W.W. Budd, L.L. Chen, A sensitivity model (SM) approach to analyze urban development in Taiwan based on sustainability indicators, Environmental Impact Assessment Review 29 (2009) 116–125.

[23] J.N. Kapferer, The New Strategic Brand Management: Advanced Insights and Strategic Thinking, Kogan Page Publishers. 2012.

[24] F.O. Karray, C. De Silva, Soft Computing and Intelligent Systems Design: Theory, Tools, and Applications, 2004.

[25] K.L. Keller, D.R. Lehmann, Brands and branding: research findings and future priorities, Marketing Science 25 (2006) 740–759.

[26] K.L. Keller, M. Parameswaran, I. Jacob, Strategic brand management, Building, Measuring, and Managing Brand Equity, Pearson Education India, 2011.

[27] C.W. Kirkwood, System Dynamics Methods, College of Business Arizona State University USA. 1998.

[28] C.Kiss,M.Bichler,Identificationofinfluencers—measuringinfluenceincustomer networks, Decision Support Systems 46 (2008) 233–253.

[29] K.C. Lee, H. Lee, N. Lee, J. Lim, An agent-based fuzzy cognitive map approach to the strategic marketing planning for industrial firms, Industrial Marketing Management 42 (2013) 552–563.

[30] S. Li, B. Davies, J. Edwards, R. Kinman, Y. Duan, Integrating group Delphi, fuzzy logic and expert systems for marketing strategy development: the hybridisation and its effectiveness, Marketing Intelligence & Planning 20 (2002) 273–284.

[31] S. Li, R. Kinman, Y. Duan, J.S. Edwards, Computer-based support for marketing strategy development, European Journal of Marketing 34 (2000) 551–575.

[32] L. Martínez, D. Ruan, F. Herrera, Computing with words in decision support systems: an overview on models and applications, International Journal of Computational Intelligence Systems 3 (2010) 382–395.

[33] J.H. Miller, Active nonlinear tests (ANTs) of complex simulation models, Management Science 44 (1998) 820–830.

[34] B.K. Mohanty, B. Bhasker, Product classification in the internet business — a fuzzy approach, Decision Support Systems 38 (2005) 611–619.

[35] J. Morente-Molinera, R. Wikström, E. Herrera-Viedma, C. Carlsson, A linguistic mobile decision support system based on fuzzy ontology to facilitate knowledge mobilization, Decision Support Systems 81 (2016) 66–75.

[36] A. Mukherjee, R. Roy, A system dynamic model of management of a television game show, Journal of Modelling in Management 1 (2006) 95–115.

[37] R. Oliva, Model calibration as a testing strategy for system dynamics models, European Journal of Operational Research 151 (2003) 552–568.

[38] R. Oliva, Model structure analysis through graph theory: partition heuristics and feedback structure decomposition, System Dynamics Review 20 (2004) 313–336.

[39] H. Qudrat-Ullah, On the validation of system dynamics type simulation models Telecommunication Systems 51 (2012)159–166

[40] H. Qudrat-Ullah, B.S. Seong, How to do structural validity of a system dynamics type simulation model: the case of an energy policy model, Energy Policy 38 (2010) 2216–2224.

[41] G.P. Richardson, P. Otto, Applications of system dynamics in marketing: editorial, Journal of Business Research 61 (2008) 1099–1101.

[42] A. Saltelli, M. Ratto, T. Andres, F. Campolongo, J. Cariboni, D. Gatelli, M. Saisana, S. Tarantola, Global Sensitivity Analysis: The Primer, John Wiley & Sons. 2008.

[43] R.G. Sargent, Verification and Validation of simulation models, In: Proceedings of the 37th Conference on Winter Simulation, 2005. pp. 130–143. pp.

[44] K. Schianetz, L. Kavanagh, Sustainability indicators for tourism destinations: a complex adaptive systems approachusing systemic indicator systems Journal of Sustainable Tourism 16 (2008) 601–628.

[45] J.D. Sterman, Business Dynamics: Systems Thinking and Modeling for a Complex World Irwin-McGraw-Hill New York 2000

[46] F. Stonedahl, U. Wilensky, Evolutionary robustness checking in the artificial Anasazi model, Proceedings of the AAAI Fall Symposium on Complex Adaptive Systems: Resilience, Robustness, and Evolvability, 2010. pp. 120–129.

[47] A.A. Tako, S. Robinson, The application of discrete event simulation and system dynamics in the logistics and supply chain context, Decision Support Systems 52 (2012) 802–815.

[48] J.C. Tiernan, An eficient search algorithm to find the elementary circuits of a graph, Communications of the ACM 13 (1970) 722–726.

[49] F. Vester, The biocybernetic approach as a basis for planning our environment, Systems Practice 1(1988) 399–413

[50] V.F., The Art of Interconnected Thinking: Tools and Concepts for a New Approach to Tackling Complexity, MCB Verlag. 2007.

[51] A. Voinov, F. Bousquet, Modelling with stakeholders, Environmental Modelling & Software 25 (2010) 1268–1281.

[52] L.A. Zadeh, Fuzzy sets, Information and Control 8 (1965) 338–353.

[53] L.A. Zadeh, From computing with numbers to computing with words. from manipulation of measurements to manipulation of perceptions JEEE Transactions on Circuits and Systems I: Fundamental Theory and Applications 46(1999) 105–119.

![](/api/attachments/9HCN5WQU/fulltext/images/e5410a642e40c72921355321db39209d6d13645944f23c6e7efb9360485f5d50.jpg)

Manuel Chica (manuel.chica.serrano@gmail.com) is deputy principal researcher at the European Centre for Soft Computing since 2012. He holds a BSc and MSc on Computer Science and a PhD degree by the University of Granada in 2011 (outstanding PhD award). His research line includes single and multi-objective evolutionary algorithms, machine learning, fuzzy logic, complex systems and agent-based modeling. His applied research contains diverse engineering and business applications such as industrial engineering, marketing, and healthcare systems. He is co-inventor of an international patent of a human–machine interface, registered in EU and US and under exploitation. In addition, he has published scientific papers in JCR-indexed journals such as Omega, Information Sciences, and the International Journal of

![](/api/attachments/9HCN5WQU/fulltext/images/2092c6db5c2c4ae7c87e5ac798e5150c31579930eec368fefef297635d7fcda8.jpg)

Production Economics. He has participated in 17 projects where he played the role of principal investigator in 11 of them. He was visiting scholar at Apple (Ireland, 2007), University of Auckland (New Zealand, 2012), University of Maryland (U.S.A., 2014) and Polytechnic of Wroclaw (Poland, 2015).

![](/api/attachments/9HCN5WQU/fulltext/images/07c91f52fdc3da188dda4d00ed2dd67d3cebdd659f0ca4411208237824db38c8.jpg)

Óscar Cordón (ocordon@decsai.ugr.es) is Full Professor at the Dept. of Computer Science and Artificial Intelli gence, University of Granada. He received his M.S. degree (1994) and his PhD (1997) in Computer Science from the same University. He was the founder and leader of this University’s Virtual Learning Center between 2001 and 2005, and he is currently the Vice-chancellor for Digital University. From 2006 to 2011 he was one of the founding researchers of the European Centre for Soft Computing, in his role of Principal Researcher, and he is still contracted as Distinguished Afiliated Researcher. He was awarded with the IEEE Computational Intelligence Society Outstanding Early Career Award in its 2011 edition, and with the Spanish National Award on Computer Science ARIT-MEL by the Spanish Computer Science Scientific Society in

![](/api/attachments/9HCN5WQU/fulltext/images/e3075811113617375a2a1dc99c4f4b06e3a140a5b2fb0e04221d5443d5961e5f.jpg)

2014. He has published around 320 peer-reviewed scientific publications (including 84 JCR-SCI-indexed journal papers, 42 in Q1), advised 16 PhD dissertations, coordinated 25 research projects and contracts (with an overall amount of 6.6M€), and he is currently Associate Editor of 11 international journals. He is also included in the 1% of most-cited researchers in the world (source: Thomson Reuters’s WoK, h index = 27).

![](/api/attachments/9HCN5WQU/fulltext/images/d68ff20ee63cd67b0d1f07bac7ebfa6b2bb4e7624232c76926ce501f210e5897.jpg)  
Valentín Iglesias (viglesias@rod.com.es) is co-founder of RØD Brand Consultants. He received his MSc on Fine Arts in 1991 (specialization in graphic design). He started his professional career in advertising and publicity as Creative Director and Brand Consultant for many international brands. For instance, he has actively participated in the brand generation of BBVA, Quiero TV, Telepizza, Union Fenosa, Amena, and Orange, among others. In 2002, he founded OficinaTresMinutos where he launched many projects for corporate branding and brand equity management. Additionally, Valentín Iglesias is professor on graphic design and interfaces at the Universidad Europea de Madrid. He has given lectures for different specializa tion courses, degrees, and conferences about brand equity and strategic management.

Sergio Damas (sdamas@ugr.es) is the Principal Researcher of the “Fuzzy-Evolutionary Applications” research unit at the European Centre for Soft Computing. Sergio Damas received the MSc and PhD in Computer Science from the University of Granada (Spain) where he was also Assistant and Associate Professor. Since 2011, Dr. Damas research interests are related to the application of Soft Computing to support the decision maker in complex and very different environments. He has published more than 100 peer-reviewed scientific publications, including more than 30 SCI-JCR-indexed papers in prestigious journals. He has participated in 30 research projects and contracts in European, National, and Regional calls. At a European level, he has been the global coordinator and the Principal Investigator of different projects.

José Mingot (jmingot@rod.com.es) is co-founder of RØD Brand Consultants. He received his MSc on Business Administration and Marketing in 1994 (ESIC, Madrid) and a BSc in Management and Economics in 1995 (University of Valencia). Since then, he has been chief marketing oficer for Kenwood (Spain and Portugal, 2000–2003), chief executive oficer for Delonghi (Portugal 2003–2005), and chief marketing oficer of the America’s Cup (2005–2007). Additionally, he was in charge of the brand equity, sponsorship and marketing management for the Volvo Ocean’s Race from 2008 to 2011.
