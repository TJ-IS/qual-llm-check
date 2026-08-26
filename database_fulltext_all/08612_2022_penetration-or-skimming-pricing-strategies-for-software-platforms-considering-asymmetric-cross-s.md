---
otero_id: 8612
otero_key: "5FNUFG6X"
title: "Penetration or Skimming? Pricing Strategies for Software Platforms Considering Asymmetric Cross-Side Network Effects"
authors: "Nan Yuan; Haiyang Feng; Minqiang Li; Nan Feng"
year: "2022"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00748"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
2022

# Penetration or Skimming? Pricing Strategies for Software Platforms Considering Asymmetric Cross-Side Network Effects

Nan Yuan , yuan\_nan@tju.edu.cn

Haiyang Feng , hyfeng@tju.edu.cn

Minqiang Li , mqli@tju.edu.cn

Nan Feng , fengnan@tju.edu.cn

Follow this and additional works at: https://aisel.aisnet.org/jais

ISSN 1536-9323

# Penetration or Skimming? Pricing Strategies for Software Platforms Considering Asymmetric Cross-Side Network Effects

Nan Yuan<sup>1</sup>, Haiyang Feng,<sup>2</sup> Minqiang Li,<sup>3</sup> Nan Feng<sup>4</sup>

<sup>1</sup>College of Management and Economics, Tianjin University, China, yuan\_nan@tju.edu.cn <sup>2</sup>College of Management and Economics, Tianjin University, China, hyfeng@tju.edu.cn <sup>3</sup>College of Management and Economics, Tianjin University, China, mqli@tju.edu.cn <sup>4</sup>College of Management and Economics, Tianjin University / Tianjin University (Qingdao) Ocean Engineering Research Institute Co. LTD, China, fengnan@tju.edu.cn

## Abstract

Considering a two-sided software platform with software developers on one side and software users on the other, we study whether the platform should adopt a penetration pricing strategy or skimming pricing strategy on the developer side. We propose a two-period analytical model with asymmetric cross-side network effects to analyze the platform’s optimal pricing strategy. Our analysis reveals that the platform should adopt a penetration pricing strategy if the user-to-developer network effect is strong and a skimming pricing strategy otherwise. If the platform does not charge users an access fee, the platform should consider subsidizing developers’ access in the first period only. However, when the platform charges users an access fee, subsidizing developers’ access in both periods can be viable for the platform. Charging the software user an access fee incentivizes the platform to subsidize developers in the first period if the user-to-developer network effect is weak. Finally, this study reveals that the optimal access fee charged or subsidy provided to developers in the two periods is determined by several key factors: developers’ basic expectations about the revenue to be gained from the platform (optimistic or pessimistic), intensities of cross-side network effects, the lengths of the two periods, and the access fee charged to users.

Keywords: Software Platform, Penetration/Skimming Pricing, Subsidizing Developers, Asymmetric Cross-Side Network Effects

Giri Tayi was the accepting senior editor. This research article was submitted on Oct 20, 2020 and underwent two revisions. Haiyang Feng is the corresponding author.

## 1 Introduction

In the digital era, information technology has promoted the rapid rise of the platform economy. A report by Accenture estimates that platform firms may represent up to \$10 trillion in socioeconomic value creation from 2016 to 2025 (Schenker, 2019). IT-enabled platforms have recently become dominant forces in many markets. As of the second quarter of 2019, five of the most valuable public corporations by market capitalization, namely Microsoft, Amazon, Apple, Alphabet, and Facebook, were all platform-based businesses. Microsoft surpassed \$1 trillion in market capitalization,<sup>1</sup> and Apple App Store and Google Play together generated \$39.7 billion in revenue in the first half of 2019 (Nelson, 2019). Aside from the giant platform companies, “myriad startups and smaller companies are thriving as well,” according to Erik

Brynjolfsson, director of the MIT Initiative in the Digital Economy (Tracy, 2019).

The extant literature has classified platforms into four types: exchanges, transaction systems, advertisingsupported media, and software platforms (Evans, 2011; Sriram et al., 2015). The software platform is an extensible codebase of a software system that provides both core functionalities shared by the modules that interoperate with it and the interfaces through which they interoperate (Tiwana et al., 2010); it connects developers with users through the software on the platform, such as app stores (Apple App Store, Google Play), operating systems (e.g., Windows, Android), and video game platforms (e.g., Steam, Xbox). According to Evans Data Corporation, the number of global software developers is expected to reach 277 million by 2023 (Daxx, 2020). This substantial growth in the number of developers is also causing rapid growth in the number of software applications available.<sup>2</sup> For instance, in 2019, the total number of applications on Google Play and Apple App Store reached 3.3 million and 2.2 million, respectively (Artyom, 2019). Since most software platforms rely on third-party developers to develop applications, it is thus important to understand whether and how platforms should charge developers for access.

Whether to adopt penetration vs. skimming pricing strategies is an important issue in two-sided markets (Rysman, 2009). The penetration pricing strategy, indicating that the platform sets a low price early in the product life cycle and raises it after having established a base, is a common pricing strategy in two-sided markets. In practice, some software platforms adopt the penetration pricing strategy on the developer side. For example, prior to 2017, Steam only charged developers \$100 without any restriction on the number of games submitted. It then raised its price and asked developers to pay an application fee of \$100 for each game they intended to publish. However, some software platforms also adopt the skimming pricing strategy, which involves charging a high introductory price and subsequently lowering it (Dean, 1976, Martin et al., 2015). For instance, prior to 2014, Microsoft charged its developers \$99 a year to use developers’ accounts and then slashed the recurring fee to a one-time fee of \$19 to attract more developers. Pricing strategies vary across different software platforms; thus, in this study, we build a two-period model, aiming to first answer the following research question:

RQ1: Should a software platform adopt the penetration or skimming pricing strategy on the developer side?

In reality, some software platforms choose to subsidize developers in certain periods, rather than charge them in all periods. For example, before Twitter began charging developers to use its data to serve business customers in June 2019, it provided developers with free access to the standard API (Constine, 2019). Wegame, a game platform launched by Tencent, initially did not subsidize developers but, beginning in May 2019, it announced the Wings Program to offer developers investment and training opportunities. Different platforms have opted to either subsidize or charge developers for access. Subsidizing access for developers can encourage developers to use the platform, subsequently attracting new users and developers to the software platform. However, the benefits gained from these developers may not adequately compensate platforms for the costs associated with subsidizing them. Hence, some software platforms choose to charge developers, which may reduce their willingness to join the platform, especially for those who have already incurred high development costs. Thus, our second research question is:

RQ2: Should a software platform subsidize or charge developers for access in different time periods when it adopts the skimming or penetration pricing strategy, and what should the optimal subsidy or access fee be?

A prominent feature of software platforms is that software developers typically join the platform before users (Hagiu, 2006). This allows developers to figure out the platform’s rules and resources, evaluate how best to meet the users’ underlying demands, develop the software, and wait for the platform to review their products. For instance, four months after Apple released its Software Development Kit (SDK) for developers, the App Store and apps were published for users. Developers on Steam are expected to wait thirty days until the platform reviews their games before launching them (Matulef, 2017). Song et al. (2018) empirically proved that the user-to-app cross-side network effects and app-to-user cross-side network effects on software platforms are asymmetric and indicated that the impacts from the developer side to the user side are characterized by a short-term effect; however, the user-to-app network effects are persistent. Thus, in this study, we assume that the platform first seeks to attract developers and then launches the platform and/or the developed software to users. We emphasize that the cross-side network effects in different directions—i.e., developer-to-user and userto-developer—are asymmetric. In other words, the impacts from developers to users can take effect immediately, while the impacts in the other direction are delayed since it takes developers time to develop, test, and upload their software. The third research question we seek to answer is:

RQ3: How do the asymmetric cross-side network effects affect the platform’s profits as well as the optimal prices that it can charge developers or the subsidies it must provide to them.

As shown in Table 1, some software platforms also charge their users access fees. It is worth noting that when the software can only run on the proprietary devices provided by the platform, the hardware fee is essentially equivalent to an access fee. For instance, users need to buy an Xbox One X console (priced at \$499 in 2019)<sup>3</sup> before purchasing and playing the video games developed for it. Some software platforms do not charge users access fees—for example, Steam and Epic. Therefore, this study is conducted with two scenarios: one in which the platform charges users an access fee and one in which it does not.

Our analytical and numerical results reveal how the software platform’s pricing strategies on the developer side in the first and second periods are affected by the access fee paid by users, the lengths of the two periods, developers’ basic expected revenue, and the strengths of the two-sided network effects. Our findings indicate that the platform should adopt a penetration pricing strategy if users have significant impacts on developers. Otherwise, the skimming pricing strategy is more profitable. When the platform does not charge users access fees, a stronger developer-to-user network effect or a longer second period will likely induce the platform to adopt the penetration pricing strategy. In contrast, developers’ optimistic expectations of future revenue will generally lead the platform to adopt the skimming pricing strategy. When users are charged an access fee or offered a subsidy, the willingness of the platform to adopt the penetration pricing strategy will first increase and then decrease as the length of the second period becomes longer.

Our findings suggest that if the platform does not charge users for access, when the platform adopts the skimming pricing strategy, it should charge developers in both periods. However, if it adopts the penetration pricing strategy, subsidies could reasonably be offered to developers in the first period. If the user-to-developer network effect is sufficiently weak, then the platform should charge developers in the first period; if it is sufficiently strong, the platform should subsidize developers; and if the user-to-developer network effect is moderate, the platform is better off subsidizing developers in the first period if they have pessimistic expectations about their likely revenue.

If users are charged an access fee or offered a subsidy, the platform should subsidize developers in the first period if the intensity of the user-to-developer network effect is sufficiently weak or strong; otherwise, it should charge developers. In the second period, the pricing strategy is more diversified than the pricing strategy when the users are charged no access fee. Therefore, the platform should charge developers if the intensity of the user-to-developer network effect is strong. If the intensity of the user-todeveloper network effect is weak, the platform should charge users; otherwise, it should subsidize users. As developers become more optimistic about their profits, the platform should increase the access fee charged to developers or decrease the subsidy it pays if the impacts of users on developers are weak.

In the case that the platform does not charge a user access fee, if developers become more optimistic about their potential revenue or if the length of the second period becomes longer, the optimal access fee charged to developers in the first period will decrease if and only if the users’ impacts on developers are sufficiently strong, while in the second period, the fee will increase under all conditions. As the intensity of the user-to-developer network effect increases, the optimal access fee charged to developers in the first period will initially increase and then decrease, while in the second period, the fee will increase monotonically. When the basic expected revenue per unit of time earned by developers is low, the increase in the intensity of the developer-to-user network effect will likely cause the platform to raise the optimal access fee charged (or decrease the subsidy offered) to developers in the first period and will have nonmonotonic impacts on it in the second period. In particular, the optimal access fee charged to developers in the second period will initially decrease and then increase, as the network effect from developers to users becomes stronger. In the case which the platform charges users an access fee or provides them with a subsidy, if developers become more optimistic, the access fee charged to users will increase if and only if the user-to-developer network effect is weak. The increase in the length of the second period has nonmonotonic impacts on the access fee charged to users. In particular, the optimal user access fee will first decrease and then increase as the length of the second period becomes longer.

The remainder of this paper proceeds as follows. The next section reviews the related literature. The third section develops a two-period model and investigates the decisions faced by the participants on both sides— i.e., developers and users. Then, in the fourth and fifth sections, the optimal pricing strategy is analyzed in two scenarios—one in which users can join the platform for free, and the other where users pay an access fee or receive a subsidy. In the last section, we summarize the extensions and findings and discuss the implications and limitations.

Table 1. Examples of Software Platforms that Do and Do Not Charge Users Access Fees

<table><tr><td>Free to users</td><td>Access fees charged to users</td></tr><tr><td>Steam</td><td>Azure Marketplace</td></tr><tr><td>Epic</td><td>PlayStation</td></tr><tr><td>Wegame (Tencent)</td><td>Xbox</td></tr><tr><td>Origin</td><td>Apple App Store</td></tr><tr><td>Firefox</td><td>Microsoft Store</td></tr></table>

## 2 Literature Review

This study is related to three streams of literature. The first focuses on the pricing strategies of two-sided platforms. Caillaud and Jullien (2003) built a twoperiod model with imperfect competition between intermediation service providers and provided divideand-conquer strategies through which companies can subsidize one side of the market and recover its losses on the other side. Parker and Van Alstyne (2005) studied a monopoly platform’s pricing strategy and showed that some platform companies prefer to subsidize one side of the market because the increased profits in a complementary market can compensate for the cost of the subsidy. Eisenmann et al. (2006) argue that a platform can choose to subsidize one side of the market, which can develop strong network effects to attract the other side. Armstrong and Wright (2007) examined whether competing platforms are better off charging buyers an amount that is below their costs, and then fully leveraging sellers’ network benefits to recover the loss incurred from subsidizing the buyers. These studies focus on identifying the appropriate side of the platform that should be subsidized or charged. Recent literature has focused on the pricing strategy on one side of the platform and the size of the subsidy. Ren and Schaar (2014) examined whether a usergenerated content platform should subsidize or tax content producers when it provides the service for free to content viewers, and found that if there are few content viewers and the content production cost is high, the platform should subsidize content producers. Fang et al. (2017) investigated a two-sided platform’s optimal prices and subsidies, considering the trade-off between revenue and social welfare maximization, and revealed that the platform should offer subsidies to participants to reach its maximal potential revenue. Gao (2018) analyzed the pricing strategy of two-sided platforms on which participants can join both sides of the platform, and showed that the platform must earn higher profit margins on one side to compensate for subsidizing users who join both sides. Zimmermann et al. (2018) explored a monopoly sharing platform’s pricing strategy for lenders and borrowers and found that the platform should increase lender fees or decrease borrower fees when the sharing price or usage capacity increases. Sun et al. (2019) investigated the optimal pricing strategy for online ride-hailing platforms and found that the platform’s optimal price consists of a base fare, a congestion fee, and an emergency fee. Dou and Wu (2019) studied the optimal pricing/subsidizing strategy in the presence of piggybacking for competing platforms and found that piggybacking changes the level of platform subsidization.

Previous studies on two-sided platforms that concentrate on software platforms are closest to the present study. These studies analytically and empirically study the critical decision-making tasks faced by software platforms. Liu (2010) investigated the pricing strategies of Nintendo and Sony’s PlayStation and showed that consumer heterogeneity induces the video game platform to employ skimming pricing, while the network effects induce it to adopt penetration pricing. Rasch and Wenzel (2013) studied software platforms’ pricing strategy in terms of the piracy of software products and showed that the license fees charged to developers are higher if greater software protection is offered but their impact on user pricing is ambiguous. Anderson et al. (2014) studied the optimum investment in the performance of video game platforms and revealed that heavy investment does not always imply a “winner-take-all” outcome. Parker et al. (2017) adopted a sequential innovation model to study the platform’s optimal intellectual property regimes and showed how the number of developers promotes the success of software platforms. Sur et al. (2019) analyzed optimal revenue sharing between the platform firm and application providers by adopting the Stackelberg model and identified the optimal sharing rates and the optimal price charged to users. They found that potential demand has a significant impact on optimal revenue sharing, and platforms should increase their market size first. Some prior literature has also studied the decisions of the software platform on first-party content (Hagiu & Spulber, 2013), compatibility (Adner et al., 2020), openness (Parker & Van Alstyne, 2018, Cenamor & Frishammar, 2021), market entry (Feng et al., 2018, Feng et al., 2020), software patching (August et al., 2019), and service integration (Zhang & Yue, 2020), among other elements.

Another important stream of studies directly related to our work is on penetration and skimming pricing strategies, Kalish (1983) studied a monopoly’s pricing strategy for a new product with word-of-mouth effects, and found that when the interest rate is zero, the price will decrease over time if the current sales have a positive implication on the future and vice versa. Krishnan et al. (1999) suggested that if price sensitivity or the discount rate is high, the firm will prefer to adopt the skimming pricing strategy. Su (2007) demonstrated that heterogeneity in valuation and customer patience determine the firm’s optimal pricing strategy and found that markdown pricing is optimal if high-value customers are less patient and low-value customers are sufficiently patient. Prior literature has also found that the firm adopts penetration and skimming pricing strategies with similar frequency (about 20%) in practice (Martin et al, 2015) and revealed the conditions under which the penetration pricing strategy should be adopted: namely, when the demand of the innovators is low (Liu et al., 2011), the market is pricesensitive and competitive (Kotler & Armstrong, 2017), the firm’s discount factor is insignificant (Du & Chen, 2017), or consumers are prone to giving positive reviews (Feng et al., 2019). Roma et al. (2016) examined the impacts of a distribution platform on developers’ pricing decisions and found that developers prefer to adopt the penetration pricing strategy in Google Play. Li (2019) studied a monopolist’s joint optimal pricing strategies for complementary products—software and hardware— and revealed that the optimal strategy is skimming for hardware and investing for software. Hu et al. (2021) investigated whether a ride-hailing platform should adopt the skimming or penetration pricing strategy from a temporal perspective, and found that if the platform shares demand-supply information with drivers, the penetration pricing strategy is superior.

The third stream of related literature focuses on asymmetric network effects, occurring in different markets in different forms. Csorba and Hahn (2006) emphasize that network effects are asymmetric, according to the software’s functionalities—that is, the network effects from content producers to users derive from the platform’s writing function used by content producers, while the network effects in the other direction derive from the reading function. Some studies focus on the intensities of the asymmetric network effects of different firms and their impacts on firms’ pricing strategies (e.g., Hoernig, 2007; Argenziano, 2009; Saito & Matsubayashi, 2017). Wilbur (2008) empirically found that in the television market, the intensity of the network effect from viewers to advertisers is stronger than it is in the opposite direction. Analogously, Chu and Manchanda (2016) showed that an increase in the number of sellers is more attractive to buyers than vice versa.

