---
otero_id: 21471
otero_key: "SNHYZBVB"
title: "Strategic decision-making processes: network-based representation and stochastic simulation"
authors: "V. Srinivas; B. Shekar"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00023-7"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Strategic decision-making processes: network-based representation and stochastic simulation

V. Srinivas, B. Shekar \*

Quantitative Methods and Information Systems Area, Indian Institute of Management Bangalore, Bangalore 560 076, India

## Abstract

Representation of decision-making in organizations is an intricate process. Qualitative Probabilistic Network (QPN)-based approach offers a scheme which is useful for representing processes involved in decision-making. This paper demonstrates the usefulness of QPN-based scheme with an illustrative case study. The focus of the case study is on understanding the strategic behavior of a key player in the Indian Automobile Industry. This is done by transforming Cognitive Maps developed into QPN-based formalisms and analyzing them. In addition to this, stochastic simulation experiment is performed on the QPN-based networks to generate hypothetical scenarios. © 1997 Elsevier Science B.V.

Keywords: Qualitative probabilistic networks; Stochastic simulation; Cognitive maps; Strategic thinking; Decision-making process; Network-based representation

## 1. Introduction

Most businesses are facing challenging situations with respect to the changes in their environment (both internal and external to the organization). This is because the environment has become more complex and uncertain. In these kinds of situations, predicting changes is a challenging task for the top management of any organization. Researchers attributed the behavior of managers in making decisions in these dynamic situations to the cognitive process of noticing changes in the environment. Current studies have linked changes in cognitive models of top management to organizational action, by studying causal assertions made by the managers of the firms $[1,2]$ . Representation of organizational change is one of the critical issues for researchers.

Managers rely on simplified representations of the real world [2]. These representations, called ‘cognitive maps’ or ‘mental models’, consist of concepts and relationships that are needed to understand various situations or environments [3]. These representations have helped researchers map managerial perceptions of environment on a larger scale. Cognitive maps have the characteristic of perceiving the environment as a set of cause-effect relationships. Barr et al. [1] point out that, causal maps underscore the critical link between managers’ understanding of environmental conditions and the strategy the firm adopts. In other words, the process attributing cause-effect precedes the process of decision making. Subsequently, these strategic decisions determine the overall direction of the organization.

Transformation of strategic decisions to actions can be captured effectively by developing cognitive maps for a firm (that span a number of years).

Diagnostic systems have been used by researchers to enumerate various possible causes for an observed event. Most of these diagnostic systems used causal representations. From the studies done on these support systems, it is found that decisions taken by managers are categorized as 'structured' and 'unstructured'. Managers, (or in general individuals), resort to unstructured decision making when they have to make decisions in uncertain environment. Qualitative analysis (in the form of cause-effect assertions) is a useful tool to capture this kind of unstructured process also. This type of qualitative analysis is implemented in support systems that help managers in diagnosis. Thus under uncertainty, it is found that individuals resort to qualitative analysis to perceive changes in environment.

In this paper we look at issues pertaining to strategic decision making in organizations. Here we see by mapping the causal thinking of managers one can understand the strategic behavior of firms. Subsequently we look at different aspects of network-based representation techniques to capture the causal thinking in managers. Here, we focus on issues pertaining to representation of organizational change using a simple graph (a Cognitive Map) that is used by researchers to understand firm behavior. However, this representation technique has certain shortcomings. Cognitive maps do not provide facilities to represent uncertainty. A formalism to represent uncertainty is provided by Qualitative Probabilistic Networks $[4,5]$ . Also there are methods to generate scenarios of a causal model represented as QPN $[6]$ .

The main contribution of this paper is to understand firm behavior with the help of cognitive maps for a firm taken from the Indian Automobile Industry. This is done by converting cognitive maps to QPNs and simulation of QPN by generating different hypothetical scenarios. We conclude by showing that stochastic simulation and such representations lead to a better understanding of organizations.

## 2. Causal representations of decision-making process in organizations

Human decision making in complex environments is not a well understood process $[7–9]$ . Simon has classified decisions into two classes: decisions that are repetitive and can be represented as algorithms, i.e. programmable procedures (structured decision making [10]); and decisions that require human judgment, i.e. those decisions that cannot be represented as clearly defined algorithms (unstructured decision making [10]). Most often in reality, individuals making decisions face a less-than-ideal environment. An important characteristic of the real world environment is imperfection in information [11]. Simon also proposed that, individuals when faced with situations where they have to execute unstructured decision, try to break the decisions into familiar structurable elements. Furthermore, they try to 'satisfice' instead of maximizing while reasoning in these situations. Under these circumstances where there is an unstructured decision processing environment, as Simon proposed in his theory, human reasoning process tends to be increasingly more heuristic [9].

Here in this study (adopting from [12]), a decision is defined as a specific commitment to action, and a decision process as a set of actions and dynamic factors which begin with the identification of a stimulus for action and ends with the specific commitment to action.

