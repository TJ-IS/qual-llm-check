---
otero_id: 8380
otero_key: "KK3VUEWN"
title: "Flexible modelling and support of interrelated decisions"
authors: "Angela Liew; David Sundaram"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.11.016"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Flexible modelling and support of interrelated decisions

Angela Liew <sup>a,</sup>⁎, David Sundaram

<sup>a</sup> Department of Accounting and Finance, University of Auckland, New Zealand

<sup>b</sup> Department of Information Systems and Operations Management, University of Auckland, New Zealand

## a r t i c l e i n f o

## Available online 24 November 2008

Keywords: Decision support systems Decision making Models Integration of models Model management

## a b s t r a c t

Decision problems often consist of numerous smaller decisions that are aggregated and interrelated while spanning multiple domains, paradigms, and/or perspectives. Therefore, the decision making process should be structured in such a <sup>fl</sup>exible and iterative manner that enables a range of structured to unstructured decisions to be considered, built and solved in an appropriate manner. We propose and implement a framework and architecture that uses the three pillars of <sup>fl</sup>exibility in decision making (sequential, parallel, convergence, and interwoven), versatility (of paradigm and/or domain), and independence of components (value, dimension, and purpose) to support the decision making process and the entire modelling lifecycle © 2008 Elsevier B.V. All rights reserved.

## 1. Decisions and models

Decision making is undeniably an essential and vital part of the human life. A decision problem can consist of numerous smaller decisions that are interrelated together, where the results of multiple decisions can be consolidated together, or one decision can in<sup>fl</sup>uence another subsequent decision. This in<sup>fl</sup>uence can be fed as an input to a subsequent decision, or as a decisional choice for the users in determining which decision to make subsequently [28]. This bigger decision, and its smaller decisions embedded within, must be represented in a simple manner for decision makers to read, understand, and communicate with.

Each decision can be represented in the form of a model, to represent, describe and depict the decision problem and its interaction under consideration [14,22], whether it is simply an abstraction schema [29], insights to the decisions rather than mere numbers [19] actual model instance [9], or executable computer program module [29]. Each decision model can be a permanent modelling scenario which can be retrieved and included as part of a bigger scenario. Alternatively, it can be a temporary modelling scenario that is aggregated or pipelined within a bigger scenario. Such model integration treatments are subject to the discretion of users at the time of making such decisions. Even though each of these decisions may have a direct or indirect bearing on other subsequent decisions and can easily in<sup>fl</sup>uence the overall decision and conclusion, many decision making processes and systems treat these decisions as independent and unrelated. This obscures the users from seeing and discovering the true effects and in<sup>fl</sup>uence of the decision problem and its interaction under consideration, whether they are interrelated and/ or interdependent. The element of interdependence may not be discovered until the full picture can be seen and assessed.

Even though many decisions do occur in a sequential fashion [42], there are also many decisions that occur in parallel, evolve over time and converge to a concluding decision, or eventually combine or are interwoven into a <sup>fi</sup>nal decision [30]. Therefore, the decision making process should neither be <sup>fi</sup>xed nor predetermined beforehand so that the execution order can be created as required. Hence, modelling is an important process in understanding, capturing, representing, and solving these decision models [7,15] especially in terms of their interrelatedness across multiple models and their instances over a period of time. Furthermore such models should ideally be able to capture functional, behavioural, organisational, and informational perspectives [9].

Decision systems are intended to assist users in making a decision. There are several types of users involved in using decision systems and these users progress as they develop more con<sup>fi</sup>dence [13]: from inexperienced/naïve decision makers, to average decision makers analysts, to experienced decision makers/modellers [5,25,43]. Each type of user has different needs and should not be restricted by the constraints of any decision system that dictates the steps and techniques behind analysing and solving a decision problem.

Some users may need more decisional and/or system usage guidance [40] while others may prefer to have minimal guidance. Some may wish the decision system will take care of the entire decision making process including prescribing the order in which each set of data is requested as well as the order in which each decision model is executed; while others may wish to intervene to a greater extent in designing the entire decision making process and the execution order to suit, or to a lesser extent in specifying a particular solution method. There are a variety of reasons as to why a human intervention is warranted and needed from the perspective of an experienced user [3]. However, it is interesting to note that the type of guidance may have an adverse effect on decision model selection and ultimately the decision outcome [26].

It is unreasonable and impractical to expect decision makers to operate a different decision making system for each decision and to comprehend the full effects of the consolidation and integration from these decisions. A decision making process is not necessarily about concentrating on the decision itself, but should emphasise the ways in which decisions are made [22]. Therefore, users should be able to choose an optimising approach and solution as well as a satis<sup>fi</sup>cing approach and solution, and not be limited to only one approach and solution that is traditionally incorporated in decision systems [12,17].

Due to the frequency and complexity of interrelated decisions, some users may recall an existing scenario as input to another scenario, or recall several existing scenarios for comparative purposes. Decision systems need to be built in a <sup>fl</sup>exible way so that decision models and components can be easily assembled and/or integrated together to create new scenarios [16] and speci<sup>fi</sup>c scenarios can be built and tailored to meet the needs of particular user groups [37]. With all these issues in mind, the framework and architecture of an ideal decision system should have independent components that enable components to be easily assembled and integrated together to form a decision scenario. They should be <sup>fl</sup>exible enough to serves various types of users and accommodate various types of decision making processes. They should also be suf<sup>fi</sup>ciently versatile to handle decision problems regardless of paradigms and/or domains under consideration. Good decision making frameworks must therefore be in place for system framework and architecture to exhibit modelling <sup>fl</sup>exibility, component independence, and versatility in domain and/or paradigm.

To overcome the issues and ful<sup>fi</sup>l the requirements discussed above, we <sup>fi</sup>rst propose a converging decision analysis process, an optimising–satis<sup>fi</sup>cing decision model, and a cyclical modelling lifecycle. We then propose a Flexible Object-Oriented Decision System (FOODS) framework and architecture to support these models and processes. A widely accepted multi-methodological approach was adopted in this research to overcome the inadequacies of a single research method [36]. The hub of the research is systems development [35,36], in which systems are built on existing theories and/or past observations and experiences and are empirically validated through the building of artefacts such as computers and programs [35]. A prototypical system was therefore developed and implemented to act as a proof-of-concept to support these proposed decision making processes, framework and architecture. Object-oriented concepts such as encapsulation and inheritance were leveraged to provide independence, <sup>fl</sup>exibility, and versatility. Ideally, we would like to validate the operation of the prototype through conducting observation and evaluation among domain experts and researchers. However, the professional relevance [2] and bene<sup>fi</sup>ts obtainable from this artefact on the notion of <sup>fl</sup>exible modelling and supporting interrelated decisions make it worthwhile to explore the framework and architecture despite the lack of <sup>fi</sup>eldwork. We will concentrate our observation and evaluation on the three pillars of <sup>fl</sup>exibility in decision modelling, versatility in paradigm and/or domain, and independence in components as evaluation criteria as collated from prior research.

## 2. Normative decision making processes

Decisions can evolve and converge into a concluding decision over time. This can occur within re-evaluating a decision problem, or evaluating across multiple decision problems that are similar. This iterative decision making process is known as the convergence process [30]. As decisions evolve and re<sup>fi</sup>ne over time, decision makers are able to concentrate on essential factors and eliminate nonessential ones in order to narrow down the scope of the decision problem. Such attention-focused method provides a cut down version of the problem [24]. A decision is subsequently made from these remaining factors of the reduced problem. Such decision-focused method provides an actionable result from the given problem [24]. Since there can be many decisions within a decision problem, several iterations of attention-focused and decision-focused methods are applied while intermediate decisions within the decision problem are made and converged. Such revision and re<sup>fi</sup>nement occur irrespective of paradigms and domains. This notion of applying the attentionfocused and decision-focused methods within a convergence decision making process is depicted in Fig. 1.

