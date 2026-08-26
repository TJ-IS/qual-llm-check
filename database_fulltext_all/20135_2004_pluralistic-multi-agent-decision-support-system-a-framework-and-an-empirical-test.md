---
otero_id: 20135
otero_key: "GWTNAF5A"
title: "Pluralistic multi-agent decision support system: a framework and an empirical test"
authors: "Rustam Vahidov; Bijan Fazlollahi"
year: "2004"
journal: "Information & Management"
doi: "10.1016/j.im.2003.08.017"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Pluralistic multi-agent decision support system: a framework and an empirical test

Rustam Vahidov<sup>a,\*</sup>, Bijan Fazlollahi<sup>b</sup>

<sup>a</sup>Department of Decision Sciences & MIS, John Molson School of Business, Concordia University, Montreal, Que., Canada H3G 1M8 <sup>b</sup>Institute of International Business, Robinson College of Business, Georgia State University, 35 Broad Street, Atlanta, GA 30303, USA

Received 17 December 2002; received in revised form 7 July 2003; accepted 23 August 2003

Available online 5 December 2003

## Abstract

Recent research in decision support systems (DSSs) has focused on building active cooperative intelligent systems. Research in agent-based decision support is a promising stream in this direction. This paper proposes a framework for a pluralistic multiagent decision support system (MADSS). The distinguishing feature of the proposed approach is its organization around human decision making process. The framework builds upon the decision support pyramid with agents organized into groups according to the phases of the problem solving model. We outline the design principles and develop architecture for MADSS. The framework is illustrated through an investment MADSS prototype. The results of the empirical test are presented. <sup>#</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Intelligent agents; Multi-agent systems; Decision support systems; Pluralistic models; Critiquing systems

## 1. Introduction

In recent years providing effective decision support has become more important due to: increased employee empowerment, heightened requirements for speed and quality in managerial decisions, and increased accessibility to a vast amount of information through electronic networks [37]. Furthermore, the emergence of the electronic economy has profoundly increased the need for decision support [58].

Research in decision support system (DSS) design has been shifting from a traditional ‘‘toolbox’’ system organization towards a more collaborative and active paradigm [10,40]. In particular, researchers have stressed the importance of providing higher cognitive level support [52] including encouragement of divergent processes, generation of decision alternatives [21], and automated critiquing of alternatives [24]. However, past research has not addressed the issue of the integration of piece-meal prescriptions for building more effective DSSs under a unified approach.

The rapidly growing areas of intelligent agents (IAs) and multi-agent systems (MASs) offer the opportunity for building more effective systems using a unified approach based on sound theories. The promise that agent-based technologies holds for enhancing DSS capabilities is recognized by many researchers [6,14,16,38,78]. IAs possess attractive features including: autonomy, proactiveness, reactivity, reasoning capability, social ability (interaction with the environment, user, and other agents), and incorporation of human-like features, e.g., beliefs, desires, intentions, commitments, motivations, etc. In our view, these features have great potential in empowering DSSs beyond the capabilities of the old ‘‘toolbox’’ model.

The purpose of this work is to introduce and investigate the effectiveness of the framework for pluralistic multi-agent decision support systems (MADSSs). The word ‘pluralistic’ in the context of our work relates to the multitude and distinctiveness of information sources, viewpoints, and perspectives incorporated in our framework. Unlike previous attempts of combining agent technologies with DSSs, our work aims at laying the foundation for development of an agent-based DSS that parallels the human problem solving process. Agents are organized by their roles according to different phases of problem solving. They interact with the user, the environment, and each other, to improve the decision making process.

## 2. Agents and MASs

The development of IAs and MASs has recently gained popularity among IS researchers [25,30]. Despite the growing body of theoretical work and applications of agent-based technologies, there is no accepted definition of the term ‘‘agent’’. Wooldridge and Jennings [74] distinguish weak and strong notions of an agent. In the weak notion, they view an it as a system that has the properties of autonomy, social ability, reactivity, and proactiveness. The strong notion stresses the appropriateness of ascribing mental ideas to agents. Hess et al. [27] distinguish essential vs. empowering features of agents. The former include goal orientation, persistence, and reactivity, whereas the latter include artificial intelligence, mobility, and interactivity. For our work we view agents as distinct autonomous active entities. In the area of ISs, IA research has aimed at integration of IS, people, equipment, decision support, and knowledge management [41,48].

Inherent in the concept of an agent are the notions of delegation and autonomy. These imply limited direct control and, therefore, increased potential for pluralism (diversity) in a system that incorporates multiple agents. Researchers in agent technologies often find it useful to use mental attitudes to describe these systems (see e.g. [73]).

Study of MAS originates from research in distributed artificial intelligence (DAI) [18,23], where the activities of the system are distributed among multiple nodes for cooperative problem solving. In MAS, agents have their own goals that may be in conflict with goals of other agents. For a review of applications of IA and MAS, see [31,46].

The question of problem solving by multiple agents is of utmost importance in MAS research. Wooldridge and Jennings [75] define cooperative problem solving as a situation when ‘‘a group of logically decentralized agents choose to work together to achieve a common goal’’. Yang and Zhang [77] proposed a comprehensive framework for distributed problem solving (DPS). In particular, in one of their models (DPS2) tasks are allocated to multiple agents that produce feature solutions that are synthesized into the final solution. This framework advocates use of multiple agents for tackling a single task, thus relying on the use of pluralistic models. Yang and Zhang refer to Kornfeld and Hewitt’s scientific community metaphor [34] that proposes the diversity based approach intrinsic in scientific communities to problem solving in general.

Within similar lines Zhang proposed a way to synthesize final solutions in systems where different agents use different inexact reasoning models to solve a problem [79]. Malhotra et al. [39] proposed the use of multiple diverse classification models where the consensus is sought among the models for producing the final outcome. A special case of synthesis, competitive synthesis, occurs when only the best proposed solution is selected [60]. The pluralism-based approach with competitive synthesis was used for search problems, where the categories of agents included experts, specialists, referees and supervisors [17]. Murthy et al. [45] described a DSS that uses multiple cooperating agents that evolved decision alternatives for multiple inter-related scheduling tasks with an application in the paper industry. Their DSS generates alternatives using so called ‘‘A-Team’’ with multiple constructor, improver, and destroyer agents incorporating diverse OR/MS models. Other similar work included the use of multiple agents for generating solutions with their subsequent evaluation in terms of appropriateness, proposer competence, and other relevant factors [2,22].

One can distinguish two categories of DPS strategies in MAS: each agent is assigned a separate problem, or a part of the problem, and each agent attempts to solve the entire problem (which is similar to DPS2).

While the first category is most appropriate for DSSs supporting inter-related decisions and group DSSs, our interest here is in the second category.

## 3. DSSs incorporating agents

A recent analysis of research in IS revealed that DSSs had been one of the most popular research topics [13]. However, traditional DSSs offer a passive form of support, where users needed to have full knowledge on how to use the relevant models, data sources, and other tools and take initiative to perform all necessary operations effectively.

