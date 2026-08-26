---
otero_id: 21749
otero_key: "E8TJRFZ2"
title: "Incorporating critique and argumentation in DSS"
authors: "Rustam Vahidov; Robert Elrod"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00031-7"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Incorporating critique and argumentation in DSS

Rustam Vahidov <sup>)</sup>, Robert Elrod

Department of Decision Sciences, College of Business Administration, Georgia State UniÕersity, 35 Broad St., Atlanta, GA 30303, USA

Accepted 12 July 1999

## Abstract

This paper proposes a framework for a decision support system DSS based on critique and argumentation. We make aŽ . distinction between positive and negative types of critique and argue that both of them are valuable in making substantiated decisions. We further propose use of debate and argumentation as means for more informative decision support. We discuss the types of knowledge used for critiquing and the appropriate form of knowledge representation. The architecture of the proposed DSS contains intelligent critiquing agents which provide the user with the qualitative feedback on candidate decisions. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Decision support systems; Critiquing systems; Argumentation; Intelligent agents

## 1. Introduction

Recently, it has been emphasized that traditional decision support systems DSS offer a weak form ofŽ . support, and an argument has been made in favor of making DSS a more active participant in decision making process 17,25,26 . Traditional DSS typically<sup>w</sup> <sup>x</sup> contain models and databases relevant to the problem; however, in order to use them effectively, users need to have full knowledge on how to use these tools and take the initiative to perform all necessary operations. In this setup, the potential power of human–computer collaboration is significantly underutilized.

Manheim 17 introduced a notion of active DSS<sup>w</sup> <sup>x</sup> and proposed an architecture for constructing such

DSS. Raghavan 25 proposed an architecture for an <sup>w</sup> <sup>x</sup> active DSS and a prototype called JANUS. One of the components of the DSS is critiquing agents. Rao et al. 26 proposed an architecture for DSS based on intelligent agents. The agents were responsible for performing specific tasks, and they cooperated to obtain a global solution. An example with air fleet control was discussed. Fazlollahi et al. 4 and Parikh<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 22 viewed adaptation as an important aspect for active DSS and introduced a framework for adaptive DSS.

The objective of this paper is to introduce a framework for an active DSS based on critique and argumentation. In this paper, we are specifically addressing the choice phase of Simon’s decision making model 33 . We argue that critique and argu-<sup>w</sup> <sup>x</sup> mentation are essential processes to support making final decisions. Our framework largely emanates from three different fields: active DSS, intelligent agents, and critiquing expert systems ES .Ž .

The field of intelligent agents has experienced an enormous growth of interest in recent years 9,21,40 .<sup>w</sup> <sup>x</sup> Although there is no agreement on the rigorous definition of an intelligent agent or a multi-agent system 9 , for our purposes, we informally describe<sup>w</sup> <sup>x</sup> an intelligent agent as a knowledge-based software component that autonomously performs specific tasks for the user. Multi-agent system contains multiple agents with possibly conflicting goals. Such systems can be used, for example, for supporting inter-related decisions by the agents 26 . A number of typical <sup>w</sup> <sup>x</sup> characteristics of an intelligent agent include: autonomy, proactiveness, purposefulness, competence, reasoning capability, and interaction with environment and other agents 9,15,16,21,40 . These fea-<sup>w</sup> <sup>x</sup> tures make intelligent agents an attractive tool for building active DSS.

There have been several attempts to combine DSS and agent technology. We already mentioned work of Rao et al. on agent-based active DSS and Raghavan’s critiquing agents. Other examples include use of agents for group decision support 27 , agent-based<sup>w</sup> <sup>x</sup> DSS for strategic planning 23 , use of utility report- <sup>w</sup> <sup>x</sup> ing agents in DSS for handling uncertainties 3 ,<sup>w</sup> <sup>x</sup> agent-based DSS with a belief revision model that takes into account the source of information 2 , and an assistant agent for exploratory data analysis 1 . <sup>w</sup> <sup>x</sup>

Critiquing ES are different from the traditional ES in that they take a proposed decision as an input in addition to the description of the situation at hand and provide a critique of the decision as an output <sup>w</sup> <sup>x</sup> 30–32 . The primary purpose of the critiquing systems is to monitor the user’s actions and indicate possible errors. Silverman 32 points out that DSS<sup>w</sup> <sup>x</sup> present an interesting opportunity for use of critique. The examples of applications of critiquing systems include medical management and medical diagnosis <sup>w x</sup> <sup>w x</sup> 10,19,20 , digital circuit design 12,34,36 , window-based interface design 7 , kitchen design <sup>w</sup> <sup>x</sup> <sup>w x</sup> <sup>w x</sup> 8 , LISP programming 6 , and requirements engineering 37 . A good survey of critiquing systems <sup>w</sup> <sup>x</sup> can be found in the work of Silverman 31 . <sup>w</sup> <sup>x</sup>

