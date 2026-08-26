---
otero_id: 15488
otero_key: "5SNSN9MP"
title: "Can Payment-per-Click Induce Improvements in Click Fraud Identification Technologies?"
authors: "Min Chen; Varghese S. Jacob; Suresh Radhakrishnan; Young U. Ryu"
year: "2015"
journal: "Information Systems Research"
doi: "10.1287/isre.2015.0598"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/5SNSN9MP/fulltext/images/2dc1f17f8bc5acdd986990d8496f6c40d95851971838177096bc6c23cd2c2829.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Can Payment-per-Click Induce Improvements in Click Fraud Identification Technologies?

Min Chen, Varghese S. Jacob, Suresh Radhakrishnan, Young U. Ryu

## To cite this article:

Min Chen, Varghese S. Jacob, Suresh Radhakrishnan, Young U. Ryu (2015) Can Payment-per-Click Induce Improvements in Click Fraud Identification Technologies?. Information Systems Research 26(4):754-772. http://dx.doi.org/10.1287/isre.2015.0598

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2015, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/5SNSN9MP/fulltext/images/542c69dde1efcf29554b115600eb4fab0ef1d90573d8f049922a4b46bee6e028.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Can Payment-per-Click Induce Improvements in Click Fraud Identification Technologies?

Min Chen

School of Business, George Mason University, Fairfax, Virginia 22030, mchen15@gmu.edu

Varghese S. Jacob, Suresh Radhakrishnan, Young U. Ryu Naveen Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080 {vjacob@utdallas.edu, sradhakr@utdallas.edu, ryoung@utdallas.edu}

ay-per-click (PPC) is a common pricing model used to pay for ads on the Web and is open to the possibility for click fraud, where clicks are not from a legitimate user. Identifying click fraud is generally done in a three-stage process: the service provider (SP) first classifies clicks as fraudulent or not, then the advertiser does the same with a different technology, and if there is a disagreement, the SP examines further and his conclusions are considered binding. The advertiser pays for clicks that are identified as valid in the first two stages or confirmed as valid in the last stage. We model the choice of the identification technologies as a double moral hazard problem We analyze the case where the PPC is incentive compatible to overcome the moral hazard problem, and examine the question of whether the incentive compatible PPC is sufficient to incentivize the two parties to unilaterally make further improvements to their identification technologies and simultaneously increase their profits. We show that when the cost of the third-stage identification technology is large, which is likely to be the case because of its complexity and use of expensive human experts, the incentive compatible PPC does not support unilateral technological improvements. We then examine a setting where the third-stage identification is delegated to a third party and find that this arrangement can induce unilateral improvements to the identification technologies in the first two stages. Collectively our results show that although the PPC model itself may not induce improvements in the first two stages of click fraud identification, a common arrangement espoused of having a third party resolve disagreements helps make PPC support unilateral technological improvements. Accordingly, we show an indirect benefit to the third-party arrangement.

Keywords: click fraud; online advertising; game theory; double moral hazard; incentives History: Alok Gupta, Senior Editor; Giri Kumar Tayi, Associate Editor. This paper was received on November 14, 2011, and was with the authors 27 months for 4 revisions. Published online in Articles in Advance November 12, 2015.

## 1. Introduction

The revenues from online advertising totaled \$49.5 billion in 2014 in the United States (IAB 2015), up 16% from 2013’s record-breaking number, and are projected to grow rapidly in the coming years as Web access and utilization become more pervasive (eMarketer 2014). Currently, the pay-per-click model (PPC) is the most prevalent pricing model for online advertising, accounting for 66% of the market in 2014 (IAB 2015). In this model, advertisers pay the service provider (SP) each time someone clicks on the ad, i.e., the payment is on a per-click basis.<sup>1</sup>

Although the PPC model is the most prevalent model, it is susceptible to click fraud, a practice of imitating a legitimate user to click on an ad to generate a charge per click without having an actual interest in the target of the ad (Liu et al. 2009).<sup>2</sup> The average click fraud rate is estimated to be around 20% (Click Forensics 2010a), resulting in significant damage to the PPC market. Solve Media estimated the loss in advertising for marketers due to click fraud at a staggering \$11.6 billion in 2014, up 22% from 2013 (O’Malley 2014). Click fraud has also severely undermined the faith of the PPC advertisers: Noting that bots are employed for click frauds, a recent survey of online publishers finds that 34% of respondents plan to deploy anti-bot solutions in 2014, a 125% increase over 2013 (Taube 2014). In another survey conducted by Ponemon Institute (2013), 65% of the respondents have experienced click frauds in their companies and 74% believe it would be very difficult to detect. As a result, click fraud is considered “the biggest threat to the Internet economy” by George Reyes, Chief Financial Officer of Google (Delaney 2005).

1.1. Industry Background and Research Question In the quest to identify click frauds, clicks are scrutinized by the SP and advertisers using various technologies in the following sequence. Once a click occurs, in the first stage the SP uses an array of automated algorithms and filters to detect invalid or fraudulent clicks in real time. This system relies on click patterns to detect invalid clicks (Google 2014) and the advertisers are not charged for the clicks identified as invalid. This system requires no involvement from advertisers and is known as the proactive system by Google. Although reportedly the rule-based online filters can detect simple forms of invalid clicks, they can be ineffective to detect advanced click fraud attacks (Tuzhilin 2006). In addition, since technical details are proprietary and thus not disclosed to outsiders, the advertisers are not informed about the performance of this system. As a result, in the second stage many advertisers use either in-house expertise or click fraud auditing firms to verify the clicks using their server-side data and contest clicks that they deem to be invalid or fraudulent—see AdWatcher (2010), Click Forensics (2010b), Dunaway (2010) and Megna (2008) for examples. In the third stage of identifying invalid clicks, the contested clicks are investigated by the SP with the help of advanced offline tools or human experts— Google refers to this system as the reactive system. Clicks classified as invalid at this stage are refunded to advertisers (Ghosemajumder 2007). Both Google and Yahoo! accept and investigate advertisers’ inquiries on invalid clicks from its advertisers (see Olsen 2008, Perez 2008 for examples) and Google claims that “all advertiser inquiries about invalid clicks are investigated” and “taken very seriously” (Google 2014).

Two features of the technologies employed to identify fraudulent clicks are noteworthy. First, the SPs and advertisers do not disclose the technical details used to identify invalid clicks for fear of the information falling into the wrong hands (Tuzhilin 2006, Wilbur and Zhu 2009). Gaustella (2007) states that service providers use “0 0 0 different signals that must be monitored to detect click fraud, signals that are a closely guarded company secret 0 0 0 0” As such, the quality of the technologies is not directly observable and contractible, leading to a double moral hazard problem. Second, the quality of the identification technologies does not appear to be very high, as the estimates of undetected click fraud rates are quite high: for example, a study conducted by Fair Isaacs estimates that 10%–15% of clicks billed to PPC advertisers are undetected fraudulent traffic (Howlett 2007). These high estimates of nondetection of click frauds suggest that there is considerable room for making improvements in the click fraud identification technologies.

The importance of the issue of click fraud and the observation of the poor technology employed for identifying invalid clicks lead us to examine whether the PPC is sufficient to incentivize the SP and the advertiser to unilaterally make improvements to their respective technologies. Specifically, we examine whether the SP will improve his click fraud identification technologies and gain additional profits, even if the advertiser does not make such improvements; and similarly, whether the advertiser will improve his click fraud identification technology and gain additional profits, even if the SP does not make such improvements: this is what we mean by unilateral improvements to technologies. If the answer to this question is affirmative, then we can conclude that despite the double moral hazard problem embedded in the click fraud problem, the PPC model will induce the two parties to work toward improving the click fraud identification technologies; of course, if the answer is not affirmative, the PPC model may need to add other elements such as third-party investigation to mitigate the agency problem.

## 1.2. Model Summary

1.2.1. The Payment per Click (PPC). To address this question, we consider a double moral hazard, principal-agent setting with the advertiser as the principal and the SP as the agent. The advertiser and the SP agree on a flat-rate PPC. Flat-rate PPC is common to comparison shopping websites/engines like PriceGrabber, eBay, and SlickDeals, who typically publish PPC rate cards based on the content, traffic, and competition of terms (Clay 2011). Numerous marketing advisory companies have developed their business model based on flat-rate PPC, instead of the auction PPC that is based on keywords such as Google’s AdWords (see BlissITSolution 2014, PocketCents 2014, Recker 2013 for examples).

1.2.2. The Click Fraud Identification Technologies. A click can be either valid or invalid and the true nature of the click is not observable. The SP and the advertiser have common knowledge of the probability that a click is valid. Once a click occurs, a three-stage process of identifying click fraud similar to that in practice occurs in the following order: First, the SP classifies clicks using a click fraud detection technology. Second, the clicks classified as valid by the SP’s detection technology are examined by the advertiser using a verification technology. Finally, the SP uses an investigation technology to classify the clicks disputed by the advertiser. The detection and investigation technologies correspond to the proactive and reactive systems employed by Google (Ghosemajumder 2007).<sup>3</sup> The classifications by the detection, verification, and investigation technologies are imperfect: they do not identify all invalid clicks and may incorrectly classify some valid clicks as invalid (see Gaustella 2007). In this paper, we use the term “precision” to refer to the quality of the technologies, and technically precision is the probability that a valid click is classified correctly by the technology. The advertiser pays the agreed on flat-rate PPC for the clicks that are identified as valid by both the detection and verification technologies or confirmed as valid by SP’s investigation technology.

1.2.3. The Double Moral Hazard Problem. The SP and the advertiser can choose either a high or low technology, where the high technology is of higher precision than the low technology. As such, high technologies are also more costly. Whether the SP and the advertiser choose the high or low technology is not observable to the other party for fear of the information falling into the wrong hands (Tuzhilin 2006, Wilbur and Zhu 2009), and thus each party chooses the respective high or low technologies to maximize his own expected profit. The high and low technologies are similar to the agent’s high and low efforts in the standard principal-agent models.

The incentive compatible PPC needs to induce the choice of high technologies by both parties and is determined by the “weakest link” of the three technologies. For example, if the cost of investigation technology is sufficiently large, the agency problem of inducing the SP’s high investigation technology is most severe and the PPC is determined by the incentive constraint with respect to the SP’s investigation technology. We refer to this as the SP’s investigation technology being the weakest link in the sequence of actions. As such, the PPC that induces the SP’s choice of the high investigation technology will also induce both the high detection and verification technologies. This is similar in spirit to prior double moral hazard principal-agent models (for example, see Hwang et al. 2006, Jayanth et al. 2011).

We then turn to the main research question: given that high technologies are induced by PPC, whether the SP will improve the precision of his high detection and high investigation technologies and gain additional profits, even if the advertiser does not make improvements to the high verification technology; and similarly, whether the advertiser will improve his high verification technology and gain additional profits, even if the SP does not make improvements to the high detection and investigation technologies.<sup>4</sup> We consider only improvements in a technology without a corresponding increase in cost because in most cases, improvements in technology can occur without significant additional cost (Lee 2007), and more important, if the parties do not find it beneficial to improve their technologies without a corresponding increase in costs, considering an increase in costs will make them not choose improvements more intensely. As such, our insight should be considered as the possible best-case scenario.

## 1.3. Summary of Results

We highlight here the intuition for the case where the SP’s investigation technology is the weakest link, because the cost of investigation technology is typically quite high (see Tuzhilin 2006). We find that improving the precision of the high investigation technology decreases the SP’s expected profit. When the difference between precisions across the high and low investigation technologies increases, as will happen when the SP makes improvements to the high investigation technology, less incentive (PPC) is required to induce the high investigation technology. In other words, the unilateral improvement by the SP to the high investigation technology will make the investigation technology less weak and thus, the PPC—the role of which is to induce the SP’s high investigation—can be decreased. This leads to lower expected profits for the SP.

A similar intuition holds for improvements in the SP’s detection technology. If the SP was to improve the precision of the high detection technology without any improvements in the high verification technology by the advertiser, the probability that the advertiser contests a truly valid click increases because of a lower misclassification rate from the improved detection technology. This increases the SP’s incentive to choose the high investigation technology to identify the contestable clicks that are truly valid and hence leads to a less severe agency problem with respect to the investigation technology. This will make the investigation technology less weak and hence the PPC can be decreased, leading to lower expected profits for the SP. Overall, the SP does not have an incentive to improve the investigation or detection technologies unilaterally, when the investigation technology is the weakest link.

