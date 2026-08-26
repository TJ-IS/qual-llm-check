---
otero_id: 17619
otero_key: "EH348CJ5"
title: "Decision support for planning"
authors: "Soumitra Dutta"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90051-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support for planning

Soumitra Dutta

European Institute of Business Administration (INSEAD), Fontainebleau, France

Planning, in general, is the process by which the long term goals of an agent are translated into short term tasks and objectives, subject to the resource constraints facing the agent. In contrast to “decision making”, planning has a distinct temporal dimension and calls for a sequence of temporally separated, inter-dependent decisions to be made over a period of time. This enables the explicit incorporation of the learning necessary during the complex iterative process of achieving a goal or moving towards a solution. This paper explores issues in the design of decision support systems for supporting planning processes in real world environments. The results of implementing a decision support system for planning in the complex financial domain of mergers and acquisitions are reported.

Keywords: Expert systems; Planning; Reasoning under uncertainty; Decision support systems; Financial applications of artificial intelligence

![](/api/attachments/EH348CJ5/fulltext/images/a22bf425044de12a80d57df3d14c546a81e9dec678b804f0e684cc304137ee51.jpg)

Soumitra Dutta is currently an Associate Professor of Information Systems in the Technology Management Area at the European Institute of Business Administration (INSEAD) in Fontainebleau, France. He is also a visiting Professor of Information Systems at the Universite Libre de Bruxelles (ULB) in Brussels, Belgium. Prior to joining INSEAD in 1989, he was a postdoctoral research assistant at the University of California at Berkeley, where he obtained a Ph.D.

## 1. Introduction

This section describes the differences between decision making, problem solving and planning. It also outlines the focus and structure of the paper.

1.1. Decision making, problem solving and planning

Decision making is an activity that has been studied from many different perspectives such as the organizational $[21,24]$ and the cognitive $[25,29]$ . Simon's $[29]$ three-stage model of decision making is widely accepted as a useful cognitive model of the decision making process. The three stages of Simon's model are: intelligence (searching the environment for conditions calling for decisions), design (inventing, developing and analyzing possible courses of action) and choice (selecting a course of action from these actions). Recently some researchers have argued that Simon's three stage model of decision making does not adequately capture all the intricacies of human problem solving. For example, Gorry and Scott-Morton $[20]$ (in a reprint of their earlier paper $[19]$ ) have observed that Simon's model of decision making suggests a “clarity” and “one-step” nature that does not correspond to real human problem solving (which typically occurs in a complex iterative manner over an extended time period). Thus, in contrast to decision making, problem solving needs to explicitly recognize the temporal dimension of the process and the learning necessary during the complex iterative process of moving towards the solution.

In the context of the above definition of problem solving, planning can be regarded as “intelligent/optimal problem solving”. While problem solving alone is concerned with the generation of a sequence of steps/operations to achieve a goal, planning ensures that the chosen set of steps/operations are “optimal” and/or satisfy the various constraints on the problem solving process. The latter function of planning is perhaps more vital as all real world problem solving has to be done with limited resources (such as finite memory, time and knowledge). Note that it is possible to solve a problem without planning, though the lack of a plan may result in a sub-optimal problem solution. Figure 1 summarizes the relationship between decision making, problem solving and planning. Each decision process shown in Figure 1 is assumed to consist of the three stage Simon model.

## 1.2. Planning

Planning has been researched with artificial intelligence (AI) for nearly two decades $[9,10,30,32]$ . Most of the early research in planning $[9]$ considered static domains in which the state of the world was given at any instant and the emphasis was on devising plans (provably correct sequence of actions) to achieve certain goals. Certain assumptions were common during the planning phase: the environment was static; the effects of various actions in the world were fully predictable; resources were unlimited; and there was perfect information about the world. Such static planners have proven to be of limited applicability in real world situations due to the frequent violation of one or more of the above assumptions. There is thus now a renewed emphasis on dynamic planning models $[1,17,18]$ which attempt to capture and reason about the dynamic and uncertain nature of the external world and satisfy the various resource constraints facing the planner.

For the purposes of this paper, planning is defined as: “the iterative process by which the long term goals of an agent are transformed into short term tasks and goals, subject to the resource constraints facing the agent." Figure 2 graphically depicts the process of planning taking into consideration various factors such as [a] the long term goals of the agent [b] current short term goals and objectives [c] prior history and experience [d] environmental conditions [e] expected future events and [e] various resource constraints. Planning can be seen to consist of a whole series of temporally separated, but interrelated decisions such that the desired goal is eventually achieved.

![](/api/attachments/EH348CJ5/fulltext/images/0c200ac82a7a499760e3eaa9909582afe2977de2d14e6d7a35fc42ff11f6d0cf.jpg)  
Fig. 1. Decision making, problem solving and planning.

![](/api/attachments/EH348CJ5/fulltext/images/a3b42d24aa2167b8e1b41e505c825d38f9384d81b20e3b2c42407488b875e4cd.jpg)  
Fig. 2. The process of planning.

As one goes through the “loop” in Figure 2, monitoring, feedback, learning and replanning become vital components of the process. In general, the external world is dynamic and changing continuously. Thus the environment has to be monitored continuously to check whether the chosen action is the best feasible choice (at that moment) and whether to modify future expectations, goals and strategies. Learning is essential as the knowledge in the agent is necessarily finite and incomplete. With each significant change in the environment, the agent must see whether it can “learn” something, i.e., change its knowledge structure. Periodic replanning is essential because the external world is dynamic. Even if a complete set of actions has been decided initially, the planning process has to continuously check to see whether unanticipated changes in the external world call for a modified “path” to be chosen in preference over the existing path.

The planning process involves both strategic planning and incremental (or tactical) planning. Strategic planning emphasizes reasoning about and deciding general strategies to achieve the long term goals. Short term tasks and goals, generated as a result of the chosen (long term) strategies, are the focus of incremental planning. Strategic planning considers a longer time horizon as compared to incremental planning. While strategies resulting from strategic planning remain fairly stable over time (barring drastic changes in the external world), the goals and tasks of incremental planning change flexibly over time to adjust to changes in the external world. Changes to active strategies and tasks are caused both by the dynamic, uncertain nature of the external world and the experiential learning occurring during the process of planning. It is hard to draw a crisp distinction between strategic and incremental planning. Often, goals and tasks have varying strategic and incremental aspects. Both strategic and incremental planning are essential for successful planning, as neither one alone is a panacea for planning. For example, a company cannot resolve a sudden liquidity problem in a strategic mode and one cannot also formulate a comprehensive five year plan in the incremental mode.

## 1.3. Focus and structure of paper

