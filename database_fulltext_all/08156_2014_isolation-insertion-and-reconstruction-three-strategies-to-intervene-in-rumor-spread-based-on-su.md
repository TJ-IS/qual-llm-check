---
otero_id: 8156
otero_key: "4RR7GX4H"
title: "Isolation, insertion, and reconstruction: Three strategies to intervene in rumor spread based on supernetwork model"
authors: "Ru-Ya Tian; Yi-Jun Liu"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.09.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Isolation, insertion, and reconstruction: Three strategies to intervene in rumor spread based on supernetwork model

Ru-Ya Tian <sup>a</sup>, Yi-Jun Liu <sup>b,</sup>⁎

<sup>a</sup> Agricultural Information Institute, Chinese Academy of Agricultural Sciences (CAAS), Beijing 100081, PR China

<sup>b</sup> Institute of Policy and Management, Chinese Academy of Sciences, Beijing 100190, PR China

## a r t i c l e i n f o

Article history: Received 14 April 2014 Received in revised form 1 September 2014 Accepted 1 September 2014 Available online 16 September 2014

Keywords: Opinion SuperNetwork Opinion intervention Isolation Strategy Insertion Strategy Reconstruction Strategy

## a b s t r a c t

Online public opinion has become an important issue affecting national bene<sup>fi</sup>t and security. Based on system modeling and simulation, combining quantitative model methods and network topology analysis, this article establishes an Opinion SuperNetwork model to investigate different strategies of online public opinion intervention. We analyzed the effects of online opinion environments, opinion agents, psychologies, and viewpoints on the online public opinion formation and evolution. We further used these factors to investigate isolation, insertion, and reconstruction strategies. The results show that all the three intervention strategies produce good results, while insertion strategy is the best. And the mutual in<sup>fl</sup>uence among superedges has the greatest impact on the result of intervention. Therefore, inserting positive superedges, meanwhile strengthening the mutual in<sup>fl</sup>uence among superedges, is the optimal intervention strategy. This investigation will help quantify the research of online public opinion intervention, while provides a new method for rumor intervention.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Public opinion re<sup>fl</sup>ects people's beliefs, attitudes, views, and emotions on various social events [1]. It is a strong “soft power” that greatly impacts on the development of those social events. Successful public opinion intervention can bene<sup>fi</sup>t the country from economic, social, and political aspects. For example, during the Iraq war, the United States government implemented a number of public opinion interventions. By close monitoring and effective intervention, the government made the public opinion supportive for the war in the early stages, which ensured the progress of the war and reduced the pressure on the government from the people [2]. With the rapid development of information technology, individual viewpoints spread vastly and quickly through various online media. This also changes the formation and evolution mechanisms of online public opinion. Completely new intervention methods have been investigated.

Dynamic models have advantages in the research of traditional public opinion evolutions. Complex network models have advantages in investigating the new-fashioned Internet-based public opinions. Combination of the two has been proven an even better approach. This article also adapts this approach, but instead of combining singlelayer network with dynamic models, we introduce the supernetwork model and combine it with dynamic models. Based on modeling and simulation methods, we investigated different intervention methods quantitatively, and got desired outcomes.

The rest of this paper is organized as follows. Section 2 reviews the previous studies of opinion intervention, and discusses the advantages and disadvantages of them. In Section 3, we described the online public opinion by an Opinion SuperNetwork, and then built three intervention models based on this supernetwork. In Section 4, we picked the “Guo Meimei Event”, and applied the methods described in Section 3 to it. The results are presented in Section 5, and different intervention strategies are compared. Section 6 concludes, and suggests possible future research approaches.

## 2. Related work

Opinion dynamic models are the most commonly used tools in studying evolution and intervention of public opinion. Ising model is one of the earliest opinion dynamic models [3]. Spins present agents with different opinions in Ising model. Based on the Ising model, a number of classic public opinion evolution models start to emerge, that include voter model [4], Sznajd model [5], majority rule model [6–8], social impact theory [9], bounded con<sup>fi</sup>dence models [10–12], CODA model [13–16], and the gambling model [17,18]. These models simulate the process and <sup>fi</sup>nal results of public opinion evolution. Detailed study of these models helps to understand the characteristics of public opinion evolution, and also shed light on the intervention of public opinion. Some scholars have adjusted various factors in the model of opinion formation, such as individual activity [19], personal authority [20], outside information impacts [21], and by doing so, successfully controlled the direction of the public opinion evolution and intervened in the public opinion model.

These models provide mathematical methods for studying public opinion evolution. But these models cannot provide fully interpretation on the complexities of the real public opinion network, in which the public opinions develop and evolve through the interactions among real people. In the recent years, with the rapid development of complex network theory, more and more complex network models are applied in the study of public opinion. Small-world network and scale-free network [22,23] are the most famous complex network models. A complex network model of public opinion provides us with the information of topologies and relationships among agents in public opinion network. Thus, the complex network theory has a growing role in the research of public opinion evolution and intervention [24–26].

However, single-layer network models cannot meet all the needs of studying the issue. The relationship between people is just one of the various driving forces of public opinion evolution. Therefore, we need to <sup>fi</sup>nd out a more comprehensive way to study the online public opinion network. Thus, in 2012, supernetwork models came into the <sup>fi</sup>eld. Supernetwork was <sup>fi</sup>rst proposed by an American computer scientist, Peter Denning [27]. And it was applied in traf<sup>fi</sup>c network [28], supply chain (logistics) [29], ecological networks [30], knowledge networks [31,32], and etc. In 2012, we <sup>fi</sup>rst applied the supernetwork model to public opinion research [33–36].

In this article, we built a four-layer Opinion SuperNetwork, based on which, the evolution of public opinion and three intervention strategies are studied.

## 3. Opinion intervention strategies

## 3.1. Opinion SuperNetwork

In the previous papers, the authors built a four-layer supernetwork model of public opinion. The four layers are agent, environment, psychology, and viewpoint. During the spread of opinion, agents are in certain opinion environment, and are in<sup>fl</sup>uenced by the environment, which provides an external driving force. Psychological status of an agent is different from others', which is an internal driving force. Agents will publish their viewpoints under the in<sup>fl</sup>uence of both internal and external driving forces [37]. According to this, we create a supernetwork model including Social Sub-Network, Environmental Sub-Network, Psychological Sub-Network, and Viewpoint Sub-Network, which is illustrated in Fig. 1.

In this model, Internet users and the replying relationships between them form the Social Sub-Network. Authorized information released by the government, opinion leaders, and mainstream presses forms the nodes of Environmental Sub-Network. The timing of release is also taken into account. Possible psychology status and the transformation relationships between them form the Psychological Sub-Network. Online viewpoint keywords are nodes of Viewpoint Sub-Network. And if two keywords have appeared in one post, there will be an edge between them. The relationships between nodes of different sub-networks form the superedges of the Opinion SuperNetwork.

