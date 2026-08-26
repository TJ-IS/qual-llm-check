---
otero_id: 16022
otero_key: "743RBPU2"
title: "Goal attainment on long tail web sites: An information foraging approach"
authors: "J.A. McCart; B. Padmanabhan; D.J. Berndt"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/i.dss.2013.01.025"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
J.A. McCart ⁎, B. Padmanabhan, D.J. Berndt

Information Systems and Decision Sciences, College of Business, University of South Florida, 4202 East Fowler Avenue, CIS 1040, Tampa, FL 33620, United States

## a r t i c l e i n f o

Article history: Received 5 August 201 Received in revised form 5 December 2012 Accepted 21 January 2013 Available online 8 February 2013

Keywords: Information Foraging Theory Long tail Data mining Clickstream analysis

## a b s t r a c t

The long tail has attracted substantial theoretical as well as practical interest, yet there have been few empirical studies that have explicitly examined the factors that drive online conversions at these sites. This research tests several hypotheses derived from Information Foraging Theory (IFT) that pertain to goal achievement on long tail Web sites. IFT introduced concepts of information patches and information scent to model information seeking behavior of individuals, but has mostly been tested in production rule environments where the theory is used to simulate user behavior. Testing IFT-driven hypotheses on real data required learning information patches and scents using an inductive approach and in this paper we adapt existing algorithms for these discovery tasks. Our results based on clickstream data from forty-seven small business Web sites show both the existence of valuable information patches and information scent trails as well as their importance in explaining conversion on these sites. The majority of the hypotheses were supported and we discuss the implications of this for researchers and practitioners.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Relatively recently, a theory called Information Foraging Theory (IFT) has emerged which explains the searching behavior of individuals as they hunt for information [33]. The thesis of IFT is that individuals are driven by a metaphorical sense of “smell” that guides them through “patches” of information in their environment based on their information goal [32]. As they “forage”, individuals evaluate whether to continue browsing in their current patch of information or leave to hunt for another one. Central to this theory are the concepts of information patches and information scent. Information patches are distinct areas of the search environment which differ in informational content. Information scent is the driving force of why a person makes a navigational selection among a group of competing options.

This research tests several hypotheses derived from this theory regarding goal attainment on “long tail” Web sites. The term “long tail” refers to a Web site that resides in the tail of a power law distribution (based on number of visits received). There are several reasons for our focus on this niche. First, long tail sites represent a sizeable, yet underresearched, portion of the Web, offering anything from commodity to specialty products and services. Second, this research was also motivated by strong practical applications where small business sites struggle with understanding conversion. Often such sites receive few repeat visitors and much smaller numbers of visitors in general than any of the larger sites and the need for theory to drive analyses is stronger. We focused on the extreme end of the long tail — where the lack of data is more acute. Third, small business sites have visitors who come in with little prior expectation in terms of brand or product quality and the content the users consume within that site are primarily the reasons for conversion. It is exactly in such cases where “patches” or the lack thereof can make a signi<sup>fi</sup>cant difference. Fourth, larger Web sites like Amazon.com also have continuous content management systems that use A/B testing to optimize pages. In such scenarios it is more likely that valuable patches are likely to predominate (i.e., most content is useful). Small businesses on the other hand often have content that is not yet optimized, a context that increases the importance of valuable and not-valuable patches.

We believe our research makes some important theoretical as well as managerial contributions. To our knowledge this is the <sup>fi</sup>rst systematic empirical study on factors that drive goal attainment on long tail Web sites. Our results show both the existence of valuable information patches and scent trails, as well as their importance in explaining the outcome of a user session at a long tail site. From a theoretical perspective our results lend support to a recent theory on information foraging behavior of individuals by validating several hypotheses derived directly from this theory. However our analysis also highlights areas where the theory may need to be extended, such as by generalizing information patches to represent sets of pages, incorporating memory into foraging decisions, and considering scent trails based on sequences of foraging decisions.

From an applied perspective these results should encourage online <sup>fi</sup>rms to seek a less myopic and more transparent view of the drivers of conversion. Concepts such as an “exit page” or “bounce rate of a page” should give way to building a deeper understanding of not just individual pages but rather the set of informational content that drives success or failure when it comes to conversions. Today most sites – particularly the ones in the long tail – rely on third party analytics (such as Google Analytics) to provide this kind of understanding and existing tools still fall short of providing this level of understanding. Also, IFT presumes knowledge of existing information patches and scents that are then used within a production rule environment. Applying IFT in a real setting however necessitates the need for inductive approaches for learning patches and scents. Our method for learning valuable information patches and scent trails is therefore an important contribution as well.

## 2. Literature review

We discuss related work in two parts. In the <sup>fi</sup>rst part we summarize in three tables (organized by type of problem considered and data sets used) related work in the IS and marketing areas on clickstream analysis, showing a void when it comes to empirical research on long tail sites. In part two we focus speci<sup>fi</sup>cally on Information Foraging Theory to provide readers a brief overview of the key concepts as well as note the prior deductive emphasis in the IFT area.

## 2.1. The case for long tail research

When a user visits a Web site, his or her main objective for visiting has been traditionally classi<sup>fi</sup>ed as either browsing or purchasing [8]. A browsing objective re<sup>fl</sup>ects how a visitor may navigate within a site [9], across multiple sites [31], or how site visits evolve over time [26]. Conversely, a purchasing objective focuses on discovering factors which affect a visitor's propensity to purchase [40]. However, the purchasing objective can be seen as a speci<sup>fi</sup>c instance of the more general goal achievement objective as many sites have purposes other than purchasing, such as <sup>fi</sup>lling in a contact form, posting a message, or responding to a survey. Therefore, the objective of a visitor can be classi<sup>fi</sup>ed as browsing, purchasing, or achieving a goal. Based on these categories, Tables 1–3 provide a summary of prior research.

While the tables summarize the relevant results within each paper, our survey highlighted three signi<sup>fi</sup>cant areas that have been understudied. A very small amount of the research on explaining goal attainment has been speci<sup>fi</sup>c to long tail sites. In fact, almost all of the empirical studies on goal attainment have used data from major Web sites. In addition, previous research has predominately focused on the purchasing aspect of goal achievement. However, other information submitting behaviors, like contact form submission for lead generation, have been largely ignored. Finally, the largest gap we identi<sup>fi</sup>ed is that IFT, a theory of foraging behavior, has not been operationalized using clickstream data, as done in our paper — perhaps one of the most signi<sup>fi</sup>cant contributions of our work. Therefore, our work targets these three under-studied areas by focusing on visitor behavior regarding contact information submission on long tail Web sites using IFT.

## 2.2. Information Foraging Theory

IFT explains the behavior of individuals as they search for information within an environment such as the Web [32]. IFT has been used to inform the design of graphical user interface controls which provide social activity visualizations as navigational cues [43]; determine optimal browsing paths for large pictures displayed in limited viewing areas [44]; explain navigation of source code during program maintenance tasks [23]; help interpret the effects of delay, familiarity, and breadth on users' performance, attitude, and intentions at Web sites [18]; and analyze the role of scent in the decision to browse a menu as opposed to searching a Web site [22].

IFT itself builds on more established theories such as Optimal Foraging Theory (OFT) [41] and the Adaptive Control of Thought-Rational Theory (ACT-R) [2]. OFT is an ecological theory concerned with explaining the foraging behavior of animals as they hunt for food. OFT assumes each animal goes through a search–encounter–decision process as they forage, with the goal being to maximize net energy gained. To maximize energy, the animal is faced with the decision of which prey to eat or how long to forage in a patch. OFT is used to explain behavioral elements of people foraging for information.

ACT-R is a psychological theory of the human mind that includes the cognitive architecture and process by which cognition works. ACT-R is used to explain at a cognitive level why actions are performed. IFT uses a production rule system from ACT-R to determine probabilistically which action is selected based on its utility within the context of a user's current information goal. For example, an action to click on a hyperlink may be chosen over backing up to a previously visited page because following the hyperlink may be more likely to lead to the information being sought. Fig. 1 shows examples of production rules [32, p. 97], which follow the form IF bconditions(s)> THEN baction>. In situations with multiple production rules ful<sup>fi</sup>lling their conditions, con<sup>fl</sup>ict resolution is undertaken where a rule is probabilistically chosen based on its utility: $U _ { i } = P _ { i } G - C _ { i } + \varepsilon [ 2 ] .$ . The utility of a production rule (U) is based on its prior probability of success and prior cost spent when achieving a goal (P and C ), the expected gain from completing the goal (G), and random noise (ε) [2].

Table 1  
Prior literature: results–multiple objectives & browsing.

<table><tr><td>Article</td><td>Research question/purpose</td><td>Results</td></tr><tr><td colspan="3">Multiple objectives</td></tr><tr><td>Kalczynski et al. [21]</td><td>How well do clickstream-complexity measures predict task completion?</td><td>Two Web site-independent clickstream-complexity measures representing the linearity and density of a session were found to perform the best with accuracies between 65% and 93% depending on the task and site.</td></tr><tr><td>Moe [25]</td><td>What visitor behavior can be uncovered from the pattern and type of pages viewed?</td><td>Four groups of visitors differing in search behavior and purchasing horizon were found, along with a fifth group of non-serious visitors. The purchase probability of each group differed depending on how immediate the purchase was and how directed the browsing behavior was.</td></tr><tr><td colspan="3">Browsing</td></tr><tr><td>Bucklin and Sismeiro [9]</td><td>Do visitors change the way they browse a Web site at the session or site level?</td><td>Visitors did dynamically change their browsing behavior at both the session and site level. Within a session browsers exhibited lock-in as they browsed deeper into a Web site. Across sessions a learning effect was observed which reduced the number of pages viewed, but not the duration spent on each page.</td></tr><tr><td>Danaher et al. [15]</td><td>What factors affect visit duration?</td><td>Age interacted with gender, Web site functionality, and the graphical content of a site negatively with regard to the duration spent on a Web site. Age interacted positively, increasing duration for older visitors for higher levels of text and advertisements on a Web site.</td></tr><tr><td>Johnson et al. [20]</td><td>Does reduced search cost lead to increased search?</td><td>Overall search levels were low across the three sectors examined. Browsing behavior was also found to differ depending on sector and level of activity.</td></tr><tr><td>Park and Fader [31]</td><td>Understand cross-site visiting behavior at the individual level.</td><td>An ability to predict when a visitor will first visit a Web site given his or her visiting pattern at another site.</td></tr><tr><td>Zhang et al. [48]</td><td>How do search cost, product characteristics, previous search behavior, and consumer characteristics affect search depth?</td><td>Lower search costs and prior search behavior were positively correlated with search depth. Price and consumer characteristics were positively correlated to search depth only for certain product types.</td></tr></table>