Classical decision support systems (DSS) are similar to static planners and typically generate entire plans for a given state of the world. They provide little or no support for the more difficult aspects of planning such as monitoring, replanning, managing inter-dependencies between different temporally separated actions and the learning occurring during the iterative process of planning. Such burdens are usually passed on to the user of the DSS.

This paper explores how the scope of conventional DSS can be enlarged to provide better decision support for planning. Due to the wide applicability of planning processes and the complexities of specific planning problems, it is difficult to propose an architecture for a planning support system which is both general enough to be applicable to different domains and specific enough to enable meaningful solutions to different problems. Thus the approach taken in this paper is to look at one complex planning problem and highlight some of the lessons learnt from implementing a specific planning support system. This research uses the financial domain of mergers and acquisitions (M and A) to explore issues related to decision support for planning. Experiences from implementing a large prototype planning support system for analyzing the progress of

M and A deals are reported to support the arguments. Most of the important planning issues in M and A are also present in other domains, and thus the applicability of the results of this research is broad in scope.

The structure of this paper is as follows. This paper has four additional sections. Section 2 introduces the domain of mergers and acquisitions and discusses some of the relevant issues to consider while providing decision support for planning in M and A. The next section introduces MARS, a prototype tool to support decision making in M and A. Section 4 provides details on the planning processes within MARS. The last section, builds on the experiences while implementing the MARS system to discuss possible extensions to the classical DSS paradigm for providing adequate decision support for planning.

## 2. Planning in mergers and acquisitions

This section introduces the domain of M and A and discusses issues in providing decision support for planning in such a domain.

## 2.1. Mergers and acquisitions: a brief introduction

The past decade has seen an astonishing increase of activity in the domain of mergers and acquisitions (M and A). According to recently reported data [8], during the 1980s, \$1.3 trillion was spent on shuffling assets – an amount on a par with the annual economic output of Germany! Current activity in M and A, while not as sensational as before, continues unabated. Europe, in particular, is experiencing a spurt of activity in M and A in anticipation of the unified economic market.

The average M and A is enormously complex and involves many interested parties. To lend some useful conceptual abstraction, it is useful to identify certain players of interest. The raider is the person or company who usually initiates a take-over attempt. The company being attacked by the raider is the target. Both the raider and the target are supported by a wide variety of support staff including investment bankers, lawyers and accountants. Another player of interest, who is usually outside the structure of the actual M and A deal, is the professional arbitrageur. The goal of the arbitrageur is to try and make arbitrage profit by wisely shifting investments in anticipation of and by reacting to merger activity. Even in simple M and A deals, other complicating factors, such as multiple bidders, white knights and legal complications often arise. Though each M and A deal is special and uniquely complex, two types of M and A deals can be identified in general: friendly and hostile. Friendly mergers are agreed upon by friendly companies and structured for mutual benefit. There is little distinction between the raider and the target as either company may initiate the M and A deal. Hostile mergers are more complex and involve attempts by the raider to forcibly takeover the target. To simplify our task we focus our attention primarily on the raider, the target and the arbitrageur. We also consider the scenario of hostile takeovers as the planning requirements in a hostile takeover are more complex and interesting from the perspective of decision support. The reader may refer to the references [16,23,26], for more details on various aspects of M and A.

## 2.2. Overview of planning in $M$ and $A$

Kuhn [23] has provided a useful graphical representation (Figure 3) of the planning processes in a M and A deal. The two major players (the raider and the target) in the M and A process have to each scan the environment (“opportunities and threats”), perform a honest internal analysis (“company analysis”) and make a decision choice (“strategic choice”) in the context of the current goals. The process of strategy formulation results in a list of alternative policies, each of which is rigorously evaluated. This evaluation leads to the selection of a particular strategy, which is then translated into short term objectives and tasks. This process is repeated iteratively. Learning is enforced through a mechanism of feedback and control.

![](/api/attachments/EH348CJ5/fulltext/images/85aebb241ffdabefaa81f1d9eac8ecaa83a084d548d818742ff03f943b1f5af2.jpg)  
Fig. 3. Conceptual structure of planning in M and A (adapted from [23]).

Each of the five boxes of Figure 3 represent rich areas for decision support in the M and A process. Consider for example the environmental scanning done by the raider to track potential takeover targets. A DSS can periodically evaluate different aspects of potential targets in the context of the raider's own goals and aspirations (which can range from benevolent intentions of acquiring and integrating a target company to busting the target for quick profits) and signal important events in the environment. A DSS can also help in the selection of pre-tender defensive strategies as such defensive tactics are adopted by potential targets only after a thorough analysis of their own strengths and weaknesses. A more challenging area for DSS is supporting the process of strategy formulation. Formulation and refinement of a raider's attack strategy or a target's defense strategy is an involved, iterative, and dynamic process. Supporting this complex reasoning task helps to identify extensions to conventional DSS for use in planning (see Section 4).

## 2.3. Planning issues in $M$ and $A$

The domain of M and A is complex. Even in a simplified scenario of a single raider and a single target, many factors affect their individual plans and actions. For tractability, one can only consider a subset of the various factors which influence the actions of the raider and the target. The domain is also, in general, ill-structured and lacks a well defined model. Some (financial and accounting) models do exist for certain structured parts of a M and A deal, but they cannot by themselves form a complete basis for the planning processes of the raider and the target. Much of the reasoning in M and A is based on heuristic guidelines and subjective analyses, all of which are difficult to quantify and model precisely.

The data available for reasoning and planning are rarely complete and certain. Uncertainty is widespread and arises from many sources: (1) the dynamic nature of the external world (explained above), (2) the presence of unpredictable forces (e.g., movements in interest rates), (3) uncertainty in the available information (e.g., uncertainty about future cash flows of a company), (4) ignorance about certain data values (e.g., private company data) and (5) subjective analyses (e.g., a target's speculation about the raider's true intentions).

The external world for the raider and the target is changing constantly. Some of these changes are important and need to be responded to immediately, e.g., a target needs to formulate a response soon after being notified that it is the subject of a takeover attempt. Other changes are less important and need to be adjusted to relatively slowly, e.g., a rise in interest rates may increase the debt burden on a raider, forcing him to rethink specific aspects of his attack strategy. The planning processes of the raider and the target have to continuously monitor changes in the external world and ensure that current actions and goals are in agreement with the state of the external world.

