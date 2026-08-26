---
otero_id: 10768
otero_key: "S74E8RBH"
title: "Including social factors in an argumentative model for Group Decision Support Systems"
authors: "Juan A. Recio-García; Lara Quijano; Belen Díaz-Agudo"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.05.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Including social factors in an argumentative model for Group Decision Support Systems ☆

Juan A. Recio-García ⁎, Lara Quijano, Belen Díaz-Agudo

School of Computing, Complutense University of Madrid, Spain

## a r t i c l e i n f o

Article history: Received 20 January 2012 Received in revised form 28 November 2012 Accepted 9 May 2013 Available online xxxx

Keywords: Decision Support Systems Negotiation Support Systems Personality Social networks Trust Multi-agent systems

## a b s t r a c t

In this paper we propose a Decision Support System for groups of people where each user delegates to an agent that represents her preferences and argues with other agents to obtain the best alternative for the whole group. The novelties of our approach are the inclusion of users' social factors, personality and trust, in the argumentation process and the negotiation system, plus a multi-agent architecture that represents the social connections within the group. Therefore, our model simulates the argumentations made by real users to agree on a concrete product in a very accurate way. As a case study, we have tested our theories in the movie recommendation domain with real social networks. We have concluded that distributed models and argumentation techniques including personality and social trust improve the satisfaction of users involved in a group decision making process.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

A decision is a choice among alternatives based on estimated values for these alternatives. Supporting a decision means helping people to work alone or in groups to gather information, generate alternatives and make decisions. A decision making process also involves the estimation, evaluation and comparison of alternatives. Our work presented in this paper consists of providing a new method to evaluate users' estimation of different products and supporting decision making processes by providing a group recommendation for these products.

Our goal is to get an accurate reproduction of the decision making processes run by real groups of people when deciding leisure activities. There are some types of items, like restaurants, movies or trips that people tend to enjoy together. These kinds of items have a very relevant commercial interest, so it is kind of a natural thing to make the most accurate recommendations to groups of people. Existing approaches on Group Decision Support Systems (GDSS) are typically based on the aggregation of the preferences of group members, where every person in the group is considered equal to the others [7,18]. Other group decision approaches have solved the con<sup>fl</sup>ict by trying to maximize the preferences of the greatest number of group members [20]. But none of these approaches have into account that different groups of people have very different characteristics that strongly affect the decision process: size, social strength and in<sup>fl</sup>uence between group members, personal preferences, personality of the group members, etc. It is a fact that when we face a situation where people's concerns don't match, con<sup>fl</sup>ict arises. Therefore, the general satisfaction of the group is not always the aggregation of the satisfaction of its members, as different people have different expectations and behavior in con-<sup>fl</sup>ict situations. This fact is taken into account in recent works that agree on the need to adapt the decision making process to the group composition [15,19]. Furthermore, it is also well-known that user preferences can be affected by the rest of the group [6,19].

Our recent work [24] involves the improvement of current group recommendation techniques by introducing two novel factors: the personality of each individual and the trust among users. We have also presented some experiments where we test our theories for recommending products to groups of people connected through social network structures. In our model, we support the process of decision making by taking into account the group personality composition and the social connections among the individuals of the group. Once the relevance of these factors has been validated, in this paper we propose integrating them into a novel approach for group decision making based on a multi-agent system that accurately reproduces real argumentation processes made by real users. In the network of agents every agent should be able to de<sup>fi</sup>ne the trustworthiness regarding the connected agents [12,14] and to re<sup>fl</sup>ect the personality of the user it is representing. Our model is based on the idea of taking into account the social connections of the collaborative agents, including the level of trust of the agent they collaborate with [11,21,32].

Therefore, this paper presents a software architecture where each user delegates to an agent that represents her in the argumentation process.

This way, users are freed from holding the typical annoying discussions to agree on a common decision for the group [30]. Another relevant advantage of this architecture is its perfect integration into existing social networks like Facebook or Google+.

Finally, we describe a case study for a collaborative movie recommender system and we present the results of an experiment where we measure the accuracy of the system results using argumentation protocols and a network topology based on a real social network.

Summarizing, this paper presents our research on GDSS by reproducing the real social organization of the group and including deliberation capabilities. Our main contribution is to improve group decisions by moving to a distributed model with social network topologies, introducing social factors, like personality and trust, plus an argumentation process that enables users to argue and defend their opinions by means of delegation to agents.

The paper runs as follows: Section 2 presents our approach for distributed GDSS and how to obtain the personality and trust factors to be integrated in this kind of systems. The distributed models and argumentation processes are explained in Section 3. Section 4 describes a case study of our method in the movie recommendation domain using data extracted from real social networks. Section 5 presents the results of our experiments. Finally, the conclusions and main lines of future work are explained in Section 6.

## 2. Distributed Group Decision Support Systems

Our approach to solving decision support problems is rooted in the Case-Based Reasoning <sup>fi</sup>eld [1]. Case-Based Reasoning (CBR) is based on the intuition that similar problems tend to recur. It means that new problems are often similar to previously encountered problems and, therefore, that past solutions may be of use in the current situation [17]. When a CBR system faces the resolution of a new problem, it will search in its case base for problems similar to the current one. Once it <sup>fi</sup>nds them, these previous cases will be adapted to the current problem in order to provide a valid answer. The analogies between CBR and Decision Support Systems (DSS) are manifold. In DSS users manage a memory of preferences that must be similar to the alternative chosen by the group. Once the best alternative is obtained it is proposed directly to the user without requiring adaptation. Moreover, both techniques pay signi<sup>fi</sup>cant attention to the learning processes that improve system performance by taking into account user knowledge (the preferences or experiences of the users).

