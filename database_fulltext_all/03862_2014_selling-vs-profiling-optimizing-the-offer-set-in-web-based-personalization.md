---
otero_id: 3862
otero_key: "FZGHN63D"
title: "Selling vs. Profiling: Optimizing the Offer Set in Web-Based Personalization"
authors: "Monica Johar; Vijay Mookerjee; Sumit Sarkar"
year: "2014"
journal: "Information Systems Research"
doi: "10.1287/isre.2014.0518"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/FZGHN63D/fulltext/images/f9e5d0d61df93afe0d71482c5f9523b52cae53584b4b63377edbad0ecb505120.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Selling vs. Profiling: Optimizing the Offer Set in Web-Based Personalization

Monica Johar, Vijay Mookerjee, Sumit Sarkar

To cite this article:

Monica Johar, Vijay Mookerjee, Sumit Sarkar (2014) Selling vs. Profiling: Optimizing the Offer Set in Web-Based Personalization. Information Systems Research 25(2):285-306. http://dx.doi.org/10.1287/isre.2014.0518

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2014, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/FZGHN63D/fulltext/images/4fc1453a34e8d32a440d3cab6ec77b4dfb596fe044f5d65b377f3cd11f87870d.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Selling vs. Profiling: Optimizing the Offer Set in Web-Based Personalization

Monica Johar

Belk College of Business, University of North Carolina at Charlotte, Charlotte, North Carolina 28223, msjohar@uncc.edu

Vijay Mookerjee, Sumit Sarkar

Naveen Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080 {vijaym@utdallas.edu, sumit@utdallas.edu}

W<sup>e</sup> <sup>study</sup> <sup>the</sup> <sup>problem</sup> <sup>of</sup> <sup>optimally</sup> <sup>choosing</sup> <sup>the</sup> <sup>composition</sup> <sup>of</sup> <sup>the</sup> <sup>offer</sup> <sup>set</sup> <sup>for</sup> <sup>firms</sup> <sup>engaging</sup> <sup>in</sup> <sup>web-based</sup> personalization. A firm can offer items or links that are targeted for immediate sales based on what is already known about a customer’s profile. Alternatively, the firm can offer items directed at learning a customer’s preferences. This, in turn, can help the firm make improved recommendations for the remainder of the engagement period with the customer. An important decision problem faced by a profit maximizing firm is what proportion of the offer set should be targeted toward immediate sales and what proportion toward learning the customer’s profile. We study the problem as an optimal control model, and characterize the solution. Our findings can help firms decide how to vary the size and composition of the offer set during the course of a customer’s engagement period with the firm. The benefits of the proposed approach are illustrated for different patterns of engagement, including the length of the engagement period, uncertainty in the length of the period, and the frequency of the customer’s visits to the firm. We also study the scenario where the firm optimizes the size of the offer set during the planning horizon. One of the most important insights of this study is that frequent visits to the firm’s website are extremely important for an e-tailing firm even though the customer may not always buy products during these visits.

Keywords: web-based personalization; electronic retailing; optimal control

History: Ram Gopal, Senior Editor; Xue Bai, Associate Editor. This paper was received on May 16, 2013, and was with the authors 3 months for 1 revision. Published online in Articles in Advance May 8, 2014.

## 1. Introduction

The use of customer information to deliver a targeted solution is known as personalization or one-to-one marketing (Peppers and Rogers 1997). A popular webbased personalization approach is to use recommendation systems that make product suggestions to a customer based on prior interactions with the firm (Tam and Ho 2005). For example, Amazon.com uses several diverse techniques like collaborative filtering and association rule mining to recommend books and gifts to their customers, while YesMail.com specializes in sending personalized emails.

Personalization has become important in web-based applications for a variety of reasons (Haubl and Trifts 2000, Ansari and Mela 2003, Murthi and Sarkar 2003). First, it can be an important source of product differentiation. Second, firms can add value by providing appropriate information to simplify the customer’s buying process. Third, the drastic reduction in the costs of information technology coupled with advancements in database technologies has significantly changed the economics of collection, storage, and processing of data about customers. The low cost of personalization substantially enhances the ability of firms to deliver customized products.

Personalization consists of two important activities— learning and matching (Mobasher et al. 2001). Learning involves collecting data from a customer’s interactions with the firm and then making inferences from the data about the customer’s profile. For instance, the relevant profile for a customer may be her membership in one of several possible demographic or psychographic segments, based on age, gender, geographical region, income, political beliefs, etc. (Montgomery et al. 2001, Wall Street Journal October 17, 2007). Matching is the process of making a set of recommendations (referred to as the offer set) based on what has been learned about the customer’s profile. The items in the offer set are a set of alternatives (e.g., products, services, or links) that are presented to the customer for a possible response (e.g., purchase, click, etc.). To be effective, matching technologies require a reliable profile of their customers. One measure of the reliability of the profile could, for instance, be the degree of certainty regarding the segment to which a customer might belong. The reliability of a profile often improves as more data is collected over the period for which the firm engages with the customer.

## 1.1. Matching Goals: Selling vs. Profiling

The focus of this study is on an allocation problem that arises in the matching component of personalization. Matching can be done with the goal of selling or profiling. When matching is selling oriented, recommendations are made to maximize sales. There is a considerable amount of recent work on optimizing the composition of the offer set with a view to maximize sales (Breese et al. 1998, Zaiane 2002, Huang et al. 2004, Bodapati 2008). Commonly used techniques for salesoriented matching include collaborative filtering and rule-based systems (Adomavicius and Tuzhilin 2005, Sandvig et al. 2007). In these studies, recommendations are made to generate immediate sales. In general, however, a trade-off could be made between matching for immediate sales versus matching for future sales. To balance these goals, several studies have suggested the use of a diversity measure that is designed to give appropriate consideration to future sales (Konstan et al. 2006, Shani et al. 2005, Kitts et al. 2000).

When matching is aimed at profiling, the products in the offer set are chosen so as to improve the reliability of the profile. By carefully varying the composition of the offer set, a firm can effectively profile a customer using techniques such as choice-based conjoint analysis (Louviere and Woodworth 1983), Hierarchical Bayes estimation techniques (Lenk et al. 1996), and the more recent adaptive conjoint techniques (Toubier et al. 2004, Abernethy et al. 2008). When matching is performed with a view to improve the reliability of the profile, it can be termed as active profiling. In active profiling, the customer is presented with an offer set that is deliberately chosen to provide more information for inferring profile attribute values. For instance, some sites randomly show new articles to readers to gather more information about them (Linden 2008). On the other hand, when profiling is passive, the profile is built using exogenous data. Active profiling can be faster because it seeks to collect data that is specifically targeted to improve the profile.

## 1.2. Personalization in Online Environments

An important (and often unique) characteristic of online environments is that personalization activities can be both dynamic and active. In traditional brick-andmortar environments, the profiling activity is usually conducted first, followed by matching that leads to specific recommendations. This sequential process could apply to online environments as well, where a profile may be explicitly obtained through registration forms or surveys, before the customer can gain access to the site (Miller et al. 2001). However, in online environments, interactions between the consumer and the firm can be explicitly observed and recorded. For example, using click-stream analysis, a profile is learned by tracking the customer’s behavior at the website where each link clicked or product purchased, represents a choice made (from a set of alternatives provided) by the customer. Thus profiling can be both dynamic and programmed, i.e., it is possible for a firm to continuously revise the profile based on a customer’s click-stream data (Padmanabhan et al. 2001).

In addition to being dynamic in nature, in online environments, profiling can also be active. That is, rather than passively learning from exogenous events, the data needed to better learn a profile can be collected using a series of carefully designed experiments. However, the ultimate goal of learning a profile is to improve sales (or some other goal such as customer satisfaction), i.e., learning is ultimately a means to an end. Thus the interactive and dynamic nature of webbased commerce requires a firm to achieve a balance between learning the profile versus immediate sales, with the ultimate objective of improving total sales over a planning horizon.

Another important consideration in online retail situations is that the size of the offer set is constrained by the available space on the device where the recommendations are being displayed as well as by the cognitive limitations of customers. Thus, within the space available for the offer set, the firm needs to decide what proportion of this set should be targeted toward making an immediate sale; the remaining proportion would be targeted toward learning the customer’s profile. In the offer set, the choice of the first partition of items can be based on the current knowledge of the user’s preferences to generate immediate sales (the selling set). The second part of the offer set can be composed of items that are directed toward improving the profile (the learning set). Note that the firm can learn the profile actively from the customer’s responses to the items in the learning set, or passively (typically to a lesser extent) by observing responses to the items in the selling set.

Prior research has considered the trade-off between exploring a consumer’s profile versus exploitation of the known profile in specific personalization contexts. However, the research questions addressed in all of these works are different from ours. Balabanovic et al. (1998) examine the effect of this trade-off on the ability to learn user profiles for a document recommendation system—thereafter, they propose that the user should be left in control to choose the appropriate balance between learning and matching. Sutton (1990) and Sia et al. (2007) consider, in addition to the expected utility of an item, an exploration bonus associated with the item when determining its ranking score. The formula to calculate the exploration bonus is exogenously specified and fixed over time.

The work by Wei et al. (2005) is perhaps the most closely related to ours. They adopt a Q-learning framework (using reinforcement learning) to determine the order in which specific items should be recommended to learn a user’s interest quickly while still maximizing the firm’s revenue. Their technique uses reinforcement learning to accurately learn the selling reward of an item over time. Items to be recommended are selected using a stochastic process where the selection probability of an item increases with its selling reward. The emphasis on exploration is implicitly controlled by a single parameter; as the value of this parameter increases, the selling reward of an item has less influence on its probability of being selected. The emphasis on exploration is chosen experimentally and remains constant over time. The Dyna-Q architecture (Sutton 1990) presents a deterministic implementation of Q-learning where an explicit exploration bonus is associated with each action (item). In the Q-learning approaches, the overall trade-off between selling versus exploration (learning) is not optimized for a set of items over a planning horizon. While it is clear from the above-mentioned studies that the trade-off between selling and learning is an important consideration for personalization algorithms, the trade-off is often obtained in an ad hoc manner, or left in the hands of the online customer. Our research complements prior work by addressing the problem of endogenously determining the optimal trade-off in a dynamic setting for a large class of such problems.

The problem we study has conceptual similarities with the armed bandit problem (Powell 2007). Specifically, our problem is similar to a two-armed bandit problem. That is, there are two projects (selling and profile building) across which resources are to be allocated. In the two-armed bandit problem, it is typically assumed that the states of the machines are independent of one another. This is not the case in our problem because both profile building rates (through active and passive learning) depend on a common state, namely, the current profile. In our problem, we also allow the customer’s profile to diminish over time. This is referred to as the profile loss. However, there is no direct counterpart of profile loss in the two-armed bandit problem. This would be the equivalent of a feature where the states of the machines change (deteriorate) with time.

The classic two-armed bandit problem usually results in a bang-bang solution, implying that only one of the two machines is operated at any point in time. One result that is different in our study is that we find the existence of interior solutions (the proportion of the offer set directed toward selling can be strictly between zero and one). Thus, in the optimal solution for our problem, resources are simultaneously spent on both projects. In summary, while both problems essentially deal with an “exploration versus exploitation” decision-making framework, there are several important differences that arise from the problem context, leading to significant differences in the optimal solution. A detailed comparison with the two-armed bandit problem is provided in §2.5.

While the core ideas developed in this paper are directed to increase sales for an e-commerce firm, our work also applies to other situations where the “explore versus exploit” trade-off is meaningful. For example, such a trade-off also occurs in the area of Web advertising. In this area, the sale of a product is analogous to a click on an ad. To increase clicks, ad servers “recommend” appropriate ads to customers arriving at a website (or the ad publisher’s site). For a new publisher, the set of ads that are most likely to generate clicks are not known up front. To generate clicks, ad-servers employ information such as the search string (used by the visitor to land on a page in the publisher’s site), and other factors that have to do with the content being presented on a page, visitor cookie information, and so on (Mookerjee et al. 2012). An ad firm in the Boston area is currently experimenting with the ideas developed in this paper in the following way. Sometimes a new ad, more importantly an ad that is not the one most likely to generate a click, is shown to the visitor to learn more about other ads that could be useful to display on the publisher’s site. Given sparse visitor-level data, the learning aspect in the above problem is not at the level of the individual Web visitor; instead, it is more practical to learn at the level of the publisher. Nevertheless, the challenge for the ad firm is conceptually similar to the one in the selling versus profiling problem. That is, for a publisher, what proportion of ads shown to visitors should be based on maximizing the probability of a click? Alternatively, what proportion should be based on trying to learn what new ads can generate clicks?

At a higher level, our study adds to the body of research on customer lifetime value (the net present value of the long-term cash flows from a customer). Customer lifetime value studies also consider a goal measured over a period of time, rather than (myopically) optimizing an objective criterion (such as sales) at a point in time. Much of the customer lifetime value research focuses on developing models that predict customers’ probabilities of purchase in the future based on past purchase behavior (e.g., Schmittlein et al. 1987, Reinartz and Kumar 2003, Fader et al. 2005). Blattberg and Deighton (1996) and Reinartz et al. (2005) study how to allocate marketing resources across various channels to balance customer acquisition with customer retention. Venkatesan et al. (2007) provide a customer selection framework, also considering how resources could be allocated across communication channels. However, none of these studies examine how learning a customer’s profile could be affected by any of the channels. Thus the trade-off of foregoing current sales to benefit learning (and hence improving future sales) is not considered.

## 1.3. Objectives and Contributions

The main objective of this study is to optimally partition the items in the offer set between selling and learning so as to maximize total sales over a given planning horizon (or a period of engagement with the customer). If one were solving the above problem for a one-time interaction with a customer (i.e., the customer never returns), all of the items in the offer set are likely to be selling oriented. However, in a typical e-tailing scenario, a customer can be expected to have repeated interactions with the firm. Thus, at least initially, it may be beneficial to sacrifice sales in favor of learning. The other aspect of interest in our study is the pattern of the customer’s interaction. There are several aspects of the interaction that matter: (i) the length of the engagement period, (ii) the uncertainty in the length of this period, and (iii) the frequency of the customer’s visits during the engagement period. A longer or less uncertain engagement period may favor learning. However, if the visits are infrequent, the knowledge of the customer’s profile may suddenly drop between visits and diminish the value of a learned profile. Thus the nature of the customer’s interaction with the firm plays a critical role in our analyses.

Regardless of the nature of the interaction with the customer, the firm’s basic decision problem is to determine the proportion of the offer set that should be targeted toward immediate sales versus the proportion toward profiling, so as to maximize the firm’s sales over an engagement period. The optimal allocation across the two activities could potentially vary during the course of the engagement period. Also, while both activities (selling and profiling) contribute toward profile building, selling can be considered to be less effective for profile building.

We consider a model where the profiling benefit of selling-oriented items and learning-oriented items is kept general (i.e., the functional form is left unspecified). This model allows us to derive structural insights into the trade-off between selling and learning. Specifically, we find that the optimal allocation to the two activities can become constant for a certain interval of time during the planning horizon. This (general) model also allows us to isolate the impact of uncertainty in the engagement period on the optimal allocation. Our analyses reveals that uncertainty in the length of the engagement period is sometimes more important to control than improving the length of this period. We also find that while an increase in the passive learning rate leads to an increase in the emphasis on selling, an increase in the rate of profile loss may lead to a decrease in selling. We also consider an nperiod model with discontinuous profile loss between successive periods, i.e., the knowledge of the profile can drop abruptly from one period to another. In such a setting, we find as the mean OFF time between the sessions increases, the time spent by the firm in the steady state increases. Finally, we introduce a model that optimizes the size of the offer set in addition to determining the optimal investment in selling. This model is relevant when the firm wishes to dynamically control the optimal number of items to offer during the engagement period.

The rest of the paper is organized as follows. In §2, we present and analyze a general model for frequent customers. In §3, we present an n-period model for customers who are infrequent visitors to the firm’s website leading to a discontinuous loss in profile knowledge. In §4, we present a model that incorporates optimization of the offer set size, in addition to determining the optimal investment in selling. Research contributions and managerial implications for firms are discussed in §5.

2. The Offer Set Composition Problem The firm’s decision problem consists of optimally composing the offer set for a customer to maximize expected sales during an engagement period. Figure 1 illustrates an offer set with items that are chosen from two perspectives: a proportion of the items are offered with a view toward immediate sales and the remainder toward profiling. Items in both subsets of the offer set contribute, to a lesser extent, to the other goal: selling also contributes to profile building, whereas profiling also contributes to selling. From the firm’s perspective, given the total size of the offer set, it is important to balance the value of an immediate sale against the future value of a better customer profile.

We next discuss a general model for the offer set composition problem where the proportion of items directed toward sales, u4t5, can vary over time. We first analyze the problem where the duration of the engagement period is deterministic, and then consider a stochastic version of the problem. The model in this section addresses situations where customers frequently visit the firm’s website, so that changes in the profile between visits are not significant.

