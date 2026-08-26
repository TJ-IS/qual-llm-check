---
otero_id: 13538
otero_key: "VD9QZNYK"
title: "The crowd against the few: Measuring the impact of expert recommendations"
authors: "Nils Herm-Stapelberg; Franz Rothlauf"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113345"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The crowd against the few: Measuring the impact of expert recommendations

![](/api/attachments/VD9QZNYK/fulltext/images/28fd00155600ac0bf283e0eae117d009538ccfd6e0d2a821968d58bf42164385.jpg)

Nils Herm-Stapelberg<sup>⁎</sup>, Franz Rothlauf

Gutenberg School of Management and Economics, Johannes Gutenberg-University Mainz, Jakob-Welder-Weg 9, 55128 Mainz, Germany

## A R T I C L E I N F O

Keywords: recommender system filter bubble experts user behavior diversity

## A B S T R A C T

A large amount of research on recommender systems has focused on improving the accuracy of suggestions in ofline settings. However, this focus and the commonly used techniques can lead to a “filter bubble”, severely limiting the diversity of content discovered by users. Several ofline studies show that this can be mitigated by using experts for recommendation. In contrast to standard recommender systems, experts are able to generate more diverse recommendations and increase the novelty of given suggestions. They can be used in missing-data or cold-start scenarios and reduce noise in the users' ratings. This paper examines the impact of employed experts' recommendations on user behavior for a real-world recommender system on a popular video-on-demand website, provided by a large television network. We study whether the potential benefits of experts lead to diferences in user behavior, user perceptions and properties of given recommendations (e.g., diversity). We find that enriching a state-of-the-art system with the suggestions of employed experts can significantly increase platform use. Even though expert recommendations are used less frequently and are less successful than expected, users watch a greater number of clips, use more recommendations, and come back to the website more frequently when they receive expert suggestions. When searching for other influencing factors, we find that experts generate more diverse recommendations and improve the taste coverage of the system keeping user satisfaction unafected. In summary, our results show large benefits of using employed experts and have implications for the design and use of recommender systems in real-world scenarios.

## 1. Introduction

Online websites often feature a massive amount of available content and services, which makes it dificult for users to decide for a specific product. Recommender systems are built to reduce this information and to weaken the decision possibility overload problem [8,40]. They are used in many diferent areas such as e-commerce, video-on-demand services, social networks, or scientific publishing websites. These sys tems suggest possible relevant products based on the assumed preferences of a user. Recommendations are commonly generated using content similarities to previously consumed items (content-based filtering) or the preferences of similar other users (collaborative filtering) [8,17].

A large amount of research on recommender systems has focused on optimizing the accuracy of the systems' recommendations [1]. More precisely, studies have centered on optimizing prediction accuracy, measured by the deviation of predicted ratings to actual given ratings of products (e.g., Root Mean Squared Error), and classification accuracy, measured by, e.g., Precision (i.e., the share of useful recommendations compared to all recommendations). This is, in general, a favorable goal since more accurate predictions should lead to more satisfied customers. However, accuracy should not be the only quality indicator that recommender systems should strive to improve [31]. Studies show that evaluating the quality of a system is much more complex and can be done from diferent angles [17,32]. For example, recommendations can be assessed by measuring how well they cover the interests of users (taste coverage), or whether they ofer diverse content (diversity) [16,17,41]. Diversity in particular can lead to increased satisfaction [23,39] and have a positive economic benefit for the system provider.

Several scholars argue that content-based and collaborative-based recommender systems often severely limit the diversity of content that is presented to users, placing them in a “filter bubble” [10,12,33]. “Filter bubble” describes the phenomenon that users only discover and consume a very limited area of the available content, never experiencing content which the recommender system rates as inappropriate for the user. The implications of the “filter bubble” can be manifold. Eli Pariser [35] argues that this can lead to heavy biases in perceptions in all sorts of areas (e.g., news consumption, search results) without the user even being aware of the influence of the system. For example, in the context of recommender systems, users of a video-on-demand service who liked several action movies would only receive recommendations for more action movies, or suggestions of movies enjoyed by other users who also liked action movies. Because of this, they might miss out on large parts of the available content, or their radical views could be increasingly reinforced [34]. Consequently, Knijnenburg et al. [20] argue that recommender systems should in general focus on “self-actualization”, i.e., helping users to discover their own, diverse interests with the help of the system, rather than having their current behaviors reinforced.

Studies show that the quality (e.g., accuracy, diversity) of recommendations can be increased by using experts [5,28,37,43]. Experts are people that have a richer knowledge of a domain than the average user, and are therefore expected to provide better recommendations. These experts can be identified from the regular user population (through their user activity), or can be experts actively working in a certain industry. Additionally, they can be directly involved in the recommendation process (as in this study), or their knowledge can be indirectly used (e.g., by using their publicly-available reviews and recommendations). Experts could potentially be used to break the “filter bubble”, i.e., to increase the diversity of content and improve exploration rather than reinforce users' taste - all while maintaining or increasing accuracy. So rather than using the entire user population (collaborative filtering) or the available metadata on products or mo vies (content-based filtering) to generate recommendations, experts could be used. However, to our knowledge, there is no large-scale online controlled study that examines the impact of using professional employed expert suggestions on user behavior, or on recommendation properties (e.g., recommendation diversity).

This paper studies the impact of expert recommendations on parti cipants' platform use by deploying a live, real-world recommender on a video-on-demand website and recruiting participants from the website's regular user population. We examine whether the theoretic advantages of experts can actually be realized in a real-world scenario. More pre cisely, this study measures the influence of expert suggestions on clip views, platform visits, recommendation use, return rate and retain rate. Although expert recommendations are used less than expected, users who receive not only system-generated but also expert recommendations watch a greater number of clips (+9.8%), visit the platform more frequently (+9.0%), and use more recommendations (+17.1%). Thus, the pure presence of expert recommendations increases the number of views although the expert recommendations shown to the user seem to be less successful than system-generated recommendations. Consequently, we study the properties of the given recommendation and find that expert recommendations have higher diversity and taste coverage in comparison to system-generated recommendations.

## 2. Related work

The concept of expert recommendations relies on the specific knowledge of domain experts to provide suggestions for users. Various types of experts are used to improve properties of recommender sys tems. Studies show that experts can increase the accuracy of re commendations across diferent application domains. Sha et al. [37] identified expert users in a mobile application that recommends “cool” pictures of places and objects. They defined “trend makers” and “trend spotters” as special cases of users that provided better recommendations than those of the entire user population. Using location-based social networks, Bao et al. [5] identified local experts for travel recommendations. Local experts are users that have a rich history of activities in a certain geographical area, which leads to the assumption that they have more knowledge of activities and attractions worth a visit than a regular user does. To generate a recommendation, the profiles of these local experts were compared to a specific user. Yun et al. [43] gathered information from Rotten Tomatoes,<sup>1</sup> which also contains ratings from experts. By combining these expert opinions with a collaborative filtering approach, they are able to improve the accuracy of their recommendations compared to a standard collaborative recommender. Similar to this, Cho et al. [11] also combined collaborative filtering with expert opinions in the context of movie recommendations. They used active system users of a certain content category as experts instead of online ratings of outside experts. Lin et al. [26] obtained similar results by combining content-based, collaborative, and expert recommenders for personal news recommendations. The performance measures used difered between these studies, covering most of the common accuracy evaluation indicators such as classification accuracy (e.g., precision) and prediction accuracy (e.g., root mean squared error). All of these studies showed significant accuracy improvements when using experts to generate recommendations.

