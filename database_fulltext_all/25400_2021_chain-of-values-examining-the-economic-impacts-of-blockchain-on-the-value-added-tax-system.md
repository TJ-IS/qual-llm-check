---
otero_id: 25400
otero_key: "CAWDPKXR"
title: "Chain of Values: Examining the Economic Impacts of Blockchain on the Value-Added Tax System"
authors: "Soohyun Cho; Kyungha (Kari) Lee; Arion Cheong; Won Gyun No; Miklos A. Vasarhelyi"
year: "2021"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2021.1912912"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Chain of Values: Examining the Economic Impacts of Blockchain on the Value-Added Tax System

Soohyun Cho, Kyungha (Kari) Lee, Arion Cheong, Won Gyun No & Miklos A. Vasarhelyi

To cite this article: Soohyun Cho, Kyungha (Kari) Lee, Arion Cheong, Won Gyun No & Miklos A. Vasarhelyi (2021) Chain of Values: Examining the Economic Impacts of Blockchain on the Value-Added Tax System, Journal of Management Information Systems, 38:2, 288-313, DOI: 10.1080/07421222.2021.1912912

To link to this article: https://doi.org/10.1080/07421222.2021.1912912

![](/api/attachments/CAWDPKXR/fulltext/images/4935cb0cbfea648dc7f675362646e48117c7c899d81faa2b825b2eabc28a085e.jpg)

View supplementary material

![](/api/attachments/CAWDPKXR/fulltext/images/2f4a071b242e19f746e52b1aabaa0a73b645d812503ab8cc87cc22e08d73a144.jpg)

Published online: 06 Aug 2021.

![](/api/attachments/CAWDPKXR/fulltext/images/578ab24623447da72463be3799e0fcfe79dee5c5cfe7c8d1e45c854bba5a2647.jpg)

Submit your article to this journal

![](/api/attachments/CAWDPKXR/fulltext/images/1ea2833e36b042d1168bc5502417a6619fe05c6272ae01e18e704c528dda68ac.jpg)

View related articles

![](/api/attachments/CAWDPKXR/fulltext/images/8ae4eb8ba9d00f31b9f6de96802c35994d14cf73cd658429eacad5a36c972c22.jpg)

View Crossmark data

Check for updates

# Chain of Values: Examining the Economic Impacts of Blockchain on the Value-Added Tax System

Soohyun Cho<sup>a</sup>, Kyungha (Kari) Lee<sup>a</sup>, Arion Cheong<sup>b</sup>, Won Gyun No<sup>a</sup>, and Miklos A. Vasarhelyi<sup>a</sup>

<sup>a</sup>Department of Accounting and Information Systems, Rutgers Business School, Rutgers, The State University of New Jersey, Newark, NJ, USA; <sup>b</sup>Department of Accounting, College of Business and Economics, California State University Fullerton, Fullerton, CA, USA

## ABSTRACT

Blockchain technology can benefit inter-organizational activities by improving data integrity, increasing transaction transparency, and decreasing transaction costs. In this paper, we discuss the strategic and economic value of this technology by applying it to the valueadded tax (VAT) reporting system, focusing on blockchain’s characteristic traceability. By efectively increasing financial transparency, the application of blockchain to the VAT system can prevent VAT-related fraud (e.g., underreported VAT) that can arise due to the information asymmetry that exists at diferent stages of the supply chain. We develop a game theoretical model that involves a retailer and two vendors in order to study the players’ strategic decisions regarding blockchain adoption and to examine the efects on social welfare. We also show how the decision to adopt blockchain depends on considerations such as adoption costs, the vendors’ VAT reporting behavior, the retailer’s profit margins, and inter-vendor competition. Furthermore, we find that under certain conditions, policymakers can increase social welfare by providing subsidies to encourage blockchain adoption.

## KEYWORDS

Blockchain; value-added tax; VAT; game theoretical model; strategic financial transparency; social welfare; blockchain impacts

## Introduction

Blockchain has the potential to become a powerful disruptive force.

89. Ryo Takahashi, McKinsey & Company (2017)

Tax professionals may need to embrace the advent of blockchain and the potential uses of distributed ledger technology beyond cryptocurrency.

44. David Jarczyk, KPMG (2018)

Recent advancements in information technology can optimize inter-organizational business processes by bolstering data integrity, which can ultimately drive an increase in business profits [9, 18, 31, 32, 74, 79]. In particular, blockchain technology strengthens data integrity by providing a decentralized system for facilitating, securing, and verifying transactions, which in turn sharpens the ability to detect and correct errors and to store transactions in a comprehensive, accurate, and up-to-date manner [62, 87]. In light of blockchain’s salutary efects on data integrity and its capacity to empower inter-organizational activities, a growing number of large public firms and businesses have announced their adoption of the technology [101]. However, blockchain adoption has also raised concerns due to the additional costs and technical complexities of its implementation [9], with some skeptics flatly declining to adopt the technology for their businesses [14].

Information technologies have also enabled the rise of a digital economy where people can buy or sell a wide range of products and services across multiple jurisdictions through online marketplaces [34, 46, 53, 54, 67]. One prominent concern that has arisen alongside this new economy centers on paying and collecting value-added tax (VAT) [12, 53, 72]. With a significant amount of global sales transactions occurring through online marketplaces, tax authorities face increasingly complex challenges to collecting VAT from multijurisdictional sellers and buyers. In particular, considerable growth in transactions of lowvalue goods, which were previously exempt from VAT due to high administrative costs, has fueled the concerns of tax authorities seeking to implement a new compliance mechanism for processing VAT. Digital goods and services sold through online platforms (e.g., streaming games from Google Stadia and Apple Arcade) generate similar concerns due to the participation of game suppliers and vendors from multinational entities [6, 11]. Because of variances in data formats and regulations across jurisdictions, there is a higher risk of VAT underreporting (intentional or unintentional) in transactions involving such services than in transactions of traditional goods [3, 12, 20, 49, 72].

Blockchain can address such problems in the VAT reporting system and reduce VAT underreporting by providing trustworthy and reliable data cultivated by its systemic characteristics, persistency, validity, and auditability [5, 28, 40, 52, 70, 77, 80, 93, 101]. More specifically, by storing transactions in distributed ledgers and enabling participants in the blockchain to secure immutable transaction trails, blockchain technology prevents participants from manipulating transactions and engaging in detrimental rent-seeking (which would extract uncompensated value from the other parties in the blockchain). Despite blockchain’s benefits of enhanced information integrity, however, the cost of its adoption has incited skepticism and resistance from some business managers. Such apprehension seems at odds with prevailing opinions concerning its implementation and economic value. According to a survey conducted by Deloitte, 80% of 1,386 senior executives in various countries considered blockchain to be a critical or essential technology in their organizations. At the same time, most survey respondents expressed the desire to see measurable and verifiable returns on blockchain investment [24, 55, 57]. These survey results reveal the need for sound analyses of the economic value of blockchain technology. Such studies can reduce barriers to blockchain adoption by assuaging concerns about uncertain returns on investment and inadequate funding [17, 32, 45, 82].

Considering the benefits and concerns arising from blockchain adoption [24, 30, 35, 47, 61, 87, 92], we study the economic impacts and strategic value of blockchain technology by applying its trust mechanisms to the VAT imposition and crediting processes for interorganizational activities between distinct and separate entities. For example, the parties that are involved in the credit-invoice method VAT process are typically connected by incomplete contracting models. One or more of the parties involved in such models may have an incentive to engage in rent-seeking behavior, in which a party increases its share of existing wealth (e.g., currently extant revenue or profit) by manipulating its contract relations while failing to create new wealth [42, 60, 63, 69, 90, 91]. Under the VAT reporting system, blockchain can serve to prevent potential fraud and reduce the cost of fraud-related uncertainty. Consequently, the primary goal of our paper is to analyze blockchain technology’s economic impacts by converting blockchain’s potential advantages (e.g., preventive controls for rent-seeking behavior and increased transaction transparency) into monetary values while safeguarding participants from potential fraud.

To achieve the abovementioned research goal, we formulate our questions and analysis regarding blockchain’s economic value vis-à-vis VAT processes by considering real-world economic issues involving the credit-invoice method VAT. In particular, we examine the economic impacts of blockchain adoption on the entities involved as well as the strategies such parties might employ to secure profits and welfare.

Our model considers 1) vendors’ rent-seeking behavior, which aims to maximize their profits when reporting VAT under a credit-invoice method VAT regime, and 2) the retailer’s strategies for blockchain adoption in the context of preventing vendors’ rentseeking behavior. We develop a game theoretical model that includes one retailer (buyer) and two competing vendors (sellers) that supply similar items to the retailer. The vendors may engage in VAT underreporting to maximize their profits, thereby reducing the retailer’s profit. To prevent this underreporting behavior, the retailer can propose adopting a private blockchain, which would be costly for both the retailer and the vendors that might enter it. We analyze the retailer’s strategies to adopt blockchain for its business processes and vendors’ strategies as they seek to maximize their profits. This model is based on various real-world examples of blockchain adoption. Walmart, for example, recently announced the adoption of the technology for its online marketplace supply chain and has encouraged its vendors to enter the blockchain [1, 27, 64, 73, 98, 99].<sup>1</sup> Similarly, IBM has introduced a platform that can be applied to procurement systems and used for supplier validation while partnering with Fortune 500 companies [66].

We find that when vendors’ products are more similar or when the retailer’s profit margin is greater, it becomes more costly for the retailer to incentivize vendors to enter the blockchain. Accordingly, the retailer is willing to tolerate higher blockchain adoption costs when vendors’ products are more diferentiated, the retailer’s profit margin is smaller, or when vendors are expected to engage in significant VAT underreporting behavior. We also study how the retailer and vendors respond diferently when the retailer takes a more assertive approach. If the retailer severs ties with vendors that do not enter the blockchain, the cost to motivate vendors to join the blockchain decreases, and blockchain adoption becomes more likely. Finally, we analyze blockchain adoption’s efects on social welfare, which hinge on the relative cost of investigating and rectifying VAT misreporting versus the cost of adoption. We find that policymakers may prefer to adopt blockchain even when the retailer and vendors may not.

Our study provides a novel economic analysis of blockchain technology adoption and the strategic use of blockchain vis-à-vis VAT imposition and crediting processes. Specifically, since EU countries have begun proposing and implementing VAT on digital goods sold through digital companies (i.e., online platforms), our findings can be used by such business entities to develop strategies aimed at preventing VAT-related fraud. <sup>2</sup> Our research is especially germane to digital companies, which are fully and solely liable for assessing, collecting, and remitting VAT on their online sales. Moreover, our paper shows how some concerns in the realm of IT (e.g., VAT processing in the digital economy) can be addressed through information technology itself (e.g., blockchain). We believe our paper will provide policymakers with insights that will allow them to fight fire with fire, as it were, by leveraging information technology to resolve IT-generated concerns and to bolster strategic plans.

