---
otero_id: 3626
otero_key: "MGDRV3D4"
title: "Idea evaluation in innovation contest platforms: A network perspective"
authors: "A. Özaygen; C. Balagué"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.06.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Idea Evaluation in Innovation Contest Platforms: A Network Perspective

Decision Support Systems

A. Özaygen, C. Balagué

![](/api/attachments/MGDRV3D4/fulltext/images/511727e57fea670676bd9401a2bf88aaf971dce5573391589e8287c1030d639a.jpg)

PII: S0167-9236(18)30098-8

DOI: doi:10.1016/j.dss.2018.06.001

Reference: DECSUP 12959

To appear in: Decision Support Systems

Received date: 12 December 2017

Revised date: 29 April 2018

Accepted date: 7 June 2018

Please cite this article as: A. Özaygen, C. Balagué , Idea Evaluation in Innovation Contest Platforms: A Network Perspective. Decsup (2018), doi:10.1016/j.dss.2018.06.001

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Idea Evaluation in Innovation Contest Platforms: A Network Perspective

A. Ozaygen <sup>¨</sup> <sup>a,b,∗</sup>, C. Balagu´e<sup>a</sup>

<sup>a</sup>LITEM, Universit´e d’Evry, T´el´ecom Ecole de Management, Universit´e Paris-Saclay,<sup>´</sup> 91025, Evry, France

<sup>b</sup>(present address) Universit´e Paris-Sud, RITM, Facult´e Jean Monnet 54, boulevard Desgranges 92330 Sceaux, France

## Abstract

Innovation contest platforms are used to collect innovative ideas of consumers. Previous research on innovation contests has principally focused on participants’ idea generation. In this paper, we analyze ideas evaluation by participants in coopetitive crowd innovation contests within a network perspective. Using data from an innovation contest platform, we create a network of users through their interactions. Then, we measure the impact of participants’ centrality scores on received and given evaluation. Our results reveal that in-degree, out-degree and authority scores are correlated with the received positive evaluation, whereas authority is negatively correlated with the number of evaluations made. We also show that betweenness centrality and hub scores have no impact. By identifying the social influencers with network scores, we propose a methodology to reduce crowd innovation voting bias and to help managers to better select the ideas.

Keywords: innovation contest, user evaluation, social network analysis,

## 1. Introduction

Companies or non-profit organizations use crowd innovation contests to collect innovative ideas and to improve innovation processes [1, 2, 3, 4, 5]. Various firms such as Philips with “Simply Innovate” [6] , Procter & Gamble with “Connect + Develop” [7], Dell’s Idea Storm [5] or sites like yet2.com, NineSigma or InnoCentive [8] have been created in order to conduct such innovation contests. The main objective of these platforms is to generate new ideas either to solve a complex problem or to imagine a new product or service. Crowd innovation contests rely on the diversity of individuals’ talents who contribute with varied skills, experience and perspectives, helping to solve problems more eficiently [9].

There are three main challenges that an innovation contest must face. First, how to generate valuable ideas. Second, how to evaluate all the ideas provided in the platform in order to select the best ones. Third, how to merge ideas. Previous literature gathers several studies aiming at better understanding the idea generation process on crowd innovation contest platforms. It has been shown that ideas’ quality and quantity, as well as comments submitted on crowd innovation contests platforms are afected by parmotivations [10], number of participants [9] and prior knowledge [11]. Other studies have investigated the characteristics and roles of participants [12, 13], developed new key elements for an efective post-contest process [14], characterized the ideal user profiles of those who generate innovative ideas [15], studied the efect of diversity such as culture and national wealth on problem solving efort and success [16] and tested the efectiveness of the diferent coopetition models with respect to creative ideas generations [17]. The major challenge of ideas evaluation in crowd innovation contest has however sparsely been studied in previous literature. In this study, we aim at filling this gap. Generally, ideas and comments submitted by participants are evaluated within the same community, which presents a high benefit in terms of time and costs of screening the best ideas [18]. However, it is also shown that crowd voting processes introduce biases [19]. In this research, we study the participants’ evaluation role within the perspective of the social network theory, then we identify the potential social influencers to propose a methodology to reduce voting bias and to provide to managers more unbiased scores helping them to better select the most promising ideas. Hence, our research questions are:

• What is the impact of participants’ activities and network positions on ideas evaluation behavior in innovation contest platforms?

• What are the potential voting biases and how can we identify the social influencers?

• How can we reduce voting bias to better select the ideas?

In this study, we analyze a coopetitive innovation contest carried out for a major international brand in small household appliances. In this platform, users are allowed to propose ideas, to make comments on ideas, and to evaluate them. We consider that crowd innovation platforms are social networks, which were defined by Trusov et al. (2010) as sites with a collection of user profiles shared between participants, and users involvement in diferent shared activities. Based on ideas and comments, we created a network of participants interactions in crowd innovation. Using a data set of 498 els in order to understand the evaluation process. We find that centrality scores such as in-degree and authority impact positive received evaluations, whereas authority impacts positive given evaluation. We also show that betweenness centrality or hub scores have no impact. In the following section, our hypotheses are presented based on literature review. In section 3, we explain the data and methodology used in this study. Our results are presented in section 4, followed by the discussion. Section 6 presents our conclusions.

## 2. Theory and Hypotheses

Coopetition and Crowd innovation: Recent research on crowd innovation underlines the existence of three platform models afecting creative performance in co-creation: competition, cooperation and coopetition. It is shown that coopetition is beneficial for innovation [20]. Moreover, coopetitive climate outperforms creative performance in idea co-creation, and therefore competition and cooperation should not be understood as two conflicting concepts, but as orthogonal constructs that can co-exist simultaneously through coopetition to produce more creative ideas [17]. Coopetitive crowd innovation platforms difer from pure competitive or purer cooperative ones by mixing both cooperative functionalities (evaluation by the community, vision of other members’ ideas, comment on other members’ ideas) and competitive ones (rewards for the winners, visible ranking of the participants) [21]. Most of the previous literature on coopetition in crowd innovation contests focuses on ideas generation but not on ideas evaluation. In this research, we aim at filling this gap.

