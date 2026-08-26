---
otero_id: 12988
otero_key: "H48QAKDK"
title: "The Evolution of Interaction Networks in Massively Multiplayer Online Games"
authors: "Johannes Putzke; Kai Fischbach; Detlef Schoder; and Peter A. Gloor"
year: "2010"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00221"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Jourņal of the Asşociation for Information Systems JAIS

Special Issue

# The Evolution of Interaction Networks in Massively Multiplayer Online Games\*

Johannes Putzke University of Cologne putzke@wim.uni-koeln.de

Kai Fischbach

University of Cologne

fischbach@wim.uni-koeln.de

Detlef Schoder

University of Cologne

schoder@wim.uni-koeln.de

Peter A. Gloor

pgloor@mit.edu

Massachusetts Institute of Technology (MIT)

## Abstract

This article examines the co-evolution of players’ individual performance and their interaction network in a Massively Multiplayer Online Game (MMOG). The objective is to test whether the application of theories from the real world is valid in virtual worlds. While the results indicate that the structural effects and demographic variables active in the real world influence the evolution of the players’ interaction network in MMOGs (e.g. transitivity, reciprocity, and homophily), they do not provide evidence that players’ structural embeddedness in the interaction network influences player performance. These findings have important implications for researchers and practitioners who need to understand social processes in MMOGs (e.g., when launching marketing campaigns in MMOGs) or who study MMOGs and then use their findings to draw conclusions about the real world (e.g., when analyzing the relationship between employee performance and network structure).

Keywords: actor-based model, exponential random graph model, massively multiplayer online game, MMOG, performance, SIENA, social capital, social network analysis.

Harri Oinas-Kukkonen, Kalle Lyytinen, and Youngjin Yoo were the guest editors of the special issue.

Volume 11, Special Issue, pp. 69-94, February 2010

# The Evolution of Interaction Networks in Massively Multiplayer Online Games

## 1. Introduction

Massively Multiplayer Online Games (MMOGs) are video games played on the Internet simultaneously by hundreds or thousands of players. Over the last few years, MMOGs have increasingly attracted the attention of players, software developers, media, enterprises and researchers and gained in commercial relevance.

World of Warcraft, the most popular MMOG in the Western hemisphere, was launched in 2005 and today is played by about 10 million active players worldwide. They pay a subscription fee of \$13-\$15 each month and spend about 374,000 hours each day (i.e., 50,000 person-days) playing (Teigland, 2007). As early as 2001, Castronova (2001) calculated that the value of virtual property produced by the players of Everquest in the virtual world Norrath corresponded to a per-capita GDP of \$2,266 (which is greater than that of China and India and roughly equal to that of Russia). Lineage II – the counterpart to World of Warcraft in Asia – has more than 14 million registered users. Second Life has more than 20 million registered (not necessarily active) accounts and up to 60,000 users logged in at any given time. Bray and Konsynski (2007) note that in June 2007 players in Second Life exchanged an average of \$1.7 million daily, and players from Entropia Universe can withdraw money from their virtual accounts at real-world ATMs.

Despite the high commercial relevance of MMOGs and the fact that they have been on the research agenda for more than a decade, they have been the subject of surprisingly little research (e.g., Parks and Floyd, 1996, term MMOGs as MUDs, MOOS, MUSHES, and VEE).<sup>2</sup> In the relatively few studies that have been conducted on MMOGs, authors discuss, for example, legal aspects (e.g., Glushko, 2007; Jenkins, 2004; Jian, 2007; Lastowka and Hunter, 2004; MacInnes, 2006), systems design (e.g., Jiang et al., 2007; Meng and Long, 2006), negative (health) consequences (e.g., Messerly, 2004; Smyth, 2007; Yao-Chung, 2006), and marketing within MMOGs (e.g., Castronova, 2005; Edery, 2006; Hemp, 2006a; Hemp, 2006b).

Not much is yet known about the evolution of the interaction network of players participating in MMOGs. Which factors determine this evolution? Are findings from studies that examine the evolution of interaction networks in the real world also valid in MMOGs? Answers to these questions are quite relevant for the analysis of MMOGs by practitioners and scholars alike; the reasons fall into three general categories.

First, game designers need to understand the factors that lead to repeated interaction between the players in MMOGs. Several studies (e.g., Kim et al., 2005) provide evidence that the social characteristics of online games are more crucial than their technological characteristics to commercial success. Understanding these factors allows game designers to implement functions in the games that are valued by players and boost commercial success.

Second, marketing managers and researchers need to understand whether real-world partner selection theories for repeated interaction are also valid in MMOGs. MMOGs will increasingly be used for marketing and new forms of advertising (e.g., Castronova, 2005; Edery, 2006; Hemp, 2006a; Hemp, 2006b). Before launching marketing campaigns in MMOGs, managers need to know whether their experiences and knowledge from the real world about the structural characteristics of social networks, word-of-mouth processes, lead user identification, and the diffusion of innovations is a solid basis for decision-making in MMOGs, or whether new theories need to be developed for MMOGs.

Third, if theories regarding partner selection for repeated interaction from the real world are found to be valid in MMOGs, it is reasonable to assume that future theories about the selection of partners for repeated interaction tested with MMOG data are, conversely, valid in the real world.<sup>3</sup> Developing theories with MMOG data has numerous advantages: analysts can record all interactions in MMOGs (text chat, voice chat, asynchronous messaging, forums, etc.), as well as all player actions. Therefore, the threats to data reliability that are typically discussed in the literature can be weakened (e.g., the social desirability bias, question order effects, memory effects, inter-observer reliability, interviewer distortion, and the Hawthorne effect). Furthermore, in many instances, study participants are more likely to allow access to their game data than to their real-life data. (For example, individuals might be resistant to provide individual performance data.) Hence, it may be possible to test theories about social selection and influence with MMOG data that are more difficult to test with real-world data due to privacy issues (e.g., theories about the relationship between network structure and employee performance).

This article, which answers these questions, is structured as follows. Section 2, Theoretica Background, reviews the related literature that examines social interactions and player performance in MMOGs, and illustrates the reasons for extending this stream of research. In the same section, we highlight theories that explain social selection and influence in the real world (with a focus on the IS literature). In Section 3, Hypotheses, we develop 10 research hypotheses to test the findings of these theories in MMOGs. Section 4, Methodology, describes the data collection and method employed. The Results section (Section 5) highlights the findings. Finally, Section 6, Conclusions, discusses the theoretical and managerial implications of the findings, notes their limitations, and provides some suggestions for further research.

## 2. Theoretical Background

## 2.1. Interaction and Performance in Massively Multiplayer Online Games

There are only a few studies that analyze factors leading to interaction and player performance in MMOGs. A first set of studies analyzes data from self-reported surveys, observations, or experiments; a second set analyzes in-game data.

Within the first set, two large-scale studies (Cole and Griffiths, 2007; Whang and Chang, 2004) survey MMOG players regarding factors that lead to repeated interactions with other players (n = 912 and n = 4,786). Cole and Griffiths (2007) mainly provide descriptive statistics about the respondents demographics and occupational status, type of MMOG played, number of hours played per week, repeated interactions between players (e.g., friendship between players, issues discussed among online friends, attraction to other players, playing together with real life friends and family) and motivations for playing. Whang and Chang (2004) classify three different “lifestyles” of players in the MMOG Lineage: single-oriented, community-oriented, and off-real world player. Single-oriented players do not appreciate the social network features of MMOGs but rather use MMOGs as just another video game and play online, while community-oriented players use the social network features of MMOGs to cooperate and communicate with others. Off-real world players are inclined to harm others and create social problems in MMOGs. Further, they Wang and Chang identify distinct differences in player values, game activities, personalities, and socio-economic status within the MMOG. Nardi et al. (2007) conduct ethnographic field work and observes a learning culture in World of Warcraft that is rather descriptive. The authors find that questions posed a public chat are answered within nine seconds to approximately three minutes, with an average of 32 seconds. While all three studies certainly provide useful insights about player interaction in MMOGs, they do not test any formal hypotheses.

There are at least two initial steps toward testable hypotheses. Experiments have found that a player’s immersion in networked environments has no influence on the percentage of time he or she spent in conversation with other players (Galimberti et al., 2001) and that task- and rewardinterdependency in games influence players’ perceived performance, but not their objective performance (Choi et al., 2007). However, neither work tests a complete model of social selection and influence. Such a model has been proposed, for example, by Guo and Barnes (2007). Their model would examine the determinants of player behavioral intentions with respect to virtual item transactions. However, they do not test their model, but rather highlight a research agenda for 2007- 2015.

So, a gap remains in our knowledge without a model to test formal hypotheses about social selection and influence in MMOGs. We propose such a model in this paper. To test the model, we follow the approach of the second set of studies. These studies do not collect data by surveys or observations, but rather by analyzing (archival) data directly from games. Hence, their measures are more highly reliable.<sup>4</sup> For example, Yee et al. (2007) examine player interaction in the MMOG Second Life. Six research assistants collected data over a seven-week period by triggering a script near locations in Second Life where at least two people were interacting. Duchenaut et al. (2006) analyze data from the MMOG World of Warcraft and highlight the extent of social activities in MMOGs. Again, however, neither study tests a formal theory regarding social selection and influence in MMOGs.

## 2.2. Theories of Social Selection and Influence

Anecdotal evidence and case studies do not yet allow for drawing any conclusions about how formal theories of social selection and influence from the real world apply to online social structures (Butler, 2001). Consequently, there is still an ongoing debate as to whether online ties are less valuable than offline ones (e.g., Cummings et al., 2002). An initial study by Noy et al. (2006) illustrates how games and simulations related to Computer-Mediated-Communication can be used to study and validate theoretical constructs from social theories and, thus, provides a basis for this kind of analysis.

The following paragraphs review formal theories of social selection and influence that form the basis for our proposed model.

Most theories of social selection and influence have been published under the umbrella of “social network analysis” (for an introduction, see Wasserman and Faust, 1994), which incorporates several methods and techniques to analyze social structures that emerge from the interaction among and between human actors. Social network analysis is an interdisciplinary research paradigm that combines sociology, anthropology, communication science, economics, physics, management science, and computer science. It is a highly intriguing topic, one which the IS community began to pay greater attention to with the awarding of the “MISQ Paper of the Year” to Lamb and Kling’s study titled “Reconceptualizing users as social actors in information systems research” in 2003 (Lamb and Kling, 2003). This paper focuses on two different research streams from social network analysis. The first stream considers the evolution of social networks, while the second research stream examines the association between an actor’s performance and his/her embeddedness within a social network.

In the first stream, early models that examined the evolution of social networks (for an introduction, see Doreian and Stokman, 1997) mainly explore how structural characteristics of networks (such as transitivity, reciprocity and degree-prestige) influence the process of network evolution (see, e.g., Wasserman and Pattison, 1996). Recent developments in this kind of model (see, e.g., Robins et al., 2007) now also allow for the integration of several actor characteristics. These actor characteristics are even allowed to co-evolve with the social network over time (e.g., Snijders et al., 2007), so that the social network (and the actor characteristics) can be dependent and independent variables concurrently. Hence, these models allow for statistical tests of causal relationships between network structure and actor characteristics that were not previously possible.

In this context, one of the most promising research approaches may be the integration of an actor’s individual performance characteristics into these models. This leads to the second research stream of social network analysis highly relevant to this paper: that which examines the relationship between an actor’s embeddedness within a social network and his/her individual performance. This stream is often called “social capital” research (e.g., McLure Wasko and Faraj, 2005). Bourdieu was the first to mention social capital as the “sum of the resources, actual or virtual, that accrue to an individual or a group by virtue of possessing a durable network of more or less institutionalized relationships of mutual acquaintance and recognition” (Bourdieu and Wacquant, 1992, p. 119). Burt calls socia capital a “metaphor about advantage,” meaning “that the people who do better are somehow better connected. Certain people or certain groups are connected to certain others, trusting certain others, obligated to support certain others, dependent on exchange with certain others. Holding a certain position in the structure of these exchanges can be an asset in its own right. That asset is social capital, in essence, “a concept of location effects in differentiated markets” (Burt, 2000, p. 347).

