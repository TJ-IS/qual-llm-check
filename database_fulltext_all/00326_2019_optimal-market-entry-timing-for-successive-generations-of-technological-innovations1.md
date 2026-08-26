---
otero_id: 326
otero_key: "WQAAJJ37"
title: "Optimal Market Entry Timing for Successive Generations of Technological Innovations1"
authors: "Zhengrui Jiang; Xinxue (Shawn) Qu; Dipak C. Jain"
year: "2019"
journal: "MIS Quarterly"
doi: "10.25300/misq/2019/14307"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# OPTIMAL MARKET ENTRY TIMING FOR SUCCESSIVE GENERATIONS OF TECHNOLOGICAL INNOVATIONS<sup>1</sup>

Zhengrui Jiang School of Business, Nanjing University, Nanjing 210093 CHINA {zjiang@nju.edu.cn}

Xinxue (Shawn) Qu Mendoza College of Business, University of Notre Dame, Notre Dame, IN 46556 50011 U.S.A. {xqu2@nd.edu}

Dipak C. Jain CEIBS, Shanghai, CHINA 201203 {dipakcjain@ceibs.edu}

Determining the optimal market entry timing for successive product generations is a critical decision for firms. Pioneering studies on market entry timing have focused on purchase-to-own (PTO) products (e.g., computers) and assumed that an old product generation can continue to be sold after the release of a new generation. In this study, both PTO products and subscribe-to-use (STU) products (e.g., Office 365) are considered, and an old generation can either coexist with or be completely replaced by the new generation. We develop a multigeneration diffusion modeling framework to help determine the optimal market entry timing for a new product generation under such diverse business scenarios. Unlike prior literature, we find that for PTO products, the optimal entry timing for a new generation can be any time during a finite planning horizon; not introducing a new generation may be optimal only if the old generation will be completely replaced upon the introduction of the new generation. Under an infinite planning horizon, the second PTO product generation should not be released until the first generation has reached full market penetration. Of greater interest, for STU products, a new generation should either be released now or never be released, regardless of the length of the planning horizon and whether the old and new generations can coexist in the market or not.

Keywords: Multigeneration diffusion, market entry strategy, purchase-to-own, subscribe-to-use

## Introduction

Most of the products and services we consume today represent improved versions of earlier generations, and our current products will eventually be replaced by better ones in the future.<sup>2</sup> The information technology (IT) market, in particular, driven by faster technological advancements and higher consumer expectations, has witnessed frequent releases of successive product generations. Well-known examples include both hardware products such as routers and switches and software products such as Microsoft Windows operating systems.

In a product line with successive generations, old generation adopters can help speed up the diffusion of a new generation because existing adopters are more familiar with the product line and hence may pay more attention to the development of a new generation. For instance, it is reported that 70% of the first-day buyers of iPhone 4 were users of earlier generations of iPhone (Hughes 2010). Most recent statistics show that

83% of iPhone 5 sales were upgrades from pervious iPhones.<sup>3</sup> Meanwhile, since different generations in a product line are partial substitutes, the introduction of a new generation can cannibalize sales of the old generation. Given the complementary and competitive relationships between successive product generations, when to release a new product to the market has important financial implications for firms.

In the past few decades, researchers have analyzed the market entry timing for a new product from different angles. In one stream of research, product quality is considered a key determinant of market entry timing. Some researchers focus on one product generation in a noncompetitive environment and examine the tradeoffs between early market entry and product maturity. For instance, Kalish and Lilien (1986) develop a model that incorporates the impact of product quality on the probability of adoption, and then use it to derive the optimal introduction time for a new product. More recent studies have considered multiple product generations. For instance, Krankel et al. (2006) propose a decision model to decide whether a monopolist firm should introduce a new generation at a given time interval or wait until the next interval to take advantage of newer technologies and release a better product. Morgan et al. (2001) study the time to market and quality trade-off for multiple product generations under a competitive environment. One of their key findings is that with a faster rate of quality improvement, longer development cycles are desirable for the single generation models, whereas shorter cycles are more beneficial under the forward-looking multiple generation model. The aforementioned studies differ from the present study in that they do not consider diffusion dynamics and cross-generation repeat purchases. In addition, product quality is a key determinant of market entry timing in the prior studies, while the present study demonstrates that market entry timing is an important strategic decision even if product quality is exogenously determined.

A second stream of research treats product quality as exogenous, but brings consumers’ valuations into the picture, and employs analytical models to determine the market launch timing or launch interval for new product versions. In one study, Prasad et al. (2004) focus specifically on the movie industry and analyze the optimal timing for video release after a theatrical release. An interesting finding is that with customer expectations considered, the distributor’s desire to limit cannibalization does not extend the time between theatrical and video releases. A tradeoff of considering consumers’ valuation is that the complex cross-generation diffusion dynamics (e.g., leapfrogging and switching) could not be fully modeled in these studies. In a more recent study, Mehra et al. (2014) examine the product lifecycle management of packaged software. They find that in a growing market with homogeneous customers, the optimal upgrade intervals increase throughout the product’s lifecycle because of demand and cost considerations. In addition, they show that the upgrade intervals are longer when successive software versions are forward-compatible, and shorter when they are not.

A third stream of research studies the adoption decisions of rational consumers in the presence of improved product versions and how they affect the firm’s marketing decisions, product development strategies, and financial performance. For instance, using a two-period framework, Dhebar (1994) finds that profit maximization in the presence of rational consumers imposes a demand-side constraint on product improvement rate. If the product quality is improved too rapidly, disequilibrium effects could result (i.e., high-end consumers could choose to wait for a future new version, leaving only mid- and low-end consumers to purchase the current version). Padmanabhan et al. (1997) examine how consumers’ expectations about the future installed base and network effects affect product sales. They find that under asymmetric information about externality, it is optimal for a high-externality firm to provide less than full quality in the first period and then make up for the quality differential by providing an upgrade in the second period. Sankarnarayanan (2007) proposes a novel contractual device named Free New Version Rights (NVR) warranty, which offers a free new version to consumers who purchased an old version, in a limited time period. The study derives conditions under which free NVR warranty is optimal, and show that with free NVR, consumer surplus decreases and social surplus increases.

In terms of research focus, this study is the closest to the fourth stream of research, represented by two pioneering studies by Wilson and Norton (1989) and Mahajan and Muller (1996). Specifically, Wilson and Norton develop a multigeneration diffusion model to decide the optimal market entry timing for a product line extension. They find that in most cases a product line extension should be introduced either at the same time as the main product (now) or not be introduced during the planning horizon (never). Under a different set of assumptions, Mahajan and Muller analyze market entry timing for an improved new product generation. Their general conclusion is that the second generation should be introduced either at the same time as the first (now) or when the sale of the first generation has reached its maturity stage (at maturity).<sup>4</sup> Both Wilson and Norton and Mahajan and Muller employ multigeneration models to capture the diffusion dynamics across product versions and over time. Due to the complexity of multigeneration diffusion models, neither study is able to take into account consumers’ valuations of product quality. The primary difference between these two prior studies and the current research is that we consider a wider range of business scenarios and derive different findings. We next elaborate the different business scenarios considered in this study.

Most prior studies on market entry timing focus on the type of products for which a one-time price is charged at the time of product sale and the ownership of the product is transferred to the buyer permanently after the transaction. Examples of such products include computers and packaged software products. We refer to this type of product as a purchase-toown (PTO) product.

In today’s market, in addition to PTO, another type of product offering is becoming increasingly common: some firms are providing ongoing services to their customers, where the fee charged depends on the duration or frequency of the service. For instance, cellular service providers charge customers subscription fees as long as they remain in their networks. This is referred to as a subscribe-to-use (STU) product. In the IT industry, for example, STU products are becoming increasingly popular because of the industry’s move toward cloud computing (Hashem et al. 2015). Instead of selling packaged software and hardware products, a growing number of firms are providing software as a service (SaaS), platform as a service (PaaS), and infrastructure as a service (IaaS) to their customers. For instance, Microsoft, which used to sell its Office Suite as a PTO product, is promoting its Office 365 as a STU offering to both consumers and businesses. STU, however, is not limited to cloud-based products. For example, software products such as Mathematica and SAS are often run on clients’ machines, but an annual license fee is still collected from customers as long as they continue to use the product.

After a new product generation is introduced to the market, firms can adopt different generation transition strategies. Some firms continue to sell their old generations as long as there is sufficient demand. For instance, digital cellular service was introduced in the early 1990s in the United States, but analog service continued until early 2000. Similarly, inkjet printers are still being sold along with the more advanced laser printers. This strategy is referred to as phase-out transition in this study. In some markets, we observe a different practice: a firm discontinues the production and/or sale of the old generation as soon as a new generation is introduced. For example, Microsoft stops selling older Office versions as soon as a new version is released. We term this generation transition strategy total transition.

The two revenue models (i.e., PTO and STU) and two generation transition strategies (i.e., phase-out and total) jointly lead to four business scenarios, as presented in Table 1.

The business scenarios illustrated in this table represent a more diverse market landscape than the one (i.e., Scenario I only) analyzed by Wilson and Norton (1989) and Mahajan and Muller (1996). This new landscape is particularly evident in today’s IT product market, characterized by breathtaking speed of technological advancements and frequent releases of new hardware products, software products, and services. Therefore, we believe that market entry strategy for technological innovations presents a unique opportunity for the information systems community to make impactful contributions to this important area of research. The primary objective of the present research is to analyze this diverse market landscape, derive the market entry timing for each business scenario, and examine whether the optimal entry timing differs across business scenarios. In addition, we would like to compare our findings with those of prior studies.

We develop a generalized multigeneration diffusion modeling framework to derive the optimal market entry timing for all four business scenarios listed in Table 1. Because the prior literature on mutligeneration diffusion and entry timing has focused on Scenario I only, existing models are limited in their scope and unfit for other considered business scenarios. Therefore, we adapt and extend existing, empirically tested diffusion models to capture the cross-generation diffusion dynamics under the new scenarios. The generalized modeling framework fills the void in the existing literature and can help firms make informed market entry timing decisions under today’s more diverse market landscape.

Based on proposed decision models, we are able to derive some interesting results. We find that with our model formulation, the findings presented in the prior studies no longer hold under the original conditions. Specifically, we find that for PTO products under phase-out transition, the optimal entry timing can be either now or sometime during the finite planning horizon, but not introducing the new product generation during the planning horizon cannot be an optimal solution. For PTO products under total transition, not introducing the new generation is a possible optimal solution. Under an infinite planning horizon, the difference between phase-out transition and total transition disappears, and the second PTO product generation should not be released until the first generation has reached full market penetration. More interestingly, our results indicate that the now or never rule is valid for STU products, the type of products not considered in the prior studies, and the rule holds regardless of the generation transition strategy or the length of planning horizon.

## Modeling Framework

In the presence of successive product generations, potential (existing) adopters of an older generation can leapfrog (switch) to a newer generation. Specifically, leapfrogging represents the behavior of potential adopters skipping previous generation(s) and directly adopting a newer generation;

<table><tr><td colspan="3">Table 1. Business Scenarios Corresponding to Revenue Models and Transition Strategies</td></tr><tr><td></td><td>Phase-out Transition</td><td>Total Transition</td></tr><tr><td>Purchase-to-Own (PTO)</td><td>Scenario I(e.g., inkjet and laser printers)</td><td>Scenario II(e.g., previous and current versions of Microsoft Office)</td></tr><tr><td>Subscribe-to-Use (STU)</td><td>Scenario III(e.g., analog and digital cellular service)</td><td>Scenario IV(e.g., previous and current versions of Mathematica software license)</td></tr></table>

switching, on the other hand, represents the behavior of existing adopters of the immediate previous generation making an upgrade to a new generation.

In the diffusion literature, several multigeneration models (e.g., Danaher et al. 2001; Jiang and Jain 2012; Mahajan and Muller 1996) explicitly capture leapfrogging and switching based on a diffusion framework. We adopt and extend the Generalized Norton-Bass (GNB) model (Jiang and Jain 2012) because this model has strong empirical support, provides closed-form expressions for both the instantaneous adoption rate and the number of units-in-use, and offers the functionality and flexibility to project the profit for all business scenarios summarized in Table 1. Furthermore, the GNB model has been adopted in the recent information systems literature to analyze the backward compatibility of successive generation of platforms (Hann et al. 2016).

We next derive the total profit for all four business scenarios discussed previously.

## Profit Projection under Phase-out Transition

As mentioned earlier, the GNB model provides closed-form expressions for the adoption rate and the number of units-inuse. As an example, the adoption rate curve represents the rate of initial adoptions of a cellular service (e.g., analog or digital), while the units-in-use curve captures the number of active subscribers of the service. Figures 1 and 2 illustrate the key differences between the adoption rate and the number of units-in-use for a two-generation case.

Without loss of generality, we assume that generation 1 (G1) is introduced at time 0 and generation 2 (G2) at time $\tau _ { 2 } \geq 0$ Before $\tau _ { 2 } ,$ the adoption rate of G1 follows the noncumulative Bass diffusion curve, while the number of units-in-use of G1 represents the cumulative number of adoptions until a given time. Therefore, the adoption rate of G1 could decrease before $\tau _ { 2 } ,$ whereas the number of units-in-use of G1 is always increasing before $\tau _ { 2 } .$ After $\tau _ { 2 } ,$ the adoption rate of G2 typically exhibits a bell-shaped curve, while the units-in-use of

G2 will be monotonically increasing. At some point during the second time period (after τ<sub>2</sub>), the units-in-use curve for G1 will start to decline, because a large number of existing adopters of G1 will switch to G2.

We differentiate adoption rate from units-in-use because the former is needed for estimating revenue generated from PTO products, while the latter is central to revenue projection for STU products.

Following the GNB model, the number of units-in-use for the two successive generations can be represented by the following equations:

$$
\begin{array}{c} S _ {1} (t) = m _ {1} F _ {1} (t) - m _ {1} F _ {1} (t) F _ {2} (t - \tau_ {2}) \\ = m _ {1} F _ {1} (t) \Big [ 1 - F _ {2} (t - \tau_ {2}) \Big ] \end{array}\tag{1}
$$

$$
\begin{array}{c} S _ {2} (t) = m _ {2} F _ {2} (t - \tau_ {2}) + m _ {1} F _ {1} (t) F _ {2} (t - \tau_ {2}) \\ = [ m _ {2} + m _ {1} F _ {1} (t) ] F _ {2} (t - \tau_ {2}) \end{array}\tag{2}
$$

The instantaneous adoption rates for the two generations are

$$
y _ {1} (t) = m _ {1} f _ {1} (t) \left[ 1 - F _ {2} (t - \tau_ {2}) \right]\tag{3}
$$

$$
\begin{array}{c} y _ {2} (t) = \left[ m _ {2} + m _ {1} F _ {1} (t) \right] f _ {2} (t - \tau_ {2}) \\ + m _ {1} f _ {1} (t) F _ {2} (t - \tau_ {2}) \end{array}\tag{4}
$$

and the cumulative numbers of adoptions for the two generations can be expressed as

$$
Y _ {1} (t) = m _ {1} F _ {1} (t) - m _ {1} \int_ {\tau_ {2}} ^ {t} f _ {1} (\theta) F _ {2} (\theta - \tau_ {2}) d \theta\tag{5}
$$

$$
Y _ {2} (t) = \left[ m _ {2} + m _ {1} F _ {1} (t) \right] F _ {2} (t - \tau_ {2})\tag{6}
$$

![](/api/attachments/WQAAJJ37/fulltext/images/647af5ffbad08afe0da01e903a85997092042ed0694339eb573ff814dbcf92b2.jpg)  
Figure 1. Adoption Rate under Phase-out Transition

Additional descriptions of Equations (1) S (6) are provided in the Appendix. In these equations, $m _ { 1 }$ represents the market potential for generation 1, and $m _ { 2 }$ is the incremental market potential specific to generation 2 (i.e., potential adopters who are only interested in generation 2). $F _ { G } ( t )$ and $f _ { G } ( t )$ denote the cumulative and noncumulative diffusion rates, both in terms of the fraction of potential adopters, for generation $G \left( G = 1 \right)$ 2). Specifically,