Ideas evaluation: The increase in the number of participants in on-line innovation contest platforms brings the problem of identifying among all the provided ideas the most creative ones. This task is in general solved by innovation contest participants for three reasons: first, it is less expensive and more rapid [18]; second, it creates a user community which will help the new product adoption and third, similarities exist on rankings between consumers and juries’ votes[22]. The ideas evaluation process is a significant research topic which is treated, among others, within various fields such as open innovation [23], creativity [24] and collective intelligence [25]. Various idea selection procedures have been developed but two main diferent approaches of evaluating participants’ ideas exist. The first one is the open evaluation process, the second is the prediction market. Open evaluation is the integration of external stakeholders in the evaluation of submitted ideas [26, 27, 28]. This procedure allows all participants to rate the submitted ideas, with the key advantage to be simple to implement. Another approach to select the best ideas is called “bag of lemons” which has been developed to filter out bad ideas accurately and fast [29]. This method is based on the fact that crowds are much better at eliminating bad ideas than at identifying good ones. The same authors developed another method to filter good ideas which they named “bag of stars”[30]. A second evaluation method is the prediction market which is used as a tool to rank submitted ideas.

Prediction markets are exchange-traded markets which trades the outcome of a future event. They are used as a forecasting tool, opinion aggregators, or as a preference indicator. The theoretical foundation of prediction markets is the hypothesis of the eficient market in which market prices reflect the sum of asymmetrically dispersed information. In prediction markets, participants buying a contract receive a payof if a future event occurs. In case that the event does not occur the participant loses his/her money. In innovation contest platforms, users bet on specific ideas and the competitive market decides which idea is better compared to others and the best is chosen. According to several experiments, idea evaluation carried out through prediction market system is found to be a useful tool [31, 32, 33, 34]. Its use results with an increase in the number of generated ideas and the number of participants as well [31], with speed in evaluation of the best ideas, scalability in the number of questions, and flexibility in the evaluation of various features and concepts to be analyzed simultaneously [32]. However, the advantages of prediction markets with respect to other methods which ranks ideas are not found. A comparison made on prediction markets and rating scale with diferent configurations conclude that a multi-criteria scale is superior to the prediction market-based evaluation process [33], because prediction markets are used by few people and include diferent information to be evaluated. Moreover, rating scales, which are easy to implement, are used in various web sites and are well-known tools which induce low cognitive load [35]. A survey made on users’ satisfaction of idea rating mechanisms shows that thumbs up/down or 5-star ratings are not good enough compared to multi-attribute scale [36].

Social influence and voting bias: As mentioned above, open innovation evaluation by participants present advantages such as costs and time reduc tion, simplicity, similarity with experts’ evaluation, but they may also be biased. First, consumers have dificulties in coming up with creative ideas, i.e. ideas that are feasible, original, and that provides customer benefits [24]. Second, creative idea selection is closely related to specific selection criteria such as originality, feasibility and possible efectiveness [37]. Moreover, positive feedback received by a given user-generated design and its perceived commercial success has an inverted U-shaped relationship [38]. Third, open evaluation process is prone to misevaluation. In competitive environments, participants use manipulation techniques, such as voting for their own ideas or against their competitors’ ideas. This fraud is a major concern of most innovation contest organizers [39]. It has been shown that positive social influence increases the likelihood of positive ratings [40]. Moreover, social influence can undermine the wisdom of crowds by decreasing the diversity of the crowd, by pushing the best answer to the peripheral of the crowd and by boosting the confidence of the crowd while it is also converging to less re liable solutions [41]. It is also argued that on-line ratings are systematically biased and manipulated due to the human herd instinct [42], or present dynamics change [43]. Using theories related to cooperation, it has been shown that direct reciprocity in crowd voting introduces bias in open innovation evaluation and potential negative implications for firms [19]. Coopetitive crowd innovation platforms are particularly interesting to study in terms of ideas evaluation because they gather evaluation biases coming from both competitive and cooperative environments. However, to our knowledge, few research exists on ideas evaluation in coopetitive crowd innovation. Table 1 presents a synthesis of the recent publications on crowd innovation platforms and our research positioning. We see that we contribute to the existing literature first by better understanding ideas evaluation by participants in coopetitive crowd innovation platforms, second by using network analysis in these contexts, and third by proposing a method to reduce existing ideas evaluation bias in order to help companies to better select ideas from crowd innovation.

## 2.1. Hypotheses

Previous literature on innovation contests shows that participants’ behavior depends on social efects. Feedback systems in the context of idea generation have significant influences on the participant contribution level [5]. More recently, it is shown by an empirical evidence that reciprocity and social influence impact positive votes in innovation contest [19]. The identification of social influencers using network analysis has been the object of numerous studies in diferent domains. Using centrality metrics, it has been identified how well diferent customers can serve as influencers in their social network [44]. In marketing, the peer influence in social networks on individual-level site usage is also studied [45]. An innovation contest can be represented as a social network with nodes (participants generating ideas) and links (comments and likes on the ideas). Considering this above previous literature, we suppose that social influencers in innovation contest, identified by network theory metrics, by providing numerous comments and likes on other participants’ ideas, influence reciprocity behaviors. Hence this leads us to the following hypothesis:

<table><tr><td></td><td>Ideas generation by participants</td><td>Ideas evaluation by participants</td><td>Ideas evaluation bias</td><td>Algorithms to improve participants&#x27; evaluation of ideas</td><td>Network Analysis</td><td>Coopetition</td></tr><tr><td>[12]</td><td>✓</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[5, 13]</td><td>✓</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[17]</td><td>✓</td><td></td><td></td><td></td><td></td><td>✓</td></tr><tr><td>[19]</td><td></td><td>✓</td><td>✓</td><td></td><td></td><td></td></tr><tr><td>[39]</td><td>✓</td><td></td><td></td><td></td><td>✓</td><td></td></tr><tr><td>[18, 31, 32, 33, 34, 29]</td><td></td><td>✓</td><td></td><td>✓</td><td></td><td></td></tr><tr><td>This study</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr></table>

H1: The higher is innovation contest participants’ a) centrality degree b) betweenness centrality c) hub and d) authority scores, the higher he/she receives positive evaluation on his/her ideas.

Previous literature using real life experiments shows that through social network analysis it is possible to find out key players in the information flow [46, 47]. In these studies, it is shown that the community is able to distinguish key players in their community [46] and lead users are occupying a distinct position within their social networks [47]. In relation to the cocreation literature, individuals with high level of social network connection should be more inclined to contribute [5] because the feeling of belonging to a community motivates people’s participation to it [48]. The literature on social roles using systemic approach, considering both the members position and interactions with other members, confirms the link between high members’ contribution and their central position in the community. It is shown that centrality and authority characterizes the most important contributors, as well as the influence of the community core on peripheral members [49]. Therefore, we propose the following hypothesis:

H2: The higher is innovation contest participants’ a) centrality degree b) betweenness centrality c) hub and d) authority scores, the higher he/she makes positive evaluation on other participants’ ideas.

The open evaluation system is designed to overcome the misevaluation of few experts who can have divergent points of view to evaluate ideas proposed by consumers [50]. In addition to some biases occurring in open evaluation systems as given above, reciprocity often explains individuals’ behaviors on social media according to the social exchange theory. This theory explains that social behaviors aim to increase the benefits and reduce the costs of the exchange process [51]. Reciprocity is important in social exchanges because interaction is based on its balance [52]. A strong empirical evidence shows that Facebook users interact according to the social exchange theory, maximizing the strength of their relationship and minimizing the cost by “liking” [53]. Moreover, users tend to increase their broadcast as they receive some reactions, which are likes received and comments received, by their audience. Another study on Facebook shows that perceived trust, community identification has important efect on the users’ continuity to use the site [54]. Based on this literature, we propose the following hypothesis on evaluations in innovation contest platforms:

H3: The higher is innovation contest participants’ number of activities (ideation and commenting) on the platform, the higher is the number of received positive evaluations by the other participants.

Using clustering and network analysis, a study on user roles and consociated with diferent behaviors in terms of contributions: socializer, idea generator, master, eficient contributor, passive idea generator, passive commentator. These six types difer not only in terms of activities but also in terms of evaluation. According to the authors, the eficient contributor, master and idea generator make more community evaluation than the other types of users. Similarly, we therefore suggest the following hypothesis:

H4: The higher is innovation contest participants’ number of activities (ideation and commenting) on the platform, the higher is the number of given positive evaluations to other participants’ ideas.

## 3. Data

Data used in this study is obtained from a crowd innovation platform for a worldwide leader in small household appliances. The contest took place from April to September 2015. On this platform, participants cannot follow each other but they can give respectively positive evaluation by clicking on a ”+1” button to submitted ideas and comments on the platform. Data collected on the innovation contest platform consist of participants’ user name, ideas, and comments, as well as given and received “+1”. Using this data, we first describe participants’ activities, then we map the network of interactions between the participants who have provided at least one idea or one comment, or those who have made an evaluation.

## 3.1. Innovation contest participants’ activities

There are three basic activities that a participant can conduct on the innovation contest platform: providing ideas, commenting on ideas, and evaluating ideas and comments by clicking on the functionality “+1”. In the crowd innovation contest studied in our research, there are 1881 subscribed participants. Among these, 498 participants submitted at least one idea or comment, or evaluated an idea or a comment.

In crowd innovation contests, some ideas are commented while others are not. If an idea is commented, the owner of the idea may answer the comment, creating therefore a dialogue. In our analysis, we are not taking into account these auto-comment loops, such as exchanges created by those thanking others for their comments or by someone starting the thread by submitting an idea, because it creates some bias in ideas’ evaluation. Users may also give a $^ { 6 6 } + 1 ^ { 9 9 }$ to any idea or comment they like. Table 2 provides detailed participants’ activities for the innovation contest. There are two columns in this table, the first one represents activities counted for all participants, the are removed. These five are the outliers who have made many comments and idea generation.

Table 2: Basic activities counted for the innovation contest.

<table><tr><td></td><td>original</td><td>without top 5</td></tr><tr><td>number of ideas</td><td>2,098</td><td>1,609</td></tr><tr><td>number of comments</td><td>2,299</td><td>798</td></tr><tr><td>number of commented ideas</td><td>1,488</td><td>1142</td></tr><tr><td>people who submitted at least one idea</td><td>438</td><td>433</td></tr><tr><td>people who received at least one comment</td><td>352</td><td>347</td></tr><tr><td>number of likes</td><td>6,886</td><td>3,435</td></tr><tr><td>people who received like</td><td>438</td><td>404</td></tr><tr><td>people who gave like</td><td>244</td><td>212</td></tr><tr><td>active users</td><td>498</td><td>493</td></tr></table>

Table 4 shows that the distribution of given and received likes or the ‘+1‘ clicks by each person participating in the campaign, revealing that all data are very skewed with many participants who did not receive or given any +1 clicks. The design of the innovation contest platform is made in such a way that it is not possible for participants to know the source of the ratings given. This property of the platform aims to reduce reciprocal behavior. Moreover, participants cannot follow each other like in any other social media. This second design characteristic avoids any information bubble which diminishes the information flow. The purpose of these features is to minimize any voting bias which are inherent to social networks.

## 3.2. Network representation of the innovation contest

The social network theory explains the interactions of people or institutions through their links [55]. Centrality measures consist of widely accepted [56]. Various centrality measures depict diferent roles of nodes within the network. Degree centrality score of a node is obtained by counting a node’s number of ties with other nodes. Betweenness centrality shows which actors are in the communication path between other actors [57, 58]. A high betweenness score identifies the nodes passing information from one cluster of people to another. These participants are also known as brokers. The Kleinberg’s HITS algorithm, gathering “hubs” and “authorities”, has been developed to rank web pages [59]. This algorithm makes a distinction between nodes known as “hubs” and others described as “authority”. A hub has many links to other nodes, whereas a node with a high authority score is pointed to by many hubs. The spread of the on-line social networks helped this analysis method to gain an important traction [60].

In this article, the studied network is created through the comments given to the ideas posted on the innovation contest platform. In this network all nodes represent people contributing to the innovation contest. A person who makes at least one comment on an idea generates a link between him/her and the idea owner. A network graph generated from comments to ideas in the innovation contest is shown in Figure 1. This network representation gives us an idea about the relationship between participants but it is not suficient to allow a detailed analysis of contest participants. The ability to make comments on diferent ideas produced by the same person creates a weighted directed graph. In this case, the direction of all edges is from the person making a comment towards the person providing an idea. As the number of comments given by one person to another one can vary, we obtain a weighted network. All network analysis and graphs in this study were made with igraph [61] and pgml [62] on R statistical computing software [63].

![](/api/attachments/MGDRV3D4/fulltext/images/20e93d7e88773a05870bcee471d7cb14a9cb92ad321a40d08d8d336c97743d09.jpg)  
Figure 1: Network of participants based on ideas-comments. Nodes without any connections are participants who have at least given one $^ { 6 } + 1 ^ { 9 }$ or an uncommented idea and did not provide any comment.

## 4. Methodology and results

Our objective in this study is to understand the parameters influencing innovation contest platform participants’ evaluations and to identify their characteristics. In order to achieve this and to test our hypotheses, we conducted several nonlinear regressions using network positions and participants’ activities as independent variables and $^ { 6 6 } + 1 ^ { 9 9 }$ collected and given as dependent variables. We have used nonlinear models because our dependent variables are count data which are the number of given and received “+1”

