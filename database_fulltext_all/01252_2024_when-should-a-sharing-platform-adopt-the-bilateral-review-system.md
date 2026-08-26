---
otero_id: 1252
otero_key: "2B5WEFYW"
title: "When Should a Sharing Platform Adopt the Bilateral Review System?"
authors: "Xuanqi Chen; Gang Li; Shengli Li; Quan Zheng"
year: "2024"
journal: "MIS Quarterly"
doi: "10.25300/misq/2023/17596"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# WHEN SHOULD A SHARING PLATFORM ADOPT THE BILATERAL REVIEW SYSTEM?<sup>1</sup>

Xuanqi Chen and Gang L

School of Management, The State Key Lab for Manufacturing Systems Engineering, The Key Lab of the Ministry of Education for Process Management & Efficiency Engineering, Xi’an Jiaotong University, Xi’an, CHINA {chenxuanqi@stu.xjtu.edu.cn} {glee@mail.xjtu.edu.cn}

Shengli Li Department of Information Management, Peking University, Beijing, CHINA {lishengli@pku.edu.cn}

Quan Zheng International Institute of Finance, School of Management, University of Science and Technology of China, Hefei, CHINA {benzheng@ustc.edu.cn}

The increasing popularity of sharing platforms is raising concerns about a lack of information on the demand side: the cost of serving specific buyers is typically unknown to sellers. To mitigate this concern, some platforms, such as Airbnb, have adopted the bilateral review system (BRS), allowing buyers and sellers to rate each other. This differs from the traditional unilateral review system (URS), which allows only buyers to rate sellers. In this study, we examine how these two review systems impact the operation of a peer-to-peer (P2P) sharing platform, where sellers with different qualities are matched with buyers with different serving costs. Our analysis reveals that under URS, even with perfect seller information, high-quality sellers can still be driven out of the market due to unknown information about the buyer and the “coproduction” nature of the serving cost. This differs from the adverse selection problem often observed in the used car market, for example, where sellers of high-quality products withdraw due to generally unknown product quality. Additionally, we highlight the critical role of the expected buyer cost: When this cost is high, BRS can benefit the platform by alleviating the adverse selection problem; however, when this cost is low, BRS becomes detrimental to the platform. Our analysis also shows that BRS helps buyers but can hurt sellers. However, BRS has the potential to generate a favorable outcome for all parties involved, resulting in a win-win-win situation benefiting the platform, buyers, and sellers. Our results not only shed light on review system design but also provide a plausible explanation for the widespread use of BRS by sharing platforms such as Airbnb, Fiverr, and Turo.

Keywords: Sharing economy, bilateral review system, platform, information asymmetry, adverse selection

## Introduction

In recent years, there has been rapid growth in the P2P sharing market for a large variety of services, such as lodging (e.g., Airbnb, Homeaway), labor sharing (e.g., Fiverr, TaskRabbit), car rentals (e.g., Turo), and ride hailing (e.g., Uber, Lyft). For example, Airbnb reported a gross booking value of \$19.1 billion for the second quarter of 2023, reflecting a 12% increase compared to the same quarter in the previous year (Novet, 2023). A unique feature of the sharing economy is that no ownership transfer occurs, making buyers less likely to protect sellers properties (Kumar et al., 2018). The following example of a complaint from an Airbnb host indicates the risk of serving unknown buyers: “I just had a guest check out and they destroyed my house, causing over \$3500 in damages and lost bookings.”

In P2P sharing markets, the serving cost is jointly determined (“coproduced”) by buyers and sellers (Heinrichs, 2013). Hence, buyer types significantly impact the service outcome. Importantly, individual sellers are not as professional as traditional firms in terms of dealing with irresponsible buyers, aggravating the potential problem (Kumar et al., 2018). This problem is particularly prominent for decentralized platforms (e.g., Airbnb, Vrbo, and Fiverr) that only act as marketplaces and charge a commission for each transaction, forcing sellers to bear the risk of serving buyers. Throughout this paper, we focus on decentralized platforms, where sellers set prices themselves, relying on available buyer information.

To resolve the problem caused by demand-side information asymmetry, platforms typically adopt the bilateral review system (BRS) instead of the traditional unilateral review system (URS). BRS permits not only traditional consumer reviews, as under URS, but also seller reviews (Figure 1). Seller reviews can reveal information about buyers and reduce demand-side uncertainty. More importantly, with BRS, the platform allows sellers to cherry-pick buyers. In other words, while all interested buyers send a request, sellers can select low-cost buyers to pay the posted price, while high-cost buyers may be rejected.

Despite the prevalence of BRS, the effect of review systems on platforms has not been sufficiently examined. On the one hand, BRS can resolve the information asymmetry of buyers and thus promote the efficiency of matching. On the other hand, it may have unintended consequences on sellers’ prices and thus reduce the platform’s commission income. In practice, nearly all decentralized P2P sharing platforms (e.g., Airbnb, Turo, BlaBlaCar) use BRS. Indeed, Fiverr, a leading labor-sharing platform, changed its review system from URS to BRS after sellers complained about malicious buyers.<sup>2</sup> However, more research would be needed to determine the underlying reasons for this.

The findings in the literature are mixed in terms of whether BRS actually improves platform profitability. For instance, while Tunc et al. (2019) show that BRS does not benefit the platform, Ke et al. (2022) indicate the opposite. The preceding discussion motivates us to examine the following questions: When should a decentralized P2P sharing platform adopt BRS? How does BRS impact the decentralized P2P sharing market and its stakeholders (buyers, sellers, and society)?

To address these questions, we developed an analytical model where sellers with a one-unit capacity of heterogeneous quality and buyers with different serving costs are matched on a monopoly sharing platform such as Airbnb. While, in practice, consumer reviews are always offered, the platform’s key concern is whether to enable seller reviews; thus, we compare the two review systems, URS vs. BRS. As the service is coproduced by sellers and buyers in the sharing economy, the serving cost of each matched pair is jointly determined by the buyer’s cost type and the seller’s quality level.

Interestingly, we found that although the seller information is known perfectly under URS, adverse selection can still occur on the seller side; that is, high-quality sellers can be unmatched and driven out of the market. This phenomenon is in stark contrast to the traditional lemon market (e.g., the used car market), where sellers of high-quality products withdraw due to supply-side information asymmetry, i.e., quality uncertainty, see Akerlof (1978). In our paper, the withdrawal of high-quality sellers is due to buyer-side information asymmetry under URS and the coproduction nature of the serving cost. When buyer types are unknown and the expected buyer cost is high, high-quality sellers charge high prices to offset the potential loss of serving high-cost buyers, and that expense discourages buyers from choosing these sellers. However, we reveal that even under URS, high-quality sellers never withdraw in a seller’s market (i.e., more buyers than sellers) or when the expected buyer cost is low (in a buyer’s market). Therefore, we identify the important role of the expected buyer cost and the market structure in determining the matching outcome due to coproduction.

We further show that BRS has two effects on the sharing market compared with URS. First, BRS generates a “shuffle effect” that changes the matching results: high-quality sellers may be unmatched under URS, but they are matched with low-cost buyers under BRS. The reason is that BRS reveals buyer types; therefore, high-quality sellers can cherry-pick low-cost buyers without the risk of being also compelled to serve high-cost buyers. This effect helps high-quality sellers match and alleviates adverse selection. Second, BRS yields a “segmentation effect” because high-quality (low-quality) sellers are matched with low-cost (high-cost) buyers. In this sense, BRS reshapes seller competition. Surprisingly, highquality sellers serving low-cost buyers may charge lower prices than low-quality sellers serving high-cost buyers. This is because all sellers recognize and prefer low-cost buyers, and high-quality sellers thus must compete to attract low-cost buyers by reducing prices.

![](/api/attachments/2B5WEFYW/fulltext/images/6f6e619b93b258ae49da389a1f5c1d4ea9d79a6c8969951659dfd52c2e25a721.jpg)  
Figure 1. Examples of Seller Reviews in the Bilateral Review System

These two effects are intertwined, and the net effect is ambiguous for each player. We find that the expected buyer cost is the primary determinant for the platform to adopt BRS. When the expected buyer cost is low, URS is always better. The reason is that providing buyer information (i.e., BRS) intensifies seller competition for low-cost buyers, reducing sellers’ prices as a whole. Thus, the platform receives less commission due to intense seller price competition. Nevertheless, when the expected buyer cost is high, BRS benefits the platform when the aggregate quality of top sellers is high. By utilizing the screening capabilities of BRS, topnotch sellers can weed out high-cost buyers and be paired with low-cost buyers. The improved matching leads to higher prices charged by these sellers, thereby boosting the platform’s commission income. These findings potentially explain why decentralized P2P platforms widely adopt BRS.

Our results also suggest that revealing buyer types under BRS always benefits buyers but can harm sellers as a whole in a buyer’s market. The intuition is that since sellers prefer lowcost buyers, information transparency induces sellers to engage in intense price competition to capture low-cost buyers. However, when the expected buyer cost is high, BRS can yield a win-win-win outcome for sellers, buyers, and the platform by alleviating the adverse selection problem.

## Literature Review

Our research is primarily based on the literature on two-sided markets and the sharing economy. Previous literature has investigated the market equilibrium of two-sided markets (Gale & Shapley, 1962), surge pricing in on-demand markets (Cachon et al., 2017), the impact of the sharing economy on traditional industries (Jiang & Tian, 2018; Benjaafar et al., 2019), reciprocity and trust (Fradkin et al., 2021), and the adverse selection and moral hazard problem in the two-sided market from a principal-agent perspective (Pavlou et al., 2007). Although demand-side information asymmetry widely exists in two-sided economies, it is not well explored in the literature.

Unlike previous work, we study the review system design of sharing platforms, finding that the information provision scheme and the expected buyer cost jointly determine matching and pricing results as well as stakeholders’ welfare.

Our research relates to adverse selection. According to Akerlof (1978), a lack of product information leads to a “lemon market,” where high-quality sellers can be driven out of the market. This effect has been widely studied in various research areas, including financing (Myers & Majluf, 1984) and the labor market (Shapiro & Stiglitz, 1984). In contrast to traditional adverse selection, we show that buyer-side information asymmetry (i.e., unknown buyer types) can also indirectly lead to seller-side adverse selection (i.e., cross-side adverse selection). We reveal that this phenomenon is driven by the unique “coproduction” feature of the serving cost in P2P sharing markets.

Our paper is also relevant to the directed search and matching problem in labor markets, as addressed in previous research (Lagos, 2000; Montgomery, 1991). In this context, firms with a limited number of job openings publicly post wages to attract workers. Additionally, firms have the discretion to reject applied workers (Shi, 2002). Ultimately, when a worker and a firm mutually select each other, they constitute matching pairs. In this field of research, one typical assumption is that matching cannot be efficiently coordinated, resulting in coordination friction. This means that numerous workers can choose the same firm with limited job openings, which, in turn, leaves positions at other firms unfilled (Burdett et al., 2001; Shi, 2002). Our setting shares similarities, as sellers with limited capacity post prices to match with buyers and, under BRS, sellers have the ability to screen buyers and reject those with high costs. However, unlike traditional labor markets, orchestrating the matching process on a sharing platform requires prompt matching once a buyer applies to a seller. This coordination significantly reduces the friction arising from multiple buyers simultaneously applying to the same sellers. Incorporating this coordination, we investigate the impact of the platform’s information provision policy on matching outcomes and unveil the cross-side adverse selection problem.

Another related stream of research considers online reviews as an information tool that can be used to reveal the quality or fitness of products. For example, Chen and Xie (2008) modeled the online product review as a method to show the degree to which the products match consumers’ needs. Jiang and Guo (2015) analyzed the design of review systems and the resulting pricing strategies. Kwark et al. (2014) indicated that providing product information on different dimensions could soften or intensify the upstream competition. Liu et al. (2017) focused on both online reviews and sales volume information, showing that these two kinds of information mutually enhance the firm’s profit. Li (2017) showed the conditions under which a profit-driven firm would prefer to reveal product reviews. However, these studies only considered online consumer reviews, referred to as URS in this paper. Our work highlights buyer-side information asymmetry and the role of seller reviews. We show that without seller reviews, providing online buyer reviews alone in P2P sharing markets can still lead to the adverse selection problem. We also characterize the conditions under which BRS mitigates adverse selection and benefits the platform.

Finally, our work contributes to the limited research on BRS. Some empirical research has investigated this topic. For example, Ye et al. (2014) analyzed changes in the design of BRS on eBay, which reduces a seller’s ability to retaliate against a buyer. Their findings emphasize the importance of a carefully designed BRS in ensuring the success of online platforms. Mayya et al. (2021) analyzed the impact of forgoing screening on Airbnb hosts. However, analytical works in this stream are relatively scarce. Jin et al. (2022) discussed BRS in the context of a ride-hailing service where the platform sets the price of each transaction, and drivers (i.e., sellers) are homogeneous in their quality. They found that under BRS, sellers can overselect buyers, which ends up hurting sellers. In contrast, we assume a decentralized platform where sellers set prices and the quality of sellers differs. For such a decentralized platform, we show that URS can lead to cross-side adverse selection, which is alleviated by BRS.

Our work is most closely related to Ke et al. (2022) and Tunc et al. (2019). Ke et al. (2022) considered a P2P market where buyers simultaneously arrive and rejected buyers cannot reapply, which leads to coordination friction. They found that BRS softens seller competition and induces high-quality sellers to charge lower prices than low-quality sellers only with incomplete market coverage. Different from their setting, we assume that buyers arrive and get matched sequentially, as this is true in most cases on P2P platforms. We show that BRS intensifies the competition, causing highquality sellers to charge lower prices than low-quality sellers, even with complete market coverage. Tunc et al. (2019) found that BRS always harms the platform and hurts society under certain conditions in a seller’s market and that BRS leads to the same platform profit and social welfare in a buyer’s market. However, their results are based on two key assumptions: a linear cost function with a bounded buyer cost parameter and two quality groups of sellers only. Contrary to Tunc et al. (2019), we consider fully heterogeneous quality sellers, a fairly general cost structure (i.e., both linear and convex functions), and an unbounded buyer cost parameter; in addition, we focus on the buyer’s market. These realistic features lead to different results, such as that BRS can benefit the platform, partially justifying the wide adoption of BRS in practice.

## Model Setup

The market consists of a monopoly platform with ?? sellers and ?? buyers. The monopoly platform (“it”) charges a commission rate $\zeta$ on each transaction. Following previous research (Li et al., 2018; Benjaafar et al., 2019) as well as real-world platform policies (Adaramola, 2022; Stacey, 2023), we assume that the commission rate is exogenously given. We distinguish two types of markets: the buyer’s market and the seller’s market. In the buyer’s market, there are more sellers than buyers $( M > N )$ , while in the seller’s market, buyers outnumber sellers $( M < N )$ . We focus on the buyer’s market because it dominates in most cases and is stable on Airbnb. In the Extension section, we explore the seller’s market.

Sellers (generically referred to here as “she”) are heterogeneous in quality $q _ { i }$ with $q _ { 1 } > q _ { 2 } > \cdots > q _ { M } ;$ that is, sellers are ordered in decreasing quality. To keep the model simple while conveying the main insights, we assume that each seller ?? (with the quality $q _ { i } )$ has only one unit of capacity to serve one buyer. For instance, a host on Airbnb can only accommodate one buyer. Seller ?? sets the price $p _ { i } ^ { \alpha }$ to maximize her profit. We use ?? ∈ {??, ??} to indicate the case of URS or BRS.

The utility function of the buyer (generically referred to here as “he”) is $U _ { i } = v _ { 0 } + q _ { i } - p _ { i } ^ { \alpha }$ if the buyer chooses seller ?? with quality $q _ { i }$ and price $p _ { i } ^ { \alpha }$ , where $v _ { 0 }$ is the buyers’ basic utility of joining the P2P market. We assume that $v _ { 0 }$ is high enough to induce all ?? buyers to join the market. In practice, the sharing economy is popular among consumers, indicating that $v _ { 0 }$ might be high in real-world settings. Incomplete market coverage is explored in Appendix D. We assume the sequential arrival of buyers and assume that once a buyer selects a seller, the two are matched under URS but the buyer can be refused under BRS, which covers most cases on P2P decentralized platforms (e.g., Airbnb, Fiverr, and Turo). This also aligns with the practice on Airbnb where sellers accept or reject a request as soon as possible.<sup>3</sup>

Buyers differ in terms of the cost to serve them, which can be either high or low: $\omega \in \{ h , l \}$ . Specifically, the serving cost of the matched pair of a type-?? buyer and a seller of quality $q _ { i }$ is given by $\theta _ { \omega } f \left( q _ { i } \right)$ (Ke et al., 2022), where $f ( q _ { i } ) = q _ { i } ^ { \gamma }$ , with $\gamma \in \{ 1 , 2 \}$ , is a linear or convex function of seller quality $q _ { i } .$ . The linear function (Tunc et al., 2019; Ke et al., 2022) and the convex function (Lin et al., 2020; Netessine & Taylor, 2007) are both used in the literature. Due to the “coproduction” nature of service on P2P sharing platforms (Heinrichs 2013), the serving cost $\theta _ { \omega } f \left( q _ { i } \right)$ is related to both $\theta _ { \omega }$ (defined as the buyer serving cost parameter) and the seller’s quality $q _ { i } .$ In practice, sellers contribute their time and properties but require a buyer’s cooperation to provide the service. All else being equal, highquality sellers have more expensive properties or greater opportunity costs and thus incur higher costs to serve buyers. Meanwhile, high-cost buyers impose a multiplier effect on the serving cost, and $\theta _ { \omega }$ measures the buyer-side impact on this cost. We assume that ?? fraction of buyers is low-cost with $\theta _ { l } ,$ and $1 - \rho$ is high-cost with $\theta _ { h } ,$ , where $0 < \rho < 1$ and $\theta _ { h } > \theta _ { l } ,$ i.e., buyers with $\theta _ { h }$ are more costly to serve. The number of low-cost and high-cost buyers are denoted by $N _ { l } = N \rho$ and $N _ { h } = N ( 1 - \rho )$ , respectively. We consider more than two types of buyers in Appendix D. For simplicity, $\theta _ { l }$ is normalized to zero and thus $\theta _ { l } f ( q _ { i } ) = 0$ We relax this zero-cost assumption in Appendix D and show that our results qualitatively hold. To simplify the notation, we denote $\theta _ { h } = \theta$ When buyer types are unknown, sellers serve a mixture of two types of buyers, and the expected serving cost is $( \rho \theta _ { l } +$ $( 1 - \rho ) \theta _ { h } ) f ( q _ { i } ) = ( 1 - \rho ) \theta f ( q _ { i } )$ . We label $( 1 - \rho ) \theta$ as the expected buyer serving cost parameter (“expected buyer cost” for short), which measures the buyer-side impact on $( 1 - \rho ) \theta f ( q _ { i } )$ when the buyer information is unknown. A summary of the notation can be found in Appendix A.

## URS

Following prior research (Chen & Xie, 2005), we assume that consumer reviews provide perfect information about seller quality; this assumption allows us to focus on the platform’s binary information disclosure decision. We show that even if perfect seller information is available, the adverse selection problem can still occur due to demand-side information asymmetry. Based on consumer reviews, buyers learn about sellers’ quality, but sellers do not know the buyer types if there are no seller reviews of buyers.

## Assumption 1: Buyers arrive sequentially.

Buyers arrive sequentially on the platform, as in most cases on Airbnb, Fiverr, and Turo. This realistic assumption enables us to circumvent the market friction discussed in previous studies (Ke et al., 2022) and focus solely on the impact of information asymmetry, which serves as the primary driver of our intriguing findings. Upon arrival, buyers choose the available seller who offers the highest utility. Since no buyer information is available, sellers cannot cherry-pick buyers. Therefore, they accept any requests and get matched with buyers; that is, buyers are ex ante homogeneous for sellers. In our setting, there is no search friction. We present the game sequence in Figure 2.

## BRS

Equipped with BRS, sellers can recognize buyer types. We make Assumption 2 following Tunc et al. (2019) and Ke et al. (2022).

Assumption 2: Information structure under BRS: Seller reviews perfectly indicate buyer types, i.e., high- or low-cost; buyer reviews perfectly indicate seller quality.

Assumption 2 is consistent with the literature on BRS. Meanwhile, perfect information revelation allows us to isolate the effect of information asymmetry on the buyer side and compare BRS with URS in a transparent way. This assumption is relaxed in Appendix D to showcase the robustness of our results.

## Assumption 3: Custom prices are available under BRS.

Under BRS, sellers set posted prices for all buyers and offer custom prices to low-cost buyers upon request; sellers also decide whether to reject or accept such requests based on the buyer type. The custom price option merits discussion. On Airbnb, sellers are specifically allowed to “set a custom price for a guest who has sent a booking inquiry,” as stated on the official website (Airbnb, 2022), and the custom price is sometimes offered by sellers to attract buyers (Clifford, 2020). Note that we define and discuss two cases in the Analysis section: same rank vs. reverse rank. For the reverse rank case, where the most interesting results arise, custom prices do not play any role; that is, the equilibrium is the same even without custom pricing. This demonstrates that custom pricing is not the driving force behind our main results. It is worth mentioning that Assumption 3 ensures the existence of a pure strategy equilibrium in the same rank case, allowing us to compare our results with those in the literature.

![](/api/attachments/2B5WEFYW/fulltext/images/7dc2651c0ab2311ee72a8a4f1a0601c768994f55c6dcb195b1dba467a17aed5b.jpg)

<table><tr><td>Step 1: Sellers set the prices and the custom prices simultaneously</td><td>Step 2: Buyers sequentially arrive to submit a request; sellers decide whether to accept the requested buyer</td></tr><tr><td colspan="2">Figure 3. Game Sequence under BRS</td></tr></table>

