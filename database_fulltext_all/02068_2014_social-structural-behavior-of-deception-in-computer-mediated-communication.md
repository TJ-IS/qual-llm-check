---
otero_id: 2068
otero_key: "9K764B86"
title: "Social structural behavior of deception in computer-mediated communication"
authors: "Jinie Pak; Lina Zhou"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.08.010"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Social structural behavior of deception in computer-mediated communication

Jinie Pak ⁎, Lina Zhou

Department of Information Systems, University of Maryland Baltimore County, 1000 Hilltop Circle, Baltimore, MD 21250, USA

## a r t i c l e i n f o

Available online xxxx

Keywords: Deception Social structural approach Deception behavior Social network analysis Computer-mediated communication

## a b s t r a c t

Deception essentially takes place in social interaction. While deception has been studied from the perspective of interpersonal interaction, little is known about social structural characteristics of deceptive communication. To <sup>fi</sup>ll the knowledge gap, this research investigates deception behavior in computer mediated communication (CMC) via the lens of social structure by answering the questions of how one deceiver socially interacts with multiple receivers and what structural characteristics can be used to delineate deception in CMC. To this end, we <sup>fi</sup>rst conceptualize deception in terms of social structure by drawing on the interpersonal deception and social network theories. We then propose a model of structural behaviors of deception in CMC that consists of three components: centrality, cohesion, and similarity, followed by an empirical evaluation of the model with realworld data collected from a game website. The <sup>fi</sup>ndings of this study provide new evidence that deception is a strategic activity where the deceiver juggles between the dual goals of promoting his or her deceptive agenda and avoiding detection.

© 2013 Published by Elsevier B.V.

## 1. Introduction

Computer mediated communication (CMC) provides social bene<sup>fi</sup>ts for individuals and organizations to create, enhance, and re-discover social ties through interactive and transparent forms of communicating and collaborating with others [1]. As the CMC technologies continuously evolve; however, online deception has become a growing threat to our society particularly due to the prevalence of online social networks, where a wealth of sensitive information could be harvested and exploited for cyber-attacks on a large number of receivers (e.g., [23,50]). In addition, deception negatively impacts group decision making process through hampering the decision making ability of others [34]. Therefore, there is an emerging need to understand deception behavior in the context of multiple receivers, which is instrumental to detecting deceptive information and uncovering malicious senders.

Deception behavior has traditionally been grouped into two main categories: verbal (e.g., negative affect) and non-verbal behaviors (e.g., facial expression) [13,22,84]. Verbal behavior is directly related to the spoken or written content and language [37,79], whereas nonverbal behavior “focuses on accessory features that are exhibited while a person is producing content” [78]. Given that text is the primary modality available in CMC, verbal behavior has been the focus of extant online deception research. Despite the availability of nonverbal behavior in CMC, it has largely been under explored in the study of online deception. There has been very limited but promising evidence for the ef<sup>fi</sup>cacy of non-verbal behavior in online deception detection [82]. In the study, Zhou and Zhang explored and empirically con<sup>fi</sup>rmed keyboard, participatory, and sequential behaviors being new channels of nonverbal cues to online deception, and called for research into new sources of nonverbal behavior of deception in CMC. To answer the call, the current study examines deception behavior via the lens of social structure.

This research looks into the context of CMC that involves one deceiver and multiple receivers. Deceptive communication encompasses backand-forth interaction between a deceiver and receivers [51]. Accordingly, deception can be viewed as a social phenomenon where individuals are connected through interactions and embedded in a structure of such relationships. The structure of ongoing social relations can be described by social structural behavior [8], and thus are related to deceptive communication and may serve as a new source of online deception behavior. There are two fundamental questions that must be answered when analyzing online deception from the social structure perspective. First, how can we conceptualize deceptive interactions as a social structure? Second, if social structure is a channel of deception behavior display, what kinds of social behaviors can be used to discriminate deceptive from truthful communication?

To address the above questions, we <sup>fi</sup>rst conceptualized deceptive communication as social relationships between deceivers and receivers, and then proposed a research model of social structural behaviors of deception in CMC by drawing on the underpinnings of the interpersonal deception theory and social network paradigms [6]. The model predicts that deception has impact on the sender's centrality, cohesion, and similarity in a social structure. We further operationalized the selected social structural behaviors with social network measures [64], and empirically validated the research model using real-world data collected from a game website. Results support most of the hypothesized effects of deception on social structural behaviors in CMC. Hereafter deception in CMC and online deception are used interchangeably.

J. Pak, L. Zhou / Decision Support Systems xxx (2013) xxx–xxx

The rest of this paper is organized as follows. In Section 2, we build theoretical foundation for a social structural approach to deceptive interaction. Subsequently, we propose a research model of social structural behavior of deception. In Section 4, we introduce method design in detail, followed by data analyses and results reported in Section 5. In Section 6, we discuss the <sup>fi</sup>ndings, implications and limitations of the research. Finally, we conclude the paper in Section 7.

## 2. A social structural approach to explaining deception

In this section, we argue that deception is essentially a type of social interaction, which lays the theoretical foundation for a social structural approach to explaining deception.

## 2.1. Deception as a type of social interaction

Social interaction is de<sup>fi</sup>ned as a situation where an individual's behaviors are continuously reorganized by, and in<sup>fl</sup>uence another individual's behaviors, and vice versa [61]. As a series of processes, social interaction can be broken down into three processes: motivational, interactional, and structuring processes [61]. Speci<sup>fi</sup>cally, motivational processes indicate that individuals are compelled and driven to interact with others; interactional processes involve actual in<sup>fl</sup>uence on each other's behaviors, signaling a course of behavior as well as interpreting both one's own behavioral signals and those of others; and structuring processes denote that social interactions are repeatedly occurring across time as well as organized (structured) in a physical space. Deception is a type of complex social interaction [58] that takes place between one or more senders and one or more receivers, and accordingly deceptive communication involves the same set of processes. Moreover, the motivational, interactional, and/or structuring components of deception have been well established in the deception literature [10,12,22].

According to the Interpersonal Deception Theory (IDT), deception is de<sup>fi</sup>ned as “a message knowingly transmitted by a sender to foster a false belief or conclusion by the receiver” [10]. As implied in the de<sup>fi</sup>nition, interactivity and strategic communications are the two key elements of deception in terms of the continuous in<sup>fl</sup>uence of a sender's behavior on a receiver and vice versa. First, to varying degrees and in diverse ways, deceivers and receivers are motivated and mobilized to interact with each other. Second, the two parties mutually in<sup>fl</sup>uence each other's behavior with or without strategic moves [58] and such strategic moves are utilized in information, behavior, and image management. During interaction processes, deceivers and receivers may signal or leak unexpected words, nonverbal leakage, strategic thinking, and emotional stress [10]. While deceivers adjust their verbal and nonverbal behaviors or deception tactics based on the receiver's feedback or response [13], receivers' perceived credibility of deceivers and their detection accuracy have continuous effect on truth bias, context interactivity, and deceivers' communication skills [11,15,81]. Substantially deception involves a series of interactive process of monitoring and adjusting communication behavior based on mutual responses or feedbacks between deceivers and receivers, and their interaction patterns are structured by such repeated interactive processes. Thus, deception exempli<sup>fi</sup>es the key processes of social interaction, and social interaction is essential to deception.

