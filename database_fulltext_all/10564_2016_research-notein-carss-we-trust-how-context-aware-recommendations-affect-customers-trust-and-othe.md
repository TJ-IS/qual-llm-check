---
otero_id: 10564
otero_key: "ABN668S2"
title: "Research Note—In CARSs We Trust: How Context-Aware Recommendations Affect Customers’ Trust and Other Business Performance Measures of Recommender Systems"
authors: "Umberto Panniello; Michele Gorgoglione; Alexander Tuzhilin"
year: "2016"
journal: "Information Systems Research"
doi: "10.1287/isre.2015.0610"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/ABN668S2/fulltext/images/1ad68fe56534a6d8a4dd7dad8f64a9dd90fe21009ad6e5cb8275158f423b92bd.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Research Note—In CARSs We Trust: How Context-Aware Recommendations Affect Customers’ Trust and Other Business Performance Measures of Recommender Systems

Umberto Panniello, Michele Gorgoglione, Alexander Tuzhilin

To cite this article:

Umberto Panniello, Michele Gorgoglione, Alexander Tuzhilin (2016) Research Note—In CARSs We Trust: How Context-Aware Recommendations Affect Customers’ Trust and Other Business Performance Measures of Recommender Systems. Information Systems Research

Published online in Articles in Advance 20 Jan 2016

http://dx.doi.org/10.1287/isre.2015.0610

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2016, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/ABN668S2/fulltext/images/16b68a8943570ea7c79a285c43f4086cb3a813139cca5f8ebd904357d365d517.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Note

# In CARSs We Trust: How Context-Aware Recommendations Affect Customers’ Trust and Other Business Performance Measures of Recommender Systems

Umberto Panniello, Michele Gorgoglione

Politecnico di Bari, 70126 Bari, Italy {umberto.panniello@poliba.it, michele.gorgoglione@poliba.it}

Alexander Tuzhilin

Stern School of Business, New York University, New York, New York 10012, atuzhili@stern.nyu.edu

ost of the work on context-aware recommender systems has focused on demonstrating that the contextual much the contextual information affects the business performance. In this paper, we study how including context in recommendations affects customers’ trust, sales, and other crucial business-related performance measures. To do this, we delivered content-based and context-aware recommendations through a live controlled experiment with real customers of a commercial European online publisher. We measured the recommendations’ accuracy and diversification, how much customers spent purchasing products during the experiment, the quantity and price of their purchases, and the customers’ level of trust. We show that collecting and using contextual information in recommendations affects business-related performance measures, such as company sales, by improving the accuracy and diversification of recommendations, which in turn improves trust and, ultimately, busines performance results.

Keywords: business value of IT; case studies; economics of IS; electronic commerce; field experiments; recommender systems; context aware

History: Vijay Mookerjee, Senior Editor; Eric Zheng, Associate Editor. This paper was received on August 7, 2015, and was with the authors 1 month for 1 revision. Published online in Articles in Advance

## 1. Introduction

The use of recommender systems (RSs) in the industry has exploded since the late 2000s to the effect that most of the major companies either have RSs in place or have recently launched major RS initiatives (Lamere 2012, Amin et al. 2012, Koenigstein et al. 2012, Liu et al. 2012, Smyth et al. 2012, Amatriain 2012). Furthermore, RSs constitute mission-critical technologies in some of these companies. For example, at least 75% of Netflix movie rentals and downloads come from their RS, making it of strategic importance to Netflix (Amatriain and Basilico 2012). Similarly, the business model of Stitch Fix relies entirely on recommender systems (Colson 2014). One of the important factors affecting the performance of RSs is the contextual information (Adomavicius and Tuzhilin 2011). Some music streaming companies, such as LastFM, ask customers to specify their mood before recommending particular music. This mood information is then used by the system to recommend only the type of music that best fits the customer’s mood, mood being a contextual variable in this case. As another example, Netflix knows the location of customers and uses the locational contextual variables, such as city and/or zip code, and time to provide context-specific recommendations of movies. As Reed Hastings, the chief executive officer of Netflix, pointed out, Netflix can improve the performance of its RS up to 3% when taking into account such contextual information as the time of day or location in their recommendation algorithms. Watch his interview at www.youtube.com/ watch?v=8FJ5DBLSFe4&feature=youtu.be.

Most of the existing work on context-aware recommender systems (CARSs) has focused on accuracy metrics for measuring the performance of RSs and demonstrated that knowledge of certain relevant types of contextual information leads to more accurate estimations of unknown ratings. Although relevant, this work constitutes only the first step toward demonstrating the usefulness of contextual information because the business community is mainly interested in economicsrelated performance metrics, such as changes in sales volumes, profits, and prices of purchased products, as opposed to the accurate estimation of unknown ratings.

The main contribution of this paper lies in proposing a model that determines the effects of contextual information on business performance outcomes, as measured by quantities of goods purchased and the total money spent by customers, using customers trust and accuracy and diversification of recommendations as intermediate variables. We study this problem empirically by conducting a live controlled experiment with real customers in a real industrial setting (a major comic books publisher in Europe). Such types of experiments are done infrequently in the recommender systems community since the vast majority of empirical work still involves the analysis of off-line historic data. We show in this paper that contextual information affects business performance outcomes, such as quantities of goods purchased and the total money spent by customers, via intermediate variables, such as customer trust and accuracy and diversification of recommendations, by deploying structural equation models (SEMs) and measuring the effects of context on business performance outcomes. We demonstrate that when contextual information is included in the recommendations that are delivered to customers, both the recommendations’ accuracy and their diversity increase. This increase is correlated with an increase in customers’ trust, which in turn is associated with an increase in the money spent by the customers who receive these recommendations and the quantity of products they buy. In our experiment the contextual information used to generate recommendations was the “intent of purchase” (i.e., the occasion and person for whom a purchase is intended) and the customer’s “mood” (i.e., the personal condition in which a purchase is done). It is important to point out that these findings do not necessarily prove a causal relationship between context and the business performance measures used in the research, but rather establish a predictive relationship between these variables (Shmueli and Koppius 2011).

## 2. Prior Work

Several scholars have studied the effect of recommendations for traditional, uncontextual RSs. Schafer et al. (2001) argued that RSs help increase sales by converting browsers into buyers, increasing cross-selling opportunities, and building customer loyalty. However, the accuracy of recommendations alone is not sufficient to explain the purchasing behavior. Trust also plays a key role. Pathak et al. (2010) found that recommendations influence shoppers’ decisions only when they are perceived to be objective and credible. Since retailers have full control of recommendations, it is natural for shoppers to discount the credibility of online RSs because of potential manipulation by retailers. This perception is further supported by anecdotal evidence of retailers manipulating the outcome of RSs (Flynn 2006, Mui 2006). Pu et al. (2011) found that whereas overall satisfaction with the recommender system defined in terms of ease of use and perceived usefulness is important for usage intentions, trust in the system and choice confidence are crucial for purchasing intentions.

The effect of accuracy of recommendations on trust has also been studied. Zhang et al. (2011) showed that the customer loyalty for online stores can be increased by improving recommendations’ accuracy but is not sufficient alone. Relevance, accuracy, completeness, and timeliness of recommendations have a significant effect on users’ decision making and satisfaction (Bharati and Chaudhury 2004). Familiar recommendations play an important role in establishing user trust in a RS (Swearingen and Sinha 2001, 2002). However, Komiak and Benbasat (2006) demonstrated that the user’s familiarity with the recommendations increased trust in the recommender’s benevolence and integrity, but not trust in its competency. Xiao and Benbasat (2007) showed that the way familiar and unfamiliar items are balanced in a recommendation list influences users trust in the perceived usefulness of and satisfaction with RSs.