We show the game sequence in Figure 3. In Step 1, sellers set posted prices and custom prices. Requests and matching occur in Step 2: Each buyer arrives sequentially on the platform to submit a request to a seller. Low-cost buyers can also request a custom price, taking into account the seller’s posted price, the buyer’s expectation of receiving the custom price, and whether he will be accepted. Then, the selected seller decides whether to accept the buyer. The matching occurs once the seller accepts the buyer.<sup>4</sup>

## Analysis

This section analyzes the equilibrium outcomes under URS and BRS, respectively.

## Analysis of URS

Because nearly all platforms post consumer reviews to reveal seller information, we regard URS as the benchmark and focus on demand-side information asymmetry. We use backward induction to solve the Nash equilibrium under URS. In Step 2, ?? buyers arrive sequentially and match with sellers to maximize their utility. Next, we study how sellers engage in price competition in Step 1. To do so, we first introduce the concept of “matching ability.” Note that the highest utility that seller ?? can offer by obtaining a nonnegative profit is:

$$
\begin{array}{c} {m a x U _ {i} \big (p _ {i} ^ {U} \big) = v _ {0} + q _ {i} - p _ {i} ^ {U}} \\ {\mathrm{s.t.} \pi_ {i} = (1 - \zeta) p _ {i} ^ {U} - (1 - \rho) \theta f (q _ {i}) \ge 0.} \end{array}\tag{1}
$$

Solving Problem (1), we obtain max $U _ { i } ( p _ { i } ^ { U } ) \leq v _ { 0 } + Q _ { m } ( i )$ where

$$
Q _ {m} (i) \stackrel {\Delta} {=} q _ {i} - \frac {(1 - \rho) \theta f (q _ {i})}{1 - \zeta}.\tag{2}
$$

Since all sellers compete for matching in a buyer’s market, they would offer a high level of utility to attract buyers. Therefore, the seller with a higher $Q _ { m } ( i )$ has a greater advantage in attracting buyers, and so we refer to $Q _ { m } ( i )$ as the matching ability of seller ?? . The following numerical examples sort the matching ability of sellers.

Example 1: Consider three sellers with quality $q _ { 1 } = 1 . 5$ $q _ { 2 } = 1 . 2$ , and $q _ { 3 } = 1$ as shown in Figure 4. Suppose $Q _ { m } ( i ) = q _ { i } - \frac { 1 } { 2 } ( 1 - \rho ) \theta q _ { i } ^ { 2 }$ . There are two interesting cases:

The same rank case: A low expected buyer cost $( 1 - \rho ) \theta = 0 . 5$ results in $Q _ { m } ( i ) = 0 . 9 4 , 0 . 8 4 , 0 . 7 5$ respectively, for seller $i = { 1 , 2 , 3 }$ . Since $Q _ { m } ( 1 ) >$ $Q _ { m } ( 2 ) > Q _ { m } ( 3 ) , Q _ { m } ( i )$ and $q _ { i }$ are in the same rank order in Figure 4a

The reverse rank case: A high expected buyer cost $( 1 - \rho ) \theta = 1$ results in $Q _ { m } ( i ) = 0 . 3 8 , 0 . 4 8 , 0 . 5$ respectively, for seller $i = { 1 , 2 , 3 }$ . Since $Q _ { m } ( 1 ) <$ $Q _ { m } ( 2 ) < Q _ { m } ( 3 ) , \ Q _ { m } ( i )$ and $q _ { i }$ are in the reverse rank order in Figure 4b.

![](/api/attachments/2B5WEFYW/fulltext/images/a44752e354ed0ef21b2263a1fbe488dfe9917b410ddd98d1b64fde13dfffa600.jpg)

Figure 4. Examples of Different Rank Scenarios  
![](/api/attachments/2B5WEFYW/fulltext/images/4d2b23c11b26e254f375b205ad2640d994fceb4c8f20809fe938f42e92887a30.jpg)

For colloquial convenience, we refer to “reverse rank” (“same rank”) as the case where matching ability $Q _ { m } ( i )$ decreases (increases) in quality, $\mathrm { i . e . , ~ } Q _ { m } ( 1 ) < Q _ { m } ( 2 ) <$ $\cdots < Q _ { m } ( M ) ( Q _ { m } ( 1 ) > Q _ { m } ( 2 ) > \cdots > Q _ { m } ( M ) )$ . Appendix D discusses general rank cases and further highlights that beyond the explicit feature of “quality,” the matching outcome is determined by the implicit feature of “matching ability” in a two-sided market with coproduction serving costs. We discuss the same rank case in the Extension section. In the subsequent analysis, unless specified otherwise, we focus on the reverse rank case to elaborate on our main interesting findings transparently. To break ties, we assume that when a buyer is indifferent between sellers, the buyer chooses the seller with the higher matching ability.<sup>5</sup> We then propose the following. Proofs are relegated to Appendix B.

Proposition 1: Under URS, reverse rank occurs when the expected buyer cost is high enough, i.e., $\begin{array} { r } { ( 1 - \rho ) \theta > \frac { 1 - \zeta } { f ^ { \prime } ( q _ { M } ) } . } \end{array}$ With reverse rank, ?? sellers $i \in \{ M - N + 1 , \ldots , \dot { M } \}$ are matched and charge the price $p _ { i } ^ { U * } = q _ { i } - \left\lfloor q _ { M - N } - \frac { } { } \right.$ $\frac { ( 1 - \rho ) \theta f ( q _ { M - N } ) } { 1 - \zeta } \biggr ] .$ , while high-quality sellers are driven out of the market.

Proposition 1 presents the equilibrium under URS in the reverse rank case. Seller $i \stackrel {  } { \in } \{ M - N + 1 , \ldots , M \}$ , whose matching ability is among the ?? highest, can get matched.

Matched seller ?? charges $p _ { i } ^ { U * } = q _ { i } - \Big [ q _ { M - N } -$ $\frac { ( 1 - \rho ) \theta f ( q _ { M - N } ) } { 1 - \zeta } \biggr ]$ such that all buyers obtain the same utility $U _ { i } = v _ { 0 } + Q _ { m } ( M - N )$ . This offered utility excludes seller $i = M - N .$ . The withdrawal of high-quality sellers can be seen in Figure 5. One may believe that high-quality sellers will always be matched (Tunc et al., 2019). However, we find that in the P2P sharing market, high-quality sellers can be driven out of the market with buyer-side information asymmetry when the expected buyer cost is high enough (i.e., $\begin{array} { r } { ( 1 - \rho ) \theta > \frac { 1 - \zeta } { f ^ { \prime } ( q _ { M } ) } ) } \end{array}$ . The intuition is as follows. In a P2P sharing market, the service is coproduced by both sides. Thus, the matching ability of each seller in Equation (2) hinges on the expected buyer cost $( 1 - \rho ) \theta$ and the seller’s quality $q _ { i }$ . When $( 1 - \rho ) \theta$ is high and buyer types are unknown, high-quality sellers charge high prices to offset the potentially high serving cost, which tremendously reduces the competitiveness of high-quality sellers and discourages buyers from choosing them.

This finding might be particularly relevant for decentralized P2P sharing platforms: On Airbnb, sellers are faced with the prospect of problematic guests, who dramatically increase serving costs through additional cleaning fees, property damage, and intangible damages (HostGPO, 2020). Hosts have reported cases of guests organizing gatherings that have incurred significant expenses, prompting Airbnb to formally forbid such events (Liang, 2022). Similarly, on Fiverr, sellers have voiced complaints about difficult buyers. For instance, one seller complained: “Needless to say, (bad buyers) are many and are running wild reining havoc and being a nightmare to sellers all over the platform.” Eventually, Fiverr changed from URS to BRS in 2018. With our notation, these situations mean that $( 1 - \rho ) \theta$ might be high; thus, highquality sellers may withdraw under URS.

Interestingly, Proposition 1 shows that in the P2P sharing market, even when the seller information is perfect under URS, high-quality sellers are still driven out of the market if the expected buyer cost $( 1 - \rho ) \theta$ is high and buyer information is unknown to sellers. This differs from the conventional wisdom about adverse selection, which suggests that the information asymmetry and the withdrawal of high-quality agents are always on the same side of the market. For example, in the used-car market, sellers of highquality products may be driven out of the market due to uncertainty regarding product quality (Akerlof, 1978). Analogously, in the insurance market, uncertainty regarding buyer-side information may drive low-risk buyers out of the market. In our paper, adverse selection cannot be explained by existing forces on the seller side (e.g., as in the used car market) or on the buyer side $( \mathrm { e . g . }$ , as in the insurance market) alone because, under URS, information uncertainty (regarding buyers) and adverse selection (on sellers) are on different sides of the two-sided market. Besides information asymmetry, the other joint force is coproduction from both sides. We refer to this new phenomenon as “cross-side adverse selection.”

This cross-side adverse selection tends to occur when (1) the commission fee $\zeta$ increases or (2) the lowest quality $q _ { M }$ increases when $f ( q )$ is convex $( \mathrm { i . e . , } f ( q ) = q ^ { 2 } )$ . When $\zeta$ increases, the serving cost weighs more heavily on the profit function $\pi = ( 1 - \zeta ) p _ { i } - ( 1 - \rho ) \theta f ( q _ { i } )$ such that highquality sellers stand to lose more due to their higher costs and tend to withdraw. Similarly, as $q _ { M }$ increases, sellers are of a (weakly) higher quality and thus suffer more due to higher costs with a convex cost function. Therefore, reverse rank tends to occur. Notably, Tunc et al. (2019) assume a linear serving cost function $f ( q ) = q$ and a low cost parameter $\theta < 1 - \zeta$ . This assumption never satisfies the condition in Proposition 1. On the contrary, we allow for $\theta >$ $1 - \zeta$ and $f ( q ) = q ^ { 2 }$ ， and either of these two generalizations leads to the reverse rank case.<sup>6</sup> By relaxing the assumption about the cost function, we find that highquality sellers may be driven out under URS.

## Analysis of BRS

Buyers arrive sequentially and choose sellers who maximize their utility $U _ { i } = v _ { 0 } + q _ { i } - p _ { i } ^ { B }$ . Analogously, we introduce the “matching ability of serving the low-cost buyer” and “matching ability of serving the high-cost buyer:”

$$
Q _ {l} (i) \triangleq q _ {i} - \frac {\theta_ {l} f (q _ {i})}{1 - \zeta} = q _ {i}\tag{3}
$$

$$
Q _ {h} (i) \stackrel {\Delta} {=} q _ {i} - \frac {\theta_ {h} f (q _ {i})}{1 - \zeta} = q _ {i} - \frac {\theta f (q _ {i})}{1 - \zeta}\tag{4}
$$

These definitions are parallel to that of Equation (2) under URS. By the same token, the highest utility that seller ?? can offer a low-cost (high-cost) buyer is $v _ { 0 } + Q _ { l } ( i ) ( v _ { 0 } + Q _ { h } ( i ) )$ Note that reverse rank (Proposition 1) implies that $Q _ { h } ( M ) >$ $Q _ { h } ( M - 1 ) > \cdots > Q _ { h } ( 1 )$ ; that is, higher-quality sellers have a lower matching ability to serve high-cost buyers. However, higher-quality sellers have a higher matching ability to serve low-cost buyers through cherry-picking, $\begin{array} { r l } { \mathrm { i . e . , } } & { { } Q _ { l } ( 1 ) > } \end{array}$ $Q _ { l } ( 2 ) > \cdots > Q _ { l } ( M )$ . We obtain the following:<sup>7</sup>

## Proposition 2: In equilibrium with BRS, the following hold.

(i) The $N _ { l }$ high-quality sellers $i \in \{ 1 , \ldots , N _ { l } \}$ charge $p _ { i } ^ { B * } = q _ { i } - q _ { N _ { l } + 1 }$ and get matched with the low-cost buyers; the $N _ { h }$ low-quality sellers $i \in \{ M - N _ { h } +$ $1 , \ldots , M \}$ charge $\begin{array} { r } { p _ { i } ^ { B * } = q _ { i } - \biggl [ q _ { M - N _ { h } } - \frac { \theta f \bigl ( q _ { M - N _ { h } } \bigr ) } { 1 - \zeta } \biggr ] } \end{array}$ and get matched with the high-cost buyers. The equilibrium remains the same even without custom prices.