## 2.1. Profile Building

The knowledge the firm has at time t about a customer’s profile is referred to as the state, denoted by x4t5, normalized between 0 and $x _ { \mathrm { m a x } } .$ The firm profiles its customers based on the customer’s shopping and search behavior at the firm’s site. A customer’s profile could consist of several attributes that might be of interest to the firm (e.g., age, gender, income, location, political beliefs, etc.). The state described by $x ( t ) = x _ { \operatorname* { m a x } }$ represents perfect knowledge about a customer $\mathbf { \Omega } ^ { \prime } \mathbf { s }$ profile $( \mathrm { e . g . } ,$ senior citizen, male, middle income, Midwest, right of center, etc.), while $x ( t ) = 0$ corresponds to a default profile, used when the firm has collected no knowledge about the customer’s segment. The firm revises the profile based on how the customer responds to items included in the offer set. This includes items aimed at better learning the profile as well as items targeted for making an immediate sale.

Figure 1 The Offer Set  
![](/api/attachments/FZGHN63D/fulltext/images/01d8ddac6eb5b0c7399905fb53e12f83a6d52363869518f3e77a7a6774b2c5eb.jpg)

We denote by $f ( x )$ the rate at which the firm learns a customer’s profile from items targeted explicitly toward learning the profile. This rate would likely depend on the efficacy of the learning algorithm. In addition, the rate can be expected to depend on the current knowledge of the customer’s profile. To account for the fact that improving the profile could likely get increasingly difficult, we expect $f _ { x } ( x )$ to be negative. The learning rate accruing from items targeted toward sales (i.e., the selling portion of the offer set) is denoted by g4x5. As was true for $f ( x ) .$ , we expect $g ( x )$ to also be a function of the efficacy of the learning algorithm, and $g _ { x } ( x )$ to be negative. Both $f ( x )$ and $g ( x )$ are assumed to be strictly positive. We expect the learning algorithm to be more effective when the firm actively, rather than passively, learns a profile; therefore $f ( { \dot { x } } ) \geq g ( x ) \geq 0$ Considering the above, the firm’s knowledge of the customer’s profile increases at a rate given by $f ( { \boldsymbol { x } } ( t ) )$ $( 1 - u ( t ) ) + \bar { g } ( x ( t ) ) u ( t )$ , where u4t5 is the proportion of items at time t that are aimed at immediate sales. In practice, an intelligent active learning algorithm (Das et al. 2010, Atahan and Sarkar 2011, Rubens et al. 2011, Fang and Si 2012) would be employed to choose the best of items for the learning set. While the exact learning algorithm does not affect our model, we expect that the items in the learning set are such that offering these items to the customer would not offend her. Thus these items should not be ones that deliberately contradict the existing customer profile.

If a customer’s preferences were static over time, it would be possible to completely acquire the profile, i.e., given sufficient time x4t5 would attain a value of $x _ { \mathrm { m a x } }$ . However, it is reasonable to assume that a customer’s preferences could change over time leading to less-than-perfect knowledge about the customer’s profile. We denote by $h ( x ) > 0 ,$ , the rate (with respect to time) at which the knowledge of a customer’s profile diminishes over the engagement period. The term can be considered to be analogous to a forgetting rate term that is common to advertising models (Vidale and Wolfe 1957, Case 1979). Considering both forces, namely, profile building and changing customer preferences, the change with respect to time in the knowledge of the customer’s profile (denoted by the dot over the variable x) can be depicted by the so-called state equation shown below.

$$
\dot {x} = f (x (t)) (1 - u (t)) + g (x (t)) u (t) - h (x (t)).\tag{1}
$$

## 2.2. The Control Problem

The firm uses its knowledge of a customer’s profile to determine the offer set to present to a customer. The offer set consists of items recommended toward making a sale by matching items to what is currently known about the customer’s profile, as well as items recommended to improve the knowledge of this profile. The sales rate, q4t5, (units of items sold per unit time) given the recommendations made at time $t ,$ is assumed as below.

$$
q (t) = q _ {0} + k u (t) x (t).\tag{2}
$$

The constant $q _ { 0 }$ corresponds to the base sales rate. This is the sales rate that can be expected to occur with no intelligent strategy to sell. For example, if the firm has no knowledge of the customer’s preferences $( x ( t ) = 0 )$ all of the items recommended (those to sell and the others to learn) contribute to the sales rate at the base level $( q _ { 0 } )$ . The value of $q _ { 0 }$ can be expected to depend on the nature of the products being sold and characteristics of visitors to a site. The second term represents the increase in the sales rate when the firm has some knowledge of the profile $( x ( t ) > 0 )$ and allocates a portion of the offer set $( u ( t ) > 0 )$ toward immediate sales. The parameter k captures how effectively the matching algorithm can use the customer’s available profile to make selling-oriented recommendations. A more effective matching algorithm is better able to convert the knowledge in a customer’s profile into sales. Both the allocation of more items to the offer set (a higher value of u4t5) and a better customer profile (a higher value of x4t5) can increase the sales rate.

We write the firm’s objective as one of maximizing the total discounted sales over the engagement period, T , by determining the optimal trajectory for the control $u ( t ) .$ , which is defined as the proportion of items directed toward sales. The engagement period T is the total amount of time that the customer spends online at the firm’s site. Depending on the nature of interaction with the customer, there are several versions of the problem that we will consider. There are three important dimensions that describe the nature of the interaction during the engagement period: (i) duration length, (ii) duration uncertainty, and (iii) frequency. We begin with the simplest case of the problem that arises when the engagement period (T ) is deterministic and the interaction frequency is high.

## 2.3. Deterministic Engagement with Frequent Visits

An example from the online merchandising firm www.overstock.com can be used to motivate this version of the problem. Overstock.com offers a premium membership plan for \$19.95 per year that provides free shipping and a 5% reward on every purchase. A customer on a premium membership plan could be considered as having a deterministic engagement period of one year. The other dimension of interaction, namely, the interaction frequency, influences the value of learning the profile. When the visit frequency is sufficiently high, the duration between successive visits can be ignored and the customer can be assumed to be continuously interacting with the firm. For a given visit frequency, the validity of this assumption depends on the nature of products being recommended. For example, for fashion goods, customer preferences may change faster than what they do for general merchandise. Overall, the nature of interaction of an overstock.com customer on a premium membership plan can be represented as one with a deterministic engagement period and frequent visits. Another example is that of Amazon Prime where members pay a yearly membership of \$79 that provides them with free shipping, unlimited streaming of TV shows and movies, and free rental of Kindle books, among other benefits.

Formally, the above control problem can be expressed as shown below. Hereafter, unless for clarity, time as an implicit argument will be suppressed as is the convention in most optimal control models.

$$
\begin{array}{r l} & {\underset {u} {\max} \int_ {0} ^ {T} (k u x + q _ {0}) e ^ {- r t} d t} \\ & {\mathrm{s.t.} \dot {x} = f (x) (1 - u) + g (x) u - h (x),} \\ & {\qquad x (0) = x _ {0}, \quad 0 \leq u (t) \leq 1, \quad 0 \leq x (t) \leq x _ {\max}.} \end{array}
$$

The state of the system, namely, the firm’s current knowledge about the customer’s profile, is influenced by the control as described by the state equation that acts as a constraint to the control problem. The starting knowledge of the consumer profile is $x _ { 0 } ,$ and the ending profile $x \bar { ( T ) }$ is free, i.e., it can take on any value in the range $[ 0 , x _ { \mathrm { m a x } } ] .$ . To ensure that the value of the profile does not become negative, we require that $h ( 0 ) = 0 ,$ implying that when there is nothing known about the profile, there is also nothing to forget. On the other hand, when u is set to 0, the rate of change in the profile reaches its maximum, given by $f ( x ) - { \bar { h } } ( x )$ . Thus we require that $f ( x _ { \mathrm { m a x } } ) - h ( x _ { \mathrm { m a x } } ) = 0 ,$ , so that when the profile reaches some maximum value $( x _ { \mathrm { m a x } } )$ , no further improvement in the profile is possible.

The current value Hamiltonian for this problem is

$$
H = (k u x + q _ {0}) + \lambda (t) (f (x) (1 - u) + g (x) u - h (x)).\tag{3}
$$

The first term in Equation (3), kux + q , represents the instantaneous payoff, whereas the second term represents the future value from improving the customer’s profile. We can interpret $\lambda ( t )$ as the value of improving knowledge of the customer profile at time t. Since increasing the knowledge of the customer’s profile should improve the sales rate, we expect $\lambda ( t )$ to be positive. Note that in this formulation $\lambda ( T ) = 0$ since there is no salvage value for the profile at the end of the engagement period. We will see in §3 that this condition changes for infrequent visitors. For that scenario, the profile of a customer at the end of one interaction period may be important and could influence the starting profile at the beginning of the next interaction period.

2.3.1. Structure of Optimal Solution. Using Pontryagin’s approach (Sethi and Thompson 2000), and some further arguments concerning the optimality of the solution, we can characterize the overall structure of the optimal solution in Proposition 1 below.

