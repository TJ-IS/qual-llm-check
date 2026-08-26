---
otero_id: 9756
otero_key: "ZV7B8G47"
title: "ExUP recommendations: Inferring user's product metadata preferences from single-criterion rating systems"
authors: "Alfred Castillo; Debra Vander Meer; Arturo Castellanos"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.02.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# ExUP recommendations: Inferring user's product metadata preferences from singlecriterion rating systems

Alfred Castillo <sup>a</sup>, Debra Vander Meer <sup>b,</sup>⁎, Arturo Castellanos <sup>c</sup>

<sup>a</sup> Department of Management, Human Resources, and Information Systems, Orfalea College of Business, Cal Poly San Luis Obispo, San Luis Obispo, CA 93407, United States

b Department of Information Systems and Business Analytics, College of Business, Florida International University, 11200 SW gth Street. RB 256B, Miami, FL 33199, United States

<sup>c</sup> Department of Information Systems and Statistics, Zicklin School of Business, Baruch College, New York, NY 10010, United States

## a r t i c l e i n f o

Article history: Received 20 February 2017 Received in revised form 16 February 2018 Accepted 17 February 2018 Available online xxxx

Keywords: Recommendation system E-commerce Single-rating Product metadata Multi-valued attributes

## a b s t r a c t

Recommendation systems make use of complex algorithms and methods to provide recommendations to consumers. Typically, online rating schemes use a single rating metric that captures the overall user experience with a product. Nevertheless, this might hinder the intricacies of how a product's attributes influence an individual's preferences. While it is possible to use sentiment and semantic analysis to interpret free text in user reviews, if available, to gain insight into a user's reasons for a product rating, these methods are expensive to implement and error prone, and rely on significant data input from the user. To overcome these challenges, we propose a method for inferring user preferences and generating recommendations without relying on the availability or quality of text reviews. Specifically, our method is designed to use existing product metadata and user rating patterns to shed light on how the attributes of a product correspond to individual preferences. Our method uses only the user's history of ratings and the corresponding product attributes to generate predicted ratings for products a user has not yet experienced. This work extends existing work in this area by focusing on multi-valued attributes, and considering the distinct impact of each attribute value in a user's preferences. In terms of computational complexity, our method runs in linear time, making it feasible for real-time implementations. Our experimental results showed that, compared with the two best-performing existing state of the art methods, our method provided review score predictions with up to: 47.7% greater precision, 6.9% greater recall, and 20.5% greater Fmeasure than existing methods.

© 2018 Elsevier B.V. All rights reserved.

## 1. Introduction

Organizations use recommender systems (RS) to better understand their customers' preferences and to leverage that understanding for filtering, recommending, and cross-selling products that the users will like. Techniques in RS use customer-provided data about the various products that they have experienced (e.g., ratings and comments).

The amount of information gathered from users for analysis differs across organizations. The most common implementation is singledimensional, where a customer is simply asked how much he or she liked a purchased product or service on a 5-star Likert-like scale. A onestar rating means that the customer did not like the product, and a fivestar rating indicates that the customer really liked it. This approach has the benefit of simplicity (it requires little effort on the part of the customer and system), which may explain its popularity in use in high-traffic internet sites such as TripAdvisor and Yelp. Netflix previously used the five-star rating system, but recently adopted an even simpler dichotomous thumbs up/down system [1]. These systems have the limitation of producing a single-point data with no dimensional information. Any richness of data related to ratings must be discovered via other means, e.g., text-mining the user provided rating summary. On the other hand, multi-criteria systems are multi-dimensional, where customers are asked for more specific preference information along a range of categories [2]. For example, Zagat asks for information across four criteria describing the user's experience in a restaurant: food, décor, service, and cost. Table 1 shows examples of single-dimension and multiple-dimension rating systems for comparison.

Intuitively, one would expect that providing more rating dimensions for the user to fill in would be beneficial and should therefore represent the majority of implementations. However, a survey of sites that collect user experience data will show that single-dimensional ratings (the focus of this paper) are by far the most common. This begs the question of why organizations would decide against having a multi-dimensional rating scale. It is possible that organizations are hoping to avoid survey fatigue [3], where the number of people willing to provide data is generally inversely proportional to the number of data points they are expected to provide (e.g., trading off richness of data to gain a larger volume of customer input). This reduces the transaction time and provides a better user experience [4].

A. Castillo et al. / Decision Support Systems xxx (2018) xxx–xxx

Table 1  
Domain examples with single and multiple dimension rating systems.

<table><tr><td></td><td colspan="2">Single dimension</td><td colspan="2">Multiple dimension</td></tr><tr><td>Restaurants</td><td>Yelp</td><td>User rating with comments</td><td>Zagat</td><td>Food, decor, service, cost</td></tr><tr><td>Movies</td><td>Netflix</td><td>Thumbs up/down rating</td><td>Kids-In-Mind.com</td><td>Sex &amp; nudity, violence &amp; gore, profanity</td></tr><tr><td>Books</td><td>Barnes and noble</td><td>User rating with comments</td><td>CompassBookRatings.com</td><td>Recommended age, overall rating, profanity/language, violence/gore, sex/nudity</td></tr></table>

A closer look at a typical single-dimension rating scenario reveals opportunities for preference analysis. To illustrate this, consider a scenario where two different sets of people dine in the same restaurant on the same day. One, a mother accompanied by her young children, was impressed with the child-friendliness of the establishment, but did not particularly enjoy the food. Another, an older couple, may have loved the food, but were perhaps less excited about the childfriendly atmosphere. These differences impact the perceptions of their experiences at the restaurant. Suppose that each of these customers were to rate the restaurant a 4 (out of 5), based on their overall experiences. They would do so for vastly different reasons, which are not captured in the single-dimension rating. Here, a collaborative filtering approach would consider these customers to be similar, even though they likely have different preferences, making a content-based approach seem appropriate.

Finding these underlying differences using single-rating data alone is challenging. In cases where users provide textual data describing their rating rationale, the unstructured data may be difficult to analyze due to incompleteness or irrelevance, as well as challenges related to context-dependent word meanings.

Ideally, we would like to have the best of both worlds data-wise: a rich multiple-dimension dataset to build inferences from, and minimal customer effort in required data entry. The products themselves provide an undervalued rich source for additional data, which is clean, as they are objects stored in a database so that they can be dynamically populated on the company website pages. Consider Yelp, for example, where a restaurant is described across a number of features, including the type of food, relative cost, the availability of parking, whether alcohol is served, and a number of other attributes. By understanding the formative relationship of a user's rating to the attributes of a product, it may be possible to infer the diversity of preferences among customers, and improve recommendation accuracy. The challenge is using these product attributes, in conjunction with user recommendation scores, to develop user preferences that are effective at generating recommendations.

In this work, we propose an approach for inferring the embedded dimensionality in user ratings, based on users' rating histories. Our method uses this embedded dimensionality to aid in explaining the variance in ratings users provide across similar products. Because these preferences differ on a person-to-person basis, our approach is based on modeling individuals rather than groups.

Cacheda and colleagues proposed an initial approach to use product attributes and individual preferences to generate recommendations [5,6] (referred to throughout the paper as the “Cacheda” approach). Their work provided recommendations within a specific product label, and considered combinations of product attributes within a product feature as one categorization. Consider the movie Pineapple Express, for example. It is labeled as a crime, action, and comedy movie in the Genre product feature. Any relative evaluation of that movie using the original Cacheda method would have to compare that movie with other movies that were also labeled crime, action, and comedy. This significantly reduces the sample size to draw inferences from, and can create an artificial “cold start” problem even when ample data is available. By not considering how well-received a movie is relative to the multiple populations (i.e., multiple attribute values) it belongs to, Cacheda can only base inferences with the population that shares the full label set. We extend Cacheda's work by viewing a product as a member of possibly many populations, and compare that product relative to the other members that also belong to that categorization. Our approach generates predictions given that a user has provided a rating for other products that also contain some given categorization. This is because preferences are generated for each categorization so that they can be analysed in isolation from the confounding effects inherent to nominal multi-valued attributes. Our methodology, Ex Uno Plures (ExUP) – meaning “out of one, many” in Latin – makes the following contributions:

First, we propose a method for generating individual recommendations based on an individual's tendencies in rating products in combination with multi-valued nominal product description attributes. This method extends Cacheda's original work in this area by considering the contribution of each descriptive attribute relative to each user's preferences, rather than as one set of product attributes. Our method is generalizable to any domain where users provide a singledimension rating for products associated with multi-valued nominal dimensional data.