In addition to increasing recommendation accuracy, expert recommenders can be used to improve the diversity of generated suggestions. Diversity can, e.g., be measured by the amount of dissimilarity in a list of recommendations [22,47] or the amount of lesser known, i.e., less frequently rated items [28]. Liu et al. [28] showed that very active users with a higher knowledge of available content can be used to define a set of seed items, which could be used for preference elicitation of new users. This approach increased the diversity of recommendations compared to diferent baseline methods, tested on the Netflix, Movielens and Last.FM datasets. Diversity has also been studied in non-expert contexts and it has been shown that users appreciate more diverse recommendations to simply accurate ones [23,32,38].

Other quality indicators of recommender systems are novelty and serendipity. Novelty describes whether a recommendation is previously unknown to a user [17]. It is sometimes used synonymously to serendipity. Using the definition of Kotkov et al. [22], serendipity also includes the perception that a recommendation is surprising, i.e., users would have not found this item on their own (unexpectedness). It also includes the accuracy of the recommendation, i.e., it is relevant to the user. The average popularity of items in a list, i.e., the relative number of ratings or views, can be used as a novelty measure since a lesserknown item is more likely to be novel to a user than a widely-recognized one [7]. Since unexpectedness or serendipity also cover the rather subjective feeling of surprise, they are often assessed by directly asking users [22]. In Lee and Lee [24], experts are identified within the general user population in the domain of music recommendations. Experts are defined as users who have a rich history of interaction with the respective platforms. These experts are better able to generate recommendations that are novel and surprising than the average user.

Another property of recommendations is coverage. Coverage can describe diferent concepts: It can describe the share of items a system is able to make suggestions for or the share of items that are actually recommended. These are defined as “prediction coverage” and “catalogue coverage”, respectively [15,42]. Third, coverage can also refer to the share of diferent user interests that can be covered by a recommender system (i.e., “taste coverage”) [41]. In a study by Zafar et al. [44], the posts of topic experts (identified by, e.g., their activity and connections to other users) were used to recommend news stories in an ofline experiment on Twitter. Expert recommendations covered more than 90% of the important topics. Even though the crowd performed similar, a lot fewer tweets of experts were needed to reach this level.

Table 1 summarizes the properties of the existing studies and compares them to the study at hand. Most relevant, the study at hand performs an online randomized controlled real-world experiment, whereas most previous approaches perform an ofline evaluation. Per forming an online experiment allows us to directly observe user behavior and use behavior-related measures such as the amount of consumed items. Additionally, the study at hand uses the knowledge of professional experts directly (compare Sect. 3) rather than crawling user opinions without any active involvement of experts in the recommendation process or experts promoted from the regular user population.

Overview of Expert Recommendation Approaches (MAE = mean absolute error, MAP = mean absolute precision, RMSE = Root Mean Squared Error, RCT = randomized controlled trial. All RS approaches include experts).

<table><tr><td>Study</td><td>Study type</td><td>Experts</td><td>Domain</td><td>RS approach</td><td>Measures</td></tr><tr><td>[3]</td><td>Offline, Lab Experiment</td><td>Professionals, passive</td><td>Movie</td><td>Collaborative</td><td>MAE, coverage, precision, user perception</td></tr><tr><td>[5]</td><td>Offline</td><td>User Experts</td><td>Tourism</td><td>Collaborative, context-aware (location)</td><td>Precision, recall</td></tr><tr><td>[11]</td><td>Offline</td><td>User Experts</td><td>E-commerce</td><td>Collaborative</td><td>MAE, coverage, precision, recall, F1</td></tr><tr><td>[24]</td><td>Offline</td><td>User Experts</td><td>Music</td><td>Collaborative</td><td>Precision, recall, novelty</td></tr><tr><td>[26]</td><td>Offline</td><td>User Experts</td><td>News</td><td>Content, collaborative, social</td><td>RMSE</td></tr><tr><td>[28]</td><td>Offline</td><td>User Experts</td><td>Movie &amp; music</td><td>Collaborative</td><td>Coverage, diversity, precision, MAP, AUC</td></tr><tr><td>[37]</td><td>Offline</td><td>User Experts</td><td>Pictures</td><td>Collaborative</td><td>Precision, recall</td></tr><tr><td>[43]</td><td>Offline</td><td>Professionals, passive</td><td>Movie</td><td>Collaborative, demographic</td><td>MAE</td></tr><tr><td>[44]</td><td>Offline</td><td>User Experts &amp; Professionals, passive</td><td>Microblogs</td><td>Only experts</td><td>Compactness, relevance, coverage</td></tr><tr><td>This study</td><td>Online (RCT)</td><td>Professionals, active</td><td>Movie</td><td>Content, collaborative</td><td>User behavior, user perceptions, diversity, taste coverage, satisfaction</td></tr></table>

## 3. Study design

To test the efects of expert recommendations, we used an available commercial system that utilizes several standard recommendation techniques and modified it to incorporate the recommendations of experts in the context of an online video-on-demand service. The platform is operated by a popular television network and has more than one million visitors per month. It currently features more than 100,000 available clips so that the amount of content provided presents an information overload problem which makes a recommender system highly valuable. The platform ofers a wide variety of content, from entertainment movies and series to documentaries and news. There are also items related to sports events or content for children. It is free to use and does not require visitors to sign-up to use the service.

The used experts are employed professionals who are responsible for and work with the content of the video-on-demand platform on a daily basis. Therefore, they have in-depth knowledge of the available clips and are able to suggest high-quality items even for niche interests.

As in most real-world applications, the recommendations given on the landing page of a website are diferent from those on the individual items' webpages. For example, amazon generates many diferent sug gestions based, $\mathbf { e . g . , }$ on previous purchases or visited webpages on the landing page. However, on an individual product website the recommendations are not based on the complete profile of a user, but rather on the current context, i.e., the currently viewed product (e.g., amazon: “Customers who bought this, also bought”). Analogously, in our study, recommendations were shown on the landing page as well as on every individual clip webpage.

## 3.1. Landing page recommendations

On the landing page, personalized recommendations are calculated based on the user's entire view history. They are a mixture of two recommender systems that use diferent well-known recommendation techniques. The first uses a Naive Bayes classifier. Naive Bayes assumes independence of all classification features. Given a set of item features, the probability that an item belongs to a class depends on 1) the like lihood that a feature is present in a certain class, 2) the likelihood of this class and 3) the likelihood of the given features [25,46]. For n features, the probability that an item belongs to class $C _ { i }$ is calculated as

$$
p (C _ {i} \mid f _ {1},..., f _ {n}) = \frac {p (C _ {i}) \prod_ {j = 1} ^ {n} p (f _ {j} \mid C _ {i})}{p (f _ {1} , . . . , f _ {n})},\tag{1}
$$

where $C _ { i }$ denotes class i (e.g., “recommended”, “not recommended”), $p$ (C ) is the overall probability of class $C _ { i } ( \mathrm { p r i o r } ) , f _ { 1 } , . . . , f _ { n }$ are the features of an item, $p ( C _ { i } | f _ { 1 } , . . . , f _ { n } )$ is the probability that an item belongs to class $C _ { i }$ given features $f _ { 1 } , . . . , f _ { n }$ (posterior), p(f<sub>j</sub>| C<sub>i</sub>) denotes the likelihood of feature $f _ { j }$ given class $C _ { i } ,$ and $p ( f _ { 1 } , . . . , f _ { n } )$ is the probability of the given features of an item (evidence). Individual models are built for every user using the available metadata on the items and previously watched clips. Available metadata includes the category, publisher, length and recency of the clip as well as the channel of the tv network where the clip first aired and whether the clip was classified to target young adults. This Naive Bayes classifier is part of the probabilistic family of content-based recommender (compared to, e.g., keyword-based models) [8]. Previous research suggests Naive Bayes to be a high performing method of that class [25].