The remainder of this paper proceeds as follows. In the Background and Literature Review section, we introduce our study context, including an overview of blockchain, VAT, and the literature that motivated our research. We then explain our model, analyze it under diferent arrangements between a retailer and two vendors, discuss our results (see the Model section and the Model Analyses section), and extend our analysis to include policy perspectives (see the Additional Analyses and Welfare Implications section). After discussing the implications of our findings (see the Discussion of Our Findings section), we conclude by emphasizing our study’s contributions regarding the economic consequences of new technology adoption and provide possible directions for future research.

## Background and Literature Review

In this section, we review the literature concerning blockchain and valued-added tax in the context of our study.

## Blockchain Technology

Blockchain technology allows users to record transactions in a ledger without a centralized, trusted party. The ledgers are stored in a peer-to-peer distributed server where network participants share the records. The consensus algorithm, meanwhile, ensures that each node (i.e., participant) of the network has a consistent record of all transactions (i.e., immutability). By design, this algorithm enables records to be traceable and ensures their integrity while demonstrating blockchain’s capacity to provide reliable data [101]. In information systems research, studies have already developed a framework for blockchain adoption in consideration of blockchain’s decentralized nature and have examined the organizational benefits and challenges arising from the adoption [87]. Meanwhile, the recent introduction of blockchain-based smart contracts ofers a new methodology to ensure compliance among participants based on predetermined rules and operate without a centralized trusted party [22, 95]. We expand on the results of earlier studies to examine how blockchain adoption can economically afect inter-organizational activities and how individual organizations can benefit from it.

## Value-added Tax (VAT)

To study the impacts of blockchain application, we choose the specific context of VAT collection and payment. Value-added tax (VAT) is a consumption tax imposed on goods or services based on the amount of value-added. VAT is levied for each point in the product’s supply. As of 2018, 166 out of 193 countries had implemented the VAT system commonly used in the European Union [43].<sup>3</sup> The credit-invoice method is the most widely used method to calculate VAT when the tax is imposed on the seller; sellers, in turn, obtain credits for their input VAT.<sup>4</sup> As shown in Figure 1, which portrays an example of the creditinvoice method, the retailer (e.g., the Apple App Store) first reports to the tax authority its tax levied on the full value of its sales. The retailer subsequently receives a credit from the tax authority based on the vendors’ (e.g., App developers) tax reports.

![](/api/attachments/CAWDPKXR/fulltext/images/74540b80a3df2a406c2076f947a9434a3d7855843ae469b1c71679999b87b0d9.jpg)  
Figure 1. Example of VAT impositions to Digital Platform.

When VAT fraud occurs, it typically involves a misreport or missing trader fraud. Additionally, trades between multijurisdictional regions (e.g., the European Union) are more vulnerable to VAT misreporting. In line with the continuous growth of the digital economy, e-commerce transactions significantly increased year-on-year by 14 percent in 2019, reflecting how people are increasingly reliant on it [85]. Online marketplaces in e-commerce platforms have facilitated cross-border transactions of low-value goods between sellers and buyers in diferent jurisdictions [7, 8, 12, 53, 96]. This facilitation has fostered significant growth in the number of transactions, impelling legislative bodies to impose VAT on low-value goods bought and sold in online marketplaces such as Amazon and eBay.<sup>5</sup> Also, online platforms’ digital services (e.g., streaming games on Google Stadia and Apple Arcade) are often developed and used under diferent jurisdictions complicating the process of confirming compliance with applicable VAT regulations [1].<sup>6</sup> These complications underline the need to implement a system that avoids non- or double taxation [12].

Our study examines issues regarding VAT imposition in the digital economy through the lens of emergent information technology (i.e., blockchain). Using a game-theoretic model, we analyze when the adoption of blockchain to the VAT system would benefit vendors and e-marketplaces (i.e., online platforms) that are not exempt from VAT under certain conditions.

## Data Integrity and VAT Fraud Schemes

Our research draws on two streams of literature, namely data integrity and the impact of VAT compliance risk on a company’s performance. The first topic, data integrity, is particularly germane to our paper’s inquiry into the utilization of blockchain as a viable means to determine provenance more accurately. Data integrity refers to the capability to detect and correct errors in a system. Enhanced data integrity can improve decision-making while increasing revenue and reducing costs. Since information technology can facilitate the maintenance and enhancement of data integrity, adopting pertinent IT mechanisms can provide a useful strategy for business processes [9, 74]. In particular, we expect blockchain to help companies realize significant improvements in data integrity with its inherently decentralized structure. This capability to sharpen data integrity is applicable to the processing of taxation data, thereby mitigating VAT compliance risk and improving business processes.

Our study also addresses VAT compliance risk and business performance. “High complexity and dynamism” in the supply chain can introduce risk, including that of financial loss to the firm [23, 33, 36, 39, 41, 86]. Meanwhile, global retailers face multiple threats due to complex cross-border tax environments and supply chains [71, 76]. Such firms can play unwitting victims to missing trader fraud, which can instigate costly legal disputes and damage reputations. Notably, a vendor’s misreporting of VAT can reduce the amount of the retailer’s VAT reimbursement. However, the retailer has limited means to verify the vendor’s integrity due to the information asymmetry between them. Indeed, in some cases, this uncertainty is only resolved when the retailer fails to obtain reimbursement from the tax authority. Evidence shows that online VAT fraud by vendors may have resulted in as much as £33 billion in lost revenue for the UK’s online marketplace retailers over a four-year period.<sup>8</sup>

Accordingly, both the public and private sectors are adopting blockchain to combat VAT fraud. The essence of the blockchain-based VAT system is to enhance transparency (i.e., provenance) for VAT calculation. In 2016, the European Commission commenced building a blockchain-based VAT system that streamlines taxation processes for intra-EU crossborder trade (i.e., a definitive VAT system), with an expected launch date of July 2022 [13, 29]. Similarly, the European private sector has also begun implementing a blockchain-based VAT system as part of a compliance framework. In contrast to the nation-level blockchainbased VAT system, the private sector is limiting the access of participants to the network by adopting private blockchain networks rather than public ones. Our study analyzes the economic factors surrounding the implementation of a private blockchain focusing on its benefit of deterring VAT fraud [75].

## Model

To study blockchain adoption’s economic value in a VAT application setting, we incorporate the retailer’s blockchain adoption decision and its efects on VAT collection into a standard Bertrand competition model. We develop a one-period model with two types of players: a retailer and two competing vendors [58, 68, 100].<sup>9</sup> The vendors supply the retailer with similar products and are one of two types: honest (H) or dishonest (D). The two types have diferent VAT reporting characteristics: H-types honestly report their VAT while D-types knowingly underreport their VAT. While the retailer cannot observe whether a vendor is honest or dishonest, it knows that the probability that the vendor is type H is $\theta \in ( 0 , 1 )$ while the probability that it is type D is ð1   θÞ, where θ is common knowledge. Each vendor knows its own type classification but cannot credibly disclose it.

We incorporate blockchain adoption into the model by focusing on its function of enhancing transparency. We assume that if the retailer adopts the blockchain system, participating vendors cannot underreport VAT due to the enhanced supply chain traceability. Since entering the blockchain is costly to vendors, the retailer may ofer an incentive to join the system by increasing the purchase price for participating vendors [37, 38, 50, 56, 65]. At the same time, the retailer must consider its own blockchain adoption costs [51].

![](/api/attachments/CAWDPKXR/fulltext/images/1fd2e1e1f3317bd2cfaa19c6df03b63d71b468896d66b1627b33de5603aac707.jpg)  
Figure 2. Game sequence.

There are four stages to the game: in Stage 1, the retailer (R) determines whether to adopt the blockchain system. If the retailer decides to adopt, it announces the incentives it will provide to any vendor that enters the blockchain system. In Stage 2, the vendors individually decide whether to enter the blockchain system adopted by the retailer. Both the retailer’s and vendors’ blockchain adoption decisions are publicly observable. In Stage 3, vendors set their prices for providing goods to the retailer, who then sells the goods to consumers after adding a profit margin. Finally, in Stage 4, the retailer and vendors tally their respective profits after paying the VAT, and the game ends. Figure 2 presents the sequence of events related to blockchain adoption and VAT collection. In the following sections, we describe the strategic interactions and respective decision processes of the retailer and vendors in greater detail.

## Retailer’s Problem

The retailer R purchases goods A and B from vendors $\nu _ { A }$ and $\nu _ { B } ,$ respectively, and sells these goods to consumers after adding a profit margin $( \kappa { > } 0 )$ .The retailer’s purchase prices and purchase quantities for the goods are determined by Bertrand competition between the two vendors and are denoted as $\omega _ { i }$ and $q _ { i } , i \in \{ A , B \}$ , respectively. The retailer sells these goods to consumers at retail price $p _ { i } = \omega _ { i } ( 1 + \kappa )$ for $i \in \{ A , B \}$ . We assume that κ is exogenously given and is common knowledge. If the retailer does not adopt blockchain, its profit function is expressed as follows:

$$
\sum_ {i = A, B} \left(p _ {i} - \omega_ {i}\right) q _ {i} - \sigma p _ {i} q _ {i} + \sigma_ {i} \omega_ {i} q _ {i},\tag{1a}
$$

where $\sigma \in ( 0 , 1 )$ is the regulatory VAT rate and $\sigma _ { i } \in [ 0 , \sigma ]$ is the VAT rate that vendor i submits. Without blockchain adoption, $\sigma _ { i } = \sigma$ if vendor i is honest, and $\sigma _ { i } = \sigma \varepsilon$ if vendor i is dishonest, where $ { \varepsilon } \in [ 0 , 1 )$ Þ captures the portion of sales the D-type vendor reports for VAT purposes.<sup>11</sup> As we can see from (Equation 1a), vendors will slash the retailer’s profit if they underreport VAT.

To enhance VAT calculation transparency and deter such underreporting of VAT, the retailer can adopt blockchain for its transactions with vendors. We assume that the retailer is the ultimate arbiter that decides whether to adopt the blockchain at the cost of $c _ { B } > 0$ . For the blockchain to deter vendors’ VAT underreporting behavior, the vendors must also adopt it. Moreover, to encourage vendors to adopt, the retailer may also provide them incentives to join. We model this consideration by having the retailer pay $\Delta \geq 0$ per product in addition to the purchase price $\omega _ { i }$ to any vendor that adopts blockchain. Another way of viewing the incentive payment Δ is to consider it as a way for the retailer to share its profit margin with the vendor.

If the retailer decides to adopt the blockchain system, it informs vendors of its decision and announces the incentive $\Delta .$ . The retailer’s profit function when it adopts blockchain is expressed as follows:

