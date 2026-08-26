---
otero_id: 688
otero_key: "HKQVDXH8"
title: "Detection of anomalous bids in procurement auctions"
authors: "P.L. Conti; M. Naldi"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.08.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Detection of anomalous bids in procurement auctions

P.L. Conti <sup>a</sup>, M. Naldi <sup>b,</sup>⁎

<sup>a</sup> Università di Roma “La Sapienza”, Dipartimento di Statistica, Probabilità e Statistiche Applicate, Piazzale Aldo Moro, Rome, Italy

<sup>b</sup> Università di Roma “Tor Vergata”, Dipartimento di Informatica, Sistemi e Produzione, Via del Politecnico 1, Rome, Italy

## a r t i c l e i n f o

Article history: Received 4 October 2007 Received in revised form 4 August 2008 Accepted 24 August 2008 Available online 3 September 2008

Keywords: Procurement Auctions Anomalous bids Statistical detection algorithms

## a b s t r a c t

Procurement auctions may be affected by abnormally low bids, whose acceptance may have negative consequences on the auctioneer. A method, based on the average submitted bid, is considered to detect such anomalous bids and aid the auctioneer in the possible rejection decision. Analytical expressions or simulation results are provided for the detection probability and for the false alarm probability. The performances heavily depend on the number of tenderers and on the dispersion of bid values. Both performance indices improve as the number of tenderers grows and generally degrade as the dispersion grows. The presence of multiple anomalous bids leads to a signi<sup>fi</sup>cant worsening of the performance, while courtesy bids raise both the false alarm probability and the detection probability. The use of the average-bid criterion, though of<sup>fi</sup>cially endorsed in national legislations, is therefore recommended as a strongly precautionary criterion, i.e. when the need to avoid anomalous bids is considered much more relevant than the costs associated to deeper investigation of anomalous bids or to the erroneous rejection of regular bids.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Procurement of goods, services, or public works is often accomplished by reverse auctions, where suppliers provide their competitive biddings to a buyer [7,8]. Each supplier indicates the minimum price at which it is willing to undertake the work or provide the goods/services. Through this competition auctions appear as an effective way of reducing prices for the buyer. Since the assignment is typically awarded to the supplier providing the lowest bid, each tenderer is spurred to provide the lowest possible bid, taking into account the expected level of competition and its expected rate of return (we assume anyway that competitors are not informed of the bids of one another, which could lead to forms of cheating as described in [27]). However, in some circumstances the behaviour of the tenderer may deviate from these guidelines. For example, it may be in desperate need of obtaining a contract, though it may turn into a <sup>fi</sup>nancial loss. Or it may aim at ousting a potential competitor (the phenomenon of predatory bidding [1]). In some cases it may even present a noncompetitive bid, i.e. a bid just a bit higher than the expected competitors so to have a very small probability of winning (the phenomenon of cover pricing), with the aim of staying in favour with the auctioneer by showing interest in the auction (hence such bids are also known as courtesy bids) [31]. In all these cases the tenderer presents an anomalous bid, whose value has been set by a line of reasoning different from that of regular competitors. Such anomalous bids represent a distortion in the regular execution of an auction. In particular, abnormally low bids, leading to awarding the contract to a supplier that could end up not providing the goods/services, are a cause of deep concern and have come to the attention of the European Union [13]. The negative consequences on the auctioneer's activity can be avoided if the anomalous bids are detected and their submitters subject to a deeper investigation, hence the need for a criterion to identify anomalous bids and support the auctioneer in the rejection decision. Decision support systems are an established tool to aid the auctioneer in auction operations such as this [25].

In the statistical literature observations that stand outside the bulk of the data (a characteristic common to both abnormally low bids and courtesy bids) are typically designated as outliers. Many statistical tests have been proposed for the general problem of identifying and removing outliers. Two surveys of such methods can be found in [2] and [34], while the most prominent one is described in the seminal paper by Grubbs [16,35]. In addition, some tests have been devised for the speci<sup>fi</sup>c purpose of detecting bids due to cover pricing (i.e. abnormally high) and have been examined e.g. in [19,30,31,33]. Instead a number of schemes, typically different from the ones above mentioned, have been introduced in the grey literature for the detection of abnormally low bids. Examples are the national regulations in Spain [20,21], Italy [28], Germany, and Turkey [37]. However, the introduction of these schemes has not been accompanied by a proper evaluation of their performances, namely of their capability to detect anomalous bids without declaring as anomalous otherwise regular bids (which we may call a false alarm).

In this paper we provide analytical expressions and simulation results for two performance indices of detection schemes: the detection probability and the false alarm probability. We focus on a class of detection schemes for abnormally low bids (hereafter we will use the generic term of anomalous bids), based on the use of the average bid. A particular version of such scheme has been of<sup>fi</sup>cially adopted by public bodies in Spain and Italy. Its relevance lies in its of<sup>fi</sup>cial endorsement, though it has so far escaped a proper evaluation. Some background information on procurement auctions is provided in Section 2, while the average-bid detection scheme itself is described in Section 5. The reference model for the bid distribution needed to perform our evaluation is provided in Section 3, while the performance indices are de<sup>fi</sup>ned in Section 4. The evaluation is <sup>fi</sup>nally conducted in Sections 6 (detection probability) and 7 (false alarm probability) for the case of a single anomalous bid. The case of multiple anomalous bids is instead studied in Section 8. In addition, the in<sup>fl</sup>uence of the presence of courtesy bids (abnormally high) on the detection of abnormally low bids is evaluated in Section 9.

## 2. Procurement auctions and anomalous bids

Auctions (actually reverse auctions) are now an established means of accomplishing procurement activities as opposed to negotiation or direct purchasing through catalogs [8]. In reverse auctions all tenderers provide their bid, indicating the minimum price at which they are willing to provide the goods or services up for auction. A number of auction formats have been devised, differing essentially for the way the auction is conducted and for the way the contract is awarded [17]. A well established format in procurement auctions is the sealed bid tendering, where all tenders are made known at the same time (for the purpose of this paper the terms tender and bid, and analogously tenderer and bidder, are considered synonymous). When the auction is based on price considerations only (e.g. because the required characteristics of the item up for auction have been well de<sup>fi</sup>ned and are therefore not a discriminant among different tenders) the contract is generally awarded to the tenderer submitting the lowest bid. Each bidder is then induced to submit the lowest bid it can under its <sup>fi</sup>nancial constraints (e.g. a minimum expected rate of return for its activities) and considering the expected competition from the other tenderers. The natural incentive to submit the lowest possible bid can however turn into an anomalous behaviour when the tendering company submits too low a bid. Such anomalous bids have received a considerable attention in the latest years, due to the distortion they introduce in the procurement activities. A precise de<sup>fi</sup>nition has also been attempted by the European Union, according to which a tender is assumed to be abnormally low if the following two conditions are met at the same time [13]:

i. In the light of the client's preliminary estimate and of all the tenders submitted, the tender seems to be abnormally low by not providing a margin for a normal level of pro<sup>fi</sup>t;

