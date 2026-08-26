---
otero_id: 21752
otero_key: "DN68DEM2"
title: "Experimentation with an information filtering system that combines cognitive and sociological filtering integrated with user stereotypes"
authors: "Bracha Shapira; Peretz Shoval; Uri Hanani"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00034-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Experimentation with an information filtering system that combines cognitive and sociological filtering integrated with user stereotypes

Bracha Shapira, Peretz Shoval <sup>)</sup>, Uri Hanani

Information Systems Engineering Program, Faculty of Engineering Sciences, Department of Industrial Engineering and Management, Ben-Gurion UniÕersity of the NegeÕ, Beersheba 84105, Israel

## Abstract

A dual-method model and system for filtering and ranking relevance of information is presented. One method is cognitive filtering, while the other is sociological filtering, which is integrated with user stereotypes. A prototype system was developed to test the applicability of the model for filtering e-mail messages, and experiments were run to determine the effects of combining the two methods in various filtering strategies. Results reveal that although cognitive filtering alone is usually more effective than sociological filtering alone, the combination of both methods yield better results than using each method individually. Ordinarily, the best filtering strategies are achieved when the two methods are used in parallel, or when cognitive filtering is the primary method, followed by sociological filtering. We conclude that the optimal filtering strategy of combining cognitive and sociological filtering is stereotype dependent; i.e., for each user stereotype, there may be a specific combination of the cognitive and sociological filtering that yields best results. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Information filtering; Information retrieval; Filtering systems; Cognitive filtering; Sociological filtering; Collaborative filtering; Content-based filtering; Cluster analysis; User stereotypes; User profiles; Experimentation; Relevance ranking; Indexing

## 1. Introduction

Information filtering is aimed at helping users cope with large amounts of information. Some filtering systems screen out irrelevant incoming information data items, e.g., documents, e-mail messages, Ž etc. , while other systems rank incoming data items . for their relevancy 3,12 . Information filtering dif-<sup>w</sup> <sup>x</sup> fers from traditional information retrieval, in that their users have long term interests informationŽ needs that are described by means of user profiles,. rather than ad-hoc needs that are expressed as queries posed to some information retrieval system.

There exist two main filtering approaches 13,16 :<sup>w</sup> <sup>x</sup> Ž .a cognitiÕe filtering, also referred to as contentbased, and bŽ . sociological filtering, also referred to as collaborative. The two approaches differ in the methods used for constructing user profiles and the techniques used to calculate relevance of incoming data items. In cognitive filtering, the user profile and the filtering technique are based solely on the content of information. The user’s profile consists of a representation of his<sup>r</sup>her areas of interest, and the filtering process is aimed at finding out to what extent the content of a candidate data item is relevant. User feedback given to the system’s relevance ranking of data items is used to update the user profile. Most commercial filtering systems employ cognitive filtering, since the method is relatively easy to implement, and produces reasonable, even if not satisfactory, filtering results 15 .

Sociological filtering was defined as ‘‘filtering that works by supporting the personal and organizational interrelationships of individuals in a community’’ 13 . Most sociological filtering systems e.g., <sup>w</sup> <sup>x</sup> Ž Refs. 2,22 interpret the definition as a collabora- <sup>w</sup> <sup>x</sup>. tive process that bases the filtering on ‘‘similar’’ users. For a given user, a group of users is found whose feedback, recommendations, or cognitive profile is most similar to his. The filtering consists of calculation of data items’ ranks, as based on comparison of the user profile or the evaluated data items, to corresponding parameters of the ‘‘similar users’’. The sociological element involved in those systems is the inclusion of other users in the process. However, the similarity of users in most systems is content-based since it is calculated on the basis of similarity of their cognitive profiles or on feedback.

Our model offers a different interpretation of sociological filtering, especially to the modeling of users in sociological filtering systems. It is based on the assumption that a user model has to include all available knowledge about the user that is relevant to the application 1 ; i.e., all knowledge about the user that might be relevant to the filtering should be included in his model. We claim that sociological parameters such as user education, occupation, knowledge, experience etc., as well as preferences and habits in consuming information, are very relevant to the filtering task. For example, a researcher and a programmer may have the same area of interest, e.g., object-oriented programming, but owing to their affiliation, education and occupation, different data items may be relevant to them. A programmer may be interested in data items that deal with new versions of software, technical communicates, etc., while a researcher may be interested in new research papers, textbooks, conference announcements, etc. To cope with such differences, the user profile in our model includes sociological parameters in addition to areas of interest.

In addition to the above, we assume that users who share sociological parameters might also have common preferences and habits with respect to their information needs. This can be achieved by the formation of user stereotypes. In other words, stereotypes may be used to infer default information about users who ‘‘belong’’ to them. Stereotypes are very broadly used in user-modeling research, and are integrated in many user-modeling applications <sup>w</sup> <sup>x</sup> 10,18 . Stereotypes are best used to infer default beliefs about users until more accurate information is obtained. They may also serve as a shortcut for a user-model by inferring knowledge about users from their stereotypic belonging.

Here are a few examples of systems that apply stereotypes for user modeling. Rich 17,18 tested<sup>w</sup> <sup>x</sup> and proved the effectiveness of stereotypes empirically in the GRUNDING system, which applies stereotypic inference for suggesting books to readers in a library. GUMS 7 is a system that builds user<sup>w</sup> <sup>x</sup> models for interactive expert systems in various fields. It distinguishes between definite and default parts of stereotypes: definite parts must apply to all the users in the stereotypes, and default parts do not necessarily apply to all users. UM-tool 4 is an<sup>w</sup> <sup>x</sup> expert system designed to find a suitable method of interaction between a user and a computer, for the purpose of searching for information in the field of computer science. The interaction includes a choice of bibliographic approaches, search tactics, and professional terms. The system chooses the form of interaction that is most suited to a user according to the stereotypes to which he belongs; building a user model is essentially a matter of finding to which stereotypes he belongs. KNOME 5 is a system that<sup>w</sup> <sup>x</sup> models users in a support system for users of UNIX. The user model represents what the system ‘believes’ the user knows about UNIX. Each user is assigned to one of four user stereotypes: novice, beginner, intermediate and expert. The information about UNIX that different users need to see is also divided into four levels of difficulty, matching those stereotypes. More examples of systems that utilize Ž stereotypes are surveyed in Ref. 21 . In spite of<sup>w</sup> <sup>x</sup> . their potential in the modeling of filtering systems, there exist only very few filtering systems that use stereotypes. For example, Ref. 10 uses stereotypes <sup>w</sup> <sup>x</sup> to increase the efficiency of a filtering system by a pre-filter phase that locates the right server for a user. The pre-filter phase is performed on a stereotypic basis rather than for individual users.

In our model, stereotypes are used in sociological filtering to infer user preferences and habits as to their information needs, from their stereotypic belonging. Users are related to stereotype according to their sociological parameters. Our model combines cognitive and sociological filtering. As shown in Refs. 2,8 , combinations of different methods yield <sup>w</sup> <sup>x</sup> better filtering results than the use of a single filtering method. We offer a new method of sociological profiling and filtering, as well as various combinations of cognitive and sociological filtering strategies. The user’s profile in our model includes sociological parameters, in addition to his<sup>r</sup>her areas of interest, and is used to relate the user to a known stereotype. Each stereotype is characterized by a set of regularities and habits of using or filtering information — expressed in a form of rules — that are assumed to be common to the users who ‘‘belong’’ to the stereotype. In sociological filtering, the rules that characterize a user’s stereotype are applied, to predict the relevance of data items.

The model presented here is a ranking filtering model; i.e., irrelevant data items are not filtered out, but are ranked for their relevancy to the user. The rationale is that users fear the loss of information and prefer to have the option of reviewing any data item. ŽThis attitude may change when filtering systems become more reliable..

A prototype system that implements this model was developed, to examine its applicability as well as its effectiveness. The model and the system that implements it are overviewed in Section 2. Section 3 describes how we implement sociological filtering. Section 4 describes experiments conducted to test the model with various filtering strategies, and Section 5 analyses the results of the experiments. Section 6 provides conclusions and discusses further research.

## 2. The model and the prototype system

## 2.1. General description of the model

The filtering model is described in greater detail in Ref. 20 ; here, we provide a brief overview only.<sup>w</sup> <sup>x</sup> Fig. 1 is a data flow diagram of the model.

The model contains four databases.

D1: Raw database — Contains the raw incoming data items to be filtered.

D2: Represented data items — Each data item is represented as a weighted-vector of terms Ž . keywords . The values of the vector entries represent the degree of relevance of the terms to the data items. The terms are weighted according to Salton’s method used in SMART system 19 .<sup>w</sup> <sup>x</sup>

