---
otero_id: 12198
otero_key: "WCCRH37R"
title: "Tour recommendations by mining photo sharing social media"
authors: "Chih-Yuan Sun; Anthony J.T. Lee"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.05.013"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Accepted Manuscript

## Tour recommendations by mining photo sharing social media

Chih-Yuan Sun, Anthony J.T. Lee

Decision Support Systems

![](/api/attachments/WCCRH37R/fulltext/images/ba94bc75cc01de62216a00b9a51e85c61d29d6c5cb22ed36ec7e124a8b9aa8f2.jpg)

PII: S0167-9236(17)30098-2

DOI: doi: 10.1016/j.dss.2017.05.013

Reference: DECSUP 12848

To appear in: Decision Support Systems

Received date: 31 August 2016

Revised date: 7 May 2017

Accepted date: 16 May 2017

Please cite this article as: Chih-Yuan Sun, Anthony J.T. Lee , Tour recommendations by mining photo sharing social media, Decision Support Systems (2017), doi: 10.1016/ j.dss.2017.05.013

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Tour Recommendations by Mining Photo Sharing Social Media

Chih-Yuan Sun and Anthony J.T. Lee Department of Information Management, National Taiwan University

## Abstract

With the increasing popularity of photo and video sharing social networks, more and more people have shared their photos or videos with their family members and friends. Therefore, in this paper, we propose a framework for recommending top-k tours to meet user’s interest and time frame by using user-generated contents in a photo sharing social network. The proposed framework contains four phases. First, we cluster geotagged locations into landmarks, and further cluster these landmarks into areas by the mean-shift clustering method. Second, we employ the Latent Dirichlet Allocation model to categorize the hashtags posted by users into landmark topics, and then use these topics to characterize landmarks and users. Third, to recommend tours for a user, we compute the tendency (or score) of the user visiting each landmark by the landmark popularity, the attraction of landmark to the user, and how many users similar to the user visit the landmark. Finally, based on the scores computed, we develop a method to recommend top-k tours with highest scores for the user. Unlike most previous methods recommending tours landmark by landmark, our framework recommends tours area by area so that users can avoid going back and forth from one area to another and save plenty of time on transportation, which in turn can visit more landmarks. The experiment results show that our proposed method outperforms the Markov-Topic method in terms of average score and precision. Our proposed framework may help users plan their trips and customize a trip for each user.

Keywords: tour recommendation, photo sharing social network, mean-shift clustering method, Latent Dirichlet Allocation model, data mining.

## 1. Introduction

With the increasing popularity of photo and video sharing social networks, more and more people have shared their photos or videos with their family members and friends. A recent Harvard

# ACCEPTED MANUSCRIPT

Business School study [34] indicates that about 70% of all Facebook activities revolve around photos, whether people are uploading, viewing, liking, or commenting on them. Moreover, Instagram, an online mobile photo and video sharing social network, lunched and had one million registered users in 2010. Its user base increased to 600 million in 2016 [30]. The shared photos usually contain geotagged locations, timestamps, hashtags and descriptions, where the geotagged location of a photo is a Global Positioning System (GPS) coordinate. If we collect the locations visited by a user and order them by the timestamps associated with the photos, we will obtain a trajectory visited by the user. By mining these trajectories, we may recommend some travel tours users most interested in, and help them plan the trips.

Many methods have been proposed for location-based recommendations. Several methods [10][22][26] focus on location recommendations. Some methods [7][25] find an optimal tour for users while the others [11][12][15] recommended top-k tours by considering trip budget, users preferences and temporal-based properties, where a tour may contain a sequence of locations. However, most methods recommend tours landmark by landmark (or location by location), and thus cannot avoid going back and forth on the tours so that users may need to spend plenty of time on transportation.

Therefore, in this paper, we propose a framework for recommending top-k tours to meet user’s interest and time frame by using user-generated contents in a photo sharing social network. The proposed framework contains four phases. First, we cluster geotagged locations into landmarks, and further cluster these landmarks into areas. Second, we category the hashtags into landmark topics, and then use these landmark topics to generate landmark and user feature vectors. Third, by landmark and user feature vectors generated in the second phase, we compute the tendency (or score) of a user visiting each landmark. Finally, based on the scores computed, we develop a method to recommend top-k tours with highest scores for the user.

The contributions of the proposed framework are summarized as follows. First, unlike most previous methods recommending tours landmark by landmark, our framework recommends tours area by area so that users can avoid going back and forth from one area to another and save plenty of time on transportation, which in turn can visit more landmarks. Second, we category the hashtags posted by users into landmark topics, and then use these topics to characterize landmarks and users.

Third, we develop a method to recommend top-k tours with highest scores for users by further considering visiting time and visiting order of areas. Thus, the recommended tours can meet user’s interest and time frame. Fourth, the experiment results show that our proposed method outperforms the comparing method. Finally, our proposed framework may help users plan their trips and customize a trip for each user.

The rest of this paper is organized as follows. We survey the related literature in Section 2 and propose our framework in Section 3. Next, we evaluate the performance of the proposed framework in Section 4. Finally, the conclusions and future work are made in Section 5.

## 2. Related work

In this section, we survey the literature of mining photo sharing social media, and location-based recommendation systems.

Photo Sharing Social Media. Popescu et al. [18] mined the associations between textual metadata and Flickr photos, and then used the associations mined to find user’s home location and gender. Zhang et al. [24] analyzed tags, image features of geo-tagged and timestamped photos to measure the occurrences of ecological phenomena. Hao et al. [6] extracted location-based representative tags from travelogues to automatically generate location overviews in both visual and textual forms. Ji et al. [8] used the landmarks from geotagged Flickr photos to implement scene summarizations and touristic recommendations. Popescu et al. [17] proposed a method to filter a set of geotagged photos to answer the questions such as how long it takes to visit a tourist attraction or where one should visit in a day in a city. Unlike these methods, Kurashima et al. [11][12] recommended tours for users by exploiting user-generated contents in Flickr.

Location-Based Recommendation Systems. Many methods have been proposed to recommend locations and tours based on user’s preferences. Kurashima et al. [10] analyzed users’ location logs to recommend locations to be visited, and estimate users’ activity areas and interest in the recommended locations. Wang et al. [22] proposed a method called Geo-SAGE to recommend a spatial item by considering user’s personal interest and the preferences of crowd in the target region. Santos et al. [19] used Google Maps to present a user-friendly web-based spatial decision support system to generate optimized vehicle routes. Tsai et al. [21] developed a route recommendation

# ACCEPTED MANUSCRIPT

system for theme park tourists to recommend the facilities and the orders to be visited. Kurashima et al. [11][12] utilized user’s preferences and photographers’ histories recorded by Flickr to recommend travel tours. Wei et al. [23] presented a tour inference framework based on collective knowledge to construct the popular tours from uncertain trajectories. Hsieh et al. [7] mined several check-in datasets to recommend time-sensitive tours consisting of a sequence of locations and timestamps by considering the visiting time and transportation time between locations.

Some previous studies [10][22][26] only recommend locations, not tours, to users. Several methods [7][25] recommend an optimal tour to users. Hsieh et al. [7] recommended an optimal tour by considering popularity, transportation time, time duration staying in each location, visiting time and visiting order. Zhang et al. [25] found an optimal tour for a user by taking the availability of points of interest (POIs) and uncertain traveling time into account. The others [11][12][15][23] recommend top-k tours to users. Lu et al. [15] considered multiple constraints to recommend the tours by considering trip budget, users’ preferences, transportation time and time duration staying in each location, where they assumed that the locations are well categorized. Wei et al. [23] constructed the tours from uncertain trajectories. Kurashima et al. [11][12] recommended top-k tours by considering user preference, transportation time and visiting order. The differences between our method and previously proposed methods are listed in Table 1.

Table 1. The differences between our method and previously proposed methods.