As shown in Table 2, there are several key differences between this study and prior studies. First, the prior works mainly focus on the skimming and penetration pricing strategy for products. However, pricing strategies for two-sided platforms have received little attention. In our study, by building a two-period model, we manage to investigate whether a software platform should adopt the penetration or skimming pricing strategy on the developer side. Second, unlike some prior studies (e.g., Anderson et al., 2014), which assume that developers and users join the platform simultaneously, we consider a sequential entry and study how the asymmetric cross-side network effects influence the platform’s optimal pricing decisions. Finally, we identify several key determinants for the pricing policy: developers’ basic expected revenue, asymmetric cross-side network effects, the lengths of the two periods, and user access fees. In contrast, no prior study has identified more than one of these determinants. These unique features distinguish our study from the previous literature.

## 3 Model

This study considers an online software platform with software developers on one side and software users on the other side. Considering asymmetric cross-side network effects, we develop a two-period model to analyze how the software platform makes pricing decisions using the penetration or skimming pricing strategy. As shown in Figure 1, we describe the twoperiod model as follows:

1. Before period ?? (?? = 1,2) begins, the platform announces the price it is charging or the subsidy it is offering in period ?? to developers, and developers make participation decisions based on the platform’s pricing strategy and the number of users on the platform. Then, the developers who decide to join the platform develop their software.

2. At the beginning of period ?? ( ?? = 1,2 ), developers launch their software and users make participation decisions.

The time lag between developers’ entry time and the software’s launch time is the time needed for software development, uploading, and platform review. Without loss of generality, the length of the whole demand window is normalized to 1, the length of Period 1 is denoted by $\begin{array} { r } { \tau _ { 1 } = \frac { 1 - \tau } { 2 } } \end{array}$ , and the length of Period 2 is denoted by $\begin{array} { r } { \tau _ { 2 } = \frac { 1 + \bar { \tau } } { 2 } } \end{array}$ . The difference in the lengths of the two time periods is denoted by $\tau \in ( - 1 , 1 )$ . It is also assumed that developers are myopic and cannot accurately estimate the future number of users when making their participation decisions. Thus, developers’ total expected revenue consists of two parts: a constant term capturing the developer’s basic expected revenue and a variable term that depends on the number of the observed users on the platform and the intensity of the cross-side network effects.

Table 2. Comparison of Our Study with Prior Studies

<table><tr><td>Article</td><td>Two-sided market</td><td>Skimming/penetration pricing</td><td>Asymmetric cross-side network effects</td><td>Subsidizing/charging</td><td>Key determinants of pricing policies</td></tr><tr><td>Kalish (1983)</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>(1) learning curve, (2) word-of-mouth effect, (3) the saturation factor</td></tr><tr><td>Krishnan et al. (1999)</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>(1) price sensitivity, (2) discount rate</td></tr><tr><td>Rochet &amp; Tirole (2003)</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td><td>(1) cross-side network effect, (2) the ratio of elasticities on both side</td></tr><tr><td>Parker &amp; Van Alstyne (2005)</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td><td>(1) cross-side network effect, (2) cross-price elasticity, (3) the ratio of surplus on both sides</td></tr><tr><td>Armstrong &amp; Wright (2007)</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td><td>(1) cross-side network effect, (2) product differentiation</td></tr><tr><td>Su (2007)</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Heterogeneity in consumers&#x27; valuation and patience</td></tr><tr><td>Liu (2010)</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>(1) network effect, (2) consumer heterogeneity, (3) oligopolistic competition</td></tr><tr><td>Ren &amp; Schaar (2014)</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td><td>(1) the quality of content, (2) consumers&#x27; payment rate</td></tr><tr><td>Kotler &amp; Armstrong (2017)</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>(1) competitive protection, (2) price sensitivity</td></tr><tr><td>Du &amp; Chen (2017)</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>(1) consumer&#x27;s strategic behavior, (2) the firm&#x27;s discounter factor</td></tr><tr><td>Li (2019)</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>Type of consumer</td></tr><tr><td>Feng et al. (2019)</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Online product review</td></tr><tr><td>Hu et al. (2021)</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Matching probabilities</td></tr><tr><td>This work</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>(1) asymmetric cross-side network effects, (2) access fee payable by users, (3) developers&#x27; basic expected revenue, (4) lengths of the two periods</td></tr></table>

![](/api/attachments/5FNUFG6X/fulltext/images/a39f03a2f9ecb14bfd28793e0d01831b4248cfd6dac5a953fed78f70599fd2d5.jpg)  
Figure 1. Timeline of the Two-Period Model

We assume that developers differ in terms of their fixed cost (??) of joining the platform—that is, developers have heterogeneous development costs. Hence, developers’ expected profit gained in period $i ( i \in \{ 1 , 2 \} )$ is formulated as

$$
\pi_ {D i} = R t _ {i} + \alpha N _ {A i} ^ {o} - p _ {d i} - c,\tag{1}
$$

where ?? represents developers’ basic expected revenue per unit of time, and $t _ { i }$ represents the length of the remaining demand window if the developer joins the market in period ?? : $t _ { 1 } = 1$ and $\begin{array} { r } { t _ { 2 } = \frac { 1 + \tau } { 2 } } \end{array}$ . Developers’ basic expected revenue per unit of time (??) measures whether developers have optimistic or pessimistic expectations regarding the revenue they will earn on the platform. With a larger (smaller) value of ?? , all developers have more optimistic (pessimistic) expectations. ?? represents the intensity of the network effects from the user side to the developer side, $N _ { A i } ^ { o } \ ( i \in$ {1, 2} ) denotes the number of users on the platform observed by developers when making participation decisions in period $i ( i \in \{ 1 , 2 \} )$ ), and ?? represents developers’ fixed cost of joining the platform. ?? also captures the overall expected profit that a developer will gain from a user, including subscription fees, advertisement revenues, in-app purchases, etc. In Period 1, when developers are making participation decisions, there are no users on the platform; thus, we have $N _ { A 1 } ^ { o } =$ 0. In Period 2, developers’ participation decisions are affected by the number of users who joined the platform in Period 1— that is, $N _ { A 2 } ^ { o } = N _ { A 1 } . p _ { d i } ( i \in \{ 1 , 2 \} )$ can be positive or negative, indicating the access fee charged or subsidy provided by the platform in period ??. Developers’ fixed cost ?? is assumed to be uniformly distributed over [0, ??]. Here, we assume that myopic developers cannot anticipate the future changes of the platform’s pricing strategy and a developer will join the platform when the developer’s expected profit is nonnegative. Thus, by solving $\pi _ { D 1 } \geq 0$ , the number of developers joining the platform in Period 1 (as shown in Figure 2a) is:

$$
N _ {D 1} = \frac {R - p _ {d 1}}{C}.\tag{2}
$$

In line with industry practice, it is assumed that developers who join the platform in Period 1 stay on the platform and do not pay the access fee (or receive a subsidy) again in Period 2. Thus, by solving $\pi _ { D 2 } \geq 0$ and deducting the number of developers joining in Period 1, the number of developers joining the platform in the Period 2 (as shown in Figure 2b) is given by:

$$
N _ {D 2} = \frac {1}{C} \left(\alpha N _ {A 1} - p _ {d 2} + p _ {d 1} + R \left(\frac {\tau - 1}{2}\right)\right)\tag{3}
$$

In Period 1, after observing the number of software available on the platform, the utility derived by users (per unit of time) after joining the platform is formulated as

$$
u _ {A 1} = v + \beta N _ {D 1} - f,\tag{4}
$$

where ?? is the basic value derived by users from joining the platform, ?? is the fee the user pays to join the platform, and ?? represents the intensity of the network effects from the developer side to the user side. Without loss of generality, we assume that each developer launches one app on the platform. ?? is assumed to be uniformly distributed over [0,1]. By solving $u _ { A 1 } \geq 0$ , the number of users joining in Period 1 is given by:

$$
N _ {A 1} = 1 + \beta N _ {D 1} - f\tag{5}
$$

Similarly, the users’ utility (per unit of time) derived in Period 2 is given by:

$$
u _ {A 2} = v + \beta (N _ {D 2} + N _ {D 1}) - f
$$

and the number of users in Period 2 is

(6)

$$
N _ {A 2} = 1 + \beta (N _ {D 2} + N _ {D 1}) - f\tag{7}
$$

The platform enjoys two revenue streams: access fees paid by developers and users. This study focuses on the software platform’s adoption of the skimming or penetration pricing strategy on the developer side. In particular, the platform determines the access fee charged or the subsidies offered to developers in the two periods $( p _ { d 1 } , p _ { d 2 } )$ to maximize its total profit. Accordingly, the platform’s optimization problem is given by

$$
\begin{array}{l} \max _ {p _ {d 1}, p _ {\mathrm{d} 2}} \pi = p _ {d 1} N _ {D 1} + p _ {d 2} N _ {D 2} \\ \qquad + f \left(\frac {1 - \tau}{2} N _ {A 1} \right. \\ \qquad + \frac {1 + \tau}{2} N _ {A 2}), \\ \qquad \text {s.t.} N _ {A 1}, N _ {A 2} \geq 0, N _ {D 1}, N _ {D 2} \geq 0. \end{array} \tag {8}
$$

In the following, we analyze the two cases in which the platform charges users an access fee $( f \neq 0 )$ or no access fee $( f = 0 )$ . Table 3 summarizes the key notations used in this study.

![](/api/attachments/5FNUFG6X/fulltext/images/03bc59fb94f2113ccc18cbf33cd986541fa2ba1985fce72d050ef5bdf3f56e0d.jpg)  
Figure 2. The Number of Developers Joining the Platform in the Two Periods

Table 3. Key Notations

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $v$ </td><td>Platform&#x27;s basic value for users,  $v \sim U[0,1]$ .</td></tr><tr><td> $R$ </td><td>Developers&#x27; basic expected revenue per unit of time.</td></tr><tr><td> $\tau_i (i \in \{1,2\})$ </td><td>Length of period  $i (i \in \{1,2\})$ .</td></tr><tr><td> $\tau$ </td><td>Difference in the lengths of the two periods,  $\tau \in (-1,1)$ .</td></tr><tr><td> $p_{di} (i \in \{1,2\})$ </td><td>Access fee charged or subsidy provided to developers in period  $i$ .</td></tr><tr><td> $\beta$ </td><td>Intensity of developer-to-user network effect.</td></tr><tr><td> $\alpha$ </td><td>Intensity of user-to-developer network effect.</td></tr><tr><td> $f$ </td><td>User&#x27;s access fee charged per unit of time.</td></tr><tr><td> $N_{Di} (i \in \{1,2\})$ </td><td>Number of developers joining the platform in period  $i (i \in \{1,2\})$ .</td></tr><tr><td> $N_{Ai}^o (i \in \{1,2\})$ </td><td>Number of users on the platform observed by developers when they make participation decisions in period  $i (i \in \{1,2\})$ .</td></tr><tr><td> $N_{Ai} (i \in \{1,2\})$ </td><td>Number of users joining the platform in period  $i (i \in \{1,2\})$ .</td></tr><tr><td> $\pi$ </td><td>Total profits gained by the platform in the two periods.</td></tr></table>

## 4 No User Access Fee

To encourage more users to participate, some software platforms do not charge their users any access fees, e.g., Steam, Wegame, and Firefox. Thus, in this section, we derive the platform’s optimal strategy if it charges no user access fees $( f = 0 )$ .

## 4.1 Optimal Pricing Strategy

By solving the optimization problem (Equation 8) with $f = 0$ , we have the optimal prices, the equilibrium numbers of developers and users in the two periods, and the optimal profit:<sup>4</sup>