$$
\sum_ {i = A, B} \left[ \left(p _ {i} - \omega_ {i} - 1 _ {i} \Delta\right) q _ {i} - \sigma p _ {i} q _ {i} + \left(\left(1 - 1 _ {i}\right) \sigma_ {i} + 1 _ {i} \sigma\right) \left(\omega_ {i} + 1 _ {i} \Delta\right) q _ {i} \right] - c _ {B},\tag{1b}
$$

where $1 _ { i } = 1$ if vendor $i \in \{ A , B \}$ enters the blockchain, and $1 _ { i } = 0$ if vendor i does not enter the blockchain. While the notation for consumer retail price $\left( { p _ { i } } \right)$ , retailer’s purchase price $\left( \omega _ { i } \right)$ , and purchase quantity $( q _ { i } )$ in (Equation 1b) are the same as in (Equation 1a), these are endogenous variables that are determined by the respective vendors’ problems. Therefore, the resulting $p _ { i } , \omega _ { i } ,$ and $q _ { i }$ in (1a) and (1b) will be diferent since the vendors incentives and constraints are likewise diferent, depending on whether the retailer adopts the blockchain.

When determining its blockchain adoption strategy, R considers the cost of blockchain adoption, the change in the purchase price, and the benefits it would reap from VAT savings, given its conjectures of how vendors will respond to the blockchain adoption decision and incentive $\Delta$

## Vendors’ Problem

Vendors A and B are engaged in a Bertrand competition. They determine the price at which they will supply their products to the retailer $\left( \omega _ { i } \right)$ , anticipating the following demand function:

$$
q _ {i} = \alpha - \beta p _ {i} + \beta t p _ {j}, i, j \in \{A, B \} \text {   and   } i \neq j,
$$

where $t \in ( 0 , 1 )$ represents the degree of substitutability between products A and $B ,$ $\alpha = 1 / ( 1 + t )$ , and $\beta = 1 / ( 1 - t ^ { 2 } ) . ^ { 1 2 }$ We assume that the vendors are symmetric but diferentiated and that this demand function is common knowledge among the players. Here, demand is determined by the price at which the retailer sells the goods to consumers, $\mathbf { \nabla } _ { \mathbf { \ } } p _ { i } ,$ which is ultimately determined by the price at which vendors supply the goods to the retailer, $\omega _ { i } ,$ given κ. Furthermore, as the degree of substitutability between the two products increases, the relative prices between the two products become more important in determining the demand for each product.<sup>13</sup>

Without considering blockchain adoption, vendor i would solve the following problem to maximize its profit:

$$
\operatorname{argmax} _ {\omega_ {i}} \omega_ {i} \left[ \alpha - \beta \omega_ {i} (1 + \kappa) + \beta t \hat {p} _ {j} \right] (1 - \sigma_ {i}),\tag{2}
$$

where $\hat { p } _ { j }$ denotes vendor $i \gamma _ { s }$ conjecture of vendor $j \dag s$ prices, and $\sigma _ { i }$ is vendor i’s VAT submission rate, depending on its type.<sup>14</sup>

If the retailer adopts the blockchain system and vendor i chooses to enter $\mathrm { i t } ,$ its maximization problem becomes

Table 1. Summary of notations.

<table><tr><td>Variable</td><td>Description</td></tr><tr><td> $\{H, D\}$ </td><td>Vendor type: honest (H) or dishonest (D)</td></tr><tr><td> $\theta \in (0, 1)$ </td><td>Ex ante probability that a vendor is type H</td></tr><tr><td>R</td><td>Retailer</td></tr><tr><td> $v_i, i \in \{A, B\}$ </td><td>Vendors A and B</td></tr><tr><td> $\omega_i$ </td><td>The retailer&#x27;s purchase price from vendor i</td></tr><tr><td> $q_i$ </td><td>The retailer&#x27;s purchase quantity from vendor i</td></tr><tr><td> $\kappa >0$ </td><td>Profit margin added by the retailer</td></tr><tr><td> $p_i = \omega_i(1 + \kappa)$ </td><td>Consumer retail price for product i</td></tr><tr><td> $\sigma \in (0, 1)$ </td><td>The regulatory VAT rate</td></tr><tr><td> $\sigma_i \in [0, \sigma]$ </td><td>The VAT rate that vendor i submits</td></tr><tr><td> $\varepsilon \in [0, 1)$ </td><td>The portion of sales the D-type vendor reports for VAT purposes</td></tr><tr><td> $c_B >0$ </td><td>Retailer&#x27;s blockchain adoption cost</td></tr><tr><td> $\Delta \geq 0$ </td><td>Per good incentive payment from the retailer to a vendor for entering the blockchain</td></tr><tr><td> $t \in (0, 1]$ </td><td>The degree of substitutability between products A and B</td></tr><tr><td> $c_b >0$ </td><td>Individual vendor&#x27;s blockchain adoption cost</td></tr><tr><td>Case BB</td><td>Case where both vendor types enter the blockchain</td></tr><tr><td>Case BN</td><td>Case where only H-type vendors enter the blockchain</td></tr><tr><td>Case NN</td><td>Case where neither type of vendor enters the blockchain</td></tr><tr><td> $\pi_i$ </td><td>Expected profit for vendor i</td></tr><tr><td> $\pi_R$ </td><td>Retailer&#x27;s expected profit</td></tr><tr><td>-</td><td>Threshold value</td></tr><tr><td>^</td><td>Conjectured value</td></tr></table>

$$
\operatorname{argmax} _ {\omega_ {i}} (\omega_ {i} + \Delta) \Big [ \alpha - \beta \omega_ {i} (1 + \kappa) + \beta t \hat {p} _ {j} \Big ] (1 - \sigma) - c _ {b}.\tag{3}
$$

While the vendor must incur the blockchain adoption cost $c _ { b } > 0 ,$ it will receive from the retailer an additional Δ per good sold. This incentive allows the vendor to lower its selling price, leading to increased demand for its product. Here, $\sigma _ { i }$ becomes σ once the vendor adopts blockchain since the increased transparency from blockchain adoption enforces truthful VAT reporting. Table 1 provides a list of the notations used in our models.

Each vendor’s decision on whether to enter the blockchain system depends on its VAT reporting strategy (or type), its conjecture regarding the other vendor’s type and strategy, the cost of blockchain adoption, and ultimately how all these factors afect its net profits. We define the equilibrium as follows.

## Definition of Equilibrium

An equilibrium in this model consists of R’s decision to adopt (or not) the blockchain, the blockchain adoption incentive Δ, the vendors’ decision to enter the blockchain system, and their selling prices $\omega _ { i }$ such that:

(1) $R ^ { * } s$ choice of blockchain adoption and $\Delta$ maximizes its expected profit, given its conjectures of the vendors’ strategies.

(2) Vendors’ decisions on pricing and on whether to enter the blockchain system maximize their profit, given R’s strategy and their conjecture of the other vendor’s strategy.

(3) All conjectures coincide with actual choices in equilibrium.

## Model Analyses

We solve the model using backward induction. Vendors set their prices after deciding whether or not to join the blockchain system and observing the other vendor’s adoption decision. Therefore, we first solve for vendors’ price-setting strategies, given blockchain adoption or non-adoption, and then solve for the conditions that would motivate a vendor to enter the blockchain system. Then, we find the retailer’s incentive choices that maximize its expected profit given blockchain adoption or non-adoption. Finally, we solve the retailer’s blockchain adoption decision by comparing the retailer’s expected profit when adopting blockchain and not adopting blockchain. We provide all omitted proofs and conditions in the Online Supplemental Appendix.

If neither vendor enters the blockchain, both vendors solve (Equation 2), conjecturing that the other vendor will do the same. Solving the problems jointly, we get the following:

$$
\omega^ {N N} = \frac {\alpha}{(2 - t) \beta (1 + \kappa)}
$$

and

$$
q ^ {N N} = \frac {\alpha}{2 - t},
$$

where the superscript NN stands for the case in which neither type enters the blockchain. If only one vendor enters the blockchain, that vendor will solve (Equation 3), while the vendor that did not enter the blockchain solves (Equation 2). Jointly solving these two provides the following:

$$
\omega_ {B} ^ {B N} = \frac {(2 + t) \alpha - 2 \beta \Delta (1 + \kappa)}{(4 - t ^ {2}) \beta (1 + \kappa)}
$$

and

$$
q _ {B} ^ {B N} = \frac {(2 + t) \alpha + (2 - t ^ {2}) \beta \Delta (1 + \kappa)}{4 - t ^ {2}},
$$

for the vendor that enters the blockchain and

$$
\omega_ {N} ^ {B N} = \frac {(2 + t) \alpha - t \beta \Delta (1 + \kappa)}{(4 - t ^ {2}) \beta (1 + \kappa)}
$$

and

$$
q _ {N} ^ {B N} = \frac {(2 + t) \alpha - t \beta \Delta (1 + \kappa)}{4 - t ^ {2}},
$$

for the vendor that does not enter the blockchain. Notably, $\omega _ { B } ^ { B N } < \omega _ { N } ^ { B N }$ and $q _ { B } ^ { B N } > q _ { N } ^ { B N }$ Because of the additional incentive that R provides to the vendor who enters the blockchain, that vendor can charge a lower price and enjoy an increase in demand.

Finally, when both types enter the blockchain, both vendors solve (Equation 3), anticipating that the other vendor will do the same. The resulting supply price and quantity are as follows:

$$
\omega^ {B B} = \frac {\alpha - \beta \Delta (1 + \kappa)}{(2 - t) \beta (1 + \kappa)}
$$

and

$$
q ^ {B B} = \frac {\alpha + (1 - t) \beta \Delta (1 + \kappa)}{2 - t}.
$$

Since $\omega ^ { B B }$ is bounded from below at zero, R would not give a Δ greater than $\frac { \alpha } { ( 1 + \kappa ) \beta }$ in the BB case.

Vendors’ blockchain adoption decisions depend on their type (H or D) and their conjectures of the other vendor’s type. Depending on the players’ blockchain adoption strategies, there are three possible cases: both vendor types enter the blockchain (case BB); only H-types enter the blockchain (case BN); or neither type enters the blockchain (case NN). Note that there cannot be a case where only D-types enter the blockchain since the adoption cost is higher for D-types than for H-types while the benefits are the same. Not only would D-types have to incur the direct cost of adoption, $c _ { b } .$ , they would also have to forgo their practice of underreporting VAT.

If neither type enters the blockchain, a vendor’s expected profit would be

$$
\pi_ {i} ^ {N N} = \omega^ {N N} q ^ {N N} (1 - \sigma_ {i}) = \frac {\alpha^ {2} (1 - \sigma_ {i})}{(2 - t) ^ {2} \beta (1 + \kappa)},\tag{4}
$$

where $\sigma _ { i } = \sigma$ if vendor i is type H, and $\sigma _ { i } = \sigma \varepsilon$ if it is type D. When both types enter the blockchain, a vendor’s expected profit would be

