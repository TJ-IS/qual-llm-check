---
otero_id: 8076
otero_key: "ZRGAEC87"
title: "Towards an interdisciplinary perspective of training intervention for negotiations: Developing strategic negotiation support contents"
authors: "Sungsoon Park; Gary E. Bolton; Ling Rothrock; Jeannette Brosig"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.02.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Towards an interdisciplinary perspective of training intervention for negotiations: Developing strategic negotiation support contents

Sungsoon Park ⁎, Gary E. Bolton, Ling Rothrock, Jeannette Brosig

Industrial and Manufacturing Engineering, Pennsylvania State University, University Park, Pennsylvania 16802, United States Smeal College of Business, Pennsylvania State University, University Park, Pennsylvania 16802, United States Economics and Business Administration, University of Duisburg-Essen, Universitaetsstrasse 12, 45117 Essen, Germany

## a r t i c l e i n f o

Article history: Received 1 January 2009 Received in revised form 16 February 2010 Accepted 22 February 2010 Available online 1 March 2010

Keywords: Electronic negotiation support systems Negotiation analysis Game theory e-commerce

## a b s t r a c t

This paper presents a prototype negotiation support system (NSS) intended to help the user to analyze the economic underpinnings of the negotiation, and to construct an initial offer. We also present the results of a behavioral test of the system using techniques from the <sup>fi</sup>eld of experimental economics. In the test, negotiators have private, asymmetric information about the value of the negotiated item. In one treatment both negotiators operate without an NSS, and in a second treatment the seller has an NSS. The data shows that the NSS assisted negotiators make offers that lead to better price outcomes for themselves. The NSS is web-based and the system might have particular relevance for e-negotiating.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

This paper presents a prototype negotiation support system (NSS) that takes the bargainer through the analysis of the economic underpinnings of the negotiation, and the formulation of initial offers. The principles underlying the NSS are culled from negotiation <sup>fi</sup>ndings in the decision science, economics and psychology literatures. The principles are general, be<sup>fi</sup>tting an NSS that aims at broad application. An important question is whether users can successfully apply an NSS of this kind to specific negotiations. As a <sup>fi</sup>rst step towards answering this question, we present a behavioral validation test of the system using techniques from experimental economics, involving human subjects who are given material incentives to perform the best they can. The test case negotiation is patterned after an actual negotiation, and features the private, asymmetric information that makes evaluating the other party's economic circumstance a challenge.

The NSS prototype has three components: A content component provides the negotiator with concepts and information culled from the negotiation analysis literature. The content component is nested in a process component that provides a framework to help the negotiator begin to organize his or her thoughts. A communication component provides an electronic ‘negotiation table.

The content component guides the user in estimating the opportunity costs for each bargainer, and in constructing a zone of potential negotiated agreements (ZOPA). Given the ZOPA, the NSS then provides guidelines on how to formulate a good opening offer. Research shows that focusing the negotiator's attention on the ZOPA — what is potentially in the deal for the other person as well as oneself — helps the negotiator avoid being “anchored” by aggressive demands made by the other side [2,21]. In addition, it is well established that the opening offers of each negotiator are good predictors of the eventual settlement [33]. In essence, the NSS aims to get the user off to a good start, guiding through what are, strategically speaking, the critical <sup>fi</sup>rst steps [5,10,21].

The present work builds on work done by Galinsky and Mussweiler [10]. They provide experimental evidence on the positive in<sup>fl</sup>uence that perspective taking (e.g., thinking about the other party's options) has on a negotiator. The design of Galinsky and Mussweiler's experiment re<sup>fl</sup>ects their objective of isolating particular behavioral effects, and they control aspects of the negotiation, such as who makes the <sup>fi</sup>rst offer. We extend their work to a more free-form environment, more akin to one in which a negotiator normally operates. The NSS walks the negotiator through a perspective taking exercise prior to the negotiation, and independent of who makes the <sup>fi</sup>rst offer. Another difference is that the NSS provides the negotiator with information on crafting an initial offer (each negotiator can make an initial offer, but only one initial offer can be the first offer in the negotiation).

The validation test focuses on a case study that captures some of the richness of a buyer–seller price negotiation. The parties have private, asymmetric information about the value of the item. That is, each party knows the value of the item to themselves but has only a partial understanding of what the value is to the other party. There are, of course, clues in the environment as to what the value to the other party might be. The clues in the test case re<sup>fl</sup>ect the kind of information that one could <sup>fi</sup>nd in the public domain (in fact, the clues in the case were found on the Internet).

The validation test is web-based and has two treatments. In the baseline treatment, both negotiators operate without the NSS. In the negotiation support treatment, the seller has an NSS. We then compare the results of the two treatments to see whether the NSS can assist seller decision making.

Our research has particular relevance to electronic negotiation (e-negotiation). Electronic environments are particularly amenable to the implementation of a system of the kind presented here, and the system could eventually be integrated with e-negotiation media and complementary support systems (potential complements to be elaborated on in a moment). At the same time, there is evidence that the medium the negotiation takes place in can in<sup>fl</sup>uence the outcome [29], so it may turn out to be important that we test the behavioral response to an NSS in a speci<sup>fi</sup>c e-negotiation environment.

Negotiation is a complex social activity, and we intend our prototype as a complement to NSS's that address other important aspects of the negotiation problem. There are a number of existing NSS's that rely on template-based and arti<sup>fi</sup>cial intelligence techniques [4]. Template-based NSS focuses on informing parties of past and present preferences, and on the progress made within the negotiation. Examples include Negotiator Pro, the Art Of Negotiating [7] and DEUS [34]. Web-enabled NSS include Smartsettle [26], INSPIRE [13] and CBSS [32]. Early decision-support negotiation systems primarily used arti<sup>fi</sup>cial intelligence techniques to model negotiation such as casebased reasoning, rule-based reasoning and hybrid reasoning. These systems are considered to be intelligent systems since they can generate solutions using the system's internal knowledge as well as users' input. Examples include LDS [20], SAL [31], NEGOPLAN [17], Mediator [14], PERSUADER [25] and Family\_Negotiator [3].

The NSS presented here focuses on fundamental principles associated with the economic strategy of negotiation, having to do with evaluating bargainer opportunity cost and using this information to derive an initial offer. The prototype NSS guides bargainers through a process (as opposed to giving them solutions). The steps in the process are how to prepare for the negotiation, how to derive an initial offer, how to avoid the anchoring effect from the other party's <sup>fi</sup>rst offer, and how to estimate the <sup>fi</sup>nal agreement price based on the other party's and the user's initial offers.

## 2. Process framework and description of the NSS content component

## 2.1. Negotiation process framework

We can think of negotiation as having three stages: the preparation phase (what to do before the negotiation begins), the initial offers phase and the reconciliation and outcome phase. A negotiation may not break down cleanly in these phases. Nevertheless, the framework is a useful organizational tool. The NSS uses insights from the literature to assist the negotiator through the <sup>fi</sup>rst two phases (and points out the direction the third phase is likely to take given what happens in the <sup>fi</sup>rst two phases).

## 2.1.1. Preparation for negotiation

During the preparation phase, the NSS draws attention to four critical constructs: interests, best alternative to a negotiated agreement, reservation prices and ZOPA. The basic procedure is to <sup>fi</sup>rst prompt the user to consider his own circumstance (e.g., his own interests) and then ask him to re<sup>fl</sup>ect on what information he has that provides insight into the other party's circumstance (e.g., the other party's interests). The full contents of the NSS are laid out in Appendix B; in this section we discuss the critical features.