Summarizing the work of foundational social capital researchers, we define social capital in this study as the value of social structures (e.g., frequent interactions and their properties) and their consequences for an actor’s performance. For our definition, social capital involves issues such as trust, shared cognitive models, and the ability to process complex information. It emerges in successful social interactions and functions as a resource that, for example, enables social structures.

Several IS researchers employ social capital as a central concept in their studies. For example, Robert et al. (2008) demonstrate how the three dimensions of social capital (structural, relational, and cognitive) influence a team’s ability to integrate knowledge and lead to better team performance (measured as team decision quality). Wonseok et al. (2005) analyze a social network of co-authors publishing in four leading IS journals and illustrate how interdisciplinary collaboration contributes to knowledge capital. Finally, Teigland and Wasko (2009) examine how intrinsic motivations and knowledge sourcing affect individual centrality and the performance of workers in multinational corporations.

Interactions on the Internet and in MMOGs, however, certainly differ from interactions in the real world. For instance, Jones et al. (2004) analyze postings to newsgroups and find that users cope with information overload by responding to simpler messages, and by generating simpler responses. Therefore, it remains unclear whether findings from studies aimed at explaining social selection and influence in the real world are valid in MMOGs. In a similar vein, Ahuja and Carley (1999) state as early as 1999 that new theories should be developed to explain actual performance in virtual organizations, although existing theories of structure and perceived performance can be expanded to virtual organizations. That call for research is no less timely today. Further, most models do not account for endogeneity of network variables and performance. Hence, we integrate an actor’s individual performance as an antecedent to, as well as an outcome of, network structure our model of network evolution.

## 3. Hypotheses

We structure the development of our research hypotheses in four parts. In the first part, we propose four hypotheses that examine the effects of endogenous <sup>5</sup> network variables on the process of network evolution. In the second part, we propose hypotheses to explain the influence of actors’ actual demographic characteristics (sex and age) on network evolution. The third part presents three hypotheses regarding performance as an antecedent to network evolution. In the fourth part, we propose three hypotheses to explain performance as an outcome of network structure.

## 3.1. Endogenous Network Effects

The first four hypotheses examine whether theories about interaction networks in the real world are also valid in MMOGs. In a highly influential paper, Contractor et al. (2006) review theories regarding the structural tendencies of interaction networks and develop a multitheoretical multilevel (MTML) framework for the examination of network dynamics. In their MTML framework, the authors identify endogenous variables and theories at four different levels of analysis: global, triadic, dyadic, and actor. They recommend that models of network formation should not focus on a single level of analysis, but rather should seek to incorporate several levels of analysis into one model. Following this recommendation, we identify four potential endogenous network effects at different levels of analysis.

At the actor level of analysis, we hypothesize that there are some costs associated with maintaining and building up partnerships for repeated interaction (c.f. Bolton and Dewatripont, 1994). Consequently, players who already interact repeatedly with many other players are less likely to seek new partners for repeated interaction. Numerous studies that examine the scale-free property of social networks (e.g., Barabási and Albert, 1999) and models of dynamic network evolution (e.g., Snijders et al., 2007) support this finding. Hence,

H1. Players have a very low general tendency to seek players as partners for repeated interaction who do not have attributes or a joint network embeddedness that are favorable to interacting repeatedly, that is, the higher the number of a player’s partners for repeated interaction, the lower the likelihood that he or she will seek partners for repeated interaction.

At the dyadic level of analysis, Contractor et al. (2006) highlight several theories that hypothesize mutual/reciprocated ties. These include social exchange theory (e.g., Blau, 1986), resource dependency theory (Pfeffer and Salancik, 1978), and network exchange theory (e.g., Willer, 1999). Other IS researchers have found reciprocal effects in online learning networks (Aviv and Ravid, 2005). Following this argument, we hypothesize,

H2. There is a greater likelihood that one player seeks another player as a partner for repeated interaction if the other player also seeks the first player as a partner for repeated interaction.

At the triadic level of analysis, several theories such as network closure theory (Coleman 1988) and balance theory (Heider, 1982) suggest a tendency for transitive triplets (c.f. Contractor et al., 2006). A triplet is transitive if player i seeks to interact repeatedly with player j, player i seeks to interact repeatedly with player l, and player j and l seek to interact repeatedly with each other (for a detailed discussion, see Holland and Leinhardt, 1970). In other words, over time an individual tends to become a friend of his or her friends. Hence, we hypothesize,

H3. The likelihood that a player seeks a partner for repeated interaction by closing a transitive triplet is higher than the likelihood of seeking a random interaction tie.

At the actor level of analysis, one of the most relevant endogenous effects is the effect of an actor’s prestige (sometimes also called deference, status, or popularity), which is defined as an actor’s number of incoming links (Wasserman and Faust, 1994). Individuals with higher prestige generally have greater access to, and control of, relevant resources, and thus more people seek to interact repeatedly with them (Ahuja et al., 2003). Therefore,

H4. The higher the prestige of a given player, the higher the likelihood that another actor will seek that player as a partner for repeated interaction.

## 3.2. Actors’ Actual Demographic Characteristics as Antecedent to Network Structure

The second set of hypotheses examines whether actors’ actual demographic characteristics influence the process of network formation. For example, several empirical studies find considerable evidence for gender homophily (e.g., Marsden, 1987) – that is, that women are more likely to choose women as partners for repeated interaction and men are more likely to choose men as partners for repeated interaction. Ibarra (1993) claims that in contexts where women are in the minority (as is usually the case in MMOGs), they find it more difficult to form relationships. (An extensive qualitative analysis of why is found in Riemenschneider et al., 2007). Kvasny et al. (2008) find that women IT professionals, who are in the minority in all segments of the IT profession, are concerned about gender discrimination in the workplace. Studies also find a tendency for girls to play in smaller groups than do boys (McPherson et al., 2001), whereas other studies find that women are higher than men in their friendship centrality (Klein et al., 2004). Several researchers find that women are less likely to initiate contacts with men than vice versa (see also the related literature in Smythe, 1991)

Since the players in the game we use for analysis (see the subsection “Data Collection and Sample” in Section 4, below) know neither the “real” (actual) gender of other players nor the gender of the virtual player, one might conclude that an actor’s actual demographic characteristics do not influence the process of network formation. Hence, we test the following hypotheses:

H5a. Actual women are less likely to seek partners for repeated interaction than are actual men.

H5b. Actual women are more likely to be sought as partners for repeated interaction than are actual men.

H5c. Actual women are more likely to seek other actual women as their partners for repeated interaction, and actual men are more likely to seek other actual men as their partners for repeated interaction.

In their review article on homophily, McPherson et al. (2001) point out that in studies of close friendship, age homophily can be a stronger predictor than anything else. Other studies of the network evolution process find that the probability of a tie between two actors increases as their age difference decreases (Louch, 2000). A recent study (Leskovec and Horvitz, 2008) finds agehomophily effects among users of Microsoft’s Instant Messenger; the same researchers also find that older users tend to send more messages. Klein et al. (2004) find that older people in an advice network are more likely to be sought as partners for repeated interaction, but do not find the same effect for friendship networks. Since the players in an MMOG do not know the actual age of their counterparts, one might conclude that an actor’s actual characteristics do not influence the process of network formation. Hence, we propose the following hypotheses:

H6a. The higher a player’s actual age, the more likely she or he is sought as a partner for repeated interaction.

H6b. The higher a player’s actual age, the more likely she or he seeks partners for repeated interaction.

H6c. The less difference in two players’ actual ages, the more likely a player will seek the other player as a partner for repeated interaction.

## 3.3. Performance as an Antecedent to Network Structure

The third set of hypotheses examines whether characteristics of virtual actors (observable by all players) influence the process of network formation. One of the most prominent characteristics is a player’s individual performance in the game. Generally, players with a high individual performance in the game are expected to have higher expertise. Hence, other players are more likely to contact them seeking advice (c.f. Borgatti and Cross, 2003; Bunderson, 2003; Hinds et al., 2000). Furthermore, players with a higher performance in the game are higher in the game’s hierarchy. Saunders et al. (1994) find that people higher in a hierarchy communicate more and write at greater length, and hypothesize that players higher in a hierarchy are more likely to seek interaction. Finally, homophily theory (e.g., McPherson et al., 2001) suggests that people who perform at a similar level are more likely to interact repeatedly with each other. In summary, we hypothesize,

H7a. The higher a player’s performance in the game, the more likely she or he is sought as a partner for repeated interaction by other players.

H7b. The higher the performance of a player in the game, the more likely she or he seeks partners for repeated interaction.

H7c. The less difference in the level of performance between two players, the more likely a player will seek the other player as a partner for repeated interaction.

## 3.4. Performance as an Outcome of Network Structure

Whereas the previous set of hypotheses considers performance as an antecedent to network structure, our final three hypotheses examine direct effects from a player’s structural position within a social network on performance.

Several authors have examined the effects of an actor’s centrality in a network on individual performance (e.g., Ahuja et al., 2003; Baldwin and Bedell, 1997; Brass, 1981; Cross and Cummings, 2004; Mehra et al., 2001; Milton and Westphal, 2005; Moran, 2005; Rodan and Galunic, 2004; Sparrowe et al., 2001). Ahuja et al. (2003) identify, among others, two ways by which the position in a social network might enhance an actor’s individual performance (see also Ahuja et al., 2003, for theoretical underpinnings and related literature): central individuals can exert more influence by virtue of being linked with a large number of other actors in the network, and central actors are more likely to be connected with other actors in the network, potentially receiving more information, of higher quality, than less central individuals. Ahuja et al. (2003) state further that an ego’s contact to its alters determines how it interprets events, perceptions, cognitions, and behaviors. In a similar vein, social influence theories (e.g., Deutsch and Gerard, 1955) examine why an ego adapts its behavior according to the behavior of its alters. These authors expect that the performance of a player will become similar to the performance of the players with which she or he repeatedly interacts. This effect is also supported in part by a study of Raz and Gloor (2007), who find that the leaders of successful Israeli software start-ups talk the most with their successful peers, whereas lowperforming companies build up ties to other low-performing companies. Hence,

H8. The greater the number of partners with whom a player seeks to interact repeatedly, the better her/his performance in the game.

H9. The greater the number of other players that seek a player as their partner for repeated interaction and, thus, supply this player with information, the higher the performance of the player sought as a partner.

H10. Over time, the likelihood that a player’s performance will become similar to the other players’ performance she or he seeks as partners for repeated interaction is greater than a random change in performance.

## 4. Methodology

## 4.1. Data Collection and Sample

To test the proposed hypotheses, we used data from the German MMOSG Ocean Control, launched in April 2006 (see Appendix A for a more detailed description of the game). The basic idea of Ocean Control is that players possess islands from which they can extract resources. With these resources, they can construct buildings, ships, and combat units, and fight against each other. Players can form alliances to support each other in their fights, and they can also bargain with each other and exchange resources.

For our study, we analyzed all interactions and activities over six months, from April to September 2006, by a subset of active users from among the first 2,000 Ocean Control users. The dataset includes all messages exchanged among players in the game, buddy lists, diplomatic relations, trade relations, alliance membership, taxes paid for alliance membership, several performance measures, as well as players’ actual demographic characteristics (sex and age). We also conducted a survey of all players during these six months that asked about factors leading to their performance in Ocean Control. However, the results of this survey are not reported in this paper and, hence, the survey questions are not specified.

We divided the data into three successive two-month periods to examine the process of network evolution. Doing so was an indispensable step in our analysis, because without such a division, we could model neither evolution of the network nor causality between network structure and performance. The three periods were: 1) April–May 2006; 2) June–July 2006; and 3) August– September 2006. We opted for three two-month periods, and not a greater number of shorter periods, to keep the number of data per period high enough to ensure stability of the parameter estimates. Furthermore, estimating the model with three periods was convenient, because having more than three periods would have meant a substantial increase in the time required for parameter estimation. Finally, it is reasonable to assume that the parameters are stable across periods if the number of periods is kept to three.