Brehmer [5] describes a distributed decision making system as an environment that (a) enables cooperation from a number of decision makers, where (b) each decision maker owns part of the resources needed to solve the problem; and (c) no decision maker has a complete overview of the problem as a whole. This schema <sup>fi</sup>ts perfectly in several works in distributed CBR that assume multi-case-base architectures involving multiple processing agents differing in their working memory [22]. In this kind of systems, each agent manages its own memory of preferences that make up its partial view of the world. To solve a given problem, this knowledge must be shared to obtain a solution for the whole group. This way we can reuse the existing research on distributed CBR in the GDSS <sup>fi</sup>eld. CBR literature proposes several ways to combine different experiences to obtain improved solutions in distributed architectures. One important methodology is the ensemble effect, explained in [23], which proves that the argumentation of two agents improves the results obtained by one only agent working with the same experiences. This conclusion was the precursor of a research line focused on <sup>fi</sup>nding the best argumentation protocols to allow CBR agents to discuss a common problem. In [23] they came up with the AMAL protocol, which enables several CBR agents to argue about a common problem by means of arguments and counterarguments. This protocol and its adaptation to our model are presented in Section 3.

Setting aside the distributed architecture, when moving from individual to GDSS, the main issue that arises is how to <sup>fi</sup>nd an alternative that satis<sup>fi</sup>es the greatest number of group members, while taking into account the preferences of the decision makers. Several GDSS propose the generation of an aggregated preference built with individual user preferences [4,31]. However, our approach to group decision support is completely different because it simulates the argumentation process of a group of users by using a distributed architecture instead of providing an aggregated estimation. This way, we try to reproduce – in an accurate way – the real argumentation process carried out by decision makers when reaching an agreement. Moreover, to reproduce these argumentations accurately in our model we include two factors that re<sup>fl</sup>ect the real (or human) behavior of users. These factors – described in following subsections – are personality and social trust.

## 2.1. Personality estimation for Group Decision Support Systems

Usually, works in GDSS consider the preferences of every member of the group to have the same degree of importance and try to satisfy the preferences of every group member. However, groups of people can have very different characteristics and can be made of people with similar or antagonistic personal preferences. It is a fact that when we face a situation in which the concerns of people appear to be incompatible a conflict situation arises.

Our approach determines that the general satisfaction of the group is not always the aggregation of the satisfaction of its members, as different people have different expectations and behavior in con<sup>fl</sup>ict situations that should be taken into account. In [24] we presented a method for group decision support where we distinguish between different types of individuals in a group. Our research characterizes people using the Thomas–Kilmann Con<sup>fl</sup>ict Mode Instrument (TKI) [29]. From the answers to the TKI test we compute a value $p _ { u } \in [ 0 , 1 ]$ that represents the personality as user u; 0 being the re<sup>fl</sup>ection of a very cooperative person and 1 the re<sup>fl</sup>ection of a very sel<sup>fi</sup>sh one. Our method takes this value into account by studying how group personality composition in<sup>fl</sup>uences the decision making process for the group, and how performance is improved for certain types of groups when compared to different simple group preference aggregation algorithms.

In this paper we present some experiments where we include the impact that personality will have on the argumentation process when two users u and v are arguing. This factor is computed as the personality difference:

$$
\Delta p _ {u, v} = p _ {u} - p _ {v}
$$

where $p _ { u }$ and $p _ { \nu }$ are the values that re<sup>fl</sup>ect the personality of users u and v respectively. Note that $\Delta p _ { u , \nu } \in [ - 1 , 1 ]$

As we detail in Section 3, we propose to use the personality difference value to con<sup>fi</sup>gure the behavior of each agent in the distributed architecture. This factor will be integrated into the group decision making process together with another feature: trust among agents. This second factor is detailed next.

## 2.2. Social trust and network topologies in GDSS

In today's networked worlds, uncertainty and anonymity are important factors that have strong implications in decision-making. Several researchers have therefore proposed to incorporate the concept of interpersonal trust in Group Decision Support Systems [27,28,32]. This factor is even more important when we are performing a group decision making process where users have to agree on an alternative for the whole group. This kind of process usually follows an argumentation schema where each user defends her preferences and rebuts others' opinions. Here, trust among users is the major factor when users must change their mind to reach a common decision.

A promising approach is to collect trust knowledge from existing social networks like Facebook, Twitter, Google+, among others.

The use of social networks and trust when building a DSS system is not new. Generally, trust is employed as a way to give more weight to some users, to compute users' similarity, or to sort and <sup>fi</sup>lter the alternatives by giving priority to trusted sources. It has been employed in different domains like movie recommendation, e-mail <sup>fi</sup>ltering [9] or ski mountaineering [2].

In our approach, we propose the use of social network topologies to re<sup>fl</sup>ect the interactions of the users within the group. We think that, by reproducing this structure, the decision making process will be a realistic reproduction of the argumentations that take place in a group and, consequently, the results will be more accurate. This organization of the users can easily be obtained from current social networks or built ad-hoc for a GDSS application. However, a very promising option is to include the system in the social network as it will easily exploit the information in the network [26]. That is one of the reasons for the use of a multi-agent architecture where each agent is linked to the user pro<sup>fi</sup>le.

Our working hypothesis is that this new organization of the structure of the group will affect and improve the result of the decision making process, mainly because with the social network topology we give a more realistic structure and organization to the group, which is closer to how the argumentations would take place in a real group when they argue about which alternative to choose. For a given group of users, we sketch a network where each node represents a person and each connection represents that the particular person has a relation with the one he is connected to. If two nodes are not connected, it means that the people they are representing don't know each other or that they are not close. When each node generates its preferences, it will consider only the information provided by the nodes that it is connected to, representing those that could have in<sup>fl</sup>uenced its decision in real life. In this way we use social network topologies to evaluate social trust, as it is re<sup>fl</sup>ected in our trust function, explained in Section 4.

Moreover, we have studied what the most important factors are in the social networks that must be taken into account when computing trust between users. Examples of these factors are: the number of shared messages, common pictures, direct friends, etc. To perform this task we have reviewed several existing works [8,10] and selected the most relevant and feasible factors. We have chosen 10 factors that are combined to get a <sup>fi</sup>nal trust value. Furthermore, we have evaluated which factors have the highest impact in the decision making process. The speci<sup>fi</sup>c trust factors are:

$f _ { 1 } ( u , v )$ : Distance in the social network.

$f _ { 2 } ( u , v )$ : Number of common friends.

$f _ { 3 } ( u , v )$ : Intensity of the relationship: how often they write each other on their walls.

$f _ { 4 } ( u , v ) { \colon }$ : Intimacy of the relationship: We classify relationships by <sup>fi</sup>nding keywords that represent different intimacy levels.

$f _ { 5 } ( u , v )$ : Duration: how long they know each other.

$f _ { 6 } ( u , v )$ : Reciprocal services: number of posted videos/songs/webs, shared games/applications.

$f _ { 7 } ( u , v )$ : Structural variable: common interests described in the users pro<sup>fi</sup>le like movies, books, or general interests.

$f _ { 8 } ( u , v )$ : Social distance: how many of the following properties are shared: political, educational, religious and demographical information.

$f _ { 9 } ( u , v ) { \colon }$ Status: value depending on the kind of status: couple, family, best friends, etc.

$f _ { 1 0 } ( u , v )$ : Pictures: percentage of pictures where they appear together.

The <sup>fi</sup>nal trust value $t _ { u , \nu }$ is a weighted average of the previously described factors:

$$
t _ {u, v} = \sum_ {i = 1} ^ {1 0} \alpha_ {i} \cdot f _ {i} (u, v).\tag{1}
$$

Note that $t _ { u , v } \in [ 0 , 1 ] .$ . We have measured the importance of every factor $\alpha _ { i }$ by using an experimental approach. Results are reported in Section 4.

In the following section we describe the distributed model to carry out our group decision making theories.

## 3. Distributed argumentative model for Group Decision Making processes

Up to this point we have described the two social factors of our approach, the one related to personality and the one related to social networks and trust among group members. Now we are going to introduce the distributed architecture that imitates the social network connections for the group decision making process. The main goal is to improve decision making by taking into account the friendship topology (who is whose friend), the group personality composition and trust between group members. To include these three features in our model we de<sup>fi</sup>ne a multi-agent architecture following a social network topology, where each agent represents a member of the group. One of the main advantages of using distributed models is that the agents representing members of the group do not necessarily have to be stored in the same machine. This way each user can have one agent representing her preferences and arguing for her best interests in her computer.

In our architecture each agent discusses with all its neighbors in the network and the <sup>fi</sup>nal decision will depend on the personality and trust the users being represented have with each other. When two agents are not connected, it means that the users they are representing don't know each other or they're not close. Therefore there won't be any kind of argumentation between them. However if two agents are connected, associated users that have some level of interpersonal trust, our model simulates a face to face discussion. This model improves the typical “fully connected” network topologies where every agent debates with every agent. We think that the “fully connected” topology is an arti<sup>fi</sup>cial representation of the group and does not re<sup>fl</sup>ect real interactions among users. Fig. 1 shows the differences between the two alternatives in the topology of the network, the “fully connected” network topology and the social network topology.

Once we have described the distributed model to be built we need the infrastructure to implement it. We use D<sup>2</sup>ISCO to implement the process of argumentation and the distributed architecture. This framework is described next in Section 3.1. It uses a reasoning protocol (fully detailed in Section 3.2) that begins with an agent issuing a query to the agents that it is linked to. Each agent will provide its individual local solution for the problem, this is, its favorite alternative for a given query. At each round the agents can rebut the solution made by its neighbor agents. These different counterexamples will have different weights depending on the personality and trust among the people who are being represented by the agents.

Finally they provide a consensual solution which will be the individual local solution of the agent that threw the query to them. This process keeps going backwards until it reaches the agent that threw the initial query. Next we will detail the argumentation processes between agents in D<sup>2</sup>ISCO.

![](/api/attachments/S74E8RBH/fulltext/images/a58fb895b0fed7fcfce0cede07e730b1bfc92b5621e4b88cbb02c63a7525b7fc.jpg)

![](/api/attachments/S74E8RBH/fulltext/images/6c17b98f6a532372bc7659d239a500dc78ce65b9b93d301404c5aad3888446e4.jpg)  
Fig. 1. a) “Fully connected” network topology. b) Social network topology.

## 3.1. D<sup>2</sup>ISCO: distributed reasoning for collective experiences

D<sup>2</sup>ISCO<sup>1</sup> is a platform for the design and implementation of deliberative and collaborative CBR applications. Using $D ^ { 2 } I S C O \left[ 1 3 \right]$ we can develop distributed decision making systems where each agent collaborates, argues and counterargues its local results with other agents in order to improve the global response of the system.

Essentially, this platform consists of the creation of a practical framework for the characterization of distributed argumentative systems. It implements a modi<sup>fi</sup>cation of the AMAL argumentation protocol that can be applied to different types of distributed systems. This protocol de-<sup>fi</sup>nes the way of exchanging arguments and counterarguments between agents. In the original AMAL protocol [23] these arguments are generated using a Description Logics system. However we follow a different approach to generate the arguments: a fuzzy reasoning system. Besides, it includes learning mechanisms to infer the trust models of the distributed CBR systems. $D ^ { 2 } I S C O$ performs a practical demonstration of the following aspects (discussed in [13]): (a) The network topology signi<sup>fi</sup>cantly in<sup>fl</sup>uences the results for the distributed CBR systems. (b) Social networks provide a network topology and a trust model that improves the results obtained. (c) The use of argumentations in the different reasoning processes improves the accuracy of the system.

Next, we will describe the argumentation protocol based on AMAL and the fuzzy decision system that generates the argumentations in our proposal.

## 3.2. Argumentation model for simulating decision making processes