$$
\pi^ {B B} = \frac {(\alpha + (1 - t) \beta \Delta (1 + \kappa)) ^ {2} (1 - \sigma)}{(2 - t) ^ {2} \beta (1 + \kappa)} - c _ {b}.\tag{5}
$$

When only H-types enter the blockchain, and there is a vendor of each type, then the H-type vendor’s profit would be

$$
\pi_ {B} ^ {B N} = \frac {\left((2 + t) \alpha + (2 - t ^ {2}) \beta \Delta (1 + \kappa)\right) ^ {2} (1 - \sigma)}{(4 - t ^ {2}) ^ {2} \beta (1 + \kappa)} - c _ {b},\tag{6}
$$

and the D-type vendor’s profit would be

$$
\pi_ {B} ^ {B N} = \frac {\left((2 + t) \alpha - t \beta \Delta (1 + \kappa)\right) ^ {2} (1 - \sigma \varepsilon)}{(4 - t ^ {2}) ^ {2} \beta (1 + \kappa)},\tag{7}
$$

where the subscript B (N) stands for blockchain adoption (or non-adoption). Comparing vendors’ profits gives us the range of $\varDelta$ within which vendors’ incentive constraints are satisfied in each case.

Anticipating the vendors’ strategies, the retailer decides whether to adopt blockchain and determines $\varDelta$ to maximize its expected profit. R’s expected profit when neither type of vendor adopts blockchain is

$$
\pi_ {R} ^ {N N} = 2 q ^ {N N} \big (p ^ {N N} (1 - \sigma) - \omega^ {N N} (1 - E [ \sigma_ {i} ]) \big),\tag{8}
$$

where $E [ { \sigma } _ { i } ] = ( \theta + ( 1 - \theta ) \in ) { \sigma } ,$ since R cannot observe vendors’ types. When R expects both types of vendors to adopt blockchain, its expected profit is

$$
\pi_ {R} ^ {B B} = 2 q ^ {B B} \big (p ^ {B B} - \omega^ {B B} - \big) (1 - \sigma) - c _ {B}.\tag{9}
$$

When R predicts only H-type vendors will adopt blockchain, it does so based on the following formulation: both vendors would adopt blockchain at probability $\theta ^ { 2 }$ ; neither vendor would adopt at probability $\left( 1 - \theta \right) ^ { 2 }$ ; and only one vendor would adopt blockchain at probability $2 \theta ( 1 - \theta )$ . Therefore, R’s expected profit in this case becomes

$$
\begin{array}{r l} & {\pi_ {R} ^ {B N} = - c _ {B} + \theta^ {2} \pi_ {R} ^ {B B} + (1 - \theta) ^ {2} \pi_ {R} ^ {N N} + 2 \theta (1 - \theta)} \\ & {\qquad \big ((p _ {B} ^ {B N} - \omega_ {B} ^ {B N} -) q _ {B} ^ {B N} (1 - \sigma) + [ p _ {N} ^ {B N} (1 - \sigma) - \omega_ {N} ^ {B N} (1 - \sigma \varepsilon) ] q _ {N} ^ {B N} \big)} \end{array}
$$

after substituting in $\pi _ { R } ^ { N N }$ . By comparing R’s profits, given the respective Δ that satisfies vendors’ incentive constraints in each case, we can solve for $R ^ { * } s$ blockchain adoption decision and determine the choice of $\Delta$ that would maximize R’s expected profit.

Notably, in our model, R reaps benefits from adopting blockchain only when dishonest vendors enter the blockchain since the increased transparency deters fraudulent VAT underreporting. Since H-types already report truthfully, their adoption of the blockchain would not benefit R. Due to the costliness of adopting blockchain and incentivizing vendors to enter the system, R would not benefit from adoption if only H-type vendors were to enter it. Therefore, R prefers case NN over case BN, since it is not worth the additional cost for R to adopt blockchain if only H were to enter. This leaves us to compare cases NN and BB. The following proposition summarizes the retailer’s blockchain adoption decision in equilibrium in this setting (all thresholds can be found in the Online Supplemental Appendix).

Proposition 1. When $c _ { b } < \overline { { c _ { b } } } , \sigma < \bar { \sigma }$ and $c _ { B } < \bar { c } _ { B } , \langle i \rangle$ R will choose to adopt blockchain and incentivize both vendors to enter the blockchain by setting $\Delta = \hat { \Delta } _ { D } ^ { B B }$ . Otherwise, R will not adopt blockchain.

Proposition 1 demonstrates that in a setting where R allows vendors to choose whether to enter the blockchain, it will decide to adopt blockchain only when the cost of blockchain adoption is not too high for both the retailer and vendors and when the $\mathrm { V A T }$ rate is suficiently low. Otherwise, it is not worthwhile for the retailer to adopt blockchain either because the cost of adoption is too high or because incentivizing vendors to join the blockchain is too costly to justify the benefits of deterring VAT underreporting.

Analyzing the condition for blockchain adoption gives us two subsets of when case NN occurs – when vendors do not adopt blockchain regardless of the retailer’s eforts, and when the retailer prefers not to adopt blockchain regardless of vendors’ incentives. The following corollary summarizes these two subsets.

Corollary 1. (i) When decreases in t and $\kappa ,$ and $\bar { \sigma }$ decreases in t; $\kappa ,$ and $c _ { b }$ ; and increases in ε when $c _ { b } < \overline { { c _ { b } } }$

(ii) When $\begin{array} { r } { c _ { B } \ge \frac { 2 ( 1 - t ) ( 1 - \epsilon ) ( 1 - \theta ) \sigma } { ( 2 - t ) ^ { 2 } ( 1 + t ) ( 1 + \kappa ) } } \end{array}$ , R will never adopt blockchain, regardless of vendors’ incentives.

Corollary 1(i) provides the conditions when vendors will not enter the blockchain regardless of the incentive provided by the retailer. The $\overline { { c _ { b } } }$ decreasing in both t and κ indicates that when vendors’ products are more similar or when the retailer adds a larger margin to the selling price, vendors are less willing to tolerate higher blockchain adoption costs. This is because vendors’ profits decrease in both t and κ, making a given blockchain adoption cost relatively more costly. The comparative statics on $\bar { \sigma }$ indicate that when vendors’ products are more similar, the retailer’s profit margin is greater, vendors’ cost of blockchain adoption is higher, or dishonest vendors’ VAT underreporting behavior is more aggressive, and they will choose not to enter the blockchain for a wider range of VAT rates. This is also driven by these variables’ efects on vendors’ profits. Note that we limit the incentive to $\begin{array} { r } { \varDelta < \frac { \alpha } { ( 1 + \kappa ) \beta } } \end{array}$ since prices are bounded from below by zero, and any $\varDelta$ greater than this amount suggests a negative price.

![](/api/attachments/CAWDPKXR/fulltext/images/e7e9efc2ccd018aa61a70042e3f0da9e7f4ef98595238da80bb79aefed33e6f0.jpg)  
(a) and $c _ { b }$

![](/api/attachments/CAWDPKXR/fulltext/images/1920a8a7b27698143250169b48e905c8e190b7637f002f6d71848926d6eb70a6.jpg)  
(b) and $c _ { B }$  
Figure 3. Blockchain adoption in terms of $\sigma , c _ { b } ,$ and $c _ { B } .$  
In Figure 3, the black area indicates the parameter values $( c _ { B } , c _ { b } ,$ , and σ) under which R adopts blockchain and the vendors enter the system (Case BB). R and/or the vendors will prefer to choose Case NN, where the parameter values lie in the light grey and dark grey areas. The light grey area indicates the region where R does not adopt the blockchain, but the vendors are suficiently incentivized to enter it. The dark grey area indicates the region where R adopts blockchain, but the vendors do not enter it. The white area denotes the region where neither R nor the vendors adopt blockchain. $( t = 0 . 0 5 , \theta = 0 . 5 )$

Corollary 1(ii) presents the lower bound on the retailer’s cost of blockchain adoption above which the retailer will prefer not to adopt blockchain, even if it does not have to compensate vendors for entering the blockchain. This threshold is decreasing in t, κ, ε, and $\theta ,$ and is increasing in σ. This implies that when vendors’ products are more similar, the retailer’s normal profit margin is greater, the dishonest vendors’ VAT underreporting behavior is less aggressive. Conversely, when vendors are more likely to be honest, R becomes less tolerant of higher blockchain adoption costs. As R’s profit increases in t, κ, ε, and θ, the retailer’s incentive to adopt blockchain decreases.

Figure 3 summarizes Proposition 1 and Corollary 1 through a numerical analysis that utilizes three variables $( c _ { B } , c _ { b } ,$ , and σ) related to the threshold conditions in Proposition 1 and Corollary 1. Figure 3a depicts the decisions of R and the vendors in terms of two parameter values, σ and $c _ { b } ;$ ; Figure 3b shows how σ and $c _ { B }$ afect R and the vendors decisions. Figures 3a and 3b illustrate how the blockchain adoption costs $c _ { b }$ and $c _ { B }$ afect the players’ respective decisions $( c _ { b }$ afects the vendors’ decision and $c _ { B }$ afects R’s decision). If the values of $c _ { b }$ and $c _ { B }$ are less than their respective threshold values, R and the vendors will all adopt the blockchain. Figure 3 also shows how the VAT rate afects the thresholds on blockchain adoption costs. While the threshold for $c _ { b }$ decreases in $\sigma ,$ the threshold for $c _ { B }$ increases in σ, reflecting how the VAT rate exerts diferent efects vis-à-vis the benefits of blockchain adoption for the retailer and vendors.

Figure 4 is an extension of Figure 3, with Figures 4a and 4b depicting how a higher t or a lower θ would afect blockchain adoption decisions. Figure 4a shows how changes in substitutability between two competing products afect the decision $( t = 0 . 5$ in Figure 4 while $t = 0 . 0 5$ in Figure 3). A comparison of Figures 3a and 4a shows that if the value of t is higher, the blockchain adoption region decreases as the threshold for $c _ { b }$ decreases. This is because as the competition between two vendors intensifies (i.e., high substitutability), the vendors have less budget to allocate to blockchain adoption.

![](/api/attachments/CAWDPKXR/fulltext/images/84cbc04273943d7cc47a03500bad63b55c3d1fcd7398c039f5a68818a586185e.jpg)  
(a) High substitutability  
(t = 0.5, = 0.5)θ

![](/api/attachments/CAWDPKXR/fulltext/images/a7d498fe9be1160577450bc2e6643a2d7409a5b5171c6c7f38fa33819d8f601a.jpg)  
(b) Lower θ  
(t = 0.05, θ = 0.2)  
Figure 4. Blockchain adoption in terms of σ and $c _ { b } .$  
In Figure 4, the black area indicates the parameter values $( c _ { B } , c _ { b } ,$ and σ) under which R adopts blockchain and the vendors enter the system (Case BB). The light grey area indicates the region where R does not adopt the blockchain, but the vendors are suficiently incentivized to enter it. The dark grey area indicates the region where R adopts blockchain, but the vendors do not enter it. The white area denotes the region where neither R nor the vendors adopt blockchain.