The advertiser also does not have an incentive to improve the high verification technology unilaterally. When the advertiser does a good job of catching fraudulent clicks by improving the high verification technology, the SP does not need to work as hard with the investigation technology, i.e., the SP has to be paid more to ensure that he chooses the high investigation technology. In the sequential action double moral hazard settings, improvements in the precision of the high verification technology results in the investigation technology becoming more of a weak link, which in turn increases the PPC. This leads to a lower expected profit for the advertiser. As such, the advertiser does not have an incentive to improve the verification technology unilaterally. Overall, we find that the PPC alone fails to induce either the SP or the advertiser to unilaterally improve their respective click fraud classification technologies. In additional analysis, we show that these insights continue to hold in settings where there is private information held by the advertiser on his true valid click rate and when we consider competitive intensity is not too high among advertisers (see Online Appendix B (available as supplemental material at http://dx.doi.org/10.1287/isre.2015.0598)).

An important point to note is that the PPC in our model is geared for solving the double moral hazard problem of inducing the SP and the advertiser to choose the high precision technologies; however, our question requires it to solve a problem that it is not geared to address in the first place: to induce the SP and the advertiser to make unilateral improvements to the high precision technologies. As such, even though this may appear to be “unfair” on the PPC model, we show that a common arrangement/mechanism can mitigate this problem and make PPC incentive compatible even for an incentive problem that it is not designed to address. Specifically, we consider a third party in the third stage that resolves the disputes between the SP and the advertiser. Similar to this arrangement, Gaustella (2007) recommends using independent auditors and more recently, Vranica (2014) advocates independent parties for advertisers.

We consider two regimes: one in which the SP pays for the third-party investigation, and two in which the advertiser pays for the third-party investigation. We show that PPC is incentive compatible for inducing unilateral improvements under both regimes. The intuition stems from noting that the party who pays for the investigation has a direct incentive to make improvements to the classification technology. This incentive spills over to the other party so as to fall in line or contest more appropriately. Thus, the third party helps to coordinate/align the incentives of the SP and the advertiser, even with the PPC model. Overall, under this arrangement the PPC model can induce not only the choice of high technologies but also unilateral improvements on the technologies. We thus highlight an indirect benefit of such delegation of click fraud classification to third parties in the last stage.

The rest of the paper is organized as follows: §2 reviews related literature; §3 describes the key elements of the model; §4 analyzes the model, provides the main results, and illustrates results using numerical examples; §5 examines an extension to the model by considering the delegation of third-stage investigation to a third party; and §6 discusses managerial insights and concludes the paper.

## 2. Related Literature

Our study is closely related to two streams of literature: one that examines the click fraud problem, and the other that examines the double moral hazard problem.

## 2.1. Literature on Click Fraud Problem

The issue of click fraud has drawn increased attention in recent years. Mungamuru et al. (2008) examine the economic incentives for the SP to fight click fraud occurring in publishers’ content networks. They find that both the SP and the advertiser’s interests are aligned to prevent the “perverse behavior” of click fraud by the content provider. In effect, if both the SP and the advertiser are “hurt” by the content provider who perpetrates click fraud, both the SP and the advertiser’s economic interests are aligned. By contrast, we take the click fraud as given and examine a setting where the SP and the advertiser have to tag a click as valid or invalid, and thus their interests are not aligned. The advertiser has an incentive to overstate invalid clicks, and the SP has the incentive to overstate valid clicks.

Wilbur and Zhu (2009) analyze the effects of click fraud on the online advertising industry. They show that when advertisers know the level of click fraud, they will lower their bids to the point that click fraud has no impact on total advertising expenditures. However, when the level of click fraud is uncertain, the SPs revenues will rise when the keyword auction is less competitive and fall when the keyword auction is more competitive. By implication, their results suggest that the PPC advertising industry can benefit from having a neutral third party to audit SPs’ click fraud detection algorithms so as to mitigate the uncertainty in click fraud. We extend this by not only considering the agency problem but also unilateral improvements in click fraud identification technologies and thus provide one possible economic rationale for third-party audits as suggested by Wilbur and Zhu (2009). We also examine the third-party investigation mechanism in this paper and show an indirect benefit in terms of helping to incentivize the SP and the advertiser to make improvements in their classification technologies.

Other works focus on the use of alternative payment methods to mitigate the click fraud problem. In particular, Mahdian and Tomak (2009) suggest the PPA model. They examine the challenges in the design of incentive-compatible PPA mechanisms and suggest approaches to tackle some of them. The PPA model, however, creates an incentive for advertisers not to report all conversions that occur on their websites, which is action fraud. Goodman (2005) proposes a pricing scheme that sells advertisers a particular percentage of all impressions rather than user clicks. Yet, the payper-percentage of impressions model, apart from being difficult to implement, deviates from the developed industry standard that sells clicks, and risks a negative backlash in the marketplace (Immorlica et al. 2005).

Overall, in contrast to these studies, we model the click fraud issue as a double moral hazard problem. Specifically, we consider the interaction between the technologies employed for classifying clicks and examine whether the PPC model would provide sufficient incentives for the SP and the advertiser to unilaterally improve their technologies. As mentioned earlier, similar to Wilbur and Zhu (2009) our results also suggest that a third party is beneficial to the PPC advertising industry. However, the reasons for such an implication are quite different from theirs: specifically, the third party helps to induce both parties to effect improvements in their technologies, which in turn will help enhance advertiser’s confidence in online advertising.

2.2. Literature on Double Moral Hazard Problems Double moral hazard problems have been examined extensively in economics and have been applied in a variety of settings. Baiman et al. (2000) examine penalties based on information from incoming inspection when the supplier’s design effort and the buyer’s appraisal effort are not observable. They show that installing an information system that makes the buyer’s appraisal result contractible can help improve product quality and the supplier’s design effort. Balachandran and Radhakrishnan (2005) examine a double moral hazard case where both the supplier’s and the buyer’s qualities are unobservable. They consider not only whether contract payments and penalties based on either information from incoming inspection or information from external failures induce first-best quality but also whether the penalty satisfies the fairness criterion. Hwang et al. (2006) examine a two-tier supply chain consisting of a supplier and a buyer, with the supplier’s quality and the buyer’s inspection effort being unobservable. They compare the inspection regime with the certification regime and show that inspection leads to additional agency cost because of the presence of agency problems, which provides a rationale for the shift to the certification regime even though the direct cost of inspection is low.

We extend these studies to the click fraud setting by examining the interactions between sequential actions by the two parties. To our knowledge, there have been no studies that examine such sequential actions in double moral hazard settings. This enables us to provide insights into whether the parties would improve the productivity of their high action in such sequential action settings.

## 3. Model Description

We examine a double moral hazard problem between a risk-neutral advertiser and a risk-neutral SP. The advertiser’s sponsored link receives x clicks enabled by the SP. Without loss of generality, we set x = 1. A click could be either valid (nonfraudulent) or invalid (fraudulent). The information on whether a click is fraudulent is not observable to the advertiser or the SP. Both the advertiser and the SP assess a probability of  that a click is valid, i.e., with probability 1 −  the advertiser and the SP expect the click to be fraudulent. Table 1 provides a list of notations used in this paper.

The SP uses a detection technology that correctly classifies a valid click as valid with probability $q ^ { \check { S 1 } }$ and an invalid click as invalid with probability $\dot { \phi ^ { S 1 } } \dot { q ^ { S 1 } }$ where $\phi ^ { S 1 }$ is such that $\phi ^ { s 1 } q ^ { s 1 } < 1 . \AA ^ { 5 }$ Correspondingly, the detection technology’s type I error rate of classifying a valid click as invalid is $\mathsf { \bar { 1 } } - q ^ { S 1 }$ , and the type II error rate of classifying an invalid click as valid is $1 - \phi ^ { S 1 } q ^ { S 1 }$ We refer to $q ^ { \check { S } 1 }$ as the precision of the detection technology because increasing $q ^ { \dot { S } 1 }$ would result in a decrease in both type I and type II errors.<sup>6</sup> The report of the classification by the detection technology is denoted $r ^ { S 1 } = v , f$ for valid and invalid or fraudulent clicks, respectively. The SP can choose a detection technology with either a high or low precision, i.e., $q ^ { S 1 } \in \{ q _ { H } ^ { S 1 } , q _ { L } ^ { S 1 } \}$ with $q _ { H } ^ { S 1 } > q _ { L } ^ { S 1 } > 0 . 5 . ^ { 7 }$ The corresponding cost of the high and low detection technology is $C ^ { S 1 } ( q ^ { S 1 } ) \in \{ C _ { H } ^ { S 1 } , C _ { L } ^ { \stackrel { \smile } { S 1 } } \}$ with $C _ { H } ^ { S 1 } > C _ { L } ^ { S 1 }$ . The choice of the detection technology is not observable to the advertiser, and thus is subject to moral hazard (see, for example, Gaustella 2007 discussed in §1). All clicks are subject to classification by the detection technology and there is a unit cost $m ^ { S 1 }$ for classifying each click. We assume that the unit cost is the same irrespective of whether the high or low detection technology is chosen by the SP.

Table 1 Summary of Notations

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $\alpha$ </td><td>The probability that a click is valid, i.e., the valid click rate</td></tr><tr><td> $\beta$ </td><td>The probability that the valid customer&#x27;s visit results in a sale, i.e., conversion rate</td></tr><tr><td> $\gamma$ </td><td>The advertiser&#x27;s expected benefit from a valid click</td></tr><tr><td> $\lambda$ </td><td>The expected profit obtained from a customer&#x27;s purchase</td></tr><tr><td> $\theta$ </td><td>The advertiser&#x27;s PPC to the SP (decision variable)</td></tr><tr><td> $q_{i}^{S1}$ </td><td>The precision of the SP&#x27;s detection technology  $i \in \{H, L\}$ </td></tr><tr><td> $q_{i}^{A}$ </td><td>The precision of the advertiser&#x27;s verification technology  $j \in \{H, L\}$ </td></tr><tr><td> $q_{k}^{S2}$ </td><td>The precision of the SP&#x27;s investigation technology  $k \in \{H, L\}$ </td></tr><tr><td> $\phi^{S1}$ </td><td>The ratio of true positive to true negative for the SP&#x27;s detection technology</td></tr><tr><td> $\phi^{A}$ </td><td>The ratio of true positive to true negative for the advertiser&#x27;s verification technology</td></tr><tr><td> $\phi^{S2}$ </td><td>The ratio of true positive to true negative for the SP&#x27;s investigation technology</td></tr><tr><td> $r_{i}^{S1}$ </td><td>Report by SP&#x27;s detection technology ( $v$  and  $f$  denotes valid and fraud clicks, respectively)</td></tr><tr><td> $r_{ij}^{A}$ </td><td>Report by advertiser&#x27;s verification technology</td></tr><tr><td> $r_{ijk}^{S2}$ </td><td>Report by SP&#x27;s investigation technology</td></tr><tr><td> $C_{i}^{S1}$ </td><td>The SP&#x27;s detection cost when choosing detection technology  $i \in \{H, L\}$ </td></tr><tr><td> $C_{j}^{A}$ </td><td>The advertiser&#x27;s verification cost when choosing verification technology  $j \in \{H, L\}$ </td></tr><tr><td> $C_{k}^{S2}$ </td><td>The SP&#x27;s investigation cost when choosing investigation technology  $k \in \{H, L\}$ </td></tr><tr><td> $m^{S1}$ </td><td>The unit cost of classifying a click by SP&#x27;s detection technology</td></tr><tr><td> $m^{A}$ </td><td>The unit cost of classifying a click by advertiser&#x27;s verification technology</td></tr><tr><td> $m^{S2}$ </td><td>The unit cost of classifying a click by SP&#x27;s investigation technology</td></tr><tr><td> $I_{i}^{A}$ </td><td>Verification probability, i.e., the probability that a click is verified by the advertiser</td></tr><tr><td> $I_{ij}^{S2}$ </td><td>Investigation probability, i.e., the probability that a click is examined by SP&#x27;s investigation technology</td></tr><tr><td> $T_{ijk}$ </td><td>Payment probability, i.e., the probability that a click is paid to the SP</td></tr><tr><td> $\bar{V}$ </td><td>The SP&#x27;s reservation profit</td></tr><tr><td> $\bar{U}$ </td><td>The advertiser&#x27;s reservation profit</td></tr></table>

The clicks classified as valid by the SP are then verified by the advertiser.<sup>8</sup> The advertiser’s verification technology classifies a truly valid click that is classified as valid by the SP, as valid with probability $q ^ { A }$ . Also, it classifies a truly invalid click that is classified as valid by the ${ \mathrm { S P } } ,$ as invalid with probability $\phi ^ { A } q ^ { A } ,$ where $\bar { \phi } ^ { A }$ is such that $\phi ^ { A } q ^ { A } < 1$ . The precision of the verification technology is characterized by $q ^ { A }$ . The report of the classification by the verification technology is denoted $r ^ { A } = v , f ,$ for valid and fraudulent clicks, respectively. The advertiser can choose a verification technology with either a high or low precision, $\mathrm { i . e . , }$ $q ^ { A } \in \{ q _ { H } ^ { A } , \overline { { q _ { L } ^ { A } } } \}$ , where $q _ { H } ^ { A } \ ( q _ { L } ^ { A } )$ denotes the precision of high (low) verification technology with a corresponding verification cost $C ^ { A } ( q ^ { A } ) \in \{ C _ { H } ^ { A } , \stackrel { \smile } { C _ { L } ^ { A } } \}$ , where $q _ { H } ^ { A } > q _ { L } ^ { A } > 0 . { \breve { 5 } }$ and $C _ { H } ^ { A } > C _ { L } ^ { A }$ . The advertiser’s choice of verification technology is not observable to the SP, and thus is subject to moral hazard as well (see Gaustella 2007). In addition, there is a unit cost $m ^ { A }$ for verifying a click. We assume that the unit cost is the same irrespective of the verification technology chosen by the advertiser. The verification probability, i.e., the probability that a click is verified by the advertiser, is denoted by

$$
I _ {i} ^ {A} = \mathrm{Pr} (r _ {i} ^ {S 1} = v) = \alpha q _ {i} ^ {S 1} + (1 - \alpha) (1 - \phi^ {S 1} q _ {i} ^ {S 1}),
$$

where the subscript $i \in \{ H , L \}$ denotes that the report is conditioned on whether the high or low detection technology $( q _ { i } ^ { S 1 } )$ is chosen.

The disagreements between the $\mathrm { S P ^ { \prime } s }$ and the advertiser’s classifications of clicks are resolved by the SP investigating such disagreements.<sup>9</sup> The investigation technology correctly classifies a contestable click $( \mathrm { i . e . , }$ a click that is classified as valid by the SP but as invalid by the advertiser) that is truly valid as valid with probability $q ^ { S 2 }$ , which denotes the precision of the investigation technology. Similarly, it correctly classifies a contestable click that is truly invalid as invalid with probability $\phi ^ { S 2 } q ^ { S 2 }$ , where $\check { \phi ^ { S 2 } }$ is such that $\phi ^ { S 2 } q ^ { S 2 } < 1$ The report of the classification by the $\mathrm { S P ^ { \prime } s }$ investigation technology is denoted by $r ^ { S 2 } = v , f$ for valid and fraudulent clicks, respectively. The SP can choose an investigation technology with either a high or low precision, i.e., $q ^ { S 2 } \in \{ q _ { H } ^ { S 2 } , q _ { L } ^ { S 2 } \}$ with $q _ { H } ^ { S 2 } > q _ { L } ^ { S 2 } > 0 . 5 .$ . The corresponding cost of the high and low investigation technology is $C ^ { S 2 } ( q ^ { S 2 } ) \in \{ C _ { H } ^ { S 2 } , C _ { L } ^ { S 2 } \}$ with $C _ { H } ^ { S 2 } > C _ { L } ^ { S 2 }$ . The choice of the investigation technology is not observable to the advertiser and thus is subject to moral hazard (see Gaustella 2007). In addition, there is a unit cost $m ^ { S 2 }$ for investigating a contestable click. We assume that the unit cost is the same irrespective of the investigation technology chosen by the SP. The investigation probability, i.e., the probability a click is investigated by the SP, is denoted by

$$
\begin{array}{r l} & I _ {i j} ^ {S 2} = \operatorname * {P r} (r _ {i} ^ {S 1} = v, r _ {i j} ^ {A} = f) \\ & \qquad = \alpha q _ {i} ^ {S 1} (1 - q _ {j} ^ {A}) + (1 - \alpha) (1 - \phi^ {S 1} q _ {i} ^ {S 1}) \phi^ {A} q _ {j} ^ {A}. \end{array}
$$

Note that $I _ { i j } ^ { S 2 }$ is determined by both the precision of the $\mathrm { S P ^ { \prime } s }$ detection technology $( \dot { q } _ { i } ^ { S 1 } )$ and the precision of the advertiser’s verification technology $( q _ { i } ^ { \bar { A } } )$

Without loss of generality, we let $\bar { C _ { L } ^ { S 1 } } = \bar { C _ { L } ^ { A } } = C _ { L } ^ { S 2 } = 0 .$ We also assume that the $\mathrm { S } \dot { \mathrm { P } ^ { \prime } } \mathrm { s }$ investigation technology is much more costly than the detection technology, $\mathrm { i . e . , } C _ { H } ^ { S 2 } \gg C _ { H } ^ { S 1 }$ , because the $\mathrm { S P ^ { \prime } s }$ investigation is complex and involves costly human expertise (Tuzhilin 2006). Thus, the investigation technology cannot be used to replace the detection technology because of its high complexity and cost. Furthermore, the cost of high investigation technology $( C _ { H } ^ { S 2 } )$ could be very large because advanced click fraud attacks can closely simulate genuine human visitor behavior (Eroshenko 2004), and hence identifying them accurately in the investigation stage can be very expensive. We further assume that the unit cost of investigation $( m ^ { S 2 } )$ is much greater than the unit cost of detection and verification, $\mathrm { i . e . , } m ^ { S 2 } \gg \{ m ^ { S 1 } , m ^ { A } \}$ , because the investigation involves the use of advanced offline tools and sometimes human examinations whereas the other two technologies usually use automated programs for classification and hence have a very small unit cost of classification. Furthermore, for simplicity we set $\phi ^ { S 1 } = \phi ^ { A } = \phi ^ { S 2 } = 1$ in the analysis because our results are not driven by these parameters.

The advertiser pays the SP  for each click that is agreed as valid by both the SP and the advertiser or identified as valid by the $\mathrm { S P ^ { \prime } s }$ investigation technology. It is the flat-rate PPC that is agreed on by both players at the beginning of the game.<sup>10</sup> This is equivalent to the advertiser paying  for each click classified as valid by the $\mathrm { S P ^ { \prime } s }$ detection technology, and then obtaining a refund of  for clicks classified as invalid by the verification and investigation technologies as is typical in flat-rate PPC models.

The sequence of events unfolds as follows. First, the advertiser and the SP agree on PPC . Second, the SP chooses the detection and investigation technologies, and the advertiser chooses the verification technology. Finally, the clicks occur, the technologies classify the clicks and the payment occurs accordingly. We assume that the classification obtained from the technologies cannot be manipulated by the SP or the advertiser. In effect, the choice of the technologies, i.e., the program/code and the team who are dedicated to examine/monitor the clicks, constitutes the processes that spew out the classification. The events are depicted in Figure 1.

We denote by $T _ { i j k }$ the probability that a click is classified as valid by the detection and verification technologies or confirmed as valid by the investigation technology, where $i , j , k \in \{ H , L \}$ indicate the detection, verification, and investigation technologies chosen by both parties. It is the conditional probability that a click is paid for and is referred to as the payment probability in the rest of the paper. Specifically, $T _ { i j k }$ is given by (with Pr denoting probability)

$$
\begin{array}{l} T _ {i j k} = \operatorname * {P r} [ \text {a click is paid} | q _ {i} ^ {S 1}, q _ {j} ^ {A}, q _ {k} ^ {S 2} ] \\ \qquad = \alpha q _ {i} ^ {S 1} [ q _ {k} ^ {S 2} + q _ {j} ^ {A} (1 - q _ {k} ^ {S 2}) ] + (1 - \alpha) (1 - q _ {i} ^ {S 1}) (1 - q _ {j} ^ {A} q _ {k} ^ {S 2}). \end{array}
$$

The advertiser expects to receive a benefit of  from a truly valid click: the expected benefit of  includes not only the expected profit obtained from the customer who has clicked through to the advertiser’s site and made a purchase (denoted by 5 but also the probability that a valid customer’s visit results in a sale (also known as the “conversion rate,” denoted by 5, i.e., $\gamma = \lambda \beta .$ Thus, given that not all truly valid customers may buy the advertiser’s products/services, the outcome of the sales cannot be used to provide information on truly valid clicks. The expected profit for the advertiser (U 5 for $i , j , k \in \{ H , L \}$ is given by

$$
U _ {i j k} = \gamma \alpha - \theta T _ {i j k} - C _ {j} ^ {A} - m ^ {A} I _ {i} ^ {A},
$$

where $U _ { i j k }$ is the advertiser’s expected benefit from the click, less (a) the expected payment to the SP, (b) the cost of verification technology, and (c) the expected cost of verifying the clicks classified by the detection technology as valid. We assume that the advertiser’s expected benefit from a valid click (5 is sufficiently high such that he will receive a nonnegative profit from participating in the PPC advertising.

The expected profit for the SP (V 5 for $i , j , k \in \{ H , L \}$ is given by

$$
V _ {i j k} = \theta T _ {i j k} - C _ {i} ^ {S 1} - C _ {k} ^ {S 2} - m ^ {S 1} - m ^ {S 2} I _ {i j} ^ {S 2},
$$

Figure 1 Game Tree for the Click Fraud Problem  
![](/api/attachments/5SNSN9MP/fulltext/images/48a391f376780bc88a2abda1105a898807876f155cb613559e85182bc5ba9d3c.jpg)  
where $V _ { i j k }$ is the $\mathrm { S P ^ { \prime } s }$ expected click payment from the advertiser less (a) the cost of the detection technology, (b) the cost of the investigation technology, (c) the expected cost of detection, and (d) the expected cost of investigation. Note that the detection technology classifies all clicks, whereas the investigation technology only needs to examine contestable clicks $( I _ { i j } ^ { S 2 }$ denotes the investigation probability).

## 4. Analysis

We examine the case where the PPC induces the choice of high technologies with the advertiser as the principal and the SP as the agent. The optimization problem is represented in Program 1.

## Program 1

$$
\max _ {\theta} U _ {H H H}\tag{OBJ}
$$

$$
\text { subject   to } V _ {H H H} \geq \bar {V} = 0,\tag{PCS}
$$

$$
V _ {H H H} \geq V _ {L H H},\tag{ICS1}
$$

$$
V _ {H H H} \geq V _ {H H L},\tag{ICS2}
$$

$$
V _ {H H H} \geq V _ {L H L},\tag{ICS12}
$$

$$
U _ {H H H} \geq U _ {H L H}.\tag{ICC}
$$

The advertiser’s expected profit function is given in (OBJ). The participation constraint (PCS) ensures that the PPC is such that the $\mathrm { S P }$ receives at least the reservation profits. Constraints (ICS1), (ICS2), and (ICS12) are the incentive compatibility constraints for the choice of high detection and investigation technologies by the SP: the advertiser’s PPC (5 induces SP’s high rather than low detection and investigation technologies. Constraint (ICC) is the incentive compatibility constraint with respect to the advertiser’s verification technology: the constraint ensures that the advertiser chooses high verification technology when the SP chooses the high detection and investigation technologies. The double moral hazard problem arises because the PPC has to ensure that both parties choose the high technologies.

Program 1 is different from standard double moral hazard problems (see Demski et al. 2004 and Hwang et al. 2006) in two important aspects: first, the $\mathrm { S P }$ can choose two technologies, i.e., detection and investigation technologies, in sequence; second, the advertiser’s choice of verification technology occurs in between the $\mathrm { S P ^ { \prime } s }$ technology choices. These aspects are important for the insights and will be discussed later when we examine the improvements in technologies (see Observations 1–3).

We make some assumptions to ensure that the representation of the problem conforms to the double moral hazard settings. First, we assume the payment probability $( T _ { i j k } )$ satisfies (A1).

Assumption 1 (A1). <sub>(a)</sub> $T _ { H j k } > T _ { L j k } , ( \mathrm { b } ) \ T _ { i j H } > T _ { i j L } ,$ and (c) $T _ { i L k } > T _ { i H k } , f o r \ i , j , k \in \{ H , \bar { L } \}$

Assumptions A1(a) and A1(b) state that compared to the low detection and investigation technologies, the high technologies increase the payment probability, i.e., $d \breve { T } / d q ^ { S 1 } > 0 , \breve { d } T / d q ^ { S 2 } > 0$ . This provides the SP with an incentive to choose high rather than low detection and investigation technologies. Assumption $\operatorname { A 1 } ( \operatorname { c } )$ states that compared with the low verification technology, the high verification technology decreases the payment probability, i.e., $d T / d q ^ { A } < 0$ . This provides the advertiser with the benefit of choosing high rather than low verification technology. Overall, Assumption A1 is similar to the assumption in the standard agency problems where high actions are more productive than low actions.

Second, we assume that the cost of the high investigation technology is sufficiently large compared to the cost of high detection technology.

Assumption 2 (A2). <sub>C</sub>S2<sub>/C</sub>S1 <sub>+</sub> <sub>m</sub>S1 <sub>+</sub> <sub>m</sub>S2<sub>I</sub> S2 <sub>></sub> 4T<sub>HHH</sub> − T<sub>HHL</sub>5/4T<sub>HHL</sub> − T<sub>LHL</sub>5.

Assumption 2 compares the ratio of the investigation technology cost to the sum of the detection technology cost and the unit costs with the ratio of investigation technology effectiveness to detection technology effectiveness. We define the effectiveness of a technology as the difference in the payment probability when the SP (advertiser) chooses the high (low) instead of the low (high) technologies. In other words, it measures how “effective” the high technology is in increasing (decreasing) the payment probability for the SP (advertiser) than the low technology. Note that what we call effectiveness is directly related to the notion of informativeness in hidden-action principal-agent models. The effectiveness is a function of the precisions of the high and low technologies but does not directly measure the quality aspect.

Particularly, the numerator of the right side of Assumption 2 is the effectiveness of the investigation technology, i.e., $T _ { H H H } - T _ { H H L } ,$ and the denominator is the effectiveness of the detection technology, i.e., $T _ { H H L } - T _ { L H L }$ . As discussed previously, given that the investigation technology is a lot more costly than detection technology because of its complexity and employment of human experts, we examine a setting where Assumption 2 is satisfied. This is a technical assumption that makes the incentive problem of inducing the high investigation technology more severe than inducing the high detection technology. We refer to this assumption as the cost of investigation being much greater than the cost of detection.

We provide a technical observation on the ordering of qualities/precision of the technologies relative to each other that will ensure the existence of a solution to Program 1.

<sup>Observation</sup> <sup>1.</sup> Assumption A1 implies the following.

(a) The precision of the investigation technology is greater than the precision of the verification technology, $\mathrm { i . e . , }$ technically $\dot { q } _ { k } ^ { S 2 } > q _ { j } ^ { A }$

(b) The proportion of right-to-wrong classifications of valid clicks by the detection technology should be moderate, i.e., technically

$$
\frac {q _ {H} ^ {A}}{(1 - q _ {H} ^ {A})} <   \frac {\alpha q _ {H} ^ {S 1}}{(1 - \alpha) (1 - q _ {H} ^ {S 1})} <   \frac {q _ {H} ^ {S 2}}{(1 - q _ {H} ^ {S 2})}.
$$

(c) The investigation probability decreases as an advertiser’s verification technology increases, i.e., technically $d I _ { i j } ^ { S 2 } / d q _ { j } ^ { A } < 0$

Observation 1(a) implies that the investigation technology is more precise than the verification technology. Intuitively speaking, if this was not true, then the investigation technology would not be effective in resolving the conflicts between the advertiser and the SP. Observation 1(b) provides bounds for the precision of the detection technology and specifically implies that the signal-to-noise ratio of the detection technology should be moderate. Furthermore, it requires that the precision of an advertiser’s verification technology not be too high and the precision of the $\mathrm { S P ^ { \prime } s }$ investigation technology be sufficiently large. Intuitively, the SP would have no incentive to choose the more productive high investigation technology if the advertiser’s verification technology is already very effective/precise. Similarly, the advertiser would lack an incentive to choose the high verification technology if the investigation technology is not good enough in resolving the conflicts between the advertiser and the SP.

Observation 1(c) implies that a better verification technology can help decrease the probability that a click is investigated and hence increase the $\mathrm { { S P ^ { \prime } s } }$ profit. This happens because given that the $\mathrm { S P ^ { \prime } s }$ detection technology is moderately good (Observation 1(b)), not many clicks will be misclassified by the detection system and hence a better verification technology will generate less contestable clicks and reduce the need for investigation. Since the SP will benefit from less investigation, this provides a rationale for why the SP may want to induce the advertiser to choose the high verification technology.

## 4.1. Results

We characterize the solution to Program 1 in Proposition 1. Our analysis focuses on the parameter region where the advertiser and the SP are induced to choose their respective high technologies. All proofs are presented in Online Appendix A.

<sup>Proposition</sup> <sup>1.</sup> When the cost of the high investigation technology is (not) sufficiently large compared with the cost of the high verification technology then the incentive problem of inducing the high investigation technology is more (less) severe than the incentive problem of inducing the high verification technology. Technically, if condition (C1) is satisfied then constraint (ICS2) is binding, and if condition (C1) is not satisfied then constraint (ICC) is binding, where condition (C1) is given by

$$
C _ {H} ^ {S 2} / C _ {H} ^ {A} > \{T _ {H H H} - T _ {H H L} \} / \{T _ {H L H} - T _ {H H H} \}.\tag{C1}
$$

In particular,

(a) $i f$ condition (C1) is satisfied, the solution is

$$
\begin{array}{r l} & {\theta^ {*} = C _ {H} ^ {S 2} / (T _ {H H H} - T _ {H H L}),} \\ & {U ^ {*} = \gamma \alpha - \theta^ {*} T _ {H H H} - C _ {H} ^ {A} - m ^ {A} I _ {H} ^ {A},} \\ & {V ^ {*} = \theta^ {*} T _ {H H H} - C _ {H} ^ {S 1} - C _ {H} ^ {S 2} - m ^ {S 1} - m ^ {S 2} I _ {H H} ^ {S 2}.} \end{array}
$$

(b) If condition (C1) is not satisfied, the solution is

$$
\begin{array}{r l} & {\theta^ {* *} = C _ {H} ^ {A} / (T _ {H L H} - T _ {H H H}),} \\ & {U ^ {* *} = \gamma \alpha - \theta^ {* *} T _ {H H H} - C _ {H} ^ {A} - m ^ {A} I _ {H} ^ {A},} \\ & {V ^ {* *} = \theta^ {* *} T _ {H H H} - C _ {H} ^ {S 1} - C _ {H} ^ {S 2} - m ^ {S 1} - m ^ {S 2} I _ {H H} ^ {S 2}.} \end{array}
$$

Proposition 1 characterizes the solution to Program 1. The solution is determined by condition (C1). In simple terms, if the cost of the investigation is sufficiently high, then condition (C1) is satisfied and the incentive problem of inducing the $\mathrm { S P ^ { \prime } s }$ high investigation technology is most severe (in §1 we refer to this as the $\mathrm { S P ^ { \prime } s }$ investigation technology being the weakest link); and on the other hand, if the cost of the investigation technology is not high, then condition (C1) is not satisfied and the incentive problem of inducing the advertiser $' _ { \mathrm { { S } } }$ high verification technology is most severe, $\mathrm { i . e . , }$ the verification technology is the weakest link. This is standard in binary action double moral hazard problems, $\mathrm { i . e . , }$ one party’s agency problem is more severe than the other’s (see Jayanth et al. 2011, Arya et al. 2007).

In a normative sense, the important takeaway from Proposition 1 is that the advertiser should consider this incentive problem even when considering his auction bids in an auction-based PPC model: if the bids are not incentive compatible, i.e., they do not satisfy the constraints in Program 1, then the SP may not have an incentive to detect fraudulent clicks.

## 4.2. The Possibility of Unilateral Improvements in Technologies

We examine our main research question of whether the incentive compatible PPC given by Propositions 1(a) and 1(b) is adequate to induce further improvements to the precision of the high technologies. Specifically, we examine how the profits of the advertiser and the SP change when each of the high technologies is improved: will the SP improve the detection and investigation technologies and improve his profits? Similarly, will the advertiser improve the verification technology and improve his profits? If these questions are answered in the affirmative, then PPC provides adequate incentives for the two parties to make improvements to their respective technologies in addition to being incentive compatible for the double moral hazard problem. For example, consider the unilateral improvements to detection technology by the SP. The SP can choose to improve the detection technology from $q _ { H } ^ { S 1 }$ to $q _ { H } ^ { S 1 } + \varepsilon ^ { S 1 }$ where $\varepsilon ^ { S 1 } > 0$ 0 The question is that given this possibility, will the resulting $\dot { \mathrm { P P C } } , \mathrm { i . e . } , \theta ( q _ { H } ^ { S 1 } + \varepsilon ^ { S 1 } )$ , be such that the $\mathrm { S P ^ { \prime } s }$ profit of $V ( q _ { H } ^ { S 1 } + \varepsilon ^ { S 1 } )$ will be greater than $V ( q _ { H } ^ { S 1 } )$ . This is akin to evaluating the derivative of $V ( \dot { q } _ { H } ^ { S 1 } + \varepsilon ^ { S 1 } )$ with respect to $\varepsilon ^ { S 1 }$ at $\varepsilon ^ { S 1 } = 0 ,$ , or equivalently performing a comparative static analysis of $\dot { V } ( q _ { H } ^ { S 1 } )$ with respect to $\overset { \sim } { q _ { H } ^ { S 1 } }$ . This is essentially our notion of the PPC model providing the SP with adequate incentives to unilaterally improve the detection technology. For this purpose, we allow for the costs of the technologies to be constant (see the discussion in §1).

Before proceeding to examine this research question, we make some key observations about how improvements in the precision of one technology would affect the effectiveness of other technologies. Note that it is the effectiveness of the technologies that drives the equilibrium, i.e., solution to Program 1. The set of observations provided below, which follow from the laws of conditional probabilities, will be useful to understand the force/intuition for the later propositions.

<sup>Observation</sup> <sup>2.</sup> The effectiveness of the investigation technology, i.e., the difference in the payment probabilities across high and low investigation technologies, (a) increases with improvements in the precision of detection technology, and (b) decreases with improvements in the precision of verification technology. Technically, (a) $\dot { d } T _ { i j H } - T _ { i j L } / d q _ { i } ^ { S 1 } > 0 .$ , and (b) $d T _ { i j H } ^ {  } - T _ { i j L } /$ $d q _ { j } ^ { A } < 0$

Observation 2(a) shows that the effectiveness of the investigation technology increases with improvements in the precision of the detection technology, and shows a level of substitutability across the detection and investigation technologies that the $\mathrm { S P }$ chooses.<sup>11</sup> Observation 2(b) shows that improvements in the advertiser’s verification technology decrease the effectiveness of the investigation technology; intuitively, when the advertiser does a good job in catching fraudulent clicks, the SP does not need to work hard with the investigation technology. Note that given that the effectiveness of the investigation technology determines the severity of the SP’s incentive problem with respect to the investigation technology, improvements to the precision of the detection (verification) technology will mitigate (exacerbate) the $\mathrm { S P ^ { \prime } s }$ incentive problem, and thus could decrease (increase) the PPC needed to induce the high investigation technology.

<sup>Observation</sup> <sup>3.</sup> The effectiveness of the verification technology, i.e., the difference in the payment probabilities across low and high verification technologies, (a) decreases with improvements in the precision of detection technology, and (b) increases with improvements in the precision of investigation technology. Technically, (a) $d T _ { i L k } - T _ { i H k } / d q _ { i } ^ { S 1 } < \breve { 0 } _ { \cdot }$ , and (b) $d T _ { i L k } - \stackrel { \cdot } { T } _ { i H k } / d q _ { k } ^ { S 2 } > 0 .$

Observation 3(a) shows that the effectiveness of the verification technology decreases with the improvements to the detection technology; intuitively, when the detection technology is sufficiently precise, the advertiser does not need to work too hard. Observation 3(b) shows that an improvement in investigation technology increases the effectiveness of the verification technology. When the advertiser knows that the investigation technology will make more precise classifications, he will have more incentives to use the high verification technology to identify the invalid clicks and fight/contend the detection technology, knowing that the ultimate resolution will be a better classification.

Overall, the properties highlighted in Observations 2 and 3 show the conflict between the advertiser and the SP, and how the improvements to technologies help mitigate/exacerbate the incentive problem with respect to their choices.

4.2.1. The Possibility of the SP Unilaterally Improving the Investigation Technology. Like computer viruses, new click fraud attacks frequently arise and become more sophisticated because of a new development—see Leyden (2009) and Perez and Menezes (2009) for examples. As a result, investigation technology has evolved to a large infrastructure that consists of “several inspection systems” and a group of click quality investigators (Tuzhilin 2006). The SP can improve the high investigation technology either by enhancing the protocols used to investigate the advertisers’ inquiries or by investing in training human experts to keep them abreast of new click fraud activities. In addition, the SP can achieve this by not only studying visitors’ activities before the clicks (Clicklab 2006) but also incorporating the advertiser-side click data (Schwarz 2008). For example, Click Forensics allows advertisers to securely share relevant information such as advertiser-side click data, $\mathrm { e . g . , }$ advertisers’ server logs, with Yahoo! (Olsen 2008). We first examine the impact of improvements in high investigation technology $( q _ { H } ^ { S 2 } )$ and the result is summarized in the following proposition.

<sup>Proposition</sup> <sup>2.</sup> (i) As the precision of the high investigation technology $( q _ { H } ^ { S 2 } )$ improves, the $P P C \ ( \theta )$ decreases, the SP’s profit 4V 5 decreases, and the advertiser’s profit 4U 5 increases. Technically, $d \theta ^ { * } / d q _ { H } ^ { S 2 } < 0 , d V ^ { * } / d q _ { H } ^ { S 2 } < 0 ,$ $\nonumber { d \bar { U } ^ { * } / d q _ { H } ^ { S 2 } > 0 ; d \theta ^ { * * } / d q _ { H } ^ { S 2 } < 0 , \stackrel { . } { d } V ^ { * * } / d q _ { H } ^ { \dot { S } \dot { 2 } } < 0 , d U ^ { * * } / d \stackrel { . . . } { q } _ { H } ^ { \dot { S } 2 } > 0 . }$

(ii) The SP will not improve the precision of the high investigation technology unilaterally.

Proposition 2 shows that irrespective of whether the advertiser’s or the $\mathrm { S P ^ { \prime } s }$ incentive problem is more severe, i.e., whether condition (C1) is satisfied or not, the SP has no incentive to improve the high investigation technology. First, consider the case where the cost of the high investigation technology is sufficiently large, $\mathrm { i . e . }$ , the PPC needs to be high enough to induce the SP’s high investigation technology (the weakest link). Improvements in the high investigation technology increase the effectiveness of the investigation technology (Assumption A1(b)), which in turn leads to a less severe agency problem and lowers the PPC. In effect, such an improvement makes the investigation technology a less weak link and thus lowers the PPC, which will reduce the $\mathrm { S P ^ { \prime } s }$ expected profit. Hence, the SP will not find it beneficial to improve the high investigation technology.

More interestingly, even when the cost of the high investigation technology is not too large, i.e., the advertiser’s incentive problem is most severe, the SP still does not find it beneficial to improve the precision of the high investigation technology. Note that in this case the PPC needs to be high enough to induce the high verification technology (the weakest link), and thus the high investigation technology is obtained for “free,” and it could appear that improvements in investigation technology can benefit the SP. However, this seemingly counterintuitive result occurs because of the interaction between the high investigation and verification technologies with respect to the payment probability. Specifically, the laws of probability dictate that improvements in the high investigation technology make the verification technology more effective (see Observation 3(b)). Hence, when the advertiser knows that investigation technology is going to yield more precise classifications, he will have more incentives to use the high verification technology to fight/contend the SPs detection technology, knowing that the ultimate resolution will be a better classification. This automatically reduces the severity of the agency problem with respect to the verification technology and thus results in a lower PPC, which in turn reduces the $\mathrm { S P ^ { \prime } s }$ profits. Overall, the SP will not have an incentive to improve the high investigation technology, which is summarized in Proposition 2(ii).

4.2.2. The Possibility of Unilaterally Improving the Detection and Verification Technologies. The SP can improve the detection technology by incorporating additional techniques into click fraud detection or by actively monitoring new click fraud activities and developing online filters to detect them. For example, as Tuzhilin (2006) suggests, in addition to the rulebased and anomaly based approaches, Google can also develop classifier-based filters based on well-known data mining methods to improve the performance of online filters. Similarly, the advertiser can improve the precision of verification technology by collecting more data from sources other than that on the advertiser’s website and then conducting experiments on the data to tune parameters for the verification technology (Daswani et al. 2008).

We first consider the case where the SP’s high investigation technology is not very costly, i.e., the advertiser’s incentive problem is more severe (condition (C1) is not satisfied). The result is summarized in the following proposition.

<sup>Proposition</sup> <sup>3.</sup> When the advertiser’s incentive problem is more severe, i.e., $C _ { H } ^ { S 2 }$ is not large, we have the following:

(i) As the precision of the high detection technology 4q<sup>S1</sup>5 improves, the PPC (5 increases, the SP’s profit (V 5 increases, and the advertiser’s profit (U 5 decreases. Technically, $d \theta ^ { * * } / d q _ { H } ^ { S 1 } > 0 , d V ^ { * * } / d q _ { H } ^ { \dot { S } 1 } > 0 , d U ^ { * * } / d q _ { H } ^ { S 1 } < 0 .$

(ii) As the precision of the high verification technology (q<sup>A</sup>) improves, the PPC (5 decreases, the SP’s profit (V 5 decreases, and the advertiser’s profit (U 5 increases. Technically, $d \theta ^ { * * } / d q _ { H } ^ { A } < 0 , d V ^ { * * } / d q _ { H } ^ { A ^ { * } } < \stackrel { . } { 0 } , d U ^ { * * } / d q _ { H } ^ { A } > 0$

(iii) The SP will improve the precision of the high detection technology unilaterally, and likewise, the advertiser will improve the precision of the high verification technology unilaterally.

Proposition 3(i) shows that when the advertiser’s incentive problem is more severe, PPC increases with improvements in the high detection technology. Note that the PPC is determined by the incentive constraint with respect to the verification technology (the weakest link), which is a “fighting” technology that creates disagreements between the advertiser and the SP. As the high detection technology improves, the advertiser’s need to “fight” with the detection technology decreases. Intuitively, when the SP’s detection technology is sufficiently good in catching the invalid clicks, the advertiser has less incentive to work hard. Hence, improving $\mathrm { S P ^ { \prime } s }$ detection technology reduces the advertiser’s benefits from choosing the high verification technology and decreases the effectiveness of the verification technology (see Observation 3(a)). This leads to a more severe agency problem that requires a higher PPC to induce the advertiser to choose the improved high verification technology. Corresponding to the increase in PPC, the $\mathrm { S P ^ { \prime } s }$ profit increases with improvements in the high detection technology. In summary, we show that contrary to a naïve belief that the SP will not always have an incentive to fight click fraud, he could improve his profits from improving the detection technology because doing so exacerbates the advertiser’s incentive problem, which leads to a higher PPC.

Proposition 3(ii) shows that when the advertiser’s incentive problem is more severe, the PPC decreases as the precision of the high verification technology improves. Improvement in the high verification technology makes it more “attractive” than the low verification technology to the advertiser and hence increases the effectiveness of the verification technology (Assumption A1(c)), which in turn reduces the severity of the advertiser’s agency problem and decreases the PPC. The lower PPC will increase the advertiser’s expected profit and thus the advertiser will find it beneficial to improve the high verification technology. Overall, Proposition 3(iii) summarizes the results of Propositions 3(i) and 3(ii).

Next, we examine the impact of improving the high detection and verification technologies for settings where the high investigation technology is sufficiently costly and the SP’s incentive problem is more severe (condition (C1) is satisfied). The result is summarized in the following proposition.

<sup>Proposition</sup> <sup>4.</sup> When the SP’s incentive problem is more severe, $i . e . , \ C _ { H } ^ { S 2 }$ is sufficiently large, we have the following:

(i) As the precision of the high detection technology $( q _ { H } ^ { S 1 } )$ improves, the PPC (5 decreases, the SP’s profit (V 5 decreases, and the advertiser’s profit (U 5 increases. Technically, $d \theta ^ { * } / d q _ { H } ^ { S 1 } < 0 , d V ^ { * } / d q _ { H } ^ { S 1 } \dot { < } \dot { 0 } , d \dot { U } ^ { * } / d q _ { H } ^ { S 1 } > 0$

(ii) As the precision of the high verification technology $( q _ { H } ^ { A } )$ improves, the PPC (5 increases, the SP’s profit (V 5 increases, and the advertiser’s profit (U 5 decreases. Techni cally, $d \theta ^ { * } / d q _ { H } ^ { A } > 0 , d V ^ { * } / d q _ { H } ^ { A } > 0 , d U ^ { * } / d q _ { H } ^ { A } < 0 .$

(iii) The SP will not improve the precision of the high detection technology unilaterally, and likewise, the advertiser will not improve the precision of the high verification technology unilaterally.

(iv) The dominant strategy for the SP and the advertiser is no improvement to the precision of the high detection and verification technologies, respectively.

(v) When the SP and the advertiser simultaneously improve the precision of their high detection and verification technologies, respectively, in a coordinated fashion, this could increase not only the social welfare but also the profits of both the SP and the advertiser if the precision of the advertiser’s verification technology is sufficiently high.

Proposition 4(i) shows that when the SP’s incentive problem is more severe, i.e., the PPC is determined by the incentive constraint with respect to the $\mathrm { S P ^ { \prime } s }$ investigation technology (the weakest link), the PPC decreases with improvements in the high detection technology. This occurs because improving the high detection technology helps increase the effectiveness of $\mathrm { S P ^ { \prime } s }$ investigation technology (see Observation $2 ( \mathsf { a } ) )$ , and hence reduces the severity of the agency problem with respect to the investigation technology. Thus, a lower PPC is sufficient to induce the SP to choose the high investigation technology as the detection technology is improved, which in turn reduces the $\mathrm { S P ^ { \prime } s }$ expected profit. This could explain the $\mathrm { S P ^ { \prime } s }$ reluctance to improve the detection technology.

On the other hand, the PPC increases if the advertiser improves the high verification technology, as shown in Proposition 4(ii). Intuitively, when the advertiser does a good job in catching fraudulent clicks, the SP has less incentive to work hard with the investigation technology (see Observation 2(b)). This exacerbates the severity of the agency problem with respect to the SP’s investigation technology and thus results in a higher PPC, which in turn reduces the advertiser’s expected profits. The important message here is that although it could appear that the advertiser would be more interested in catching fraud clicks, he may not always be better off by improving the verification technology. Overall, Proposition 4(iii) summarizes the results of Propositions 4(i) and 4(ii).

Propositions 4(iv) and 4(v) show that the SP and the advertiser essentially face the classic prisoner’s dilemma outcome in a noncooperative game. Proposition 4(iv) directly arises from Proposition 4(iii): the PPC cannot induce both parties to make improvements in their respective technologies, unilaterally, i.e., in a noncooperative setting—an impossibility result. However, Proposition $4 ( \mathbf { v } )$ shows that, if there is a coordination mechanism that helps the players coordinate and enforces nondeviations from the improvements through appropriate penalties, not only may the social welfare increase, each player may also be able to increase his respective profits if the advertiser’s verification technology is sufficiently good.

The result on social welfare has implications to the next question of whether other mechanisms can help both the SP and the advertiser in making improvements to their respective technologies. For example, if the social welfare increases with improvements in detection and verification technologies, then there is a potential for designing coordination mechanisms; if, however, the social welfare does not increase, then looking for coordination mechanisms will be moot. The total expected profits for the SP and the advertiser is given by the following:

$$
\begin{array}{r} S W = U + V = \gamma \alpha - C _ {H} ^ {S 1} - C _ {H} ^ {S 2} - C _ {H} ^ {A} \\ - m ^ {S 1} - m ^ {A} I _ {H} ^ {A} - m ^ {S 2} I _ {H H} ^ {S 2}. \end{array}\tag{SW}
$$

Equation (SW) shows an important feature of the double moral hazard model in the click fraud setting. The detection, verification, and investigation technologies affect the social welfare only through the increased/ decreased costs of conducting the classification of clicks later in the sequence. There is no productive effect in the sense that the expected benefit (5 is improved. It can be verified that the social welfare increases as the precision of the advertiser’s high verification technology improves, i.e., $d S W / d q _ { H } ^ { A } > 0 ,$ , because such improvements help to save investigation costs (see Observation 1(c)). Similarly, the social welfare increases as the precision of the $\dot { \mathrm { S P ^ { \prime } s } }$ high detection technology improves, if the precision of the advertiser’s high verification is sufficiently high, i.e., $d S W / d q _ { H } ^ { S 1 } > 0$ if $q _ { H } ^ { A } > \alpha + [ m ^ { A } ( 2 \alpha - 1 ) / m ^ { S 2 } ] ^ { - }$ These results follow directly from the intuition embedded in Proposition $4 ( \mathrm { v } ) . ^ { 1 2 }$

## 4.3. Illustrating Proposition 4

We present a numerical example to highlight the result in Proposition 4. For this purpose, we use the following parameter values: $\alpha = 0 . { \dot { 6 2 } } , { \dot { \gamma = 8 0 } } , q _ { H } ^ { S 2 } = 0 . 9 9 , q _ { H } ^ { A } = 0 . 6 9 ,$ $\dot { \phi } ^ { S 1 } = 0 . 8 5 , ~ \phi ^ { A } = 0 . 8 8 , ~ \phi ^ { S 2 } = 1 . 1 0 , ~ \dot { q } _ { I . } ^ { \dot { S } \dot { 1 } } = 0 . 6 3 , ~ \dot { q } _ { I . } ^ { \ddot { A } } = 0 . 5 3 ,$ $q _ { L } ^ { S 2 } = 0 . 7 8 , C _ { H } ^ { S 1 } = 0 . 3 8 , C _ { H } ^ { A } = 0 . 2 5 , C _ { H } ^ { \overleftarrow { S 2 } } = 0 . 6 0 , \overleftarrow { C _ { L } ^ { \overleftarrow { S 1 } } } = 0 . 2 5 ,$ $\overleftarrow { C } _ { L } ^ { S 2 } = 0 . 4 0 , \ \mathring { C } _ { L } ^ { A } = 0 , m ^ { S 1 } \overset {  } { = } m ^ { A } = 0 , \ \mathring { m } ^ { S 2 } = 2 0$ , and $\bar { V } = 0 .$ The costs of the high technologies appear to be small, because even though the technology costs are large, given that the number of clicks is in the billions, the cost per click is small. We let the unit cost for clicks classified by the $\mathrm { S P ^ { \prime } s }$ detection technology and the advertiser’s verification technology be zero, because these two technologies commonly use automated programs to classify clicks and hence the unit cost of classifying a click can be negligible. Nevertheless, the $\mathrm { S P ^ { \prime } s }$ investigation technology requires careful examinations by human experts, so the unit cost of classifying a click by the investigation technology is usually $\mathrm { \ h i g h . ^ { 1 3 } }$

Table 2 provides the ${ \mathrm { P P C } } ,$ the advertiser’s, and the $\mathrm { S P ^ { \prime } s }$ profits for varying values of the high detection technology precisions $( q _ { H } ^ { S 1 } )$ . Clearly, the PPC and $\mathrm { S P ^ { \prime } s }$ profits decrease as the high detection precision is improved. This illustrates that the SP will not have the incentive to improve the high detection technology unilaterally in this case.

Table 2 Numerical Example to Illustrate Proposition 4

<table><tr><td colspan="4">Effect of high detection technology</td></tr><tr><td> $q_{H}^{S1}$ </td><td>θ</td><td>V</td><td>U</td></tr><tr><td>0.690</td><td>34.4221</td><td>10.9718</td><td>32.8376</td></tr><tr><td>0.694</td><td>32.5050</td><td>10.1187</td><td>33.6911</td></tr><tr><td>0.698</td><td>30.7903</td><td>9.3556</td><td>34.4545</td></tr><tr><td>0.702</td><td>29.2473</td><td>8.6690</td><td>35.1414</td></tr><tr><td>0.706</td><td>27.8517</td><td>8.0479</td><td>35.7628</td></tr><tr><td>0.710</td><td>26.5831</td><td>7.4835</td><td>36.3275</td></tr><tr><td>0.714</td><td>25.4251</td><td>6.9682</td><td>36.8431</td></tr></table>

Note. Parameter values:  = 0062,  = 80, q<sup>S2</sup> = 0099, q<sup>A</sup> = 0069, <sup>S1</sup> = 0085, <sup>A</sup> = 0088, <sup>S2</sup> = 1010, q<sup>S1</sup> = 0063, q<sup>A</sup> = 0053, q<sup>S2</sup> = 0078, $\dot { C } _ { H } ^ { S 1 } = 0 . 3 8 ,$ $C _ { H } ^ { A } = 0 . 2 5 , \underline { { C } } _ { H } ^ { S 2 } = 0 . 6 0 , C _ { L } ^ { S 1 } = 0 . 2 5 , C _ { L } ^ { S 2 } = 0 . 4 0 , C _ { L } ^ { A } = 0 , m ^ { S 1 } = m ^ { \dot { A } } = 0 ,$ , and $m ^ { S 2 } = 2 0 , \bar { V } = 0 .$

To illustrate Propositions 4(iv) and 4(v), we use the value for the high detection (verification) technology at $q _ { H } ^ { S 1 } = 0 . 7 0 ~ ( q _ { H } ^ { A } = 0 . 6 9 )$ as the starting point and consider improvements resulting in the following: $q _ { H } ^ { S 1 } = 0 . 7 1$ $( q _ { H } ^ { \bar { A } } = 0 . 6 9 6 4 )$ . Table 3 illustrates the strategies by both players and their corresponding payoffs. Examining the advertiser’s payoffs reveals that regardless of what action the SP takes, the advertiser is always better off by not improving his current high verification technology. Specifically, if the SP chooses not to improve the current detection technology (chooses $q _ { H } ^ { S 1 } \stackrel {  } { = } 0 . 7 0 )$ , then the advertiser is better off by keeping the verification precision at $q _ { H } ^ { A } = 0 . 6 9 , \mathrm { i . e . , } U ( q _ { H } ^ { \bar { A } } = \bar { 0 } . 6 9 ) = 3 4 . 8 0 6 8 >$ $U ( q _ { H } ^ { A } = 0 . 6 9 6 4 ) = 3 2 . 9 0 1 2$ . If the SP chooses to improve the detection precision up to $q _ { H } ^ { S 1 } = 0 . 7 1$ , the advertiser is still better off with his current precision at $q _ { H } ^ { A } = 0 . 6 9$ even though the high detection technology is improved, $\mathrm { i . e . , } U ( q _ { H } ^ { A } = 0 . 6 9 ) { \stackrel { \smile } { = } } 3 6 . 3 2 7 5 > U ( q _ { H } ^ { A } = 0 . { \stackrel { \smile } { 6 9 } } 6 4 ) = { \dot { 3 } } 4 . 8 3 1 4$ Hence, the advertiser’s dominant strategy is not to improve the high verification technology.

Similarly, the SP has no incentive to improve the current high detection technology, regardless of the advertiser’s strategy. In particular, if the advertiser keeps the high verification precision at $q _ { H } ^ { A } = 0 . 6 9 .$ , the SP will be worse off with improvements in the high detection technology, i.e., $V ( q _ { H } ^ { \mathsf { S 1 } } = 0 . 7 1 ) = 7 . 4 8 3 5 < V ( q _ { H } ^ { S 1 } = 0 . 7 0 ) =$ 900034. If the advertiser improves the verification technology to $q _ { H } ^ { A } = 0 . 6 9 6 4$ , then the SP would still be worse off with improving the high detection technology, i.e., $V ( q _ { H } ^ { S 1 } = 0 . 7 \dot { 1 } ) = 9 . 0 \dot { 1 } 9 0 < \check { V ( } q _ { H } ^ { S 1 } = 0 . 7 0 ) = 1 0 . 9 4 7 3$ . Thus, the SP’s dominant strategy is also not to improve his detection technology. Overall, keeping the current verification and detection precisions at $q _ { H } ^ { A } = 0 . 6 9$ and $q _ { H } ^ { S 1 } = 0 . 7 0$ are the dominant strategies for both players, and in equilibrium, the advertiser receives $U = { \hat { 3 } } 4 . { \dot { 8 } } 0 6 8$ and the SP receives $V = 9 . 0 0 3 4$

Table 3 Payoffs to Players in the Coordination Example

<table><tr><td rowspan="2"></td><td colspan="3">SP</td></tr><tr><td></td><td> $q_{H}^{S1}=0.70$ </td><td> $q_{H}^{S1}=0.71$ </td></tr><tr><td rowspan="2">Advertiser</td><td> $q_{H}^{4}=0.69$ </td><td>34.8068, 9.0034</td><td>36.3275, 7.4835</td></tr><tr><td> $q_{H}^{4}=0.6964$ </td><td>32.9012, 10.9473</td><td>34.8314, 9.0190</td></tr></table>

Note. Payoffs to: (Advertiser, SP).

Nevertheless, if both parties can coordinate through some verifiable mechanisms such as a third-party audit, they can both be better off by improving their technologies simultaneously. In this example, if both improve the precision of the high detection and verification technologies, then the advertiser’s profit increases to $U = 3 4 . 8 \bar { 3 } 1 4$ instead of $U = 3 4 . 8 0 6 8$ and the SP’s profit improves to $V { = } 9 . 0 1 9 0$ instead of $V = 9 . 0 0 3 4$ . These increases in payoffs are the increases in return on investments.

## 5. A Mechanism to Mitigate the Result in Proposition 4

Our result shows that even though the PPC is incentive compatible and solves the moral hazard problem, it does not induce the SP and the advertiser to make improvements to their respective technologies in a noncooperative setting. Note that the latter is a problem that the PPC is not designed to solve, and thus it is not surprising that the PPC fails to solve that problem. We consider a common arrangement that we observe in practice—a third party is engaged to do the investigation in the third stage (Gaustella 2007).<sup>14</sup> In particular, the disagreements in the $\mathrm { S P ^ { \prime } s }$ and advertiser’s classification of invalid clicks are resolved by a neutral third party (instead of the SP). Furthermore, as shown in Proposition 2 the SP does not have an incentive to improve the investigation technology—as such, we examine whether removing the two-action SP problem is effective in making the PPC solve both the moral hazard problem as well as the unilateral improvement problem.

Since the third party is a neutral party, the investigation technology is not subject to moral hazard in the sense that both the SP and the advertiser are aware of the technology. Thus, the precision of the investigation technology used by the third party (q<sup>I</sup> 5, unlike the detection precision and the verification precision that are not observable or contractible, is common knowledge to both players.<sup>15</sup> That is, the investigation technology correctly classifies a truly valid contestable click as valid with probability $q ^ { I }$ and this is observable/known by both parties. As earlier, we assume the investigation technology is more informative than the detection and verification technologies, i.e., $q ^ { I } > \{ q _ { i } ^ { S } , q _ { j } ^ { A } \}$ . Note that we use S (not S15 as the superscript for parameters related to the $\mathrm { S P ^ { \prime } s }$ detection technology in this extension.

The probability that a click is paid for is given by

$$
T _ {i j} = \alpha q _ {i} ^ {S} [ q ^ {I} + q _ {j} ^ {A} (1 - q ^ {I}) ] + (1 - \alpha) (1 - q _ {i} ^ {S}) (1 - q _ {j} ^ {A} q ^ {I}).
$$

The probability that a click is inspected by the third party (i.e., the $\bar { \mathsf { S P } }$ classifies it as valid but the advertiser disagrees) is given by

$$
I _ {i j} ^ {I} = \alpha q _ {i} ^ {S} (1 - q _ {j} ^ {A}) + (1 - \alpha) (1 - q _ {i} ^ {S}) q _ {j} ^ {A}.
$$

The third party charges a unit cost $m ^ { I }$ for each click investigated. We consider two regimes for how the investigation cost is paid. First, we consider a regime where the cost is paid by the SP, i.e., the SP-pay regime; the SP pays because the third-party substitutes for the $\mathrm { S P ^ { \prime } s } ^ { - }$ third-stage classification technology. Second, we consider a regime where the cost is paid by the advertiser, i.e., advertiser-pay regime; the advertiser pays because it is in his self-interest to contest clicks. The expected profit for the advertiser 4U 5 and SP 4V 5 for $i , j \in \{ H , L \}$ under the payment regime $k \in \{ A , S \}$ is given by

$$
U _ {i j} ^ {k} = \gamma \alpha - \theta T _ {i j} - C _ {j} ^ {A} - m ^ {A} I _ {i} ^ {A} - D m ^ {I} I _ {i j} ^ {I},
$$

and

$$
V _ {i j} ^ {k} = \theta T _ {i j} - C _ {i} ^ {S} - m ^ {S} - (1 - D) m ^ {I} I _ {i j} ^ {I},
$$

respectively, with D being an indicator variable where D = 1 if $k = A$ (advertiser-pay regime) and $D = 0$ if k = S (SP-pay regime) otherwise.

The advertiser’s problem is provided in the following program for $k \in \{ A , S \}$ . Since we examine the incentives for supporting further unilateral improvements, we focus on the case where both the $\mathrm { S \hat { P } }$ and advertiser choose their respective high technologies. For simplicity, we set $m ^ { S } = m ^ { \hat { A } } = 0$

Program 2

$$
\max _ {\theta} U _ {H H} ^ {k}\tag{OBJ-P2}
$$

$$
\text { subject   to } V _ {H H} ^ {k} \geq \bar {V} = 0,\tag{PCS-P2}
$$

$$
V _ {H H} ^ {k} \geq V _ {L H} ^ {k},\tag{ICS-P2}
$$

$$
U _ {H H} ^ {k} \geq U _ {H L} ^ {k}.\tag{ICC-P2}
$$

This represents a standard double moral hazard setting and differs from Program 1 in that the SP chooses one technology instead of two in sequence since the investigation is delegated to a neutral third party.

Next, we make some assumptions that are similar in spirit to Assumptions A1 and A2.

Assumption 3 (A3). <sub>(a)</sub> $T _ { H j } > T _ { L j } , ( { \bf b } ) T _ { i L } > T _ { i H } ,$ (c) $I _ { H j } ^ { I } < I _ { L j } ^ { I } ,$ and (d) $I _ { i H } ^ { I } < I _ { i L } ^ { I } f o r ^ { ' } i , j \in \{ \stackrel { I } { H } , L \}$

Assumption 3 is similar to the standard assumption in the moral hazard setting that requires high technology/action to be more productive than low technology/action. In particular, Assumptions A3(c) and $\mathrm { A } 3 ( \mathrm { d } )$ state that high technologies help reduce the investigation probability, which provides the players additional incentives to choose high technology over low technology in the third-party investigation mechanism.

Assumption 4 (A4).

$$
\begin{array}{r l} & {\mathrm{(a)} \max \bigg \{\frac {C _ {H} ^ {A} T _ {L L}}{(T _ {L L} - T _ {L H}) I _ {L L} ^ {I}}, \frac {C _ {H} ^ {A} (T _ {H L} - T _ {L L})}{(T _ {H L} - T _ {H H}) (I _ {H L} ^ {I} - I _ {L L} ^ {I})}} \\ & {\qquad - \left. \frac {C _ {H} ^ {S}}{(I _ {H L} ^ {I} - I _ {L L} ^ {I})} \right\} <   m ^ {I} <   \frac {C _ {H} ^ {A} T _ {H H}}{I _ {H H} ^ {I} (T _ {H L} - T _ {H H})} - \frac {C _ {H} ^ {S}}{I _ {H H} ^ {I}}} \end{array}
$$

and

$$
\begin{array}{r l} & {\mathrm{(b)} \frac {C _ {H} ^ {A} [ (T _ {H L} - T _ {L L}) I _ {H H} ^ {I} - T _ {H H} (I _ {H L} ^ {I} - I _ {L L} ^ {I}) ]}{(I _ {H H} ^ {I} - I _ {H L} ^ {I} + I _ {L L} ^ {I}) (T _ {H L} - T _ {H H})}} \\ & {\qquad <   C _ {H} ^ {S} <   \frac {C _ {H} ^ {A} (T _ {H L} I _ {L L} ^ {I} - T _ {L L} I _ {H L} ^ {I})}{I _ {L L} ^ {I} (T _ {H L} - T _ {H H})}.} \end{array}
$$

Assumption A4(a) is a sufficient condition for a solution to Program 2 in the SP-pay regime with a slack participation constraint. In particular, the assumption requires the cost of a third-party investigation to be moderate—the cost should not be too high otherwise the SP’s expected profit will not be positive; the cost should not be too low so as to create an incentive for the SP not to choose the high detection technology. To see the latter, suppose the cost of the third-party investigation is very low, then the SP will find it beneficial not to incur a large cost with the high detection technology, and instead let the relatively cheap investigation technology do the appropriate classifications. Furthermore, since we examine the SP’s and the advertiser’s incentive to improve their respective technologies, it is moot to examine the settings where low technologies are induced.

Technically, if the assumption is not satisfied, then the SP’s moral hazard will not be severe enough, and as such the participation constraint may be binding. This will imply that there is no moral hazard problem for the SP in the third-party investigation setting. When we compare the setting with the third-party investigation (Proposition 5) and the setting without the third party investigation (Proposition 4), clearly if the third party fully mitigates the moral hazard problem and thus helps to mitigate the unilateral improvements in the click fraud identification technologies, then it is an unfair comparison.<sup>16</sup> By making this assumption, we also ensure that the SP’s moral hazard problem exists in both settings and our comparison is fair. As such, our analysis focuses on the domain of the parameter space where the advertiser and the SP are induced to choose their respective high technologies. Assumption A4(b) requires the cost of the high detection technology to be moderate such that the region defined in Assumption $\mathtt { A 4 ( a ) }$ is nonempty and high technologies are induced.

Similarly, the following Assumption A5 is made for the advertiser-pay regime and it requires that the third-party investigation cost not be too high.

Assumption 5 (A5).

$$
\begin{array}{r l} & m ^ {I} <   \min \bigg \{\frac {C _ {H} ^ {A}}{(I _ {H L} ^ {I} - I _ {H H} ^ {I})} - \frac {C _ {H} ^ {S} (T _ {H L} - T _ {H H})}{(T _ {H H} - T _ {L H}) (I _ {H L} ^ {I} - I _ {H H} ^ {I})}, \\ & \frac {\alpha (1 - \alpha) [ (1 - q ^ {I}) + q ^ {I ^ {2}} ] C _ {H} ^ {A}}{T _ {H H} (T _ {H L} - T _ {H H}) + (I _ {H L} ^ {I} - I _ {H H} ^ {I}) \alpha (1 - \alpha) [ (1 - q ^ {I}) + q ^ {I ^ {2}} ]} \bigg \}. \end{array}
$$

We characterize the solution to Program 2 in Proposition 5.

<sup>Proposition</sup> <sup>5.</sup> (i) In the SP-pay regime, under Assumptions A3 and A4, the solution to Program 2 is

$$
\begin{array}{r} \theta^ {\#} = C _ {H} ^ {A} / (T _ {H L} - T _ {H H}), U ^ {\#} = \gamma \alpha - \theta^ {\#} T _ {H H} - C _ {H} ^ {A}, \\ V ^ {\#} = \theta^ {\#} T _ {H H} - C _ {H} ^ {S} - m ^ {I} I _ {H H} ^ {I}. \end{array}
$$

Both the advertiser and the SP have incentives to improve the precision of their respective high technologies unilaterally, $i . e . , \dot { d V ^ { \# } } / d q _ { H } ^ { S } > 0$ and $\dot { d U ^ { \# } } / d q _ { H } ^ { A } > 0$

(ii) In the advertiser-pay regime, under Assumptions A3 and A4, the solution to Program 2 is

$$
\begin{array}{r l} & {\theta^ {\# \#} = [ C _ {H} ^ {A} - m ^ {I} (I _ {H L} ^ {I} - I _ {H H} ^ {I}) ] / (T _ {H L} - T _ {H H}),} \\ & {U ^ {\# \#} = \gamma \alpha - \theta^ {\# \#} T _ {H H} - C _ {H} ^ {A} - m ^ {I} I _ {H H} ^ {I},} \\ & {V ^ {\# \#} = \theta^ {\# \#} T _ {H H} - C _ {H} ^ {S}.} \end{array}
$$

Both the advertiser and the SP have incentives to improve the precision of their respective high technologies unilaterally, $i . e . , \dot { d } V ^ { \# \# } / d q _ { H } ^ { \bar { S } } > 0$ and $d U ^ { \# \# } / d \check { q } _ { H } ^ { A } > 0 .$

Essentially, when both parties choose high technologies and the cost of a third-party investigation is not very high, the PPC mitigates the problem of no unilateral improvements in the technologies, i.e., the result in Proposition 4. For the SP-pay regime, the intuition for why the mechanism works is that the SP finds it beneficial to improve the detection technology because doing so not only increases the PPC but also saves on the third-stage cost. Knowing that the SP has incentives to improve the detection technology, the advertiser in turn has an incentive to improve the verification technology so as to sustain the $\mathrm { S P ^ { \prime } s }$ improvement. Similarly, in the advertiser-pay regime, a better verification technology not only decreases the PPC but also reduces the need for a third-party investigation. Knowing that the advertiser has an incentive to improve the verification technology, the SP “fights” back by improving the detection technology because doing so exacerbates the advertiser’s incentive problem and increases the PPC. In effect, the delegation of the last stage of the classification technology to a third-party helps incentivize both the SP and the advertiser to improve their respective technologies and by doing so both of them benefit.

Table 4 Numerical Example for the SP-Pay Regime

<table><tr><td rowspan="2"></td><td colspan="3">SP</td></tr><tr><td></td><td> $q_{H}^{S}=0.70$ </td><td> $q_{H}^{S}=0.71$ </td></tr><tr><td rowspan="2">Advertiser</td><td> $q_{H}^{A}=0.69$ </td><td>44.0583, 0.3519</td><td>43.8822, 0.5289</td></tr><tr><td> $q_{H}^{A}=0.6964$ </td><td>44.2714, 0.1770</td><td>44.1021, 0.3483</td></tr></table>

Note. Payoffs to: (Advertiser, SP).

We illustrate in Table 4 a numerical example for a third-party investigation in the SP-pay regime using the same parameter values as in the earlier example. If the detection technology remains at $q _ { H } ^ { S } = 0 . 7 0$ , the advertiser is better off by improving the verification precision to $q _ { H } ^ { A } = 0 . 6 9 6 4 , \mathrm { i . e . } , U \dot { ( } q _ { H } ^ { A } = 0 . 6 9 6 4 ) = 4 4 . 2 7 1 4 >$ $\begin{array} { r } { \bar { U } ( q _ { H } ^ { A } = 0 . 6 9 ) = 4 4 . 0 5 8 3 . } \end{array}$ If the SP improves the detection precision up to $q _ { H } ^ { S } = 0 . 7 1$ , the advertiser is still better off with the improved precision, i.e., $U ( q _ { H } ^ { A } = 0 . 6 9 6 4 ) =$ 4401021 $> U ( q _ { H } ^ { \hat { A } } = 0 . 6 9 \hat { ) } = 4 3 . 8 8 2 2$ . Hence, the advertiser’s dominant strategy is to improve the high verification technology. Similarly, the SP also has an incentive to improve the high detection technology, regardless of the advertiser’s strategy. In particular, if the verification precision remains at $q _ { H } ^ { \bar { A } } = 0 . { \dot { 6 } } 9$ , the SP can increase his profit from 0.3519 to 0.5289 by improving the detection precision up to $q _ { H } ^ { S } = 0 . 7 1$ . If the verification precision improves to $q _ { H } ^ { A } = 0 . 6 9 6 4$ , the SP would still be better off with improving the high detection technology, i.e., $V ( q _ { H } ^ { S } = 0 . 7 \dot { 1 } ) = 0 . 3 \dot { 4 } 8 3 > V ( \stackrel { \sim } { q } _ { H } ^ { S } = 0 . 7 0 ) = 0 . 1 7 7 0 .$ . Thus, the SP’s dominant strategy is also to improve his detection technology. Overall, improving the current verification and detection precisions are the dominant strategies for both players even in a noncooperative setting, and in equilibrium, the advertiser receives $U = 4 4 . 1 0 \breve { 2 } 1$ and the SP receives $V = 0 . 3 4 8 3$

Table 5 shows a numerical example for the advertiserpay regime using the same parameter values except that $m ^ { \widetilde { I } } = 2 . 5$ . Specifically, if the detection precision is $q _ { H } ^ { S } = 0 . 7 0$ , the advertiser has an incentive to improve the verification technology, i.e., $U ( q _ { H } ^ { A } = 0 . 6 9 6 4 ) = \dot { 4 } 6 . 2 2 9 4 >$ $U ( q _ { H } ^ { A } = 0 . 6 9 ) = 4 6 . 0 \dot { 1 } 6 2$ . If the detection precision improves up to $q _ { H } ^ { S } = 0 . 7 1$ , the advertiser is better off with the improved technology, i.e., $U ( q _ { H } ^ { A } = 0 . 6 9 6 4 ) =$ $4 6 . 2 2 3 4 > \hat { U } ( q _ { H } ^ { A } = 0 . 6 9 ) = 4 6 . { \overset { \sim } { 0 } } 0 3 4$ . Hence, the advertiser’s dominant strategy is to improve the verification technology. Likewise, the $\mathrm { S P ^ { \prime } s }$ dominant strategy is to improve his detection technology. In particular, if the advertiser keeps the high verification precision at $q _ { H } ^ { A } = 0 . 6 9$ , the $\mathrm { S } \bar { \mathrm { P } } ^ { \prime } \mathrm { s }$ profit increases from 2.3838 to 2.3967 by improving the detection precision up to $q _ { H } ^ { S } = 0 . 7 \dot { 1 }$ . When the verification precision improves to $q _ { H } ^ { A } = 0 . 6 9 6 4$ , the SP would still be better off with improvements to the high detection technology, $\mathrm { i . e . , }$ $\dot { V ( q _ { H } ^ { S } = 0 . 7 1 ) } = 2 . 1 8 1 7 > \check { V } ( q _ { H } ^ { S } = 0 . 7 0 ) = 2 . 1 7 5 4$ . In equilibrium, the advertiser receives $U = 4 6 . 2 2 3 4$ and the SP receives $V = 2 . 1 8 1 7$

Table 5 Numerical Example for the Advertiser-Pay Regime 4m<sup>I</sup> = 2055

<table><tr><td rowspan="2"></td><td colspan="3">SP</td></tr><tr><td></td><td> $q_{H}^{S}=0.70$ </td><td> $q_{H}^{S}=0.71$ </td></tr><tr><td rowspan="2">Advertiser</td><td> $q_{H}^{A}=0.69$ </td><td>46.0162, 2.3838</td><td>46.0034, 2.3967</td></tr><tr><td> $q_{H}^{A}=0.6964$ </td><td>46.2294, 2.1754</td><td>46.2234, 2.1817</td></tr></table>

Note. Payoffs to: (Advertiser, SP).

## 6. Managerial Implications and Concluding Remarks

We examined a flat-rate PPC model and a three-stage click fraud identification process: (1) the SP first classifies clicks using a detection technology—the proactive system (Ghosemajumder 2007); (2) the advertiser does the same to those classified as valid by the $\mathrm { S P ^ { \prime } s }$ detection technology using a verification technology (Google 2014); (3) the SP examines the disagreements using an investigation technology—the reactive system (Ghosemajumder 2007). The choice of click fraud technologies are not observable and contractible and hence are subject to moral hazard.

The important managerial insight is to highlight that in the most likely setting of the cost of investigation technology being large, both the SP and the advertiser will not have an incentive under the PPC model to further improve the quality of their click fraud classification technologies. This could provide one rationale for why the undetected click fraud rates continue to be high and insights for managers to use other mechanisms. Accordingly, we examine one of the mechanisms that is recommended in the industry—third-party investigation, in which the third-stage resolution of disagreements is done by an independent third party and paid for either by the SP or the advertiser. Note that the double moral hazard problem continues to exist in this setting as well. We show that in spite of the double moral hazard problem, albeit with one unobservable choice by the SP instead of two, third-party investigation helps to not only make the flat rate PPC incentive compatible to induce the high detection and verification technologies but also provides incentives for each party to improve their respective technologies. This shows an indirect benefit of delegation of investigation to third parties, an arrangement that is increasingly espoused by the online advertising industry circles (Gaustella 2007, Vranica 2014).

The auction-based PPC model is another pricing model that is popular in online advertising. Clay (2011) compares the benefits of the flat-rate and auction-based $\mathrm { P P } \bar { \mathrm { C } }$ and concludes that advertisers who know their consumers better and have a large advertising budget would benefit from flat-rate $\mathrm { P P C s } ,$ whereas those who do not know much about their customers should use the auction PPC to learn about the keywords that are more appropriate for them. Even though our model considers a flat-rate PPC model, which is common in comparison shopping sites, the insight is applicable to the auction-based PPC model as well. The auctionbased PPC needs to solve the hidden information problem of the advertiser’s value of advertising as well as the double moral hazard problem of click fraud identification. Our model does not consider the hidden information problem. We implicitly assume that the PPC that is incentive compatible for the double moral hazard problem also solves the hidden information problem. In essence, if the auction-based PPC does not solve the double moral hazard problem, then clearly the auction-based PPC will not be able to provide adequate incentives to improve the identification technologies. As such, the additional insight in a normative sense is that auction-based bids need to consider the double moral hazard problem as well. If the auction-based PPC solves the double moral hazard problem as well, then our insights about further improvements to the detection technologies will carry over in that setting as well; and a third-party investigation will be helpful to induce further improvements. Overall, in general, for PPC models, we show that an alternative mechanism, in which the independent party executes the investigation, helps the PPC model solve not only the moral hazard problem but also the unilateral improvement problem.

This is a first step to provide insights into the demand for alternative mechanisms that are not based on ${ \mathrm { P P C } } ,$ and it opens the door for a rich array of possibilities that future work can examine. For example, future research can examine whether reputation in a multiperiod repeated game can help induce the SP and the advertiser to make improvements to their respective technologies. In a related fashion, future work can also examine competition among advertisers where the expected benefit of each advertiser is adversely affected by the number of pages on which his competitors advertise. This will create an interaction between competition and the click fraud problem, and whether such competition helps to create incentives for the advertiser and the $\mathrm { S P }$ to unilaterally improve their click fraud identification technologies will be an interesting extension. In addition, it will also be interesting to consider a single SP with multiple advertisers wherein the SP optimizes on the high classification technologies by considering the portfolio of advertisers and their potential verification costs. Although we demonstrated a structure of competition and private information where our result will carry through (see Online Appendix B), future research could expand the number of advertisers, advertising slots, and SPs to describe the effect of click fraud on Edelman et al. (2007) generalized second price auction mechanism.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2015.0598.

## Acknowledgments

The authors would like to thank the senior editor, associate editor, and the anonymous reviewers for their constructive comments and suggestions.

## References

AdWatcher (2010) Testimonials-AdWatcher. Accessed July 5, 2015, http://www.adwatcher.com/testimonials.php.

Arya A, Glover J, Radhakrishnan S (2007) The Controllability Principle in Responsibility Accounting: Another Look, Essays in Accounting Theory in Honour of Joel S. Demski (Springer, New York), 183–198.

Baiman S, Fischer PE, Rajan MV (2000) Information, contracting and quality costs. Management Sci. 46(6):776–789.

Balachandran KR, Radhakrishnan S (2005) Quality implication of warranties in a supply chain. Management Sci. 51(8):1266–1277.

BlissITSolution (2014) Pay per click (PPC). Accessed July 5, 2015, http://www.blissitsolutions.com/pay-per-click/.

Cavusoglu H, Mishra BK, Raghunathan S (2005) The value of intrusion detection systems in information technology security architecture. Inform. Systems Res. 16(1):28–46.

Chen M, Jacob VS, Radhakrishnan S, Ryu YU (2012) The effect of third party investigation on pay-per-click advertising. 33rd Internat. Conf. Inform. Systems, Orlando, FL.

Clay B (2011) The difference between flat rate and bid-based PPC campaigns. Accessed July 5, 2015, http://www.sitepronews.com/ 2011/07/22/the-difference-between-flat-rate-and-bid-based -ppc-campaigns/.

ClickFacts (2010) ClickFacts ad network suite for advertising networks and publishers. Accessed November 13, 2011, http://www .clickfacts.com/ad-buddy.html.

Clicklab (2006) Clicklab click fraud detection frequently asked questions. Accessed July 5, 2015, http://www.clicklab.com/ Clicklab-click-fraud-detection-FAQ.pdf.

Click Forensics (2010a) Click fraud rate rises slightly in Q2 2010 to 18.6 percent. Accessed November 13, 2011, http:// www.clickforensics.com/newsroom/press-releases/165-click -fraud-rate-rises-slightly-in-q2-2010-to-186-percent.html.

Click Forensics (2010b) Current click forensics for advertisers. Accessed November 13, 2011, http://www.clickforensics.com/ products/for-advertisers-and-agencies/advertiser-advertisers .html.

Click Forensics (2010c) Collecting click data. Accessed November 13, 2011, http://www.clickforensics.com/whatwedo/how-we-do-it/ getting-data.html.

Daswani N, Mysen C, Rao V, Weis S, Gharachorloo K, Ghosemajumder S (2008) Online advertising fraud. Jakobsson M, Ramzan Z, eds. Crimeware: Understanding New Attacks and Defenses (Addison-Wesley Professional, Indianapolis).

Delaney K (2005) In “Click fraud,” Web outfits have a costly problem: Marketers worry about bills inflated by people gaming the search ad-system. Wall Street J. (April 6) A1. http://online.wsj.com/ article/SB111275037030799121.html.

Demski JS, Frimor H, Sappington DEM (2004) Efficient manipulation in a repeated setting. J. Accounting Res. 42(1):31–49.

Dunaway G (2010) ContextWeb partners with Mpire for Adsdaq verification. Accessed July 5, 2015, http://www.adotas.com/2010/ 09/contextweb-partners-with-mpire-for-adsdaq-verification/.

Edelman B, Ostrovsky M, Schwarz M (2007) Internet advertising and the generalized second price auction: Selling billions of dollars worth of keywords. Amer. Econom. Rev. 97(1):242–259.

eMarketer (2014) Digital ad spending worldwide to hit \$137.53 billion in 2014. Accessed July 5, 2015, http://www.emarketer.com/ newsroom/index.php/digital-ad-spending-top-37-billion-2012 -market-consolidates/.

Eroshenko D (2004) Click fraud: The state of the industry. Pay Per Click Analyst. http://www.payperclickuniverse.com/pay -per-click-search-engines-articles.php?article\_id=23.

Gaustella N (2007) Estimating the real click fraud rate. Accessed July 5, 2015, http://www.sitepronews.com/2007/04/13/estimating -the-real-click-fraud-rate/.

Ghosemajumder S (2007) Invalid clicks—Google’s overall numbers. Accessed July 5, 2015, http://adwords.blogspot.com/2007/02/ invalid-clicks-googles-overall-numbers.html.

Goodman J (2005) Pay-per-percentage of impressions: An advertising method that is highly robust to fraud. Workshop on Sponsored Search Auctions, Vancouver.

Google (2014) Google’s protection against invalid clicks. Accessed July 5, 2015, http://www.google.com/ads/adtrafficquality/ invalid-click-protection.html.

Greenberg A (2008) Yahoo! cozies up to its click-fraud critics. Accessed July 5, 2015, http://www.forbes.com/2008/03/17/click-fraud -yahoo-tech-security-cx\_ag\_0317click.html.

Howlett G (2007) Combating click fraud. Marketing Pilgrim. Accessed July 5, 2015, http://www.marketingpilgrim.com/2007/05/ combating-click-fraud.html.

Hwang I, Radhakrishnan S, Su L (2006) Vendor certification and appraisal: Implications for supplier quality. Management Sci. 52(10):1472–1482.

IAB (2015) IAB Internet advertising revenue report—2014 full year results. Accessed July 5, 2015, http://www.iab.net/media/file/ IAB\_Internet\_Advertising\_Revenue\_Report\_FY\_2014.pdf.

Immorlica N, Jain K, Mahdian M, Talwar K (2005) Click fraud resistant methods for learning click-through rates. Deng X, Ye Y, eds. Internet and Network Economics. Lecture Notes Comput. Sci., Vol. 3828 (Springer-Verlag, Berlin Heidelberg), 34–45.

Jayanth R, Jacob V, Radhakrishnan S (2011) Vendor/client interaction for requirements assessment in software development: Implications for feedback process. Inform. Systems Res. 22(2):289–305.

Kshetri N (2010) The economics of click fraud. IEEE Security Privacy 8(3):45–53.

Lee CH (2007) Improving classification performance using unlabeled data: Naïve Bayesian case. Knowledge-Based Systems 20(3):220–224.

Leyden J (2009) Stealthy click fraud tool exploits 9ball attack. Accessed July 5, 2015, http://www.theregister.co.uk/2009/07/ 01/stealthy\_click\_fraud\_malware/.

Liu D, Chen J, Whinston AB (2009) Current issues in keyword auctions. Adomavicius G, Gupta A, eds. Handbook of Information Systems: Business Computing, Vol. 3 (Emerald Group Publishing Limited, Bingley, UK), 69–97.

Mahdian M, Tomak K (2009) Pay-per-action model for on-line advertising. Internat. J. Electronic Commerce 13(2):113–128.

Megna M (2008) Click Forensics submitting click fraud reports to Google. Accessed July 5, 2015, http://www.ecommerce -guide.com/news/news/article.php/3777551.

Mungamuru B, Weis S, Garcia-Molina H (2008) Should ad networks bother fighting click fraud? Yes, they should. Stanford Infolab Technical Report, Stanford, CA, http://ilpubs .stanford.edu:8090/840/.

Nelson T (2007) Mortgage fraud at financial institutions: Prevention and response. Financial services alert. Pepper Hamilton LLP. Accessed July 5, 2015, http://apps.americanbar.org/buslaw/ committees/CL130000pub/newsletter/200703/nelson.pdf.

O’Malley G (2014) Click fraud costs marketers \$11B, IAB issues key report. Accessed July 5, 2015, http://www.mediapost.com/ publications/article/218549/click-fraud-costs-marketers-11b -iab-issues-key-r.html.

Olsen S (2008) Click Forensics, Yahoo take on click-fraud cases. Accessed July 5, 2015, http://news.cnet.com/8301-1023\_3 -9986373-93.html.

Perez JC (2008) Google allies with click-fraud-detection firm Click Forensics. Accessed July 5, 2015, http://www.computerworld .com/article/2533534/security0/google-allies-with-click-fraud -detection-firm-click-forensics.html.

Perez JC, Menezes JP (2009) Foxy “Bahama botnet” causes surge in click fraud. Accessed July 5, 2015, http://www.itbusiness.ca/ news/foxy-bahama-botnet-causes-surge-in-click-fraud/14026.

Peters G (2010) How to fight click fraud in Google Adwords. Accessed July 5, 2015, http://www.cyberindian.com/web -marketing/google-adwords/how-to-fight-click-fraud-in-google -adwords.php.

PocketCents (2014) Flat rate PPC local online advertising. Accessed July 5, 2015, https://pocketcents.wordpress.com/local-online -advertising/.

Ponemon Institute (2013) The 2013 eCommerce cyber crime report: Safeguarding brand and revenue this holiday season. Accessed

July 5, 2015, http://www.emc.com/collateral/analyst-reports/ h12493-ar-2013-ecommerce-cyber-crime-report.pdf.

Recker K (2013) Flat rate cost per click (CPC) vs. real time bid costs. Accessed July 5, 2015, http://www.ntent.com/resources/ flat-rate-cost-per-click-cpc-vs-real-time-bid-costs.

Schwarz B (2008) Yahoo partners with 3rd party click fraud company, Click Forensics. Accessed July 5, 2015, http:// searchengineland.com/yahoo-partners-with-3rd-party-click -fraud-company-click-forensics-13586.

Taube A (2014) Botnets will cause \$11.6 billion in wasted ad spending this year. Accessed July 5, 2015, http://www .businessinsider.com/study-bots-will-waste-116b-in-ad-spend -in-2014-2014-1.

Tuzhilin A (2006) The Lane’s gifts v. Google report. Accessed July 5, 2015, http://googleblogspot.com/pdf/Tuzhilin\_Report.pdf.

Virginia (2014) Medicaid fraud and non-fraud recovery. Accessed July 5, 2015, http://www.dss.virginia.gov/files/division/bp/ medical\_assistance/manual\_transmittals/manual/m17.pdf.

Vranica S (2014) A “crisis” in online ads: One-third of traffic is bogus. Wall Street J. http://www.wsj.com/articles/SB10001 424052702304026304579453253860786362.

Wilbur KC, Zhu Y (2009) Click fraud. Marketing Sci. 28(2):293–308.

Zhang X, Feng J (2011) Cyclical bid adjustments in search-engine advertising. Management Sci. 57(9):1703–1719.