ii. The tenderer cannot explain its price on the basis of the economy of the construction method, or the technical solution chosen, or the exceptionally favourable conditions available to the tenderer, or the originality of the work proposed.

Several researchers have examined the reasons for such behaviour [1,5,10]. A list of possible reasons is reported below:

i. The bidder underestimates its cost (due to irrationality or bad performance of its budgeting department);

ii. The bidder expects to renegotiate the contract later, e.g. when it is too costly for the auctioneer to replace the winning company;

iii. The bidder's <sup>fi</sup>nancial conditions are very bad, leading it to use the awarded contract as a bridging opportunity (just surviving and waiting for better times), since the company's possible losses are upper bounded by the possibility of going bankrupt;

iv. The bidder may aim at ousting a competitor (a.k.a. predatory bidding).

If the procurement procedure allows so, the bidder, after submitting its bid, could recognize its mistake leading to an excessively low bid and revise its bid accordingly. A procedure including such second stage adjustment of bids has been proposed in [36]. Such mechanism, lying halfway between the sealed bid auction and the multiple rounds involved in a descending or ascending auction, doesn't seem to have been widely adopted and is not further considered here.

Whatever the reason for the abnormally low bid the contracting authority shall typically act in two stages, <sup>fi</sup>rst examining the distribution of bid values (and maybe comparing them with an expected cost basis) in order to detect the presence of anomalous bids, and then performing a deeper investigation of the tender labelled as anomalous. The second stage analysis will say if that bid is reasonable, i.e. supported by the actual operating conditioning of the tendering company, and lead to reject it if that's not the case. Such two-stage strategy is actually suggested by Article 55 of 2004 EU Directive [11], according to which “the contracting authority shall, before it may reject those tenders, request in writing details of the constituent elements of the tender which it considers relevant.” As an alternative to such reactive strategy, the auctioneer could have the auction preceded by a prequali<sup>fi</sup>cation phase, where prospective bidders are screened for the purpose of eliminating those that don't appear suf<sup>fi</sup>ciently reliable to perform the work if awarded the contract. Such prequali<sup>fi</sup>cation may be conducted by looking e.g. at the size and reputation of contractors, or at their previous participation at similar contests. However, if (as it happens) the prices requested in previously submitted bids are a screening variable, the prequali<sup>fi</sup>cation may result in those contractors submitting higher prices being eliminated rather than those submitting too low bids [9]. In the following we will not consider the presence of a prequali<sup>fi</sup>cation phase.

## 3. Bid distribution models

For the purpose of de<sup>fi</sup>ning and evaluating any statistical detection criterion we are compelled to use a working model for the distribution of bid values.

A simple model for distribution of costs rather than bid values is provided by Calveras [5], right in the context of abnormally low bids. In that model all the bidders have the same cost structure, so that the cost $C _ { \mathrm { P } }$ of the project under auction is made of two components: a deterministic one, which represents the knowledge common to all the tenderers, plus a random component

$$
C _ {P} = c + s.\tag{1}
$$

The random component s is modelled by a Bernoulli distribution: it takes the value $- k _ { G }$ with probability 1−p and the value $k _ { \mathrm { B } }$ otherwise. In order to result in positive bids the condition cN $k _ { \mathrm { G } }$ must of course hold. The overall cost is therefore again Bernoullian, with expected value

$$
E [ C _ {P} ] = (1 - p) (c - k _ {\mathrm{G}}) + p (c + k _ {\mathrm{B}}) = c + p (k _ {\mathrm{B}} + k _ {\mathrm{G}}) - k _ {\mathrm{G}}.\tag{2}
$$

Though the proposed distribution is asymmetric, a symmetric version, where $k _ { \mathrm { B } } = k _ { \mathrm { G } } ,$ , has also been proposed by the same authors in [4].

Starting from this cost model, a model can be derived for the bids by multiplying the cost by an expected rate of return, leading again to a Bernoulli model.

In a recent paper, in the context of an auction directed to a mass market rather than a procurement auction, the following larger set of probability models has been considered [23]:

– Uniform;

– Triangular;

– Gaussian;

– Exponential;

– Pareto.

In this set the <sup>fi</sup>rst three represent the case of bids clustered around a central value (dictated by the common cost structure). The exponential and Pareto distribution are instead representative of situations where signi<sup>fi</sup>cant differences exist among the bids, with lower bids being more likely than large ones (though quite large bids are possible). Though the range of models considered in the literature also extends to the Lognormal [3] and to the Weibull [24], the normal model appears to be the most appropriate, being supported by empirical data concerning the construction sector through the use of proper statistical tests [19,26,31]. In this paper we restrict to the case of the Gaussian model, which, in addition to being supported by statistical <sup>fi</sup>tting to empirical data, re<sup>fl</sup>ects a common cost structure, with differences among the bids related either to errors in the cost estimation and quotation or to small competitive advantages. In the following we consider two scenarios, named Scenario A and B. In Scenario A all the bids are regular (i.e. not anomalous). The N bids can therefore be considered as N i.i.d. (independent and identically distributed) random variables $X _ { 1 } , X _ { 2 } , . . . , X _ { N }$ following a common Gaussian distribution with expected value $\mu$ and standard deviation $\sigma ,$ so that the common distribution function is

$$
\begin{array}{l} F _ {X _ {1}} (x) = F _ {X _ {2}} (x) = \dots = F _ {X _ {N}} (x) \\ \qquad = P (\mu + Z \sigma <   x) = P \left(Z <   \frac {x - \mu}{\sigma}\right) = G \left(\frac {x - \mu}{\sigma}\right), \end{array}\tag{3}
$$

indicating by $Z \mathbf { a }$ standard Gaussian variable and by $G ( \cdot )$ the associated standard Gaussian cumulative distribution function.

In Scenario B instead just N−1 bids are regular, being represented by random variables $X _ { 1 } , X _ { 2 } , . . . , X _ { N - 1 }$ following the same Gaussian probability distribution as in Scenario A. Beside these regular bids there is one anomalous bid, represented by the random variable $X _ { N } ,$ which follows again a Gaussian distribution with identical standard deviation σ as the regular bids but with a (rebated) mean value, lowered by the rebating factor $\beta \colon$

$$
E [ X _ {N} ] = \beta \mu 0 <   \beta <   1,\tag{4}
$$

$$
F _ {X _ {N}} (x) = P (\beta \mu + Z \sigma <   x) = G \left(\frac {x - \beta \mu}{\sigma}\right).\tag{5}
$$

Fro the sake of completeness we note that though we have restricted to the i.i.d. case, as the vast majority of the literature, this need not be the case. For example in the seminal paper by Friedman a different probability distribution is envisaged for each competitor [14], though the resulting complexity of the problem leads the same author to go back to the concept of an average bidder and therefore to a single bid distribution.

## 4. Performance indices for detection methods

We need a criterion, embodied in a number of indices, to evaluate how good the detection method is in identifying the presence of anomalous bids.