2.1.1.1. Interests. Misunderstanding the interests of one's negotiation counterpart can lead to erroneous attributions [18], failure to maximize joint gain [28], or impasse [27]. In addition, not understanding the other side's sources of power may lead to unwise strategies that can produce adverse outcomes. So it is important to understand not only one's own interests, but also the other party's interests and alternatives to a negotiated agreement.

The contents of the NSS explain to the user that, “Interests are the underlying reasons that each party has for wanting to reach agreement.” The system user (the seller in this case) is reminded of his own interests, and then asked, “From what you know presently, what would you say the buyer's interest is? Give your best guess.” This type of debiasing technique is known as “considering the opposite” [16].<sup>1</sup>

2.1.1.2. Best alternative to a negotiated agreement (BATNA) and reservation price. The NSS next explains to the user that “A bargainer's interests tell something about the best alternative to a negotiated agreement (BATNA), what will be done if no settlement is reached in the negotiation. In turn BATNA helps understand the walk-away value, the price below or above which a bargainer is no longer interested in an agreement.” Determining the BATNA is critical to determining the opportunity cost the negotiator incurs in entering into an agreement [9], which is in turn critical to determining the walk-away value, more formally known in the literature as the reservation price [22]. The system user is reminded of his own BATNA and walk-away value, and then is asked to give a best guess of the buyer's BATNA and walk-away value.

2.1.1.3. Zone of possible agreement (ZOPA). The bargaining zone is a fundamental concept in negotiation analysis [22,30]. The NSS explains to the user that, “Together, the buyer and seller walk-aways de<sup>fi</sup>ne the zone of possible agreement (ZOPA). Each point inside the ZOPA represents a settlement at which both parties would <sup>fi</sup>nd it pro<sup>fi</sup>table to make an agreement.” The concept is illustrated to the user with a diagram (see Fig. B.1 in Appendix B). The user is further advised that, “During the negotiation, and particularly at the beginning of the negotiation, ask questions to test if your understanding of the buyer's interests is correct. Your goal, as seller, is to obtain a price at the high end of the ZOPA, while the buyer can be expected to work to obtain a price at the lower end.”

## 2.1.2. Initial offers for negotiation

The anchoring effect refers to the fact that people tend to make adjustments to their position based on an initial starting position, and often the adjustment process is slow. First offers exhibit a strong anchoring effect in situations of <sup>fl</sup>uidity and uncertainty as is often the case with negotiations [10]. They exercise a strong in<sup>fl</sup>uence on both counteroffers [12] and <sup>fi</sup>nal outcomes [5,6,15,19]. More speci<sup>fi</sup>cally, because of the anchoring effect, initial counteroffers and <sup>fi</sup>nal outcomes are consistently found to be positively correlated with <sup>fi</sup>rst offers. In addition, <sup>fi</sup>rst offers are better predictors of <sup>fi</sup>nal settlement price than is knowledge of concessionary behavior [33].

Based on the above research [11], the NSS advises the user to make an aggressive initial offer — but one within reason. On the one hand, an aggressive initial offer leverages the positive correlation of counteroffer and concessionary behavior, making for a better expected outcome for the user. On the other hand, as unreasonably aggressive offer, de<sup>fi</sup>ned in the NSS as an offer that “does not satisfy, under any conditions” the interests of the party who receives it, threatens to undermine the offerer's credibility. The NSS advises that “under no conditions, should you respond” to an unreasonable offer “with a counteroffer” since this only validates the unreasonable behavior.

Advice in the initial offer section of the NSS was organized as answers to four questions: “How aggressive should my initial offer be?”; “Is it better to put my initial offer on the table <sup>fi</sup>rst or after the other bargainer?”; “How should I respond if the other bargainer makes an unreasonable <sup>fi</sup>rst offer?”; and “Given the two initial offers, what is the most likely settlement given the two initial offers?” (Appendix B lists the answers given.)

## 2.2. Research objective

In light of the <sup>fi</sup>ndings of the negotiation research, the main question guiding the development and testing of a prototype NSS is this: Does leading the negotiator through the application of broad strategic concepts to their negotiation problem make participants more effective in the practice of negotiation?

In the experiment, we will investigate how negotiators perform without an NSS versus with one to guide them. The speci<sup>fi</sup>c issues of interest are: (1) how the <sup>fi</sup>rst offers differ between the two treatments; (2) how the counteroffers differ between the two treatments; and (3) how much a system user's negotiation performance improves, as measured by the <sup>fi</sup>nal price agreement.

## 3. Experiment design

We <sup>fi</sup>rst describe the test case negotiation used in the study. We then discuss the negotiation web platform, followed by a description of the treatments and methods used to run the experiment.

## 3.1. Test case negotiation

In the negotiation, each party knows the value of the item to themselves but has only a partial understanding of what the value is to the other party. Neither the structure of this information nor the possible moves of the negotiators during the negotiation are common knowledge (Sebenius [23], discusses why these features are critical to the outcomes of negotiation in practice). The case involves the sale of the Internet domain name “Grays.com.” Easy to remember domain names are highly sought by business, since names that are dif<sup>fi</sup>cult to remember can lead to a loss of trade. The market value of domain names varies widely, ranging from the cost of the registration fee up to the most ever paid, \$345 million for ‘business.com’ [1].