Figure 4b depicts how a higher proportion of dishonest vendors (lower θ) afects blockchain adoption (θ = 0.5 in Figure 3a and θ = 0.2 in Figure 4b). A comparison of Figures 3a and 4b shows how the retailer becomes increasingly willing to adopt blockchain for lower values of θ in order to prevent the vendors from underreporting VAT. Notice that even if the tax rate is relatively low, the expected underreported VAT can ultimately be high in the presence of a low value of θ.

## Additional Analyses and Welfare Implications

Thus far, we have considered a case where the retailer cannot force the vendor to adopt blockchain. This section looks at an expanded scenario wherein the retailer forces vendors to adopt blockchain by threatening to sever business ties if they do not. We also study the implications of blockchain adoption as they relate to the tax collection agency and analyze the efects on social welfare.

## Retailer’s Blockchain Adoption Decision an Obligation Policy

Depending on the retailer’s market power and its reliance on the vendors, the retailer may pursue a take-it-or-leave-it approach to push vendors to enter the blockchain. In this subsection, we consider a scenario in which the vendors must enter the adopted blockchain system or risk severing business ties with R. While the retailer’s profit given Δ in this scenario is the same as in the base model, the obligation policy allows the retailer to motivate vendors to adopt the system with a lower Δ. As before, the retailer does not prefer the case where only H-type vendors enter the adopted blockchain.

Moreover, under the obligation policy, the BN case could result in a monopoly for the vendor that chooses to enter the blockchain, leaving the retailer in a worse position than it was in prior to adoption. Therefore, the retailer decides either not to adopt reject adoption (case NN) or to adopt the system and incentivize both vendors to enter it (case BB).

Under the obligation policy, the vendors’ incentive constraint for the BB case becomes

$$
\pi^ {B B} > 0 c _ {b} <   \frac {(1 - t) (1 + \Delta (1 + \kappa)) ^ {2} (1 - \sigma)}{(2 - t) ^ {2} (1 + t) (1 + \kappa)}.\tag{10}
$$

For any Δ, the right-hand side is greater than in the base setting, indicating that R can motivate vendors to enter the blockchain with a smaller Δ. The following corollary examines R’s decision regarding the new strategy.

Corollary 2. If R requires its vendors to enter the adopted blockchain if they wish to continue doing business with R (obligation policy), it will tolerate higher blockchain adoption costs (c ) than in the case without the obligation policy.

By comparing the necessary $\varDelta \ ' s$ to motivate vendors’ blockchain adoption with and without the obligation policy, we find that the diference decreases in t, κ, σ, and ε. This implies that the obligation policy is more efective when the products are less similar, the retailer’s profit margin is smaller, the VAT rate is lower, and when dishonest vendors underreport a more significant portion of their VAT.

## Tax Collection Agency

In the previous sections, we focused on the decision makers who determine whether to adopt the blockchain system (the retailer) or participate in the system (the vendors). Adopting blockchain to the VAT reporting system can also afect the tax collection agency in terms of collected tax amounts and the costs of handling misreported or underreported tax. In this subsection, we expand our examination by analyzing how blockchain adoption afects the tax collection agency’s profits and discuss its impact on social welfare.

We focus on analyzing how blockchain adoption afects a tax collection agency in Cases NN and BB since these are the feasible cases based on our analysis. According to the assumptions of our base model (the autonomy policy scenario), if the blockchain system is not adopted (Case NN), information asymmetry exists between the retailer, vendors, and tax collection agency in the short term. We further assume that the tax collection agency may incur additional costs to correct the misreported tax over the long term. Under these assumptions, the VAT reporting process unfolds as follows: the tax collection agency, which employs the credit-invoice method VAT, collects tax from the retailer and vendors based on the full value of their respective sales, $2 q ^ { N N } ( p ^ { N N } \sigma + \omega ^ { N N } E [ \sigma _ { i } ] )$ , and gives tax credits to the retailer based on what was reported by vendors, $2 q ^ { N N } ( \omega ^ { N N } E [ \sigma _ { i } ] )$ . The expected profit of the tax collection agency in the short term would be

$$
T _ {s h o r t} ^ {N N} = 2 q ^ {N N} p ^ {N N} \sigma
$$

since the taxes collected from the vendors and the tax credits paid to the retailer cancel each other out.

If the retailer requests a modification of an incorrect tax credit arising from $D ' s$ underreporting, the tax collection agency would rectify the incorrect tax credit by paying the correct credit to the retailer. We assume that this process occurs over the medium term of the VAT reporting system cycle.<sup>15</sup> In the medium term, the tax collection agency’s profit would be

$$
T _ {m e d i u m} ^ {N N} = 2 q ^ {N N} p ^ {N N} \sigma - 2 q ^ {N N} \omega^ {N N} (\sigma - E [ \sigma_ {i} ]) - c _ {f \_ m e d i u m},
$$

where $c _ { f - m e d i u m }$ is the expected cost for rectifying the incorrect credit caused by $D ' s$ misreported tax and paying the correct credit to the retailer. We can express this cost as $c _ { f - m e d i u m } = 2 c _ { s } ( 1 - \theta )$ ; where $c _ { s }$ is the cost spent by the tax collecting agency for the above investigation and rectification, and $2 ( 1 - \theta )$ is the probability that at least one of the vendors is a D-type. In the medium term, the tax credit granted by the tax agency to the retailer is larger than the tax collected from the vendors due to the aforementioned information asymmetry.

Finally, in the long term, the tax collection agency conducts an audit to identify D-type vendors’ underreported tax. If the tax agency identifies the vendor who misreported VAT, the agency’s resulting profit would be

$$
T _ {l o n g} ^ {N N} = 2 q ^ {N N} \sigma p ^ {N N} - c _ {f \_ l o n g}
$$

where $c _ { f \_ l o n g } = c _ { f \_ m e d i u m } + 2 c _ { s } ( 1 - \theta )$ is the total cost the tax agency incurs to identify and correct misreported tax. $c _ { f \_ l o n g }$ captures the additional investigation cost the agency must spend, $c _ { s } ,$ to rectify $D ' s$ misreported VAT and to impose the correct tax. When pursuing an expanded investigation between the medium and long term, the tax collection agency would perform a cost-benefit analysis that considers the administrative and compliance costs as well as the prospective benefits of deterring further misreporting [12, 16].

Conversely, if blockchain is adopted to the supply chain linking the retailers and vendors, the profit of the tax collection agency would simply be $T _ { B B } = \bar { 2 } q _ { i } ^ { B B } \sigma p _ { i } ^ { B B }$ . Since the blockchain system deters the relevant entities from misreporting taxes, its adoption would preclude any costs arising from investigating and rectifying tax misreporting. Specifically, since $\begin{array} { r } { q _ { i } ^ { N N } p _ { i } ^ { N N } - q _ { i } ^ { B B } p _ { i } ^ { B B } \geq 0 \Big ( \frac { \Delta ( 1 + \kappa ) ( t + \Delta + \Delta \kappa ) } { ( 2 - t ) ^ { 2 } ( 1 + t ) } \geq 0 \Big ) } \end{array}$ , if the value of $c _ { s }$ or $q _ { i } ^ { N N }$ is high or the value of $\theta$ is low, $c _ { s }$ would be significantly higher than the additional profits the tax collection agency would reap in the case of blockchain adoption (as opposed to non-adoption). In other words, if more goods are traded in the digital economy, the tax agency will prefer to adopt blockchain to control VAT misreporting. Moreover, if more low-value goods are traded $( \mathrm { i . e . , i f } p _ { i } ^ { N N }$ and $ { p _ { i } ^ { B B } }$ are low), $c _ { s }$ is perceived as a relatively high cost by the tax agency, which will thus prefer to adopt blockchain to control VAT misreporting.

Another mechanism the tax collection agency can adopt is the imposition of penalties for entities that underreport their taxes. Let us suppose that the tax collection agency imposed $c _ { p }$ on the D-type vendor that misreported their tax. This penalty has two functions. First, it deters vendors from underreporting their tax by increasing the cost of misreporting. Second, from the tax collection agency’s perspective, $c _ { p }$ essentially functions as revenue. Therefore, introducing this penalty will decrease the occurrence of tax misreporting and also reduce the tax collection agency’s net cost of an investigation. From the tax collection agency’s perspective, both of these efects would diminish the net benefit of adopting blockchain. However, our model shows that unless the agency can impose a penalty that is prohibitively high enough to deter all tax misreporting, the imposition of a penalty cannot entirely negate the efects of blockchain adoption.

## Social Welfare

To analyze the impact of blockchain adoption on social welfare, we compare the long-term social welfare between cases NN and BB. We define social welfare as the sum of the profits of the afected and relevant entities (i.e., the retailer, vendors, and tax collection agency). The long-term expected social welfare in the feasible cases (NN and BB) are expressed as follows, respectively:

$$
S W _ {N N} = \pi_ {R} ^ {N N} + \sum_ {i = A, B} \pi_ {i} ^ {N N} + T _ {N N - j}, j \in \{m e d i u m, l o n g \}, a n d
$$

$$
S W _ {B B} = \pi_ {R} ^ {B B} + \sum_ {i = A, B} \pi_ {i} ^ {B B} + T _ {B B}.
$$

A comparison between $S W _ { N N }$ and $S W _ { B B }$ reveals that policymakers should encourage the retailer and vendors to adopt blockchain if investigation and rectification costs arising from the misreported tax would significantly outstrip the costs of blockchain adoption $\left( c _ { s } > 2 c _ { b } + c _ { B } \right)$ . In our analysis, Proposition 1 and Corollary 1 show that the retailer and vendors would adopt blockchain if the adoption costs are below certain thresholds. The aforementioned analysis shows that even when the retailer and vendors may decide not to adopt blockchain, policymakers – who place greater weight on social welfare and costs triggered by misreported tax – may prefer to adopt blockchain and would consider subsidizing blockchain adoption costs for the sake of enhanced welfare.

If we introduced the penalty $c _ { p }$ that we discussed in the previous subsection, SW<sub>NN</sub> would increase since the penalty would deter some D-type vendors from misreporting their tax. The payment itself does not afect social welfare since it is a transfer payment from the D-type vendor to the tax collection agency. While the penalty may reduce the net benefit of adopting blockchain, it does not nullify the benefits of blockchain adoption since imposing the penalty still requires investigation and rectification costs and cannot entirely prevent or detect tax misreporting.