For this purpose we can de<sup>fi</sup>ne the two states of nature (mutually exclusive) that can occur in the realization of a procurement auction: the state $H _ { 0 }$ where all the bids are regular and the state $H _ { 1 }$ where an anomalous bid (in the sense of abnormally low) is present. At <sup>fi</sup>rst we do not consider the case where multiple anomalous bids may be present, since, given the typically low number of participants, this should be a very rare event. In the language of Section 3 the state of nature $H _ { 0 }$ corresponds to Scenario A, while the state $H _ { 1 }$ corresponds to Scenario B.

The detection method focuses on the lowest bid and suggests one of two decisions: either considering it a regular bid and accepting it (decision $D _ { 0 } )$ or marking it as anomalous (decision $D _ { 1 } ) _ { \ d }$ , which in turn calls for its deep analysis and may lead to its rejection.

The combination of the two states of nature with two possible decision outcomes gives rise to four possible situations, of which two are correct and two are in error. The detection method is correct if the bids are all regular and none is marked as anomalous (state $H _ { 0 }$ and decision $D _ { 0 } )$ or, on the other hand, if an anomalous bid is present and is detected (state $H _ { 1 }$ and decision $D _ { 1 } ) .$ . Instead the detection method leads to wrong conclusions if the anomalous bid is not detected (state $H _ { 1 }$ and decision $D _ { 0 } )$ or if a regular bid is rejected (state $H _ { 0 }$ and decision $D _ { 1 } )$

We consider then two classical performance indices, associated to two of the previously described four situations and describing respectively a correct decision and an error condition:

– Detection Probability $P _ { \mathrm { d } } { = } P [ D _ { 1 } | H _ { 1 } ]$ , i.e. the probability of detecting the anomalous bid when present;

– False Alarm Probability $P _ { \mathrm { f a } } { = } P [ D _ { 1 } | H _ { 0 } ]$ , i.e. the probability of declaring a bid anomalous when all the bids are instead regular.

It is to be noted that the detection probability is evaluated under the hypothesis that an anomalous bid is actually present (Scenario B) and is the probability of detecting that anomalous bid. The false alarm probability has been evaluated under Scenario A as the probability of the event that a regular bid is smaller than the detection threshold. The probability values pertaining to the two remaining situations (i.e. the probability of missing an anomalous bid or of correctly declaring all the bids regular) can be easily recovered from the two cases just de<sup>fi</sup>ned as their complement to 1. A method shall perform the better the larger its $P _ { \mathrm { d } }$ and the lower its $P _ { \mathrm { f a } }$

Secondary requirements are that the detection method performance does not depend on the size of the auction (represented by the number of participants) and on the parameters of the bid distribution model (e.g. the variance of the bid distribution). In particular, in the absence of the latter requirement the detection method performance would not be predictable in advance of the auction realization. Instead, if the performance depends on the auction size, the problem can be partially circumvented by adjusting the discrimination parameter as a function of the number of participants.

## 5. The average-bid detection method

A detection method for anomalous bids can be devised based on the sampling average of all the bids that have been submitted in the auction. Namely we set a threshold T equal to some fraction α of the sampling average $\overbar { X }$ and compare each bid with this threshold. The ith bid $X _ { i }$ is declared anomalous (and therefore subject to further examination) if $X _ { i } { < } T { = } { \alpha } { \overline { { X } } } .$ The rationale is that in a regular context (i.e. free of anomalous bids) the average bid represents a rough indication of the common value attributed to the procurement item by the participants: a large deviation from the average bid may be due to reasons other than the common evaluation of the item's value. The only parameter to be chosen in the de<sup>fi</sup>nition of the detection method is the threshold coef<sup>fi</sup>cient α in the range (0–1): the larger it is the larger the probability of detecting a potential anomalous bid, but the method gets also more prone to false alarms.

A special interest in evaluating this average-bid criterion is due to its practical relevance, being of<sup>fi</sup>cially endorsed by at least two institutional bodies, in Spain and Italy.

In fact, the Spanish regulation considers as anomalous those bids lower than the average bid by at least 10% (i.e. α=0.9), when there are at least three participants [20,21]. In the case of two participants the criterion is formulated in an alternative way: a bid is anomalous if it is lower than the other by at least 25%. It is readily seen that this formulation can be expressed as an average-bid criterion with a different value for the thresholding coef<sup>fi</sup>cient. In fact, if we consider the bid $X _ { 1 }$ (the same can be obtained if we consider the other bid $X _ { 2 } )$ the condition for being considered anomalous is $X _ { 1 } { \leq } 0 . 7 5 X _ { 2 } .$ By adding 0.75X to both terms we get the alternative formulation

![](/api/attachments/HKQVDXH8/fulltext/images/3d96f163b4f714cd9534c8d4b4950581022a990e538349165ec9de7c606e612e.jpg)  
Fig. 1. Detection probability under an 80% rebating factor $\scriptstyle ( \alpha = 0 . 9 )$

$X _ { 1 } { \leq } 0 . 7 5 ( X _ { 1 } { + } X _ { 2 } ) / 1 . 7 5 ,$ , i.e. $X _ { 1 } { \le } \frac { 3 } { 7 } \overline { { X } } ,$ , which is the average-bid criterion with $\textstyle \alpha = { \frac { 3 } { 7 } } \simeq 0 . 4 2 9$

<sup>g</sup>Similarly, the Italian agency for public procurement CONSIP has set a criterion based on the maximum starting bid, which is the value assumed as a starting reference so that all tenderers can express their bids as rebates with respect to this reference value [12]. According to this criterion a bid is considered anomalous if it deviates more than 20% from the average rebate. Again, this criterion can be expressed and analysed on the basis of the average bid. If we indicate the discriminating rebating factor by γ, the rebate associated to the generic ith bid as $R _ { i } ,$ and the average rebate as <sup>¯¯</sup>R, the anomaly condition is $R _ { i } \ge ( 1 + \gamma ) \overline { { R } }$ . Since the rebate can be expressed through the associated bid and the starting reference value B by

$$
\begin{array}{l} R _ {i} = B - X _ {i}, \\ \overline {{R}} = B - \overline {{X}}, \end{array}\tag{6}
$$

the anomaly condition can be expressed through the bids rather than the rebate

$$
B - X _ {i} > (1 + \gamma) (B - \overline {{X}}) \rightarrow X _ {i} <   (1 + \gamma) \overline {{X}} - \gamma \beta \rightarrow X _ {i} + \gamma \beta <   (1 + \gamma) \overline {{X}},\tag{7}
$$

meaning that we can employ the same evaluation tools as for the average-bid criterion by setting $\alpha { = } 1 + \gamma$ and considering for the bid distribution a normal distribution $N ( \mu + \gamma \beta , \sigma ^ { 2 } )$ , i.e. replacing in all formulas $\mu \log \mu + \gamma \beta .$

## 6. Detection probability