<table><tr><td></td><td>UP</td><td>PO</td><td>TT</td><td>TD</td><td>VT</td><td>VO</td><td>BF</td><td>TK</td></tr><tr><td>Hsieh et al. [7]</td><td></td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td></td><td></td></tr><tr><td>Zhang et al. [25]</td><td>●</td><td></td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td></td></tr><tr><td>Wei et al. [23]</td><td></td><td>●</td><td>●</td><td></td><td></td><td></td><td></td><td>●</td></tr><tr><td>Lu et al. [15]</td><td>●</td><td></td><td>●</td><td>●</td><td></td><td></td><td></td><td>●</td></tr><tr><td>Kurashima et al. [11][12]</td><td>●</td><td></td><td>●</td><td></td><td></td><td>●</td><td></td><td>●</td></tr><tr><td>Ours</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr></table>

Note: UP stands for user preference, PO for popularity, TT for transportation time, TD for time duration staying in each location, VT for visiting time, VO for visiting order, BF for

avoiding going back and forth on the recommended tour, and TK for recommending top-k locations (or landmarks).

It looks that our method is more similar to those of Hsieh et al. [7] and Zhang et al. [25] in Table 1. However, both methods only recommend an optimal tour for a user, while our method recommends top-k tours. Also, Lu et al. [15] assumed that the locations are well categorized; however, the geotagged locations in a photo sharing social network are not. Therefore, we compare our proposed framework with Kurashima et al. [11][12] since they also recommend top-k tours.

## 3. Our proposed framework

In this section, we propose a framework to recommend top-k tours for a user (she), where she will specify a starting time and a trip length, and may optionally specify a starting location. When a user posts a photo in a social network, she often marks some hashtags with the photo, where the photo usually contains a timestamp and a geotagged location (a GPS coordinate) that the photo is taken.

![](/api/attachments/WCCRH37R/fulltext/images/5ee6bd8eedebd131b4cd0b4172265d133c99a84d281e5929a937e4db67892b1f.jpg)  
Figure 1. The proposed framework.

The proposed framework first employs the mean-shift clustering method [5] to group neighboring locations into a cluster, called a landmark, and then further groups these landmarks into clusters, each of which is called an area. That is, the locations are clustered into two layers, namely landmark and area. Next, it applies the Latent Dirichlet Allocation (LDA) model [2] to category the hashtags into landmark topics, which can be used to characterize landmarks and users. Based on these topics, it derives a landmark feature vector for each landmark and a user feature vector for each user. Then, to recommend a tour for a user, it uses the landmark and user feature vectors to compute the scores of each landmark and each area by the popularity of the landmark, the attraction of the landmark to the user, and how many users similar to the user visiting the landmark. Finally, based on the scores computed, it recommends top-k tours with highest scores to the user.

## 3.1. Location clustering

A photo in Flickr is usually tagged with a GPS coordinate. However, these GPS coordinates tagged with the photos taken around a landmark may be slightly different, where a landmark may be a store, a restaurant, a building, or a sightseeing spot. Crandall et al. [4] showed that the mean-shift clustering method is an effective method for extracting landmarks from spatial data. Thus, we apply it to group the tagged locations into clusters, each of which represents a landmark.

However, if we recommend a tour landmark by landmark, users may need to go back and forth from one area to another during a tour. For example, a recommended tour contains landmarks A, B, C and D, where A and C are close to each other, and B and D are close to each other but it takes time from A to B, from B to C, or from C to D. If a user visits these landmarks in order, she needs to go back and forth. To avoid going back and forth on a recommended tour, we further employ the mean-shift clustering method to group neighboring landmarks into a cluster, each of which represents an area. Thus, A and C can be clustered into an area, and B and D into the other. Then, users can visit A and C, and then B and D. That is, we group locations into two layers of clusters, and recommend a tour area by area, not landmark by landmark.

## 3.2. Landmark and user characterization

Since LDA has been widely used and performed well in many applications such as document summarization [1], topic inference [3] and tag recommendation [9], we apply it to characterize landmarks. For each landmark, we collect all the hashtags marked in all the locations clustered into the landmark to form a virtual document. Thus, we have a collection of landmarks’ virtual documents. Then, we apply LDA to category landmarks’ virtual documents into landmark topics, where each virtual document can be viewed as a mixture of various landmark topics.

LDA is a probabilistic model used to discover latent landmark topics of virtual documents. To

# ACCEPTED MANUSCRIPT

reduce the time complexity of LDA, we employ the collapsed Gibbs sampling algorithm [13] to implement LDA. Specifically, the landmark topic assignment is re-sampled by Eq. (1), where $P ( z _ { i } { = } c |$ $z _ { - i } ,$ H; , $\beta )$ denotes the probability that the ith hashtag $( h _ { i } )$ is assigned to landmark topic c given $z { - } i$ and $H , z _ { i }$ is the landmark topic to which $h _ { i }$ may be assigned, H contains all the hashtags in all virtual documents, $z { - } _ { i }$ contains all landmark topics except z<sub>i</sub>, $n _ { - i } ^ { d _ { i } , c }$ is the number of hashtags assigned to $c$ in virtual document $d _ { i }$ by excluding the current topic assginment of $h _ { i } , \ d _ { i }$ is the virtual document containing $h _ { i } , \ n _ { - i } ^ { c , h _ { i } }$ is the number of times that $h _ { i }$ is assigned to $c \sin$ excluding the current topic assignment of $h _ { i } , ~ | H |$ is the number of hashtags in H, K contains all landmark topics, |K| is the number of landmark topics in $K ,$ and $\alpha$ and $\beta$ are the parameters to decide Dirichlet distributions. That is, the probability that $h _ { i }$ is assigned to $^ { c , }$ $P ( z _ { i } { = } c | z _ { - i }$ , H; , $\beta )$ , is proportional to the ratio of the number of hashtags assigned to c to the total number of hashtags in $d _ { i }$ $( \frac { n _ { - i } ^ { d _ { i } , c } + \alpha } { \sum _ { c ^ { \prime } } n _ { - i } ^ { d _ { i } , c ^ { \prime } } + | K | \alpha } )$ , and the ratio of the number of times that h<sub>i</sub> is assigned to $c$ to the total number of hashtags assigned to $c$ in all virtual documents $( \frac { n _ { - i } ^ { c , h _ { i } } + \beta } { \sum _ { h ^ { \prime } } n _ { - i } ^ { c , h ^ { \prime } } + | H | \beta } )$

$$
P (z _ {i} = c | z _ {- i}, H; \alpha , \beta) \propto \frac {n _ {- i} ^ {d _ {i} , c} + \alpha}{\sum_ {c ^ {\prime}} n _ {- i} ^ {d _ {i} , c ^ {\prime}} + | K | \alpha} \times \frac {n _ {- i} ^ {c , h _ {i}} + \beta}{\sum_ {h ^ {\prime}} n _ {- i} ^ {c , h ^ {\prime}} + | H | \beta}\tag{1}
$$

From Eq. (1), $h _ { i }$ is more likely to be assgined to $c$ if there is a large number of hashtags of $c$ in $d _ { i }$ and $h _ { i }$ is frequently assigned to c in the virtual documents. The sampling process is performed repeatedly until a pre-specified number of iterations $\tau _ { I }$ is reached.