Mili 18 has proposed use of critique and advi- <sup>w</sup> <sup>x</sup> sory support in DSS. In the conceptual design of DECAD, decision critique and advisor, the system is intended to watch for subtle errors and advise the user concerning further actions. However, use of the advising facilities has been criticized for leading to user miscalibration, specifically, for promoting overconfidence of the user in the system-generated ‘‘advice’’ 11 . Fischer and Mastaglio 5 proposed a <sup>w</sup> <sup>x</sup> <sup>w x</sup> very appealing view of the interaction of the user with the critique-based DSS as a cooperative problem solving process. In this design, the user’s solution is analyzed by the critiquing system and suggestions on improvement are made iteratively, until the user is satisfied.

The research in the field of critiquing systems tends to emphasize negative critiques and underestimates the potential benefit of positive feedback to the user. Although positive critique has been considered earlier 5 , its use was very marginal. In this<sup>w</sup> <sup>x</sup> paper, we propose a framework with both negative and positive critiquing agents as components of a DSS. We further introduce use of argumentation and debate between these agents as a potential way to better inform the decision making process.

## 2. A framework for a DSS with critique and argumentation

## 2.1. Key requirements

It has been demonstrated that in the past decision support has been mainly restricted to the low cognitive level support 24 . Typical functionality of a DSS included such tasks as data storage, retrieval, and manipulation, consistency checking, small calculations, etc. 24 . Apparently, most of the support has <sup>w</sup> <sup>x</sup> been provided for the intelligence stage of the decision making process. In order to address the high level support issues, the use of artificial intelligence techniques seems to be appropriate 24 .<sup>w</sup> <sup>x</sup>

Raghavan 25 emphasizes that DSS need to offer<sup>w</sup> <sup>x</sup> advanced forms of support in which the system would be able to be an active participant of decision making. Among the features of such a DSS would be the following: monitoring decision making process and detecting inconsistencies, understanding user contexts and goals and performing required activities, criticizing decisions, forcing divergent or convergent process depending on user’s behavior 25 .<sup>w</sup> <sup>x</sup>

We have identified a number of requirements for our critique-based DSS which address the major concerns raised in the literature and those listed here relate to the functionality of DSS 4,24–26 . The<sup>w</sup> <sup>x</sup> DSS should:

<sup>Ø</sup> watch user’s actions and provide proactive feedback to the user;

<sup>Ø</sup> provide both negative and positive critique;

<sup>Ø</sup> substantiate the critique if necessary;

<sup>Ø</sup> be able to deal with violation of ‘‘soft’’ constraints;

<sup>Ø</sup> adapt critique to user’s profile; and

<sup>Ø</sup> be able to stress divergent or convergent process. Use of agents in a DSS helps to make the DSS a more active participant in decision making. The need for positive as well as negative critique comes from the intuition that human decision makers tend to assess their choices in terms of advantages and disadvantages, pros and cons.

Substantiation of the claims by the critiquing agents is achieved through the use of argumentation. The theory of argumentation provides a conceptual tool for substantiating the claims using premises Ž . data and warrants which substantiate the data 38 .<sup>w</sup> <sup>x</sup> Examples of conceptual framework for computerbased use of argumentation include use of argumentation and negotiation within organizational support system context 28 and for task allocation 29 . <sup>w x</sup> <sup>w x</sup>

Most of the negative critique has been directed to the detection of errors while often it is more appropriate to talk about drawbacks of the proposed solutions. The drawbacks are different from errors in that they are ‘‘softer’’ than the errors. Errors are usually associated with violation of crisp constraints. Fischer and Mastaglio 5 point out that the target of the<sup>w</sup> <sup>x</sup> critiquing systems should be these ‘‘soft’’ constraints. Making critique adaptive to the user’s profile is essential for providing valuable feedback. Another important aspect is stressing divergent thought processes if the user tends to be convergent and convergent thought processes if user tends to be divergent.

## 2.2. Paradigm

It is well accepted that DSS address less structured problems e.g., Ref. 35 . In such problems, Ž <sup>w</sup> <sup>x</sup>. there is no pre-specified rigorous way of arriving at solutions. DSS are designed to support some or all stages intelligence, design, and choice of decision Ž .

making while dealing with unstructured or semistructured problems. Since there is no pre-specified algorithm, a variety of possibilities are considered before determining a final diagnosis, specifying alternatives and making a final choice. In a sense, solving an ill-structured problem is very akin to the scientific research process.