$$
\begin{array}{l} F _ {G} (t) = \int_ {0} ^ {t} f _ {G} (\theta) d \theta = \\ \left\{ \begin{array}{c c} 0, & t <   0 \\ \frac {1 - e ^ {- (p _ {G} + q _ {G}) t}}{\left(\frac {q _ {G}}{p _ {G}}\right) e ^ {- (p _ {G} + q _ {G}) t} + 1}, & t \geq 0 \end{array} \right. \end{array}\tag{7}
$$

As is common in the diffusion literature, we refer to $p _ { G }$ and $q _ { G }$ as the coefficient of innovation and coefficient of imitation, respectively, for generation G.

It is worth noting that existing adopters of G1 can switch from G1 to G2, but not vice versa. Because G2 is the latest product generation available in the market, every adopter of G2 would choose to use G2. The cumulative number of adoptions of G2 always equals the number of units-in-use of G2. On the other hand, existing adopters of G1 can switch to G2, thus the number of units-in-use of G1 equals the cumulative number of adoptions of G1 minus the number of adopters who have switched from G1 to G2.

In order to estimate the total profit generated from two product generations, we need to make some assumptions.

Assumption 1: Decision-makers consider only the profit generated during a finite planning horizon.

When used in projecting future demand or profits, there are three treatments of the time dimension: (1) discrete time periods with unspecified length (e.g., Moorthy and Png 1992), (2) finite time horizon (e.g., Wilson and Norton 1989), and (3) infinite time horizon (e.g., Mahajan and Muller 1989). Among them, the finite planning horizon is the most common according to our own literature review, and the most frequently used in real-world economic analysis (e.g., August and Niculescu 2013; Guo and Chen 2018; Klemme and Schoney 1984). As illustrated in Figure 3, this study also adopts a finite planning horizon, denoted by D. Our goal is to derive the optimal market entry timing for a second product generation, denoted by $\tau _ { 2 } ^ { * } ,$ assuming that the length of the planning horizon is exogenously given.

![](/api/attachments/WQAAJJ37/fulltext/images/ca69c1f496b060780f2d5ea0e2d3a865bdd5339ed7dbae4ca54b45e538d79fa8.jpg)  
Figure 2. Units-in-Use under Phase-out Transition

The duration of this planning horizon could be determined based on the product’s expected time on the market (Cohen et al. 1996) or a time duration (e.g., Kalish 1983; Nascimento and Vanhonacker 1988) beyond which revenue generated becomes so uncertain that it is not worth considering. As pointed out in a National Academy of Engineering report (NAE 1992), a shorter planning horizon is preferred if the firm faces a shorter planning horizon, higher technological and market uncertainty, higher investment risk, and lower ability in the application of technology, and vice versa.

Assumption 2: During the planning horizon, the cost and price of a product both increase at the same rate as the discount rate, hence the present value of profit per unit sale or per unit time of service to a customer remains constant for the entire planning horizon.<sup>5</sup>

We define unit contribution margin (for PTO product) as the present value of the profit resulting from selling one unit of a PTO product, and denote the unit contribution margin for generation G by $\pi _ { G } .$ Similarly, we define unit contribution margin (for STU service) as the present value of the profit generated from providing one unit time’s STU service for one customer, and denote the unit contribution margin for generation G by $\varphi _ { G } .$ We assume that all profit margins are positive (i.e., $\pi _ { G } > 0 , \varphi _ { G } > 0 )$

<table><tr><td>Release of First Generation (G1)</td><td>Release of Second Generation (G2)</td></tr><tr><td>0</td><td>τ2</td></tr></table>

Figure 3. Timeline of the Model

For purchase-to-own (PTO) products, the profit at any given time is proportional to the adoption rate at that time, hence the total time-discounted profit for the two product generations during the entire planning horizon (from time 0 to D) equals

$$
\begin{array}{c} \pi (\tau_ {2}) = \pi_ {1} \int_ {0} ^ {D} y _ {1} (\theta) d \theta + \pi_ {2} \int_ {\tau_ {2}} ^ {D} y _ {2} (\theta) d \theta \\ = \pi_ {1} Y _ {1} (D) + \pi_ {2} Y _ {2} (D) \end{array}\tag{8}
$$

For subscribe-to-use (STU) products, the profit at any given time is proportional to the number of units-in-use at that time, therefore the total profit during the planning horizon is

$$
\pi (\tau_ {2}) = \varphi_ {1} \int_ {0} ^ {D} S _ {1} (\theta) d \theta + \varphi_ {2} \int_ {\tau_ {2}} ^ {D} S _ {2} (\theta) d \theta\tag{9}
$$

Equations (8) and (9) both assume that the fixed cost of introducing a new generation is insignificant when compared to the variable costs and the revenues generated from product sale or service, hence the fixed cost is not considered in our analysis. This assumption also ensures a fair comparison between our findings and those of Wilson and Norton (1989) and Mahajan and Muller (1996), because the same assumption is also implicitly adopted by the two prior studies.

## Profit Projection under Total Transition

As stated earlier, the GNB model considers only phase-out transition; we now extend it for profit projection under total transition. In Equations (1)–(4), the term $F _ { 2 } ( t - \tau _ { 2 } )$ represents the leapfrogging multiplier (i.e., the proportion of potential adopters who leapfrog to G2). Under total transition, since G1 is discontinued once G2 is introduced, we need to make the following assumption:

Assumption 3: Under total transition, all customers who would otherwise adopt G1 will adopt G2 instead after the latter is released.

Assumption 3 essentially sets the effective leapfrogging multiplier to 1. Therefore, the adoption rate for G1 drops to 0 after $\tau _ { 2 } ,$ and the original adopt rate of G1 is added to the rate of G2. Hence, the adoption rates for G1 and G2 become, respectively,

$$
\dot {y} _ {1} (t) = \left\{ \begin{array}{c c} m _ {1} f _ {1} (t), & t <   \tau_ {2} \\ 0, & t \geq \tau_ {2} \end{array} \right.\tag{10}
$$

$$
\begin{array}{r l} \dot {y} _ {2} (t) & = \left[ m _ {2} + m _ {1} F _ {1} (\tau_ {2}) \right] f _ {2} (t - \tau_ {2}) \\ & + m _ {1} f _ {1} (t), \quad t \geq \tau_ {2} \end{array}\tag{11}
$$

From the adoption rates, we obtain the cumulative number of adoptions for G1 and G2:

$$
\dot {Y} _ {1} (t) = \left\{ \begin{array}{l l} m _ {1} F _ {1} (t), & t <   \tau_ {2} \\ m _ {1} F _ {1} (\tau_ {2}), & t \geq \tau_ {2} \end{array} \right.\tag{12}
$$

$$
\begin{array}{c} \dot {Y} _ {2} (t) = \Big [ m _ {2} + m _ {1} F _ {1} (\tau_ {2}) \Big ] F _ {2} (t - \tau_ {2}) + \\ m _ {1} \Big [ F _ {1} (t) - F _ {1} (\tau_ {2}) \Big ], t \geq \tau_ {2} \end{array}\tag{13}
$$

We next derive the number of units-in-use for the two generations. We consider the scenario where existing adopters of G1 can continue to use the old generation until they decide to switch to G2, and the probability of switching at any given time is the same as that in the phase-out transition case. An example is that cellular phone users who have adopted analog service before the introduction of digital services are allowed to keep their analog service until they voluntarily switch to digital service. Therefore, before $\tau _ { 2 } ,$ the number of units-inuse of G1 is the same as the cumulative number of adoptions of G1. After $\tau _ { 2 } ,$ , the number of units-in-use of G1 equals the cumulative number of adoptions of G1 minus the cumulative number of switchings from G1 to G2. On the other hand, since G2 is the newest generation, the number of units-in-use of G2 always equals the cumulative number of adoptions of G2. Hence,

$$
\dot {S} _ {1} (t) = \left\{ \begin{array}{c c} m _ {1} F _ {1} (t), & t <   \tau_ {2} \\ m _ {1} F _ {1} (\tau_ {2}) [ 1 - F _ {2} (t - \tau_ {2}) ], & t \geq \tau_ {2} \end{array} \right.\tag{14}
$$

$$
\begin{array}{r l} \dot {S} _ {2} (t) & = \dot {Y} _ {2} (t) = \left[ m _ {2} + m _ {1} F _ {1} (\tau_ {2}) \right] F _ {2} (t - \tau_ {2}) \\ & + m _ {1} \left[ F _ {1} (t) - F _ {1} (\tau_ {2}) \right], \quad t \geq \tau_ {2} \end{array}\tag{15}
$$

Similar to Equations (8) and (9), under total transition, the total profits for PTO products and STU products are, respectively,

$$
\pi (\tau_ {2}) = \pi_ {1} \dot {Y} _ {1} (\tau_ {2}) + \pi_ {2} \dot {Y} _ {2} (D)\tag{16}
$$

$$
\pi (\tau_ {2}) = \varphi_ {1} \int_ {0} ^ {D} \dot {S} _ {1} (\theta) d \theta + \varphi_ {2} \int_ {\tau_ {2}} ^ {D} \dot {S} _ {2} (\theta) d \theta\tag{17}
$$

For better comparison with phase-out transition, we show the adoption rate and units-in-use curves under total replacement in Figures 4 and 5, respectively.

By comparing these two figures with Figures 1 and 2 for phase-out transition, we can see several important differences:

(1) Under total transition, the adoption rate of G1 drops to zero upon the introduction of G2 at time $\tau _ { 2 } .$

(2) Owing to the “forced” leapfrogging, the adoption rate of G2 starts at a higher level than that of G1 just before $\tau _ { 2 } .$

(3) Since the adoption of G1 stops after the introduction of G2, the number of units-in-use of G1 decreases monotonically after $\tau _ { 2 } .$

Based on the profit projections derived in this section, we next derive the optimal market entry timing for the four business scenarios summarized in Table 1.

## Market Entry Timing for PTO Products

We first analyze the two-generation case for PTO products. Our goal is to find the market entry timing for the second generation (G2) that maximizes the total profit. The two generation transition strategies (i.e., phase-out transition and total transition) are separately examined.

## Scenario I: PTO Products under Phase-out Transition

As explained earlier, many consumer products (e.g., computers, TVs) fall under Scenario I: PTO products under phase-out transition. The total profit for this business scenario is given in Equation (8); hence the decision problem for deciding the optimal market entry time for G2 is formulated as

$$
\max _ {\alpha_ {2} \leq \tau_ {2} \leq D} \pi (\tau_ {2}) = \pi_ {1} Y _ {1} (D) + \pi_ {2} Y _ {2} (D)\tag{18}
$$

with the functional forms of $Y _ { 1 } ( D )$ and $Y _ { 2 } ( D )$ given in Equations (5) and (6), respectively. $\alpha _ { 2 }$ represents the earliest possible introduction time for the second generation.

Regarding the values of coefficient of innovation (p) and coefficient of imitation (q) across generations, the prior literature has adopted different assumptions and reported different empirical findings. Some studies such as Wilson and Norton (1989), and Mahajan and Muller (1996) assume that p and q remain constant across generations. Other studies (e.g. Danaher et al. 2001) find that allowing q to change across product generations can lead to a better model fit. In a recent study, based on data for 39 product generations in 12 product markets, Stremersch et al. (2010) find that changes in the two coefficients across generations are insignificant for all but one product category (steel making). We therefore assume that p and q both remain constant from G1 to G2.

Denoting the values of the constant coefficients by p and q (i.e., $p = p _ { 1 } = p _ { 2 } ,$ and $q = q _ { 1 } = q _ { 2 } )$ , we have $F ( t ) = F _ { 1 } ( t ) = F _ { 2 } ( t )$ and $f ( t ) = f _ { 1 } ( t ) = f _ { 2 } ( t )$ , œt. Problem (18) then becomes

$$
\begin{array}{c} \operatorname{MAX} _ {\alpha_ {2} \leq \tau_ {2} \leq D} \pi (\tau_ {2}) = \\ \pi_ {1} \left[ m _ {1} F (D) - m _ {1} \int_ {\tau_ {2}} ^ {D} f (\theta) F (\theta - \tau_ {2}) d \theta \right] \\ + \pi_ {2} \left[ m _ {2} + m _ {1} F (D) \right] F (D - \tau_ {2}) \end{array}\tag{19}
$$

It is important to note that under a finite planning horizon, full market penetration is not possible. The proportion of market penetration of the two product generations, and hence the expected profit, depends on the length of the planning horizon and market entry timing. Using the GNB model, we find that delaying the introduction of G2 allows G1 to reach a larger portion of its potential adopters (represented by $m _ { 1 } )$ , which leads to less leapfrogging and more switching to G2. This is beneficial to a firm because switching implies acrossgeneration repeat purchases while leapfrogging does not. On the other hand, delaying the market entry of G2 results in fewer adoptions by those who are only interested in G2 (counted in $m _ { 2 } ) _ { : }$ , because a larger portion of the planning horizon will lapse when G2 enters the market.

![](/api/attachments/WQAAJJ37/fulltext/images/2bc97a963c74558a1700be5e26a8b173cd4c7bb3852eda8f2365df5c24fb4c4c.jpg)  
Figure 4. Adoption Rate under Total Transition

Regarding the optimal market entry timing under Scenario I, we have the following result:

Proposition 1. For PTO products under phase-out transition, it is always optimal to introduce the second generation sometime before the end of the planning horizon $( D )$ . Specifically, there exists a positive φ such that

$$
\left\{ \begin{array}{l l} \tau_ {2} ^ {*} <   D - \varphi , & i f \varphi <   D - \alpha_ {2} \\ \tau_ {2} ^ {*} = \alpha_ {2}, & i f \varphi \geq D - \alpha_ {2} \end{array} \right.
$$

where $a _ { 2 } \geq 0$ represents the earliest possible introduction time for the second generation.<sup>6</sup>

Proposition 1 can be illustrated by Figure 6. If φ (expression provided in the proof of Proposition 1 in the Appendix) is smaller than $( D - a _ { 2 } )$ , G2 should be introduced to the market at a time between $a _ { 2 }$ (inclusive) and $( D - \varphi )$ . If φ is greater than or equal to $( D - a _ { 2 } )$ , G2 should be introduced as early as possible $\operatorname { ( i . e . , } \tau _ { 2 } ^ { * } = a _ { 2 } )$ .

Note that similar to prior research, here we assume the expected profit per unit sale is fixed for both generations. Therefore, the total profit generated from both product generations depends on the numbers of adoptions of G1 and G2 and their relative unit contribution margins. When the unit contribution margin for G2 is at least as high as that for

![](/api/attachments/WQAAJJ37/fulltext/images/014ff1bd309312dbe1df55313a15b3fb026eea61bc8d74a54e6890c49b7a3fc0.jpg)  
Figure 5. Units-in-Use under Total Transition

G1 $( \pi _ { 1 } \ \leq \ \pi _ { 2 } ) .$ , introducing G2 at any time $\tau _ { 2 }$ during the planning horizon (even $\mathrm { i f } \tau _ { 2 }$ is not the optimal time) is always better than not introducing G2 at all. This is because switching from G1 to G2 and the adoptions by the G2-specific adopters both strictly increase the profit, and leapfrogging from G1 to G2 does not decrease the profit when $\pi _ { 1 } \leq \pi _ { 2 }$

In case the unit contribution margin for G2 is less than that for G1 $( \pi _ { 1 } > \pi _ { 2 } )$ , each leapfrogging reduces the profit by $( \pi _ { 1 } - \pi _ { 2 } )$ while each switching or each initial adoption by a G2-specific adopter increases the profit by $\pi _ { 2 } .$ Even if the benefit is less than the cost when G2 is introduced early in the planning horizon, the benefit/cost ratio will increase as the introduction time moves closer to the end of the planning horizon. The reason is that as the introduction time $\left( \tau _ { 2 } \right)$ of G2 is delayed, more potential adopters would have adopted G1 by time $\tau _ { 2 } ,$ hence the rate of leapfrogging after $\tau _ { 2 }$ will decrease, while the rate of switching will increase. Therefore, the total benefit can exceed the total cost of introducing G2 before the end of the planning horizon.

From Proposition 1, we conclude that regardless of the length of the planning horizon, the relative unit contribution margin, the relative market potential, and the projected diffusion curves of the two generations, it is always optimal to introduce the second generation PTO product sometime during the planning horizon.

We believe that our finding has empirical support. First, it is frequently observed that firms introduce a new generation a few years after the older generation entered the market. Second, there are many reported real-world examples that firms intentionally delayed the introduction of a new innovation to achieve a higher benefit. Examples include the Microsoft Longhorn operating system, Intel’s Camino chipset, and other innovations such as DVD, MP3, and 3G Cellular networks (Wang and Hui 2005, 2010). These examples show that the entry timing can indeed lie between “now” and the end of the planning horizon.

![](/api/attachments/WQAAJJ37/fulltext/images/64ed119c38bcb00564e622517f2cfd14075ca468120575c50f938cc4d99087d5.jpg)  
Figure 6. Illustration of Proposition 1

Proposition 2. For PTO products under phase-out transition, if the unit contribution margin for the second generation (π ) is equal to or greater than that for the first generation $( \pi _ { 1 } )$ and the planning horizon (D) is shorter than or equal to $l n ( q / p ) / ( q + p )$ , then it is optimal to introduce the second generation as early as possible. Formally,

$$
\tau_ {2} ^ {*} = \alpha_ {2}, i f \pi_ {1} \leq \pi_ {2} a n d D \leq \ln (q / p) / (p + q)
$$

Proposition 2 provides a sufficient (but not necessary) condition for introducing the new generation as early as possible. It is important to note that the condition requires assessing not only the relative contribution margins of G1 and G2, but also the duration of the planning horizon. According to Bass (1969), the time of peak diffusion for G1 (assuming that leapfrogging does not occur and the planning horizon is sufficiently long) is reached at $T ^ { * } { = } \ln ( q / p ) / ( p + q )$ . For some new products, especially in a volatile market, a firm’s planning horizon could be much shorter than the time to peak. From Proposition 2, we conclude that if the planning horizon is shorter than $T ^ { * }$ and the unit contribution margin for the second generation is at least as high as that for the first generation, the second generation should be introduced as early as possible.

To gain a better understanding of the analytical results, we conduct numerical analyses to further examine how the market entry timing of G2 affects the generational adoptions and the total profit. In order to have a broad representation of today’s market, we estimate the Bass model parameter values based on the 1999–2011 sales data for three popular consumer electronics products (standard cell phone, digital TV, and MP3 player) and adopt their averages $( \mathrm { i . e . , } p = 0 . 0 0 8 5 5$ and $q = 0 . 4 2 9 ) . ^ { 7 }$ The market potentials for G1 and G2 are set to $m _ { 1 } = m _ { 2 } = 1 0$ million. The unit contribution margins are assumed to be $\pi _ { 1 } = \pi _ { 2 } = \mathbb { S } 1 0 0$ . In addition, we assume that G2 is available for market introduction at time zero.

We first try two planning horizons at $D = 1 0$ and 20 years, and record how the total profit changes with the entry timing of G2. The results are shown in Figures 7(a) and 7(b). From these figures, we observe that the total profit decreases monotonically when $D = 1 0$ years, whereas it first increases and then decreases when $D = 2 0$ years. Therefore, when the planning horizon is D = 10 years, the optimal market entry timing for G2 is $\tau _ { 2 } ^ { * } { = } 0$ , implying that it is optimal to introduce G2 at the same time as G1, and the resulting total profit is $\pi ^ { * }$ = \$1.39 billion. When the planning horizon is extended to D = 20 years, the optimal market entry timing changes to $\tau _ { 2 } ^ { * } =$ 4.73 years, and the total profit is $\pi ^ { * } = \mathbb { S } 2 . 6 8$ billion.

Additional analyses show that the optimal entry timing for G2 increases monotonically with the duration of the planning horizon. This is because with a longer planning horizon, a firm can delay the release of G2 to increase the number of adoptions of G1 and subsequently cross-generation repeat purchases, while still leaving plenty of time for existing adopters to switch to G2 and for G2-specific potential adopters to adopt the new generation.

Proposition 1 states that never cannot be an optimal solution under Scenario I. The numerical solutions further confirm that the optimal entry timing for G2 can be now, before maturity (i.e., $T ^ { * } = 8 . 9 5$ years for G1), or after maturity. We would like to note that there are real-world examples in which a new product generation was introduced before the maturity stage of an old generation. For instance, Apple Inc. launched its new iPad 3 in March 2012, even though the sales of iPad 2 (launched in March 2011) were still on a strong upward trajectory (Olanoff 2012), implying that its maturity stage has not arrived yet.

![](/api/attachments/WQAAJJ37/fulltext/images/f148535e415e75eb7c8427a93d778327412b61fd95cd2578f341e32d949aeb0d.jpg)

![](/api/attachments/WQAAJJ37/fulltext/images/ee8439bfe8adc129762adba1b7d89299c81c20e786be712335d5071c451650eb.jpg)  
Figure 7. How the Profit and Cross-Generation Adoptions Change with Entry Timing

## Scenario II: PTO Products under Total Transition

For PTO products under total transition, since G1 is discontinued after the introduction of G2, all potential adopters who would have adopted G1 will leapfrog to G2 instead.

The total profit under Scenario II can be obtained based on Equation (16). Therefore, the problem for deciding the profitmaximizing market entry timing for G2 is formulated as

$$
\underset {\alpha_ {2} \leq \tau_ {2} \leq D} {\text { MAX }} \pi (\tau_ {2}) = \pi_ {1} \dot {Y} _ {1} (\tau_ {2}) + \pi_ {2} \dot {Y} _ {2} (D)\tag{20}
$$

where $\dot { Y } _ { 1 } \left( t \right)$ and $\dot { Y } _ { 2 } \left( t \right)$ are defined in Equations (12) and (13), respectively.

We still assume that the coefficients of innovation and imitation remain the same across generations, implying $F ( t )$ $= F _ { 1 } ( t ) = F _ { 2 } ( t )$ and $f ( t ) = f _ { 1 } ( t ) = f _ { 2 } ( t )$ , œt. Then (20) becomes

$$
\begin{array}{c} \underset {\alpha_ {2} \leq \tau_ {2} \leq D} {\text {MAX}}   \pi (\tau_ {2}) = \pi_ {1} m _ {1} F (\tau_ {2}) \\ + \pi_ {2} [ m _ {2} + m _ {1} F (\tau_ {2}) ] F (D - \tau_ {2}) \\ + \pi_ {2} m _ {1} [ F (D) - F (\tau_ {2}) ] \end{array}\tag{21}
$$

Unlike under Scenario I (PTO products under phase-out transition), we are able to obtain a closed-form solution for (21) under a common scenario. The detailed derivation is provided in the Appendix.

More interestingly, we find analytically that never could be an optimal solution under Scenario II, as stated in the following proposition:

Proposition 3. For PTO products under total transition, if the unit contribution margin for the second generation is equal to or greater than that for the first generation, it is always optimal to introduce the second generation sometime during the planning horizon. If the unit contribution margin for the second generation is less than that for the first generation, not introducing the second generation during the planning horizon could be an optimal solution.

When the unit contribution margin for G2 is at least as high as that for ${ \mathrm { G } } 1 \left( \pi _ { 1 } \leq \pi _ { 2 } \right)$ , the conclusions of Proposition 1 and Proposition 3 are the same, and the interpretations for Scenario I (PTO products under phase-out transition) (see discussion after Proposition 1) remain valid for Scenario II (PTO products under total transition). In case $\pi _ { 1 } > \pi _ { 2 } ,$ the conclusion is in clear contrast to Proposition 1 (for phase-out transition). The differences in findings under phase-out and total transitions can be explained as follows:

For PTO products, under total transition, introducing G2 is less profitable than under phase-out transition for two reasons. First, all else being equal, there are more leapfroggers under total transition than under phase-out transition. Since $\pi _ { 2 } < \pi _ { 1 }$ , more leapfrogging leads to higher revenue loss.

Second, although the introduction of G2 can lead to switching and hence cross-generation repeat purchases, all else being equal, the number of repeat purchases is lower under total transition than that under phase-out transition. This implies that the benefit derived from repeat purchases is lower. With both factors considered, it is clear that the cost of introducing G2 is higher and the benefit is lower under total transition than under phaseout transition, hence not introducing G2 could be an optimal solution under total transition.

To illustrate, we adopt the same parameter values used in the previous subsection. With a short planning horizon of 10 years, the optimal solution is obvious $( \mathrm { i } . \mathrm { e } . , \tau _ { 2 } ^ { * } = 0 )$ . When the planning horizon increases to 20 years, the optimal entry timing for G2 equals $\tau _ { 2 } ^ { * } = 7 . 4 0$ years. Again, as the duration of planning horizon increases, it is beneficial to delay the market entry timing.

We also examine the less likely scenario with $\pi _ { 1 } > \pi _ { 2 } .$ Specifically, we let $\pi _ { 1 } = \mathbb { S } 1 0 0 , \pi _ { 2 } = \mathbb { S } 4 0$ , and $D = 1 0$ years. The optimal solution is found to be $\tau _ { 2 } ^ { * } > 1 0$ years, implying that G2 should not be introduced during the planning horizon, a result consistent with Proposition 3.

## Market Entry Timing for STU Products

We now derive the market entry timing for the two-generation case for STU products. Unlike PTO products, customers do not pay a one-time fee to gain permanent access to a STU product; instead, the fee is calculated based on how long the customer consumes the product or service. From a modeling perspective, a key difference between PTO and STU is that under the former, the profit at any given point in time depends on the instantaneous adoption rate; while for the latter, the profit depends on the number of units-in-use at any given time.

In terms of revenue implications, there are two important differences between STU and PTO products. First, for STU products, whether a customer adopts G2 through leapfrogging or switching does not affect the firm’s revenue from G2, because the revenue is not generated through one-time product sale. For PTO products, however, switching is more beneficial than leapfrogging. Second, for an STU product, how long the product is being consumed by users directly affects a firm’s revenue, while for a PTO product, the duration of usage has no direct effect on revenue.

We examine both Scenario III (STU products under phase-out transition) and Scenario IV (STU products under total transition) summarized in Table 1. Under Scenario III, the total profit can be estimated from Equation (9). Therefore, the optimal market entry time for G2 can be obtained by

$$
\begin{array}{c} \underset {\alpha_ {2} \leq \tau_ {2} \leq D} {\text { MAX }} \pi (\tau_ {2}) = \varphi_ {1} \int_ {0} ^ {D} S _ {1} (\theta) d \theta + \\ \varphi_ {2} \int_ {\tau_ {2}} ^ {D} S _ {2} (\theta) d \theta \end{array}\tag{22}
$$

where $S _ { 1 } ( t )$ and $S _ { 2 } ( t )$ are defined in Equations (1) and (2), respectively.

For Scenario IV, the total profit can be estimated based on Equation (17). Hence the problem is formulated as

$$
\begin{array}{c} \underset {\alpha_ {2} \leq \tau_ {2} \leq D} {\text { MAX }} \pi (\tau_ {2}) = \varphi_ {1} \int_ {0} ^ {D} \dot {S} _ {1} (\theta) d \theta + \\ \varphi_ {2} \int_ {\tau_ {2}} ^ {D} \dot {S} _ {2} (\theta) d \theta \end{array}\tag{23}
$$

where ${ \dot { S } } _ { 1 } \left( t \right)$ and $\dot { S } _ { 2 } \left( t \right)$ are given in Equations (14) and (15), respectively.

We again let $p = p _ { 1 } = p _ { 2 }$ and $q = q _ { 1 } = q _ { 2 }$ . Problem (22) then becomes

$$
\begin{array}{c} \underset {\alpha_ {2} \leq \tau_ {2} \leq D} {\text { MAX }} \pi (\tau_ {2}) = \varphi_ {1} \int_ {0} ^ {D} m _ {1} F (\theta) [ 1 - F (\theta - \tau_ {2}) ] d \theta + \\ \varphi_ {2} \int_ {\tau_ {2}} ^ {D} [ m _ {2} + m _ {1} F (\theta) ] F (\theta - \tau_ {2}) d \theta \end{array} \tag {24}
$$

and problem (23) changes to

$$
\begin{array}{l} \underset {\alpha_ {2} \leq \tau_ {2} \leq D} {\text { MAX }} \pi (\tau_ {2}) = \varphi_ {1} m _ {1} \int_ {0} ^ {\tau_ {2}} F (\theta) d \theta + \\ \varphi_ {1} \int_ {\tau_ {2}} ^ {D} \dot {S} _ {1} (\theta) d \theta + \varphi_ {2} \int_ {\tau_ {2}} ^ {D} \dot {S} _ {2} (\theta) d \theta \end{array}\tag{25}
$$

It is worth noting that for STU products, whether the generation transition strategy is phase-out or total transition is less important than it is for PTO products. Furthermore, if the unit contribution margins for the two generations are close, when a customer leapfrogs/switches from G1 to G2 has little impact on the total profit. Therefore, despite the difference in model formulations, our analytical and numerical findings for Scenarios III and IV are similar. For this reason, unless necessary, we do not differentiate Scenarios III and IV in the remaining discussion.

We would like to emphasize that for STU products, the total profit depends on not only the number of adopters of each service, but also the duration of each service being consumed. Therefore, all else being equal, delaying the introduction of G2 is more costly for STU products because it reduces the average duration of G2 being consumed by customers.

For most service types, G2 is expected to be at least as profitable as G1 per unit time of service $\left( \varphi _ { 1 } \leq \varphi _ { 2 } \right)$ . Under this condition, we have the following finding:

Proposition 4. For STU products, if the unit contribution margin for the second generation is equal to or greater than that for the first generation, it is always optimal to introduce the second generation as early as possible.

Proposition 4 can be explained as follows: If G2 is introduced earlier, although the number of switchings during the planning horizon may either increase or decrease, we can tell from Equations (1) and (2) or Equations (14) and (15) that the sum of the numbers of leapfroggings and switchings can only increase. Because G2 is at least as profitable as G1, more leapfroggings or switchings from G1 to G2 can never decrease the revenue. Furthermore, an earlier market entry time allows G2 to be used longer during the planning horizon, and more G2-specific potential adopters (represented by m<sub>2</sub>) can adopt G2 by the end of the planning horizon, thus leading to higher revenue for the firm. Therefore, G2 should be introduced as soon as possible.

We again take the cellular phone service as an example. If the unit contribution margin for 4G service is at least as high as that for 3G, then 4G service should be introduced as soon as it becomes available. This is because customers’ leapfrogging or switching from 3G to 4G service cannot decrease the profit; and potential customers who are waiting for 4G service can start adopting the service earlier, thus increasing the total profit during the planning horizon.

We also would like to emphasize that Proposition 4 does not hold for PTO products, which shows that the revenue model adopted by a firm does affect its optimal market entry strategy.

In case the new generation is not as profitable as the old generation per unit time of service $( \varphi _ { 1 } > \varphi _ { 2 } )$ , we have the following conclusion:

Proposition 5. For STU products, even if the unit contribution margin for the second generation is less than that for the first generation, it is still optimal to introduce the second generation as early as possible if the market potential specific to the second generation is sufficiently large.

This proposition shows that a large market potential for G2 can compensate its lower contribution margin. Specifically, if G2 is not as profitable as G1, then whenever a customer shifts to G2, either through leapfrogging or switching, the firm’s profit drops. However, if the number of potential adopters who are only interested in G2 (i.e., the market potential specific to G2) is sufficiently large, the loss can be compensated by the additional revenue generated from such adopters. Therefore, even if the unit contribution margin for the second generation is less than that for the first generation, introducing G2 at the earliest date may still be optimal if the market potential for G2 is sufficiently large. If the market potential for G2 is not sufficiently large, we find that a firm should either introduce it late in the planning horizon or not introduce it at all.

For numerical illustration, we adopt a dataset that includes the numbers of analog and digital cellular phone subscribers in the United States. The estimated parameter values are $p =$ 0.0158, $q = 0 . 2 7 9 , m _ { 1 } = 3 8 . 6 8$ million, and $m _ { 2 } = 3 1 8 . 0 6$ million. The unit contribution margin for one year’s cellular service is set to $\varphi _ { 1 } = \varphi _ { 2 } = \mathbb { S } 2 0 0$ . We again assume that G2 is available for release at time zero. We find that regardless of the duration of planning horizon $( \boldsymbol { \mathrm { e } } . \boldsymbol { \mathrm { g } } . , D = 1 0$ or 20 years), the optimal introduction time for G2 is always $\tau _ { 2 } ^ { * } = 0 .$ , a result consistent with Proposition 4.

To understand the solution under the less likely scenario where G2 is less profitable than G1, we let $\varphi _ { 1 } = \mathbb { S } 2 0 0 { \mathrm { ~ a n d ~ } } \varphi _ { 2 }$ = \$100, and vary the value of $m _ { 2 } ,$ which represents the incremental market size for G2 after it is introduced. The planning horizon is fixed at D = 10 years.

As shown in Figure 8(a), with $m _ { 2 } = 2 0$ million, the total profit decreases monotonically as the introduction of G2 is delayed. Hence, it is optimal to introduce G2 as early as possible (i.e., now). When $m _ { 2 }$ decreases to 12 million, the total profit first decreases and then increases as $\mathrm { G } 2 \mathrm { : } \mathrm { s }$ introduction is postponed (see Figure 8(b)). Since the highest profit is achieved at $\tau _ { 2 } ^ { * } { = } 0$ years, G2 should again be introduced now. When $m _ { 2 }$ is further reduced to $m _ { 2 } = 1 1$ million, as shown in Figure 8(c), the impact of the entry time on the total profit is also nonmonotonic; the highest profit, however, is achieved at $\tau _ { 2 } ^ { * } > 1 0$ years, hence G2 should not be introduced during the planning horizon (i.e., never).

To verify whether the optimal market entry timing can lie between now and never, we vary the values of $m _ { 2 }$ by increasingly smaller increments, and find that the optimal solution still exhibits the interesting now or never pattern, similar to the finding reported by Wilson and Norton (1989). Specifically, the optimal entry timing for G2 is always now (τ<sup>\*</sup> = 0) when $m _ { 2 } \geq 1 1$ 1.64 million, and the solution jumps to never $( \tau _ { 2 } ^ { * } > 1 0$ years) when $m _ { 2 } \leq 1 1 . 6 3$ million. In addition, we find that a similar threshold exists for the unit contribution margin for G2 $\left( \varphi _ { 2 } \right)$ , around which a very small change in the parameter value can change the optimal entry timing from now to never.

![](/api/attachments/WQAAJJ37/fulltext/images/7c5739ff7b137348d4781ab85b14acfeb67fe3af9ea1583e21db1a02ea6332df.jpg)

![](/api/attachments/WQAAJJ37/fulltext/images/e81aff284010a61bb67490083cb499d3e9088829135ef174b3b25e4264e833f6.jpg)  
(b) m2 = 12, τ2 = 0, "Now"

![](/api/attachments/WQAAJJ37/fulltext/images/b2f617ae6b924f59b84bb70ba6a6271e0eeda5fe1a0aef9e673cc624ee0bb966.jpg)  
(c) m2 = 11, τ2>D, "Never"  
Figure 8. Now or Never Depending on the Incremental Market Size for G2

The mathematical explanation for the now or never rule can be better understood from Figure 8. Since the curves representing the total profit either decreases monotonically (Figure 8a)) or first decreases and then increases (Figures 8b) and 8c)), the maximum profit can only be achieved at the two ends (time 0 as in Figures 8a) and 8b), time 10 as in Figure 8c)) of the planning horizon, implying that the optimal market entry timing is either now or never.

