---
otero_id: 2098
otero_key: "ATYGAAHW"
title: "Networked individuals predict a community wide outcome from their local information"
authors: "Thomas Chesney"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.07.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Networked individuals predict a community wide outcome from their local information

Thomas Chesney ⁎

Nottingham University Business School, Wollaton Road, Nottingham NG8 1BB, UK

a r t i c l e i n f o

Article history: Received 13 February 2013 Received in revised form 19 July 2013 Accepted 21 July 2013 Available online 1 August 2013

Keywords: Social network Consensus decision Viral marketing Simulation

## a b s t r a c t

The term ‘viral’ is used to describe a phenomenon that tends to be shared by those who encounter it. This paper considers the act of responding positively to a phenomenon by sharing it with others, something exempli<sup>fi</sup>ed by the online social media acts of choosing to ‘like’ on Facebook, ‘retweet’ on Twitter, or by a similar mechanism on websites such as LinkedIn, Flickr or Pinterest. Using a threshold model of in<sup>fl</sup>uence, simulations are run on four network structures where a critical mass chooses to share a phenomenon that eventually either goes viral or does not. The data collected are examined to determine whether an individual node can make an accurate prediction about the state of the entire network just from information on the behavior of their neighbors. The intention is to study what it is in terms of network structure that makes an individual good at sensing the zeitgeist, or ‘spirit of the age’. Findings show that those best placed to predict are ‘important’ as measured by network centrality, and members of numerous communities. The characteristics of the critical mass are important in determining the spread of a phenomenon and it is possible for an individual node to predict an outcome as well as an observer who has access to the state of every node in the network. Potential applications might be found in monitoring the success of marketing campaigns, or in organizations wishing to keep abreast of current trends in a situation where data on network structure is available but data on the activity of network members is limited.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

The Mona Lisa, Harry Potter and the Philosopher's Stone, the Bat Out Of Hell album, grunge music group Nirvana and the horror <sup>fi</sup>lm Saw, all have one thing in common: they were not expected to be popular yet they each achieved immense cultural signi<sup>fi</sup>cance. Analyzing them to identify the source of their huge success would be unproductive. The intrinsic quality of each could be examined, but this would not reveal why it became so phenomenal. All of them had some or even many contemporary ‘competitors’ of similar quality that did not—to use the social contagion terminology—go viral.

‘Going viral’ is an ill de<sup>fi</sup>ned term but can be taken to mean the tendency of a phenomenon to be shared by those who encounter it [29]. This sharing could happen in a physical sense (as in “take this CD and listen to it”) or it could be the sharing of an idea (“that music group is worth listening to”). With the use of social media such as Facebook, Twitter and LinkedIn, it is even simpler that these — information in any format can be shared with friends by a single mouse click, or it can even be set to happen automatically (examples are given in Section 2).