We consider <sup>fi</sup>rst the possibility of correctly detecting the presence of an anomalous bid when there is one. Indicating by $\{ x _ { 1 } , . . . , x _ { N } \}$ the set of submitted bids (i.e. a realization of the random variables $X _ { 1 } , . . . , X _ { N } ) ,$ , a bid in that set is declared anomalous if it is smaller than the threshold αx.̄

Without loss of generality, for the purpose of evaluating the detection probability, we can suppose that the bids $\{ X _ { 1 } , . . . , X _ { N - 1 } \}$ are regular and the last one $X _ { N }$ is anomalous, i.e.

$$
X _ {1}, \dots , X _ {N - 1} \sim N (\mu , \sigma^ {2}),\tag{8}
$$

$$
X _ {N} \sim N (\beta \mu , \sigma^ {2}).\tag{9}
$$

The anomalous bid is detected if it is smaller than the threshold, so that the detection probability is

$$
P _ {\mathrm{d}} = P [ X _ {N} <   T ].\tag{10}
$$

If we express the detection threshold in the following way by isolating the contribution of the anomalous bid

$$
T = \alpha \overline {{X}} = \frac {\alpha}{N} \left(\sum_ {i = 1} ^ {N - 1} X _ {i} + X _ {N}\right),\tag{11}
$$

the detection probability can be in turn expressed by comparing the values of two independent quantities: the anomalous bid and the sum of the regular bids. In symbols:

$$
\begin{array}{c} P _ {\mathrm{d}} = P \bigg [ X _ {N} <   \frac {\alpha}{N} \sum_ {i = 1} ^ {N - 1} X _ {i} + \frac {\alpha}{N} X _ {N} \bigg ] \\ = P \bigg [ X _ {N} - \frac {\alpha}{N - \alpha} \sum_ {i = 1} ^ {N - 1} X _ {i} <   0 \bigg ]. \end{array}\tag{12}
$$

Taking into account the assumptions (8) and (9), and considering that a weighted sum of normal random variables is again a normal random variable, then the detection probability can be expressed as

$$
G \left[ \frac {\mu}{\sigma} \left(\alpha \frac {N - 1}{N - \alpha} - \beta\right) \left(\alpha^ {2} \frac {N - 1}{(N - \alpha) ^ {2}} + 1\right) \right]\tag{13}
$$

The resulting detection probability can be easily parametrized as a function of the coef<sup>fi</sup>cient of variation of the regular bids, i.e. the ratio $\sigma / \mu$ The detection probability will be larger the larger the argument of the standard normal probability distribution in Eq. (13), i.e. if $\scriptstyle \mathbf { \dot { \alpha } } \mathbf { > } \beta$ and if the coef<sup>fi</sup>cient of variation is small. Here we report the detection curve for one value of the threshold coef<sup>fi</sup>cient $\scriptstyle \alpha = 0 . 9 \ ( { \mathrm { i . e . } }$ the value adopted in the Spanish regulation), two different values for the rebating factor $\beta { = } 0 . 8 , 0 . 9$ , and some values for the number of bids in the typical range [3–20]. In these curves, shown respectively in Fig. 1 and in Fig. 2, we see that:

– the detection probability heavily depends on both the number of participants and the dispersion of their bids;

– the impact of bid dispersion gets stronger as the number of participants decreases;

– the range of values of the detection probability heavily depends on the rebating factor (it is always lower than 0.5 when $\beta { = } 0 . 9$ , but larger than 0.5 when $\beta { = } 0 . 8 )$

– the sign of the slope of the curve depends on the rebating factor (again changing when passing from β=0.8 to β=0.9).

As to the latter two points we can derive analytically the conditions under which the detection probability is a growing function of the coef<sup>fi</sup>cient of variation $m = \sigma / \mu$ In fact, in the argument of Eq. (13) the factor multiplying m turns negative if the following condition holds

$$
\beta > \alpha \frac {N - 1}{N - \alpha}.\tag{14}
$$

In this case the cumulative distribution function gets below 0.5 and becomes a decreasing function of the coef<sup>fi</sup>cient of variation. For the values at hand there is not a dominant factor between the thresholding coef<sup>fi</sup>cient α and the number of tenderers N. In fact, for $\alpha { = } 0 . 9$ the discriminating value of the rebating factor varies from 0.857 (when there are 3 participants) to 0.895 (when there are 20 participants), while if $\alpha { = } 0 . 8$ the window is slightly larger and shifts to the interval 0.7273÷0.7917.

![](/api/attachments/HKQVDXH8/fulltext/images/8dc5800876204bbad2aaf8cc4575360a0577e69986ed14a677332d0bf1f2b053.jpg)  
Fig. 2. Detection probability under a 90% rebating factor (α=0.9).

![](/api/attachments/HKQVDXH8/fulltext/images/10c169ac478e269dbcbb24364f08c634ba52e255781fa9351ebc3b095fb76e3c.jpg)  
Fig. 3. False alarm probability estimated by simulation (α =0.9).

## 7. False alarm probability

In order to evaluate the false alarm probability we consider Scenario A, where all the bids are regular. In this section we will provide <sup>fi</sup>rst the derivation of the exact expression for $P _ { \mathrm { f a } } .$ However, given the computational burden associated to it, we will provide an estimation of the false alarm probability by Monte Carlo simulation and an approximated analytical expression turning into quite a good approximation of the true value.

Denoting by $X _ { ( 1 ) }$ the random variable representing the minimum bid, i.e. the lowest order statistic, the false alarm probability can be expressed as

$$
P _ {\mathrm{fa}} = P \left[ X _ {(1)} <   \alpha \overline {{X}} \right].\tag{15}
$$

We now operate some transformations on this expression in order to use a few results provided in [22]. We make now the simplifying assumption (to be removed later) that the N bids are represented by i.i. d. random variables $Z _ { 1 } , Z _ { 2 } , . . . , Z _ { N }$ with a standard Gaussian distribution. We can then rewrite the expression providing $P _ { \mathrm { f a } }$ in the following way:

$$
\begin{array}{l} P _ {\mathrm{fa}} = P \big [ Z _ {(1)} <   \alpha \overline {{Z}} \big ] \\ \qquad = P \big [ Z _ {(1)} <   \alpha \overline {{Z}} + \overline {{Z}} - \overline {{Z}} \big ] \\ \qquad = P \big [ Z _ {(1)} <   \overline {{Z}} + (\alpha - 1) \overline {{Z}} \big ] \\ \qquad = P \big [ Z _ {(1)} - \overline {{Z}} <   (\alpha - 1) \overline {{Z}} \big ]. \end{array}\tag{16}
$$

By introducing the auxiliary variables $W _ { i } { = } { - } Z _ { i } i { = } 1 , 2 , . . . , N ,$ for which we have

$$
\begin{array}{c} W _ {(1)} = - Z _ {(N)}, \\ W _ {(N)} = - Z (1), \\ \overline {{W}} = - \overline {{Z}}, \end{array}\tag{17}
$$

the false alarm probability can be expressed in terms of the deviation of the maximum bid from the average one