The economic reason behind the now or never rule is as follows. Note that never can be an optimal solution only if the unit contribution margin for G2 is less than that for G1 (φ $> \varphi _ { 2 } )$ In this case, although a firm loses money when leapfrogging or switching occurs, it benefits from capturing the G2-specific potential adopters. If such benefit, which depends on the G2-specific market size $\left( m _ { 2 } \right)$ and the unit contribution margin for ${ \bf G } 2 \left( \varphi _ { 2 } \right)$ , is greater than the expected loss, G2 should be introduced as early as possible; otherwise it should not be introduced.

We would like to point out that there are similarities and differences between our finding and the now or never conclusion in Wilson and Norton. Both findings are under the condition that the unit contribution margin for G2 is lower than that for G1. The difference is that Wilson and Norton derive the finding for PTO products, whereas our finding is valid only for STU products. It is very interesting to observe that the conclusion of the prior study remains valid in this study, although for completely different business scenarios.

## Optimal Market Entry Timing under an Infinite Planning Horizon

The findings presented in the previous two sections are derived based on a finite planning horizon, which, according to our literature search, is the most commonly seen in the prior literature and most frequently adopted in practice (e.g.,

Guo and Chen 2018; Klemme and and Schoney 1984). However, since some prior research on market entry timing (e.g., Mahajan and Muller 1996) has considered an infinite time horizon, for the purpose of theoretical comparison, we now examine whether the findings derived for a finite planning horizon remain valid under an infinite planning horizon.