<sup>Proposition</sup> <sup>1.</sup> The structure of the optimal policy for an engagement period T is

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} I & 0 \leq t <   \tau \\ \hat {u} & \tau \leq t \leq \theta \\ 1 & \theta <   t \leq T \end{array} \right. \quad w h e r e \quad I = \left\{ \begin{array}{l l} 0 & x _ {0} <   \hat {x} \\ \hat {u} & x _ {0} = \hat {x} \\ 1 & x _ {0} > \hat {x}. \end{array} \right.
$$

The details to calculate xˆ, $\hat { u } , \ \tau ,$ and  are provided in Appendix A.

<sup>Proof.</sup> Appendix A.<sup>1</sup>

Proposition 1 states that, based on initial conditions, the optimal control either begins with full selling or full learning. Next,  and  represent the points in time when the optimal control enters and exits the so-called steady state, i.e., the control is constant. In the steady-state region, a fixed proportion of the offer set is allocated to selling. Finally, after the steady-state region, the focus shifts completely on selling.

At the start of the engagement period, the optimal solution depends on the initial value of the customer’s profile. If the firm already possesses sufficient knowledge about the profile (the initial value of the profile is greater than the steady-state value of the profile), it is better for the firm to start with full selling. On the other hand, when the initial value of the profile is less than the steady-state value, the firm should start by investing entirely in learning. In both of the above cases, when the profile value reaches the steady-state value, an interior equilibrium is struck between learning and selling. After the steady-state period, when the end of the engagement period is imminent $( \theta < t \leq T ) .$ the firm has no incentive to learn and concentrates entirely on selling.

Two useful results follow from Proposition 1.

<sup>Corollary</sup> <sup>1.</sup> Near the end of the engagement period, the firm always finds it optimal to completely direct recommendations toward sales.

<sup>Proof.</sup> Appendix A.

Corollary 1 highlights that the primary incentive for a firm to learn arises from its ability to improve future recommendations and thereby future sales. This incentive reduces with time because there is less time left to generate sales. As a consequence, the firm should direct all its effort toward sales near the end of the engagement period.

<sup>Corollary</sup> <sup>2.</sup> Fully directing recommendations toward learning the user’s profile can only occur at the start of the engagement period.

<sup>Proof.</sup> Appendix A.

Corollary 2 states that recommendations directed purely at profile building can only occur when there is sufficient time left to exploit the knowledge of the user’s preferences. This is reasonable because unless there is enough time left to sell, learning the profile alone will not improve the firm’s total sales over the engagement period. Note that a direct consequence of Corollary 2 is that a full sell followed by full learn strategy is never optimal: if pure learning is part of the optimal policy, then it must occur before any selling (partial or pure) occurs.

2.3.2. Steady-State Solutions. Steady-state solutions are practically significant. The presence of a steady-state solution indicates that the firm can stay in dynamic equilibrium (analogous to driving a car in cruise control), balancing the objectives of learning with selling. Singular solutions are also intuitively appealing because a firm can be expected to simultaneously do some learning and some selling. Extreme solutions (full learning or full selling), on the other hand, are typically transient phenomena and are either a means to enter a steady state or arise from an end of horizon effects. For completeness, however, we provide some insights into situations where steady-state solutions do not exist. As we will observe, these situations are quite extreme.

To summarize, steady-state solutions cannot be sustained when the firm does not care much about the future or when the engagement period is relatively short. We begin with two results that provide an understanding into the forces that act against the existence of a steady-state solution.

<sup>Corollary</sup> <sup>3.</sup> As the discount rate increases, the value of the steady-state profile decreases and optimal allocation toward sales increases.

<sup>Proof.</sup> Appendix A.

High discount rates imply that the firm does not care much about the future. Corollary 3 asserts that the steady-state emphasis on learning decreases with the discount rate (r). This is reasonable since learning is useful only when it can be exploited in the future. Corollary 4 below provides one situation under which a steady-state solution can be ruled out.

<sup>Corollary</sup> <sup>4.</sup> The pure bang-bang form of the control is optimal if the discount rate is greater than a critical value.

<sup>Proof.</sup> Appendix A.

Corollary 4 identifies an extreme case: when the discount rate exceeds a certain threshold, a steady-state solution can no longer be sustained as the emphasis on learning continues to decrease. In such cases, the optimal control directly switches from pure learning to pure selling, i.e., without entering an intermediate steady-state region.

The existence of a steady-state solution can also be ruled out if there is not much difference between active and passive learning. Once again, this represents an unlikely situation because active learning is specifically targeted toward learning parts of the profile that are ambiguous. Finally, a very short engagement period also acts against the existence of a steady-state solution. Conceptually, a short engagement period should have the same effect as a high discount rate. When the discount rate is high, the firm does not care about the future and mainly emphasizes immediate sales. Similarly, a short engagement period lowers the incentive to learn since there is not enough time to convert the learned profile into sales.

Finally, in scenarios where the pure bang-bang form of the control is optimal, the firm is best served by starting with a pure learning phase (u = 0) to build the profile and then exploiting this knowledge for the rest of the engagement period $( u = 1 )$ . It should be noted that the pure bang-bang policy also allows for a special case where full selling is the optimal strategy for the entire engagement period.

## 2.4. Stochastic Engagement with Frequent Visits 2.4. Stochastic Engagement with Frequent Visits

Unlike our earlier example, we will focus here on situations where shoppers sign up for accounts where the membership is free (or its price is sufficiently low) such that the customer incurs almost no cost of disengaging with the firm. When the customer has no monetary incentive to stay with the firm for a given period, it is more appropriate to consider a stochastic engagement period (denoted by T<sup>˜</sup> ). Alternatively, stochastic engagement periods can arise from the uncertainty about customer types, viz., different customers may remain engaged for different periods of time. In other words, the randomness in engagement periods may sometimes not originate from the actions of the firm, such as a membership fee, but may be inherent to the uncertainty in consumer type.

With a stochastic engagement period, the objective function (total discounted sales over the engagement period) also becomes stochastic. Hence we need to maximize the expected value of the objective function as shown below. Let the probability density function (PDF) for the engagement period be denoted as y4t5, $t \in [ 0 , \infty ]$ . Given this distribution, the expected payoff for the firm is

$$
E [ J ] = \int_ {0} ^ {\infty} \left\{\int_ {0} ^ {t} q (\tau) e ^ {- r \tau} d \tau \right\} y (t) d t.
$$

By changing the order of integration, we have

$$
\begin{array}{c} E [ J ] = \int_ {0} ^ {\infty} q (t) e ^ {- r t} \left\{\int_ {t} ^ {\infty} y (\tau) d \tau \right\} d t \\ = \int_ {0} ^ {\infty} q (t) (1 - Y (t)) e ^ {- r t} d t. \end{array}
$$

The above expression is similar to the one in the deterministic case with an effective sales rate of $q ( t )$ times $( 1 - Y ( t ) )$ , where $Y ( t )$ is the cumulative density function of the engagement period.<sup>2</sup>

For additional insights, we have analyzed the case where the engagement period is drawn from either an exponential distribution. However, many of the insights carry over to situations where the engagement period is differently distributed: Appendix A.2.2 analyzes a case where the engagement period is uniformly distributed.

2.4.1. Exponential Engagement Period. An exponential distribution serves as a good model for the engagement period where the firm offers an unlimited free membership. As a result, the customer’s history of time spent with the firm does not provide any knowledge of the remaining period of engagement.

Formally, let the engagement period follow an exponential distribution with a mean of $1 / \nu .$ . Given this distribution, the modified control problem can be expressed as

$$
\begin{array}{l} \max _ {u} E [ J ] = \max _ {u} \int_ {0} ^ {\infty} (k u x + q _ {0}) e ^ {- (r + v) t} d t \\ \text {s.t.} \dot {x} = f (x) (1 - u) + g (x) u - h (x), \\ x (0) = x _ {0}, \quad 0 \leq u (t) \leq 1, \quad 0 \leq x (t) \leq x _ {\max}. \end{array}
$$

The objective function above easily lends itself to the current value Hamiltonian formulation, where $( r + \nu )$ can be interpreted as the effective discounting factor. The current value Hamiltonian for this problem is identical to Equation (3). Since the Hamiltonian is linear in the control variable, it suggests a bang-bang (u is 0 or 1) plus singular form for the optimal control. The singular region can be characterized by a steadystate (interior) solution. When the steady-state region is feasible, the optimal solution can be described as shown in Proposition 2.

<sup>Proposition</sup> <sup>2.</sup> The structure of the optimal policy for an exponentially distributed engagement period is

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} I & 0 \leq t <   \omega \\ \hat {u} & t \geq \omega \end{array} \right. \quad w h e r e \quad I = \left\{ \begin{array}{l l} 0 & x _ {0} <   \hat {x} \\ 1 & x _ {0} > \hat {x} \\ \hat {u} & x _ {0} = \hat {x}. \end{array} \right.
$$

The details to calculate ${ \hat { x } } , \ { \hat { u } } ,$ and  are provided in Appendix A.

<sup>Proof.</sup> Appendix A.

The choice of the control at the beginning of the engagement period has the same intuition as that for the deterministic case. That is, depending on initial conditions, it is optimal to focus entirely on either selling or learning. However, unlike the deterministic case, once the system reaches a steady state (at time ), it persists forever in this state. This is because when the engagement period is exponentially distributed, the firm’s expectation of the time remaining in the engagement does not change with time. Thus the firm finds it optimal to hold the steady state forever. Next, we present a result on the impact of the mean of the engagement period of a firm’s incentive to learn.

<sup>Corollary</sup> <sup>5.</sup> The allocation to learning during steady state increases with the mean of the engagement period.

<sup>Proof.</sup> Appendix A.

Recall that a firm will invest in learning a customer’s profile if it can match this improved profile when making recommendations for sales later. Small engagement periods provide less incentive for learning. Thus, in Corollary ${ \bar { 5 , } }$ we find that as the mean engagement period $( 1 / \nu )$ increases, the firm has an increased incentive to learn the customer’s profile (uˆ decreases, xˆ increases), since the future benefits of better matched recommendations can be expected to last longer.

2.4.2. Impact of Uncertainty. The exponential model of the engagement period enables us to evaluate how the firm’s policy is affected by the uncertainty about the customer’s engagement period. Particularly, we contrast the allocation to learning in the singular region across the two versions of the problem.

<sup>Proposition</sup> <sup>3.</sup> When the length of a deterministic engagement period is equal to the expected length of a stochastic engagement period (exponentially distributed), the allocation to learning is higher when the engagement period is deterministic, rather than stochastic.

## <sup>Proof.</sup> Appendix A.

The insight offered in Proposition 3 is that, in the face of any uncertainty in the engagement period, the firm finds it optimal to decrease the learning effort in the singular region. The intuition is that in the deterministic case, the firm precisely knows how long the learned profile can be used, and can determine the optimal mix of passive and active learning. However, any uncertainty associated with the duration of the engagement period decreases the firm’s incentive to learn, since there is a possibility that the customer may exit the system at any time. As a result, the steady-state allocation toward learning is lower in the stochastic case as compared to the deterministic case.

2.5. Comparison with Two-Armed Bandit Problem It is instructive to compare our problem with the twoarmed bandit problem. Two restrictions are applied to reduce our problem to the two-armed bandit problem. First, the learning functions (f and g) are set to be independent of the current profile, specifically these functions are set to be constants $\bar { f }$ and ${ \overline { { g } } } ,$ respectively. Second, unlike our problem where the customer’s changing preferences can cause the profile to deteriorate with time, we do not allow our stock of knowledge (represented by the variable $x ( t ) )$ to deplete over time. Hence we set $h ( x ) = 0$ . With these restrictions, the reduced problem (the two-armed bandit problem) is presented as follows:

$$
\begin{array}{l} \max _ {u} \int_ {0} ^ {T} (k u x + q _ {0}) e ^ {- r t} d t \\ \text {s.t.} \dot {x} = \bar {f} (1 - u) + \bar {g} u, \\ x (0) = x _ {0}, \quad 0 \leq u (t) \leq 1, \quad 0 \leq x (t) \leq x _ {\max}. \end{array}
$$

Our analysis shows that in the classic two-armed bandit problem, the optimal control is always bang-bang, i.e., an interior control is never optimal. To show this, we study the behavior of $H _ { u } ,$ the partial derivative of the Hamiltonian with respect to the control.

2.5.1. Study of $H _ { u }$ . For an interior control to be optimal, we must have $H _ { u } = 0$ . In addition, for this condition to sustain for any (nonzero) length of time, the derivative of $H _ { u }$ with respect to time must also be zero. Thus for the possibility of an interior control, we require that

$$
\begin{array}{r l} & H _ {u} = k x - \lambda (\bar {f} - \bar {g}) = 0, \\ & \dot {H} _ {u} = k \dot {x} - \dot {\lambda} (\bar {f} - \bar {g}) = 0. \end{array}
$$

Now, we know that $\dot { \lambda } = r \lambda - H _ { x } = - k u + r \lambda$ . Substituting, we get $\dot { H } _ { u } = k \bar { f } - k x r = 0$ . For $\dot { H _ { u } }$ to be zero, we must have a constant value of x in the interior region, implying that x˙ must be zero. However, for x˙ to be zero, we must have $u = \bar { f } / ( \bar { f } - \bar { g } )$ , which is infeasible because this ratio is greater than one. Thus we can rule out the possibility of an interior control, implying that only a bang-bang control can be optimal for this reduced problem. It can be shown that this distinction also holds with a stochastic planning horizon.

The essential argument made above can be summarized as follows. In our problem, the fact that the profile improvement functions (f and $g )$ are state dependent and that customer preferences could change over time, creates the possibility of an interior control where both selling and personalization are simultaneously pursued. Such a control can be ruled out for the two-armed bandit problem.

## 3. A Model with Discontinuous Profile Loss

An important aspect of the model formulation thus far has been that we only considered customers that frequently interacted with the firm. For frequent visitors, the time spent between visits is small enough that it can be ignored. However, this assumption is challenged for infrequent customers. Specifically, in (1), we consider time to be a continuous variable and ignore periods when the customer is not interacting at the firm’s website. Essentially, changes in the state variable are ignored when the customer is offline, i.e., not interacting with the firm. This assumption is a reasonable approximation if the customer frequently visits the website, e.g., daily or weekly, and the offline periods are not too long. For an infrequent engagement pattern, however, the profile can be discontinuous and can drop suddenly between visits. Video games that are not subscription based, fashion, cellular handsets, etc., are all examples of such rapid obsolescence situations where customer preferences could change rapidly with time.

A customer can be thought of as being in an “ON” state in a period of engagement where the time between visits is short enough that there is no appreciable change in the profile between visits. Between two periods of frequent engagement (i.e., between two successive ON states), a customer could exist in an OFF state where the customer does not visit the firm for a sufficiently long period. The models we have considered so far have consisted of customers who are always in an ON state. In this section, we will present a model where a customer is in an ON state for a certain (deterministic) period of time, but moves to an OFF state for a random period of time. Specifically, to study the effects of a discontinuous loss in the profile, we consider customers with the pattern: ON followed by OFF, followed by ON, and so on. Note that rapid obsolescence scenarios outlined above support this setup of returning customers, viz., multiple engagement (ON) periods followed by OFF periods. Intuitively, we can allow for such customers by suitably adjusting the initial knowledge of the consumer profile $( x _ { 0 } ) _ { \ast }$ from one interaction period (ON period) to the next. Thus the firm’s objective for n-period problem can be generalized as

maxJ u

$$
\begin{array}{l} = E \bigg [ \int_ {0} ^ {T} V _ {1} (u (t), x (t), x (0)) e ^ {- r t} d t \\ \qquad + \int_ {T + s _ {1}} ^ {2 T + s _ {1}} V _ {2} (u (t), x (t), x _ {1} (T)) e ^ {- r t} d t \\ \qquad + \int_ {2 T + s _ {1} + s _ {2}} ^ {3 T + s _ {1} + s _ {2}} V _ {3} (u (t), x (t), x _ {2} (2 T + s _ {1})) e ^ {- r t} d t \\ \qquad + \dots + \int_ {s _ {1} + s _ {2} + \dots + s _ {n - 1} + (n - 1) T} ^ {s _ {1} + s _ {2} + \dots + s _ {n - 1} + n T} V _ {n} (u (t), x (t), \\ \qquad X _ {n - 1} (s _ {1} + s _ {2} + \dots + s _ {n - 2} + (n - 1) T)) e ^ {- r t} d t \bigg ], \end{array}\tag{4}
$$

where $V _ { i }$ is the instantaneous value function associated with the ON period i.

The value function in any period not only depends on state and control during the period, but also on the ending state of the previous period. The random variable $\mathbf { \boldsymbol { s } } _ { i }$ represents the duration for which the customer does not interact with the firm (the OFF time) at the end of the ith period of interaction. Clearly, the firm accumulates no sales revenue during this duration. We assume that $\mathbf { \boldsymbol { s } } _ { i }$ are independently, exponentially distributed with a mean of $\bar { 1 } / \eta$ . The starting (random) profile at the beginning of the (i + 1)th period is assumed to be given by $e ^ { - \rho s _ { i } }$ times the ending profile of the ith period, where $\rho$ is a coefficient that affects the magnitude of profile loss during the OFF time. A high value of this coefficient corresponds to a case where the customer preferences could change rapidly with time.

We focus on problems with the property that the optimal solution includes a steady-state component in any period. A condition on the parameters of the problem is imposed to ensure such a property. A direct implication of this property is the following: while the starting profile for a given period is a random variable, the ending profile is not. We state this result in the lemma below.

<sup>Lemma</sup> <sup>1.</sup> The ending profile in any interaction period is independent of the starting profile if steady state was achieved in the period.

<sup>Proof.</sup> Refer to Appendix B.

To solve the problem, we introduce a value (to all future periods) associated with the ending profile of a period. The value of the ending profile in a period can be interpreted as a salvage value. However, using the result asserted in the above lemma, the ending profile does not impact the value in the rest of the planning horizon; rather its effect is limited to only the next period. Thus the firm only needs to consider the benefits from the next visit by the customer. Using this property, the structure of the optimal policy for an n-period model is characterized below.

<sup>Proposition</sup> <sup>4.</sup> Assuming that the length of each interaction period (ON state) is sufficiently large $( \dot { T } > T _ { c } )$ , the optimal solution for the n-period problem is of the form

<table><tr><td>Period 1</td><td>Period 2,3,...,n</td></tr><tr><td>0 -ˆu-1 iff x1(0) &lt;ˆx</td><td>0 -ˆu-1</td></tr><tr><td>1 -ˆu-1 iff x1(0) &gt;ˆx</td><td></td></tr></table>

Where $T _ { c }$ is the solution of the equation,

$$
\hat {x} = \int_ {0} ^ {T _ {c}} (f (\kappa) - h (\kappa)) d \kappa .
$$

<sup>Proof.</sup> Appendix $\mathrm { B , }$ including details to calculate $\hat { x }$ and $\hat { u } .$

The critical value $\left( T _ { c } \right)$ represents the time it would take for the profile to increase from zero to the steadystate value, if full learning is employed. Interestingly, the steady-state values of the profile and the control (the values of $\hat { x }$ and uˆ) are the same in all periods, implying that the nature of the steady state for a problem with a single period $( n = 1 )$ is the same as that for a problem with multiple periods. Also, observe that the starting choice of the control is always zero for all periods except the first one. This is expected because the initial profile for any period will typically be lower than the steady-state profile. The reason for this is also clear. Because the ending profile of any period is strictly below the steady-state value (given that all periods always end with full selling), the starting profile for the next period should never be greater (even if the OFF time is zero).

The presence of the salvage value only impacts the time spent in the steady state, but not the level of the steady-state profile. That is, we still find (as in Proposition 1) that it is optimal for the firm to invest fully in sales toward the end of each interaction, but the amount of time spent in this region (after steady state) changes with the introduction of a salvage value function. We expand on this result below.

<sup>Corollary</sup> <sup>6.</sup> As the mean OFF time $( 1 / \eta )$ decreases, the time spent in steady state increases.

<sup>Proof.</sup> Refer to Appendix B.

Corollary 6 highlights that as the mean OFF time decreases, the firm should increase the emphasis on learning to obtain benefits in the future. A lower value of the mean OFF time $( 1 / \eta )$ also implies a lower profile loss between periods. This increases the salvage value associated with the ending profile, and hence increases the time spent in the steady state (when a mix of selling and learning is pursued). Even though the firm continues to invest fully in sales toward the end of the engagement period, the additional emphasis on learning is evidenced by reducing the time spent in pure selling.

## 4. Optimizing the Size of the Offer Set

Another important consideration in online retail situations (in addition to the issue of selling versus profiling) is the size of the offer set. The offer set size is often constrained by the available space on the device where the recommendations are being displayed as well as by the cognitive limitations of customers. Considerations about the size of the offer set relates to the research on retail assortment problems with limited shelf space (Caro and Gallien 2007). In the models considered so far, we assume the size of the offer set to be fixed. We now relax this requirement and develop a model to optimize the size of this set (denoted by s4t5), together with optimizing the proportion of this set that is directed toward selling (u4t5).

For the offer set size to have a meaningful impact on the problem, there should be a tension between increasing the set size and decreasing it. That is, there should be a negative and positive effect of the size of the set. We capture the negative effect of increasing the set size by considering that the ability to learn (both passive and active) decreases with the size (s). The learning functions are denoted by $g ( x , s )$ and $f ( x , s )$ , respectively. The decreased ability to learn can be expected to occur because a higher set size places a higher cognitive burden on the customer. Thus the marginal learning diminishes for each additional unit offered in the set. Taken together, these assumptions require that $\partial g / \partial s \le \partial f / \partial { \big / } s \le 0$ . The fact that passive learning is more negatively impacted than active profiling can be attributed to the fact that in active profiling items are deliberately chosen to learn. The positive effect of offer set size is accounted for by allowing the sales rate to increase with the increase in the number of items offered. Hence we formulate the firm’s objective as follows:

$$
\begin{array}{r l} \underset {u (t) s (t)} {\max} & \int_ {0} ^ {T} (k u s x + q _ {0}) e ^ {- r t} d t \\ \text {s.t.} & \dot {x} = f (x, s) (1 - u) + g (x, s) u - h (x, s) \\ & x (0) = x _ {0}, \quad 0 \leq x (t) \leq x _ {\max}, \\ & 0 \leq u (t) \leq 1, \quad 0 \leq s (t) \leq \sigma_ {\max}. \end{array}
$$

The structure of the optimal policy and key results of this model are characterized below.

<sup>Proposition</sup> <sup>5.</sup> The structure of the optimal policy for a planning horizon T is

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} I & 0 \leq t <   \tau \\ \hat {u} & \tau \leq t \leq \theta \\ 1 & \theta <   t \leq T \end{array} \right. a n d s ^ {*} (t) = \left\{ \begin{array}{l l} Y & 0 \leq t <   \tau \\ \hat {s} & \tau \leq t \leq \theta \\ \sigma_ {1} (x) & \theta <   t \leq T, \end{array} \right.
$$

$$
w h e r e I = \left\{ \begin{array}{l l} 0 & x _ {0} <   \hat {x} \\ 1 & x _ {0} > \hat {x} \end{array} \right., Y = \left\{ \begin{array}{l l} \sigma_ {0} (x) & x _ {0} <   \hat {x} \\ \sigma_ {1} (x) & x _ {0} > \hat {x}. \end{array} \right.
$$

The details to calculate $\sigma _ { 0 } , \sigma _ { 1 } , \hat { x } , \hat { u } , \hat { s } , \tau ,$ and  are provided in Appendix C.<sup>3</sup>

<sup>Proof.</sup> Refer to Appendix C.

When comparing with the basic model in Proposition 1, we find that the steady solution continues to remain optimal for the current problem. However, the values of the steady-state profile and the allocation to selling (xˆ and uˆ) are different. Some properties associated with the optimal offer set size are summarized below.

<sup>Corollary</sup> <sup>7.</sup> In the region where the firm is fully invested in learning (beginning of the planning horizon when $x _ { 0 } < \hat { x } )$ , the optimal size of the offer set depends on the state variable $( s ^ { \dot { * } } = \sigma _ { 0 } ( x ) )$ , where $\partial \stackrel { . . } { f } ( x , s ) / \partial s \dot { | } _ { s = \sigma _ { 0 } } = 0 .$

<sup>Proof.</sup> Refer to Appendix C.

In the beginning, all of the items in the offer set are directed toward learning. Because the active learning rate depends on the optimal offer set size, the set size is chosen such that it maximizes the active profiling rate $( \partial f ( x , s ) / \partial s | _ { s = \sigma _ { 0 } } = 0 )$

<sup>Corollary</sup> <sup>8.</sup> The optimal size of the offer set at the end of the planning horizon is equal to its maximum value.

<sup>Proof.</sup> Refer to Appendix C.

Corollary 8 characterizes the optimal offer set size toward the end of the planning horizon when the firm is fully invested in sales $( u ^ { * } = 1 )$ . There are two compensating effects that arise from an increase in size of the offer set in this region. The positive effect is that the payoff from investing fully in sales is maximized by increasing the offer set size. Basically, in this region, the firm would like to increase the number of items it can offer to maximize the matching probability, given that user profile knowledge has been accumulated. On the other hand, increasing the offer set has the negative effect of reducing the passive learning rate. In this region, the value of learning diminishes with time, since we are approaching the end of the session. Thus the positive effect (on selling) of increasing the offer set dominates over the negative effect (on learning). This is the intuition for increasing the optimal offer set size in the region after exiting the steady state. In fact, as a continuation of this trend, we find that at the end of the planning horizon, the optimal offer set size is equal to its maximum value.

## 5. Conclusions

The models studied in this paper prescribe how a firm should divide its efforts between the future value of learning a customer’s preferences and the immediate value of selling to the customer. Learning comes at an opportunity cost, i.e., immediate revenue is foregone. However, during later interactions with the customer, improved knowledge about the customer’s preferences provides better selling opportunities.

More specifically, we ask: What combination of learning and selling should be employed, and how should the mix of learning and selling change over the engagement period? Our main finding is that always trying to sell is usually not a good long-term strategy. Learning is particularly important when a new customer arrives with little background information. Selling is more important when a customer arrives with sufficient profile information or when there is less time left to exploit the learned profile. Learning is more important when the customer profile can be learned more efficiently, or if the customer profile changes more rapidly. The pattern of interaction with the customer also has an important influence on the importance of learning. When the engagement period is more predictable or when customers visit frequently, there is more incentive to learn.

One of the most important insights of this study is that frequent visits to the firm’s website are extremely important for an e-tailing firm even though the customer may not always buy products during these visits. This arises from the fact that frequent visits help the firm stay current with the customer’s preferences. Thus the products recommended better track the changing tastes and preferences of the customer. More generally, our study reveals that firms would benefit by appropriately influencing the characteristics of the engagement with the customer. Here, the relative importance of the length of the engagement period versus its uncertainty is worthy of mention. It is not always beneficial to increase the expected length of the period if the period becomes less predictable as a result. Overall, it is important for e-tailing firms to use appropriate incentives to influence the nature of the engagement with the customer. Traditionally, however, most incentives (such as spot discounts, e-coupons, etc.) are geared toward selling. Our study indicates that similar incentives should be designed to facilitate learning. While choosing the emphasis on selling is the main theme of this paper, we studied a model where the firm could also manipulate the size of the offer set during the planning horizon. Typically, the size of the offer set was found to increase with the emphasis on selling.

Avenues for future work are numerous. The actual behavior of customers during visits can be incorporated into the decision model. Thus the learning strategy could be tailored to the actual profile learned in the course of the engagement period. The impact of learning on the profile can be considered to be stochastic. These extensions point toward a closed-loop optimal control problem. Further, learning can have more explicit costs such as the nuisance value to the customer, rather than only the lost selling opportunity.

## Appendix A.

## A.1. Deterministic Planning Horizon

<sup>Proposition</sup> <sup>1.</sup> The structure of the optimal policy for an engagement period T is

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} I & 0 \leq t <   \tau \\ \hat {u} & \tau \leq t \leq \theta \\ 1 & \theta <   t \leq T, \end{array} \right. \quad w h e r e \quad I = \left\{ \begin{array}{l l} 0 & x _ {0} <   \hat {x} \\ u ^ {s} & x _ {0} = \hat {x} \\ 1 & x _ {0} > \hat {x}. \end{array} \right.
$$

<sup>Proof.</sup> We begin by formulating the current value Hamiltonian for this problem as follows:

$$
H = k u x + q _ {0} + \lambda (f (x) (1 - u) + g (x) u - h (x)),\tag{A1}
$$

where  is the adjoint state variable

$$
\frac {\partial H}{\partial u} = k x - \lambda (f (x) - g (x)).\tag{A2}
$$

The Hamiltonian is linear in the control variable $u ,$ so that the optimal solution is given by

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} 0 & \text {iff} \phi (t) = k x - \lambda (f (x) - g (x)) <   0 \\ \text {singular} & \text {iff} \phi (t) = k x - \lambda (f (x) - g (x)) = 0 \\ 1 & \text {iff} \phi (t) = k x - \lambda (f (x) - g (x)) > 0. \end{array} \right.\tag{A3}
$$

where $\phi ( t ) = \partial H / \partial u = k x - \lambda ( f ( x ) - g ( x ) )$ is hereafter referred to as a switching function.

From Equation (A3), we know that in the singular region,

$$
\phi (t) = k x - \lambda (f (x) - g (x)) = 0, \text {   hence   } \lambda = \frac {k x}{f (x) - g (x)}.\tag{A4}
$$

Also, we know that the adjoint equation is given by (from Equation (A1))

$$
\dot {\lambda} = r \lambda - H _ {x} = - k u - \lambda \left(- r + (1 - u) \frac {\partial f}{\partial x} + u \frac {\partial g}{\partial x} - \frac {\partial h}{\partial x}\right).\tag{A5}
$$

Requiring $\dot { H } _ { u } = 0$ in the singular region and simplifying using Equations (A4) and (A5), we get

$$
\begin{array}{l} (f (x) - h (x)) \bigg (1 - \frac {x (\partial f / \partial x - \partial g / \partial x)}{f (x) - g (x)} \bigg) \\ + x \bigg (\frac {\partial f}{\partial x} - \frac {\partial h}{\partial x} - r \bigg) = 0. \end{array}\tag{A6}
$$

Note that Equation (A7) is independent of $u , \ t ,$ and therefore it is clear that steady state is attained in the singular region (x4t5 is constant), and it can be obtained by solving Equation (A6), viz.,

$$
\begin{array}{l} \hat {x} = \big [ (h (\hat {x}) - f (\hat {x})) (f (\hat {x}) - g (\hat {x})) \big ] \\ \qquad \cdot \Bigg [ (g (\hat {x}) - f (\hat {x})) \bigg (r + \frac {\partial h}{\partial x} - \frac {\partial f}{\partial x} \bigg) \\ \qquad + (f (\hat {x}) - h (\hat {x})) \bigg (\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x} \bigg) \Bigg ] ^ {- 1}. \end{array}\tag{A7}
$$

It can be shown that Equation (A7) always has a feasible solution when the steady state is feasible (refer to Property A.5)

$$
\hat {\lambda} = \frac {k f (\hat {x})}{g (\hat {x}) (\partial f / \partial x) - f (\hat {x}) (\partial g / \partial x)},\tag{A8}
$$

$$
\hat {u} = \frac {f (\hat {x}) - h (\hat {x})}{f (\hat {x}) - g (\hat {x})}.\tag{A9}
$$

LC condition for existence of singular solution in Appendix A. The LC condition can be written as

$$
\begin{array}{l} - \frac {\partial}{\partial u} \left(\frac {\partial^ {2} H _ {u}}{\partial t ^ {2}}\right) \\ = - k \underbrace {\left(\frac {\partial f}{\partial x} - \frac {\partial h}{\partial x}\right)} _ {-} \underbrace {(g - f)} _ {-} + \left(k + \lambda \left(\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x}\right)\right) \\ \cdot \underbrace {\left((f - h) \left(\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x}\right) + (g - f) \left(r + \frac {\partial h}{\partial x} - \frac {\partial f}{\partial x}\right)\right)} _ {-} - \lambda \underbrace {(g - f)} _ {-} \\ \cdot \underbrace {\left(\left(\frac {\partial^ {2} g}{\partial x ^ {2}} - \frac {\partial^ {2} f}{\partial x ^ {2}}\right) \underbrace {(f - h)} _ {+} + \underbrace {(g - f)} _ {-} \underbrace {\left(\frac {\partial^ {2} h}{\partial x ^ {2}} - \frac {\partial^ {2} f}{\partial x ^ {2}}\right)} _ {+} + r \left(\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x}\right)\right)} _ {+} \end{array}
$$