Second, we performed an analysis of the computational complexity of our method. We show that it maintains linear complexity, updateing for each new product rating in near real-time.

Third, we implemented our method as a prototype to demonstrate the feasibility of our approach. We created a large 10 M record database of movie data and user ratings from online sources to sample from and serve as a testbed dataset for accuracy comparison experiments.

Finally, we ran a set of experiments to compare the accuracy of our method to that of existing methods, and demonstrate that we achieve 6.74% to 47.74% greater precision, 0.76% to 6.85% greater recall, and an F-measure that is 4.79% to 20.54% greater than existing methods. We also ran a set of experiments to show that our method performs well with datasets with various unique attribute set sizes.

The remainder of the paper is organized as follows: In Section 2, we discuss background and related work. In Section 3, we discuss the solution approach and introduce our method. In Section 4, we describe the instantiated ExUp artifact and the experimental setup, and present a discussion of the results. The paper then concludes with a discussion of implications, limitations, and future work.

## 2. Related work

Recommendation systems (RS) are responsible for selecting a subset of items or products that may be of interest for users from a large pool of alternatives, with the assumption that latent user preferences can be inferred from a user's demographic data (e.g., gender, age, income, zip code), explicit transactional data (e.g., product ratings, comments), implicit transactional data (e.g., adding/removing items from carts), or an item's attribute data (e.g., product brand, product price) [7]. RS is used in many web-based implementations from e-learning to e-commerce to e-government [8] via three primary categories: collaborative filtering (CF), content-based filtering, and hybrid approaches [7,9,10]. From an information retrieval perspective, there are also knowledge-based implementations of RS [11]; however these differ from the former three categories of RS in that they rely less on generating latent user preferences, and more on explicitly defined knowledge as the primary mechanism for providing recommendations (e.g., a user profile populated with specific preferences) [12].

The various implementations of RS are similar in goal, matching users with products, but differ in types of algorithm(s) used, the focus of preferential analysis in utility functions, and the type of data used in analysis or generated as part of the process. The most common RS technique is collaborative filtering (CF) [13], which can be: (1) memorybased, via user or item-centric Pearson/vector cosine correlation, or Top-N algorithms [14], or (2) model-based, via constructing models (typically during off-peak hours) that cluster similar users or products based on some criteria [8]. CF implementations infer groupings based on similar behaviors, and then make predictions for future behavior based on the discovered patterns of behavior of the group [14] in order to make a recommendation (e.g., products also enjoyed by “nearest neighbors”), predict ratings (numerical representation or classification of perceived enjoyment on some scale), and provide filtering (omission of items with low perceived enjoyment). Similarly, contentbased (CB) implementations predict future behavior, but with a focus on developing heuristics based on known data-points (e.g., user history, product attributes) to provide tailored recommendations. These systems generate insights via sentiment/semantic analysis of usergenerated content [15], or by leveraging machine learning to analyze user navigation or system interaction patterns [16–18].

When various CF and CB methods are combined in creative ways, combining the strengths of each method (i.e., group methods vs. individual methods, data sparsity, scalability, cold start) [19], the implementation is termed a “hybrid” recommendation system [20–22]. Hybrid methods can leverage CF techniques and CB techniques separately, and then combine the output of each in some fashion, or use the output of one as the input of the other [13]. Essentially, the implementation of a hybrid RS is a strategic solution to a technical problem that depends on what type data is available, what it is needed for, and what types of interesting patterns and associations one might want to surface.

## 2.1. Multi-criteria rating systems

Most rating systems elicit a single-criterion of overall item evaluation from a user. However, this is considered limited in utility due to the multi-dimensional nature of a user's evaluation of an item. Also, inferences based on other user's evaluations (such as clustering) make the assumption that the subjective user preferences are shared among the constituents of the group [23]. Multi-criteria rating systems take into account the multi-dimensional subjective evaluation of an item by a user (e.g., a user rating of 1/5 for “price”, 5/5 for “aesthetics”, and 4/5 for “quality”). These systems provide an important stream of research dealing with context-dependent product filtering, recommendation, and preference elicitation [2,13,23,24].

Techniques for incorporating multi-criteria ratings into recommendation systems are important in increasing the relevance of recommended items to users [2]. However, given the pervasiveness of single-criterion systems, preference data may simply not be explicitly available, requiring the creative use of available data to add meaningful dimensionality (preferential elicitation) for preference analysis. For example, Ansari, Essegaier and Kohli proposed a method using Markov Chain Monte Carlo methods with seemingly disparate data (movie-related features, evaluation from experts, customer demographics) to develop models for customer and product heterogeneity [25]. Si and Jin proposed the Flexible Mixture Model (FMM) to allow for multiple partition/cluster participation of users and products by generating two latent variables for users and products in relation to the ratings [26]. The FMM was used in a multi-criteria setting and combined with a maximum weight spanning tree algorithm (Chow-Liu Tree [27]), to determine the dominant criteria of each user (for grouping purposes) via the removal of the psychometric halo-effect property (e.g., the inability of raters to evaluate criteria independent of the others) [28]. Researchers have applied fuzzy logic and neural networks to determine important product and user criteria used in multi-criteria systems [29,30]. Furthermore, researchers have developed additional metrics of user differences to normalize predictions [31], determine user preferences in a probabilistic model [32], and associate social or emotional factors of users [33].

Most of the literature above is concerned with similarities of products or users. Dissimilarity has also been used, primarily as a mechanism for removing noise from calculated measures (e.g., removing halo-effect, normalizing predictions). Ideally, we would like to build an RS that can utilize those differences directly, which would afford an individualized approach to discovering the relative value of a product within a product space, and of specific user preferences within the contextualized history of that user. Individualized instances of RS are typically computationally costly, which limits their utility in real-time implementations where user experience is important, such as web-based systems [4].

A common approach to producing faster recommendation systems is to extend Agrawal and Srikant's Apriori Algorithm [34]. To improve its performance, there have been attempts at reducing the I/O operations and CPU cycles during database scanning [35] and leveraging infrastructure (such as Hadoop) to minimize the impact of these requirements [36] as well as discovering and producing subgroupings within products [37,38]—an item-centric approach.

Work in multi-criteria recommender systems extends the RS research stream by capturing richer user preferences along several dimensions and incorporating contextual information, increasing the quality of recommendations [17,23]. From a consumer's perspective, the multi-attribute utility theory states that products are a bundle of attributes that consumer's value. Thus, these systems are expected to (1) have a reliable estimation of attribute weights (2) evaluate alternatives offers for users, and (3) have a reasonable expectation of the level of cognitive effort required from the user [39]. In this area there has been much research incorporating the use of non-linear functions and repurposed external data within utility functions to produce better recommendations; yet, the trade-off lies in the cost of increased computational complexity. For example, one approach has introduced fuzzy lookup algorithms combined with social media data to understand a user's social circle's product preferences and generate product recommendations [40]. There is still a need for recommendation systems that can combine product and user-centric approaches to produce accurate recommendations while maintaining real-time feasibility.

## 2.2. The Cacheda recommendation approach

Cacheda looks granularly at the product and user pairings in an attempt to address the sparsity, computational efficiency, and updatability issues that RSs suffer from. It algorithmically calculates the tendencies towards preferences by combining a user- and item-centric approach [5,6]. Cacheda captures tendencies as the average difference between historical ratings to a mean, either based on the item or user. Taking an item-centric approach, the mean is the item's mean for a sample of users, in which case the difference is calculated as an absolute difference from the sample's average on similar items. Complementary to the item-centric component is the user-centric component where the mean is the user's own mean on a subset of products, where the difference is calculated using the user's average rating so that an item can be deemed particularly “good” or “bad” relative to user's history in that subset.

The power of this algorithm lies in its user-centric approach, which allows for an individual-based adjustment for those users which may be generally optimistic (generally positive), or pessimistic (generally negative) [41]. It also normalizes variance between those users which tend to vote conservatively (between middle ranges, smaller standard deviation) and those that vote on the extremes (positive or negative, larger standard deviation) [42]. By understanding these tendencies, an item's rating makes more sense in the context of a user. For example, a rating of a 4 can be very good if the user's history shows an average rating of 3 or less, but is poor for the user if they rate most items a 4.5. The user-centric algorithm captures the variation between the mean of an item and the evaluation of the user in order to correct the mean of the item to one that more closely matches that for the user. The itemcentric algorithm enables one to look at the context of an item in order to evaluate the favorability of it. For example, taking into consideration a group of users' average rating for this type of item, it can determine whether users rate this specific item favorably, or unfavorably within its peer products. The general idea is that tendencies can be calculated, and that they are relative to the user doing the rating, and the item being rated.