The accuracy of the predictions provided by a RS is only one of the possible variables affecting trustworthiness (Lenzini et al. 2009). Several studies have demonstrated that diversity, diversification, variety, and novelty of recommendations can have an important role. Most researchers agree that consumers generally prefer more variety when given a choice (Baumol and Ide 1956, Kahn and Lehmann 1991). Fleder and Hosanagar (2009) demonstrated that RSs that discount item popularity in the selection of recommendable items may increase sales more than RSs that do not. Similarly, Brynjolfsson et al. (2003) showed that increased product variety made available through electronic markets can be a significantly larger source of consumer surplus gains. The concepts of novelty and diversity are often discussed as a joint function because it is important in many applications to recommend a wide range of items that customers have not seen before (Vargas and Castells 2011, Zhang and Hurley 2009). Following this work, in this paper we consider both diversity and novelty as aspects of a more general concept that we call diversification, as explained in §3.3. McGinty and Smyth (2003) found that diversity can provide significant gains if carefully tuned. Simonson (2005) showed that higher variety seeking decreases receptivity to customized offers. Ziegler et al. (2005) showed that users’ overall satisfaction with recommendation lists goes beyond accuracy and involves other factors, e.g., the diversification of the result set. Similar results were found by other studies (Bollen et al. 2010, Smyth and McClave 2001). Hu and Pu (2011) showed that perceived diversity significantly influences users perceived ease of use and usefulness of the RS, positive attitudes toward the system, and behavioral intentions.

Some researchers have also investigated the combined effect of accuracy and diversity. Additional recommendations of familiar products serve as a context within which unfamiliar recommendations are evaluated (Cooke et al. 2002). Liang et al. (2006) demonstrated that both the number of recommended items and the recommendation accuracy had significant effects on user satisfaction. McGinty and Smyth (2003) highlighted the pitfalls of naively incorporating diversity-enhancing techniques into existing RSs. They pointed out that diversity should be provided adaptively rather than being enhanced in each and every recommender cycle. Knijnenburg et al. (2012) found that users may not perceive diversified recommendation sets as more diverse, but they perceive them as more accurate. Situational (context) and personal characteristics (such as trust, domain knowledge, and perceived control) can mediate this perception. An important contribution was made by Adomavicius and Kwon (2012), who demonstrated the existence of a trade-off between accuracy and diversity. Ranking recommendations according to the predicted rating values provides good predictive accuracy, but it tends to perform poorly with respect to recommendation diversity.

All of this prior work focuses on examining relationships between accuracy, diversification, trustworthiness of recommendations, and increased levels of sales and other business-related indicators for the tradi tional recommender systems. Much research has been done on CARSs, and Adomavicius and Tuzhilin (2011) provide a broad overview of this area. However, no research has been done on studying these effects for the context-aware recommender systems, especially in the context of conducting controlled live experiments in real industrial settings. Most of the research has focused on the relationship between context and accuracy. For instance, Adomavicius et al. (2005) showed that contextual information can increase recommendation accuracy if deployed properly. Furthermore, Panniello et al. (2009) compared several alternative context-aware methods and demonstrated that context can increase recommendation accuracy. Very little research has included other variables, such as diversity and trust, in the analysis. For instance, Panniello et al. (2012) compared accuracy and diversity of contextaware RSs without studying the effect on customer behavior. Gorgoglione et al. (2011) studied the combined effect of accuracy and diversity on customers trust and behavior in a live controlled experiment. They found that a context-aware RS can outperform other types of RSs not only in terms of accuracy but also in terms of trust and other economics-based performance metrics. They also compared accuracy and diversity of different recommendation engines. The authors, however, did not propose any analytical model, did not provide significant explanations of these results, and stated the need for further research.

In this paper, we go well beyond Gorgoglione et al. (2011) and explore the relationship between context and business performance outcomes at a significantly deeper level. By deploying structural equation models, we measure the effect of including contextual information in recommendations on their accuracy and diversification and the effect of customer’s trust on their purchasing behavior, namely, money spent and quantity of products purchased.

## 3. Methodology

To study how context-aware recommendations affect business-related performance, we conducted a live experiment in partnership with a well-known global European publishing firm. The company’s Web division mainly sells comic books and related products, such as DVDs, stickers, and T-shirts. As a part of its normal business, the company sends a weekly nonpersonalized newsletter to 24,364 customers. The firm agreed to send personalized recommendations of comic books via email (in addition to the traditional weekly newsletter) to a sample of 360 customers as a part of our project. The 360 customers were randomly selected from the customer database. The experiment participants were then randomized into three experimental treatment groups.

## 3.1. Experimental Design

We followed the standard experimental design approach and split the study participants into three experimental treatment conditions. Each group received a personalized newsletter generated via a different recommendation engine: 90 users received content-based recommendations, 90 users received random recommendations, and 180 users received context-aware recommendations. We decided to double the number of users included in the contextual group since a CARSbased system needs more ratings than a traditional one to work correctly. This does not bias the results because we averaged each performance metric across customers instead of using the absolute values. Therefore, the metrics used in the study are not affected by the number of participants in each group. We measured accuracy and diversification of recommendations, the customers trust in these recommendations, and business-related metrics, namely, the quantity of goods purchased, average price, and money spent by customers, as described further in §3.3. To make a meaningful comparison, the firm gave us access to the data pertaining to the purchasing behavior of the customers involved in the experiment in a period of 20 months before the experiment began. By comparing the data before and after the experiment, we could observe the effect of recommendations on customers’ purchasing behavior and, in turn, on business performance.

We addressed this problem by developing a structural equation model (Bollen 1989) determining the effects of contextual information on business performance outcomes via intermediate variables, such as accuracy and diversification of recommendations and trust that customers put into these recommendations. In this study, we empirically validated the following conclusion and showed that it is indeed the case: using contextual information increases the recommendations accuracy and diversification, this increase affects customers’ trust, and the increase in trust affects the money spent by customers and the quantity of products they purchase. We chose a between-subjects design for the experiment because we needed to measure certain aspects of the user experience (trust and purchasing behavior). In this case the experiment had to be as close to a real-world usage situation as possible, and it was imperative to avoid spillover effects and other biases (Knijnenburg 2012). This choice entailed defining different treatments, namely, a group of customers receiving context-aware recommendations and another receiving context-unaware recommendations.

Before starting the experiment, we asked the participants to rate a representative set of 12 comic books selected by the company. This set of comic books was representative of the whole item database, and it was the same for each user. This initial step was needed to build the initial user profiles and avoid the “cold start” problem (Schein et al. 2012), given that building a preexperiment user profile was possible only for less than 5% of users, those who had purchased more than one item per year.

After that, each subject received a personalized weekly newsletter displaying 10 recommended comic books for nine consecutive weeks. The newsletter contained a link to a personal recommendation page displaying the 10 recommended items. Five items were “recommended brand new items” selected from brand new arrivals at the firm (about 30 brand new published comic books per week), and the remaining five were “recommended old items” selected from the arrivals in the past two months (about 250 items). As explained in §5, this does not introduce issues related to preimposed diversity and therefore does not bias the results. Each item was presented with the following information: title, cover image, description, and a “see more details” link. The customers were invited to rate each recommended product by clicking on a 0–5 point scale. Although the users might not have read a recommended book when asked to give a rating, the information provided about the books was sufficient for the customers to make a good assessment because of the special nature of the comic books industry. Comic books usually come in series with the main characters from the series being familiar to the comic books fans. Therefore, if a customer has not read a particular recommended book, she can always click on the “see more details” link, read the general description of the new book, and then use the prior knowledge about the whole series and its main characters to form an informed opinion about how much interest she has in that book.

These solicited ratings were subsequently used to update the user profile for each user (except for the random treatment; see §3.2). All of the aforementioned settings were applied to all three treatment groups. The average response rate (i.e., users who gave feedback during the experiment) was about 65% for each treatment condition.

## 3.2. Types of Recommender Systems Used in the Study

During the experiment we used three different RSs: a content-based system, a context-aware system, and a random one. We chose a content-based recommendation algorithm, rather than a collaborative filtering (CF) method, because it would have been difficult to generate meaningful recommendations using the CF approach since the experiment was carried out with few participants and the user/item matrix was relatively sparse—the two conditions adversely affecting CF results.

3.2.1. Content Based. The content-based algorithm (Pazzani and Billsus 2007) uses characteristics of previously purchased or rated items to build customers’ preference profiles and uses these profiles to provide appropriate recommendations. More formally, contentbased systems estimate an unknown rating $u ( i , s )$ of item s for user i based on the ratings $u ( i , s _ { j } )$ assigned by user i to items $s _ { j } \in S$ that are similar to item s (Adomavicius and Tuzhilin 2005). In particular, let ItemProfile4s5 for item s and UserProfile4i5 for user i be two vectors representing the item characteristics and the customer preference, respectively. We computed ItemProfile4s5 by extracting a set of keywords taken from the content of $s \left( \mathrm { e . g . } \right)$ a comic book description). We computed UserProfile4i5 by analyzing the content of the items previously seen and rated by user i. It is defined as a vector of weights $( w _ { i 1 } , \dots , w _ { i z } ) .$ , where each $w _ { i j }$ denotes the importance of keyword j to user i. We computed $w _ { i j }$ as an “average” of the ratings provided by user i to those items that contained the keyword $j \in Z$ . In our study, we assumed that $z = 8 0$ , thus restricting the keyword profile lengths to 80 words. Candidate items are compared with a user profile, and the most relevant items are recommended, where the relevance u4i1 s5 of item s to user i is determined as the average weights of the words in common between UserProfile4i5 and ItemProfile4s5. The top 10 items with the highest u4i1 s5 are recommended to the user in the newsletter. Since we adopt a content-based engine that uses item features, we checked that each item had the same amount of information (title, subtitle, and description) to avoid the introduction of biases.