One-Dimensional Cutting Stock Problem (1D-CSP) was used for illustrative purposes in order to design and implement the proposed framework and architecture. 1D-CSP is about cutting strips of raw material into desired sizes according to customer order widths. We often do not have unlimited supplies of raw materials and would therefore need to formulate and decide on which cutting patterns are used. 1D-CSP is a resource management problem with a traditional goal of minimising wastage [20]. Besides wastage, there may be other objectives that must be considered [48]. For example, minimise machine setups through the changing of cutting knives [10,23], minimise machine setups through reducing the number of cutting patterns used [23,27,47], or minimise the number of disruption in the sequence of cutting patterns used [50]. Even though 1D-CSP is considered to be a simple problem in pure mathematical terms [20,21], it becomes a reasonably complex decision problem once one considers all the real world constraints and objectives, and the interrelated decisions involved within its decision making process.

The 1D-CSP can be used as a decision problem to illustrate the converging decision analysis process, as depicted in Fig. 1. The <sup>fi</sup>rst decision is a pattern generation heuristic that generates combinations of cutting patterns. This decision concentrates only on generating those cutting patterns that are relevant to the decision problem under consideration (an attention-focused method). The second decision is determining which cutting patterns among the generated ones should be retained or discarded (a decision-focused method). This can be based on speci<sup>fi</sup>c rules such as an allowable number of cutting knives per cutting pattern. It can also be based on the decision maker's personal experience on whether certain cutting patterns should be discarded. The third decision is the creation of linear programming constraints that identi<sup>fi</sup>es the feasible area of the problem under consideration (an attention-focused method), while the fourth decision is <sup>fi</sup>nding an optimal point within the feasible area (a decision-focused method).

Neither of the focused methods has to produce an optimal or a satis<sup>fi</sup>cing solution necessarily. It is entirely up to the decision maker to decide on what sort of solution is desired at the time. Each decision and solution can be encompassed within a decision model that consists of both the optimising model and satis<sup>fi</sup>cing model, as depicted in Fig. 2. In a decision problem that consists of multiple interrelated decisions, the result from one model may be fed into another model continuously until an ultimate result is reached, and the result from a model can take on a different solution option. Each decision model may return to itself for re<sup>fi</sup>nement, or return to the previous model for additional processing, or feed to the next model for further processing. This return may be due to an infeasible solution, or a better understanding of the model which eventually leads to a change in the parameters of the model.

![](/api/attachments/KK3VUEWN/fulltext/images/14992f62d84cbd9019ea3dd9954dc2d8f95ca4b89371cf87fc4646ddcb3cb7f7.jpg)  
Fig. 1. Converging decision analysis, as in an 1D-CSP scenario.

![](/api/attachments/KK3VUEWN/fulltext/images/ae50abae54427c1fb5e7363b4bdad39a674ad4916bcb3fd199733e64132553fd.jpg)  
Fig. 2. Optimising–satis<sup>fi</sup>cing decision model.

The 1D-CSP can be used to illustrate the optimising–satis<sup>fi</sup>cing decision model, as depicted in Fig. 2. The <sup>fi</sup>rst decision model pattern generation heuristic is a satis<sup>fi</sup>cing model that produces only those cutting patterns that are relevant and desirable to the decision problem under consideration. The second decision model is also a satis<sup>fi</sup>cing model in selecting or deselecting among the cutting patterns already produced. The third and fourth decision models are optimising models that optimise using the linear programming's simplex method.

## 3. Decision modelling lifecycle

The approach of Simon [41] to the decision making process in terms of intelligence, design, and choice is very decision-oriented. However, as Golub [22] has suggested it is about the way in which we model the decision. Therefore, we propose to integrate Simon's [41] proposal with MS/OR's modelling proposals [7,14,22,29,34] that attempt to support every phase and aspects of decisions and modelling lifecycle [18]. Such a design approach is crucial to support the modelling and decision environments [45] and ensure that nonpredetermined decision making processes and interrelated decisions characteristics can be modelled.

This proposed modelling process is cyclical and iterative, and enables continuous adjustment and re<sup>fi</sup>nement especially in storing and retrieving decision problems as decision scenarios, as summarised in Fig. 3. Despite the fact that the modelling lifecycle progresses step-by-step in a cycle, it can return to any earlier steps and not just the previous one, and can skip some steps in the later iteration if it has already gone through that particular step earlier on. It is however more dif<sup>fi</sup>cult to represent these possible movements visually in the modelling lifecycle and is therefore not illustrated in Fig. 3. The lifecycle is valuable not only from the point of view of modelling the decision itself but especially for highlighting the role of the system components of the decision, whether it is a data, model, solver, or scenario. Once a problem is understood it can be represented in the form of a model which is then instantiated with data and integrated with solvers so that it can be executed. Such a model is especially bene<sup>fi</sup>cial if it is storable and retrievable for later use and comparison. Once a model is represented, a solution can be derived through analysing and investigating as well as comparing with various model instances. The derived solution is then reviewed and validated. If it is considered unsatisfactory such information can be used to modify and reformulate the decision model.

Even though the decision system will progress through the entire modelling lifecycle in producing the end result, it is important to note however that not all users will execute all the steps of the modelling lifecycle. Depending on the competencies of the decision makers and their permissions, they may interact with certain steps in the modelling lifecycle. For example, the inexperienced decision maker may interact with only step 2; the average decision maker may interact with steps 2, 3 and 4; whereas the experienced decision maker may interact with all 6 steps in the modelling lifecycle, as shown and contrasted in Fig. 4. This decision modelling lifecycle provides a sound basis for the decision support and modelling framework and architecture.

![](/api/attachments/KK3VUEWN/fulltext/images/821ae943abf21ae966518ca2ffc32ad3eb1abf44ae2b3fd0b88cd31aae6eb257.jpg)  
Fig. 3. Cyclical modelling lifecycle.

![](/api/attachments/KK3VUEWN/fulltext/images/108411d9b1c8de00ee367c88d120032043dbbd80e7d7ee202b1d93728a92be59.jpg)  
Fig. 4. Interaction between 3 types of user groups and the modelling lifecycle.

## 4. Decision support and modelling framework and architecture

## 4.1. Flexible Object-Oriented Decision System (FOODS) framework

Decision problems are often considered to be complex because the result from one decision can aggregate, pipeline, or in<sup>fl</sup>uence a subsequent decision [28]. One of the key concepts employed in the FOODS framework is the independence of decision components [17,38,39]; important object-oriented constructs such as abstraction, encapsulation, and modularity are leveraged to provide the independence of these components. It is this independence that enables the framework to handle interrelated decisions, as summarised in Fig. 5. Decision models cannot be pure abstractions [9]. They must be populated with raw data that instantiates the model, solved with some known methods/solvers through an user interface that enables users to interact with the system, and be presented with results using visualisation mechanisms. Five major decision components are thus proposed in this FOODS framework, namely, data, model, dialog, solver and visualisation, as illustrated by Fig. 6. These components are essentially system components that enable the <sup>fl</sup>exible creation of a decision system. Data is the component where the raw data is physically stored and retrieved from [43]. The model represents the problem under consideration [43]. Solver is a component that comprises a combination of known mathematical and computational methods used to generate computation results and solve a model instance [29,31]. Visualisation is a component that combines both embedded text and chart presentations [8]. Dialog is an interface template that supports language exchange and interaction between the user and the decision system [32], and is de<sup>fi</sup>ned somewhat differently from what was <sup>fi</sup>rst introduced [43]. These components possess well-de<sup>fi</sup>ned interfaces that allow us to connect, map and integrate them together to support sequential, parallel, convergent, and interwoven decision <sup>fl</sup>ows and scenarios. Such mapping and integration between components can be permanent to create scenario. They can also be temporary or ad-hoc and be accomplished through the kernel.