Nodes in each layer of the supernetwork can be classi<sup>fi</sup>ed as being positive or negative, whereas the negative nodes will bene<sup>fi</sup>t the spreading of the rumor, and vice versa. We can dig the reply network among netizens of the study case directly, and identify the main information during that time period by focusing on mainstream media. To identify the psychological status of a netizen (i.e. an Internet user) and its attribute of being positive or negative, we analyze the text of every post using ICTCLAS (Institute of Computing Technology, Chinese Lexical Analysis System), a specialized software that can split every sentence into words, and extract nouns, adjectives, and verbs. Then, HowNet software will further analyze the extracted words and classify them into 5 different psychological types according to Likert scale. Based on the same processing by ICTCLAS, we can also cluster the words which we extracted before by barycentric clustering, and the cluster results are the main viewpoints [38].

Then, the superedges in the supernetwork can be divided into three types. The one that contains only positive nodes is a “positive superedge $( S E ^ { + } ) "$ . The one with at least one negative node is a “negative superedge $( S E ^ { - } ) "$ . If all nodes in the superedge are negative, it is classi<sup>fi</sup>ed as “pure negative superedges”. In Fig. 1, color red represents a negative attribute. Color green represents a positive attribute. The solid red line in the <sup>fi</sup>gure represents a negative superedge, and the green solid line represents a positive superedge.

## 3.2. Intervention strategy-isolation model

According to the theory of two-step <sup>fl</sup>ow of communication [39], most people's opinions are in<sup>fl</sup>uenced by “opinion leaders”. Opinion leaders are in<sup>fl</sup>uenced by the mass media. So ideas <sup>fl</sup>ow from mass media to opinion leaders, and then to a wide population. Opinion leaders play important roles of mediation or <sup>fi</sup>ltering in the process of communication and information spreading. Focusing on the “opinion leaders” is the idea of isolation strategy, i.e. removing opinion leaders will greatly change the spreading of information.

Isolating one negative superedge under certain rules will make changes of node attributes based on the changes of network structure, and further lead negative superedges in the supernetwork to change to positive ones. In Fig. 2, the solid lines represent the existing relationships between the elements. The superedge within the dashed box is the one under isolation. Dashed lines indicate the changed relationships between elements after isolation.

This article uses the ORA [40] to identify elite <sup>fi</sup>gures and key <sup>fi</sup>gures in supernetwork. A superedge containing elite <sup>fi</sup>gure is an elite superedge. A superedge with key <sup>fi</sup>gure is a key superedge. Accordingly, there will be three sub-strategies (expressed as $\mathsf { S } 1 - \mathsf { a } , \mathsf { S } 1 - \mathsf { b } ,$ and S1-c). S1-a: Isolating elite superedges; S1-b: isolating key superedges; and S1-c: isolating ordinary superedges. The implementation of these strategies in the Opinion SuperNetwork is carried out according to the following rules.

## 3.2.1. Rule 1. Evolution of Environmental Sub-Network

A negative environment is the one with spread of rumors, denoted by $E ^ { - }$ <sup>−</sup>. Environment of positive attribute refutes rumors, denoted by $E ^ { + }$ . After superedge isolations, superedge with agent A in it changes. It disconnects its connections of the isolated negative environment node, in turn connects to a positive node in Environmental Sub-Network. The new environment is $E ^ { \prime }$ . Its property depends on environment information E and its neighbors (other agents having reply relationships with it), namely,

$$
E ^ {\prime} = \frac {\sigma_ {E} \times N + \sum \sigma_ {j} \times 2}{N}.\tag{1}
$$

$\sigma _ { E } = + 1$ , it is the property of the new positive environmental information. $A _ { j }$ is the neighbor of agent $A _ { i } ,$ and σ is his point of view. When the viewpoint is positive, $\sigma _ { j } = + 1 ;$ ; otherwise $\sigma _ { j } = - 1 . j = 1 , 2 , \cdots , \Nu ,$ and $j \neq i , \Nu$ is the total number of the neighbors of agent $A _ { i \cdot }$

## 3.2.2. Rule 2. Evolution of Psychological Sub-Network

Positive psychology, with which the agent is reluctant to believe the rumors, is denoted by $P ^ { + }$ . Negative psychology, with which the agent is willing to believe the rumors, is denoted by $P ^ { - }$ , neutral psychology is $P ^ { 0 }$

Agent's psychology nodes connection changes with the environment changes. When the agent is exposed to a changed environment, no matter the change is caused by the change of the surrounding environment property in Environmental Sub-Network or by the change of the neighbors, we can calculate the new environment according to fomula (1). And then calculate the psychology transition probabilities in this new environment. The probability that the agent's positive psychology transforms to a negative one is

![](/api/attachments/4RR7GX4H/fulltext/images/2138c291a6475605c162b448db2f772d840a19ef2c2e2180c10273b9638738e4.jpg)  
Fig. 1. Diagram of Opinion SuperNetwork structure.

$$
\rho^ {+ \rightarrow -} = \frac {\exp (- E ^ {\prime} / T)}{\exp (E ^ {\prime} / T) + \exp (- E ^ {\prime} / T)}.\tag{2}
$$

And the probability that the agent's negative psychology transforms to a positive one is

$$
\rho^ {- \rightarrow +} = \frac {\exp (E ^ {\prime} / T)}{\exp (E ^ {\prime} / T) + \exp (- E ^ {\prime} / T)}.\tag{3}
$$

T is the temperature of the public opinion environment, re<sup>fl</sup>ecting the degree of concern on the event by the public. If the agent's psychology changes, its connection with the nodes in Psychological Sub-Network changes, and so does its superedge.

## 3.2.3. Rule 3. Evolution of Social Sub-Network

Positive agent $A ^ { + }$ is the one that harbors positive psychology, while negative agent $A ^ { - }$ harbors negative psychology. The property of an agent is judged in accordance with its psychological attribute according to the following rules:

![](/api/attachments/4RR7GX4H/fulltext/images/0fd0043c0927d2bbecb6f05e67257293869309f1a8dbc69981c44b95a2f56e13.jpg)  
Fig. 2. Diagram of isolation strategy.

① ∃ psychology of the agent is negative, then the agent is negative.

② ∀ psychology of the agent is positive, then the agent is positive.

## 3.2.4. Rule 4. Evolution of Viewpoint Sub-Network

The viewpoint expressed as spreading rumors is denoted by $K ^ { - }$ while the one clarifying rumors is $K ^ { + }$ . Viewpoint of the agent changes with the change of the agent's property.

① When the property of the agent changes from negative to positive, negative viewpoints of the agent shift to the majority of the neighbors' positive viewpoints.

② When the property of the agent changes from positive to negative, positive viewpoints of the agent shift to the majority of the neighbors' negative viewpoints.

If any viewpoint of agent A is changed, its connection with the node in Viewpoint Sub-Network changes, and so does its superedge.

## 3.3. Intervention strategy-insertion model