Figure 1 Hierarchical Structure of Context: (a) Intent of Purchase and (b) Customer’s Mood  
![](/api/attachments/ABN668S2/fulltext/images/9869d15b3bb58fd47d53db8f69981b5344e07d100a307c286fd138d49571e127.jpg)

3.2.2. Context Aware. The CARS developed for our experiment used the same content-based algorithm discussed in the previous section to compare the two methods on the same basis. The only difference is that we used the contextual profile UserProfile4i1 k5 of user i in context k (e.g., a gift for a parent in Figure 1(a)) instead of the general noncontextual profile UserProfile4i5. We computed profile UserProfile4i1 k5 by following the prefiltering approach (Adomavicius and Tuzhilin 2011, Panniello et al. 2009) by analyzing the content of the items previously seen and rated by user i in context k. In particular, the contextual information k is used as a label for filtering out those items that were not rated in this context k, i.e., this method selects from the initial set of all of the ratings only those referring to context k. As a result, UserProfile4i1 k5 contains only the data pertaining to context k. After that, the contentbased algorithm is launched on only these selected data to produce recommendations specific to context k. Therefore, a different item can be recommended when using the contextual user profile UserProfile4i1 k5 versus the case when the uncontextual user profile UserProfile4i5 is used. For example, a Spider-Man comic book can be suggested to the user “Joe” as a potential gift for a friend, whereas that comic book would not be recommended to the user “Joe” when he is looking for his personal collection. In this work, we follow the representational approach to defining contextual information (Dourish 2004), which assumes that all of the contextual variables and their structures are known a priori and fixed (Adomavicius and Tuzhilin 2011, Panniello et al. 2009, Kwon and Kim 2009). In our case, we define context by two contextual attributes (variables): the intent of a purchase made by a customer and the customer’s mood (see Figure 1). The contextual attribute intent of purchase distinguishes the situation of whether the user is looking for recommendations for her personal interest (further distinguished between recommendations for her collections, special issues or occasional reading) or for a gift (further distinguished between recommendations for a gift to a partner, a friend, etc.). The attribute customer’s mood assumes that the customer may be looking for different recommendations depending on her type of mood, which can be “dark,” “energetic,” “positive” or “calm” in our study. We decided to use intent of purchase and mood as contextual variables in our study after setting up focus groups, conducting several interviews with readers, and discussing the produced results with company management. When users of the contextual treatment group received the newsletter, it was requested that they specify the context in which they wanted to receive recommendations (i.e., for a personal purpose or for a gift, and then for whom, and what their mood was at the moment). Then recommendations were shown to the participants only for this specified context.

3.2.3. Random/Control Group. Unlike the contentbased and context-aware approaches, the random approach does not take the user profile into consideration when recommending new products. Instead, it randomly selects, without replacement, a set of items to recommend from the products that have not been recommended or purchased before.

## 3.3. Performance Measures

We used accuracy, trust, diversification, and customer purchasing activities as metrics that measure various performance aspects of our recommendation methods. We describe them in turn now.

3.3.1. Accuracy. Accuracy was measured by precision and by the average rating provided by customers. Among the traditional information retrieval performance metrics, such as precision, recall, and F -measure, only precision can be computed in our case, since it is not possible in a live experiment to know the ratings of the unseen items needed to compute recall and the F -measure. Precision of a recommendation (Herlocker et al. 2004) for each customer in each week is measured as the ratio between the total number of items recommended to the jth customer and the number of items which proved to be “relevant” for the jth customer among those selected by the RS. We considered an item being “relevant” if it was rated as 3, 4, or 5 on the 0–5 scale. We decided to consider $^ { 3 , }$ 4, and 5 as “relevant” ratings instead of considering only 4 or $5 ,$ as discussed in Herlocker et al. (2004), since our rating scale was from 0 to 5 instead of 1 to $5 ,$ as in Herlocker et al. (2004). Precision for each customer (Pre) was then computed as the average across the nine weeks of the experiment in each treatment. We also measured accuracy by computing the average rating provided by each customer. We computed the average rating provided by each user in each week as the mean rating provided by the user to the N items recommended and rated by the user in each week. The overall average rating provided by each user (Rtn) was then measured as the mean average rating provided during the whole experiment (i.e., over the nine weeks). We computed the precision and the average ratings using the feedback data provided by the customers after receiving each newsletter. We used Pre and Rtn variables in the structural equation model as the two observable variables of a latent variable called accuracy.

3.3.2. Trust. At the end of the experiment, we provided the participants with a final survey in which we asked them to answer the 11 trust-related questions, $\mathrm { Q _ { 1 } }$ through $\mathrm { Q } _ { 1 1 }$ (for details, see Panniello et al. 2015). These questions asked the customers how much they agree on certain statements about the newsletter service. The purpose is to measure how much the participants trusted the received recommendations and to study whether there were differences in customers’ trust across the treatments.

Trust is a multidimensional concept studied by many researchers (McKnight et al. 2002, Schoorman et al. 2007). In particular, Mayer et al. (1995) demonstrated that the three most important dimensions of trust include ability, benevolence, and integrity. Ability (also referred to as competence) represents the ability “of the trustee to do what the truster needs,” benevolence represents the “trustee caring and motivation to act in the truster’s interests,” and integrity represents the “trustee honesty and promise keeping” (McKnight et al. 2002, p. 337). All three concepts are interdependent, as observed by Mayer et al. (1995). Schoorman et al. (2007) insist on the need to measure trust using all three aspects because all three factors can contribute to trust. Several papers, including those in the information systems and e-commerce areas (Ganesan 1994, Jarvenpaa et al. 1998, Gefen et al. 2003, Wang and Benbasat 2005, Pavlou et al. 2007), have defined trust as a multidimensional variable embracing these concepts. In our work, we embraced this prior research on trust and structured our questionnaire so that it was consistent with these prior concepts and definitions of trust, as shown below.

The constructs for trust were derived from prior studies, such as Mayer et al. (1995) and Beldad et al. (2010). We selected and adapted the set of questions and scales used in Doney and Cannon (1997), Wang and Benbasat (2005), and Schoorman et al. (2007). Each answer was provided on the 1–5 scale (for details on trust questions $\mathrm { Q _ { 1 } \mathrm { - Q _ { 1 1 } , } }$ , see Panniello et al. 2015):

• Four questions (from $\mathrm { Q } _ { 2 }$ to $\mathrm { Q } _ { 5 } )$ are measures of ability and investigate the users’ perceptions of whether the recommended products were aligned with the users’ needs.

• Two questions $( \mathrm { Q } _ { 6 }$ and $\mathrm { Q } _ { 7 } )$ are measures of integrity and refer to the ability of keeping commitments and not lying, implying reliability.

• Two questions $\mathrm { ( Q _ { 8 } }$ and $\mathrm { Q _ { 9 } ) }$ are measures of benevolence that focus on the users’ opinion about the firm’s motivations.

We have also included the manipulation check $\mathrm { Q _ { 1 } }$ in the survey, testing the users’ propensity to trust in general. Finally, we had two additional questions, $\mathrm { Q } _ { 1 0 }$ and $\mathrm { Q } _ { 1 1 } ,$ that were not directly related to measuring trust and purchasing behavior. Therefore, we have not included them in this analysis. The fourth question in the survey $\mathrm { ( Q _ { 4 } ) }$ was used as a measure of diversification as defined below. Therefore, seven measures of trust were used in total in the experiment. They were used in the SEM as observable variables of a latent variable called trust.

3.3.3. Diversification. We measured the recommendation diversification in our experiment by measuring both the diversity and the novelty of recommendations. As reported in $\ S 2 ,$ prior research considers novelty and diversity as two aspects of the more general concept of diversification. We used four metrics for diversification, including three metrics for diversity and one for novelty. Each one is described below.