The Grays.com negotiation involves a seller and a buyer looking to negotiate a transaction price. The pro<sup>fi</sup>t for the seller (Chris) is the difference between the negotiated price and the reservation price (\$15,000). The pro<sup>fi</sup>t for the buyer (Kelly) is the difference between the reservation price (\$550,000) and the negotiated price. Each negotiator's task is to maximize his or her own pro<sup>fi</sup>t from the negotiation. All parties know their own reservation price, but are uncertain about the other party's reservation price.

The summary of public information for both parties is as follows (see Appendix A for the full case): The Grays are getting ready for what will be the <sup>fi</sup>rst major league baseball season played in Washington in several decades. Kelly, owner of this baseball team, is interested in a new web site because baseball teams sell tickets through their web sites. Washington lured the team by agreeing to <sup>fi</sup>nance and build a new \$440 million stadium that it will rent to the team for an average of \$5.5 million per year. The city expects average attendance to be 30,000 people per game. The average ticket price will be \$21.43. The Grays are scheduled to play 86 home games this season. Information of this sort is easily obtained on the Internet. The name of the team, ‘Grays’, was announced to the public soon after the decision to move to Washington was taken, and prior to checking domain name availability.

Chris, the present owner of the Grays.com name, runs Gray's Restaurant and Catering which is located in a college town of about 120,000 people, several hundred miles from Washington. ‘Grays.com’ promotes both restaurant and catering businesses. The restaurant's menu is prominently displayed, complete with this week's special offerings, as are directions to the restaurants. Catering menus and suggestions are also posted.

Kelly recently telephoned Chris to say he might be interested in buying the Grays.com name. The call was unsolicited: Chris had not put the domain name on the market. Chris asked for time to think about it. The parties agreed they would talk again within a few of days. Chris and Kelly have never previously had dealings, nor do they anticipate future business or social interaction. Either side can terminate negotiations and can refuse to make an agreement if either thinks that is what is best.

Grays.com has three features that make it an apt test bed for the NSS prototype. First, it captures the basic strategic elements of negotiations in naturally arising circumstances: Domain name negotiations are commonly about price determination (in fact, Grays.com is based on a true story although it is unlikely that subjects were familiar with it). Second, the negotiating context of the “Grays. com” negotiation is easy to explain and to understand. Third, domain name transactions potentially have a large ZOPA, admitting a wide range of outcomes that are bene<sup>fi</sup>cial to both parties, and so the kind of negotiation in which an NSS might do a negotiator the most good.

Observe that the seller Chris has an information advantage in that he has more information available to calculate the revenue value of the domain name to Kelly than Kelly has to calculate the same for Chris. Observing the case as a role playing exercise in classes suggested that those playing Chris did not always have the skill to press this advantage. For this reason, we decided to run the test giving Chris the NSS.

## 3.2. Building an electronic negotiation web platform

The main functions of the Negotiation Site are the following: 1) web access so that two parties anywhere can negotiate; 2) communication and interaction tools so that negotiators can communicate in real-time; 3) offer and message storage enabling review of this information at any time during the negotiation; and 4) security and privacy so that the system should be able to recover from system or communication failure. All information is stored in a database on a server machine. The Negotiation Site has three main web pages: Negotiation Home (see Fig. 1- A), Negotiation Table (see Fig. 1-B), and Summary of Negotiation (see Fig. 1-C). Through the Negotiation Home, participants move to the registration web page. Once a participant completes the registration, the participant can move to the Negotiation Table, where negotiators receive or send their offers or messages to one another. Upon completion of the negotiation, the Summary of Negotiation states the agreed upon price.

## 3.3. Treatments and laboratory protocol

## 3.3.1. Treatments

The experiment had a between-subjects design with forty subjects in each of two treatments. All participants were full-time undergraduate or graduate students at the Pennsylvania State University. Each participant was assigned to either the buyer or the seller role, and matched with a participant in the other role for a single negotiation. In the baseline treatment, both parties negotiated without the prototype NSS. In the negotiation support treatment, sellers were aided by the prototype NSS while the buyers were not. The buyer did not know the seller had access to an NSS.

A  
![](/api/attachments/ZRGAEC87/fulltext/images/d7bce42f507bb9ad4d0966d8aa73ec13fdf1e49ace0bee2fe4b15acfb2ed734a.jpg)

![](/api/attachments/ZRGAEC87/fulltext/images/cc43e40b31a18d19629838b403fc2d6fab142a2b833f62bfdb02179b6abb88da.jpg)

C  
![](/api/attachments/ZRGAEC87/fulltext/images/96cc7777783559cdcc6f3ac0b11840341fdd737468c2fd8e67a83317216836ec.jpg)  
Fig. 1. Negotiation web site.

## 3.3.2. Laboratory protocol

Participants receive instructions on how to conduct a two-party negotiation via the Negotiation Table web page. Participants assigned to the buyer role sat on one side of the computer room while those assigned to the seller role sat on the opposite side. Buyer–seller pairings were anonymous. The instructions included a packet of materials including the treatment protocol, public information (see Appendix A.1), and private information depending on their role (see Appendices A.2 and A.3). After reading the instructions, assigned pairs conducted their negotiation. The time allotted for negotiating was 60 min, with remaining time displayed on the computer. Bargainers reached a mutual settlement by agreeing to a price or, if time lapsed, the negotiation was declared an impasse without agreement.

All participants received a \$5 show-up fee. Those who reached a negotiated agreement received an additional US\$0.053 per 1000 dollars of pro<sup>fi</sup>t implied by the negotiated price (maximum of \$25 plus show-up fee). Individual negotiation results and payments were treated as con<sup>fi</sup>dential information. Each treatment took about 90 min to complete.

## 4. Results and discussion

We compare the two treatments through three central variables: <sup>fi</sup>nal agreement price, <sup>fi</sup>rst offer, and initial counteroffer (the latter two together being ‘the initial offers’).

## 4.1. Final agreement

All forty negotiation pairs (20 pairs for the baseline treatment and 20 pairs for the negotiation support treatment) reached an agreement. The average <sup>fi</sup>nal agreement price under the negotiation support treatment is signi<sup>fi</sup>cantly higher than that of the baseline treatment (\$277,728 vs. \$155,543, pb0.005, one-tailed robust rankorder test<sup>2</sup>). This is consistent with the supposition that the NSS helps sellers in the negotiation support treatment to reach a more favorable <sup>fi</sup>nal agreement.

## 4.2. Initial offers

To better understand how the NSS assisted sellers reach better agreements, we turn our attention to initial offers. The breakdown of initial offers (<sup>fi</sup>rst offers and initial counter offers) by role is shown in Table 1.