Our proposal allows a group of agents $\{ A _ { 1 } , \dots , A _ { n } \}$ to deliberate about the correct solution to a problem Q by means of an argumentation process, re<sup>fi</sup>ned with a fuzzy decision system that takes into account the personality of each user in the system and the trust they have with each other.

When the argumentation process starts, each agent uses its own internal memory to <sup>fi</sup>nd a solution for a given query Q and then they begin a deliberation process with other agents by means of counterarguments. This also allows the agents to learn from the counterexamples received from other agents. The reasoning protocol begins with an agent $( A _ { q } )$ issuing a query to the agents that it is linked to. Each one of these agents retrieves k solutions from its own memory. Then, an argumentation process consisting of k cycles is performed to defend and discard the proposed solutions by means of counterexamples. When the process <sup>fi</sup>nishes $A _ { q }$ receives at most k trusted solutions.<sup>2</sup>

Our argumentation and solution retrieval process is hierarchical. When solving a problem Q, the agent that issues the query $A _ { q }$ becomes the root of the whole hierarchy of agents, de<sup>fi</sup>ned by the structure of the social network. Then, the query is propagated to the leaves of the tree and the retrieval of the solution follows an inverse path. The leaves of the tree deliberate with their immediate parent node $A _ { p } ,$ which organizes the reasoning. When this intermediate deliberation <sup>fi</sup>nishes, $A _ { p }$ participates in the deliberation organized by its parent node but this time it takes on the role of a child node $A _ { c } .$ This behavior is repeated until reaching the root $A _ { q } .$ Therefore, the distributed reasoning process <sup>fi</sup>nishes with agent $A _ { q }$ obtaining a list of agreed-on solutions ranked with a goodness value.

The method consists of a series of rounds. In the initial round, each agent states what its individual local solution for the problem Q is. Then, during each round an agent can try to rebut the solution or prediction made by any of the other agents by giving a counterexample. When an agent receives a counterargument or counterexample, it informs the other agents if it accepts the counterargument or not. Moreover, agents also have the opportunity to answer counterarguments by trying to generate a defense from the counterargument.

More speci<sup>fi</sup>cally, the argumentation process is directed by the parent node/agent $A _ { p } ,$ , which issues the query and organizes the deliberation of its child nodes (A ). The agent that leads the argumentation $\left( A _ { p } \right)$ plays an important role in the decision making process because it de<sup>fi</sup>nes the con-<sup>fi</sup>dence in the agents involved in the argumentation, and decides if a counterexample is accepted or rejected based on (a) its con<sup>fi</sup>dence in the agents involved, (b) the goodness value of their items, (c) her own personality and (d) the personality of the other agents involved. This process follows a peer-to-peer schema where the lead agent $A _ { p }$ deliberates with each child agent A individually. After every peer-to-peer deliberation $A _ { p }$ keeps the best item that has agreed with $A _ { c } .$ . Then it will deliberate again with the following child agent and so on.

When a child agent A representing user u proposes a solution i to the parent agent $A _ { p }$ (representing user v), this solution is rated with a value $g _ { u , i }$ that represents its goodness value according to the preferences and partial knowledge of user u. In DSS this measure of goodness is usually based on the estimation of an agent's/user's preferences. This estimation can be obtained by applying similarity metrics developed in the Case-Based Reasoning domain. In our case, this preference is a rating that denotes the preference of the user u for a given item i and is referred to as rating(u,i). Next we will study how to compute the goodness value by means of a fuzzy system that combines these estimations. Then, the following subsection presents our novel method to modify this value according to the personality and trust of the users.

A counterexample against a solution i is another solution $i _ { c e } ,$ which is rather similar to i but it has a low value of goodness. An agent $A _ { p }$ representing user v will present a counterexample when another agent A proposes a solution i that does not suit the preferences of v. The counterexample $i _ { c e } ,$ is a solution from the memory of $A _ { p }$ that demonstrates that the solution i is not good because both are similar but the counterexample has a low value of goodness. A defense against a counterexample $i _ { c e }$ is another solution i that is rather similar to $i _ { c e }$ and it has a high value of goodness. Here, the defense $i _ { d }$ is presented by the same user that proposed the initial solution.

A key feature of the distributed reasoning protocol described above is the decision system that rates, accepts or rejects proposed solutions, arguments, counter-arguments and defenses. Our proposal relies on a fuzzy reasoner [33] that is able to <sup>fi</sup>nd counterexamples that cannot be generated by logical induction. We have chosen this technique because it allows us to perform deliberations about incomplete preference memories and eliminates the restrictions that appear when using descriptive logics (used in the original AMAL protocol). The details of fuzzy reasoner are described in [13]. Next we will show how to include the personality and trust factors to improve the ratings given to a product by an agent.

## 3.3. Including personality and trust in the argumentation process

Each agent A representing the user u that receives a query must return a proposed solution i to the lead agent $A _ { p }$ that represents user v. This solution is the best one found in the memory of user u rated with a value $g _ { u , i }$ that re<sup>fl</sup>ects its goodness. As we have previously explained this value is obtained by means of a fuzzy system that combines both the similarity value of the query with that product and the rating given by the user according to the partial knowledge of the domain stored in the memory of the user (referred to as rating(u,i)). To compute both values we apply similarity metrics taken from the CBR domain.

However, we have enhanced this rating value with the social factors described in Sections 2.1 and 2.2: personality and trust. As we stated before, these factors will boost the performance of the group recommender as they represent the real features of human deliberations more accurately.

Our method modi<sup>fi</sup>es the rating value according to the difference in personalities between users u and v. If the lead user v has a strong personality it won't easily accept the solution proposed by u. Therefore we increment or decrement the goodness value according to the difference in personalities. Moreover, the trust $t _ { u , \nu }$ between the two users must be taken into account when computing the rating value: a low trust value implies a low goodness. Therefore, we obtain a modi<sup>fi</sup>ed goodness value $g ^ { \prime } { } _ { u , i }$ computed as follows:

$$
g _ {u, i} ^ {\prime} = t _ {u v} \cdot \left(g _ {u, i} + \Delta p _ {u, v}\right)\tag{2}
$$

where $\Delta p _ { u , \nu }$ is the personality difference between users, and $t _ { u , \nu }$ is the trust that exists between users u and $\nu . g _ { ( u , i ) }$ is the goodness value for the solution i given by user u and computed by means of the fuzzy system.<sup>3</sup>

With this formula we modify the goodness value estimated for every user and item. It will be higher when the personality and trust parameters are also high, and lower in the opposite case. Therefore, the argumentation process presented before uses the $g ^ { \prime } { } _ { u , i }$ value instead of the original $g _ { u , i }$ goodness to include the social factors in the group decision making process.

Once the distributed argumentation protocol is described, next we describe how to apply it in a real case study.

## 4. Case study: movie recommendation

To evaluate our GDSS methodology we have chosen the recommendation domain because it is a clear example of GDSS systems. Moreover, movie recommendation is a very accessible area with datasets available and, more importantly, well known to users. The main hypotheses to validate are:

H1. The multi-agent architecture of deliberative agents connected according to a real social network improves the accuracy of standard “fully connected” group recommenders.

H2. The personality and trust factors improve the performance of distributed group recommenders.

H3. Individual satisfaction increases when using this new group recommendation technique because agents are able to argue about the item chosen.

Following sections detail the case study used to demonstrate the hypotheses formulated. Next we describe the experimental set-up, followed by the results.

## 4.1. Experimental set-up

In order to perform our experiment in the movie recommendation domain, we created two events in two different social networks, Facebook<sup>4</sup> and Tuenti.<sup>5</sup> In these events we asked 58 participants to complete three questionnaires.<sup>6</sup>

The <sup>fi</sup>rst questionnaire obtains the individual preferences of the user about cinema. Users have to evaluate 50 heterogeneous movies from the MovieLens data set [3] (rating them using a Likert scale from 0.0 to 5.0). On average, each user rated 30 movies. These movies rated make up the list of products that is assigned to each agent as the pro<sup>fi</sup>le of each participant, that is, the memory of preferences. Next, a second test asks users to choose their 3 favorite movies from a list of 15 recent movies (chosen heterogeneously from movies in the MovieLens database), that represents a movie listing from a cinema. These movies are the ones they would actually like to watch or had enjoyed best, and are denoted as their individual favorites set. $\mathrm { i f } _ { u } .$

To measure the accuracy of the group recommendation we created groups with our participants and we asked them to simulate that they were going to the cinema together. We provided them with the 15 movies that represented our movie listing in the second questionnaire and we asked them to choose which 3 movies they would actually watch together. We managed to gather 15 groups of 9, 5 or 3 members. The three movies chosen by each group G are stored as the real group favorites set, rgf . This way, to evaluate the accuracy of our recommender we were able to compare the set proposed by the recommender – the gf set – with the real preferences $\operatorname { r g f } _ { G }$ . Particularly, we measure the number of movies in $\mathrm { g f } _ { G }$ that are also in $\operatorname { r g f } _ { G } .$ . The concrete evaluation measures used to compare the two sets are detailed in Section 4.2.

Once we have the memory of preferences for each user, we need the personality and trust factors. A third questionnaire serves to obtain the personality value, $p _ { u } ,$ by asking the 30 questions from the TKI personality test [29]. Next, trust among users is calculated by analysing the factors explained in Section 2.2. These factors are combined using a weighted average, see Eq. (1), whose weights are obtained through a genetic algorithm (GA). Our GA manages a population of vectors of weights α . These vectors are combined and mutated in order to maximize a <sup>fi</sup>tness function. Therefore, the individuals of the GA population (vectors of weights) are used to compute the trust factor $t _ { u , \nu }$ required by the approach. The <sup>fi</sup>tness function compares the result of our group recommender con<sup>fi</sup>gured with each individual α to the real rating given by the users. These weights are shown in Fig. 2 where we can observe that common friends, pictures, interests and friendship duration are the most relevant factors.

Next step is the con<sup>fi</sup>guration of the multi-agent system. As we have previously detailed every agent is connected to others according to the real relationships of the represented user in a real social network. Therefore, we create an agent for each user that is linked to the real friends of the user.

Finally, every agent requires an individual movie recommender to <sup>fi</sup>nd suitable movies for a given query. These recommenders return the rating value rating(u,i) described in Section 3.3. To obtain this value we use CBR similarity metrics applied to the products and ratings in the memory of user preferences. The individual recommender implemented follows a knowledge based approach [16] that compares descriptions of the products and returns a collection composed of the ones most similar to the query.

## 4.2. Evaluation metrics

The aim of the evaluation is to compare the results of our recommender system to the real preferences of the users (that is, what would happen in a real life situation). This evaluation has some particular features that must be taken into account. First, we are not interested in a long list of ordered movies when estimating the movies a user or group should watch. Real users are only interested in a few movies they really want to watch. This fact discards several evaluation metrics that compare the ordering of the items in the real list of favorite movies and the estimated one. On the other hand, the number of relevant and retrieved items in our system is <sup>fi</sup>xed. Therefore, we cannot use general measures like recall or precision. However, there are some metrics used in the Information Extraction <sup>fi</sup>eld that limit the set retrieved. This is the case of the precision@n measure, which computes the precision after n items have been retrieved. In our case, we can use the precision@3 to evaluate how many of the movies in gf are in the rgf set (note that $| \mathrm { r g f } _ { G } | = 3 )$ . This kind of evaluation can be seen from a different point of view: we are usually interested in having at least one of the movies from gf in the rgf set. This measure is called success@n (or s@n) and returns 1 if there is at least one hit in the <sup>fi</sup>rst n positions. Therefore, we could use s@3 to evaluate our system by computing the rate of recommendations where we have at least “one-hit” in the real group favorites list. For example, a 90% accuracy using s@3 means that the recommender suggests at least one correct movie for 90% of the groups evaluated. In fact, s@3 is equivalent to having precision@3 1/3. We can also de<sup>fi</sup>ne a “two-hits” metric or doublesucess@3 (2s@3), equivalent to precision@3 ≥ 2/3, which represents the number of times the estimated favorites list gf contains at least two movies from rgf . Obviously, it is much more dif<sup>fi</sup>cult to achieve high results using this second measure.