In a typical managerial decision making situation, more specifically in those related to strategic management issues, decision makers receive ambiguous data continuously. Most often the decision problems are to be represented in terms of the global problem domain, i.e. involving the whole organization $[13,14]$ . There are a number of models that describe managerial decision making processes $[15,12]$ . These models hypothesize about cause–effect relationships among variables that correspond to the structure of the problem at hand. In the same spirit, strategy process and strategy content researchers are interested in these kinds of causal relations $[16]$ . The causal linkages between strategy of a firm and firm-performance has been the central theme in most of the research work so far. Analyses of causal linkages have helped researchers to understand ‘strategic change’ $[1,17,2]$ . It has also helped in attributing causes to performance in organizations $[18,19]$ . The causal inferencing model of Einhorn and Hogarth $[20]$ suggests a method of utilizing cues for generating causal hypothesis. Cues include temporal order, contiguity amongst the variables in time and space and similarity of cause and effect. These causal cues are used in diagnostic systems which are used in understanding strategic issues [14]. Billman and Courtney [21] developed a system by which one can automate discovery of causal hypothesis for managerial problem formulation. They have extended the causal cues model of Einhorn and Hogarth [20] to develop causal hypothesis. Their system perceives the behavior of variables in an environment through probabilistic cues-to-causality, and generates previously unknown hypothesis by aggregating the probabilities into a single criterion of causal relatedness.

Typically, a diagnostic problem starts with the observation of a certain behavior which is recognized as a deviation from the expected or desirable performance [22]. Dutton et al., [14] have developed a framework to conceptualize diagnosis in strategic management. This framework has three modules: input, process and output. Input consists of the problem structure in the form of cognitive maps (discussed in later sections) and details of the strategic issues; the Process module captures the conceptual and empirical treatments of diagnosis; Output module gives the possible outputs after the process as a set of assumptions or cause-effect assertions or predictive judgments, like for example, whether the drop in sales volume is caused by the misdirected promotional strategy or poor product performance or because of change in consumer perceptions. Courtney et al. [23], have used a knowledge-based approach for problem diagnosis. These systems developed so far are not built on well formed formalisms. Billman and Courtney [21] have used a heuristic measure to establish the strength of causality. Courtney et al. [23] have used a heuristic to select a causal link from the knowledge base. A technique that is used to capture causal links is the network-based representation. We discuss the technique and related variations in Section 3. The variations are based on whether there is any provision for representation for uncertainty or not.

## 3. Network-based representation for qualitative analysis

Studies in managerial decision making reveal that managers are more likely to resort to qualitative reasoning, when they are in ill-structured decision situations. Similarly when diagnosticians are faced with largely quantitative data, they resort to qualitative reasoning [1]. These qualitative assertions are represented as directed graphs. These qualitative assertions are represented as directed graphs that may be classified as: Deterministic representation and Non-deterministic representation schemes. Non-deterministic representation has various forms, viz. Bayesian Probabilistic Networks, Belief Networks [24,6], Influence Diagrams [25,26], and Qualitative Probabilistic Networks [4]. The deterministic networks that are discussed here are the Cognitive Maps [3], which are, in essence, graphs.

## 3.1. Non-deterministic network representation

In the non-deterministic mode of representation like a Bayesian Network, the directed arcs between two variables capture the conditional probabilistic dependency. However, in some networks which are based on Dempster–Shafer theory [27], the non-deterministic guidelines follow a different set of mathematics, unlike a Bayesian approach. Thus essentially, the non-deterministic type of reasoning can be classified into Bayesian Networks and Non-Bayesian Networks [6]. In this paper we look only at Bayesian Networks and highlight their strong points.

## 3.1.1. Bayesian Networks: an overview

The two related graph-based formalisms that have been advocated for computer representation of probabilistic knowledge are Pearl's Belief Networks [24] and the influence diagrams of Shachater [25,26]. A modification of influence diagrams and Belief Networks are the Qualitative Probabilistic Networks [4]. Graph representations are computationally attractive and have conceptual advantages in their focus on dependencies among the probabilistic variables. Both these representations encode probabilistic models as directed graphs, with the nodes representing uncertain variables and the links denoting probabilistic dependence. Within each node is a table recording the distribution of the node's values given each combination of values for its direct predecessor nodes. Different distributions of interest under various scenarios or decisions may be computed through propagation or graph reduction techniques. Influence diagrams also include specially designated decision nodes and informational links to indicate which chance variables are known at the time decisions are made. A special class of nodes indicate the utility of outcomes represented in the network. In Section 3.1.1.1 we look at Bayesian Belief Networks and Qualitative Probabilistic Networks. Influence Diagrams are detailed elsewhere [25,26].