The NSS was based on the supposition that sellers would reach better results due to changes in initial offer behavior. So sellers' initial offers (either <sup>fi</sup>rst offers or initial counteroffers) made in the negotiation support treatment should be higher than sellers' initial offers made in the baseline negotiation (see Fig. 2). We did an analysis of variance (ANOVA) on the two dimensions of the experiment: type (baseline treatment vs. negotiation support treatment) and role (buyer vs. seller). The test reveals signi<sup>fi</sup>cant differences in both type (F(1,75)=5.281, p=0.024) and role (F(1,75)=23.576, p=0.000). There is also a signi<sup>fi</sup>cant interaction effect (F(1,75) = 5.595, p=0.021, shown in Fig. 2).

The ANOVA results seem to be mainly driven by the fact that the sellers' initial counteroffers are less affected by the buyers' <sup>fi</sup>rst offers in the negotiation support treatment than in the baseline treatment. Also, the average of sellers' <sup>fi</sup>rst offers in the negotiation support treatment is signi<sup>fi</sup>cantly higher than the average of seller's <sup>fi</sup>rst offers in the baseline treatment (\$580,000 vs. \$269,375 pb0.001, one-tailed robust rank-order test). That is, the <sup>fi</sup>rst offer anchoring effect is mitigated. The average of initial counteroffers made by sellers is signi<sup>fi</sup>cantly more aggressive (i.e., higher) in the negotiation support treatment than in the baseline treatment as well (\$571,071 vs. \$235,583 pb0.025, one-tailed robust rank-order test). The average of buyers' <sup>fi</sup>rst offers, the average of sellers' <sup>fi</sup>rst offers and the average of buyers' initial counteroffers in the baseline treatment are not signi<sup>fi</sup>cantly different from each average of those values in the negotiation support treatment (see Table 2).

Table 1  
Number of the initial offers and agreements in two treatments

<table><tr><td>Type of treatment</td><td colspan="2">Baseline treatment</td><td colspan="2">Negotiation support treatment</td></tr><tr><td>Role in negotiation</td><td>Buyer (Kelly)</td><td>Seller (Chris)</td><td>Buyer (Kelly)</td><td>Seller (Chris)</td></tr><tr><td>No. first offer made by</td><td>12</td><td>8</td><td>14</td><td>5 (6)a</td></tr><tr><td>No. initial counteroffer made by</td><td>8</td><td>12</td><td>6</td><td>14</td></tr><tr><td>No. agreement</td><td>20</td><td></td><td>20</td><td></td></tr></table>

<sup>a</sup> In the negotiation support treatment, one seller made a <sup>fi</sup>rst offer of \$300,000,000. This value was excluded for <sup>fi</sup>rst offers related to data analyses for this paper (including this value would not change our main observations).

![](/api/attachments/ZRGAEC87/fulltext/images/3150dfbc8fd2012b44dc233815bbe98ead3c6dca9a51dda909b5c4f85df100e3.jpg)  
Fig. 2. Average of initial offers by treatment and role.

## 4.3. Correlation and regression

Investigating the correlation between initial offers and <sup>fi</sup>nal prices provides further support for the supposition that the higher <sup>fi</sup>nal prices in NSS are due to changes in initial offer decisions. In particular, more aggressive (higher) initial offers should induce more bene<sup>fi</sup>cial <sup>fi</sup>nal agreements for sellers in both treatments. The more aggressive or higher sellers' initial offers can be measured as the difference between seller initial offer and buyer initial offer for each negotiation pair.

Correlation results obtained from the two treatments are given in Table 3. In the baseline treatment, both <sup>fi</sup>rst and initial offers, whether made by buyers or sellers, are positively and signi<sup>fi</sup>cantly correlated with the <sup>fi</sup>nal price. And initial offers are positively and signi<sup>fi</sup>cantly correlated with one another. Turning to the negotiation support treatment, we see that correlations involving the seller remain strong, while those involving the buyer have been greatly reduced and are generally not signi<sup>fi</sup>cant. That is, the anchoring effect associated with the buyer's initial (<sup>fi</sup>rst) offer is greatly reduced when the seller is assisted by the negotiation support system.

Table 3  
Correlation results in two treatments.

<table><tr><td colspan="2">Baseline treatment</td><td>Correlation (Spearman)</td></tr><tr><td>Seller&#x27;s first offers</td><td>Final prices</td><td> $r(8)=0.738, p=0.037$ </td></tr><tr><td>Buyer&#x27;s first offers</td><td>Final prices</td><td> $r(12)=0.550, p=0.064$ </td></tr><tr><td>Sellers&#x27; initial offers</td><td>Buyers&#x27; initial offers</td><td> $r(20)=0.563, p=0.010$ </td></tr><tr><td>Sellers&#x27; initial offers</td><td>Final prices</td><td> $r(20)=0.937, p=0.000$ </td></tr><tr><td>Buyers&#x27; initial offers</td><td>Final prices</td><td> $r(20)=0.556, p=0.011$ </td></tr><tr><td colspan="2">Negotiation support treatment</td><td>Correlation (Spearman)</td></tr><tr><td>Seller&#x27;s first offers</td><td>Final prices</td><td> $r(5)=0.872, p=0.050$ </td></tr><tr><td>Buyer&#x27;s first offers</td><td>Final prices</td><td> $r(14)=-0.220, p=0.450$ </td></tr><tr><td>Sellers&#x27; initial offers</td><td>Buyers&#x27; initial offers</td><td> $r(19)=-0.035, p=0.888$ </td></tr><tr><td>Sellers&#x27; initial offers</td><td>Final prices</td><td> $r(19)=0.732, p=0.000$ </td></tr><tr><td>Buyers&#x27; initial offers</td><td>Final prices</td><td> $r(19)=0.050, p=0.838$ </td></tr><tr><td>Sellers&#x27; initial offers</td><td>Seller&#x27;s assessments for buyer&#x27;s reservation price</td><td> $r(19)=0.859, p=0.000$ </td></tr></table>

Spearman Correlation test is signi<sup>fi</sup>cant at the p≤0.05.

Fig. 3 associates each <sup>fi</sup>nal price with the difference between the seller's initial offer and the buyer's initial offer. The scatter plot and associated regression lines show that, for a given difference in initial offers, <sup>fi</sup>nal prices tend to be higher in the negotiation support treatment than in the baseline treatment. While the regression lines cross, this is because of the two exceptional outcomes in the negotiation support treatment, both of which are also associated with quite high <sup>fi</sup>nal prices. The evidence in Fig. 3 suggests that sellers in the negotiation support treatment were better able to overcome the anchoring effect of buyer's initial offers than were sellers in the baseline treatment.