Diversity is defined as the extent to which the items in the recommendation list belong to different categories of items. We use individual diversity, as opposed to aggregated diversity (Adomavicius and Kwon 2012), because we want to evaluate the single individual’s reaction to recommendations. Diversity is measured using the classification of diversity metrics in probability-based, logarithm-based, and rank-based measures (McDonald and Dimmick 2003). Among these metrics we selected the three most popular measures, one from each of the three categories, i.e., the Simpson diversity index (SD), Shannon’s entropy (Ent), and the Tidemann and Hall diversity index (TH) (McDonald and Dimmick 2003), respectively

$$
S D = 1 - \sum_ {i} p _ {i} ^ {2}, E n t = - \sum_ {i} p _ {i} \log_ {k} p _ {i},
$$

$$
T H = 1 - \frac {1}{2 \sum_ {i} r p _ {i} - 1},
$$

where $p _ { i }$ is the proportion of recommended items in the ith category, k is the number of categories, r is the rank of the ith category (ranked with 1 as the largest category).

We used four comic book categories, according to the main classification the company uses to present its products in its website: (1) Marvel comics (including the well-known comic books popularized by the American publisher), (2) Manga comics (including all comic books published in Japan), (3) other comics (including all comic books popularized by either European publishers or American publishers other than the “Marvel” brand), and (4) bundled comics (including any kind of comic books sold in association with a DVD or other media content). The choice of these categories was made in agreement with company management. To provide each data set with a ranking of categories, we used the number of distinct items contained in each category as defined by the relative website. Novelty is defined as the extent to which a customer did not know the items in the recommendation list. We measured the “novelty” of recommendations using the fourth question in the final survey $\mathrm { ( Q _ { 4 } ) }$ , namely, the extent of agreement to the statement “Personalized newsletters recommended comic books that I didn’t know” (for details, see Panniello et al. 2015).

These four measures were used in the SEM as observable variables of a latent variable called diversification.

3.3.4. Purchases. We decided to measure business performance associated with the use of a RS by measuring the purchasing behavior of customers during the experiment. In particular, we measured the following metrics: the money spent by customers and the quantity and prices of the items purchased, as defined below. These metrics were computed both during the nine weeks (two months) of the experiment and during the 20 months before it. We selected these three metrics because (a) they are important metrics of the economic activity of a company, (b) they are directly related to recommendations, and (c) we can easily measure them in our study.

We measured the purchased quantity (Qty) of a product per month per capita in each group (namely, content based, context aware, and control) during the experiment by counting the total number of products bought in each group divided by the number of months divided by the number of customers in each group. We measured the mean monthly expenditure (money spent, Mon) per capita by the customers during the experiment in each group by counting the total amount of money spent in each group divided by the number of months divided by the number of customers in each group.

We also measured the average price (Pri) of the products bought during the experiment by computing the average of the prices of the products bought in each period by each treatment group. We computed the same three measures by using prior customer data related to the 20 months before the experiment (§3.1). The comparison between corresponding measures before and during the experiment is useful to observe changes in the customer purchasing behavior. We used Qty, Mon, and Pri in the SEM as three observable variables of a latent variable called Purchases. Table 1 reports the measures used in the experiment together with their descriptions.

Table 1 Summary of Performance Measures Used in the Experiment

<table><tr><td>Latent variable</td><td>Observed variable</td><td>Unit</td></tr><tr><td colspan="3">Accuracy</td></tr><tr><td>Pre</td><td>Average precision of recommendations</td><td>%</td></tr><tr><td>Rtn</td><td>Average rating provided by the user</td><td>0–5</td></tr><tr><td colspan="3">Diversification</td></tr><tr><td>SD</td><td>Simpson&#x27;s diversity</td><td> $0–1^a$ </td></tr><tr><td>Ent</td><td>Shannon&#x27;s entropy</td><td> $0–1^a$ </td></tr><tr><td>TH</td><td>Tidemann and Hall&#x27;s diversity</td><td> $0–1^a$ </td></tr><tr><td> $Q_4$ </td><td>Novelty (“The personalized newsletter recommended books that I didn’t know”)</td><td>0–5</td></tr><tr><td colspan="3">Trust</td></tr><tr><td> $Q_2$ </td><td>Ability (“The personalized newsletter is like a real expert”)</td><td>0–5</td></tr><tr><td> $Q_3$ </td><td>Ability (“Personalized newsletter provided relevant recommendations”)</td><td>0–5</td></tr><tr><td> $Q_5$ </td><td>Ability (“I am willing to let the personalized newsletter assist me”)</td><td>0–5</td></tr><tr><td> $Q_6$ </td><td>Integrity (“The personalized newsletter is reliable”)</td><td>0–5</td></tr><tr><td> $Q_7$ </td><td>Integrity (“I trust the personalized newsletter”)</td><td>0–5</td></tr><tr><td> $Q_8$ </td><td>Benevolence (“The company created the personalized newsletter to help me”)</td><td>0–5</td></tr><tr><td> $Q_9$ </td><td>Benevolence (“The personalized newsletter is a service provided by the company to customers”)</td><td>0–5</td></tr><tr><td colspan="3">Purchases</td></tr><tr><td>Mon</td><td>Money spent by customers during the experiment</td><td>€</td></tr><tr><td>Qty</td><td>Quantity (number) of items purchased</td><td>#</td></tr><tr><td>Pri</td><td>Average price of items purchased</td><td>€/#</td></tr></table>

<sup>a</sup>Values are continuous numbers raging on a 0 to 1 scale.

## 4. Model Development

As explained in §2, prior research shows that maximizing the recommendation accuracy leads to better economic performance of RS (Schafer et al. 2001). In addition to accuracy, some scholars have also demonstrated the importance of the diversification (Baumol and Ide 1956, Kahn and Lehmann 1991, Brynjolfsson et al. 2003, Fleder and Hosanagar 2009, Adomavicius and Kwon 2012) and the trust measures (Pathak et al. 2010, Pu et al. 2011) in recommender systems. Several scholars have argued that customers’ trust in a RS is driven by the accuracy of its recommendations (Zhang et al. 2011, Bharati and Chaudhury 2004, Swearingen and Sinha 2001, Komiak and Benbasat 2006) and by their diversification (Xiao and Benbasat 2007, Lenzini et al. 2009, Cooke et al. 2002, Adomavicius and Kwon

Figure 2 Structured Equation Model for Testing Our Hypothesis  
![](/api/attachments/ABN668S2/fulltext/images/7024b563cad467df396853b4dd2ce6557d5931aa31f1e0307c0907dc4bdf93ec.jpg)

2012). Finally, Gorgoglione et al. (2011) investigated the correlations between business’s performance outcomes (such as quantity and price of purchased items) and recommendations’ performance (such as accuracy and diversity). They also provided preliminary insights into the effect of customer trust on the aforementioned correlations.

Combining all of these previous results, we developed a model representing the relationship between business performance outcomes, accuracy, diversification of recommendations, and customer trust, where recommendations can be generated by either a contextaware or a context-unaware engine. This model allows us to investigate how contextual information in recommender systems affects a company’s business performance. The model is presented in Figure 2 and is built using structural equation modeling (Bollen 1989). Following Bollen (1989), we used several observed variables (see Table 1 and §3.3) as representatives of four latent variables (see Figure 2).

Before testing our model, we performed several statistical tests to check whether there are significant differences among the three treatments and the population. In particular, we performed t-tests and chi-square tests. We were able to perform such comparison tests with the population at large because the company that collaborated with us on this project gave us access to the demographic and transactional data for the whole population of their customers. In particular, we selected six variables pertaining to demographic and transactional information for each treatment and the whole population: (1) age; (2) gender; (3) number of orders; (4) number of purchased items; (5) money spent on the website; (6) year of subscription (length of the customer relationship with the online shop). For all of these variables, we performed statistical significance tests among the three treatment groups (namely, content based, context aware, and control), and we did not find any statistically significant difference (for $p > 0 . 0 5 )$ . We also performed statistical significance tests between the three treatment groups and the whole population, and we did not find any statistically significant differences either (for $p > 0 . 0 5 )$ These tests were run to check possible differences in the demographic characteristics of the users or in their purchasing behavior before the experiment. Since the results of these tests are not significant (for details on these tests, see Panniello et al. 2015), we conclude that there is no customer attrition during the experiment and that our sample is representative of the whole population of the customers of that company.