$$
\left\{ \begin{array}{c} p _ {d 1} ^ {*} = \frac {4 C ^ {2} R + (C - \alpha \beta) (2 C \alpha + 2 R \alpha \beta + C R (\tau - 1))}{2 (3 C - \alpha \beta) (C + \alpha \beta)}, \\ p _ {d 2} ^ {*} = \frac {C (2 C \alpha + R \alpha \beta + C R \tau)}{(3 C - \alpha \beta) (C + \alpha \beta)}, \end{array} \right.\tag{9a}
$$

$$
\left\{ \begin{array}{l} N _ {D 1} ^ {*} = \frac {\alpha \beta (R + 2 \alpha + R \tau) - C (2 \alpha + R (\tau - 3))}{2 (3 C - \alpha \beta) (C + \alpha \beta)}, \\ N _ {A 1} ^ {*} = \frac {(2 C + R \beta) (3 C + \alpha \beta) + R \beta (\alpha \beta - C) \tau}{2 (3 C - \alpha \beta) (C + \alpha \beta)}, \end{array} \right. \left\{ \begin{array}{c} N _ {D 2} ^ {*} = \frac {2 C \alpha + R \alpha \beta + C R \tau}{(3 C - \alpha \beta) (C + \alpha \beta)}, \\ N _ {A 2} ^ {*} = \frac {6 + R \beta (3 + \tau)}{6 C - 2 \alpha \beta}. \end{array} \right.\tag{9b}
$$

$$
\pi^ {*} = \frac {2 R \alpha \beta (R + 2 \alpha + R \tau) + C \left(4 \alpha^ {2} + 4 R \alpha \tau + R ^ {2} (3 + \tau^ {2})\right)}{4 (3 C - \alpha \beta) (C + \alpha \beta)}.\tag{9c}
$$

To ensure that $N _ { D 1 } ^ { * } , N _ { D 2 } ^ { * } , N _ { A 1 } ^ { * } , N _ { A 2 } ^ { * } > 0$ , we assume $\alpha \beta <$ 3?? and $\begin{array} { r } { R > \frac { 2 \alpha \left( C - \alpha \beta \right) } { C \left( 3 - \tau \right) + \alpha \beta \left( 1 + \tau \right) } } \end{array}$ in the rest of the paper.<sup>5</sup> As mentioned in the introduction, the platform can adopt one of the following two pricing strategies: penetration pricing strategy, that is, setting a low introductory price in Period 1 and raising it in Period 2 (Cabral et al.,

1999), and skimming pricing strategy, that is, charging a higher price in Period 1 than in Period 2 (Jain et al.1999). By comparing the platform’s optimal prices in Equation (9), we have Proposition 1.

Proposition 1: If the platform charges users no access fee:

(a) the skimming pricing strategy is more profitable than the penetration strategy if and only if the intensity of the user-to-developer network effect is weak $\begin{array} { r } { ( 0 < \alpha \le \frac { ( 3 - \tau ) C R } { 2 ( C + R \beta ) } ) ; } \end{array}$

(b) otherwise, if the intensity of the user-todeveloper network effect satisfies ?? > $\begin{array} { r } { \frac { ( 3 - \tau ) C R } { 2 ( C + R \beta ) } } \end{array}$ , the platform should adopt the penetration pricing strategy.

Proposition 1 shows that whether the platform should adopt the penetration or skimming pricing strategy depends on the intensity of the user-to-developer network effect. If the intensity of the network effect from users to developers is too weak to significantly improve developers’ total expected benefit obtained in Period 2, to increase developers’ enthusiasm to join, the platform should set a lower access fee for developers in Period 2—that is, the skimming pricing strategy is more profitable, as shown in Figure 3. This strategy allows the platform to first attract innovative developers who have lower development costs; then, when the platform decreases the access fee in Period 2, after observing the number of users joining in Period 1, developers with relatively higher development costs will join, allowing the market to expand in this period.

on the platform that no one would join the platform in Period 1. To rule out this trivial case, our analysis is conducted under the assumption $\begin{array} { r } { R > \frac { 2 \alpha \left( C - \alpha \beta \right) } { C \left( 3 - \tau \right) + \alpha \beta \left( 1 + \tau \right) } . } \end{array}$

![](/api/attachments/5FNUFG6X/fulltext/images/b3e157399a81bbbdbb4ccd05c1e8958543b716605596b8543c98a78fa68b04b8.jpg)  
Figure 3. The Platform’s Optimal Pricing Strategy $( \beta = 0 . 5 , \tau = 0 . 2 , C = 1 )$

If users’ impacts on developers are strong ( ?? > $\frac { C R ( 3 - \tau ) } { 2 ( C + R \beta ) } )$ ), the platform is better off setting a lower introductory access fee to increase developers’ enthusiasm for joining the platform and subsequently attracting more users in Period 1. Then, by utilizing the strong impact of users on developers, the willingness of the remaining developers to join the platform will be significantly enhanced in Period 2. Therefore, the platform will be able to increase the access fee in this period. This finding is consistent with our observations. Steam, the largest PC gaming platform, adopts the penetration pricing strategy. It first charged developers a low access fee—for \$100 they could submit as many games as they wanted to. This lowaccess-fee strategy was successful. A large number of game developers and gamers joined the platform. In 2016, an average game on Steam sold 6,640 copies and earned \$25,245 in revenue (Galyonkin, 2017). Later, Steam raised the access fee, charging developers \$100 per game in 2017, when its revenue increased by \$800 million, compared with 2016 (Galyonkin, 2018).

The penetration pricing strategy is commonly adopted for information goods showing direct network effects (Winter & Sundqvist, 2010). For instance, CompuServe, a commercial online service provider, set a low access fee for consumers in its early market period and then raised it (Cabral et al., 1999). However, the skimming pricing strategy is relatively more commonly adopted for physical goods, such as luxury cars and electronic devices. Proposition 1 indicates that in platform markets with cross-side network effects, both penetration and skimming pricing strategies are viable.

As shown by the optimal solutions in Equation (9a), the platform’s optimal pricing structure also depends on the developer-to-user network effect ( ?? ), the difference between the lengths of the two periods (??), and developers’ basic expectations of the revenue per unit of time (??). Thus, we analyze the impacts of the changes in these variables on the optimal pricing strategy; the results are summarized in Proposition 2.

## Proposition 2:

(a) As the intensity of the developer-to-user network effect (??) increases, the platform is more likely to adopt penetration pricing.

(b) As the length of Period 2 becomes longer (?? increases), the platform is more likely to adopt penetration pricing.

(c) As developers’ basic expectations of the revenue gained per unit of time (??) increase, the platform will be more willing to adopt skimming pricing.

Proposition 1 reveals that the platform becomes more likely to adopt the penetration pricing strategy as the user-to-developer network effect becomes stronger, because the platform tends to leverage a strong network effect to charge a high price in Period 2. For the same reason, as shown in Proposition 2(a), when the effect of developers on users becomes stronger, the platform is more likely to utilize a low access fee to entice more developers and users to join in Period 1, which subsequently enhances the willingness of developers to join in Period 2. Thus, penetration pricing is more likely to be adopted by the platform as the developer-to-user network effect intensifies.

A larger ?? indicates that the length of Period 2 gets longer while the length of Period 1 gets shorter. As the length of Period 2 increases, developers’ expectations about the revenue that will be gained in this period improve. Thus, the platform will be more likely to set a higher Period 2 price, owing to developers’ increased willingness to participate in Period 2. In other words, if Period 2 becomes longer, the penetration pricing strategy will likely outperform the skimming pricing strategy.

Proposition 2(c) shows an interesting finding that the platform prefers the skimming pricing more than the penetration pricing when developers have more optimistic expectations. As ?? increases, all developers joining in the two periods will have more optimistic expectations regarding their future earnings. Further, increases in the basic expected revenue of developers who join in Period 1 will be larger than that of developers who join in Period 2 because of the longer service period. Thus, the platform will be better off setting a higher price in Period 1. Therefore, the platform will more likely adopt skimming pricing as developers’ earning expectations become more favorable.

Based on the optimal solutions (Equation 9), the conditions under which the platform should subsidize developers are derived and summarized in Proposition 3.

Proposition 3: When the platform charges no user access fee:

(a) if the platform adopts the skimming pricing strategy $\begin{array} { r } { ( 0 < \alpha < \frac { \dot { 3 } C R - C R \tau } { 2 ( C + R \beta ) } ) } \end{array}$ , it should charge the developers during both periods;

(b) if the platform adopts the penetration pricing strategy, the platform should charge the developers in Period 2 and in Period 1,

(i) if the intensity of the user-to-developer network effect is sufficiently weak $\begin{array} { r } { ( \ \frac { 3 C R - C R \tau } { 2 \left( C + R \beta \right) } < \alpha \leq C / \beta \ ) } \end{array}$ , the platform should charge the developers, i.e., $p _ { d 1 } ^ { * } >$ 0;

(ii) if the intensity of the user-to-developer network effect is moderate $( C / \beta < \alpha <$ $\frac { c \left( 3 - \tau + \sqrt { 3 3 + \tau ( 2 + \tau ) } \right) } { 4 \beta } \ )$ and developers have a relatively pessimistic expectation $\begin{array} { r } { ( ~ 0 < R \le \frac { 2 C \alpha ( \alpha \beta - C ) } { 4 C ^ { 2 } + ( 2 \alpha \beta - C ( \tau - 1 ) ) ( C - \alpha \beta ) } ~ ) . } \end{array}$ the platform should subsidize developers;

(iii) if the intensity of the user-to-developer network effect is strong $\begin{array} { r } { ( \ \frac { C \left( 3 - \tau + \sqrt { 3 3 + \tau ( 2 + \tau ) } \right) } { 4 \beta } \leq \alpha < 3 C / \beta ) } \end{array}$ the platform would be better off subsidizing developers.

In this case, because the platform charges no user access fees, developers’ access fees are the platform’s sole source of revenue; thus, the platform should charge developers in at least one period. In Period 2, subsidizing developers can boost user participation but cannot benefit the platform in terms of profit. Hence, the platform should charge developers in this period, regardless of whether it adopts the skimming or penetration pricing strategy.

When the intensity of the user-to-developer network effect is insignificant $\begin{array} { r } { ( 0 < \alpha \leq \frac { 3 C R - C R \tau } { 2 ( C + R \beta ) } ) } \end{array}$ , the increased profit derived in Period 2 as a result of subsidizing developers in Period 1 cannot offset the costs; thus, regardless of whether the platform adopts the skimming or penetration pricing strategy, charging developers in Period 1 is the platform’s optimal strategy. The network effect from users to developers functions as a bridge connecting the two periods, and with its increase, the platform should devote more effort to getting more users on board in Period 1. Therefore, as shown in Figure 3, when the platform adopts the penetration pricing strategy and the intensity of the user-to-developer network effect is sufficiently strong $\begin{array} { r } { ( \frac { C \left( 3 - \tau + \sqrt { 3 3 + \tau ( 2 + \tau ) } \right) } { 4 \beta } \leq \alpha < \frac { 3 C } { \beta } ) } \end{array}$ , to utilize users’ significant impacts on developers, the platform is better off subsidizing developers in Period 1. As users impacts on developers are moderate $( \frac { C } { \beta } < \alpha <$ $\frac { C { \left( 3 - \tau + \sqrt { 3 3 + \tau ( 2 + \tau ) } \right) } } { 4 \beta } )$ , whether to charge or subsidize developers in Period 1 depends on developers’ basic expected revenue per unit of time. Intuitively, the platform should subsidize developers if they have a relatively pessimistic expectation of the revenue they will likely earn.

## 4.2 Comparative Analysis

Based on comparative static analysis, we have the following lemmas, revealing the impacts of the changes in four exogenous parameters, i.e., developers’ basic expected revenue per unit of time (??), the difference in the lengths of the two periods (??), and the intensities of the cross-side network effects (?? and $\beta ) _ { ; }$ , on the platform’s optimal price and profit as well as the number of developers and users joining in the two periods.

Lemma 1: As developers’ basic expected revenue per unit of time (??) increases, (a) in Period 1,

$$
\begin{array}{r l} & {\mathrm{if} 0 <   \alpha <   \frac {C (3 - \tau + \sqrt {3 3 + \tau (2 + \tau)})}{4 \beta}, \mathrm{wehave}} \\ & {\frac {\partial p _ {d 1} ^ {*}}{\partial R} > 0; \mathrm{if} \frac {C (3 - \tau + \sqrt {3 3 + \tau (2 + \tau)})}{4 \beta} \leq \alpha <   \frac {3 C}{\beta},} \\ & {\mathrm{wehave} \frac {\partial p _ {d 1} ^ {*}}{\partial R} \leq 0;} \end{array}\tag{i}
$$

$$
\mathrm{(ii)} \quad \frac {\partial N _ {D 1} ^ {*}}{\partial R} > 0, \frac {\partial N _ {A 1} ^ {*}}{\partial R} > 0;
$$

(b) in Period 2, we have $\begin{array} { r } { \frac { \partial p _ { d 2 } ^ { * } } { \partial R } > 0 , \frac { \partial N _ { D 2 } ^ { * } } { \partial R } > 0 , \frac { \partial N _ { A 2 } ^ { * } } { \partial R } > } \end{array}$ $0 ;$

(c) the platform’s total profit will increase, i.e., $\begin{array} { r } { \frac { \partial \pi ^ { * } } { \partial R } > 0 . } \end{array}$

Lemma 1 indicates that when the platform charges no user access fees, as developers become more optimistic about the revenue they will earn on the platform, the optimal price in Period 1 will increase if the intensity of the user-to-developer network effect is weak or moderate $\begin{array} { r } { ( 0 < \alpha < \frac { C ( 3 - \tau + \sqrt { 3 3 + \tau ( 2 + \tau ) } ) } { 4 \beta } ) } \end{array}$ , and decrease otherwise $\begin{array} { r l } { ( } & { { } \frac { C ( 3 - \tau + \sqrt { 3 3 + \tau ( 2 + \tau ) } ) } { 4 \beta } \leq \alpha < \frac { 3 C } { \beta } } \end{array} )$ The platform’s optimal price in Period 2 will increase with developers’ more optimistic earning expectations.

The reason is as follows. In Period 2, if developers have more optimistic expectations about the revenue they will earn, they will be more willing to join the platform; thus, the platform should raise the optimal price in Period 2. In Period 1, the effects of developers’ expected revenue per unit of time are more complicated. A low access fee charged in Period 1 can affect the profit gained in Period 2 in two ways. First, low access fees can entice both developers and users to join in Period 1, thus enhancing the network value of the platform for developers in Period 2. Second, developers joining the platform in the two periods come from the same pool; thus, the decreased Period 1 access fee will shrink Period 2’s potential market size on the developer side. In this case, with an increase in developers’ basic expected revenue, the platform faces a dilemma between a higher platform network value $f o r$ developers and a larger potential pool of developers in Period 2.

If the intensity of the user-to-developer network effect is not significantly high $\begin{array} { r } { ( 0 < \alpha < \frac { C ( 3 - \tau + \sqrt { 3 3 + \tau ( 2 + \tau ) } ) } { 4 \beta } ) } \end{array}$ the incremental network value for developers, resulting from a low access fee in Period 1, will not be large enough to entice a sufficient number of developers to join in Period 2. Hence, the platform should raise the Period 1 access fee as developers become more optimistic about the revenue they will earn in order to guarantee a large enough potential market size in Period 2. However, if users’ impacts on developers are sufficiently strong $\begin{array} { r } { \mathrm { ( ~ } \frac { C ( 3 - \tau + \sqrt { 3 3 + \tau ( 2 + \tau ) } ) } { 4 \beta } \leq \alpha < \frac { 3 C } { \beta } \mathrm { ~ ) } } \end{array}$ decreasing the price in Period 1 will entice more developers and users to join in this period and will largely improve the platform’s network value and enhance developers’ willingness to join the platform in Period 2. Therefore, as ?? increases, the platform should decrease the access fee charged or increase the subsidy offered in Period $\begin{array} { r } { 1 \mathrm { { i f } } \frac { C ( 3 - \tau + \sqrt { 3 3 + \tau ( 2 + \tau ) } ) } { 4 \beta } \leq \alpha < \frac { 3 C } { \beta } . } \end{array}$

Lemma 2 analyzes the effects of the changes in the lengths of the two periods (??) on the optimal price, profit, and numbers of platform participants in the two periods.

Lemma 2: As Period 2 becomes longer (?? increases),

(a) in Period 1, if $0 < \alpha < C / \beta$ , we have $\frac { \partial p _ { d 1 } ^ { * } } { \partial \tau } >$ $\begin{array} { r } { 0 , \frac { \partial N _ { D 1 } ^ { * } } { \partial \tau } < 0 , \frac { \partial N _ { A 1 } ^ { * } } { \partial \tau } < 0 ; \mathrm { i f } \leq \alpha < } \end{array}$ , we have $\begin{array} { r } { \frac { \partial p _ { d _ { 1 } } ^ { * } } { \partial \tau } \leq 0 , \frac { \partial N _ { D _ { 1 } } ^ { * } } { \partial \tau } \geq 0 , \frac { \partial N _ { A _ { 1 } } ^ { * } } { \partial \tau } \geq 0 ; } \end{array}$

(b) in Period $\begin{array} { r } { 2 , \frac { \partial p _ { d 2 } ^ { * } } { \partial \tau } > 0 , \frac { \partial N _ { D 2 } ^ { * } } { \partial \tau } > 0 , \frac { \partial N _ { A 2 } ^ { * } } { \partial \tau } > 0 ; } \end{array}$

(c) the platform’s total profit will increase, i.e., $\begin{array} { r } { \frac { \partial \pi ^ { * } } { \partial \tau } > 0 . } \end{array}$

Lemma 2 indicates that when the length of Period 2 becomes longer (the length of Period 1 becomes shorter), $p _ { d 1 } ^ { * }$ will increase if the user-to-developer network effect is weak $( 0 < \alpha < C / \beta )$ and decrease otherwise $( C / \beta \le \alpha < 3 C / \beta )$ , and the optimal price in Period $2 ~ ( p _ { d 2 } ^ { * } )$ increases under all conditions. It is intuitive that as the length of Period 2 increases, developers will expect to earn higher revenues in this period because of a longer remaining demand window; thus, the platform is better off raising the optimal price in Period 2.

The length of the demand window for developers who join in Period 1 remains unchanged, given a fixed total length of the two periods. However, as ?? increases, the optimal Period 1 price may increase or decrease, depending on the intensity of the user-to-developer network effect. Because of the increased Period 2 price, the platform has the incentive to accept more developers during this period. Theoretically, there are two possible ways to get more developers on board in Period 2: first, increase the Period 1 price to ensure that more developers will wait to join in Period 2; second, decrease the Period 1 price to entice more developers and users to join in Period 1 and then leverage the userto-developer network effect to attract more developers in Period 2. Whether the first or second option will be more effective depends on the intensity of the user-todeveloper network effect. When the intensity of the user-to-developer network effect is too weak $( 0 < \alpha <$ $\ C / \beta )$ to increase developers’ enthusiasm to join in Period 2, as ?? increases, the platform should raise the Period 1 price to enlarge the developer pool in Period 2. When the user-to-developer network effect is sufficiently strong $( C / \beta \le \alpha < 3 C / \beta )$ , as Period 2 becomes longer, the platform will be better off decreasing the Period 1 price to improve the network value of the platform to developers in Period 2 by leveraging the strong network effect.

Table 4. Effects of an Increase in ?? on Optimal Prices and Profits

<table><tr><td></td><td> $p_{d1}^{*}$ </td><td> $p_{d2}^{*}$ </td><td> $\pi_{1}^{*}$ </td><td> $\pi_{2}^{*}$ </td><td> $\pi^{*}$ </td></tr><tr><td> $\alpha \uparrow$ </td><td>↓</td><td>↓↑</td><td>↓↑↓</td><td>↑</td><td>↑</td></tr></table>

![](/api/attachments/5FNUFG6X/fulltext/images/54bcb0d401c7199095f47dafc8454895dc286b40eba8138ceb7d4e77edc90814.jpg)

![](/api/attachments/5FNUFG6X/fulltext/images/df1274ac03a154c63ccc224848ce25341420f891339a945363c43706f9eb7553.jpg)  
Figure 4. The Impacts of the User-to-Developer Network Effect (??) on the Optimal Prices and Profits in the Two Periods (?? = ??. ??, ?? = ??, ?? = ??. ??, ?? = ??)

Lemma 3 analyzes the effects of the intensity of the user-to-developer network effects on the optimal price, profit, and number of platform participants in the two periods. We define a threshold of the intensity of the user-to-developer network effect:

$$
\alpha^ {\prime} = \frac {C \beta (R \beta (\tau - 3) - 6 C) + 2 \sqrt {C ^ {2} \beta^ {2} (2 C + R \beta (1 - \tau)) (6 C + R \beta (3 + \tau))}}{\beta^ {2} (2 C + R \beta (1 + \tau))}.
$$

Lemma 3: Table 4 summarizes the effects of an increase in the intensity of the user-to-developer network effect on the platform’s optimal prices and profit.

Lemma 3 indicates that the impact of the increase in the intensity of the user-to-developer network effect on the optimal price in Period 1 is nonmonotonic i.e., $p _ { d 1 } ^ { * }$ will first increase $( 0 < \alpha < \alpha ^ { \prime } )$ and then decrease $( \alpha \geq \alpha ^ { \prime } )$ with the increase in ??. However, the optimal price in Period 2 always increases with a stronger user-todeveloper network effect, as shown in the left panel in Figure 4. This finding on the optimal price in Period 2 is intuitive, but the finding on the optimal price in Period 1 is counterintuitive. When the intensity of the user-todeveloper network effect satisfies $0 < \alpha < \alpha ^ { \prime }$ , even if it has increased, it is too weak to significantly enhance developers’ willingness to join the platform and expand the market in Period 2 through a decrease in the Period 1 price. Thus, as the impacts of users on developers become stronger, the platform should increase the Period 1 price to ensure a sufficiently large size of the market potential of developers in Period 2. When $\alpha \geq$ $\alpha ^ { \prime } { \mathrm { . } }$ the intensity of the user-to-developer network effect is so strong that developers are relatively insensitive to changes in the Period 2 prices. Thus, as ?? increases, the platform should decrease the Period 1 price, attempting to entice more developers and users to join in this period and then utilize the strong impacts of users on developers to increase profits in Period 2. Furthermore, according to Lemma 3, as the impacts of users on developers become salient, the profit derived in Period 1 will decrease first $( 0 < \alpha \leq \alpha ^ { \prime } )$ , and then increase $( \alpha ^ { \prime } < \alpha < \frac { C } { \beta } ) _ { } .$ , and finally decrease $\begin{array} { r } { \big ( \frac { 1 } { \beta } \leq \alpha < \frac { 3 C } { \beta } \big ) . } \end{array}$ . The profit gained in Period 2 will monotonically increase (as shown in the right panel in Figure 4), as will the total profit, indicating that when the intensity of network effects from users to developers falls into low- or highrange intervals, as the intensity increases, the platform can achieve higher total profits by sacrificing profits in Period 1.

Analyzing the impacts of the network effect from the developer side to the user side on the platform’s optimal prices and profits leads to Lemma 4. We define a threshold of the intensity of the developer-to-user network effect:

$$
\beta^ {\prime} = \frac {R \alpha (\tau - 3) + 2 \left(\alpha^ {2} + \sqrt {\alpha^ {2} (R - 2 \alpha - R \tau) (3 R + 2 \alpha + R \tau)}\right)}{\alpha^ {2} (R + 2 \alpha + R \tau)}.
$$

Lemma 4: Table 5 summarizes the effects of an increase in the intensity of the developer-to-user network effect on the platform’s optimal prices and profit.

Some of the results in Lemma 4 are noteworthy. For instance, when developers have pessimistic expectations about the basic revenue they will gain (?? ≤ $\frac { 2 \bar { \alpha } } { 1 - \tau } )$ , as the intensity of the developer-to-user network effect increases, the optimal Period 1 price decreases. However, the impact of the increase in $\beta$ on the optimal price in Period 2 is nonmonotonic, i.e., $p _ { d 2 } ^ { * }$ first decreases and then increases, as shown in Figure 5a.

Table 5. Effects of an Increase in ?? on Optimal Prices and Profit

<table><tr><td></td><td> $p_{d1}^{*}$ </td><td> $p_{d2}^{*}$ </td><td> $\pi^{*}$ </td></tr><tr><td> $R \leq \frac{2\alpha}{1 - \tau}$ </td><td>↓</td><td>↓↑</td><td>↑</td></tr><tr><td> $R > \frac{2\alpha}{1 - \tau}$ </td><td>↑↓</td><td>↑</td><td>↑</td></tr></table>

![](/api/attachments/5FNUFG6X/fulltext/images/9885d914550771ce65e88112c0381e04c1e395cbd6b3d82f5f5880c77011047e.jpg)

![](/api/attachments/5FNUFG6X/fulltext/images/74846bb363184d14a0889bfdedf9c3ca4adcb569e86940d56b6664be2f677961.jpg)

![](/api/attachments/5FNUFG6X/fulltext/images/90e2b943ee92d26c686fe50d8035969b0c1544ce9028ce3b419c6ebb0bb08ad0.jpg)  
(a) Developers have low expectations about basic revenue with ?? = ??, ?? = ??, ?? = ??, ?? = ??.

![](/api/attachments/5FNUFG6X/fulltext/images/c98d17de680a31f8ad19782da5aa3c7255f781ba08095eb91c33c6fac7ad90ea.jpg)  
(b) Developers have high expectations about basic revenue with ?? = ??, ?? = ??, ?? = ??, ?? = ??.  
Figure 5. Impacts of the Developer-to-User Network Effect (??) on the Optimal Prices in the Two Periods

The explanation is as follows. When developers have pessimistic expectations about revenue, they will have less enthusiasm to join the platform. As ?? increases, to make full use of it, the platform should reduce the price in Period 1. The market sizes on both the developer and user sides in Period 1 get larger. As ?? increases, the changes in the Period 2 price are determined by the intertemporal price competition between the two periods and the intensity of the developer-to-user network effect. Reduction in the Period 1 price brings downward pressure to the Period 2 price since the developers who join in Period 2 are expected to have higher development costs. Even if more users join the platform in Period 1, as the intensity of the network effects from developers to users increases in the lowrange interval, it will be too weak to significantly increase developers’ willingness to join in Period 2.

Thus, the platform should reduce the price in this period to prevent the number of participating developers from shrinking. When the intensity of the network effect increases to a strong interval, even developers with high development costs will be relatively insensitive to the Period 2 price because of the high network value of the platform, and the platform will thus be better off increasing the price in Period 2.

As shown in Figure 5(b), when developers have optimistic expectations about the revenue they will gain $( R > 2 \alpha / ( 1 - \tau ) )$ ), as developers’ impacts on users become stronger, the optimal price in Period 1 first increases and then decreases. The platform’s optimal price in Period 2 increases with a stronger developer-to-user network effect.

## 5 If Users Are Charged an Access Fee or Offered a Subsidy

As mentioned earlier, some software platforms charge an access fee from the software users. In this section, we study the case where users are charged an access fee or provided with a subsidy $( f \neq 0 )$ . We derive the optimal solutions by resolving the optimization problem (Equation 8) through Equations 10a-c (see below).

By analyzing the optimal solutions (Equation 10), we have Proposition 4, which characterizes the conditions under which the platform should charge or subsidize users. Define a threshold: $\begin{array} { r } { \alpha _ { f } = \frac { R \beta ^ { 2 } ( 1 + \bar { \tau } ) + C \beta ( 2 + \tau ) - C R \tau } { 4 C + 2 R \beta } + } \end{array}$ 1 ቀ(????<sup>2</sup>(1+??)+????(2+??)−??????)<sup>2</sup>+2(2??+????)(6??+????(3+??<sup>2</sup>))ቁ<sup>2</sup> 4??+2????

Proposition 4. The platform should charge users if and only if the intensity of the user-to-developer network effect is weak $( \alpha < \alpha _ { f } ) ;$ otherwise, subsidizing developers is a better choice.

Charging users an access fee leads to both positive and negative effects. The positive effect is that the platform can gain profits on both the user and developer sides. The negative effect is that users’ willingness to join in Period 1 becomes lower, which, subsequently, reduces developers’ willingness to join in Period 2. If users have insignificant impacts on developers $( \alpha < \alpha _ { f } ) .$ , the negative effect is weak. To leverage the positive effect, the platform should charge users and focus on making more profit on the user side. If the intensity of the userto-developer network effect is strong, the negative effect of charging users an access fee is significant and reduces the participation of developers in Period 2. Thus, to weaken the negative effect, the platform should subsidize users and focus on making profits on the developer side only.

Proposition 5 shows how the changes in developers basic expectation of the revenue gained per unit of time (??) affect the optimal access fee charged to users $( f ^ { * } )$ ).