≤ 00

(A10)

Equation (A10) satisfies the LC condition, which implies that the singular solution, if it exists, is optimal so long as

(i) ${ \bar { f ( x ) } } \geq g ( x )$ . This follows since f 4x5 is the learning rate when the firm is completely invested toward exploration, while $g ( x )$ is the learning rate when the firm is completely invested toward sales.

(ii) $( \partial / \partial x ) \{ g ( x ) - f ( x ) \} > 0 , ( \partial ^ { 2 } / \partial x ^ { 2 } ) \{ g ( x ) - f ( x ) \} \le 0 .$ . We assume the negative impact of reducing investment toward explo ration $( f ( x ) - g ( x ) )$ reduces at a decreasing rate as the firm learns more about the consumer’s profile.

(iii) $( \partial / \partial x ) \{ f ( x ) - h ( x ) \} < 0 , ( \partial ^ { 2 } / \partial x ^ { 2 } ) \{ f ( x ) - h ( x ) \} \leq 0 .$ . Note that $f ( x ) - h ( x )$ is the effective learning rate when investing wholly toward exploration. We expect this learning rate to be negatively impacted as the firm learns more about a consumer at an increasing rate, $i . e . , f ( x ) - h ( x )$ is decreasing and concave.

(iv) The discount rate is less than a critical value, $r \leq r _ { c } =$ $[ ( f - g ) ( \partial ^ { 2 } h / \partial x ^ { 2 } - \partial ^ { 2 } f / \partial x ^ { 2 } ) + ( \partial ^ { 2 } f / \partial x ^ { 2 } - \partial ^ { 2 } g / \partial x ^ { 2 } ) ( f - \dot { h } ) ] /$ $( \partial g / \partial x - \partial f / \partial x )$

Next, to show the optimal structure, we establish the following properties.

<sup>Property</sup> <sup>A.1.</sup> The optimal solution cannot transition from $u ^ { * } = 1$ to $u ^ { * } = 0$

<sup>Property</sup> <sup>A.2.</sup> The optimal cannot transition from $u ^ { * } =$ singular to $u ^ { * } = 0$

<sup>Property</sup> <sup>A.3.</sup> The transition from $u ^ { * } = 0$ to $u ^ { * } = 1$ is monotonic.

<sup>Property</sup> <sup>A.4.</sup> The transition from u<sup>∗</sup> = singular to $u ^ { * } = 1$ is monotonic.

Based on Properties A.1–A.4, it follows that the optimal policy will be of the form:

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} I & 0 \leq t <   \tau \\ \hat {u} & \tau \leq t \leq \theta \\ 1 & \theta <   t \leq T, \end{array} \right. \quad \text { where } I = \left\{ \begin{array}{l l} 0 & x _ {0} <   \hat {x} \\ u ^ {s} & x _ {0} = \hat {x} \\ 1 & x _ {0} > \hat {x}. \end{array} \right.
$$

<sup>Corollary</sup> <sup>1.</sup> Near the end of the engagement period, the firm always finds it optimal to completely direct recommendations toward sales.

<sup>Proof.</sup> The corollary directly follows from the structure of the optimal policy. <sup></sup>

<sup>Corollary</sup> <sup>2.</sup> Fully directing recommendations toward learning the user’s profile can only occur at the start of the engagement period.

<sup>Proof.</sup> As seen from the structure of the optimal policy, the full learning phase cannot occur near the end or during the singular region.

<sup>Corollary</sup> <sup>3.</sup> As the discount rate increases, the value of the steady-state profile decreases and optimal allocation toward sales increases.

Proof. We have

$$
\begin{array}{l} \hat {x} = \big [ (h (\hat {x}) - f (\hat {x})) (f (\hat {x}) - g (\hat {x})) \big ] \\ \qquad \cdot \Bigg [ (g (\hat {x}) - f (\hat {x})) \bigg (r + \frac {\partial h}{\partial x} - \frac {\partial f}{\partial x} \bigg) \\ \qquad + (f (\hat {x}) - h (\hat {x})) \bigg (\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x} \bigg) \Bigg ] ^ {- 1} = Z (\hat {x}, r) \\ \qquad \frac {d \hat {x}}{d r} = \underbrace {\frac {\partial}{\partial r} Z (\hat {x} , r)} _ {-} \Bigg / \bigg (1 - \underbrace {\frac {\partial}{\partial \hat {x}} Z (\hat {x} , r)} _ {-} \bigg) \leq 0. \end{array}
$$

We have

$$
\begin{array}{c} \hat {u} = \frac {f (\hat {x}) - h (\hat {x})}{f (\hat {x}) - g (\hat {x})}, \\ \frac {d \hat {u}}{d \hat {x}} = \frac {\left(\frac {\partial f}{\partial x} - \frac {\partial h}{\partial x}\right) (f (\hat {x}) - g (\hat {x})) - \left(\frac {\partial f}{\partial x} - \frac {\partial g}{\partial x}\right) (f (\hat {x}) - h (\hat {x}))}{(f (\hat {x}) - g (\hat {x})) ^ {2}} \leq 0, \\ \frac {d \hat {u}}{d r} = \underbrace {\frac {d \hat {u}}{d \hat {x}}} _ {-} \underbrace {\frac {d \hat {x}}{d r}} _ {-} \geq 0. \quad \square \end{array}
$$

<sup>Corollary</sup> <sup>4.</sup> The pure bang-bang form of the control is optimal if the discount rate is greater than a critical value, where the critical value is given by $r _ { c } ^ { ' } = [ ( f - g ) ( \partial ^ { 2 } h / \partial x ^ { 2 } - \partial ^ { 2 } f / \partial x ^ { 2 } ) +$ $( \partial ^ { 2 } f / \partial x ^ { 2 } - \partial ^ { 2 } g / \partial x ^ { 2 } ) ( f - \check { h } ) ] / ( \partial g / \partial x - \partial f / \partial x ) .$

<sup>Proof.</sup> The proof follows from the LC condition. Note that so long as the LC condition is satisfied, the steady-state solution is optimal. Hence

$$
\underbrace {\left(\frac {\partial^ {2} g}{\partial x ^ {2}} - \frac {\partial^ {2} f}{\partial x ^ {2}}\right)} _ {-} \underbrace {(f - h)} _ {+} + \underbrace {(g - f)} _ {-} \underbrace {\left(\frac {\partial^ {2} h}{\partial x ^ {2}} - \frac {\partial^ {2} f}{\partial x ^ {2}}\right)} _ {+} + \underbrace {r \left(\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x}\right)} _ {+} > 0.
$$

Simplifying, we get the necessary condition on the discount rate. <sup></sup>

<sup>Property</sup> <sup>A.5.</sup> When the singular solution is optimal, the steady-state value (xˆ) is unique.

<sup>Proof.</sup> In the singular region, the steady-state variable is the solution of the equation

$$
\begin{array}{l} \hat {x} = \frac {(h (\hat {x}) - f (\hat {x})) (f (\hat {x}) - g (\hat {x}))}{(g (\hat {x}) - f (\hat {x})) \bigg (r + \frac {\partial h}{\partial x} - \frac {\partial f}{\partial x} \bigg) + (f (\hat {x}) - h (\hat {x})) \bigg (\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x} \bigg)} \\ = Z (\hat {x}), \end{array}
$$

i. $\mathrm { e } . , { \hat { x } } - Z ( { \hat { x } } ) = 0$ . Differentiating w.r.t. x, we can show that as long as the LC condition (A.11) is satisfied, i.e., singular region is optimal,

$$
\begin{array}{l}\frac {\partial}{\partial \hat {x}} Z (\hat {x})\\= \left[ \right. \underbrace {\left((g (\hat {x}) - f (\hat {x})) \left(r + \frac {\partial h}{\partial x} - \frac {\partial f}{\partial x}\right) + (f (\hat {x}) - h (\hat {x})) \left(\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x}\right)\right)} _ {-}\\\cdot \underbrace {\left(\left(\frac {\partial f}{\partial x} - \frac {\partial g}{\partial x}\right) (h (\hat {x}) - f (\hat {x})) + \left(\frac {\partial h}{\partial x} - \frac {\partial f}{\partial x}\right) (f (\hat {x}) - g (\hat {x}))\right)} _ {+}\\- \underbrace {(h (\hat {x}) - f (\hat {x}))} _ {-} \underbrace {(f (\hat {x}) - g (\hat {x}))} _ {+}\\\cdot \underbrace {\left(\left(\frac {\partial^ {2} g}{\partial x ^ {2}} - \frac {\partial^ {2} f}{\partial x ^ {2}}\right) (f - h) + (g - f) \left(\frac {\partial^ {2} h}{\partial x ^ {2}} - \frac {\partial^ {2} f}{\partial x ^ {2}}\right) + r \left(\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x}\right)\right)} _ {-}\\\cdot \underbrace {\left[ \underbrace {\left((g (\hat {x}) - f (\hat {x})) \left(r + \frac {\partial h}{\partial x} - \frac {\partial f}{\partial x}\right) + (f (\hat {x}) - h (\hat {x})) \left(\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x}\right)\right) ^ {2}} _ {+} \right] ^ {- 1}} _ {+}\end{array}
$$