![](/api/attachments/KK3VUEWN/fulltext/images/54ab5afa05af5e4d57c9848753f6b54d34619368928b4af9b5728bc32e90fa6e.jpg)  
Fig. 5. Object-oriented principles and the three pillars of FOODS.

![](/api/attachments/KK3VUEWN/fulltext/images/034b7f6b20975dec535a7f7c26b7153b81a8b11d7dad73d106727e15196bebb6.jpg)  
Fig. 6. FOODS framework.

The modelling lifecycle is fundamental to model-driven decision systems as the systems need to be able to gather intelligence to formulate models, integrate models with components, solve and execute models, and be able to use the results. The independence between components enables decision systems to be versatile. Key object-oriented principles such as inheritance and modularity are also leveraged to enhance versatility, as depicted in Fig. 5. For example, different but equivalent solvers can be de<sup>fi</sup>ned as modules or components that can be used to execute the same model. Such plug and play modularity enables us to provide paradigm versatility, i.e. execution of the same model with solvers from different paradigms. These independent components map to each other [38,39] as pluggable objects [49], and are retrievable from their component pool [8] and can be integrated through the kernel for scenario execution. The kernel plays an important part in mapping and validating the components, which in turn supports the complete modelling lifecycle. In order to ensure that each component is independent from each other, generic modelling ideas and integration issues are explored and considered, such as, data–model, model– solver, solver–visualisation, data–visualisation, and data–solver independences [31,38,39].

![](/api/attachments/KK3VUEWN/fulltext/images/4504d4530e3390d7919fd84c0a1b985d133826536b977651ec806bf5ce325f48.jpg)  
Fig. 7. An example of a decision scenario that utilises the FOODS framework.

Each decision scenario calls for a different combination of components [16]. Despite the fact that the order of the decision making process must be executed in a sequential manner, the decision making process itself is not in a <sup>fi</sup>xed and prede<sup>fi</sup>ned manner. To provide such <sup>fl</sup>exibility we need to be supported by the twin pillars of independence and versatility. We also need to have components with well-de<sup>fi</sup>ned interfaces with the ability to interact through messaging and mapping, as depicted in Fig. 5. Since the result from one decision may in<sup>fl</sup>uence a subsequent decision, it is therefore important to store certain decisions as independent and permanent model instances so that they can be pipelined or consolidated as part of another decision model. The interrelated nature of decisions makes a problem less straightforward and highlights the representation and integrations of models that bring reduced cost [11], increased modelling productivity and reusability [19], facilitated growth and evolution of modelling systems, and ultimately improved managerial decisions [4,46]. Depending on the nature or condition of the problem, the existence of integration may be temporary or permanent. A combination of temporary and permanent integration will be desired if the problem consists of numerous smaller decision models. A user may decide on the suitability of the type of models at the time of execution, and the different levels of model integration enables varying spectrum of user groups to be accommodated. A user may also decide to store the output of that model permanently before feeding it into the next model or allow reformulation and recalculation to happen at each occurrence. This level of integration in terms of providing reusable model objects [37] is often not developed because it is dif<sup>fi</sup>cult to put into practice and is seldom supported by any implementation environment.

For example, a decision problem may consist of numerous decision models: M1, M2, M3, and M4. It uses components that are obtainable from the component pools as proposed in the decision support and modelling framework. This representation, in Fig. 7, helps us in modelling the overall decision problem. Each of these models can be fed individually or collectively: M1 feeds into M2 and M4; M2 feeds into M3; and M3 feeds into M4. Each of these decision models can also be integrated with other components in a temporary or permanent manner regardless of whether it is an atomic component: data, model, solver, visualisation, dialog (e.g. M4–S2–D4–M3–M1, and M3–D3– M2), or if it is a compound component: data–model–solver, data– model (e.g. M1–D2–D1), and model–solver (e.g. M2–S1). Furthermore, the decision models can be saved as a retrievable scenario for later use (e.g. Scenario 1, Scenario 2). Each of these stored scenarios can be fed into or embedded as part of another scenario (e.g. Scenario 1 feeds into Scenario 2, which in turn feeds into Scenario 3). Such an example instance shows that the proposed decision making processes and modelling lifecycle discussed earlier can be supported <sup>fl</sup>exibly through model and component integration.

## 4.2. Flexible Object-Oriented Decision System (FOODS) architecture

Traditionally, a three-tiered architecture is divided into three distinct layers: presentation, application logic, and data. However, this traditional architecture is unable to support integration well. This three-tiered architecture was subsequently modi<sup>fi</sup>ed into: presentation, integration, and component pool; where the application logic is separated into 5 elements: model, solver, mapping, validation, and scenario [8]. This modi<sup>fi</sup>ed three-tiered architecture is in line with the three levels of technologies: Speci<sup>fi</sup>c DSS, DSS Generator, and DSS Tools [44]. However, this modi<sup>fi</sup>ed architecture is still unable to support the integration of multiple decision models within a decision model. We therefore propose a new architecture with four layers which better enables the integration of components and models. These four distinct layers, namely, presentation layer, kernel integration layer, component integration layer, and component pool layer are depicted in Fig. 8.

![](/api/attachments/KK3VUEWN/fulltext/images/f0efaa35e6ae553dadd615b41c0884158c19a0cc52fa710f2f44bd937da5ee53.jpg)  
Fig. 8. FOODS architecture and its corresponding DSS tools employed.

<table><tr><td>Scenario</td><td>Routine / Non-Routine</td><td>Structured / Unstructured</td><td>Versatility</td><td>Flexibility</td></tr><tr><td>Automated</td><td>Routine</td><td>Structured</td><td>Low</td><td>Low</td></tr><tr><td>Semi-Automated</td><td>Non-Routine</td><td>Semi-Structured</td><td>Medium to High</td><td>Medium</td></tr><tr><td>Manual</td><td>Non-Routine</td><td>Unstructured</td><td>High</td><td>High</td></tr></table>

Fig. 9. Differentiating various decision scenario.

The presentation layer is the layer that communicates with the users in the form of a presentation language, and receives instructions from the users in the form of an action language [8]. The kernel integration layer is the layer that takes care of the kernel, the composition scenario of the kernel and the execution of the kernel. It holds all the components in place irrespective of the paradigms and executes in the form of a problem scenario, and hence is able to handle stored scenarios being included as an independent scenario inside a bigger scenario regardless of the domains. The component integration layer is the layer that ensures the <sup>fl</sup>exible amalgamation of multiple components. This layer focuses on component integration, model integration that occurs on an ad hoc basis until it is stored, as well as stored scenarios. The kernel and component integration layers are vital in combining the various components together and supporting the intelligence, design, choice, and implementation activities that encompass the lifecycle of decision modelling. The component pool layer manages all the <sup>fi</sup>ve different components: data, models, solvers, dialog, and visualisation [8]. There are two types of components in this layer: compound components, and atomic components. Compound components are component objects that are permanently integrated. They can be treated as stored scenario objects that are pluggable and be included as part of another bigger scenario. Atomic components can be categorised as base components that exist in most scenarios. They can be permanently integrated into a compound component and communication components that are essential if the description or results of the problem scenario is intended to be communicated with. Each component or sub-component is constructed and implemented using object-oriented concepts, is signi<sup>fi</sup>ed by an object-oriented class, and contains its own properties and functionalities.

![](/api/attachments/KK3VUEWN/fulltext/images/e1257e2c70e82798914645d283e7a02aa7982cee2ae15ff71356a3bcd7531ce9.jpg)  
Fig. 10. The modelling process of an automated 1D-CSP scenario.