In Figure 5, we show how the retailer and vendors’ blockchain adoption decisions can difer from those of policymakers (who prioritize social welfare). Specifically, in Figure 5a, a high tax rate encourages policymakers to adopt the blockchain while the retailer and vendors decide against it. What is interesting from this numerical analysis is that blockchain adoption occurs naturally (based on the choice of the retailer and vendors) and only maximizes social welfare for intermediate values of $\sigma .$ Also, the numerical analysis shows that if σ is significantly low, the tax collection agency and the retailer do not care about the potential loss caused by misreported tax and thus do not adopt the blockchain.

Figure 5b shows that if the adoption costs $( c _ { B }$ and $c _ { b } )$ are relatively high, the retailer and vendors do not adopt blockchain, but policymakers prefer adoption in consideration of the potential benefits to social welfare. In this case, policymakers may consider subsidizing the adoption cost for the retailer and vendors. Since the figure also shows that the vendors are more sensitive to blockchain adoption cost considerations, policymakers may also allocate more subsidies to that particular group.

![](/api/attachments/CAWDPKXR/fulltext/images/e2b9bb2e78cd942e2eba6760d3561cddd3fab0e9869c0ba30b51b7b64a41eaed.jpg)  
(a) Blockchain adoption in terms of and $c _ { s }$

![](/api/attachments/CAWDPKXR/fulltext/images/19f33e57e3b7521a34dcbb129438c2568733d5c567aed081c2b6e92c9860404a.jpg)  
(b) Blockchain adoption in terms of $c _ { b }$ and $c _ { B }$  
Figure 5. Diference between social welfare and blockchain adoption decision (Case BB). In Figure 5(a) and Figure 5(b), the black area indicates the parameter values $( c _ { B } , c _ { b } , c _ { s } , \mathsf { a n d } \sigma )$ under which social welfare is maximized through blockchain adoption (i.e., policymakers prefer to adopt blockchain) and R and the vendors adopt blockchain (Case BB). Meanwhile, in the grey area, social welfare is maximized through blockchain adoption, but blockchain is not adopted by R and the vendors (Case NN). The white area denotes where social welfare is maximized without blockchain adoption, and blockchain is not adopted by R and the vendors (Case NN). $( t = 0 . 0 5 , \theta = 0 . 3 )$

## Discussion of Our Findings Concerning Blockchain and Auditing

Our paper examines the factors driving blockchain’s increasing indispensability to the digital economy. Blockchain can help increase VAT compliance in transactions involving multijurisdictional sellers and buyers such as those operating in online marketplaces and platforms. More specifically, our paper focuses on blockchain’s ability to enhance data integrity and deter tax misreporting by vendors. Accordingly, we examine scenarios where diferent entities adopt blockchain after considering the repercussions for VAT collection and payment. Our findings in Proposition 1 and Corollary 1 show that the retailer will consider the adoption costs and VAT rate to determine its blockchain adoption policy under the following two conditions. First, if blockchain adoption costs are relatively low, the retailer will choose to adopt while ofering incentives to vendors. A low adoption cost grants the retailer the flexibility to provide incentives to vendors to encourage them to join the blockchain, ultimately increasing its profit. Moreover, if the retailer ofers an acceptable incentive, the low price could convince vendors to enter the blockchain and forego illicitly profiting from underreported VAT. In addition, if policymakers expect blockchain adoption to contribute to gains in social welfare, they may seek to subsidize the cost of adoption; advances in technology could decrease that cost even further. Second, on the one hand, if the VAT rate is relatively low, vendors would have less incentive to underreport VAT, enabling the retailer to attract vendors to enter the blockchain by ofering a smaller incentive payment. If the VAT rate is high, on the other hand, vendors would have a stronger incentive not to enter the blockchain due to the opportunity to underreport

VAT and generate higher profits. Hence, it would be more costly to incentivize vendors to enter the blockchain, ultimately swaying entities weighing blockchain adoption to consider other mechanisms to bolster VAT compliance.

Another mechanism that can prevent and detect unintentional errors or intentional misstatements is auditing. Auditing has been studied extensively in information economics and accounting as a method that can reduce agency costs [26, 44, 97], especially when information asymmetry exists between the principal and agent [25, 81]. However, one critical diference between blockchain and auditing is that the latter is subject to agencyrelated problems [4], whereas the former is not. Cao et al. [15] highlight this diference in their paper by modeling blockchain as an automatic verification feature while modeling auditors as agents maximizing their utility. Moreover, blockchain ofers a superior alternative vis-à-vis cost, continuity, and automaticity in the following ways: 1) the operational costs of blockchain systems are less dependent on the size of the transaction volume as compared to traditional audit procedures [21]; 2) traditional audits cannot continuously monitor business activities, whereas blockchain can provide timely data quality assurance [59, 101]; and 3) unlike audits, blockchain can provide automatic verification without revealing the proprietary information of the clients (e.g., vendors) [15].

## Concluding Remarks

## Theoretical Implications

We have proposed a modeling framework to analyze the strategic and economic value of blockchain by applying it to a VAT reporting system setting. Specifically, our model captures the following dynamics of relevant entities in the blockchain adoption and VAT collection processes: 1) two potential types of vendors (H and D) vis-à-vis VAT tax reporting; 2) the competition between vendors and resultant impacts on the purchase price p; 3) the retailer’s incentive pricing strategy vis-à-vis vendors (i.e., increasing the purchase price by Δ) aimed at deterring VAT underreporting; and 4) the retailer’s potential strategies vis-à-vis the vendors’ decisions regarding blockchain adoption (i.e., encouraging or obligating the vendors to join the blockchain). Based on these captured dynamics, we analyzed the retailer’s blockchain adoption and purchase price strategies and the vendors decisions to enter the blockchain or not.

Our findings provide pragmatic ideas for blockchain adoption by considering returns on blockchain investment through an analysis of concrete monetary values rather than relying on uninformed popular beliefs concerning the benefits of blockchain. Furthermore, our model can easily be adapted to analyze blockchain’s utility in processing other types of tax compliance (e.g., sales tax for online sellers and buyers across multiple states [19]) and to assess blockchain’s efects on data integrity for inter-organizational activities. In addition, this paper’s game theoretical model provides implications for blockchain application strategies in scenarios where entities’ decisions are influenced by asymmetric information and divergent interests.

## Managerial Implications

Our findings ultimately argue for blockchain adoption in consideration of its potential benefits and cost savings and provide significant managerial insights for entities considering the adoption of and entry into blockchain systems, as well as for the policymakers who regulate these entities.

Our analysis shows, on the one hand, that a retailer will adopt the technology and ofer incentives for vendors to enter the blockchain if the VAT rate and adoption costs are relatively low. On the other hand, if the retailer decides to do business only with vendors that enter the blockchain, vendors will tolerate higher adoption costs. In our extended analysis involving the tax collection agency and social welfare efects, we find that policymakers may encourage the retailer and vendors to adopt blockchain in consideration of the potential costs arising from misreported VAT (notably, the policymakers decision conditions are less strict than those of the retailer and vendors). If the retailer and vendors do not adopt blockchain due to cost concerns, policymakers may consider subsidizing the adoption. Even though our analysis focuses on retailers and vendors, the model setup can be generalized to explore blockchain’s potential value for various other entities, such as companies or government agencies adopting private blockchain systems as well as for those entities that are deliberating whether to enter the systems being ofered to them.

## Notes

1. In recent years, Walmart has assiduously developed its e-commerce business strategies and significantly increased its online sales.

2. Shopify’s guidance to its vendors reflects the ways in which the newly imposed VAT on digital goods can potentially afect both the internal and inter-company business processes of online platforms. See more details at https://help.shopify.com/en/manual/taxes/tax-on-digitalproducts.

3. See more details at https://www.oecd-ilibrary.org/docserver/ctt-2018-en.pdf.

4. Comparatively, the subtraction method does not impose VAT tax on the firm for each transaction stage and is instead calculated as a net amount at year-end. Japan is the only country that uses the subtraction method.

5. Low-value goods refer to goods whose value does not exceed certain monetary thresholds (e.g., €150) are generally exempt from VAT.

6. See more details at https://en.wikipedia.org/wiki/List\_of\_video\_game\_developers (list of video game developers) and https://en.wikipedia.org/wiki/List\_of\_Stadia\_games (list of Stadia games).

7. The commission rate (profit margin in our paper) used in Figure 1 is based on a recent Apple press release. See more details at: https://www.apple.com/newsroom/2020/11/apple-announces -app-store-small-business-program/.

8. See more details at http://www.vatfraud.org/.

9. In our model, the retailer is the buyer and the vendors are sellers.

10. While profit margins vary across product categories, they are generally consistent among products within a given category. Empirically, on Amazon, these rates range from 6 percent to 25 percent of the sales price, depending on the product category [94].

11. To simplify our analysis, we keep ε exogenous. Endogenizing ε should not qualitatively change our results.

12. This is a commonly used linear demand system [2, 44, 48, 78, 83, 84].

13. Abhishek et al. (2016) [2] refer to the degree of substitutability as the “degree of diferentiation.”

14. In our model, we consider digital goods and assume that the marginal cost of production for the goods is zero. However, the model can be extended to accommodate non-zero marginal

costs. Kim (2018) [48] provides a good discussion on how electronic channels would interact with traditional channels.

15. This assumption stems from real-world examples. If a retailer has various vendors, some of which are cross-border entities from multinational jurisdictions, it could take more time to investigate misreported VAT.

## References

1. Abeyratne, S.A.; and Monfared, R.P. Blockchain ready manufacturing supply chain using distributed ledger. International Journal of Research in Engineering and Technology, 5, 9 (2016), 1–10.

2. Abhishek, V.; Jerath, K.; and Zhang, Z.J. Agency selling or reselling? Channel structures in electronic retailing. Management Science, 62, 8 (2016), 2259–2280.

3. Almunia, M.; Gerard, F.; Hjort, J.; Knebelmann, J.; Nakyambadde, D.; Raisaro, C.; and Tian, L. An analysis of discrepancies in tax declarations submitted under value-added tax in Uganda. International Growth Centre Project Report, (2017). https://www.theigc.org/wp-content /uploads/2017/05/Almunia-et-al-2017-final-report.pdf (accessed on May, 2021).

4. Antle, R. The auditor as an economic agent. Journal of Accounting Research, 20, 2 (1982), 503–527.

5. Antons, D.; Salge, T. O.; Barrett, M., Kohli, R.; and Oborn, E. The Social Value of Information Technology: How IT Investments Enhance Hospital Reputation. Westchester: Academy of Management Proceedings, 2015.

6. Arakji, R.Y.; and Lang, K.R. Digital consumer networks and producer-consumer collaboration: innovation and product development in the video game industry. Journal of Management Information Systems, 24, 2 (2007), 195–219.

7. Bakos, Y.; and Brynjolfsson, E. Bundling information goods: Pricing, profits, and eficiency. Management science, 45, 12 (1999), 1613-1630.

8. Bakos, Y.; and Brynjolfsson, E. Bundling and Competition on the Internet. Marketing science, 19, 1 (2000), 63–82.