(ii) High-quality seller $i _ { h } \in \{ 1 , \dots , N _ { l } \}$ charges a lower price than that of low-quality seller $i _ { l } \in \{ M - N _ { h } +$ $1 , \ldots , M \}$ (i.e., $p _ { i _ { h } } ^ { B * } < p _ { i _ { l } } ^ { B * }$ but $q _ { i _ { h } } > q _ { i _ { l } } )$ if the quality gap $q _ { i _ { h } } - q _ { i _ { l } }$ between these two sellers is small (i.e., $q _ { i _ { h } } -$ $\begin{array} { r } { q _ { i _ { l } } < q _ { N _ { l } + 1 } - q _ { M - N _ { h } } + \frac { \theta f \left( q _ { M - N _ { h } } \right) } { 1 - \zeta } \dag . } \end{array}$

Figure 6 illustrates the matching result stated in Proposition 2.

![](/api/attachments/2B5WEFYW/fulltext/images/e331b8f294047939b44699e02db149b33c3f74537bd7157e839f539ef53f172c.jpg)

Sellers $i \in \{ 1 , \ldots , N _ { l } \}$ serve low-cost buyers because their matching abilities $Q _ { l } ( i )$ are the $N _ { l }$ highest; these sellers thus distinguish themselves in the competition for low-cost buyers. Sellers $i \in \{ M - N _ { h } + 1 , \ldots , M \}$ serve $N _ { h }$ high-cost buyers because their matching abilities $Q _ { h } ( i )$ are the $N _ { h }$ highest among the remaining sellers $i \in \{ N _ { l } + 1 , \ldots , M \}$ . The highquality sellers charge $p _ { i } ^ { B * } = q _ { i } - q _ { N _ { l } + 1 }$ to match with the low-cost buyers and offer the same utility $v _ { 0 } + q _ { N _ { l } + 1 }$ . This offered utility prevents the other sellers from attracting lowcost buyers. Similarly, the low-quality sellers charge $p _ { i } ^ { B ^ { * } } =$ $\begin{array} { r } { q _ { i } - \bigg [ q _ { M - N _ { h } } - \frac { \theta f \left( q _ { M - N _ { h } } \right) } { 1 - \zeta } \bigg ] } \end{array}$ to match with the high-cost buyers and offer the same utility $v _ { 0 } + Q _ { h } ( M - N _ { h } )$ . This offered utility $v _ { 0 } + Q _ { h } ( M - N _ { h } )$ excludes other sellers from competing for the high-cost buyers.

Interestingly, as shown in Figure 6, low- and high-quality sellers are matched, leaving sellers of intermediate quality unmatched. This is because intermediate-quality sellers are outperformed by high-quality sellers through the cherrypicking of low-cost buyers and low-quality sellers in terms of providing low prices to high-cost buyers. This matching pattern is supported by real-world practices, as observed in the context of Airbnb. On the one hand, most high-quality houses listed on Airbnb are in high demand and often hard to book; on the other hand, low-quality accommodations tend to attract bookings through their low prices.<sup>8</sup> Appendix B shows that the withdrawal of intermediate-quality sellers is efficient because the efficiency of matching depends on both the seller quality and the buyer type. That is, in contrast to the traditional perspective, which only examines the quality, higher seller quality does not always mean higher efficiency in a two-sided market with coproduction costs. Besides, Proposition 2(i) also shows that the equilibrium is the same even without custom pricing, indicating that custom pricing is not the driving force of our most interesting results.

We identify two effects of BRS. First, we find that the matching outcome changes: High-quality sellers are matched with low-cost buyers under BRS, but they are not matched under URS. We refer to this as the “shuffle effect.” Recall from Proposition 1 that high-quality sellers can lose their competitive edge and withdraw under URS. Under BRS, information asymmetry is resolved, allowing high-quality sellers to cherry-pick low-cost buyers in order to reduce their serving costs substantially. These lower serving costs induce high-quality sellers to charge an attractive price and get matched with low-cost buyers.

Second, BRS has a “segmentation effect.” Note that under URS, sellers serve a mixture of low-cost and high-cost buyers by offering $v _ { 0 } + Q _ { m } ( M - N )$ to exclude seller $i = M - N$ By contrast, BRS segments buyers into high-cost and low-cost types, and high-cost (low-cost) buyers obtain utility $v _ { 0 } +$ $Q _ { h } ( M - N _ { h } ) \ ( v _ { 0 } + q _ { N _ { l } + 1 } )$ from low-quality (high-quality) sellers who exclude seller $i = M - N _ { h } \left( i = N _ { l } + 1 \right)$ . In this sense, seller competition is reshaped by BRS.

Unexpectedly, as Proposition 2(ii) states, low-cost buyers can enjoy high-quality service while paying less. Also, high-cost buyers have to pay more for the low-quality service (i.e., $p _ { i _ { h } } ^ { B * } < p _ { i _ { l } } ^ { B * }$ but $q _ { i _ { h } } > q _ { i _ { l } } )$ when the quality gap between high quality $q _ { i _ { h } }$ and low quality $q _ { i _ { l } }$ is small. This indicates that high-quality sellers subsidize low-cost buyers in order to attract them. This is because BRS reveals buyer types, and all sellers prefer and compete for low-cost buyers. As a result, high-quality sellers outperform others in attracting low-cost buyers and may charge lower prices due to competition.

In summary, we have identified two effects of BRS in the reverse rank case. However, the net effect is ambiguous for specific stakeholders, depending on the nature of the market.

## Comparison: URS vs. BRS in the Reverse Rank Case

In this section, we compare the impact of URS and BRS in the reverse rank case $\begin{array} { r } { ( \mathrm { i . e . , } ( 1 - \rho ) \theta > \frac { 1 - \zeta } { f ^ { \prime } ( q _ { M } ) } ) } \end{array}$ to present our most interesting findings. We label top sellers as those with the $N _ { l }$ highest qualities and denote their aggregate quality by $\textstyle \sum _ { i = 1 } ^ { N _ { l } } q _ { i }$

## Platform Profit

We compare the platform profit under URS $( \pi _ { U } )$ and BRS $\left( \pi _ { B } \right)$ , which is given by the commission income of all transactions $\zeta \sum _ { i } p _ { i } ^ { \alpha }$

Proposition 3: With reverse rank, BRS makes the platform better off when the aggregate quality of top sellers is high $\begin{array} { r } { ( i . e . , \sum _ { i = 1 } ^ { N _ { l } } q _ { i } > A _ { 1 } ) . } \end{array}$ . Otherwise, the platform cannot become better off under BRS. Moreover, $A _ { 1 }$ increases in ??.

To grasp the intuition, we offer the following:

$$
\frac {\pi_ {B} - \pi_ {U}}{\zeta} = \underbrace {\sum_ {i = 1} ^ {N _ {l}} q _ {i} - \sum_ {i = M - N + 1} ^ {M - N _ {h} + 1} q _ {i}} _ {\text {shuffle effect}} - \underbrace {\left[ N _ {l} q _ {N _ {l} + 1} + N _ {h} Q _ {h} (M - N _ {h}) - N Q _ {m} (M - N) \right]} _ {\text {segmentation effect}}.\tag{5}
$$

Equation (5) presents the impact of the shuffle effect and the segmentation effect on the platform profit. Recall that the segmentation effect can harm the platform profit because it intensifies the seller competition for low-cost buyers, leading to subsidization (Proposition 2(ii)) and a drop in overall prices as well as commission income. Further, the aggregate quality of top sellers $\textstyle \sum _ { i = 1 } ^ { N _ { l } } q _ { i }$ only affects the shuffle effect and does not factor into the segmentation effect. When $\textstyle \sum _ { i = 1 } ^ { N _ { l } } q _ { i }$ is high, the shuffle effect is strong enough to match low-cost buyers with high-quality sellers who charge higher prices because of their higher quality, which benefits the platform. In practice, Airbnb has launched a list called “Airbnb Plus” containing top sellers who are inspected in person to guarantee their high quality (Al-Saad, 2019). Similarly, Fiverr’s editorial team manually reviews the best-performing sellers and recognizes them as “Top Rated Sellers” to indicate their high quality (Timmers, 2022). Such recognition identifies top sellers who provide high-quality services in the aggregate $\begin{array} { r } { ( \mathrm { i . e . , } \sum _ { i = 1 } ^ { N _ { l } } q _ { i } > A _ { 1 } ) } \end{array}$ . In this case, BRS can benefit the platform in line with our predictions.

Proposition 3 suggests that the ability of BRS to benefit the platform is limited when high-cost buyers become more costly to serve $( \mathrm { i } . \mathrm { e } . , A _ { 1 }$ increases in ?? ), conditional on the reverse rank case. Recall from Propositions 1 and 2 that the prices of matched sellers under URS and BRS weakly increase in $\theta ^ { 9 } .$ This is because as $\theta$ increases, the matched sellers raise their prices—excluding seller $i = M - N$ under URS and seller $i = M - N _ { h }$ under BRS with weakened matching abilities $Q _ { m } ( M - N )$ and $Q _ { h } ( M - N _ { h } )$ . Hence, the price competition is softened, which benefits the platform in both URS and BRS. Note that the excluded seller has a higher quality under URS than under BRS due to the segmentation effect $( { \mathrm { i . e . , } } f ( q _ { M - N } ) > f \bigl ( q _ { M - N _ { h } } \bigr ) )$ . Together with the coproduction nature, the benefit of a higher ?? is stronger under URS, and the platform thus tends to favor URS when $\theta$ increases. <sup>10</sup> Appendix B also analyzes the impact of $\dot { \rho }$ on different stakeholders.

## Welfare

We now examine the overall welfare. Seller profit is defined as the aggregate profit of all sellers and is given by $\Sigma _ { i } [ ( 1 - \bar { \zeta } ) \bar { p } _ { i } ^ { \alpha } - \bar { \theta _ { \omega } f } ( q _ { i } ) ]$ , where $( 1 - \zeta ) p _ { i } ^ { \alpha }$ is the income, and $\theta _ { \omega } f ( q _ { i } )$ is the serving cost. We denote the aggregate seller profit as $\Pi _ { \alpha } , \alpha \in \{ U , B \}$ . Also, buyer surplus $C S _ { \alpha }$ equals the sum of buyer utility $\textstyle \sum _ { i } U _ { i } .$ . Furthermore, we use $S W _ { \alpha }$ to denote social welfare as the sum of seller profit, consumer surplus, and platform profit.

Proposition 4: With reverse rank, BRS always benefits buyers. It harms sellers when top sellers provide low aggregate quality services (i.e., $\textstyle \sum _ { i = 1 } ^ { N _ { l } } q _ { i } < A _ { 2 } )$ and benefits sellers when $\begin{array} { r } { \sum _ { i = 1 } ^ { N _ { l } } q _ { i } > A _ { 2 } } \end{array}$ . Moreover, $A _ { 2 }$ increases in ??.

Conventional wisdom suggests that buyers are typically worse off if sellers know buyer information and implement price discrimination against them. Surprisingly, Proposition 4 indicates that the opposite may also be true: BRS always benefits buyers as a whole but can harm sellers. Obviously, buyers benefit from the shuffle effect. Regarding the segmentation effect, although high-cost buyers may be harmed due to the higher prices, the benefit to low-cost buyers (i.e., the intensified competition and subsidization) always dominates. Hence, buyers are better off as a whole under BRS.

As for sellers, although the shuffle effect favors them, the segmentation effect can harm low-quality sellers who are compelled to serve high-cost buyers. Proposition 4 shows that when the aggregate quality of top sellers is low (i.e., $\textstyle \sum _ { i = 1 } ^ { N _ { l } } q _ { i } < A _ { 2 } )$ , the shuffle effect is dominated by intensified competition for low-cost buyers, and sellers are thus harmed in the aggregate. Moreover, recalling that a higher ?? softens seller competition and benefits sellers, and given that this benefit is stronger under URS than that under BRS, sellers tend to favor URS when buyers are more costly to serve (i.e., $A _ { 2 }$ increases, or the range $\textstyle \sum _ { i = 1 } ^ { N _ { l } } q _ { i } < A _ { 2 }$ expands when ?? becomes higher) with reverse rank.

Next, we verify that BRS improves social welfare and summarize the win-win-win outcome that benefits all parties involved.

Corollary 1: With reverse rank, BRS always improves social welfare compared to URS. Also, BRS generates a win-win-win outcome for sellers, buyers, and the platform if top sellers provide high aggregate quality services (i.e., $\textstyle \sum _ { i = 1 } ^ { N _ { l } } q _ { i } >$ ??????{ $\left. A _ { 1 } , A _ { 2 } \right\}$ . Moreover, ?????? $\left[ A _ { 1 } , A _ { 2 } \right\}$ increases in ??.

Corollary 1 establishes that BRS always improves social welfare by addressing information asymmetry issues on the buyer side. Recall from Proposition 1 that high-quality sellers may withdraw under URS. Corollary 1 confirms that this withdrawal is indeed the (cross-side) adverse selection problem from the social welfare perspective.

## Extensions

This section first explores the same rank case and the seller’s market to shed light on when a sharing platform should adopt BRS. Then, we point out other extensions.

## Same Rank and Seller’s Market

We discussed the reverse rank case to present our most interesting results. This section analyzes the same rank case and the seller’s market. To ease exposition, all technical details are presented in Appendix C.

In a buyer’s market, aligning with the context explored in Tunc et al. (2019), we focus on the same rank case where the matching abilities $Q _ { m } ( i ) , Q _ { l } ( i )$ , and $Q _ { h } ( i )$ all increase in quality (other cases fall under the general rank case). We observe the occurrence of this case when the expected buyer cost falls below a certain threshold (i.e., $( 1 - \rho ) \theta <$ $\textstyle { \frac { ( 1 - \zeta ) ( 1 - \rho ) } { f ^ { \prime } ( q _ { 1 } ) } } )$ . In this situation, BRS always harms the platform, suggesting that it should not be adopted when buyers are not costly to serve in a P2P market. Furthermore, we demonstrate that in a seller’s market, BRS also harms the platform. The reasoning behind these results is as follows. On the one hand, when buyers are not costly to serve, highquality sellers have high matching abilities to attract buyers, preventing them from withdrawing under URS. On the other hand, in a seller’s market where buyers outnumber sellers, sellers are relatively scarce, ensuring them one-to-one matches with buyers. As a result, cross-side adverse selection never arises in these two situations. Hence, BRS does not improve the matching efficiency (i.e., the shuffle effect is absent) and eventually hurts the platform due to intensified competition for low-cost buyers. These findings indicate that the platform should carefully examine the expected buyer cost and market conditions before adopting BRS.

## Other Extensions

For robustness, we also consider five extensions in Appendix D: Namely, (1) incomplete market coverage, (2) more than two types of buyers, (3) positive serving cost parameter for low-cost buyers, (4) imperfect buyer information, and (5) general rank case. The results of these extensions confirm the robustness of our basic model conclusions. Furthermore, we obtain new insights as follows.

With incomplete market coverage (small $v _ { 0 . }$ ), BRS may result in fewer matching pairs compared with URS, thus harming social welfare because the segmentation effect raises the cost (and thus price) to serve those high-cost buyers under BRS (as opposed to a mixture of sellers under URS). As a result, high-cost buyers are unmatched under BRS when $v _ { 0 }$ is small, even though they would have been matched under URS.

In scenarios involving more than two types of buyers, a novel matching pattern arises in the reverse rank case. Specifically, intermediate-quality sellers can get matched with middle-cost buyers when the cost function is convex. However, with a linear cost function, intermediate-quality sellers are always unmatched, and the matching pattern described in our main paper remains unchanged.

## Discussion and Conclusion

Buyer-side information asymmetry is ubiquitous in the P2P sharing market. Some platforms have implemented BRS to resolve this problem, but the literature has not sufficiently discussed its mechanism and impact. Endeavoring to fill this gap, our paper studies the platform’s optimal choice between BRS and URS, and the impact of BRS on different stakeholders. We developed an analytical model to characterize the matching between heterogeneous sellers with a one-unit capacity and heterogeneous buyers in the context of the sharing economy. We found that under URS, even when the seller-side information is perfect, the adverse selection problem can still arise on the seller side (i.e., highquality sellers withdraw) owing to buyer-side information asymmetry and the coproduction nature of the serving cost. Our results show that BRS can benefit the platform through the shuffle effect in the reverse rank case. However, BRS always harms the platform in the same rank case when the matching abilities all increase in quality (in a buyer’s market) or in a seller’s market. Finally, we reveal that providing buyer information benefits buyers but may hurt sellers in the aggregate and that BRS improves social welfare by mitigating the cross-side adverse selection problem, thus potentially creating a win-win-win outcome for the platform, buyers, and sellers.

## Theoretical Contributions

We contribute to the literature on bilateral review systems by revealing the importance of the expected buyer cost and market structure of P2P sharing platforms, which have not been sufficiently examined in previous studies. In particular, our paper identifies the cross-side adverse selection problem that arises in a buyer’s market with high expected buyer costs under URS. Furthermore, our findings show that BRS leads to a shuffle effect, which plays a pivotal role in the adoption of BRS by effectively mitigating cross-side adverse selection. Absent this shuffle effect, BRS always proves detrimental to the platform (Tunc et al., 2019). Different from Ke et al. (2022), we unveil that BRS can intensify seller competition, prompting high-quality sellers to charge lower prices than those of low-quality sellers, regardless of market structure (i.e., even in a buyer’s market). These results are rooted in the context of sequential buyer arrivals, which aligns with most cases observed in real-world P2P sharing markets.

Furthermore, we extend the literature on adverse selection. Our research identifies a previously overlooked aspect of this issue: the presence of coproduction costs in the P2P sharing market. When these costs are factored in, we found that unknown information and the withdrawal of highquality agents can occur on different sides of the market, resulting in cross-side adverse selection. This is distinct from the traditional adverse selection problem where unknown information and the withdrawal of high-quality agents occur on the same side of the market (Akerlof, 1978). By illuminating this issue, our research offers a deeper understanding of market inefficiency and adverse selection in the sharing economy context.

## Practical Implications

Our study has a number of implications for sharing platforms. We identify the critical role of the expected buyer cost (high vs. low), market structure (buyer’s market vs. seller’s market), and seller quality in determining the effectiveness of URS and BRS for P2P sharing platforms due to coproduction nature.

We provide a cautious note to platforms under URS: URS can lead to the withdrawal of high-quality sellers, resulting in inefficient matching outcomes when buyers are costly to serve and in a buyer’s market (i.e., more sellers than buyers). This inefficiency also depends on the cost structure and tends to occur when the serving cost increases quickly in the quality (e.g., a convex serving cost) and sellers’ qualities are high. Such a concern is especially relevant to short-term rental platforms like Airbnb and Vrbo, where sellers share heavy assets, such as houses. This type of market exhibits several characteristics: the property quality is typically high, a buyer’s market predominates, and serving costs are more likely to increase rapidly in quality (see Appendix C for details). In contrast, such inefficiency does not arise when buyers are not costly to serve or in a seller’s market (i.e., more buyers than sellers).

Moreover, we reveal that a sharing platform should adopt BRS when the expected buyer cost is high in a buyer’s market, and the aggregate quality of top sellers is high.<sup>11</sup> It is worth pointing out that Ye et al. (2014) demonstrated that without careful design, sellers can potentially misuse BRS for retaliatory purposes against buyers. Consequently, the effectiveness of BRS hinges not only on its thoughtful adoption but also on the meticulous design to prevent such retaliatory behaviors.

Further, we provide guidance for social planners: A selfinterested platform adopting URS may thereby reduce social welfare. When the expected buyer cost is high, even if market inefficiency occurs due to buyer information asymmetry, the platform does not always have the incentive to provide buyer information if the platform is positioned to serve a low-quality market. Therefore, our research calls for the regulation of sharing platforms from an information perspective.

We next discuss other policies that are used by some platforms. First, sellers on Airbnb can choose from “instant booking” or “request booking” options. Instant booking allows buyers to match with sellers immediately (Mayya et al., 2021); this policy corresponds with the seller’s strategy to forgo screening and accept both types of buyers in our model. Request booking corresponds to the seller’s strategy to cherry-pick low-cost buyers based on seller reviews. Our paper suggests that hosts with high-quality properties should disable instant booking to avoid the risk of accommodating unreliable guests, whereas hosts with low-quality properties may consider utilizing this option.

Secondly, in addition to BRS, another commonly used tool to mitigate the information asymmetry problem is requiring buyers to provide a security deposit prior to receiving the service. If there is any property damage, the deposit will not be returned. Although this prepaid monetary incentive motivates the buyer to protect the property and reduce the serving cost (Weber, 2014), this cost can still be significant if substantial damage occurs or if the deposit retrieval process is overly cumbersome. As a result, cross-side adverse selection may still be a concern. In such scenarios, relying solely on a security deposit cannot ensure the matching of high-quality sellers. Therefore, a more effective approach could involve combining a security deposit with BRS.

## Future Research Directions

Finally, we discuss some potential directions for future research. First, we only considered a monopoly platform. However, it would be worthwhile to consider multiple platforms in a competitive environment to reexamine the information provision policy because the selection of review systems may have a substantial impact on platform competition. Second, although we briefly discussed deposits, we did not investigate them in detail as a mechanism. It would be interesting to explore mechanisms such as security deposits and platform insurance in future research. Third, we focused on the decentralized matching used by platforms like Airbnb and Fiverr, but other matching rules exist on other sharing platforms. For instance, future research could study (1) centralized matching, where the platform sets the price and matches buyers and sellers (e.g., Uber), or (2) bidding matching, where buyers post the task and sellers bid on it (e.g., Upwork). Fourth, more work could be done to identify properties of the general rank case other than the matching outcome.

## Acknowledgments

The authors would like to thank the senior editor, Siva Viswanathan, the associate editor, and the three anonymous referees for their comments. The authors also thank the committee of the CWEIST (2019), especially the suggestions and comments from Zach Zhizhong Zhou, De Liu, Xianjun Geng, and Zhenhua Wu. Gang Li, Shengli Li, and Quan Zheng are co-corresponding authors. Xuanqi Chen and Gang Li acknowledge the financial support from the National Natural Science Foundation of China (Grant No. 71832011 and 72372128), and the Science and Technology Innovation Team Plan of Shaanxi Province under Project 2020TD-006. Xuanqi Chen also would like to thank Yulan Wang and her financial support from the Research Grants Council of Hong Kong (Grant No. 15500820). Shengli Li is partially supported by the NSFC (Grant No. 71832011 and 71972004). Quan Zheng is partially supported by the NSFC (Grant No. 72122020, 71832011,71921001 and 72091215).

## References

Adaramola, S. (2022). Airbnb service fee: What percentage does Airbnb take? Booking Ninjas. https://www.bookingninjas. com/blog/airbnb-service-fee-what-percentage-does-airbnbtake

Airbnb. (2022). Sending special offers. https://www.airbnb.com/ help/article/35/sending-special-offers?%5C\_set%5C bev%5C\_on%5C\_new%5C\_domain=1565349127%5C\_OTI1 NTAxOTg3NDQ3&locale= en%5C

Akerlof, G. A. (1978). The market for “lemons”: Quality uncertainty and the market mechanism. The Quarterly Journal of Economics, 84(3) 488-500. https://doi.org/10.2307/1879431

Al-Saad, T. (2019). Airbnb’s growth strategy: How they attract and retain 150 million users. Webprofits. https://www.webprofits. com.au/blog/airbnb-growth-strategy

AllTheRooms. (2022). Average Airbnb occupancy rates by city. https://www.alltherooms.com/analytics/average-airbnboccupancy-rates-by-city/

Benjaafar, S., Kong, G., Li, X., & Courcoubetis, C. (2019). Peerto-peer product sharing: Implications for ownership, usage, and

social welfare in the sharing economy. Management Science, 65(2), 477-493. https://doi.org/10.1287/mnsc.2017.2970

Burdett, K., Shi, S., & Wright, R. (2001). Pricing and matching with frictions. Journal of Political Economy, 109(5), 1060–1085. https://doi.org/10.1086/322835

Cachon, G. P., Daniels, K. M., & Lobel, R. (2017). The role of surge pricing on a service platform with self-scheduling capacity. Manufacturing & Service Operations Management 19(3), 368- 384. https://doi.org/10.1287/msom.2017.0618

Chen, Y., & Xie, J. (2005). Third-party product review and firm marketing strategy. Marketing Science 24(2), 218-240. https://doi.org/10.1287/mksc.1040.0089

Chen, Y., & Xie, J. (2008). Online consumer review: Word-ofmouth as a new element of marketing communication mix. Management Science, 54(3), 477-491. https://doi.org/10.1287/ mnsc.1070.0810

Clifford, R. (2020). Airbnb occupancy rate: 15 actionable tips to boost your results. Hospitable. https://hospitable.com/airbnboccupancy-rate/

DMR. (2023). Fiverr statistics and facts. (2023). https://expandedramblings.com/index.php/fiverr-facts-statistics/

Fradkin, A., Grewal, E., & Holtz, D. (2021). Reciprocity and unveiling in two-sided reputation systems: Evidence from an experiment on Airbnb. Marketing Science, 40(6), 1013-1029. https://doi.org/10.1287/mksc.2021.1311

Gale, D., & Shapley, L. S. (1962). College admissions and the stability of marriage. The American Mathematical Monthly, 69(1), 9-15. https://doi.org/10.2307/2312726

Heinrichs, H. (2013). Sharing economy: a potential new pathway to sustainability. GAIA-Ecological Perspectives for Science and Society, 22(4), 228-231. http://dx.doi.org/10.14512/ gaia.22.4.5

HostGPO. (2020). Screening problematic guests on Airbnb: Less obvious guest red flags. https://blog.hostgpo.com/screeningproblematic-guests-on-airbnb-less-obvious-guest-red-flags/

Jiang, B., & Tian, L. (2018). Collaborative consumption: Strategic and economic implications of product sharing. Management Science, 64(3), 1171-1188. https://doi.org/10.1287/mnsc. 2016.2647

Jiang, Y., & Guo, H. (2015). Design of consumer review systems and product pricing. Information Systems Research, 26(4) 714- 730. https://doi.org/10.1287/isre.2015.0594

Jin, C., Hosanagar, K., & Veeraraghavan, S. K. (2022). Do ratings cut both ways? impact of bilateral ratings on platforms (Working paper). National University of Singapore.

Ke, T. T., Sun, M., & Jiang, B. (2022). Peer-to-peer markets with bilateral ratings (Working paper, The Chinese University of Hong Kong). SSRN https://papers.ssrn.com/sol3/papers. cfm?abstract\_id=3034915

Kumar, V., Lahiri, A., & Dogan, O. B. (2018). A strategic framework for a profitable business model in the sharing economy. Industrial Marketing Management, 69, 147-160. https://doi.org/10.1016/j.indmarman.2017.08.021

Kwark, Y., Chen, J., & Raghunathan, S. (2014). Online product reviews: Implications for retailers and competing

manufacturers. Information Systems Research, 25(1), 93-110. https://doi.org/10.1287/isre.2013.0511

Kwark, Y., Chen, J., & Raghunathan, S. (2017). Platform or wholesale? a strategic tool for online retailers to benefit from third-party information. MIS Quarterly, 41(3), 763-785. https://doi.org/10.25300/misq/2017/41.3.05

Lagos, R. (2000). An alternative approach to search frictions. Journal of Political Economy, 108(5), 851-873. https://doi.org/ 10.1086/317674

Leavy, J. (2020). How to deal with bad Airbnb guests (5 tips). The STR Community. https://airhostacademy.com/how-to-dealwith-bad-airbnb-guests

Li, L., Chen, J., & Raghunathan, S. (2018). Recommender system rethink: Implications for an electronic marketplace with competing manufacturers. Information Systems Research, 29(4), 1003-1023. https://doi.org/10.1287/isre.2017.0765

Li, X. (2017). Revealing or non-revealing: The impact of review disclosure policy on firm profitability. MIS Quarterly, 41(4), 1335-1345. https://doi.org/10.25300/misq/2017/41.4.14

Liang, A. (2022). Airbnb permanently bans parties and events around the world. BBC. https://www.bbc.com/news/business-61976350.

Lin, M., Pan, X. A., & Q. Zheng. (2020). Platform pricing with strategic buyers: The impact of future production cost. Production and Operations Management, 29(5), 1122-1144. https://doi.org/10.1111/poms.13157

Liu, Y., Feng, J., & Liao, X. (2017). When online reviews meet sales volume information: Is more or accurate information always better? Information Systems Research, 28(4), 723-743. https://doi.org/10.1287/isre.2017.0715

Mayya, R., Ye, S., Viswanathan, S., & Agarwal, R. (2021). Who forgoes screening in online markets and why? Evidence from Airbnb. MIS Quarterly, 45(4), 1745-1776. https://doi.org/ 10.25300/misq/2021/15335

McMahan, D. (2018). 7 things your Airbnb host wants to tell you (but probably won’t). NBC News. https://www.nbcnews.com/ better/business/7-things-your-airbnb-host-wants-tell-youprobably-won-ncna890546

Montgomery, J. D. (1991). Equilibrium wage dispersion and interindustry wage differentials. The Quarterly Journal of Economics, 106(1), 163-179. https://doi.org/10.2307/2937911

Myers, S. C., & Majluf N. S. (1984). Corporate financing and investment decisions when firms have information that investors do not have. Journal of Financial Economics, 13(2), 187-221. https://doi.org/10.1016/0304-405X(84)90023-0

Netessine, S., & Taylor, T. A. (2007). Product line design and production technology. Marketing Science, 26(1), 101-117. https://doi.org/10.1287/mksc.1060.0216

Novet, J. (2023). Airbnb reports continued deceleration in nights and experiences booked. CNBC. https://www.cnbc.com/ 2023/08/03/airbnb-abnb-q2-earnings-report-2023.html

Pavlou, P. A., Liang H., & Xue, Y. (2007). Understanding and mitigating uncertainty in online exchange relationships: A principal-agent perspective. MIS Quarterly, 31(1), 105-136. https://doi.org/10.2307/25148783

Qiu, L., Cheng, H. K., & Pu, J. (2017). Hidden profiles in corporate prediction markets: The impact of public information precision and social interactions. MIS Quarterly, 41(4), 1249-1273. https://doi.org/10.25300/misq/2017/41.4.11

Radner, R. (1979). Rational expectations equilibrium: Generic existence and the information revealed by prices. Econometrica, 47(3) 655-678. https://doi.org/10.2307/1910413

Rusteen, D. (2017). Five easy ways to increase your Airbnb search rank. Optimizemybnb. https://optimizemyairbnb.com/increase-airbnbsearch-easy/

Shapiro, C., & Stiglitz, J. E. (1984). Equilibrium unemployment as a worker discipline device. The American Economic Review, 74(3), 433-444. http://www.jstor.org/stable/1804018

Shi, S. (2002). A directed search model of inequality with heterogeneous skills and skill-biased technology. The Review of Economic Studies, 69(2), 467-491. https://www.jstor.org/ stable/1556739

Stacey, K. (2023). Does Fiverr take a cut? (Fees explained for beginners). Freelance Ready. https://freelanceready.com/doesfiverr-take-a-cut/

Timmers, S. (2022). Everything you should know about the Fiverr seller levels. Family Handyman. https://www.familyhandyman. com/list/airbnb-horror-stories

Tunc, M. M., Cavusoglu, H., & Raghunathan, S. (2019). Two-sided adverse selection and bilateral reviews in sharing economy (Working paper, Tilburg University). SSRN. https://papers.ssrn. com/sol3/papers.cfm?abstract\_id=3499979

Weber, T. A. (2014). Intermediation in a sharing economy: insurance, moral hazard, and rent extraction. Journal of Management Information Systems, 31(3), 35-71. https://www. jstor.org/stable/43590293

Ye, S., Gao, G., & Viswanathan S. (2014). Strategic behavior in online reputation systems. MIS Quarterly, 38(4), 1033-1056. https://www.jstor.org/stable/26627961

## Author Biographies

Xuanqi Chen is a Ph.D student in the School of Management, Xi’an Jiaotong University, and is a dual Ph.D student in the Department of Logistics and Maritime Studies, the Hong Kong Polytechnic University. His current research interests include economics of information systems, data privacy, and platform strategy.

Gang Li is a professor at the School of Management, Xi’an Jiaotong University. He received his Ph.D. in supply chain management from Xi’an Jiaotong University in 2005. His research interests include supply chain management, retailing operations, and the interface between marketing, information, and operations management. His papers have been published in journals such as Production and Operations Management, Decision Sciences Journal, European Journal of Operational Research, IEEE Transactions on Engineering Management, etc. He is the author of four books and has received five research grants from the Natural Science Foundation of China.

Shengli Li is an associate professor in the Department of Information Management at Peking University. He received his Ph.D. in information systems from the University of Florida in 2013. Dr. Li’s research interests focus on the economics of information systems, electronic commerce, and social media. His research has been published in several journals, including Production and Operations Management, Journal of Management Information Systems, Information & Management, and Decision Support Systems.

Quan Zheng is a professor of marketing and operations management at the School of Management at the University of Science and Technology of China (USTC). He received his Ph.D. from the University of Florida prior to joining USTC in 2018. His current research focuses on retail and platform operations, behavioral pricing, supply chain management, and the interface between operations and marketing/IS/economics. His publications have appeared in Management Science, Marketing Science, M&SOM, and Production and Operations Management.

## Appendix A

## Summary of Notation

<table><tr><td colspan="2">Table A1. Summary of Notation</td></tr><tr><td>M</td><td>Number of sellers</td></tr><tr><td> $q_i$ </td><td>Quality of the seller ranked  $i$  on quality</td></tr><tr><td>N</td><td>Number of buyers</td></tr><tr><td>ρ</td><td>Proportion of low-cost buyers</td></tr><tr><td> $f(q_i)$ </td><td> $f(q_i)=q_i$  or  $q_i^2$ </td></tr><tr><td>θ</td><td>Serving cost parameter of high-cost buyers</td></tr><tr><td> $\theta_\omega f(q_i)$ </td><td>Serving cost of seller  $i, \omega \in h,l$ , where  $\theta_l=0, \theta_h=\theta$ </td></tr><tr><td> $Q_m(i)$ </td><td>Matching ability of seller  $i$  to serve the mixture of buyers under URS</td></tr><tr><td> $Q_h(i)$ </td><td>Matching ability of seller  $i$  to serve high-cost buyers under BRS</td></tr><tr><td> $Q_l(i)$ </td><td>Matching ability of seller  $i$  to serve low-cost buyers under BRS</td></tr><tr><td> $N_h, N_l$ </td><td> $N_h=N(1-\rho), N_l=N\rho$ </td></tr><tr><td>ζ</td><td>Commission rate of the platform</td></tr><tr><td> $p_i^\alpha$ </td><td>Price of seller  $i$  under URS (BRS) when  $\alpha = U (\alpha = B)$ </td></tr><tr><td> $U_i$ </td><td>Buyer utility derived from seller  $i$ </td></tr><tr><td> $\pi_i$ </td><td>Profit of seller  $i$ </td></tr><tr><td> $s_i$ </td><td>Custom price of seller  $i$  under BRS</td></tr><tr><td> $\pi_B, \pi_U$ </td><td>Platform profit under BRS and URS</td></tr><tr><td> $\Pi_B, \Pi_U$ </td><td>Seller profit under BRS and URS</td></tr><tr><td> $CS_B, CS_U$ </td><td>Buyer surplus (consumer welfare) under BRS and URS</td></tr><tr><td> $SW_B, SW_U$ </td><td>Social welfare under BRS and URS</td></tr></table>

## Appendix B

## Proofs

To prove Proposition 1, we first prove a more general result in Lemma B1, where $Q _ { m } ( \cdot )$ is in a general form.

Lemma B1: Sort $Q _ { m } ( \cdot )$ in descending order and label: $Q _ { m } [ 1 ] > Q _ { m } [ 2 ] > \cdots > Q _ { m } [ M ]$ , where $Q _ { m } [ j ]$ corresponds to $Q _ { m } ( \cdot )$ that ranks ?? among all $Q _ { m } ( i )$ , and [??] labels the seller with $Q _ { m } [ j ]$ . In equilibrium, we have the following.

• Sellers $i \in \{ [ 1 ] , [ 2 ] , \ldots , [ N ] \}$ are matched and offer $U _ { i } ^ { * } = v _ { 0 } + Q _ { m } [ N + 1 ]$

• Seller [?? + 1] is unmatched and offers $U _ { [ N + 1 ] } ^ { * } = v _ { 0 } + Q _ { m } [ N + 1 ]$

• Other sellers are unmatched, and they offer arbitrary utility below $v _ { 0 } + Q _ { m } [ N + 1 ]$

Proof of Lemma B1: To prove the equilibrium, we show the existence and the uniqueness.

Existence: No seller deviates because (1) if seller $i \in \{ [ 1 ] , [ 2 ] , \ldots , [ N ] \}$ decreases her price, she will get less profit. If she increases her price, she offers lower utility than that of seller $\left[ N + 1 \right]$ . That is, she is beaten by other ?? sellers and thus cannot get matched with ?? buyers. (2) Seller $[ N + 1 ]$ cannot get matched because conditional on the positive profit, the highest utility that she can offer is $v _ { 0 } + Q _ { m } [ N + 1 ]$ (recall the definition of the matching ability), while $v _ { 0 } + Q _ { m } [ N + 1 ]$ is the utility offered by the other ?? sellers. By the tie-breaking assumption, she is beaten by ?? sellers with higher matching abilities. Therefore, she cannot improve her profit by deviating. (3) Other sellers’ pricing strategies do not impact the equilibrium because they cannot offer a utility higher than $v _ { 0 } + Q _ { m } ^ { - } [ N + 1 ]$ ; that is, they cannot improve profits by deviating.

Uniqueness: Buyers choose the ?? sellers who offer the highest utility, leaving unmatched other $M - N$ sellers who offer lower utility. Consider any seller $[ j ] \in \{ [ 1 ] , [ 2 ] , \dots , [ N ] \}$ and seller $[ N + \dot { 1 } ]$ . Recall that seller [??] has a higher $Q _ { m } ( \cdot )$ than $Q _ { m } [ N + 1 ]$ of seller $[ N + 1 ]$ Figure B1 shows the reaction curve of seller [??] and seller $[ N + 1 ]$

![](/api/attachments/2B5WEFYW/fulltext/images/81d01e72923c2da5445e6e94021172e0797d5525ed791ee0914f232f90b9ffcc.jpg)

Figure B1. Reaction Curve under URS

The unique intersection is at $v _ { 0 } + Q _ { m } [ N + 1 ]$ . As for other sellers, they cannot offer higher utility than $v _ { 0 } + Q _ { m } [ N + 1 ]$ . Hence, they offer arbitrary utility below $v _ { 0 } + Q _ { m } [ N + 1 ]$ , which does not impact the equilibrium outcome. □

Proof of Proposition 1: We have the reverse rank case when $\begin{array} { r } { Q _ { m } ( i ) = q _ { i } - \frac { ( 1 - \rho ) \theta f ( q _ { i } ) } { 1 - \zeta } } \end{array}$ decreases in $q _ { i } , \forall i .$ This implies

$$
\frac {d Q _ {m} (i)}{d q _ {i}} <   0, \forall i
$$

and thus

$$
1 - f ^ {\prime} (q _ {i}) \frac {(1 - \rho) \theta}{1 - \zeta} <   0, \forall i.
$$

Since $f ^ { \prime } ( q _ { i } ) = 1 \ \mathrm { o r } \ 2 q _ { i }$ , the highest $1 - f ^ { \prime } ( q _ { i } ) { \frac { ( 1 - \rho ) \theta } { 1 - \zeta } }$ is reached at $i = M \ ( { \mathrm { i . e . } }$ ., the lowest quality). Hence, $\begin{array} { r } { 1 - f ^ { \prime } ( q _ { i } ) \frac { ( 1 - \rho ) \theta } { 1 - \zeta } < 0 } \end{array}$ , ∀?? is equivalent to

$$
1 - f ^ {\prime} (q _ {M}) \frac {(1 - \rho) \theta}{1 - \zeta} <   0.
$$

Next, by Lemma B1 and the definition of reverse rank, the matched sellers $[ j ] \in \{ 1 , \ldots , N \}$ are those indexed $i \in \{ M - N + 1 , \ldots , M \}$ . The pricing outcomes are obtained by inserting the utility given by Lemma B1 into $p _ { i } = v _ { 0 } + q _ { i } - U _ { i }$

Moreover, it is obvious that $\frac { 1 - \zeta } { f ^ { \prime } ( q _ { M } ) }$ decreases in ??. When the serving cost is convex $( \gamma = 2 )$ , we know $\begin{array} { r } { \frac { 1 - \zeta } { f ^ { \prime } ( q _ { M } ) } = \frac { 1 - \zeta } { 2 q _ { M } } } \end{array}$ decreases in $q _ { M } . \sqcup$

More discussion of the condition for Proposition 1: We argue that only assuming a linear cost function cannot rule out the reverse rank case. Note that the assumption $\theta < 1 - \zeta$ in Tunc et al. (2019) ensures full market coverage under BRS $( { \mathrm { i . e . , ~ } } u _ { i } = q _ { i } - p _ { i } \geq 0$ and $\pi _ { i } =$ $( 1 - \zeta ) p _ { i } - \theta q _ { i } \geq 0$ always hold). Importantly, this assumption $\theta < 1 - \zeta$ happens to be a sufficient condition to rule out the reverse rank case $( \mathrm { i . e . , } ( 1 - \rho ) \theta > 1 - \zeta$ never holds). However, if we investigate the partial market coverage in the setting of Tunc et al. $\left( 2 0 1 9 \right) ( { \mathrm { i . e . } }$ $\theta > 1 - \zeta )$ , reverse rank indeed occurs under URS when $( 1 - \rho ) \theta > 1 - \zeta$ . In our paper, we assume a high $v _ { 0 }$ in the utility function $u _ { i } =$ $v _ { 0 } + q _ { i } - p _ { i }$ to achieve full market coverage. In this sense, we separate the condition for full market coverage (on $v _ { 0 } )$ and for the same/reverse rank (on $\theta ( 1 - \rho ) \quad$ ) clearly, which enables us to identify the reverse rank case.

To prove Proposition 2, we first prove a more general result in Lemma B2, where $Q _ { l } ( \cdot )$ and $Q _ { h } ( \cdot )$ are in general forms.

Lemma B2: Suppose $Q _ { l } ( 1 ) > Q _ { l } ( 2 ) > \cdots > Q _ { l } ( M )$ and $Q _ { h } ( 1 ) < Q _ { h } ( 2 ) < \cdots < Q _ { h } ( M )$ . In equilibrium, we have the following.

• Sellers $i \in \{ 1 , \ldots , N _ { l } \}$ get matched with $N _ { l }$ low-cost buyers; these sellers offer $U _ { i } ^ { * } = v _ { 0 } + Q _ { l } ( N _ { l } + 1 )$ and only accept low-cost buyers.

• Sellers $i \in \{ M - N _ { h } + 1 , \ldots , M \}$ get matched with $N _ { h }$ high-cost buyers; these sellers offer $U _ { i } ^ { * } = v _ { 0 } + Q _ { h } ( M - N _ { h } )$ and accept both types of buyers.

• Seller $i = N _ { l } + 1$ offers $U _ { N _ { l } + 1 } ^ { * } = v _ { 0 } + Q _ { l } ( N _ { l } + 1 )$ and only accepts a low-cost buyer; she is unmatched.

• Seller $i = M - N _ { h }$ offers $U _ { M - N _ { h } } ^ { * } = v _ { 0 } + Q _ { h } ( M - N _ { h } )$ and accept both types of buyers; she is unmatched.

• Other sellers are unmatched; each of them offers arbitrary utility in terms of an accept/reject decision. In particular, if she only accepts low-cost buyers (accept all buyers), her arbitrary utility is below $v _ { 0 } + Q _ { l } ( N _ { l } + \bar { 1 } ) \ ( v _ { 0 } + Q _ { h } ( M - N _ { h } ) )$

Proof of Lemma B2: To prove the equilibrium, we show the existence and the uniqueness.

Existence: No seller deviates because (1) if seller $i \in \{ 1 , \ldots , N _ { l } \}$ decreases her price, she will get less profit, and if she increases her price, seller $N _ { l } + 1$ will beat her by offering a higher utility so she cannot get matched with a low-cost buyer. Besides, if seller ?? deviates to accept high-cost buyers, conditional on the positive profit, the highest utility that she can offer to high-cost buyers is $\boldsymbol { v } _ { 0 } + \boldsymbol { Q } _ { h } ( i )$ (recall the definition of the matching ability) and is thus less than the utility $U _ { j } ^ { * } = v _ { 0 } + Q _ { h } ( M - N _ { h } )$ offered by $N _ { h }$ sellers $j \in \{ M - N _ { h } + 1 , \ldots , M \}$ ; therefore, she cannot get matched with any of the $N _ { h }$ high-cost buyers.

(2) If seller $i \in \{ M - N _ { h } + 1 , \ldots , M \}$ decreases the price, she will get less profit; and if she increases the price, seller $M - N _ { h }$ will beat her by offering a higher utility so she cannot get matched with a high-cost buyer. Besides, if she deviates to cherry-pick the low-cost buyer, conditional on the positive profit, the highest utility that she can offer to the low-cost buyers is $Q _ { l } ( i ) = v _ { 0 } + Q _ { l } ( i )$ (recall the definition of the matching ability) and is thus less than the utility $U _ { j } ^ { * } = v _ { 0 } + Q _ { l } ( N _ { l } + 1 )$ offered by $N _ { l }$ sellers $j \in \{ 1 , \dots , N _ { l } \}$ ; therefore, she cannot get matched with any of the $N _ { l }$ low-cost buyers.

(3) Seller $N _ { l } + 1$ and seller $M - N _ { h }$ cannot get matched by the tie-breaking assumption, and other sellers cannot get matched due to low matching abilities. In other words, deviation does not improve the profits of any of these sellers.

Uniqueness: For any pair of seller $j \in \{ 1 , \dots , N _ { l } \}$ and seller $N _ { l } + 1$ , we have $Q _ { l } ( j ) > Q _ { l } ( N _ { l } + 1 )$ ; for any pair of seller $k \in \{ M - N _ { h } +$ $1 , \ldots , M \}$ and seller $M - N _ { h }$ , we have $Q _ { h } ( k ) > Q _ { h } ( M - N _ { h } )$ . The reaction curves of these two pairs of sellers are shown in Figure B2.

![](/api/attachments/2B5WEFYW/fulltext/images/af3c2403a94952755a1f375872939acb2923b6fefe256812cb1a7de08c490550.jpg)

![](/api/attachments/2B5WEFYW/fulltext/images/a57e879e1619548f5f8944d9493618c7b358a31bf7fa26e327a02ac8a6611c55.jpg)  
Figure B2. Reaction Curves under BRS

The unique intersection is at $U _ { j } = v _ { 0 } + Q _ { l } ( N _ { l } + 1 )$ and $U _ { k } = v _ { 0 } + Q _ { h } ( M - N _ { h } )$ , respectively.

Other sellers’ strategies do not impact the equilibrium because they cannot get matched; that is, $Q _ { l } ( N _ { l } + 1 )$ and $Q _ { h } ( M - N _ { h } )$ are higher than their matching abilities. Among these unmatched sellers, if one only accepts low-cost buyers (accept all buyers), her arbitrary utility is below $v _ { 0 } + Q _ { l } ( N _ { l } + 1 ) ( v _ { 0 } + Q _ { h } ( M - N _ { h } ) )$ . □

Proof of Proposition 2: Applying Lemma B2, we obtain the stated utility in equilibrium. The pricing outcomes follow from inserting the offered utility into $p _ { i } = v _ { 0 } + q _ { i } - U _ { i }$ . Moreover, each seller has only one price, and thus the custom price does not play any role; that is, the equilibrium remains the same without the custom prices. Note that in rational expectation equilibrium, each seller sets an arbitrary custom price as long as the offered utility is below $v _ { 0 } + Q _ { l } ( N _ { l } + 1 )$ . The custom price is not used in equilibrium. This is because low-cost buyers cannot improve the utility by requesting the custom prices from low-quality sellers $j \in \{ M - N _ { h } + 1 , \dots , M \}$ , given that sellers $i \in \{ 1 , \ldots , N _ { l } \}$ offer the utility $v _ { 0 } + Q _ { l } ( N _ { l } + 1 )$ with the posted prices.

Next, we compare the price of high-quality seller $i _ { h } \in \{ 1 , \ldots , N _ { l } \}$ and low-quality seller $i _ { l } \in \{ M - N _ { h } + 1 , \ldots , M \} ; p _ { i _ { h } } ^ { * } < p _ { i _ { l } } ^ { * } \Leftrightarrow q _ { i _ { h } } - q _ { i _ { l } } <$ $q _ { N _ { l } + 1 } - q _ { M - N _ { h } } + \frac { \theta f \left( q _ { M - N _ { h } } \right) } { 1 - \zeta } . ~ \sqsupset$

The withdrawal of intermediate-quality sellers is efficient: One may wonder whether it is inefficient for the low-quality sellers to be matched but for the intermediate-quality sellers to be unmatched. However, low-quality sellers are more efficient than intermediate-quality sellers to serve high-cost buyers under BRS. This can be seen from the social welfare of seller ?? serving a single high-cost buyer: $S W _ { i } = U _ { i } +$ $\pi _ { i } + \pi _ { p } = v _ { 0 } + q _ { i } - \theta f ( q _ { i } )$ . This $S W _ { i }$ decreases in quality $q _ { i } ( \mathrm { i . e . , } \theta > \frac { 1 } { f ^ { \prime } ( q ) } )$ with reverse rank (i.e., $\begin{array} { r } { \theta > \frac { 1 - \zeta } { \left( 1 - \rho \right) f ^ { \prime } \left( q \right) } \mathrm { g i v e n } \frac { 1 - \zeta } { 1 - \rho } > 1 } \end{array}$ , because the commission rate $\zeta$ is around 20% and the proportion of low-cost buyers $\rho$ is higher than 20% (Leavy, 2020). That is, $\textstyle { \frac { 1 - \zeta } { 1 - \rho } } > 1$ always holds.

Proof of Proposition 3: We have the following:

$$
\pi_ {B} = \zeta \sum_ {i = 1} ^ {N _ {l}} \left(q _ {i} - q _ {N _ {l} + 1}\right) + \zeta \sum_ {i = M - N _ {h} + 1} ^ {M} \left[ q _ {i} - Q _ {h} (M - N _ {h}) \right],\tag{B1}
$$

$$
\pi_ {U} = \zeta \sum_ {i = M - N + 1} ^ {M} \left[ q _ {i} - Q _ {m} (M - N) \right],\tag{B2}
$$

where $Q _ { m } ( \cdot )$ and $Q _ { h } ( \cdot )$ are the matching abilities (see Equations 2 and 4). We then obtain

$$
\frac {\pi_ {B} - \pi_ {U}}{\zeta} = \sum_ {i = 1} ^ {N _ {l}} q _ {i} - \sum_ {i = M - N + 1} ^ {M - N _ {h} + 1} q _ {i} - \left[ N _ {l} q _ {N _ {l} + 1} + N _ {h} Q _ {h} (M - N _ {h}) - N Q _ {m} (M - N) \right].
$$

Define

$$
A _ {1} = \sum_ {i = M - N + 1} ^ {M - N _ {h} + 1} q _ {i} + \left[ N _ {l} q _ {N _ {l} + 1} + N _ {h} Q _ {h} (M - N _ {h}) - N Q _ {m} (M - N) \right].
$$

It is clear that $\pi _ { B } > \pi _ { U } \mathrm { i f } \sum _ { i = 1 } ^ { N _ { l } } q _ { i } > A _ { 1 }$ , and $\pi _ { B } \leq \pi _ { U }$ otherwise. Moreover, we have

$$
\frac {\partial A _ {1}}{\partial \theta} = N \frac {1 - \rho}{1 - \zeta} \big [ f (q _ {M - N}) - f \big (q _ {M - N _ {h}} \big) \big ] > 0.
$$

We next focus on the condition on $\rho .$ Since $q _ { i }$ and $f ( q _ { i } )$ are in general forms, no closed-form solution exists. To obtain the closed-form solution, we assume $f ( q ) = q$ and $\begin{array} { r } { q _ { i } = 1 - \frac { i - 1 } { M } } \end{array}$ and have

$$
\pi_ {B} - \pi_ {U} = \zeta N \rho \frac {1 - \zeta + N (1 - \zeta + \theta \rho - \theta)}{(1 - \zeta) M}.
$$

Solving $\pi _ { B } - \pi _ { U } \lesseqgtr 0 .$ we have $\begin{array} { r } { \rho \lessgtr \rho _ { 1 } = 1 - \frac { N + 1 } { N } \frac { 1 - \zeta } { \theta } . } \end{array}$ . This implies that when $\mathbf { \nabla } \cdot \rho$ is high, BRS benefits the platform because the shuffle effect is strong and dominates the segmentation effect. □

Proof of Proposition 4: We first compare the seller’s profits in the two cases. We have the following:

$$
\Pi_ {B} = \sum_ {i = 1} ^ {N _ {l}} (1 - \zeta) \big (q _ {i} - q _ {N _ {l} + 1} \big) + \sum_ {i = M - N _ {h} + 1} ^ {M} \{(1 - \zeta) [ q _ {i} - Q _ {h} (M - N _ {h}) ] - \theta f (q _ {i}) \},
$$

$$
\Pi_ {U} = \sum_ {i = M - N + 1} ^ {M} \{(1 - \zeta) [ q _ {i} - Q _ {m} (M - N) ] - (1 - \rho) \theta f (q _ {i}) \}.
$$

Therefore, we obtain:

$$
\frac {\Pi_ {B} - \Pi_ {U}}{1 - \zeta} = \sum_ {i = 1} ^ {N _ {l}} q _ {i} - A _ {2},\tag{B3}
$$

where

$$
A _ {2} = \sum_ {i = M - N + 1} ^ {M} Q _ {m} (i) - \sum_ {i = M - N _ {h} + 1} ^ {M} Q _ {h} (i) + \frac {N _ {l} q _ {N _ {l} + 1} + N _ {h} Q _ {h} (M - N _ {h}) - N Q _ {m} (M - N)}{1 - \zeta}.
$$

When $\begin{array} { r } { \sum _ { i = 1 } ^ { N _ { l } } q _ { i } > A _ { 2 } } \end{array}$ , we have $\Pi _ { B } - \Pi _ { U } > 0$ , and otherwise, $\Pi _ { B } - \Pi _ { U } \leq 0$ . Moreover, we have

$$
\frac {\partial A _ {2}}{\partial \theta} = \frac {N _ {h}}{(1 - \zeta)} \big (\overline {{f _ {M - N + 1} ^ {M}}} - \overline {{f _ {M - N _ {H} + 1} ^ {M}}} \big) + \frac {N _ {h}}{(1 - \zeta) ^ {2}} \big [ f (q _ {M - N}) - f \big (q _ {M - N _ {h}} \big) \big ] > 0,
$$

where $\overline { { f _ { x } ^ { y } } }$ denotes the average quality of sellers $i \in \{ x , \ldots , y \} ( x < y )$ and $\overline { { f _ { M - N + 1 } ^ { M } } } > \overline { { f _ { M - N _ { h } + 1 } ^ { M } } } .$

Then, we compare the buyer surplus results. We have the following:

$$
C S _ {B} = N (1 - \rho) \left[ q _ {M - N _ {h}} - \frac {\theta f (q _ {M - N _ {h}})}{1 - \zeta} \right] + N \rho \left[ q _ {N _ {l} + 1} - q _ {M - N _ {h}} + \frac {\theta f (q _ {M - N _ {h}})}{1 - \zeta} \right],
$$

$$
C S _ {U} = N \left[ q _ {M - N} - \frac {(1 - \rho) \theta f (q _ {M - N})}{1 - \zeta} \right].
$$

With some algebraic manipulation, we have

$$
C S _ {B} - C S _ {U} = N \big [ Q _ {m} (M - N _ {h}) - Q _ {m} (M - N) + \rho \big (q _ {N _ {l} + 1} - q _ {M - N _ {h}} \big) \big ] > 0.
$$

We next focus on the condition on $\rho .$ Since $q _ { i }$ and $f ( q _ { i } )$ are in general forms, no closed-form solution exists. To obtain the closed-form solution, we assume $f ( q ) = q$ and $q _ { i } = 1 - \frac { i - 1 } { M }$ and have

$$
\frac {\Pi_ {B} - \Pi_ {U}}{1 - \zeta} = N \rho \frac {2 (N + 1) (1 - \zeta) - N \theta (1 - \rho)}{2 (1 - \zeta) M}.
$$

Solving $\frac { \Pi _ { \mathrm { B } } - \Pi _ { \mathrm { U } } } { 1 - \zeta } \lesseqgtr 0 .$ , we have $\begin{array} { r } { \rho \lessgtr \rho _ { 2 } = 1 - 2 \frac { N + 1 } { N } \frac { 1 - \zeta } { \theta } . } \end{array}$ . This implies that when $\mathbf { \nabla } \cdot \rho$ is high, BRS benefits the sellers because the shuffle effect is strong and dominates the segmentation effect. □

Proof of Corollary 1: The all-win outcome can be obtained by combining Propositions 3 and 4. In terms of social welfare under BRS and URS, we have $\begin{array} { r } { { S W } _ { B } = \sum _ { i = 1 } ^ { N _ { l } } q _ { i } + \sum _ { i = M - N _ { h } + 1 } ^ { M } [ q _ { i } - \theta f ( q _ { i } ) ] } \end{array}$ under BRS,

$\begin{array} { r } { S W _ { U } = \sum _ { i = M - N + 1 } ^ { M } [ q _ { i } - ( 1 - \rho ) \theta f ( q _ { i } ) ] } \end{array}$ under URS. By comparing the average quality, we obtain

$$
S W _ {B} - S W _ {U} = N _ {l} \left(\frac {\sum_ {i = 1} ^ {N _ {l}} q _ {i}}{N _ {l}} - \frac {\sum_ {i = M - N + 1} ^ {M - N _ {h}} q _ {i}}{N _ {l}}\right) + \theta N _ {h} \left[ \frac {\sum_ {i = M - N + 1} ^ {M} f (q _ {i})}{N} - \frac {\sum_ {i = M - N _ {h} + 1} ^ {M} f (q _ {i})}{N _ {h}} \right] > 0.
$$

□

## Appendix C

## Comparison with the Literature and Technical Details

The following tables compare our paper with the literature. In addition, we summarize the unique features that enable us to obtain distinct results compared to those found in the literature. We also compare our results obtained in the same rank case and in the seller’s market with those in Tunc et al. (2019). Finally, we provide technical details.

<table><tr><td colspan="3">Table C1. Comparison with Ke et al. (2022)</td></tr><tr><td></td><td>Ke et al. (2022)</td><td>Our paper</td></tr><tr><td>Buyer arrival assumption</td><td>Buyers arrive simultaneously</td><td>Buyers arrive sequentially</td></tr><tr><td>Price competition</td><td>BRS softens price competition</td><td>BRS intensifies price competition</td></tr><tr><td>Subsidization effect</td><td>Occurs with incomplete market coverage</td><td>Occurs with complete and incomplete coverage</td></tr><tr><td>Adverse selection</td><td>High-quality sellers are always matched</td><td>High-quality sellers may withdraw</td></tr></table>

<table><tr><td colspan="3">Table C2. Comparison with Tunc et al. (2019)</td></tr><tr><td></td><td>Tunc et al. (2019)</td><td>Our paper</td></tr><tr><td>Cost function assumption</td><td>Function  $f(q) = q$  and  $\theta < 1 - \zeta$ </td><td>Function  $f(q) = q$  or  $q^2$  and unbounded  $\theta$ </td></tr><tr><td>Quality assumption</td><td>Two quality groups</td><td>Fully heterogeneous quality</td></tr><tr><td>Adverse selection</td><td>URS is sufficient to solve market breakdown</td><td>High-quality sellers can withdraw in URS</td></tr><tr><td>Market focus</td><td>Seller&#x27;s market with the same rank</td><td>Buyer&#x27;s market with reverse rank</td></tr><tr><td>Results in the buyer&#x27;s market</td><td>BRS does not change the platform profit</td><td>BRS increases or decreases the platform profit</td></tr><tr><td>Results in the seller&#x27;s market</td><td colspan="2">BRS decreases the platform profit (i.e., the same result in their paper and ours)</td></tr></table>

## Realistic Features

Unlike previous literature on BRS (Tunc et al., 2019; Ke et al., 2022), our model incorporates the following realistic features. First, we consider a cost structure that nests a linear and convex cost function concerning quality. In practice, higher-quality assets are significantly more costly to maintain because they have more delicate devices, larger spaces, and more luxury amenities, and therefore the serving cost can increase quickly as the quality rises. To capture this feature, we follow the literature by assuming a convex cost function (Netessine & Taylor, 2007; Lin et al., 2020). Furthermore, we identify the important role of the expected buyer cost in determining the matching outcom due to the coproduction.

Second, sellers are fully heterogeneous in quality rather than having only two types. This aligns with the observation that the service providers in the sharing economy are highly heterogeneous, and the consumer reviews (e.g., ratings on Airbnb) enable buyers to distinguish those heterogeneous sellers. The heterogeneity moderates seller competition, leading to different managerial insights.

Third, instead of assuming a seller’s market, our focus is on a buyer’s market. In 2020 and 2021, the Airbnb average daily occupancy rates in eight example cities were all below 50%, even on holidays. In 500 cities in the United States, the highest average occupancy rate was 48.4% in 2021 (AllTheRooms, 2022). On Fiverr, the number of transactions per day is far smaller than the number of sellers (DMR, 2022). Hence, the buyer’s market is more prevalent and relevant for these decentralized sharing platforms. Our results concerning the buyer’s market depart sharply from the previous research.

## Comparison in the Same Rank Case and in a Seller’s Market

We first compare our work with Tunc et al. (2019) by following their settings with $\theta < 1 - \zeta$ and $f ( q ) = q \ ( \mathrm { i . e }$ ., the same rank case). Slightly different results are derived (technical details are in Appendix C). We find that in the buyer’s market, BRS always harms the platform, while they show that BRS yields the same platform profit as URS. Furthermore, in the seller’s market, we obtain the same result (i.e., BRS always harms the platform) even with relaxed assumptions (i.e., ?? is not bounded and $f ( q ) = q \ \mathrm { o r } \ q ^ { 2 } )$ . In the buyer’s market, recall from Proposition 3 that the shuffle effect plays a critical role in the adoption of BRS with reverse rank. Our result reveals that with $f ( q ) = q$ and $\theta < 1 - \zeta$ as in Tunc et al. (2019), the same rank case occurs, and the same high-quality sellers are matched under URS and BRS. Therefore, the shuffle effect disappears. We accordingly find that BRS always harms the platform because of intensified seller competition brought by the segmentation effect.

Interestingly, we do not obtain the same results as those in Tunc et al. (2019) even with $f ( q ) = q$ and $\theta < 1 - \zeta$ . The difference rests on the assumption of seller quality: fully heterogeneous quality vs. two quality groups (i.e., high and low quality). In the buyer’s market considered by Tunc et al. (2019), high-quality sellers get matched with buyers but face head-to-head competition and charge prices equal to the serving costs in both URS and BRS. Hence, the commission income, proportional to prices, is the same. In accordance with practice, we assume fully heterogeneous sellers. The heterogeneity softens the head-to-head competition vis-à-vis their model and generates the different commission incomes under URS and BRS. However, if the qualities of high-quality sellers $i \in \{ 1 , \ldots , N \}$ are extremely close $( \mathrm { i } . \mathrm { e } . , q _ { 1 }$ converges to $q _ { N } ) .$ we find that the platform profit is the same under URS and BRS. This confirms that seller heterogeneity enables our results to differ from prior literature’s conclusions.

We next discuss the seller’s market. In this situation, our results are similar to Tunc et al. (2019)’s because all sellers are matched. This means that high-quality sellers are never driven out of the market under URS. Therefore, BRS and URS lead to a similar all-matched outcome, and thus the shuffle effect disappears. Absent the shuffle effect, we confirm that BRS always harms the platform due to the seller competition for low-cost buyers brought by the segmentation effect. We also demonstrate the robustness of our result in Appendix C by considering that the seller’s and buyer’s market can both occur.

## Technical Details

This subsection is organized as follows: Result C0 discusses the condition for the same rank case and shows that this case always arises in Tunc et al. (2019). Results C1, C2, and $C 2 ^ { * }$ elaborate on the equilibrium of the same rank case. Results C3 and C4 present the equilibrium in the seller’s market, where the price and platform profit are denoted by $p _ { i } ^ { S , \alpha * }$ and $\pi _ { i } ^ { S , \alpha * }$ with $\alpha \in \{ U , B \}$ , respectively. Lemma C2 demonstrates the robustness of our result when the seller’s market occurs with a probability. Our solution concept is the rational expectation equilibrium. To obtain the pure-strategy equilibrium and compare the results, the custom price and another technical assumption $\begin{array} { r } { ( \frac { \theta } { 1 - \zeta } < \chi , } \end{array}$ shown in the proof) are used. Again, recall that we focus on the same rank case where $Q _ { m } ( i ) , Q _ { l } ( i )$ , and $Q _ { h } ( i )$ increase in $q _ { i } .$

Result C0: Suppose $\theta _ { h } = \theta , \theta _ { l } = 0$ , and $f ( q ) = q o r q ^ { 2 }$ . The matching abilities $Q _ { m } ( i ) , Q _ { l } ( i )$ , and $Q _ { h } ( i )$ increase in $q _ { i }$ when the expected buyer cost $\theta ( 1 - \rho )$ is lower than a threshold, i.e., $\begin{array} { r } { \theta ( 1 - \rho ) < \frac { ( 1 - \zeta ) ( \bar { 1 } - \rho ) } { f ^ { \prime } ( q _ { 1 } ) } . } \end{array}$ Suppose $f ( q ) = q$ and $\theta < 1 - \zeta$ (Tunc et al., $2 0 I 9 ) , Q _ { m } ( i )$ $Q _ { l } ( i )$ , and $Q _ { h } ( i )$ always increase in $q _ { i }$

Result C1: Assume that $Q _ { m } ( i ) , Q _ { l } ( i )$ , and $Q _ { h } ( i )$ increase in ?? . Under URS, sellers $i \in \{ 1 \ldots , N \}$ get matched with ?? buyers and charge $\begin{array} { r } { p _ { i } ^ { U * } = q _ { i } - \Big [ q _ { N + 1 } - \frac { ( 1 - \rho ) \theta f ( q _ { N + 1 } ) } { 1 - \zeta } \Big ] . } \end{array}$ . Under BRS, we have the following:

• Sellers $i \in \{ 1 , \ldots , N _ { l } \}$ are matched with $N _ { l }$ low-cost buyers; these sellers only accept low-cost buyers and charge $p _ { i } ^ { B * } = q _ { i } -$ $\begin{array} { r } { \left[ q _ { N + 1 } - \frac { \theta f ( q _ { N + 1 } ) } { 1 - \zeta } \right] - \frac { \theta f \left( q _ { N _ { l } + 1 } \right) } { 1 - \zeta } . } \end{array}$

• Sellers $i \in \{ N _ { l } + 1 , \ldots , N \}$ are matched with $N _ { h }$ high-cost buyers; these sellers accept all buyers and charge $p _ { i } ^ { B * } = q _ { i } -$ $\begin{array} { r } { \left[ q _ { N + 1 } - \frac { \theta f ( q _ { N + 1 } ) } { 1 - \zeta } \right] } \end{array}$ . Among these, seller $N _ { l } + 1$ charges the custom price $\begin{array} { r } { s _ { N _ { l } + 1 } ^ { * } = q _ { N _ { l } + 1 } - \left[ q _ { N + 1 } - \frac { \theta f ( q _ { N + 1 } ) } { 1 - \zeta } \right] - \frac { \theta f \left( q _ { N _ { l } + 1 } \right) } { 1 - \zeta } } \end{array}$ to a lowcost buyer; sellers $i \in \{ N _ { l } + 2 , \ldots , N \}$ set the arbitrary custom prices to offer the utility below $\begin{array} { r } { v _ { 0 } + Q _ { h } ( N + 1 ) + \frac { \theta f ( q _ { i } ) . } { 1 - \zeta } } \end{array}$

• Seller $i = N + 1$ is unmatched; she accepts both types of buyers and offers $v _ { 0 } + Q _ { h } ( N + 1 )$

• Sellers $i \in \{ N + 2 , \ldots , M \}$ are unmatched; each of them offers arbitrary utility in terms of an accept/reject decision. In particular, if she only accepts low-cost buyers (resp. accept all buyers), her arbitrary utility is below $\begin{array} { r } { v _ { 0 } + Q _ { h } ( N + 1 ) + \frac { \theta f \left( q _ { N _ { l } + 1 } \right) } { 1 - \zeta } ( r e s p . \ v _ { 0 } } \end{array}$ + $Q _ { h } ( N + 1 ) )$ .

Result C2: Assume that $Q _ { m } ( i ) , Q _ { l } ( i )$ , and $Q _ { h } ( i )$ increase in ??<sub>??</sub>. BRS decreases the platform profit.

Result $\mathbf { C } 2 ^ { \ast } \mathrm { : }$ Assume that $Q _ { m } ( i ) , Q _ { l } ( i )$ , and $Q _ { h } ( i )$ increase in ?? . When $q _ { 1 }  q _ { N } ,$ , the platform profit is the same under BRS and under URS.

Result C3: Consider the seller’s market $( i . e . , N > M )$ . Under URS, all sellers are matched and charge $p _ { i } ^ { S , U * } = v _ { 0 } + q _ { i }$ . Under BRS, if the number of low-cost buyers is extremely high $( i . e . , N _ { l } \ge M )$ , all sellers cherry-pick low-cost buyers and set $p _ { i } ^ { S , B * } = v _ { 0 } + q _ { i }$ . Otherwise $( i . e .$ $N _ { l } < M )$ , sellers $i \in \{ 1 , \ldots , N _ { l } \}$ are matched with $N _ { l }$ low-cost buyers; these sellers only accept low-cost buyers and charge $p _ { i } ^ { S , B * } = v _ { 0 } + q _ { i } -$ $\frac { \theta f \big ( q _ { N _ { l } + 1 } \big ) } { 1 - \zeta } .$ . Sellers $i \in \{ N _ { l } + 1 , \ldots , M \}$ are matched with $N _ { h }$ high-cost buyers; these sellers accept all buyers and charge $p _ { i } ^ { S , B * } = v _ { 0 } + q _ { i } ,$ among these, seller $N _ { l } + 1$ charges the custom price $\begin{array} { r } { s _ { N _ { l } + 1 } ^ { * } = v _ { 0 } + q _ { N _ { l } + 1 } - \frac { \theta f \left( q _ { N _ { l } + 1 } \right) } { 1 - \zeta } } \end{array}$ to a low-cost buyer, and the other sellers set arbitrary custom prices above a threshold

Result C4: In the seller’s market, if the number of low-cost buyers is not extremely high $( i . e . , N _ { l } < M )$ , BRS decreases the platform profit. If the number of low-cost buyers is extremely high $( i . e . , N _ { l } \ge M )$ , BRS yields the same platform profit (note that this is a trivial case, and we do not elaborate on this case).

Proof of Result C0: Inserting $\theta _ { h } = \theta , \theta _ { l } = 0$ , and $f ( q ) = q$ or $q ^ { 2 }$ into $\begin{array} { r } { \frac { \partial Q _ { m } ( i ) } { \partial q _ { i } } > 0 , \frac { \partial Q _ { l } ( i ) } { \partial q _ { i } } > 0 } \end{array}$ , and $\frac { \partial Q _ { h } ( i ) } { \partial q _ { i } } > 0$ , we obtain $\begin{array} { r } { \theta < \frac { 1 - \zeta } { f ^ { \prime } ( q _ { 1 } ) } } \end{array}$ and equivalently $\begin{array} { r } { \theta ( 1 - \rho ) < \frac { ( 1 - \zeta ) ( 1 - \rho ) } { f ^ { \prime } ( q _ { 1 } ) } } \end{array}$ . With $f ( q ) = q$ and $\theta < 1 - \zeta$ , this case always occurs because $\begin{array} { r } { \theta < \frac { 1 - \zeta } { f ^ { \prime } ( q _ { 1 } ) } = 1 - \zeta } \end{array}$ always holds. □

To prove Result C1, we first prove a more general result $( \mathrm { i . e . , } \theta _ { l } , \theta _ { h } , Q _ { l } ( i )$ , and $Q _ { h } ( i )$ are in general forms).

Lemma C1: In equilibrium, suppose $Q _ { l } ( i )$ and $Q _ { h } ( i )$ increase in $q _ { i }$ , and the cost parameter of high-cost and low-cost buyers are $\theta _ { h }$ and $\theta _ { l } ,$ , respectively. We have the following:

• Sellers $i \in \{ 1 , \ldots , N _ { l } \}$ get matched with $N _ { l }$ low-cost buyers; these sellers only accept low-cost buyers and offer $U _ { i } ^ { * } = v _ { 0 } +$ $\begin{array} { r } { Q _ { h } ( N + 1 ) + \frac { ( \theta _ { h } - \theta _ { l } ) f \left( q _ { N _ { l } + 1 } \right) } { 1 - \zeta } . } \end{array}$

Sellers $i \in \{ N _ { l } + 1 , \ldots , N \}$ get matched with $N _ { h }$ high-cost buyers; these sellers accept both types of buyers and set the posted price to offer $U _ { i } ^ { * } = v _ { 0 } + Q _ { h } ( N + 1 )$ to high-cost buyers. Among these sellers, seller $N _ { l } + 1$ sets the custom price $s _ { N _ { l } + 1 } ^ { * }$ to offer $U _ { i } ^ { * } =$ $\begin{array} { r } { v _ { 0 } + Q _ { h } ( N + 1 ) + \frac { ( \theta _ { h } - \theta _ { l } ) f \left( q _ { N _ { l } + 1 } \right) } { 1 - \zeta } } \end{array}$ to low-cost buyers, and sellers $i \in \{ N _ { l } + 2 , \ldots , N \}$ set the arbitrary custom prices to offer the utility below $\begin{array} { r } { v _ { 0 } + Q _ { h } ( N + 1 ) + \frac { ( \theta _ { h } - \theta _ { l } ) f \left( q _ { N _ { l } + 1 } \right) } { 1 - \zeta } . } \end{array}$

Seller $i = N + 1$ is unmatched; she accepts both types of buyers and offers $U _ { N + 1 } ^ { * } = v _ { 0 } + Q _ { h } ( N + 1 )$

• Sellers $i \in \{ N + 2 , \ldots , M \}$ are unmatched; each of them offers arbitrary utility in terms of an accept/reject decision. In particular, if she only accepts low-cost buyers (resp. accept all buyers), her arbitrary utility is below $\begin{array} { r } { v _ { 0 } + Q _ { h } ( N + 1 ) + \frac { ( \theta _ { h } - \theta _ { l } ) f \left( q _ { N _ { l } + 1 } \right) } { 1 - \zeta } ( r e s p } \end{array}$ $v _ { 0 } + Q _ { h } ( N + 1 ) )$ .

Proof of Lemma C1: We prove the existence and the uniqueness as follows.

Existence: No seller deviates because: (1) If seller $i \in \{ 1 , \ldots , N _ { l } \}$ decreases the price, she will get less profit. If she increases the price, she will be beaten by seller $N _ { l } + 1$ with a custom price and get less profit (with the technical assumption $\frac { \theta ^ { - } } { 1 - \zeta } < \chi$ that will be discussed later). If seller $i \in \{ 1 , \ldots , N _ { l } \}$ deviates to serve high-cost buyers, she should at least offer utility $v _ { 0 } + Q _ { h } ( N + 1 )$ to compete for these buyers. Since $Q _ { h } ( N + 1 )$ is higher than her matching ability to serve the high-cost buyer, she cannot get matched and thus gets zero profit.

(2) If seller $i \in \{ N _ { l } + 1 , \ldots , N \}$ decreases the price, she will get less profit. If she increases the price, she cannot get matched with a high-cost buyer because seller $N + 1$ will beat her by offering a higher utility. If she deviates from the custom price $s _ { i } ^ { * } ,$ , her profit is not improved because she should at least offer utility $\begin{array} { r } { U _ { i } ^ { * } = v _ { 0 } + Q _ { h } ( N + 1 ) + \frac { \theta f \left( q _ { N _ { l } + 1 } \right) } { 1 - \zeta } } \end{array}$ to capture a low-cost buyer, while she gets lower profit, i.e., $\begin{array} { r } { ( 1 - \zeta ) \left( q _ { i } - q _ { N + 1 } + \frac { \theta f ( q _ { N + 1 } ) } { 1 - \zeta } - \frac { \theta f \left( q _ { N _ { l } + 1 } \right) } { 1 - \zeta } \right) \leq ( 1 - \zeta ) \left( q _ { i } - q _ { N + 1 } + \frac { \theta f ( q _ { N + 1 } ) } { 1 - \zeta } \right) - \theta f ( q _ { i } ) . } \end{array}$

(3) Seller $N + 1$ and the other sellers do not deviate because their highest offered utility $v _ { 0 } + Q _ { l } ( \cdot ) \ ( \mathrm { r e s p . } \ v _ { 0 } + Q _ { h } ( \cdot ) )$ cannot exceed $v _ { 0 } +$ $\begin{array} { r } { Q _ { h } ( N + 1 ) + \frac { ( \theta _ { h } - \theta _ { l } ) f \left( q _ { N _ { l } + 1 } \right) } { 1 - \zeta } \left( \mathrm { r e s p . ~ } v _ { 0 } + Q _ { h } ( N + 1 ) \right) } \end{array}$ . Accordingly, these sellers are unable to get matched and thus cannot deviate to improve their profits.

Uniqueness: We first use proof by contradiction to show that seller $k \in \{ N + 1 , \ldots , M \}$ cannot get matched. Suppose seller $k \in \{ N +$ $1 , \ldots , M \}$ is matched with a type-ω buyer $( \omega \in \{ h , l \} )$ and offers utility $u _ { k } ^ { \omega } .$ Since there are ?? buyers, at least one seller $j \in \{ 1 , \ldots , N \}$ is unmatched (offering utility $u _ { j } ^ { \omega } < u _ { k } ^ { \omega }$ to type-?? buyers) and obtains zero profit. Recall that $u _ { i } ^ { \omega } \leq v _ { 0 } + Q _ { \omega } ( \cdot )$ , and $Q _ { \omega } ( \cdot )$ increases in seller quality $q _ { i } .$ Seller ?? can increase the utility to $\overline { { u _ { J } ^ { \omega } } } > u _ { k } ^ { \omega }$ and get matched with that buyer and obtain a positive profit. Therefore, seller ?? cannot get matched, which contradicts our assumption. This result implies that seller $i \in \{ 1 , \ldots , N \}$ gets matched with either a low-cost buyer or a high-cost buyer.

Then for the pair of any seller ?? $\in \{ 1 , \ldots , N \}$ who will be matched with a high-cost buyer and seller $N + 1 .$ , their reaction curve is shown in the left panel of Figure C1. The unique intersection is at $U _ { i } = v _ { 0 } + Q _ { h } ( N + 1 )$ ), indicating that $N _ { h }$ sellers who are matched with high-cost buyers offer $U _ { i } = v _ { 0 } + Q _ { h } ( N + 1 )$ .

![](/api/attachments/2B5WEFYW/fulltext/images/ccd383a96a6884222ab44767c954b072a9fe53096d5888ad7dc769d725a63941.jpg)

![](/api/attachments/2B5WEFYW/fulltext/images/f0c8b7b988e75e93f9a69ad199e57a3668204d134a790d8baaae7fd5b4ca4d79.jpg)  
Figure C1. Reaction Curves under BRS when $\textcircled { 9 } m \textcircled { 9 } m \textcircled { 9 } m \textcircled { 9 } m \textcircled { 9 }$ , and $\textcircled { 9 } \textcircled { 9 }$ Increase in ??<sub>??</sub>

Next, consider the competition for low-cost buyers among sellers $i \in \{ 1 , \ldots , N \}$ . These sellers compete by increasing utility until they are indifferent between serving low-cost buyers with price $p _ { i } ^ { l }$ and serving high-cost buyers with price $p _ { i } ^ { h }$ , i.e., $( 1 - \zeta ) p _ { i } ^ { l } - \theta _ { l } f ( q _ { i } ) =$ $( 1 - \zeta ) p _ { i } ^ { h } - \theta _ { h } f ( q _ { i } )$ . We obtain $\begin{array} { r } { p _ { i } ^ { l } = p _ { i } ^ { h } - \frac { \theta _ { h } - \theta _ { l } } { 1 - \zeta } f ( q _ { i } ) } \end{array}$ and thus

$$
U _ {i} ^ {l} = U _ {i} ^ {h} + \frac {\theta_ {h} - \theta_ {l}}{1 - \zeta} f (q _ {i}).
$$

Recall that $U _ { i } ^ { h } = v _ { 0 } + Q _ { h } ( N + 1 )$ is the utility that seller ?? should offer to serve high-cost buyers. We thus derive the highest utility that seller ?? is willing to offer to the low-cost buyer:

$$
\widetilde {U} (i) = v _ {0} + Q _ {h} (N + 1) + \frac {\theta_ {h} - \theta_ {l}}{1 - \zeta} f (q _ {i}).
$$

Since $\widetilde { U } ( i )$ increases in the seller quality $q _ { i } , \widetilde { U } ( j ) > \widetilde { U } ( N _ { l } + 1 )$ ) holds for the pair of any seller $j \in \{ 1 , \dots , N _ { l } \}$ and seller $N _ { l } + 1$ . The reaction curve of seller $j \in \{ 1 , \ldots , N _ { l } \}$ and seller $N _ { l } + 1$ is shown in the right panel of Figure C1. The unique intersection is at:

$$
U _ {j} = \widetilde {U} (N _ {l} + 1) = v _ {0} + Q _ {h} (N + 1) + \frac {\theta_ {h} - \theta_ {l}}{1 - \zeta} f \big (q _ {N _ {l} + 1} \big),\tag{C1}
$$

which is the utility offered by seller ?? to get matched with low-cost buyers. Seller $N _ { l } + 1$ sets her custom price to offer $\widetilde U ( N _ { l } + 1 ) = v _ { 0 } +$ $\begin{array} { r } { Q _ { h } ( N + 1 ) + \frac { \theta _ { h } - \theta _ { l } } { 1 - \zeta } f \left( q _ { N _ { l } + 1 } \right) } \end{array}$ but cannot get matched with any low-cost buyer by the tie-breaking assumption. These unique intersections prove the uniqueness. □

Proof of Result C1: Applying Lemma B1 with $i = \left[ i \right] ( \mathrm { i } . \mathrm { e } .$ , the same rank), we obtain the equilibrium under URS. Under BRS, applying Lemma C1 with $\theta _ { h } = \theta$ and $\theta _ { l } = 0$ , we obtain the offered utility in equilibrium. The pricing outcomes are obtained by inserting the utility into $p _ { i } = v _ { 0 } + q _ { i } - U _ { i }$ . In equilibrium, no buyer requests the custom price because doing so cannot improve the utility. □

Discussion of the Technical Assumption: Recall that seller $N _ { l } + 1$ offers the custom price $s _ { N _ { l } + 1 } ^ { * }$ . Since buyers arrive sequentially, seller $N _ { l } + 1$ might be booked by high-cost buyers and thus cannot offer the custom price due to the constraint of the one-unit capacity. This results in no intersection in the reaction curve. To rule out this case, we use the technical assumption $\begin{array} { r } { \frac { \theta } { 1 - \zeta } < \chi . } \end{array}$ . If a seller $j \in \{ 1 , \dots , N _ { l } \}$ raises her price and does not exclude seller $N _ { l } + 1$ from attracting low-cost buyers, the highest price she can set is $q _ { j } - Q _ { h } ( N + 1 )$ , assuming the other sellers set extremely high arbitrary custom prices $( { \mathrm { i . e . } }$ , offer extremely low utility). This represents the best case for seller $j ;$ if seller ?? cannot increase her profit in this best case, she will not deviate. Namely, we give a sufficient condition that ensures the existence of a pure strategy equilibrium. Let Φ denote the probability that seller ?? gets matched. Considering the random arrival sequence, we have:

$$
\Phi = \frac {\sum_ {k = 1} ^ {N _ {h}} C _ {N _ {l}} ^ {1} C _ {N _ {h}} ^ {k} A _ {N _ {l} - 1 + k} ^ {N _ {l} - 1 + k} A _ {N _ {h} - k} ^ {N _ {h} - k} \frac {k}{N _ {h}}}{A _ {N} ^ {N}} = \frac {N _ {l} (N _ {h} - 1) !}{N !} \sum_ {k = 1} ^ {N _ {h}} \frac {(N _ {l} + k - 1) !}{(k - 1) !}.
$$

The denominator follows from the fact that there are $A _ { N } ^ { N }$ possible arrival sequences for ?? buyers. To obtain the numerator, we first select one buyer from the $N _ { l }$ low-cost buyers to be the last one to arrive (labeled as buyer $\Lambda ) ,$ which can be done in $C _ { N _ { l } } ^ { 1 }$ ways. Among the $N _ { h }$ high-cost buyers, we choose ?? to arrive before buyer $\Lambda { ( C _ { N _ { h } } ^ { k } }$ cases), and there are $A _ { N _ { l } - 1 + k } ^ { N _ { l } - 1 + k }$ possible arrival sequences for the $N _ { l } - 1$ low-cost buyers and the selected ?? high-cost buyers. After the arrival of buyer Λ, the remaining $N _ { h } - k$ high-cost buyers arrive $( A _ { N _ { h } - k } ^ { N _ { h } - k }$ sequences). Given that the ?? high-cost buyers have arrived before buyer $\Lambda ,$ seller ?? gets matched if any one of these ?? buyers selects seller $i = N _ { l } + 1$ , who then cannot offer the custom price to a low-cost buyer. Now consider the opposite scenario, where the ?? high-cost buyers do not choose seller $i = N _ { l } + 1$ ; namely, they select the other $N _ { h } - 1$ sellers. This opposite scenario occurs with probability $\begin{array} { r } { \frac { C _ { N _ { h } - 1 } ^ { k } } { C _ { N _ { h } } ^ { k } } = \frac { N _ { h } - k } { N _ { h } } } \end{array}$ , and thus we obtain the probability $\begin{array} { r } { 1 - \frac { N _ { h } - k } { N _ { h } } = \frac { k } { N _ { h } } . } \end{array}$ . The numerator is then obtained by summing up from $k = 1$ to $N _ { h }$

Accordingly, seller ?? does not increase the price when the highest expected profit by deviating is lower than that by not deviating:

$$
\big [ q _ {j} - Q _ {h} (N + 1) \big ] \varPhi <   q _ {j} - \frac {\theta}{1 - \zeta} f \big (q _ {N _ {l} + 1} \big) - Q _ {h} (N + 1),   \forall j \in \{1, \dots , N _ {l} \}.
$$

This implies

$$
\big [ q _ {N _ {l}} - Q _ {h} (N + 1) \big ] \varPhi <   q _ {N _ {l}} - \frac {\theta}{1 - \zeta} f \big (q _ {N _ {l} + 1} \big) - Q _ {h} (N + 1).\tag{C2}
$$

Define

$$
\chi = \frac {(1 - \Phi) (q _ {N _ {l}} - q _ {N + 1})}{q _ {N _ {l} + 1} - (1 - \Phi) q _ {N + 1}}.
$$

We solve inequality (C2) and obtain $\begin{array} { r } { \frac { \theta } { 1 - \zeta } < \chi . } \end{array}$ which is a sufficient condition to ensure that the unique pure strategy equilibrium candidate is indeed an equilibrium.

Proof of Result C2 and $\mathbf { C } 2 ^ { \ast } \colon$ We have the following in the same rank case:

$$
\pi_ {B} = \zeta \sum_ {i = 1} ^ {N _ {l}} \left[ q _ {i} - q _ {N + 1} + \frac {\theta f (q _ {N + 1})}{1 - \zeta} - \frac {\theta f (q _ {N _ {l} + 1})}{1 - \zeta} \right] + \zeta \sum_ {i = N _ {l} + 1} ^ {M} \left[ q _ {i} - q _ {N + 1} + \frac {(1 - \rho) \theta f (q _ {N + 1})}{1 - \zeta} \right],\tag{C3}
$$

$$
\pi_ {U} = \zeta \sum_ {i = 1} ^ {N} \left[ q _ {i} - q _ {N + 1} + \frac {(1 - \rho) \theta f (q _ {N + 1})}{1 - \zeta} \right],\tag{C4}
$$

$$
\frac {\pi_ {B} - \pi_ {U}}{\zeta} = \frac {N _ {l} \theta [ f (q _ {N + 1}) - f (q _ {N _ {l} + 1}) ]}{1 - \zeta} <   0.
$$

Moreover, when $q _ { N + 1 } \to q _ { N _ { l } + 1 } , \pi _ { B } - \pi _ { U } \to 0$ . □

Proof of Result C3: In the seller’s market, sellers do not compete for buyers. Therefore, under URS, all sellers charge the highest price $p _ { i } ^ { S , U * } = v _ { 0 } + q _ { i }$ to leave zero surplus for buyers. Under BRS, if $N _ { l } \ge M$ , all sellers can get matched with low-cost buyers. Hence, no seller competes for low-cost buyers. They only accept low-cost buyers and set $p _ { i } ^ { S , B * } = v _ { 0 } + q _ { i } . \mathrm { I f } N _ { l } < M .$ , sellers compete for low-cost buyers. Similar to the proof of Lemma C1 (and use a similar technical assumption), we can derive the following: In equilibrium, seller $i \in \{ 1 , \ldots , N _ { l } \}$ charges $\begin{array} { r } { p _ { i } ^ { S , B * } = v _ { 0 } + q _ { i } - \frac { \theta f \left( q _ { N _ { l } + 1 } \right) } { 1 - \zeta } ; } \end{array}$ seller $i \in \{ N _ { l } + 1 , \ldots , M \}$ charges $p _ { i } ^ { S , B * } = v _ { 0 } + q _ { i } ;$ seller $N _ { l } + 1$ sets the custom price $s _ { N _ { l } + 1 } ^ { * } = v _ { 0 }$ + $\begin{array} { r } { q _ { N _ { l } + 1 } - \frac { \theta f \left( q _ { N _ { l } + 1 } \right) } { 1 - \zeta } . } \end{array}$ □

Proof of Result C4: If $N _ { l } > M$ , the prices are the same $( { \mathrm { i . e . , } } p _ { i } ^ { S , U * } = p _ { i } ^ { S , B * } = v _ { 0 } + q _ { i } )$ . Therefore, the platform profit, proportional to the sum of prices, is the same under URS and BRS. If $N _ { l } < M$ , we have

$$
\pi^ {S, B} - \pi^ {S, U} = \zeta \sum_ {i = 1} ^ {N _ {l}} \left(- \frac {\theta f (q _ {N _ {l} + 1})}{1 - \zeta}\right) <   0. \square
$$

Lemma C2: Suppose the probability for the seller’s market to occur is $\mu .$ With the reverse rank case, BRS benefits the platform when ?? is low $( \mu < \tilde { \mu } )$ and $\begin{array} { r } { \sum _ { i = 1 } ^ { N _ { l } } q _ { i } > A _ { 1 } } \end{array}$

Proof of Lemma C2: In the seller’s market, the platform profit under BRS and URS is

$$
\pi_ {B} = \zeta \left[ \sum_ {i = 1} ^ {N _ {l}} \left(v _ {0} + q _ {i} - \frac {\theta f (q _ {N _ {l} + 1})}{1 - \zeta}\right) + \sum_ {N _ {l} + 1} ^ {M} \{(v _ {0} + q _ {i} \}) \right],
$$

$$
\pi_ {U} = \zeta \sum_ {i = 1} ^ {M} (v _ {0} + q _ {i}).
$$

We have

$$
\frac {\pi_ {B} - \pi_ {U}}{\zeta} = \mu \sum_ {i = 1} ^ {N _ {l}} \left(- \frac {\theta f (q _ {N _ {l} + 1})}{1 - \zeta}\right) + (1 - \mu) \left[ \sum_ {i = 1} ^ {N _ {l}} q _ {i} - A _ {1} \right].
$$

We can observe that if $\mu = 1 \left( \mathrm { i . e . } \right.$ , the seller’s market), BRS always harms the platform. $\mathbb { f } \mu = 0 ( \mathrm { i . e . } ,$ , the buyer’s market), recall from Proposition 3 that when $\begin{array} { r } { \sum _ { i = 1 } ^ { N _ { l } } q _ { i } > A _ { 1 } } \end{array}$ , BRS improves platform profit. Define

$$
\tilde {\mu} = \frac {\sum_ {i = 1} ^ {N _ {l}} q _ {i} - A _ {1}}{\sum_ {i = 1} ^ {N _ {l}} q _ {i} - A _ {1} + \sum_ {i = 1} ^ {\widetilde {N _ {l}}} \frac {\theta f (q _ {\widetilde {N _ {l}} + 1})}{1 - \zeta}}.
$$

The platform becomes better off when $\begin{array} { r } { \sum _ { i = 1 } ^ { N _ { l } } q _ { i } > A _ { 1 } } \end{array}$ and $\mu < \tilde { \mu } .$ . □

## Appendix D

## Extensions

We discuss the following extensions: (1) incomplete market coverage, (2) more than two types of buyers, (3) positive serving cost parameter for low-cost buyers, (4) imperfect buyer information, and (5) general rank case.

## Incomplete Market Coverage

In our main model, we assume full market coverage with a high basic value $v _ { 0 } .$ . This assumption helps us present our main findings clearly by eliminating the possibility of mismatches. In this section, we extend the model to accommodate a lower $v _ { 0 }$ , where incomplete market coverage may occur. We first demonstrate that BRS can still benefit the platform with reverse rank. When $v _ { 0 }$ is low, it is possible that $v _ { 0 }$ + $Q _ { m } ( i ) < 0 \left( v _ { 0 } + Q _ { h } ( i ) < 0 \right)$ , implying that seller $\textit { i } \in \{ M - N + 1 , \ldots , M \} ( i \in \{ M - N _ { h } + 1 , \ldots , M \} )$ can only provide negative utility and thus remain unmatched under URS (BRS). Compared with our main model, the platform loses the commission income from these unmatched sellers. Let us label the lost commission income as $\zeta X _ { U }$ under URS and $\zeta X _ { B }$ under BRS. With reverse rank, recall that $Q _ { m } ( i )$ and $Q _ { h } ( i )$ increase in ?? $( \mathrm { i . e . } ,$ , decrease in quality). Under URS, we define

$$
i _ {U} = \max \{i | v _ {0} + Q _ {m} (i) <   0 \}.
$$

Here, seller $i _ { U }$ possesses the highest matching ability among those who can only provide negative utility to buyers $( v _ { 0 } + Q _ { m } ( i ) < 0 )$ . In other words, sellers $i \leq i _ { U }$ all satisfy the condition $v _ { 0 } + Q _ { m } ( i ) < 0$ and therefore cannot be matched. Consequently, the platform loses the commission income $\zeta X _ { U }$ from sellers $i \in \{ M - N + 1 , \ldots , i _ { U } \}$ due to negative $\boldsymbol { v } _ { 0 } + \boldsymbol { Q } _ { m } ( i )$ , where

$$
X _ {U} = \left\{ \begin{array}{c l}  \sum_ {i = M - N + 1} ^ {i _ {U}} (q _ {i} - Q _ {m} (M - N)), & \text {if} i _ {U} \geq M - N + 1 \\ 0, & \text {if} i _ {U} <   M - N + 1 \end{array} . \right.
$$

Note that if $i _ { U } < M - N + 1$ , the platform does not lose any commission income, and thus $X _ { U } = 0$

Similarly, under BRS, the platform loses the commission income from sellers $i \in \{ M - N _ { h } + 1 , \ldots , i _ { B } \}$ where

$$
i _ {B} = \max \{i | v _ {0} + Q _ {h} (i) <   0 \},
$$

$$
X _ {B} = \left\{ \begin{array}{c l} \sum_ {i = M - N _ {h} + 1} ^ {i _ {B}} (q _ {i} - Q _ {h} (M - N _ {h})), & \mathrm{if} i _ {B} \geq M - N _ {h} + 1 \\ 0, & \mathrm{if} i _ {B} <   M - N _ {h} + 1 \end{array} . \right.
$$

We then modify Equation (5) by adding $X _ { U }$ and $X _ { B }$ and obtain

$$
\frac {\pi_ {B} - \pi_ {U}}{\zeta} = \sum_ {i = 1} ^ {N _ {l}} q _ {i} - \sum_ {i = M - N + 1} ^ {M - N _ {h} + 1} q _ {i} - \left[ N _ {l} q _ {N _ {l} + 1} + N _ {h} Q _ {h} (M - N _ {h}) - N Q _ {m} (M - N) \right] - X _ {B} + X _ {U}.
$$

BRS thus benefits the platform when $\begin{array} { r } { \sum _ { i = 1 } ^ { N _ { l } } q _ { i } > A _ { 1 } ^ { D } } \end{array}$ , where we define

$$
A _ {1} ^ {D} = \sum_ {i = M - N + 1} ^ {M - N _ {h} + 1} q _ {i} + \left[ N _ {l} q _ {N _ {l} + 1} + N _ {h} Q _ {h} (M - N _ {h}) - N Q _ {m} (M - N) \right] + X _ {B} - X _ {U}.
$$

Next, let us consider the mismatching under URS and BRS. It is obvious that BRS can help alleviate mismatching: Consider an extremely high serving cost parameter $\theta ( { \mathrm { e . g . , } \theta  \infty } )$ . Under URS, no seller-buyer matching pair exists because of the extremely high expected buyer cost. Nevertheless, BRS enables high-quality sellers to cherry-pick low-cost buyers and thus increases the number of matching pairs.

We are also interested in whether BRS can cause more mismatching. To simplify the analysis but convey the key message, we shall assume $f ( q ) = q$ to rule out the intermediate rank case and obtain the following.

Proposition D1: With reverse rank, given that all buyers are matched under URS and $f ( q ) = q ,$ , at least one buyer is unmatched under BRS if the high-cost buyers are too costly to serve, i.e., $\begin{array} { r } { \theta > \left( 1 - \zeta \right) \left( \frac { v _ { 0 } } { q _ { M - N _ { h } + 1 } } + 1 \right) } \end{array}$ . Social welfare decreases if the quality ?? $^ { - N _ { h } + 1 }$ of the unmatched seller is sufficiently high $( q _ { M - N _ { h } + 1 } > \bar { q } )$

Proof of Proposition D1: The statement “with reverse rank, all buyers are matched under URS” requires $v _ { 0 } + Q _ { m } ( M - N + 1 ) > 0$ because seller $i = M - N + 1$ has the lowest matching ability among the sellers matched in our main model.

Under BRS, suppose that at least one buyer is unmatched. This means that $v _ { 0 }$ is low such that $v _ { 0 } + Q _ { h } ( i ) < 0$ holds for at least one seller $i \in \{ M - N _ { h } + \bar { 1 } , \ldots , M \}$ . Among these sellers, seller $i = M - N _ { h } + 1$ has the lowest matching ability in the reverse rank case. Hence, at least a mismatch occurs when $v _ { 0 } + Q _ { h } ( M - N _ { h } + 1 ) < 0$ ; solving this inequality, we obtain $\begin{array} { r } { \theta > \left( 1 - \zeta \right) \left( \frac { v _ { 0 } } { q _ { M - N _ { l } + 1 } } + 1 \right) } \end{array}$ . Importantly, the condition $v _ { 0 } + Q _ { h } ( M - N _ { h } + 1 ) < 0$ does not violate $v _ { 0 } + Q _ { m } ( M - N + 1 ) > 0$ . Consequently, we demonstrate that mismatching can occur under BRS, even when all buyers are matched under URS.

Next, we analyze the social welfare when seller $i = M - N _ { h } + 1$ is unmatched under BRS. We have

$$
S W _ {B} = \sum_ {i = 1} ^ {N _ {l}} q _ {i} + \sum_ {i = M - N _ {h} + 2} ^ {M} (q _ {i} - \theta q _ {i}),
$$

$$
S W _ {U} = \sum_ {i = M - N + 1} ^ {M} (q _ {i} - (1 - \rho) \theta q _ {i}),
$$

$$
S W _ {B} - S W _ {U} = B _ {1} - (1 - \theta) q _ {M - N _ {h} + 1},
$$

where

$$
B _ {1} = N _ {l} \left(\frac {\sum_ {i = 1} ^ {N _ {l}} q _ {i}}{N _ {l}} - \frac {\sum_ {i = M - N + 1} ^ {M - N _ {h}} q _ {i}}{N _ {l}}\right) + \theta N _ {h} \left(\frac {\sum_ {i = M - N + 1} ^ {M} q _ {i}}{N} - \frac {\sum_ {i = M - N _ {h} + 1} ^ {M} q _ {i}}{N _ {h}}\right) > 0.
$$

When the quality of the unmatched seller is high, i.e., $\begin{array} { r } { q _ { M - N _ { h } + 1 } > \bar { q } = \frac { B _ { 1 } } { 1 - \theta } , } \end{array}$ we have $S W _ { B } - S W _ { U } < 0 .$ □

Proposition D1 points out a potential inefficiency of BRS. With incomplete market coverage (small $v _ { 0 } )$ , BRS may result in fewer matching pairs compared with URS, thus harming social welfare. This is because the segmentation effect raises the cost (and thus price) to serve thos high-cost buyers under BRS (as opposed to a mixture of sellers under URS). As a result, the high-cost buyers are unmatched under BRS when $v _ { 0 }$ is small, even though they would have been matched under URS. Although BRS improves resource allocation by segmenting sellerbuyer pairs as discussed in the main paper, it harms social welfare when the negative impact caused by the fewer matching pairs is more pronounced (i.e., the quality $q _ { M - N _ { h } + 1 }$ of the unmatched seller is high).

## More Than Two Types of Buyers

In the model presented previously, we only consider two types of buyers with $\theta _ { h }$ and $\theta _ { l }$ . This assumption simplifies the matching pattern and shows that intermediate-quality sellers are always driven out. However, it enables us to convey the key message that BRS can benefit the platform when it alleviates the withdrawal of high-quality sellers. In this section, we seek to understand how considering three consumer types affects the matching outcome. We now assume that there are three types of buyers: low-cost buyers with $\theta _ { l } = 0 $ , middle-cost buyers with ${ \widehat { \theta } } ,$ and high-cost buyers with $\theta _ { h } = \theta ( \theta > \widehat { \theta } > 0 )$ , with the proportion $\rho _ { l } , \rho _ { m } ,$ and $\rho _ { h } .$ , respectively $( \rho _ { l } + \rho _ { m } + \rho _ { h } = 1 )$ ). We redefine the expected buyer cost as $\rho _ { m } \hat { \theta } + \rho _ { h } \theta$ and have the following.

Lemma D1: With three types of buyers, when the expected buyer cost is high (i.e., $\begin{array} { r } { \rho _ { m } \widehat { \theta } + \rho _ { h } \theta > \frac { 1 - \zeta } { f ^ { \prime } ( q _ { M } ) } \big ) , } \end{array}$ , the reverse rank case occurs under URS. In this case, the intermediate-quality sellers are matched only when the cost function is convex $( i . e . , f ( q ) = q ^ { 2 } )$ and the serving cost parameter of middle-cost buyer $\hat { \theta }$ is intermediate $( i . e . , \underline { { { \theta } } } < \hat { \theta } < \bar { \theta } )$ ; otherwise, high-quality and low-quality sellers are matched, while the intermediate-quality sellers are unmatched.

Proof of Lemma D1: We redefine the matching ability under URS as

$$
Q _ {m} (i) = q _ {i} - \frac {\rho_ {m} \hat {\theta} + \rho_ {h} \theta}{1 - \zeta} f (q _ {i}),\tag{D1}
$$

and define the matching ability for middle-cost buyers (let ??̂ label “middle-cost”) under BRS as

$$
Q _ {\widehat {m}} (i) = q _ {i} - \frac {\widehat {\theta}}{1 - \zeta} f (q _ {i}).
$$

Sort $Q _ { \widehat { m } } ( i )$ into descending order for sellers $i \in \{ N \rho _ { l } + 1 , \ldots , M - N \rho _ { h } \}$ . We have

$$
Q _ {\hat {m}} [ 1 ] > Q _ {\hat {m}} [ 2 ] > \dots > Q _ {\hat {m}} [ M - N (\rho_ {l} + \rho_ {h}) ],
$$

where [??] represents seller ?? whose $Q _ { \widehat { m } } ( i )$ ranks ?? among sellers $i \in \{ N \rho _ { l } + 1 , \ldots , M - N \rho _ { h } \}$ . The matching ability under BRS for low and high-cost buyers follows the previous definition $( \mathrm { i } . \mathbf { e } . , Q _ { l } ( i ) = q _ { i }$ and $\begin{array} { r } { Q _ { h } ( i ) = q _ { i } - \frac { \theta } { 1 - \zeta } f ( q _ { i } ) ) } \end{array}$ .

By Equation (D1), when $\begin{array} { r } { \rho _ { m } \widehat { \theta } + \rho _ { h } \theta > \frac { 1 - \zeta } { f ^ { \prime } ( q _ { M } ) } , Q _ { m } ( i ) = q _ { i } - \frac { \rho _ { m } \widehat { \theta } + \rho _ { h } \theta } { 1 - \zeta } f ( q _ { i } ) } \end{array}$ decreases in $q _ { i } ,$ and reverse rank occurs. Next, we prove the existence and the uniqueness of the following equilibrium when reverse rank occurs: When $f ( q ) = q ^ { 2 }$ and

$$
\underline {{\theta}} = \frac {1 - \zeta}{f ^ {\prime} (q _ {N \rho_ {l} + 1})} <   \hat {\theta} <   \bar {\theta} = \frac {1 - \zeta}{f ^ {\prime} (q _ {M - N \rho_ {h}})},
$$

the $N \rho _ { l }$ high-quality sellers $i \in \{ 1 , \ldots , N \rho _ { l } \}$ are matched with low-cost buyers and offer $u _ { i } = v _ { 0 } + q _ { N \rho _ { l } + 1 }$ . The $N \rho _ { h }$ low-quality sellers $i \in$ $\{ M - N \rho _ { h } + 1 , \dots , M \}$ are matched with high-cost buyers and offer $u _ { i } = v _ { 0 } + Q _ { h } ( M - N \rho _ { h } )$ . The $N \rho _ { m }$ intermediate-quality sellers ?? ∈ $\{ [ 1 ] , \dots , [ N \rho _ { m } ] \}$ are matched with middle-cost buyers and offer $u _ { i } = v _ { 0 } + Q _ { \widehat { m } } [ N \rho _ { m } + 1 ]$ , and seller $[ N \rho _ { m } + 1 ]$ offers $u _ { [ N \rho _ { m } + 1 ] } = v _ { 0 } +$ $Q _ { \widehat { m } } [ N \rho _ { m } + 1 ] .$

For high and low-quality sellers who are matched with low and high-cost buyers, the proof is the same as that for Proposition 2. This is because the newly added intermediate-quality sellers cannot beat high (low)-quality sellers to compete for low (high)-cost buyers (i.e., $Q _ { l } ( i )$ increases in $q _ { i }$ and $Q _ { h } ( i )$ decreases in $q _ { i } )$ . Now we prove the existence and the uniqueness of the equilibrium regarding intermediate-quality sellers.

Existence: Consider seller $i \in \{ [ 1 ] , \ldots , [ N \rho _ { m } ] \}$ . She does not decrease the price because doing so decreases the profit. She does not increase the price because seller $[ N \rho _ { m } + 1 ]$ ] offers a higher utility than her, which would make seller ?? unmatched. Besides, seller ?? does not deviate to compete for low (high)-cost buyers because the highest utility that she can offer to these buyers is lower than the offered utility of $N \rho _ { l }$ $( N \rho _ { h } )$ high (low)-quality sellers.

Uniqueness: Consider the reaction curve in the competition for middle-cost buyers among intermediate-quality sellers $j \in \{ [ 1 ] , \dots , [ N \rho _ { m } ] \}$ and seller $[ N \rho _ { m } + 1 ]$ . Similar to Figure B1, there is only one intersection at $u _ { i } = v _ { 0 } + Q _ { \widehat { m } } [ N \rho _ { m } + 1 ]$

Furthermore, we prove by contradiction that the intermediate quality sellers are not matched when $\begin{array} { r } { \widehat { \theta } \leq \frac { 1 - \zeta } { f ^ { \prime } \left( q _ { N \rho _ { l } + 1 } \right) } \operatorname { o r } \widehat { \theta } \geq \frac { 1 - \zeta } { f ^ { \prime } \left( q _ { M - N \rho _ { h } } \right) } } \end{array}$ . Suppose that there exist intermediate quality sellers who are matched. Note that seller $i \in \{ M - N \mathsf { p } _ { h } + 1 , \ldots , M \} ( \mathrm { r e s p } , i \in \{ 1 , \ldots , N \rho _ { l } \} )$ can always get matched because their matching ability for high-cost (resp. low-cost) buyers are the $N \rho _ { h } \ ( { \mathrm { r e s p . } } \ N \rho _ { l } )$ highest. Therefore, the unmatched sellers have $q _ { i }$ such that $q _ { M - N ( 1 - \rho _ { h } ) } \leq q _ { i } \leq q _ { N \rho _ { l } + 1 }$ . The statement “intermediate-quality sellers are matched” implies that at least one seller with higher quality (denoted by ??<sup>̅</sup> ) and one with lower quality (denoted by $\underline { { k } } )$ are unmatched (see Figure D1). If $\begin{array} { r } { \widehat { \theta } \leq \frac { 1 - \zeta } { f ^ { \prime } \left( q _ { N \rho _ { l } + 1 } \right) } , Q _ { \widehat { m } } ( i ) } \end{array}$ increases in $q _ { i }$ when $q _ { i } \le q _ { N \rho _ { l } + 1 }$ . Then seller $\bar { k }$ can beat the intermediate-quality sellers and get matched because her matching ability $Q _ { \widehat m } ( \cdot )$ is higher. This is a contradiction. If $\begin{array} { r } { { \hat { \theta } \geq \frac { 1 - \zeta } { f ^ { \prime } \left( q _ { M - N \rho _ { h } } \right) } , Q _ { \widehat { m } } ( i ) } } \end{array}$ decreases in $q _ { i }$ when $q _ { i } \geq q _ { M - N \rho _ { h } } .$ Then seller $\underline { { k } }$ can beat the intermediate-quality sellers and get matched because her matching ability $Q _ { \widehat m } ( \cdot )$ is higher. This is a contradiction.

Note that the condition $\begin{array} { r } { \frac { 1 - \zeta } { f ^ { \prime } \left( q _ { N \rho _ { l } + 1 } \right) } < \hat { \theta } < \frac { 1 - \zeta } { f ^ { \prime } \left( q _ { M - N \rho _ { h } } \right) } } \end{array}$ in Lemma D1 only holds with $f ( q ) = q ^ { 2 }$ . It never holds with $f ( q ) = q$ because $\begin{array} { r } { \frac { 1 - \zeta } { f ^ { \prime } \left( q _ { N \rho _ { l } + 1 } \right) } = \frac { 1 - \zeta } { f ^ { \prime } ( q _ { M - N \rho _ { h } } ) } . \ \boxed { \begin{array} { r l r l } \end{array} } } \end{array}$

Recall Figure 6 for the matching outcome in our main model with two types of buyers: High-quality and low-quality sellers are matched, while the intermediate-quality sellers are unmatched. Lemma D1 confirms that even with three types of buyers, this matching outcome still qualitatively holds. Additionally, we find that the intermediate-quality sellers get matched with middle-cost buyers when the cost function is convex $( { \mathrm { i . e . , } } f ( q ) = q ^ { 2 } )$ and the cost parameter $\hat { \theta }$ is intermediate $( \underline { { { \theta } } } < \hat { \theta } < \bar { \theta } )$ , as shown in Figure D1. It is noteworthy that with a linear cost function $f ( q ) = q$ , the intermediate-quality sellers are always unmatched.

<table><tr><td rowspan="3"></td><td colspan="4"> $N\rho_h$  high-cost buyers</td><td colspan="4"> $N\rho_m$  middle-cost buyers</td><td colspan="4"> $N\rho_l$  low-cost buyers</td></tr><tr><td rowspan="2">low</td><td colspan="3">matching</td><td colspan="3">matching</td><td colspan="3">matching</td><td colspan="2">high</td></tr><tr><td> $q_M$ </td><td>......</td><td> $q_{M-N\rho_h+1}$ </td><td>......</td><td colspan="3">sellers  $i \in \{[1], ..., [N\rho_m]\}$  with  $Q_{\hat{m}}[1], ..., Q_{\hat{m}}[N\rho_m]$ </td><td> $q_{N\rho_l}$ </td><td>......</td><td colspan="2"> $q_1$ </td></tr></table>

Figure D1. Matching Pattern with Three Types of Sellers When $i i \pmb { \left( 0 \pmb { \eta } \right) } = \pmb { \left( 0 \pmb { \eta } \right) }$ and $\textcircled { 1 } \times \textcircled { 2 } \textcircled { 2 }$

## Positive Serving Cost Parameter for Low-cost Buyers

This section relaxes the assumption $\theta _ { l } = 0$ . Instead, we assume that the low-cost buyers are not too costly to serve, i.e., $\begin{array} { r } { 0 < \theta _ { l } < \frac { 1 - \zeta } { f ^ { \prime } ( q _ { 1 } ) } , } \end{array}$ according to the observation on Airbnb: The low-cost guests with good reviews behave with good manners and keep the place tidy; they significantly reduce the risk of sellers and are welcomed by hosts. This assumption enables us to focus on the same rank and the reverse rank cases discussed previously. Now the expected buyer cost becomes $\rho \theta _ { l } + ( 1 - \rho ) \theta _ { h }$ . We show that our main results still qualitatively hold.

Redefine the matching ability $\begin{array} { r } { Q _ { m } ^ { D } ( i ) = q _ { i } - \frac { \rho \theta _ { l } + ( 1 - \rho ) \theta _ { h } } { 1 - \zeta } f ( q _ { i } ) } \end{array}$ under URS, $\begin{array} { r } { Q _ { l } ^ { D } ( i ) = q _ { i } - \frac { \theta _ { l } } { 1 - \zeta } f ( q _ { i } ) } \end{array}$ for low-cost and $\begin{array} { r } { Q _ { h } ^ { D } ( i ) = q _ { i } - \frac { \theta _ { h } } { 1 - \zeta } f ( q _ { i } ) } \end{array}$ for high-cost buyers under BRS. The expressions $v _ { 0 } + Q _ { m } ^ { D } ( i ) , v _ { 0 } + Q _ { l } ^ { D } ( i )$ , and $\boldsymbol { v } _ { 0 } + \boldsymbol { Q } _ { h } ^ { D } ( i )$ represent the highest utility that seller ?? can offer conditional on obtaining a positive profit for the mixture of buyers under URS, for low-cost buyers under BRS, and for high-cost buyers under BRS, respectively.

Proposition D2: In equilibrium, we have the following.

(a) In the reverse rank case (the expected buyer cost is high, i.e., $\begin{array} { r } { \rho \theta _ { l } + ( 1 - \rho ) \theta _ { h } > \frac { 1 - \zeta } { f ^ { \prime } ( q _ { M } ) } , } \end{array}$ BRS benefits the platform when the aggregate quality of top sellers is high $( \sum _ { i = 1 } ^ { N \rho } q _ { i } > A _ { 2 } ^ { D } )$ .

(b) In the same rank case where $Q _ { m } ^ { D } ( i )$ $Q _ { l } ^ { D } ( i ) .$ , and $Q _ { h } ^ { D } ( i )$ all increase in $q _ { i } ,$ , BRS always harms the platform.

Proof of Proposition D2: Since $\begin{array} { r } { \theta _ { l } < \frac { 1 - \zeta } { f ^ { \prime } ( q _ { 1 } ) } , \mathrm { ~ w e ~ h a v e ~ } \frac { \partial Q _ { l } ^ { D } ( i ) } { \partial q _ { i } } > 0 , \forall i ; } \end{array}$ ; that is, high-quality sellers have high matching abilities by cherrypicking low-cost buyers. We focus on the same rank case and the reverse rank case discussed in our main paper.

The reverse rank case occurs when $\frac { \partial Q _ { m } ^ { D } ( i ) } { \partial q _ { i } } < 0 , \forall i ;$ that is, $\begin{array} { r } { \rho \theta _ { l } + ( 1 - \rho ) \theta _ { h } > \frac { 1 - \zeta } { f ^ { \prime } ( q _ { M } ) } . } \end{array}$ . This also implies $\begin{array} { r } { \frac { \partial Q _ { h } ^ { D } ( i ) } { \partial q _ { i } } < 0 , } \end{array}$ , ∀?? because $\theta _ { h } > \rho \theta _ { l } +$ $\begin{array} { r } { ( 1 - \rho ) \theta _ { h } > \frac { 1 - \zeta } { f ^ { \prime } ( q _ { M } ) } . } \end{array}$ . In other words, $Q _ { h } ^ { D } ( i )$ decreases in $q _ { i }$ .

The same rank case occurs when $\begin{array} { r } { \frac { \partial Q _ { m } ^ { D } ( i ) } { \partial q _ { i } } > 0 \mathrm { ~ a n d } \frac { \partial Q _ { h } ^ { D } ( i ) } { \partial q _ { i } } > 0 , \forall i . } \end{array}$

By replacing $Q _ { h } ( i )$ and $Q _ { l } ( i )$ with $Q _ { h } ^ { D } ( i )$ and $Q _ { l } ^ { D } ( i )$ , Lemma B2 and C1 yield Result D1 and $\mathrm { D } 2 \colon$

Result D1 (reverse rank): In equilibrium of the reverse rank case with BRS, sellers $i \in \{ 1 , \ldots , N _ { l } \}$ are matched with $N _ { l }$ low-cost buyers; these sellers only accept low-cost buyers and offer $U _ { i } ^ { * } = v _ { 0 } + Q _ { l } ^ { D } ( N _ { l } + 1 )$ . Sellers $i \in \{ M - N _ { h } + 1 , \ldots , M \}$ are matched with $N _ { h }$ high-cost buyers; these sellers accept both types of buyers and offer $U _ { i } ^ { * } = v _ { 0 } + Q _ { h } ^ { D } ( M - N _ { h } )$ . Moreover, seller $N _ { l } + 1$ offers $U _ { N _ { l } + 1 } ^ { * } = v _ { 0 } +$ $Q _ { l } ^ { D } ( N _ { l } + 1 )$ and only accepts a low-cost buyer, seller $M - N _ { h }$ offers $U _ { i } ^ { * } = v _ { 0 } + Q _ { h } ^ { D } ( M - N _ { h } )$

Result D2 (same rank): Suppose the matching abilities all increase in $q _ { i } .$ In equilibrium with BRS, sellers $i \in \{ 1 , \ldots , N _ { l } \}$ are matched with $N _ { l }$ low-cost buyers; these sellers only accept low-cost buyers and offer $\begin{array} { r } { U _ { i } ^ { * } = v _ { 0 } + Q _ { h } ^ { D } ( N + 1 ) + \frac { \theta _ { h } - \theta _ { l } } { 1 - \zeta } f \bigl ( q _ { N _ { l } + 1 } \bigr ) } \end{array}$ . Sellers $i \in \{ N _ { l } + 1 , \ldots , N \}$ are matched with $N _ { h }$ high-cost buyers; these sellers accept both types of buyers and offer $U _ { i } ^ { * } = v _ { 0 } + Q _ { h } ^ { D } ( N + 1 )$ ). Moreover, seller $N _ { l } + 1$ sets the custom price $s _ { N _ { l } + 1 } ^ { * }$ to offer the low-cost buyer $U _ { N _ { l } + 1 } ^ { * } = v _ { 0 } + Q _ { l } ^ { D } ( N _ { l } + 1 )$ . Seller $N + 1$ offers $U _ { i } ^ { * } = v _ { 0 } + Q _ { h } ^ { D } ( N + 1 )$ .

We obtain the platform profit under BRS with the same and reverse rank by inserting Result D1 and D2 into Equation (B1) and (B2). The equilibrium under URS follows by replacing $Q _ { m } ( i )$ with $Q _ { m } ^ { D } ( i )$ in Lemma B1; we then derive the platform profit under URS by plugging the equilibrium outcome into Equation (C3) and (C4). We have the following:

$$
\pi_ {U, \mathrm{same}} ^ {D} = \zeta \sum_ {i = 1} ^ {N} [ q _ {i} - Q _ {m} ^ {D} (N + 1) ],
$$

$$
\pi_ {U, \mathrm{reverse}} ^ {D} = \zeta \sum_ {i = M - N + 1} ^ {M} [ q _ {i} - Q _ {m} ^ {D} (M - N) ],
$$

$$
\pi_ {B, \mathrm{same}} ^ {D} = \zeta \sum_ {i = 1} ^ {N _ {l}} \Big [ q _ {i} - Q _ {h} ^ {D} (N + 1) - \frac {\theta_ {h} - \theta_ {l}}{1 - \zeta} f \big (q _ {N _ {l} + 1} \big) \Big ] + \zeta \sum_ {i = N _ {l} + 1} ^ {N} [ q _ {i} - Q _ {h} ^ {D} (N + 1) ],
$$

$$
\pi_ {B, \mathrm{reverse}} ^ {D} = \zeta \sum_ {i = 1} ^ {N _ {l}} [ q _ {i} - Q _ {l} ^ {D} (N _ {l} + 1) ] + \zeta \sum_ {i = M - N _ {h} + 1} ^ {M} [ q _ {i} - Q _ {h} ^ {D} (M - N _ {h}) ].
$$

In the same rank case, $\pi _ { B , \mathrm { s a m e } } ^ { D } - \pi _ { U , \mathrm { s a m e } } ^ { D } < 0$ always holds. In the reverse rank case, $\begin{array} { r } { \pi _ { \mathrm { B , r e v e r s e } } ^ { \mathrm { D } } - \pi _ { \mathrm { U , r e v e r s e } } ^ { \mathrm { D } } > 0 \Leftrightarrow \sum _ { i = 1 } ^ { N \rho } q _ { i } > A _ { 2 } ^ { D } } \end{array}$ , where

$$
A _ {2} ^ {D} = \sum_ {i = M - N + 1} ^ {M - N _ {h}} q _ {i} + N _ {l} Q _ {l} ^ {D} (N _ {l} + 1) + N _ {h} Q _ {h} ^ {D} (M - N _ {h}) - N Q _ {m} ^ {D} (M - N). \square
$$

## Imperfect Buyer Information

So far, we have assumed perfect seller and buyer information. Note that the imperfect seller information has been widely studied in the literature (Akerlof, 1978; Kwark et al., 2014). To highlight the uniqueness of BRS, we examine the imperfect buyer information in this extension. Let $\beta > \frac { 1 } { 2 }$ denote the probability that the type of buyer is correctly indicated by the seller review, and thus $\beta$ represents the accuracy of the seller review (Kwark et al., 2014). A low-cost (high-cost) buyer gets good (bad) reviews with probability $\beta$ and bad (good) reviews with probability $1 - \beta$ . We assume a not extremely low level of accuracy $( \beta > \bar { \beta }$ where $\hat { \beta }$ is defined later) to ensure that the matching ability to serve low-cost buyers increases in quality; this enables us to focus on the reverse and the same rank case discussed in the main paper.

A high (low)-cost buyer gets bad reviews $\boldsymbol { r } = \boldsymbol { \theta } _ { h }$ (good reviews $r = \theta _ { l } )$ with probability ?? and good reviews $r = \theta _ { l }$ (bad reviews $r = \theta _ { h } )$ with probability $1 - \beta$ . The Bayesian equation suggests

$$
P r (\theta_ {l} | r = \theta_ {l}) = \frac {P r (r = \theta_ {l} | \theta_ {l}) P r (\theta_ {l})}{P r (r = \theta_ {l} | \theta_ {l}) P r (\theta_ {l}) + P r (r = \theta_ {l} | \theta_ {h}) P r (\theta_ {h})} = \frac {\beta \rho}{\beta \rho + (1 - \beta) (1 - \rho)},
$$

$$
P r (\theta_ {h} | r = \theta_ {l}) = \frac {P r (r = \theta_ {l} | \theta_ {h}) P r (\theta_ {h})}{P r (r = \theta_ {l} | \theta_ {l}) P r (\theta_ {l}) + P r (r = \theta_ {l} | \theta_ {h}) P r (\theta_ {h})} = \frac {(1 - \beta) (1 - \rho)}{\beta \rho + (1 - \beta) (1 - \rho)},
$$

$$
P r (\theta_ {h} | r = \theta_ {h}) = \frac {P r (r = \theta_ {h} | \theta_ {h}) P r (\theta_ {h})}{P r (r = \theta_ {h} | \theta_ {h}) P r (\theta_ {h}) + P r (r = \theta_ {h} | \theta_ {l}) P r (\theta_ {l})} = \frac {\beta (1 - \rho)}{\beta (1 - \rho) + (1 - \beta) \rho},
$$

$$
P r (\theta_ {l} | r = \theta_ {h}) = \frac {P r (r = \theta_ {h} | \theta_ {l}) P r (\theta_ {l})}{P r (r = \theta_ {h} | \theta_ {h}) P r (\theta_ {h}) + P r (r = \theta_ {h} | \theta_ {l}) P r (\theta_ {l})} = \frac {(1 - \beta) \rho}{\beta (1 - \rho) + (1 - \beta) \rho}.
$$

The perceived cost parameter is thus $\begin{array} { r } { E [ \theta | r = \theta _ { l } ] = \frac { ( 1 - \beta ) ( 1 - \rho ) } { \beta \rho + ( 1 - \beta ) ( 1 - \rho ) } \theta } \end{array}$ after observing $r = \theta _ { l }$ and $\begin{array} { r } { E [ \theta | r = \theta _ { h } ] = \frac { \beta ( 1 - \rho ) } { \beta ( 1 - \rho ) + ( 1 - \beta ) \rho } \theta } \end{array}$ after observing $\boldsymbol { r } = \boldsymbol { \theta } _ { h }$ . The proportions of buyers with good and bad reviews are $\tilde { \rho } = \rho \beta + ( 1 - \rho ) ( 1 - \beta )$ and $1 - \tilde { \rho } ,$ , and the numbers are denoted by $N _ { g } = \tilde { \rho } N$ and $N _ { b } = ( 1 - \tilde { \rho } ) N$ , respectively. Similar to Equation (3), we can define the matching ability to serve a low-cost buyer as:

$$
Q _ {l} ^ {E} (i) = q _ {i} - \frac {E [ \theta | r = \theta_ {l} ]}{1 - \zeta} f (q _ {i}).
$$

The following demonstrates the robustness of our main findings.

Proposition D3: When seller reviews are not perfect but the accuracy is not extremely low $( \beta > \bar { \beta } )$ , we have the following:

In the reverse rank case, BRS makes the platform better off when the aggregate quality of top sellers is high (i.e., $\textstyle \sum _ { i = 1 } ^ { N _ { l } } q _ { i } > A _ { 3 } ^ { D } )$ . Otherwise, the platform is worse off;

• In the same rank case where the matching abilities all increase in $q _ { i } ,$ BRS always makes the platform worse off.

Proof of Proposition D3: The statement ${ } ^ { \mathfrak { s } } Q _ { l } ^ { E } ( i )$ increases in $q _ { i } , \ "$ or

$$
\frac {\partial Q _ {l} ^ {E} (i)}{\partial q _ {i}} = 1 - \frac {(1 - \beta) (1 - \rho)}{\beta \rho + (1 - \beta) (1 - \rho)} \frac {f ^ {\prime} (q _ {i})}{1 - \zeta} \theta > 0, \forall i
$$

is equivalent to $\begin{array} { r } { \beta > \bar { \beta } ( \bar { \beta } = \frac { ( 1 - \rho ) ( 1 - D _ { x } ) } { ( 1 - \rho ) ( 1 - D _ { x } ) + \rho D _ { x } } } \end{array}$ where $\begin{array} { r } { D _ { x } = \frac { 1 - \zeta } { f ^ { \prime } ( q _ { 1 } ) } ) } \end{array}$ , under which high-quality sellers have the highest matching abilities to get matched with good-review buyers. Plugging $\theta _ { h } = E [ \theta | \dot { r } = \dot { \theta } _ { h } ] , \theta _ { l } = E [ \theta | r = \theta _ { l } ] , \rho = \rho ^ { \prime } , N _ { l } = N _ { g }$ , and $N _ { h } = N _ { b }$ into Lemma B1, we obtain the equilibrium under URS; again, plugging them into Lemmas B2 and C1, respectively, we obtain the following equilibrium under BRS:

Reverse Rank: High-quality seller $i \in \{ 1 , \ldots , N _ { g } \}$ get matched with $N _ { g }$ good-review buyers and charge $p _ { i } ^ { B * } = q _ { i } - q _ { N _ { g } } + \frac { E [ \theta | r = \theta _ { l } ] q _ { N _ { g } } } { 1 - \zeta }$ ; low-quality sellers $i \in \{ M - N _ { b } + 1 , \ldots , M \}$ get matched with $N _ { b }$ bad-review buyers and charge $p _ { i } ^ { B * } = q _ { i } - q _ { M - N _ { b } } + \frac { E [ \theta | r = \theta _ { l } ] q _ { M - N _ { b } } } { 1 - \zeta } ,$

By Equation (B2) and (B1), we have $\begin{array} { r } { \pi _ { B , \mathrm { r e v e r s e } } ^ { E } - \pi _ { U , \mathrm { r e v e r s e } } ^ { E } > 0 \Leftrightarrow \sum _ { i = 1 } ^ { N _ { g } } q _ { i } > A _ { 3 } ^ { D } } \end{array}$ , where

$$
A _ {3} ^ {D} = \sum_ {i = M - N + 1} ^ {M - N _ {b}} q _ {i} + N _ {g} Q _ {l} ^ {E} (N _ {g} + 1) + N _ {b} Q _ {h} ^ {E} (M - N _ {b}) - N Q _ {m} ^ {E} (M - N),
$$

with the matching ability $Q _ { m } ^ { E } ( M - N ) = q _ { M - N } - \frac { ( 1 - \rho ) \theta f ( q _ { M - N } ) } { 1 - \zeta } , Q _ { l } ^ { E } \bigl ( N _ { g } + 1 \bigr ) = q _ { N _ { g } + 1 } - \frac { E [ \theta | r = \theta _ { l } ] f \bigl ( q _ { N _ { g } + 1 } \bigr ) } { 1 - \zeta } , \mathrm { a n d } Q _ { h } ^ { E } ( M - N _ { b } ) = q _ { M - N _ { b } } - 1$ $\frac { \relax E [ \theta | r = \theta _ { h } ] f \left( q _ { M - N _ { b } } \right) } { 1 - \zeta } ;$ , respectively.

Same Rank: Suppose the matching abilities all increase in ??<sub>??</sub>. High-quality sellers $i \in \{ 1 , \ldots , N _ { g } \}$ get matched with $N _ { g }$ good-review buyers and charge $p _ { i } ^ { B ^ { * } } = q _ { i } - q _ { N + 1 } + \frac { E [ \theta | r = \theta _ { h } ] q _ { N + 1 } } { 1 - \zeta } - \frac { ( E [ \theta | r = \theta _ { h } ] - E [ \theta | r = \theta _ { l } ] ) f \big ( q _ { N _ { g } + 1 } \big ) } { 1 - \zeta }$ ; low-quality sellers $i \in \{ N _ { g } + 1 , \ldots , N \}$ get matched with $N _ { b }$ bad-review buyers and charge $\begin{array} { r } { p _ { i } ^ { B * } = q _ { i } - q _ { N + 1 } + \frac { E [ \theta | r = \theta _ { h } ] q _ { N + 1 } } { 1 - \zeta } } \end{array}$ ; seller $N _ { g } + 1$ sets the custom price $s _ { N _ { g } + 1 } ^ { * }$ to offer $U _ { N _ { g } + 1 } ^ { * } = v _ { 0 } +$ $q _ { N _ { g } + 1 } - q _ { N + 1 } + \frac { E [ \theta | r = \theta _ { h } ] q _ { N + 1 } } { 1 - \zeta } - \frac { ( { \varepsilon } [ \theta | r = \theta _ { h } ] - { \varepsilon } [ \theta | r = \theta _ { l } ] ) f \big ( q _ { N _ { g } + 1 } \big ) } { 1 - \zeta }$ for low-cost buyers.

By Equation (C3) and (C4), we have

$$
\pi_ {B, \mathrm{same}} - \pi_ {U, \mathrm{same}} = \frac {N}{1 - \zeta} \frac {(2 \beta - 1) (1 - \rho) \rho}{\beta (1 - \rho) + (1 - \beta) \rho} \Bigl (f (q _ {N + 1}) - f (q _ {N _ {g} + 1}) \Bigr) <   0
$$

because $f ( q _ { N + 1 } ) < f \left( q _ { N _ { g } + 1 } \right)$ and $\begin{array} { r } { \frac { \left( 2 \beta - 1 \right) \left( 1 - \rho \right) \rho } { \beta \left( 1 - \rho \right) + \left( 1 - \beta \right) \rho } > 0 . } \end{array}$ given $\beta > { \frac { 1 } { 2 } } .$ □

## General Rank Case

We study the most interesting same rank and reverse rank cases in the main paper. The following presents the matching outcome in the general rank case where high-quality sellers may be partially driven out of the market under URS, i.e., the intermediate rank case.

Lemma D2: Under URS, ?? buyers are matched with the sellers whose matching abilities $Q _ { m } ( \cdot )$ rank from 1 to ??. Under BRS, $N _ { l }$ low-cost buyers are matched with the highest-quality seller $i \in I = \{ 1 , \ldots , N _ { l } \} ; N _ { h }$ high-cost buyers are matched with the sellers $j \notin I$ whose matching abilities $Q _ { h } ( \cdot )$ rank from 1 to $N _ { h }$

Proof of Lemma D2: By Lemma B1, we obtain the matching outcome under URS. We prove the matching outcome under BRS by contradiction.

Let us first focus on seller ?? ∈ ??. To show that she is matched with a low-cost buyer, we prove that she is not unmatched, and that she is not matched with a high-cost buyer. (1) Suppose seller ?? is unmatched. Then, she can always increase the offered utility to get matched with a low-cost buyer because her matching ability is among the $N _ { l }$ highest ones, leading to a contradiction. (2) Suppose seller ?? is matched with a high-cost buyer by offering ??<sup>̅</sup>. If seller ?? deviates to attract a low-cost buyer, her highest offered utility is $\begin{array} { r } { \overline { { u _ { \iota } } } = \overline { { U } } + \frac { \theta f ( q _ { i } ) } { 1 - \zeta } } \end{array}$ (by equaling the profit when serving a low-cost and a high-cost buyer). It is obvious that there exists seller ?? ∉ ?? matched with a low-cost buyer, and seller ?? can beat seller ?? in the competition for the high-cost buyer by offering $\overline { { U } } + \epsilon ( > \overline { { U } } )$ , where $\epsilon > 0$ is an infinitesimal. Therefore, seller $k ^ { * } s$ highest offered utility to that low-cost buyer is $\begin{array} { r } { \overline { { u _ { k } } } = \overline { { U } } + \epsilon + \frac { \theta f ( q _ { k } ) } { 1 - \zeta } } \end{array}$ (by equaling the profit when serving a low-cost and a high-cost buyer). We have $\bar { u _ { \iota } } > \bar { u _ { k } }$ because $f ( q _ { i } ) > f ( q _ { k } )$ ; that is, seller ?? has the incentive to deviate and attract the low-cost buyer. Again, we have a contradiction.

Let ?? denote the set of sellers whose matching abilities $Q _ { h } ( j )$ rank from 1 to $N _ { h }$ among sellers ?? ∉ ??.

(1) Suppose seller $j \in J$ is unmatched. Then, she can always increase the offered utility to get matched with a high-cost buyer because her matching ability is among the $N _ { h }$ highest ones. (2) Suppose seller $j \in J$ is matched with a low-cost buyer. Then, there must be a seller ?? ∈ ?? who is not matched with a low-cost buyer, a situation for which the previous analysis has shown the contradiction. □

Lemma D2 reveals that beyond the explicit feature “quality,” the matching outcome is determined by the implicit feature “matching ability” $Q _ { m } ( \cdot )$ and $Q _ { h } ( \cdot )$ in the two-sided market with coproduction serving cost.

Recall that high-quality sellers can cherry-pick low-cost buyers and get matched under BRS but partially withdraw under URS in the intermediate rank case. In this situation, the shuffle effect arises. When these sellers who withdraw are of high enough quality, the shuffl effect is sufficiently strong to improve the commission income, indicating that BRS can benefit the platform.

Let us use an example with $f ( q _ { i } ) = q _ { i } ^ { 2 }$ to illustrate this result. Note that the matching ability $\begin{array} { r } { Q _ { m } ( i ) = q _ { i } - \frac { ( 1 - \rho ) \theta } { 1 - \zeta } q _ { i } ^ { 2 } } \end{array}$ first decreases and then increases in $q _ { i } ;$ as a result, sellers with the top $N - y$ highest quality and the bottom ?? lowest quality possess the ?? highest matching abilities $Q _ { m } ( \cdot )$ under URS in an intermediate rank case, where $y \in [ 0 , N ]$ is an integer. Recalling Lemma B1, we can establish a mapping between sellers with $Q _ { m } [ 1 ] , \dots , Q _ { m } [ N ]$ and sellers with quality ranks $i \in \{ 1 , 2 , \ldots , N _ { l } - 1 \} \cup \{ M - N _ { h } , \ldots , M \}$ (i.e., let $y = N _ { l } - 1 )$ ), while $Q _ { m } [ N + 1 ]$ and $i = M - N _ { h } - 1$ . This configuration clearly represents an intermediate rank case.