Moreover, we checked for biases in the treatment groups with respect to the propensity to trust. We found that the differences between the mean value of the answers to Q in each group were nonstatistically significant. Thus, the users in the different treatment groups were similar in terms of propensity to trust.

We also performed the test of price distributions to exclude any biases that might influence customers’ reactions due to significant difference in the price distributions of the products. To perform these tests, we measured (a) the distribution of the product prices in the whole catalogue and (b) the distribution of the prices of recommended items. We did these tests for both the entire duration of the experiment (nine weeks) and for each week of the experiment. We then performed the analysis of the price distributions for (1) all of the products available in the catalogue in each one of the nine weeks, (2) recommended items versus all of the products available in the catalogue, and (3) recommended items versus all of the products available in the catalogue over the nine weeks. We did not find any statistically significant difference (p > 0005). Additional details of this analysis can be found in Panniello et al. (2015). Based on all this analysis, we can conclude the following:

—prices did not change significantly during the nine weeks, and customers did not perceive any variation in the prices of the products available that might have biased their reaction to recommendations;

—there is no bias in the recommender systems toward recommending more of the highly priced (versus low priced) products, and recommendations were not biased toward certain price categories.

Table 2 Results of the SEM

<table><tr><td>Estimate accuracy → Trust</td><td>1.767 (0.792)*</td></tr><tr><td>Estimate diversification → Trust</td><td>3.541 (1.759)*</td></tr><tr><td>Estimate trust → Purchase</td><td>0.390 (0.183)*</td></tr><tr><td>p-value</td><td>0.360</td></tr><tr><td> $\chi^2/df$ </td><td>1.047</td></tr><tr><td>RMSEA</td><td>0.017</td></tr><tr><td>p-value close to fit</td><td>0.964</td></tr></table>

Notes. Standard errors are in parentheses. RMSEA, root mean square error of approximation.  
<sup>∗</sup>Significant at $\begin{array} { r } { p < 0 . 0 5 . } \end{array}$

Finally, we performed statistical tests on the response rate of each treatment. These tests were useful to ensure that no bias occurred among the treatments in terms of customers’ response that may influence the interpretation of the experimental results. We measured the response rate for each of the nine weeks for the three treatment groups. We then ran the tests of statistical significance to check whether there were differences among the response rates of the three treatments, one per each week, and we did not find any statistically significant differences among them (p > 0005).

After controlling for all of the aforementioned statistical checks, we built a SEM to test our framework (Figure 2). The results (see Table 2) support our model: the regression coefficients are positive and significant.<sup>1</sup> Therefore, we can conclude that the recommendations accuracy and diversification affect customers’ trust, which in turn affects customers’ purchases. This finding does not prove that increasing both accuracy and diversification always causes an increase in trust, which, in turn, causes higher level of purchases. We rather observe that these variables are correlated in terms of a predictive relationship (Shmueli and Koppius 2011). Therefore, this result has immediate implications on RS design and particularly on the goal of this research, i.e., studying how context-aware recommendations affect customer behavior compared to other kinds of recommendations. In §5, these implications are discussed.

## 5. Effect of Context

In this section we analyze how including context in a recommender system affects customer’s purchasing behavior by affecting accuracy and diversification of recommendations, which in turn affects trust and purchases. As a starting point, we show that contextual information affects accuracy and diversification of recommendations. These results are reported in the appendix.

Next, we show the combined effects of accuracy and diversification of the recommendations received by the users across the three treatments, i.e., context aware, content based, and control. For each treatment and each user, we computed the average accuracy and averaged it across the nine weeks and users. Similarly, we computed the average diversification.

Then we plotted accuracy (x-axis) against diversification (y-axis). We followed this procedure for each accuracy (Pre and Rtn) and diversification (SD, Ent, TH, and $\mathrm { Q } _ { 4 } )$ metric combination, thus obtaining eight plots. For the sake of conciseness, we only present one of these plots in Figure 3, where Pre (precision) is plotted against Ent (Shannon’s entropy). The other graphs show similar results. Each point in Figure 3 represents a user, and all of the points representing users in the same treatment (content-based, context-aware, and random recommendations) are marked with the same symbol in Figure 3 and are connected to the centroid of the cluster of users belonging to that treatment in the precision–diversity space of Figure 3. To make the analysis consistent, we considered the subset of users for whom we have complete information (i.e., each user in this subset provided an answer to the final survey), and we can compute the average precision and Shannon’s entropy for each of them.

Looking at the position of the centroid of each treatment in Figure 3 and generalizing the observation to the other metrics, we can state that the content-based recommendations are characterized by high accuracy and low diversification on average, whereas the random recommendations are highly diverse but inaccurate. The context-aware recommendations are more accurate and more diversified than those generated by the content-based RS. Furthermore, context-aware recommendations are significantly more accurate, albeit less diversified than the random ones. These differences among the centroids were significant in all of the eight cases according to t-tests with $p < 0 . 0 0 1$ . Considering Figure 3, we can conclude that context-aware RSs provide more accurate and diversified recommendations than the traditional content-based RSs and significantly more accurate, although somewhat less diverse recommendations than random RSs.

After demonstrating that context-aware recommendations improve both accuracy and diversification versus the traditional content-based recommendations, we conducted one more analysis to empirically validate the consequence of this result. We tested the hypothesis that context affects trust and purchases. We measured the actual purchasing behavior of the customers in the three treatment groups before and during the experiment. Table 3 reports the results.

Figure 3 Accuracy (Pre) vs. Diversity (Ent) of Content-Based (), Context-Aware (×), and Random (<sup></sup>) Recommendations for Each User in These Three Treatments

![](/api/attachments/ABN668S2/fulltext/images/53a7ac2fcbe5df9c027384e0ac81aa61a7f2035baaf51af8bef02b0343b249e4.jpg)

The first two rows report the euros spent (Mon) per month per customer before and during the experiment, respectively. The third row reports the percentage variation. Similar measures are reported for the number of products purchased (Qty) and their price (Pri). The two groups that received personalized recommendations increased the monthly expenditure. The increase in the context-aware group is higher than that of the content-based group: 28.2% and 16.9%, respectively. This finding shows that personalized recommendations are correlated with the increase in customer expenditures, even when a noncontextual RS, such as the one described in this paper, is employed. The monthly expenditure per customer remained almost the same in the control group (3.6%). For the content-based group, the quantity increased (36.8%) and the price of items decreased (−14.5%). On the contrary, the quantity decreased for the context-aware group by 7.7%, whereas the average price of items increased by 38.9%. The quantity decreases by 31.9% in the control group, whereas the few items bought had higher prices (52.1%). The statistical differences were tested using the Wilcoxon test (Barnes 1994).

Table 3 Purchasing Behavior of Customers in the Three Treatments