[64].

## 4.1. Nonlinear regressions against participants evaluations

In this section, we show the result of various nonlinear regressions made against two types of evaluations: first participants’ received participants given “+1”. These regressions aim to identify which activity and network scores of a participant in the innovation contest have and im-

Table 3 provides definitions of the variables used in this research. The descriptive statistics of the data are shown in Table 4. The statistics related to participants’ activities on the innovation contest platforms and also the network scores of participants obtained from their interactions with each other through comments made on ideas. In the following section, a correlation matrix is given in Table 5 for each parameter used in our analysis.

Table 3: Variable definitions.

<table><tr><td>Variable</td><td>Definition</td></tr><tr><td colspan="2">Dependent variables</td></tr><tr><td>GIVEN.LIKE</td><td>Number of given “+1” by a participant</td></tr><tr><td>REC.LIKE</td><td>Number of received “+1” by a participant</td></tr><tr><td colspan="2">Independent variables</td></tr><tr><td>IDEA</td><td>Number of ideas given by an innovation contest participant</td></tr><tr><td>DEG.OUT</td><td>Number of comments given</td></tr><tr><td>DEG.IN</td><td>Number of comments received</td></tr><tr><td>BET</td><td>Betweenness centrality score</td></tr><tr><td>HUB</td><td>Kleinberg’s hub score</td></tr><tr><td>AUTH</td><td>Kleinberg’s authority score</td></tr></table>

## 4.2. Comparison of models

Our data set contains 493 participants who did not always provide and/or received an evaluation. In order to find the model with the best fit, we compare diferent nested models: Poisson, Zero Inflated Poisson and

Table 4: Descriptive statistics.

<table><tr><td></td><td>N</td><td>mean</td><td>sd</td><td>se</td><td>min</td><td>max</td></tr><tr><td colspan="7">activities on the platform</td></tr><tr><td>GIVEN.LIKE</td><td>493</td><td>10.21</td><td>44.53</td><td>2.01</td><td>0.00</td><td>493.00</td></tr><tr><td>REC.LIKE</td><td>493</td><td>10.26</td><td>16.57</td><td>0.75</td><td>0.00</td><td>104.00</td></tr><tr><td>IDEA</td><td>493</td><td>3.26</td><td>5.44</td><td>0.24</td><td>0.00</td><td>49.00</td></tr><tr><td colspan="7">network scores</td></tr><tr><td>DEG.IN</td><td>493</td><td>1.67</td><td>1.96</td><td>0.09</td><td>0.00</td><td>13.00</td></tr><tr><td>DEG.OUT</td><td>493</td><td>0.89</td><td>3.25</td><td>0.15</td><td>0.00</td><td>25.00</td></tr><tr><td>BET</td><td>493</td><td>0.00</td><td>0.02</td><td>0.00</td><td>0.00</td><td>0.24</td></tr><tr><td>HUB</td><td>493</td><td>0.00</td><td>0.01</td><td>0.00</td><td>0.00</td><td>0.07</td></tr><tr><td>AUTH</td><td>493</td><td>0.02</td><td>0.03</td><td>0.00</td><td>0.00</td><td>0.32</td></tr></table>

Table 5: Pearson correlation matrix.

<table><tr><td></td><td>V1</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>IDEA</td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>DEG.IN</td><td>2</td><td>0.697</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>DEG.OUT</td><td>3</td><td>0.572</td><td>0.457</td><td>1</td><td></td><td></td><td></td></tr><tr><td>BET</td><td>4</td><td>0.401</td><td>0.485</td><td>0.701</td><td>1</td><td></td><td></td></tr><tr><td>HUB</td><td>5</td><td>0.419</td><td>0.416</td><td>0.795</td><td>0.624</td><td>1</td><td></td></tr><tr><td>AUTH</td><td>6</td><td>0.822</td><td>0.599</td><td>0.468</td><td>0.319</td><td>0.365</td><td>1</td></tr></table>

Zero Inflated Negative Binomial. We started to use Poisson model as we are dealing with count data model but also to compare with zero-inflated models. We have considered zero-inflated models because the dependent variables; given and received “+1” contain high number of zeros [64].

There are various fit tests such as boundary likelihood, Vuong and AIC/BIC tests to choose the best fitted model between Poisson, negative binomial and zero-inflated models [64]. In this study, we have used log likelihood and AIC; our corresponding regression results are shown on Tables 6 and 7.

The boundary likelihood test is used to determine between the zeroinflated Poisson (ZIP) and zero-inflated negative binomial (ZINB). The pvalues of the boundary likelihood model is less than 0.05 thus ZINB is the preferable model over ZIP for the received and given $^ { 6 6 } + 1 ^ { 9 9 } .$ . Moreover, the result of the AIC test for the ZINB, ZIP and Poisson models for the regressions made against the received “+1” are shown in Table 6, and for the given “+1” are in Table 7 respectively. The AIC test favors the use of the ZINB model for both cases. The log likelihood results for the ZINB, ZIP and Poisson models also favors the use of zero-inflated negative binomial in both cases.

Table 6: Zero-inflated negative binomial (ZINB), zero-inflited Poisson (ZIP) and poisson models, the dependent variable is the received ”+1” by users.

<table><tr><td></td><td>ZINB</td><td>ZIP</td><td>Poisson</td></tr><tr><td>(Intercept)</td><td>1.00***(0.05)</td><td>1.57***(0.02)</td><td>1.44***(0.02)</td></tr><tr><td>IDEA</td><td>0.06***(0.01)</td><td>0.03***(0.00)</td><td>0.03***(0.00)</td></tr><tr><td>GIVEN.LIKE</td><td>0.00(0.00)</td><td>0.00***(0.00)</td><td>0.00***(0.00)</td></tr><tr><td>DEG.IN</td><td>0.29***(0.03)</td><td>0.19***(0.01)</td><td>0.21***(0.01)</td></tr><tr><td>DEG.OUT</td><td>0.04*(0.02)</td><td>0.03***(0.00)</td><td>0.04***(0.00)</td></tr><tr><td>BET</td><td>-0.00(0.00)</td><td>-0.00(0.00)</td><td>-0.00(0.00)</td></tr><tr><td>HUB</td><td>-0.01(0.01)</td><td>-0.01***(0.00)</td><td>-0.01***(0.00)</td></tr><tr><td>AUTH</td><td>0.01***(0.00)</td><td>0.00***(0.00)</td><td>0.00***(0.00)</td></tr><tr><td>AIC</td><td>2756.22</td><td>3810.58</td><td>4004.05</td></tr><tr><td>Log Likelihood</td><td>-1368.11</td><td>-1896.29</td><td>-1994.02</td></tr><tr><td>Num. obs.</td><td>493</td><td>493</td><td>493</td></tr><tr><td>BIC</td><td></td><td></td><td>4037.65</td></tr><tr><td>Deviance</td><td></td><td></td><td>2402.28</td></tr></table>

