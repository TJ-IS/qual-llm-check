---
otero_id: 3368
otero_key: "9G49JZ38"
title: "Pricing Data Services: Pricing by Minutes, by Gigs, or by Megabytes per Second?"
authors: "Ying-Ju Chen; Ke-Wei Huang"
year: "2016"
journal: "Information Systems Research"
doi: "10.1287/isre.2016.0651"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/9G49JZ38/fulltext/images/6f08239c14ac05dc7037f5cbd332e1c525d3248cf6b2d9229defdaa0b38176dd.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Pricing Data Services: Pricing by Minutes, by Gigs, or by Megabytes per Second?

Ying-Ju Chen, Ke-Wei Huang

To cite this article:

Ying-Ju Chen, Ke-Wei Huang (2016) Pricing Data Services: Pricing by Minutes, by Gigs, or by Megabytes per Second?. Information Systems Research

Published online in Articles in Advance 29 Aug 2016

http://dx.doi.org/10.1287/isre.2016.0651

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2016, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/9G49JZ38/fulltext/images/91a0d951c5dd167ec1cfdf042715b5e724ef16e0b2ef8ad17b7cc41b6916cde4.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Pricing Data Services: Pricing by Minutes, by Gigs, or by Megabytes per Second?

Ying-Ju Chen

School of Business and Management and School of Engineering, Hong Kong University of Science and Technology, Clear Water Bay, Kowloon, Hong Kong, imchen@ust.hk

Ke-Wei Huang

Department of Information Systems, National University of Singapore, Singapore 117417, huangkw@comp.nus.edu.sg

otivated by the pervasive discrepancy among the pricing schemes of data services, this paper investigates model in which a monopoly data services seller faces heterogeneous consumers whose utilities depend on the usage and the connection speed. We examine three options for the seller to conduct the second-degree (indirect) price discrimination: by minutes, by gigabytes (Gigs), and by megabytes per second (Mbps). We show that the after-sales self-selection behaviors have a significant impact on the seller’s profitability, and it leads to a firstorder influence on the pricing metric selection. We prove that either pricing by Gigs or Mbps can be optimal. Pricing by Gigs can dominate pricing by Mbps even if the consumer’s utility is more sensitive in changes in the connection speed. We also find that when incorporating the bandwidth costs or congestion costs, pricing by Mbps becomes more attractive as it allows the seller to directly control the congestion effect. These findings may help practitioners to develop their own pricing plans and pricing metrics selection.

Keywords: service pricing; price discrimination; versioning; game theory

History: Anitesh Barua, Senior Editor; Xianjun Geng, Associate Editor. This paper was received on March 21, 2010, and was with the authors 27 months for 4 revisions. Published online in Articles in Advance August 29, 2016.

## 1. Introduction

Since 2000, the explosion of data traveling on the Web has brought in tremendous revenues for Internet service providers (ISPs) and telecommunication companies. Recently, the same trend has propagated to the cell phone industry. While the percentage of cellular carriers’ revenue from data plans remains relatively low in 2010 (less than 20%, even including lucrative text messaging services), the expected year-over-year growth rate is high. Primary drivers for this trend include higher data throughput around 1 megabytes per second (Mbps), availability in most major metropolitan areas, multiple device options (including smartphones, laptops, netbooks, iPads, and eBook readers such as Kindle), and an increasing selection of mobile applications and middleware (Rysavy 2008). In 2008, based on WiMax, the next generation’s wireless technology, Sprint–Nextel started offering data services promising average download/upload of 4/2 Mbps. Typical industry analysts see no roadblocks of the long-term adoption of cellular broadband, particularly after iPhone 3G offered consumers an addictive taste for mobility of computing.

Being aware of such a rising trend, how can a data services provider capitalize on the opportunity? Anecdotal evidence from various ISPs and cell phone companies seems to imply pricing is the key. An intuitive approach for marketing managers is probably to learn from the history of pricing ISP technologies in the past. However, the historical pricing plans are quite different, particularly on how the ISPs choose their “pricing metrics”—the basis or units for price discrimination. Historically, 56 K modem dialup and ISDN ISP services were charged based on per-hour pricing.<sup>1</sup> Nowadays, most of the residential ADSL (asymmetric digital subscriber line) services or cable-modem-based ISPs charge consumers based on download/upload speeds.<sup>2</sup> As we move toward the era of mobile commerce, leading mobile companies offer wireless broadband 3G services with pricing plans based on the total data usage limit (gigabytes, Gigs, or GB).<sup>3</sup> While most of the mobile broadband service providers charge consumers by Gigs, pricing plans based on download/upload speeds (e.g., in Singapore and Malaysia) or time usage (e.g., the per-hour pricing in Taiwan and the per-day pricing in New Zealand) are also adopted contemporarily. The same paradoxical phenomenon exists in the pricing for fixed-line or wireless backhaul data networks in which a large telecommunication vendor charges small ISPs by data usage or by bandwidth.

Recent evidence strengthens our conjecture that practitioners do not have scientific methods to choose pricing metrics for data services, as fixed-line residential ISPs realized that the prevalent pricing by Mbps may not be profit maximizing. For example, in 2008, Time Warner first experimented in Texas a trial of “consumption-based billing” or called “metered pricing,” which is essentially one form of pricing by Gigs. They claimed that this strategic move was made to boost the revenue by avoiding the consequences of unfairness pricing (Pegoraro 2009).<sup>4</sup> Time Warner’s experiment soon ignited the interests of ISPs all over the world: major ISPs either announced or rolled out testing volume-based plans even at the risks of offending consumers (Chua 2008 and Hartley 2009). Some of these experiments were halted by regulators who believe that they may go against the consumers’ benefits. Nevertheless, this does not preclude the possibility that meticulous design of pricing plans could enhance the ISPs’ profitability, since regulatory concerns and the ISPs’ intrinsic incentives are typically misaligned.<sup>5</sup> As another example, during an interview with the Wall Street Journal in November 2010, Verizon’s Chief Financial Officer revealed that they were considering a tiered pricing structure for wireless data connection, a pricing method similar to home wired Internet service. However, a few months later, Verizon decided to use pricing by Gigs that is common for 3G plans (Cheng and Raice 2010). This provides a piece of evidence that the pricing metric selection is challenging even for the world’s largest telecommunication company.

Motivated by the pervasive discrepancy regarding the pricing scheme and the lack of consensus, this paper attempts to investigate the selection of pricing metrics and the corresponding ISP pricing plans. In pursuit of this goal, we construct a model in which a monopoly data service provider (seller hereafter) intends to provide heterogeneous consumers data services under second-degree price discrimination plans (also called nonlinear pricing or indirect price discrimination in the literature). Different from utility functions used in the literature, consumers’ utilities comprise three core components: time usage, connection speed, and data usage (which is the product of the first two components). On the other hand, consumers are heterogeneous with regard to their willingness-to-pay per unit data usage and/or per connection speed. These unique characteristics suggest that in addition to pricing plans, the seller also has three options of pricing metrics: by time usage (per minute or per hour), by connection speed (per Mbps), and by data usage (per Gigs). In essence, our model adds the first-stage metrics selection problem on top of the standard nonlinear pricing model in which it typically takes one pricing metric as exogenously given (e.g., Maskin and Riley 1984 and Mussa and Rosen 1978).<sup>6</sup>

Without a rigorous analysis, an intelligent guess by marketing professionals could be using the pricing metric that “plays the most important role in the consumers’ utility” or the pricing metric that is most correlated to the heterogeneity in demand. The problem of pricing metrics selection turns out to be more sophisticated. We show that the key criterion for the pricing metric selection is not simply the a priori consumer sensitivities to each pricing metric or demand characteristics; rather, what could matter more is the flexibility left to the consumers to adjust the remaining pricing metrics that are not specified in the pricing plan. The reason is that flexibility leads to overconsumption relative to the profit-maximizing level, aggravating the conflict of interests between the seller and the consumers. To explain this concept, we take ADSL pricing as an example. When the seller prices by Mbps, the consumers are left with flexibility in choosing the data usage, and clearly they will choose the level of usage to maximize their utilities because usage is free. It is intuitive to infer that consumers’ data usage will become too high in the ISPs’ eyes. The intertwining effect between pricing metric and consumers’ after-sales action, to our knowledge, has never been documented in the existing literature on nonlinear pricing or digital goods pricing.

Building on this observation, we set up our baseline model in Section 3 to analytically demonstrate these phenomena in a mathematically rigorous manner. We show that profitability of pricing metrics critically depends on how a pricing metric balances the profit from price discrimination and the flexibility left for consumers to adjust after the transaction. In our baseline model, we assume that the utility function is additive of two concave functions in data usage and speed, respectively. Under this assumption, pricing by time usage is suboptimal and interestingly the profit-maximizing pricing strategy based on time is uniform pricing. The reason is that in our baseline model, consumers obtain utilities from the time usage only through the total data usage. Thus, under pricing by minutes, consumers still have the discretion of selecting data usage. The after-sales overconsumption (relative to the profit-maximizing level) is so overwhelming that it forces the seller to abandon the use of multitiered pricing plans.

On the contrary, under pricing by Gigs or Mbps, the seller can effectively suppress the after-sales selfselection of the consumers; thus, the optimal pricing strategy is to use multitiered pricing plans. To choose between these two pricing options, the seller needs to gauge complicated cost-benefit analysis. The seller’s final revenue can be decomposed into three parts. In addition to the revenue derived from the classical second-degree price discrimination, we identify two novel effects that emerge from the after-sales selfselection behaviors. First, after-sales self-selection can maximize part of the consumer’s utility function and increase the consumer’s overall utility (e.g., buffetstyle pricing can increase consumption and utility). Second, after-sales behaviors could lead to “overconsumption,” especially for heavy-usage consumers. As a result, consumers become more heterogeneous in their preference. This aggravated information asymmetry makes it more challenging for the seller to facilitate price discrimination, thereby leading to the undesirable revenue reduction.

We then extend our analysis in several directions. In particular, we incorporate the supply side constraint in two different ways. First, we introduce a waiting cost in the consumer’s utility function. This waiting cost captures the time opportunity cost when the Internet service is too slow. We allow each individual consumer’s waiting cost to depend on the aggregate level of bandwidth usage of the entire population. We find that “disutility toward waiting” makes pricing by Mbps more profitable. In addition, when the seller is confronted with the total bandwidth constraint, a similar prediction is established. The underlying reason is that pricing by Mbps allows the seller to directly control the congestion effect. By contrast, under other pricing metrics, the connection speed is at the consumers’ discretion and they do not internalize the negative externality brought to others.

The remainder of this paper is organized as follows. Section 2 reviews some relevant literature. In Section 3, we introduce the model. Section 4 characterizes the seller’s optimal pricing scheme. In Section 5, we investigate the impacts of some crucial components of our model setup and discuss the possible consequences. Section 6 concludes and provides several directions for extensions. All proofs are relegated to the appendix.

## 2. Literature Review

Our research is built on the nonlinear pricing literature and adds to a growing literature on digital goods pricing using a similar model setup. Previous research has studied nonlinear pricing of digital goods in the contexts of search-based and subscription-fee pricing for online information services (Jain and Kannan 2002), the impacts of menu costs (Sundararajan 2004b), pricing to deter piracy with digital rights management (Sundararajan 2004a), customized bundling (Hitt and Chen 2005), three-part tariff (fixed-up-to (FUT) pricing plan) in the telecommunication industry (Masuda and Whang 2006), versioning with outside options (Chen and Seshadri 2007), personalization with privacy concerns and disposal costs (Chellappa and Shivendu 2010), upgrading pricing strategy (Mehra et al. 2012), and pricing with infrastructure costs (Huang and Sundararajan 2011). However, all of the aforementioned papers do not discuss pricing metrics selection, which is the central issue in this paper.

The typical weakness of the aforementioned literature is to assume that all information technology (IT) costs are fixed and irrelevant; thus, the supply side properties of the IT infrastructure are neglected. On the other hand, another well-developed line of analytical pricing research focuses on the supply side explanations for pricing IT services. The seminal study by Mendelson (1985) highlights the optimal transfer pricing for IT services whose supply is subject to capacity constraints, resulting in a fundamental trade-off between the utilization rate and consumers’ delay costs. Many subsequent papers have extended Mendelson’s model, including Mendelson and Whang (1990), Dewan and Mendelson (1990), Gupta et al. (1997, 2000), and Konana et al. (2000). In a related vein, some researchers abstract away from queueing effects and examine other important properties of IT infrastructure. MacKie-Mason and Varian (1995) provides one pioneering stylized model. In the early Internet age, Odlyzko (1998) provides a detailed conceptual summary of related economics and business practice about pricing telecommunication services.

In a series of papers (Fishburn and Odlyzko 2000, Fishburn et al. 2000), the authors untangle the complicated relationship among infrastructure utilization, infrastructure topology, quality of services (delay), and costing and pricing of the infrastructure capacity or IT services. Along this line of studies, Du et al. (2008a) conceptualize a model of the Internetbased storage provisioning network. They propose a novel “discount factor,” which can be calculated from the service delay and the topology of service providers. This discount factor is examined empirically and serves as an accurate index for the service providers’ incentive to trade excessive storage capacity (see also Du et al. 2008b). Das et al. (2011) investigate the optimal pricing for storage services with demand uncertainty and show that the forward contracts can reduce risk and enhance the service provider’s revenue. Our paper is built on the nonlinear pricing literature; unlike the prior studies, we jointly investigate the specifications of utility function, information asymmetry, and pricing metrics selection. We further examine how supply side factors (such as congestion costs) interact with the above demand-side effects.

Recently, researchers in the information systems (IS) field have started to discuss pricing problems similar to our metrics selection problem. Choudhary (2010) provides a pioneering model to study the profitability of different types of price schemes, a concept similar to the pricing metrics in the present paper. The pricing metrics selection is first investigated in Huang (2009), where he focuses on the direct (third-degree) price discrimination. Unlike Huang (2009), we incorporate the after-sales behaviors of the consumers and investigate the indirect (second-degree) price discrimination. Lahiri et al. (2008) investigate multiapplication pricing versus data usage pricing. While their primary focus is on the comparison between these two pricing plans and their relation to net-neutrality (i.e., the regulation that ISP vendors should not price discriminate consumers based on the applications), we study the optimal pricing metric for “usage” pricing.

It is also worth mentioning that in our baseline model, under pricing by time usage, the seller’s price discrimination power is completely offset by the aftersales consumer behaviors, i.e., uniform pricing is optimal. This finding is similar to the optimality of “no versioning” in the IS literature. Notably, the profitability of versioning digital goods has been examined in a number of papers, including Bhargava and Choudhary (2001, 2004), Jing (2007), and Jones and Mendelson (2011); see also Bhargava and Choudhary (2008) for a thorough investigation of when and why versioning is optimal in various contexts. This research stream documents that “no versioning,” or equivalently uniform pricing, is optimal when the utility function has a separable form: $U ( q , \theta ) = A ( q ) \times$ $B ( \theta ) - p$ (Bhargava and Choudhary 2008). Our result may provide a new rationale for the suboptimality of versioning. Since our original specification of utility function is increasing and concave in all three pricing metrics, it falls outside the documented regime wherein no versioning is shown to be optimal (e.g., Bhargava and Choudhary 2008). However, the consumer’s after-sales overconsumption could be so strong that it transforms the utility function from a concave function into a multiplicative function of $\theta ;$ this makes it unprofitable for the seller to conduct price discrimination. Although the conclusion is the same as that in the versioning literature, the underlying driving force is completely different.