$$
\begin{array}{l} P _ {\mathrm{fa}} = P \big [ Z _ {(1)} - \overline {{Z}} (\alpha - 1) \overline {{Z}} \big ] \\ \qquad = P \big [ - W _ {(N)} + \overline {{W}} - (\alpha - 1) \overline {{W}} \big ] \\ \qquad = P \big [ W _ {(N)} - \overline {{W}} > (\alpha - 1) \overline {{W}} \big ] \\ \qquad = 1 - P \big [ W _ {(N)} - \overline {{W}} <   (\alpha - 1) \overline {{W}} \big ]. \end{array}\tag{18}
$$

At this point we can use results in [22] which provided the following formula

$$
P \left[ W _ {(N)} - \overline {{{W}}} <   v \right] = \frac {\sqrt {N}}{\left[ \sqrt {2 \pi} \right] ^ {N - 1}} G _ {N - 1} (N v),\tag{19}
$$

where the G-functions de<sup>fi</sup>ned by Godwin [15] are employed:

$$
\begin{array}{l} G _ {0} (y) = 1, \\ G _ {r} (y) = \int_ {0} ^ {y} \exp \left[ - \frac {t ^ {2}}{2 r (r + 1)} \right] G _ {r - 1} (t) d t \quad r = 2, 3, \dots , N - 1. \end{array}\tag{20}
$$

Taking into account that $W _ { ( N ) } - { \overline { { W } } }$ is independent of $\overline { W }$ (the proof is reported in Appendix $\mathsf { A } ) ,$ , the false alarm probability is then

$$
\begin{array}{l} P _ {\mathrm{fa}} = 1 - P \big [ W _ {(N)} - \overline {{W}} <   (\alpha - 1) \overline {{W}} \big ] \\ = 1 - \frac {\sqrt {N}}{\Big (\sqrt {2 \pi} \Big) ^ {N - 1}} \int_ {- \infty} ^ {+ \infty} G _ {N - 1} [ N (\alpha - 1) w ] f _ {\overline {{W}}} (w) d w. \end{array}\tag{21}
$$

Removing the standard assumption the false alarm probability can be expressed as

$$
\begin{array}{l} P _ {\mathrm{fa}} = P \left[ X _ {(1)} <   \alpha \overline {{X}} \right] \\ \quad = P \left[ \mu + \sigma Z _ {(1)} <   \alpha (\mu + \sigma \overline {{Z}}) \right] \\ \quad = P \left[ Z _ {(1)} - \overline {{Z}} <   (\alpha - 1) \left(\frac {\mu}{\sigma} + \overline {{Z}}\right) \right]. \end{array}\tag{22}
$$

Performing the same steps as above we can write the equivalent of Eq. (18) for the general case:

$$
P _ {\mathrm{fa}} = 1 - P \left[ W _ {(N)} - \overline {{W}} <   (\alpha - 1) \left(\overline {{W}} - \frac {\mu}{\sigma}\right) \right].\tag{23}
$$

Now, after de<sup>fi</sup>ning the random variate

$$
U = (\alpha - 1) \left(\overline {{W}} - \frac {\mu}{\sigma}\right),\tag{24}
$$

which follows a Gaussian distribution with

$$
\begin{array}{l} \operatorname{E} [ U ] = (1 - \alpha) \frac {\mu}{\sigma}, \\ \operatorname{Var} [ U ] = \frac {(1 - \alpha) ^ {2}}{N}, \end{array}\tag{25}
$$

the false alarm probability for the non standard case is

$$
P _ {\mathrm{fa}} = 1 - \frac {\sqrt {N}}{(\sqrt {2 \pi}) ^ {N - 1}} \int_ {- \infty} ^ {+ \infty} G _ {N - 1} [ N u ] f _ {U} (u) d u.\tag{26}
$$

The dif<sup>fi</sup>culties in the use of Eq. (26) lie in the recursive computation of the G-functions, which can get very long-winded as the number of tenderers grows.

![](/api/attachments/HKQVDXH8/fulltext/images/38cc0dba0a2a8538297cdd2a00eb66d4f2f853a1b1b263fba7ddce6ce2b8a989.jpg)  
Fig. 4. False alarm probability by numerical approximation (α=0.9).

![](/api/attachments/HKQVDXH8/fulltext/images/70d042540c92cd08b3ff1bb9d5b117976decdb807fc4fdb34f9a873c5302ac48.jpg)  
Fig. 5. Detection probability under an 80% rebating factor (α=0.9) for multiple anomalous bids.

For this reason we <sup>fi</sup>rst turn to Monte Carlo simulation. We generate 100,000 auction instances, i.e. 100,000 sets of bids, extract the lowest among them for each instance, compare it with the detection threshold, and obtain the estimate of the false alarm probability as the proportion of times that the threshold is exceeded on the low side. The number of simulation runs (100,000) guarantees that the relative standard error (i.e. the coef<sup>fi</sup>cient of variation of the estimate) is smaller than 0.022 for all the cases examined. In Fig. 3 we report the results for a threshold coef<sup>fi</sup>cient $\alpha { = } 0 . 9$

As can be seen, the false alarm probability heavily depends on the dispersion of the bid values and is quite large, being even larger than the detection probability if the rebating factor is larger than 90%.

Another estimate of the false alarm probability can be obtained by replacing the sampling average in the general expression (15) by the average of the minimum and maximum bid (mid-range):

$$
P _ {\mathrm{fa}} \simeq P \left[ X _ {(1)} <   \alpha \frac {X _ {(1)} + X _ {(N)}}{2} \right] = P \left[ X _ {(1)} <   \frac {\alpha}{2 - \alpha} X _ {(N)} \right],\tag{27}
$$

which we can express by employing the order statistics pertaining to a set of i.i.d. standard Gaussian variables

$$
P _ {\mathrm{fa}} \simeq P \left[ \mu + \sigma Z _ {(1)} <   \frac {\alpha}{2 - \alpha} (\mu + \sigma Z _ {(N)}) \right] = P \left[ Z _ {(1)} <   2 \frac {\mu}{\sigma} \frac {\alpha - 1}{2 - \alpha} + \frac {\alpha}{2 - \alpha} Z _ {(N)} \right].\tag{28}
$$

Since the correlation between the minimum and the maximum bid is the weakest one among the correlations between any two order statistics, we proceed to compute this approximation of the false alarm probability as $\mathrm { i f } Z _ { ( 1 ) }$ and $Z _ { ( N ) }$ were independent:

$$
P _ {\mathrm{fa}} \simeq \int_ {- \infty} ^ {+ \infty} g _ {(N)} (s) G _ {(1)} [ h (s) ] d s.\tag{29}
$$

where $g _ { ( N ) } ( \cdot )$ and $G _ { ( 1 ) } ( \cdot )$ are respectively the probability density function of the maximum bid and the probability distribution function of the minimum bid, and h(s) is now the function

$$
h (s) = 2 \frac {\mu}{\sigma} \frac {\alpha - 1}{2 - \alpha} + \frac {\alpha}{2 - \alpha} s.\tag{30}
$$

By recalling the well known expressions [6]