3.1.1.1. Bayesian Belief Networks. In Bayesian Belief Networks, the nodes of the network follow the probability calculus of Bayesian conditionalization. Bayesian methods provide a formalism for reasoning about partial beliefs under conditions of uncertainty. They are also called as Causal Probabilistic Networks [28], Bayesian Belief Networks [24], Probabilistic Influence Diagrams [25,26]. We refer to a Bayesian Belief Network simply as a belief network. A key advantage of belief networks is that they represent probabilistic relationships concisely. A belief network consists of a graphical structure that is augmented by a set of probabilities. The graphical structure is a directed, acyclic graph in which nodes represent domain variables. Prior probabilities are assigned to source nodes, and conditional probabilities are associated with arcs. In particular, for each source node $x_{i}$ (i.e. nodes without any in coming arcs), there is a prior probability function $P(x_{i})$ , which is the marginal probability of node $x_{i}$ . For each node $x_{j}$ with one or more direct predecessors, $S_{j}$ , there is a conditional probability function $P(x_{i}|S_{j})$ . A general belief network can be represented as $(V, A, P)$ , where $V$ is the set of variables (i.e. vertices or nodes), $A$ is the set of arcs between variables and $P$ the set of probabilities. Belief networks are capable of representing the probabilities over any discrete sample space, such that the probability of any sample point in that space can be computed using the network. The key feature of belief networks is their explicit representation of the conditional independence among the nodes (nodes). The assumption here is that in these networks all relevant 'causal factors' and 'influences' have been faithfully captured by the arcs [29]. Consider a network given in Fig. 1. Since it has no predecessors, node $a$ is quantified with the marginal probability, $P(a)$ . The probability of the remaining nodes can be determined by $P(a)$ and conditionals $P(b|a)$ ,

![](/api/attachments/SNHYZBVB/fulltext/images/38695bf2e76814d11a7b2e99b9df7a85b78553dbed94dcb29ec9a4d3232d6c39.jpg)

$P(c|a)$ , $P(d|b, c)$ and $P(e|d)$ . The joint distribution can be factored as:

$$
\mathrm{P} (a, b, c, d, e)
$$

$$
= \mathrm{P} (a) ^ {*} \mathrm{P} (b | a) ^ {*} \mathrm{P} (c | a) ^ {*} \mathrm{P} (d | a, b, c) ^ {*} \mathrm{P} (e | a, b, c, d)
$$

From the assumption of conditional independence:

$$
\begin{array}{r l} & P (a, b, c, d, e) \\ & = P (a) ^ {*} P (b | a) ^ {*} P (c | a) ^ {*} P (d | b, c) ^ {*} P (e | d) \end{array}
$$

In this formalism, propositions are given numerical parameters signifying the degree of belief accorded to them under some body of knowledge, and the parameters are combined and manipulated according to the rules of probability theory. For example, if node A stands for the statement 'ITC is going to launch new products in 1994', then $P(A|K)$ stands for a person's subjective belief in A given a body of knowledge K, in this case could be: information of Indian tobacco industry, the Chairman's statement, and assessments of ITC's performance over the past 5 or 10 yr etc. These Bayesian formalisms obey three basic axioms of probability theory (given in Appendix A). The basic expressions in the Bayesian formalism are statements about conditional probabilities [6]. If these networks have a qualitative sign $\{+, -, 0\}$ over the directed arcs, then they facilitate qualitative analysis. Such networks are called as Qualitative Probabilistic Networks (QPNs henceforth) [4].

3.1.1.2. Qualitative Probabilistic Networks. Formally, a qualitative probabilistic network is a pair $G = (V, Q)$ . V is the set of variables, or vertices of the graph. Q is the qualitative relationships among the variables. There are basically two types of relationships that are represented on these networks. The first one is the qualitative influence, which is relationship describing the sign existing between a pair of variables. The other form is qualitative synergy, which is the interaction among the influences $[4,5]$ .

These networks are seen essentially as abstractions of influence diagrams that encode constraints on the probabilistic relation among the variables rather than precise numeric distribution. These are also seen as influence diagrams with the numeric conditional probability tables replaced by qualitative probabilistic relations among the variables. Similar to Influence Diagrams [26] inference here is accomplished by applying sequences of two truth-preserving operations: node reduction and link reversal.

## 3.1.2. Belief propagation using stochastic simulation

Lauritzen and Spiegelhalter [30] use clique-triangulation method to propagate beliefs. Pearl [6] uses belief revision as a method to update probabilities. Both these methods fail when the network under consideration has multiple links. Pearl [6] suggests the usage of stochastic simulation as a method to update beliefs under this condition. This method is an extension of the 'logic sampling' approach of Henrion [31]. In this method of computing probabilities, the frequency of events that occur in a simulation run are counted. For a causal model of a domain, this method is used to generate random samples of hypothetical scenarios that are likely to develop in the domain. The probability of any event or combination of events are then computed by counting the percentage of samples in which the event is true. Different possible scenarios can be generated by clamping the evidence variables to the values observed and performing stochastic simulation on the clamped network. Propagation of beliefs takes place by assigning conditional distributions to all the neighboring variables of a particular variable $X$ , and sequentially scanning the entire network with the computed distribution and finally instantiating with the new value of $X$ . (For more details on this method refer to Pearl [6]). This scheme of belief propagation is adopted in our study (the methodology is detailed in Section 4).

## 3.2. Deterministic networks—cognitive maps