## 5. Summary

The prototype NSS organizes the negotiation into three phases: the preparation phase, the initial offer phase, and the reconciliation and outcome phase. The NSS content is based on some of the most robust research <sup>fi</sup>ndings concerning negotiation behavior, and guides system users through the <sup>fi</sup>rst two steps of the process. In the preparation phase, the NSS motivates system users to think not only about their own reservation price and BATNA, but also about the other party's reservation price and BATNA, along with the ZOPA. The NSS also guides initial offer formation. Together, the contents of the NSS aim to steer the system user away from the initial offer anchoring effect negotiators are known to be prone to. To validate the effectiveness of our prototype NSS, we conducted web-based negotiations using two types of treatments, a baseline treatment in which none of the negotiators has an NSS and a negotiation support treatment in which the sellers' decisions are assisted by an NSS.

In line with our supposition, the average of <sup>fi</sup>nal prices in the negotiation support treatment is signi<sup>fi</sup>cantly higher than in the baseline treatment. Further analyses of buyers' and sellers' initial offers reveal that this effect is due to differences in sellers' initial counteroffers. Assisted by a negotiation support system, sellers make, on average, signi<sup>fi</sup>cantly higher counteroffers than without such a system. Regression and correlation results demonstrate that the anchoring effect of buyers' <sup>fi</sup>rst offers was reduced when sellers were assisted by the NSS.

Table 2  
One-tailed robust rank-order test results by role of initial offers between two treatments.

<table><tr><td>Role</td><td colspan="2">Buyer</td><td rowspan="2">One-tailed robust rank-order test</td><td colspan="2">Seller</td><td rowspan="2">One-tailed robust rank-order test</td></tr><tr><td>Treatment</td><td>Baseline</td><td>Negotiation support</td><td>Baseline</td><td>Negotiation support</td></tr><tr><td>Average of first offer</td><td>$86,668</td><td>$43,215</td><td>Insignificant</td><td>$269,375</td><td>$580,000</td><td>Significant</td></tr><tr><td>Average of initial counteroffer</td><td>$59,813</td><td>$162,000</td><td>Insignificant</td><td>$235,583</td><td>$571,071</td><td>Significant</td></tr></table>

One-tailed robust rank-order test is signi<sup>fi</sup>cant at the 0.05 level.

![](/api/attachments/ZRGAEC87/fulltext/images/a662c9a31f227a2c834f5b8c37284a6cfec6d98d66955b502966b80f628514de.jpg)  
Fig. 3. OLS regression: Independent variable is difference value between the seller's initial offer and the buyer's initial offer, dependent variable is <sup>fi</sup>nal price

Our empirical <sup>fi</sup>ndings con<sup>fi</sup>rm that the prototype NSS is a useful tool to assist a negotiator. It promotes more effective performance, provides empirically validated strategic information that helps to mitigate the <sup>fi</sup>rst offer anchoring effect, and promotes better <sup>fi</sup>nal prices in negotiations.

Our test examined negotiating circumstances in which one negotiator was assisted by the NSS and the other was not. A useful extension for future testing would be to see how the system performs when both negotiators are assisted by the NSS. There are several interesting possibilities. One hypothesis would be that the in<sup>fl</sup>uence of the NSS is neutralized, so that an NSS user has an advantage if the other negotiator has no NSS, but neither side has an advantage when both employ the NSS. Observe that in this case, using the NSS is a dominant strategy: A negotiator gains an advantage if he is the only one using an NSS and needs an NSS to avoid disadvantage if the other side has one. Another hypothesis is that the effectiveness of the NSS depends on underlying information conditions. For example, the present test provided the NSS to the information advantaged negotiator. One might argue that, if both negotiators are assisted by an NSS, it would continue to favor the information advantaged negotiator since the added information provides greater grist for the kind of analysis the NSS promotes. Alternatively, however, the NSS might teach the information disadvantaged negotiator how to neutralize the information advantage of the other side, to the point where the information disadvantaged negotiator does better with an NSS, even if the other side uses one as well. Finally, in our test the negotiator with the NSS was more aggressive. If both negotiators have an NSS and if both are more aggressive, this might lead to a higher level of negotiations ending with no agreement (in our test, all negotiations ended with an agreement).

Further elaboration of the NSS might usefully proceed in two additional directions. One direction is the development of an additional training tool that helps to practice negotiation skills. This tool might, for example, might be elaborated to provide detailed feedback to users at the end of the negotiation. The other direction, for use in <sup>fi</sup>eld negotiations, is the extension to other common strategic problems, such as the handling of tradeoffs in negotiations involving multiple issues. This tool might, for example, provide assistance in making package offers. The empirical technique described in this paper can be extended to test the ef<sup>fi</sup>cacy of these further advancements.

## Acknowledgements

The authors are indebted to the unknown reviewers for their critical review and the pointing suggestions that enabled us to get the best out of this work. We are, indeed, thankful to them.

## Appendix A. Negotiation scenario information for subjects

## A.1. Public information for both parties

## A.1.1. Grays.com — with confidential information

The <sup>fi</sup>rst section of this case is public information available to all parties. The second section contains private information available only to your role. The case is patterned after an actual negotiation although names and some facts have been changed.

The negotiation involves the sale of the Internet domain name ‘Grays.com’. The present owner of the name is Chris Gray, proprietor and chef of Gray's Restaurant and Catering, located in a mid-west college town. The prospective buyer is the new major league baseball club, the Washington Grays. The Washington Grays are represented by Kelly Kaplan, one of the partners that own the team.

A.1.2. About Internet domgin names. All Internet locations have a numerical, or IP, address to identify them to networked computers. IP addresses are dif<sup>fi</sup>cult for most people to remember, and so the domain name system was created to provide more intuitive, less numeric addressing. Rights to domain names are governed by the Internet Corporation for Assigned Names and Numbers (ICANN), an international nonpro<sup>fi</sup>t group chartered for “preserving the operational stability of the Internet.” ICANN runs, or <sup>fi</sup>nds companies to run, the 13 “root server” computers that contain the IP addresses for all top-level domains (.com, .org, .de, etc.) used in the world. The .com domain is run by the Verisign company. Domain names are registered through third party companies that Verisign licenses. These companies charge \$9 to \$35 a year to register a domain name, paying \$6 of the fee to Verisign. Once a name is registered, it remains the property of the registrant so long as the annual renewal fee is paid. The registrant is free to sell the name to another party if they so choose. Resale of this sort is not unusual; in fact, there are several Internet markets that specialize in private domain name transactions. Domain names are often bought speculatively, in anticipation that they will have market value in the future.