Prior literature: results–purchasing & goal achievement.

<table><tr><td>Article</td><td>Research question/purpose</td><td>Results</td></tr><tr><td colspan="3">Purchasing</td></tr><tr><td>Moe and Fader [26]</td><td>To model individual-level evolving visit patterns over time.</td><td>Examining data at an individual-level contradicted aggregated visit patterns. More frequent visits and an increase in visiting rates increased visitors&#x27; probability of purchasing.</td></tr><tr><td>Moe and Fader [27]</td><td>To model individual-level dynamic conversion behavior.</td><td>The individual-level model contradicted aggregated conversion trends. Over time the overall purchase probability of a visitor decreased, repeat visits had less of an impact on purchasing, and visitor experience raised the purchasing threshold.</td></tr><tr><td>Montgomery et al. [28]</td><td>Can the path a visitor takes through a Web site help predict purchase?</td><td>Future paths were predicted with greater accuracy by the model using paths and by allowing search behavior (i.e., exploratory, directed) to change during a session. Purchase prediction was 10% and 21% accurate after a visitor viewed one page and six pages, respectively.</td></tr><tr><td>Padmanabhan et al. [29]</td><td>What are the implications of using site-centric (i.e., incomplete) data versus user-centric (i.e., complete) data?</td><td>Models using user-centric data outperformed models using site-centric data by a wide margin. Using site-centric data can lead to erroneous results since significant metrics in site-centric models may no longer be significant in user-centric models.</td></tr><tr><td>Sismeiro and Bucklin [40]</td><td>Does viewing the purchasing process as a series of tasks increase prediction accuracy?</td><td>The multi-task model outperformed the competing single task models supporting the series of tasks concept. The model metrics differed in effect sign, size, and significance between tasks indicating some metrics were better predictors of some tasks over others.</td></tr><tr><td>Van den Poel and Buckinx [42]</td><td>How well do different types of metrics predict purchases?</td><td>Detailed clickstream metrics, which were divided according to the underlying content of the page (e.g., product information, community pages), were found to be the most important predictors of purchase.</td></tr><tr><td colspan="3">Goal achievement</td></tr><tr><td>Chatterjee et al. [12]</td><td>To model a visitor&#x27;s probability of clicking a banner advertisement.</td><td>Advertisements exhibited “wearout” such that multiple exposures reduced the probability of a visitor clicking an advertisement. Infrequent visitors were also more likely to click on a banner advertisement than frequent visitors.</td></tr></table>

## 2.3. Information patches

An information patch is a grouping of similar information [32]. In this study, a site-patch refers to an entire Web site as a patch, whereas a page-patch represents a Web page or pages as a patch. Regardless of what a patch represents, a user will continue to forage within a patch until the “expected potential of that patch is less than the mean expected value of going to a new patch” [32, p. 81]. The patch-leaving rule [11] is to forage in a patch as long as $U ( x ) > { \overline { { U } } } ,$ where U(x) is the utility of a forager in their current state and U is the mean utility of other patches [32].

## 2.4. Information scent

Information scent is the use of cues obtained from the text and images associated with a hyperlink to provide information about distal content [32]. As shown in the production rule in Fig. 1a, links are followed based on their relative scents (i.e., highest activation) with respect to a user's current goal. The activation of a link is de<sup>fi</sup>ned as a distance measure between the words of a link and a goal [32].

In summary, IFT has been conceptualized using a production rule system to simulate browsing behavior. However, such a deductive approach is limited because it (1) requires that patches be pre-de<sup>fi</sup>ned for the production rule system and (2) currently considers patches only as a single page (or an entire Web site). This research addresses these limitations by describing how patches (of various sizes) may be learned in an inductive manner.

Table 3 Prior literature: datasets

<table><tr><td>Article</td><td>Type</td><td>Category</td><td>Year</td><td>Duration</td><td>Long tail?</td></tr><tr><td colspan="6">Multiple objectives</td></tr><tr><td>Kalczynski et al. [21]a</td><td>Site-centric</td><td>Government, hardware, insurance, &amp; travel</td><td>Unknown</td><td>Unknown</td><td>Unknown</td></tr><tr><td>Moe [25]</td><td>Site-centric</td><td>Nutritional supplements</td><td>2000</td><td>7 weeks</td><td>Yes</td></tr><tr><td colspan="6">Browsing</td></tr><tr><td>Bucklin and Sismeiro [9]</td><td>Site-centric</td><td>Autos</td><td>1999</td><td>1 month</td><td>No</td></tr><tr><td>Danaher et al. [15]</td><td>User-centric</td><td>Multiple (e.g., Amazon, eBay, Yahoo)</td><td>2000</td><td>1 month</td><td>No</td></tr><tr><td>Johnson et al. [20]</td><td>User-centric</td><td>Books, music, &amp; travel (e.g., Amazon, CDNow, Expedia)</td><td>1997-1998</td><td>1 year</td><td>No</td></tr><tr><td>Park and Fader [31]</td><td>User-centric</td><td>Books &amp; music (e.g., Amazon, CDNow)</td><td>1997-1998</td><td>8 months</td><td>No</td></tr><tr><td>Zhang et al. [48]</td><td>User-centric</td><td>Music, computer hardware, &amp; travel (e.g., Amazon, Dell, Expedia)</td><td>2002</td><td>6 months</td><td>No</td></tr><tr><td colspan="6">Purchasing</td></tr><tr><td>Moe and Fader [26]</td><td>Site-centric</td><td>Books &amp; music (Amazon &amp; CDNow)</td><td>1998</td><td>8 months</td><td>No</td></tr><tr><td>Moe and Fader [27]</td><td>Site-centric</td><td>Books (Amazon)</td><td>1998</td><td>8 months</td><td>No</td></tr><tr><td>Montgomery et al. [28]</td><td>Site-centric</td><td>Books (Barnes &amp; Noble)</td><td>2002</td><td>1 month</td><td>No</td></tr><tr><td>Padmanabhan et al. [29]</td><td>Both</td><td>Multiple</td><td>N/A</td><td>6 months</td><td>No</td></tr><tr><td>Sismeiro and Bucklin [40]</td><td>Site-centric</td><td>Autos</td><td>2000-2001</td><td>70 days</td><td>No</td></tr><tr><td>Van den Poel and Buckinx [42]</td><td>Site-centric</td><td>Food</td><td>2001-2002</td><td>11 months</td><td>Yes</td></tr><tr><td colspan="6">Goal achievement</td></tr><tr><td>Chatterjee et al. [12]</td><td>Site-centric</td><td>Magazine</td><td>1995</td><td>7 months</td><td>No</td></tr></table>

<sup>a</sup> Captured clickstream data from subjects performing a pre-speci<sup>fi</sup>ed experimental task.

![](/api/attachments/743RBPU2/fulltext/images/91c44223fac33b16c0cf5222e43d5925000249c1a23a1fb7345f0ca7d5befca1.jpg)  
Fig. 1. Example production rules [32, p. 97].

## 3. Learning information patches and trails

While IFT has predominantly de<sup>fi</sup>ned a single Web page as a patch, we extend the de<sup>fi</sup>nition of an information patch to a set of Web pages as well. For instance, a good product with a bad warranty highlighted in user reviews may result in a set of pages including the product page, a reviews page, and a warranty information page that are collectively accessed quite often. Also as this example shows, the information patches that <sup>fi</sup>rms may care most about learning are those that can distinguish between good and bad outcomes, such as a goal being satis<sup>fi</sup>ed or not. We de<sup>fi</sup>ne such discriminating information patches as “valuable information patches”. From an inductive learning perspective, itemset learning algorithms in data mining [1] are naturally good candidates to learn information patches since itemsets represent collections of items. Taking this a step further, contrast sets in data mining have been proposed as a mechanism for learning discriminating sets of itemsets between groups [5]. This method can therefore be directly applied to learning valuable information patches as we show further below in this section.

IFT has de<sup>fi</sup>ned information scent as a distance measure between a hyperlink and a user's goal. We retain that spirit but extend this to de-<sup>fi</sup>ne “scent trails”, which are paths foragers follow in their information search. Hence scent trails are page sequences, as compared to sets (for patches). From an inductive perspective, sequential pattern learning algorithms such as SPAM [3] have been used to learn precisely such sequences from symbolic sequences (such as Web pages in a session). We adopt this method to discover scent trails. We further de<sup>fi</sup>ne valuable scent trails to be sequences that discriminate between goal and non-goal sessions and adapt the contrast set method again to learn valuable scent trails. For lack of space we present this in detail for “patches” alone.

## 3.1. Contrast sets

From the data mining literature, contrast sets are a way to <sup>fi</sup>nd differences between groups [5]. A contrast set is a combination of attributes and their values which differ in support among separate groups [5]. Let there be k attributes A $( A _ { 0 } , A _ { 1 } , . . . , A _ { \mathrm { { k } } - 1 } )$ , where $A _ { i }$ can have one of m values $( V _ { i 0 } , \nabla _ { i 1 } , . . . , V _ { i m - 1 } ) .$ A contrast set is a conjunction of attributes de-<sup>fi</sup>ned for n groups $\left( G _ { 0 } , G _ { 1 } , . . . , G _ { n - 1 } \right)$ [5]. For example, a contrast set may be $( P a g e A = 1 ) \land ( P a g e C = 1 )$ , where the attributes represent Web pages and a value of $\ " { } ^ { \cdot \bullet } 1 \ " { }$ signi<sup>fi</sup>es a page was visited. Support in a group is de-<sup>fi</sup>ned as the percentage of instances where the contrast set is true within the group [5]. The support from the previous example may be 5% for goal sessions and 17% for non-goal sessions.