A cognitive map can be seen as a picture or visual aid in comprehending the mappers' understanding of particular individual [32], group or organization [1]. They aim it to be seen as a representation that is amenable to analysis by both the mapper and others. These maps are also called as 'Cause Maps' because they basically try to capture causal linkages. For the present work we use the terms 'cause maps' and 'cognitive maps' interchangeably. Most methods follow 'cognitive mapping' method presented by Axelrod [3]. Axelrod and his collaborators used to understand political decision makers. Their work is based on 'content analysis' of the documents written by these political leaders and from the speeches made by them. For representational purpose, a cause map is usually drawn as short pieces of text linked with unidirectional arrows. Essentially, these maps are directed graphs. They are therefore characterized by an hierarchical structure. The directed arcs between two nodes have a qualitative sign over it. This representation resembles QPNs in topology. However the nodes here are deterministic. These maps have been used of late to map strategic thinking of organizations. Klein and Cooper [33] used this technique to examine the behavior and perceptions of individual decision-makers.

## 3.2.1. Mapping of strategic thought

Most academics and practitioners interested in organizations believe that conscious choices can, at least some of the time, affect economic and social outcomes in expected ways. Cognitive science characterizes minds as intentional, representational and computational. In addition, it stresses the significance of tracking the overt manifestations of intelligent behavior (intelligent strategic behavior in strategic management—in other words what strategists think and do). Eden [34] puts this aspect quite clearly. He argues the importance of vision of the key actors in an organization on its behavior. According to him, analytical techniques that focus on numbers and not on ideas, will rarely meet the requirements of understanding the behavior of a firm. A cognitive science approach to mapping strategic thought uses cognitive psychology and artificial intelligence to comprehend managerial minds: fathoming managers strategic intentions, deciphering their representational knowledge about strategy, studying their reasoning processes and recording a description of managerial behavior in strategic management setting. In short, this inter-disciplinary research focuses on understanding the minds of strategic managers. The principal criteria for reasoning efficiently is to have an appropriate scheme to represent the minds of the strategists. Formalizing knowledge as a computer program is a major contribution which cognitive science can add to the study of strategic thought. Stubbart and Ramaprasad [35] use several criteria to test knowledge representation schemes. Cognitive Mapping scheme of Axelrod [3] has facilitated knowledge representation in business strategy [1]. Eden [34] has developed a system, Strategic Options Development and Analysis (SODA), to capture the views and ideas of top management of various companies using cognitive maps. He has captured the causal assertions by interviewing the managers. He has developed ‘group maps’, which are an aggregation of beliefs of people who have similar thinking. From these group maps, he has developed a ‘strategic map’ which is the final aggregation of ideas of various people. The nodes (causal constructs identified from the interviews are represented as nodes) in this strategic group represent the consensus goals the company should achieve.

Chang Lee [36] uses technique of cognitive mapping to simulate strategic planning situations. He uses this technique to generate different scenarios. This kind of system can be an aid to the diagnostic systems detailed in Section 3. Bougon et al. [17] describes various cognitive processes in the organizations. However, these deterministic networks described so far have been used in a descriptive sense. They are used just as a representation tool by which a decision maker can comprehend the situation in the form of a graph. In effect, they are a static representation of the situation. They do not help in developing a possible future scenario. When new evidence comes, how does a person or an organization with this kind of causal map behave? This is an intuitive query for which deterministic networks do not provide an answer.

In summary, from the above discussion we can see the deterministic networks (cognitive maps) do not provide any method to capture uncertain reasoning. QPNs provide formalism based on probabilistic theory to reason uncertainty. As we have seen, organizations work in an uncertain environment. Reasoning this kind of complex decision making, like strategic decision making, we should ideally use networks like QPNs, which have set of formalisms built over them. These formalisms can aid a decision maker to study organizations much more clearly, by capturing the uncertainties, than pure deterministic reasoning (like in a cause map).

In Section 4 we detail about case study and the Research Methodology adopted to develop the cognitive maps and construct a QPN over the cognitive map.

## 4. Research methodology

Here we study the organizational action, that are primarily based on top manager's view of the environment and subsequent understanding of the same. We map the sample firms' top managers' understanding, and see how these interpretations change, along with the subsequent impact of these interpretations on organizational responses. A cognitive view of strategy formulation is essential. From the discussion in the previous sections, we find that Causal maps provide an excellent way of mapping the changing managerial beliefs. According to Narayanan and Fahey [2] “...Causal maps provide a convenient shorthand to describe the lenses which filter the data and means by which data are interpreted.” Narayanan and Fahey [2] have used revealed causal maps to map the assertions of causality the top managers choose to reveal. These revealed causal maps (RCMs) are taken as the principal maps to study the behavior.

## 4.1. Case study

The Indian Automobile Industry is selected as the context of study. This industry's scenario has undergone drastic transformations in the form of reduced government concessions. In the LCV and HCV (Light Commercial Vehicle and Heavy Commercial Vehicle) segment the scenario is quite different. The key players, Firm A and Firm B introduced little innovation into their products (in this paper the names of the firms and relevant confidential details are not disclosed on the requests made by the firm management). The thrust was more on indigenous product development. Marketing was not considered important in this segment of the industry. Product quality and after sales service were considered the key differentials in this segment. However the picture changed a bit in the late 80s. After the sales boom in the mid-eighties, this industry had fallen into steady recession between 1989 and 1992. The principal causes for this, according to the manufacturers, were the steep hike in fuel prices, the devaluation of the rupee, increase in excise duties and change in the tax trade off rules pertaining to depreciation. Escalation in prices, coupled with reduced buying capacity among the middle class caused the shrinkage in demand in this segment.