We used Condor software (formerly TecFlow) (Gloor and Zhao, 2004) to construct adjacency matrices for the three periods. In the following, $x ( t ) = x _ { i j } ( t )$ denotes an n×n adjacency matrix, where $\mathsf { X } _ { \mathsf { i j } } { = } 1 ( 0 )$ represents a tie (no tie) from actor i to actor j $( \mathsf { i , j } { = } 1 , \ldots \mathsf { n } )$ in period t, that is, player i sends at least two messages to player j (i→j). We decided on a threshold of c=2 to exclude one -time interactions from our analysis that would be classified in a qualitative analysis either as spam (publicity, etc.) or as extraordinary events. Furthermore, a threshold of c=2 reflects sustainable/repeated interaction and is appropriate for testing the proposed hypotheses that examine repeated interactions.

Table 1. Network Density Indicators and Number of Dyads

<table><tr><td></td><td>April-May</td><td>June-July</td><td>August-September</td></tr><tr><td colspan="4">Network density indicators</td></tr><tr><td>Density</td><td>0.05</td><td>0.10</td><td>0.12</td></tr><tr><td>average degree</td><td>2.82</td><td>5.39</td><td>6.32</td></tr><tr><td>number of ties</td><td>152</td><td>291</td><td>341</td></tr><tr><td colspan="4">Dyad counts</td></tr><tr><td>mutual dyads</td><td>64</td><td>125</td><td>139</td></tr><tr><td>asymmetrical dyads</td><td>24</td><td>41</td><td>63</td></tr><tr><td>null dyads</td><td>1397</td><td>1319</td><td>1283</td></tr><tr><td>total dyads</td><td>1485</td><td>1485</td><td>1485</td></tr></table>

Since some of the 2,000 actors either did not play during the six months or dropped out of the game altogether, we examined only the interactions of 55 actors belonging to three alliances in the game. Most players in these three alliances played over the full period of six months. The demographics of this subsample are comparable to the total sample, with a mean age of 27.63 years (s.d. = 9.73 years)

and a gender distribution of 81.4 percent male and 18.6 percent female. Tables 1 and 2 provide an overview of some descriptive network statistics of the subsample. Figure 1 illustrates the interaction network in period 3.

Table 2. Tie changes between subsequent observations

<table><tr><td></td><td>0 =&gt; 0</td><td>0 =&gt; 1</td><td>1 =&gt; 0</td><td>1 =&gt; 1</td><td>Distance</td></tr><tr><td>April–May – June–July</td><td>2625</td><td>193</td><td>54</td><td>98</td><td>247</td></tr><tr><td>June–July – August–September</td><td>2503</td><td>176</td><td>126</td><td>165</td><td>302</td></tr></table>

![](/api/attachments/H48QAKDK/fulltext/images/ec5998276ca8c9048f1a2d0f0d9c62269611ffcbc4e99ad2031aaa742faa3eb2.jpg)  
Figure 1. Interaction Network in Period 3.

## 4.2. Model

To examine the dynamic co-evolution of network structure and performance, we employed a stochastic, actor-driven modeling approach proposed by Snijders (e.g., Snijders, 1996; Snijders et al., 2007). The advantage of Snijders’ methodology is that the same variable can be interpreted as both an independent and a dependent variable concurrently, as the following paragraphs show. This makes it possible to establish a causal relationship between structural network variables and performance.

Snijders models the co-evolution of network structure and actor characteristics as a continuous-time Markov process $\mathsf { Y } ( \mathrm { t } ) { = } ( \mathsf { X } ( \mathrm { t } ) , Z _ { \mathsf { h } 1 } ( \mathrm { t } ) , { \ldots } , Z _ { \mathsf { h } } ( \mathrm { t } ) )$ on the space of actors’ characteristics $Z _ { \mathsf { h i } } ( \mathsf { h } { = } 1 , . . . , \mathsf { H } )$ (in this case, performance), as well as of all digraphs on a set of n actors (i.e., all adjacency matrices). Since a Markov process can be described fully by its first observation y(t ) and a transition matrix, Snijders derives the elements of the transition matrix between state $y = ( \mathsf { x } , z )$ and the next state $\boldsymbol { \hat { y } } = ( \boldsymbol { \hat { x } } , \boldsymbol { \hat { z } } )$ as

$$
q _ {i j} = \left\{ \begin{array}{c l} \lambda_ {i} ^ {[ X ]} (y) p (x (\mathrm{i} \Rightarrow \mathrm{j}) | x, z) & \text { if } \hat {\mathrm{y}} = (x (\mathrm{i} \Rightarrow j), z), \\ \lambda_ {i} ^ {[ Z _ {h} ]} (y) p (z (\mathrm{i} \square_ {\mathrm{h}} \delta) | x, z) & \text { if } \hat {\mathrm{y}} = (x, z (\mathrm{i} \square_ {\mathrm{h}} \delta)), \\ - \sum_ {i} \left\{\sum_ {j \neq i} q (y; (x (\mathrm{i} \Rightarrow \mathrm{j}), z)) + \sum_ {\delta \in \{- 1, 1 \}} q (y; (x, z (\mathrm{i} \square_ {\mathrm{h}} \delta))) \right\} & \text { if } \hat {\mathrm{y}} = \mathrm{y}, \\ 0 & \text { otherwise } \end{array} \right.
$$

Explanation: To derive the transition matrix, Snijders decomposes each change between two consecutive observations $\mathsf { y } ( \mathsf { t } _ { \mathsf { m } } )$ and $\mathsf { y } ( \mathsf { t } _ { \mathsf { m } + 1 } )$ into so-called “micro $\mathsf { s t e p s ^ { \ast } - }$ randomly determined moments in time where one of the actors i has the opportunity either to: change a tie variable $\mathsf { X } _ { \mathsf { i j } }$ (i.e. ${ \widehat { y } } = ( x ( i \Rightarrow j ) , z ) ) ;$ ; change his or her own characteristics $Z _ { \mathrm { h i } }$ by $\delta ~ ( \mathfrak { i . e . } \hat { y } = \big ( x , z ( i \updownarrow _ { \mathfrak { h } } \delta ) \big ) )$ ; or change nothing $( \mathsf { i } . \mathsf { e } . \hat { y } = y )$ . The queue time between two micro steps is assumed to follow an exponential distribution, with parameters specified by so-called rate-functions $\lambda _ { i } ^ { [ X ] }$ and $\lambda _ { i } ^ { [ Z _ { h } ] }$ that we assume to be constant and independent between actors in this study.

To obtain transition intensities, Snijders multiplies the rate functions by the probabilities of an actual change taking place. Whereas $p = \bigl ( x ( i \Rightarrow j ) | , x ( t ) , z ( t ) \bigr )$ denotes the probability that actor i changes its tie to actor j (conditioned on all other ties being constant, and given actor characteristics), $p =$ $( z ( i \uparrow _ { \mathrm { h } } \delta ) | x , z )$ denotes the probability that actor i’s characteristic h will decrease or increase by δ.

These probabilities must be specified to estimate the full model. Therefore, Snijders models the change probabilities as a discrete choice model in multinomial logit form (cf. McFadden, 1974), that is

$$
p = \big (x (i \Rightarrow j) |, x (t), z (t) \big) = \frac {e ^ {u ^ {[ X ]}} \big (\beta , x (i \Rightarrow j) (t) , z (t) \big)}{\sum_ {k} e ^ {u ^ {[ X ]}} \big (\beta , x (i \Rightarrow j) (t) , z (t) \big)}
$$

where $u ^ { [ X ] }$ denotes the deterministic part of a utility function that actor i attributes to the network configuration. In this study, we estimate 104 different models with different utility functions composed of variables/effects (the next section explains them in detail). For example, a utility function that allows a test of H2 (reciprocity) and H3 (transitivity) only might be defined as

$$
u _ {i} ^ {[ X ]} \big (\beta^ {[ X ]}, y \big) = \beta^ {r e c i p r o c i t y} \sum_ {j} x _ {i j} x _ {j i} + \beta^ {t r a n s i t i v i t y} \sum_ {j, l} x _ {i j} x _ {i l} x _ {j l}
$$

Analogously, the formulas for the behavioural evolution of performance can be derived (for a more detailed discussion, see Snijders et al., 2007).

## 4.3. Measures and Effects Included in Utility Function and Performance Function

General tendency to repeatedly interact with alters (density/outdegree effect) is measured as $\sum _ { j } x _ { i j }$ (cf. hypothesis $1 ) ^ { 6 } { } _ { : }$ , that is, player i’s utility function $u ^ { [ X ] }$ increases by value 1 if player i seeks player j as a partner for repeated interaction, because the corresponding value in the adjacency matrix $\mathsf { X } _ { \parallel }$ equals 1 if player i repeatedly interacts with player j (and is 0 otherwise). Consequently, a negative parameter $\dot { \beta } ^ { \circ \mathsf { u f d e g r e e } }$ indicates that player i does not tend to seek random partners for repeated interaction, but that each additional interaction tie is associated with some “cost” for player i.

Number of mutual ties (reciprocity) is measured as $\textstyle \sum _ { j } x _ { i j } x _ { j l }$ (cf. hypothesis 2), that is, player i’s $\mathsf { x } _ { \mathrm { i j } } = 1 )$ , a positive parameter β<sup>age</sup> <sup>homophily</sup> indicates that a player is more likely to seek another player as a partner for repeated interaction if both players have a similar age.

<table><tr><td>utility function  $u^{[X]}$  increases by value 1 only if player i seeks player j as a partner for repeated interaction ( $x_{ij} = 1$ ) and player j seeks player i as a partner for repeated interaction ( $x_{ji} = 1$ ). If one of these ties is missing (i.e.  $x_{ij} = 0$  or  $x_{ji} = 0$ ), the product will equal 0. Consequently, a positive parameter  $\beta^{\text{reciprocity}}$  indicates a greater likelihood that player i seeks player j as a partner for repeated interaction if player j also chooses player i as a partner for repeated interaction.</td></tr><tr><td>Number of transitive triplets (transitivity) is measured as  $\sum_{j,l} x_{ij} x_{il} x_{jl}$  (cf. hypothesis 3), that is, player i&#x27;s utility function  $u^{[X]}$  increases by value 1 if player i seeks an interaction tie that closes a transitive triplet, because the product  $x_{ji}$   $x_{il}$   $x_{jl}$  equals 1 only if player i repeatedly seeks interaction with player j ( $x_{ji} = 1$ ) as well as player i repeatedly seeks interaction with player l ( $x_{il} = 1$ ) and player j repeatedly seeks interaction with player l ( $x_{jl} = 1$ ). A positive parameter  $\beta^{\text{transitivity}}$  thus indicates a greater likelihood that player i seeks an interaction tie that closes a transitive triplet than seeks a random tie.</td></tr><tr><td>Prestige of a player (popularity of alter) is measured as  $\frac{1}{n} \sum_{j} x_{ij} \sum_{l} x_{lj}$  (cf. hypothesis 4)., that is, player i&#x27;s utility function  $u^{[X]}$  comprises a term that reflects 1/n times the indegree of all other players j to whom player i is tied. Hence, a positive parameter  $\beta^{\text{popularity of alter}}$  indicates that a player is more likely to seek a player who has a greater popularity as a partner for repeated interaction.</td></tr><tr><td>Demographic characteristics are measured as follows. Gender was coded 1 for men and 2 for female. Age was measured in years since birth.</td></tr><tr><td>The gender alter effect is measured as  $\sum_{j} x_{ij} \text{gender}_{j}$  (cf. hypotheses 5b), that is, player i&#x27;s utility function  $u^{[X]}$  increases by value 1 if player i seeks player j, who is male, as a partner for repeated interaction ( $x_{ji} = 1$  and  $\text{gender}_{j} = 1$ ), but by value 2 ( $x_{ji} = 1$  and  $\text{gender}_{j} = 2$ ) if she or he seeks player j, who is female, as a partner for repeated interaction. Hence, a positive parameter  $\beta^{\text{gender alter}}$  indicates that women are more likely to be sought as partners for repeated interaction than are men.</td></tr><tr><td>The age-alter effect was measured as  $\sum_{j} x_{ij} \text{age}_{j}$  (cf. hypotheses 6a), i.e. player i&#x27;s utility function  $u^{[X]}$  increases by player j&#x27;s age if player i seeks to player j as a partner for repeated interaction. Hence, a positive parameter  $\beta^{\text{age alter}}$  indicates that older people are more likely to be sought as partners for repeated interaction than younger player.</td></tr><tr><td>The gender-ego effect is measured as  $\text{gender}_{i} \sum_{j} x_{ij}$  (cf. hypotheses 5a), that is, player i&#x27;s utility function increases by value 2 (1) with each player j to whom player i seeks interaction repeatedly, if player i is female (male). Hence, a positive parameter  $\beta^{\text{gender ego}}$  indicates that male players are more likely to seek partners for repeated interaction than are female players.</td></tr><tr><td>The age-ego effect is measured as  $\text{age}_{i} \sum_{j} x_{ij}$  (cf. hypotheses 6b), that is, player i&#x27;s utility function increases by the value of player i&#x27;s age for each tie that actor seeks to another player j. Hence, a positive parameter  $\beta^{\text{age ego}}$  indicates that older players are more likely to seek partners for repeated interaction than are younger players.</td></tr><tr><td>Gender homophily is measured as  $\sum_{j} x_{ij} I\{ \text{gender}_{i} = \text{gender}_{j} \}$ , where I is an indicator function (cf. hypothesis 5c), that is, player i&#x27;s utility function increases by value 1 if player i seeks a partner for repeated interaction that has the same gender. Hence, a positive parameter  $\beta^{\text{gender homophily}}$  indicates that males tend seek other males as their partners for repeated interaction, and females tend to seek other females as their partners for repeated interaction.</td></tr><tr><td>Age homophily is measured as  $\sum_{j} x_{ij} \left( \frac{\max_{ij} |age_{i}-age_{j}| - |age_{i}-age_{j}|}{\max_{ij} |age_{i}-age_{j}|} - \frac{\overline{\max_{ij} |age_{i}-age_{j}| - |age_{i}-age_{j}|}}{\max_{ij} |age_{i}-age_{j}|} \right)$  (cf. hypothesis 6c). The first term in the brackets reflects a similarity score between player i and player j. It calculates the difference between the age of the two players  $|age_{i} - age_{j}|$  (in absolute values) and standardizes this difference by the range of all players&#x27; ages  $\max_{ij} |age_{i} - age_{j}|$ . The second term reflects the mean of all similarity scores standardized by the range of all players&#x27; ages. Since the complete term in brackets is included only in player i&#x27;s utility function, if player i is tied to player j (i.e.,</td></tr></table>

