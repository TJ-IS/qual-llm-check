---
otero_id: 13838
otero_key: "VZA8S3QK"
title: "Recommendations Using Information from Multiple Association Rules: A Probabilistic Approach"
authors: "Abhijeet Ghoshal; Syam Menon; Sumit Sarkar"
year: "2015"
journal: "Information Systems Research"
doi: "10.1287/isre.2015.0583"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [141.161.91.14] On: 25 August 2015, At: 07:36 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## HSR

![](/api/attachments/VZA8S3QK/fulltext/images/cf2871c071849fd95b7e59672ec69937a9906b629f0c5169dd42c03131453270.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Recommendations Using Information from Multiple Association Rules: A Probabilistic Approach

Abhijeet Ghoshal, Syam Menon, Sumit Sarkar

To cite this article:

Abhijeet Ghoshal, Syam Menon, Sumit Sarkar (2015) Recommendations Using Information from Multiple Association Rules: A Probabilistic Approach. Information Systems Research

Published online in Articles in Advance 31 Jul 2015

http://dx.doi.org/10.1287/isre.2015.0583

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2015, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/VZA8S3QK/fulltext/images/ef6827a187573fbd67b559e6e0fe673b234367ff2cc5bf476f78081969443997.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Recommendations Using Information from Multiple Association Rules: A Probabilistic Approach

Abhijeet Ghoshal College of Business, University of Louisville, Louisville, Kentucky 40292, abhijeet.ghoshal@louisville.edu

Syam Menon, Sumit Sarkar Naveen Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080 {syam@utdallas.edu, sumit@utdallas.edu}

usiness analytics has evolved from being a novelty used by a select few to an accepted facet of conducting Bbusiness. Recommender systems form a critical component of the business analytics toolkit and, by enabling firms to effectively target customers with products and services, are helping alter the e-commerce landscape. A variety of methods exist for providing recommendations, with collaborative filtering, matrix factorization, and association-rule-based methods being the most common. In this paper, we propose a method to improve the quality of recommendations made using association rules. This is accomplished by combining rules when possible and stands apart from existing rule-combination methods in that it is strongly grounded in probability theory. Combining rules requires the identification of the best combination of rules from the many combinations that might exist, and we use a maximum-likelihood framework to compare alternative combinations. Because it is impractical to apply the maximum likelihood framework directly in real time, we show that this problem can equivalently be represented as a set partitioning problem by translating it into an information theoreti context—the best solution corresponds to the set of rules that leads to the highest sum of mutual information associated with the rules. Through a variety of experiments that evaluate the quality of recommendations made using the proposed approach, we show that (i) a greedy heuristic used to solve the maximum likelihood estimation problem is very effective, providing results comparable to those from using the optimal set partitioning solution; (ii) the recommendations made by our approach are more accurate than those made by a variety of state-of-the-art benchmarks, including collaborative filtering and matrix factorization; and (iii) the recommendations can be made in a fraction of a second on a desktop computer, making it practical to use in real-world applications.

Keywords: personalization; Bayesian estimation; maximum likelihood; information theory; data analytics History: Ram Gopal, Senior Editor; Gautam Pant, Associate Editor. This paper was received on April 28, 2013, and was with the authors 9 months for 2 revisions. Published online in Articles in Advance.

## 1. Introduction

A recent International Data Corporation report estimates that the business analytics market will grow at a compounded rate of 9.8%, and reach 50.7 billion by 2016. This is partly fueled by the growth in the amount of customer data readily available to firms and the potential for businesses to leverage their data through the novel use of software-based analytic techniques. Recommender systems form an integral part of the business analytics toolkit, and several studies have shown that personalized recommendations can enable firms to effectively target customers with products and services (Häubl and Trifts 2000, Tam and Ho 2003). For example, Pathak et al. (2010) find that the strength of a recommender system has a positive effect on sales and prices.

Recommendations are made on a continuous basis and can have a substantial impact on the bottom line.

According to Hosanagar et al. (2014), 60% of Netflix rentals stem from recommendations, and 35% of Amazon’s sales originate from their recommendation system. It is easy to see that even a small improvement in the quality of recommendations would be worth millions of dollars every year to a retailer.

A variety of methods exist for providing recommendations, with collaborative filtering, matrix factorization, and association-rule-based methods being the most common.<sup>1</sup> In this paper, we focus on improving the quality of rule-based recommendations by combining information from multiple association rules. Rule-based approaches comprise one prominent class of techniques used to provide personalized recommendations to customers. Firms such as Broad-Vision provide rule-based tools to firms that wish to implement recommendation systems on their websites (Hanson 2000). Rules are easy to understand, which appeals to marketers interested in cross selling or product placement. Often, such rule-based systems use association rules (Hastie et al. 2009).

Association rules are implications of the form 8bread, milk9 → 8yogurt9, where 8bread1 milk9 is called the antecedent of the rule and 8yogurt9 is called its consequent. Although millions of such implications are possible in a typical data set, not all of them are useful for providing recommendations. Agrawal et al. (1993) provided a method to identify those rules where the items in the rules appear in a reasonably large number of transactions (termed the support of the rule) and where a consequent has a high probability of being chosen when the items in the antecedent have already been chosen (termed the confidence of the rule). Every mined rule must meet minimum thresholds for both support and confidence.

Association rules compactly express how products group together (Berry and Linoff 2004), and they have been successfully used for market basket analysis (Gordon 2008, Lewin 2009). Recommendation systems based on association rules leverage available rules and a customer’s basket, to recommend items as the customer is shopping. Many firms implement associationrule-based recommender systems because they can be used unobtrusively in automated systems to provide recommendations to customers in real time. For instance, Forsblom et al. (2009) developed a mobile application for a Nokia smartphone that uses association rules to recommend retail products to customers. Prominent companies like IBM promote association rule mining capabilities in their business analytics software (IBM 2009a, b; 2010). Moreover, because an association-rule-based system compares alternative items to recommend based on their probabilities of purchase, the system can be easily adapted to make recommendations based on expected payoffs associated with the items.<sup>2</sup>

Whereas there has been considerable work done on mining rules more efficiently (e.g., Ng et al. 1998; Bayardo 1998; Bayardo and Agrawal 1999; Zaki 2000; Webb 2000, 2008, 2010; Webb and Zhang 2005; Calders et al. 2013; Zhou et al. 2013), research into the use of rules to make effective recommendations is scarce. Zaïane (2002) proposed a method that finds all eligible rules (rules whose antecedents are subsets of the basket and whose consequents are not) and recommends the consequent of the eligible rule with the highest confidence. Baralis and Garza (2002) and Baralis et al. (2004) proposed related approaches (referred to as L3 and L3G, respectively) for classification based on the selective pruning and elimination of “harmful” rules; these can be adapted for recommending items as well. Wang and Shao (2004) suggested considering only maximal rules, i.e., eligible rules whose antecedents are maximal-matching<sup>3</sup> subsets of the basket. All these approaches focus on identifying a single rule to make the recommendation. Often, however, the antecedent of the selected rule will not contain all of the items in the basket. Consequently, the recommendation is made on the basis of partial information—items not present in the antecedent of the rule being used for recommendation are effectively ignored. It is not difficult to see that the item being recommended could be different if the recommendation system could use information from all of the items in the basket. The set of eligible rules often contains multiple rules with the same consequent, and the quality of recommendations could potentially be improved by combining such rules effectively.

The notion of combining rules has been explored in a few studies in the past. Given a customer’s basket, Lin et al. (2002) calculated the score for each item as the sum of the products of the supports and confidences of all eligible rules with that item as the consequent. The item with the highest score was recommended to the customer. Wickramaratna et al. (2009) presented an approach to identify rules that predict the presence and absence of an item, and proposed a Dempster–Shaffer-based approach for combining rules when some rules predict that a customer will purchase an item, whereas other rules predict the contrary. However, they noted that their approach is not scalable for real-time applications.

There has also been some work attempting to combine classification rules. Li et al. (2001) suggested classifying customers using classification based on multiple association rules (CMAR). They grouped eligible rules with the same consequent (class) and evaluated the sum of weighted -squares of the rules in each group. The customer was assigned to the consequent class corresponding to the group with the highest sum. Liu et al. (2003) classified customers using a score calculated based on the combination of all of the eligible rules (determined based on the attributes of the customer). Their scoring formula requires the identification of rules with negations and cannot be adapted for selecting items to recommend in a traditional association rule mining context. Thabtah (2007) provided a detailed survey on various classification approaches that use single and multiple association rules for classification.

Two other techniques that have been successfully employed in recommendation systems are collaborative filtering and matrix factorization. Collaborativefiltering-based methods are perhaps the best known, at least since Amazon.com decided to deploy collaborative filtering as part of their recommender system (Linden et al. 2003). These methods use the known preferences of a group of users to make recommendations or predictions of the unknown preferences for other users. Matrix factorization methods gained recognition partly as a result of successes in the Netflix Prize competition. These methods represent users and items through factors identified from the data, and an item is recommended to a user when the item and user are similar vis-à-vis these factors (Koren et al. 2009). Su and Khoshgoftaar (2009) provide a detailed survey of several approaches based on collaborative filtering and matrix factorization.

It is evident from the above discussion that there exists a considerable amount of literature on recommendation techniques. However, the literature lacks a principled approach to combine information from multiple rules. This paper makes multiple contributions in this regard.

(i) A common characteristic of the existing works that attempt to combine rules is that all of the methods proposed are ad hoc in nature. By contrast, we propose a method formally grounded in probability theory to combine multiple rules and make recommendations based on as many items in the basket as possible. As with other approaches that use association rules, we assume that the rules have already been mined (using any of the methods that have been proposed for mining rules) and available for use. Given a customer’s basket, we estimate the probability of each item (that can be recommended) being selected by the customer.

(ii) We view the collection of rules being combined as a probability model. When multiple potential rule combinations exist for a particular target item, the best combination of rules (i.e., the best probability model) needs to be identified. We develop a maximum likelihood approach to determine the best model; the problem is framed as one of maximizing the likelihood that the observed data (the training data used to mine the rules) is generated from the competing probability models represented by the feasible rule combinations. The problem of maximizing likelihood requires us to estimate the likelihoods from the training data at the time recommendations are made. However, it is not feasible to do this in real time because many probability parameters need to be estimated for each probability model, and the training data sets will be large in most practical cases. We show that this problem can be transformed into an equivalent problem of maximizing the mutual information (MI) associated with each model, where the mutual information of the model is the sum of the mutual information values associated with the rules included in the model. The mutual information values associated with the mined rules can be precomputed. These values enable the efficient comparison of alternative probability models in real time.

(iii) When the number of items in a customer’s basket increases, the number of feasible rule combinations can grow rapidly. Therefore, the number of probability models to compare could be large for some problem instances. We develop a greedy heuristic that determines good solutions in real time regardless of the size of the basket. Experiments comparing the performance of an optimal approach with that of the heuristic are conducted on three real data sets. The performance of the heuristic is virtually identical to that of the optimal for experiments conducted on one data set, and only marginally worse for experiments conducted on the other two (the differences are not statistically significant).

(iv) The effectiveness of our methodology—termed maximum likelihood recommendation (MLR)—is demonstrated through a variety of additional computational experiments that compare it to many key benchmarks. We compare the accuracy of recommendations made by MLR to those made by (a) the single-rule approaches of Zaïane (2002), Wang and Shao (2004), and Baralis et al. (2004) (called L3G); (b) the rule combination approaches of Li et al. (2001) and Lin et al. (2002); (c) item-based collaborative filtering; and (d) matrix factorization implemented as FunkSVD in the LensKit toolset (lenskit.grouplens.org). MLR is shown to outperform all of the benchmarks, and the performance improvements are observed to be robust at various support and confidence thresholds used for mining rules in all three data sets. When it is feasible to combine multiple rules so that a larger proportion of the basket is covered by the rule antecedents than would be possible otherwise, MLR performs particularly well.

We describe the problem in detail in §2 and discuss the methodology in §3. Section 4 presents results of the experiments conducted to validate our approach for rule-based recommendation environments. Section 5 compares MLR with the collaborative filtering and matrix factorization approaches. Section 6 concludes this paper.

## 2. Problem Description

The problem being considered in this paper is best illustrated through an example. Consider a customer who has three items $i _ { 1 } , i _ { 2 } ,$ and $i _ { 3 }$ in her basket B, i.e., $\mathbf { B } = \{ i _ { 1 } , i _ { 2 } , i _ { 3 } \}$ . The eligible rules for this basket—i.e., all available rules whose antecedents are subsets of the basket—are listed in Table 1. Rules $R _ { 1 } { - } R _ { 4 }$ have item $x _ { 1 }$ as their consequent, whereas item $x _ { 2 }$ is the consequent of rules $R _ { 5 } – R _ { 8 }$ . Our task is to select one of $x _ { 1 }$ or $x _ { 2 }$ and recommend it to the customer.

Table 1 Eligible Rules for Basket $\pmb { 8 } = \{ i _ { 1 } , i _ { 2 } , i _ { 3 } \}$

<table><tr><td>Rule</td><td>Antecedent</td><td>Consequent</td><td>Confidence (%)</td></tr><tr><td> $R_{1}$ </td><td> $i_{1}, i_{2}$ </td><td> $x_{1}$ </td><td>60</td></tr><tr><td> $R_{2}$ </td><td> $i_{2}, i_{3}$ </td><td> $x_{1}$ </td><td>40</td></tr><tr><td> $R_{3}$ </td><td> $i_{1}$ </td><td> $x_{1}$ </td><td>53</td></tr><tr><td> $R_{4}$ </td><td> $i_{3}$ </td><td> $x_{1}$ </td><td>43</td></tr><tr><td> $R_{5}$ </td><td> $i_{1}, i_{3}$ </td><td> $x_{2}$ </td><td>42</td></tr><tr><td> $R_{6}$ </td><td> $i_{2}, i_{3}$ </td><td> $x_{2}$ </td><td>50</td></tr><tr><td> $R_{7}$ </td><td> $i_{1}$ </td><td> $x_{2}$ </td><td>58</td></tr><tr><td> $R_{8}$ </td><td> $i_{2}$ </td><td> $x_{2}$ </td><td>62</td></tr></table>

Traditional rule-based approaches identify the best rule from the eligible set and recommend the associated consequent. ${ \mathrm { S o } } ,$ for example, Zaïane’s (2002) approach would rank the eligible rules based on their confidences and select the consequent of the rule with the highest confidence as the item to recommend. The rule with the highest confidence in our example is $R _ { 8 } ,$ and consequently, $x _ { 2 }$ would be recommended to the customer. However, recommending $x _ { 2 }$ based on $R _ { 8 }$ ignores some items in the basket $( i _ { 1 }$ and $i _ { 3 } ) ,$ , despite the fact that another rule, $R _ { 5 } ,$ exists with these items in the antecedent. This is true in general—making a recommendation based on a single rule often disregards items in the basket that are not in the antecedent of the rule being used.

If we could effectively combine rules and cover as many items of the basket as possible, our recommendation would be more informed. The question then becomes one of determining the best way to combine multiple rules. This is the primary objective of this paper—to provide a theoretical basis for combining rules. Given the items in a customer’s basket, we combine rules when necessary to estimate the probabilities of each relevant consequent being selected by the customer and recommend the item with the highest probability. Note that this is not unlike what the single-rule approach would do if there was a rule whose antecedent covered the entire basket—i.e., combinations of rules can be interpreted in much the same way as any single rule would be.

Before we calculate the probabilities associated with each potential recommendation, however, we need to identify the rules to combine. It is quite possible that there will be multiple potential combinations to choose from. For example, we have already seen that rules $R _ { 5 }$ and $R _ { 8 }$ could be combined to estimate the probability for $x _ { 2 }$ . From Table 1, we can also see that rules $R _ { 6 }$ and $R _ { 7 }$ could be used to estimate the same probability as well. Different combinations of rules can yield different probability estimates, and we show how to choose the best combination from the different alternatives.

## 3. Maximum Likelihood Recommendation

MLR can be viewed as a three-step process. The first step identifies all of the eligible rules and, from them, the feasible consequents. For each of these feasible consequents, the best probability estimate conditioned on the basket is identified in the second step. The third step selects the consequent with the highest probability.

## 3.1. Identifying Eligible Rules and Consequents

We first find all of the eligible rules by ensuring that all items in the antecedent of a selected rule appear in the basket while its consequent does not. The consequents of the eligible rules are added to a consequent list M. In our example, M contains two consequents, $\{ x _ { 1 } , x _ { 2 } \}$

3.2. Computing the Probability of a Consequent Given a customer with a basket B, we are interested in estimating $P ( x \mid \mathbf { B } )$ , the probability that she will choose item x from M. Although we would ideally like to use a rule that has x as the consequent and an antecedent identical to $\mathbf { B } ,$ such a rule may not exist. It is more likely that we will find several rules with x as the consequent, whose antecedents are subsets of B. These rules can be used, with appropriate conditional independence assumptions, to arrive at an estimate for $P ( x \mid \mathbf { B } )$ . Such assumptions have been used extensively for estimation when the available data were not sufficient to estimate the full distributions and have been found to be robust in practice (Domingos and Pazzani $1 9 9 7 ) . ^ { 4 }$ For example, naïve Bayes classifiers are known to perform very well in many applications (Han et al. 2012, p. 350). According to Shmueli et al. (2010, p. 153), techniques using such assumptions often rely on the orderings of the probability estimates, which are usually close to accurate even if many of these assumptions are violated.

Specifically, if we have multiple eligible rules with disjoint antecedents and a common consequent x, we can estimate $P ( x \mid \mathbf { B } )$ by combining the information in these rules under the assumption that the antecedents are conditionally independent given the common consequent x. Note that the antecedents of the rules being combined have to be disjoint to avoid double counting the impact of the common items in the rules.<sup>5</sup>

Suppose there are r eligible rules with disjoint antecedents that have x as the consequent. Let the antecedent of rule $R _ { j }$ be $A _ { j } ,$ and let A represent $\textstyle \bigcup _ { j = 1 } ^ { r } A _ { j }$ By assuming that the antecedents $A _ { j }$ are conditionally independent given x, we can approximate $P ( x | \mathbf { B } )$ as $P ( x | \mathbf { \bar { A } } )$ follows:

$$
\begin{array}{c} P (x | \mathbf {A}) = \frac {P (\mathbf {A} | x) \cdot P (x)}{P (\mathbf {A})} = \frac {P (\mathbf {A} | x) \cdot P (x)}{P (x , \mathbf {A}) + P (\bar {x} , \mathbf {A})} \\ = \frac {(\prod_ {j = 1} ^ {r} P (A _ {j} | x)) \cdot P (x)}{(\prod_ {j = 1} ^ {r} P (A _ {j} | x)) \cdot P (x) + (\prod_ {j = 1} ^ {r} P (A _ {j} | \bar {x})) \cdot P (\bar {x})}. \end{array}\tag{1}
$$

To evaluate $P ( x | \mathbf { A } )$ using (1), we need to know $P ( x )$ and $P ( { \bar { x } } )$ along with $P ( A _ { i } \mid x )$ and $P ( A _ { j } \mid \bar { x } )$ for each of the r rules $R _ { j } ; P ( x )$ is simply the support of the consequent x, and $P ( { \bar { x } } )$ is $( 1 - P ( x ) )$ . Each of the parameters $P ( A _ { j } \mid x )$ and $P ( A _ { j } \mid \bar { x } )$ can be obtained from the confidences of the rules involved $( \mathrm { i . e . , } P ( x | A _ { i } ) )$ and the supports of x and $A _ { j }$ (i.e., P4x5 and $P ( A _ { j } ) { \big ) }$ . All these parameters can be precomputed from the data at the time the rules are mined.

Consider computing $P ( x _ { 1 } \mid \mathbf { B } )$ for consequent $x _ { 1 }$ using rules $R _ { 1 }$ and $R _ { 4 }$ from the example in Table 1. Assume that $P ( x _ { 1 } ) = 0 . 2 , P ( A _ { 1 } ) = 0 . 2 ,$ and $P ( A _ { 4 } ) = 0 . 2 1$ for our illustrative example. Using these probabilities and the confidences of the two rules, the additional parameters required in (1) can be calculated as follows:

$$
\begin{array}{c} P (\bar {x} _ {1}) = 1 - P (x _ {1}) = 0. 8, \\ P (A _ {1} | x _ {1}) = \frac {P (x _ {1} | A _ {1}) \cdot P (A _ {1})}{P (x _ {1})} = 0. 6, \\ P (A _ {1} | \bar {x} _ {1}) = \frac {P (A _ {1}) - P (x _ {1} | A _ {1}) \cdot P (A _ {1})}{(1 - P (x _ {1}))} = 0. 1, \end{array}
$$

$$
\begin{array}{l} P (A _ {4} \mid x _ {1}) = \frac {P (x _ {1} \mid A _ {4}) \cdot P (A _ {4})}{P (x _ {1})} = 0. 4 5, \\ P (A _ {4} \mid \bar {x} _ {1}) = \frac {P (A _ {4}) - P (x _ {1} \mid A _ {4}) \cdot P (A _ {4})}{(1 - P (x _ {1}))} = 0. 1 5. \end{array}
$$

Substituting these values into (1), we get

$$
P (x _ {1} \mid \mathbf {B}) = \frac {0 . 6 \cdot 0 . 4 5 \cdot 0 . 2}{0 . 6 \cdot 0 . 4 5 \cdot 0 . 2 + 0 . 1 \cdot 0 . 1 5 \cdot 0 . 8} = 0. 8 2.
$$

This example illustrates how the information from the two rules $R _ { 1 }$ and $R _ { 4 }$ can be combined. The rule with the highest confidence for consequent $x _ { 1 }$ was $R _ { 1 } ,$ with a confidence of 0.6. We see that the estimated value of $P ( x _ { 1 } \mid \mathbf { B } )$ is much higher than 0.6. This suggests that the estimates of the probability of the customer choosing a particular consequent can be quite different when multiple rules are considered, relative to that when single rules are used.

## 3.3. Multiple Ways of Computing the Probability of a Consequent

Whereas the illustration above combined rules $R _ { 1 }$ and $R _ { 4 }$ to estimate the probability that $x _ { 1 }$ will be chosen given the basket $\mathbf { B } ,$ this probability can also be estimated using the rules $R _ { 2 }$ and $R _ { 3 } .$ To do so, we need the estimates of $P ( x _ { 1 } | A _ { 2 } )$ and $P ( x _ { 1 } | A _ { 3 } )$ from Table 1, along with $P ( A _ { 2 } )$ and $P ( A _ { 3 } )$ . Suppose $P ( A _ { 2 } ) = 0 . 2$ and $P ( A _ { 3 } ) = 0 . 3$ . Then $P ( x _ { 1 } \mid \mathbf { B } )$ can be estimated as 0.75 using Equation (1). This estimate is different from that obtained when $R _ { 1 }$ and $R _ { 4 }$ are combined.

As this example illustrates, there could be many groups of rules that could be combined to estimate the probability of a feasible consequent. We call each such group an admissible group. Formally, an admissible group is defined as a set of eligible rules with disjoint antecedents that have the same consequent.

An admissible group to which no other eligible rule can be added while maintaining admissibility is called a maximal admissible group. When the union of the antecedents of the rules in the admissible group is equal to the basket B, we say that the group fully covers the basket; it partially covers the basket otherwise. The collection of all of the eligible rules for a given consequent x is called a consequent set and is denoted by G4x5. In our example, the consequent set is $\mathcal { G } ( x _ { 1 } ) = \{ \dot { R _ { 1 } } , R _ { 2 } , R _ { 3 } , R _ { 4 } \}$ , and the two maximal admissible groups corresponding to $x _ { 1 }$ are $\mathcal { S } _ { 1 } = \{ R _ { 1 } , R _ { 4 } \}$ and $\bar { \mathcal { S } } _ { 2 } = \bar { \{ } R _ { 2 }  , R _ { 3 } \}$

## 3.4. Comparing Maximal Admissible Groups

As we saw in §3.3, it may be possible to compute the confidence of x using one of several admissible groups. A natural question is, which admissible group should be used to estimate $P ( x | \mathbf { B } ) \ ?$ In this section, we first discuss how to compare maximal admissible groups that fully cover the basket; we then extend our findings to maximal admissible groups that partially cover the basket.

Ideally, we should use that admissible group which can best approximate the true joint distribution across the items in the basket B and x, i.e., P4B1 x5. Therefore, we compare the admissible groups using the likelihood of each group generating the true underlying distribution $P ( \mathbf { B } , x )$ . The likelihoods of interest in our case are those associated with the probability models implied by the collection of rules for each admissible group. Specifically, each admissible group corresponds to a probability model with some associated conditional independence assumptions. For example, the admissible group $\mathcal { S } _ { 1 } = \{ R _ { 1 } , R _ { 4 } \}$ assumes that the set $\{ i _ { 1 } , i _ { 2 } \}$ is conditionally independent of the set $\left\{ i _ { 3 } \right\}$ given $x _ { 1 } ,$ , whereas $\mathcal { S } _ { 2 } = \{ R _ { 2 } , R _ { 3 } \}$ assumes that the set $\{ i _ { 2 } , i _ { 3 } \}$ is conditionally independent of the set $\{ i _ { 1 } \}$ given $x _ { 1 }$ . Therefore, by comparing the admissible groups using their likelihoods, we are essentially checking which conditional independence assumption is most likely to hold, given the data. In essence, this problem can be viewed as one of maximizing the likelihood that the observed data are generated from the competing probability models represented by the admissible groups.<sup>6</sup>

The maximum-likelihood framework requires the estimation of the likelihoods from training data. This is not feasible in real time because training data sets can be large, and many parameters need to be estimated for each probability model. Consequently, for this to be a useful approach, we have to transform this into a problem that can be solved in real time. We show that the log-likelihood can be conveniently represented as a function of the mutual information<sup>7</sup> associated with the rules in an admissible group and the entropies of the items in the basket. The mutual information terms can be precomputed for every rule and kept available for use at run time, which eliminates the need to estimate parameters from the data during the recommendation process.

We consider the mutual information associated with a rule to be the mutual information across all of the individual attributes in the rule (including the items in both the antecedent and the consequent of the rule). Therefore, the MI across attributes $i _ { 1 } , \dots , i _ { n }$ is (Kullback 1959)

$$
\operatorname{MI} (i _ {1}, \dots , i _ {n}) = \sum_ {i _ {1}, \dots , i _ {n}} P (i _ {1}, \dots , i _ {n}) \log \frac {P (i _ {1} , \dots , i _ {n})}{P (i _ {1}) \cdots P (i _ {n})}.
$$

Thus, the mutual information associated with a rule $R _ { j }$ having antecedent $A _ { j } = \{ i _ { j 1 } , \dots , i _ { j k } \}$ and consequent $x _ { m }$ is

$$
\begin{array}{l} \operatorname{MI} (R _ {j}) = \operatorname{MI} (A _ {j}, x _ {m}) = \operatorname{MI} (i _ {j 1}, \ldots , i _ {j k}, x _ {m}) \\ \qquad = \sum_ {i _ {j 1}, \ldots , i _ {j k}, x _ {m}} P (i _ {j 1}, \ldots , i _ {j k}, x _ {m}) \\ \qquad \cdot \log \frac {P (i _ {j 1} , \ldots , i _ {j k} , x _ {m})}{P (i _ {j 1}) \cdot \cdots \cdot P (i _ {j k}) \cdot P (x _ {m})}. \end{array}
$$

The entropy of an item i is $\begin{array} { r } { H ( i ) = - \sum _ { i } P ( i ) \log P ( i ) } \end{array}$

The mutual information associated with a rule captures the mutual dependency across all of the items in the antecedent and the consequent of the rule. The entropy of an attribute is a measure of how much uncertainty is represented in the probability distribution of the attribute.

Proposition 1 shows that the log-likelihood associated with a maximal admissible group can be represented as the sum of the mutual information terms associated with each participating rule, less the sum of the entropies associated with every item in the basket B and the entropy associated with the consequent. Proposition 1 helps represent the problem using the mutual information terms associated with rules. This has intuitive appeal, as the mutual information term for a rule is higher if the items in the antecedent and the consequent are more dependent on each other. The best admissible group, therefore, is the one where the rules collectively convey as much information about the consequent as possible.

<sup>Proposition</sup> <sup>1.</sup> Given a consequent and all corresponding admissible groups that fully cover the basket, the admissible group that maximizes the likelihood also has the highest sum of the mutual information terms associated with the participating rules.

<sup>Proof.</sup> We first show that the log-likelihood associated with a maximal admissible group can be represented as the sum of the mutual information terms associated with each participating rule, less the sum of the entropies associated with the consequent and all of the items in the basket.

Given a basket $\mathbf { B } = \{ i _ { 1 } , \ldots , i _ { n } \}$ , let the consequent of interest be $i _ { n + 1 }$ . To estimate the likelihood of a probability model associated with an admissible group, we consider the distribution associated with these items, based on the absence or presence of each item in every transaction of the data set. We denote the binary attributes corresponding to the set of items as $\mathbf { I } \stackrel { \cdot } { = } \{ \mathbf { i } _ { 1 } , \ldots , \mathbf { i } _ { n } , \mathbf { i } _ { n + 1 } \}$ . Let the data set T consist of s transactions, i.e., $\mathbf { T } = \{ \mathbf { t } ^ { 1 } , \mathbf { t } ^ { 2 } , \dots , \mathbf { t } ^ { s } \}$ , where $\mathbf { t } ^ { j }$ is a vector of ones and zeroes corresponding to the presence and absence of the items $\mathbf { { \hat { i } } } _ { 1 } , \dots , \mathbf { { \tilde { i } } } _ { n + 1 }$ in the jth transaction.

Let there be r rules in an admissible group under consideration, and let $\mathbf { A } _ { l }$ denote the attributes corresponding to the antecedent $A _ { l }$ in the lth rule of the admissible group. The probability distribution corresponding to the rules in the admissible group can be written as $\begin{array} { r } { P ( \mathbf { I } ) = \prod _ { l = 1 } ^ { r } P ( \mathbf { A } _ { l } | \mathbf { i } _ { n + 1 } ) \cdot P ( \mathbf { i } _ { n + 1 } ) } \end{array}$ . The probability associated with the items appearing in the jth transaction, $P ( \mathbf { \boldsymbol { t } } ^ { j } )$ , is represented as $\begin{array} { r } { \prod _ { l = 1 } ^ { r } \bar { P } ( \mathbf { A } _ { l } ^ { j } | \mathbf { i } _ { n + 1 } ^ { j } ) \cdot P ( \mathbf { i } _ { n + 1 } ^ { j } ) } \end{array}$ , and the likelihood for the admissible group is

$$
L = \prod_ {j = 1} ^ {s} P (\mathbf {t} ^ {j}) = \prod_ {j = 1} ^ {s} \left(\left(\prod_ {l = 1} ^ {r} P (\mathbf {A} _ {l} ^ {j} \mid \mathbf {i} _ {n + 1} ^ {j})\right) \cdot P (\mathbf {i} _ {n + 1} ^ {j})\right).
$$

The log-likelihood, $L ^ { \prime } ,$ is

$$
\begin{array}{l} \log (L) = L ^ {\prime} = \sum_ {j = 1} ^ {s} \sum_ {l = 1} ^ {r} \log P (\mathbf {A} _ {l} ^ {j} | \mathbf {i} _ {n + 1} ^ {j}) + \sum_ {j = 1} ^ {s} \log P (\mathbf {i} _ {n + 1} ^ {j}) \\ = \sum_ {l = 1} ^ {r} \sum_ {j = 1} ^ {s} \log P (\mathbf {A} _ {l} ^ {j} | \mathbf {i} _ {n + 1} ^ {j}) + \sum_ {j = 1} ^ {s} \log P (\mathbf {i} _ {n + 1} ^ {j}). \end{array}\tag{2}
$$

Each instance $( \mathbf { A } _ { l } ^ { j } , \mathbf { i } _ { n + 1 } ^ { j } )$ corresponds to one of the $2 ^ { ( n + 1 ) }$ realizations of the attributes (i.e., the set of 0–1 values the attributes can assume) comprising the antecedent and the consequent of the lth rule. Let the probability for the kth realization of $( \mathbf { A } _ { l } , \mathbf { i } _ { n + 1 } )$ be $P ^ { k } ( \mathbf { A } _ { l } ^ { \bullet } , \mathbf { i } _ { n + 1 } ) . ^ { 8 }$ Furthermore, let the frequency of occurrences for the kth realization of $( \mathbf { A } _ { l } ^ { \mathsf { ^ { * } } } , \mathbf { i } _ { n + 1 } )$ be $f ^ { k } ( { \mathbf { A } } _ { l } , \mathbf { i } _ { n + 1 } )$ , and let the frequency of occurrences for the kth realization of $\mathbf { i } _ { n + 1 }$ be $f ^ { k } ( \mathbf { i } _ { n + 1 } ^ { - } )$ . Therefore,

$$
\sum_ {j = 1} ^ {s} \log P (\mathbf {A} _ {l} ^ {j} | \mathbf {i} _ {n + 1} ^ {j}) = \sum_ {k} f ^ {k} (\mathbf {A} _ {l}, \mathbf {i} _ {n + 1}) \log P ^ {k} (\mathbf {A} _ {l} | \mathbf {i} _ {n + 1}),
$$

and

$$
\sum_ {j = 1} ^ {s} \log P (\mathbf {i} _ {n + 1} ^ {j}) = \sum_ {k} f ^ {k} (\mathbf {i} _ {n + 1}) \log P ^ {k} (\mathbf {i} _ {n + 1}).
$$

Because $P ^ { k } ( \mathbf { A } _ { l } , \mathbf { i } _ { n + 1 } ) = f ^ { k } ( \mathbf { A } _ { l } , \mathbf { i } _ { n + 1 } ) / s$ and $P ^ { k } ( \mathbf { i } _ { n + 1 } ) =$ $f ^ { k } ( \mathbf { i } _ { n + 1 } ) / s ,$ , we have

$$
\begin{array}{r} \sum_ {j = 1} ^ {s} \log P (\mathbf {A} _ {l} ^ {j} | \mathbf {i} _ {n + 1} ^ {j}) = s \sum_ {k} \frac {f ^ {k} (\mathbf {A} _ {l} , \mathbf {i} _ {n + 1})}{s} \log P ^ {k} (\mathbf {A} _ {l} | \mathbf {i} _ {n + 1}) \\ = s \sum_ {k} P ^ {k} (\mathbf {A} _ {l}, \mathbf {i} _ {n + 1}) \log P ^ {k} (\mathbf {A} _ {l} | \mathbf {i} _ {n + 1}). \end{array}
$$

Similarly, $\begin{array} { r } { \sum _ { j = 1 } ^ { s } \log P ( \mathbf { i } _ { n + 1 } ^ { j } ) = s \sum _ { k } P ^ { k } ( \mathbf { i } _ { n + 1 } ) \log P ^ { k } ( \mathbf { i } _ { n + 1 } ) } \end{array}$ Substituting for

$$
\sum_ {j = 1} ^ {s} \log P (\mathbf {A} _ {l} ^ {j} | \mathbf {i} _ {n + 1} ^ {j}) \quad \text { and } \quad \sum_ {j = 1} ^ {s} \log P (\mathbf {i} _ {n + 1} ^ {j})
$$

in (2) we have

$$
\begin{array}{l} L ^ {\prime} = \sum_ {l = 1} ^ {r} s \sum_ {k} P ^ {k} (\mathbf {A} _ {l}, \mathbf {i} _ {n + 1}) \log P ^ {k} (\mathbf {A} _ {l} | \mathbf {i} _ {n + 1}) \\ \qquad + s \sum_ {k} P ^ {k} (\mathbf {i} _ {n + 1}) \log P ^ {k} (\mathbf {i} _ {n + 1}) \\ \qquad = s \sum_ {l = 1} ^ {r} \sum_ {k} P ^ {k} (\mathbf {A} _ {l}, \mathbf {i} _ {n + 1}) \log P ^ {k} (\mathbf {A} _ {l} | \mathbf {i} _ {n + 1}) \\ \qquad + s \sum_ {k} P ^ {k} (\mathbf {i} _ {n + 1}) \log P ^ {\boldsymbol k} (\mathbf {i} _ {n + 1}). \end{array}\tag{3}
$$

Consider the term $\begin{array} { r l } { { \phantom { { \sum } _ { k } } } P ^ { k } ( \mathbf { A } _ { l } , \mathbf { i } _ { n + 1 } ) } \end{array}$ log $P ^ { k } ( \mathbf { A } _ { l } | \mathbf { i } _ { n + 1 } )$ in the first sum, and let the antecedent $\mathbf { A } _ { l }$ comprise the m items $\{ i _ { 1 } , \dots , i _ { m } \} \colon$

$$
\begin{array}{l} \sum_ {k} P ^ {k} (\mathbf {A} _ {l}, \mathbf {i} _ {n + 1}) \log P ^ {k} (\mathbf {A} _ {l} | \mathbf {i} _ {n + 1}) \\ = \sum_ {k} P ^ {k} (\mathbf {i} _ {1}, \mathbf {i} _ {2}, \ldots , \mathbf {i} _ {m}, \mathbf {i} _ {n + 1}) \log \left(\frac {P ^ {k} (\mathbf {i} _ {1} , \mathbf {i} _ {2} , \ldots , \mathbf {i} _ {m} , \mathbf {i} _ {n + 1})}{P ^ {k} (\mathbf {i} _ {n + 1})}\right) \\ = \sum_ {k} P ^ {k} (\mathbf {i} _ {1}, \mathbf {i} _ {2}, \ldots , \mathbf {i} _ {m}, \mathbf {i} _ {n + 1}) \\ \cdot \log \left(\frac {P ^ {k} (\mathbf {i} _ {1} , \mathbf {i} _ {2} , \ldots , \mathbf {i} _ {m} , \mathbf {i} _ {n + 1}) \cdot P ^ {k} (\mathbf {i} _ {1}) \cdot \ldots \cdot P ^ {k} (\mathbf {i} _ {m})}{P ^ {k} (\mathbf {i} _ {1}) \cdot \ldots \cdot P ^ {k} (\mathbf {i} _ {m}) \cdot P ^ {k} (\mathbf {i} _ {n + 1})}\right) \\ = \sum_ {k} P ^ {k} (\mathbf {i} _ {1}, \mathbf {i} _ {2}, \ldots , \mathbf {i} _ {m}, \mathbf {i} _ {n + 1}) \\ \cdot \log \left(\frac {P ^ {k} (\mathbf { i} _ {1} , \mathbf {i} _ {2} , \ldots , \mathbf {i} _ {m} , \mathbf {i} _ {n + 1})}{P ^ {k} (\mathbf {i} _ {1}) \cdot \ldots \cdot P ^ {k} (\mathbf {i} _ {m}) \cdot P ^ {k} (\mathbf {i} _ {n + 1})}\right) \\ + \sum_ {k} P ^ {k} (\mathbf {i} _ {1}, \mathbf {i} _ {2}, \ldots , \mathbf {i} _ {m}, \mathbf {i} _ {n + 1}) \log (P ^ {k} (\mathbf {i} _ {1}) \cdot \ldots \cdot P ^ {k} (\mathbf {i} _ {m})) \\ = \sum_ {k} P ^ {k} (\mathbf {i} _ {1}, \mathbf {i} _ {2}, \ldots , \mathbf {i} _ {m}, \mathbf {i} _ {n + 1}) \\ \cdot \log \left(\frac {P ^ {k} (\mathbf {i} _ {1} , \mathbf {i} _ {2} , \lddots , \mathbf {i} _ {m} , \mathbf {i} _ {n + 1})}{P ^ {k} (\mathbf {i} _ {1}) \cdot \ldots \cdot P ^ {k} (\mathbf {i} _ {m}) \cdot P ^ {k} (\mathbf {i} _ {n + 1})}\right) \\ + \sum_ {k} P ^ {k} ({\mathbf i}, {\mathbf i}, {\mathbf i}, {\ldots}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf j}, {\mathbf j}, {\mathbf j}, {\mathbf j}, {\mathbf j}, {\mathbf j}, {\mathbf j}, {\mathbf j}, {\mathbf j}, {\mathbf j}, {\mathbf j}, {\mathbf j}, {\mathbf j}, {\mathbf j}, {\mathbf j}, {\mathbf j}, {\mathbf j}, {\mathbf j}, {\mathbf j}, {\mathbf j}, {\mathbf k}. \\ + \dots + \sum_ {k} P ^ {k} ({\mathbf i}, {\mathbf i}, {\mathbf i}, {\ldots}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}, {\mathbf i}. \end{array}
$$

Over all possible realizations of $\big \{ \mathbf { i } _ { 1 } , \mathbf { i } _ { 2 } , \dots , \mathbf { i } _ { m } , \mathbf { i } _ { n + 1 } \big \}$

$$
\sum_ {k} P ^ {k} \left(\mathbf {i} _ {1}, \mathbf {i} _ {2}, \dots , \mathbf {i} _ {m}, \mathbf {i} _ {n + 1}\right) \log P ^ {k} \left(\mathbf {i} _ {j}\right)
$$

simplifies to $\textstyle \sum _ { k } P ^ { k } ( \mathbf { i } _ { j } )$ log $P ^ { k } ( \mathbf { i } _ { j } )$ , with $k$ now indexing all possible realizations of $\{ \mathbf { i } _ { j } \} , \mathrm { i . e . , } 0$ and 1. Therefore,

$$
\begin{array}{c} \sum_ {k} P ^ {k} (\mathbf {A} _ {l}, \mathbf {i} _ {n + 1}) \log P ^ {k} (\mathbf {A} _ {l} | \mathbf {i} _ {n + 1}) \\ = \sum_ {k} P ^ {k} (\mathbf {i} _ {1}, \mathbf {i} _ {2}, \ldots , \mathbf {i} _ {m}, \mathbf {i} _ {n + 1}) \end{array}
$$

$$
\begin{array}{l} \cdot \log \biggl (\frac {P ^ {k} (\mathbf {i} _ {1} , \mathbf {i} _ {2} , \ldots , \mathbf {i} _ {m} , \mathbf {i} _ {n + 1})}{P ^ {k} (\mathbf {i} _ {1}) \cdot \ldots \cdot P ^ {k} (\mathbf {i} _ {m}) \cdot P ^ {k} (\mathbf {i} _ {n + 1})} \biggr) \\ + \sum_ {k} P ^ {k} (\mathbf {i} _ {1}) \log P ^ {k} (\mathbf {i} _ {1}) + \dots + \sum_ {k} P ^ {k} (\mathbf {i} _ {m}) \log P ^ {k} (\mathbf {i} _ {m}) \\ = \sum_ {k} P ^ {k} (\mathbf {i} _ {1}, \mathbf {i} _ {2}, \ldots , \mathbf {i} _ {m}, \mathbf {i} _ {n + 1}) \\ \cdot \log \biggl (\frac {P ^ {k} (\mathbf {i} _ {1} , \mathbf {i} _ {2} , \ldots , \mathbf {i} _ {m} , \mathbf {i} _ {n + 1})}{P ^ {k} (\mathbf {i} _ {1}) \cdot \ldots \cdot P ^ {k} (\mathbf {i}   _ {m}) \cdot P ^ {k} (\mathbf {i} _ {n + 1})} \biggr) \\ + \sum_ {q \in A _ {l}} \sum_ {k} P ^ {k} (\mathbf {i} _ {q}) \log P ^ {k} (\mathbf {i} _ {q}) \\ = \text { MI } (\mathbf {i} _ {1}, \mathbf {i} _ {2}, \ldots , \mathbf {i} _ {m}, \mathbf {i} _ {n + 1}) - \sum_ {q \in A _ {l}} (H _ {q}). \end{array}
$$

Therefore, by substituting for

$$
\sum_ {k} P ^ {k} (\mathbf {A} _ {l}, \mathbf {i} _ {n + 1}) \log P ^ {k} (\mathbf {A} _ {l} | \mathbf {i} _ {n + 1})
$$

in (3) we get

$$
\begin{array}{c} L ^ {\prime} = s \sum_ {l = 1} ^ {r} \mathrm{MI} _ {l} - s \sum_ {l = 1} ^ {r} \sum_ {q \in A _ {l}} (H _ {q}) - s H _ {n + 1} \\ = s \bigg (\sum_ {l = 1} ^ {r} \mathrm{MI} _ {l} - \sum_ {q = 1} ^ {n + 1} (H _ {q}) \bigg). \end{array}
$$

The entropy terms in the above expression are the same for every admissible group under consideration. Therefore, the admissible group that maximizes the likelihood has the highest sum of mutual information terms associated with the participating rules. <sup></sup>

The mutual information terms can be precomputed for every rule and kept available for use at run time. Comparing admissible groups using mutual information is straightforward. For example, suppose the mutual information values of the rules in $\mathcal { S } _ { 1 } =$ $\{ R _ { 1 } , R _ { 4 } \}$ and $\mathcal { S } _ { 2 } = \{ R _ { 2 } , R _ { 3 } \}$ are as in Table 2. Because the sum of the mutual information values for the rules in $\mathcal { S } _ { 1 } ~ ( 0 . 1 5 6 + 0 . 0 4 5 = 0 . 2 0 1 )$ is less than the corresponding value for the rules in $\mathcal { S } _ { 2 } ~ ( 0 . 1 6 4 + 0 . 0 9 8 =$ 00262), $\mathcal { S } _ { 2 }$ will be preferred over $\mathcal { S } _ { 1 }$

Given a consequent x and associated consequent set G4x5, the problem of finding the best admissible group—i.e., the admissible group that maximizes the sum of mutual information values—can be formulated as the integer program (AG) as follows:

Table 2 Mutual Information of Rules in $\mathcal { S } _ { 1 }$ and $\mathcal { S } _ { 2 }$

<table><tr><td>Rules</td><td>Items in the rules</td><td>MI</td></tr><tr><td> $R_{1}$ </td><td> $i_{1}, i_{2}, x_{1}$ </td><td>0.156</td></tr><tr><td> $R_{2}$ </td><td> $i_{2}, i_{3}, x_{1}$ </td><td>0.164</td></tr><tr><td> $R_{3}$ </td><td> $i_{1}, x_{1}$ </td><td>0.098</td></tr><tr><td> $R_{4}$ </td><td> $i_{3}, x_{1}$ </td><td>0.045</td></tr></table>

$$
\begin{array}{l} \max \sum_ {i \in G (x)} M _ {i} y _ {i}, \\ \text {s.t.} \sum_ {i \in G (x)} a _ {i j} y _ {i} = 1 \quad \forall   j \in {\bf B}, \\ y _ {i} \in \{0, 1 \} \quad \forall   i \in {\mathcal {G}} (x), \end{array}\tag{AG}
$$

where $M _ { i }$ is the mutual information corresponding to $R _ { i } \in \mathcal G ( \boldsymbol x ) , a _ { i j }$ is 1 if the $j \mathrm { t h }$ item of the basket is present in rule $R _ { i } \in \mathcal G ( x )$ and 0 otherwise, and $y _ { i }$ is a binary decision variable that is set to 1 if rule $R _ { i } \in \mathcal G ( x )$ is included in the solution and to 0 otherwise. The constraint ensures that an item in the basket can only be present in the antecedent of exactly one rule selected for inclusion in the admissible group. We note that (AG) is a set partitioning problem (Balas and Padberg 1976), and therefore NP-hard. The reason for this intractability is the combinatorial number of ways in which rules may be combined, where each combination (admissible group) is associated with a unique set of conditional independence assumptions.

So far we have considered maximal admissible groups that fully cover the basket. However, there could exist maximal admissible groups that cover only a subset of the basket; indeed, it is possible that none of the maximal admissible groups cover the entire basket. In such cases, when considering an admissible group, we assume that the items that are not covered and the consequent are independent of each other, and that the corresponding mutual information terms are zero. Although this may not be strictly true, the fact that such rules were not retained after mining suggests that the dependence is weak. This can be viewed as ensuring that rules of the form $\{ i \} \to \{ x \}$ exist for every item i in the basket by adding dummy rules with mutual information values of zero wherever necessary.

## 3.5. Finding a Good Admissible Group

As noted earlier, the problem of finding the admissible group that maximizes the sum of the mutual information values for the rules is NP-hard. When the number of items in a customer’s basket is small, the number of possible admissible groups is likely to be small and the problem can be solved easily. However, when the basket is large, it may be difficult to determine the best admissible group quickly. We propose a greedy heuristic to solve large instances of this problem, as such approaches have been shown to work well on set partitioning problems (e.g., Ergun et al. 2007). It is easy to implement and exploits the properties of the optimal solution presented in Proposition 2 and Corollary 1.

<sup>Proposition</sup> <sup>2.</sup> The mutual information corresponding to a rule $\mathbf { A } \to \{ x \}$ is always greater than or equal to the sum of the mutual information values corresponding to rules $\{ A _ { 1 } \}  \{ x \} , \ \{ { \tilde { A } } _ { 2 } \}  \{ x \} , \ldots , \{ A _ { n } \}  \ \{ x \}$ if the antecedents $A _ { 1 } , A _ { 2 } , \ldots , A _ { n }$ are mutually disjoint and $\textstyle \bigcup _ { j = 1 } ^ { n } A _ { j } = \mathbf { A } .$

<sup>Proof.</sup> The mutual information corresponding to the rule $\{ A \} \to \{ x \}$ is

$$
\begin{array}{l} = \sum_ {k} P ^ {k} (\mathbf {A}, \mathbf {x}) \log \biggl (\frac {P ^ {k} (\mathbf {A} , x)}{\prod_ {i _ {m} \in A} P ^ {k} (\mathbf {i} _ {m}) \cdot P ^ {k} (\mathbf {x})} \biggr) \\ = \sum_ {k} P ^ {k} (\mathbf {A}, \mathbf {x}) \log \biggl (\frac {P ^ {k} (\mathbf {A} \mid x)}{\prod_ {i _ {m} \in A} P ^ {k} (\mathbf {i} _ {m})} \biggr). \end{array}\tag{4}
$$

The sum of mutual information values of the rules $\{ A _ { 1 } \} \to \{ x \} , \{ A _ { 2 } \} \to \{ x \} , \dots , \{ A _ { n } \} \to \{ x \}$ is

$$
\begin{array}{l} \sum_ {j = 1} ^ {n} \sum_ {k} P ^ {k} (\mathbf {A} _ {l}, \mathbf {x}) \log \biggl (\frac {P ^ {k} (\mathbf {A} _ {j} , x)}{(\prod_ {i _ {m} \in A _ {j}} P ^ {k} (\mathbf {i} _ {m})) \cdot P ^ {k} (x)} \biggr) \\ \qquad = \sum_ {j = 1} ^ {n} \sum_ {k} P ^ {k} (\mathbf {A} _ {j}, \mathbf {x}) \log \biggl (\frac {P ^ {k} (\mathbf {A} _ {j}   |   x _ {i})}{\prod_ {i _ {m} \in A _ {j}} P ^ {k} (\mathbf {i} _ {m})} \biggr) \\ \qquad = \sum_ {j = 1} ^ {n} \sum_ {k} P ^ {k} (\mathbf {A}, \mathbf {x}) \log \biggl (\frac {P ^ {k} (\mathbf {A} _ {j}   |   \mathbf {x})}{\prod_ {i _ {m} \in A _ {j}} P ^ {k} (\mathbf {i} _ {m})} \biggr) \\ \qquad = \sum_ {k} P ^ {k} (\mathbf {A}, \mathbf {x}) \log \biggl (\frac {\prod_ {j = 1} ^ {n} P ^ {k} (\mathbf {A} _ {j}   |   x)}{\prod_ {j = 1} ^ {n} \prod_ {i _ {m} \in A _ {j}} P ^ {k} (\mathbf {i} _ {m})} \biggr) \\ \qquad = \sum_ {k} P ^ {k} (\mathbf {A}, \mathbf {x}) \log \biggl (\frac {\prod_ {j = 1} ^ {n} P ^ {k} (\mathbf {A} _ {j}   \mid   x)}{\prod_ {i _ {m} \in A} P ^ {k} (\mathbf {i} _ {m})} \biggr) \end{array}\tag{5}
$$

since $\textstyle \bigcup _ { i = 1 } ^ { n } A _ { j } = \mathbf { A }$

The denominators in the logarithm expressions are identical in Equations (4) and (5), as are the coefficients for the logarithm terms. The numerator from Equation (4) is

$$
\sum_ {k} P ^ {k} (\mathbf {A}, \mathbf {x}) \log P ^ {k} (\mathbf {A} | \mathbf {x}) = \sum_ {k} P ^ {k} (\mathbf {A} | \mathbf {x}) P ^ {k} (\mathbf {x}) \log P ^ {k} (\mathbf {A} | x).
$$

Because the distribution $P ^ { k } ( \mathbf { A } | \mathbf { x } )$ is fixed, the expression $\begin{array} { r } { \sum _ { k } P ^ { k } ( \mathbf { A } \mid \mathbf { x } ) \log P ^ { k } ( \mathbf { A } \mid x ) } \end{array}$ is the maximum possible for each value of x. Therefore, the numerator from Equation (4) is always greater than or equal to that from Equation (5). It is equal if and only if all of the conditional independence assumptions implied by the rules $\{ A _ { 1 } \} \to \{ x \} , \{ A _ { 2 } \} \to \{ x \} , \ldots , \{ A _ { n } \} \to \{ \hat { x } \}$ hold. <sup></sup>

When a consequent set includes rules of the form described in Proposition 2, we say that rule $\{ A \} \to \{ x \}$ subsumes the rules $\{ A _ { 1 } \}  \{ \bar { x } \} , \{ A _ { 2 } \}  \{ x \} , . . . ,$ $\{ A _ { n } \} \to \{ x \}$

<sup>Corollary</sup> <sup>1.</sup> An admissible group S is at least as good as another admissible group T if the antecedent of every rule in T is a subset of the antecedent of some rule in S. The admissible group S is strictly better if any of the conditional independence assumptions implied by T but not by S do not hold.

<sup>Proof.</sup> The mutual information values corresponding to the identical rules in $\mathcal { S }$ and $\mathcal { T }$ are the same. If there exists at least one rule R in $\mathcal { S }$ such that the antecedents of n rules $R _ { 1 } , \ldots , R _ { n }$ in $\mathcal { T }$ are proper subsets of the antecedent of R, then, according to Proposition 2, the mutual information corresponding to $\bar { R }$ is greater than or equal to the sum of the mutual information values corresponding to the rules $R _ { 1 } , \ldots , R _ { n } .$ Hence, the sum of the mutual information values corresponding to the rules in $\mathcal { S }$ is greater than or equal to the sum of the mutual information values corresponding to the rules in T. As shown in Proposition 2, the sum of the mutual information values corresponding to the rules $R _ { 1 } , \ldots , R _ { n }$ is strictly less if any of the conditional independence assumptions implied by S but not T do not strictly hold. <sup></sup>

The heuristic to find an admissible group for a consequent x is shown in Figure 1. The intuition is to keep adding rules with high mutual information into the admissible group without violating admissibility until no more rules can be added. Hence, the rules are arranged in a decreasing order of mutual information and are added to the admissible group starting from the rule with the highest mutual information until all of the items in the basket are covered or all of the rules have been considered. By selecting rules with higher mutual information, the heuristic ensures that the solution does not include two or more rules from the consequent set that are subsumed by a single rule from that set.

## 3.6. Computational Complexity of MLR

As mentioned earlier, the first step when recommending an item using MLR is to identify eligible rules. This requires the items in the basket to be sorted in some predetermined order (e.g., lexicographic) and, given n items in the data set, can be done in O4n log4n5) in the worst case. The eligible rules are