The second recommender uses a k-nearest-neighbor approach to calculate users that are similar to the current user. One of the common techniques to define the nearest neighbors is cosine similarity. Users are modeled as vectors that contain information on their previously con sumed items (i.e., the rating assigned to each item). Cosine similarity calculates the angle between the two vectors of two users for every user combination in the dataset (building an m x m matrix, where m is the number of users) as

$$
\cos \Bigl (\overrightarrow {a}, \overrightarrow {b} \Bigr) = \frac {\overrightarrow {a} * \overrightarrow {b}}{| | \overrightarrow {a} | | | | \overrightarrow {b} | |},\tag{2}
$$

where $\vec { a }$ and $\xrightarrow [ b ] { }$ are vectors of users a and b that contain the previously watched clips (i.e., their rating). A user's recommendations are the previously watched clips of those users with the k-highest similarity values. Therefore, this technique can be classified as a collaborative recommender. Collaborative filtering is the most widely-used recommendation approach in the literature and also commonly used in the industry [14]. There are many diferent similarity measures for collaborative filtering based recommendations available in the litera. ture, however (weighted/adjusted) cosine-similarity is the most popular one [9,30,45].

We combine the recommendations of these two recommenders with expert recommendations. Since even a larger group of experts would be unable to provide personal recommendations for every individual user, experts define lists of clips they deem worthy of recommendation, in each of the available categories (e.g. comedy). More precisely, they hand-pick at least 20 diferent clips for each category and update the lists multiple times a day. Each expert is able to add as well as remove clips from every list. This design ensures that the specific knowledge of the employed experts is properly used and generates recommendations that can be used for many users without the need of tailoring the sug gestions to each individual user. For thousands of users, user-specific recommendations would not be possible due to time and efort constraints of the experts.

For the recommendations shown to the user, we randomly choose expert recommendations from the lists and mix them with the systemgenerated suggestions. To make sure that some of the visible re commendations presented to users are from experts, about half of the shown recommendations are expert suggestions. This is done to avoid biases due to the positioning of expert recommendations on a web site since users often use only the very first suggestions and ignore most of the rest, e.g., when using search engines $[ 6 , 1 9 ]$ . In our setting, there i no notable diference in the presentation of recommendations to avoid further behavioral biases.

We combine the diferent techniques to mitigate drawbacks of each technique. The most common issue in collaborative filtering is the “new-item problem” [18,25]. Newly released items do not have many user ratings available and would therefore not be recommended. They would be integrated slowly into the recommendation process and only if users deliberately search for these items or discover them in other ways (e.g., through promotions). Content-based filtering does not need an item to be rated by any user since it could still recommend a new item based on its metadata and similarity to previously consumed clips. Content-based filtering, however, enforces filter bubbles (sometimes called “overspecialization problem”) since it does not allow recommendations outside of the already consumed content categories of a user $[ 1 0 , 1 2 ]$ . Since collaborative filtering is not based on any content information of the clips, it is able to recommend from other categories, increasing the coverage of diverse tastes (even though it is still restricted to similar users). Both approaches also sufer from the “new user problem”, since it is dificult to generate suggestions for users with a small history of consumption. Experts, however, could still recommend high-quality content even for new users, since they have extensive knowledge of the available catalogue and can suggest clips for niche interests [3,26,28].

## 3.2. Clip page recommendations

In contrast to the landing page recommendations, the recommendations given on the individual clip pages are based on the currently-watched clip, rather than the full viewing history of a user. Three diferent recommenders determine suggestions using diferent approaches, which are then combined with expert recommendations.

The first recommender calculates similarities between items based on a weighted cosine similarity that utilizes available data on the potential clips. The n features include the category of the clip (e.g., comedy), the channel of the tv network, the producer, the clip length and its recency (in days, since its oficial release). The similarity is calculated as

$$
w c o s \Big (\overrightarrow {c}, \overrightarrow {d} \Big) = \frac {\sum_ {i = 1} ^ {n} c _ {i} * d _ {i} * \omega_ {i}}{\sqrt {\sum_ {i = 1} ^ {n} c _ {i} * \omega_ {i}} * \sqrt {\sum_ {i = 1} ^ {n} d _ {i} * \omega_ {i}}},\tag{3}
$$

where $\vec { c }$ and $\vec { d }$ are vectors of items c and d that contain the n features of each item. The assigned weight of feature i is denoted by $\omega _ { i } .$ Since the recommender is based on similarities between items based on their metadata, it can be classified as a content-based recommender [8]. As mentioned before, (weighted) cosine similarity is a commonly used approach to calculate similarities between users or products in recommender systems [9,30,45].

The second recommender generates suggestions by using an itemitem collaborative filtering algorithm, similar to amazon's “Customers who bought this, also bought”. Item-item collaborative filtering works by computing similarities between items. However, the similarity is not based on the metadata of an item (as for the content-based recommender), but on the behavior of users. For example, it multiple users give a rating of 5 stars to both products $P _ { 1 }$ and $P _ { 2 } ,$ then item-item collaborative filtering considers the two products $P _ { 1 }$ and $P _ { 2 }$ to be similar to each other. The similarity calculation can again be done by using weighted cosine similarity. One major advantage of item-item collaborative filtering is that the necessary similarity matrix can be calculated ofline without requiring the current user as context. Thus, this approach can also be used on larger platforms that feature many users and products (as in our case), is therefore commonly used in the industry, and shows high performance in, $\mathrm { e . g . , }$ , e-commerce or video-ondemand scenarios [17,27].

Nevertheless, it is possible that the collaborative filtering recommender is not able to generate a recommendation $( \boldsymbol { \mathrm { e . g . } } ,$ , if the clip has not been watched before). If, in addition, there is also no or only little metadata available for this clip, the similarity-based system is also not able to generate a recommendation. In these cases, we use a third recommender that utilizes keywords. The recommender just searches a keyword database to find clips with similar keywords. This recommender works like a content-based recommender as its results depend on the properties of the clips.

Analogously to the landing page, we mix expert recommendations to the system-generated recommendations. We randomly choose clips from the expert recommendation list that match the overall category of the current context (i.e., the currently watched clip).

## 3.3. Data collection

We applied the recommender system to the online video-on-demand service of the large television network. Regular users of the video-ondemand website received a pop-up, that briefly explained that the platform developed a new recommendation system and they had the chance to evaluate it. The explanation did not give any details on how the recommendations were generated or the fact that experts were involved. We recruited a total of 6374 users that voluntarily opted to participate in the study. Many of the recruited users never used the platform after registering for the study and 11 users had to be removed from the data due to technical dificulties (e.g., users were accidentally assigned to both groups). This left us with a total of 2715 users in the dataset.

There were no monetary or other incentives provided. Users who decided to participate were only asked for a valid e-mail address and a password to avoid selection biases since requiring more information could have scared privacy-sensitive users. In addition, since users did not know what exactly was tested or that experts were involved, we do not believe that privacy issues played a role in this study [4]. However, the participants could optionally provide additional information, such as age, gender, and location. 1875 participants disclosed their age (69.1%), 2000 their gender (73.7%) and 1771 (65.2%) their location. Tables 2 and 3 give an overview of the age and gender distribution. The users' locations were representative of the population distribution across the observed country. The numbers indicate that we have a heterogeneous user base with respect to gender and across age groups. Only children and young teenagers were excluded since they are not allowed to participate due to legal and ethical considerations.

In our study, we randomly assigned users to one of two groups: the treatment group received recommendations as described in Sects.3.1 and 3.2 including expert recommendations. In contrast, the control group did not receive any suggestions that were made by experts. They only received system-generated suggestions. This design allows us to examine the impact of using employed professionals for recommendation. Besides not using experts in the control group, there were no other diferences between the two groups.

Table 2  
Overview of Participants' Age.

<table><tr><td>Age</td><td>18–25</td><td>26–35</td><td>36–45</td><td>46–55</td><td>56–65</td><td>66–75</td><td>&gt; 75</td></tr><tr><td>Count</td><td>128</td><td>328</td><td>330</td><td>484</td><td>410</td><td>168</td><td>27</td></tr></table>