$$
\begin{array}{l} g _ {(N)} (s) = N [ G (s) ] ^ {N - 1} g (s), \\ G _ {(1)} (s) = 1 - [ 1 - G (u (s)) ] ^ {N}. \end{array}\tag{31}
$$

the <sup>fi</sup>nal approximation for the false alarm probability is

$$
P _ {\mathrm{fa}} \simeq \int_ {- \infty} ^ {+ \infty} N [ G (s) ] ^ {N - 1} g (s) \left\{1 - [ 1 - G (h (s)) ] ^ {N} \right\} d s,\tag{32}
$$

which can be computed numerically. The results, for the same cases of Fig. 3, are plotted in Fig. 4.

The differences with the simulation data are quite limited (typically lower than 5% as the coef<sup>fi</sup>cient of variation exceeds 0.1), so that the resulting approximation can be retained as a useful one.

## 8. Performance in the presence of multiple anomalous bids

We have so far considered the presence of a single anomalous bid in a procurement lot, multiple anomalous bids being rather rare. However, in some cases they could actually occur. Detection devices for multiple outliers have appeared in the past in the literature, see e.g. [29] and [34]. We now consider that case in the context of the averagebid criterion. The expected effect on its performance is twofold: on one hand, detecting multiple anomalous bids is certainly more dif<sup>fi</sup>cult than detecting a single one; on the other hand, the more the anomalous bids the more the detection threshold is pushed downwards.

In order to perform a quantitative evaluation we rede<sup>fi</sup>ne Scenario B as follows:

Scenario B-bis Among the N bids $N { - } N _ { \mathrm { a } }$ are regular and $N _ { \mathrm { a } }$ are anomalous.

Without loss of generality, regular bids are identi<sup>fi</sup>ed by the lowervalued indices. Hence, for the values of the N bids we may write

$$
\begin{array}{l} X _ {i} \sim \mathrm{N} (\mu ; \sigma^ {2}) \quad i = 1, \ldots , N - N _ {\mathrm{a}} \\ X _ {i} \sim \mathrm{N} (\beta \mu ; \sigma^ {2}) \quad i = N - N _ {\mathrm{a}} + 1, \ldots , N \end{array}\tag{33}
$$

Accordingly, we now de<sup>fi</sup>ne the probability of detecting all the anomalous bids

$$
P _ {\mathrm{d}} = \mathbb {P} \left[ \min _ {N - N _ {\mathrm{a}} + 1 \leq i \leq N} X _ {i} <   T \right],\tag{34}
$$

where the threshold is

$$
T = \frac {\alpha}{N} \sum_ {i = 1} ^ {N} X _ {i}\tag{35}
$$

Since the false alarm probability is evaluated under the hypothesis that all the bids are regular (Scenario A as de<sup>fi</sup>ned in Section $^ { 3 ) , }$ this metric is unaffected by the presence of multiple anomalous bids. In what follows we therefore con<sup>fi</sup>ne ourselves to evaluate the detection probability, resorting to simulation. For each of the cases reported here, we have used $^ { - } 1 0 ^ { 5 }$ simulation instances. We report the values obtained for the following case:

– Number of bids $N = 2 0$

– Number of anomalous bids $N _ { \mathrm { a } } { = } 2 , 3$

– Threshold coef<sup>fi</sup>cient $\alpha { = } 0 . 9$

– Rebating factor $\beta { = } 0 . 8 , 0 . 9$

![](/api/attachments/HKQVDXH8/fulltext/images/23d626bd9b23c01c795d2deebc6259b8d1a77f73418d14794c0fe3a4c01291b2.jpg)  
Fig. 6. Detectionprobability under a 90% rebating factor (α=0.9) for multiple anomalous bids.

![](/api/attachments/HKQVDXH8/fulltext/images/94f2a10556eb4857b16c1bd55b337b8634ba0a4a630ef3a4ea6672f357488d20.jpg)  
Fig. 7. Detection probability under a 90% rebating factor in the presence of courtesy bids.

In Figs. 5 and 6 the detection curves pertaining respectively to $\beta { = } 0 . 8$ and $\beta { = } 0 . 9$ are shown. For a better comparison, we also report the curve pertaining to a single anomalous bid case.

As expected the detection performance worsens and $P _ { \mathrm { d } }$ dramatically decays when a second anomalous bid is added. We observe the same effect of the coef<sup>fi</sup>cient of variation and the rebating factor: when the rebating operated by anomalous bids is very small (e.g. $\beta { = } 0 . 9$ or even closer to 1), the detection probability grows slightly as the bids get more dispersed, staying however in the region well below 0.5 due to the low value of the threshold coef<sup>fi</sup>cient α. Although not shown here, similar curves are obtained for a lower number of bidders. Three anomalous bids out of 20 are already enough to get the detection probability of limited use.

## 9. Impact of courtesy bids

In some cases regular bids are also accompanied by courtesy (a.k.a. as cover or complimentary) bids, i.e. bids which are submitted in order to stay in favour with the auctioneer by appearing to be interested in obtaining the contract. As explained in [31] such bids are not intended to be competitive and are typically produced by adding some percent on the top of a regular bid. Since they are produced to appear “similar” to regular bids, they should be nearly undetectable by the auctioneer. In [31] a detection criterion for them is proposed. Here we are interested in the effect they have on the average-bid method to detect anomalous bids. Since courtesy bids are typically larger than regular bids, the net effect of their presence in a procurement lot is to raise the detection threshold, hence raising at the same time both the false alarm probability and the detection probability. An additional negative consequence of the presence of courtesy bids (which we shall not further examine here) is the distortion they introduce in bidding models used to predict the probability of winning the auction [32].

![](/api/attachments/HKQVDXH8/fulltext/images/8af33d5cdfda7a21cf1cf96c36522f87e63753b7005c0cfd52b90b0530c19a25.jpg)  
Fig. 8. Detection probability under an 80% rebating factor in the presence of courtesy bids.

In this section we perform a quantitative evaluation of the impact of courtesy bids on the two performance indices so far considered. For this purpose we introduce two modi<sup>fi</sup>ed scenarios:

Scenario A-ter Among the N bids, $N { - } N _ { \mathrm { c } }$ are regular and $N _ { \mathrm { c } }$ are courtesy ones.

Scenario B-ter Among the N bids, $N { - } N _ { \mathrm { c } } { - } 1$ are regular, $N _ { \mathrm { c } }$ are courtesy ones, and there is a single anomalous bid.

As to the distribution of courtesy bids, following [31] we assume that they have the same probability distribution as the regular one (i.e. normal) but with a shifted mean value. Again, without loss of generality, we can mark the regular bids by the lower-valued indices. We have then for the values of the N bids in Scenario A-ter

$$
\begin{array}{l} X _ {i} \sim N (\mu ; \sigma^ {2}) i = 1, \ldots , N - N _ {\mathrm{c}} \\ X _ {i} \sim N (\gamma \mu ; \sigma^ {2}) i = N - N _ {\mathrm{c}} + 1, \ldots , N, \end{array}\tag{36}
$$