A potential contrast set (PCS) is one where the contrast set (cset) is suf<sup>fi</sup>ciently large in at least one of the groups, where largeness is having a support greater than or equal to a speci<sup>fi</sup>ed minimum support (minSup). Formally, a PCS between two groups is one that satis<sup>fi</sup>es the condition: max(support(cset,G ),support(cset,G ))≥minSup (adapted from Satsangi and Zaiane [35]). A signi<sup>fi</sup>cant contrast set (SCS) is a PCS that also meets the signi<sup>fi</sup>cance condition. Formally, a contrast set is signi<sup>fi</sup>cant between two groups if $P ( c s e t | G _ { 0 } ) \neq P ($ (cset| $G _ { 1 } )$ at a speci<sup>fi</sup>ed alpha level (adapted from Bay and Pazzani [5]). A SCS is hence a valuable information patch since it represents the fact that the set of pages tends to be visited more in one group than another.

## 3.2. Discovering patches

To discover valuable patches, contrast sets were found where the attributes of the set consisted of the distinct pages visited by a user during their session at a Web site. Each Web site contained sessions where either a goal was achieved during a session or not. Sessions were separated and placed into Web site i's goal dataset $( D _ { G i } )$ or non-goal dataset $( D _ { N i } )$ . Each Web site had $N _ { i }$ sessions. $N _ { G i }$ and $N _ { N i }$ denote the sizes of datasets $D _ { G i }$ and $D _ { N i } ,$ respectively.

Frequent itemsets were discovered from each Web site's datasets using the MAFIA (Maximal Frequent Itemsets Algorithm) [10] algorithm<sup>1</sup>. The algorithm was run separately on $D _ { G i }$ and $D _ { N i }$ for each Web site and resulted in a set of frequent itemsets $I _ { G i }$ and $I _ { N i }$ .

Fig. 2 is an example of frequent itemsets mined from a Web site with three Web pages (A, B, and C) (assuming a minSup of 10%). On the left-hand side of the <sup>fi</sup>gure are the itemsets discovered from the goal dataset $( D _ { G i } )$ , whereas the itemsets from the non-goal dataset $\left( D _ { N i } \right)$ ) are on the right-hand side. The itemsets are arranged in a lattice by level according to their size (i.e., how many pages are in the itemset). Lines are drawn between itemsets to show their relation to other itemsets. To the right of each itemset in parentheses is the count of support for the itemset. The empty itemset at level 0 represents the entire dataset.

Potential contrast sets were formed starting with the most general (level 0) frequent itemsets found in either dataset and then continuing on to higher-level itemsets. To evaluate a PCS, a contingency table was populated with the amount of support and non-support for the PCS's itemset from each dataset. When the itemset for a PCS was found in both $I _ { G i }$ and $I _ { N i } ,$ then the contingency table was created where ${ \cal S } _ { G i j } \left( { \cal S } _ { N i j } \right)$ is the count of support for itemset j from Web site i in the goal (non-goal) dataset<sup>2</sup>.

## 3.3. Determining patch value

The signi<sup>fi</sup>cance of each potential contrast set was then calculated using Fisher's exact test [14]. Although prior research has used the $\chi ^ { 2 }$ test for independence to determine signi<sup>fi</sup>cance [5], the approximation of α may suffer when the expected value of at least 20% of the cells in the contingency table are below <sup>fi</sup>ve or any one expected value is less than one [13]. When considering goal achievement on long tail sites, the counts in the contingency table are often too small or imbalanced in their distribution for the $\chi ^ { 2 }$ test to adequately approximate α. Thus, Fisher's exact test, which makes no such approximation, was used instead.

To control the familywise error rate and provide more power to more general PCS, a different α level (adjusted using the Bonferroni method [37]) was used for each level of the itemset lattice. The purpose of such a change in α was to distribute “… <sup>1</sup> of the total α to tests at level 1, <sup>1</sup> to tests at level 2, and so on” [5, p. 304]. This results in greater power being available to test the most general PCSs.

Eq. (1) [5] was used to determine the alpha level (α ) for testing all PCSs at a speci<sup>fi</sup>ed level. In the equation, α is the expected familywise error rate, l is the level, and C is the number of candidate PCSs being tested at level l. The purpose of the min function was to ensure that α was at least as stringent as the previous level for each subsequent level.

$$
\alpha_ {l} = \min \left(\frac {\frac {\alpha}{2 ^ {l}}}{C _ {l}}, \alpha_ {l - 1}\right)\tag{1}
$$

<sup>1</sup> Frequent sequential patterns were discovered from each Web site's datasets using the SPAM (Sequential Pattern Mining) algorithm [3].

<sup>2</sup> When the itemset was missing from one of the datasets $( \mathrm { i . e . }$ , it was not frequent), then the count of support and non-support was unknown. In such a case the support frequency for the contingency table $( S _ { G i j } \ : 0 \mathrm { r } \ : S _ { N i j } )$ was calculated [35] according to the supCount formula: supCount=round(N minSup), where N is $N _ { G i }$ or $N _ { N i }$ and minSup is minimum support.

![](/api/attachments/743RBPU2/fulltext/images/11adec1261911e937d592417329b6b7a4c66faa46faaedb03209f3141a339a60.jpg)  
Fig. 2. Example itemsets by dataset.

Following Bay and Pazzani [5], if a PCS was found to be signi<sup>fi</sup>cant at $\alpha { = } 0 . 0 5$ , then the patch it represents was deemed valuable (see online appendix for a sensitivity analysis). A valuable patch which was predominately visited by users from the goal group was known as a goal patch and placed in the set $P _ { G i } ,$ whereas visitation mostly from the non-goal group resulted in a patch being labeled as a non-goal patch and being placed in the set $P _ { N i \cdot }$ Formally, a patch was deemed a goal patch if $\begin{array} { r } { \frac { S _ { G \bar { y } } } { N _ { G i } } > \frac { S _ { N i j } } { N _ { N i } } , } \end{array}$ and a non-goal patch otherwise. By classifying patches in such a manner, a visitor may signal expected goal outcome to the <sup>fi</sup>rm via the presence or absence of patch visitation.

The numerical value assigned to a valuable patch was determined via the difference formula (Eq. (2)) [47]. Difference values range from zero to two, with a higher number representing a greater difference in support between the two groups.

$$
\text { difference } \left(S _ {G i j}, S _ {N i j}\right) = \frac {\left| \frac {S _ {G i j}}{N _ {G i}} - \frac {S _ {N i j}}{N _ {N i}} \right|}{\frac {1}{2} \left(\frac {S _ {G i j}}{N _ {G i}} + \frac {S _ {N i j}}{N _ {N i}}\right)}\tag{2}
$$

## 4. Information Foraging Theory hypotheses

Table 4 lists the nine IFT hypotheses, with the rationale for each hypothesis provided in Sections 4.1 and 4.2. The table also lists the results of prior studies for each hypothesis, along with whether the hypothesis is testing or extending IFT. For convenience, Table 5 provides a list of common terms used in the hypotheses. More details about the terms can be found in the speci<sup>fi</sup>ed sections (“A” refers to Appendix A in the online supplement).

## 4.1. Information patch

What an information patch represents depends on the level of analysis being examined. At a high level, an entire Web site can be considered a patch. At a lower level, a Web page or set of Web pages may be considered a patch. The <sup>fi</sup>rst four hypotheses (Hypotheses 1–4) in this section examine how browsing behavior can lead to goal achievement by considering the Web site as a patch (i.e., site-patch). A bene<sup>fi</sup>t of taking a site-patch perspective is that only coarse data on browsing behavior is required. The last two hypotheses (Hypotheses 5 and 6) in this section take a more detailed viewpoint by focusing on speci<sup>fi</sup>c pages or sets of pages being visited (i.e., page-patches). Although concentrating on page-patches requires <sup>fi</sup>ner-grained data, the lower level of analysis may tease out differences not seen at the site level between goal and non-goal-achieving foragers.

## 4.1.1. Site-patch

Since a forager has imperfect information and limited computational facilities, an optimal decision of how long to spend in a site is unlikely. Instead, a forager is likely to employ satis<sup>fi</sup>cing [32,39], making a decision that satis<sup>fi</sup>es a need (e.g., rate of information gain) at some speci<sup>fi</sup>ed level. When reading online texts for learning, satis<sup>fi</sup>cing is a commonly used technique [34]. Using satis<sup>fi</sup>cing, a forager will continue to spend time reading pages on a Web site as long as information of value is being obtained. Therefore, a high total duration spent at a site can be associated with obtaining more information relevant to a user's information goal, which leads to Hypothesis 1.

<table><tr><td rowspan="2">Hyp. #</td><td rowspan="2">Hypothesis</td><td colspan="4">Results of prior studiesa</td></tr><tr><td>Sup.</td><td>Not sup.</td><td>Mixed</td><td>Extends IFT?</td></tr><tr><td colspan="6">Information patch-site-patch</td></tr><tr><td>1</td><td>Higher total duration spent in a session will be positively associated with achieving a goal on this long tail Web site.</td><td></td><td></td><td>[29,40]</td><td>No</td></tr><tr><td>2</td><td>Higher number of pages viewed in a session will be positively associated with achieving a goal on this long tail Web site.</td><td>[25]</td><td></td><td>[12,40,42]</td><td>No</td></tr><tr><td>3</td><td>Returning to this site during the same session will be positively associated with achieving a goal on this long tail Web site.</td><td></td><td></td><td></td><td>Partially</td></tr><tr><td>4</td><td>Returning to this site during a different session will be positively associated with achieving a goal on this long tail Web site.</td><td></td><td>[12]</td><td>[40]</td><td>Yes</td></tr><tr><td colspan="6">Information patch-page-patch</td></tr><tr><td>5</td><td>Visiting more highly valued goal page-patches in a session will be positively associated with achieving a goal on this long tail Web site, where value is alternatively computed as the:(a) maximum value of any visited goal page-patch(b) value from the last visited goal page-patch(c) summation of values from all visited goal page-patches.</td><td></td><td></td><td>[25,40,42]b</td><td>Yes</td></tr><tr><td>6</td><td>Higher median total duration spent within visited goal page-patches in a session will be positively associated with achieving a goal on this long tail Web site.</td><td></td><td></td><td></td><td>Partially</td></tr><tr><td colspan="6">Strict information scent</td></tr><tr><td>7</td><td>A lower proportion of repeatedly visited pages in a session will be positively associated with achieving a goal on this long tail Web site.</td><td></td><td></td><td>[25]b</td><td>Yes</td></tr><tr><td>8</td><td>A more linear clickstream in a session will be positively associated with achieving a goal on this long tail Web site.</td><td></td><td></td><td></td><td>Yes</td></tr><tr><td colspan="6">Relaxed information scent</td></tr><tr><td>9</td><td>Following more highly valued goal scent trails in a session will be positively associated with achieving a goal on this long tail Web site, where value is alternatively computed as the:(a) maximum value of any followed goal scent trail(b) value from the last followed goal scent trail(c) summation of values from all followed scent trails.</td><td></td><td></td><td>[28,46]b</td><td>Yes</td></tr></table>