Table 3  
Overview of Participants' Gender.

<table><tr><td>Gender</td><td>Male</td><td>Female</td><td>Other / Not disclosed</td></tr><tr><td>Count</td><td>952</td><td>1048</td><td>715</td></tr></table>

To reduce biases in user behavior, users had no knowledge of what exactly was being tested and what experimental group they belonged to (and how the recommendations were generated) [2]. The platform's interface and available content was identical to the regular platform that people were used to, except for the provided recommendations. The recommendations were presented in a horizontal list showing eight recommended clips which was modeled of other lists that were previously used on the platform in order to reduce discovery efects and make it easier for everyone to use the platform. Because of the very diverse user base, sudden changes could have resulted in selection biases since, e.g., not-computer-savvy users could have had problems using the website and subsequently dropped out.

Since some users wanted to explore what was new in the study in comparison to the regular platform, they clicked through many clips and websites after registering. To account for these “discovery” or “novelty” efects [36], we only used data starting two weeks after the initial registration period. Besides removing discovery efects, this also further mitigated “cold start” issues (see section 3.1 for details on the new-item and new-user problem). Experts can help mitigate cold-start issues since they have typically rated or consumed many diferent items, are motivated to explore new ones, and have extensive knowledge of the catalogue [3,26,28]. They are able to recommend clips to users even if the clip hasn't been viewed by a user before or if there is no metadata available. Since we only use data starting from the third week, we have some data on users' previous viewing behavior available. Additionally, we showed a banner on the landing page to completely new users, to indicate that recommendations would only be shown if they interact with the platform. We asked users how long it took to no longer see this banner and over 95% indicated that it was gone within the first week. Therefore, we assume that cold-start issues did not have an influence on the study's results.

We collected two types of data from the user: First, we recorded the clickstreams of users' interactions with the website over a period of 10 weeks. This led to 617,194 total interactions. An interaction is every click a user makes on the platform, e.g., on a search button, on a video clip, or on a recommendation. Of those 617,194 interaction, 87,357 were clicks on a video clip. Recommendation are responsible for 7270 of the watched clips. Second, we conducted a post-study questionnaire. The questionnaire was sent out after the 10 week study period and we received a total of 3560 responses. 1351 of those had to be removed because of incomplete answers, failed control questions or because users were inactive during the study period. This left us with a total of 2209 questionnaires for validation and analysis.

## 4. Results

Using experts in the context of recommender systems yields many advantages that have been extensively tested in ofline settings, but not in a large-scale online study. There is only little knowledge of the actual impact of expert recommendations on user behavior. Therefore, we analyzed the clickstreams to assess the impact of expert suggestions on the number of watched clips, the number of total visits and the number of recommendations used (Sect. 4.1). Sect. 4.2 examines how often recommendations of a certain type (e.g., expert, collaborative, contentbased) were used by the participants, in order to evaluate the success of diferent recommendation algorithms. Finally, Sect. 4.3 studies whether users that click on a recommendation continue clicking on other recommendations.

## 4.1. User behavior

Since standard accuracy measures can only be used in ofline tests and are not valid for online tests, we studied user behavior in our study and examined whether recommendations were used more often in one of the groups. A higher use of recommendations would indicate higher accuracy since users are expected to use those suggestions more that better fit their individual preferences. Consequently, we study the total clips watched, the number of visits, the number of visits where at least one (active visits) or multiple (multiclip visits) items were consumed as well as the number of clicks on recommendations (rec. clicks). Additionally, we measured the return rate, i.e., how often a user i returns to the platform as

$$
R e t u r n R a t e _ {i} = \frac {V i s i t e d D a y s _ {i}}{S t u d y D u r a t i o n}\tag{4}
$$

and the retain rate, i.e., the percentage of users that still use the platform at the end of the study period as

$$
R e t a i n R a t e = \frac {L W U _ {\mathrm{g}}}{T U _ {\mathrm{g}}},\tag{5}
$$

where $g$ is one of the two groups (treatment, control), $L W U _ { g }$ is the number of users of group g that visited the platform in the last week of the study (Last Week Users) and $T U _ { g }$ is the total number of users that are in group g (Total Users).

Table 4 compares the numbers for the two groups, where every indicator (except the retain rate) is measured per user. Significance values are calculated by using a non-parametric Mann-Whitney-U test, since normality of distributions cannot be assumed.

We found that the behavior of users in the treatment group (receiving expert and system-generated recommendations) is significantly diferent from the control group (receiving only system-generated recommendations). Users that received expert suggestions watched more clips (33.70 vs. 30.68 clips, +9.84%, W = 880,373, p = 0.045) and visited the platform more often (24.60 vs. 22.58 times, +8.95%, W = 884,334, p = 0.070). They returned on 18.35% of the days in the 10 week study period (compared to only 17.15% in the control group, W = 887,531, p = 0.092) and had more visits where at least one clip was watched (active visits, 18.55 vs. 16.30, +13.80%, W = 881,391, $p = 0 . 0 4 9 )$

We also report how often more than one clip was consumed during a single visit (multiclip visits) and how often recommendations were used (rec. clicks). This is interesting since recommendations are most useful when targeting users that are browsing or have enough time available to consume multiple items. Receiving expert recommendations is associated with a 15.65% increase in multiclip visits (6.06 vs. 5.24, W = 881,985, p = 0.051) and a 17.10% increase in clicks on

## Table 4

Group comparisons. All measures except Retain rate are given per user. Significance cutofs are: $^ { * } 0 . 1 , ^ { * * } 0 . 0 5 , ^ { * * * } 0 . 0 1 .$ . <sup>a</sup> Test statistic of the Mann-Whitney-U test. <sup>b</sup> Since retain rate is a binary outcome per user, Fisher's test is used for the test of group diferences.

<table><tr><td>Measure</td><td>Control Group</td><td>Treatment Group</td><td>Percentage Difference</td><td> $W^a$ </td><td>Significance</td></tr><tr><td>Clips Watched</td><td>30.68</td><td>33.70</td><td>+ 9.84%</td><td>880,373</td><td>0.045**</td></tr><tr><td>Rec. Clicks</td><td>4.62</td><td>5.41</td><td>+ 17.10%</td><td>838,272</td><td>&lt; 0.01***</td></tr><tr><td>Total Visits</td><td>22.58</td><td>24.60</td><td>+ 8.95%</td><td>884,334</td><td>0.070*</td></tr><tr><td>Active Visits</td><td>16.30</td><td>18.55</td><td>+ 13.80%</td><td>881,391</td><td>0.049**</td></tr><tr><td>Multiclip Visits</td><td>5.24</td><td>6.06</td><td>+ 15.65%</td><td>881,985</td><td>0.051*</td></tr><tr><td>Return rate</td><td>0.1715</td><td>0.1835</td><td>+ 7.00%</td><td>887,531</td><td>0.092*</td></tr><tr><td>Retain rate</td><td>0.3662</td><td>0.4211</td><td>+ 14.99%</td><td>b</td><td>&lt; 0.01***</td></tr></table>

recommendations (5.41 vs. 4.62, $W = 8 3 8 , 2 7 2 , p \ < \ 0 . 0 1 )$ . Although our experts have the disadvantage that they can not make personalized recommendations for each user, showing expert recommendations to the users leads to a significantly higher use of the platform.

## 4.2. Algorithm success

We analyzed how often recommendations were clicked by the users that are generated by the diferent types of recommendation algorithms. In particular, we examine whether diferent types of re commendations were clicked more often than expected comparing the observed click rate to the expected probability of a click. For recommendations that are more attractive to the user, the observed click rate is higher; for all recommendations that are less attractive, it is lower.