Overall, this industry necessitated high investments but the margins are very low. Therefore, the need for extensive infrastructure created high barriers of entry so far. With the opening of the Indian economy, global players are expected to enter the market and these high entry barriers do not as such offer any protection. Big players like General Motors, FIAT, Mitsubishi are planning to enter through equity participation. In other words, the industry is geared for lot of activity, and it is felt that it would be worthwhile studying the behavior of a key player (Firm A).

## 4.2. Conceptual scheme for organizing cognitive maps

The conceptual scheme used here is similar in approach to that detailed in Narayanan and Fahey [2]. Decision makers use different languages to express themselves and when these assertions are mapped, there would be a definite gap between representation and reality. The first step was to 'translate' these maps into a language which serves some theoretical purpose. The conceptual scheme used is depicted in Fig. 2. It basically consists of three blocks: Environment, Strategy and Objectives and concepts prevalent in strategic management. Each block is decomposed into constituent elements. The block Environment is conceived in terms of macroenvironmental and industry. Strategy is decomposed into functional manifestations: Marketing, Manufacturing, R and D, Finance, Personnel and Organization related. Causal linkages are elicited from causal assertions made by the decision maker.

![](/api/attachments/SNHYZBVB/fulltext/images/4f924a67b94235e6c1d7efa63f12769ad8fd3f5e022bd3c6257aa0ff32e63569.jpg)  
Fig. 2.

## 4.3. Data sources

Sources for data for the present study are shareholders' reports. Researchers have used these reports to identify corporate strategies [37], assess causal assertions within firms [18] and study organizational renewal [1,2]. The central assumption is that these reports reflect the beliefs of top management. Annual reports are typically prepared by public relations departments. In all probabilities there is likelihood of the specific words being edited by others in the organization. The other data source that have been used are published interviews of the chief executives at that moment of time and published articles on the company's profile and special reports. Furthermore, refining of the revealed causal maps are done in consultation with the executives of the companies. However, the primary source of data are annual reports as it is believed that this document is too important as not to be given close attention by the top management. In this study, one year is adopted as the temporal unit for stratification of data. It is believed that one year is a sufficiently long period to evidence changes in the cognitive maps developed.

## 4.4. Stages for development of cognitive maps

(1) Initially, 'raw' cognitive maps are developed. These raw cognitive maps are the simple causal assertions taken from the annual reports. The coding procedures followed are detailed in [2].

(2) From these raw cognitive maps, revealed causal maps are developed. Thus, when the concepts of a raw cognitive map are categorized onto a framework it leads to a revealed cognitive map. All causal assertions are categorized into various functional manifestations.

(3) For the latest of the ‘raw’ cognitive map, subjective probabilistic estimates for the company are obtained. The choice of studying only the last year is due to memories of the happenings for earlier years would have dimmed and also there would be a bias in the estimates.

To guard against researcher's bias, both authors worked independently in mapping text into a cognitive map, and then in translating a cognitive map into a revealed casual map. The inter-coder reliability was more than $95\%$ in this exercise.

Thus the primary motivation in transforming a raw cognitive map onto a revealed cognitive map is to assess the longitudinal analysis of the firm's behavior. These representations (revealed cognitive map) are looked at keeping the following issues in mind [34]: How does the structure of the revealed cognitive maps change over time? How do the maps accommodate changing environmental conditions? And what differences in strategic thrusts are visible in the maps over a period of time? It is proposed to study the possible future behavior, in terms of belief revision of subjective estimates, and how they logically follow the past strategy adopted by the company, in terms of analysis from the revealed cognitive maps.

These raw cognitive maps and the revealed cognitive maps (RCMs) that are constructed are used as the basis to study the behavior of Firm A. For the latest of the revealed cognitive map the subjective estimates are captured and stochastic simulation is done.

## 5. Results and conclusions

The strategic behavior of the firm is studied by constructing cognitive maps for the years starting from 1989–1990 to 1992–1993. Figs. 4 and 5 give the abstract form of the RCM developed for the years 1989–1990 and 1992–1993 respectively. The behavior of the firm is understood by noticing the inter-linkages among the hierarchical blocks in the conceptual framework constructed for every cognitive map developed (Fig. 3 shows part of the raw cognitive map constructed for the year 1992–1993, which is later converted to a RCM, Fig. 5).

## 5.1. Data interpretation

From the RCMs, it is interpreted that the company under consideration has borne the brunt of general economic recessionary trends prevailing in the economy. These observations are obtained from looking at the varying casual linkages among the blocks in light of the questions sighted for investigation given in Section 4.4. These observations are then compared to the environment setting the firm is experiencing during that year. There were indications (in 1989–1990) to diversify into other segments of the automobile industry. The company eventually entered into passenger car segment in 1991–1992 from heavy commercial vehicle segment. Some of the problems it faced in 1992–1993 like threat of entry of Multi national Companies into Indian market, shift in customer focus and increase in fuel prices resulting in demand for fuel efficient vehicles etc., never existed in 1989–1990. This shows that the management never considered to look into these large scale long term shifts.