D3: User profiles — Contains two types of profiles for each user: 1 A cognitive profile: includesŽ . the user’s areas of interest, presented as a weightedvector of terms keyword . Each entry in the vectorŽ . represents a term, and the user provided weight represents the degree of the user’s interest in the term, in a 0–100 scale. 2 A sociological profile:Ž . includes sociological parameters of the user, such as his<sup>r</sup>her education, occupation, age, experience, etc.

D4: Stereotype data and rules: contains descriptions of known user stereotypes. Each stereotype is represented by a set of sociological parameters that are common to users who ‘‘belong’’ to the stereotype, and by a set of information filtering rules that are typical to the stereotype. The rules prescribe customary ways in which users that belong to a certain stereotype use or filter information. The rules refer to parameters in a data item. For example, for an e-mail message, parameters may include its goal Ž . purpose , quality of source and length. A rule specifies the relevancy of a data item to a user who belongs to the stereotype, with respect to a certain parameter. It has the following format.

If param Ž² : ² :. Ž <sup>s</sup> val\_of\_param then rank <sup>¤</sup> ² :. value , where:

<sup>Ø</sup> ² : param is a parameter of the data item, such as its goal or length;

<sup>Ø</sup> ² : val\_of\_param is a value from a set of possible values of the parameter;

<sup>Ø</sup> ² : value is a 1–7 number that signifies, for each stereotype, the degree of relevance of a data item to the corresponding val² : \_of\_param .

Here is an example: the rule If goal Ž <sup>s</sup> ‘conference’ then rank. 5.9 determines that, for a certain stereotype, messages announcing conferences are of high relevance.

The model contains three main processes.

F1: Representation process — Converts raw data items to a vector of weighted-terms.

![](/api/attachments/DN68DEM2/fulltext/images/c2deff9448c24ff5556be2f6c4ebd8071ef24bc17e6d09c3dfd0c7529b8059bd.jpg)  
Fig. 1. Data flow diagram of the filtering model.

F2: Filtering process — The main process of the model; it calculates the relevance rank of each data item. As said, the filtering process incorporates two main methods.

<sup>Ø</sup> Cognitive filtering, where a data item is examined for relevancy to the user on the basis of his<sup>r</sup>her areas of interest. This is accomplished by calculating the statistical correlation between the vector of terms that represent the user interests and the vector of terms that represent the data item.

<sup>Ø</sup> Sociological filtering, where the relevance of a data item is calculated by applying certain filtering rules of the user’s stereotype. The user’s stereotype is determined according to the similarity of his<sup>r</sup>her sociological profile to the sociological parameters of the existing stereotypes.

Each filtering method produces a relevance rank for a data item that is being examined. The overall rank of a data item is calculated as some combination of the two ranks. One of our goals is to find appropriate combinations of both filtering methods that yield best relevance ranks for different user stereotypes.

F3: Learning process — Based on feedback from the filtering process, this process may update the user’s profile, his<sup>r</sup>her stereotype’s rules, and even re-assign the user to a different stereotype. This Ž paper will not elaborate on the learning process..

## 2.2. Combinations of filtering methods

We offer two basic combinations of the filtering methods: consecutiÕe and parallel.

<sup>Ø</sup> In the consecutiÕe combination, one of the filtering methods is considered ‘‘primary’’, i.e., more important. Thus, a data item is first filtered by the primary method, and only if its resulting rank is above a certain relevance threshold, the second filtering method is applied, providing a second relevance rank. The relevance threshold reflects a desiredŽ emphasis on the primary filtering method. In a realworking system, its initial value can be set according to some desired emphasis on the primary method, and later on be fine-tuned by a learning process, according to user feedback. For our prototype system and experiments, we have determined the threshold by trial-and-error, as will be detailed in Section 4.. Hence, the overall relevance rank of the data item is a weighted-average of the two ranks, with more weight given to the primary method. If the relevance rank of the primary method is below the relevance threshold, this rank is considered as the overall rank of that data item. The consecutive combination seems to be suitable for situations i.e., user stereotypes Ž . where one of the filtering methods cognitive orŽ sociological is assumed to be more important or . effective, while the other filtering method provides ‘‘fine tuning’’ to determine the overall degree of relevance of the data item.

<sup>Ø</sup> In the parallel combination, each of the filtering methods is applied on every data item, providing its relevance rank. The overall rank of a data item is the average of the two ranks. This combination seems to be suitable for situations where none of the two filtering methods is assumed to be more important or effective than the other.

As already stated, one objective of the experiments is to examine the different filtering approaches and find out optimal strategies for different user stereotypes.

## 2.3. The prototype system

We have implemented the filtering model in a prototype system. The system is designed to run in batch mode, so as to enable experimentation, i.e., evaluation and ranking of data items using different filtering strategies. For the purpose of this research, the system was implemented to accept as input Ž . files that contain e-mail messages. These files are initially created by separate software that serves as a front-end interface to various e-mail systems: users who obtain e-mail messages from various sources Ž . list servers utilize that software to evaluate and rank the relevancy of their incoming messages on a 1–7 scale. The user-evaluated messages are saved to a special file. At the experimentation stage, the system reads the messages from that file and predicts the relevancy of each message several times, each time according to a different filtering strategy that is being examined as will be detailed in following Ž sections ..

![](/api/attachments/DN68DEM2/fulltext/images/ad2d18ebb3c2ddead02136755d79c01d5d067e2db2468266d9a45063bd093988.jpg)  
Fig. 2. Filtering module of the prototype system.

The main component of the prototype system is a filtering module that implements the two filtering methods in various ways. The filtering module utilizes two main engines: cognitiÕe engine, which implements cognitive filtering, and sociological engine, which implements sociological filtering. Fig. 2 graphically shows the structure of the filtering module.

The interface screen of the prototype system enables the experimenter to enter or select the following parameters:

<sup>Ø</sup> The user id or name whose e-mail messages file is to be evaluated at the current run i.e., experi- Ž ment ..

<sup>Ø</sup> The filtering strategy to be used. The following options are available:

\- Cognitive filtering only.

\- Sociological filtering only.

\- Parallel combination both cognitive and soci-Ž ological filtering ..

\- Consecutive combinations, with either filtering method as the ‘‘primary’’, i.e., cognitive followed by sociological, or sociological followed by cognitive. For each of these combinations we enable two different weightings of the primary and secondary method, namely 60%:40% and 70%:30%.

\- Random generation of evaluations, as a test case for any filtering method i.e., to see if anyŽ of the filtering methods yield better evaluations than random ..

## 3. Sociological filtering: formation of stereotypes, rules and parameters

In order to implement the model and perform experiments, we have to create user profiles both Ž cognitive and sociological , form user stereotypes,. and for each stereotype, define appropriate filtering rules and sociological parameters to represent it. The implementation process included the following activities: 1 user interviews; 2 formation of userŽ . Ž . stereotypes; 3 definition of the stereotypes’ rules; Ž . and 4 definition of the stereotypes’ representative Ž . sociological parameters.

## 3.1. User interÕiews

We need to interview information users i.e., re-Ž cipients of information filtering services in a certain. domain, in order to identify their sociological parameters and information filtering rules. The environment domains for our implementation and the following experiments are information technology departments at universities. The information users are academic researchers faculty , information spe- Ž . cialists, graduate students, and technical staff e.g.,Ž computer network managers, computer technician .. We have interviewed 40 e-mail users i.e., users whoŽ subscribe to several list-servers each from the exper-. iment domain. The interviews were based on a questionnaire consisting of two main parts.

Table 1  
Sociological parameters and their numerical decoding

<table><tr><td>Parameter</td><td>Possible values (and their numerical decoding)</td></tr><tr><td>Education</td><td>PhD (1), MSc (2), engineer (3), BSc (4), technician (5)</td></tr><tr><td>Occupation</td><td>Researcher (1), information specialist (2), computer professional (3), student (4)</td></tr><tr><td>Level</td><td>Junior (1), intermediate (2), senior (3)</td></tr><tr><td>Computer knowledge</td><td>Novice user (1), experienced user (2), professional (3), computer scientist (4)</td></tr><tr><td>Age</td><td>Up to 25 (1), between 25 and 40 (2), above 40 (3)</td></tr><tr><td>No. of lists subscribed</td><td>Up to 2 (1), between 2 and 7 (2), above 7 (3)</td></tr><tr><td>Use of e-mail</td><td>Once in a couple of days (1), once a day (2), several times a day (3)</td></tr><tr><td>Weekly use of Internet</td><td>Up to 5 h (1), between 5 and 10 h (2), above 10 h (3)</td></tr><tr><td>% of e-mail filtering</td><td>No filtering (1), up to 20% (2), between 20% and 50% (3), above 50% (4)</td></tr></table>

Table 2  
Sociological profiles of some users