<sup>∗∗∗</sup>p < 0.001, <sup>∗∗</sup>p < 0.01, <sup>∗</sup>p < 0.05

## 4.3. Model interpretation

Comparing the various models, we found out that the zero-inflated negative binomial models are best suited for the received and also for the given $^ { 6 6 } + 1 ^ { 9 9 }$ . In this section, we interpret the ZINB models based on coeficient values. To interpret ZINB model, the coeficient values have to be exponentiated giving the incidence rate ratios [64]. The zero-inflated negative binomial model made against the received “+1”, given in Table 6, shows that the number of ideas provided by a participant (IDEA), the number of comments that a participant receives (DEG.IN), the number of comments given by the participant (DEG.OUT), and the authority score (AUTH) are significant. To obtain the incidence rates we take the exponential of the parameters obtained in the ZINB model. This gives us an incidence rate of 5.8% for the IDEA, 33.6% for comments received (DEG.IN), 4.3% for the comment given (DEG.OUT) and 0.6% for the AUTH value respectively.

Table 7: Zero-inflated negative binomial (ZINB), zero-inflited Poisson (ZIP) and poisson models, the dependent variable is the given ”+1” by users.

<table><tr><td></td><td>ZINB</td><td>ZIP</td><td>Poisson</td></tr><tr><td>(Intercept)</td><td>1.29***(0.14)</td><td>2.53***(0.02)</td><td>1.69***(0.02)</td></tr><tr><td>IDEA</td><td>0.09(0.08)</td><td>0.03***(0.00)</td><td>0.04***(0.00)</td></tr><tr><td>REC.LIKE</td><td>0.06**(0.02)</td><td>-0.00*(0.00)</td><td>0.00(0.00)</td></tr><tr><td>DEG.IN</td><td>-0.17(0.10)</td><td>0.11***(0.01)</td><td>0.14***(0.01)</td></tr><tr><td>DEG.OUT</td><td>0.11(0.07)</td><td>0.07***(0.00)</td><td>0.09***(0.00)</td></tr><tr><td>BET</td><td>0.01(0.01)</td><td>0.00(0.00)</td><td>0.00(0.00)</td></tr><tr><td>HUB</td><td>0.02(0.04)</td><td>0.01***(0.00)</td><td>0.00(0.00)</td></tr><tr><td>AUTH</td><td>-0.02**(0.01)</td><td>-0.01***(0.00)</td><td>-0.01***(0.00)</td></tr><tr><td>AIC</td><td>2247.58</td><td>13131.73</td><td>17245.65</td></tr><tr><td>Log Likelihood</td><td>-1113.79</td><td>-6556.87</td><td>-8614.83</td></tr><tr><td>Num. obs.</td><td>493</td><td>493</td><td>493</td></tr><tr><td>BIC</td><td></td><td></td><td>17279.26</td></tr><tr><td>Deviance</td><td></td><td></td><td>16386.62</td></tr></table>

<sup>∗∗∗</sup>p < 0.001, <sup>∗∗</sup>p < 0.01, <sup>∗</sup>p < 0.05

We also run several regressions with the given “+1” as dependent variable as shown in Table 7. A zero-inflated negative binomial regression shows that the significant parameters are the “+1” obtained (REC.LIKE) and authority (AUTH) score. These results show that people receiving a “+1” are 6.5 % more likely to give a “+1” and the authority score decreases by 2.2 % the incidence rate of giving a “+1”. These results show that active participants in giving likes are also active in evaluating other ideas through a “+1” given. On the other hand, the authority (AUTH) score which is significant shows that the incidence rate is negatively correlated with the given “+1”. This means that authorities in this network are reluctant to evaluate others.

These results show that the first hypothesis (the higher is innovation contest participants’ a) centrality degree b) betweenness centrality c) hub and d) authority score, the higher he/she obtains positive evaluation), and the third hypothesis (the higher is innovation contest participants’ activities (ideation and commenting) on the platform, the higher is the number of the received positive evaluations to the participants) are partially validated.

## 4.4. Methodology to reduce social voting bias

Our previous analyses show that more crowd innovation platform members have high level of centrality of degree or authority, more they give or receive likes on ideas. These results reveal voting bias linked to social influence. They also mean for managers in innovation that selecting ideas receiving the most important number of likes is not a good solution because the evaluations contain bias. In order to overcome this problem and to help managers to select the most promising ideas, we propose the following method in order to reduce voting bias coming from both competitive and cooperative environments and to reveal more unbiased scores for ideas evaluation.

## 4.4.1. First step: Design of the innovation contest to reduce ideas evaluation bias coming from competitive environment

As mentioned above, competitive environments generate evaluation manipulation techniques such as voting positively for its own ideas and voting negatively for its competitors’ ideas. To reduce these two biases, crowd innovation platforms need to present two characteristics. First, it must not be possible for participants to know the source (member) of the ratings given. Second, participants must not follow each other like in any other social media. This was implemented in the platform we used in this research.

## 4.4.2. Second step: to remove autocomments and autolikes

As we previously reported, autocomments and autolikes are manipulation techniques in competitive environments of crowd innovation platforms. They may introduce bias in ideas evaluation by artificial inflation of positive ideas evaluation from participants making autocomments or autolikes. Consequently, we suggest to remove autocomments and autolikes from the ideas comments and likes database extracted from the platform.

## 4.4.3. Third step: network analysis to identify social influencers

Once the database is ”cleaned”, and following our analysis, we propose to run a network analysis providing the following criteria on each participant in the crowd innovation platform of the network: degree in and authority. Therefore, we can identify the most important nodes in terms of social influence (highest level of degree in or authority).

## 4.4.4. Fourth step: algorithm to reduce bias

In order to reduce bias coming from cooperative environments, and therefore linked to social influencers in the network, we suggest afecting a weight of 0.5 instead of 1 to any like coming from or going to a member identified in the third step as a social influencer, in order to reduce reciprocity efect and to give more unbiased ratings.

## 5. Discussion