## Figure 1 Heuristic for Finding a Good Admissible Group

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: (i) Basket  $B = \{i_{1}, \ldots, i_{n}\}$ .
(ii) Consequent set  $\mathcal{G}(x) = \{R_{1}, \ldots, R_{m}\}$ .
Output: An admissible group for x
Steps:
1. Set item list Z = B. Initialize admissible group  $Y = \varnothing$ .
2. Sort the rules in  $\mathcal{G}(x)$  in decreasing order of mutual information.
3. Repeat steps 3(a) and 3(b) till no more rules can be added to Y.
3(a) Add the next rule from  $\mathcal{G}(x)$  to Y if all items in its antecedent are in Z. This rule has the highest mutual information among all rules whose antecedents have items in Z.
3(b) Remove the items from Z that are present in the antecedent of the added rule.
</div>

then identified by verifying whether the items in the antecedents and consequents of the rules are present in the basket. This can be done via binary search, in O4log4n)). Therefore, the presence of all items in the antecedent can be checked in O4n log4n5). If there are a total of m rules, then the complexity of checking their eligibilities is mn log4n5.

Once the set of eligible rules is created, potential items for recommendation are identified from the consequents of these rules, along with the consequent sets of each. This is done by scanning the eligible rules and adding the consequent x of each rule into M if it is not present already, and by adding the rule to the appropriate consequent list G4x5. The presence of an item in M can be checked using binary search, whereas binary insertion can be used to add a new consequent into M. The complexity of checking for the presence of an item or adding an item in M is O4log4n)). Thus, given n items in the data set, the complexity of identifying potential recommendations and creating the consequent sets is O4n log4n)). When all of the rules in the set of eligible rules have been considered, M contains all items x that can potentially be recommended and the corresponding lists G4x5 are their consequent sets.