<table><tr><td colspan="8">Patterns / Constraints</td></tr><tr><td></td><td>45m</td><td>36m</td><td>31m</td><td>14m</td><td>edge</td><td>chosen?</td><td>run-times</td></tr><tr><td>1</td><td>1</td><td>1</td><td></td><td>1</td><td>5</td><td>YES</td><td>97</td></tr><tr><td>2</td><td></td><td>1</td><td>2</td><td></td><td>2</td><td>YES</td><td>198</td></tr><tr><td>3</td><td></td><td>2</td><td></td><td>2</td><td>0</td><td>YES</td><td>158</td></tr></table>

Fig. 11. Display recommended patterns and its implementation solution of an automated scenario.

The proposed FOODS architecture can be illustrated using the same example instance shown in Fig. 7 that demonstrated the use of the FOODS framework. For example, the kernel integration layer holds the components M4, V, and G in place and executes it as Scenario 3 there and then, whereas the component integration layer joins either all the atomic components permanently together (e.g. M1–D1–D2), or a combination of atomic and compound components permanently (e.g. M2–M3–Scenario1) and temporarily (e.g. M4–D4–S2–Scenario2– Scenario1) together.

Through the use of the proposed FOODS architecture, a user can undertake the decision making process one phase at a time by creating smaller scenarios and integrating existing scenarios into a bigger scenario. This allows the user to have a better appreciation of the effects of a decision within the bigger context of the overall decision through the integration of multiple components and stored scenarios and irrespective of the domains. The proposed FOODS architecture also considers both the converging decision analysis and decision making processes proposed earlier and allows the entire proposed cyclical modelling lifecycle discussed earlier to be modelled.

## 5. Example instances of decisions and modelling systems

Three differing speci<sup>fi</sup>c DSS scenarios are created as examples to illustrate, assess and validate our proposals; namely automated, semiautomated, and manual scenarios. These scenarios can be applied to a spectrum of structured to unstructured and routine to non-routine decision scenarios, and are charted against the various decision scenarios in Fig. 9. They are also distinguishable from each other in the context of <sup>fl</sup>exibility and versatility.

The activities, decisions, and requests in a 1D-CSP are represented in the form of use cases [37] and are clustered accordingly to the six iterative steps proposed in the cyclical modelling lifecycle, as illustrated earlier in Fig. 3. These use cases are also categorised into <sup>fi</sup>ve groups, namely, domain, optimising, satis<sup>fi</sup>cing, utilities, and generic in each of the three example scenarios (Fig. 10 for automated, Fig. 12 for semi-automated, Figs. 14, 15, and 17 for manual). Each category usually employs its own data structure. Therefore if the decision path deviates from one category to another, mapping will occur in order to match and transpose the data requirement between the data structures of the two categories. We will walk through each of the example scenarios in the remainder of this section, and in the order from straightforward to sophisticated (i.e. fully automated to totally manual). The design of the data structures and the implementation of the prototype will be discussed brie<sup>fl</sup>y in the next section.

![](/api/attachments/KK3VUEWN/fulltext/images/5bd00401b1067f6613d0c5f211c3edfa7a10e687ec181f1e6aa9b2a7349558a8.jpg)  
Fig. 12. The modelling process of a semi-automated 1D-CSP scenario (with Scenarios A, B, and C)

## 5.1. Automated scenarios

An automated scenario is de<sup>fi</sup>ned as a model scenario in which a prescribed scenario is given and the user enters the parameters required for the domain and the system will solve and display the problem accordingly. It deals with decision situations that are structured and routine, and is designed with inexperienced decision makers in mind where high decision guidance and system usage are provided. It is also a scenario that is implemented in most commercial and research decision systems suitable for handling 1D-CSP where the decision process is <sup>fi</sup>xed and predetermined.

Fig. 10 gives an overview of the roadmap of the decision modelling lifecycle of an automated 1D-CSP scenario. The user starts the modelling process and enters the required parameters in the precise order that the system prescribes. S/he only interacts with the system about the description of the problem. The decision paths of this scenario tend to lie along the domain category, since there is no <sup>fl</sup>exibility in choosing the paradigm. Once the required data of the domain is entered, the user can solve the 1D-CSP and see the <sup>fi</sup>nal solution displayed. The user does not know the execution order or the solver used in the decision-making process and does not interfere with them. Furthermore, the user is unaware of the intermediate results that had been considered in each of the interrelated decisions. Hence s/he can only see the <sup>fi</sup>nal recommended cutting patterns and run-times rather than displaying all cutting patterns that have been considered, as shown in Fig. 11.

## 5.2. Semi-automated scenarios

A semi-automated scenario is similar to an automated scenario where a prescribed scenario is given and the user enters the parameters required for the domain and in the order prescribed. However, the user has some control over some of the decision components to use, such as solver and visualisation. It deals with decision situations that are semistructured but not routine. It is designed for users who are more experience and familiar with the decision problem and/or decision system, and where some levels of decision and system usage guidance are provided. Even though the user does not necessarily know the execution order or the intermediate results from the interrelated decisions within the decision-making process, s/he can interfere with the selection of the solver to use in the computation. It is a scenario where it is more readily implemented in research decision systems.

There are varying semi-automated scenarios in which in Scenario A the user chooses a domain solver without specifying a paradigm; a Scenario B where s/he chooses a speci<sup>fi</sup>c paradigm/solver (either an optimising solver, or a satis<sup>fi</sup>cing solver); or a Scenario C where s/he chooses a domain solver and then decides to select a particular paradigm solver to use (either an optimising solver, or a satis<sup>fi</sup>cing solver). These three slightly varying scenarios demonstrate some <sup>fl</sup>exibility where a different solver can be chosen. Such <sup>fl</sup>exibility in choosing a solver provides the versatility in dealing with any paradigm problems. The roadmap of these three varying semi-automated scenario examples are charted and shown against each other as in Fig. 12.

## 5.3. Manual scenarios

A manual scenario is de<sup>fi</sup>ned as a model scenario in which the user has the total freedom to choose any solution method and/or available solver; and to design the decision making steps and sequence to be actioned and executed. This scenario deals with decision situations that are unstructured and non-routine and were little or no decision guidance is necessary. The user is able to create any type of scenario instance using the same prototypical system, such as a 1D-CSP scenario, a pure optimising scenario (e.g. a linear programming scenario), or a satis<sup>fi</sup>cing pattern generation scenario. The user can also create a decision instance inwhich several stored scenarios are retrieved and temporarily integrated together with other components. It is designed for experienced decision makers who wish to have absolute control not only over which components to use, but also in the design of every step of the decision making process. Such notion of <sup>fl</sup>exibility is illustrated as in Fig. 13.

![](/api/attachments/KK3VUEWN/fulltext/images/7e23d01dc9dc60d4f4505139ce98871bed6f45e337719b2d4e953d283ea74bae.jpg)  
Fig. 13. Sample execution lists of manual 1D-CSP scenarios.

The fact that the user has the freedom to capture and design the problem and choose the solution methods suggests that a manual scenario is domain and paradigm independent. Hence, this scenario may appear sophisticated to manoeuvre since the users are no longer following a predetermined process, but are rather involved in the design of the process.

Even though the user wishes to have little or no decision guidance, s/he may wish to have some system guidance to avoid any failure to compute due to insuf<sup>fi</sup>cient data or incompatible data structure. The decision paths of a manual scenario tend to span across many categories since the power user can decide to follow an in-depth decision making process, and/or incorporate scenarios that have been saved and stored for later retrieval and use. It is a scenario that is rarely discussed nor implemented in any commercial or research decision systems. We will go through a manual scenario example instance that ultimately produces three decision scenarios in solving one decision problem. In doing this we also illustrate the complete decision modelling lifecycle that we proposed earlier.

5.3.1. Create Model Scenario 1 for later use

In this model scenario, we will walk through the <sup>fi</sup>rst two steps of the decision modelling lifecycle and take a simple straight forward decision path along the domain and general categories, as suggested in Fig. 14.

Step 1: Formulation of the model: the user starts the modelling process by creating a domain model instance 1D-CSP scenario.