Consequently, we define the expected probability $p _ { r }$ of a click on a recommendation of type r (we distinguish between recommendation types “expert”, “content similarity”, “item-collaborative” and “keyword” for the clip pages; “expert”, “user-collaborative” and “Naive Bayes” for the landing page) as

$$
p _ {r} = \frac {n s _ {r}}{\sum_ {r} n s _ {r}},\tag{6}
$$

where $n s _ { r }$ is the number of shown recommendations of a certain type r and $\Sigma _ { r } n s _ { r }$ is the total number of shown recommendations from all sources.

We define the diference between the observed percentage of clicks on recommendations of a certain recommender and the expected probability $p _ { r }$ as the “Algorithm Success” (AS) of the recommendation type r:

$$
A S _ {r} = \frac {n c _ {r}}{\sum_ {r} n c _ {r}} - p _ {r},\tag{7}
$$

where nc is the number of clicks on recommendations of type r and ∑ nc is the total number of clicks on recommendations of all types.

Consequently, $A S _ { r } = 0$ indicates that the recommender r performed as expected, a negative value shows that the recommendations of r were clicked less than expected, indicating a poor quality of this recommender. In contrast, a positive value of AS, indicates that the re. commendations of recommender r were clicked more than expected, indicating a good quality of the given suggestions.

Fig. 1 and Table 5 present the results. A value of $+ 0 . 0 5$ indicates that this recommender was used an absolute 5% more often than expected, e.g., 55% of times instead of 50%. For example, we showed 100 recommendation lists to the user, where half of the recommendations were from one recommender. Thus, we expect 50 clicks on recommendations from this particular recommender. If we observe 55 clicks on recommendations from this particular recommender, we have an absolute percentage diference (algorithm success) of 5% (+0.05).

For the recommendations given on the individual clip pages (Fig. 1, left), the recommender r based on content similarity generated recommendations that were clicked significantly more often than expected $( A S ~ = ~ + ~ 0 . 0 7 , ~ + 2 2 . 9 \% )$ In contrast, the expert recommendations were clicked significantly less than expected $( A S ~ = ~ - ~ 0 . 0 7 7 , ~ - 1 8 . 6 \% )$ . The recommendations of the item-based collaborative recommender were also clicked less than expected $( A S = \mathrm { ~ - ~ } 0 . 0 1 9 , \mathrm { ~ - 1 3 . 4 8 \% } )$ . For the recommendations on the landing page, we obtain similar results (Fig. 1, right). Expert recommendations were used slightly less than expected, though not significantly less $( p = 0 . 1 3 )$ . In contrast to the clip page recommendations, collaborative recommendations were clicked more often than expected $( A S = \mathrm { ~ + ~ } 0 . 0 2 2 , \mathrm { ~ + ~ } 3 6 . 8 5 \% )$ . This can be explained as the collaborative recommender used the full profile of a user as context, increasing the available data and making it easier for the recommender to find suitable recommendations. The clicks on the recommendations generated by the Naive-Bayes-based recommender were as expected (AS close to 0).

The results are counter-intuitive, as expert-based suggestions were used less than expected even though the treatment group used the platform significantly more often.

## 4.3. Success of recommendations

Consequently, we study how successful recommendations are. We are interested in how often users that clicked on a recommendation continue clicking on other recommendations. Users will more likely click on other recommendations if the previously used recommenda tions are of higher quality and suit the needs of the user.

In particular, we calculate for users who are in the treatment group (they see a mix of expert and system-generated recommendations) and who click on one recommendation (either expert or system-generated) the probability $P _ { a l l } { } ^ { t r e a t m e n t }$ that these users click on another recommendation. Furthermore, we calculate for users who are in the treatment group and who click on one expert recommendation, the probability $P _ { e x p e r }$ <sup>treatment</sup> that these users click on another re- t commendation. For comparison, we calculate for all users who are in the control group (they only see system-generated recommendations) and who have clicked on one (system-generated) recommendation, the probability ${ P _ { a l l } } ^ { c o n t r o l }$ that these users click on another recommendation.

![](/api/attachments/VD9QZNYK/fulltext/images/d874957471015039c4a4b9821ac8eba57ad0d18fc1bace57edfe99dd57106bd2.jpg)  
Fig. 1. Algorithm Success of all recommender by page type (individual clip page vs. landing page of the platform).

Table 5  
Algorithm success. Significance cutofs are: $^ { * } 0 . 1 , ^ { * * } 0 . 0 5 , ^ { * * * } 0 . 0 1$

<table><tr><td>Recommender</td><td>Page</td><td>Expected Share</td><td>Actual Share</td><td>Algorithm Success</td><td>Relative Difference</td><td>Significance</td></tr><tr><td>EX</td><td>Landing</td><td>0.438</td><td>0.419</td><td>-0.019</td><td>-4.36%</td><td>0.13</td></tr><tr><td>UCB</td><td>Landing</td><td>0.061</td><td>0.083</td><td>0.022</td><td>+36.85%</td><td>&lt; 0.01***</td></tr><tr><td>NB</td><td>Landing</td><td>0.501</td><td>0.498</td><td>-0.003</td><td>-0.65%</td><td>0.81</td></tr><tr><td>EX</td><td>Clip</td><td>0.416</td><td>0.339</td><td>-0.077</td><td>-18.60%</td><td>&lt; 0.01***</td></tr><tr><td>ICB</td><td>Clip</td><td>0.141</td><td>0.122</td><td>-0.019</td><td>-13.48%</td><td>&lt; 0.01***</td></tr><tr><td>CSM</td><td>Clip</td><td>0.305</td><td>0.375</td><td>0.070</td><td>+22.90%</td><td>&lt; 0.01***</td></tr><tr><td>KEY</td><td>Clip</td><td>0.137</td><td>0.164</td><td>0.027</td><td>+19.71%</td><td>0.06*</td></tr></table>

Probability that users who clicked on a recommendation click on another recommendation.

<table><tr><td colspan="2">Treatment group</td><td>Control group</td></tr><tr><td> $P_{all}^{treatment}$ </td><td> $P_{expert}^{treatment}$ </td><td> $P_{all}^{control}$ </td></tr><tr><td>31.5%</td><td>17.2%</td><td>14.6%</td></tr></table>

For the analysis we only consider users who have used (expert) recommendations at least once during the study. Table 6 shows the results. We find that clicking on an expert recommendation lowers the chance that a user will click on more recommendations $( P _ { e x p e r t } { ' r e a t m e n t } ~ < ~ P _ { a l l } { ' r e a t m e n t } )$ . This result is consistent with our previous findings regarding algorithm success, where we find that expert recommendations presented to the user seem to be of lower quality and less successful than system-generated recommendations. However, for users who are in the control group (they only see system-generated recommendations) and who have clicked on a (system-generated) re commendation, the probability of clicking on another recommendation is lowest and only 14.6%. Thus, users in the control group click on another recommendation less frequently. The findings are consistent with the result that the use of recommendations and watched clips increases if expert recommendations are presented to users.

The diferences between the numbers are significant. Clicking on expert recommendations lowers the probability of clicking on another recommendation by 14.3% $( \mathsf { W } = 2 2 , 3 9 6 , p \ < \ 0 . 0 1 )$ . Users who did not receive expert suggestions at all, have an even lower probability of clicking on another recommendation $( 1 4 . 6 \% , \mathrm { W } = 1 7 6 , 1 8 6 , p \ < \ 0 . 0 1$ , compared to $P _ { e x p e r t } { \overbrace { ^ { t r e a t m e n t } ) } }$

## 5. Properties of recommendation