<table><tr><td></td><td>Content-based</td><td>Context-aware</td><td>Control</td></tr><tr><td colspan="4">Mon (€)</td></tr><tr><td>Before</td><td>2.03</td><td>1.95</td><td>0.91</td></tr><tr><td>During</td><td>2.38</td><td>2.50</td><td>0.94</td></tr><tr><td>%var Qty (#)</td><td>+16.9***</td><td>+28.2***</td><td>+3.6**</td></tr><tr><td>Before</td><td>0.33</td><td>0.37</td><td>0.15</td></tr><tr><td>During</td><td>0.45</td><td>0.34</td><td>0.10</td></tr><tr><td>%var Pri (€/#)</td><td>+36.8**</td><td>-7.7***</td><td>-31.9**</td></tr><tr><td>Before</td><td>6.18</td><td>5.26</td><td>6.20</td></tr><tr><td>During</td><td>5.29</td><td>7.31</td><td>9.43</td></tr><tr><td>%var</td><td>-14.5***</td><td>+38.9***</td><td>+52.1***</td></tr></table>

<sup>∗∗</sup>Significant at p < 0005; <sup>∗∗∗</sup>significant at $p < 0 . 0 1$

Furthermore, to demonstrate that the results in Table 3 are not merely due to the (a) customer-level unobserved effects, (b) time-related unobserved effects, and (c) preexisting systematic differences in trends across groups, we developed the following two econometric models and tested them on the data:

$$
\begin{array}{c} P u r c h a s e _ {i t} = \beta_ {i} + \beta_ {1} M o n t h + \beta_ {2} M o n t h \cdot \mathrm{CARS} _ {i} \\ + \beta_ {3} M o n t h \cdot \mathrm{CONT} _ {i} + \varepsilon_ {i t}, \end{array}\tag{S1}
$$

$$
\begin{array}{r} P u r c h a s e _ {i t} = \beta_ {i} + \beta_ {1} P o s t _ {t} + \beta_ {2} P o s t _ {t} \cdot \mathrm{CARS} _ {i} \\ + \beta_ {3} P o s t _ {t} \cdot \mathrm{CONT} _ {i} + \varepsilon_ {i t}, \end{array}\tag{S2}
$$

where i represents the customer and t time; CARS and CONT represent the context-aware and content-based treatments, respectively; Month is each month before and during the experiment; and Post is a dummy variable equal to 1 if the observation is during the experiment. Purchase is one of the measures in Table 1 (money, quantity, price). In particular, we used (S1) to study whether the changes in Table 3 could be due to customer $( \beta _ { i } )$ , time $( \beta _ { 1 } )$ unobserved effects or to preexisting purchase trends between customers in the context-aware $( \beta _ { 2 } )$ and content-based $( \beta _ { 3 } )$ groups. We used (S2) to measure the net benefit of contextual $( \beta _ { 2 } )$ and content-based $( \beta _ { 3 } )$ recommendations after controlling for unobserved time-related $( \beta _ { 1 } )$ and customer-specific $( \beta _ { i } )$ unobserved factors. The details of the models are provided in Panniello et al. (2015). The results of the analysis conducted by using (S1) demonstrated that there are neither customer-level unobserved effects nor time-related unobserved effects that can increase the purchases across customers $( \beta _ { i }$ and $\beta _ { 1 }$ are not significant). Moreover, there are no preexisting declining or increasing differences in the purchase trends in the CARS and CONT groups $( \beta _ { 2 }$ and $\beta _ { 3 }$ are not significant). The results of the analysis conducted by using (S2) confirmed most of the results presented in Table 3. In particular, both context-aware and content-based recommendations have a positive net effect on the total amount of money spent by users and the quantity of purchased items. In fact, whereas $\beta _ { i }$ and $\beta _ { 1 }$ are not significant, $\beta _ { 2 }$ and $\beta _ { 3 }$ are significant when Purchase is measured by the money spent by customers and the quantity of purchased items (Mon and Qty in Table 1). In the model (S2) built by measuring $P u r c h a s e _ { i t }$ by the average price of the items purchased (Pri in Table 1), no $\beta$ coefficient was significant (except the constant). This means that we can claim that both context-aware and content-based recommendations have a positive net effect on the money spent by customers and the quantity of items purchased, once customer-level and time unobserved effects are excluded.

Based on all of these results, we conclude that col lecting and using contextual information in a RS affects business-related performance measures, such as company’s sales, by improving accuracy and diversification of recommendations, which in turn improves trust and, ultimately, business performance results. In particular, the use of CARSs is correlated with a higher level of money spent purchasing products compared with the use of a content-based RS. The effect of context on business performance can be different if measured by either the quantity of purchased products or the money spent. As Table 3 shows, the customers in the context-aware group slightly decreased the number of items they purchased, but they increased the money spent for purchasing those items, whereas the customers in the content-based group showed the opposite behavior. One plausible explanation of why contextual information leads to more money spent by customers is because of the combined effect of two phenomena in customer behavior. The first is the need for a balance between relevance and diversification. People like relevant items (accurate recommendations) but at the same time want to discover new items and be aware of diverse purchasing options. The second phenomenon is the tendency to balance the expenditure and quantity of purchases. For example, consider a customer who receives a diversified recommendation where she finds both relevant items (she already knew) and novel items (she did not know). The customer has to make the decision of which one to buy. The question is how much she is willing to spend for that novel item versus the relevant but already known one. A plausible explanation is that she will balance money versus quantity. As she has already bought products similar to the relevant item, she may want to reduce the expenditure in favor of quantity (buy more items for less money). On the contrary, if she has never bought a product similar to the novel one, she may be willing to spend more money on that item as a “trial” version, as long as the quantity remains low (e.g., buy only one item and spend more). This constitutes our explanation of the behavior we have observed, i.e., different behavior of customers receiving alternative types of recommendations. It is important to understand that the explanation presented above constitutes only one plausible explanation of the observed phenomenon. This is the case because the research findings presented in this section are based on predictive rather than causal relationships. Since we have not proven true causal relationships between the observed variables, we therefore cannot claim true and unique explanations of the observed phenomena. As a part of future research, we should try to establish and prove the causality of some of the observed relationships.

Finally, it is important to remark that we have measured the users’ overall level of purchase rather than the purchase of the recommended products. We could not limit the observation of purchasing behavior to the products that were both recommended and purchased because it was impossible to collect all of the appropriate data. It would be interesting to demonstrate that using CARSs may lead to the higher levels of purchase of the recommended products, and we should explore it further in our subsequent research. Nevertheless, we maintain that our result that using CARSs leads to higher levels of trust, which leads to higher total purchases, is also important and interesting. This point that all of the aspects of customer trust are really important in recommender systems was further highlighted by Neil Hunt, the chief product officer of Netflix during his keynote address at the 2014 ACM Conference in Recommender Systems (Hunt 2014). Moreover, CARS utilization can potentially lead to higher purchases of both overall and recommended products; i.e., it is very feasible that the increases in sales due to CARSs and higher levels of trust are not limited exclusively to the recommended products.

## 6. Conclusion

Most of the work on CARSs has focused on demonstrating that contextual information leads to more accurate recommendations and on developing efficient recommendation algorithms utilizing this additional contextual information. Little work has been done, however, on studying how much contextual information affects the purchasing behavior of customers. In this paper, we went beyond accuracy and showed how context affects other crucial business-related metrics, such as expenditure of customers, quantity of purchased products, average price, and levels of trust. We have extended the work done by Gorgoglione et al. (2011), which demonstrated that CARS can outperform other kinds of RSs not only in terms of accuracy but also in terms of trust and other economics-based performance metrics. More specifically, in this paper, we have shown in a more systematic manner how context can affect firm’s business performance, such as quantities of goods purchased and the total money spent by customers, by building a comprehensive structural equation model that also includes customer trust and accuracy and diversity of recommendations. We empirically tested the model by conducting a live controlled experiment with customers in a real industrial setting of partnership with a major European publishing firm. We showed that context affects accuracy and diversification, which together affect customer trust, which in turn affects their purchasing behavior.

Although we did not experiment with the algorithms based on the collaborative filtering approach, we expect that these results could be generalized to it as well. For the CF recommendations, it has been demonstrated that context increases accuracy (Adomavicius et al. 2005, Panniello et al. 2012) and diversity of recommendations (Panniello et al. 2012). This implies that, even for the CF systems, CARSs should improve both accuracy and diversity of recommendations. Assuming that accuracy and diversity affect trust, which in turn affects sales, this implies that our model should also hold for the CF-based recommender systems.

The findings of this research have important managerial implications. As argued in this paper, it is important for recommender systems to collect and use contextual data in most of the business applications, such as recommending movies, music, mobile, and many other types of recommendations. Furthermore, we also argued that it is important to do this not only because CARSs improve accuracy of recommendations, which was shown before, but also because they can contribute to the improvement of business performance measures for companies in several significant ways. Therefore, we expect that this work will influence managers in the recommendation companies in favor of adopting CARSs in their recommendation engines since the industry is currently thinking deeply about various ways to add contextual information to the existing recommendation engines.

One limitation of this research lies in that we have not proven causality between context and purchases, but rather established a correlation between these factors. Another limitation is related to the collected data and the fact that the users rate the comic books before they read them in some cases. Although, as explained in this paper, it is a reasonable assumption for this particular application, it would be good to conduct new controlled experiments on this or other applications where ratings are elicited from the users only after they have “consumed” the products.

These limitations and other considerations suggest the following possible future research directions. The first natural research direction would be an attempt to establish causality between context and purchases. Another interesting future research topic would be to show that using CARSs may lead to higher purchase of recommended products and not only to higher overall purchases. Also, as a future work, we would like to test the results reported in this paper on other types of recommendation applications and for other types of industries. This should allow us to generalize and broaden our conclusions and perhaps identify additional factors affecting economic behavior and trust of customers besides the accuracy and diversification of recommendations studied in this paper. Finally, an interesting future research topic would be the investigation of different effects that context-aware recommendations can have on the number of items customers buy and their prices.

## Appendix

Figure A.1 reports the accuracy of recommendations for each group during the nine weeks of the experiment computed by averaging Pre (Figure A.1(a)) and Rtn (Figure A.1(b)) across the users in each treatment. As Figure A.1(a) demonstrates, the precision of the recommendations generated by the contentbased and context-aware RSs are significantly higher than that of the random recommendations (statistically significant with $p < 0 . 0 0 1 )$ . To the contrary, the precision of the contentbased and the context-aware RSs across the nine weeks is similar, i.e., there are no statistically significant differences found between the two groups (p > 005). More details on the comparison can be found in Panniello et al. (2015). These results are reinforced by the similar results reported in Figure A.1(b) showing the average rating provided by users in each week. Similarly to precision, the CARS performed slightly better than the content-based approach starting from week four, as customers provided higher average ratings to the recommended items, whereas the random RS performed worse than the two personalized RSs. Only the differences between the content-based and control groups and between the context-aware and control groups were found to be statistically significant (p < 00001).

Figure A.2 reports the distribution of recommendation accuracy across the users in each treatment. Accuracy was measured by Pre (Figure A.2(a)) and Rtn (Figure A.2(b)) for each customer by considering the whole set of recommendations received during the nine weeks of the experiment. The graph reports the percentage of customers who received a set of recommendations with a certain level of precision (a) or who provided a certain average rating from 1 to 5 (b). The differences between the three groups are statistically significant according to a t-test in all cases with p < 00001 except the difference between the content-based RS and the CARS when accuracy is measured by Rtn. These findings confirm the observation made above. Context has a significant effect on the accuracy of recommendations, given that the CARS outperforms the context-unaware RS (content-based) in terms of precision.

Figure A.3 reports two metrics of diversification for each group during the nine weeks of the experiment computed by averaging Ent (Figure A.3(a)) and TH (Figure A.3(b)) across the users in each treatment (we cannot plot $\mathrm { Q } _ { 4 }$ versus time). The random recommender (control) generated the most diverse recommendations, as expected, at least according to the Ent measure. The TH presents similar values, especially when random recommendations are compared to the context-aware ones, because this index is strongly influenced by the number of item categories. The recommendation diversification for the CARS is always higher than that of the content-based case. The differences are statistically significant according to a t-test in all of the cases with $p < 0 . 0 0 1$ , except the difference between the random recommender and the CARS when diversity is measured by TH. More details can be found in Panniello et al. (2015). Figure A.4 reports the distribution of the diversification metrics for the three groups. The diversity of recommendations was measured using Ent (Figure $\mathrm { A } . 4 ( \mathsf { a } ) )$ , whereas the recommendation novelty was measured by $\mathrm { Q } _ { 4 }$ (Figure A.4(b)). The values of SD and TH are similar to those of Ent. In particular, the y-axes reports the percentage of customers who received a set of recommendations with a certain level of diversification (x-axes). All metrics are computed for each customer by considering the whole set of recommendations received during the nine weeks of the experiment. It is interesting to note that both the diversity and the novelty of the CARS approach are very similar to that provided by a random RS (control), whereas the recommendations generated by the content-based RS were much less diverse and less novel compared to those of the other systems. It is also interesting to note that diversity and novelty are consistent. The recommendations generated by the random RS were perceived by customers in the control group as the most novel, as expected, as Figure A.3(b) shows. The novelty of recommendations generated by a CARS (as measured by $\mathrm { Q } _ { 4 } )$ is close to that of recommendations generated by a random RS and higher than that of recommendations from a content-based RS. Differences are statistically significant according to a t-test in all of the cases. More details are provided in Panniello et al. (2015).

Figure A.1 (a) Precision and (b) Average Ratings of Recommendations in the Nine Weeks  
![](/api/attachments/ABN668S2/fulltext/images/a4f7a94e0f1aca2c9ce8097f0e1242dabeca017ceeafdc878260ef1db09cc45c.jpg)

![](/api/attachments/ABN668S2/fulltext/images/bd1d1a82fa53825840f09f840e7e36aeb2be4ef12ff47fbda3188d98b21bbab8.jpg)

Figure A.2 Distribution of (a) Precision and (b) Average Ratings Across Users  
![](/api/attachments/ABN668S2/fulltext/images/aa78da59c0e7860b546c816d958fad5ce2ba0f8d70174c296932bcc19654fa28.jpg)

![](/api/attachments/ABN668S2/fulltext/images/0d0c41418f99e6f1bf6355f0843323ce4f76a641389ff23a6b8b0808b9d51008.jpg)

Figure A.3 Diversity of Recommendations: The (a) Shannon and (b) Tidemann and Hall Indexes  
![](/api/attachments/ABN668S2/fulltext/images/9920a9751ba4df0270d57a9ed317a46dd10453fe96552f4d6e57a713b7373dd6.jpg)

![](/api/attachments/ABN668S2/fulltext/images/bfcbcb75271dc78d62caf78dcc6025bf3ec107ce3b026ad1bfeebc3aff97b6fb.jpg)

Figure A.4 Distribution of (a) the Shannon Index and (b) Novelty Across Users  
![](/api/attachments/ABN668S2/fulltext/images/7fe6f0ba47d4aaa2cc4c7765f6931df38b4d796ecff83ee9e7da8dbb176854b0.jpg)

## References

Adomavicius G, Kwon YO (2012) Improving aggregate recommendation diversity using ranking-based techniques. IEEE Trans. Knowledge Data Engrg. 24(5):896–911.

Adomavicius G, Tuzhilin A (2005) Towards the next generation of recommender systems: A survey of the state-of-the art and possible extensions. IEEE Trans. Knowledge Data Engrg. 17(6): 734–749.

Adomavicius G, Tuzhilin A (2011) Context-aware recommender systems. Ricci F, Rokach L, Shapira B, Kantor PB, eds. Recommender Systems Handbook (Springer Science + Business Media, New York), 217–253.

Adomavicius G, Sankaranarayanan R, Sen S, Tuzhilin A (2005) Incorporating contextual information in recommender systems using a multidimensional approach. ACM Trans. Inform. Systems 23(1):103–145.

![](/api/attachments/ABN668S2/fulltext/images/6bda0851f347ae73b95895c040e4d399438e97bc2390efa56210469ebe2edc04.jpg)

Amatriain X (2012) Building industrial-scale real-world recommender systems. Sixth ACM Conf. Recommender Systems (ACM, New York), 7–8.

Amatriain X, Basilico J (2012) Netflix recommendations: beyond the 5 stars (part 1). http://techblog.netflix.com/2012/04/netflix -recommendations-beyond-5-stars.html.

Amin MS, Yan B, Sriram S, Bhasin A, Posse C (2012) Social referral: Leveraging network connections to deliver recommendations. Sixth ACM Conf. Recommender Systems (ACM, New York), 273–276.

Barnes JW (1994) Statistical Analysis for Engineers and Scientists (McGraw Hill, Singapore).

Baumol WE, Ide A (1956) Variety in retailing. Management Sci. 3(1): 93–101.

Beldad A, de Jong M, Steehouder M (2010) How shall I trust the faceless and the intangible? A literature review on the antecedents of online trust. Comput. Human Behav. 26(5):857–869.

Bharati P, Chaudhury A (2004) An empirical investigation of decisionmaking satisfaction in web-based decision support systems. Decision Support Systems 37(2):187–197.

Bollen DGFM, Knijnenburg BP, Willemsen MC, Graus MP (2010) Understanding choice overload in recommender systems. Proc. 4th ACM Conf. Recommend. Systems (ACM, New York), 63–70.

Bollen KA (1989) Structural Equations with Latent Variables (Wiley, New York).

Brynjolfsson E, Hu Y, Smith MD (2003) Consumer surplus in the digital economy: Estimating the value of increased product variety at online booksellers. Management Sci. 49(11):1580–1596.

Colson E (2014) Blending human computing and recommender systems for personalized style recommendations. Proc. 8th ACM Conf. Recommend Systems (ACM, New York), http://www .slideshare.net/EricColson/blending-human-computing-and -recommender-systems-for-personalized-style-recommendations.

Cooke A, Sujan H, Sujan M, Weitz B (2002) Marketing the unfamiliar: The role of context and item-specific information in electronic agent recommendations. J. Marketing Res. 39(4):488–497.

Doney PM, Cannon JP (1997) An examination of the nature of trust in buyer–seller relationships. J. Marketing 61(2):35–51.

Dourish P (2004) What we talk about when we talk about context. Personal Ubiquitous Comput. 8(1):19–30.

Fleder D, Hosanagar K (2009) Blockbuster culture’s next rise or fall: The impact of recommender systems on sales diversity. Management Sci. 55(5):697–712.

Flynn LJ (2006) Like this? You’ll hate that. New York Times (January 23) 1, http://www.nytimes.com/2006/01/23/ technology/23recommend.html?emc=eta1&\_r=0.

Ganesan S (1994) Determinants of long-term orientation in buyerseller relationship. J. Marketing 58(2):1–19.

Gefen D, Karahanna E, Straub DW (2003) Trust and TAM in online shopping: An integrated model. MIS Quart. 27(1):51–90.

Gorgoglione M, Panniello U, Tuzhilin A (2011) The effect of contextaware recommendations on customer purchasing behavior and trust. 5th ACM Conf. Recommend Systems (ACM, New York), 85–92.

Herlocker JL, Konstan JA, Terveen LG, Riedl JT (2004) Evaluating collaborative filtering recommender systems. ACM Trans. Inform. Systems 22(1):5–53.

Hu R, Pu P (2011) Enhancing recommendation diversity with organization interfaces. 16th Internat. Conf. Intelligent User Interfaces (ACM, New York), 347–350.

Hunt N (2014) Quantifying the value of better recommendations. 8th ACM Conf. Recommend Systems, Foster City, CA, https:// recsys.acm.org/recsys14/keynotes/.

Jarvenpaa SL, Knoll K, Leidner DE (1998) Is anybody out there? Antecedents of trust in global virtual teams. J. Management Inform. Systems 14(4):29–64.

Kahn B, Lehmann DR (1991) Modeling choice among assortments. J. Retailing 67(3):274–299.

Knijnenburg BP (2012) Conducting user experiments in recommender systems. 6th ACM Conf. Recommend. Systems (ACM, New York), https://recsys.acm.org/recsys12/tutorials.

Knijnenburg BP, Willemsen MC, Gantner Z, Soncu H, Newell C (2012) Explaining the user experience of recommender systems. User Model. User Adapt. Interact. 22(4–5):441–504.

Koenigstein N, Nice N, Paquet U, Schleyen N (2012) The Xbox recommender system. Sixth ACM Conf. Recommender Systems (ACM, New York), 281–284.

Komiak S, Benbasat I (2006) The effects of personalization and familiarity on trust and adoption of recommendation agents. MIS Quart. 30(4):941–960.

Kwon O, Kim J (2009) Concept lattices for visualizing and generating user profiles for context-aware service recommendations. Expert Systems Appl. 36(2):1893–1902.

Lamere PB (2012) I’ve got 10 million songs in my pocket: Now what? 6th ACM Conf. Recommend. Systems (ACM, New York), 207–208.

Lenzini G, Houten YV, Huijsen W, Melenhorst M (2009) Shall I trust a recommendation? Towards an evaluation of the trustworthiness of recommender sites. ADBIS Workshop (Springer-Verlag, Berlin Heidelberg), 121–128.

Liang TP, Lai HJ, Ku YC (2006) Personalized content recommendation and user satisfaction: Theoretical synthesis and empirical findings. J. Management Inform. Systems 23(3):45–70.

Liu Q, Chen T, Cai J, Yu D (2012) Enlister: Baidu’s recommender system for the biggest Chinese Q&A website. Sixth ACM Conf. Recommender Systems (ACM, New York), 285–288.

Mayer RC, Davis JH, Schoorman FD (1995) An integrative model of organization trust. Acad. Management Rev. 20(3):709–734.

McDonald D, Dimmick J (2003) The conceptualization and measurement of diversity. Commun. Res. 30(1):60–79.

McGinty L, Smyth B (2003) On the role of diversity in conversational recommender systems. Fifth Internat. Conf. Case-Based Reasoning (Springer-Verlag, Berlin Heidelberg), 276–290.

McKnight DH, Choudhury V, Kacmar C (2002) Developing and validating trust measures for e-commerce: An integrative typology. Inform. System Res. 13(3):334–359.

Mui YQ (2006) Wal-Mart blames Web site incident on employee’s error. Washington Post (January 7), http://www.washingtonpost.com/ wp-dyn/content/article/2006/01/06/AR2006010601875.html.

Panniello U, Gorgoglione M, Tuzhilin A (2015) CARS we trust: How context-aware recommendations affect customers’ trust and other business performance measures of recommender systems. Working paper, Stern School of Business, New York University, New York.

Panniello U, Tuzhilin A, Gorgoglione M (2012) Comparing contextaware recommender systems in terms of accuracy and diversity. User Model. User Adapt. Interact. 24(1–2):35–65.

Panniello U, Tuzhilin A, Gorgoglione M, Palmisano C, Pedone A (2009) Experimental comparison of pre- vs. post-filtering approaches in context-aware recommender systems. RecSys ’09 (ACM, New York), 265–268.

Pathak B, Garfinkel R, Gopal RD, Venkatesan R, Yin F (2010) Empirical analysis of the impact of recommender systems on sales. J. Management Inform. Systems 27(2):159–188.

Pavlou P, Liang H, Xue Y (2007) Understanding and mitigating uncertainty in online exchange relationships: A principal-agent perspective. MIS Quart. 31(1):105–136.

Pazzani MJ, Billsus D (2007) Content-based recommendation systems. Brusilovsky P, Kobsa A, Nejdl W, eds. The Adaptive Web, Lecture Notes Comput. Sci., Vol. 4321 (Springer-Verlag, Berlin Heidelberg), 325–341.

Pu P, Chen L, Hu R (2011) A user-centric evaluation framework for recommender systems. 5th ACM Conf. Recommender Systems (ACM, New York), 23–27.

Schafer JB, Konstan JA, Riedl J (2001) E-commerce recommendation applications. Data Mining Knowledge Disc. 5(1):115–153.

Schein AI, Popescul A, Ungar LH, Pennock DM (2012) Methods and metrics for cold-start collaborative filtering. 25th Internat. ACM SIGIR Conf. Res. Development Inform. Retrieval (ACM, New York), 253–260.

Schoorman FD, Mayer RC, Davis JH (2007) An integrative model of organizational trust: Past, present, and future. Acad. Management Rev. 32(2):344–354.

Shmueli G, Koppius OR (2011) Predictive analytics in information systems research. MIS Quart. 35(3):553–572.

Simonson I (2005) Determinants of customers’ responses to customized offers: Conceptual framework and research propositions. J. Marketing 69(1):32–45.

Smyth B, McClave P (2001) Similarity vs. diversity. 4th Internat. Conf. Case-Based Reasoning: Case-Based Reasoning Res. Development (Springer-Verlag, London), 347–361.

Smyth B, Coyle M, Briggs P (2012) HeyStaks: A real-world deployment of social search. Sixth ACM Conf. Recommender Systems (ACM, New York), 289–292.

Swearingen K, Sinha R (2001) Beyond algorithms: An HCI perspective on recommender systems. ACM SIGIR Workshop on Recommender Systems (ACM, New York), 393–408.

Swearingen K, Sinha R (2002) Interaction design for recommender systems. Conf. Designing Interactive Systems (ACM, New York), 25–28.

Vargas S, Castells P (2011) Rank and relevance in novelty and diversity metrics for recommender systems. Fifth ACM Conf. Recommender Systems (ACM, New York), 109–116.

Wang W, Benbasat I (2005) Trust in and adoption of online recommendation agents. J. Assoc. Inform. Systems 6(3): 72–100.

Xiao B, Benbasat I (2007) E-commerce product recommendation agents: Use, characteristics, and impact. MIS Quart. 31(1):137–209.

Zhang C, Agarwal R, Lucas HCL (2011) Personalized product recommendations, recommender systems, household production function, retailer learning, laboratory experiment, online product brokering. MIS Quart. 35(4):859–881.

Zhang M, Hurley N (2009) Avoiding monotony: Improving the diversity of recommendation lists. 2009 ACM Conf. Recommender Systems (ACM, New York), 123–130.

Ziegler C, McNee SM, Konstan JA, Lausen G (2005) Improving recommendation lists through topic diversification. 14th International Conf. World Wide Web (ACM, New York), 22–32.