The RCMs indicated that the company faced severe labor unrest problem in couple of its plants in 1988–1989. Cognitive maps of successive years (1991–1992) of the company revealed that the management has started off several schemes for its employees in 1991–1992, and 1992–1993.

![](/api/attachments/SNHYZBVB/fulltext/images/ea43b9303a5192d0e7f1d48a94ecdf038c7164f77de6e69b78fc35b8dc94c411.jpg)  
Fig. 3.

![](/api/attachments/SNHYZBVB/fulltext/images/6331215ea8c17cdff7fd79cbc31f70660370bd257987c14fdb9db73d96c86277.jpg)  
Fig. 4.

From the cognitive maps, it is also seen that the company also started to stress more on indigenous product development, it has even started its own R&D center. It has started collaborating with MNCs which are considered to be leaders in their field, as a measure to upgrade its technology to world standards.

In the year 1988–1989, there was little emphasis on marketing and customer services. The picture is quite different in 1992–1993. There are programs which are being launched within the company to emphasize the importance every link of its value-chain [25]. In 1992–1993, the cognitive maps revealed that the top management has started to strengthen the marketing function.

For the year 1990–1991, there has been increasing emphasis on exports and environment consciousness in the company. These aspects became important in the light of events that are taking place in the Indian economy. The government integrated Indian economy with the world economy in a step by step liberalization process. The company has consolidated its business by integrating backwards (by acquiring some suppliers and by internally sourcing critical components). There has also been restructuring in the Board in consequence to changes in the Board of the holding company.

These strategic changes revealed from the cognitive maps make us conclude that the company is gearing up to a market driven economy from the regulated and protected economy. There is also increase in issues which are not dealt with in the earlier years, viz. new product development, by the top management.

From the above analysis, we understand that the company till 1990 has enjoyed the fruits of a protected market and became a leading player in the Indian Automobile industry, feels its position threatened. It has geared itself to face the challenges of liberalization.

## 5.2. Stochastic simulation exercise

For the RCMs of year 1992–1993, as detailed in the earlier sections, subjective judgments of executives-in-charge are captured. A computer simulation is done for the part cognitive map (developed for the year 1992–1993) given in Fig. 3. Software for performing this stochastic simulation has been developed in FORTRAN on the VAX/VMS 3300 computer system. Each simulation cost 100 iterations for convergence, this number was arrived after doing several dry runs. Several hypothetical scenarios were generated and revised probabilistic estimates that occurred at each node at the end of the simulation run were taken as revised subjective estimates. Table 1 gives the subjective estimates obtained from managers for the cognitive map given in Fig. 3. Table 2 details about the simulation for the two hypothetical scenarios.

In scenario 1, we observe that there has been an increase in profits. This means that D = 1. We then instantiate all other unobserved variables to an arbitrary initial state (here, A = 1, B = 1, C = 1 and E = 0). As described in Pearl [6], each variable from the arbitrary initial state, chooses another state in accordance with the conditional probability of that variable, based on the current state of the variables in the neighborhood. Any variable, say X, chooses a particular state in the range $P(x|W_{x})$ to $P(-x|W_{x})$ , where $W_{x}$ is the Markov blanket for variable X. If X = A, then $W_{x}$ consists of nodes B and C.

![](/api/attachments/SNHYZBVB/fulltext/images/0e859c77b44a9d83a89502b0c039c5ee41534ecced3c540a4bb838aacf02b405.jpg)  
Fig. 5.

<table><tr><td colspan="2">Subjective estimates (inputs to the simulation programme)</td></tr><tr><td>P(a) = 0.3</td><td></td></tr><tr><td>P(b|a) = 0.2</td><td>P(b|-a) = 0.7</td></tr><tr><td>P(c|a) = 0.75</td><td>P(c|-a) = 0.25</td></tr><tr><td>P(d|b,c) = 0.75</td><td>P(d|b,-c) = 0.7</td></tr><tr><td>P(d|-b,c) = 0.8</td><td>P(d|-b,-c) = 0.1</td></tr><tr><td>P(e|b) = 0.6</td><td>P(e|-b) = 0.1</td></tr></table>

Table 1 gives the subjective probabilistic estimates for the causal network depicted in Fig. 3. From Table 2 we observe that clamping node ‘increase in profits and margins’ (node D) to value 1 leads to an increase in probability of node ‘demand for Firm A vehicles’ (node B). From Fig. 3, we can see that nodes B and D are positively related. An increase in probability of occurrence of node B increases the probability of occurrence of node D, from relation (1). Similarly, nodes D and C are negatively related. An increase in the probability of occurrence of node C decreases the probability of occurrence of node D.