A variety of reasoning strategies are needed for effective planning [12]. Financial and accounting models exist for certain aspects of a M and A deal (e.g., computing accounting combinations). Their results are used by the raider and the target for structuring parts of the M and A deal. These models are usually mathematical and algorithmic in nature. Heuristic reasoning is also important and is used for different purposes: (1) representing expert knowledge about the domain (as in expert systems), (2) interpreting the outputs of algorithmic models (such as financial models to generate expected cash flows) and (3) representing subjective analyses of various factors (e.g., the raider's assessment strategy to determine the degree of satisfaction among the shareholders of the target company).

The nature of the domain calls for a balance between the strategic and incremental aspects of planning. Operating in the strategic mode, the raider and the target define general goals and reason about the best plans to achieve these goals. Reasoning at the strategic level is analogous to meta-reasoning models [31] in knowledge-based systems and emphasizes the determination of general strategies to achieve the long term goals. Operating in the incremental mode, the raider and the target react to immediate problems and unexpected changes in the external world. Incremental plans and tasks are affected, both by strategic planning and the changing nature of the external world. Strategic planning is, in general, more stable over time (long term goals do not change rapidly) as compared to incremental planning, which, usually changes flexibly to react to the changing external world.

Learning is an important component of the planning procedures. Learning is partly represented by the cumulative store of experience and history. For example, the success or failure of prior anti-trust moves in other similar situations plays a major role in the raider's evaluation of the possibility of an anti-trust move succeeding under the current circumstances.

## 3. MARS: A mergers and acquisitions reasoning system

This section describes MARS, a prototype reasoning system for planning in the domain of M and A.

## 3.1. Commercial DSS for $M$ and $A$

A number of DSS are sold commercially for providing decision support for certain aspects of a M and A deal. For example, the Alcar Group Inc. of Stokie, Illinois, markets two DSS called the Value Planner and the Merger Planner. The Value Planner gives users the power to generate historical and forecasted financial statements, income statements, balance sheets, cash flow statements and ratios. The Merger Planner enhances the Value Planner's abilities by giving users the power to analyze mergers, acquisitions and divestures. Users can combine the raider and the target into a new entity by specifying deal structure, taxable or non-taxable methods of combinations, and purchase or pooling accounting treatments. There are other DSS which use game theoretic approaches for the analysis of strategies and possible outcomes. Various asset estimation DSS are also available on the market. These DSS are useful for the tasks which they are designed to solve. However they usually have one or both of the following limitations:

\- They are designed as static planners and are primarily geared towards giving a set of actions or plans based on a given state of the external world. Thus neither do they provide support for iterating through the planning loop of Figure 2 nor do they account for the dynamic nature of the environment.

![](/api/attachments/EH348CJ5/fulltext/images/1322e014ac8816a38d4444414f20dc1921f2316577d08f85c38be2ad73aa4b9d.jpg)  
Fig. 4. Architecture of MARS.

\- The results of these DSS models are based primarily on quantitative data and are thus rarely useful directly for planning. Rather, they have to be used in conjunction with heuristic and subjective analyses (performed by human experts) of other qualitative factors.

## 3.2. Software architecture of MARS

MARS is a prototype M and A reasoning tool which simulates and provides expert advice regarding the actions of the raider, target and the arbitrageur in the context of a unsolicited takeover attempt. The general software architecture of MARS is as shown in Figure 4. There are four independent simulators. The global simulator provides a simulation of the variations of the macro-economic variables affecting the M and A deal (e.g., the interest rate). The three other simulators simulate the reasoning and planning of the raider, target and the arbitrageur respectively. There is a fusion of different reasoning techniques in all four simulators and each of them is independently capable of integrated reasoning and planning with uncertain, incomplete and time varying information.

There are two sources of data input to the system. The quantitative input is planned to come from on-line commercial data-bases such as Compustat and Valueline and consists of numerical data (such as financial ratios) about the companies under consideration. The qualitative data is planned to come from the output of an intelligent information retrieval system (developed independently from MARS) called SCISOR [22]. SCISOR takes the Dow Jones News service as input and retrieves facts related to relevant merger activity. For example, it can retrieve reports of shareholder dissatisfaction in the target company and supply this information to the MARS knowledge base.

The knowledge-base depicted in the center of Figure 4 represents the common knowledge base that is accessible to all four simulators. Each simulator updates the publicly known effects of its actions and plans in the public knowledge base. Local to each simulator, there exists another knowledge base which stores information private to that simulator. For example, the true intentions of the raider are stored in the private knowledge base of the raider simulator. Contents of the private knowledge bases are not known to the other simulators. This mechanism allows the simulators to protect their individual reasoning and planning. The raider, target and arbitrageur simulators, each use a variety of models, some quantitative, others qualitative (heuristic) and case-based. The simulators usually communicate by declaring their actions and intentions in the public knowledge base. Direct communication can take place, if required, between the simulators (usually between the target and the raider simulators). Such direct communications are private and not reflected in the public knowledge base unless one of the parties in the communication updates the public knowledge base.

MARS has been implemented in Common-LISP using KEE and RUM [6]. The first version was implemented on the Symbolics LISP workstation. A later version of MARS has been implemented in PRIMO [2] and can run on the SUN workstation also. The knowledge-bases of MARS contains more than 600 rules. Though this is a fairly large number for a prototype system, the overall size is still a small fraction of what a real-life application in this domain would demand. MARS incorporates many simplifications about the M and A reasoning process and is to be viewed as a research prototype. More details on the structure and implementation of MARS are given in an earlier paper [3].

## 3.3. User interface of MARS

Figure 5 depicts a screen-dump from the operation of MARS at a specific instant. Data about 3 companies are displayed in the windows on the left. There can be more than 3 companies in the MARS system, but only three can be displayed simultaneously. The data representation format is as follows: attribute name, attribute value and a graphical representation of uncertainty (see Figure 8 in Section 4.2). Data about the arbitrageur is displayed in the top right window. Global macro-economic data which is public and affects all players in the M and A process are displayed in the window marked “Global”. The bottom-right window displays data about the M and A deal in progress. Due to a limitation on the number of windows which can be displayed on one screen, the M and A data in the “Merger” window is player specific. For example, the raider's view of the M and A deal is currently displayed in Figure 5. Other views (such as the target's and arbitrageur's views) can be selected by the user with the help of the mouse. The central window is used for interactions with the user and also displays summaries of activities during each planning cycle. The data displayed in each window is historical in nature (notice the time stamp visible in some windows) and prior data can be accessed by scrolling in the respective windows. The bottom window contains some important initialization and explanation commands.

## 3.4. Planning cycle of MARS

The planning cycle of MARS consists of several distinct phases as shown in Figure 6. The first initialization phase consists of the following four important sub-steps:

[1] The user is asked to define the number of companies in the system and enter their initial data. The data entered by the user for each company consists of both public (accessible to other companies in MARS) and private (inaccessible to other companies) data. Examples of public company attributes initialized by the user at this stage include book-value, stock-price and pe-ratio. Examples of private company data include true-management-goals and perceived-shareholder-satisfaction. Extensive financial data about publicly traded companies are readily available from many on-line database sources. Note that defining a company essentially causes the MARS system to activate a simulator for the that company (similar in structure and function to the simulators shown in figure 4 for the raider and the target).

![](/api/attachments/EH348CJ5/fulltext/images/801f2ba268693e99f6a9e4f2838651e3212b76b49e8bf88fc37bdf2e1ffe6738.jpg)  
Fig. 5. The user interface of MARS.

![](/api/attachments/EH348CJ5/fulltext/images/9b263a33eca8cd97cd4ad7b2d5d124bb5847982000b9d87b8cfba4de4f56dac0.jpg)  
Fig. 6. Planning cycle in MARS.

[2] Based on the data input by the user, the MARS system activates each individual company simulator to perform an internal analysis and suggest an appropriate pre-tender defensive strategy. The heuristic reasoning processes determining the pre-tender defensive strategy are common to all company simulators (in the current implementation of MARS). However, the chosen defensive strategies shall (in general) be different for the various companies due to the varying company specific data (both public and private) entered by the user. The user can override any particular suggestion of a pre-tender defensive strategy. Note that even this step requires fairly complex reasoning as a company has to be selectively cautious in adopting an appropriate defensive strategy (adopting too many defensive strategies can lead to a decrease in the stock price of the company).

[3] Next, the user has to select any one company to assume the role of a raider and initialize certain special private data for the raider that influence its strategy formulation and planning processes. These variables include raider-merger-goals and raider-risk-preference. While all attributes for a given raider can be changed at any later stage by the user, the choice of a particular company as a raider is fixed and cannot be changed later. This is because the designation of a particular company as a raider causes the MARS system to add a special “raider” module to the simulator of that company. While the generic company simulator simulates reasoning common to all companies (such as determination of pre-tender defensive strategies), the add-on raider module simulates the planning and reasoning behavior specific to the raider. Note that the choice of the raider is not immediately reflected in the public knowledge-base and so other companies are not aware of the identity of the raider at this stage.

[4] The last step in the initialization phase calls for the user to initialize relevant data about the arbitrageur and the global macro-economic environment. This step causes MARS to activate the simulator for the arbitrageur and the global environment. Note that data values entered during the initialization phase for all entities in MARS can be changed at any later stage.

After this initialization phase, a simple planning cycle in MARS consists of the raider making a move, the target responding to the raider's move, the arbitrageur shifting assets in response to the observed raider and target actions and the global simulator varying the macro-economic parameters appropriately. This cycle is repeated continuously till the raider is either successful or concedes defeat.

Each simulator plans and executes one or more tasks/actions during every planning cycle. Complex reasoning and planning is required on the parts of all four simulators for taking the appropriate set of actions at any step in the cycle. One of the first actions of the raider simulator is to perform an environmental scan and determine if any company is an appropriate target. The choice of an appropriate target is entirely guided by the initialization of the raider merger goals and the characteristics of other companies in the MARS database. It is possible that the raider simulator may refrain from attacking any target in one or more planning cycles if no company meets its desired merger goal characteristics. Once a potential target has been identified, the raider simulator has to determine the appropriate strategy to attack the target. Public notification of the identities of the raider and the target is made only when the raider makes a public bid for the target (such as making a tender offer). Till the moment of this public notification, all other players in the system (including the potential target and the arbitrageur) can only guess about the identity and intentions of the raider and the potential target. Thus it is necessary for each simulator to individually keep track of relevant developments in the environment during every planning cycle and take appropriate actions. For example, If the raider has chosen a secretive “toe-hold” strategy of slowly acquiring stock in the target company, the target company may not know that it is the subject of a takeover attempt, except by observing the slow accumulation of stock by the raider. However, once the target identifies the stock accumulation by the raider, it has to immediately react to this development and determine whether the intentions of the raider company are benign or malignant. It is evident that each simulator has to be able to plan in an dynamic environment fraught with uncertainty and imprecision.

## 3.5. Modes of decision support in MARS

MARS can operate in three different simulation modes, all of which can be arbitrarily interleaved:

Autonomous: In this mode, the raider and target simulators plan and reason autonomously to “play” against each other. The arbitrageur simulator observes the actions of the raider and the target and suitably updates its investment strategy.

I am Target: The user can take the role of the target in this mode and play against the raider. The arbitrageur simulator is unaffected.

I am Raider: In this mode, the user can assume the role of the raider and play against the target. The arbitrageur simulator operates as in the other modes.

![](/api/attachments/EH348CJ5/fulltext/images/de821f31adff525865f3adc157bc9849b9e31ced17f1a89368b90207636073db.jpg)  
Fig. 7. Types of decision support offered by MARS.

These three different modes of operation allow the observance of a rich variety of planning behaviors and reactions on the part of the raider, the target and the arbitrageur. It is important to note that there are no “canned” scenarios or outcomes. As all four simulators are independent and hide their private actions and data from the other simulators, a variety of different planning behaviors can be obtained. Each simulator tries to take the best action, given its limited resources and knowledge, and suitably reacts to the (known) actions of the other players.

The decision support offered by the MARS system to the user can be classified into the following three categories (as shown in Figure 7):

\- Passive observer: Here the user does not intervene in the operation of the MARS system (except for the initialization phase). The various simulators in the MARS system reason and plan autonomously and the M and A scenario evolves without any active intervention by the user (as in the autonomous mode of operation). The user can learn about the M and A domain by observing the planning behaviors of the various simulators (the user can, when desired, obtain explanations for various actions taken by the simulators).

\- Active intervention: Here the user actively intervenes in the operation of the various simulators within MARS during the evolution of the takeover attempt. By intervening and changing variable values and planning choices at appropriate moments, the user can test different hypotheses or observe different scenarios. For example, the user can arbitrarily decrease the assets of the raider suddenly and then observe how the raider simulator reacts to this new constraint. This is (similar to but) richer than the traditional “what-if” kind of decision support provided in conventional DSS because the user can observe the effects of many arbitrary changes in a set of inter-related and temporally separated actions taken by the different simulators within MARS.

\- Active participant: This is the most complex form of decision support provided by MARS and it allows the user to participate in the M and A scenario in a chosen role. Thus the user can choose to act as either the raider or the target and participate in the evolution of the M and A scenario as a regular player. Some of the most interesting scenarios of interactions were observed in this mode because a capricious user (acting as either the raider or the target) can effectively test the robustness of planning mechanisms of the other simulators in the system.

As the three different modes of simulation in MARS can be mixed, the user is not restricted to any one mode of decision support. During any one M and A scenario, the user can choose to be a passive observer for some time, intervene actively in the planning behaviors of the simulators at other times and sometimes even assume the role of one of the players within MARS. This ability to arbitrarily interleave the different simulation modes of MARS allows the user to use the system for complex modes of decision support.

## 4. Decision support for planning in MARS

As mentioned in Section 2.3, successful planning in the M and A domain requires the integration of a variety of reasoning strategies and models. This section expands on certain important issues related to providing decision support for planning within the MARS system.

## 4.1. Software architectural basis

The base software architecture of the planning modules in MARS is rule-based. A rule-based choice seems appropriate as it helps to represent a large proportion of the qualitative and subjective reasoning necessary for strategy formulation in M and A. Many quantitative models are integrated by incorporating suitable links in the premises and conclusions of rules. Rules are also used to represent the interpretation of the results of the calls to these quantitative models. This allows the integration of subjective and qualitative factors into the reasoning processes. A rule-based architecture also allows the incorporation of the effect of prior history into the planning processes. A T-Norm [28] based calculus is used in the rule-based inference process to account for the uncertainty in the domain. A belief revision feature facilitates the real-time monitoring of changes in the external domain. Thus rules seem to provide the maximum flexibility in building a system to meet many of the planning requirements imposed by the complex domain of M and A. More details on specific aspects of decision support in MARS within the software architecture of MARS are given in the following sub-sections.

The structure of a generic rule in MARS is more complex than simple IF..THEN.. rules. Rules are discounted by sufficiency (S), indicating the strength with which the antecedent implies the consequent and necessity (N), indicating the degree to which a failed antecedent implies a negated consequent. Note that conventional strict implication rules are special cases with S = 1 and N = 0. Each rule has an associated context which represents the set of preconditions determining the rule's applicability to a given situation. This mechanism provides an efficient screening of the knowledge base by focusing the inference process on small rule subsets. A simplified structure of a rule in MARS is given below:

<table><tr><td>(Rule-name Knowledge-Base-Name</td><td>%name of knowledge base contain-ing rule rule-name</td></tr><tr><td>Premise-List</td><td>%list of premises</td></tr><tr><td>Consequence-List</td><td>%list of consequences</td></tr><tr><td>Premise-Slots</td><td>%entities to keep track of during belief revision</td></tr><tr><td>Context-List</td><td>%context defining the applicability of the rule</td></tr><tr><td>Sufficiency-Necessity-Measure</td><td>%to represent plausibility of rules</td></tr><tr><td>T-Norm -Operator</td><td>%uncertainty calculi detail (see Section 4.2)</td></tr><tr><td>Context-threshold</td><td>%gives the minimum certainty level of the context-list</td></tr><tr><td>Context-Flag Rule-Daemon)</td><td>%defines the validity of the context %an optional argument</td></tr></table>

The context facility, sufficiency and necessity measures and the T-Norm operators give additional power to the rules to represent complexity in the domain. More details on these topics are given in the following sub-sections.

## 4.2. Reasoning under uncertainty

Uncertainty is an important feature of the domain in M and A. MARS utilizes an interval valued measure of uncertainty and uses the T-Norm based calculi of RUM [6] to combine (interval valued) uncertainty measures during the rule-based inference procedure.

Consider the representation of uncertainty in facts within MARS. Facts are qualified by a degree of confirmation and a degree of refutation. For a fact A, the lower bound of the confirmation and the lower bound of the refutation are denoted by L(A) and L(not A)) respectively. As in the case of Dempster's [11] lower and upper probability bounds, the following identity holds: L(not A) = 1 - U(A), where U(A) denotes the upper bound of the uncertainty in A and is interpreted as the amount of failure to refute A. Note that L(A) + L(not A) need not necessarily be equal to 1, as there maybe some ignorance about A which is given by (1 - L(A) - L(not A)). The degree of confirmation and refutation for the proposition A can be written as the interval [L(A), U(A)]. This can be graphically represented as shown in Figure 8. (Note the graphical representation of uncertainty for data values in Figure 5.)