Initially, each hashtag in the virtual documents is randomly assigned to a landmark topic. In each iteration of the sampling process, each hashtag is reassigned to a landmark topic according to the probabilities computed by Eq. (1). Let us demonstrate how a hashtag is reassigned to a landmark topic by an example, where virtual document $d _ { I }$ contains 8 hashtags, the number of hashtags in $d _ { I }$ assigned to the first, second and third landmark topics are respectively 5, 2 and 1, hashtag island appears 50 times in all virtual documents, 30 of them are assigned to the first landmark topic, 15 of them are assigned to the second landmark topic, 5 of them is assigned to the third landmark topic, the number of hashtags in all virtual documents assigned to the first, second and third landmark topics are respectively 100, 150 and 200, the number of landmark topics is 3 (i.e. |K|=3), the number of hashtags in all virtual documents is 450 (i.e. |H|=450), and $\alpha { = } \beta { = } 0 . 1$ . For hashtag island in $d _ { I }$ assigned to the first landmark topic in the previous iteration, by excluding the current topic assignment, $\begin{array} { r } { n _ { - i } ^ { d _ { 1 } , 1 } { = } 4 , ~ \sum _ { c ^ { \prime } } n _ { - i } ^ { d _ { 1 } , c ^ { \prime } } { = } 7 , ~ n _ { - i } ^ { 1 , i s l a n d } ~ = 2 9 } \end{array}$ and $\textstyle \sum _ { h ^ { \prime } } n _ { - i } ^ { 1 , h ^ { \prime } } = 9 9 $ . Thus, the probability that the hashtag is assigned to the first landmark topic, $P ( z _ { i } { = } 1 | z _ { - i } , H ; 0 . 1 , 0 . 1 )$ , is proportional to $\frac { 4 + 0 . 1 } { 7 + 3 \times 0 . 1 } \times$ $\frac { 2 9 + 0 . 1 } { 9 9 + 4 5 0 \times 0 . 1 } { \cong } 0 . 1 1 3$ , where $z _ { i }$ is the landmark topic to which island may be assigned. The probability that the hashtag is assigned to the second landmark topic, $P ( z _ { i } { = } 2 | z _ { - i } , H ; 0 . 1 , 0 . 1 )$ , is proportional to $\begin{array} { r } { \frac { 2 + 0 . 1 } { 7 + 3 \times 0 . 1 } \times \frac { 1 5 + 0 . 1 } { 1 5 0 + 4 5 0 \times 0 . 1 } \cong 0 . 0 2 2 } \end{array}$ , where $n _ { - i } ^ { d _ { 1 } , 2 } = 2 , n _ { - i } ^ { 2 , i s l a n d } = 1 5$ and $\begin{array} { r } { \sum _ { h ^ { \prime } } n _ { - i } ^ { 2 , h ^ { \prime } } = 1 5 0 } \end{array}$ . Similarly, the probability that the hashtag is assigned to the third landmark topic, $P ( z _ { i } { = } 3 | z _ { - }$ i, H; 0.1, 0.1), is proportional to $\begin{array} { c } { { \frac { 1 + 0 . 1 } { 7 + 3 \times 0 . 1 } \times \frac { 5 + 0 . 1 } { 2 0 0 + 4 5 0 \times 0 . 1 } \tilde { \equiv } 0 . 0 0 3 } } \end{array}$ , where $n _ { - i } ^ { d _ { 1 } , 3 } = 1 , n _ { - i } ^ { 3 , i s l a n d } = 5$ and $\begin{array} { r } { \sum _ { h ^ { \prime } } n _ { - i } ^ { 3 , h ^ { \prime } } = 2 0 0 } \end{array}$ Therefore, the probabilities that hashtag island is assigned to the first, second and third landmark topics $\begin{array} { r } { \mathrm { a r e ~ } \frac { 0 . 1 1 3 } { 0 . 1 1 3 + 0 . 0 2 2 + 0 . 0 0 3 } \cong 0 . 8 2 , \frac { 0 . 0 2 2 } { 0 . 1 1 3 + 0 . 0 2 2 + 0 . 0 0 3 } \cong 0 . 1 6 \mathrm { ~ a n d ~ } \frac { 0 . 0 0 3 } { 0 . 1 1 3 + 0 . 0 2 2 + 0 . 0 0 3 } \cong 0 . 0 2 } \end{array}$ . That is, the hashtag is assigned to the first landmark topic with probability 82%, the second landmark topic with probability 16%, and the third landmark topic with probability 2%. A hashtag is labeled as landmark $\tau _ { 2 } .$ a hashtag may be labeled as multiple landmark topics.

After the sampling process finishes, each hashtag may be labeled as one or more landmark topics. Each landmark topic c can be represented by a collection of hashtags labeled as c. Let us consider an example shown in Figure 2, where the superscript $j$ of a hashtag denotes the labeled landmark topic of the hashtag, and hastag island in $V D _ { I }$ has two labels. The hashtags labeled as the first landmark topic are alcatraz, island, jail and prison. Thus, we may infer that the first landmark topic is about Alcatraz Island. Similarly, the second landmark topic is about San Francisco Giants, and the third is about San Francisco Fisherman’s Wharf. There are four hashtags in $V D _ { I }$ labeled as the first landmark topic, and two hashtags labeled as the third landmark topic. Thus, the landmark feature vector of $V D _ { I }$ is (2/3, 0, 1/3). Similarly, those of $V D _ { 2 }$ and $V D _ { 3 }$ are (0, 0.8, 0.2) and (0.2, 0,

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$VD_{1} = \{\mathrm{alcatraz}^{1},\mathrm{island}^{1,3},\mathrm{pier}^{3},\mathrm{jail}^{1},\mathrm{prison}^{1}\}$ $VD_{2} = \{\mathrm{baseball}^{2},\mathrm{bay}^{3},\mathrm{attpark}^{2},\mathrm{giants}^{2},\mathrm{nationalleague}^{2}\}$ $VD_{3} = \{\mathrm{fishermanswharf}^{3},\mathrm{island}^{1},\mathrm{pier}^{3},\mathrm{bay}^{3},\mathrm{pier}39^{3}\}$
</div>

0.8), respectively.

Figure 2. Three virtual documents after the sampling process finishes.

Since the virtual document of a landmark has a probability of belonging to each landmark topic, we represent each landmark as a feature vector (landmark feature vector hereafter), where the value of the jth dimension of the landmark feature vector denotes the portion of hashtags labeled as the jth landmark topic in the virtual document.

With landmark feature vectors, we can derive the probability of a landmark topic c given a user u by summing up the landmark feature vector of all the landmarks visited by u by Eq. (2), where $P ( c | l _ { i } )$ is the value of the cth dimension of landmark feature vector of $l _ { i } , N ( l _ { i } , u )$ is the number of times that user u visited landmark $l _ { i } , N ( u )$ is the total number of times that user u visited each landmark, and L contains all landmarks visited by u. Since a user has a probability of belonging to each landmark topic, we represent each user as a feature vector (user feature vector hereafter).

$$
P (c | u) = \sum_ {l _ {i} \in L} P (c | l _ {i}) \frac {N (l _ {i} , u)}{N (u)}\tag{2}
$$

## 3.3. Score of each landmark and area

To recommend a tour for user u, we compute the score of u visiting each landmark by the popularity of the landmark, the similarity between the landmark feature vector and $\vec { u ^ { \mathrm { ~ s ~ } } }$ user feature vector, and how many users similar to u visit the landmark.

The more users visit a landmark, the more popular the landmark is. The popularity of landmark l is defined by Eq. (3), where $N ( l )$ is the number of visits to l, and L contains all landmarks.

$$
P O P (l) = \frac {N (l)}{a r g _ {l ^ {\prime} \in L} M a x (N (l ^ {\prime}))}\tag{3}
$$

The more a landmark meets $u ^ { \prime } \mathrm { s }$ interest, the more attractive the landmark is to u. The attraction of landmark l to user u is defined by the inner product of $l ^ { \circ } \mathrm { s }$ landmark feature vector and $\vec { u ^ { \mathrm { ~ s ~ } } }$ user feature vector as shown in Eq. (4), where $P ( c | u )$ is the value of the cth dimension of user feature vector of $u ,$ and K contains all landmark topics. We normalize the attraction into [0,1].

$$
A T T (u, l) = \sum_ {c \in K} P (c | u) P (c | l)\tag{4}
$$

The more users similar to u visit a landmark, the more likely u visits the landmark. The users similar to $u , S U ( u )$ , are the users whose similarity to u is not less than a threshold as shown in Eq. (5), where the similarity between two users, $S i m ( u , u ^ { \prime } )$ , is defined by the inner product of the user feature vectors of both users, U contains all users, and $\tau _ { 3 }$ is a pre-specified threshold. The ratio of similar users visiting the landmark is defined by Eq. (6), where Checkin(u’, l) is equal to 1 if user $u '$ has checked in landmark l, and $| S U ( u ) |$ is the number of users in $S U ( u )$ . Similarly, we normalize the ratio into [0,1].

$$
S U (u) = \{u ^ {\prime} | S i m (u, u ^ {\prime}) \geq \tau_ {3}, u ^ {\prime} \in U \}\tag{5}
$$

$$
R S U (u, l) = \frac {\sum_ {u ^ {\prime} \in S U (u)} C h e c k i n (u ^ {\prime} , l)}{| S U (u) |}\tag{6}
$$