Recently researchers have argued in favor of making DSS a more active participant in the decision making process. The vision has favored a higher degree of system involvement and collaboration with the human in the decision process. Within the context of active support Raghavan [53] posited that DSSs should be able to stress divergent processes. More recently, some researchers emphasized the importance of a ‘‘holistic’ approach [44].

It has been recognized that ‘‘the potential contributions of IAs to DSSs is enormous’’ [72]. This has been re-emphasized in the recent special issue of the DSS journal on the next decade of DSS [11,59]. Autonomy, reactivity, social ability, and proactiveness of agents can facilitate active decision support. ‘‘Mentalistic’ characterization and reasoning capability can promote high-level cognitive processes, including qualitative reasoning, handling soft information, and alternative generation. Furthermore, the artificial ‘‘persona’’ view of agents [42] can contribute towards stronger collaborative relationships between a human and a DSS.

Rao et al. [54] proposed an agent-based system where the overall problem was decomposed and each subproblem assigned to a specific agent that had the corresponding competence. Shaw and Fox [57] proposed use of agents for group decision support within an organization. Bui and Lee [9] proposed an agent-based organizational DSS with the emphasis made on the types of coordination in such system. Pinson et al. [50] proposed an agent-based distributed DSS for strategic planning, where the agents possessed domain-specific knowledge and communicated via a blackboard to ensure consistency of solutions. Wang and Liao [71] proposed the framework of cooperative decision systems, which is a distributed IS. In their architecture they have client, server, and central agents that engage in communication for DPS. Sycara et al. [67] proposed an architecture for decision support using agents called Retsina, where the network of interface, task, and information agents would be used to deliver the right information to the right user for decision making purposes. Bordetsky and Mark [8] described a multi-agent approach to casebased decision support and groupware coordination. Zhuge [80] proposed an agent-based ‘‘cognitive’’ workflow approach for distributed team co-operation with application to software development process.

Most of these approaches either consider large decomposable problems, naturally distributed environments, distributed information sources, or group decision making. Our interest is in supporting the essence of decision making as a problem solving activity. From this point of view, the work by Angehrn [3] is interesting. He introduced the notion of stimulus-based agents in DSSs. In these the virtual team of agents collaborates on a given problem in a conceptual space called an ‘‘arena’’. The virtual team includes framing, solving, and process agents that actively participate, intervene, and propose alternative courses of action during decision making. The vision was recently illustrated using DSS with case-based reasoning, where the ‘‘story-teller’’ and ‘‘advisor’’ agents intervened in multi-criteria decision making process with suggestive guidance [4]. While the use of guidance could lead to user miscalibration [32] and increased restrictiveness [61] of DSS, the idea of active ‘‘intermediary’’ agents in DSS is very appealing.

Another interesting approach was proposed in the work by Hess et al., where the agents were organized by data, models, and user interface components in accordance with the system view of DSSs. The agents were responsible for monitoring both the environment and the user, generating proposals as the data changed, and learning user preferences. Variance analysis was used as an illustration. The work, however, aimed at enhancing DSSs with agents, with continuous monitoring of relevant data and faster response. While definitely promoting active support, the approach did not target direct support of decision making as a problem solving activity. Furthermore, the systemdriven organization of agents (i.e. by models, data, and interface) did not realize the opportunities of man–machine collaboration and, in essence, introduced an agent toolbox.

The goal of our work is to propose a framework for an agent-based DSS that targets improved decision making, parallels human problem solving processes, and supports the major phases of decision making. In this work we adopt Simon’s model [64] of problem solving.

## 4. Insights from problem solving and epistemology

One of the key themes in DSSs is that they aim at illstructured problems, which Stabell [66] characterized as one where: there are ambiguous, or conflicting objectives; the effect of actions on outcomes is uncertain; and it is not clear which actions have effect on the outcomes. The fundamental principles of problem solving include separation of evaluation and judgment from idea generation and promoting divergent (idea generation) and convergent (evaluation) activities during these phases [49]. Ironically, traditional modelbased DSSs do not support the divergence–convergence principles of problem solving. Furthermore, in what-if DSSs alternative generation and evaluation are not separated. Evans [20] argued that a computer algorithm for supporting problem solving would generate diverse alternatives in a single run. He further referred to the following comment by Woolsey: ‘‘When you give the manager a spread of alternatives, with good points and bad points outlined, few can argue that the work is insufficient’’ [76].

In addressing ill-structured problems characterized with high levels of uncertainty and ambiguity, one cannot therefore guarantee the effectiveness of solutions if one relies on a single model. There is an intrinsic need for a variety of approaches and a pluralism of views for effective decision processes. Hewitt [28] introduced the notion of due process as a way of dealing with conflicting ‘‘Microtheories’’ in organizations. Hewitt’s work largely correlated with the concept of the ‘‘scientific community metaphor’’ introduced by Kornfeld and Hewitt. This built on a view of scientific communities as highly parallel, pluralistic systems that work concurrently. Kornfeld and Hewitt advocated this diversity to be utilized in design of parallel systems. In Kuhn’s [35] view the diversity of opinions among scientists arises mostly from their different values, although, divergent beliefs are also possible when there are several schools of thought. Kuhn’s work provided an important insight: that there are at least two sources of pluralism in scientific research communities—diversity in beliefs and diversity in values.

Churchman’s work on inquiring systems has inspired the vision of a DSS incorporating Kantian, Hegelian, and Singerian modes of inquiry [15]. These modes advocate the use of multiple models (Kant), debate and argumentation (Hegel), and incorporation of values and multiple worldviews (Singer) in informing decision processes. Simon [63] noted that pluralism is one of the essential criteria of analysis that informs the decision making process, and it is ‘‘. . . the guarantee of due process’’.

Within the context of IS research, Mingers put forward an argument that a pluralistic approach is essential in combining research methods. He pointed out that the research results will be ‘‘richer and more reliable if different research methods, preferably from different (existing) paradigms, are routinely combined together’’ [43].

## 5. A framework for MADSS: decision support pyramid model

## 5.1. Sources of pluralism and their relation to anthropomorphic features of agents

The concept of intentional systems lies at the core of mentalistic models of an agent. This framework allows us to describe and explain the behavior of complex systems in a familiar and convenient way it is especially important in our case since we base our framework upon a human decision making model. We use the terms views and values in our framework. By ‘‘views’’ here we imply a set of implicit and explicit relevant assumptions, knowledge, and skills used to pursue a given set of objectives that compose the knowledge and expertise of a particular agent. The term ‘‘values’’ denotes a set of relevant common objectives and preferences that an agent chooses to pursue. In other words, while values refer to ‘‘what’’ objectives to pursue, views provide alternative ways of answering the question of ‘‘how’’ to achieve the objectives. The models of decision analysis under uncertainty are examples of value-driven pluralism. Decision makers choose the basic behaviors of risktaking, worst-case scenario, minimizing regret (opportunity loss) and others depending on the values they hold. The adoption of an anthropomorphic description supports the two types of judgment (evaluative and predictive) [29], helps the user understand and relate to the behavior of the proposing agents from the intentional stance (i.e. knowing the intentional attributes of a proposer agent the user can understand the implications of its proposals), and facilitates the user view of the DSS as an active collaborator rather than a passive tool.