Kornfeld and Hewitt 14 were first to introduce<sup>w</sup> <sup>x</sup> the scientific community metaphor in machine problem solving. They based their metaphor on the work of philosophers Popper and Lakatos who argued that diversity of opinions in scientific communities is a necessary condition for scientific progress. Although Kornfeld and Hewitt do not explicitly state what kind of problems their metaphor addresses, it is most likely that these include less structured problems.

In the scientific community metaphor, there are several roles participating in problem solving process. These roles include proposers, opponents de- Ž vil’s advocates , and proponents. These roles are. viewed as very essential for successful problem solving. The proposers suggested their solutions to the problem. In scientific communities, this would be equivalent to proposing an explanation for a phenomenon or class of phenomena. The opponents are playing the role of devil’s advocates and criticize the proposed solutions. The proponents defend, substantiate, and augment the proposed solutions.

## 2.3. Framework

We propose a similar design of roles in a DSS framework. While the role of proposers may be played by the user or other sources, the roles of proponents and opponents may be delegated to the negative and positive critiquing agents. We call these agents the ‘‘devil’’ and the ‘‘angel’’, respectively. The devil’s role is to examine the user-proposed solution with the sole intention to find possible violations, drawbacks, and potential problems. The angel’s role is quite the opposite; it is trying to identify the strengths of the proposed solution. The devil and angel are integral parts of the system, and despite the eternally ongoing conflict between them, this creative discontent enhances quality decision making. Polarization of critique is helpful because it is natural for a human decision maker to assess the alternatives in terms of their pros and cons.

In our setup, DSS provide useful qualitative feedback in addition to the numerical one. Fig. 1 shows interaction of the roles in our DSS. The proposer suggests a candidate decision. The angel and the devil examine the solution, critique it and respond to each other’s critique by proposing counter-arguments. The decision maker can request for substantiation of the agents’ claims, in which case, the agents propose their arguments to relate their critique to the current situation and the warrants. The decision maker can accept the proposed decision or reject it, in which case, the proposer will have to come up with a new alternative for the DSS to consider.

The roles of the proposer and the decision maker are typically performed by the user of a DSS. The angel and devil are software agents. The process is iterative and continues until the decision maker finds the proposed decision acceptable. In this framework, single DSS incorporates the power of a group since several intelligent entities are involved in the actual human–machine interaction.

One can think of mechanisms for controlling the intensity of critique as well as the intensity of arguments by using system parameters. We can also put more emphasis on either positive or negative critique. If we emphasize negative critique by diminishing or completely eliminating positive feedback, this will stress pessimistic bias in decision maker, thus, forcing the proposer to search for more alternatives. Therefore, the negative critique would tend to stress divergent behavior. On the other hand, if we diminish negative critique, the positive feedback would introduce an opposite optimistic kind of bias inŽ . decision makers, making them more lenient in accepting the proposed decisions. Hence, the positive critique is likely to stress convergent behavior. We can, therefore, manipulate the intensity of one or the other type of critique to counteract the user’s natural bias on the divergence–convergence scale.

![](/api/attachments/E8TJRFZ2/fulltext/images/372311870a7d966dd77af4b68c92f3e673d05626af7cd03918b5514a1f55474f.jpg)  
Fig. 1. Interaction of roles in a critiquing DSS.

## 3. Organization of critique

Silverman 30–32 illustrates that a typical archi- <sup>w</sup> <sup>x</sup> tecture for an expert critiquing system includes the difference analyzer, file of errors, and dialogue generator. The system uses the difference analyzer to examine the user-defined solution and detect the significant deviations from the system’s internally generated solution. That difference is then sent to the file of errors, and a corresponding critique message is generated by the dialogue generator. The critique message often contains a canned text.

The difference analyzer can work only if the system has some kind of idea of what the solution may look like. In ill-structured problems, this is rarely the case. Nevertheless, it is often easier to critique solutions than propose good solutions 18 . <sup>w</sup> <sup>x</sup> Often, it is not only the solution per se which is scrutinized but its properties.

We distinguish the following types of the critiquing knowledge in our design for DSS:

<sup>Ø</sup> objective-related critique;

<sup>Ø</sup> preference-related critique;

<sup>Ø</sup> soft constraints-related critique; and

<sup>Ø</sup> reactive critique.

The objective-related critique knowledge addresses the issues related to how well or how poorly the proposed decision promises to achieve the key objectives of the user. For example, the key objective could be maximizing the expected profit of a business organization. We denote this knowledge by the symbol O.

Preference-related critique knowledge reflects the user preferences in critique. The user here could be an individual making personal decisions, or a representative of some organization. The distinction between the objectives and preferences is somewhat fuzzy. Example of preferences could be company’s policy regarding different aspects of their business. In such case, the critique would try to find out whether the proposed solution does or does not fit the company’s general policy. We denote this knowledge symbolically by P.