Economists often use “Herd Behavior” to describe the group psychology of economy individuals. Herd Behavior describes how individuals in a group can act together without planned direction. Flock is a very messy organization. But if there is a leader in the move to occupy the main attention, the whole <sup>fl</sup>ock will continue to imitate the leader's every move. The whole <sup>fl</sup>ock then goes to wherever the leader goes to. Insertion strategy uses “Herd Behavior” theory. We insert a positive superedge to manipulate leader's behavior. In this way we guide the direction of public opinion, so as to achieve the purpose of the intervention of online public opinion.

Inserting one positive superedge under certain rules will make changes of node attributes based on the changes of network structure, and further lead negative superedges in the supernetwork to change to positive ones. In Fig. 3, the solid lines represent the existing relationships between the elements. The superedge within the dashed box is the inserted superedge. Dashed lines indicate the changed relationships between elements after insertion.

![](/api/attachments/4RR7GX4H/fulltext/images/9d3ebe07e108fe825b7b9276e813a056d647856f03db5eae24b2b8d275a5fdd3.jpg)  
Fig. 3. Diagram of insertion strategy.

When a positive superedge is inserted, in<sup>fl</sup>uence effects of the inserted superedge on the supernetwork structure should be under consideration. So are the boundary of superedge choosing and mutual in<sup>fl</sup>uence between ordinary superedges. Accordingly, here are the three sub-strategies (expressed as S2-a, S2-b, and S2-c) of insertion strategy, namely, S2-a: Adjusting the in<sup>fl</sup>uence of the inserted leader superedge; S2-b: adjusting the selection boundary of guiding objects; and S2-c: adjusting the mutual in<sup>fl</sup>uence between ordinary superedges inside the supernetwork. The implementation of these strategies in the Opinion SuperNetwork is carried out according to the following rules.

The attitude of agent $A _ { i }$ depends on its superedge $S E _ { i } , \ S E _ { i } =$ $\{ A _ { i } , E _ { i } , P _ { i } , K _ { i } \}$

$A _ { i }$ expresses social situation in public opinion spreading, values for 0, 0.5 and 1. 0 means that majority of the neighbors believe rumors. 1 means that the majority do not believe rumors. 0.5 means that the proportion of neighbors who do and do not believe rumors is even.

$P _ { i }$ represents the psychological situation in public opinion spreading, values for 0, 0.5 and 1. 0 expresses that the psychology is willing to believe the rumors. 1 means that the psychology is reluctant to believe the rumors. 0.5 means that psychology is neutral.

$E _ { i }$ expresses environmental condition in public opinion spreading, values for 0 and 1. 0 means that a negative environment with spread of rumors, 1 means that a positive environment refutes rumors.

$K _ { i }$ represents the viewpoint situation in public opinion spreading, values for 0, 0.5 and 1. 0 indicates that viewpoint is negatively expressed as spreading rumors. 1 indicates a positive point of view clarifying rumors. 0.5 means a neutral point of view.

In this study, we take the condition of $S E _ { i } = 0 . 3 \times A _ { i } + 0 . 2 5 \times E _ { i } +$ $0 . 2 5 \times P _ { i } + 0 . 2 \times K _ { i } .$ The function means that agents have the greatest contributions to the formation of a superedge, and the viewpoints have the least ones, while environment and psychology have relative medium contributions. $S E _ { i } = f ( A _ { i } , E _ { i } , P _ { i } , K _ { i } )$ is an abstract function, which can be adjusted according to the speci<sup>fi</sup>c situation to get desirable intervention effects.

Superedge contains the information comprehensively of public opinion agent, public opinion environment, agent's psychology and point of view, and the value ranges in [0,1]. Closer to 0 indicates supporting rumors, while closer to 1 indicates not supporting the rumors.

Implementation of guiding public opinion can be conducted by guiding superedge SE . Set a supernetwork containing N superedges. Insert a “leader” superedge $S E _ { 0 } .$ It evolves following Rule 1.

Rule 1. Connect the “Leader” superedge $S E _ { 0 }$ to the “worst” superedge $S E _ { S ( t ) }$ (or one of the “worst” superedges, e.g. S t arg min 1≤i≤N $\{ S E _ { i } ( t ) \} )$ . “Leader” superedge $S E _ { 0 }$ update rule is as follows.

