---
otero_id: 11048
otero_key: "ARJZHTJJ"
title: "A Study of Enterprise Software Licensing Models"
authors: "Shengli Li; Hsing Kenneth Cheng; Yang Duan; Yu-Chen Yang"
year: "2017"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2017.1297636"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Study of Enterprise Software Licensing Models

Shengli Li, Hsing Kenneth Cheng, Yang Duan & Yu-Chen Yang

To cite this article: Shengli Li, Hsing Kenneth Cheng, Yang Duan & Yu-Chen Yang (2017) A Study of Enterprise Software Licensing Models, Journal of Management Information Systems, 34:1, 177-205, DOI: 10.1080/07421222.2017.1297636

To link to this article: http://dx.doi.org/10.1080/07421222.2017.1297636

![](/api/attachments/ARJZHTJJ/fulltext/images/7881ccdc0b721f261f0c437b46c37143dae78bd577521c3020466a9fe786f3ab.jpg)

View supplementary material

![](/api/attachments/ARJZHTJJ/fulltext/images/50b6d0ffef0458fc22cee07633cbba5499411b8323e716ad8e1efc7ce9aed508.jpg)

Published online: 20 Apr 2017.

![](/api/attachments/ARJZHTJJ/fulltext/images/c01c818d7c6786c084361cc347704f4f14005773755327e2695bcdafdd17a790.jpg)

Submit your article to this journal

![](/api/attachments/ARJZHTJJ/fulltext/images/66cef18eed0b497a3d880afd7ee256130b8ac3953b0c650966a3de4b19acd7c9.jpg)

Article views: 15

![](/api/attachments/ARJZHTJJ/fulltext/images/cb2ffa95ec9901365ac3c834f27439abbc4e696aedb4f7df7c6cd0c2910ab4ed.jpg)

View related articles

![](/api/attachments/ARJZHTJJ/fulltext/images/de6d31596fa2eb1bd95a86c8187329ad5d6602fe3892aae7dbe795c5af3ea2b1.jpg)

View Crossmark data

# A Study of Enterprise Software Licensing Models

SHENGLI LI, HSING KENNETH CHENG, YANG DUAN, AND YU-CHEN YANG

SHENGLI LI (lishengli@mail.xjtu.edu.cn; corresponding author) is an associate professor in the Department of Information Management and Electronic Commerce of the School of Management, Xi’an Jiaotong University. He received his Ph.D. in information systems (IS) from the University of Florida. His research interests include economics of IS, cloud computing, supply chain management, and social networks analysis. His work has been published in Decision Support Systems, European Journal of Operational Research, and Production and Operations Management.

HSING KENNETH CHENG (kenny.cheng@warrington.ufl.edu) is the John B. Higdon Eminent Scholar and chair of the Department of Information Systems and Operations Management of Warrington College of Business Administration at the University of Florida. He received his Ph.D. in computers and information systems from William E. Simon Graduate School of Business Administration, University of Rochester. His research interests focus on analyzing the impact of Internet technology on software development and marketing, and on IS policy issues, in particular network neutrality.

YANG DUAN (yangduan@hkbu.edu.hk) is an assistant professor in the Department of Finance and Decision Sciences at Hong Kong Baptist University. She obtained her doctoral degree with a concentration in corporate finance at the Chinese University of Hong Kong. Her primary research interests include corporate finance, financial markets, social media, and e-commerce.

YU-CHEN YANG (ycyang@mis.nsysu.edu.tw) is an assistant professor in the Department of Information Management in the College of Management at National Sun Yat-sen University, Taiwan. He received his Ph.D. in information systems from the University of Florida. His research interests include e-commerce, economics of information systems, and data mining.

ABSTRACT: We study an enterprise software vendor’s decision on three prominent licensing models– on-premises, software as a service (SaaS), and hybrid. Our findings indicate that both the customers’ estimation of the future software quality improvement and network effects play critical roles in the software vendor’s choice of optimal licensing models. If the network effects are weak, the enterprise software vendor should choose the on-premises model when customers have a low estimation of the software quality improvement in the upgrade version. The hybrid model should be implemented if this estimation is in the mid-range, while the SaaS model generates the highest profit when customers believe that the upgrade version will have a significant improvement in software quality. As the network effects become stronger, the on-premises model will be dominated by the other two licensing models and is never optimal. In the event of a high upgrade cost and strong network effects, SaaS becomes the best licensing model due to its multitenancy nature.

KEY WORDS AND PHRASES: enterprise software, network effects, on-premises license, SaaS, software as a service, software licensing, software quality uncertainty.

Traditionally, corporations purchase enterprise software, defined as the software intended to solve enterprise-wide problems, by paying the price up front and installing the software on their computers, a software licensing practice known as the on-premises model. Examples of enterprise software include customer relationship management (CRM) software, enterprise resources planning (ERP) software, and others. With the rapid advancement of the Internet in the late 1990s, software as a service (SaaS) has emerged as a new software licensing model and gained significant popularity [22]. In this licensing model, customers pay a subscription fee on a recurring basis, and have access to the software as long as they pay the subscription fee<sup>1</sup>. Many businesses that could not afford the steep licensing fees of on-premises software can now benefit from the SaaS delivery model [17]. It has been estimated that SaaS sales will grow from \$22.6 billion in 2013 to \$50.8 billion in 2018, with a yearly growth rate around 17.6 percent [8].

The SaaS model has attracted well-established software vendors such as Oracle, SAP, and Microsoft to offer some of their applications on a subscription basis. In particular, the SaaS model is now a common delivery model for enterprise software providers. While the revenues from SaaS sale are growing, the SaaS is cannibalizing the market of the on-premises enterprise software. As the SaaS licensing model is gaining more and more popularity, a critical question facing the enterprise software vendors is whether they will be better off by converting to the SaaS model from the on-premises model. A major objective of this study is to provide guidelines for enterprise software vendors on this critical issue.

The SaaS model in essence amounts to a software leasing model where the customers rent the software from the vendor and pay the rent for the period of usage. The on-premises model is a selling model in which customers purchase the software and own the license perpetually. Although the problem of whether to sell or lease physical goods has been studied extensively, enterprise software has three distinct features that have not been considered in prior literature. First, customers of enterprise software will incur a customization cost or unfit cost not usually seen in the purchase or leasing of physical goods. This is because enterprise software comes with embedded business processes—that is, a prescribed way of doing business that may not be commensurate with a customer’s existing processes. Customers adopting enterprise software under the on-premises model have to either reengineer their business processes to fit the enterprise software or customize the enterprise software to fit their own idiosyncrasies, which can lead to a substantial customization cost [4].

Note that customization is very different from configuration of enterprise software. Customization involves tinkering with the source code of the software, whereas configuration deals with choosing among options provided within the software such as U.S. versus European date and currency format. The SaaS provider runs the software on its server, while all of its customers are connected to the server to use the software through the Internet, a typical feature of SaaS called “multitenancy.” Thus, it is virtually impossible for customers subscribing to the software through the SaaS licensing model to customize the software according to their preferences. Dillon et al. [12] find that “not enough ability to customize” is one of the most significant challenges facing the SaaS model. Thus, SaaS customers bear an unfit cost, but incur no customization cost. Customers who desire to customize enterprise software to fit their unique needs have to opt for an on-premises licensing model and incur a customization cost.

The second distinct feature of enterprise software is that upgrade is an important issue to consider in adopting it because a newer version becomes available just a few years after the previous one. For example, “the real catch for many long term enterprise resource planning customers is the continuing cost of upgrades” [21, paragraph 1]. In the on-premises model, customers who purchased the previous version have the option to pay an upgrade price to upgrade to the new version. In the SaaS model, the upgrade is automatically done at the server by the provider and all customers have access to the latest version without paying the upgrade price. The estimation of the quality of the newer version in the future complicates a forward-looking customer’s decision about whether to adopt the software at the present. “Multitenancy” is the third distinct feature that allows SaaS providers to benefit from economies of scale. When a new version of software becomes available, every customer under the on-premises license who chooses to upgrade incurs an upgrade cost, while an SaaS provider charges only a one-time upgrade cost for all its customers, which results in an economy of scale benefit in upgrading to new version. Last but certainly not least, software exhibits positive network effects since customers’ utility increases with the number of customers adopting the same software.

The enterprise software vendor essentially has three options for licensing its software. The vendor can adopt a pure on-premises licensing model, a pure SaaS licensing model, or a hybrid model where both on-premises and SaaS models are available to customers. One example of enterprise software adopting the hybrid licensing model is Microsoft Dynamics CRM. Customers can either choose the Microsoft Dynamics CRM online (SaaS) or the Microsoft Dynamics CRM On-Premises. Considering the distinct features of enterprise software discussed above, this study aims to provide useful guidelines for enterprise software vendors regarding which licensing model—on-premises, SaaS, or hybrid—generates the highest profit. We find that the vendor should adopt the SaaS licensing model when customers’ estimation of software quality improvement in the future is low. The optimal licensing choice is the on-premises model when customers’ estimation of future software quality improvement is high, and the hybrid model is optimal when customers’ estimation of future software quality improvement is medium. Furthermore, a key finding of our research indicates that the on-premises model is dominated in the presence of strong network effects. We also find that a higher customization cost or upgrade cost favors the SaaS model while a higher unfit cost or realized software quality improvement in the future favors the on-premises model.

## Literature Review

Our research draws on three streams of literature: leasing versus selling, customers’ uncertainty about product quality, and cloud computing and SaaS. The research on leasing versus selling is relevant to our research in that SaaS is essentially a leasing model of software and on-premises is a selling model. Using the automobile market as an example, Desai and Purohit [11] adopt a two-period model to analyze the leasing and selling strategies of durable goods. They find that the depreciation rate of durable goods is a critical factor that impacts the profitability of leasing and selling. Extending the previous work, Desai and Purohit [10] analyze the problem of a duopoly in which each vendor optimizes its fraction of units to lease. They find that the fraction of lease, shown to depend on the reliability of goods, decreases with the increase of competition between manufacturers and the similarity of their products. Bhaskaran and Gillbert [2] investigate the impact of a complementary product on a durable goods manufacturer’s choice on leasing and selling. They show that when the extent of complementarities is sufficiently strong, the manufacturer’s preference for leasing will shift to selling. Chien and Chu [7] study selling and leasing strategy for durable goods with network externalities. They find that selling can be more profitable than leasing when the product or technology is relatively new. However, the leasing strategy is preferable when the market matures. The two-period model adopted in our research follows that of the prior literature. We extend the prevailing two-period model of leasing versus selling adopted in previous research to capture the intrinsic features of SaaS and on-premises models, including the unfit cost under the SaaS model, the customization cost under the on-premises model, and the economies of scale in upgrade cost due to the “multitenancy” feature of SaaS