<sup>a</sup> Many studies did not explicitly test hypotheses. Thus, support was determined from variables tested within predictive models.  
b Indicates studies that tested a related hypothesis.

Hypothesis 1. Higher total duration spent in a session will be positively associated with achieving a goal on this long tail Web site.

Prior research has found mixed support for the association between absolute total duration and the achievement of a goal. Positive, negative, and non-signi<sup>fi</sup>cant associations were found dependent on the task on one e-commerce Web site [40]. Positive and non-signi<sup>fi</sup>cant associations were also found using site-centric and user-centric data at another group of e-commerce Web sites [29].

Each additional page visited represents a decision point where the user believed the value of continuing to browse at this site was higher than what they expected to <sup>fi</sup>nd elsewhere. In a similar vein as Hypothesis 1, a forager will continue to visit pages within a Web site as long as information of interest is being obtained. Therefore, a high number of pages viewed at a site can be a proxy for obtaining more information relevant to a user's information goal, which leads to Hypothesis 2.

Table 5 Common terms.

<table><tr><td>Term</td><td>Description</td><td>More details</td></tr><tr><td>Goal page-patch</td><td>Page-patch visited mostly by goal sessions. Valued by difference in proportion of visitation between goal and non-goal sessions.</td><td>Sections 3.3, 4.1.2</td></tr><tr><td>Goal scent trail</td><td>Scent trail followed mostly by goal sessions. Valued by difference in proportion of visitation between goal and non-goal sessions.</td><td>Sections 3.3, 4.2.2</td></tr><tr><td>Linear clickstream</td><td>Browsing complexity: straight path less complex than one with loops.</td><td>Section 4.2.1, A.3</td></tr><tr><td>Page-patch</td><td>Web page or set of pages as a patch.</td><td>Sections 2.3, 4.1.2</td></tr><tr><td>Relaxed information scent</td><td>Scent from portions of a session. Does not assume repeat visitation is inefficient.</td><td>Section 4.2.2, A.4</td></tr><tr><td>Site-patch</td><td>Web site as a patch.</td><td>Sections 2.3, 4.1.1</td></tr><tr><td>Strict information scent</td><td>Scent from an entire session. Repeated page visits seen as inefficient browsing behavior.</td><td>Section 4.2.1, A.3</td></tr></table>

Hypothesis 2. Higher number of pages viewed in a session will be positively associated with achieving a goal on this long tail Web site.

Empirically, support has also been mixed for the association between absolute number of pages viewed and conversion. Prior research has found a positive [25] and mixed association [12] depending on the task [40] or type of pages viewed [42].

The <sup>fi</sup>rst two hypotheses (Hypotheses 1 and 2) test IFT without extending the theory. Both hypotheses test the theory's expectation that users employ the concept of satis<sup>fi</sup>cing when foraging for information [32,39]. As patches are assumed to exhibit diminishing returns, visitors should forage in a patch only as long as they are satis<sup>fi</sup>ed with their rate of information gain.

While foraging within a Web site, a user forms a general opinion of the value of the site. When leaving one site for another, a forager believes greater value may be found elsewhere. However, if a user returns shortly after leaving, the forager was unable to <sup>fi</sup>nd a more valuable Web site. Therefore, the site of interest is more likely than other Web sites to contain the information necessary to ful<sup>fi</sup>ll the user's goal, which leads to Hypotheses 3.

Hypothesis 3. Returning to this site during the same session will be positively associated with achieving a goal on this long tail Web site.

The third hypothesis partially extends IFT. The idea is not novel that a forager would leave a patch when the rate of information gain falls below the mean rate of gain obtainable from the environment. However, the Marginal Value Theorem [11] assumes an optimal forager with perfect information. Since foragers are known to possess imperfect information, the actual judgment on the mean rate of gain obtainable from other patches may be incorrect. Therefore, a forager may return to the original patch after exploring other parts of the environment and realizing the original site still provided the highest rate of information gain.

When the span of time between visits is greater, returning to a Web site demonstrates the positive evaluation of the site in two manners. First, the act of returning to a site indicates the forager originally valued the Web site enough to remember its existence. Second, having a general recollection of the site and then returning also indicates the Web site is expected to contain the information needed to ful<sup>fi</sup>ll the user's goal, which leads to Hypotheses 4.

Hypothesis 4. Returning to this site during a different session will be positively associated with achieving a goal on this long tail Web site.

Prior research has found negative [12], along with positive and non-signi<sup>fi</sup>cant support depending on the task [40] for the association between returning to a Web site after a session has ended and achieving a goal. As far as can be determined, the exit and return of a user during a session has not been examined in prior research.

Hypothesis 4 is considered an extension to IFT because it introduces memory from past sessions. When searching for information, a forager will use information scent to guide them to patches of interest (e.g., a Web site). The level of scent recognized by a forager is dependent on the strength of chunks activated from declarative memory [32]. It is assumed that when a forager visits a Web site of value, greater attention will be paid to the cues that represent that site compared to sites of a lower value. Greater cue attention will in turn more strongly activate the chunks representing those cues in declarative memory [2]. At a later time, when the forager has an information goal that may be achieved from the valuable Web site, those chunks representing the Web site will have a greater probability of being retrieved (than chunks representing lower-valued Web sites) from declarative memory due to being previously activated.

## 4.1.2. Page-patch

As previously discussed, a page-patch consists of a Web page or set of Web pages that collectively provide information for an individual. However, certain page-patches may provide more useful information to a user than others. The identi<sup>fi</sup>cation of which page-patches are useful is likely to be similar among foragers with comparable goals. Patches which are better able to distinguish between goal and non-goal foragers are given higher value than other patches.

Thus, a user who visits more valuable goal page-patches (as de<sup>fi</sup>ned by proportion of visitation) at a Web site is more likely to achieve a goal, which leads to Hypothesis 5.

Hypothesis 5. Visiting more highly valued goal page-patches in a session will be positively associated with achieving a goal on this long tail Web site, where value is alternatively computed as the:

(a) maximum value of any visited goal page-patch

(b) value from the last visited goal page-patch

(c) summation of values from all visited goal page-patches.

Negative and non-signi<sup>fi</sup>cant associations between speci<sup>fi</sup>c individual pages and conversion have been found in prior research [40]. Differences between the types of pages visited and conversion rate have been found at one e-commerce Web site [25]. The actual relationship between types of pages viewed and conversion was found to be mixed at another e-commerce site [42].

Similar to Hypothesis 1, a forager will continue to spend time reading pages within goal patches as long as information of value is being obtained. However, unlike Hypothesis 1, only the time spent on pages within already identi<sup>fi</sup>ed valuable goal page-patches is considered. Thus, a high median total duration spent within goal page-patches at a site can be associated with obtaining more information relevant to a user's information goal, which leads to Hypothesis 6.

Hypothesis 6. Higher median total duration spent within visited goal page-patches in a session will be positively associated with achieving a goal on this long tail Web site.

The hypotheses dealing with page-patches (Hypotheses 5 and 6) are considered an extension because IFT does not de<sup>fi</sup>ne patches as being associated with a particular group of foragers (e.g., goal versus non-goal sessions). Instead, the patchy structure of the Web is assumed to be independent of a forager's information goal [32]. Hypothesis 5 is also an extension to the theory because patches in IFT are not given value independent of the current forager. Instead, the value of a patch is determined by an individual's behavior within that patch (e.g., time spent).

## 4.2. Information scent

This section presents three hypotheses dealing with information scent. In the <sup>fi</sup>rst two hypotheses (Hypotheses 7 and 8), information scent is characterized by considering a user's entire session as a single monolithic event. In both these hypotheses a fairly strict de<sup>fi</sup>nition of information scent is considered, which views any inef<sup>fi</sup>ciencies in a user's clickstream (e.g., backtracking) as having poorer scent. The last hypothesis (Hypothesis 9) takes a more detailed viewpoint by looking at information scent among different fragments of a user's session. In this hypothesis a more relaxed characterization of information scent is used which recognizes that complex sessions may still be of high scent even in the presence of some inef<sup>fi</sup>ciencies.

## 4.2.1. Strict information scent

When a forager has a single well-de<sup>fi</sup>ned goal in mind it would be expected that the user would exhibit a focused search pattern [25]. With a well-de<sup>fi</sup>ned goal, the forager is better able to evaluate the scent of each link and hence make more accurate navigational choices. Viewed as a whole, such navigational choices for a forager with high levels of scent should result in a directed clickstream.

A directed path is characterized by few (if any) repeat visitations of pages, since it is assumed that a rational forager would obtain any and all information from a page the <sup>fi</sup>rst time it was visited. Therefore, a goal is more likely to be achieved when a smaller proportion of pages are visited multiple times at a Web site, which leads to Hypothesis 7.

Hypothesis 7. A lower proportion of repeatedly visited pages in a session will be positively associated with achieving a goal on this long tail Web site.

Taking a <sup>fi</sup>ner-grained conceptualization of strict information scent considers the overall complexity of a user's clickstream, as opposed to just general backtracking behavior. A less complex clickstream is one which exhibits a linear path through a site [36], which is indicative of high scent. As path information is used to determine complexity, backtracking behavior at many different pages rather than a single page may be teased out from a session.

For example, consider a user's browsing behavior at two Web sites. At one site seven pages were visited and four of those pages were unique. All of the non-unique pages were the home page which was used as the main hub for all the other pages being visited. At the other site the same number of total pages and unique pages were visited. At this Web site, however, each non-unique page was different from one another. Although the clickstreams from both Web sites have the same proportion of repeatedly visited pages, the clickstream from the second site is more linear and thus less complex than the second.