The advantages of choosing such an interval valued uncertainty representation (as opposed to a more conventional single numbered representation – such as probability) are:

\- Separation of degrees of positive and negative evidence: Note that if there is evidence for fact A to the degree x (i.e., L(A) = x), it does not automatically follow that there is evidence for the negation of fact A to the degree 1 - x. Using simple probabilities we would not be able to make this distinction (because Prob(A) = 1 - Prob(not A)).

![](/api/attachments/EH348CJ5/fulltext/images/96184ab2cf0367a99c440d3b2350d40425460f5afefceb4dd654c46c3efd0ea4.jpg)  
Fig. 8. Graphical representation of uncertainty.

\- Explicit representation of ignorance: It is important to be able to represent ignorance (i.e., the absence of both positive and negative evidence) about facts explicitly. Using the interval valued uncertainty representation, complete ignorance about a fact A can be represented by the interval [0,1]. Any inference which utilizes the fact A should adequately reflect this ignorance. It is not possible to explicitly and easily represent ignorance about facts using a single numbered uncertainty representation (such as probabilities).

RUM provides an uncertainty calculus based on a set of five Triangular norms (T-norms) [28] for inference in the rule graph. T-norms and T-conorms are two-place functions from

$$
[ 0, 1 ] \times [ 0, 1 ] \rightarrow [ 0, 1 ]
$$