The score of u visiting l is defined by Eq. (7), where $w _ { p o p }$ is the weight of the popularity of l, $\boldsymbol { w } _ { a t t }$ is the weight of the attraction of l to $u ,$ and $w _ { r s u }$ is the weight of the ratio of similar users, and $w _ { p o p } +$ $w _ { a t t } + w _ { r s u } = 1$

$$
S L (u, l) = w _ {p o p} P O P (l) + w _ {a t t} A T T (u, l) + w _ {r s u} R S U (u, l)\tag{7}
$$

![](/api/attachments/WCCRH37R/fulltext/images/c3ca525f93b7b5f4d0f9d55f84b53824dbd1976490aa164e0bcd930d1c40edf9.jpg)  
Figure 3. Example duration distribution.

Since we recommend the landmarks area by area, we first learn the time duration distribution of an area from the dataset. Let DD(a, d) be the probability distribution of visiting area a in time duration d, where $D D ( a , \ d )$ is learnt from the dataset. That is, the time duration distribution is calculated by the check-in records in a on an hourly basis. Figure 3 shows an example time duration distribution of area a. By the time duration distribution, we can determine if it is appropriate to visit a in a given time duration. For example, if we want to know how well it is to spend 3 hours in visiting a given the time duration distribution in Figure 3, we first generate a Gaussian distribution

# ACCEPTED MANUSCRIPT

$G ( d ; \mu , \sigma ^ { 2 } )$ and then measure the difference between $D D ( a , d )$ and $G ( d ; \mu , \sigma ^ { 2 } )$ , where the mean value $\mu$ is 3 and $\sigma$ is the standard deviation of the time duration distribution of $^ { a . }$ Here, we use the symmetric Kullback-Leibler (KL) Divergence [7] to measure the difference between two distributions as shown in Eq. (8), which represents the fitness of visiting a in time duration $d ' .$ . A smaller KL value indicates a better match between both distributions.

$$
\begin{array}{r l} & D _ {K L} (G (d; d ^ {\prime}, \sigma^ {2}) | | D D (a, d)) \\ & \qquad = \sum_ {d} G (d; d ^ {\prime}, \sigma^ {2}) \log \frac {G (d ; d ^ {\prime} , \sigma^ {2})}{D D (a , d)} + \sum_ {d} D D (a, d) \log \frac {D D (a , d)}{G (d ; d ^ {\prime} , \sigma^ {2})} \end{array}\tag{8}
$$

We select those time durations with probability not less than a pre-specified threshold $\tau _ { 4 }$ as candidate time durations. For example, the selected time durations of the area shown in Figure 3 are 1, 2, 3, 4 and 8 if $\tau _ { 4 } { = } 0 . 0 6$ . For each selected time duration $d \chi _ { \chi }$ , we choose a set of landmarks in $a$ so that the stay time in a is not greater than $d '$ , and the summation of the scores of chosen landmarks is the largest, where the stay time of a landmark is derived from the average stay time of the check-in records in the dataset, and the stay time in a is the ion of the stay time of all chosen landmarks. The score of $u$ visiting $a$ in time duration $d '$ is defined by Eq. (9), where Chosen(a, d’) contains all chosen landmarks in $^ { a , }$ and the total stay time of all chosen landmarks is not greater than $d '$ . Then, we choose the time duration for an area as a candidate so that the score of visiting the area in the time duration is not less than a pre-specified threshold $\tau _ { 5 \cdot }$ That is, we further remove the candidate time durations with the scores less than the threshold.

$$
S A \big (u, a, d ^ {\prime} \big) = \sum_ {l \in C h o s e n (a, d ^ {\prime})} S L (u, l) \times D _ {K L} (G (d; d ^ {\prime}, \sigma^ {2}) | | D D (a, d)) ^ {- 1}\tag{9}
$$

## 3.4. Tour recommendation

For a user planning a trip with starting time st and trip length tl, we develop a method, called Tour Recommendations by Sharing Photos (TRSP), to recommend top-k tours with highest scores for the user, where the user may optionally specify starting location sl, each tour contains a sequence of areas, each of which contains a set of recommended landmarks. When adding an area to a recommended tour, we consider the visiting time and visiting order of the area, and the transportation time between the area and the last area of the tour.

The score of visiting area a from time t to $t '$ is defined by Eq. (10), where N(a) is the number of times that a is visited, N(a, [t, t’]) is the number of times that a is visited in $[ t , t ^ { \prime } ]$ , and [t, t’] is a time interval. We compute the probability of visiting a in [t, t’] by $\textstyle \frac { N ( a , [ t , t ^ { \prime } ] ) } { N ( a ) }$ , and then normalize it on an hourly basis by dividing the probability by $t { \mathit { \ Y } } _ { - t . }$ The fitness of a visiting order is defined in Eq. (11), where $N ( a , a ^ { \prime } )$ is the number of times that $\acute { a }$ is visited after a.

$$
V T (a, [ t, t ^ {\prime} ]) = \frac {N (a , [ t , t ^ {\prime} ])}{(t ^ {\prime} - t) * N (a)}\tag{10}
$$

$$
V O (a, a ^ {\prime}) = \frac {N (a , a ^ {\prime})}{N (a)}\tag{11}
$$

If $\acute { a }$ is never visited after a, the fitness is 0. Thus, we employ the Non-negative Matrix Factorization (NMF) method [20] to factorize the fitness matrix V into two matrices W and H, and then approximate V by WH, where an entry $( a , a ^ { \prime } )$ in V denotes the fitness of visiting $\acute { a }$ after a. Figure 4 shows an example of NMF, where V is factorized into two matrices W and H, and approximated by the inner product of both matrices. As shown in the example, most zero-entries in the matrix are approximated by a small positive value, which leads to better score computation.

$$
\left[ \begin{array}{c c c c} 0. 3 & 0 & 0 & 0. 1 \\ 0. 5 & 0 & 0 & 0. 1 \\ 0. 1 & 0. 1 & 0 & 0. 2 \\ 0 & 0. 1 & 0. 1 & 0. 6 \end{array} \right] \approx W \times H = \left[ \begin{array}{c c c c} 0. 3 0 0 5 & 0. 0 1 0 7 & 0. 0 0 5 6 & 0. 0 9 7 0 \\ 0. 4 9 9 9 & 0. 0 0 5 7 & 0 & 0. 1 0 0 2 \\ 0. 0 9 9 1 & 0. 0 3 8 5 & 0. 0 2 8 5 & 0. 2 0 7 9 \\ 0. 0 0 0 2 & 0. 1 1 8 7 & 0. 0 9 0 7 & 0. 5 9 7 7 \end{array} \right]
$$

## Figure 4. An example of NMF.

Next, we describe how the TRSP method recommends top-k tours with highest scores for a user. The TRSP method is shown in Figure 5. We first sort all the areas in non-increasing order by their scores and then construct candidate tours by appending an area to the existing candidate tours at a time, where the area is chosen in order. It ensures that the areas with larger scores are considered before those with smaller ones in the tour construction process. For each area to be considered, we check if the area can be appended to any candidate tour to generate a new one. If this is the case, we further check whether the tour duration of the newly generated candidate tour reaches the trip length tl or not. If yes, the newly generated candidate tour is added to the output list olist; otherwise, it is added to the candidate tour list clist. We repeat the tour construction process until top-k tours are found. During the tour construction process, we devise a pruning strategy to prune redundant candidate tours. If the largest possible score of a candidate tour is less than the score of the kth tour in the output list, the candidate tour is redundant and can be removed from the candidate list.

In step (1), we compute the score for each pair of area a and time duration d by Eq. (9), sort the scores in non-increasing order, and record the sorted areas in an area list alist, where each area is associated with a time duration d. For example, Figure 6(a) illustrates an alist containing the sorted pairs, where $a _ { d }$ denotes that the time duration of visiting area a is d hours. That is, A<sub>1</sub> denotes that the time duration of visiting area A is 1 hour. Next, if the starting location sl is specified, we add the area of sl to a candidate tour list clist; otherwise, we remove the first area in alist and add it to clist in step (2), where the added area forms the first tour in clist and the tour duration is the stay time of the added area. For each area in alist, we append it to each candidate tour in clist if the area has not been appended to the candidate tour, and the tour duration of the newly appended tour does not exceed the trip length tl in the repeat-loop until alist or clist is empty (steps 3-17).