Snappy, easy to remember domain names are highly sought by business, since names that are dif<sup>fi</sup>cult to remember can lead to a loss of trade. (Search engines ease this problem some, but to the extent that there are similar names used by different companies, there can still be confusion.) The market value of domain names varies widely, ranging from the cost of registration fee up to the most ever paid, \$7.5 million, for ‘business.com’. To cut down on customer confusion, some businesses take multiple domain names for their web site. This comes at a cost, however; the consultant Gartner Group estimates that managing a new domain name can cost \$75,000 for marketing and legal expenses.

A.1.3. About the Washington Grays. The Grays are getting ready for, what will be, the <sup>fi</sup>rst major league baseball season played in Washington in several decades. Prior to the upcoming season, the Grays played in Vancouver, Canada, as the ‘Bobcats’. The Vancouver team struggled, however, with low ticket sales. Washington lured the team by agreeing to <sup>fi</sup>nance and build a new \$440 million stadium that it will rent to the team for an average of \$5.5 million per year. The city expects average attendance to be 30,000 people per game. The average ticket price will be \$21.43. The Grays are scheduled to play 86 home games this season. (Information of this sort is easily obtained on the Internet.)

The name ‘Grays’ was chosen to commemorate the ‘Homestead Grays’, a team that played in the Negro Baseball League during the <sup>fi</sup>rst half of the twentieth century, at a time when African American players were not permitted in the major leagues. The name was announced to the public soon after the decision to move to Washington was taken for the purpose of generating publicity, and prior to checking domain name availability. Baseball teams sell tickets directly through their web sites. The sites are also used to promote the team and associated merchandise.

A.1.4. About Gray's Restaurant and Catering. Gray's Restaurant and Catering is located is a college town of about 120,000 people in a scenic area, several hundred miles from Washington. The business is housed in an upscale hotel of about 100 rooms. The hotel is busy year round, with lodgers coming for university events (e.g., sporting events, professional conferences, etc.), as well as for the regular entertainment events hosted by the local arena.

‘Grays.com’ promotes both restaurant and catering businesses (the hotel keeps a separate web site which links with Grays.com). The restaurant's menu, suitable for an upscale hotel, is prominently displayed, complete with this week's special offerings, as are directions to the restaurants. The site advises diners to make reservations and provides the phone number to do so. Catering menus and suggestions are also posted. Catering customers are invited to call to schedule an event.

A.1.5. About the negotiation. Kelly recently telephoned Chris saying that the Washington Grays might be interested in buying the Grays. com name. The call was unsolicited: Chris had not put the name on the market. Chris asked for time to think about it. The parties agreed they would talk again within a few of days.

This is a one-time bargaining situation. There is a single issue under contention: Price, and any agreement must be reported in terms of price only. An agreement should be treated as legally binding and <sup>fi</sup>nal. Both sides are permitted to break off negotiations and can refuse to make an agreement if they think that is what is best for them. Chris and Kelly have never previously had dealings nor do they anticipate future business or social interaction.

This completes the public information given to both bargainers. The private information re<sup>fi</sup>nes uncertainties in the public information concerning the bargainer's situation, what he knows about the other parties to the negotiation or about the object being negotiated. The private information does not introduce new issues.

## A.2. Private information for sellers (role Chris Gray) only