Extended from IDT, deceptive communication is not just a type of social interaction but more of strategic interaction driven by deceptive intent, leading to unique patterns of deceptive social interaction. For instance, deceivers are more likely to use control attempts when they are negotiating their outcomes with their partner or when they perceive that their partner is questioning their decision [34]. IDT was originally proposed from the interpersonal context, and accordingly many studies have focused on deceptive communication in dyads. The theory has recently been extended to explain deception when the deceiver interacts with two or more receivers [51,81]. This research expands the deception literature by focusing on deception that involves a multi-way communication between one sender (i.e. deceiver) and multiple receivers.

## 2.2. Examining deception via the lens of social structure

Social structure has been one of the central concepts in social theory and analysis. Despite the fact that social structure has been used in sophisticated theoretical propositions or frameworks [4], there is no generally agreed upon de<sup>fi</sup>nition of social structure; and the concept of social structure is often implicitly assumed. Fundamentally social structure is a network (structure) with a set of relations among actors in that network, and a structural approach studies social structure comprehensively by examining the patterns of embeddedness and connectedness of actors [27]. In social science, the social structural approach often refers to social network analysis (SNA) with emphasis on structural patterning in social networks (structures) [27,33,38]. SNA offers analytical and statistical methods for measuring patterns and structures of interaction among social actors at different levels of the network such as ego networks and whole networks [56].

An actor in a network can be de<sup>fi</sup>ned or categorized by patterns of his/her relations with other actors, namely social role. To be speci<sup>fi</sup>c, a social role is a combination of particular sets of behavioral, meaningful, and structural attributes of a social actor [67], and the patterns of those attributes of social actors are relatively stable. SNA is used to uncover the power and in<sup>fl</sup>uence of actors and to identify subgroups and their social roles such as leaders, gatekeepers, and brokers [38,42,66]. As discussed in Section 2.1, deception involves social interaction between individuals. The social structural approach helps us to identify deception behavior by looking into the ways that deceivers interact with, in<sup>fl</sup>uence and are in<sup>fl</sup>uenced by receivers, either directly or indirectly. In terms of a social structural view of deception, deceivers and receivers are treated as social actors and the chain of their strategic activities is interpreted as relations in a social network. In other words, the ongoing iterative processes of cognitive and behavioral adjustments between deceivers and receivers are interpreted as links (relationships) between them.

This study aims to examine deception in group communication from the social structural perspective based on two principles: 1) the deceiver and receivers can be modeled as social actors who are motivated by goals, intentions, interests, or tasks; and 2) most deceptive interactions consist of the exchange of valued items (e.g. information or materials). Given that online deception research has been narrowly focused on verbal behavior with few exceptions (i.e., [76]), the social structural approach to deception not only provides sociological explanations for online deception but also provides a new avenue for deception detection.

## 3. The research model and hypotheses development

According to the social structural approach to deception, deceivers and truth-tellers are treated as distinct social roles, and their interactions, behavioral expectations, and structural relations are expected to be different. Speci<sup>fi</sup>cally, we hypothesize that the deceiver's deceptive intent has an impact on three structural characteristics of his or her network: centrality, cohesion, and similarity. The research model is presented in Fig. 1.

## 3.1. Centrality

Centrality is an important structural attribute of a social network that signals potential importance, in<sup>fl</sup>uence, and prominence of an actor in the network [28]. In other words, an actor's centrality in a network implies whether or not the actor has power or in<sup>fl</sup>uence over other actors in the network [44]. Centrality can be manifested in the embeddedness or connectedness of an actor in a network, which allows the actor to impose constraints on or provide opportunities for social interaction [38]. Substantial evidence has shown that centrality measures can capture behavioral tactics in organizations [62,8,7]. For example, assertive behavior implies power, whereas upward appeal and ingratiation imply a lack of resource or dependence on others.

![](/api/attachments/9K764B86/fulltext/images/fdacc53503759201e41b272e94276da77c5e1251c3925c5b401b96d60450dc34.jpg)  
Fig. 1. The research model.

The possible impact of deceptive intent on power or in<sup>fl</sup>uence of a deceiver in a network is not straightforward, because in terms of strategic moves and control attempts in interaction, deceptive communication is expected to be in<sup>fl</sup>uenced by two types of strategies: persuasive and protective strategies [10]. During deception, a deceiver engages in greater strategic activity that is designed to manage information, behavior, and image as the interaction unfolds. On the one hand, a deceiver aims to persuade or mislead others into a false belief about a certain topic; on the other hand, the deceiver has to pretend to be innocent or trustworthy in order to protect himself/herself from being caught in deception. These two dichotomous strategies in deceptive interaction fundamentally affect behaviors of deceivers [10], including structural behaviors. In social interaction, a deceiver should juggle between being in a dominant position to deceive others (persuasive) and being passive and submissive to avoid detection [77]. Negotiation research has also shown that bargaining tactics typically deal with gaining information from one's opponent while concealing information about oneself [39,43]. Therefore, we expect that the impact of deceptive intent on centrality vary with speci<sup>fi</sup>c centrality metrics that have differing implications for power or in<sup>fl</sup>uence.

The simplest and intuitively obvious concept of centrality is based on the degree of an actor, the number of nodes to whom an actor is directly tied. According to Freeman [28], degree centrality implies the visibility or the potential for activity in communication. In directed networks, degree centrality can be divided into the degree count for incoming ties (in-degree or prestige) and for outgoing ties (out-degree). An actor with high in-degree centrality in<sup>fl</sup>uences other actors as far as his or her opinions are taken into account, and an actor with high outdegree centrality is in an advantaged position by making more choices for satisfying needs and being less dependent on other actors [16]. Depending on the type of ties (e.g. supervisory relation and seeking advice), either in-degree or out-degree measures may be interpreted as prominence or in<sup>fl</sup>uence [60,75].

An actor, who intends to deceive others in an interactive context where actors are ‘engaged’ with one another on a voluntary basis, should take a more in<sup>fl</sup>uential role than a truth-telling actor. In such informal group CMC, however, an individual can take charge of whom he responds to, but have little control over who responds to him. In search engines, pages with higher in-degrees are more likely to be authorities [45]. Moreover, according to preferential attachment on directed graphs [18], nodes receive new links in proportion to their in-degree. Thus, indegree centrality is a better indicator of prominence in a network of social interaction than out-degree centrality is. Accordingly, the in<sup>fl</sup>uence of a deceiver can be manifested in his high in-degree, and the <sup>fi</sup>rst hypothesis is proposed as follows:

H1-a. Deceivers have a higher level of in-degree centrality than truth-tellers.

