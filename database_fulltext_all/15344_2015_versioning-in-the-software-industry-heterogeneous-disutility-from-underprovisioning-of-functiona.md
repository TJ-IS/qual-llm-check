---
otero_id: 15344
otero_key: "R6GA9SEW"
title: "Versioning in the Software Industry: Heterogeneous Disutility from Underprovisioning of Functionality"
authors: "Shivendu Shivendu; Zhe (James) Zhang"
year: "2015"
journal: "Information Systems Research"
doi: "10.1287/isre.2015.0597"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/R6GA9SEW/fulltext/images/e018a0e1a944c840e17d5840c3702e07cb431382c0a80180b3b0e0c548517b50.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Versioning in the Software Industry: Heterogeneous Disutility from Underprovisioning of Functionality

Shivendu Shivendu, Zhe (James) Zhang

To cite this article:

Shivendu Shivendu, Zhe (James) Zhang (2015) Versioning in the Software Industry: Heterogeneous Disutility from Underprovisioning of Functionality. Information Systems Research 26(4):731-753. http://dx.doi.org/10.1287/isre.2015.0597

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2015, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/R6GA9SEW/fulltext/images/ae4ec11783b0fdd9c400bf1216804d99f4ec66737732a1439ed9fa7694466f75.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Versioning in the Software Industry: Heterogeneous Disutility from Underprovisioning of Functionality

Shivendu Shivendu

Muma College of Business, University of South Florida, Tampa, Florida 33620, shivendu@usf.edu

Zhe (James) Zhang

Naveen Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080, jameszhangzhe@utdallas.edu

iterature has identified factors such as piracy, network externality, or concave cost of producing quality as key drivers of software versioning. However, software firms adopt versioning strategies that are often invariant across different market settings. To explain universal business practice of software versioning, we focus on “inconvenience” or disutility that users experience when software has lower functionality than what they require to accomplish tasks. In our model, users are heterogeneous on marginal valuation for functionality and the required level of functionality such that those with higher valuation have a higher required level of functionality. Users do not derive any additional utility if the software has more functionality than what they require. We show that heterogeneous disutility from underprovisioning of functionality is a sufficient condition for optimality of versioning under fairly general conditions. We also show that, as high-type users’ required level of functionality increases, the firm increases the functionality level of the high version. Yet surprisingly, the firm may decrease the functionality level of the low version if the proportion of high-type users is moderate. On the other hand, as the required level of functionality of low-type users increases, the firm may reduce the functionality level of the low version when the proportion of high-type users is high, though the functionality level of the high version remains the same. Counterintuitively, an increase in the high-type (low-type) users’ required level of functionality negatively (positively) impacts high-type users’ consumer surplus.

Keywords: vertical differentiation; versioning; pricing; disutility from underprovisioning History: Il-Horn Hann, Senior Editor; Anjana Susarla, Associate Editor. This paper was received July 13, 2012, and was with the authors 9.5 months for 3 revisions.

## 1. Introduction

Versioning<sup>1</sup> as a product-price strategy is ubiquitous in information goods in general and in software in particular. A firm offers different versions of software at different prices such that different “types” of users self-select the version-price pair that is “targeted” to them (Mussa and Rosen 1978, Varian 1998, Shapiro and Varian 1998). Software firms first develop a flagship product with the highest level of functionality and then create different versions by strategically disabling some of the functionality of the flagship product (Ghose and Sundararajan 2005, Gershoff et al. 2012, Wei and Nault 2013, Dey and Lahiri 2013). For example, Microsoft offers their on-premise operating system Windows 8 in three versions and their on-premise productivity software Office 2013 in five versions. Adobe Systems offers their graphics editing software Adobe Photoshop CS in two versions. IBM offers their statistical software IBM SPSS Statistics in three versions. Similarly, Intuit, which specializes in the tax-related software TurboTax, offers five versions of its federal and state tax filing software. In light of this commonly observed business practice of software firms, it is not surprising that the study of versioning strategies is of central interest to the academics in information systems (IS). However, they do not recommend versioning as a universal strategy, but recommend it only under certain market conditions (see Table 1).

Often, software firms’ versioning strategy does not appear to be determined by specific market conditions identified in the literature. For example, Microsoft has a worldwide product strategy for Windows operating systems and adopts versioning strategy in the United States and the Chinese markets for Windows 8, even though piracy rates are much higher in China (The Software Alliance 2012). Furthermore, firms often adopt versioning strategy for software products with weak network externality. TurboTax is available in five versions with increasingly more complex capabilities, even though users of electronic tax filing software do not necessarily benefit from an increase in the installed base. Similarly, since it is almost costless for software firms to remove functionality from the flagship product to create a version with a lower level of functionality, and marginal cost of additional copies is negligible (Varian 1998, Bhargava and Choudhary 2004, Chellappa and Shivendu 2005, Wei and Nault 2014), cost structure may not be the driver of versioning strategies. Furthermore, literature recommends that versioning is not optimal if the marginal cost of producing different versions is the same (Anderson and Dana 2009, Salant 1989). Nonetheless, we observe software firms adopt a versioning strategy even though the marginal cost of producing different versions is the same.

Table 1 Summary of Findings of Literature on Versioning of Information Goods for a Monopolist Firm

<table><tr><td>Paper</td><td>Model specification</td><td>Conditions under which versioning is optimal</td></tr><tr><td>Bhargava and Choudhary (2001)</td><td>Vertical differentiation</td><td>When the highest quality product does not have the lowest cost-quality ratio</td></tr><tr><td>Wu et al. (2003), Chellappa and Shivendu (2005), Wu and Chen (2008)</td><td>Vertical differentiation</td><td>When there is piracy</td></tr><tr><td>Jing (2000), Cheng and Tang (2010)</td><td>Vertical differentiation</td><td>When there is network externality</td></tr><tr><td>Chen and Seshadri (2007)</td><td>Vertical differentiation</td><td>When users have convex value for outside options</td></tr><tr><td>Wei and Nault (2014)</td><td>Vertical and horizontal differentiation</td><td>When shared characteristics are not too valuable relative to mutually exclusive characteristics or if consumer valuation of the highest group is not too much higher than the next lowest group</td></tr><tr><td>Raghunathan (2000)</td><td>Vertical differentiation</td><td>When cannibalization effect is large</td></tr><tr><td>Bhargava and Choudhary (2008)</td><td>Vertical differentiation</td><td>When relative valuations and cost for low- and high-quality versions decrease when taste for quality decreases</td></tr><tr><td>Niculescu and Wu (2014)</td><td>Vertical differentiation</td><td>When users&#x27; prior on premium functionality is either relatively low or high, then offering a feature-limited version for free is optimal</td></tr></table>

The research objective of this paper is to bridge the gap between the recommendations of extant literature and universally adopted business practice of versioning strategy by software firms. Our work belongs to the stream of literature that has analyzed software firms motivation for versioning strategy from a perspective of how users derive utility from software, in the absence of any specific product characteristics or market conditions (Raghunathan 2000, Chen and Seshadri 2007, Wei and Nault 2014).

In our abstraction, users consider buying software to accomplish a specific set of tasks. To accomplish these tasks, users require a set of functionality in a software product. Software functionality consists of a set of features that enable users to perform certain tasks (Wilde and Scully 1995). For example, Microsoft product development teams begin the process of new software development by first creating a “vision statement” that provides a list of “user activities that need to be supported by the product features” (Cusumano and Selby 1997, p. 56). If the software product has less functionality than what the users require, then their willingness to pay is moderated by the “inconvenience” or disutility that they experience from underprovisioning.

This inconvenience or disutility can be either due to users incurring time and effort to manually accomplish their subtasks, or their annoyance and frustration or even emotional distress from not being able to accomplish some of the subtasks. For example,<sup>2</sup> a statistician, who wants to accomplish a task of demand forecasting, may require four functionality from spreadsheet software: (1) copying and pasting cells, (2) performing basic arithmetic operations, (3) running forecasting models, and (4) synchronizing files at multilocations (local computers and cloud). When the statistician evaluates a software product, like Microsoft Excel 2010, she takes into account the functionality of the software and her required level of functionality. If the software has functionality (1), (2), and (3) only, then she derives a benefit from these three functionality. Since the software does not provide functionality (4), she needs to update the files separately in each location, thus, incurring inconvenience or disutility. This leads to lowering of her willingness to pay for the software.

In addition, we consider the situation where users are heterogeneous in marginal valuation for functionality and requirements of functionality. High valuation or high-type users have higher requirements for functionality because they use the software in a complex task environment.<sup>3</sup> Continuing with the example of a spreadsheet software product, a school student also uses software, like Microsoft Excel 2010, to do her schoolwork. Compared with the statistician (high valuation), who does demand forecasting and has requirements for all four functionality, the student (low valuation) only requires functionality (1) and (2), and, thus, has a lower requirement of functionality. Furthermore, users derive no additional utility if the software has more functionality than what they require because they do not use functionalities beyond their requirement.<sup>4</sup> Therefore, the student has no additional utility from the spreadsheet software that has functionality for demand forecasting because she does not require it.

Continuing with the statistician and student example, if the spreadsheet software does not have the functionality to do demand forecasting, then the statistician uses multiple computations to do the same. This takes time and effort, and thus she experiences inconvenience. On the other hand, the student does not experience any inconvenience because of the missing functionality of demand forecasting because she does not require it. However, if the software does not have the functionality of copying and pasting cells, then both the statistician and the student manually input the same value in different cells. This takes time and effort, and, therefore, both of them experience inconvenience. In this paper, we examine the role of inconvenience or disutility from underprovisioning of functionality in a firm’s product-pricing strategy and show that in a vertically differentiated market, heterogeneous disutility from underprovisioning of functionality is a sufficient condition for optimality of versioning under fairly general conditions.

There is anecdotal evidence to support our conceptualization of the required level of functionality and inconvenience that users experience if software has a lower level of functionality than the required level.<sup>5</sup> It appears that there is a general agreement among various user groups that users evaluate the features of any particular version of software in relation to their requirements of “features” or functionality and experience inconvenience if the software has a lower level of functionality than what they require. Moreover, business reports support our abstraction that more functionality does not necessarily translate to more usefulness.<sup>6</sup>

In our conceptualization, a user’s willingness to pay for different versions of software consists of two parts: benefit from the level of functionality in software, and disutility from underprovisioning of functionality in relation to her required level of functionality. A user’s utility from a particular version of software is additive in benefit from functionality and disutility from underprovisioning of functionality. Our conceptualization of how users derive utility from software is different from extant literature in versioning (see Table 1) in the following three key aspects: (1) different types of users have different required levels of functionality, (2) more functionality than the required level of functionality does not increase users’ utility, and (3) users experience inconvenience or disutility if the software has less functionality than their required levels. These three key differences imply that in our setup, utility functions of high-type and low-type users cross over at some functionality level, which we characterize as an “indifferent level of functionality,” and high-type users have a higher willingness to pay than low-type users only if the functionality level is higher than this utility cross-over point. Note that the extant literature assumes that high-type users have a higher willingness to pay for any functionality level. We characterize this property of high-type and low-type users’ utility function to cross over at a positive utility level as a “single-crossing property” (Cooper 1984, p. 570).

Our work is close to Wei and Nault (2014) in the sense that in their hierarchical characteristics case, users are heterogeneous in their requirement for functionality beyond which their utility does not increase in functionality. Yet the key difference is that in their case users do not experience inconvenience from underprovisioning of functionality. This key difference implies that whereas in their model users who have a higher marginal valuation for functionality have a higher willingness to pay for all levels of functionality, in our model users with a higher marginal valuation for functionality (high type) have a lower willingness to pay than users with a low marginal valuation for functionality (low type) if there is a severe underprovisioning of functionality. As a result, in our setting, even though the market is vertically differentiated and all users’ willingness to pay weakly increases in functionality, ordering of willingness to pay of high-type and low-type users is not maintained for all functionality levels.

One of our key findings is that when users experience heterogeneous inconvenience because of underprovisioning of functionality, a versioning strategy is optimal even in the absence of other market conditions. This is so because when users experience heterogeneous inconvenience from underprovisioning of functionality, then high-type users incur higher inconvenience from the low-version software than low-type users. Therefore, high-type users are less attracted to the low-version software, and hence, the firm needs to provide them less incentive or information rent to stay with the high-version software. This dynamic leads to optimality of versioning strategy under fairly general conditions.

With fast changing computing environments and technologies, users’ required set of functionality is likely to increase over a period of time. When high-type users require more functionality, they get a high version with a higher functionality level, but their surplus decreases. Nevertheless, whether the firm should increase or decrease the functionality level of the low version depends on the distribution of user types. When lowtype users require more functionality, one might think that the firm should increase the functionality level of the low version to extract surplus. However, we find that the firm may lower the functionality level of the low version to economize on information rent when the market is dominated by high-type users.

Our contributions in this research are twofold. First, we identify heterogeneous disutility from underprovisioning as a sufficient condition for optimality of versioning under fairly general market conditions. This allows us to provide a novel explanation for the widespread business practice of versioning in the software industry. Our conceptualization sheds light on conditions under which a firm provides low-type users software with less functionality than they require, even if the software firm has zero cost of providing them their required level of functionality. Our key managerial recommendation is that software firms should take users’ inconvenience or disutility from underprovisioning of functionality into consideration in designing a versioning strategy. We also identify some interesting insights relating to the firm’s optimal versioning strategy as users’ required level of functionality increases.

Second, we propose a novel conceptualization of consumer utility that captures users’ heterogeneities in marginal valuation for functionality and required level of functionality. This allows us to analyze commonly observed situations in which high-type users not only have higher marginal valuation for functionality but also have a higher requirement for functionality. Previous studies have only considered users’ marginal valuation for functionality or quality in either linear utility function (Chellappa and Shivendu 2003, 2005; Bhargava and Choudhary 2001, 2004, 2008; Jones and Mendelson 2011; Wei and Nault 2013; Dey and Lahiri 2013) or quadratic utility function (Raghunathan 2000, Ghose and Sundararajan 2005). Our conceptualization of disutility from underprovisioning of functionality allows us to study the impact of changes in users requirements for functionality on a versioning strategy even when users’ marginal valuation for functionality does not change. This conceptualization allows us to develop a utility framework where high-type and low-type users’ utility functions cross over, which may also be relevant in studying other information goods markets.