Sources of pluralism and their relations to aspects of ill-structured problems

<table><tr><td rowspan="2"></td><td colspan="2">Dimensions of pluralism</td></tr><tr><td>Ill-structured problems: Stabell</td><td>Ill-structured problems: Keen and Morton [33]</td></tr><tr><td>Views</td><td>The effect of actions on outcomes is uncertain</td><td>There is no best methodology to approach solving the problems</td></tr><tr><td>Values</td><td>Ambiguous, or conflicting objectives</td><td>The criteria for choosing the best decisions are not clear</td></tr></table>

The MADSS framework incorporates pluralistic agents that have diverse sets of views and values in approaching the problem and informs the decision maker about this diversity. Table 1 shows how this views and values approach relates to the characteristics of ill-structured problems.

## 5.2. The pyramid model

There are three groups of agents in the proposed multi-agent DSS design organized by the phases of Simon’s model: intelligence, design, and choice. The intelligence group incorporates agents that gather information from different electronic sources and the user in order to inform the user and other agents and to detect developing problems and opportunities. Use of agents for this task has been widely advocated. For example, Teo and Choo [68] stress the importance of automated gathering of relevant information for competitive intelligence. The design group normally has fewer ‘‘experts’’: proposers and analysts. They differ in the expertise they use, intrinsic values, and contextual competencies. The proposers submit their proposals, while the analysts perform supporting functions for the proposers. The next layer comprises two types of critiquing agents: positive (‘‘angel’’), and negative (‘‘devil’’) agents. They support the choice phase of decision making. The human decision maker resides at the top of the pyramid. The models aim at incorporating the power of teamwork in a single DSS (Fig. 1).

The pyramid delineates a general organization of the agents in a pluralistic multi-agent DSS. The human user can participate at any layer; i.e. collect certain types of information, generate, or refine the alternatives, and provide extra critique. From a problem solving perspective, the model facilitates the divergence–convergence principle (since the agents incorporate different views/values) and the principle of deferred judgment (since the alternatives are generated before the evaluation stage).

![](/api/attachments/GWTNAF5A/fulltext/images/587578c3806c14dd8540022c8748619bad6813bad525974415cedbca85154d2c.jpg)  
Fig. 1. The decision support pyramid.

Table 2  
Summary of design principles for the agents of design group

<table><tr><td colspan="2">Coverage</td><td colspan="3">Pluralism</td><td colspan="3">Quality</td></tr><tr><td>Views</td><td>Values</td><td>Value-driven</td><td>View-driven</td><td>Overall</td><td>Consistency</td><td>Robustness</td><td>Justifiability</td></tr><tr><td>All relevant views should be covered</td><td>All relevant values should be covered</td><td>Maximize value-driven pluralism</td><td>Minimize view-driven pluralism</td><td>Control overall pluralism</td><td>Agent&#x27;s behavior consistent</td><td>Agent&#x27;s behavior robust</td><td>Agent&#x27;s behavior justifiable</td></tr></table>

## 6. Design group

The role of the design group agents is to generate proposals for decisions. The proposers generate their candidate decisions based on their views and values. The analyst agents perform functions supporting the proposers. For example, they can provide the analysis of a situation from the viewpoint of a certain theory.

## 6.1. Design principles

\- Coverage of basic values. All basic standard desirable sets of objectives or values should be pursued in MADSS. For example, in an investment DSS there should be a risk-loving agent, risk-averse agent, and possibly a risk-neutral agent. The designer should identify all relevant values.

\- Coverage of different views. All relevant systems of views on how to achieve given sets of objectives should be incorporated into the system. Thus if a particular system of views is not dominated in a preference sense by other views in all input and value contexts, there should be an agent in the system incorporating that system of views.

\- Managing pluralism: maximizing value-driven pluralism. The divergence should be maximized among the agents with respect to their values.

\- Managing pluralism: minimizing view-driven pluralism. While there could be multiple views, it is possible that one is more appropriate for some contexts than some other view. Minimizing viewdriven pluralism should be achieved through attempting to identify the right contexts for different views (though there will still be some ‘‘gray’’ area).

\- Managing pluralism: controlling overall pluralism. The number of agents with different values and views should be limited in order to reduce the number of generated alternatives.

\- Quality: internal consistence. Each agent’s knowledge should be internally consistent, i.e. the same agent should not react differently to the same situations.

\- Quality: robustness. Each agent should be able to respond with the proposal in any situation, i.e. the proposers’ expertise should not be brittle.

\- Quality: justifiability. Any proposal of any proposer must be justifiable in terms of the underlying views/ values.

Table 2 summarizes the above principles for the design agents.

## 7. Choice group

## 7.1. Critiquing systems

We chose critiquing expert systems as a kernel for our choice agents. They can be viewed as a special type of systems that take a proposed decision as an input in addition to the description of the situation at hand and provide a critique of the decision as an output [62]. The primary purpose of the critiquing systems was to monitor the user’s actions and indicate possible errors.

We incorporated both negative and positive critiquing agents as components of MADSS. The devil’s role is to examine the user-proposed solution with the sole intention of finding possible violations, drawbacks, and potential problems. The angel’s role is to identify the strength of the proposed solution. Polarization of critique is helpful, since it is natural for a human decision maker to assess the alternatives in terms of their pros and cons.

In order to build a good critique, the system needs to incorporate certain types of knowledge. We distinguish the following types in our DSS: objective-related;

Table 3  
Summary of design principles for MADSS framework

<table><tr><td>Group</td><td>Types of agents</td><td>Organization</td><td>Purpose</td><td>Phase of decision</td><td>Mode of inquiry by churchman</td></tr><tr><td>Intelligence agents</td><td>Information</td><td>By sources of information</td><td>Information delivery</td><td>Intelligence</td><td>Lock</td></tr><tr><td>Design agents</td><td>Proposing</td><td>By views and values</td><td>Alternative generation</td><td>Design</td><td>Kant, singer</td></tr><tr><td>Choice agents</td><td>Critiquing</td><td>By negative and positive critique</td><td>Identifying pros and cons</td><td>Choice</td><td>Hegel</td></tr></table>

preference-related; soft constraints-related; expertrelated and reactive (debate).

The objective-related critique knowledge (O) involves the achievement of the key objectives of the user. For example, the key objective could be maximizing the expected profit. Preference-related critique knowledge (P) reflects the decision maker’s preferences. We also incorporated soft constraints in our critiquing agent knowledge. These are different from hard constraints, in that their violation can be tolerated, to some degree. For example, the soft constraint for a business firm could be to avoid large inventory build-ups. The soft constraints-related critique here (S) is aimed at showing the way that these are addressed. Expert related critiques (E) examine the appropriateness of a certain proposer’s proposal in a given situation. For example, a technical analyst’s advice may not be appropriate for long-run investment decisions. In reactive critique knowledge (R), an agent considers the opponent’s critique in addition to the properties of the solution and those of the user to build a counter-critique. Both critique and counter-critique may be useful to the decision maker in better assessing the proposed solution.