Out-degree as well as in-degree centrality is eventually useful to explaining the level of communication activity. Given that deceivers are less-forthcoming than truth-tellers [22], we argue that deceptive intent also has effect on out-degree. In CMC, individuals who normally do not have the ability to form a social relationship are free to share information [65], and the sharing takes place in informal communication <sup>fl</sup>ow and barter of the interactions [21]. A deceiver is less likely to engage in information sharing because of his or her hidden deceptive agenda, but he or she is more likely to suppress own communication activity or visibility to protect himself/herself from suspicion of receivers [78,84]. Consequently, a deceiver speaks or writes less and in less detail. The deceivers attempt of holding back also helps him or her to minimize possible discrepancies resulting from his/her inability to control all aspects of behavior equally. Thus, we propose that:

H1-b. Deceivers have a lower level of out-degree centrality than truth-tellers.

Betweenness centrality focuses on the extent to which actors are strategically located on the shortest paths between other pairs of actors [26]. An actor can in<sup>fl</sup>uence a group by withholding or distorting information in transmission [57,7,35]. Such a position would offer the deceiver an advantage in manipulating information, which is crucial to the success of deception. No matter whether the manipulation of information is accomplished through falsi<sup>fi</sup>cation (deliberately creating false information), concealment (hiding relevant information), or equivocation (skirting issues by changing the subject or offering indirect responses) [10,24,2], the deceiver is expected to occupy a high-betweenness position in order to control communication and coordinate group processes by conveying false, incomplete, or vague information.

H1-c. Deceivers have a higher level of betweenness centrality than truth-tellers.

Closeness centrality is measured as a function of geodesic distance (shortest path) [28], namely the inverse of the average geodesic distance between an actor and all other actors in the network. This centrality suggests two intuitions about the role of an actor: control of communication and ef<sup>fi</sup>ciency of information <sup>fl</sup>ow [7]. First, the control of communication represents a different dimension from other centrality measures [75], which determines structural interdependence of an actor by the extent to which an actor can avoid the potential control of others [35]. For instance, an actor taking a non-central position in a network in terms of closeness would depend on others as an intermediary of messages. Second, the ef<sup>fi</sup>ciency of information <sup>fl</sup>ow is positively associated with the notion of closeness in terms of fewer message transmissions, shorter time and lower costs in spreading information to other actors in a network. In general, deception requires more cognitively complex processes than stating the truth because a deceiver needs to not only come up with deceptive messages that are different from what he or she really believes but also sift through his or her mind to <sup>fi</sup>nd any hint of a seemingly plausible reason to justify the message in case of being questioned [10,76,77]. Deception is often described as an adversarial game, which involves unexpected words, nonverbal leakage, strategic thinking, and emotion. Depending on the others' feedback or response, a deceiver has to adjust his or her behavior and strategic moves. As a result, the deceiver is more deliberate in self-regulating his or her behavior, thoughts and feeling, and is more likely to usurp mental resources than a truth-teller [22], leaving him or her with less cognitive capacity available for maintaining a close relationship with the rest of the group. In addition, a study of terrorist networks has shown that their members are likely to prioritize security over ef<sup>fi</sup>ciency over the execution of any single attack [54]. In a similar vein, a deceiver who interacts with multiple receivers is likely to prefer the protective strategy when faced with the tradeoff between ef<sup>fi</sup>ciency and security [80].

H1-d. Deceivers have a lower level of closeness centrality than truth-tellers.

## 3.2. Cohesion

Structural cohesion is an important feature of the relational dimension of social solidarity and subgroups. Structural cohesion refers to the psychological identi<sup>fi</sup>cation of members within a collectivity and a relational component, which shows the patterns of multiple connections within the group [53]. The members of larger groups are rarely connected directly to all other members, and consequently subgroups are likely to form [25]. For example, if kinship or friendship exists between actors in a group, they are connected to one another with stronger interpersonal ties, and accordingly this subgroup is more cohesive, compared with other actors. The identi<sup>fi</sup>cation of such subgroup provides an understanding of information and resource <sup>fl</sup>ow, access to information, and allocation of power in a social structure [29,30]. To support subgroup identi<sup>fi</sup>cation, it is useful to understand how a cohesive group of actors is embedded in a network.

In a group that involves a single deceiver, the deceiver is the minority. When trying to in<sup>fl</sup>uence other group members, the minority tends to team up with people who are similar to self because it is easier for one to in<sup>fl</sup>uence others when he or she is a part of in-group [49]. In addition, the overall success of deception often hinges on building ‘trust’ relationship with other members through initial displays. In order to establish the trust relationship, an individual with deceptive intent has to act like collaborating with others. Moreover, the establishment of trust relationship at an early stage would help the deceiver to push his or her own agenda to his or her supporting group later. Studies of criminal networks have shown that the networks often can be partitioned into subgroups consisting of individuals who closely interact with one another [20,41,72]. Therefore, we propose the following hypothesis:

H2. Deceivers have a higher level of cohesion than truth-tellers.

## 3.3. Similarity

Structural similarities can be measured at the levels of individual actors, subgroups within the entire network, and the entire network [56]. Given the focus of this study on deception behavior, structural similarity was measured at the level of individual actors (i.e., egonetwork) as were other structural constructs. Structural similarity is fundamentally related to structural equivalence, which measures the degree to which actors are similar. The construct has served to identify sets of actors who are very similar to one another, and distinct from actors in other sets [38].

Friedkin [29] suggests that structural similarity is based on interpersonal solidity and identi<sup>fi</sup>cation. The more similar the two actors' structural positions, the more similar their initial orientations on issues are likely to be. Conversely, the more discrepant between actors' initial orientations on issues, the more dissimilar are their structural positions. In contrast with truth-tellers, deceivers approach the group task or the target issue with distinctively different intentions and motives from other receivers. This sets deceivers' strategic and/or nonstrategic choices in terms of with whom to interact and how often to interact apart from those of truth-tellers, which in turn lead to different structural embeddedness. Therefore, we propose the last hypothesis as follows:

H3. Deceivers have a lower level of similarity to other receivers than truth-tellers.

## 4. Research methods

In this section, we introduce research methods in detail, including data collection, social network construction, and operationalization of social structure constructs.

## 4.1. Data collection

The data was collected from a ma<sup>fi</sup>a game website [63]. This game contains a deceiving role, who is motivated to deceive in order to win the game. Additionally, the game proceeds by rounds, which allows deception to unfold over time. The simplest version of the game was selected in this study to minimize possible confounding effects of other factors. This game setup consists of seven players divided into two groups: ma<sup>fi</sup>a sided (i.e. ma<sup>fi</sup>a and hooker) and non-ma<sup>fi</sup>a sided players (i.e. cop, watcher, and three villagers). The objective of the ma<sup>fi</sup>a game is to eliminate the opponent group. We randomly selected 72 games, and their outcomes are equally divided between the two opposing groups.