![](/api/attachments/S74E8RBH/fulltext/images/5970315f6cf91b4cc7aae670ec040359a153ee417ed8641ee6a6fd74bb15de19.jpg)  
Fig. 2. Weights to obtain the trust value.

## 5. Discussion of the evaluation results

Given the three hypotheses we want to validate, and the experimental setup, in this section we discuss the obtained results. We have compared the proposed distributed model to a standard “fully connected” group recommender to prove H1. Global results are shown in Fig. 3. As we can observe in the two <sup>fi</sup>rst columns of the <sup>fi</sup>gure, the two approaches are similar if we use the s@3 measure, the standard model being slightly better by 3%. However, if we evaluate using the more demanding 2s@3 metric we obtain an improvement of 17%. Therefore we can con<sup>fi</sup>rm the <sup>fi</sup>rst hypothesis and assert that the social network organization of the agents improves the performance of the system.

Next, we studied the accuracy of our proposal regarding group size. Fig. 4 shows the results of our experiment for the three different group sizes. Here we are using the personality and trust factors plus deliberation capabilities with a social network topology. The s@3 line shows how many times our group recommender provided one product within its <sup>fi</sup>rst three choices that the group would really have selected. And the 2s@3 shows the number of times that the group recommender provided two products that the group would have really selected. This last measure is therefore much more dif<sup>fi</sup>cult to obtain so the percentage is always lower. By studying the size of the groups we can observe that generally the recommender gives better results for smaller groups.

The second hypothesis to be tested (H2) is that social factors improve the performance of our distributed recommender. To con<sup>fi</sup>rm it we repeated the experiments using the original goodness value $g _ { u , i }$ instead of the modi<sup>fi</sup>ed versiong ${ \bf \chi } _ { u , i } ^ { \prime } ,$ shown in Eq. (2), which includes the personality and trust parameters. The results obtained are reported in the last column in Fig. 3, where we can observe a poorer performance particularly in the 2s@3 metric.

Furthermore, we wanted to check that the improvement achieved when using social factors is due to the argumentation protocol that takes them into account when <sup>fi</sup>nding the best alternative for the group. That is, there is no correlation between the performance and the social characterization of the groups being evaluated. To discard this lack of correlation we described the groups regarding the average and standard deviation of the trust and personality values of their members. The average values let us measure if a group is mostly composed of members with a high/low personality or trust; meanwhile the standard deviation re<sup>fl</sup>ects the homogeneity of the group regarding the two parameters. After running several statistical tests we found no evidence of correlation between these variables and the performance of the system (evaluated using the precision@3 metric that summarizes s@3 and 2@3<sup>7</sup>). The resulting correlation matrix is shown in Fig. 5. As we can observe, there is no correlation at all between the variables studied. Therefore we can conclude that the improvement in performance is rooted in the appropriate combination of social factors carried out by the argumentation protocol.

![](/api/attachments/S74E8RBH/fulltext/images/64956338a364e5c6608137e0cbe53e1d7fc8b4d4cf16a14d2f68f74e952cb9ae.jpg)  
Fig. 3. Comparison of the global results. Standard vs. distributed model.

Finally we are very interested in each user's individual satisfaction. Our hypothesis (H3) is that users' preferences are taken more into account by our model because the deliberation process lets them argue about and rebut the product to be chosen by the group. Therefore, their individual satisfaction should be higher.

Individual satisfaction is measured by comparing how many movies proposed by the group recommender – gf – are in the user's list of favorite movies – $\cdot \mathrm { i f } _ { u } \cdot $ obtained by means of the third questionnaire. When comparing our distributed model with the standard model we found an increase of 5% in the average satisfaction of the users. Our explanation for this result is that the argumentation method enables users to express their opinions more clearly. For example, if they specially dislike one movie and it is proposed by another agent during the deliberation process, the representing agent can state its dislike in the rounds of argumentation and counter-argumentation.

The experimental validation of our hypothesis represents a valuable contribution to the Group Decision Support Systems <sup>fi</sup>eld as they con<sup>fi</sup>rm the utility of exploiting social network structures to integrate social knowledge in the decision making process. Moreover we propose multi-agent systems as a suitable architecture to implement such decision systems. We also have probed that trust and personality are two social factors that help to obtain an accurate reproduction of the decision making processes run by real groups of people. The inclusion of these factors in GDSS increases the individual satisfaction of the users involved in the group decision making process, and this fact should be taken into account when designing this kind of systems.

## 6. Conclusions and future work

Group Decision Support Systems represent a wide range of appli cations with rising impact in the current web [25,32]. Moreover, the need for systems capable of providing decision support for groups of people is attracting more interest as there are many leisure activities that are carried out in groups and organized through social networks. Therefore, we propose a novel approach for GDSS based on a distributed architecture of agents with deliberation capabilities that argue and defend the preferences of the represented user to reach a joint solution. This architecture exploits social information available in social networks, like the topology of user relationships and their mutual trust to improve the performance of the system. Moreover, our model includes the personality of each member of the group to re<sup>fl</sup>ect real argumentation processes accurately.

![](/api/attachments/S74E8RBH/fulltext/images/43cdcdf98ff981913bca0f54df51ce28b5fb5d54a6a8dbeec18fbc63e2ae1d34.jpg)  
Fig. 4. Comparison of the results obtained using distributed models plus the personality and trust factors for the 3 different sizes of groups.