A more detailed discussion of the use of critiquing agents at the choice stage can be found elsewhere [70]. Summary of important principles in our framework is given in Table 3.

## 8. Architecture for pluralistic MADSS

Fig. 2 shows the architecture of MADSS consisting of entities (E) and agents (A). The major components of the architecture include: user interface; data and models (E); intelligence team (A); design team (A) and choice team (A).

![](/api/attachments/GWTNAF5A/fulltext/images/907ff6bf924c819c951d26d4f5a0bf3d3d699543c03f9b474f7f1ef271b28837.jpg)  
Fig. 2. The generic architecture of MADSS.

Data and models provide information (data) and services (models) to different agents and the user, if required. The intelligence team contains one or more information agents, the purpose of which is to obtain, aggregate, and assess relevant information. The design team contains analysts and proposing agents that examine the situation at hand and produce proposals (in general, the analysts may not be required).

The choice team consists of two types of agents: the positive and negative critique agents, which critique the proposals generated by the proposing team, as well as those modified/specified by the user.

During decision making, the proposers analyze the decision situation and generate their solutions based on their views and values. The critiquing agents analyze the proposals in terms of pros and cons. The proposing and critiquing agents may request additional information from the intelligence agents, if required. The user may try his/her own proposal, or modify/refine one of the generated proposals. The user may also perform sensitivity analysis, change some of the estimates and examine the impact of these changes on the generated alternatives and critique. The user evaluates the alternatives in light of the critique and exercises judgment in making the final choice.

## 9. MADSS prototype for investment decisions

To illustrate our approach and investigate the viability and benefits of the framework, we developed a prototype MADSS for investment decisions. The problem of investments requires selection of a weighted portfolio of securities that suits the investor’s objectives [19]. The problem is ill-structured, since the objectives of an investor with respect to return, risk, liquidity, time horizon, and other important criteria are not clear-cut and the performance of individual securities cannot be accurately predicted.

The purpose of the prototype MADSS was to assist the user (decision maker) in his/her investment decisions by determining a portfolio of securities. The prototype specifically targeted equity instruments (stocks) selected from the software industry. The prototype included the agents of the design and choice teams.

Table 4  
Organization of the pluralistic proposers

<table><tr><td rowspan="2"></td><td colspan="2">Views</td></tr><tr><td>Technical</td><td>Fundamental</td></tr><tr><td colspan="3">Values</td></tr><tr><td>Risk taking</td><td>Proposer 1</td><td>Proposer 3</td></tr><tr><td>Risk averse</td><td>Proposer 2</td><td>Proposer 4</td></tr></table>

The relevant data for the problem were downloaded from Internet sources.

The design team consisted of two analyst agents and four proposers. The analysts helped to identify a small subset of promising securities from which the proposers determined their portfolios and submitted them to the user. The analysts incorporated different sets of views, namely, two schools of thought in security analysis: fundamental analysis [55] and technical analysis [51]. The four proposers determined the portfolio, based on the analyst recommendations and the values (reflected in their objectives) that they held. The value dimension of the proposers here reflected their attitude towards risk. Each analyst advised two proposers. One of these in each of two groups was a risk taker while the other was risk averse. Table 4 summarizes the organization of the proposers.

Although the fields of portfolio management and security analysis have not been formally integrated, the design developed here offered a good approach to incorporating the two in one system. In the prototype, the analysts screened the set of securities using fuzzy rules and identified candidates for further analysis. The fundamental analyst essentially performed simplified ratio analysis comparing different securities in a standardized manner. The major categories of ratios included profitability, solvency, and value.

Technical analysis attempted to identify the trends and their turning points based on the preponderance of evidence using several indicators. These included moving averages of price and their crossovers, momentum, relative strengths, and others. The technical analyst used trend determining techniques to identify the securities that were likely to grow in value. An example of a common technical rule was:

IF Short Term MA crosses the Long Term MA from below THEN trend will be upwards (‘‘buy’’ signal).

The proposers determined portfolios of the fixed size (10 securities) made up from the securities available in

![](/api/attachments/GWTNAF5A/fulltext/images/9f55a3cef10c9ff5174d36b688a09450f386af71dd490368c23d9ca02410e7d3.jpg)  
Fig. 3. MADSS prototype interface.

the pool. Risk-taking proposers looked for ways of maximizing the expected return while accepting somewhat high risk, while risk-averse proposers trid to keep risk under control and still earn moderate return. The proposers accepted recommended stocks from their corresponding analysts and determined the actual proportions for these stocks in a portfolio through maximizing fuzzy objectives by using a simple iterative improvement search.

The choice team consisted of two critiquing agents that analyzed and critiqued the proposed portfolios. There were a number of important factors affecting investment decisions including expected return and risk, user preferences, and the source of the investment advice. Generally, one sought to maximize return while controlling risk. This knowledge was used for providing objective-related critique. If the user chose a portfolio with the expected return being high, the angel detected this and told user ‘‘the expected return of this portfolio is high.’’ The devil, on the other hand, could detect a high risk associated with the proposed allocation and prompt it to the user.

![](/api/attachments/GWTNAF5A/fulltext/images/0a1e39d9f34649f84e09c51ac9988877c3469627f3e42e298c4e14148166c1fd.jpg)  
Fig. 4. Critics.

Table 5  
Summary of dependent variables

<table><tr><td>Category</td><td>Variable</td><td>Description</td></tr><tr><td>Productivity/outputs</td><td>Return on portfolio</td><td>Accumulated wealth of portfolio</td></tr><tr><td rowspan="4">Process</td><td>Number of alternatives</td><td>Number of candidate decisions examined</td></tr><tr><td>Divergence of alternatives</td><td>How diverse are the alternatives</td></tr><tr><td>Quality of alternatives</td><td>Average potential return of alternatives</td></tr><tr><td>Time spent</td><td>Time spent to reach a final decision</td></tr><tr><td rowspan="3">Perception</td><td>Change in understanding/learning</td><td>The decision maker&#x27;s understanding of the problem/field</td></tr><tr><td>Satisfaction</td><td>Perceived satisfaction with the DSS</td></tr><tr><td>Confidence</td><td>The decision maker&#x27;s confidence in the generated decision</td></tr></table>

Fig. 3 shows the user interface of the prototype. The available stocks were listed in a box on the left (the actual names of stocks were coded to prevent the subjects in the experiment from using any prior knowledge about its performance). The return and risk estimates of the portfolio were displayed in the upper right-hand corner. Every time these were recalculated, critiquing agents started analyzing the newly defined portfolio. The central part of the screen contains portfolios generated by the proposers. Fig. 4 shows another example screenshot with the feedback from the critics.

## 10. Experiments