The game is played via online chat rooms. Each round of the game consists of two stages: day and night. During the day, all players discuss and make collective decisions about who the ma<sup>fi</sup>a might be via voting. The player who gets the most votes would be eliminated from the game. During the night, the ma<sup>fi</sup>a kills (eliminates) one of non-ma<sup>fi</sup>a sided players, and the cop selects one of the other surviving players for investigation and accumulates the identity of that player. The game continues to the next round until only one of the two opposing groups has surviving members, and the surviving side would win the game [9]. The game has set rules against disruptive acts such as self-voting and inactive players. In such cases, players would receive warning and suspension from the game. Further, a player who does not participate actively is more likely to become a target of early elimination because players tend to vote randomly on the <sup>fi</sup>rst day of the game.

All the roles are randomly assigned. Each player is only aware of his or her own role in the game except for the ma<sup>fi</sup>a sided players who are informed of the identities of other members in the same group. In order to win, the ma<sup>fi</sup>a player intends to deceive about his/her own and others' true identity, while the cop is expected to share what he/she truly knows about other players during a game. Therefore, the ma<sup>fi</sup>a player was treated as the deceiver and the cop as the truth-teller in the current study.

## 4.2. Social network construction

To construct social networks from online chat sessions, we need to identify two types of elements: nodes and links. The nodes were identi<sup>fi</sup>ed by extracting unique identi<sup>fi</sup>ers of game players from chat logs. The identi<sup>fi</sup>er of each player is automatically attached to the beginning of messages sent by the player.

The identi<sup>fi</sup>cation of links between nodes, which is more complex than node extraction, was implemented by inferring interactional coherence between chat messages. In this study, interactional coherence was analyzed with heuristic rules that infer ‘reply-to’ relationships between exchanged messages. The rules were initially developed based on unique features of CMC such as disrupted turn-taking and ambiguity of sequential coherence [3, 40] and then adapted and expanded for inferring underlying communication relationships among nodes [47,55]. Speci<sup>fi</sup>cally, four types of heuristic rules were used to infer ‘reply-to’ relationships, including direct addressing of users, temporal proximity, temporal density, and monitoring coherence of messages [45,49–51, 59].

In order to resolve the ambiguity of conversational and textual coherence in group communication, message coherence was analyzed based on both linguistic cohesion and conversational structure [31] in this study. Linguistic cohesion indicates semantic relations between text elements in a discourse [32], which was assessed using the following <sup>fi</sup>ve cues [36]: reference (words used to refer back to previously mentioned subjects), substitution (words used instead of another), ellipsis (connection becomes clear through the exclusion of certain words), conjunction (segments linked through speci<sup>fi</sup>c linking words), and lexical cohesion (links created through lexical repetition). Conversational structure, on the other hand, re<sup>fl</sup>ects the role that given sentences, phrases, or utterance play in a conversation. More detail about interactional coherence analysis can be found in Appendix A.

The procedure of social network construction is illustrated with the following sample chat messages, where pi (i = 1,2,3) denotes identi-<sup>fi</sup>ers of three different players.

p1: p2, are you mafia though? p2: No p3: mafia here p3: btw

First, three unique identi<sup>fi</sup>ers of players were extracted from the chat messages, which make three nodes in the network. Second, an analysis of interactional coherence between chat messages shows that the <sup>fi</sup>rst message directly addresses p2, which is immediately followed by a message from p2, and thus there exists a ‘reply-to’ relationship between the second message and the <sup>fi</sup>rst message. Similarly, based on an analysis of coherence of messages, the third message references and is in proximity to the <sup>fi</sup>rst message, so a ‘reply-to’ relationship also exists between the two messages. Finally, a social network is constructed that consists of three nodes (p1, p2, p3) and two links (p2–p1, p3–p1).

Following the above procedure, we constructed social networks for each of the selected games through a manual analysis of chat messages. At the beginning, a subset of 14 games was randomly selected and analyzed by two coders independently. An analysis of the inter-rater reliability of the two coding results showed that the kappa statistics was 0.64, which was moderately satisfactory. The inconsistent results were resolved through face-to-face discussion, which led to re<sup>fi</sup>nement of some heuristic rules and chatting acts, as introduced above. The revised heuristic rules and chatting acts were then used to analyze the remaining games as well as re-analyze the 14 games.

4.3. Operationalization of independent and dependent variables

## Independent variable:

• Deceptive Intent: It is a binary variable with two possible values: deceiving (i.e., the ma<sup>fi</sup>a player) and truth-telling (i.e., the cop player).

Dependent Variables:

• Centrality: It was measured with four variables [5]:

o In-degree: the number of edges that point toward the node of interest.

o Out-degree: the number of edges that point from the node of interest.

o Closeness: an inverse of the sum of the shortest distances from the focal node to all other nodes.

o Betweenness: the number of times a node occurs on a geodesic path between a pair of other nodes.

• Cohesion: Structural cohesion was operationalized as a dimension of social embeddedness based on communication connectivity in terms of clustering coef<sup>fi</sup>cient [53], which measures the degree to which actors in a network tend to cluster together. Clustering coef<sup>fi</sup>cient is de<sup>fi</sup>ned as the number of edges connecting a node's neighbors divided by the total number of possible edges between the node's neighbors [5].

• Similarity: Structural similarity was calculated based on the pattern of relations of the target actor to a group of other referencing actors [38], and the group of villagers was selected as the referencing actors in this study. The similar was measured as the Pearson correlation coef<sup>fi</sup>cient [69], where +1.00 indicates a perfect structural equivalence between two nodes, and −1.00 an exact opposite.

## 5. Data analyses and results

A total of 72 seven-node networks were constructed, the values of social structural variables were computed with UCINET [5]. The descriptive statistics is reported in Table 1.

A paired-sample t-test was performed to test the hypotheses, and the results are reported in Table 2. The results show that deceivers have a higher level of in-degree centrality (p b .05), betweenness centrality (p b .01), and clustering coef<sup>fi</sup>cient (p b .001), and a lower level of closeness centrality (p b .01) and structural similarity (p b .01), in comparison with truth-tellers. However, the analysis on outdegree did not yield signi<sup>fi</sup>cant result. Thus, hypotheses H2 and H3 were supported and hypothesis H1-a partly supported.

## 6. Discussion

## 6.1. Major findings and alternative explanations

The study examined deception behavior in CMC via the lens of social structure. Our proposed research model of social structural behavior of online deception was largely supported by the results of an empirical study. The <sup>fi</sup>ndings of this study show that deceivers <sup>fi</sup>nd themselves in different types of social structures characterized by centrality, cohesion, and similarity from truth-tellers.