With high scent, a forager will exhibit a less complex and more linear clickstream than with low scent. Therefore, a less complex clickstream, in terms of linearity, at a Web site is more likely to lead to goal achievement, which leads to Hypothesis 8.

Hypothesis 8. A more linear clickstream in a session will be positively associated with achieving a goal on this long tail Web site.

Session complexity has been used to successfully discriminate users via their clickstream into high and low scoring groups [24]; in the use of product recommendation agents [36]; and in predicting the completion of informational and e-commerce tasks [21].

## 4.2.2. Relaxed information scent

The previous two hypotheses considered the session as a whole and assumed that any “inef<sup>fi</sup>ciencies” in a user's clickstream were considered indicators of poor scent. However, certain “inef<sup>fi</sup>ciencies” may instead be a part of the natural decision making process of a user.

For example, [25] found that when directed shoppers were deciding between products, their clickstreams demonstrated multiple repeated visits to the pages of the products being considered. Hence, rather than arbitrarily penalizing clickstream complexity, we hypothesize that some more complex clickstreams could actually be positively related to goal achievement. To meet that need, goal scent trails are used in a similar spirit as goal page-patches from Hypothesis 5. Goal scent trails are path fragments that goal-achieving foragers predominately follow. Non-goal scent trails are predominately followed by non-goal-achieving foragers. A user who follows more highly valued goal scent trails is likely to have a goal similar to the goal-achieving foragers on that Web site, which leads to Hypothesis 9.

Hypothesis 9. Following more highly valued goal scent trails in a session will be positively associated with achieving a goal on this long tail Web site, where value is alternatively de<sup>fi</sup>ned as the:

(a) maximum value of any followed goal scent trail

(b) value from the last followed goal scent trail

(c) summation of values from all followed scent trails.

Path information has been used successfully in clickstream research to predict future path selections [28]. Various ways of representing paths have also been tested. The use of path fragments, which take into account the order, adjacency, and recency of information, has been found to be more accurate for predicting future paths than other manners of representing paths [46]. As far as can be determined, the use of path fragments which distinguish between groups of a Web site population has not been examined in prior research.

The <sup>fi</sup>nal three hypotheses (Hypotheses 7–9) are seen as extensions to IFT. Within IFT, scent is viewed as a real-time mechanism that foragers use to select a navigational option (e.g., selecting which link to click next). While all three hypotheses still assume scent works by the same mechanism, an overall level of scent from a forager's aggregated behavior is conceptualized instead. In addition, Hypothesis 9 also extends IFT by introducing the concept of trails of scent that are common among foragers.

## 5. Method

This section details the method followed to test the nine IFT hypotheses. A description of the data sample is provided in Section 5.1. The manner in which each hypothesis' measure was calculated is explained in Section 5.2. Finally, Section 5.3 discusses how the hypotheses were tested.

## 5.1. Data sample

The hypotheses were tested using a site-centric dataset which had 250,162 sessions that visited 47 informational long tail Web sites over a one-year period. The data was collected from a Web-hosting company that specializes in servicing small businesses. The goal being examined was the submission of a contact form. 4979 sessions (1.99%) resulted in the submission of a contact form. Table 6 presents descriptive statistics about the Web sites and sessions used in the analysis.

## 5.2. Measures

Table 7 summarizes the measures used to test the hypotheses<sup>3</sup>. The name of each measure along with a description of how it was calculated is provided. In addition, the hypothesis which corresponds to the measure is also provided in the table. A more in-depth description of the measures is given in the online supplement Appendix A.

Table 6  
Web site and session statistics.

<table><tr><td></td><td>Mean</td><td>St. dev.</td><td>Minimum</td><td>Maximum</td></tr><tr><td colspan="5">Web site statistics</td></tr><tr><td colspan="5">Pages</td></tr><tr><td>Valid pages</td><td>16.36</td><td>13.00</td><td>5</td><td>79</td></tr><tr><td>Excluded  $pages^a$ </td><td>2.04</td><td>0.29</td><td>2</td><td>4</td></tr><tr><td colspan="5">Sessions</td></tr><tr><td>Total sessions</td><td>5322.60</td><td>7473.76</td><td>245</td><td>44,405</td></tr><tr><td>Goal sessions</td><td>105.94</td><td>90.13</td><td>51</td><td>587</td></tr><tr><td>Non-goal sessions</td><td>5216.66</td><td>7427.53</td><td>192</td><td>44,111</td></tr><tr><td colspan="5">other</td></tr><tr><td>Conversion</td><td>5.26%</td><td>5.70%</td><td>0.51%</td><td>24.25%</td></tr><tr><td colspan="5">Session statistics</td></tr><tr><td colspan="5">Pages viewed</td></tr><tr><td>All sessions</td><td>4.91</td><td>5.05</td><td>2</td><td>152</td></tr><tr><td>Goal sessions</td><td>10.34</td><td>7.17</td><td>2</td><td>87</td></tr><tr><td>Before goal</td><td>5.60</td><td>5.26</td><td>1</td><td>84</td></tr><tr><td>Non-goal sessions</td><td>4.80</td><td>4.94</td><td>2</td><td>152</td></tr><tr><td colspan="5">Session duration (min)</td></tr><tr><td>All sessions</td><td>3.78</td><td>6.99</td><td>0.00</td><td>134.75</td></tr><tr><td>Goal sessions</td><td>11.46</td><td>11.96</td><td>0.17</td><td>120.15</td></tr><tr><td>Before goal</td><td>8.80</td><td>9.21</td><td>0.08</td><td>94.17</td></tr><tr><td>Non-goal sessions</td><td>3.62</td><td>6.76</td><td>0.00</td><td>134.75</td></tr></table>

<sup>a</sup> Excluded pages include all contact form and form processing pages.

## 5.3. Hypothesis testing

Each of the metrics was tested individually to determine if they were able to distinguish between goal and non-goal sessions at any long tail Web site. The metrics were tested at the Web site unit of analysis since the goal was to <sup>fi</sup>nd metrics which were signi<sup>fi</sup>cant over multiple long tail sites. Since each Web site had numerous goal and non-goal sessions, the median value was separately taken for each group. The median values for the goal and non-goal sessions were then used as each Web site's paired data points.

The binomial metrics RETURN and VISITED did not use median values since the metrics were only <sup>fl</sup>ags indicating if someone left the site or had visited the site before. Therefore, each Web site was compared according to the probability of a goal occurring given if the user left and returned to the site or stayed at the site the entire session. The RETURN measure compared the P(Goal|Returned) versus P(Goal|Stayed). The VISITED measure compared the P(Goal|Returned) versus P(Goal| New).

The dependent-samples sign test [14] was used to test each hypothesis. The sign test is a non-parametric test of differences between observation pairs and was used because all of its assumptions were fully met; unlike the more assumption stringent exact Wilcoxon signed rank test and t-test [14]. The sign test excludes data points (i.e., Web sites) with no difference in their observation pair (i.e., X =Y ). Web sites retained by the sign test will be referred to as “non-tied” in the results.

## 6. Results

The results of learning patches and trails are described in Section 6.1, while the results of the nine IFT hypotheses are presented in Section 6.2.

## 6.1. Learned patches and trails

A total of 14 (29.79%) and 10 (21.28%) Web sites found patches and trails when mined at an α of 0.05. Table 8 presents descriptive statistics of the learned patches and trails by Web site. The table lists the number of patches or trails found; size, in number of Web pages, of the patches and trails; percentage of the Web site all patches or trails of that site covered; and value of the patch or trail (from Eq. (2)).

Table 9 shows two examples each of discovered patches and trails. The table contains a short description of the Web site and the value and pages that make up the patch or trail. For trails, the order in which the pages are displayed does matter. For patches, page order does not matter.

Table 7 Metrics.

<table><tr><td>Hyp. #</td><td>Metric</td><td>Description</td></tr><tr><td colspan="3">Information patch-site-patch</td></tr><tr><td>1</td><td>SITEDUR</td><td>Duration in seconds spent on a Web site.</td></tr><tr><td>2</td><td>SITEPGS</td><td>Number of pages viewed on a Web site.</td></tr><tr><td>3</td><td>RETURN</td><td>If visitor left the Web site and returned during the same session.</td></tr><tr><td>4</td><td>VISITED</td><td>If user had previously visited the Web site before.</td></tr><tr><td colspan="3">Information patch-page-patch</td></tr><tr><td>5a</td><td>PATCHMAX</td><td>Maximum value of any goal page-patch visited.</td></tr><tr><td>5b</td><td>PATCHLAST</td><td>Value of last goal page-patch visited.</td></tr><tr><td>5c</td><td>PATCHSUM</td><td>Total value of all goal page-patches visited.</td></tr><tr><td>6</td><td>PATCHDUR</td><td>Median duration in seconds spent in all goal page-patches.</td></tr><tr><td colspan="3">Strict information scent</td></tr><tr><td>7</td><td>UNIQUE</td><td>Percentage of unique pages viewed.</td></tr><tr><td>8</td><td>LINEAR</td><td>Linearity of clickstream.</td></tr><tr><td colspan="3">Relaxed information scent</td></tr><tr><td>9a</td><td>TRAILMAX</td><td>Maximum value of any goal trail followed.</td></tr><tr><td>9b</td><td>TRAILLAST</td><td>Value of last goal trail followed.</td></tr><tr><td>9c</td><td>TRAILSUM</td><td>Total value of all goal trails followed.</td></tr><tr><td colspan="3">Other</td></tr><tr><td>n/a</td><td>GOAL</td><td>Whether a goal occurred during the session.</td></tr></table>

## 6.2. Results and discussion

Table 10 presents the results of the nine hypotheses, with more detail provided below.

## 6.2.1. Information patch–site-patch

The <sup>fi</sup>rst hypothesis was supported at α=0.01 (S=33; p-value= 0.0040), where 33 out of 47 Web sites (70.21%) had a higher median duration among goal sessions than non-goal sessions. Goal sessions lasted roughly four minutes before submitting a contact form, while non-goal sessions foraged for about three minutes.