## Method: TRSP

Input: User u, starting time st, trip length tl, and starting location sl (optional)

Output: Top-k tours with highest scores

1. Compute the score for each area by Eq. (9), sort the scores in non-increasing order, and record the sorted areas in a list alist.

2. If sl is specified, add the area of sl to clist; otherwise, remove the first area in alist and add it to clist, where the added area forms the first tour in clist and the tour duration is the stay time of the added area. Set i=0.

3. repeat

4. Remove the first area in alist, and assign it to a and a’s time duration to d.

5. foreach tour o in clist do

6. if a is not in o then

7. Let b be a candidate tour formed by appending a to o, where the score of b equals $r + S A ( u , a , d ) ^ { * } V T ( a , [ t , t + d ] ) ^ { * } V O ( a ^ { \prime } , a )$ , TD(b) equals $T D ( o ) \mathrm { + } T T ( a ^ { \prime } , a ) \mathrm { + } d ,$ r is the score of $^ { O , }$ a’ is the last area in $^ { O , }$ t equals $s t \substack { + T D ( o ) + T T ( a ^ { \prime } , a ) }$ , TD(b) is b’s tour duration and $T T ( a ^ { \prime } , a )$ is the transportation time from a’ to a.

8. if $b \mathrm { ^ { * } s }$ tour duration is less than tl then

9. Add b to clist.

10. else

11. i=i+1.

12. Add b to olist and sort the tours in olist in non-increasing order. If i is not less than k, let ps be the score of the last tour in olist, and keep only top-k tours in olist.

13. endif

15. end foreach

16. Apply the pruning strategy to prune redundant candidate tours in clist.

## Figure 5. The TRSP method.

For each tour o in clist, if $a$ is not in $^ { o , }$ a can be appended to o to form a new candidate tour b in step (7), where the score of b equals $r \mathrm { + } S A ( u , a , d ) ^ { \ast } V T ( a , [ t , t + d ] ) ^ { \ast } V O ( a ^ { \prime } , a )$ , r is the score of $^ { O , }$ $\boldsymbol { a } ^ { \prime }$ is the last area in $^ { o , }$ t equals st plus TD(o) plus $T T ( a ^ { \prime } , a )$ , TD(o) is $\omega ^ { \prime } \ s \ \mathrm { t o u r }$ $T T ( a ^ { \prime } , a )$ is the transportation time from $\boldsymbol { a } ^ { \prime }$ to a, VT(a, [t, t+d]) and $V O ( a ^ { \prime } , a )$ are computed by Eqs. (10) and (11), and TD(b) equals $T D ( o ) \mathrm { + } T T ( a ^ { \prime } , a ) \mathrm { + } d .$ If $b \mathrm { ^ { * } s }$ tour duration is less than $t l ,$ we add $^ b$ to clist in step (9); otherwise, we add b to the output list olist and sort the tours in olist in non-increasing order and then check if the number of tours in olist is not less than k in step (12). If this is the case, we record the score of the kth tour in olist (ps), and keep only top-k tours in olist, where $p s$ can be used to prune redundant candidate tours in clist as shown in step (16).

Figure 6(b) shows how to append an area to clist step by step, where the starting location is not specified, and the newly appended tours are marked grey in each step. We first remove the first area $A _ { I }$ $B _ { I }$ to each candidate tour in clist, and obtain three candidate tours namely, $A _ { I }$ $B _ { I }$ and $A _ { I } B _ { I } ,$ where $B _ { I }$ and $A _ { I } B _ { I }$ are newly appended tours and marked grey. Then, we append $B _ { 2 }$ to each candidate tour in clist, and obtain five candidate tours namely, A<sub>1</sub>, $B _ { I }$ $A _ { I } B _ { I }$ $B _ { 2 }$ and $A _ { I } B _ { 2 }$ , where $B _ { 2 }$ and $A _ { I } B _ { 2 }$ are newly appended tours and marked grey. Since area B has been appended to tours $B _ { I }$ and $A _ { I } B _ { I } , B _ { 2 }$ cannot be appended to them. Furthermore, appending $C _ { I }$ to each candidate tour in clist, we obtain eleven candidate tours as shown in Figure 6(b), where the newly appended tours are marked grey. Figure 6(c) shows an example of olist, where $p s$ denotes the score of the kth tour.

After adding candidate tours to clist in steps (5)-(15), we devise a pruning strategy to prune redundant candidate tours in clist. For each candidate tour $_ { o } '$ , we check if the largest possible score of $\acute { o }$ is less than $p s$ , where the largest possible score is estimated by Eq. (12), and $r '$ is the score of $o$ ’, $S S ( t l - T D ( o ^ { \prime } ) )$ is the summation of the scores of the first tlTD(o’) areas in clist, which are not in $\acute { o }$ . If this is the case, $\acute { o }$ can be removed from clist since its score is certainly less than the least score of top-k tours. Because trip length and tour duration are calculated on an hourly basis, the maximum number of areas that can be added to $\acute { o }$ is at most $t l { - } T D ( o ^ { \prime } )$ . If the score of the tour formed by $\acute { o }$ and these areas is still less than $p s , o ^ { \prime }$ is obviously not a candidate tour to be recommended. Thus, it can be removed from clist.

$$
L S (o ^ {\prime}) = r ^ {\prime} + S S (t l - T D (o ^ {\prime}))\tag{12}
$$

<table><tr><td> $A_1$ </td><td> $B_1$ </td><td> $B_2$ </td><td> $C_1$ </td><td>...</td></tr></table>

(a) alist  
![](/api/attachments/WCCRH37R/fulltext/images/278f4393068378ba8f8646807d87f743d44db721b17286d9548c6b27b35e3371.jpg)

(b) clist

<table><tr><td></td><td>Tour</td><td>Score</td></tr><tr><td>1</td><td> $A_{1}B_{1}C_{1}$ </td><td>4.55</td></tr><tr><td>2</td><td> $A_{1}B_{2}C_{1}$ </td><td>4.23</td></tr><tr><td>3</td><td> $A_{1}B_{1}$ </td><td>3.93</td></tr><tr><td>...</td><td>...</td><td>...</td></tr><tr><td>k</td><td>...</td><td>ps</td></tr></table>

(c) olist  
Figure 6. An example of TRSP.

## 4. Experiment results

In this section, we evaluate the performance of the proposed method. The dataset was collected within 7km of the center of San Francisco City by downloading photo metadata from Flickr using public API of Flickr. The photos were taken between January 1<sup>st</sup>, 2013 and December 31th, 2015. There are 140,885 photographs taken by 4,905 users. Since users tend to check-in the neighboring locations several times, we remove the users taking fewer than 30 photos and the trajectories with length less than 5, where a trajectory contains a series of locations that a user checked in during a day, and the length of a trajectory is defined as the number of locations in it. This is because these users (or trajectories) are not good for tour recommendations since they visit (or contain) too few landmarks or areas. In addition, we remove the hashtags that contain non-English characters or all numbers. Finally, there are 74,421 photos, 672 users and 2,744 trajectories in total.

Next, we apply the mean-shift clustering method to find the landmarks and areas. Landmarks are extracted by adjusting the bandwidth of the mean-shift clustering method until the average of maximum distance between locations in each landmark is less than $\theta ,$ where $\theta$ ranges from 50 to 500 by step of 50 meters. Most of neighboring POIs can be clustered into a landmark when $\theta$ is 300 meters. Thus, we set  to 300 meters in the following experiments. The areas are extracted in a similar way, where the average of maximum distance ranges from 1000 to 2000 by step of 100 meters. Most of neighboring landmarks can be clustered together when the average of maximum distance is 1700 meters. Thus, we set the average of maximum distance to 1700 meters in the following experiments.