Implies that the steady-state value $\hat { x }$ that solves the equation $\hat { x } - Z ( \hat { x } ) = 0$ is unique.

<sup>Property</sup> <sup>A.6.</sup> When the singular solution is optimal, steadystate solution is feasible iff

$$
Z (0) = \frac {- f (0) (f (0) - g (0))}{(g (0) - f (0)) (r - \partial f / \partial x) + f (0) (\partial g / \partial x - \partial f / \partial x)} > 0.
$$

<sup>Proof.</sup> We have already shown in Property A.5 that when the LC condition is satisfied, the steady-state solution is unique. Further, so long as $Z ( 0 ) > 0$ , it follows that $( x - Z ( x ) ) | _ { x = 0 } < 0$ and combining with

$$
1 - \underbrace {\frac {\partial}{\partial \hat {x}} Z (\hat {x})} _ {-} > 0,
$$

there must be some interior value $( 0 \leq \hat { x } \leq 1 )$ such that $\hat { x } - Z ( \hat { x } ) = 0 . \quad \varTheta$

## A.2. Stochastic Planning Horizon

## A.2.1. Exponentially Distributed ${ \tilde { T } } .$

<sup>Proposition</sup> <sup>2.</sup> The structure of the optimal policy for an exponentially distributed engagement period is

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} I & 0 \leq t <   \omega \\ \hat {u} & t \geq \omega , \end{array} \right. \quad w h e r e \quad I = \left\{ \begin{array}{l l} 0 & x _ {0} <   \hat {x} \\ 1 & x _ {0} > \hat {x}. \end{array} \right.
$$

<sup>Proof.</sup> The proof follows on the same lines as Proposition 1. The main difference is that there are no end-of-horizon effects. Hence, once the steady state is established, the system stays in this state forever. Further, we need to establish the following properties.

<sup>Property</sup> <sup>A.7.</sup> The optimal solution at the end of the engagement period cannot be $u ^ { * } = 0$

<sup>Property</sup> <sup>A.8.</sup> The optimal cannot transition from $u ^ { * } = 1$ to $u ^ { * } = 0$

<sup>Property</sup> <sup>A.9.</sup> The transition from $u ^ { * } = 0$ to $u ^ { * } = 1$ is monotonic.

<sup>Property</sup> <sup>A.10.</sup> The optimal solution cannot transition from $u ^ { * } =$ singular to $u ^ { * } = 1 . \square$

<sup>Corollary</sup> <sup>5.</sup> The allocation to learning during steady state increases with the mean of the engagement period.

Proof. We have

$$
\frac {\partial \hat {x}}{\partial \nu} = - \big [ \underbrace {(f (\hat {x}) - h (\hat {x}))} _ {+} \underbrace {(f (\hat {x}) - g (\hat {x})) ^ {2}} _ {+} \big ] / \underbrace {[ D ] ^ {2}} _ {-} \geq 0,
$$

where

$$
D = (g (\hat {x}) - f (\hat {x})) \left(r + \nu + \frac {\partial h}{\partial x} - \frac {\partial f}{\partial x}\right) + (f (\hat {x}) - h (\hat {x})) \left(\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x}\right).
$$

Therefore, steady-state learning (xˆ) increases as the mean duration of the engagement period $( 1 / \nu )$ increases.

In addition, we get

$$
\frac {\partial \hat {u}}{\partial \nu} = \frac {\underbrace {(f (\hat {x}) - g (\hat {x})) \left(\frac {\partial f}{\partial x} - \frac {\partial h}{\partial x}\right) - (f (\hat {x}) - h (\hat {x})) \left(\frac {\partial f}{\partial x} - \frac {\partial g}{\partial x}\right)} _ {-}}{\underbrace {(f (\hat {x}) - g (\hat {x})) ^ {2}} _ {+}}   \cdot \underbrace {\frac {\partial \hat {x}}{\partial \nu}} _ {+} \leq 0.
$$

Therefore, steady-state investment in selling (uˆ) decreases as the mean engagement period $( 1 / \nu )$ increases. <sup></sup>

A.2.2. Uniformly Distributed T<sup>˜</sup> . A uniform distribution assumption may be appropriate to use when the customer’s membership expires after a certain period. Because the membership is free (or the fee is sufficiently low), the customer could leave at any time during this period. However, unlike the case of unlimited membership, there is an upper limit on the length of the engagement period. With a uniformly distributed engagement period, the distribution of the remaining period of engagement changes with the time already spent.

Formally, let the engagement period (T<sup>˜</sup> ) follow a uniform distribution U 601 T 7<sup>¯</sup> . We observe that the Hamiltonian is still linear in the control variable, suggesting a bang-bang (either 0 or 1) form for the optimal control, plus a possible singular region. The characteristics of the optimal solution for a uniformly distributed engagement period are summarized in the following proposition.

<sup>Proposition</sup> <sup>A.2.1.</sup> The structure of the optimal policy for a uniformly distributed engagement period is

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} I & 0 \leq t <   l \\ \hat {u} (t) & t \geq l, \end{array} \right. \quad w h e r e \quad I = \left\{ \begin{array}{l l} 0 & x _ {0} <   \hat {x} (0) \\ 1 & x _ {0} > \hat {x} (0) \\ \hat {u} (t) & x _ {0} = \hat {x} (0). \end{array} \right.
$$

The details to calculate ${ \hat { x } } ( t ) , { \hat { u } } ( t )$ , and l are provided earlier.

<sup>Proof.</sup> As compared to the previous models (deterministic T and stochastic T<sup>˜</sup> with exponential distribution), here, the singular region is not steady state, but varies as the session progresses (function of t).

The structure requires the establishment of the following properties.

<sup>Property</sup> <sup>A.11.</sup> The optimal solution at the end of the engagement period cannot be $u ^ { * } = 0$

<sup>Property</sup> <sup>A.12.</sup> The optimal cannot transition from $u ^ { * } = 1$ to $u ^ { * } = 0$

<sup>Property</sup> <sup>A.13.</sup> The optimal cannot transition from $u ^ { * } =$ singular to $u ^ { * } = 0$

<sup>Property</sup> <sup>A.14.</sup> The transition from $u ^ { * } = 0 \ t o \ u ^ { * } = 1$ is monotonic. <sup></sup>

The general form of the optimal solution in Proposition A.2.1 is similar to Proposition 2. The main difference is that, unlike the previous models (deterministic or exponentially distributed engagement period), the control and state are no longer constant in the singular region. That is, steady-state solutions do not exist.

<sup>Proposition</sup> <sup>A.2.2.</sup> When the engagement period is uniformly distributed, the allocation toward learning in the singular region decreases with time.

$$
\hat {x} = \frac {\left(1 - \frac {t}{T}\right) (f (\hat {x}) - h (\hat {x}))}{\frac {1}{T} + \left(1 - \frac {t}{T}\right) \left(r - \left(\frac {\partial f}{\partial x} - \frac {\partial h}{\partial x}\right) + \frac {f (\hat {x}) - h (\hat {x})}{g (\hat {x}) - f (\hat {x})} \left(\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x}\right)\right)}.
$$

Let us define SS4x1 t5ˆ , so that $\hat { x } = S S ( \hat { x } , t )$ . Further, let us define functions, $N _ { S S } ( \hat { x } , t )$ and $D _ { S S } ( \hat { x } , t )$ to represent numerator and denominator of the above. With some algebra, it can be shown that

$$
\begin{array}{c} \frac {d \hat {x}}{d t} = \frac {\partial S S / \partial t}{1 - \partial S S / \partial \hat {x}} \quad \text {and} \quad \frac {d \hat {x}}{d t} = \underbrace {\frac {\partial S S / \partial t}{-}} _ {-} \leq 0, \\ \frac {d \hat {u}}{d t} = \underbrace {(f (\hat {x}) - g (\hat {x})) \Big (\frac {\partial f}{\partial x} - \frac {\partial h}{\partial x} \Big) - (f (\hat {x}) - h (\hat {x})) \Big (\frac {\partial f}{\partial x} - \frac {\partial g}{\partial x} \Big)} _ {-} \\ \cdot \underbrace {\frac {d \hat {x}}{d t}} _ {-} \geq 0. \quad \square \end{array}
$$

As stated in Corollary 5, the optimal learning sought by the firm in the singular region decreases as the engagement period progresses. The intuition is that, since the engagement period is uniformly distributed, the incentive for the firm to invest in learning should decrease with time. Hence, it is optimal to gradually transfer focus from learning to selling. Thus, with time, the knowledge of the profile decreases and the focus on selling increases.

## A.2.3. Comparing Optimal Policies.

<sup>Proposition</sup> <sup>3.</sup> When the length of a deterministic engagement period is equal to the expected length of a stochastic engagement period (uniformly or exponentially distributed), the allocation to learning is higher when the engagement period is deterministic, rather than stochastic.

<sup>Proof.</sup> From the earlier propositions, we already found the expression for the steady-state value of the profile. Planning horizon, T , is deterministic (refer to Equation (A8))

$$
\begin{array}{l} \hat {x} _ {\text {deterministic}} = (h (\hat {x}) - f (\hat {x})) (f (\hat {x}) - g (\hat {x})) \cdot \Big [ (g (\hat {x}) - f (\hat {x})) \\ \qquad \cdot \left(r + \frac {\partial h}{\partial x} - \frac {\partial f}{\partial x}\right) + (f (\hat {x}) - h (\hat {x})) \left(\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x}\right) \Big ] ^ {- 1}, \\ \hat {x} _ {\text {exponential}} = (h (\hat {x}) - f (\hat {x})) (f (\hat {x}) - g (\hat {x})) \cdot \Big [ (g (\hat {x}) - f (\hat {x})) \\ \qquad \cdot \left(\frac {1}{T} + r + \frac {\partial h}{\partial x} - \frac {\partial f}{\partial x}\right) + (f (\hat {x}) - h (\hat {x})) \left(\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x}\right) \Big ] ^ {- 1}, \\ \hat {x} _ {\text {uniform}} (t) = (h (\hat {x}) - f (\hat {x})) (f (\hat {x}) - g (\hat {x})) \cdot \Big [ (g (\hat {x}) - f (\hat {x})) \bigg (\frac {1}{2 T - t} \\ \qquad + r + \frac {\partial h}{\partial x} - \frac {\partial f}{\partial x} \bigg) + (f (\hat {x}) - h (\hat {x})) \bigg (\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x} \bigg) \Big ] ^ {- 1}. \end{array}
$$

It is easy to see that the deterministic profile is always higher. <sup></sup>

<sup>Proposition</sup> <sup>A.2.3.</sup> The allocation to learning during the singular region is higher for a uniformly distributed period than it is for an exponentially distributed period before the mean of the engagement period. Beyond the mean, it is lower.

<sup>Proof.</sup> From the earlier propositions, we already found the expression for the steady-state value of the profile.

$$
\begin{array}{l} \hat {x} _ {\text { exponential }} = (h (\hat {x}) - f (\hat {x})) (f (\hat {x}) - g (\hat {x})) \cdot \left[ (g (\hat {x}) - f (\hat {x})) \right. \\ \qquad \qquad \qquad \cdot \left(\frac {1}{T} + r + \frac {\partial h}{\partial x} - \frac {\partial f}{\partial x}\right) + (f (\hat {x}) - h (\hat {x})) \left(\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x}\right) \bigg ] ^ {- 1}, \\ \hat {x} _ {\text { uniform }} (t) = (h (\hat {x}) - f (\hat {x})) (f (\hat {x}) - g (\hat {x})) \cdot \left[ (g (\hat {x}) - f (\hat {x})) \right. \\ \qquad \qquad \qquad \cdot \left(\frac {1}{2 T - t} + r + \frac {\partial h}{\partial x} - \frac {\partial f}{\partial x}\right) + (f (\hat {x}) - h (\hat {x})) \left(\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x}\right) \bigg ] ^ {- 1}. \end{array}
$$

With some algebra, it can be established that $t < E [ \tilde { T } ] = T ,$ $\hat { x } _ { \mathrm { u n i f o r m } } ( t ) > \hat { x } _ { \mathrm { e x p o n e n t i a l } }$ . In contrast, for $t < E [ \tilde { T } ] = T , \hat { x } _ { \mathrm { u n i f o r m } } ( t ) <$ xˆ<sub>exponential</sub>. <sup></sup>

When the engagement period is stochastic (uniform or exponential), the relative incentive to learn depends on the expected time left in the engagement period. In the exponential case, the expected time left in the engagement period does not change $( \mathrm { i . e . }$ , it is always the mean), whereas this time monotonically decreases in the uniform case. Therefore, in the uniform case, before the mean, there is sufficient time left in the engagement period such that the firm has a greater incentive to learn. Hence the steady-state allocation to learning is higher for the uniform case. However, after the mean, the firm can expect the engagement period to end soon, and the allocation toward learning in the uniform case is steadily reduced.

## A.3. Comparative Statics—Deterministic

## Planning Horizon

We analyze how the optimal solution changes with the passive learning rate as well as the rate of profile loss. In this section, we will focus on scenarios where steady-state solutions exist.

A.3.1. Passive Learning Rate. We first examine the effect of the passive learning rate on the optimal solution in Proposition 5.

<sup>Proposition</sup> <sup>A.3.1.</sup> As the passive learning rate shifts upward, there is more emphasis on selling.

<sup>Proof.</sup> By replacing $g ( \hat { x } )  \alpha + g ( \hat { x } )$ and $\partial g / \partial x \to \partial g / \partial x .$ we get

$$
\hat {x} = \frac {(h (\hat {x}) - f (\hat {x})) (f (\hat {x}) - \alpha - g (\hat {x}))}{(\alpha + g (\hat {x}) - f (\hat {x})) \left(r + \frac {\partial h}{\partial x} - \frac {\partial f}{\partial x}\right) + (f (\hat {x}) - h (\hat {x})) \left(\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x}\right)}.
$$

Let the denominator be represented by function

$$
\begin{array}{c} D \equiv (\alpha + g (\hat {x}) - f (\hat {x})) \bigg (r + \frac {\partial h}{\partial x} - \frac {\partial f}{\partial x} \bigg) \\ + (f (\hat {x}) - h (\hat {x})) \bigg (\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x} \bigg) \leq 0. \end{array}\tag{A11}
$$

It can be shown that

$$
\frac {\partial \hat {x}}{\partial \alpha} = \frac {(f (\hat {x}) - h (\hat {x})) ^ {2}}{D ^ {2}} \underbrace {\left(\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x}\right)} _ {- \mathrm{ve}} \leq 0.\tag{A12}
$$

Similary, we can see that in this model, the steady-state investment toward selling

$$
\hat {u} = \frac {f (\hat {x}) - h (\hat {x})}{f (\hat {x}) - \alpha - g (\hat {x})}.
$$

Using the above identity, we can rewrite the steady-state learning as

$$
\hat {x} = - \frac {(f (\hat {x}) - h (\hat {x})) ^ {2}}{\hat {u} D}.
$$

It can be shown that

$$
\frac {\partial \hat {x}}{\partial \alpha} = \frac {(f (\hat {x}) - h (\hat {x})) ^ {2}}{(\hat {u} D) ^ {2}} \bigg (\frac {\partial \hat {u}}{\partial \alpha} D + \hat {u} \underbrace {\left(r + \frac {\partial h}{\partial x} - \frac {\partial f}{\partial x}\right)} _ {+ \mathrm{ve}} \bigg) \leq 0.\tag{A13}
$$

Combining Equations (A12) and (A13), it must be true that

$$
\frac {\partial \hat {u}}{\partial \alpha} D \leq 0.\tag{A14}
$$

Combining Equations (A11) and (A14), it must be true that

$$
\frac {\partial \hat {u}}{\partial \alpha} \geq 0.\tag{A15}
$$

From Equation (A12), $\partial \hat { x } / \partial \alpha \leq 0 .$ , therefore two possibilities exist:

(1) If $x _ { 0 } < \hat { x } ,$ then firm starts with $u ^ { * } = 0$ , but enters into steady state quickly as  increases (in that sense time in $u ^ { * } = 0$ decreases and $\boldsymbol { u } ^ { * } = \boldsymbol { \hat { u } }$ increases).