## PTO Products

We first consider Scenario I for PTO products under phaseout transition. With an infinite planning horizon, problem (19) changes to

$$
\begin{array}{r l} \underset {\alpha_ {2} \leq \tau_ {2} \leq \infty} {\text { MAX }} & \pi (\tau_ {2}) = \pi_ {1} \left[ m _ {1} F (\infty) - m _ {1} \int_ {\tau_ {2}} ^ {\infty} f (\theta) F (\theta - \tau_ {2}) d \theta \right] \\ & + \pi_ {2} \left[ m _ {2} + m _ {1} F (\infty) \right] F (\infty - \tau_ {2}) \end{array}
$$

Since $F ( \infty ) = 1$ , the problem can be simplified to

$$
\begin{array}{c} \operatorname{MAX} _ {\alpha_ {2} \leq \tau_ {2} \leq \infty} \pi (\tau_ {2}) = \pi_ {1} m _ {1} - \\ \pi_ {1} m _ {1} \int_ {\tau_ {2}} ^ {\infty} f (\theta) F (\theta - \tau_ {2}) d \theta + \pi_ {2} (m _ {1} + m _ {2}) F (\infty - \tau_ {2}) ^ {(2 6)} \end{array}
$$

Because there is no closed-form solution to problem (19), under a finite planning horizon, the optimal market entry timing can only be numerically obtained. Under an infinite planning horizon, we next show that the optimal solution to problem (26) can be obtained without numerical analysis.

In the objective function of (26), the first term represents the total profit generated from G1, assuming all potential adopters will adopt G1, the second term is the loss of profit due to leapfrogging from G1 to G2 (i.e., potential adopters skipping G1 and directly adopting G2) and the third term represents the total profit generated from G2. With any finite $\tau _ { 2 } ,$ the third term equals $\pi _ { 2 } ( m _ { 1 } + m _ { 2 } )$ . Therefore, the key to this optimization seems to be to minimize the number of leapfroggers, or the second term of the objective function.

How can the number of leapfroggers be minimized? The answer is to delay the release of G2 as much as possible until every single potential adopter of G1 has purchased G1. Mathematically, this suggests that $\tau _ { 2 } ^ { * } = \infty ,$ since from Equation (7), we have $F _ { 2 } ( \infty ) = 1$ . Apparently, the solution is not ideal even for a theoretical exploration since the time left for G2 (4, 4) is mathematically not well defined.

Further examination shows that $F _ { 2 } ( t )$ will become close to 1 very quickly as t increases. For instance, suppose the market potential for G1 is $m _ { 1 } \ = \ 1 { , } 0 0 0 .$ and the coefficient of innovation (p) and coefficient of imitation (q) for a PTO product take their average values reported in the prior literature (Sultan et al. 1990) (i.e., $p = 0 . 0 3 , q = 0 . 3 8 )$ , then a 99.95% market penetration can be achieved at t = 24.92 years. Since $Y _ { 1 } ( 2 4 . 9 2 ) = 1 , 0 0 0 \times 9 9 . 9 5 \% = 9 9 9 . 5 \approx 1 , 0 0 0$ after rounding, for practical purpose, 99.95%, or even a slightly lower percentage, might be as good as “full market penetration” to a firm. By defining such a (practical) full market penetration, which can be achieved in finite time, we eliminate the mathematical problem mentioned earlier. Subsequently, we can choose the time at which a (practical) full market penetration is achieved, which can vary with the values of p and q, as the optimal time to introduce the new generation G2.

We also examine Scenario II, PTO products under total transition. It turns out that the profit is also maximized when G2 is introduced after G1 has achieved full market penetration. At this optimal solution, the difference between phase-out transition and total transition disappears. Therefore, we have the following conclusion:

Under infinite planning horizon, it is optimal to introduce the new generation (G2) when the first generation (G1) has achieved full market penetration.

## STU Products

For STU products, the optimal entry timing cannot be obtained by evaluating the objective functions of (24) and (25), because they grow to infinity as the planning horizon increases to infinity. Instead, based on the (practical) full market penetration defined earlier, we next show that the infinite time horizon problem can be turned into a finite time horizon problem.

As explained in the previous section, the total profit generated from STU products depends on the units-in-use curves instead of the adoption rate curves. As shown in Figures 9 and 10, we compare two scenarios, where G2 is released at time $\tau _ { 2 }$ and $\tau _ { 2 } + \theta ,$ respectively. Subsequently, G1 will eventually be replaced by G2, and the number of units-in-use of G2 will eventually reach $m _ { 1 } + m _ { 2 }$ We denote the time of such an occurrence by $T _ { f }$ and $T _ { f } + \varepsilon ,$ , corresponding to the release time $\tau _ { 2 }$ and $\tau _ { 2 } + \theta ,$ respectively. Since the level of market penetration reaches the same level after time $T _ { f } .$ + ε under the two scenarios, their total profit from this point on cancels out. Subsequently, whether $\tau _ { 2 }$ or $\tau _ { 2 } + \theta$ is a better market entry time depends on the profit generated during the time horizon $[ 0 , T _ { f } + \varepsilon ]$ . With this construction, we can turn the otherwise infinite time horizon problem into a finite time horizon problem. As a result, the original now or never rule derived for the finite planning horizon should continue to hold.

## Summary of All Findings

Some of the results presented in this section and the previous two sections, the propositions in particular, might not directly answer the research questions we plan to address in the present research. However, these minor analytical and numerical results jointly lead to the major findings that we would like to emphasize in this research. For ease of comparison and discussion, we summarize all the major findings in Table 2.

Clearly, Table 2 shows that the optimal market entry timing depends on the types of revenue model (PTO versus STU), generation transition strategies (phase-out versus total transition), as well as length of the planning horizon (finite versus infinite). Specifically, from this table, we have several important observations.

First, we find that the generation transition strategy (phase-out transition versus total transition) has limited impact on the qualitative findings; it makes a difference only for PTO products under a finite planning horizon, where never (i.e., not introducing the second PTO product generation) can be an optimal solution under total transition, while it cannot be optimal under phase-out transition. Under an infinite planning horizon, the difference between phase-out transition and total transition disappears; it is always optimal to introduce the second PTO product generation after the first generation has reached full market penetration.

Second, extending the planning horizon from finite to infinite changes the qualitative conclusions for PTO products, but it does not change the qualitative conclusions for STU products.

![](/api/attachments/WQAAJJ37/fulltext/images/6bb59d6c11d1d4af5cdbfd2035c85c98ef23c704673bc6929f4730979a38e0e7.jpg)  
Figure 9. Units-in-Use if G2 Released at τ<sub>2</sub>

![](/api/attachments/WQAAJJ37/fulltext/images/2b13b9238c63a792498c301a083d0260b267b8cd47931fecf495de2bc3b209e4.jpg)  
Figure 10. Units-in-Use if G2 Released at τ<sub>2</sub> + θ

Table 2. Summary of Findings on Optimal Entry Timing

<table><tr><td>Planning Horizon</td><td>Revenue Model</td><td>Phase-out Transition</td><td>Total Transition</td></tr><tr><td rowspan="2">Finite</td><td>PTO</td><td>now or during planning horizon, but not never</td><td>now, during planning horizon, or never</td></tr><tr><td>STU</td><td colspan="2">now or never</td></tr><tr><td rowspan="2">Infinite</td><td>PTO</td><td colspan="2">at full market penetration of G1</td></tr><tr><td>STU</td><td colspan="2">now or never</td></tr></table>

Third, recall that the prior studies consider only Scenario I (PTO products under phase-out transition), and conclude that the second generation should be introduced now or never (Wilson and Norton 1989), or now or at maturity (Mahajan and Muller 1996). As shown in Table 2, we find that neither the now or never rule nor the now or at maturity rule holds under Scenario I.

Finally, regardless of the generation transition strategy or the length of the planning horizon, the now or never rule holds for STU products. This is a very interesting finding because the now or never rule is derived by prior studies for PTO products, but we find that it remains valid, but only for a different product type: STU products. We also would like to point out that now is more likely to be optimal for STU products than never, because the contribution margin of a new generation is likely no lower than that of an old generation.

In sum, the results summarized in Table 2 show that under today’s diverse market landscape, it is indeed necessary for firms to more carefully examine their market entry strategies, because the optimal entry timing does depend on their underlying business models and the length of the planning horizon.

## Comparison of Generation Transition Strategies and Revenue Models

So far, we have implicitly assumed that a firm’s revenue model (PTO or STU) and generation transition strategy (phase-out or total transitions) are decided before the optimal market entry timing is considered. This is because revenue model and generation transition strategy are more strategic level decisions and are likely driven by a firm’s long-term strategic plan or resource constraints. For instance, if a software vendor believes that the future of the industry lies in cloud computing, it will most likely choose the STU model instead of the PTO model, and more likely than not, such an important strategic decision would have been made well before the release of the first generation, let alone the release of the second generation. Similarly, if a firm needs to build new facilities for a new product generation, then it makes better sense for it to choose a phase-out transition instead of total transition, because the former allows the firm to continue to utilize the old facilities. On the other hand, if the firm has to use the existing facilities, and it is inefficient to support the production and distribution of two product generations, then total transition would be the better option.

What if a firm’s strategic plan is flexible and resources constraints are not binding, so that the revenue model and generation transition can be simultaneously determined with the optimal market entry strategy? We attempt to address this question in the rest of this section.

## Phase-out Transition Versus Total Transition

The difference between phase-out transition and total transition is whether an old generation continues to exist in the market after the introduction of a new generation. Under Assumption 3, since all customers who would have adopted G1 will purchase G2 instead, the profitability of the two transition strategies depends on the comparison of the two generations’ unit contribution margins. If the unit contribution margin of the second generation is higher than that of the first generation, total transition is better than phase-out transition, and vice versa.

Therefore, if the generation transition strategy is endogenized, the market entry timing can be determined in two steps: (1) based on the relative contribution margins, choose between phase-out or total transition; (2) using models proposed in the earlier sections on market entry timing, calculate the optimal market entry timing.

## PTO Versus STU

The comparison between the two revenue models, PTO and STU, is not as straightforward. This is because the comparison of total profits under the two revenue models depends on the two generations’ unit contribution margins as well as the length of the planning horizon. The impact of the unit contribution margin is obvious: as the profit generated per unit sale or per unit time of service to a customer increases, the relative profit can increase accordingly. Furthermore, since the duration of service directly affects the total profit under the STU model, while how long a product is in use has less impact on the total profit under the PTO model, the length of planning horizon also has an important effect on the profit comparison. As a result of this complexity, it is not possible to draw a general conclusion regarding whether PTO or STU is better without actually calculating the total profit.

Therefore, to determine whether PTO or STU is more profitable, we need to formulate the decision models under both options, obtain their respective optimal market entry timing, and calculate their total profits. The revenue model leading to a higher total profit should be the best model.

Numerical analysis is conducted to compare PTO or STU. The previous parameter values $( p = 0 . 0 0 8 5 5 , q = 0 . 4 2 9 , m _ { 1 } =$ $m _ { 2 } { = } 1 0 \mathrm { m i l l i o n } )$ are again used. The unit contribution margin for PTO products is set at $\pi _ { 1 } = \pi _ { 1 } = \mathbb { S } 1 0 0$ , the unit contribution margin for STU product is $\varphi _ { 1 } = \varphi _ { 1 } = \mathbb { S } 5 0$ , and the planning horizon is D = 10 years. We find that using these parameter values, PTO leads to a slightly higher profit (\$2.09 billion) than STU (\$1.97 billion), hence PTO is the better revenue model. If we increase unit contribution margin for STU slightly (e.g., \$55), STU becomes preferable to PTO. Alternatively, if the planning horizon is slightly longer (e.g., 11 years), STU also outperforms PTO. Therefore, STU is a more preferable revenue model when the ratio of unit contribution margin of STU to that of PTU is large, or when the planning horizon is long.

## Model Extensions

In the previous sections, we focus on the two-generation case and assume that a firm sells either PTO or STU products, but not both. In this section, we extend our model to analyze more general business scenarios: (1) a firm offers for sale a PTO product along with a complimentary service that can be interpreted as a STU product, (2) a product line includes three successive generations, and (3) when network effects, product compatibility, and switching cost are present. We consider only phase-out transition for all extensions.

## PTO–STU Product Bundle

For some product lines, a firm can generate revenue from selling a PTO product and a complimentary subscriptionbased service. Cellular phone bundled with cellular network service is an example of such a revenue model. Another example is that manufacturers of GPS units can benefit from both one-time sales of GPS units and subsequent sales of map updates. In yet another example, manufacturers of printers can generate revenue from initial sales of printers as well as future sales of toners or cartridges. Such product offerings can be considered bundles of PTO and STU products. We next derive the optimal entry timing for such a PTO–STU product bundle.

For a PTO–STU product bundle, the profit generated from the PTO component is proportional to the number of PTO products sold, and the profit generated from the STU component at any instant of time is always proportional to the number of units-in-use at that time. Therefore, the profit projections separately derived for PTO and STU products are still applicable for the PTO and STU components of the bundle. Thus, the optimal entry timing for the second generation of a PTO–STU product bundle can be obtained by

$$
\begin{array}{l} \text {MAX} _ {\alpha_ {2} \leq \tau_ {2} \leq D} \pi (\tau_ {2}) = \pi_ {1} Y _ {1} (D) + \pi_ {2} Y _ {2} (D) + \\ \varphi_ {1} \int_ {0} ^ {D} S _ {1} (\theta) d \theta + \varphi_ {2} \int_ {\tau_ {2}} ^ {D} S _ {2} (\theta) d \theta \\ s. t. \quad Y _ {1} (D) = m _ {1} F (D) - m _ {1} \int_ {\tau_ {2}} ^ {D} f (\theta) F (\theta - \tau_ {2}) d \theta \\ Y _ {2} (D) = [ m _ {2} + m _ {1} F (D) ] F (D - \tau_ {2}) \\ S _ {1} (t) = m _ {1} F (t) [ 1 - F (t - \tau_ {2}) ] \\ S _ {2} (t) = [ m _ {2} + m _ {1} F (t) ] F (t - \tau_ {2}) \end{array}\tag{27}
$$

From (27), the total profit for a PTO–STU product bundle can be interpreted as the weighted average of the profits for the PTO and STU components. For example, if we set the unit contribution margin for the STU component to $\scriptstyle \varphi _ { 1 } = \varphi _ { 2 } = 0$ , the formulation reduces to the PTO profit in Equation (18). Similarly, if the unit contribution margin for the PTO component is $\pi _ { 1 } { = } \pi _ { 1 } { = } 0 _ { \colon }$ , the simplified formulation represents the STU profit in Equation (22). Therefore, whether the optimal solution is consistent with the findings for PTO or STU products depends on the ratio between the unit contribution margin for the PTO component and that for the STU component.