The coherence between hastags is frequently used to assess whether the most frequent hashtags in a landmark topic are coherent to each other, as shown in Eq. (13) [16], where tc denotes the coherence, |K| denotes the number of landmark topics, m is the number of most frequent hashtags in landmark topic $^ { c , }$ $D ( c , h _ { i } )$ denotes the number of virtual documents containing hashtag $h _ { i }$ in $^ { c , }$ and $D ( c , h _ { i } , h _ { j } )$ denotes the number of virtual documents containing both $h _ { i }$ and $h _ { j }$ in c. Note that the coherence is negative. The larger the coherence, the more coherent the hashtags in each landmark topic.

$$
t c = \frac {\sum_ {c = 1} ^ {| K |} \sum_ {j = 2} ^ {m} \sum_ {i = 1} ^ {j - 1} l o g \frac {D (c , h _ {i} , h _ {j}) + 1}{D (c , h _ {i})}}{| K |}\tag{13}
$$

## ACCEPTED MANUSCRIPT

![](/api/attachments/WCCRH37R/fulltext/images/253a1cd2d5096c3d7dbd64d49a10c2270782858ef556d48d60c257174ed605f1.jpg)  
Figure 7. Coherence vs. number of landmark topics.

Figure 7 shows the coherence versus the number of landmark topics, where the number of landmark topics varies from 10 to 50 by step of 5. The coherence is not improved much when the number of landmark topics is greater than 30. Thus, we first cluster hashtags into 30 landmark topics; however, some landmark topics are quite similar to each other. This is because users frequently tag their photos with some common words. Next, we cluster them into 25 landmark topics where some landmark topics are similar to each other too. Therefore, we set the number of landmark topics to 20 in the following experiments.

To determine the values of the pre-specified thresholds, we first vary $\tau _ { I }$ from 1000 to 2000 by step of 100. The topic assignment of each hashtag is stable (or most topic assignments of hashtags are kept unchanged) when $\tau _ { I }$ is 1500. Second, we vary $\tau _ { 2 }$ from 0.1 to 0.5 by step of 0.1. The smaller the threshold $\tau _ { 2 }$ is, the more landmark topics a hashtag would be labeled. We decide the value of threshold $\tau _ { 2 }$ by the coherence between hastags, and set $\tau _ { 2 }$ to 0.2 in the following experiments. Third, we vary $\tau _ { 3 }$ from 0.01 to 0.2 by step of 0.01. We can obtain the highest average score when $\tau _ { 3 }$ is 0.1. Finally, we vary $\tau _ { 4 }$ from 0.01 to 0.1 by step of 0.01, and $\tau _ { 5 }$ from 0.01 to 0.1 by step of 0.01. We can obtain a reasonable combination of time durations when $\tau _ { 4 }$ is 0.06 and $\tau _ { 5 }$ to 0.05. Thus, we set $\tau _ { I }$ to 1500, $\tau _ { 2 }$ to 0.2, $\tau _ { 3 }$ to 0.1, $\tau _ { 4 }$ to 0.06 and $\tau _ { 5 }$ to 0.05 in the following experiments.

We compare our method with the Markov-Topic method [12], as both methods extract the landmarks by the mean-shift clustering method and recommend top-k tours for users. The differences between both methods are (1) our method clusters locations into two layers and recommends tours area by area; however, Markov-Topic recommends tours landmark by landmark, (2) Markov-Topic does not use hashtags while our method clusters hashtags into landmark topics by LDA and use the clustered topics to characterize landmarks and users, and (3) our method considers more features than Markov-Topic, namely the popularity of landmark, the ratio of similar users visiting the landmark, the time duration of an area, and the visiting time of an area.

## 4.1. Performance evaluation

We first tune the weights of the scores of popularity, attraction and ratio of similar users. Figure 8 illustrates the average score versus the weights of the scores of popularity and attraction of landmark to user. The average score is highest when $w _ { p o p } { = } 0 . 4 , w _ { a t t } { = } 0 . 5$ and $w _ { r s u } { = } 0 . 1$ . Thus, we use this combination of weights in the following experiments. Since a user tends to visit a landmark attracted to the user, the weight of the attraction of landmark l to user u $( w _ { a t t } )$ is the highest. Also, the more popular a landmark is, the more likely the landmark is visited by users. Moreover, since users have quite different check-in landmarks in a photo sharing social network, the weight of the ratio of similar users visiting the landmark $( w _ { r s u } ) \mathrm { i s }$ t lowest.

![](/api/attachments/WCCRH37R/fulltext/images/0e633692b1273dd02bc30dc57c6ce9246716f3c1d7ced65cb45acb39726b6f5d.jpg)  
Figure 8. Average score of different combinations of weights.

Next, we investigate the effect of each parameter. Figure 9 presents the average score versus the number of recommended tours k, where the average score is the total score of recommended tours divided by k. The average score slightly decreases as k increases in TRSP. The higher score a tour has, the sooner the tour is recommended. Thus, the more tours are recommended, the smaller average score is. However, the average score of Markov-Topic increases from k=1 to 3 and then decreases after k=3. This is because Markov-Topic finds the top-k tours without considering the popularity of landmark, the ratio of similar users visiting the landmark, the time duration of an area, and the visiting time of an area. Since Markov-Topic has the highest average score when k=3, we compare the two methods by setting k to 3 in the following experiments.

![](/api/attachments/WCCRH37R/fulltext/images/c42f1da80b9345ca1fa9233117d71640315b282e4ae8f99c6f9632d63a544a81.jpg)  
Figure 9. Average score vs. number of recommended tours.

![](/api/attachments/WCCRH37R/fulltext/images/f76f71b6aaa850b574eabb2496b194ea87ef0cc1244e835e5f398181b2ac0ed3.jpg)

Figure 10. Average score vs. trip length.

Figure 10 shows the average score versus the trip length. As the trip length increases, the average score increases. This is because users can visit more areas (or landmarks). Markov-Topic has a higher score when the trip length is less than 7 since it recommends tours landmark by landmark and always chooses the landmarks with highest scores, while TRSP recommends tours area by area. The recommended landmarks in an area may be not the ones with highest scores. Thus, the average score of TRSP is lower than that of Markov-Topic in the beginning. However, when the trip length is greater than 7, the average score of TRSP is greater than that of Markov-Topic. This is because Markov-Topic tends to recommend landmarks so that users may need to go back and forth in the tours.

![](/api/attachments/WCCRH37R/fulltext/images/9b9d4321a4bf191dc02b2dbc27eca468ad377edacdfe2b2c241f79e9ef09c983.jpg)  
Figure 11. Precision of one step prediction of both methods.

For each trajectory, we delete its last location, and use both TRSP and Markov-Topic methods to predict the last location. For Markov-Topic, we predict the top-k landmarks with highest scores, where k=3 since Markov-Topic has the highest average score when k=3. If the predicted top-k landmarks contain the deleted location, Markov-Topic gains a hit. For TRSP, we predict top-k areas with highest scores. If the predicted areas contain the deleted location, TRSP gains a hit. We calculate the precision by dividing the number of hits by the number of predictions for each method. Figure 11 shows the precision of one step prediction of both methods. TRSP outperforms

# ACCEPTED MANUSCRIPT

Markov-Topic. This is because TRSP recommends tours by areas and considers more features. Figure 11 also shows the precision for each variation of TRSP, where TRSP-POP, TRSP-RUS and TRSP-VO are TRSP without considering the popularity of the landmark, the ratio of similar users visiting the landmark, and the visiting order, respectively. It’s shown that TRSP performs better than these three variations, and the impact of the visiting order of the landmark is greater than that of the popularity, which is greater than that of the ratio of similar users visiting the landmark.

## 4.2. Example tours

In this section, we demonstrate some example tours recommended by our proposed method and Markov-Topic. TRSP recommends top-k tours for each request made by a user. Figure 12 shows an example tour recommended by TRSP, Beach St [1.5 hours] → 0.5 hours → Palace of Fine Arts [1 hours] → 0.5 hours → Golden Gate Bridge [2 hours] → 0.5 hours → Vista Point [2 hours], where the time in the brackets denotes the time duration in the area, the time between two arrows denotes the transportation time between two areas, and each area is circled by a blue line. The black spot is the starting landmark and the white spot is the ending landmark.