As predicted, deception has an in<sup>fl</sup>uence on most of the centrality measures. Speci<sup>fi</sup>cally, deceptive intent has a positive impact on betweenness centrality and a negative impact on in-degree and closeness centralities. However, deception was not found to have an effect on out-degree centrality. We can provide the following alternative explanations. First, the out-degree centrality is used to measure the ability of an individual to interact directly with many others, or to make many others aware of his or her views [38]. Deception is driven by intent, which is usually hidden or not easily observable to enhance the chance of deception success [48]. Thus, in CMC where participants have the control over the frequency and the targets of their interactions, a deceiver would shun away from disclosing his/her viewpoint in order to protect himself/herself. Second, given that out-degree centrality re<sup>fl</sup>ects a level of productivity [46], the lack of effect of out-degree centrality in this study con<sup>fi</sup>rms the <sup>fi</sup>nding of an earlier study of online deception behavior [76]. Third, as suggested by previous research on deception and adaptive interaction, deceivers tend to control and maintain appropriate conversational involvement depending on receivers' reactions and other contextual factors [68]. For instance, deceivers show non-signi<sup>fi</sup>cant increase in response to increased receiver involvement, while compensating decreased receiver involvement. Thus, the compensation and reciprocity relationship between deceivers and truth-tellers in synchronous CMC would reduce the difference in their levels of involvement.

Table 1  
Descriptive statistics of the social structural behaviors.

<table><tr><td rowspan="2">Social network measures</td><td colspan="2">Min</td><td colspan="2">Max</td><td colspan="2">Mean</td><td colspan="2">Std. dev.</td><td colspan="2">Std. error</td></tr><tr><td>T</td><td>D</td><td>T</td><td>D</td><td>T</td><td>D</td><td>T</td><td>D</td><td>T</td><td>D</td></tr><tr><td>In-degree</td><td>0</td><td>0</td><td>7</td><td>7</td><td>4.01</td><td>4.62</td><td>1.674</td><td>1.706</td><td>.197</td><td>.201</td></tr><tr><td>Out-degree</td><td>0</td><td>1</td><td>7</td><td>7</td><td>3.98</td><td>4.04</td><td>1.756</td><td>1.336</td><td>.207</td><td>.158</td></tr><tr><td>Betweenness</td><td>0</td><td>0</td><td>13.33</td><td>6</td><td>1.35</td><td>2.62</td><td>2.167</td><td>2.008</td><td>.255</td><td>.267</td></tr><tr><td>Closeness</td><td>.09</td><td>0</td><td>.20</td><td>.20</td><td>.853</td><td>.056</td><td>.031</td><td>2.112</td><td>.004</td><td>.247</td></tr><tr><td>Clustering coefficient</td><td>0</td><td>0</td><td>1.00</td><td>1.51</td><td>.669</td><td>.842</td><td>.236</td><td>.260</td><td>.028</td><td>.031</td></tr><tr><td>Similarity</td><td>-.237</td><td>-.276</td><td>0.424</td><td>0.340</td><td>.427</td><td>.131</td><td>.600</td><td>.705</td><td>.071</td><td>-.083</td></tr></table>

T: truth-teller; D: deceiver.

As expected, deceivers show a higher level of cohesion than truthtellers, which is also consistent with the <sup>fi</sup>ndings from the analyses of terrorist networks [70,71,73]. Additionally, the <sup>fi</sup>nding that deceivers are less similar to other receivers than truth-tellers con<sup>fi</sup>rms our prediction, which provides fundamental evidence that deception leads to a different social structure.

## 6.2. Research implications

The <sup>fi</sup>ndings of this study extend extant theories and research on explaining the impact of deceptive intent on online behavior in multiple aspects. First, to the best of our knowledge, this is the <sup>fi</sup>rst study that investigates deception behavior in CMC via the lens of social structure. To address one major limitation of previous studies of online deception [83], this research extends the scope of online deception behavior by exploring non-verbal behavior with respect to social structure. Second, our <sup>fi</sup>ndings with regard to centrality, cohesion, and similarity of social structure of deceptive interactions provide empirical evidence in support of the proposed social structural approach to deception in group communication. In addition, this research creates new knowledge about deception behavior concerning the social interaction between the deceiver and receivers. Third, the differing impacts of deceptive intent on various centrality measures highlight the importance of studying the centrality of deceptive communication in multiple dimensions. Fourth, this research develops heuristic rules and chat acts based on interaction coherence analysis to identify ‘replyto’ relations in CMC in social network construction. Last but not the least, our <sup>fi</sup>ndings provide empirical support for the generalizability of tradition deception theories [10,14,52,74] to CMC. The theories propose that deception is a strategic activity where the deceiver juggles between the dual goals of promoting his deceptive agenda to and preventing himself from detection and even suspicion by the receivers.

Table 2  
Paired-sample t-test results.

<table><tr><td>Hypothesis</td><td>Social structural behavior</td><td>Measures</td><td>Mean difference (D-T)</td><td>Std. error</td><td>p-Value</td></tr><tr><td>H1-a</td><td></td><td>In-degree</td><td>.603</td><td>.259</td><td>.023*</td></tr><tr><td>H1-b</td><td>Centrality</td><td>Out-degree</td><td>.041</td><td>.239</td><td>.864</td></tr><tr><td>H1-c</td><td></td><td>Closeness</td><td>-.793</td><td>.247</td><td>.002**</td></tr><tr><td>H1-d</td><td></td><td>Betweenness</td><td>1.227</td><td>.371</td><td>.001**</td></tr><tr><td>H2</td><td>Cohesion</td><td>Clustering coefficient</td><td>.177</td><td>.038</td><td>.000***</td></tr><tr><td>H3</td><td>Similarity</td><td>Correlation coefficient</td><td>-.296</td><td>.105</td><td>.003**</td></tr></table>

p b .05.  
\*\* p b .01.  
⁎⁎⁎ p b .001.

Our <sup>fi</sup>ndings that deception leads to higher in-degree and betweenness centralities and lower closeness centrality have two important implications: 1) different centrality measures have different implications for the power and in<sup>fl</sup>uence of deceptive communication; and 2) deceivers strategically position themselves in a social network while leaking non-strategic behavior via social structure. Speci<sup>fi</sup>cally, the <sup>fi</sup>nding on in-degree centrality of deceivers suggests that deceivers attempt to take a prominent position by engaging receivers in social interaction to gain trust and cooperation of the receivers; the <sup>fi</sup>nding on betweenness centrality implies that deceivers seek to allow, withhold, or distort incoming and outgoing communication of receivers by exerting control over information transfer and diffusion in a network; and the <sup>fi</sup>nding on closeness centrality indicates that, while deceivers are more distant from and thus less ef<sup>fi</sup>cient in accessing receivers in communication networks than truth-tellers, deceivers are more independent of others' control or less reliant on others to get access to information. Consistent with the view that deception is a cognitively taxing process that engages both strategic and non-strategic behaviors during interactions, the <sup>fi</sup>ndings on centrality as a whole imply that the deceiver holds a favorable position as a mediator or a broker in an adversarial network that provides opportunities for him to persuade and in<sup>fl</sup>uence others through exclusive access to resources (e.g., information [17,35,38]) while simultaneously limiting his effort in reaching out to many receivers to protect his deceptive intent from getting noticed or arousing suspicion.