There are some limitations with this work. Although categorizations are not explicitly defined, it is reasonable to assume that it must be used in some form (i.e., products must be grouped in some way). In singlegrouping scenarios the algorithm works well and outperforms many other RS algorithms; however, in the presence of multi-criteria systems, it suffers from some of the same issues that it is meant to address (e.g., data sparsity) [2]. In the context of movies, a movie that is categorized as a “drama, romance, $\boldsymbol { \mathbf { \mathit { W } } } \boldsymbol { \mathbf { \vec { d } } } \boldsymbol { \Gamma } ^ { \prime \prime }$ (e.g., Casablanca) would only be able to be compared to other movies in that specific categorization (40 movies out of 10,681 in our IMDB dataset). Although this categorization is meaningful, the likelihood of any user having more than one rating in this specific category to generate accurate user-centric tendencies from it is very small, or non-existent as observed in our dataset of 10 M reviews. The movie could instead be associated with separate calculated tendencies relative to other drama (5979 movies), romance (2556 movies), and war movies (606 movies). This would provide a tendency for relative performance for the product within each category, and a more refined calculation for the user's mean towards products in any category. In this paper we further this approach, which is described in the following section.

## 3. Proposed method and solution approach

Our work builds upon related work and falls under the hybrid approach category and extends the work of Cacheda et al. (2011) [6], which makes the following three assumptions: The first assumption refers to the compensatory dimensionality of a user's rating as a formative construct, comprised of a user's tendency towards viewing the various product attributes as favorable/unfavorable. Second, there is an inherent preference towards certain attributes (user's product choice) causing the prevalence of some attributes over others. This affinity towards a specific product's atomic attributes may not be explicitly present in the user's profile but can be derived based on the user's previous experiences. This results in a matrix of all the user's tendencies for all the product atomic attributes the user has had any experience with. Third, we assume the relative weights for each of the atomic attributes can be combined via linear additive relationships. In this case, ExUP can use this additional learned information about the user with a utility function to provide user-product mappings. The utility function's job is to ensure that users are presented with recommended products with the various combinations of attributes that the user has shown preference towards. Similarly, the utility function should filter out products comprised of attributes they have shown distaste towards. The assumption is that the estimated magnitude (degree) and direction (like/dislike) matters for both the individual and the product. Once preference scores are derived product filtering becomes a straight-forward sorting problem.

In the remainder of this section, we present a model representing the domain space for the study. We leverage work done by Cacheda and colleagues to develop preference metrics for the distinct attributes of a product by a user. We also develop relative product performance as compared to other products that share specific attributes. In Table 2, we present a summary of the notation used throughout the remainder of the paper. In the final part of this section, we describe the method for instantiating ExUP.

A product is described by a set of features that are consistent within a specific type of product. For example, movies can be described by genre, actors, MPAA rating, or director, while restaurants can be described by cuisine, atmosphere, dress code, and other feature descriptors. For a given feature, we can describe all possible label values for the feature as $\mathsf { V } = \{ \mathsf { v } _ { 1 } . . . \mathsf { v } _ { | \mathsf { V } | } \}$ . In this work, consistent with generating models for RS for some predetermined categorization (such as when a user is browsing categories), we limit our analysis to a single feature (which may be multi-valued) as a basis for predicting ratings. Some features will naturally have a single value because they are mutually exclusive (i.e., a movie cannot have an ‘R’ MPAA rating and a “PG-13” MPAA rating), but that is not true of all features (i.e., a movie does not typically have a single actor, but rather an entire cast of actors). Thus, for the remainder of this paper, when we refer to V, we refer to the set of possible values for the selected feature of interest. The feature “Genre” has the following set of possible values: V = {action, adult, adventure, animation, biography, comedy, crime, documentary, drama, family, fantasy, filmnoir, history, horror, music, musical, mystery, romance, scifi,

short; sport; thriller; war; western :

We identify the set of labels in V that apply to a product i as V ⊆ V. We further identify the set of products in I for which a label v applies as $I _ { v } \subseteq I .$ Operationally, we define a table that captures all product-label detail where the rows are products and the columns are feature values. The table is illustrated with example data in Table 3, where each row describes $V _ { i }$ for a product i, and each column describes $I _ { v }$ for a value v. The members of V are simply the feature values that exist for the product (coded as $" 1 "$ in the table) (e.g., $V _ { F r o z e n } =$ {animation,comedy, adventure (not shown)}). Alternatively, we can also look at product memberships for a specific value $I _ { \nu }$ (where the product is coded 1 for a column) (e.g., $I _ { C o m e d y } =$ {bettle juice,frozen,office space}).

A user provides a single numeric rating r of a product $r _ { u , i } \in$ {min(r) … max (r)}, which represents the degree of enjoyment user u experienced with product i. A user/product rating table can be created such that the intersections are user ratings (see Table 4). The typical rating system is of the set of whole numbers from one to five (inclusive), $[ 1 , 5 ] \in \mathbb { Z } ,$ but the data set we are using contains half-star ratings: {1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5}. A product's average rating for all users (population) is $\overline { { \pmb { r } _ { U _ { i } } } } |$ (the column average in Table 4). Normally, this average is

Table 2 Summary of notation.

<table><tr><td>Notation</td><td>Meaning</td></tr><tr><td>U</td><td>Set of all users (u), such that  $U = \{ u_1...u_{|U|} \}$ . Subscripts identify subsets of users containing a specific attribute of interest. For example,  $U_i$  would refer to the set of all users that have rated a specific product (i), such that  $U_i \subseteq U$ .</td></tr><tr><td>I</td><td>Set of all products i, such that  $I = \{ i_1...i_{|I|} \}$ . Subscripts identify subsets of products containing a specific attribute of interest. For example,  $I_u$  would refer to the set of all products that have rated by a specific user (u), such that  $I_u \subseteq I$ .</td></tr><tr><td>V</td><td>Set of all possible label values for a label category, such that  $V = \{ v_1...v_{|V|} \}$ . Subscripts identify subsets of products containing a specific attribute of interest. For example,  $V_i$  would refer to the set of all label values that belong to a specific product (i), such that  $V_i \subseteq V$ .</td></tr><tr><td>R</td><td>Set of ratings r available to users, such that  $R = \{ \min(r) ... \max(r) \}$ . In this study,  $R = \{ 1,1.5,2,2.5,3,3.5,4,4.5,5 \}$ .</td></tr><tr><td>ru,i</td><td>A single rating by a user (u) for a product (i), such that ru,i ∈ R.</td></tr><tr><td> $\overline{r}_{U_i}$ </td><td>The average rating for a product (i) across all users who have rated it (Ui), such that  $\overline{r}_{U_i} \in \mathbb{Q}$ . The subscript will vary depending on the average rating to be calculated, but will follow the conventions identified in this table.</td></tr><tr><td>tu,v</td><td>The calculated tendency of a user (u) towards a specific feature value (v). The subscript will vary on the tendency to be calculated (item-centric/user-centric) but will follow the same conventions identified in this table.</td></tr><tr><td colspan="2">In this study, a set of users  $U = \{ u_1...u_{|U|} \}$  provide ratings for a set of products,  $I = \{ i_1...i_{|I|} \}$ , where the set of products that a specific user has rated is  $I_u \subseteq I$  and the set of users that have rated a specific product is  $U_i \subseteq U$ .</td></tr></table>

Please cite this article as: A. Castillo, et al., ExUP recommendations: Inferring user's product metadata preferences from single-criterion rating systems, Decision Support Systems (2018), https://doi.org/10.1016/j.dss.2018.02.006

Table illustration of products and value labels

<table><tr><td rowspan="2">Product</td><td colspan="6">Values</td></tr><tr><td>Animation</td><td>Drama</td><td>Comedy</td><td>Crime</td><td>Fantasy</td><td>...</td></tr><tr><td>Beetle Juice</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>...</td></tr><tr><td>Frozen</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>...</td></tr><tr><td>Office Space</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>...</td></tr><tr><td>The Godfather</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>...</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td></td></tr></table>

given to users by the systems; a final average rating along with the number of users that have rated it to arrive at that average. The system's average for all users will be used when available and calculated otherwise. A user's average rating for all the products they have rated is $\overline { { r _ { I _ { u } } } }$ (the row average in Table 4). As an example, a user (u = 123) rated a movie called “Office Space” $( i = { 3 } ^ { " } )$ ) with a rating of 2.0 (therefore, $r _ { 1 2 3 , 3 } = 2 . 0 )$ , yet this movie had an average rating by all users of a 4.2 (therefore, $\overline { { \overline { { r _ { U _ { 3 } } } } } } = 4 . 2 $ :Also, this user (u = 123) has rated on average <sup>¼</sup>all movies a 3.25 $( \overline { { r _ { I _ { 1 2 3 } } } } = 3 . 2 5 )$ (refer to Table 4).

## 3.1. Solution details

Tendencies are calculated for the user (user-centric), and for the feature's value (item-centric). The user's tendency (favorable or unfavorable) towards a feature value is relative to how the user has rated other products. If the user finds this feature value favorable, then the resulting tendency should be positive (above the user's mean). Conversely, if the user finds this feature value unfavorable, then the resulting tendency should be negative (below the user's mean). We therefore define the tendency of a user towards a feature value $( t _ { u , v } )$ as the average difference between a user's product rating of products containing a specific feature value and the user's average rating for all products (see Formula 1). Once these are calculated for all feature values in the user's history, they serve as lookup values for evaluating a user's overall tendency (deviation from mean) for the specific combination of feature values belonging to a product being evaluated. These values can be combined via a simple average; however the frequency of each feature value that exists in the user's history provides an implicit preference by the user. Therefore, we define the final tendency $( t _ { u , v _ { i } } )$ of a user towards a product's multi-valued feature set as a weighted average of all the feature value tendencies calculated for the user, that belong to the product (see Formula 2).

$$
t _ {u, v} = \frac {\sum_ {i \in I _ {u , v}} \left(r _ {u , i} - \overline {{r _ {I _ {u}}}}\right)}{\mid I _ {u , v} \mid}\tag{1}
$$

$$
t _ {u, V _ {i}} = \frac {\sum_ {v \in V _ {i}} \left(| I _ {u , v} | * t _ {u , v}\right)}{\sum_ {v \in V _ {i}} | I _ {u , v} |}\tag{2}
$$

If the users regard a product within a specific feature value as good or bad, this is relative to the other products the population has experienced within that feature value. In this manner, the product may be considered good as an “action” movie if it has an elevated rating compared to other “action” movies, but considered poor as a “comedy” if it has a lower rating when compared to other “comedy” movies. Therefore, we define the tendency of a product within a specific feature value $\left( t _ { i , \nu } \right)$ as the average difference between the product's average rating and that of other products within its specific feature value (see Formula 3). For clarity, where i denotes the product for comparison it is held constant as i = 123, and where it varies as elements of a set it is kept simply as i. Some feature values are more popular and have a more accurate mean. These tendencies are also combined in a weighted method for all feature values of the product to arrive at an overall tendency for the product $( t _ { i } ,$ Formula 4).

Table illustration of users and products with rating data.

<table><tr><td rowspan="2">Users</td><td colspan="5">Products</td><td rowspan="2">User avg.</td></tr><tr><td>Beetle Juice</td><td>Frozen</td><td>Office Space</td><td>The Godfather</td><td>...</td></tr><tr><td>123</td><td>2</td><td>4.5</td><td>2</td><td></td><td>...</td><td>3.25</td></tr><tr><td>404</td><td>4</td><td></td><td>5</td><td>4</td><td>...</td><td>4.33</td></tr><tr><td>311</td><td></td><td>5</td><td></td><td>2</td><td>...</td><td>4.8</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>

$$
t _ {1 2 3, v} = \frac {\sum_ {i \in I _ {v}} \left(\overline {{r _ {U _ {1 2 3}}}} - \overline {{r _ {U _ {i}}}}\right)}{\left| I _ {v} \right| - 1}\tag{3}
$$

$$
t _ {1 2 3} = \frac {\sum_ {v \in V _ {1 2 3}} \left(| I _ {v} | * t _ {1 2 3 , v}\right)}{\sum_ {v \in V _ {i}} | I _ {v} |}\tag{4}
$$

The formulas for predicting the final rating of a product for a user $( r _ { u , i } )$ use the average rating of the user (r ) in combination with the calculated tendency for the item's feature set (t ), and also use the average rating of the product $\left( \overline { { r _ { U _ { i } } } } \right)$ in combination with the calculated tendency for the <sup>Þ</sup>user on that particular value set that belongs to the product $( t _ { u , V _ { i } } ) .$ . The possible outcomes are represented graphically in Fig. 1, where the solid horizontal lines are the resulting prediction. If the tendencies are both (for user and product) positive (see Fig. 1a), then Formula 5 is used (max function) to use the tendency that has the greatest positive impact (e.g., an outstanding product within its aggregate category, or a product with an exceptionally appealing feature set for the user). If the tendencies are both negative (see Fig. 1b), then Formula 6 is used (min function) to also use the tendency that has the greatest negative impact (e.g., a deplorable product within its aggregate category, or a product with a feature set that is highly disliked by the user). If one tendency is positive and the other is negative, one of two things can happen. If the sums converge (see Fig. 1c), then Formula 7 is used (min(max) function). However, if the sums diverge (see Fig. 1d) then Formula 8 is used (weighted average). The sums for determining convergence/divergence are: (1) the user average rating with the item tendency, (2) the item average rating with the user tendency. These formulas are adopted from the work of Cacheda and colleagues [5,6].

$$
r _ {u, p} = \max \left(\overline {{r _ {I _ {u}}}} + t _ {i}, \overline {{r _ {U _ {i}}}} + t _ {u, V _ {i}}\right) (\text { See   Fig.1a })\tag{5}
$$

$$
r _ {u, p} = \min \left(\overline {{r _ {I _ {u}}}} + t _ {i}, \overline {{r _ {U _ {i}}}} + t _ {u, V _ {i}}\right) (\text { See   Fig.1b })\tag{6}
$$

$$
\begin{array}{l} r _ {u, p} = \min \big (\max \big (\overline {{r _ {I _ {u}}}}, (\overline {{r _ {I _ {u}}}} + t _ {i}) (1 - \beta) + \big (\overline {{r _ {U _ {i}}}} + t _ {u, V _ {i}} \big) \beta \big), \overline {r _ {U _ {i}}} \big) \\ \times (\text { See   Fig.1c }) \end{array}\tag{7}
$$

$$
r _ {u, p} = \overline {{r _ {U _ {i}}}} \beta + \overline {{r _ {I _ {u}}}} (1 - \beta) (\text { See   Fig.1d })\tag{8}
$$

## 3.2. Data structures and methods

Our method requires four data structures, which can be implemented in main memory as a multidimensional array, or in auxiliary memory, such as tables in SQL server. These data structures serve as lookup tables for fetching values, and for updating whenever there is a change. The first of these, P, is a IxVmatrix. The rows represent all products (i ∈ I) of interest, while the columns represent all possible values $( \nu \in V )$ for a given feature (i.e., genre). The intersection (P[i,v]) contains $\ " { 1 } \ "$ if it is a feature value for that product $( \nu \in V _ { p } ) .$ , and $" 0 "$ otherwise (refer to Table 3). The second matrix, Q, is a UxI matrix. The rows represent all users in the system (u ∈ U), while the columns represent all current products within the

A. Castillo et al. / Decision Support Systems xxx (2018) xxx–xxx

![](/api/attachments/ZV7B8G47/fulltext/images/dcc59ad77ea4ccf6ad617e006fa99affe07c7fb61e4f63abb268a13d2f16216b.jpg)  
Fig. 1. Graphical representations of possible relations between means (circles) and tendencies (arrows), adapted from [6].

domain of interest (i ∈ I). The intersection is the user's rating of a particular product $( Q [ u , i ] = r _ { u , i } )$ (refer to Table 4). The computational complexity in generating these tables is O(mn), where m is the number of rows and n the number of columns. To minimize the operational impact of generating and updating these tables in a potentially large system (millions of users and products) the data structures should be created in auxiliary memory, if they do not already exist.

There are three situations that trigger updates to these two matrices: a new user (u ∉ U), new product (i ∉ I), or new rating by a user on a product. The updates for these tables are straightforward. A new user results in an additional row added to the Q matrix $( Q [ u , * ] )$ . A new product results in an additional row to the P matrix $( P [ i , * ] ) ,$ , which is populated with 1’s where $\nu \in V _ { p \cdot } A$ new product also results in an additional column to the Q matrix $( Q [ * , i ] )$ . Finally, a new rating by a user (u) on a product (i) results in an update the Q matrix where Q $[ u , i ] = r _ { u , i }$ . The computational complexity of adding a row/column or updating a cell is linear O(1).

These matrices are used as references to generate the tendency tables for products. Every product will have its tendency calculated for each specific feature value $\left( t _ { i , \nu } \right)$ resulting in a final tendency for the product (t ). Note that if there is no history of user ratings for a product, then the tendency estimated is 0 as we cannot assume there is any deviation, and the mean is estimated from all products within that product's categorizations (Algorithm 1, lines 3, 14–16). The average product rating for the products can either be from a readily available source (typically stored in a table) or it can easily be calculated as the column average of Q (Algorithm 1, line 4). The computational complexity for generating a product's relative performance for all applicable label values is linear. These are computed as follows for a specific product (i = 123), which Algorithm 1 describes in detail.

## Algorithm 1. Generate product tendencies for label values (e.g., label values of {action, drama, romance})

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1. input product = 123, Q[u,i]
2.
3. if Q[*,product] is not empty then
4. assign  $\overline{r_{U_{123}}}$  = average of Q[*,product] //avg rating of product
5. for each v where P[product,*] = 1 //labels of the product
6. assign labelNumerator = 0
7. assign labelCounter = 0
8. for each i where P[*,v] = 1 //other items with label
9. assign valueNumerator +=  $\overline{r_{U_{product}}}$  - average of Q[*,i]
10. assign valueCounter++
11. end loop
12. assign  $t_{product,v}$  = labelNumerator/labelCounter
13. return  $t_{product,v}$ 
14. end loop
15. else
16. assign  $t_{product,v}$  = 0
17. return  $t_{product,v}$ 
18. end if
</div>

The returned tendencies for the product on each label value membership is then populated into a matrix that mirrors the structure of P (the rows are products and the columns are the label values) with the exception that instead of a 1 or 0 the cell value is either null (no tendency calculated) or what was returned by Algorithm 1. We will call this matrix W[i, v]. If it is desirable to provide recommendations on categorical search parameters (e.g., Genre = “action”) for a user that we have no knowledge of, then providing a top-N recommendation of the preferred products under this label value is a straightforward sorting exercise on W for that categorization. Otherwise, a final tendency based on some categorization for label values (e.g., Genre) for a product can be computed by using this matrix as a lookup for generating a final tendency for a product based on some feature (e.g., Genre), with linear computational complexity, as follows, which Algorithm 2 describes in detail.

## Algorithm 2. Generate aggregate product tendency for label Categories (e.g., Genre)

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
(e.g., Genre)

1. Inputs: product = 123, W[i, v], P[i, v], Q[u, i]
2.
3. assign finalNumerator = 0, finalCounter = 0
4. for each v where W[product, *] is not null //label value
5. assign entriesInV = Count(P[*, v])
6. assign finalCounter += entriesInV
7. assign finalNumerator += entriesInV * W[product, v]
8. end loop
9. assign $t_{product}$ = finalNumerator/finalCounter
10. return $t_{product}$
11. end loop
</div>

The matrices are also used as references to generate the tendency tables for users. Every user will have their tendency calculated for each specific feature value $\left( t _ { u , \nu } \right)$ . The user's preferences can then serve as a lookup table to find optimal combinations, to do filtering of products depending on search criteria, or to predict a product's specific tendency for the user. These are computed as follows for a specific user $( u = 3 2 1 )$ on all features of some product (i = 123), but can also be done for the features of all products to populate the user tendencies initially, which Algorithm 3 describes in detail.

## Algorithm 3. Generate user tendencies for label values (e.g., label values of {action, drama, romance})

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1. input user = 321, product = 123 or *, Q[u,i], P[i,v]
2.
3. if Quser,*is not empty then
4. assign $\overline{r_{l\_user}}$ = Average of Q[user,*] //user average rating
5. for each v where P[product,*] = 1
6. assign valNumerator = 0
7. assign valCounter = 0
8. for each i in P[*,v] and Q[user,*]
9. assign valNumerator = valNumerator + r_user,i - $\overline{r_{l\_user}}$
10. assign valCounter++
11. end loop
12. if valCounter &lt;&gt; 0 then
13. assign t_user,v = valNumerator/valCounter
14. else
15. assign t_user,v = 0
16. end if
17. return t_user,v and valCounter
18. end loop
19. end if
</div>

The returned tendencies for the user on each label value is then populated into a new matrix that mirrors the structure of W, with the exception that the rows are now users instead of products, and the cell contains the results of Algorithm 3. We will call this matrix Y[u,v]. For quick updates the valCounter variable should be kept track of in another matrix that mirrors Y, with the exception that it has the counts in the cells instead of the calculated tendencies. We will call this count matrix $Z [ u , v ]$ . If it is desirable to provide filtering on products of desirable attributes $( \mathrm { e . g . , G e n r e = " a c t i o n " } )$ for a user, then providing a top-N recommendation of the best products under preferred label values is a straightforward sorting exercise on Y. Otherwise, a final tendency based on some categorization for label values (e.g., Genre) for a specific product can be computed by using this matrix as a lookup for generating a final tendency for a product based on some feature (e.g., Genre), with linear computational complexity resulting in a final tendency for a specific feature set $( t _ { u , V _ { i } } )$ , which Algorithm 4 describes in detail.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 4. Aggregate user tendency for Category (e.g., Genre)

1. input user = 321, product = 123, Y[i, v], Z[i, v]
2.
3. assign numerator = 0, denominator = 0
4. for each v where P[product,*] = 1 //the label values
5. assign numerator = numerator + (Z[user, v]*Y[user, v])
6. assign denominator = denominator + Y[user, v]
7. end loop
8. if denominator &lt;&gt; 0 then
9. assign $t_{u,V_i}$ = numerator/denominator
10. else
11. assign $t_{u,V_i}$ = 0
12. end if
13. return $t_{u,V_i}$
14. end if
</div>

Predictions can then be generated by inputting the average rating for the user, the average rating for the product, the result of Algorithm 2, and the result of Algorithm 3 into one of the Formulas 5 through 8, depending on the considerations illustrated in Fig. 1 which would be implemented in logic. To find out if tendencies are positive or negative all that needs to be done is to compare the tendency calculated and check if it is greater than or equal to 0, or not. If they go in opposite directions (one is positive and the other is negative), determining whether they converge or diverge is also relatively straight forward once we know which mean is greater, and if the tendency is positive or negative. The lesser of the two averages will either have a tendency that is positive (showing convergence), or negative (showing divergence). The greater of the two averages will either have a tendency that is positive (showing divergence), or negative (showing convergence). It is only necessary to check both when the first one checked is based on a tendency of zero (assumed positive, but means neutral).

## 4. Experimental study

In this section we compare the performance of ExUp to CF and the original Cacheda et al. method. We use the commonly accepted metrics of recall, precision, and F-measure [21] to measure accuracy across all methods. Recall (R) reflects the percentage of correct positive predictions out of all the possible positives in the evaluation set, while precision (P) reflects the percentage of correct positive predictions out of the predicted positives. The F-measure (F) is simply a ratio of overall goodness of fit for precision and recall (see Table 5). In the subsections that follow we describe how these metrics were gathered and compared.

Cacheda's algorithm was somewhat challenging to develop because using the entire multi-valued product label provided little utility due to the low availability of similarly labeled data in the training set (a limitation addressed in this paper). As a result, most of the records in the scoring dataset resulted in using the population average ratings for prediction. The primary method of extracting data would be generating predictions based on the entire label (e.g., “drama, foreign, comedy”), which would artificially reduce the results of Cacheda as a function of low data availability rather than a function of their method. To address this, the data was prepared as dummy coded dataset, with binary values indicating presence (1) or absence (0) of a singular attribute, of all user ratings, and products such that predictions can be generated for each user/product on each attribute. This preserves comparable testing for all algorithms absent a viable alternative.

The beta used in Formulas 7 and 8 should be established empirically. We performed the experiment on each beta from 0.1 to 0.9, analyzing RMSE, and precision and recall measures to identify the ideal beta for inclusion in the study. The best RMSE performing beta was $0 . 5 ,$ which was non-statistically different from 0.6 or 0.4 at the 0.05 level of significance. Recommendations systems are used to provide product recommendations, making Like/Dislike precision and recall scores a better indicator of performance. The results in the later showed 0.6 as the best beta, which was also found to achieve the best results in the original Cacheda works. As a result, the beta of 0.6 was chosen for both.

For the CF component Weka was used to instantiate a k-nearest neighbors classifier, IBk [43]. We selected this because of its ability to identify the optimal value of K based on cross-validation. We used a brute force algorithm called LinearNNSearch to establish Euclidean distances between the neighbors. After several training iterations of various sizes (up to 1000 neighbors), we found that a value of 22 for nearest neighbors (K) was the optimal setting for this dataset.

## 4.1. Data gathering and data cleaning

We started by using the publicly available 10 million record dataset from MovieLens.org. Although the dataset was rich in quantity of user ratings, it did not have any details about the \~10,000 movies, besides a title. We needed to tie in valid external aggregate ratings and descriptive data about each movie title from a high-volume website, such as IMDB.com. Using external aggregate ratings have been shown to improve recommendation systems, as long as the external source is statistically representative of the population (or individual) of interest [44]. For simplicity, we did not stratify the external rating data to generate sub population aggregate ratings based on some stereotyping of the individual (e.g., males only, age 18–25, etc.).

The title was used as a seed value to obtain the data from other websites programmatically. The MovieLens IDs of the movies served as a lookup to obtain the IMDB.com IDs. Any movies that did not have a direct translation were programmatically looked up via JSON calls with a fuzzy lookup (criterion set to 90% match threshold for over 5 characters, and 100% match threshold for anything equal to or b5 characters) based on the title search results of the movie on IMDB's API. The conversion from Movie Lens ID to IMDB\_IDs was then used to obtain all the information about the movies that exists on IMDB.com. The repetitive structure of the IMDB.com website made it feasible to use XPath expressions and Ruby scripts to automate the data collection. Binary lookup tables were created for multi-valued non-parametric attributes, such as genre, that are similar to that of Table 3. Genre is an n-valued attribute where the mean count of $n { = } 3$ , minimum is $n { = } 1$ , and maximum is n=9. A random sample of 54,816 total ratings was extracted from the full dataset by identifying enough users randomly to exceed the 50,000 threshold for the study. To ensure consistency, the same datasets used for train (randomly selected 70% of the data) and test (randomly selected 30% of the data) were used for all three systems.

Predictive performance metrics.

<table><tr><td>Precision</td><td>Recall</td><td>F-measure</td></tr><tr><td> $P = \frac{TP}{TP+FP}$ </td><td> $R = \frac{TP}{TP+FN}$ </td><td> $F = \frac{2(P*R)}{P+R}$ </td></tr></table>

## 4.2. Results

We present the results of our experiments in Table 6. Following [21], the performance of CF and Cacheda et al. were contrasted with that of our method via the F-measure. Although it is important to ensure that all items recommended are indeed favorable, it is also important to not incorrectly categorize favorable products as non-favorable. This is why the F-measure is better suited for recommendation systems, as it provides a harmonic mean of the precision and recall. We also performed a z-test for proportions [45] for precision and recall to identify where we significantly outperformed the other methods prior to comparing F-measures. Statistically significant differences for precision, recall, and F-measure were calculated and are highlighted with an asterisk symbol (\*).

The absolute difference in F-measure is substantial if it is N0.05, and the difference in at least one of its components (i.e., precision or recall) is statistically significant (determined using the z-test for proportions at the significance level of 0.05, two-tailed, critical value of z = 1.96) [21].

Numeric results are for raw scores (a prediction of [1,5]). However, Like/Dislike/Neutral results are more relevant for recommendation systems as their goal is to provide recommendations that a user will like, filter those that they will not like, and possibly take a chance on those that the user may be neutral about. In this way, the raw score predictions were binned to show that they liked it (prediction of 4, 5), disliked it (prediction of 1, 2), or were neutral (prediction of 3).

Numerical predictions for ExUp showed a performance increase of: (1) 47.74% in the precision (0.169 above 0.354), 6.86% in the recall (0.017 above 0.248), and 20.55% in the F-measure (0.06 above 0.292) of CF's; and (2) 14.19% in the precision (0.065 above 0.458), 0.76% in the recall (0.017 above 0.248), and 5.39% in the F-measure (0.018 above 0.334) of Cacheda. Like/Neutral/Dislike predictions for ExUp showed a performance increase of: (1) 9.83% in the precision (0.051 above 0.519), 4.16% in the recall (0.018 above 0.433), and 6.57% in the F-measure (0.031 above 0.472) of CF's; and (2) 6.74% in the precision (0.036 above 0.534), 3.20% in the recall (0.014 above 0.437), and 4.79% in the F-measure (0.023 above 0.480) of Cacheda. The results for our method were significantly different (α = 0.05) than both CF and Cacheda. for all precision comparisons, and all but one recall comparisons. Recall was not significantly greater than CF's for Like/Neutral/Dislike predictions. The F-measure for ExUp was greater for all scenarios, but only reached significance in the numerical comparison against CF due to the differences between the F-measures not achieving a difference of at least 0.05.

To allow for a deeper understanding of where ExUp may be beneficial, we compared precision and recall for users binned based on their system use (see Fig. 2). The data was heavily skewed on number of reviews and required a log transform in order to evenly separate users into five groups based on their system use (number of reviews). The choice of number of bins was made by using histograms of experimental RMSE values and finding the best fit based on distribution. The final choice was five bins with the following labels: “1” (reviews b45; group average 28.66); “2” (45 ≤ reviews b102; group average 66.51); “3” 102 ≤ reviews b225; group average 149.78); “4” (225 ≤ reviews b510 reviews; group average 332.28); and “5” (510 b reviews; group average 724.77) (see Fig. 2).

Results for the 2 (Numeric, Like/Dislike) × 3 (RS algorithms) comparison, asterisk indicates significant difference (α = 0.05, two-tailed).

<table><tr><td></td><td></td><td>ExUP</td><td>Cacheda</td><td>CF</td></tr><tr><td rowspan="5">Numerical</td><td>Precision (P)</td><td>0.523</td><td>0.458*</td><td>0.354*</td></tr><tr><td>P z-score</td><td>Used for Comparison</td><td>13.08</td><td>34.27</td></tr><tr><td>Recall (R)</td><td>0.265</td><td>0.263</td><td>0.248*</td></tr><tr><td>R z-score</td><td>Used for Comparison</td><td>0.457</td><td>3.920</td></tr><tr><td>F-Measure</td><td>0.352</td><td>0.334</td><td>0.292*</td></tr><tr><td rowspan="5">Like/Dislike</td><td>Precision (P)</td><td>0.570</td><td>0.534*</td><td>0.519*</td></tr><tr><td>P z-score</td><td>Used for Comparison</td><td>7.28</td><td>10.30</td></tr><tr><td>Recall (R)</td><td>0.451</td><td>0.437*</td><td>0.433*</td></tr><tr><td>R z-score</td><td>Used for Comparison</td><td>2.835</td><td>3.650</td></tr><tr><td>F-Measure</td><td>0.503</td><td>0.480</td><td>0.472</td></tr></table>

Although ExUp does seem to perform well even with newer users that haven't interacted much with the system (see Fig. 2), the mild degradation for users with much higher system use initially was thought to reflect sensitivity towards the recency of historical reviews; however this was subsequently dismissed via additional analysis. The review data spans 14 years and it is reasonable to expect that a user's taste may change over time, resulting in a slow convergence of the actual vs. calculated tendencies of the individual. However, any analysis that includes timestamps with the MovieLens dataset should be done with caution. The timestamps show that reviews may have been recovered into the MovieLens database at some point, as evidenced by a large number of reviews in a humanly-impossible short period of time. This indicated that the timestamps for the user reviews may be unreliable for in-depth analysis with regards to timing. With the above in consideration, additional analysis was done looking only at only the most recent reviews for each group, which produced similar results to Fig. 2 above.

The number of attributes possible in a product can vary widely. Genre was selected as the comparison attribute because it was the least sparse; and handling large sparse datasets without some mechanism of reducing the dimensionality of the data is a limitation of current rating systems, which could have caused an unfair advantage in performance comparisons. However, we also performed a sensitivity analysis to determine if ExUp perfoms well with different sparse multi-valued attributes (see Table 7). The test was done by selecting some of the more challenging attributes that have large numbers of unique values: (1) director with 2321 possible values, and (2) keywords with 5292 possible values. For keywords, the instantiated artifact in Visual Studio was programmed to use the PorterStemmerAlgorithm class for populating the matrix, which allows for the meaningful grouping of similar words (e.g., lovers, love, and loving is reduced to the stemmed term “lov”). This reduced the keyword attribute from 17,009 unique terms to 5292 stemmed terms.

The results in Table 7 show that ExUp is robust in its performance with various sparse attributes of a product. Using our method with keywords produced greater results than that of the genre attribute (Numerically achieved 5.25% greater precision, 30.62% greater recall, and 22.12% greater F-measure; and achieved in Like/Dislike a 7.92% greater precision, 17.10% greater recall, and 13.13% greater F-measure). Using our method with the director attribute also produced better results that than of genre (Numerically achieved 16.59% greater precision, and 53.35% greater recall, 40.94% greater F-measure; and achieved in Like/ Dislike a 17.15% greater precision, 33.87% greater recall, and 26.46% greater F-measure). The results found for the director and keyword attributes all significantly exceeded the performance of Genre (alpha of 0.05), which was used for comparison in this study.

![](/api/attachments/ZV7B8G47/fulltext/images/bb759220a856d76023a5d8001cb26bcf532e5b7495ee9ed0c03d704cc1794d20.jpg)  
Fig. 2. ExUp performance based on user's system use.  
Please cite this article as: A. Castillo, et al., ExUP recommendations: Inferring user's product metadata preferences from single-criterion rating systems, Decision Support Systems (2018), https://doi.org/10.1016/j.dss.2018.02.006

Table 7  
Results when comparing ExUp performance for attributes with varying numbers of unique values, asterisk indicates significant difference difference (α = 0.05, two-tailed).

<table><tr><td colspan="2"></td><td>Genre (24 unique)</td><td>Director (2321 unique)</td><td>Keywords (5292 unique)</td></tr><tr><td rowspan="5">Numerical</td><td>Precision (P)</td><td>0.523</td><td>0.627*</td><td>0.552*</td></tr><tr><td>P z-score</td><td>Used for comparison</td><td>-21.100</td><td>-5.833</td></tr><tr><td>Recall (R)</td><td>0.265</td><td>0.568*</td><td>0.382*</td></tr><tr><td>R z-score</td><td>Used for comparison</td><td>-61.643</td><td>-25.083</td></tr><tr><td>F-Measure</td><td>0.352</td><td>0.596*</td><td>0.452*</td></tr><tr><td rowspan="5">Like/dislike</td><td>Precision (P)</td><td>0.570</td><td>0.688*</td><td>0.619*</td></tr><tr><td>P z-score</td><td>Used for comparison</td><td>-24.498</td><td>-10.009</td></tr><tr><td>Recall (R)</td><td>0.451</td><td>0.682*</td><td>0.544*</td></tr><tr><td>R z-score</td><td>Used for comparison</td><td>-46.750</td><td>-18.655</td></tr><tr><td>F-Measure</td><td>0.503</td><td>0.684*</td><td>0.579*</td></tr></table>

The most drastic difference in performance was with the director attribute. It is possible that any product may have product-specific attributes that correlate highly with perceived quality, and be the best choice for generating predictions. In this case, the outcome of any movie production is arguably based on the director's artistic choices in how to present/tell a story, which is somewhat consistent (similar to the brand of a product). There is more preferential variance in a broad category, such as genre (due to the various good and inferior members), than there is in a more granular context, such as movies that are about love (or the stemmed term “lov”). However, the relative performance of a specific director (when compared among his/her peers) would be the most likely to have the least preferential variance for a user out of the three groups. Data sparsity alone for a given dataset may not tell the entire story. Although these results indicate an opportunity for future work in dimensionality reduction and feature selection considerations, it is clear that our method provides good results given attribute sets of various sizes.

## 5. Discussion, conclusions, and future work

The findings of this work showed promising results in comparison to Cacheda et al.'s work, and collaborative filtering. We provided a method that takes into account the more commonly found multi-valued attributes of products. This method helps to alleviate some of the issues with trying to algorithmically generate recommendations and calculate predictions based on non-parametric and multi-valued data. It also provides a means for eliciting specific preferences of an individual on attributes of a product from the common single-value rating system. Although the results did show improvement over the existing algorithms, one of the recall differences was not statistically significant. The ability of ExUP in suggesting products that are liked with accuracy (precision) is significantly greater than all others. However, the ability of ExUP in capturing all liked products (recall) did not significantly outperform the others. In other words, when ExUP provides a recommendation it is more accurate, however it is not necessarily better at providing all possible recommendations when compared to other algorithms when using a single feature space (e.g., genre). It is probable that ExUP is sensitive to detecting the users that value this feature space as important to achieve its high precision, but also that not all users use the tested feature space (genre) as a primary means for evaluating a product. Taking a look at other attributes that may be a better proxy of a product's quality (such as the director for movies) may provide a better overall prediction, as our results show when comparing differently sized attribute sets. This should be determined empirically for any given domain. At worst, ExUP provides accurate recommendations that may closely match the performance of existing implementations, however at a significant performance increase with relatively easy updatability.

There are some limitations to this work. Our method did not solve some of the timeless limitations of recommender system such as sparsity, the cold-start problem, and sensitivity to fake reviews. However, it does show promising results for variously sized sparse datasets —this may be a function of the type of data that was selected as examples—and should be investigated in future work. Although there is some relief for data sparsity by generating tendencies for various features of products in single-dimension rating systems, there still needs to be the presence of ratings that would not exist with entirely new products or users. For products that have existing user ratings, a new user can be provided recommendations solely based on the category the user indicates interest in and the relative performance of the products within that categorization. Also, means are highly sensitive to outliers and skewness. Most rating systems have bounded scores (e.g., 1–5), virtually eliminating the possibility for outliers; however, it is possible that the scores are heavily skewed. There may be an overabundance of inferior or superior products that cause unintended shifts in the means used in calculation, producing artificially inflated or deflated preferential scores in specific categories. Environments with large variance data may want to consider implementing a mechanism of top-k retrieval to minimize this effect [46].

There are many opportunities for future work. First, our results also showed that there is a slight degradation in performance as users mature in a given system. Further analysis was not possible in the present dataset, but future work should take into account how these tendencies change over time (historicity). For example, as users interact with a system over a long period of time the system may suffer from generating recommendations using all the user's data that occurred during multiple stages of life for an individual (childhood, adulthood, family life), and mechanisms that incorporate when users change their preferences still need to be explored.

Attempts were made to explore differences due to group membership without success, possibly due to the unreliability of the timestamps in the dataset. Interestingly, there is some supporting evidence for behavioral differences between group membership, or at least other types of differences that are not captured in the MovieLens/IMDB data.

ExUP relies on the availability of at least some data on the product or the user to create preferential scores, however there may be situations where there is a cold-start problem with both the user and the product, and the creative use of auxiliary data as a viable proxy may help alleviate these situations. For example, item-item similarity analysis, such as that provided by the Google similarity value [47], may find appropriate proxies for estimating missing values for new items from globally available data. Also, it is possible that some attribute-specific user preferences generated by ExUP are product independent and would show inter-domain consistency. Additional datasets should be used and experiments conducted to further explore the opportunities afforded by ExUP in various contexts.

## References

[1] N. McAlone, The Exec who Replaced Netflix's 5-Star Rating System with ‘Thumbs Up Thumbs Down'Business Insider 2017

[2]. G. Adomavicius Y. Kwon, New recommendation techniques for multicriteria rating systems, IEEE Intelligent Systems 22 (2007) 48–55.

[3] M. Galesic, M. Bosnjak, Effects of questionnaire length on participation and indicators of response quality in a web survey, Public Opinion Quarterly 73 (2009) 349–360.

[4] Y. Lee, K.A. Kozar, Understanding of website usability: specifying and measuring constructs and their relationships, Decision Support Systems 52 (2012) 450–463.

[5] V. Formoso, F. Cacheda, V. Carneiro, Algorithms for efficient collaborative filtering, Efficiency Issues in Information Retrieval Workshop, 2008.

[6] F. Cacheda, V. Carneiro, D. Fernández, V. Formoso, Comparison of collaborative filtering algorithms: limitations of current techniques and proposals for scalable, highperformance recommender systems, ACM Transactions on the Web 5 (2011).

[7] Z. Huang, W. Chung, H. Chen, A graph model for E-commerce recommender systems, Journal of the Association for Information Science and Technology 55 (2004) 259–274.

[8] J. Lu, D.S. Wu, M.S. Mao, W. Wang, G.Q. Zhang, Recommender system application developments: a survey, Decision Support Systems 74 (2015) 12–32.

[9] R. Burke, Hybrid Web Recommender Systems, the Adaptive Web, Springer, Berlin, Heidelberg, 2007 377 408

[10] G. Adomavicius, Y. Kwon, Improving aggregate recommendation diversity using ranking-based techniques, IEEE Transactions on Knowledge and Data Engineering 24 (2012) 896–911.

[11] R. Burke, M. Ramezani, Matching Recommendation Technologies and Domains, Recommender Systems Handbook, Springer, Berlin, Heidelberg, 2011 367–386.

[12] F. Ricci, L. Rokach, B. Shapira, Recommender Systems: Introduction and Challenges, Springer, Berlin/Heidelberg, 2015.

[13] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions, IEEE Transactions on Knowledge and Data Engineering 17 (2005) 734–749.

[14] X. Su, T.M. Khoshgoftaar, A survey of collaborative filtering techniques, Advances in Artificial Intelligence 2009 (2009) 4.

[15] N. Archak, A. Ghose, P.G. Ipeirotis, Deriving the pricing power of product features by mining consumer reviews, Management Science 57 (2011) 1485–1509.

[16] S. Gong, Learning user interest model for content-based filtering in personalized recommendation system, JDCTA: International Journal of Digital Content Technology and its Applications 6 (2012) 155–162.

[17] G. Adomavicius, A. Tuzhilin, Context-aware recommender systems, Recommender Systems Handbook, Springer, Boston, MA, USA 2011, pp. 217–253.

[18] R. Mishra, P. Kumar, B. Bhasker, A web recommendation system considering sequential information, Decision Support Systems 75 (2015) 1–10.

[19] J. Bobadilla, F. Ortega, A. Hernando, J. Bernal, Generalization of recommender systems: collaborative filtering extended to groups of users and restricted to groups of items, Expert Systems with Applications 39 (2012) 172–186.

[20] S.K. Lee, Y.H. Cho, S.H. Kim, Collaborative filtering with ordinal scale-based implicit ratings for mobile music recommendations, Information Sciences 180 (2010) 2142–2155.

[21] G. Adomavicius, R. Sankaranarayanan, S. Sen, A. Tuzhilin, Incorporating contextual information in recommender systems using a multidimensional approach, ACM Transactions on Information Systems 23 (2005) 103–145.

[22] C.Q. Jiang, R. Duan, H.K. Jain, S.X. Liu, K. Liang, Hybrid collaborative filtering for highinvolvement products: a solution to opinion sparsity and dynamics, Decision Support Systems 79 (2015) 195–208.

[23] G. Adomavicius, Y. Kwon, Multi-criteria recommender systems, Recommender Systems Handbook, Springer. Berlin. Heidelberg 2015, pp. 847–880.

[24] N. Manouselis, C. Costopoulou, Analysis and classification of multi-criteria recommender systems, World Wide Web 10 (2007) 415–441.

[25] A. Ansari, S. Essegaier, R. Kohli, Internet recommendation systems, Journal of Marketing Research 37 (2000) 363–375.

[26] L. Si, R. Jin, Flexible mixture model for collaborative filtering, Proceedings of the 20th International Conference on Machine Learning (ICML-03) 2003, pp. 704–711.

[27] C. Chow, C. Liu, Approximating discrete probability distributions with dependence trees, IEEE Transactions on Information Theory 14 (1968) 462–467.

[28] N. Sahoo, R. Krishnan, G. Duncan, J. Callan, Research note—the halo effect in multicomponent ratings and its implications for recommender systems: the case of yahoo! Movies, Information Systems Research 23 (2012) 231–246.

[29] M. Nilashi, O.B. Ibrahim, N. Ithnin, Hybrid recommendation approaches for multicriteria collaborative filtering, Expert Systems with Applications 41 (2014) 3879–3900.

[30] D.H. Park, H.K. Kim, I.Y. Choi, J.K. Kim, A literature review and classification of recommender systems research, Expert Systems with Applications 39 (2012) 10059–10072.

[31] J.L. Herlocker, J.A. Konstan, A. Borchers, J. Riedl, An algorithmic framework for performing collaborative filtering, Proceedings of the 22nd Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM 1999, pp. 230–237.

[32] R. Jin, L. Si, C. Zhai, Preference-Based Graphic Models for Collaborative Filtering, Morgan Kaufmann Publishers Inc., Proceedings of the Nineteenth conference on Uncertainty in Artificial Intelligence, 2002 329–336.

[33] J. Ellenberg, The Netflix Challenge, 16, Wired-San Francisco, 2008 114.

[34] R. Agrawal, R. Srikant, Mining sequential patterns, Data Engineering, 1995. Proceedings of the Eleventh International Conference on, IEEE 1995, pp. 3–14

[35] R. Agrawal, J.C. Shafer, Parallel mining of association rules, IEEE Transactions on Knowledge and Data Engineering 8 (1996) 962–969.

[36] X.Y. Yang, Z. Liu, Y. Fu, MapReduce as a programming model for association rules algorithm on Hadoop, International Conference on Information Sciences and Interaction Sciences (ICIS), IEEE 2010, pp. 99–102.

[37] F. Herrera, C.J. Carmona, P. González, M.J. Del Jesus, An overview on subgroup discovery: foundations and applications, Knowledge and Information Systems 29 (2011) 495–525.

[38] T. Tassa, Secure mining of association rules in horizontally distributed databases, IEEE Transactions on Knowledge and Data Engineering 26 (2014) 970–983.

[39] M. Scholz, V. Dorner, M. Franz, O. Hinz, Measuring consumers' willingness to pay with utility-based recommendation systems, Decision Support Systems 72 (2015) 60–71.

[40] F. Liu, H.J. Lee, Use of social network information to enhance collaborative filtering performance, Expert Systems with Applications 37 (2010) 4772–4778.

[41] M.Á. García-Cumbreras, A. Montejo-Ráez, M.C. Díaz-Galiano, Pessimists and optimists: improving collaborative filtering through sentiment analysis, Expert Systems with Applications 40 (2013) 6758–6765.

[42] G. Linden, B. Smith, J. York, Amazon.com recommendation - item-to-item collaborative filtering, IEEE Internet Computing 7 (2003) 76–80.

[43] D.W. Aha, D. Kibler, M.K. Albert, Instance-based learning algorithms, Machine Learning 6 (1991) 37–66.

[44] A. Umyarov, A. Tuzhilin, Using external aggregate ratings for improving individual recommendations, ACM Transactions on the Web 5 (2011) 3.

[45] S.K. Kachigan, Statistical Analysis: an Interdisciplinary Introduction to Univariate & Multivariate Methods. Radius Press, New York 1986.

[46] A. Ayanso, P.B. Goes, K. Mehta, Range query estimation with data skewness for top-k retrieval Decision Support Systems 57 (2014) 258–273

[47] T.C.-K. Huang, Y.-L. Chen, M.-C. Chen, A novel recommendation model with Google similarity, Decision Support Systems 89 (2016) 17–27.

Alfred Castillo is an Assistant Professor at California Polytechnic State University, San Luis Obispo. He received his PhD in Business (Information Systems) from Florida International University. His research interests include data analytics, design science, and user resistance. He holds a Master of Science in Management Information Systems from Florida International University, and a Bachelor of Science in Computer Science from Park University. Prior to his doctoral studies, he worked for several years in industry in various Information Technology roles for public entities, including the United States Marine Corps.

Debra Vander Meer is an Associate Professor in the Department of Information Systems and Business Analytics in the College of Business at Florida International University. Her research interests involve applying concepts from computer science and information systems to real-world problems. Her work is widely published in these fields. She holds a PhD from the Georgia Institute of Technology.

Arturo Castellanos received his PhD degree in Business (Information Systems) from Florida International University. He is an Assistant Professor in the Department of Information Systems and Statistics at the Zicklin School of Business, Baruch College (CUNY). His research interests are in the areas of System Analysis and Design, Healthcare IS, and Business Analytics.