Step 2: Instantiation of the model with data: the user continues on with the modelling process and is able to <sup>fl</sup>exibly decide on the order of entering the data as required by the domain that best suit the user. In this instance, the demand orders and their corresponding minimum quantities are entered <sup>fi</sup>rst. This is followed by the raw material availability. The user decides to save and store this Scenario 1 away for later use, so that it is easier to construct many different scenarios and compare the various computations and results.

## 5.3.2. Create Model Scenario 2 by including an existing Model Scenario 1

In this model scenario, we will walk through the complete decision modelling lifecycle and along the decision paths that span across the domain, general, and satis<sup>fi</sup>cing categories, as suggested in Fig. 15.

Step 1: Formulation of the model: the user starts the modelling process by creating a domain model instance of the 1D-CSP scenario.

Step 2: Instantiation of the model with data: the user continues on with the modelling process by recalling a previously stored scenario data, in this case Scenario 1, without having to reenter the same domain data again.

![](/api/attachments/KK3VUEWN/fulltext/images/9604f7f4853a71c975a40c1a75bd7f288d443d8a33b43a94988e13f5cf9e3713.jpg)  
Fig. 14. The modelling process of a manual 1D-CSP Scenario 1.

![](/api/attachments/KK3VUEWN/fulltext/images/0c05487dcc0bf922b339dde14bb9f64d47356f9d83bb693c1a77e4932e1540a5.jpg)  
Fig. 15. The modelling process of a manual 1D-CSP Scenario 2.

Step 3: Integration of the model with satisficing solvers: due to the fact that the user can design the decision paths once the domain data are set and ready, the user can then decide on either an optimised solution or a satis<sup>fi</sup>cing solution. In this scenario, the user selects a satis<sup>fi</sup>cing method for execution. The user may do so based on his/her personal knowledge on generating some suitable cutting patterns to start the decision making and modelling process. This domain scenario happens to be of the same type as the satis<sup>fi</sup>cing scenario and therefore minimises the need for mapping between domain and satis<sup>fi</sup>cing scenarios. Hence the user need not do any mapping between them.

Step 4: Execution of the model: once a solver is chosen the user can execute and solve the instantiated satis<sup>fi</sup>cing model.

Step 5: Analysis of the model: the user is then able to decide on the dialog and visualisation in order to view the solved solution and come to a conclusion on whether to adjust the inputs or outputs, or to continue with the recommended solution. The fact that the dialog component is independent from the model scenario suggests that the decision system can represent and solve a scenario in a versatile fashion according to its industry. Furthermore, the independence of the visualisation component means that the cutting patterns solution can be viewed in different forms, for example, in a matrix style, or a stacked bar chart. By choosing a stacked bar chart, we can visually evaluate the output quantities and wastage, as shown in Fig.16. Once the user has analysed the model, s/he may wish to return to reformulate and instantiate the model. Hence, the user returns to the start of the cycle to reformulate in the next step.

![](/api/attachments/KK3VUEWN/fulltext/images/39395cd700eba61218dcbc997c39bc248c37ddf3630be9ac7e342f8501526360.jpg)  
Fig. 16. Display all generated patterns (in stacked bar style) of a manual scenario.

Step 6: Reformulation of the model: the user uses the existing satis<sup>fi</sup>cing model instance.

Step 7: Instantiation of the model with data: as explained earlier, the user is able to interfere with and adjust the suggested model solution, rather than simply accept the computed results in a manual scenario. Therefore, the user is able to repeatedly include or discard any suggested patterns that were generated based on his/her own knowledge or experience. The narrowing and decision-oriented actions described here in this example in terms of patterns generation and selection of patterns are in line with the attention-focused and decisionfocused methods discussed earlier and as shown in the <sup>fi</sup>rst half of Fig. 1.

<sup>fl</sup>exibility also enables the user to easily construct many variations and compare the computations and results without having to re-enter all the domain data from scratch (through the integration of Model Scenario 1 at the start) and re-generate all the cutting patterns (through the integration of this Model Scenario 2 later on).

5.3.3. Create Model Scenario 3 by including existing Model Scenarios 1 and 2

Similar to the previous model scenario, we will also walk through the decision modelling lifecycle and across several categories on our decision paths, except through the optimising instead of the satis<sup>fi</sup>cing category, as suggested in Fig. 17.

Step 1: Formulation of the model: the user starts the modelling process by creating a domain model instance of the 1D-CSP scenario.

Step 2: Instantiation of the model with data: the user continues on with the modelling process by recalling the previously stored scenario data, in this case Scenario 1, without having to reenter the same domain data again. The user then enters the objective, and subsequently obtains another stored scenario data, in this case Scenario 2, to retrieve the generated and chosen cutting patterns. As mentioned earlier in Scenario 2, the domain scenario happens to be of the same type as the satis<sup>fi</sup>cing scenario and therefore no mapping is warranted.

Step 3: Integration of the model with optimising solvers: once again, the user has the freedom to design the decision paths and can interfere as well as decide on the preferred paradigm. Once all the required data are instantiated, the user can proceed to choose the necessary solver to continue with the decision making process. In this scenario, the user may choose to resolve the model instance in an optimised manner. Hence a new optimising scenario is created and the current model instance is mapped to the new optimising model. This mapping is necessary since the input models are of domain and satis<sup>fi</sup>cing models and are therefore of a different data type structure. This integration is in line with the optimising– satis<sup>fi</sup>cing decision model, as shown in Fig. 2. Once the domain and satis<sup>fi</sup>cing models are mapped to the newly created optimising model, the user can select an optimising method for execution. This optimising method <sup>fi</sup>rst concentrates on generating the relevant demand constraints given the already pre-decided cutting patterns retrieved from Scenario 2. It then decides on the best quantities of each cutting patterns from the speci<sup>fi</sup>ed objective. Such concentrating and deciding actions through the usage of the linear programming algorithm described here are in line with the attention-focused and decision-focused methods discussed earlier and as shown in the second half of Fig. 1.

Whenever the model is ready, the user is able to save and leave this Scenario 2 and progress to other activities or explorations. Such  
![](/api/attachments/KK3VUEWN/fulltext/images/3e97254db8d47b7d65849e135286f5ecae90c4ef5138049b87d562b1071aeb30.jpg)  
Fig. 17. The modelling process of a manual 1D-CSP Scenario 3.

Step 4: Execution of the optimising model: once a solver is chosen the user can execute and solve the instantiated optimising model instance.

Step 5: Integration of the optimising model with the domain solvers: in order to interpret the optimised model solution, the optimising model instance that was instantiated and solved is subsequently mapped back to a domain model instance for viewing or further processing.

Step 6: Analysis of the domain model: the user is now able to view the results that have been solved using both satis<sup>fi</sup>cing and optimising solution methods in the computation. The user can now come to a conclusion on whether to accept the recommended solution or adjust the inputs or outputs to recomputed or reformulate. The independence of the visualisation component enables the user to <sup>fl</sup>exibly choose how s/ he wishes to view the results. Therefore, the suggested quantities of each derived cutting patterns can be viewed in a matrix style as shown in Fig. 18, or in a pie chart to visually evaluate the recommended cutting patterns against its overall usage and wastage from these patterns.

## 6. The differing example scenarios and the implementation of the prototype

It is important to note several differences among these three differing example scenarios. Firstly, the user has the total freedom to design and decide on the decision making process of a manual scenario, including incorporating computed stored scenarios into consideration and computation (as shown in manual scenario 3). The user can therefore model decisions that are nested, parallel, interwoven, and/or convergent. Secondly, the user can design the decision making process as s/he goes or at the start of the process and add, delete, or modify each activity and/or decision accordingly in a manual scenario. Thirdly, there is structured decision guidance in the automatic scenario as the user is guided in following the prescribed decision making process. Fourthly, there is some decision guidance in the semi-automatic scenario similar to the automatic scenario where the user is guided in the decision making process. However, the user has some freedom in deciding on which paradigm's solver to incorporate, whether s/he wishes to obtain an optimised solution, or a satis<sup>fi</sup>cing solution. Fifthly, there is no decision guidance in the manual scenario. The user will need to decide and devise every single detail of the component and integration including any data type mapping. This signi<sup>fi</sup>cantly reduces the bias contributed by the decision system to a minimum.