Crowd innovation is an emergent practice in the digital age aiming at crowd sourcing to customers ideas generation and evaluation. The main benefit is the production of a big number of ideas in a short time. In this study, we make six contributions to the previous literature on innovation contests. First, we focus on the evaluation challenge of these ideas in crowd innovation platforms, whereas previous research focused on participant activities [13, 5]. Second, our research takes into account the interactions between participants of a co-creation site within a social network perspective and uses several centrality scores to characterize users who have diferent roles in the flow of information. Except in [12] in order to classify participants’ roles, network theory and centrality measures have not been used in modeling factors impacting crowd innovation participants’ behavior, more specifically evaluation. Third, our research focuses on coopetitive crowd innovation platforms, extending therefore the emerging papers of coopetition in crowd innovation [65]. We present the first study on participants’ ideas evaluation behavior in coopetitive platforms, which are particularly interesting by gathering voting bias coming from both competition and cooperation environments. Our fourth contribution concerns the findings improving a better understanding of evaluation processes in crowd innovation, which has not been done in previous literature. We show that number of provided ideas, degree-in, degree-out and authority is positively correlated with the number of positive evaluations received. We also find that the authority score impacts negatively the number of evaluation contributions, revealing that authorities are reluctant to evaluate others. Therefore, they must be considered principally as ideas providers but not as evaluators. Moreover, contrary to previous literature on lead users, asserting their role of linking diferent social groups by their high score of betweenness centrality [47], we show in this research that betweenness centrality score in crowd innovation platforms has significantly no efect on the number of received or given eval uations. The fifth contribution is that we reveal voting bias linked to social influence by characterizing ideas evaluation contributors by their network positions. We therefore extend the recent literature on voting bias in innovation contests [19] by measuring network centrality and social influence scores and by showing their efects on evaluation. Moreover, whereas [19] focus on biases in cooperation environments, we extend the identification of biases in coopetition climates. Therefore, we study biases coming from both competitive and cooperative climates. Our sixth contribution is to propose a methodology in order to reduce the voting biases in coopetitive crowd innovation and to help managers of innovation better selecting the promising ideas provided in a crowd innovation platform.

This research provides diferent managerial outcomes. The first one concerns crowd innovation platform managers who aim at increasing the performance of their platforms. By using network analysis, they can characterize structurally central members and influencers’ participants in ideas evaluation process. We suggest that crowd innovation platform managers follow network centrality scores in their business intelligence and analytics systems.The second recommendation targets managers in innovation. Our research provides a methodology aiming at selecting the good ideas from the crowd by reducing existing social voting biases coming from both competition and cooperation in the platform. This will change the widespread usage of open innovation by companies which often select the ideas receiving the most important number of positive evaluations without making further analysis.

Even though the network approach is a valuable tool to understand the participants’ evaluation in innovation contests and to reduce voting bias to select the most promising ideas, additional research on other innovation contests data is needed to increase the external validity of our results. Our users choose to evaluate (or not) ideas i.e. extrinsic or/and intrinsic motivations or idea content. Some theoretical background on good evaluation profile should also be interesting to consider in order to identify who should be the best profile of participants for ideas evaluation in crowd innovation platforms. Complementary studies on diferent crowd innovation contests should fine tune the reducing voting bias algorithm. Finally, future research on the impact of human-machine interactions, ergonomy, and functionalities of crowd innovation contests on the evaluation network of participants would provide additional insights.

## 6. Conclusion

In this study, we analyzed a crowd innovation contest launched by the major brand of small household appliances. We first ran a network analysis based on participants’ ideas and comments and found that activities such as submitting ideas, commenting on ideas, and various network centrality degrees impact on the positive evaluation received or given by participants. These results show that participants’ network position criteria are key indicators to analyze ideas evaluation process on current crowd innovation contests, that network analysis provides criteria to develop a methodology to reduce voting bias in coopetitive environments.This study presents several managerial recommendations while opening future potential research

## Acknowledgment

This research received financial support from PIA (Programme Investissement d’Avenir) of the French government for the Innovagora Project.

## References

[1] A. C. Bullinger, A.-K. Neyer, M. Rass, and K. M. Moeslein, “Community-based innovation contests: Where competition meets cooperation,” Creativity and Innovation Management, vol. 19, no. 3, pp. 290–303, 2010.

[2] S. Adamczyk, A. C. Bullinger, and K. M. M¨oslein, “Innovation Contests: A Review, Classification and Outlook,” Creativity and Innovation Management, vol. 21, no. 4, pp. 335–360, 2012. 00119.

[3] J. Morgan and R. Wang, “Tournaments for Ideas,” California Management Review, vol. 52, no. 2, pp. 1–35, 2010.

[4] F. T. Piller and D. Walcher, “Toolkits for idea competitions: A novel method to integrate users in new product development,” R&D Management, vol. 36, pp. 307–318, June 2006.

[5] L. Chen, J. R. Marsden, and Z. Zhang, “Theory and Analysis of Company-Sponsored Value Co-Creation,” Journal of Management Information Systems, vol. 29, pp. 141–172, Oct. 2012.

[6] S. Nørskov, Y. M. Antorini, and M. B. Jensen, “Innovaitve Brand Community Members and Their Willingness to Share Ideas with Companies,” International Journal of Innovation Management, vol. 20, p. 1650046, Aug. 2016.

[7] M. Dodgson, D. M. Gann, and A. Salter, “The role of technology in the shift towards open innovation: The case of Procter & Gamble,” R&D Management, vol. 36, pp. 333–346, June 2006.

[8] E. Enkel, O. Gassmann, and H. W. Chesbrough, “Open R&D and open innovation: Exploring the phenomenon,” R&D Management, vol. 39, pp. 311–316, Sept. 2009. 01155.

[9] K. J. Boudreau, K. R. Lakhani, and M. Menietti, “Performance Responses to Competition across Skill-levels in Rank Order Tournaments: Field Evidence and Implications for Tournament Design.,” Rand Journal of Economics, vol. 47, no. 1, pp. 140–165, 2013.

[10] L. Muhdi and R. Boutellier, “Motivational Factors Afecting Partici pation and Contribution of Members in Two Diferent Swiss Innovation Communities,” International Journal of Innovation Management, vol. 15, no. 03, pp. 543–562, 2011.

[11] K. Frey, C. L¨uthje, and S. Haag, “Whom should firms attract to open innovation platforms? The role of knowledge diversity and motivation,” Long Range Planning, vol. 44, no. 5-6, pp. 397–420, 2011.