which are monotonic, commutative and associative. They are the most general families of binary functions which satisfy the requirements of the conjunction and disjunction operators respectively. Their corresponding boundary conditions satisfy the truth tables of the logical AND and OR operators. Five uncertainty calculi based on the following five T-norms are defined in RUM:

$$
\begin{array}{r l} & {\mathrm{T} _ {1} (\mathrm{a}, \mathrm{b}) = \max (0, \mathrm{a} + \mathrm{b} - 1)} \\ & {\mathrm{T} _ {1. 5} (\mathrm{a}, \mathrm{b}) = \left(\mathrm{a} ^ {0. 5} + \mathrm{b} ^ {0. 5} - 1\right) ^ {2} \text {if} (\mathrm{a} ^ {0. 5} + \mathrm{b} ^ {0. 5}) \geqslant 1} \\ & {\quad = 0 \text {else}} \\ & {\mathrm{T} _ {2} (\mathrm{a}, \mathrm{b}) = \mathrm{ab}} \\ & {\mathrm{T} _ {2. 5} (\mathrm{a}, \mathrm{b}) = (\mathrm{a} ^ {- 1} + \mathrm{b} ^ {- 1} - 1) ^ {- 1}} \\ & {\mathrm{T} _ {3} (\mathrm{a}, \mathrm{b}) = \min (\mathrm{a}, \mathrm{b})} \end{array}
$$

Their corresponding DeMorgan dual T-conorms, denoted by $S_{i}(a,b)$ , are defined as: $S_{i}(a,b)=1-T_{i}(1-a,1-b)$ . Note that $T_{1}(S_{1})$ corresponds to the logical AND (OR) operation and $T_{3}(S_{3})$ to the fuzzy AND (OR). $T_{2}$ is the multiplicative AND – similar to that used in probability theory. For each calculus (represented by the above five T-norms), many operations have been defined in RUM to enable rule-based inference. Two basic operations (for simple rule-based inference) are described below:

![](/api/attachments/EH348CJ5/fulltext/images/4519d81814edd30ca2cf7990c89fe295e014ccabb329f463c123ca24209fa078.jpg)  
Fig. 9. Effects of different uncertainty calculi.

Antecedent Evaluation: To determine the aggregated certainty range [b, B] of the n clauses in the antecedent of a rule, when the certainty range of the ith clause is given by [bi,Bi]:

$$
[ b, B ] = \left[ T _ {i} \left(b _ {1}, b _ {2}, \dots , b _ {n}\right), T _ {i} \left(B _ {1}, B _ {2}, \dots , B _ {n}\right) \right]
$$

Conclusion Detachment (Modus Ponens): To determine the certainty range, $[c,C]$ of the conclusion of a rule, given the aggregated certainty range, $[b,B]$ of the rule premise and the rule sufficiency, S, and rule necessity, N:

$$
[ \mathrm{c}, \mathrm{C} ] = \left[ \mathrm{T} _ {\mathrm{i}} (\mathrm{S}, \mathrm{b}), 1 - \left(\mathrm{T} _ {\mathrm{i}} (\mathrm{N}, (1 - \mathrm{B}))\right) \right]
$$

These five calculi provide the user with an ability to choose the desired uncertainty calculus starting from the most conservative $(T_{1})$ to the most liberal $(T_{3})$ . $T_{1}(T_{3})$ is the most conservative (liberal) T-norm in the sense that for the same input certainty ranges of facts and rule sufficiency and necessity measures, $T_{1}(T_{3})$ shall yield the minimum (maximum) degree of confirmation of the same conclusion. This is illustrated with the help of a simple example in Figure 9. Note that with $T_{1}$ there is complete ignorance about the conclusion C while with $T_{3}$ the conclusion C is confirmed to the degree 0.5 and has a degree of ignorance of only 0.2 (0.7 - 0.5). There is no one “correct” calculi. The calculus (T-Norm operator) chosen will depend on the user’s perception of the importance for certainty about the concerned facts. Observe that the choice of five different uncertainty calculi (corresponding to the five different T-Norm operators) gives the user the choice to explicitly represent the fact that certain inference paths are more important than others. This is not easily done if a single uncertainty calculi were chosen. To summarize, the role of the T-Norm based uncertainty calculus can be described as:

\- Giving the user a choice of uncertainty calculi ranging from the conservative (Boolean) to the liberal (fuzzy)

\- To allow the user to reflect the relative importance of the different premises for the conclusions in a rule by the choice of the appropriate T-Norm operator for that rule and

\- To represent the importance of the (aggregated) premises for the conclusion by the choice of the sufficiency and necessity measures.

The uncertainty calculi of RUM used in MARS is anchored on the semantics of many-valued logics and is possibilistic in nature. References [6,7] describe a comparison of RUM's T-Norm based uncertainty calculi with other reasoning with uncertainty systems, such as Modified Bayesian, Certainty Factors and Dempster-Shafer.

## 4.3. Monitoring dynamic environments

MARS uses the belief revision mechanism of RUM to support reasoning under dynamic environments. The belief revision mechanism detects changes in the input, keeps track of the dependency of the intermediate and final conclusions on these inputs, and maintains the validity of these inferences. For any conclusion made by a rule, the mechanism monitors the changes in the certainty measures that constitute the conclusion's support. Validity flags are used to reflect the state of the certainty. For example, a flag can indicate that the uncertainty measure is valid, unreliable (because of a change in support), too ignorant to be useful, or inconsistent with respect to the other evidence. A lazy evaluation is performed on the changes propagated by variations in the environment.

Consider the simple rule graph shown in Figure 10. Assume that the graph has been evaluated initially yielding a value of rule conclusion, C3. Thus the flags of all the rule premises and conclusions – indicated by circles – are “good”. Now if at some later time there is some change in the value of premise P11, then its flag is changed from “good” to “bad”. The change in flags is propagated down the rule graph, i.e., the flags of conclusions C1 and C3 are also changed to “bad”. Note that the new value of C3 is not computed when its flag is changed. If later, the system tries to retrieve the value of C3, the inference mechanism notices that the flag of C3 is “bad”. It then recomputes only that part of the rule graph whose flags are “bad” to obtain the new value of C3. In this example, are simplified the flags to two values “good” and “bad”. Other kinds of flags (as explained above) are also supported.

All simulators in MARS utilize the above described belief maintenance mechanism to constantly monitor the external world and ensure that all facts and assumptions used for reasoning and planning are still valid. If any critical data values change, the belief maintenance mechanism conveys information about the changes to the planning modules in the simulators. The planning module than evaluates the urgency and importance of the change to decide whether to simply ignore the change or replan and take some corrective action(s). For example, the raider may have taken on a particular debt burden on the assumption of a certain interest rate. If the interest rate fluctuates, the planning model of the raider simulator has to re-evaluate the debt burden and take necessary corrective actions.

## 4.4. Strategy formulation process

Possible strategies and actions are organized in a hierarchy, called the strategy hierarchy. Choices higher up in the strategy hierarchy have a high strategic intent, while choices near the leaf nodes in the strategy hierarchy have a high tactical (or incremental) content. A simplified representation of the partial strategy hierarchy for the raider simulator is depicted in Figure 11. At the top level, the raider can only adopt one of the two possible strategies: attack the target or retreat and concede defeat. Assuming that he chooses the attack strategy, there are several different strategies for attack: toe-hold (slowly acquire stock in the target), bear-hug (make a private merger offer to the company) or tender-offer (make a public merger offer). Subsequent to his choice of any one of these strategies for attack, there are further options to be chosen from. If he chooses the toe-hold strategy, he can acquire the toe-hold in the target by buying either from the market or directly from some friendly investors. The bear hug strategy leads to two options: try to contact the target management either directly or through some indirect (intermediate) contacts. Similarly, if the tender offer strategy has been chosen, the strategy for structuring the tender offer has to be chosen: either one-tier (one price offered for all stocks) or two-tier (a higher price offered for stocks sold early on).

![](/api/attachments/EH348CJ5/fulltext/images/11fc2abae35bb7cd8b93ae5d0fe3f6b1771324cf4c6fb7f674951cb5b154a72a.jpg)  
Fig. 10. A simple rule graph.

![](/api/attachments/EH348CJ5/fulltext/images/39eacf3b51fa1b4b7d687abc455c4be78e3054913e14bb3ed45adf75d018f7f6.jpg)  
Fig. 11. Simplified plan hierarchy for the raider.