## 3. Model

In this section, we introduce our baseline model. Before proceeding, we would like to highlight that our analysis shows that the profit-maximizing pricing metric critically depends on the functional form of the utility function. Various specifications of utility functions may lead to very different equilibrium outcomes. The utility function proposed in this section serves as an example that is applicable to selected real-world applications. Similar to other complicated economics models, more realistic utility functions are numerically but not analytically tractable. Therefore, based on our exploration efforts so far, it is challenging to devise a perfect functional form for all realistic applications. General properties of the equilibrium will be discussed in Section 5. The main purposes of this section are to explain the distinguishing features of this new pricing problem and to demonstrate how one can analytically solve this problem.

Pricing Metrics. We build on the standard nonlinear pricing model (or equivalently second-degree price discrimination model) by Mussa and Rosen (1978). A risk-neutral seller (he) intends to provide data services to heterogeneous consumers indexed by type $\theta ,$ and the seller does not know the exact type for each consumer (she). Throughout this paper, we use B, M, and $B \times M \equiv Q$ to denote the three pricing metrics. Specifically, B is the average connection speed per unit time, Q is the total data usage, and M represents the total time usage. Each of these pricing metrics has been adopted in the ISP pricing practice. We will use pricing by B, M, and Q to refer to the pricing plan based on speed, time usage, and data usage.<sup>7</sup>

This study attempts to investigate the pricing metrics selection problem of three cases: two pricing metrics B1 M1 and one multiplicative pricing metric $Q =$ B ×M. This setup does not perfectly fit all applications because of this simplified multiplicative property, but it is rich enough to demonstrate the complexity in the metrics selection problem and hopefully provide some practical guidelines. This problem is also scientifically interesting since it has not been studied in the vast number of nonlinear pricing papers.

Consumers’ Utility Function. To provide the simplest model for studying the pricing metrics selection problem, we start our analysis with the following functional form for the consumer’s utility:

$$
u (B, M, \theta) = U ^ {Q} (Q, \theta) + U ^ {B} (B, \theta),
$$