Chris Gray has had the “Grays.com” domain name since the business is beginning about <sup>fi</sup>ve years ago. While the web site has proven valuable, the business is now well known in what is, after all, a small town. Gray does not think it would be hard to redirect local restaurant and catering customers to a new web site. Moreover, records show that almost all out-of-town hits to the site come through the hotel's web site, and changing the hotel's site to link to a new domain name is easy. Still, advertising expenses associated with a change exist, and estimates for these are \$15,000 (seller's reservation price).

The pro<sup>fi</sup>t from any deal made to sell Grays.com, then, is

Negotiated price−\$15; 000:

Chris Gray's job is to maximize the pro<sup>fi</sup>t from the negotiation, given that the pro<sup>fi</sup>t will be \$0 if the deal is incomplete (taking less than \$15,000 for the domain name is not an option). As to the Washington Grays, you did some searching on the web and found that there are already a number of similar sounding web sites (e.g., GoGrays.com) that have been registered by businesses that intend to sell tickets to the games second hand. These sights might be confused with the of<sup>fi</sup>cial Washington Grays site (you also discovered that the margins in the middle man ticket business are generally small and so the companies rarely buy domain names at premium prices; i.e., they buy whatever name they can get for \$35 or less). Beyond this, you have no further information than the public information given above.

## A.3. Private information for buyers (role Kelly Kaplan) only

If Kelly Kaplan cannot obtain “Grays.com” domain name, the best alternative is to accept WashingtonGrays.com which is not yet registered to anyone, and is available for a \$10 registration fee. Kaplan estimates that using WashingtonGrays.com, instead of Grays.com, would cost the team 1% of ticket sales in the <sup>fi</sup>rst year. This creates an expected cost of about \$550,000 and becomes the upper limit for obtaining Grays.com. You think that the costs beyond the <sup>fi</sup>rst year will be far less substantial, and so accounting for them is not necessary.

The pro<sup>fi</sup>t from any deal made with Gray's Restaurant and Catering, then, is

\$550; 000−negotiated price:

The task, then, is to maximize pro<sup>fi</sup>t from the negotiation, given that the pro<sup>fi</sup>t will be \$0 if the deal does not occur. Paying more than \$550,000 (Buyer's Reservation Price) is not an option since this would give result in negative pro<sup>fi</sup>t. Concerning Gray's Restaurant and Catering, no further public information is available to Kaplan.

## Appendix B. Negotiation support contents (NSC) model for role sellers

Please read the following carefully before beginning the negotiation. The information provided, and the questions to consider, are intended to help you achieve a better negotiation outcome.

## B.1. Negotiation preparation phase

Prior to negotiation, you want to consider carefully, four critical concepts that will help you understand your own position as well as that of the other side

■ Interests are the underlying reasons that each party has for wanting to reach a negotiated agreement.

• You (Chris) are interested in selling the website “Grays.com” for the most cash possible. The amount must be high enough to cover any damage to your restaurant and catering business.

• From what you know presently, what would you say Kelly's interest is? Give your best guess.

■ A bargainer's interests tell something about the best alternative to a negotiated agreement (BATNA), what will be done if no settlement is reached in the negotiation. In turn, BATNA helps understand the walk-away value, the price below or above which a bargainer is no longer interested in an agreement.

• Your (Chris's) BATNA is to keep your website as is. The walkaway value you attribute to this option is the replacement value of the site, \$15,000.

• What is your best guess of Kelly's BATNA? From this BATNA, estimate Kelly's walk-away.

■ Together, Chris and Kelly's walk-aways de<sup>fi</sup>ne the zone of possible agreement (ZOPA). Each point inside the ZOPA (Fig. B.1) represents a settlement at which both parties would <sup>fi</sup>nd it pro<sup>fi</sup>table to make an agreement.

During the negotiation, and particularly at the beginning of the negotiation, ask questions to test if your understanding of Kelly's interests is correct. Your goal, as Chris, is to obtain a price at the higher end of the ZOPA, while Kelly can be expected to work to obtain a price at the lower end.

## B.2. Initial offer phase

After you have discussed interests with the opponent, at some point, one or both of you will make an initial offer. The data suggests that initial offers are the most important predictors of the bargaining settlement. The following information is provided to make a better initial offer. Here are answers based on data from previous studies in negotiation, to frequently asked questions about initial offers:

■ How aggressive should my initial offer be?

• The data suggests that bargainers do best when their initial offers are aggressive within reason. A good <sup>fi</sup>rst offer is one that appeals to the opponent's interests but stretches the other bargainer's ability to meet your demand. Usually, this means that the offer is in the neighborhood of the walk-away value of the other bargainer.

■ Is it better to put my initial offer on the table <sup>fi</sup>rst or after the other bargainer?

• The data suggests that, on average, no advantage or disadvantage accrues to going <sup>fi</sup>rst (or going second).

• One word of caution, if you put your initial offer on the table second: People who go second have a tendency to be in<sup>fl</sup>uenced by the initial offer <sup>fi</sup>rst put on the table. The higher (lower) the <sup>fi</sup>rst offer, the higher (lower) the initial counteroffer tends to be. If you make the initial counteroffer, do not be unduly in<sup>fl</sup>uenced by the <sup>fi</sup>rst offer.

■ How should I respond if the other bargainer makes an unreasonable <sup>fi</sup>rst offer?

• An unreasonable <sup>fi</sup>rst offer is one that does not satisfy, under any conditions, your interests. If you receive a <sup>fi</sup>rst offer like this, you should explain to the opponent that it is not acceptable for this reason, and throw it back to him or her for a more acceptable initial counteroffer. Under no conditions, should you respond with a counteroffer. Doing so, will only validate the unreasonable offer in the mind of the other bargainer.

■ Given the two initial offers, what is the most likely settlement given the two initial offers?

• If the initial offers differ, as they probably will, one or both sides will have to make concessions in order to arrive at an agreement. The data suggests that the most likely outcome is half way between the two initial offers (Fig. B.2). This is the reason for the importance for your first offer to be aggressive within reason, and why, if you go second, you should not be unduly in<sup>fl</sup>uenced by the other bargainer's <sup>fi</sup>rst offer.

![](/api/attachments/ZRGAEC87/fulltext/images/4c214f28f0450708f3ed2b31ead1fd9be1b37eead8cd9d9b3ee5bc7370ade5ab.jpg)  
Fig. B.1. Zone of possible agreement.

![](/api/attachments/ZRGAEC87/fulltext/images/2599c5c49e6c2620c7758e2ffc18e3812c79e7b651ac4cd2a7f8835468e53ee3.jpg)  
Fig. B.2. Mid-point of both parties' initial offers.

• The illustration in Fig. B.2 however, is average behavior. Ways exist to shade the concession stage of bargaining in your direction.

## References

[1] The Wall Street Journal, Master of Domain: Business.com Gets Big Payday, Again, http://online.wsj.com/article/SB118541740110378568.html (July 26, 2007).

[2] O.J. Bartos, Process and Outcome of Negotiation, Columbia University Press, New York, 1974

[3] E. Bellucci, J. Zeleznikow, Family-negotiator: an intelligent decision support system for negotiation in Australian family law, Forth Conference of the International Society for Decision Support Systems. International Society for Decision Support Systems, Lausanne, 1997.

[4] E. Bellucci, J. Zeleznikow, Trade-off manipulations in the development of negotiation decision support systems, International Conference on System Sciences, Hawaii, 2005.

[5] A.A. Benton, H.H. Kelley, B. Liebling, Effects of extremity of offers and concession rate on the outcomes of bargaining, Journal of Personality & Social Psychology 24 (1972) 73–83.

[6] J.M. Chertkoff, M. Conley, Opening offer and frequency of concessions as bargaining strategies, Journal of Personality & Social Psychology 7 (1967) 181–185.

[7] J.A. Eidelman, Software for negotiations, Law Practice Management 19 (1993) 50–55.

[8] N. Feltovich, Critical values for the robust rank-order test, Communications in Statistics — Simulations and Computation 34 (2005) 525–547.

[9] R. Fisher, W. Ury, Getting to Yes: Negotiating Agreement Without Giving In, Penguin Books, New York, 1981.

[10] A.D. Galinsky, T. Mussweiler, First offers as anchors: the role of perspective-taking and negotiator focus, Journal of Personality & Social Psychology 81 (2001) 657–669.

[11] A.D. Galinsky, Should You Make The First Offer? Negotiation (2004).

[12] V.L. Huber, M.A. Neale, Effects of cognitive heuristics and goals on negotiator performance and subsequent goal setting, Organizational Behavior & Human Decision Processes 38 (1986) 342–365.

[13] G. Kersten, Support for group decisions and negotiations, in: J. Climaco (Ed.), An Overview, in Multiple Criteria Decision Making and Support, Springer Verlag, Heidelberg, 1997.

[14] J.L. Kolodner, R.L. Simpson, The mediator: analysis of an early case-based problem solver, Cognitive Science 13 (1989) 507–549.

[15] R.M. Liebert, W.P. Smith, J.H. Hill, M. Keiffer, The effects of information and magnitude of initial offer on interpersonal negotiation, Journal of Experimental Social Psychology 4 (1968) 1231–1243.

[16] C.G. Lord, L. Ross, M.R. Lepper, Biased assimilation and attitude polarization: the effects of prior theories on subsequently considered evidence, Journal of Personality & Social Psychology 47 (1979) 2098–2109.

[17] S. Matwin, T. Szapiro, K. Haigh, Genetic algorithms approach to a negotiation support system, IEEE Transactions on Systems Man and Cybernetics 21 (1991) 129-140

[18] M.W. Morris, R.P. Larrick, S.K. Su, Misperceiving negotiation counterparts: when situationally determined bargaining behaviors are attributed to personality traits, Journal of Personality & Social Psychology 77 (1999) 52–67.

[19] G.B. Northcraft, M.A. Neale, Experts, amateurs, and real estate: an anchoring-andadjustment perspective on property pricing decisions, Organizational Behavior & Human Decision Processes 39 (1987) 84–97.

[20] M.A. Peterson, D. Waterman, Evaluating civil claims: an expert systems approach to evaluating product liability cases, in: C. Walter (Ed.), Computer Power and Legal Reasoning, West Publishing Company, 1985.

[21] D.G. Pruitt, P.J. Carnevale, Negotiation in Social Con<sup>fl</sup>ict, Brooks/Cole, Paci<sup>fi</sup>c Grove 1993.

[22] H. Raiffa, The Art and Science of Negotiation, Harvard University Press, Cambridge, MA 1982

[23] J.K. Sebenius, Negotiation analysis: a characterization and review, Management Science 38 (1992) 18–38.

[24] S. Siegel, N.J. Castellan, Nonparametric Statistics for the Behavioral Sciences, 2nd ED.McGraw-Hill New York NY 1998

[25] K.P. Sycara, Machine learning for intelligent support of con<sup>fl</sup>ict resolution, Decision Support Systems 10 (1993) 121–136.

[26] E.M. Thiessen, J.P. McMahon, Beyond win–win in cyberspace, Ohio State Journal on Dispute Resolution 15 (2000) 643.

[27] L. Thompson, Negotiation behavior and outcomes: empirical evidence and theoretical issues, Psychological Bulletin 108 (1990) 515–532.

[28] L. Thompson, D. Hrebec, Lose–lose agreements in interdependent decision making, Psychological Bulletin 120 (1996) 396–409.

[29] K.L. Valley, J. Moag, M.H. Bazerman, A matter of trust: effects of communication on the efficiency and distribution of outcomes Journal of Economic Behavior & Organization 34 (1998) 211.

[30] R.E. Walton, R.B. Mckersie, A Behavioral Theory of Labor Negotiations: An Analysis of a Social Interaction System, McGraw-Hill, New York, 1965.

[31] D.A. Waterman, J. Paul, M. Peterson, Expert systems for legal decision making Expert Systems 3 (1986) 212–226.

[32] Y. Yuan, B.J. Rose, N. Archer, H. Suarga, A Web-Based Negotiation Support System, EM-Electronic Markets 8. 1998.

[33] G.A. Yukl, Effects of situational variables an opponent concessions on a bargainer's perception, Aspirations, and Concessions, Journal of Personality & Social Psychology 29 (1974) 227–236.

[34] J. Zeleznikow, R. Meersman, D. Hunter, E. Van Helvoort, Computer tools for aiding legal negotiation, ACIS95-Sixth Australasian Conference on Information Systems, Curtin University of Technology, Perth, Western Australia, 1995.

![](/api/attachments/ZRGAEC87/fulltext/images/8d87de2edf839fc970fc95ab8ed29783d336d3330557962e7ba66afd5cccaddb.jpg)  
Sungsoon Park has been a Research Associate of Smeal College of Business at Penn State University. He also received his doctorate degree from Department of Indus trial and Manufacturing Engineering at Penn State University. His research focuses on the cognitive decision making, behavior negotiation strategy, display visualization and human performance modeling. He published in European Journal of Operational Research and several technical reports in the area. He is currently the member of the Institute of Industrial Engineers and Institute of Electrical and Electronics Engineers.

![](/api/attachments/ZRGAEC87/fulltext/images/930a635f3e1990489218117ace7fda04f4db7d068c9c9fbb93f0ed3e620599cc.jpg)

Gary Bolton is a Professor of Economics and Executive Programs Faculty Fellow at Penn State University. He is also the Director of the Laboratory of Economic Management and Auctions (LEMA). He received his Ph.D. from the Graduate School of Industrial Administration (now the Tepper School) at Carnegie Mellon University. His areas of expertise are decision making and design economics. Much of his recent work focuses on negotiation strategy and eliciting cooperative behavior. Proiects include a decisionsupport system for negotiators and the design of eBay's Feedback 2.0 system. Dr. Bolton publishes widely in economics and business literatures, with recent articles appearing in the American Economic Review, Management

Science, and Manufacturing and Service Operations Management. He has held visiting positions at the University of Cologne, Harvard Business School, Caltech, the Institute of Economic Analysis, Barcelona, and Chinese University of Hong Kong, among others. His research work is presently supported by the U.S. National Science Foundation.

![](/api/attachments/ZRGAEC87/fulltext/images/3f05534aafa75ef7f1d5c632f2402abd577c69105b8a8883ee3cca930a0a5d34.jpg)

Ling Rothrock has been a professor in the Harold and Inge Marcus Department of Industrial and Manufacturing Engineering at Pennsylvania State University since 2002. He served on the faculty at the Biomedical, Industrial, and Human Factors Department at Wright State University from 2000 to 2002. From 1995 to 2000, he served in the U. S. Army as an executive of<sup>fi</sup>cer in a maintenance company, a logistics of<sup>fi</sup>cer in support of an Air Defense Artillery brigade (PATRIOT), and a research scientist in the Army Research Laboratory.

Prof. Rothrock's research areas include human-in-the-loop discrete event simulations, display visualization, and human-machine performance evaluation. His simulation

![](/api/attachments/ZRGAEC87/fulltext/images/d6da66a61b704c75ef908495a5e360162ef816042e43dbc18d7f2bc0c818b759.jpg)

software has been used by the U.S. Navy for training and modeling. He has also been funded by the National Science Foundation to investigate decision strategies in dynamic tasks. He has published over 50 technical articles in the area and obtained over \$800,000 in external funding. Dr. Rothrock is an Associate Editor for the Institute of Electrical and Electronics Engineers Transactions on Systems, Man, and Cybernetics (Part A), the current president of the Computer and Information Systems Division of the Institute of Industrial Engineers and a member of the Human Factors and Ergonomics Society.

Jeannette Brosig is a Professor of Economics at the University of Duisburg-Essen, Germany. She is also the Director of the Essen Laboratory for Experimental Economics (elfe). She received her doctorate degree and her ‘Habilitation’ from the University of Magdeburg, Germany. Her research focuses on behavior in bilateral and multilateral negotiations as well as on the design of incentive systems. Among others, she published in Games and Economic Behavior, Experimental Economics, and Journal of Economic Behavior and Organization.