In general there are several competing avenues of strategy formulation at each node of the strategy hierarchy. Complex networks of rules are used to evaluate the degree of desirability of different possible strategies at every stage. The T-Norm based interval valued uncertainty calculus of MARS (described earlier) is used to compute the uncertainty in the desirabilities of the various strategic options.

Based on his choice of appropriate strategies, the raider has to execute certain actions to achieve short term goals in consonance with his long term strategy and goals. These actions are represented by plan scripts $[27]$ , shown as rectangles at the leaf nodes in Figure 11. A plan script is simply a set of actions which are executed each time the associated choice is chosen from the strategy hierarchy. For example if the direct bear hug strategy is chosen, the associated plan script will contain actions which call for the raider simulator to determine an appropriate value for the target company, find a suitable private communication channel, send a private merger offer to the target and take appropriate actions to react to the target's response. Not all actions need to executed during every planning cycle. Thus, though a raider may decide to try the direct bear hug strategy for a number of consecutive planning cycles (see Figure 6), he will send the initial private tender offer only when the bear hug strategy is first selected. During later cycles, the raider simulator will select appropriate responses to the target's actions (such as raising the offered price if the target indicates the willingness to accept the offer for a sweetened merger offer). Note that scripts exist for all nodes in the strategy hierarchy (although they are only shown for the leaf nodes in Figure 11 for clarity of representation).

The belief maintenance mechanism existing in MARS aids in achieving a balance between strategic and incremental planning. Changes in the external world which affect the current choice of particular strategies are flagged to the system. Any switch in chosen strategies is dependent on the magnitude of change in the interval valued representations giving the desirabilities of different strategic options. Thresholds are set which discourage rapid changes in chosen strategies high up in the strategy hierarchy (to keep long term strategic planning stable) and encourage smooth incremental transitions (between chosen strategies) down the strategy hierarchy (to react flexibly to the external world). More details on the planning processes within MARS are given in references $[4,5]$ .

## 4.5. Feedback and learning

An important part of the process of planning is an ability to learn from prior experience. MARS supports a library of cases which stores the cumulative experience from prior situations. The software architecture of the case library is similar to rules. Each prior situation (case) stored in the case-library contains several case templates. The structure of each case template is similar to the structure to individual rules (see Section 4.1) and can be simply described as:

premise-list %factors in the prior case relevant for the event to be true

conclusion-list %the event described by this particular case-template

context-list %the context in which this event occurred in the prior case

<table><tr><td>sufficiency/necessity</td><td>%the degree of importance of the factors for the event to occur</td></tr><tr><td>T-Norm operator)</td><td>%defines the relative importance of the various factors</td></tr></table>

However, the semantics of the above case template is different from that for conventional rules. The above case-template is to be interpreted as defining the factors which were relevant for a particular event to occur in a certain prior case. The chosen T-Norm operator and the sufficiency/necessity measures define respectively the relative importance of the various factors and the degree of importance of the factors for the occurrence of the event (see Section 4.2).

Any particular M and A scenario can be described by an aggregation of case templates of the form shown above. When needed (such as for determining the possibility of success of an antitrust suit), the planning modules of the various simulators in MARS explore the case library to retrieve relevant prior information and utilize them in the current reasoning processes. References $[13,14]$ describe the approach taken in MARS to integrate this learning from prior history into the reasoning processes without altering the conventional inference engine of rule-based reasoning. Though desirable, it is not currently possible to automatically update the case library with a description of the active M and A scenario. All updates to the case library have to be made manually.

## 5. Conclusions

This concluding section of the paper summarizes the limitations of conventional DSS and suggests extensions to DSS for adequately supporting planning processes.

## 5.1. Limitations of conventional DSS

The primary strengths of conventional DSS are in the relatively structured aspects of the M and A process, where some well accepted quantitative models exist, and the required data are available reliably and publicly. Commercial M and A DSS (see Section 3.1) usually use quantitative models which are based on a set of assumptions about the world. These assumptions are not always satisfied, and thus the results generated are sometimes suspect. A common problem is the assumption that all data input to the model are fully correct and reliable. In practice, knowledge about the confirmation or refutation of data values is usually partial.

Conventional DSS pass on to the user the responsibility for interpreting the outputs of quantitative models. It is actually the interpretation of these results in the context of the current world that makes the results useful for planning. The problem of making sense of the results of models gets more complicated when one or more models generate different answers for the same variable. Under such conditions, the choice of the correct data values to use requires a substantial amount of context dependent, qualitative reasoning. The reliance of models on quantitative data also often results in qualitative data being ignored. Qualitative data are valuable for many aspects of reasoning and cannot be ignored in the process of planning a M and A.

A M and A deal evolves over time, and chosen strategies may change over time. For example, it is common for the raider to change the structure of a tender offer depending upon the response of the target management and shareholders. Planning this process requires continuous monitoring of the changing situation. Conventional DSS typically focus on one-time decisions and cannot provide adequate decision support for the temporal dimension of the M and A process. An important consequence of ignoring the temporal aspects of planning is that these DSS cannot learn over time. They have no capabilities for capturing, storing, and learning from prior experiences.

To summarize, the limitations of conventional DSS are:

\- A dominant reliance on quantitative models and a consequent lack of emphasis on qualitative models;

\- An inability to use the context of the problem to interpret the results of models (this being burdened on the user);

\- Poor support for integrating answers from different models;

\- Inadequate support for reasoning with uncertain and incomplete sets of data;

\- An inability to monitor the temporal progress of planning processes and react flexibly to changes; and

\- Poor facilities to support learning.

## 5.2. Planning support systems

The decision support provided by MARS from the perspective of any one player (such as the raider) is depicted conceptually in Figure 12 [15]. The MARS system has a variety of models (quantitative, heuristic and case-based) that are used for reasoning and planning. Different models can produce different answers for the same variables. For example, a raider may have a set of rules (heuristic model) to determine the possibility of an anti-trust move succeeding given the current situation. The raider may also attempt to determine the possibility of anti-trust success by comparing the current situation with similar prior situations (case-based model). These two models shall, in general, yield different answers. MARS uses the confirmation/refutation measures associated with the two models along with the T-Norm based uncertainty calculus to generate an integrated value for the degrees of confirmation and refutation of the possibility of success of an anti-trust move. The integrated answers for data values are used for planning by the system.

The planning module in MARS uses a rule-based approach to interpret the answers produced by the models and suggest possible planning/action strategies to the user. The planning module continuously monitors the external world (with the help of the belief maintenance system) for any changes which might affect its planning decisions. Note that the system has assumed to a large extent the burden of interpreting the answers of models and planning (it is no longer on the user). The user can, if necessary, provide data to the planning module and over-ride the generated planning decisions. A history module stores previous states of the world and provides relevant prior experiences for use in case-based models. After certain actions are executed (either by the user or the system), the planning module begins to consider its next phase of action, given the context of its prior planning knowledge. This enables the system to learn while planning and to react continuously and prudently to changes in the external world. This can be seen in Figure 6, where the raider (and other) simulator(s) plans for the best action during each cycle of the simulation. It does not begin planning afresh during each cycle, but plans in the context of the known history of planning, the current state of the world and the predicted future course of actions. This effectively preserves the temporal dimension of planning.