We study the given recommendations to better understand whether there are other factors that can explain the diferences between expert and system-generated recommendations. Multiple ofline studies on expert recommendations have shown that experts are able to improve diferent quality measures such as the diversity [28] and coverage [44] of given recommendations. Therefore, we examine the properties (diversity, satisfaction, coverage) of the given recommendations to unveil possible diferences between the system-generated suggestions and the expert recommendations. Results of diversity and coverage are based on the observed click behavior; results for perceived satisfaction are based on a questionnaire sent to the users after the end of the experiment (compare Sect. 3.3).

## 5.1. Diversity

We measure the diversity of recommendation lists that were shown in the two groups. More specifically, we calculate the (normalized) intralist-similarity (ILS) [47].

$$
I L S (R L _ {i, j}) = \frac {\sum_ {b _ {k} \in R L _ {i , j}} \sum_ {b _ {e} \in R L _ {i , j} , b _ {k} \neq b _ {e}} w c o s (b _ {k} , b _ {e})}{2 \times | R L _ {i , j} |},\tag{8}
$$

where $R L _ { i , j }$ is the recommendation list j presented to user $i , b _ { k }$ and $b _ { e }$ denote clips in this recommendation list. wcos $( b _ { k } , b _ { e } )$ calculates the weighted cosine similarity between clips $b _ { k }$ and $b _ { e }$ and $| R L _ { i , j } |$ denotes the length of the recommendation list. Since ILS measures the similarity of items of a list (and therefore the opposite of diversity), a high ILS value indicates less diverse recommendations. ILS varies between −1 (perfect dissimilarity) and 1 (perfect similarity).

We use the following metadata to calculate the weighted cosine similarity of the clips:

1. Overall category a clip belongs to, according to the producers,

2. overall category a clip belongs to, according to the experts,

3. length of the clip,

4. channel of the tv network where the clip first aired,

5. publisher of the clip,

6. recency of the clip (in days since release), and

7. is the clip classified as targeting young adults (binary value).

The first line of Table 7 shows the average ILS of the recommendation lists shown to the control and treatment group. The values are relatively high due to the following reasons:

1. Some of the recommendation approaches either use the same metadata as the ILS calculation to suggest items, or they are based on the overall category of a clip.

2. Some of our recommenders are intentionally designed to generate recommendations that are content-wise close to the currently watched clip (content similarity, keyword).

3. The platform features many series or recurring formats to which popular clips often belong. Since all clips in the same series have similar content, we obtain high ILS scores.

Diferences in properties of shown recommendations between treatment and control group.

<table><tr><td>Construct</td><td>Measure Type</td><td>Control</td><td>Treatment</td><td>Difference</td><td>Significance</td></tr><tr><td>ILS</td><td>click behavior</td><td>0.598</td><td>0.578</td><td>-0.020</td><td>0.03**</td></tr><tr><td>Perceived Satisfaction</td><td>questionnaire</td><td>3.42</td><td>3.43</td><td>0.01</td><td>&gt;0.1</td></tr></table>

Nevertheless, the ILS values of the treatment group are significantly diferent $( p \ : = \ : 0 . 0 3 )$ from the control group. This means that adding experts leads to more diverse clip lists (lower ILS). This finding is in line with existing studies that suggest that by showing users more diverse decision possibilities, their satisfaction with the system and their use of the system can increase, even if these diverse recommendations are not very accurate [13,21].

## 5.2. Perceived satisfaction

Although there are no large scale studies that study the satisfaction of users with recommendations given by experts, there is extensive research on the influence of properties of recommendations on user satisfaction: For example, Ziegler et al. [47] showed that increasing the diversity of recommendations increases user satisfaction. Previous studies found that more diverse recommendations lead to higher user satisfaction, even if the resulting accuracy sufers by the higher diversification [21,23]. More precisely, they showed that higher diversity can reduce the dificulty users have in choosing one of the recommenda tions, which in turn increases their choice satisfaction. The framework of Knijnenburg et al. [21] also shows other potential reasons for a higher user satisfaction: For example, the system's capabilities $( \boldsymbol { \mathrm { e . g . , } }$ accuracy, diversity) can influence the perceived recommendation quality. Since there is evidence that expert recommendations can improve the capabilities of recommender systems, we expect that adding expert suggestions can also increase user satisfaction.

Consequently, the questionnaire asked the users to rate their per ceived satisfaction with the system. All items were measured on a 5- point Likert scale, ranging from “completely disagree” to “completely agree”.

To assess the validity of this approach, we conducted a confirmatory factor analysis (CFA). We removed several items due to insuficient factor loadings, cross-loadings, or residual correlations. Based on the average variance extracted (AVE), all factors achieved convergent validity $\left( \mathsf { A V E } > 0 . 5 \right)$ . Since all correlations between factors were less than the square root of the AVE of each factor, we were also able to assume discriminant validity. Thus, we could use the results of the questionnaire for our analysis.

The second line of Table 7 shows the resulting average of “perceived satisfaction”. We observe no measurable diference in user satisfaction between treatment and control group (3.42 vs. 3.43). In both groups, users were happy with the suggestions they received. Surprisingly, the use of expert recommendations leads to a significant higher use of the platform, although user satisfaction does not increase.

## 5.3. Coverage

We can measure coverage either as prediction coverage, catalogue coverage, or taste coverage (see Sect. 2). In our study, we did not measure prediction coverage since –aside from the added expert suggestions– both groups saw recommendations from the same recommender system. We also did not measure catalogue coverage. as our experts did not make clip-specific recommendations. With thousands of clips being uploaded or deleted every day, the experts were not able to define thousands of diferent clips for each category.

However, we can measure taste coverage (TC) which counts how many unique recommendations were used in comparison to the number of unique clips that were watched by a user. We define taste coverage as

$$
T C _ {i} = \frac {U C L _ {u s e d , i}}{U C L _ {w a t c h e d , i}},\tag{9}
$$

where $U C L _ { u s e d , }$ is the number of unique (recommended) clips that user i clicked on and $U C L _ { w a t c h e d , }$ is the number of unique clips that were watched by this user in total.

In addition, we measure the share of unique recommendations used (i.e., recommendations that were actually clicked) over the number of unique recommendations given (Unique Recommendation Clicks) as

$$
U R C _ {i} = \frac {U C L _ {u s e d , i}}{U C L _ {r e c , i}},\tag{10}
$$

where $U C L _ { r e c , i }$ is the number of unique clips that were recommended to user i. A higher value of URC indicates that users watched more different clips because of the given suggestions.

For TC, the treatment group performs slightly higher with an average score of 0.258 compared to 0.25 for the control group. Thus, expert recommendations are able to cover slightly more of the overall watched clips and better cover the interests of the users $( p ~ < ~ 0 . 1 )$ Thus, “taste coverage” is slightly higher when recommendations from employed experts are used. Taking into account that experts generate more diverse recommendations and lead to a higher use of the platform, this result confirms the previous findings.

We found similar results for URC. For the treatment group (0.161), the score is significantly higher $( p \ < \ 0 . 0 1 )$ in comparison to the control group (0.156). Thus, the users used relatively more unique recommendations when expert suggestions were mixed into the list. Again, this result is in line with the previous findings of a higher diversity and higher platform use in the treatment group.

## 6. Conclusions and future research

This paper studied the efect of expert recommendations on user behavior, user perceptions, and properties of recommendations. By using a large scale online experiment in a realistic setting, we were able to show the benefits of using employed experts. More precisely, we found that using experts leads to an increase in the number of watched clips (+9.8%), the use of recommendations (+17.1%), and whether people still used the platform after 10 weeks (+15% retain rate). Users visited the platform more often (+9%) and had more frequent visit where they watched more than one clip (+15.7%). Thus, experts can significantly increase platform usage, are able to keep users longer on the website, and make users come back more frequently. Expert recommendations can be highly beneficial for the success of recommender systems as the higher platform usage can directly translate into revenue (e.g., by showing ads before or during the consumption of a clip).