<table><tr><td>User no.</td><td>Education</td><td>Occupation</td><td>Level</td><td>Computer knowledge</td><td>Age</td><td>No. of lists subscribed</td><td>Use of e-mail</td><td>Weekly use of Internet</td><td>% of e-mail filtering</td></tr><tr><td>1</td><td>1</td><td>1</td><td>2</td><td>4</td><td>3</td><td>2</td><td>2</td><td>2</td><td>3</td></tr><tr><td>2</td><td>3</td><td>4</td><td>3</td><td>3</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>3</td><td>3</td><td>4</td><td>3</td><td>3</td><td>1</td><td>1</td><td>2</td><td>1</td><td>1</td></tr><tr><td>4</td><td>1</td><td>1</td><td>3</td><td>2</td><td>3</td><td>2</td><td>2</td><td>2</td><td>3</td></tr><tr><td>5</td><td>2</td><td>2</td><td>3</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>6</td><td>5</td><td>3</td><td>2</td><td>2</td><td>2</td><td>1</td><td>1</td><td>3</td><td>1</td></tr><tr><td>7</td><td>3</td><td>3</td><td>2</td><td>3</td><td>1</td><td>2</td><td>2</td><td>1</td><td>2</td></tr><tr><td>8</td><td>1</td><td>1</td><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>1</td><td>1</td></tr></table>

The first part includes questions on sociological parameters that might affect users in their information seeking and filtering behavior. These parameters will found a basis for defining stereotypes’ sociological parameters, and for assigning new users to existing stereotypes. The questions include parameters such as the user’s education, occupation, age, level at work, computer knowledge and experience, number of list-servers subscribed to, and rate of Internet use. Some of these parameters were proposed in the literature e.g., education 5,17 , occupationŽ <sup>w</sup> <sup>x</sup> <sup>w x</sup> <sup>w x</sup> <sup>w</sup> <sup>x</sup> 17 , level 23 and computer knowledge 1,5 .. Other parameters, such as the number of lists the user subscribed to, or the rate of Internet use, are proposed here because we believe that they have different effects on different user types. For each question<sup>r</sup>parameter, we provided a set of possible answers values .Ž .

Table 1 presents the sociological parameters, their possible values and numerical decoding. <sup>1</sup> The result of this part of the interview is sociological profiles of the 40 users. Table 2 exemplifies the sociological profiles of eight of them. For example, it shows that User 1 is a PhD, researcher in computer science, age above 40, subscribes to two to seven list servers, who spend 5–10 weekly hours on the Internet.

The second part of the interview consisted of questions concerning the users’ preferences and habits in seeking or filtering information. Each question deals with a certain parameter of data items, such as its goal subject , source and length. TheŽ . users were asked to rank the importance<sup>r</sup>relevance of each parameter to them, using a 1–7 scale: A rank of 0 would mean that the parameter is not relevant; 1 — that it is of low importance, and 7 — that it is very important. The ranks assigned by users to each parameter provide a basis for the definition of use stereotypes and filtering rules.

As an outcome of this part of the interviews, a set of eight rules with identical param and ² : ² : ² : val\_of\_param , but with different value was defined and implemented in the prototype system. ŽOther questions concerning information seeking and filtering behavior, to which most users — over 85% — answered that they are non-relevant for the filtering process, did not lead to the definition of filtering rules. Table 3 presents the parameters of the eight. filtering rules that were implemented, and Table 4 exemplifies the values assigned by eight of the 40 users. The rules are labeled as their valŽ ² : \_of\_param in Table 3. For example, it shows that User 1. evaluates messages about conferences as important Ž . 5 , while messages about job offers are regarded as not important 1 .Ž .

Table 3  
Filtering rules

<table><tr><td>Parameter</td><td>Val_of_param</td><td>Meaning of the rule</td></tr><tr><td>Goal</td><td>Conference</td><td>Announcement of a conference</td></tr><tr><td>Goal</td><td>Paper</td><td>Call for papers</td></tr><tr><td>Goal</td><td>Internet</td><td>Reference to sites on the Internet</td></tr><tr><td>Goal</td><td>Technical</td><td>Technical message</td></tr><tr><td>Goal</td><td>Job</td><td>Job offer</td></tr><tr><td>Goal</td><td>Fund</td><td>Announcement on funds (research grants, etc.)</td></tr><tr><td>Length</td><td>Length &gt;2 screens</td><td>Message whose length is above two screens</td></tr><tr><td>History</td><td>Occurrences &gt;2</td><td>Message topic already discussed (replied) more than twice</td></tr></table>

## 3.2. Formation of user stereotypes

We used the clustering technique 9 for the parti-<sup>w</sup> <sup>x</sup> tion of the interviewed users to stereotypes. Clustering is a suitable data-analysis technique for stereotype formation 21 since clusters and stereotypes share the basic idea of setting groups whose members are similar in various parameters.

There exist three main general categories of clustering methods: k-means clustering, two-way joining clustering Ž . also termed block clustering , and joining clustering Ž . also termed tree clustering . K-means clustering is used when where there is a hypothesis concerning the desired number of clusters; this method will produce exactly k different clusters. Two-way joining clustering is useful in the rela- Ž tively rare situations when one expects that both . cases observations and variables will simultane- Ž . ously contribute to the uncovering of meaningful patterns of clusters. Joining tree clustering( ) , which is the most popular clustering method, joins together objects into successively larger clusters, using some measure of similarity or distance between the objects. This clustering algorithm begins by placing each object in a separate cluster. Then, an iterative process of joining objects into same clusters is performed. In each iteration, more objects are linked together into common, meaningful clusters.

Table 4  
Values of filtering rules assigned by some users

<table><tr><td rowspan="2">User no.</td><td colspan="8">Rules and values</td></tr><tr><td>Conference</td><td>Paper</td><td>Internet</td><td>Technical</td><td>Job</td><td>Fund</td><td>Length</td><td>History</td></tr><tr><td>1</td><td>5</td><td>4</td><td>4</td><td>1</td><td>1</td><td>5</td><td>1</td><td>3</td></tr><tr><td>2</td><td>6</td><td>3</td><td>6</td><td>2</td><td>2</td><td>2</td><td>1</td><td>2</td></tr><tr><td>3</td><td>6</td><td>3</td><td>6</td><td>3</td><td>2</td><td>1</td><td>3</td><td>3</td></tr><tr><td>4</td><td>6</td><td>6</td><td>3</td><td>2</td><td>5</td><td>6</td><td>2</td><td>2</td></tr><tr><td>5</td><td>2</td><td>1</td><td>1</td><td>1</td><td>4</td><td>2</td><td>2</td><td>2</td></tr><tr><td>6</td><td>5</td><td>1</td><td>5</td><td>6</td><td>2</td><td>2</td><td>1</td><td>6</td></tr><tr><td>7</td><td>5</td><td>1</td><td>6</td><td>7</td><td>2</td><td>2</td><td>1</td><td>4</td></tr><tr><td>8</td><td>6</td><td>7</td><td>2</td><td>1</td><td>1</td><td>7</td><td>4</td><td>2</td></tr></table>

We used joining clustering for the formation of stereotypes, since the other clustering methods are not applicable to our problem: K-means clustering is not suitable because we do not have a hypothesis concerning a desired number of stereotypes. Two-way joining clustering is not suitable either, because our purpose is to organize the observed data users inŽ . meaningful structures stereotypes , but we do notŽ . need to cluster any variable only the users, whoŽ form the cases<sup>r</sup>observations . In our case, the simi-. larities among users who form a stereotype are based on commonalties in their patterns of information usage and filtering, as deduced from the values of filtering rules that have been assigned by the users. Each rule provides one parameter in the similarity calculation, and its value is the numeric value for² : the calculation. We used the joining clustering technique as applied in Statistica-for-Windows versionŽ 6.0 by Statsoft. To compute clusters, the Euclidean. distance measure was used. The amalgamation rule, which determines when two clusters are sufficiently similar to be linked together, is the unweighted pair-group average. In this method, the distance between two clusters is calculated as the average distance between all pairs of objects in the two different clusters.

Fig. 3 displays the result of the clustering process. It shows clearly four clusters, separated by dashed

lines. Table 5 displays the grouping of the 40 users into the four stereotypes, as based on Fig. 3. TheŽ stereotype numbers refer to the precedence in their definition during the clustering process..

Dendrogram Rescaled Distance Cluster Combine  
![](/api/attachments/DN68DEM2/fulltext/images/5abd8644f7945718455bf9196d53943d717a01b1d50217f4ad8922bea4d275c2.jpg)  
Fig. 3. Clustering results.

Table 5  
Partition of users to stereotypes

