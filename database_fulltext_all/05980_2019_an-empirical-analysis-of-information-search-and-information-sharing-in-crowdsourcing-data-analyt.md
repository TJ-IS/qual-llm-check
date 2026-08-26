---
otero_id: 5980
otero_key: "4XE3SVF5"
title: "An empirical analysis of information search and information sharing in crowdsourcing data analytic contests"
authors: "Daniel E. O'Leary"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.03.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An empirical analysis of information search and information sharing in crowdsourcing data analytic contests<sup>☆</sup>

![](/api/attachments/4XE3SVF5/fulltext/images/fd196abc9366c642b755b52857b8ed5db3a0e152556ee68be038e97bab6566c7.jpg)

Daniel E. O'Leary

University of Southern California, 3660 Trousdale Parkway, Los Angeles, CA 90089-0441, United States of Americ

## A R T I C L E I N F O

Keywords: User behavior Crowdsourcing Contest theory Social media Big data Data analytics Crowdsourcing as a service Crowdsourcing platforms Information sharing

## A B S T R A C T

Crowdsourcing provides the ability for contest developers to hold data analytics contests, gathering solutions from a set of potential participants typically allowing participants to communicate using social media for information search and sharing. Using a logarithmic model in an empirical analysis of crowdsourcing data, we find that the contest reward and time, is related, but with decreasing returns, to the number of participants and their efort to solve the contest problem. We also find that designers can gain increasing returns if they can engage additional participants to become a part of the crowdsourcing efort.

However, the primary purpose of this paper is to analyze the relationship between both the asking of questions (information search) and the answering of questions (information sharing) and the amount of reward associated with the crowdsourcing competition. In particular, we examine the question “does contest reward afect the amount of information search and sharing?” As part of that analysis, this paper empirically investigates the impact of the reward, length of the contest and development of the potential user base on participant behavior of information exchange, using contest theory to frame the analysis, generating a number of diferent empirical findings. We find that the analysis of the relationship between communication in topics and posts is consistent with building community, rather than self-interest.

## 1. Introduction

A recent trend is to gather the “wisdom of the crowd” e.g., [1]. One approach to gathering that wisdom that has generated momentum is to use crowdsourcing; that is, gathering inputs from a broad range of contributors, typically over the Internet. These eforts have resulted in a number of diferent types of crowdsourcing, including crowdfunding (e.g., Kickstarter), crowd voting (e.g., Launcht), crowdsourcing data gathering (e.g., CrowdFlower), crowdsourcing “big data” and “data analytics” (Kaggle.com), crowdsourcing design (e.g., 99designs.com) and a range of other approaches and problem types.

Our focus is on crowdsourcing data analytic contests. Since there is a “gap” in the availability of those with data analytic skills,<sup>1</sup> crowdsourcing provides a vehicle to access a “community” of knowledgeable potential participants. This can be done using “crowdsourcing as a service” (CSAAS) where those providing the service not only provide the platform but also access to the potential participant solvers. At the base of these “as a service” oferings, are platforms in which participants compete for rewards by providing potential solutions to a speci fied problem, typically in the form of a contest.

Contest designers have potential “levers” that they can use to facilitate the crowdsourcing, including choosing the “Reward” and the “Length” of the contest (Time). In general, ceteris paribus, crowdsourcing works better the more players and teams that are involved in the contest. Accordingly, contest designers are concerned with the potential ability of the Reward and Length of the contest to generate teams to participate in their contests. Thus, designers will be interested in addressing such issues as “how is the reward or the time related to the number of players or teams?” and “is the length of the contest related to the number of solutions submitted?”

In addition, contest designers are likely to choose a platform where that platform allows informed participants to be a part of the contests. Further, since informed contestants are better than uninformed contestants, contest designers are likely to find that there will be some form of social media built into the platform so that the contestants can communicate about the crowdsourcing efort, e.g., ask questions and potentially get answers to those questions. Thus, platform designers are concerned about the impact of their platform design on the resulting contests through both the potential participants and the ability of participants to both ask and answer questions (information search and information sharing). However, since there is a monetary Reward, there are concerns as to whether participants will share questions or answers using the platform because other participants could benefit from those information disclosures. As a result, contest designers and platform designers are interested in whether this social media-based platform structure will facilitate information search and information sharing.

## 1.1. Research objectives and findings

The primary research objective of this paper is to focus on the use of social media and information search and information sharing in these data analytic-based crowdsourcing settings. Social media provides the ability to share information – both ask questions and get answers. We likely would expect that the number of questions asked (“topics”) would be positively related to the reward ofered in the crowdsourcing contest. However, since asking questions can remove asymmetries of information (and thus may provide others with potential solution insights), there are disincentives to ask those questions, particularly as the reward increases, thus the result is not clear, a priori. Further, it is not clear what would we expect regarding the number of answer (“posts”) to those questions. Since there is a potential reward at stake, would we expect the number of answers to be positively, negatively or not related to the amount of the reward? Self-interest and the ad vantages that accrue to maintaining information asymmetries (e.g., [2,3] and others) would suggest a negative relationship and notions of “community” (e.g., [4]) could suggest a positive relationship as the community comes to the support of the question askers as part of the culture.

In this research, we find a positive relationship between the number of questions (topics) and the reward. However, the results regarding the relationship between the number of answers (posts) and rewards required multiple forms of statistical analysis. We found that statistical analysis of our “aggregate” data generated a negative relationship between the number of posts and the amount of the reward. However, when the data is matched using a propensity analysis is done, there is no relationship, but when a mediation analysis is done, there is a positive relationship between the number of posts and the amount of the reward, indicating that information sharing throughout is positively related to the amount of the reward, consistent with a “community” perspective.

This paper also addresses other issues of direct importance to developing “crowdsourcing as a service.” Since contest designers have to design contests, those contest designers are interested in the efects and relationships associated with the Reward and the Length of the contest. For example, does “more” Reward generate “more” crowdsourcing participants? Does a longer contest engage more contest participants? What if the contest designer were able to influence the number of potential participants?

## 1.2. Approach

This paper performs this analysis using crowdsourcing data derived of roughly 100 heterogeneous contests, from Kaggle.com (Kaggle), perhaps the largest and best-known data analytics crowdsourcing service. At Kaggle, companies post problems and data and allow individuals and teams to generate solutions for those problems and compete for monetary rewards. Kaggle provides a social media-based platform infrastructure and a potential pool of participants. Although players must register with Kaggle, creating an increasingly larger pool of potential participants, participation in any given contest is voluntary. As an example of the kind of competition that occurs at Kaggle, they have teamed with Netflix to use the crowd to generate a better movie recommendation algorithm.

## 1.3. Outline of this paper

This paper proceeds in the following manner. This first section has motivated and stated the research problem examined in this paper. Section 2 summarizes some of the previous literature from crowdsourcing, the impact of reward in crowdsourcing, contest theory and the intersection of crowdsourcing, contest theory and social media. Section 3 reviews the emerging industries of “crowdsourcing as a service,” provides some background about Kaggle and reviews the typical Kaggle contest and how that model is related to crowdsourcing in general. Section 4 reviews the data and the variables on which this paper is developed. Section 5 summarizes the expectations and hypotheses analyzed in this paper. Section 6 reviews the methodology used in this paper. Section 7 reviews the findings. Section 8 reviews those findings and discusses some of the implications for practice. Finally, Section 9 summarizes the paper, develops some potential extensions and reviews the contributions.

## 2. Selected previous literature

The purpose of this section is to briefly review the previous literature in crowdsourcing, the role of reward in crowdsourcing, contest theory, the intersection of crowdsourcing and contest theory and the use of social media-based approaches in such contests.

## 2.1. Crowdsourcing

Crowdsourcing has been defined as “the practice of obtaining needed services, ideas, or content by soliciting contributions from a large group of people and especially from an online community rather than from traditional employees or suppliers.”<sup>2</sup> The term “crowdsourcing” was developed in contrast to outsourcing, by firms that gathered information from the crowd [5]. Crowdsourcing has been studied for its contributions along multiple dimensions, in a range of diferent appli cation areas. A typology was developed for crowdsourcing [6] based inpart on Howe's [7] typology of crowdsourcing, including Crowdsourcing Co-Creation, Competitions, Voting, Wisdom and Funding. Tripathy et al. [6] summarize much of the information systems literature related to those five crowdsourcing types. Further, there have been a number of applications in diferent functional and application areas. For example, Gao et al. [8] investigated crowdsourcing for disaster relief.

Crowdsourcing is consistent with economic theory. For example, as noted by Hayek [9] “…knowledge (is) not given to anyone in its totality.” Instead “…the knowledge of the circumstances of which we must make use never exists in concentrated or integrated form, but solely as the dispersed bit of incomplete and frequently contradictory knowledge which all the separate individuals possess.” In addition to this notion by Hayek [9] that local information and knowledge difers, there are at least three other fundamental assumptions of gathering information from the crowd (e.g., [1]). First, one of the key assumptions is that there is better solution quality when there are more participants. Second, there is the assumption that there potentially is greater solution diversity with more participants. Third, more solutions are better than fewer solutions. Thus, there is interest in understanding what factors drive the number of participants and the numbers of their solutions or their efort in generating those solutions.

## 2.2. The role of the reward in crowdsourcing