[12] J. F¨uller, K. Hutter, J. Hautz, and K. Matzler, “User Roles and Contributions in Innovation-Contest Communities,” Journal of Management Information Systems, vol. 31, no. 1, pp. 273–308, 2014.

[13] K. Hutter, J. F¨uller, J. Hautz, V. Bilgram, and K. Matzler, “Machiavellianism or Morality: Which Behavior Pays Of In Online Innovation Contests?,” Journal of Management Information Systems, vol. 32, no. 3, pp. 197–228, 2015.

[14] G. Juell-Skielse, A. Hjalmarsson, E. Juell-Skielse, P. Johannesson, and D. Rudmark, “Contests as innovation intermediaries in open data markets,” Information Polity, vol. 19, no. 3-4, pp. 247–262, 2014.

[15] A. Armisen and A. Majchrzak, “Tapping the innovative business poten-399, 2015. 00000.

[16] J. Bockstedt, C. Druehl, and A. Mishra, “Problem-solving efort and success in innovation contests: The role of national wealth and na-

tional culture,” Journal of Operations Management, vol. 36, pp. 187– 200, 2015.

[17] Z. Zhao, D. Renard, M. Elmoukhlisse, and C. Balagu´e, “What affects creative performance in idea co-creation: Competitive, cooperative or coopetitive climate?,” International Journal of Innovation Management, vol. 20, no. 04, p. 1640002, 2016. 00000.