<table><tr><td>Stereotype</td><td>Users</td></tr><tr><td>1</td><td>1, 4, 8, 9, 17, 25, 23, 29, 30, 31, 32, 37</td></tr><tr><td>2</td><td>5, 6, 10, 11, 13, 14, 15, 16, 22, 27, 36</td></tr><tr><td>3</td><td>2, 3, 18, 19, 20, 35, 38, 39, 40</td></tr><tr><td>4</td><td>7, 12, 21, 24, 26, 28, 33, 34</td></tr></table>

## 3.3. Definition of the stereotypes’ rules

Definition of the stereotypes’ rules means three things: a determination of the rules that are applica- Ž . ble to each of the stereotypes; b determination ofŽ . the value of each rule for each of the stereotypes; value actually means the relevance-rank that will be given to an evaluated data item by this rule; and cŽ . determination of procedures to compute certainty of each rule.

For the determination of the rules that are applicable to a certain stereotype, the statistical average of each rule’s values for all users that belong to that stereotype was calculated. Only rules whose standard deviation is below a certain threshold are selected to represent the stereotype. The justification for this is that a low standard deviation implies unity of the rule value among the members of the stereotype. ŽThe threshold for the standard deviation was set according to the following criteria: a It must not beŽ . too high, so that not to include all the rules in all the stereotypes, because it is not reasonable that all rules will apply to all stereotypes. b It must not be too Ž . low, so that a stereotype will include at least several rules. For the prototype system, we set the threshold by trial-and-error to two, so that each stereotype will include at least four rules..

The value of each rule included in a certain stereotype is the average of the values of its rules. Table 6 displays the rules that represent each stereotype and their average values. As can be seen, the stereotypes differ in the set of the rules that represent them, and in the average values of their rules. For example, stereotype 1 has six relevant rules; for each of these rules, the standard deviation of their values were below the threshold 2, while for the rest two rules ‘‘technical’’ and ‘‘length’’ the standard devi-Ž .

ations were above that threshold. Note that the same rule may be relevant to several stereotypes, but with different values for each e.g., messages about funds Ž are of high importance for stereotype 1 but low for stereotypes 2 and 4 ..

Each rule is implemented by special procedures, which determine how to evaluate and rank messages. Ranking is based on multiplication of two factors: the first of which is the average value of that rule for the stereotype as shown in Table 6 and the other isŽ . a certainty factor, which indicates to what degree is the rule relevant to the evaluated message. Hence, if a rule is not relevant at all, its rank is 0; if it is 100% relevant, its rank is equal to the average value for that stereotype as in Table 6 ; otherwise, it is anyŽ . number between, depending on the certainty factor computed. To compute the certainty factor of a rule, the system looks for specific indicators in the message that enables it to determine the pertinence of the message to the rule. The indications are based on the occurrences of appropriate terms and common structures in various types of e-mail messages see Ref.Ž <sup>w</sup> <sup>x</sup> 14 . For example: to determine with 100% certainty. that a message is about a conference announcement, either a the body of the message must include more Ž . than one occurrence of terms from a pre-defined list of ‘‘conference terms’’, and at least one occurrence of a date, or b at least one occurrence of a ‘‘con-Ž . ference term’’ in the subject header of the message. Partial fulfilment of conditions will result with lower certainty. Space precludes showing more detailsŽ about the rule procedures and certainty factors..

Table 6  
Rules of stereotypes and their average values

<table><tr><td rowspan="2">Rule</td><td colspan="4">Average values of rules per stereotypes</td></tr><tr><td>Stereotype 1</td><td>Stereotype 2</td><td>Stereotype 3</td><td>Stereotype 4</td></tr><tr><td>Conference</td><td>5.83</td><td>2.45</td><td>4.78</td><td>4.38</td></tr><tr><td>Paper</td><td>5.92</td><td>1.36</td><td>2.00</td><td>1.38</td></tr><tr><td>Internet</td><td>4.25</td><td>-</td><td>4.89</td><td>-</td></tr><tr><td>Technical</td><td>-</td><td>-</td><td>1.89</td><td>6.63</td></tr><tr><td>Job</td><td>2.08</td><td>-</td><td>2.22</td><td>1.5</td></tr><tr><td>Fund</td><td>6.5</td><td>1.82</td><td>-</td><td>1.88</td></tr><tr><td>Length</td><td>-</td><td>-</td><td>-</td><td>1.5</td></tr><tr><td>History</td><td>1.92</td><td>1.73</td><td>1.44</td><td>-</td></tr></table>

3.4. Definition of the stereotypes’ sociological parameters

We need to define the sociological parameters and values to represent each stereotype, so as to enable the assignment of new users to the right stereotypes.

To accomplish this, the frequency of values of each of the sociological parameters is calculated for the users who belong to a given stereotype. RecallŽ that the sociological parameters were obtained during the first part of the interview. Only parameters . whose frequency is aboÕe a certain threshold are considered as representative of a stereotype. We set Ž the frequency threshold by taking into consideration the following criteria: a It should be above 50%, to Ž . assure that only highly frequent sociological parameters represent each stereotype. b It should not beŽ . too high, so that there will remain a sufficient number of parameters to represent each stereotype; we decided that each stereotype be represented by at least five sociological parameters. By trial-and-error, this led us to set the frequency threshold to 60%.. Hence, each stereotype is represented by a set of the most common values of sociological parameter of the users who belong to that stereotype.

Table 7 presents the sociological parameters and their values for each stereotype. For example, the sociological profile of stereotype 1 is: PhD researcher, age above 40, uses e-mail once a day, subscribes to two to seven list-servers, and usually filters out 20%–50% of the e-mail messages. It is noticeable that a certain parameter may represent different stereotypes, with the same or with different values. For example, occupation is represented in all stereotypes, but in every stereotype with a different value, while the level of users is typically junior in stereotypes 2 and 3, senior in stereotype 4, and not typical at all in stereotype 1.

## 4. Experimentation with filtering strategies

We conducted a series of experiments with the prototype system, aimed at examining the following issues:

1. The applicability of the model, especially the applicability of sociological filtering integrated with stereotypes.

2. The impact of using dual-method filtering, i.e., various combinations parallel and consecutive Ž . of sociological and cognitive filtering.

3. The optimal filtering strategy for different user stereotypes.

4. The impact of certain filtering rules on relevance ranking.

The experiments involved 10 users, consumers of e-mail messages, from the same domain that was used to create the database of stereotypes and filtering rules but not from the above 40 users .Ž .

To enable cognitive filtering, we had to prepare a cognitive profile of each of the 10 participants, describing his<sup>r</sup>her areas of interest. Each of the 10 participants received a proposed list of terms that was generated from several dozen of his<sup>r</sup>her incoming e-mail messages. The list included the most frequently occurring terms in those messages. It was Ž prepared with the aid of special software that extracts meaningful terms from messages, employing stemming algorithm, look-up tables and a stop-list, and counts the frequency of the meaningful terms.. Each participant was asked to review the proposed list of terms, add or drop terms, and weigh each term for its degree of interest to him, using a 0–100 scale.

Table 7  
Representing sociological values for the stereotypes

<table><tr><td rowspan="2">Parameter</td><td colspan="4">Values of parameters</td></tr><tr><td>Stereotype 1</td><td>Stereotype 2</td><td>Stereotype 3</td><td>Stereotype 4</td></tr><tr><td>Education</td><td>1 (PhD)</td><td>2 (MSc)</td><td>-</td><td>-</td></tr><tr><td>Occupation</td><td>1 (researcher)</td><td>2 (information specialist)</td><td>4 (student)</td><td>3 (technical staff)</td></tr><tr><td>Level</td><td>-</td><td>1 (junior)</td><td>1 (junior)</td><td>3 (senior)</td></tr><tr><td>Computer knowledge</td><td>-</td><td>2 (experienced user)</td><td>-</td><td>3 (professional)</td></tr><tr><td>No. of lists is subscribed</td><td>2 (2–7 lists)</td><td>-</td><td>1 (up to 2 lists)</td><td>2 (2–7 lists)</td></tr><tr><td>Use of e-mail</td><td>2 (once a day)</td><td>2 (once a day)</td><td>3 (more than once a day)</td><td>-</td></tr><tr><td>Weekly use of Internet</td><td>-</td><td>-</td><td>1 (up to 5 h)</td><td>-</td></tr><tr><td>Age</td><td>3 (above 40)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>% of e-mail filtering</td><td>3 (20%–50%)</td><td>-</td><td>1 (no filtering)</td><td>3 (20%–50%)</td></tr></table>

For example, User-X was offered a list of over 400 terms, generated from his e-mail messages. Here is a partial list of terms in alphabetic order and hisŽ . weights: artificial intelligence 60 , algorithms 70 ,Ž . Ž . agents 50 , browsing 50 , client–server 50 , clus- Ž . Ž . Ž . tering 50 , communication 60 , database 50 , and Ž . Ž . Ž . digital library 90 .Ž .