Soft constraints are different from the hard constraints in that the violation of soft constraints can be tolerated to some degree. For example, the soft constraint for a business firm could be to avoid large inventory build-ups. But how large is large is not clear, and there is no clear-cut inventory amount that should not be exceeded. Use of fuzzy sets would probably be most appropriate to deal with these constraints. The critique here is aimed at telling the user to what degree the soft constraints are violated. We denote this knowledge by S.

The above types of knowledge can be described in the following fashion:

$$
\mathrm{K} (\mathrm{p} (\mathrm{s}); \mathrm{p} (\mathrm{u})) \rightarrow \mathrm{c} (\mathrm{s}) \quad \mathrm{K} \in \{\mathrm{O}, \mathrm{P}, \mathrm{S} \}
$$

Here, s is solution, u is the user, p stands for property, and c is critique.

In reactive critique knowledge, an agent considers the opponent’s critique in addition to the properties of the solution and those of the user to build a counter-argument. This critique mostly addresses the relationships between different, possibly conflicting objectives and preferences. Both critique and counter-argument may be useful to the decision maker to better assess the proposed solution. The reactive knowledge is denoted here by R, and is described as follows:

$$
\mathrm{R} (\mathrm{p} (\mathrm{s}); \mathrm{p} (\mathrm{u}); \mathrm{c} (\mathrm{s})) \rightarrow \mathrm{c} (\mathrm{s})
$$

The total knowledge of the system can be then described as:

$$
\mathrm{O} \cup \mathrm{P} \cup \mathrm{S} \cup \mathrm{R}
$$

This knowledge is distributed between the positive and negative critiquing agents angel and devil .Ž .

## 4. Knowledge representation

We propose use of combination of rules and frames as a knowledge representation scheme appropriate for the critique. This approach allows us to combine the inferencing capabilities of the rule-based representation with the expressive power of the frame-based representation 39 .<sup>w</sup> <sup>x</sup>

Each instance of critique is represented by a frame consisting of slots and demons Fig. 2 . The Ž . list of slots and attached demons includes the following.

<sup>Ø</sup> Criterion. This slot contains the name of the criterion to which the critique relates. For example, if the name of the variable is ‘‘Risk’’, then the critique relates to the riskiness of the proposed decision.

![](/api/attachments/E8TJRFZ2/fulltext/images/b7d152937ca1e962265bcf5dda67f9e46e8b1ef5b20b16e93b23722ba330c692.jpg)  
Fig. 2. An example critique frame.

<sup>Ø</sup> Condition. Holds the logical expression that represents the conditional part of the rules for critique. For example, ‘‘standard deviation of portfolio <sup>s</sup>high and user risk profile<sup>s</sup>risk averse’’.

<sup>Ø</sup> Variables. Stores the names of variables used in the condition.

<sup>Ø</sup> Data. Stores the list of actual values for the variables used in the conditional part of the rules. Demon Ž . ‘‘if-added’’ : matches the actual values of data with the condition and writes the calculated support value into the slot ‘‘support’’.

<sup>Ø</sup> Support. Indicates to what degree the condition is supported by the data. Ranges from 0 to 1. Demon Ž . ‘‘if-added’’ : compares the added<sup>r</sup>modified value of support with the threshold value and sets the value of ‘‘activation’’ slot to one if the support exceeds the threshold.

<sup>Ø</sup> Threshold. Keeps the threshold value. If support exceeds this value the critique becomes active.

<sup>Ø</sup> ActiÕation. Indicates whether critique is active Ž . Ž . Ž . ‘‘1’’ or not ‘‘0’’ . Demon ‘‘if-added’’ : If the activation level is set to one the text of critique theŽ contents of the slot ‘‘critique’’ is displayed to the. user.

<sup>Ø</sup> Critique. Holds the text of the critique theŽ claim . This is the conclusion part of the critiquing . rules.

<sup>Ø</sup> Warrant: Stores the warrant used in argumentation. For example, ‘‘High risk portfolios are not appropriate for risk averse people’’.

The antecedent part of the critiquing rules is stored in the slot ‘‘condition’’. We advocate use of fuzzy logic 13,41 in construction of rules since: the<sup>w</sup> <sup>x</sup> kind of critique discussed here mostly deals with soft types of advantages and disadvantages as opposed to the type of critique that deals with crisp errors, and, therefore, it may be naturally specified in fuzzy terms; and fuzzy rules provide the means to determine the degree of strength, or the degree of support of the resulting critique on a continuous scale from 0 to 1 as opposed to the traditional bi-valued logic, thus, allowing to estimate the strength of the critique.