Modifying Equation (C4), the platform obtains profit

$$
\pi_ {U} = \zeta \left[ \sum_ {i = 1} ^ {N _ {l} - 1} q _ {i} + \sum_ {i = M - N _ {h}} ^ {M} q _ {i} - N Q _ {m} (M - N _ {h} - 1) \right].
$$

Then, as discussed in Lemma B2, suppose that sellers $i \in \{ 1 , \ldots , N _ { l } \}$ get matched with $N _ { l }$ low-cost buyers, and $i \in \{ M - N _ { h } + 1 , \ldots , M \}$ } get matched with $N _ { h }$ high-cost buyers. By Equation (B1), we have

$$
\pi_ {B} = \zeta \sum_ {i = 1} ^ {N _ {l}} \left(q _ {i} - q _ {N _ {l} + 1}\right) + \zeta \sum_ {i = M - N _ {h} + 1} ^ {M} \left[ q _ {i} - Q _ {h} (M - N _ {h}) \right],
$$

$$
\frac {\pi_ {B} - \pi_ {U}}{\zeta} = q _ {N _ {l}} - q _ {M - N _ {h}} + N Q _ {m} (M - N _ {h} - 1) - N _ {l} q _ {N _ {l} + 1} - N _ {h} Q _ {h} (M - N _ {h}).
$$

Hence, BRS benefits the platform when $q _ { N _ { l } } > A _ { 4 } ^ { D }$ , where

$$
A _ {4} ^ {D} = q _ {M - N _ {h}} - N Q _ {m} (M - N _ {h} - 1) + N _ {l} q _ {N _ {l} + 1} + N _ {h} Q _ {h} (M - N _ {h}).
$$

This example demonstrates that BRS can indeed benefit the platform in the intermediate rank case.