To enable sociological filtering, we had to prepare a sociological profile of each of the 10 participant users, and then assign each of them to an appropriate stereotype. The sociological profile of each participant was created with a questionnaire, similar to the way it was created for the 40 original users seeŽ Section 3.1 . For example, for User-X, we obtained. the following profile: education, PhD 1 ; occupa-Ž . tion, researcher 1 ; level, senior 2 ; computerŽ . Ž . knowledge, computer science 4 ; age, above 40 4 ;Ž . Ž . number of subscribed lists, two to seven 2 ; fre-Ž . quency of e-mail usage, once a day 2 ; weekly useŽ . of Internet, 5–10 h 2 ; percentage of e-mail mes- Ž . sages filtered out, 20–50 2 .Ž .

The assignment procedure that relates a new user to a stereotype calculates the Euclidean distance between the user’s sociological profile and the vectors of sociological parameters that represent each of the existing stereotypes see Table 7 . The EuclideanŽ . distance between two vectors x Ž . the user’s profile and y Ž . the sociological parameters of a stereotype is Ždistance $x , y ) = \{ \Sigma _ { i } ( x _ { i } - y _ { i } ^ { 2 } ) \} ^ { 1 / 2 }$ <sup>w</sup> <sup>x</sup> 6 . The stereotype whose vector of sociological parameters is closest to the user’s profile is chosen to be ‘‘his’’ stereotype. 2

For example, the Euclidean distance of the sociological profile of User-X to the sociological profiles of stereotypes 1, 2, 3 and 4 is 1, 3.162, 4, and 2.449, respectively; hence, User-X is assigned to stereotype 1. It means that User-X inherits from stereotype 1 the respective filtering rules as shown in Table 6 . Ž .

Table 8 presents the assignment of the 10 participants to the four stereotypes, as resulted from the assigning procedure.

For the actual experiments with the various filtering strategies, each of the 10 participants evaluated the relevancy of about 200 e-mail messages that came in from list-servers dealing with professional matters. This was done with the aid of front-end software that was developed for this purpose. The users used a 1–7 scale to rank the relevancy of each message see Fig. 4 . Once a user evaluated a mes-Ž . sage, its rank, along with the message and the user identification, was saved to a special file. The same messages were evaluated later by the filtering system; each message was evaluated several times — each time using a different filtering strategy. The output of these runs were a file for each participant user, containing for each message, the user’s evaluation rank , the ranks produced by each of the filter- Ž . ing strategies, and the randomly generated rank.

The following is an example for the evaluation of a certain e-mail message obtained by User-X. The message was sent from DBWORLD a list server forŽ database people , announcing an opening for a post- . doctoral fellowship. Part of that message is displayed in Fig. 4. User - X who was assigned to stereotype 1Ž — researchers — as based on his sociological profile ranked the relevancy of this message as three,. possibly because he was not looking for a job. His partial interest in the message may be a result of the information it provides on job openings in his working area.

In cognitiÕe filtering, the system evaluates this message by computing the correlation between the weighted-terms in the user’s cognitive profile and the frequency of those terms in the message, relatively to the message length. The system identifiesŽ and counts the frequency of meaningful terms, as described earlier for the construction of cognitive profiles; see beginning of Section 4. For this mes-. sage, the relevance rank is 4.27. The correlation is Ž actually 0.61 in a <sup>y</sup>1 to 1 scale; 4.27 is its transformation onto a 1–7 scale. This rank is high, com- . pared to the user’s rank, because the message contains terms that appear in the user’s profile such as Ž communication and agents , but — as indicated by . the user — the message is not so relevant to him Ž . rank 3 . This example shows that cognitive filtering alone may not be sufficient, and may even be misleading.

Assignment of participant users to stereotypes

<table><tr><td>Stereotype</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Users</td><td>1, 6, 9</td><td>2, 5, 8</td><td>7, 10</td><td>3, 4</td></tr></table>

![](/api/attachments/DN68DEM2/fulltext/images/30580337e7da1327921f6ab86d4a08ce0c3d4690e8d33c3ae48b0ab3383575ee.jpg)  
Fig. 4. Front-end interface for e-mail evaluation.

In sociological filtering, the system evaluates this message by applying the six filtering rules of stereotype 1 User-X’s stereotype . Each of these rulesŽ . may provide one rank<sup>r</sup>value, and the overall sociological rank for the message is the average of the applicable rules’ ranks. The rules of stereotype 1 yielded the following ranks:

<sup>Ø</sup> Conference<sup>s</sup>0: the system found no evidence that the message is about a conference announcement.

<sup>Ø</sup> Paper<sup>s</sup>0: the system found no evidence that the message is about a call for papers.

<sup>Ø</sup> Internet<sup>s</sup>0: the message does not include an Internet address.

<sup>Ø</sup> Job<sup>s</sup>2.08: the system found that the message is definitely about a job opening, and therefore rated the message according to the value of this rule for stereotype 1.

<sup>Ø</sup> Fund<sup>s</sup>4.5: the system found that the message is about funding with 70% certainty, which is multiplied by the value of the rule 6.5 . The 70%Ž . certainty was determined because the stem ‘‘fund’’ appears in the message body, but not in the subject header.

<sup>Ø</sup> History<sup>s</sup>0: the message does not refer to earlier messages having the same subject obtained by the user i.e., no ‘‘reply’’ with same subject in theŽ message header ..

Table 9  
Correlation results for stereotype 1 researchersŽ .

<table><tr><td colspan="5">X = user evaluation; Y = system evaluation; N = 429; correlation significant at p &lt; 0.05</td></tr><tr><td>Filtering strategy</td><td>r(X,Y)</td><td> $r^2$ </td><td>t</td><td>p</td></tr><tr><td>Cognitive</td><td>0.5753*</td><td>0.3309*</td><td>14.533*</td><td>0.0000*</td></tr><tr><td>Sociological</td><td>0.4767*</td><td>0.2273*</td><td>11.207*</td><td>0.0000*</td></tr><tr><td>Parallel</td><td>0.5875*</td><td>0.3451*</td><td>15.002*</td><td>0.0000*</td></tr><tr><td>Cognit (60)-sociol (40)</td><td>0.5939*</td><td>0.3528*</td><td>15.256*</td><td>0.0000*</td></tr><tr><td>Cognit (70)-sociol (30)</td><td>0.6066*</td><td>0.3680*</td><td>15.766*</td><td>0.0000*</td></tr><tr><td>Sociol (60)-cognit (40)</td><td>0.5330*</td><td>0.2841*</td><td>13.018*</td><td>0.0000*</td></tr><tr><td>Sociol (70)-cognit (30)</td><td>0.5160*</td><td>0.2262*</td><td>12.447*</td><td>0.0000*</td></tr><tr><td>Random</td><td>-0.0473</td><td>0.0022</td><td>-0.978</td><td>0.3284</td></tr></table>

Thus, the overall rank of this message, according to the sociological filtering method, is the average of the applicable rules’ ranks, i.e., $( 2 . 0 8 + 4 . 5 ) / 2 =$ 3.29. In this example, the sociological filtering rank is closer to the user’s evaluation, because this message is more related with the sociological profile of the user — and hence with the filtering rules that apply to this stereotype — than with the cognitive profile of that user.

The rank of this message according to the parallel filtering strategy is calculated as the average of cognitive and sociological ranks: 4.27Ž . <sup>q</sup>3.29 <sup>r</sup>2<sup>s</sup> 3.78, which is better i.e., closer to the user’s evalua-Ž tion than cognitive filtering, but worse than socio-. logical filtering. The result for consecutiÕe filtering where cognitive filtering is the primary method, with weight 70%, followed by sociological filtering is: 0.7 4.27Ž . Ž . <sup>q</sup> 0.3 3.29 <sup>s</sup> 3.976. For consecutive filtering where sociological filtering is the primary method the rank is 3.29, equal to sociological filtering alone. This is because the relevance threshold for sociological filtering is 3.5; since the rank obtained by sociological filtering is lower than the threshold, it becomes the overall rank of the message. <sup>3</sup>

In conclusion, for this particular example, the best strategy is sociological filtering, then comes a consecutive strategy where sociological filtering is the primary method, and followed by the parallel filtering strategy. Cognitive filtering is worst strategy for this case. Of course, for different users in the sameŽ or different stereotypes and different messages, dif-. ferent results may be obtained, meaning that different filtering strategies may be more appropriate.

