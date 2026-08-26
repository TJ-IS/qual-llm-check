---
otero_id: 13046
otero_key: "AN26UCKF"
title: "<b>Research Note</b>—The Halo Effect in Multicomponent Ratings and Its Implications for Recommender Systems: The Case of Yahoo! Movies"
authors: "Nachiketa Sahoo; Ramayya Krishnan; George Duncan; Jamie Callan"
year: "2012"
journal: "Information Systems Research"
doi: "10.1287/isre.1100.0336"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## 6SR

![](/api/attachments/AN26UCKF/fulltext/images/06db2636e9cdde8a216a8dc43b79893bdfa8329adf0e6cf75d0071e61f189ad6.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Research Note—The Halo Effect in Multicomponent Ratings and Its Implications for Recommender Systems: The Case of Yahoo! Movies

Nachiketa Sahoo, Ramayya Krishnan, George Duncan, Jamie Callan,

To cite this article:

Nachiketa Sahoo, Ramayya Krishnan, George Duncan, Jamie Callan, (2012) Research Note—The Halo Effect in Multicomponent Ratings and Its Implications for Recommender Systems: The Case of Yahoo! Movies. Information Systems Research 23(1):231-246. http://dx.doi.org/10.1287/isre.1100.0336

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2012, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/AN26UCKF/fulltext/images/4f9116890f47bc233e2f8cf9afe54199816e1dd76a6fcd3ec3a381a4f2b8ec62.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

Research Note

# The Halo Effect in Multicomponent Ratings and Its Implications for Recommender Systems: The Case of Yahoo! Movies

Nachiketa Sahoo

Tepper School of Business, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213, nsahoo@cmu.edu

Ramayya Krishnan, George Duncan

Heinz College, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213 {rk2x@cmu.edu, gd17@andrew.cmu.edu}

Jamie Callan

Carnegie Mellon University, Pittsburgh, Pennsylvania 15213, callan@cs.cmu.edu

ollaborative filtering algorithms learn from the ratings of a group of users on a set of items to find personal-Cized recommendations for each user. Traditionally they have been designed to work with one-dimensional ratings. With interest growing in recommendations based on multiple aspects of items, we present an algorithm for using multicomponent rating data. The presented mixture model-based algorithm uses the component rating dependency structure discovered by a structure learning algorithm. The structure is supported by the psychometric literature on the halo effect. This algorithm is compared with a set of model-based and instancebased algorithms for single-component ratings and their variations for multicomponent ratings. We evaluate the algorithms using data from Yahoo! Movies. Use of multiple components leads to significant improvements in recommendations. However, we find that the choice of algorithm depends on the sparsity of the training data. It also depends on whether the task of the algorithm is to accurately predict ratings or to retrieve relevant items. In our experiments a model-based multicomponent rating algorithm is able to better retrieve items when training data are sparse. However, if the training data are not sparse, or if we are trying to predict the rating values accurately, then the instance-based multicomponent rating collaborative filtering algorithms perform better. Beyond generating recommendations we show that the proposed model can fill in missing rating components. Theories in psychometric literature and the empirical evidence suggest that rating specific aspects of a subject is difficult. Hence, filling in the missing component values leads to the possibility of a rater support system to facilitate gathering of multicomponent ratings.

Key words: collaborative filtering; multicomponent rating; halo effect; Bayesian network; mixture model; expectation maximization; recommender system

History: Paul Goes, Senior Editor; Balaji Padmanabhan, Associate Editor. This paper was received on July 16, 2008, and was with the authors 10.75 months for 2 revisions. Published online in Articles in Advance April 8, 2011.

## 1. Introduction

Recommender systems are increasingly used in online communities, e.g., shopping sites, subscription service sites, and online meeting places (see Table 1). The recommendations are generated from the collection of user preferences, yet they are personalized to each user. Recommender systems are especially useful when the user has too many choices to explore—they assist the users in discovering items that will appeal to them.

From the retailer’s perspective, recommender systems may be used to target advertise items to its customers. A merchant at an online marketplace can use a recommender system to induce demand for less-known items in the system. By using its proprietary recommender system, Netflix is able to effectively merchandise its collection of more than 100,000 movies. It is able to create demand for older, and often less-known, movies by advertising them to users who might like those movies. Given the constraint on the number of movies a subscriber can rent at a time, increase in demand for older movies reduces the demand for the newer releases, which are more expensive to stock. As reported in the annual Securities and Exchange Commission filing of the company in 2006, the success of the Netflix business model depends, to a certain extent, on effective use of and user satisfaction in relation to their recommender system (Netflix 2006).

Table 1 Examples of Collaborative Filtering-Based Recommender Systems

<table><tr><td>Item type recommended</td><td>Commercial</td><td>Noncommercial</td></tr><tr><td>Music</td><td>iTunes, Last.fm,Yahoo! Music</td><td>iRATEradio.com,mystrands.com</td></tr><tr><td>Movies</td><td>Netflix.com,blockbuster.com</td><td>movielens.umn.edu,filmaffinity.com</td></tr><tr><td>Websites</td><td></td><td>StumbleUpon.com</td></tr><tr><td>Aggregated</td><td>Amazon.com,half.ebay.com</td><td></td></tr></table>

Online storefronts are not the only places where recommender systems can be used. There are communities of users with common interests who use recommender systems to find new items that they might enjoy. Some examples of such communities are Last.fm and Pandora.com (Internet radio stations with music recommender systems) and StumbleUpon.com (a Web page recommender system). The development of such services suggests that recommender systems are important tools for mining collective user preferences to help users better navigate large choice spaces.

A key input to recommender systems is the ratings that users give to the items in the system. The ratings provide information about the quality of the item as well as about the taste of the user who gave the rating. Most recommender systems have been designed for single-valued ratings, i.e., for each pair (user, item) we have one rating indicating how much the user liked the item. However, sometimes there are multiple components to a rating. For instance, the popular Zagat survey (Zagat.com) rates restaurants on four criteria: food, decor, services, and cost. Similarly, a movie could be rated for its plot, acting, visual effects, and direction. When such ratings are available from users, it is plausible that a recommender system could be designed that makes use of these component ratings and produces better recommendations for the users.

## 1.1. Contributions of This Paper

In this paper we build on a successful collaborative filtering algorithm for single component ratings to design an algorithm that makes use of multicomponent ratings. We do this by discovering a dependency structure among multicomponent rating data using the Chow-Liu structure discovery algorithm. The discovered structure is validated by the literature on the halo effect. We embed this dependency structure in a flexible mixture model (FMM) (Si and Jin 2003). FMM has been shown to work better than the traditional mixture models for collaborative filtering. We evaluate a set of model-based and instance-based onecomponent rating collaborative filtering algorithms and their extensions for the multicomponent rating data set. The algorithms were tested using multicomponent rating data collected from Yahoo! Movies. The test results show a significant improvement from the use of multiple component ratings. We identify which multicomponent rating algorithm performs better in which scenario and provide some insight into the behaviors of model-based and instance-based algorithms for collaborative filtering. We also show that the proposed model can be used to fill in the missing rating components for incomplete records. This allows us to generate better recommendations for more users when there are incomplete ratings in the data. This also raises the possibility of a rater support system for helping users rate specific aspects of an item.

It is important to distinguish the current work from collaborative filtering in the presence of multidimensional context information, such as finding a recommendation for a movie to watch on a Sunday in the evening with children. Studies exist in the literature to incorporate multidimensional context information into the recommendation generation process. Adomavicius et al. (2005) suggest a reduction-based approach where a context-specific recommendation is generated by using only the ratings collected in the context of interest. In the current work we address a different research question: How can we use the information in various components of a rating to make better recommendations for the users?

## 1.2. Background

Given a user’s ratings on a subset of items and his peers’ ratings on possibly different subsets of items, collaborative filtering algorithms predict which of the items the user would like among the items that he or she has not yet rated. Collaborative filtering algorithms recommend to each user items that are popular among the group of users who are similar to him. This can be thought of as automating the spread of information through word of mouth (Shardanand and Maes 1995). Because collaborative filtering algorithms do not use the content information of the items, they are not limited to recommending only the items with content that the user has rated before (see Adomavicius and Tuzhilin 2005 for a review of the literature in collaborative filtering).

The first group of collaborative filtering algorithms were primarily instance-based on the work of Resnick et al. (1994). In the training step of the algorithm a database of user ratings is built and is used to find similar users and/or items for generating recommendations. These algorithms became popular because they are simple, intuitive, and are sufficient for many small data sets. However, they do not scale to large data sets without further approximations. Also, because they do not learn any user model from the available preferences, they are of limited use as data mining tools (Hofmann 2004).

A second group of collaborative filtering algorithms, known as model-based algorithms, surfaced later (Breese et al. 1998, Chien and George 1999, Getoor and Sahami 1999). They compile the available user preferences into compact statistical models from which the recommendations are generated. Notable model-based collaborative filtering approaches include singular value decomposition to identify latent structure in ratings (Billsus and Pazzani 1998); probabilistic clustering and Bayesian networks (Breese et al. 1998, Chien and George 1999); repeated clustering (Ungar and Foster 1998); dependency networks (Heckerman et al. 2001); latent class models (Hofmann and Puzicha 1999) and latent semantic models (Hofmann 2004) to cluster the ratings; and flexible mixture models to separately cluster users and items (Si and Jin 2003). Unlike the instancebased approach, the model-based algorithms are slow to train; once trained, however, they can generate recommendations quickly.

The model-based algorithms are often described with the help of probabilistic graphical models. Probabilistic graphic models provide a framework based on probability theory and graph theory to approximate complex distributions (Pearl 2000). They graphically express conditional independencies among variables. The variables are represented as nodes, and dependence among them is expressed as edges in a graph. The assumption they encode about the distribution is that each node is independent of the nondescendent nodes conditional on its parent nodes. This allows one to use the chain rule of probability to factor the joint distribution over all the variables into the product of small conditional distributions. These smaller distributions can be individually estimated. This simplifies the operation on the joint distribution during training and inference (Koller and Friedman 2009).

Product recommendation systems have been explored in marketing science as well. Often the goal is to predict the purchase outcome when a customer is targeted. Recently Moon and Russell developed an autologistic recommendation model-based on tools from the spatial statistics literature (Moon and Russell 2008). This model uses the consumers’ purchase history to estimate the probability of a future purchase.

Most of the algorithms in the literature are designed to use unidimensional ratings. In a recent work, Adomavicius and Kwon present approaches for multicriteria rating collaborative filtering (Adomavicius and Kwon 2007). Their work is instance-based in identifying similar users but model-based in aggregating component ratings into one overall rating. Lee and Teng use skyline queries to generate multicriteriabased recommendations from individual component rating predictions, where each component rating is predicted using traditional collaborative filtering algorithms (Lee and Teng 2007).

The multicomponent rating collaborative filtering has some apparent similarity with the conjoint analysis in marketing science (Green and Srinivasan 1978). In conjoint analysis the objective is to estimate a consumer’s preference function in terms of the weight the consumer assigns to the attributes of a product. However, collaborative filtering is effective for goods for which attributes can not be readily determined. For instance, directorial style of a movie is hard to express using an attribute-value system. It is worth noting that a high rating for directorial style of a particular movie does not mean the user puts more weight on the directorial quality. Rather, it means that the user perceives a better match of the directorial style, which is not part of the data, with her preference. In this regard, content-based filtering strategies have more similarity with the conjoint analysis than do the collaborative filtering strategies.

The current work is built on the FMM for collaborative filtering (Si and Jin 2003). FMM models the user and item distribution separately by using two latent variables (Figure 1). It has been shown to work better than other latent class models for collaborative filtering. We extend it for multicomponent ratings, taking into account specific properties of these types of data.

Multicomponent rating data exhibit high correlation among the rating components. This is known as the halo effect (Thorndike 1920, Wells 1907). The halo occurs in part because of the failure of the raters to evaluate each component independent of the others (Cooper 1981, Shweder 1975). In some cases this could be a result of the design of the questionnaire that collects multicomponent ratings. If the definitions of the components are ambiguous or not sufficiently different from each other, the collected ratings are likely to be correlated (Kevin and Reynolds 1988). Although there is some debate about whether halo is entirely bad (Cooper 1981, Fisicaro 1988), it is generally considered undesirable because correlated components provide less information than independent ones. At the rating time the halo can be reduced by increasing the familiarity between the rater and the subject (Heneman 1974, Koltuv 1962, Landy and Farr 1980), reducing the time between the observation and the rating (Borgatta et al. 1958, Shweder and D’Andrade 1980), clever questionnaire designs that make the rater aware of the differences among the components (Rizzo and Frank 1977), and sensitizing the raters by training them to observe and avoid the halo effect (Borman 1979, Latham et al. 1980, Ivancevich 1979).

Figure 1 Flexible Mixture Model of Si and Jin (2003)  
![](/api/attachments/AN26UCKF/fulltext/images/0c2ce47248b8aafdfffbb4030e5cc2325b8ecacd9669d297ba2053c64160b175.jpg)  
Note. Latent variable nodes are shaded; observed variable nodes are not shaded. Source: Si and Jin (2003).

Some halo effect is almost always present despite precautions. Holzbach suggests using a global component in the rating to collect each rater’s overall impression of the subject and statistically remove its effect from each component rating (Holzbach 1978). Similar approaches are taken by Landy et al. (Landy et al. 1980) and by Myers (1965) to arrive at more accurate component ratings. Some elements of our approach described in §2.4 are similar to the approach proposed by Holzbach. To the best of our knowledge, the halo effect has not been studied in the context of recommender systems despite recent advances in multicomponent rating collaborative filtering algorithms.

## 2. Multicomponent Rating Recommender System

By rating multiple aspects of an item, users provide more information about their preferences. The variation in different users’ component ratings while they seemingly agree on their overall impression of the item can be informative. For instance, consider two users $u _ { 1 }$ and $u _ { 2 }$ who have given the same overall ratings to the movie $m _ { 1 }$ (Table 2). But, they differ in how they rate the components of the movie. User $u _ { 1 }$ likes the plot of the movie, whereas user $u _ { 2 }$ likes the direction of the movie. Without the component ratings we would have concluded that users would not particularly like any movie similar to $m _ { 1 }$ . But the component ratings tell us more. They suggest that user $u _ { 1 }$ might like other movies that have a story similar to $m _ { 1 } ,$ and user $u _ { 2 }$ might like a movie that has been directed by the same director or a director with a similar style. Therefore, if we can effectively use the information in the component ratings, we should be able to find more relevant items for the users.

Table 2 An Example of Multicomponent Rating

<table><tr><td>User</td><td>Movie</td><td>Story</td><td>Acting</td><td>Visuals</td><td>Direction</td><td>Overall</td></tr><tr><td> $u_{1}$ </td><td> $m_{1}$ </td><td>4</td><td>1</td><td>2</td><td>1</td><td>2</td></tr><tr><td> $u_{2}$ </td><td> $m_{1}$ </td><td>2</td><td>1</td><td>1</td><td>4</td><td>2</td></tr></table>

Note. Ratings are on a scale of 0–4.

Our empirical work has been motivated by the availability of extensive multicomponent rating data from the Yahoo! Movies website. Although the general approach taken in this work is applicable for any data with component ratings, for clarity we shall describe the methods of this work with the help of the Yahoo! data set.

## 2.1. Data Description and Preliminary Analysis

The rating data were collected from the Yahoo! Movies website using a custom program written in Java programming language. Each record of the rating data has seven variables: item or movie ID 4I 5, user ID 4U 5, ratings on story 4S5, acting 4A5, visuals 4V 5, direction 4D5, and overall 4O5 quality of the movie. The ratings are on a 13-point scale $( A + , A , A - , B + , B , B - , C \dot { + } , C , C - , D + , D , D - , F )$ . We recoded them to a scale of 0–4:

$$
\begin{array}{r l} & {(\{A +, A, A - \} \longrightarrow 4, \{B +, B, B - \} \longrightarrow 3,} \\ & {\{C +, C, C - \} \longrightarrow 2, \{D +, D, D - \} \longrightarrow 1, \{F \} \longrightarrow 0),} \end{array}
$$

so that there are enough data points in each rating bucket. This is especially important for the conditional probability tables estimated in this paper. The models are estimating the probability of observing certain rating values when a user and an item probabilistically belong to some latent classes. If there are not enough data points for a rating value, the probability estimates will be unreliable. Although there were 691,496 (user, item) pairs in the original data set, the user frequency in the data turns out to be skewed (Figure 2). Ratings from users who have rated very few movies are not useful for collaborative filtering, because we cannot reliably know the preferences of a user from only a few of his ratings. Also, we need enough ratings per individual to both train and test the model. Therefore, we have retained only those records that contain users who have at least 20 ratings. After this filtering there were 45,892 records, 1,058 unique users, and 3,430 unique movies.

Figure 2 log − log Plot of Frequency of Users Who Have Rated a Certain Number of Movies  
![](/api/attachments/AN26UCKF/fulltext/images/3a83660db27b0de12dc6f1c95fdc2b088d73ec9d4b0c3d2101bd8b7ba5c861b6.jpg)

Table 3 Correlation Among Components of Rating

<table><tr><td></td><td>S</td><td>A</td><td>D</td><td>V</td><td>O</td></tr><tr><td>S</td><td>1.00</td><td>0.79</td><td>0.82</td><td>0.74</td><td>0.87</td></tr><tr><td>A</td><td>0.79</td><td>1.00</td><td>0.81</td><td>0.73</td><td>0.83</td></tr><tr><td>D</td><td>0.82</td><td>0.81</td><td>1.00</td><td>0.79</td><td>0.88</td></tr><tr><td>V</td><td>0.74</td><td>0.73</td><td>0.79</td><td>1.00</td><td>0.80</td></tr><tr><td>O</td><td>0.87</td><td>0.83</td><td>0.88</td><td>0.80</td><td>1.00</td></tr></table>

Table 4 Principal Components

<table><tr><td>Component</td><td>One</td><td>Two</td><td>Three</td><td>Four</td><td>Five</td></tr><tr><td>% variance explained</td><td>84.5</td><td>5.7</td><td>4.4</td><td>3.2</td><td>2.2</td></tr></table>

Table 5 Factor Loadings After Quartimax Rotation

<table><tr><td></td><td>Factor 1</td><td>Factor 2</td><td>Uniquenesses</td></tr><tr><td>S</td><td>0.91</td><td>0.23</td><td>0.11</td></tr><tr><td>A</td><td>0.87</td><td>-0.02</td><td>0.21</td></tr><tr><td>V</td><td>0.93</td><td>-0.08</td><td>0.10</td></tr><tr><td>D</td><td>0.84</td><td>-0.12</td><td>0.25</td></tr><tr><td>O</td><td>0.95</td><td>0.03</td><td>0.07</td></tr></table>

Examining the data set for the halo effect, we find that the components are highly correlated (Table 3). One way to detect halo effect is by principal component analysis (PCA) and factor analysis (Morrison 1967). If most of the variance in the components can be explained by one principal component or one factor, then it suggests the presence of the halo effect (Kafry et al. 1979). PCA of the ratings shows that there is one component that explains 84.5% variance (Table 4). Factor analysis of the components produced a factor structure dominated by one factor (Table 5). These indicate that there is halo error in the collected ratings.

## 2.2. Modeling Component Ratings for Collaborative Filtering

The information contained in the multicomponent rating has two parts: the overall component captures the user’s overall impression about the item and the variation among the components after partialling out the effect of the overall component tells us how the user evaluates aspects of the item. Traditionally, only the overall component has been used to carry out collaborative filtering (e.g., in Si and Jin 2003). In this section we show how to use the additional information in components along with the overall component.

We use a mixture model similar to the FMM (Si and Jin 2003) (Figure 1). FMM proposes that the rating an item receives from a user is governed by a small number of latent classes for the users and a small number of latent classes for the items. Given the latent classes, the rating is independent of the particular user and the particular item. We can start by embedding all five rating components in the graphic model in place of the only overall component used in the FMM. However, rating components are highly correlated, as shown in Table 3. An incorrect independence among the component ratings in the model would lead us to believe—incorrectly—that each rating component provides completely new additional information about the user preferences.

Figure 3 Flexible Mixture Model for Component Rating Collaborative Filtering  
![](/api/attachments/AN26UCKF/fulltext/images/440caa10dc2ec3ea87ed78a3aa733a5fe4084a248e0913ad8cefbdb021f5cf5e.jpg)

Therefore, one would do well to find the dependency structure among the five components of the rating (Figure 3). This can be posed as a search problem, where the goal is to find the dependency graph that maximizes the probability of the data. Just as during maximum likelihood estimation, the parameter that maximizes the probability of data is deemed to be closest to the true parameter, in the structure search exercise, the structure that maximizes the probability is deemed the best approximation of the true dependency (Koller and Friedman 2009). To estimate the number of different subgraphs among the five components, note that there are 10 unique pairs, each of which can have an edge between them in either direction or have no edge at all. Discarding structures containing cycles, we have 29,281 candidate structures to search through. This is time consuming. Another problem with a complete model search is that the configurations with multiple parents will lead to large conditional probability tables for which we do not have enough data to estimate the probabilities reliably.

We strike a balance between having completely independent rating variables with no edge between them and accommodating fully connected rating variables that account for all possible dependencies. We restrict ourselves to a category of structures that can capture much of the dependency among the rating variables while being amenable to fast and reliable parameter estimation. Chow and Liu (1968) have shown that if we have only discrete variables and we restrict ourselves to only those structures in which there is at most one parent node for each node, i.e., trees, we can efficiently search through them to find the tree that maximizes the probability of data. When the probability distribution is factored according to a tree dependency structure, the graph that maximizes the log probability of the data is the one that maximizes the sum of pairwise mutual information<sup>1</sup> over each edge in the graph. Hence the tree can be found by a maximum weight spanning tree algorithm (Chow and Liu 1968).

Figure 4 Discovered Structure in the Subratings

<table><tr><td rowspan="2"></td><td colspan="5">Mutual information</td></tr><tr><td>S</td><td>A</td><td>V</td><td>D</td><td>O</td></tr><tr><td>S</td><td>—</td><td>0.61</td><td>0.72</td><td>0.51</td><td>0.88</td></tr><tr><td>A</td><td>0.61</td><td>—</td><td>0.68</td><td>0.47</td><td>0.73</td></tr><tr><td>V</td><td>0.72</td><td>0.68</td><td>—</td><td>0.64</td><td>0.92</td></tr><tr><td>D</td><td>0.51</td><td>0.47</td><td>0.64</td><td>—</td><td>0.66</td></tr><tr><td>O</td><td>0.88</td><td>0.73</td><td>0.92</td><td>0.66</td><td>—</td></tr></table>

Such an exercise over the five component ratings leads to the structure shown in Figure 4. The structure states that the strongest of the dependencies among the components of the ratings is between the Overall rating and the components, as can be verified from the pairwise mutual information table in Figure 4. This shows the strong influence of a user’s Overall impression of a movie on the perception of the other aspects of the movie. In the data we would find evidence of dependence between any pair of variables, but changing the parent for any of the components from O to any other variable (under the tree structure restriction one variable can have at most one parent) would lead to a lower probability of the data. Another way of reading this discovered structure is: given the Overall rating, the components are independent. Note that this dependency structure says that if we do not condition on the Overall rating, then the S1 A1 D, and V variables are dependent or correlated, which is consistent with the expectation we started with.

## 2.3. Parallels

It is interesting to compare the approach taken in the psychometric literature (Holzbach 1978, Myers 1965, Landy et al. 1980) with the discovered Chow-Liu tree dependency structure among the movie rating components.

Following a procedure like Holzbach’s, when we statistically remove the halo effect of the Overall component on the other components through partial correlation (Table 6), the average intercomponent correlation among variables S1 A1 D, and V reduces from 0.78 to 0.26. As all correlations are positive, some reduction in correlation is expected when computing partial correlations. However, the average partial correlation among the variables is the least when we control for the variable O among the possible five variables. The average partial correlations when we control for S1 A1 D, and V are 0.47, 0.53, 0.35, and 0.60, respectively. These observations are in accordance with Holzbach’s proposition that by controlling for Overall rating we can peer beyond the halo effect at the more accurate component ratings.

The dependency structure given in Figure 4 says that if we condition on the Overall rating 4O5, then the components should be independent of each other. Strictly speaking, this assertion of the Chow-Liu tree is correct only if the assumption that the dependency among the rating components can be described by a tree structure is correct. However, a weaker assertion that states that among all possible variables that we might have conditioned on, conditioning on O leads to least residual dependency among the remaining components, is still true. We found that the discovered structure persists over different random subsets of the data, suggesting that it is robust.

This result empirically validates the approach taken by Holzbach (1978), Myers (1965), and Landy et al. (1980) using a much larger data set. It is interesting to note that the Chow-Liu tree structure discovery method, which is agnostic to the meaning of the rating components, arrives at a conclusion based on the empirical distribution of the data that agrees with the what researchers in psychometric literature arrived at based on the general impression theory of the halo

Table 6 Partial Correlations Controlling for Overall Rating

<table><tr><td> $r_{R_i R_j.0}$ </td><td>S</td><td>A</td><td>D</td><td>V</td></tr><tr><td>S</td><td>1.00</td><td>0.25</td><td>0.26</td><td>0.15</td></tr><tr><td>A</td><td>0.25</td><td>1.00</td><td>0.32</td><td>0.22</td></tr><tr><td>D</td><td>0.26</td><td>0.32</td><td>1.00</td><td>0.33</td></tr><tr><td>V</td><td>0.15</td><td>0.22</td><td>0.33</td><td>1.00</td></tr></table>

## Figure 5 Flexible Mixture Model with Component Rating Dependency Structure

![](/api/attachments/AN26UCKF/fulltext/images/894b6ac720fa3d7e493055cc57d1e72cfc68215795127c3aebb8d0e25ca51e3e.jpg)

effect. We believe this agreement adds to the validity of both approaches.

## 2.4. Model Estimation Using the

## Expectation-Maximization (EM) Algorithm

Using the discovered structure between the components of the ratings, we construct the model shown in Figure 5 for collaborative filtering. As we have hidden variables, the parameters need to be estimated using an indirect method. We propose an algorithm based on the EM framework (Dempster et al. 1977). The algorithms based on the EM framework have two alternating steps that monotonically increase probability of the data or the likelihood of the parameters. First is the E (expectation) step, where one computes the distribution of the unobserved variable given all the observed variables. This is the same as doing an inference on the graphical model for the hidden variables. It can be shown that among all distributions over the hidden variables, the posterior distribution given the observed data maximizes the expected log probability. Intuitively, the posterior distribution over the hidden variables given the observation is our best guess about the values of the hidden variables.

Second is the M (maximization) step, where one estimates the parameters of the complete distribution (consists of observed and unobserved variables) using the standard maximum likelihood estimation. This operation maximizes the expected log probability given the posterior distribution of the unobserved variables.

The E and the M steps in our case are: E step

$$
\begin{array}{l} P (Z _ {u}, Z _ {i} \mid \vec {X}), \\ = \frac {P (Z _ {u}) P (Z _ {i}) P (I \mid Z _ {i}) P (U \mid Z _ {u}) \prod_ {j = 1} ^ {5} P (R _ {j} \mid Z _ {u} , Z _ {i} , \mathrm{Pa} _ {R _ {j}})}{\sum_ {Z _ {u}} \sum_ {Z _ {i}} P (Z _ {u}) P (Z _ {i}) P (I \mid Z _ {i}) P (U \mid Z _ {u}) \prod_ {j = 1} ^ {5} P (R _ {j} \mid Z _ {u} , Z _ {i} , \mathrm{Pa} _ {R _ {j}})}, \end{array}\tag{1}
$$

M step

$$
P (Z _ {u}) = \frac {1}{L} \sum_ {l} \sum_ {Z _ {i}} P (Z _ {u}, Z _ {i} | \vec {X} _ {(l)}),\tag{2}
$$

$$
P (Z _ {i}) = \frac {1}{L} \sum_ {l} \sum_ {Z _ {u}} P (Z _ {u}, Z _ {i} | \vec {X} _ {(l)}),\tag{3}
$$

$$
P (U \mid Z _ {u}) = \frac {\sum_ {l : U _ {(l)} = U} \sum_ {Z _ {i}} P (Z _ {u} , Z _ {i} \mid \vec {X} _ {(l)})}{\sum_ {l} \sum_ {Z _ {i}} P (Z _ {u} , Z _ {i} \mid X _ {l})},\tag{4}
$$

$$
P (I \mid Z _ {i}) = \frac {\sum_ {l : I _ {(l)} = I} \sum_ {Z _ {u}} P (Z _ {u} , Z _ {i} \mid \vec {X} _ {(l)})}{\sum_ {l} \sum_ {Z _ {u}} P (Z _ {u} , Z _ {i} \mid \vec {X} _ {(l)})},\tag{5}
$$

$$
\begin{array}{l} P (R _ {j} \mid Z _ {u}, Z _ {i}, \mathrm{Pa} _ {R _ {j}}) \\ = \frac {\sum_ {l : R _ {j (l)} = R _ {j} \& \mathrm{Pa} _ {R j (l)} = \mathrm{Pa} _ {R j}} P (Z _ {u} , Z _ {i} \mid \vec {X} _ {(l)})}{\sum_ {l : \mathrm{Pa} _ {R j (l)} = \mathrm{Pa} _ {R j}} P (Z _ {u} , Z _ {i} \mid \vec {X} _ {(l)})}, \end{array}\tag{6}
$$

where

Z = Latent class variable to cluster the users,

$Z _ { i }$ = Latent class variable to cluster the items,

$$
R _ {j} = j \text {   th   rating   node;   } R _ {j} \in \{S, A, V, D, O \},
$$

Pa = parent rating node of $R _ { j } ,$

L = number of records in the data set,

l = record index,

$\vec { X } _ { ( l ) }$ = record numbered $l ;$ it consists of observations for $U , I , S , A , V , D ,$ and $O ,$

$U _ { ( l ) }$ = variable U in the record numbered $l ,$

$I _ { ( l ) }$ = variable I in the record numbered $l ,$

$R _ { j ( l ) } = { \mathrm { r a t i n g ~ v a r i a b l e ~ } } R _ { j }$ in the record numbered $l ,$

$\mathrm { P a } _ { R _ { j } ( l ) } = { \mathrm { r a t i n g ~ v a r i a b l e ~ P a } } _ { R _ { j } }$ in the record numbered l.

The E step shown above is the conditional distribution computed by dividing joint distribution of all variables, factored using the conditional independencies, by the joint distribution of only the observed variables, obtained by marginalizing out the hidden variables. The M step in the EM algorithm estimates the maximum likelihood estimate of the parameters using both the observed and the unobserved variables. If we could observe all variables, we could find the maximum likelihood estimate of parameters of each conditional probability table by dividing the number of records with matching values for all the variables in the conditional probability table by the total number of records with matching values of the conditioning variables. However, we do not observe the hidden variables. Therefore, we have to use our best guess about their number of occurrences or their expected occurrence counts at a record given the observations of other variables in the same record. This is obtained from the posterior distribution of the hidden variable. Because this conditional distribution is multinomial, the expected number of times a hidden variable takes a certain value in one record is

## Figure 6 Flexible Mixture Model with Independent Component Ratings

![](/api/attachments/AN26UCKF/fulltext/images/eb8fb385127191ad3e7d2b4a6750f5a5ec0ee847fe812562feb20a5a07a56c92.jpg)

same as the probability of the hidden variable taking that value given the value of the observed variables. All equations of the M step can be obtained by tabulating the values of the observed variables and, for the hidden variables, using the expected number of times the hidden variables take a certain value.

We compare this model with discovered dependency structure with the model that assumes independence among the component ratings conditional on the latent classes (Figure 6). The E and the M steps for the case when all components are assumed independent are derived in a similar manner.

E step

$$
\begin{array}{l} P (Z _ {u}, Z _ {i} \mid \vec {X}), \\ = \frac {P (Z _ {u}) P (Z _ {i}) P (I \mid Z _ {i}) P (U \mid Z _ {u}) \prod_ {j = 1} ^ {5} P (R _ {j} \mid Z _ {u} , Z _ {i})}{\sum_ {Z _ {u}} \sum_ {Z _ {i}} P (Z _ {u}) P (Z _ {i}) P (I \mid Z _ {i}) P (U \mid Z _ {u}) \prod_ {j = 1} ^ {5} P (R _ {j} \mid Z _ {u} , Z _ {i})} \end{array}\tag{7}
$$

M step

$$
P (Z _ {u}) = \frac {1}{L} \sum_ {l} \sum_ {Z _ {i}} P (Z _ {u}, Z _ {i} | \vec {X} _ {(l)}),\tag{8}
$$

$$
P (Z _ {i}) = \frac {1}{L} \sum_ {l} \sum_ {Z _ {u}} P (Z _ {u}, Z _ {i} | \vec {X} _ {(l)}),\tag{9}
$$

$$
P (U \mid Z _ {u}) = \frac {\sum_ {l : U _ {(l)} = U} \sum_ {Z _ {i}} P (Z _ {u} , Z _ {i} \mid \vec {X} _ {(l)})}{\sum_ {l} \sum_ {Z _ {i}} P (Z _ {u} , Z _ {i} \mid X _ {l})},\tag{10}
$$

$$
P (I \mid Z _ {i}) = \frac {\sum_ {l : I _ {(l)} = I} \sum_ {Z _ {u}} P (Z _ {u} , Z _ {i} \mid \vec {X} _ {(l)})}{\sum_ {l} \sum_ {Z _ {u}} P (Z _ {u} , Z _ {i} \mid \vec {X} _ {(l)})},\tag{11}
$$

$$
P (R _ {j} \mid Z _ {u}, Z _ {i}) = \frac {\sum_ {l : R _ {j (l)} = R _ {j}} P (Z _ {u} , Z _ {i} \mid \vec {X} _ {(l)})}{\sum_ {l} P (Z _ {u} , Z _ {i} \mid \vec {X} _ {(l)})}.\tag{12}
$$

Note that the key difference between these two sets of expressions is the absence of any parent node in the conditioning part of the conditional probability of the component ratings (Expressions (6) and (12)). The intuitions behind these equation are similar to those described for the previous set.

We also compare these approaches with the baseline case where there is only one rating: the Overall rating on the movie. The E and the M steps can be borrowed from Si and Jin (2003) or derived following the approach used to arrive at Equations (1)–(12). E step

$$
\begin{array}{l} P (Z _ {u}, Z _ {i} \mid U, I, O) \\ = \frac {P (Z _ {u}) P (Z _ {i}) P (I \mid Z _ {i}) P (U \mid Z _ {u}) P (O \mid Z _ {u} , Z _ {i})}{\sum_ {Z _ {u}} \sum_ {Z _ {i}} P (Z _ {u}) P (Z _ {i}) P (I \mid Z _ {i}) P (U \mid Z _ {u}) P (O \mid Z _ {u} , Z _ {i})} \end{array}\tag{13}
$$

M step

$$
P (Z _ {u}) = \frac {1}{L} \sum_ {l} \sum_ {Z _ {i}} P (Z _ {u}, Z _ {i} | U _ {(l)}, I _ {(l)}, O _ {(l)}),\tag{14}
$$

$$
P (Z _ {i}) = \frac {1}{L} \sum_ {l} \sum_ {Z _ {u}} P (Z _ {u}, Z _ {i} | U _ {(l)}, I _ {(l)}, O _ {(l)}),\tag{15}
$$

$$
P (U \mid Z _ {u}) = \frac {\sum_ {l : U _ {(l)} = U} \sum_ {Z _ {i}} P \left(Z _ {u} , Z _ {i} \mid U _ {(l)} , I _ {(l)} , O _ {(l)}\right)}{L \times P \left(Z _ {u}\right)},\tag{16}
$$

$$
P (I \mid Z _ {i}) = \frac {\sum_ {l : I _ {(l)} = I} \sum_ {Z _ {u}} P (Z _ {u} , Z _ {i} \mid U _ {(l)} , I _ {(l)} , O _ {(l)})}{L \times P (Z _ {i})},\tag{17}
$$

$$
P (O \mid Z _ {u}, Z _ {i}) = \frac {\sum_ {l : O _ {(l)} = O} \sum_ {Z _ {u}} P (Z _ {u} , Z _ {i} \mid U _ {(l)} , I _ {(l)} , O _ {(l)})}{\sum_ {l} P (Z _ {u} , Z _ {i} \mid U _ {(l)} , I _ {(l)} , O _ {(l)})}.\tag{18}
$$

In each of these approaches the number of the classes (levels of $Z _ { u }$ and $\mathsf { \bar { Z } } _ { i } )$ is a user-specified parameter. The greater the number of classes, the better the fit of the model will be with to the training data, resulting in larger probability of data, but that will increase the risk of overfitting the model to the training data. Another factor to keep in mind is that increasing the number of classes by n times leads to $n ^ { 2 }$ times more multiplications in the E step and n times more additions in the M step. In our experiments the time taken to complete with higher levels of classes has been the bottleneck. We have experimented with $4 , 8 ,$ $^ { 1 6 , }$ and 32 classes. The times taken to complete the experiments were approximately 2.5 hours, 17 hours, 92 hours, and 670 hours, respectively, on a 3.0-GHz pentium processor computer. This leads to some interesting findings. The model with only an Overall rating performs best, with 4 hidden classes. The more complex model with 5 independent components performs best at 8 hidden classes and almost as well with 16. The model with 5 dependent components performs best with 16 hidden classes. The reported results contain the best results for each model.

All models performed poorly when we used 32 classes because of too many parameters to estimate. It causes at least two problems:

1. Small number of data points for each parameter leads to unreliable estimations;

2. Overfitting of the model to the training data.

A method that adaptively determines the number of classes given the size of the data set at hand would be most appropriate in a real-life setting. However, we leave that for a future study.

2.4.1. Smoothing of Parameter Estimates Using BDe Prior (Koller and Friedman 2009). To guard against over-fitting to the training data we smooth the parameter estimates in the M step using a Dirichlet prior, which is the multivariate generalization of the beta distribution and conjugate prior for the multinomial distribution. A parameter $( \theta _ { 1 } , \dots , \theta _ { K } )$ following Dirichlet distribution with the hyperparameters $( \alpha _ { 1 } , \ldots , \alpha _ { K } )$ has the probability distribution

$$
P (\theta_ {1}, \ldots , \theta_ {K}) \sim \prod_ {k} \theta_ {k} ^ {\alpha_ {k} - 1}.
$$

The expected value of $\theta _ { k } = \alpha _ { k } / ( \sum _ { k = 1 } ^ { k = K } \alpha _ { k } )$ . If we update this prior using multinomial data with counts $M _ { 1 } , \dots , M _ { K } ,$ , then we obtain the posterior that is another Dirichlet distribution with hyper parameters $( \alpha _ { 1 } + M _ { 1 } , \ldots , \alpha _ { K } + M _ { K } )$ . Thus the expected values of the components can be obtained by adding the counts to the numerator and denominator of the original formula:

$$
E (\theta_ {k}) = \frac {M _ {k} + \alpha_ {k}}{(\sum_ {k} M _ {k}) + (\sum_ {k} \alpha_ {k})}.\tag{19}
$$

Therefore, the s can be thought of as pseudocounts and the sum of $\alpha ^ { \prime } \mathrm { s }$ is a measure of the weight of the prior. Note that for each combination of values of the parent nodes there is a different set of parameters and priors. If the same Dirichlet prior were used for each conditional distribution, the nodes with more parent configurations would have larger weights of the priors. BDe prior is a Dirichlet prior constructed so that the weight of the prior would be the same for each node, irrespective of how many parent configurations, and thus conditional probability tables, there are for each of them (Nir Friedman 1998). We use a BDe prior to smooth the parameter estimates during the model training phase.

## 2.5. Predicting the Overall Rating

The goal is to predict the rating a user would give to an item he has not yet rated. Hence, the partial observation consists of the user and the item from which we are trying to predict the Overall rating.

The joint distribution over all variables (observed and latent) is the product of the conditional probability table estimated in §2.4, from which we need to marginalize away those variables that we are not interested in. In this section we focus on our ability to predict the overall rating. Therefore, we need to marginalize all variables except U 1 I1 and O. For the three models discussed in the previous section, the distribution over the variables ${ \hat { U } } , I ,$ and O is

$$
\begin{array}{l} P (U, I, O) = \sum_ {Z _ {u}} P (Z _ {u}) P (U \mid Z _ {u}) \\ \qquad \cdot \sum_ {Z _ {i}} P (O \mid Z _ {u}, Z _ {i}) P (Z _ {i}) P (I \mid Z _ {i}). \end{array}\tag{20}
$$

Although the expression for all three models is the same, the parameters estimated are different because of different conditional independence assumptions.

For user $u _ { a }$ and item i we are interested in the conditional distribution of the overall rating, namely,

$$
P (O \mid u _ {a}, i) = \frac {P (u _ {a} , i , O)}{\sum_ {O} P (u _ {a} , i , O)}.\tag{21}
$$

The mode of this distribution of O is predicted as the output.<sup>2</sup>

## 2.6. Instance-Based Approaches

We compare the performance of these proposed algorithms with several of the existing one-component and multicomponent instance-based methods. As a baseline we use the framework proposed by Breese et al. (1998):

$$
\hat {R} _ {t j} = \bar {R} _ {t} + \frac {1}{\sum_ {i} ^ {N _ {u}} a b s (s i m (t , i))} \sum_ {i} ^ {N _ {u}} s i m (t, i) (R _ {i j} - \bar {R} _ {i}),\tag{22}
$$

where the expected rating a user t would give to item j is computed by ratings of other users weighted by similarity of those users to the target user t. One of several metrics can be used to compute the similarity between two users who are represented by the vectors of ratings they have given. Some choices are cosine, correlation, inverse Eucledian distance, etc. We use the correlation coefficient to obtain baseline results, because it has often been used in the literature.

Adomavicius and Kwon (2007) have generalized the similarity measure in Equation (22) to the case of ratings with multiple components. Their predicted rating can be summarized as

$$
s i m (t, i) = \frac {1}{1 + d i s t _ {u} (t , i)},\tag{23}
$$

$$
d i s t _ {u} (t, i) = \frac {1}{| U _ {t} \cap U _ {i} |} \sum_ {l \in U _ {t} \cap U _ {i}} d i s t _ {r} (R _ {t l}, R _ {i l}),\tag{24}
$$

where $U _ { i }$ is the set of ratings given by the user i.

Several distance metrics are explored for dist between two multicomponent ratings, such as

1. Manhattan distance

$$
\sum_ {k} | R _ {i} (k) - R _ {j} (k) |;
$$

2. Euclidean distance

$$
\sqrt {\sum_ {k} (R _ {i} (k) - R _ {j} (k)) ^ {2}};
$$

3. Chebyshev distance

$$
\max _ {k} | R _ {i} (k) - R _ {j} (k) |.
$$

They found that the Chebyshev distance–based approach performs best among the distance-based approaches considered. The distance metrics proposed in Adomavicius and Kwon (2007) for multicomponent rating collaborative filtering do not take into account the correlation between rating components. One multidimensional distance measure that takes into account correlation between dimensions is Mahalanobis distance (Mahalanobis 1936). Mahalanobis distance between two random vectors xE and yE that are assumed to be drawn from one common distribution is

$$
d i s t _ {m a h a} (\vec {x}, \vec {y}) = \sqrt {(\vec {x} - \vec {y}) ^ {T} S ^ {- 1} (\vec {x} - \vec {y})},\tag{25}
$$

where S is the covariance of the distribution. In one set of experiments we use Mahalanobis distance. This is done using Equation (25) in Equations (23) and (24). We compute the covariance matrix from the ratings used in the training data.

Because of the correlation among the component ratings, it is worth considering whether it would suffice to isolate the principal rating component through a principal component analysis and use that in a single component rating collaborative filtering algorithm. We obtain the principal component of the multicomponent rating through a PCA rotation and compute the correlation between pairs of users based on their thus identified principal component ratings on movies. After computing the similarity between the users, we use original ratings in Equation (22) to compute the predicted value of a user’s rating on a movie.

The set of collaborative filtering methods compared is summarized in Table 7.

## 3. Results and Discussion

3.1. Experiments with Random Training Samples To compare the effectiveness of the three models we use a fraction of the user ratings to train our models (training set) and the remaining ratings to test the prediction (test set). A certain fraction of each user’s records was randomly selected to include in the training data to make sure that there were some training data for each user in the test set. For each user-item pair in the test data we predict their overall rating 4O5 using each model. We calculate the mean absolute error (MAE) of the predictions with the help of the known ratings. We also evaluate the algorithms’ ability to retrieve the highest rated items. These two results need not be correlated (Herlocker et al. 2004). Appropriateness of each depends on the application environment.

Table 7 Set of Algorithms Compared

<table><tr><td></td><td>Model-based</td><td>Instance-based</td></tr><tr><td>Multicomponent</td><td>1. 5 Dependent subratings2. 5 Independent subratings</td><td>3. Chebyshev4. Mahalanobis5. PCA</td></tr><tr><td>One component</td><td>6. Flexible mixture model</td><td>7. User-user correlation</td></tr></table>

For an application where the recommended items are presented to the user along with a score for each item, it is important to predict the numerical values of the ratings accurately. One example of such an application environment can be found in the movie recommender system of Netflix. The rating prediction accuracy can be measured using the MAE of the predictions:

$$
\mathrm{MAE} = \frac {1}{L _ {\mathrm{test}}} \sum_ {l = 1} ^ {L _ {\mathrm{test}}} | o _ {l} - \hat {o} _ {l} |,
$$

where $L _ { \mathrm { t e s t } } =$ the number of records in the test data; $o _ { l } =$ the true rating; and $\hat { o } _ { l } =$ the predicted rating.

However, in many other applications the user is only presented with the top few items that he is likely to rate highly. The numerical values of the items are deemed of no interest. One example of such an application environment can be found at Amazon.com. Here, if the recommender system can identify the top few items for the user with little noise, then it is considered to have fulfilled the requirement. It does not matter if all the predicted ratings are biased up or down, as long as the predicted ratings order the items in the same way the user would, i.e., a relatively higher rating for items that the user would rate A followed by lower ratings to items that the user would rate B, and so on. This correctness of ordering of items for users can be evaluated using precision-recall plots, precision at top five, or mean reciprocal rank (MRR).

To describe them briefly, assume for a moment that the user would be only interested in the items rated A. Consider the top-N item predictions. Precision is the fraction of the N items that the user would have rated A. Recall is the fraction of items that the user would have rated A that are in the top N . With increasing N , more A-rated items are fetched, improving recall. But, at the same time, more of those items that are rated less than A are also retrieved, damaging the precision score. A good recommender system should be able to retrieve many of the A-rated items while maintaining high precision. Hence, a plot of precision at 11 standard recall levels 40%1 10%1 20%1 0 0 0 1 100%5 is commonly used to compare the performance of different systems (Baeza-Yates and Ribeiro-Neto 1999).

Often in retrieval and recommendation tasks the quality of only the top few recommendations is of interest, because users typically do not look beyond the first few items. We measure the quality of top items recommended using two metrics:

1. Mean precision of the top five items recommended;

2. MRR of the first relevant item recommended (Voorhees 2000):

$$
\mathrm{MRR} = \frac {1}{\# u s e r s} \sum_ {i} ^ {\# u s e r s} \frac {1}{r a n k _ {f i r s t r e l e v a n t}}.
$$

MRR measures how soon a person gets a relevant recommendation from the algorithm.

3.1.1. Accuracy in Rating Prediction. The average MAE scores using 30 different random train/test partitions are shown in Figure 7. As expected, the overall error for each model decreases with increasing amounts of training data. However, we see that in this set of results using Chebyshev and Mahalanobis distance metrics in an instance-based multicomponent framework best predicts the rating values. Using the principal component after a PCA rotation of the five component ratings does not do any better or worse than simply using the overall rating in a correlation-based single-component rating algorithm.

However, one of the advantages of model-based approaches is that after training the models, the rating prediction step is quick. Therefore, these approaches are more suitable for online recommendation generations. If one is interested in using a model-based recommender system, we have the following insights. Naively extending the existing FMM for collaborative filtering with component ratings without considering the existing correlation among the component ratings does not lead to any improvement in the prediction of overall ratings over using only one component rating. As discussed in §2.2, components of the ratings are correlated and assuming independence among them given latent class leads to overcounting of evidence. When we capture the dependence among the rating components through the Overall rating and explicitly model for it, the prediction accuracy improves. Error plots of the two model-based algorithms, one using only the overall rating and the other using five components with dependency, show that there is an advantage of using multicomponent ratings when the training set is small—up to about 30% of the available data set for training in this case. But when there are enough training data, using only the Overall rating leads to more accurate prediction of Overall rating. This suggests that when we have a user’s Overall rating over a large number of items, adding component ratings does not lead to any further improvement in the ability to predict the Overall rating the user might place on a new item.

Figure 7 Plot of Errors by Amount of Training Data Used, for Different Models  
![](/api/attachments/AN26UCKF/fulltext/images/f2985543072044f2d22a4e20c61c4ef6061a155e424ee9b6777cc6943cfaaf54.jpg)

To verify that the differences in the average MAE seen in Figure 7 are significant and not a result of chance, we performed a pairwise t-test using MAE obtained at the 30 different train/test splits. We found that the differences are indeed significant except where the error lines in Figure 7 cross.

3.1.2. Accuracy in Retrieving Top N Items. The seven algorithms were trained as described in §2.4 at different training set sizes. Then the ratings for each user-item pair in the test set were computed using the prediction function of each method. This creates an ordering over the test item set for each user. A recommender system would recommend items from this list in decreasing order of predicted rating. The goal of the precision-recall curve is to find out how the precision of the recommendation is affected as more items are included from this list in the pursuit of retrieving all the relevant items. In this set of experiments we treat movies with a rating of 4 in the test set as relevant. The precision versus recall curve is given in Figure 8. A separate experiment that treats movies with a rating of 3 or higher in the test set as relevant returns similar results, albeit with a higher precision value at each recall level because of the presence of more relevant items.

When the training fraction is low the model with discovered structure gives the highest precision at each recall level. However, when we have more training data, the instance-based multicomponent rating algorithms using Chebyshev or Mahalanobis distance do better. The instance-based approaches using only the overall component or the principal component have the worst precision. The model with independence assumption among the component ratings returns the lowest precision among the modelbased approaches.

Figure 8 Typical Precision-Recall Curves with Sparse Training Data  
![](/api/attachments/AN26UCKF/fulltext/images/ffa21376fa4ceacce0770c4b80616b77e00737b82c52495c5c6f6c8c462ffe87.jpg)

![](/api/attachments/AN26UCKF/fulltext/images/940d7c52acc688f38bb74fed24ad638bf2af4cdffdede5232f54fb418d70837f.jpg)

We also compute the mean precision after top-five retrievals and MRRs of each algorithm at these training fractions. The results shown in Figure 10 agree with the general observation made in the precisionrecall curves in Figure 8. Among the model-based approaches, the model with dependency structure performs best. However, as we use more training data, instance-based multicomponent rating approaches that use Chebyshev or Mahalanobis distances outperform the model-based approaches (Figure 9).

One possible reason for better performance of modelbased approaches over instance-based approaches when the training fractions are low is that the latter are based on pairwise similarity computations. When the training data are sparse, the pairwise comparisons of users are unreliable. However, the model-based approaches suffer less from these problems because each user is effectively compared with a model of a group of users that is less sparse. Thus the users are classified into the correct class more accurately. However, when there are more training data, the pairwise user-to-user comparisons can be done more reliably. This leads to improved performance of the instancebased multicomponent approaches.

Figure 9 Typical Precision-Recall Curves with Less Sparse Training Data  
![](/api/attachments/AN26UCKF/fulltext/images/a3d2b0fba7368ea8947e21e629180360ad0489f653c398c329125719ffd6bdd8.jpg)

![](/api/attachments/AN26UCKF/fulltext/images/474b3dcec74b8648a636e4fae6f86469cc1ac81ed022253a41ba9245b71e6946.jpg)  
Note. Instance-based algorithms using Chebyshev distance and Mahalanobis distance do best when we use 80% of the data for training.

Figure 10 Mean Precision at Top Five and Mean Reciprocal Rank  
![](/api/attachments/AN26UCKF/fulltext/images/8e5c4b8a720fde2345ee4ed995f118e9576f4ea8771036cec63ec92bdc427ed3.jpg)

Hence, the takeaway from these tests is that we can improve the rating prediction accuracy by using a multicomponent rating, although the right algorithm to use depends on the sparsity of the training data. It also depends on whether the recommender system is being used to predict the ratings accurately or to retrieve the most relevant items quickly.

## 3.2. Filling in Missing Component Ratings

Raters find it easier to form an overall impression about their subject than to objectively evaluate specific aspects of it (Feeley 2002). This leads to two kinds of problems in collecting multicomponent rating data:

1. Halo effect. If they choose to rate the components without deliberating enough to evaluate them objectively, rating values get biased by their overall impression of the subject. This, known as the halo error, is treated in §§1.2, 2.1, and 2.3.

Figure 11 Records with Partial Information  
![](/api/attachments/AN26UCKF/fulltext/images/0e848c302d8659fed36f6968540f46cd427a010db1b35105a8bb1452d402e47f.jpg)

2. Missing values. If the raters choose to skip rating the components, we have a missing data problem for rating components. In our data set, 34% of the records (235,659 of 691,495) had incomplete rating information and thus needed to be discarded for the experiments described in the previous sections. Of those 235,695 incomplete records 225,515 (95%) have only the Overall rating (Figure 11). This indicates the difficulty in obtaining component ratings from the users.

There are two opportunities for contribution here:

1. If we can predict the harder aspect ratings for a user for an item taking the user’s Overall rating into account, then we can design a rating support system. One use case is: the user gives his Overall rating on the item and the system prefills the component ratings. Then the user confirms them or modifies them if he feels they are different from how he would rate.

2. If we can fill in the missing values in the data set, we can generate recommendations for more users. Because we need a minimum number of ratings per user in the data set, discarding incomplete records eliminates many users, and consequently many of their records even with complete ratings. Table 8 shows the difference between sizes of the data set when we discard the incomplete records and when we fill in the missing values using the method described in this section.

Table 8 Increase in Data Set Size After Filling in Missing Components

<table><tr><td></td><td>With unfilled components</td><td>Filled-in components</td><td>Percentage of increase</td></tr><tr><td>Number of users</td><td>1,058</td><td>1,680</td><td>59</td></tr><tr><td>Number of items</td><td>3,430</td><td>3,926</td><td>14</td></tr><tr><td>Number of records</td><td>45,892</td><td>74,110</td><td>61</td></tr></table>

We showed in §2 that the probability distribution over all the variables can be factored as

$$
\begin{array}{c} P (U, \vec {R}, I) = \sum_ {Z _ {u}, Z _ {i}} P (Z _ {u}) P (Z _ {i}) P (I \mid Z _ {i}) P (U \mid Z _ {u}) \\ \cdot \prod_ {j = 1} ^ {5} P (R _ {j} \mid Z _ {u}, Z _ {i}, \mathrm{Pa} _ {R _ {j}}). \end{array}\tag{26}
$$

Because we always have Overall ratings in our data, we focus on predicting missing component ratings. To make an inference about one of the component ratings such as S using the values of U , I, and O variables, we need to carry out two operations on distribution given in Equation (26):

1. Marginalize away the variables we do not need, i.e., $R _ { i } \in \bar { A } , D , V$

2. Plug in the values of the variable we have. Let’s denote them as $u , i ,$ and o.

The operations result in the following:

$$
\begin{array}{l} \mathcal {P} (u, I, S, O) \\ = \sum_ {Z _ {u}} P (Z _ {u}) \sum_ {Z _ {i}} P (Z _ {i}) P (O | Z _ {u}, Z _ {i}) P (I | Z _ {i}) \\ \quad \cdot P (U | Z _ {u}) P (S | Z _ {u}, Z _ {i}, O), \\ \Rightarrow P (u, i, S, o) = \sum_ {Z _ {u}} P (Z _ {u}) \sum_ {Z _ {i}} P (Z _ {i}) P (o | Z _ {u}, Z _ {i}) \\ \quad \cdot P (i | Z _ {i}) P (u | Z _ {u}) P (S | Z _ {u}, Z _ {i}, o), \\ \propto P (S | u, i, o). \end{array}
$$

The result is a function of S that is proportional to its posterior distribution given the variable values $u , i ,$ and o. The mode of this distribution is output as the predicted value of S.

3.2.1. Experiments and Results. First we use only the complete records in this experiment to predict the missing components and verify the predictions. The component ratings are hidden in the test data. Only the ${ \bar { U } } , I ,$ and O variable values were used from the test data to predict the hidden component ratings. We predicted each of the component ratings (S1 A1 V 1 D) for every record in the test set and computed the MAE. Tenfold<sup>3</sup> cross validation was used to generate the training and testing samples (Mitchell 1997). We compared our results with the performance of the missing value analysis (MVA) routines of SPSS. The Error values are given in Table 9.

MAEs in predicted missing values are close to 0036 on a scale of length 4. When we predict the component ratings using only the U and I values, as is done with traditional collaborative filtering, the MAE values are between 006 and 007. This suggests that our method is able to extract considerable benefit from the additional available information in the Overall rating. The regression approach to predict missing values, part of the SPSS MVA module, was not very successful at an error of about 0.6. However, the EM algorithm used in the SPSS MVA module produced results almost as good as ours. The algorithm takes an iterative approach that alternates between the following two steps until convergence. Starting with random initialization of the missing values,

Table 9 Comparison of Different Methods Filling in Missing Rating Components

<table><tr><td>Method</td><td>MAE</td></tr><tr><td>Multicomponent FMM</td><td>0.353</td></tr><tr><td>SPSS EM</td><td>0.368</td></tr><tr><td>SPSS regression</td><td>0.569</td></tr><tr><td>CF predicting components</td><td>0.701</td></tr></table>

1. Regress each variable in turn against all other remaining variables and estimate the coefficients

2. Predict missing variable values of the incomplete records using a linear regression model with the help of the coefficients estimated so far and the other variables in the record.

Examining the error distribution of our method, we found that the errors are well behaved, with very few predictions off by a large margin (Figure 12). In about 70% of the cases we were accurate in our prediction of the missing value and in about 96% of the cases the prediction was within one rating of the true value.

## 4. Conclusions

We started this study with the following question:

Can the recommendations by collaborative filtering algorithms be improved by using multiple component ratings?

Figure 12 Error Distributions While Filling in Missing Rating Components  
![](/api/attachments/AN26UCKF/fulltext/images/10c48b5739f81f1314f4ac6475b1508ba0931d63b82a2fafbd2c1c16358ba788.jpg)

To answer this question we collected multicomponent movie rating data from Yahoo! Movies. Because component ratings are correlated due to halo effect, a structure discovery exercise was carried out to find the dependency tree that captures most of the dependencies among the components. The discovered structure is interesting in itself. It says that the component ratings provided by the users are more correlated to the Overall ratings than they are to other component ratings. This suggests the possible relation between the Overall impression of the user and the ratings given to the components. In this context we draw a connection to the work on the halo effect in the psychometric literature. The body of work on halo effect indicates that component ratings are influenced by the presence of other strong factors and by the Overall impression.

We develop a mixture model-based collaborative filtering algorithm incorporating the discovered dependency structure. In addition, several one-component algorithms and their variations for multicomponent ratings were evaluated on the collected data set. The multicomponent rating algorithms lead to better performance than the one-component rating algorithms in both predicting the rating values accurately and in retrieving the most relevant movies quickly. The model-based algorithm using dependency structure leads to better retrieval performance when the training data are sparse. However, when more training data are available, using instancebased multicomponent rating approaches that use Chebyshev or Mahalanobis distance to measure distance between two ratings perform better. In addition, these two instance-based multicomponent rating algorithms are able to predict the ratings more accurately than other algorithms that we tested.

One of the advantages of the model-based approaches is that after the model is calibrated, it can be used to quickly generate recommendations. This makes them suitable for scenarios like shopping websites where real-time recommendation generation is important. When the training data are sparse—a common problem faced in real-world scenarios—there is an advantage of using multicomponent ratings in a model that accounts for the halo effect. However, if we have more training data, one component rating flexible mixture model is able to better predict the ratings than other model-based approaches.

The proposed multicomponent model can be used to predict values of the missing component ratings. This is useful because in the current data set approximately one-third of the records have one or more of the component ratings missing. We show that the missing values can be filled in reliably. This allows us to generate recommendations for 59% more users and to recommend 14% more items.

Multicomponent rating collaborative filtering algorithms can suffer because of poor data. One can argue that objectively rating aspects of an item requires deliberation that can only be expected from professional critiques. This can cause the halo effect and reduce the information in the components. In this work we provide an approach to use the limited but important information in the components to make better recommendations. However, with increased emphasis on user-generated content and on valuable services using them, we expect the quality of such data to improve. The proposed algorithm will be even more valuable in such a scenario.

Our work suggests several future research directions. One of foremost importance is the evaluation of the proposed method in other multicomponent rating data sets. Also, in the presence of adequate numbers of ratings, a more complete dependency graph among the ratings might be discovered and used, as it will better capture the dependency among the rating components. We have shown that the proposed model can be used to fill in the missing rating components. Such an approach can be used to design a rater support system that predicts a user’s component ratings using his overall rating. But such a system might bias the rater. The implementation and evaluation of such a rater support system is an interesting topic to explore.

## References

Adomavicius, G., Y. O. Kwon. 2007. New recommendation techniques for multicriteria rating systems. IEEE Intelligent Systems 22(3) 48–55.

Adomavicius, G., A. Tuzhilin. 2005. Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions. IEEE Trans. Knowledge Data Engrg. 17(6) 734–749.

Adomavicius, G., R. Sankaranarayanan, S. Sen, A. Tuzhilin. 2005. Incorporating contextual information in recommender systems using a multidimensional approach. ACM Trans. Information Systems 23(1) 103–145.

Baeza-Yates, R. A., B. A. Ribeiro-Neto. 1999. Modern Information Retrieval. ACM Press, Addison-Wesley, New York.

Billsus, D., M. J. Pazzani. 1998. Learning Collaborative Information Filters. Morgan Kaufmann Publishers, San Francisco.

Borgatta, E. F., J. H. Mann, L. S. Cottrell. 1958. The spectrum of individual interaction characteristics: An interdimensional analysis. Psych. Rep. 4 279–319.

Borman, W. C. 1979. Format and training effects on rating accuracy. J. Appl. Psych. 64(4) 410–421.

Breese, J. S., D. Heckerman, C. Kadie. 1998. Empirical analysis of predictive algorithms for collaborative filtering. Technical report, Microsoft Research, Redmond, WA.

Chien, Y. H., E. I. George. 1999. A Bayesian model for collaborative filtering. Proc. 7th Internat. Workshop on Artificial Intelligence Statist., FT Lauderdale, FL. http://uncertainty99 .microsoft.com/proceedings.com.

Chow, C. K., C. N. Liu. 1968. Approximating discrete probability distributions with dependence trees. IEEE Trans. Information Theory 14(3) 462–467.

Cooper, W. H. 1981. Ubiquitous halo. Psych. Bull. 90(2) 218–244.

Dempster, A. P., N. M. Laird, D. B. Rubin. 1977. Maximum likelihood from incomplete data via the EM algorithm. J. Roy. Statist. Soc. 39(1) 1–38.

Feeley, T. H. 2002. Comment on halo effects in rating and evaluation research. Human Comm. Res. 28(4) 578–586.

Fisicaro, S. A. 1988. A reexamination of the relation between halo error and accuracy. J. Appl. Psych. 73(2) 239–244.

Getoor, L., M. Sahami. 1999. Using probabilistic relational models for collaborative filtering. Workshop on Web Usage Analysis User Profiling (WEBKDD’99), San Diego.

Green, P. E., V. Srinivasan. 1978. Conjoint analysis in consumer research: Issues and outlook. J. Consumer Res. 5(2) 103–123.

Heckerman, D., D. M. Chickering, C. Meek, R. Rounthwaite, C. Kadie. 2001. Dependency networks for inference, collaborative filtering, and data visualization. J. Machine Learn. Res. 1 49–75.

Heneman, H. G. 1974. Comparision of self and superior ratings of managerial performance. J. Appl. Psych. 59(5) 638–642.

Herlocker, J. L., J. A. Konstan, L. G. Terveen, J. T. Riedl. 2004. Evaluating collaborative filtering recommender systems. ACM Trans. Inform. Systems 22(1) 5–53.

Hofmann, T. 2004. Latent semantic models for collaborative filtering. ACM Trans. Inform. Systems (TOIS) 22(1) 89–115.

Hofmann, T., J. Puzicha. 1999. Latent class models for collaborative filtering. D. Thomas, ed. Proc. 16th Internat. Joint Conf. Artificial Intelligence (IJCAI-99-Vol2), Morgan Kaufmann Publishers, San Francisco, 688–693.

Holzbach, R. L. 1978. Rater bias in performance ratings: Superior, self, and peer ratings. J. Appl. Psych. 63(5) 579–588.

Ivancevich, J. M. 1979. Longtudinal study of the effects of rater training on psychometric error in ratings. J. Appl. Psych. 64(5) 502–508.

Kafry, D., S. Zedeck, R. Jacobs. 1979. Discriminability in multidimensional performance evaluations. Appl. Psych. Measurement 3(2) 187–192.

Kevin, R. M., D. H. Reynolds. 1988. Does true halo affect observed halo? J. Appl. Psych. 73(2) 235–238.

Koller, D., N. Friedman. 2009. Structured Probabilistic Models: Principles and Techniques. MIT Press, Cambridge, MA.

Koltuv, B. B. 1962. Some characteristics of intrajudge trait intercorrelations. Psych. Monograph 76 1–24.

Landy, F. J., J. L. Farr. 1980. Performance rating. Psych. Bull. 87(1) 72–107.

Landy, F. J., R. J. Vance, J. L. Barnes-Farrell, J. W. Steele. 1980. Statistical control of halo error in performance ratings. J. Appl. Psych. 65(5) 501–506.

Latham, G. P., E. D. Pursell, K. N. Wexley. 1980. Training managers to minimize rating errors in observation of behavior. J. Appl. Psych. 60(5) 550–555.

Lee, H. H., W. G. Teng. 2007. Incorporating multi-criteria ratings in recommendation systems. IEEE Internat. Conf. Inform. Reuse and Integration, Las Vegas, NV, 273–278.

MacKay, D. J. C. 2003. Information Theory, Inference, and Learning Algorithms. Cambridge University Press, New York.

Mahalanobis, P. C. 1936. On the generalised distance in statistics. Proc. Natl. Inst. Sci. 2(1) 49–55.

Mitchell, T. 1997. Machine Learning. McGraw-Hill Book Company, New York.

Moon, S., G. J. Russell. 2008. Predicting product purchase from inferred customer similarity: An autologistic model approach. Management Sci. 54(1) 71–82.

Morrison, D. F. 1967. Multivariate Statistical Methods. McGraw-Hill Book Company, New York.

Myers, J. H. 1965. Removing halo from job evaluation factor structure. J. Appl. Psych. 49(3) 217–221.

Netflix, Inc. 2006. Form 10-K annual report pursuant to Section 13 or 15(d) of the Securities Exchange Act of 1934. United States Securities and Exchange Commission, Washington, DC.

Friedman, N., M. Goldszmidt. 1998. Learning in Graphical Models, Chapter 15. Kluwer Academic Publishers, Dordrecht, The Netherlands, 431–432.

Pearl, J. 2000. Causality: Models, Reasoning, and Inference. Cambridge University Press, New York.

Resnick, P., N. Iacovou, M. Suchak, P. Bergstrom, J. Riedl. 1994. GroupLens: An open architecture for collaborative filtering of netnews. Proc. Conf. Comput.-Supported Cooperative Work, CSCW’94, Chapel Hill, NC, 175–186.

Rizzo, W. A., F. D. Frank. 1977. Influence of irrelevant cues and alternate forms of graphic rating scales on the halo effect. Personnel Psych. 30(3) 405–417.

Shardanand, U., P. Maes. 1995. Social information filtering: Algorithms for automating “word of mouth.” In CHI: Proc. SIGCHI Conf. Human Factors Computing Systems, ACM Press/Addison-Wesley Publishing, New York, 210–217.

Shweder, R. A. 1975. How relevant is an individual difference in personality? J. Personality 43(3) 455–484.

Shweder, R. A., R. G. D’Andrade. 1980. The systematic distortion hypothesis. R. A. Schweder, D. W. Fiske, eds. New Directions for Methodology of Behavioral Science: Fallible Judgment Behavioral Res. Jossey Bass, San Franciso, 37–58.

Si, L., R. Jin. 2003. Flexible mixture model for collaborative filtering. Proc. Twentieth Internat. Conf. Machine Learning (ICML), AAAI Press, San Francisco, 704–711.

Thorndike, E. L. 1920. A constant error in psychological ratings. J. Appl. Psych. 4(1) 25–29.

Ungar, L. H., D. P. Foster. 1998. Clustering methods for collaborative filtering. Proc. Workshop Recommendation Systems, AAAI, Menlo Park, CA, 112–125.

Voorhees, E. M. 2000. The TREC-8 question answering track report. Proc. Eighth Text Retrieval Conf., Gaithersburg, MD. http://trec.nist.gov/pubs/trec8/t8\_proceedings.html, 77–82.

Wells, F. L. 1907. A Statistical Study of Literary Merit. R. S. Woodworth, ed. Science Press, New York.