Player performance (perf ) is measured as the number of experience points in the game (rescaled on a scale from 0-254). In Ocean Control, players gain experience points for actions such as constructing buildings. The main reason for using experience points as a measure of performance is that other measures are more problematic because of an assumption of conditional independence (which is a requirement for the model). The three performance effects included in a player’s utility function (alter/ego/similarity) are defined analogously to the demographic effects (cf. Hypotheses 5 and 6). Consequently, a positive parameter β<sup>performance</sup> <sup>alter</sup> indicates that players who have a higher performance are more likely to be sought as partners for repeated interaction, a positive parameter β<sup>performance</sup> <sup>ego</sup> indicates that high-performing players are more likely to seek partners for repeated interaction, and a positive parameter $\beta ^ { \mu }$ <sup>performance</sup> <sup>similarity</sup> indicates that players tend to seek players who have a similar performance as partners for repeated interaction. The effects of a player’s network position on performance included in the performance function were defined analogously as performance outdegree $p e r f _ { i } \sum _ { j } x _ { i j }$ , performance indegree $p e r f _ { i } \sum _ { j } x _ { j i }$ , and performance total similarity $\begin{array} { r } { \sum _ { j } x _ { i j } \left( \frac { m a x _ { i j } \left| p e r f _ { i } - p e r f _ { j } \right| - \left| p e r f _ { i } - p e r f _ { j } \right| } { m a x _ { i j } \left| p e r f _ { i } - p e r f _ { j } \right| } - \frac { \overline { { m a x _ { i j } \left| p e r f _ { i } - p e r f _ { j } \right| } - \left| p e r f _ { i } - p e r f _ { j } \right| } } { m a x _ { i j } \left| p e r f _ { i } - p e r f _ { j } \right| } \right) } \end{array}$ (cf. hypotheses 8-10), Hence, a positive parameter β<sup>performance</sup> <sup>outdegree</sup> indicates that players who seek more partners for repeated interaction tend to have a higher performance; a positive parameter β<sup>performance</sup> <sup>indegree</sup> indicates that higher the number of players who seek a given player as a partner for repeated interaction, the higher the performance of that player; and a positive parameter $\beta ^ { \mathrm { t o t a l \ s i m i l i a r t y } }$ indicates that a player’s performance tends to become similar to the performance of those players she or he seeks as partners for repeated interaction.

Furthermore, we include three control variables in our analysis: a general drive toward high performance $p e r f _ { i } .$ , and a quadratic tendency effect $\left( p e r f _ { i } - \overline { { p e r f _ { \imath } } } \right) ^ { 2 }$ in the performance function, and a homophily between players belonging to the same alliance in the utility function $\begin{array} { r } { \sum _ { j } x _ { i j } I \big \{ a l l i a n c e _ { i } = a l l i a n c e _ { j } \big \} } \end{array}$ , where <sub>??</sub> is an indicator function that takes a value of 1 if both players belong to the same alliance, and 0 if not. Hence, player i’s utility function increases by value 1 only with each partner with whom player i seeks to interact repeatedly and who is in the same alliance. Hence, a positive parameter β<sup>alliance</sup> <sup>homophily</sup> indicates that players tend to seek players as partners for repeated interaction who are in the same alliance.

## 4.4. Analysis

Altogether, we estimated 104 different models, of which six are reported in this paper (due to space limitations). All models were estimated using the method of moments with the Robbins-Monro (1951) stochastic approximation procedure. Snijders et al. (2007) provides a detailed description of the procedure and statistics employed for the moment estimation. All models were estimated using SIENA (Simulation Investigation for Empirical Network Analysis) 3.11. T-tests indicate good convergence for all models (criteria employed $\mathsf { t } < . 1 )$ and the covariance matrices do not indicate evidence for multicollinearity that might lead to problems during the estimation (compare Robins et al., 2007). Before estimation, individual covariates were centered by subtracting their mean value. Missing data on covariates and dependent action variables were replaced by the variables’ average score at this observation moment. To ensure a minimal impact of missing data treatment on parameter estimation, the calculation of the target statistics used for estimation was restricted to nonmissing data.

The different models were developed in a hierarchical analysis. Effects were retained in the subsequent models if they were significant and improved model fit according to Neyman-Rao tests. In the nested model comparisons by Neyman-Rao tests, we compare a model that restricts the newly added parameters to be zero against a model that allows the newly added parameters to vary freely. Large deviations and hence large $\mathsf X ^ { 2 }$ values (and low p-values) indicate that the restricted model has a worse fit than the unrestricted model and, hence, the newly added parameters should be integrated into the model.

## 5. Results

Model 1 (Table 3) illustrates the results of a model that includes the four endogenous network effects as well as an effect controlling for alliance homophily. Neyman-Rao tests indicate that the inclusion of all effects into the model at the same time enhances model fit $( \mathsf { X } ^ { 2 } = 3 7 6 3 . 1 4 ; \mathsf { d } . \mathsf { f } . = 5 ; \mathsf { p } < . 0 0 0 1 )$ , and that the inclusion of one parameter at a time enhances model fit (e.g. Χ² (outdegree) = 1457.37; d.f. = $1 ; \textsf { p } < \ldots 0 0 0 1 )$ Since all effects are found to be statistically significant at a 1 percent level of significance and in the expected direction (apart from the popularity of alter parameter which is negative), H1–H3 are supported. Players have a very low general tendency to seek alters as their partners for repeated interaction who do not have attributes or a joint network embeddedness favorable to interacting repeatedly (H1). The likelihood that player i seeks player j as a partner for repeated interaction is greater if player j also chooses player i as a partner for repeated interaction (H2). And the likelihood that a player seeks a partner for repeated interaction by closing a transitive triplet is higher than the likelihood of seeking a random interaction tie (H3).

Table 3. Model 1 – Endogenous Network Effects

<table><tr><td></td><td>β</td><td>s.d.</td><td>t-value</td><td>p-value</td></tr><tr><td>rate parameter period 1</td><td>30.66</td><td>6.10</td><td>5.02</td><td>&lt;.01***</td></tr><tr><td>rate parameter period 2</td><td>24.74</td><td>3.48</td><td>7.12</td><td>&lt;.01***</td></tr><tr><td>Outdegree</td><td>-2.61</td><td>.16</td><td>-16.56</td><td>&lt;.01***</td></tr><tr><td>Reciprocity</td><td>2.84</td><td>.13</td><td>21.19</td><td>&lt;.01***</td></tr><tr><td>transitive triplets</td><td>.11</td><td>.01</td><td>9.38</td><td>&lt;.01***</td></tr><tr><td>popularity of alter</td><td>-2.67</td><td>.86</td><td>-3.11</td><td>&lt;.01**</td></tr><tr><td>alliance homophily</td><td>.62</td><td>.11</td><td>5.42</td><td>&lt;.01***</td></tr></table>

H4, however, is not supported. Rather, the popularity of alter effect goes in the opposite direction, indicating that players with higher prestige (i.e., indegree) are less likely to be sought as partners for repeated interaction. Finally, the effect of the control variable “alliance homophily” is also in the expected direction and significant, indicating that players are more likely to seek players as their partners for repeated interaction who are part of the same alliance in the game.

Models 2 and 3 (Tables 4 and 5) test whether the players’ actual demographic characteristics influence the process of network formation. Neyman-Rao tests indicate that the inclusion of gender effects in Model 2 (Table 4) enhances model fit $( X ^ { 2 } = 1 1 . 7 2 ; \mathrm { d . f . } = 3 ; \mathsf { p } < . 0 1 )$ . As evident from the nonsignificant gender homophily effect in Table 4, H5c is not supported, that is, there is no statistical evidence that actual women are more likely to seek other actual women as their partners for repeated interaction, and actual men are more likely to seek actual men as their partners for repeated interaction. Also, Neyman-Rao tests indicate that simply including a gender homophily effect $( \mathsf X ^ { 2 } =$ $0 . 7 4 ; \mathsf { d } . \mathsf { f } . = 1 ; \mathsf { p } = . 3 9 )$ does not enhance model fit. This corresponds to our expectation that the actor’s actual demographic characteristics do not influence the process of network evolution. However, contrary to our expectations, the results indicate a significant gender alter effect as well as a significant gender ego effect in support of H5a and H5b, that is, actual women are less likely to seek partners for repeated interaction than are actual men (H5a), and actual women are more likely to be sought as partners for repeated interaction than are actual men (H5b). Whereas H5a also seems intuitive (because women/men do not change their way of interacting), it is surprising that the players’ actual demographic characteristics (not directly observable during the game) influence the process of network formation, and women are more likely to be sought as partners for repeated interaction than are men (H5b).

<table><tr><td colspan="5">Table 4. Model 2 – Gender Effects</td></tr><tr><td></td><td>B</td><td>s.d.</td><td>t-value</td><td>p-value</td></tr><tr><td>rate parameter period 1</td><td>31.79</td><td>6.68</td><td>4.76</td><td>&lt;.01***</td></tr><tr><td>rate parameter period 2</td><td>24.93</td><td>3.44</td><td>7.25</td><td>&lt;.01***</td></tr><tr><td>Outdegree</td><td>-2.78</td><td>.17</td><td>-16.83</td><td>&lt;.01***</td></tr><tr><td>Reciprocity</td><td>2.93</td><td>.17</td><td>17.61</td><td>&lt;.01***</td></tr><tr><td>transitive triplets</td><td>.10</td><td>.01</td><td>9.27</td><td>&lt;.01***</td></tr><tr><td>popularity of alter</td><td>-2.12</td><td>.86</td><td>-2.45</td><td>.01*</td></tr><tr><td>alliance homophily</td><td>.71</td><td>.12</td><td>6.11</td><td>&lt;.01***</td></tr><tr><td>gender alter</td><td>.41</td><td>.18</td><td>2.22</td><td>.03*</td></tr><tr><td>gender ego</td><td>-.46</td><td>.20</td><td>-2.37</td><td>.02*</td></tr><tr><td>gender homophily</td><td>-.05</td><td>.15</td><td>-.34</td><td>.73</td></tr></table>

