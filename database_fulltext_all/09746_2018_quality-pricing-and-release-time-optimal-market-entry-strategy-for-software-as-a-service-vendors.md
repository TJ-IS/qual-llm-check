---
otero_id: 9746
otero_key: "TRJXGV8F"
title: "Quality, Pricing, and Release Time: Optimal Market Entry Strategy for Software-as-a-Service Vendors1"
authors: "Haiyang Feng; Zhengrui Jiang; Dengpan Liu"
year: "2018"
journal: "MIS Quarterly"
doi: "10.25300/misq/2018/14057"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# QUALITY, PRICING, AND RELEASE TIME: OPTIMAL MARKET ENTRY STRATEGY FOR SOFTWARE-AS-A-SERVICE VENDORS<sup>1</sup>

Haiyang Feng College of Management and Economics, Tianjin University, Tianjin 300072, CHINA {hyfeng@tju.edu.cn}

Zhengrui Jiang College of Business, Iowa State University, Ames, Iowa 50011-2027 U.S.A. {zjiang@iastate.edu}

Dengpan Liu School of Economics and Management, Tsinghua University, Beijing, CHINA 100084 {liudp@sem.tsinghua.edu.cn}

As a new software licensing model, software-as-a-service (SaaS) is gaining tremendous popularity across the globe. In this study, we investigate the competition between a new entrant and an incumbent in an SaaS market, and derive the optimal market entry strategy for the new entrant. One interesting finding is that, when its product quality is significantly lower than that of the incumbent, the new entrant should adopt an instantrelease strategy (i.e., releasing its product at the start of the planning horizon). If the initial quality gap of the two products is small, the new entrant is better off adopting a late-release strategy (i.e., deferring the release of the new product until its quality surpasses that of the existing product). We also find that instant-release and late-release are essentially low-quality/low-price and high-quality/high-price strategies, respectively. In addition, we explore the scenario where the two competing products are partially compatible, and characterize the impact of asymmetric incompatibility on the two vendors’ market strategies at equilibrium. We find that the new entrant’s zero-profit region expands as the level of incompatibility between the two competing products increases. Moreover, if the new entrant adopts the instant-release strategy, its profit decreases with the level of incompatibility. When the level of incompatibility is sufficiently high, the instant-release strategy may not be viable for the new entrant. On the other hand, if the new entrant adopts the late-release strategy, its profit increases with the level of incompatibility from its product to the incumbent’s, but decreases with the level of incompatibility in the other direction.

Keywords: Game theory, duopoly, market entry strategy, Software-as-a-Service, network effects, asymmetric compatibility, switching cost

## Introduction

Over the past decade, Software-as-a-Service (SaaS), a cloudbased alternative to the traditional on-premises software delivery model, has gained tremendous popularity across the globe (Columbus 2012). The increasing popularity of SaaS is mainly attributed to its lower cost of ownership and ease of deployment, as compared to its traditional on-premises counterpart. The industry has seen a clear trend toward adopting SaaS products (Hamerman 2014). Gartner forecasted that the global SaaS market would continue to grow and reach \$55.1 billion in 2018, up from \$46.3 billion in 2017 (Pettey and Goasduff 2017). Given the tremendous growth of SaaS adoption, Cisco projected that by 2018, 59% of total cloud workloads will be used to support SaaS applications, an increase from 41% in 2013 (Cisco 2014). Although the projected growth rates may vary, the consensus is that the shift to SaaS and the expeditious growth of SaaS revenue will likely continue into the foreseeable future.

Meanwhile, the profit margin of the SaaS software sector lags far behind its revenue growth. As the SaaS market expands, market competition also intensifies, and as a result, the SaaS software sector is not doing well financially. According to a Software Industry Financial Report (Software Equity Group 2015), 59% of the publicly traded SaaS vendors were unprofitable in 2014, and around 90% of them had a margin below their on-premises peers. Despite the dismal profit margin of the sector, the top performers, mostly market leaders in their respective software categories (e.g., NetSuite in ERP, and Tableau in business intelligence) have delivered admirable returns. It is mostly vendors in the middle or lower ends of the market spectrum that are struggling to gain market share and increase revenue (Software Equity Group 2015).

After the rapid expansion in recent years, most of the major SaaS categories are already occupied or dominated by incumbent vendors. Vendors seeking to profit from the growing SaaS market but having missed the opportunity to enter their market segment as a leader are now facing challenging market conditions. For instance, CRM SaaS vendors were coming under increasing downward pricing pressure when a new vendor entered the market (Beal 2008). More recently, it was reported that SaaS prices had been kept artificially low due to intensified competition (Kwang 2012). Another report by the Software Equity Group (2015) showed that the median profit margin of public SaaS companies had declined substantially in recent years, from a peak of 9.6% in 2010 to -9.8% in 2014. In contrast, the median profit margin of on-premises software vendors was 17% in 2014.

For incumbent SaaS vendors, the intensifying market competition, downward pricing pressure, and decreasing profit margin unavoidably affect their bottom line; for new market entrants, such unfavorable market conditions significantly reduce their chance of survival. Therefore, it is critical for new entrants to make informed decisions on market positioning at the time of entry. Thus, our primary goal in the present research is to derive an optimal market entry strategy for new vendors who seek to enter a SaaS market already occupied by incumbents.

Since consumers are primarily concerned with their net utility derived from consuming the product, of critical importance is the pricing and product quality decisions of the new entrants. In fact, quality and price are considered the two most important decision variables that new entrants can leverage so as to gain a foothold in a competitive market. For instance, in the advanced analytics SaaS market where SAS and IBM dominate, startups such as Alpine Data Labs (alpinenow.com) and Revolution Analytics (revolutionanalytics.com) were able to use a low pricing strategy to grab some market share from their big incumbent competitors (Henschen 2011). Similarly, in the CRM SaaS market, Highrise (highrisehq.com) focused on offering low-cost and simple solutions to cost-sensitive customers (Tatum 2013). On the other hand, there are vendors who choose to adopt a premium pricing strategy, under which they invest heavily to deliver the best software package, and then charge a premium price. SuccessFactors (successfactors.com), now part of SAP, adopts such a strategy with a superior product quality in the human capital management SaaS market (Cochrane et al. 2014). Thus, one of the research questions we plan to address in this study is under what conditions the low-quality/low-price strategy is preferable to the high-quality/high-price strategy and vice versa.

A higher product quality typically demands more development time, which may cause delay to the release of the product. Hence, the desirable product quality is a key factor that affects a vendor’s decision on market entry timing. Although the product quality and time-to-market tradeoff has been well studied in the general new product development and marketing literature (e.g., Bayus 1997; Cohen et al. 1996; Rodríguez-Pinto et al. 2011), no extant work has studied such a tradeoff for SaaS products, which have their own distinctive characteristics such as subscription pricing. In this research, we not only explicitly model the quality and release time tradeoff, but also investigate how the new entrant’s decision on product quality and market entry timing affects the pricing, market share, and profitability of the vendors engaged in competition.

Furthermore, given that software products are typically subject to strong network effects (Brynjolfsson and Kemerer 1996; Gallaugher and Wang 2002), we attempt to examine how the within- and cross-product network effects affect market competition and hence the market entry strategy for new entrants. Finally, since the prior literature on information goods have shown that switching cost and lock-in effects can affect vendors’ quality or pricing strategies (e.g., Chen and Wu 2012; Fuentelsaz et al. 2012; Zhu and Zhou 2012), we also analyze the impact of switching cost on the new entrant’s market entry timing and pricing decisions.

The market scenario we analyze in this study is described as follows. Attracted by the rapidly expanding market, a new vendor seeks to enter a segment of the SaaS market, where one incumbent vendor is providing a SaaS product considered to be a substitute to the new entrant’s product. At the start of the time horizon, the product quality of the new entrant is lower than that of the incumbent. By deferring the release of its product, the new entrant can further improve the product quality. The incumbent is ready to adjust its product price in response to the market entry of the new entrant. In the meantime, consumers stand to adapt as the market structure changes from monopoly to duopoly, and will choose the SaaS product that maximizes their utility. Using a game-theoretic modeling framework, we develop a duopoly model of competition between the incumbent vendor and the new entrant, and derive the optimal pricing, quality, and market entry timing for the new entrant. By examining the derived optimal market entry strategy, we also hope to better understand how the various market factors, such as network effects and switching cost, play a role in affecting the new vendor’s entry strategy and market outcomes.

Some interesting findings emerge from our analysis. First, we find that if the initial quality gap between the competing products is sufficiently large, it is optimal for the new entrant to adopt a low-quality/low-price strategy and release its product immediately (i.e., instant-release strategy); otherwise, the new entrant is better off adopting a high-quality/high-price strategy, which allows the new entrant to defer releasing the product until its quality surpasses that of the incumbent product (i.e., late-release strategy). Second, when the competing products are partially compatible, the zero-profit region for the new entrant, in which the new entrant would lose the entire market, expands with the level of incompatibility. Third, a higher level of incompatibility (in either direction) will reduce the new entrant’s profit derived from the instantrelease strategy. Thus, at a sufficiently high level of incompatibility, the instant-release strategy may turn out not to be viable for the new entrant. On the other hand, when the new entrant adopts the late-release strategy, a higher level of incompatibility from its product to the incumbent’s, which essentially makes it more difficult for the consumers of the incumbent to leverage the cross-product network effects from the new entrant, increases its profit, whereas a higher level of incompatibility in the other direction may reduce its profit.

Fourth, we show that switching cost, if considered, can help the incumbent gain market power over the new entrant by taking advantage of the installed base established in the monopoly stage. In addition, with a higher switching cost, the new entrant is more likely to adopt the instant-release strategy. Finally, we show that our main findings on the new entrant’s optimal market entry strategy are robust even when some of the key assumptions in our models are relaxed.

Our research makes substantial novel theoretical contributions to the literature on vertical differentiation. This work is the first attempt to capture the novel three-way tradeoff among service duration, development cost, and product quality, a unique tradeoff faced by SaaS vendors, which has not been addressed in conventional vertical differentiation models (e.g., Blattberg and Wisniewski 1989; Boccard and Wauthy 2010; Wauthy 1996). Second, our model is the only one that studies vertical differentiated products with subscription-based pricing, while all the prior vertical differentiation models (e.g., Bergemann and Välimäki 2002; Hung and Schmitt 1988; Lutz 1997; Liu and Zhang 2013) analyze purchase-toown products (i.e., customers pay a one-time price to acquire the ownership of a product and can use it throughout its life span). Third, our model is the only one that uses a continuous time decision variable to capture the release of the products facing vertical competition, while the other models either do not consider a continuous time dimension (e.g., Noh and Moschini 2006) or do not consider release time as a decision variable (e.g., Bergemann and Välimäki 2002). This unique feature in our model setup allows us to identify the optimal timing of product release from a continuous time interval for the new entrant, taking into account the aforementioned threeway tradeoff. Fourth, our model is the only one that incorporates all three factors important to SaaS products (i.e., network effects, product compatibility, and switching cost), and characterizes their effects on the market entry strategy of SaaS vendors. Finally, we show that when the competing SaaS products are partially compatible, the new entrant can choose from among three possible release strategies: instant-release, Type I late-release, and Type II late-release. To the best of our knowledge, such a finding has not been reported in any conventional vertical competition model.

The rest of the paper is organized as follows. The next section discusses the related literature. Using a two-stage model that includes a monopoly stage and a duopoly stage, we first analyze the scenario where the products offered by the incumbent and the new entrant are fully compatible, and then examine the more general scenario where the two competing products are partially compatible. Subsequently, in the model extensions we take into account factors such as consumers switching cost, and analyze how such factors would affect the new entrant’s market entry strategies. We conclude the paper with discussions on research contributions, practical implications, and limitations that could be addressed in future studies.

## Related Literature

The present research is related to several streams of literature. The first stream is on network effects, which arise when the utility a consumer derives from a good increases with the total number of consumers of that good (Katz and Shapiro 1985). Researchers have found empirical evidence of network effects in many software products, including spreadsheets (Brynjolfsson and Kemerer 1996), web servers (Gallaugher and Wang 2002), and video games (Shankar and Bayus 2003). Similarly, network effects have been analyzed for subscriptionbased information technology services (Niculescu et al. 2012).

Another stream of related literature is on the tradeoffs between product quality and time-to-market. Earlier analytical and empirical studies in this research stream have focused on monopolist markets (e.g., Bayus 1997; Kalish and Lilien 1986). More recently, there are studies that focus on the decisions under duopoly settings (e.g., Kopel and Löffler 2008; Savin and Terwiesch 2005). These prior studies differ from the present research in that they focus on general product categories such as computers, copiers, and cars, without considering the characteristics of software products (e.g., low margin cost of production and network effects), let alone other distinctive features of SaaS products (e.g., subscription pricing).

The present research is more closely related to the prior literature on SaaS or similar products such as application service providers (ASPs). The earlier studies focus on deriving the pricing and licensing strategies for monopolistic SaaS or ASP vendors (e.g., Cheng and Koehler 2003; Choudhary et al. 1998; Gurnani and Karlapalem 2001). These studies show that non-perpetual software offering provides vendors with more flexibility in product offerings that can help improve their profitability.

Some of the prior research on SaaS compares the SaaS licensing model and the perpetual licensing model for monopolistic vendors. Choudhary (2007) finds that the difference in dissemination of new features between SaaS and perpetual licensing affects a monopolistic vendor’s decision to invest in product quality. Specifically, under the SaaS model, the vendor tends to invest more, leading to better quality and higher profit compared to the perpetual licensing model. In another study, Zhang and Seidmann (2010) examine the different licensing options available to a monopolistic vendor, and show that under strong network effects, the hybrid licensing model, under which both SaaS and perpetual licensing are made available to consumers, is the most profitable option.

In addition, some prior research on SaaS analyzes the competition between SaaS and perpetual software vendors. Fan et al. (2009) consider a SaaS product a bundle of software and service. Their analyses show that compared with shrink-wrap software, the service component of a SaaS product leads to lower implementation cost for users, higher operation cost for vendors, and the equilibrium market price is higher. However, the higher operation cost may affect the SaaS vendor’s ability to invest in product quality in the long run. In a more recent study, Ma and Seidmann (2015) examine the competition between a traditional off-the-shelf software vendor and a SaaS vendor that charges consumers per-transaction fees. The study shows that the lack-of-fit cost of the SaaS product is a key factor in determining which product(s) will end up occupying the market. Based on the analytical results, the authors also offer some pricing and quality recommendations to vendors of both types of software.

A key difference between the present study and the aforementioned streams of research on SaaS is that we analyze a duopoly market with two SaaS vendors competing for market share and profit, whereas the focus of the prior research streams was on either monopolistic vendors or the competition between a SaaS vendor and a perpetual software vendor.

Prior research with a focus on the direct competition between SaaS vendors is rare. Fishburn and Odlyzko (1999) investigate the existence of competitive equilibria when one vendor adopts a policy of fixed subscription fee per period and the other charges on a per-use basis, and find that in the absence of collusion, competition will lead to ruinous price wars. To the best of our knowledge, the closest study to ours is Ma and Kauffman (2014), which analyzes the pricing and quality strategies for two competing SaaS vendors. One of its main findings is that clients’ switching costs play a critical role in determining the outcome of the competition. For instance, an increase in switching cost can significantly worsen the position of the less competitive vendor, while the more competitive vendor can charge a higher price and achieve a significantly higher profit. Although the present research and Ma and Kauffman both study market competition between two SaaS vendors, there are significant differences in terms of research focus, model assumptions, and findings. For instance, we focus on deriving the market entry strategy for a new entrant, whereas the previous study does not differentiate between an incumbent and a new entrant. Moreover, we consider the tradeoff between quality, development costs, and market entry timing, whereas Ma and Kauffman assume that the competing products are both available at time zero, and development costs are considered sunk costs. In addition, we explicitly model the impact of product compatibility and the network effects on the two vendors’ market decisions, while compatibility and network effects are not considered by the prior study. Furthermore, consumers’ willing-to-pay is continuously distributed in our model, which is different from Ma and Kauffman’s discrete valuation assumption.

## A Two-Stage Model

Consider two SaaS vendors, Vendors A and B, providing vertically differentiated products, products A and B, respectively. Without loss of generality, let Vendor A be the incumbent and Vendor B the new entrant. Following a common practice in the SaaS market, both vendors adopt subscription-based pricing (i.e., consumers are charged a fixed subscription fee per unit time; Fishburn and Odlyzko 1999). As shown in Figure 1, at time 0, the earliest time at which product B passes the minimum feature and quality threshold and can be released, Vendor A has already released its product at time $\tau _ { A }$ $( \tau _ { A } < 0 )$ Here it is worth noting that Vendor $\mathbf { A } ,$ when releasing its product, has made its pricing (for the monopoly stage) and product quality decisions. We assume that such decisions, once being made, remain unchanged throughout the monopoly stage. This is because once it has released its product and developed a large customer base, the incumbent becomes far less flexible than a challenger that has yet to enter the market, and cannot change its plans rapidly and frequently due to possible technology inertia and structural inertia (Colombo and Delmastro 2002; Ghemawat 1991; Hannan and Freeman 1984).

Since the main purpose of the present study is to explore the optimal market entry strategy for the new vendor, we focus on the finite demand window [0, D] in subsequent analysis. We assume that at time 0, Vendor B decides on its timing of market entry, denoted by $\tau _ { B } , ~ \tau _ { B } ~ \geq ~ 0$ At $\tau _ { B } ,$ product B is released and the two vendors start to compete by choosing their subscription prices $p _ { A } ^ { D }$ and $p _ { B } ^ { D } ,$ respectively, where the superscript “D” stands for duopoly.

We also assume that the development cost that Vendor B has incurred prior to time 0 is sunk. Thus, Vendor B makes its decisions based on the net profit derived in the finite demand window [0, D] (Cohen et al. 1996). The quality of product B at time 0, denoted by $q _ { B 0 } ,$ however, is lower than that of product A at time 0, denoted by $q _ { _ { A 0 } } ( \mathrm { i } . \mathbf { e } . , q _ { B 0 } < q _ { A 0 } )$ . Hence the initial quality gap of the two products is $\Delta q _ { 0 } = q _ { A 0 } - q _ { B 0 } .$ Vendor B can also choose a release time $\tau _ { B } > 0$ to continue developing its product after time 0. Following previous studies (e.g., Cohen et al. 1996), we assume that the quality of product B at time $\tau _ { B } , q _ { B } ( \tau _ { B } )$ , increases linearly with $\tau _ { B } ,$ that is,

$$
q _ {B} (\tau_ {B}) = q _ {B 0} + \lambda_ {1} \tau_ {B}\tag{1}
$$

where $\lambda _ { 1 } > 0$ is the rate of quality improvement for product B in the product development stage.

It is worth noting that in practice, SaaS vendors can continue to improve the quality of their products even after release. In fact, continuous quality improvement is considered a key advantage of SaaS in comparison with perpetual licensing (e.g., Choudhary 2007). However, to ensure that the end users’ experience is maximized, SaaS vendors usually do not release a product until its core features are completed and its quality reaches a certain threshold. After release, the focus of quality improvement typically shifts to product maintenance and incremental feature improvements. Thus, it is reasonable to believe that the rate of quality improvement after release is approximately the same for both vendors.<sup>2</sup> Therefore, after the release of product B, the qualities of the two products take the following forms:

$$
\left\{ \begin{array}{l l} q _ {A} (\tau) = q _ {A 0} + \lambda_ {2} \tau , & \tau \in [ 0, D ] \\ q _ {B} (\tau) = q _ {B 0} + \lambda_ {1} \tau_ {B} + \lambda_ {2} (\tau - \tau_ {B}), & \tau \in [ \tau_ {B}, D ] \end{array} \right.\tag{2}
$$

where $\lambda _ { 2 } \left( \lambda _ { 2 } > 0 \right)$ is the rate of quality improvement for the two vendors after release, and it is assumed to be lower than $\lambda _ { 1 } .$ <sup>3</sup> Following prior studies (e.g., Calantone and Di Benedetto 2000), we assume that the development cost for product B and the maintenance cost are both linear functions of time. We denote Vendor B’s development cost (per unit time) before release by $k _ { \mathrm { 1 : } }$ , and the cost per unit time incurred for product maintenance and incremental feature improvements after release by $k _ { 2 } .$ It is reasonable to assume that development cost is higher than maintenance cost $( \mathrm { i } . \mathrm { e } . , k _ { 1 } > k _ { 2 } )$ Given the fixed demand window, delaying the release by one unit time increases the development cost by $k _ { 1 }$ and decreases the maintenance cost by $k _ { 2 } .$ , hence we term the difference of two costs the marginal development cost (per unit time), which is denoted by k ${ \bf \nabla } ( k = k _ { 1 } - k _ { 2 } )$ . Thus, the sum of the development cost and maintenance cost is

$$
k _ {1} \tau_ {B} + k _ {2} (D - \tau_ {B}) = (k + k _ {2}) \tau_ {B} + k _ {2} (D - \tau_ {B}) = k \tau_ {B} + k _ {2} D
$$

![](/api/attachments/TRJXGV8F/fulltext/images/ebf0b227e569f697e57e945c9573805db921194ca6ec6bc6db44863ee0a96811.jpg)

Figure 1. Two Stages of the Demand Window  
![](/api/attachments/TRJXGV8F/fulltext/images/f29c13a229b168d438d5650e6d5e14c7f2b7e473dd6903df56aab3ca0871efeb.jpg)  
(a) Product B Is Released before $\tau _ { E }$  
Figure 2. Product Quality as a Function of Time

In the above equation, since $k _ { 2 } D$ is a constant and hence does not affect the release strategy, we only retain the total marginal development cost in the rest of the analysis:<sup>4</sup>

$$
c = k \tau_ {B}\tag{3}
$$

Figure 2 illustrates the product quality of each product as a function of time τ. The time instance when product B catches up with product A in quality is $\tau _ { E } = \Delta q _ { 0 } / \lambda$ , where $\lambda = \lambda _ { 1 } - \lambda _ { 2 }$ is the difference between the rates of quality improvement for product B before and after its release.

On the demand side, the net utility that a consumer derives from consuming a SaaS product depends on her valuation of the product and the network effects. We use consumer type θ to capture consumers’ heterogeneity in valuation toward a given SaaS product. Following previous studies (Cheng and Liu 2012; Hoppe and Lehmann-Grube 2001; Pang and Etzion 2012), we assume that θ is uniformly distributed over $[ \theta _ { 0 } , 1 ] .$ and the potential market size is normalized to $( 1 ~ - ~ \theta _ { 0 } )$ accordingly. Here, $\theta _ { 0 }$ represents the type of consumers with the minimum willingness-to-pay, and is assumed to be nonnegative. Furthermore, we do not consider the scenario where both vendors serve only the high-end market $\theta _ { 0 } \geq 0 . 5$ while completely ignoring the low-end market. Thus, we assume $\theta _ { 0 } \in [ 0 , 0 . 5 )$ in our analysis.

![](/api/attachments/TRJXGV8F/fulltext/images/2530d1eee2db02833c24285fd5e96a0182803b8fb66e509749d129a780435bab.jpg)  
(b) Product B Is Released after $\tau _ { E }$

We also consider network effects, which refer to the phenomenon that the value of a product increases with its network size. As is common in the prior literature (e.g., Jing 2007; Zhang and Seidmann 2010), we assume that the benefit resulting from network effects increases linearly with the network size. We denote the installed based or network size of product A in the monopoly stage by $Q _ { A } ^ { M } ,$ and those of products A and B in the duopoly stage by $Q _ { A } ^ { D }$ and $\mathcal { Q } _ { B } ^ { D } ,$ respectively. Then, in the duopoly stage, the net utility (per unit time) that a type $\theta$ consumer gains from consuming product $i , \ i \ \in$ $\{ A , B \}$ , is

$$
\begin{array}{c} U \left(\theta , q _ {i} (\tau)\right) = \theta q _ {i} (\tau) - p _ {i} ^ {D} + \alpha Q _ {i} ^ {D} + \\ \beta_ {j} Q _ {j} ^ {D}, i, j \in \{A, B \}, i \neq j \end{array}\tag{4}
$$

where $\alpha \geq 0$ represents the intensity of network effects, measuring the increase in the consumer’s willingness-to-pay when an additional consumer joins the network, and $\beta _ { j } \in [ 0 ,$ , α] represents the intensity of cross-product network effects that users of product j have on those of product i. Specifically, $\beta _ { j }$ measures the increase in the consumer’s willingness-to-pay for product i when an additional consumer joins the network of product j. We would like to note that the values for $\beta _ { A }$ and $\beta _ { B }$ may not be the same. This is because a vendor with a relatively low market share (e.g., a new entrant) may intentionally make its product compatible with the product having a relatively high market share in order to take advantage of the latter’s larger network. The vendor with the relatively high market share, on the other hand, does not always prefer to make its product compatible with the product having a low market share. Rather, it may try to maintain a high level of incompatibility to avoid the potential erosion of its consumer base. For example, software products such as Apache OpenOffice can often be used to process files created with Microsoft Office, which is in the position of market dominance, but not vice versa.

<table><tr><td colspan="2">Table 1. Summary of Notations</td></tr><tr><td>Notation</td><td>Description</td></tr><tr><td> $D$ </td><td>Demand window</td></tr><tr><td> $\theta$ </td><td>Consumer type, capturing heterogeneous consumer valuation toward a given SaaS product</td></tr><tr><td> $\theta_0$ </td><td>Type of consumers with the minimum willingness-to-pay</td></tr><tr><td> $\tau_B$ </td><td>Product B&#x27;s release time</td></tr><tr><td> $\lambda_1$ </td><td>Rate of product B&#x27;s quality improvement before release</td></tr><tr><td> $\lambda_2$ </td><td>Rate of quality improvement for products A and B after release</td></tr><tr><td> $\lambda$ </td><td>Difference between the rates of quality improvement before and after release</td></tr><tr><td> $k$ </td><td>Vendor B&#x27;s marginal development cost (per unit time),  $k = k_1 - k_2$ </td></tr><tr><td> $q_A(\tau), q_B(\tau)$ </td><td>Quality of product A and product B at time  $\tau$ , respectively</td></tr><tr><td> $q_{A0}, q_{B0}$ </td><td>Initial quality (at time 0) of product A and product B, respectively,  $q_{B0} < q_{A0}$ </td></tr><tr><td> $\Delta q_0$ </td><td>Initial quality gap (at time 0), i.e.,  $\Delta q_0 = q_{A0} - q_{B0}$ </td></tr><tr><td> $p_A^D, p_B^D$ </td><td>Subscription prices of the two products in the duopoly stage</td></tr><tr><td> $Q_A^M$ </td><td>Network size of product A in the monopoly stage</td></tr><tr><td> $Q_A^D, Q_B^D$ </td><td>Network sizes of the two products in the duopoly stage</td></tr><tr><td> $\pi_A^D, \pi_B^D$ </td><td>Profit rates of the two products in the duopoly stage</td></tr><tr><td> $\Pi_A, \Pi_B$ </td><td>Total profits of the two products in the demand window, [0, D]</td></tr><tr><td> $\alpha$ </td><td>Intensity of (within-product) network effects</td></tr><tr><td> $\beta_j$ </td><td>Intensity of cross-product network effects (from product j to product i)</td></tr><tr><td> $\gamma_j$ </td><td>Level of incompatibility (from product j to product i),  $\gamma_j = \alpha - \beta_j$ </td></tr><tr><td> $c_S$ </td><td>Consumers&#x27; switching cost</td></tr><tr><td> $\tau_E$ </td><td>Time instance when the new entrant catches up with the incumbent in quality</td></tr></table>

For notational convenience, we denote the level of incompatibility from product j to product i, which essentially captures the level of difficulty for the users of product i to leverage the cross-product network effects arising from product j, by $\gamma _ { j } , \gamma _ { j }$ $\mathbf { \alpha } = \alpha - \beta _ { i }$ Thus, the level of incompatibility between the two substitutable products is determined by the values of the parameters $\beta _ { j } , j \in \{ A , B \}$ . If $\beta _ { { \scriptscriptstyle A } } = \beta _ { { \scriptscriptstyle B } } = \alpha ( \beta _ { { \scriptscriptstyle A } } = \beta _ { { \scriptscriptstyle B } } = 0 )$ , then $\gamma _ { A }$ $\mathit { \Psi } = \mathit { \Psi } \gamma _ { B } = 0 \ \left( \widehat { \gamma } _ { A } = \gamma _ { B } = \alpha \right)$ and the two products are fully compatible (fully incompatible); $\operatorname { i f } 0 < \{ \beta _ { A } , \beta _ { B } \} < \alpha .$ , then $0 <$ $\{ \gamma _ { A } , \gamma _ { B } \} <$ α and the two products are partially compatible (or partially incompatible). In the following three sections, we first derive the optimal price, and then separately examine the full-compatibility and the partial-compatibility scenarios. The key notations used in our models are summarized in Table 1.

We employ a game-theoretic framework to derive the optimal pricing and quality decisions for the two vendors. The order of play for the two vendors and their consumers is as follows:

(1) Vendor B, the new entrant, chooses its time of entry.

(2) Given Vendor B’s time of entry, Vendors A and B choose their respective subscription prices for the duopoly stage.

(3) In response to the vendors’ decisions, consumers subscribe to the product that would maximize their net utility.

As is customary in backward induction, we first obtain the two vendors’ optimal subscription prices, and then solve the optimal product release time for the new entrant.

the

## Optimal Price and Profit Rate

We first assume that Vendor B’s market entry timing is given, and its development cost is sunk. In such a case, maximizing each vendor’s total profit in the duopoly stage is equivalent to maximizing its profit rate (i.e., profit per unit time). We examine the two cases— $- q _ { A } ( \tau _ { B } ) < q _ { B } ( \tau _ { B } )$ (as shown in Figure $2 ( \mathrm { a } ) )$ and $q _ { A } ( \tau _ { B } ) > q _ { B } ( \tau _ { B } )$ (as shown in Figure 2(b)), separately. Since the equilibrium solutions in the two cases are symmetric with respect to the quality of the two products, to avoid repetition, we denote the product with higher quality upon the release of product B by H and the other one by L. That is, if $q _ { A } ( \tau _ { B } ) > q _ { B } ( \tau _ { B } )$ H=A, L=B; otherwise, H=B, L=A. The notations for price, demand, and profit rate are revised accordingly.

For analytical tractability, following previous studies (Dutta et al. 1995; Hoppe and Lehmann-Grube 2001), we assume that the value of $\cdot \theta _ { 0 } ,$ , which denotes the type of consumers with the minimum willingness-to-pay, is set in such a way that all consumers would purchase either product A or B in the duopoly stage.<sup>5</sup> Let denote the type of consumer who is <sup>D</sup> $\hat { \theta } ^ { D }$ indifferent between products H and L. From Equation (4), we have

$$
\begin{array}{l} \hat {\theta} ^ {D} q _ {H} (\tau_ {B}) - p _ {H} ^ {D} + \alpha Q _ {H} ^ {D} + \beta_ {L} Q _ {L} ^ {D} = \\ \hat {\theta} ^ {D} q _ {L} (\tau_ {B}) - p _ {L} ^ {D} + \alpha Q _ {L} ^ {D} + \beta_ {H} Q _ {H} ^ {D} \end{array}\tag{5}
$$

where $Q _ { H } ^ { D } = 1 - \hat { \theta } ^ { D }$ and $\mathcal { Q } _ { L } ^ { D } = \hat { \theta } ^ { D } - \theta _ { 0 }$ are the network sizes of products H and L, respectively. From Equation (5), we obtain

$$
\hat {\boldsymbol {\theta}} ^ {D} = \frac {p _ {H} ^ {D} - p _ {L} ^ {D} - \theta_ {0} \gamma_ {L} - \gamma_ {H}}{q _ {H} (\tau_ {B}) - q _ {L} (\tau_ {B}) - \gamma_ {H} - \gamma_ {L}}\tag{6}
$$

As explained earlier, $\gamma _ { j } = \alpha - \beta _ { j }$ represents the level of incompatibility from product j to product i, which essentially captures the level of difficulty for the users of product i to leverage the cross-product network effects arising from product $j , i , j \in \{ H , L \} , i \neq j .$ That is, with a higher γ<sub>j</sub>, users of product i derive a lower utility from the network of product j.

We adopt the common assumption that the marginal cost of serving an additional customer of information goods is zero. Then, maximizing the profit rate of each vendor is equivalent to maximizing the product of its subscription price and market share

$$
\begin{array}{l} \left\{ \begin{array}{l} \max _ {p _ {L} ^ {D}} \pi_ {L} = p _ {L} ^ {D} \left(\hat {\theta} ^ {D} - \theta_ {0}\right) \\ \max _ {p _ {H} ^ {D}} \pi_ {H} = p _ {H} ^ {D} \left(1 - \hat {\theta} ^ {D}\right) \end{array} \right. \\ \text {s.t.} \theta_ {0} \leq \hat {\theta} ^ {D} \leq 1 \\ p _ {L} ^ {D} \geq 0, p _ {H} ^ {D} \geq 0 \end{array}\tag{7}
$$

At the fulfilled expectation equilibrium (Katz and Shapiro 1985), the equilibrium prices, demand, and profit rates for the two vendors take the following forms:

a. $\mathrm { I f } \left( q _ { H } \big ( \tau _ { B } \big ) - q _ { L } \big ( \tau _ { B } \big ) \right) \geq \frac { 1 - \theta _ { 0 } } { 1 - 2 \theta _ { 0 } } \big ( \gamma _ { L } + 2 \gamma _ { H } \big ) .$ the equili- <sup>,</sup>

brium prices, demand, and profit rates for the two vendors are given by

$$
\left\{ \begin{array}{l} p _ {H} ^ {D *} = \frac {(2 - \theta_ {0}) (q _ {H} (\tau_ {B}) - q _ {L} (\tau_ {B})) - (1 - \theta_ {0}) (2 \gamma_ {L} + \gamma_ {H})}{3} \\ p _ {L} ^ {D *} = \frac {(1 - 2 \theta_ {0}) (q _ {H} (\tau_ {B}) - q _ {L} (\tau_ {B})) - (1 - \theta_ {0}) (\gamma_ {L} + 2 \gamma_ {H})}{3} \end{array} \right.\tag{8.1}
$$

$$
\left\{ \begin{array}{l} \hat {\theta} ^ {D *} = \frac {1}{3} \frac {\left(1 + \theta_ {0}\right) \left(q _ {H} \left(\tau_ {B}\right) - q _ {L} \left(\tau_ {B}\right)\right) - \left(1 + 2 \theta_ {0}\right) \gamma_ {L} - \left(\theta_ {0} + 2\right) \gamma_ {H}}{q _ {H} \left(\tau_ {B}\right) - q _ {L} \left(\tau_ {B}\right) - \gamma_ {L} - \gamma_ {H}} \\ Q _ {H} ^ {D *} = \frac {1}{3} \frac {\left(2 - \theta_ {0}\right) \left(q _ {H} \left(\tau_ {B}\right) - q _ {L} \left(\tau_ {B}\right)\right) - \left(1 - \theta_ {0}\right) \left(2 \gamma_ {L} + \gamma_ {H}\right)}{q _ {H} \left(\tau_ {B}\right) - q _ {L} \left(\tau_ {B}\right) - \gamma_ {L} - \gamma_ {H}} \\ Q _ {L} ^ {D *} = \frac {1}{3} \frac {\left(1 - 2 \theta_ {0}\right) \left(q _ {H} \left(\tau_ {B}\right) - q _ {L} \left(\tau_ {B}\right)\right) - \left(1 - \theta_ {0}\right) \left(\gamma_ {L} + 2 \gamma_ {H}\right)}{q _ {H} \left(\tau_ {B}\right) - q _ {L} \left(\tau_ {B}\right) - \gamma_ {L} - \gamma_ {H}} \end{array} \right. (8. 2)
$$

$$
\left\{ \begin{array}{l} \pi_ {H} ^ {D *} = \frac {1}{9} \frac {\left[ (2 - \theta_ {0}) \left(q _ {H} (\tau_ {B}) - q _ {L} (\tau_ {B})\right) - (1 - \theta_ {0}) (2 \gamma_ {L} + \gamma_ {H}) \right] ^ {2}}{q _ {H} (\tau_ {B}) - q _ {L} (\tau_ {B}) - \gamma_ {L} - \gamma_ {H}} \\ \pi_ {L} ^ {D *} = \frac {1}{9} \frac {\left[ (1 - 2 \theta_ {0}) \left(q _ {H} (\tau_ {B}) - q _ {L} (\tau_ {B})\right) - (1 - \theta_ {0}) (\gamma_ {L} + 2 \gamma_ {H}) \right] ^ {2}}{q _ {H} (\tau_ {B}) - q _ {L} (\tau_ {B}) - \gamma_ {L} - \gamma_ {H}} \end{array} \right.\tag{8.3}
$$

$$
0 <   \left(q _ {H} \left(\tau_ {B}\right) - q _ {L} \left(\tau_ {B}\right)\right) <   \frac {1 - \theta_ {0}}{1 - 2 \theta_ {0}} \left(\gamma_ {L} + 2 \gamma_ {H}\right),
$$

equilibrium prices, demand, and profit rates for the two vendors take the following forms:

$$
\left\{ \begin{array}{l} p _ {H} ^ {D *} = \theta_ {0} \left(q _ {H} \left(\tau_ {B}\right) - q _ {L} \left(\tau_ {B}\right)\right) + \gamma_ {H} \left(1 - \theta_ {0}\right) \\ p _ {L} ^ {D *} = 0 \end{array} \right.\tag{9.1}
$$

$$
\left\{ \begin{array}{l} \hat {\boldsymbol {\theta}} ^ {D *} = \boldsymbol {\theta} _ {0} \\ Q _ {H} ^ {D *} = 1 - \boldsymbol {\theta} _ {0} \\ Q _ {L} ^ {D *} = 0 \end{array} \right.
$$

(9.2)

$$
\left\{ \begin{array}{l} \pi_ {H} ^ {D *} = \theta_ {0} \big (q _ {H} \big (\tau_ {B} \big) - q _ {L} \big (\tau_ {B} \big) \big) \big (1 - \theta_ {0} \big) + \gamma_ {H} \big (1 - \theta_ {0} \big) ^ {2} \\ \pi_ {L} ^ {D *} = 0 \end{array} \right.\tag{9.3}
$$

(All proofs of equilibria, lemmas, propositions, and corollaries are relegated to the Appendix.)

As shown below, our analysis on the equilibrium solutions (8) and (9) leads to several interesting analytical findings.

Lemma 1: The equilibrium prices and profit rates for the two products remain constant in the duopoly stage if the quality difference of the two products is fixed; otherwise, they increase with the quality difference of the two products.

Given our assumption that the rates of quality improvement for the two products after release are equal, their quality gap remains unchanged in the duopoly stage. Therefore, although consumers at large benefit from the quality improvement, as long as the quality difference of the two products upon the release time of product B is exogenous, the two vendors do not change their respective subscription prices, maintaining constant market shares and profit rates throughout the duopoly stage.

By examining the conditions for the equilibrium, we find that when the quality difference between the two products f a l l s w i t h i n a s p e c i f i c r e g i o n , t h a t i s , $\left( q _ { H } \left( \tau _ { _ { B } } \right) - q _ { L } \left( \tau _ { _ { B } } \right) \right) \in \left[ 0 , \frac { 1 - \theta _ { 0 } } { 1 - 2 \theta _ { 0 } } ( \gamma _ { _ { L } } + 2 \gamma _ { _ { H } } ) \right]$ the equilibrium price and  , profit rate for Vendor L drop to zero. Hereafter, we refer to this region as the zero-profit region for Vendor L. Thus, when deciding on the optimal release time, Vendor B, if having chosen to target the low-end market, should avoid falling within this region. When $\gamma _ { L } = \gamma _ { H } = 0$ (i.e., the two products are fully compatible), the above zero-profit region for quality difference shrinks to $0 \ ( \mathrm { i . e . , } \ q _ { H } ( \tau _ { B } ) = q _ { L } \big ( \tau _ { B } \big ) \ )$ , indicating that it is not profitable for the new entrant to release a product of the same quality as the existing product. The observation below presents an interesting property of the zero-profit region.

Observation 1: Vendor L’s zero-profit region expands with the incompatibility between the two products $( i . e . , \gamma _ { H } a n d \gamma _ { L } )$ ).

The above observation suggests that the higher the level of incompatibility (either from H to L or from L to H), the larger is the zero-profit region for Vendor L.

We summarize our results regarding the impact of the level of incompatibility on the equilibrium outcomes (8) and (9) in Table 2. As shown in the table, when the quality difference upon the release time of product B is relatively large, Vendor L can benefit from a lower level of incompatibility (in either direction) between the two products. On the other hand, while Vendor H can also benefit from a lower level of incompatibility from the low quality product to its product, it prefers to have a higher level of incompatibility from its product to the low quality product.

In the region $( \left( q _ { { \cal H } } \left( \tau _ { { \cal B } } \right) - q _ { { \cal L } } \left( \tau _ { { \cal B } } \right) \right) < \frac { 1 - \theta _ { \scriptscriptstyle 0 } } { 1 - 2 \theta _ { \scriptscriptstyle 0 } } \left( \gamma _ { { \cal L } } + 2 \gamma _ { { \cal H } } \right) )$ , the zero-profit region for Vendor $\mathrm { L , }$ the profit rate of Vendor H increases with $\gamma _ { H } .$ This is because a higher $\gamma _ { H }$ will better differentiate product H from product L by decreasing the network value of the latter and, as a result, Vendor H can charge a higher price for its product.

With the two vendors’ optimal subscription prices obtained, we next derive the optimal product release time for the new entrant in full-compatibility and partial-compatibility scenarios.

## Fully Compatible SaaS Products

To rapidly gain a footing in a market, a new entrant often has no option but to make its product as compatible with the existing product as possible. Therefore, in this section, we focus on the scenario where product B is made fully compatible with product A $( \mathrm { i . e . , } \beta _ { A } = \beta _ { B } = \alpha )$ . Under such a scenario, consumers of the two products form a joint network and contribute indistinguishably to the common network effects.

In the previous section, we obtained the optimal price and profit rate assuming the release time of product B is given. We now derive the optimal release time of product B. Product release time is an important strategic decision for Vendor B because it determines the product quality upon release, which, as shown in Equations (8) and (9), in turn affects the vendor’s equilibrium price, market share, and profit rate. Furthermore, the release time also determines the remaining service time for Vendor B in the finite demand window.

Unlike in the previous section where the objective is to maximize the profit rates, here the vendor aims to maximize its total profit for the entire demand window, denoted by $\Pi _ { B } ,$ which equals the total revenue, that is, the product of the profit rate $( \pi _ { B } ^ { D ^ { * } } )$ and the duration of service $( D - \tau _ { B } )$ , minus the marginal development cost (see Equation (3)). From (8) and (9), it is clear that the functional form of Vendor B’s profit rate depends on whether the quality of its product is lower than that of product A, or, equivalently, whether product B is released before the instant of time $( \tau _ { E } = \frac { \Delta q _ { 0 } } { \lambda } )$ when the qualities of the two products become equal.

Table 2. Impact of Levels of Incompatibility on Price, Demand, and Profit Rate

<table><tr><td colspan="2">Changes in levels of incompatibility</td><td> $p_{H}^{D*}$ </td><td> $Q_{H}^{D*}$ </td><td> $\pi_{H}^{*}$ </td><td> $p_{L}^{D*}$ </td><td> $Q_{L}^{D*}$ </td><td> $\pi_{L}^{*}$ </td></tr><tr><td rowspan="2"> $(q_{H}-q_{L})\geq\frac{1-\theta_{0}}{1-2\theta_{0}}(\gamma_{L}+2\gamma_{H})$ </td><td> $\gamma_{H}$ increases</td><td>↓</td><td>↑</td><td>↑</td><td>↓</td><td>↓</td><td>↓</td></tr><tr><td> $\gamma_{L}$ increases</td><td>↓</td><td>↑</td><td>↓</td><td>↓</td><td>↓</td><td>↓</td></tr><tr><td rowspan="2"> $(q_{H}-q_{L})<\frac{1-\theta_{0}}{1-2\theta_{0}}(\gamma_{L}+2\gamma_{H})$ </td><td> $\gamma_{H}$ increases</td><td>↑</td><td>–</td><td>↑</td><td>–</td><td>–</td><td>–</td></tr><tr><td> $\gamma_{L}$ increases</td><td>–</td><td>–</td><td>–</td><td>–</td><td>–</td><td>–</td></tr></table>

Based on the above discussion and the equilibrium solutions (8) and (9), the optimal release time for product B in the fullcompatibility scenario can be obtained by maximizing Vendor B’s total profit with respect to $\tau _ { B } .$

$$
\max _ {\tau_ {B}} \Pi_ {B} (\tau_ {B}) = \left\{ \begin{array}{l} r \left[ q _ {A} (\tau_ {B}) - q _ {B} (\tau_ {B}) \right] (D - \tau_ {B}) - k \tau_ {B}, \tau_ {B} \leq \tau_ {E} \\ s \left[ q _ {B} (\tau_ {B}) - q _ {A} (\tau_ {B}) \right] (D - \tau_ {B}) - k \tau_ {B}, \tau_ {B} > \tau_ {E} \end{array} \right.\tag{10}
$$

$$
\text { where } r = \left(\frac {1 - 2 \theta_ {0}}{3}\right) ^ {2} \text { and } s = \left(\frac {2 - \theta_ {0}}{3}\right) ^ {2}.
$$

As shown above, Vendor B has different objective functions at the two time intervals separated by $\tau _ { E } ,$ hence we need to examine the two intervals separately.<sup>6</sup> When $\tau _ { B } \leq \tau _ { E } ,$ , as shown in Figure $3 , \Pi _ { B }$ decreases with $\tau _ { B } ,$ thus, we have a local optimum $\tau _ { B } ^ { * } = 0$ , implying that Vendor B’s best strategy is to release its product at time 0, and its profit is $\Pi _ { { \scriptscriptstyle B } } = r \Delta q _ { 0 } D _ { \scriptscriptstyle B }$ where $\Delta \boldsymbol { q } _ { 0 }$ denotes the initial quality gap (at time 0), that is, $\Delta q _ { 0 } = q _ { A 0 } - q _ { B 0 } .$

When $\tau _ { B } > \tau _ { E } ,$ as shown in Figure 3, there is a parabolic relationship between $\Pi _ { B }$ and $\tau _ { B } .$ . Specifically, when $\tau _ { B } \in ( \tau _ { E } , \tau _ { d } ] ,$ where $\tau _ { d } = \frac { D } { 2 } + \frac { \Delta q _ { 0 } } { 2 \lambda } - \frac { k } { 2 \lambda s }$ Vendor B’s profit increases with, $\tau _ { B } ,$ attaining a local maximum at $\tau _ { B } ^ { * } = \tau _ { d } ^ { \phantom { * } } ,$ when $\tau _ { B } \in ( \tau _ { d } , D ]$ , the profit decreases with $\tau _ { B } .$ Therefore, the second locally optimal solution is $\tau _ { B } ^ { * } = \tau _ { d }$ With the two local optima being considered, the globally optimal solution for Vendor B is simply the local optimum with the higher profit, that is, $\Pi _ { B } ^ { * } = \operatorname* { m a x } \left\{ \Pi _ { _ B } \left( 0 \right) , \Pi _ { _ B } \left( \tau _ { d } \right) \right\}$ and $\tau _ { B } ^ { * } = \underset { \tau _ { B } \in \{ 0 , \tau _ { d } \} } { \arg \operatorname* { m a x } } \left\{ \Pi _ { B } ( \tau _ { B } ) \right\}$

We are able to identify the condition under which one local optimum is better than the other. The condition contains the following threshold value:

$$
\Delta \bar {q} _ {0} = \min \left\{D \lambda + \frac {k}{s} + \frac {2 \lambda r D}{s} - \frac {2 \lambda}{s} \sqrt {r ^ {2} D ^ {2} + \frac {k s D}{\lambda} + \frac {k r D}{\lambda} + D ^ {2} s r}, \quad D \lambda - \frac {k}{s} \right\}
$$

We summarize the derived condition in the proposition below.

Proposition 1: When the two vendors’ products are fully compatible, if the initial product quality gap is above a certain threshold $( i . e . , \ \Delta q _ { 0 } > \Delta \overline { { q } } _ { 0 } )$ , it is optimal for Vendor B to release its product at time $\theta \ ( i . e . , \ \tau _ { B } ^ { * } = 0 )$ Otherwise $( i . e . , \Delta q _ { 0 } \leq \Delta \overline { { q } } _ { 0 } )$ , it is optimal for Vendor B to release the product at $\tau _ { B } ^ { * } = \tau _ { d } ,$ at which point its quality is higher than that of product A. The realized total profits of Vendors A and B during the demand window [0, D] are

$$
\Pi_ {A} ^ {*} = \left\{ \begin{array}{l l} s \Delta q _ {0} D, & \Delta q _ {0} > \Delta \overline {{q}} _ {0} \\ \Pi_ {A} ^ {M *} + \Pi_ {A} ^ {D *}, & \Delta q _ {0} \leq \Delta \overline {{q}} _ {0} \end{array} \right.
$$

$$
\Pi_ {B} ^ {*} = \left\{ \begin{array}{c c} r \Delta q _ {0} D, & \Delta q _ {0} > \Delta \overline {{q}} _ {0} \\ \frac {D ^ {2} s \lambda}{4} - \frac {D s \Delta q _ {0}}{2} - \frac {D k}{2} + \frac {\Delta q _ {0} ^ {2} s}{4 \lambda} + \frac {k ^ {2}}{4 \lambda s} - \frac {k \Delta q _ {0}}{2 \lambda}, & \Delta q _ {0} \leq \Delta \overline {{q}} _ {0} \end{array} \right.
$$

respectively, where $\Pi _ { A } ^ { M ^ { * } } = \pi _ { A } ^ { M } \left( \frac { D } { 2 } + \frac { \Delta q _ { 0 } } { 2 \lambda } - \frac { k } { 2 \lambda s } \right)$ and $\Pi _ { A } ^ { D * } = r \lambda \Biggl [ \left( \frac { D } { 2 } - \frac { \Delta q _ { 0 } } { 2 \lambda } \right) ^ { 2 } - \frac { k ^ { 2 } } { 4 \lambda ^ { 2 } s ^ { 2 } } \Biggr ]$ are Vendor A’s profits in the monopoly and duopoly stages within the demand window [0, D], respectively, and $\pi _ { A } ^ { M }$ is Vendor A’s profit rate in the monopoly stage.

Corollary 1 follows immediately from Proposition 1.

Corollary 1: At the local optimum $\tau _ { B } ^ { * } = 0$ , product B has a lower quality (and lower price) than product A, whereas at the other local optimum $\tau _ { B } ^ { * } = \tau _ { d } ,$ , product B surpasses product A in quality and commands a higher price.

![](/api/attachments/TRJXGV8F/fulltext/images/b0712fe7d5d0c10c3de453c5b85632d22daf70df0b6223c1b9441c925d0678c2.jpg)  
Figure 3. Vendor B’s Profit as a Function of τ<sub>B</sub>

Proposition 1 and Corollary 1 summarize one of the most interesting findings of the present research. In practice, we observe that some SaaS vendors such as Revolution Analytics and Highrise adopted a low-quality/low-price strategy while others such as SuccessFactors followed a high-quality/highprice strategy. Proposition 1 suggests that the preferred strategy of the new entrant depends critically on the initial quality gap between the product offerings of the incumbent and new entrant. When the initial quality gap is relatively large (recall that product B has a lower initial quality than product A at time 0), it is optimal for the new entrant to release its product at time 0. Conversely, when the initial quality gap is relatively small, it is optimal for Vendor B to continue its product development and release product B at a later time. This result is counterintuitive, as one would expect that if the new entrant’s product quality is initially low, instead of releasing it immediately, the new entrant might be better off continuing the development process to enhance its product quality.

An explanation for this counterintuitive result is as follows. If the initial quality gap is relatively large, it would take the new entrant too long to catch up with the incumbent in product quality. Consequently, the new entrant might be better off just serving the lower-end market immediately, which we refer to as the instant-release strategy. This is because with subscription-based licensing, unlike that of traditional perpetual licensing, vendors could derive more revenue by simply being in service for a longer period of time. On the other hand, if the initial quality gap is relatively small, the new entrant may be better off adopting a completely different strategy: deferring the release of its product and continuing to improve its product quality. We refer to such a strategy as the late-release strategy. Compared with the instant-release strategy, the late-release strategy, if optimal, allows the new entrant to surpass its rival in product quality when entering the market, and end up reaping more profit in a shorter service period.

The mathematical reasoning behind Proposition 1 can be illustrated with Figure 4. The two continuous curves in the figure represent Vendor B’s profit functions corresponding to the two local maxima illustrated in Figure 3. Specifically, with $\tau _ { B } ^ { * } { = } 0$ , the $\mathrm { p r o f i t } \Pi _ { B } ( 0 )$ increases monotonically with $\Delta \boldsymbol { q } _ { 0 } .$ With $\tau _ { B } ^ { * } = \tau _ { d } ,$ , Vendor $\mathrm { B } ^ { \prime } \mathrm { s }$ profit is a quadratic function of the initial quality gap $\Delta q _ { 0 } ,$ , attaining its theoretical minimum at $\Delta q _ { 0 } = D \lambda + \frac { k } { s }$ . However, when $\Delta q _ { 0 } > D \lambda$ , we find that $\tau _ { E }$ is larger than $D ,$ which is clearly not feasible. Therefore, with $\tau _ { B } ^ { * } = \tau _ { d } ,$ the profit $\Pi _ { B } ( \tau _ { d } )$ decreases monotonically with $\Delta \boldsymbol { q } _ { 0 }$ until $\Delta q _ { 0 } = D \lambda$ The two curves intersect at $\Delta q _ { 0 } = \Delta \overline { { q } } _ { 0 } .$ Clearly, to the left of the intersection point of the curves, since the profit curve $\Pi _ { B } ( \tau _ { d } )$ is above the curve $\Pi _ { B } ( 0 )$ , it is optimal for the new entrant to release its product at $\tau _ { B } ^ { * } = \tau _ { d } ^ { \phantom { * } } ,$ to the right of the intersection point, it is optimal to release the product at $\tau _ { B } ^ { * } = 0$ . The aforementioned optimal profit curves are depicted using solid lines in Figure 4.

Another corollary also follows from Proposition 1.

Corollary 2: Vendor $B ^ { \prime } s$ s profit at the equilibrium decreases with $\Delta { q } _ { 0 }$ when $\Delta q _ { 0 } \leq \Delta \overline { { q } } _ { 0 } ,$ , and increases monotonically when $\Delta q _ { 0 } > \Delta \overline { { q } } _ { 0 } .$

The above corollary suggests that when the instant-release strategy is the optimal choice, the new entrant is better off having a lower initial quality at the start of the horizon. This result is counterintuitive, as one would think that a higher initial quality would result in a higher profit for the new entrant. One possible explanation for this result is as follows.

![](/api/attachments/TRJXGV8F/fulltext/images/d836fe098f89160d27f4201311b754bbbf15a7d2b4a06e11ba61efa3b540f69e.jpg)

$$
\Delta \bar {q} _ {0} = \min \left\{D \lambda + \frac {k}{s} + \frac {2 \lambda r D}{s} - \frac {2 \lambda}{s} \sqrt {r ^ {2} D ^ {2} + \frac {k s D}{\lambda} + \frac {k r D}{\lambda} + D ^ {2} s r}, \quad D \lambda - \frac {k}{s} \right\}
$$

Figure 4. Vendor B’s Profit as a Function of Initial Quality Gap

Given that the optimal release strategy is instant-release, the new entrant upon release would have a lower product quality than the incumbent. Therefore, the new entrant, by having an even lower initial quality, can benefit from more product differentiation and less price competition with the incumbent.

In addition, we identify the following analytical properties based on the comparative statics analysis of the equilibrium outcomes.

Corollary 3: When $\Delta q _ { 0 } > \Delta \bar { q } _ { 0 } ,$ we have $\begin{array} { r } { \frac { \partial \Pi _ { B } ^ { * } } { \partial D } > 0 , \frac { \partial \Pi _ { B } ^ { * } } { \partial \Delta q _ { 0 } } > 0 , } \end{array}$ $\frac { \partial \Pi _ { A } ^ { * } } { \partial D } > 0 .$ and , $\frac { \partial \Pi _ { A } ^ { * } } { \partial \Delta q _ { 0 } } > 0$ . When $\Delta q _ { 0 } \leq \Delta \overline { { q } } _ { 0 } ,$ the following properties hold:

$$
\frac {\partial \tau_ {B} ^ {*}}{\partial D} > 0, \quad \frac {\partial \Pi_ {B} ^ {*}}{\partial D} \geq 0, \quad \frac {\partial \Pi_ {A} ^ {*}}{\partial D} > 0.
$$

$$
\frac {\partial \tau_ {B} ^ {*}}{\partial k} <   0, \quad \frac {\partial \Pi_ {B} ^ {*}}{\partial k} \leq 0, \quad \frac {\partial \Pi_ {A} ^ {*}}{\partial k} <   0.
$$

c. When $\begin{array} { r l r } { k } & { { } \le } & { s \Delta q _ { 0 } , } \end{array}$ we have $\frac { \partial \tau _ { B } ^ { * } } { \partial \lambda } \leq 0 , \frac { \partial \Pi _ { B } ^ { * } } { \partial \lambda } > 0 ,$ $\frac { \partial \Pi _ { \mathcal { A } } ^ { M * } } { \partial \lambda } { \leq } 0$ and , $\frac { \partial \Pi _ { A } ^ { D * } } { \partial \lambda } > 0 ;$ when $k > s \Delta q _ { 0 } ,$ we have $\frac { \partial \tau _ { B } ^ { * } } { \partial \lambda } > 0 , \frac { \partial \Pi _ { B } ^ { * } } { \partial \lambda } > 0 , \frac { \partial \Pi _ { A } ^ { * } } { \partial \lambda } > 0 .$

$$
d. \quad \frac {\partial \tau_ {B} ^ {*}}{\partial q _ {B 0}} <   0, \quad \frac {\partial \Pi_ {B} ^ {*}}{\partial q _ {B 0}} > 0, \quad \frac {\partial \Pi_ {A} ^ {M *}}{\partial q _ {B 0}} <   0, a n d \frac {\partial \Pi_ {A} ^ {D *}}{\partial q _ {B 0}} > 0.
$$

Some of the results in Corollary 3 are noteworthy. For instance, under the condition $\Delta q _ { 0 } \leq \Delta \overline { { q } } _ { 0 } ,$ , when it is optimal for Vendor B to further improve its product quality after time 0, both vendors’ profits increase as the marginal development cost for Vendor B decreases. Although the conclusion regarding Vendor $\mathrm { B } ^ { \prime } \mathrm { s }$ profit is intuitive, the one regarding Vendor A’s is not. Further examination reveals that Vendor A can benefit from Vendor B’s lower marginal development cost for two reasons: (1) with lower marginal development cost, Vendor B will postpone its product release, so Vendor A will enjoy a longer monopoly period; (2) a longer development period may allow product B to have a greater quality advantage over product $\mathbf { A } ,$ leading to more product differentiation and hence less price competition between the two vendors, and as a result, Vendor A’s profit rate in the duopoly stage can increase.

Corollary 3 also indicates that, when $\Delta q _ { 0 } \leq \Delta \overline { { q _ { 0 } } }$ , with a higher initial product quality $q _ { B 0 } ,$ Vendor B releases its product earlier and achieves a higher profit; the profit for Vendor A, on the other hand, is lower in the monopoly stage and higher in the duopoly stage. One possible explanation for such changes in Vendor $\mathrm { \bf A } \ ' \mathrm { \bf s }$ profit is that as product B is released earlier, the duration of the monopoly stage is shortened and that of the duopoly stage is extended.

![](/api/attachments/TRJXGV8F/fulltext/images/3a26a5239cd7bf7af0372027fa55598cf7efca3fefbf578d964098ca16213b9e.jpg)  
Figure 5. Impact of Product B’s Initial Quality on Equilibrium Outcomes

We also conduct numerical analysis to further investigate the impacts of the initial product quality of the new entrant on its profit and optimal release time. Given the discrete nature of the equilibrium solutions, we keep the initial quality gap $( \Delta q _ { 0 } )$ close to $\Delta \overline { { q _ { 0 } } }$ in our numerical analyses. The default values for the parameters are set at $D = 2 0 , \lambda = 0 . 1 , k = 0 . 1 , \theta _ { 0 } = 0 , \alpha =$ 1, and $q _ { A 0 } = 2$ . We vary the value of $q _ { B 0 }$ while holding other parameter values constant.

As shown in Figure 5, Vendor B’s profit curve bears resemblance to that in Figure 4. The pattern of the change from the late-release to instant-release of product B is also consistent with our theoretical findings. The optimal release time curve shown in Figure 5 demonstrates the switching pattern for the two locally optimal solutions as described in Proposition 1.

## Partially Compatible SaaS Products

In this section, we analyze a more general scenario where Vendor B has made its product partially compatible with product A. Under this scenario, consumers of one product can still benefit from the consumer network of the other one, but the intensity of cross-product network effects is smaller than that of within-product network effects (i.e., $\{ \beta _ { A } , \beta _ { B } \} < \alpha )$ For example, although Google Docs and Microsoft Office differ in product features, Google Docs allows users to open and edit Microsoft Office files using the Office Compatibility Mode (OCM); thus, Google Docs and Microsoft Word partially share each other’s network and can be considered partially compatible products.

Recall that product B starts with a lower quality, but catches up with product A in quality at a later time $\begin{array} { r } { \tau _ { E } = \frac { \Delta q _ { 0 } } { \lambda } } \end{array}$ which<sup>,</sup> divides the demand window into two intervals: $[ 0 , \tau _ { E } )$ and $[ \tau _ { E } , D ]$ . From the equilibrium equations (8) and (9), the market share of product B drops to zero when $\left( q _ { A } - q _ { B } \right) \in { \left[ 0 , \frac { 1 - \theta _ { 0 } } { 1 - 2 \theta _ { 0 } } \left( \gamma _ { B } + 2 \gamma _ { A } \right) \right] } .$ and product B captures<sup>,</sup> the entire market when $\begin{array} { r } { \left( q _ { B } - q _ { A } \right) \in \bigg [ 0 , \frac { 1 - \theta _ { 0 } } { 1 - 2 \theta _ { 0 } } \left( \gamma _ { A } + 2 \gamma _ { B } \right) \bigg ] . } \end{array}$ Accordingly, the zero-profit release time interval for product B is $\tau _ { B } \in \left[ \underline { { \tau } } _ { 1 } , \tau _ { E } \right]$ and its winner-take-all time interval , is $\tau _ { B } \in \left[ \tau _ { E } , \overline { { \tau } } _ { 1 } \right] .$ where $\begin{array} { r } { \underline { { \tau } } _ { 1 } = \frac { \Delta q _ { 0 } } { \lambda } - \frac { 1 - \theta _ { 0 } } { 1 - 2 \theta _ { 0 } } \frac { 2 \gamma _ { A } + \gamma _ { B } } { \lambda } } \end{array}$ ， and $\overline { { \tau } } _ { 1 } = \frac { \Delta q _ { 0 } } { \lambda } + \frac { 1 - \theta _ { 0 } } { 1 - 2 \theta _ { 0 } } \frac { 2 \gamma _ { B } + \gamma _ { A } } { \lambda }$ We summarize the above findings. in the lemma below.

Lemma 2: It is not profitable for Vendor B to release its product in its zero-profit time interval $\big [ \underline { { \tau } } _ { 1 } , \tau _ { E } \big ] .$ If the vendor releases its product in the winner-take-all time interval $\left( \tau _ { E } , \overline { { \tau } } _ { 1 } \right)$ ,  product A will be driven out of the market. The above two time intervals expand with the levels of incompatibility between the products $( \gamma _ { A }$ and $\gamma _ { B } ) .$

Figure 6 shows the zero-profit and winner-take-all release time intervals for the new entrant. Apparently, Vendor B should avoid releasing its product in the zero-profit time interval. On the other hand, it is worth noting that releasing in the winner-take-all interval may not be the optimal strategy for Vendor B either, as it can be shown analytically that an earlier release in $[ 0 , \underline { { \tau } } _ { 1 } )$ can result in a longer service period and a later release after $\overline { { \tau _ { 1 } } }$ can lead to a higher profit rate.

<table><tr><td rowspan="2"></td><td colspan="2">Zero-Profit Region</td><td colspan="2">Winner-Take-All Region</td></tr><tr><td>0</td><td> $\tau_{1}$ </td><td> $\tau_{E}$ </td><td> $\overline{\tau}_{1}$ </td></tr></table>

Figure 6. Zero-Profit and Winner-Take-All Release Time Intervals for the New Entrant

Substituting $q _ { H } \mathbf { o r } q _ { L }$ in Equations (8.3) and (9.3) with $q _ { B } ( \tau _ { B } )$ $= q _ { B 0 } + \lambda _ { 1 } \tau _ { B } \mathrm { o r } q _ { A } ( \tau _ { B } ) = q _ { A 0 } + \lambda _ { 2 } \tau _ { B }$ , we obtain Vendor B’s profit rate:

$$
\pi_ {B} ^ {D *} = \left\{ \begin{array}{l l} \frac {1}{9} \frac {\left[ (1 - 2 \theta_ {0}) \left(q _ {A 0} - q _ {B 0} - \lambda \tau_ {B}\right) - \left(1 - \theta_ {0}\right) \left(\gamma_ {B} + 2 \gamma_ {A}\right) \right] ^ {2}}{q _ {A 0} - q _ {B 0} - \lambda \tau_ {B} - \gamma_ {B} - \gamma_ {A}}, & \tau_ {B} <   \underline {{\tau}} _ {1} \\ \theta_ {0} \left(q _ {B 0} + \lambda \tau_ {B} - q _ {A 0}\right) (1 - \theta_ {0}) + \gamma_ {B} (1 - \theta_ {0}) ^ {2}, & \tau_ {E} <   \tau_ {B} <   \overline {{\tau}} _ {1} \\ \frac {1}{9} \frac {\left[ (2 - \theta_ {0}) \left(q _ {B 0} + \lambda \tau_ {B} - q _ {A 0}\right) - (1 - \theta_ {0}) (2 \gamma_ {A} + \gamma_ {B}) \right] ^ {2}}{q _ {B 0} + \lambda \tau_ {B} - q _ {A 0} - \gamma_ {A} - \gamma_ {B}}, & \overline {{\tau}} _ {1} \leq \tau_ {B} \leq D \end{array} \right. \tag {11}
$$

Vendor B’s profit maximization problem is, therefore,

$$
\max _ {\tau_ {B}} \Pi_ {B} = \left\{ \begin{array}{l l} \frac {1}{9} \frac {\left[ (1 - 2 \theta_ {0}) (q _ {x 0} - q _ {B 0} - \lambda \tau_ {B}) - (1 - \theta_ {0}) (\gamma_ {B} + 2 \gamma_ {A}) \right] ^ {2}}{q _ {x 0} - q _ {B 0} - \lambda \tau_ {B} - \gamma_ {B} - \gamma_ {A}} (D - \tau_ {B}) - k \tau_ {B}, & \tau_ {B} <   \underline {{\tau}} _ {1} \\ \left[ \theta_ {0} (q _ {B 0} + \lambda \tau_ {B} - q _ {A 0}) (1 - \theta_ {0}) + \gamma_ {B} (1 - \theta_ {0}) ^ {2} \right] (D - \tau_ {B}) - k \tau_ {B}, & \tau_ {E} <   \tau_ {B} <   \overline {{\tau}} _ {1} \\ \frac {1}{9} \frac {\left[ (2 - \theta_ {0}) (q _ {B 0} + \lambda \tau_ {B} - q _ {A 0}) - (1 - \theta_ {0}) (2 \gamma_ {A} + \gamma_ {B}) \right] ^ {2}}{q _ {B 0} + \lambda \tau_ {B} - q _ {A 0} - \gamma_ {A} - \gamma_ {B}} (D - \tau_ {B}) - k \tau_ {B}, & \overline {{\tau}} _ {1} \leq \tau_ {B} \leq D \\ \text {s.t.} & \tau_ {B} \in [ 0, \underline {{\tau}} _ {1}) \cup (\tau_ {E}, D ] \end{array} \right. \tag {1}\tag{12}
$$

To obtain the globally optimal solution for problem (12), we first derive the locally optimal solutions in two intervals: the low-quality interval $[ 0 , \ \underline { { \tau } } _ { 1 } )$ and the high-quality interval $( \tau _ { E } , D ]$ . When $\tau _ { B } \in [ 0 , \underline { { \tau } } _ { 1 } )$ , product $\mathrm { B } ^ { \prime } \mathrm { s }$ quality is lower than that of product A. It can be shown that $\begin{array} { r } { \frac { \partial \pi _ { B } ^ { D * } } { \partial \tau _ { B } } < 0 } \end{array}$ holds in this region, implying that Vendor $\mathrm { B } ^ { \prime } \mathrm { s }$ total profit decreases with $\tau _ { B }$ when $\tau _ { B } \in [ 0 , \underline { { \tau } } _ { 1 } )$ . Therefore, $\tau _ { B } ^ { * } = 0$ is the only one local maximum in the interval $[ 0 , \underline { { \tau } } _ { 1 } )$

As shown in Figure $6 , \overline { { \tau } } _ { 1 }$ divides the high-quality interval $( \tau _ { E } , D ]$ into two sub-intervals: $( \tau _ { E } , \overline { { \tau } } _ { 1 } )$ and $[ \overline { { \tau } } _ { 1 } , D ] .$ . In $( \tau _ { E } , \overline { { \tau } } _ { 1 } )$ , the only possible interior local optimal solution is $\tau _ { d 1 } = \frac { D } { 2 } + \frac { \Delta q _ { 0 } } { 2 \lambda } - \frac { \gamma _ { B } \left( 1 - \theta _ { 0 } \right) ^ { 2 } + k } { 2 \lambda \theta _ { 0 } \left( 1 - \theta _ { 0 } \right) }$ While a closed-form expres-<sup>.</sup> sion for the optimal solution in $[ \overline { { \tau } } _ { 1 } , D ]$ cannot be analytically derived for $k > 0 ,$ , we are still able to obtain some interesting analytical findings.

Le $\begin{array} { r } { \tau _ { d 2 } = \frac { D } { 4 } + \frac { 3 \left( \Delta q _ { 0 } + \gamma _ { A } + \gamma _ { B } \right) } { 4 \lambda } + \frac { \sqrt { \left( D \lambda - \Delta q _ { 0 } - \gamma _ { A } - \gamma _ { B } \right) \left( D \lambda - \Delta q _ { 0 } - \gamma _ { A } - \gamma _ { B } + x \right) } } { 4 \lambda } } \end{array}$ where $\begin{array} { r } { x = \frac { 8 ( 1 - \theta _ { 0 } ) } { 2 - \theta _ { 0 } } \big ( 2 \gamma _ { \scriptscriptstyle A } + \gamma _ { \scriptscriptstyle B } \big ) - 8 \gamma _ { \scriptscriptstyle A } - 8 \gamma _ { \scriptscriptstyle B } . } \end{array}$ Regarding Vendor $\mathrm { B } ^ { \prime } \mathrm { s }$ release strategy, we have the following proposition:

Proposition 2: When the two products are partially compatible, if their initial quality gap is sufficiently large, Vendor B should release its products instantly; otherwise, it is better off adopting the late-release strategy.<sup>7</sup> In the latter scenario, Vendor B should release its product no later than time $\overline { { \tau } } _ { 1 }$ or $\tau _ { d 2 } ,$ whichever occurs later (i.e., $\tau _ { E } < \tau _ { B } ^ { * } \leq \operatorname* { m a x } \{ \overline { { \tau } } _ { 1 } , \tau _ { d 2 } \} \big )$

Corollary 4 follows immediately from Proposition 2.

Corollary 4: The following two types of late-release strategies are possible. Type I: Vendor B releases its products in $[ \overline { { \tau } } _ { 1 } , \tau _ { d 2 } )$ , and Vendors A and B serve the low-end and high-end markets, respectively; Type II: Vendor B releases its product in the winner-take-all region $( \tau _ { E } , \overline { { \tau } } _ { 1 } )$ , driving product A out of market.

Proposition 2 is in line with Proposition 1 obtained for the full-compatibility scenario. We analytically show that in the partial-compatibility scenario, even with asymmetric incompatibility, the instant-release strategy (i.e., entering the market at time zero) and the late-release strategy (i.e., releasing product B after it surpasses product A in quality) are still the only two options that Vendor B should consider, and the best market entry timing still depends on the initial quality gap.

As for the two types of late release strategies outlined in Corollary 4, which one is preferable to the new entrant depends on the degree of incompatibility between the two competing products. As shown in Figure 7, as the degrees of incompatibility $( \gamma _ { A }$ and $\gamma _ { B } )$ increase, Vendor B’s optimal laterelease strategy changes from Type I to Type II.

It is also worth noting that Corollary 1 still holds in this partial-compatibility scenario. That is, the instant-release strategy is a low-quality/low-price strategy, whereas the laterelease strategy is a high-quality/high-price strategy.

In addition, we conduct comparative static analyses to investigate how the levels of incompatibility affect the price, demand, and profit of the new entrant, and summarize the results in the lemma below.

![](/api/attachments/TRJXGV8F/fulltext/images/23a651a56ffd1a4a1ae50f4798054e998e6ca91546b654142068987982e3c581.jpg)  
(Parameter Values: $D = 2 0 , k = 0 . 1 , \alpha = 0 . 2 , \lambda = 0 . 1 , \theta _ { 0 } = 0 , q _ { A 0 } = 2 , q _ { B 0 } = 1 . 4 5 )$

Figure 7. Optimal Release Strategy

Table 3. Impacts of γ<sub>A</sub> or γ<sub>B</sub> on Equilibrium Outcome for Vendor B

<table><tr><td rowspan="3">Changes in levels of incompatibility</td><td rowspan="2" colspan="3">Instant-Release Strategy</td><td colspan="6">Late-Release Strategy</td></tr><tr><td colspan="3">Type I</td><td colspan="3">Type II</td></tr><tr><td> $p_{B}^{D*}$ </td><td> $Q_{B}^{D*}$ </td><td> $\Pi_{B}^{*}$ </td><td> $p_{B}^{D*}$ </td><td> $Q_{B}^{D*}$ </td><td> $\Pi_{B}^{*}$ </td><td> $p_{B}^{D*}$ </td><td> $Q_{B}^{D*}$ </td><td> $\Pi_{B}^{*}$ </td></tr><tr><td> $\gamma_{A}$  increases</td><td>↓</td><td>↓</td><td>↓</td><td>↓</td><td>↑</td><td>↓</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $\gamma_{B}$  increases</td><td>↓</td><td>↓</td><td>↓</td><td>↓</td><td>↑</td><td>↑</td><td>↑</td><td>-</td><td>↑</td></tr></table>

Lemma 3: When Vendor B adopts the instant-release strategy, its profit decreases with the level of incompatibility (in either direction). When Vendor B adopts the late-release strategy, its profit increases with the level of incompatibility from product B to product A, but decreases with the level of incompatibility in the other direction.

Table 3 provides a more detailed summary of the impact of the levels of incompatibility on the equilibrium price, demand, and profit for Vendor B.

In order to determine the optimal release time for product B, we need to first calculate Vendor B’s total profit corresponding to the instant-release and late-release strategies, respectively, and then choose the one with the higher profit. Since the optimal release time for the late-release strategy is not analytically tractable, we resort to numerical methods to obtain the globally optimal solution. We set the parameter values at $D = 2 0 , \lambda = 0 . 1 , q _ { A 0 } = 2 , \theta _ { 0 } = 0 , \alpha = 0 . 5 , k = 0 . 1 , q _ { B 0 }$ $= 1 . 2 5$ , and $\gamma _ { A } , \gamma _ { B } \in [ 0 , 0 . 5 ]$ The impacts of the levels of incompatibility on Vendor B’s optimal market entry strategy and profit are shown in Figure 8.

Figure 8(a) shows that the new entrant prefers the instantrelease strategy when both $\gamma _ { A }$ and $\gamma _ { B }$ are relatively small, and the late-release strategy when both $\gamma _ { A }$ and $\gamma _ { B }$ are relatively large. The explanation is as follows. According to Lemma 2, an increase in $\gamma _ { A }$ and $\gamma _ { B }$ will lead to the expansion of the zeroprofit region for the low-quality vendor. When the values of $\gamma _ { A }$ and $\gamma _ { B }$ are sufficiently large, Vendor B, who has a lower initial quality, would fall within the zero-profit region if the instant-release strategy was adopted; thus, Vendor B would prefer to adopt the late-release strategy. As shown in Figure 8(b), Vendor B’s profit obtained in the instant-release strategy decreases when $\gamma _ { A }$ increases, and that obtained in the laterelease strategy increases with $\gamma _ { B } .$ These observations are in line with our analytical findings in Lemma 3 and Table 3.

## Model Extensions

In this section, we explore four extended models (Model Extensions I–IV), with one key assumption being relaxed in each of the models. Due to space constraints, we choose to present only Model Extension I, which addresses the issues of switching cost, in the main text. We relegate the detailed analysis of the other three extended models (Model Extensions II–IV) to the appendix, and retain only a summary of the models at the end of this section.

![](/api/attachments/TRJXGV8F/fulltext/images/e14294b687c6c5ef93d371c850da0fe805fe69b3f7e91c0267a1d78dd2a1aa95.jpg)  
(a) Optimal Market Entry Strategy

![](/api/attachments/TRJXGV8F/fulltext/images/7bfc66e3f8f7cc1e89ccd821d59db5fbb662de9b9d94503adee8a23ec367b014.jpg)  
(b) Maximal Profit  
Figure 8. Optimal Market Entry Strategy and Maximal Profit of Vendor B

## Model Extension I: A Model with Switching Cost

In the previous sections, we implicitly assume that the cost for consumers to switch from product A to product B is negligible. In some markets, however, switching cost could be significant for end users due to differences in functionalities, interfaces, platforms, and data formats of the two SaaS products. Therefore, it may seem reasonable to assume that a higher level of compatibility is necessarily associated with a lower switching cost. In practice, however, an incumbent can inflate the switching cost regardless of the level of compatibility between a competitor’s product and its own. For instance, customers can upload data to Amazon Web Services (AWS) for free, but have to pay to take data out of it (Butler 2013), which makes it difficult for the customers to switch to the competing vendors who provide compatible services.

In this subsection, we take into account users’ switching cost and reexamine the two vendors’ decisions on product quality, pricing, and entry timing. As before, we first derive the equilibrium prices of the two products and then analyze Vendor B’s optimal market entry timing.

We use $\hat { \theta } ^ { M }$ to denote the type of consumer who is indifferent between subscribing and not subscribing to product A in the monopoly stage, and $\hat { \theta } \left( \hat { \theta } \geq \hat { \theta } ^ { M } \right)$ to denote the type of consumer who subscribes to product A before $\tau _ { B }$ and is indifferent between switching to product B and continuing to use product A after $\tau _ { B } .$ With switching cost, denoted by $c _ { S } ,$ taken into consideration, consumers will revise the net utility obtained from product B. We assume that $c _ { S }$ is linearly increasing with the duration of time the users have been using the product, that is,

$$
c _ {S} = c _ {0} (\tau_ {B} - \tau_ {A})\tag{13}
$$

where $c _ { 0 }$ is a positive constant, and $\tau _ { { \scriptscriptstyle A } } , \tau _ { { \scriptscriptstyle A } } < 0 .$ , is the release time of product A.

The indifferent consumer type $\hat { \theta }$ satisfies the following equation:

$$
\begin{array}{l} \left(\hat {\theta} q _ {A} (\tau_ {B}) - p _ {A} ^ {D} + \alpha Q _ {A} ^ {D} + \beta_ {B} Q _ {B} ^ {D}\right) (D - \tau_ {B}) = \\ \left(\hat {\theta} q _ {B} (\tau_ {B}) - p _ {B} ^ {D} + \alpha Q _ {B} ^ {D} + \beta_ {A} Q _ {A} ^ {D}\right) (D - \tau_ {B}) - c _ {S} \end{array}\tag{14}
$$

Solving Equation (14) yields

$$
\hat {\theta} = \frac {p _ {B} ^ {D} - p _ {A} ^ {D} + \gamma_ {A} Q _ {A} ^ {D} - \gamma_ {B} Q _ {B} ^ {D}}{q _ {B} (\tau_ {B}) - q _ {A} (\tau_ {B})} + \frac {c _ {S}}{(q _ {B} (\tau_ {B}) - q _ {A} (\tau_ {B})) (D - \tau_ {B})}\tag{15}
$$

To take into account switching cost, we need to know how the market is divided between the two vendors. Other than the three types of market segmentation scenarios shown in Figure 9, switching cost doesn’t affect the market size of the two vendors. Therefore, we focus on these three types of market segmentation.

![](/api/attachments/TRJXGV8F/fulltext/images/5c1349e96dfcdb595cd944a1160267ccf5f3f67c4ebe7a59a5815b5c2418d9ae.jpg)  
(a) Case I: $q _ { B } ( \tau _ { B } ) > q _ { A } ( \tau _ { B } )$ and $\hat { \theta } ^ { M } \leq \hat { \theta } ^ { D }$

![](/api/attachments/TRJXGV8F/fulltext/images/c3c76e39eeb48a87a637cfd275db72e6fb4b1864c42853df9e2bbadb7b39f0ba.jpg)  
(b) Case II: $q _ { B } ( \tau _ { B } ) > q _ { A } ( \tau _ { B } )$ and $\hat { \theta } ^ { D } < \hat { \theta } ^ { M } < \hat { \theta }$

![](/api/attachments/TRJXGV8F/fulltext/images/97298ea56a699d498c1c97bc68eaf27e894957f5f3b50bba17a5b4ebc44bc76a.jpg)  
(c) Case III: $q _ { B } ( \tau _ { B } ) < q _ { A } ( \tau _ { B } )$ and $\hat { \theta } ^ { M } < \hat { \theta }$  
Figure 9. Market Segmentation when Switching Cost Is Considered

Recall that $\hat { \theta } ^ { M }$ is the type of consumer who is indifferent between subscribing and not subscribing to product A in the monopoly stage and $\hat { \theta } ^ { D }$ is the consumer type that derives identical net utility from products A and B in the duopoly stage when switching cost is not considered. From

$$
\hat {\boldsymbol {\theta}} ^ {D} = \frac {p _ {B} ^ {D} - p _ {A} ^ {D} + \gamma_ {A} Q _ {A} ^ {D} - \gamma_ {B} Q _ {B} ^ {D}}{q _ {B} (\tau_ {B}) - q _ {A} (\tau_ {B})}
$$

and

$$
\hat {\boldsymbol {\theta}} = \frac {p _ {B} ^ {D} - p _ {A} ^ {D} + \gamma_ {A} Q _ {A} ^ {D} - \gamma_ {B} Q _ {B} ^ {D}}{q _ {B} (\tau_ {B}) - q _ {A} (\tau_ {B})} + \frac {c _ {S}}{(q _ {B} (\tau_ {B}) - q _ {A} (\tau_ {B})) (D - \tau_ {B})},
$$

we conclude that $\hat { \theta }$ is larger than $\hat { \theta } ^ { D }$ when $q _ { B } ( \tau _ { B } ) > q _ { A } ( \tau _ { B } )$ To fully understand the market segmentation, we also need to compare the values of $\hat { \theta } ^ { D }$ and $\hat { \theta } ^ { M }$ , where $\hat { \theta } ^ { M }$ is assumed to be exogenous in this section.

As shown in Figure 9, before Vendor B enters the market, all consumers located in $\left[ \hat { \theta } ^ { \scriptscriptstyle M } , 1 \right]$ would subscribe to product A. In Case I, after product B is released, the consumers in $\left[ \theta _ { 0 } , \hat { \theta } \right]$ will continue to use product A, while those in $\left( { \hat { \theta } } , 1 \right]$ will switch to product B. In Case II, the market is divided into four segments after product B is released, the consumers located in $\left( { \hat { \theta } } , 1 \right]$ will switch to product B. In the meantime, the consumers in $\left[ \theta _ { 0 } , \hat { \theta } ^ { M } \right)$ start their new subscription. Specifically, those in $\left[ \theta _ { 0 } , \hat { \theta } ^ { D } \right]$ will subscribe to product A, and those in $\left( \hat { \theta } ^ { D } , \hat { \theta } ^ { M } \right)$ will subscribe to product B. In Case III, consumers in $\left( { \hat { \theta } } , 1 \right]$ will subscribe to product A, and those in $\big [ \theta _ { 0 } , \hat { \theta } \big ]$ will subscribe to product B in the duopoly stage.

For each of the three cases shown in Figure 9, there is a set of profit rate functions that leads to an equilibrium. The details of the equilibria are provided in Section 13 of the Appendix.

The closed-form expression for product B’s optimal release time cannot be obtained. Thus, we conduct numerical analyses to investigate the impacts of switching cost on the Vendor B’s pricing, quality, and entry timing decisions. We set the parameter values at $D = 2 0 , \lambda = 0 . 1 , q _ { \scriptscriptstyle A 0 } = 2 , \tau _ { \scriptscriptstyle A } = - 2 , \theta _ { 0 } = 0 ,$ α $= 0 . 2 , k = 0 . 1 , q _ { B 0 } \in \{ 1 . 3 , 1 . 5 , 1 . 7 \} , \gamma _ { A } = 0 . 1 , \gamma _ { B } = 0 \mathrm { { } } .$ , and $c _ { 0 } =$ $0 , 0 . 0 2 , 0 . 0 4 , . . . , 0 . 2$ , with increments of 0.02.

Figure 10 shows how Vendor B’s market entry timing and total profit change with the switching cost. From this figure, we can draw the following conclusions. First, the results concerning the optimal release time suggest that when the initial quality gap is relatively small $( { \bf e . g . } , q _ { B 0 } = 1 . 7 )$ , the laterelease strategy is optimal for the new entrant. When the initial quality gap is relatively large $( { \bf e . g . } , q _ { B 0 } = 1 . 3 )$ , the vendor is better off adopting the instant-release strategy. When the initial quality gap is moderate $( { \bf e . g . } , q _ { B 0 } = 1 . 5 )$ , as the switching cost becomes higher, Vendor B’s optimal strategy changes from late-release to instant-release. Therefore, the effect of a higher switching cost on the release strategy appears to be similar to that of a larger initial quality gap. Second, Vendor B’s profit decreases monotonically as the switching cost increases, indicating the increasing market power of the incumbent over the new entrant.

![](/api/attachments/TRJXGV8F/fulltext/images/8ffdecd991ada18c75d650ddf3407506e96bab72a86ea78ed806d457e472e08f.jpg)

![](/api/attachments/TRJXGV8F/fulltext/images/18869e242d6f7e49e25b6796cb7c605de265c98371c4f1567469b291042d910b.jpg)  
Figure 10. Vendor B’s Optimal Release Time and Profit as Functions of c<sub>0</sub>

![](/api/attachments/TRJXGV8F/fulltext/images/4ceb0b33e97c0b1091791b78fd97323018877b928c21ee63c9dcc060367935d3.jpg)  
Figure 11. Release Strategy under Different Combinations of ∆q<sub>0</sub> and c<sub>0</sub>

Figure 11 provides a more complete picture of one of the most important conclusions of the present research. The solid line in the figure represents the threshold quality gap that divides the space into the late-release region and the instant-release region. As shown in the figure, regardless of the levels of switching cost, if the initial quality gap is sufficiently small $( \mathrm { i } . { \mathsf { e } } . , q _ { B 0 }$ is sufficiently close to $q _ { A 0 } ) _ { i }$ , the late-release strategy is always preferred by the new entrant; when the initial quality gap $\Delta \boldsymbol { q } _ { 0 }$ is above a certain threshold, the optimal release strategy changes to instant-release. Furthermore, as the switching cost increases, the threshold value that separates the late-release and the instant-release regions drops, indicating that the instant-release strategy becomes more preferable to the consumers when the switching cost is higher.

In summary, our key findings in the previous sections remain valid even when consumers’ switching cost is considered, and with a higher switching cost the new entrant is more likely to adopt the instant-release strategy.

## Summary of Model Extensions II–IV

To check the robustness of our main findings, we also explore three other model extensions (Model Extensions II-IV), details of which are provided in the Appendix. Specifically, in Model Extension II (Section 14 of the Appendix), we analyze the case in which the assumption of linear development cost is relaxed and the marginal development cost is assumed to be a quadratic function of development time. In

Model Extension III (Section 15 of the Appendix), we investigate the scenario where the assumption of equal post-release quality improvement rate is relaxed and the two vendors have unequal post-release quality improvement rates. In Model Extension IV (Section 16 of the Appendix), we study the scenario where the full market coverage assumption is relaxed and the market is assumed to be partially covered. We find that our main results on market entry strategy remain valid under these extensions.

## Conclusion and Future Research

Software-as-a-service (SaaS), a new software licensing and delivery model widely considered a convenient and costefficient alternative to the traditional on-premises model, has recently received considerable attention from both industry and academia. The market of SaaS has expanded rapidly and attracted a large number of software vendors, leading to intense competition among SaaS vendors and unfavorable market conditions for new entrants. To survive and thrive in the competitive market, new SaaS vendors need to strategically make market entry decisions. Unfortunately, the extant literature on SaaS provides little insight in this regard. In fact, to the best of our knowledge, no attempt has yet been made to explore the competition between a new entrant and an incumbent vendor in a SaaS market. Our study aims to fill this gap in the literature. Specifically, we employ a gametheoretic framework to investigate the scenario where a new SaaS vendor seeks to enter the market and compete with an incumbent vendor providing substitutable SaaS products, making strategic market decisions on product quality, pricing, and entry timing.

The main findings of this research are as follows. First, we find that the new entrant’s optimal decision on entry timing depends on the initial quality gap between the competing products. Specifically, if the quality of the new product is close to that of the existing one, the new entrant would prefer to adopt a late-release strategy (i.e., deferring the release of the new product in order to further improve it and eventually surpass the existing product in quality); otherwise, the new entrant would prefer to adopt an instant-release strategy (i.e., releasing the product immediately). We find that instantrelease and late-release lead to a low-quality/low-price strategy, and a high-quality/high-price strategy, respectively. Second, if the two products are partially compatible, when the new entrant adopts the instant-release strategy, a higher level of incompatibility (in either direction) will reduce its profit, and as a result, the new entrant may find it unprofitable to employ the instant-release strategy if the level of incompatibility is sufficiently high. When the new entrant adopts the late-release strategy, its profit increases with the level of incompatibility from its product to the incumbent’s, but may decrease with the level of incompatibility in the other direction. Finally, we show that our main findings remain valid even when factors such as consumers’ switching cost are taken into consideration.

Our research has important practical implications for SaaS vendors. First of all, the closed-form analytical solutions that we obtain for the optimal entry timing and pricing can be used as guidelines for SaaS vendors to make strategic market decisions, especially when they are seeking to enter a market occupied by an incumbent vendor. For instance, the proposed instant-release and late-release strategies could help the new entrant determine the best timing of market entry. It is important to note that, regardless of which release strategy is chosen, the new entrant needs to make sure that it sufficiently differentiates its product from the incumbent’s in quality. In addition, our analyses regarding the impact of degrees of incompatibility on equilibrium outcomes can provide some managerial guidelines for the new SaaS vendors when deciding to what extent its product should be compatible with the existing product.

We have to acknowledge that our study, like any other research endeavor, is not without its limitations. One limitation is that we assume the incumbent vendor’s initial product quality is exogenous in our models. One possible direction for future study is to endogenize the incumbent’s own market entry timing and hence its initial product quality, and derive the optimal market entry timing, pricing, and quality decisions for two competing SaaS vendors. A second limitation is that the current study analyzes the competition between two SaaS vendors primarily from the new vendor’s perspective, and the incumbent is more passive than the entrant in its response to competition and can only compete along the pricing dimension. In an extension study, it would be interesting to analyze a more comprehensive scenario where vendors compete along both product quality and pricing dimensions. A related limitation of the present study is that we assume the incumbent does not employ any deterrence strategy when the market entry of a new SaaS vendor is imminent. A future study could take into consideration possible short-term entry deterrence actions the incumbent may take, such as lowering the price of subscription and allocating more resources on quality improvement, and reexamine the market entry strategy for new vendors. Furthermore, an interesting phenomenon often observed in the SaaS market is that some vendors offer their product for free (e.g., Google Docs versus Office 365) in exchange for other benefits such as a larger customer base or sales of complementary products. While it is beyond the scope of the present study to address this issue, we believe it can be a potential avenue for future research.

## Acknowledgments

The authors would like to thank the senior editor, Sulin Ba, the associate editor, and the three anonymous reviewers for their insightful comments and suggestions that have helped us greatly in improving the quality of this paper. The first author (Haiyang Feng) acknowledges the financial support from the National Natural Science Foundation of China (Grant No. 71701147 and 70925005), and also would like to thank Professor Minqiang Li from Tianjin University for his support and guidance throughout this project. Dengpan Liu’s research was supported in part by the National Natural Science Foundation of China under grant 71490723.

## References

Bayus, B. L. 1997. “Speed-to-Market and New Product Performance Trade-Offs,” Journal of Product Innovation Management (14:6), pp. 485-497.

Beal, B. 2008. “NetSuite’s Salesforce.com Discount Indicative of SaaS CRM Pricing Pressures,” TechTarget (http://searchcrm. techtarget.com/news/1335708/NetSuite-s-Salesforce-comdiscount-indicative-of-SaaS-CRM-pricing-pressures).

Bergemann, D., and Välimäki, J. 2002. “Entry and Vertical Differentiation,” Journal of Economic Theory (106:1), pp. 91-125.

Blattberg, R. C., and Wisniewski, K. J. 1989. “Price-Induced Patterns of Competition,” Marketing Science (8:4), pp. 291-309.

Boccard, N., and Wauthy, X. Y. 2010. “Equilibrium Vertical Differentiation in a Bertrand Model with Capacity Precommitment,” International Journal of Industrial Organization (28:3), pp. 288-297.

Brynjolfsson, E., and Kemerer, C. F. 1996. “Network Externalities in Microcomputer Software: An Econometric Analysis of the Spreadsheet Market,” Management Science (42:12), pp. 1627-1647.

Butler, B. 2013. “Cloud Prices: How Low Can They Go?,” Network World, March 28 (http://www.networkworld.com/ article/2164852/cloud-computing/cloud-prices--how-low-canthey-go-.html).

Calantone, R. J, and Di Benedetto, C. A. 2000. “Performance and Time to Market: Accelerating Cycle Time with Overlapping Stages,” IEEE Transactions on Engineering Management (47:2), pp. 232-244.

Chen, P.-Y., and Wu, S.-Y. 2012. “The Impact and Implications of On-Demand Services on Market Structure,” Information Systems Research (24:3), pp. 750-767.

Cheng, H. K., and Koehler, G. J. 2003. “Optimal Pricing Policies of Web-Enabled Application Services,” Decision Support Systems (35:3), pp. 259-272.

Cheng, H. K., and Liu, Y. 2012. “Optimal Software Free Trial Strategy: The Impact of Network Externalities and Consumer Uncertainty,” Information Systems Research (23:2), pp. 488-504.

Choudhary, V. 2007. “Comparison of Software Quality under Perpetual Licensing and Software as a Service,” Journal of Management Information Systems (24:2), pp. 141-165.

Choudhary, V., Tomak, K., and Chaturvedi, A. 1998. “Economic Benefits of Renting Software,” Journal of Organizational Computing and Electronic Commerce (8:4), pp. 277-305.

Cisco. 2014. “Cisco Global Cloud Index: Forecast and Methodology, 2013–2018,” Cisco, San Jose, CA.

Cochrane, T., Shah, S., Murphy, J., and Holliday, J. 2014. “How SaaS Providers Can Use Pricing to Achieve Their Ambitions,” Bain Brief, July 9, Bain & Company, Boston.

Cohen, M. A., Eliasberg, J., and Ho, T.-H. 1996. “New Product Development: The Performance and Time-to-Market Tradeoff,” Management Science (42:2), pp. 173-186.

Colombo, M. G., and Delmastro, M. 2002. “The Determinants of Organizational Change and Structural Inertia: Technological and Organizational Factors,” Journal of Economics & Management Strategy (11:4), pp. 595-635.

Columbus, L. 2012. “SaaS Adoption Accelerates, Goes Global in the Enterprise,” Forbes, October 31 (http://www.forbes.com/ sites/louiscolumbus/2012/10/31/saas-adoption-accelerates-goesglobal-in-the-enterprise/).

Dutta, P. K., Lach, S., and Rustichini, A. 1995. “Better Late Than Early: Vertical Differentiation in the Adoption of a New Technology,” Journal of Economics & Management Strategy (4:4), pp. 563-589.

Fan, M., Kumar, S., and Whinston, A. B. 2009. “Short-Term and Long-Term Competition between Providers of Shrink-Wrap Software and Software as a Service,” European Journal of Operational Research (196:2), pp. 661-671.

Fishburn, P. C., and Odlyzko, A. M. 1999. “Competitive Pricing of Information Goods: Subscription Pricing Versus Pay-Per-Use,” Economic Theory (13:2), pp. 447-470.

Fuentelsaz, L., Maicas, J. P., and Polo, Y. 2012. “Switching Costs, Network Effects, and Competition in the European Mobile Telecommunications Industry,” Information Systems Research (23:1), pp. 93-108.

Gallaugher, J. M., and Wang, Y. M. 2002. “Understanding Network Effects in Software Markets: Evidence from Web Server Pricing,” MIS Quarterly (26:4), pp. 303-327.

Ghemawat, P. 1991. “Market Incumbency and Technological Inertia,” Marketing Science (10:2), pp. 161-171.

Gurnani, H., and Karlapalem, K. 2001. “Optimal Pricing Strategies for Internet-Based Software Dissemination,” Journal of the Operational Research Society (52:1), pp. 64-70.

Hamerman, P. D. 2014. “Application Adoption Trends: The Rise of SaaS,” Forrester Research, Cambridge, MA, May 5 (https://www.forrester.com/report/Application+Adoption+ Trends+The+Rise+Of+SaaS/-/E-RES116071).

Hannan, M. T., and Freeman, J. 1984. “Structural Inertia and Organizational Change,” American Sociological Review (49:2), pp. 149-164.

Henschen, D. 2011. “Low-Cost Options for Predictive Analytics Challenge SAS, IBM,” Information Week, July 26 (http://www.informationweek.com/software/informationmanagement/low-cost-options-for-predictive-analytics-challengesas-ibm/d/d-id/1099191).

Hoppe, H. C., and Lehmann-Grube, U. 2001. “Second Mover Advantages in Dynamic Quality Competition,” Journal of Economics & Management Strategy (10:3), pp. 419-433.

Hung, N. M., and Schmitt, N. 1988. “Quality Competition and Threat of Entry in Duopoly,” Economics Letters (27:3), pp. 287-292.

Jing, B. 2007. “Network Externalities and Market Segmentation in a Monopoly,” Economics Letters (95:1), pp. 7-13.

Kalish, S., and Lilien, G. L. 1986. “A Market Entry Timing Model for New Technologies,” Management Science (32:2), pp. 194-205.

Katz, M. L., and Shapiro, C. 1985. “Network Externalities, Competition, and Compatibility,” The American Economic Review (75:5), pp. 424-440.

Kopel, M., and Löffler, C. 2008. “Commitment, First-Mover, and Second-Mover Advantage,” Journal of Economics (94:2), pp. 143-166.

Kwang, K. 2012. “Competition Keeps SaaS Profits Artificially Low,” ZD Net, November 23 (http://www.zdnet.com/article/ competition-keeps-saas-profits-artificially-low/).

Liu, Q., and Zhang, D. 2013. “Dynamic Pricing Competition with Strategic Customers under Vertical Product Differentiation,” Management Science (59:1), pp. 84-101.

Lutz, S. 1997. “Vertical Product Differentiation and Entry Deterrence,” Journal of Economics (65:1), pp. 79-102.

Ma, D., and Kauffman, R. J. 2014. “Competition between Software-as-a-Service Vendors,” IEEE Transactions on Engineering Management (61:4), pp. 717-729.

Ma, D., and Seidmann, A. 2015. “Analyzing Software as a Service with Per-Transaction Charges,” Information Systems Research (26:2), pp. 360-378.

Niculescu, M. F., Shin, H., and Whang, S. 2012. “Underlying Consumer Heterogeneity in Markets for Subscription-Based IT Services with Network Effects,” Information Systems Research (23:4), pp. 1322-1341.

Noh, Y. H., and Moschini, G. 2006. “Vertical Product Differentiation, Entry-Deterrence Strategies, and Entry Qualities,” Review of Industrial Organization (29:3), pp. 227-252.

Pang, M.-S., and Etzion, H. 2012. “Research Note–Analyzing Pricing Strategies for Online Services with Network Effects,” Information Systems Research (23:4), pp. 1364-1377.

Pettey, C., and Goasduff, L. 2017. “Gartner Says Worldwide Public Cloud Services Market to Grow 18 Percent in 2017,” Gartner Newsroom, February 22 (https://www.gartner.com/ newsroom/id/ 3616417).

Rodríguez-Pinto, J., Carbonell, P., and Rodríguez-Escudero, A. I. 2011. “Speed or Quality? How the Order of Market Entry Influences the Relationship between Market Orientation and New Product Performance,” International Journal of Research in Marketing (28:2), pp. 145-154.

Savin, S., and Terwiesch, C. 2005. “Optimal Product Launch Times in a Duopoly: Balancing Life-Cycle Revenues with Product Cost,” Operations Research (53:1), pp. 26-47.

Shankar, V., and Bayus, B. L. 2003. “Network Effects and Competition: An Empirical Analysis of the Home Video Game Industry,” Strategic Management Journal (24:4), pp. 375-384.

Software Equity Group. 2015. “The Software Industry Financial Report,” Software Equity Group, San Diego, CA (http://softwareequity.com/Reports/2015\_Software\_Industry\_ Financial\_Report.pdf).

Tatum, C. 2013. “The 2013 CRM Vendor Landscape,” CRM Switch, January 3 (http://www.crmswitch.com/crm-industry/crmvendor-landscape-2013/).

Wauthy, X. 1996. “Quality Choice in Models of Vertical Differentiation,” The Journal of Industrial Economics (44:3), pp. 345-353.

Zhang, J., and Seidmann, A. 2010. “Perpetual Versus Subscription Licensing Under Quality Uncertainty and Network Externality Efects,” Journal of Management Information Systems (27:1), pp. 39-68.

Zhu, K. X., and Zhou, Z. Z. 2012. “Research Note–Lock-in Strategy in Software Competition: Open-Source Software Vs. Proprietary Software,” Information Systems Research (23:2), pp. 536-545.

## About the Authors

Haiyang Feng is an assistant professor of Information Management and Management Science at the College of Management and Economics, Tianjin University. He received his Ph.D. in Management Science from Tianjin University in 2014. His current research interests include economics of information systems, platform strategy, and business analytics. His papers have been published in academic journals including International Journal of Production Economics, Computers & Industrial Engineering, Computers & Operations Research, and Soft Computing.

Zhengrui Jiang is the Thome Professor in Business and associate professor of information systems at the College of Business, Iowa State University. He received his Ph.D. in Management Science with a concentration in information systems from the University of Texas at Dallas. His primary research interests include business intelligence/analytics, diffusion of innovations, and economics of information goods. He has published in leading academic journals including Information Systems Research, Management Science, IEEE Transactions on Knowledge and Data Engineering, INFORMS Journal on Computing, and Journal of Management Information Systems. He currently serves as an associate editor for MIS Quarterly. He also served as a program cochair for the 2014 Midwest Association of Information Systems Conference and the 2015 Big XII+ MIS Research Symposium.

Dengpan Liu is a professor at the Department of Management Science and Engineering in the School of Economics and Management, Tsinghua University. He received his Ph.D. in management science with a concentration in information systems from the University of Texas at Dallas in 2006. His current research interests include economics of information systems, information security, optimal software development methodologies, and personalization at e-commerce sites. He has published in Information Systems Research, Management Science, and Journal of Management Information Systems, among others.

# QUALITY, PRICING, AND RELEASE TIME: OPTIMAL MARKET ENTRY STRATEGY FOR SOFTWARE-AS-A-SERVICE VENDORS

Haiyang Feng College of Management and Economics, Tianjin University, Tianjin 300072, CHINA {hyfeng@tju.edu.cn}

Zhengrui Jiang College of Business, Iowa State University, Ames, Iowa 50011-2027 U.S.A. {zjiang@iastate.edu}

Dengpan Liu School of Economics and Management, Tsinghua University, Beijing, CHINA 100084 {liudp@sem.tsinghua.edu.cn}

## Appendix

Proofs

1 Proof of Equilibrium Solutions (8) and (9)

$$
\begin{array}{l} \left\{ \begin{array}{l} \max _ {p _ {L} ^ {D}} \pi_ {L} = p _ {L} ^ {D} \left(\hat {\theta} ^ {D} - \theta_ {0}\right) \\ \max _ {p _ {H} ^ {D}} \pi_ {H} = p _ {H} ^ {D} \left(1 - \hat {\theta} ^ {D}\right) \end{array} \right. \\ s. t. \theta_ {0} \leq \hat {\theta} ^ {D} \leq 1 \\ p _ {L} ^ {D} \geq 0, p _ {H} ^ {D} \geq 0 \end{array}\tag{7}
$$

Substituting $\begin{array} { r } { \hat { \theta } ^ { D } = \frac { p _ { H } ^ { D } - p _ { L } ^ { D } - \theta _ { 0 } \gamma _ { L } - \gamma _ { H } } { q _ { H } \left( \tau _ { B } \right) - q _ { L } \left( \tau _ { B } \right) - \gamma _ { H } - \gamma _ { L } } } \end{array}$ into (7), and solving the first order conditions yields

$$
\left\{ \begin{array}{l} p _ {H} ^ {D *} = \frac {(2 - \theta_ {0}) (q _ {H} (\tau_ {B}) - q _ {L} (\tau_ {B})) - (1 - \theta_ {0}) (2 \gamma_ {L} + \gamma_ {H})}{3} \\ p _ {L} ^ {D *} = \frac {(1 - 2 \theta_ {0}) (q _ {H} (\tau_ {B}) - q _ {L} (\tau_ {B})) - (1 - \theta_ {0}) (\gamma_ {L} + 2 \gamma_ {H})}{3} \end{array} \right.\tag{8.1}
$$

and

$$
\left\{ \begin{array}{l} \hat {\theta} ^ {D *} = \frac {1}{3} \frac {(1 + \theta_ {0}) (q _ {H} (\tau_ {B}) - q _ {L} (\tau_ {B})) - (1 + 2 \theta_ {0}) \gamma_ {L} - (\theta_ {0} + 2) \gamma_ {H}}{q _ {H} (\tau_ {B}) - q _ {L} (\tau_ {B}) - \gamma_ {L} - \gamma_ {H}} \\ Q _ {H} ^ {D *} = \frac {1}{3} \frac {(2 - \theta_ {0}) (q _ {H} (\tau_ {B}) - q _ {L} (\tau_ {B})) - (1 - \theta_ {0}) (2 \gamma_ {L} + \gamma_ {H})}{q _ {H} (\tau_ {B}) - q _ {L} (\tau_ {B}) - \gamma_ {L} - \gamma_ {H}} \\ Q _ {L} ^ {D *} = \frac {1}{3} \frac {(1 - 2 \theta_ {0}) (q _ {H} (\tau_ {B}) - q _ {L} (\tau_ {B})) - (1 - \theta_ {0}) (\gamma_ {L} + 2 \gamma_ {H})}{q _ {H} (\tau_ {B}) - q _ {L} (\tau_ {B}) - \gamma_ {L} - \gamma_ {H}} \end{array} \right.\tag{8.2}
$$

Thus, the two vendors’ profits are

$$
\left\{ \begin{array}{l} \pi_ {H} ^ {D *} = \frac {1}{9} \frac {\left[ (2 - \theta_ {0}) (q _ {H} (\tau_ {B}) - q _ {L} (\tau_ {B})) - (1 - \theta_ {0}) (2 \gamma_ {L} + \gamma_ {H}) \right] ^ {2}}{q _ {H} (\tau_ {B}) - q _ {L} (\tau_ {B}) - \gamma_ {L} - \gamma_ {H}} \\ \pi_ {L} ^ {D *} = \frac {1}{9} \frac {\left[ (1 - 2 \theta_ {0}) (q _ {H} (\tau_ {B}) - q _ {L} (\tau_ {B})) - (1 - \theta_ {0}) (\gamma_ {L} + 2 \gamma_ {H}) \right] ^ {2}}{q _ {H} (\tau_ {B}) - q _ {L} (\tau_ {B}) - \gamma_ {L} - \gamma_ {H}} \end{array} \right.\tag{8.3}
$$

The prices and demands of the two vendors in this equilibrium are positive if and only if $\begin{array} { r } { \big ( q _ { H } ( \tau _ { B } ) - q _ { L } ( \tau _ { B } ) \big ) \geq \frac { 1 - \theta _ { 0 } } { 1 - 2 \theta _ { 0 } } ( \gamma _ { L } + 2 \gamma _ { H } ) . } \end{array}$

When $\begin{array} { r } { \left( q _ { H } ( \tau _ { B } ) - q _ { L } ( \tau _ { B } ) \right) < \frac { 1 - \theta _ { 0 } } { 1 - 2 \theta _ { 0 } } ( \gamma _ { L } + 2 \gamma _ { H } ) } \end{array}$ , the price of Vendor L in Equilibrium (8) is negative, hence we have a new equilibrium solution by setting $p _ { L } ^ { D * } = 0$

$$
\left\{ \begin{array}{c} p _ {H} ^ {D *} = \theta_ {0} \big (q _ {H} (\tau_ {B}) - q _ {L} (\tau_ {B}) \big) + \gamma_ {H} (1 - \theta_ {0}) \\ p _ {L} ^ {D *} = 0 \end{array} \right.\tag{9.1}
$$

$$
\left(\hat {\theta} ^ {D *} = \theta_ {0} \right.\tag{9.2}
$$

$$
\left(Q _ {L} ^ {D *} = 0 \right.
$$

$$
\left\{ \begin{array}{c} \pi_ {H} ^ {D *} = \theta_ {0} \big (q _ {H} (\tau_ {B}) - q _ {L} (\tau_ {B}) \big) (1 - \theta_ {0}) + \gamma_ {H} (1 - \theta_ {0}) ^ {2} \\ \pi_ {L} ^ {D *} = 0 \end{array} \right.\tag{9.3}
$$

□□

## 2 Proof of Lemma 1

After product B’ release, the quality difference of the two products remains unchanged because the two vendors have the same post-release quality improvement rate. Therefore, from equations (8) and (9), the equilibrium prices and profit rates for the two products remain constant in the duopoly stage. In addition, equilibrium prices and profit rates for the two products increase with quality difference of the two products upon the release of product B because $\begin{array} { r } { \frac { \partial \pi _ { H } ^ { D * } } { \partial \Delta q } \geq 0 } \end{array}$ and $\begin{array} { r } { \frac { \partial \pi _ { L } ^ { D * } } { \partial \Delta q } \geq 0 } \end{array}$ hold $( \varDelta q = q _ { H } ( \tau _ { \mathrm { B } } ) - q _ { L } ( \tau _ { \mathrm { B } } ) )$ □□

## 3 Proof of Observation 1

From equilibrium (9.1) through (9.3), in the zero-profit region, i.e., $\begin{array} { r } { \left( q _ { H } ( \tau _ { B } ) - q _ { L } ( \tau _ { B } ) \right) < \frac { 1 - \theta _ { 0 } } { 1 - 2 \theta _ { 0 } } ( \gamma _ { L } + 2 \gamma _ { H } ) } \end{array}$ , the price and profit rate of Vendor L are both zero. Since $\frac { 1 - \theta _ { 0 } } { 1 - 2 \theta _ { 0 } }$ is positive, any increase in $\gamma _ { H } \mathrm { o r } \gamma _ { L }$ would expand this zero-profit region of Vendor L. □□

## 4 Proof of Proposition 1

$$
\max _ {\tau_ {B}} \Pi_ {B} = \left\{ \begin{array}{l} r [ q _ {A} (\tau_ {B}) - q _ {B} (\tau_ {B}) ] (D - \tau_ {B}) - k \tau_ {B}, \tau_ {B} \leq \tau_ {E} \\ s [ q _ {B} (\tau_ {B}) - q _ {A} (\tau_ {B}) ] (D - \tau_ {B}) - k \tau_ {B}, \tau_ {B} > \tau_ {E} \end{array} \right.\tag{10}
$$

The necessary conditions for $\tau _ { d }$ to be the globally optimal solution of (10) are

$$
\tau_ {E} <   \tau_ {d} <   D\tag{A1}
$$

$$
\Pi_ {B} (\tau_ {d}) > \Pi_ {B} (0)\tag{A2}
$$

Condition (A1) ensures that $\tau _ { d }$ belongs to the feasible region $( \tau _ { E } , D )$ , and (A2) is needed because $\tau _ { d }$ is the more profitable solution than 0. Since $\begin{array} { r } { \tau _ { E } = \frac { \Delta q _ { 0 } } { \lambda } } \end{array}$ and $\begin{array} { r } { \tau _ { d } = \frac { D } { 2 } + \frac { \Delta q _ { 0 } } { 2 \lambda } - \frac { \bar { k } } { 2 \lambda s } , } \end{array}$ condition (A1) is equivalent to

$$
\Delta q _ {0} <   D \lambda - \frac {k}{s}
$$

The profit difference between the two local optimal solutions is

$$
\Pi_ {B} (\tau_ {d}) - \Pi_ {B} (0) = \frac {s}{4 \lambda} \varDelta q _ {0} ^ {2} - \frac {D s}{2} \varDelta q _ {0} - \frac {k}{2 \lambda} \varDelta q _ {0} - r D \varDelta q _ {0} + \frac {D ^ {2} s \lambda}{4} + \frac {k ^ {2}}{4 s \lambda} - \frac {D k}{2}
$$

It can be shown that $\Pi _ { B } ( \tau _ { d } ) > \Pi _ { B } ( 0 )$ leads to

$$
\Delta q _ {0} <   \Delta q _ {0} ^ {\prime} \mathrm{or} \Delta q _ {0} > \Delta q _ {0} ^ {\prime \prime}
$$

$$
\text {where} \Delta q _ {0} ^ {\prime} = D \lambda + \frac {k}{s} + \frac {2 \lambda r D}{s} - \frac {2 \lambda}{s} \sqrt {r ^ {2} D ^ {2} + \frac {k s D}{\lambda} + \frac {k r D}{\lambda} + D ^ {2} s r} \text {and} \Delta q _ {0} ^ {\prime \prime} = D \lambda + \frac {k}{s} + \frac {2 \lambda r D}{s} + \frac {2 \lambda}{s} \sqrt {r ^ {2} D ^ {2} + \frac {k s D}{\lambda} + \frac {k r D}{\lambda} + D ^ {2} s r}.
$$

Note that $\Delta q _ { 0 } ^ { \prime \prime } > D \lambda - \frac { k } { s } ;$ thus, $\Delta q _ { 0 } > \Delta q _ { 0 } ^ { \prime \prime }$ violates condition (A1). Therefore, conditions (A1) and (A2) hold only when $\Delta { q } _ { 0 }$ satisfies

$$
\Delta q _ {0} \leq \Delta \bar {q} _ {0}
$$

$$
\text { where } \Delta \bar {q} _ {0} = \min \left\{D \lambda + \frac {k}{s} + \frac {2 \lambda r D}{s} - \frac {2 \lambda}{s} \sqrt {r ^ {2} D ^ {2} + \frac {k s D}{\lambda} + \frac {k r D}{\lambda} + D ^ {2} s r}, D \lambda - \frac {k}{s} \right\}.
$$

Therefore, i $\because \Delta q _ { 0 } \leq \Delta \bar { q } _ { 0 } , \tau _ { d }$ is the optimal release time; otherwise, Vendor B should release its product at time 0. Correspondingly, the profits of the two vendors are

$$
\Pi_ {B} ^ {*} = \left\{ \begin{array}{c c} r \Delta q _ {0} D, & \Delta q _ {0} > \Delta \bar {q} _ {0} \\ \frac {D ^ {2} s \lambda}{4} - \frac {D s \Delta q _ {0}}{2} - \frac {D k}{2} + \frac {\Delta q _ {0} ^ {2} s}{4 \lambda} + \frac {k ^ {2}}{4 \lambda s} - \frac {k \Delta q _ {0}}{2 \lambda}, \Delta q _ {0} \leq \Delta \bar {q} _ {0} \end{array} \right.
$$

$$
\Pi_ {A} ^ {*} = \left\{ \begin{array}{l l} s \Delta q _ {0} D, & \Delta q _ {0} > \Delta \bar {q} _ {0} \\ \Pi_ {A} ^ {M *} + \Pi_ {A} ^ {D *}, & \Delta q _ {0} \leq \Delta \bar {q} _ {0} \end{array} \right.
$$

where $\begin{array} { r } { \Pi _ { A } ^ { M * } = \pi _ { A } ^ { M * } \left( \frac { D } { 2 } + \frac { A q _ { 0 } } { 2 \lambda } - \frac { k } { 2 \lambda s } \right) \mathrm { a n d } \Pi _ { A } ^ { D * } = r \lambda \left[ \left( \frac { D } { 2 } - \frac { A q _ { 0 } } { 2 \lambda } \right) ^ { 2 } - \frac { k ^ { 2 } } { 4 \lambda ^ { 2 } s ^ { 2 } } \right] . } \end{array}$

□□

## 5 Proof of Corollary 1

When $\tau _ { B } ^ { * } = 0$ , the prices of product A and B take the forms

$$
\left\{ \begin{array}{l} p _ {A} ^ {D *} = \frac {2 - \theta_ {0}}{3} \Delta q _ {0} \\ p _ {B} ^ {D *} = \frac {1 - 2 \theta_ {0}}{3} \Delta q _ {0} \end{array} \right.
$$

The condition $\theta _ { 0 } \in \left[ 0 , \frac { 1 } { 2 } \right)$ leads to $\begin{array} { r } { \frac { 2 - \theta _ { 0 } } { 3 } > \frac { 1 - 2 \theta _ { 0 } } { 3 } ; } \end{array}$ ; thus, the equilibrium price of product B is lower than that of product A.

When Vendor B releases its product at $\begin{array} { r } { \tau _ { B } ^ { * } = \frac { D } { 2 } + \frac { \varDelta q _ { 0 } } { 2 \lambda } - \frac { k } { 2 \lambda s } . } \end{array}$ , the prices of product A and B become

$$
\left\{ \begin{array}{l} p _ {A} ^ {D *} = \frac {1 - 2 \theta_ {0}}{3} (q _ {B 0} + \lambda \tau_ {B} ^ {*} - q _ {A 0}) \\ p _ {B} ^ {D *} = \frac {2 - \theta_ {0}}{3} (q _ {B 0} + \lambda \tau_ {B} ^ {*} - q _ {A 0}) \end{array} \right.
$$

Since $\begin{array} { r } { \frac { 2 - \theta _ { 0 } } { 3 } > \frac { 1 - 2 \theta _ { 0 } } { 3 } ; } \end{array}$ , we conclude that the price of product B is higher than that of product A when the new entrant adopts the late-release strategy. □□

## 6 Proof of Corollary 2

As stated in Proposition 1, when $\varDelta q _ { 0 } \leq \varDelta \bar { q } _ { 0 }$ , Vendor B’s profit is given by

$$
\Pi_ {B} ^ {*} = \frac {D ^ {2} s \lambda}{4} - \frac {D s \varDelta q _ {0}}{2} - \frac {D k}{2} + \frac {\varDelta q _ {0} ^ {2} s}{4 \lambda} + \frac {k ^ {2}}{4 \lambda s} - \frac {k \varDelta q _ {0}}{2 \lambda}
$$

which is a quadric function of $\varDelta q _ { 0 }$ . As $\varDelta q _ { 0 }$ increases, $\Pi _ { B } ^ { * }$ reaches its minimum at $\begin{array} { r } { \varDelta q _ { 0 } = \frac { D } { \lambda } + \frac { k } { s } . } \end{array}$ . Since $\varDelta \bar { q } _ { 0 } < \frac { D } { \lambda } + \frac { k } { s } .$ Π<sup>∗</sup> decreases with $\varDelta q _ { 0 }$ when $\varDelta q _ { 0 } \leq \varDelta \bar { q } _ { 0 }$

When $\begin{array} { r } { \varDelta q _ { 0 } > \varDelta \bar { q } _ { 0 } . } \end{array}$ , the profit of Vendor B is given by

$$
\Pi_ {B} ^ {*} = r \Delta q _ {0} D
$$

which is an increasing function of $\Delta { { q } _ { 0 } }$ . Therefore, Vendor B’s profit increases monotonically with $\varDelta q _ { 0 }$ when $\varDelta q _ { 0 } > \varDelta \bar { q } _ { 0 }$

□□

## 7 Proof of Corollary 3

(1) When $\Delta q _ { 0 } > \Delta \bar { q } _ { 0 }$ the two vendors’ profits are given by

$$
\left\{ \begin{array}{l} \Pi_ {A} ^ {*} = s \Delta q _ {0} D \\ \Pi_ {B} ^ {*} = r \Delta q _ {0} D \end{array} \right.
$$

$$
\mathrm{Thus}, \frac {\partial \Pi_ {B} ^ {*}}{\partial D} = s \Delta q _ {0} > 0, \frac {\partial \Pi_ {B} ^ {*}}{\partial \Delta q _ {0}} = s D > 0, \frac {\partial \Pi_ {A} ^ {*}}{\partial D} = r \Delta q _ {0} > 0, \mathrm{and} \frac {\partial \Pi_ {A} ^ {*}}{\partial \Delta q _ {0}} = r D > 0.
$$

(2) When $\Delta q _ { 0 } \leq \Delta \bar { q } _ { 0 }$ , the vendors’ profits are

$$
\left\{ \begin{array}{c} \Pi_ {A} ^ {*} = \Pi_ {A} ^ {M *} + \Pi_ {A} ^ {D *} \\ \Pi_ {B} ^ {*} = \frac {D ^ {2} s \lambda}{4} - \frac {D s \varDelta q _ {0}}{2} - \frac {D k}{2} + \frac {\varDelta q _ {0} ^ {2} s}{4 \lambda} + \frac {k ^ {2}}{4 \lambda s} - \frac {k \varDelta q _ {0}}{2 \lambda} \end{array} \right.
$$

where $\begin{array} { r } { \Pi _ { A } ^ { M * } = \pi _ { A } ^ { M } \left( \frac { D } { 2 } + \frac { A q _ { 0 } } { 2 \lambda } - \frac { k } { 2 \lambda s } \right) \mathrm { a n d } \Pi _ { A } ^ { D * } = r \lambda \left[ \left( \frac { D } { 2 } - \frac { A q _ { 0 } } { 2 \lambda } \right) ^ { 2 } - \frac { k ^ { 2 } } { 4 \lambda ^ { 2 } s ^ { 2 } } \right] . } \end{array}$ , and the optimal release time is $\begin{array} { r } { \tau _ { B } ^ { * } = \frac { D } { 2 } + \frac { \Delta q _ { 0 } } { 2 \lambda } - \frac { k } { 2 \lambda s } . } \end{array}$

a. The first order derivatives of the optimal release time $( \tau _ { B } ^ { * } )$ and the profits $( \Pi _ { A } ^ { * } , \Pi _ { B } ^ { * } )$ with respect to the demand window ܦ are

$$
\frac {\partial \tau_ {B} ^ {*}}{\partial D} = \frac {1}{2}
$$

$$
\frac {\partial \Pi_ {B} ^ {*}}{\partial D} = \frac {s (D \lambda - \Delta q _ {0} - \frac {k}{s})}{2}
$$

$$
\frac {\partial \Pi_ {A} ^ {*}}{\partial D} = \frac {\pi_ {A} ^ {M}}{2} + r \frac {D \lambda - \Delta q _ {0}}{2}
$$

It is obvious that $\frac { \partial \tau _ { B } ^ { * } } { \partial D } > 0$ . From $\Delta q _ { 0 } \leq \Delta \bar { q } _ { 0 }$ we have $\begin{array} { r } { \Delta q _ { 0 } \le D \lambda - \frac { k } { s } , \mathrm { i . e . , } D \lambda - \Delta q _ { 0 } - \frac { k } { s } \ge 0 } \end{array}$ . Hence, we have $\begin{array} { r } { \frac { \partial \Pi _ { B } ^ { * } } { \partial D } \geq 0 \mathrm { ~ a n d } \frac { \partial \Pi _ { A } ^ { * } } { \partial D } > } \end{array}$ 0.

b. The first order derivatives of the optimal release time $( \tau _ { B } ^ { * } )$ and the profits $( \Pi _ { A } ^ { * } , \Pi _ { B } ^ { * } )$ with respect to the marginal development cost ݇ are

$$
\frac {\partial \tau_ {B} ^ {*}}{\partial k} = - \frac {1}{2 \lambda s}
$$

$$
\frac {\partial \Pi_ {B} ^ {*}}{\partial k} = - \frac {1}{2 \lambda} \left(D \lambda - \frac {k}{s} + \Delta q _ {0}\right)
$$

$$
\frac {\partial \Pi_ {A} ^ {*}}{\partial k} = - \frac {\pi_ {A} ^ {M}}{2 \lambda s} - \frac {r \lambda k}{2 \lambda^ {2} s ^ {2}}
$$

It is obvious that $\begin{array} { r } { \frac { \partial \tau _ { B } ^ { * } } { \partial k } < 0 } \end{array}$ and $\frac { \partial \Pi _ { A } ^ { * } } { \partial k } < 0$ . From $\Delta q _ { 0 } \leq \Delta \bar { q } _ { 0 }$ , we have $\begin{array} { r } { \Delta q _ { 0 } \le D \lambda - \frac { k } { s } ; } \end{array}$ ,thus $D \lambda - \frac { k } { s } + \Delta q _ { 0 } \ge 0$ . Therefore, we conclude $\begin{array} { r } { \frac { \partial \Pi _ { B } ^ { * } } { \partial k } \leq 0 } \end{array}$

c. The first order derivatives of the optimal release time $( \tau _ { B } ^ { * } )$ with respect to ߣ is

$$
\frac {\partial \tau_ {B} ^ {*}}{\partial \lambda} = - \frac {\Delta q _ {0}}{2 \lambda^ {2}} + \frac {k}{2 s \lambda^ {2}}
$$

$\begin{array} { r } { \mathrm { I f } k > s \varDelta q _ { 0 } , \frac { \partial \tau _ { B } ^ { * } } { \partial \lambda } } \end{array}$ is positive; otherwise $( k \leq s \varDelta q _ { 0 } , )$ (, it is negative.

Based on the Envelope Theorem, from $\Pi _ { B } ^ { * } = s [ q _ { B 0 } + \lambda \tau _ { B } ^ { * } - q _ { A } ] ( D - \tau _ { B } ^ { * } ) - k \tau _ { B } ^ { * }$ , we have $\begin{array} { r } { \frac { \partial \Pi _ { B } ^ { * } } { \partial \lambda } = s \tau _ { B } ^ { * } ( D - \tau _ { B } ^ { * } ) } \end{array}$ , in which $\tau _ { B } ^ { * } = \frac { D } { 2 } +$ $\frac { \Delta q _ { 0 } } { 2 \lambda } - \frac { k } { 2 \lambda s }$ is smaller than ܦ. Hence, $\frac { \partial \Pi _ { B } ^ { * } } { \partial \lambda } > 0$ holds.

When $k \leq s \varDelta q _ { 0 } .$ , the monopoly stage becomes shorter as ߣ increases. Therefore, Vendor A’s profit in the monopoly stage declines. However, its profit obtained in the duopoly stage increases because $\begin{array} { r } { \frac { \partial \Pi _ { A } ^ { D * } } { \partial \lambda } = r \left[ \left( \frac { D } { 2 } - \frac { A q _ { 0 } } { 2 \lambda } \right) ^ { 2 } - \frac { k ^ { 2 } } { 4 \lambda ^ { 2 } s ^ { 2 } } \right] + r \lambda \left[ \left( \frac { D } { 2 } - \frac { A q _ { 0 } } { 2 \lambda } \right) \frac { A q _ { 0 } } { \lambda ^ { 2 } } + \frac { k ^ { 2 } } { 2 \lambda ^ { 3 } s ^ { 2 } } \right] > } \end{array}$ 0.

When $k > s \varDelta q _ { 0 }$ , as ߣ increases, the monopoly stage becomes longer, and Vendor A’s profit in the monopoly stage increases, i.e., $\frac { \partial \Pi _ { A } ^ { M * } } { \partial \lambda } > 0$ . In addition, $\begin{array} { r } { \frac { \partial \Pi _ { A } ^ { D * } } { \partial \lambda } = r \left[ \left( \frac { D } { 2 } - \frac { \Delta q _ { 0 } } { 2 \lambda } \right) ^ { 2 } - \frac { k ^ { 2 } } { 4 \lambda ^ { 2 } s ^ { 2 } } \right] + r \lambda \left[ \left( \frac { D } { 2 } - \frac { \Delta q _ { 0 } } { 2 \lambda } \right) \frac { A q _ { 0 } } { \lambda ^ { 2 } } + \frac { 2 k ^ { 2 } } { 4 \lambda ^ { 3 } s ^ { 2 } } \right] > 0 } \end{array}$ still holds. Therefore, the total profit of Vendor A increases with ߣ, i.e., $\frac { \partial \Pi _ { A } ^ { * } } { \partial \lambda } > 0$

d. It is obvious that $\begin{array} { r } { \frac { \partial \tau _ { B } ^ { * } } { \partial q _ { B 0 } } = - \frac { 1 } { 2 \lambda } < 0 \mathrm { ~ a n d } \frac { \partial \Pi _ { B } ^ { * } } { \partial q _ { B 0 } } = \frac { D s } { 2 } - \frac { s \Delta q _ { 0 } } { 2 \lambda } + \frac { k } { 2 \lambda } > 0 } \end{array}$ because $\begin{array} { r } { \Delta q _ { 0 } \le D \lambda - \frac { k } { s } . } \end{array}$ The profit of Vendor A in the monopoly stage is $\Pi _ { A } ^ { M } = \pi _ { A } ^ { M } \tau _ { B } ^ { * }$ . With a larger $q _ { B 0 } ,$ Vendor B releases its products earlier, indicating that Vendor A has a shorter monopoly stage; thus, its profit in the monopoly stage decreases, i.e. $\frac { \partial \Pi _ { A } ^ { M * } } { \partial q _ { B 0 } } < 0$ . Furthermore, the first order derivatives of $\Pi _ { A } ^ { D * }$ with respect to ݍ <sub>଴஻</sub> is $\frac { \partial \Pi _ { A } ^ { D * } } { \partial q _ { B 0 } } = \frac { r } { 2 } \biggl ( D - \frac { \Delta q _ { 0 } } { \lambda } \biggr )$ . Because $\Delta q _ { 0 } < D \lambda - \frac { k } { s } ,$ we have $\frac { \partial \Pi _ { A } ^ { D * } } { \partial q _ { B 0 } } > 0$ □□

## 8 Proof of Lemma 2

From the equilibrium outcomes (8) and (9), if $\tau _ { B } \in \left[ \underline { { \tau } } _ { 1 } , \tau _ { E } \right]$ , Vendor B’s profit rate is zero; thus it is not profitable for Vendor B to release its product in this zero-profit region. If Vendor B releases its product in its winner-take-all region $( \tau _ { E } , \overline { { \tau } } _ { 1 } )$ , the demand of Vendor A drops to zero, i.e., product A is driven out of market. Because $\begin{array} { r } { \frac { \partial \tau _ { E } } { \partial \gamma _ { H } } = 0 , \frac { \partial \overline { { \tau } } _ { 1 } } { \partial \gamma _ { H } } > 0 } \end{array}$ , and $\begin{array} { r } { \frac { \partial \underline { { \tau } } _ { 1 } } { \partial \gamma _ { H } } < 0 } \end{array}$ , both regions expand as $\gamma _ { H }$ increase. Similarly, the two regions expand as $\gamma _ { L }$ increases $\begin{array} { r } { ( \frac { \partial \tau _ { E } } { \partial \gamma _ { L } } = 0 , \frac { \partial \overline { { \tau } } _ { 1 } } { \partial \gamma _ { L } } > 0 , \mathrm { a n d } \frac { \partial \underline { { \tau } } _ { 1 } } { \partial \gamma _ { L } } < 0 ) } \end{array}$ ). □□

## 9 Equilibrium Prices and Demands Corresponding to Different Release Strategies

a. When Vendor B adopts the instant-release strategy,

$$
\left\{ \begin{array}{l} p _ {A} ^ {D *} = \frac {(2 - \theta_ {0}) \Delta q _ {0} - (1 - \theta_ {0}) (2 \gamma_ {B} + \gamma_ {A})}{3} \\ p _ {B} ^ {D *} = \frac {(1 - 2 \theta_ {0}) \Delta q _ {0} - (1 - \theta_ {0}) (\gamma_ {B} + 2 \gamma_ {A})}{3} \end{array} \right.\tag{A3}
$$

$$
\left\{ \begin{array}{l} Q _ {A} ^ {D *} = \frac {1}{3} \frac {(2 - \theta_ {0}) \Delta q _ {0} - (1 - \theta_ {0}) (2 \gamma_ {B} + \gamma_ {A})}{\Delta q _ {0} - \gamma_ {B} - \gamma_ {A}} \\ Q _ {B} ^ {D *} = \frac {1}{3} \frac {(1 - 2 \theta_ {0}) \Delta q _ {0} - (1 - \theta_ {0}) (\gamma_ {B} + 2 \gamma_ {A})}{\Delta q _ {0} - \gamma_ {B} - \gamma_ {A}} \end{array} \right.\tag{A4}
$$

b. When Vendor B adopts the late-release strategy and $\tau _ { B } ^ { * } \in \left( \tau _ { E } , \overline { { \tau } } _ { 1 } \right)$ 2

$$
\left\{ \begin{array}{c} p _ {A} ^ {D *} = 0 \\ p _ {B} ^ {D *} = \theta_ {0} (\lambda \tau_ {B} ^ {*} - \Delta q _ {0}) + \gamma_ {B} (1 - \theta_ {0}) \end{array} \right.\tag{A5}
$$

$$
\left\{ \begin{array}{l l} Q _ {A} ^ {D *} = 0 \\ Q _ {B} ^ {D *} = 1 - \theta_ {0} \end{array} \right.\tag{A6}
$$

c. When Vendor B adopts the late-release strategy and $\tau _ { B } ^ { * } \in [ \overline { { \tau } } _ { 1 } , D ]$ 2

$$
\left\{ \begin{array}{l} p _ {A} ^ {D *} = \frac {(1 - 2 \theta_ {0}) (\lambda \tau_ {B} ^ {*} - \Delta q _ {0}) - (1 - \theta_ {0}) (\gamma_ {A} + 2 \gamma_ {B})}{3} \\ p _ {B} ^ {D *} = \frac {(2 - \theta_ {0}) (\lambda \tau_ {B} ^ {*} - \Delta q _ {0}) - (1 - \theta_ {0}) (2 \gamma_ {A} + \gamma_ {B})}{3} \end{array} \right.\tag{A7}
$$

$$
\left\{ \begin{array}{l} Q _ {A} ^ {D *} = \frac {1}{3} \frac {(1 - 2 \theta_ {0}) (\lambda \tau_ {B} ^ {*} - \Delta q _ {0}) - (1 - \theta_ {0}) (\gamma_ {A} + 2 \gamma_ {B})}{\lambda \tau_ {B} ^ {*} - \Delta q _ {0} - \gamma_ {A} - \gamma_ {B}} \\ Q _ {B} ^ {D *} = \frac {1}{3} \frac {(2 - \theta_ {0}) (\lambda \tau_ {B} ^ {*} - \Delta q _ {0}) - (1 - \theta_ {0}) (2 \gamma_ {A} + \gamma_ {B})}{\lambda \tau_ {B} ^ {*} - \Delta q _ {0} - \gamma_ {A} - \gamma_ {B}} \end{array} \right.\tag{A8}
$$

□□

## 10 Proof of Proposition 2

From equilibrium solutions (8) and (9), if Vendor B adopts the instant-release strategy, its optimal price, demand, and profit are given by

$$
\left\{ \begin{array}{l l} p _ {B} ^ {D *} = \frac {(1 - 2 \theta_ {0}) \Delta q _ {0} - (1 - \theta_ {0}) (\gamma_ {B} + 2 \gamma_ {A})}{3} \\ Q _ {B} ^ {D *} = \frac {1}{3} \frac {(1 - 2 \theta_ {0}) \Delta q _ {0} - (1 - \theta_ {0}) (\gamma_ {B} + 2 \gamma_ {A})}{\Delta q _ {0} - \gamma_ {B} - \gamma_ {A}} \\ \Pi_ {B} ^ {*} = \frac {1}{9} \frac {[ (1 - 2 \theta_ {0}) \Delta q _ {0} - (1 - \theta_ {0}) (\gamma_ {B} + 2 \gamma_ {A}) ] ^ {2}}{\Delta q _ {0} - \gamma_ {B} - \gamma_ {A}} D \end{array} \right.
$$

Then, we have $\begin{array} { r } { \frac { \partial \Pi _ { B } ^ { * } } { \partial \Delta q _ { 0 } } > 0 . } \end{array}$ , because $\frac { \partial p _ { B } ^ { D * } } { \partial \Delta q _ { 0 } } > 0$ and $\frac { \partial Q _ { B } ^ { D * } } { \partial \Delta q _ { 0 } } > 0$

When Vendor B releases its products at $\hat { \tau } \left( \hat { \tau } > \tau _ { E } \right)$ 2

a. $\mathrm { I f } \hat { \tau } \in \left( \tau _ { E } , \overline { { \tau } } _ { 1 } \right)$ , the profit of Vendor B is given by

$$
\Pi_ {B} = [ \theta_ {0} (\lambda \hat {\tau} - \Delta q _ {0}) (1 - \theta_ {0}) + \gamma_ {B} (1 - \theta_ {0}) ^ {2} ] (D - \hat {\tau}) - k \hat {\tau}
$$

which decreases with $\varDelta q _ { 0 }$

b. If $\hat { \tau } \in [ \overline { { \tau } } _ { 1 } , D ]$ [, the profit of Vendor B is given by

$$
\Pi_ {B} = \frac {1}{9} \frac {[ (2 - \theta_ {0}) (\lambda \hat {\tau} - \Delta q _ {0}) - (1 - \theta_ {0}) (2 \gamma_ {A} + \gamma_ {B}) ] ^ {2}}{\lambda \hat {\tau} - \Delta q _ {0} - \gamma_ {A} - \gamma_ {B}} (D - \hat {\tau}) - k \hat {\tau}
$$

Then, we have

$$
\frac {\partial \Pi_ {B}}{\partial \Delta q _ {0}} = \frac {(D - \hat {\tau}) [ (2 - \theta_ {0}) (\lambda \hat {\tau} - \Delta q _ {0}) - (1 - \theta_ {0}) (2 \gamma_ {A} + \gamma_ {B}) ]}{9} \frac {2 \gamma_ {A} + (3 - \theta_ {0}) \gamma_ {B} - (2 - \theta_ {0}) (\lambda \hat {\tau} - \Delta q _ {0})}{(\lambda \hat {\tau} - \Delta q _ {0} - \gamma_ {A} - \gamma_ {B}) ^ {2}}
$$

$\hat { \tau } \geq \overline { { \tau } } _ { 1 }$ yields $2 \gamma _ { A } + ( 3 - \theta _ { 0 } ) \gamma _ { B } - ( 2 - \theta _ { 0 } ) ( \lambda \hat { \tau } - \Delta q _ { 0 } ) \leq 0$ . Thus, we have $\begin{array} { r } { \frac { \partial \Pi _ { B } } { \partial \Delta q _ { 0 } } \leq 0 } \end{array}$ , implying that Vendor B’s profit decreases with $\Delta { { q } _ { 0 } }$

Therefore, when Vendor B releases its products after $\tau _ { E } .$ , its profit curve will move downwards as the initial quality gap $\Delta { q } _ { 0 }$ becomes larger. Hence, Vendor B’s maximal profit obtained by releasing products in $[ \overline { { \tau } } _ { 1 } , D ]$ decreases with $\Delta q _ { 0 }$

Vendor B’s profit obtained from the instant-release strategy increases with $\begin{array} { r } { \varDelta q _ { 0 } , } \end{array}$ , while that obtained from the late-release strategy decreases with it. Therefore, there exists a threshold value $\varDelta \bar { q } _ { 0 }$ for the initial quality gap, under which the late-release strategy is more profitable than the instant-release strategy.

Vendor B’s profit maximization problem is, therefore,

$$
\max _ {\tau_ {B}} \Pi_ {B} = \left\{ \begin{array}{c} \frac {1}{9} \frac {[ (1 - 2 \theta_ {0}) (q _ {A 0} - q _ {B 0} - \lambda \tau_ {B}) - (1 - \theta_ {0}) (\gamma_ {B} + 2 \gamma_ {A}) ] ^ {2}}{q _ {A 0} - q _ {B 0} - \lambda \tau_ {B} - \gamma_ {B} - \gamma_ {A}} (D - \tau_ {B}) - k \tau_ {B}, \tau_ {B} <   \underline {{\tau}} _ {1} \\ [ \theta_ {0} (q _ {B 0} + \lambda \tau_ {B} - q _ {A 0}) (1 - \theta_ {0}) + \gamma_ {B} (1 - \theta_ {0}) ^ {2} ] (D - \tau_ {B}) - k \tau_ {B}, \tau_ {E} <   \tau_ {B} <   \overline {{\tau}} _ {1} \\ \frac {1}{9} \frac {[ (2 - \theta_ {0}) (q _ {B 0} + \lambda \tau_ {B} - q _ {A 0}) - (1 - \theta_ {0}) (2 \gamma_ {A} + \gamma_ {B}) ] ^ {2}}{q _ {B 0} + \lambda \tau_ {B} - q _ {A 0} - \gamma_ {A} - \gamma_ {B}} (D - \tau_ {B}) - k \tau_ {B}, \overline {{\tau}} _ {1} \leq \tau_ {B} \leq D \end{array} \right.\tag{12}
$$

$$
\mathrm{s.t.} \tau_ {B} \in \left[ 0, \underline {{\tau}} _ {1}\right) \cup (\tau_ {E}, D ]
$$

When $\tau _ { B } \in [ \overline { { \tau } } _ { 1 } , D ]$ [, it is intractable to obtain the locally optimal release time in this interval. When $k = 0$ , the only root o $\mathrm { f } \frac { \partial \Pi _ { B } } { \partial \tau _ { B } } = 0 \mathrm { i n } [ \overline { { \tau } } _ { 1 } , D ]$ takes the form,

$$
\tau_ {d 2} = \frac {D}{4} + \frac {3 (\Delta q _ {0} + \gamma_ {A} + \gamma_ {B})}{4 \lambda} + \frac {\sqrt {(D \lambda - \Delta q _ {0} - \gamma_ {A} - \gamma_ {B}) [ D \lambda - \Delta q _ {0} - \gamma_ {A} - \gamma_ {B} + x ]}}{4 \lambda}
$$

where $\begin{array} { r } { x = \frac { 8 ( 1 - \theta _ { 0 } ) } { 2 - \theta _ { 0 } } ( 2 \gamma _ { A } + \gamma _ { B } ) - 8 \gamma _ { A } - 8 \gamma _ { B } } \end{array}$

Hence, when $k = 0$ , in time interval $[ \overline { { \tau } } _ { 1 } , D ] , \overline { { \tau } } _ { 1 }$ and $\tau _ { d 2 }$ are the only two possible optimal solutions for Vendor B. Furthermore, we have $\begin{array} { r } { \frac { \partial \Pi _ { B } } { \partial k } < 0 ; } \end{array}$ based on the envelop theorem, the locally optimal release time of Vendor B in $[ \overline { { \tau } } _ { 1 } , D ]$ [ decreases with $\begin{array} { r } { k , \mathrm { i } . \mathrm { e } . , \frac { \partial \tau _ { B } ^ { * } } { \partial k } < 0 } \end{array}$

Therefore, we conclude that when adopting the late-release strategy, Vendor B should not release its product later than time $\overline { { \tau } } _ { 1 }$ or time $\tau _ { d 2 }$ whichever occurs later. That is, $\tau _ { B } ^ { * } < \operatorname* { m a x } \{ \overline { { \tau } } _ { 1 } , \tau _ { d 2 } \}$ □□

## 11 Proof of Corollary 4

From Proposition 2, Vendor B cannot release its products later than time $\overline { { \tau } } _ { 1 }$ or time $\tau _ { d 2 }$ , whichever occurs later. Thus, if a Type I late-release strategy is adopted, $\tau _ { d 2 }$ must be larger than $\overline { { \tau } } _ { 1 }$ and the optimal release time must fall within $[ \overline { { \tau } } _ { 1 } , \tau _ { d 2 } )$ . In addition, Lemma 2 indicates that, when product B is released after $\overline { { \tau } } _ { 1 } ,$ products A and B coexist in the market and serve the low-end and the high-end markets, respectively. Regarding Type II late release strategy, Lemma 2 proves that when product B is released in the winner-take-all time interval $( \tau _ { E } , \overline { { \tau } } _ { 1 } )$ , product A will be driven out of the market. □□

## 12 Proof of Lemma 3

As shown in Table $^ { 2 , }$ when Vendor B adopts the instant-release strategy, its product quality is lower than Vendor $\mathrm { \bf A } \ ' \mathrm { \bf s . }$ Thus, Vendor B’s profit rate decreases with $\gamma _ { H }$ or $\gamma _ { L }$ . Hence, Vendor B’s total profit also decreases with the level of incompatibility.

When Vendor B adopts the late-release strategy, and the optimal release time falls within $( \tau _ { E } , \overline { { \tau } } _ { 1 } )$ , we have

$$
\Pi_ {B} (\tau_ {B}) = [ \theta_ {0} (q _ {B 0} + \lambda \tau_ {B} - q _ {A 0}) (1 - \theta_ {0}) + \gamma_ {B} (1 - \theta_ {0}) ^ {2} ] (D - \tau_ {B}) - k \tau_ {B}
$$

Obviously, Vendor B’s profit curve moves upward as $\gamma _ { B }$ becomes larger and its maximal profit increases with $\gamma _ { B }$

When Vendor B adopts the late-release strategy, and the optimal release time falls within $[ \overline { { \tau } } _ { 1 } , D ]$ [, Vendor B’s profit is

$$
\Pi_ {B} (\tau_ {B}) = \frac {1}{9} \frac {[ (2 - \theta_ {0}) (q _ {B 0} + \lambda \tau_ {B} - q _ {A 0}) - (1 - \theta_ {0}) (2 \gamma_ {A} + \gamma_ {B}) ] ^ {2}}{q _ {B 0} + \lambda \tau_ {B} - q _ {A 0} - \gamma_ {A} - \gamma_ {B}} (D - \tau_ {B}) - k \tau_ {B}
$$

Thus, for a given $\tau _ { B } .$ , we have $\begin{array} { r } { \frac { \partial \Pi _ { B } ( \tau _ { B } ) } { \partial \gamma _ { A } } < 0 } \end{array}$ and $\frac { \partial \Pi _ { B } ( \tau _ { B } ) } { \partial \gamma _ { B } } > 0$ . Therefore, when releasing its product in $[ \overline { { \tau } } _ { 1 } , D ]$ [, Vendor B’s maximal profit increases with $\gamma _ { B }$ , while decreases with $\gamma _ { A }$ □□

## 13 Equilibrium with Switching Cost Considered

## Case I

In this case, the vendors’ objectives are to maximize their respective profit rates:

$$
\begin{array}{l} \left\{ \begin{array}{l} \max _ {p _ {A} ^ {D}} \pi_ {A} ^ {D} = p _ {A} ^ {D} \big (\hat {\theta} - \theta_ {0} \big) \\ \max _ {p _ {B} ^ {D}} \pi_ {B} ^ {D} = p _ {B} ^ {D} \big (1 - \hat {\theta} \big) \end{array} \right. \\ \text {s.t.} \theta_ {0} \leq \hat {\theta} ^ {M} \leq \hat {\theta} ^ {D} \leq \hat {\theta} \leq 1 \end{array}\tag{A9}
$$

Based on the fulfilled expectation equilibrium, solving (A9) yields the following equilibrium solution:

$$
\left\{ \begin{array}{l} p _ {A} ^ {D *} = \frac {(1 - 2 \theta_ {0}) (q _ {B} (\tau_ {B}) - q _ {A} (\tau_ {B})) - (1 - \theta_ {0}) (\gamma_ {A} + 2 \gamma_ {B}) + \frac {c _ {S}}{D - \tau_ {B}}}{3} \\ p _ {B} ^ {D *} = \frac {(2 - \theta_ {0}) (q _ {B} (\tau_ {B}) - q _ {A} (\tau_ {B})) - (1 - \theta_ {0}) (2 \gamma_ {A} + \gamma_ {B}) - \frac {c _ {S}}{D - \tau_ {B}}}{3} \end{array} \right.\tag{A10.1}
$$

$$
\left\{ \begin{array}{l} \widehat {\theta} ^ {*} = \frac {1}{3} \frac {(1 + \theta_ {0}) (q _ {B} (\tau_ {B}) - q _ {A} (\tau_ {B})) - (1 + 2 \theta_ {0}) \gamma_ {A} - (\theta_ {0} + 2) \gamma_ {B} + \frac {c _ {S}}{D - \tau_ {B}}}{q _ {B} (\tau_ {B}) - q _ {A} (\tau_ {B}) - \gamma_ {A} - \gamma_ {B}} \\ Q _ {A} ^ {D *} = \frac {1}{3} \frac {(1 - 2 \theta_ {0}) (q _ {B} (\tau_ {B}) - q _ {A} (\tau_ {B})) - (1 - \theta_ {0}) (\gamma_ {A} + 2 \gamma_ {B}) + \frac {c _ {S}}{D - \tau_ {B}}}{q _ {B} (\tau_ {B}) - q _ {A} (\tau_ {B}) - \gamma_ {A} - \gamma_ {B}} \\ Q _ {B} ^ {D *} = \frac {1}{3} \frac {(2 - \theta_ {0}) (q _ {B} (\tau_ {B}) - q _ {A} (\tau_ {B})) - (1 - \theta_ {0}) (2 \gamma_ {A} + \gamma_ {B}) - \frac {c _ {S}}{D - \tau_ {B}}}{q _ {B} (\tau_ {B}) - q _ {A} (\tau_ {B}) - \gamma_ {A} - \gamma_ {B}} \end{array} \right.\tag{A10.2}
$$

$$
\left\{ \begin{array}{l} \Pi_ {A} ^ {D *} = \frac {1}{9} \frac {\left[ (1 - 2 \theta_ {0}) (q _ {B} (\tau_ {B}) - q _ {A} (\tau_ {B})) - (1 - \theta_ {0}) (\gamma_ {A} + 2 \gamma_ {B}) + \frac {c _ {S}}{D - \tau_ {B}} \right] ^ {2}}{q _ {B} (\tau_ {B}) - q _ {A} (\tau_ {B}) - \gamma_ {A} - \gamma_ {B}} \\ \Pi_ {B} ^ {D *} = \frac {1}{9} \frac {\left[ (2 - \theta_ {0}) (q _ {B} (\tau_ {B}) - q _ {A} (\tau_ {B})) - (1 - \theta_ {0}) (2 \gamma_ {A} + \gamma_ {B}) - \frac {c _ {S}}{D - \tau_ {B}} \right] ^ {2}}{q _ {B} (\tau_ {B}) - q _ {A} (\tau_ {B}) - \gamma_ {A} - \gamma_ {B}} \end{array} \right.\tag{A10.3}
$$

This equilibrium holds when $\theta _ { 0 } \leq \hat { \theta } ^ { M } \leq \hat { \theta } ^ { D * } \leq \hat { \theta } ^ { * } < 1$

## Case II

In this case, the profit-maximization problem is

$$
\left\{ \begin{array}{l} \max _ {p _ {A} ^ {D}} \pi_ {A} ^ {D} = p _ {A} ^ {D} \big (\hat {\theta} - \hat {\theta} ^ {M} + \hat {\theta} ^ {D} - \theta_ {0} \big) \\ \max _ {p _ {B} ^ {D}} \pi_ {B} ^ {D} = p _ {B} ^ {D} \big (1 - \hat {\theta} + \hat {\theta} ^ {M} - \hat {\theta} ^ {D} \big) \\ \text {s.t.} \theta_ {0} \leq \hat {\theta} ^ {D} \leq \hat {\theta} ^ {M} <   \hat {\theta} \leq 1 \end{array} \right.\tag{A11}
$$

The corresponding equilibrium prices and profit rates are

$$
\left\{ \begin{array}{l} p _ {A} ^ {D *} = \frac {(1 - 2 \theta_ {0} - \widehat {\theta} ^ {M}) (q _ {B} - q _ {A}) - 2 (1 - \theta_ {0}) (\gamma_ {A} + 2 \gamma_ {B}) + \frac {c _ {S}}{D - \tau_ {B}}}{6} \\ p _ {B} ^ {D *} = \frac {(2 - \theta_ {0} + \widehat {\theta} ^ {M}) (q _ {B} - q _ {A}) - 2 (1 - \theta_ {0}) (2 \gamma_ {A} + \gamma_ {B}) - \frac {c _ {S}}{D - \tau_ {B}}}{6} \end{array} \right.\tag{A12.1}
$$

$$
\left\{ \begin{array}{l} Q _ {A} ^ {D *} = \frac {(1 - 2 \theta_ {0} - \widehat {\theta} ^ {M}) (q _ {B} - q _ {A}) - 2 (1 - \theta_ {0}) (\gamma_ {A} + 2 \gamma_ {B}) + \frac {c _ {S}}{D - \tau_ {B}}}{3 (q _ {B} - q _ {A} - 2 \gamma_ {A} - 2 \gamma_ {B})} \\ Q _ {B} ^ {D *} = \frac {(2 - \theta_ {0} + \widehat {\theta} ^ {M}) (q _ {B} - q _ {A}) - 2 (1 - \theta_ {0}) (2 \gamma_ {A} + \gamma_ {B}) - \frac {c _ {S}}{D - \tau_ {B}}}{3 (q _ {B} - q _ {A} - 2 \gamma_ {A} - 2 \gamma_ {B})} \end{array} \right.\tag{A12.2}
$$

$$
\left\{ \begin{array}{l} \Pi_ {A} ^ {D *} = \frac {1}{1 8} \frac {\left[ (1 - 2 \theta_ {0} - \widehat {\theta} ^ {M}) (q _ {B} - q _ {A}) - 2 (1 - \theta_ {0}) (\gamma_ {A} + 2 \gamma_ {B}) + \frac {c _ {S}}{D - \tau_ {B}} \right] ^ {2}}{3 (q _ {B} - q _ {A} - 2 \gamma_ {A} - 2 \gamma_ {B})} \\ \Pi_ {B} ^ {D *} = \frac {1}{1 8} \frac {\left[ (2 - \theta_ {0} + \widehat {\theta} ^ {M}) (q _ {B} - q _ {A}) - 2 (1 - \theta_ {0}) (2 \gamma_ {A} + \gamma_ {B}) - \frac {c _ {S}}{D - \tau_ {B}} \right] ^ {2}}{3 (q _ {B} - q _ {A} - 2 \gamma_ {A} - 2 \gamma_ {B})} \end{array} \right.\tag{A12.3}
$$

This equilibrium holds when $p _ { A } ^ { D * } \geq 0 , p _ { B } ^ { D * } \geq 0 , Q _ { A } ^ { D * } \geq 0$ , and $Q _ { B } ^ { D * } \geq 0$

## Case III

The two vendors’ objectives are to maximize their respective profit rates:

$$
\left\{ \begin{array}{l} \max _ {p _ {A} ^ {D}} \pi_ {A} ^ {D} = p _ {A} ^ {D} \big (1 - \hat {\theta} \big) \\ \max _ {p _ {B} ^ {D}} \pi_ {B} ^ {D} = p _ {B} ^ {D} \big (\hat {\theta} - \theta_ {0} \big) \\ \text {s.t.} \theta_ {0} \leq \hat {\theta} ^ {M} <   \hat {\theta} \leq 1 \end{array} \right.\tag{A13}
$$

The equilibrium prices and profit rates take the following forms:

$$
\left\{ \begin{array}{l} p _ {A} ^ {D *} = \frac {(2 - \theta_ {0}) (q _ {A} - q _ {B}) - (1 - \theta_ {0}) (\gamma_ {A} + 2 \gamma_ {B}) + \frac {c _ {S}}{D - \tau_ {B}}}{3} \\ p _ {B} ^ {D *} = \frac {(1 - 2 \theta_ {0}) (q _ {A} - q _ {B}) - (1 - \theta_ {0}) (2 \gamma_ {A} + \gamma_ {B}) - \frac {c _ {S}}{D - \tau_ {B}}}{3} \end{array} \right.\tag{A14.1}
$$

$$
\left\{ \begin{array}{l} \widehat {\theta} ^ {*} = \frac {1}{3} \frac {(1 + \theta_ {0}) (q _ {A} - q _ {B}) - (1 + 2 \theta_ {0}) \gamma_ {B} - (\theta_ {0} + 2) \gamma_ {A} - \frac {c _ {S}}{D - \tau_ {B}}}{q _ {A} - q _ {B} - \gamma_ {A} - \gamma_ {B}} \\ Q _ {A} ^ {D *} = \frac {1}{3} \frac {(2 - \theta_ {0}) (q _ {A} - q _ {B}) - (1 - \theta_ {0}) (\gamma_ {A} + 2 \gamma_ {B}) + \frac {c _ {S}}{D - \tau_ {B}}}{q _ {A} - q _ {B} - \gamma_ {A} - \gamma_ {B}} \\ Q _ {B} ^ {D *} = \frac {1}{3} \frac {(1 - 2 \theta_ {0}) (q _ {A} - q _ {B}) - (1 - \theta_ {0}) (2 \gamma_ {A} + \gamma_ {B}) - \frac {c _ {S}}{D - \tau_ {B}}}{q _ {A} - q _ {B} - \gamma_ {A} - \gamma_ {B}} \end{array} \right.\tag{A14.2}
$$

$$
\left\{ \begin{array}{l l} \Pi_ {A} ^ {D *} = \frac {1}{9} \frac {\left[ (2 - \theta_ {0}) (q _ {A} - q _ {B}) - (1 - \theta_ {0}) (\gamma_ {A} + 2 \gamma_ {B}) + \frac {c _ {S}}{D - \tau_ {B}} \right] ^ {2}}{q _ {A} - q _ {B} - \gamma_ {A} - \gamma_ {B}} \\ \Pi_ {B} ^ {D *} = \frac {1}{9} \frac {\left[ (1 - 2 \theta_ {0}) (q _ {A} - q _ {B}) - (1 - \theta_ {0}) (2 \gamma_ {A} + \gamma_ {B}) - \frac {c _ {S}}{D - \tau_ {B}} \right] ^ {2}}{q _ {A} - q _ {B} - \gamma_ {A} - \gamma_ {B}} \end{array} \right.\tag{A14.3}
$$

The above equilibrium holds when $\theta _ { 0 } \leq \hat { \theta } ^ { M } < \hat { \theta } ^ { * } \leq 1$

□□

## 14 Model Extension II: A Model with Quadratic Cost Function

In this subsection, we analyze the case in which marginal development cost is a quadratic function of development time:

$$
c = k \tau_ {B} ^ {2}\tag{A15}
$$

We find that under this new quadratic cost function, the equilibrium prices, demands, and profit rates shown in (8) and (9) remain valid.

In the full-compatibility scenario, the optimal release time for Vendor B can be derived by

$$
\max _ {\tau_ {B}} \Pi_ {B} = \left\{ \begin{array}{l} r (\Delta q _ {0} - \lambda \tau_ {B}) (D - \tau_ {B}) - k \tau_ {B} ^ {2}, \tau_ {B} \leq \tau_ {E} \\ s (\lambda \tau_ {B} - \Delta q _ {0}) (D - \tau_ {B}) - k \tau_ {B} ^ {2}, \tau_ {B} > \tau_ {E} \end{array} \right.\tag{A16}
$$

where $\begin{array} { r } { \tau _ { E } = \frac { \Delta q _ { 0 } } { \lambda } } \end{array}$ . By solving (A16), we have two local optima: $\tau _ { B } = 0$ and $\begin{array} { r } { \tau _ { B } = \frac { D \lambda s + \varDelta q _ { 0 } s } { 2 \lambda s + 2 k } } \end{array}$ , corresponding to instant-release and late-release strategies, respectively. Proposition 1still holds under a quadratic cost function, but the threshold value takes a different form:

$$
\Delta \overline {{q}} _ {0} ^ {\prime} = \min \left\{D \lambda + \frac {2 D}{s} [ k (r + s) + \lambda r s - (k + \lambda s) h ], \frac {D \lambda^ {2} s}{\lambda s + 2 k} \right\}
$$

where $\begin{array} { r } { h = \sqrt { \frac { ( k + \lambda s ) r ^ { 2 } + ( k + \lambda r ) s ^ { 2 } + 2 k r s } { k + \lambda s } } . } \end{array}$

If the initial quality gap is larger than $\Delta \overline { { q } } _ { 0 } ^ { \prime } .$ , Vendor B should release its products immediately; otherwise, the late-release strategy is preferred.

In the partial-compatibility scenario, Vendor $\mathrm { B } \ ' \mathrm { s }$ profit maximization problem is,

$$
\max _ {\tau_ {B}} \Pi_ {B} = \left\{ \begin{array}{c} \frac {1}{9} \frac {[ (1 - 2 \theta_ {0}) (q _ {A 0} - q _ {B 0} - \lambda \tau_ {B}) - (1 - \theta_ {0}) (\gamma_ {B} + 2 \gamma_ {A}) ] ^ {2}}{q _ {A 0} - q _ {B 0} - \lambda \tau_ {B} - \gamma_ {B} - \gamma_ {A}} (D - \tau_ {B}) - k \tau_ {B} ^ {2}, \tau_ {B} <   \underline {{\tau}} _ {1} \\ [ \theta_ {0} (q _ {B 0} + \lambda \tau_ {B} - q _ {A 0}) (1 - \theta_ {0}) + \gamma_ {B} (1 - \theta_ {0}) ^ {2} ] (D - \tau_ {B}) - k \tau_ {B} ^ {2}, \tau_ {E} <   \tau_ {B} <   \overline {{\tau}} _ {1} \\ \frac {1}{9} \frac {[ (2 - \theta_ {0}) (q _ {B 0} + \lambda \tau_ {B} - q _ {A 0}) - (1 - \theta_ {0}) (2 \gamma_ {A} + \gamma_ {B}) ] ^ {2}}{q _ {B 0} + \lambda \tau_ {B} - q _ {A 0} - \gamma_ {A} - \gamma_ {B}} (D - \tau_ {B}) - k \tau_ {B} ^ {2}, \overline {{\tau}} _ {1} \leq \tau_ {B} \leq D \\ \text {s.t.} \tau_ {B} \in [ 0, \underline {{\tau}} _ {1}) \cup (\tau_ {E}, D ] \end{array} \right.\tag{A17}
$$

As shown in Figure A1, the result in the partial-compatibility scenario still holds when the quadratic cost function is adopted.

![](/api/attachments/TRJXGV8F/fulltext/images/b17a179650f9a6606d22e95ee563bc310e545fe015bc7e839cdb7c2168aac788.jpg)  
(a) Optimal Market Entry Strategy

![](/api/attachments/TRJXGV8F/fulltext/images/54b89502531e4ace43ed72163ed277e98ac77793317254bfca1672bfbc57d09d.jpg)  
(b) Maximal Profit

$$
(D = 2 0, \lambda = 0. 1, q _ {A 0} = 2, \theta_ {0} = 0, \alpha = 0. 5, k = 0. 1, q _ {B 0} = 1. 2 5, \text {and} \gamma_ {A}, \gamma_ {B} \in [ 0, 0. 5 ])
$$

Figure A1. Optimal Market Entry Strategy and Maximal Profit of Vendor B

In summary, our main analytically findings still hold even when a quadratic cost function is adopted.

□□

## 15 Model Extension III: A Model with Unequal Quality Improvement Rates

In this subsection, we investigate the scenario where the two vendors have unequal post-release quality improvement rates. After $\tau _ { B } .$ , the quality levels of product A and B are given by

$$
\left\{ \begin{array}{c} q _ {A} (\tau) = q _ {A 0} + \lambda_ {2 A} \tau , \tau \in [ 0, D ] \\ q _ {B} (\tau) = q _ {B 0} + \lambda_ {1} \tau_ {B} + \lambda_ {2 B} (\tau - \tau_ {B}), \tau \in [ \tau_ {B}, D ] \end{array} \right.\tag{A18}
$$

where $\lambda _ { 2 A }$ and $\lambda _ { 2 B }$ are post-release quality improvement rates of product A and B, respectively. Let ߣ߂ denote the difference between $\lambda _ { 2 A }$ and $\lambda _ { 2 B } , \mathrm { i . e . , } \lambda \lambda = \lambda _ { 2 A } - \lambda _ { 2 B } . \Delta \lambda > 0 ( \Delta \lambda < 0 )$ indicates that, after product $\mathrm { B } ^ { \prime } \mathrm { s }$ release, product A’s quality increases faster (slower) than that of product B.

From the solutions of optimal profit rates, i.e., Equations (8.3) and (9.3), we have the following findings. In the case of unequal post-release quality improvement rates, as the quality gap between the two products in the duopoly stage increases (decreases) over time, the profit rates of both vendors increase (decrease) over time. The explanation for this finding is as follow. A larger quality gap leads to less competition between the two vendors, so both the prices and profit rates for the two products increase. So long as the post-release quality improvement doesn’t change the sign of $\left( q _ { A } ( \tau ) - q _ { B } ( \tau ) \right)$ , another finding follows immediately: If product B has a lower post-release quality improvement rate $( \lambda _ { 2 A } > \lambda _ { 2 B } )$ , the profit rate of Vendor B associated with the instant-release strategy increases over time, whereas its profit rate associated with the late-release strategy decreases over time. On the other hand, if the post-release quality improvement rate of product B is higher $( \lambda _ { 2 A } < \lambda _ { 2 B } )$ , the profit rate of Vendor B associated with the instant-release strategy decreases over time, whereas its profit rate associated with the late-release strategy increases over time.

In Table A1 below, we summarize the changes in quality gap and profit rates of the two vendors when their post-release quality improvement rates are different.

Table A1. Changes in Profit Rates of the Two Vendors

<table><tr><td>Δλ</td><td>Strategy</td><td>Quality Gap (Over time)</td><td>Profit rate of Vendor B (Over time)</td><td>Profit rate of Vendor A (Over time)</td></tr><tr><td rowspan="2">&gt;0</td><td>Instant-Release</td><td>Increase</td><td>Increase</td><td>Increase</td></tr><tr><td>Late-Release</td><td>Decrease</td><td>Decrease</td><td>Decrease</td></tr><tr><td rowspan="2">&lt;0</td><td>Instant-Release</td><td>Decrease</td><td>Decrease</td><td>Decrease</td></tr><tr><td>Late-Release</td><td>Increase</td><td>Increase</td><td>Increase</td></tr></table>

As shown in Table A1, if Vendor B has a lower post-release quality improvement rate than Vendor A, the instant-release strategy is preferred by the new entrant; otherwise, the unequal quality improvement rates improve Vendor B’s profit in the late-release strategy. This result is similar in spirit to Proposition 1. In both cases, the new vendor should adopt the instant-release strategy if it is difficult to compete with the incumbent on product quality, and choose the late-release strategy otherwise. A closer examination of Table A1 reveals that the release strategy preferred by the new entrant is always the one that results in an increasing quality gap over time. This is because a larger quality gap can effectively reduce the competition between the two products.

![](/api/attachments/TRJXGV8F/fulltext/images/04bc14ad9a36cbbf2794d2942e4b4724c9dc9daa1b2ac727acdd312429a24073.jpg)  
(a) Optimal Market Entry Strategy

![](/api/attachments/TRJXGV8F/fulltext/images/8651bd2d5370a6c3ff19e1b445ca9dd5a13497be0a4a138deba66a0453f6a7de.jpg)  
(b) Maximal Profit

$$
(D = 2 0, \lambda_ {1} = 0. 1, q _ {A 0} = 2, q _ {B 0} = 1. 5, \lambda_ {2 A} \in [ 0, 0. 0 5 ], \lambda_ {2 B} \in [ 0, 0. 0 5 ], \theta_ {0} = 0, \alpha = 0. 2, \gamma_ {A} = \gamma_ {B} = 0. 1, k = 0. 1)
$$

Figure A2(a) shows that an increase in $\lambda _ { 2 A }$ may change Vendor B’s optimal strategy from late-release to instant-release, while an increase in $\lambda _ { 2 B }$ has the opposite effect. As shown in Figure A2(b), in the region where the instant-release strategy is optimal, Vendor B attains its highest profit when $\lambda _ { 2 A } = 0 . 0 5$ and $\lambda _ { 2 B } = 0$ . Similarly, when the values of $( \lambda _ { 2 A } , \lambda _ { 2 B } )$ falls within the region where the late-release strategy is optimal, Vendor B attains its highest profit at $( \lambda _ { 2 A } , \lambda _ { 2 B } ) = ( 0 , 0 . 0 5 )$ ). □□

## 16 Model Extension IV: A Model with Partial Market Coverage

In the full-compatibility scenario, to ensure that the market is fully covered, the value of $\theta _ { 0 } ,$ representing the type of customers with the minimum marginal willingness-to-pay, should satisfy

$$
\theta_ {0} q _ {L} - p _ {L} ^ {D *} + \alpha (1 - \theta_ {0}) > 0\tag{A19}
$$

in which L represents the product with lower quality and $\begin{array} { r } { p _ { L } ^ { D * } = \frac { ( 1 - 2 \theta _ { 0 } ) ( q _ { H } - q _ { L } ) } { 3 } } \end{array}$ . From (A19), we have

$$
\alpha > \frac {(1 - 2 \theta_ {0}) q _ {H} - (1 + \theta_ {0}) q _ {L}}{3 (1 - \theta_ {0})}\tag{A20}
$$

Similarly, in the partial-compatibility scenario, when $\begin{array} { r } { ( q _ { H } - q _ { L } ) \ge \frac { 1 - \theta _ { 0 } } { 1 - 2 \theta _ { 0 } } ( \gamma _ { L } + 2 \gamma _ { H } ) , \theta _ { 0 } } \end{array}$ satisfy should

$$
\theta_ {0} q _ {L} - p _ {L} ^ {D *} + \alpha Q _ {L} ^ {D *} + \beta_ {H} Q _ {H} ^ {D *} > 0\tag{A21}
$$

Because $\theta _ { 0 } q _ { L }$ and $\beta _ { H } Q _ { H } ^ { D * }$ are non-negative terms, $\alpha Q _ { L } ^ { D * } > p _ { L } ^ { D * }$ is a sufficient condition for (A21). Substituting $p _ { L } ^ { D * } =$ $\frac { ( 1 - 2 \theta _ { 0 } ) ( q _ { H } - \bar { q _ { L } } ) - ( 1 - \theta _ { 0 } ) ( \gamma _ { L } + 2 \gamma _ { H } ) } { 3 }$ and $\begin{array} { r } { Q _ { L } ^ { D * } = \frac { 1 } { 3 } \frac { ( 1 - 2 \theta _ { 0 } ) ( q _ { H } - q _ { L } ) - ( 1 - \theta _ { 0 } ) ( \gamma _ { L } + 2 \gamma _ { H } ) } { q _ { H } - q _ { L } - \gamma _ { L } - \gamma _ { H } } } \end{array}$ into $\alpha Q _ { L } ^ { D * } > p _ { L } ^ { D * }$ , we have

$$
\alpha > q _ {H} - q _ {L} - \gamma_ {L} - \gamma_ {H}\tag{A22}
$$

When $\begin{array} { r } { ( q _ { H } - q _ { L } ) < \frac { 1 - \theta _ { 0 } } { 1 - 2 \theta _ { 0 } } ( \gamma _ { L } + 2 \gamma _ { H } ) } \end{array}$ , i.e., in the zero-profit region for Vendor L, the full-coverage assumption holds unconditionally because the price of L drops to zero

Therefore, we conclude that when the intensity of network effects is sufficiently high, our assumption that “the value of $\theta _ { 0 }$ is set in such a way that all consumers will purchase either A or B in the duopoly stage” can be satisfied.

<table><tr><td></td><td>No purchase</td><td>L</td><td>H</td></tr><tr><td> $\theta_0$ </td><td> $\hat{\theta}_0$ </td><td> $\hat{\theta}^D$ </td><td>1</td></tr></table>

Figure A3 shows the market segmentation under partial market coverage. ${ \widehat { \theta } } _ { 0 }$ denotes the type of consumer who is indifferent between purchasing product L and making no purchasing. In this case, the two vendors’ equilibrium prices when the two products are fully compatible are

$$
\left\{ \begin{array}{l} p _ {H} ^ {D *} = (q _ {H} - q _ {L}) \frac {2 q _ {H} - \alpha}{4 q _ {H} - q _ {L} - 3 \alpha} \\ p _ {L} ^ {D *} = (q _ {H} - q _ {L}) \frac {q _ {L} + \alpha}{4 q _ {H} - q _ {L} - 3 \alpha} \end{array} \right.\tag{A23}
$$

Both $p _ { H } ^ { D * }$ and $p _ { L } ^ { D * }$ equal zero when $q _ { H } = q _ { L } ;$ thus, Lemma 2 still holds under partial market coverage. That is, the new entrant should not release its product at the time when its product quality equals that of the incumbent.

For robustness check, we analyze an extreme case in which the intensity of network effects equals zero (ߙ = 0(. In this case, the optimal prices, demand, and profit rates for the two vendors are

$$
\left\{ \begin{array}{l} p _ {H} ^ {D *} = \frac {2 q _ {H} (q _ {H} - q _ {L})}{4 q _ {H} - q _ {L}} \\ p _ {L} ^ {*} = \frac {q _ {L} (q _ {H} - q _ {L})}{4 q _ {H} - q _ {L}} \end{array} \right. \quad \left\{ \begin{array}{l} Q _ {H} ^ {*} = \frac {2 q _ {H}}{4 q _ {H} - q _ {L}} \\ Q _ {L} ^ {*} = \frac {q _ {H}}{4 q _ {H} - q _ {L}} \end{array} \right. \quad \left\{ \begin{array}{l} \pi_ {H} ^ {*} = \frac {4 q _ {H} ^ {2} (q _ {H} - q _ {L})}{(4 q _ {H} - q _ {L}) ^ {2}} \\ \pi_ {L} ^ {*} = \frac {q _ {H} q _ {L} (q _ {H} - q _ {L})}{(4 q _ {H} - q _ {L}) ^ {2}} \end{array} \right.\tag{A24}
$$

The optimal release time can be obtained by solving

$$
\max _ {\tau_ {B}} \Pi_ {B} = \left\{ \begin{array}{c} \frac {q _ {A} (\tau_ {B}) q _ {B} (\tau_ {B}) [ q _ {A} (\tau_ {B}) - q _ {B} (\tau_ {B}) ]}{[ 4 q _ {A} (\tau_ {B}) - q _ {B} (\tau_ {B}) ] ^ {2}} (D - \tau_ {B}) - k \tau_ {B}, \tau_ {B} \leq \tau_ {E} \\ \frac {4 q _ {B} ^ {2} (\tau_ {B}) [ q _ {B} (\tau_ {B}) - q _ {A} (\tau_ {B}) ]}{[ 4 q _ {B} (\tau_ {B}) - q _ {A} (\tau_ {B}) ] ^ {2}} (D - \tau_ {B}) - k \tau_ {B}, \tau_ {B} > \tau_ {E} \end{array} \right.\tag{A25}
$$

Since the optimal release time for the new entrant is analytically intractable, we choose to graphically compare the profits of Vendor B under full and partial market coverage. The solid and the dotted lines in Figure A4 represent the profit curves of Vendor B under full coverage, and partial coverage, respectively. As shown in the figure, although the optimal release time and profit for Vendor B under partial coverage differs from those under full coverage, the pattern of two-local-optima remains unchanged.

![](/api/attachments/TRJXGV8F/fulltext/images/43dd56e26d821817706de853a8c8a4ce3c64dd3bee82edb62d3206d4b6a78ac0.jpg)  
(a( $\underline { { \varDelta q _ { 0 } = 0 . 2 5 } }$

![](/api/attachments/TRJXGV8F/fulltext/images/bad3cc3bc14a0903250395ce776bf5e0ffeb08619cfcb4c6f7d9da4680a2ea6e.jpg)  
(b( $\underline { { \varDelta q _ { 0 } = 0 . 5 } }$

![](/api/attachments/TRJXGV8F/fulltext/images/1b1e4c92b1752ae73c19a4f53a14cc423c61f38666589d9406f3fcd75e2c6702.jpg)  
(c( $\underline { { \varDelta q _ { 0 } } } = 0 . 7 5$  
0.1, = ߣ 20, = ܦ) $q _ { A 0 } = 2 , \theta _ { 0 } = 0 , \alpha = 0 . 2$ ,(only coverage full for ( $k = 0 . 1 )$

## Figure A4. Profit Comparison

We have also examined whether instant release and late release remain the only feasible release strategies under partial market coverage. We find that, theoretically speaking, a third possible strategy does exist. Specifically, under partial market coverage, after adopting the instantrelease strategy, Vendor B’s product quality is lower than Vendor $\mathbf { A } \ ' \mathbf { s } .$ . In this case, if Vendor B increases its product quality, more low-end consumers will be attracted to purchase product B, i.e., ${ \widehat { \theta } } _ { 0 }$ becomes smaller. However, when we assume $\theta _ { 0 }$ to be sufficiently large to ensure that the market is fully covered, such expansion in low-end market wouldn’t exist. Therefore, using $\theta _ { 0 }$ to assure full-market coverage could in some cases eliminate Vendor $\mathrm { B } \ ' \mathrm { s }$ incentive to increase its product quality.

As discussed above, when we relax the full-market coverage assumption by considering the partial-coverage scenario $( \mathrm { i } . \mathsf { e } . , \theta \in [ 0 , 1 ] )$ (, a higher quality for product B will attract more low-end customers; thus, it is theoretically possible that the “releasing on time $0 ^ { \circ }$ strategy could change to “releasing in $( 0 , \tau _ { E } ) , ^ { \ ' }$ which allows Vender B to further increase its quality even when it determines to target the low end market. However, further analysis reveals that even in the partial-coverage scenario (i.e., $\theta \in [ 0 , 1 ] )$ (, Vendor B prefers “releasing at time $0 ^ { \circ }$ to “releasing in $\left( 0 , \tau _ { E } \right) ^ { \ ' }$ in most cases. This is because although delaying the release from time 0 to a later time in $( 0 , \tau _ { E } )$ might lead to a slightly larger market share for Vendor B, the benefit of releasing its product at time 0 can still be higher for the following reasons:

(a) Releasing at time 0 would give Vendor B the longest possible duration of service.

(b) Releasing at time 0 would save Vendor B’s development cost.

(c) Releasing at time 0 would help Vendor B better differentiate its product from the incumbent’s in quality, thus reducing competition between the vendors.

To examine the tradeoffs, we have conducted additional numerical experiments. We find that “releasing at time $0 ^ { \circ }$ can still be a viable strategy under various circumstances, whereas “releasing in $( 0 , \tau _ { E } ) ^ { \dag }$ can be optimal only when the initial quality of vendor B’s product is close to 0. Recall that the scenario we consider in this study is that Vendor B’s product is ready for release at time 0, which indicates that product B’s initial quality cannot be too low. Therefore, although it is theoretically possible for “releasing in $( 0 , \tau _ { E } ) ^ { \dag }$ to be an optimal strategy, the probability that it would occur under the scenario we consider is very small.
