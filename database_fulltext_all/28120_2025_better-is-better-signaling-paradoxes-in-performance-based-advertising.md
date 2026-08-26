---
otero_id: 28120
otero_key: "55K585HS"
title: "Better Is Better? Signaling Paradoxes in Performance-Based Advertising"
authors: "Ran Pan; Juan Feng"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.0419"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Better Is Better? Signaling Paradoxes in Performance-Based Advertising

Ran Pan,<sup>a</sup> Juan Feng<sup>b,</sup>\*

<sup>a</sup> International Institute of Finance, School of Management, University of Science and Technology of China, Anhui 230026, China;

<sup>b</sup> Department of Management Science and Engineering, School of Economics and Management and Shenzhen International Graduate School, Tsinghua University, Beijing 100190, China

\*Corresponding author

Contact: rpan@ustc.edu.cn, https://orcid.org/0000-0002-7563-779X (RP); fengjuan@sem.tsinghua.edu.cn, https://orcid.org/0000-0002-0548-1531 (JF)

Received: August 17, 2021 Revised: July 19, 2022; June 17, 2023; January 28, 2024 Accepted: May 8, 2024 Published Online in Articles in Advance: July 31, 2024

https://doi.org/10.1287/isre.2021.0419

Copyright: © 2024 INFORMS

Abstract. Advertising signaling theory shows that costly advertising can serve as a credible signal of product quality (hereafter ad-signal), provided that the effectiveness of advertising can be accurately measured. The rise of performance-based advertising, in which advertising is paid based on consumer actions, such as clicking on or purchasing through an ad link, presents challenges in measuring the effectiveness of advertising. Specifically, it becomes difficult to differentiate whether a consumer’s action is caused by ad-signal or the inherent product appeal. This leads to a critical question: how does this inaccuracy in evaluating advertising effectiveness affect the signaling role of advertising? This research analyzes how the inherent product reputation and the breadth of ad-signal reach impact the signaling role of advertising, uncovering two paradoxes under performance-based advertising: a higher product reputation does not necessarily help advertising to signal product quality (product reputation paradox), and a broader ad-signal reach can impede the signaling role of advertising (ad-signal reach paradox). We propose modified payment schemes to address both paradoxes. These insights contribute to advertising signaling theory and offer practical guidance for designing effective payment schemes under performance based advertising.

Funding: This work was supported by the National Natural Science Foundation of China [Grants 72301265, 72171132].

Keywords: signaling theory • signaling paradox • performance-based advertising • product reputation • ad-signal reach

CPA, or cost per action, is the Holy Grail for targeted advertising. —Marissa Mayer, former president and CEO of Yahoo! and long-time Google executive

## 1. Introduction

Advertising signaling theory demonstrates that costly advertising can credibly signal product quality, hereafter ad-signal. Because consumers are more likely to repurchase high-quality products than lower quality ones, it is challenging for a low-quality product seller to afford the expensive advertising cost of the high-quality product seller (e.g., Nelson 1970, 1974; Kihlstrom and Riordan 1984; Milgrom and Roberts 1986; Sahni and Nair 2020). As information technologies have made it possible to measure and record consumer actions following advertising, performance-based advertising has become widely adopted in recent years, under which firms only pay for consumer actions following an ad link, such as pay per click, pay per call, and pay per sale (e.g., Hu 2004, Animesh et al. 2010, Liu et al. 2010, Yang and Ghose 2010, Dellarocas 2012, Xu et al. 2012, Liu and Viswanathan 2014, Hu et al. 2016, Sun et al. 2020).

This innovative approach, although welcomed by advertisers, imposes challenges in preserving the signaling ability of advertising. Specifically, a consumer’s action following the advertisement can result from (1) the ad’s effectiveness in signaling product quality or (2) the inherent appeal of the product. If the measure of advertising performance cannot differentiate the sources of these actions, it creates noise in evaluating the ad’s overall effectiveness.

This persistent noise inherent in performance-based advertising has already been highlighted in the literature. For instance, Blake et al. (2015) demonstrate that search engine marketing (SEM) had minimal effectiveness for well-known companies such as eBay, whereas Coviello et al. (2017) show that SEM expenditures can be more efficient for less well-known companies. In practice, when a digital advertising platform charges advertisers based on the number of clicks, it tends to display ads with high predicted click probabilities, introducing noise into the evaluation of advertising effectiveness (Gordon et al. 2021). More specifically, through a field experiment involving 200,000 users across 13 Asian cities and more than 600 local restaurants, Sahni and Nair (2020) reveal a crucial insight: the effectiveness of advertising in signaling product quality significantly increases when the product lacks an established reputation. This demonstrates that product reputation can be a source of noise when evaluating the effectiveness of advertising signals.

How critical is the problem? Aral (2021) documents cases with up to a 4,100% overestimation in advertising performance for brand search ads, underscoring the magnitude of these discrepancies. Whereas metrics such as click-through and purchase rates provide insights into advertising impact, they do not differentiate between the influence of product reputation and the effectiveness of the ad-signal itself, nor do they clarify whether consumers make purchases because of the ad-signal or the inherent appeal of the product. This inevitably influences the signaling role of advertising under the performance-based scheme.

In this paper, we develop a theoretical framework to study the intricate interplay between product reputation, ad-signal reach, and the signaling role of advertising under the performance-based scheme. Our model introduces two key factors: a product reputation factor, measuring the product’s performance in making sales without ad-signal, and an ad-signal reach factor, evaluating the outreach potential of the advertising signal. Specifically, we extend traditional signaling literature, which assumes that the advertising signal impacts all consumers uniformly, by considering three types of consumers based on whether they are influenced by the advertising signal or product reputation: (1) consumers who are influenced by the product reputation regardless of the advertising signal; (2) consumers who are not influenced by the product reputation, but are influenced by the advertising signal; and (3) consumers who are influenced by neither the product reputation nor the advertising signal.

Why do our results diverge from previous studies? Intuitively, one might believe that a higher reputation product would easily signal its quality through advertising because of a larger base of loyal customers. However, our analysis reveals two paradoxes: a higher product reputation does not always aid the highquality firm in signaling its product quality through advertising (product reputation paradox), and a larger adsignal reach can impede advertising’s signaling ability (ad-signal reach paradox). This crucially hinges on how advertising payment is calculated, in which mixing product and advertising performance inflates signaling costs for a product with a high reputation even in more effective advertising outlets.

Practically, this study highlights the vital role of information technologies in precisely evaluating advertising performance under performance-based payment schemes. It offers valuable insights for platforms to design effective advertising payment schemes, aiding advertisers in delivering quality signals to consumers and adjusting advertising strategies in the realm of performance-based advertising.

The remainder of the paper is organized as follows: We review the related literature in Section 2. We introduce the benchmark model in Section 3. In Section 4, we analyze how different payment schemes affect the signaling paradoxes. In Section 5, we present our conclusions and future directions.

## 2. Literature Review

This section provides an overview of the related literature and how this study builds on and extends various streams of research.

## 2.1. Signaling Theory

Our research contributes to signaling literature, which aims to solve information asymmetry problems in online transactions and posits that effective signals can help high-quality firms/goods differentiate themselves from low-quality ones (e.g., Nelson 1970, 1974; Mil grom and Roberts 1986; Zhao 2000; Guo and Jiang 2016; Jiang et al. 2016; Sahni and Nair 2020). These signals can take many forms, such as advertising (Sahni and Nair 2020), reputation (Hollenbeck 2018), price (Guo and Jiang 2016), and website quality (Wells et al. 2011). These studies focus on whether a factor can signal qual ity, whereas our study explores how product reputation and ad-signal reach interact to impact signal ability.

A significant stream in signaling theory concerns the idea that costly advertising serves as a credible signal because low-quality firms cannot cover the cost of advertising if they mimic the behavior of high-quality firms (Nelson 1970, 1974; Kihlstrom and Riordan 1984; Milgrom and Roberts 1986). However, these studies assume that advertising signal can reach all potential consumers and only consider new products without an established reputation. In contrast, this study relaxes these assumptions and investigates the impact of product reputation and ad-signal reach on signaling functions.

## 2.2. Online Advertising

Internet-based advertising is a related area of research explored by several studies. Notably, some studies examine the design of keyword auction mechanisms employed by major advertising platforms such as Google, Yahoo!, and Microsoft, including works by Liu et al. (2010), Zhang and Feng (2011), Xu et al. (2012),