When comparing the decision modelling lifecycle roadmaps for all three differing example scenarios (Fig. 10 for automated, Fig. 12 for semi-automated, Figs. 14, 15, and 17 for manual), we can see that the decision paths tend to lie within certain categories for each scenario. For an automated scenario, the user has no control or knowledge about the decision paths, and is therefore restricted to in<sup>fl</sup>exible and prede<sup>fi</sup>ned paths and tasks and also within the domain category. There is low versatility in terms of no choice in solvers. For a semiautomated scenario, the user has some in<sup>fl</sup>uence over the choice of de<sup>fi</sup>ne solvers and some <sup>fl</sup>exibility in the decision paths to move within the optimising, domain and satis<sup>fi</sup>cing categories (albeit the possible movement to the optimising category is not illustrated in any of the semi-automated scenarios here in Fig. 12). For a manual scenario, the user has the <sup>fl</sup>exibility to design his/her own decision paths. Hence, the decision paths of a manual scenario will not be restricted to certain categories like an automated or a semi-automated scenario, and will have movement to all available categories (albeit the possible movement to the utilities category is not illustrated here in Fig. 17). The manual scenario also exhibits the potential versatility since the user can choose any solvers regardless of its paradigm or domain. Furthermore, an experienced user can design, create and save a manual scenario of which can be used later as an automated or a semiautomated scenario template by other less experienced users, or for solving more routine and structured decision scenarios.

Patterns / Constraints

<table><tr><td></td><td>1650m</td><td>1610m</td><td>1440m</td><td>800m</td><td>700m</td><td>530m</td><td>symbol</td><td>RHS</td><td>edge</td><td>chosen?</td><td>run-times</td></tr><tr><td>1</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>&lt;=</td><td>3300</td><td>0</td><td>YES</td><td>9</td></tr><tr><td>2</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>&lt;=</td><td>3300</td><td>40</td><td>YES</td><td>0</td></tr><tr><td>3</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>&lt;=</td><td>3300</td><td>210</td><td>YES</td><td>0</td></tr><tr><td>4</td><td>1</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>&lt;=</td><td>3300</td><td>50</td><td>YES</td><td>0</td></tr><tr><td>5</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>&lt;=</td><td>3300</td><td>150</td><td>YES</td><td>0</td></tr><tr><td>6</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>&lt;=</td><td>3300</td><td>320</td><td>YES</td><td>0</td></tr><tr><td>7</td><td>1</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>&lt;=</td><td>3300</td><td>250</td><td>YES</td><td>0</td></tr><tr><td>8</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>&lt;=</td><td>3300</td><td>420</td><td>YES</td><td>0</td></tr><tr><td>9</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>3</td><td>&lt;=</td><td>3300</td><td>60</td><td>YES</td><td>0</td></tr><tr><td>10</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>&lt;=</td><td>3300</td><td>80</td><td>YES</td><td>3</td></tr><tr><td>11</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>&lt;=</td><td>3300</td><td>250</td><td>YES</td><td>0</td></tr><tr><td>12</td><td>0</td><td>1</td><td>0</td><td>2</td><td>0</td><td>0</td><td>&lt;=</td><td>3300</td><td>90</td><td>YES</td><td>0</td></tr><tr><td>13</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>&lt;=</td><td>3300</td><td>190</td><td>YES</td><td>0</td></tr><tr><td>14</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>&lt;=</td><td>3300</td><td>360</td><td>YES</td><td>0</td></tr><tr><td>15</td><td>0</td><td>1</td><td>0</td><td>0</td><td>2</td><td>0</td><td>&lt;=</td><td>3300</td><td>290</td><td>YES</td><td>0</td></tr><tr><td>16</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>&lt;=</td><td>3300</td><td>460</td><td>YES</td><td>0</td></tr></table>

Fig. 18. Display all generated patterns and its implementation solution (in matrix style) of a manual scenario

Nested decisions can be modelled in a manual scenario as the user retrieves a stored scenario from within a scenario, as shown in Figs. 15 and 17. Such nested decisions also demonstrate the consolidation and pipelining of models that belong to the same modelling paradigm (in this case a domain scenario feeds and consolidates with another domain scenario). Interwoven and converging decisions can also be modelled. Through an attention-focused method, the user selects a satis<sup>fi</sup>cing method and generates the desired cutting patterns, as shown in Fig. 15. Having viewed the cutting patterns produced, the user can go through the list of patterns repeatedly and select or deselect each pattern within a decision-focused method, as shown in Fig. 15. The desire to choose and modify which cutting patterns to use or not to use is subject to the results of a previous decision (in this case the generated cutting patterns). Such desire illustrates the splicing of models, where the choice of model is dependent on the results of another decision. The user can also retrieve a stored scenario (in this case manual scenario 1) and consolidate and/or interweave it with the objective(s) and retrieve a second stored scenario (in this case manual scenario 2) that consists of generated and preselected cutting patterns, as shown in Fig. 17. The user can then pipeline two models of different modelling paradigms together by merging the current domain scenario (in this case manual scenario 3) into an attentionfocused optimising scenario in producing the required optimising constraints. These constraints can then be fed into a decision-focused method in order to produce a <sup>fi</sup>nal and optimal solution. The results from two different modelling paradigms (in this case the optimising scenario and the original domain scenario prior to mapping) are consolidated together to present an ultimate decision and results of the 1D-CSP scenario, as shown in Fig. 17. As a result, manual scenario has illustrated the four levels of model integration through the manual scenarios 1, 2, and 3.

These differences demonstrate the attributes of the three key pillars in building a decision system that supports the proposed decision analysis, decision making process, entire modelling lifecycle, and FOODS framework and architecture: <sup>fl</sup>exibility, independence and versatility. In terms of <sup>fl</sup>exibility, the result from one model can be fed individually or grouped together as inputs to another model. The results can also be retrieved and used as inputs to another model or affect the choice of subsequent models. Such <sup>fl</sup>exibility enables the decision making process and the decision models to be constructed as they emerge or reformulated repeatedly with differing components. Furthermore, the model can be saved, retrieved and reused in later decision instances, and thus allows different scenarios to be investigated and compared. It may be argued that if decisions are unstructured and non-routine, there is no need to retrieve or reuse a stored scenario. However, we cannot reject the possibilities that an organisation may receive 1D-CSP jobs that consume the same cutting patterns from the same customer despite different order quantities each time.

In reality, most 1D-CSP jobs have more than one traditional objective of minimising wastage, employ machineries that may not be able to accept every combination of cutting patterns, and consist of more than 6 order widths which in turn generate over 1000 cutting patterns for consideration. For computation, performance and timesaving reasons, the ability to store and retrieve a scenario becomes a valid and necessary motivation. These characteristics for <sup>fl</sup>exibility are clearly demonstrated in the manual scenario. In order for the user to have the ability to select decision components that suit decision models under consideration, the components themselves must be independent from each other. This enables the values of the decision problems to be changed; the number of problem constraints, objectives, and parameters to be increased or decreased accordingly.

Research Objectives/ Evaluation Criteria / Implementation Requirements