The second hypothesis was not found to be signi<sup>fi</sup>cant at any of the tested alpha levels (S=8; p-value=0.9937). Only eight of the 28 non-tied Web sites (28.57%) had a higher median number of pages viewed for goal sessions versus non-goal sessions. While the results are somewhat unexpected, what is more surprising is the relative sensitivity of the pages viewed measure. By including visits to the contact form page in the analysis, the results of Hypothesis 2 become signi<sup>fi</sup>cant at α=0.05 (S=19; p-value=0.0436)<sup>4</sup>. The lack of robustness for the pages viewed measure found in this study coupled with the mixed associations previous research has found illustrates the dif<sup>fi</sup>culty of using this measure as a proxy for information gathered through browsing.

The third hypothesis was also not supported at any of the tested levels (S=0; p-value=1.0000). None of the 47 Web sites had a higher percentage of goals achieved among foragers who left the site and returned during the same session than visitors that stayed on the site during their entire session. The results indicate a forager was less likely to achieve a goal if the user left a Web site and returned within the same session (the opposite of Hypothesis 3), which was signi<sup>fi</sup>cant at α=0.01 (S=47; p-value=b0.0001), indicating that more focused foragers were more likely to achieve a goal. The results of this hypothesis should take into account the inability of the referring <sup>fi</sup>eld measure to capture if a forager used another tab or Web browser to view another site. Thus, the actual leaving and returning behavior of visitors may be greater than found in this analysis.

Table 8 Patch and trail statistics.

<table><tr><td></td><td>Mean</td><td>St. dev.</td><td>Minimum</td><td>Maximum</td></tr><tr><td colspan="5">Patches</td></tr><tr><td>Patches per site</td><td>11.93</td><td>28.74</td><td>1</td><td>111</td></tr><tr><td>Patch size</td><td>1.82</td><td>0.64</td><td>1</td><td>4</td></tr><tr><td>Patch coverage</td><td>28.63%</td><td>13.85%</td><td>10.00%</td><td>50.00%</td></tr><tr><td>Patch difference (value)</td><td>0.67</td><td>0.16</td><td>0.27</td><td>1.31</td></tr><tr><td colspan="5">Trails</td></tr><tr><td>Trails per site</td><td>4.70</td><td>8.04</td><td>1</td><td>27</td></tr><tr><td>Trail size</td><td>2.15</td><td>0.34</td><td>2</td><td>4</td></tr><tr><td>Trail coverage</td><td>26.47%</td><td>14.80%</td><td>6.90%</td><td>50.00%</td></tr><tr><td>Trail difference (value)</td><td>0.79</td><td>0.19</td><td>0.46</td><td>1.13</td></tr></table>

Median values from each Web site were used to calculate the measures.

The <sup>fi</sup>nal hypothesis to examine the value of the entire Web site as a patch (Hypothesis 4) was signi<sup>fi</sup>cant at α=0.10 (S=29; p-value= 0.0719). 29 of the 47 Web sites (61.70%) had a higher median probability of a form submission among goal sessions when a user had visited the site before. In general, only small differences were found between the proportion of goal sessions that had and had not visited the site before (0.62% difference between groups). Thus, not all Web sites had higher proportions of goal sessions with previous visitations. A potential rationale for the slightly signi<sup>fi</sup>cant <sup>fi</sup>ndings may be because leaving contact information on a Web site has no real monetary cost associated with the action. Therefore, the submission of a contact form may not require the same degree of thought and comparison that purchasing does, which may lower the need for repeat visitations to a site.

## 6.2.2. Information patch–page-patch

The <sup>fi</sup>fth hypothesis expected that visitation of goal patches would be positively associated with goal achievement. The actual value from a forager's visitation of patches was speci<sup>fi</sup>ed in slightly different ways in three sub-hypotheses: maximum value of a patch, value of last patch visited, and total value of all patches visited. The three sub-hypotheses of Hypothesis 5 were all found to be signi<sup>fi</sup>cant at α=0.01 (S=9; p-value=0.0020 for all three measures). Fourteen Web sites out of the 47 total Web sites discovered patches at the

Example patches and trails.

<table><tr><td></td><td>Web site</td><td>Difference</td><td>Pages</td></tr><tr><td colspan="4">Patches</td></tr><tr><td>Outboard motor seller</td><td>0.93</td><td>IndexOverstock bargains20 hp outboard 4-cycle motors</td><td></td></tr><tr><td>Furniture maker</td><td>0.57</td><td>IndexProductsAbout us</td><td></td></tr><tr><td colspan="4">Trails</td></tr><tr><td>Dance lessons</td><td>1.00</td><td>IndexRegistration schedulePhotosTestimonials</td><td></td></tr><tr><td>Cake baker</td><td>0.80</td><td>IndexPhotosPrices</td><td></td></tr></table>

Table 10 Results.

<table><tr><td rowspan="2">Hyp. #</td><td rowspan="2">Metric</td><td colspan="2">N</td><td colspan="3">Sign test</td></tr><tr><td>Total</td><td>Sign  $test^a$ </td><td>S</td><td>p-Value</td><td>Sig.</td></tr><tr><td colspan="7">Information patch-site-patch</td></tr><tr><td>1</td><td>SITEDUR</td><td>47</td><td>47</td><td>33</td><td>0.0040</td><td>***</td></tr><tr><td>2</td><td>SITEPGS</td><td>47</td><td>28</td><td>8</td><td>0.9937</td><td></td></tr><tr><td>3</td><td>RETURN</td><td>47</td><td>47</td><td>0</td><td>1.0000</td><td></td></tr><tr><td>3</td><td>(Opposite)</td><td>47</td><td>47</td><td>47</td><td>&lt;0.0001</td><td>***</td></tr><tr><td>4</td><td>VISITED</td><td>47</td><td>47</td><td>29</td><td>0.0719</td><td>*</td></tr><tr><td colspan="7">Information patch-page-patch</td></tr><tr><td>5a</td><td>PATCHMAX</td><td>14</td><td>9</td><td>9</td><td>0.0020</td><td>***</td></tr><tr><td>5b</td><td>PATCHLAST</td><td>14</td><td>9</td><td>9</td><td>0.0020</td><td>***</td></tr><tr><td>5c</td><td>PATCHSUM</td><td>14</td><td>9</td><td>9</td><td>0.0020</td><td>***</td></tr><tr><td>6</td><td>PATCHDUR</td><td>14</td><td>14</td><td>13</td><td>0.0009</td><td>***</td></tr><tr><td colspan="7">Strict information scent</td></tr><tr><td>7</td><td>UNIQUE</td><td>47</td><td>45</td><td>45</td><td>&lt;0.0001</td><td>***</td></tr><tr><td>8</td><td>LINEAR</td><td>47</td><td>21</td><td>18</td><td>0.0007</td><td>***</td></tr><tr><td colspan="7">Relaxed information scent</td></tr><tr><td>9a</td><td>TRAILMAX</td><td>10</td><td>6</td><td>6</td><td>0.0156</td><td>**</td></tr><tr><td>9b</td><td>TRAILLAST</td><td>10</td><td>6</td><td>6</td><td>0.0156</td><td>**</td></tr><tr><td>9c</td><td>TRAILSUM</td><td>10</td><td>6</td><td>6</td><td>0.0156</td><td>**</td></tr></table>

Hypotheses 5a–c and 9a–c are each signi<sup>fi</sup>cant at <sup>α</sup>.  
<sup>a</sup> Sites with no difference between goal and non-goal sessions are omitted.  
⁎ Signi<sup>fi</sup>cant at α≤0.10.  
⁎⁎ Signi<sup>fi</sup>cant at α≤0.05.  
\*\*\* Signi<sup>fi</sup>cant at α≤0.01

0.05 signi<sup>fi</sup>cance level, with only nine of those 14 sites (64.29%) being non-tied. All nine of the non-tied Web sites had goal sessions with higher median values for the most valuable patch visited, last patch visited, and sum of all patches visited.

On average, foragers visited 2.75 patches per session. With so few patches being visited it was possible that some of the measures did not differ from one another by a great deal. For example, sessions that only visited a single patch would have the same value for all three measures. However, as foragers visited almost three patches per session, the average value of was at least 0.42 points higher than either of the other measures, making it unlikely the PATCHSUM measure included only the same patches as the other two measures. For the other two measures though, the average difference between PATCHMAX and PATCHLAST was only 0.03 points, indicating many sessions may have had the same patch be the most valuable and last patch visited. Therefore, even though both sub-hypotheses were supported, the similarity of each measure means the actual impact of the most valuable and last visited patch cannot be reliably separated from one another.

The sixth hypothesis was also supported at α=0.01 (S=13; p-value=0.0009). Thirteen of the 14 non-tied Web sites (92.86%) with discovered patches had goal sessions spend a higher median duration of time within patches than non-goal sessions spent in patches. On average, goal sessions spent almost three-quarters of a minute more in patches than non-goal sessions.

## 6.2.3. Strict information scent

Hypothesis 7 was the <sup>fi</sup>rst of two hypotheses that de<sup>fi</sup>ned information scent in a strict manner. The results found that goal achieving sessions would visit fewer duplicate pages than non-goal sessions, supporting the hypothesis at α=0.01 (S=45; p-value=b0.0001). All 45 of the non-tied Web sites had goal sessions with a higher median percentage of unique pages viewed than non-goal sessions, with goal sessions viewing, on average, almost 78% unique pages and non-goal sessions viewing only about 70%.

Hypothesis 8 also viewed information scent in a strict manner; however, this hypothesis took a <sup>fi</sup>ner-grained conceptualization by examining the complexity of a user's session. The hypothesis was found to be signi<sup>fi</sup>cant at α=0.01 (S=18; p-value=b0.0001). Eighteen of the 21 non-tied Web sites (85.71%) had higher median linear clickstream values for goal sessions compared to non-goal sessions. The goal sessions had an average linear clickstream value of 0.69 compared to the average value of 0.57 for non-goal sessions.

## 6.2.4. Relaxed information scent