Another relevant stream of literature focuses on the impact of customers’ uncertainty about product quality on the vendor’s product strategy. Cheng and Liu [5] and Cheng et al. [6] study the impact of customers’ uncertainty on software vendors’ free trial strategy. They find that free trial strategies involving the time-locked feature could help alleviate the effect of customers’ uncertainty about new software. Customers’ uncertainty in the setting of advance selling is somewhat similar to uncertainty about the quality of software upgrade in the future. Prasad et al. [20] investigate under which condition it will be optimal for the vendor to adopt the advance selling mechanism given customers’ uncertainty about product quality. They find that the vendor is better off with advance selling when the customers’ expected valuation exceeds customers’ expected surplus of not buying advance by a certain threshold. Niculescu and Wu [18] study two emerging software business models including feature-limited freemium where the vendor offers the software for free and charges for premium features, and uniform seeding where the vendor gives the full product for free to a percentage of the market uniformly across the customer types. They find that customers’ prior estimation of the value of functionality is one of the key factors influencing the software vendor’s choice of optimal business models. Boone et al. [3] empirically demonstrate that customers’ perceptions of future product introductions influence their purchase actions. In one study on incentives of content contributors on YouTube, Tang et al. [24] categorize forward-looking contributors as considering both current and future utilities when making contributions. Similar to previous research in this stream, our research shows that the customer’s estimation on future improvement of software quality is a crucial factor that influences the software vendor’s choice of licensing models.

The literature most relevant to our study is the research on cloud computing and SaaS. SaaS involves mainly two types of pricing models: subscription and pay-per-use (or pay-per-transaction). Several researchers have investigated the pay-per-use pricing model of SaaS. Balasubramanian et al. [1] analyze the pay-per-use mechanism and the traditional selling mechanism for pricing information goods. They find that the payper-use mechanism yields a higher profit depending on the usage frequency and the transaction cost associated with the pay-per-use pricing scheme. Postmus et al. [19] compare two software pricing strategies: fixed fee and pay-per-use licensing, assuming that customers can develop the software in-house. They find that the vendor prefers payper-use licensing when in-house development costs are expensive; otherwise it prefers fixed fee. Ma and Seidmann [16] look into the issue of the competition between SaaS and MOTS (modifiable off-the-shelf) providers. In their model, they capture the multitenancy structure of SaaS, the capacity hedging challenge of MOTS users, and the cost savings from economies of scale and lack-of-fit costs in the SaaS environment. They find that the SaaS provider should invest in reducing both its lack-of-fit costs and its pertransaction price to benefit from increased economies of scale. Although our study focuses on the subscription model rather than the pay-per-use model of SaaS, the multitenancy and lack-of-fit costs of SaaS are common features of our model and those in the aforementioned literature.

Several researchers also investigated the supply chain of SaaS under the pay-peruse model. Demirkan et al. [9] study four coordination strategies between ASP (application service provider) and AIP (application infrastructure provider) in an SaaS supply chain. They find that it is possible for the two partners to agree on a profit-sharing strategy that can make the socially desired equilibrium their preferred strategy. In one empirical study, Susarla et al. [23] identified two forms of contracts in the SaaS supply chain: fixed price contracts in which users agree to pay a prespecified fixed price per month, and time and materials contracts in which ASPs use a cost-based pricing approach and bill clients for monthly usage. They find that performance guarantees are significantly associated with a higher likelihood of fixed price contracts. Furthermore, service uncertainty is significantly associated with the likelihood of a time and materials contract.

There is a general lack of research on SaaS involving the subscription model, with the overwhelming majority of the SaaS literature focusing on the pay-per-use pricing model. (Ma and Kauffman [15] and Fan et. al. [13] are among few notable exceptions.) However, enterprise software vendors tend to implement the subscription model rather than the pay-per-use model studied in prior literature. For example, the most popular customer relations management SaaS provider Salesforce.com charges by the number of users per period irrespective of the transaction volumes. Instead of the pay-per-use pricing mechanism, our study focuses on the subscription model to reflect the common practice adopted by enterprise software vendors. Our research contributes to the stream of literature on subscription pricing models in SaaS. In sum, our research contributes to three streams of literature: leasing versus selling, customer’s uncertainty about product quality, and SaaS. More important, our research is among the first to examine an enterprise software vendor’s optimal choice of licensing models by taking into account both the intrinsic features of the enterprise software and those of the underlying on-premise and SaaS licensing models.

## The Models

In this section, we present the SaaS, on-premises, and hybrid models and explore the software vendor’s optimal choice of licensing model. We first formulate the software vendor’s profit function under each licensing model, and then derive the vendor’s optimal profits under each model, and determine under what conditions the vendor should opt for which licensing model. The base models in this section do not consider network effects. In the next section, we introduce the network effects and examine the influence of such effects on the vendor’s licensing decisions.

We adopt the prevailing two-period model where the enterprise software vendor provides the first version in the first period and the upgraded version in the second period. Each period in our two-period model represents the lifecycle of enterprise software before the next major upgrade, which typically covers a time horizon of two to three years. At the beginning of the first period, the customers’ valuation v is uniformly distributed in the interval 0; v , where v represents the customer who has the highest valuation of the first version software. The customer estimates that her valuation in the second period will becomev 1 θ if she adopts the upgraded version software. At the beginning of the second period, the customer learns that her true valuation is v 1 k from adopting the upgraded version software. Table 1 summarizes the notation used in our model.

In general, agile software development follows a product roadmap as “the basis for The process starts with listing all the product features and enhancements, followed by prioritizing and scheduling these features and enhancements. The requirement specs of the future enhancements are usually two versions ahead and the design specs are one version ahead of the current software. Therefore, the quality of the upgrade version to be released in the second period, k; has been determined and is known to the enterprise software vendor at the beginning of the first period. The customers, however, do not know the value ofkat the beginning of the first period and can only form an estimate of θ. The enterprise software vendor can obtain the customers’ estimation of upgrade version quality θ by different market investigation schemes. For example, using the structured questionnaire developed in Hendriks et al. [14], the enterprise software vendor can perform market research to obtain the value of customers’ estimation of the upgrade version quality.

Table 1. Notations

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
v Customer's valuation of the software, uniformly distributed in $[0,\bar{v}]$ $\theta$ The customers' estimation of the software quality improvement in the second period  
$k$ The true quality improvement of the software in the second period  
$P_L$ The subscription fee under the SaaS model  
$P_{S1}$ The price in period 1 under the on-premises model  
$P_{S2}$ The price in period 2 under the on-premises model  
$P_U$ Upgrade price of the new version for customers who purchase the first version and choose to upgrade  
$C_m$ Customization cost under the on-premises model  
$C_f$ Unfit cost under the SaaS model  
$C_u$ Upgrade cost
</div>

## The SaaS Licensing Model

Customers who choose to subscribe to the software will sign a contract with the software vendor that lasts for two periods. If the customers choose to subscribe, they pay a subscription fee $P _ { L }$ in each period. Under the SaaS model, customers will incur an unfit cost $C _ { f }$ per period. In addition to the unfit cost due to the embedded business processes of the enterprise software not compatible with those of the customers, the unfit cost can also arise because of reliability and security issues of the SaaS delivery model [17]. The higher the customer’s concern about reliability and security, the higher the unfit cost of the SaaS model to the customer. In the second period, the enterprise software vendor undertakes the upgrade cost $C _ { u }$ and upgrades the software for all customers. The customers’ estimated utility from subscribing to the software equals $U _ { L L } = \nu - P _ { L } - C _ { f } + \nu ( 1 + \theta ) - P _ { L } - C _ { f }$ , where the subscript LL indicates Lease (subscribing) in the first period and Lease in the second period. Those customers who choose not to subscribe to the SaaS have the utility $U = 0 .$

It is worth noting that even without a contract requiring a subscription in both periods, customers who subscribe in the first period will still subscribe in the second period. This can easily be shown as follows. The estimated two-period utility of subscribing in both periods equals $U _ { L L } = \nu - P _ { L } - C _ { f } + \nu ( 1 + \theta ) - P _ { L } - C _ { f }$ : The estimated two-period utility of strategy Lease (subscribing) only in the first period and Inactive in the second period equals $U _ { L \mathrm { I } } = \nu - P _ { L } - C _ { f }$ . It is obvious that $U _ { L \mathrm { I } } \geq 0$ if and only $\mathrm { i f } \nu \geq P _ { L } + C _ { f }$ . It follows that $U _ { L L } > U _ { L \mathrm { I } }$ when $\nu \ge P _ { L } + C _ { f }$ . Thus, customers who subscribe in the first period will still subscribe in the second period even without the force of a contract.

Our base model does not consider the possibility of customers not subscribing in the first period and yet opting to do so in the second period on observing the realized quality of the upgrade version k. While this might occur in the rare extreme case where k is exceedingly high (e.g., the upgrade version is two times better than the first version), this extreme case is excluded in the base model for the sake of simplicity and conformity to reality.<sup>4</sup>

The marginal customer type who is indifferent between subscribing to the software and not subscribing is denoted by $\nu _ { o } ,$ where $\begin{array} { r } { \nu _ { o } = \frac { 2 ( P _ { L } + C _ { f } ) } { 2 + \theta } } \end{array}$ after simple algebra. For ease of analytical exposition and presentation, we ignore the discount factor in our two-period model. Introducing the discount factor δ will not change the qualitative behavior of our results. The total number of customers who subscribe to the software thus equals $\bar { \nu } - \frac { 2 ( P _ { L } + C _ { f } ) } { 2 + \theta }$ . The profit function under the SaaS licensing model is $\begin{array} { r } { \pi = 2 P _ { L } \Big ( \bar { \nu } - \frac { 2 ( P _ { L } + C _ { f } ) } { 2 + \theta } \Big ) - C _ { u } } \end{array}$ . We then summarize the software vendor’s optimal subscription fee and profit as follows.

Lemma 1: When the enterprise software vendor adopts the SaaS licensing model, it charges the optimal subscription fee $\begin{array} { r } { P _ { L } { } ^ { * } = \frac { ( 2 + \theta ) \bar { \nu } - 2 C _ { f } } { 4 } } \end{array}$ and achieves an optimal profit of $\begin{array} { r } { \pi ^ { * } = \frac { \left( ( 2 + \theta ) \hat { \nu } - 2 C _ { f } \right) ^ { 2 } } { 4 ( 2 + \theta ) } - C _ { u } } \end{array}$

## The On-Premises Licensing Model

Under the on-premises model, the enterprise software vendor sells the first version at $P _ { S 1 }$ in the first period and the upgraded version in the second period. Customers who purchase the software in the first period need to customize the software and incur a customization cost $C _ { m }$ in addition to the purchase price of the software $P _ { S 1 }$ . In the second period, those who have purchased the software in the first period and choose to upgrade pay an upgrade price $P _ { U }$ to obtain the upgraded version of the software. In addition, they bear the upgrade cost $C _ { u }$ that captures the effort required for customers to implement the upgrade. We let $C _ { u } { > } C _ { m }$ and $C _ { u } { > } C _ { f }$ . That is, the upgrade cost is more substantial than the customization cost and unfit cost. Customers who have not purchased the first version can buy the upgraded version at price $P _ { S 2 }$ in the second period. Reflecting the reality, we let $P _ { S 2 } \geq P _ { S 1 }$ and $P _ { S 2 } \geq P _ { U }$ , implying that the price of the newer version is no less than that of the first version and the upgrade price.

## The Customers’ Decision in the First Period

At the beginning of the first period, the customers decide to purchase or not by calculating the total utility from both the first and second periods. Only if making the purchase now leads to a higher two-period utility will the customers choose to purchase in the first period. In total, they consider the following four strategies: Remain Inactive in both periods (II), Inactive in the first period and only Buy in the second period (IB), Buy in the first period and Hold on to the older version in the second period (BH), and Buy in the first period and Upgrade in the second period (BU). Customers will choose to purchase in the first period only if their estimated two-period utility satisfies the condition max $( B H , B U ) { > } \operatorname* { m a x } ( I I , I B )$ , which indicates that purchasing in the first period will lead to a higher two-period total utility than not doing so. Customers’ estimated two-period utility of strategy II equals $U _ { I I } = 0 $ The estimated two-period utility of strategy IB equals $U _ { I B } = \nu ( 1 + \theta ) - P _ { S 2 } - C _ { m }$ . The estimated two-period utility of strategy BH equals $U _ { B H } = \nu - P _ { S 1 } - C _ { m } + \nu ,$ while the estimated two-period utility of strategy BU equals $U _ { B U } = \nu - P _ { S 1 } - C _ { m } + \nu ( 1 + \theta ) - P _ { U } - C _ { u }$