Whether a phenomenon will go viral cannot be predicted by examining the characteristics of that phenomenon: going viral is a network effect.<sup>1</sup> Watts [64, Chapter 3] gives a good account of this argument. There would however be enormous value in being able to predict which ideas—or songs, books, products, adverts etc.—are going viral [2,1,3,61,30] and social media services already sell related information to businesses (see for example http://datasift.com). At the point of creation success cannot be predicted; by the time something has gone viral, everyone knows that it is a success. This paper examines making a prediction between these two points, limiting it to be based on what one member of a social network can see in the behavior of his or her neighbors. In a simulation study the paper considers the network characteristics of individuals who are successful at making a prediction, characteristics of early adopters, and the impact of network structure on the ability to predict. The intention is to study what it is in terms of network structure that makes an individual good at sensing the zeitgeist, or ‘spirit of the age’.

![](/api/attachments/ATYGAAHW/fulltext/images/5cd92033560633a580301521ec161d780b4993c63ff5040b0516e14e8870c252.jpg)  
Fig. 1. Screen shot from the Rotten Tomatoes website showing a list of <sup>fi</sup>lms that Facebook friends have chosen to like

The application of this research question may not be immediately apparent. Sargut and McGrath [53] discuss a concept they refer to as the ‘hyperconnected world’, a place characterized by complexity. They describe the difference between operating in a complicated environment and a complex environment as being the presence of unpredictable interactions between connected elements which mean simple actions can produce unintended consequences. In a hyperconnected world, an understanding of each element that makes up an environment does not produce an understanding of the behavior of the environment as a whole [45]. As an example of this hyperconnection, members of the online social network Facebook have recently noticed information about (or perhaps ‘information from’ — this point is debatable) their friends appearing on so called ‘trusted partner’ websites [31]. One instance of this can be found on the movie review site Rotten Tomatoes where visitors to the site who are also members of Facebook, are presented with their ‘Friend Activity’ (Fig. 1). This activity is a list of <sup>fi</sup>lms their friends have selected (on Facebook) to ‘like’. Similar features can be found on travel websites, video sharing sites and many others.<sup>2</sup>

This is seen as a very signi<sup>fi</sup>cant development [53,18] which creates decision points where an individual knows something of what his or her friends have done given the same choice. This is not new in itself — friends have always discussed such things. What is new is the availability of explicit data, without requesting it, from perhaps a large number of friends at the time an individual is making a decision. Such decision points are likely to become more common and it is not unrealistic to think that future developments will include not only what <sup>fi</sup>lms/holidays/etc. a friend liked, but also what <sup>fi</sup>lms and holidays they disliked. It has been argued [53] that knowing what friends think of a product or service will have a huge impact on the decision to adopt that product or service. Even product reviews from complete strangers on sites such as Amazon or eBay, or word of mouth reviews are known to affect an individual's purchase decision [51,70,22,46].

## 2. Social networks and social contagion

## 2.1. Social contagion

This paper considers the act of responding positively to something which causes it to be shared with others. The scenario studied is exempli<sup>fi</sup>ed by the Facebook app of the music sharing service Spotify. This app automatically shares with friends (although it can be turned off) a list of songs that individuals have listened to. Imagine I see that three of my friends have listened to a song. This alone causes me to listen to the song. Facebook shares this fact with my friends, which causes more of them to listen to it too. That everyone involved may have hated the song does not come into it. Several other examples are presented in Fig. 2.

There are two salient features of this scenario that set it apart from most examples of information diffusion. Firstly, an individual does not choose to share the phenomenon. The choice they make is whether or not to pay attention to it; the sharing happens automatically. Secondly, the phenomenon is either shared or not by all who encounter it; there is no deterioration in signal strength. This is unlike a rumor or a ‘hot tip from a market trader, which loses its spreading power as it moves through the network away from its originator.

![](/api/attachments/ATYGAAHW/fulltext/images/5febeb6926bcac45117ff5a5d2baf8de9c3cf03e328f4ff83ea5d593633794c1.jpg)  
Fig. 2. Facebook adverts that use the choices of others: on the left three friends have used TripAdvisor and it is unclear whether the experience was positive or negative; on the right eight people have used and liked Amazon. This technology has not been without teething troubles. In 2007, the Facebook product Beacon garnered controversy when it shared details of purchases made by individuals, including what were to have been surprise gifts.

A number of researchers have examined how to identify individuals —in terms of their network structure—that a marketing department would select to share their product if they could, in order for that product to spread as widely as possible [41,27,38,37]. The current research question is related but here we are not trying to identify the top in<sup>fl</sup>uencers. Rather we want to identify the individuals who might potentially be able to sense whether something is on its way to going viral. We say ‘potentially be able’ because the individuals we are trying to identify might not realize that they are well placed to make this prediction, something that has implications for the prediction method we will test.

There is a wide literature from psychology and economics examining in<sup>fl</sup>uence. Rather than attempt to review it all here, this section will focus solely on the mechanism of in<sup>fl</sup>uence that we use, a threshold model. For a comprehensive review of the wider literature see Forgas and Williams [25]. Threshold rules have been widely studied although they are not the only model of in<sup>fl</sup>uence [23]. For instance, both Kiss and Bichler [38] and Aral and Walker [4] (discussed at length later in this section) model the determinants that impact on the likelihood of sharing. However threshold rules have been used successfully in the past to examine in<sup>fl</sup>uence, and several studies reviewed next demonstrate it can be appropriate in an online social media context.

In an analysis of collective behavior Granovetter [28], drawing on the work of Schelling [54], uses a threshold rule to illustrate how two almost identical crowds can arrive at vastly different group behavior. The running case he uses is a riot although the same idea can apply to almost any binary choice situation. The examples he gives are diffusion of innovations, spread of rumors, spread of disease, worker strikes, voting, going to university, leaving meetings/parties and migration. The key criterion is that the cost and bene<sup>fi</sup>t to each individual depend on the choices that others make: as more people make a positive choice, the cost of making a positive choice decreases and the bene<sup>fi</sup>ts increase. If few people riot then the cost is high as they are all likely to be caught and the bene<sup>fi</sup>t is low as together they may not create much mayhem. If lots of people riot the cost is low as few can expect to be caught and collectively they will achieve high damage.<sup>3</sup>

Going back to being in<sup>fl</sup>uenced on Facebook to listen to a song on Spotify, here the cost and bene<sup>fi</sup>t are very low but they are not zero. The ‘cost’ of listening to a song is that I might hear a song that I do not enjoy or miss hearing one that I would. This cost goes down (actually the likelihood of paying it goes down) as I see more of my friends listening to it.<sup>4</sup>

Following Watts and Dodds [65], the threshold rule used here differs from Granovetter's in two ways. Granovetter de<sup>fi</sup>nes a person's threshold as the proportion of the group he or she would have to see decide positively before he or she would decide positively. Here the threshold is an absolute value rather than a proportion: the probability p(s ) of a person i choosing to respond positively<sup>5</sup> is 1 whenever the number of their friends e who have chosen to respond positively is greater than or equal to their threshold v:

$$
p (s _ {i}) = \left\{ \begin{array}{l l} 1 & \text { if } e _ {i} \geq v _ {i} \\ 0 & \text { if } e _ {i} <   v _ {i} \end{array} \right..
$$

In addition, Granovetter considers one group of individuals all connected to each other. Using network terminology he considers a ‘fully connected graph’. The groups studied here are arranged in a structure intended to capture the characteristics of social networks. What these characteristics are will be explained later but for now we only need note that an individual in the network is not connected to all others — he or she only sees the actions of his or her friends or neighbors, not the actions of everyone in the network. (In fact, Granovetter did discuss extending his model to include social structure.)

To initially trigger a threshold, a critical mass is needed. A critical mass is a small group of early adopters who ‘start the ball rolling’ in in<sup>fl</sup>uencing the spread of a phenomenon [42]. Conventional wisdom states that for the phenomenon to spread, the critical mass should be special in some way: highly connected or have above average in<sup>fl</sup>uence [35,40,50,59,60]. However this view has been challenged [65] with Watts [64] pointing out that there is nothing special about the match that starts a forest <sup>fi</sup>re.

Three important studies examine in<sup>fl</sup>uence in social networks and demonstrate the validity of a threshold model. In the <sup>fi</sup>rst, Salganik and Watts [52] run an experiment where 12,000 subjects are asked to visit a website where they can download songs by unknown bands. Subjects in the treatment group see a proxy for each song's popularity based on the number of times it was downloaded. The authors manipulate this and <sup>fi</sup>nd that the perceived popularity of the songs does in fact in<sup>fl</sup>uence whether it is downloaded. The authors do not attribute this to participants following a threshold rule although that is consistent with the results. The only problem with this interpretation is that in some cases very unpopular songs are downloaded more times than would be expected by random. This suggests that popularity and unpopularity each have salience and it is this salience rather than a threshold that is in<sup>fl</sup>uencing their download. Granovetter [28, p. 1437] would defend the threshold model by arguing that this salience is impacting on what the threshold is, and not operating in place of a threshold. That popular and unpopular songs are downloaded does complicate the threshold model though, as both cases in<sup>fl</sup>uence the same outcome (a download). This situation is therefore unlike the ones Granovetter studies although he does brie<sup>fl</sup>y discuss such complicated models and concludes that a threshold rule is still consistent with them

Centola [15] on the other hand <sup>fi</sup>nds explicit support for the use of a threshold rule in an online social network. He studies how knowledge about whether others have adopted healthy behaviors impacts on whether an individual chooses to adopt them. He creates social networks by linking participants according to two predetermined network structures, to examine the in<sup>fl</sup>uence that structure has on adoption behavior. Results show that social reinforcement from multiple people makes participants much more willing to adopt behavior up to a point after which additional connections with adopters make no difference. This and a follow up study of the same data [16] suggest that a threshold may be operating in the adoption choice and certainly a threshold model is consistent with the data observed.

Finally Aral and Walker [4] report a study of in<sup>fl</sup>uence in online social networks. They examine a Facebook app that sends messages— which are very similar to the Spotify information described before—to a random selection of the friends of an individual who installed the app, alerting them to this fact. The authors analyze the data to identify in<sup>fl</sup>uential and susceptible individuals. They do not explicitly make use of a threshold model but examine the determinants of the probability of adoption as a function of the number of messages an individual receives from one friend. Their results do not negate a threshold model, but highlight that threshold values would be in<sup>fl</sup>uenced by the age, sex and relationship status of both the in<sup>fl</sup>uencers and the individuals being in<sup>fl</sup>uenced. We could imagine incorporating in<sup>fl</sup>uencer characteristics by adjusting the threshold as before. For example they <sup>fi</sup>nd that men are more in<sup>fl</sup>uential than women. To accommodate this in the threshold model, in a group with more men than women we could imagine that an individual's threshold drops. Their model is one individual in<sup>fl</sup>uencing one individual. This is different from Granovetter's model, where each group member sends out one message and it is the number of people who send out a message that triggers the threshold rule. This later rule is the one used in this study, and it is applied on simulated and real social networks.

Our interest lies in the characteristics of these networks and what is it about how they are structured that impacts on an individual's ability to predict. We do not consider the characteristics of individuals in the network, which have been well studied by other researchers [4,37]. Following Centola [16] we vary network characteristics—described in the next section—in order to isolate the part that structure plays, while holding individual characteristics constant. We vary how nodes are positioned in networks by using four pre-set network structures, which are described in the method section.

## 2.2. Social networks

Given the description in Section 2.1, the likelihood of a node deciding to share can be calculated. Let x be the size of the critical mass, n the number of nodes in the network, $\nu _ { i }$ the threshold value of node i and $e _ { i }$ the number of $i \backslash s$ friends. Then the probability p(si) of i sharing at the end of time period $t _ { 1 } ,$ , assuming that i is not itself part of the critical mass, is the probability that in $e _ { i }$ there are at least as many members of the critical mass than v :

$$
p (s i _ {t 1}) = \frac {e _ {i} !}{(e _ {i} - v _ {i}) ! (v _ {i} !)} \cdot \left(\frac {x}{n}\right) ^ {v _ {i}}.
$$

The probability of sharing at the end of ${ \bf \dot { \boldsymbol { t } } } _ { 2 }$ is the probability that in the neighborhood of i there are at least as many nodes that shared in $t _ { 1 }$ as the threshold:

$$
p (s i _ {t 2}) = \frac {e _ {i} !}{(e _ {i} - v _ {i}) ! (v _ {i} !)} \cdot p (s i _ {t 1}).
$$

By any given time period, the probability of a node sharing is:

$$
p (s i _ {t n}) = \frac {e _ {i} !}{(e _ {i} - v _ {i}) ! (v _ {i} !)} \cdot p (s i _ {t n - 1}).
$$

An individual's prediction rule is deliberately different from their decision to share — we can all think of things we happen to like and will tell others about, but which we know are not considered popular or mainstream. An individual's prediction rule will be based on the proportion of their friends who share and is presented as follows, where w is the number of friends who have shared and a is the proportion of friends the individual is going to use to make their prediction.

$$
p r e d i c t i o n = \left\{ \begin{array}{l l} s u c c e s s & \text { if } (w / e) \geq \alpha \\ f a i l & \text { if } (w / e) <   \alpha \end{array} \right..
$$

The likelihood of this rule being triggered in any time period is:

$$
p (p r e d i c t _ {s u c c e s s}) = \sum_ {1} ^ {\frac {e ^ {t}}{(\epsilon - a) ! (a !)}} p (s i _ {t n}) ^ {a}.
$$

If connections occur at random, the likelihood of node i being connected to a speci<sup>fi</sup>c node is $\frac { e _ { i } } { n - 1 }$ . However it is known that connections do not occur at random.

Typically social networks are characterized by high clustering and short path lengths [66], preferential attachment [7], and assortative mixing by degree [48]:

1. Clustering can be informally explained as the friend of my friend is also my friend, and can be de<sup>fi</sup>ned as: if Node A is related to Node B and B is related to $\complement ,$ then—if the network exhibits high clustering—it follows that A tends to also be related to C. Clustering is measured by the clustering coef<sup>fi</sup>cient which can be de<sup>fi</sup>ned [47] as the fraction of paths of length two—for example A to B and B to C—that are closed by a relationship between A to C.

2. Path length is the number of edges between any two nodes in the network, and in a social network is a measure of the shortest number of acquaintances needed to link two people. That people in a social network are linked by short paths was famously demonstrated by Milgram's six degrees of separation experiment [44]. The measure of this is the average path length which is the shortest path between a node and all other nodes, averaged across all nodes in the network.

3. Preferential attachment is said to occur when those who have gain more [49]. In terms of network structure, preferential attachment exists when the few know many and the many know few. In other words most nodes are connected to a small number of other nodes, while a small number of nodes are highly connected. It has been suggested [7] that nodes in a social network tend to interact with n other nodes with a probability $P ( n ) \approx n ^ { - \gamma } .$ . This results in what is known as a scale-free power-law degree distribution, although the existence of an actual power law has been called into question [56,55] and one will not appear in this study.

4. When a network exhibits assortative mixing, nodes in the network tend to be linked to nodes that they are similar to. This similarity could be along any dimension: race or socio-economic status for instance. A node's degree is the number of other nodes it is directly connected to. Assortative mixing by degree exists when highly connected nodes tend to be connected to other highly connected nodes. The assortative coef<sup>fi</sup>cient measures assortative mixing and can be interpreted as a correlation coef<sup>fi</sup>cient [47].

It has recently been shown that homophily has a signi<sup>fi</sup>cant role in the spread of information around a network [34,32]. While we do not explicitly consider homophily here, it is captured in network structure and therefore does feature in a sense.<sup>6</sup> However the existence of homophily may lead to some friends (those most similar to an individual) being given more weight than others in their ability to in<sup>fl</sup>uence an individual. As stated earlier in Footnote $^ { 4 , }$ we do not consider relationship ‘weight’ here but we do discuss the issue later.

The preceding are network level metrics which will be used to compare the different social structures examined in this paper. There also exist node level metrics which quantify characteristics of individual nodes. Given the analysis from before, it might be expected that the following metrics will impact on a node's ability to predict:

1. Degree centrality has already been mentioned. It is the number of neighbors each node has and can be used as a proxy for how central or important a node is [47].

2. Betweenness centrality is similar in concept to degree but is de<sup>fi</sup>ned differently. It measures the extent to which a node lies on paths between other nodes [26] and is calculated as the average number of paths that pass through anode between every pair of nodes [47].

3. Local clustering is the probability that two of a node's neighbors are themselves linked [63].

4. A geodesic is the shortest possible path between two nodes [67].

5. Lastly a node's threshold value is essentially a metric of how susceptible that node is to in<sup>fl</sup>uence.

## 2.3. Hypotheses

When a phenomenon is shared, the processes at work occur over time. In a simulation this is usually modeled in discrete time periods (see [57] for a review). In the <sup>fi</sup>rst time period, the critical mass shares news about the phenomenon with their neighbors. The length of the path between a member of the critical mass and their neighbors is 1. In subsequent time periods, the length of the paths along which news is shared increase by 1. Therefore the farther away a node is from the critical mass, the longer it will take for news about the existence of the phenomenon to reach it, let alone for enough information to <sup>fi</sup>lter through in order to make a prediction. We would expect a node far from the critical mass to be less able to sense whether something is being shared than a node near it. This is equally true outside of a simulation, where time is continuous: if news from the critical mass must pass through many people to get to an individual, then that individual would be expected to be slower at sensing whether something is being shared than someone closer to the critical mass. Since after a certain point (described in Section 4) phenomena that are going viral get shared rapidly, we expect this slowness in turn to have an impact on predictive accuracy.

Hypothesis 1. A node's predictive accuracy will be negatively related to its geodesic to the nearest member of the critical mass.

The value of an individual's position in a network can be considered in terms of the social capital which it offers [36]. Social capital can be described as ‘opportunity’ [12]. It is the value that comes from knowing what resources others possess and having the opportunity to access them [19]. Those with high network centrality tend to have high social capital [13]. We hypothesize therefore that those with high centrality will have access to superior social resources and that these will in turn lead to a superior ability to predict.

Hypothesis 2. A node's predictive accuracy will be positively related to its importance as measured by its centrality.

Diffusion through a network stalls when it invades a ‘tight knit’ or highly clustered community [24]. Information spreads through the community ef<sup>fi</sup>ciently as members quickly share it which each other, but beyond them it can struggle to break away to reach the rest of the network [17]. This has been observed in simulation studies: [39] <sup>fi</sup>nd that diffusion occurs ef<sup>fi</sup>ciently between communities only when members are forced to create links with members of one other community. When links form randomly and more realistically with others from multiple communities, diffusion slows.

This means that a node which sits in a tight knit community will be able to see what is being shared around that community but may struggle to get a sense of what is happening outside it. How ‘tight knit’ a community is can be measured by the local clustering coef<sup>fi</sup>cient, as described in the previous section. Therefore we expect the clustering coef-<sup>fi</sup>cient to be negatively related to accuracy.

Hypothesis 3. A node's predictive accuracy will be negatively related to its clustering coef<sup>fi</sup>cient.

Most work looking at diffusion through social networks considers an individual's susceptibility to social in<sup>fl</sup>uence, rather than the susceptibility of their friends [69], even though the susceptibility an individual's friends will likely have an impact on a number of outcomes, including an individual's ability to predict whether a phenomenon is going viral. However it is unclear what the underlying processes involved are. Will an individual who has friends who are particularly choosey about what they share be better able to predict? Or would it be better to have friends who they share everything they come across? There is a case for thinking either might be best.

Choosy friends may act as a <sup>fi</sup>lter removing all but the ‘best’ and therefore most likely to succeed phenomena from an individual's sensorium. Alternatively those who share more will alert an individual to the existence of more, perhaps before any of it starts to take off. Adoption rates have been found to increase when the number of friends adopting increases [6]. However this only means that having susceptible friends will make it more likely that the phenomenon being shared will go viral, which is not surprising. The impact on accuracy has not been tested before, therefore the following hypothesis is left directionless.

Hypothesis 4. Susceptibility of friends, as measured by their average threshold value, will be related to predictive accuracy.

Much of the diffusion literature suggests that members of a critical mass that can in<sup>fl</sup>uence a phenomenon to go viral must be special in some way — centrally located within the network for example [35,40,50,59,60]. For instance, in a study of online communities, [62] <sup>fi</sup>nd that a successful critical mass has access to resources others do not have. In network terms, both degree centrality and betweenness centrality bring with them additional resources [47], and so we hypothesize that a successful critical mass will have high centrality.

Hypothesis 5. A critical mass that shares phenomena that spread successfully will have higher centrality than a critical mass that shares phenomena that did not spread successfully.

## 3. Method

The research question was studied by simulation. Social science has been slow to adopt simulation as a research method [5] although this is changing (for example [58]). Three undirected network con<sup>fi</sup>gurations were simulated to contain 500 nodes. An additional network structure, part of the Facebook graph with 534 nodes, was also used. Each node was created to be a re<sup>fl</sup>ex agent [10] that would act according to a decision rule and react to the decisions of other nodes. The decision rule was the threshold rule described before: in any time period, decide to share if the number of neighbor nodes which have decided to share in the previous time period is greater than or equal to the threshold. ‘Decide to share’ means simply that a node transmitted a 1 to all of its neighbors, otherwise it transmitted a 0. Threshold values were drawn randomly from the normal distribution N(4,1).

The procedure for running one simulation was as follows. The simulation ran in discrete time periods. To start, x nodes were randomly chosen with uniform probability to be the critical mass. The critical mass was forced to decide positively in time period, $t _ { 0 } .$ Nodes reacted to this in time period $t _ { 1 }$ and so on in subsequent time periods. Time period $t _ { m a x }$ was chosen by experimentation to be long enough to achieve an outcome and x was chosen such that in under half the simulations the phenomenon spreads successfully through the network. One thousand simulations were run for each network con<sup>fi</sup>guration.

The networks were created and the simulations run using the R programming language and were:

## 1. A small world model.

In this con<sup>fi</sup>guration networks exhibit high clustering and short path lengths. Each node is directly linked to a small set of other nodes arranged in ‘neighborhoods’, which gives high clustering, and all nodes can be reached from any one node in a small number of steps, which gives short path lengths. The small world network used here is based on work by Watts and Strogatz [66] who <sup>fi</sup>nd that small world networks can be classi<sup>fi</sup>ed by two parameters, the clustering coef<sup>fi</sup>cient and average path length. Full details of how this network was created are presented in the Appendix A.

2. A model designed to exhibit all four social network characteristics, referred to as M3.

As explained earlier, real social networks are known to have characteristics in addition to high clustering and short path lengths. This second model is intended to model these additional properties and is therefore more realistic than the small world. To create this model, nodes were added one at a time in discrete time steps. Before connections were made, a node joined one ‘group’, which was not explicitly part of the network. Network links were <sup>fi</sup>rst made between that node and the others in the group with a high probability which gives that node a set of ‘friends’. Then additional links were made between the node and members of other groups that the node's friends were also members of with low probability. In laymen's terms, each node followed the following rule: make friends with those around you, plus some of their friends. Full details are given in the Appendix A.

## 3. A random model.

A con<sup>fi</sup>guration model [47] is a network in which the degree of each node is speci<sup>fi</sup>ed, but otherwise all connections are created randomly. This network was a con<sup>fi</sup>guration model, created to have the same degree distribution as the M3 model. This means that the 500 nodes in the random model have the same degrees as the 500 nodes in the M3 model, but the edges between them were all created randomly. It also means that, as described later in the discussion section, there is a strong case to be able to directly compare M3 and the random model. As before, details are given in the Appendix A.

## 4. A sample of Facebook's graph.

Network structure data from Facebook was taken from [43]. These authors captured the groups (Facebook's terminology is ‘lists’) that one user is a member of, plus the relationships that exist between all members of those groups. The resulting network featured 534 users, a similar size to the other networks.

The <sup>fi</sup>rst three of these were chosen for this study because they vary in how much they exhibit the network and node characteristics, which were explained in Section 2.2. All three exhibit short path lengths. M3 exhibits high clustering, preferential attachment and assortativity by degree. The small world model exhibits high clustering but not preferential attachment or assortativity. The random network exhibits preferential attachment but not clustering or assortativity. By varying these characteristics we are able to study the impact they have on the ability to predict. The Facebook network was included to verify our results in a real setting.

Statistics on the four networks are shown in Table 1. The table also gives an indication of similarities between M3 and the Facebook sample.

Table 1 Network metrics

<table><tr><td></td><td>Small world</td><td>M3</td><td>Random</td><td>Facebook</td></tr><tr><td>Average path length</td><td>3.5</td><td>5.0</td><td>3.0</td><td>3.4</td></tr><tr><td>Clustering</td><td>0.36</td><td>0.43</td><td>0.05</td><td>0.45</td></tr><tr><td>Assortativity</td><td>-0.005</td><td>0.310</td><td>-0.028</td><td>0.220</td></tr><tr><td>Critical mass (x) used</td><td>60</td><td>20</td><td>20</td><td>20</td></tr></table>

![](/api/attachments/ATYGAAHW/fulltext/images/4fddede538d85c77024b16be556e515b480b7229ef2c2bd562759694c1277574.jpg)  
Fig. 3. An s-shaped adoption curve showing the typical way a phenomenon goes viral. The tipping point is where phenomena destined not to go viral <sup>fl</sup>atten out and those destined for success take off.

Additional information is given in the Appendix A. By running one thou sand simulations on each network we can identify which nodes are good at prediction, and statistically analyze why this is in terms of the node level characteristics. We can also, to a limited degree, compare the network structures themselves to determine how the network level characteristics in<sup>fl</sup>uence ability to predict. (The reason we can only do this to a limited degree is fully explained at the start of the discussion section but in brief it is because the networks were created parametrically and only certain parameters can be directly compared.)

## 4. Results

In this section results are presented largely without comment — a discussion will be offered in Section 5. Three sets of analysis are presented: an examination of the characteristics of nodes that are successful at prediction alongside a comparison with unsuccessful nodes; an analysis of the characteristics of the critical mass and their relationship to success or failure; and a comparison of the accuracy achieved by individual nodes with that achieved by a global or ‘god's eye’ view of the network.

Successful simulations follow the well known adoption s-curve [32] shown in Fig. 3. We begin the analysis by considering what happens around the tipping point, when successes and failures begin to separate. A network structure had approximately the same tipping point in all simulations. This was identi<sup>fi</sup>ed by examining the time period when the number of share decisions in those simulations that were destined for failure tailed off. This is not a precise measure, and the studies reported were repeated for several times periods around the chosen tipping points, which were $t _ { 1 5 }$ for the small world model, $t _ { 3 }$ for the M3 model, $t _ { 4 }$ for the random model and $t _ { 3 }$ for Facebook. Results did not change. The measure of a node's accuracy was calculated to be:

$$
a c c u r a c y = \frac {\text { number   of   times   node's   sprediction   matched   the   outcome }}{\text { total   number   of   simulations }}.
$$

The mean (sd) accuracy achieved by nodes in each network for each value of a. (None of the nodes in the Facebook graph made a positive prediction with a = .7).

<table><tr><td rowspan="2"></td><td colspan="3">Value of a</td></tr><tr><td>0.3</td><td>0.5</td><td>0.7</td></tr><tr><td>M3</td><td>0.79 (0.03)</td><td>0.79 (0.01)</td><td>0.8 (0.00)</td></tr><tr><td>Small world</td><td>0.64 (0.03)</td><td>0.66 (0.02)</td><td>0.63 (0.03)</td></tr><tr><td>Random</td><td>0.85 (0.03)</td><td>0.86 (0.02)</td><td>0.87 (0.01)</td></tr><tr><td>Facebook</td><td>0.80 (0.03)</td><td>0.80 (0.03)</td><td>NA</td></tr></table>

Correlation coef<sup>fi</sup>cients (p-values) assessing the relationship between the predictive accuracy of nodes and the node level metrics. As before, since none of the nodes in the Facebook graph made a positive prediction with a = .7, this result is not included.

<table><tr><td rowspan="2">Network</td><td rowspan="2">a</td><td colspan="5">Metric</td></tr><tr><td>Degree centrality</td><td>Betweenness centrality</td><td>Local clustering</td><td>Average geodesic to critical mass</td><td>Average threshold of friends</td></tr><tr><td rowspan="3">M3</td><td>.3</td><td>.44 (0.00)</td><td>.14 (0.00)</td><td>-.26 (0.00)</td><td>-.50 (0.00)</td><td>.07 (0.12)</td></tr><tr><td>.5</td><td>.34 (0.00)</td><td>.10 (0.02)</td><td>-.30 (0.00)</td><td>-.35 (0.00)</td><td>.08 (.07)</td></tr><tr><td>.7</td><td>.19 (0.00)</td><td>.05 (0.23)</td><td>0 (1)</td><td>-.25 (0.00)</td><td>.13 (.00)</td></tr><tr><td rowspan="2">Small world</td><td>.3</td><td>.25 (0.00)</td><td>.29 (0.00)</td><td>-.26 (0.00)</td><td>-.37 (0.00)</td><td>-.02 (0.64)</td></tr><tr><td>.5</td><td>.15 (0.00)</td><td>.22 (0.00)</td><td>-.30 (0.00)</td><td>-.37 (0.00)</td><td>-.05 (0.30)</td></tr><tr><td rowspan="3">Random</td><td>.7</td><td>.05 (0.28)</td><td>-.07 (0.13)</td><td>.05 (0.24)</td><td>-.10 (0.03)</td><td>-.02 (0.72)</td></tr><tr><td>.3</td><td>.46 (0.00)</td><td>.30 (0.00)</td><td>.08 (0.08)</td><td>-.60 (0.00)</td><td>-.07 (0.12)</td></tr><tr><td>.5</td><td>.35 (0.00)</td><td>.20 (0.00)</td><td>.04 (0.36)</td><td>-.33 (0.00)</td><td>.02 (0.72)</td></tr><tr><td rowspan="3">Facebook</td><td>.7</td><td>.17 (0.00)</td><td>.09 (0.03)</td><td>.33 (0.00)</td><td>-.33 (0.00)</td><td>.12 (0.01)</td></tr><tr><td>.3</td><td>.13 (0.00)</td><td>.04 (0.38)</td><td>-.06 (0.15)</td><td>-.13 (0.00)</td><td>-.03 (0.45)</td></tr><tr><td>.5</td><td>.10 (0.02)</td><td>.03 (0.49)</td><td>-.16 (0.00)</td><td>-.10 (0.02)</td><td>-.03 (0.47)</td></tr></table>

Recall that an individual's prediction rule is presented as follows:

$$
p r e d i c t i o n = \left\{ \begin{array}{l l} s u c c e s s & \text { if } (w / e) \geq \alpha \\ f a i l & \text { if } (w / e) <   \alpha \end{array} \right..
$$

Low, mid and high values of a were considered, chosen to be: 0.3, 0.5 and 0.7. The simulations were processed to give each node's accuracy at making a prediction when following the above rule.

## 4.1. Characteristics of successful nodes

Two aspects of node characteristics were considered: the impact of network structure on node accuracy, and the relationship between node accuracy and node metrics. For reasons that will be fully discussed in Section 5, care needs to be exercised when comparing the network structures. M3 and the random structure can usually be directly compared, but neither can easily be directly compared with the small world. This is important when considering the impact of network structure on accuracy, which is presented in Table 2. The table shows the mean accuracy achieved by nodes in each network for each value of a. A series of t-tests (not reported here) were performed on these data which showed small but signi<sup>fi</sup>cant differences between each.

Node accuracy was assessed against the node metrics to determine what made a node good or bad at prediction. The metrics were described earlier but as a reminder they were: degree, betweenness centrality, local clustering and average geodesic length to the critical mass. This last metric is the average shortest path length between a node and each node chosen to be the critical mass, averaged over all simulations. Table 3 presents the relationship between predictive accuracy and each metric. The table indicates the characteristics that nodes which are good at predicting have.

Examining the direction and size of the p-values in the table suggests that node degree and node betweenness, which are similar in concept, have the same impact on node accuracy, although with the Facebook network betweenness, while still positively related to accuracy, is not signi<sup>fi</sup>cantly related to accuracy.<sup>7</sup> The table provides evidence that high clustering deterioriates the ability to predict. The geodesic to the critical mass is signi<sup>fi</sup>cantly and negatively related to accuracy.

## 4.2. Characteristics of the critical mass

Each simulation ended with one of two possible outcomes: success where the simulated phenomenon was shared through the network, and failure where the phenomenon did not spread. It was initially thought that an objective criteria of success would be needed in terms of the number of nodes that eventually chose to share, but in fact this was not the case as there was a clear ‘all or nothing’ demarcation in the outcomes. This is shown in Table 4 along with the results of t-tests demonstrating the difference. Note that this is a product of the choice of x (the size of the critical mass) and the threshold values, and is not a <sup>fi</sup>nding.

Difference between the successful and unsuccessful simulations, as measured by the number of nodes which chose to share. The p-value is from a t-test for a difference in means and shows a signi<sup>fi</sup>cant difference between the two

<table><tr><td rowspan="2"></td><td colspan="2">Success</td><td colspan="2">Failure</td><td rowspan="2">p</td></tr><tr><td>Mean</td><td>sd</td><td>Mean</td><td>sd</td></tr><tr><td>Small world</td><td>485</td><td>26</td><td>150</td><td>83</td><td>0.00</td></tr><tr><td>M3</td><td>256</td><td>9</td><td>22</td><td>3</td><td>0.00</td></tr><tr><td>Random</td><td>279</td><td>8</td><td>23</td><td>3</td><td>0.00</td></tr><tr><td>Facebook</td><td>464</td><td>3</td><td>25</td><td>4</td><td>0.00</td></tr></table>

To examine whether there was anything special about the critical mass in simulations that were successful and in those that were not, a series of t-tests were performed for each network, comparing the metrics of the critical mass with the metrics of nodes that were not the critical mass. The results are shown in Table 5. These data support the notion that the characteristics of the critical mass are important in determining community success or failure. In every network structure, in successful simulations, the degree and betweenness of the critical mass are signi<sup>fi</sup>cantly higher than those nodes that are not part of the critical mass, and in failed simulations the degree and betweenness are signi<sup>fi</sup>cantly lower. Recall that degree and betweenness are each a measure of the ‘importance’ of a node in the network structure. The data suggest that the local clustering of the critical mass is unimportant.

## 4.3. Prediction from a global view

We wanted to see how a node's ability to predict an outcome compares with that of a global view of the network, where the share decisions of all nodes are visible. Intuitively it would seem that the global view will always give a better prediction, and our data support that it almost always does. However even though it was rare, nodes were found that bested a global view. The global view was made by a decision tree using default parameters known to produce reasonable results, and while these could probably have been tweaked to improve accuracy, or other more advanced data mining techniques used in place of a decision tree, the goal was to determine how individual nodes compare with a simple prediction approach that had access to more information.

As the <sup>fi</sup>rst set of simulations achieved a stark distinction between success and failure (Table 4) which would be easy for a global view to predict, a new set of simulations were run with parameters adjusted to give a wider spread in the outcomes. Using only the M3 network this time, new threshold values were created drawn from an N(6,3) distribution, and the size of the critical mass x adjusted from 20 to 45. As before, 1000 simulations were run to produce training data, but this time an additional 500 simulations were run to give a test dataset. Training and testing data are often used in machine learning applications, where both must be generated from the same underlying data generation process. Only the training data is used to set model parameters, in this case build the decision tree and identify the best prediction strategy for individual nodes, as explained next. The model is then tested on the testing data as an independent measure of the performance of the model [8]. The analysis was performed at the tipping point, identi<sup>fi</sup>ed to be $t _ { 1 0 } .$

The accuracy that individual nodes achieved was assessed exactly as before using the training data to identify the best performing strategy.<sup>8</sup> This was then used on the test data to give each node's predictive accuracy. For the global view prediction, a decision tree was created to predict the outcome based on the decisions of all nodes at time period $t _ { 1 0 } ,$ using the training data. The decision tree was built using the data mining software Rattle [68]. The accuracy of this tree was then calculated by using it on the test data. This time, because of the wider spread in outcomes, an objective measure of success in terms of the number of nodes which <sup>fi</sup>nally chose to share was needed. A range of values were used where success was de<sup>fi</sup>ned as 50%, 55% 60% and 65% of nodes which chose to share.

Table 5  
Results of t-tests looking for a difference in node metrics between the critical mass and the other nodes. The tests are split by network and by whether the simulation was successful or not.

<table><tr><td rowspan="2"></td><td rowspan="2">Outcome</td><td colspan="2">Critical mass</td><td colspan="2">Not critical mass</td><td rowspan="2">p</td></tr><tr><td>Mean</td><td>sd</td><td>Mean</td><td>sd</td></tr><tr><td colspan="7">M3</td></tr><tr><td rowspan="2">Degree</td><td>Success</td><td>11.3</td><td>9.3</td><td>9.5</td><td>8.2</td><td>0.00</td></tr><tr><td>Failure</td><td>9.1</td><td>7.8</td><td>9.6</td><td>8.2</td><td>0.00</td></tr><tr><td rowspan="2">Betweenness</td><td>Success</td><td>1314.3</td><td>3947.1</td><td>972.1</td><td>3281.4</td><td>0.00</td></tr><tr><td>Failure</td><td>886.8</td><td>2974.9</td><td>989.9</td><td>3324.5</td><td>0.00</td></tr><tr><td rowspan="2">Local clustering</td><td>Success</td><td>0.58</td><td>0.22</td><td>0.56</td><td>0.23</td><td>0.00</td></tr><tr><td>Failure</td><td>0.6</td><td>0.2</td><td>0.6</td><td>0.2</td><td>0.11</td></tr><tr><td colspan="7">Small world</td></tr><tr><td rowspan="2">Degree</td><td>Success</td><td>10.01</td><td>1.30</td><td>9.98</td><td>1.31</td><td>0.00</td></tr><tr><td>Failure</td><td>1.0</td><td>1.3</td><td>1.0</td><td>1.3</td><td>0.01</td></tr><tr><td rowspan="2">Betweenness</td><td>Success</td><td>629.9</td><td>363.0</td><td>623.4</td><td>363.1</td><td>0.01</td></tr><tr><td>Failure</td><td>621.2</td><td>363.3</td><td>624.6</td><td>363.1</td><td>0.09</td></tr><tr><td rowspan="2">Local clustering</td><td>Success</td><td>0.4</td><td>0.1</td><td>0.4</td><td>0.1</td><td>0.69</td></tr><tr><td>Failure</td><td>0.4</td><td>0.1</td><td>0.3</td><td>0.1</td><td>0.19</td></tr><tr><td colspan="7">Random</td></tr><tr><td rowspan="2">Degree</td><td>Success</td><td>11.5</td><td>9.7</td><td>9.5</td><td>8.2</td><td>0.00</td></tr><tr><td>Failure</td><td>9.2</td><td>7.9</td><td>9.6</td><td>8.3</td><td>0.00</td></tr><tr><td rowspan="2">Betweenness</td><td>Success</td><td>675.9</td><td>1079.1</td><td>480.4</td><td>859.4</td><td>0.00</td></tr><tr><td>Failure</td><td>453.9</td><td>819.7</td><td>489.7</td><td>872.1</td><td>0.00</td></tr><tr><td rowspan="2">Local clustering</td><td>Success</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.88</td></tr><tr><td>Failure</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.47</td></tr><tr><td colspan="7">Facebook</td></tr><tr><td rowspan="2">Degree</td><td>Success</td><td>38.1</td><td>03.7</td><td>36.0</td><td>29.3</td><td>0.00</td></tr><tr><td>Failure</td><td>30.2</td><td>24.2</td><td>36.3</td><td>29.5</td><td>0.00</td></tr><tr><td rowspan="2">Betweenness</td><td>Success</td><td>1376.8</td><td>4192.4</td><td>1291.5</td><td>3812.7</td><td>0.01</td></tr><tr><td>Failure</td><td>1036.1</td><td>3026.9</td><td>1304.8</td><td>3855.1</td><td>0.00</td></tr><tr><td rowspan="2">Local clustering</td><td>Success</td><td>0.56</td><td>0.24</td><td>0.56</td><td>0.24</td><td>0.66</td></tr><tr><td>Failure</td><td>0.56</td><td>0.25</td><td>0.57</td><td>0.24</td><td>0.01</td></tr></table>

Using 60% of nodes as a de<sup>fi</sup>nition of success to illustrate the analysis, the best performing strategy for individual nodes was a = 0.7. Using this approach with the training data, the best performing group of nodes was chosen. In this case, 9 nodes were picked. (Nine were chosen as there was a drop in accuracy between the 9th and 10th best performing node.) The accuracy of these nodes was assessed on the test data (Table 6). When the outcome was de<sup>fi</sup>ned as 55%, and using a proportion approach with a = 30% two nodes actually performed better than the global view prediction. The global view achieved 80.6% accuracy while the two nodes achieved 80.8 and 81.0%. With only two such nodes however it is not possible to examine them statistically.

## 5. Discussion

## 5.1. Overview

In this research we went looking for the network characteristics that would make someone good as sensing what is commonly called the vibe or zeitgeist, even if they do not realize it themselves. The fact that we were not looking for individuals who necessarily knew they could be good at sensing this meant we did not equate ‘liking’ something with predicting that it will be a success: an individual's prediction rule was not the same as their share (threshold) rule. We did this as our interest was in network characteristics (and not how ‘with it’ individuals perceive themselves as being). However this intuitively makes sense — we can all think of things we like even though we know they are not mainstream popular. The scenario considered was one where sharing is binary in that it either happens or does not, and the decision to share was based entirely on the number of friends who have chosen to share.

Table 6  
An illustration showing the accuracy achieved by the top performing nodes in predicting whether at least 60% of all nodes will share when a = 70%, compared with the accuracy achieved by the global view

<table><tr><td>Node ID</td><td>Accuracy (%)</td></tr><tr><td>250</td><td>68</td></tr><tr><td>253</td><td>68</td></tr><tr><td>388</td><td>68</td></tr><tr><td>101</td><td>68</td></tr><tr><td>116</td><td>67</td></tr><tr><td>242</td><td>64</td></tr><tr><td>280</td><td>65</td></tr><tr><td>461</td><td>65</td></tr><tr><td>466</td><td>64</td></tr><tr><td>Global</td><td>76</td></tr></table>

Our main <sup>fi</sup>ndings are as follows. We <sup>fi</sup>nd support for Hypothesis 1: a node's predictive accuracy is negatively related to its geodesic to the nearest member of the critical mass. ‘Important’ people—as measured by network centrality—are best placed to make a prediction, supporting Hypothesis 2. Close knit communities serve to reduce the ability of an individual in them to sense what is going on beyond the community boundaries, supporting Hypothesis 3. Those most able to predict accurately have relatively many friends and those friends are relatively not susceptible to in<sup>fl</sup>uence, answering Hypothesis 4. The characteristics of the critical mass are important in determining a successful outcome: there may be nothing special about the match that starts a forest <sup>fi</sup>re, but where it gets lit matters a lot, which addresses Hypothesis 5.

To begin to discuss these <sup>fi</sup>ndings we must clarify exactly what in the simulations can be compared with validity.

This sort of simulation study allows for relative comparisons of outcomes and an examination of the existence and direction of relationships among variables, but the actual outcomes achieved are usually not meaningful. So for instance, it would not make sense to conclude that nodes in an M3 network can achieve on average z% accuracy as z would be an artifact of the parameters of the simulation and not a property inherent in all M3 networks. Accuracy achieved can be varied up or down by altering the threshold values and the probabilities used to create the M3 network (as described in the Appendix A).

It is possible to compare node metrics and values of a within any one of the network structures, and to compare the existence and direction— but not necessarily the strength—of relationships found between structures. There is also a strong case to directly compare M3 with the random network, as they have identical degree distributions. It is much more dif<sup>fi</sup>cult to justify a direct comparison between M3 and the random network with the small world network. As an explanation of this: there are a high number of potential small world networks with n = 500, and a high number of M3 networks with n = 500 and differences found between any two of them would be unlikely to generalize to the entire population of small world networks and M3 networks which have n = 500. Parameters could be chosen in such a way that M3 outperforms the small world model and vice versa, but to emphasize the point: this would not impact on the existence and direction of relationships among variables.

A similar point must be made about our de<sup>fi</sup>nition of ‘viral’. Typically in the simulations where the phenomenon spread successfully, it spread through 70%+ of the nodes. By any reasonable de<sup>fi</sup>nition, if information spread through 1% or even 0.1% of Twitter or Facebook users, that information would be said to have ‘gone viral’. In fact the 70% <sup>fi</sup>gure is an artifact of our chosen parameters and is not a <sup>fi</sup>nding. It could be moved up or down by varying the x parameter, the size of the critical mass.

This does not limit generalizing our results to cases where spread only occurs through say 1%. We can imagine our 500 nodes being part of a much larger network of 10,000 nodes. In this case, the phenomenon may only spread through less than 5%. If we were able to isolate the 500 as being a community or sub-graph of interest, then our results would be unaffected. Otherwise the relationships would still exist, although they may be harder to identify.

## 5.2. Important individuals with friends in many places

The results in Table 3 suggest a strong relationship between degree and accuracy. This holds even in the small world model which exhibits little variation in degree. The same picture is seen when using betweenness as the measure of importance. The strength of the relationship falls as a increases. This suggests that in order to make an accurate prediction, have many friends and if only a few of them share something then predict that it is going viral.

In order for this to work however, the friends cannot just be anybody — they have to be people who do not know each other. Tight communities—those with high clustering—have a negative impact on ability to predict. The M3 network shows preferential attachment, high clustering and high assortativity, the random network shows preferential attachment but not clustering or assortativity. The random network achieves a higher average accuracy than M3 (as seen in Table 2). This difference is therefore due to clustering or assortativity. At the node level, in networks which exhibit clustering, nodes which have high local clustering are worse at prediction than others (as seen in Table 3). This suggests that it is clustering which is producing the negative effect, something likely caused by the spread of a phenomenon around a cluster tending to trigger a prediction rule when in fact the phenomenon is not spreading far around the rest of the network.

Table 3 suggests that the friends of those best placed to predict accurately have relatively high thresholds, in other words, they are not susceptible to in<sup>fl</sup>uence. Such friends tend to act as a <sup>fi</sup>lter revealing only the phenomena most likely to go viral.

Assortativity appears to have little impact on ability to predict. This can be seen in Table 3 by comparing the signi<sup>fi</sup>cance and direction of p-values between M3 which exhibits assortativity with both the small world and random networks which do not. There is no effect in M3 which does not appear in one or both of the others.

Finally, the impact of path length is on limiting the time period in which a node can perceive the phenomenon as it spreads, supporting Hypothesis 1. This is not an important <sup>fi</sup>nding, and in any case social network average path lengths are very low (Facebook's is reported to be 3.7 [9]), but it is somewhat interesting.

The Facebook graph was used as a robustness check on results and as shown in Table 3, relationships seen between node metrics and predictive accuracy in Facebook are almost identical to those seen in M3, with the exception of susceptibility of friends (as measured by their threshold) which was not related to accuracy in the Facebook graph, but was in M3.

## 5.3. The critical mass and the global view

Considering Hypothesis 5, which concerned the characteristics of the critical mass, the data show a clear relationship between importance of the critical mass in network structure as measured by degree and betweenness, and determining the success or failure of the spread of the phenomenon. As reviewed in Section 2, opinion in the literature on this is mixed but this study suggests that where the critical mass sits in the network is important in determining success.

The analysis of the global view was largely just for interest but it suggests that it is possible to <sup>fi</sup>nd nodes that are very good at making a prediction. Unfortunately it is not yet possible to explain with certainty why they can do this, and future work should examine this further.

## 5.4. Implications for research

Much of the work in this area studies how information spreads around a social network, often trying to identify what makes an individual a good in<sup>fl</sup>uencer or someone who is susceptible to in<sup>fl</sup>uence. By contrast this research has examined making a prediction about whether a phenomenon will go viral, and we separated each individual's decision about whether they choose to like the phenomenon and whether they think it will go viral. This opens up a new line of enquiry that could prove a useful addition to the area, the study of ‘sensing’ what is going on in a wider community from observing friend's behavior. Several new research questions present themselves. Here we studied network characteristics while holding individual characteristics constant but it may be useful to study both together to determine how individual characteristics impact on network characteristics and vice versa (this is not new although there are still many unanswered questions here), and how both interact to increase or decrease ability to predict. Another key area is in relationship weight. Individuals will put more stock in the behavior of some friends than others and it is an open question as to what in<sup>fl</sup>uences this decision and the impact it has. The software created to run our simulations is a platform that could be used to study these, perhaps supported by data collected in the <sup>fi</sup>eld. Likewise, the M3 algorithm creates a network that has the properties of real social networks which could be useful in future research. Code for both is available from the author.

## 5.5. Implications for practice

This is an early study into technology that allows recommendations to be made to friends via online social networks. The technology is rapidly evolving and is not yet well understood by users. How it will develop is uncertain. The implications of this research for organizations and individuals are therefore dif<sup>fi</sup>cult to properly assess. However one obvious application of these ideas lies in monitoring viral marketing campaigns. Viral marketing attempts to use pre-existing social networks to create brand awareness or product sales through processes that encourage information about the brand to be shared. With access to information about a social network graph, or even part of it, it may be possible to identify individuals who are well placed to determine whether a new campaign is working early on and allow marketers to adjust their strategy appropriately. The results of this study may also help marketers identify who to target to encourage them to join the critical mass, something which is already an active research area.

Other potential applications might be found for organizations wishing to keep abreast of current trends in a situation where data on network structure is available but data on the activity of network members is limited, or for those wishing to encourage knowledge sharing among a network of employees by manipulating that network via a mechanism such as of<sup>fi</sup>ce allocation.

## 5.6. Limitations and future research directions

The model of in<sup>fl</sup>uence used here is based on three assumptions: that share signals are sent to all friends, that the critical mass is spread uniformly through the network and that threshold values are normally distributed. Each of these potentially limits the generalisability of the results and should be addressed in future research. The <sup>fi</sup>rst could be dealt with by adding a relationship ‘weight’ as described below. The second may be an unrealistic assumption but we would only expect it to impact on our results for Hypothesis 5, about the characteristics of the critical mass. We would still expect our other results to hold.

The last assumption should also not impact on our main results unless we believe that individuals' thresholds impact on network structure. While perhaps unlikely it should be noted that this is indeed possible — individuals may choose to create friendships with others who have similar levels of susceptibility to in<sup>fl</sup>uence as them. Again future work should examine this in detail.

```prolog
g <- simplify(g, remove.multiple = TRUE, remove.loops = TRUE).
```

In the scenario studied here, individuals are modeled as having responded positively to something (by listening to a song, using an app, reading an article) and then behind the scenes the social media service they are using shares this fact with their friends. This removes consideration of all attitudes toward the phenomenon under question — it does not matter if the individual actually enjoyed the song, app or article once they had listened to it, used it or read it. Future research could determine if and how our results generalize to scenarios where enjoyment does matter (but in fact as described in Section 2 the scenario we studied is so common that it is of interest in its own right).

One criticism leveled at similar work (see for example [65]) is that results are ‘just based on simulation’ and cannot apply in the real world. Simulation is an important tool in the study of network science as it allows for the creation and manipulation of identical network structures and nodes in those networks. This study does not take into account human aspects such as mood and personal preferences but this is not a weakness as it means that the real element of interest, network attributes, can be studied without introducing the confounds of these additional aspects. There is nothing limiting the generalizing of these results to real world networks unless we believe that mood, personal preferences and other human aspects are not distributed evenly through social networks. Having said that, and as mentioned earlier, one interesting ‘human aspect’ that could and should be examined in future work is the in<sup>fl</sup>uence of particular friends, where one friend is ‘listened to’ more than others — seeing that one friend has listened to a song might make an individual more likely to listen to it than seeing that a different friend listened to it. This could be achieved by varying the prediction rule to give more or less weight to different friends.

One last area for future research is examining different share rules. The threshold rule we used is just one possible model and others do exist, and each probably applies in certain contexts (compare for instance sharing a song with sharing news of a terrorist attack). Future research should examine how choice of diffusion model impacts on results.

## Appendix A. Network parameters and algorithm

## A.1. A small world mode

Conceptually, the small world network is set up by arranging n nodes in a circle and connecting each to a certain number of nodes to one side of it, and then randomly selecting and rewiring edges to randomly selected nodes [66]. This results in high clustering (from the initial con<sup>fi</sup>guration of the edges) and short path lengths (from the rewired edges). The small world network used in this study was created in R using the igraph package with the following code (included to allow replication):

![](/api/attachments/ATYGAAHW/fulltext/images/5132b2bd380894face076d05d0da656b9c5dbfa97c0fd14b58f6bb992bc5efd1.jpg)

The re-wiring probability of 0.1 (the fourth parameter in the <sup>fi</sup>rst line of code) has been found in past studies to create networks with clustering and path lengths comparable real social networks [11].

## A.2. M3

M3 is similar to a model of network formation presented by [33]. The algorithm to create M3 is as follows (R code is available from the author):

```python
Set n = 1
Set ClusterNet[1,1] = n
For i = 1 to NetworkSize.
    Set n = n + 1
    Set m to random(1:n)
    Set Clusters to be all columns in ClusterNet that contain m
    Set HighProbCluster to random(1:Clusters)
    Add m,n to edgelist
    For j = 1 to length(HighProbCluster).
    If binomial(highprobability) = 1
    Then add HighProbCluster[j],n to edgelist.
    Set LowProbClusters all Clusters-HighProbCluster
    For k = 1 to count(LowProbClusters).
    For l = 1 to length(LowProbClusters[k]).
    If binomial(lowprobability) = 1.
    Then add LowProbCluster[k,l],n to edgelist.
    ClusterNet[1,n] = n.
```

This network has been grown up to 20,000 nodes and consistently exhibits higher than random clustering with a similar clustering coef<sup>fi</sup>- cient to Watts–Strogatz models and path lengths similar to Watts– Strogatz and the Barabási–Albert model. Sub-groups do not get unrealistically high. The largest in the model of 20,000 was around 100. The network exhibits preferential attachment as shown in Fig. 4. The <sup>fi</sup>gure compares degree distribution in M3 with 8,000,000 Facebook users. For this study, ‘highprobability’ was set to 0.7, ‘lowprobability’ was 0.4.

![](/api/attachments/ATYGAAHW/fulltext/images/67b54171b9dff34be7949fc5f13e45b61ff4d6a926724e5f47b63b4f2b744665.jpg)  
Fig. 4. Log–log plot showing degree distribution in M3 (left) and Facebook. The Facebook data is not the sample that was used in this study but was data on 8,000,000 users, taken from [14]. The <sup>fi</sup>gure is only intended to show a trend in M3 and Facebook that the ‘few know many, the many know few’, which was the de<sup>fi</sup>nition of preferential attachment in Section 2. Note that if the degree distribution followed a power law the data would follow a straight line exactly Note also that we would only expect to see power law behavior in the middle section of the data [20]. For those wanting to directly compare the two, notice the differing y scale.

## A.3. A random model

The following igraph code was used to create a con<sup>fi</sup>guration model with the same node degrees as M3, but with the edges created randomly:

g b- degree.sqeuence.game(degree(M3))

g b- simplify(g, remove.multiple = TRUE, remove.loops = TRUE).

## References

[1] A.S. Abrahams, J. Jiao, W. Fan, G.A. Wang, Z. Zhang, What's buzzing in the blizzard of buzz? automotive component isolation in social media postings, Decision Support Systems 54 (4) (2013) 871–882.

[2] A.S. Abrahams, J. Jiao, G.A. Wang, W. Fan, Vehicle defect discovery from social media, Decision Support Systems 54 (1) (2012) 87–97.

[3] S. Aral, D. Walker, Creating social contagion through viral product design: a randomized trial of peer in<sup>fl</sup>uence in networks, Management Science 57 (9) (2011) 1623–1639.

[4] S. Aral, D. Walker, Identifying in<sup>fl</sup>uential and susceptible members of social networks, Science 337 (6092) (2012) 337–341.

[5] W.S. Bainbridge, The Warcraft Civilization, MIT Press, 2010.

[6] E. Bakshy, B. Karrer, L.A. Adamic, Social in<sup>fl</sup>uence and the diffusion of user-created content, Proceedings of the 10th ACM Conference on Electronic Commerce. EC '09, ACM, New York, NY, USA, 2009, pp. 325–334

[7] A. Barabási, R. Albert, Emergence of scaling in random networks, Science 286 (1999) 509–512.

[8] D. Barber, Bayesian Reasoning and Machine Learning, Cambridge University Press 2012.

[9] BBC, Facebook users average 3.74 degrees of separation , URL http://www.bbc.co.uk news/technology-158442302011.

[10] J. Bermudez, Cognitive Science, Cambridge University Press, 2010.

[11] J. Bruggeman, Social Networks, Routledge, 2008.

[12] R. Burt, The contingent value of social capital, Administrative Science Quarterly 42 (2) (1997) 339–365.

[13] R. Burt, Social capital: theory and research, Aldine Transaction, Ch. Structural Holes Versus Network Closure as Social Capital, 2001.

[14] S. Catanese, P. De Meo, E. Ferrara, G. Fiumara, A. Provetti, Crawling Facebook for social network analysis purposes Proceedings of the International Conference on Web Intelligence, Mining and Semantics, ISBN: 978-1-450-30148-0, May 25–27 2011, pp. 52:1–52:8.

[15] D. Centola, The spread of behavior in an online social network experiment, Science 329 (5996) (2010) 1194–1197.

[16] D. Centola, An experimental study of homophily in the adoption of health behavior, Science 334 (6060) (2011) 1269–1272.

[17] D. Centola, M. Macy, Complex contagions and the weakness of long ties, The American Journal of Sociology 113 (3) (2007) 702–734.

[18] C. Cheung, M. Lee, A theoretical model of intentional social action in online social networks, Decision Support Systems 49 (2010) 24–30.

[19] C.-M. Chiu, M.-H. Hsu, E.T. Wang, Understanding knowledge sharing in virtual communities: an integration of social capital and social cognitive theories, Decision Support Systems 42 (3)(2006) 1872-1888.

[20] A. Clauset, C. Shalizi, M. Newman, Power-law distributions in empirical data, SIAM Review 51 (4) (2009) 661–703.

[21] G. Cumming, Understanding the New Statistics, Routledge, 2011.

[22] T. Dierkes, M. Bichler, R. Krishnan, Estimating the effect of word of mouth on churn and cross-buying in the mobile phone marker with markov logic networks, Decision Support Systems 51 (2011) 361–371.

[23] P.S. Dodds, D.J. Watts, Universal behavior in a generalized model of contagion, Physical Review Letters 92 (21) (2004).

[24] D. Easley, J. Kleinberg, Networks, Crowds and Markets, Cambridge University Press, 2010.

[25] In: J. Forgas, K. Williams (Eds.), Social In<sup>fl</sup>uences: Direct and Indirect Processes, Psychology Press, 2001.

[26] L. Freeman, Centrality in social networks conceptual clari<sup>fi</sup>cation, Social Networks 215 (1978).

[27] A. Galstyan, V. Musoyan, P. Cohen, Maximizing in<sup>fl</sup>uence propagation in networks with community structure, Physical Review E 79 (5) (2009).

[28] M. Granovetter, Threshold models of collective behavior, The American Journal of Sociology 83 (6) (1978) 1420–1443.

[29] Z. Guo, Optimal decision making for online referral marketing, Decision Support Systems 52 (2) (2012) 373–383.

[30] S. Hill, F. Provost, C. Volinsky, Network-based marketing: identifying likely adopters via consumer networks, Statistical Science 21 (2) (2006) 256–276.

[31] C. Hoofnagle, J. King, Consumer information sharing: where the sun still don't shine, Tech. rep., Samuelson Law, Technology & Public Policy Clinic, UC Berkeley, December 2007, (URL http://www.truststc.org/pubs/323.html).

[32] M. Jackson, Social and Economic Networks, Princeton University Press, 2008.

[33] M. Jackson, B.W. Rogers, Meeting strangers and friends of friends: how random are social networks? American Economic Review 97 (3) (2007) 890–915.

[34] M.O. Jackson, D. López-Pintado, Diffusion and contagion in networks with heterogeneous agents and homophily, 2011. , (CoRR abs/1111.0073).

[35] E. Katz, P. Lazarsfeld, Personal In<sup>fl</sup>uence: The Part Played by People in the Flow of Mass Communications Transaction Publishers. 1955

[36] M. Keith, H. Demirkan, M. Goul, The in<sup>fl</sup>uence of collaborative technology knowledge on advice network structures, Decision Support Systems 50 (1) (2010) 140–151.

[37] D. Kempe, J. Kleinberg, E. Tardos, Maximizing the spread of in<sup>fl</sup>uence through a social network, Proceedings of the ninth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. KDD '03, ACM, 2003, pp. 137–146.

[38] C. Kiss, M. Bichler, Identi<sup>fi</sup>cation of in<sup>fl</sup>uencers — measuring in<sup>fl</sup>uence in customer networks, Decision Support Systems 46 (1) (2008) 233–253.

[39] L. Kuandykov, M. Sokolov, Impact of social neighborhood on diffusion of innovation s-curve, Decision Support Systems 48 (4) (2010) 531–535.

[40] P. Lazarsfeld, The People's Choice: How the Voter Makes up his Mind in a Presidential Campaign, Columbia University Press, 1968.

[41] Y.-M. Li, Y.-L. Shiu, A diffusion mechanism for social advertising over microblogs, Decision Support Systems 54 (1) (2012) 9–22

[42] G. Marwell, P. Oliver, The Critical Mass in Collective Action: A Micro-social Theory, Cambridge University Press, 1993.

[43] J.J. McAuley, J. Leskovec, Learning to discover social circles in ego networks, Neural Information Processing Systems, 2012.

[44] S. Milgram, The small world problem, Psychology Today 2 (1967) 60–67.

[45] J. Miller, S. Page, Complex Adaptive Systems, Princeton University Press, 2007.

[46] S. Mudambi, D. Schuff, What makes a helpful online review? A study of customer reviews on amazon.com, MIS Quarterly 34 (1) (2010) 185–200

[47] M. Newman, Networks an Introduction, Oxford University Press, 2010

[48] M.E.J. Newman, J. Park, Why social networks are different from other types of networks, Physical Review E 68 (3) (2003) 036122

[49] D.D.S. Price, A general theory of bibliometric and other cumulative advantage processes, Journal of the American Society for Information Science (1976) 292–306.

[50] E. Rogers, Diffusion of Innovations 4th Edition, Free Press, New York, NY, USA, 1995.

[51] H. Rui, Y. Liu, A. Whinston, Whose and what chatter matters? The effect of tweets on movie sales, Decision Support Systems 55 (4) (2013) 863–870.

[52] M. Salganik, D. Watts, Leading the herd astray: an experimental study of self-ful<sup>fi</sup>lling prophecies in an arti<sup>fi</sup>cial cultural market, Social Psychology Quarterly 71 (4) (2008) 338–355.

[53] G. Sargut, R. McGrath, Learning to live with complexity, Harvard Business Review 89 (9) (2011) 68–76, (136).

[54] T.C. Schelling, Dynamic models of segration, Journal of Mathematical Sociology 1 (1971).143-186

[55] D.B. Stouffer, R.D. Malmgren, L.A.N. Amaral, Comment on Barabasi, Nature 435 (Oct. 2005) 207, ((2005). ArXiv Physics e-prints).

[56] M.P.H. Stumpf, M.A. Porter, Critical truths about power laws, Science 335 (6069) (2012) 665-666

[57] A.A. Tako, S. Robinson, The application of discrete event simulation and system dynamics in the logistics and supply chain context, Decision Support Systems 52 (4) (2012) 802–815.

[58] O. Toubia, E. Johnson, T. Evgeniou, P. Delqui, Dynamic experiments for estimating preferences: an adaptive method of eliciting time and risk parameters, Management Science (2012), (in press).

[59] T. Valente, Network Models of the Diffusion of Innovations, Hampton Press, 1995

[60] C. Van den Bulte, Y.V. Joshi, New product diffusion with in<sup>fl</sup>uentials and imitators, Marketing Science 26 (3)(2007) 400–421.

[61] R. van der Lans, G. van Bruggen, J. Eliashberg, B. Wierenga, A viral branching model for predicting the spread of electronic word of mouth, Marketing Science 29 (2) (2010) 348–365.

[62] M.M. Wasko, R. Teigland, S. Faraj, The provision of online public goods: examining social structure in an electronic network of practice, Decision Support Systems 47 (3) (2009) 254–265.

[63] S. Wasserman, K. Faust, Social Network Analysis: Methods and Applications, Cambridge University Press, 1994.

[64] D. Watts, Everything is Obvious, Atlantic Books, New York, NY, USA, 2011.

[65] D. Watts, P. Dodds, In<sup>fl</sup>uentials, networks and public opinion formation, Journal of Consumer Research 34 (2007).

[66] D. Watts, S. Strogatz, Collective dynamics of ‘small world’ networks, Nature 393 (1998) 440–442.

[67] D. West, Introduction to Graph Theory, Prentice Hall, 1996.

[68] G. Williams, Data Mining with Rattle and R, Springer, 2011.

[69] Y.C. Xu, C. Zhang, L. Xue, Measuring product susceptibility in online product review social network, Decision Support Systems (2013), http://dx.doi.org/10.1016/ j.dss.2013.01.009.

[70] X. Zheng, S. Zhu, Z. Lin, Capturing the essence of word-of-mouth for social commerce: assessing the quality of online e-commerce reviews by a semi-supervised approach, Decision Support Systems 56 (2013) 211–222.

Thomas Chesney's research examines the behavior of networked individuals. He is a lecturer in information systems at Nottingham University Business School and has a PhD in Information Systems from Brunel University, an MSc in Informatics from Edinburgh University, and a BSc in Information Management from the Oueen's University of Belfast. His research has appeared in numerous peer reviewed journals including the Information Systems Journal and the International Journal of Human Computer Studies. He is co-author of Fundamentals of Business Information Systems, published by Cengage Learning.