Model 3 (Table 5) extends Model 2 by an age-ego, and age-alter, and an age-homophily effect. None of the effects proposed in H6a–H6c are statistically significant (p=.05), that is, there is no statistical evidence that the actor’s actual age influences the process of network formation. In particular, the parameter estimates testing H6a (older players are more likely to be sought as partners for repeated interaction than are younger players) and H6c (older players are more likely to seek other older players as their partners for repeated interaction, and younger players are more likely to seek other younger players as their partners, for repeated interaction). However, the age-ego effect is significant at a 10 percent level of significance (p = .07), indicating that actual older people are more likely to seek partners for repeated interaction than actual younger players (H6b). Furthermore, this effect is intuitive, because older/younger players do not change their interaction behavior although their actual age is not observable. Neyman-Rao tests indicate that the inclusion of all age effects into the model at the same time increases model fit (Χ² = 13.42; d.f. = 3; p < .01), and that the increased model fit can be attributed to a large extent to the inclusion of the age-ego effect $( \mathsf { X } ^ { 2 } = 1 2 . 9 2 ; \mathsf { d . f . } = 1 ; \mathsf { p } < . 0 1 )$ Hence, we include the weak, non-significant age-ego effect in subsequent models. The other nonsignificant effects (such as age homophily) are not integrated into the subsequent models to achieve parsimony of the models.

<table><tr><td colspan="5">Table 5. Model 3 – Age Effects</td></tr><tr><td></td><td>B</td><td>s.d.</td><td>t-value</td><td>p-value</td></tr><tr><td>rate parameter period 1</td><td>32.14</td><td>6.81</td><td>4.72</td><td>&lt;.01***</td></tr><tr><td>rate parameter period 2</td><td>24.75</td><td>3.31</td><td>7.48</td><td>&lt;.01***</td></tr><tr><td>Outdegree</td><td>-2.85</td><td>.18</td><td>-15.92</td><td>&lt;.01***</td></tr><tr><td>Reciprocity</td><td>2.95</td><td>.14</td><td>20.45</td><td>&lt;.01***</td></tr><tr><td>transitive triplets</td><td>.10</td><td>.01</td><td>9.58</td><td>&lt;.01***</td></tr><tr><td>popularity of alter</td><td>-1.92</td><td>.94</td><td>-2.05</td><td>.04*</td></tr><tr><td>alliance homophily</td><td>.75</td><td>.12</td><td>6.22</td><td>&lt;.01***</td></tr><tr><td>gender alter</td><td>.46</td><td>.19</td><td>2.46</td><td>.01*</td></tr><tr><td>gender ego</td><td>-.47</td><td>.18</td><td>-2.30</td><td>.02*</td></tr><tr><td>gender homophily</td><td>-.03</td><td>.16</td><td>-0.19</td><td>.85</td></tr><tr><td>age alter</td><td>.00</td><td>.01</td><td>0.53</td><td>.59</td></tr><tr><td>age ego</td><td>.01</td><td>.01</td><td>1.81</td><td>.07</td></tr><tr><td>age homophily</td><td>-.16</td><td>.30</td><td>-0.53</td><td>.60</td></tr></table>

Model 4 (Table 6) tests whether player performance can be seen as an antecedent to network structure. None of the three performance effects are found to be statistically significant. Furthermore, Neyman-Rao tests do not indicate an increase in model fit if any of these parameters is included into the model (e.g. Χ² = 1.90; d.f. = 3, p = .59). Hence, H7a–H7c are not supported.

Model 5 (Table 7) examines whether the non-significant performance effects might be attributed to overfitting the model. However, leaving out the popularity of alter, alliance homophily, and gender effects does not change the results substantially. Also, a Neyman-Rao test indicates that including performance effects in Model 5 does not increase model fit (Χ² = 1.92; d.f. = 3; p = .59). Hence, one cannot conclude any of the following: that the higher a player’s performance in the game, the more likely she or he is sought as a partner for repeated interaction (H7a); that the higher a players’ performance, the more likely she or he seeks other players as partners for repeated interaction (H7b); or that the less difference in the performance between two players, the more likely a player will seek the other player as partner for repeated interaction (H7c).

Table 6. Model 4 – Performance as Antecedent to Network Structure (1)

<table><tr><td></td><td>β</td><td>s.d.</td><td>t-value</td><td>p-value</td></tr><tr><td>rate parameter period 1</td><td>29.47</td><td>5.79</td><td>5.09</td><td>&lt;.01***</td></tr><tr><td>rate parameter period 2</td><td>24.77</td><td>3.53</td><td>7.02</td><td>&lt;.01***</td></tr><tr><td>Outdegree</td><td>-2.74</td><td>.19</td><td>-14.46</td><td>&lt;.01***</td></tr><tr><td>Reciprocity</td><td>2.92</td><td>.19</td><td>15.60</td><td>&lt;.01***</td></tr><tr><td>transitive triplets</td><td>.11</td><td>.01</td><td>10.08</td><td>&lt;.01***</td></tr><tr><td>popularity of alter</td><td>-2.48</td><td>.88</td><td>-2.81</td><td>&lt;.01**</td></tr><tr><td>alliance homophily</td><td>.69</td><td>.13</td><td>5.47</td><td>&lt;.01***</td></tr><tr><td>gender alter</td><td>.45</td><td>.15</td><td>2.94</td><td>&lt;.01**</td></tr><tr><td>gender ego</td><td>-.37</td><td>.19</td><td>-1.91</td><td>.06</td></tr><tr><td>age ego</td><td>.02</td><td>.01</td><td>3.02</td><td>&lt;.01**</td></tr><tr><td>performance alter</td><td>.01</td><td>.01</td><td>.88</td><td>.38</td></tr><tr><td>performance ego</td><td>-.01</td><td>.01</td><td>-.74</td><td>.46</td></tr><tr><td>performance homophily</td><td>.26</td><td>.23</td><td>1.14</td><td>.25</td></tr></table>

## Table 7. Model 5 – Performance as Antecedent to Network Structure (2)

<table><tr><td></td><td>B</td><td>s.d.</td><td>t-value</td><td>p-value</td></tr><tr><td>rate parameter period 1</td><td>30.17</td><td>6.24</td><td>4.84</td><td>&lt;.01***</td></tr><tr><td>rate parameter period 2</td><td>21.87</td><td>2.79</td><td>7.85</td><td>&lt;.01***</td></tr><tr><td>Outdegree</td><td>-2.40</td><td>.08</td><td>-28.91</td><td>&lt;.01***</td></tr><tr><td>Reciprocity</td><td>2.80</td><td>.14</td><td>19.74</td><td>&lt;.01***</td></tr><tr><td>transitive triplets</td><td>.10</td><td>.01</td><td>12.96</td><td>&lt;.01***</td></tr><tr><td>performance alter</td><td>-.00</td><td>.01</td><td>-.51</td><td>.61</td></tr><tr><td>performance ego</td><td>-.00</td><td>.01</td><td>-.12</td><td>.90</td></tr><tr><td>performance homophily</td><td>.17</td><td>.21</td><td>.79</td><td>.43</td></tr></table>

Table 8. Model 6 – Performance as Outcome of Network Structure

<table><tr><td></td><td>B</td><td>s.d.</td><td>t-value</td><td>p-value</td></tr><tr><td colspan="5">Network Evolution</td></tr><tr><td>rate parameter period 1</td><td>32.08</td><td>8.75</td><td>3.67</td><td>&lt;.01***</td></tr><tr><td>rate parameter period 2</td><td>24.67</td><td>3.32</td><td>7.43</td><td>&lt;.01***</td></tr><tr><td>Outdegree</td><td>-2.74</td><td>.18</td><td>-15.57</td><td>&lt;.01***</td></tr><tr><td>Reciprocity</td><td>2.90</td><td>.17</td><td>16.62</td><td>&lt;.01***</td></tr><tr><td>transitive triplets</td><td>0.10</td><td>.01</td><td>9.32</td><td>&lt;.01***</td></tr><tr><td>Popularity of alter</td><td>-2.26</td><td>.86</td><td>-2.63</td><td>&lt;.01**</td></tr><tr><td>alliance homphily</td><td>.70</td><td>.14</td><td>5.09</td><td>&lt;.01***</td></tr><tr><td>gender alter</td><td>.43</td><td>.22</td><td>1.92</td><td>.06</td></tr><tr><td>gender ego</td><td>-.36</td><td>.18</td><td>-1.97</td><td>.05*</td></tr><tr><td>age ego</td><td>.02</td><td>.01</td><td>3.23</td><td>&lt;.01**</td></tr><tr><td colspan="5">Performance Evolution</td></tr><tr><td>rate performance period1</td><td>597.36</td><td>55.48</td><td>10.77</td><td>&lt;.01***</td></tr><tr><td>rate performance period2</td><td>971.48</td><td>57.51</td><td>16.89</td><td>&lt;.01***</td></tr><tr><td>performance tendency effect</td><td>.07</td><td>.02</td><td>3.61</td><td>&lt;.01***</td></tr><tr><td>performance effect on performance</td><td>.00</td><td>.00</td><td>1.80</td><td>.07</td></tr><tr><td>performance indegree</td><td>.00</td><td>.08</td><td>0.05</td><td>.96</td></tr><tr><td>performance outdegree</td><td>.00</td><td>.08</td><td>0.06</td><td>.95</td></tr><tr><td>performance total similarity</td><td>.34</td><td>.29</td><td>1.19</td><td>.23</td></tr></table>

Finally, Model 6 (Table 8) tests whether performance can be regarded as an outcome of network structure. None of the hypothesized effects is found to be statistically significant at a 5 percent level of significance, and Neyman-Rao tests do not indicate that including these effects enhances model fit (e.g. Χ² = 4.97; d.f. = 3; p = .17). Hence, hypotheses 8–10 are not supported. (The results also do not change substantially when controlling for several other variables such as age, gender, and playing time in the performance function.) One cannot conclude that the greater the number of partners with whom a player seeks to interact repeatedly, the better that player’s performance in the game (H8), the greater the number of other players that seek that player as their partner for repeated interaction, the higher the player’s performance (H9), or that the likelihood that a player’s performance will become similar to the performance of other players she or he seek as partners for repeated interaction is greater than a random change in performance (H10).

## 6. Conclusions

## 6.1. Theoretical Implications

This study examines the factors that determine the evolution of the interaction network of players participating in an MMOG. In this context, we test whether theories that seek to explain the evolution of interaction networks in the real world are also valid in MMOGs. Hence, Hypotheses 1–4 employ the MTML framework of Contractor et al. (2006) in an MMOG to test whether the same structura variables influence the process of network evolution. Whereas the results support Hypotheses 1–3 (i.e., negative density/outdegree effect, positive reciprocity, and transitivity effects), there is no support for Hypothesis 4 (positive popularity of alter effect). Rather, the alternate hypothesis (negative popularity of alter effect) is supported at a 5 percent level of significance, that is, a given player is less likely to seek another player as a partner for repeated interaction if that second player has already been sought by many other players as a partner for repeated interaction. A possible explanation might be that the first player does not want a partner for repeated interaction who is too popular and probably does not have the time to reciprocate the interaction requests.

Hypotheses 5 and 6 test whether the process of network formation is influenced by actors’ actual demographic characteristics (that are not directly observable by other players). We find that players actual demographic characteristics still allow for drawing conclusions about the likelihood of seeking partners for repeated interaction, that is, men and older people are more likely to seek partners for repeated interaction. This can be seen in the way that players do not try to mask the interaction behavior that is idiosyncratic to their “real identity.” Interestingly, the results also reveal that women are more likely to be sought as partners for repeated interaction (remembering that a player’s actua gender is not directly observable by other players). This indicates that players can “sense” the actual gender of others by their actions in the game. In summary, there is sound statistical evidence that network evolution in the real world and in MMOGs is influenced by the same structural variables, as well as by the same demographic variables. Hence, MMOGs may be a good approximation of the real world and can serve as testbed for researchers focusing on network characteristics and demographic variables to examine, for example, diffusion processes.

We do not find any statistically significant effects between network structure and performance (either with performance as an antecedent to network structure or as an outcome of network structure). This indicates that, unlike in the real world, high-performing actors in MMOGS are not necessarily sought as partners for repeated interaction. Furthermore, structural social capital does not necessarily influence player performance in MMOGs. Consequently, variables such as performance may be correlated differently to network evolution in the real world and in (hedonic) MMOGs. Hence, researchers should be cautious when claiming the validity of their findings regarding the association between network structure and performance (e.g., with respect to employee performance) if the findings are obtained using game data.