The warrant is presented to the user as a part of argument only when the user requests for the substantiation of the claim critique by an agent. Sillince Ž . <sup>w</sup> <sup>x</sup> 28 points out that warrant is the actual rule used in argumentation. Despite the semantic identity of the textual expression of the warrant and the corresponding operational rule in an agent’s knowledge base, we still distinguish the two since the former is more readable as a natural language construct , and, hence, Ž . presentable for the user than the structured rule that operationalizes the warrant.

We can set a threshold value to control the intensity of critique. For example, if the threshold value was set to 0.5, then, the critique with lower support would not be presented to the decision maker and the opponent agent. Only critique strong enough to exceed the threshold value would become active. If the thresholds for both positive and negative critique are equal, then, the system has neutral bias. Increasing threshold for one type of critique and decreasing for the other one introduces either positive or negative bias, thus, making DSS devil- or agent-dominated. The larger the value for the threshold, the less charged debates are and vice versa. The threshold can be that valuable lever to manipulate the divergent<sup>r</sup>convergent behavior in the decision maker.

The intensity of critique can also be manipulated for different kinds of critique. For example, manipulating the intensity of reactive critique would increase or decrease amount of debate. We can, therefore, stress more complex behavior of the system. Fig. 3 shows a map with two dimensions: positive vs. negative critique, and reactive vs. non-reactive critique. A system can be manipulated in such manner as to position the DSS along the axes or in one of the quadrants. If the system is positioned in the origin, it would be neutral. Placing the system in one of the quadrants would bring about one of the four behaviors: optimistic debater, optimistic abstainer, pessimistic abstainer, and pessimistic debater. This flexibility can be effectively used to suit the style and preferences of the user.

![](/api/attachments/E8TJRFZ2/fulltext/images/de4dae232620b1a45d7c61bba06202bad8c5152358e0a093e71cc39dd2cb339b.jpg)  
Fig. 3. A map of critiquing DSS’ profile.

The mechanism of generating critique at the frame level proceeds as follows. When the new data is recorded into the ‘‘data’’ slot the corresponding demon matches it with the conditional construct to generate the degree of support, i.e., the degree to which the condition is true. This support is recorded into the corresponding slot. The ‘‘support’’ slot’s demon compares the just added value with that of threshold, and if the former exceeds the latter, then, sets the activation bit to unity, or does nothing otherwise. When the ‘‘activation’’ slot is on, its demon sends the contents of the slot ‘‘critique’’ out to be displayed to the user. Warrant is retrieved by the request of the user only. Use of the warrant is much similar to the use of the explanation facilities in the context of the traditional ES. The important difference is, though, that in traditional ES explanations are provided usually for the single final conclusion, while here, warrants are used to justify normally multiple critiquing claims.

## 5. Architecture of the DSS

Fig. 4 shows the architecture of the critiquing DSS. The DSS includes three major components: data and models, communications, and critiquing agents. Data and models are the traditional components of DSS that can be used by the user and other agents to retrieve relevant information and perform quantitative analysis of the trial decisions.

The critiquing agents are knowledge-based entities capable of reasoning. The structure of the critiquing agent includes the knowledge base and the monitor. The knowledge base contains critique organized as frames as discussed earlier. The monitor updates the values of variables listed in the different frames through interaction with data, models, and the blackboard and processes the requests for the argumentation by retrieving the warrant and the data to accompany the claim. The negative critique agent Ž . ‘‘devil’’ receives the trial solution from the user and tries to critique it. It also communicates with the user profile agent if it finds that communication necessary for the inference. The ‘‘devil’’ also listens to the messages from its counterpart, the ‘‘angel’’, and tries to respond to the positive critique. The ‘‘devil’’ has rules in its knowledge base that anticipate possible positive messages and presents counter arguments.

The positive critique agent ‘‘angel’’ also takesŽ . the user-defined solution and the user properties to highlight the advantages of the proposed solution. As its counterpart, it is listening to the ‘‘devil’s’’ messages, recognizing them and tying to come up with the counter-argument. The knowledge bases of the critiquing agents should be constructed in such a way so to avoid possible deadlocks where the agents keep repeating the same arguments to each other.

![](/api/attachments/E8TJRFZ2/fulltext/images/fa6cb323d17904f775aabaa2c065d2786302593707ff6cceb42117ba324d1408.jpg)  
Fig. 4. Architecture of the critiquing DSS.

The communications block manages interactions between the agents and the user. The blackboard stores the trial decisions, critique, and counter-critique and serves as a vehicle of sharing this information between the agents and the user. The dialogue organizer organizes the critique in a readable format for presentation to the user, and presents arguments upon the user’s request.