It can easily be shown that the strategy IB is always dominated by BH because $U _ { I B } \leq U _ { B H }$ . Thus, customers have only three possible strategies (II, BH, BU) to consider at the beginning of the first period. The marginal customer type who is indifferent between II and BH is $\begin{array} { r } { \nu _ { 1 } = \frac { P _ { S 1 } + C _ { m } } { 2 } } \end{array}$ ; and the marginal customer type who is indifferent between BH and BU is $\begin{array} { r } { \nu _ { 2 } = \frac { P _ { U } + C _ { u } } { \theta } } \end{array}$ . Customers’ preferences for the three strategies are depicted in the following two possible market segmentations.

In the first scenario, $\nu _ { 2 } \geq \nu _ { 1 }$ . The corresponding market segmentation is shown in Figure 1. The segments of BH and BU correspond to customers who believe purchasing the software in the first period will bring a higher two-period total utility. Thus, the first period demand equals $\bar { \nu } - \frac { P _ { S 1 } + C _ { m } } { 2 }$

In the second scenario, $\nu _ { 2 } { < } \nu _ { 1 }$ . Customers expect that the strategy BU always brings in a higher two-period utility than BH. The market is segmented as in Figure 2. The marginal customer type who is indifferent between II and BU in Figure 2 equals $\frac { P _ { S 1 } + P _ { U } + C _ { m } + C _ { u } } { \gamma _ { + } \mu }$ resulting in demand in the first period in this scenario of $\begin{array} { r } { \bar { \nu } - \frac { P _ { S 1 } + P _ { U } + \bar { C } _ { m } + C _ { u } } { 2 + \theta } } \end{array}$

## The Customers’ Decision in the Second Period

First we discuss the customers’ decision in the second period in scenario 1. At the beginning of the second period, the true value of quality improvement k will be revealed to the customers. Based on the realized knowledge of k, customers will decide whether to upgrade or to purchase the latest version depending on their prior purchase decision in the first period.

<table><tr><td colspan="2">II</td><td colspan="2">BH</td><td colspan="2">LL</td></tr><tr><td> $\nu$ </td><td></td><td> $v_1$ </td><td></td><td> $v_2$ </td><td></td></tr></table>

Figure 1. Market Segmentation in the On-Premises Model Under Scenario 1, Where All Three Types of Customers (II, BH, BU) Exist

![](/api/attachments/ARJZHTJJ/fulltext/images/2b0b6e388941b21dc4bc3d37bff909255c4463f93d1e5b5fc62af954be48db08.jpg)  
Figure 2. Market Segmentation in the On-Premises Model Under Scenario 2, Where Only Two Types of Customers (II, BU) Exist

Customers who have purchased the first version in the first period will derive utility $U = \nu ( 1 + k ) - P _ { U } - C _ { u }$ if they choose to upgrade. The utility they will derive in the second period by sticking to the previous version is given by $U = \nu .$ . Thus, customers whose valuation satisfies the condition $\nu ( 1 + k ) - P _ { U } - C _ { u } { > } \nu ,$ i.e, $\nu > \frac { P _ { U } + C _ { u } } { k }$ will choose to upgrade. Therefore, the number of customers choosing to upgrade in the second period equals $\bar { \nu } - \frac { P _ { U } + C _ { u } } { k }$ . Note that the number of customers who choose to upgrade cannot exceed the number of customers who have purchased in the first period, implying that $\begin{array} { r } { \frac { P _ { U } + C _ { u } } { k } \ge \frac { P _ { S 1 } + C _ { m } } { 2 } } \end{array}$ must hold. This condition can be rewritten as $\begin{array} { r } { P _ { U } \ge \frac { { P _ { S 1 } } + { C _ { m } } } { 2 } k - C _ { u } } \end{array}$ . The intuition is that all customers will choose to upgrade in the second period when $P _ { U }$ is low enough.

Customers who have not purchased in the first period will derive utility $U = \nu ( 1 + k ) - P _ { S 2 } - C _ { m }$ if they choose to purchase the latest version in the second period. If they choose not to purchase in the second period either, they will derive 0 utility in the second period. Thus, customers whose valuation satisfies the condition $\nu > \frac { P _ { S 2 } + C _ { m } } { 1 + k }$ will choose to purchase in the second period, and the number of customers who purchase in the second period equals $\frac { P _ { S 1 } + C _ { m } } { 2 } - \frac { P _ { S 2 } + C _ { m } } { 1 + k }$ . To guarantee that this demand will be nonnegative, the condition $\frac { P _ { S 1 } ^ {  } { + } C _ { m } } { 2 } \geq \frac { \overset { ! } { P } _ { S 2 } ^ {  } { + } C _ { m } } { 1 { + } k }$ needs to be satisfied. This condition can be rewritten as $\begin{array} { r } { P _ { S 2 } \le \frac { 1 + k } { 2 } ( P _ { S 1 } + C _ { m } ) - C _ { m } } \end{array}$ . We find that the condition $\begin{array} { r } { P _ { S 2 } \le \frac { 1 + k } { 2 } ( P _ { S 1 } + C _ { m } ) - C _ { m } } \end{array}$ can never be satisfied, indicating that no customer will purchase only in the second period under scenario 1.

Customers’ behavior in the second period in scenario 2 is described as follows. Similar to scenario 1, customers who have purchased the first version in the first period will choose to upgrade if their valuation satisfies the condition $\nu > \frac { P _ { U } + C _ { u } } { k }$ . Thus, the number of customers who choose to upgrade in the second period equals $\begin{array} { r } { \bar { \nu } - \frac { P _ { U } + C _ { u } } { k } } \end{array}$ . Note that the number of customers who upgrade in the second period cannot exceed the number of customers who purchase in the first period. Therefore, the condition $\begin{array} { r } { \frac { P _ { U } + C _ { u } } { k } \ge \frac { P _ { S 1 } + P _ { U } + C _ { m } + C _ { u } } { 2 + \theta } } \end{array}$ must hold.

Customers who did not purchase in the first period will decide whether to purchase in the second period based on their knowledge of k. Customers whose valuation satisfies the condition $\nu { > } \frac { P _ { S 2 } { + } C _ { m } } { 1 { + } k }$ will choose to purchase in the second period. Thus, the number of customers who purchase in the second period equals $\begin{array} { r } { \frac { \tilde { P _ { S 1 } { + } } \tilde { P _ { U } } { + } C _ { m } { + } C _ { u } } { 2 + \theta } - \frac { P _ { S 2 } { + } C _ { m } } { 1 + k } } \end{array}$ . To guarantee nonnegative demand, the condition $\begin{array} { r } { \frac { \tilde { P _ { S 1 } } + \tilde { P _ { U } } + C _ { m } + C _ { u } } { 2 + \theta } \geq \frac { \tilde { P _ { S 2 } } + C _ { m } } { 1 + k } } \end{array}$ must hold. We find this condition cannot be satisfied, ruling out the existence of customers who purchase only in the second period in scenario 2.

## Optimal Profit of the Software Vendor Adopting On-Premises Licensing Model

Summarizing the results of previous sections, the software vendor’s optimization problem under scenario 1 is described by Equation (1):

$$
\begin{array}{c} \max _ {P _ {S 1}, P _ {S 2}, P _ {U}} \pi = P _ {S 1} \cdot (\bar {\nu} - \frac {P _ {S 1} + C _ {m}}{2}) + P _ {U} \cdot (\bar {\nu} - \frac {P _ {U} + C _ {u}}{k}) \\ s. t. P _ {U} \geq \frac {k}{2} (P _ {S 1} + C _ {m}) - C _ {u} \\ P _ {U} \geq \frac {\theta}{2} (P _ {S 1} + C _ {m}) - C _ {u} \end{array} ,\tag{1}
$$

and specified by Equation (2) under scenario 2:

$$
\begin{array}{c} \max _ {P _ {S 1}, P _ {S 2}, P _ {U}} \pi = P _ {S 1} \cdot (\bar {\nu} - \frac {P _ {S 1} + P _ {U} + C _ {m} + C _ {u}}{2 + \theta}) + P _ {U} \cdot (\bar {\nu} - \frac {P _ {U} + C _ {u}}{k}) \\ s. t. \frac {P _ {U} + C _ {u}}{k} \geq \frac {P _ {S 1} + P _ {U} + C _ {m} + C _ {u}}{2 + \theta} \\ P _ {U} \leq \frac {\theta}{2} (P _ {S 1} + C _ {m}) - C _ {u} \end{array} .\tag{2}
$$

Solving the above optimization problems, we find that the optimal solutions are characterized by a threshold value of customers’ estimation of future quality improvement θ. When $\begin{array} { r } { \theta \leq \frac { 2 \left( \bar { \nu } k + C _ { u } \right) } { 2 \bar { \nu } + C _ { m } } } \end{array}$ ; the optimal solutions are:

$$
P _ {S 1} ^ {*} = \frac {2 \bar {\nu} - C _ {m}}{2},\tag{3}
$$

$$
P _ {U} ^ {*} = \frac {k \bar {v} - C _ {u}}{2}, \text { and }\tag{4}
$$

$$
\pi^ {*} = \frac {2 C _ {u} {} ^ {2} + k C _ {m} {} ^ {2} + 2 k \bar {\nu} ((2 + k) \bar {\nu} - 2 (C _ {m} + C _ {u}))}{8 k}..\tag{5}
$$

If $\theta { > } \frac { 2 ( \bar { \nu } k { + } C _ { u } ) } { 2 \bar { \nu } { + } C _ { m } }$ ; the optimal solutions are:

$$
P _ {S 1} ^ {*} = \big \{ \begin{array}{l} \frac {(2 + \theta) \bar {\nu} - C _ {m} - C _ {u}}{2}, k <   \frac {4 C _ {u} + 2 \theta C _ {u}}{C _ {m} + C _ {u} + 2 \bar {\nu} + \theta \bar {\nu}} \\ \frac {(2 - k + \theta) C _ {u} - (2 + k + \theta) C _ {m} + (2 + \theta) (2 - k + \theta) \bar {\nu}}{2 (2 + \theta)}, k \geq \frac {4 C _ {v} + 2 \theta C _ {u}}{C _ {m} + C _ {u} + 2 \bar {\nu} + \theta \bar {\nu}}, \end{array}\tag{6}
$$

$$
P _ {U} ^ {*} = \left\{ \begin{array}{l} 0, k <   \frac {4 C _ {U} + 2 \theta C _ {u}}{C _ {m} + C _ {u} + 2 \bar {\nu} + \theta \bar {\nu}} \\ \frac {C _ {m} k + C _ {u} (k - 2 \theta - 4) + k \bar {\nu} (2 + \theta)}{2 (2 + \theta)}, k \geq \frac {4 C _ {u} + 2 \theta C _ {u}}{C _ {m} + C _ {u} + 2 \bar {\nu} + \theta \bar {\nu}}, \text { and } \end{array} \right.\tag{7}
$$

$$
\pi^ {*} = \frac {\left((2 + \theta) \bar {v} - C _ {m} - C _ {u}\right) ^ {2}}{4 (2 + \theta)}..\tag{8}
$$

The above solutions indicate that the software vendor’s optimal price, upgrade price, and profit are independent of θ when customers’ prior estimation is lower than or equal to the threshold value $\frac { 2 ( \bar { \nu } k + C _ { u } ) } { 2 \bar { \nu } + C _ { m } }$ . In this case, customers’ low estimation of the quality improvement in the second period will lead to the total demand in the first period, $\bar { \nu } - \frac { P _ { S 1 } + C _ { m } } { 2 }$ ; being independent of θ (corresponding to scenario 1). In the second period, the quality improvement becomes known, and demand is influenced by the realized quality improvement parameter k rather than θ.

When customers’ prior estimation is higher than the threshold value, the software vendor’s optimal price, upgrade price, and profit are influenced by θ. In particular, the profit is increasing in θ. At the beginning of the first period, when θ is high enough, customers who decide to buy in the first period will plan to upgrade in the second period (corresponding to scenario 2). A higher $\theta$ causes the marginal customer type who is indifferent between buying and not buying shifting leftward, which expands demand in the first period, leading to a higher profit.

We also observe that there are two cases when $\theta { > } \frac { 2 ( \bar { \nu } k { + } C _ { u } ) } { 2 \bar { \nu } { + } C _ { m } }$ . At the beginning of the second period, customers learn the value of k and then decide whether to upgrade or not. When k is low such that $\begin{array} { r } { k { < \frac { 4 C _ { u } + 2 { \theta } C _ { u } } { C _ { m } + C _ { u } + 2 \bar { \nu } + \theta \bar { \nu } } } } \end{array}$ , no customer is willing to upgrade even if the upgrade price is 0 due to the upgrade cost. Hence, the software vendor can arbitrarily charge a nonnegative upgrade price since the upgrade demand will always be zero. We let the optimal upgrade price be zero for simplicity. We summarize the findings in the following proposition.

Proposition 1: When the software vendor adopts the on-premises licensing model, there exists a threshold value $\frac { 2 ( \bar { \nu } k + C _ { u } ) } { 2 \bar { \nu } + C _ { m } }$ of the customers’ estimation of the quality improvement in the second period (θ). When $\begin{array} { r } { \theta \leq \frac { 2 \left( \bar { \nu } k + C _ { u } \right) } { 2 \bar { \nu } + C _ { m } } } \end{array}$ , the software vendor sets the price and upgrade price as described in Equations (3) and (4), and achieves an optimal profit of Equation (5). When $\theta { > } \frac { \hat { 2 } ( \hat { \nu } k { + } C _ { u } ) } { 2 \hat { \nu } { + } C _ { m } }$ , the optimal price and upgrade price are specified in Equations (6) and (7), and the optimal profit for the software vendor is shown in Equation (8).

There are several interesting findings from Proposition 1. Intuitively, the enterprise software vendor will achieve a higher profit through improving customers’ estimation of the software quality improvement in the second period. However, Proposition 1 indicates that the profit remains unchanged with the increase of $\theta$ when $\theta$ is smaller than the threshold value $\frac { 2 ( \bar { \nu } k + C _ { u } ) } { 2 \bar { \nu } + C _ { m } }$ . Only when $\theta { > } \frac { 2 ( \bar { \nu } k { + } C _ { u } ) } { 2 \bar { \nu } { + } C _ { m } }$ , improving customers’ prior estimation leads to a higher profit (in this case $\textstyle { \frac { \partial \pi ^ { * } } { \partial \theta } } > { \ddot { 0 } } )$ . Simple comparative statics analysis shows that this threshold value increases in $C _ { u }$ and $k ,$ and decreases in $C _ { m }$

Another counterintuitive result from Proposition 1 is that the increase in the realized software quality improvement in the second period k does not necessarily lead to an increase in the upgrade price. Only when the value of $k$ is greater than $\frac { 4 C _ { u } + 2 \theta C _ { u } } { C _ { m } + C _ { u } + 2 \bar { \nu } + \theta \bar { \nu } }$ , will there be customers who are willing to upgrade, and the optimal upgrade fee increases with $k ( \xrightarrow { \partial P _ { U } } ^ { * } > 0 )$ .

## The Hybrid Licensing Model

Under the hybrid model, the enterprise software vendor offers both the SaaS and onpremises versions to the market simultaneously. Customers can access the software through either licensing model. All the characteristics under the pure SaaS model and on-premises model remain unchanged in the hybrid model.

## Customers’ Decision in the First Period

In the beginning of the first period, customers decide whether to purchase, subscribe, or do nothing based on their estimated total utility of two periods. Since the SaaS model requires subscription in both periods, there are no options to Lease in the first period and Inactive in the second period (denoted by LI), Inactive in the first period and Lease in the second period (IL), Lease in the first period and Buy in the second period (LB), and Buy in the first period and Lease in the second period (BL). Thus, customers consider the following five potential strategies: remain Inactive in both periods (II), Inactive in the first period and Buy in the second period (IB), Buy in the first period and Hold on to the older version in the second period (BH), Buy in the first period and Upgrade in the second period (BU), and Lease in both periods (LL). It can be easily shown that the strategy IB is always dominated by BH, thus leaving only four feasible strategies for customers: II, BH, BU, LL. Customers’ estimated two-period utility of strategy II equals $U _ { I I } = 0$ The estimated two-period utility of strategy BH equals $U _ { B H } = \nu - P _ { S 1 } - C _ { m } + \nu ,$ , while the estimated two-period utility of strategy BU equals $U _ { B U } = \nu - P _ { S 1 } - C _ { m } + \nu ( 1 + \theta ) - P _ { U } - C _ { u }$ . Finally, the estimated two-period utility of strategy LL equals $U _ { L L } = \nu - P _ { L } - C _ { f } + \nu ( 1 + \theta ) - P _ { L } - C _ { f }$

We find that the comparison between the strategies LL and BU only depends on prices including $P _ { S 1 } , \ P _ { U }$ ; and $P _ { L }$ since $U _ { B U } - U _ { L L } = 2 ( P _ { L } + C _ { f } ) - P _ { S 1 } - C _ { m } - P _ { U } - C _ { u }$ This implies that strategies BU and LL will not coexist because customers will either find strategy BU more desirable than LL or the other way around. The software vendor can choose the magnitudes of $P _ { S 1 } , P _ { U }$ ; and $P _ { L }$ to lead customers to choose either LL or BU. Desai and Purohit (1998) discussed a similar phenomenon in their study of the leasing and selling strategies in the automobile market. Following the terms used in Desai and Purohit (1998), we define two marketing strategies for the software vendor as: (1) premium lease, under which the software vendor’s pricing decision makes the LL strategy more desirable than the BU strategy for customers; (2) value lease, under which the BU strategy dominates the LL strategy.

In the case of value lease, only three strategies are left to customers: II, BH, and BU. In this case, the hybrid model converges to a pure on-premises model as we have discussed above.

In the case of premium lease, the three strategies left are II, BH, and LL. The marginal customer type who is indifferent between II and BH is given by $\begin{array} { r } { \nu _ { 1 } = \frac { P _ { S 1 } + C _ { m } } { 2 } } \end{array}$ ; and the marginal customer type who is indifferent between BH and LL is $\begin{array} { r } { \nu _ { 2 } = \frac { 2 P _ { L } + 2 C _ { f } - P _ { s 1 } - C _ { m } } { \theta } } \end{array}$ . Customers’ preferences for the three strategies are depicted in the following two possible market segmentations.

In the first scenario, $\nu _ { 2 } \geq \nu _ { 1 }$ . The corresponding market segmentation is shown in Figure 3. The segment of BH corresponds to customers who believe purchasing the software in the first period will bring a higher two-period total utility. Thus, the number of customers who choose to purchase in the first period equals $\begin{array} { r } { \frac { 2 P _ { L } + 2 C _ { f } - P _ { s 1 } - C _ { m } } { \theta } - \frac { P _ { S 1 } + C _ { m } } { 2 } } \end{array}$ . The segment of LL corresponds to customers who believe subscribing in the first period will bring a higher two-period utility. Therefore, the number of customers who choose to subscribe in the first period equals $\begin{array} { r } { \bar { \nu } - \frac { 2 P _ { L } + 2 C _ { f } - P _ { s 1 } - C _ { m } } { \theta } } \end{array}$

In the second scenario, $\nu _ { 2 } { < } \nu _ { 1 }$ . Customers expect that the strategy LL always generates a higher two-period utility than BH. In this scenario, the hybrid model converges to a pure

![](/api/attachments/ARJZHTJJ/fulltext/images/66e8e04431816dbb04da2660f997ec9930ddc862834448e8466781e63c16e8e2.jpg)  
Figure 3. Market Segmentaion Under the Hybrid Model

SaaS model as we have analyzed above. Thus, only scenario 1 in the premium lease marketing strategy corresponds to the hybrid model and we will focus on this scenario in subsequent analyses.

## The Customers’ Decision in the Second Period

At the beginning of the second period, the true value of quality improvement k will be revealed to customers. Based on the realized knowledge of k, customers will decide whether to upgrade or purchase the latest version depending on their prior purchase decision in the first period. Recall that customers who subscribe in the first period will still subscribe in the second period as has been shown above. Thus, the number of customers who choose to subscribe in the second period equals that of the first period, $\begin{array} { r } { \bar { \nu } - \frac { 2 P _ { L } + 2 C _ { f } - P _ { s 1 } - C _ { m } } { \theta } } \end{array}$

Customers who have purchased the first version in the first period will derive the utility of $\nu ( 1 + k ) - P _ { U } - C _ { u }$ if they choose to upgrade. The utility they will derive in the second period by sticking to the previous version is given by $U = \nu .$ Thus, customers whose valuation satisfies the condition $\nu ( 1 + k ) - P _ { U } - C _ { u } { > } \nu , \mathrm { i . e , } \nu { > } \frac { P _ { U } + C _ { u } } { k }$ , will choose to upgrade. Therefore, the number of customers choosing to upgrade in the second period equals $\begin{array} { r } { \frac { 2 P _ { L } + 2 C _ { f } - P _ { s 1 } - C _ { m } ^ { * } } { \theta } - \frac { P _ { U } + C _ { u } } { k } } \end{array}$

## Optimal Profit of the Software Vendor Adopting the Hybrid Model

Based on the foregoing analyses, the software vendor’s decision problem offering the hybrid licensing model is described as follows:

$$
\begin{array}{l} \max _ {P _ {S 1}, P _ {S 2}, P _ {U}, P _ {L}} \pi = P _ {S 1} \cdot \left(\frac {2 P _ {L} + 2 C _ {f} - P _ {s 1} - C _ {m}}{\theta} - \frac {P _ {S 1} + C _ {m}}{2}\right) \\ + P _ {U} \cdot \left(\frac {2 P _ {L} + 2 C _ {f} - P _ {s 1} - C _ {m}}{\theta} - \frac {P _ {U} + C _ {u}}{k}\right) \\ + 2 P _ {L} \cdot \left(\bar {\nu} - \frac {2 P _ {L} + 2 C _ {f} - P _ {s 1} - C _ {m}}{\theta}\right) - C _ {u} \\ s. t. \frac {P _ {U} + C _ {u}}{k} \geq \frac {P _ {S 1} + C _ {m}}{2} \\ \frac {2 P _ {L} + 2 C _ {f} - P _ {s 1} - C _ {m}}{\theta} \geq \frac {P _ {U} + C _ {u}}{k} \end{array}\tag{9}
$$

The constraints ensure that the number of customers who upgrade is nonnegative and does not exceed the number of customers who purchase in the first period. We let

$$
\begin{array}{l} \bar {k} _ {1} = \frac {2 C _ {u} \theta}{\bar {\nu} \theta + 2 C _ {f} - C _ {m}}, \text { and } \\ \quad 4 \bar {\nu} \theta + 4 C _ {m} \theta + 4 C _ {m} + 4 C _ {u} - 8 C _ {f} \\ \bar {k} _ {2} = \frac {- \sqrt {\left(4 \bar {\nu} \theta + 4 C _ {m} \theta + 4 C _ {m} + 4 C _ {u} - 8 C _ {f}\right) ^ {2} - 3 2 C _ {u} \theta (2 \bar {\nu} + C _ {m})}}{2 (2 \bar {\nu} + C _ {m})} \end{array}
$$

tion to the above decision problem is given as follows:

$$
P _ {S 1} ^ {*} = \left\{ \begin{array}{l} \frac {2 \bar {\nu} - C _ {m}}{2}, k \leq \bar {k} _ {1} \\ \frac {2 \bar {\nu} - C _ {m}}{2}, \bar {k} _ {1} <   k <   \bar {k} _ {2} \\ \frac {k (2 (C _ {m} + C _ {u}) - k C _ {m} - 4 C _ {f}) + 2 \theta (2 (1 + k) C _ {m} - \bar {\nu} (4 + k) - 2 C _ {u})}{k ^ {2} - 4 \theta (2 + k)}, k \geq \bar {k} _ {2} \end{array} , \right.\tag{10}
$$

$$
P _ {U} ^ {*} = \{\frac {0 , k \leq \bar {k} _ {1}}{\frac {2 k C _ {f} + \bar {\nu} k \theta - k C _ {m} - 2 \theta C _ {u}}{4 \theta - k}}, \bar {k} _ {1} <   k <   \bar {k} _ {2}   \frac {\theta (4 + k) (2 C _ {u} - \bar {\nu} k) + k C _ {m} (k - 2 \theta) - 2 k ^ {2} C _ {f}}{k ^ {2} - 4 \theta (2 + k)}, k \geq \bar {k} _ {2}    ,\tag{11}
$$

$$
P _ {L} ^ {*} = \bigl \{ \begin{array}{l} \frac {(2 + \theta) \bar {\nu} - 2 C _ {f}}{4}, k \leq \bar {k} _ {1} \\ \frac {2 \bar {\nu} (k - 2 \theta (2 + \theta)) + 2 \theta C _ {u} + k C _ {m} - 4 C _ {f} (k - 2 \theta)}{4 (k - 4 \theta)}, \bar {k} _ {1} <   k <   \bar {k} _ {2} \\ \frac {(2 + \theta) ((C _ {m} + C _ {u}) k - 2 \bar {\nu} \theta (2 + k)) - 2 C _ {f} (2 + k) (k - 2 \theta)}{2 k ^ {2} - 8 \theta (2 + k)}, k \geq \bar {k} _ {2} \end{array} ,\tag{12}
$$

$$
\pi^ {*} = \left\{ \begin{array}{l} \big (C _ {m} ^ {2} k - 8 C _ {u} (2 C _ {u} + k) - 8 k \bar {\nu} (C _ {f} - 2 C _ {u}) + 4 k \bar {\nu} ^ {2} (1 - k) \big) \theta^ {2} \\ \frac {+ 2 k \theta (2 C _ {f} - C _ {m}) (2 C _ {f} - C _ {m} + 8 C _ {u} - 4 k \bar {\nu}) + 2 k \bar {\nu} ^ {2} \theta^ {2} - 4 k ^ {2} (2 C _ {f} - C _ {m}) ^ {2}}{8 k \theta^ {2}}, k \leq \bar {k} _ {1} \\ 4 k C _ {m} (k \bar {\nu} - 2 C _ {u}) + 1 6 k C _ {f} (2 \bar {\nu} \theta + 2 C _ {m} + C _ {u} - k \bar {\nu}) + k C _ {m} ^ {2} (k - 4 (2 + \theta)) \\ \frac {+ 4 \big (2 k C _ {u} ((4 + \bar {\nu}) \theta - k) + k \bar {\nu} ^ {2} (k - 2 \theta (2 + \theta)) - 2 \theta C _ {u} ^ {2} \big) - 3 2 k C _ {f} ^ {2}}{8 k (k - 4 \theta)}, \bar {k} _ {1} <   k <   \bar {k} _ {2}. \\ 4 (2 + k) C _ {f} ^ {2} + C _ {u} (2 C _ {u} + k (k - 2 \bar {\nu})) \\ - 2 C _ {f} ((C _ {m} + C _ {u}) (4 + k) - \bar {\nu} (2 + k) (k - 2 \theta)) \\ + \theta \big (C _ {u} ^ {2} + 2 \bar {\nu} ^ {2} (2 + k) - C _ {u} (8 + k (4 + \bar {\nu})) \big) \\ \frac {(2 + k) \bar {\nu} ^ {2} \theta^ {2} + C _ {m} ^ {2} (2 + \theta) + C _ {m} (2 + \theta) (2 C _ {u} - k \bar {\nu})}{4 \theta (2 + k) - k ^ {2}}, k \geq \bar {k} _ {2} \end{array} \right.\tag{13}
$$

Proposition 2: When the software vendor adopts the hybrid licensing model, three sets of optimal solutions are obtained for three different segments of the realized quality improvement in the second period (k). The software vendor sets the optimal price, upgrade price, and the subscription fee as described in Equations (10) to (12), and achieves an optimal profit of Equation (13).

When the realized quality improvement in the second period is low such that $k \leq \bar { k } _ { 1 }$ , the constraint $\begin{array} { r } { \frac { P _ { U } + C _ { u } } { k } \ge \frac { P _ { S 1 } + C _ { m } } { 2 } } \end{array}$ is binding. This implies that when the quality improvement in the second period is lower than the threshold value of $\bar { k } _ { 1 }$ , no customers choose to upgrade even if the upgrade is free of charge $( \mathrm { i } . \mathsf { e } . , P _ { U } = 0 )$ due to the significant upgrade cost. We thus let the optimal upgrade fee be ${ P _ { U } } ^ { * } { = } 0$ in this case for simplicity.

When the realized quality improvement in the second period is higher than the threshold value of $\bar { k } _ { 2 }$ ; the constraint $\begin{array} { r } { \frac { 2 P _ { L } + 2 C _ { f } - P _ { s 1 } - C _ { m } } { \theta } \geq \frac { P _ { U } + C _ { u } } { k } } \end{array}$ is binding. Then all customers who have purchased in the first period will upgrade in the second period. That is, when the quality improvement in the second period is high enough, all customers will choose to upgrade. Finally, when neither constraint is binding, a portion of the customers who have purchased in the first period will upgrade, while others will not.

We find from Proposition 2 that ${ P _ { S 1 } } ^ { * }$ is independent of θ when $k \leq \bar { k } _ { 1 }$ and $\bar { k } _ { 1 } < k < \bar { k } _ { 2 }$ . However, the optimal profits in three segments always involve θ, indicating that the increase or decrease of customers’ prior estimation can always impact the software vendor’s profit. Recall from Proposition 1 that the software vendor’s profit may not be influenced by θ under certain conditions. Propositions 1 and 2 taken together show that the added feature of SaaS under the hybrid model, compared to the pure on-premises model, allows the software vendor to benefit more from the increase of customers’ prior estimation.

## Which Licensing Model to Adopt?

In further analyses, we find that the hybrid model will degenerate to a pure on-premises model or SaaS model under specific conditions involving θ (customers’ prior estimation of the quality improvement of software in the second period) and $k$ (the realized quality improvement of software in the second period). In particular, the conditions under which the hybrid model will degenerate to a pure SaaS model are given by:

$$
\begin{array}{l} \theta \geq \frac {4 C _ {f}}{C _ {m}} - 2, k \leq \bar {k} _ {1} \\ \{\theta \geq \frac {1 6 C _ {f} - 8 C _ {m} - 4 C _ {u} + k C _ {m} + 2 k \bar {\nu}}{4 C _ {m}}, \bar {k} _ {1} <   k <   \bar {k} _ {2}. \\ \theta \geq \frac {2 (2 C _ {m} + 2 C _ {u} - C _ {f} k - k \bar {\nu} - 4 C _ {f})}{k \bar {\nu} - 2 C _ {m} - 2 C _ {u}}, k \geq \bar {k} _ {2} \end{array}\tag{14}
$$

The conditions under which the hybrid model will degenerate to a pure onpremises model are given by:

$$
\begin{array}{l} \theta \leq \frac {2 C _ {f} - C _ {m}}{\bar {\nu}}, k \leq \bar {k} _ {1} \\ \{\theta \leq \frac {k \bar {\nu} + 4 C _ {f} - 2 C _ {m} - C _ {u}}{2 \bar {\nu}}, \bar {k} _ {1} <   k <   \bar {k} _ {2} \\ \theta \leq \frac {k ^ {2} \bar {\nu} + 2 k \bar {\nu} + 4 C _ {f} (2 + k) - (4 + k) (C _ {m} + C _ {u})}{2 \bar {\nu} (2 + k)}, k \geq \bar {k} _ {2} \end{array} .\tag{15}
$$

As we observe from the above two sets of conditions, there are three regions for the values of k. For each region of $k ,$ there are two threshold values of θ. When θ is higher than a threshold value, the hybrid licensing model will degenerate to a pure SaaS model. When $\theta$ is lower than another threshold value, the hybrid model degenerates to a pure on-premises model.

The degeneration of the hybrid licensing model to the SaaS model (or the onpremises model) implies that the software vendor’s optimal pricing decisions derived from solving the hybrid model problem will have the result that no customers will choose to access the software through the on-premises model (or SaaS model). For example, when k is in the mid range, the hybrid model degenerates to a pure SaaS model if $\begin{array} { r } { \theta \geq \frac { 1 6 C _ { f } - 8 C _ { m } - 4 C _ { u } + k C _ { m } + 2 k \bar { \nu } } { 4 C _ { m } } } \end{array}$ . That is, in the case of optimality under the hybrid model, no customers access the software through the on-premises model. Note that the software vendor can still make the hybrid model happen in any case. For example, the software vendor can still attract customers to access the onpremises model by setting a very low $P _ { S 1 }$ and $P _ { U }$ . However, the profit generated by such a “hybrid” model will be lower than that of the SaaS model. We thus have the following proposition.

Proposition 3: For a given realized quality improvement in the second period (k), there exist two threshold values of the customers’ prior estimation of the quality improvement in the second period (θ). The hybrid model dominates when θ is in between the two threshold values. The SaaS model performs the best when θ is higher than the larger threshold value, while the on-premises model is preferable when θ is lower than the smaller threshold value. The threshold values of θ for three segments of k are given by Equations (14) and (15).

Proposition 3 indicates that a higher θ prefers SaaS while a lower θ prefers onpremises. When $\theta$ is in the mid range, the SaaS and on-premises coexist. The intuition behind Proposition 3 is as follows. Under the SaaS licensing model, the decrease in $\theta$ lowers customers’ willingness to subscribe to the software and thus leads to a lower demand and profit for the software vendor. Under the on-premises model, however, the decrease in θ does not impact the software vendor’s profitability when θ is low enough. When θ is high, all customers plan to upgrade in the second period (corresponding to scenario 2 as shown in Figure 2) and max $( B H , B U ) = B U$ holds for every customer. In this case, the first period demand, which equals $\begin{array} { r } { \bar { \nu } - \frac { P _ { S 1 } + P _ { U } + C _ { m } + C _ { u } } { 2 + \theta } } \end{array}$ , will be lower with a decrease in θ. When θ is low enough, however, a group of customers who plan to hold on to the old version in the second period starts to appear (corresponding to scenario 1 as shown in Figure 1). When a group of customers who prefer strategy BH exists, demand in the first period, which equals $\bar { \nu } - \frac { P _ { S 1 } + C _ { m } } { 2 }$ , is independent of θ. The second period demand (equals $\begin{array} { r } { \bar { \nu } - \frac { P _ { U } + C _ { u } } { k } ) } \end{array}$ is also independent of θ. As a result, when θ is low enough, the profit achieved under the on-premises licensing model stays the same when θ decreases, while the profit achieved under the licensing models that involves SaaS (including SaaS and hybrid) decreases when θ decreases. Therefore, the on-premises licensing model is preferable when $\theta$ is low enough. In contrast, when $\theta$ is high enough, pure SaaS is more attractive.

## Comparative Statics

To examine the impact of unfit cost and customization cost on the enterprise software vendor’s optimal licensing model choice, we define the threshold value of θ above which the hybrid model will degenerate to a pure SaaS model as $\bar { \theta } _ { 1 }$ ; and the threshold value of $\theta$ below which the hybrid model will degenerate to a pure onpremises model as $\bar { \theta } _ { 2 }$ . Table 2 summarizes the comparative statics of $\bar { \theta } _ { 1 }$ and $\bar { \theta } _ { 2 }$ with respect to the unfit cost $C _ { f }$ and the customization cost $C _ { m }$ . See the appendix for proof. We observe from Table 2 that the partial derivatives of $\bar { \theta } _ { 1 }$ with respect to $C _ { f }$ are positive for all ranges of $k ,$ , indicating that a higher $C _ { f }$ leads to a smaller region where the pure SaaS is preferred. That is, the higher the unfit cost, the less attractive the pure SaaS model is compared to the hybrid model. Moreover, the partial derivatives of $\bar { \theta } _ { 2 }$ with respect to $C _ { m }$ are negative for all ranges of $k ,$ which reveals that the higher the customization cost, the less attractive the pure on-premises is compared to the hybrid model.

Note that the expressions of threshold values of θ given by Proposition 3 are involved with k for each range of k. That is, both θ and k together determine which licensing model is the optimal choice. Table 2 also summarizes the comparative statics of $\bar { \theta } _ { 1 }$ and $\bar { \theta } _ { 2 }$ with respect to k. We observe that for the range where $k \leq \bar { k } _ { 1 }$ 2 the partial derivatives of $\bar { \theta } _ { 1 }$ and $\bar { \theta } _ { 2 }$ with respect to $k$ are both 0. For the range where $k { > } \bar { k } _ { 1 }$ , the partial derivatives of $\bar { \theta } _ { 1 }$ and $\bar { \theta } _ { 2 }$ with respect to $k$ are both positive. This indicates that increased realized quality improvement in the second period will lead to higher threshold values of $\theta$ where the hybrid model degenerates to the SaaS or on-premises model. These threshold values, however, do not vary with k when k is small. This implies that the higher k is, the less favorable the SaaS model is.

Table 2. Comparative Statics of $\bar { \theta } _ { 1 }$ and $\bar { \theta } _ { 2 }$ with Respect to $C _ { f } , C _ { m }$ and k

<table><tr><td>Comparative statics</td><td> $\frac{\partial\bar{\theta}_{1}}{\partial C_{f}}$ </td><td> $\frac{\partial\bar{\theta}_{2}}{\partial C_{m}}$ </td><td> $\frac{\partial\bar{\theta}_{1}}{\partial k}$ </td><td> $\frac{\partial\bar{\theta}_{2}}{\partial k}$ </td></tr><tr><td> $k \leq \bar{k}_{1}$ </td><td>+</td><td>-</td><td>0</td><td>0</td></tr><tr><td> $\bar{k}_{1} < k < \bar{k}_{2}$ </td><td>+</td><td>-</td><td>+</td><td>+</td></tr><tr><td> $k \geq \bar{k}_{2}$ </td><td>+</td><td>-</td><td>+</td><td>+</td></tr></table>

## The Impact of Network Effects

In the presence of network effects, the customers’ utility from using the software increases with the total number of users of the software by $\gamma N ,$ where γ is the intensity of network effects and N is the number of users of the software. Both the original version and the upgrade version of software are compatible with each other.

## The Impact of Network Effects on the SaaS Licensing Model

The customers’ estimated two-period utility from subscribing to the software in the presence of network effects equals $U = \nu - P _ { L } - C _ { f } + \nu ( 1 + \theta ) - P _ { L } - C _ { f } + 2 \gamma N$ The customers who choose not to subscribe derive zero utility. The marginal customer type who is indifferent between subscribing to the software and doing without is equal to $\frac { 2 ( P _ { L } + C _ { f } - \gamma N ) } { 2 + \theta }$ . Thus, the total number of subscribers is $\begin{array} { r } { N = \bar { \nu } - \frac { 2 ( P _ { L } + C _ { f } - \gamma N ) } { 2 + \theta } } \end{array}$ . Solving for $N ,$ one has $\begin{array} { r } { N = \frac { ( 2 + \theta ) \bar { \nu } - 2 C _ { f } - 2 P _ { L } } { 2 + \theta - 2 \gamma } } \end{array}$ . The software vendor’s profit equals $\begin{array} { r } { \pi = 2 \bar { P } _ { L } \cdot \frac { ( 2 + \theta ) \bar { \nu } - 2 C _ { f } - 2 P _ { L } } { 2 + \theta - 2 \gamma } - C _ { u } } \end{array}$ . The software vendor’s optimal subscription fee and profit are thus given in Lemma 2.

Lemma 2: When the software vendor adopts the SaaS licensing model in the presence of network effects, it charges the subscription fee $\begin{array} { r } { P _ { I } { ^ { * } _ { \mathrm { = } } } \breve { \frac { ( 2 + \theta ) \bar { \nu } - 2 C _ { f } } { A } } } \end{array}$ and $\begin{array} { r } { \pi ^ { * } = \frac { \hat { \nu } ( 2 + \theta ) \left( 4 \hat { C } _ { f } - \hat { \nu } ( 2 + \theta ) \right) + 4 \hat { C } _ { u } ( 2 - 2 \hat { \nu } + \theta ) - 4 { C _ { f } } ^ { 2 } } { 8 \gamma - 4 ( 2 + \theta ) } } \end{array}$ 4 achieves an optimal profit of

Comparing Lemmas 1 and 2, we find that the optimal subscription fee remains the same with or without network effects. However, the total number of subscribers $\frac { ( 2 + \theta ) \bar { \nu } - 2 C _ { f } - 2 P _ { L } } { 2 + \theta - 2 \gamma }$ increases in $\gamma ,$ indicating that the network effects benefit the vendor by enlarging the demand rather than enabling the vendor to charge a higher subscription fee.

## The Impact of Network Effects on the On-Premises Licensing Model

Following the analyses in the absence of network effects, there are two scenarios to consider under the on-premises licensing model.

In scenario 1, there are three possible options for customers to consider at the beginning of the first period. Customers’ estimated two-period utility of strategy II equals 0. The estimated two-period utility of strategy BH is given by $\nu - P _ { S 1 } - C _ { m } + \nu + 2 \gamma N$ , where N denotes the total number of customers who purchase in the first period and γ stands for network effects intensity, as before. The estimated two-period utility from adopting strategy BU equals $\nu - P _ { S 1 } - C _ { m } + \nu ( 1 + \theta ) - P _ { U } - C _ { u } + 2 \gamma N$ . The marginal customer type who is indifferent between strategies BH and II is described by $\frac { P _ { S 1 } + C _ { m } - 2 \gamma N } { \gamma }$ . The marginal customer type who is indifferent between BH and BU is $\frac { P _ { U } + ^ {  } C _ { u } } { \theta }$ . The first period demand thus equals $\begin{array} { r } { \bar { \nu } - \frac { P _ { S 1 } + C _ { m } - 2 \gamma N } { 2 } } \end{array}$ . By $\begin{array} { r } { \bar { \nu } - \frac { P _ { S 1 } + C _ { m } - 2 \gamma N } { 2 } = N , } \end{array}$ , we obtain $\begin{array} { r } { N = \frac { 2 \bar { \nu } - P _ { S 1 } - C _ { m } } { 2 ( 1 - \gamma ) } } \end{array}$

At the beginning of the second period, customers will receive utility $\nu + \gamma N$ if they choose to hold the old version in the second period. Customers who choose to upgrade will receive utility $\nu ( 1 + k ) - P _ { U } - C _ { u } + \gamma N$ . Thus, the number of customers who choose to upgrade in the second period equals $\bar { \nu } - \frac { P _ { U } + C _ { u } } { k }$ . Therefore, the software vendor’s optimization problem is formulated as follows:

$$
\begin{array}{l} \max _ {P _ {S 1}, P _ {S 2}, P _ {U}} \pi = P _ {S 1} \cdot \frac {2 \bar {\nu} - P _ {S 1} - C _ {m}}{2 (1 - \gamma)} + P _ {U} \cdot (\bar {\nu} - \frac {P _ {U} + C _ {u}}{k}) \\ s. t. \frac {P _ {S 1} + C _ {m} - 2 \gamma \bar {\nu}}{2 (1 - \gamma)} \leq \frac {P _ {U} + C _ {u}}{\theta} \\ \frac {P _ {S 1} + C _ {m} - 2 \gamma \bar {\nu}}{2 (1 - \gamma)} \leq \frac {P _ {U} + C _ {u}}{k} \end{array} .\tag{16}
$$

In scenario 2, customers have two options to consider: II and BU. Customers’ estimated two-period utility of BU equals $\nu - P _ { S 1 } - C _ { m } + \nu ( 1 + \theta ) - P _ { U } - C _ { u } + 2 \gamma N$ , where N equals the number of customers who purchased the software in the first period. The estimated two-period utility of II equals 0. Thus, the marginal customer type who is indifferent between BU and II is represented by $\frac { \stackrel { \ y ^ { \prime } } { P _ { S 1 } } + \stackrel { \ l } { P _ { U } } + C _ { m } + \stackrel { \smile } { C _ { u } } - 2 \gamma N } { 2 + \theta }$

In the second period, if customers choose to stick to the old version, they will receive the utility of $\nu + \gamma N$ . Customers who choose to upgrade receive the utility of $\nu ( 1 + k ) - P _ { U } - C _ { u } + \gamma N$ . Thus the number of customers who choose to upgrade equals $\bar { \nu } - \frac { P _ { U } + C _ { u } } { k }$ By $\begin{array} { r } { \bar { \nu } - \frac { P _ { S 1 } + P _ { U } + C _ { m } + C _ { u } - 2 \gamma N } { 2 + \theta } = N , } \end{array}$ we obtain $\begin{array} { r } { N = \frac { ( 2 + \theta ) \bar { \nu } - P _ { S 1 } - P _ { U } - C _ { m } - C _ { u } } { 2 + \theta - 2 \gamma } } \end{array}$ . The software vendor’s optimization problem of adopting on-premises licensing model with network effects is thus specified as follows:

$$
\begin{array}{l} \max _ {P _ {S 1}, P _ {S 2}, P _ {U}} \pi = P _ {S 1} \cdot \left(\frac {\bar {v} (2 + \theta) - P _ {S 1} - P _ {U} - C _ {m} - C _ {u}}{2 (1 - \gamma) + \theta}\right) + P _ {U} \cdot (\bar {v} - \frac {P _ {U} + C _ {u}}{k}) \\ s. t. \frac {P _ {U} + C _ {u}}{k} \geq \frac {P _ {S 1} + P _ {U} + C _ {m} + C _ {u} - 2 \gamma \bar {v}}{2 (1 - \gamma) + \theta} \\ \frac {(P _ {S 1} + C _ {m}) (2 + \theta) + 2 \gamma (C _ {u} + P _ {U} - \bar {v} (2 + \theta))}{4 (1 - \gamma) + 2 \theta} > \frac {P _ {U} + C _ {u}}{\theta} \end{array} .\tag{17}
$$

We find that the above optimization problem is analytically intractable, and analytical solutions for the on-premises licensing model with network effects are not available. As we will see in the next section, the hybrid licensing model with network effects is as complicated as the on-premises model and is not amenable to analytical solutions. We thus resort to numerical analyses to obtain managerial insights on the impact of network effects on the comparison of three licensing models.

## The Impact of Network Effects on the Hybrid Model

Recall from the analysis of the hybrid model in the absence of network effects, at the beginning of the first period, customers have three options to consider: II, BH, and LL. Customers’ estimated two-period utility of strategy II equals 0. The estimated two-period utility of strategy BH is given by $\nu - P _ { S 1 } - C _ { m } + \nu + 2 \gamma N$ , and the estimated two-period utility from adopting strategy LL equals $\nu - P _ { L } - C _ { f } + \nu ( 1 + \theta ) - P _ { L } - C _ { f } + 2 \gamma N$ , where $\gamma$ represents the network effects intensity and N denotes the total number of customers who adopt the software including those who purchase and those who subscribe to the software in the first period. The marginal customer type who is indifferent between strategies BH and II is described by $\frac { P _ { S 1 } + C _ { m } - 2 \gamma N } { \Upsilon }$ . The marginal customer type who is indifferent between BH and $\begin{array} { r } { L L \mathrm { ~ i s ~ } \frac { 2 P _ { L } + 2 C _ { f } - P _ { s 1 } - C _ { m } } { \theta } } \end{array}$ . The total number of customers who adopt the software in the first period thus equals $\begin{array} { r } { \bar { \nu } - \frac { P _ { S 1 } + C _ { m } - 2 \gamma N } { 2 } } \end{array}$ . Invoking the rational expectation equilibrium, we let $\begin{array} { r } { \bar { \nu } - \frac { \bar { P _ { S 1 } } + \bar { C _ { m } } - 2 \gamma N } { 2 } = N } \end{array}$ and obtain $\begin{array} { r } { N = \frac { 2 \bar { \nu } - P _ { S 1 } - C _ { m } } { 2 ( 1 - \gamma ) } } \end{array}$ . That is, the total number of customers who choose the on-premises and SaaS models in the first period equals $\frac { 2 \bar { \nu } - P _ { S 1 } - C _ { m } } { 2 ( 1 - \gamma ) }$ . The marginal customer type $\frac { P _ { S 1 } + C _ { m } - 2 \gamma N } { 2 }$ thus can be written as $\frac { P _ { S 1 } + C _ { m } - 2 \gamma \bar { \nu } } { 2 ( 1 - \gamma ) }$

At the beginning of the second period, the customers who purchase the software in the first period will receive utility $\nu + \gamma N$ if they choose to hold on to the old version in the second period. The customers who choose to upgrade will receive utility $\nu ( 1 + k ) - P _ { U } - C _ { u } + \gamma N$ . It follows that the number of customers who opt to upgrade in the second period equals $\begin{array} { r } { \frac { 2 P _ { L } + 2 C _ { f } - P _ { s 1 } - C _ { m } } { \theta } - \frac { P _ { U } + C _ { u } } { k } } \end{array}$ . Therefore, the software vendor’s optimization problem of adopting the hybrid licensing model in the presence of network effects is formulated as follows:

$$
\begin{array}{l} \max _ {P _ {S 1}, P _ {S 2}, P _ {U}, P _ {L}} \pi = P _ {S 1} \cdot \left[ \frac {2 P _ {L} + 2 C _ {f} - P _ {s 1} - C _ {m}}{\theta} - \frac {P _ {S 1} + C _ {m} - 2 \gamma \bar {\nu}}{2 (1 - \gamma)} \right] \\ + P _ {U} \cdot \left[ \frac {2 P _ {L} + 2 C _ {f} - P _ {s 1} - C _ {m}}{\theta} - \frac {P _ {U} + C _ {u}}{k} \right] + 2 P _ {L} \cdot \left[ \bar {\nu} - \frac {2 P _ {L} + 2 C _ {f} - P _ {s 1} - C _ {m}}{\theta} \right] \\ s. t. \frac {P _ {U} + C _ {u}}{k} \geq \frac {P _ {S 1} + C _ {m} - 2 \gamma \bar {\nu}}{2 (1 - \gamma)} \\ \frac {2 P _ {L} + 2 C _ {f} - P _ {s 1} - C _ {m}}{\theta} \geq \frac {P _ {U} + C _ {u}}{k} \end{array}\tag{18}
$$

Again, the constraints ensure that the number of customers who upgrade is nonnegative and does not exceed the number of customers who purchase in the first period. We note that the hybrid licensing model in the presence of network effects unfortunately is too complex to have analytical solutions.

## Comparison of the Three Licensing Models in the Presence of Network Effects

In this section, we explore the impact of customers’ estimation of the quality improvement of the upgrade version and network effects on the enterprise software vendor’s optimal decision of licensing model. As both the SaaS and the hybrid models in the presence of network effects are analytically intractable, we resort to numerical analyses to derive managerial insights as to which licensing model is the best under what condition.

We have run extensive numerical experiments and report the two most representative results in Figures 4 and 5. The baseline parameters of these two figures are as follows: customers’ maximum valuation of the enterprise software v is set at 10, the customization cost is 10 percent of v, the unfit cost is 11 percent of $\bar { \nu } ,$ the upgrade cost is 20 percent of $\bar { \nu } ,$ and the quality improvement of the upgrade version is 25 percent. That is, $\bar { \nu } = 1 0 , C _ { m } = 1 , C _ { f } = 1 . 1 , C _ { u } = 2$ , and $k = 0 . 2 5$ . Both Figures 4 and 5 show the changes of the network effects in the x-axis and the changes of customers’ estimation of the quality improvement of the upgrade version in the y-axis. Both figures clearly depict the regions where the on-premises, SaaS, and hybrid are optimal. The only difference between Figures 4 and 5 is $C _ { u } = 2$ in Figure 4, whereas $C _ { u } = 2 . 5$ in Figure 5.

When the network effects are weak, both Figures 4 and 5 indicate that for a given intensity of network effects, the on-premises licensing model is optimal if customers’ estimation of the software quality improvement in the second period θ is low, the hybrid model outperforms the other two licensing models for θ in the mid range, and SaaS generates the highest profit for high values of θ.

We observe from Figure 4 that the on-premises model is never optimal when strong network effects exist (when the intensity of network effects γ exceeds 0.4 in Figure 4). This indicates that network effects benefit the hybrid and SaaS licensing models more than the on-premises model. The intuition is as follows. When the network effects become stronger, customers’ utility under either the SaaS or the onpremises licensing model will increase. The profits achieved under both licensing models increase too. Under the SaaS model, customers are obliged to subscribe to the services for two periods. (Recall that even without a contract, customers will subscribe to the SaaS services for the second period if they do so in the first period.) Thus, the software vendor can reap the benefits of network effects from the increased demand in both periods. Under the on-premises model, the first period demand increases with the intensity of network effects. However, the number of customers who upgrade in the second period, which equals $\bar { \nu } - \frac { P _ { U } + C _ { u } } { k }$ , is independent of network effects. Therefore, stronger network effects only increase demand in the first period. As a result, the profit achieved under the on-premises model increases at a lower rate than that under the SaaS licensing models (including the hybrid and SaaS model).

In Figure 4, when the enterprise software exhibits strong network effects, SaaS is the optimal licensing model if customers’ estimation of the quality improvement of the upgraded version θ is high, while the hybrid model performs best if the θ is low. This result comes from the multitenancy feature of the SaaS licensing model since customers believe they will reap more benefits from the economy of scale of the upgraded version in the second period, which makes the SaaS model more attractive to customers. This phenomenon will become more pronounced when the upgrade cost $C _ { u }$ is increased 25 percent from $C _ { u } = 2 . 0$ in Figure 4 to $C _ { u } = 2 . 5$ in Figure 5, which shows that the SaaS model dominates the other two licensing models as soon as the intensity of network effects γ exceeds 0.25.

As indicated by Table 2, the realized second period software quality improvement k will also impact the threshold values of θ where the hybrid model degenerates to the SaaS or on-premises model. Figure 6 explores the combined influence of k and θ on the software vendor’s optimal choice of licensing model in the presence of network effects where the parameter values are $\bar { \nu } = 1 0 , \ C _ { m } = 1 , \ C _ { f } = 1 . 1$ $C _ { u } = 2$ , and $\gamma = 0 . 1$

![](/api/attachments/ARJZHTJJ/fulltext/images/c4cc2108bcc3ee5f1c8c6d002bb274bada8aaf298d3c6d3869c9d3df320c313e.jpg)  
Figure 4. The Impact of Network Effects on the Comparison of the Three Models $( C _ { u } = 2 )$

![](/api/attachments/ARJZHTJJ/fulltext/images/2cf4d0e99bbacc9b700af60f9b1f7bd3921e7b0b8784216e1d3a31f9d4494a53.jpg)  
Figure 5. The Impact of Network Effects on the Comparison of the Three Models $( C _ { u } = 2 . 5 )$

We observe from Figure 6 that the region where the SaaS model dominates shrinks, while the region where the on-premises model dominates expands as k increases. This observation is attributed to the fact that k does not impact the demand under the SaaS model whereas it is a key factor inducing users to upgrade under the on-premises model. Therefore, the on-premises model is preferred when k is large.

## Implications and Discussion

As the enterprise software vendor contemplates which licensing model—on-premises, SaaS, or hybrid—works best, our research shows that the optimal choice of licensing models is determined by several key factors, including customers’ estimation of future software quality improvement, realized future software quality improvement, network effects, customization cost, unfit cost, and upgrade cost. If the network effects are weak, the enterprise software vendor should choose the onpremises model when customers have a low estimation of software quality improvement in the upgrade version. The hybrid model should be implemented if this estimation is in the mid range, whereas the SaaS model generates the highest profit when customers believe that the upgrade version will have a significant improvement in software quality. As the network effects become stronger, the on-premises model will be dominated by the other two licensing models and is never optimal. In the event of a high upgrade cost and strong network effects, SaaS becomes the best licensing model due to its multitenancy nature. Finally, the comparative statics results of our research show that the higher the unfit cost, the less attractive the pure SaaS model is compared to the hybrid model, and that the higher the customization cost, the less attractive the pure on-premises is compared to the hybrid model. We discuss the managerial implications of these key factors affecting the enterprise software vendor’s optimal choice of licensing model.

## Implications of Network Effects

In general, enterprise software can be categorized by its business functions into several different types of products such as business intelligence, business process management, content management system, customer relationship management, enterprise resource planning (ERP), and supply chain management.<sup>5</sup> Different types of enterprise software result in different degrees of network effects. For example, ERP and supply chain software types exhibit stronger network effects than business intelligence software types since companies employing the same ERP or supply chain management enterprise software benefit from the seamless exchange of business data to achieve tighter business integration among partners in the supply chain. One would expect companies not to share the results of their use of business intelligence software with others. Our research indicates that we should expect to observe more and more enterprise software with strong network effects to move toward the SaaS licensing model. IDG forecasts that the market share of SaaS in ERP market will increase from 23.5 percent in 2013 to 38.5 percent in 2018 corroborate the implications of our findings [8].

![](/api/attachments/ARJZHTJJ/fulltext/images/bae82bfd4c6c8000399f4cd80ce54a1536f9c3b6334ea8bd8aa0f65022183a1c.jpg)  
Figure 6. The Combined Impacts of k and θ in the Presence of Network Effects (γ 0:1)

## Implications of Customization Cost

Enterprise software is difficult to customize since it is inherently complex and feature rich. The plug-in components architecture is an emerging approach to increase the customizability of enterprise software, a prominent example of which is the OSGi Alliance, formerly Open Service Gateway Initiative.<sup>6</sup> OSGi defines an open standard and provides mechanisms aimed at a resulting enterprise application that is easier to customize for customers. Our research indicates that the increasing customizability of enterprise software developed through plug-in components architecture or similar standards will thus reduce the customization cost and favor the onpremises or hybrid licensing model.

The enterprise software vendor has, however, the option to increase the customizability of its enterprise software delivered through the SaaS model. One such example is the customizable CRM software offered by Salesboom.com.<sup>7</sup> There are dual effects of the increasing customizability of the SaaS version of enterprise software. On the one hand, it reduces the unfit cost of SaaS customers. On the other hand, the reduced unfit cost is achieved through an additional customization cost incurred by the customers. Whether the SaaS model is the preferred licensing model is thus more nuanced and depends on the net effect of both costs.

## Implications of Customers’ Estimation of the Upgrade Version Quality

An important finding of this research is that for any given true quality of the upgrade version in the second period, the SaaS licensing model is preferred when customers have a relatively high estimation of upgrade version quality in the second period θ, and the on-premises model should be selected when θ is low, whereas the hybrid model works best in between. However, among the several key factors affecting the enterprise software vendor’s optimal choice of licensing model, the only factor unknown to the vendor is customers’ estimation of the upgrade version in the second period θ. It is thus imperative for the vendor to have an accurate read of θ in order to make an informed decision. Hendriks et al. [14] propose a method to identify and subsequently measure the most important software quality characteristics following the ISO-9126 standard. The enterprise software vendor can adapt the structured questionnaire developed in Hendriks et al. [14] and obtain the value of customers’ estimation of the upgrade version quality accordingly.

## Impacts of the Enterprise Software Vendor’s Reputation

The origin of enterprise software dates back to the era of manufacturing resource planning (MRP II), which evolved into today’s enterprise resource planning (ERP) software. SAP, as the earliest ERP software, has had many upgrades since its inception 40 years ago. Although the model in this research is a stylized two-period model, it can be applied successively to subsequent upgrades. For example, for a three-period model involving two upgrades: the first upgrade in the second period becomes the current version, and the second upgrade becomes the upgrade version in the third period, and so forth. Intuitively, if the enterprise software vendor underdelivers in terms of the realized upgrade quality being lower than the customers’ estimate, customers will lower their estimation for the quality of the next upgrade version, which will favor the vendor’s choice of the on-premises licensing model. However, such a reputation will hinder the enterprise software vendor’s initiative to offer an SaaS or a hybrid licensing model when the market trend may move toward the SaaS delivery model.

A popular industry practice we observe in reality suggests that enterprise software vendors usually announce a roadmap for future upgrades giving detailed specifics, which has the effect of aligning customers’ estimate of future upgrade quality with the true upgrade version quality. Our research indicates that the vendor should opt for the hybrid model when this is the case. This implies that we should observe more vendors adopting the hybrid licensing model in the future.

## Conclusion

Software as a service (SaaS) has become an increasingly popular software licensing model since the term was first coined in February 2001 by the Software & Information Industry Association’s (SIIA) eBusiness Division, although most software is still offered through the traditional on-premises model. The objective of this research is to examine the enterprise software vendor’s decision among the SaaS, onpremises, and hybrid (a combination of SaaS and on-premises) licensing models by considering the unique features of each model.

Our results indicate that both customers’ estimation of future software quality improvement and network effects play critical roles in the software vendor’s choice of optimal licensing models. When the network effects are weak, the enterprise software vendor should choose the on-premises model when customers have a low estimation of software quality improvement in the upgrade version. The hybrid model should be implemented if this estimation is in the mid range, whereas the SaaS model generates the highest profit when customers believe that the upgrade version will have a significant improvement in software quality. As the network effects become stronger, the on-premises model will be dominated by the other two licensing models and is never optimal. In the event of a high upgrade cost and strong network effects, SaaS becomes the best licensing model due to its multitenancy nature—that is, economy of scale in upgrading to the newer version.

Our research is not without limitations. One limitation of this research is that the product qualities of the current and upgrade versions are exogenously given. A potentially interesting extension is to treat software quality as part of the product development decision, and explore the software vendor’s incentive to invest in improving quality under different licensing models. Another limitation is the assumption of the second period selling price as being no less than that of the first period, although it is an assumption that reflects reality. We conjecture that an extension without this assumption may not yield additional insights. Both extensions are analytically intractable, and computational analyses will be needed to obtain managerial insights.

## NOTES

1. In this study, the firm producing the enterprise software is referred to as the enterprise software vendor or the software vendor for short, and the institutions that are the clients of the enterprise software vendor are referred to as the customers.

2. See www.salesforce.com/crm/editions-pricing.jsp.

3. See http://blog.akquinet.de/2014/10/08/agile-roadmaps-in-software-development/

5. See https://en.wikipedia.org/wiki/Enterprise\_software#Types.

6. See https://www.osgi.org/

7. See www.salesboom.com/products/tools-customization.html.

## Funding

This work is supported by the National Natural Science Foundation of China (71402134, 71572138, 71571140, 71473191, and 91546119) and the Ministry of Science and Technology of Taiwan (104-2410-H-110-031).

## Supplemental File

Supplemental data for this article can be found on the publisher’s website at 10. 1080/07421222.2017.1297636

## REFERENCES

1. Balasubramanian, S.; Bhattacharya, S.; and Krishnan, V. Pricing information goods: A strategic analysis of the selling and pay-per-use mechanisms. UNC Kenan-Flagler Research Paper no. 2013-10, 2013.

2. Bhaskaran, W.R., and Gillbert, S.M. Selling and leasing stratgies for durable goods with complementary products. Management Science, 51, 8 (2005), 1278–1290.

3. Boone, D.S.; Lemon, K.N.; and Staelin, R. The impact of firm introductory strategies on consumers’ perceptions of future product introductions and purchase decisions. Journal of Product Innovation Management, 18 (2001), 96–109.

4. Born, C. What makes a good CRM parkage? 2003. Available at: http://www.computer world.com/article/2570293/crm/what-makes-a-good-crm-package-.html

5. Cheng, H.K., and Liu, Y. Optimal software free trial strategy: The impact of network externalities and consumer uncertainty. Information Systems Research, 23, 2 (2011), 488–504.

6. Cheng, H.K.; Shengli, L.; and Yipeng, L. Optimal software free trial strategy: Limited version, time-locked, or hybrid? Production and Operations Management, 24, 3 (2015), 504– 517.

7. Chien, H.K., and Chu, C.Y.C. Sale or lease? Durable-goods monopoly with network effects. Marketing Science, 27, 6 (2008), 1012–1019.

8. Columbus, L. IDC predicts SaaS enterprise applications will be a \$50.8b market by 2018. 2014. Available at: HYPERLINK “https://www.forbes.com/sites/louiscolumbus/2014/ 12/20/idc-predicts-saas-enterprise-applications-will-be-a-50-8b-market-by-2018/ ”\l“204e7f5922a8” https://www.forbes.com/sites/louiscolumbus/2014/12/20/idc-predicts-saasenterprise-applications-will-be-a-50-8b-market-by-2018/#204e7f5922a8

9. Demirkan, H.; Cheng, H.K.; and Bandyopadhyay, S. Coordination strategies in an SaaS supply chain. Journal of Management Information Systems, 26, 4 (2010), 119–143.

10. Desai, P., and Purohit, D. Competition in durable goods market: The strategic consequences of leasing and selling. Marketing Science, 18, 1 (1999), 42–58.

11. Desai, P., and Purohit, D. Leasing and selling: Optimal marketing strategies for a durable goods firm. Management Science, 44, 11 (1998), 19–34.

12. Dillon, T.; Wu, C.; and Chang, E. Cloud computing: Issues and challenges. Paper presented at the 24th IEEE International Conference on Advanced Information Networking and Applications, Perth, Australia, April 20–23, 2010.

13. Fan, M; Kumar, S.; and Whinston, A. B. Short-term and long-term competition between providers of shrink-wrap software and software as a service. European Journal of Operation Research, 196 (2009), 661–671.

14. Hendriks, R.; van Veenendaal, E.; and van Vonderen, R. Measuring software product quality. Software Quality Professional, 5, 1 (2002), 6–13.

15. Ma, D., and Kauffman, R.J. Competition between software as a service vendors. IEEE Transactions on Engineering Management, 61, 4 (2014), 717–729.

16. Ma, D., and Seidmann, A. Analyzing software as a service with per-transaction charges. Information Systems Research, 26, 2 (2015), 360–378.

17. Marston, S.; Li, Z.; Bandyopadhyay, S.; Zhang, J.; and Ghalsashi, A. Cloud computing: The business perspective. Decision Support Systems, 51 (2011), 176–189.

18. Niculescu, M.F., and Wu, D.J. Economics of free under perpetual licensing: Implications for the software industry. Information Systems Research, 25, 1 (2014), 173–199.

19. Postmus, D.; Wijngaard, J.; and Wortmann, H. An economic model to compare the profitability of pay-per-use and fixed-ff licensing. Information and Software Technology, 51, 3 (2009), 581–588.

20. Prasad, A.; Stecke, K.E.; and Zhao, X. Advance selling by a newsvendor retailer. Production and Operations Management, 20, 1 (2011), 129–142.

21. Richardson, B. Beware upgrading enterprise software: Total cost can be many times the license fee, 2005. Available at: http://www.computerweekly.com/opinion/Beware-upgradingenterprise-software-total-cost-can-be-many-times-the-licence-fee

22. Software & Information Industry Association. Software as A service: Strategic backgrounder. 2001.

23. Susarla, A.; Barua, A.; and Whinston, A.B. A transaction cost perspective of the “Software as a Service” business model. Journal of Management Information Systems, 26, 2 (2009), 205–240.

24. Tang, Q.; Gu, B.; and Whinston, A.B. Content contribution for revenue sharing and reputation in social media: A dynamic structural model. Journal of Management Information Systems, 29, 2 (2012), 41–76.