The next step is to apply the heuristic proposed in Figure 1 to each consequent in M. Creating the admissible group for a consequent requires checking whether the items in the antecedents of rules in the associated consequent set are present in the basket; this is of complexity O4n log4n)) for each rule. In the worst case, items in the antecedents of all m rules may have to be checked for their presence in the basket; this is of complexity O4mn log4n55. This procedure has to be repeated for every possible consequent, and therefore the worst case complexity of the heuristic is O4mn<sup>2</sup> log4n55.

The probabilities can be estimated for each item in M using the rules in the admissible groups in O4m5. Across all items, therefore, the complexity is O4mn5. The item with the highest estimated probability can be identified in O4n5, through a single scan of M.

Thus, the overall complexity of MLR is O4mn<sup>2</sup> log4n55, which is linear in the number of rules mined, and has a low-order polynomial complexity in the number of items in the data set. Because the size of a typical basket is much smaller than n, the average complexity should be much better. Note that the complexity does not depend on the size of the data set—once the rules are mined, MLR does not use the data set to find items to recommend.

## 4. Experiments

We conduct a large number of systematic experiments on several real data sets to investigate the quality of recommendations made by MLR. First, we conduct experiments comparing recommendations made using the optimal approach to identify admissible groups (i.e., formulation AG) with those made by the greedy heuristic presented in Figure 1. Then we conduct experiments comparing recommendations made using MLR with various benchmarks including the single-rule approaches of Zaïane (2002), Wang and Shao (2004), and Baralis et al. (2004) (called L3G), and the rule combination methods of Li et al. (2001) and Lin et al. (2002) (comparison with nonrule-based approaches are presented in §5). All of the experiments are performed using code written in Java, on a Pentium Dual Core machine (2.6 GHz) with 32 GB RAM.