The remainder of this paper is organized as follows: In §2, we outline our conceptualization of consumer utility function and monopolist software firm’s product strategies. In §3, we discuss product-pricing strategies of the firm and show that a versioning strategy is optimal. In §4, we discuss the impacts of changes in users’ required level of functionality on the software firm’s optimal versioning strategy. In §5, we analyze some extensions to our model and also discuss the implications of relaxing some of the model assumptions. We conclude our analysis and provide managerial implications in §6.

## 2. Model

We consider a class of software that provides a set of functionality to users to perform their tasks to meet specific needs (Wilde and Scully 1995). Users evaluate software in a task-oriented context akin to Garvin’s (1984) perspective of “user view” of quality, which corresponds to “the totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs” (International Organization for Standardization (ISO) 1994, p. 11). Software quality consists of multidimensional attributes like functionality, reliability, correctness, and usability (Kitchenham and Pfleeger 1996); and very often the only differentiating attribute among the different versions is functionality. In our model, users derive utility from a set of functionality of the software (Kekre et al. 1995) and recognize functionality as a measure of quality (Wei and Nault 2014).

Users require a set of functionality in software because they use it to accomplish a specific set of tasks. We refer to this set as the users’ required level of functionality. Users, who have higher marginal valuation for functionality, use software in a more complex task-oriented environment and, therefore, require more functionality. If the software has less functionality than users’ required level of functionality, then users experience inconvenience. The source of this inconvenience may be time or effort required to accomplish subtasks for which software has no functionality or it may stem from annoyance, frustration, or emotional distress from not being able to accomplish subtasks. We refer to this inconvenience as disutility from underprovisioning of functionality. Furthermore, in our context, users do not use functionality that is beyond their required functionality level and hence, derive no additional benefit from overprovisioning of functionality.

We consider a market that is vertically differentiated with heterogeneous users. Without loss of generality, we assume that there are two types of users, namely, high type and low type and each type of user is denoted by a duplet $\{ \theta _ { i } , x _ { i } \}$ where $i \in \{ \check { H } , L \} . ^ { 7 }$ The parameter  captures users’ heterogeneities in marginal valuation for functionality, where $\theta _ { H } > \theta _ { L } ,$ , and the parameter x denotes users’ required levels of functionality, where $x _ { H } > x _ { L }$ . In our conceptualization, high-type users have a higher marginal valuation for functionality as well as a higher required level of functionality compared to low-type users. Elements of duplet $\left\{ \theta _ { i } , x _ { i } \right\}$ can take any value as long as the rank ordering is maintained. In our example of the statistician and the student, if the valuation of functionality and the required level of functionality of the statistician is $\{ \theta _ { S H } ^ { - } , x _ { S H } \}$ , and that of the student is $\{ \theta _ { S L } , x _ { S L } \} ,$ then $\theta _ { S H } > \theta _ { S L }$ and $x _ { S H } > x _ { S L }$ This conceptualization of maintaining the rank ordering closely mimics the reality wherein one observes that progressively higher versions of software are almost always forward compatible (the higher version has all of the functionality of the lower version), and higher versions are sold at higher prices.<sup>8</sup> Moreover, this conceptualization of two-dimensional ordered user heterogeneities is similar to the hierarchical characteristics case of Wei and Nault (2014). For the sake of completeness, in $\ S 5 . 4 ,$ we discuss a firm’s versioning strategy when the rank ordering is not maintained.