From Fig. 3, we can see that nodes A and B are negatively related. An increase in the probability of occurrence of node A reduces the probability of occurrence of node B. Similarly, nodes A and C are positively related. An increase in probability of occurrence of node A increases the probability of occurrence of node C. In the second scenario, we clamped node A (which means there is general economic recession existing in the economy), and node D (which means that there is increase in profits) to value 1 and performed the simulation. The probability of node ‘rising costs of production’ came down and the node ‘demand for Firm A vehicles’ also came down. In other words the top management attributes the cause for ‘increase in profits and margins’ to node ‘rising costs of production’ in this particular scenario. This is because of reduction in the probability of the occurrence of the node ‘rising costs of production’ which had a causal influence on the other nodes.

Table 2  
Simulation results (outputs from the simulation programme)

<table><tr><td>Scenario 1</td><td>Scenario 2</td></tr><tr><td>Clamp node</td><td>Clamp nodes</td></tr><tr><td>D (estimates after 100 runs)</td><td>D and A (estimates after 100 runs)</td></tr><tr><td>P(b|d) = 0.8</td><td>P(b|d,a) = 0.3</td></tr><tr><td>P(c|d) = 0.7</td><td>P(c|d,a) = 0.55</td></tr></table>

The choice of the starting state values of the variables greatly influenced the number of runs it took to converge.

From this exercise it has been demonstrated that as and when new evidence is gathered, by clamping the related nodes in the belief network, we may see changing beliefs in a belief network. This simulation model shows that, if we have a cognitive map of the top management of the company and the subjective estimates, we can observe how their perceptions change when new events take place.

This kind of scenario generating methods are particularly useful in competitor analysis. If a company can develop a cognitive map of its competitor, with approximate subjective estimates, it can predict the behavior of its competitor in terms of the revised beliefs. These beliefs get transformed into actions. Finally, these actions set the strategy that the company adopts. Similarly, to any researcher who is interested in issues related to impacts of changes in top management thinking on organizational behavior this technique would be useful.

## Acknowledgements

The authors like to thank Prof. J. Ramachandran of the Corporate Strategy and Policy Area, Indian Institute of Management Bangalore for the fruitful discussions with respect to the case study in this paper.

## Appendix A

For any two events A, B, the three basic axioms of Bayesian formalism are:

1. $0 \leq P(A) \leq 1;$

2. $P(\text{sure proposition}) = 1$ ;

3. $P(A$ or $B) = P(A) + P(B)$ , if $A$ and $B$ are mutually exclusive.

## References

[1] P.S. Barr, J.L. Stimpert, A.S. Huff, Cognitive change, strategic action and organizational renewal, Strat. Manage. J. 13 (1992) 15–36.

[2] V.K. Narayanan, L. Fahey, Evolution of revealed causal maps during decline: a case study of admiral, in: A.S. Huff (Ed.), Mapping Strategic Thought, John Wiley and Sons, 1990, pp. 109–134.

[3] R. Axelrod, The cognitive mapping approach to decision making, in: R. Axelrod (Ed.), Structure of Decision, Princeton University Press, Princeton, NJ, 1976, pp. 221–250.

[4] M.P. Wellman, Fundamental concepts of Qualitative Probabilistic Networks, Artificial Intelligence, Vol. 44, 1990a, pp. 257–303.

[5] M.P. Wellman, Graphical Inference In Qualitative Probabilistic Networks, NETWORKS, Vol. 20, John Wiley and Sons, 1990b, pp. 687–701.

[6] J. Pearl. Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference, Morgan Kaufmann, 1988.

[7] D. Jung, J.R. Burns, Connectionist approaches to inexact reasoning and learning systems for executive and decision support-conceptual design. Decision Support Syst. (North-Holland) 10 (1993) 37–66.

[8] A. Newell, H.A. Simon, Human Problem Solving, Prentice-Hall, Englewood Cliffs, NJ, 1972.

[9] H.A. Simon, New Science of Management Decision, Harper and Row, New York, 1960.

[10] V. Zwass, Management Information Systems, Wm.C. Brown Publishers, 1992.

[11] A. Basu, A. Dutta, Reasoning with imprecise knowledge to enhance intelligent decision support, IEEE Trans. Syst. Man and Cybernetics 19 (4) (1989) 756–770.

[12] H. Mintzberg, D. Reisinghani, A. Theoret, The structure of unstructured decision processes, Admin. Sci. Quart. 21 (1976) 247–275.

[13] N.H. Ata Mohammed, F.J. Courtney, D.B. Paradice, A prototype DSS for structuring and diagnosing managerial problems, IEEE Trans. Syst. Man and Cybernetics 18 (6) (1988) 899–907.

[14] J.E. Dutton, L. Fahey, V.K. Narayanan, Toward understanding strategic issue diagnosis, Strat. Manage. J. 4 (1983) 307–323.

[15] R.L. Ackoff, Creating the Corporate Future, Wiley, New York, 1981.

[16] D. Schendel, Introduction to the Summer 1992 special issue on strategic process research, Strat. Manage. J. 13 (1992) 1–4.

[17] M. Bougon, K. Weick, D. Binkhorst, Cognition in organisations: an analysis of the Utrecht Jazz Orchestra, Admin. Sci. Quart. 21 (1977) 606–639.