The proposed DSS works as follows. The user starts entering decisions, doing ‘‘what-if’’ analysis using data from the database, and models. The critiquing agents take the user-specified trial decision from the blackboard and examine it to identify advantages and disadvantages. Their critique is written to the blackboard and the agents start examining their counter-parts critique to produce reaction. The process halts when no new changes are made to the blackboard. The dialogue organizer then organizes and displays the result of the critique and debate to the user in a presentable way. If the user requests for substantiation of certain claims, the dialogue organizer sends that request to the appropriate agent to elicit the related argument. The user receives the feedback and uses his<sup>r</sup>her judgement to either accept the decision or explore other possibilities. If the user finds the solution acceptable, the system finishes its work.

The proposed architecture and working principles for the critique-based DSS fit well in the paradigm of collaboration between a human and a computer. Indeed, the agents can be viewed as experts in the field whom the decision maker consults before making the final choice. Their qualitative feedback is a valuable addition to the quantitative analysis done with the help of models. Such a setup would improve significantly the performance of human decision makers.

## 6. Example of critique

This section illustrates critique using the simplified example of investment decisions 4 . In this<sup>w</sup> <sup>x</sup> investment problem, the decision maker is trying to allocate the available funds to the portfolio of securities in order to achieve his<sup>r</sup>her financial objectives.

In our example, we consider wide classes of different securities, i.e., T-bills, bonds, and stocks. There are a number of important factors that need to be taken into consideration while making investment decisions. These factors include: expected return and risk, liquidity of assets, and others. Historical information and expert opinions can be used to evaluate the above factors.

Fig. 5 shows an example portfolio and the corresponding critique from both ‘‘devil’’ and ‘‘angel’’. The critique is organized by the important criteria including risk, return, and liquidity. More criteria can be included in the real full-scale system. Generally, one seeks to increase the expected return, diminish risk, and improve increase liquidity. The Ž . decision maker also has a set of preferences e.g.,Ž risk aversion , and constraints e.g., financial posi- . Ž tion and stability ..

Within each criterion the order of critique is O, P, S, R objective-related, preference-related, soft-con-Ž straint-related, and reactive . Consider, for example,.

the critique by the agents regarding the portfolio risk. Given the user-specified allocation the numeric characteristics e.g., expected risk and return are calcu-Ž . lated. The negative critique disadvantage includes aŽ . claim objective-related that the user-specified port-Ž . folio implies high risk 21.3% . The positive sideŽ . notes that the risk corresponds to the user’s risk preference preference-related . The ‘‘devil’’ thenŽ . notes that the user has little capability to tolerate such risk soft constraint-related , and the ‘‘angel’’Ž . notes that the risk is necessary to achieve high expected return reactive . The lists of pros and consŽ . provides the user with insightful implications of the candidate decisions in the soft verbal format. The buttons with the question marks can be used for substantiation request, in which case an argument in favor of the corresponding claim will be provided. For example, the argument in favor of the aforementioned reactive critique would be: ‘‘Since critique is ‘This is a high-risk portfolio’, and portfolio return is high data and generally high return requires taking Ž .

![](/api/attachments/E8TJRFZ2/fulltext/images/2443b798b45f60e71982d57cc9afd7f0e818dfa070a3d7ca46cf9c53e34d4835.jpg)  
Fig. 5. Example of critique.

higher risk warrant , this risk is necessary to provide Ž . high return claim .’’Ž .

In summary, the critiquing agents act here as financial consultants which are allowed to communicate and react to each other’s opinion. The user receives qualitative as well as quantitative feedback from the DSS which can improve the quality of the user’s decisions and promote his<sup>r</sup>her understanding of the problem of investment.

## 7. Conclusions

We have introduced a conceptual framework for a DSS based on critique and argumentation. We emphasized that both negative and positive critique are valuable for the decision making process. We introduced a notion of debate and argumentation in DSS as a valuable activity in assessing candidate decisions. The architecture of the proposed DSS includes critiquing agents which collaborate with the user in making effective decisions. We discussed the types of knowledge used by the critiquing agents and the appropriate representation scheme for this knowledge.

Future research efforts can be directed at empirical testing of the effectiveness of DSS based on our framework for different application areas. Also, an interesting research question would be how to adapt the critique strategies to the cognitive style of the user. We discussed one possible way in which critique could be manipulated so that to adapt to the user’s divergent<sup>r</sup>convergent behavior. Exploring this dimension would be an interesting direction for the future research efforts.

## References

<sup>w</sup> <sup>x</sup> 1 R.St. Amant, P.R. Cohen, Evaluation of semi-autonomous assistant for exploratory data analysis, Proceedings of the First International Conference on Autonomous Agents, Marina del Rey, CA, USA, February 5–8, 1997, pp. 355–362.