We performed experiments to investigate the effectiveness of the MADSS prototypes empirically. We compared the performance of the MADSS with that of a ‘‘traditional’’ DSS (TDSS), i.e., the passive DSS with data and models. The TDSS prototype was a subset of the MADSS including the models, data, and interface but not including the agents. Data in TDSS included historical information of stock performance, market performance indicators, and the financial data and ratios for the stocks. The models allowed calculations of the expected portfolio return and risk. The interface allowed viewing and selecting stocks into the portfolio, manipulating proportions of stocks in the portfolio, viewing relevant financial indicators of the stocks, and graphing historical performance of the stocks in terms of raw data and the moving averages. Our major expectation was that MADSS would promote higher effectiveness of decisions than the traditional DSS.

## 10.1. Variables

Different approaches have been proposed for measuring effectiveness of DSSs [1,26,47,56]. Sprague and Carlson [65] described four major categories: productivity, process, perception, and product measures. Keen and Morton [33] advised use multiple methods for evaluating DSSs including: decision outputs; changes in decision process; changes in managers concepts of decision situation; procedural changes; classical cost/benefit analysis; service measures; managers’ assessment of the system’s value and anecdotal evidence. The measure categories used here derived from these. Table 5 summarizes the dependent variables.

## 10.2. Research hypotheses

## 10.2.1. Decision outputs

The quality of the investment decisions is traditionally measured by the resulting return on the portfolio. The MADSS was expected to lead to better performance on the average, leading to:

Hypothesis 1. The portfolio selected by an MADSS user will yield higher return than the portfolio selected by TDSS user.

Hypothesis 2. The portfolio selected by an MADSS user will yield higher return than the market that both systems target.

One well-known criterion dealing with investor preferences is the expected risk level. The riskier the investment, the more the variance of the returns, and vice versa. A good system should lead to producing portfolios with the risk level adequate to user objectives/preferences:

Hypothesis 3. The ratio of the variances of portfolio returns produced by risk-seeking users to the variances of portfolio returns produced by the risk-averse users is greater for MADSS user than that for TDSS user.

Sharda et al. stressed the use of the variance of performance measures as an important indicator of the consistency of the decisions. An improved DSS would lead to more consistent decisions, and would therefore have less variance in the key decision criteria:

Hypothesis 4. Returns generated by the portfolios selected by MADSS users will have less variance than returns generated by the portfolios selected by TDSS users.

## 10.2.2. Decision process

Alternative generation is an important step in decision making. We expected that MADSS users would generate more diverse and promising alternatives than TDSS users:

Hypothesis 5. An MADSS user will examine no less alternatives than TDSS user.

Hypothesis 6. An MADSS user will generate no less diverse alternatives than TDSS user.

Hypothesis 7. An MADSS user will generate alternatives, which will potentially yield higher return on the average than TDSS user.

Another important process measure is the time required to reach a decision. The improved DSS should lead to a reduced time for reaching a decision.

Hypothesis 8. An MADSS user will require less time to reach a decision than TDSS user.

## 10.2.3. Perception

On the learning dimension, the MADSS user could learn more and improve understanding about investment problems than could a TDSS user, since the former was exposed to the divergence of approaches/ views on the investment process:

Hypothesis 9. An MADSS user will learn more about investment concepts than TDSS user.

We further expected the user to be more satisfied and confident in the decision using a more active system than the TDSS:

Hypothesis 10. An MADSS user will have more satisfaction with the system than TDSS user.

Hypothesis 11. An MADSS user will have higher confidence in final decisions than TDSS user.

## 10.3. Experimental design

The task here involved selecting a portfolio of stocks suitable for the user’s investment objectives and preferences. Once chosen, the portfolio was unchanged for a period of time (9 months). Each subject was asked to select 10 stocks and determine their relative weights in a portfolio. Prior to selection, the subjects indicated their investment objectives and preferences in terms of return and risk. The subjects then used available models in DSS to make their choice. In a multi-agent DSS the users also received the recommendations of the agents. Fifty software industry stocks were chosen with the condition that the data on these stocks should have been available at least from the beginning of year 1993. The DSS prototypes randomly chose a date from the mid-nineties and accepted the market situation at that time as a current situation. The stock symbols were coded X1 through XN to block the interference of any prior knowledge.

The subjects were able to view the past performance of the stocks, as well as the relevant financial indicators. In particular, widely used financial ratios dealing with profitability, solvency, and other aspects of a firm were made available. User-friendly GUI interface made it easy for subjects with moderate computer skills to view, analyze, select, and deselect stocks to determine the composition of a portfolio. The performance of the selected portfolios was then evaluated using historical data.

The subjects for the study were selected from the graduate and upper level undergraduate business administration students registered for courses at a major south-eastern US university. These subjects had exposure to the basic principles of investments as part of their general business education. Many were part-time students with working experience.

Return was measured by the weighted average of the individual stock returns. The number of alternatives generated was automatically recorded by the DSS prototypes. Every time the subjects specified a trial portfolio this alternative was recorded if it was new (different from the previously generated alternatives). Divergence of the alternatives was measured using the average distance measure between the consecutive portfolios (Hamming distance). The quality of alternative portfolios was measured as the average return they would have generated if selected as final portfolios. The time spent to reach a decision in minutes was automatically recorded by the systems. Learning was measured using a test on investment concepts before and after the treatment. The perceptive measures of satisfaction and confidence were measured by a questionnaire using seven-point Likert scale.

The measures for Hypothesis 3 were obtained as follows. Hypothesis 3 deals with the difference in ratios of variances for the two groups of users of DSSs. We use the following notation:

$\sigma _ { \mathrm { m r } } ^ { 2 }$ is the variance of return of portfolios produced by risk-taking MADSS users;

$\sigma _ { \mathrm { m a } } ^ { 2 }$ is the variance of return of portfolios produced by risk-averse MADSS users;

$\sigma _ { \mathrm { t r } } ^ { \overline { { 2 } } }$ is the variance of return of portfolios produced by risk-taking TDSS users;

\- $\sigma _ { \mathrm { t a } } ^ { 2 }$ is the variance of return of portfolios produced by risk-averse TDSS users.

We were interested in testing Hypothesis 3: $\sigma _ { \mathrm { m r } } ^ { 2 } / \sigma _ { \mathrm { m a } } ^ { 2 } > \sigma _ { \mathrm { t r } } ^ { 2 } / \sigma _ { \mathrm { t a } } ^ { 2 }$

The experiments only yielded single estimates of the above variances. Therefore, we decided to use simulations. First, we conducted the experiments and collected the data about the distributions of $r _ { \mathrm { m r } } , r _ { \mathrm { m a } } , r _ { \mathrm { t r } } ,$ and $r _ { \mathrm { t a } } .$ . We then approximated these distributions with known theoretical (normal) distributions and estimated the parameters of the distributions. Simulated returns based on the estimated distributions were generated and compared with the actual data. The comparison revealed adequacy of the simulated and actual data. We then generated multiple samples, calculated sample variances and their ratios, and treated these ratios as random numbers. Finally, we statistically tested the hypothesis.