Proposition 5. If the user-to-developer network effect is weak $\begin{array} { r } { ( \alpha < \frac { \beta ^ { 2 } ( 1 + \tau ) - C \tau + \sqrt { 2 C \beta ^ { 2 } ( 3 - \tau ) + C ^ { 2 } \tau ^ { 2 } + \beta ^ { 4 } ( 1 + \tau ) ^ { 2 } } } { 2 \beta } ) , } \end{array}$ , as developers’ basic expectation of the revenue gained per unit of time (??) increases, the platform should raise the access fee charged from (or decrease the subsidy offer to) users; otherwise, the platform should decrease the access fee (or increase the subsidy).

As ?? increases, developers have more optimistic expectations of future revenue and will thus be more willing to join the platform. More developers joining in Period 1 will enhance users’ willingness to join in this period. If the impact of users on developers is weak, charging users a higher price will not significantly reduce developers’ enthusiasm to participate. Therefore, in this case, the platform should charge users a higher access fee (or offer them lower subsidies) to increase profits. If the user-to-developer network effect is strong, charging users a higher price will significantly reduce developers’ willingness to join in Period 2. Thus, by leveraging the strong network effect, the platform will be better off decreasing the access fee charged to users (or increasing their subsidy) in order to expand the market size on the developer side as ?? increases.

Equations 10 a-c