We perform numerical analyses to examine the solutions for two different cases. In the first case, the profit resulting from the STU component of the bundle is significantly higher than the profit from the PTO component. An example is that cellular service providers typically profit more from subscription fees than from cellular phone sales. We set the unit contribution margin for cellular phone sale to $\pi _ { 1 } = \pi _ { 2 } = \mathbb { S } 2 0$ and the unit contribution margin for cellular network service to $\varphi _ { 1 } = \varphi _ { 2 } = \mathbb { S } 2 0 0$ . Three different planning horizons (20, 25, and 30 years) are tried, and the solutions all suggest that it is optimal to introduce G2 as early as possible $( \mathrm { i } . \mathrm { e } _ { \cdot } , \tau _ { 2 } ^ { \ast } = 0 )$ . This is expected because the profit from the STU component dominates the profit from the PTO component and, based on Proposition 4, the profit from a STU product is maximized at $\tau _ { 2 } ^ { * } = 0$

In the second case, a firm derives revenue primarily from a PTO component instead of a STU component. An example is that refrigerator manufacturers profit mainly from selling refrigerators instead of water filters. For illustration, we change the unit contribution margins to $\pi _ { 1 } = \pi _ { 2 } = \mathbb { S } 2 0 0$ and $\varphi _ { 1 }$ $\mathbf { \Phi } = \varphi _ { 2 } = \mathbb { S } 1$ , and set the planning horizon to 30 years. The optimal introduction time for G2 is found to be $\bar { \tau _ { 2 } ^ { * } } = 1 . 7$ years. In this case, since the unit contribution margin for the PTO component is significantly higher than that for the STU component, slightly delaying the introduction of G2 can lead to more cross-generation repeat purchases and a higher profit.

## Three Product Generations

We now demonstrate how the optimal market entry timing can be determined for a three-generation case. We consider only PTO products under phase-out transition for illustration purposes.

The GNB model (Jiang and Jain 2012) is again used to project the adoption rates for all three generations. The optimal market entry timing for G2 and G3 can be determined based on

$$
\begin{array}{c} \operatorname{MAX} _ {\alpha_ {2} \leq \tau_ {2} \leq \tau_ {3} \leq D} \pi (\tau_ {2}, \tau_ {3}) = \pi_ {1} Y _ {1} (D) \\ + \pi_ {2} Y _ {2} (D) + \pi_ {3} Y _ {3} (D) \\ s. t. \quad Y _ {1} (D) = m _ {1} F (D) - m _ {1} \int_ {\tau_ {2}} ^ {D} f (\theta) F (\theta - \tau_ {2}) d \theta \\ Y _ {2} (D) = [ m _ {2} + m _ {1} F (D) ] F (D - \tau_ {2}) \\ - \int_ {\tau_ {3}} ^ {D} [ (m _ {2} + m _ {1} F (\theta)) f _ {2} (\theta - \tau_ {2}) \\ + m _ {1} f (\theta) F (\theta - \tau_ {2}) ] F (\theta - \tau_ {3}) d \theta \\ Y _ {3} (D) = \left\{m _ {3} + [ m _ {2} + m _ {1} F (D) ] F (D - \tau_ {2}) \right\} \\ F (D - \tau_ {3}) \end{array}\tag{28}
$$

We use the average parameter values reported in prior research (Sultan et al. 1990), that is, $p = 0 . 0 3 , q = 0 . 3 8$ , in the numerical analysis. The market potentials for the three generations are set to $m _ { 1 } = 1 0 0$ million, $m _ { 2 } = 2 0 0$ million, and $m _ { 3 } = 3 0 0$ million. The unit contribution margins are assumed to be equal across generations: $\pi _ { 1 } = \pi _ { 2 } = \pi _ { 3 } = \mathbb { S } 2 0$ The planning horizon is first set to $D = 3 0$ years, and the profitmaximizing introduction time is found to be $\tau _ { 2 } ^ { * } = 5 . 0$ years for G2 and $\tau _ { 3 } ^ { * } = 1 4 . 1$ years for G3. If the planning horizon is reduced to $D = 2 5$ years, it is optimal to introduce both generations a few years earlier: G2 at $\tau _ { 2 } ^ { * } = 2 . 4$ years for and G3 at $\tau _ { 3 } ^ { * } = 1 0 . 3$ years. With an even shorter planning horizon $D = 2 0$ years, the optimal solution is $\tau _ { 2 } ^ { * } = 0 . 0$ years and $\tau _ { 3 } ^ { * } =$ 6.5 years. We again find that the shorter the planning horizon, the earlier should G2 and G3 be introduced, and that the optimal entry timing can be now, before maturity, or after maturity.

## Network Effects, Compatibility, and Switching Cost

As is customary in the product diffusion literature, so far we have implicitly assumed that network effects, product compatibility, and switching cost are either exogenous or negligible. In a third extension model, we examine how these additional economic factors can affect the new generation’s optimal market entry timing and the total profit. Due to space limitations, we only summarize the key findings while relegating the detailed analysis to the Appendix.

Briefly, in the presence of network effects, we find that the impact of within-generation network effects on the optimal market entry timing for a new product generation is not monotonic: as the intensity of within-generation network effects increases from a low level, the optimal market entry timing first decreases (shorter time to market) and then increases (longer time to market). The benefit generated from network effects and the optimal market entry timing are also affected by backward and forward compatibility. Specifically, we find that a higher backward compatibility leads to a delayed optimal market entry timing, and higher forward compatibility leads to an earlier optimal release time. Furthermore, our results show that a larger switching cost leads to an earlier optimal market entry timing for the new generation.

## Conclusions and Future Research Directions

The IT product market is characterized by breathtaking speed of technological advancements and frequent releases of new hardware products, software products, and services. Successful management of new generations of technological products can bring many benefits. For instance, it can lead to better customer satisfaction, and can help a firm sustain its revenue stream from a relatively constant customer base.

Despite its importance, prior research on market entry timing for successive product generations has been limited. This study fills this void by developing analytical models to derive the optimal market entry timing for new product generations under a variety of business scenarios that are frequently observed in today’s diverse market landscape. In particular, in addition to purchase-to-own (PTO) products, we also consider subscribe-to-use (STU) products that are becoming increasingly popular in the IT industry’s move toward cloud computing. To the best of our knowledge, the present research is the first to propose a generalized modeling framework to derive market entry timing for multiple business scenarios.

One of our main methodological contributions is that we develop several extension multigeneration models to estimate the sales under different market scenarios, including the extension model for total transition, and the revenue model for PTO–STU product bundles. These diffusion models are essential for developing subsequent decision models to derive the optimal market entry timing. To the best of our knowledge, no similar models have been proposed in prior studies.

Based on the proposed multigeneration modeling framework, we are able to derive several important findings. Specifically, for PTO products under a finite planning horizon, if an old generation can remain on the market with a new generation, we find that, irrespective of the relative profits or market sizes of the two generations, it is always beneficial to introduce the new generation either now or sometime during the planning horizon. Never (i.e., not introducing the new generation during the planning horizon) cannot be an optimal solution. If an old PTO product generation is completely replaced by a new generation upon the latter’s release, now, sometime during the planning horizon, or never all can be optimal solutions. Under an infinite planning horizon, the difference between phase-out transition and total transition disappears, and the second PTO product generation should not be released until the first generation has reached complete market penetration.

For subscribe-to-use (STU) products, the optimal market entry timing for the second generation is either now or never. Furthermore, for STU products, now or never is the optimal entry timing regardless of the generation transition strategy and the length of planning horizon. This now or never rule was originally discovered by Wilson and Norton (1989) for PTO products. Unlike the prior study, we find that the rule holds for STU products, but not for PTO products. It is very interesting to observe that the conclusion of a prior study remains valid in this study, although for a completely different business scenario.

The analytical models and findings have significant practical implications. As explained earlier, successive releases of new product generations are critical for a firm’s market survival and profitability, hence making informed market entry timing decisions is of strategic importance to firms. The models developed in this study have several important advantages that help firms make better market entry timing decisions. First, unlike some prior studies that focus on qualitative explorations of economic phenomena, the models we develop in this study can be operationalized once the model parameter values are estimated. Second, the proposed models provide a broad coverage of today’s diverse market landscape, including not only the four base business scenarios, but also more complex ones such as product and service bundle and multiple product generations. Third, we have clearly spelled out the differences in optimal market entry timing for different business scenarios. This can help decision makers reduce the chance of making suboptimal decisions or mistakes even under incomplete information (e.g., when some parameter values could not be easily obtained).

There exist several interesting future research directions. First, the present study treats product quality as exogenously given. In a future study, one could endogenize consumers evaluation of product quality, and develop a more comprehensive model to determine the optimal product quality for each generation along with the optimal market entry timing. Second, marketing mix variables such as pricing and advertising are not considered in this study. It would be interesting to analyze how pricing and advertising affect a firm’s market entry timing decision, and then derive a profit-maximizing solution with the best combination of market entry timing and pricing/advertising policies. Third, analogous to most research on market entry timing, the present research focuses on the monopolist case only. A future study could examine how competition affects the adoption of different generations of the same brand as well as across brands, and analyze how market entry timing can be leveraged to achieve a favorable market position.

## Acknowledgments

The authors would like to thank the senior editor, Bin Gu, the associate editor, and the two anonymous reviewers for their constructive comments and suggestions. Xinxue (Shawn) Qu served as the corresponding author of this paper.

## References

August, T., and Niculescu, M. F. 2013. “The Influence of Software Process Maturity and Customer Error Reporting on Software Release and Pricing,” Management Science (59:12), pp. 2702-2726.

Bass, F. M. 1969. “A New Product Growth Model for Consumer Durables,” Management Science (15:1), pp. 215-227.

Cohen, M. A., Eliashberg, J., and Ho, T. 1996. “New Product Development: The Performance and Time-to-Market Tradeoff.” Management Science (42:2), pp. 173-186.

Danaher, P. J., Hardie, B. G. S., and Putsis, W. P. 2001. “Marketing-Mix Variables and the Diffusion of Successive Generations of a Technological Innovation,” Journal of Marketing Research (38:4), pp. 501-514.

Dhebar, A. 1994. “Durable-Goods Monopolists, Rational Consumers, and Improving Products,” Marketing Science (13:1), pp. 100-120.

Guo, Z., and Chen, J. 2018. “Multigeneration Product Diffusion in the Presence of Strategic Consumers,” Information Systems Research (29:1), pp. 206-224.

Hann, I., Koh, B., and Niculescu, M. F. 2016. “The Double-Edged Sword of Backward Compatibility: The Adoption of Multi-Generational Platforms in the Presence of Intergenerational Services,” Information Systems Research (27:1), pp, 112-139,

Hashem, I. A. T., Yaqoob, I., Anuar, N. B., Mokhtar, S., Gani, A., and Khan, S. U. 2015. “The Rise of ‘Big Data’ on Cloud Computing: Review and Open Research Issues,” Journal of Information Systems (47:C), pp. 98-115.