where γ is the shifting factor. Instead, in Scenario B-ter we have

$$
\begin{array}{l l} X _ {i} \sim N (\mu ; \sigma^ {2}) & i = 1, \ldots , N - N _ {\mathrm{c}} - 1 \\ X _ {i} \sim N (\gamma \mu ; \sigma^ {2}) & i = N - N _ {\mathrm{c}}, \ldots , N - 1 \\ X _ {N} \sim N (\beta \mu ; \sigma^ {2}) \end{array}\tag{37}
$$

The performance indices are accordingly de<sup>fi</sup>ned as

$$
\begin{array}{l} P _ {\mathrm{fa}} = \mathbb {P} [ X _ {N} <   T ] \\ P _ {d} = \mathbb {P} \bigg [ \min _ {i} X _ {i} <   T \bigg ] \end{array}\tag{38}
$$

and evaluated in Scenarios A-ter and B-ter, respectively. The detection threshold used in both cases is

$$
T = \frac {\alpha}{N} \sum_ {i = 1} ^ {N} X _ {i}\tag{39}
$$

We evaluate <sup>fi</sup>rst the detection probability. Using the same approach as in Section 6, the following expression is obtained

$$
\begin{array}{l} P _ {\mathrm{d}} = \mathbb {P} \left[ X _ {N} <   \frac {\alpha}{N} \left(\sum_ {i = 1} ^ {N - N _ {\mathrm{c}} - 1} X _ {i} + \sum_ {j = N - N _ {\mathrm{c}}} ^ {N - 1} X _ {j} + X _ {N}\right) \right] \\ = \mathbb {P} \left[ X _ {N} <   \frac {\alpha}{N - \alpha} \left(\sum_ {i = 1} ^ {N - N _ {\mathrm{c}} - 1} X _ {i} + \sum_ {j = N - N _ {\mathrm{c}}} ^ {N - 1} X _ {j}\right) \right] \\ = G \left[ \frac {\mu}{\sigma} \left(\alpha \frac {N - N _ {\mathrm{c}} - 1 + \gamma N _ {\mathrm{c}}}{N - \alpha} - \beta\right) \left(1 + \alpha^ {2} \frac {N - 1}{(N - \alpha) ^ {2}}\right) ^ {- 1 / 2} \right] \end{array}\tag{40}
$$

In Figs. 7 and 8, the impact of courtesy bids is shown in the following cases:

– Number of bids N=20

– Number of courtesy bids $N _ { \mathrm { c } } { = } 1 , \ : \mathrm { z }$ 5

![](/api/attachments/HKQVDXH8/fulltext/images/7b97d20e9a7bfb80b98f36916463821df22fb696a65e30a224a01cdc4b1cc42d.jpg)  
Fig. 9. False alarm probability in the presence of courtesy bids (10 bids)

![](/api/attachments/HKQVDXH8/fulltext/images/5b0ecf5cec6bff5b2252605e58a3aafe5ab3a4443c3eafc4eff954161a35d796.jpg)  
Fig. 10. False alarm probability in the presence of courtesy bids (20 bids).

– Threshold coef<sup>fi</sup>cient $\alpha { = } 0 . 9$

– Rebating factor $\beta { = } 0 . 8 , 0 . 9$

– Shifting factor $\gamma = 1 . 2$

As far as the latter parameter is concerned, we use here a quite large value on purpose. Although in [31] shifting factors of a few percent points are envisaged, and large values such as those used here would be probably detected (e.g. by the use of the method presented in the same [31]), here we want to examine the “worst case” of courtesy bids. If they were very close to the regular ones, they would have a negligible effect on the detection of anomalous bids. Figs. 7 and 8 show a direct comparison between the probability values obtained in the presence of courtesy bids and those obtained when all the bids are regular (Scenario A, with $N = 2 0 )$ . In the absence of any effect the values should be unaltered (e.g. in Fig. 8 we should have a straight line bisecting the diagram).

The effect of such courtesy bids would be noticeable, especially for lower rebating cases (i.e. β nearer to 1).

To evaluate the false alarm probability we proceed by simulation, again with $1 0 ^ { 5 }$ instances and the following parameters:

– Number of bids $N = 1 0 , 2 0$

– Number of courtesy bids $N _ { \mathrm { c } } = 1 , 2$

– Threshold coef<sup>fi</sup>cient $\alpha { = } 0 . 9$

– Shifting factor γ=1.2

The resulting curves are reported in Figs. 9 and 10. The performance metric is plotted again in the presence of courtesy bids vs. the case where all bids are regular. The increase of the false alarm probability is particular relevant for small values of the probability (and for small values of the number of bidders). Courtesy bids have controversial effects on the performance of the average-bid criterion: they raise the probability of detecting anomalous bids but also increase the occurrence of false alarms.

## 10. Conclusions

An average bid based method has been presented for the detection of abnormally low bids in procurement auctions. Two performance indices have been selected for its evaluation: the detection probability and the false alarm probability, whose dependence on the number of tenderers, the dispersion of bids, and the rebating factor of the anomalous bid has been investigated. A large number of participants has always a positive effect on the performance of the method. Instead, a larger dispersion of bids contributes to lower the detection probability as long as it is larger than 0.5. It is generally to be noted that the method may be affected by a large proportion of false alarms. However, if multiple anomalous bids are present (even just three) the performance worsens signi<sup>fi</sup>cantly. On the other hand, the presence of courtesy bids increases both the detection probability and the false alarm probability. Since a large number of false alarms results in a cost associated to the further investigation work and may give rise to unjusti<sup>fi</sup>ed rejection of low but regular bids (which increases the price for the auctioneer), the method is recommended when the need to avoid anomalous bids is much more relevant than the costs associated to false alarms.

## Appendix A. Proof of independence between sampling average and extreme deviation from sampling average

The independence between $\overline { W }$ and $W _ { ( N ) } - \overline { { W } }$ is a consequence of Basu's theorem. In fact, observe <sup>fi</sup>rst that the distribution of $\dot { W } _ { ( N ) } { - } \overline { { W } } =$ $( W _ { ( N ) } - \mathbb { E } [ W ] ) - ( { \overline { { W } } } - \mathbb { E } [ W ] )$ is independent of the parameter E W , i.e. $\dot { W } _ { ( N ) } { - } \overline { { W } }$ is ancillary for μ. Since W<sup>¯¯¯</sup> is a suf<sup>fi</sup>cient and complete statistics for E W (see p. 43 of [18]), from Basu's theorem (see p. 42 of [18]) it follows that $W _ { ( N ) } - { \overline { { W } } }$ and W<sup>¯¯¯</sup> are independent.

## References

[1] G. Alexandersson, S. Hulten, Predatory bidding in competitive tenders: a Swedish case study, European Journal of Law and Economics 22 (1) (2006) 73.

[2] R.J. Beckman, R.D. Cook, Outlier…s, Technometrics 25 (2) (May 1983) 119.