9. Ballou, D.P.; and Tayi, G.K. Methodology for allocating resources for data quality enhancement. Communications of the ACM, 32, 3 (1989), 320–329.

10. Bao, D.-H.; and Romeo, G.C. Tax Avoidance and Corporations in the United States—The Efective Tax Rate Abnormality for the Top Five Percent by Corporate Size. Journal of Applied Business and Economics, 14, 4 (2013), 88–100.

11. Bloomberg Tax. Insight: Online Gaming-Play with VAT Carefully. 2020. https://news.bloom bergtax.com/daily-tax-report-international/insight-online-gaming-play-with-vat-carefully (accessed on May, 2021).

12. Bloomberg Tax. Tax Authorities Worldwide Lean on E-Commerce Sites to Collect VAT. 2019. https://news.bloombergtax.com/daily-tax-report-international/tax-authorities-worldwidelean-on-e-commerce-sites-to-collect-vat (accessed on May, 2021).

13. Bloomberg Tax b. EU Inches Toward Blockchain in Fight Against VAT Fraud. 2019. https:// news.bloombergtax.com/daily-tax-report-international/eu-inches-toward-blockchain-in-fight -against-vat-fraud-1 (accessed on May, 2021)

14. Browne, R. Five things that must happen for blockchain to see widespread adoption, according to Deloitte. CNBC, 2018. https://www.cnbc.com/2018/10/01/five-crucial-challenges-forblockchain-to-overcome-deloitte.html (accessed on May, 2021).

15. Cao, S.; Cong, L.W.; and Yang, B. Financial Reporting and Blockchains: Audit Pricing, Misstatements, and Regulation. SSRN, (2019). https://papers.ssrn.com/sol3/Papers.cfm? abstract\_id=3248002. (accessed on May, 2021)

16. Carrillo, P.; Pomeranz, D.; and Singhal, M. Tax me if you can: Evidence on firm misreporting behavior and evasion substitution. Working Paper, Harvard University (2014).

17. Chellappa, R. K.; and Shivendu, S. Economic implications of variable technology standards for movie piracy in a global context. Journal of Management Information Systems, 20, 2 (2003), 137–168.

18. Clemons, E.K.; and Hitt, L.M. Poaching and the misappropriation of information: Transaction risks of information exchange. Journal of Management Information Systems, 21, 2 (2004), 87–107

19. CNBC. US Supreme Court struggles with e-commerce sales tax case. 2018. https://www.cnbc. com/2018/04/17/us-supreme-court-to-consider-whether-to-let-states-force-out-of-stateonline-retailers-to-collect-sales-taxes.html (accessed on May, 2021)

20. Cryptomorrow. Blockchain met e-invoicing and has potential to make it much better. 2019. https://blockmodo.com/markets/news/a93b8ae2-6abc-3cba-8b27-79ac2798010d-hvn-block chain-met-e-invoicing-and-has-potential-to-make-it-much-bette (accessed on May, 2021).

21. Dai, J.; and Vasarhelyi, M.A. Toward blockchain-based accounting and assurance. Journal of Information Systems, 31, 3 (2017), 5–21.

22. Davidson, S.; De Filippi, P.; and Potts, J. Economics of blockchain. Available at SSRN 2744751, (2016).

23. Dawson, G.S.; Watson, R.T.; and Boudreau, M.-C. Information asymmetry in information systems consulting: Toward a theory of relationship constraints. Journal of Management Information Systems, 27, 3 (2010), 143–178.

24. Deloitte. Deloitte’s 2019 global blockchain survey: blockchain gets down to business. Deloitte, 2019. https://www2.deloitte.com/content/dam/Deloitte/se/Documents/risk/DI\_2019-globalblockchain-survey.pdf (accessed on May, 2021).

25. Demski, J.S.; and Sappington, D. Optimal incentive contracts with multiple agents. Journal of Economic Theory, 33, 1 (1984), 152–171.

26. Demski, J.S.; Frimor, H.; and Sappington, D.E. Audit error. Journal of Engineering and Technology Management, 23, 1–2 (2006), 4–17.

27. Dimitrov, B. How Walmart And Others Are Riding A Blockchain Wave To Supply Chain Paradise. Forbes, 2019. https://www.forbes.com/sites/biserdimitrov/2019/12/05/how-walmartand-others-are-riding-a-blockchain-wave-to-supply-chain-paradise/ (accessed on May, 2021).

28. DuPont, Q.; and Maurer, B. Ledgers and law in the blockchain. Kings Review. 2015http:// kingsreview.co.uk/magazine/blog/2015/06/23/ledgers-and-law-in-the-blockchain (accessed on May, 2021)

29. Fortune Z. European Commission To Introduce Blockchain Regulatory Sandbox By 2022. 2020. https://fortunez.com/european-commission-to-introduce-blockchain-regulatorysandbox-by-2022/(accessed on May, 2021).

30. Gastwirth, A.; and Hamilton, M. H. How blockchain, Internet of Things and smart contracts improve the supply chain. Dlapiper, 2018. https://www.dlapiper.com/en/uk/insights/publica tions/2018/09/ipt-news-q3-2018/how-blockchain-iot-and-smart-contracts-improve-thesupply-chain/(accessed on February, 2021).

31. Gefen, D. What makes an ERP implementation relationship worthwhile: Linking trust mechanisms and ERP usefulness. Journal of Management Information Systems, 21, 1 (2004), 263–288.

32. Geng, X.; Lin, L.; and Whinston, A.B. Efects of organizational learning and knowledge transfer on investment decisions under uncertainty. Journal of Management Information Systems, 26, 2 (2009), 123–145.

33. Ghose, A.; Telang, R.; and Krishnan, R. Efect of electronic secondary markets on the supply chain. Journal of Management Information Systems, 22, 2 (2005), 91–120.

34. Gomber, P.; Kaufman, R.J.; Parker, C.; and Weber, B.W. On the fintech revolution: interpreting the forces of innovation, disruption, and transformation in financial services. Journal of Management Information Systems, 35, 1 (2018), 220–265.

35. Gozman, D.; Liebenau, J.; and Mangan, J. The innovation mechanisms of fintech start-ups: insights from SWIFT’s innotribe competition. Journal of Management Information Systems, 35, 1 (2018), 145–179.

36. Grover, V.; and Kohli, R. Cocreating IT value: New capabilities and metrics for multifirm environments. MIS Quarterly, (2012), 225-232.

37. Grover, V.; Chiang, R. H. L.; Liang, T. -P.; and Zhang, D. Creating strategic business value from big data analytics: a research framework. Journal of Management Information Systems, 35, 2 (2018), 388–423.

38. Grover, V.; Kohli, R.; and Ramanlal, P. Being Mindful in Digital Initiatives. MIS Quarterly Executive, 17, 3 (2018), 11.

39. Harland, C.; Brenchley, R.; and Walker, H. Risk in supply networks. Journal of Purchasing and Supply management, 9, 2 (2003), 51–62.

40. Hinz, O.; Otter, T.; and Skiera, B. Estimating network efects in two-sided markets. Journal of Management Information Systems, 37, 1 (2020), 12–38.

41. Ho, S.-C.; Kaufman, R.J.; and Liang, T.-P. A growth theory perspective on B2C e-commerce growth in Europe: An exploratory study. Electronic Commerce Research and Applications, 6, 3 (2007), 237–259.

42. Huang, H.; Parker, G.; Tan, Y. R.; and Xu, H. Altruism or shrewd business? Implications of technology openness on innovations and competition. MIS Quarterly, 44, 3 (2020).

43. James, K. The rise of the value-added tax. Cambridge, UK: Cambridge University Press, 2015.

44. Jarczyk, D. Blockchain and the future of tax. KPMG, 2018. https://tax.kpmg.us/articles/2018/ blockchain-and-future-of-tax.html (accessed on May, 2021)

45. Jerath, K.; and Zhang, Z.J. Store within a store. Journal of Marketing Research, 47, 4 (August 2010), 748–763.

46. Johnson, M. E.; and Whang, S. E-business and supply chain management: An overview and framework. Production and Operations management, 11, 4 (2002), 413–423.

47. Kathuria. A.; Karhade, P. P.; Konsynski, B. R. In the realm of hungry ghosts: Multi-level theory for supplier participation on digital platforms. Journal of Management Information Systems, 37, 2 (2020), 396–430.

48. Kazan, E.; Tan, C.-W.; Lim, E.T.K.; Sørensen, C.; and Damsgaard, J. Disentangling digital platform competition: The case of UK mobile payment platforms. Journal of Management Information Systems, 35, 1 (2018), 180–219.

49. Kim, A. Doubly-bound relationship between publisher and retailer: The curious mix of wholesale and agency models. Journal of Management Information Systems, 35, 3 (2005), 840–865.

50. Koester, A. Investor valuation of tax avoidance through uncertain tax positions. In 2011 American Accounting Association Annual Meeting-Tax Concurrent Sessions. 2011.

51. Kohli, R.; and Devaraj, S. Measuring information technology payof: A meta-analysis of structural variables in firm-level empirical research. Information Systems Research, 14, 2 (2003), 127–145.

52. Kohli, R.; and Devaraj, S. Realizing the business value of information technology investments: An organizational process. MIS Quarterly Executive, 3, 1 (2008), 6.

53. Kohli, R.; Devaraj, S.; and Ow, T. T. Does information technology investment influence a firm’s market value? A case of non-publicly traded healthcare firms. MIS Quarterly, 36, 4 (2012), 1145–1163.

54. KPMG. VAT/GST treatment of cross-border services https://assets.kpmg/content/dam/kpmg/ xx/pdf/2017/11/ess-survey-13-nov-17.pdf (accessed on May, 2021).

55. Liang, T. P. (2017). Organizational adoption of information technologies. Pacific Asia Journal of the Association for Information Systems, 9, 1 (2017), 1.

56. Liang, T.-P.; and Huang, J.-S. A framework for applying intelligent agents to support electronic trading. Decision Support Systems, 28, 4 (2000), 305–317.

57. Liang, T.-P.; and Huang, J.-S. An empirical study on consumer acceptance of products in electronic markets: a transaction cost model. Decision Support Systems, 24, 1 (1998), 29–43.

58. Liang, T.-P.; You, J.-J.; and Liu, C.-C. A resource-based perspective on information technology and firm performance: A meta analysis. Industrial Management & Data Systems, 110, 8 (2010), 1138–1158.

59. Lin, M.; Li, S.; and Whinston, A.B. Innovation and price competition in a two-sided market. Journal of Management Information Systems, 28, 2 (2011), 171–202.

60. Lindow, P.E.; and Race, J.D. Beyond traditional audit techniques. Journal of Accountancy, 194, 1 (2002), 28–33.

61. Lowry, P.B.; Zhang, J.; Moody, G.D.; Chatterjee, S.; Wang, C.; and Wu, T. An integrative theory addressing cyberharassment in the light of technology-based opportunism. Journal of Management Information Systems, 36, 4 (2019), 1142–1178.