$$
S E _ {0} (t) = \left\{ \begin{array}{l l} S E _ {S (t)} (t) + \alpha , & \quad \text { if }    S E _ {S (t)} <   1 - \beta \\ S E _ {0} (t), & \quad \text { if }    S E _ {S (t)} \geq 1 - \beta \end{array} \right..\tag{4}
$$

When the “worst” superedge supports rumors, the “leader” superedge guides it with intensity α. When the “worst” superedge does not support rumors, the “leader” superedge does not act. Under the guidance of “leader” superedge, the other ordinary superedges update their property values according to Rule 2.

Rule 2. Ordinary superedge SE updates its property value as the following rules.

A. Under the condition of $S E _ { i } ( t ) \geq 1 - \beta ,$

$$
S E _ {i} (t + 1) = \left\{ \begin{array}{l l} S E _ {i} (t) - \gamma , & \text { if } \frac {1}{n} \sum_ {j = 1} ^ {n} S E _ {j} (t) <   1 - \beta \\ S E _ {i} (t), & \text { if } \frac {1}{n} \sum_ {j = 1} ^ {n} S E _ {j} (t) > 1 - \beta \\ \left. \begin{array}{l} S E _ {i} (t) - \gamma , \quad \text { with   probability } k \\ S E _ {i} (t), \quad \text { with   probability } 1 - k \end{array} \right\}, & \text { if } \frac {1}{n} \sum_ {j = 1} ^ {n} S E _ {j} (t) = 1 - \beta \end{array} . \right.\tag{5}
$$

When ordinary superedge does not support rumors, there is an internal in<sup>fl</sup>uence γ on it from its neighbors if the average property of its neighbors expresses as supporting the rumors; no effect on it if its neighbors are not supporting the rumors; there is an internal in<sup>fl</sup>uence γ on it with probability of k if average property of its neighbors is neutral.

B. Under the condition of $S E _ { i } ( t ) < 1 - \beta ,$

$$
S E _ {i} (t + 1) = \left\{ \begin{array}{l l} S E _ {i} (t), & \text { if } \frac {1}{n} \sum_ {j = 1} ^ {n} S E _ {j} (t) <   1 - \beta \\ S E _ {i} (t) + \gamma , & \text { if } \frac {1}{n} \sum_ {j = 1} ^ {n} S E _ {j} (t) > 1 - \beta \\ \left. \begin{array}{l} S E _ {i} (t) + \gamma , \quad \text { with   probability } k \\ S E _ {i} (t), \quad \text { with   probability } 1 - k \end{array} \right\}, & \text { if } \frac {1}{n} \sum_ {j = 1} ^ {n} S E _ {j} (t) = 1 - \beta \end{array} . \right.\tag{6}
$$

When ordinary superedge supports rumors, there is an internal in<sup>fl</sup>uence γ on it from its neighbors if its neighbors are not supporting the rumors; no effect on it if the average property of its neighbors expresses as supporting the rumors; there is an internal in<sup>fl</sup>uence γ on it with probability of k if average property of its neighbors is neutral.

In the above formula, n is the total number of neighbor superedges of $S E _ { i } . \propto , \beta ,$ , and γ are controllable parameters. α re-<sup>fl</sup>ects guiding intensity of the “leader” superedge. The greater the value is, the greater the “leader” superedge guiding intensity is. β re<sup>fl</sup>ects the dividing line of guiding objects selection. It characterizes the threshold of guided superedges. γ re<sup>fl</sup>ects the internal in<sup>fl</sup>uence of supernetwork, namely, the interaction between ordinary superedges.

## 3.4. Intervention strategy-reconstruction model

In chaos theory, butter<sup>fl</sup>y effect describes the sensitive dependency on initial conditions in which a small change at one place in a deterministic nonlinear system can result in large differences in a later state. A tiny change can affect the development of things totally. Based on the butter<sup>fl</sup>y effect theory, this article uses the way of reconstructing supernetwork structure to make an initial condition change in the system. So that the direction of public opinion changes in a chain reaction, so as to achieve the purpose of the intervention of online public opinion.

Reconstructing one superedge under certain rules will make changes of node attributes based on the changes of network structure, and further lead negative superedges in the supernetwork to change to positive ones. In Fig. 4, the solid lines represent the existing relationships between the elements. Dashed lines indicate the changed relationships between elements after reconstruction.

According to the structural characteristics of supernetwork and the rules of opinion spreading, the initial perturbation can be implemented on the opinion environment, opinion agent, agent's psychology or agent's point of view. Therefore here go the four sub-strategies (expressed as S3-a, S3-b, S3-c, and S3-d) of reconstruction strategy, namely, S3-a: Adjusting activation threshold in opinion environment; S3-b: adjusting attenuation radius of agent's impact; S3-c: adjusting stimulation of agent's psychology; and S3-d: adjusting aggregating effect of agent's viewpoint. The implementation of these strategies in the Opinion SuperNetwork is carried out according to the following rules.

## 3.4.1. Definition of opinion agent

A node in Social Sub-Network represents an opinion agent $A _ { i \cdot } A _ { j }$ are its neighbors, i.e. those have reply relationships with agent $A _ { i }$ in Social Sub-Network. Where $j = 1 , 2 , \cdots , n$ , n is the number of the agent's neighbors.

## 3.4.2. Definition of agent's viewpoint

$$
K _ {i} (t). K _ {i} (t) =
$$

$\sum _ { q = 1 } ^ { p } ( k _ { i } ( t ) ) _ { q }$ wherein $( k _ { i } ( t ) ) _ { q }$ is one of the keywords of agent $A _ { i }$ at time $t . p$ is the number of all the keywords of agent $A _ { i }$ at time t. That is to say, the viewpoint $K _ { i } ( t )$ of agent $A _ { i }$ at time t is expressed as the average value of the sum of all viewpoint keywords. $K _ { i } ( t )$ and $k _ { i } ( t )$ both have three kinds of values. +1 means opinion agent $A _ { i }$ expressed is positive that clari<sup>fi</sup>es rumors. −1 means negative viewpoint that spreads rumors. 0 means neutral.

## 3.4.3. Definition of opinion environment

The environment that agent $A _ { i }$ in is $E _ { i } .$ The value is $+ 1 0 \Gamma - 1$ , respectively as positive or negative environmental information.

## 3.4.4. Definition of agent's psychology

P is the psychology of agent A . The value $\mathsf { i } s + 1 , + 2 , - 1 , - 2 \mathsf { o r } 0 . + 1$ represents “positive” psychology. Agents under this kind of psychological driving force do not believe rumors. +2 represents “positive plus”

![](/api/attachments/4RR7GX4H/fulltext/images/67cad55bd162e20de79bd76a3da7bd131198cbb07fbeb3f7f20a8d9f9980a0a5.jpg)  
Fig. 4. Diagram of reconstruction strategy.

psychology. Agents under this kind of psychological driving force do not believe the rumors, and also persuade others not to believe rumors. $^ { - 1 }$ represents “negative” psychology. Agents under this kind of psychological driving force are willing to believe rumors. −2 represents “negative plus” psychology. Agents under this kind of psychological driving force are willing to believe the rumors, and also extend their discontent to the government or society. 0 represents “wavering” psychology. Agents under this kind of psychological driving force hold neutral attitude.

## 3.4.5. Definition of impact intensity

$$
I _ {i} = I _ {s} + I _ {n}.
$$

$\sum _ { I _ { s } = \frac { j = 1 } { m } } ^ { m } ( K _ { i } ( t ) ) _ { j }$ is the impact from reconstruction-source neighbors. $I _ { n } =$ $\underline { { \sum _ { j = 1 } ^ { n } \left( K _ { i } ( t ) \right) _ { j } } }$ is the impact from non-reconstruction-source neighbors, i e

is the impact from non-reconstruction-source neighbors, i.e. the impact of other common neighbors. $( K _ { i } ( t ) ) _ { j }$ <sub>j</sub> is the viewpoint of neighbors of agent $A _ { i }$ (either reconstruction-source neighbors or common ones) at time t. m is the number of the reconstruction-source neighbors of agent $A _ { i } .$ . n is the number of common neighbors of agent $A _ { i } .$ In other words, the impact intensity $I _ { i }$ on agent $A _ { i }$ at time t is the average value of the sum of all viewpoint keywords from the reconstruction-source and all the other common neighbors.

## 3.4.6. Definition of activation threshold

$c _ { i } = K _ { i } ( t ) - \lambda E _ { i }$ is the activation threshold that agen $A _ { i }$ accepts intervention. It is the difference between opinion's property value and environment attribute value. Wherein $K _ { i } ( t )$ is the viewpoint of agent $A _ { i }$ expressed at time $t . \lambda \in ( 0 , 1 )$ is an adjustable parameter, which represents the dependence of agent's activation threshold on the environment E .

At the initial time of the simulation, we select a superedge (reconstruction-source) to implement reconstruction to make its property change to positive. Any one of the agents affected by this change evolves in accordance with rules 1–3.

Rule 1. If $K _ { i } ( t ) = - 1$

$$
K _ {i} (t + 1) = \left\{ \begin{array}{c c} - 1 & I _ {i} <   c _ {i} \\ + 1 & \text { with   probability } \rho_ {1} \\ 0 & \text { with   probability } 1 - \rho_ {1} \end{array} \right\} I _ {i} \geq c _ {i}.\tag{7}
$$

If the opinion is negative at time t, then at the next time, if impact intensity of its neighbors on it is less than its activation threshold $c _ { i } ,$ its property remains unchanged. If impact intensity of its neighbors on it is no less than its activation threshold, its property transits to positive with probability $\rho _ { 1 } .$ , or to neutral with probability $1 - \rho _ { 1 } .$ . Probability $\rho _ { 1 } = \alpha ( | P _ { i } | ) ^ { - 1 } . P _ { i }$ is the psychology of agent $A _ { i }$ with a value of $- 1 0 \Gamma - 2 . \alpha \in ( 0 , 1 )$ is an adjustable parameter. It represents the dependence of probability ${ } ^ { \prime } \rho _ { 1 }$ on the psychology $P _ { i }$

Rule 2. $\mathrm { I f } K _ { i } ( t ) = + 1 ,$

$$
K _ {i} (t + 1) = \left\{ \begin{array}{c c} + 1 & I _ {i} > c _ {i} \\ - 1 & \text { with   probability } \rho_ {2} \\ 0 & \text { with   probability } 1 - \rho_ {2} \end{array} \right\} I _ {i} \leq c _ {i}.\tag{8}
$$

If the opinion is positive at time t, then at the next time, if impact intensity of its neighbors on it exceeds its activation threshold $c _ { i } ,$ , its property remains unchanged. If impact intensity of its neighbors on it doesn't exceed its activation threshold, its property transits to negative with probability $\rho _ { 2 } ,$ or to neutral with probability $1 - \rho _ { 2 } .$ . Probability $\rho _ { 2 } = \beta ( | P _ { i } | ) ^ { - 1 } . P _ { i }$ is the psychology of agent $A _ { i }$ with a value of $+ 1 \ 0 \Gamma \ + 2$ $\beta \in ( 0 , 1 )$ is an adjustable parameter. It represents the dependence of probability $\rho _ { 2 }$ on the psychology $P _ { i } .$

Rule 3. I $\begin{array} { r } { \mathbb { f } K _ { i } ( t ) = 0 } \end{array}$

$$
K _ {i} (t + 1) = \left\{ \begin{array}{c c} + 1 & I _ {i} > c _ {i} \\ - 1 & I _ {i} <   c _ {i} \\ 0 & I _ {i} = c _ {i} \end{array} \right..\tag{9}
$$

If the opinion is neutral at time t, then at the next time, if impact intensity of its neighbors on it exceeds its activation threshold $c _ { i } ,$ its property transits to positive. If impact intensity of its neighbors on it is less than its activation threshold $c _ { i } ,$ its property transits to negative. If impact strength of its neighbors on it is equal to its activation threshold $c _ { i } ,$ its property remains unchanged.

## 4. Data processing

## 4.1. Case introduction

On June 20th, 2011, Guo Meimei showed off her wealth on the Internet. She represented herself as “chief commercial manager of Chinese Red Cross”, living in a big house and driving Maserati. This caused widespread concerns and controversy. The Chinese netizens questioned the money <sup>fl</sup>ows of the Chinese Red Cross. A seemingly insigni<sup>fi</sup>cant event of a girl showing off triggered a trust crisis of the Red Cross. Different rumors spread and are exaggerated on the Internet and became a national event.

Based on public opinion data from the Internet, 2108 original posts about the Guo Meimei Incident were collected from “Phoenix BBS” (www.bbs.ifeng.com), from 489 recognized netizens that participated in the discussion. Several evolutionary summits exist in the development of the incident (Fig. 5). In this article, we selected 33 netizens who have most posts on each peak. Based on their reply relations, opinion environment, psychological statuses, and viewpoints, we built a supernetwork model of this public opinion crisis.

The supernetwork model was established according to the development of “Guo Meimei Incident". The model contains four sub-networks. including 33 agents in Social Sub-Network, 3 pieces of environmental information in Environmental Sub-Network, 5 psychological statuses in Psychological Sub-Network, and 20 viewpoints in Viewpoint Sub-Network. The details are illustrated in Table 1. Nodes in the supernetwork form 33 superedges by their relationships, including 6 positive superedges, 12 pure negative ones, and 15 negative ones (Fig. 1 & Table 1).

![](/api/attachments/4RR7GX4H/fulltext/images/a58a65228ff9e8c1aef90cc0fa73671b5249d2e7c25fc0a3e24cc4f5bb9c6bb6.jpg)  
Fig. 5. Guo Meimei incident post trends (partial view).

## 4.2. Simulation experiment

In this study, Matlab programming is used to seek the variation of the proportion of negative superedges over time under the circumstance of implementing the three strategies in public opinion intervention. And intervention ef<sup>fi</sup>ciency of different strategies and sub strategies on Guo Meimei Incident is under comparison, too. The procedure is as follows:

Step 1: Initialize property values of all elements and the topology of the Opinion SuperNetwork.

Step 2: Calculate the proportion of negative superedges. If the ratio is N0%, then continue, otherwise go to Step 4.

Step 3: Implement one piece of the intervention sub-strategies. Update the nodes' properties in all the four sub-networks according to the evolution rules of the intervention strategy.

Step 4: Calculate the ratio of negative superedges. If the ratio is N0%, return to Step 3 to cycle, otherwise end.

Implement all the three intervention strategies. Conduct 1000 independent simulation experiments under each sub-strategy, and take the average value as the result.

## 5. Results

## 5.1. Intervention effect of isolation strategy

$S E _ { 1 0 } ^ { + }$ and $S E _ { 2 2 } ^ { - }$ are both elite superedges. $S E _ { 1 0 } ^ { + }$ is a positive one. The number of negative superedges reduces slowly after the isolation of it. SE<sup>−</sup> is negative. There is a signi<sup>fi</sup>cant reduction of negative superedges after the isolation. It shows that the isolation strategy has a signi<sup>fi</sup>cant effect on public opinion intervention (Fig. 6(a)). The opinion agent in elite superedge is a hub node at the heart of the network. Its contribution to public opinion information dissemination is much larger than other ordinary nodes, which shows a power-law distribution. It is usually called opinion leader, who relies on the speci<sup>fi</sup>c public opinion environment to cater to mass psychology, and to guide the direction of public opinion. “Two-step <sup>fl</sup>ow of communication” theory in the Journalism is the practical application of this principle. So the isolation of elite superedges can intervene in public opinion effectively.

$S E _ { 1 3 } ^ { - } , S E _ { 1 8 } ^ { - } , S E _ { 2 8 } ^ { - } ,$ , and $S E _ { 2 9 } ^ { - }$ are the key superedges of pure negative ones. There is an obvious reduction of negative superedges after isolating them. Isolating SE<sup>−</sup> works best, because not only it contains the key environment node and key psychological node, but also it contains the most critical negative viewpoint nodes (Fig. 6(b)). Key superedges are potential elite superedges. They emerge gradually after excluding the elite ones, and occupy the position of “opinion leader”. Therefore we also need to pay attention to the key superedges when intervene in public opinion.

$S E _ { 3 2 } ^ { - } , S E _ { 1 5 } ^ { - } , S E _ { 1 6 } ^ { - } , S E _ { 2 5 } ^ { - } , S E _ { 2 4 } ^ { - } , S E _ { 2 } ^ { - }$ , and $S E _ { 6 } ^ { - }$ are ordinary superedges of pure negative ones. There is a reduction of negative superedges after isolating them although not as signi<sup>fi</sup>cant as the effects of isolating key superedges (Fig. 6(c)). Spiral of silence theory describes the process by which one opinion becomes dominant as those who perceive their opinion to be in the minority do not speak up because society threatens individuals with fear of isolation [41]. Individuals tend to publicly express their opinions and attitudes when they perceive their view to be dominant or on the rise. Conversely, when individuals perceive that their opinion is less popular or losing popularity, they are less likely to voice it in public. Isolating ordinary negative superedges makes negative voices decreased, leading to a spiral of silence phenomenon, so as to achieve the purpose of the intervention of public opinion.

## 5.2. Intervention effect of insertion strategy

The proportion of those who support the rumors remained unchanged at <sup>fi</sup>rst and then rose slightly before inserting “leader”

Opinion SuperNetwork of “Guo Meimei incident”.

<table><tr><td>Sub-Network</td><td>Node Number</td><td>Illustration</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">Environmental Sub-Network</td><td rowspan="3">3</td><td> $E_{1}^{-}$ </td><td colspan="4">Guo Meimei showed off her wealth, triggering a trust crisis of the Red Cross.</td></tr><tr><td> $E_{2}^{+}$ </td><td colspan="4">Red Cross released a statement to clarify no relationships with Guo Meimei.</td></tr><tr><td> $E_{3}^{-}$ </td><td colspan="4">Netizens questioned the investigation results of Beijing police.</td></tr><tr><td rowspan="2">Psychological Sub-Network</td><td rowspan="2">5</td><td> $P_{1}^{+}$ </td><td> $P_{2}^{+}$ </td><td> $P_{3}^{0}$ </td><td> $P_{4}^{-}$ </td><td> $P_{5}^{-}$ </td></tr><tr><td>Positive plus</td><td>Positive</td><td>Wavering</td><td>Negative</td><td>Negative plus</td></tr><tr><td rowspan="2">Social Sub-Network</td><td rowspan="2">33</td><td> $A_{1}^{-}$ </td><td> $A_{2}^{-}$ </td><td> $A_{3}^{-}$ </td><td>...</td><td> $A_{33}^{-}$ </td></tr><tr><td>Zhou Lubao</td><td>Grdgg</td><td>Mountain Top</td><td>...</td><td>Scholar</td></tr><tr><td rowspan="4">Viewpoint Sub-Network</td><td rowspan="4">20</td><td> $K_{1}^{-}$ </td><td colspan="4">Question Guo Meimei&#x27;s showing off.</td></tr><tr><td> $K_{2}^{-}$ </td><td colspan="4">Pay attention to the healthy growth of the post-90s generation.</td></tr><tr><td>...</td><td colspan="4">...</td></tr><tr><td> $K_{20}^{+}$ </td><td colspan="4">Believe investigation results of Beijing police.</td></tr></table>

superedge. After inserting “leader” superedge, the proportion of rumor supporters obviously decreased, indicating that insertion strategy has a signi<sup>fi</sup>cant role in guiding online public opinion as shown in Fig. 7(a).

Parameter α re<sup>fl</sup>ects the in<sup>fl</sup>uence intensity of the “leader” superedge. When $\begin{array} { r } { \alpha \leq 0 . 5 , } \end{array}$ , with the increase of the in<sup>fl</sup>uence of the “leader” superedge, its guiding effect on online public opinion increases gradually. When $\alpha > 0 . 5 ,$ in<sup>fl</sup>uence of the “leader” superedge does not affect the guiding effect signi<sup>fi</sup>cantly as shown in Fig. 7(b).

Parameter β indicates the selection boundary of guiding objects that has a certain impact on intervention effect. Guiding effect on online public opinion of “leader” superedge only appears gradually after $\mathrm { \beta \geq 0 . 4 }$ . It indicates that the rumors should be guided properly in time, not to wait until all are rumor supporters as shown in Fig. 7(c).

Parameter γ characterizes the mutual in<sup>fl</sup>uence between ordinary superedges inside the supernetwork. Guiding effect of “leader” superedge on online public opinion enhances with the increasing of parameter γ as shown in Fig. 7(d).

## 5.3. Intervention effect of reconstruction strategy

Before the implementation of the reconstruction, the proportion of negative superedge remained unchanged at the beginning, and declined slightly later. After the implementation of the reconstruction, the proportion of negative superedge declined signi<sup>fi</sup>cantly, indicating that the reconstruction strategy has signi<sup>fi</sup>cant intervention effect on online public opinion as shown in Fig. 8(a).

Activation threshold has a negative correlation with public opinion environment, with coef<sup>fi</sup>cient λ. The activation threshold and intervention effect on public opinion decline as the increasing of λ. It illustrates that the spreading of public opinion has a strong dependence on the environment. So creating a mainstream public opinion environment can achieve desired intervention effect (Fig. 8(b)).

Attenuation radius of agent's impact represents how much distance in the surrounding neighborhood the reconstruction source agent can in<sup>fl</sup>uence. The higher the attenuation radius is, the more neighbors it can in<sup>fl</sup>uence. With the increase of attenuation radius, the intervention effect of reconstruction is signi<sup>fi</sup>cantly enhanced. This is because the contribution of the hub nodes in the network is much greater than ordinary nodes for the dissemination of information, showing a power law distribution. The more agents the reconstruction source affects, the more effective the intervention is. Therefore, using “two-step <sup>fl</sup>ow of communication” theory to cultivate positive opinion leaders and giving full play of their role to conduct public opinion intervention are feasible (Fig. 8(c)).

Intervention effect on public opinion is enhanced with the increasing of α and decreased with the increasing of β. It indicates that the stimulation of agent's psychology has signi<sup>fi</sup>cant impacts on public opinion. Opinion propagation process can be intervened in through psychological intervention. Intervention effect is more sensitive to the value change of β, indicating that positive psychology cultivation has better results than negative psychology counseling (Fig. 8(d) & (e)).

While calculating the value of public opinion K (t), we give positive viewpoints higher weights to indicate a positive public opinion aggregating <sup>fi</sup>eld. Giving negative viewpoints higher weights indicates negative public opinion aggregating <sup>fi</sup>eld. Giving positive and negative viewpoints equal weights indicates no apparent aggregating effect of agent's viewpoint. The results show that at the early stage of intervention implementation, there is no signi<sup>fi</sup>cant difference between intervention effect with a positive public opinion aggregating <sup>fi</sup>eld and the one without aggregating <sup>fi</sup>eld. But in the latter part of the intervention, intervention effect with a positive public opinion aggregating <sup>fi</sup>eld is signi<sup>fi</sup>cantly better. Intervention effect on public opinion with a negative public opinion aggregating <sup>fi</sup>eld is poor all the time. Thus, we can adjust the direction of aggregating effect of agent's viewpoint to create a positive public opinion <sup>fi</sup>eld in public opinion intervention (Fig. 8(f)).

![](/api/attachments/4RR7GX4H/fulltext/images/52674042360ce629afcd141a91a85082308197f6b90756fa5970974a1a7e7ea9.jpg)

![](/api/attachments/4RR7GX4H/fulltext/images/246b525ca1ee311047e6602fa956ec9d58f7c40641e67fba4dd7f6b4aea88ca8.jpg)  
Fig. 6. Intervention effect of isolation strategy.

![](/api/attachments/4RR7GX4H/fulltext/images/40116d919cacfc2b0530ed648450346816008d96c29ba30a571f9d09028630c4.jpg)

![](/api/attachments/4RR7GX4H/fulltext/images/a1e4c45a0b4288dc2678faf70ec73e2b5c09102f11c0b4f8f20ee744a7394c4a.jpg)  
Fig. 7. Intervention effect of insertion strategy.

## 5.4. Strategy selection

Take the average reduction ratio of negative public opinion (i.e. negative superedges) under the implementation of various intervention strategies as the evaluation criteria. Compare intervention effects of the three strategies and various sub-strategies to obtain Fig. 9. The results show that the effect of isolating elite superedges is optimal in isolation strategy, followed by isolating key superedges. Isolating ordinary superedges has the worst effect. In insertion strategy, the mutual in<sup>fl</sup>uence between ordinary superedges inside the supernetwork has the greatest contribution to the intervention effect. The in<sup>fl</sup>uence of the inserted leader superedge takes second place. The selection boundary of guiding objects contributes the least. In reconstruction strategy, adjusting aggregating effect of agent's viewpoint to create a positive <sup>fi</sup>eld has the greatest intervention effect. Attenuation radius of agent's impact takes second place. Activation threshold in opinion environment contributes less. Intervention effect of stimulation of agent's psychology is minimal.

Through the simulation experiments, we found that the linkage between the various components of the supernetwork is an important basis for public opinion intervention. Intervention effect of insertion strategy is superior to the other two. We believe it is because after isolating negative superedges, a substitute will appear to occupy the important position, playing the role of opinion leader. And therefore intervention effect of isolation strategy is not as signi<sup>fi</sup>cant as the one of inserting positive opinion leaders directly. Reconstruction strategy only optimizes the supernetwork structure, with highlighting the role of positive superedges, and weakening negative ones. But it neither deletes negative elements, nor adds positive ones. So the intervention effect is better than isolation strategy but inferior to insertion strategy on the whole. In insertion strategy, the mutual in<sup>fl</sup>uence between ordinary superedges inside the supernetwork has the greatest contribution to the intervention effect. Therefore, inserting positive superedges with strengthening the mutual in<sup>fl</sup>uence between ordinary superedges is the optimal intervention strategy.

## 6. Conclusion and future work

This paper made two important contributions to the study of online public opinion intervention. First, we both establish and validate a supernetwork model of opinion intervention, which includes four subnetworks — Social, Environmental, Psychological, and Viewpoint Subnetworks. And we incorporate it with dynamic simulations. Compared to the prior studies that use only dynamic models or dynamic models with single-layer networks, this paper is more consistent with the way that online public opinion evolves. Moreover, this model supports more detailed analyses about the impact of different driving forces on online public opinion. For instance, the previous studies have demonstrated that psychological statuses tend to impact agents [42]. Yet, knowledge that social relationships, environmental information, psychological statuses and viewpoint keywords are valid driving forces of online public opinion will reveal a more detailed picture about online public opinion. Recognition of the major driving forces of online public opinion provides researchers an opportunity to add depth to their analyses and highlight the signi<sup>fi</sup>cance of each of these factors for intervening in online public opinion.

![](/api/attachments/4RR7GX4H/fulltext/images/9daef5217457357ea969024108de9a205e4cb9fbf0943e873511d5e2b9a5f180.jpg)  
Fig. 8. Intervention effect of reconstruction strategy.

Second, this investigation contributes to the research of online public opinion intervention, by developing and validating three important strategies based on supernetwork model. These intervention models are shown reliable and valid, and are successfully applied to a picked rumor event. Intervention effects of different strategies and substrategies are compared. For this particular rumor event, we found that the insertion strategy, when combined with strengthening the mutual in<sup>fl</sup>uence within the supernetwork, is an optimal strategy.

The analysis of these strategies using supernetwork model can provide the government with a more comprehensive metric of online public opinion events. Such metric allows them to obtain a deeper understanding of the factors affecting netizens' willingness to spread rumors. Such understanding and our supernetwork model will help the government <sup>fi</sup>nd the keys to solve online public opinion crisis, and make strategic decisions to intervene in rumor spread.

![](/api/attachments/4RR7GX4H/fulltext/images/c67b8c5099f894bd51e39dace2a54a3841aaab890fb147da99f1d450513b4b1d.jpg)  
Fig. 9. Effect comparison of different intervention strategies.

This work provides a useful reference for theoretical studies of public opinion intervention from a quantitative perspective. In future study, more work can be done to improve our investigation. First, the strategies of isolating, inserting or reconstructing multiple superedges and their impacts on evolutionary mechanisms and intervention effects can be considered. Second, intervention mechanisms and effects of mixed strategies will be explored and studied. Third, we may extend the three strategies to other study <sup>fi</sup>elds, such as Electronic Commerce, and intellectual cooperation.

## Acknowledgments

This study was <sup>fi</sup>nancially supported by the National Natural Science Foundation of China (NSFC) (91024010, 91324009), Innovative Research Team Program of Chinese Academy of Sciences (KACX1-YW-1011), and Major Research Program of Institute of Policy and Management, Chinese Academy of Sciences (Y201201Z06).

## References

[1] Y.Z. Cheng, T. Xu, Q.K. Peng, W. Zhou, Opinion dynamics with the different community and individual characteristics, Journal of Systems Engineering 27 (4) (2012) 431–438.

[2] Y.Y. Zhao, G. Kou, Y. Peng, S.M. Li, On modeling and analysis of opinion formation with heterogeneous con<sup>fi</sup>dence levels for emergencies, Systems Engineering-Theory & Practice 32 (5) (2012) 971–976

[3] E. Ising, Beitrag zur theorie des ferromagnetismus, Zeitschrift fur Physik A: Hadrons and Nuclei 31 (1) (1925) 253–258.

[4] P. Clifford, A. Sudbury, A model for spatial con<sup>fl</sup>ict, Biometrika 60 (3) (1973) 581–588.

[5] K. Sznajd-Weron, J. Sznajd, Opinion evolution in closed community, International Journal of Modern Physics C 11 (6) (2000) 1157–1165.

[6] S. Galam, Majority rule, hierarchical structures and democratic totalitarianism: a statistical approach, Journal of Mathematical Psychology 30 (4) (1986) 426–434.

[7] S. Galam, Minority opinion spreading in random geometry, The European Physical Journal B-Condensed Matter and Complex Systems 25 (4) (2002) 403–406.

[8] S. Galam, Sociophysics: a review of Galam models, International Journal of Modern Physics C 19 (3) (2008) 409–440.

[9] B. Latané, The psychology of social impact, American Psychologist 36 (4) (1981) 343–356.

[10] G. Deffuant, D. Neau, F. Amblard, G. Weisbuch, Mixing beliefs among interacting agents, Advances in Complex Systems 3 (01n04) (2000) 87–98.

[11] G. Weisbuch, G. Deffuant, F. Amblard, J.P. Nadal, Meet, discuss, and segregate, Complexity 7 (3) (2002) 55–63

[12] R. Hegselmann, U. Krause, Opinion dynamics and bounded con<sup>fi</sup>dence models, analysis, and simulations, Journal of Arti<sup>fi</sup>cial Societies and Social Simulation 5 (3) (2002) 1–33.

[13] A.C.R. Martins, C.D. Kuba, The importance of disagreeing: contrarians and extremism in the CODA model, Advances in Complex Systems 13 (5) (2010) 621–634.

[14] A.C.R. Martins, Bayesian updating rules in continuous opinion dynamics models, Journal of Statistical Mechanics: Theory and Experiment 2009 (2) (2009) P02017.

[15] A.C.R. Martins, Continuous opinions and discrete actions in opinion dynamics problems, International Journal of Modern Physics C 19 (4) (2008) 617–624.

[16] A.C.R. Martins, Mobility and social network effects on extremist opinions, Physical Review E 78 (3)(2008) 036104

[17] A. Di Mare, V. Latora, Opinion formation models based on game theory, International Journal of Modern Physics C 18 (9) (2007) 1377–1395.

[18] L. Cao, X. Li, Mixed evolutionary strategies imply coexisting opinions on networks, Physical Review E 77 (1) (2008) 016108.

[19] A. Grabowski, Opinion formation in a social network: the role of human activity Physica A: Statistical Mechanics and its Applications 388 (6) (2009) 961–966.

[20] B.J. Prettejohn, M.J. Berryman, M.D. McDonnell, A model of the effects of authority on consensus formation in adaptive networks: impact on network topology and robustness, Physica A: Statistical Mechanics and its Applications 392 (4) (2013) 857–868.

[21] K. Kacperski, J.A. Hołyst, Phase transitions as a persistent feature of groups with leaders in models of opinion formation Physica A: Statistical Mechanics and its Applications 287 (3–4) (2000) 631–643.

[22] D.J. Watts, S.H. Strogatz, Collective dynamics of ‘small-world’ networks, Nature 393 (6684) (1998) 440–442.

[23] A.L. Barabási, R. Albert, Emergence of scaling in random networks, Science 286 (5439) (1999) 509–512.

[24] G. Weisbuch, Bounded con<sup>fi</sup>dence and social networks, The European Physical Journal B-Condensed Matter and Complex Systems 38 (2) (2004) 339–343.

[25] S. Fortunato, Damage spreading and opinion dynamics on scale-free networks, Physica A: Statistical Mechanics and its Applications 348 (2005) 683–690.

[26] M.H. He, D.M. Zhang, H.Y. Wang, X.G. Li, P.J. Fang, Public opinion evolution model with the variable topology structure based on scale free network, Acta Physica Sinica 59 (8) (2010) 5175–5181.

[27] P.J. Denning, The science of computing: supernetworks, American Scientist 73 (3) (1985) 225-227

[28] A. Nagurney, On the relationship between supply chain and transportation network equilibria: a supernetwork equivalence with computations, Transportation Research Part E: Logistics and Transportation Review 42 (4) (2006) 293–316

[29] T. Wakolbinger, A. Nagurney, Dynamic supernetworks for the integration of social networks and supply chains with electronic commerce: modeling and analysis of buyer–seller relationships with computations, NETNOMICS: Economic Research and Electronic Networking 6 (2) (2004) 153–185.

[30] E. Estrada, J.A. Rodríguez-Velázquez, Subgraph centrality and clustering in complex hyper-networks, Physica A: Statistical Mechanics and its Applications 364 (2006) 581–594.

[31] A. Nagurney, J. Dong, Management of knowledge intensive systems as supernetworks: modeling, analysis, computations, and applications, Mathematical and Computer Modelling 42 (3–4) (2005) 397–417.

[32] Y.J. Xi, Y.Z. Dang, K.J. Liao, Knowledge supernetwork model and its application in organizational knowledge systems, Journal of Management Sciences in China 12 (3) (2009) 12–21.

[33] Y.J. Liu, Q.Q. Li, R.Y. Tian, N. Ma, Formation and application of public opinion based on supernetwork analysis, Bulletin of the Chinese Academy of Sciences 28 (5) (2012) 560–568.

[34] Q.Q. Li, Y.J. Liu, Dynamical model of public opinion and its application based on supernetwork, Bulletin of the Chinese Academy of Sciences 28 (5) (2012) 569–577.

[35] R.Y. Tian, Y.J. Liu, Intervention of public opinion and its application based on supernetwork analysis, Bulletin of the Chinese Academy of Sciences 28 (5) (2012) 578–585.

[36] N. Ma, Y.J. Liu, Recognition of online opinion leaders based on supernetwork analysis, Bulletin of the Chinese Academy of Sciences 28 (5) (2012) 586–594.

[37] Y.J. Liu, Q.Q. Li, X.Y. Tang, N. Ma, R.Y. Tian, Superedge prediction: what opinions will be mined based on an opinion supernetwork model? Decision Support Systems 64 (2014) 118–129.

[38] N. Ma, Y.J. Liu, SuperedgeRank algorithm and its application in identifying opinion leader of online public opinion supernetwork, Expert Systems with Applications 41 (4) (2014) 1357–1368.

[39] E. Katz, P.F. Lazarsfeld, Personal In<sup>fl</sup>uence: The Part Played by People in the Flow of Mass Communications, Transaction Publishers, 1970.

[40] K.M. Carley, J. Diesner, J. Reminga, M. Tsvetovat, Toward an interoperable dynamic network analysis toolkit, Decision Support Systems 43 (4) (2007) 1324–1347.

[41] E. Noelle‐Neumann, The spiral of silence: a theory of public opinion, Journal of Communication 24 (2) (1974) 43–51.

[42] S. Galam, Collective beliefs versus individual in<sup>fl</sup>exibility: the unavoidable biases of a public debate, Physica A: Statistical Mechanics and its Applications 390 (17) (2011) 3036–3054.

![](/api/attachments/4RR7GX4H/fulltext/images/09c2b875c89423c159233ee8ed9ba180d7b3eeea73e01040d5f34ae80eaad9bc.jpg)  
Ru-Ya Tian works in Agricultural Information Institute of CAAS. She got her Ph.D. in Management of Science and Engineering from the Institute of Policy and Management of Chinese Academy of Sciences, and her research interests include opinion dynamics and complex networks

![](/api/attachments/4RR7GX4H/fulltext/images/34eb3e53f633280f201c1864f58fe73ece943dffa993288e4ef6c04f46480e76.jpg)

Yi-Jun Liu is an associate research fellow of Institute of Polic and Management of Chinese Academy of Sciences. Her research includes opinion dynamics, complex networks and sustainable development strategies.