Second, we examined whether expert recommendations were clicked more often than expected comparing the observed click rate on expert recommendations to the expected probability of a click. Surprisingly, we found that expert-based suggestions were used less than expected even though the treatment group significantly used the platform more often. This is in line with the finding that the probability of clicking on another recommendation decreases when the first clicked recommendation was generated by experts. Nevertheless, users who did not receive expert suggestions at all, have an even lower probability of clicking on another recommendation.

Although expert recommendations seem to be less successful, users that receive not only system-generated but also expert recommendations significantly use the platform more often and more intense. Thus, the argument of McNee et al. that “accuracy is not enough” [32] or has even “hurt recommender systems” [32] seems to be valid as the accuracy of recommendations alone is not suficient to explain the higher system usage in the presence of expert recommendations. Instead, there must be other factors that are relevant to users. Consequently, we also studied possible diferences in the properties of expert recommenda tions versus system-generated ones. We found that experts were able to provide more diverse recommendations that better cover the interest of the users (i.e., taste coverage).

Our study at hand gives strong evidence that the use of expert re commendations has a quite large and significant impact on user behavior. Although expert recommendations are used less than expected, the overall platform usage significantly increases. Comparing the properties of the recommendations shown to the users, we find that expert recommendations are more diverse and better cover the taste of users. Consequently, the next steps would be to focus on diversity and directly control the diversity of recommendations in a large controlled online experiment.

There are multiple areas for future research and several limitations to this study. First, the purpose of this study was to observe the impact of expert recommendations on user behavior. Even though we observed an increase in several user-behavior-related measures as well as differences in recommendation properties (e.g., diversity), we cannot make any causal inference that diversity is responsible for this. Controlled tests that directly manipulate the recommendation diversity and taste coverage, etc., in the context of expert recommendations would be needed to answer this question.

Second, we tested expert recommendations in a low-risk setting of video-on-demand recommendations. The implications of choosing lowquality recommendations were negligible for users since they could stop watching a clip at any point in time and they would not lose money if they did. In other words, there were no severe negative consequences if users selected low-quality recommendations. Therefore, users might have been more interested in exploring the diverse possibilities of the platform. This could be diferent in other settings such as e-commerce or dating. Thus, we suggest studying the efect of using experts in different domains, especially domains where people rely more frequently on personal recommendations by experts (e.g., in classic retail stores). However, it could be more dificult to identify experts in certain areas, or users might be less receptive to expert recommendations in some cases (e.g., users might not want expert recommendations on dating platforms for reasons of privacy). This also raises the question on how to access the degree of expert knowledge and whether this should influence the weighting of a certain expert's opinion. Experts with a lot of work experience in a certain domain might be better able to give recommendations than “new” experts, but they might also be more expensive, and they might be oblivious to current trends.

Third, employed experts can be hard to find and often have to be paid. Since their exact cost and how many hours the experts spent in total is often unknown, it is hard to decide whether it is economically viable for companies to use experts for recommendations. This has to be calculated individually while considering both the cost for the experts and the approximated benefit of the increased watch time and visit frequency of the visitors on the platform. Another challenge is that, depending on the domain, it might be very dificult to even find an expert capable of giving recommendations in a reasonable timeframe, for example if the available items are very diverse (e.g., amazon).

Finally, we intentionally did not disclose to the user which recommendations were made by experts, and users did not know that experts were involved. Previous studies have shown that users tend to trust experts more, so the mere explanation that a suggestion stems from expert knowledge might have an influence on the perception of this recommendation. This might counter the fact that expert recommendations seem to be less accurate and were used less than ex pected. It is interesting to see whether the efect of expert re commendations changes when users are aware that actual humans are generating the suggestions. Recent research suggests that users might actually prefer algorithmic over human advice and this efect might be influenced by the personal expertise of a user [29].

## Declaration of Competing Interest

None.

## References

[1] Gediminas Adomavicius, Jesse C. Bockstedt, Shawn P. Curley, Jingjing Zhang, Do recommender systems manipulate consumer preferences? A study of anchoring efects, Inf. Syst. Res. 24 (4) (2013) 956–975.

[2] Gediminas Adomavicius, Jesse C. Bockstedt, Shawn P. Curley, Jingjing Zhang, Reducing Recommender Systems Biases: An Investigation of Rating Display Designs, Manag. Inf. Syst. Q. 43 (4) (2019) 1321–1341.

[3] Xavier Amatriain, Neal Lathia, Josep M. Pujol, Haewoon Kwak, Nuria Oliver, The wisdom of the few: a collaborative filtering approach based on expert opinions from the web, Proceedings of the International Conference on Research and Development in Information Retrieval (SIGIR ‘09), 2009, pp. 532–539.

[4] Xavier Amatriain, Josep M. Pujol, Nava Tintarev, Nuria Oliver, Rate it again : increasing recommendation accuracy by user re-rating, Proceedings of the 3rd ACM Conference on Recommender Systems - RecSys ‘09, 2009, pp. 173–180.

[5] Jie Bao, Zheng Yu, Mohamed F. Mokbel, Location-based and preference-aware recommendation using sparse geo-social networking data, Proceedings of the 20th International Conference on Advances in Geographic Information Systems - SIGSPATIAL ‘12, 2012, pp. 199–208.

[6] Judit Bar-llan, Kevin Keenoy, Mark Levene, Eti Yaari, Presentation bias is sig nificant in determining user preference for search results-A user study, J. Am. Soc. Inf. Sci. Technol. 60 (1) (2009) 135–149

[7] Jesús Bobadilla, Antonio Hernando, Fernando Ortega, Jesús Bernal, A framework for collaborative filtering recommender systems, Expert Syst. Appl. 38 (12) (2011) 14609–14623.

[8] Jesús Bobadilla, Fernando Ortega, Antonio Hernando, Javier Alcalá, Improving collaborative filtering recommender system results and performance using genetic algorithms, Knowl-Based Syst, 24 (8) (2011).1310–1316

[9] Jesús Bobadilla, Francisco Serradilla, Jesús Bernal, A new collaborative filtering metric that improves the behavior of recommender systems. Knowl.-Based Syst. 23 (6) (2010) 520–528.

[10] Engin Bozdag, Qi Gao, Geert Jan Houben, Martijn Warnier, Does ofline political segregation afect the filter bubble? An empirical analysis of information diversity for Dutch and Turkish Twitter users, Comput. Hum. Behav. 41 (2014) (2014) 405–415.

[11] Jinhyung Cho, Kwiseok Kwon, Yongtae Park, Collaborative filtering using dua information sources, JEEE Intell, Syst, 22 (3) (2007) 30–38

[12] Marco De Gemmis, Pasquale Lops, Giovanni Semeraro, Cataldo Musto, An in vestigation on the serendipity problem in recommender systems, Inf. Process. Manag, 51 (5) (2015) 695–717.

[13] D. Michael, F. Maxwell Harper Ekstrand, Martijn C. Willemsen, Joseph A. Konstan, User perception of diferences in recommender algorithms, Proceedings of the 8th ACM Conference on Recommender systems - RecSys ‘14, 2014, pp. 161–168.

[14] Achraf Gazdar, Lotfi Hidri, A new similarity measure for collaborative filtering based recommender systems, Knowl.-Based Syst. 188 (2020) (2020) 105058.

[15] Mouzhi Ge, Carla Delgado-Battenfeld, Dietmar Jannach, Beyond accuracy: evalu ating recommender systems by coverage and serendipity, Proceedings of the 4th ACM conference on Recommender systems - RecSys ‘10, 2010, pp. 257–260

[16] Anupriya Gogna, Angshul Majumdar, Balancing accuracy and diversity in recommendations using matrix completion framework, Knowl.-Based Syst. 125 (2017) (2017) 83–95.