(2) If $\begin{array} { r } { x _ { 0 } > \hat { x } , } \end{array}$ , then firm starts with $\boldsymbol { u } ^ { * } = 1$ , and enters later into steady state (in that sense time in $u ^ { * } = 1$ increases as xˆ decreases).

Note that in either case, the emphasis on selling increases until the exit of steady state.

It can also be shown that

$$
\hat {\lambda} = \frac {h (\hat {x}) - f (\hat {x})}{D},\tag{A16}
$$

$$
\frac {\partial \hat {\lambda}}{\partial \alpha} = \frac {(f (\hat {x}) - h (\hat {x}))}{D ^ {2}} \underbrace {\left(r + \frac {\partial h}{\partial x} - \frac {\partial f}{\partial x}\right)} _ {+ \mathrm{ve}} \geq 0.\tag{A17}
$$

The time spent in $u ^ { * } = 1$ after exiting the steady-state region is determined by the time taken to reduce the adjoint variable from $\lambda ( \theta ) = \hat { \lambda }$ to $\lambda ( T ) = 0 .$ . From Equation $( \mathsf { A 1 7 } )$ , it follows that time spent outside the steady-state region increases (in that sense time in $u ^ { * } = 1$ increases while $\boldsymbol { u } ^ { * } = \boldsymbol { \hat { u } }$ decreases).

Therefore, combining Equations (A15)–(A17) emphasis on selling increases as  increases. <sup></sup>

A high passive learning rate can be interpreted as a situation where a firm has a relatively homogeneous set of items to sell so there is not much incentive to learn. For example, a specialty goods store might already cater to a highly differentiated consumer segment, leaving less room for experimentation and cross-selling across product groups. As a result, the firm may be able to learn almost as effectively from tracking consumer responses to sales recommendations as from those directed toward learning.

There are three forces that lead to the higher emphasis on selling. First, as the passive learning rate shifts upward, the allocation to selling during the steady-state period increases and the steady-state value of the profile decreases. Hence we can conclude that overall emphasis on selling in the steady state increases. Second, as the passive learning rate shifts upward, the time taken to enter steady state also increases. This can be explained as follows. Recall that steady state is achieved from the initial state either by letting the profile drift (via pure selling) or by actively increasing it (via pure learning). When pure selling is employed, a higher passive learning rate results in a slower drift in the profile, hence the time taken to reach the (same) value of the profile increases. When pure learning is employed $( \mathrm { i . e . }$ , there is no selling), the passive learning rate cannot affect the time taken to reach steady state, but the steady-state value of the profile decreases. Finally, as the passive learning rate shifts upward, the time spent after steady state also increases. Taken together, we find that an upward shift in the passive learning rate increases the emphasis on selling.

A.3.2. Profile Loss Rate. We next examine the effect of the rate of profile loss on the optimal solution.

<sup>Proposition</sup> <sup>A.3.2.</sup> The effect of an upward shift in the rate of profile loss $( h ( x ) )$ , on the steady-state solution is as follows:

(i) the steady-state value of the learning function (xˆ) decreases.

(ii) the proportion of offer set aimed at sales in the steady state (uˆ) decreases.

<sup>Proof.</sup> By replacing $h ( \hat { x } )  \beta + h ( \hat { x } )$ and $\partial h / \partial x \to \partial h / \partial x ,$ we get

$$
\begin{array}{l} \hat {x} = ((\beta + h (\hat {x}) - f (\hat {x})) (f (\hat {x}) - g (\hat {x}))) \cdot \bigg [ (g (\hat {x}) - f (\hat {x})) \\ \qquad \cdot \bigg (r + \frac {\partial h}{\partial x} - \frac {\partial f}{\partial x} \bigg) + (f (\hat {x}) - \beta - h (\hat {x}) \bigg (\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x} \bigg) \bigg ] ^ {- 1}. \end{array}\tag{A18}
$$

Let the denominator be represented by function

$$
\begin{array}{l} D \equiv (g (\hat {x}) - f (\hat {x})) \bigg (r + \frac {\partial h}{\partial x} - \frac {\partial f}{\partial x} \bigg) \\ \qquad + (f (\hat {x}) - \beta - h (\hat {x})) \bigg (\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x} \bigg) \leq 0. \end{array}\tag{A19}
$$

It can be shown that

$$
\frac {\partial \hat {x}}{\partial \beta} = - \frac {(f (\hat {x}) - g (\hat {x})) ^ {2}}{D ^ {2}} \underbrace {\left(r + \frac {\partial h}{\partial x} - \frac {\partial f}{\partial x}\right)} _ {+ \mathrm{ve}} \leq 0.\tag{A20}
$$

Similary, we can see that in this model, the steady-state investment toward selling

$$
\hat {u} = \frac {f (\hat {x}) - \beta - h (\hat {x})}{f (\hat {x}) - g (\hat {x})}.\tag{A21}
$$

Using the above identity, we can rewrite the steady-state learning as

$$
\hat {x} = - \frac {\hat {u} (f (\hat {x}) - g (\hat {x})) ^ {2}}{D}.\tag{A22}
$$

It can be shown that

$$
\frac {\partial \hat {x}}{\partial \beta} = - \frac {(f (\hat {x}) - g (\hat {x})) ^ {2}}{D ^ {2}} \bigg (\frac {\partial \hat {u}}{\partial \beta} D - \hat {u} \underbrace {\left(\frac {\partial f}{\partial x} - \frac {\partial g}{\partial x}\right)} _ {- \text {ve}} \bigg) \leq 0.\tag{A23}
$$

Combining Equations (A20) and (A23), it must be true that

$$
\frac {\partial \hat {u}}{\partial \beta} D \geq 0.\tag{A24}
$$

Combining Equations (A19) and (A24), it must be true that $\partial { \hat { u } } / \partial \beta \leq 0 .$ 

An upward shift in the rate of profile loss $( h ( x ) )$ makes learning more difficult. Therefore, as h4x5 shifts upward, the extent of the consumer knowledge being sought in the steady state decreases (xˆ decreases). On the other hand, since selling cannot be effective without adequate learning, the firm increases its investment toward learning in steady state as the rate of profile loss shifts upward.

The impact of learning efficiency on the optimal solution is more complicated. Here, we find that the emphasis on selling may increase or decrease with the learning efficiency. This effect can be easily demonstrated using a simple linear model.<sup>4</sup> Here, we find that when the learning efficiency is below a critical value $( A < A ^ { \mathrm { c r i t } } )$ , the overall emphasis on selling increases. However, after a critical value $( A > A ^ { \mathrm { c r i t } } )$ the trend reverses and the emphasis on selling decreases.

## Appendix B.

## B.1. A Model with a Discontinous Profile Loss

<sup>Proposition</sup> <sup>4.</sup> Assuming that the length of each interaction period (ON state) is sufficiently large $( T > T _ { c } )$ , the optimal solution for the n-period problem is of the form

<table><tr><td>Period 1</td><td>Period 2,3,...,n</td></tr><tr><td>0 -ˆu-1 iff x1(0) &lt;ˆx</td><td>0 -ˆu-1</td></tr><tr><td>1 -ˆu-1 iff x1(0) &gt;ˆx</td><td></td></tr></table>

<sup>Proof.</sup> The n-period problem for the firm can be generalized as

$$
\begin{array}{l} \max _ {u} J = E \left[ \int_ {0} ^ {T} V _ {1} (u (t), x (t)) e ^ {- r t} d t \right. \\ \quad + \int_ {T + s _ {1}} ^ {2 T + s _ {1}} V _ {2} (u (t), x (t), x _ {1} (T)) e ^ {- r t} d t \\ \quad + \int_ {2 T + s _ {1} + s _ {2}} ^ {3 T + s _ {1} + s _ {2}} V _ {3} (u (t), x (t), x _ {2} (2 T + s _ {1})) e ^ {- r t} d t + \dots \\ \quad + \int_ {s _ {1} + s _ {2} + \dots + s _ {n - 1} + (n - 1) T} ^ {s _ {1} + s _ {2} + \dots + s _ {n - 1} + n T} V _ {n} (u (t), x (t), \\ \quad X _ {n - 1} (s _ {1} + s _ {2} + \dots + s _ {n - 2} + (n - 1) T)) e ^ {- r t} d t \Bigg ], \end{array}\tag{B1}
$$

where $V _ { i }$ is the instantaneous value function associated with period i. In this most general form, it is a function of not only the state and control of period 4u4t5 and $x ( t ) )$ , but also on the ending state of the previous period $( x _ { i - 1 } ( T ) )$ . Note

$$
{ } ^ { 4 } \dot { x } = A ( 1 - x ) ( 1 - u ) + A ( 1 - x ) \psi u - \beta _ { 0 } x .
$$

also that $\mathbf { \boldsymbol { s } } _ { i }$ are exponentially distributed i.i.d.’s representing the OFF period between consecutive interactions (therefore the firm accumulates no payoff during this time).

Using transformation of variables, Equation (B1) can be rewritten. For example, for period $^ { 2 , }$ the transformation can be written as follows:

$$
\int_ {T + \varsigma_ {1}} ^ {2 T + \varsigma_ {1}} V _ {2} (u _ {2} (t), x _ {2} (t), x _ {1} (T)) e ^ {- r t} d t.
$$

Transformation of variables $\mu = t - ( T + \mathfrak { s } _ { 1 } )$

$$
\begin{array}{r c l} t \to T + \mathfrak {s} _ {1} & \Rightarrow & \mu \to 0, \\ t \to 2 T + \mathfrak {s} _ {1} & \Rightarrow & \mu \to T, \\ d t = d \mu & \Rightarrow & \int_ {0} ^ {T} V _ {2} (u _ {2} (\mu + T _ {1} + \mathfrak {s} _ {1}), x _ {2} (\mu + T _ {1} + \mathfrak {s} _ {1}), x _ {1} (T)) \\ & \cdot e ^ {- r (\mu + T _ {1} + \mathfrak {s} _ {1})}   d \mu . \end{array}
$$

Hence the overall objective in Equation (B1) can be rewritten as

maxJ u

$$
\begin{array}{l} \max _ {u} \\ = E \left[ \int_ {0} ^ {T} V _ {1} (u (t), x (t)) e ^ {- r t} d t \right. \\ \quad + \int_ {0} ^ {T} V _ {2} (u (t + s _ {1} + T), x (t + s _ {1} + T), x _ {1} (T)) e ^ {- r (t + s _ {1} + T)} d t \\ \quad + \int_ {0} ^ {T} V _ {3} (u (t + s _ {1} + s _ {2} + 2 T), x (t + s _ {1} + s _ {2} + 2 T), x _ {2} (T)) \\ \quad \cdot e ^ {- r (t + s _ {1} + s _ {2} + 2 T)} d t + \dots \\ \quad + \int_ {0} ^ {T} V _ {n} (u (t + s _ {1} + \dots + s _ {n - 1} + (n - 1) T), \\ \quad x (t + s _ {1} + \dots + s _ {n - 1} + (n - 1) T), x _ {n - 1} (T)) \\ \quad \cdot e ^ {- r (t + s _ {1} + s _ {2} + \dots + s _ {n - 1} + (n - 1) T)} d t \Bigg ]. \end{array}
$$

Now, instead of writing $\begin{array} { r } { ( u ( t + \sum _ { k = 1 } ^ { i - 1 } s _ { k } + ( i - 1 ) T ) } \end{array}$ and $\begin{array} { r } { x ( t + \sum _ { k = 1 } ^ { i - 1 } \pmb { \varsigma } _ { k } + ( i - 1 ) T ) } \end{array}$ for each period $i ,$ we write the control and the state in each period as $u _ { i } ( t )$ and $x _ { i } ( t ) .$ , respectively. Here, $u _ { i } ( t )$ represents the control in the period i so the argument can be normalized to lie between 0 and $T ,$ after doing appropriate discounting. Similarly, $x _ { i } ( t )$ represents the state in period i.

Therefore the overall objective can be rewritten as

$$
\begin{array}{l} \max _ {u _ {1}, u _ {2}, \dots , u _ {n}} J = E \left[ \int_ {0} ^ {T} \left(k u _ {1} (t) x _ {1} (t) + q _ {0}\right) e ^ {- r t} d t \right. \\ \quad \left. + \int_ {0} ^ {T} \left(k u _ {2} (t) x _ {2} (t) + q _ {0}\right) e ^ {- r \left(t + s _ {1} + T\right)} d t \right. \\ \quad \left. + \int_ {0} ^ {T} \left(k u _ {3} (t) x _ {3} (t) + q _ {0}\right) e ^ {- r \left(t + s _ {1} + s _ {2} + 2 T\right)} d t + \dots \right. \\ \quad \left. + \int_ {0} ^ {T} \left(k u _ {n} (t) x _ {n} (t) + q _ {0}\right) \right. \\ \quad \cdot e ^ {- r \left(t + s _ {1} + s _ {2} + \dots + s _ {n - 1} + (n - 1) T\right)} d t ], \end{array} \tag {B}\tag{B2}
$$

such that:

$$
\begin{array}{l} x _ {2} (0) = x _ {1} (T) e ^ {- \rho s _ {1}}, \\ x _ {3} (0) = x _ {2} (T) e ^ {- \rho s _ {2}}, \\ x _ {n} (0) = x _ {n - 1} (T) e ^ {- \rho s _ {n - 1}}. \end{array}
$$

We begin by establishing some useful properties.

Property B.1. <sub>As</sub> <sub>long</sub> <sub>as</sub> $T \geq T _ { i } ^ { c }$ , it is guaranteed that steady state will be achieved.

We solve the problem assuming that steady state can be achieved in any period i. The sufficient condition that ensures the existence of the steady state is derived below. The maximum time it takes for reaching steady state in period i (assuming it starts out at $x _ { 0 } = 0 )$ is given by $T _ { i } ^ { c } .$ where $T _ { i } ^ { c }$ is the solution of the following equation:

$$
\hat {x} _ {i} = \int_ {0} ^ {T _ {i} ^ {c}} (f (\kappa) - h (\kappa)) d \kappa .
$$

<sup>Property</sup> <sup>B.2.</sup> The ending learning capital in any interaction period is independent of the starting learning capital as long as steady-state region is attained.

<sup>Proof.</sup> In the general form, the objective function in any period i can be written as

$$
\max _ {u _ {i}} E \left[ e ^ {r (\sum_ {m = 1} ^ {i - 1} s _ {m} + (i - 1) T)} \int_ {0} ^ {T} \left(k u _ {i} (t) x _ {i} (t) + q _ {0}\right) e ^ {- r (t +)} d t \right] + S _ {i} \left(x _ {i} (T)\right).
$$

We denote the constant $E [ e ^ { r ( \sum _ { m = 1 } ^ { i - 1 } \mathsf { s } _ { m } + ( i - 1 ) T ) } ]$ by $M _ { i - 1 }$

Solving for the singular region, we find that the steadystate value of the control and the state is the same for every period $i , \mathrm { i } . \mathrm { e } . , \hat { x } _ { i } = \hat { x }$ and $\hat { u } _ { i } = \hat { u } _ { { \scriptscriptstyle  } }$ , which are given by

$$
\begin{array}{l} \hat {x} = (h (\hat {x}) - f (\hat {x})) (f (\hat {x}) - g (\hat {x})) \cdot \bigg [ (g (\hat {x}) - f (\hat {x})) \\ \qquad \cdot \bigg (r + \frac {\partial h}{\partial x} - \frac {\partial f}{\partial x} \bigg) + (f (\hat {x}) - h (\hat {x})) \bigg (\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x} \bigg) \bigg ] ^ {- 1}, \\ \hat {u} = \frac {f (\hat {x}) - h (\hat {x})}{f (\hat {x}) - g (\hat {x})}, \quad \text { and } \quad \hat {\lambda} = \frac {M _ {i - 1} k f (\hat {x})}{g (\hat {x}) (\partial f / \partial x) - f (\hat {x}) (\partial g / \partial x)}. \end{array}\tag{B3}
$$

When the steady state can be achieved, the expected objective function can be rewritten as

$$
\begin{array}{r l} \max _ {u _ {i}} & \Big \{M _ {i - 1} \int_ {0} ^ {\tau_ {i}} (k u _ {i} (t) x _ {i} (t) + q _ {0}) e ^ {- r t} d t \\ & + M _ {i - 1} \int_ {\tau_ {i}} ^ {\theta_ {i}} (k u _ {i} (t) x _ {i} (t) + q _ {0}) e ^ {- r t} d t \\ & + M _ {i - 1} \int_ {\theta_ {i}} ^ {T} (k u _ {i} (t) x _ {i} (t) + q _ {0}) e ^ {- r t} d t + S _ {i} (x _ {i} (T)) \Big \}, \end{array}
$$