The personality factor re<sup>fl</sup>ects the cooperativeness or sel<sup>fi</sup>shness of each user when selecting a product for the whole group. It measures the degree of acceptance of the products proposed by other users and the way to solve con<sup>fl</sup>icts. To obtain this factor we use a popular personality test called TKI [29]. The second factor used by our model is trust among users. Several studies point out the importance of personal trust in real argumentations and the requirement to include this feature in software models reproducing those processes [9,27]. We measure social trust among users by analysing several features found in common social networks. Examples of these social factors are distance in the social network, number of common friends, intensity, intimacy or duration of the relationship.

Both parameters, personality and trust, are used to customize the argumentation processes performed by the agents. However, the most important novelty of this paper is the organization of these agents according to users' real social relationships. We provide empirical evidence that this “social network topology” more accurately reproduces the argumentations carried out by humans when discussing a joint choice.

<table><tr><td rowspan="6"></td><td>AVG_Trust</td><td></td><td></td><td></td><td></td></tr><tr><td>AVG_Personality</td><td></td><td></td><td></td><td></td></tr><tr><td>STD_Trust</td><td></td><td></td><td></td><td></td></tr><tr><td>STD_Personality</td><td></td><td></td><td></td><td></td></tr><tr><td>precision@3</td><td></td><td></td><td></td><td></td></tr><tr><td>AVG_Trust</td><td>AVG_Personality</td><td>STD_Trust</td><td>STD_Personality</td><td>precision@3</td></tr></table>

Fig. 5. Correlation between performance (evaluated using precision@3) and the average (AVG) and standard deviation (STD) of the personality and trust parameters.

Our approach has been tested in the movie recommendation domain although our proposal is not speci<sup>fi</sup>c to this domain and could be easily adapted to others. To evaluate the accuracy of the system we compare the products chosen by real groups of users to the ones proposed by our recommender. We apply two different metrics to measure the degree of overlap between both sets of products. Our system performs in a similar way to standard group models when we evaluate internally whether there is at least one product correctly proposed by the recommender. However, when we toughen the evaluation metric and measure whether there are at least two correct proposals, our approach is 17% more accurate.

Our experiments also compare users' individual satisfaction. This is how individual preferences are taken into account when deciding a common product for the group. Thanks to the argumentation capabilities given to agents we obtain an increase of 5% in individual satisfaction.

Regarding future work we think that any improvement in the individual goodness value used internally by each agent to represent the preference of the user for a given product would have a high impact on the <sup>fi</sup>nal result for the group. To do so, we plan to test other individual preference estimation techniques like collaborative <sup>fi</sup>ltering. Furthermore, we are currently implementing a real application in Facebook that will apply the proposed techniques to recommend movies to groups of friends. This application will serve as a real scenario to validate current and future methods.

The most signi<sup>fi</sup>cant limitation of our study is the nature of the groups being evaluated. In this study we have evaluated groups which members had a friendship relation. However the performance of the system when applied to other kinds of groups, such as families, should be also studied.

We can conclude that our model proposed accurately reproduces real decision making processes experienced by groups of people when deciding leisure activities. The improvement is not only due to the inclusion of personality and social trust factors, but also to the agent-based architecture that simulates face-to-face discussions between users.

## References

[1] A. Aamodt, E. Plaza, Case-based reasoning: foundational issues, methodological variants, and system approaches, Arti<sup>fi</sup>cial Intelligence Communications 7 (1994) 39–59.

[2] P. Avesani, P. Massa, R. Tiella, A trust-enhanced recommender system application: Moleskiing, SAC '05: Proceedings of the 2005 ACM Symposium on Applied Computing, ACM, NY, USA, 2005, pp. 1589–1593.

[3] J. Bobadilla, F. Serradilla, A. Hernando, Collaborative <sup>fi</sup>ltering adapted to recommender systems of e-learning, Knowledge-Based Systems 22 (2009) 261–265.

[4] Srdjevic Bojan, Linking analytic hierarchy process and social choice methods to support group decision-making in water management, Decision Support Systems 42 (2007) 2261–2273(Decision Support Systems in Emerging Economies).

[5] B. Brehmer, Time scales, distributed decision making and modern information technology, in: J. Rasmussen, B. Brehmer, J. Leplat (Eds.), Distributed decision making: cognitive models for cooperative work, Wiley, 1991.

[6] Y.L. Chen, L.C. Cheng, C.N. Chuang, A group recommendation system with consideration of interactions among group members, Expert Systems with Applications 34 (2008) 2082–2090.

[7] A. Crossen, J. Budzik, K.J. Hammond, Flytrap: intelligent group music recommendation, IUI, 2002, pp. 184–185.

[8] E. Gilbert, K. Karahalios, Predicting tie strength with social media, CHI '09: Proceedings of the 27th international conference on Human factors in computing systems, ACM, New York, NY, USA, 2009, pp. 211–220.

[9] J.A. Golbeck, Computing and applying trust in web-based social networks. Ph.D. thesis, College Park, MD, USA , 2005. (Chair-Hendler, James).

[10] J. Golbeck, Combining provenance with trust in social networks for semantic web content <sup>fi</sup>ltering, in: L. Moreau, I.T. Foster (Eds.), Provenance and Annotation of Data, International Provenance and Annotation Workshop, IPAW 2006, Chicago, IL. USA May 3–5 2006 Revised Selected Papers volume 4145 of Lecture Notes in Computer ScienceSpringer, 2006, pp. 101–108.

[11] J. Golbeck, Generating predictive movie recommendations from trust in social networks iTrust: 4th International Conference on Trust Management, IUI 2006 pp. 93–104.

[12] J. Golbeck, J.A. Hendler, Inferring binary trust relationships in web-based social networks, ACM Transactions on Internet Technology 6 (2006) 497–529.

[13] S. González-Sanz, J.A. Recio-García, B. Díaz-Agudo, D2ISCO: Distributed Deliberative CBR Systems with iCOLIBRI. 1st Int. Conference on Computational Collective Intelligence, volume 5796 of LNCS Springer, 2009 pp. 321–332