The subjects were randomly assigned to one of the two types of DSS. They were given instructions on how to fill out a questionnaire, answer the test questions, and use the DSSs. The subjects filled out the questionnaire concerning their demographics (including major and the investment experience) and took a multiple-choice test measuring their knowledge of investment before proceeding to the DSS session. After completing the task, subjects answered the questionnaire concerning their confidence and satisfaction levels. The post-test was then given to measure the improvement of the subjects’ knowledge of investments concepts.

## 10.4. Results

A total of 125 subjects participated in an experiment. Among these, 19 did not complete the experimental task and were thus considered non-response. Among the 106 collected observations four were deleted on the basis of time spent to complete the DSS session. The decision was made to drop the observations if the time spent on this part was less than 2 min, since these subjects did not seem to have taken the task seriously. The remaining 102 observations were retained for further analysis. The average age of the participants was 25.6 years. The average work experience was 6.4 years. At least 50% of the participants reported having work experience of 5 years or more.

The subjects were randomly assigned to one of the two groups (MADSS: treatment vs. TDSS: control). Out of the total of 102 subjects exactly half (51) were in the treatment group, and the rest in the control group. Statistical tests supported the assumption of homogeneity between the two groups (results are available upon request to the authors). An instrument

Table 6  
Results of hypothesis testing

<table><tr><td rowspan="2">Hypothesis</td><td colspan="2">MADSS</td><td colspan="2">TDSS</td><td rowspan="2">P-value</td><td rowspan="2">Confirm. (α = 0.05)</td></tr><tr><td>Mean</td><td>S.D.</td><td>Mean</td><td>S.D.</td></tr><tr><td>Hypothesis 1—return: MADSS vs. TDSS</td><td>0.5203</td><td>0.1528</td><td>0.2868</td><td>0.1530</td><td>0.000</td><td>Yes</td></tr><tr><td>Hypothesis 2—return: MADSS vs. market</td><td>0.5203</td><td>0.1528</td><td>0.3129</td><td>0.0935</td><td>0.000</td><td>Yes</td></tr><tr><td>Hypothesis 3—achievement of objectives</td><td>1.3278</td><td>0.4064</td><td>0.9228</td><td>0.4064</td><td>0.000</td><td>Yes</td></tr><tr><td>Hypothesis 4—variances</td><td>0.5203</td><td>0.0233</td><td>0.2868</td><td>0.0234</td><td>0.861</td><td>No</td></tr><tr><td>Hypothesis 5—alternatives: number</td><td>5.4706</td><td>5.6012</td><td>3.6862</td><td>7.0781</td><td>0.081</td><td>Yes</td></tr><tr><td>Hypothesis 6—alternatives: diversity</td><td>0.5404</td><td>0.3353</td><td>0.0396</td><td>0.0730</td><td>0.000</td><td>Yes</td></tr><tr><td>Hypothesis 7—alternatives: quality</td><td>0.5249</td><td>0.1203</td><td>0.3018</td><td>0.1347</td><td>0.000</td><td>Yes</td></tr><tr><td>Hypothesis 8—time</td><td>6.5098</td><td>3.8490</td><td>9.6078</td><td>5.2653</td><td>0.001</td><td>Yes</td></tr><tr><td>Hypothesis 9—learning</td><td>3.5294</td><td>17.644</td><td>0.7843</td><td>13.091</td><td>0.187</td><td>No</td></tr><tr><td>Hypothesis 10—satisfaction</td><td>4.2500</td><td>1.6552</td><td>3.6961</td><td>1.5877</td><td>0.001</td><td>Yes</td></tr><tr><td>Hypothesis 11—confidence</td><td>4.1225</td><td>1.4793</td><td>3.9460</td><td>1.6320</td><td>0.328</td><td>No</td></tr></table>

including eight questions was developed to measure the variables of satisfaction and confidence based on the questionnaires provided in past work reported in the DSS literature [12,69]. The reliability and validity of these measures were tested using Cronbach’s alpha and factor analysis. The tests showed that the measures were reliable and valid (results are again available upon request). Summary of hypotheses testing is given in Table 6. Fig. 5 shows boxplots of MADSS vs. TDSS returns.

![](/api/attachments/GWTNAF5A/fulltext/images/3c26f8a23d4b3d455418b0be65de4f94fcc858c6d470ada2e54a9f30786373c5.jpg)  
Fig. 5. Boxplots of MADSS vs. TDSS returns.

As can be seen from the table, 8 out of 11 statistical hypotheses were confirmed at the 0.05 level. Hypothesis 4 for the variances was not confirmed. However, the hypothesized difference is larger for coefficients of variation than for variances. Hypothesis 9, dealing with improved understanding/learning, was not confirmed. The study did not show a significant difference in the level of confidence (Hypothesis 11). Confidence, however, is a controversial measure, since overconfidence might lead to user ‘‘miscalibration’’. Despite the fact that the above three hypotheses were not confirmed, the overall results are encouraging and provide support in favor of MADSS.

## 11. Summary and discussion

We proposed a new framework for building agentbased DSSs centered on human problem solving process. Its main premise was in incorporating pluralistic models in a single DSS through IAs. The work revolved around a decision support pyramid model with three categories of agents: intelligence, design, and choice. This paper primarily focused on the latter two categories of agents and proposed their design principles. The two major sources of diversity in design agents included different views and values on handling ill-structured problems. Organization of the choice agents built on the idea of critiquing systems. We proposed two types of antagonistic (positive vs. negative) critiquing agents. We also empirically tested the MADSS prototype for investment decisions based on the conceptual framework. Overall, the results of the experiments supported our expectation that a pluralistic agent-based DSS would outperform the traditional ‘‘toolbox’’-like passive DSS.

This work is the first step in the direction of employing pluralistic models for building multi-agent DSSs. Its design principles were sufficiently general to outline a framework for MADSS. This was both an advantage and a disadvantage of the proposed framework. On one hand, this made the choice of tools for building the component agents fairly flexible, but on the other hand, the work does not show what techniques (e.g. expert systems, neural nets, etc.) the designers should employ to build the agents.

One possible concern with the development of practical systems based on the our framework is the complexity associated with the need to supply multiple agents. However, recent work in decision support on demand [7], and component-based assembly of DSSs [5,36] promises to alleviate this concern by integrating pre-developed agents and other components into MADSS.

## References

[1] A. Agah, K. Tanie, Fuzzy logic controller design utilizing multiple contending agents, Fuzzy Sets and Systems 106, 1999, pp. 121–130.

[2] R.J. Aldag, D.J. Power, An empirical assessment of computer-assisted decision analysis, Decision Sciences 17 (4), 1986, pp. 572–588.

[3] A.A. Angehrn, Computers that criticize you: stimulus-based decision support systems, Interfaces 23 (3), 1993, pp. 3–16.

[4] A.A. Angehrn, S. Dutta, Case-based decision support, Communications of the ACM 41 (5), 1998, pp. 77–86.