$$
U ^ {Q} (Q, \theta) = \left\{ \begin{array}{l l} \delta \theta B M - \frac {1}{2 \eta} (B M) ^ {2}, & \text {if} B M <   \eta \delta \theta , \\ \frac {1}{2} \eta \delta^ {2} \theta^ {2}, & \text {if} B M \geq \eta \delta \theta , \end{array} \right.\tag{1}
$$

$$
U ^ {B} (B, \theta) = \left\{ \begin{array}{l l} \theta B - \frac {1}{2 \gamma} B ^ {2}, & \text { if } B <   \gamma \theta , \\ \frac {1}{2} \gamma \theta^ {2}, & \text { if } B \geq \gamma \theta . \end{array} \right.
$$

Parameters $\delta , \eta ,$ and  are positive parameters and are identical across consumers. The variables $B , \ M ,$ and Q are assumed to be nonnegative. In other words, we assume the utility function consists of two weakly increasing quadratic functions with satiation points. The first term of (1) represents an increasing and concave function of data usage Q. Similarly, the second term is a quadratic function in connection speed B. We impose the two inequalities to ensure that the utility function is always weakly increasing. Once $B M > \eta \delta \dot { \theta }$ or $B > \gamma \theta ,$ , we assume these two quadratic functions equal $\scriptstyle { \frac { 1 } { 2 } } \dot { \eta } \delta ^ { 2 } \theta ^ { 2 }$ or ${ \scriptstyle { \frac { 1 } { 2 } } } \gamma \theta ^ { 2 } .$ , respectively.

The quadratic utility function of one abstract metric in pricing models was first adopted by Singh and Vives (1984), and it has been widely used as the microfoundation of linear demand function in applied economics papers. This quadratic functional form is appropriate in our pricing context also for the following reasons. First, it satisfies all of the regularity conditions required in the nonlinear pricing literature, as it is increasing and concave in each pricing variable. Intuitively, this implies that the consumer always prefers more data usage, time usage, and faster connection when the unused pricing metrics are fixed, but it exhibits a diminishing marginal rate of preference for each metric.

Second, this functional form has been applied because of its tractability to derive transparent closedform solutions. Hence, it appears frequently as the baseline model or as the main numerical example in the nonlinear pricing literature (Grubb 2009, Hitt and Chen 2005, Huang and Sundararajan 2011, Sundararajan 2004b). This utility assumption is mathematically equivalent to models with $u ( Q , \theta ) = \theta Q$ and a constant variable cost at ${ \textstyle \frac { 1 } { 2 } } Q ^ { 2 }$ in the vertical differentiation literature (Mussa and Rosen 1978) or models with $u ( Q , \theta ) = \theta \dot { Q } - { \textstyle \frac { 1 } { 2 } } Q ^ { 2 }$ and a zero variable cost in the versioning or pricing for digital goods literature (e.g., Chellappa and Shivendu 2007, 2010, and Sundararajan 2004a). Our results can therefore be compared with the existing literature using these assumptions. Tractability requirement is also higher in our analysis because we tackle a problem with more than one potential pricing metric. We defer the discussion about the concavity of B when we explain why consumers can self-select speed at the end of this section.

There are two additive, separable quadratic utility functions in (1) for the following reasons. First, this model is connected to the vast empirical literature that examines the utility function or determinants of the value of an Internet connection, ranging from the dialup era in the late 1990s to the modern mobile broadband era. Researchers either use discrete choice models with random utility functions (Ida and Kuroda 2006, Satitsamitpong et al. 2012, Savage and Waldman 2004) or hedonic pricing regression (Deligiorgi et al. 2007, Wallsten and Riso 2014, Stranger and Greenstein 2007, Yu and Prud’Homme 2010). In either case, almost all papers use simple linear regressions with B, M, or Q specified as explanatory variables.<sup>8</sup> Second, the separable form allows us to isolate the two effects a priori in the consumers’ utilities; their interplay is then crystalized after we incorporate the after-sales self-selection. Third, it is arguably the simplest functional form that delivers analytical results.

In (1), we include only two (but not three) quadratic components because in reality, it seems that modern ISP consumers do not derive utilities from the time usage alone. The value of time usage seems to be highly correlated with the data usage in most scenarios of ISP pricing. By contrast, some may even argue that $u ( \bar { B , } M , \bar { \theta ) }$ should be decreasing in time usage because of the disutility of waiting time. We choose (1) for ease of exposition to explain the complex effects among pricing metrics. We provide an alternative setup with the waiting time disutility in Section 5.2.2. Another justification is that earlier empirical studies mostly include time usage in the regression, whereas most recent studies about broadband pricing do not include time usage at all. This hints to the trend that nowadays time usage does not directly affect consumers’ utilities (as opposed to the 1990s).

Consumers’ Type and Heterogeneity. In (1), the parameter  summarizes the individual consumer’s heterogeneous preference about usage. In the literature,  is interpreted as the marginal willingness-to-pay of Q when the utility function is specified as $u ( Q , \theta ) =$ $\theta \bar { Q } - { \textstyle \frac { 1 } { 2 } } Q ^ { 2 }$ . That is, one unit increase in Q may lead to  unit increase in the utility function. The parameter  also represents the heterogeneity in preference because the utility-maximizing level of Q critically depends on the value of . In this simplest example, $Q ^ { * } = \theta$

The relative importance of the preference on B and Q is moderated by three parameters: $\delta , \eta ,$ and $\gamma .$ The coefficient of the first-order term, BM or $\theta B ,$ in (1) is  versus 1. When $\delta \ge 1$ , there are two effects: the consumers become more sensitive to changes in $Q$ than in B and the first utility function is relatively more valuable than the second one. Therefore, one interpretation of  is that it can moderate consumer heterogeneity. To see this, in (1), the local maxima of the first quadratic function is $\delta \eta \theta ,$ implying larger values of  maps to a more diverse utility-maximizing usage level. Parameters  and  are used to model the concavity of these two quadratic functions.<sup>9</sup> The larger  or $\gamma \ \mathrm { i s } ,$ the less diminishing return connection speed will be.

Take connection speed, $B ,$ as an example. In the dialup age, all consumers use the Internet for basic Web browsing and emailing, and they are not much better off when given a higher connection speed and they do not have heterogeneous preference in B. Earlier empirical studies about dialup pricing also show that connection speed is only marginally significant in the utility function (Yu and Prud’Homme 2010). The analogy in our setup is that  is larger than 1. At the same time, the marginal benefit in getting faster speed could decrease sharply and the satiation speed is relatively low, which in our setting corresponds to having a smaller sensitivity parameter . By contrast, for the modern residential ADSL case, consumers can use a wide variety of applications, such as online games, peer-to-peer applications, Skype, and streaming music or videos. Different consumers may have distinct preferences about which application to use. Also, larger bandwidth is critical in the effectiveness of some applications, which translates to a larger .

Information Structure. The functional form (1) is common knowledge in this model. The variables $B ,$ $M ,$ , or $B \times M$ are observable pricing metrics. Consistent with the literature, the parameter $\theta$ is privately observed by the consumer but is unknown to the seller. From the seller’s perspective,  is a random variable, and for simplicity we assume that it is uniformly distributed over 601 17. This distributional assumption is relaxed in Section 5. This information asymmetry between the seller and the consumers leads to a single-dimensional screening problem, and it allows us to partially follow the systematic approach developed by Maskin and Riley (1984) (it is only partial as there are multiple pricing metrics). Implicitly, we assume that consumers who have a stronger preference for Q also have a stronger preference for B in this model.

Timing. The sequence of events proceeds as follows.

Stage 1. The seller determines the pricing metrics out of three options: time usage, data usage, or connection speed.

Stage 2. The seller announces a pricing menu as a function of the selected pricing metric: $P ^ { \boxtimes } ( M ) , P ^ { B } ( B )$ or $P ^ { Q } ( Q )$ , where the superscripts indicate the different scenarios.

Stage 3. Each consumer self-selects one pricing option from the pricing menu.

Stage 4. Each consumer adjusts the variable(s) not explicitly specified in the pricing menu to maximize her utility. For example, under pricing by $M ,$ the consumer can adjust the speed (B) or equivalently data usage $( Q = B { \dot { M } } )$ to maximize her utility. Under pricing by B, the data usage (Q) or equivalently the time usage (M) can be self-selected in this stage. Finally, under pricing by Q, the consumer determines the speed or equivalently the time usage.

The majority of the existing literature solves the pricing problem in Stages 2 and 3. Thus, the unique feature here is that we add two additional stages, Stages 1 and 4, to account for the pricing metrics choice of the seller and the after-sales self-selection of the consumers. By backward induction, we first take the pricing metrics as given and derive the optimal pricing plans under three different scenarios (Stage 2’s solutions) in Sections 4.1–4.3. Following this, we compare the seller’s maximum expected profits and determine the optimal pricing metric in Stage 1 in Section 4.4.

Notably, in Stage 4 we allow the consumers to adjust the total data usage, time, or speed. In reality, it is natural to assume that ISP subscribers can choose data or time usage. The interpretation of the self-selection of speed includes the following scenarios. First, consumers can select the speed because they can choose from a list of speed-demanding software applications. Using these applications means the consumer chooses a faster speed. Second, some applications allow consumers to specify the speed. For example, most peer-to-peer (P2P) software applications allow consumers to fine-tune the speed as a continuous variable, a scenario that perfectly fits our setup. For streaming video sites, consumers can choose the resolution of videos, which indirectly affects the speed usage. The third possibility is that families or small/medium companies may need to share one broadband connection among several $\mathrm { P C } s ,$ smart $\mathrm { T V s , }$ or mobile devices. Consumers can decide the number of devices to share that connection, which indirectly affects the total speed usage.

This list of options also leads to potential concavity in the utility function in B for the following reasons. First, when the faster speed is used for sharing among several users and devices in a large family or smallmedium companies, as B increases, ultimately it can meet the demand of all users in the same local network. Therefore, the utility function is concave when B is large enough. Second, for Skype or streaming videos, when the connection is fast enough, the difference in the quality of the service becomes negligible to consumers. This implies that the utility function could be concave in B. For P2P software or other applications, the benefit of faster connection has decreasing marginal benefits to customers because the disutility of waiting becomes smaller when the duration of waiting becomes smaller. Last, given a fixed limit on speed, we can imagine that consumers will first use the application that is more important to them. As the speed increases, consumers start adopting less useful applications. This results in a smaller utility gain and therefore, the utility function in B could be concave.

Optimal Pricing Plan. The seller cannot observe the consumer’s type  and a nonlinear pricing plan is implemented to maximize expected profits. As an example, the objective function under pricing by M in Stage 2 is given by

$$
\Pi = \max _ {P ^ {M} (M)} \mathbb {E} _ {\theta} [ P ^ {M} (M) ],
$$

and likewise for the other two pricing metrics B and Q. We do not assume any cost function in the objective function. Discussions about the impacts of cost functions are in Section 5.

In general, the (second-stage) problem of designing the pricing plan is fairly complicated since it requires the seller to characterize the entire function. Fortunately, researchers have made significant progress in this area and we can greatly simplify the analysis and proofs in this study. Specifically, as a first step, we can invoke the revelation principle to replace the pricing plan $( \mathrm { i . e . , } P ^ { M } ( M ) )$ by a menu of type-dependent contracts $( \mathrm { i . e . , ~ } ( M ( \theta ) , P ^ { \check { M } } ( \theta ) ) )$ ; see similar arguments in Maskin and Riley (1984) and Sundararajan (2004b). The remaining solution procedure is standard and well established in the literature. Having introduced the consumers’ utility, information structure, and the seller’s objective, we characterize the optimal pricing plans for the three different metrics in Section 4.

## 4. Analysis

In this section, we first characterize the seller’s optimal pricing scheme in three pricing metrics, respectively. Comparing the profitability of three metrics is reported in Section 4.4. A numerical example is provided in Section 4.5.

## 4.1. Pricing by Minutes

We start with the simplest case in which the seller charges by time usage M in Stage 1. In Stage $^ { 2 , }$ the seller offers a menu $\{ ( M ( \theta ) , P ^ { \check { M } } ( \theta ) ) \}$ for the consumers to self-select. As a type- consumer chooses an arbitrary contract $( M ( { \hat { \theta } } ) , { \bar { P ^ { M } } } ( { \hat { \theta } } ) )$ from the menu in Stage $^ { 3 , }$ her net utility, denoted by $U ^ { M } ( B \mid \theta , \hat { \theta } )$ , can be expressed as

$$
\begin{array}{r} U ^ {M} (B \mid \theta , \hat {\theta}) = \delta \theta B M (\hat {\theta}) - \frac {1}{2 \eta} (B M (\hat {\theta})) ^ {2} \\ + \theta B - \frac {1}{2 \gamma} B ^ {2} - P ^ {M} (\hat {\theta}). \end{array}\tag{2}
$$

Note that M does not appear in the argument of the left-hand side because it is specified in the contract and has been fixed in Stage 4. This is also the only difference between (1) and (2).

Because the equality $Q = B M$ always holds, the consumer’s problem in Stage 4 is to choose $B ,$ or equivalently Q, that maximizes her utility.<sup>10</sup> Since (2) is a quadratic function of $B ,$ it is straightforward to verify that the optimal solution is one of the local maximal points of two quadratic functions

$$
B ^ {*} (\theta , \hat {\theta}) = \theta \max \biggl [ \frac {\eta \delta}{M (\hat {\theta})}, \gamma \biggr ].
$$

Given this solution, we next derive the “effective utility function” for the seller to conduct price discrimination in Stage 2 and Stage 3. We denote this effective utility function by $U ^ { M } ( \Breve { \theta } , \hat { \theta } ) \equiv U ^ { M } ( B ^ { * } ( \theta , \hat { \theta } )$ $\theta , { \hat { \theta } } )$ , where  means consumer type and $\hat { \theta }$ means the per-M contract designed for type <sup>ˆ</sup>. Therefore, $U ^ { M } ( { \hat { \theta } } , { \hat { \theta } } )$ is the utility function of type  when she chooses the contract designed for type <sup>ˆ</sup>. Furthermore, we let $U ^ { M } ( \theta ) \equiv U ^ { M } ( \breve { \theta } , \theta )$ to save notation.

Substituting $B ^ { * } ( \theta , { \hat { \theta } } )$ into (2) yields

$$
U ^ {M} (\theta , \hat {\theta}) = \theta^ {2} Y (M (\hat {\theta})) - P ^ {M} (\hat {\theta}),\tag{3}
$$

in which $Y ( M ( { \widehat { \theta } } ) )$ is a complicated function of $M ( { \hat { \theta } } )$ but not . The exact expression of $Y ( M ( { \widehat { \theta } } ) )$ is given in the appendix. The utility function $U ^ { M } ( \theta , \hat { \theta } )$ is also used for calculating the optimal nonlinear pricing in the literature. Notably, the existing literature typically starts with assumptions of the functional form of $\dot { U } ^ { M } ( \theta , \hat { \theta } )$ as a function of M and . Given $U ^ { M } ( \theta , \hat { \theta } ) .$ researchers derive the optimal pricing plan following the solution procedure in the literature.

The seller’s optimization problem in Stage 2 can be formulated as follows:

$$
\begin{array}{r l} \Pi^ {M} = & \max _ {M (\theta), P ^ {M} (\theta)} \mathbb {E} _ {\theta} [ P ^ {M} (\theta) ] \\ & \text {s.t.} (I C - M) \colon U ^ {M} (\theta) \geq U ^ {M} (\theta , \hat {\theta}), \quad \forall   \theta , \hat {\theta}; \\ & (I R - M) \colon U ^ {M} (\theta) \geq 0, \quad \forall   \theta , \end{array}\tag{4}
$$

where the incentive compatibility constraint (IC-M) induces the consumer to select the contract designed for her, and the individual rationality constraint (IR-M) guarantees that the consumer is willing to participate. The truth telling is induced without loss of generality given the revelation principle. All of these conditions are exactly the same as those in the literature, except that $U ^ { M } ( \theta , \hat { \theta } )$ is derived after we incorporate a stage of additional self-selection as illustrated in this section.

Solving this seemingly complicated problem turns out to be an easy task. In the versioning literature, the standard assumption is $U ( q , \theta ) \stackrel { \textstyle - } { = } \theta q - p$ with zero variable cost. It has been well documented that “no versioning,” equivalently uniform pricing, is optimal when the utility function has a separable form: $U ( q , \theta ) = A ( q ) \stackrel { . } { \times } B ( \theta ) - p$ (Bhargava and Choudhary 2008). Equation (3) obviously satisfies this separable property. As a consequence, the optimal pricing is uniform pricing and the corresponding seller’s profit can be obtained from solving standard monopoly pricing. The results are summarized in the next lemma.

<sup>Lemma</sup> <sup>1.</sup> When the utility function is (1), under pricing by M, the optimal pricing plan is uniform pricing

$$
\begin{array}{c} M ^ {*} = Q ^ {*} / B ^ {*} = \delta \eta / \gamma , \\ P ^ {M} (\theta) = \frac {2}{9} (\eta \delta^ {2} + \gamma). \end{array}
$$

The seller’s corresponding expected profit is $\Pi ^ { M } = ( 2 / 2 7 ) \times$ $( \eta \delta ^ { 2 } + \gamma )$

This lemma highlights the importance of consumers’ self-selection in Stage 4. Given (1), pricing by M seems to be one plausible choice of pricing (at least it shall be more profitable than uniform pricing), because pricing by M captures part of the consumer’s heterogeneity. However, our analysis shows that the flexibility left to the consumers is so strong that the monopoly price discrimination power is completely deprived. An implication of Lemma 1 is that a poorly chosen metric for price discrimination may not generate more profit than the uniform pricing strategy. Recall that this result is derived under the assumption of (1). If (1) indeed characterizes the preference of ISP consumers, our finding is consistent with the current practice: ISP vendors mostly consider between nonlinear pricing by Q or pricing by B. If (1) contains additional terms in M, Lemma 1 may not hold.

Sections 4.2 and 4.3 show that when the pricing metric is different, the seller can still conduct nonlinear pricing and profitability improves.

## 4.2. Pricing by Mbps

Let us now switch to the case in which the seller charges the consumers by connection speed in the first stage. The solution procedure is the same as that in Section 4.1. In this scenario, the seller offers a menu $\{ ( B ( \theta ) , P ^ { B } ( \theta ) ) \}$ to the consumers and each consumer then selects a contract from the menu. As a type- consumer selects a contract $( B ( \hat { \theta } ) , P ^ { B } ( \hat { \theta } ) )$ , her net utility becomes

$$
\begin{array}{c} U ^ {B} (M \mid \theta , \hat {\theta}) = \delta B (\hat {\theta}) M \theta - \frac {1}{2 \eta} (B (\hat {\theta}) M) ^ {2} \\ + B (\hat {\theta}) \theta - \frac {1}{2 \gamma} B (\hat {\theta}) ^ {2} - P ^ {B} (\hat {\theta}). \end{array}\tag{5}
$$

Similar to Section 4.1, here the consumer has the discretion of deciding how long she spends in using the service (or equivalently $\breve { Q }$ because $Q = B M { \dot { ) } }$ Mathematically, the role of B or M is the same in the first two terms, whereas only B appears in the last two terms. Intuitively, this means that in our setup, consumers care about the connection speed, in addition to the preference about data usage, but do not care about the time usage beyond its correlation with data usage. This could be more applicable when pricing residential broadband in recent years but less applicable when pricing dialup services before 2000.

From (5), we observe that the consumer’s utility function is again quadratic and concave in M. Thus, the optimal time usage selected by the consumer, denoted by $M ^ { * } ( \theta , \hat { \theta } )$ , is an interior solution characterized by the first-order condition

$$
M ^ {*} (\theta , \hat {\theta}) = \frac {\delta \eta \theta}{B (\hat {\theta})}.\tag{6}
$$

Note that $M ^ { * }$ is chosen to maximize the first quadratic function, whereas when pricing by M, B is chosen to maximize both quadratic functions. Because both functions are increasing and concave, more flexibility left for consumers in Stage 4 leads to more severe overconsumption.

Given the optimal time usage selection, we can then define $U ^ { B } ( \theta , { \hat { \theta } } ) \equiv U ^ { B } ( M ^ { * } ( \theta , { \hat { \theta } } ) \mid \theta , { \hat { \theta } } )$ as the type- consumer’s maximum net utility if she chooses the contract $( B ( { \hat { \theta } } ) , P ^ { B } ( { \hat { \theta } } ) ) ;$ furthermore, we let $U ^ { B } ( \theta ) \equiv$ $U ^ { B } ( \theta , \theta )$ to save notation. Substituting (6) into (5), we can derive the closed-form expression of $U ^ { B } ( \theta , { \hat { \theta } } )$ which becomes the input of the seller’s optimization problem in Stage 2 as follows:

$$
U ^ {B} (\theta , \hat {\theta}) = B (\hat {\theta}) \theta - \frac {1}{2 \gamma} [ B (\hat {\theta}) ] ^ {2} + \frac {1}{2} \eta \delta^ {2} \theta^ {2} - P ^ {B} (\hat {\theta}),\tag{7}
$$

$$
\Pi^ {B} = \max _ {B (\theta), P ^ {B} (\theta)} \mathbb {E} _ {\theta} [ P ^ {B} (\theta) ]\tag{8}
$$

$$
\mathrm{s.t.} U ^ {B} (\theta) \geq U ^ {B} (\theta , \hat {\theta}), \quad \forall \theta , \hat {\theta},\tag{9}
$$

$$
U ^ {B} (\theta) \geq 0, \quad \forall \theta ,\tag{10}
$$

with the corresponding (IC) and (IR) constraints (9) and (10), respectively. We observe one critical difference between pricing by B and pricing by M2 $U ^ { \scriptscriptstyle B } ( \theta , \hat { \theta } )$ is qualitatively the same as the original quadratic function and those utility functions specified in the literature with an additional term ${ \scriptstyle { \frac { 1 } { 2 } } } \delta ^ { 2 } \theta ^ { 2 }$ , whereas $U ^ { M } ( \theta , \hat { \theta } )$ is not a simple quadratic function anymore.

<sup>Lemma</sup> <sup>2.</sup> When the utility function is (1), under pricing by $B ,$ the optimal pricing plan is

$$
B ^ {*} (\theta) = \gamma (2 \theta - 1);
$$

$$
P ^ {B} (\theta) = \gamma \left(2 \theta - \frac {1}{2} - \theta^ {2}\right) + \underbrace {\frac {\underline {{\theta}} \gamma (2 \underline {{\theta}} ^ {2} - 6 \underline {{\theta}} + 3)}{2 (3 \underline {{\theta}} - 2)}} _ {\text { Fixed   Fee }};\tag{11}
$$

$$
\underline {{\theta}} = \frac {1}{4 \gamma + 3 \delta^ {2} \eta} (2 \gamma + \delta^ {2} \eta + \sqrt {\gamma \delta^ {2} \eta + \delta^ {4} \eta^ {2}}).
$$

The seller’s corresponding maximum expected profit is $\Pi ^ { B } =$ $\textstyle { \frac { 1 } { 6 } } \gamma - \underline { { \theta } } ^ { 2 } ( \gamma - \frac { 4 } { 3 } \underline { { \theta } } \dot { \gamma } + \frac { 1 } { 2 } \delta ^ { 2 } \eta - \underline { { \theta } } \delta ^ { 2 } \eta )$ and  is the lowest-type customer served by the seller.

All of these results are qualitatively similar to those in the nonlinear pricing literature. For example, the highest-type consumer (with $\theta = 1 )$ receives the welfare-maximizing connection speed, whereas all other types select degraded connection speeds. Although $\check { P } ^ { \hat { B } } ( \theta )$ looks complicated at first sight, it includes a constant term that corresponds to a fixed access fee to the data service (i.e., it does not depend on ). It can be verified that $\dot { P } ^ { B } ( \theta )$ is a concave function of $\theta ;$ furthermore, once we substitute  by $B ^ { * } ( \theta )$ $P ^ { B } ( B )$ is indeed a concave function. Thus, the seller provides discounts to consumers who subscribe to more expensive plans with faster speed.

## 4.3. Pricing by Gigs

Now suppose that the seller charges the consumers by data usage. In this case, the contract only specifies the data usage Q45 and the corresponding price $P ^ { Q } ( \theta )$ . Accordingly, a type- consumer has the discretion to select the composition of connection speed and minutes that collectively make her total data usage cap equal to $Q ( { \hat { \theta } } )$ . Given the pricing plan, essentially the consumer can choose B or M to maximize her net utility in Stage 4

$$
\begin{array}{c} U ^ {Q} (B \mid \theta , \hat {\theta}) = \delta \theta Q (\hat {\theta}) - \frac {1}{2 \eta} Q (\hat {\theta}) ^ {2} \\ + B \theta - \frac {1}{2 \gamma} B ^ {2} - P ^ {Q} (\hat {\theta}), \end{array}\tag{12}
$$

$$
Q (\theta) = B (\theta) \times M (\theta) \quad \forall \theta .
$$

Compared with (5) in Section 4.2, these two equations are qualitatively the same because of symmetry.

Similar to the other two cases, the consumer maximizes (13) by choosing B. It is straightforward to derive $B ^ { * } ( \theta ) = \gamma \theta$ . Substituting this term back to (13) leads to the following effective utility function in Stage 3:

$$
U ^ {Q} (\theta , \hat {\theta}) = \delta \theta Q (\hat {\theta}) - \frac {1}{2 \eta} Q (\hat {\theta}) ^ {2} + \frac {1}{2} \gamma \theta^ {2} - P ^ {Q} (\hat {\theta}).\tag{13}
$$

In Stage 2, the seller’s optimization problem in this case becomes

$$
\Pi^ {Q} = \max _ {Q (\theta), P ^ {Q} (\theta)} \mathbb {E} _ {\theta} [ P ^ {Q} (\theta) ]\tag{14}
$$

$$
\mathrm{s.t.} U ^ {Q} (\theta) \geq U ^ {Q} (\theta , \hat {\theta}), \quad \forall \theta , \hat {\theta},
$$

$$
U ^ {Q} (\theta) \geq 0, \quad \forall \theta .\tag{15}
$$

(16)

The optimal solution to the above optimization problem is summarized below.

<sup>Lemma</sup> <sup>3.</sup> When the utility function is (1), under pricing by Q, the optimal pricing plan is

$$
\begin{array}{c} Q ^ {*} (\theta) = \eta \delta (2 \theta - 1); \\ P ^ {Q} (\theta) = \eta \delta^ {2} \bigg (2 \theta - \frac {1}{2} - \theta^ {2} \bigg) + \frac {\delta^ {2} \eta \underline {{\theta}} (2 \underline {{\theta}} ^ {2} - 6 \underline {{\theta}} + 3)}{2 (3 \underline {{\theta}} - 2)}; \\ \underline {{\theta}} = \frac {1}{3 \gamma + 4 \delta^ {2} \eta} (\gamma + 2 \delta^ {2} \eta + \sqrt {\gamma^ {2} + \gamma \delta^ {2} \eta}). \end{array}\tag{17}
$$

The seller’s corresponding maximum expected profit is $\begin{array} { r } { \Pi ^ { Q } = \frac { 1 } { 6 } \eta \delta ^ { 2 } - \underline { { \theta } } ^ { 2 } ( \frac { 1 } { 2 } \overset { { \prime } } { \gamma } - \underline { { \theta } } \gamma + \delta ^ { 2 } \eta - \frac { 4 } { 3 } \underline { { \theta } } \delta ^ { 2 } \eta ) } \end{array}$

Solutions in Lemmas 2 and 3 are the same when we replace  by $\eta \delta ^ { 2 }$ . Having characterized the optimal pricing plans under different pricing metrics, we proceed to compare the seller’s expected profits in Section 4.4.

## 4.4. Comparison

We are now ready to derive the optimal pricing metric(s) in Stage 1. Our findings are summarized in the following proposition.

<sup>Proposition</sup> <sup>1.</sup> Suppose (1) approximates the consumers’ utility. We find the following:

1. Under pricing by M, the seller offers uniform pricing, whereas in the other two scenarios, the seller offers multitiered pricing plans at optimality.

2. Pricing by M is suboptimal.

3. Comparing pricing by Q and B, pricing by B is profit maximizing if and only i ${ \dot { \mathbf { \zeta } } } \ y \geq \delta ^ { 2 } { \boldsymbol { \eta } }$

The first implication of Proposition 1 is that pricing by M is inferior to the other two options. The main reason is that the after-sales selection by consumers provides too much leeway for consumers. Thus, pricing by M is relatively ineffective in screening among heterogeneous consumers.

Our result suggests that when the consumer preference is perfectly characterized in (1), pricing by Q or pricing by B is optimal. Although the equilibrium profit functions are complicated, the comparison result is neat. Pricing by B is more profitable than pricing by Q when $\gamma \geq \delta ^ { 2 } \eta$ . In the current setting, the (first-order) parameters of $\theta Q ( { \hat { \theta } } )$ and $\theta B ( { \hat { \theta } } )$ in (1) are  and 1, respectively. When $\delta < 1 .$ , the first concave function in Q is smaller than the second concave function in B. Therefore, pricing by B seems to be more attractive in this case. Regarding the secondorder parameters in (1), we can make a similar conjecture: when $\gamma \geq \eta .$ , the second concave function in B is generally larger. Formally, if we give the consumer full flexibility to self-select both Q and B, the maximal utilities of these two concave functions are $\scriptstyle { \frac { 1 } { 7 } } \eta \delta ^ { 2 } \theta ^ { 2 }$ and ${ \scriptstyle { \frac { 1 } { 2 } } } \gamma \theta ^ { 2 } .$ , respectively. Therefore, $\gamma \geq \delta ^ { 2 } \eta$ implies the potential profit from the second function is larger. We summarize the procedure to select the pricing metrics as follows.

## Observation 1.

1. We eliminate the options of metrics that leave too much flexibility to consumers, especially the metric that is always a multiplicative component of a more influential metric, such as M is part of Q in our baseline setup.

2. Among the remaining metrics, our additivity assumption allows us to consider the profit from two metrics separately. The seller then compares the price discrimination benefit from the chosen metric and the profit loss from the consumers’ overconsumption relative to the profitmaximizing level.

Our model provides one potential explanation regarding why residential ADSL is priced by Mbps, whereas 3G cellular ISPs use pricing by Q. At the same time, ISPs hesitate to move from pricing by Q to pricing by B in the 4G age. As we explained earlier, residential ADSL consumers are more heterogeneous in speed because of bandwidth sharing and heterogeneity in the applications they prefer (with a relatively smaller ). By contrast, users of 3G mainly use email or browsing, and they rarely share 3G bandwidth. Both suggest that 3G users are less heterogeneous in speed. Similarly, the utility derived directly from speed is less important than the utility derived from data usage. Therefore, ADSL should be priced by Mbps than by Gigs. The 4G services could provide the speed as fast as earlier ADSL did. However, U.S. operators unambiguously choose pricing by Q. This could result from the fact that there is no bandwidth sharing among multiple users or devices, and few consumers have developed the habit to use speed-demanding applications over their cell phones. Comparing the ADSL pricing versus 4G pricing suggests the explanation is more of demand side than of supply side, because 4G may have more bandwidth in its nascent stage with few adopters.

The discussion about the general applicability of this observation is in Section 5.1. Next, we will numerically investigate how three pricing metrics may affect consumer surplus, welfare, and a seller’s profit.

## 4.5. Numerical Example

This section reports the results of a numerical example to shed more light on our findings. The utility function solved in this example is given by

$$
u (B, M, \theta) = 2 B M \theta - \frac {1}{2} (B M) ^ {2} + B \theta - \frac {1}{2} B ^ {2}.
$$

In other words, $\delta = 2 , \eta = \gamma = 1$ . This implies that consumers value data usage more than connection speed. For ease of exposition, we provide graphic illustrations in Figures 1–3. In these figures, the solid line is the result from pricing by M, the dashed line is the result from pricing by B, and the dotted line is the result from pricing by Q.

Profit Comparisons. As in other price discrimination cases, under pricing by B or Q, consumers with high valuations are charged higher prices than in the single price scenario, whereas consumers with low valuations are charged lower prices; furthermore, the market coverage becomes larger. In our model, the seller’s profit of pricing either by B or by Q is higher than that in the single price case. A surprising result is that pricing by B is slightly more profitable than pricing by M (with uniform pricing). The seller’s profits under these three pricing metrics are 0.403 (by $Q ) >$ 0.377 (by $B ) > 0 . 3 \hat { 7 0 }$ (by M); the profit improvement using pricing by B over uniform pricing is 1.89%. By sharp contrast, the improvement is 8.92% from the optimal pricing metric Q over the second best metric B. This illustrates the importance of pricing metrics selection. A poorly chosen metric can be as ineffective as surrendering most price discrimination power.

Figure 1 Seller’s Profits Under Three Pricing Metrics  
![](/api/attachments/9G49JZ38/fulltext/images/08f9bb324860b75e2726f6ef75511710e4077d20728c5e39e2c769d528dd31d7.jpg)

Figure 2 Social Welfare Under Three Pricing Metrics  
![](/api/attachments/9G49JZ38/fulltext/images/939f61330d907aed8bd0a99029bfcd88b014ebcd2b8ef748f24d27793409bb97.jpg)

Figure 3 Consumer Surplus Under Three Pricing Metrics  
![](/api/attachments/9G49JZ38/fulltext/images/0d7b699a34c393422f34172c97c3c297fae4a535a7a2113dc6a9450fd577eb4c.jpg)

Welfare Implications. So far, we mainly focus on the revenue maximization from the seller’s perspective. Nevertheless, these pricing metrics also have strong implications on the consumer surplus and social welfare. To this end, we shall first characterize the socially optimal connection speed and data usages. We denote the solutions by superscript e. From the consumers’ utility functions in (1) and the fact that the seller incurs no variable cost of providing services, the socially optimal solutions should be<sup>11</sup>

$$
B ^ {e} (\theta) = \gamma \theta , \quad \text { and } \quad Q ^ {e} (\theta) = \eta \delta \theta ,
$$

(18)

where superscript e indicates the efficient levels. For ease of exposition, define $[ x ] ^ { + } = \operatorname* { m a x } [ x , 0 ]$ as the positive part for any x.

Comparing (18) to Lemmas 2 and 3, we observe a downward distortion

$$
B ^ {*} (\theta) = \gamma [ 2 \theta - 1 ] ^ {+}, \quad \mathrm{and} \quad Q ^ {*} (\theta) = \eta \delta [ 2 \theta - 1 ] ^ {+}.
$$

This is the standard distortion result from information asymmetry in the literature, and we provide a graphic illustration in Figure 2. Under pricing by M, the seller offers an unlimited usage plan. Accordingly, consumers will self-select the efficient usage and the welfare is therefore the highest. However, a welfare loss arises from the seller’s revenue maximization incentive because fewer consumers are served. Under the optimal pricing plan by Q, much more consumers with low valuations are served by low usage plans. The total welfare in the numerical example is 0.616 (by Q) > 0.593 (by B) > 0.586 (by M). In other words, price discrimination is beneficial to society in this example.

Consumer Surplus. Consumer surplus can be derived by substituting the solutions in each case into $u ( B , M , { \bar { \theta } } )$ in (1). Numerical results are shown in Figure 3. Consistent with the findings in the pricing literature, consumers with high valuations are worse off under price discrimination, whereas consumers with low valuations benefit. The total consumer surplus is 0.213 (by Q) < 0.2159 (by $B ) < 0 . 2 1 6 1$ (by M). In this example, the aggregate consumer surplus is lower under price discrimination, suggesting that the seller becomes the primary beneficiary of the increased welfare.

Profit Sensitivity in  and . We also numerically analyze how three parameters may affect the profitability of pricing metrics. First, we consider the case with $\eta = \gamma = 1$ while  is a variable. Now we can draw three curves to illustrate how profit may change with respect to . Our example suggests that pricing by M is indeed suboptimal while the profitability of the other two depends on the value of . The larger  is, the more profitable pricing by B. Moreover, our figure shows that when  has extreme values, selecting the right metric becomes more critical to the firm’s profit.

Figure 4 (Color online) Seller’s Profits versus   
![](/api/attachments/9G49JZ38/fulltext/images/1b095579e1d6964460d1bfa3d916c00d45c045416e0ee6920e95e147c5cf3943.jpg)

Figure 5 (Color online) Seller’s Profits versus   
![](/api/attachments/9G49JZ38/fulltext/images/1ad19dff05e4ae913b46f9047fab2989d72019fe517a7879bdb48598b872c8f1.jpg)

We next consider the case in which $\delta = \gamma = 1$ while  is a variable. In Figures 4 and 5, the three profitability curves are qualitatively similar to the previous example. The major difference is that in Figure $5 ,$ the curves are more concave than their counterparts in Figure 4. Although we have three parameters, the figure by varying  is qualitatively the same as Figure 5 when $\dot { \delta } = \check { 1 }$ . Therefore, this case is omitted for brevity.

## 5. Discussions and Extensions

In this section, we consider two variants of our model characteristics to evaluate the robustness of the results from our baseline model. We will investigate how variations in the utility functions and supply constraints affect the implications from our baseline model.

## 5.1. General Utility and Type Distribution

In the first extension, we accommodate the general utility function form and type distribution. The goal is to investigate under what general conditions our findings in the baseline model are still valid and also how the utility’s functional form may affect our results. We first start with a special case of utility function that illustrates the intrinsic reason that pricing by M is dominated by the other two pricing metrics in Section 5.1.1. In Section 5.2, we present a general formulation and highlight the underlying forces that lead to the differences in profitability from pricing by B or $Q .$

5.1.1. General Utility Function with Multiplicative Pricing Metrics. Suppose that the consumer’s utility function depends only on Q but is independent of M and $B , \mathsf { \bar { i } . e . , \mathsf { \Lambda } } U ( B , \mathsf { \bar { M } } , \theta ) \equiv U ( Q , \theta ) .$ , where $Q = B M$ . In such a scenario, this model degenerates to the standard nonlinear pricing model. We can show that the seller should simply choose Q as the pricing metric.

Proposition 2. <sub>If</sub> $U ( B , M , \theta ) \equiv U ( Q , \theta )$ , then pricing by $Q$ weakly outperforms pricing by M and by B.

To explain the rationale behind this proposition, it is helpful to review the optimality condition (firstorder condition) for deriving optimal pricing plans from the literature. Assuming $\bar { U ( Q , \theta ) }$ satisfies several general assumptions developed in the literatur $_ { ; , } ^ { ~ 1 2 }$ the following has been well documented.

Lemma 4. Suppose $U ( B , M , \theta ) \equiv U ( Q , \theta )$

1. The seller’s profit can be expressed as

$$
\begin{array}{l} \int_ {\underline {{\theta}}} ^ {1} P (\theta) d \theta \\ = \int_ {\underline {{\theta}}} ^ {1} \left[ U (Q, \theta) - \frac {\partial U (Q , \theta)}{\partial \theta} \frac {1 - F (\theta)}{f (\theta)} \right] ^ {+} d \theta , \end{array}\tag{19}
$$

where $\underline { { \theta } }$ is the lowest-type consumer who is served.

2. The optimal quantity plan $Q ^ { * } ( \theta )$ is determined by maximizing the integrand of (19) pointwise. Specifically, if the integrand is increasing in Q, then the optimal solution of Q is the upper bound of Q. If the integrand is a concave function, the optimal solution of Q is determined by the first-order condition.

3. Given $Q ^ { * } ( \theta )$ , the optimal pricing plan P for type  is determined by the following formula:

$$
P (\theta) = U (Q ^ {*} (\theta), \theta) - \int_ {\theta} ^ {\theta} \frac {\partial U (Q , t)}{\partial t} d t.
$$

Please refer to Grubb (2009), Maskin and Riley (1984), and Sundararajan (2004b) for the detailed assumptions and proofs. All of our baseline results can be derived by this lemma. This result allows us to better explain the proof of Proposition 2 in a succinct way. The optimal data usage plan is determined by the following equation as stated in the lemma:

$$
\max _ {Q} \left[ U (Q, \theta) - \frac {\partial U (Q , \theta)}{\partial \theta} \times \frac {1 - F (\theta)}{f (\theta)} \right] ^ {+}.
$$

This is weakly larger than

$$
\max _ {B \text {   or   } M} \left[ U (B M, \theta) - \frac {\partial U (B M , \theta)}{\partial \theta} \times \frac {1 - F (\theta)}{f (\theta)} \right] ^ {+},
$$

irrespective of what the consumers choose for M or B in Stage 4.

Intuitively, under pricing by $Q ,$ although consumers can still choose the values of either M or $B ,$ they cannot effectively affect the utility function. This is because $Q$ is the only variable that affects the utility function, and it is also the only term specified by the seller in the pricing contract. By contrast, if the seller prices by B or $\begin{array} { r } { \bar { \cal M } , } \end{array}$ the self-selection in Stage 4 can only adversely affect the seller’s profit maximization. Therefore, in this case, Q is the optimal pricing metric.

5.1.2. General Formulation to Quantify the Self-Selection Effects. We now generalize the utility function to the following one:

$$
U = U ^ {Q} (Q, \theta) + U ^ {B} (B, \theta),\tag{20}
$$

where each utility function is increasingly concave and it satisfies other regularity conditions in the nonlinear pricing literature. Applying Lemma 4, the seller’s profit function is given by

$$
\begin{array}{l} \int_ {\underline {{\theta}}} ^ {1} \bigg [ \underbrace {U ^ {Q} (Q , \theta) + U ^ {B} (B , \theta)} _ {\text {   Consumer   Surplus   }} \\ \qquad - \underbrace {\frac {\partial}{\partial \theta} [ U ^ {Q} (Q , \theta) + U ^ {B} (B , \theta) ] \times \frac {1 - F (\theta)}{f (\theta)}} _ {\text {   Information   Rent   }} \bigg ] ^ {+} d \theta . \end{array}
$$

In this equation, the first two terms in the integrand are simply the consumer’s utility function. If the seller can identify each consumer’s type and conduct firstdegree price discrimination, his profit is simply the sum of the first two terms. Information asymmetry inevitably reduces the seller’s profit and forces him to leave some surplus to consumers; this is labeled as the information rent in the literature and is captured by the last two terms (Maskin and Riley 1984).

Equation (20) is a generalized form of (1) in our baseline setup. Similar to Proposition $^ { 4 , }$ we can still show that pricing by M is suboptimal, because M is a multiplicative component of Q in the utility function.

Proposition 3. <sub>If</sub> $U ( B , M , \theta ) \equiv U ^ { Q } ( Q , \theta ) + U ^ { B } ( B , \theta )$ then pricing by M is weakly worse than pricing by Q.

Next, we investigate the profitability between pricing by Q or B. Take the pricing by B as an example. In Stage 4, each consumer self-selects Q to maximize her own utility $U ^ { Q } ( Q , \theta )$ and the solution is the efficient usage $Q ^ { e } ( \theta ) = \operatorname { a r g }$ max $U ^ { Q } ( Q , \theta )$ . Substituting it back to the seller’s profit function, we obtain the following expression:

$$
\begin{array}{l} \max _ {B (\theta)} \Pi^ {B} = \int_ {0} ^ {1} \left[ \underbrace {U ^ {Q} (Q ^ {e} , \theta)} _ {\text { 1st   Effect }} - \underbrace {\frac {\partial U ^ {Q} (Q ^ {e} , \theta)}{\partial \theta} \frac {1 - F (\theta)}{f (\theta)}} _ {\text { 2nd   Effect }} \right. \\ \left. + \underbrace {U ^ {B} (B , \theta) - \frac {\partial U ^ {B} (B , \theta)}{\partial \theta} \times \frac {1 - F (\theta)}{f (\theta)}} _ {\text { 3rd   Effect }} \right] ^ {+} d \theta . \end{array}\tag{21}
$$

This expression succinctly summarizes three effects in this model. Note that the seller can only choose B and can directly influence only the third effect, whereas the first two effects are “decided” by the consumers. First, when a pricing metric is not specified in the contract, the consumer will self-select it at the welfare-maximizing (first-best) level. This exceeds the profit-maximizing (second-best) level as various researchers have shown. Second, consumers’ self-selection in Stage 4 makes the resulting utility function more sensitive to  $( \mathrm { i . e . , } \partial U ^ { Q } / \partial \theta$ is larger because Q is larger than the second-best level). This exacerbated heterogeneity among consumers makes it more costly for the seller to conduct second-degree price discrimination, and consequently the seller has to pay more information rent. The third effect is the traditional price discrimination effect. It coincides with the seller’s profit function in Lemma $^ { 4 , }$ and can be interpreted as the isolated effect wherein the seller ignores the consumer’s after-sales self-selection.

For ease of exposition, let us denote the profitmaximizing level by $Q ^ { \pi } ( \theta )$ and $B ^ { \pi } ( \theta )$ . Equation (21) vividly summarizes the conflict between the seller and the consumers. The seller can use the pricing plan to induce consumers to choose the profit-maximizing $B ^ { \pi } ( \theta )$ and leave the flexibility for the consumers to choose $Q ^ { e } ( \theta )$ , which can be shown to be larger than $Q ^ { \pi } ( \theta )$ and the overconsumption leads to a lower profit level. If the seller prices by $Q ,$ the situation reverses: the seller chooses $Q ^ { \pi } ( \theta )$ and the consumer chooses $B ^ { e } ( \theta )$ 1 which is again larger than $B ^ { \pi } ( \theta )$ . In general, the seller needs to balance the gain and loss of three effects to decide the total profit between $[ B ^ { \pi } ( \theta ) , Q ^ { e } ( \theta ) ]$ versus $[ B ^ { e } ( \theta ) , Q ^ { \pi } ( \theta ) ]$ . Our baseline criterion in Proposition 1 may be applicable only to quadratic utility functions. In general, the seller has to balance the loss in the first two terms and the gain from the last two terms to decide the optimal pricing metric.

Decomposing the total profit into three terms in (21) also produces a valuable by-product. When $\partial U ^ { B } ( B , \theta ) / \partial \theta \mathrm { o r } \partial U ^ { Q } ( Q ^ { e } , \theta ) / \partial \theta$ is zero, pricing by Q or B is optimal, respectively. This result can be deduced without proof because (21) already shows that when $\partial U ^ { Q } ( Q ^ { e } , { \bf \dot { \theta } } ) / \partial \theta = 0 .$ 1 the integrand is already optimized; there is no downside to let the consumers selfselect Q.

Proposition 4. <sub>If</sub> $U ( B , M , \theta ) \equiv U ^ { Q } ( Q , \theta ) + U ^ { B } ( B ) .$ then pricing by Q is more profitable than pricing by B. Similarly, $\breve { i f } U ( B , M , \theta ) \equiv \dot { U } ^ { Q } ( B , \theta ) + U ^ { B } ( \stackrel { . } { Q } )$ , then pricing by B is more profitable than pricing by Q.

A number of real-world pricing problems that do not meet the assumptions of our baseline model could be solved by Proposition 4. Note that in (20), our specification of utility function only comprises two pricing metrics. Therefore, our analysis can be applied to those applications with only two natural pricing metrics. For example, fixed-line telephone services could be priced by the number of phone calls or the total minutes of phone calls. To decide the profitmaximizing metric, the telecommunication company can evaluate the gain from price discrimination by one metric and the loss from overconsumption (relative to the profit-maximizing level) by the other metric using the methodology provided in this section. Long-distance fixed-line telephones are mostly priced by time usage because consumers’ utility function may have a larger proportion in total time usage than in the number of phone calls. By contrast, local fixed-line phone pricing provides a good contrasting example. When consumers place local phone calls, the number of phone calls is relatively more important than total time usage.

As another interesting example, hotels typically charge ISP services by time usage, not by speed or even data usage. This is in sharp contrast to residential ISP and our analysis provides one possible reason. Most hotel guests need the Internet primarily for emails and browsing (so speed becomes secondary) and they may need to check emails daily. Therefore, consumers are more concerned about time usage and they care less about data usage in this context. This leads to the phenomenon that pricing by time usage such as “number of days” becomes more profitable than pricing by data usage.

## 5.2. Supply Side Constraints

In this section, we incorporate the supply side constraints into our setup.

5.2.1. Aggregated Bandwidth Costs. In our basic framework, we focus exclusively on the demand side concerns, leaving the supply side issues unaddressed. A notable issue is the presence of aggregate bandwidth capacity constraint, which is particularly crucial for dial-up or 3G wireless broadband connections. To incorporate the bandwidth capacity concern, we assume the seller incurs a fixed cost for improving its infrastructure to provide bandwidth capacity. The new profit function is therefore

$$
\Pi = \max _ {B (\theta), P ^ {B} (\theta)} \left\{\mathbb {E} _ {\theta} [ P ^ {B} (\theta) ] - C (T) \right\},\tag{22}
$$

where $\begin{array} { r } { T = \int _ { \underline { { \theta } } } ^ { 1 } B ( \theta ) } \end{array}$ d represents the seller’s total bandwidth capacity.

In this scenario, the selection of pricing metrics and the design of pricing plans must take into account this supply constraint. In the nonlinear pricing literature, it has been documented that the convex cost function C4T 5 gives rise to an endogenously determined constant variable cost (Huang and Sundararajan 2011). This variable cost corresponds to the “shadow price,” i.e., the incremental benefit that the seller obtains while marginally increasing the bandwidth capacity. Equation (22) is equivalent to a pricing problem with a constant variable cost on B as follows:

$$
\Pi = \max _ {B (\theta), P ^ {B} (\theta)} \mathbb {E} _ {\theta} [ P ^ {B} (\theta) - \lambda B (\theta) ],\tag{23}
$$

where  is the Lagrange multiplier associated with the total bandwidth constraint. In other words, this setup also covers the extensions in which there is a constant variable cost associated with the pricing metric.

It can be verified that the solution procedures in Stages 3 and 4 are entirely the same. Even in Stage 2, the solutions about pricing by M and Q are still the same because the seller cannot choose B, which is chosen by the consumers in Stage 4 to maximize the utility function. Therefore, pricing by M is still suboptimal and only the solution of pricing by B is different. As a result, the relative profitability between pricing by Q and pricing by B is different from that in the baseline case. Our main finding is summarized in the following proposition.

<sup>Proposition</sup> <sup>5.</sup> Suppose that the utility function is given by (1), and the seller incurs a fixed cost function in the total bandwidth. Pricing by M is still the least profitable pricing option. Pricing by B becomes relatively more profitable than pricing by Q, relative to Proposition 1.

The intuition is as follows. Under pricing by B, the seller can set higher prices per Mbps to balance the marginal revenue and the marginal cost that results from C4T 5. However, under other pricing metrics, B is not controlled by the seller but is chosen by the consumers. Thus, the equilibrium choice of B maximizes the consumer’s utility but does not internalize the infrastructure cost C4T 5. Proposition 5 suggests the following. As long as there is a fixed cost that is a function of the sum of one particular pricing metric, the seller’s incentive to use that pricing metric is strengthened. Because Huang and Sundararajan (2011) show that (22) is equivalent to a pricing problem with a constant variable cost on $B ,$ a variable cost in pricing metric also increases the seller’s profit from using that pricing metric. In the ISP context, it seems that only the connection speed B contributes to the operating cost; this subsequently provides one more incentive for the seller to choose pricing by B. In different kinds of service pricing, costs may be a function of the total amount or the number of transactions, leading to the possibility of optimal pricing plans using different metrics.

At first glance, Proposition 5 may look inconsistent with the residential ADSL pricing: the total bandwidth is quite sufficient but ISPs price by B, whereas bandwidth constrained mobile service providers price by Q. One possibility is that the ADSL service over a fiber optic network is more expensive than the mobile ISP infrastructure. The other conjecture is that the demand-side effects may have dominated this supply side effect. In practice, as data communication technology advances, the bandwidth limitation for each consumer will be relaxed. The number of applications available in the market also increases sharply. Therefore, the shape of the utility function becomes quite different in speed and data usage.

Take the residential ADSL in 2012 as an example. According to Forrester (Anderson 2010), more and more consumers may need connection speeds faster than a threshold to use streaming videos, Skype, virtual world, P2P applications, real-time gambling, or multiplayer online games. Some families or small companies may need to share the bandwidth with more than five members. These emerging applications make consumers more heterogeneous in their preferences over connection speed, because some consumers may still use ADSL for emails and basic browsing. As a result, pricing by Q could be less profitable for ADSL. In sharp contrast, by dialup or 3G data services, consumers mostly use emails and basic browsing features. In the dialup age, consumers may not have heterogeneous preference over speed at all because no speed-demanding applications are available.

Pushing this idea further, we note that in the utility function, consumers are more heterogeneous about the data usage than speed ( is larger); therefore, pricing by Q is more profitable.<sup>13</sup> In recent years, ISPs attempted to move to pricing by Q because if all consumers have already adopted speed demanding

$$
u (B, M, \theta) = \delta \theta Q - \frac {1}{2} Q ^ {2} + \frac {1}{\gamma} B,
$$

applications, their preference could become more heterogeneous in Gigs than in Mbps. Therefore, residential ISPs may realize that if approved by regulators, it will be more profitable to price by Gigs.

5.2.2. Disutility of Waiting. In reality, the usage of a consumer may impose negative externality on others. For example, in the ISP pricing application, consumers may have to wait for a long time when there are many consumers due to the limited bandwidth. This creates the disutility of waiting and shall be incorporated in our model. To this end, we follow the approach of Masuda and Whang (2006) to incorporate the disutility of waiting via the modified utility function

$$
u (B, M, \theta) = \delta \theta B M - \frac {1}{2 \eta} (B M) ^ {2} + \theta B - \frac {1}{2 \gamma} B ^ {2} - Q \times C (T),\tag{24}
$$

where $\textstyle T = \int _ { \theta } ^ { 1 } B ( \theta ) d \theta$ is the total connection speed and C is a continuously increasing, convex cost function. The addition of the last term represents the disutility of waiting.

There are two main differences between (22) and (24). First, (22) includes an additional cost term, whereas (24) includes an additional disutility, relative to the baseline model. Second, (22) includes a fixed cost that is theoretically equivalent to a constant variable cost. By contrast, disutility in (24) is proportional to data usage. Notably, while Masuda and Whang (2006) focus on the two-type case to show the equivalence between FUT pricing and the optimal pricing plan, we allow for a continuum of consumer types.

Given this setup, we can show the following:

<sup>Proposition</sup> <sup>6.</sup> Suppose the utility function is given by (24). Pricing by M is still the least profitable pricing option. Pricing by B becomes relatively more profitable than pricing by Q, relative to Proposition 1.

The intuition behind this proposition is as follows: when pricing by M or Q, consumers self-select B in the last stage. This self-selection is qualitatively the same as that in our baseline model: a consumer’s selection of B will not affect T because she is infinitesimal (Masuda and Whang 2006). Returning to Stage 2, the seller’s price discrimination problem is qualitatively the same as that in the baseline case. Therefore, single pricing is still optimal under pricing by M because the self-selection is too strong. When the seller prices by Q, the results are qualitatively similar after we incorporate the terms associated with $Q \times C ( T )$ . The optimal pricing by B becomes more complicated. First, in Stage 4, consumers will choose a smaller data usage because of $- Q \times C ( T )$ . This then leads to a different stage 2, because C4T 5 depends on $\textstyle { \int _ { \theta } ^ { 1 } B ( \theta ) d \theta }$ and B45 can be manipulated by the seller directly. Despite this difficulty, we are able to show that the profit in this case becomes relatively larger than that from pricing by Q.

<table><tr><td colspan="4">Table 1 Summary of Results</td></tr><tr><td>Case</td><td>Utility function</td><td>Cost function</td><td>Optimal metric selection</td></tr><tr><td>1</td><td> $U^{Q}(Q, \theta)$ </td><td>n.a.</td><td> $Q$  is more profitable than  $B$  and  $M$ .</td></tr><tr><td>2</td><td> $U^{Q}(Q, \theta) + U^{B}(B, \theta)$ </td><td>n.a.</td><td> $M$  is suboptimal. Either  $Q$  or  $B$  could be optimal.</td></tr><tr><td>3</td><td> $U^{Q}(Q, \theta) + U^{B}(B)$ </td><td>n.a.</td><td> $Q$  is more profitable than  $B$  and  $M$ .</td></tr><tr><td>4</td><td> $U^{Q}(Q, \theta) + U^{B}(B, \theta)$ </td><td> $C(\int_{\theta}^{1} B(\theta) d\theta)$ </td><td> $M$  is suboptimal.  $B$  is more profitable than case 2.</td></tr><tr><td>5</td><td> $U^{Q}(Q, \theta) + U^{B}(B, \theta)$ </td><td> $C \times B$ </td><td> $M$  is suboptimal.  $B$  is more profitable than case 2.</td></tr><tr><td>6</td><td> $U^{Q}(Q, \theta) + U^{B}(B, \theta) - QC(\int_{\theta}^{1} B(\theta) d\theta)$ </td><td>n.a.</td><td> $M$  is suboptimal.  $B$  is more profitable than case 2.</td></tr></table>

Since the disutility term depends on both Q and $B ,$ one may conjecture that the dominance of pricing by B or Q requires very different conditions from those in 1. Nevertheless, this conjecture is not true because of the important role of the consumers’ Stage 4 self-selection. First, the new term $Q \times C ( T )$ does not depend on  directly and therefore it does not affect the cannibalization problem under price discrimination (no second effect in (21)). Rather, $Q \times C ( T )$ affects the first and third effects identified in Section 5.1.2. Under pricing by Q, consumers self-select the connection speed $B ,$ leading to a more serious congestion problem. The benefit of this pricing plan is that the seller can directly balance the cost and benefit of $Q \times C ( T )$ in the third effect. At the same time, the shortcoming is that the seller can only indirectly alleviate the delay cost C4T 5 by charging higher prices on Q.

By contrast, underpricing by B, he directly adjusts the pricing plans to mitigate the congestion problem, whereas the impact of $Q \times C ( T )$ is controlled by consumers in Stage 4 (effect 1). Because $Q \times C ( T )$ does not depend on $\theta ,$ there is no conflict of interests between the seller and consumers, as they both intend to maximize the consumers’ benefit in either effect 1 or effect 3. Consequently, the benefit of pricing by Q disappears, leading to the dominance of pricing by B.

## 6. Conclusions

In this paper, we investigate the selection of pricing metrics and the design of pricing plans for the sellers of data services. We observe that the pricing metric selection crucially depends on the role of pricing metrics in the utility function, and the after-sales consumer behavior is influential in the seller’s profitability. Please refer to Table 1 for the summary of results. The after-sales selection allows the consumers to maximize their own utility functions by choosing pricing metrics not specified in the pricing contract. Typically, consumers will consume much more than the profit-maximizing level, adversely impacting the seller’s profit. We show that in the extreme case, a pricing metric, such as time usage in the baseline case (case 2 in Table 1), may not provide any additional profits from price discrimination. This conclusion is reached under the utility assumption specified in Table 1. In some applications, such as Skype pricing or ISP pricing during hotel stays, time usage may play a more important role in the utility function. For example, we can replace B by M in cases 1, 2, and 3 of Table 1 and pricing by time usage may become the profit-maximizing choice. One shall be cautious when applying these results for a practical pricing problem.

At a higher level, our analysis suggests that when considering among the options of pricing metrics, the seller should balance three effects. The first effect is traditional price discrimination. The second effect is aftersales self-selection. It can increase the willingness-topay for data services, similar to an “all-you-can-eat” option in other pricing contexts. For any unspecified metrics, consumers will self-select to maximize their own utility. Third, however, the associated increase in utility aggravates information asymmetry because higher-type consumers with heavier usage will gain much more than lower-type users. This increases heterogeneity among consumers and reduces profit from second-degree price discrimination.

Our model may be extended in a couple of ways. First, for simplicity, we do not impose an upper bound on the pricing metrics in our current analysis. Instead, consumers will consume at the satiation level of a pricing metric that is not specified in the pricing contract. In the ISP practice, even if a metric is not specified as the pricing basis in the contract, that metric may face an artificial or technological upper limit when the user self-selects after sales. For example, when pricing by data usage, speed may be capped artificially by the ISP or there is a technical limit of speed. Our conjecture is as follows. If the limit is smaller than the profit-maximizing level, then the seller may not choose this metric because leaving it for consumers to self-select does not create conflict with the seller. If the limit is between the profit-maximizing level and the satiation level (the level solved in the current paper), then this upper limit alleviates the conflict between the seller and the consumer. In other words, when being left unused this metric becomes less harmful.

Second, we assume that consumers can perfectly predict how much they will use the services. In some scenarios, it is possible that while signing the contract, consumers face future uncertainties and consequently ex post usages may be different from their ex ante estimates (see Grubb 2009 and Jain and Kannan 2002). Conceivably, consumers are more inclined to pay more for the pricing plans that lead to a lower variance of future payment. Hence, the seller should price by the metric that leads to a smaller variance in future payments. At the same time, as illustrated in our paper, the after-sales consumer behavior may have significant impacts on the effective utility function. Therefore, the seller should also consider which metric can mitigate the consumer risk because of their after-sales self-selection behavior.

Third, we shall also acknowledge that in the literature there is another way to explicitly incorporate the queuing feature in the nonlinear pricing setup to model bandwidth congestion costs, e.g., Afèche and Mendelson (2004). However, in this line of study, the majority of the authors’ effort is devoted to characterizing the performance evaluation of the underlying queuing problem, because this significantly influences what kind of quality of service guarantee the seller can provide, and what portion of consumers will endogenously join the system in equilibrium. Including queuing features is certainly interesting, and it shall generate novel and nonoverlapping insights to the metrics selection problem.

Fourth, consumers may be heterogeneous along different dimensions (such as sensitivities to total usage, speed, and time), and these sensitivities may not be perfectly correlated. For example, among consumers who only use basic browsing and email services (not sensitive in speed), some may be more sensitive in usage than others. This case is ruled out in the single-dimensional setup. Despite its generality, multidimensional setup is rarely adopted in the overwhelming majority of the literature because of the tractability concern (Rochet and Stole 2003, Armstrong and Rochet 1999, Armstrong 2000, and Asker and Cantillon 2008). At the same time, to our knowledge, no contemporary pricing plan of data services simultaneously specifies more than one pricing metric. Extending along this direction is challenging.

Finally, it is also intriguing to evaluate the consumers’ psychological reactions to the pricing metrics. For example, consumers prefer “simple” pricing plans. However, analytical modeling studies seem to lack consensus regarding how to quantify the simplicity of pricing plans, or how to incorporate bounded rationality of consumers into mainstream economics models. Also, consumers may perceive different levels of fairness attached to distinctive pricing metrics. In practice, it is perceived as unfair for airlines to price by volume or by weight of a passenger but it is perceived as fair to price air freight cargos by volume or by weight. Incorporating behavioral issues into pricing is an important future research direction for pricing analytical studies.

## Acknowledgments

The authors thank the review team for their detailed comments and many valuable suggestions that have significantly improved the quality of the paper. The first author is partially supported by Hong Kong Research Grants Council [Grants 616613, 16206814, and 16502815]. The second author is partially sponsored by the Singapore Ministry of Education [Grant R253-000-103-112]. Authorship is in alphabetical order. The second author is the corresponding author. All the remaining errors are those of the authors.

## Appendix. Proofs

<sup>Proof</sup> <sup>of</sup> <sup>Lemma</sup> <sup>1.</sup> The consumer’s problem in Stage 4 is to choose a connection speed B that maximizes her utility. Because both quadratic functions in the utility function are always increasing and concave when $M ( { \hat { \theta } } )$ is fixed, we cannot derive the maximizer directly by $\partial U ^ { M } ( B | \theta , \hat { \theta } ) / \partial B = 0$ The reason is that the derivatives of $\delta \theta B M ( \hat { \theta } ) - ( 1 / ( 2 \eta ) )$ $( B M ( { \hat { \theta } } ) ) ^ { 2 }$ and the derivative of $\theta B - ( 1 / ( 2 \gamma ) ) B ^ { 2 }$ are always greater than or equal to zero. The maximizer is determined by finding the $B ^ { * } ( \theta , \hat { \theta } )$ that makes both derivatives zero. Otherwise, a larger B always increases the objective function.

The maximizer of $\dot { \delta } \theta B M ( \hat { \theta } ) - ( 1 / ( 2 \eta ) ) ( B M ( \hat { \theta } ) ) ^ { 2 }$ is $B =$ $\eta \delta \theta / M ( { \hat { \theta } } )$ and the maximizer of $\theta B - ( 1 / ( 2 \gamma ) ) B ^ { 2 }$ is $B = \theta \gamma$ $\mathrm { A s }$ a result, the overall maximizer of $U ^ { M } ( B \mid \theta , \hat { \theta } ) / \partial B$ is given by

$$
B ^ {*} (\theta , \hat {\theta}) = \max \left(\frac {\eta \delta \theta}{M (\hat {\theta})}, \theta \gamma\right).
$$

In fact, all values greater than $B ^ { * } ( \theta , \hat { \theta } )$ will lead to the same value of the objective function. For simplicity, we choose the smallest value as the optimal solution. The maximal value of the objective function is the sum of the maximal values of two quadratic functions because after the satiation value of $B ,$ both objective functions’ values are the same. Therefore

$$
U ^ {M} (B ^ {*} \mid \theta , \hat {\theta}) = \frac {1}{2} \eta \delta^ {2} \theta^ {2} + \frac {1}{2} \gamma \theta^ {2} - P ^ {M}.
$$

To simplify our expression, we now define a constant $Y \equiv$ ${ \textstyle \frac { 1 } { 7 } } \eta \delta ^ { 2 } + { \textstyle \frac { 1 } { 7 } } \gamma$ . The effective utility function is transformed to $\bar { U } ^ { M } ( M , \mathbf { \bar { \theta } } ) = \theta ^ { 2 } Y$ . By the versioning literature, uniform pricing is optimal because the consumers cannot be separated by screening by M.

Next, we will solve the optimal uniform pricing $P ^ { M } ,$ . The marginal consumer who feels indifferent between buying or not is determined by

$$
U ^ {M} (B ^ {*} \mid \theta , \hat {\theta}) = 0 \Leftrightarrow \frac {\theta^ {2}}{2} (\eta \delta^ {2} + \gamma) - P ^ {M} = 0.
$$

Therefore, the marginal consumer type is given by $\theta =$ $\sqrt { { 2 P ^ { M } } / { ( \eta \delta ^ { 2 } + \gamma ) } }$ . The objective function for profit maximizing becomes max M $P ^ { M } \times ( 1 - \sqrt { 2 P ^ { M } / ( \eta \delta ^ { 2 } + \dot { \gamma } ) } )$ . The optimal solution for $P ^ { M }$ and the seller’s profit are stated in Lemma 1 in Section 4.1 <sup></sup>

<sup>Proof</sup> <sup>of</sup> <sup>Lemma 2.</sup> The proof is the same as that in Lemma 1. We again start with Stage 4 in which the consumer decides the optimal M given the value of B chosen in Stage 3. The problem is easier than that in Lemma 1 because we only need to maximize one, not two, quadratic functions. The necessary condition to characterize the optimal M is given by

$$
\frac {\partial U ^ {B} (M \mid \theta , \hat {\theta})}{\partial M} = \delta B (\hat {\theta}) \theta - \frac {1}{\eta} B (\hat {\theta}) ^ {2} M,
$$

which suggests that the optimal solution is an interior solution $\bar { M } ( \theta , \hat { \theta } ) = ( \delta \eta \theta ) / \bar { B ( \theta ) }$ . Substituting this solution into (5), it follows that

$$
\begin{array}{c} U ^ {B} (\theta , \hat {\theta}) = \delta \theta B (\hat {\theta}) \frac {\delta \eta \theta}{B (\hat {\theta})} - \frac {1}{2 \eta} \bigg [ B (\hat {\theta}) \frac {\delta \eta \theta}{B (\hat {\theta})} \bigg ] ^ {2} \\ + B (\hat {\theta}) \theta - \frac {1}{2 \gamma} B (\hat {\theta}) ^ {2} - P ^ {B} (\hat {\theta}), \end{array}
$$

which equals to $( 7 )$ and is the effective consumer’s utility function for the seller’s maximization problem in Stage 2. Note that in this case, the effective utility function is qualitatively a quadratic function of $B ( \hat { \theta } )$ and is qualitatively the same as stylized nonlinear pricing models with quadratic utility functions. It can be verified that this effective utility function satisfies all assumptions requested by the nonlinear pricing literature and we can directly apply the theorems (results) of the literature. As a result, by Lemma 4 in Section 5.1.1, the seller’s expected profit is given by

$$
\begin{array}{c} \mathbb {E} _ {\theta} [ P ^ {B} (\theta) ] = \int_ {0} ^ {1} \biggl [ \frac {1}{2} \eta \delta^ {2} \theta^ {2} + B (\theta) \theta - \frac {1}{2 \gamma} B (\theta) ^ {2} \\ - (\eta \delta^ {2} \theta + B (\theta)) (1 - \theta) \biggr ] ^ {+} d \theta , \end{array}
$$

which can be rewritten as

$$
\mathbb {E} _ {\theta} [ P ^ {B} (\theta) ] = \int_ {0} ^ {1} \left[ \eta \delta^ {2} \theta \left(\frac {3}{2} \theta - 1\right) + (2 \theta - 1) B (\theta) - \frac {1}{2 \gamma} B (\theta) ^ {2} \right] ^ {+} d \theta . \tag {25}\tag{25}
$$

The integrand is still a concave function of $B ( \theta )$ . By pointwise maximization, the interior solution is

$$
B ^ {*} (\theta) = \gamma (2 \theta - 1),
$$

which is positive if and only if $\theta \ge 1 / 2$ . The cutoff level  (marginal, lowest-type customer served by the seller) is determined by equating the integrand to zero

$$
\eta \delta^ {2} \underline {{\theta}} \left(\frac {3}{2} \underline {{\theta}} - 1\right) + \frac {\gamma}{2} (2 \underline {{\theta}} - 1) ^ {2} = 0.
$$

The seller’s expected profit is derived by

$$
\int_ {\underline {{\theta}}} ^ {1} \left\{\eta \delta^ {2} \theta \left(\frac {3}{2} \theta - 1\right) + \frac {\gamma}{2} (2 \theta - 1) ^ {2} \right\} d \theta ,\tag{26}
$$

and the indefinite integral is given by $ \begin{array} { l } { { \frac { 1 } { 6 } } \theta { \left( 3 \gamma - 6 \theta \gamma + 4 { \theta } ^ { 2 } \gamma - \right.} \end{array}  }$ $3 \theta \delta ^ { 2 } \eta + 3 \theta ^ { 2 } \delta ^ { 2 } \eta )$ . When $\theta = 1 ,$ this term simplifies to ${ \scriptstyle { \frac { 1 } { 6 } } } \gamma .$ When $\theta = \underline { { \theta } } ,$ , this expression does not have a neat expression. We report the simplest expression in Lemma 2. <sup></sup>

<sup>Proof</sup> <sup>of</sup> <sup>Lemma</sup> <sup>3.</sup> This case is qualitatively very similar to the pricing by B case. In Stage 4, the consumers will self-select a connection speed that maximizes their utilities: $B ^ { * } = \theta \gamma$ . As a result, the effective utility function is given by

$$
U ^ {Q} (\theta , \hat {\theta}) = \delta \theta Q (\hat {\theta}) - \frac {1}{2 \eta} Q (\hat {\theta}) ^ {2} + \frac {1}{2} \gamma \theta^ {2} - P ^ {Q} (\hat {\theta}).
$$

We can follow the same approach in the preceding proofs. By Lemma 4 in Section 5.1.1, the seller’s expected profit is expressed as follows: The seller’s expected profit is given by

$$
\begin{array}{r} \mathbb {E} _ {\theta} [ P ^ {Q} (\theta) ] = \int_ {0} ^ {1} \bigg [ \delta \theta Q (\theta) - \frac {1}{2 \eta} Q (\theta) ^ {2} + \frac {1}{2} \gamma \theta^ {2} \\ - [ \delta Q (\theta) + \gamma \theta ] (1 - \theta) \bigg ] ^ {+} d \theta , \end{array}\tag{27}
$$

which can be simplified to

$$
\mathbb {E} _ {\theta} [ P ^ {Q} (\theta) ] = \int_ {0} ^ {1} \left[ \gamma \theta \left(\frac {3}{2} \theta - 1\right) + \delta (2 \theta - 1) Q (\theta) - \frac {1}{2 \eta} Q (\theta) ^ {2} \right] ^ {+} d \theta\tag{28}
$$

The integrand is a concave function of $Q ( \theta )$ . Therefore, it is maximized at $Q ^ { * } ( \theta ) = \eta \delta ( 2 \theta - 1 )$

Substituting back to the profit function yields

$$
\int_ {\underline {{\theta}}} ^ {1} \left[ \gamma \theta \left(\frac {3}{2} \theta - 1\right) + \frac {\eta \delta^ {2}}{2} (2 \theta - 1) ^ {2} \right] ^ {+} d \theta .\tag{29}
$$

The cutoff level  is determined by equating the integrand to zero: $\underline { { \theta } } = ( 1 / ( 3 \gamma + 4 \delta ^ { 2 } \eta ) ) ( \gamma + \dot { 2 } \delta ^ { 2 } \bar { \eta } + \sqrt { \dot { \gamma } ^ { 2 } + \gamma \delta ^ { 2 } \eta } )$ . The indefinite integral is given by

$$
\begin{array}{r l} & {\int \left(\gamma \theta \bigg (\frac {3}{2} \theta - 1 \bigg) + \frac {\eta \delta^ {2}}{2} (2 \theta - 1) ^ {2}\right) d \theta} \\ & {\qquad = \frac {1}{6} \theta (3 \theta^ {2} \gamma - 3 \theta \gamma + 3 \delta^ {2} \eta - 6 \theta \delta^ {2} \eta + 4 \theta^ {2} \delta^ {2} \eta),} \end{array}
$$

which equals to $\eta \delta ^ { 2 } / 6$ at $\theta = 1$ . At $\theta = \underline { { \theta } } ,$ it equals $\underline { { \theta } } ^ { 2 } \big ( { \textstyle { \frac { 1 } { 2 } } } \gamma -$ $\begin{array} { r l r } { \underline { { \theta } } \gamma + \delta ^ { 2 } \eta - \frac { 4 } { 3 } \underline { { \theta } } \delta ^ { 2 } \eta ) } & { { } } & { } \end{array}$ 

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>1.</sup> Part 1 follows from Lemma 1. Part 2 follows immediately from our profit-maximization problem. The uniform pricing is one of the feasible pricing plans when the ISP prices by Q or B. Therefore, the optimal nonlinear pricing by Q or B must lead to a higher profit. Part 3 can be shown as follows.

Subtracting the integrands of (26) by the integrands of (29) yields

$$
\frac {1}{2} (1 - \theta) ^ {2} (\gamma - \delta^ {2} \eta),
$$

which is positive if and only if $\gamma \geq \delta ^ { 2 } \eta$ . Therefore $P ^ { B } ( \theta )$ is greater than $P ^ { Q } ( \theta )$ for all  if and only if $\gamma \geq \delta ^ { 2 } \eta .$ Since the lower bounds $\underline { { \theta } } ^ { B }$ and $\underline { { \theta } } ^ { Q }$ are determined by equating the integrands to zero $( P ^ { B } ( \theta )$ or $P ^ { Q } ( \theta ) = 0 )$ , when $\gamma \geq \delta ^ { 2 } \eta , \ \underline { { \theta } } ^ { B }$ $\leq \underline { { \theta } } ^ { \breve { Q } }$ . The reason is that $P ^ { B } ( \underline { { \theta } } ^ { Q } ) > P ^ { Q } ( \underline { { \theta } } ^ { Q } )$ because $P ^ { B } ( \theta ) >$ $P ^ { Q } ( \theta )$ ∀ . So $P ^ { B } ( \underline { { \theta } } ^ { B } ) = 0 .$ , implies $\underline { { \theta } } ^ { B } < \underline { { \theta } } ^ { Q }$ . Therefore, pricing by B also leads to larger market coverage. As a consequence, $\mathbb { E } _ { \theta } ^ { ^ { \prime } } [ P ^ { B } ( \theta ) ] \geq \mathbb { E } _ { \theta } [ P ^ { Q } ( \theta ) ]$ if and only if $\gamma \ge \delta ^ { 2 } \gamma$ . 

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>2.</sup> To prove the proposition, let us formulate the seller’s optimization problem. Under pricing by Q, the contract only specifies the data usage Q45 and the corresponding price $\bar { P } ^ { Q } ( \theta )$ . In Stage 4, as the consumer’s utility $u ( B , \bar { M } , \bar { \theta } )$ depends only on Q, the problem degenerates. Thus, we can formulate the seller’s optimization problem in Stage 2 as

$$
\max _ {Q (\theta), P ^ {Q} (\theta)} \mathbb {E} _ {\theta} [ P ^ {Q} (\theta) ]\tag{30}
$$

$$
\mathrm{s.t.} U (Q (\theta), \theta) - P ^ {Q} (\theta)
$$

$$
\geq U (Q (\hat {\theta}), \theta) - P ^ {Q} (\hat {\theta}), \quad \forall \theta , \hat {\theta},\tag{31}
$$

$$
U (Q (\theta), \theta) - P ^ {Q} (\theta) \geq 0, \quad \forall \theta ,\tag{32}
$$

where the constraints are the corresponding (IC) and (IR) conditions.

Now let us consider instead the case with pricing by minutes. In this case, the seller specifies a menu $\dot { \{ ( M ( \theta ) , P ^ { M } ( \theta ) ) \} }$ for the consumers. As a type- consumer chooses an arbitrary contract $( M ( { \hat { \theta } } ) , P ^ { M } ( { \bar { \theta } } ) )$ from the menu in Stage 3, her net utility can be expressed as

$$
U ^ {M} (B \mid \theta , \hat {\theta}) = U (B M (\hat {\theta}), \theta) - P ^ {M} (\hat {\theta}).
$$

Thus, in Stage 4 the consumer should choose the optimal connection speed $B ( \theta , { \hat { \theta } } )$ that maximizes $U ^ { M } ( B \mid \theta , \hat { \theta } )$ . Given this, the seller’s optimization problem in Stage 2 can be formulated as

$$
\max _ {M (\theta), P ^ {M} (\theta)} \mathbb {E} _ {\theta} [ P ^ {M} (\theta) ]\tag{33}
$$

$$
\mathrm{s.t.} U (B (\theta , \theta) M (\theta), \theta) - P ^ {M} (\theta)
$$

$$
\geq U (B (\theta , \hat {\theta}) M (\hat {\theta}), \theta) - P ^ {M} (\hat {\theta}), \quad \forall \theta , \hat {\theta},\tag{34}
$$

$$
U (B (\theta , \theta) M (\theta), \theta) - P ^ {M} (\theta) \geq 0, \quad \forall \theta ,\tag{35}
$$

$$
B (\theta , \hat {\theta}) = \underset {B} {\arg \max} \{U (B M (\hat {\theta}), \theta) - P ^ {M} (\hat {\theta}) \},\tag{36}
$$

where the last constraint indicates the consumer’s Stage 4 decision.

We shall argue that the value of problem (30) is weakly higher than that of problem (33). To see this, suppose that there exists a solution $\{ M ( \theta ) , P ^ { \dot { M } } ( \theta ) \}$ and the induced connection speed selection $\{ B ( { \boldsymbol { \theta } } , { \hat { \boldsymbol { \theta } } } ) \}$ for (33). We now show that we can construct a solution $\{ Q ( \theta ) , P ^ { Q } ( \theta ) \}$ based on $\{ M ( \theta ) , P ^ { M } ( \theta ) \}$ and $\{ B ( { \boldsymbol { \theta } } , { \hat { \boldsymbol { \theta } } } ) \}$ that is feasible to problem (30). Consider the following menu:

$$
Q (\theta) = B (\theta , \theta) M (\theta), \quad \text { and } \quad P ^ {Q} (\theta) = P ^ {M} (\theta), \quad \forall   \theta .\tag{37}
$$

Under this menu, we can verify that

$$
\begin{array}{l} U (Q (\theta), \theta) - P ^ {Q} (\theta) \\ = U (B (\theta , \theta) M (\theta), \theta) - P ^ {M} (\theta) \geq 0, \quad \forall \theta , \end{array}
$$

where the inequality follows from (35). Furthermore, we obtain that

$$
\begin{array}{r l} & U (Q (\hat {\theta}), \theta) - P ^ {Q} (\hat {\theta}) \\ & = U (B (\hat {\theta}, \hat {\theta}) M (\hat {\theta}), \theta) - P ^ {M} (\hat {\theta}) \\ & \leq U (B (\theta , \hat {\theta}) M (\hat {\theta}), \theta) - P ^ {M} (\hat {\theta}) \\ & \leq U (B (\theta , \theta) M (\theta), \theta) - P ^ {M} (\theta), \end{array}
$$

where the first inequality follows from the definition of $B ( \theta , { \hat { \theta } } ) .$ , and in the second inequality we apply (34). Thus, under the menu in (37), both (31) and (32) are satisfied, i.e., it is feasible to problem (30). As the seller’s expected payoff is $\mathbb { E } _ { \theta } [ P ^ { Q } ( \theta ) ] { \overset { * } { = } } \mathbb { E } _ { \theta } [ P ^ { M } ( \theta ) ]$ 1 the value of problem (30) is weakly higher than that of problem (33). A similar argument can be applied to show the dominance over pricing by Mbps. <sup></sup>

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>3.</sup> When the seller prices by M, the objective function is given by

$$
\max _ {M (\theta)} \Pi^ {M} = \int_ {0} ^ {1} \left[ U ^ {Q} (M B ^ {M}, \theta) + U ^ {B} (B ^ {M}, \theta) - \frac {\partial U ^ {Q} (Q , \theta)}{\partial \theta} \right.
$$

$$
\left. \cdot \frac {1 - F (\theta)}{f (\theta)} - \frac {\partial U ^ {B} (B ^ {M} , \theta)}{\partial \theta} \frac {1 - F (\theta)}{f (\theta)} \right] ^ {+} d \theta ,\tag{38}
$$

where $\begin{array} { r } { B ^ { M } = \arg \operatorname* { m a x } _ { \boldsymbol { B } } U ^ { Q } ( { M } { B ^ { M } } , \boldsymbol { \theta } ) + U ^ { B } ( B ^ { M } , \boldsymbol { \theta } ) } \end{array}$ . When the seller prices by Q, the objective function is given by

$$
\begin{array}{r l} \max _ {Q (\theta)} \Pi^ {Q} = & \int_ {0} ^ {1} \left[ U ^ {Q} (Q, \theta) + U ^ {B} (B ^ {e}, \theta) - \frac {\partial U ^ {Q} (Q , \theta)}{\partial \theta} \frac {1 - F (\theta)}{f (\theta)} \right. \\ & \left. - \frac {\partial U ^ {B} (B ^ {e} , \theta)}{\partial \theta} \frac {1 - F (\theta)}{f (\theta)} \right] ^ {+} d \theta , \end{array} \tag {39}
$$

where $B ^ { e } = \operatorname { a r g m a x } _ { _ B } U ^ { B } ( B ^ { e } , \theta )$ . We will show that (39) is larger than (38). First, note that in (39), only ${ \cal U } ^ { Q } ( Q , \theta ) -$ $( { \partial \smile } { \bf { \breve { U } } } ^ { Q } ( Q , \theta ) / { \partial \theta } ) ( ( 1 - F ( \theta ) ) / f ( \theta ) )$ depends on Q, and therefore, these two terms together are larger than the counterpart in (38) because the objective function is maximized over these two terms in (39), conditional on any value of $M ( \theta )$ . Second, this proposition will be established if we can show that the remaining two terms in (39) are greater than the counterpart in (38). The remaining two terms, $U ^ { B } ( B ^ { e } , \theta ) - ( \partial U ^ { B } ( B ^ { \ ' } , \theta ) / \partial \theta ) \times \left( ( 1 - F ( \theta ) ) / f ( \theta ) \right)$ , are actually the objective function of a standard nonlinear pricing problem with only one metric in Equation (19). It has been established that B<sup>e</sup> is the welfare-maximizing solution and its value is larger than the profit-maximizing solution $\begin{array} { r } { B ^ { * } \mathrm { = a r g m a x } _ { B } U ^ { B } ( \bar { B , \theta } ) - ( \partial U ^ { B } ( \bar { B , \theta } ) / \partial \theta ) ( ( 1 - F ( \theta ) ) / f ( \theta ) ) } \end{array}$ It has also been established in the literature that ${ \cal U } ^ { B } ( B , \theta ) -$ $( \partial U ^ { B } ( B , \theta ) / \partial \theta ) ( ( 1 - F ( \theta ) ) / f ( \theta ) )$ is a concave function (Maskin and Riley 1984 and Sundararajan 2004b). Therefore, the concavity implies that $U ^ { B } ( B , \theta ) - \big ( \partial U ^ { B } ( B , \theta ) / \partial \theta \big ) \big ( ( 1 - F ( \theta ) ) / f ( \theta ) \big )$ is decreasing for $B > B ^ { * }$ . Since $B ^ { M } = \arg \operatorname* { m a x } _ { _ R } U ^ { Q } ( M B ^ { M } , \theta ) +$ $U ^ { B } ( B ^ { M } , \theta )$ and both $U ^ { Q } ( M \times B ^ { M } , \theta )$ and $\overset { \vartriangle } { U } ^ { \boldsymbol { B } } ( B ^ { \dot { M } } , \boldsymbol { \theta } )$ have weakly positive first derivatives, $B ^ { M }$ is larger than B<sup>e</sup>. Therefore, $\mathring { U } ^ { { \delta } } ( B , \theta ) - ( \partial U ^ { B } ( B , \theta ) / \partial \theta ) ( ( 1 - F ( \theta ) ) / \big / f ( \theta ) )$ is larger in (39) at value B<sup>e</sup>. <sup></sup>

<sup>Proof</sup> <sup>of</sup> <sup>Proposition 5.</sup> Let us start with the exogenous bandwidth capacity. When the seller charges consumers by Mbps, the pricing problem is equivalent to

$$
\begin{array}{l} \Pi^ {B} = \max _ {B (\theta), P ^ {B} (\theta)} \mathbb {E} _ {\theta} [ P ^ {B} (\theta) ] \\ \text { s.t. } (9), (1 0), \text { and } \int_ {0} ^ {1} B (\theta) d \theta \leq T. \end{array}
$$

Let  denote the Lagrange multiplier associated with the capacity constraint. We can then write down the Lagrangian of this optimization problem as

$$
L = \mathbb {E} _ {\theta} [ P ^ {B} (\theta) ] + \lambda \left[ T - \int_ {0} ^ {1} B (\theta) d \theta \right] = \int_ {0} ^ {1} [ P ^ {B} (\theta) - \lambda B (\theta) ] d \theta + \lambda T.
$$

As the constant T does not affect the optimization problem, this problem is equivalent to a pricing problem in which the seller faces no capacity constraint but instead incurs a constant per unit bandwidth cost . Given the above, we can then incorporate the bandwidth capacity constraint through an endogenous marginal cost, $C ( { \overset { \cdot } { T } } )$ . We can define the endogenous shadow price as $\lambda ( T ) = d C ( T ) / d T$ and transform the problem to a new problem in which the seller faces no capacity constraint but incurs a constant variable cost. This shows (23) in Section 5.2.1.

Next, we discuss the solution of the metrics selection problem with constant variable cost. Under pricing by M or by Q, adding a constant variable cost in B does not lead to a material change of the proofs of Lemmas 1 and 3. Since the additional cost is not part of the utility function, Stage 4 is always the same. Back to Stages 2 and 3, when pricing by M or by Q, the additional cost in B becomes a fixed cost because it is not a function of M or Q. Therefore, all solutions are essentially the same. As a consequence, pricing by M still leads to nondiscriminatory pricing and is suboptimal.

The only difference is when pricing by B, the Stage 2’s profit maximizing becomes different. We list the profitmaximizing problem when pricing by Q and pricing by B for comparison. Similar to $( 2 5 )$ and (28), the profit functions are given by

$$
\begin{array}{c} \mathbb {E} _ {\theta} [ P ^ {B} (\theta) ] = \max _ {B (\theta)} \int_ {\theta^ {B}} ^ {1} \left[ \eta \delta^ {2} \theta \left(\frac {3}{2} \theta - 1\right) + (2 \theta - 1) B (\theta) \right. \\ \left. - \frac {1}{2 \gamma} B (\theta) ^ {2} - \lambda B (\theta) \right] d \theta \end{array}
$$

and

$$
\begin{array}{c} \mathbb {E} _ {\theta} [ P ^ {Q} (\theta) ] = \max _ {Q (\theta)} \int_ {\underline {{\theta}} Q} ^ {1} \bigg [ \gamma \theta \bigg (\frac {3}{2} \theta - 1 \bigg) + \delta (2 \theta - 1) Q (\theta) \\ - \frac {1}{2 \eta} Q (\theta) ^ {2} - \lambda B ^ {e} (\theta) \bigg ] d \theta , \\ \text {where} B ^ {e} (\theta) = \underset {B (\theta)} {\arg \max} U ^ {Q} (B | \theta , \hat {\theta}) = \bigg [ \theta B (\theta) - \frac {1}{2 \gamma} B (\theta) ^ {2} \bigg ]. \end{array}
$$

The only additional term is $\lambda B ( \theta )$ . Without $\lambda B ( \theta )$ , Proposition 1 shows that $\mathbb { E } _ { \theta } [ P ^ { B } ( \theta ) ] \ge \mathbb { E } _ { \theta } [ P ^ { Q } ( \theta ) ]$ if and only if $\gamma \geq$ $\delta ^ { 2 } \eta .$ . In the new optimization problems, when pricing by $B ,$ the seller can adjust $\lambda B ( \theta )$ to maximize $\mathbb { E } _ { \theta } [ P ^ { B } ( \theta ) ]$ , whereas when pricing by Q, the seller leaves the money on the table to let the consumers set this cost term at $\lambda B ^ { e } ( \theta )$ . Therefore, the pricing by B becomes more profitable than pricing by Q, compared with the baseline model. <sup></sup>

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>6.</sup> When the seller prices by $Q ,$ the revised profit function is given by

$$
\begin{array}{c} \int_ {0} ^ {1} \left[ \delta \theta Q (\theta) - \frac {1}{2 \eta} Q (\theta) ^ {2} - Q (\theta) \times C (T) + \frac {1}{2} \gamma \theta^ {2} \right. \\ \left. - [ \delta Q (\theta) + \gamma \theta ] (1 - \theta) \right] ^ {+} d \theta , \end{array}
$$

which differs from the baseline Equation (27) only in −Q45 $\times C ( T )$ . Maximizing the integrand, we can derive the optimal solution of Q as  $\cdot \delta ( 2 \theta - 1 ) - C ( T ) ]$ 7. Substituting this optimal solution back in the integrand (the objective function) yields

$$
\int_ {0} ^ {1} \left[ \frac {1}{2} \eta [ 2 \theta \delta - \delta - C (T) ] ^ {2} + \frac {1}{2} \gamma \theta (3 \theta - 2) \right] ^ {+} d \theta .\tag{40}
$$

Again, when $C ( T )$ is set at 0, this expression is the same as that in the baseline case. Pricing by M can be shown following the same procedure.

Next, we turn to the pricing by B case. The Stage 4 solution now is different because of the additional $- Q ( \theta ) \times C ( T )$ in the utility function. The optimal solution of Q in Stage 4 is $\eta [ \delta \theta - \dot { C } ( T ) ]$ 7. Therefore, the effective utility function is given by

$$
U ^ {B} (\theta , \hat {\theta}) = B (\hat {\theta}) \theta - \frac {1}{2 \gamma} [ B (\hat {\theta}) ] ^ {2} + \frac {\eta}{2} [ \delta \theta - C (T) ] ^ {2} - P ^ {B} (\hat {\theta}),
$$

which differs from (7) only in C4T 50

The revised profit function is given by

$$
\begin{array}{c} \mathbb {E} _ {\theta} [ P ^ {B} (\theta) ] = \int_ {0} ^ {1} \bigg [ \frac {\eta}{2} [ \delta \theta - C (T) ] ^ {2} + B (\theta) \theta - \frac {1}{2 \gamma} B (\theta) ^ {2} \\ - [ \eta \delta (\delta \theta - C (T)) + B (\theta) ] (1 - \theta) \bigg ] ^ {+} d \theta , \end{array}
$$

which is the counterpart of (27) in the baseline case. Deriving the optimal pricing plan turns out to be challenging even if we assume a linear cost function. This is because T depends on B45 and T influences the result through a general function C4T 5. Nonetheless, in what follows, we are able to show that pricing by B becomes relatively more profitable than pricing by Q without characterizing the optimal plan.

Our strategy is as follows. First, we assume that when the seller chooses B45, he ignores its influence on C4T 5 and simply takes C4T 5 as given. This naïve approach leads to a suboptimal pricing plan, and allows us to derive the best pricing solution B45 within this restricted class. We then show that given the inequality condition in Proposition 1, the seller’s profit using this naïve approach is weakly higher than that under the optimal pricing by Q. This subsequently establishes that the optimal pricing by B dominates pricing by Q.

The optimal solution of $B ( \theta )$ when we treat C4T 5 as a constant is the same as that in the baseline case: $B ^ { * } ( \theta ) = \gamma ( 2 \theta - 1 )$ . Therefore, the “optimized” profit function within this restricted class is given by

$$
\int_ {0} ^ {1} \left[ \eta \delta^ {2} \theta \left(\frac {3}{2} \theta - 1\right) + \eta C (T) \left[ \frac {C (T)}{2} + \delta - 2 \theta \delta \right] + \frac {\gamma}{2} (2 \theta - 1) ^ {2} \right] ^ {+} d \theta , \tag {41}\tag{41}
$$

which is the counterpart of (26) in the baseline case and the second term is the additional term. Subtracting the integrand of (40) by (41), we obtain ${ \scriptstyle \frac { 1 } { 7 } } ( 1 - \theta ) ^ { 2 } ( \delta ^ { 2 } \eta - \gamma )$ , which is exactly the same as the condition in the baseline case. This establishes our result. <sup></sup>

## References

Afèche P, Mendelson H (2004) Pricing and priority auctions in queueing systems with a generalized delay cost structure. Management Sci. 50(7):869–882.

Anderson J (2010) Understanding the changing needs of the U.S. online consumer. Forrester Res. https://www.forrester.com/ report/Understanding+The+Changing+Needs+Of+The+US +Online+Consumer+2010/-/E-RES57861.

Armstrong M (2000) Optimal multi-object auctions. Rev. Econom. Stud. 67(3):455–481.

Armstrong M, Rochet J (1999) Multi-dimensional screening: A user’s guide. Eur. Econom. Rev. 43(4):959–979.

Asker J, Cantillon E (2008) Properties of scoring auctions. RAND J. Econom. 39(1):69–85.

Baig E (1997) AOL isn’t the only connection in town. Business-Week, 144. http://www.bloomberg.com/news/articles/1997-02 -23/aol-isnt-the-only-connection-in-town.

Bhargava HK, Choudhary V (2001) Information goods and vertical differentiation. J. Management Inform. Systems 18(2):89–106.

Bhargava H, Choudhary V (2004) Economics of an information intermediary with aggregation benefits. Inform. Systems Res. 15(1):22–36.

Bhargava H, Choudhary V (2008) Research note—When is versioning optimal for information goods? Management Sci. 54(5): 1029–1035.

Chellappa R, Shivendu S (2007) An economic model of privacy: A property rights approach to regulatory choices for online personalization. J. Management Inform. Systems 24(3):193–225.

Chellappa R, Shivendu S (2010) Mechanism design for free but no free disposal services: The economics of personalization under privacy concerns. Management Sci. 56(10):1766–1780.

Chen Y-J, Seshadri S (2007) Product development and pricing strategy for information goods under heterogeneous outside opportunities. Inform. Systems Res. 18(2):150–172.

Cheng R, Raice S (2010) Verizon rethinks pricing. Wall Street Journal (November 17). http://www.wsj.com/articles/SB10001424052 748704648604575620963722752820.

Choudhary V (2010) Use of pricing schemes for differentiating information goods. Inform. Systems Res. 21(1):78–92.

Chua HH (2008) Bandwidth hogs may force ISPs to adopt volume-based charges. The Straits Times (August 4). http://web .international.ucla.edu/institute/article/95551.

Das S, Du AY, Gopal R, Ramesh R (2011) Risk management and optimal pricing in online storage grids. Inform. Systems Res. 22(4):756–773.

Deligiorgi C, Michalakelis C, Vavoulas A, Varoutas D (2007) Nonparametric estimation of a hedonic price index for ADSL connections in the European market using the Akaike information criterion. Telecomm. Systems 36(4):173–179.

Dewan S, Mendelson H (1990) User delay costs and internal pricing for a service facility. Management Sci. 36(12):1502–1517.

Du A, Geng X, Gopal R, Ramesh R, Whinston A (2008a) Capacity provision networks: Foundations of markets for sharable resources in distributed computational economies. Inform. Systems Res. 19(2):144–160.

Du A, Geng X, Gopal R, Ramesh R, Whinston A (2008b) Topographically discounted Internet infrastructure resources: A panel study and econometric analysis. Inform. Tech. Management 9(2):135–146.

Fishburn P, Odlyzko A (2000) Dynamic behavior of differential pricing and quality of service options for the Internet. Decision Support Systems 28(1-2):123–136.

Fishburn P, Odlyzko A, Siders R (2000) Fixed fee versus unit pricing for information goods: competition, equilibria, and price wars. Kahin B, Varian HR, eds. Internet Publishing and Beyond: The Economics of Digital Information and Intellectual Property (MIT Press, Cambridge, MA), 167–189.

Grubb M (2009) Selling to overconfident consumers. Amer. Econom. Rev. 99(5):1770–1807.

Gupta A, Stahl D, Whinston A (1997) A stochastic equilibrium model of Internet pricing. J. Econom. Dynam. Control 21(4-5): 697–722.

Gupta A, Jukic B, Stahl D, Whinston A (2000) Extracting consumers’ private information for implementing incentive-compatible Internet traffic pricing. J. Management Inform. Systems 17(1): 9–29.

Hartley M (2009) Internet providers fear Bell’s billing change threatens services. Canwest News Service (August 13).

Hitt L, Chen P (2005) Bundling with customer self-selection: A simple approach to bundling low-marginal-cost goods. Management Sci. 51(10):1481–1493.

Huang K-W (2009) Optimal criteria for selecting price discrimination metrics when buyers have log-normally distributed willingness-to-pay. Quant. Marketing Econom. 7(3):321–341.

Huang K-W, Sundararajan A (2011) Pricing digital goods: Discontinuous costs and shared infrastructure. Inform. Systems Res. 22(4):721–738.

Ida T, Kuroda T (2006) Discrete choice analysis of demand for broadband in Japan. J. Regulatory Econom. 29(1):5–22.

Jain S, Kannan P (2002) Pricing of information products on online servers: Issues, models, and analysis. Management Sci. 48(9):1123–1142.

Jing B (2007) Network externalities and market segmentation in a monopoly. Econom. Lett. 95(1):7–13.

Jones R, Mendelson H (2011) Information goods vs. industrial goods: Cost structure and competition. Management Sci. 57(1): 164–176.

Konana P, Gupta A, Whinston A (2000) Integrating user preferences and real-time workload in information services. Inform. Systems Res. 11(2):177–196.

Lahiri A, Dewan R, Freimer M (2008) Pricing of wireless services: Application pricing vs. traffic pricing. Workshop Inform. Systems Econom.

Levy S (2008) Pay per gig. Washington Post (January 30). http:// www.washingtonpost.com/wp-dyn/content/article/2008/01/29/ AR2008012903205.html.

MacKie-Mason J, Varian H (1995) Pricing congestible network resources. IEEE J. Selected Areas Comm. 13(7):1141–1149.

Maskin E, Riley J (1984) Monopoly with incomplete information. RAND J. Econom. 15(2):171–196.

Masuda Y, Whang S (2006) On the optimality of fixed-up-to tariff for telecommunications service. Inform. Systems Res. 17(3): 247–253.

Mehra A, Bala R, Sankaranarayanan R (2012) Competitive behavior-based price discrimination for software upgrades. Inform. Systems Res. 23(1):60–74.

Mendelson H (1985) Pricing computer services: Queueing effects. Comm. ACM 28(3):312–321.

Mendelson H, Whang S (1990) Optimal incentive-compatible priority pricing for the m/m/1 queue. Oper. Res. 38(5):870–883.

Mussa M, Rosen S (1978) Monopoly and product quality. J. Econom. Theory 18(2):301–317.

NewsBytes (1998) PacBell intros new dialup and ISDN services. NewsBytes (June 11).

Odlyzko A (1998) The economics of the Internet: Utility, utilization, pricing, and quality of service. AT&T Research. http://ftp .unpad.ac.id/orari/library/library-ref-eng/ref-eng-1/physical/ the-economics-of-the-internet.pdf.

Pegoraro R (2009) Broadband caps can cost you. Washington Post (May 3). http://www.washingtonpost.com/wp-dyn/content/ article/2009/05/02/AR2009050200123.html.

Rochet J, Stole L (2003) Optimal dynamic auctions. The economics of multidimensional screening. Dewatripont M, Hansen L, Turnovsky S, eds. Advances in Economics and Econometrics: Theory and Applications—Eighth World Congress (Cambridge University Press, New York), 150–197.

Rysavy P (2008) Figuring out the 3G and 4G mobile broadband market is tough. InformationWeek (May 12). www.rysavy.com/ Articles/2008\_05\_global\_Mobile.pdf.

Satitsamitpong M, Otsuka T, Jitsuzumi T, Mitomo H (2012) An analysis of demand-based factors for broadband migration. Appl. Econom. J. 19(2):1–17.

Savage SJ, Waldman DM (2004) United States demand for Internet access. Rev. Network Econom. 3(3):228–246.

Singh N, Vives X (1984) Price and quantity competition in a differentiated duopoly. RAND J. Econom. 15(4):546–554.

Stranger G, Greenstein S (2007) Pricing in the shadow of firm turnover: ISPs in the 1990s. Internat. J. Indust. Organ. 26(3): 625–642.

Sundararajan A (2004a) Managing digital piracy: Pricing and protection. Inform. Systems Res. 15(3):287–308.

Sundararajan A (2004b) Nonlinear pricing of information goods. Management Sci. 50(12):1660–1673.

Wallsten SJ, Riso J (2014) Residential and business broadband prices. Part 1: An empirical analysis of metering and other price determinants. Technology Policy Institute Working paper, Washington, DC.

Yu K, Prud’Homme M (2010) Econometric issues in hedonic price indices: The case of Internet service providers. Appl. Econom. 42(15):1973–1994.