The overall goal was to find out which filtering strategy generates evaluations that are mostly correlated with the user evaluations, and if any filtering strategy is consistently more effective than other for different user stereotypes. The rationale for the use of correlation is that effectiveness of a filtering system cannot be determined according to some ‘‘objective’’ measure; it can only be determined by comparing it’s prediction of relevancy of data items to user subjective evaluation of relevancy of the same data items. We evaluated our filtering system using Pearson correlation to measure the correlation between the user’s relevance judgments of e-mail messages, and the system’s prediction of the relevance of those messages. This enabled us to conclude to what extent the system predictions satisfy users’ needs. Significant correlation means that the system can effectively predict relevance of messages, since its judgment is ‘‘proportional’’ to the user’s judgments. Furthermore, since we measured the correlation between system prediction and user evaluation while employing various filtering methods, we were able to compare the performance of the different filtering methods.

The comparison of filtering strategies was done within stereotypes because the experiments are meant to examine the effect of sociological filtering as integrated with stereotypes. To do so, for every filtering strategy, a vector that includes the ranks of messages given by users that belong to a certain stereotype was correlated with the system-produced ranks for the same messages.

Table 10  
Correlation results for stereotype 2 information specialists Ž .

<table><tr><td colspan="5">X = user evaluation; Y = system evaluation; N = 469; correlation significant at p &lt; 0.05</td></tr><tr><td>Filtering strategy</td><td>r(X,Y)</td><td> $r^2$ </td><td>t</td><td>p</td></tr><tr><td>Cognitive</td><td>0.5048*</td><td>0.2548*</td><td>12.636*</td><td>0.0000*</td></tr><tr><td>Sociological</td><td>0.4828*</td><td>0.2331*</td><td>11.914*</td><td>0.0000*</td></tr><tr><td>Parallel</td><td>0.6387*</td><td>0.4079*</td><td>17.938*</td><td>0.0000*</td></tr><tr><td>Cognit (60)-sociol (40)</td><td>0.4677*</td><td>0.2187*</td><td>11.434*</td><td>0.0000*</td></tr><tr><td>Cognit (70)-sociol (30)</td><td>0.4420*</td><td>0.1953*</td><td>10.647*</td><td>0.0000*</td></tr><tr><td>Sociol (60)-sociol (40)</td><td>0.3914*</td><td>0.1532*</td><td>9.191*</td><td>0.0000*</td></tr><tr><td>Sociol (70)-sociol (30)</td><td>0.0646</td><td>0.0042</td><td>1.399</td><td>0.1624</td></tr><tr><td>Random</td><td>-0.0473</td><td>0.0022</td><td>-1.023</td><td>0.3068</td></tr></table>

In addition to the above, we wanted to test the impact of specific rules on sociological filtering. For that, we conducted an additional experiment with one of the stereotypes that we chose randomly. In this experiment, we examined the effect of each rule by omitting it from its stereotype. For each filtering strategy that involves sociological filtering, we ran the system several times, each time omitting one of the rules, and computed the correlation as above.

## 5. Analysis of results

The main results of the experiments are summarized in Tables 9–12. Each table refers to one stereotype and shows the correlation between the system’s rankings of the messages Ž . Y and the users’ rankings Ž . X . Each row refers to a different filtering strategy. ŽRandom means system generated random ranking, i.e., no filtering method.. N is the number of messages involved in the analysis of all users in the Ž stereotype ..