Our findings mirror the various results obtained by other researchers. For example, Rafaeli and Ravid (2003) examine the interactions and performance of players in a supply-chain, role-playing simulation game, and find that sharing information in the team via email has a positive impact on performance. Teigland et al. (2006), though, examine network data from 1,434 individuals in 28 offices at a multinational high-technology firm, and find that a high centrality in the overall network has a negative effect on efficient performance. However, diversity of personal ties, the use of electronic ties, and network centrality are found to have positive effects on creative performance. Future research should distinguish further between different types and performance, and analyze the relationship between network structure and performance in more detail.

## 6.2. Managerial Implications

In addition to the theoretical insights, this study also provides some insights for practitioners. Our work applies the MTML framework of Contractor et al. (2006) to an MMOG, and the results indicate that theories regarding (endogenous) social network effects (such as transitivity and reciprocity) can be transferred from a real-world context to MMOGs. These findings are particularly important for marketing managers interested in word-of-mouth, diffusion of innovations, lead-user identification, and viral marketing campaigns: The findings suggest strongly that their knowledge of the structural effects of network dynamics acquired through their “real-world experience” is a solid basis for future management decisions (e.g., when launching marketing campaigns in MMOGs). Furthermore, marketing managers can use MMOGs as a testbed for real-world marketing campaigns when the focus is on the customers’ structural and demographic characteristics.

With respect to socio-demographic variables, we find that women are less likely to seek partners for repeated interaction, women are more likely to be sought as partners for repeated interaction, and older people are more likely to seek partners for repeated interaction. These findings could, for example, help managers and game designers develop alternative pricing models for MMOGs. Since older people place greater emphasis on a large number of “buddies” in the game and generally are also better off financially, one pricing option might be to restrict the maximum number of buddies in a buddy list unless the player pays a higher monthly subscription fee.

In this study, we find no effects from player performance in a game on network evolution, nor any effects from players’ structural embeddedness in the interaction network on player performance. Although all players in the game can interact repeatedly with each other, it is clear that mere technological infrastructure alone is not enough to achieve a social infrastructure of interaction that enhances player performance (cf. Kelly and Jones, 2001). Therefore, managers should support research that seeks to understand in greater detail the interplay between repeated interactions, knowledge exchange, and performance. Since employees are often unwilling to provide data that allow for correlating performance with (efficient) interactions, studies that examine the co-evolution of the interaction network and performance in MMOGs could provide useful hints for managers interested in the efficiency of certain organization/interaction structures. However, researchers must still identify the conditions under which a transfer of such findings in an MMOG to the real world is truly valid. Managers can help by providing access to relevant data.

## 6.3. Limitations and Future Research

Social network analysis is a highly interdisciplinary area of research that continues to accrue growing attention in computer science, sociology, communication science, economics, and physics (as evidenced by the number of papers on the subject being published in these fields). In this study, we employ a multidisciplinary approach, following the recommendation of Bray and Konsynski (2007) that scholars examining MMOGs draw not only on literature within their specific field, but also from related fields. Of course, as with any empirical study, ours is subject to some limitations that could be seen as affecting the rigor and relevance. In a multidisciplinary study such as ours, this may be especially problematic, given that what is seen as a limitation or even a “fatal flaw” in one discipline may not be seen as such in another.<sup>8</sup>

We do not consider most of these limitations to void our results, so long as we remain aware of them as we draw our conclusions. In fact, they suggest some future research that examines interaction networks and performance in MMOGs in a variety of different disciplines. In particular, future research should seek to overcome the limitations that stem from the sample, the methodology employed, and the omission of certain variables when testing theories of social selection and influence.

Regarding our sample, we use data from a German MMOG (see Appendix A). Study results, though, may vary considerably between different cultures (see Kayworth and Leidner, 2001; Leidner and Kayworth, 2006). Therefore, future studies should explore these questions through a multinational comparison. Furthermore, while we are unable to monitor whether the self-reported responses from players regarding their ages and genders are indeed true, a mean age of 27.63 years (s.d. = 9.73 years) and a gender distribution of 81.4 percent male and 18.6 percent female seems to be reasonable for the players of MMOGs (cf. Cole and Griffiths, 2007). In a study of postings in Usenet newsgroups, Crowston and Kammerer (1998) find that about 87 percent are by males, which is quite similar to our sample. Hence, this is a “limitation” of little consequence in examining a representative sample of MMOG players. Furthermore, we focused our analysis on 55 actors, members of three alliances in which most players played over the full period of six months. However, players’ alliance membership might influence their performance metrics (e.g., through mutual support). This may, in turn, result in a lower likelihood of detecting a network-performance link. Hence, future research should analyze the relationship between players’ network embeddedness and player performance, with a sample consisting of players who belong to more alliances in the game. Some further analyses revealed that our analyzed sub-sample showed enough variance in the individual players’ number of experience points to draw meaningful conclusions.

Finally, to avoid issues of privacy, we did not analyze the content of messages between players. We note, though, that personal messages could reflect some “conflict” between players and, hence, lead to lower performance (of individual players or of an entire alliance) (see Wakefield et al., 2008).

Regarding our methodology, readers should be aware of the assumptions of the stochastic actororiented model (cf. Snijders et al., 2007). We assume that all players act conditionally independent from each other, all players change their characteristics conditionally independent, and players cannot change their characteristics and interaction partners during the same micro step. Consequently, micro steps are randomly determined moments in time (following an exponential distribution) during which a player has the opportunity to seek a partner for repeated interaction or to change his or her characteristics (e.g., performance), but not to seek a partner for interaction and change his and her characteristics.

We also assume that player i seeks player j as a partner for repeated interaction in period t if actor i sends at least two messages (c=2) to player j in period t. Although this assumption seems reasonable, a different cutoff value might lead to different results. Nevertheless, estimating some models using a cutoff value of c=5 (not reported in this paper) does not substantially change the results of the models. Furthermore, there are as yet no satisfactory measures of explained variation (that proposed by Snijders, 2004, may be a first step in this direction). Hence, we illustrate the relationship between the different models using Neyman-Rao tests.

We cannot include in this study every possible, interesting effect. For example, when examining the effects of gender on network formation, the authors cannot extend the study to examine whether men are more likely to seek women as partners for repeated interaction (or vice versa), because this effect led to poor convergence of the estimation algorithm. Future research should seek to analyze this effect in greater detail. Furthermore, when examining the relationship between network structure and performance, we explore a linear relationship between in- and outdegree and performance only. It is possible that neither players with too many contacts nor players with too few contacts have a high performance. Nevertheless, these effects are not yet implemented in SIENA (the software used for estimation), and so we must leave the examination of non-linear effects of centrality on performance for our future research. In addition, the performance metric (number of experience points) might be affected by other factors such as, for example, players’ time spent playing, experience with other games, and completion of non-competitive game activities. Hence, future research should control for

these factors.

In the same context, we also examine performance as an outcome only at the individual level. Future research should analyze performance effects at the group level as well (see, e.g., Fuller et al., 2006; Kane, in Review, 2nd round).

Finally, we do not integrate concepts of trust into this study (e.g., Sarker et al., in review). It may well be that trust is one of the most important factors for teams that rely exclusively on virtual interaction (see Jarvenpaa and Leidner, 1999, for an extensive discussion). Hence, future research should seek to draw a stronger distinction between temporary and ongoing repeated interactions (see Saunders and Ahuja, 2006) and examine whether a player’s tenure in an alliance influences his or her individual interaction patterns (see Ahuja and Galvin, 2003). Futhermore, it may be worthwhile to distinguish between the spatial and social proximity of players in the game and examine in greater detail the effects of geographic proximity on social selection.

It is our hope that our research will assist others in conducting these types of studies and form the basis for substantial future research into MMOGs and the co-evolution of social networks and actor characteristics in MMOGS. Further, we hope that our research provides useful insights for managers and other practitioners that can be applied now both in real-world and MMOG settings.

## Acknowledgements

The authors thank Scott M. Cooper, Marius Cramer, Rob Laubacher, Jure Leskovec, Robin Teigland, Ben Waber, Florian Weber, and the three anonymous reviewers, as well as the discussants at the XXVIII Sunbelt Social Network Conference for their input and valuable comments on earlier drafts of this article.

## References

Ahuja, M. K. and K. M. Carley (1999) “Network Structure in Virtual Organizations,” Organization Science (10) 6, pp. 741-757.

Ahuja, M. K., D. F. Galletta, and K. M. Carley (2003) “Individual Centrality and Performance in Virtual R&D Groups: An Empirical Study,” Management Science (49) 1, pp. 21-38.

Ahuja, M. K. and J. E. Galvin (2003) “Socialization in Virtual Groups,” Journal of Management (29) 2, pp. 161-185.

Ariely, D. and M. I. Norton (2007) “Psychology and Experimental Economics: A Gap in Abstraction,” Current Directions in Psychological Science (16) 6, pp. 336-339.

Aviv, R. and G. Ravid (2005) “Reciprocity Analysis of Online Learning Networks,” Journal of Asynchronous Learning Networks (9) 4, pp. 1-23.

Baldwin, T. T. and M. D. Bedell (1997) “The Social Fabric of a Team-based M.B.A. Program: Network Effects on Student Satisfaction and Performance,” Academy of Management Journal (40) 6, pp. 1369-1397.

Barabási, A.-L. and R. Albert (1999) “Emergence of Scaling in Random Networks,” Science (286) 5439, pp. 509-512.

Bernard, H. R., P. D. Killworth, and L. Sailer (1980) “Informant Accuracy in Social Network Data IV: A Comparison, of Clique-Level Structure in Behavioral and Cognitive Network Data,” Social Networks (2) 3, pp. 191-218.

Bernard, H. R., P. D. Killworth, and L. Sailer (1982) “Informant Accuracy in Social-Network Data V: An Experimental Attempt to Predict Actual Communication from Recall Data,” Social Science Research (11) 1, pp. 30-66.

Blau, P. M. (1986) Exchange and Power in Social Life: Transaction Publishers.

Bolton, P. and M. Dewatripont (1994) “The Firm as a Communication Network,” The Quarterly Journal of Economics (109) 4, pp. 809-839.

Borgatti, S. P. and R. Cross (2003) “A Relational View of Information Seeking and Learning in Social Networks,” Management Science (49) 4, pp. 432-445.

Bourdieu, P. and L. J. D. Wacquant (1992) An Invitation to Reflexive Sociology. Cambridge, UK: University of Chicago Press.

Brass, D. J. (1981) “Structural Relationships, Job Characteristics, and Worker Satisfaction and Performance,” Administrative Science Quarterly (26) 3, pp. 331-348.

Bray, D. A. and B. R. Konsynski (2007) “Virtual worlds: Multi-disciplinary Research Opportunities,” ACM SIGMIS Database (38) 4, pp. 17-25.

Bunderson, J. S. (2003) “Team Member Functional Background and Involvement in Management Teams: Direct Effects and the Moderating Role of Power Centralization,” Academy of Management Journal (46) 4, pp. 458-474.

Burt, R. S. (2000) “The Network Structure of Social Capital,” Research in Organizational Behavior (22), pp. 345-423.

Butler, B. S. (2001) “Membership Size, Communication Activity, and Sustainability: A Resource-Based Model of Online Social Structures,” Information Systems Research (12) 4, pp. 346- 362.

Castronova, E. (2001) “Virtual Worlds: A First-Hand Account of Market and Society on the Cyberian Frontier,” in CESifo Working Paper Series No. 618: SSRN.

Castronova, E. (2005) “Real Products in Imaginary Worlds,” Harvard Business Review (83) 5, pp. 20- 22.

Choi, B., I. Lee, D. Choi, and J. Kim (2007) “Collaborate and Share: An Experimental Study of the Effects of Task and Reward Interdependencies in Online Games,” CyberPsychology & Behavior (10) 4, pp. 591-595.

Cole, H. and M. D. Griffiths (2007) “Social Interactions in Massively Multiplayer Online Role-Playing Gamers,” CyberPsychology & Behavior (10) 4, pp. 575-583.