[3] K. Brown, A theoretical and statistical study of decision making under uncertainty— a competitive bidding for leases of offshore petroleum tracts, Ph.D. thesis, Southern Methodist University (1966).

[4] A. Calveras, J.-J. Ganuza, E. Hauk, Las bajas temerarias en las subastas de obras publicas. Un analisis de la regulacion española, Hacienda Publica 162 (2002) 135.

[5] A. Calveras, J.-J. Ganuza, E. Hauk, Wild bids. Gambling for resurrection in procurement contracts, Journal of Regulatory Economics 26 (2004) 41.

[6] H. David, Order Statistics, J. Wiley, New York, 1970.

[7] E. David, R. Azoulay-Schwartz, S. Kraus, Bidding in sealed-bid and English multiattribute auctions, Decision Support Systems 42 (2) (2006) 527.

[8] N. Dimitri, G. Piga, G. Spagnolo (Eds.), Handbook of Procurement, Cambridge University Press, Cambridge, 2006

[9] D.S. Drew, M.R. Skitmore, Prequali<sup>fi</sup>cation and c-competitiveness, OMEGA: International Journal of Management Science 21 (3) (1993) 363.

[10] A. Engel, Essays on risk management in procurement auctions, Ph.D. thesis, Friedrich-Alexander-Universität Erlangen-Nürnberg, Wirtschatfs- und Sozialwissenschaftliche Fakultät (2005).

[11] European Parliament, Directive 2004/18/EC on the coordination of the procedures for the award of public works contracts, public supply contracts and public service contracts, March 31 2004.

[12] European Union Public Procurement Learning Lab and Working Group on auction design and competitive issues, An exploratory analysis of public procurement practices in Europe, December 2004.

[13] European Union Working Group on the Prevention Detection and elimination of Abnormally Low Tenders in the European Construction Industry, Abnormally low tenders, 1999.

[14] L. Friedman, A competitive-bidding strategy, Operations Research 4 (1) (February 1956) 104.

[15] H. Godwin, On the distribution of the estimate of mean deviation obtained from samples from a normal population, Biometrika 33 (1945) 254

[16] F.E. Grubbs, Sample criteria for testing outlying observations, The Annals of Mathematical Statistics 21 (1) (March 1950) 27.

[17] P. Klemperer, Auctions: Theory and Practice, Princeton University Press, Princeton, 2004

[18] E.L. Lehmann, G. Casella, Theory of Point Estimation, II Ed.Springer Verlag, New York, 1998.

[19] R. McCaffer, A. Pettitt, Distribution of bids for buildings and roads contracts, Operations Research Quarterly 27 (4) (1976) 835.

[20] Ministerio de Hacienda de España, Ley de contratos de las administraciones públicas, Boletín O<sup>fi</sup>cial del Estado, vol. no. 148, June 21 2000.

[21] Ministerio de Hacienda de España, Reglamento general de la ley de contratos de las administraciones públicas, Boletín O<sup>fi</sup>cial del Estado, vol. no. 257, October 26 2001.

[22] K. Nair, The distribution of the extreme deviate from the sample mean and its studentized form, Biometrika 35 (1/2) (1948) 118.

[23] M. Naldi, G. D'Acquisto, Performance of the Vickrey auction for digital goods under various bid distributions, Performance Evaluation 65 (1) (January 2008) 10.

[24] S. Oren, M. Rothkopf, Optimal bidding in sequential auctions, Operations Research 23 (6) (1975) 1080.

[25] M.P. Papazoglou, A. Tsalgatidou, Business to business electronic commerce issues and solutions Decision Support Systems 29 (4) (2000) 301.

[26] T.H. Pin, W. Scott, Bidding model for refurbishment work, Journal of Construction Engineering and Management 120 (2) (May/June 1994) 257.

[27] R. Porter, Y. Shoham, On cheating in sealed-bid auctions, Decision Support Systems 39 (1) (2005) 41.

[28] Presidente della Repubblica Italiana D. Lgs, 163/2006 Codice dei contratti pubblici relativi a lavori servizi e forniture in attuazione delle direttive 2004/17/CE e 2004/ 18/CE Suppl, ordinario n. 107 della Gazzetta Ufficiale n. 100 (2 May 2006).

[29] B. Rosner, On the detection of many outliers, Technometrics 17 (2) (May 1975) 221.

[30] M. Skitmore, Graphical method for identifying high outliers in construction contract auctions, The Journal of the Operational Research Society 52 (7) (July 2001) 800.

[31] R. Skitmore, Identifying non-competitive bids in construction contract auctions, OMEGA: International Journal of Management Science 30 (6) (2002) 443.

[32] M. Skitmore, Predicting the probability of winning sealed bid auctions: the effects of outliers on bidding models, Construction Management & Economics 22 (1) (2004) 101.

[33] R.M. Skitmore, H.P. Lo, A method for identifying high outliers in construction contract auctions, Engineering Construction and Architectural Management 9 (2) (2002) 90.

[34] G.L. Tietjen, The analysis and detection of outliers, in: R.B. D'Agostino, M.A. Stephens (Eds.), Goodness-of-<sup>fi</sup>t Techniques, vol. ch. 12, Marcel Dekker, Inc., 1986, p. 497.

[35] G.L. Tietjen, R.H. Moore, Some Grubbs-type statistics for the detection of several outliers, Technometrics 14 (3) (August 1972) 583.

[36] F. Van Cauwelaert, E. Heynig, Correction of bidding errors: the Belgian solution, Journal of the Construction Division, vol. 105 (CO1), American Society of Civil Engineers, March 1979, p. 13.

[37] M. Zanza, Final Presentation of the works of the CONSIP Working Group on Auction Design and Competitive Issues, Rome, December 13 2004.

Pier Luigi Conti graduated from the Rome University “La Sapienza” in Statistics, in 1988; he received a Ph.D. in Statistics in 1992. In the period 1992–1998 he was Researcher in Statistics at the Rome University “La Sapienza”; in 1998 he moved to the University of Bologna as Associate Professor of Statistics. Since 2000, he is Full Professor of Statistics at the Rome University “La Sapienza”. Dr. Conti published about 50 papers in international journals and proceedings of international conferences. His main interests are: nonparametric statistics, statistical inference for queueing models, sampling theory and techniques.

Maurizio Naldi was born in Palermo in 1963. He graduated cum laude in 1988 in Electronic Engineering at the University of Palermo and then received his Ph.D. in Telecommunications Engineering from the University of Rome at Tor Vergata. After graduation he pursued an industrial career, <sup>fi</sup>rst at Selenia (now Alenia) as a radar designer (1989–1991), and then in the Network Planning Departments of Italcable (1991–1994), Telecom Italia (1995–1998), and WIND (1998–2000) where he was appointed Head, Traf<sup>fi</sup>c Forecasting & Network Cost Evaluation Group. Since 2000 he is with the University of Rome at Tor Vergata, where he is now Aggregate Professor. He is the author of more than 100 scienti<sup>fi</sup>c publications. He is a Senior Member of IEEE, and a member of AEI, SIS, and MAA.