## 4.1. Data

We use three real data sets in our experiments. Data sets Retail and BMS-POS were obtained from the Frequent Itemset Mining Implementations Dataset repository (http://fimi.ua.ac.be/data/), whereas the third data set, comScore2013, was obtained from Wharton Research Data Services. Retail is a marketbasket data set collected from a Belgian retail store (Brijs et al. 2014), BMS-POS is a point-of-sales data set collected from a large electronics retailer (Zheng et al. 2001), and comScore2013 is a transactional data set consisting of items purchased by customers from various online e-retailers in the year 2013. The basic characteristics of the data sets are shown in Table 3.

One point of clarification is needed here with regard to data set size. There are two conventions used to represent market basket data sets. In one, a basket is a record of items that are purchased together, and would essentially comprise a list of items along with the ID of the transaction—this is the convention we have followed in our paper. However, there is another commonly used convention where data sets (including the comScore2013 data set used in our experiments) represent a basket as transaction ID–item pairs, breaking up a single transaction across many rows of data. For example, a transaction i involving the purchase of items A, B, and C would be represented as a single row (record) 8i1 A1 B1 C9 if the first convention was followed, whereas it would be represented as three separate records 8i1 A9, 8i1 B9, and 8i1 C9 in the alternate representation. The former representation will contain as many records as transactions, whereas the latter will have as many records as transaction– item pairs. When comparing data set size in terms of records, we need to make sure that the same convention is used. The row labeled “Number of transaction\_id-item pairs” provides the data set size using the latter approach (after eliminating duplicate/ redundant records), whereas the row titled “Number of transactions” provides the number of transactions based on the former representation. The BMS-POS data set is by far the largest, having 515,597 transactions and over three million transaction–item pairs. The comScore2013 data set is the most current and involves 22,963 transactions and about 85,000 nonredundant transaction–item pairs. The retail data set is in between in size using either metric, with 88,162 transactions and approximately 900,000 pairs.

Table 3 Data Set Characteristics

<table><tr><td>Characteristics</td><td>Retail</td><td>BMS-POS</td><td>comScore2013</td></tr><tr><td>Number of items</td><td>16,470</td><td>1,657</td><td>60</td></tr><tr><td>Number of transaction_id-item pairs</td><td>908,069</td><td>3,351,381</td><td>84,963</td></tr><tr><td>Number of transactions</td><td>88,162</td><td>515,597</td><td>22,963</td></tr><tr><td>Average transaction length (items)</td><td>10.3</td><td>6.5</td><td>3.7</td></tr></table>

As can be seen from Table 3, Retail is the least dense of the three data sets we have used—customers purchase an average of 10.3 items from a maximum possible 16,470, resulting in a data set density of 41003/1614705 = 000625%. comScore2013, with a density of (3.7/60), or 6.17%, is the densest, and the density of BMS-POS falls in between (0.39%).

All data sets have the items in the transactions ordered lexicographically based on their labels. We randomize the ordering of items in each transaction to avoid any bias that might result from this preordering of the items. Eighty percent of the transactions from each data set are used for training (e.g., generating rules or learning models), with the rest used for testing purposes.

## 4.2. MLR vs. Rule-Based Systems: Experimental Setup

The experiments involve performing fivefold crossvalidation tests using these data sets. In the experiments, baskets are provided to the recommender systems (MLR and the relevant benchmark), and the number of successful recommendations made by each approach is tracked. The experiments are designed to mimic the interactions of a customer at a website to the extent possible. The recommender system can recommend items every time a customer adds an item to the basket. To replicate this process, each transaction in the test data set is used to create multiple test baskets iteratively. The first basket created from a transaction contains the first item in the transaction. Each recommender system recommends an item for potential addition into the basket. If the recommended item is present in the remainder of the transaction, the recommendation is considered successful, and the recommended item is then added to the basket to create the next basket. If both systems recommend different items successfully, both items are added to the basket to avoid any potential bias from the addition of just one of them.<sup>9</sup> If neither recommendation is successful, a randomly selected item from the remainder of the transaction is added to the basket. This process is repeated for the transactions until at least half of the items in the transactions are included in the basket.<sup>10</sup> This is repeated for every transaction in the test data set. The approaches are compared based on average accuracy of recommendations. The results reported are for baskets for which both approaches (MLR and the benchmark) provide recommendations.<sup>11</sup>

Table 4 Comparing Optimal and Heuristic Approaches

<table><tr><td rowspan="2">Data set</td><td rowspan="2">Conf. threshold (%)</td><td rowspan="2">No. of rules mined</td><td rowspan="2">No. of baskets</td><td colspan="2">No. of successful recommendations</td></tr><tr><td>Optimal</td><td>Heuristic</td></tr><tr><td rowspan="4">Retail</td><td>30</td><td>2,136</td><td>52,246</td><td>13,036</td><td>13,036</td></tr><tr><td>40</td><td>2,022</td><td>46,720</td><td>12,837</td><td>12,837</td></tr><tr><td>50</td><td>1,954</td><td>44,767</td><td>12,793</td><td>12,793</td></tr><tr><td>60</td><td>1,512</td><td>37,144</td><td>10,970</td><td>10,969</td></tr><tr><td rowspan="4">BMS-POS</td><td>30</td><td>69,207</td><td>301,100</td><td>97,362</td><td>96,902</td></tr><tr><td>40</td><td>56,795</td><td>275,274</td><td>93,586</td><td>93,174</td></tr><tr><td>50</td><td>45,517</td><td>231,700</td><td>86,571</td><td>86,321</td></tr><tr><td>60</td><td>32,019</td><td>179,756</td><td>76,604</td><td>76,542</td></tr><tr><td rowspan="4">comScore2013</td><td>30</td><td>168,392</td><td>7,166</td><td>2,487</td><td>2,471</td></tr><tr><td>40</td><td>141,035</td><td>7,166</td><td>2,373</td><td>2,355</td></tr><tr><td>50</td><td>111,719</td><td>7,168</td><td>2,147</td><td>2,128</td></tr><tr><td>60</td><td>84,954</td><td>7,171</td><td>1,703</td><td>1,695</td></tr></table>

## 4.3. Finding the Best Admissible Group: Optimal vs. Heuristic Approaches

As part of the MLR process, we need to identify the best admissible group from the many combinations that might exist. We showed in §3.4 that this problem is NP-hard and can be represented as the set-partitioning problem AG. Furthermore, we proposed a heuristic to achieve the same end (Figure 1). In our first set of experiments, we compare these two versions of MLR—one using the optimal solution from the set partitioning problem AG and the other the solution from the heuristic—to understand the practical impact on recommendation accuracy of using the heuristic. Table 4 shows the results of the experiments for a support threshold of 0.2%<sup>12</sup> and confidence thresholds of 30%, 40%, 50%, and 60% (increasing the confidence threshold beyond 60% generates very few rules).

Table 5 MLR vs. Single Rules: MLR Uses Multiple Rules

<table><tr><td rowspan="2">Data set</td><td rowspan="2">Conf. threshold (%)</td><td rowspan="2">Baskets where MLR used ≥ 2 rules</td><td colspan="2">MLR</td><td colspan="2">Single-rule approach (Zaïane 2002)</td><td rowspan="2">Improvement (%)</td></tr><tr><td>Accuracy no. (%)</td><td>Time</td><td>Accuracy no. (%)</td><td>Time</td></tr><tr><td rowspan="4">Retail</td><td>30</td><td>16,929</td><td>917 (5.42%)</td><td>0.00054</td><td>776 (4.58%)</td><td>0.00048</td><td>18.20***</td></tr><tr><td>40</td><td>15,975</td><td>914 (5.72%)</td><td>0.00053</td><td>773 (4.84%)</td><td>0.00048</td><td>18.24***</td></tr><tr><td>50</td><td>15,761</td><td>881 (5.59%)</td><td>0.00051</td><td>742 (4.71%)</td><td>0.00045</td><td>18.71***</td></tr><tr><td>60</td><td>9,214</td><td>233 (2.53%)</td><td>0.00050</td><td>211 (2.29%)</td><td>0.00045</td><td>10.43</td></tr><tr><td rowspan="4">BMS-POS</td><td>30</td><td>103,718</td><td>9,865 (9.51%)</td><td>0.00853</td><td>8,523 (8.22%)</td><td>0.00762</td><td>15.74***</td></tr><tr><td>40</td><td>64,689</td><td>4,838 (7.48%)</td><td>0.00798</td><td>4,277 (6.61%)</td><td>0.00754</td><td>13.14***</td></tr><tr><td>50</td><td>32,107</td><td>1,776 (5.53%)</td><td>0.00779</td><td>1,495 (4.66%)</td><td>0.00757</td><td>18.78***</td></tr><tr><td>60</td><td>17,398</td><td>492 (2.83%)</td><td>0.00631</td><td>428 (2.46%)</td><td>0.00620</td><td>14.90**</td></tr><tr><td rowspan="4">comScore2013</td><td>30</td><td>689</td><td>91 (13.27%)</td><td>0.01638</td><td>54 (7.9%)</td><td>0.01303</td><td>68.01***</td></tr><tr><td>40</td><td>494</td><td>56 (11.38%)</td><td>0.01437</td><td>29 (5.87%)</td><td>0.01282</td><td>93.79***</td></tr><tr><td>50</td><td>291</td><td>25 (8.72%)</td><td>0.01360</td><td>14 (4.67%)</td><td>0.01286</td><td>86.76**</td></tr><tr><td>60</td><td>129</td><td>10 (7.45%)</td><td>0.01273</td><td>6 (4.5%)</td><td>0.01226</td><td>65.52</td></tr></table>

<sup>∗∗</sup>Significant at the 5% level; <sup>∗∗∗</sup>significant at the 1% level.

These results show that although using the optimal admissible groups sometimes does lead to more successful recommendations, the improvement in performance is very small. For the experiments conducted on the Retail data set, the results are virtually identical. The differences are greater for the experiments conducted on the data sets BMS-POS and com-Score2013. However, none of the differences are statistically significant. We also found that the number of instances where the heuristic and optimal approaches choose different admissible groups is also very small. At the same time, the time taken by the heuristic to make recommendations is a fraction of the time taken by the optimal approach. Incorporating an integer programming solver into a recommender system is worthwhile only if the benefits over easily implemented procedures are substantial. Given the results of these experiments, that does not seem to be the case. Consequently, all of the other results reported in this paper are based on using the heuristic. Of course, in situations where the optimal approach is viable, the results are likely to be better than those currently being reported.

The number of rules generated for the same set of support and confidence thresholds depends on the data set density. Therefore, mining Retail results in the fewest number of rules and mining comScore2013 results in the most. The average number of rules generated from each data set (for each of the parameter settings used in our experiments) is also provided in Table 4.

## 4.4. MLR vs. Single-Rule-Based Approaches

We conduct several experiments to compare MLR with the single-rule-based approaches of Zaïane (2002), Wang and Shao (2004), and Baralis et al. (2004). The approach proposed by Baralis et al. (2004) (called L3G), is for classification. We have adapted it to the item recommendation context—in a transactional data set, the consequents of eligible rules are analogous to classes to which a customer may belong. The performances of all of the single-rule-based approaches are similar, and therefore we present only the results comparing MLR with the approach of Zaïane (2002). As in the previous section, the first set of experiments are performed with rules mined from the training data sets using a support threshold of 0.2% and confidence thresholds of 30%, 40%, 50%, and 60%.

4.4.1. MLR Uses Multiple Rules. When making recommendations using MLR, the admissible group corresponding to the recommended item may contain one or multiple rules. When an item is recommended using an admissible group with only one rule, it is typically the same as that recommended by the single-rulebased benchmark. However, significant improvements in performance are observed when MLR recommends items using admissible groups with multiple rules. Table 5 presents the results for those instances for whichitems are recommendedusingmultiple rules.The results are averaged over five cross-validation experiments. The number of rules combined usually ranged between two and three.

The first column of Table 5 identifies the data set. The second column shows the confidence threshold used for mining. The third column shows the numbers of baskets where MLR recommended items using multiple rules. The fourth and fifth columns show the number (and percentage) of successful recommendations with MLR and the average time taken, respectively. The sixth and seventh columns present similar information for the single-rule approach. The last column shows the percentage improvement using MLR.

Table 5 shows that MLR performs substantially better than the single-rule approach when items are recommended using multiple rules. The improvements in performances by using MLR are statistically significant at the 1% level or better in most of the experiments. Although the absolute improvements may appear small, the relative improvements are substantial; given the very large number of recommendations that are typically made every day, the net impact on revenues will be substantial as well. The times taken to make recommendations are in milliseconds for both approaches; because these times are possible even on the basic desktop machines we used to conduct the experiments, making recommendations using either of these approaches will not have any perceptible impact on the load times of Web pages. In addition, the standard deviations are also very low—in the worst case they are 0.00229 for Retail, 0.00853 for BMS-POS, and 0.01638 for comScore2013. This makes MLR a very viable approach for real-time situations.

Table 6 Fraction of Basket Covered When MLR Uses Multiple Rules

<table><tr><td rowspan="2">Data set</td><td rowspan="2">Conf. threshold (%)</td><td colspan="2">Percentage of items covered when MLR uses multiple rules</td></tr><tr><td>MLR (%)</td><td>Single-rule approach (%)</td></tr><tr><td rowspan="4">Retail</td><td>30</td><td>56.26</td><td>26.95</td></tr><tr><td>40</td><td>56.76</td><td>26.83</td></tr><tr><td>50</td><td>56.46</td><td>26.67</td></tr><tr><td>60</td><td>46.84</td><td>23.42</td></tr><tr><td rowspan="4">BMS-POS</td><td>30</td><td>85.90</td><td>53.22</td></tr><tr><td>40</td><td>78.01</td><td>48.34</td></tr><tr><td>50</td><td>76.86</td><td>44.84</td></tr><tr><td>60</td><td>83.70</td><td>45.59</td></tr><tr><td rowspan="4">comScore2013</td><td>30</td><td>98.09</td><td>65.38</td></tr><tr><td>40</td><td>97.06</td><td>63.25</td></tr><tr><td>50</td><td>95.53</td><td>60.23</td></tr><tr><td>60</td><td>93.68</td><td>57.45</td></tr></table>

For a given data set and support threshold, there are fewer eligible rules for each consequent when a higher confidence threshold is used for mining. Consequently, MLR requires less time to recommend items as the confidence threshold increases. Similarly, the average times required by the two approaches are highest for comScore2013 and lowest for Retail, as a result of the difference in the number of rules mined.

When MLR recommends items using multiple rules, the rules used cover a much larger proportion of items in the baskets compared to the coverages of the rules used by the single-rule approach. In Table $^ { 6 , }$ we show the average percentages of items in the baskets covered by the two approaches for each data set. Combining the results in Tables 5 and $6 ,$ it is clear that increasing the coverage of items in the baskets substantively improves the performance of the recommender system. Because all of the items in these baskets rarely co-occur simultaneously in transactions, they do not appear as antecedents of any rule. The rules that exist—which get used by the benchmark— cover a relatively small percentage of items in the baskets. By combining rules, MLR is able to improve the coverage and thereby perform better than the benchmark.

The coverage of items is smallest in Retail and largest in comScore2013 when either of the approaches is used. This is again a direct result of data set density—the rules generated from Retail have only a few items, whereas those from comScore2013 have many more relative to the number of items in the data set. Even when MLR combines rules, only about half of the items in the baskets are covered in the case of Retail, whereas more than 90% of the baskets are covered in the case of comScore2013.

4.4.2. MLR Uses One Rule. As mentioned earlier, MLR may provide a recommendation using a probability model consisting of a single rule. For completeness, we present the results for instances where MLR uses single rules in Table 7. Given that both approaches recommend the same item often, the results are as expected—the qualities of the recommendations provided by the approaches are quite similar.

The performances of both approaches are much better when MLR recommends items using single rules (the fourth column of Table 7) compared to when it recommends items using multiple rules (the fourth column of Table 5). This is because the baskets for which MLR makes recommendations using multiple rules are typically larger (than baskets for which single rules are used), and the items in the baskets for which MLR makes recommendations using multiple rules co-occur less frequently in transactions. Therefore, it is less likely that there would be reliable probability estimates for many of the potential target items given the entire basket. As a result, it is far more difficult to recommend items that are likely to be purchased in the former case than in the latter; this difficulty is reflected in the marked differences in successful recommendations. When single rules are used for recommending items for the baskets included in Table 5, recommendations are significantly worse than when MLR is used. Also, as expected, MLR requires less time to recommend items when using single rules (the fifth column of Table 7) than when using multiple rules (the fifth column of Table 5) because the available numbers of eligible rules are fewer in the former case. Table 8 shows the percentages of items in the baskets covered by the rules used by the two approaches.

It is clear that the percentages are very close and, furthermore, the majority of items in the baskets are covered. Hence, the accuracies of both of the approaches are similar. The effect of density is clear here as well—the fraction of the baskets covered is lowest for Retail and highest for comScore2013, irrespective of the approach used.

Table 7 MLR vs. Single Rules: MLR Also Uses Single Rules

<table><tr><td rowspan="2">Data set</td><td rowspan="2">Conf. threshold (%)</td><td rowspan="2">Baskets where MLR used 1 rule</td><td colspan="2">MLR</td><td colspan="2">Single-rule approach (Zaïane 2002)</td><td rowspan="2">Improvement (%)</td></tr><tr><td>Accuracy no. (%)</td><td>Time</td><td>Accuracy no. (%)</td><td>Time</td></tr><tr><td rowspan="4">Retail</td><td>30</td><td>35,278</td><td>12,058 (34.18%)</td><td>0.00036</td><td>12,054 (34.17%)</td><td>0.00039</td><td>0.04</td></tr><tr><td>40</td><td>30,705</td><td>11,862 (38.63%)</td><td>0.00036</td><td>11,856 (38.61%)</td><td>0.00038</td><td>0.05</td></tr><tr><td>50</td><td>28,966</td><td>11,852 (40.92%)</td><td>0.00033</td><td>11,845 (40.89%)</td><td>0.00035</td><td>0.06</td></tr><tr><td>60</td><td>27,904</td><td>10,693 (38.32%)</td><td>0.00034</td><td>10,690 (38.31%)</td><td>0.00035</td><td>0.03</td></tr><tr><td rowspan="4">BMS-POS</td><td>30</td><td>199,542</td><td>86,977 (43.59%)</td><td>0.00563</td><td>86,968 (43.58%)</td><td>0.00509</td><td>0.01</td></tr><tr><td>40</td><td>213,461</td><td>88,707 (41.56%)</td><td>0.00582</td><td>88,657 (41.53%)</td><td>0.00531</td><td>0.06</td></tr><tr><td>50</td><td>201,471</td><td>84,883 (42.13%)</td><td>0.00600</td><td>84,765 (42.07%)</td><td>0.00579</td><td>0.14</td></tr><tr><td>60</td><td>163,312</td><td>76,400 (46.78%)</td><td>0.00561</td><td>76,279 (46.71%)</td><td>0.00529</td><td>0.16</td></tr><tr><td rowspan="4">comScore2013</td><td>30</td><td>6,457</td><td>2,365 (36.63%)</td><td>0.00968</td><td>2,362 (36.58%)</td><td>0.00944</td><td>0.14</td></tr><tr><td>40</td><td>6,087</td><td>2,287 (37.58%)</td><td>0.00977</td><td>2,286 (37.56%)</td><td>0.00961</td><td>0.04</td></tr><tr><td>50</td><td>5,473</td><td>2,089 (38.17%)</td><td>0.00970</td><td>2,086 (38.12%)</td><td>0.00964</td><td>0.13</td></tr><tr><td>60</td><td>3,921</td><td>1,666 (42.48%)</td><td>0.00998</td><td>1,661 (42.36%)</td><td>0.00990</td><td>0.28</td></tr></table>

Table 8 Fraction of Basket Covered When MLR Uses Single Rules

<table><tr><td rowspan="2">Data set</td><td rowspan="2">Conf. threshold (%)</td><td colspan="2">Percentage of items covered when MLR uses single rules</td></tr><tr><td>MLR (%)</td><td>Single-rule benchmark (%)</td></tr><tr><td rowspan="4">Retail</td><td>30</td><td>60.58</td><td>58.86</td></tr><tr><td>40</td><td>62.51</td><td>60.71</td></tr><tr><td>50</td><td>63.67</td><td>61.88</td></tr><tr><td>60</td><td>56.48</td><td>54.86</td></tr><tr><td rowspan="4">BMS-POS</td><td>30</td><td>93.91</td><td>93.08</td></tr><tr><td>40</td><td>88.13</td><td>87.18</td></tr><tr><td>50</td><td>82.52</td><td>81.56</td></tr><tr><td>60</td><td>81.49</td><td>80.76</td></tr><tr><td rowspan="4">comScore2013</td><td>30</td><td>99.14</td><td>98.42</td></tr><tr><td>40</td><td>98.34</td><td>97.58</td></tr><tr><td>50</td><td>97.05</td><td>96.06</td></tr><tr><td>60</td><td>94.59</td><td>93.12</td></tr></table>

4.4.3. Experiments with Different Supports. We perform additional experiments on Retail at support thresholds 0.1% and 0.3% to analyze the robustness of the two approaches to changes in the support threshold. The results are shown in Table 9. We present results only for those instances where MLR recommends items using multiple rules, as the performances of MLR and the benchmark are again quite similar for the other instances.

MLR performs better when items are recommended using multiple rules regardless of the support and confidence thresholds used for mining. The improvements are statistically significant, with an exception only when rules mined at 60% confidence thresholds are used. The improvement in performance is smaller when the rules mined at higher support thresholds are used. For example, the improvement achieved by using MLR is 23.25% when rules mined at support and confidence thresholds of 0.1% and 30%, respectively, are used, compared to 14.83% when rules mined at a 0.3% support threshold and 30% confidence threshold are used. One possible reason could be the more frequent use of rules with higher supports by the single-rule approach when rules mined at higher support thresholds are used. Rules with higher supports are more reliable. Hence, the scope for improvement by using MLR is smaller.

As evident from Table 9, the performance of association-rule-based recommender systems varies with the support and confidence thresholds used for mining the rules. No established theoretical basis exists for the selection of appropriate thresholds (Goh and Ang 2007). The thresholds to use depend on the application characteristics (e.g., the data density, the number of items being sold, the size of the database, etc.). They can be empirically determined by examining the performances of rules mined from representative historical data with different sets of thresholds (Liu and Hsu 2005, Goh and Ang 2007, Witten et al. 2011). Domain experts can also help determine acceptable thresholds (Schiaffino and Amandi 2006).

4.4.4. Rules Mined Using Lift and Leverage Instead of Confidence. Although confidence<sup>13</sup> is the most widely used metric for rule generation, other metrics like lift and leverage are also used occasionally. Given a rule $\{ A \} \to \{ X \}$ , lift is defined as the ratio of the confidence of the rule to the support of its consequent, i.e., 4P4A and $X ) / ( P ( A ) P ( X ) { \hat { ) } } )$ 5. Lift measures the relative increase in the probability of the consequent given the antecedent compared to the consequent’s prior. Leverage is the difference between the actual frequency of co-occurrence of A and X and the expected frequency if A and X were independent, i.e., leverage is $\overset { \underset { \star } { P } ( A }$ and X5 − P4A5 · P4X5. In a sales setting, this would translate to the number of extra items sold than the number expected under independence. We conducted additional experiments to assess the performance of MLR when rules mined using lift and leverage are used for making recommendations.

Table 9 Multiple Support Levels on Retail: MLR Uses Multiple Rules

<table><tr><td rowspan="2">Sup. threshold (%)</td><td rowspan="2">Conf. threshold (%)</td><td rowspan="2">Baskets where MLR used ≥ 2 rules</td><td colspan="2">MLR</td><td colspan="2">Single-rule approach</td><td rowspan="2">Improvement (%)</td></tr><tr><td>Accuracy no. (%)</td><td>Time</td><td>Accuracy no. (%)</td><td>Time</td></tr><tr><td rowspan="4">0.1</td><td>30</td><td>24,616</td><td>1,141 (4.63%)</td><td>0.013</td><td>926 (3.76%)</td><td>0.004</td><td>23.25***</td></tr><tr><td>40</td><td>22,818</td><td>1,106 (4.85%)</td><td>0.012</td><td>901 (3.95%)</td><td>0.004</td><td>22.80***</td></tr><tr><td>50</td><td>22,212</td><td>1,006 (4.53%)</td><td>0.012</td><td>818 (3.68%)</td><td>0.004</td><td>22.99***</td></tr><tr><td>60</td><td>14,380</td><td>340 (2.37%)</td><td>0.010</td><td>298 (2.08%)</td><td>0.004</td><td>14.08*</td></tr><tr><td rowspan="4">0.3</td><td>30</td><td>12,494</td><td>780 (6.25%)</td><td>0.002</td><td>680 (5.44%)</td><td>0.001</td><td>14.83***</td></tr><tr><td>40</td><td>12,020</td><td>780 (6.49%)</td><td>0.002</td><td>679 (5.65%)</td><td>0.001</td><td>14.87***</td></tr><tr><td>50</td><td>11,884</td><td>761 (6.40%)</td><td>0.002</td><td>661 (5.56%)</td><td>0.001</td><td>15.16*</td></tr><tr><td>60</td><td>6,467</td><td>171 (2.64%)</td><td>0.002</td><td>159 (2.46%)</td><td>0.001</td><td>7.28</td></tr></table>

<sup>∗</sup>Significant at the 10% level; <sup>∗∗∗</sup>significant at the 1% level or better.

We first compared recommendation accuracies using each of the three metrics (confidence, lift, and leverage). We found confidence-based rules to perform significantly better than lift-based rules on all three data sets. We know from Table 5 that MLR significantly outperforms the single-rule-based approach when rules generated using confidence are used. Therefore, MLR using rules based on confidence clearly dominate rules generated using lift. Whereas confidence-based rules significantly outperform leverage-based rules on Retail, the improvements are not significant on BMS-POS and comScore2013. We then compared the performance of MLR with the single-rule approach when the rules available are mined using leverage. As was the case earlier (with confidence based rules), we found that using MLR on leverage-based rules significantly outperformed the (leverage based) single-rule approach. Therefore, MLR is preferable over all of the single-rule-based approaches.

4.4.5. Recommending Multiple Items. We also conduct experiments where two items are recommended for each basket by both approaches. We consider a recommendation to be successful when at least one of the two recommended items is present in the remainder of the transaction. BMS-POS is used for the experiments, and the rules are mined at a support threshold of 0.2% and confidence thresholds of 15%, 20%, 25%, 30%, and 35%, respectively. The reason for using rules mined at these thresholds is that the average number of items that can be recommended per basket is four or more when rules mined at these thresholds are used.

Table 10 shows the results of the experiments for those baskets for which MLR recommends both items using multiple rules; the performance improvement is significant. The differences in the performances of the two approaches are not significant when either one or both items are recommended by MLR using single rules. The times taken to make the multiple recommendations are virtually identical to those when single items are recommended (i.e., as shown in Table 5).

## 4.5. MLR vs. Rule Combination Approaches

Various experiments were conducted comparing MLR with the rule combination approach of Lin et al. (2002) and the CMAR approach of Li et al. (2001). The improvement from using MLR compared with the approach of Lin et al. (2002) was more than the improvement over CMAR. Therefore, we only report results comparing MLR with CMAR.

CMAR was developed for classification, and therefore we had to adapt it to work in a product recommendation context (as discussed for L3G). CMAR works as follows. When a basket is provided to CMAR, it evaluates the sums of the weighted -squares of the rules in the individual consequent sets, and the item corresponding to the consequent set with the highest sum is recommended. The -square of a rule indicates the correlation between the items in the rule. Rules in a consequent set with the highest sum of weighted -squares have the highest correlation with each other, and the consequent corresponding to that consequent set is expected to have the highest probability of occurrence (Li et al. 2001). The sum of the weighted -squares of the rules in a consequent is $\Sigma ( \chi ^ { 2 } \chi ^ { 2 } / \operatorname* { m a x } \chi ^ { 2 } )$ , where $\chi ^ { 2 }$ is the -square statistic of a rule with antecedent P and consequent c, and max $\chi ^ { 2 }$ is evaluated as

$$
\max \chi^ {2} = \left(\min \{\sup (P), \sup (c) \} - \frac {\sup (P) \sup (c)}{| T |}\right) ^ {2} | T | e,
$$

Table 10 MLR vs. Single Rule When Two Items are Recommended (BMS-POS)

<table><tr><td>Conf. threshold (%)</td><td>No. of baskets</td><td>MLR accuracy no. (%)</td><td>Single rule accuracy no. (%)</td><td>Improvement (%)</td></tr><tr><td>15</td><td>43,360</td><td>4,407 (10.16%)</td><td>3,569 (8.23%)</td><td>23.49***</td></tr><tr><td>20</td><td>41,916</td><td>3,851 (9.19%)</td><td>3,236 (7.72%)</td><td>18.99***</td></tr><tr><td>25</td><td>38,338</td><td>3,137 (8.18%)</td><td>2,745 (7.16%)</td><td>14.26***</td></tr><tr><td>30</td><td>30,474</td><td>2,086 (6.84%)</td><td>1,891 (6.20%)</td><td>10.31***</td></tr><tr><td>35</td><td>19,886</td><td>1,080 (5.43%)</td><td>1,002 (5.04%)</td><td>7.70</td></tr></table>

<sup>∗∗∗</sup>Significant at the 1% level or better.

Table 11 MLR vs. CMAR

<table><tr><td></td><td>Conf. threshold (%)</td><td>No. of baskets</td><td colspan="2">MLR accuracy no. (%)</td><td colspan="2">CMAR accuracy no. (%)</td><td>Improvement (%)</td></tr><tr><td rowspan="4">Retail</td><td>30</td><td>51,417</td><td>12,058</td><td>(23.45%)</td><td>11,635</td><td>(22.63%)</td><td>3.64***</td></tr><tr><td>40</td><td>45,909</td><td>11,840</td><td>(25.79%)</td><td>11,515</td><td>(25.08%)</td><td>2.82**</td></tr><tr><td>50</td><td>43,974</td><td>11,804</td><td>(26.84%)</td><td>11,498</td><td>(26.15%)</td><td>2.66**</td></tr><tr><td>60</td><td>36,751</td><td>10,506</td><td>(28.59%)</td><td>10,439</td><td>(28.40%)</td><td>0.65</td></tr><tr><td rowspan="4">BMS-POS</td><td>30</td><td>59,111</td><td>17,727</td><td>(29.99%)</td><td>15,617</td><td>(26.42%)</td><td>13.51***</td></tr><tr><td>40</td><td>54,366</td><td>17,317</td><td>(31.85%)</td><td>16,958</td><td>(31.19%)</td><td>2.12**</td></tr><tr><td>50</td><td>45,671</td><td>16,153</td><td>(35.37%)</td><td>15,753</td><td>(34.49%)</td><td>2.54***</td></tr><tr><td>60</td><td>35,352</td><td>14,547</td><td>(41.15%)</td><td>14,347</td><td>(40.58%)</td><td>1.40</td></tr><tr><td rowspan="4">comScore2013</td><td>30</td><td>6,882</td><td>2,203</td><td>(32.00%)</td><td>2,152</td><td>(31.27%)</td><td>2.36</td></tr><tr><td>40</td><td>6,346</td><td>2,102</td><td>(33.12%)</td><td>2,055</td><td>(32.38%)</td><td>2.27</td></tr><tr><td>50</td><td>5,576</td><td>1,911</td><td>(34.27%)</td><td>1,890</td><td>(33.89%)</td><td>1.10</td></tr><tr><td>60</td><td>3,937</td><td>1,554</td><td>(39.46%)</td><td>1,539</td><td>(39.08%)</td><td>0.96</td></tr></table>

<sup>∗∗</sup>Significant at the 5% level; <sup>∗∗∗</sup>significant at the 1% level or better.

where

$$
\begin{array}{r l} e = \frac {1}{\sup (P) \sup (c)} + \frac {1}{\sup (P) (| T | - \sup (c))} \\ & + \frac {1}{(| T | - \sup (P)) \sup (c)} \\ & + \frac {1}{(| T | - \sup (P)) (| T | - \sup (c))}, \end{array}
$$

sup4P 5 = number of transactions with items in P , sup4c5 = number of transactions with consequent $c ,$ and

T  = total number of transactions.

Readers are referred to Li et al. (2001) for additional details of their approach.

As with the previous comparison, experiments are first performed using rules mined at a support threshold of 0.2% and confidence thresholds of 30%, 40%, 50%, and 60% on all of the data sets. Table 11 shows the results of the experiments over all of the baskets.<sup>14</sup> Each individual recommendation is made within a fraction of a second by both approaches. For the Retail and BMS-POS data sets, the improvements in the performances achieved by using MLR are statistically significant except when rules mined at a 60% confidence threshold are used. In the case of com-Score2013, although MLR consistently performs better than CMAR, the improvements achieved by MLR are not statistically significant.

We conducted additional experiments on the Retail data set using rules mined at support thresholds of 0.1% and 0.3%. The relative performances of the two approaches are very similar for those experiments as well and are not reported here for brevity.

## 5. Comparisons with Collaborative Filtering and Matrix Factorization

Although rule-based recommender systems are commonly used in the retail domain (e.g., Forsblom et al. 2009) and form integral components of many commercial software packages (IBM 2009a, b; 2010), no individual system has been found to be universally better than others. In this section, we provide evidence of the broad applicability of MLR by comparing it to two state-of-the-art techniques—collaborative filtering and matrix factorization. Both approaches are widely used for providing recommendations and have been shown to perform well in general (Linden et al. 2003, Deshpande and Karypis 2004, Koren et al. 2009, Ekstrand et al. 2011). We present results from several experiments conducted on the three data sets, comparing the quality of recommendations from MLR with those generated using these approaches.

Although two approaches to collaborative filtering are popular, Jannach et al. (2011) point out that the need to handle millions of users in large e-commerce systems makes user-based collaborative filtering impractical in real-time environments. Item-based collaborative filtering, on the other hand, makes predictions based on the similarity between items. These can be computed off-line, which makes item-based collaborative filtering a viable approach for making real-time recommendations. Also, item-based collaborative filtering is designed to generate recommendations using transactional data (Linden et al. 2003). Therefore, we use item-to-item collaborative filtering in our experiments.

The Netflix Prize competition revealed that matrix factorization methods can also be very effective in making recommendations. These methods represent users and items via latent factors identified from the data, with an item being recommended to a user when the item and user are similar vis-à-vis these factors (Koren et al. 2009). A well-known matrix factorization technique for recommender systems is singular value decomposition (SVD), and one version of which, called FunkSVD, was popularized by Funk (2006). We use FunkSVD (Funk 2006) in our experiments.

We use the collaborative filtering and FunkSVD implementations provided by Ekstrand et al. (2011) in an open source project named LensKit (http://lenskit .org). As noted by the authors, LensKit provides carefully tuned implementations of these leading algorithms (all of the implementations are in Java). We note that in their experiments on three separate data sets, Ekstrand et al. (2011) find FunkSVD to perform the best on two data sets and the item-to-item collaborative filtering approach to perform the best on the third. We provide brief descriptions of the two methods below; specific details about the implementations can be found in Ekstrand et al. (2011). 15

The idea behind the item-based approach is to find items that are rated as similar to the items that have been liked by a target user. Given a data set involving m items, the item-based collaborative filtering procedure implemented by Ekstrand et al. (2011) requires two parameters as inputs—a model size (k) and a neighborhood size (l). The system computes scores for the items being considered for recommendation by multiplying an m × m similarity matrix (model) with a column vector representing the current basket of the user (the vector has a 1 for all items present in the basket and a 0 for the other items). The model size is the number of similarities retained in each column of the model; other similarities are set to 0. The neighborhood size is the number of similarities used to calculate the score of an item; other similarities are ignored. The item with the highest score is recommended.

The matrix factorization technique determines latent factors, associates each user with a user-factor vector and each item with an item-factor vector, and makes predictions using the inner product of such vectors. The parameters of the model are learned with the objective of minimizing the differences between predicted and actual ratings while avoiding overfitting (Koren et al. 2009). FunkSVD accomplishes this using a stochastic gradient descent learning algorithm.

We perform, as before, fivefold cross-validation experiments on all of the data sets. We use a support threshold of 0.2% and confidence thresholds of 30%, 40%, 50%, and 60% for MLR. We experimented with various values of model sizes (up to 500) and neighborhood sizes (up to 150) for collaborative filtering.

Although FunkSVD was originally designed for ratings of user—item pairs (like any matrix factorization technique), it has been observed to work well for binary data if all of the zero values are replaced with a small number like 0.1 (XLVector 2012). Therefore, we modify the data sets in this manner to run FunkSVD. The resulting data sets are completely dense; in fact, those corresponding to Retail and BMS-POS cannot be used in their entirety by LensKit. Therefore, for each original training data set from Retail, we randomly select 2,000 transactions for model building. We are able to use 10,000 transactions (again randomly selected) as the training data sets for BMS-POS, because this data set has many fewer items than Retail. We experimented with other numbers of randomly selected transactions for creating ratings data sets— the results do not differ significantly.<sup>16</sup> We were able to use all of the transactions in comScore2013 because the training data sets are relatively small. The modified data sets for Retail and BMP-POS have more than 10 million values for user–item pairs (the largest data set used by Ekstrand et al. (2011) has 10 million values), whereas the modified data sets for comScore2013 have more than a million user–item pairs.

In these experiments, the training data sets are used to create the models for the nonrule-based systems. The basket creation scheme is slightly different from the one described in §4. In the interest of time, the baskets are created from each transaction in the test data sets by randomly selecting half the items in the transaction—the test baskets are identical for all of the approaches. This does not affect the results significantly because we still get enough instances (baskets) to draw statistically reliable conclusions. The results presented are for those transactions for which all of the approaches generate recommendations and are averaged over all cross-validation experiments. The performance of the collaborative filtering system is not very sensitive to changes in the model and neighborhood sizes. We report the results for the experiments with model size 500 and neighborhood size 150 since the system’s performance is a little better with these settings. For FunkSVD, we use the default settings of the implementation—other settings provided similar or inferior performances. Table 12 presents the quality of recommendations provided by each approach for each data set and confidence threshold.

The relative improvements achieved by MLR over collaborative filtering are statistically significant for every experiment on each of the data sets. MLR consistently outperforms FunkSVD as well, although the improvements in the case of comScore2013 are not statistically significant. These results show that MLR is not only superior to other rule-based approaches for the data sets we have examined, but outperforms other state-of-the-art approaches for our data sets as well.

Table 12 MLR vs. Collaborative Filtering (CF) and FunkSVD

<table><tr><td rowspan="2">Data set</td><td rowspan="2">Conf. threshold (%)</td><td colspan="3">Accuracy (%)</td><td rowspan="2">Improvement over CF (%)</td><td rowspan="2">FunkSVD (%)</td></tr><tr><td>CF</td><td>FunkSVD</td><td>Improvement over MLR</td></tr><tr><td rowspan="4">Retail</td><td>30</td><td>32.90</td><td>43.91</td><td>47.27</td><td>43.65***</td><td>7.64***</td></tr><tr><td>40</td><td>33.85</td><td>45.01</td><td>48.41</td><td>43.00***</td><td>7.55***</td></tr><tr><td>50</td><td>34.42</td><td>45.44</td><td>48.87</td><td>41.98***</td><td>7.55***</td></tr><tr><td>60</td><td>36.10</td><td>47.64</td><td>52.12</td><td>44.40***</td><td>9.41***</td></tr><tr><td rowspan="4">BMS-POS</td><td>30</td><td>45.21</td><td>47.30</td><td>50.07</td><td>10.76***</td><td>5.86***</td></tr><tr><td>40</td><td>48.16</td><td>50.43</td><td>53.48</td><td>11.04***</td><td>6.05***</td></tr><tr><td>50</td><td>50.21</td><td>52.74</td><td>55.71</td><td>10.96***</td><td>5.64***</td></tr><tr><td>60</td><td>52.18</td><td>55.24</td><td>57.93</td><td>11.02***</td><td>4.86***</td></tr><tr><td rowspan="4">comScore2013</td><td>30</td><td>33.82</td><td>36.03</td><td>36.39</td><td>7.60**</td><td>0.99</td></tr><tr><td>40</td><td>35.69</td><td>38.18</td><td>38.69</td><td>8.41**</td><td>1.36</td></tr><tr><td>50</td><td>37.31</td><td>39.93</td><td>40.55</td><td>8.70**</td><td>1.56</td></tr><tr><td>60</td><td>43.33</td><td>46.22</td><td>47.11</td><td>8.73**</td><td>1.92</td></tr></table>

<sup>∗∗</sup>Significant at the 5% level or better; <sup>∗∗∗</sup>significant at the 1% level or better.

As an additional robustness check, we conducted experiments where we included in each basket all but one randomly selected item from a transaction and provided such baskets to the MLR and benchmark systems. MLR again performed significantly better than both collaborative filtering and matrix factorization in these experiments on the Retail and BMS-POS data sets. Although MLR performs better than collaborative filtering and FunkSVD on comScore2013, the improvements are not statistically significant.

## 6. Conclusions and Managerial Implications

Traditional approaches that use only a single rule for recommending items typically ignore items in the baskets of customers that may be present in the antecedents of other rules. We propose an approach— maximum likelihood recommendation—to combine multiple rules to recommend items to cover as many items in a basket as possible. Although a few methods have been proposed to combine rules, these are all ad hoc, without a robust theoretical basis. By contrast, MLR has a strong theoretical foundation—it recommends items using rules that maximize the likelihood of generating the true underlying distribution of the data set used for generating the rules. This process identifies the best set of rules to combine when estimating the probability that a customer will add a recommended item to her basket. Our approach tries to preserve as many important dependencies as possible based on the available rules (this typically leads to making as few conditional independence assumptions as possible across items in a basket).

It is not practical to solve the problem of maximizing likelihood directly, however, because it requires the estimation of parameters from the data set during run time. We show that maximizing the likelihood is equivalent to maximizing the sum of the mutual information values of the participating rules— this result makes the real-time use of this approach feasible.

We conduct extensive experiments to test the viability of the proposed approach. Comparisons are made with several traditional single-rule-based approaches, two methods that have been proposed to combine rules, and two other state-of-the-art recommendation approaches—collaborative filtering and matrix factorization. The experiments show that MLR consistently outperforms all of the other approaches, particularly when rules are available for combination. We also find that the performance improvements are robust across data sets at various support and confidence thresholds.

Although the absolute improvements may seem small at first glance, it is important to remember that recommendations are made on a continuous basis. For instance, during the holiday season in 2012, Amazon.com sold 306 items per second (Clark 2012). The 2012 annual report for Amazon.com mentions that their net sales for the fourth quarter of 2012 amounted to \$21.27 billion. If 35% of these revenues are generated from recommendations (as mentioned in Hosanagar et al. 2014), even a 1% increase in success rate would amount to an increase in revenues of approximately \$70 million every quarter. Such improvements can lead to increasing revenues by millions of dollars every year for smaller firms as well.

Several characteristics of MLR make it suitable for firms that provide personalized recommendations to their online customers. The use of probability calculus provides semantic clarity in an environment that is naturally fraught with uncertainty—at the same time, the approach is able to deliver recommendations effectively. The robust theoretical basis of MLR makes it very versatile. Because it compares alternative items to recommend based on their probabilities of purchase, it can be easily adapted to make recommendations based on expected payoffs associated with the items. This is not possible with any of the existing approaches, i.e., rule combination, collaborative filtering, or matrix factorization. The use of probability theory also allows MLR to be easily adapted to use lift-based approaches to make recommendations if needed—again this is not possible with any of the other approaches. Although we use association rules mined from historical data in our experiments, the approach can easily accommodate rules provided by human experts. Such rules may be available from marketing experts for new items that are being offered and for which transactional data are not yet available. MLR can also use association rules with negations if such rules are found to improve the quality of recommendations. MLR is computationally quite efficient, taking only a fraction of a second per recommendation on average, and furthermore, this is accomplished using a simple desktop computing environment. As a result, using MLR instead of the single-rule-based approach should not affect the quality of service during regular operation in commercial environments.

Although the results of our experiments with MLR are very encouraging, we note that the performances of different approaches can be sensitive to the application domain and data characteristics. For example, our results are consistent with those of Mobasher et al. (2001) with regard to collaborative filtering— they also found an association-rule-based approach to outperform a collaborative-filtering-based one. However, Sarwar et al. (2000) found evidence to the contrary. Similarly, FunkSVD is shown to perform better than item-based collaborative filtering on two Movie-Lens data sets, but worse on a Yahoo! Music data set (Ekstrand et al. 2011). Given the differences in performances of alternative approaches for different application domains, firms would be prudent to evaluate the different types of available approaches to identify the best one for their specific context.

Our work opens up several avenues for future research. MLR can serve as a valuable new method to consider for ensemble-based approaches because its theoretical basis is quite different (and therefore independent) from those of memory-based approaches such as collaborative filtering and matrix factorization. It would be useful to develop ways to combine MLR with other extant approaches to determine which techniques best complement each other. Another interesting opportunity is to examine how

MLR could be extended to incorporate probabilistic context-based approaches that account for item metadata, user demographics, etc. An important issue that has emerged in recent years is the extent to which a recommendation technique is vulnerable to manipulations that are often referred to as shilling attacks (Mobasher et al. 2007). It will be useful to examine in future research how robust MLR is to such attacks compared to extant techniques. Finally, it would be useful to extend recommendation query languages like REQUEST (Adomavicius et al. 2011) by incorporating a probability-based query interface that will allow end users to generate recommendations in a flexible and user-friendly manner.

## Acknowledgments

The authors would like to thank Michael Ekstrand for his considerable help in using LensKit for the experiments that involved collaborative filtering and matrix factorization techniques. The authors would also like to thank the senior editor, associate editor, and anonymous reviewers for the detailed and constructive comments and suggestions that helped improve this paper.

## References

Adomavicius G, Tuzhilin A, Zheng R (2011) REQUEST: A query language for customizing recommendations. Inform. Systems Res. 22(1):99–117.

Agrawal R, Imielinski T, Swami A (1993) Mining association rules between sets of items in large databases. Buneman P, Jajodia S, eds. Proc. ACM SIGMOD Conf. Management of Data (ACM, New York), 207–216.

Balas E, Padberg M (1976) Set partitioning: A survey. SIAM Rev. 18(4):710–760.

Baralis E, Garza P (2002) A lazy approach to pruning classification rules. Kumar V, Tsurnoto S, Zhong N, Yu PS, Wu X, eds. Proc. 2002 IEEE Internat. Conf. Data Mining (IEEE, Washington, DC), 35–42.

Baralis E, Chiusano S, Garza P (2004) On support thresholds in associative classification. Proc. 2004 ACM Sympos. Appl. Comput. (ACM, New York), 553–558.

Bayardo RJ (1998) Efficiently mining long patterns from databases. Tiwari A, Franklin M, eds. Proc. 1998 ACM-SIGMOD Internat. Conf. Management of Data (ACM, New York), 85–93.

Bayardo RJ Jr, Agrawal R (1999) Mining the most interesting rules. Proc. Fifth ACM SIGKDD Internat. Conf. Knowledge Discovery and Data Mining (ACM, New York), 145–154.

Berry M, Linoff G (2004) Data Mining and Techniques, 2nd ed. (Wiley Computer Publishing, New York).

Brijs T (2014) Retail market basket data set. Accessed April 5, 2014, http://fimi.ua.ac.be/data/retail.pdf.

Calders T, Dexters N, Gillis JJM, Goethals B (2013) Mining frequent itemsets in a stream. Inform. Systems 39:1–23.

Clark K (2012) Amazon has best holiday season ever, selling 306 items per second. Forbes (December 27), http://www .forbes.com/sites/kellyclay/2012/12/27/amazon-has-bestholiday-season-ever-selling-306-items-per-second/.

Deshpande M, Karypis G (2004) Item-based top N recommendation algorithms. ACM Trans. Inform. Systems 22(4):143–177.

Domingos P, Pazzani M (1997) On the optimality of the simple Bayesian classifier under zero-one loss. Machine Learn. 29(2–3): 103–130.

Ekstrand MD, Ludwig M, Konstan JA, Riedl JT (2011) Rethinking the recommender research ecosystem: Reproducibility, openness, and LensKit. Proc. Fifth ACM Conf. Recommender Systems (ACM, New York), 133–140.

Ergun O, Kuyzu G, Savelsbergh M (2007) Reducing truckload transportation costs through collaboration. Transportation Sci. 41(2):206–221.

Forsblom A, Nurmi P, Floreen P, Peltonen P, Saarikko P (2009) Massive—An intelligent shopping assistant. Proc. Workshop on Personalization in Mobile and Pervasive Comput., Trento, Italy.

Funk S (2006) Netflix update: Try this at home. Accessed June 20, 2012, http://sifter.org/∼simon/journal/20061211.html.

Goh DH, Ang RP (2007) An introduction to association rule mining: An application in counseling and help-seeking behavior of adolescents. Behav. Res. Methods 39(2):259–266.

Gordon L (2008) Leading Practices in Market Basket Analysis. How top retailers are using market basket analysis to win margin and market share. (FactPoint Group, Los Altos, CA).

Han J, Kamber M, Pei J (2012) Data Mining2 Concepts and Techniques, 3rd ed. (Morgan Kaufmann, San Francisco).

Hanson W (2000) Principles of Internet Marketing (South-Western College Publishing, Cincinnati).

Hastie T, Tibshirani R, Friedman J (2009) The elements of statistical learning. Data Mining, Inference and Prediction, 2nd ed. (Springer, New York).

Häubl G, Trifts V (2000) Consumer decision making in online shopping environments: The effects of interactive decision aids. Marketing Sci. 19(1):4–21.

Hosanagar K, Fleder DM, Lee D, Buja A (2014) Will the global village fracture into tribes: Recommender systems and their effects on consumers. Management Sci. 60(4):805–823.

IBM (2009a) IBM SPSS retail market basket analysis. Accessed April 11, 2012, ftp://service.boulder.ibm.com/software/uk/ data/ibm-spss-retail-datasheet.pdf.

IBM (2009b) Retail market basket analysis. Accessed April 11, 2012, https://www-304.ibm.com/easyaccess/fileserve/?contentid =193973.

IBM (2010) Predictive analytics for retail market basket analysis. Accessed April 11, 2012, ftp://public.dhe.ibm.com/common/ ssi/ecm/en/yts03013gben/YTS03013GBEN.PDF.

Jannach D, Zanker M, Felfernig A, Friedrich G (2011) Recommender Systems2 An Introduction (Cambridge University Press, Cambridge, UK), 31–35.

Koren Y, Bell R, Volinsky C (2009) Matrix factorization techniques for recommender systems. IEEE Comput. 42(8):30–37.

Kullback S (1959) Information Theory and Statistics (Wiley, New York).

Lewin BA (2009) Beyond the grocery and retail store: Applying market basket analysis to the service industry. White paper, 1010Data. http://bartlewin.com/resources/marketbasketanaly sisfortheserviceindustries.pdf.

Li W, Han J, Pei J (2001) CMAR: Accurate and efficient classification based on multiple class-association rules. Cercone N, Lin TY, Wu X, eds. Proc. IEEE Internat. Conf. Data Mining (IEEE, Washington, DC), 369–376.

Lin W, Alvarez SA, Ruiz C (2002) Efficient adaptive-support association rule mining for recommender systems. Data Mining Knowledge Discovery 6(1):83–105.

Linden G, Smith B, York J (2003) Amazon.com recommendations: Item-to-item collaborative filtering. IEEE Internet Comput. 7(1):76–80.

Liu B, Ma Y, Wong CK (2003) Scoring the data using association rules. Appl. Intelligence 18:119–135.

Liu Y, Hsu P (2005) A new approach to generate frequent patterns from enterprise databases. Singh S, Singh M, Apte C,

Perner P, eds. Third Internat. Conf. Adv. Pattern Recognition ICAPR (Springer-Verlag, Berlin Heidelberg), 371–380.

Mobasher B, Burke R, Bhaumik R, Williams C (2007) Towards trustworthy recommender systems: An analysis of attack models and algorithm robustness. ACM Trans. Internet Tech. 7(4):23–38.

Mobasher B, Dai H, Luo T, Nakagawa M (2001) Effective personalization based on association rule discovery from Web usage data. Proc. 3rd Internat. Workshop on Web Inform. Data Management (ACM, New York), 9–15.

Ng RT, Lakshmanan LVS, Han J, Pang A (1998) Exploratory mining and pruning optimizations of constrained associations rules. Tiwari A, Franklin M, eds. Proc. 1998 ACM SIGMOD Internat. Conf. Management of Data (ACM, New York), 13–24.

Pathak B, Garfinkel R, Gopal R, Venkatesan R, Yin F (2010) Empirical analysis of the impact of recommender systems on sales. J. Management Inform. Systems 27(2):159–188.

Sarwar B, Karypis G, Konstan J, Riedl J (2000) Analysis of recommendation algorithms for e-commerce. EC’00, Minneapolis (ACM, New York), 158–167.

Schiaffino S, Amandi A (2006) Personalizing user-agent interaction. Knowledge-Based Systems 19(1):43–49.

Shmueli G, Patel NR, Bruce PC (2010) Data Mining for Business Intelligence, 2nd ed. (John Wiley and Sons, Hoboken, NJ).

Su X, Khoshgoftaar TM (2009) A survey of collaborative filtering techniques. Adv. Artificial Intelligence 2009:1–19.

Tam KY, Ho SY (2003) Web personalization: Is it effective? IT Professional 5(5):53–57.

Thabtah FA (2007) A review of associative classification mining. Knowledge Engrg. Rev. 22(1):37–65.

Wang FH, Shao HM (2004) Effective personalized recommendation based on time-framed navigation clustering and association mining. Expert Systems Appl. 27(3):365–377.

Watanabe S (1960) Information theoretical analysis of multivariate correlation. IBM J. Res. Development 4(1):66–82.

Webb GI (2000) Efficient search for association rules. Proc. Sixth ACM SIGKDD Internat. Conf. Knowledge Discovery and Data Mining (ACM, New York), 99–107.

Webb GI (2008) Layered critical values: A powerful directadjustment approach to discovering significant patterns. Machine Learn. 71(2–3):307–323.

Webb GI (2010) Self-sufficient itemsets: An approach to screening potentially interesting associations between items. Trans. Knowledge Discovery Data 4(1):3–20.

Webb GI, Zhang S (2005) k-optimal rule discovery. Data Mining Knowledge Discovery 10(1):39–79.

Wickramaratna K, Kubat M, Premaratne K (2009) Predicting missing items in shopping carts. IEEE Trans. Knowledge Data Engrg. 21(7):985–998.

Witten IH, Frank E, Hall MA (2011) Data Mining—Practical Machine Learning Tools and Techniques, 3rd ed. (Morgan Kaufmann, Burlington, MA), 123.

XLVector (2012) XLVector—Recommender system. Accessed July 7, 2012, http://xlvector.net/blog/?p= 465.

Zaïane OR (2002) Building a recommender agent for e-learning systems. Proc. Internat. Conf. Comput. Ed. (IEEE, Washington, DC), 55–59.

Zaki MJ (2000) Generating nonredundant association rules. Proc. Sixth ACM SIGKDD Internat. Conf. Knowledge Discovery and Data Mining (ACM, New York), 34–43.

Zheng Z, Kohavi R, Mason L (2001) Real world performance of association rule algorithms. Proc. 7th ACM SIGKDD Internat. Conf. Knowledge Discovery and Data Mining (ACM, New York), 401–406.

Zhou C, Cule B, Goethals B (2013) Itemset based sequence classification. Proc. Eur. Conf. Machine Learn. Principles and Practice of Knowledge Discovery in Data, 353–368.