Arnosti et al. (2016), Chen (2017), Sayedi (2018), Balseiro and Gur (2019), Zeithammer (2019), and Despotakis et al. (2021). Whereas both the design of keyword auction mechanisms and the signaling theory of advertising are significant facets of online advertising, they have different focuses. The present study focuses on the signaling theory of advertising, highlighting two signaling paradoxes that are underexplored in the previous literature and providing techniques to resolve these paradoxes.

Furthermore, this study relates to performance-based advertising, which is popular in the industry and widely studied in academia (Hu 2004, Animesh et al. 2010, Yang and Ghose 2010, Dellarocas 2012, Hu et al. 2016). However, previous studies on performance-based advertising have not considered advertising signaling theory. Feng and Xie (2012) fill this gap by exploring how performance-based advertising can signal quality. Differently, our study primarily focuses on the influence of product reputation and ad-signal reach on the signaling theory of advertising.

## 2.3. Product Reputation

The literature on product reputation extensively examines the role of brand names in communicating unobservable qualities to consumers in line with signaling theory. Scholars such as Kihlstrom and Riordan (1984), Erdem and Swait (1998), Kirmani and Rao (2000), and Erdem et al. (2006) show that brand reputation can serve as a signal of high quality. Specifically, Erdem et al. (2006) demonstrate the credibility of brands as a signal of quality in a cross-country validation study. These findings suggest that products with higher reputations are better equipped to signal their quality.

Our study explores the impact of product reputation on the signaling theory of advertising and highlights the potential cost of advertising for high-quality products that attract purchases from loyal consumers. Our results extend the previous literature on brands signaling quality, building on the work of Kihlstrom and Riordan (1984), who examine the effect of reputation on signaling theory. Different from their focus on two special cases, we consider the general condition of product reputation and explore how its magnitude influences signaling theory. We also introduce two modified advertising payment schemes and explore how they affect the signaling function.

## 2.4. Advertising Reach

Many researchers study advertising reach, highlighting various factors that can enhance advertising reach, such as advertising repetition (e.g., Campbell and Keller 2003, Ghose and Yang 2009, Todri et al. 2020) and crowdedness (Andrews et al. 2016). Our study contributes to this literature by exploring how the signal reach of advertising can affect the signaling theory of advertising.

In summary, this study extends traditional signaling theory by examining how product reputation and ad-signal reach impact signaling effectiveness. Our findings provide theoretical explanations for existing empirical studies about advertising signaling and highlight the conditions for the disclosure effect in advertising as identified by Sahni and Nair (2020). Additionally, we offer insights into how the signaling function of advertising can be influenced by quality differences between products. Our work sheds new light on the complex relationship between product reputation, ad-signal reach, and advertising signaling theory.

## 3. Model Setup

Consider a company selling a product with a quality level $q \ ( { \mathrm { w h e r e } } \ q \in \{ { \hat { H } } , L \}$ and $0 < \bar { L } < H \leq 1 )$ in two periods. To consumers, the true quality level is unknown and could be either H or L with equal probability. Below, we specify the demand derivation for each period.

## 3.1. The First Period Demand

In the first period, consumers decide whether to purchase the product based on their expected utility, defined as $u = \theta \bar { Q _ { } } - { \cal P } ,$ , where (1) $Q \left( Q \in \{ \hat { H } , L \} \right)$ ) represents consumers’ perceived quality in the first period; (2) θ, consumers’ willingness to pay (WTP) for the perceived quality, is uniformly distributed over [0, R], that is, $\theta \sim { \bar { U } } [ 0 , { \dot { R } } ] ;$ and (3) P is the product price. A consumer purchases in the first period if and only if the consumer’s expected utility is positive. This implies that only consumers with $\theta > \dot { P } / Q$ make the purchase.

Considering the influence of product reputation and ad-signal reach on consumers’ perceived quality levels, we categorize consumers into three types:

1. Type-A consumers, who are influenced by the product reputation and perceive the product quality as H $( \mathrm { i . e . , ~ } Q = H )$ regardless of the advertising signal. Therefore, the utility function for Type-A consumers is $u _ { A } = \theta H - P$ . The proportion of Type-A consumers increases in the product reputation and the true quality levels (q). Define $\beta ~ ( 0 \leq \beta < 1 / H )$ as the product reputation factor such that βq percent of consumers are Type-A. The demand from Type-A consumers in the first period, $D _ { A } ^ { q }$ (depicted as the $\hat { D } _ { A } ^ { q }$ areas in Figure 1), can be represented by

$$
D _ {A} ^ {q} = \beta q (R - \mathrm{P/H}).
$$

2. Type-B Consumers are unaffected by product reputation. In a separating equilibrium, they perceive the product quality as high $\left( \mathrm { i . e . , ~ } Q = H \right)$ because they observe the advertising signal.<sup>2</sup> Therefore, the utility function for Type-B consumers is $u _ { B } = \theta H - P$ . The proportion of $\bar { \mathrm { T y p e } } { \cdot } \mathrm { B }$ consumers increases with the ad-signal reach. We define $\eta \left( \eta \geq 0 \right)$ as the ad-signal reach factor, which also represents the proportion of

Figure 1. (Color online) First Period Demand: without Ad-signal (Left) and with Ad-signal (Right)  
![](/api/attachments/55K585HS/fulltext/images/8c962160adb063a7b2bab2a0fae205500092dd437295893928bef1de87697301.jpg)

Type-B consumers. Then, the demand from Type-B consumers in the first period, $D _ { B }$ (depicted as the $D _ { B }$ area in the right-hand panel of Figure 1), can be represented by

$$
D _ {B} = \eta (R - P / H).
$$

3. Type-C consumers: The remainder of consumers are Type-C, who remain unaffected by either the product reputation or the advertising signal. They perceive the product quality as low $( \mathrm { i . e . , } Q = L ) , ^ { 3 }$ so the utility function for Type-C consumers is $u _ { C } = \theta L - P _ { \cdot }$ . In the first period, denote the demand generated by Type-C consumers without and with ad-signal as $\dot { D } _ { c } ^ { \bar { q } }$ and ${ \ddot { D } } _ { c } ^ { q } ,$ respectively, depicted as $\dot { D } _ { c } ^ { q }$ and $\ddot { D } _ { c } ^ { \ q }$ areas in Figure 1. Then,