[5] S. Ba, R. Kalakota, A. Whinston, Using client–broker–server architecture for Intranet decision support, Decision Support Systems 19, 1997, pp. 171–192.

[6] M. Bauer, D. Dengler, TrIAs: trainable information assistants for cooperative problem solving, in: Proceedings of the Third International Conference on Autonomous Agents, Seattle, Washington, 1999, pp. 260–266.

[7] H.K. Bhargava, R. Krishnan, R. Muller, Decision support on demand: emerging electronic markets for decision technologies, Decision Support Systems 19, 1997, pp. 193–214.

[8] A. Bordetsky, G. Mark, Memory-based feedback controls to support groupware coordination, Information Systems Research 11 (4), 2000, pp. 366–385.

[9] T. Bui, J. Lee, An agent-based framework for building decision support systems, Decision Support Systems 25, 1999, pp. 225–237.

[10] C. Carlsson, O. Kokkonen, P. Walden, On the improvement of strategic investment decisions and active decision support systems, in: Proceedings of the 32nd Hawaii International Conference on System Sciences, 1999.

[11] C. Carlsson, E. Turban, DSS: directions for the next decade, Decision Support Systems 33 (2), 2002, pp. 105–110.

[12] W.L. Cats-Baril, G.P. Huber, Decision support systems for ill-structured problems: an empirical study, Decision Sciences 18, 1987, pp. 350–372.

[13] E. Claver, R. Gonzales, J. Llopis, An analysis of research in information systems (1981–1997), Information and Management 37, 2000, pp. 181–195.

[14] J. Collins, C. Bilot, M. Gini, Mixed-initiative decision support in agent-based automated contracting, in: Proceedings of the Fourth International Conference on Autonomous Agents, Barcelona, Catalonia, 2000, pp. 247–254.

[15] J.F. Courtney, Decision making and knowledge management in inquiring organizations: toward a new decision-making paradigm for DSS, Decision Support Systems 31, 2001, pp. 17–38.

[16] S. Das, D. Grecu, COGENT: cognitive agent to amplify human perception and cognition, in: Proceedings of the Fourth International Conference on Autonomous Agents, Barcelona, Catalonia, 2000, pp. 443–450.

[17] J. Denzinger, Knowledge-based distributed search using teamwork, in: Proceedings of the First International Conference on Multi-agent Systems, San-Francisco, CA, 1995, pp. 81–88.

[18] E. Durfee, in: G. Weiss (Ed.), Distributed Problem Solving and Planning, MAS, 1999, pp. 121–164.

[19] E.J. Elton, M.J. Gruber, Modern Portfolio Theory and Investment Analysis, Wiley, New York, 1995.

[20] J.R. Evans, Creative Thinking in the Decision and Management Sciences, South Western Publishing Co., 1990.

[21] B. Fazlollahi, R. Vahidov, A method for generation of alternatives by decision support systems, Journal of Management Information Systems 18 (2), 2001, pp. 229–250.

[22] B. Fazlollahi, R. Vahidov, R.A. Aliev, Multi-agent distributed intelligent system based on fuzzy decision making, International Journal of Intelligent Systems 15 (9), 2000, pp. 849– 858.

[23] J. Ferber, Multi-agent Systems: An Introduction to Distributed Artificial Intelligence, Addison-Wesley, New York, 1999.

[24] G. Fischer, T. Mastaglio, A conceptual framework for knowledge-based critic systems, Decision Support Systems 7, 1991, pp. 355–378.

[25] S. Franklin, A. Graesser, Is it an Agent, or Just a Program? in: N. Jennings (Ed.), Intelligent Agents. III. Agent Theories, Architectures and Languages, Springer, Budapest, Hungary, 1996, pp. 1–20.

[26] M. Gelderman, Task difficulty, task variability and satisfaction with management support systems, Information and Management 39 (7), 2002, pp. 593–604.

[27] T.J. Hess, L.P. Rees, T.R. Rakes, Using autonomous software agents to create next generation of decision support systems, Decision Sciences 31 (1), 2000, pp. 1–31.

[28] C. Hewitt, Offices are open systems, in: A.H. Bond, L. Gasser (Eds.), Readings in Distributed Artificial Intelligence, Morgan Kaufmann, San Mateo, CA, 1988, pp. 321–329.

[29] R. Hogarth, Judgment and Choice, Wiley, New York, 1987.

[30] N. Jennings, On agent-based software engineering, Artificial Intelligence 117, 2000, pp. 277–296.

[31] N. Jennings, M. Wooldridge, Applications of intelligent agents, in: M. Wooldridge (Ed.), Agent Technology: Foundations, Applications and Markets, Springer, Berlin, 1998.

[32] G.M. Kasper, A theory of decision support system design for user calibration, Information Systems Research 7 (2), 1996, pp. 215–232.

[33] P.G.W. Keen, M.S.S. Morton, DSS: An Organizational Perspective, Addison-Wesley, Reading, MA, 1978.

[34] W.A. Kornfeld, C. Hewitt, The scientific community metaphor, IEEE Transactions on Systems, Man, and Cybernetics SMC-11 (1), 1981, pp. 24–33.

[35] T.S. Kuhn, The Structure of Scientific Revolutions, University of Chicago Press, Chicago, 1996.

[36] K.R. Lang, A.B. Whinston, A design of a DSS intermediary for electronic markets, Decision Support Systems 25 (3), 1999, pp. 193–214.

[37] F.J. Lerch, D.E. Harter, Cognitive support for real-time dynamic decision making, Information Systems Research 12 (1), 2001, pp. 63–82.

[38] M. Limayem, G. DeSanctis, Providing decisional guidance for multicriteria decision making in groups, Information Systems Research 11 (4), 2000, pp. 386–401.

[39] M.K. Malhotra, S. Sharma, S.S. Nair, Decision making using multiple models, European Journal of Operations Research 114, 1999, pp. 1–14.

[40] M. Manheim, An architecture for active DSS, in: Proceedings of the 21st Hawaiian International Conference on Systems Sciences, vol. III, 1988, pp. 356–365.

[41] S. March, A. Hevner, S. Ram, Research commentary: an agenda for information technology research in heterogeneous and distributed environments, Information Systems Research 11 (4), 2000, pp. 327–341.

[42] J. McDonald, J. Tobin, Customer empowerment in the digital economy, in: A. Lowy, D. Ticoll (Eds.), Blueprint to the Digital Economy: Creating Wealth in the Era of e-business, McGraw-Hill, New York, 1998, pp. 202–220.

[43] J. Mingers, Combining IS research methods: towards a pluralist methodology, Information Systems Research 12 (3), 2001, pp. 240–259.

[44] D. Mirchandani, R. Pakath, Four models for a decision support system, Information and Management 35, 1999, pp. 31–42.

[45] S. Murthy, R. Akkiraju, R. Goodwin, P. Keskinocak, J. Rachlin, F. Wu, J. Yeh, R. Fuhrer, S. Kumaran, A. Aggarwal, M. Sturzenbecker, R. Jayaraman, R. Daigle, Cooperative multiobjective decision support for the paper industry, Interfaces 29 (5), 1999, pp. 5–30.