Hughes, N. 2010. “Apple’s Recurring Revenue Stream: 77% of iPhone 4 Sales Were Upgrades,” Apple Insider, June 25 (avail-

able at https://appleinsider.com/articles/10/06/25/apples\_ recurring\_revenue\_stream\_77\_of\_iphone\_4\_sales\_were\_ upgrades).

Jiang, Z., and Jain, D. C. 2012. “A Generalized Norton-Bass Model for Multigeneration Diffusion,” Management Science (58:10), pp. 1887-1897.

Kalish, S. 1983. “Monopolist Pricing with Dynamic Demand and Production Cost,” Marketing Science (2:2), pp. 135-159.

Kalish, S., and Lilien, G. 1986. “A Market Entry Timing Model for New Technologies,” Management Science (32:2), pp. 194-205.

Klemme, R. M., and Schoney, R. A. 1984. “Economic Analysis of Land Bid Prices Using Profitability and Cash Flow Considerations in Finite Planning Horizons,” North Central Journal of Agricultural Economics (6:2), pp. 117-127.

Krankel, R. M., Duenyas, I., and Kapuscinski, R. 2006. “Timing Successive Product Introductions with Demand Diffusion and Stochastic Technology Improvement,” Manufacturing & Service Operations Management (8:2), pp. 119-135.

Mahajan V., and Muller, E. 1996. “Timing, Diffusion, and Substitution of Successive Generations of Technological Innovations: The IBM Mainframe Case,” Technological Forecasting and Social Change (51:2), pp. 109-132.

Mehra, A., Seidmann, A., and Mojumder, P. 2014. “Product Life Cycle Management of Packaged Software,” Production and Operations Management (23:3), pp. 366-378.

Moorthy, K. S., and Png, I. P. L. 1992. “Market Segmentation, Cannibalization, and the Timing of Product Introductions,” Management Science (38:3), pp. 345-359.

Morgan, L. O., Morgan, R. M., and Moore, W. L. 2001. “Quality and Time-to-Market Trade-offs When There Are Multiple Product Generations,” Manufacturing & Service Operations Management (3:2), pp. 89-104.

Nascimento, F., and Vanhonacker, W. R. 1988. “Optimal Strategic Pricing of Reproducible Consumer Goods,” Management Science (34:8), pp. 921-937.

National Academy of Engineering. 1992. Time Horizons and Technology Investments, Washington, DC: National Academies Press.

Olanoff, D. 2012. “It Might Take the New iPad 8 Months to Surpass the iPad 2 as the Leading Tablet,” The Next Web, March 9 (http://thenextweb.com/apple/2012/03/09/it-might-take-thenew-ipad-8-months-to-surpass-the-ipad-2-as-the-leading-tablet/; accessed June 5, 2012).

Padmanabhan, V., Rajiv, S., and Srinivasan, K. 1997. “New Products, Upgrades, and New Releases: A Rationale for Sequential Product Introduction,” Journal of Marketing Research (34:4), pp. 456-472.

Prasad, A., Bronnenberg, B., and Mahajan, V. 2004. “Product Entry Timing in Dual Distribution Channels: The Case of the Movie Industry,” Review of Marketing Science (2:1), Article 4.

Sankaranarayanan, R. 2007. “Innovation and the Durable Goods Monopolist: The Optimality of Frequent New-Version Releases,” Marketing Science(26:6), pp. 774-791.

Stremersch, S., Muller, E., and Peres, R. 2010. “Does New Product Growth Accelerate across Technology Generations?,” Marketing Letters (21:2), pp. 103-120.

Sultan, F., Farley, J. U., and Lehmann, D. R. 1990. “A Meta-Analysis of Applications of Diffusion Models,” Journal of Marketing Research (27:1), pp. 70-77.

Wang, Q. H., and Hui, K. L. 2005. “To Launch or Not to Launch: An Economic Analysis of Delayed Product Introduction, in Proceedings of the 38<sup>th</sup> Annual Hawaii International Conference on System Sciences, Volume 8, p. 213.1.

Wang, Q. H., and Hui, K. L. 2010. “Delayed Product Introduction,” in Proceedings of the 2010 Pacific Asia Conference on Information Systems, Paper 29.

Wilson L. O., and Norton, J. A. 1989. “Optimal Entry Timing for a Product Line Extension,” Marketing Science (8:1), pp. 1-17.

## About the Authors

Zhengrui Jiang is a professor at the School of Business, Nanjing University. He previously was the Thome Professor in Business and professor of information systems at the Ivy College of Business, Iowa State University. He received his Ph.D. in Management Science from the University of Texas at Dallas. His primary research interests include business intelligence/analytics, data quality, decision-making under uncertainty, diffusion of technological innovations, and economics of information technology. He research appears in leading academic journals including Information Systems Research, Management Science, MIS Quarterly, IEEE Transactions on Knowledge and Data Engineering, INFORMS Journal on Computing, and Journal of Management Information Systems. He serves, or has served, as an associate editor for Information Systems Research and MIS Quarterly, as a senior editor for Production and Operations Management, and as a program co-chair for the 2014 Midwest Association of Information Systems Conference, the 2015 Big XII+ MIS Research Symposium, and the 2018 Workshop on Information Technologies and Systems, He received the MIS Quarterly Outstanding Associate Editor award in 2016.

Xinxue (Shawn) Qu is an assistant professor at the Mendoza College of Business, University of Notre Dame. He received his Ph.D. in Business and Technology from Iowa State University. His primary research interests include business intelligence/analytics, database management, multi-generation technology diffusion, and reinforcement learning. He has published his work in MIS Quarterly and Decision Sciences and presented his research at multiple conferences including INFORMS Conference on Information Systems and Technology (CIST) and the Workshop on Information Technology and Systems (WITS). He won the Excellence in Doctoral Student Research award at the Ivy College of Business, Iowa State University. He is a member of the Association of Information Systems and INFORMS.

Dipak C. Jain is President, professor of Marketing, and global advisor at China Europe International Business School (CEIBS). His influential career spans nearly four decades as an educator, a senior business school administrator, and a consultant to corporations and governments. He was Dean of Northwestern University’s Kellogg School of Management from 2001–2009, Dean of INSEAD from 2011–2013, and Director of Sasin from 2014– 2017. Prior to his deanship at Kellogg, he served as the departmental editor of Management Science (marketing) and an area editor of Marketing Science. His areas of research expertise include marketing of hightech products, market segmentation and competitive market structure analysis, cross-cultural issues in global product diffusion, new product innovation, and forecasting models. He has published more than 60 articles in leading academic journals and has earned the prestigious John D. C. Little Best Paper Award. In addition, he received the Pravasi Bharatiya Divas from the Prime Minister of India, an award that recognizes exceptional leadership contributions of overseas Indians.

# Optimal Market Entry Timing for Successive Generations of Technological Innovations

Zhengrui Jiang School of Business, Nanjing University, Nanjing 210093 CHINA {zjiang@nju.edu.cn}

Xinxue (Shawn) Qu Mendoza College of Business, University of Notre Dame, Notre Dame, IN 46556 50011 U.S.A. {xqu2@nd.edu}

Dipak C. Jain CEIBS, Shanghai, CHINA 201203 {dipakcjain@ceibs.edu}

## Appendix

## Interpretation of the GNB Model Equations

Based on the Generalized Norton-Bass Model (Jiang and Jain 2012), the number of units-in-use for the two successive generations can be represented by the following equations:

$$
S _ {1} (t) = m _ {1} F _ {1} (t) - m _ {1} F _ {1} (t) F _ {2} (t - \tau_ {2}) = m _ {1} F _ {1} (t) [ 1 - F _ {2} (t - \tau_ {2}) ]\tag{A1}
$$

$$
S _ {2} (t) = m _ {2} F _ {2} (t - \tau_ {2}) + m _ {1} F _ {1} (t) F _ {2} (t - \tau_ {2}) = [ m _ {2} + m _ {1} F _ {1} (t) ] F _ {2} (t - \tau_ {2})\tag{A2}
$$

The term $m _ { 1 } F _ { 1 } ( t )$ in Equation (1) represents the cumulative number of adoptions of G1, assuming that G2 were never introduced. Because G2 is introduced at time $\tau _ { 2 } , \mathbf { a }$ portion, $m _ { 1 } F _ { 1 } ( t ) F _ { 2 } ( t - \tau _ { 2 } )$ to be exact, of the G1 adopters will substitute G1 with G2, hence the term is subtracted from $S _ { 1 } ( t )$ and added to $S _ { 2 } ( t )$ (. The substitution term counts both leapfroggers (those who skip G1) and switchers (those who upgrade from G1 to G2). The leapfrogging multiplier, i.e., the proportion of potential adoteprs of G1 who choose to leapfrog at time t is assumed to be $F _ { 2 } ( t - \tau _ { 2 } )$ in the GNB model. Taking into consideration the leapfroggers, the instantaneous adoption rate for G1 takes the form

$$
y _ {1} (t) = m _ {1} f _ {1} (t) [ 1 - F _ {2} (t - \tau_ {2}) ]\tag{A3}
$$

In addition to leapfrogging, existing adopters of G1 also switch to G2. The number of switchers take the form of ݉ ${ } _ { 1 } F _ { 1 } ( t ) f _ { 2 } ( t - \tau _ { 2 } )$ . Adding the leapfrogging and switching terms to the adoptions by the G2-specific adopters, we obtain the adoption rate for G2

$$
y _ {2} (t) = [ m _ {2} + m _ {1} F _ {1} (t) ] f _ {2} (t - \tau_ {2}) + m _ {1} f _ {1} (t) F _ {2} (t - \tau_ {2})\tag{A4}
$$

From Equations (3) and (4), we can obtain the cumulative numbers of adoptions for the two generations

$$
Y _ {1} (t) = m _ {1} F _ {1} (t) - m _ {1} \int_ {\tau_ {2}} ^ {t} f _ {1} (\theta) F _ {2} (\theta - \tau_ {2}) d \theta\tag{A5}
$$

$$
Y _ {2} (t) = [ m _ {2} + m _ {1} F _ {1} (t) ] F _ {2} (t - \tau_ {2})\tag{A6}
$$

## Proof of Proposition 1

The derivative of the objective function of (19) with respect to $\tau _ { 2 }$ equals

$$
\frac {d \pi (\tau_ {2})}{d \tau_ {2}} = \frac {d}{d \tau_ {2}} \left\{\pi_ {1} \left[ m _ {1} F (D) - m _ {1} \int_ {\tau_ {2}} ^ {D} f (\theta) F (\theta - \tau_ {2}) d \theta \right] + \pi_ {2} [ m _ {2} + m _ {1} F (D) ] F (D - \tau_ {2}) \right\}
$$

Jiang et al./Optimal Market Entry Timing

$$
\begin{array}{c} = \frac {d}{d \tau_ {2}} \{\pi_ {1} m _ {1} F (D) \} - \frac {d}{d \tau_ {2}} \Bigg \{\pi_ {1} m _ {1} \int_ {\tau_ {2}} ^ {D} f (\theta) F (\theta - \tau_ {2}) d \theta \Bigg \} + \frac {d}{d \tau_ {2}} \{\pi_ {2} [ m _ {2} + m _ {1} F (D) ] F (D - \tau_ {2}) \} \\ = 0 - \pi_ {1} m _ {1} \frac {d}{d \tau_ {2}} \Bigg \{\int_ {\tau_ {2}} ^ {D} f (\theta) F (\theta - \tau_ {2}) d \theta \Bigg \} - \pi_ {2} [ m _ {2} + m _ {1} F (D) ] f (D - \tau_ {2}) \end{array}
$$

Note that that the last term is obtained based on Equation (7) or equivalently $\begin{array} { r } { \frac { d F ( t ) } { d t } = f ( t ) } \end{array}$

The derivative of integral term can be derived based on the Leibniz’s rule:

$$
\begin{array}{r} \frac {d}{d \tau_ {2}} \Bigg \{\int_ {\tau_ {2}} ^ {D} f (\theta) F (\theta - \tau_ {2}) d \theta \Bigg \} = - f (\tau_ {2}) F (\tau_ {2} - \tau_ {2}) + \int_ {\tau_ {2}} ^ {D} \frac {d}{d \tau_ {2}} [ f (\theta) F (\theta - \tau_ {2}) ] d \theta \\ = - 0 - \int_ {\tau_ {2}} ^ {D} f (\theta) f (\theta - \tau_ {2}) d \theta \end{array}
$$

The first term equals 0 because $F ( \tau _ { 2 } - \tau _ { 2 } ) = F ( 0 ) = 0$

Therefore,

$$
\frac {d \pi (\tau_ {2})}{d \tau_ {2}} = \pi_ {1} m _ {1} \int_ {\tau_ {2}} ^ {D} f (\theta) f (\theta - \tau_ {2}) d \theta - \pi_ {2} [ m _ {2} + m _ {1} F (D) ] f (D - \tau_ {2})\tag{A7}
$$

From (A7), we have

$$
\begin{array}{l} \frac {d \pi (\tau_ {2})}{d \tau_ {2}} <   \pi_ {1} m _ {1} \left[ \max _ {0 \leq \theta \leq D} f (\theta) \right] ^ {2} (D - \tau_ {2}) - \pi_ {2} [ m _ {2} + m _ {1} F (D) ] f (D - \tau_ {2}) \\ \quad <   \pi_ {1} m _ {1} \left[ \max _ {0 \leq \theta \leq D} f (\theta) \right] ^ {2} (D - \tau_ {2}) - \pi_ {2} [ m _ {2} + m _ {1} F (D) ] \min _ {0 \leq \theta \leq D} f (\theta) \\ = \pi_ {1} m _ {1} \left[ \max _ {0 \leq \theta \leq D} f (\theta) \right] ^ {2} \Bigg [ (D - \tau_ {2}) - \frac {\pi_ {2} [ m _ {2} + m _ {1} F (D) ] \min _ {0 \leq \theta \leq D} f (\theta)}{\pi_ {1} m _ {1} \left[ \max _ {0 \leq \theta \leq D} f (\theta) \right] ^ {2}} \Bigg ] \end{array}
$$

Let

$$
\varphi = \frac {\pi_ {2} [ m _ {2} + m _ {1} F (D) ] \min _ {0 \leq \theta \leq D} f (\theta)}{\pi_ {1} m _ {1} \left[ \max _ {0 \leq \theta \leq D} f (\theta) \right] ^ {2}}
$$

then we have

$$
\frac {d \pi (\tau_ {2})}{d \tau_ {2}} <   \pi_ {1} m _ {1} \left[ \max _ {0 \leq \theta \leq D} f (\theta) \right] ^ {2} [ (D - \varphi) - \tau_ {2} ]
$$

Therefore,

$$
\frac {d \pi (\tau_ {2})}{d \tau_ {2}} <   0, \text {   if   } (D - \varphi) \leq \tau_ {2} \leq D
$$

Given that $\pi ( \tau _ { 2 } )$ is monotonically decreasing with $\tau _ { 2 } \in [ D - \varphi , D ]$ [, we conclude that

$$
\tau_ {2} ^ {*} <   (D - \varphi), \quad \text { if } (D - \varphi) > \alpha_ {2} \text { or   equivalently, } \varphi <   D - \alpha_ {2}
$$

and $\tau _ { 2 } ^ { * } = \alpha _ { 2 } , \qquad \mathrm { i f } \left( D - \varphi \right) \leq \alpha _ { 2 }$ or equivalently, $\varphi \geq D - \alpha _ { 2 }$

In either case, $\tau _ { 2 } ^ { * } < D$ holds. Therefore, not introducing the second generation during the planning horizon cannot be optimal.

## Proof of Proposition 2

To prove that G2 should be introduced as early as possible, we only need to show

$$
\frac {d \pi (\tau_ {2})}{d \tau_ {2}} <   0, \forall \tau_ {2} \in [ 0, D ]
$$

where $\frac { d \pi ( \tau _ { 2 } ) } { d \tau _ { 2 } }$ has the same expression shown in (A7). First, with $\theta \in [ \tau _ { 2 } , D ]$ [, we have

$$
0 \leq (\theta - \tau_ {2}) \leq (D - \tau_ {2}) \leq D \leq T ^ {*} = \ln (q / p) / (p + q)
$$

Since $f ( t )$ ( is a monotonically increasing function of t before its peak is reached, i.e., when $t \leq T ^ { * }$ , we have

$$
\begin{array}{c} f (\theta - \tau_ {2}) \leq f (D - \tau_ {2}) \Rightarrow \\ \int_ {\tau_ {2}} ^ {D} f (\theta) f (\theta - \tau_ {2}) d \theta <   \int_ {\tau_ {2}} ^ {D} f (\theta) f (D - \tau_ {2}) d \theta = [ F (D) - F (\tau_ {2}) ] f (D - \tau_ {2}) \leq F (D) f (D - \tau_ {2}) \end{array}
$$

From $\pi _ { 1 } \leq \pi _ { 2 } .$ , we further conclude

$$
\pi_ {1} m _ {1} \int_ {\tau_ {2}} ^ {D} f (\theta) f (\theta - \tau_ {2}) d \theta <   \pi_ {2} m _ {1} F (D) f (D - \tau_ {2})
$$

which leads to

$$
\frac {d \pi (\tau_ {2})}{d \tau_ {2}} = \pi_ {1} m _ {1} \int_ {\tau_ {2}} ^ {D} f (\theta) f (\theta - \tau_ {2}) d \theta - \pi_ {2} [ m _ {2} + m _ {1} F (D) ] f (D - \tau_ {2}) <   0, \quad \forall \tau_ {2} \in [ 0, D ]
$$

## Derivation of Optimal Market Entry Timing for PTO Products under Total Transition

First, the objective function of (21) can be reorganized as

$$
\pi (\tau_ {2}) = \pi_ {2} m _ {1} F (D) + (\pi_ {1} - \pi_ {2}) m _ {1} F (\tau_ {2}) + \pi_ {2} [ m _ {2} + m _ {1} F (\tau_ {2}) ] F (D - \tau_ {2})
$$

Taking the derivative of the above function with respect to $\tau _ { 2 }$ yields

$$
\frac {\partial \pi (\tau_ {2})}{\partial \tau_ {2}} = (\pi_ {1} - \pi_ {2}) m _ {1} f (\tau_ {2}) - \pi_ {2} m _ {2} f (D - \tau_ {2}) + \pi_ {2} m _ {1} f (\tau_ {2}) F (D - \tau_ {2}) - \pi_ {2} m _ {1} F (\tau_ {2}) f (D - \tau_ {2})\tag{A8}
$$

After substituting $F ( \cdot )$ ( and $f ( \cdot )$ , letting $x = e ^ { ( p + q ) \tau _ { 2 } }$ and $\delta = e ^ { - ( p + q ) D }$ , and some additional algebraic rearrangement (details available from the authors), the above derivative can be expressed as

$$
\begin{array}{r l} & {\frac {d \pi (\tau_ {2})}{d \tau_ {2}} = H (x) (a x ^ {2} + b x + c)} \\ & {\mathrm{where} \quad H (x) = - \frac {(p + q) ^ {2} x}{p [ (q / p) + x ] ^ {2} [ (q / p) \delta x + 1 ] ^ {2}}} \\ & {\quad a = (\pi_ {2} - \pi_ {1}) m _ {1} \delta^ {2} \left(\frac {q}{p}\right) ^ {2} + \pi_ {2} m _ {2} \delta + \pi_ {2} m _ {1} \delta^ {2} \frac {q}{p} + \pi_ {2} m _ {1} \delta} \\ & {\quad b = 2 (\pi_ {2} - \pi_ {1}) m _ {1} \delta \frac {q}{p} + 2 \pi_ {2} m _ {2} \delta \frac {q}{p}} \end{array}\tag{A9}
$$

and

$$
c = \pi_ {2} m _ {2} \delta \left(\frac {q}{p}\right) ^ {2} - \pi_ {1} m _ {1} - \pi_ {2} m _ {1} \delta \frac {q}{p}
$$

We next take a closer look at the terms in (A9). Since $x = e ^ { ( p + q ) \tau _ { 2 } } \geq 1$ , we must have

$$
H (x) <   0
$$

We present below the solution for the most likely scenario, i.e., $a > 0$ and $b > 0 . { } ^ { 1 }$

We first examine the first-order condition $\begin{array} { r } { \frac { d \pi ( \tau _ { 2 } ) } { d \tau _ { 2 } } = 0 } \end{array}$ . Since $H ( x )$ ( in (A9) is always negative, we conclude that the first-order condition requires

$$
a x ^ {2} + b x + c = 0\tag{A10}
$$

Note that here $x = e ^ { ( p + q ) \tau _ { 2 } } \geq 1$ for $\forall \tau _ { 2 } \geq 0$

We examine three conditions, based on how the value of c compares with the other parameters.

(1) $\pmb { c } > b ^ { 2 } / ( 4 a )$ (. This condition implies $b ^ { 2 } - 4 a c < 0$ . Under this scenario, (A10) has no real solution. From $a > 0 ,$ we have

$$
a x ^ {2} + b x + c = 0 > 0, \forall x
$$

Since $H ( x ) < 0$ , we conclude

$$
\frac {d \pi (\tau_ {2})}{d \tau_ {2}} <   0, \forall \tau_ {2} \geq 0
$$

Because the net profit decreases monotonically as the introduction of G2 is delayed, it is optimal to introduce generation 2 as early as possible, that is,

$$
\tau_ {2} ^ {*} = \alpha_ {2}
$$

(2) $\mathbf { 0 } \leq c \leq b ^ { 2 } / ( 4 a )$ (. Under this scenario, $b ^ { 2 } - 4 a c \geq 0 .$ , hence (A10) has a real-number solution:

$$
x = \frac {- b \pm \sqrt {b ^ {2} - 4 a c}}{2 a}
$$

Since $c \geq 0 ,$ , we must have $( b ^ { 2 } - 4 a c ) \leq b ^ { 2 }$ . Under this condition, the root(s) of (A10) are non-positive. Hence,

$$
a x ^ {2} + b x + c = 0 > 0, \forall x \geq 1
$$

$$
\Rightarrow \frac {d \pi (\tau_ {2})}{d \tau_ {2}} <   0, \forall \tau_ {2} \geq 0
$$

Therefore,

$$
\tau_ {2} ^ {*} = \alpha_ {2}
$$

Based on scenarios (1) and (2), we conclude

$$
c \geq 0 \Rightarrow \tau_ {2} ^ {*} = \alpha_ {2}
$$

(3) $c < 0$ . This condition leads to $b ^ { 2 } - 4 a c \geq b ^ { 2 }$ . In this case, the two roots of (A10) are

$$
\left\{ \begin{array}{l l} x _ {1} = \frac {- b - \sqrt {b ^ {2} - 4 a c}}{2 a} <   0 \\ x _ {2} = \frac {- b + \sqrt {b ^ {2} - 4 a c}}{2 a} > 0 \end{array} \right.
$$

In this case, if $x _ { 2 } \leq e ^ { ( p + q ) \alpha _ { 2 } } .$ , or equivalently,

$$
c \geq - a e ^ {2 (p + q) \alpha_ {2}} - b e ^ {(p + q) \alpha_ {2}}
$$

we still have

$$
\frac {d \pi (\tau_ {2})}{d \tau_ {2}} \leq 0, \forall x \geq e ^ {(p + q) \alpha_ {2}}, \mathrm{or} \forall \tau_ {2} \geq \alpha_ {2}
$$

Therefore,

$$
\tau_ {2} ^ {*} = \alpha_ {2}
$$

On the other hand, if $x _ { 2 } > e ^ { ( p + q ) \alpha _ { 2 } }$ , or equivalently,

$$
c <   - a e ^ {2 (p + q) \alpha_ {2}} - b e ^ {(p + q) \alpha_ {2}}
$$

we have

$$
\frac {d \pi (\tau_ {2})}{d \tau_ {2}} \geq 0, \forall x \leq x _ {2}
$$

And

$$
\frac {d \pi (\tau_ {2})}{d \tau_ {2}} <   0, \forall x > x _ {2}
$$

Hence,

or

$$
\tau_ {2} ^ {*} = \frac {\mathrm{Ln} (x _ {2})}{p + q}
$$

$$
\tau_ {2} ^ {*} = \mathrm{Ln} (\frac {- b + \sqrt {b ^ {2} - 4 a c}}{2 a}) / (p + q)
$$

Optimal Solution: Taking into consideration all three scenarios, the optimal solution for Scenario II is

$$
\tau_ {2} ^ {*} = \left\{ \begin{array}{l l} \operatorname{Ln} \left(\frac {- b + \sqrt {b ^ {2} - 4 a c}}{2 a}\right) / (p + q), & \text { if } c <   - a e ^ {2 (p + q) \alpha_ {2}} - b e ^ {(p + q) \alpha_ {2}} \\ \alpha_ {2}, & \text { otherwise } \end{array} \right.
$$

## Proof of Proposition 3

(1). We first prove that with $\pi _ { 1 } \leq \pi _ { 2 }$ , we have $\tau _ { 2 } ^ { * } < D$

Again, taking the derivative of the objective function of (21) with respect to $\tau _ { 2 }$ yields the results shown in (A8):

$$
\frac {\partial \pi (\tau_ {2})}{\partial \tau_ {2}} = (\pi_ {1} - \pi_ {2}) m _ {1} f (\tau_ {2}) - \pi_ {2} m _ {2} f (D - \tau_ {2}) + \pi_ {2} m _ {1} f (\tau_ {2}) F (D - \tau_ {2}) - \pi_ {2} m _ {1} F (\tau_ {2}) f (D - \tau_ {2})
$$

It is easy to show that the sum of first two terms is less than zero, that is,

$$
(\pi_ {1} - \pi_ {2}) m _ {1} f (\tau_ {2}) - \pi_ {2} m _ {2} f (D - \tau_ {2}) <   0\tag{A11}
$$

Now let us take a look at the third and fourth terms.

$$
\begin{array}{r} \pi_ {2} m _ {1} f (\tau_ {2}) F (D - \tau_ {2}) - \pi_ {2} m _ {1} F (\tau_ {2}) f (D - \tau_ {2}) \\ = \pi_ {2} m _ {1} [ f (\tau_ {2}) F (D - \tau_ {2}) - F (\tau_ {2}) f (D - \tau_ {2}) ] \end{array}\tag{A12}
$$

In (A12), as $\tau _ { 2 } \to \infty , F ( D - \tau _ { 2 } ) \to 0$ , while all other terms remain well above zero. As a result, (A12) necessarily becomes negative. This result, together with (A11), lead to the conclusion that

$$
\frac {\partial \pi (\tau_ {2})}{\partial \tau_ {2}} <   0, \mathrm{as} \tau_ {2} \rightarrow \infty
$$

Therefore, we must have $\tau _ { 2 } ^ { * } < D$

(2). We now prove that with $\pi _ { 1 } > \pi _ { 2 } .$ , it is possible to have $\tau _ { 2 } ^ { * } > D$ , implying that not introducing the second generation during the planning horizon could be an optimal solution.

Again, by looking at the expression in (A8), it can be shown that regardless of the value of the other parameters, if $\pi _ { 1 }$ is sufficiently large, we can have $\frac { \partial \pi ( \tau _ { 2 } ) } { \partial \tau _ { 2 } } > 0 , \forall \tau _ { 2 } \in [ 0 , D ]$ [. Then, not introducing the second generation is indeed an optimal solution.

## Proof of Proposition 4

We separately examine Scenarios III and IV.

(1) Under Scenario III (STU products and phase-out transition), the objective function of (24) can be rearranged to

$$
\pi (\tau_ {2}) = \varphi_ {1} m _ {1} \int_ {0} ^ {D} F (\theta) d \theta + (\varphi_ {2} - \varphi_ {1}) m _ {1} \int_ {\tau_ {2}} ^ {D} F (\theta) F (\theta - \tau_ {2}) d \theta + \varphi_ {2} m _ {2} \int_ {\tau_ {2}} ^ {D} F (\theta - \tau_ {2}) d \theta .
$$

Therefore,

$$
\begin{array}{r} \frac {d \pi (\tau_ {2})}{d \tau_ {2}} = (\varphi_ {2} - \varphi_ {1}) m _ {1} \left[ - F (\tau_ {2}) F (\tau_ {2} - \tau_ {2}) - \int_ {\tau_ {2}} ^ {D} F (\theta) f (\theta - \tau_ {2}) d \theta \right] + \varphi_ {2} m _ {2} \left[ - F (\tau_ {2} - \tau_ {2}) - \int_ {\tau_ {2}} ^ {D} f (\theta - \tau_ {2}) d \theta \right] \\ = - (\varphi_ {2} - \varphi_ {1}) m _ {1} \int_ {\tau_ {2}} ^ {D} F (\theta) f (\theta - \tau_ {2}) d \theta - \varphi_ {2} m _ {2} F (D - \tau_ {2}) \end{array}\tag{A13}
$$

If $\varphi _ { 1 } \leq \varphi _ { 2 } .$ , we have

$$
\left\{ \begin{array}{l l} \frac {d \pi (\tau_ {2})}{d \tau_ {2}} <   0, & i f \tau_ {2} <   D \\ \frac {d \pi (\tau_ {2})}{d \tau_ {2}} = 0, & i f \tau_ {2} = D \end{array} \right.
$$

Since $\pi ( \tau _ { 2 } )$ decreases monotonically as $\tau _ { 2 }$ increases, G2 should be introduced to the market as early as possible, that is, $\tau _ { 2 } ^ { * } = \alpha _ { 2 }$

(2) Under Scenario IV (STU products and total transition), the objective function of (25) can be rearranged to

$$
\begin{array}{r l} & {\pi (\tau_ {2}) = \varphi_ {1} m _ {1} \int_ {0} ^ {\tau_ {2}} F (\theta) d \theta + \varphi_ {1} \int_ {\tau_ {2}} ^ {D} m _ {1} F (\tau_ {2}) [ 1 - F (\theta - \tau_ {2}) ] d \theta + \varphi_ {2} \int_ {\tau_ {2}} ^ {D} \{[ m _ {2} + m _ {1} F (\tau_ {2}) ] F (\theta - \tau_ {2}) + m _ {1} [ F (\theta) - F (\tau_ {2}) ] \} d \theta} \\ & {\quad = \varphi_ {1} m _ {1} \int_ {0} ^ {D} F (\theta) d \theta - \varphi_ {1} m _ {1} \int_ {\tau_ {2}} ^ {D} F (\theta) d \theta + \int_ {\tau_ {2}} ^ {D} \{(\varphi_ {1} - \varphi_ {2}) m _ {1} F (\tau_ {2}) + \varphi_ {2} m _ {2} F (\theta - \tau_ {2})} \\ & {\qquad + (\varphi_ {2} - \varphi_ {1}) m _ {1} F (\tau_ {2}) F (\theta - \tau_ {2}) + \varphi_ {2} m _ {1} F (\theta) \} d \theta} \\ & {\quad = \varphi_ {1} m _ {1} \int_ {0} ^ {D} F (\theta) d \theta + \int_ {\tau_ {2}} ^ {D} \{(\varphi_ {1} - \varphi_ {2}) m _ {1} F (\tau_ {2}) + \varphi_ {2} m _ {2} F (\theta - \tau_ {2})} \\ & {\qquad + (\varphi_ {2} - \varphi_ {1})m _ {1}F (\tau_ {2})F (\theta - \tau_ {2}) + (\varphi_ {2} - \varphi_ {1})m _ {1}F (\theta) \}d \theta} \end{array}
$$

Then,

$$
\begin{array}{r l} & {\frac {d \pi (\tau_ {2})}{d \tau_ {2}} = - \{(\varphi_ {1} - \varphi_ {2}) m _ {1} F (\tau_ {2}) + \varphi_ {2} m _ {2} F (\tau_ {2} - \tau_ {2}) + (\varphi_ {2} - \varphi_ {1}) m _ {1} F (\tau_ {2}) F (\tau_ {2} - \tau_ {2}) + (\varphi_ {2} - \varphi_ {1}) m _ {1} F (\tau_ {2}) \}} \\ & {\qquad + \int_ {\tau_ {2}} ^ {D} \{(\varphi_ {1} - \varphi_ {2}) m _ {1} f (\tau_ {2}) - \varphi_ {2} m _ {2} f (\theta - \tau_ {2})} \\ & {\qquad - (\varphi_ {2} - \varphi_ {1}) m _ {1} F (\tau_ {2}) f (\theta - \tau_ {2}) + (\varphi_ {2} - \varphi_ {1}) m _ {1} f (\tau_ {2}) F (\theta - \tau_ {2}) \} d \theta} \\ & {\qquad = (\varphi_ {1} - \varphi_ {2}) m _ {1} f (\tau_ {2}) (D - \tau_ {2}) - \varphi_ {2} m _ {2} F (D - \tau_ {2}) - (\varphi_ {2} - \varphi_ {1}) m _ {1} F (\tau_ {2}) F (D - \tau_ {2}) +} \end{array}
$$

$$
(\varphi_ {2} - \varphi_ {1}) m _ {1} f (\tau_ {2}) \int_ {\tau_ {2}} ^ {D} F (\theta - \tau_ {2}) d \theta\tag{A14}
$$

If $\varphi _ { 1 } \leq \varphi _ { 2 }$ , we have

$$
\begin{array}{r l} & {\frac {d \pi (\tau_ {2})}{d \tau_ {2}} <   (\varphi_ {1} - \varphi_ {2}) m _ {1} f (\tau_ {2}) (D - \tau_ {2}) - \varphi_ {2} m _ {2} F (D - \tau_ {2}) - (\varphi_ {2} - \varphi_ {1}) m _ {1} F (\tau_ {2}) F (D - \tau_ {2}) + (\varphi_ {2} - \varphi_ {1}) m _ {1} f (\tau_ {2}) \int_ {\tau_ {2}} ^ {D} d \theta} \\ & {\qquad = (\varphi_ {1} - \varphi_ {2}) m _ {1} f (\tau_ {2}) (D - \tau_ {2}) - \varphi_ {2} m _ {2} F (D - \tau_ {2}) - (\varphi_ {2} - \varphi_ {1}) m _ {1} F (\tau_ {2}) F (D - \tau_ {2}) + (\boldsymbol {\varphi} _ {2} - \boldsymbol {\varphi} _ {1}) m _ {1} f (\tau_ {2}) (D - \tau_ {2})} \\ & {\qquad = - \varphi_ {2} m _ {2} F (D - \tau_ {2}) - (\varphi_ {2} - \varphi_ {1}) m _ {1} F (\tau_ {2}) F (D - \tau_ {2})} \end{array}
$$

Hence,

$$
\left\{ \begin{array}{l l} \frac {d \pi (\tau_ {2})}{d \tau_ {2}} <   0, & i f \tau_ {2} <   D \\ \frac {d \pi (\tau_ {2})}{d \tau_ {2}} = 0, & i f \tau_ {2} = D \end{array} \right.
$$

Therefore, it is optimal to release G2 as early as possible, that is, $\tau _ { 2 } ^ { * } = \alpha _ { 2 }$

## Proof of Proposition 5

We separately examine Scenarios III and IV.

(1) Under Scenario III (STU products and phase-out transition), $\operatorname { i f } \varphi _ { 1 } > \varphi _ { 2 } .$ , from (A13) we have

$$
\begin{array}{r l} & {\frac {d \pi (\tau_ {2})}{d \tau_ {2}} = (\varphi_ {1} - \varphi_ {2}) m _ {1} \int_ {\tau_ {2}} ^ {D} F (\theta) f (\theta - \tau_ {2}) d \theta - \varphi_ {2} m _ {2} F (D - \tau_ {2})} \\ & {\qquad <   (\varphi_ {1} - \varphi_ {2}) m _ {1} \int_ {\tau_ {2}} ^ {D} F (D) f (\theta - \tau_ {2}) d \theta - \varphi_ {2} m _ {2} F (D - \tau_ {2})} \\ & {\qquad = [ (\varphi_ {1} - \varphi_ {2}) m _ {1} F (D) - \varphi_ {2} m _ {2} ] F (D - \tau_ {2})} \end{array}
$$

Therefore,

$$
\frac {d \pi (\tau_ {2})}{d \tau_ {2}} <   0 \mathrm{if} (\varphi_ {1} - \varphi_ {2}) m _ {1} F (D) \leq \varphi_ {2} m _ {2}
$$

or equivalently,

$$
\frac {d \pi (\tau_ {2})}{d \tau_ {2}} <   0 \text {if} m _ {2} \geq \frac {(\varphi_ {1} - \varphi_ {2}) F (D)}{\varphi_ {2}} m _ {1}
$$

Thus

$$
\tau_ {2} ^ {*} = \alpha_ {2} \mathrm{if} m _ {2} \geq \frac {(\varphi_ {1} - \varphi_ {2}) F (D)}{\varphi_ {2}} m _ {1}
$$

(2) Under Scenario IV (STU products and total transition), if $\varphi _ { 1 } > \varphi _ { 2 }$ , from (A14) we have

$$
\begin{array}{c} \frac {d \pi (\tau_ {2})}{d \tau_ {2}} = - \varphi_ {2} m _ {2} F (D - \tau_ {2}) - (\varphi_ {2} - \varphi_ {1}) m _ {1} F (\tau_ {2}) F (D - \tau_ {2}) + (\varphi_ {1} - \varphi_ {2}) m _ {1} f (\tau_ {2}) \int_ {\tau_ {2}} ^ {D} [ 1 - F (\theta - \tau_ {2}) ] d \theta \\ \frac {d \pi (\tau_ {2})}{d \tau_ {2}} \leq 0 \Leftrightarrow - \varphi_ {2} m _ {2} F (D - \tau_ {2}) + (\varphi_ {1} - \varphi_ {2}) m _ {1} F (\tau_ {2}) F (D - \tau_ {2}) + (\varphi_ {1} - \varphi_ {2}) m _ {1} f (\tau_ {2}) \int_ {\tau_ {2}} ^ {D} [ 1 - F (\theta - \tau_ {2}) ] d \theta \leq 0 \\ \Leftrightarrow \varphi_ {2} m _ {2} F (D - \tau_ {2}) \geq (\varphi_ {1} - \varphi_ {2}) m _ {1} F (\tau_ {2}) F (D - \tau_ {2}) + (\varphi_ {1} - \varphi_ {2}) m _ {1} f (\tau_ {2}) \int_ {\tau_ {2}} ^ {D} [ 1 - F (\theta - \tau_ {2}) ] d \theta \end{array}
$$

$$
\Leftrightarrow m _ {2} \geq \frac {(\varphi_ {1} - \varphi_ {2}) m _ {1}}{\varphi_ {2}} \left[ F (\tau_ {2}) + \frac {f (\tau_ {2})}{F (D - \tau_ {2})} \int_ {\tau_ {2}} ^ {D} [ 1 - F (\theta - \tau_ {2}) ] d \theta \right]
$$

The second term on the RHS of the equation is always positive, that is,

$$
F (\tau_ {2}) + \frac {f (\tau_ {2})}{F (D - \tau_ {2})} \int_ {\tau_ {2}} ^ {D} [ 1 - F (\theta - \tau_ {2}) ] d \theta > 0, \forall \tau_ {2} \in [ \alpha_ {2}, D ]
$$

We let

$$
\nu = \max _ {0 \leq \tau_ {2} \leq D} f \left[ F (\tau_ {2}) + \frac {f (\tau_ {2})}{F (D - \tau_ {2})} \int_ {\tau_ {2}} ^ {D} [ 1 - F (\theta - \tau_ {2}) ] d \theta \right]
$$

It can be shown that

$$
\frac {d \pi (\tau_ {2})}{d \tau_ {2}} \leq 0, \quad \text {if} m _ {2} \geq \frac {(\varphi_ {1} - \varphi_ {2}) m _ {1}}{\varphi_ {2}} \nu
$$

## Extension Model with Network Effects, Compatibility, and Switching Cost Considered

In the main text we have implicitly assumed that network effects, product compatibility, and switching cost are either exogenous or negligible. Here, we develop an extension model to examine how these additional economic factors can affect the new generation’s optimal market entry timing and the total profit. We consider only PTO products under phase-out transition in the following analysis.

Network effects refer to the phenomenon that the utility a consumer receives from using a product increases with the number of users of tha product (Katz and Shapiro 1985). In the presence of two product generations, it is possible that the valuation of one generation can benefit from its own network as well as the other generation’s network. In other words, there exist both within-generation network effects and crossgeneration network effects. Cross-generation network effects exist because of backward and forward compatibility. Specifically, backward (forward) compatibility allows the new (old) product generation to benefit from the old (new) product generation’s network (Choi 1994)

To differentiate the multiple sources of network effects, we denote the intensity of within-generation network effects (i.e., the incremental utility resulting from one more users joining the focal generation’s network) by $\alpha ,$ the intensity of forward compatibility by $\beta _ { f }$ , and the intensity of backward network effects by $\beta _ { b } .$ . Because forward compatibility is more difficult to achieve and backward compatibility is more critical to the success of a product line, firms typically consider backward compatibility to be of higher strategic importance (Choi 1994, Kretschmer and Claussen 2016). Hence we assume that the intensity of forward compatibility is no higher than that of backward compatibility. In addition, the intensity of cross-generation network effects cannot be larger than that of within-generation network effects. Given these two assumptions, we have $0 \leq \beta _ { f } \leq \beta _ { b } \leq \alpha$ . The network size of each generation at time t is simply the number of units-in-use at that time, that is, $S _ { 1 } ( t )$ or $( S _ { 2 } ( t )$

To capture the impact of these economic factors, it is necessary to consider the value of each product generation to potential adopters. First, the new product generation is expected to have a higher quality than that of the older generation. We denote the product quality of G1 (G2), measured by its value to adopters, by $\delta _ { 1 } ( \delta _ { 2 } ) . ^ { 2 }$ With the network effects induced benefits considered, the value of G1 at time t can be expressed as

$$
V _ {1} (t) = \delta_ {1} + \alpha S _ {1} (t) + \beta_ {f} S _ {2} (t)\tag{A15}
$$

Similarly, the value of G2 at time t take the form

$$
V _ {2} (t) = \delta_ {2} + \alpha S _ {2} (t) + \beta_ {b} S _ {1} (t)\tag{A16}
$$

Therefore, the difference in value between the two product generations is

$$
\Delta V (t) = V _ {1} (t) - V _ {2} (t) = (\delta_ {1} - \delta_ {2}) + \alpha [ S _ {1} (t) - S _ {2} (t) ] + \beta_ {f} S _ {2} (t) - \beta_ {b} S _ {1} (t)\tag{A17}
$$

For potential adopters of G1 who have not adopted G1 yet, they have the options of adopting either G1 or G2 after the latter is released. Using the widely adopted logit choice model (Guadagni and Little 1983, Morgan et al. 2001), the percentage of potential adopters who choose G2 instead of G1 at time t, which is essentially the leapfrogging multiplier, equals

$$
u _ {2} (t) = \frac {e ^ {V _ {2} (t)}}{e ^ {V _ {2} (t)} + e ^ {V _ {1} (t)}} = \frac {1}{1 + e ^ {\Delta V (t)}}, t \geq \tau_ {2}\tag{A18}
$$

With respect to those customers who have already adopted G1, the switching cost, denoted by ߱, comes into play. As a result, the percentag of them who are willing to switch to G2 at time t, i.e., the switching multiplier, takes the form

$$
w _ {2} (t) = \frac {e ^ {V _ {2} (t) - \omega}}{e ^ {V _ {2} (t) - \omega} + e ^ {V _ {1} (t)}} = \frac {1}{1 + e ^ {\Delta V (t) + \omega}}, t \geq \tau_ {2}\tag{A19}
$$

With the leapfrogging and switching multipliers defined, we can revise the GNB model to capture the effect of network effects, backward forward compatibility, and switching cost on the diffusion of the two product generations. Because of the complex dependencies among leapfrogging/switching, units-in-use, and adoptions, it is not possible to develop a continuous-time multigeneration diffusion model. Therefore, we revise a discrete version of the GNB model based on the leapfrogging and switching multipliers shown in Equations (A18) and (A19).

Under a discrete time model, we consider discrete time instances $t \in \{ 0 , 1 , 2 , \dots , \tau _ { 2 } , \dots , D \}$ , where $\tau _ { 2 }$ still denotes the release time of G2 and the length of planning horizon is still D. The noncumulative adoption rate $y _ { G } ( t )$ for generation G is now interpreted as the number of adoptions occurring during time interval $( t - 1 , ~ t ] . ~ S _ { G } ( t )$ and $Y _ { G } ( t )$ represent the number of units-in-use and the cumulative number of adoptions, respectively, for generation G at time t. Based on these definitions, prior to the release of G2 at time $\tau _ { 2 } ,$ the adoptions of G1 can be characterized by

$$
y _ {1} (t) = m _ {1} [ F _ {1} (t) - F _ {1} (t - 1) ], 1 \leq t \leq \tau_ {2}\tag{A20}
$$

$$
S _ {1} (t) = Y _ {1} (t) = m _ {1} F _ {1} (\tau_ {2}), 0 \leq t \leq \tau_ {2}\tag{A21}
$$

After the release of G2, due to leapfrogging and switching, the two functions change to

$$
y _ {1} (t) = m _ {1} [ F _ {1} (t) - F _ {1} (t - 1) ] [ 1 - u _ {2} (t) ], t \geq \tau_ {2} + 1\tag{A22}
$$

$$
S _ {1} (t) = S _ {1} (t - 1) [ 1 - w _ {2} (t) ] + m _ {1} [ F _ {1} (t) - F _ {1} (t - 1) ] \{1 - u _ {2} (t) \}, t \geq \tau_ {2} + 1\tag{A23}
$$

In addition, the following equation holds throughout the planning horizon:

$$
Y _ {1} (t) = Y _ {1} (t - 1) + y _ {1} (t), t \geq 1\tag{A24}
$$

For the new generation G2, we have

$$
\begin{array}{r l} & y _ {2} (t) = m _ {2} [ F _ {2} (t - \tau_ {2}) - F _ {2} (t - \tau_ {2} - 1) ] \\ & + S _ {1} (t - 1) w _ {2} (t) + m _ {1} [ F _ {1} (t) - F _ {1} (t - 1) ] u _ {2} (t), t \geq \tau_ {2} + 1 \end{array}\tag{A25}
$$

$$
S _ {2} (\tau_ {2}) = Y _ {2} (\tau_ {2}) = 0, t = \tau_ {2}\tag{A26}
$$

$$
S _ {2} (t) = Y _ {2} (t) = Y _ {2} (t - 1) + y _ {2} (t), t \geq \tau_ {2} + 1\tag{A27}
$$

Equations (A15) – (A27) jointly constitute the discrete-time diffusion model with network effects. We refer to it as the DNE model in the rest of the discussion.

Based on the DNE model, the optimal entry time for G2 can be formulated as

$$
\max _ {\alpha_ {2} \leq \tau_ {2} \leq D} \pi (\tau_ {2}) = \pi_ {1} \sum_ {t = 1} ^ {D} y _ {1} (t) + \pi_ {2} \sum_ {t = \tau_ {2}} ^ {D} y _ {2} (t)\tag{A28}
$$

Given the complexity of the model, analytical findings are unattainable. Hence, similar to prior studies (e.g., Mahajan and Muller 1996, Koca, Souza, and Druehl 2010, and Joshi, Reibstein, and Zhang 2009), we conduct numerical analysis to examine how the network effects, backward-forward compatibility, and switching cost affect the new generation’s optimal market entry timing and the total profit. We retain some parameter values used in the previous numerical analysis as default values, i.e., m<sub>1</sub> = m<sub>2</sub> = 10 million, $\pi _ { 1 } = \pi _ { 2 } = \mathbb { S } 1 0 0$ , and D=10 years (or 120 months). The other default values are set at $p = 0 . 0 2 , q = 0 . 2 , \delta _ { 1 } - \delta _ { 2 } \mathrm { = - } 1 0 ; \alpha \mathrm { = } 2 , \beta _ { f } = \beta _ { b } = 1$ , and ߱=20.

## Within-Generation Network Effects

We first examine how the intensity of within-generation network (ߙ ( affects the optimal market entry timing of G2 and the firm’s profitability. From Equation (A17), we can tell that when the two product generations are completely compatible, i.e., $\alpha = \beta _ { f } = \beta _ { b }$ , having a larger network size of its own does not help a particular product generation, because the other generation can benefit equally from its larger network size. In fact, the larger is the difference between ߙ and $\beta _ { f } ( \beta _ { b } )$ (, the more advantageous it is to have a large network size. For this reason, in our first analysis, we change the value of α while keeping the values of $\cdot \beta _ { f } , \beta _ { b }$ , and other parameters fixed at their default values. As shown in Figure A1(a), as the value of α increases, the firm’s total profit exhibits a monotonically increasing pattern, showing that the firm can benefit directly from stronger within-generation network effects.

![](/api/attachments/WQAAJJ37/fulltext/images/954e0cecb0e9c5965acf7b5c9411e372b204273cac812a4dacece29fbfba5b41.jpg)  
(a)

![](/api/attachments/WQAAJJ37/fulltext/images/e467b43d7cd39da219b501687d4ff85d0f7f53afb0f31f8392c31d76d33aa291.jpg)  
(b)  
Figure A1. Impact of Intensity of Within-Generation Network Effects (α)

What is more interesting is that the optimal entry timing shows a non-monotonic pattern, which first decreases (shorter time to market) and then increases (longer time-to-market) after a bottom is reached. In order to better understand this interesting pattern, we plot the numbers of adoptions of G1 and G2, as well as the total number of adoptions, in Figure A1(b). From this figure, we can see that $Y _ { 1 , }$ , denoting the total number of adopters of G1, drops when the value of α changes from 1 to 2; this is because, as shown in Figure A1(a), G2 enters the market earlier, hence taking away more potential adopters from G1. This reduction in the number of G1 adoptions, however, is more than compensated by the sharp increase in the number of G2 adoptions, which is evident in Figure A1(b). In sum, although the number G1 adoptions drops as G2 enter the market earlier, the total number of adoptions of G1 and G2 increases, leading to a higher profit

However, as α changes from 2 to 3, the optimal market entry timing of G2 and Y are no longer in sync, and the results are not expected — the number of G1 adoptions increases although G2 enters the market earlier. Upon further examination, we find that this is a result of withinnetwork effects. Specifically, with a higher intensity of within-network effect, the proportion of potential adopters who are willing to leapfrog from G1 to G2 becomes smaller; this is because upon release G2 has a much smaller network size than G1. In other words, the cannibalization of G1 adoptions by the earlier release of G2 will be limited if the within-generation network effects are sufficiently high.

As show in Figure A1(a), the optimal market entry timing reaches the bottom when α equals 4, 5, 6. We next explain why it is optimal to delay the release of G2 as α increases beyond 6. It is worth noting that with a constant market size, the key to improve the total profit is to increase the number of cross-generation repeat adoptions, i.e., the number of adopters who buy both G1 and G2. As explained earlier, a large within-generation network effects, resulting from a large network size of G1 in relation to that of G2, can decrease the canalization effect. Therefore, delaying the release of G2 can help increase the number of G1 adopters in two ways. First, it increases the number of G1 adoptions before the release. Second, a larger network size upon the release of G2 can further reduce the canalization effect. Since the vast majority of G1 adopters will eventually switch to G2, a large number of G1 adoptions implies more cross-generation repeat adoptions, and hence a higher total profit.

## Backward/Forward Compatibility

We also conduct numerical analysis to examine the impact of backward and forward compatibility on the optimal market entry timing and the total profit. To allow a large range of parameter values, we set the intensity of with-generation network effects to $\alpha = 1 0 .$ . Then, with the intensity of forward-compatibility $( \beta _ { f } )$ ( fixed at 0, we vary the intensity of backward-compatibility $( \beta _ { b } )$ from 0 to 10, and record the results in Figure A2. Subsequently, we fix $\beta _ { b }$ at 8, and vary the value of $\beta _ { f }$ from 0 to 8; the results are summarized in Figure A3. The breakdown of the adoptions of the two generations are not shown because they add limited additional insight. From Figure A2, we can tell that with a higher backward compatibility, a firm can delay the release of the second generation. The profit increases dramatically as $\beta _ { b }$ increases from 0 to 1, but remains relatively flat afterward. The impact of forward compatibility is almost the opposite. The new generation should be released earlier with a higher forward compatibility. The profit remains little changed as $\beta _ { f }$ changes from 0 to 7, but drops sharply when $\beta _ { f } { = } 7 { = } \beta _ { b }$ Considering that fact that profit is also at the lowest when in Figure A3 when $\scriptstyle { \dot { \beta } } _ { b } = 0 = \beta _ { f }$ , we conclude that it is less profitable when the intensities of forward and backward compatibility are equal

(a)  
(b)  
Figure A2. Impact of Intensity of Backward Compatibility Figure A3. Impact of Intensity of Forward Compatibility (<sub>࢈</sub>ࢼ) $( \beta _ { f } )$  
![](/api/attachments/WQAAJJ37/fulltext/images/0114cc9c243aa288a0b60c827a1914d5626bfd6e25464d6bc399850419b5d4f9.jpg)

![](/api/attachments/WQAAJJ37/fulltext/images/64da61d8d42b580d83fb69d63c6bbafaf6e525cf744e0dd135d95a0cd25798cc.jpg)

## Switching Cost

We also examine how the switching cost affects the new generation’s optimal market entry timing and the firm’s profitability. As shown in Figure A4(a), a larger switching cost leads to a lower profit and an earlier optimal market entry timing for G2. From Figure A4(b), we can see that the number of G2 adoptions remains little changed, while the number of G1 adoptions drops significantly. Our explanations for this trend is as follows. A higher switching cost reduces the attractiveness of the new generation to those who have already adopted G1. As a result, delaying the release of G2 to increase the number of cross-generation repeat purchases becomes less justifiable. Although releasing G2 earlier also leads to more cannibalization, such cannibalization is not a concern because the profit per adoption is the same for G1 and G2. With both factors considered, it makes sense for the firm to release G2 earlier.

![](/api/attachments/WQAAJJ37/fulltext/images/08b20119a35854b043640b929c9fc27bd4c40f21b608f80174ca8bf686a89a71.jpg)

![](/api/attachments/WQAAJJ37/fulltext/images/1abe500ebf7fcbf5c8fab0ae6e8232b98bdfbf28f73cbe251cc94b5ac777c54b.jpg)  
Figure A4. Impact of Switching Cost (࣓(

In sum, within-generation network effects, backward-forward compatibility, and switching cost all have influence on the new generation’s optimal market entry timing and the firm’s total profit. While the directions of their impact on the total profit are as generally expected, thei impact on market entry timing are not as straightforward.

## References

Choi, J. P. 1994. “Network Externality, Compatibility Choice, and Planned Cbsolescence,” The Journal of Industrial Economics (42:2), pp. 167-182.

Guadagni, P. M., and Little, J. D. 1983. “A Logit Model of Brand Choice Calibrated on Scanner Data,” Marketing Science (2:3), pp. 203- 238.

Jiang, Z., and Jain, D. C. 2012. “A Generalized Norton-Bass Model for Multigeneration Diffusion,” Management Science (58:10), pp. 1887- 1897.

Joshi, Y. V., Reibstein, D. J., and Zhang, Z. J. 2009. “Optimal Entry Timing in Markets with Social Influence,” Management Science (55:6), pp. 926-939.

Katz, M. L. and., Shapiro, C. 1985. “Network Externalities, Competition, and Compatibility,” The American Economic Review (75:3) pp. 424-440.

Koca, E., Souza, G. C., and Druehl, C. T. 2010. “Managing Product Rollovers,” Decision Sciences (41:2), pp. 403-423.

Kretschmer, T., and Claussen, J. 2016. “Generational Transitions in Platform Markets—The Role of Backward Compatibility,” Strategy Science (1:2), pp. 90-104.

Mahajan V., and Muller, E. 1996. “Timing, Diffusion, and Substitution of Successive Generations of Technological Innovations: The IBM Mainframe Case,” Technological Forecasting and Social Change (51:2), pp. 109-132.

Morgan, L. O., Morgan, R. M., and Moore, W. L. 2001. “Quality and Time-to-Market Trade-offs When There Are Multiple Product Generations,” Manufacturing & Service Operations Management (3:2), pp. 89-104.