$$
\left\{ \begin{array}{l l} \dot {D} _ {c} ^ {q} = (1 - \beta q) (R - P / L), & \text { without   ad - signal } \\ \ddot {D} _ {c} ^ {q} = (1 - \beta q - \eta) (R - P / L), & \text { with   ad - signal }. \end{array} \right.
$$

By aggregating the first period demand from all consumer types in the market (noting that Type-B consumers exist only when ad-signal is present), we calculate the overall first period demand, denoted as $\dot { D } _ { 1 } ^ { q }$ without ad-signal and $\ddot { D } _ { 1 } ^ { \dot { q } }$ with ad-signal,

$$
\left\{ \begin{array}{l l} \dot {D} _ {1} ^ {q} = D _ {A} ^ {q} + \dot {D} _ {c} ^ {q}, & \text { without   ad - signal } \\ \ddot {D} _ {1} ^ {q} = D _ {A} ^ {q} + D _ {B} + \ddot {D} _ {c} ^ {q}, & \text { with   ad - signal }. \end{array} \right.\tag{1}
$$

## 3.2. The Second Period Demand

In the second period, consumers who did not purchase the product in the first period will not purchase in the second period, either. Among the consumers who purchased in the first period, Type-A consumers are loyal to the product and will certainly repurchase, implying that the second period demand from Type-A consumers remains to be $D _ { A } ^ { q }$

In contrast, Type-B and Type-C consumers are not loyal. In the second period, following Milgrom and Roberts (1986), we assume that only a fraction $q$ of Type-B and Type-C consumers who purchased in the first period will be satisfied and make a repeat purchase. Then, the second period demand from Type-B consumers is $q D _ { B } ,$ , and that from Type-C consumers is qD<sup>q</sup><sub>c</sub> .

![](/api/attachments/55K585HS/fulltext/images/84dc24ec2a00ae1b96461c5eeb2b9b4039275adf5b4d0d271e5f50819e8732fc.jpg)

The overall second period demand, denoted as $\dot { D } _ { 2 } ^ { q }$ without ad-signal and $\ddot { D } _ { 2 } ^ { q }$ with ad-signal, can be calculated by summing up the second period demand across all consumer types, respectively,

$$
\left\{ \begin{array}{l l} \dot {D} _ {2} ^ {q} = D _ {A} ^ {q} + q \dot {D} _ {c} ^ {q}, & \text { without   ad - signal } \\ \ddot {D} _ {2} ^ {q} = D _ {A} ^ {q} + q D _ {B} + q \ddot {D} _ {c} ^ {q}, & \text { with   ad - signal }. \end{array} \right.\tag{2}
$$

In this study, we focus on the scenario in which all three customer types coexist, characterized by the condition $0 < \eta \leq 1 - \beta H$

## 3.3. The Total Demand

Summing up Equations (1) and (2), we derive the total demand over the two periods. Here, $\dot { D } _ { s } ^ { q }$ denotes the demand without ad-signal, and $\ddot { D } _ { s } ^ { q }$ denotes the demand with ad-signal:

$$
\left\{ \begin{array}{l l} \dot {D} _ {s} ^ {q} = 2 D _ {A} ^ {q} + (1 + q) \dot {D} _ {c} ^ {q}, & \text { without   ad - signal } \\ \ddot {D} _ {s} ^ {q} = 2 D _ {A} ^ {q} + (1 + q) (D _ {B} + \ddot {D} _ {c} ^ {q}), & \text { with   ad - signal }. \end{array} \right.\tag{3}
$$

## 3.4. The Firm’s Gross Profit

Let $C _ { q }$ represent the cost of producing a product with quality $q . ^ { \overset { - } { 4 } }$ Denote the firm’s gross profit without and with ad-signal as $\dot { \pi } ( \beta , \eta ; q )$ and π¨ $\left( \beta , \eta ; q \right)$ , respectively. Thus,

$$
\dot {\pi} (\beta , \eta ; q) = (P - C _ {q}) \dot {D} _ {s} ^ {q}.\tag{4}
$$

$$
\ddot {\pi} (\beta , \eta ; q) = (P - C _ {q}) \ddot {D} _ {s} ^ {q}.\tag{5}
$$

The total advertising expenditure is then

$$
A (a; q) = a \ddot {D} _ {s} ^ {q},\tag{6}
$$

where a represents the per-unit advertising expenditure.<sup>5</sup> The table in Appendix A summarizes the notation we use in this model.

## 3.5. Signaling Function

Advertising can serve as a signal if and only if a separating equilibrium exists such that the high-quality firm benefits from signaling through advertising, whereas the low-quality firm cannot cover the advertising expenditure from mimicry. That is, $\exists a > 0 ,$ , such that

$$
\left\{ \begin{array}{l} \ddot {\pi} (\beta , \eta ; H) - A (a; H) > \dot {\pi} (\beta , \eta ; H), \\ \ddot {\pi} (\beta , \eta ; L) - A (a; L) \leq \dot {\pi} (\beta , \eta ; L). \end{array} \right.\tag{7}
$$

By plugging Equations (4)–(6) into Equation (7), we can derive the condition required for advertising to signal as stated in Lemma 1.

## 4. Model Results

## 4.1. Signaling Paradox

Lemma 1 (Separating Equilibrium). Advertising can signal quality if and only if there exists an $a > 0$ such that

$$
\frac {\ddot {\pi} (\beta , \eta ; L) - \dot {\pi} (\beta , \eta ; L)}{\ddot {D} _ {s} ^ {L}} \leq a <   \frac {\ddot {\pi} (\beta , \eta ; H) - \dot {\pi} (\beta , \eta ; H)}{\ddot {D} _ {s} ^ {H}}.\tag{8}
$$

Plugging Equations (3)–(5) into Equation (8), we derive that a separating equilibrium exists if and only $\begin{array} { r } { i f f _ { N } ( \beta , \eta ) < \frac { ( P - C _ { H } ) ( 1 + H ) } { ( P - C _ { L } ) ( 1 + L ) } , } \end{array}$ where $f _ { N } ( \beta , \eta ) = \frac { \left( 2 \beta H + \eta H + \eta \right) \left( R - P / H \right) + \left( 1 + H \right) \left( 1 - \beta H - \eta \right) \left( R - P / L \right) } { \left( 2 \beta L + \eta L + \eta \right) \left( R - P / H \right) + \left( 1 + L \right) \left( 1 - \beta L - \eta \right) \left( R - P / L \right) } .$

Lemma 1 specifies the conditions under which advertising can signal quality in the context of performancebased advertising, taking into account the influence of both the product reputation and the ad-signal reach. To delve deeper into this, we investigate the precise impacts of product reputation and ad-signal reach on the signaling function of advertising as follows.

Proposition 1 (Product Reputation Paradox). A higher reputation factor $( \beta )$ makes it more difficult for the highquality firm to effectively signal through advertising except when $\bar { ( R - P / L ) } \bar { ( 1 + L ) } ^ { \sim } > \breve { 2 } \big ( R - P / \breve { H ) } / ( 1 + H )$

This paradox arises because of the existence of Type-A (loyal) customers. Specifically, a higher product reputation leads to more sales from loyal consumers, which should be attributed to the product reputation, but instead they are attributed to the advertising performance. The highquality firm is, therefore, penalized by having to spend more on advertising. Consequently, a more strict condition for a separating equilibrium is required, a phenomenon we call the product reputation paradox.

However, when $\big ( R - P / L \big ) ( 1 + L ) > 2 \big ( R - P / H \big ) / ( 1$ + H), the number of loyal customers for the low-quality firm approaches that of the high-quality firm. A higher β increases the advertising cost for the low-quality firm to signal quality without increasing profit to the same degree. So it becomes easier for the high-quality firm to deter the low-quality firm from imitation.

Proposition 1 makes two contributions: it extends traditional signaling theory by incorporating product reputation and provides theoretical explanations for existing empirical observations regarding the product reputation paradox. Proposition 1 aligns with the empirical finding in Sahni and Nair (2020), who demonstrate that the dis closure effect in advertising is more pronounced when the product reputation factor (β) is lower. In the context of restaurant visits, this could be caused by (1) consumers using the platform away from their typical city of search, (2) high uncertainty about the quality of a restau rant, and (3) restaurants having received few ratings in the past. This paradox suggests that advertising is more effective in signaling product quality when the product has a lower reputation.

This finding aligns with prior research, such as Kihlstrom and Riordan (1984), which indicates that an established reputation can adversely affect the signal ing role of advertising. Moreover, our study extends the literature by identifying specific conditions under which this negative impact occurs, offering a framework to elucidate the underlying mechanisms, particularly in evaluating advertising performance. These insights serve as the foundation for proposing modifications to the performance-based advertising scheme as discussed in Section 4.2.

Proposition 2 (Ad-signal Reach Paradox). Broader adsignal reach (η) requires more strict conditions for advertising to signal product quality except when $\left( R - P / L \right)$ $( \tilde { 1 + } L ) < \bar { 2 } \big ( R - { P } / { H } \big ) / ( \tilde { 1 } + \bar { H ( ) }$

Proposition 2 reveals a counterintuitive outcome: broader ad-signal reach may diminish the effectiveness of advertising as a signal of product quality under performance-based advertising. Intuitively, this occurs because the measured performance of advertising includes actions from both initial purchases and repeat purchases. This increases the cost of signaling through advertising for the high-quality product as ad-signal reaches more consumers (a higher η), leading to a larger number of repurchases. Consequently, a broade ad-signal reach makes it more challenging for the high quality firm to effectively signal its product quality through advertising, a phenomenon we call the adsignal reach paradox. It is worth noting that Proposition 4 provides a thorough demonstration of the underlying reasons for this paradox.

However, when there is a substantial quality gap between high- and low-quality products $\left( \mathrm { i . e . , ~ } \hat { \left( R - P / L \right) } \right)$ $( 1 + L ) < 2 \bar { \big ( } R - P / H \big ) / ( \bar { 1 + H } ) \bar { ) }$ , as the ad-signal reach increases, the high-quality firm can enhance its sales more efficiently through advertising compared with the low-quality firm. As a result, it becomes easier for the high-quality firm to successfully signal its product quality.

Corollary 1 (β and η Affect the Existence of a Separating Equilibrium). A separating equilibrium exists if and only if both the product reputation factor (β) and the ad-signal reach factor (η) are not excessively large (i.e., $\beta < \overline { { \beta } }$ and $\eta < \overline { { \eta } } )$ , where $\overline { { \beta } }$ and η are specified in Appendix B.

Corollary 1 explores the impact of the product reputation paradox and the ad-signal reach paradox, showing that higher product reputation or ad-signal reach can impede the signaling ability of advertising. Specifically, if the product reputation or ad-signal reach attains sufficiently high levels (when $\beta \in ( \overline { { \beta } } , 1 / H )$ or $\eta \in ( \overline { { \eta } } , 1 - \beta H ) )$ advertising no longer effectively signals quality. Assuming that the product reputation factor or ad-signal reach factor follows a uniform distribution (i.e., $\beta \sim U [ 0 , 1 / H ]$ or $\eta \sim U [ 0 , 1 - \beta H ] )$ , the likelihood that advertising fails to signal is $\scriptstyle \left( { \frac { 1 } { H } } - { \overline { { \beta } } } \right) ^ { - } { \frac { 1 } { H } } = 1 - { \overline { { \beta } } } H$ or $( 1 - \beta H - \overline { { \eta } } ) / ( 1 - \beta H )$

This particular case (when $\beta > \overline { { \beta } } \ : \mathrm { o r } \ : \eta > \overline { { \eta } } )$ aligns with the findings of Feng and Xie (2012), who discovered that advertising cannot signal product quality when repeat purchases are excessively weighted in advertising performance assessments. Moreover, Corollary 1 extends previous studies that assume ad-signal reaches all potential consumers $( \mathrm { e . g . }$ ., Nelson 1970, 1974; Kihlstrom and Riordan 1984; Milgrom and Roberts 1986; Feng and Xie 2012) by allowing the possibility that some consumers are not exposed to, or aware of, the advertising signal. It also identifies two additional factors that hinder the signaling ability of performancebased advertising, namely, the product reputation paradox and the ad-signal reach paradox.

## 4.2. Modifications in the Advertising Payment Scheme

So far, we have assumed that, under the performancebased advertising scheme, the firm needs to pay for every action regardless of whether the action is caused by the ad-signal or the product reputation. Propositions 1 and 2 demonstrate that this payment scheme can undermine the signaling ability of a high-quality product because of the product reputation paradox or adsignal reach paradox. In this section, we discuss the modifications to the advertising scheme.

4.2.1. Scheme I: Do Not Charge Sales from Loyal Consumers and Repeat Purchases. We demonstrate that (i) the product reputation paradox arises because sales from Type-A (loyal) customers are counted as advertising performance (Proposition 1) and (ii) the ad-signal reach paradox arises when repeat purchases are also included in the advertising performance (Proposition 2). To address these paradoxes, it is necessary to exclude sales from both loyal customers and repeat purchases when counting the advertising performance. As technologies such as web page cookies, customer relationship management systems, and big data analytics can track and record these actions, we propose scheme I that only charges the advertiser for purchases that are not affected by the product reputation in the first period:

$$
A _ {I} (a; q) = a _ {I} (\ddot {D} _ {1} ^ {q} - D _ {A} ^ {q}), q \in \{H, L \}.\tag{9}
$$

That is, $A _ { I } ( a ; q ) = a _ { I } ( D _ { B } + \ddot { D } _ { c } ^ { q } ) , q \in \{ H , L \}$ . Here, $A _ { I }$ and $a _ { I }$ denote the total advertising expenditure and the perunit advertising expenditure in scheme I, respectively. Plugging Equation (9) into Equation (7), we solve fo the separating equilibrium.

Lemma 2 (Scheme I Separating Equilibrium). Under scheme I, advertising can signal quality if and only if there exists an $a _ { I } > 0$ such that

$$
\frac {\ddot {\pi} (\beta , \eta ; L) - \dot {\pi} (\beta , \eta ; L)}{D _ {B} + \ddot {D} _ {c} ^ {L}} \leq a _ {I} <   \frac {\ddot {\pi} (\beta , \eta ; H) - \dot {\pi} (\beta , \eta ; H)}{D _ {B} + \ddot {D} _ {c} ^ {H}}.\tag{10}
$$

Plugging Equations (4) and (5) into Equation (10), we derive that a separating equilibrium exists $i f$ and only if $f _ { I } ( \beta , \eta )$ $\begin{array} { r } { < \frac { ( P - C _ { H } ) ( 1 + H ) } { ( P - C _ { L } ) ( 1 + L ) } , } \end{array}$ , where $\begin{array} { r } { f _ { I } \big ( \beta , \eta \big ) = \frac { \eta \big ( R - P / H \big ) + \big ( 1 - \beta H - \eta \big ) \big ( R - P / L \big ) } { \eta \big ( R - P / H \big ) + \big ( 1 - \beta L - \eta \big ) \big ( R - P / L \big ) } . } \end{array}$

We now investigate the impacts of product reputation and ad-signal reach on the signaling function of advertising in the modified scheme I.

Proposition 3 (Scheme I Resolves the Product Reputation Paradox). Under scheme I, the product reputation paradox is resolved. Furthermore, the higher $\beta ,$ the easier it is to signal quality through advertising.

Proposition 3 reveals that the modified payment scheme addresses the product reputation paradox. Specifically, advertising becomes less costly for the high quality firm than for the low-quality firm if sales from loyal customers are excluded when counting advertising performance regardless of the quality difference between the high- and low-quality products. This confirms our finding that the inclusion of sales from loyal consumers results in the product reputation paradox (as shown in Proposition 1).

Proposition 4 (Scheme I Cannot Resolve the Ad-signal Reach Paradox). Under scheme I, the ad-signal reach paradox cannot be resolved.

Proposition 4 demonstrates that the ad-signal reach paradox persists even when sales from Type-A consumers (depicted as area $A _ { 0 }$ in Figure 2) and repurchases are excluded. In scheme I, only the sales from Type-B and Type-C consumers are considered:

1. For Type-C consumers, those who have a high WTP (i.e., $\overset { \mathrm { ~ \ i ~ } } { P } / L < \theta < R )$ would purchase the product even if the perceived product quality is low (depicted as area $C _ { 0 }$ in Figure 2) as their expected utility is positive $( \theta L - P > 0 )$ . Therefore, their purchases should not be counted in advertising performance measurement.

Figure 2. (Color online) First Period Demand with Adsignal  
![](/api/attachments/55K585HS/fulltext/images/c2bf6df59cc9492b502f0067466ae07dc2d7b6b348c555b80add4eee764db859.jpg)  
Consumers' WTP for PerceivedQuality(θ)

2. The counting of sales from Type-B consumers, specifically those who have a high WTP $\left( \mathrm { i . e . , ~ } P / L \right.$ $< \theta < R )$ , is more intricate. On one hand, these sales should not be counted because these consumers would make the purchase even if their perceived product quality is low in the absence of advertising (because of $ { \dot { \theta } } \dot { L } - P > 0 .$ , depicted as area $B _ { 0 }$ in Figure 2); on the other, these sales should be counted because advertising has effectively altered these consumers’ perception of the product quality to high quality (H).

However, despite the aforementioned negative impact on the signaling ability of advertising because of the counting of advertising performance, including these sales from Type-B and Type-C consumers, can enhance the signaling ability of advertising because the low-quality firm has to pay more advertising expenses for these sales than the high-quality firm does, that is, $a \big ( 1 - \beta L \big ) \big ( R - P / L \big ) > a \big ( 1 - \beta \dot { H } \big ) ( R - P / L )$ This positive effect, however, diminishes when the adsignal reach (η) is high as the high-quality firm has to pay more to signal its product quality (i:e:, η(P=L � $P / H )$ when η increases. As a result, a high ad-signa reach (η) still hinders the signaling ability of advertising under scheme I.

Proposition 4 indicates that including sales from consumers with a high WTP plays a significant role in the ad-signal reach paradox. Based on this finding, we propose scheme II, which aims to address the ad-signal reach paradox by excluding these sales.

4.2.2. Scheme II: Charge Only for Incremental Sales Generated by the Advertising. Recall that Propositions 2 and 4 show that the ad-signal reach paradox exists because of what is counted when measuring the advertising performance. We propose scheme II, which counts only the incremental sales brought by the advertising signal in the first period (depicted as area $B _ { 1 }$ in

Figure 2) as shown in Equation (11):

$$
A _ {I I} (a; q) = a _ {I I} (\ddot {D} _ {1} ^ {q} - \dot {D} _ {1} ^ {q}), q \in \{H, L \}.\tag{11}
$$

Here, $A _ { I I }$ and $a _ { I I }$ denote the total advertising expenditure and the per-unit advertising expenditure in scheme II, respectively. In this scheme, not only the sales from loyal consumers (impacted by product reputation) and consumers with high WTP, but also the sales in the second period are excluded from the advertising performance measurement. In this way, more loyal consumers, more repeat purchases, or a higher ad-signal reach no longer make advertising more expensive for the high-quality firm. Plugging Equation (11) into Equation (7), we solve for the separating equilibrium.

Proposition 5 (Scheme II Separating Equilibrium). Under scheme II, advertising can signal quality if and only if there exists an $a _ { I I } > 0$ such that

$$
\frac {\ddot {\pi} (\beta , \eta ; L) - \dot {\pi} (\beta , \eta ; L)}{\ddot {D} _ {1} ^ {L} - \dot {D} _ {1} ^ {L}} \leq a _ {I I} <   \frac {\ddot {\pi} (\beta , \eta ; H) - \dot {\pi} (\beta , \eta ; H)}{\ddot {D} _ {1} ^ {H} - \dot {D} _ {1} ^ {H}}.\tag{12}
$$

Plugging Equations (1), (4), and (5) into Equation (12), we derive that a separating equilibrium exists if and only if $\frac { ( p - c _ { H } ) ( 1 + H ) } { ( p - c _ { L } ) ( 1 + L ) } > 1$

Proposition 5 reveals that, by counting only the sales generated by advertising in the first period, a separating equilibrium exists if and only $\begin{array} { r } { \mathrm { i f } \ \frac { ( p - c _ { H } ) ( 1 + H ) } { ( p - c _ { L } ) ( 1 + L ) } > 1 } \end{array}$ , in which case neither of the two paradoxes exist. This echoes our findings in Proposition 4: to effectively modify both paradoxes, the advertising payment scheme should exclude not only sales from repurchases, but also sales driven by product reputation and sales from consumers who have a high WTP. This payment scheme requires the platform to be able to infer the firm’s sales with and without ad-signal in the first period, however. In reality, accurately measuring the performance without ad-signal requires the sharing of information between the firm and the platform, which makes it difficult to implement this scheme.

## 5. Conclusion

As information technologies make it possible to accurately track and record consumer actions following advertising, performance-based advertising has become widely adopted because advertisers only need to pay for associated actions. This paper shows that, however, merely counting all actions into the performance of advertising may lead advertisers to pay for actions that should not be attributed to advertising. As a result, a higher reputation of the high-quality firm or a broader ad-signal reach by the advertising outlet can both make it more difficult for a high-quality firm to signal its product quality.

This paper makes a first attempt to articulate the impact of various methods of counting advertising performance on the signaling ability of advertising under performance-based advertising. We identify two paradoxes, the reputation paradox and the ad-signal reach paradox, and discuss different modification schemes to address these paradoxes.

Our study extends existing literature on advertising signaling, which traditionally focuses on new products without an established reputation and assumes that adsignal reaches every potential consumer (e.g., Nelson 1970, 1974; Kihlstrom and Riordan 1984; Milgrom and Roberts 1986; Feng and Xie 2012). In practice, however, some new products, such as the latest generation of the iPhone, may already have an established reputation, and different advertising outlets may have varying adsignal reaches. By acknowledging that not all consumers are reached by the advertising signal and recognizing the presence of loyal consumers regardless of the impact of the advertising signal, we are able to derive richer insights into performance-based advertising.

Our study also offers platforms with valuable insights for designing effective payment schemes that more accurately quantify advertising performance. Furthermore, it offers practical guidelines for advertisers on how to adjust their advertising strategies to more effectively convey quality signals to consumers under a performancebased advertising scheme.

Our research is not without limitations. First, our study focuses on the signaling paradoxes of performance-based advertising without specifically studying the auction mechanisms. Future research could extend this model to explore how auction pricing and competition might impact advertising signaling strategies. Second, in this study, the product price is exogenously given. It would be interesting to endogenize the price decision and examine how the two signaling levers, price and advertising, are influenced by product reputation and ad-signal reach.

## Acknowledgments

The authors thank the senior editor and anonymous reviewers, especially the first reviewer, for their careful examination of the manuscript and invaluable comments and suggestions, which substantially improved the paper.

Appendix A. Table of Notations

<table><tr><td>Notation</td><td>Definitions</td></tr><tr><td>i</td><td>Index for periods. i = 1, 2 represents the first and the second period, respectively.</td></tr><tr><td>q</td><td>Product true quality level, which takes two values, H and L, where 0 &lt; L &lt; H ≤ 1. For simplicity, we express this as q ∈ {H, L}.</td></tr><tr><td>Q</td><td>The perceived quality of the product, Q ∈ {H, L}</td></tr><tr><td>θ</td><td>Consumer&#x27;s willingness to pay for the perceived quality (i.e., WTP), θ ~ U[0, R]</td></tr><tr><td>P</td><td>Price for the product</td></tr><tr><td>u</td><td>Consumer&#x27;s expected utility in the first period, u = θQ - P</td></tr><tr><td>β</td><td>Product reputation factor, β &gt; 0</td></tr><tr><td>η</td><td>Ad-signal reach factor, 0 &lt; η ≤ 1 - βH</td></tr><tr><td>a</td><td>Per-unit advertising fee</td></tr><tr><td>A</td><td>Total advertising fee</td></tr><tr><td> $D_A^q$ </td><td>Type-A consumers&#x27; demand for the q product in the first period</td></tr><tr><td> $D_B$ </td><td>Type-B consumers&#x27; demand for the H (or L) product in the first period</td></tr><tr><td> $\dot{D}_c^q$ </td><td>Type-C consumers&#x27; demand for the q product in the first period without ad-signal</td></tr><tr><td> $\ddot{D}_c^q$ </td><td>Type-C consumers&#x27; demand for the q product in the first period with ad-signal</td></tr><tr><td> $\dot{D}_i^q$ </td><td>The demand for the q product in the period i without ad-signal</td></tr><tr><td> $\ddot{D}_i^q$ </td><td>The demand for the q product in the period i with ad-signal</td></tr><tr><td> $\dot{D}_s^q$ </td><td>The total demand for the q product over two periods without ad-signal</td></tr><tr><td> $\ddot{D}_s^q$ </td><td>The total demand for the q product over two periods with ad-signal</td></tr><tr><td> $\dot{\pi}(\beta, \eta; q)$ </td><td>The q firm&#x27;s profit without ad-signal</td></tr><tr><td> $\ddot{\pi}(\beta, \eta; q)$ </td><td>The q firm&#x27;s profit with ad-signal</td></tr></table>

## Appendix B. Proofs of Lemmas, Propositions, and Corollaries

Proof of Lemma 1 (Separating Equilibrium in the Traditional Scheme). Submitting $\dot { A _ { ( } a ; \boldsymbol { q } ) } = \bar { a } \bar { D } _ { s } ^ { q } , \boldsymbol { q } \in \{ H , L \}$ , into Equation $( 7 ) .$ , we derive that, in the traditional advertising scheme, the separating equilibrium exists if and only if $\exists a _ { N } > 0$ such that

$$
\frac {\ddot {\pi} \left(\beta , \eta ; L\right) - \dot {\pi} \left(\beta , \eta ; L\right)}{\ddot {D} _ {s} ^ {L}} \leq a _ {N} <   \frac {\ddot {\pi} \left(\beta , \eta ; H\right) - \dot {\pi} \left(\beta , \eta ; H\right)}{\ddot {D} _ {s} ^ {H}}.
$$

Then, the separating equilibrium exists if and only if

$$
\frac {\ddot {\pi} (\beta , \eta ; L) - \dot {\pi} (\beta , \eta ; L)}{\ddot {D} _ {s} ^ {L}} <   \frac {\ddot {\pi} (\beta , \eta ; H) - \dot {\pi} (\beta , \eta ; H)}{\ddot {D} _ {s} ^ {H}}.\tag{B.1}
$$

Plugging the equations of $\ddot { \pi } \left( \beta , \eta ; H \right) , \ \ddot { \pi } \left( \beta , \eta ; L \right) , \ \dot { \pi } \left( \beta , \eta ; H \right)$ $\dot { \pi } \left( \boldsymbol { \beta } , \eta ; L \right) , \ddot { \boldsymbol { D } } _ { s } ^ { H }$ , and $\ddot { D } _ { s } ^ { L }$ into Equation $( \mathrm { B } . 1 ) ,$ , we derive that the separating equilibrium exists if and onl $\begin{array} { r } { \dot { \gamma } \operatorname { i f } \dot { f } _ { N } \big ( \beta , \eta \big ) < \frac { ( P - C _ { H } ) ( 1 + H ) } { ( P - C _ { L } ) ( 1 + L ) } , } \end{array}$ where $f _ { N } \big ( \beta , \dot { \eta } \big ) = \ddot { D } _ { s } ^ { H } / \ddot { D } _ { s } ^ { L }$ . Specifically,

$$
= \frac {(2 \beta H + \eta H + \eta) (R - P / H) + (1 + H) (1 - \beta H - \eta) (R - P / L)}{(2 \beta L + \eta L + \eta) (R - P / H) + (1 + L) (1 - \beta L - \eta) (R - P / L)}.
$$

Proof of Proposition 1 (Product Reputation Paradox). According to Lemma 1, the separating equilibrium exists if and only if $\eta > 0$ and $\begin{array} { r } { f _ { N } \big ( \beta , \eta \big ) < \frac { ( P - C _ { H } ) ( 1 + H ) } { ( P - C _ { L } ) ( 1 + L ) } . } \end{array}$ , where

$$
\begin{array}{l} f _ {N} (\beta , \eta) \\ = \frac {(2 \beta H + \eta H + \eta) (R - P / H) + (1 + H) (1 - \beta H - \eta) (R - P / L)}{(2 \beta L + \eta L + \eta) (R - P / H) + (1 + L) (1 - \beta L - \eta) (R - P / L)}. \end{array}
$$

We know that $f _ { N } = \ddot { D } _ { s } ^ { H } / \ddot { D } _ { s } ^ { L }$ , where

$$
\begin{array}{r l} & {\ddot {D} _ {s} ^ {H} = \big (2 \beta H + \eta H + \eta \big) \big (R - P / H \big)} \\ & {\qquad + \big (1 + H \big) \big (1 - \beta H - \eta \big) \big (R - P / L \big),} \end{array}
$$

and

$$
\begin{array}{r l} & {\ddot {D} _ {s} ^ {L} = (2 \beta L + \eta L + \eta) (R - P / H)} \\ & {\qquad + (1 + L) (1 - \beta L - \eta) (R - P / L).} \end{array}
$$

Then, we get

$$
\frac {\partial \ddot {D} _ {s} ^ {H}}{\partial \beta} = 2 H (R - P / H) - H (1 + H) (R - P / L) > 0,
$$

and

$$
\frac {\partial \ddot {D} _ {s} ^ {L}}{\partial \beta} = 2 L (R - P / H) - L (1 + L) (R - P / L) > 0.
$$

So we have $\begin{array} { r l } & { \frac { \partial f _ { N } \left( \boldsymbol { \beta } , \boldsymbol { \eta } \right) } { \partial \boldsymbol { \beta } } = \frac { 1 } { ( \boldsymbol { \ddot { D } } _ { \mathrm { s } } ^ { L } ) ^ { 2 } } \left( \frac { \partial \boldsymbol { \ddot { D } } _ { s } ^ { H } } { \partial \boldsymbol { \beta } } \cdot \boldsymbol { \ddot { D } } _ { s } ^ { L } - \frac { \partial \boldsymbol { \ddot { D } } _ { s } ^ { L } } { \partial \boldsymbol { \beta } } \cdot \boldsymbol { \ddot { D } } _ { s } ^ { H } \right) } \end{array}$

1. If $\frac { \partial f _ { N } \big ( \beta , \eta \big ) } { \partial \beta } > 0 ,$ we need

$$
\frac {\frac {\partial \ddot {D} _ {s} ^ {H}}{\partial \beta}}{\frac {\partial \ddot {D} _ {s} ^ {L}}{\partial \beta}} > \frac {\ddot {D} _ {s} ^ {H}}{\ddot {D} _ {s} ^ {L}} = f _ {N} (\beta , \eta)
$$

and ma $f _ { N } ( \beta , \eta )  f _ { N } ( { \scriptstyle { \frac { 1 } { H } } } , 0 ) . S 0 , { \mathrm { i f } } ( R - P / L ) ( 1 + L ) < 2 { \big ( } R - P / H { \big ) }$ $\begin{array} { r } { / ( 1 + H ) \mathrm { t h e n } \frac { \partial f _ { N } \left( \beta , \eta \right) } { \partial \beta } > 0 . } \end{array}$

2. I $\dot { \varepsilon } \frac { \partial f _ { N } \big ( \beta , \eta \big ) } { \partial \beta } < 0 ,$ , we need

$$
\frac {\frac {\partial \ddot {D} _ {s} ^ {H}}{\partial \beta}}{\frac {\partial \ddot {D} _ {s} ^ {L}}{\partial \beta}} <   \frac {\ddot {D} _ {s} ^ {H}}{\ddot {D} _ {s} ^ {L}} = f _ {N} (\beta , \eta)
$$

and mi $\begin{array} { r } { \ i f _ { N } \big ( \beta , \eta \big ) \longrightarrow f _ { N } ( \frac { 1 } { H } , 0 ) . \thinspace S \mathrm { o } , \mathrm { i f } \left( R - P / L \right) ( 1 + L ) > 2 \big ( R - P / H \big ) } \end{array}$ $\begin{array} { r } { / ( 1 + H ) \mathrm { t h e n } \frac { \partial f _ { N } \left( \beta , \eta \right) } { \partial \beta } < 0 . } \end{array}$

Thus, we derive that

$$
\text {If} (R - P / L) (1 + L) <   2 (R - P / H) / (1 + H), f _ {N} (\beta , \eta)
$$

$$
\beta (\text { i.e., } \partial f _ {N} (\beta , \eta) / \partial \beta > 0)
$$

2. $\mathrm { I f } ( R - P / L ) ( 1 + L ) > 2 \bigl ( R - P / H \bigr ) / ( 1 + H ) , f _ { N } \bigl ( \beta , \eta \bigr )$ decreases in $\beta ~ ( \mathrm { i . e . , } ~ \partial f _ { N } ( \beta , \eta ) / \partial \beta < 0 )$

Because the advertising can signal the product quality if and only $\begin{array} { r } { \mathrm { i f } f _ { N } \big ( \beta , \eta \big ) < \frac { ( P - \check { C } _ { H } ) ( 1 + H ) } { ( P - C _ { L } ) ( 1 + L ) } , } \end{array}$ , when $f _ { N } \left( \beta , \eta \right)$ increases, the condition required for the advertising to signal product quality becomes stronger. So a higher reputation (a higher $\beta )$ of the H firm makes it more difficult for the H firm to signal through advertising except when $( R - P / L ) ( 1 + L ) > 2 ( R - P$ $/ H ) / ( \bar { 1 } + H )$

Proof of Proposition 2 (Ad-signal Reach Paradox). From the definition of $f _ { N } ( \beta , \eta )$ , we have

$$
\begin{array}{l} \frac {\partial f _ {N} (\beta , \eta)}{\partial \eta} \\ = \frac {\Big ((1 + H) (1 + L) \Big (R - \frac {P}{L} \Big) - 2 \Big (R - \frac {P}{H} \Big) \Big) \beta (H - L) \Big (\frac {P}{L} - \frac {P}{H} \Big)}{\Big ((2 \beta L + \eta L + \eta) \Big (R - \frac {P}{H} \Big) + (1 + L) \big (1 - \beta L - \eta \big) \Big (R - \frac {P}{L} \Big) \Big) ^ {2}}. \end{array}
$$

Letting $\frac { \partial f _ { N } ( \beta , \eta ) } { \partial \eta } > 0 .$ , we derive that

$$
\left(R - \frac {P}{L}\right) (1 + L) > \frac {2 \left(R - \frac {P}{H}\right)}{(1 + H)},
$$

and letting $\begin{array} { r } { \frac { \partial f _ { N } ( \beta , \eta ) } { \partial \eta } < 0 } \end{array}$ , we derive that

$$
\left(R - \frac {P}{L}\right) (1 + L) <   \frac {2 \left(R - \frac {P}{H}\right)}{(1 + H)}.
$$

Thus,

1. If $( R - P / L ) ( 1 + L ) > 2 \big ( R - P / H \big ) / ( 1 + H ) , f _ { N } \big ( \beta , \eta \big )$ increases in η $\mathrm { ( i . e . , } \partial f _ { N } \big ( \beta , \eta \big ) / \partial \eta > 0 \mathrm { ) }$

2. I $\mathrm { ~ f ~ } ( R - P / L ) ( 1 + L ) < 2 \big ( R - P / H \big ) / ( 1 + H ) , f _ { N } \big ( \beta , \eta \big )$ decreases in η $( \mathrm { i . e . , } \partial f _ { N } \big ( \beta , \eta \big ) / \partial \eta < 0 )$

Because the advertising can signal the product quality if and only $\begin{array} { r } { \mathrm { i f } f _ { N } \big ( \beta , \eta \big ) < \frac { ( P - C _ { H } ) ( 1 + H ) } { ( P - C _ { L } ) ( 1 + L ) } . } \end{array}$ , when $f _ { N } \left( \beta , \eta \right)$ increases. the condi tion required for the advertising to signal product quality becomes stronger. So a higher ad-signal reach level $( \eta )$ requires a stronger condition for advertising to signal product quality $( \mathrm { i . e . } ,$ , ad-signal reach paradox) except when $\big ( R - P / L \big ) ( 1 + L )$ $< 2 \bigl ( R - P / H \bigr ) / ( 1 + H )$

Proof of Corollary 1. Both Propositions 1 and 2 reveal that, in most cases, a higher $\beta$ or η makes it more difficult for advertising to signal product quality. Thus, it is worth noting that, for some given fixed costs, there exists an upper<sub>� �</sub> bound to $\beta$ (denoted as ${ \overline { { \beta } } } \in \left( 0 , 1 / H \right) )$ and η (denoted as $\overline { { \eta } }$ $\in ( 0 , 1 - \beta H ) )$ ) satisfying that $\begin{array} { r } { f _ { N } ( \overline { { \beta } } ) | _ { \beta < 1 / H } = \frac { \overline { { ( P - C _ { H } ) ( 1 + H ) } } } { ( P - C _ { L } ) ( 1 + L ) } } \end{array}$ and $\begin{array} { r } { f _ { N } \mathrm { { ( } } \overline { { \eta } } \mathrm { ) } | _ { \eta < 1 - \beta L } = \frac { ( P - C _ { H } ) ( 1 + H ) } { ( P - C _ { L } ) ( 1 + L ) } } \end{array}$ such that, if and only if ${ \mathrm { : } } \beta \in \left( 0 , { \overline { { \beta } } } \right)$ or $\eta \in ( 0 , \overline { { \eta } } )$ , the advertising can serve as a signal of quality.

Proof of Lemma 2 (Separating Equilibrium in Scheme I). Submitting $A _ { I } ( a , q ) = a _ { I } ( \ddot { D } _ { 1 } ^ { q } - D _ { A } ^ { \bar { q } } ) , q \in \{ H , L \}$ into Equation (7), we derive that, in the modified advertising scheme I, the separating equilibrium exists if and only if $\bar { \exists } a _ { I } > 0$ such that

$$
\frac {\ddot {\pi} \left(\beta , \eta ; L\right) - \dot {\pi} \left(\beta , \eta ; L\right)}{\ddot {D} _ {1} ^ {L} - D _ {A} ^ {L}} \leq a _ {I} <   \frac {\ddot {\pi} \left(\beta , \eta ; H\right) - \dot {\pi} \left(\beta , \eta ; H\right)}{\ddot {D} _ {1} ^ {H} - D _ {A} ^ {H}}.
$$

Because $\ddot { D } _ { 1 } ^ { q } - D _ { A } ^ { q } = D _ { B } + \ddot { D } _ { c } ^ { q } ,$ we derive that the separating equilibrium exists if and only i $\mathrm { f } \exists a _ { I } > 0$ such that

$$
\frac {\ddot {\pi} (\beta , \eta ; L) - \dot {\pi} (\beta , \eta ; L)}{D _ {B} + \ddot {D} _ {c} ^ {L}} \leq a _ {I} <   \frac {\ddot {\pi} (\beta , \eta ; H) - \dot {\pi} (\beta , \eta ; H)}{D _ {B} + \ddot {D} _ {c} ^ {H}}.
$$

Then, the separating equilibrium exists if and only if

$$
\frac {\ddot {\pi} (\beta , \eta ; L) - \dot {\pi} (\beta , \eta ; L)}{D _ {B} + \ddot {D} _ {c} ^ {L}} <   \frac {\ddot {\pi} (\beta , \eta ; H) - \dot {\pi} (\beta , \eta ; H)}{D _ {B} + \ddot {D} _ {c} ^ {H}}.\tag{B.2}
$$

Plugging the equations of $\ddot { \pi } \left( \beta , \eta ; H \right) , \ \ddot { \pi } \left( \beta , \eta ; L \right) , \ \dot { \pi } \left( \beta , \eta ; H \right) .$ $\dot { \pi } ( \beta , \eta ; L ) , D _ { B } , \ddot { D } _ { c } ^ { H }$ and $\ddot { D } _ { c } ^ { L }$ into Equation (B.2), we derive that the separating equilibrium exists if and only if $f _ { I } ( \beta , \eta ) <$ $\frac { ( P - C _ { H } ) ( 1 + H ) } { ( P - C _ { L } ) ( 1 + L ) }$ , where $\boldsymbol { \dot { f } } _ { I } \big ( \boldsymbol { \beta } , \eta \big ) = ( D _ { B } + \boldsymbol { \ddot { D } } _ { c } ^ { H } ) / ( D _ { B } + \boldsymbol { \ddot { D } } _ { c } ^ { L } )$ . Specifically,

$$
f _ {I} (\beta , \eta) = \frac {\eta (R - P / H) + (1 - \beta H - \eta) (R - P / L)}{\eta (R - P / H) + (1 - \beta L - \eta) (R - P / L)}.
$$

Proof of Proposition 3 (Modification in Product Reputation Paradox in Scheme I). According to Lemma $^ { 2 , }$ we have

$$
f _ {I} (\beta , \eta) = \frac {\eta (R - \frac {P}{H}) + (1 - \beta H - \eta) (R - \frac {P}{L})}{\eta (R - \frac {P}{H}) + (1 - \beta L - \eta) (R - \frac {P}{L})},
$$

and then,

$$
\begin{array}{l} \frac {\partial f _ {I} (\beta , \eta)}{\partial \beta} \\ = \frac {- (H - L) (R - P / L) (\eta (R - P / H) + (1 - \eta) (R - P / L))}{(\eta (R - P / H) + (1 - \beta L - \eta) (R - P / L)) ^ {2}} <   0. \end{array}
$$

This implies tha $f _ { I } \left( \beta , \eta \right)$ decreases in $\beta .$ As the advertising can signal the product quality if and only $\begin{array} { r } { \mathrm { i f } f _ { I } ( \beta , \eta ) < \frac { ( P - C _ { H } ) \overline { { ( 1 + H ) } } } { ( P - C _ { L } ) ( 1 + L ) } , } \end{array}$ when $f _ { I } ( \beta , \eta )$ decreases, it becomes easier for the high-quality firm to signal product quality through advertising. So, in the modified scheme I, the higher the product reputation factor $\beta ,$ the easier it is to signal quality through advertising, indicating that the product reputation paradox does not exist in scheme I.

Proof of Proposition 4 (Modification in Ad-signal Reach Paradox in Scheme I). According to Lemma 2, we have

$$
f _ {I} (\beta , \eta) = \frac {\eta \left(R - \frac {p}{H}\right) + (1 - \beta H - \eta) \left(R - \frac {p}{L}\right)}{\eta \left(R - \frac {p}{H}\right) + (1 - \beta L - \eta) \left(R - \frac {p}{L}\right)},
$$

then

$$
\frac {\partial f _ {I} (\beta , \eta)}{\partial \eta} = \frac {\beta (H - L) (R - P / L) (P / L - P / H)}{(\eta (R - P / H) + (1 - \beta L - \eta) (R - P / L)) ^ {2}} > 0.
$$

So we get $\begin{array} { r } { \frac { \partial f _ { I } } { \partial \eta } > 0 . } \end{array}$ , implying that, if the advertising performance factor (η) is higher, performance-based advertising requires a stronger condition for advertising to retain its signaling ability. This indicates that, under performance-based advertising, the ad-signal reach paradox cannot be eradicated even if we do not count the repeat purchases as well as the sales from the loyal consumers into the performance of advertising.

Proof of Proposition 5 (Separating Equilibrium in Modified Scheme II). Submitting $\dot { A _ { I I } } ( a , q ) = a _ { I I } ( \ddot { D } _ { 1 } ^ { q } - \dot { D } _ { 1 } ^ { q } ) , q \in \{ H , L \}$ into Equation (7), we derive that, in the modified advertising scheme $\scriptstyle \mathrm { I I , }$ the separating equilibrium exists if and only if $\exists a _ { I I } > 0$ such that

$$
\frac {\ddot {\pi} \left(\beta , \eta ; L\right) - \dot {\pi} \left(\beta , \eta ; L\right)}{\ddot {D} _ {1} ^ {L} - \dot {D} _ {1} ^ {L}} \leq a _ {I I} <   \frac {\ddot {\pi} \left(\beta , \eta ; H\right) - \dot {\pi} \left(\beta , \eta ; H\right)}{\ddot {D} _ {1} ^ {H} - \dot {D} _ {1} ^ {H}}.
$$

Then, the separating equilibrium exists if and only if

$$
\frac {\ddot {\pi} (\beta , \eta ; L) - \dot {\pi} (\beta , \eta ; L)}{\ddot {D} _ {1} ^ {L} - \dot {D} _ {1} ^ {L}} <   \frac {\ddot {\pi} (\beta , \eta ; H) - \dot {\pi} (\beta , \eta ; H)}{\ddot {D} _ {1} ^ {H} - \dot {D} _ {1} ^ {H}}.\tag{B.3}
$$

Plugging the equations of $\dot { \iota } \left( \beta , \eta ; H \right) , \ddot { \pi } \left( \beta , \eta ; L \right) , \dot { \pi } \left( \beta , \eta ; H \right)$ $\dot { \pi } \left( \beta , \eta ; L \right) , \ddot { D } _ { 1 } ^ { H } , \dot { D } _ { 1 } ^ { H } , \ddot { D } _ { 1 } ^ { L } ,$ , and $\dot { D } _ { 1 } ^ { L }$ into Equation (B.3), we derive that the separating equilibrium exists if and only if $f _ { I I } ( \beta , \eta )$ ${ < \frac { ( P - C _ { H } ) ( 1 + \bar { H } ) } { ( P - C _ { L } ) ( 1 + L ) } . }$ , where $f _ { I I } \left( \beta , \eta \right) = 1$ . That is, the separating equilibrium exists if and only if $\frac { ( P - C _ { H } ) ( 1 + H ) } { ( P - C _ { L } ) ( 1 + L ) } > 1$

## Endnotes

<sup>1</sup> Please refer to the references therein in these papers.

<sup>2</sup> When there exists a separating equilibrium, advertising expenditure can serve as a signal of product quality. In this scenario, consumers perceive the product quality as H because “the choice that an H makes a separating equilibrium must yield $\rho = 1$ (ρ is the probability a firm is believed to be producing quality $H ) ^ { \prime \prime }$ (Milgrom and Roberts 1986, $\mathrm { { p . } }$ 806).

<sup>3</sup> Without observing an advertising signal, consumers perceive the product quality as L because “whatever choice $( P _ { L } , A _ { L } )$ is made by the ${ \mathrm { L } } ,$ in separating sequential equilibrium this choice must yield $\rho =$ 0 (ρ is the probability a firm is believed to be producing quality H)” (Milgrom and Roberts 1986, p. 804).

<sup>4</sup> Following Milgrom and Roberts (1986), we do not assume $C _ { H } > C _ { L }$ We also ignore any fixed costs because including them would have no effect on the solution

<sup>5</sup> Following Dellarocas (2012), the counting of sales (under the payper-sale mechanism) could be interpreted as the counting of actions times the conversion rate of each action (under the pay-per-click/call mechanisms). Alternatively, we could simply define a as the effective cost per sale, $\begin{array} { r } { a = \frac { c o s t p e r a c t i o n } { c o n v e r s i o n \underline { { r a t e o f } } t h e a c t i o n } . } \end{array}$ . Thus, although we focus on a pay-per-sale model in this paper, our results can apply to other performance-based mechanisms such as pay-per-click/call given an exogenous conversion rate of clicks/calls.

## References

Andrews M, Luo X, Fang Z, Ghose A (2016) Mobile ad effectiveness: Hyper-contextual targeting with crowdedness. Marketing Sci. 35(2):218–233.

Animesh A, Ramachandran V, Viswanathan S (2010) Research note— Quality uncertainty and the performance of online sponsored search markets: An empirical investigation. Inform. Systems Res. 21(1):190–201.

Aral S (2021) What digital advertising gets wrong. Harvard Bus. Rev. (February 19), https://hbr.org/2021/02/what-digital advertising-gets-wrong.

Arnosti N, Beck M, Milgrom P (2016) Adverse selection and auction design for internet display advertising. Amer. Econom. Rev. 106(10):2852–2866.

Balseiro SR, Gur Y (2019) Learning in repeated auctions with budgets: Regret minimization and equilibrium. Management Sci. 65(9): 3952–3968.

Blake T, Nosko C, Tadelis S (2015) Consumer heterogeneity and paid search effectiveness: A large-scale field experiment. Econometrica 83(1):155–174.

Campbell MC, Keller KL (2003) Brand familiarity and advertising repetition effects. J. Consumer Res. 30(2):292–304.

Chen Y-J (2017) Optimal dynamic auctions for display advertising. Oper. Res. 65(4):897–913.

Coviello L, Gneezy U, Goette L (2017) A large-scale field experiment to evaluate the effectiveness of paid search advertising. CESifo Working Paper Series No. 6684, University of California, San Diego.

Dellarocas C (2012) Double marginalization in performance-based advertising: Implications and solutions. Management Sci. 58(6): 1178–1195.

Despotakis S, Ravi R, Sayedi A (2021) First-price auctions in online display advertising. J. Marketing Res. 58(5):888–907.

Erdem T, Swait J (1998) Brand equity as a signaling phenomenon. J. Consumer Psych. 7(2):131–157.

Erdem T, Swait J, Valenzuela A (2006) Brands as signals: A crosscountry validation study. J. Marketing 70(1):34–49.

Feng J, Xie J (2012) Research note—Performance-based advertising: Advertising as signals of product quality. Inform. Systems Res. 23(3 part 2):1030–1041.

Ghose A, Yang S (2009) An empirical analysis of search engine advertising: Sponsored search in electronic markets. Management Sci. 55(10):1605–1622.

Gordon BR, Jerath K, Katona Z, Narayanan S, Shin J, Wilbur KC (2021) Inefficiencies in digital advertising markets. J. Marketing 85(1):7–25.

Guo X, Jiang B (2016) Signaling through price and quality to consu J. Marketing

Hollenbeck B (2018) Online reputation mechanisms and the decreas ing value of chain affiliation. J. Marketing Res. 55(5):636–654.

Hu YJ (2004) Performance-based pricing models in online advertising Preprint, submitted March 3, https://dx.doi.org/10.2139/ssrn 501082.

Hu Y, Shin J, Tang Z (2016) Incentive problems in performance-based online advertising pricing: Cost per click vs. cost per action. Management Sci. 62(7):2022–2038.

Jiang B, Tian L, Xu Y, Zhang F (2016) To share or not to share: Demand forecast sharing in a distribution channel. Marketing Sci. 35(5): 800–809.

Kihlstrom RE, Riordan MH (1984) Advertising as a signal. J. Political Econom. 92(3):427–450.

Kirmani A, Rao AR (2000) No pain, no gain: A critical review of the literature on signaling unobservable product quality. J. Marketin 64(2):66–79.

Liu D, Viswanathan S (2014) Information asymmetry and hybrid advertising. J. Marketing Res. 51(5):609–624.

Liu D, Chen J, Whinston AB (2010) Ex ante information and the design of keyword auctions. Inform. Systems Res. 21(1):133–153

Milgrom P, Roberts J (1986) Price and advertising signals of product quality. J. Political Econom. 94(4):796–821.

Nelson P (1970) Information and consumer behavior. J. Political Econom. 78(2):311–329.

Nelson P (1974) Advertising as information. J. Political Econom. 82(4):729–754

Sayedi A (2018) Real-time bidding in online display advertising. Marketing Sci. 37(4):553–568.

Sahni NS, Nair HS (2020) Does advertising serve as a signal? Evidence from a field experiment in mobile search. Rev. Econom. Stud. 87(3):1529–1564.

Sun H, Fan M, Tan Y (2020) An empirical analysis of seller advertising strategies in an online marketplace. Inform. Systems Res. 31(1): 37–56.

Todri V, Ghose A, Singh PV (2020) Trade-offs in online advertising: Advertising effectiveness and annoyance dynamics across the purchase funnel. Inform. Systems Res. 31(1):102–125.

Wells JD, Valacich JS, Hess TJ (2011) What signal are you sending? How website quality influences perceptions of product quality and purchase intentions. MIS Quart. 35(2):373–396.

Xu L, Chen J, Whinston A (2012) Effects of the presence of organic listing in search advertising. Inform. Systems Res. 23(4):1284–1302.

Yang S, Ghose A (2010) Analyzing the relationship between organic and sponsored search advertising: Positive, negative, or zero interdependence? Marketing Sci. 29(4):602–623.

Zeithammer R (2019) Soft floors in auctions. Management Sci. 65(9): 4204–4221.

Zhang X, Feng J (2011) Cyclical bid adjustments in search-engine advertising. Management Sci. 57(9):1703–1719.

Zhao H (2000) Raising awareness and signaling quality to uninformed consumers: A price-advertising model. Marketing Sci 19(4):390–396.

Copyright of Information Systems Research is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.