[17] Jonathan L. Herlocker, Joseph A. Konstan, Loren G. Terveen, John T. Riedl, Evaluating collaborative filtering recommender systems, ACM Trans. Inf. Syst. 22 (1) (2004) 5–53.

[18] Ke Ji, Hong Shen, Addressing cold-start: Scalable recommendation with tags and keywords. Knowl.-Based Syst, 83 (1) (2015) 42–50.

[19] Mark T. Keane, Maeve O'Brien, Barry Smyth, Are people biased in their use of search engines? Commun. ACM 51 (2) (2008) 49–52.

[20] Bart P. Knijnenburg, Saadhika Sivakumar, Daricia Wilkinson, Recommender Systems for Self-Actualization, Proceedings of the 10th ACM Conference on Recommender Systems RecSys ‘16, 2016, pp. 215–218.

[21] Bart P. Knijnenburg, Martijn C. Willemsen, Zeno Gantner, Hakan Soncu, Chris Newell. Explaining the user experience of recommender systems. User Model User-Adap. Inter, 22 (4–5) (2012) 441–504.

[22] Denis Kotkov, Shuaiqiang Wang, Jari Veijalainen, A survey of serendipity in re commender systems. Knowl.-Based Syst. 111 (2016) (2016) 180–192

[23] Matevž Kunaver, Tomaž Požrl, Diversity in recommender systems – a survey, Knowl.-Based Syst. 123 (2017) (2017) 154–162

[24] Kibeom Lee. Kvogu Lee. Using dynamically promoted experts for music re commendation, JEEE Trans, Multimedia 16 (5) (2014) 1201–1210.

[25] Blerina Lika, Kostas Kolomvatsos, Stathes Hadiiefthymiades, Facing the cold start problem in recommender systems. Expert Syst. Appl. 41 (4) (2014) 2065–2073.

[26] Chen Lin, Runquan Xie, Lei Li, Zhenhua Huang, Tao Li, PRemiSE: personalized news recommendation via implicit social experts, Proceedings of the 21st ACM international conference on Information and knowledge management - CIKM12, 2012. pp. 1607-1611.

[27] Greg Linden, Brent Smith, Jeremy York, Amazon,com recommendations: item-to: item collaborative filtering, IEEE Internet Comput. 7 (1) (2003) 76–80

[28] Nathan Liu, Xiangrui Meng, Chao Liu, Qiang Yang, Wisdom of the better few : cold start recommendation via representative based rating elicitation, Proceedings of the 5th ACM conference on Recommender systems - RecSys ‘11, 2011, pp. 37–44.

[29] Jennifer M. Logg, Julia A. Minson, Don A. Moore, Algorithm appreciation: people prefer algorithmic to human judgment, Organ. Behav. Hum. Decis. Process. 151 (2019) (2019) 90–103.

[30] Xin Luo, Yunni Xia, Qingsheng Zhu, Yi Li, Boosting the K-Nearest-Neighborhood based incremental collaborative filtering, Knowl.-Based Syst. 53 (2013) (2013) 90–99.

[31] Elaheh Malekzadeh Hamedani, Marjan Kaedi, Recommending the long tail items through personalized diversification, Knowl.-Based Syst. 164 (2019) (2019) 348–357.

[32] Sean M. McNee, John Riedl, Joseph A. Konstan, Being accurate is not enough: how accuracy metrics have hurt recommender systems, CHI’06 extended abstracts on Human factors in computing systems, 2006, pp. 1097–1101.

[33] Efrat Nechushtai. Seth C. Lewis. What kind of news gatekeepers do we want ma: chines to be? Filter bubbles, fragmentation, and the normative dimensions of algorithmic recommendations, Comput. Hum. Behav. 90 (2019) (2019) 298–307.

[34] O. Derek, Derek Greene Callaghan, Maura Conway, Joe Carthy, Draig Cunningham, Down the (White) Rabbit Hole: The Extreme Right and Online Recommender Systems, Soc. Sci. Comput. Rev. 3 (4) (2015) 459–478.

[35] E. Pariser, The Filter Bubble: What the Internet Is Hiding from you, Penguin Books Limited. 2011.

[36] Mario Rodriguez, Christian Posse, Ethan Zhang, Multiple objective optimization in recommender systems, Proceedings of the 6th ACM conference on Recommender systems - RecSys 12, 2012, pp. 11–18.

[37] Xiaolan Sha, Sophia Antipolis, Daniele Quercia, Pietro Michiardi, Matteo Amico, Spotting trends: the wisdom of the few, Proceedings of the 6th ACM conference on Recommender systems - RecSys ‘12, 2012, pp. 51–58.

[38] Catarina Sismeiro, Ammara Mahmood, Competitive vs. complementary efects in online social networks and news consumption: a natural experiment, Manag. Sci. 64 (11) (2018) 5014–5037

[39] Yicheng Song, Nachiketa Sahoo, Elie Ofek, When and how to diversify-a multi category utility model for personalized content recommendation, Manag. Sci. 65 (8) (2019) 3737–3757.

[40] Weiquan Wang, Izak Benbasat, Attributions of Trust in Decision Support Technologies: A Study of Recommendation Agents for E-Commerce, J. Manag. Inf. Syst. 24 (4) (2008) 249–273.

[41] Daricia Wilkinson, Testing a recommender system for self-actualization,

Proceedings of the 12th ACM conference on Recommender systems - RecSys, 18 2018, pp. 543–547.

[42] Weiwei Yuan, Donghai Guan, Young Koo Lee, Sungyoung Lee, Sung Jin Hur, Improved trust-aware recommender system using small-worldness of trust net works, Knowl.-Based Syst, 23 (3) (2010) 232–238

[43] Long Yun, Yan Yang, Jing Wang, Ge Zhu, Improving rating estimation in recommender using demographic data and expert opinions, Proceedings of the 2nd IEEE International Conference on Software Engineering and Service Science - ICSESS ‘11, 2011, pp. 120–123.

[44] Muhammad Bilal Zafar, Parantapa Bhattacharya, Niloy Ganguly, Saptarshi Ghosh, Krishna P. Gummadi, On the wisdom of experts vs. crowds: discovering trustworthy topical news in microblogs, Proceedings of the 19th ACM Conference on Computer-Supported Cooperative Work & Social Computing - CSCW ‘16, 2016, pp. 437–450.

[45] Feng Zhang, Ti Gong, Victor E. Lee, Gansen Zhao, Chunming Rong, Qu. Guangzhi, Fast algorithms to evaluate collaborative filtering recommender systems, Knowl.- Based Syst. 96 (2016) (2016) 96–103.

[46] Tong Zhang, Vijay S. Iyengar, Recommender Systems Using Linear Classifiers, J. Mach. Learn. Res. 2 (3) (2002) 313–334.

[47] Cai-Nicolas Ziegler, Sean M. McNee, Joseph A. Konstan, Georg Lausen, Improving recommendation lists through topic diversification. World Wide Web Conference ‘05, 2005, pp. 22–32.

Franz Rothlauf is a professor of Information Systems at the University of Mainz, Germany. He has published more than 100 technical papers in the context of planning and optimization, decision support, artificial intelligence, e-business, and software engineering, co-edited several conference proceedings and edited books. Since 2013, he is Academic Director of the Executive MBA program at the University of Mainz. Since 2016, he is Chief Information Officer of the University of Mainz, Since 2007. he is member of the Executive Committee of ACM SIGEVO. He was elected Chair of SIGEVO in 2019. His mair research interests are the application of metaheuristics and neural networks in decisior support systems.

Nils Herm-Stapelberg is a doctoral candidate at the Chair of Information Systems and Business Administration at the University of Mainz, Germany. His main research interests are in the area of Human Computer Interaction (HCI). More specifically, his work is concerned with the implications of recommender systems on user behavior and user perceptions as well as the economic and social implications of recommender systems.