Coleman, J. S. (1988) "Social Capital in the Creation of Human Capital," American Journal of Sociology (94), pp. 95-120.

Contractor, N. S., S. Wasserman, and K. Faust (2006) “Testing Multitheoretical, Multilevel Hypotheses about Organizational Networks: An Analytic Framework and Empirical Example,” Academy of Management Review (31) 3, pp. 681-703.

Cross, R. and J. N. Cummings (2004) “Tie and Network Correlates of Individual Performance in Knowledge-intensive work,” Academy of Management Journal (47) 6, pp. 928-937.

Crowston, K. and E. Kammerer (1998) “Communicative Style and Gender Differences in Computermediated Communications,” in B. Ebo (Ed.) Cyberghetto or Cybertopia: Race, Class and Gender on the Internet, Westport, CT: Praeger, pp. 185-204.

Cummings, J. N., B. Butler, and R. Kraut (2002) “The Quality of Online Social Relationships,” Communications of the ACM (45) 7, pp. 103-108.

Deutsch, M. and H. B. Gerard (1955) “A Study of Normative and Informational Social Influences upon Individual Judgment,” (51) 3, pp. 629-636.

Doreian, P. and F. N. Stokman (1997) Evolution of Social Networks. Amsterdam: Gordon and Breach.

Ducheneaut, N., N. Yee, E. Nickell, and R. J. Moore. (2006) ““Alone together?” Exploring the Social Dynamics of Massively Multiplayer Online Games.” SIGCHI Conference on Human Factors in Computing Systems, 2006, pp. 407-416.

Edery, D. (2006) “Reverse Product Placement in Virtual Worlds,” Harvard Business Review (84) 12, pp. 24-24.

Freeman, L. C., A. K. Romney, and S. C. Freeman (1987) “Cognitive structure and informant accuracy,” American Anthropologist (89) 2, pp. 310-325.

Fuller, M. A., A. M. Hardin, and R. M. Davison (2006) “Efficacy in Technology-Mediated Distributed Teams,” Journal of Management Information Systems (23) 3, pp. 209-235.

Galimberti, C., S. Ignazi, P. Vercesi, and G. Riva (2001) “Communication and Cooperation in Networked Environments: An Experimental Analysis,” CyberPsychology & Behavior (4) 1, pp. 131-146.

Gloor, P. A. and Y. Zhao (2004) “TeCFlow - A Temporal Communication Flow Visualizer for Social Network Analysis,” in ACM CSCW. Chicago, Illinois.

Glushko, B. (2007) “Tales of the (Virtual) City: Governing Property Disputes in Virtual Worlds,” Berkeley Technology Law Journal (22) 1, pp. 507-532.

Guo, Y. and S. Barnes (2007) “Why People Buy Virtual Items in Virtual Worlds with Real Money,” ACM SIGMIS Database (38) 4, pp. 69-76.

Heider, F. (1982) The Psychology of Interpersonal Relations: Lawrence Erlbaum Associates.

Hemp, P. (2006a) “Avatar-Based Marketing,” Harvard Business Review (84) 6, pp. 48-57.

Hemp, P. (2006b) “The Avatar as Consumer,” Harvard Business Review (84) 2, pp. 60-61.

Hinds, P. J., K. M. Carley, D. Krackhardt, and D. Wholey (2000) “Choosing Work Group Members: Balancing Similarity, Competence, and Familiarity,” Organizational Behavior & Human Decision Processes (81) 2, pp. 226-251.

Holland, P. W. and S. Leinhardt (1970) “A Method for Detecting Structure in Sociometric Data,” The American Journal of Sociology (76) 3, pp. 492-513.

Ibarra, H. (1993) “Personal Networks of Women and Minorities in Management: A Conceptual Framework,” Academy of Management Review (18) 1, pp. 56-87.

Jarvenpaa, S. L. and D. E. Leidner (1999) “Communication and Trust in Global Virtual Teams,” Organization Science (10) 6, pp. 791-815.

Jenkins, P. S. (2004) “The Virtual World as a Company Town: Freedom of Speech in Massively Multiple Online Role Playing Games,” Journal of Internet Law (8) 1, pp. 1-18.

Jian, W. (2007) “The Stable Self-Enforcement and Distribution of Property Right,” American Law & Economics Association Papers (40) pp. 1-13.

Jiang, X., F. Safaei, and P. Boustead (2007) “An Approach to Achieve Scalability through a Structured Peer-to-Peer Network for Massively Multiplayer Online Role Playing Games,” Computer Communications (30) 16, pp. 3075-3084.

Jones, Q., G. Ravid, and S. Rafaeli (2004) “Information Overload and the Message Dynamics of Online Interaction Spaces: A Theoretical Model and Empirical Exploration,” Information Systems Research (15) 2, pp. 194-210.

Kane, G. (in Review, 2nd round) “IS Proficiency in Social Networks,” MIS Quarterly.

Kayworth, T. R. and D. E. Leidner (2001) “Leadership Effectiveness in Global Virtual Teams,” Journal of Management Information Systems (18) 3, pp. 7-40.

Kelly, S. a. and M. Jones (2001) “Groupware and the Social Infrastructure of Communication,” Communications of the ACM (44) 12, pp. 77-79.

Killworth, P. D. and H. R. Bernard (1976) “Informant Accuracy in Social Network Data,” Human Organization (35) 3, pp. 269.

Killworth, P. D. and H. Russell Bernard (1979) “Informant Accuracy in Social Network Data Ill: A Comparison of Triadic Structure in Behavioral and Cognitive Data,” Social Networks (2) 1, pp. 19-46.