<table><tr><td rowspan="6">Independence</td><td>❖ the ability to select different components with different models</td><td>component independence</td></tr><tr><td>❖ the values can be changed</td><td>value (data) independence</td></tr><tr><td>❖ the number of problem constraints (i.e. rows) can be in/decreased</td><td rowspan="3">dimension (data) independence</td></tr><tr><td>❖ the number of objectives can be in/decreased, which in turn affects the parameters</td></tr><tr><td>❖ the number of parameters (i.e. variables or columns) can be in/decreased</td></tr><tr><td>❖ the computational direction of the problem can be changed</td><td>purpose (solver) independence</td></tr><tr><td rowspan="5">Flexibility</td><td>❖ the result from one model can be feed as an input to another model</td><td rowspan="3">model integration (consolidation and pipelining)</td></tr><tr><td>❖ the result from one model can be grouped together as an input to another model</td></tr><tr><td>❖ the result from one model can be retrieved and used as an input to another model</td></tr><tr><td>❖ the result from one model affects the choice of subsequent models</td><td>model integration (splicing)</td></tr><tr><td>❖ the model can be saved and reused</td><td>management of model instances</td></tr><tr><td rowspan="2">Versatility</td><td>❖ the inclusion of both optimising and satisficing methods</td><td>paradigm versatility</td></tr><tr><td>❖ the investigation of decision problems across multiple industries and/or jobs</td><td>domain versatility</td></tr></table>

Fig. 19. The three pillars of FOODS: independence, <sup>fl</sup>exibility, and versatility.

These characteristics for independence are demonstrated in all the three differing scenarios. Furthermore, the computational direction of the problem can be changed with the change of solvers, as demonstrated in the semi-automated and manual scenarios. In terms of versatility, both optimising and satis<sup>fi</sup>cing models should be able to be considered and incorporated within the same decision model. The decision model should not be limited to solve a particular problem of a particular job in a particular industry, but be accommodating enough to consider a range of different problems across industries and jobs. Such opportunities for these versatility criteria are especially highlighted in the manual scenario. These key pillars and their criteria and principles are summarised and shown in Fig. 19.

The building of artefacts such as computers and programs is considered as a form of empirical inquiry [35]. Even though it is easier for users to understand hierarchically organised system descriptions conceptually and visually than object-oriented ones [1], the prototypical system was implemented using an object-oriented database management system JADE since it aids better management of complexity in the real world in terms of system objects and structural

## MathematicalProgram

description: String

objective\_function: Constraint

resulting\_function: Constraint

resulting\_coefficients:

Collection(Coefficient)

get\_objective

get\_description

get\_objective\_function

get\_num\_of\_resulting\_coeff

set\_objective

set\_description

repetition [6,33]. In terms of the data structures, even though a 1D-CSP is often considered as a general linear programming problem since it is solvable using an integer programming and a linear programming approach, it is also solvable using a heuristic approach such as a delayed column generation [20]. The Cutting Stock class object is therefore not created as a child of the General Linear Program class object in the prototype. Since both the 1D-CSP and a linear programming problem share many properties, an abstract mathematical program class object is thus created. The <sup>fi</sup>ve clusters groups of use cases signify <sup>fi</sup>ve possible class objects. Although the heuristic method can be constructed using a separate Satis<sup>fi</sup>cing class object, it is simply included as part of the Cutting Stock class object since these clusters share the same properties and methods and by not separating them minimises the need for mapping during runtime. Fig. 20 gives a summary of the major object-oriented class objects and their properties and methods implemented in the prototype. Therefore, if the Cutting Stock domain or satis<sup>fi</sup>cing scenario is fed into a General Linear Program scenario, or vice versa, mapping is necessary in order for the two decision models to integrate. As mentioned earlier, each decision

![](/api/attachments/KK3VUEWN/fulltext/images/664a5459969cc135a340dc5e9f6874628a3128064b89994afaa5655817937679.jpg)

## CuttingStock

get\_raws

get\_num\_of\_orders

get\_num\_of\_raws

generate\_optimal\_patterns

generate\_delayed\_patterns

make\_pattern

## GeneralLinearProgram

basis: Collection(DecisionVariable)

get\_basis

get\_num\_of\_basis

get\_num\_of\_artificials

get\_num\_of\_slacks

Fig. 20. An extracted class diagram of the implemented object-oriented class objects.

component is independent from each other. Hence any changes to one component do not affect other components, unless they belong to the same inheritance hierarchy. A separate mapping class object is created to deal with mapping between components. If signi<sup>fi</sup>cant changes have been made to a particular component then the mapping class will be updated to re<sup>fl</sup>ect such change. In manual scenario 3 (see Fig. 17), the domain scenario is map into an optimising scenario when the data within the domain scenario was transposed and validated to suit the optimising scenario.

## 7. Conclusion

The basic concern of any decision system is to ensure that decision makers are supported to make better decisions, rather than being replaced and/or dictated by decision systems. The decisions under consideration may be anything from routine to non-routine, structured to unstructured decisions, and simple to one that consists of numerous smaller decisions that are aggregated and/or interrelated. Therefore the decision making process is no longer limited to be sequential. It may be nested, parallel, interwoven, and/or converging. As the user learns more about the decision problems, s/he may wish to participate more actively in the selection of decision components, even if the decision components are included only during design time. As the user becomes more con<sup>fi</sup>dent, s/he may wish to build his/her own decision making process to suit, and retrieve previously stored scenarios as inputs and/or scenario comparisons. Therefore, the decision systems need to be accommodating to the needs and pro<sup>fi</sup>les of the users through the ability to use differing scenarios, from fully automated to completely manual scenarios. We propose decision making processes, modelling processes, system frameworks, system architectures, and a prototypical implementation to support such complex requirements entailed by <sup>fl</sup>exibility, versatility, and modelling life cycle support.

A simple mathematical example, namely 1D-CSP, was used to illustrate the interrelated nature of decisions through the proposed decision making and modelling processes, framework, and architecture, Three example scenarios: automated, semi-automated, and manual scenarios are used to validate the <sup>fl</sup>exibility and complexity of the proposed decision analysis and decision making processes in handling interrelated decisions. These scenarios explored the art of decision making and described how converging decisions are developed in producing a course of action. The user should be free to choose either an optimising or a satis<sup>fi</sup>cing method to resolve a problem, rather than be restricted to one paradigm or the other. From the evaluation results and sample sessions of the prototypical system, we can see that it is able to handle interrelated decisions within a 1D-CSP problem by following the entire modelling lifecycle and under varying conditions of versatility and <sup>fl</sup>exibility. Even though the evaluation results and sample sessions of the prototypical system was situated within the context of a particular problem domain, it highlighted the potential of our proposals to be generic. In particular the decision analysis process, the decision making and modelling processes, the FOODS framework, and architecture, are generic enough to be applicable to other domains and paradigms.

## References

[1] R. Agarwal, A.P. Sinha, M. Tanniru, Cognitive <sup>fi</sup>t in requirements modeling: a study of object and process method, Journal of Management Information Systems 13 (2) (1996) 137-162.

[2] D. Arnott, G. Pervan, Eight key issues for the decision support systems discipline Decision Support Systems 44 (3) (2008) 657–672.

[3] M. Beynon, S. Rasmequan, S. Russ, A new paradigm for computer-based decision support, Decision Support Systems 33 (2) (2002) 127–142.

[4] G.D. Bhatt, J. Zaveri, The enabling role of decision support systems in organizational learning, Decision Support Systems 32 (3) (2002) 297–309.

[5] T. Bhrammanee, V. Wuwongse, ODDM: a framework for model bases, Decision Support Systems 44 (3) (2008) 689–709.

[6] S. Biswas, Y. Narahari, Object oriented modeling and decision support for supply chains, European Journal of Operational Research 153 (3) (2004) 704–726.

[7] G.D. Brewer, P. DeLeon, The Foundations of Policy Analysis, Dorsey Press Homewood, IL, 1995.

[8] K.J. Chen, D. Sundaram, A. Srinivasan, The design and implementation of a component-based decision support system generator, Proceedings of The International Society for Decision Support Systems — The 6th International Conference, Brunel University, London, 2001.