The <sup>fi</sup>nding that deceivers are more likely to belong to tightly knit groups than truth-tellers suggests that deceivers form alliance with receivers in order to gain credibility and get access to information. It is part of a deceiver's strategic move to build a sense of trust and rapport with receivers in the same group. Forming an alliance with receivers is a strategic move on the deceiver's side, which may help him/her to push for his/her agenda or false information

Deceivers are structurally less similar to receivers than truth-tellers in terms of ties to receivers. This <sup>fi</sup>nding suggests that deceivers are embedded in a different type of social structure from truth-tellers. Moreover, it provides strong evidence for the validity of the social structural approach to studying online deception, and shed light on structural behaviors of deceivers in CMC groups.

## 6.3. Practical implications

This research provides several practical implications. First, the structural deception behavior identi<sup>fi</sup>ed in this study can be used to enhance human users' ability to detect online deception and to develop automatic deception detection solution. For instance, the <sup>fi</sup>ndings of the current study can be used to enrich training material on deception behavior and increase awareness of online deception for both professionals and laypersons in deception detection. Second, advancing our knowledge about online deception behavior or cues to online deception can aid promoting a more secure and trustworthy cyberspace, where social media users may develop trust relationships, online businesses may identify credible and in<sup>fl</sup>uential customers and gain knowledge about particular products or markets for viral marketing, and government agencies may uncover and prevent online deception, fraud, and crime. Third, the proposed methods for analyzing social interaction in CMC expand the application of social network analysis techniques to addressing broad online behaviors.

## 6.4. Limitations and future directions

This study exposes several limitations and raises important research issues for further inquiry on deception behavior in CMC. First, in addition to the three types of social structural behaviors examined here, other characteristics of social structure such as embeddedness are worthy of exploration for online deception. Second, we did not consider the dynamics of social structural behaviors despite of the panel data collected in this study. A follow-up analysis of temporal patterns of structural behavior of deceptive communication is warranted, using techniques such as dynamic network analysis [19]. A third limitation is that the social structural behaviors in our research model were operationalized on unweighted networks, which overlook the intensity of ties or relationships between actors. Fourth, this study is solely focused on social structural behaviors of deceptive communication, and future studies should combine the new insights gained on structural behavior with prior <sup>fi</sup>ndings on verbal behavior of online deception to improve the performance of deception detection. Last but not the least, although our <sup>fi</sup>ndings extends the dimension of online deception behavior to social structure, we did not sample broadly across communication media. Future research to replicate our <sup>fi</sup>ndings in CMC settings with varying levels of synchronicity should be conducted.

## 7. Conclusion

Deception hampers the effective use of CMC for both personal and business purposes. In this article, building on the notion that deception is a type of social interaction, we proposed a social structural approach to investigating online deception behavior. Drawing from deception and social network theories, we developed a research model of structural behaviors of deception. The results of an empirical study largely supported the model, showing that deception in<sup>fl</sup>uences three types of structural constructs — centrality, cohesion, and similarity. In addition, the impacts of deception on centrality varied depending on the type of centrality measures. Our <sup>fi</sup>ndings provide new insights into deception behavior by looking into how deceivers position themselves in a network structure established through social interaction. Speci<sup>fi</sup>cally, deceivers gain power over others in a network not by reaching out or getting publicity, but rather by the means of controlling resource accessible to others, gaining prominence, and forming supporting groups through trust building. These <sup>fi</sup>ndings highlight that deception is a strategic activity where the deceivers manage the trade-off between persuasive and protective strategies in interaction with receivers. This research has important implications for both research and practice as online deception continues to evolve in the networked economy.

## Acknowledgments

This research is supported in part by UMBC DRIF, the National Science Foundation (IIS-1250395), and a Department of Education GAANN Fellowship (P200A120100). Any opinions, <sup>fi</sup>ndings or recommendations expressed here are those of the authors and are not necessarily those of the sponsors of this research.

## Appendix A

Rules for inferring relationships among nodes.

<table><tr><td>Category</td><td></td><td>Description</td><td>Example</td></tr><tr><td rowspan="4">Linguistic feature</td><td>Direct addressing</td><td>If a message directly addresses another user&#x27;s ID, then a relationship is established between the sender and the addressee.</td><td>A: B, are you mafia though?B: No</td></tr><tr><td>Reference</td><td>If a message contains ‘you’ to reference someone, or if a message repeats the words or phrases mentioned in an earlier message; then a relationship is established between the senders of the messages.</td><td>A: lynch this grammar naziB: I&#x27;m not a grammar nazi.C: I am a grammar nazi you know.</td></tr><tr><td>Substitution</td><td>If a message contains words as substitutes for something or someone mentioned in an earlier messages, then a relationship is established between the senders of the messages.</td><td>A: Da is afk.B: hes not there</td></tr><tr><td>Conjunction</td><td>If two messages are connected with a conjunction, then a relationship is established between the senders of the messages.</td><td>A: I&#x27;ll be on youB: and then the persons nameA: You be on me</td></tr><tr><td rowspan="2">Conversational Feature</td><td>Question-Answer</td><td>If one message contains conversational initiation (e.g., wh-question, declarative question, and yes/no question), and another message contains conversational response to the previous messages (e.g., answer, agreement, and disagreement), then a relationship is established between the senders of the messages.</td><td>A: Do you have to have any special training?B: No, I haven&#x27;tA: Well, how old are you?B: 18 yrsA: So you&#x27;re taking a government course?B: Not really?!?</td></tr><tr><td>Statement/Opinion</td><td>If one message contains a statement or an opinion and a following message contains a response (e.g., acknowledgment, accept, and reject), then a relationship is established between the senders of the messages.</td><td>A: He&#x27;s probably, oh, a good two years old, big, old,B: Nah, He&#x27;s about five months old Well,A: rabbits are darling.B: I think it would be kind of stressful.</td></tr></table>

Please cite this article as: J. Pak, L. Zhou, Social structural behavior of deception in computer-mediated communication, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.010

## References

[1] J.Q. Anderson, L. Rainie, The Future of Social Relations, Pew Internet & American Life Project, http://www.pewinternet.org/Reports/2010/The-future-of-social-relations. aspxJuly 10 2010[accessed on May 10, 2012].

[2] L. Anolli, M. Balconi, R. Ciceri, Deceptive Miscommunication Theory (DeMiT): A New Model for the Analysis of Deceptive Communication, in: R.C., G.R., L. Anolli (Eds.), Say Not to Say: New Perspectives on Miscommunication, IOS Press, 2001.

[3] T.Ö. Berglund, Disrupted turn adjacency and coherence maintenance in instant messaging conversations, Language @ Internet 6 (2009).

[4] P.M. Blau, Exchange and Power in Social Life, Transaction Publishers, 1964.

[5] S.P. Borgatti, M.G. Everett, L.C. Freeman, UCINET 6 for Windows Software for Social Network Analysis, Analytic Technologies, Harvard, MA, 2002.