The columns of each table are: r XŽ . ,Y is the correlation coefficient; $r ^ { 2 }$ is the coefficient of determination; t is the statistic of significance test; and p is the level of significance of the correlation $( p <$ 0.05 is considered significant . The results are inter-. preted as follows: The higher the correlation between the rankings of a filtering strategy and those of the users belonging to a given stereotype — the better it is, because it means that the system’s evaluation of messages is similar to the user’s evaluation of the same messages.

Based on those tables, here are our main observations on the results per stereotype:

<sup>Ø</sup> Stereotype 1: Cognitive filtering alone is better than sociological filtering alone, but parallel filtering is better than either method alone. The best strategy here is consecutive filtering with cognitive as the primary method. The worst strategy for this stereotype is sociological filtering alone, while second to worst would be consecutive filtering with sociological as primary. Therefore, at any rate, sociological filtering improves performance when applied in parallel with or following cognitive filtering.

Correlation results for stereotype 3 studentsŽ .

<table><tr><td colspan="5">X = user evaluation; Y = system evaluation; N = 179; correlation significant at p &lt; 0.05</td></tr><tr><td>Filtering strategy</td><td>r(X,Y)</td><td> $r^2$ </td><td>t</td><td>p</td></tr><tr><td>Cognitive</td><td>0.4686*</td><td>0.2194*</td><td>7.053*</td><td>0.0000*</td></tr><tr><td>Sociological</td><td>0.4342*</td><td>0.1885*</td><td>6.412*</td><td>0.0000*</td></tr><tr><td>Parallel</td><td>0.5884*</td><td>0.3462*</td><td>9.682*</td><td>0.0000*</td></tr><tr><td>Cognit (60)-sociol (40)</td><td>0.6155*</td><td>0.3788*</td><td>10.389*</td><td>0.0000*</td></tr><tr><td>Cognit (70)-sociol (30)</td><td>0.6153*</td><td>0.3786*</td><td>10.385*</td><td>0.0000*</td></tr><tr><td>Sociol (60)-cognit (40)</td><td>0.5303*</td><td>0.2812*</td><td>8.321*</td><td>0.0000*</td></tr><tr><td>Sociol (70)-cognit (30)</td><td>0.5056*</td><td>0.2556*</td><td>7.797*</td><td>0.0000*</td></tr><tr><td>Random</td><td>-0.0178</td><td>0.0003</td><td>-0.237</td><td>0.8132</td></tr></table>

Table 12  
Correlation results for stereotype 4 technical staff Ž .

<table><tr><td colspan="5">X = user evaluation; Y = system evaluation; N = 350; correlation significant at p &lt; 0.05</td></tr><tr><td>Filtering strategy</td><td>r(X,Y)</td><td> $r^2$ </td><td>t</td><td>p</td></tr><tr><td>Cognitive</td><td>0.4062*</td><td>0.1650*</td><td>8.292*</td><td>0.0000*</td></tr><tr><td>Sociological</td><td>0.6521*</td><td>0.4252*</td><td>16.045*</td><td>0.0000*</td></tr><tr><td>Parallel</td><td>0.7051*</td><td>0.4971*</td><td>18.548*</td><td>0.0000*</td></tr><tr><td>Cognit (60)-sociol (40)</td><td>0.5482*</td><td>0.3005*</td><td>12.226*</td><td>0.0000*</td></tr><tr><td>Cognit (70)-sociol (30)</td><td>0.5301*</td><td>0.2810*</td><td>11.663*</td><td>0.0000*</td></tr><tr><td>Sociol (60)-cognit (40)</td><td>0.6578*</td><td>0.4327*</td><td>16.291*</td><td>0.0000*</td></tr><tr><td>Sociol (70)-cognit (30)</td><td>0.6598*</td><td>0.4353*</td><td>16.378*</td><td>0.0000*</td></tr><tr><td>Random</td><td>-0.0511</td><td>0.0026</td><td>-0.955</td><td>0.3404</td></tr></table>

<sup>Ø</sup> Stereotype 2: Parallel filtering yield the best results, followed by cognitive filtering alone and then sociological filtering alone. Surprisingly, the results for the two consecutive methods are lower than for each method alone. Particularly low are theŽ results when sociological filtering is the primary method..

<sup>Ø</sup> Stereotype 3: Here again, the consecutive strategy with cognitive filtering as primary method yields the best results, followed by parallel filtering. Then comes consecutive with sociological filtering as primary method. Last again is sociological filtering alone, and second to last be cognitive filtering alone.

<sup>Ø</sup> Stereotype 4: Again, parallel filtering is best, but here the second best strategy is consecutive with sociological as primary method. Following that is sociological filtering alone. The worst strategy for this stereotype is cognitive filtering alone, and second to worst is consecutive with cognitive filtering as primary method.

These results are summarized in Table 13, which shows the strategies within each stereotype by descending order of correlation with the users’ evaluations.

The following interesting observations on the results concern all stereotypes.

Ž . 1 For all stereotypes, all system’s evaluations — whether using one-phase filtering cognitive or Ž sociological , or two-phase filtering combinations,. correlate significantly with the users’ evaluations. ŽThe only exception is the result for stereotype 2 using a consecutive sociological–cognitive filtering with weight 70:30, which is not significant, and — as expected — the randomly generated ranks do not correlate with user evaluations for any stereotype.. This suggests that all filtering methods yield effective results, that match with the users needs to a certain extent. The correlation coefficients range Ž between 0.4062 and 0.7051..

Ž . Ž . 2 For most stereotypes 1, 2 and 3 , cognitive filtering alone provides higher correlation than sociological filtering alone. Hence, sociological filtering cannot substitute cognitive filtering, which is based on the contents terms of data items.Ž .

Table 13  
Order of filtering strategies within stereotypes

<table><tr><td>Order</td><td>Stereotype 1</td><td>Stereotype 2</td><td>Stereotype 3</td><td>Stereotype 4</td></tr><tr><td>1</td><td>Cognit (70) + sociol (30)</td><td>Parallel</td><td>Cognit (60) + sociol (40)</td><td>Parallel</td></tr><tr><td>2</td><td>Cognit (60) + sociol (40)</td><td>Cognitive</td><td>Cognit (70) + sociol (30)</td><td>Sociol (70) + cognit (30)</td></tr><tr><td>3</td><td>Parallel</td><td>Sociological</td><td>Parallel</td><td>Sociol (60) + cognit (40)</td></tr><tr><td>4</td><td>Cognitive</td><td>Cognit (60) + sociol (40)</td><td>Sociol (60) + cognit (40)</td><td>Sociological</td></tr><tr><td>5</td><td>Sociol (60) + cognit (40)</td><td>Cognit (70) + sociol (30)</td><td>Sociol (70) + cognit (30)</td><td>Cognit (60) + sociol (40)</td></tr><tr><td>6</td><td>Sociol (70) + cognit (30)</td><td>Sociol (60) + cognit (40)</td><td>Cognitive</td><td>Cognit (70) + sociol (30)</td></tr><tr><td>7</td><td>Sociological</td><td>Sociol (70) + cognit (30)</td><td>Sociological</td><td>Cognitive</td></tr></table>

Table 14  
Correlation results for stereotype 1 with omitted rules

<table><tr><td rowspan="2">Filtering strategy</td><td colspan="6">Correlation coefficients  $r(X,Y)$ </td></tr><tr><td>No rule omitted</td><td>Omitting “funds”</td><td>Omitting “jobs”</td><td>Omitting “Internet”</td><td>Omitting “papers”</td><td>Omitting “conference”</td></tr><tr><td>Sociological</td><td>0.476736*</td><td>0.472940*</td><td>0.422040*</td><td>0.327266*</td><td>0.475272*</td><td>0.308894*</td></tr><tr><td>Parallel</td><td>0.587494*</td><td>0.582887*</td><td>0.528965*</td><td>0.165880*</td><td>0.522723*</td><td>0.418711*</td></tr><tr><td>Cognit (60)–sociol (40)</td><td>0.593946*</td><td>0.589738*</td><td>0.552459*</td><td>0.305457*</td><td>0.575950*</td><td>0.547813*</td></tr><tr><td>Cognit (70)–sociol (30)</td><td>0.606589*</td><td>0.602929*</td><td>0.569228*</td><td>0.572088*</td><td>*</td><td>0.578735*</td></tr><tr><td>Sociol (60)–cognit (40)</td><td>0.533029*</td><td>0.528019*</td><td>0.481711*</td><td>0.339888*</td><td>0.453403*</td><td>0.336227*</td></tr><tr><td>Sociol (70)–cognit (30)</td><td>0.515992*</td><td>0.511744*</td><td>0.077390</td><td>0.336365*</td><td>0.439662*</td><td>0.352029*</td></tr></table>

Ž . Ž . 3 For most stereotypes 1, 2 and 3 , the consecutive strategy where cognitive is primary filtering method provides higher correlation coefficients than the consecutive strategy where sociological is primary method.

Ž . 4 In no case are cognitive or sociological filtering alone better than some combination of cognitive and sociological either consecutive or parallel .Ž .

Ž . Ž . 5 For two stereotypes 2 and 3 , parallel filtering turned out to be best, and for the other two 1 and 4Ž . — second best after the consecutive where cogni- Ž tive filtering is primary . Consequently, in all cases. parallel filtering is better than cognitive alone or sociological alone.

Ž . Ž . 6 For two stereotypes 1 and 3 , consecutive combinations with cognitive filtering as primary method turned out to be best strategy.

Ž . 7 Sociological filtering alone is worst strategy for two stereotypes 1 and 3 , while cognitive filter- Ž . ing alone is worst strategy for one stereotype only Ž . 4 .

Ž . 8 Most of the two-phase filtering results have higher correlation coefficients than the corresponding one-phase filtering method. That is, parallel filtering is compared to either of the filtering methods, while consecutive combination is compared in each run to the filtering method that was considered as ‘‘primary’’ method on that run.

In conclusion, for every stereotype there is at least one significantly better result when the strategy is to combine the two filtering methods in some way. So, dual-method filtering is definitely vital. However, there is no single strategy that is ‘‘best’’ in all cases;

the best strategy is stereotype-dependent. In other words, for every stereotype the best strategy needs to be discovered. This can be done by means of experimentation or after gaining experience with the system.

Stereotype 1 was randomly chosen for the additional experiment, where we ran the system while omitting rules. The results of this experiment are presented in Table 14. It displays the correlation coefficients Ž Ž .. r X,Y obtained with the complete set of rules identical to the equivalent column in TableŽ 9 , and the coefficients obtained when each time. another rule is omitted. Note that cognitive filtering Ž is not included here, as it is not affected by rules..

As can be seen, in all cases a missing rule affects the filtering results, i.e., the correlation coefficients are smaller but not to a point that makes the resultsŽ insignificant . The omission of different rules causes. different changes in the correlation, meaning that each rule has some specific effect in its stereotype. For example, the most affecting rules for stereotypeŽ 1 are ‘‘conference’’ and ‘‘Internet’’, while the. ‘‘jobs’’ rule has little effect on the correlation coefficients. These results make sense, since the represen-Ž tative occupation for stereotype 1 is researcher.. These outcomes also emphasize the importance of a learning process that will detect needs for additional rules, as well as possibilities to omit unnecessary rules, or change the ranks<sup>r</sup>values of existing rules.

## 6. Conclusions

Sociological filtering is defined in this model as a filtering process that evaluates and ranks relevance of data items as based on user sociological parameters. We implemented sociological filtering by means of rules attached to user stereotypes. We showed that sociological filtering, even as a single filtering method, is significantly correlated with user evaluations, implying that it is viable and can be used to predict the relevance of data items for users. However, we found that in most cases cognitive filtering alone is more correlated with user evaluations than sociological filtering alone. This should not be taken as a surprise; after all, cognitive filtering is about the content of data items, which is obviously a major criterion for relevance.

We found it clearly that for every stereotype, there exists at least one combination of the two filtering methods consecutive or parallel that is Ž . better than either filtering method alone. The conclusion from that is that dual-method filtering is better than any single-method filtering. These results strengthen results of other researchers e.g., Ref. 2 Ž <sup>w</sup> <sup>x</sup>. that combined collaborative and content-based filtering and have shown improvement compared to content-based filtering.

The experiments show that there is no single ‘‘best’’ strategy for combining cognitive and sociological filtering. For different stereotypes, there may be different ‘‘best’’ combinations: parallel, or cognitive followed by sociological, or sociological followed by cognitive. Hence, the optimal filtering strategy may be considered as a stereotype characteristic, which can be inferred by experimentation and experience.

The impact of stereotypes on user modeling is already known 5,18 , and so is their potential contri-<sup>w</sup> <sup>x</sup> bution to information filtering 11 . Our experiments<sup>w</sup> <sup>x</sup> iterate on the viability of stereotypes, offering new methods of handling them via cluster-analysis. We use stereotypes to infer knowledge about users, which is hard to infer directly from them. Specifically, we infer information usage and filtering patterns from stereotypic belonging. We found, through interviews, that users are having difficulties in defining information preferences; when asked, they provided only general and fuzzy descriptions of their information needs. It seems more efficient to initially infer user needs form their stereotypical belonging, and if needed, to adapt them via a learning process.

For the formation of the stereotypes, we have assumed that in a heterogeneous environment like aŽ university there are different user types, and it is . possible to find clusters of users that have similar patterns of information usage and filtering. Users, who employ similar filtering rules, also tend to share common sociological parameters e.g., same profes-Ž sion, job, and education ..

The filtering model includes a learning process, but we have addressed it only partially when weŽ dealt with the need to revise the stereotypes if new users cannot be assigned confidently to existing stereotypes . In the future, we plan to extend the. learning process, so that it will become possible to detect new rules or change existing rules as based on user feedback, as well as due to changes in the user population and their information needs.

Because of the small number of participants in the experiments, we cannot claim for external validity of the results. For that, more experiments, encompassing more users and involving a variety of application domains, are needed. However, our experiments did show the applicability of dual-method filtering model, including the integration of sociological filtering with stereotypes. Furthermore, the consistency of the results, which are based on about 200 data items per participant, certainly show the correctness of the approach and encourage further research.

The model presented in the paper can be applied as a front-end filtering system in various information technology domains, such as e-mail list-servers, newsgroups, search engines for information retrieval systems and Internet search, electronic commerce, and digital libraries. In the case of e-mail list-servers, such a system can assist the list master to disseminate ‘‘push’’ messages selectively — not necessar-Ž . ily to all members of the list. Similarly, such a filtering system can be applied in newsreaders, to filter relevant news articles to readers according to their stereotypic belonging. The filtering system that applies this model can be part of a search engine of a retrieval system, or an Internet search engine. Users may be related to known stereotypes that are maintained by the systems, to receive information that matches their stereotypic preferences as well as their queries.

In electronic commerce, such a system can be applied to various commercial activities, such as advertising, marketing, or auction, where different products can be offered to potential customers on the basis of their stereotypic affiliation. In digital libraries, such a system can assist readers in finding the information they need, by matching the retrieved information to their cognitive needs as defined by their queries, and to their preferences and habits as defined by the stereotypes that they belong to. In a separate research, we are working on the integration of the model into digital libraries in several domains.

For each application domain, it is necessary to carefully define the most suitable set of sociological parameters to be included in the sociological profile of users and in the stereotypes’ representation vector. For example: a system designed for electronic commerce will include parameters that are relevant to potential customers e.g., the range of income, area Ž of living, shopping history, etc. . Prior to implement-. ing the system in a certain domain, one needs to analyze the domain environment in order to determine the parameters that might have influence on users’ needs of information in the specific domain.

## References

<sup>w</sup> <sup>x</sup> 1 R.B. Allen, User models: theory, methods and practice, Int. J. Man-Mach. Stud. 32 1990 511–543.Ž .

<sup>w</sup> <sup>x</sup> 2 M. Balabanovic, Y. Shoham, Fab: content-based collaborative recommendation system, Commun. ACM 40 3 1997 Ž . Ž . 66–72.

<sup>w</sup> <sup>x</sup> 3 N.J. Belkin, W.B. Croft, Information filtering and information retrieval: two sides of the same coin?, Commun. ACM 35 12 1992 29–38.Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 G. Brajnik, G. Guida, C. Tasso, User modeling in expert man–machine interfaces: a case study in intelligent information retrieval, IEEE Trans. Systems, Man and Cybernetics 20 Ž . Ž . 1 1990 66–185.

<sup>w</sup> <sup>x</sup> 5 D.N. Chin, KNOME: modeling what the user knows, in: A. Kobsa, W. Wahster Eds. , User Models in Dialog Systems,Ž . Chap. 3, Springer-Verlag, Berlin, 1989, pp. 74–107.

<sup>w</sup> <sup>x</sup> 6 W.J. Dixon, F.J. Massey, Introduction to Statistical Analysis, 4th edn., McGraw-Hill, New York, 1983.

<sup>w</sup> <sup>x</sup> 7 W. Finin, GUMS: a general user modeling shell, in: A. Kobsa, W. Wahster Eds. , User Models in Dialog Systems,Ž . Chap. 15, Springer-Verlag, Berlin, 1989, pp. 411–430.

<sup>w</sup> <sup>x</sup> 8 P.W. Foltz, S.T. Dumais, Personalized information delivery: an analysis of information filtering methods, Commun. ACM 35 12 1992 51–60.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 A.K. Jain, R.C. Dubes, Algorithms for Clustering Data, Prentice-Hall Advanced Reference Series, 1988.

<sup>w</sup> <sup>x</sup> 10 J. Kay, Um: a user modeling toolkit, Second Int’l User Modeling Workshop, 1990, pp. 11–51.

<sup>w</sup> <sup>x</sup> 11 J. Kay, R. Kummerfeld, Customization and Delivery of

Multimedia Information, Technical Report, Basser Dept. of Computer Science, University of Sydney, 1994.

<sup>w</sup> <sup>x</sup> 12 F. Killander, A Brief Comparison of News Filtering Software, Http:<sup>rr</sup> www.glue.umd.edu<sup>r</sup> enee<sup>r</sup> medlab<sup>r</sup> filter<sup>r</sup> filter.html, 1996.

<sup>w</sup> <sup>x</sup> 13 T. Malone, K. Grant, F. Turbak, S. Brobst, M. Cohen, Intelligent information sharing systems, Commun. ACM 30 Ž . Ž .5 1987 390–402.

<sup>w</sup> <sup>x</sup> 14 A.D. May, Automatic classification of e-mail messages by message type, J. Am. Soc. Inf. Sci. 48 1 1997 32–39.Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 H. McLeary, Filtered information services — a revolutionary new product or a new marketing strategy?, Online 4 18Ž . Ž . 1994 33–42.

<sup>w</sup> <sup>x</sup> 16 M. Morita, Y. Shinoda, Information filtering based on user behavior analysis and best match retrieval, in: Proceedings of the 17th Annual Intl. ACM SIGIR Conference for Research and Development, 1994, pp. 272–281.

<sup>w</sup> <sup>x</sup> 17 E. Rich, User modeling via stereotypes, Cognit. Sci. 3 1979Ž . 329–354.

<sup>w</sup> <sup>x</sup>18 E. Rich, Stereotypes and user modeling, in: A. Kobsa, W. Wahster Eds. , User Models in Dialog Systems, Springer-Ž . Verlag, 1989, pp. 35–51.

<sup>w</sup> <sup>x</sup>19 G. Salton, W.J. McGill, Introduction to Modern Information Retrieval, McGraw-Hill, New York, 1983.

<sup>w</sup> <sup>x</sup> 20 B. Shapira, U. Hanani, A. Raveh, P. Shoval, Information filtering: a new two-phase model using stereotypic profiling, J. Intell. Inf. Syst. 8 1997 155–165.Ž .

<sup>w</sup> <sup>x</sup> 21 B. Shapira, P. Shoval, U. Hanani, Stereotypes in information filtering systems, Inf. Process. Manage. 33 3 1997 273– Ž . Ž . 287.

<sup>w</sup> <sup>x</sup> 22 U. Shardanand, P. Maes, Social information filtering algorithm for automating ‘‘Word of Mouth’’, Proceedings of the 1995 ACM Conference on Human Factors in Computing Systems, 1995, pp. 210–217.

<sup>w</sup> <sup>x</sup> 23 J. Vassileva, A practical and adaptable user model support browsing in hypermedia information systems, Proceedings of Intelligent Multimedia Information Retrieval Systems and Management, RIAO, New York, 1994.

![](/api/attachments/DN68DEM2/fulltext/images/bb7fe854b786750376a97b225fb9a4e56014c2d589cda6fb824ff4878b50ed37.jpg)

Bracha Shapira received her BSc degree in Computer Science from Bar-Ilan University, MSc in Computer Science from the Hebrew University of Jerusalem, and PhD in Information Systems from Ben-Gurion University. Her doctoral dissertation entitled ‘‘a two-phase filtering model integrating stereotypes’’ was presented at the ICIS’97 doctoral consortium. In 1998, she was a visiting researcher at the Center for Information Management Integration and Connectiv-

ity at Rutgers University, and is now faculty with the MSIS Department in the School of Business at Rutgers. Bracha’s research interests include information filtering, user modeling for digital libraries and Internet news applications, especially with the integration of stereotypes.

![](/api/attachments/DN68DEM2/fulltext/images/2689f60a2cf32bbd3cc286460a4dc69faf74bee5c1d5acb1c8861d733caa051d.jpg)

Peretz Shoval is Professor of Information Systems at Ben-Gurion University Israel. He earned his BA in Economics and MSc in Information Systems from Tel-Aviv University, and PhD in Information Systems 1981 from the Univer-Ž . sity of Pittsburgh, where he specialized in expert systems for information retrieval. In 1984, he joined the Department of Industrial Engineering and Management at Ben-Gurion University, where he started and is head of the

Information System Engineering Program. Prior to moving to academia, he held professional and managerial positions in computer companies and in the IDF. Shoval’s research interests include data modeling and database design, information systems analysis and design methods, and information retrieval and filtering. He has published numerous papers in journals and presented his research in various conferences. Shoval is the developer of ADISSA methodology and tools for systems analysis and design, and of ADDS system for conceptual and logical database design.

![](/api/attachments/DN68DEM2/fulltext/images/4600ddc3b795a0c0a594c9b3969a74de93f238616b846edbae6969c98abd0585.jpg)

Uri Hanani received his BSc in Mathematics and Physics, and MA and PhD in Operation Research from the Hebrew University of Jerusalem. He is Lecturer at the Department of Information Studies of Bar-Ilan University, and at the Department of Industrial Engineering and Management of Ben-Gurion University, Israel. Formerly, he was director of the Medical Informatics Department at Hadssah Medical Center, Jerusalem. Hanani’s research interests include intel-

ligent hypertext, information harvesting and intelligent information retrieval. He is member of IEEE Computer Society and the ACM.