$$
\left\{ \begin{array}{c} p _ {d 1} ^ {*} = \frac {C ^ {2} (2 \alpha + \beta (\tau - 3) + 2 R (3 + \tau)) - C (2 \alpha \beta^ {2} (1 + \tau) + R (2 \alpha^ {2} - \alpha \beta (5 + \tau) + \beta^ {2} (3 + \tau^ {2})) - 2 R \alpha \beta^ {3} (1 + \tau))}{1 2 C ^ {2} - 2 \alpha \beta^ {3} (1 + \tau) - C (4 \alpha^ {2} - 4 \alpha \beta (2 + \tau) + \beta^ {2} (3 + \tau^ {2}))}, \\ p _ {d 2} ^ {*} = \frac {2 R \alpha \beta^ {2} (1 + \tau) (\alpha - \beta - \beta \tau) + C ^ {2} (8 \alpha + 8 R \tau - 2 \beta (3 + \tau)) - C \beta (2 \alpha (1 + \tau) (\beta (2 + \tau) - 2 \alpha) + R (\beta (1 + \tau) (3 + \tau^ {2}) - 2 \alpha (2 + \tau + \tau^ {2}))}{2 4 c ^ {2} - 4 \alpha \beta^ {3} (1 + \tau) - 2 c (4 \alpha^ {2} - 4 \alpha \beta (2 + \tau) + \beta^ {2} (3 + \tau^ {2}))}, \\ f ^ {*} = \frac {(2 C + R \beta) (3 C + 2 \alpha (\beta - \alpha)) + 2 \alpha (R \beta^ {2} + C (\beta - R)) \tau + C R \beta \tau^ {2}}{1 2 C ^ {2} - 2 \alpha \beta^ {3} (1 + \tau) - C (4 \alpha^ {2} - 4 \alpha \beta (2 + \tau) + \beta^ {2} (3 + \tau^ {2}))}. \end{array} \right.\tag{10a}
$$

$$
\left\{ \begin{array}{l l} N _ {D 1} ^ {*} = \frac {C ((2 R + \beta) (3 - \tau) - 2 \alpha) + \alpha (3 R \beta (1 + \tau) - 2 R \alpha + 2 \beta^ {2} (1 + \tau))}{1 2 C ^ {2} - 2 \alpha \beta^ {3} (1 + \tau) - C (4 \alpha^ {2} - 4 \alpha \beta (2 + \tau) + \beta^ {2} (3 + \tau^ {2}))}, \\ N _ {D 2} ^ {*} = \frac {2 (\alpha (2 C + R \beta) + (2 R + \beta) C \tau)}{1 2 C ^ {2} - 2 \alpha \beta^ {3} (1 + \tau) - C (4 \alpha^ {2} - 4 \alpha \beta (2 + \tau) + \beta^ {2} (3 + \tau^ {2}))}. \end{array} \right.\tag{10b}
$$

$$
\left\{ \begin{array}{l l} N _ {A 1} ^ {*} = \frac {6 C ^ {2} + R \alpha \beta^ {2} (1 + \tau) + C (2 R \alpha \tau + R \beta (1 - \tau) (3 + \tau) + \beta (1 + \tau) (2 \alpha - \beta \tau))}{1 2 C ^ {2} - 2 \alpha \beta^ {3} (1 + \tau) - C (4 \alpha^ {2} - 4 \alpha \beta (2 + \tau) + \beta^ {2} (3 + \tau^ {2}))}, \\ N _ {A 2} ^ {*} = \frac {3 (2 + R \beta) (C + \alpha \beta) + (2 C R \alpha + 2 C (R + \alpha) \beta + (C + R \alpha) \beta^ {2}) \tau - C \beta (R + \beta) \tau^ {2}}{1 2 C ^ {2} - 2 \alpha \beta^ {3} (1 + \tau) - C (4 \alpha^ {2} - 4 \alpha \beta (2 + \tau) + \beta^ {2} (3 + \tau^ {2}))}. \end{array} \right.\tag{10c}
$$

![](/api/attachments/5FNUFG6X/fulltext/images/c241691bb22351f215f6e174992cf9fcfc513540d9b3a27c3c49fa7a6ff474e0.jpg)  
Figure 6. Optimal Pricing Strategy When ?? ≠ ?? (?? = ??. ??, ?? = ??. ??, ?? = ??)

Compared with the findings in Proposition 1, the impacts of the user-to-developer network effect (??) on the optimality of the pricing strategies remain qualitatively unchanged—that is, the skimming strategy outperforms the penetration strategy if the user-todeveloper network effect is weak, as shown in Figure 6.

Analogous to Proposition 3, we reexamine whether the platform should subsidize or charge developers if it charges users an access fee (or subsidizes users).

Lemma 5: If users are charged an access fee or offered a subsidy, if the user-to-developer network effect is sufficiently weak $( \alpha \leq \underline { { \alpha } } _ { 1 } )$ or strong $( \alpha \geq \overline { { \alpha } } _ { 1 } ) ,$ 6 the platform should subsidize developers in Period 1; if the user-to-developer network effect is moderate, the platform should charge developers in Period 1.

Compared with the findings in Proposition 3, Lemma 5 shows that when users are charged an access fee or offered a subsidy, the platform should subsidize developers in Period 1 if the user-to-developer network effect is strong. However, different from the finding in Proposition 3, if the intensity of the user-to-developer network effect is sufficiently weak, the platform should subsidize rather than charge developers in Period 1, as shown in Figure 7a. When charging/subsidizing users, the platform treats the user side as a profit center when the user-to-developer network effect is weak (as shown in Proposition 4). Compared with charging developers in Period 1, subsidizing them not only improves the platform’s profit gained from the developer side in Period 2 but also stimulates users’ participation. Hence, when the user-to-developer network effect is weak, subsidizing developers is more profitable and the platform earns a large proportion of revenue from the user side.

From the numerical results shown in Figure $^ { 7 , }$ we can observe that the platform should subsidize developers if the user-to-developer network effect is weak or strong in Period 1, and it should charge developers in Period 2 if the user-to-developer network effect is strong. When the platform charges or subsidizes users, the platform can earn profits from both developers and users in both periods. Thus, in contrast with the case of no access fee being charged or subsidy being provided on the user side, the platform will have more diversified pricing strategies on the developer side in Period 2.

There exists a counterintuitive finding that the platform charges developers in Period 1 and subsidizes new entrants in Period 2 when the user-to-developer network effect is moderate. The reason for this finding is as follows. Developers who join the platform in Period 1 are likely those with low development costs. In Period 2, the remaining interested developers likely have relatively high development costs. Remember that the user-to-developer network effect is moderate in this case. To attract these high-cost, low-incentive developers and to leverage their impacts on user participation, the platform will be better off subsidizing developers in Period 2. The profits gained from users should more than cover the subsidies offered to developers in Period 2. This strategy can be observed in practice. Microsoft first charged developers for using the Developer Edition of SQL Server. This strategy attracted developers with low development costs and ensured that the platform earned revenue. Then SQL Server gained the second largest market share in the database management system market in 2015 (Adrian, 2016). Afterward, Microsoft began to offer the Developer Edition of SQL Server for free (since 2016), and thus boosted the participation of developers and users. Now, over 34,401 websites (users) are built on the SQL Server. <sup>7</sup>

![](/api/attachments/5FNUFG6X/fulltext/images/66953d4b3978dd3d7b16a552f97875b5c5bf6166dd31d857c4975d74df89e517.jpg)  
(a) In Period 1

![](/api/attachments/5FNUFG6X/fulltext/images/1530820349001277030e82e30ac8dfaafd72dc90e65c8d980f8f9a11605974bb.jpg)  
(b) In Period 2  
Figure 7. Subsidizing or Charging Developers in the Two Periods (?? = ??. ??, ?? = ??, ?? = ??)

![](/api/attachments/5FNUFG6X/fulltext/images/f0eb6e2a705e579228de2e8897ab884ede0d116b3239989179df78e94fb2caee.jpg)  
(a) Effect of ?? on ??<sup>∗</sup>

![](/api/attachments/5FNUFG6X/fulltext/images/fb5a94f100b4085a27b597969c3ccb047b1f32eac1b1fb6aba487d00a28c3ecd.jpg)  
(b) Effect of ?? on Pricing Strategy  
Figure 8. Optimal Access Fee Charged to Users and Pricing Strategy Under Different ?? (?? = ??. ??, ?? = ??, ?? = ??)

By numerical experiments, we find that as the length of Period 2 increases (?? increases), the platform’s optimal access fee charged to users first declines and then increases, as shown in Figure 8(a). Developers will likely be more willing to join in Period 2 if the period becomes longer. Due to the cross-side network effect, users also have more incentives to join in Period 2. Thus, it seems intuitive that the platform should raise the user access fee at this time. However, the platform may choose an alternative strategy: charging a higher price to developers in Period 2. In this case, the platform benefits from charging a lower access fee to users to further enhance developers’ incentives to join in Period 2. Therefore, the increase in Period 2’s length has a nonmonotonic effect on the optimal access fee charged to users. When Period 2 is short, the optimal access fee decreases as it increases in length.

We also analyze how a prolonged Period 2 affects the optimality of the skimming or penetration pricing strategy through numerical experiments, as shown in Figure 8(b). We can conclude that when the platform charges users access fees or provides subsidies to them, as ?? increases, the platform’s willingness to adopt the skimming pricing strategy first decreases and then increases. Compared with Proposition 2, when ?? is short, the platform is also less likely to adopt the skimming pricing strategy as ?? increases. However, when the length of Period 2 is sufficiently long, the platform is more likely to adopt the skimming strategy as ?? increases. In this case, the platform treats the user side as a profit center, and the access fee charged to users increases with ??. As Period 2 becomes longer, the platform reduces the price charged to developers to attract more developers, which, subsequently, enhances users’ incentives to participate. Thus, in this case, the skimming pricing strategy will be more likely to be adopted as Period 2 gets longer.

## 6 Extensions and Conclusions

## 6.1 Summary of Extensions

We develop four extension models to account for potential variations on our primary assumptions. Extension 1 assumes that the platform has users before third-party developers begin participating. Extension 2 considers potential competition between developers and the same-side network effect. Extension 3 investigates the scenario in which platforms charge developers transaction fees. Extension 4 assumes that the platform charges different access fees to users in the two periods. We found that our main findings on the pricing strategy of the software platform remain qualitatively valid under these extensions. Further details regarding these extension models are provided in Appendix B.

## 6.2 Findings

Developers have begun to invert the firm, as they have become key to the rapid scaling of software platform firms and are now central to the success of platform firms (Parker et al., 2017). Hence, the pricing strategy on the developer side plays an important role in the development of software platforms. Skimming and penetration pricing strategies and asymmetric crossside network effects exist widely on software platforms but have received little attention in the extant literature. Our study fills this gap by employing a twoperiod model to analyze whether software platforms should adopt a penetration or skimming pricing strategy on the developer side when considering asymmetric cross-side network effects. The main findings of this study are as follows.

First, the skimming pricing strategy is the optimal strategy if the intensity of the user-to-developer network effect is weak; the platform should adopt the penetration pricing strategy otherwise. When the platform charges no access fee to users, with a stronger developer-to-user network effect or a longer second period, the platform will be more likely to adopt the penetration pricing strategy. However, the platform will be more willing to adopt the skimming pricing strategy with developers’ higher basic expected revenue. When the platform charges an access fee or provides a subsidy to users, a longer second period first increases and then decreases the willingness of the platform to adopt the penetration pricing strategy. Second, if the platform does not charge users an access fee, the platform should charge developers in the two periods if it adopts the skimming pricing strategy. However, if the platform adopts the penetration pricing strategy, it is better off subsidizing developers in Period 1 if the impacts of users on developers are weak or the impacts are moderate and developers have pessimistic expectations regarding revenue. Third, after endogenizing the platform’s access fee charged to users, the platform should charge users if users impacts on developers are weak. In Period 1, if the user-to-developer network effect is sufficiently weak or strong, the platform should subsidize developers; otherwise, the platform should charge developers. In Period 2, the platform should charge developers if the intensity of the user-to-developer network effect is strong and subsidize them otherwise. Finally, as the user-to-developer network effect becomes stronger, the price charged to developers in Period 1 first increases and then decreases, and the price charged in Period 2 always increases. However, when developers become pessimistic about their potential earnings on the platform, as the developer-to-user network effect becomes stronger, the price in Period 1 will decrease and the price in Period 2 will first decrease and then increase. As the length of Period 2 gets longer, the optimal access fee charged to users will first decrease and then increase.

## 6.3 Managerial Implications and Future Research Directions

Our study provides practical guidelines to support software platforms in making informed pricing decisions. First, our study offers insights on whether a software platform should adopt the skimming or penetration pricing strategy on the developer side. In particular, prior literature shows that network effects induce the platform to adopt a penetration pricing strategy for consumers (Liu, 2010); however, we found that a significant user-to-developer network effect incentivizes the platform to adopt the penetration pricing strategy on the developer side.

Second, software platforms with different revenue structures should adopt different subsidizing/charging pricing strategies. When platforms charge users an access fee, subsidizing access for developers in both the first and second periods is viable. However, when the platform firm only charges developers an access fee, it can subsidize access for developers in one period at the most.

Third, our findings can help software platform firms make sound decisions on how to jointly implement skimming/penetration pricing and subsidy strategies. Currently, some two-sided platforms, such as Uber and Didi, adopt the penetration pricing strategy and subsidize service providers in Period 1 in an attempt to rapidly expand their market size. However, our findings suggest that in Period 1, subsidizing access for developers is not always the optimal strategy for the software platform. Our findings also suggest that when users are charged an access fee or provided with a subsidy, the platform should adopt the skimming pricing strategy and charge developers in Period 1 and subsidize them in Period 2 if the user-to-developer network effect is not strong.

Fourth, software platforms need to evaluate developers’ basic expected revenue gained from joining the platform, the impacts of users on the participation decisions of developers, the impacts of developers on the participation decisions of users, and the length of the pricing cycle. Our findings can help the platform adjust its pricing strategy as these main factors vary. For example, when developers have more optimistic expectations about the revenue they will gain on the platform, the platform should decrease the access fee charged or increase the subsidy offered in Period 1 if the user-to-developer network effect is sufficiently strong, and raise the access fee or reduce the subsidy in Period 2. Although this study assumes that developers are myopic, the two-period model allows developers to update their choices after observing the participation decisions of the other developers and users, indicating that developers are more strategic if they rely less on their subjective expectations. Hence, our findings could help platforms adjust their pricing strategies when developers are strategic—that is, when developers’ basic expected revenue plays an insignificant role in developers’ decisions and the network size dominates.

The present study suggests several directions for future research. First, we focus on monopoly software platforms’ skimming and penetration pricing strategies. A future study could examine two competing software platforms’ pricing strategies on the developer side. Second, this study only investigates whether a platform should adopt a penetration/skimming strategy on the developer side. Investigating it on both the user and developer sides in a duopoly market is also a possible future research direction. Finally, other economic factors, such as developers’ pricing decisions and the openness strategy regarding the platform’s intellectual property, have not been considered in the present study but could be examined in future research.

## 6.4 Acknowledgments

The authors would like to thank the senior editor, Giri Tayi, and the two anonymous reviewers for their insightful comments and suggestions. This work was supported by the National Natural Science Foundation of China (Grant Nos. 71631003, 72022012, 71971153, 71871155, 71701147) and Shandong Industrial Internet Innovation and Entrepreneurship Community.

## References

Adner, R., Chen, J., & Zhu, F. (2020). Frenemies in platform markets: Heterogeneous profit foci as drivers of compatibility decisions. Management Science, 66(6), 2432-2451.

Adrian, M. (2016). DBMS 2015 numbers paint a picture of slow but steady change. Gartner. https://blogs.gartner.com/mervadrian/2016/04/12/dbms-2015-numbers-painta-picture-of-slow-but-steady-change/

Anderson, E. G., Parker, G. G., & Tan, B. (2014). Platform performance investment in the presence of network externalities, Information System Research, 25(1), 152-172.

Argenziano, A. R. (2009). Asymmetric networks in two-sided markets. American Economic Journal: Microeconomics, 1(1), 17-52.

Armstrong, M., & Wright, J. (2007). Two-sided markets, competitive bottlenecks and exclusive contracts. Economic Theory, 32(2), 353-380.

Artyom, D. (2019). App stores list. Business of Apps. http://www.businessofapps.com/guide/appstores-list/.

August, T., Dao, D., & Kim, K. (2019). Market segmentation and software security: Pricing patching rights. Management Science, 65(10), 4451-4949.

Cabral, L. M. B., Salant, D. J., & Woroch, G. A. (1999). Monopoly pricing with network externalities. International Journal of Industrial Organization, 17(2), 199-214.

Caillaud, B., & Jullien, B. (2003). Chicken & egg: Competition among intermediation service providers. Rand Journal of Economics, 34(2), 309-328.

Cenamor, J., & Frishammar, J. (2021). Openness in platform ecosystems: Innovation strategies for complementary products. Research Policy, 50(1), 104-148.

Chu, J., & Manchanda, P. (2016). Quantifying crossnetwork effects in online C2C platforms. Marketing Science 35(6), 870-893.

Constine, J. (2019). Twitter cracks down on API abuse, will charge B2B devs. TechCrunch. http://techcrunch.com/2019/03/19/twitterdeveloper-review/

Csorba, G., & Hahn, J. H. (2006). Functional degradation and asymmetric network effects. The Journal of Industrial Economics, 54(2), 253-268.

Daxx T. (2020). How many software developers are in the US and the world in 2019? http://www.daxx.com/blog/developmenttrends/number-software-developers-world.

Dean, J. (1976). Pricing policies for new products. Harvard Business Review, 54(6), 141-153

Dou, Y., & Wu, D. J. (2019). Platform competition under network effects: Piggybacking and optimal subsidization. Information Systems Research, 32(3), 820-835.

Du, P., Chen, Q. (2017). Skimming or penetration: Optimal pricing of new fashion products in the presence of strategic consumers. Annals of Operations Research, 257, 275-295.

Eisenmann, T. R., Parker, G., & Van Alstyne, M. W. (2006). Strategies for two sided markets. Harvard Business Review, 10, 92-101.

Evans, D. S. (2011). Platform economics: Essays on multi-sided businesses. Competition Policy International.

Fang, Z., Huang, L., & Wierman, A. (2017). Prices and Subsidies in the sharing economy. Proceedings of the 26<sup>th</sup> International Conference on World Wide Web (pp. 53-62).

Feng, H., Jiang, Z., & Liu, D. (2018). Quality, pricing, and release time: Optimal market entry strategy for new software-as-a-service vendors. MIS Quarterly, 42(1), 333-353.

Feng, H., Jiang, Z., Li, M., & Feng, N. (2020). First-or second-mover advantage? The case of ITenabled platform market. MIS Quarterly, 44(3) 1107-1141.

Feng, J., Li, X., Zhang, X. (2019). Online product reviews-triggered dynamic pricing: Theory and evidence. Information Systems Research, 30(4), 1107-1123.

Galyonkin, S. (2018). Steam in 2017. Steam Spy. https://galyonk.in/steam-in-2017- 129c0e6be260.

Galyonkin, S. (2017). Steam Sales in 2016. Steam Spy. https://galyonk.in/steam-sales-in-2016- def2a8ab15f2.

Gao, M. (2018). Platform pricing in mixed two-sided markets. International Economic Review 3(59), 1103-1129.

Hagiu, A. (2006). Pricing and commitment by twosided platforms. Rand Journal of Economics, 37(3), 720-737.

Hagiu, A., & Spulber, D. (2013). First-party content and coordination in two-sided markets. Management Science, 59(4), 933-949.

Hoernig, S. (2007). On-net and off-net pricing on asymmetric telecommunications networks. Information Economics and Policy, 19(2), 171- 188.

Hu, B., Hu, M., & Zhu, H. (2021). Surge pricing and two-sided temporal responses in ride hailing. Manufacturing & Service Operations Management, 24(1), 91-109.

Jain, D. C., Muller, E., & Vilcassim, N. J. (1999). Pricing patterns of cellular phones and phonecalls: A segment-level analysis, Management Science, 45(2), 131-141.

Li, Hui. (2019). Intertemporal price discrimination with complementary products: E-books and ereaders. Management Science, 65(6), 2665- 2694..

Liu, H. (2010). Dynamics of pricing in the video game console market: skimming or penetration? Journal of Marketing Research, 47(3), 428- 443.

Liu, Y., Cheng, H. K., Tang, Q. C., & Eryarsoy, E. (2011). Optimal software pricing in the presence of piracy and word-of-mouth effect. Decision Support Systems, 51(1), 99-107.

Kalish, S. (1983). Monopolist pricing with dynamic demand and production cost. Marketing Science, 2(2), 135-159.

Kotler, P., & Armstrong, G. (2017), Principles of marketing (17th ed.). Pearson.

Krishnan, T., Frank, V., Bass, M, and Jain, DC. (1999). Optimal pricing strategy for new products. Management Science, 45(12), 1650-1663.

Martin, S., Marc, F., & Gerard, J. (2015). Skimming or penetration? Strategic dynamic pricing for new products. Marketing Science, 34(2), 235-249.

Matulef Jeffrey. (2017). Steam Greenlight to be replaced with Steam Direct next week. Eurogamer. https://www.eurogamer.net/articles/2017-06- 06-steam-greenlight-to-be-replaced-withsteam-direct-next-week.

Nelson R. (2019). Global app revenue reached \$39 billion in the first half of 2019, up 15% yearover-year. Sensor Tower. https://sensortower.com/blog/app-revenueand-downloads-1h-2019.

Parker, G. G., & Van Alstyne, M. (2005). Two-sided network effects: a theory of information product design, Management Science, 51(10), 1494-1504.

Parker, G. G., & Van Alstyne, M. (2018). Innovation, openness, and platform control. Management Science, 64(7), 3015-3032.

Parker, G. G., Van Alstyne, M., & Jiang, X. (2017). Platform ecosystems: How developers invert the firm. MIS Quarterly, 41(1), 255-266.

Rasch, A., & Wenzel, T. (2013). Piracy in a two-sided software market. Journal of Economic Behavior & Organization, 88, 78-89.

Rochet, J. C., & Tirole, J. (2003). Platform competition in two-sided markets. Journal of the European Economic Association, 1(4), 990-1029.

Roma, P., Zambuto, F., Perrone, G. (2016). The role of the distribution platform in price formation of paid apps. Decision Support Systems, 91, 13-24.

Ren, S., & Schaar, M. (2014). Smart data pricing. In S. Sen, C. Joe-Wong, S. Ha, M. Chiang (Eds.), To tax or to subsidize: The economics of usergenerated content platforms. Wiley.

Rysman, M. (2009). The economics of two-sided markets. Journal of Economic Perspectives, 23(3), 125-143

Saito, R., & Matsubayashi, N. (2017). Sequential product positioning in the presence of an asymmetric network externality intensity. Managerial and Decision Economics, 3(39), 320-334.

Schenker, J. L. (2019). The platform economy. The Innovator. https://innovator.news/the-platformeconomy-3c09439b56.

Song, P., Xue, L., Rai, A., & Zhang, A. C. (2018). The ecosystem of software platform: A study of asymmetric cross-side network effects and platform governance. MIS Quarterly, 42(1), 121-142

Sriram, S., Manchanda, P., Bravo, M. E., Chu, J., Ma, L., Song, M., Shriver, S., & Subramanian, U. (2015). Platforms: A multiplicity of research opportunities. Marketing Letter, 26(2), 141- 152.

Su, X. (2007). Intertemporal pricing with strategic customer behavior. Management Science, 53(5), 726-741.

Sun, L., Teunter, R. H., Babai, M.Z., & Hua, G. (2019). Optimal pricing for ride-sourcing platforms. European Journal of Operational Research, 278(3), 783-795.

Sur, M., Lee, D. & Kim, K. (2019). Optimal revenue sharing in platform markets: A Stackelberg model. Journal of Revenue Pricing Management, 18, 317-331.

Tiwana, A., Konsynski, B., & Bush, A. A. (2010). Platform evolution: Coevolution of platform architecture, governance, and environmental dynamics. Information Systems Research, 21(4), 675-687.

Tracy, M. (2019). Looking to stay relevant, big enterprises embrace the platform. MIT Management Sloan School. https://mitsloan. mit.edu/ideas-made-to-matter/looking-to-stayrelevant-big-enterprises-embrace-platform

Wilbur, K. C. (2008). A two-sided, empirical model of television advertising and viewing markets. Marketing Science, 27(3), 356-378.

Winter, S., & Sundqvist, S. (2010). New product pricing strategies for network effects products: Free products? International Journal of Technology Marketing, 5(3), 250

Zhang, X., & Yue, W.T. (2020). Integration of onpremises and cloud-based software: The product bundling perspective. Journal of the Association for Information Systems, 21(6), 1507-1551.

Zimmermann, S., Angerer, P., Provin, D., & Nault, B. R. (2018). Pricing in C2C sharing platforms. Journal of the Association for Information Systems, 19(8), 672-688.

## Appendix A: Proofs

## Optimal Solutions for the Optimization Problem (Equation 8)

(1) Case 1: $\pmb { f } = \pmb { 0 }$

In this case, the optimum $p _ { \mathrm { d 1 } }$ and $p _ { \mathrm { d } 2 }$ satisfy the following first-order conditions:

$$
\frac {\partial \pi}{\partial p _ {d 1}} (p _ {d 1} ^ {*}, p _ {d 2} ^ {*}) = \frac {\partial \pi}{\partial p _ {d 2}} (p _ {d 1} ^ {*}, p _ {d 2} ^ {*}) = 0.
$$

To ensure optimality, the following second-order conditions must hold:

$$
\frac {\partial^ {2} \pi}{\partial p _ {d 1} ^ {2}} = - \frac {2}{c} <   0.
$$

$$
D e t (H e s s i a n) = \frac {\partial^ {2} \pi}{\partial p _ {d 1} ^ {2}} \frac {\partial^ {2} \pi}{\partial p _ {d 2} ^ {2}} - \left(\frac {\partial \pi}{\partial p _ {d 1} \partial p _ {d 2}}\right) ^ {2} = \frac {(3 C - \alpha \beta) (C + \alpha \beta)}{C ^ {4}} > 0,
$$

which requires $\alpha < \frac { 3 C } { \beta } .$ Thus, all our analyses are conducted under the condition of $\alpha < \frac { 3 C } { \beta } .$

$N _ { D 1 } ^ { * } , N _ { D 2 } ^ { * } , N _ { A 1 } ^ { * } , N _ { A 2 } ^ { * } > 0$ requires $\begin{array} { r } { R > \frac { 2 \alpha \left( C - \alpha \beta \right) } { C \left( 3 - \tau \right) + \alpha \beta \left( 1 + \tau \right) } . } \end{array}$

The total profit of the platform is

$$
\pi^ {*} = \frac {2 R \alpha \beta (R + 2 \alpha + R \tau) + C (4 \alpha^ {2} + 4 R \alpha \tau + R ^ {2} (3 + \tau^ {2}))}{4 (3 C - \alpha \beta) (C + \alpha \beta)},
$$

the profit gained in Period 1 is

$$
\pi_ {1} ^ {*} = \frac {\left(2 C \alpha + C R (\tau - 3) - \alpha \beta (R + 2 \alpha + R \tau)\right) \left(2 R \alpha^ {2} \beta^ {2} + C \alpha \beta (2 \alpha + R (- 3 + \tau)) - C ^ {2} (2 \alpha + R (3 + \tau))\right)}{4 (3 C - \alpha \beta) ^ {2} (C + \alpha \beta) ^ {2}},
$$

and the profit gained in Period 2 is

$$
\pi_ {2} ^ {*} = \frac {C (2 C \alpha + R \alpha \beta + C R \tau) ^ {2}}{(3 C - \alpha \beta) ^ {2} (C + \alpha \beta) ^ {2}}.
$$

(2) Case 2: $\pm \mathbf { 0 }$

In this case, the optimum $p _ { \mathrm { d } 1 } , p _ { \mathrm { d } 2 } , f$ should satisfy the following conditions:

$$
\frac {\partial^ {2} \pi}{\partial p _ {d 1} ^ {2}} = - \frac {2}{c} <   0.
$$

$$
D e t (H e s s i a n) = \frac {\partial^ {2} \pi}{\partial p _ {d 1} ^ {2}} \frac {\partial^ {2} \pi}{\partial p _ {d 2} ^ {2}} - \left(\frac {\partial \pi}{\partial p _ {d 1} \partial p _ {d 2}}\right) ^ {2} = \frac {(3 C - \alpha \beta) (C + \alpha \beta)}{C ^ {4}} > 0.
$$

$$
d e t \left( \begin{array}{c c c} \frac {\partial^ {2} \pi}{\partial p _ {d 1} ^ {2}} & \frac {\partial^ {2} \pi}{\partial p _ {d 1} \partial p _ {d 2}} \frac {\partial^ {2} \pi}{\partial p _ {d 1} \partial f} \\ \frac {\partial^ {2} \pi}{\partial p _ {d 2} \partial p _ {d 1}} & \frac {\partial^ {2} \pi}{\partial p _ {d 2} ^ {2}} & \frac {\partial^ {2} \pi}{\partial p _ {d 2} \partial f} \\ \frac {\partial^ {2} \pi}{\partial f \partial p _ {d 1}} & \frac {\partial^ {2} \pi}{\partial f \partial p _ {d 2}} & \frac {\partial^ {2} \pi}{\partial f ^ {2}} \end{array} \right) = \frac {- 1 2 C ^ {2} + 2 \alpha \beta^ {3} (1 + \tau) + C (4 \alpha^ {2} - 4 \alpha \beta (2 + \tau) + \beta^ {2} (3 + \tau^ {2}))}{2 C ^ {4}} <   0.
$$

We assume there are developers and users on the platform, and, thus, our analysis is conducted under the following conditions: $N _ { D 1 } ^ { * } , N _ { D 2 } ^ { * } , N _ { A 1 } ^ { * } , N _ { A 2 } ^ { * } > 0$

The total profit of the platform is:

$$
\pi^ {*} = \frac {3 C ^ {2} + C (3 R ^ {2} + 3 R \beta + 2 \alpha \beta + 2 \alpha (R + \beta) \tau + R (R + \beta) \tau^ {2}) + R \alpha (2 R \beta (1 + \tau) - R \alpha + 2 \beta^ {2} (1 + \tau))}{1 2 C ^ {2} - 2 \alpha \beta^ {3} (1 + \tau) - C (4 \alpha^ {2} - 4 \alpha \beta (2 + \tau) + \beta^ {2} (3 + \tau^ {2}))}.
$$

## Proof of Proposition 1

From the optimal solutions, we have $\begin{array} { r } { p _ { d 2 } ^ { * } - p _ { d 1 } ^ { * } = \frac { 2 C \alpha + 2 R \alpha \beta + C R ( \tau - 3 ) } { 6 C - 2 \alpha \beta } } \end{array}$ . Thus, if $\begin{array} { r } { \alpha > \frac { ( 3 - \tau ) C R } { 2 ( C + R \beta ) } , p _ { d 2 } ^ { * } - p _ { d 1 } ^ { * } > 0 , } \end{array}$ ; otherwise, if $\begin{array} { r } { 0 < \alpha < \frac { ( 3 - \tau ) C R } { 2 ( C + R \beta ) } , p _ { d 2 } ^ { * } - p _ { d 1 } ^ { * } < 0 . } \end{array}$

## Proof of Proposition 2

Let ?? denotes the threshold distinguishing the two strategies: $\begin{array} { r } { y = \frac { ( 3 - \tau ) C R } { 2 ( C + R \beta ) } . } \end{array}$ . The first-order derivatives of ?? with respect to ??, ??, and ?? are as follows:

$$
\frac {\partial y}{\partial \beta} = \frac {C R ^ {2} (- 3 + \tau)}{2 (C + R \beta) ^ {2}} <   0, \frac {\partial y}{\partial \tau} = - \frac {C R}{2 C + 2 R \beta} <   0, \frac {\partial y}{\partial R} = \frac {C ^ {2} (3 - \tau)}{2 (C + R \beta) ^ {2}} > 0.
$$

## Proof of Proposition 3

Under the precondition $\begin{array} { r } { \alpha < \frac { 3 C } { \beta } , } \end{array}$ we have $\begin{array} { r } { p _ { d 2 } ^ { * } = \frac { C ( 2 C \alpha + R \alpha \beta + C R \tau ) } { ( 3 C - \alpha \beta ) ( C + \alpha \beta ) } > 0 } \end{array}$ . When the platform adopts the skimming pricing strategy, that is $p _ { d 1 } ^ { * } > p _ { d 2 } ^ { * }$ , it should charge developers in Period 1 as well.

If the platform adopts the penetration pricing strategy,

(1) when $0 < \alpha \leq C / \beta$ , we have $p _ { d 1 } ^ { * } > 0 ;$

(2) when $\begin{array} { r } { C / \beta < \alpha < \frac { C \left( 3 - \tau + \sqrt { 3 3 + \tau ( 2 + \tau ) } \right) } { 4 \beta } } \end{array}$ , if $\begin{array} { r } { 0 < R \leq \frac { 2 C \alpha ( \alpha \beta - C ) } { 4 C ^ { 2 } + ( 2 \alpha \beta - C ( \tau - 1 ) ) ( C - \alpha \beta ) } , } \end{array}$ we have $p _ { d 1 } ^ { * } < 0 ;$ otherwise, if $R >$ $\frac { 2 C \alpha ( \alpha \beta - C ) } { 4 C ^ { 2 } + ( 2 \alpha \beta - C ( \tau - 1 ) ) ( C - \alpha \beta ) } ,$ , we have $p _ { d 1 } ^ { * } > 0 ;$ ;

(3) $\begin{array} { r } { \mathrm { w h e n } \frac { C \left( 3 - \tau + \sqrt { 3 3 + \tau ( 2 + \tau ) } \right) } { 4 \beta } \leq \alpha < 3 C / \beta } \end{array}$ , we have $p _ { d 1 } ^ { * } < 0$

## Proof of Lemma 1

(1) The first-order derivative of the optimal price in Period 1 with respect to ?? is $\begin{array} { r } { \frac { \partial { p } _ { d 1 } ^ { * } } { \partial { R } } = \frac { C \alpha \beta ( 3 - \tau ) + C ^ { 2 } ( 3 + \tau ) - 2 \alpha ^ { 2 } \beta ^ { 2 } } { 2 ( 3 C - \alpha \beta ) ( C + \alpha \beta ) } } \end{array}$ . We obtain that if $\begin{array} { r } { 0 < \alpha < \frac { \mathbf { C } \left( 3 - \tau + \sqrt { 3 3 + \tau ( 2 + \tau ) } \right) } { 4 \beta } , \frac { \partial p _ { d 1 } ^ { * } } { \partial R } > 0 ; \mathrm { i f } \frac { \mathbf { C } \left( 3 - \tau + \sqrt { 3 3 + \tau ( 2 + \tau ) } \right) } { 4 \beta } \leq \alpha < \frac { 3 C } { \beta } , \frac { \partial p _ { d 1 } ^ { * } } { \partial R } \leq 0 . } \end{array}$

(2) The first-order derivative of the optimal price in Period 2 with respect to ?? is $\begin{array} { r } { \frac { \partial p _ { d 2 } ^ { * } } { \partial R } = \frac { C ( \alpha \beta + C \tau ) } { ( 3 C - \alpha \beta ) ( C + \alpha \beta ) } , } \end{array}$ , which is positive.

(3) The first-order derivative of the platform’s total profit with respect to $\begin{array} { r } { R \mathrm { ~ i s ~ } \frac { \partial \pi ^ { * } } { \partial R } = \frac { 2 C \alpha \tau + 2 \alpha \beta ( R + \alpha + R \tau ) + C R ( 3 + \tau ^ { 2 } ) } { ( 3 C - \alpha \beta ) ( C + \alpha \beta ) } , } \end{array}$ , which is positive.

(4) The first-order derivative of the number of developers and users in two periods with respect to ?? are as follows, all of which are positive:

$$
\frac {\partial N _ {D 1} ^ {*}}{\partial R} = \frac {C (3 - \tau) + \alpha \beta (1 + \tau)}{2 (3 C - \alpha \beta) (C + \alpha \beta)}, \frac {\partial N _ {D 2} ^ {*}}{\partial R} = \frac {\alpha \beta + C \tau}{(3 C - \alpha \beta) (C + \alpha \beta)}, \frac {\partial N _ {A 1} ^ {*}}{\partial R} = \frac {\beta (C (3 - \tau) + \alpha \beta (1 + \tau))}{2 (3 C - \alpha \beta) (C + \alpha \beta)}, \frac {\partial N _ {A 2} ^ {*}}{\partial R} = \frac {\beta (3 + \tau)}{6 C - 2 \alpha \beta}.
$$

## Proof of Lemma 2

(1) The first-order derivative of the optimal price in Period 1 with respect to ?? i $\begin{array} { r } { \mathrm { ~ ; ~ } \frac { \partial p _ { d 1 } ^ { * } } { \partial \tau } = \frac { C R ( C - \alpha \beta ) } { 2 ( 3 C - \alpha \beta ) ( C + \alpha \beta ) } , } \end{array}$ , we obtain that if $\begin{array} { r } { 0 < \alpha < \frac { C } { \beta } , \frac { \partial p _ { d 1 } ^ { * } } { \partial \tau } > 0 ; \mathrm { i f } \frac { C } { \beta } \leq \alpha < \frac { 3 C } { \beta } , \frac { \partial p _ { d 1 } ^ { * } } { \partial \tau } \leq 0 . } \end{array}$

(2) The first-order derivative of the optimal price in Period 2 with respect to $\begin{array} { r } { \tau \mathrm { ~ i s } \frac { \partial p _ { d 2 } ^ { * } } { \partial \tau } = \frac { C ^ { 2 } R } { ( 3 C - \alpha \beta ) ( C + \alpha \beta ) } , } \end{array}$ , which is positive.

(3) The first-order derivative of the platform’s total profit with respect to ?? is $\begin{array} { r } { \frac { \partial \pi ^ { * } } { \partial \tau } = \frac { R \left( \alpha ( 2 C + R \beta ) + R \tau C \right) } { 2 ( 3 C - \alpha \beta ) ( C + \alpha \beta ) } . } \end{array}$ , which is positive.

(4) The first-order derivative of the number of developers and users in Period 1 with respect to ?? are $\begin{array} { r } { \frac { \partial N _ { D 1 } ^ { * } } { \partial \tau } = } \end{array}$ $\begin{array} { r } { \frac { R \alpha \beta - R C } { 2 ( 3 C - \alpha \beta ) ( C + \alpha \beta ) } , \frac { \partial N _ { A 1 } ^ { * } } { \partial \tau } = \frac { R \beta ( - C + \alpha \beta ) } { 2 ( 3 C - \alpha \beta ) ( C + \alpha \beta ) } , } \end{array}$ , respectively. We obtain that if $\begin{array} { r } { 0 < \alpha < \frac { C } { \beta } , \frac { \partial N _ { D 1 } ^ { * } } { \partial \tau } < 0 , \frac { \partial N _ { A 1 } ^ { * } } { \partial \tau } < 0 ; \mathrm { i f } \frac { C } { \beta } \le \alpha < } \end{array}$ $\begin{array} { r } { \frac { 3 C } { \beta } , \frac { \partial N _ { D 1 } ^ { * } } { \partial \tau } \geq 0 , \frac { \partial N _ { A 1 } ^ { * } } { \partial \tau } \geq 0 . } \end{array}$

(5) The first-order derivative of the number of developers and users in Period 2 with respect to ?? are $\begin{array} { r } { \frac { \partial N _ { D 2 } ^ { * } } { \partial \tau } = } \end{array}$ $\begin{array} { r } { \frac { C R } { ( 3 C - \alpha \beta ) ( C + \alpha \beta ) } \operatorname { a n d } \frac { \partial N _ { A 2 } ^ { * } } { \partial \tau } = \frac { R \beta } { 6 C - 2 \alpha \beta } , } \end{array}$ both of which are positive.

## Proof of Lemma 3

(1) The first-order derivative of the optimal price in Period 1 with respect to ?? is $\begin{array} { r } { \frac { \partial p _ { d 1 } ^ { * } } { \partial \alpha } = } \end{array}$ $\displaystyle \frac { C ( 2 C + R \beta ) ( 3 C ^ { 2 } - 6 C \alpha \beta - \alpha ^ { 2 } \beta ^ { 2 } ) - C R \beta ( 5 C ^ { 2 } - 2 C \alpha \beta + \alpha ^ { 2 } \beta ^ { 2 } ) \tau } { 2 ( 3 C - \alpha \beta ) ^ { 2 } ( C + \alpha \beta ) ^ { 2 } } .$ . Then we find that:

$$
\left\{ \begin{array}{l} \frac {\partial p _ {d 1} ^ {*}}{\partial \alpha} \geq 0, \text {if} 0 <   \alpha \leq \frac {C \beta (R \beta (\tau - 3) - 6 C) + 2 \sqrt {C ^ {2} \beta^ {2} (2 C + R \beta (1 - \tau)) (6 C + R \beta (3 + \tau))}}{\beta^ {2} (2 C + R \beta (1 + \tau))}, \\ \frac {\partial p _ {d 1} ^ {*}}{\partial \alpha} <   0, \text {if} \alpha > \frac {C \beta (R \beta (\tau - 3) - 6 C) + 2 \sqrt {C ^ {2} \beta^ {2} (2 C + R \beta (1 - \tau)) (6 C + R \beta (3 + \tau))}}{\beta^ {2} (2 C + R \beta (1 + \tau))}. \end{array} \right.
$$

(2) The first-order derivative of the optimal price in Period 2 with respect to ?? $\mathrm { i s } \frac { \partial p _ { d 2 } ^ { * } } { \partial \alpha } =$ $\frac { C \Big ( ( 2 C + R \beta ) \big ( 3 C ^ { 2 } + \alpha ^ { 2 } \beta ^ { 2 } \big ) + 2 C R \beta ( \alpha \beta - C ) \tau \Big ) } { 2 ( 3 C - \alpha \beta ) ^ { 2 } ( C + \alpha \beta ) ^ { 2 } } ,$ , which is positive.

(3) The first-order derivative of the platform’s total profit with respect to ?? is $\begin{array} { r } { \frac { \partial \pi ^ { * } } { \partial \alpha } = } \end{array}$ (2????+??????+?? $\begin{array} { r l } & { \frac { 8 \tau ) ( ( 2 C + R \beta ) ( 3 C + \alpha \beta ) + R \beta ( \alpha \beta - C ) \tau ) } { 2 ( 3 C - \alpha \beta ) ^ { 2 } ( C + \alpha \beta ) ^ { 2 } } } \end{array}$ , which is positive.

(4) The first-order derivative of the platform’s total profit in Period 1 with respect to ?? is $\frac { \partial \pi _ { 1 } ^ { * } } { \partial \alpha } =$ $\displaystyle \frac { ( \alpha \beta - C ) ( \alpha ( 2 C + R \beta ) + R C \tau ) \big ( 2 C \alpha \beta ^ { 2 } \big ( \alpha + R ( 3 - \tau ) \big ) + R \alpha ^ { 2 } \beta ^ { 3 } ( 1 + \tau ) + C ^ { 2 } \beta \big ( 1 2 \alpha + R ( 5 \tau - 3 ) \big ) - 6 C ^ { 3 } \big ) } { 2 ( \alpha \beta - 3 C ) ^ { 3 } ( C + \alpha \beta ) ^ { 3 } } ,$ , we have

$$
\left\{ \begin{array}{l} \frac {\partial \pi_ {1} ^ {*}}{\partial \alpha} \leq 0, \text {if} 0 <   \alpha \leq \frac {C \beta (R \beta (\tau - 3) - 6 C) + 2 \sqrt {C ^ {2} \beta^ {2} (2 C + R \beta (1 - \tau)) (6 C + R \beta (3 + \tau))}}{\beta^ {2} (2 C + R \beta (1 + \tau))}, \\ \frac {\partial \pi_ {1} ^ {*}}{\partial \alpha} > 0, \text {if} \frac {C \beta (R \beta (\tau - 3) - 6 C) + 2 \sqrt {C ^ {2} \beta^ {2} (2 C + R \beta (1 - \tau)) (6 C + R \beta (3 + \tau))}}{\beta^ {2} (2 C + R \beta (1 + \tau))} <   \alpha <   \frac {C}{\beta}, \\ \frac {\partial \pi_ {1} ^ {*}}{\partial \alpha} \leq 0, \text {if} \frac {C}{\beta} \leq \alpha <   \frac {3 C}{\beta}. \end{array} \right.
$$

(5) The first-order derivative of the platform’s total profit in Period 2 with respect to ?? is $\begin{array} { r } { \frac { \partial \pi _ { 2 } ^ { * } } { \partial \alpha } = } \end{array}$ $\frac { 2 C ( \alpha ( 2 C + R \beta ) + R \tau C ) ( ( 2 C + R \beta ) ( 3 C ^ { 2 } + \alpha ^ { 2 } \beta ^ { 2 } ) + 2 C R \beta ( \alpha \beta - C ) \tau ) } { ( 3 C - \alpha \beta ) ^ { 3 } ( C + \alpha \beta ) ^ { 3 } }$ , which is positive.

(6) The first-order derivative of the number of developers in Period 1 with respect to ?? is $\begin{array} { r } { \frac { \partial N _ { D 1 } ^ { * } } { \partial \alpha } = } \end{array}$ $\displaystyle \frac { 2 C \alpha \beta ^ { 2 } ( \alpha + R ( 3 - \tau ) ) - 6 C ^ { 3 } + R \alpha ^ { 2 } \beta ^ { 3 } ( 1 + \tau ) + C ^ { 2 } \beta ( 1 2 \alpha + R ( 5 \tau - 3 ) + \beta \gamma ) } { 2 ( 3 C - \alpha \beta ) ^ { 2 } ( C + \alpha \beta ) ^ { 2 } } \beta ,$ , we find that:

$$
\left\{ \begin{array}{l} \frac {\partial N _ {D 1} ^ {*}}{\partial \alpha} \leq 0, \text {if} 0 <   \alpha \leq \frac {C \beta (R \beta (\tau - 3) - 6 C) + 2 \sqrt {C ^ {2} \beta^ {2} (2 C + R \beta (1 - \tau)) (6 C + R \beta (3 + \tau))}}{\beta^ {2} (2 C + R \beta (1 + \tau))}, \\ \frac {\partial N _ {D 1} ^ {*}}{\partial \alpha} > 0, \text {if} \alpha > \frac {C \beta (R \beta (\tau - 3) - 6 C) + 2 \sqrt {C ^ {2} \beta^ {2} (2 C + R \beta (1 - \tau)) (6 C + R \beta (3 + \tau))}}{\beta^ {2} (2 C + R \beta (1 + \tau))}. \end{array} \right.
$$

(7) The first-order derivative of the number of users in Period 1 with respect to ?? is $\begin{array} { r } { \frac { \partial N _ { A 1 } ^ { * } } { \partial \alpha } = } \end{array}$ $\frac { \beta ( ( 2 C + R \beta ) ( \alpha \beta ( 6 C + \alpha \beta ) - 3 C ^ { 2 } ) + R \beta ( 5 C ^ { 2 } + \alpha \beta ( - 2 C + \alpha \beta ) ) \tau ) } { 2 ( 3 C - \alpha \beta ) ^ { 2 } ( C + \alpha \beta ) ^ { 2 } }$ . Then, we have:

$$
\left\{ \begin{array}{l} \frac {\partial N _ {A 1} ^ {*}}{\partial \alpha} \leq 0, \text {if} 0 <   \alpha \leq \frac {C \beta (R \beta (\tau - 3) - 6 C) + 2 \sqrt {C ^ {2} \beta^ {2} (2 C + R \beta (1 - \tau)) (6 C + R \beta (3 + \tau))}}{\beta^ {2} (2 C + R \beta (1 + \tau))}, \\ \frac {\partial N _ {A 1} ^ {*}}{\partial \alpha} > 0, \text {if} \alpha > \frac {C \beta (R \beta (\tau - 3) - 6 C) + 2 \sqrt {C ^ {2} \beta^ {2} (2 C + R \beta (1 - \tau)) (6 C + R \beta (3 + \tau))}}{\beta^ {2} (2 C + R \beta (1 + \tau))}. \end{array} \right.
$$

(8) The first-order derivative of the number of developers and users in Period 2 with respect to ?? are as follows, both of which are positive:

$$
\frac {\partial N _ {D 2} ^ {*}}{\partial \alpha} = \frac {(2 + R \beta) (3 C ^ {2} + \alpha^ {2} \beta^ {2}) - 2 C R \beta (C - \alpha \beta) \tau}{(3 C - \alpha \beta) ^ {2} (C + \alpha \beta) ^ {2}}, \frac {\partial N _ {A 2} ^ {*}}{\partial \alpha} = \frac {\beta (6 C + R \beta (3 + \tau))}{2 (\alpha \beta - 3 C) ^ {2}}.
$$

## Proof of Lemma 4

(1) The first-order derivative of the optimal price in Period 1 with respect to $\beta$ is:

$$
\frac {\partial p _ {d 1} ^ {*}}{\partial \beta} = - \frac {C \alpha (- 2 C \alpha \beta (2 \alpha + R (- 3 + \tau)) + \alpha^ {2} \beta^ {2} (R + 2 \alpha + R \tau) + C ^ {2} (1 0 \alpha + R (- 3 + 5 \tau)))}{2 (3 C - \alpha \beta) ^ {2} (C + \alpha \beta) ^ {2}}.
$$

Then, if $\begin{array} { r } { R \leq \frac { 2 \alpha } { 1 - \tau } . } \end{array}$ , we have $\begin{array} { r } { \frac { \partial p _ { d 1 } ^ { * } } { \partial \beta } \leq 0 ; } \end{array}$ ; if $\begin{array} { r } { R > \frac { 2 \alpha } { 1 - \tau } , } \end{array}$ , when $\begin{array} { r } { \beta < \frac { R C \alpha ( \tau - 3 ) + 2 \left( C \alpha ^ { 2 } + \sqrt { C ^ { 2 } \alpha ^ { 2 } \left( R - 2 \alpha - R \tau \right) \left( 3 R + 2 \alpha + R \tau \right) } \right) } { \alpha ^ { 2 } \left( R + 2 \alpha + R \tau \right) } } \end{array}$ , we have $\frac { \partial p _ { d 1 } ^ { * } } { \partial \beta } > 0$ , and when $\begin{array} { r } { \beta > \frac { R C \alpha ( \tau - 3 ) + 2 \left( C \alpha ^ { 2 } + \sqrt { C ^ { 2 } \alpha ^ { 2 } \left( R - 2 \alpha - R \tau \right) \left( 3 R + 2 \alpha + R \tau \right) } \right) } { \alpha ^ { 2 } \left( R + 2 \alpha + R \tau \right) } , } \end{array}$ , we have $\frac { \partial p _ { d 1 } ^ { * } } { \partial \beta } < 0$

(2) The first-order derivative of the optimal price in Period 2 with respect to $\beta$ is:

$$
\frac {\partial p _ {d 2} ^ {*}}{\partial \beta} = \frac {C \alpha (R \alpha^ {2} \beta^ {2} + 2 C \alpha \beta (2 \alpha + R \tau) - C ^ {2} (4 \alpha + R (2 \tau - 3)))}{(3 C - \alpha \beta) ^ {2} (C + \alpha \beta) ^ {2}}.
$$

Then, if $\begin{array} { r } { R \leq \frac { 2 \alpha } { 1 - \tau } , } \end{array}$ when $\begin{array} { r } { \beta \leq \frac { \sqrt { C ^ { 2 } \alpha ^ { 2 } ( 2 \alpha + R ( \tau - 1 ) ) ( 2 \alpha + R ( 3 + \tau ) ) } - C \alpha ( 2 \alpha + R \tau ) } { R \alpha ^ { 2 } } } \end{array}$ , we have $\frac { \partial p _ { d 2 } ^ { * } } { \partial \beta } \leq 0$ , and when $\beta >$ $\frac { \sqrt { C ^ { 2 } \alpha ^ { 2 } ( 2 \alpha + R ( \tau - 1 ) ) ( 2 \alpha + R ( 3 + \tau ) ) } - C \alpha ( 2 \alpha + R \tau ) } { R \alpha ^ { 2 } } ,$ , we have $\begin{array} { r } { \frac { \partial p _ { d 2 } ^ { * } } { \partial \beta } > 0 ; \mathrm { i f } R > \frac { 2 \alpha } { 1 - \tau } , } \end{array}$ we have $\frac { \partial p _ { d 2 } ^ { * } } { \partial \beta } > 0$

(3) The first-order derivative of the platform’s total profit with respect to $\begin{array} { r } { \beta \mathrm { i s } \frac { \partial \pi ^ { * } } { \partial \beta } = } \end{array}$ $\frac { \alpha ( \alpha ( 2 { \cal C } + R \beta ) + { \cal C } R \tau ) \Big ( 2 \alpha ( \alpha \beta - { \cal C } ) + R \big ( 3 - \tau + \alpha \beta ( 1 + \tau ) \big ) \Big ) } { ( 3 { \cal C } - \alpha \beta ) ^ { 2 } ( { \cal C } + \alpha \beta ) ^ { 2 } }$ . The boundary $\begin{array} { r } { R > \frac { 2 \alpha \left( C - \alpha \beta \right) } { 3 - \tau + \alpha \beta \left( 1 + \tau \right) } } \end{array}$ implies that $2 \alpha ( \alpha \beta - C ) +$ $R { \bigl ( } 3 - \tau + \alpha \beta ( 1 + \tau ) { \bigr ) } > 0$ . Thus, $\frac { \partial \pi ^ { * } } { \partial \beta } > 0$

(4) The first-order derivative of the number of developers in Period 1 with respect to $\begin{array} { r } { \beta \mathrm { ~ i s } \frac { \partial N _ { D 1 } ^ { * } } { \partial \beta } = } \end{array}$ $\frac { \alpha \Big ( \alpha ^ { 2 } \beta ^ { 2 } ( R + 2 \alpha + R \tau ) + C ^ { 2 } \big ( 1 0 \alpha + R ( 5 \tau - 3 ) \big ) - 2 C \alpha \beta \big ( 2 \alpha + R ( \tau - 3 ) \big ) \Big ) } { ( 3 C - \alpha \beta ) ^ { 2 } ( C + \alpha \beta ) ^ { 2 } }$ . We find that if $\begin{array} { r } { R \leq \frac { 2 \alpha } { 1 - \tau } ; } \end{array}$ we have $\begin{array} { r } { \frac { \partial N _ { D 1 } ^ { * } } { \partial \beta } \geq 0 ; } \end{array}$ if $\begin{array} { r } { R > \frac { 2 \alpha } { 1 - \tau } , } \end{array}$ , when $\begin{array} { r }  \beta < \frac { R C \alpha ( \tau - 3 ) + 2 \left( C \alpha ^ { 2 } + \sqrt { C ^ { 2 } \alpha ^ { 2 } \left( R - 2 \alpha - R \tau \right) \left( 3 R + 2 \alpha + R \tau \right) } \right) } { \alpha ^ { 2 } \ell \mathbf { \} \cdot \mathbf { \sigma } \cdot \mathbf { \sigma } \cdot \mathbf { \sigma } \cdot \mathbf { \sigma } \mathbf { \sigma } \cdot \mathbf { \sigma } } , } \end{array}$ , we have $\begin{array} { r } { \frac { \partial N _ { D 1 } ^ { * } } { \partial \beta } < 0 } \end{array}$ , and when $\beta >$ ?? (??+2??+????) $\frac { R C \alpha ( \tau - 3 ) + 2 { \left( C \alpha ^ { 2 } + \sqrt { C ^ { 2 } \alpha ^ { 2 } ( R - 2 \alpha - R \tau ) ( 3 R + 2 \alpha + R \tau ) } \right) } } { \alpha ^ { 2 } ( R + 2 \alpha + R \tau ) } ,$ we have $\frac { \partial N _ { D 1 } ^ { * } } { \partial \beta } > 0$

(5) The first-order derivative of the number of users in Period 1 with respect to $\begin{array} { r } { \beta \mathrm { i s } \frac { \partial N _ { A 1 } ^ { * } } { \partial \beta } = } \end{array}$ $\displaystyle \frac { C \Big ( 6 C \alpha \beta ( R + 2 \alpha + R \tau ) + \alpha ^ { 2 } \beta ^ { 2 } \big ( 2 \alpha + R ( 5 + \tau ) \big ) - 3 C ^ { 2 } \big ( 2 \alpha + R ( \tau - 3 ) \big ) \Big ) } { \cos { \mathrm { ~ \alpha ~ o ~ n ~ 2 ~ } \ell \mathrm { ~ c ~ e ~ n ~ } \omega } \mathrm { . ~ } }$ , we find that: if $\begin{array} { r } { R \leq \frac { 2 \alpha } { 1 - \tau } , } \end{array}$ when $\beta \leq$ (3??−????) (??+????) $\begin{array} { r } { \frac { 2 \sqrt { 3 } \sqrt { C ^ { 2 } \alpha ^ { 2 } ( 2 \alpha + R ( \tau - 1 ) ) ( 2 \alpha + R ( 3 + \tau ) ) } - 3 C \alpha ( R + 2 \alpha + R \tau ) } { 2 \mathrm { ~ \ell ~ \alpha ~  ~ \ell ~ \alpha ~ } } , } \end{array}$ , we have $\frac { \partial N _ { A 1 } ^ { * } } { \partial \beta } \leq 0$ , and when $\beta >$ ??<sup>2</sup>(2??+??(5+??)) $\frac { 2 \sqrt { 3 } \sqrt { C ^ { 2 } \alpha ^ { 2 } ( 2 \alpha + R ( \tau - 1 ) ) ( 2 \alpha + R ( 3 + \tau ) ) } - 3 C \alpha ( R + 2 \alpha + R \tau ) } { \alpha ^ { 2 } ( 2 \alpha + R ( 5 + \tau ) ) } ;$ , we have $\frac { \partial N _ { A 1 } ^ { * } } { \partial \beta } > 0$ ; if $\begin{array} { r } { R > \frac { 2 \alpha } { 1 - \tau } , } \end{array}$ we have $\frac { \partial N _ { A 1 } ^ { * } } { \partial \beta } > 0$

(6) The first-order derivative of the number of developers in Period 2 with respect to $\begin{array} { r } { \beta \mathrm { i s } \frac { \partial N _ { D 2 } ^ { * } } { \partial \beta } = } \end{array}$ $\frac { \alpha \Bigl ( R \alpha ^ { 2 } \beta ^ { 2 } + 2 C \alpha \beta ( 2 \alpha + R \tau ) - C ^ { 2 } \bigl ( 4 \alpha + R ( 2 \tau - 3 ) \bigr ) \Bigr ) } { ( 3 C - \alpha \beta ) ^ { 2 } ( C + \alpha \beta ) ^ { 2 } }$ . Then, if $\begin{array} { r } { R \leq \frac { 2 \alpha } { 1 - \tau } ; } \end{array}$ when $\begin{array} { r } { \beta \leq \frac { \sqrt { C ^ { 2 } \alpha ^ { 2 } ( 2 \alpha + R ( \tau - 1 ) ) ( 2 \alpha + R ( 3 + \tau ) ) } - C \alpha ( 2 \alpha + R \tau ) } { R \alpha ^ { 2 } } } \end{array}$ we have $\begin{array} { r } { \frac { \partial N _ { D 2 } ^ { * } } { \partial \beta } \leq 0 . } \end{array}$ , and when $\begin{array} { r } { \beta > \frac { \sqrt { C ^ { 2 } \alpha ^ { 2 } ( 2 \alpha + R ( \tau - 1 ) ) ( 2 \alpha + R ( 3 + \tau ) ) } - C \alpha ( 2 \alpha + R \tau ) } { R \alpha ^ { 2 } } } \end{array}$ , we have $\begin{array} { r } { \frac { \partial N _ { D 2 } ^ { * } } { \partial \beta } > 0 ; \mathrm { i f } R > \frac { 2 \alpha } { 1 - \tau } , } \end{array}$ we have $\frac { \partial N _ { D 2 } ^ { * } } { \partial \beta } > 0$

(7) The first-order derivative of the number of users in Period 2 with respect to ?? is $\begin{array} { r } { \frac { \partial N _ { A 2 } ^ { * } } { \partial \beta } = \frac { 3 C ( 2 \alpha + R ( 3 + \tau ) ) } { 2 ( 3 C - \alpha \beta ) ^ { 2 } } } \end{array}$ , which is positive.

## Proof of Proposition 4

The optimality conditions in A1 require $1 2 C ^ { 2 } - 2 \alpha \beta ^ { 3 } ( 1 + \tau ) - C \big ( 4 \alpha ^ { 2 } - 4 \alpha \beta ( 2 + \tau ) + \beta ^ { 2 } ( 3 + \tau ^ { 2 } ) \big ) > 0 .$ . By solving $( 2 C + R \beta ) \big ( 3 C + 2 \alpha ( \beta - \alpha ) \big ) + 2 \alpha \big ( R \beta ^ { 2 } + C ( \beta - R ) \big ) \tau + C R \beta \tau ^ { 2 } > 0 .$ , we obtain that if $\alpha < \alpha _ { f } , f ^ { * } >$

0; and if $\alpha \ge \alpha _ { f } , f ^ { * } \le 0$ , where $\begin{array} { r } { \alpha _ { f } = \frac { R \beta ^ { 2 } ( 1 + \tau ) + C \beta ( 2 + \tau ) - C R \tau } { 4 C + 2 R \beta } + \frac { \left( \left( R \beta ^ { 2 } ( 1 + \tau ) + C \beta ( 2 + \tau ) - R C \tau \right) ^ { 2 } + 2 \left( 2 C + R \beta \right) \left( 6 C + R \beta \left( 3 + \tau ^ { 2 } \right) \right) \right) ^ { \frac { 1 } { 2 } } } { 4 C + 2 R \beta } . } \end{array}$

## Proof of Proposition 5

The derivative of the optimal access fee with respect to ?? is:

$$
\frac {\partial f ^ {*}}{\partial R} = \frac {2 C \alpha \tau - 2 \alpha \beta^ {2} (1 + \tau) + \beta (2 \alpha^ {2} - \tau^ {2} - 3 C)}{2 \alpha \beta^ {3} (1 + \tau) + C (4 \alpha^ {2} - 4 \alpha \beta (2 + \tau) + \beta^ {2} (3 + \tau^ {2})) - 1 2 C ^ {2}}.
$$

Then, $\frac { \partial f ^ { * } } { \partial R } > 0$ is equivalent to $\begin{array} { r } { 0 < \alpha < \frac { \beta ^ { 2 } ( 1 + \tau ) - C \tau + \sqrt { 2 C \beta ^ { 2 } ( 3 - \tau ) + C ^ { 2 } \tau ^ { 2 } + \beta ^ { 4 } ( 1 + \tau ) ^ { 2 } } } { 2 \beta } . } \end{array}$

## Proof of Lemma 5

$$
\begin{array}{l} \text {If} \alpha \leq \frac {2 C ^ {2} - 2 R \beta^ {3} (1 + \tau) + C \beta \big (R (5 + \tau) - 2 \beta (1 + \tau) \big) - 2 F _ {1}}{4 C R} \text {or} \alpha \geq \frac {2 C ^ {2} - 2 R \beta^ {3} (1 + \tau) + C \beta \big (R (5 + \tau) - 2 \beta (1 + \tau) \big) + 2 F _ {1}}{4 C R}, p _ {d 1} ^ {*} \text {is negative; if} \\ \frac {2 C ^ {2} - 2 R \beta^ {3} (1 + \tau) + C \beta \big (R (5 + \tau) - 2 \beta (1 + \tau) \big) - 2 F _ {1}}{4 C R} <   \alpha <   \frac {2 C ^ {2} - 2 R \beta^ {3} (1 + \tau) + C \beta \big (R (5 + \tau) - 2 \beta (1 + \tau) \big) + 2 F _ {1}}{4 C R}, p _ {d 1} ^ {*} > 0. \text {Note that} \alpha \text {is} \end{array}
$$

1 ቀ8??<sup>2</sup>??ቀ????(??−3)+2??(3+??)−????<sup>2</sup>(3+??<sup>2</sup>)ቁ+(2??<sup>2</sup>−2????<sup>3</sup>(1+??)+????(??(5+??)−2??(1+??)))<sup>2</sup>ቁ<sup>2</sup> Define ??<sub>1</sub> = 2 , ??<sub>1</sub> = max $\left\{ 0 , \frac { 2 C ^ { 2 } - 2 R \beta ^ { 3 } \left( 1 + \tau \right) + C \beta \left( R \left( 5 + \tau \right) - 2 \beta \left( 1 + \tau \right) \right) - 2 F _ { 1 } } { 4 C R } \right\}$ , and $\begin{array} { r } { \overline { { \alpha } } _ { 1 } = \frac { 2 C ^ { 2 } - 2 R \beta ^ { 3 } \left( 1 + \tau \right) + C \beta \left( R \left( 5 + \tau \right) - 2 \beta \left( 1 + \tau \right) \right) + 2 F _ { 1 } } { 4 C R } . } \end{array}$ . Then, if $\alpha \leq$ $\underline { { \alpha _ { 1 } } }$ , we have $p _ { d 1 } ^ { * } \leq 0 ; \mathrm { i f } \underline { { \alpha } } _ { 1 } < \alpha < \overline { { \alpha } } _ { 1 }$ , we have $p _ { d 1 } ^ { * } > 0 ; \mathrm { i f } \alpha \geq \overline { { \alpha } } _ { 1 }$ , we have $p _ { d 1 } ^ { * } \leq 0$

## Appendix B: Extensions

## Extension 1: Users Participating before Developers

In practice, before third-party developers are allowed to join the platform, some software platforms, such as Apple, already have users on the platform because of first-party software. Therefore, in this extension, we assume that there are users on the platform before third-party developers begin participating and investigate how the participation of users affects the platform’s optimal pricing strategy. When third-party developers make participation decisions in Period 1, they can observe the number of users on the platform. Thus, a developer’s expected profit gained in Period 1 is reformulated as

$$
\pi_ {D 1} ^ {F} = R + \alpha N _ {A 0} - p _ {d 1} - c,
$$

where $N _ { A 0 }$ is the number of users who join the platform before the third-party developers’ participation. Thus, the number of developers joining the platform in Period 1 is

$$
N _ {D 1} ^ {F} = \frac {1}{C} (R + \alpha N _ {A 0} - p _ {d 1}).
$$

First, we analyze the platform’s optimal pricing strategies if it charges zero access fees to users $( f = 0 )$ in Lemma B1 and B2. Defining the threshold: $\begin{array} { r } { \alpha _ { 1 } = \frac { 2 C N _ { A 0 } - C - R \beta + \left( ( C + R \beta - 2 C N _ { A 0 } ) ^ { 2 } + 2 C R \beta ( 3 - \tau ) N _ { A 0 } \right) ^ { \frac { 1 } { 2 } } } { 2 \beta N _ { A 0 } } . } \end{array}$

Lemma B1. If the platform charges no access fee to users, the skimming pricing strategy is more profitable than the penetration pricing strategy if and only if the intensity of the user-to-developer network effect is weak $( 0 < \alpha \leq \alpha _ { 1 } ) ;$ otherwise, the penetration pricing strategy is superior.

## Lemma B2. If the platform charges no access fee to users:

(a) When the platform adopts the skimming pricing strategy $( 0 < \alpha < \alpha _ { 1 } )$ , it should charge developers in both periods.

(b) When the platform adopts the penetration pricing strategy, the platform should charge developers in Period 2 and in Period 1

(i) if the user-to-developer network effect is sufficiently weak $\begin{array} { r } { ( \alpha _ { 1 } < \alpha \leq \frac { 2 C N _ { A 0 } - C + C ( 1 + 8 N _ { A 0 } ^ { 2 } ) ^ { \frac { 1 } { 2 } } } { 2 \beta N _ { A 0 } } ) } \end{array}$ , the platform should charge developers $( p _ { d 1 } ^ { * } > 0 )$ .

(ii) if the intensity of the user-to-developer network effect is moderate $\begin{array} { r } { ( \frac { 2 C N _ { A 0 } - C + C ( 1 + 8 N _ { A 0 } ^ { 2 } ) ^ { \frac { 1 } { 2 } } } { 2 \beta N _ { A 0 } } < \alpha < } \end{array}$ $\frac { C { \left( 3 - \tau + \sqrt { 3 3 + \tau ( 2 + \tau ) } \right) } } { 4 \beta } )$ ), and developers have a relatively pessimistic expectation of the revenue they gain per unit of time $\begin{array} { r } { ( 0 < R \leq \frac { 2 \alpha ( C ^ { 2 } + 2 C \alpha \beta - \alpha ^ { 2 } \beta ^ { 2 } ) N _ { A 0 } + 2 C ^ { 2 } \alpha - 2 C \alpha ^ { 2 } \beta } { 2 \alpha ^ { 2 } \beta ^ { 2 } + C \alpha \beta ( \tau - 3 ) + C ^ { 2 } ( 3 + \tau ) } ) } \end{array}$ , the platform prefers to subsidize developers.

(iii) if the intensity of the user-to-developer network effect is strong $\begin{array} { r } { ( \frac { C \left( 3 - \tau + \sqrt { 3 3 + \tau ( 2 + \tau ) } \right) } { 4 \beta } \leq \alpha < 3 C / \beta ) } \end{array}$ , the platform is better off subsidizing developers.

In summary, although the existence of users before developers begin participating changes the threshold conditions characterizing the optimal pricing strategy, the pattern of the network effect’s effects on the platform’s optimal strategy remains unchanged. Furthermore, when the platform charges an access fee to users or provides a subsidy to users, through numerical analysis, we find that our main findings still hold, as shown in Figure B1.

![](/api/attachments/5FNUFG6X/fulltext/images/ce872ab96481565a38c0ef7e6a749ebe3d8beb9529b1bf98fc5e381b7efa0186.jpg)  
a. Platform’s Pricing Strategy on the User Side (?? = ??. ??, ?? = −??. ??, ?? = ??, ?? = ??)

![](/api/attachments/5FNUFG6X/fulltext/images/aace3eb4bbbca7717320bdf41ee8b6f5e242e693d23beded57f7cfc1673d4d73.jpg)  
b. Platform’s Pricing Strategy on the Developer Side $( \beta = 0 . 5 , \tau = 0 . 2 , N _ { A 0 } = 0 . 2 , C = 1 )$  
Figure B1. Optimal Strategy on Both the User and Developer Sides When $f \neq 0$

## Extension 2: Same-Side Network Effect

In this extension, we take potential competition among developers into account. The developer’s expected profit gained in Period 2 is reformulated as

$$
\pi_ {D 2} ^ {S} = \pi_ {D 2} - \gamma N _ {\mathrm{D1}},
$$

where ?? is the same-side network effect among developers. Thus, the number of developers joining the platform in Period 2 is given by

$$
N _ {D 2} ^ {S} = \frac {1}{C} \left(p _ {\mathrm{d} 1} - p _ {\mathrm{d} 2} + \alpha N _ {\mathrm{A} 1} - \gamma N _ {\mathrm{D} 1} + R \left(\frac {\tau - 1}{2}\right)\right).
$$

Lemma B3 and B4 summarize the platform’s optimal pricing strategies if it charges users no access fee $( f = 0 )$

Lemma B3: If the platform charges no access fee to users, the skimming pricing strategy is more profitable if and only if and only if the intensity of the user-to-developer network effect is weak $\begin{array} { r } { \begin{array} { r } { ( 0 < \alpha \leq \frac { C R ( 3 - \tau ) + 2 R \gamma } { 2 ( C + R \beta ) } ) . } \end{array} } \end{array}$

## Lemma B4. If the platform charges no access fee to users:

(a) When the platform adopts the skimming pricing strategy $\begin{array} { r } { ( 0 < \alpha < \frac { C R ( 3 - \tau ) + 2 R \gamma } { 2 ( C + R \beta ) } ) } \end{array}$ , it should charge developers in both periods.

(b) When the platform adopts the penetration pricing strategy, the platform should charge developers in Period 2, and in Period 1

(i) if the intensity of the user-to-developer network effect is sufficiently weak $\begin{array} { r } { ( \frac { C R ( 3 - \tau ) + 2 R \gamma } { 2 ( C + R \beta ) } < \alpha \leq \frac { \gamma + C } { \beta } ) } \end{array}$ the platform’s optimal strategy is to charge developers, $\mathrm { i } . \mathrm { e } . , p _ { d 1 } ^ { \ast } > 0$

(ii) if the intensity of the user-to-developer network effect is moderate $\begin{array} { r } { ( \frac { \gamma + C } { \beta } < \alpha < \frac { 4 \gamma + \left( 3 - \tau + \sqrt { 3 3 + \tau ( 2 + \tau ) } \right) } { 4 \beta } ) _ { } } \end{array}$ and developers have a relatively pessimistic expectation of the revenue they gain per unit of time $( 0 <$ $\begin{array} { r } { R \leq \frac { 2 C ^ { 2 } \alpha - 2 C \alpha ( \alpha \beta - \gamma ) } { 2 ( \gamma - \alpha \beta ) ^ { 2 } + C ( \alpha \beta - \gamma ) ( \tau - 3 ) - C ^ { 2 } ( 3 + \tau ) } \big ) _ { \lvert \tau \rvert } } \end{array}$ , the platform prefers to subsidize developers.

(iii) if the intensity of the user-to-developer network effect is strong $\begin{array} { r } { \frac { 4 \gamma + \left( 3 - \tau + \sqrt { 3 3 + \tau ( 2 + \tau ) } \right) } { 4 \beta } \leq \alpha < \frac { \gamma + 3 C } { \beta } ) } \end{array}$ , the platform is better off subsidizing developers.

From Lemma B3 and B4 we find that our main findings still hold when $f = 0$ after taking the same-side network effect among developers into account. When the platform charges an access fee from or provides a subsidy to users, through numerical analysis, we find that the main findings in Section 5 are still valid, as shown in Figure B2.

![](/api/attachments/5FNUFG6X/fulltext/images/16bc57a1f90e8113bb61ee6b2af7621edff64c6280e69608e219f88ef8e5ae25.jpg)  
a. Platform’s Pricing Strategy on the User Side (?? = ??. ??, ?? = −??. ??, ?? = ??, ?? = ??)

![](/api/attachments/5FNUFG6X/fulltext/images/e2cd9c7b4824cf82b0756aec697419ca9810656eeb1d8aaf8c4480fb39df07a7.jpg)  
b. Platform’s Pricing Strategy on the Developer Side (?? = ??. ??, ?? = ??. ??, ?? = ??. ??, ?? = ??)  
Figure B2. Optimal Pricing Strategy on Both the User and Developer Sides When $f \neq 0$ with Same-Side Network Effect

## Extension 3: Transaction Fee

In practice, some software platforms charge developers transaction fees. For example, Apple takes 30% of the revenue generated on the App Store from developers. Therefore, in this extension, we take transaction fees into account and investigate how the transaction fee affects the platform’s optimal pricing strategy. The developer’s expected profit gained in Period $2 ^ { 8 }$ is reformulated as,

$$
\pi_ {D 2} ^ {T} = \pi_ {D 2} - \mu \delta N _ {A 1},
$$

where $\mu$ is the per-transaction fee paid to the platform and $\delta$ denotes the developer’s estimated percentage of users who will purchase its product. Thus, the number of new developers joining the platform in Period 2 is given by

$$
N _ {D 2} ^ {T} = \frac {1}{C} \bigg ((\alpha - \mu \delta) N _ {A 1} - p _ {d 2} + p _ {d 1} - R \left(\frac {\tau - 1}{2}\right) \bigg).
$$

Accordingly, the optimization problem is reformulated as

$$
\begin{array}{r l} \max _ {p _ {d 1}, p _ {\mathrm{d} 2}} \pi^ {\mathrm{T}} = p _ {d 1} N _ {D 1} + p _ {d 2} N _ {D 2} + \lambda \left(\left(\frac {1 - \tau}{2}\right) N _ {\mathrm{A} 1} N _ {\mathrm{D} 1} + \left(\frac {1 + \tau}{2}\right) N _ {\mathrm{A} 2} N _ {\mathrm{D} 2}\right), \\ \mathrm{s.t.} N _ {A 1}, N _ {A 2} \geq 0, N _ {D 1}, N _ {D 2} \geq 0. \end{array}
$$

To ease exposition, we denote $\lambda = \mu \delta$ . If the platform charges users no access fee, we reexamine the platform’s optimal pricing strategy on the developer side through numerical analysis. The results, shown in Figure B3, indicate that the penetration pricing strategy still outperforms the skimming pricing strategy if the user-to-developer network effect is sufficiently strong when the transaction fee is taken into consideration.

![](/api/attachments/5FNUFG6X/fulltext/images/a66b9d0031a50c6f7be2edbf8f1a65130eba260905654d9ea6e62780e0c2b927.jpg)  
Figure B3. Platform’s Pricing Strategy for Developers when $\pmb { f } = \pmb { 0 }$ with a Transaction Fee (?? = ??. ??, ?? = ??. ??, ?? = ??. ??, ?? = ??)

Lemma B5: If no access fee is charged to users, in Period 1, if the user-to-developer network effect is weak $( \alpha \leq$ $\mathrm { m a x } \{ 0 , \alpha _ { 1 } ^ { T } \} )$ or strong $( \alpha > \alpha _ { 2 } ^ { T } )$ , the platform should subsidize developers. Otherwise, if the user-to-develope network effect satisfies max $\{ 0 , \alpha _ { 1 } ^ { T } \} < \alpha < \alpha _ { 2 } ^ { T }$ , the platform is better off charging developers.

$$
\begin{array}{r l} & {\mathrm{Denote} F _ {1} = \frac {\binom{4 C ^ {4} + 1 6 R ^ {2} \beta^ {4} \lambda^ {2} (\tau^ {2} - 1) + 4 C ^ {3} \beta (4 \lambda (\tau - 1) + R (9 + \tau)) + 8 C R \beta^ {3} \lambda (2 R (\tau - 3) + 3 \lambda (1 - \tau^ {2}))}{+ C ^ {2} \beta^ {2} (3 2 R \lambda (\tau - 2) + 8 \lambda^ {2} (1 - \tau^ {2}) + R ^ {2} (3 3 + \tau (2 + \tau)))}}{\frac {2}{4 \beta (C + R \beta)}}, \alpha_ {1} ^ {T} =} \\ & {\frac {2 C ^ {2} + 2 R \beta^ {2} \lambda (1 - \tau) + C \beta (3 R + 2 \lambda - (R + 2 \lambda) \tau) - 2 F _ {1}}{4 \beta (C + R \beta)}, \alpha_ {2} ^ {T} = \frac {2 C ^ {2} + 2 R \beta^ {2} \lambda (1 - \tau) + C \beta (3 R + 2 \lambda - (R + 2 \lambda) \tau) + 2 F _ {1}}{4 \beta (C + R \beta)}.} \end{array}
$$

Compared with the findings in Proposition 3, Lemma B5 indicates that with the per-transaction fee, the platform is more likely to subsidize developers in Period 1. The reason is that subsidizing developers in Period 1 can entice more developers to join in Period 1 and then make profits by collecting the transaction fees. By numerical analysis, we also find that when the platform charges the transaction fee, subsidizing developers in Period 2 is viable, as shown in Figure B4.

![](/api/attachments/5FNUFG6X/fulltext/images/1f9c3b0c8e75aa998b945fb5a4f1fd63e365898b874a5c275b9296d1233767c5.jpg)  
Figure B4. Charging or Subsidizing Developers in the Second Period When a Per-Transaction Fee is Charged $( \beta = 0 . 5 , \tau = 0 . 2 , \lambda = 0 . 2 , C = 1 )$

When the platform charges users an access fee or offers users a subsidy, through numerical analysis (shown in Figure B5), we find that after taking the per-transaction fee into account the main findings in Section 5 are still valid.

![](/api/attachments/5FNUFG6X/fulltext/images/654612f4ece334b7883ce984ea4eea44f2f0e00a2f11dc2068f300ebbc020e5e.jpg)

![](/api/attachments/5FNUFG6X/fulltext/images/d22bb288b2db58a29eade2f663732e1cbd2b7f419559315945d92937f7ff988c.jpg)  
a. Platform’s Pricing Strategy on the User Side (?? = ??. ??, ?? = −??. ??, ?? = ??, ?? = ??)  
b. Platform’s Pricing Strategy on the Developer Side (?? = ??. ??, ?? = ??. ??, ?? = ??. ??, ?? = ??)  
Figure B5. The Platform’s Optimal Pricing Strategy on the User Side and Developer Side when $f \neq 0$ with a Transaction Fee

## Extension 4: Charging Different Access Fees to Users in the Two Periods

In this extension, we consider the case in which the platform charges different access fees to users in the two periods. Thus, the utility derived by users (per unit of time) in Period 1 after joining the platform is formulated as

$$
u _ {A 1} = v + \beta N _ {D 1} - f _ {1},
$$

where $f _ { 1 }$ is the user’s access fee paid for joining the platform or the subsidy offered by the platform in Period 1. The number of users joining the platform in Period 1 is:

$$
N _ {A 1} = 1 + \beta N _ {D 1} - f _ {1}.
$$

Similarly, the users’ utility (per unit of time) derived in Period 2 is reformulated as:

$$
u _ {A 2} = v + \beta (N _ {D 2} + N _ {D 1}) - f _ {2},
$$

where $f _ { 2 }$ is the user’s access fee paid for joining the platform or the subsidy offered by the platform in Period 2. And the number of users joining in Period 2 is:

$$
N _ {A 2} = 1 + \beta (N _ {D 2} + N _ {D 1}) - f _ {2}.
$$

The platform’s optimization problem is given by

$$
\begin{array}{r l} & {\underset {p _ {d 1}, p _ {\mathrm{d} 2}} {\max} \pi = p _ {d 1} N _ {D 1} + p _ {d 2} N _ {D 2} + \frac {1 - \tau}{2} f _ {1} N _ {A 1} + \frac {1 + \tau}{2} f _ {2} N _ {A 2},} \\ & {\qquad \mathrm{s.t.} N _ {A 1}, N _ {A 2} \geq 0, N _ {D 1}, N _ {D 2} \geq 0.} \end{array}
$$

Through numerical analysis, we find that when the platform charges different access fees to users during the two periods, it prefers to charge a higher access fee or provide a lower subsidy to users in Period 2 if the intensity of the user-to-developer network effect is strong, as shown in Figure B6(a). The reason is that a lower access fee or a higher subsidy in Period 1 can lure more users to join in Period 1, and then the platform could make profits by utilizing the high user-to-developer network effect to attract developers and users in Period 2. Figure B6 shows that the main findings in Section 5 are still valid.

![](/api/attachments/5FNUFG6X/fulltext/images/8c80e5e93cad68cdbc963e71af900679f22bb375451082489c871ef6a5308e50.jpg)  
a. Optimal Access Fees on the User Side (?? = ??. ??, ?? = ??, ?? = −??. ??, ?? = ??)

![](/api/attachments/5FNUFG6X/fulltext/images/8c24a1ca75b7e09e4401831a45de6ad5d67b197a0be6cef294f92949e859434b.jpg)  
b. Platform’s Pricing Strategy on the Developer Side (?? = ??. ??, ?? = ??. ??, ?? = ??. ??, ?? = ??)  
Figure B6. The Platform’s Optimal Pricing Strategy on the User Side and Developer Side in the Two Periods

## About the Authors

Nan Yuan is a PhD candidate in the Department of Information Management and Management Science at the College of Management and Economics, Tianjin University. Her research interests include platform economics and pricing strategies. She has presented her work at the Pacific Asia Conference on Information Systems.

Haiyang Feng is an associate professor of information management and management science at the College of Management and Economics, Tianjin University. He received his PhD in management science from Tianjin University in 2014. His current research interests include economics of information systems, platform strategy, and business analytics. His papers have been published in academic journals including MIS Quarterly, Decision Support Systems, International Journal of Production Economics, Computers & Industrial Engineering, Computers & Operation Research, among others.

Minqiang Li is a professor in the Department of Information Management and Management Science at the College of Management and Economics, Tianjin University, Tianjin, P. R. China. He received a PhD degree in systems engineering and management science from Tianjin University. His major research interests cover management science and decision support, electronic commerce, data mining, and business intelligence, and evolutionary computation. Hi papers have appeared in Management Science, MIS Quarterly, Journal of Management Information Systems, European Journal of Operational Research, Journal of Evolutionary Economics, International Journal of Production Economics, Information & Management, IEEE Transactions on Neural Networks and Learning Systems, Information Sciences, and other journals.

Nan Feng is a professor of information management and management science in the College of Management and Economics, Tianjin University. He received his PhD degree in management science from Tianjin University in 2007. His current research interests include economics of information systems, information security, and business analytics. He has published in MIS Quarterly, Decision Support Systems, Information & Management, Electronic Commerce Research and Applications, Enterprise Information Systems, among other journals.

Copyright © 2022 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