![](/api/attachments/WCCRH37R/fulltext/images/853019fd6830134b1b46dbac4b7cc1b90051950c616ca515b293a3255d858289.jpg)

Figure 12. Example tour recommended by TRSP.

Figure 13 shows the tours recommended by the TRSP and Markov-Topic methods, where the trip length is 8 hours. TRSP tends to recommend a longer tour as shown in Figure 13(a) while Markov-Topic tends to recommend a tour with fewer landmarks as shown in Figure 13(b). This is because Markov-Topic may recommend a tour in which users may need to go back and forth from one area to another. In Figure 13(a), TRSP selects 3 areas in the 8-hour tour and then recommends the landmarks best fit user’s interest in these areas, where each area is circled by a blue line. Thus, it can avoid going back and forth on the recommended tour, save the transportation time, and recommend 8 landmarks within 8 hours. On the other hand, in Figure 13(b), Markov-Topic only recommends 5 landmarks within 8 hours since it needs to go back and forth on the tour and wastes plenty of time on transportation.

![](/api/attachments/WCCRH37R/fulltext/images/b8686fe7e87c43112fb2058e30f234e0881f56ff3c634889ac09f2c03bf38e00.jpg)  
(a) TRSP

![](/api/attachments/WCCRH37R/fulltext/images/97d62a01d908632722b64c80c4bdc8871a3049066692b4b7b7c8a53c715d1a2a.jpg)  
(b) Markov-Topic  
Figure 13. Example tours of both methods.

To recommend tours for different types of users, we first group similar users together by the k-means clustering method [14] and group them into 15 clusters. Next, we use each cluster to represent a specific type of user, and select two clusters as an example. For each cluster selected, we

# ACCEPTED MANUSCRIPT

choose some frequent hashtags posted by the users in the cluster. For example, the frequent hashtags of the first cluster U1 are golden, gate, bridge, sausalito, recreation, national and water. The frequent hashtags of the second cluster U2 are chinatown, square, bayarea, unionsquare and restaurant. Figure 14 shows the recommended tours of both types of users, where we do not set the starting location for both types of users. We can see that the recommended tour for users of cluster U1 is near the areas of beach and the Golden Gate Bridge, and the recommended tour for users of cluster U2 is from area of Union Square to area of China town, which are places known for shopping and dining.

![](/api/attachments/WCCRH37R/fulltext/images/eda9629ad355295a89d1e5c58d4441f262fc071f926eac8ce467e3ec0f4d409f.jpg)  
(a) Cluster U1

![](/api/attachments/WCCRH37R/fulltext/images/c7a37a560a2bbc9e8706d9870ee0d7e0bc85817863107f329c633997e2b946be.jpg)  
(b) Cluster U2  
Figure 14. Example tours with different types of users.

Figure 15 shows the tours recommended for different visiting time, where the starting location is the Fisherman wharf. Figure 15(a) shows the tour for the starting time of 9 a.m., where the tour moves along the beach and toward the Golden Gate Bridge, which are sight-seeing spots much popular in the daytime. Figure 15(b) illustrates the tour for the starting time of 5 p.m., where the tour moves toward the China town and Union Square, which are known for dining and have more night activities.

## 5. Conclusions and future work

In this paper, we have proposed a framework to recommend top-k tours with highest scores for a user by using the photos shared by users in an online social network. Unlike most previous methods recommending tours landmark by landmark, the proposed framework recommends tours area by area, and uses hashtags to characterize landmarks and users. Therefore, users can visit the landmarks met their interest and avoid going back and forth on the recommended tours.

![](/api/attachments/WCCRH37R/fulltext/images/0f8b93545dd8d77c0d35ef84a1e16c894e667b9ccaa55b07af280c7c593d9eba.jpg)  
(a) Visiting time: 9 a.m.

![](/api/attachments/WCCRH37R/fulltext/images/b98507c0091d337c2829d13644127a108cc2d4805f0b7ae50617be837871315a.jpg)  
(b) Visiting time: 5 p.m.  
Figure 15. Example tours with different visiting time.

The experiment results show that our proposed method outperforms the Markov-Topic method in terms of average score and precision. This is because TRSP recommends tours by areas and considers more features than Markov-Topic. It is shown that these features can be used to improve the precision of TRSP, and TRSP performs better than each of its own variations. The impact of the visiting order of the landmark on precision is greater than that of the popularity, which is greater than that of the ratio of similar users visiting the landmark. Moreover, the example of recommended tours shows that our method can avoid going back and forth on the tour. Finally, our method can recommend tours best fit users’ need according to the types of users and different visiting time. Therefore, TRSP can help users plan their trips and customize a trip for each user.

Although we collect the dataset from San Francisco in Flickr in the experiment, the proposed framework can be also used for recommending tours of a large geographical region. This is because we recommend tours area by area and take the transportation time between areas into consideration. That is, we just append an area to a candidate tour at a time. Thus, we only need to consider the neighboring areas which are close to the last area of the candidate tour. Also, we design a pruning strategy to remove the redundant tours. In addition, we may use larger areas for recommending tours of a large geographical region. For example, an area may represent a national park or a city. Therefore, the proposed framework can be straightforwardly used for recommending tours of a large geographical region.

The proposed method can enrich the stream of research on tour recommendations in the following aspects. First, although some previous methods have been proposed to recommend tours by using the photos posted in social networks, most of them are not dedicated to resolving the problem of going back and forth on the tours Second, unlike previous methods recommending tours landmark by landmark, our method clusters locations into two layers and recommends tours area by area. Third, we apply LDA to category the hashtags posted by users into landmark topics and use these topics to characterize landmarks and users. Finally, our method considers more features than previous methods, namely the popularity of landmark, the ratio of similar users visiting the landmark, the time duration of an area, and the visiting time of an area.

The findings may also provide the travelers and tour providers several managerial implications. First, the proposed framework can help travelers plan their trips. Next, by analyzing travelers behavior, we may know what kind of tours best fit travelers’ interest. With this information, we could adjust the recommendation system to improve the performance and users’ experience. Furthermore, tours providers may use our framework to advertise some suitable tours to users.

Our proposed method mines user-generated contents posted by users to recommend tours. Thus, the mining results may depend on the dataset collected and may be biased by the dataset. For example, users of a specific social network can represent only a fraction of the true population, or the

# ACCEPTED MANUSCRIPT

data are just come from photos posted by users who have cameras or cell phones. However, it’s shown that about 70% of all Facebook activities revolve around photos [34], and the user base of photo sharing social networks increases rapidly [30]. For example, the number of active users in Flickr was 112 million in June 2015 [28]. Also, the number of active users in Instagram was 100 million in 2013, and 600 million in 2016 [30]. The percentage of population used Instagram in the U.S. was 27.6% in 2016 [29]. The demographics in Facebook, Instagram and Flickr are close to each other [33], which are also close to that of the U.S [27]. Moreover, the number of smartphone users was 2.1 billion worldwide and 207 million in the U.S. in 2016 [31]. Thus, people can easily access smartphones to take photos and get them posted. More and more people share their photos in online social networks. The more photos shared in online social networks, the less effect of bias. Although we use the dataset collected from Flickr to recommend tours, it is straightforward to applying the proposed framework to the datasets collected from the other photo sharing social networks since most shared photos contain timestamps, geotagged locations, and hashtags. Thus, we may also collect the datasets from multiple photo sharing social networks and consolidate these datasets together, and then use the consolidated datasets to recommend tours, which may reduce the bias. On the other hand, one may concern the issue of copyright for collecting and using photos from different social networks. Therefore, the use the Copyright Act [32].

In the future, we may extend our framework in the following directions. First, to improve the framework that can meet various users’ need, we may consider more constraints, such as tour budget, cost of visiting a landmark or an area, number of POIs to be visited in an area, users' ages and genders, and the structure of users’ ages and genders if the users plan a trip as a group. Second, we may extend our framework to allow users to specify the ending location or a set of locations to be visited. Third, our framework may be extended to consider more features of locations, such as visiting seasons. Finally, we may collect more datasets to evaluate the performance of the proposed framework and improve the framework so that users have more flexibility to plan their trips in near future.

## Acknowledgments