![](/api/attachments/EH348CJ5/fulltext/images/f87dcb1e62fcad8e05ea24e50cfedf5a89d3fee0dd22b72a404a7eae71385ec0.jpg)  
Fig. 12. A planning support system.

Figure 12 reflects the requirements imposed on planning in M and A and highlights important features to be supported in a planning support system. The most important of these features are:

\- Support for a variety of models (both quantitative and qualitative);

\- Integration of answers produced by different models for the same variables;

\- The transfer of a significant burden of interpreting (and planning with) the results of the models from the user onto the system;

\- Support for the temporal dimension of the decision making process (by using past history and future predictions for planning); and

\- An ability to learn from prior experience.

## References

[1] AAAI Spring Symposium Proceedings on Planning in Uncertain, Unpredictable or Changing Environments, Stanford, 1990.

[2] J. Aragones and P.P. Bonissone, PRIMO: A Tool for Reasoning with Incomplete and Uncertain Information, in Proceedings of the 3rd International Conference on Information Processing and Management of Uncertainty in Knowledge-Based Systems, Paris, pp. 891–898, July, 1990.

[3] P.P. Bonissone and S. Dutta, MARS: A Mergers and Acquisitions Reasoning System, Computer Science in Economics and Management, Vol. 3, No. 3, pp 239–268, Kluwer Academic Publishers, 1990.

[4] P.P. Bonissone and S. Dutta, Merging Strategic and

Tactical Planning in Dynamic, Uncertain Environments, in Proceedings of the DARPA Workshop on Innovative Approaches to Planning, Scheduling and Control, pp 379–389, San Diego, Nov. 1990.

[5] P.P. Bonissone and S. Dutta, Merging Strategic and Tactical Planning in Dynamic, Uncertain Environments, in the Proceedings of the 8th IEEE Conference on AI Applications, Monterey, California, March 2–6, 1992.

[6] P.P. Bonissone, S. Gans and K.S. Decker, RUM: A Layered Architecture for Reasoning with Uncertainty, in Proceedings of the 10th International Joint Conference on Artificial Intelligence, pp. 891–898, 1987.

[7] P.P. Bonissone, Summarizing and Propagating Uncertain Information with Triangular Norms, in International Journal of Approximate Reasoning, Vol. 1, No. 1, pp. 71–101, North Holland, 1987.

[8] Business Week, The Best and the Worst Deals of the '80s, January 15, pp. 40–48, 1990.

[9] P. Cohen and E.A., Feigenbaum, The Handbook of AI, Vol. III, Addison Wesley, 1982.

[10] Computational Intelligence, Special Issue on Planning, Vol. 4, No. 4, Nov. 1988.

[11] A.P. Dempster, Upper and Lower Probabilities Induced by a Multi-valued Mapping, Annals of Mathematical Statistics, 38, pp. 325–339, 1967.

[12] S. Dutta and P.P. Bonissone, An Approach to Integrating Diverse Reasoning Techniques, in Proceedings of the General Conference on 2nd Generation Expert Systems and their Applications – 10th International Workshop, Avignon, France, pp. 37–51, 1990.

[13] S. Dutta and P.P. Bonissone, Integrating Case Based and Rule Based Reasoning, International Journal of Approximate Reasoning, Vol. 8, pp. 163–203, 1993.

[14] S. Dutta and P.P. Bonissone, Integrating Case Based and Rule Based Reasoning: The Possibilistic Connection, in Proceedings of 6th Conference on Uncertainty in AI, Cambridge, MA, pp. 290–300, 1990.

[15] S. Dutta, Decision Support for Planning: Experiences from the Mergers and Acquisitions Domain, in DSS-91 Transactions, Proceedings of the 11th International Conference on Decision Support Systems, I. Zigurs (Ed.), June 3–5, Anaheim, CA, pp. 142–155, 1991.

[16] R.C. Ferrara, Mergers and Acquisitions in the 1980s: Attack and Survival, Practising Law Institute, New York, 1987.

[17] R. Firby, An Investigation into Reactive Planning in Complex Domains, in Proceedings of the 6th National Conference on Artificial Intelligence (AAAI), pp. 202–206, 1987.

[18] M. Georgeff and A. Lansky, Reactive Planning and Reasoning, in the Proceedings of the 6th National Conference on Artificial Intelligence (AAAI), pp. 677–682, 1987.

[19] G.A. Gorry and M.S. Scott-Morton, A Framework for Management Information Systems, Sloan Management Review, 55–70, Fall 1971.

[20] G.A. Gorry and M.S. Scott-Morton, A Framework for Management Information Systems, SMR Classic Reprint, Sloan Management Review, pp. 49–61, Spring 1989.

[21] G.P. Huber and R.R. McDaniel, The Decision-Making Paradigm of Organizational Design, Management Science, Vol. 32, No. 5, pp. 572–589, May 1986.

[22] P.S. Jacobs and L.F. Rau, SCISOR: Extracting Information from Online News, Communications of the ACM, pp. 88–97, Nov. 1990.

[23] R.L. Kuhn, Mergers, Acquisitions and Leveraged Buyouts, Vol. IV, Dow-Jones Irwin, 1990.

[24] J.G. March and H.A. Simon, Organizations, John Wiley and Sons, Inc., New York, 1958.

[25] A. Newell and H.A. Simon, Human Problem-Solving, Englewood Cliffs, Prentice Hall, New Jersey, 1972.

[26] M.L. Rock, The Mergers and Acquisitions Handbook, McGraw-Hill, 1987.

[27] R.C. Schank, Scripts, Plans, Goals and Understanding, Lawrence Erlbaum, 1977.

[28] B. Schweizer and A. Sklar, Associative Functions and Abstract Semi-groups, Publicationes Mathematicae Debrecen, Vol. 10, pp. 69–81, 1963.

[29] H.A. Simon, The New Science of Management Decision, Harper and Row, New York, 1960.

[30] W. Swartout, DARPA Workshop on Planning, AI Magazine, Vol. 9, No. 2, pp. 115–130, 1988.

[31] R. Wilensky, Meta-Planning: Representing and using knowledge about planning in problem solving and natural language understanding, Cognitive Science, 5, pp. 197–233, 1981.

[32] D. Wilkins, Practical Planning, Morgan Kaufmann Publishers, 1988.