[9] B. Curtis, M. Kellner, J. Over, Process modelling, Communications of the ACM 35 (9) (1992) 75–90.

[10] A. Diegel, E. Montocchio, E. Walters, S.V. Schalkwyk, S. Naidoo, Setup minimising conditions in the trim loss problem, European Journal of Operational Research 95 (3) (1996) 631–640.

[11] D. Dolk, B. Konsynski, Model management in organizations, Information & Management 9 (1) (1985) 35–47.

[12] M. Draman, I. Kuban Altinel, N. Bajgoric, A. Tamer Unal, B. Birgoren, A clone-based graphical modeler and mathematical model generator for optimal production planning in process industries, European Journal of Operational Research 137 (3) (2002) 483–496.

[13] H.L. Dreyfus, S.E. Dreyfus, Mind Over Machine: The Power of Human Intuition and Expertise in the Era of the Computer, Free Press, New York, 1986.

[14] G. Eppen, F. Gould, Introductory Management Science, Prentice-Hall, New Jersey, 1984, pp. 164–165.

[15] D.M. Eriksson, A framework for the constitution of modelling processes: a proposition, European Journal of Operational Research 145 (1) (2003) 202–215.

[16] C. Fierbinteanu, A decision support systems generator for transportation demand forecasting implemented by constraint logic programming, Decision Support Systems 26 (3) (1999) 179–194.

[17] A. Geoffrion, An introduction to structured modelling, Management Science 33 (5) (1987) 547–588.

[18] A. Geoffrion, Computer-based modeling environments, European Journal of Operational Research 41 (1) (1989) 33–45.

[19] A. Geoffrion, Reusing structured models via model integration, Twenty-Second Annual Hawaii International Conference on System Sciences, IEEE Computer Society Press, Los Alamitos, CA, 1989.

[20] P. Gilmore, R. Gomory, A linear programming approach to the cutting-stock problem, Operations Research 9 (1961).

[21] P. Gilmore, R. Gomory, A linear programming approach to the cutting-stock problem — Part II, Operations Research 11 (1963).

[22] A.L. Golub, Decision Analysis: An Integrated Approach, John Wiley & Sons, New York, 1997.

[23] C. Goulimis, Optimal solutions for the cutting stock problem, European Journal of Operational Research 44 (2) (1990) 197–208.

[24] S. Holtzman, Intelligent Decision Systems, Addison-Wesley Publishing, 1989.

[25] B. Iyer, G. Shankaranarayanan, M.L. Lenard, Model management decision environment: a web service prototype for spreadsheet models, Decision Support Systems 40 (2) (2005) 283–304.

[26] J.J. Jiang, G. Klein, Side effects of decision guidance in decision support systems, Interacting with Computers 12 (5) (2000) 469–481.

[27] R.E. Johnston, Rounding algorithms for cutting stock problems, Asia-Paci<sup>fi</sup>c Journal of Operational Research 3 (1986) 166–171

[28] J.E. Kottemann, D.R. Dolk, Model integration and modelling languages: a process perspective, Information Systems Research 3 (1) (1992) 1–16.

[29] R. Krishnan, K. Chari, Model management: survey, future research directions and a bibliography, The Interactive Transactions of OR/MS 3 (1) (2000).

[30] A. Langley, H. Mintzberg, P. Pitcher, E. Posada, Opening up decision making: the view from the black stool, Organization Science 6 (3) (May-Jun 1995) 260–279

[31] K.W. Lee, S.Y. Huh, A model–solver integration framework for autonomous and intelligent model solution, Decision Support Systems 46 (2) (2006) 926-944.

[32] A. Liew, D. Sundaram, Complex decision making processes: their modelling and support, Thirty-Eighth Annual Hawaii International Conference on System Sciences, IEEE Computer Society Press, Kona, Hawaii, 2005.

[33] D. Liu, T.J. Stewart, Integrated object-oriented framework for MCDM and DSS modelling, Decision Support Systems 38 (3) (2004) 421–434.

[34] K. Mathur, D. Solow, Management Science: The Art of Decision Making, Prentice Hall, Englewood Cliffs, New Jersey, 1994.

[35] A. Newell, H. Simon, Computer science as empirical inquiry: symbols and search, Communications of the ACM 19 (3) (1976) 13–126.

[36] J.J. Nunamaker, M. Chen, T. Purdin, Systems development in information systems research, Journal of Management Information Systems 7 (3) (1991) 89–106.

[37] D.J. Power, R. Sharda, Model-driven decision support systems: concepts and research directions, Decision Support Systems 43 (3) (2007) 1044–1061.

[38] R.G. Ramirez, C. Ching, R.D. St Louis, Model–data and model–solver mappings: a basis for an extended DSS framework, ISDSS Conference Proceedings, 1990.

[39] R.G. Ramirez, C. Ching, R.D. St Louis, Independence and mappings in model-based decision support systems, Decision Support Systems 10 (3) (1993) 341–358.

[40] M.S. Silver, Decisional guidance for computer-based decision support, MIS Quarterly 15 (1) (1991) 105–122.

[41] H. Simon, The New Science of Management Decision, Prentice-Hall, Englewood Cliffs, NJ, 1977.

[42] H. Simon, Models of Bounded Rationality, Harper and Row, Cambridge, M.A., 1983

[43] R.J. Sprague, A framework for the development of decision support systems, MIS Quarterly 4 (4) (1980) 1–26.

[44] R.J. Sprague, E. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, N.J., 1982

[45] A. Srinivasan, D. Sundaram, An object relational approach for the design of decision support systems, European Journal of Operational Research 127 (3) (2000) 594–610.

[46] L. Tung, R.G. Ramirez, R.D. St Louis, Model integration in an object-oriented model management system, Twenty-Fourth Annual Hawaii International Conference on System Sciences, IEEE Computer Society Press, Kauai, Hawaii, 1991.

[47] S. Umetani, M. Yagiura, T. Ibaraki, One-dimensional cutting stock problem to minimize the number of different patterns, European Journal of Operational Research 146 (2003) 388–402.

[48] G. Wascher, An LP-based approach to cutting stock problems with multiple objectives, European Journal of Operational Research 44 (2) (1990) 175–184.

[49] S. Wrobel, D. Wettschereck, E. Sommer, W. Emde, Extensibility in data minin system, 2nd International Conference on Knowledge Discovery and Data Mining, 1997.

[50] B.J. Yuen, K.V. Richardson, Establishing the optimality of sequencing heuristics for cutting stock problems, European Journal of Operational Research 84 (3) (1995) 590–598.

![](/api/attachments/KK3VUEWN/fulltext/images/a71207c442284236852daaa735e99ab7976e1fd68c6b54117f63d82175127ad8.jpg)

Angela Liew is a PhD candidate and a Senior Tutor in Accounting Information Systems at the University of Auckland. She received her BCom/BSc conjoint degrees in Accounting and Computer Science, and MCom(Hons) research degree in Management Science and Information Systems, all from the University of Auckland, and is a Certi<sup>fi</sup>ed Practising Accountant with CPA Australia. Her research interests include decision making, decision support, data modelling, accounting information systems, and accounting and information systems education.

![](/api/attachments/KK3VUEWN/fulltext/images/cc8bf1f134d3fa7df95e8e955f677a56c714aacaea4e7b6652e9688c0b4ededf.jpg)

David Sundaram is an Associate Professor in the Department of Information Systems and Operations Management at the University of Auckland. He has varied academic (B.E. in Electronics & Communications, PG Dip in Industrial Engineering, and Ph.D. in Management Science & Information Systems) as well as work (systems analysis, design, consulting, teaching, and research) background. His primary research interests include the 1) Design and Implementation of <sup>fl</sup>exible and evolvable Information and Decision Systems; 2) Process, Information, and Decision Modelling; 3) Triple Bottom Line Modelling and Reporting; 4) Enterprise Service Oriented Architectures.