The authors are grateful to the anonymous referees for their helpful comments and suggestions. This research was supported in part by the Ministry of Science and Technology, Republic of China under Grant No. MOST 103-2410-H-002-109-MY3 and MOST 106-2410-H-002-MY3.

## References

[1] R. Arora, and B. Ravindran, Latent Dirichlet allocation based multi-document summarization, Proceedings of the Second Workshop on Analytics for Noisy Unstructured Text Data, pages 91–97, 2008.

[2] D. M. Blei, A. Y. Ng, and M. I. Jordan, Latent Dirichlet allocation, Journal of Machine Learning Research, Vol. 3, pages 993–1022, 2003.

[3] K. R. Canini, L. Shi, and T.L. Griffiths, Online inference of topics with latent Dirichlet allocation, Proceedings of the Twelfth International Conference on Artificial Intelligence and Statistics, pages 65–72, 2009.

[4] D. Crandall, L. Backstrom, D. Huttenlocher, and J. Kleinberg, Mapping the world’s photos, Proceedings of the 18th International Conference on World Wide Web, pages 761–770, 2009.

[5] Y. Cheng, Mean shift, mode seeking, and clustering, IEEE Transactions on Pattern Analysis and Machine Intelligence, Vol. 17, No. 8, pages 790–799, 1995.

[6] Q. Hao, R. Cai, X. Wang, J. Yang, Y. Pang, and L. Zhang, Generating location overviews with images and tags by mining user-generated travelogues, Proceedings of the 17th ACM International Conference on Multimedia, pages 801–804, 2009.

[7] H.P. Hsieh, C.T. Li, and S.D. Lin, Exploiting large-scale check-in data to recommend time-sensitive routes, Proceedings of the ACM SIGKDD International Workshop on Urban Computing, pages 55–62, 2012.

[8] R. Ji, Y. Gao, B. Zhong, H. Yao, and Q. Tian, Mining Flickr landmarks by modeling reconstruction sparsity, ACM Transactions on Multimedia Computing, Communications, and Applications, Vol. 7S, No. 1, pages 31.1–31.22, 2011.

[9] R. Krestel, P. Fankhauser, and W. Nejdl, Latent Dirichlet allocation for tag recommendation, Proceedings of the Third ACM Conference on Recommender Systems, pages 61–68, 2009.

## ACCEPTED MANUSCRIPT

[10] T. Kurashima, T. Iwata, T. Hoshide, N. Takaya, and K. Fujimura, Geo topic model: Joint modeling of user’s activity area and interests for location recommendation, Proceedings of the Sixth ACM International Conference on Web Search and Data Mining, pages 375–384, 2013.

[11] T. Kurashima, T. Iwata, G. Irie, and K. Fujimura, Travel route recommendation using geotags in photo sharing sites, Proceedings of the 19th ACM International Conference on Information and Knowledge Management, pages 579–588, 2010.

[12] T. Kurashima, T. Iwata, G. Irie, and K. Fujimura, Travel route recommendation using geotagged photos, Knowledge and Information Systems, Vol. 37, No. 1, pages 37–60, 2013.

[13] J.S. Liu, The collapsed Gibbs sampler in Bayesian computations with applications to a gene regulation problem, Journal of the American Statistical Association, Vol. 89, No. 427, pages 958–966, 1994.

[14] S. Lloyd, Least squares quantization in PCM, IEEE Transactions on Information Theory, Vol. 28, No. 2, pages 129–137, 1982.

[15] E.H.C. Lu, C.Y. Chen, and V. S. Tseng, Personalized trip recommendation with multiple constraints by mining user check-in behaviors, Proceedings of the ACM 20th International Conference on Advances in Geographic Information Systems, pages 209–218, 2012.

[16] D. Mimno, H.M. Wallach, E. Talley, M. Leenders and A. McCallum, Optimizing semantic coherence in topic models, Proceedings of Conference on Empirical Methods in Natural Language Processing, pages 262–272, 2011.

[17] A. Popescu, and G. Grefenstette, Deducing trip related information from Flickr, Proceedings of the 18th International Conference on World Wide Web, pages 1183–1184, 2009.

[18] A. Popescu, and G. Grefenstette, Mining user home location and gender from Flickr tags, Proceedings of the Fourth International AAAI Conference on Weblogs and Social Media, pages 307–310, 2010.

[19] L. Santos, J. Coutinho-Rodrigues, and C.H. Antunes, A web spatial decision support system for vehicle routing using Google Maps, Decision Support Systems, Vol. 51, No. 1, pages 1–9, 2011.

[20] S. Sra, and I. S. Dhillon, Generalized nonnegative matrix approximations with Bregman divergences, Proceedings of International Confrence on Advances in Neural Information Processing Systems, pages 283–290, 2005.

[21] C.Y. Tsai, and S.H. Chung, A personalized route recommendation service for theme parks using RFID information and tourist behavior, Decision Support Systems, Vol. 52, No. 2, pages 514–527, 2012.

[22] W. Wang, H. Yin, L. Chen, Y. Sun, S. Sadiq, and X. Zhou, Geo-SAGE: A geographical sparse additive generative model for spatial item recommendation, Proceedings of the 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pages 1255–1264, 2015.

[23] L.Y. Wei, Y. Zheng, and W.C. Peng, Constructing popular routes from uncertain trajectories, Proceedings of the 18th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pages 195–203, 2012.

[24] H. Zhang, M. Korayem, D. J. Crandall, and G. Lebuhn, Mining photo-sharing websites to study ecological phenomena, Proceedings of the 21st International Conference on World Wide Web, pages 749–758, 2012.

[25] C. Zhang, H. Liang, K. Wang, and J. Sun, Personalized trip recommendation with POI availability and uncertain traveling time, Proceedings of the 24th ACM International on Conference on Information and Knowledge Management, pages 911–920, 2015.

[26] V. W. Zheng, Y. Zheng, X. Xie, and Q. Yang, Collaborative location and activity recommendations with GPS history data, Proceedings of the 19th International Conference on World Wide Web, pages 1029–1038, 2010.

[27] Demography of the United States, Wikipedia, https://en.wikipedia.org/wiki/Demography\_of\_the\_United\_States.

[28] Hot company: how many people use Verizon products, Expandedramblings, http://expandedramblings.com/index.php/hot-company-many-people-use-verizon-products-yah oo-aol-flickr-tumblr.

[29] Instagram penetration rate in the United States, Statista, https://www.statista.com/statistics/293778/us-instagram-penetration.

[30] Number of monthly active Instagram users, Statista, https://www.statista.com/statistics/253577/number-of-monthly-active-instagram-users.

[31] Number of smartphone users worldwide, Statista, https://www.statista.com/statistics/330695/number-of-smartphone-users-worldwide.

[32] Subject matter and scope of copyright, http://www.copyright.gov/title17/92chap1.html#107.

[33] The demographics of social media properties: Looking beyond downloads, Vertoanalytics, http://www.vertoanalytics.com/the-demographics-of-social-media-properties-looking-beyond-d ownloads.

[34] The growing importance of digital photo sharing to brands, Qubemedia, http://qubemedia.net/social-media/rise-photographs-social-media.

# ACCEPTED MANUSCRIPT

Chih-Yuan Sun received BBA and MBA degrees in Information Management from National Taiwan University, Taiwan, R.O.C. She will work on her ME degree in Computer Science, Cornell University. Her current research interests include data mining, social media analysis, knowledge management and business intelligence.

Anthony J.T. Lee received a BS in Information Engineering and Computer Science from National Taiwan University, Taiwan, R.O.C, and a Ph.D. degree in Computer Science from University of Illinois at Urbana-Champaign, USA, respectively. He joined the Department of Information Management, College of Management, National Taiwan University and he is now a professor. His papers have appeared in Pattern Recognition, Pattern Recognition Letters, Information Systems, Journal of Systems and Software, Information Sciences, Data and Knowledge Engineering, Expert Systems with Applications, Journal of Information Management, ACM Transactions on Management Information Systems, Decision Support Systems, etc. His current research interests include data mining, knowledge management, decision support systems, business intelligence, information economics, and business modeling. He is a member of INFORMS, ACM and IEEE.