where $\tau _ { i }$ and $\theta _ { i }$ represent the entry and exit time, respectively, associated with the steady-state region in interaction period i. Note also that $\tau _ { i }$ represents the time it takes for the state variable to reach from the starting value $x _ { i } ( 0 ) = x _ { i - 1 } ( \ ' T ) e ^ { - \rho s _ { i - 1 } }$ to the steady-state value $x _ { i } ( \tau _ { i } ) = \hat { x } .$ . On the other hand, the exit time depends on how much time it takes for the adjoint variable to go from its steady-state value $\lambda _ { i } ( \theta _ { i } ) = \hat { \lambda }$ , to its ending value as derived from the transversality condition, $\lambda _ { i } ( T _ { i } ) = \bar { S _ { x _ { i } } ( x _ { i } ( T ) ) }$ . In turn, this exit time determines the ending state value $x _ { i } ( T )$ . Based on this intuition, the following properties become clear:

(1) It is important to note that the solution in the singular region 4uˆ and x5ˆ is independent of the initial learning capital $x _ { i } ( 0 ) = x _ { i - 1 } ( T ) e ^ { - \rho s _ { i - 1 } }$ as well as the exact period index i.

(2) Only the entry time into the steady state depends on the ending state of the previous period, $i . e . , \ \tau _ { i }$ is a function of $x _ { i - 1 } ( T )$ but $\theta _ { i }$ is not.

(3) The ending state is independent of the starting state, $i . e . ,$ $x _ { i } ( T )$ depends on  and is independent of $x _ { i } ( 0 ) = x _ { i - 1 } ( T )$ . 

Using recursion, we can now rewrite the objective as

$$
\max _ {u _ {i}} J _ {i} = E \left[ \int_ {0} ^ {T} (k u _ {i} (t) x _ {i} (t) + q _ {0}) e ^ {- r (t + \sum_ {m = 1} ^ {i - 1} s _ {m} + (i - 1) T)} d t \right] + E [ J _ {i + 1} ],
$$

where

$$
\begin{array}{l} E [ J _ {i + 1} ] = E \bigg [ \int_ {0} ^ {T} (k u _ {i + 1} ^ {*} (t) x _ {i + 1} (t) + q _ {0}) e ^ {- r (t + \sum_ {m = 1} ^ {i} s _ {m} + i T)} d t \bigg ] \\ \qquad + E [ J _ {i + 2} ], \\ E [ J _ {i + 2} ] = E \bigg [ \int_ {0} ^ {T} (k u _ {i + 2} ^ {*} (t) x _ {i + 2} (t) + q _ {0}) e ^ {- r (t + \sum_ {m = 1} ^ {i + 1} s _ {m} + (i + 1) T)} d t \bigg ] \\ \qquad + E [ J _ {i + 3} ]. \end{array}\tag{B4}
$$

By using Property B.2, it is clear that in Equation (B4), only $E [ J _ { i + 1 } ]$ is a function of $x _ { i } ( T )$ , but $E [ J _ { i + 2 } ] , E [ J _ { i + 3 } ] , . . .$ 0 are not. Therefore

$$
\begin{array}{r l} S _ {i} (x _ {i} (T)) & = E [ J _ {i + 1} ] \\ & = E \bigg [ \int_ {0} ^ {T} (k u _ {i + 1} ^ {*} (t) x _ {i + 1} (t) + q _ {0}) e ^ {- r (t + \sum_ {m = 1} ^ {i} s _ {m} + i T)} d t \bigg ] \\ & = E \bigg [ \int_ {0} ^ {\tau_ {i + 1}} (k u _ {i + 1} ^ {*} (t) x _ {i + 1} (t) + q _ {0}) e ^ {- r (t + \sum_ {m = 1} ^ {i} s _ {m} + i T)} d t \\ & \quad + \int_ {\tau_ {i + 1}} ^ {\theta_ {i + 1}} (k u _ {i + 1} ^ {*} (t) x _ {i + 1} (t) + q _ {0}) e ^ {- r (t + \sum_ {m = 1} ^ {i} s _ {m} + i T)} d t \\ & \quad + \int_ {\theta_ {i + 1}} ^ {T} (k u _ {i + 1} ^ {*} (t) x _ {i + 1} (t) + q _ {0}) e ^ {- r (t + \sum_ {m = 1} ^ {i} s _ {m} + i T)} d t \bigg ]. \end{array}\tag{B5}
$$

Also, recall that only $\tau _ { i + 1 } ,$ the entry time, depends on $x _ { i } ( T )$ while $\theta _ { i + 1 }$ is independent of $x _ { i } ( T )$ (instead $\theta _ { i + 1 }$ is related to $M _ { i - 1 }$ and $x _ { i + 1 } ( T ) )$ .

Thus, after some simplification, the transversality condition for period i can be written as

$$
\begin{array}{l} \lambda_ {i} (T) = \frac {\partial}{\partial x _ {i} (T)} \int_ {0} ^ {\infty} \int_ {0} ^ {\infty} \dots \int_ {0} ^ {\infty} \left[ \int_ {\tau_ {i + 1}} ^ {\theta_ {i + 1}} \left(k \hat {u} \hat {x}\right) e ^ {- r \left(t + \sum_ {m = 1} ^ {i} s _ {m} + i T\right)} d t \right. \\ \left. + \int_ {\theta_ {i + 1}} ^ {T} \left(k u _ {i + 1} ^ {*} (t) x _ {i + 1} (t)\right) e ^ {- r \left(t + \sum_ {m = 1} ^ {i} s _ {m} + i T\right)} d t \right. \\ \left. + \int_ {0} ^ {T} \left(q _ {0}\right) e ^ {- r \left(t + \sum_ {m = 1} ^ {i} s _ {m} + i T\right)} d t \right] \\ \cdot (\eta e ^ {- \eta s _ {1}}) (\eta e ^ {- \eta s _ {2}}) \dots (\eta e ^ {- \eta s _ {i}}) d s _ {1} d s _ {2} \dots d s _ {i}. \end{array} \tag {B6}
$$

Since $\mathsf { \pmb { S } } _ { i }$ is the exponentially distributed i.i.d. random variable representing OFF time between interactions with mean value $1 / \eta ,$ , and only $\tau _ { i + 1 }$ depends on $x _ { i } ( T )$ , this can be simplified (using Leibnitz differentiation under the integral sign) to

$$
\begin{array}{l} \lambda_ {i} (T) = (- k \hat {u} \hat {x} e ^ {- r (i T)}) \left(\int_ {0} ^ {\infty} \left(e ^ {- r \left(\tau_ {i + 1} + s _ {i}\right)} \frac {\partial \tau_ {i + 1}}{\partial x _ {i} (T)}\right) \eta e ^ {- \eta s _ {i}} d s _ {i}\right) \\ \cdot \left(\prod_ {m = 1} ^ {i - 1} \int_ {0} ^ {\infty} \left(e ^ {- r s _ {m}}\right) \eta e ^ {- \eta s m} d s _ {m}\right). \end{array} \tag {B7}\tag{B7}
$$

We prove some properties based on the equation above.

<sup>Property</sup> <sup>B.3.</sup> In the limit that the OFF period is infinitely large $( \eta \to 0 )$ , the transversality condition $\lambda _ { i } ( T ) \to 0$

<sup>Property</sup> <sup>B.4.</sup> In the limit that the OFF period is infinitely small $( \eta \to \infty )$ , the transversality condition $\grave { \lambda _ { i } } ( T ) \to \hat { \lambda } . \quad \Breve { \square }$ Property B.5.

$$
\begin{array}{c} \frac {\partial}{\partial \eta} \lambda_ {i} (T) = (- k \hat {u} \hat {x} e ^ {- r (i T)}) \frac {\partial}{\partial \eta} \biggl (\int_ {0} ^ {\infty} \biggl (e ^ {- r (\tau_ {i + 1} + s _ {i})} \frac {\partial \tau_ {i + 1}}{\partial x _ {i} (T)} \biggr) \\ \cdot \eta e ^ {- \eta s _ {i}} d s _ {i} \biggr) \biggl (\prod_ {m = 1} ^ {i - 1} \int_ {0} ^ {\infty} (e ^ {- r s _ {m}}) \eta e ^ {- \eta s m} d s _ {m} \biggr) \geq 0. \end{array}
$$

We use the following identities to prove this:

(i) $\partial \tau _ { i + 1 } / \partial x _ { i } ( T ) \leq 0$ since the time to enter steady state in period $i + 1$ will decrease as the ending learning capital from period $i ~ ( x _ { i } ( T ) )$ increases.

(ii) $\begin{array} { r } { \int _ { 0 } ^ { \infty } \dot { \eta } e ^ { - \eta \mathbf { s } _ { i } } d \mathbf { s } _ { i } = 1 } \end{array}$ is the PDF for exponentially distributed $\mathbf { \boldsymbol { s } } _ { i }$ .

(iii) Finally, it can be shown that both the integrand functions $G ( \zeta _ { i } ) = ( e ^ { - r ( \tau _ { i + 1 } + \varsigma _ { i } ) } ( \partial \tau _ { i + 1 } / \partial x _ { i } ( T ) ) )$ and $H ( \mathfrak { s } _ { k } ) = \bar { ( } e ^ { - r \mathfrak { s } _ { k } } )$ are such that $( \partial / \partial \mathsf { s } _ { i } ) G ( \mathsf { s } _ { i } ) \geq 0 , ( \partial / \partial \mathsf { s } _ { k } ) H ( \mathsf { s } _ { k } ) \leq 0 .$

So $\begin{array} { r } { ( \int _ { 0 } ^ { \infty } ( e ^ { - \dot { r } ( \bar { \tau } _ { i + 1 } + \dot { \bar { s } _ { i } } ) } ( \partial \bar { \tau } _ { i + 1 } / \partial x _ { i } ( T ) ) ) \dot { \eta } e ^ { - \dot { \eta } \widehat { s _ { i } } } d \mathbf { s } _ { i } ) \ = \ \int _ { 0 } ^ { \infty } G ( \mathfrak { s } _ { i } ) | } \end{array}$ $\eta e ^ { - \eta \mathsf { s } _ { i } } d \mathsf { s } _ { i }$ can be interpreted as a weighted sum of the $G ( \pmb { \varsigma } _ { i } )$ function. Now, as  increases, the weights become large for smaller values of $\mathbf { \boldsymbol { s } } _ { i }$ and smaller for large $\mathbf { \boldsymbol { s } } _ { i } .$ . Combine this with the fact that $( \partial / \partial \pmb { \varsigma } _ { i } ) G ( \pmb { \varsigma } _ { i } ) \geq 0 ,$ , it follows that $\begin{array} { r } { \int _ { 0 } ^ { \infty } G ( s _ { i } ) \eta e ^ { - \eta s _ { i } } d s _ { i } } \end{array}$ decreases (becomes more negative) as  increases.

The same intuition can be used to show that $\begin{array} { r } { ( \prod _ { k = 1 } ^ { i - 1 } \int _ { 0 } ^ { \infty } H ( \pmb { \varsigma } _ { k } ) \pmb { \eta } e ^ { - \pmb { \eta } \pmb { s } _ { k } } d \pmb { \varsigma } _ { k } ) } \end{array}$ 5 increases as  increases.

Hence proved that

$$
\begin{array}{l} \frac {\partial}{\partial \eta} \lambda_ {i} (T) = (- k \hat {u} \hat {x} e ^ {- r (i T)}) \\ \qquad \cdot \frac {\partial}{\partial \eta} \left(\int_ {0} ^ {\infty} \left(e ^ {- r (\tau_ {i + 1} + s _ {i})} \frac {\partial \tau_ {i + 1}}{\partial x _ {i} (T)}\right) \eta e ^ {- \eta s _ {i}} d s _ {i}\right) \\ \qquad \cdot \left(\prod_ {k = 1} ^ {i - 1} \int_ {0} ^ {\infty} (e ^ {- r s _ {k}}) \eta e ^ {- \eta s _ {k}} d s _ {k}\right) \geq 0. \end{array}
$$

This has a nice interpretation. As the mean OFF time $( 1 / \eta )$ decreases, the time it takes for the adjoint variable to go from its steady-state value $\lambda _ { i } ( \theta _ { i } ) = \hat { \lambda }$ , to its ending value decreases $\lambda _ { i } ( T )$ Hence the time spent in steady-state increases. <sup></sup>

<sup>Property</sup> <sup>B.6.</sup> For completeness, we now show that period i + 1 could not have started with $u ^ { * } = 1$ by contradiction.

Say period $i + 1$ starts with $u ^ { * } = 1$ region, then it can be shown that Equation (B7) will be transformed to (B8).

$$
\lambda_ {i} (T) = \int_ {0} ^ {\infty} \left((k u _ {i + 1} ^ {*} (\tau_ {i + 1}) x _ {i + 1} (\tau_ {i + 1}) - k \hat {u} \hat {x}) e ^ {- r (\tau_ {i + 1} + s _ {I} + i T)} \frac {\partial \tau_ {i + 1}}{\partial x _ {i} (T)}\right)
$$

$$
\cdot \eta e ^ {- \eta s _ {i}} d \mathbf {s} _ {i} \left(\prod_ {k = 1} ^ {i - 1} \int_ {0} ^ {\infty} (e ^ {- r \mathbf {s} _ {k}}) \eta e ^ {- \eta s _ {k}} d \mathbf {s} _ {k}\right) = 0.\tag{B8}
$$

This implies that period i will end in the $u ^ { * } = 1$ region, in turn, $x _ { i } \bar { ( } T ) < \hat { x } \Rightarrow \bar { x } _ { i + 1 } ( 0 ) = x _ { i } ( T ) e ^ { - \rho s _ { i } } < \hat { x }$ . Thus period $i + 1$ must start in $u ^ { * } = 0 .$ But this contradicts our assumption. Hence, it is proved that any intermediate interaction period cannot start in $u ^ { * } = 1 , \ \sqsupset$

Hence, Properties B.1–B.5 complete the proof. <sup></sup>

<sup>Lemma</sup> <sup>1.</sup> The ending learning capital in any interaction period is independent of the starting learning capital if the steady-state region is attained.

<sup>Proof.</sup> Follows from Property B.2 above. <sup></sup>

<sup>Corollary</sup> <sup>6.</sup> As the mean OFF time $( 1 / \eta )$ decreases, the time spent in steady state increases.

<sup>Proof.</sup> Follows from Property B.5 above. <sup></sup>

## Appendix C.

## C.1. Optimizing the Size of the Offer Set

<sup>Proposition</sup> <sup>5.</sup> The structure of the optimal policy for a planning horizon T is

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} I & 0 \leq t <   \tau \\ \hat {u} & \tau \leq t \leq \theta \\ 1 & \theta <   t \leq T \end{array} \right. a n d s ^ {*} (t) = \left\{ \begin{array}{l l} Y & 0 \leq t <   \tau \\ \hat {s} & \tau \leq t \leq \theta \\ \sigma_ {1} (x) & \theta <   t \leq T, \end{array} \right.
$$

$$
w h e r e I = \left\{ \begin{array}{l l} 0 & x _ {0} <   \hat {x} \\ 1 & x _ {0} > \hat {x}, \end{array} \right. Y = \left\{ \begin{array}{l l} \sigma_ {0} (x) & x _ {0} <   \hat {x} \\ \sigma_ {1} (x) & x _ {0} > \hat {x}, \end{array} \right.
$$

$$
\left. \frac {\partial f (x , s)}{\partial s} \right| _ {s = \sigma_ {0}} = 0, a n d k x + \lambda \left. \frac {\partial g (x , s)}{\partial s} \right| _ {s = \sigma_ {1}} = 0.
$$

<sup>Proof.</sup> The dynamic optimal control problem for composition of the consideration set, under known session duration T , can be formulated as follows:

$$
\begin{array}{r l} \max _ {u (t), s (t)} & J = \max _ {u (t), s (t)} \int_ {0} ^ {T} q (t) e ^ {- r t} d t \\ & = \max _ {u (t) s (t)} \int_ {0} ^ {T} (k u (t) s (t) x (t) + q _ {0}) e ^ {- r t} d t \\ \text {s.t.} & \dot {x} = f (x, s) (1 - u) + g (x, s) u - h (x, s), \\ & x (0) = x _ {0}, \quad 0 \leq u (t) \leq 1, \quad 0 \leq s (t) \leq \sigma_ {\max}. \end{array}
$$

We begin by formulating the Hamiltonian for this problem as follows:

$$
H = k u s x + q _ {0} + \lambda (f (x, s) (1 - u) + g (x, s) u - h (x, s)),\tag{C1}
$$

where  is the adjoint state variable

$$
\frac {\partial H}{\partial u} = k s x - \lambda (f (x, s) - g (x, s)),\tag{C2}
$$

$$
\frac {\partial H}{\partial s} = k u x + \lambda \left(\frac {\partial f}{\partial s} + u \left(\frac {\partial g}{\partial s} - \frac {\partial f}{\partial s}\right)\right).\tag{C3}
$$

The Hamiltonian is linear in the control variable $u ,$ so that the optimal solution is given by

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} 0 & \text {iff} \phi (t) = k x s - \lambda (f (x) - g (x)) <   0 \\ \text {singular} & \text {iff} \phi (t) = k x s - \lambda (f (x) - g (x)) = 0 \\ 1 & \text {iff} \phi (t) = k x s - \lambda (f (x) - g (x)) > 0, \end{array} \right.\tag{C4}
$$

where $\phi ( t ) = \partial H / \partial u = k s x - \lambda ( f ( x ) - g ( x ) )$ 5 is hereafter referred to as a switching function.

The other control variable, viz., offer set size (s) is chosen per Equation (C3) as follows:

$$
\frac {\partial H}{\partial s} = 0 = k u x + \lambda \left(\frac {\partial f}{\partial s} + u \left(\frac {\partial g}{\partial s} - \frac {\partial f}{\partial s}\right)\right).
$$

Primarily, we are trying to establish that singular control is feasible for this general problem. Similar to Proposition 1, we derive the singular solution as follows:

$$
\hat {x} = (f (\hat {x}, \hat {s}) - h (\hat {x}, \hat {s})) (f (\hat {x}, \hat {s}) - g (\hat {x}, \hat {s})) \cdot \bigg [ (f (\hat {x}, \hat {s}) - h (x ^ {s}, s ^ {s})
$$

$$
\left. \cdot \left(\frac {\partial f}{\partial x} - \frac {\partial g}{\partial x}\right) - (f (\hat {x}, \hat {s}) - g (\hat {x}, \hat {s})) \left(\frac {\partial f}{\partial x} - \frac {\partial h}{\partial x} - r\right) \right] ^ {- 1},\tag{C5}
$$

$$
\mathrm{hence} \hat {\lambda} = \frac {k \hat {x} \hat {s}}{f (\hat {x} , \hat {s}) - g (\hat {x} , \hat {s})},\tag{C6}
$$

$$
\text { hence } \hat {u} = \frac {f (\hat {x} , \hat {s}) - h (\hat {x} , \hat {s})}{f (\hat {x} , \hat {s}) - g (\hat {x} , \hat {s})},\tag{C7}
$$

$$
\text { hence } \hat {s} = (- 1) \cdot \left(\frac {\partial f / \partial s}{f (\hat {x} , \hat {s}) - h (\hat {x} , \hat {s})} + \frac {\partial g / \partial s - \partial f / \partial s}{f (\hat {x} , \hat {s}) - g (\hat {x} , \hat {s})}\right) ^ {- 1}.\tag{C8}
$$

From Equation (C8), it is clear that the optimal offer set size in the singular region is indeed constant (and independent of time). Therefore the optimal solution in the singular region is steady state and characterized by Equations (C5)–(C8).

An additional note from Equation (C8) is that, for the steady state to be feasible, i.e., $\bar { \hat { s } } > 0 ,$ we need that

$$
\frac {\partial g}{\partial s} \leq \frac {\partial f}{\partial s} \leq 0.\tag{C9}
$$

LC condition for existence of singular solution. From Equations (C3)–(C8), the LC condition can be written as

$$
\begin{array}{l} \text {hence} - \frac {\partial}{\partial u} \left(\frac {\partial^ {2} H _ {u}}{\partial t ^ {2}}\right) \\ = - k \underbrace {\left(\underbrace {\frac {\partial f}{\partial x} - \frac {\partial h}{\partial x}} _ {-}\right)} _ {-} \underbrace {(g - f)} _ {-} + \left(k + \lambda \left(\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x}\right)\right) \\ \cdot \underbrace {\left((f - h) \left(\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x}\right) + (g - f) \left(r + \frac {\partial h}{\partial x} - \frac {\partial f}{\partial x}\right)\right)} _ {-} - \lambda \underbrace {(g - f)} _ {-} \\ \cdot \underbrace {\left(\left(\underbrace {\frac {\partial^ {2} g}{\partial x ^ {2}} - \frac {\partial^ {2} f}{\partial x ^ {2}}} _ {-}\right) \underbrace {(f - h)} _ {+} + \underbrace {(g - f)} _ {-} \underbrace {\left(\frac {\partial^ {2} h}{\partial x ^ {2}} - \frac {\partial^ {2} f}{\partial x ^ {2}}\right)} _ {+} + r \underbrace {\left(\frac {\partial g}{\partial x} - \frac {\partial f}{\partial x}\right)} _ {+}\right)} _ {+} \end{array}
$$

$$
\leq 0.\tag{C10}
$$

Equation (C8) satisfies the LC condition, which implies that the singular solution, if it exists, is optimal so long as

(i) $f ( x , s ) \geq g ( x , s )$ . This follows since $f ( x , s )$ is the learning rate when the firm is completely invested toward exploration, while $g ( x , s )$ is the learning rate when the firm is completely invested toward sales for any given offer set size s.

(ii) $( \partial / \partial \dot { x } ) \{ g ( x , s ) - f ( x , s ) \} > 0 , ( \partial ^ { 2 } / \partial x ^ { 2 } ) \{ g ( x , s ) - f ( x , s ) \}$ $\leq 0 .$ . We assume the negative impact of reducing investment toward exploration $( f ( x , s ) - { \overline { { g } } } ( x , s ) )$ reduces at a decreasing rate as the firm learns more about the consumer’s profile for any given offer set size s.

(iii) $( \partial / \partial x ) \{ f ( x , s ) - h ( x , s ) \} < 0 , ( \partial ^ { 2 } / \partial x ^ { 2 } ) \{ f ( x , s ) - h ( x , s ) \}$ $\leq 0 .$ . Note that $f ( x , s ) - h ( x , s )$ is the effective learning rate when investing wholly toward exploration. We expect this learning rate to be negatively impacted as the firm learns more about a consumer at an increasing rate, $i . e . , f ( x , s ) - h ( x , s )$ is decreasing and concave for a given offer set size s.

(iv) The discount rate is less than a critical value, $r \leq r _ { c } =$ $( ( \dot { f } - g ) ( \partial ^ { 2 } h / \partial x ^ { 2 } - \partial ^ { 2 } f / \partial x ^ { 2 } ) + ( \partial ^ { 2 } f / \partial x ^ { 2 } - \partial ^ { 2 } g / \partial x ^ { 2 } ) ( f - \ddot { h } ) ) /$ $( \partial g / \partial x - \partial f / \partial x )$

Next, we prove some useful properties on the lines similar to Proposition 1.

<sup>Property</sup> <sup>C.1.</sup> Near the end of the engagement period, the firm always finds it optimal to completely direct recommendations toward sales.

<sup>Property</sup> <sup>C.2.</sup> The optimal solution cannot transition from $u ^ { * } = 1 \ t o \ u ^ { * } = 0 .$ . 

<sup>Property</sup> <sup>C.3.</sup> The optimal cannot transition from $u ^ { * } =$ singular to $u ^ { * } = 0 . \square$

<sup>Property</sup> <sup>C.4.</sup> Fully directing recommendations toward learn ing the user’s profile can only occur at the start of the engagement period.

<sup>Proof.</sup> The result follows from Properties C.2 and C.3. <sup></sup>

<sup>Property</sup> <sup>C.5.</sup> The transition from $u ^ { * } = 0$ to $u ^ { * } = 1$ is monotonic. <sup></sup>

<sup>Property</sup> <sup>C.6.</sup> The transition from u<sup>∗</sup> = singular to $u ^ { * } = 1$ is monotonic. <sup></sup>

Based on Properties C.1–C.6, it follows that the optimal policy will be of the form

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} I & 0 \leq t <   \tau \\ \hat {u} & \tau \leq t \leq \theta \\ 1 & \theta <   t \leq T, \end{array} \right. \quad \text { where } \quad I = \left\{ \begin{array}{l l} 0 & x _ {0} <   \hat {x} \\ \hat {u} & x _ {0} = \hat {x} \\ 1 & x _ {0} > \hat {x}. \end{array} \right.
$$

Here,  and $\theta$ are the optimal switching points and can be calculated as follows:

 is the time taken to enter the steady state, vis-à-vis time taken to go from $x _ { 0 }$ to $\boldsymbol { x } ( \tau ) = \boldsymbol { \hat { x } }$ . Similarly,  can be calculated based on the time taken $( T - \theta )$ to go from $\lambda ( \theta ) = \hat { \lambda } \ \mathrm { t o } \ \lambda ( T ) = 0$ to satisfy the transversality condition. <sup></sup>

Corollary $7 .$ In the region where the firm is fully invested in learning (beginning of the planning horizon when $x _ { 0 } < \hat { x } ) .$ the optimal size of the offer set depends on the state variable $( s ^ { * } = \sigma _ { 0 } ( x ) )$ , where $\partial f ( x , s ) / \partial s | _ { s = \sigma _ { 0 } } = 0$

<sup>Proof.</sup> From Equation (C3), in the region $u ^ { * } = 0$ , the optimal offer set size is chosen such that

$$
\frac {\partial H}{\partial s} = \lambda \frac {\partial f}{\partial s} = 0. \quad \square
$$

<sup>Corollary</sup> <sup>8.</sup> The optimal size of the offer set at the end of the planning horizon is equal to its maximum value.

<sup>Proof.</sup> From C3, at $u = 1 , H _ { s } = k x + \lambda ( ( \partial f / \partial s ) + ( \partial g / \partial s -$ $\partial f / \partial s ) )$ 1

$$
\text { hence } \frac {\partial H (T)}{\partial s} = k x \geq 0 \quad \text { since } \lambda (T) = 0.\tag{C11}
$$

Since s<sup>∗</sup> is bang-bang in nature, it follows from (C11) that at the end of the planning horizon, the optimal size of the offer set is equal to its maximum value. <sup></sup>

## References

Abernathy J, Evgeniou T, Toubia O, Vert J-P (2008) Eliciting consumer preferences using robust adaptive choice questionnaires. IEEE Trans. Knowledge Data Engrg. 20(2):145–155.

Adomavicius G, Tuzhilin A (2005) Personalization technologies: A process-oriented perspective. Comm. ACM 48(10):83–90.

Ansari A, Mela CF (2003) E-customization. J. Marketing Res. 40(2): 131–145.

Atahan P, Sarkar S (2011) Accelerated learning of user profiles. Management Sci. 57(2):215–239.

Balabanovic M (1998) Exploring versus exploiting when learning user models for text recommendation. User Modeling User-Adapted Interaction 8:71–102.

Blattberg RC, Deighton J (1996) Manage marketing by the customer equity test. Harvard Bus. Rev. 74(4):136–144.

Bodapati A (2008) Recommendation systems with purchase data. J. Marketing Res. XLV:77–93.

Breese JS, Heckerman D, Kadie C (1998) Empirical analysis of predictive algorithms for collaborative filtering. Proc. 14th Conf. Uncertainty in Artificial Intelligence (Morgan Kaufmann, San Francisco), 43–52.

Caro F, Gallien J (2007) Dynamic assortment with demand learning for seasonal consumer goods. Management Sci. 53(2):276–292.

Case JH (1979) Economics and the Competitive Process (New York University Press, New York).

Das A, Mathieu C, Ricketts D (2010) Maximizing profit using recommender systems. WWW2010.

Fader PS, Hardie BGS, Lee KL (2005) Counting your customers, the easy way: An alternative to the Pareto/NBD model. Marketing Sci. 24(2):275–284.

Fang Y, Si L (2012) A latent pairwise preference learning approach for recommendation from implicit feedback. Proc. 21st ACM Internat. Conf. Inform. Knowledge Management (CIKM’12), October 29– November 2 (ACM, New York), 2567–2570.

Haubl G, Trifts V (2000) Consumer decision making in online shopping environments: The effects of interactive decision aids. Marketing Sci. 19(1):4–21.

Huang Z, Chung W, Chen H (2004) A graph model for e-commerce recommender systems. J. Amer. Soc. Inform. Sci. Tech. 55(3): 259–274.

Kitts B, Freed D, Vrieze M (2000) Cross-sell: A fast promotion-tunable customer-item recommendation method based on conditionally independent probabilities. KDD’00: Proc. Sixth ACM SIGKDD Internat. Conf. Knowledge Discovery and Data Mining (ACM, New York), 437–446.

Konstan AJ, McNee MS, Ziegler C, Torres R, Kapoor N, Riedl JT (2006) Lessons on applying automated recommender systems to information-seeking tasks. Proc. 21st National Conf. Artificial Intelligence (AAAI, Boston), 1630–1633.

Lenk PJ, DeSarbo WS, Green PE, Young MR (1996) Hierarchical Bayes conjoint analysis: Recovery of partworth heterogeneity from reduced experimental designs. Marketing Sci. 15(2):173–191.

Linden G (2008) People who read this article also read. IEEE Spectrum 45(3):46–60.

Louviere JJ, Woodworth G (1983) Design and analysis of simulated consumer choice or allocation experiments: An approach based on aggregate data. J. Marketing Res. 20:350–367.

Miller TW, Dickson PR (2001) On-line market research. Internat. J. Electronic Commerce 5(3):139–167.

Mobasher B, Berendt B, Spiliopoulou M (2001) KDD for personalization. Tutorial 5th Eur. Conf., Principles and Practice of Knowledge Discovery in Databases (PKDD-2001) (Springer-Verlag, Berlin).

Montgomery AL (2001) Applying quantitative marketing techniques to the Internet. Interfaces 30(2):90–108.

Mookerjee R, Kumar S, Mookerjee V (2012) To show or not to show: Using user profiling to manage ad campaigns at Chitika. Interfaces 42(5):449–464.

Murthi BPS, Sarkar S (2003) The role of the management sciences in research on personalization. Management Sci. 49(10):1344–1362.

Padmanabhan B, Zheng Z, Kimbrough SO (2001) Personalization from incomplete data: What you don’t know can hurt. ACM SIGKDD Internat. Conf. KDD (ACM, New York).

Peppers D, Rogers M (1997) Enterprise One to One: Tools for Competing in the Interactive Age (Doubleday, New York).

Powell WB (2007) Approximate Dynamic Programming: Solving the Curses of Dimensionality (John Wiley & Sons, New York).

Reinartz WJ, Kumar V (2003) Customer lifetime duration: An empirical framework for measurement and explanation. J. Marketing 67(January):77–99.

Reinartz WJ, Thomas SJ, Kumar V (2005) Balancing acquisition and retention resources to maximize customer profitability. J. Marketing 69(1):63–79.

Rubens N, Kaplan D, Sugiyama M (2011) Active learning in recommender systems. Ricci F, Rokach L, Shapira B, Kantor PB, eds. Recommender Systems Handbook (Springer, New York), 735–767.

Sandvig JJ, Mobasher B, Burke R (2007) Robustness of collaborative recommendation based on association rule mining. Proc. 2007 Conf. Recommender Systems (ACM, New York), 105–112.

Schmittlein D, Morrison D, Colombo R (1987) Counting your customers: Who are they and what will they do next? Management Sci. 33(1):1–24.

Sethi SP, Thompson GL (2000) Optimal Control Theory: Applications to Management Science and Economics (Kluwer Academic Publishers, Norwell, MA).

Shani G, Heckerman D, Brafman RI (2005) A MDP-based recommender system. J. Machine Learn. Res. 6:1265–1295.

Sia KC, Zhu S, Chi Y, Hino K, Tseng BL (2007) Capturing user interests by both exploitation and exploration. Proc. 11th Internat. Conf. User Modeling 4511:334–339.

Sutton RS (1990) Integrated architectures for learning, planning and reacting based on approximation dynamic programming. Proc. 7th Internat. Conf. Machine Learn. (Morgan Kaufmann, San Francisco), 216–224.

Tam YK, Ho YS (2005) Web personalization as a persuasion strategy: An elaboration likelihood model perspective. Inform. Systems Res. 16(3):271–291.

Toubier O, Hauser JR, Simester DJ (2004) Polyhedral methods for adaptive choice-based conjoint analysis. J. Marketing Res. 41:116–131.

Venkatesan R, Kumar V, Bohling T (2007) Optimal customer relationship management using Bayesian decision theory: An application for customer selection. J. Marketing Res. 44(4):579–594.

Vidale ML, Wolfe HB (1957) An operations-research study of sales response to advertising. Oper. Res. 5(3):370–381.

Wall Street Journal (2007) Firm mines offline data to target online ads. (October 17).

Wei YZ, Moreau L, Jennings NR (2005) Learning users’ interest by quality classification in market-based recommender systems. IEEE Trans. Knowledge Data Engrg. 17(12):1678–1688.

Zaiane OR (2002) Building a recommender agent for e-learning systems. Proc. Internat. Conf. Comput. Ed. (ICCE’02) (IEEE, Piscataway, NJ).