[6] S.P. Borgatti, P.C. Foster, The network paradigm in organizational research: a review and typology, Journal of Management 29 (2003) 991–1013.

[7] D.J. Brass, M.E. Burkhardt, Potential power and power use: an investigation of structure and behavior, Academy of Management Journal 36 (1993) 441–470.

[8] D.J. Brass, K.D. Butter<sup>fi</sup>eld, B.C. Skaggs, Relationship and unethical behavior: a social network perspective, Academy of Management Review 23 (2012) 14–31.

[9] M. Braverman, O. Etesami, E. Mossel, Ma<sup>fi</sup>a: a theoretical study of players and coalitions in a partial information environment, The Annals of Applied Probability 18 (2008) 825–846.

[10] D.B. Buller, J.K. Burgoon, Interpersonal deception theory, Communication Theory 6 (1996) 203–242.

[111 IK. Burgoon, I.A. Bonito, B. Bengtsson, C. Cederberg, M. Lundeberg, I. Allspach, Interactivity in human–computer interaction: a study of credibility, understanding, and in<sup>fl</sup>uence, Computers in Human Behavior 16 (2000) 553–574.

[12] J.K. Burgoon, J.A. Bonito, A. Ramirez, N.E. Dunbar, K. Kam, J. Fischer, Testing the interactivity principle: effects of mediation, propinquity, and verbal and nonverbal modalities in interpersonal interaction, The Journal of Communication 52 (2002) 657–677.

[13] J.K. Burgoon, D.B. Buller, Interpersonal deception: III. Effects of deceit on perceived communication and nonverbal behavior dynamics, Journal of Nonverbal Behavior 18 (1994).

[14] J.K. Burgoon, D.B. Buller, L. Guerrero, W. A<sup>fifi</sup>, C. Feldman, Interpersonal deception: XII. Information management dimensions underlying deceptive and truthful messages, Communication Monographs 63 (1996) 50–69.

[15] J.K. Burgoon, T. Qin, The dynamic nature of deceptive verbal communication, Journal of Language and Social Psychology 25 (2006) 76–96

[16] M.E. Burkhardt, D.J. Brass, Changing patterns or patterns of change: the effects of a change in technology on social network structure and power, Administrative Science Quarterly 35 (1990) 104.

[17] R.S. Burt, The network structure of social capital, Research in Organizational Behavior 22 (2000) 345–423.

[18] A. Capocci, V.D.P. Servedio, F. Colaiori, L.S. Buriol, D. Donato, S. Leonardi, et al., Preferential attachment in the growth of social networks: the internet encyclopedia Wikipedia, Physics Review E 74 (2006).

[19] K.M. Carley, Dynamic networks: what is a network? Knowledge Creation Diffusion Utilization, 2012. 1–63.

[20] H. Chen, W. Chung, J.J. Xu, G. Wang, Y. Qin, M. Chau, Crime data mining: a general framework and some examples, Computer 37 (2004) 50–56

[21] C.U, Ciborra, R. Andreu, Sharing knowledge across boundaries, Journal of Information Technology 16 (2001) 73–81.

[22] B.M. DePaulo, J.J. Lindsay, B.E. Malone, L. Muhlenbruck, K. Charlton, H. Cooper, Cues to deception. Psychological Bulletin 129 (2003) 74-118

[23] H. Du, S.J. Yang, Discovering collaborative cyber attack, SBP2011, Springer, 2011, pp. 129–136.

[24] P. Ekman, Lying and deception, in: N.L. Stein, P.A. Ornstein, B. Tversky, C. Brainerd (Eds.), Memory for Everyday and Emotional Events, Lawrence Erlbaum Associates, Mahwah, New Jersey, 1997.

[25] D.R. Forsyth, Group Dynamic, Wadsworth, Cengage Learning, Belmont, CA, 2010.

[26] L.C. Freeman, Centrality in social networks conceptual clari<sup>fi</sup>cation, Social Networks 1 (1979) 215–239.

[27] L.C. Freeman, The Development of Social Network Analysis: A Study in the Sociology of Science, Empirical Press, 2004.

[28] L.C. Freeman, D. Roeder, R. Mulholland, Centrality in social networks: II, Experimental Results 2 (1979) 119–141

[29] N.E. Friedkin, Structural bases of interpersonal in<sup>fl</sup>uence in groups: a longitudinal case study, American Sociological Review 58 (1993) 861–872

[30] N.E. Friedkin, Social cohesion, Annual Review of Sociology 30 (2004) 409–425.

[31] T. Fu, A. Abbasi, H. Chen, A hybrid approach to web forum interactional coherence analysis, Journal of the American Society for Information Science 59 (2008) 1195–1209.

[32] T. Fu, H. Chen, Analysis of Cyberactivism: Analyzing Content Development and A Case Study of Online Free Tibet Activities Visualizing Social Interactions in Web Forum, Arti<sup>fi</sup>cial Intelligence (2008) 0–5.

[33] M.M. Fuller, A. Wagner, B.J. Enquist, Using network analysis to characterize forest structure, Natural Resource Modeling 21. (2008) 2–4

[34] G.A. Giordano, J.S. Stoner, R.L. Brouer, J.F. George, The in<sup>fl</sup>uences of deception and computer-mediation on dyadic negotiations, Journal of Computer-Mediated Communication 12 (2007) 362-383

[35] E.M. Hafner-burton, A.H. Montgomery, Centrality in Politics: How Networks Confer Influence, Human Rights. , 2010. 1–21,

[36] M.A.K. Halliday, R. Hasan, Cohesion in English, Longman, London, 1976.

[37] J.T. Hancock, L. Curry, S. Goorha, M. Woodworth, On lying and being lied to: a linguistic analysis of deception in computer-mediated communication, Discourse Processes 45 (2008) 1–23.

[38] R.A. Hanneman, M. Riddle, Introduction to Social Network Methods, Published University of California, Riverside, CA, 2005.

[39] K. Hausken, Game-theoretic and Behavioral Negotiation Theory, Group Decision and Negotiation 6 (1997) 511–528.

[40] S.C. Herring, Interactional coherence in CMC, Proceedings of the 32nd Annual Hawaii International Conference on Systems Sciences, IEEE, 1999, p. 13.

[41] C.E. Hutchins, M. Benham-Hutchins, Hiding in plain sight: criminal network analysis, Computational and Mathematical Organization Theory 16 (2009) 89–111.

[42] C. Kadushin, Introduction to Social Network Theory: Some Basic Network Concepts and Propositions, 2004.

[43] P.H. Kim, Power dynamics in negotiation, Academy of Management Review 30 (2005) 799–822.

[44] C. Kiss, M. Bichler, Identi<sup>fi</sup>cation of in<sup>fl</sup>uencers — measuring in<sup>fl</sup>uence in customer networks, Decision Support Systems 46 (2008) 233–253.

[45] J. Kleinberg, Authoritative sources in a hyperlinked environment, Journal of the ACM 46 (1999) 604–632.

[46] Z. Kozareva, E. Riloff, E. Hovy, Semantic class learning from the web with hyponym pattern linkage graphs, Proceeding of ACL-08:HLT, 2008, pp. 1048–1056.

[47] I. Lakatos, The Methodology of Scienti<sup>fi</sup>c Research Programmes: Philosophical Papers, Cambridge University Press, 1978.

[48] D. Li, E. Santos, Deception detection in human reasoning, IEEE International Conference on Systems Man and, Cybernetics, 2011, pp. 165–172.

[49] A. Maass, R.D. Clark, Hidden impact of minorities: <sup>fi</sup>fteen years of minority in<sup>fl</sup>uence research, Psychological Bulletin 95 (1984) 428–450.

[50] M. Maccomascaigh, T. Bell, J. Murphy, Magic Quadrant for Web Content Management, Management, 2010. 1–24.

[51] L.K. Marett, J.F. George, Deception in the case of one sender and multiple receivers, Group Decision and Negotiation 13 (2004) 29–44.

[52] S. McCornack, Information manipulation theory, Communication Monographs 59 (1992) 1–16.

[53] J. Moody, D.R. White, Structural cohesion and embeddedness: a hierarchical conception of social groups, American Sociological Review 68 (2003).

[54] C. Morselli, C. Giguere, K. Petit, The ef<sup>fi</sup>ciency/security trade-off in criminal networks, Social Networks 29 (2007) 143–153.

[55] P. Mutton, Inferring and visualizing social networks on internet relay chat, Proceedings. 8th International Conference on Information Visualisation, IEEE, 2004, pp. 35–43.

[56] J. Scott, Social network analysis: a handbook, Contemporary Sociology 3 (2000) 208.

[57] M.E. Shaw, Group structure and the behavior of individuals in small groups, The Journal of Psychology 38 (1954) 139–149.

[58] K.E. Sip, J.C. Skewes, J.L. Marchant, W.B. McGregor, A. Roepstorff, C.D. Frith, What if I get busted? Deception, choice, and decision-making in social interaction, Frontiers in Neuroscience 6 (2012) 58.

[59] A. Stolcke, K. Ries, N. Coccaro, E. Shriberg, R. Bates, D. Jurafsky, et al., Dialogue act modeling for automatic tagging and recognition of conversational speech, Computational Linguistics 26 (2000) 339–373.

[60] M.T. Torfason, J.A. Kitts, Prominence, Encyclopedia of Social Networks, Sage Publications, George Bar, New York, 2010.

[61] J.H. Turner, A Theory of Social Interaction, Stanford University Press, Stanford, California, 1988.

[62] R. Vempati, V.R. Krishnan, Power and in<sup>fl</sup>uence strategies: an analysis across departments, NMIMS Management Review 12 (2000) 1–10

[63] P. Wang, Epic Ma<sup>fi</sup>a, http://wiki.epicma<sup>fi</sup>a.com/index.php?title=Main\_Page2012.

[64] S. Wasserman, K. Faust, Social network analysis: methods and applications, Social Networks 8 (1994) 825.

[65] B. Wellman, Designing the Internet for a networked society, Communications of the ACM 45 (2002) 91–96.

[66] B. Wellman, Network analysis: some basic principles, Network 1 (2007) 155–200.

[67] H.T. Welser, Visualizing the signatures of social roles in online discussion groups <sup>fi</sup>nding social roles in online discussion, 8 (2007) 1–32.

[68] J.K. White, C.H. Burgoon, Adaptation and communicative design: patterns of interaction in truthful and deceptive conversations, Human Communication Research 27 (2001) 9–37.

[69] S. Williams, Pearson's correlation coef<sup>fi</sup>cient, The New Zealand Medical Journal 109 (1996) 38.

[70] J.J. Xu, H. Chen, CrimeNet Explorer: A Framework for Criminal Network Knowledge Discovery, ACM Transactions on Information Systems 23 (2005) 201–226.

[71] J.J. Xu, B. Marshall, S. Kaza, H. Chen, Analyzing and visualizing criminal network dynamics: a case study, ISI 2004 LNCS 3073, Springer-Verlag, 2004, pp. 359–377.

[72] C.C. Yang, N. Liu, M. Sageman, Analyzing the terrorist social networks with visualization tools, Intelligence and Security Informatics, 2006, pp. 331–342.

[73] C.C. Yang, T.D. Ng, Terrorism and crime related weblog social network: link, content analysis and information visualization. 2007 IFFE Intelligence and Security Informatics JEFE 2007 pp.55-58

[74] L.N.T. Yeung, T.R. Levine, Information manipulation theory and perceptions of deception in Hong Kong, Communication Reports 12 (1999).

[75] B. Zemljič, V. Hlebec, Reliability of measures of centrality and prominence, Social Networks 27 (2005) 73–88.

[76] L. Zhou, An empirical investigation of deception behavior in instant messaging, IEEE Transactions on Professional Communication 48 (2005) 147–160.

[77] L. Zhou, J.K. Burgoon, J.F. Nunamaker, D. Twitchell, Automating linguistics-based cues for detecting deception in text-based asynchronous computer-mediated communications, Group Decision and Negotiation 13 (2004) 81–106

[78] L. Zhou, J.K. Burgoon, D.P. Twitchell, T. Qin, J.F. Nunamaker, A comparison of classi-<sup>fi</sup>cation methods for predicting deception in computer-mediated communication, Information Systems Management (2004) 139–165.

[79] L. Zhou, J.K. Burgoon, D. Zhang, J.F. Nunamaker, Language dominance in interpersonal deception in computer-mediated communication Computers in Human Behavior 20 (2004) 381–402.

[80] L. Zhou, Y. Sung, D. Zhang, Deception performance in online group negotiation and decision making: the effects of deception experience and deception skill, Group Decision and Negotiation 22 (2013) 153–172.

[81] L. Zhou, D. Zhang, A comparison of deception behavior in dyad and triadic group decision making in synchronous computer-mediated communication, Small Group Research 37 (2006) 140–164.

[82] L. Zhou, D. Zhang, Typing or messaging? Modality effect on deception detection in computer-mediated communication, Decision Support Systems 44 (2007) 188–201.

[83] L. Zhou, D. Zhang, Automatic deception detection in computer-mediated communi cation, IEEE Intelligent Systems (2012) 73–75.

[84] M. Zuckerman, B.M. DePaulo, R. Rosenthal, Verbal and nonverbal communication of deception, in: L. Berkowitz (Ed.), L. Berk (Ed.), Advances in Experimental Social PsychologyAcademic Press, New York, 1981, pp. 1–59.

Jinie Pak is a Ph.D doctoral candidate student of Information Systems at the University of Maryland, Baltimore County, USA. She received her masters degree in Information Systems from the University of Maryland, Baltimore County. Her research interests include online deception detection, social network analysis, dynamic network analysis, and social media

Lina Zhou is an Associate Professor of Information Systems, University of Maryland, Baltimore County, USA. Her current research interests include deception detection, ontology, social network analysis, and mobile web.