Kim, Y.-Y., S. Oh, and H. Lee (2005) “What Makes People Experience Flow: Social Characteristics of Online Games,” International Journal of Advanced Media and Communication (1pp. 76-92.

Klein, K. J., L. Beng-Chong, J. L. Saltz, and D. M. Mayer (2004) “How Do they Get there? An Examination of the Antecedents of Centrality in Team Networks,” Academy of Management Journal (47) 6, pp. 952-963.

Kvasny, L., F. C. Payton, V. Mbarika, and A. Amadi (2008) “Gender Perspectives on the Digital Divide, IT Education and Workforce Participation in Kenya,” IEEE Transactions on Education (51) 2, pp. 256-261.

Lamb, R. and R. Kling (2003) “Reconceptualizing Users as Social Actors in Information Systems Research,” MIS Quarterly (27) 2, pp. 197-235.

Lastowka, F. G. and D. Hunter (2004) “The Laws of the Virtual Worlds,” California Law Review (92) 1, pp. 3-73.

Leidner, D. E. and T. Kayworth (2006) “Review: A Review of Culture in Information Systems Research: Toward a Theory of Information Technology Culture Conflict,” MIS Quarterly (30) 2, pp. 357-399.

Leskovec, J. and E. Horvitz. (2008) “Planetary-Scale Views on a Large Instant-Messaging Network.” World Wide Web, Beijing, China, 2008.

Louch, H. (2000) “Personal Network Integration: Transitivity and Homophily in Strong-tie Relations,” Social Networks (22) 1, pp. 45-64.

MacInnes, I. (2006) “Property Rights, Legal Issues, and Business Models in Virtual World Communities,” Electronic Commerce Research (6) 1, pp. 39-56.

Marsden, P. V. (1987) “Core Discussion Networks of Americans,” American Sociological Review (52) 1, pp. 122-131.

Marsden, P. V. (1990) “Network Data and Measurement,” Annual Review of Sociology (16) 1, pp. 435-463.

McFadden, D. (1974) “Conditional Logit Analysis of Qualitative Choice Behaviour,” in P. Zarembka (Ed.) Frontiers in Econometrics, NY: Academic Press, pp. 105-142.

McLure Wasko, M. and S. Faraj (2005) “Why Should I Share? Examining Social Capital and Knowledge Contribution in Electronic Networks of Practice,” MIS Quarterly (29) 1, pp. 35-57.

McPherson, M., L. Smith-Lovin, and J. M. Cook (2001) “Birds of a feather: Homophily in Social Networks,” Annual Review of Sociology (27) 1, pp. 415.

Mehra, A., M. Kilduff, and D. J. Brass (2001) “The Social Networks of High and Low Self-Monitors: Implications for Workplace Performance,” Administrative Science Quarterly (46) 1, pp. 121- 146.

Meng, Y. and C. Long (2006) “System-performance Modeling for Massively Multiplayer Online Roleplaying Games,” IBM Systems Journal (45) 1, pp. 45-58.

Messerly, J. G. (2004) “How Computer Games Affect CS (and Other) Students’ School Performance,” Communications of the ACM (47) 3, pp. 29-31.

Milton, L. P. and J. D. Westphal (2005) “Identity Confirmation Networks and Cooperation in Work Groups,” Academy of Management Journal (48) 2, pp. 191-212.

Moran, P. (2005) “Structural vs. Relational Embeddedness: Social Capital and Managerial Performance,” Strategic Management Journal (26) 12, pp. 1129-1151.

Nardi, B. A., S. Ly, and J. Harris. (2007) “Learning Conversations in World of Warcraft.” Proceedings of the 40th Annual Hawaii International Conference on System Sciences, 2007, pp. 79.

Noy, A., D. R. Raban, and G. Ravid (2006) “Testing Social Theories in Computer-mediated

Parks, M. R. and K. Floyd (1996) “Making Friends in Cyberspace,” Journal of Communication (46) 1, pp. 80-97.

Pfeffer, J. and G. R. Salancik (1978) The External Control of Organizations. New York: Harper & Row.

Rafaeli, S. and G. Ravid (2003) “Information Sharing as Enabler for the Virtual Team: An Experimental Approach to Assessing the Role of Electronic Mail in Disintermediation,” Information Systems Journal (13) 2, pp. 191-206.

Raz, O. and P. A. Gloor (2007) “Size Really Matters--New Insights for Start-ups’ Survival,” Management Science (53) 2, pp. 169-177.

Riemenschneider, C. K., D. J. Armstrong, M. F. Reid, R. L. Rashé et al. (2007) “Barriers IT Employees Face - A Gender Perspective.” Americas Conference on Information Systems, Keystone, Colorado, 2007.

Robbins, H. and S. Monro (1951) “A Stochastic Approximation Method,” The Annals of Mathematical Statistics (22) 3, pp. 400-407.

Robert, L. P., A. R. Dennis, and M. K. Ahuja (2008) “Social Capital and Knowledge Integration in Digitally Enabled Teams,” Information Systems Research (19) 3, pp. 314-334.

Robins, G., T. Snijders, P. Wang, M. Handcock et al. (2007) “Recent Developments in Exponential Random Graph (p\*) Models for Social Networks,” Social Networks (29) 2, pp. 192-215.

Rodan, S. and C. Galunic (2004) “More than Network Structure: How Knowledge Heterogeneity Influences Managerial Performance and Innovativeness,” Strategic Management Journal (25) 6, pp. 541-562.

Sarker, S., M. K. Ahuja, S. Kirkeby, and S. Sarker (in review) “Revisiting the Role of Trust and Communication in Distributed Teams: A Test of Three Competing Models using the Social Networks Perspective,” MIS Quarterly (-.

Saunders, C. S. and M. K. Ahuja (2006) “Are All Distributed Teams the Same?,” Small Group Research (37) 6, pp. 662-700.

Saunders, C. S., D. Robey, and K. A. Vaverek (1994) “The Persistence of Status Differentials in Computer Conferencing,” Human Communication Research (20) 4, pp. 443-472.

Smyth, J. M. (2007) “Beyond Self-Selection in Video Game Play: An Experimental Examination of the Consequences of Massively Multiplayer Online Role-Playing Game Play,” CyberPsychology & Behavior (10) 5, pp. 717-721.

Smythe, M.-J. (1991) “Gender and Communication Behaviors: A Review of Research,” in B. Dervin and M. J. Voigt (Eds.) Progress in Communication Science, Norwich, NJ: Ablex, pp. 173-216.

Snijders, T. A. B. (1996) “Stochastic Actor-Oriented Models for Network Change,” Journal of Mathematical Sociology (21) 1/2, pp. 149-172.

Snijders, T. A. B. (2004) “Explained Variation in Dynamic Network Models,” Mathematics & Social Sciences (168), pp. 31-41.

Snijders, T. A. B., C. E. G. Steglich, and M. Schweinberger (2007) “Modeling the Co-evolution of Networks and Behavior,” in K. v. Montford, H. Oud, and A. Satorra (Eds.) Longitudinal Models in the Behavioral and Related Sciences, Newark, NJ: Lawrence Earlbaum.

Sparrowe, R. T., R. C. Liden, S. J. Wayne, and M. L. Kraimer (2001) “Social Networks and the Performance of Individuals and Groups,” Academy of Management Journal (44) 2, pp. 316- 325.

Teigland, R. (2007) “Fad or Future? What Do Virtual Worlds Have to Offer,” in IFL Conference on Second Life & Virtual Worlds.

Teigland, R., C. Smatt, and M. Wasko (2006) “Webs of Advice: Examining the Relationships between Personal Ties, Electronic Ties, and Performance,” in Academy of Mangement Annual Meeting. Atlanta.

Teigland, R. and M. Wasko (2009) “Knowledge Transfer in MNCs: Examining how Intrinsic Motivations and Knowledge Sourcing Impact Individual Centrality and Performance,” Journal of International Management (15) 1, pp. 15-31.

Wakefield, R., D. E. Leidner, and G. Garrison (2008) “A Model of Conflict, Leadership, and Performance in Virtual Teams,” Information Systems Research (19) 4, pp. 434-455.

Wasserman, S. and K. Faust (1994) Social Network Analysis: Methods and Applications: Cambridge University Press.

Wasserman, S. and P. Pattison (1996) “Logit models and logistic regressions for social networks: I. An introduction to Markov graphs and p\*,” Psychometrika (61) 3, pp. 401-425.

Whang, L. S.-M. and G. Chang (2004) “Lifestyles of Virtual World Residents: Living in the On-Line Game “Lineage”,” CyberPsychology & Behavior (7) 5, pp. 592-600.

Willer, D. (1999) Network Exchange Theory. Westport, CT: Praeger Publishers.

Wonseok, O. H., C. Jin Nam, and K. I. M. Kimin (2005) “Coauthorship Dynamics and Knowledge Capital: The Patterns of Cross-Disciplinary Collaboration in Information Systems Research,” Journal of Management Information Systems (22) 3, pp. 265-292.

Yao-Chung, C. (2006) “Massively Multiplayer Online Role-Playing Game-Induced Seizures: ANeglected Health Problem in Internet Addiction,” CyberPsychology & Behavior (9) 4, pp. 451-456.

Yee, N., J. N. Bailenson, M. Urbanek, F. Chang et al. (2007) “The Unbearable Likeness of Being Digital: The Persistence of Nonverbal Social Norms in Online Virtual Environments,” CyberPsychology & Behavior (10) 1, pp. 115-121.

## Appendix A. Description of the Game “Ocean Control”

It is important to ensure that the findings of this study are not idiosyncratic to the particular game analyzed. Therefore, we would like to provide the reader some further information about the game. None of this information is crucial, but it may facilitate the interpretation of the results (particularly those regarding players’ performance). Ocean Control is a browser game. At the beginning of the game, each player opts to participate as warrior or merchant. Players can observe the actions taken by other players, and access other players’ profiles. These profiles contain username, three individual performance metrics (experience points, ordinary points, and current ranking in the game), the names and coordinates of islands possessed by the player, alliance membership (name), number of alliance members, as well as performance metrics of the alliance (total number of points, average points per member, and ranking). Players can annotate their profiles with any additional information using free text fields. Most “Ocean Control” players are members of an alliance. Although alliance membership is not critical for success, it increases the likelihood of a player’s success since alliance members support each other during fights (by sending combat units and exchanging resources). According to some players, most communication in Ocean Control between players (via text messages) is taskrelated.

<table><tr><td>About the Authors</td></tr><tr><td>Johannes Putzke is a PhD candidate and research associate at the Department of Information Systems and Information Management, University of Cologne, Germany. His current research interests include social network analysis, complex systems, network science, (social) media and marketing.</td></tr><tr><td>Kai Fischbach is an Assistant Professor in the Department of Information Systems and Information Management at the University of Cologne. He is also Associate Director of the Center for Applied Social Network Analysis (CASNA) in Cologne. Previously, he worked at the WHU-Otto Beisheim School of Management (Germany) and has been a visiting scholar at the Massachusetts Institute of Technology (USA) and the University of Illinois at Urbana-Champaign (USA). His research focuses on the formation of social and complex networks, open innovation, and the design of efficient information exchanges.</td></tr><tr><td>Detlef Schoder is a Professor of Information Systems and Information Management at the University of Cologne. Previously, he served as Chair of Electronic Business at WHU-Otto Beisheim School of Management. He is the author of a large number of reviewed publications, including journal articles in leading international outlets such as the Journal of Product Innovation Management, Journal of Marketing, Journal of Electronic Commerce Research, Journal of the Association of Information Systems, Harvard Business Review, International Journal on Media Management, Electronic Markets, and Communications of the ACM. Professor Schoder has worked not only in Germany, but also in the United States, Republic of Kazakhstan, and Japan. He has been an invited Visiting Scholar at Stanford University, the University of California, Berkeley, and the Massachusetts Institute of Technology (MIT).</td></tr><tr><td>Peter A. Gloor is a Research Scientist at the MIT Center for Collective Intelligence where his research focuses on Collaborative Innovation Networks, swarm creativity, and dynamic social network analysis. He is also Chief Creative Officer of startup galaxyadvisors AG as well as a lecturer at University of Cologne and Aalto University in Finland. He obtained his Ph.D from the University of Zurich and was a Post-Doc at the MIT Lab for Computer Science. Later he was Section Leader Software Engineering at UBS, a Principal at PwC and a Principal and European Practice Leader for E-Business at Deloitte Consulting.</td></tr><tr><td>Copyright © 2010, by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers for commercial use, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via e-mail from ais@gsu.edu.</td></tr></table>

#

ISSN: 1536-9323

Editor

Kalle Lyytinen

Case Western Reserve University

<table><tr><td colspan="4">Senior Editors</td></tr><tr><td>Michael Barrett</td><td>University of Cambridge</td><td>Robert Fichman</td><td>Boston College</td></tr><tr><td>Dennis Galletta</td><td>University of Pittsburgh</td><td>Varun Grover</td><td>Clemson University</td></tr><tr><td>Jeffrey Parsons</td><td>Memorial University of Newfoundland</td><td>Suzanne Rivard</td><td>Ecole des Hautes Etudes Commerciales</td></tr><tr><td>Carol Saunders</td><td>University of Central Florida</td><td>Avi Seidmann,</td><td>University of Rochester</td></tr><tr><td>Ananth Srinivasan</td><td>University of Auckland</td><td>Bernard Tan</td><td>National University of Singapore</td></tr><tr><td>Michael Wade</td><td>York University</td><td>Ping Zhang</td><td>Syracuse University</td></tr><tr><td colspan="4">Editorial Board</td></tr><tr><td>Steve Alter</td><td>University of San Francisco</td><td>Kemal Altinkemer</td><td>Purdue University</td></tr><tr><td>Michel Avital</td><td>University of Amsterdam</td><td>Cynthia Beath</td><td>University of Texas at Austin</td></tr><tr><td>Michel Benaroch</td><td>University of Syracuse</td><td>Avi Bernstein</td><td>University of Zurich,</td></tr><tr><td>Anandhi S. Bharadwaj</td><td>Emory University</td><td>Marie-Claude Boudreau</td><td>University of Georgia</td></tr><tr><td>Susan A. Brown</td><td>University of Arizona</td><td>Andrew Burton-Jones</td><td>University of British Columbia</td></tr><tr><td>Traci Cart</td><td>University of Oklahoma</td><td>Dubravka Cecez-Kecmanovic</td><td>University of New South Wales</td></tr><tr><td>Patrick Y.K. Chau</td><td>University of Hong Kong</td><td>Mike Chiasson</td><td>Lancaster University</td></tr><tr><td>Mary J. Culnan</td><td>Bentley College</td><td>Jan Damsgaard</td><td>Copenhagen Business School</td></tr><tr><td>Elizabeth Davidson</td><td>University of Hawaii</td><td>Jason Derdrick</td><td>University of California, Irvine</td></tr><tr><td>Samer Faraj</td><td>McGill university</td><td>Chris Forman</td><td>Carnegie Mellon University</td></tr><tr><td>Peter Gray</td><td>University of Virginia</td><td>Ola Henfridsson</td><td>Viktoria Institute &amp; Halmstad University</td></tr><tr><td>Traci Hess</td><td>Washington State University</td><td>Qing Hu</td><td>Iowa State University</td></tr><tr><td>Jimmy Huang</td><td>University of Warwick</td><td>Kai Lung Hui</td><td>National University of Singapore, Singapore</td></tr><tr><td>Bala Iyer</td><td>Babson College</td><td>Hemant Jain</td><td>University of Wisconsin-Milwaukee</td></tr><tr><td>Zhenhui (Jack) Jiang</td><td>National University of Singapore</td><td>Bill Kettinger</td><td>University of Memphis</td></tr><tr><td>Gary Klein</td><td>University of Colorado, Colorado Springs</td><td>Ken Kraemer</td><td>University of California, Irvine</td></tr><tr><td>Mary Lacity</td><td>University of Missouri-St. Louis</td><td>Liette Lapointe</td><td>McGill University</td></tr><tr><td>T.P. Liang</td><td>National Sun Yat-Sen Universitvty</td><td>Kai H. Lim</td><td>City University of Hong Kong, Hong Kong</td></tr><tr><td>Lihui Lin</td><td>Boston University</td><td>Ji-Ye Mao</td><td>Renmin University</td></tr><tr><td>Anne Massey</td><td>Indiana University</td><td>Ramiro Montealegre</td><td>University of Colorado at Boulder</td></tr><tr><td>Michael Myers</td><td>University of Auckland, New Zealand</td><td>Fiona Fui-Hoon Nah</td><td>University of Nebraska-Lincoln</td></tr><tr><td>Fred Niederman</td><td>St. Louis University</td><td>Mike Newman</td><td>University of Manchester</td></tr><tr><td>Brian Pentland</td><td>Michigan State University</td><td>Geert Poels</td><td>Katholieke Universiteit Leuven</td></tr><tr><td>Jaana Porra</td><td>University of Houston</td><td>Sandeep Purao</td><td>Penn State University</td></tr><tr><td>T. S. Raghu</td><td>Arizona State University</td><td>Dewan Rajiv</td><td>University of Rochester</td></tr><tr><td>Neil Ramiller</td><td>Portland State University</td><td>Matti Rossi</td><td>Helsinki School of Economics</td></tr><tr><td>Suprateek Sarker</td><td>Washington State University</td><td>Susan Scott</td><td>The London School of Economics and Political Science</td></tr><tr><td>Ben Shao</td><td>Arizona State University</td><td>Olivia Sheng</td><td>University of Utah</td></tr><tr><td>Choon-ling Sia</td><td>City University of Hong Kong</td><td>Carsten Sorensen</td><td>The London School of Economics and Political Science</td></tr><tr><td>Katherine Stewart</td><td>University of Maryland</td><td>Mani Subramani</td><td>University of Minnesota</td></tr><tr><td>Burt Swanson</td><td>University of California at Los Angeles</td><td>Jason Thatcher</td><td>Clemson University</td></tr><tr><td>Ron Thompson</td><td>Wake Forest University</td><td>Christian Wagner</td><td>City University of Hong Kong</td></tr><tr><td>Dave Wainwright</td><td>Northumbria University</td><td>Eric Walden</td><td>Texas Tech University</td></tr><tr><td>Eric Wang</td><td>National Central University</td><td>Jonathan Wareham</td><td>ESADE</td></tr><tr><td>Stephanie Watts</td><td>Boston University</td><td>Tim Weitzel</td><td>Bamberg University, Germany</td></tr><tr><td>George Westerman</td><td>Massachusetts Institute of Technology</td><td>Kevin Zhu</td><td>University of California at Irvine</td></tr><tr><td colspan="4">Administrator</td></tr><tr><td>Eph McLean</td><td>AIS, Executive Director</td><td colspan="2">Georgia State University</td></tr><tr><td>J. Peter Tinsley</td><td>Deputy Executive Director</td><td colspan="2">Association for Information Systems</td></tr></table>