[18] J.R. Bettman, B.A. Weitz, Attributions in the board room: causal reasoning in corporate annual reports, Admin. Sci. Quart. 28 (1983) 165–183.

[19] G.R. Salancik, J. Meindel, Corporate attributions as strategic illusions of management control. Admin. Sci. Quart. 29 (1984) 583–600.

[20] H.J. Einhorn, R.M. Hogarth, Judging probable cause, Psych. Bull. 99 (1986) 3–19.

[21] B. Billman, F.J. Courtney, Automated discovery in managerial problem formulation: formation of causal hypothesis for cognitive mapping, Decision Sci. 24 (1993) 23–41.

[22] R. Milne, Strategies for diagnosis, IEEE Trans. Syst. Man and Cybernetics SMC-17 (3) (1987) 333–339.

[23] F.J. Courtney, B.D. Paradice, N.H. Ata Mohammed. A knowledge-based DSS for managerial problem diagnosis. Decision Sci. 18 (3) (1987) 373–399.

[24] J. Pearl, Fusion, propagation, and structuring in belief networks, Artificial Intelligence 29 (1986) 241–288.

[25] R.D. Shachater, Evaluating influence diagrams, Oper. Res. 34 (1986) 871–882.

[26] R.D. Shachater, Probabilistic inference and influence diagrams, Oper. Res. 36 (4) (1988) 589–604.

[27] J. Gordon, E.H. Shortliffe, The Dempster–Shafer theory of evidence, in: Glenn Shafer, Judea Pearl (Eds.), Readings in Uncertain Reasoning, Morgan Kaufmann Publishers, 1990, pp. 529–539.

[28] R. Hovorka, S. Andreassen, J.J. Benn, K.G. Olesen, E.R. Carson, Causal probabilistic network modeling—an illustration of its role in the management of chronic diseases, IBM Syst. J. 31 (4) (1992) 635–648.

[29] S.F. Roehrig, Path analysis and probabilistic networks: analogous concepts, in: Jay F. Nunamaker, R.H. Sprague (Eds.), Proceedings of the 26th Hawaiian International Conference on System Sciences, Vol. III, IEEE Computer Society Press, Los Alamitos, CA, 1993, pp. 523–532.

[30] S.L. Lauritzen, D.J. Speigelhalter. Local computations with probabilities on graphical structures and their application to expert systems, R. Stat. Soc. B50 2 (1988) 157–224.

[31] M. Henrion, Propagating uncertainty by logic sampling in Bayes' Networks, Technical Report, Department of Engineering and Public Policy, Carnegie Mellon University, 1986.

[32] J.A. Hart, Cognitive maps of three Latin American policy makers, World Politics XXX (1) (1977) 115–140.

[33] H.J. Klien, D.F. Cooper, Cognitive maps of decision-makers in a complex game, J. Oper. Res. Soc. 33 (1982) 63–71.

[34] C. Eden, Strategic thinking with computers. Long Range Planning 23 (6) (1990) 35–43.

[35] C.I. Stubbart, Arkalgud Ramaprasad, Comments on the empirical articles and recommendations for future research, in: A.S. Huff (Ed.). Mapping Strategic Thought. John Wiley and Sons, 1990, pp. 251–290.

[36] K. Chang Lee, A cognitive map knowledge-based strategic planning simulation, in: Jay F. Nunamaker, Ralph H. Sprague (Eds.), Proceedings of the 26th Hawaiian International Conference on Systems Sciences, Vol. III, IEEE Computer Society Press, Los Alamitos, CA, 1993, pp. 249–267.

[37] E.H. Bowman, Strategy, annual reports and alchemy, California Manage. Rev. 20 (1978) 64–71.

![](/api/attachments/SNHYZBVB/fulltext/images/25af16ae5a259bb603a081b4f0300652b0d517bd2e0945847044c47e4e52b8e3.jpg)

Decision Support Systems, Business Process Innovation, IT Strategy, and Competitive Strategy. He is a student member of Academy of Management.

Vadhri Srinivas is a doctoral student at the Indian Institute of Management Bangalore in Quantitative Methods and Information Systems Area. He holds a B.Tech in Electrical and Electronics Engineering from S.V. University, Tirupati; and M.E. in Controls and Instrumentation from CEG, Anna University, Madras. His research focus is: Representational issues of Strategic Thinking in organizations. His other research interest include: Uncertainty Representation,

![](/api/attachments/SNHYZBVB/fulltext/images/0923f87df2811b41862b1da74b93d9454de93f3082d17f2a06a6044d48d92273.jpg)

B. Shekar is an assistant professor in the Quantitative Methods and Information Systems Area of the Indian Institute of Management Bangalore. He holds a B.E. in Electronics and Communication Engineering from University of Madras; and M. Tech in Computer Technology from the Indian Institute of Technology Delhi; and a Ph.D. in Computer Science from the Indian Institute of Science, Bangalore. His research interests include Pattern Recognition, Decision Support Sys-

tems, Artificial Intelligence, and Fuzzy Theory and Applications. His research has been published in Pattern Recognition, Pattern Recognition Letters, along with several conferences' proceedings.