[46] H.S. Nwana, D.T. Ndumu, A brief introduction to software agent technology, in: M. Wooldridge (Ed.), Agent Technology: Foundations, Applications and Markets, Springer, Berlin, 1998, pp. 29–47.

[47] R.M. O’Keefe, The evaluation of decision-aiding systems: guidelines and methods, Information and Management 17, 1989, pp. 217–226.

[48] T.A. Ottaway, J.R. Burns, Adaptive, agile approaches to organizational architecture utilizing agent technology, Decision Sciences 28 (3), 1997, pp. 483–511.

[49] S.J. Parnes, R.B. Noller, A.M. Biondi, Guide to Creative Action, Charles Scribner’s Sons, New York, 1977.

[50] S.D. Pinson, J.A. Louca, P. Moraitis, A distributed decision support system for strategic planning, Decision Support Systems 20 (1), 1997, pp. 35–51.

[51] M.J. Pring, Technical Analysis Explained: The Successful Investor’s Guide to Spotting Investment Trends and Turning Points, McGraw-Hill, New York, 1991.

[52] F.J. Radermacher, Decision support systems: scope and potential, Decision Support Systems 7, 1994, pp. 315– 328.

[53] S.A. Raghavan, JANUS: a paradigm for active decision support, Decision Support Systems 7, 1991, pp. 379–395.

[54] H.R. Rao, R. Sridhar, S. Narain, An active intelligent decision support system, Decision Support Systems 12 (1), 1994, pp. 79–91.

[55] J.C.J. Ritchie, Fundamental Analysis: A Back-to-the-Basics Investment Guide to Selecting Quality Stocks, McGraw-Hill, New York, 1996.

[56] R. Sharda, S.H. Barr, J.C. McDonnell, Decision support system effectiveness: a review and an empirical test, Management Science 34 (2), 1988, pp. 139–159.

[57] M. Shaw, M. Fox, Distributed artificial intelligence for group decision support. Integration of problem solving, coordination and learning, Decision Support Systems 9, 1993, pp. 349– 367.

[58] M. Shaw, J.D. Gardner, M.H. Thomas, Research opportunities in electronic commerce, Decision Support Systems 21, 1997, pp. 149–156.

[59] J.P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2), 2002, pp. 111–126.

[60] R. Sikora, M.J. Shaw, A multi-agent framework for the coordination and integration of information systems, Management Science 44 (11), 1997, pp. S65–S78.

[61] M. Silver, Systems that Support Decision Makers: Descrip tion and Analysis, Wiley, New York, 1991.

[62] B.G. Silverman, Critiquing Human Error: A Knowledge Based Human–Computer Collaboration Approach, Academic Press, London, 1992.

[63] H. Simon, Applying information technology to organization design, Public Administration Review 33, 1973, pp. 268–278.

[64] H.A. Simon, The New Science of Management Decision, Prentice-Hall, Englewood Cliffs, NJ, 1977.

[65] R.H.J. Sprague, E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982.

[66] C. Stabell, Towards a theory of decision support, in: P. Gray (Ed.), Decision Support and Executive Information Systems, Prentice-Hall, Englewood Cliffs, NJ, 1994, pp. 45–57.

[67] K. Sycara, A. Pannu, M. Williamson, D. Zeng, K. Decker, Distributed intelligent agents, IEEE Expert 11, 1996, pp. 36–46.

[68] T.S.H. Teo, W.Y. Choo, Assessing the impact of using the Internet for competitive intelligence, Information and Management 39 (1), 2001, pp. 67–83.

[69] G. Udo, Rethinking the effectiveness measures of decision support systems, Information and Management 22, 1992, pp. 123–135.

[70] R. Vahidov, R. Elrod, Incorporating critique and argumentation in DSS, Decision Support Systems 26 (3), 1999, pp. 249– 258.

[71] H. Wang, L. Liao, A framework of constraint-based modeling for cooperative decision systems, Knowledge-Based Systems 10, 1997, pp. 111–120.

[72] A. Whinston, Intelligent agents as a basis for decision support systems, Decision Support Systems 20 (1), 1997, pp. 1.

[73] M. Wooldridge, Reasoning About Rational Agents, MIT Press, Cambridge, MA, 2000.

[74] M. Wooldridge, N. Jennings, Intelligent agents: theory and practice, Knowledge Engineering Review 10 (2) (1995).

[75] M. Wooldridge, N. Jennings, Towards a theory of cooperative problem solving, in: J.P. Muller (Ed.), Distributed Software Agents and Applications: MAAMAW’94, Odense, Denmark, 1994, pp. 40–53.

[76] G. Woolsey, Two essays on model motivation: with this sign optimize and the Sheckels of silver solution, Interfaces 9 (1), 1978, pp. 13–17.

[77] H. Yang, C. Zhang, Definition and application of a comprehensive framework for distributed problem solving, in: Distributed Artificial Intelligence, Architecture and Modeling. First Australian Workshop on DAI, Canberra, ACT, Australia, 1995, pp. 1–16.

[78] J. Yen, Special issue of DSS—intelligent agents and digital community, Decision Support Systems 28, 2000, pp. 217– 218.

[79] C. Zhang, Cooperation under uncertainty in distributed expert systems, Artificial Intelligence 56, 1992, pp. 21–69.

[80] H. Zhuge, Workflow- and agent-based cognitive flow management for distributed team cooperation, Information and Management 40 (5), 2003, pp. 419–429.

![](/api/attachments/GWTNAF5A/fulltext/images/ca9afa0177b87e85123284fe5fd14f45c33e1028e75a4522c0e3c0098def48f4.jpg)

Rustam Vahidov is an assistant professor of Management Information Systems at the Department of Decision Sciences and MIS at John Molson School of Business, Concordia University, Montreal, Que., Canada. He earned his PhD from Georgia State University, Atlanta, GA. His research interests include decision support systems, agent technologies, genetic algorithms, fuzzy logic, neural networks, and electronic commerce. He has published in

the Journal of Management Information Systems, Journal of Decision Support Systems, Information and Management, International Journal of Intelligent Systems, Fuzzy Sets and Systems, and other journals and conference proceedings.

![](/api/attachments/GWTNAF5A/fulltext/images/518c0a9243602ac0210a2cc97101a85d6113cb98550460b61b081c94037a402a.jpg)

Bijan Fazlollahi is a professor in the Department of Computer Information Systems and Institute of International Business in the Robinson College of Business at Georgia State University, Atlanta, GA. He received his PhD in Management Information Systems from Syracuse University. His current research interests include decision support systems and application of emerging technologies for decision support. He has

published in the Journal of Management Information Systems, Journal of Decision Support Systems, Information and Management, Information Systems Research, Decision Sciences, Interfaces, Fuzzy Sets and Systems, and International Journal of Intelligent Systems. His experience includes serving as a consultant in the area of decision support systems for large public organizations. He serves in the editorial board of the Journal of Data Base Management.