[14] T. Grandison, M. Sloman, A Survey of trust in internet applications, IEEE Communications Surveys and Tutorials 3 (2000) 2-16

Please cite this article as: J.A. Recio-García, et al., Including social factors in an argumentative model for Group Decision Support Systems, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.05.007

[15] A. Jameson, B. Smyth, Recommendation to groups, in: P. Brusilovsky, A. Kobsa, W. Nejdl (Eds.), The Adaptive Web, Methods and Strategies of Web Personalization, Volume 4321 of Lecture Notes in Computer Science, Springer, 2007, pp. 596–627.

[16] D. Jannach, M. Zanker, A. Felfernig, G. Friedrich, Recommender Systems: An Introduction, Cambridge University Press, 2011.

[17] D.B. e. Leake, Case-based reasoning: experiences, lessons, and future directions, Menlo Park, CA: AAAI Press/MIT Press, Menlo Park, CA, 1996.

[18] H. Lieberman, N.W.V. Dyke, A.S. Vivacqua, Let's browse: a collaborative web browsing agent, IUI, 1999, pp. 65–68.

[19] J. Masthoff, Group modeling: selecting a sequence of television items to suit a group of viewers, User Modeling and User-Adapted Interaction 14 (2004) 37–85.

[20] J. Masthoff, A. Gatt, In pursuit of satisfaction and the prevention of embarrassment: affective state in group recommender systems, User Modeling and User-Adapted Interaction 16 (2006) 281–319.

[21] D.W. McDonald, Recommending collaboration with social networks: a comparative evaluation CHI '03: Proceedings of the SIGCHI conference on Human factors in com: puting systems, ACM, New York, NY, USA, 2003, pp. 593–600.

[22] L. McGinty, B. Smyth, Collaborative case-based reasoning: applications in personalised route planning, Procs. ICCBR, Springer LNAI, 2001, pp. 362–376.

[23] S. Ontañón, E. Plaza, An argumentation-based framework for deliberation in multiagent systems, Argumentation in Multi-Agent Systems. LNCS, volume 4946, 2008, pp. 178–196.

[24] L. Quijano-Sánchez, J.A. Recio-García, B. Díaz-Agudo, Personality and social trust in group recommendations, Procs of the 22th International Conference on Tools with Arti<sup>fi</sup>cial Intelligence, ICTAI'10, IEEE Computing Society, 2010, pp. 121–126.

[25] J. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2002) 111–126(Decision Support System: Directions for the Nest Decade).

[26] S.B. Shum, L. Cannavacciuolo, A.D. Liddo, L. Iandoli, I. Quinto, Using social network analysis to support collective decision-making process, IJDSST 3 (2011) 15–31.

[27] R.R. Sinha, K. Swearingen, Comparing recommendations made by online systems and friends, DELOS Workshop: Personalisation and Recommender Systems in Digital Libraries, 2001.

[28] J. Song, F. Zahedi, Trust in health infomediaries, Decision Support Systems 43 (2007) 390–407.

[29] R.H. Kilmann, K.W. Thomas, Developing a Forced-Choice Measure of Con<sup>fl</sup>ict-Handling Behavior: The “MODE” Instrument, Educational and Psychological Measurement 37 (1977) 309–325, http://dx.doi.org/10.1177/001316447703700204.

[30] T.W. Wang, S.K. Tadisina, Simulating internet-based collaboration: a cost-bene<sup>fi</sup>t case study using a multi-agent model, Decision Support Systems 43 (2007) 645–662.

[31] In: G. Weiss (Ed.), Multiagent Systems: A Modern Approach to Distributed Arti<sup>fi</sup>cial Intelligence, MIT Press, Cambridge, MA, USA, 1999.

[32] C.N. Ziegler, J. Golbeck, Investigating interactions of trust and interest similarity, Decision Support Systems 43 (2007) 460–475.

[33] H.J. Zimmermann, Fuzzy Set Theory—and its Applications, 3rd ed. Kluwer Academic Publishers, Norwell, MA, USA, 1996.

![](/api/attachments/S74E8RBH/fulltext/images/2a3f4d0bbed60f30e86e84d97f74dd61bafa1001dcc57668c005c00240258b1b.jpg)

![](/api/attachments/S74E8RBH/fulltext/images/cc75e78bd908037ff49608e66d3fa7a22474a0bf12db7ab5c91d0ea080b34116.jpg)

Juan A. Recio-Garcia is Assistant Teacher at the Arti<sup>fi</sup>cial Intelligence Department at the Computer Science Faculty at the Complutense University of Madrid, where he obtained a PhD in Computer Science in 2008, His research has focused on the con<sup>fl</sup>uence of Software Engineering and Case-Based Reasoning, developing the COLIBRI framework for building CBR systems. Currently he is also working in the areas of Recommender Systems and Semantic Web. He has several publications at International Conferences and Journals.

![](/api/attachments/S74E8RBH/fulltext/images/fb66dad8b1d8a515b884b43f5376b4d69e81dfd21bf0760459dc91638dacac97.jpg)

Lara Quijano is a PhD student at the Complutense Univeristy of Madrid. Her areas of research are Recommender Systems, Social Networks, Social Factors, Multi-Agent Systems, Decision Support Systems, etc. She is presently working in Decision Support Systems where she has developed several algorithms to re<sup>fl</sup>ect accurately argumentations between users in this kind of systems. Her publications have appeared in various Journals and International Conferences.

Belen Diaz-Agudo is a professor at the Arti<sup>fi</sup>cial Intelligence Department at the Computer Science Faculty at the Complutense University of Madrid. Her research interests include Case Based Reasoning, Semantic Web, Recommender Systems and their relationships to applied intelligent systems. She has more than 50 publications at International Conferences and Journals, and has participated in the organization of AI conferences.
