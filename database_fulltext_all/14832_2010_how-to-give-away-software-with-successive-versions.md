---
otero_id: 14832
otero_key: "M4GG8BP4"
title: "How to give away software with successive versions"
authors: "Zhengrui Jiang"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.05.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# How to give away software with successive versions<sup>☆</sup>

Zhengrui Jiang

College of Business, Iowa State University, 2340 Gerdin Business Building, Ames, IA 50011-1350, United States

## a r t i c l e i n f o

Article history: Received 15 February 2009 Received in revised form 6 April 2010 Accepted 4 May 2010 Available online 31 May 2010

Keywords: Free software Bass model Multi-generation diffusion model Software versions Software promotion

## a b s t r a c t

Free software offer as a promotional tool has been employed by software <sup>fi</sup>rms of all sizes. In this research, we propose an extended multi-generation diffusion model that separates substitution from switching, and develop methodologies to help a <sup>fi</sup>rm determine the optimal number of free adoptions for each version. Our analyses show that due to the word-of-mouth effect, free offer can help increase a <sup>fi</sup>rm's total pro<sup>fi</sup>t for all versions of a product. Furthermore, we <sup>fi</sup>nd that in the presence of low-valuation free adopters, the optimal number of high-valuation free adopters decreases, the total number of free adopters increases, and the total pro<sup>fi</sup>t improves substantially as a result.

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

An interesting phenomenon observed in today's market is the sheer number of software products being given away through various distribution channels. For instance, in order to promote their new products, many software <sup>fi</sup>rms simply make their proprietary products available for free download from either their own websites or other third-party sites such as www.download.com. From the Web, we can <sup>fi</sup>nd thousands of free software products being offered in various forms. Some free software comes with content limitations. A well-known example is Acrobat Reader, which can read PDF <sup>fi</sup>les but does not offer the functionality to create PDF <sup>fi</sup>les. Other free software products are provided with time limitations. For instance, the 30-day trial version of Minitab includes all the functionalities of the full-<sup>fl</sup>edged commercial version, but the free version will stop functioning after 30 days. In addition to these “limited” types, we also observe numerous free software products being given away with neither time nor content limitations. Examples include personal <sup>fi</sup>nancial management software Simply Money [8], small business accounting software Simply Accounting [5], and utility software SpyBlocker [4].

In this study, we focus on free software offers without time or content limitations. This type of free software is typically available only during a promotional period or for a limited quantity. For instance, Simply Money and Simply Accounting were given away only to the <sup>fi</sup>rst million customers who requested for them. Once the promotion ends, a <sup>fi</sup>rm starts charging a price for the new product. Although we consider only free software offer without limitations, the analyses and <sup>fi</sup>ndings of this research provide a basis for studying other types of offerings with time and/or content limitations.

Prior research on free software can be broadly classi<sup>fi</sup>ed into three categories. The <sup>fi</sup>rst category focuses on the network externality side of the bene<sup>fi</sup>t. For instance, Haruvy and Prasad [12,13] study how a <sup>fi</sup>rm can take advantage of the network externality effect of a new software product by introducing a limited version to go with the full-<sup>fl</sup>edged commercial version. In another empirical study, Gallaugher and Wang [10] test the impact of free software on commercial software in markets where both freeware and paid software are available. Research in this category concludes that because of network externality, free adopters increase future adopters' valuation of a software product. As shown in prior research, a larger network has a positive effect on price in many software markets [6]. Therefore, free software offer can indirectly lead to a higher pro<sup>fi</sup>t for a software <sup>fi</sup>rm. The second category of research focuses on the demonstration effect of free software versions with limited functionalities. The studies by Manica et al. [19] and Faugère and Tayi [9] propose methodologies to optimize the design of demo versions, i.e., deciding their optimal content and/or time limitations. In a more recent article, Hui et al. [14] study the economics of shareware with limited features. Among others, the authors conclude that shareware quality tends to increase if potential customers are more averse to uncertainty and tends to decrease in the presence of piracy. In the third category of research on free software, the word-of-mouth effect of the free software adopters is examined. Based on a single-version software product, the study by Jiang and Sarkar [16] shows that even if other documented bene<sup>fi</sup>ts such as network externality and demonstration effect are insigni<sup>fi</sup>cant, a software <sup>fi</sup>rm can still bene<sup>fi</sup>t from free offer; this is because the word-of-mouth effect from the free adopters can help speed up the diffusion of a new product. This study is in line with prior research in the third category. We also focus on software products for which the word-of-mouth effect is the only signi<sup>fi</sup>cant bene<sup>fi</sup>t that a <sup>fi</sup>rm can reap from free offer. The primary difference between the prior research by Jiang and Sarkar [16] and this study is that the former considers products with a single version while this study examines software products with multiple successive versions.

For both economic and software engineering considerations, most software <sup>fi</sup>rms do not attempt to deliver a complete and perfect product in one development cycle. Instead, they choose to keep rolling out new versions one after another, with later versions typically coming with added functionality [7]. Microsoft Windows and Of<sup>fi</sup>ce represent two good examples of such practice, with new versions released every few years. With software versioning, users enjoy everimproving features of software products, often at the cost of paying the same line of products more than once in their lifetime. Besides generating repeated sales, successive versioning brings a number of other important bene<sup>fi</sup>ts to software <sup>fi</sup>rms. It delivers quicker return to investment, limits the impact of market uncertainty, reduces the risk of project failure, and provides <sup>fi</sup>rms with opportunities to re<sup>fi</sup>ne their development methodologies and improve product quality in later development cycles.

Although we have not seen any formal analysis on free offer policy for successive software versions, the diffusion of products with multiple generations has been studied in the diffusion literature. The extant multi-generation diffusion models are all extensions of the seminal Bass model [1], which is credited as “the most popular model in the <sup>fi</sup>eld of marketing” ([21], p.83). The Bass model is applicable only to products with one generation. The <sup>fi</sup>rst multi-generation extension of the Bass model is proposed by Norton and Bass [20]. Following Norton and Bass, other researchers develop extensions and variations to the Norton and Bass model (e.g., [17,18,22–24]). Empirical veri<sup>fi</sup>cations in these studies show that multi-generation diffusion models are applicable not only to technological products such as IBM mainframe computers and mobile phones, but also to non-technological products such as milk containers.

With successive software versioning in context, our goal in this research is to develop an optimal free offer policy for a new software product based on various economic factors and market conditions. Speci<sup>fi</sup>cally, we attempt to answer the following questions: if wordof-mouth is the only signi<sup>fi</sup>cant bene<sup>fi</sup>t factor, should free offer be given for the <sup>fi</sup>rst version only or for subsequent versions as well? If free offer is bene<sup>fi</sup>cial for a given version, how many free copies should be distributed? Does the release time of the subsequent versions have an impact on the free offer policy and its pro<sup>fi</sup>tability? Does the composition of free adopters have an impact on the optimal free offer policy?

The rest of the paper is organized as follows. In Section 2, we introduce diffusion models that have a bearing on our research. In Section 3, the bene<sup>fi</sup>t of free offer for a single software version is discussed. The free offer policy for two successive versions is analyzed in Sections 4 and 5, with Section 4 focusing on cases where every free adopter has a reservation price equal to or above the sale price, and Section 5 focusing on cases where at least a portion of the free adopters' reservation price is lower than the sale price. In Sections 4 and 5, the price of the software is assumed to be constant across versions. This assumption is relaxed in Section 6, where we analyze the free offer policy with different prices for successive versions. Lastly, we discuss in Section 7 the managerial implications and future research directions.

## 2. Diffusion models

In this section, we <sup>fi</sup>rst review the basic Bass model [1] and the multi-generation diffusion model by Norton and Bass [20], and then propose an extended multi-generation diffusion that is suitable for modeling the diffusion dynamics of multiple successive software versions.

## 2.1. Bass model

The Bass model is appropriate for a single production generation. The model can be represented by the following equation:

$$
\frac {d Y (t)}{d t} = \left[ p + \frac {q}{m} Y (t) \right] [ m - Y (t) ],\tag{1}
$$

where Y(t) represents the cumulative number of adopters by time t, and the three constant parameters m, p, and q denote the potential market size, the coefficient of innovation, and the coefficient of imitation, respectively. Eq. (1) shows that the diffusion rate at a given time t equals the product of (i) the instantaneous probability of adoption at time t, which increases linearly with the number of existing adopters, and (ii) the number of potential adopters who have not adopted by time t. The cumulative number of adoptions and the non-cumulative diffusion rate at time t, denoted by S(t), can be derived based on Eq. (1):

$$
\begin{array}{l} Y (t) = \frac {m \Big (1 - e ^ {- (p + q) t} \Big)}{(q / p) e ^ {- (p + q) t} + 1}, \text { and } \\ S (t) = \frac {m (p + q) ^ {2}}{p} \frac {e ^ {- (p + q) t}}{\big [ (q / p) e ^ {- (p + q) t} + 1 \big ] ^ {2}}. \end{array}
$$

Fig. 1 shows the typical shape of a Bass diffusion curve (with qNp). The adoption rate is low when the product is <sup>fi</sup>rst released. Due to both the word-of-mouth effect and the external in<sup>fl</sup>uences such as advertisement, the adoption rate gradually picks up until a peak is reached. After the peak time t<sup>⁎</sup>, the adoption rate decreases due to market saturation effect.

## 2.2. Norton and Bass model