Marginal valuation for functionality (5, and required level of functionality (x5, are users’ private information and the software firm only knows the distribution. The proportion of high-type users, denoted by $\{ \theta _ { H } , x _ { H } \}$ in the market is , and the proportion of low-type users, denoted by $\left\{ \theta _ { L } , x _ { L } \right\}$ , is $1 - \alpha$ . The market consists of both types of users, that is, $\alpha \in ( 0 , 1 )$ . Our setting of a market with two types of users is sufficient to obtain useful insights of a monopolist’s product-pricing decisions (Laffont and Martimort 2002, p. 31; Chellappa and Shivendu 2005; Wu and Chen 2008). Later, in $\bar { 8 } \bar { 5 } . 2$ we extend our analysis to a market with N types of users.

A user evaluates software by taking into consideration not only the benefit from functionality that is present in the software but also the inconvenience or disutility from those functionality that are required by her but are not provided in the software. To that extent, in our conceptualization, a user derives utility from software in two distinct parts. This conceptualization has some similarity to Chellappa and Shivendu (2010), in which consumers evaluate utility from personalization services in two parts, benefit from personalization services and disutility from loss of privacy as they use personalization services.

First, part of a user’s utility is benefit derived from the functionality available in the software, which is given by $\theta f ( q )$ , where function $f ( q )$ maps software functionality to benefit. We assume $f ( q )$ is continuous and differentiable $\forall q > 0 ,$ , users’ benefit increases at a nonincreasing rate as functionality level of the software increases: $\partial { f ( q ) } / \partial q > 0$ and $\partial ^ { 2 } f ( q ) / \partial q ^ { 2 } \leq 0 ,$ , and $f ( 0 ) = 0 .$ Since in our setup users do not derive any additional benefit if the level of functionality in software is greater than their required level of functionality, we define two benefit functions: $f _ { H } ( q )$ for high-type users and $f _ { L } ( q )$ for low-type users, where $f _ { H } ( q ) = \dot { f ( q ) } \forall q \in [ 0 , x _ { H } )$ and $f _ { H } ( q ) = f ( \bar { x _ { H } } ) \ \forall \ q \geq x _ { H } ,$ , and $f _ { L } ( q ) = f ( q ) \forall q \in [ 0 , x _ { L } )$ and $f _ { L } ( q ) = f ( x _ { L } ) \ \forall q \geq x _ { L }$ . Hence, the benefit from functionality to high-type users is given by $\theta _ { H } f ( q ) \forall q \in$ $[ 0 , x _ { H } )$ and $\theta _ { H } f ( x _ { H } ) \ \forall q \geq x _ { H }$ and the benefit from functionality to low-type users is given by $\theta _ { L } f ( q ) \forall q \in$ $[ 0 , x _ { L } )$ and $\theta _ { L } f ( x _ { L } ) \ \forall q \geq x _ { L }$ (Figure 1, left plot). The linear utility function used in the literature (Mussa and Rosen 1978, Moorthy and Png 1992, Chellappa and Shivendu 2003) with $f ( q ) = a q ,$ , where a is a constant, is a special case of our conceptualization of users’ benefit from software functionality without an upper bound.

Second, part of a user’s utility function is inconvenience or disutility that she experiences because some functionality that she requires is not available in the software. We capture a user’s disutility from underprovisioning by a function $g ( x _ { i } , q )$ , where $i \in \{ H , L \}$ We assume that the function $g ( x _ { i } , q )$ is continuous and differentiable $\forall q \in ( 0 , x _ { i } )$ , where $i \in \{ H , L \}$ and a user experiences zero disutility when the functionality level of the software is the same or greater than her required level, that is, $g ( x _ { i } , q ) | _ { q \geq x _ { i } } = 0 , i \in \{ H , L \}$ (Figure 1, left plot). Users’ disutility from underprovisioning decreases at a nondecreasing rate as the software functionality level $( q )$ increases: $\partial g ( x _ { i } , q ) / \partial q < 0$ and $\partial ^ { 2 } g ( x _ { i } , q ) / \partial \bar { q ^ { 2 } } \geq 0 , \forall \bar { q } \in ( 0 , x _ { i } )$ , where $i \in \{ H , L \}$ . This implies that as the functionality increases, users experience less inconvenience and the rate of reduction of inconvenience decreases. In other words, users’ sensitivity to underprovisioning decreases as the software functionality level gets closer to their required level of functionality.

On the other hand, users experience an increase in disutility at a nondecreasing rate as their required level of functionality 4x5 increases: $\partial g ( x _ { i } , q ) / \bar { \partial x } _ { i } > 0$ and $\partial ^ { 2 } g ( x _ { i } , q ) / \partial x _ { i } ^ { 2 } \geq ^ { 2 } 0 , \forall q \in ( 0 , x _ { i } )$ , where $i \in \{ H , L \}$ This is because as the gap between the required level of functionality and functionality in the software increases, inconvenience to users increases. In other words, given a functionality level $( q \in ( 0 , x _ { i } ) )$ in the software, users’ sensitivity to underprovisioning increases as their required level of functionality increases. Furthermore, users who have a higher required level of functionality experience a greater reduction in inconvenience as the software functionality level increases: $\partial ^ { 2 } g ( x _ { i } , q ) / \partial x _ { i } \partial q < 0 \ \forall q \in ( 0 , x _ { i } )$ , where $i \in \{ H , L \}$ . In other words, high-type users experience more inconvenience compared with low-type users as software functionality decreases because they are more sensitive to underprovisioning. In the context of our example of the statistician and the student, if the software does not provide the functionality of copy and paste cells, then the statistician incurs more inconvenience than the student.

Figure 1 User Benefit from Functionality, Inconvenience from Underprovisioning of Functionality, and Utility  
![](/api/attachments/R6GA9SEW/fulltext/images/4e985a9f55b6737eb3b15d52f08c3ed642beb97cd6780c17d05f5a3c6d2f2a02.jpg)

Users evaluate software by taking into consideration the benefit from functionality and also the inconvenience or disutility from underprovisioning. They derive zero utility if the benefit from functionality is less than the inconvenience from underprovisioning. We write the utility function as

$$
\begin{array}{r l} U _ {i} (\theta_ {i}, x _ {i}, q) = \left\{ \begin{array}{l l} \max \{\theta_ {i} f (q) - g (x _ {i}, q), 0 \} & \text { if } q <   x _ {i} \\ \theta_ {i} f (x _ {i}), & \text { if } q \geq x _ {i} \end{array} \right. \\ i \in \{H, L \}. \end{array}\tag{1}
$$

Note that the utility function in (1) is similar to Chellappa and Shivendu (2010) in conceptualizing utility in two parts, namely, the benefit from functionality and disutility from underprovisioning, but it has two key differences from their nonmonotonic concave utility function. First, in our setup, users with heterogeneous required levels of functionality experience less disutility from underprovisioning as the level of functionality in the software gets closer to their required level of functionality. Moreover, users experience no disutility if the level of functionality in the software is equal to or more than their required level. However, in their paper, users with a heterogeneous concern for privacy incur more disutility from the loss of privacy as they use more personalization services.<sup>9</sup> Second, in our setup, users are heterogeneous in marginal valuation for functionality (benefit from functionality), whereas in their setup users are homogeneous in valuation for services (benefit from services).

Figure 1 illustrates the conceptualization of our utility function (1). The left plot describes the increase in the benefit and decrease in the inconvenience or disutility from the increasing functionality for both types of users. The right plot describes the utility function $U ( \cdot )$ for both types of users, which is nonnegative. Since both utility curves increase at a nonincreasing rate in functionality, it implies that these two curves only cross once at $q = q ^ { \prime }$ . A formal definition follows.

![](/api/attachments/R6GA9SEW/fulltext/images/c402d5abc3d1600bdf449886ad4f64853f5253ac3d76b172d8b7d5976fc53bb0.jpg)

<sup>Definition</sup> <sup>1.</sup> “Indifferent functionality level” is a functionality level $q ^ { \prime }$ at which both high-type and low-type users derive the same utility, that is, $U _ { H } ( q ^ { \prime } ) = \dot { U _ { L } } \hat { ( } q ^ { \prime } )$

Note three key characteristics of the user utility function in (1): (a) utility is monotonically increasing at a decreasing rate in functionality for high-type as well as for low-type users up to their respective required levels of functionality in the region where utility is positive. This conceptualization has some similarity to quadratic utility functions employed in the IS literature (Raghunathan 2000, Sundararajan 2004). (b) Users’ utility remains constant for any functionality level higher than their required level, which is similar to Ghose and Sundararajan (2005) and the hierarchical case of Wei and Nault (2014). (c) The Spence-Mirrlees Single-Crossing Condition is satisfied, that is $\partial ^ { 2 } U _ { i } ( \theta _ { i } , x _ { i } , q ) / \partial { \bar { \theta } } _ { i } \partial q > 0$ and $\partial ^ { 2 } U _ { i } ( \theta _ { i } , x _ { i } , q ) / \partial x _ { i } \partial q > 0 .$ $\forall q < x _ { i }$ and $U _ { i } ( \theta _ { i } , x _ { i } , q ) > 0$ , where $i \in \{ H , L \}$ . The key difference between our model and previous quadratic utility models in IS (Raghunathan 2000, Sundararajan 2004, Ghose and Sundararajan 2005) is that in their models the utility maximizing functionality level depends only on the user’s marginal valuation for functionality, whereas, in our model, the utility maximizing functionality level depends on another parameter, that is, users’ required level of functionality (x5.

Now we turn our attention to a software firm’s product-pricing strategy. Following versioning literature in IS (Bhargava and Choudhary 2001, 2008; Chen and Seshadri 2007; Chellappa and Shivendu 2005; Wei and Nault 2014; Wu and Chen 2008; Lahiri et al. 2013) we consider a monopolistic market setting.<sup>10</sup> A software firm may offer different versions of the software, which differ only in the level of functionality. High version software has a higher level of functionality compared with the low version, which has a subset of functionality of the high version and to that extent versions are upward compatible (Raghunathan 2000). Without loss of generality, we assume that the high version has all of the functionality that the software firm has developed and the low version has a subset of the functionality of the high version.

Following the literature (Wei and Nault 2008, Chellappa and Shivendu 2005), we assume that the development cost of the first copy of the software, $c ( q ) .$ , is continuous, differentiable, and convex in the functionality level of the highest version of the software, $\partial c ( q ) \dot { / } \partial q > 0$ and $\partial ^ { 2 } c ( q ) / \partial q ^ { 2 } > 0 \forall q$ . The convex cost of producing functionality is consistent with the real-world software development process where incorporating additional functionality in software requires more design and testing effort at an increasing rate (Chen and Seshadri 2007). The firm develops the high version of the software with the largest set of functionality and removes some functionality, without incurring any additional cost, to create the low version (Ghose and Sundararajan 2005, Wei and Nault 2014). Furthermore, there is no variable cost of producing additional copies of the high- or low-version software and all upfront R&D investment is sunk.

Before we analyze the firm’s optimal product-pricing strategy, we make the following two assumptions to focus our analysis to a market where high-type users are attracted to the low version and the cost of producing functionality is not too high.

<sup>Assumption</sup> <sup>1.</sup> (a) High-type users have a higher utility than low-type users for the software that has a required level of functionality of low-type users. (b) The lowest functionality level at which high-type users derive nonzero utility is higher than the lowest functionality level at which low-type users derive nonzero utility.

In other words, Assumption 1(a) means that $U _ { H } ( \theta _ { H } , x _ { H } , x _ { L } ) > U _ { L } ( \theta _ { L } , x _ { L } , \bar { x _ { L } } )$ . This assumption ensures that the software version that gives maximum utility to low-type users gives higher utility to hightype users. It allows us to exclude the trivial case where high-type users have no incentive to buy the low-version with functionality $q = x _ { L }$ . Assumption 1(b) ensures that there is some feasible version of software for which low-type users’ utility is higher than that of high-type users’ (Figure 1, right plot).

<sup>Assumption</sup> <sup>2.</sup> The marginal cost of developing functionality is relatively small such that the highest functionality level that the firm develops $( q ^ { * } )$ is greater than the low-type users’ required level of functionality, that is, $q ^ { * } > x _ { L } . ^ { 1 1 }$

Assumption 2 implies that irrespective of the firm’s product strategy, the rate of increase of utility from functionality is greater than the rate of increase of the cost of producing functionality at the low-type users’ required level of functionality. Since the rate of increase of utility is higher than the rate of increase of cost at $q = x _ { L } .$ , the optimal level of functionality developed by the firm is higher than $x _ { L } .$ . This assumption excludes the noninteresting case where the firm underprovides to low-type users because of the high cost of producing functionality.

## 2.1. Firm’s Product-Price Strategies

The monopolist software firm can adopt one of the two broad product-price strategies: sell only one version or sell two versions. We analyze these two strategies in the following subsections.

2.1.1. Single Version Strategy. When the software firm sells a single version, it creates one version and can set a price such that (i) only high-type users buy, or (ii) both types of users buy, or (iii) only low-type users buy. Note that from Assumption $\dot { 2 } ,$ the firm produces a functionality level, which is higher than the required level of functionality of low type, $q ^ { * } > x _ { L }$ (see Figure 1, right plot). From Assumption 1, we know $\bar { U } _ { H } ( q = x _ { L } ) ^ { } > \bar { U } _ { L } ( q = x _ { L } )$ . This implies that for any functionality level, which is higher or equal to the required level of functionality of low-type users, high-type users have higher utility than low-type users. Therefore, if the firm sets a price such that low-type users buy, then high-type users always buy at that price. Hence, selling a single version only to low-type users (strategy (iii)) is not feasible.

Under strategy (i), the firm produces software of functionality level $q _ { H }$ and sets price $p _ { H }$ such that only high-type users buy. The firm’s profit function is

$$
\pi_ {H} (q _ {H}, p _ {H}) = \alpha p _ {H} - c (q _ {H}),\tag{2}
$$

and the firm’s optimization problem is

$$
\begin{array}{l l} \max _ {q _ {H}, p _ {H}} & \pi_ {H} (q _ {H}, p _ {H}) \\ \text { subject   to } & \text { IR   (L: not   buy):   U_{L} (\theta_{L} , x_{L} , q_{H}) - p_{H} <  0,} \\ & \text { IR   (H: buy):   U_{H} (\theta_{H} , x_{H} , q_{H}) - p_{H} \geq 0.} \end{array}
$$

Note that IR (L) ensures that low-type users do not buy and IR (H) ensures that high-type users buy the single version. Since there is only one version, we do not consider individual compatibility constraints (ICs).

From Assumption $^ { 2 , }$ we know that the highest optimal functionality is $q ^ { * } > x _ { L }$ . This implies that $q _ { H } > x _ { L }$ . Since the utility of high-type users increases but the utility of low-type users does not increase as the functionality level increases beyond $x _ { L } ,$ , we have $U _ { H } ( q = q _ { H } ) >$ ${ \dot { U } } _ { H } ( q = x _ { L } )$ , and $U _ { L } ( q = q _ { H } ) = U _ { L } ( q = x _ { L } )$ . From Assumption 1, we know $U _ { H } ( q = x _ { L } ) > U _ { L } ( q = x _ { L } )$ . Hence, $U _ { H } ( q = q _ { H } ) > U _ { L } ( q = q _ { H } )$ . Therefore, the IR (H) must be binding, i.e., $p _ { H } = U _ { H } ( \theta _ { H } , x _ { H } , q _ { H } )$ and this ensures that IR (L) is satisfied.

Under strategy (ii), the firm produces software of functionality level $q _ { A }$ and sets price $p _ { A }$ such that both types of users buy. The firm’s profit function is

$$
\pi_ {A} (q _ {A}, p _ {A}) = p _ {A} - c (q _ {A}),\tag{3}
$$

and the firm’s optimization problem is

$$
\begin{array}{l l} \max _ {q _ {A}, p _ {A}} & \pi_ {A} (q _ {A}, p _ {A}) \\ \text { subject   to } & \text { IR   (L: buy): } U _ {L} (\theta_ {L}, x _ {L}, q _ {A}) - p _ {A} \geq 0, \\ & \text { IR   (H: buy): } U _ {H} (\theta_ {H}, x _ {H}, q _ {A}) - p _ {A} \geq 0. \end{array}
$$

Note that IR (L) and IR (H) ensure that both types of users buy. Since the utility of the low-type user does not increase when the functionality level increases beyond $x _ { L } ,$ , the maximum utility of low-type is $U _ { L } ( \theta _ { L } , x _ { L } , q = x _ { L } )$ . From Assumption 2, we know that the highest optimal functionality $q ^ { * } > x _ { L } ,$ , therefore the firm offers $q _ { A } = x _ { L }$ . When the firm sells to both types of users, the maximum price that it can set is $U _ { L } ( \theta _ { L } , x _ { L } , q = x _ { L } )$ . From Assumption 1, at that price, high-type users also buy. The firm sets the price such that IR (L) is binding and Assumption 1 ensures that IR (H) is satisfied.

2.1.2. Versioning Strategy. When the firm adopts a versioning strategy, it develops a high version with the highest functionality level and then creates a low version by disabling some functionality of the high version. The firm sells these two versions (a high version and a low version) at different prices and users selfselect to buy the version of their choice. The firm’s profit function is

$$
\pi_ {V} (p _ {V H}, p _ {V L}, q _ {V H}, q _ {V L}) = \alpha p _ {V H} + (1 - \alpha) p _ {V L} - c (q _ {V H}),\tag{4}
$$

and the firm’s optimization problem is

$$
\max _ {p _ {V H}, p _ {V L}, q _ {V H}, q _ {V L}} \pi_ {V} (p _ {V H}, p _ {V L}, q _ {V H}, q _ {V L})
$$

subject to

IR (H: buy high version):

$$
U _ {H} (\theta_ {H}, x _ {H}, q _ {V H}) - p _ {V H} \geq 0,
$$

IR (L: buy low version):

$$
U _ {L} (\theta_ {L}, x _ {L}, q _ {V L}) - p _ {V L} \geq 0,
$$

IC (H: buy high version):

$$
U _ {H} (\theta_ {H}, x _ {H}, q _ {V H}) - p _ {V H} \geq U _ {H} (\theta_ {H}, x _ {H}, q _ {V L}) - p _ {V L},
$$

IC (L: buy low version):

$$
U _ {L} (\theta_ {L}, x _ {L}, q _ {V L}) - p _ {V L} \geq U _ {L} (\theta_ {L}, x _ {L}, q _ {V H}) - p _ {V H}.
$$

These four constraints ensure that high-type users buy the high version and low-type users buy the low version. We know that the firm pays information rent to high-type users to incentivize them to buy the high version and not shift to the low version. Therefore, IR (H: buy high version) is always satisfied. Moreover, since it is the high-type users who need to be provided incentives to buy the version targeted to them, IC (L: buy low version) must be satisfied. Hence, we are left with IR (L: buy low version) and IC (H: buy high version). It is easy to see that the firm’s optimal pricing strategy requires that these two constraints bind. This is because by binding IR (L: buy low version), the firm saves on information rent to be paid to high-type users, and by binding IC (H: buy high version) the firm ensures that it does not overpay information rent.

In §3 we analyze optimal functionality and prices set by the software firm under different product-pricing strategies and compare profits to identify the optimal strategy.

## 3. Optimal Product-Pricing Strategy

Before we examine the firm’s profits under different product-pricing strategies given in §2.1, we first consider some characteristics of the utility function in (1) and the optimal functionality level under different product-pricing strategies. Since high-type users have a higher required level of functionality $( x _ { H } > x _ { L } )$ , they are more sensitive to underprovisioning of functionality (compared to low-type users), in the region in which their utility is positive (see Figure 1). The following Lemma gives an important result relating to the indifferent level of functionality q<sup>0</sup>(see Definition 1).

<sup>Lemma</sup> <sup>1.</sup> When users experience heterogeneous disutility from underprovisioning of functionality, the indifferent functionality level is such that $\mathrm { ( i ) } \ \check { q } ^ { \prime } > 0$ and (ii) $\dot { U _ { H } ( \theta _ { H } , x _ { H } , q ^ { \prime } ) = U _ { L } ( \theta _ { L } , x _ { L } , q ^ { \prime } ) } > 0 .$

For all proofs, see Online Appendix B (available as supplemental material at http://dx.doi.org/10.1287/ isre.2015.0597).

From Assumption 1(b), high-type users get positive utility from software at a higher functionality level than low-type users. When the software has the same functionality as the high-type users’ required level of functionality $( q = x _ { H } )$ , then high-type users derive higher utility from the software compared to low-type users, $U _ { H } = \mathbf { \bar { \theta } } _ { H } f ( x _ { H } ) > U _ { L } = \theta _ { L } f ( x _ { L } )$ , because $x _ { H } > x _ { L }$ and $\theta _ { H } > \theta _ { L }$ . Furthermore, since for both types of users utility is monotonically nondecreasing in the level of functionality, there exists a functionality level $q ^ { \prime } > 0 ,$ at which both types of users derive the same positive utility from the software.

Before deciding the functionality-price menu under different product strategies, the firm determines the highest level of functionality to produce under each strategy. In our model, the utility derived by high-type users does not increase if the software’s functionality level is higher than the high-type user’s required level, that is, if $q > x _ { H }$ . This implies that an increase in the level of functionality beyond the required level $x _ { H }$ does not lead to any increase in high-type user’s utility. Nonetheless, the firm incurs a higher development cost for developing a higher level of functionality. Therefore, it is never optimal for the firm to develop the level of functionality of the high-version higher than $x _ { H }$

<sup>Lemma</sup> <sup>2.</sup> (A) When the firm adopts the product strategy of selling one version only to high-type users, the optimal level of functionality $q _ { H } ^ { * }$ solves the first-order condition given by $\alpha \theta _ { H } f ^ { \prime } ( q _ { H } ^ { * } ) - \alpha g ^ { \prime } ( x _ { H } , q _ { H } ^ { * } ) - c ^ { \prime } ( q _ { H } ^ { * } ) = 0 .$ . The optimal level of functionality is bound such that $x _ { L } < q _ { H } ^ { * } \leq x _ { H }$ and it increases within this bound as the proportion of high-type users () increases. (B) When the firm adopts the product strategy of selling one version to both types of users, the optimal level of functionality is the same as the low-type users’ required functionality level, that is, $q _ { A } ^ { * } = x _ { L }$ . (C) When the firm adopts a versioning strategy, the highest level of functionality is the same as in (A), that is, $q _ { V H } ^ { * } = q _ { H } ^ { * }$

When the software firm adopts the product strategy of selling only to high-type users, the optimal functionality is set at the level at which the marginal cost of producing functionality equals the marginal utility of functionality to high-type users, weighted by the proportion of high-type users in the market. As the proportion of high-type users increases, the firm increases the level of functionality of software because the increase in revenue outweighs the increase in development cost of additional functionality. When the firm adopts the product strategy of selling to both types of users, the maximum price that the firm can charge is the maximum utility of low-type users. From Assumption 2, we know that the highest optimal functionality is $q ^ { * } > x _ { L }$ . Since under this product strategy, the firm cannot charge a higher price by producing functionality beyond the low-type users’ required level of functionality, the optimal functionality level is $q _ { A } ^ { * } = x _ { L }$

When the software firm adopts a versioning strategy, the optimal functionality level of the high version is the same as the optimal functionality level given in Lemma 2(A). The economic intuition behind this result is as follows: When the firm adopts a versioning strategy, then the firm first develops the highest functionality level and targets it to high-type users, and then it removes some functionality from the high version of the software to create the low version of the software and targets that to low-type users. The optimal level of functionality of the high version is determined by the trade-off between the marginal benefit of functionality to high-type users and the marginal cost of producing functionality. Since this trade-off is the same under the option of selling only to high-type users or adopting a versioning strategy, the optimal highest functionality level produced under both options (Lemma 2(A) and Lemma 2(C)) is the same.

Under the versioning strategy, the firm has to ensure that each type of user buys the version targeted to them. Since for any functionality level greater than $q ^ { \prime } ,$ high-type users have a higher utility than low-type users, only they may consider switching to the low version. To make them indifferent between buying the high version and switching to the low version, the firm needs to provide them some incentive or information rent.

<sup>Proposition</sup> <sup>1.</sup> Under a versioning strategy, the software firm’s optimal level of functionality of the low version is bounded between the indifferent functionality level and the required level of functionality of the low-type user, that is, $q ^ { \prime } \leq q _ { V L } ^ { * } \leq x _ { L }$

When the functionality level of the low version is $q ^ { \prime } ,$ then the firm pays no information rent to high-type users because at that functionality level both types of users derive the same utility. If the firm offers the low version at a level of functionality lower than $q ^ { \prime } ,$ then the firm loses revenue from low-type users and also does not gain revenue from high-type users by saving information rent (which is zero at $q ^ { \prime } )$ . Therefore, the firm never lowers the functionality of the low version below the indifferent functionality level, that is, $q _ { V L } ^ { * } \geq q ^ { \prime }$

On the other hand, if the firm offers the low version with functionality higher than the low-type users required level, then the firm cannot increase the price of the low version because their utility does not increase for functionality level beyond $x _ { L }$ . Hence the firm does not gain any additional revenue from low-type users. Furthermore, the firm has to pay higher information rent to high-type users because their gain from switching to the low version increases. This results in a net loss to the firm. Therefore, the firm never offers the low version with a functionality level higher than the low-type users’ required level of functionality, that is, $q _ { V L } ^ { * } \leq x _ { L }$

<sup>Lemma</sup> <sup>3.</sup> When users experience heterogeneous disutility from underprovisioning of functionality, then under a versioning strategy, the optimal functionality level of the low version depends on the proportion of high-type users in the market. (A) When $\alpha \in ( 0 , \alpha _ { 2 } )$ , the optimal functionality level of the low version is $q _ { V L } ^ { * } = x _ { L } . \ ( \mathrm { B } )$ When $\alpha \in \left[ \alpha _ { 2 } , \alpha _ { 1 } \right]$ the optimal functionality level of the low version is bound within $[ q ^ { \prime } , x _ { L } ] ,$ such that $q _ { V L } ^ { * }$ solves the first-order condition: $( \theta _ { L } f ^ { \prime } ( q _ { V L } ^ { * } ) - g ^ { \prime } ( x _ { L } , q _ { V L } ^ { * } ) ) \stackrel {  } { - \alpha } ( \theta _ { H } f ^ { \prime } ( q _ { V L } ^ { * } ) - g ^ { \prime } ( x _ { H } , q _ { V L } ^ { * } ) ) = 0$ (C) When $\alpha \in ( \alpha _ { 1 } , 1 )$ , the optimal functionality level of the low version is $q _ { V L } ^ { * } = q ^ { \prime }$ . The two threshold values of proportion of high-type users are upper threshold proportion

$$
\alpha_ {1} = \frac {\theta_ {L} f ^ {\prime} (q ^ {\prime}) - g ^ {\prime} (x _ {L} , q ^ {\prime})}{\theta_ {H} f ^ {\prime} (q ^ {\prime}) - g ^ {\prime} (x _ {H} , q ^ {\prime})}
$$

and lower threshold proportion

$$
\alpha_ {2} = \frac {\theta_ {L} f ^ {\prime} (x _ {L})}{\theta_ {H} f ^ {\prime} (x _ {L}) - g ^ {\prime} (x _ {H} , x _ {L})}.
$$

Lemma 3 characterizes the optimal functionality level of the low version under a versioning strategy. This optimal functionality level depends on two critical proportions of high-type users in the market, $\alpha _ { 1 }$ and $\alpha _ { 2 }$ The optimal functionality level of the low version is $x _ { L }$ as long as there are relatively fewer high-type users in the market, that is, $\alpha \in ( 0 , \bar { \alpha _ { 2 } } ]$ . The economic intuition is that in this range, there are relatively more lowtype users, thus the marginal benefit of functionality from low-type users is greater than the marginal loss from information rent to be paid to high-type users to maintain incentive compatibility. Therefore, it is optimal for the firm to offer the low-version software at the highest possible functionality level for that version, $x _ { L }$ (Figure 2). We characterize this critical proportion of high-type users, $\alpha _ { 2 } ,$ as the lower threshold proportion. Hence, when the proportion of high-type users in the market is lower than the lower threshold proportion ( ), there is no underprovisioning of functionality in the low version of software $( q _ { V L } ^ { * } = x _ { L } )$

When the proportion of high-type users in the market is moderate, $\alpha \in [ \alpha _ { 2 } , \alpha _ { 1 } ] ,$ , then the firm makes a tradeoff between the marginal revenue from low-type users and the marginal information rent to high-type users by adjusting the functionality level of the low version. The firm reduces functionality of the low version from its upper bound $x _ { L }$ as the proportion of hightype users increases (Figure 2). This is because as the proportion of high-type users increases, functionality of the low version is distorted downward to save on information rent. When the proportion of high-type users is relatively large in the market, $\alpha \in ( \alpha _ { 1 } , 1 )$ , the firm is better off by setting the functionality level of the low version at its lower bound, that ${ \mathrm { i } } \mathbf { s } ,$ at the indifferent functionality level $q ^ { \prime }$ where information rent to high-type users is zero. We characterize this critical proportion of high-type users, $\alpha _ { 1 } ,$ as the upper threshold proportion. Hence, when the proportion of high-type users in the market is higher than the upper threshold proportion $\left( \alpha _ { 2 } \right)$ , the underprovisioning of functionality in the low version of the software is most severe $( q _ { V L } ^ { * } = q ^ { \prime } )$ .

Figure 2 Optimal Functionality Level of the Low Version as the Proportion of High-Type Users’ Changes  
![](/api/attachments/R6GA9SEW/fulltext/images/52e5ccd93c0867a15c08eb5096c0c4d797e84870a96a8666406041e8a1d5b71d.jpg)

Now we focus on comparing profits under different product strategies. Note that under the strategy of selling the high version only to high-type users, market coverage is partial. On the other hand, under the strategy of selling one version to both types of users and under the versioning strategy the market is fully covered. Under the versioning strategy, the firm’s ability to charge a high price for the high version is limited because of the potential of cannibalization between versions (Raghunathan 2000, Belleflamme et al. 2003). The firm provides information rent to high-type users such that they receive the same net surplus from buying either of the versions, and therefore, do not switch from buying the high version to the low version. Yet low-type users do not find the highversion attractive and buy the low version. As the level of functionality offered to low-type users decreases (from $x _ { L } )$ , revenue from low-type users decreases, but revenue from high-type users increases because the firm pays less information rent. The firm determines an optimal level of functionality of the low version (Lemma 3) and the price of the high version by making a trade-off between these two opposite effects.

Proposition 2 (Sufficient Condition for Optimality of the Versioning Strategy). <sub>In</sub> <sub>a</sub> <sub>vertically</sub> differentiated market where users have heterogeneous required levels of functionality, if users experience disutility from underprovisioning of functionality, then the versioning strategy is always optimal.

The economic intuition of Proposition 2 is as follows. When $\alpha \in ( 0 , \alpha _ { 2 } )$ , the functionality level of the low version is $x _ { L } ,$ , under a versioning strategy (Lemma 3(A)). Therefore, in this region, compared with the product strategy of selling to both types of users, a versioning strategy has the same revenue from low-type users, but higher revenue from high-type users, after adjusting for a higher development cost for a high level of functionality. Hence, in this region, a versioning strategy dominates the strategy of selling to both types of users. As the proportion of high-type users in the market increases, the optimal revenue under a versioning strategy increases but the optimal revenue under a strategy of selling to both types of users remains constant. Therefore, when the proportion of high-type users is relatively higher, $\alpha \in [ \alpha _ { 2 } , 1 )$ , the versioning strategy also dominates the strategy of selling to both types of users (Figure 3).

Figure 3 Profits Under the Three Product Strategies When User Experience Disutility from Underprovisioning of Functionality  
![](/api/attachments/R6GA9SEW/fulltext/images/032b20fc2dbded33335f9ed48be95b6361b96f0e5f9bc142169ca63498f6cea8.jpg)

Now we compare the optimal profit under a versioning strategy with the optimal profit under a strategy of selling a single version only to high-type users. Since the firm may have to provide some information rent to high-type users under a versioning strategy, the price of the high version may be lower compared to a strategy of selling only to high-type users, even though the optimal functionality level of the high version is the same under both product strategies $( q _ { V H } ^ { * } = q _ { H } ^ { * } )$ Consequently, the revenue from high-type users under a versioning strategy is lower than that under a strategy of selling a single version only to high-type users. Yet the gain in revenue from low-type users under a versioning strategy more than compensates for this loss of revenue from high-type users, when the proportion of high-type users is relatively low, $\alpha \in ( 0 , \alpha _ { 1 } ]$

On the other hand, when the proportion of high-type users is relatively high, $\alpha \in ( \alpha _ { 1 } , 1 )$ , the firm sets the optimal functionality level of the low-version at $q ^ { \prime }$ (Lemma 3(C)), and therefore, does not pay information rent to high-type users. This implies that the price of the high version is the same as under the strategy of selling a single version only to high-type users. Hence, under a versioning strategy, the firm generates the same revenue from high-type users and some additional revenue from low-type users. Therefore, optimal profit is higher under a versioning strategy compared with that under a product strategy of selling only to high-type users. Figure 3 graphically shows profits under the three product-price strategies and the dominance of a versioning strategy.

## 4. Impact of Increase in Users’ Required Level of Functionality

With the rapid technological changes, users’ requirements for software functionality and computing needs are changing at a fast pace. One would expect that the required level of functionality of both types of users will increase over a period of time, though users valuation of functionality may not change. In this section, we discuss the impact of increase in users required level of functionality, $x _ { H }$ or $x _ { L } ,$ one at a time, on the firm’s versioning strategy.

<sup>Lemma</sup> <sup>4.</sup> As the required level of functionality of hightype users $( x _ { H } )$ increases, (i) the indifferent functionality level $q ^ { \prime }$ increases, and (ii) the optimal level of functionality of the high-version $q _ { V H } ^ { * }$ increases.

As high-type users required functionality level increases they become more sensitive to underprovisioning of functionality. They experience more inconvenience or disutility for any functionality level lower than their previous required level of functionality, and therefore, their utility decreases. On the other hand, there is no impact on the low-type users’ utility when $x _ { H }$ increases. This is illustrated in Figure $^ { 4 , }$ left plot, where the required level of functionality of high-type users increases from $x _ { H A }$ to $x _ { H B }$ $( x _ { H A } < x _ { H B } )$ Since high-type users are more sensitive to underprovisioning of functionality, they get the same utility as low-type users at a higher functionality level. This leads to shifting of the intersection point of the two utility curves to the right. Therefore, the indifferent functionality level, $q ^ { \prime } .$ , increases as $x _ { H }$ increases (see Figure $4 , q _ { A } ^ { \prime } > q _ { B } ^ { \prime } )$

For the rest of the analysis, we assume that the increase in $x _ { H }$ is not large and Assumption 1(a) continues to hold, that is, $U _ { H } ( \theta _ { H } , x _ { H B } , x _ { L } ) > U _ { L } ( \theta _ { L } , x _ { L } , x _ { L } )$ Moreover, since there is no change in the required level of functionality of low-type users, Assumption 2 $( q ^ { * } > x _ { L } )$ continues to hold. Moreover, since high-type users are more sensitive to disutility from underprovisioning, the lowest functionality level at which hightype users derive nonzero utility increases. Therefore, Assumption 1(b) continues to hold.

The firm increases the high-version’s functionality level, $q _ { V H } ^ { * } ,$ as high-type users’ required level of functionality increases. The economic intuition is that as $x _ { H }$ increases, the marginal effect of functionality on high-type users’ utility increases, though the marginal development cost remains the same. Therefore, the firm increases the high-version’s functionality level.

Figure 4 Utility Curves for Both Types of Users, and the Optimal Functionality Level of the Low Version as Required Functionality Level of High-Type Users Increases Where $f ( q ) = q , g ( x , q ) = ( x - q ) ^ { 2 } , c ( q ) = q ^ { 2 }$ , and ${ \cal X } _ { H A } < { \cal X } _ { H B }$  
![](/api/attachments/R6GA9SEW/fulltext/images/61c92fea208ec2f8f1092ae803800c8f426054dd55eb1114bc0ed3f34dfd0fd7.jpg)

![](/api/attachments/R6GA9SEW/fulltext/images/292c8c8dddf3f5bd54ad543ecfa57040885524def790f2a3b37436eff811e72e.jpg)

<sup>Proposition</sup> <sup>3.</sup> As the required level of functionality of high-type users $x _ { H }$ increases, (i) the lower threshold proportion $\alpha _ { 2 }$ and the upper threshold proportion $\alpha _ { 1 }$ decrease, (ii) the optimal functionality of the low-version $q _ { V L } ^ { * }$ (a) does not change if the proportion of high-type users is small, (b) decreases if the proportion of high-type users is moderate, and (c) increases if the proportion of high-type users is large.

When high-type users’ required functionality level increases, they become less attracted to the low version, because they experience more inconvenience or more disutility from underprovisioning. Therefore, the firm needs to pay lower information rent to make high-type users indifferent to switching to the low version. This implies that by reducing the low-version functionality level from the low-type users’ required level, the marginal gain from saving on information rent increases, but the marginal loss of revenue from lowtype users remains the same. Thus, the firm reduces the low-version functionality level from the low-type users required functionality level, $x _ { L } ,$ , when there are relatively fewer high-type users in the market, that is, at a lower $\alpha _ { 2 }$ . This is illustrated in Figure $^ { 4 , }$ right plot, where $\alpha _ { 2 B } < \alpha _ { 2 A } .$ . Note that it also implies that the firm reduces the low-version functionality at a faster rate as  increases. Combining these two factors—an increase in the indifferent functionality level, $q _ { B } ^ { \prime } > q _ { A } ^ { \prime }$ (Lemma 4), and a faster decrease of high-type users’ utility with functionality—the firm offers the low version with functionality at $q _ { B } ^ { \prime }$ when there are relatively fewer high-type users in the market, that is, at a lower $\alpha _ { 1 }$ (Figure 4, right plot, $\alpha _ { 1 B } < \alpha _ { 1 A } )$

As discussed above, when $x _ { H }$ increases, both the upper threshold proportion $\alpha _ { 1 }$ and the lower threshold proportion $\alpha _ { 2 }$ decrease, but the impact on the functionality level of the low version is mixed. If there are few high-type users in the population (small $\alpha ) ,$ low-type users continue to receive the same level of functionality $x _ { L } ,$ when $x _ { H }$ increases. This occurs simply because there are not enough high-type users to make any impact on the trade-off between information rent and revenue from low-type users. When there are a relatively moderate number of high-type users, the firm lowers the functionality level of the low version. This is because high-type users are now more sensitive to changes in the functionality level of the low version, and the firm gains more revenue through a reduction in information rent by decreasing the functionality of the low version than the loss of revenue from low-type users.

On the other hand, when the proportion of high-type users is relatively high, the functionality level of the low version increases as $x _ { H }$ increases. Recall that when the proportion of high-type users is relatively high, low-type users get the low version at the indifferent functionality level $q ^ { \prime }$ because the firm pays zero information rent. Lemma 4 states that the indifferent quality level increases, $q _ { B } ^ { \prime } > q _ { A } ^ { \prime }$ as $x _ { H }$ increases, and therefore, the firm increases the functionality level of the low version when $\alpha$ is relatively high. Figure 4 illustrates the three possible scenarios, low-type users get higher functionality level when $\alpha _ { H A B } < \alpha < 1 .$ , lower functionality level when $\alpha _ { 2 B } < \alpha < \alpha _ { H A B } ,$ and no change in functionality level when $0 < \alpha < \alpha _ { 2 B }$

<sup>Lemma</sup> <sup>5.</sup> As the required level of functionality of lowtype users $( x _ { L } )$ increases, (i) the indifferent functionality level $q ^ { \prime }$ decreases, and (ii) there is no impact on the optimal level of functionality of high-version $q _ { V H } ^ { * }$

An increase in the low-type users’ required level of functionality has the opposite impact on the indifferent functionality level $q ^ { \prime }$ compared to the case described in Lemma 4. When $x _ { L }$ increases, the high-type users’ utility remains the same, but the utility of low-type users decreases for any functionality level lower than their previous required level of functionality (Figure 5, left plot). This is so because low-type users become more sensitive to underprovisioning of functionality. Yet since they are always less sensitive to underprovisioning of functionality compared with high-type users, they get the same utility as high-type users at a lower functionality level. This leads to the shifting of the intersection point of the two utility curves to the left. Hence, the indifferent functionality level, $q ^ { \prime } ,$ , decreases as $x _ { L }$ increases (Figure 5, left plot).

Note that as $x _ { L A }$ increases to $x _ { L B } ,$ , the utility of lowtype users at $q = x _ { L B }$ increases, but the utility of hightype users at $q = x _ { L B }$ increases even more because they get more benefit and also experience less disutility. Hence, as $x _ { L }$ increases, Assumption 1(a) continues to hold. Since an increase in $x _ { L }$ does not impact optimal functionality $q ^ { * }$ , when $x _ { L }$ increases, we are only considering the situations where Assumption $2 \left( x _ { L } < q ^ { * } \right)$ and Assumption 1(b) continue to hold.

Recall that Lemma 2 states that the optimal functionality of the high version is independent of the characteristics of low-type users; and Lemma 4 states that the functionality level of the high version increases when high-type users’ required level of functionality increases. One may expect that the firm will increase the functionality of the low version (reduce functionality distortion) as $x _ { L }$ increases. The following proposition provides surprising results.

<sup>Proposition</sup> <sup>4.</sup> As the required level of functionality of low-type users $( x _ { L } )$ increases, (i) the lower threshold proportion $\alpha _ { 2 }$ and the upper threshold proportion $\alpha _ { 1 }$ increase, (ii) the optimal functionality of the low-version $q _ { V L } ^ { * }$ (a) increases if the proportion of high-type users is relatively low, and (b) decreases if the proportion of high-type users is relatively high.

Low-type users become more sensitive to underprovisioning of functionality as their required functionality level increases. This implies that by reducing the lowversion functionality level from the low-type users’ required level of functionality, the firm’s marginal gain from saving on information rent remains the same, but the marginal loss of revenue from low-type users increases. This leads to the firm reducing the low-version functionality level from the low-type users required functionality level $x _ { L } ,$ , when there are relatively more high-type users in the market, that is at higher $\alpha _ { 2 }$ (Figure 5, right plot, $\alpha _ { 2 L A } < \alpha _ { 2 L B } )$ . This also implies that the firm reduces the low-version functionality at a slower rate as  increases. Furthermore, when $x _ { L }$ increases the indifferent functionality level $q ^ { \prime }$ decreases (Lemma 5). This results in the firm stopping to reduce the functionality level of the low version when there are relatively more high-type users in the market, that is at higher $\alpha _ { 1 }$ (Figure 5, right plot, $\alpha _ { 1 L A } < \alpha _ { 1 L B } )$

The firm’s decision whether to reduce or increase functionality level of the low version when the low-type users’ required level of functionality increases depends on the proportion of high-type users in the market. The impacts are the opposite compared to an increase in the high-type users’ required level of functionality (Proposition 3). In Figure 5, right plot, low-type users get a higher functionality level when $0 < \alpha < \alpha _ { L A B }$ or a lower functionality level when $\alpha _ { L A B } < \alpha < 1$

<sup>Proposition</sup> <sup>5.</sup> When high-type users get information rent, (1) if the required level of functionality of high-type users $( x _ { H } )$ increases, then consumer surplus decreases; (2) if the required level of functionality of low-type users (x ) increases, consumer surplus increases.

Figure 5 Utility Curves for Both Types of Users, and the Optimal Functionality Level of the Low Version as Required Functionality Level for Low-Type Users Increases When $f ( q ) = q , g ( x , q ) = ( x - q ) ^ { 2 } , c ( q ) = q ^ { 2 }$ , and $\chi _ { _ { L A } } < \chi _ { _ { L B } }$  
![](/api/attachments/R6GA9SEW/fulltext/images/6918e2cdf0515eea3b3782ea1699000d7e0da5fd8517bf1120085ed5ddd77c46.jpg)

![](/api/attachments/R6GA9SEW/fulltext/images/b46c3399faa6bcc5f79d68f08761673a9fc5be861d9bf3d79dcaa30eba64b1b5.jpg)

Figure 6 Consumer Surplus of a High-Type User, (a) When $x _ { H }$ Increases $( { \cal X } _ { H B } > { \cal X } _ { H A } ) ;$ (b) When $x _ { L }$ Increases $( \boldsymbol { \chi } _ { L B } > \boldsymbol { \chi } _ { L A } )$  
![](/api/attachments/R6GA9SEW/fulltext/images/6af3a30c19175cdf1d7d7a99493af6e26c664be95a4e777cc4e37f363f721e83.jpg)  
(a)

We know that the firm needs to provide information rent to high-type users only when the proportion of the high type is lower than the upper threshold proportion, $\alpha \in ( 0 , \alpha _ { 1 } )$ (Lemma 3). As high-type users’ required level of functionality increases, they become more sensitive to underprovisioning of functionality and less inclined to switch to the low version. Thus, the firm provides less information rent to make them indifferent to switching to the low version. Therefore, the consumer surplus of those high-type users who get information rent declines when $\alpha \in ( 0 , \alpha _ { 1 B } )$ (see Figure 6(a)). Since the upper threshold proportion decreases (Proposition 3), $\alpha _ { 1 B } < \alpha _ { 1 A } ,$ high-type users get zero rent when $\alpha \in [ \alpha _ { 1 B } , \alpha _ { 1 A } )$ . When the proportion of high-type users is large, that is, $\alpha \in [ \alpha _ { 1 A } , 1 )$ high-type users get zero information rent as before (see Figure 6(a)). Hence, counterintuitively, high-type users are not better off when their required level of functionality increases even though they get a version with a higher functionality level.

On the other hand, as the low-type users’ required level of functionality increases, they become more sensitive to underprovisioning. When $\alpha \in ( 0 , \alpha _ { 1 L A } )$ (Figure 6(b)), the firm increases the functionality level of the low version, and pays more information rent, leading to an increase in surplus of high-type users. When $\alpha \in [ \alpha _ { 1 L A } , \alpha _ { 1 L B } )$ , then high-type users who did not get information rent get some information rent as $x _ { L }$ increases since the upper threshold proportion of hightype users increase (Proposition 4). Therefore, when $\alpha \in ( 0 , \alpha _ { 1 L B } )$ , high-type users get more information rent

![](/api/attachments/R6GA9SEW/fulltext/images/0b7e0831537c7392a6b8590847229bebbfdf7bc6ddffb3d7795db2d130670a02.jpg)  
(b)  
leading to a higher consumer surplus to high-type users as $x _ { L }$ increases. When the proportion of high-type users is large, that is, $\alpha \in [ \alpha _ { 1 L B } , 1 )$ , high-type users get zero surplus because $q _ { V L } ^ { * } = q ^ { \prime }$ (see Figure 6(b)).

## 5. Some Extensions

In this section, we analyze the impact of the following six settings regarding the optimal versioning strategy in §3: (1) when users do not experience disutility from underprovisioning of functionality, (2) when the market consists of N discrete types of users, (3) when Assumption 1 or 2 is relaxed, one at a time, (4) when rank ordering of valuation and the required level of functionality are not maintained, (5) impact of relative strength of the benefit function $f ( q )$ and disutility function $g ( x , q )$ on versioning strategy, and (6) impact of competition on versioning strategy.

## 5.1. No Disutility from Underprovisioning of Functionality

When users do not experience disutility from underprovisioning of functionality, then $g ( x _ { i } , q ) = 0 , \forall q$ for $\bar { i } \in \{ H , L \}$ . The utility function in (1) can be modified as

$$
U _ {i} (\theta_ {i}, x _ {i}, q) = \left\{ \begin{array}{l l} \theta_ {i} f (q), & \text { if } q <   x _ {i} \\ \theta_ {i} f (x _ {i}), & \text { if } q \geq x _ {i} \end{array} \right\}, \quad i \in \{H, L \}.\tag{5}
$$

<sup>Proposition</sup> <sup>6.</sup> When users do not experience disutility from underprovisioning of functionality, (i) when the proportion of high-type users is small $\alpha < \theta _ { L } / \theta _ { H }$ , the firm adopts a versioning strategy; and (ii) when the proportion of high-type users is large $\alpha \geq \theta _ { L } / \theta _ { H } ,$ the firm adopts a single-version strategy and sells only to high-type users.

Under a versioning strategy, the firm sets the optimal functionality level of the high version at the same level as when it sells a single version only to high-type users. Nonetheless, when there is no disutility from underprovisioning, the marginal gain from producing a high functionality level decreases, but the marginal cost of producing functionality remains the same as in §3. Hence the firm produces the high version with a lower functionality level. On the other hand, the firm chooses the optimal functionality level of the low version by trading off the decrease in revenue from high-type users because of payment of information rent in the presence of the low version and an increase in revenue from low-type users. Note that when $g = 0 ,$ then the upper threshold proportion $\alpha _ { 1 }$ and the lower threshold proportion $\alpha _ { 2 }$ values given in Lemma 3 converge to $\alpha _ { 1 } = \alpha _ { 2 } = \theta _ { L } / \theta _ { H }$ . When there are relatively more high-type users in the market, $\alpha \in [ \theta _ { L } / \theta _ { H } , 1 )$ , the firm sets the functionality level of the low version to zero to minimize information rent. It means that in this situation, the firm adopts a single-version strategy of selling only to high-type users. When there are relatively less high-type users in the market, $\alpha \in ( 0 , \theta _ { L } / \theta _ { H } )$ the firm sets the level of functionality of the low version at the required functionality level of low-type users, that is $x _ { L } ,$ to extract the maximum revenue from low-type users. Though the firm pays information rent to high-type users, the revenue gain from low-type users is more than the revenue loss (due to information rent) from high-type users. Hence versioning strategy dominates the single-version strategy of selling only to high-type users. Note that when the firm adopts a single-version strategy of selling to both types of users, the optimal functionality level is $x _ { L }$ as discussed in Lemma 2. Since under the versioning strategy, the firm sets the functionality of the low version at $x _ { L } ,$ , and gets more revenue from high-type users compared to selling a single version to both types of users, the profit under a versioning strategy dominates a single version strategy of selling to both types of users when $\alpha \in ( 0 , \theta _ { L } / \theta _ { H } )$ . Hence, the firm adopts a versioning strategy. Profits under the three product strategies are shown in Figure 7.

When users do not experience disutility from underprovisioning, our model has a close similarity to the hierarchical characteristics case of Wei and Nault (2014). Moreover, the condition under which a versioning strategy is optimal for the firm as given in Proposition 6 is similar to their condition given in the hierarchical characteristics case.

## 5.2. Market with N User Segments

We extend our analysis of §3 with two user types to a market consisting of N user types. Let there be $m _ { n }$ users of each type where $n \in \{ 1 , \bar { 2 } , \dots , N \}$ . Each type of user type (n5 is characterized by a duplet $\{ \theta _ { n } , { \bar { x _ { n } } } \} .$

Figure 7 Profits Under Different Product Strategies When There Is No Disutility from Underprovisioning  
![](/api/attachments/R6GA9SEW/fulltext/images/b7be0123480f0a8835325474bb375e5c7f934b6d7ed0f993dae996c2401ccebb.jpg)

$n \in \{ 1 , 2 , \ldots , N \}$ . Without loss of generality, we assume that user segments are ordered such that $\theta _ { N } > \theta _ { N - 1 } >$ $\cdots > \theta _ { 2 } > \theta _ { 1 }$ and $x _ { N } > x _ { N - 1 } > \cdot \cdot \cdot > x _ { 2 } > x _ { 1 }$ . Note that this is consistent with our conceptualization in §2 that the ordering of users’ marginal valuation for functionality and the required level of functionality is maintained such that $\theta _ { i } < \theta _ { i + 1 }$ and $x _ { i } < x _ { i + 1 }$ for $i \in \left\{ 1 , 2 , \dots , N - 1 \right\}$ In this context, we rewrite Assumption 1(a), as Equation (6)

$$
\begin{array}{c} U _ {i} (\theta_ {i}, x _ {i}, q = x _ {i - 1}) > U _ {i - 1} (\theta_ {i - 1}, x _ {i - 1}, q = x _ {i - 1}) \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \text { for } \forall i \in \{2, \ldots , N \}. \end{array}\tag{6}
$$

Assumption 1(b) can be restated as: the lowest functionality level at which users of higher types derive nonzero utility is higher than the lowest functionality level at which users of lower types derive nonzero utility. Assumption 2 can be rewritten as Equation (7)

$$
q ^ {*} \geq x _ {N - 1}.\tag{7}
$$

<sup>Proposition</sup> <sup>7.</sup> When users experience heterogeneous disutility from underprovisioning of functionality in a market consisting of N user segments, versioning strategy with a customized version for each segment is optimal.

First, we start with two types of users, the N -type and the 4N − 15-type. From Proposition 2 we know that it is optimal for the firm to adopt a versioning strategy and target one version to N -type users and another version to 4N − 15-type users. Then we consider the addition of a new market segment of 4N − 25-type users. In this situation the firm has six possible productprice strategies: (1) sell one version so that only N -type buy, (2) sell one version so that only N - and 4N − 15- types buy, (3) sell two versions so that N -type buy the high-version, 4N − 15-type buy the low-version, and 4N − 25-type do not buy, (4) sell one version so that $N \cdot ,$

4N − 15-, and 4N − 25-types buy, (5) sell two versions so that N - and 4N − 15-types buy the high-version, and 4N − 25-type buy the low version, and (6) sell three versions so that N -type buy the high version, 4N − 15-type buy the middle version, and 4N − 25-type buy the low version. Comparing firm profits under these product strategies we show that offering three versions targeted to each of the three user segments is optimal.

Note that the results from two-type user segments in $\ S 3$ (Proposition 2) extend to three-type segments because the firm gains more by providing another version targeted to the 4N − 25-type. The additional revenue from the 4N − 25-type is higher than the potential loss because of paying information rent to the 4N − 15-type and/or N -type users.

Assumptions in (6) and restated Assumption 1(b) implies that the indifferent functionality level between two adjacent user segments is higher than the required functionality level of the lower user segment, that is, $q _ { i , i - 1 } ^ { \prime } < x _ { i - 1 }$ . This property implies that the inconvenience or disutility experienced by the higher type user segment is such that the firm can offer a lower version at $q _ { i , i - 1 } ^ { \prime }$ to the 4i − 15-type users without paying any information rent to all user segments above 4i − 15-type.

Now, if we add another user segment 4N − 35 to our market such that $\theta _ { N - 2 } > \theta _ { N - 3 }$ and $x _ { N - 2 } > x _ { N - 3 } ,$ then similarly we can again show that the firm is better off by adding a new version targeted to the new 4N − 35-type users than to lower the price of the version targeted to any higher type user segments to cover the new segment. Extending this analysis, we show that when the market consists of N user segments then the firm’s optimal product-price strategy is to offer N versions and price them in such a way that each user segment self-selects versions targeted to them.

## 5.3. Impact of Model Assumptions on Versioning Strategy

In this subsection we study the impact of relaxing Assumptions 1(a), 1(b), and 2, one at a time, on the optimal versioning strategy of the firm. Assumption 1(a) implies that $U _ { H } ( q = x _ { L } ) > U _ { L } ( q = x _ { L } )$ . If this assumption is relaxed, then there can be the following two situations: $( \mathrm { i } ) \ U _ { H } ( q = x _ { L } ) = U _ { L } ( q = x _ { L } )$ , or (ii) $U _ { H } ( q =$ $x _ { L } ) < U _ { L } ( q = x _ { L } )$ . Situation (i) implies that the indifferent functionality level is $q ^ { \prime } = x _ { L }$ . Under this situation, when the firm offers the low version with functionality level at $x _ { L }$ , then information rent to high-type users is zero. Therefore, we get a special case of Lemma $^ { 3 , }$ where $q _ { V H } ^ { * } = q ^ { * } , q _ { V L } ^ { * } = x _ { L } ,$ and both the upper and lower threshold proportions of high-type users are equal to 1, that is, $\alpha _ { 2 } = \alpha _ { 1 } = 1$ . In this situation, it is optimal for the firm to adopt a versioning strategy.

Under situation (ii), the indifferent functionality level is higher than the low-type users’ required functionality level, that is $q ^ { \prime } > x _ { L }$ . To study the optimality of versioning strategy, we also need to take into consideration the relative position of the highest functionality level developed by the firm $( q ^ { * } )$ with respect to $x _ { L }$ and $q ^ { \prime } .$ This leads us to three possible situations: (a) $x _ { L } < q ^ { * } < q ^ { \prime } ,$ , (b) $x _ { L } < q ^ { \prime } < q ^ { * }$ , and (c) $x _ { L } < q ^ { \prime } = q ^ { * }$ (see Figures $8 ( \mathsf { a } ) { - } 8 ( \mathsf { c } ) )$

In situation (a), the optimal functionality level produced by the firm is such that at that functionality level, $q = q ^ { * }$ , high-type users have a very high disutility from underprovisioning, leading to their utility being lower than low-type users. It implies that the firm needs to pay increasingly more information rent if it lowers the functionality of the low version from $x _ { L }$ . Therefore, in this situation, versioning is not optimal. On the other hand, in situation (b), the firm offers the low version with a functionality level $q _ { V L } ^ { * } = x _ { L }$ since there is no gain in revenue by offering the low version with

Figure 8 Utility of High and Low-Type Users When (a) $x _ { L } < q ^ { * } < q ^ { \prime }$ , (b) $x _ { L } < q ^ { \prime } < q ^ { * }$ , and (c) $x _ { L } < q ^ { \prime } = q ^ { * }$  
![](/api/attachments/R6GA9SEW/fulltext/images/5721d2a01efe9d4ddbdeffc140fde8f33e2e020c2e17d4105c31a3867c628d4e.jpg)

![](/api/attachments/R6GA9SEW/fulltext/images/ca980728193c246e3637dfeab3f1981f75979b8c7a74e761dace6a39a6c17d3f.jpg)  
(b) $x _ { L } < q ^ { \prime } < q ^ { * }$

![](/api/attachments/R6GA9SEW/fulltext/images/b91017eb549b213999403f031e6a1cbe32b12a27c791252d234915b5a811b355.jpg)  
(c) $x _ { L } < q ^ { \prime } = q ^ { * }$

Figure 9 Utility of High-Type and Low-Type Users When (a) $q ^ { * } < q ^ { \prime } < X _ { L }$ , (b) $q ^ { \prime } = q ^ { * } < X _ { L }$ , (c) $q ^ { \prime } < q ^ { \ast } < X _ { L }$ , and (d) $q ^ { \prime } < q ^ { \ast } = X _ { L }$

![](/api/attachments/R6GA9SEW/fulltext/images/6ba8d0491ef48e6aa2d4595f2365b947095fc8dd96de9959d3beccabed17857e.jpg)  
(a) $q ^ { * } < q ^ { \prime } < x _ { L }$

![](/api/attachments/R6GA9SEW/fulltext/images/cf290e1f179ce70715a752713f260daa049a41ef715f9244f386eedbad467f06.jpg)  
(b) q<sup>\*</sup> = q- < x<sub>L</sub>

![](/api/attachments/R6GA9SEW/fulltext/images/3f1583edf8d91aed7f99d5a49397b64a083c45be3c010240d5a7096d62fab04d.jpg)  
(c) q- < q<sup>\*</sup> < x<sub>L</sub>

![](/api/attachments/R6GA9SEW/fulltext/images/44cedf7b2c3f629f9c1e70430ad2791d6c622f1a1bb55a3fa74a00f4af0ef97f.jpg)  
(d) q- < q<sup>\*</sup> = x<sub>L</sub>

functionality more than $x _ { L }$ . Furthermore, by providing the high version with $q _ { V H } ^ { * } = q ^ { * }$ , the firm pays zero information rent to high-type users, and versioning is optimal. Moreover, in situation (c), low-type users have a higher utility than high-type users for any functionality level $q < q ^ { * }$ . It is not optimal to offer the high version with functionality $q _ { V H } ^ { * } = q ^ { * }$ to low-type users and to offer the low version with functionality $q _ { V L } ^ { * } < q ^ { * }$ to high-type users, as the firm needs to pay increasingly more information rent to low-type users if it lowers the functionality of the low version from $q ^ { * }$ Also, low-type users are indifferent from any functionality level from $x _ { L }$ to $q ^ { \prime } = q ^ { * }$ . Therefore, the firm just offers a single version with $q ^ { * }$ functionality.

If Assumption 1(b) were to be relaxed, then it implies that the utility functions of the two types do not cross over. In this situation, since there is no cross-over point, the firm does not have the ability to distort the low-version’s functionality level. Hence, the versioning strategy will be optimal only when a proportion of high-type users is smaller than some critical proportion $\alpha < { \hat { \alpha } } .$ . The value of ˆ depends on the properties of function $f ( \cdot )$ and $g ( \cdot , \cdot )$ , and $\hat { \alpha } \in [ \alpha _ { 2 } , \alpha _ { 1 } ]$ , where $\alpha _ { 1 }$ and $\alpha _ { 2 }$ are given by Lemma 3.

Now, we consider the impact of relaxing Assumption 2, which is $q ^ { * } > x _ { L }$ . If this assumption were to be relaxed, then we need to consider the relative position of the optimal functionality level with respect to the indifferent functionality level $q ^ { \prime } .$ Therefore, the following four situations may arise: (a) $q ^ { * } < q ^ { \prime } < x _ { L } ,$ (b) $q ^ { \prime } = q ^ { \ast } < x _ { L } .$ , (c) $q ^ { \prime } < q ^ { * } < x _ { L }$ , and (d) $q ^ { \prime } < q ^ { * } = x _ { L }$ (Figures 9(a)–9(d)).

In situations (a) and (b), the firm sells only one version at the optimal functionality level. This happens because the firm needs to pay more information rent to high-type users than the gain from selling another version with lower functionality to low-type users. Therefore, in these two situations ((a) and (b)), versioning is not optimal. In situations (c) and (d), the firm will produce $q _ { V H } ^ { * } = q ^ { * }$ , and $q _ { V L } ^ { * } \in [ q ^ { \prime } , q ^ { * } ]$ , and versioning is optimal, as the firm pays zero rent to high-type users when $q _ { V L } ^ { * } = q ^ { \prime }$

## 5.4. Impact of Ordering of Valuation and Required Level of Functionality on Versioning

In our conceptualization, high-type users have a higher marginal valuation for functionality as well as a higher required level of functionality compared to low-type users. This implies that the elements of duplet $\{ \theta _ { i } , x _ { i } \}$ can take any value as long as the rank ordering is maintained. This conceptualization closely mimics the reality where one observes software versions with higher levels of functionality sold at higher prices. However, for the sake of completeness, in this subsection we study the impact on the versioning strategy of a software firm if the rank ordering is not maintained, that is $\theta _ { H } > \theta _ { L }$ but $x _ { H } \leq x _ { L }$ . Note that in this case, Assumption 1(b) does not hold.

Let us first consider the case where $x _ { H } = x _ { L }$ . In this situation, both types of users experience the same disutility from underprovisioning, and thus, the utility curve of high-type users is above the utility curve of low-type users for all feasible functionality levels. The implication of homogeneous disutility is that the versioning strategy is not optimal. This is because the revenue gain from selling two versions is always less than the information rent required to be paid to high-type users (the formal analysis and proof is in Online Appendix B).

When $x _ { H } < x _ { L }$ , then three distinct subcases arise: (a) the maximum utility of high-type users is greater than the maximum utility of low-type users, that is, $\theta _ { H } f ( x _ { H } ) > \theta _ { L } f ( x _ { L } ) ; ( \mathbf { b } )$ the maximum utility of high-type users is equal to the maximum utility of low-type users, that is, $\bar { \theta _ { H } f } ( x _ { H } ) = \theta _ { L } f ( x _ { L } ) ;$ and (c) the maximum utility of high-type users is lower than the maximum utility of low-type users, that is, $\theta _ { H } f ( x _ { H } ) < \theta _ { L } f ( x _ { L } )$ . Figure 10 illustrates these three cases.

Figure 10 Utility of High-Type and Low-Type Users When $x _ { H } < x _ { L }$  
![](/api/attachments/R6GA9SEW/fulltext/images/e74a32c0296c5e9bf77b8052d7ef790b4d4da2e1a6af3e3ba0f876299226e2db.jpg)  
(a) $\theta _ { H } f ( x _ { H } ) > \theta _ { L } f ( x _ { L } )$

![](/api/attachments/R6GA9SEW/fulltext/images/8dd0563eb2714849def483f98dd51ab6545044b8b50c068d9e0d901ef1e434da.jpg)  
(b) $\theta _ { H } f ( x _ { H } ) = \theta _ { L } f ( x _ { L } )$

![](/api/attachments/R6GA9SEW/fulltext/images/1a826ca2f8c6ed72ee0f2345b912978bd1fee2b60152d2c383c68ddd59dae007.jpg)  
(c) <sub>H</sub> f (x<sub>H</sub>) < <sub>L</sub> f (x<sub>L</sub>)

In case (a), the utility function for high-type users is above the utility function of low-type users for all feasible functionality levels. In this situation, when the firm sells one version, it considers selling $q = x _ { L }$ to all users or to only high-type users. If the firm adopts a versioning strategy, it will always sell the high version with $q _ { V H } = x _ { L }$ and the low version with a functionality level less than $x _ { L }$ , that is $q _ { V L } \in [ 0 , x _ { L } )$ Since low-type users experience more disutility than high-type users, the information rent paid to hightype users will always be more than $( \bar { \theta _ { H } } - \theta _ { L } ) f ( \bar { q _ { V L } } )$ This implies that, when the firm adopts a versioning strategy, the loss in revenue due to information rent is always more than the gain in revenue from low-type users. Therefore, versioning strategy is not optimal (the formal analysis and proof is in Online Appendix B). A similar analysis applies to case (b) and leads to versioning being not optimal. Note that in cases (a) and (b) the utility functions of low-type and high-type users do not cross over. In case (c), the required level of functionality of low-type users $x _ { L }$ is so high that the cross-over point of the utility function of the two types is to the right of the required level of functionality of high-type user $x _ { H }$ . It is easy to see that in this case, since the utility functions cross over, the firm can save on the information rent by setting the functionality level of the high version at $q _ { V H } ^ { * } = x _ { L }$ and the low version at $q _ { V L } ^ { * } = q ^ { \prime }$ . This leads to versioning being an optimal strategy in this case.

Figure 11 Impact of Users’ Inconvenience on Consumer Utilit  
![](/api/attachments/R6GA9SEW/fulltext/images/2f36b5978a983dbcadc3f5cb0f6ba8292a277bd95e321b102dc08d4f45740c82.jpg)

## 5.5. Impact of Relative Strength of $f ( q )$ and $g ( x , q )$ on Versioning Strategy

In this subsection, we examine the impact of the relative strengths of the benefit function $f ( q )$ and disutility from the underprovisioning function $g ( x , q )$ on the firm’s versioning strategy. Given a benefit function $f ( q )$ , when the strength of the disutility function $g ( x , q )$ increases (users experience more disutility from underprovisioning), it leads to a steeper slope of utility curves of both types of users. This results in a shifting of the utility curves of both types of users downward.

This implies that the indifferent functionality level $( q ^ { \prime } )$ shifts to the right, which is illustrated in Figure 11 (left plot). Note that the strengthening of the disutility function $g ( x , q )$ shifts the highest optimal functionality $q ^ { * }$ to the right $( q _ { 2 } ^ { * } > q _ { 1 } ^ { * } )$ , because though the marginal cost of producing functionality remains the same, the marginal benefit from functionality increases. Since, in this case the utility curves of both types of users cross over, the versioning strategy remains optimal. Therefore, as users’ disutility from underprovisioning becomes stronger, the firm adopts versioning and increases the level of functionality of the high version. The level of functionality of the low version may increase or decrease depending on the parameter values.

![](/api/attachments/R6GA9SEW/fulltext/images/2bcc9ebeff75e37b9b16e3f798f47d04cb5438e2a7a8052063d84df512b09118.jpg)

Given a disutility function $g ( x , q ) .$ , when the strength of the benefit function $f ( q )$ increases $( f _ { 2 } ( q ) > f _ { 1 } ( \bar { q } ) )$ , utility curves of both types of users become steeper, that is, the slopes of the utility curves increase. This shifts the utility curves of both types of users upward. This implies that the indifferent functionality level shifts to the left $( q _ { 2 } ^ { \prime } < q _ { 1 } ^ { \prime } )$ 5. Note that the strengthening of $f ( q )$ shifts the highest optimal functionality $q ^ { * }$ to the right, $q _ { 2 } ^ { * } > q _ { 1 } ^ { * }$ . Since the utility curves of both types of users cross over, the versioning strategy remains optimal. The firm increases the level of functionality of the high version, but may increase or decrease the level of functionality of the low version depending on the parameter values (Figure 11, right plot).

To summarize, the relative strengths of function $f ( \cdot )$ and $g ( \cdot , \cdot )$ do not impact the existence of the crossover point between utility functions of high-type and low-type users. This implies that the firm’s gain from offering two versions continues to be more than the information rent paid to high-type users. Therefore, a versioning strategy remains optimal and only the functionality levels of high version and low version are impacted by the relative strengths of function $f ( \cdot )$ and $g ( \cdot , \cdot )$

## 5.6. Impact of Competition on a Firms Versioning Strategy

Our model considers a monopolist market structure. It will be interesting to examine how our results may be impacted in a competitive market setting. We consider a duopoly market structure with two heterogeneous firms, Firms 1 and 2 where their software development costs are $c _ { i } ( \boldsymbol { q } )$ , where $i \in \{ 1 , 2 \}$ . On the line of Moorthy (1988), Wei and Nault (2008), and Jones and Mendelson (2011), we consider a two-stage Bertrand competition. In the first stage, the two firms develop software with quality $q _ { i } ,$ where $i \in \{ 1 , 2 \}$ , and in the second stage, they compete in prices.

From Wei and Nault (2008) and Jones and Mendelson (2011), we know that it is not Nash equilibrium for both firms to develop information goods with the same quality. The intuition is that Bertrand competition leads to marginal cost pricing, and since the marginal cost for software is zero, neither firm gains a positive profit. Now, both firms have the option to either produce only one quality (Firm i produces $q _ { i } , i \in \{ 1 , 2 \} )$ or to adopt a versioning strategy (Firm i produces $q _ { i } ^ { H }$ and $q _ { i } ^ { L } )$ . If $q _ { 2 } ^ { H } = q _ { 2 } ^ { L } = \check { q _ { 2 } }$ and $q _ { 1 } ^ { \breve { H } } > q _ { 1 } ^ { L } > 0$ , then only Firm 1 adopts a versioning strategy, and Firm 2 does not adopt a versioning strategy. Similarly, if $q _ { 1 } ^ { H } = q _ { 1 } ^ { L } = q _ { 1 }$ and $q _ { 2 } ^ { H } > q _ { 2 } ^ { L } > 0$ , then only Firm 2 adopts a versioning strategy, and Firm 1 does not adopt a versioning strategy. Without loss of generality, we assume $c _ { 1 } ( q ) <$ $c _ { 2 } ( q )$ , which leads to $q _ { 1 } ^ { * } > q _ { 2 } ^ { * }$ , where $q _ { i } ^ { * }$ is the quality level that Firm i produces in the case of a monopolist setting. This implies that Firm 1 is the high-quality firm and Firm 2 is the low-quality firm.

Let Firm 1 produce the high-quality version, $q _ { 1 } ^ { H } = q _ { 1 } ^ { * }$ where $q _ { 1 } ^ { * }$ is the quality level that Firm 1 produces in the case of the monopolist setting. Firm 1 can produce the low-quality version $q _ { 1 } ^ { L } < q _ { 1 } ^ { H }$ without incurring any cost. We have shown in $\ S 3$ that when users experience disutility from underprovisioning of functionality, the utility of high-type and low-type users cross at the indifference quality level $q ^ { \prime } .$ . Therefore, if Firm 1 offers the low-quality version, $q _ { 1 } ^ { L } \leq q ^ { \prime }$ , at the price $U _ { L } ( q _ { 1 } ^ { L } )$ then Firm 1 pays zero information rent to high-type users, and low-type users buy the low-quality version.

Suppose Firm 2’s optimal quality of the high version is $q _ { 2 } ^ { H } = q _ { 2 } ^ { * } < q _ { 1 } ^ { * }$ . There are two possibilities: (1) $q ^ { \prime } \leq q _ { 2 } ^ { * } < q _ { 1 } ^ { * }$ and $( 2 ) \ q _ { 2 } ^ { * } < q ^ { \prime }$ . In the first case, since Firm 1 is more cost efficient $( c _ { 1 } ( q ) < c _ { 2 } ( q ) )$ , Firm 2 does not compete for high-type users with Firm 1. Therefore, Firm 2 does not adopt a versioning strategy and provides one quality at $q _ { 2 } = q _ { 2 } ^ { * }$ to low-type users, and the maximal price it can charge is $U _ { L } ( q _ { 2 } ^ { * } )$ . In this situation, Firm 1 can respond without cost by offering the low version, $q _ { 1 } ^ { L } = \bar { q ^ { \prime } }$ , to low-type users and set the price at $U _ { L } ( q ^ { \prime } ) - \varepsilon .$ . Firm 1 does not need to pay information rent to high-type users, and, at the same time, it captures all low-type users leading to zero market demand for Firm 2. Firm 2 knows this, and therefore, its best strategy is to exit the market. Similarly in the second case, it is clear that Firm 1 always, without cost, captures low-type users, and the best response for Firm 2 is to exit the market. This implies that in equilibrium, the high-quality firm (Firm 1) adopts a versioning strategy and the low-quality firm (Firm 2) does not enter the market. This analysis is in conformity with the empirical observations that vertically differentiated markets for information goods tend to be highly concentrated or monopolistic (Jones and Mendelson 2011). This is also consistent with the observation of Wei and Nault (2008) that a vertically differentiated market for information goods can be regarded as a “natural monopoly.”

## 6. Discussion

This work belongs to the stream of literature in information systems that has studied versioning strategy from a perspective of users’ utility from software under general market conditions. In our abstraction, users derive utility from software in a task oriented context and require a certain set of functionality to accomplish their tasks. Users are heterogeneous on two dimensions: valuations for functionality and required levels of functionality; and high-type users require a higher level of functionality. Furthermore, users experience disutility if functionality provided in the software is lower than their required level and derive no additional utility if functionality provided in the software is more than what they require. This conceptualization of the utility function for software is unique and allows us to study software firm’s product-pricing strategies when users experience disutility from underprovisioning.

We show that under our model framework and assumptions, heterogeneous disutility from underprovisioning of functionality is a sufficient condition for optimality of versioning strategies for a monopolist software firm. The economic intuition for our finding is as follows. When a software firm adopts a singleversion strategy of selling to all users, the firm’s profit is limited by the maximum utility derived by low-type users when software provides their required level of functionality. When the firm adopts a single-version strategy of selling only to high-type users, the firm does not serve low-type users. When the firm adopts a versioning strategy, it can serve the entire market but has to pay information rent to high-type users. When users experience disutility from underprovisioning, under a versioning strategy, high-type users are paid lower information rent. This savings in information rent leads to the profit under a versioning strategy dominating under a single-version strategy irrespective of the distribution of user types. Furthermore, we demonstrate the role of heterogeneous disutility from underprovisioning of functionality by showing that when users do not experience disutility from underprovisioning, versioning strategy is suboptimal if the proportion of high-type users is relatively high in the market.

We also examine the impact of an increase in users’ required level of functionality on the software firm’s product-pricing decisions under a versioning strategy. This provides insights to software firms since one would expect that users may require more software functionality over a time period in a fast changing technological landscape and work environment. When high-type users require more functionality, the firm increases the functionality level of the high version, but decreases the functionality level of the low version when the proportion of high-type users is relatively moderate in the market. It is so because high-type users become more sensitive to underprovisioning of functionality, and the firm gains more in saving of information rent from high-type users than loss of revenue from low-type users by downward distorting functionality of the low version. On the other hand, when the low-type users’ required level of functionality increases, surprisingly, when the proportion of hightype users is relatively large, the firm lowers the level of functionality of the low version. This is so because lowtype users become more sensitive to underprovisioning of functionality and the indifferent functionality level (functionality level at which both types of users have the same utility) decreases.

Extant literature in IS has focused on either the cost structure of developing quality or market characteristics like the presence of piracy or network externality or distribution of user types to study the profitability of a monopolistic firm’s versioning strategy. The general recommendation has been that it is suboptimal to offer versions of information goods like software where the development cost is convex and the marginal cost is negligible (Bhargava and Choudhary 2001, 2008; Jones and Mendelson 2011). However, we recommend that when users derive utility in a task-oriented context, software firms should take into account users’ heterogeneous inconvenience or disutility from underprovisioning, and adopt a versioning strategy.

In this paper, we propose a novel conceptualization of the utility function that captures user heterogeneities in marginal valuation of functionality, required level of functionality, and inconvenience or disutility from underprovisioning. Previous studies have considered only heterogeneous marginal valuation for functionality or quality in either linear utility function (Bhargava and Choudhary 2001, 2004; Chellappa and Shivendu 2003, 2005) or quadratic utility function (Raghunathan 2000), or nondecreasing quadratic utility function (Ghose and Sundararajan 2005). These utility functions are illustrated in the leftmost plot of Figure 12 and it is clear that the utility function of high-type and low-type users do not cross over at a positive utility level. In addition, Wei and Nault (2014) employ a linear utility function where users derive no additional utility from overprovisioning beyond their required levels of functionality. The middle plot in Figure 12 illustrates their utility formulation where also the utility function of high-type and low-type users do not cross over at a positive utility level. Our utility function integrates these parts from extant literature with our abstraction of inconvenience or disutility if the software provides less functionality than what a user requires. The conceptualization of user disutility from underprovisioning leads to type-dependent utility functions that cross over at a positive utility level (Figure 12, rightmost plot). This property leads to the optimality of the versioning strategy.

Our approach is based on how users derive utility from software and our conceptualization of utility function is new. There are some key similarities and differences between our work and the stream of literature in IS that has studied optimality of a versioning strategy from the utility perspective, namely, Chen and Seshadri (2007) and Wei and Nault (2014). In Chen and Seshadri (2007), users have convex reservation utilities for outside options. It implies that high-type users have a higher valuation of outside options than low-type users. This conceptualization has some similarity to our model where high-type users are more sensitive to underprovisioning of functionality, and hence, are less attracted to the low version. The key difference is that in their model, type-dependent outside option is exogenous and is independent of the quality of information good, whereas type-dependent disutility from underprovisioning depends on the level of functionality in the software in our model. This difference is key to our result that the entire market is covered, whereas in their case relatively high- and low-type users are excluded. The key difference between our model and Wei and Nault (2014) is that in their model users do not experience any inconvenience or disutility from underprovisioning. This key difference leads to optimality of versioning in our case, whereas in their hierarchical characteristics case versioning is optimal only under certain distributions of user types.

Figure 12 Comparison of Our Utility Function with Utility Functions Employed in Extant Versioning Literature  
![](/api/attachments/R6GA9SEW/fulltext/images/80b7d6c0eae6067b26934e2b537fee269da5ebe0ba70bc6a0195458adfbee6b8.jpg)

![](/api/attachments/R6GA9SEW/fulltext/images/2b22882715d24575640a42b08ad7ea7420b27ee1d46be39c2108897deeeebf03.jpg)  
B: Quadratic utility function (Raghunathan 2000)

![](/api/attachments/R6GA9SEW/fulltext/images/1f62d535a63acdcbba82a61f038479275deee5c4f002db350ee29e3740d9a662.jpg)  
A: Linear utility function (Bhargava and Choudhary 2001, 2004; Chellappa and Shivendu 200, 200)  
C: Nondecreasing quadratic utility function (Ghose and SundaraRAjan 2005)

The managerial implication of our research for information goods firms is that careful investigation of functionality requirements of their different user segments is critical for an optimal versioning strategy. Inherent differences in users’ functionality requirements and inconvenience from underprovisioning could potentially explain why some providers sell a single version whereas others adopt versioning. It could explain differences in product-pricing strategies even when firms have a similar cost structure of producing functionality; software has a similar level of network externality and markets have a similar piracy level. For example, Microsoft offers Windows 8 in three versions in the United States because different user segments are not only heterogeneous in their marginal valuation for functionality but also in their required level of functionality. On the other hand, Corel offers PhotoImpact in a single version only. Based on our analysis, one possible explanation for this may be that different user segments of PhotoImpact may have similar requirements for functionality though they may have a heterogeneous valuation for functionality. This situation is similar to one discussed in §5.4 wherein both types of users have the same required level of functionality. In that case, any underprovisioning would impact different user segments in the same way. This limits the ability of the firm to save information rent by distorting the low-version’s functionality. The optimal strategy is likely to be a single-version product strategy. The same logic may explain cases where software firms simultaneously adopt a versioning strategy for some products and a single-version strategy for others. For example, Adobe offers Photoshop CS in two versions but sells a single version of Digital Publishing Suite.

This research also provides key insights to managers to develop the optimal product-pricing strategy for information goods like software and information services from which users derive utility in a taskoriented context and users’ requirements for functionality increase over time. More specifically, when there is a shift in users’ required levels of functionality, firms may need to adjust the degree of functionality distortion of the low version to avoid either any loss of revenue from low-type users or any overpayment of information rent to high-type users. Managers also need to be aware that the optimal degree of functionality distortion in the low version depends on the proportion of high-type users in the market, and the firm may accordingly adjust the low-version’s functionality level in different markets. For example, Microsoft offers Windows 7 Home Basic only in some emerging markets. Moreover, since the relative strength of the benefit function from functionality provided in the software and the disutility function from underprovisioning of functionality is critical in determining the extent of underprovisioning, managers should pay special attention to this in determining product-pricing strategies.

We made some assumptions regarding the users’ required level of functionality and cost of development to build the framework for analysis. Note that though we assume a convex cost function, our results hold for any general cost function as long as Assumption 2 holds. In §5, we show that a versioning strategy often dominates other product strategies even when some of the assumptions are relaxed, one at a time. We also examine the profitability of a versioning strategy when rank ordering of valuation and required level of functionality is not maintained and find that versioning is optimal only under some conditions.

Our framework and analysis has some limitations. In our setup, users have full information about functionality provided in different versions of the software and also know their own “required level of functionality.” However, in practice, users may have some uncertainty about the functionality provided in the software and also about their own required level of functionality. A future research project may allow user uncertainty about the level of functionality in software and required level of functionality. Moreover, we assume that users evaluate different versions of a single software product, whereas in practice users may adopt a bundle of software products and services with complementary or overlapping functionality. This is outside the scope of the current model, and may be an avenue for future research.

Our model is not a dynamic model and has a single period with no uncertainty. Therefore, users do not update their beliefs about functionality of the software like in the model of Shapiro (1983). We also do not capture the dynamics of product strategies to trace the equilibrium path of a firm’s strategies. An intertemporal model that abstracts dynamics of changes in users’ requirements of functionality and analyzes multiperiod product-pricing strategies of the software firm is an interesting avenue for future research.

Within the framework of our assumptions, we have examined the impact of competition in a duopolistic setting (§5.6). It may be fruitful to extend the framework to an oligopolistic competitive market structure. Moreover, we have not modeled the process through which users arrive at their “required level of functionality” and how a software firm may impact the same through a strategic new product preannouncement like “vaporware.” This may be a possible area to extend our framework.

It may also be worthwhile to study a firm’s versioning strategy under different types of utility functions and analytically establish that only certain types of utility functions lend themselves to versioning. Moreover, we assume that overprovisioning is useless, though in some situations it may be utility decreasing when users have some resource constraints, as in Chellappa and Mehra (2011). Future research may examine versioning strategies under costly overprovisioning on the lines of Chellappa and Shivendu (2010), which may shed some light on the theoretical understanding of the widespread creation of bloatware.<sup>12</sup> Further, the class of utility function with a single-crossing property, developed in this research, can be used to study product-pricing strategy of other information goods.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2015.0597.

## Acknowledgments

The authors would like to thank the senior editor, the associate editor, and the three anonymous reviewers for their helpful and insightful comments.

## Appendix A. Summary of Notation

$\theta _ { H }$ Marginal valuation for functionality of high-type users.

$\theta _ { L }$ Marginal valuation for functionality of low-type users.

$x _ { H }$ High-type users required level of functionality.

$x _ { L }$ Low-type users required level of functionality.

$q _ { H }$ Functionality under a strategy of selling a single version only to high-type users.

$q _ { A }$ Functionality under a strategy of selling a single version to all users.

q<sub>VL</sub> Functionality of the low-version under a versioning strategy.

q<sub>VH</sub> Functionality of the high-version under a versioning strategy.

 Proportion of high-type users in the market.

N Superscript: case where users do not experience disutility from underprovisioning of functionality.

$p _ { A }$ Price under a product strategy of selling a single version to all users.

$p _ { H }$ Price under a product strategy of selling a single version only to high-type users.

$p _ { V H }$ Price of the high-version under a versioning strategy.

$p _ { V L }$ Price of the low-version under a versioning strategy.

$\pi _ { A }$ Profit under a product strategy of selling a single version to all users.

$\pi _ { H }$ Profit under a product strategy of selling a single version only to high-type users.

$\pi _ { V }$ Profit under a versioning strategy.

$q ^ { \prime }$ Functionality level where both types of users have the same utility.

$\alpha _ { 2 } , \alpha _ { 1 }$ Critical values of proportion of high-type users in the market where the firm starts and stops distorting functionality of the low-version, respectively.

## References

Anderson ET, Dana JD Jr (2009) When is price discrimination profitable. Management Sci. 55(6):980–989.

Belleflamme P, Gordon W, Watt R (2003) Pricing information goods in the presence of copying. Gordon W, Watt R, eds. The Economics of Copyright: Developments in Research and Analysis (Edward Elgar Publishers, Cheltenham, UK), 26–54.

<sup>12</sup> Software bloat is a process whereby successive versions of a computer program include an increasing proportion of unnecessary features that the end users do not access, or that generally use more system resources than necessary, while offering little or no benefit to users (http://en.wikipedia.org/wiki/Bloatware).

Bhargava HK, Choudhary V (2001) Information goods and vertical differentiation. J. Management Inform. Systems 18(2):89–106.

Bhargava HK, Choudhary V (2004) Economics of an information intermediary with aggregation benefits. Inform. Systems Res. 15(1):22–36.

Bhargava HK, Choudhary V (2008) Research note—when is versioning optimal for information goods? Management Sci. 54(5): 1029–1035.

Chellappa RK, Mehra A (2011) Versioning 2.0: A product line and pricing model for information goods under usage constraints and with R&D costs. Working paper, Theory of Economics of Information Systems, Lake Tahoe, NV. http://www.teis -workshop.org/papers/Versioning\_Chellappa\_Mehra.pdf.

Chellappa RK, Shivendu S (2003) Economic implication of variable technology standards for movie piracy in a global context. J. Management Inform. Systems 20(2):137–168.

Chellappa RK, Shivendu S (2005) Managing piracy: Pricing and sampling strategies for digital experience goods in vertically segmented markets. Inform. Systems Res. 16(4):400–417.

Chellappa RK, Shivendu S (2010) Mechanism design for “free” but “no free disposal” services: The economics of personalization under privacy concerns. Management Sci. 56(10):1766–1780.

Chen Y, Seshadri S (2007) Product development and pricing strategy for information goods under heterogeneous outside opportunities. Inform. Systems Res. 18(2):150–172.

Cheng HK, Tang QC (2010) Free trial or no free trial: Optimal software product design with network effects. Eur. J. Oper. Res. 205(2):437–447.

Cooper R (1984) On allocative distortions in problems of self-selection. RAND J. Econom. 15(4):568–577.

Cusumano M, Selby R (1997) How Microsoft builds software. Comm. ACM 40(6):53–61.

Dey D, Lahiri A (2013) The zero-day DLC strategy: A case for versioning to facilitate product sampling. Working paper, University of Washington, Seattle, http://teis-workshop.org/papers/2013/ 02\_The\_Zero-Day\_DLC\_Strategy.pdf.

Garvin DA (1984) What does “product quality” really mean? Sloan Management Rev. 26(1):25–43.

Gershoff AD, Kivetz R, Keinan A (2012) Consumer response to versioning: How brand’s production methods affect perceptions of unfairness. J. Consumer Res. 39(2):382–398.

Ghose A, Sundararajan A (2005) Software versioning and quality degradation? An exploratory study of the evidence. Proc. 26th Internat. Conf. Inform. Systems, Las Vegas, NV, 59–70.

International Organization for Standardization (ISO) (1994) ISO 8402: Quality Management and Quality Assurance—Vocabulary, International Organization for Standardization, 2nd ed. (ISO, Geneva).

Jing B (2000) Versioning information goods with network externalities. Proc. 21st Internat. Conf. Inform. Systems, Brisbane, Queensland, Australia, 1–12.

Jones R, Mendelson H (2011) Information goods vs. industrial goods: Cost structure and competition. Management Sci. 57(1):164–176.

Kekre S, Krishnan MS, Srinivasan K (1995) Drivers of customer satisfaction for software products: Implications for design and service. Management Sci. 41(9):1456–1470.

Kitchenham B, Pfleeger SL (1996) Software quality: The elusive target [special issues section]. Software, IEEE 13(1):12–21.

Laffont JJ, Martimort D (2002) The Theory of Incentives: The Principal-Agent Model (Princeton University Press, Princeton, NJ).

Lahiri A, Dewan RM, Freimer M (2013) Pricing of wireless services: Service pricing vs. traffic pricing. Inform. Systems Res. 24(2): 418–435.

Methvin D (2009) Can an office suite be too powerful? Information-Week (July 16), http://www.informationweek.com/windows/ microsoft-news/can-an-office-suite-be-too-powerful/229205780.

Moorthy KS (1988) Product and price competition in a duopoly. Marketing Sci. 7(2):141–168.

Moorthy KS, Png I (1992) Market segmentation, cannibalization, and the timing of product introductions. Management Sci. 38(3): 345–359.

Mussa M, Rosen S (1978) Monopoly and product quality. J. Econom. Theory 18(2):301–317.

Niculescu M, Wu DJ (2014) Economics of free under perpetual licensing: Implications for the software industry. Inform. Systems Res. 25(1):173–199.

Raghunathan S (2000) Software editions: An application of segmentation theory to the packaged software market. J. Management Inform. Systems 17(1):87–113.

Salant SW (1989) When is inducing self-selection suboptimal for a monopolist. Quart. J. Econom. 104(2):391–397.

Shapiro C (1983) Premiums for high quality products as returns to reputations. Quart. J. Econom. 98(4):659–679.

Shapiro C, Varian H (1998) Versioning: The smart way to sell information. Harvard Bus. Rev. 107(6):106–114.

Sundararajan A (2004) Managing digital piracy: Pricing and protection. Inform. Systems Res. 15(3):287–308.

The Software Alliance (2012) 2011 BSA Global Software Piracy Study, 9th ed. (Washington, DC), http://portal.bsa.org/globalpiracy2011/ downloads/study\_pdf/2011\_BSA\_Piracy\_Study-Standard.pdf.

Varian HR (1998) Versioning information goods. Hurley D, Kahin B, Varian HR, eds. Internet Publishing and Beyond (MIT Press, Cambridge, MA), 190–202.

Wei X, Nault BR (2008) Vertically differentiated information goods: Monopoly power through versioning. Working paper, Haskayne School of Business, University of Calgary, Calgary, Alberta, http://ssrn.com/abstract=1677561.

Wei X, Nault BR (2013) Experience information goods: “Versions-toupgrade”. Decision Support Systems 56:494–501.

Wei X, Nault BR (2014) Monopoly versioning of information goods when consumers have group tastes. Production Oper. Management 23(6):1067–1081.

Wilde N, Scully MC (1995) Software reconnaissance: Mapping program features to code. J. Software Maintenance: Res. Practice 7(1):49–62.

Wu S, Chen P, Anandalingam G (2003) Fighting information goods piracy with versioning. Proc. 24th Internat. Conf. Inform. Systems, Seattle, 617–629.

Wu SY, Chen PY (2008) Versioning and piracy control for digital information goods. Oper. Res. 56(1):157–172.