62. Mai, F.; Shan, Z.; Bai, Q.; Wang, X.; and Chiang, R.H.L. How does social media impact Bitcoin value? A test of the silent majority hypothesis. Journal of Management Information Systems, 35, 1 (2018), 19–52.

63. Mamoshina, P.; Ojomoko, L.; Yanovich, Y.; Ostrovski, A.; Botezatu, A.; Prikhodko, P.; Izumchenko, E.; Aliper, A.; Romantsov, K.; Zhebrak, A.; Ogu, I.A.; and Zhavoronkov, A. Converging blockchain and next-generation artificial intelligence technologies to decentralize and accelerate biomedical research and healthcare. Oncotarget, 9, 5 (2018), 5665–5690.

64. Marotta, D. J. What Is Rent-Seeking Behavior? Forbes. https://www.forbes.com/sites/ davidmarotta/2013/02/24/what-is-rent-seeking-behavior/(accessed on May, 2021).

65. Maruping, L.M.; Venkatesh, V.; Thong, J.Y.L.; and Zhang, X. A risk mitigation framework for information technology projects: A cultural contingency perspective. Journal of Management Information Systems, 36, 1 (2019), 120–157.

66. McKinsey & Company. Blockchain technology for supply chain – A must of a maybe? Mckinsey, 2017. https://www.mckinsey.com/business-functions/operations/our-insights/block chain-technology-for-supply-chainsa-must-or-a-maybe# (accessed on May, 2021).

67. Mearian, Lucas. Chainyard unveil blockchain-based “Trust Your Supplier” network. IBM, 2019. https://www.computerworld.com/article/3429642/ibm-chainyard-unveil-blockchainbased-trust-your-supplier-network.html (accessed on May, 2021).

68. Melville, N.; and Kohli, R. Roadblocks to Implementing Modern Digital Infrastructure: Exploratory Study of API Deployment in Large Organizations. Honolulu: 54th Hawaii International Conference on System Sciences Proceedings. 2021.

69. Mishra, B.K. and Raghunathan, S. Retailer-vs. vendor-managed inventory and brand competition. Management Science, 50, 4 (2004), 445–457.

70. Murphy, K.M.; Shleifer, A.; and Vishny, R.W. Why is rent-seeking so costly to growth? The American Economic Review, 83, 2 (1993), 409–414.

71. Niu, B.; Li, J.; Zhang, J.; Cheng, H. K., and Tan, Y. Strategic analysis of dual sourcing and dual channel with an unreliable alternative supplier. Production and Operations Management, 28, 3 (2019), 570–587.

72. Nordbäck, E.S.; and Espinosa, J.A. Efective coordination of shared leadership in global virtual teams. Journal of Management Information Systems, 36, 1 (2019), 321–350.

73. OECD. The role of digital platforms in the collection of VAT/GST on online sales. 2019. http:// www.oecd.org/tax/consumption/the-role-of-digital-platforms-in-the-collection-of-vat-gst-ononline-sales.pdf (accessed on May, 2021).

74. Oshri, I.; Dibbern, J.; Kotlarsky, J.; and Krancher, O. An information processing view on joint vendor performance in multi-sourcing: the role of the guardian. Journal of Management Information Systems, 36, 4 (2019), 1248–1283.

75. Pardo, T.A.; Tayi, G.K.; Zhang, P.; Fan, J.; and Yu, S. Interorganizational information integration: A key enabler for digital government. Government Information Quarterly, 4, 24 (2007), 691–715.

76. Pomeranz, D. No taxation without information: Deterrence and self-enforcement in the value added tax. American Economic Review, 105, 8 (2015), 2539–2569.

77. Premkumar, G.; Ramamurthy, K.; and Saunders, C.S. Information processing view of organizations: An exploratory examination of fit in the context of interorganizational relationships. Journal of Management Information Systems, 22, 1 (2005), 257–294.

78. Qahri-Saremi, H.; and Turel, O. Ambivalence and coping responses in post-adoptive information systems use. Journal of Management Information Systems, 37, 3 (2020), 820–848.

79. Raju, J.S.; Sethuraman, R.; and Dhar, S.K. The introduction and performance of store brands. Management Science, 41, 6 (June 1995), 957–978.

80. Roberts, N.; and Grover, V. (2012). Leveraging information technology infrastructure to facilitate a firm’s customer agility and competitive activity: An empirical investigation. Journal of Management Information Systems, 28(4), 231–270.

81. Salge, T. O.; Kohli, R.; and Barrett, M. Investing in Information Systems. MIS Quarterly, 39, 1 (2015), 61–90.

82. Sappington, D.E. Incentives in principal-agent relationships. Journal of economic Perspectives, 5, 2 (1991), 45–66.

83. Shapiro, C.; Carl, S.; and Varian, H. R. Information Rules: A Strategic Guide to the Network Economy. Boston: Harvard Business Press, 1998.

84. Shubik, M.; and Levitan, R. Market Structure and Behavior. Cambridge: Harvard University Press, 1980, P. 32.

85. Singh, N.; and Vives, X. Price and quantity competition in a diferentiated duopoly. The RAND Journal of Economics, 15, 4 (Winter 1984), 546–554.

86. Statista. E-commerce share of total global retail sales from 2015 to 2023. https://www.statista. com/statistics/534123/e-commerce-share-of-retail-sales-worldwide/2020 (accessed on May, 2021).

87. Steinfield, C.; Markus, M.L.; and Wigand, R.T. Through a glass clearly: Standards, architecture, and process transparency in global supply chains. Journal of Management Information Systems, 28, 2 (2011), 75–108.

88. Sun Yin, H.H.; Langenheldt, K.; Harlev, M.; Mukkamala, R.R.; and Vatrapu, R. Regulating cryptocurrencies: A supervised machine learning approach to de-anonymizing the bitcoin blockchain. Journal of Management Information Systems, 36, 1 (2019), 37–73.

89. Takahashi, R. How can creative industries benefit from blockchain? McKinsey, 2017. https:// www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/ how-can-creative-industries-benefit-from-blockchain (accessed on May, 2021)

90. Tan, Y. R. Trading virtual goods? Implications on virtual goods developer and consumer. 930 Implications on virtual goods developer and consumer. SSRN, 2020. https://papers.ssrn.com/ sol3/papers.cfm?abstract\_id=3626413 (accessed on May, 2021)

91. Tan, Y. R. and Carrillo, J. The Agency Model for Digital Goods: Strategic Analysis of Dual Channels in Electronic Publishing Industry. Portland: PICMET’14 Conference: Portland International Center for Management of Engineering and Technology; Infrastructure and Service Integration, 2014.

92. Tapscott, D.; and Tapscott, A. The impact of the blockchain goes beyond financial services. Harvard Business Review, 10, (2016), 2–5.

93. Thompson, S.; Whitaker, J.; Atanasov, V.; and Kohli, R. Can We Quantify the Benefits of IT-Enabled Chronic Disease Management? AMCIS: Healthcare Informatics & Health Information Tech (SIGHealth), 2020.

94. Tian, L.; Vakaharia. A.; Tan. Y.; Xu, T. Marketplace, Reseller, or Hybrid: Strategic Analysis of an Emerging E-Commerce Model. Production and Operations Management, 27, 8 (2018), 1595– 1610.

95. Venkatesh, V.; Kang, K.; Wang, B.; Zhong, R.Y.; and Zhang, A. System architecture for blockchain based transparency of supply chain social sustainability. Robotics and Computer-Integrated Manufacturing, 63 (2020), 101896.

96. Walmart. How Shopify helps Walmart Marketplace Sellers. 2020. https://marketplace.walmart. com/shopify/(accessed on May, 2021).

97. Watts, R.; and Zimmerman, J. Agency problems, auditing, and the theory of the firm: Some evidence. The Journal of Law & Economics, 26, 3 (1983), 613–633.

98. Winkler, T.J.; and Wulf, J. Efectiveness of IT service management capability: Value co-creation and value facilitation mechanisms. Journal of Management Information Systems, 36, 2 (2019), 639–675.

99. Wu, D.; Ray, G.; and Whinston, A.B. Manufacturers’ distribution strategy in the presence of the electronic channel. Journal of Management Information Systems, 25, 1 (2008), 167–198.

100. Xu, L.; Chen, J.; and Whinston, A. Oligopolistic pricing with online search. Journal of Management Information Systems, 27, 3 (2010), 111–142.

101. Ziolkowski, R.; Miscione, G.; and Schwabe, G. Decision problems in blockchain governance: Old wine in new bottles or walking in someone else’s shoes? Journal of Management Information Systems, 37, 2 (2020), 316–348.

## About the Authors

Soohyun Cho (scho@business.rutgers.edu) is an Assistant Professor of Accounting and Information Systems at Rutgers University. She earned her Ph.D. in Information Systems from the University of Florida. Dr. Cho’s research interests include online platforms, telecommunication policy, and cybersecurity. Her work has appeared in Information Systems Research and Journal of Management Information Systems.

Kyungha (Kari) Lee (kyunghalee@business.rutgers.edu) is an Assistant Professor in the Accounting & Information Systems Department at Rutgers University. She received her Ph.D. in Accounting Information and Management from Northwestern University. Dr. Lee’s research interests include the incentives and efects of disclosure, the role of information intermediaries, and emerging technology in auditing. Her work has appeared in the Accounting Review, Journal of Accounting Research, Review of Accounting Studies, and Accounting Horizon.

Arion Cheong (acheong@fullerton.edu) is an Assistant Professor of Accounting at the California State University at Fullerton. He is completing his Ph.D. in accounting information systems at Rutgers University. His research and teaching focus on the application of data analytics in accounting and the managerial implication of information technology. During his time at Rutgers University, he has advised numerous firms how to develop analytical models.

Won Gyun No (wgno@business.rutgers.edu) is an Associate Professor of Accounting Information Systems at Rutgers Business School. His research interests includes cybersecurity, blockchain, Extensible Business Reporting Language (XBRL), audit data analytics, and privacy.

Miklos A. Vasarhelyi (miklosv@business.rutgers.edu) is KPMG Distinguished Professor of Accounting Information Systems and Director of the Rutgers Accounting Research Center and Continuous Auditing and Reporting Laboratory at Rutgers University. He holds a Ph.D in MIS from UCLA and an MBA from MIT. Dr. Vasarhelyi has published more than 200 journal articles, 20 books, and directed over 45 Ph.D. theses. He is the editor of the Artificial Intelligence in Accounting and Auditing series and the Journal of Emerging Technologies in Accounting. He is credited with the original continuous audit application and is the leading researcher in this field. He has been recognized as Outstanding Educator of the year by the AAA in 2014, AICPA distinguished scholar in 2018, and the Wasserman awardee by ISACA in 2013.