The multi-generation diffusion model proposed by Norton and Bass [20] captures the diffusion dynamics across multiple product generations. The model can be illustrated using two successive product generations. As shown in Fig. 2, the <sup>fi</sup>rst generation is released at time 0 and the second one is introduced at time θ. According to the Norton and Bass model, the diffusion processes of the two generations can be captured by the following equations:

![](/api/attachments/M4GG8BP4/fulltext/images/6116f8316d722bd71a88170cf8d51566a6add0a26b0b252d11e4f1153c1e426b.jpg)  
Fig. 1. A typical Bass diffusion curve $( q > p ) .$

$$
\begin{array}{r l} & Z _ {1} (t) = m _ {1} F _ {1} (t) - m _ {1} F _ {1} (t) F _ {2} (t - \theta) = m _ {1} F _ {1} (t) [ 1 - F _ {2} (t - \theta) ], \\ & Z _ {2} (t) = m _ {2} F _ {2} (t - \theta) + m _ {1} F _ {1} (t) F _ {2} (t - \theta) = F _ {2} (t - \theta) [ m _ {2} + m _ {1} F _ {1} (t) ]. \end{array}
$$

In these two equations, $Z _ { i } ( t )$ denotes the number of adopters who are using generation $i , i \in \{ 1 , 2 \}$ , at time $t , m _ { 1 }$ is the number of potential adopters for generation 1, and $m _ { 2 }$ is the number of potential adopters unique to generation 2. According to Norton and Bass [20], all potential adopters of generation 1 are also possible adopters of generation $2 . F _ { i } ( t )$ represents the cumulative proportion of adoptions by time t for generation i, provided that the adoptions of each generation are completely independent of the adoptions of other generations. $F _ { i } ( t )$ takes the following functional form:

$$
F _ {i} (t) = \frac {1 - e ^ {- (p _ {i} + q _ {i}) t}}{(q _ {i} / p _ {i}) e ^ {- (p _ {i} + q _ {i}) t} + 1},
$$

where $p _ { i }$ and $q _ { i }$ are the coef<sup>fi</sup>cient of innovation and coef<sup>fi</sup>cient of imitation, respectively, for generation i. Analogous to prior research $( \mathrm { e . g . }$ ., [22]), $F _ { i } ( t )$ can also be interpreted as representing the progress of the diffusion of information about generation i. Since the diffusion of generation 2 starts from time , $F _ { 2 } ( t - \theta ) = 0$ for tbθ. The derivative of $F _ { i } ( t )$ , representing the non-cumulative adoption rate for generation i, is

$$
f _ {i} (t) = \frac {(p _ {i} + q _ {i}) ^ {2}}{p _ {i}} \frac {e ^ {- (p _ {i} + q _ {i}) t}}{\left[ (q _ {i} / p _ {i}) e ^ {- (p _ {i} + q _ {i}) t} + 1 \right] ^ {2}}.
$$

Based on the Norton and Bass model, the diffusion process for generation 1 before time θ is the same as the process for a single generation. After time θ, the group of customers that are unique to generation 2 also adopt the new generation as if it is the only one available; at the same time, the new generation 2 starts attracting existing and potential adopters away from generation 1, re<sup>fl</sup>ected by the term m ${ } _ { 1 } F _ { 1 } ( t ) F _ { 2 } ( t - \theta )$ in $Z _ { 1 } ( t )$ and $Z _ { 2 } ( t )$

## 2.3. An extended multi-generation diffusion model

After a new product generation becomes available, some <sup>fi</sup>rst-time adopters who otherwise would adopt the old generation may decide to purchase the new generation instead, we call this type of adopter behavior first-purchase substitution (or substitution for short). Besides the <sup>fi</sup>rst-time adopters, some existing adopters of the old generation may be willing to upgrade to the new generation, if they believe that the improvements in the new generation are worth the investment. We call this behavior generation switching (or switching for short). To a software <sup>fi</sup>rm, the primary difference between switching and substitution is that the former leads to repeat purchases from the same potential adopter, while latter does not. In their study, Norton and Bass acknowledge the existence of substitution and switching, but do not differentiate the two ([20], p. 1074). In this study, <sup>fi</sup>rst-purchase substitution and generation switching need to be differentiated, because their economic implications are different.

Out of the relevant extensions of the Norton and Bass model, only the model proposed by Mahajan and Muller [18] explicitly models produc upgrades (i.e., generation switching in this study). However, the Mahajan and Muller model is not appropriate for this research for the following reasons, First, their model considers the number of systems in use instead of the total number of adoptions or purchases, thus making it difficult to determine the amount of sales in a given time period. Second, a closed-form solution is not available for the speed of adoption, making the revenue calculation infeasible. Third, their assumption that the proportion of potential adopters who shift from an old generation to a new generation remains constant over time is not applicable to software products. The Mahajan and Muller model, however, provides a basis fo extending the Norton and Bass model to address potential adopters' generation switching behavior. In their model, Mahajan and Muller assume that product upgrades also follow a Bass-type diffusion process, with the potential market size for upgrade at any given time t equal to the number of existing adopters for each previous generation right before t. In this research, we restrict the potential adopters for switching to those who have adopted before the new generation is released. This restriction is appropriate because software products, unlike physical products, do not wear out by usage. If an adopter decides to purchase the older version even after the new version is released, the adopter is highly unlikely to purchase an upgrade to the new version again. Regarding the speed of diffusion for a new software version, we assume that the coef<sup>fi</sup>cient of innovation $( p )$ is the same for new purchases and upgrades, so is the coef<sup>fi</sup>cient of imitation (q). Based on the existing models and the aforementioned factors, we next develop an extended model suitable for this research.

![](/api/attachments/M4GG8BP4/fulltext/images/aa8bd5a9cd6d7e3c4f49dc4c8c7f2a2677740d9f08c447012fe515b2a129cc62.jpg)  
Fig. 2. Diffusion curves for two successive product generations.

After generation 2 is introduced to the market at time θ, a portion $\left( \alpha _ { 2 } \right)$ of those who otherwise would have adopted generation 1 would gsubstitute it with generation 2 instead. Hence, the cumulative number of substitutions from generation 1 to generation 2 by time t, denoted by $B _ { 2 } ( t )$ , equals