Much previous research in crowdsourcing has focused on participants freely contributing to crowdsourcing projects (e.g., [10]). In particular, the crowd will often volunteer resources, time and ideas to diferent projects. However, if we assume self-interest then we would expect participants to be interested in direct returns/rewards for their participation. As a result, it is not surprising that there is substantial evidence that people are concerned with getting monetary rewards for their involvement in crowdsourcing activities. For example, there are a number of blogs that address the concern of participants receiving money for those involved in crowdsourcing, including topics such as “18 ways to earn money from crowdsourcing” (http://mashable.com/ 2011/04/01/make-money-crowdworking/). Further, crowdsourcing competitors have asked sponsors of such competitions “Could you please raise the prize money?” (https://www.kaggle.com/c/avazu-ctr prediction/forums/t/10963/could-you-please-raise-the-prize-money) As a result, although crowdsourcing often appears altruistic at first glance, there are very explicit calls for monetary prizes, suggesting the importance of such prizes or rewards in crowdsourcing.

Rewards typically take one of two diferent forms in crowdsourcing. First, rewards are given to the winners of contests. As noted in Dahl [11] prizes and competition are at the base of crowdsourcing in settings. There are a number of such settings where contests take place, such as coding (e.g., https://www.topcoder.com), designing (https:// 99designs.com), analytics and data science (e.g., https://www.kaggle. com/) and others. In reward settings, typically the reward is given to those with the highest quality or best solution. Second, rewards are given for just doing work, for example on Amazon Turk. However, this paper focuses on the first type, where there is a contest between the participants.

## 2.3. Contest theory

This paper uses “contest theory” as a substrate to investigate crowdsourced, reward-based competitions, focusing on the information system-based communications between competitors. Contests are characterized as having the following three key elements (e.g., [12]). First, there is some reward or prize that is to be won and split among the contestants. In its simplest form the prize goes to a single winner. Second, there is a given set of contestants. Third, contestants expend resources to win the prize. In particular, competing participants have the opportunity to improve the probability of winning a contest by expending scarce resources, such as efort, money, time or people (e.g., [13]). Another distinguishing feature of contests is that, in general it is assumed that the investment of efort is a “sunk cost,” and previous contest eforts are “non-retrievable” for the current contest (e.g., [14]). Efort ties to a particular contest and this paper analyzes these contests as stand-alone observations.

There has been some limited previous research on asymmetries of information in contests.<sup>3</sup> However, the focus of much of that research has generally been on asymmetries of information about the reward [12]. In contrast, in Kaggle and other contemporary crowdsourcing contests available over the Internet, the reward information is made widely and openly available and well-known. As a result, this research is not concerned with asymmetries of information about the reward. Instead this research is concerned about asymmetries of information that may help competitors drive toward a solution, either through in formation search or information sharing in response to those question generated through platform social media capabilities.

Our research is being done from the perspective of the contest and platform developers and not from the contest players. We assume a winner take all format as is typically the case in crowdsourcing contests, then winning teams can allocate the winnings as they see appropriate. Further, this paper addresses the notion that there can be diminishing returns associated with the efects of the reward, through the way that the model is formulated, as discussed in the methodology section. This finding is consistent with some of the theoretical literature

on contests [15].

Although there is interest of the crowd in rewards, there is some tension in the contest theory with rewards. In particular, there is evidence that a large reward can work against participation and efort. For example, as noted by Konrad [12] (also discussed further below) “Suppose that there are 1,000 contestants … and that the only benefit of participating in the contest is one given prize of a given size. In this situation, most of the contestants will be strongly discouraged and only a small group of top contestants will make a serious efort to win the prize.” As a result, in a crowd setting, the relationship between participants, efort, communications and reward is equivocal.

In addition, contest theory (e.g., [12]) typically assumes that the number of potential players is constant or the contest analyzed occurs at a point in time. As a result, historically the dynamics of the number of players is not an issue analyzed in contest theory. This paper directly addresses this issue by capturing a modeling variable aimed at the number of potential participants that are increasing over time. Finally, although there have been some references to the “length of the contest” in “contest theory” (e.g., [16]) there seems to be limited empirical analysis of the concept and its efects on participation in contest, efort, communication or other issues. As a result, this research directly accommodates the length of the contest as a variable of interest that is modeled and analyzed

## 2.4. Crowdsourcing and contest theory

Although there has been limited analysis of the integration of crowdsourcing and contest theory researchers have initiated investigation of some crowdsourcing and contest issues (see Dechaneaux et al. [13] for a recent review). For example, Archak and Sundararajan [17] provide a game theoretic model of a crowdsourcing contest that allowed them to theoretically investigate the optimal prize structure. They find that when the agents designing the contest are risk-neutral, the principal should optimally allocate their budget to the top prize even if it values more than one submission. In analysis of a crowdsourcing site in China, Shao et al. [18] found that higher awards, easier tasks, longer duration and lower competition intensity led to a higher number of solvers.

One assumption associated with integrating crowdsourcing and contest theory is that competition for a reward among the crowd leads to better solution quality. There has been some research to support this issue. For example, using simulations in a crowdsourcing context, Huang et al. [19] found that “… when the firm increases the award … individuals would submit more designs and exert more efort.” In an other recent study Araujo [20] in an analysis of 99designs.com found that financial incentives had an efect on the quality of the design and attracted a larger pool of designers. Hofstetter et al. [21] developed an experiment where they found that ofering more prizes motivates more high-performing individuals to participate again and to put in more creative efort. Similarly, Chaudhari [22] found that ofering more rewards generated more participation.

## 2.5. Embedding social media in crowdsourcing-based contests

Diferent than the emerging literature at the nexus of crowdsourcing and contest theory this paper is primarily concerned with the efects of using social media in crowdsourcing contests. In particular, this paper is most concerned with pushing the edges of contest theory to consider the impact of “information search” and “information sharing” as accommodated in social media, since with social media people can ask questions to the world as part of their information search and with social media, people can answer questions (e.g., [23]).

Contest theory was created before one of the most engaging developments of the twenty-first century: social media. As a result, contest theory largely ignores social media capabilities. In contemporary society, social media is one of the primary tools for communication.

Accordingly, in spite of the fact that contest platforms, typically include social media capabilities, classic contest theory does not account for social media. As a result, this paper integrates social media question asking and answering into our use of contest theory.

Classic contest theory researchers have studied how the efects of information sharing between competitors can afect the competition in a contest (e.g., [24]). However, much of that research pre-dates social media and does not consider the efects of contests in a social media setting. There has been very limited research embedding contest theory, crowdsourcing and rewards. Some researchers (e.g., [25]) note that social media is being embedded in crowdsourcing but don't create models built around its use.

However, many contemporary crowdsourcing contest systems build in social media capabilities. As a result, it is not surprising that increasingly social media is being embedded in competitive contest situations available on the Internet. Use of social media likely broadly informs a participant which other competitors are interested in the particular competition and what are some of the key concerns and issues associated with the contest. For example, statements and questions provided as “topics of discussion” using social media inform others of key concerns and issues. Further, such information could be used to imitate potential approaches and successful competitors. Similarly, “posted” answers to those questions can work to further remove information asymmetries and potentially, broadly further inform competitors. As a result, social media can work to remove information asymmetries between competitors, e.g., work as additional information disclosures.

Typically, contest designers want better and high quality solutions. Since broadly informing competitors is likely to generate better solu tions, it typically is to the advantage of the contest developer to facilitate such information exchange and remove information asymmetries. Further, contest designers likely are interested in determining if contest platforms with question asking and answering capabilities “work” and don't discourage information exchanges. Unfortunately, there has been limited analysis of communications, in the context of contest theory participation in the use of computer-based systems, particularly social media-based systems.

## 3. Kaggle and Kaggle contests: crowdsourcing analytics as a service

Kaggle, founded in 2010, provides a very general information sys tems platform for predictive modeling and analytics competitions on which companies and researchers post their data, and statisticians, ar tificial intelligence researchers and data miners from all over the world compete to produce the best models. Contestants typically receive a reward or prize for winning the contest. Recently, Kaggle was acquired by Google, suggesting that although Kaggle currently may be a key industry competitor, their influence is likely to increase. Kaggle has received substantial media attention deriving from their model of crowdsourcing data analysis using competitions. A broad base of companies have partnered competitions on Kaggle, including Ford, Deloitte, Booz Allen, Merck, Allstate, Liberty Mutual, EMC and others. In addition, a number of nonprofit organizations, such as NASA, NSF, U. S. Census, American Epilepsy Society and others also have partnered competitions.

There are a number of industries, that we broadly refer to as “crowdsourcing as a service” (CSAAS). In particular, there are a number of emerging industry segments where the crowd participates in contests with rewards in order to help solve a problem. Currently, the approach used by Kaggle to facilitate the “as a service” is almost identical across these industries.<sup>4</sup> A key aspect of this crowdsourcing “as a service” is the development of related “communities” of potential participants for those contests. For example, Kaggle has been referred to as the “world's largest machine learning community.”<sup>5</sup> As a result, Kaggle is among the best known in CSAAS.<sup>6</sup> Recently, the Wall Street Journal has touted Kaggle as one of the world's largest data science companies that provides the most “eficient” access to artificial intelligence talent.<sup>7</sup>

## 3.1. Kaggle crowdsourcing contests

Although a number of hybrid approaches can be executed using Kaggle, there is a general approach associated with each Kaggle contest and similarly other crowdsourcing settings. In a typical crowdsourcing contest, there is a single start date and a single completion date. There typically is a reward (prize) for winning the contest. That prize may be winner-take-all, prizes may be allocated for first, second and third place, or alternative arrangements can be made. At the start of the contest, data is posted for the specific contest. In addition, there typically is a single date after which entries can be submitted. There may be limits on the number of entries per day per team or player, and there may be a limit on the final number of submissions. Although crowdsourcing brings people together to solve a problem, Kaggle tries to keep diferent groups and players separate to a certain extent. There typically are limitations on the number of accounts per participant (e.g., one) and the extent to which sharing among teams is allowed (in order to maintain independence of solutions). This set of processes is very general and used in many crowdsourcing settings.

As with crowdsoucing in general, at Kaggle feedback to the participants is accomplished through social media. There are “Topics” (information search) and “Posts” (information sharing) and public leader boards summarize leading solutions. Contests allow questions using “Topics,” to potentially disambiguate issues associated with the contest. In addition, contestants can provide answers to the “Topics” with socalled “Posts.” As a result, Kaggle's platform provides a very general social media-like subsystem in support of the contests, with such question asking and answering.

In addition, there are a number of rules related to submission of solutions.<sup>8</sup> For example, participants have both public and private leaderboards that capture the relative ranking of the solutions that they have generated for each contest that they enter. Public scores are received for each submission and are computed based on only a fraction of the public test data, typically 25%–33%. After the competition is over, the solutions are run on the remaining test data. Final results are based on the private leaderboard. As noted by Kaggle, “This separation of the test set into public and private portions is what ensures the most accurate but generalized model is the one that wins the challenge.”

## 3.2. Diferences between crowdsourcing contests and contest theory

It appears that four diferent factors, deriving from crowdsourcing contests, have received limited attention in contest theory: information search (particularly using social media), information sharing (with social media), potential number of participants and length of the contest. In classic contest theory, contestants apparently do not seek information regarding the process of generating innovations for the contest. As a result, in contest theory there is not a focus on information flows that occur as part of the social media side: “Topics” or “Posts.” Accordingly, although classic contest theory includes a role for information search, it does not seem to investigate information search as implemented as social media in an information systems platform, such as Kaggle. In addition, contest theory does not provide a role for information sharing as can be generated using social media. These issues are the primary focus of this paper. In addition, classic contest theory does not seem to account for the number of potential participants. In classic research tournaments, the number of contestants is set. However, for example, as noted by Harris,<sup>9</sup> Kaggle had access to fewer than 5000 participants at the end of 2010, roughly 22,500 participants at the end of 2011, approximately 70,000 participants at the end of 2012 and went over 100,000 potential participants roughly halfway through 2013. In June 2017, there were over 1000,000 members<sup>10</sup> Additionally, Kaggle contests occur over diferent lengths of time. Contests may be a single day (or less) and they can take years. It is likely that the contest duration could afect a number of issues related to contests, including the number of participants and their efort.

## 3.3. Generality of Kaggle contest (crowdsourcing as a service)

Kaggle's approach to crowdsourcing is very general. Aspects of its approach are present in a wide range of crowdsourcing settings. Generally crowdsourcing has participants “sign-up” in order to participate as is done at Kaggle. This allows development of a potential set of participants in the crowdsourcing events. Typically, crowdsourcing events have a limited life, as is done at Kaggle. Crowdsourcing events may have a reward, as seen at Kaggle. Crowdsourcing events also ty pically have some sort of social media basis. Broadly there are two such social media-based approaches: generating questions and answers or posting comments.

## 3.4. “Successful” Kaggle competitions

There are likely multiple ways to determine the success of a Kaggle. com contest. At one level, a “successful” competition for a contest is one that generates a high quality solution to the given problem and a solution that the company can use, although these may not be related. Unfortunately, our data does not include a measure of quality. Further, it is unlikely that it would even be possible to provide a common acceptable measure of quality for the roughly one hundred highly heterogeneous Kaggle.com competitions in our sample. Even if there was, it is unlikely that the sponsor would be willing to share information about the quality issue. As a result, this paper does not measure or analvze quality, per se.

However, crowdsourcing is more likely to generate a quality solution if there are more (rather than less) teams or individuals participating. In addition, crowdsourcing is more likely to generate a quality solution if there are more (rather than fewer) solutions. In any case, the sponsor of the contest can always choose to not use any of the submitted solutions. Accordingly, our first concern is estimating the factors that are related to the contest participants (Teams and Players), and the measure of efort as seen in submitted solutions (Entries) focusing on the concerns of the contest designer.

## 4. Data and variables

Data was gathered from Kaggle.com.<sup>11</sup> At that web site competition data is available including the following five sets of variables: Reward, Participants, Efort Level (number of entries), Date of the Contest, Length of the Contest and Social Media supporting the contest (numbe of topics and posts for those topics).

## 4.1. Reward

Contests typically have a dollar reward that is provided to the winning team. However, not all competitions have had explicit dollar rewards. For example, the reward for some contests was listed as “Swag,” “Knowledge,” “Jobs,” “kudos” or “\$ 0.” As a result, the data was divided into two sets, those with a dollar reward and those with no dollar reward. At the time that the data was gathered there were 124 competitions with non-zero dollar rewards and 19 competitions with no dollar reward. The scope of this paper includes only those competitions with a non-zero dollar reward.

## 4.2. Participants: actual number of participating teams and players

There are two diferent measures associated with the number of participants in the Kaggle contests: teams and players. “Teams” measures the number of teams reported by Kaggle as participating in a given competition. “Players” measures the number of individuals participating in a given Kaggle competition, i.e., the number of players on those teams. The number of players also provides a measure of the available potential human resources that are currently engaged to solve the Kaggle competitions.

## 4.3. Efort level: number of entries by participants

“Entries” captures the number of entries or solutions proposed as part of a given Kaggle competition. As a result, Entries is used to model the efort variable.

## 4.4. Number of users

As noted above the number of participants available to participate in a Kaggle competition has been growing substantially over time. The number of “downloaders of competition datasets” at the time of the contest was used to provide the potential number of users or participants in any Kaggle contest.

## 4.5. Length of the contest

Each contest had a certain duration determined as the diference between the start of the contest and the end of the contest, as measured in days. That duration is referred to as the length of the contest. Intuitively, a longer duration provides the opportunity for more po tential participants and more potential efort. In addition, a longer contest provides the potential for more communications using the social media aspects of Kaggle.

## 4.6. Social media: topics and posts

Competitions inevitably generate questions by participants and potential participants. As a result, Kaggle contests have structured a “social” side that allows question asking, etc., but that question asking is visible to all potential competitors. In particular, associated with each Kaggle contest is the ability to post questions or assertions, referred to as “Topics.” In addition, other players can respond to those topics with additional “Posts.” Posts may be diferent proposed answers to topic questions. In any case, posts are sequentially dependent on topics.

In Kaggle, “Topics” cover a number of diferent discussion points initiated by a range of diferent people, including competition administrators and participants. Topics generally capture information search eforts, while Posts capture information sharing eforts. Topics and posts could provide insight to the participants about a range of othe related issues, including “who” is planning on participating in the contest, “how much” potential efort will be required to solve the problem, “how to solve” the problem and other concerns. In the past, topics have included issues such as

• Questions and discussions about the data set, e.g., test data vs. training data

• Questions about typos in formulas

• Questions about the data

Questions about the scoring metric

• Was anyone able to compile a program that was used to generate the benchmark?

• Who had the winning solution?

• What approach was used to solve the problem?

• Making the participants aware of a survey to study demographics of participants

• To ask if there was an academic paper about the competition

As a result, Topics include information search that can afect the competition. Posts to the Topics include responses to the topic by others who have seen the original topic – post discussion. Accordingly, Topics are often question-based while Posts are more answer-based.

## 4.7. Data observations excluded

This analysis uses ninety-eight heterogeneous contest observations. Four observations (contests) were removed because they used a different process than the rest, employing multiple deadlines and sub missions. Eleven observations did not have complete information. Ten observations were not included because the time frame that the contest was open was either too short (e.g., one day) or too long (more than a year). One observation was eliminated because the reward included rewards beyond the monetary rewards (e.g., a potential trip and tour of the organization). Accordingly, twenty-six of the one hundred and twenty-four reward-based contests available at the time the data was gathered were not included in the data and analysis.

## 5. Expectations and hypotheses

This section summarizes the three basic sets of hypotheses ad dressed in this paper and the expectations associated with those hypotheses. The diferent terms for participants in these contests is given in Table 1.

## 5.1. Estimating the number of participants and their efort

Contest theory suggests that the resources and efort that are devoted to a contest are a function of the amount of the reward. For ex ample, as noted by, e.g., Corchon [26], the number of participants in a contest is expected to depend positively on the amount of the reward. In addition, contest theory also suggests that the efort generated for a contest is a function of the reward. However, the relationship between the number of contestants, efort and the reward can be equivocal as noted above [12].

Contest theory often assumes a stable set of potential participants, however, in the case of Kaggle, the number of potential participants is increasing over time. As a result, we would expect the number of participants in any contest to be related to that potential set of participants (“Users”): the larger the potential set of Users the larger the number of actual participants and their corresponding efort. Accordingly, in this research the variable “Users” would be expected to be positively related to the number of players and teams and their efort in any specific contest. We treat the number of Users as a control variable, since although a contest designer might be able to change the number of potential participants through publicity and other eforts, it is likely that number is stable but, as seen above, growing.

Table 1  
Roles in contests.

<table><tr><td>Role</td><td>Description</td></tr><tr><td>Player</td><td>Anyone participating in a particular contest</td></tr><tr><td>Team</td><td>A team made up of players who are participants in a particular competition</td></tr><tr><td>Entities</td><td>Players and teams, that participate in a contest</td></tr><tr><td>User</td><td>Anyone registered to potentially participate in a contest</td></tr></table>

Further, although contest theory has only limited research with respect to the length of the contest, it is easy to imagine that potentially the longer a contest runs the more participation that it will garner and the more efort that can be generated. As a result, we would expect that the Length of the contest would be positively related to both participation and efort. This discussion results in the following two hypotheses:

Hypothesis 1a. (Contest Designer): The number of entities (Teams and Players) that submit entries to a contest is positively related to the Reward, the number of Users and the Length of the contest (Time).

Hypothesis 1b. (Contest Designer): The efort (Entries) submitted to a contest is positively related to the Reward, the number of Users and the Length of the contest (Time).

Although a positive relationship is expected between reward and both numbers of participating entities (Teams and Players) and efort, there is likely to be diminishing returns associated with that reward. As noted in the example above [12], as the reward increases, the likelihood of any one entity winning decreases as the number of participating entities increases. This issue is discussed in greater detail in the methodology section with the formulation of the estimation model.

## 5.2. Estimating the number of topics (information search)

The ability for participants to do information search is facilitated by the design of the platform. Information search is initiated as decision makers generate information needs [27]. The number of topics initiated as part of the social media about a contest provides one measure of the extent of information search (question asking) generated by the participants. The more topics, the more information searches being conducted by the participants. In general, we would expect that the number of topics (amount of information search) would be positively related to the reward, amount of efort and length of the contest. We also use the potential number of participants as a control variable.

The greater the reward associated with the contest, the more help (questions, clarifications, etc.) that would be expected to be solicited in the contest. In particular, contest participants would work to remove ambiguities from their potential solution of the problem. Further, with more contest participants we would expect more activity in social media, since there would be more people to ask questions. As a result, we generally would expect a positive relationship between the number of topics and reward. In addition, the more the efort, the more questions or topics that might be raised. Further, the longer the length of the contest, the more the opportunity to generate more Topics because there is more time to analyze and research question. Finally, we would expect that the number of potential participants (Users) would be positively related to the number of topics because potential participants could be exploring the opportunities to become involved in a contest by asking questions or expressing concerns about that contest. This discussion results in the following hypothesis.

Hypothesis 2. (Information Search): The number of Topics for a contest is positively related to the Reward, the number of potential participants, the number of participants (Teams and Players), the efort (Entries) and the Length of the contest.

## 5.3. Estimating the number of posts (information sharing)

It is likely that the number of posts is positively related to the number of topics, since there can be no “Posts” without “Topics”: they are sequentially related. Accordingly, the number of topics is expected to be positively related to the number of posts. Further, as seen below we start with the number of Topics in the estimation of the number of Posts and try to determine if there is any additional information added with other variables. People ask questions in the topics and people share answers in the posts. Thus, Topics represent information search, while Posts represent information sharing [28].

A priori, it is not clear if the number of posts would be positively related, negatively related or not related to the Reward. First, self-in terest [2,3] would suggest that if contestants want the reward for themselves or their team, then they probably would not clarify a Topic (not Posting) for another participant or team, even if they knew the answer or had an opinion – they would maintain information asym metries. Second, history is based on the notion of human cooperation (e.g., [4]), where such cooperation is not always dependent on monetary rewards. Further, even game theory touts notions of cooperative games, and the “fairness” and “naturalness” of outcomes. Third, Constant et al. [29] found that “organizational ownership” of information afected attitudes toward “sharing” information. At one level, when a topic is posted, that posting gives ownership of the topic either to the poster or to the community. In this case, if the Reward is positively related to the number of Topics, then there would likely be a positive relationship between the number of Posts and the Reward. Because of these three perspectives, we do not choose to hypothesize, a priori, the relationship with the number of posts and reward. However, based on the reasoning used above, the number of posts is likely to be related to the number of participants (Teams, Players) and their eforts (Entries), for the same reasons noted in the estimation of Topics. In addition, both the number of potential participants and the length of the contest are likely to be positively related to the number of posts, for the same reason as the number of topics. This discussion is summarized in Hypothesis 3.

Hypothesis 3. (Information Sharing): The number of posts for a contest is positively related to the number of participants (Teams and Players), the efort (Entries), the number of Topics, the number of potential users and the length of the contest.

The three hypotheses are summarized in Fig. 1.

## 6. Methodology and estimation model

This section of the paper discusses the methodology used to analyze the data. A logarithmic model was developed to model the contest theory structure of the variables and setting. Classical statistical tool were used to investigate those models. This research employed pro pensity score matching and performed a mediated variable analysis to better understand the underlying relationships between the variables.

## 6.1. Logarithmic model

An empirical exponential/logarithmic relationship between price and quantity has been observed in marketing statistical models (e.g., [30], p. 260). In the same sense that in marketing a particular sales price is expected to generate a particular sales volume, in a crowdsourcing contest a particular reward could be expected to generate a specific number of contestants. As a result, this research employs that same structural relationship between the reward and the quantity of participants in a Kaggle contest. In this paper we model the relationship between price and volume using that marketing approach. Let Log (Ω) represent the natural logarithm of Ω.

${ \mathrm { Q u a n t i t y } } = \alpha ^ { * } ( { \mathrm { P r i c e } } ) ^ { * * } \beta .$ , where it is expected that $1 > \beta > 0 .$

“Quantity” will be used to measure a range of diferent goods: number of teams, number of participants, number of entries, number of topics, and number of posts as given in the hypotheses. “Price” will be measured using the contest reward for winning. As a result, we will examine models of the type seen in the following example:

Log (number of participants) Log= $( \alpha ) + \beta ^ { \ast }$ Log (contest Reward),

where $" \alpha "$ is the intercept and $" \mathrm { { \beta } } ^ { \prime \prime }$ is a regression coeficient. β provides insight into the relationship between the increases of the reward on the number of participants, etc. This log model has an interesting interpretation in that a 1% increase in the reward will increase participation by β%. $\mathrm { I f } 1 > \beta > 0$ then there are diminishing returns associated with increasing the reward. We would expect such a range on $\beta$ because as the reward increases not just more, but better competitors likely will be drawn to the contest. As more and better competitors are drawn into the contest, then the probability of participants of winning is likely to decrease. Since Kaggle displays information about competitors that is readily available to all of the other competitors. Thus, although larger rewards would be expected to bring additional competitors to the competition, they will also scare away other competitors, resulting in diminishing returns in terms of quantity of participants, efort, etc.

## 6.2. Statistical analysis

Factor analysis was used to investigate the number of factors in portions of the data. In addition, correlation analysis and standard least squares were used to find which variables were statistically significantly related to the dependent variables. The statistical package SAS - JMP was used throughout.

![](/api/attachments/4XE3SVF5/fulltext/images/2b644868bc66c9d0ff8310bd9c3ac338c0cb5d268974a642ce7c403dacff475f.jpg)  
Fig. 1. Pictorial summary of three hypotheses

## 6.3. Multi-collinearity

The extent of multi-co-linearity was tested in each equation using the “variance inflation factor” (VIF). In the literature (e.g., [31]) it is recommended that the VIF be 4 or below. Because of the high correlations between Teams, Players and Entries no equation estimation was done with two or more of those variables. Ultimately, in each of the other regression equations estimated below, VIFs were below 3, sug gesting limited multi-collinearity among the variables.

## 6.4. Propensity score matching

Based on the previous literature ([32,33], and others) this paper used propensity scores to match a subset of the contests with each other, as a means of investigating “causal relationships”. This research used a propensity analysis to make sure that similar events were com pared and to allow for control over confounding observations. Accordingly, the data was divided into “high” reward contests and “low” reward contests. Using roughly the mean of the original sample resulted in 27 observations at or above \$13,000 and 71 observations below \$13,000.<sup>12</sup> Propensity scores were generated based on models developed using the year of the contest and the length of the contest. Using propensity scores those 27 high reward observations were matched with 27 of the remaining 71 observations, resulting in 54 total observations in the matched sample, and 44 unused observations.

## 6.5. Demonstrating mediation

In this research we also investigated the data for mediation efect (e.g., [34]), in the relationship between topics and posts. As noted by Barron and Kenny [35], in order to demonstrate mediation three dif ferent regression equations need to be estimated. First, the independent variable is used to estimate the dependent variable and the independent variable is found to be statistically significant. Second. the mediator variable must be estimated from the same independent variables and the independent variable is found to be statistically significant. Third, the dependent variable must be estimated using both the independent variables and the mediator. If mediation is occurring then the mediator variable will be significant in the third equation. In addition, the previously significant relationship between the independent variable (Re. ward) and the dependent variable (Posts) will no longer be significant. These three equations are illustrated in the path diagram in Fig. 2.

## 7. Findings

This section summarizes the analysis of the data, including a sum mary of the correlation findings and the findings for each of the hypotheses. The analysis contrasts the findings from the full sample (N = 98) and the matched sample (N = 54). The results from the two samples are similar for Hypotheses 1 and 2. However, for hypothesis $^ { 3 , }$ which analyzes the relationship between Reward and Posts, the findings between the two samples are diferent. The results are summarized in Fig. 3.

## 7.1. Data summary

The summary statistics are given in Table 2. That panel includes means for the entire sample $( \mathbb { N } = 9 8 ) ,$ , the matched sample $( \mathrm { N } = 5 4 ) ;$ the high reward group (N = 27), the matched low reward group (N = 27) and all of the low reward contests (N = 71), including those

![](/api/attachments/4XE3SVF5/fulltext/images/acd6fe822eb30d2811c00516cb6061b84839dbb3739681bf74cff0a929dc49ef.jpg)  
Fig. 2. Mediator variable [34,35].

in the matched sample.

## 7.2. Correlation findings

The correlation coeficients for the matched data are summarized in panel A of Table 3 and the statistical significance of that data is summarized in Table 3, panel B.

Reward is statistically significantly correlated with both social media variables: Topics and Posts. The people resources (entities) of “Teams” and “Players” are highly correlated with each other and with the efort, as captured by “Entries.” In addition, each of the resource and efort variables are statistically significantly correlated with each of Topics and Posts. Finally, Topics and Posts are statistically significantly correlated with each other.

## 7.3. Factor analysis - estimation of Teams, Players and Entries

The variables that make up the measures of the number of participants and the amount of efort are all particularly highly correlated with each other, suggesting that although theoretically there are two diferent sets of variables, empirically there is one factor. Because of their high correlations, a factor analysis was done to determine the number of factors in this data. Maximum likelihood and common factor analysis found a single factor, with a Chi-Square test of < 0.0001. See Table 4 for Eigenvalue information.

## 7.4. Hypotheses 1a and 1b – estimation of entities and efort (Table 5)

This research used the independent variables of Reward, number of potential Users and the Length of the contest to estimate the number of Teams, Players and Entries that ultimately were formed for the contests. Each of Hypotheses 1a and 1b was substantiated, at least in part using both the entire sample and the matched data. The regression equations for the estimation of Teams, Players and Entries are given in Table 5. The results indicate that when estimating the number of Teams, Players, or Entries, the Reward was positive and statistically significant at no worse than p = .0099, while Users was positively and statistically significant at better than 0.0001 in each of the equations. In the full contest, length of the contest was only statistically significant in estimating the efort variable Entries. The β regression coeficients on Reward ranged from roughly 0.2141 to 0.2677, with $0 . 0 0 0 9 \leq \mathbf { p } \leq . 0 0 9 9$ . These results for the log model suggest a diminishing returns model on $\beta ,$ the coeficient on Reward, with $1 > \beta > 0 .$ However, there are increasing returns to scale in the matched sample for the variable Users with coeficients ranging from 1.2722 to 1.6134 when using the matched sample. This coeficient provides a measure of the “robustness” of the Kaggle platform and this coeficient would be important for comparing Kaggle to other platforms. Thus, both contest designers and platform designers would be interested in this coeficient.

![](/api/attachments/4XE3SVF5/fulltext/images/68a325b2667f3a76ee9b6ecc4366ad0d3b09869854d705cf0412723a1b5a6200.jpg)  
Fig. 3. Matching of hypotheses and results

Table 2  
Data summary<sup>a</sup>.

<table><tr><td>Variable</td><td>Mean (N = 54)</td><td>Std. Dev. (N = 54)</td><td>Min (N = 54)</td><td>Max (N = 54)</td><td>Mean - entire sample (N = 98)</td><td>Mean - high reward (N = 27)</td><td>Mean - matched low reward (N = 27)</td><td>Mean - all low reward (N = 71)</td></tr><tr><td>Reward</td><td>20,175.93</td><td>28,960.1</td><td>500</td><td>175,000</td><td>13,043.34</td><td>34,574.07</td><td>5777.78</td><td>4855.59</td></tr><tr><td>Length-Days</td><td>76.62</td><td>26.89</td><td>31</td><td>157</td><td>71.39</td><td>79.78</td><td>73.48</td><td>68.2</td></tr><tr><td>Users</td><td>87,150</td><td>39,983</td><td>41,330</td><td>170,050</td><td>67,280</td><td>92,790</td><td>81,510</td><td>42,900</td></tr><tr><td>Teams</td><td>431.83</td><td>424.96</td><td>27</td><td>1785</td><td>339.11</td><td>568.52</td><td>295.15</td><td>251.87</td></tr><tr><td>Players</td><td>509</td><td>488.81</td><td>29</td><td>1942</td><td>393.8</td><td>667.26</td><td>350.74</td><td>289.8</td></tr><tr><td>Entries</td><td>6949.7</td><td>8885.05</td><td>205</td><td>36,065</td><td>4922.61</td><td>9827.52</td><td>4071.89</td><td>3057.37</td></tr><tr><td>Topics</td><td>64.69</td><td>37.32</td><td>11</td><td>190</td><td>51.56</td><td>82.07</td><td>47.3</td><td>39.96</td></tr><tr><td>Posts</td><td>457.57</td><td>365.75</td><td>38</td><td>1841</td><td>365.62</td><td>608.93</td><td>306.22</td><td>273.1</td></tr></table>

<sup>a</sup> Median values for reward were 11,500 (N = 54), 8000 (N = 98), 25,000 (N = 27), 6000 (N = 27) and 5000 (N = 71).

## Table 3

Correlation coeficients for matched data.

<table><tr><td>N = 54</td><td>Reward-Ln</td><td>Users-Ln</td><td>Length-Ln</td><td>Teams-Ln</td><td>Players-Ln</td><td>Entries-Ln</td><td>Topics-Ln</td></tr><tr><td>Reward-Ln</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Users-Ln</td><td>0.0154</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Length-Ln</td><td>0.2027</td><td>0.2367</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Teams-Ln</td><td>0.3314</td><td>0.6368</td><td>0.2261</td><td></td><td></td><td></td><td></td></tr><tr><td>Players-Ln</td><td>0.3271</td><td>0.6388</td><td>0.2494</td><td>0.9967</td><td></td><td></td><td></td></tr><tr><td>Entries-Ln</td><td>0.3064</td><td>0.6207</td><td>0.2857</td><td>0.9334</td><td>0.9316</td><td></td><td></td></tr><tr><td>Topics-Ln</td><td>0.4734</td><td>0.5209</td><td>0.4095</td><td>0.7013</td><td>0.7163</td><td>0.6559</td><td></td></tr><tr><td>Posts-Ln</td><td>0.4450</td><td>0.5718</td><td>0.3795</td><td>0.7905</td><td>0.7950</td><td>0.7332</td><td>0.9372</td></tr></table>

Panel B – statistical significance of correlation coeficients (N = 54)

<table><tr><td>N = 54</td><td>Reward-Ln</td><td>Users-Ln</td><td>Length-Ln</td><td>Teams-Ln</td><td>Players-Ln</td><td>Entries-Ln</td><td>Topics-Ln</td></tr><tr><td>Reward-Ln</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Users-Ln</td><td>0.9122</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Length-Ln</td><td>0.1415</td><td>0.0848</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Teams-Ln</td><td>0.0144</td><td>&lt; 0.0001</td><td>0.1002</td><td></td><td></td><td></td><td></td></tr><tr><td>Players-Ln</td><td>0.0158</td><td>&lt; 0.0001</td><td>0.0690</td><td>&lt; 0.0001</td><td></td><td></td><td></td></tr><tr><td>Entries-Ln</td><td>0.0242</td><td>&lt; 0.0001</td><td>0.0362</td><td>&lt; 0.0001</td><td>&lt; 0.0001</td><td></td><td></td></tr><tr><td>Topics-Ln</td><td>0.0003</td><td>&lt; 0.0001</td><td>0.0021</td><td>&lt; 0.0001</td><td>&lt; 0.0001</td><td>&lt; 0.0001</td><td></td></tr><tr><td>Posts-Ln</td><td>0.0007</td><td>&lt; 0.0001</td><td>0.0047</td><td>&lt; 0.0001</td><td>&lt; 0.0001</td><td>&lt; 0.0001</td><td>&lt; 0.0001</td></tr></table>

Table 4  
Factor analysis of Teams, Players and Entries.

<table><tr><td colspan="4">Eigenvalues</td></tr><tr><td>Number</td><td>Eigenvalue</td><td>Percent</td><td>Cum Percent</td></tr><tr><td>1</td><td>2.9266</td><td>97.552</td><td>97.552</td></tr><tr><td>2</td><td>0.0704</td><td>2.346</td><td>99.898</td></tr><tr><td>3</td><td>0.0031</td><td>0.102</td><td>100.000</td></tr></table>

## 7.5. Hypothesis 2 – estimation of topic (Table 6).

The research used two sets of variables to estimate the number of Topics, the independent variables of Reward, Users and Length, and the resulting participation (Teams and Players) and the efort (Entries). The regression results for estimation of “Topics” for both samples are summarized in Table 6 estimating topics using Reward-Ln, Users-Ln and Length-Ln. The results confirm Hypothesis 2.

The results for the original data and the matched sample are very similar. Reward was statistically significant at better than or equal to p = .0019 in each of the two equations. Length was statistically significant or marginally significant in each regression equation. The number of potential Users was statistically significant in all but one of the equations. Since Teams, Players and Entries load as a single factor and since they are so highly correlated we will only include the regressions for Team and Entries to illustrate their impact on the primary focus of this paper, the Topics and the Posts.

Table 5  
Estimation of Teams, Players and Entries (Hypothesis 1).

<table><tr><td></td><td>N = 98</td><td>N = 54</td><td>N = 98</td><td>N = 54</td><td>N = 98</td><td>N = 54</td></tr><tr><td>Model</td><td>Teams</td><td>Teams</td><td>Players</td><td>Players</td><td>Entries</td><td>Entries</td></tr><tr><td>R Square</td><td>0.3305</td><td>0.5091</td><td>0.3692</td><td>0.5100</td><td>0.3516</td><td>0.4805</td></tr><tr><td>Reward-Ln</td><td>0.2141</td><td>0.2307</td><td>0.2221</td><td>0.2230</td><td>0.2402</td><td>0.2677</td></tr><tr><td>Prob &gt; |t|</td><td>0.0018</td><td>0.0027</td><td>0.0009</td><td>0.0035</td><td>0.0043</td><td>0.0099</td></tr><tr><td>VIF</td><td>1.2768</td><td>1.0441</td><td>1.2768</td><td>1.0441</td><td>1.2768</td><td>1.2768</td></tr><tr><td>Users-Ln</td><td>0.5020</td><td>1.285</td><td>0.5268</td><td>1.2722</td><td>0.635</td><td>1.6134</td></tr><tr><td>Prob &gt; |t|</td><td>0.0003</td><td>&lt; 0.0001</td><td>0.0001</td><td>&lt; 0.0001</td><td>0.0002</td><td>&lt; 0.0001</td></tr><tr><td>VIF</td><td>1.1533</td><td>1.0606</td><td>1.1533</td><td>1.0606</td><td>1.1533</td><td>1.1533</td></tr><tr><td>Length-Ln</td><td>0.3283</td><td>0.03253</td><td>0.3718</td><td>0.1004</td><td>0.6827</td><td>0.3039</td></tr><tr><td>Prob &gt; |t|</td><td>0.1671</td><td>0.9049</td><td>0.1061</td><td>0.7113</td><td>0.0208</td><td>0.4148</td></tr><tr><td>VIF</td><td>1.1165</td><td>1.1058</td><td>1.1165</td><td>1.1058</td><td>1.1165</td><td>1.1165</td></tr></table>

Table 6  
Estimation of the number of topics (Hypothesis 2).

<table><tr><td></td><td>N = 98</td><td>N = 54</td><td>N = 98</td><td>N = 54</td><td>N = 98</td><td>N = 54</td></tr><tr><td>R Square</td><td>0.5434</td><td>0.5294</td><td>0.6746</td><td>0.6258</td><td>0.6438</td><td>0.5899</td></tr><tr><td>Reward-Ln</td><td>0.1963</td><td>0.1928</td><td>0.1371</td><td>0.1284</td><td>0.1491</td><td>0.1494</td></tr><tr><td>Prob &gt; |t|</td><td>&lt; 0.0001</td><td>&lt; 0.0001</td><td>&lt; 0.0001</td><td>0.0059</td><td>&lt; 0.0001</td><td>0.0019</td></tr><tr><td>VIF</td><td>1.2768</td><td>1.0441</td><td>1.4166</td><td>1.2516</td><td>1.3929</td><td>1.1943</td></tr><tr><td>Users-Ln</td><td>0.3016</td><td>0.5979</td><td>0.1628</td><td>0.2385</td><td>0.1769</td><td>0.3357</td></tr><tr><td>Prob &gt; |t|</td><td>&lt; 0.0001</td><td>&lt; 0.0001</td><td>0.0114</td><td>0.1275</td><td>0.0089</td><td>0.0360</td></tr><tr><td>VIF</td><td>1.1533</td><td>1.0606</td><td>1.3225</td><td>1.8663</td><td>1.3342</td><td>1.7434</td></tr><tr><td>Length-Ln</td><td>0.3764</td><td>0.3511</td><td>0.2855</td><td>0.3420</td><td>0.2422</td><td>0.3017</td></tr><tr><td>Prob &gt; |t|</td><td>0.0026</td><td>0.0410</td><td>0.0075</td><td>0.0278</td><td>0.0320</td><td>0.0635</td></tr><tr><td>VIF</td><td>1.1165</td><td>1.1058</td><td>1.1395</td><td>1.1061</td><td>1.1822</td><td>1.1207</td></tr><tr><td>Teams - Ln</td><td></td><td></td><td>0.2766</td><td>0.2795</td><td></td><td></td></tr><tr><td>Prob &gt; |t|</td><td></td><td></td><td>&lt; 0.0001</td><td>0.0009</td><td></td><td></td></tr><tr><td>VIF</td><td></td><td></td><td>1.4937</td><td>2.0369</td><td></td><td></td></tr><tr><td>Entries</td><td></td><td></td><td></td><td></td><td>0.1965</td><td>0.1624</td></tr><tr><td>Prob &gt; |t|</td><td></td><td></td><td></td><td></td><td>&lt; 0.0001</td><td>0.0098</td></tr><tr><td>VIF</td><td></td><td></td><td></td><td></td><td>1.5422</td><td>1.9249</td></tr></table>

## 7.6. Hypothesis 3 – estimation of posts (Tables 7 and 8).

The research used two diferent approaches to model the number of

Estimation of the number of posts using entire sample (Hypothesis 3).

<table><tr><td colspan="5">Original N = 98 data points - estimating posts</td></tr><tr><td>Model</td><td>Post-1</td><td>Post-2</td><td>Post-3</td><td>Post-4</td></tr><tr><td>R Square</td><td>0.8822</td><td>0.9104</td><td>0.9071</td><td>0.9022</td></tr><tr><td>Reward-Ln</td><td>-0.0464</td><td>-0.0494</td><td>-0.0512</td><td>-0.0515</td></tr><tr><td>Prob &gt; |t|</td><td>0.0994</td><td>0.0465</td><td>0.0426</td><td>0.0469</td></tr><tr><td>VIF</td><td>1.694</td><td>1.6948</td><td>1.6965</td><td>1.6975</td></tr><tr><td>Topics-Ln</td><td>1.3725</td><td>1.1391</td><td>1.1379</td><td>1.1937</td></tr><tr><td>Prob &gt; |t|</td><td>&lt; 0.0001*</td><td>&lt; 0.0001*</td><td>&lt; 0.0001*</td><td>&lt; 0.0001*</td></tr><tr><td>VIF</td><td>1.694</td><td>2.6948</td><td>2.8388</td><td>2.519</td></tr><tr><td>Teams-Ln</td><td></td><td>0.2083</td><td></td><td></td></tr><tr><td>Prob &gt; |t|</td><td></td><td>&lt; 0.0001*</td><td></td><td></td></tr><tr><td>VIF</td><td></td><td>2.0388</td><td></td><td></td></tr><tr><td>Players - Ln</td><td></td><td></td><td>0.205</td><td></td></tr><tr><td>Prob &gt; |t|</td><td></td><td></td><td>&lt; 0.0001*</td><td></td></tr><tr><td>VIF</td><td></td><td></td><td>2.2161</td><td></td></tr><tr><td>Entries - Ln</td><td></td><td></td><td></td><td>0.1355</td></tr><tr><td>Prob &gt; |t|</td><td></td><td></td><td></td><td>&lt; 0.0001*</td></tr><tr><td>VIF</td><td></td><td></td><td></td><td>1.897</td></tr></table>

Table 8  
Propensity match sample estimation of number of posts (Hypothesis 3).

<table><tr><td colspan="5">Matched sample N = 54 - estimating posts</td></tr><tr><td>Model</td><td>Reward</td><td>Teams</td><td>Players</td><td>Entries</td></tr><tr><td>R Square</td><td>0.8783</td><td>0.9133</td><td>0.9098</td><td>0.9030</td></tr><tr><td>Reward-Ln</td><td>0.0010</td><td>0.0011</td><td>0.0034</td><td>0.0017</td></tr><tr><td>Prob &gt; |t|</td><td>0.9772</td><td>0.9695</td><td>0.9090</td><td>0.9571</td></tr><tr><td>VIF</td><td>1.2889</td><td>1.2889</td><td>1.2894</td><td>1.2889</td></tr><tr><td>Topics-Ln</td><td>1.2931</td><td>1.0391</td><td>1.039</td><td>1.104</td></tr><tr><td>Prob &gt; |t|</td><td>&lt; 0.0001*</td><td>&lt; 0.0001*</td><td>&lt; 0.0001*</td><td>&lt; 0.0001*</td></tr><tr><td>VIF</td><td>1.2889</td><td>2.2579</td><td>2.3646</td><td>2.0499</td></tr><tr><td>Teams-Ln</td><td></td><td>0.2284</td><td></td><td></td></tr><tr><td>Prob &gt; |t|</td><td></td><td>&lt; 0.0001*</td><td></td><td></td></tr><tr><td>VIF</td><td></td><td>1.9679</td><td></td><td></td></tr><tr><td>Players - Ln</td><td></td><td></td><td>0.2223</td><td></td></tr><tr><td>Prob &gt; |t|</td><td></td><td></td><td>0.0001</td><td></td></tr><tr><td>VIF</td><td></td><td></td><td>2.3646</td><td></td></tr><tr><td>Entries - Ln</td><td></td><td></td><td></td><td>0.1366</td></tr><tr><td>Prob &gt; |t|</td><td></td><td></td><td></td><td>0.0008</td></tr><tr><td>VIF</td><td></td><td></td><td></td><td>1.7552</td></tr></table>

Posts. Because sequentially Topics are related to Posts, the initial mode used Topics as the base and analyzed Reward, the participation variables (Team and Players) and efort (Entries) to estimate Posts. The concern was with understanding “what is the additional contribution of those other variables, over and above the number of Topics?” That approach was used on both the original and the matched data generating diferential results. The second model, developed as part of the mediation analysis, was based on using the independent variables of Reward. Users and Length to estimate the number of Posts.

The estimation of the number of posts for Hypothesis 3 is summarized in Tables 7 and 8. For this hypothesis, we were primarily concerned as to the sign of the regression coeficient on Reward. Unlike the results for Hypotheses 1 and 2, the two diferent samples provide significantly diferent results and a diferent view of the relationship between the reward and the number of posts. Analysis of the original sample of 98 contests results in a negative coeficient on reward (Table 7), while analysis of the propensity-matched contests finds no statistically significant relationship (Table 8). However, in the next subsection we perform mediation analysis of the matched sample data. We find that underlying the matching data Topics is a mediator variable and that allows us to find that the number of Posts is positively related to the Reward.

## 7.7. Mediation findings in matched sample (Fig. 3 and Table 9)

Additional analysis of the propensity matched data indicates that reward is mediated by the number of topics (Fig. 4). As seen in Table 9, when estimating Posts, Reward has a positive and statistically significant coeficient on reward. Similarly, when estimating Topics, Re ward has a positive and statistically significant coeficient. However, as seen in Table 8 when both Topics and Reward are in the same equation estimating Posts, Reward is not statistically significant. Accordingly, as noted above this indicates that Topics is a mediating variable for Reward. Using a similar analysis we also find that Length also is mediated by Topics. As a result, the number of Posts (answers) is predicated upon both the Length of the contest and the Reward.

Table 9  
Reward mediation analysis (See Fig. 3).

<table><tr><td colspan="3">Matched sample N = 54</td></tr><tr><td>Model</td><td>Topics</td><td>Posts</td></tr><tr><td>Fig. 1 Equation</td><td>Second</td><td>First</td></tr><tr><td>R Square</td><td>0.2241</td><td>0.1979</td></tr><tr><td>Reward-Ln</td><td>0.2158</td><td>0.2801</td></tr><tr><td>Prob &gt; |t|</td><td>0.0003</td><td>0.0007</td></tr></table>

![](/api/attachments/4XE3SVF5/fulltext/images/e97c523132c76268629a1db0c976b14e11a682aa6bb37f72a2a59a3dc8fa25fe.jpg)  
Fig. 4. Single mediator model (based on [34,35]).

Table 10  
Estimation of posts using independent variables (Hypothesis 4).

<table><tr><td>Model</td><td>N = 98</td><td>N = 54</td></tr><tr><td>R Square</td><td>0.4316</td><td>0.5446</td></tr><tr><td>Reward-Ln</td><td>0.2281</td><td>0.2529</td></tr><tr><td>Prob &gt; |t|</td><td>&lt; 0.0001</td><td>0.0001</td></tr><tr><td>VIF</td><td>1.2768</td><td>1.0441</td></tr><tr><td>Users-Ln</td><td>0.4331</td><td>0.9336</td></tr><tr><td>Prob &gt; |t|</td><td>0.0001</td><td>&lt; 0.0001</td></tr><tr><td>VIF</td><td>1.1533</td><td>1.0606</td></tr><tr><td>Length-Ln</td><td>0.4176</td><td>0.394</td></tr><tr><td>Prob &gt; |t|</td><td>0.0296</td><td>0.0893</td></tr><tr><td>VIF</td><td>1.1165</td><td>1.1057</td></tr></table>

## 7.8. Estimation of posts using independent variables

A summary of the estimation of the number of Posts is in Table 10. As seen in that table, the coeficients on each of the three variables are positive and either statistically significant or marginally statistically significant. Although each of the coeficients is < 1, the coeficient on Users in the matched sample is close to 1 and as a result, close to an increasing returns to scale.

## 8. Discussion and implications for practice

The purpose of this section is to summarize and discuss some of the implications of these findings for crowdsourcing data analytic contests, with particular interest in such crowdsourcing eforts that use social media. Companies using crowdsourcing contests have multiple “levers” that they can use to design the contests. Those variables include providing a reward, getting potential participants to register, establishing the length of the contest and encouraging the use of social media, say through the choice of platform, in order to increase the number of potential participants (perhaps through publicity of the specific contest). The variables have three “indicators” that would help understand how to actually use these results: the interpretation of the coeficients (increasing or diminishing returns), positive or negative coeficients and whether or not the results are statistically significant.

## 8.1. Reward (contest designer)

Our analysis suggests a positive and statistically significant relationship with Reward in each of the uses investigated. However, we did find that although the Reward is important, apparently there are diminishing returns associated with Reward increases. In particular, a roughly 1% increase in reward will increase entity participation and efort by only roughly 0.20% - 0.28%. Further, the coeficient on

Reward ranged from roughly 0.12% to 0.20% when related to the number of Topics, but ranged from 0.11% to 0.29% when related to the number of Posts. As a result, when designing a crowdsourcing efort that involves a Reward, companies would expect the level of the Reward to impact the number of participants, their efort and their social media activity. However, Reward generally has the lowest impact of any of the independent variables, based on the regression coeficients.

## 8.2. Length of the contest (contest designer)

Length of the contest was positive and statistically significant in each of the models estimating the number of Topics (Table 6). Similarly, length of the contest was positively related to the number of participants and their efort as seen in Table 5, but only statistically significant in one of those models. The coeficients in those models were < 1 suggesting diminishing returns. It is a variable that is mediated away by Topics in the analysis of Posts, however it also has a positive coeficient. Accordingly, length of contest appears to play a role in facilitating information flow using social media however, it should be regarded as part of a portfolio of activities in designing crowdsourcing contests.

## 8.3. Potential set of participants (contest designer/platform designer)

The number of potential users is the one independent variable that apparently can provide increasing returns to scale, based on the coefficients seen in Table 5 for the matched sample. Not only was each of the results in that table positive and statistically significant, but the coeficients for Users in the matched sample are > 1. This suggests that organizers would gain disproportionately if they could get potential participants to sign-up and download and analyze databases. Actions that facilitate that approach could include providing information about the contests or potentially providing educational opportunities to broaden the set of participants. In addition, this variable, likely characterizes capabilities of the Kaggle platform. This variable is critical to comparing Kaggle to any other potential source for competitions and a key variable for the platform designer to evaluate their platform.

## 8.4. Social media (topics and posts) (platform designer)

Crowdsourcing is built around social media and open information and provides the ability to share information. It provides an open environment for information search and discussion. For example, participants can post questions and provide answers to those questions. When estimating the number of Topics (Questions asked) each of the independent variables of Reward, Users and Length of the crowdsourcing activity were found to be statistically significant and positive (Table 6) and similarly when estimating the number of Posts (Table 9). However, there were diminishing returns on each of the independent variable coeficients when estimating Topics or Posts. As a result, it can be important for crowdsourcers to “spread” their eforts across the multiple dimensions available to them. Interestingly, and particularly important, the number of Topics has a coeficient > 1 when estimating the number of Posts indicating increasing returns to scale. As a result, eforts to grow generation of Topics will have a positive relationship with the number of posts.

## 8.5. Impact of mediation of reward

Before accounting for mediation, it appeared that reward had either a negative (Table 7) or no impact on the number of posts (Table 8). However, as discussed above reward is a mediated by topics, thus that means that reward, which is ultimately controlled by the contest designer, is a key variable in generating communication. As seen in Table 10, a 1% increase in the reward will generate between roughly a

0.23% to a 0.25% increase in the number of posts, roughly consistent with the percent increase in the participation and efort (Table 5). Reward continues to have an impact throughout the contest variables, however, the impact is not linear. For the platform designer this illustrates that the structure of information search and information sharing captured by the platform, appears to foster a community efort, rather than one driven by self-interest, as measured by a positive coeficient on reward.

## 8.6. Information search and information sharing

There is some tension with information search in this contests. In contrast to classic information search, social media information search communications in the topics are “seen” by other participants, because of the social media structure in Kaggle – there is no information asymmetry. As a result, when one team lists a topic, other participants can gain information insight into potential problem solutions through analysis of the topics. The questions become information disclosures. Thus, a Topic can remove some information asymmetries between the person listing the topic and the other players. Accordingly, in a contest there is a rationale for not seeking information through topics, unless there is no other alternative because social media communication signal questions, concerns and involvement.

Our results between reward and information search and sharing are not consistent with the self-interest theory. Constant et al. [29], preceding the development of social media, found that a belief in the ownership of information overcomes the influence of self-interest. There are at least two perspectives consistent with that finding and the results here. First, the use of Topics to ask questions could provide a degree of ownership by the Topic asker, so that asking the question could stake out quasi-ownership of the information. Second, alternatively, the result would be consistent with a “community” perspective on social media, where questions raised in a public forum and answers to those questions, belong broadly to the overall community.

## 9. Summary, extensions and contributions

This paper has investigated data gathered from crowdsourcing analytic competitions as part of an empirical analysis of participant information search and information sharing behavior using social media. Analysis of that data found the Reward and the number of en tities and amount of efort are related to each other using an exponential/logarithm model, suggesting diminishing returns. In addition, analysis of that data found that the extent of use of social media “Topics” was positively related to the Reward, the potential pool of participants, the Length of the contest, the number of Teams (and Players) and the efort (Entries). Finally, in our primary concern, we found that the number of “Topics” is a mediating variable for the number of “Posts” and that the number of Posts was positively related to “Reward” and “Length of the Contest.”

## 9.1. Extensions

There are a number of potential extensions of this research. First, this research focused on crowdsourcing data analytic contests. As a result, future research could investigate information sharing and the use of social media while crowdsourcing other types of problems beyond data analytics, and compare the findings. The analysis of data analytics contests provides a benchmark that can serve as a basis of comparison to other settings and organizations.<sup>13</sup> Second, this research has examined Kaggle competitions using aggregated usage data. However, potentially behavioral research could be done to explore “internal” motivations for individual behavior in social media and in contests with a real reward. Third, “information sharing” seems to be a relatively under-developed area, particularly in the area of crowdsourcing. This paper proposed that questions and answers in public forums become “owned” by the community or the question asker/answerer. Fourth, the analysis data suggests some changes in the data captured. For example, it would be helpful to make date information about the posts and topics be available so that such information could be studied over time.<sup>14</sup>

## 9.2. Contributions

This paper investigates the use of social media in contests and to crowdsourcing. This paper provides methodological and real world contributions. First, this paper introduces the exponential/logarithm relationship into contest theory between entity participation (number of Teams and Players) and the reward, and the efort (Entries) and the reward. That model suggests that there are diminishing returns associated with reward increases. In particular, in this setting, a roughly 1% increase in reward will increase crowdsourcing participation and efort by only roughly 0.21%–0.27% (Table 5). However, there were increasing returns to scale for number of Topics relative to the number of Posts. Second, using factor analysis, this paper finds that empirically the number of participants (teams and players) and the efort measures (e.g., number of entries) are highly correlated and efectively provide a single factor. Although these variables are distinct in contest theory, empirically they are closely related in this setting. Third, this paper expands classic contest theory to include the efects of potential number of participants, the extent of time that the contest is open and using social media for information search and sharing. Fourth, this paper introduced the potential use of contest theory into the analysis of crowdsourcing and information system platforms, such as Kaggle. Fifth, and most importantly, this paper provides an empirical analysis of participant social media use that finds the numbers of Topics and Posts are positively dependent on the Reward, the user base and the length of the contest, and the number of Topics is a mediating variable. Finally, this paper uses its results to provide contest developers guidance in their design and use of contests in such crowdsourcing as a service settings.

## References

[1] J. Surowiecki, The Wisdom of Crowds, Random House, New York, United States of America, 2004 (2004).

[2] K. Eisenhardt, Agency theory: an assessment and review, Academy of Management 14 (1) (1989) 57–74.

[3] J.E. Stiglitz, The contributions of the economics of information to twentieth century economics, The Ouarterly Journal of Economics 115 (4) (2000) 1441–1478.

[4] Mark Pagel, Wired for Culture: The Natural History of Human Cooperation, Penguin UK. 2012.

[5] J. Howe, The Rise of Crowdsourcing, Wired, 2006. http://archive.wired.com/ wired/archive/14.06/crowds.html.

[6] A. Tripathi, N. Tahmasbi, D. Khazanchi, L. Najjar, Crowdsourcing typology: a review of IS research and organizations, Midwest AIS Proceedings, 2014 http://aisel. aisnet.org/cgi/viewcontent.cgi?article=1018&context=mwais2014.

[7] J. Howe, Crowdsourcing, why the Power of the Crowd Is Driving the Future of Business, Crown, New York, 2008

[8] H. Gao, G. Babier, R. Goolsby, Harnessing the crowdsourcing power of social media, IEEE Intelligent Systems 26 (3) (2011) 10–14.

[9] E Havek, The use of knowledge in society, The American Fconomic Review 35 (4 (1945) 519–530

[10] O. Nov, O. Arazy, D. Anderson, Crowdsourcing for science: understanding and enhancing scisourcing contributions, ACM CSCW 2010 Workshop on the Changing Dynamics of Scientific Collaborations. 2010 http://faculty poly.edu/\~onoy/Noy %20Arazy%20Anderson%20CSCW%202010%20workshop.pdf.

[11] D. Dahl, “How Kaggle uses the crowd to solve your big data problems,” Wired February 24, 2014. http://www.inc.com/magazine201403/darren-dahl/big-data crowdsourcing-kaggle.html.

[12] K. Konrad, Strategy and Dynamics in Contests, Oxford University Press, New York, 2009.

[13] E. Dechaneaux, D. Kovenkoch, R. Sheremeta, A survey of research on contests, all pay auctions and tournaments, Experimental Economics 18 (4) (2014) 1–61.

[14] N. Netzer, C. Wiermann, Signaling in Research Contests, August 31, 2005. ftp:// 193.196.11.222/pub/zew-docs/veranstaltungen/Papers/Netzer\_Wiermann.pdf.

[15] S. Szymanski, Competitive Balance and Income Redistribution in Team Sports, Royal Economic Society, University of Warwick, 2001 available at: http://www. warwick.ac.uk/res2002/papers/Szymanski.pdf

[16] S.O. Parreiras, A tortoise and a hare race, 2013 Conference on Tournaments, Contests and Relative Performance Evaluation, 2013, January.

[17] N. Archak, A. Sundararajan, Optimal design of crowdsourcing contests, Proceedings of the 2009 International Conference on Information Systems, 2009.

[18] B. Shao, L. Shi, B. Xu, L. Liu, Factors afecting participation of solvers in crowdsourcing: an empirical study from China. Electronic Markets 22 (2) (2012) 73–82

[19] Y. Huang, P. Singh, T. Mukhopadhyay, “How to Design Crowdsourcing Contest: A Structural Empirical Analysis,” Workshop of Information Systems and Economics, http://www.krannert.purdue.edu/faculty/kkarthik/wise12/papers%5Cwise12\_ submission\_149.pdf, (2012).

[20] R. Araujo, 99designs: an analysis of creative competition in crowdsourced design, Proceedings of the First AAAI Conference on Human Computation and Crowdsourcing, 2013, 2013, pp. 17–24.

[21] R. Hofstetter, J.Z. Zhang, A. Herrmann, Successive open innovation contests and incentives: winner-take-all or multiple prizes? Journal of Product Innovation Management 35 (4) (2017) 492–517

[22] A.M. Chaudhari, Crowdsourcing for Engineering Design: Theoretical and Experimental Studies. (2017).

[23] J. Bian, Y. Liu, E. Agichtein, H. Zha, Finding the right facts in the crowd: factoid question answering over social media, Proceedings of the 17th conference on World Wide Web, ACM, 2008, April, pp. 467–476.

[24] R. Nitsche, N. Hinten-Reed, Competitive Impacts of Information Exchange, Charles River Associates, June, 2004https://www.e-ca.com/sites/default/files/note\_on\_ information\_exchange\_en.pdf.

[25] W. Li, W.T. Tsai, W. Wu, Crowdsourcing for large-scale software development, Crowdsourcing, Springer, Berlin, Heidelberg, 2015, pp. 3–23.

[26] L. Corchon, The theory of contests: a survey, Review of Economic Design, 11:2 Springer – Verlagg, 2007.

[27] C.C. Kuhlthau, Inside the search process: information seeking from the user's perspective, Journal of the American Society for Information Science 42 (5) (1991) 361–371.

[28] M. Efron, Information search and retrieval in microblogs, Journal of the American Society for Information Science and Technology 62 (6) (2011) 996–1008.

[29] D. Constant, S. Kiesler, L. Sproull, What's mine is ours or is it? A study of attitudes about information sharing, Information Systems Research 5 (4) (1994) 400–421.

[30] A. Montgomery, Reflecting Uncertainty about Economic Theory when Estimating Consumer Demand, (2002), pp. 257–294 (in Franses and Mongomery [36]).

[31] Y. Pan, R.T. Jackson, Ethnic diference in the relationship between acute inflammation and serum ferritin in US adult males, Epidemiology and Infection 136 (03) (2008) 421–431.

[32] J. Reiter, Using statistics to determine causal relationships, American Mathematical Monthly 107 (1) (2000).

[33] P.R. Rosenbaum, D.B. Rubin, Constructing a control group using multivariate matched sampling methods that incorporate the propensity score, The American Statistician 39 (1) (1985) 33–38.

[34] D. MacKinnon, Modern Mediation Analysis, (2014).

[35] R. Baron, D. Kenny, The moderator – mediator variable distinction in social psychological research, Journal of Personality and Social Psychology 51 (6) (1986) 1173-1182.

[36] P. Franses, A. Montgomery, Econometric Models in Marketing, Elsevier, Kidlington, Oxford, England, 2002.

Daniel O'Leary is a Professor in the Marshall School of Business at the University of Southern California, focusing on prediction markets, crowdsourcing, innovations and social media. Dan received his Ph. D. from Case Western Reserve University. He is the former editor of IEEE Intelligent Systems and current editor of John Wiley's Intelligent Systems in Accounting, Finance and Management. His book, Enterprise Resource Planning Systems, published by Cambridge University Press, has been translated into both Chinese and Russian. Much of Professor O’Leary's research has studied emerging tech nologies and their use in business settings.