[18] O. Toubia and L. Flor\`es, “Adaptive idea screening using consumers,” Marketing Science, vol. 26, no. 3, pp. 342–360, 2007.

[19] R. Hofstetter, S. Aryobsei, and A. Herrmann, “Should you really produce what consumers like online? empirical evidence for reciprocal votagement, vol. 35, no. 2, pp. 209–229, 2018.

[20] M. Bengtsson and S. Kock, “Coopetition: Quo vadis? past accomplishments and future challenges,” Industrial marketing management, vol. 43, no. 2, pp. 180–188, 2014.

[21] M. Elmoukhliss, D. Renard, Z. Zhao, and C. Balagu´e, “De la comp´etition \`a la coop´etition,” Revue fran¸caise de gestion, no. 6, pp. 11– 24, 2017.

[22] P. R. Magnusson, E. W¨astlund, and J. Netz, “Exploring users’ appropriateness as a proxy for experts when screening new product/service ideas,” Journal of Product Innovation Management, vol. 33, no. 1, pp. 4–18, 2016.

[23] H. W. Chesbrough, Open Innovation: The New Imperative for Creating And Profiting from Technology. Harvard Business School Press, 2003.

[24] T. Amabile, Creativity in Context. Westview press, 1996. 08554.

[25] A. W. Woolley, C. F. Chabris, A. Pentland, N. Hashmi, and T. W. Malone, “Evidence for a Collective Intelligence Factor in the Performance of Human Groups,” Science, vol. 330, pp. 686–688, 2010. 00840.

[26] J. Haller, V. Velamuri, D. Schneckenberg, and K. M. Moeslein, “Exploring the Design Elements of Open Evaluation,” Journal of Strategy and Management, pp. 1–43, 2016.

[27] J. West and M. Bogers, “Profiting from external innovation: A review of research on open innovation,” 2011.

[28] M. Elmquist, T. Fredberg, and S. Ollila, “Exploring the field of open innovation,” European Journal of Innovation Management, vol. 12, no. 3, pp. 326–345, 2009.

[29] M. Klein and A. C. B. Garcia, “High-Speed Idea Filtering With the Bag of Lemons,” Decision Support Systems, vol. 78, pp. 39–50, 2015.

[30] M. Klein, A. N. A. Cristina, and B. Garcia, “The Bag of Stars : Highpp. 1–14, 2012.

[31] C. A. LaComb, J. A. Barnett, and Q. Pan, “The imagination market,” Information Systems Frontiers, vol. 9, pp. 245–256, July 2007. 00084.

[32] E. Dahan, A. Soukhoroukova, and M. Spann, “New Product Development 2.0: Preference Markets-How Scalable Securities Markets Identify Winning Product Concepts and Attributes,” Journal of Product Inno-

[33] I. Blohm, C. Riedl, J. M. Leimeister, and H. Krcmar, “Idea Evaluation Mechanisms for Collective Intelligence in Open Innovation Communities: Do Traders Outperform Raters?,” in ICIS 2011 Proceedings, vol. 4, pp. 1–24, 2011.

[34] A. Soukhoroukova, M. Spann, and B. Skiera, “Sourcing, Filtering, and Evaluating New Product Ideas: An Empirical Exploration of the Performance of Idea Markets,” Journal of Product Innovation Management, vol. 29, pp. 100–112, Jan. 2012. 00113.

[35] J. J. Van Merri¨enboer, P. A. Kirschner, and L. Kester, “Taking the load of a learner’s mind: Instructional design for complex learning,” Educational psychologist, vol. 38, no. 1, pp. 5–13, 2003.

[36] C. Riedl, I. Blohm, J. M. Leimeister, and H. Krcmar, “Rating Scales for Collective Intelligence in Innovation Communities: Why Quick and Easy Decision Making Does Not Get it Right,” in Thirty First International Conference on Information Systems, pp. 98–104, 2010.

[37] E. F. Rietzschel, B. a Nijstad, and W. Stroebe, “The selection of creative ideas after individual idea generation: Choosing between creativity and impact.,” British journal of psychology, vol. 101, pp. 47–68, 2010.

## ACCEPTED MANUSCRIPT

[38] M. B. Jensen, C. Hienerth, and C. Lettl, “Forecasting the Commercial Attractiveness of User-Generated Designs Using Online Data: An Empirical Study within the LEGO User Community,” Journal of Product Innovation Management, vol. 31, pp. 75–93, Dec. 2014. 00010.

[39] V. K. Velamuri, D. Schneckenberg, J. B. Haller, and K. M. Moeslein, “Open evaluation of new product concepts at the front end of innovation: objectives and contingency factors,” R&d Management, vol. 47, no. 4, pp. 501–521, 2017.

[40] L. Muchnik, S. Aral, and S. J. Taylor, “Social influence bias: A randomized experiment,” Science, vol. 341, no. 6146, pp. 647–51, 2013. 00304.

[41] J. Lorenz, H. Rauhut, F. Schweitzer, and D. Helbing, “How social influence can undermine the wisdom of crowd efect,” Proceedings of the National Academy of Sciences, vol. 108, no. 22, pp. 9020–9025, 2011.

[42] S. Aral, “The Problem With Online Ratings,” MIT Sloan Management Review, Winter, vol. 55, no. 2, pp. 47–52, 2014. 00000.

[43] P. B. Goes, M. Lin, and C.-m. Au Yeung, “popularity efect in usergenerated content: Evidence from online product reviews,” Information

[44] C. Kiss and M. Bichler, “Identification of influencersmeasuring influence in customer networks,” Decision Support Systems, vol. 46, no. 1, pp. 233–253, 2008.

[45] M. Trusov, A. V. Bodapati, and R. E. Bucklin, “Determining influential users in internet social networks,” Journal of Marketing Research, vol. 47, no. 4, pp. 643–658, 2010.

[46] A. Banerjee, A. G. Chandrasekhar, E. Duflo, and M. O. Jackson, “Gossip: Identifying Central Individuals in a Social Network,” arXiv:1406.2293 [physics], Oct. 2016. 00000.

[47] J. Kratzer, C. Lettl, N. Franke, and P. A. Gloor, “The Social Network Position of Lead Users,” Journal of Product Innovation Management,

[48] W.-S. Yoo, K.-S. Suh, and M.-B. Lee, “Exploring the Factors Enhancing Member Participation in Virtual Communities,” Journal of Global Information Management, vol. 10, pp. 55–71, July 2002.

[49] L. Benamar, C. Balagu´e, and M. Ghassany, “The identification and influence of social roles in a social media product community,” Journal of Computer-Mediated Communication, vol. 22, no. 6, pp. 337–362, 2017.

[50] M. K. Poetz and M. Schreier, “The Value of Crowdsourcing: Can Users Really Compete with Professionals in Generating New Product Ideas?,” Journal of Product Innovation Management, vol. 29, no. 2, pp. 245–256, 2012.

[51] R. Cropanzano and M. S. Mitchell, “Social exchange theory: An interdisciplinary review,” Journal of management, vol. 31, no. 6, pp. 874– 900, 2005. 03466.

[52] M. G¨obel, R. Vogel, and C. Weber, “Management Research on Reciprocity: A Review of the Literature,” Business Research, vol. 6, pp. 34– 53, May 2013. 00020.

[53] J. Surma, “Social exchange in online social networks. The reciprocity phenomenon on Facebook,” Computer Communications, vol. 73, Part B, pp. 342–346, Jan. 2016. 00004.

[54] R. Chen, S. K. Sharma, and H. Raghav Rao, “Members’ site use continuance on Facebook: Examining the role of relational capital,” Decision Support Systems, vol. 90, pp. 86–98, Oct. 2016. 00001.

[55] M. O. Jackson, Social and Economic Networks. Princeton University Press, 2010. 00000.

[56] F. Bloch, M. O. Jackson, and P. Tebaldi, “Centrality Measures in Networks,” arXiv:1608.05845 [physics], Aug. 2016. 00004.

[57] U. Brandes, “A faster algorithm for betweenness centrality,” Journal of mathematical sociology, vol. 25, no. 2, pp. 163–177, 2001.

[58] L. C. Freeman, “Centrality in social networks conceptual clarification,” Social networks, vol. 1, no. 3, pp. 215–239, 1978.

[59] J. M. Kleinberg, “Authoritative Sources in a Hyperlinked Environment,” Journal of the ACM, vol. 46, no. May 1997, pp. 668–677, 1999.

[60] A. Guille, H. Hacid, C. Favre, and D. A. Zighed, “Information difusion in online social networks: A survey,” ACM SIGMOD Record, vol. 42, no. 2, pp. 17–28, 2013. 00260.

[61] G. Csardi and T. Nepusz, “The igraph software package for complex network research,” InterJournal Complex Systems, vol. 1695, no. 5, pp. 1–9, 2006.

[62] Y. Croissant, Pglm: Panel Generalized Linear Model. 2013. 00005 R package version 0.1-2.

[63] R Core Team, R: A Language and Environment for Statistical Computing. Vienna, Austria: R Foundation for Statistical Computing, 2015.

[64] J. M. Hilbe, Modeling Count Data. Cambridge University Press, 2014.

[65] Z. Zhao, D. Renard, M. Elmoukhliss, and C. Balague, “What afects creative performance in idea co-creation: competitive, cooperative or coopetitive climate?,” in The role of creativity in the management of innovation: state of the art and future research outlook, pp. 123–148, World Scientific, 2017.

# ACCEPTED MANUSCRIPT

## Altay Özaygen

Completed his PhD at Institut-Mines Télécom, Télécom École de Management. Altay worked as a postdoctoral researcher at Institut-Mines Télécom, Télécom École de Management, Smart Object and Social Networks Chair. He works since August 2017 as a postdoctoral researcher at Université Paris-Sud. His research interests are intellectual property rights, open innovation, patent analysis and software industry. Before his PhD, Altay worked as a programmer and Unix and Linux system administrator for nearly 10 years.

## Christine Balagué

Christine Balagué is Professor at Institut Mines Telecom-TEM, member of LITEM (Laboratory of Innovation Technology Economy and Management). She is holder of the research chair on Social Networks and IoT. She was Vice-President of National Digital Council ( http://www.cnnumerique.fr/en/) in France between 2013 and 2016. Her researches focus on measuring and modeling users’ experience in social networks and IoT, as well as their impact on economy and society. Diploma: HDR, Ph Management at HEC, ESSEC, Master of econometry at ENSAE. She is also Chevalier de l'Ordre National du Mérite.

# ACCEPTED MANUSCRIPT

## Highlights

• We analyze ideas evaluation by participants in coopetitive crowd innovation contests within a network perspective.

• Our results reveal that in-degree, out-degree and authority scores are correlated with the received positive evaluation, whereas authority is negatively correlated with the number of evaluations made.

• By identifying the social influencers with network scores, we propose a methodology to reduce crowd innovation voting bias and to help managers to better select the ideas.

• We took into account your remarks and we made corrections and enrichment in the revised version of the paper.

• We worked for this modified version on the reduction of voting bias.

To increase our contribution, we propose an algorithm in order to decrease the biased votes and to reveal more unbiased scores to help managers of innovations in better selecting the promising ideas in a crowd innovation platform. Section 4.4 « Methodology to reduce voting bias » in the modified paper.

• Finally, we rewrite the discussion part and outline six contributions of our research.

![](/api/attachments/MGDRV3D4/fulltext/images/51d8c395c08d52b3c5e5e43f646b089fab6db15df1649895b414ee29033220cc.jpg)  
Figure 1