The <sup>fi</sup>nal hypothesis examined is information scent from a relaxed viewpoint, where fragments of paths were examined. The value obtained from a forager following a trail was speci<sup>fi</sup>ed in three sub-hypotheses: maximum value of a trail, value of last trail followed, and total value of all trails followed. The three sub-hypotheses were all found to be significant at α=0.05 (S=6; p-value=0.0156 for all three measures). Ten Web sites out of the 47 total sites discovered trails at the 0.05 signi<sup>fi</sup>cance level, with only six of those 10 sites (60.00%) being non-tied. All six of the non-tied Web sites had goal sessions with higher median values for the most valuable trail followed, last trail followed, and sum of all trails followed.

On average, foragers followed 1.60 trails per session. As many foragers only followed one to two trails per session, the difference in value between the three trail measures (0.26 to 0.33) failed to reveal a clear and distinct difference. Thus, even though the sub-hypotheses were supported, the actual impact of each measure cannot be reliably separated from one another.

## 7. Conclusions and future work

This research sought to explain goal achievement (i.e., choice behavior) at limited traf<sup>fi</sup>c long tail Web sites using Information Foraging Theory (IFT) [32,33]. The thesis of IFT is that individuals are driven by a metaphorical sense of smell that guides them through patches of information in their environment. Having a foundation in both psychology and ecology, IFT draws from both disciplines to explain the mechanisms and the resulting behavior of information foragers.

This research demonstrated how IFT may be used as a theoretical basis for clickstream research. The core concepts of IFT were quanti<sup>fi</sup>ed and tested outside of a production rule environment using clickstream data. In addition, theoretical extensions were introduced which considered memory of past Web site visitation, forager-independent valuation of patches and trails, and re<sup>fi</sup>ned de<sup>fi</sup>nitions of scent. The results supported many of the core concepts and theoretical extensions of IFT. Thus, this research not only demonstrated the ability of IFT to explain goal achievement, but also introduced theoretical extensions which provide a more in-depth explanation of goal behavior.

This research also presented a method on how to learn patches and scent trails using contrast sets [5]. Measures were introduced which quantify a forager's visitation of patches and trail following behaviors. For Web sites that discover patches and trails, the measures are capable of distinguishing goal from non-goal sessions. Using IFT as a guiding theoretical framework, traditionally under-studied long tail Web sites were able to be examined even in light of their sparse datasets. This research <sup>fi</sup>lled a void in the literature by being among the <sup>fi</sup>rst to empirically study goal achievement on long tail Web sites. Taken together these machine learning approaches lay out a novel pathway for further clickstream research based on IFT.

In addition to the research-oriented contributions of this work, these IFT inspired methods may <sup>fi</sup>nd more immediate applications. Foremost, the existence of information patches and scent trails postulated by IFT offers a useful perspective on Web site traf<sup>fi</sup>c patterns. By identifying small, tightly focused patches and trails, these methods help support a more meaningful analysis by practitioners. Currently, tools such as link analysis or other visualization techniques are used to understand Web site traf<sup>fi</sup>c patterns. Unlike these tools, IFT raises the level of abstraction above the individual page level, instead emphasizing more natural groupings of information content.

The automated patch and trail discovery techniques presented in this paper make IFT-driven analysis more accessible to sites. A Web site designer or online advertiser could look to the distinguishing patches and trails for insights on interesting visitor behaviors that distinguish between “goal” and “non-goal” sessions. Recall (from Section 3) the previous example of a patch that included product, warranty, and review pages, which highlighted a potentially troublesome product experience. These types of patches and trails represent actionable items for both Web site designers, as well as more directed programmatic interventions to better manage customer experiences. It seems quite reasonable to expect that such methods will <sup>fi</sup>nd their way into widely available Web analytic toolkits (the Web hosting provider who made these datasets available is in the process of integrating analyses based on patches and scent trails aimed at a toolkit for small business sites).

Future research studies will examine the concept of patches and trails in more detail. One avenue of research is the discovery and investigation of “stinky patches”, which turn visitors away from a site. Besides potentially providing a more complete understanding of visitor behavior, uncovering “stinky patches” can also provide a rich target for site improvement. Patches (of the “non-stinky” variety) may also prove useful in online advertising. Recent research has examined the optimal design for online advertisements [17] and can be extended to include optimizing landing pages from learned patches as well. Another avenue of research may incorporate page content to form topically-relevant patches and trails, or even uncover intra-page patches. One popular application area for this method is sentiment analysis in text. While the literature in this area [4,45] looks at the semantics of content in pages, there may be opportunities to extend these ideas by learning positive or negative patches — reviews, or paragraphs, that most impact conversion.

The concept of patches and trails can also be used as a means of highlighting potentially useful information for end-users based on patterns of access. For instance, Willet et al. [43] used graphical indicators on GUI controls to indicate popular or under-explored areas of information based on usage patterns. The use of such controls may be helpful in information-intensive domains, such as healthcare. A study examining information foraging behavior of physicians in a trauma emergency department found roughly half of the examined physicians' time was spent gathering information, with roughly 16% of that time spent reading patients' electronic health records (EHRs) [38]. Thus, to facilitate information gathering activities, patches of documents within a patient's EHR can be discovered and presented to the provider. However, instead of presenting patches solely based on all other providers' usage patterns, patches can be learned based on providers and/or patients with speci<sup>fi</sup>c characteristics. For instance, discovering patches based on provider spe cialty (e.g., oncology), type of provider (e.g., physician, nurse), provider expertise (e.g., resident versus attending), patient population (e.g., patients with post-traumatic stress disorder (PTSD)), or any combination thereof. Furthermore, the idea can be further abstracted by using the type of documents within the EHR being viewed (e.g., orthopedic surgery consult document, nursing triage document) along with topic modeling [6,7] to infer the types and content of documents that make up the discovered patches. Thus, documents from new patients or patients with a single provider (i.e., those with a sparseness of usage data) can be similarly abstracted, matched to pre-discovered patches, and then presented to the provider.

Web search is another interesting area where patches can be used to potentially provide a user with a richer set of information. Consider a query such as “places to visit in Barcelona”. Traditional search engines today return a ranked list of individual Web pages. Instead, if a search engine tracks users of this query across sites, and learns that many users visit two pages of information on famous sites in Barcelona and then usually also visit a tour bus site that organizes tours in the city, it may be useful to present the set of three links as a popular “patch” for this particular query. Note that in this case the pages related to actual sites are likely more relevant than the Web site corresponding to the tour bus site, which otherwise may not rank in the top few returned links at all. Dean and Henzinger [16] for instance had presented an early approach for <sup>fi</sup>nding Web pages related to a given page that is known to be useful for a user. An implicit suggestion in that approach is that the set of related pages is relevant to the user. However they do not discuss how such a set can be inductively learned from usage data, which is where the approach presented in this paper is potentially useful.

One of the challenges in learning such patches is of course being able to track users across multiple pages after they leave the search engine. While toolbars enable such tracking, it is still not widely used for this purpose. Another approach to possibly learning such patches might be to utilize intelligent Web crawling from a speci<sup>fi</sup>c page of interest. Recent work [30] shows that the Web exhibits both topic and status locality, where pages with short link distances between them are more likely to be similar in both their status as well as their content topic. Such a cluster of related pages can then be augmented with PageRank to return potentially relevant information patches to users.

Generalizing beyond the Web search example, today's recommender systems typically operate at the single object level, i.e. recommending a single page or song and then grouping together the best recommendations into a list that is presented to a user. There may be interesting opportunities to extend this toward recommending information patches, that contain sets of interesting objects that are often consumed together.

There are two possibly interesting directions. In the <sup>fi</sup>rst approach, the list that is generated can be considered an information patch. There is much work in the recommender systems area now that indeed takes a similar perspective. While not using the term “patches” or even necessarily learning such frequently visited sets, this research frames the problem as determining a set of items to recommend to optimize possibly multiple objectives. Ziegler et al. [49] for instance argues that the recommended list can be improved by ensuring diversity in the topics present in the list. In the second approach, it is possible that these systems recommend a list of patches, not a list of individual items. This is closer in spirit to the Web search example presented above, but is not currently used in popular recommender systems online.

While many of the examples above highlight potentially impactful future ideas in using information patches, recent work, also in the recommender systems area, provides some insights into how trails can be incorporated into effective recommendations. Hariri et al. [19] present an approach for music recommendation, that essentially learns sequences of latent topics in songs that people listen to, and then use such a sequence (or trail) to make predictions on the next song to recommend in a playlist. Indeed, their work utilizes user playlists – which represent curated sequences of songs across a large number of users – to learn such latent topic sequences in music.

Beyond just information patches or trails it may be interesting to consider context sensitive variants of these as well. As mobile devices (and apps) proliferate, information patches might be appropriately personalized as well. For instance, a restaurant query on a mobile phone might need to pull together information from multiple apps that are relevant to construct a personalized information patch that is returned to a user. More generally, the above examples in healthcare, Web search and recommender systems provide exciting ideas for future research that extend the ideas of information patches and trails further. We hope to examine some of these in future work.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at http:// dx.doi.org/10.1016/j.dss.2013.01.025.

## References

[1] R. Agrawal, R. Srikant, Fast algorithms for mining association rules in large databases, Proc. 20th Internat. Conf. Very Large Data Bases, 1994, pp. 487–499, San Francisco, CA.

[2] J. Anderson, D. Bothell, M. Byrne, S. Douglass, C. Lebiere, Y. Qin, An integrated theory of the mind, Psychological Review 111 (2004) 1036–1060.

[3] J. Ayres, J. Flannick, J. Gehrke, T. Yiu, Sequential pattern mining using a bitmap representation, Proc. 8th Internat. Conf. Knowledge Discovery Data Mining (KDD-02), 2002, pp. 429–435, Edmonton, Alberta, Canada.

[4] X. Bai, Predicting consumer sentiments from online text, Decision Support Systems 50 (2011) 732–742.

[5] S. Bay, M. Pazzani, Detecting change in categorical data: mining contrast sets, Proc. 5th Internat. Conf. Knowledge Discovery Data Mining (KDD-99), 1999, pp. 302–306, San Diego, CA.

[6] D. Blei, Probabilistic topic models, Communications of the ACM 55 (2012) 77–84.

[7] D. Blei, A. Andrew, M. Jordan, Latent Dirichlet allocation, Journal of Machine Learning Research 3 (2003) 993–1022.