<sup>w</sup> <sup>x</sup> 2 A.F. Dragoni, Distributed decision support system under limited degrees of competence: a simulation study, Decision Support Systems 20 1 1997 17–34.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 L. Ekenberg, M. Danielson, B. Magnus, Imposing security constraints on agent-based decision support, Decision Support Systems 20 1 1997 3–15.Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 B. Fazlollahi, M. Parikh, S. Verma, Adaptive decision sup-

port systems, Decision Support Systems 20 4 1997 295– Ž . Ž . 317.

<sup>w</sup> <sup>x</sup> 5 G. Fischer, Th. Mastaglio, A conceptual framework for knowledge-based critic systems, Decision Support Systems 7 Ž . 1991 355–378.

<sup>w</sup> <sup>x</sup> 6 G. Fischer, A critic for LISP, in: Proceedings of the 10th International Joint Conference on Artificial Intelligence, Milan, Italy, 1987, pp. 177–184.

<sup>w</sup> <sup>x</sup> 7 G. Fischer, A.C. Lemke, Knowledge-based design environments for user interface design, Technical Report, Department of Computer Science, University of Colorado, Boulder, CO, 1989.

<sup>w</sup> <sup>x</sup> 8 G. Fischer, A. Morch, CRACK: a critiquing approach to cooperative kitchen design, in: Proceedings of the International Conference on Intelligent Tutoring Systems, Montreal, Canada, 1998, pp. 176–185.

<sup>w</sup> <sup>x</sup> 9 S. Franklin, A. Graesser, Is it an agent, or just a program?: a taxonomy for autonomous agents, in: J.P. Muller, M.J. Wooldridge, N.R. Jennings Eds. , Intelligent Agents III:Ž . Agent Theories, Architectures, and Languages, Springer-Verlag, Berlin, 1997, pp. 21–36.

<sup>w</sup> <sup>x</sup> 10 A.S. Gertner, Plan recognition and evaluation for on-line critiquing, User Modelling and User-Adapted Interaction 7 Ž . Ž .2 1997 107–140.

<sup>w</sup> <sup>x</sup> 11 G.M. Kasper, A theory of decision support system design for user calibration, Information Systems Research 7 2 1996Ž . Ž . 215–232.

<sup>w</sup> <sup>x</sup> 12 V.E. Kelly, The CRITTER system: automated critiquing of digital circuit designs, in: Proceedings of the 21st Design Automation Conference, ACM<sup>r</sup>IEEE, 1984, pp. 419–425.

<sup>w</sup> <sup>x</sup> 13 G.J. Klir, B. Yuan, Fuzzy Sets and Fuzzy Logic: Theory and Applications, Prentice Hall, 1995.

<sup>w</sup> <sup>x</sup> 14 W.A. Kornfeld, C. Hewitt, The scientific community metaphor, IEEE Transactions on Systems, Man, and Cybernetics SMC 11 1 1981 24–33.Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 M. Luck, N. Griffiths, M. D’Inverno, From Agent Theory to Agent Construction: A Case Study. Intelligent Agents III: Agent Theories, Architectures, and Languages, Springer-Verlag, Berlin, 1997, pp. 49–64.

<sup>w</sup> <sup>x</sup> 16 P. Maes, Modeling adaptive autonomous agents, in: C.G. Langton Ed. , Artificial Life: An Overview, The MIT Press,Ž . Cambridge, MA, 1995, pp. 135–162.

<sup>w</sup> <sup>x</sup> 17 M.L. Manheim, An architecture for active DSS, Proceedings of the 21 Hawaiian International Conference on System Sciences, IEEE Computer Society, 1988, pp. 356–365.

<sup>w</sup> <sup>x</sup>18 F. Mili, A framework for a decision critic and advisor, in: Proceedings of 21st Hawaii Conference on System Sciences, Vol. 3, 1988, pp. 381–386.

<sup>w</sup> <sup>x</sup> 19 P. Miller, ATTENDING: critiquing a physician’s management plan, IEEE Transactions on PAMI, PAMI-5, September, 1983, pp. 449–461.

<sup>w</sup> <sup>x</sup> 20 P. Miller, Expert Critiquing Systems: Practice-Based Medical Consultation By Computer, Springer-Verlag, 1986.

<sup>w</sup> <sup>x</sup> 21 H.S. Nwana, D.T. Ndumu, An introduction to agent technology, in: H.S. Nwana, N. Azarmi Eds. , Software Agents and Ž . Soft Computing, Springer-Verlag, Berlin, 1997, pp. 3–26.

<sup>w</sup> <sup>x</sup> 22 M. Parikh, Adaptive decision support systems: a framework