$$
B _ {2} (t) = \left\{ \begin{array}{l l} 0, & t <   \theta , \\ \alpha_ {2} m _ {1} [ F _ {1} (t) - F _ {1} (\theta) ], & t \geq \theta . \end{array} \right.\tag{2}
$$

We refer to $\alpha _ { 2 }$ as the substitution ratio, representing the proportion of potential adopters of generation 1 who, after being informed of generation 2, will substitute generation 1 with generation 2. Along with the <sup>fi</sup>rst-time purchasers, those who have adopted generation 1 before time θ may switch to generation 2 after it is available. The speed of switching depends on the progress of the diffusion of information about the newer generation. The cumulative number of switching adoptions by time t, denoted by $W _ { 2 } ( t )$ , is

$$
W _ {2} (t) = \left\{ \begin{array}{l l} 0, & t \leq \theta , \\ m _ {1} F _ {1} (\theta) F _ {2} (t - \theta), & t > \theta , \end{array} \right.\tag{3}
$$

Due to the <sup>fi</sup>rst-purchase substitutions, the cumulative number of adoptions of generation 1 by time t, denoted by $Y _ { 1 } ( t )$ , is

$$
Y _ {1} (t) = \left\{ \begin{array}{l l} m _ {1} F _ {1} (t), & t \leq \theta , \\ m _ {1} F _ {1} (t) - B _ {2} (t) = m _ {1} F _ {1} (t) - \alpha_ {2} m _ {1} [ F _ {1} (t) - F _ {1} (\theta) ], & t > \theta . \end{array} \right.\tag{4}
$$

Note that a switching from generation 1 to generation 2 does not lead to a reduction in $Y _ { 1 } ( t ) ;$ ; hence $Y _ { 1 } ( t )$ is an increasing function of time. The cumulative number of adoptions of generation 2, denoted by $Y _ { 2 } ( t ) ,$ , equals

$$
Y _ {2} (t) = \left\{ \begin{array}{l l} 0, & t \leq \theta , \\ m _ {2} F _ {2} (t - \theta) + B _ {2} (t) + W _ {2} (t) = m _ {2} F _ {2} (t - \theta) + m _ {1} \alpha_ {2} [ F _ {1} (t) - F _ {1} (\theta) ] + m _ {1} F _ {1} (\theta) F _ {2} (t - \theta), & t > \theta . \end{array} \right.\tag{5}
$$

We call this modi<sup>fi</sup>ed model the Extended Multi-Generation diffusion model (EMG). In the rest of the analyses, we use Eqs. $( 2 ) - ( 5 )$ to model the diffusion dynamics across two successive software versions and derive the optimal free offer solution.

## 3. Free offer for a single version

In order to understand the cost and bene<sup>fi</sup>t of free software offer, we <sup>fi</sup>rst examine a simple case — there exists only one software version during the product lifecycle. In addition, we assume that all free adopters have a reservation price equal to or higher than the sale price of the software, i.e., they would adopt the software even if they were charged the regular price. For this simple case, free offer speeds up the diffusion of the new product because of the word-of-mouth effect from the free adopters, at the cost of losing potential revenue from every free adopter. The impact of free offer on the diffusion of a new product is illustrated in Fig. 3a and b. The curve in Fig. 3a represents the diffusion rate without free offer and the one in Fig. 3b represents the diffusion rate right after free offer. Clearly, because of the word-of-mouth effect from the free adopters, the diffusion curve in Fig. 3b starts from a higher level than the one shown in Fig. 3a.

Further, we <sup>fi</sup>nd based on Eq. (1) that with n free adoptions, the curve shown in Fig. 3b perfectly matches the portion of the curve shown in Fig. 3a starting from the time point (τ) when the number of adopters reaches n [16]. Such a time τ can be determined by

$$
\tau = Y ^ {- 1} (n) = \frac {\ln [ (m p + n q) / (m p - n p) ]}{p + q}.
$$

Software products, unlike physical products, do not face supply constraints, and can be quickly and cost-ef<sup>fi</sup>ciently distributed to a large number of potential adopters through various channels. Further, some free software offer can start before the commercial launch of a software version. This is because free copies can be distributed as soon as a new version is <sup>fi</sup>nalized, while the formal commercial release cannot start until all internal and external red-tapes are cleared and various agreements (e.g., with vendors and retailers) are negotiated and <sup>fi</sup>nalized. In certain situations, a close-to-<sup>fi</sup>nish beta version can be made available even before the product is <sup>fi</sup>nalized. For these reasons, we in this research assume that free offer causes no or negligible delay to the commercial launch of any software version. With this assumption, the impact of free offer is equivalent to left-shifting the original diffusion curve, with the amount of shifting (τ) a function of the number of free adopters (n). Without loss of generality, we set the sale price after free offer to 1. Assuming a discount rate r and a demand window $D ,$ the optimal number of free adoptions $( \boldsymbol n ^ { * } )$ can be determined by

![](/api/attachments/M4GG8BP4/fulltext/images/aaf74faf41a99b35f30dc57b572e9a6a1e2bb82737f1406af5462a26171d2ba2.jpg)

![](/api/attachments/M4GG8BP4/fulltext/images/c697c0fb72c135f18c63e9f48988573f2a541a8f6ac3195a78fd9fe21247447a.jpg)  
Fig. 3. a. Diffusion curve without free offer. b. Diffusion curve after free offer.

$$
\begin{array}{l} \underset {n} {\text { Max }} V (n) = \int_ {\tau} ^ {\tau + D} S (t) e ^ {- r (t - \tau)} d t, \\ \text { s.t. } \tau = \frac {\ln [ (m p + n q) / (m p - n p) ]}{p + q}. \end{array}\tag{6}
$$

Since τ and n uniquely determine each other, the optimization problem Eq. (6) can also be formulated as

$$
\underset {\tau} {\text { Max }} \quad V (\tau) = \int_ {\tau} ^ {\tau + D} \frac {m (p + q) ^ {2}}{p} \frac {e ^ {- (p + q) t}}{\left[ (q / p) e ^ {- (p + q) t} + 1 \right] ^ {2}} e ^ {- r (t - \tau)} d t.\tag{6'}
$$

Once the optimal $\tau ^ { * }$ is determined, the optimal $n ^ { * } = Y ( \tau ^ { * } )$ can be calculated. This is true for a product with just one version in its lifecycle, as well as for any given version of a multi-version product. Therefore, in the rest of the discussion, we use either the optimal amount of left-shifting or the optimal number of free adoptions to represent the optimal free offer solution.

Based on the same formulation Eq. (6), Jiang and Sarkar [16] show that it is the discount factor, the <sup>fi</sup>nite demand window, or more likely, the combination of the two that makes free offer bene<sup>fi</sup>cial to a software <sup>fi</sup>rm. In addition, Jiang and Sarkar conclude that if free offer is bene<sup>fi</sup>cial, it is always optimal to give away the free copies right after the software is ready for release.

## 4. Free offer for two successive versions

In this section, we develop a free offer policy for software products with two successive versions. We consider two cases, one without version switching and the other with version switching. The former assumes that each potential adopter will purchase at most one software version, while the latter assumes that some adopters may purchase both versions. For both cases, we assume that all free adopters have a reservation price equal to or higher than the sale price of the adopted version. Hence, every free adoption represents a loss of potential revenue for the software <sup>fi</sup>rm.

## 4.1. Free offer without switching

In the absence of version switching, $W _ { 2 } ( t ) = 0$ . Under this special case,

$$
Y _ {1} (t) = m _ {1} F _ {1} (t) - B _ {2} (t), \forall t > \theta , \text { and }\tag{\( (4') \}
$$

$$
Y _ {2} (t) = m _ {2} F _ {2} (t - \theta) + B _ {2} (t), \forall t > \theta .\tag{\( (5') \}
$$

As shown in Fig. 2, we <sup>fi</sup>rst assume that version 1 of a software product is released at time 0 and version 2 is released at a predetermined time θ. If the software <sup>fi</sup>rm charges a <sup>fi</sup>xed price $P r _ { 1 }$ for version 1 and a <sup>fi</sup>xed price $P r _ { 2 }$ for version 2, the total discounted revenue for the two versions equals

$$
V = P r _ {1} \int_ {0} ^ {D} \frac {d Y _ {1} (t)}{d t} e ^ {- r t} d t + P r _ {2} \int_ {\theta} ^ {D} \frac {d Y _ {2} (t)}{d t} e ^ {- r t} d t,\tag{7}
$$

where $Y _ { 1 }$ and Y are de<sup>fi</sup>ned in Eqs. (4′) and (5′), respectively. Substituting Eqs. (4′) and (5′) into Eq. (7), we have

$$
\begin{array}{l} V = m _ {1} P r _ {1} \int_ {0} ^ {D} f _ {1} (t) e ^ {- r t} d t + m _ {2} P r _ {2} \int_ {0} ^ {D} f _ {2} (t - \theta) e ^ {- r t} d t \\ \qquad + (P r _ {2} - P r _ {1}) \int_ {\theta} ^ {D} \frac {d B _ {2} (t)}{d t} e ^ {- r t} d t. \end{array}\tag{8}
$$

In the software market, the regular sale price for most software products remains relatively stable across successive versions. Hence, for mathematical tractability, we assume that the <sup>fi</sup>rm charges the same price for versions 1 and 2. Without loss of generality, we let ${ P r } _ { 1 } = { P r } _ { 2 } = 1$ . Eq. (8) then reduces to

$$
V = m _ {1} \int_ {0} ^ {D} f _ {1} (t) e ^ {- r t} d t + m _ {2} \int_ {\theta} ^ {D} f _ {2} (t - \theta) e ^ {- r t} d t\tag{9}
$$

From Eq. (9), we conclude that when the prices for the two successive versions are the same, we can treat the diffusion processes as two completely independent ones, i.e., one for version 1 with a potential market size of m and the other for version 2 with a potential market size of $m _ { 2 } ,$ and assume that substitutions never occur. This simpli<sup>fi</sup>cation is possible because after time θ, whether a customer adopts version 1 or version 2 does not affect the <sup>fi</sup>rm's revenue.

We next examine the free offer policy for two successive software versions without switching. We consider only the scenario where n<sub>1</sub> out of $m _ { 1 }$ potential adopters receive and adopt version 1 for free, and n out of m potential adopters adopt version 2 for free (we have also analyzed other scenarios and found that the qualitative results and hence the managerial implications are similar). The resulting leftshifting for version 1 and version 2 are τ and φ, respectively. Since the diffusion processes of the two versions can be decomposed into two independent ones, the optimal free offer policy for version 1 and version 2 can be separately computed using a model similar to Eqs. (6) or (6′).

We would like to point out that with the discount factor considered, none of the existing diffusion-based studies in the literature is able to produce a closed-form solution. In this research. except for some special scenarios, numerical methods are also needed to compute the best solution. In order to determine the optimal number of free adopters, we need to know the projected diffusion path for each version. In the product diffusion literature, methods have been proposed to estimate the Bass model parameters based on diffusion history of analogous products [2,3]. For illustration purpose, we use a set of spreadsheet sales data from the UK [11] to estimate the Bass model parameters and treat them as the parameters for the <sup>fi</sup>rst version: $p _ { 1 } = 0 . 0 0 2 , q _ { 1 } = 0 . 6 4 8$ and $m _ { 1 } = 1 0 2 5 \mathrm { K } .$ For subsequent versions, Norton and Bass [20] assume that the coef<sup>fi</sup>cient of innovation and the coef<sup>fi</sup>cient of imitation are the same as those for the <sup>fi</sup>rst version. Some more recent studies, however, <sup>fi</sup>nd that allowing the parameter values to differ across generations lead to better model <sup>fi</sup>t and prediction performance [15,25]. In this research, we assume that the coef<sup>fi</sup>cient of innovation and the coef<sup>fi</sup>cient of imitation are different across software versions. For version 2, we let $p _ { 2 } = p _ { 1 } + \Delta p$ and $q _ { 2 } = q _ { 1 } + \Delta q ,$ where $\Delta p$ and $\Delta q$ equal the increases estimated by Wang and Chang [25] for the diffusion of mobile phones, which lead to $p _ { 2 } { = } 2 . 0 0 5 { \times } 1 0 ^ { - 3 }$ and $q _ { 2 } = 0 . 8 3 0 4$ . The number of potential adopters that are unique to version 2, m , is assumed to be half of m . Regarding the remaining parameters, we set the discount rate (r) to 0.1, the demand window (D) to 10, and the release time for the second version (θ) to 2. Using these parameter values, we numerically obtain the optimal free offer solution: $n _ { 1 } ^ { * } { = } 1 1 2 \mathrm { K }$ and $n _ { 2 } ^ { * } = 4 7 \mathrm { K } ,$ equivalent to a left-shifting of $\tau ^ { * } { = } 5 . 7 1$ and $\varphi ^ { * } { = } 4 . 5 2$ respectively, and the resulting net revenue is $V ^ { * } { = } 9 7 9 \mathrm { K } .$ This solution is illustrated in Fig. 4.

In the above example, the release time of the second version (θ) is assumed to be exogenous. We next relax this assumption and examine the impact of θ on the optimal free offer solution. Although a closed-form solution cannot be obtained, we have the following observation:

Observation 1. When the price of two successive software versions is the same and version switching does not occur, the optimal number of free adopters for version 1 $( n _ { 1 } ^ { * } )$ is independent of the release time for version ${ 2 \left( \theta \right) } ;$ on the other hand, the optimal number of free adopters for version $2 ~ ( n _ { 2 } ^ { * } )$ changes with θ, and the total time-discounted revenue $( \boldsymbol { V } ^ { * } )$ for both versions increases as θ moves earlier.

This observation can be illustrated using Fig. 4. As we show earlier, the diffusion of the two versions can be treated as two independent processes with a potential population of m and m , respectively. If version 2 is released earlier, the optimal left-shifting $( \tau _ { 1 } ^ { * } )$ stays the same for version 1, since decreasing the value of θ does not affect the diffusion of the <sup>fi</sup>rst version in any manner. On the other hand, the duration of the true demand window for version 2, i.e., $( D - \theta )$ increases as the value of θ decreases. The net revenue will increase as a result for two reasons. First, the purchases of version 2 will occur earlier. Second, a portion of the potential adopters who otherwise will miss the demand window will be able to adopt because of the essentially extended demand window. Based on Observation 1, we conclude that if a <sup>fi</sup>rm is able to control its release time, version 2 should be released as early as possible.

## 4.2. Free offer with switching

When switching is common across the two successive versions, $Y _ { 2 } ( t )$ increases by $W _ { 2 } ( t )$ . Hence,

$$
\begin{array}{l} V = m _ {1} P r _ {1} \int_ {0} ^ {D} f _ {1} (t) e ^ {- r t} d t + m _ {2} P r _ {2} \int_ {\theta} ^ {D} f _ {2} (t - \theta) e ^ {- r t} d t \\ \qquad + (P r _ {2} - P r _ {1}) \int_ {\theta} ^ {D} \frac {d B _ {2} (t)}{d t} e ^ {- r t} d t + P r _ {2} \int_ {\theta} ^ {D} \frac {d W _ {2} (t)}{d t} e ^ {- r t} d t. \end{array}
$$

Once again, we let ${ P r } _ { 1 } = { P r } _ { 2 } = 1$ , the above equation is simpli<sup>fi</sup>ed to

$$
V = m _ {1} \int_ {0} ^ {D} f _ {1} (t) e ^ {- r t} d t + [ m _ {2} + m _ {1} F _ {1} (\theta) ] \int_ {\theta} ^ {D} f _ {2} (t - \theta) e ^ {- r t} d t.\tag{10}
$$

Compared to Eq. (9), the term $m _ { 2 }$ is replaced by $[ m _ { 2 } + m _ { 1 } F _ { 1 } ( \theta ) ]$ in $\operatorname { E q . } \left( 1 0 \right)$ . Clearly, other factors held constant, the discounted revenue is higher with switching than without switching. This is because with switching, some customers will purchase more than once during the demand window. Further, unlike those in Eq. (9), the diffusion processes for the two successive versions captured in Eq. (10) can no longer be considered two separate ones. We infer from the expression that as the release of the second version delays, the number of possible switching adoptions, and hence the number of repeat purchases, increases. On the other hand, the further is the delay to the release of version 2, the smaller is the present value of the revenue generated by a purchase of version 2. Therefore, when θ is endogenous, a <sup>fi</sup>rm needs to balance this tradeoff when deciding the release time for the second version.

![](/api/attachments/M4GG8BP4/fulltext/images/385d7b2946fad8c8eb154822f323c3a280d32c7f508f1460a5be1500df267972.jpg)  
Fig. 4. Optimal left-shifting without switching.

With potential adopters' switching behavior considered, we next examine the optimal free offer policy for a software product with two successive versions. Because some adopters may purchase both versions at different times, the implications of free offers become more complex in comparison with the case without switching. Depending on whether the release time for version 2 is exogenous or endogenous, the bene<sup>fi</sup>t of free offer is different. In what follows, we examine these two cases separately.

## 4.2.1. Exogenous release time for version 2

We assume that all adopters of version 1 before θ have an equal probability of switching to version 2, regardless of whether they received version 1 for free. Further, each of the potential adopters of version 2, who is either unique to version 2 or ready to switch to version 2, has the same chance of receiving a free copy of version 2 and exerts the same amount of word-of-mouth in<sup>fl</sup>uence on future adopters. Compared with the case without version switching, free offer in this case not only speeds up the diffusion of version 1, but also increases the number of potential adopters for version 2. With $n _ { 1 }$ free adopters for version 1 (resulting in a left-shifting of τ), the number of potential adopters for version 2 becomes $m _ { 2 } ^ { \prime } { = } m _ { 2 } + m _ { 1 } F _ { 1 } ( \theta + \tau )$ . The total discounted revenue thus equals

$$
\begin{array}{c} V (n _ {1}) = m _ {1} \int_ {\tau} ^ {D + \tau} f _ {1} (t) e ^ {- r (t - \tau)} d t + m _ {2} ^ {\prime} \int_ {\theta} ^ {D} f _ {2} (t - \theta) e ^ {- r t} d t. \\ \text { where } m _ {2} ^ {\prime} = m _ {2} + m _ {1} F _ {1} (\theta + \tau), \text { and } \\ \tau = \frac {\ln [ (p _ {1} m _ {1} + q _ {1} n _ {1}) / (p _ {1} m _ {1} - p _ {1} n _ {1}) ]}{p _ {1} + q _ {1}}. \end{array}\tag{11}
$$

Suppose that free offer for version 2 is also provided at a predetermined time θ, and $n _ { 2 }$ potential adopters adopt it for free. The optimal free offer problem can be formulated as

$$
\begin{array}{l} \underset {n _ {1}, n _ {2}} {\text { Max }} V (n _ {1}, n _ {2}) = m _ {1} \int_ {\tau} ^ {D + \tau} f _ {1} (t) e ^ {- r (t - \tau)} d t + m _ {2} ^ {\prime} \int_ {\theta + \varphi} ^ {D + \varphi} f _ {2} (t - \theta) e ^ {- r (t - \varphi)} d t, \\ \text { s.t. } m _ {2} ^ {\prime} = m _ {2} + m _ {1} F _ {1} (\theta + \tau), \\ \tau = \frac {\ln [ (p _ {1} m _ {1} + q _ {1} n _ {1}) / (p _ {1} m _ {1} - p _ {1} n _ {1}) ]}{p _ {1} + q _ {1}}, \\ \varphi = \frac {\ln [ (p _ {2} m _ {2} ^ {\prime} + q _ {2} n _ {2}) / (p _ {2} m _ {2} ^ {\prime} - p _ {2} n _ {2}) ]}{p _ {2} + q _ {2}}. \end{array}\tag{12}
$$

From Eq. (12), we can see that the amount of left-shifting for version $2 ~ ( \varphi )$ is a function of the number of potential adopters for version $2 \left( m _ { 2 } ^ { \prime } \right)$ , which, in turn, depends on the left-shifting for version 1 (τ). Therefore, unlike the non-switching case, where the two versions can be treated as two independent ones, the two diffusion processes shown in Eq. (12) cannot be completely separated. Despite the complexity, we are able to derive an important property of the problem. If we search for the optimal number of free adopters for version $2 ( n _ { 2 } ^ { * } )$ which also uniquely determines the optimal amount of left-shifting $( \varphi ^ { * } )$ , for each given value of $n _ { 1 } ,$ , the following conclusion holds:

Proposition 1. With version switching and a fixed release time for version $^ { 2 , }$ the optimal number of free adopters for version $2 ( n _ { 2 } ^ { * } )$ increases with the number of free adopters for version $\textit { 1 } ( n _ { 1 } ) ,$ , while the optimal amount of left-shifting for version ${ \dot { 2 } } \left( \varphi ^ { * } \right)$ is independent of $\lceil n _ { 1 } .$

(All proofs are provided in the Appendix.)

The fact that $\varphi ^ { * }$ is independent of n allows us to numerically obtain the optimal free offer solution in two steps. In step one, we search for the $\varphi ^ { * }$ that maximizes $\mu ( \varphi ) \equiv \int _ { \theta + \infty } ^ { D + \varphi } f _ { 2 } ( t - \theta ) e ^ { - r ( t - \varphi ) } \mathrm { d } t ,$ which is independent of the value of . In step two, we search for the optimal $\tau ^ { * }$ that maximizes $V ( \tau , \varphi ^ { * } )$ . In each step, we only need to search a one-dimensional space; therefore, Proposition 1 helps improve computational ef<sup>fi</sup>ciency. Once $\tau ^ { * }$ and $\varphi ^ { * }$ are obtained, $n _ { 1 } ^ { * }$ and $n _ { 2 } ^ { * }$ can be easily computed.

For ease of comparison, we adopt the same parameter values used in Section 4.1. The optimal solution obtained is $\tau ^ { * } = 7 . 9 7 , \varphi ^ { * } = 4 . 5 2$ (or $n _ { 1 } ^ { * } { = } 3 6 1 \mathrm { K } , n _ { 2 } ^ { * } { = } 1 1 0 \mathrm { K } ) $ , and $V ^ { * } { = } 1 3 2 8 \mathrm { K } .$ By comparing this solution with the one without switching, we <sup>fi</sup>nd that, as expected, switching increases a <sup>fi</sup>rm's net revenue. With switching, the portion of free adoptions for version 1, determined by $\tau ^ { * }$ , increases. This is because free offer is more bene<sup>fi</sup>cial in the presence of version switching — giving away one copy of version 1 not only speeds up the diffusion of version 1, but also increases the number of switching adoptions to version 2. Consistent with Proposition 1, we note that the percentage of free adopters for version 2 remains unchanged. This con<sup>fi</sup>rms that $\varphi ^ { * }$ can be obtained independently of other parameters including τ.

## 4.2.2. Endogenous release time for version 2

When the release time of version 2 is endogenous, Eq. (12) is further expanded to

$$
\begin{array}{l} \underset {n _ {1}, n _ {2}, \theta} {\text {Max}} V (n _ {1}, n _ {2}, \theta) = m _ {1} \int_ {\tau} ^ {D + \tau} f _ {1} (t) e ^ {- r (t - \tau)} d t + m _ {2} ^ {\prime} \int_ {\theta + \varphi} ^ {D + \varphi} f _ {2} (t - \theta) e ^ {- r (t - \varphi)} d t, \\ \text {s.t.} m _ {2} ^ {\prime} = m _ {2} + m _ {1} F _ {1} (\theta + \tau), \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qend{array}\tag{13}
$$

With three decision variables to be determined, coupled with the fact that a closed-form expression for the discounted revenue is not obtainable, Eq. (13) seems to be a challenging problem to solve. With a closer examination of the expression, however, we <sup>fi</sup>nd that the search for the optimal solution is not as complex as it may <sup>fi</sup>rst appear. In order to <sup>fi</sup>nd the optimal solution $( \tau ^ { * } , \varphi ^ { * } , \dot { \theta } ^ { * } )$ , we vary the value of θ from 0 to D with appropriate increments $( \mathrm { e . g . , } 1 / 1 0 , \mathrm { o r } 1 / 1 2$ of a year). For each given value of θ, we use the numerical method for Eq. (12) to obtain the best (τ, φ) and the corresponding maximum revenue V. Once the results for all considered θ values are obtained, we select the value of θ that leads to the highest revenue as the optimal $\boldsymbol { \theta } ^ { * }$ . This $\boldsymbol { \theta } ^ { * }$ and the corresponding $\tau ^ { * } , \varphi ^ { * }$ , and $V ^ { * }$ , jointly constitute the optimal solution for the free offer problem formulated in Eq. (13).

Based on the same parameter values used in previous subsections, we repeat the numerical analysis and record how the amount of leftshifting for both versions and the net revenue change with θ. The results are shown in Fig. 5. This <sup>fi</sup>gure shows a concave relationship between V and θ. The maximum revenue $V ^ { * } { = } 1 4 8 0 \mathrm { K }$ is achieved at $\theta ^ { * } { = } 4 . 8 , \tau ^ { * } { = } 6 . 8 9$ , and $\varphi ^ { * } { = } 5 . 0 2$ (or n<sup>⁎</sup>=217 K and $n _ { 2 } ^ { * } = 1 8 6 \mathrm { K } )$ . For this example, we conclude that even if the second version is ready to be released at the end of year 2, the <sup>fi</sup>rm should wait until the start of the <sup>fi</sup>fth year to launch the new version.

![](/api/attachments/M4GG8BP4/fulltext/images/1088612c029b311d0cbf52c291025472306cc78446b2b53e853aa27a254ebbe1.jpg)  
Fig. 5. Impact of the release time for version 2 (θ).

Note that the obtained optimal release time $\left( \varphi ^ { * } \right)$ is valid only if the second version is ready for release on or before $\boldsymbol { \Phi } ^ { * }$ . If the new version is not ready for release at $\boldsymbol { \Phi } ^ { * }$ , it should be released as soon as it is ready.

## 5. Free offer involving low-valuation adopters

In a given population, not everyone who is interested in a software product can afford it. For expositional convenience, we name the potential adopters with a reservation price lower than the sale price of the software low-valuation potential adopters, and those with a reservation price equal to or higher than the sale price high-valuation potential adopters. So far, we have considered only the cases where all free adopters are from the group of high-valuation potential adopters. For these cases, every free adoption results in a loss of potential revenue, because the free adopters would be willing to purchase the software if free offer were not available.

In this section, we examine a more general free offer case. When free software copies are given away, they are adopted by both highvaluation and low-valuation potential adopters. The difference between the two types of free adopters is that the high-valuation ones always lead to a loss of potential revenue, while the lowvaluation ones do not. In this research, we assume that a highvaluation free adopter and a low-valuation free adopter always have the same amount of word-of-mouth in<sup>fl</sup>uence on future adopters.

## 5.1. Model formulation

In what follows, we <sup>fi</sup>rst examine the implications of lowvaluation free adopters on the bene<sup>fi</sup>t of free offer, and then develop a free offer policy that takes into consideration low-valuation free adopters. In the Bass model and its multi-generation extensions, the market size parameter refers to the number of high-valuation potential adopters, and the diffusion curve only re<sup>fl</sup>ects the highvaluation adopters' rate of adoption. When free offer is provided, because of the inclusion of the low-valuation free adopters, the speed of the entire diffusion process can further increase. We next examine the net impact of the low-valuation free adopters on the speed of diffusion. Suppose there are (1+λ)n free adopters; among them n are high-valuation ones and λn are low-valuation ones, with λ representing the ratio between low-valuation and high-valuation free adopters. Upon examination, we <sup>fi</sup>nd that if we ignore those low-valuation free adopters, the diffusion curve right after free offer perfectly matches the diffusion curve for the case where only high-valuation free adopters exist. Now, assuming that the “extra” λn low-valuation free adopters adopt before all high-valuation adopters, the original hazard rate Eq. (1) becomes

$$
\frac {d Y (t)}{d t} = \Big [ p + \frac {q}{m} (Y (t) + \lambda n) \Big ] [ m - Y (t) ],
$$

which can be rewritten as

$$
\frac {d Y (t)}{d t} = \left[ p ^ {\prime} + \frac {q}{m} Y (t) \right] [ m - Y (t) ], \text {   where   } p ^ {\prime} = p + (q / m) \lambda n.\tag{14}
$$

From Eq. (14), we conclude that incorporating the word-of-mouth effect from the low-valuation free adopters is equivalent to increasing the value of the coef<sup>fi</sup>cient of innovation $( p )$ by (q/m)λn. When there is only one software version, Jiang and Sarkar [16] show that with a higher $p ,$ the optimal number of high-valuation free adopters decreases, while the total number of free adopters increases, and the speed of diffusion and the net revenue both increase as a result. These conclusions can be extended to the various scenarios discussed in Section 4 for a software product with two successive versions. For instance, with version switching and an endogenous θ, the free offer problem can be formulated as

$$
\begin{array}{l} \underset {n _ {1}, n _ {2}, \theta} {\text {Max}} V (n _ {1}, n _ {2}, \theta) = m _ {1} \int_ {\tau} ^ {D + \tau} f _ {1} ^ {\prime} (t) e ^ {- r (t - \tau)} d t + m _ {2} ^ {\prime} \int_ {\theta + \phi} ^ {D + \phi} f _ {2} ^ {\prime} (t - \theta) e ^ {- r (t - \phi)} d t, \\ \text {s.t.} p _ {1} ^ {\prime} = p _ {1} + (q _ {1} / m _ {1}) \lambda n _ {1}, \\ F _ {1} ^ {\prime} (t) = \frac {1 - e ^ {- (p _ {1} ^ {\prime} + q _ {1}) t}}{(q _ {1} / p _ {1} ^ {\prime}) e ^ {- (p _ {1} ^ {\prime} + q _ {1}) t} + 1}, \\ m _ {2} ^ {\prime} = m _ {2} + m _ {1} F _ {1} ^ {\prime} (\theta + \tau), \\ p _ {2} ^ {\prime} = p _ {2} + (q _ {2} / m _ {2} ^ {\prime}) \lambda n _ {2}, \\ \tau = \frac {\ln [ (p _ {1} ^ {\prime} m _ {1} + q _ {1} n _ {1}) / (p _ {1} ^ {\prime} m _ {1} - p _ {1} ^ {\prime} n _ {1}) ]}{p _ {1} ^ {\prime} + q _ {1}}, \\ \varphi = \frac {\ln [ (p _ {2} ^ {\prime} m _ {2} ^ {\prime} + q _ {2} n _ {2}) / (p _ {2} ^ {\prime} m _ {2} ^ {\prime} - p _ {2} ^ {\prime} n _ {2}) ]}{p _ {2} ^ {\prime} + q _ {2}}, \\ f _ {i} ^ {\prime} (t) = \frac {(p _ {i} ^ {\prime} + q _ {i}) ^ {2}}{p _ {i} ^ {\prime}} \frac {e ^ {- (p _ {i} ^ {\prime} + q _ {i}) t}}{\left[ (q _ {i} / p _ {i} ^ {\prime}) e ^ {- (p _ {i} ^ {\prime} + q _ {i}) t} + 1 \right] ^ {2}}, i = 1, 2. \end{array}\tag{15}
$$

Despite the additional constrains in Eq. (15), the real difference between the two formulations in Eqs. (13) and (15) is that the coef<sup>fi</sup>cient of innovation for version 1 is revised higher in Eq. (15) to take into consideration the in<sup>fl</sup>uences of the low-valuation adopters. If we let λ=0, Eq. (15) reduces to Eq. (13). Therefore, Eq. (13) can be considered a special case of Eq. (15).

## 5.2. Impact of model parameters

We next examine how the model parameters impact the optimal solution to Eq. (15). Again, although a closed-form solution cannot be obtained, we are able to arrive at the following conclusion:

Proposition 2. In the presence of low-valuation free adopters, the net revenue $( V ^ { * } )$ increases monotonically with the ratio of low-valuation to high-valuation free adopters (λ), the demand window (D), the coefficients of innovation $( p _ { 1 } , p _ { 2 } )$ , and the coefficients of imitation (q , q ); while it decreases with the discount rate (r).

The conclusions in this proposition are quite intuitive. For instance, others factors being equal, a higher λ implies more low-valuation free adopters, from who a software <sup>fi</sup>rm can bene<sup>fi</sup>t from the same amount of word-of-mouth effect without losing any potential revenue. Therefore, the <sup>fi</sup>rm's net revenue can only increase with a higher λ.

Note that since Eq. (13) is a special case of Eq. (15), Proposition 2 holds for Eq. (13) as well.

We numerically obtain the optimal solution to Eq. (15) based on the same parameter values used in the previous section. The value of λ is set to 1, implying an equal number of low-valuation and highvaluation free adopters. The results show that the maximum revenue $( \boldsymbol { V } ^ { * } )$ is 1722 K, representing a 16% increase from the case without low-valuation free adopters (1480 K). This revenue is achieved with $n _ { 1 } ^ { * } = 1 7 2 \mathrm { K } , \ n _ { 2 } ^ { * } = 1 7 1 \ \bar { \mathrm { K } } ,$ and $\theta ^ { * } { = } 5 . 0 1$ . Compared with the case without low-valuation free adopters, the optimal number of highvaluation free adopters decreases for both versions, and it is optimal to wait a little longer before releasing the second version.

## 5.3. Sensitivity analysis

We next examine how the free offer solution and the revenue are affected by the different environment/economic factors.

To better understand the impact of the ratio of low-valuation to high-valuation free adopters, we vary the value of λ from 1/8 to 8, and record the corresponding optimal solutions. The results are shown in Fig. 6. Because of the difference in scales, we show the results in two separate charts. As we can see from the <sup>fi</sup>rst chart on the left, as the value of λ increases, the optimal number of high-valuation free adopters decreases for both versions, while the total number of free adopters, including both high-valuation and low-valuation ones, increases for both versions. From the chart on the right, we can see that it is optimal to delay releasing version 2 with a higher λ. As expected, the total revenue increases with λ. From Fig. 6, we infer that the increase in net revenue comes from three sources: (i) fewer highvaluation free adopters lead to a smaller revenue loss; (ii) a larger number of free adopters further increase the speed of diffusion, and (iii) the delayed release of version 2 lead to more version switches or repurchases. Based on this result, <sup>fi</sup>rms should try to target as many low-valuation free adopters as possible in the promotion process, provided that it is not too costly to identify them.

To examine the impact of the length of the demand window, we vary its value from 3 to 15 years while keeping the other parameter values <sup>fi</sup>xed; the corresponding optimal solutions are summarized in Fig. 7. The total number of free adopters is not shown in the <sup>fi</sup>rst chart, because with a <sup>fi</sup>xed λ, the ratio between the total number of free adopters and the number of high-valuation free adopters remains constant regardless of the length of the demand window. From this <sup>fi</sup>gure, we <sup>fi</sup>nd that as the duration of the demand window increases, the optimal release time for the second version is pushed further back, the optimal number of free adopters decreases for both version, and the total revenue increases along the way. While the increase in revenue is consistent with Proposition 2 and is intuitive, the change in the number of free adopters is not obvious. By further analyzing the optimal solution, we realize that with a <sup>fi</sup>xed demand window, in most cases it is optimal to left-shift the curve until the peak of the diffusion curve moves to approximately the middle of the demand window, so that the largest number of paid adopters can adopt within the <sup>fi</sup>xed demand window. This implies that with a larger demand window, the left-shifting should be smaller in most cases, hence a smaller number of free adopters are needed.

![](/api/attachments/M4GG8BP4/fulltext/images/1b928f2602b59d7242e38f598280bf9b3393af0408d8aaa9c78c4ce2b57d2e62.jpg)

![](/api/attachments/M4GG8BP4/fulltext/images/6412601fb7fd99329f4fe0587ac90e36bfdb3645ba31370a1a1f57c74933903e.jpg)  
Fig. 6. Impact of the ratio of low-valuation to high-valuation free adopters (λ).

![](/api/attachments/M4GG8BP4/fulltext/images/ea7915ec9b20e4eceed609d38ba6cad301f8d55101583288bffdd3e348bae966.jpg)

![](/api/attachments/M4GG8BP4/fulltext/images/6dc000fb8b2c29d246b5acc4f115aaca4ce9b8b7dc492e2aff72e841f336c9c0.jpg)  
Fig. 7. Impact of the demand window (D).

We also varied the discount rate r from 3% to 13%; the results are shown in Fig. 8. As expected, the optimal revenue decreases as the discount rate increases. The <sup>fi</sup>gure also shows that it is optimal to give away more free copies with a higher discount rate. This is expected since a higher speed of diffusion is more bene<sup>fi</sup>cial when the discount rate is higher. What is counter-intuitive is the shape of the curve representing the optimal release time for version $2 ~ ( { \boldsymbol { \theta } } ^ { * } )$ . Instead of releasing the second version earlier to reduce time-discounting, the results show that the release of the second version should be further delayed when the discount rate is higher. We speculate that this is because with more free adopters, the increase in the number of repurchases will more than offset the larger discount due to the delay in releasing the second version.

Finally, we vary the coef<sup>fi</sup>cient of innovation for the second version, which determines its starting diffusion rate, from 0.002 to 0.512 while keeping other parameters <sup>fi</sup>xed. The optimal solutions are summarized in Fig. 9. As expected, the net revenue increases monotonically with $p _ { 2 } ;$ this is because a higher $p _ { 2 }$ leads to a higher speed of diffusion, which leads to a higher time-discounted revenue. Further, it is optimal to delay releasing version 2 as $p _ { 2 }$ increases. This is due to the fact that with a higher starting diffusion rate, a <sup>fi</sup>rm can afford delaying the release to eventually generate more repurchases. The <sup>fi</sup>gure also shows that the optimal number of free offers for version 1 does not reduce much as the value of $p _ { 2 }$ increases. The optimal number of free adopters for version 2, on the other hand, decreases quickly, until zero is reached. We thus conclude that under certain conditions, it may not be bene<sup>fi</sup>cial to give away free software copies. If the diffusion of the newer version can take off quickly by itself, then free offer may not be needed.

## 6. Unequal pricing across successive versions

So far, we have focused on the scenarios where two successive software versions are charged the same price. In this section, we relax this assumption and examine the impact of unequal pricing on the free offer solution. For ease of comparison, we consider the scenario with switching but without low-valuation free adopters, and ignore the impact of pricing on the number of potential buyers.

## 6.1. Model formulation

We still denote the price of version 1 by $P r _ { 1 }$ and that of version 2 by $P r _ { 2 } .$ As shown in Eq. (8), when the prices for the two successive versions are different, the impact of substitutions on the <sup>fi</sup>rm's net revenue, re<sup>fl</sup>ected by the term $( P r _ { 2 } - P r _ { 1 } ) \int _ { \Theta } ^ { D } \frac { d B _ { 2 } ( t ) } { d t } e ^ { - r t } d t$ , has to be considered. Recall that $B _ { 2 } ( t )$ , the cumulative number of substitutions between time θ and time t, equals a fraction of the number of adopters who would have adopted version 1 if version 2 were not available. By substituting $B _ { 2 } ( t )$ , we expand the third term in Eq. (8) to

$$
(P r _ {2} - P r _ {1}) \int_ {\theta} ^ {D} \frac {d}{d t} \left\{\alpha_ {2} m _ {1} \left[ F _ {1} (t) - F _ {1} (\theta) \right] \right\} e ^ {- r t} d t.
$$

![](/api/attachments/M4GG8BP4/fulltext/images/505a29014d06d99c5a7a691f71c23a07c91608bf7766c2ec8adaaff70d36e174.jpg)

Now consider the impact of free offer on this term. If there are $n _ { 1 }$ free adopters of version 1, translating to a left-shifting of τ, the above term changes to

$$
\begin{array}{c} (P r _ {2} - P r _ {1}) \int_ {\theta + \tau} ^ {D + \tau} \frac {d}{d t} \{\alpha_ {2} m _ {1} [ F _ {1} (t) - F _ {1} (\theta + \tau) ] \} e ^ {- r (t - \tau)} d t \\ = (P r _ {2} - P r _ {1}) \alpha_ {2} m _ {1} \int_ {\theta + \tau} ^ {D + \tau} f _ {1} (t) e ^ {- r (t - \tau)} d t. \end{array}\tag{16}
$$

![](/api/attachments/M4GG8BP4/fulltext/images/b4f0870615c4c5c629fb7b14e0a25200e3f7fcd562d3e5cfbe916d801853033c.jpg)  
Fig. 8. Impact of the discount rate (r).

![](/api/attachments/M4GG8BP4/fulltext/images/20ffcce648e070110089a7fa0b826e92922563905a18247e7a58fe14fd9b3c72.jpg)

![](/api/attachments/M4GG8BP4/fulltext/images/18f4c9f41503162544ed165190794ab9fdf00b2e481e6fd33a314b43db8934c6.jpg)  
Fig. 9. Impact of the coef<sup>fi</sup>cient of innovation for version 2 (p<sub>2</sub>).

Incorporating the term Eq. (16) and the different prices into Eq. (12), we have the problem formulation for free offer under unequal pricing:

$$
\begin{array}{r l} \underset {n _ {1}, n _ {2}} {\text {Max}} & V (n _ {1}, n _ {2}) = P r _ {1} \cdot m _ {1} \int_ {\tau} ^ {D + \tau} f _ {1} (t) e ^ {- r (t - \tau)} d t \\ & \qquad + P r _ {2} \cdot m _ {2} ^ {\prime} \int_ {\theta + \phi} ^ {D + \phi} f _ {2} (t - \theta) e ^ {- r (t - \phi)} d t \\ & \qquad + (P r _ {2} - P r _ {1}) \alpha_ {2} m _ {1} \int_ {\theta + \tau} ^ {D + \tau} f _ {1} (t) e ^ {- r (t - \tau)} d t, \\ & \text {s.t.} m _ {2} ^ {\prime} = m _ {2} + m _ {1} F _ {1} (\theta + \tau), \\ & \qquad \tau = \frac {\ln [ (p _ {1} m _ {1} + q _ {1} n _ {1}) / (p _ {1} m _ {1} - p _ {1} n _ {1}) ]}{p _ {1} + q _ {1}}, \\ & \qquad \phi = \frac {\ln [ (p _ {2} m _ {2} ^ {\prime} + q _ {2} n _ {2}) / (p _ {2} m _ {2} ^ {\prime} - p _ {2} n _ {2}) ]}{p _ {2} + q _ {2}}. \end{array}\tag{17}
$$

It can be shown that Proposition 1 still holds for this revised free offer formulation with unequal pricing, which makes the numerical search for the optimal solution ef<sup>fi</sup>cient.

## 6.2. Numerical analysis

We conduct numerical analyses to examine how unequal pricing affects the optimal solution to Eq. (17). We adopt the same Bass model parameter values as in Section 4.2.1 and let $\alpha _ { 2 } = 0 . 5$ . The price for version 1 is <sup>fi</sup>xed at 1.0, and the price for version 1 is varied from 1.0 to 2.0 in steps of 0.1. The corresponding solutions are shown in Fig. 10. From this <sup>fi</sup>gure, we can see that as the price for version 2 increases, the optimal numbers of free adoptions for the two versions $( \mathrm { i } . \mathrm { e } . , n _ { 1 } ^ { * }$ and $n _ { 2 } ^ { * } )$ both decrease, with the optimal number for version 1 decreasing at a faster speed than that for version 2. The total discounted revenue increases monotonically with the price of version 2. The decreasing $n _ { 2 } ^ { * }$ is expected since with a higher price for version

![](/api/attachments/M4GG8BP4/fulltext/images/46da0258975182f7c319ca1abcb5ad02daa35fc60a8c7dbafd45bad358130cfd.jpg)  
Fig. 10. Impact of differential pricing across versions.

2, the cost of giving away free copies is higher. The decreasing $n _ { 1 } ^ { * }$ requires more careful examination and can be explained as follows. With a higher price for version 2, the cost of giving away version 1 to a potential adopter of version 1 also becomes higher. This is because a portion of the potential adopters of version 1 will purchase a higherpriced version 2 after time θ, thus leading to a higher expected revenue per potential adopter of version 1, when compared with a lower price for version 2.

We also analyze the impact of the substitution ratio $( \alpha _ { 2 } )$ , i.e., the proportion of the potential adopters of version 1 who substitute version 1 with version 2, on the solution to problem Eq. (17). We vary the substitution ratio from 0.1 to 1.0, while keeping the ratio between the prices of version 2 and version 1 <sup>fi</sup>xed at 1.2; the results are summarized in Fig. 11. We can see from this <sup>fi</sup>gure that with a higher substitution ratio, the optimal number of free adopters drops for both versions, and the total discounted revenue increases as a result. We thus conclude that if more potential adopters are willing to buy the more expensive newer version, the <sup>fi</sup>rm does not need to promote either version as aggressively as otherwise, and the pro<sup>fi</sup>t will still turn higher.

## 7. Concluding remarks

This study shows that the optimal free offer policy depends on various market conditions and economic factors. If repurchases are negligible, each new version should be released as early as possible, and the optimal number of free adopters can be separately determined for each version. When repurchases are signi<sup>fi</sup>cant, the release time of a new version can impact the total revenue and hence should be considered a decision variable. In the presence of low-valuation free adopters, a <sup>fi</sup>rm's pro<sup>fi</sup>t can further increase; therefore, low-valuation potential adopters should be targeted if possible.

![](/api/attachments/M4GG8BP4/fulltext/images/24f6a79a9753a92fb0e2f67d97b069d963d4adb6895f4a24d33b65323513e5ec.jpg)  
Fig. 11. Impact of the substitution ratio (p ) $( P r _ { 2 } / P r _ { 1 } = 1 . 2 ) .$

The free offer policy we study in this research provides software <sup>fi</sup>rms with a low-cost, low-risk promotional technique for their new products. By adopting an optimal free offer policy, <sup>fi</sup>rms can improve their pro<sup>fi</sup>t and solidify their position in the competitive marketplace by quickly reaching a larger portion of the market. The models we develop in this study can help <sup>fi</sup>rms make informed decisions when implementing the free offer policy. From our analyses in this research, it is obvious that <sup>fi</sup>rms should target the low-valuation potential adopters if it is easy to identify them. Even if signi<sup>fi</sup>cant cost will be incurred to identify these low-valuation customers, the model we propose can help decide whether the additional bene<sup>fi</sup>t generated from the low-valuation potential customers is suf<sup>fi</sup>cient to justify the cost of <sup>fi</sup>nding them. Besides free offer, <sup>fi</sup>rms typically have other options such as advertising or manipulating word-of-mouth by rewarding existing customers who recommend their products to others. The methodologies we develop in this study can help compare the bene<sup>fi</sup>ts of these options so that <sup>fi</sup>rms can choose the most ef<sup>fi</sup>cient promotional strategy.

This research may be extended along several directions. First, we only examine the offering of “unlimited” free software in this study; an obvious extension would be to develop a free offer policy for free software with time or content limitations. In the presence of such limitations, some free adopters may later decide to purchase the commercial version without any limitation. We expect that the stricter are such limitations, the more likely that the free adopters will <sup>fi</sup>nd that investing in the commercial version makes sense. On the other hand, too much limitation may affect the word-of-mouth in<sup>fl</sup>uences from the free adopters, either because they will be less con<sup>fi</sup>dent about the quality of the commercial version, or because they will be less enthusiastic or feel less obligated to spread the word about the product. This tradeoff needs to be considered when deciding the optimal degree of limitation for a free software version. Second, this study considers software products for which network externality is insigni<sup>fi</sup>cant, which allows us to focus on the increased speed of diffusion as the only bene<sup>fi</sup>t of free offer. For products for which both word-of-mouth and network externality are signi<sup>fi</sup>cant, the overall bene<sup>fi</sup>t will be even higher. A comprehensive model, incorporating both the increased speed of diffusion due to word-of-mouth and the improved valuation due to network externality, may be used to develop an optimal free offer strategy for this type of product. Third, we in this research treat the functionality of all versions as exogenously given. A possible extension would be to examine how many improvements should be included in a newer version to maximize the overall bene<sup>fi</sup>t for a <sup>fi</sup>rm. Fourth, we examine only two software versions in this study, it would be interesting to examine the bene<sup>fi</sup>t of free offer for products with more than two successive versions. With multiple versions, it is possible that the diffusion of a later version can be affected by the free offer decisions for all previous versions. However, we expect that most of the <sup>fi</sup>ndings derived for the two-version scenarios will remain valid for multiple versions. Finally, the pricing effect on the diffusion of a software product is not considered in this research. It may be possible to derive an optimal free offer policy under a dynamic pricing policy.

## Appendix

Proof of Proposition 1. Suppose that when the number of free adopters for version 1 is <sup>fi</sup>xed at $n _ { 1 } ,$ , the optimal number of free adopters for version 2 is n<sup>⁎</sup> and the corresponding left-shifting is $\varphi ^ { * } .$ When $n _ { 1 }$ changes to $\tilde { n } _ { 1 } ,$ , the optimal number of free adopters for version 2 and the corresponding optimal left-shifting changes to $\tilde { n } _ { 2 } ^ { * }$ and $\tilde { \Phi } ^ { * }$ , respectively.

By examining the objective function of Eq. (12), we conclude that with a <sup>fi</sup>xed number of free adopters for version 1, the <sup>fi</sup>rst term $m _ { 1 } \int _ { \tau } ^ { D + \tau } f _ { 1 } ( t ) e ^ { - r ( t - \tau ) } \mathrm { d } t$ and m′ in the second term are <sup>fi</sup>xed; therefore, the maximum revenue can be determined by selecting a φ that maximizes $\mu ( \varphi ) \equiv \int _ { \theta + \phi } ^ { D + \phi } f _ { 2 } ( t - \theta ) e ^ { - r ( t - \varphi ) } \mathrm { d } t$ . Since $\varphi ^ { * }$ is the optimal left-shifting corresponding to $n _ { 1 } ,$ we must have

$$
V (n _ {1}, \varphi^ {*}) \geq V (n _ {1}, \tilde {\varphi} ^ {*}),
$$

which yields

$$
V (n _ {1}, \varphi^ {*}) - V (n _ {1}, \tilde {\varphi} ^ {*}) = m _ {2} ^ {\prime} [ \mu (\varphi^ {*}) - \mu (\tilde {\varphi} ^ {*}) ] \geq 0 \Rightarrow \mu (\varphi^ {*}) \geq \mu (\tilde {\varphi} ^ {*}).\tag{A1}
$$

Similarly, the fact that $\tilde { \Psi } ^ { * }$ is the optimal left-shifting corresponding to $\tilde { n } _ { 1 }$ leads to

$$
\mu (\tilde {\varphi} ^ {*}) \geq \mu (\varphi^ {*}).\tag{A2}
$$

From Eqs. (A1) and (A2), we conclude

$$
\mu (\tilde {\varphi} ^ {*}) = \mu (\varphi^ {*}) \Rightarrow V (n _ {1}, \varphi^ {*}) = V (n _ {1}, \tilde {\varphi} ^ {*}).
$$

Following the same logic, we have

$$
V (\tilde {n} _ {1}, \tilde {\varphi} ^ {*}) = V (\tilde {n} _ {1}, \varphi^ {*}).
$$

If the left-shifting that maximizes $\mu ( \varphi )$ is unique, the following must hold:

$$
\tilde {\varphi} ^ {*} = \varphi^ {*}.
$$

Even if the optimal left-shifting is not unique, an optimal φ for a given value of $n _ { 1 }$ will be optimal for any other value of $n _ { 1 }$ as well. Therefore, we conclude that $\varphi ^ { * }$ is independent of $n _ { 1 }$ .

Further, since $n _ { 2 } ^ { * } { = } m _ { 2 } ^ { \prime } F _ { 2 } ( \stackrel { . } { \varphi } ^ { * } )$ and $m _ { 2 } ^ { \prime }$ increases with $n _ { 1 } , n _ { 2 } ^ { * }$ must also increase with $n _ { 1 } .$

Proof of Proposition 2. Suppose that the optimal solution for a given set of parameters is $\{ n _ { 1 } ^ { * } , \ n _ { 2 } ^ { * } , \ \theta ^ { * } \}$ , and the corresponding optimal revenue is $V ^ { * }$ . By examining the hazard rate Eq. (1), we can see that if the value of the coef<sup>fi</sup>cient of innovation increases from $p _ { 1 }$ to $p _ { 1 } .$ , the probability of adoption for those who have not adopted strictly increases. Therefore, if we keep the original optimal solution $n _ { 1 } ^ { * }$ $n _ { 2 } ^ { * } ,$ and $\boldsymbol { \theta } ^ { * } ,$ , the time interval between any two consecutive adoptions strictly decreases. Because of the discount factor, the net present value of all purchases will increase to V′ $( V ^ { \prime } { > } V ^ { * } )$ . Now, if we obtain a new solution $\{ \tilde { n } _ { 1 } ^ { * } , \tilde { n } _ { 2 } ^ { * } , \tilde { \theta } ^ { * } \}$ based on the increased coef<sup>fi</sup>cient of innovation $\tilde { p } _ { 1 } ,$ the resulting optimal revenue $\tilde { V } ^ { * }$ cannot decrease, i.e. $\tilde { V } ^ { * } \geq V ^ { \prime }$ Therefore, we must have $\tilde { V } ^ { * } \geq V ^ { * }$ . Based on the same reasoning, it can be shown that the optimal revenue also increases with $p _ { 2 } , q _ { 1 }$ , and $q _ { 2 } .$

Regarding λ, as shown in Eq. (14), a higher λ implies a larger p′; therefore, the optimal revenue increases strictly with λ.

With a larger $D ,$ some potential adopters who otherwise will not adopt before the end of the demand window will be able to adopt. Based on the same logic used in proving the conclusion regarding $p _ { 1 } ,$ it can be shown that the optimal revenue increases with D as well.

With a lower discount rate r, the same adoption will lead to lower discounted revenue and hence an increased revenue after discounting. Therefore, following a similar logic used for other parameters, the optimal revenue strictly increases as the discount rate r decreases.

## References

[1] F.M. Bass, A new product growth for model consumer durables, Management Science 15 (5) (1969)

[2] F.M. Bass, K. Gordon, T.L. Ferguson, M.L. Githens, DIRECTV: forecasting diffusion of a new technology prior to product launch, Interfaces 31 (3) (2001).

[3] B.L. Bayus, High-de<sup>fi</sup>nition television: assessing demand forecasts for a next generation consumer durable, Management Science 39 (11) (1993).

[4]. I Borland Fighting back against PC invaders Tech News on ZDNet (June 25 2002) available at http://news.zdnet.com/2100-1009\_22-939046.html

[5] California CPA, First Million Get Free Accounting Software — Free Stuff, (Dec. 2001).

[6] S. Chakravarty, K. Dogan, N. Tomlinson, A hedonic study of network effects in the market for word processing software, Decision Support Systems 41 (4) (2006).

[7] K. Dogan, Y. Ji, V. Mookerjee, and S. Radhakrishnan, managing the versions of a software product under variable and endogenous demand. Information Systems Research (forthcoming), doi:10.1287/isre.1090.0275.

[8] P. M. Eng, Below bargain basement: software freebies. Business Week, Nov. 8 (1993).

[9] C. Faugère, G.K. Tayi, Designing free software samples: a game theoretic approach Information Technology and Management 8 (4) (2007).

[10] J.M. Gallaugher, Y. Wang, Network effects and the impact of free goods: an analysis of the Web server market, International Journal of Electronic Commerce 3 (4) (1999).

[11] M. Givon, V. Mahajan, E. Muller, Software piracy: estimation of lost sales and the impact on software diffusion, Journal of Marketing 59 (1) (1995)

[12] E. Haruvy, A. Prasad, Optimal product strategies in the presence of network externalities, Information Economics and Policy 10 (4) (1998).

[13] E. Haruvy, A. Prasad, Optimal freeware quality in the presence of network externalities: an evolutionary game theoretical approach, Journal of Evolutionary Economics 11 (2) (2001).

[14] W. Hui, B. Yoo, K.Y. Tam, Economics of shareware: how do uncertainty and piracy affect shareware quality and brand premium? Decision Support Systems 44 (3) (2008).

[15] T. Islam, N. Meade, The diffusion of a technology: a more general model, Technological Forecasting and Social Change 56 (1997).

[16] Z. Jiang, S. Sarkar, The role of free software offer in software diffusion, Journal of Management Information Systems 26 (3) (Winter 2009–10).

[17] D.B. Jun, Y.S. Park, A choice-based diffusion model for multiple generations of products, Technological Forecasting and Social Change 61 (1999).

[18] V. Mahajan, E. Muller, Timing, diffusion, and substitution of successive generations of technological innovations: the IBM mainframe case, Technological Forecasting and Social Change 51 (1996).

[19] D.J. Manica, V. Mookerjee, S. Rhee, Optimal software demonstration design, Proceedings of the 13th Annual Workshop for Information Technology Systems, Seattle, WA, 2003.

[20] J. Norton, F.M. Bass, A diffusion theory model of adoption and substitution for successive generations of high-technology products, Management Science 33 (9) (1987).

[21] E.M. Rogers, Diffusion of InnovationsFifth Edition, Free Press, New York, NY, 2003.

[22] L.O. Wilson, J.A. Norton, Optimal entry timing for a product line extension, Marketing Science 8 (1) (1989).

[23] M.W. Speece, D.L. Maclachlan, Forecasting <sup>fl</sup>uid milk package type with a multigeneration new product diffusion model, IEEE Transactions on Engineering Management 39 (2) (1992).

[24] M.W. Speece, D.L. Maclachlan, Application of a multi-generation diffusion model to milk container technology, Technological Forecasting and Social Change 49 (3) (1995).

[25] M.Y. Wang, C.H. Chang, Applications of a multi-generation diffusion model to pagers and mobile phones, IEEE International Engineering Management Conference (IEMC), Cambridge, U.K., August, 2002

![](/api/attachments/M4GG8BP4/fulltext/images/72e562a35d078f34506ddb5e519912aafbf9b777e167f5ab78453f4ff2e6ca79.jpg)

Zhengrui Jiang is an assistant professor of Management Information Systems at the College of Business, Iowa State University. He received his PhD degree in Information Systems from the University of Texas at Dallas. His research interests include the impact of data quality on decisionmaking, software economics, and software engineering. His research has appeared in leading journals including Management Science, Information Systems Research, Journal of Management Information Systems, and International Journal of Research in Marketing, and in conferences such as ICIS, WITS, and PACIS. He is a member of AIS and INFORMS.