[8] R. Bucklin, J. Lattin, A. Ansari, S. Gupta, D. Bell, E. Coupey, J. Little, C. Mela, A. Montgomery, J. Steckel, Choice and the Internet: from clickstream to research stream, Marketing Letters 13 (2002) 245–258.

[9] R. Bucklin, C. Sismeiro, A model of Web site browsing behavior estimated on clickstream data, Journal of Marketing Research 40 (2003) 249–267.

[10] D. Burdick, M. Calimlim, J. Gehrke, MAFIA: a maximal frequent itemset algorithm for transactional databases, Proc. 17th Internat. Conf. Data Engineering, 2005, pp. 443–452, Heidelberg, Germany.

[11] E. Charnov, Optimal foraging, the marginal value theorem, Theoretical Population Biology 9 (1976) 129–136.

[12] P. Chatterjee, D. Hoffman, T. Novak, Modeling the clickstream: implications for Web-based advertising efforts, Marketing Science 22 (2003) 520–541.

[13] W. Cochran, Some methods for strengthening the common $\chi ^ { 2 }$ tests, Biometrics 10 (1954) 417–451.

[14] W. Conover, Practical Nonparametric Statistics, 3rd edition John Wiley & Sons, Inc., New York, NY, 1999.

[15] P. Danaher, G. Mullarkey, S. Essegaier, Factors affecting Web site visit duration: a cross-domain analysis, Journal of Marketing Research 43 (2006) 182–194.

[16] J. Dean, M. Henzinger, Finding related pages in the world wide web, Computer Networks 31 (1999) 1467–1479.

[17] J. Deane, P. Pathak, Ontological analysis of Web surf history to maximize the click-through probability of Web advertisements, Decision Support Systems 47 (2009) 364–373.

[18] D. Galletta, R. Henry, S. McCoy, P. Polak, When the wait isn't so bad: the interacting effects of Website delay, familiarity, and breadth, Information Systems Research 17 (2006) 20–37.

[19] N. Hariri, B. Mobasher, R. Burke, Context-aware music recommendation based on latent topic sequential patterns, 6th ACM Conf. on Recommender Sys., 2012, pp. 131–138, New York, NY.

[20] E. Johnson, W. Moe, P. Fader, S. Bellman, G. Lohse, On the depth and dynamics of online search behavior, Management Science 50 (2004) 299–308.

[21] P. Kalczynski, S. Senecal, J. Nantel, Predicting on-line task completion with clickstream complexity measures: a graph-based approach, International Journal of Electronic Commerce 10 (2006) 121–141.

[22] M. Katz, M. Byrne, Effects of scent and breadth on use of site-speci<sup>fi</sup>c search on e-commerce Web sites, ACM Transactions on Human-Computer Interaction 10 (2003) 198–220.

[23] J. Lawrance, R. Bellamy, M. Burnett, Scents in programs: does information foraging theory apply to program maintenance? IEEE Symposium Visual Languages Human-Centric Computing, Coeur d' Alene, ID, 2007, pp. 15–22.

[24] J. McEneaney, Graphic and numerical methods to assess navigation in hypertext, International Journal of Human Computer Studies 55 (2001) 761–786.

[25] W. Moe, Buying, searching, or browsing: differentiating between online shoppers using in-store navigational clickstream, Journal of Consumer Psychology 13 (2003) 29–39.

[26] W. Moe, P. Fader, Capturing evolving visit behavior in clickstream data, Journal of Interactive Marketing 18 (2004) 5–19.

[27] W. Moe, P. Fader, Dynamic conversion behavior at e-commerce sites, Management Science 50 (2004) 326-335.

[28] A. Montgomery, S. Li, K. Srinivasan, J. Liechty, Modeling online browsing and path analysis using clickstream data, Marketing Science 23 (2004) 579–595.

[29] B. Padmanabhan, Z. Zheng, S. Kimbrough, Personalization from incomplete data: what you don't know can hurt, Proc. 7th Internat. Conf. Knowledge Discovery Data Mining (KDD-01), 2001, pp. 154–163, San Francisco, CA.

[30] G. Pant, P. Srinivasan, Predicting web page status, Information Systems Research 21 (2010).345-364

[31] Y. Park, P. Fader, Modeling browsing behavior at multiple Websites, Marketing Science 23 (2004) 280–303.

[32] P. Pirolli, Information Foraging Theory: Adaptive Interaction with Information, Oxford University Press, New York, NY, 2007.

[33] P. Pirolli, S. Card, Information foraging, Psychological Review 106 (1999) 643–675.

[34] W. Reader, S. Payne, Allocating time across multiple texts: sampling and satis<sup>fi</sup>cing, Human Computer Interaction 22 (2007) 263–298.

[35] A. Satsangi, O. Zaiane, Contrasting the contrast sets: an alternative approach, Proc. 11th Internat. Database Engineering Applications Symposium, 2007, pp. 114–119, Banff, Alberta, Canada.

[36] S. Senecal, P. Kalczynski, J. Nantel, Consumers' decision-making process and their online shopping behavior: a clickstream analysis, Journal of Business Research 58 (2005) 1599–1608.

[37] J.P. Shaffer, Multiple hypothesis testing, Annual Review of Psychology 46 (1995) 561–584.

[38] N. Shang, T. Kannampallil, A. Franklin, Information foraging behavior in a trauma emergency department, AMIA 2012 Annual Symposium, 2012, Chicago, IL.

[39] H. Simon, Rational choice and the structure of the environment, Psychological Review 63 (1956) 129–138.

[40] C. Sismeiro, R. Bucklin, Modeling purchase behavior at an e-commerce Web site: a task-completion approach, Journal of Marketing Research 41 (2004) 306–323.

[41] D. Stephens, J. Krebs, Foraging Theory, Princeton University Press, 1986.

[42] D. Van den Poel, W. Buckinx, Predicting online-purchasing behaviour, European Journal of Operational Research 166 (2005) 557–575.

[43] W. Willett, J. Heer, M. Agrawala, Scented widgets: improving navigation cues with embedded visualizations, IEEE Transactions on Visualization and Computer Graphics 13 (2007).1129–1136.

[44] X. Xie, H. Liu, W. Ma, H. Zhang, Browsing large pictures under limited display sizes JEEE Transactions on Multimedia 8 (2006) 707–715.

[45] K. Xu, S.S. Liao, J. Li, Y. Song, Mining comparative opinions from customer reviews for competitive intelligence, Decision Support Systems 50 (2011) 743–754

[46] Q. Yang, T. Li, K. Wang, Building association-rule based sequential classi<sup>fi</sup>ers for Web-document prediction, Data Mining Knowledge Discovery 8 (2004) 253–273.

[47] Y. Yang, B. Padmanabhan, Segmenting customer transactions using a pattern-based clustering approach, Proc. 3rd IEEE Internat. Conf. Data Mining, 2003, pp. 411–418, Melbourne, FL.

[48] J. Zhang, X. Fang, O.L. Sheng, Online consumer search depth: theories and new <sup>fi</sup>ndings, Journal of Management Information Systems 23 (2006) 71–95.

[49] C. Ziegler, S. McNee, J. Konstan, G. Lausen, Improving recommendation lists through topic diversi<sup>fi</sup>cation, 14th Internat. World Wide Web Conf., 2005, pp. 22–32, New York, NY.

James A. McCart is a Research Health Science Specialist at the Health Services Research and Development (HSR&D)/Rehabilitation Research and Development (RR&D) Center of Excellence at the James A. Haley Veterans Hospital. His research interests include the use of data and text mining and natural language processing in applications for health informatics, clickstream analysis, and information retrieval. His work has been published in Communications of the ACM, Journal of the American Medical Informatics Association, Journal of Computer Information Systems, and Biomedical Informatics Insights. His work in information retrieval and natural language processing has also been funded by the Department of Veterans Affairs' HSR&D and QUERI services. He received his BS in Information Systems at Purdue University and a MS and PhD in Management Information Systems from the University of South Florida.

Balaji Padmanabhan is Anderson Professor of Global Management and Associate Professor of Information Systems & Decision Sciences at the University of South Florida. His research addresses data analytics for business applications, algorithms for online news recommender systems, service quality and customer churn, behavioral pro<sup>fi</sup>ling and pattern discovery from customer databases. His work has been published in both computer science and information systems journals including Management Science, Information Systems Research, MIS Quarterly, INFORMS Journal on Computing, Decision Support Systems, IEEE TKDE and ACM TMIS. He received a B.Tech from the Indian Institute of Technology (IIT) and a PhD from New York University (NYU). His professional service includes work as Associate Editor and Program Committee Member of several academic journals and conferences. He has worked with several <sup>fi</sup>rms on technical, strategic and educational issues related to business and data analytics and has also created and taught undergraduate, MBA/MS and doctoral courses in areas related to business/data analytics, computational thinking and electronic commerce.

Donald I. Berndt is an Associate Professor in the Information Systems and Decision Sciences Department in the College of Business at the University of South Florida (USF). He received his Ph D. in Information Systems from the Stern School of Business at New York University. He also holds a M S. in Computer Science from the State University of New York at Stony Brook and a B S. from the University of Rhode Island. Dr. Berndt's research and teaching interests include the intersection of arti<sup>fi</sup>cial intelligence and database systems, data warehousing, data and text mining, as well as a long-standing interest in parallel programming. Of particular interest is the application of data and knowledge management techniques in the healthcare sector, including work on text mining electronic medical records as part of the Consortium for Healthcare Informatics (CHIR), a multi-institution Department of Veterans Affairs (VA) research initiative. His work has appeared in leading journals, including Communications of the ACM, IEEE Computer, Decision Support Systems, Discrete Applied Mathematics, Journal of Biomedical Informatics, and Journal of the American Medical Informatics Association. Along with his academic focus, he has been involved in a series of entrepreneurial ventures most recently co-founding SiteWit.com, a data mining-based online advertising company, after co-founding Medegy Inc. in the USF Business Incubator, which focused on transferring healthcare data warehousing to the commercial marketplace. Previously, Dr. Berndt worked at Yale University and Scienti<sup>fi</sup>c Computing Associates, where he participated in the development of commercial versions of the Linda parallel programming environment. He also developed arti<sup>fi</sup>cial intelligence applications in academic settings and at Cognitive Systems, Inc.