for making decision support systems more effective, PhD Thesis, Department of Decision Sciences, Georgia State University, Atlanta, GA, 1998.

<sup>w</sup> <sup>x</sup> 23 S.D. Pinson, J.A. Louca, P. Moraitis, A distributed decision support system for strategic planning, Decision Support Systems 201 1997 35–51.Ž .

<sup>w</sup> <sup>x</sup> 24 F.J. Radermacher, Decision support systems: scope and potential, Decision Support Systems 7 1994 315–328.Ž .

<sup>w</sup> <sup>x</sup> 25 S.A. Raghavan, JANUS: a paradigm for active decision support, Decision Support Systems 7 1991 379–395.Ž .

<sup>w</sup> <sup>x</sup> 26 H. Rao, S.R. Raghav, S. Narain, An active intelligent decision support system — architecture and simulation, Decision Support Systems 12 1 1994 79–91.Ž . Ž .

<sup>w</sup> <sup>x</sup> 27 M. Shaw, M. Fox, Distributed artificial intelligence for group decision support. Integration of problem solving, coordination and learning, Decision Support Systems 9 1993 349–Ž . 367.

<sup>w</sup> <sup>x</sup> 28 J.A.A. Sillince, Argumentation and contract models for strategic organization support systems, Decision Support Systems 16 31 1996 325–326.Ž . Ž .

<sup>w</sup> <sup>x</sup>29 J.A.A. Sillince, Extending electronic coordination mechanisms using argumentation: the case of task allocation, Knowledge-Based Systems 10 1998 325–326.Ž .

<sup>w</sup> <sup>x</sup> 30 B.G. Silverman, Evaluating and refining expert critiquing systems: a methodology, Decision Sciences 23 1 1992 Ž . Ž . 86–110.

<sup>w</sup> <sup>x</sup> 31 B.G. Silverman, Survey of expert critiquing systems: practical and theoretical frontiers, Communications of the ACM 35 Ž . Ž .4 1992 106–127.

<sup>w</sup> <sup>x</sup> 32 B.G. Silverman, Critiquing Human Error: A Knowledge-Based Human–Computer Collaboration Approach, Academic Press, London, 1992.

<sup>w</sup> <sup>x</sup> 33 H.A. Simon, The New Science of Decision Making, Harper and Row, New York, 1960.

<sup>w</sup> <sup>x</sup> 34 R.L. Spickelmier, A.R. Newton, Critic: a knowledge-based program for critiquing circuit designs, in: Proceedings of 1988 IEEE International Conference on Computer Design, VLSI in Computers and Processors, 1988, pp. 324–327.

<sup>w</sup> <sup>x</sup> 35 R.H. Sprague, A framework for the development of decision support systems, MIS Quarterly 4 4 1980 1–26. Ž . Ž .

<sup>w</sup> <sup>x</sup> 36 R. Steele, Cell-based VLSI design advice using default reasoning, in: Proceedings of 3rd Annual Rocky Mountain Conference on Artificial Intelligence, Denver, 1988, pp. 66– 74.

<sup>w</sup> <sup>x</sup> 37 A. Sutcliffe, The domain theory for requirements engineering, IEEE Transactions on Software Engineering 24 3Ž . Ž .1998 175–190.

<sup>w</sup> <sup>x</sup> 38 S. Toulmin, The Uses of Argument, Cambridge Univ. Press, 1958.

<sup>w</sup> <sup>x</sup> 39 E. Turban, Expert Systems and Applied Artificial Intelligence, Macmillan, 1992.

<sup>w</sup> <sup>x</sup> 40 M. Wooldridge, N. Jennings, Intelligent agents: theory and practice, Knowledge Engineering Review 10 2 1995 115–Ž . Ž . 152.

<sup>w</sup> <sup>x</sup> 41 L.A. Zadeh, Fuzzy logic, IEEE Computer, April 1988Ž . 83–93.

![](/api/attachments/E8TJRFZ2/fulltext/images/e83b58227c0b9788881fc38e3b395cb249e6d5d1b613cd0d52c7800d87af9a3e.jpg)

Rustam Vahidov is a doctoral candidate at the Department of Decision Sciences at Georgia State University. His research is in the areas of intelligent agents, soft computing, and decision support systems. His papers have been published in various proceedings, including European Congress on Intelligent Techniques and Soft Computing, World Congress on Neural Networks and others.Robert Elrod is an Associate Professor of Decision Sciences at Geor-

gia State University, Atlanta, GA. Dr. Elrod received his PhD and MSc from Clemson University, and BS from Presbyterian College. His research is in the area of problem solving, cognition, and use of decision support systems as they relate to the individua problem-solving style.
