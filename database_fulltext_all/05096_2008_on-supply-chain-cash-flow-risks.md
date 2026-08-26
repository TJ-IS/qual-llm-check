---
otero_id: 5096
otero_key: "AJKWE9QK"
title: "On supply chain cash flow risks"
authors: "Chih-Yang Tsai"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.12.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 44 (2008) 1031– 1042

www.elsevier.com/locate/dss

# On supply chain cash flow risks <sup>☆</sup>

Chih-Yang Tsai<sup>⁎</sup>

School of Business, State University of New York at New Paltz, New Paltz, NY 12561, USA

Received 10 August 2006; received in revised form 25 November 2007; accepted 2 December 2007 Available online 15 December 2007

## Abstract

This study models the supply chain related cash flow risks for a business entity measured by the standard deviations of cash inflows, outflows, and netflows of each period in a planning horizon. The goal is to provide an insightful look on how common practices that intend to improve the Cash Conversion Cycle (CCC), e.g., offering early payment discounts, may contribute to cash flow risks. We show the benefits and recommend the best policy of using Asset-Backed Securities (ABS) to finance accounts receivable as a means to shorten the CCC and lower the cash inflow risk. It is particularly helpful to small vendors having tight cash reserves and high financing costs.

© 2007 Elsevier B.V. All rights reserved.

Keywords: Supply chain; Cash flow risks; Cash conversion cycle; Simulation

## 1. Introduction

Cash is a vital resource needed to support almost all activities in an organization. It provides a cushion for companies during difficult times, and allows them to swiftly take advantage of growth opportunities by expansion. A study conducted by Sloan [24] showed that the cash flow component of earnings is a better indicator of the persistence of earnings performance than the accrual component of earnings. We study cash flows generated from regular business operations as they are closely related to supply chain activities. Among the three supply chain flows, physical, information, and cash, previous supply chain studies focused more on the first two flows. For example, the bullwhip effect, which causes increasing fluctuations of order patterns moving upstream along a supply chain, demonstrates the relationship between the information flow and physical flow [14], and a great number of studies have devoted to quantifying and/or identifying ways to reduce such an effect (see for example, [1,3,6,8,9,15,16,17,18,23]). However, the relationship between the physical flow and cash flow is less explored. In [4], the authors recognized a trend in which more corporate executives are now extending the supply chain manager's accountability from functional efficiency (reducing operating costs) to organization wide efficiency such as cash flow efficiency. As a result, a better understanding of the causal relationship between supply chain performance and financial measures is critical to both supply chain and financial managers. The main objective of this study is to establish such a relationship with a focus on cash flow risks using a simple framework which allows us to observe the dynamics of supply chain related cash flows.

The Cash Conversion Cycle (CCC) [10], also known as the Cash-to-Cash Cycle or simply the Cash

Cycle, is heavily dependent on a company's supply chain capability. Shorter CCC means lower financial costs to fund business operations. To reduce the CCC, a company can reduce days-in-inventory, shorten days-in-receivables and prolong days-in-payables. These three time-related factors are affected by the lead time of production, credit periods of receivables and payables, and early collection/payment patterns due to trade discounts. Dell Computer financed its parts and components costs with the credit offered by its suppliers because of its negative 40 days CCC [22]. This practice puts more financial burdens on smaller suppliers, who either need to finance the credit periods with a higher interest rate, or offer deep early payment discounts to reduce CCC. Moreover, a potential problem of focusing on reducing the CCC is that it does not address any risk factors. For example, when a discount is offered as a means to reduce daysin-receivables, it usually increases cash inflow risks due to the lack of knowledge in predicting the amount of early collection. The main purpose of this study is to measure the supply chain cash flow risks with respect to a few time related risk factors, including the lead time, credit periods of Accounts Receivable (AR) and Accounts Payable (AP), and early receipt/ payment patterns.

We show that some common practices intended to reduce the CCC can lead to higher cash flow risks and demonstrate that properly structured asset-backed securities, which acquire a fixed portion of AR, can reduce a vendor's financial costs, CCC and cash inflow risks. The next section lays the groundwork for this study including the assumptions and the relationships among demands, sales, inventories and cash flows. Section 3 introduces the design of the simulation study and presents all simulation results. Section 4 establishes the analytical result to support the use of Asset-Backed Securities (ABS) as a win-win solution to finance accounts receivable and identifies the best ABS policy to minimize cash inflow risks. Section 5 provides the conclusion of this study.

## 2. Measuring cash flow risks

Supply chain management emphasizes the coordination among supply chain members from suppliers and their suppliers to distributors and their customers. Lee and others [15] quantified the bullwhip effect and showed the potential of variance reduction due to information sharing. Raghunathan [21] showed that the variance reduction due to information sharing was not as much as what originally indicated in [15] because suppliers could extract demand information from order information given by their customers when demands are stationary.

On the cash flow side, the CCC is one of the popular supply chain performance measures [5,26]. It contains three elements, 1) days in inventory, 2) days in receivables, and 3) days in payables, and can be expressed as

$$
\begin{array}{r l} \text { CCC } & = \text { Inv } / (\text { COGS } / 3 6 5) + \text { AR } / (\text { Sales } / 3 6 5) \\ & - \text { AP } / (\text { COGS } / 3 6 5) \end{array}
$$

where Inv and COGS represent average inventory and annual Cost of Goods Sold respectively. The three cycle times vary across industries and may depend on the market power of the organization with respect to its customers and suppliers. The three time related factors that impose significant influences on the CCC and cash flow risks to an organization are:

(1) The lead time for internal processing (production and delivery) and the timing of its related cash outflows,

(2) The credit periods for AR to its customers and the pattern of early collection of AR, and

(3) The credit periods for AP from its suppliers and the pattern of early payment of AP.

Since most trade terms are negotiated for a long period of time, we assume that trade discounts for early collection of AR and early payment of AP are constants. As a result, the patterns of early collection and payment are independent of the discount rates. Using a three tier supply chain structure, we assume the organization of interest is a manufacturer who purchases parts and components from several suppliers and delivers finished goods to several customers. It adopts a make-to-stock policy in which all orders received in each period are shipped in the same period and unfilled orders are lost. There is an l-period lead time needed to process and ship finished goods to the customers, during which the payment for processing and shipping costs are evenly spread. The manufacturer offers a credit term, (c /1, net r), to its customers, i.e., $\mathrm { { a } } c _ { r }$ (usually 2%) discount if payment is received in the next period after delivery or the full amount is due within r periods. We assume customers either pay within the discount period or wait until the full term because there is no incentive to pay early after missing the discount period. Similarly, there is a credit term granted by the suppliers to the manufacturer, $( c _ { p } / 1$ net $p )$ . The length of each period is determined by the review cycle of cash related decisions. In any time period t, the proposed model allows the manufacturer to produce a cash flow forecast with an emphasis on the cash flow risk (standard deviation) for future periods based on supply chain activities.

## 2.1. Demands

When quantifying the bullwhip effect in a supply chain, Lee et al. [15] used an $A R ( 1 )$ autoregression model first appeared in [11],

$$
D _ {t + 1} = d + \rho D _ {t} + \epsilon_ {t + 1}, t = 0, 1, 2, \dots\tag{1}
$$

for the demand of time period $t + 1$ given the demand of time period $t , D _ { t } ,$ where d is a constant and $- 1 \leq \rho \leq 1$ is the correlation between $D _ { t }$ and $D _ { t + 1 }$ . The noise element, $\epsilon _ { t + 1 } , \ t \geq 0$ is a random variable drawn from an independent identically distributed normal distribution $N ( 0 , \sigma ^ { 2 } )$ . Note that $D _ { i }$ in [15] represents the quantity of goods whereas in this study, $D _ { i }$ denotes the total dollar amount of all orders in time period i.

In order to make the production decision discussed in the next section, we need to forecast future demand $D _ { t + i }$ from its expected value $E [ D _ { t + i } ]$ . The following Lemma expresses all expected future demands and their associated risks in terms of $d , \rho , D _ { t } ,$ and time period index $t + i .$ . It also provides some asymptotic behavior of future demands.

Lemma 2.1. Given the AR (1) demand distribution in (1), the following results hold when $D _ { t }$ is known.

(1) $\begin{array} { r } { E [ D _ { t + i } ] = \mu _ { t + 1 } = \frac { d ( 1 - \rho ^ { i } ) } { 1 - \varrho } + \rho ^ { i } D _ { t } } \end{array}$ or in expanded form as $d ( 1 + \rho + \rho ^ { 2 } + \cdots + \rho ^ { i - 1 } ) + \rho ^ { i } D _ { t }$

(a) When $\rho {  } 0 , \mu _ { t + i } { \longrightarrow } d$

(b) When $\rho {  } 1 , \mu _ { t + \mathrm { i } } {  } i d { + } D _ { t } .$

(c) When $\rho {  } { - } 1 , \mu _ { t + i } {  } [ i \mathrm { m o d } \ 2 ] d { + } ( - 1 ) ^ { i } D _ { t } .$

(2) $\begin{array} { r } { \mathrm { V a r } [ D _ { t + i } ] = \sigma _ { t + i } ^ { 2 } = \frac { \sigma ^ { 2 } \left( 1 - \rho ^ { 2 i } \right) } { 1 - \rho ^ { 2 } } } \end{array}$ or in expanded form as $\sigma ^ { 2 } ( 1 + \rho ^ { 2 } + \rho ^ { 4 } + . . . + \rho ^ { 2 ( i - 1 ) } )$

(a) When $\rho {  } 0 , \sigma _ { t + i } ^ { 2 }  \sigma ^ { 2 }$

(b) When $\rho {  } \pm 1 , \sigma _ { t + i } ^ { 2 } \mathrm {  } i \sigma ^ { 2 }$

(3) $\mathrm { C o v } [ D _ { t + i } , D _ { t + j } ] = \rho ^ { j - i } \sigma _ { t + i } ^ { 2 } f o r j > i > 0 .$

(a) When $\rho {  } 0 , \mathrm { C o v } [ D _ { t + i } , D _ { t + j } ] {  } 0 .$

(b) When $\rho \to 1 , \mathrm { C o v } [ D _ { t + i } , D _ { t + j } ] \to i \sigma ^ { 2 }$

(c) When $\iota \rho \mathrm { - } \mathrm { - } 1 , \mathrm { C o v } [ D _ { t + i } , \bar { D _ { t + j } } ] \mathrm { - } ( - 1 ) ^ { j - i } i \sigma ^ { 2 } .$

Proof. See Appendix A.

The rest of this paper assumes $\rho { > } 0$ , which is more reasonable in practice.

## 2.2. Production, inventory, and sales

Let $K _ { t + i }$ be the amount of production in sales value completed the l-period process in period $t + i .$ Due to the lead time, parts and components for $K _ { t + i }$ must arrive in $t + i - l$ and the production be started in $t + i - l + 1$ to meet the potential demand in $t + i .$ Hence, the level of production $( K _ { t + i } )$ is determined by the forecast of the future demand, $D _ { t + i } ,$ and inventory level, $I _ { t + i - 1 }$ , from period $t + i - 1$ . The sales amount in $t + i$ is thus S = Min $( D _ { t + i } , I _ { t + i - 1 } +$ $K _ { t + i } )$ . When $D _ { t + i } > I _ { t + i - 1 } + K _ { t + i } ,$ we have lost sales. Otherwise, we have inventory $I _ { t + i } { > } 0$ due to forecast errors. The inventory level at the end of $t + i$ is determined by $I _ { t + i } { = } \mathrm { M a x } ( I _ { t + i - 1 } { + } K _ { t + i } { - } S _ { t + i } , 0 )$ . To reduce the chance of stockout, the manufacturer includes a fixed level of safety stock, SS, in the inventory. Because $D _ { i } , i { = } 1 , 2 , . . . ,$ are random variables, $K _ { i } , S _ { i } ,$ , and $I _ { i }$ are also random variables. When the value of a random variable $V _ { i }$ is realized, we denote it as ${ \bar { V } } _ { i } .$ . The cost of processing $K _ { t + i }$ is consisted of two parts, the processing and shipping/ handling cost which we call the α-cost and the parts and components cost which is called the $\beta \mathrm { - c o s t }$ . The α-cost is a fixed percentage, α, of $K _ { i }$ for all i. It includes labor cost and any overheads that can be attributed to $K _ { i }$ . The β-cost is also a fixed percentage, $\beta ,$ of $K _ { i }$ for all i. It covers the parts/components cost. If $\alpha + \beta < 1$ , we have a positive gross profit.

The manufacturer makes its production decision in time period t for $K _ { t + l }$ by substituting the involved random variables with their realized values if realized or with their expected values if not realized yet. Table 1 lists the relationship between these variables using an example in which $l { = } 3$ . In the table, all the values of $K _ { i } , \ S _ { i } ,$ and $I _ { i }$ for $i \leq t$ are realized. The expected value $E _ { t } [ D _ { t + i } ]$ based on information available in time period t is used as the forecast for $D _ { t + i } .$ Due to the 3-period lead time, production level $\bar { K } _ { t + 3 } =$ $E _ { t } [ D _ { t + 3 } ] + ( \mathrm { S S } - E _ { t } [ I _ { t + 2 } ] )$ is committed in period t based on the forecast demand $E _ { t } [ D _ { t + 3 } ]$ and an adjustment factor $\mathrm { S S } - E _ { t } [ I _ { t + 2 } ]$ to maintain the safety stock level when $\mathrm { S S } { > } E _ { t } [ I _ { t + 2 } ]$ or to reduce excessive inventory when $\mathrm { S S } { < } E _ { t } [ I _ { t + 2 } ]$ . For simplicity reason we omit the subscript t for all expected values estimated based on information available at time t, i.e., $( E [ X ] \equiv E _ { t } [ X ] )$ Likewise, $\bar { K } _ { t + 1 } { = } E _ { t - 2 } [ D _ { t + 1 } ] { + } \mathrm { S S } { - } E _ { t - 2 } [ I _ { t } ]$ and $\bar { K } _ { t + 2 } =$ $E _ { t - 1 } [ D _ { t + 2 } ] + \mathrm { S S } - E _ { t - 1 } [ I _ { t + 1 } ]$ have been determined earlier in time periods $t - 2$ and $t - 1$ respectively based on the information available then. To obtain the value of $E [ I _ { t + 2 } ]$ for the adjustment factor in $\bar { K } _ { t + 3 } ,$ one can recursively substitute the terms in $I _ { t + 2 } , S _ { t + 2 } , I _ { t + 1 }$ , and $S _ { t + 1 }$ from Columns (3) and (4) of Table 1 until all terms are replaced by either realized constants or expected future demands to reach

Table 2  
Demand, production and sales in various time periods

<table><tr><td>Time</td><td>(1)  $D_i$ </td><td>(2)  $K_i (l=3)$ </td><td>(3)  $S_i$ </td><td>(4)  $I_i$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>t-2</td><td> $\overline{D}_{t-2}$ </td><td> $\overline{K}_{t-2}$ </td><td> $\overline{S}_{t-2}$ </td><td> $\overline{I}_{t-2}$ </td></tr><tr><td>t-1</td><td> $\overline{D}_{t-1}$ </td><td> $\overline{K}_{t-1}$ </td><td> $\overline{S}_{t-1}$ </td><td> $\overline{I}_{t-1}$ </td></tr><tr><td>t</td><td> $\overline{D}_t$ </td><td> $\overline{K}_t$ </td><td> $\overline{S}_t$ </td><td> $\overline{I}_t$ </td></tr><tr><td>t+1</td><td> $D_{t+1}$ </td><td> $\overline{K}_{t+1}=E_{t-2}[D_{t+1}]+SS-E_{t-2}[I_t]$ </td><td> $S_{t+1}=\text{Min}(D_{t+1},\overline{I}_t+\overline{K}_{t+1})$ </td><td> $I_{t+1}=\text{Max}(\overline{I}_t+\overline{K}_{t+1}-S_{t+1},0)$ </td></tr><tr><td>t+2</td><td> $D_{t+2}$ </td><td> $\overline{K}_{t+2}=E_{t-1}[D_{t+2}]+SS-E_{t-1}[I_{t+1}]$ </td><td> $S_{t+2}=\text{Min}(D_{t+2},I_{t+1}+\overline{K}_{t+2})$ </td><td> $I_{t+2}=\text{Max}(I_{t+1}+\overline{K}_{t+2}-S_{t+2},0)$ </td></tr><tr><td>t+3</td><td> $D_{t+3}$ </td><td> $\overline{K}_{t+3}=E[D_{t+3}]+SS-E[I_{t+2}]$ </td><td> $S_{t+3}=\text{Min}(D_{t+3},I_{t+2}+\overline{K}_{t+3})$ </td><td> $I_{t+3}=\text{Max}(I_{t+2}+\overline{K}_{t+3}-S_{t+3},0)$ </td></tr><tr><td>t+4</td><td> $D_{t+4}$ </td><td> $E[K_{t+4}]=E[D_{t+4}]$ </td><td> $S_{t+4}=\text{Min}(D_{t+4},I_{t+3}+K_{t+4})$ </td><td> $I_{t+4}=\text{Max}(I_{t+3}+K_{t+4}-S_{t+4},0)$ </td></tr><tr><td>t+5</td><td> $D_{t+5}$ </td><td> $E[K_{t+5}]=E[D_{t+5}]$ </td><td> $S_{t+5}=\text{Min}(D_{t+5},I_{t+4}+K_{t+5})$ </td><td> $I_{t+5}=\text{Max}(I_{t+4}+K_{t+5}-S_{t+5},0)$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>

$$
E [ I _ {t + 2} ] = \left\{ \begin{array}{l l} \overline {{I}} _ {t} + \overline {{K}} _ {t + 1} + \overline {{K}} _ {t + 2} - E [ D _ {t + 1} ] - E [ D _ {t + 2} ] & \text { if } E [ I _ {t + 1} ], E [ D _ {t + 2} ] > 0 \\ \overline {{K}} _ {t + 2} - E [ D _ {t + 2} ] & \text { if } E [ I _ {t + 1} ] = 0, E [ D _ {t + 2} ] > 0. \\ 0 & \text { if } E [ S _ {t + 2} ] = 0 \end{array} \right.
$$

In general, the production decision in period t is made according to $\bar { K } _ { t + l } { = } E [ D _ { t + l } ] + \mathrm { S S } - [ I _ { t + l - 1 } ]$ . Future production levels, $K _ { t + i } , \ i \geq l + 1$ , do not need to be committed until later periods. Thus, we simply set $E [ K _ { t + i } ] =$ $E [ D _ { t + i } ]$ because the adjustment factor is zero due to the fact that $E [ I _ { t + i - 1 } ] { = } \mathrm { S S }$ for $i \geq l + 1$ before obtaining any further information to update future forecast errors. Even though $\mathrm { V a r } [ D _ { t + i } ]$ increases as i increases, the manufacturer adopts a constant SS because future production levels after $t + l$ will be determined later with the arrival of new information, which reduces the variances because $\mathrm { V a r } _ { t } [ D _ { t + i } ] \geq \mathrm { V a r } _ { t + 1 } [ D _ { t + i } ]$ according to Lemma 2.1.

$0 \leq \gamma _ { t + i } \leq 1$ and $S _ { t + i - 1 }$ are random variables. Further, they are independent of each other because customers do not coordinate their payment activities amongst themselves. The balance of the sales $( 1 - \gamma _ { t + i } ) S _ { t + i - 1 }$ is due in period $t + i + r - 1$ due to the credit term of r periods. Note that for early collection, the manufacturer actually receives $( 1 - c _ { r } ) R _ { t + i }$ instead of $R _ { t + i } ,$ because of the early collection discount. Thus, total cash inflow in time period t +i can be written as

$$
\begin{array}{c} \mathrm{IN} _ {t + i} = (1 - c _ {r}) R _ {t + i} + (S _ {t + i - r} - R _ {t + i - r + 1}) \\ = (1 - c _ {r}) \gamma_ {t + i} S _ {t + i - 1} \\ \quad + (1 - \gamma_ {t + i - r + 1}) S _ {t + i - r},   i = 1, 2, \ldots \end{array}\tag{2}
$$

## 2.3. Cash inflows and outflows

We use $R _ { t + }$ to represent the amount credited to AR due to early collection from customers for the sales, $S _ { t + i - 1 }$ , in period $t + i - 1$ $R _ { t + i } { = } \gamma _ { t + i } S _ { t + i - 1 }$ is a random variable because we assume both the proportion of early collection

Table 2 details the cash inflows and outflows based on the same scenario in Table 1 and $r = 3 , p = 2$ . Again, all random variables for periods on and before period t are known constants. Column (5) shows the amount of early collection credited to AR when received one period after the sales. Column (6) records the total cash inflow in each period. It is consisted of the cash receipt from the early collection of the previous period delivery and collection of the unpaid portion of sales completed r periods ago. Due to the 3-period credit term, in t + 1, t + 2 the manufacturer is still collecting from realized sales in the past where $\overline { { \gamma } } _ { t - 1 } , \ \overline { { \gamma } } _ { t }$ and $\overline { { S } } _ { t - 2 } , \ \overline { { S } } _ { t - 1 }$ are known constants. In $t + 3 , \overline { { S } } _ { t }$ is known, but $\gamma _ { t + 1 }$ is not realized yet, leading to a higher risk than those in t + 1 and $t { + } 2$ After t + 3, every element in Eq. (2) is a random variable. As a result, the cash inflow risks in the first two periods of the planning horizon are substantially lower than the later periods.

Cash inflows and outflows in various time periods

<table><tr><td>Time</td><td>(5)  $R_{i}$ </td><td>(6) IN $_{i}$ (r=3)</td><td>(7)  $\alpha_{i}$ (l=3)</td><td>(8)  $\beta_{i}$ (p=2)</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>t-2</td><td> $\overline{R}_{t-2}$ </td><td> $\overline{\text{IN}}_{t-2}$ </td><td> $\overline{\alpha}_{t-2}$ </td><td> $\overline{\beta}_{t-2}$ </td></tr><tr><td>t-1</td><td> $\overline{R}_{t-1}$ </td><td> $\overline{\text{IN}}_{t-1}$ </td><td> $\overline{\alpha}_{t-1}$ </td><td> $\overline{\beta}_{t-1}$ </td></tr><tr><td>t</td><td> $\overline{R}_{t}$ </td><td> $\overline{\text{IN}}_{t}$ </td><td> $\overline{\alpha}_{t}$ </td><td> $\overline{\beta}_{t}$ </td></tr><tr><td>t+1</td><td> $R_{t+1}=\gamma_{t+1}\overline{S}_{t}$ </td><td> $(1-c_{r})R_{t+1}+(1-\overline{\gamma}_{t-1})\overline{S}_{t-2}$ </td><td> $\alpha(\overline{K}_{t+1}+\overline{K}_{t+2}+\overline{K}_{t+3})/3$ </td><td> $\beta[(1-c_{p})\delta_{t+1}\overline{K}_{t+3}+(1-\delta_{t})\overline{K}_{t+2}]$ </td></tr><tr><td>t+2</td><td> $R_{t+2}=\gamma_{t+2}S_{t+1}$ </td><td> $(1-c_{r})R_{t+2}+(1-\overline{\gamma}_{t})\overline{S}_{t-1}$ </td><td> $\alpha(\overline{K}_{t+2}+\overline{K}_{t+3}+K_{t+4})/3$ </td><td> $\beta[(1-c_{p})\delta_{t+2}K_{t+4}+(1-\delta_{t+1})\overline{K}_{t+3}]$ </td></tr><tr><td>t+3</td><td> $R_{t+3}=\gamma_{t+3}S_{t+2}$ </td><td> $(1-c_{r})R_{t+3}+(1-\gamma_{t+1})\overline{S}_{t}$ </td><td> $\alpha(\overline{K}_{t+3}+K_{t+4}+K_{t+5})/3$ </td><td> $\beta[(1-c_{p})\delta_{t+3}K_{t+5}+(1-\delta_{t+2})K_{t+4}]$ </td></tr><tr><td>t+4</td><td> $R_{t+4}=\gamma_{t+4}S_{t+3}$ </td><td> $(1-c_{r})R_{t+4}+(1-\gamma_{t+2})S_{t+1}$ </td><td> $\alpha(K_{t+4}+K_{t+5}+K_{t+6})/3$ </td><td> $\beta[(1-c_{p})\delta_{t+4}K_{t+6}+(1-\delta_{t+3})K_{t+5}]$ </td></tr><tr><td>t+5</td><td> $R_{t+5}=\gamma_{t+5}S_{t+4}$ </td><td> $(1-c_{r})R_{t+5}+(1-\gamma_{t+3})S_{t+2}$ </td><td> $\alpha(K_{t+5}+K_{t+6}+K_{t+7})/3$ </td><td> $\beta[(1-c_{p})\delta_{t+5}K_{t+7}+(1-\delta_{t+4})K_{t+6}]$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>

Column (7) lists the α-cost in each period. Due to the 3-period lead time, there are three production batches running simultaneously in each period at three different stages toward completion. The α-cost in $t + 1$ involves three committed production batches, $\overline { { K } } _ { t + 1 } , \overline { { K } } _ { t + 2 } .$ , and $\begin{array} { r } { \bar { K } _ { t + 3 } . } \end{array}$ . Hence the risk is zero. It increases in periods $t { + } 2$ and t + 3 as the constant portion of the α-cost is diminishing. In general, the α-cost in $t + i$ for processing the l batches, $\begin{array} { r } { K _ { t + i } , . . . , K _ { t + i + l - 1 } \mathrm { i } \mathbf { i } \mathbf { s } \frac { \alpha } { l } \sum _ { k = 0 } ^ { l - 1 } K _ { t + i + k } } \end{array}$ . Column (8) records the β-cost in each period. For example, due to the production lead time, parts and components for $K _ { t + 4 }$ are received in $t + 1$ . In $t { + } 2$ , the manufacturer pays $( 1 - c _ { p } ) \delta _ { t + 2 } \beta K _ { t + 4 }$ for an early payment discount and starts processing $K _ { t + 4 } . \ \delta _ { t + 2 }$ is a random variable representing the proportion of $\beta K _ { t + 4 }$ paid early. The balance is paid in period $t { + } 3$ due to the credit term $p { = } 2$ . In period $t + 2 ,$ , the manufacturer also pays the balance of $\beta \bar { K } _ { t + 3 }$ delivered in t. Thus total β-cost in $t { + } 2$ is $\beta [ ( 1 - c _ { p } ) \delta _ { t + 2 } K _ { t + 4 } + ( 1 - \delta _ { t + 1 } ) \bar { K } _ { t + 3 } ]$ . Periods $t + 1$ and $t { + } 2$ have lower β-cost risks because they include the payment to some realized purchases of parts and components.

The time shift of cash inflows between sales and cash receipts is contributed by the credit term, $r ,$ and the time shift between the internal operations and the realization of the α-cost is due to the lead time, l. However, the time shift between the receipt of parts/ components and the realization of the β-cost is affected by both l and the credit term, $p .$ . In general, for period t + i, $0 \leq \delta _ { t + i } \leq 1$ is a random variable, independent of $\beta K _ { t + i + l - 1 }$ (delivered in $t + i - 1 )$ , representing the proportion of $\beta K _ { t + i + l - 1 }$ paid early in period $t + i .$ In addition, the manufacturer pays for the parts and components received $p$ periods ago for the production of $K _ { t + i + l - p }$ less the early payment made in $t ^ { + } i ^ { - } p ^ { + } 1$

Thus, total cash outflow in period $t + i$ is

$$
\begin{array}{l} O _ {t + i} = \beta \big [ (1 - c _ {p}) \delta_ {t + i} K _ {t + i + l - 1} + (1 - \delta_ {t + i - p + 1}) K _ {t + i + l - p} \big ] \\ \quad + \frac {\alpha}{l} \sum_ {k = 0} ^ {l - 1} K _ {t + i + k}, \text {   for   } i = 1, 2, \dots \end{array}\tag{3}
$$

In practice, an individual order might not be split and paid partially for a discount. However, since $S _ { i }$ and $K _ { i }$ represent the sum from a large number of orders, we assume that the overall portion of orders paid early can be approximated by $\gamma _ { i }$ and $\delta _ { i } .$ . From the discussion based on the example in Tables 1 and 2, we learn that lead times and credit terms cause the time gap between supply chain physical flows (sales) and cash flows. Longer lead times and credit terms reduce the risks of cash flows due to a larger realized portion of the random variables involved. It, however, increases the CCC.

Summing up Eqs. (2) and (3), we obtain the netflow for each period as

$$
\begin{array}{l} N _ {t + i} = (1 - c _ {r}) \gamma_ {t + i} S _ {t + i - 1} + (1 - \gamma_ {t + i - r + 1}) S _ {t + i - r} \\ \quad - [ \beta (1 - c _ {p}) \delta_ {t + i} K _ {t + i + l - 1} + \beta (1 - \delta_ {t + i - p + 1}) K _ {t + i + l - p} \\ \quad + \frac {\alpha}{l} \sum_ {k = 0} ^ {l - 1} D _ {t + i + k} ] \text {   for   } i = 1, 2, \dots \end{array} \tag {4}
$$

From (4), when there is no early collection and payment (all $\gamma _ { k }$ and $\delta _ { k }$ are 0), the netflow reduces to

$$
N _ {t + i} = S _ {t + i - r} - \beta K _ {t + i + l - p} - \frac {\alpha}{l} \sum_ {k = 0} ^ {l - 1} K _ {t + i + k}.\tag{5}
$$

When $p { = } l { + } r ,$ the suppliers fully finance the manufacturer's β-cost to cover the periods of processing lead time and AR credit terms because $N _ { t + i } =$ $\begin{array} { r } { S _ { t + i - r } - \beta K _ { t + i - r } - \ \frac { \alpha } { l } \sum _ { k = 0 } ^ { l - 1 } K _ { t + i + k } } \end{array}$ , i.e., receiving the payment for the sales of $S _ { t + i - r }$ from the customers and paying the β-cost to the suppliers for $K _ { t + i - r }$ in the same period. When $p { > } l { + } r ,$ the suppliers finance the manufacturer beyond what they delivered. This scenario usually happens between a small vendor and its larger and more dominant customers, where the vendor is compelled to accept longer credit terms in order to keep the business. However, the financial cost would have been lower should the customers finance their own accounts payable because larger organizations normally receive more favorable terms from the banks than smaller companies. All phenomena described in this section are verified by the simulation study detailed in the next section.

## 3. Simulation experiements

## 3.1. Design of simulation experiments

The simulation study is designed to identify the patterns of cash flows under the assumptions described in the previous section. Unless specified otherwise, all simulation runs are conducted based on the following parameters.

(1) d= 200 and $\sigma = 2 5 \mathrm { : }$ : We set σ significantly smaller than d to avoid negative demands and large forecast errors. In addition, the safety stock SS is set at 3σ

(2) t = 30: We set the decision point at period 30, allowing the demand process to settle into a stable state.

(3) $\alpha + \beta { = } 0 . 9 $ : This is to allow a 10% gross margin, in-line with most matured products.

(4) An eight-period planning horizon: Due to the $\rho \mathrm { - }$ factor, the $\operatorname { A R } ( 1 )$ series becomes stationary after a few periods, i.e., $E [ D _ { t + k } ] \approx E [ D _ { t + k + 1 } ] \approx$ $E [ D _ { t + k + 2 } ] \approx$ The phenomenon limits the model's ability to forecast demands too far into the future. Therefore, we set our planning horizon to eight periods.

(5) ρ = 0.7: As mentioned earlier, a positive $\rho$ is more reasonable in practice. The value of 0.7 is chosen to ensure that it is not too small to turn the expected future demands stationary very soon. Lower $\rho$ values make the demand stable and the problem less challenging.

(6) Distributions of $\dot { \gamma } _ { i }$ and $\delta _ { i } \colon$ Three distributions and a constant rate are chosen to represent the behavior of $\gamma _ { i } .$ The uniform distribution represents the scenario where there is no knowledge about the trading partners' early payment patterns. On the other extreme, the constant rate represents the scenario of having complete knowledge about the early payment pattern. The normal distribution and triangular distribution are somewhere between the two extreme scenarios, where the former is a popular distribution and the latter is easy for a decision maker to estimate its parameters. For $\delta _ { i } ,$ we use a triangular distribution with a smaller range since the manufacturer has better knowledge about its own early payment pattern.

All simulation results presented hereafter are obtained from the averages of 500 simulation runs. The first simulation result presented in Fig. 1 verifies the accuracy of the simulation setup by comparing the expected demands obtained from Lemma 2.1 and the average demands from the simulation runs for periods t + 1 to t + 8 along with their respective one standard deviation ranges. The center line and the two one-standard-deviation lines overlap greatly between the expected and simulated results. The chart shows that the risks (standard deviations) of future demands increase over time and the simulated results closely follow the analytical results. From (2) of Lemma 2.1, we observe that $\sigma _ { t + } ^ { \dot { 2 } }$ increases as we move toward future periods (larger i) when $\rho \neq 0 .$ . In addition, $\sigma ^ { 2 } < \sigma _ { t + i } ^ { ~ 2 } < i \sigma ^ { 2 }$ provides the upper and lower bounds for $\sigma _ { t + i } ^ { 2 }$ . When demands are highly dependent $( \rho \to \pm 1 )$ ), the variances of future demands increase linearly with respect to i.

![](/api/attachments/AJKWE9QK/fulltext/images/034d7d1cab31b7abd0eb200869f902c62c9c416cf49c606fb26434f90c8ee7ed.jpg)  
Fig. 1. 1-Std range of expected and simulated demands.

![](/api/attachments/AJKWE9QK/fulltext/images/98a8dbdd18639693b1a994eaad4737f923b0ee0cea775f694383c514a76cf3f9.jpg)  
Fig. 2. Expected demands and sales.

Fig. 2 shows the expected demands and average simulated sales under three levels of SS and beginning inventory $\textstyle { \overline { { I _ { t } } } } ,$ namely, (1) SS = I<sup>¯</sup><sub>t</sub> = 0, (2) ${ \mathrm { S S } } { = } \overline { { I _ { t } } } { = } 3 \sigma$ , and (3) ${ \mathrm { S S } } { = } \overline { { I _ { t } } } { = } 5 \sigma$ when l = 3. As SS increases, the chance of stockout is reduced resulting in a smaller gap between the average sales line and the expected demand line. In the cases of $\mathrm { \partial S } = 3 \sigma$ and $\mathrm { S } \mathrm { S } { = } 5 \sigma$ , the gap grows bigger as we move toward later periods. In the SS= 0 case, the gap is more significant starting from t + 1 due to the lack of beginning inventory and safety stock to meet demands in all periods. According to the periodical review model, future production levels (those after period t +l) will be reevaluated and committed later with additional information, providing a chance to reduce the gap.

## 3.2. Cash inflows

Fig. 3 shows the simulated cash inflow risks, $\sqrt { \mathrm { V a r } [ \mathrm { I N } _ { t + i } ] }$ , under l=3, r=4, SS=3σ and the three distributions of $\gamma _ { t + i }$ mentioned earlier plus two constant $\gamma \mathbf { \ ' } _ { \mathbf { S } }$ . The cash inflow risks from the constant $\gamma = 0$ and $\gamma { = } 0 . 5$ (standard deviation = 0) cases are much lower than those from the remaining three distributions with the uniform distribution U(0,1) (standard deviation= 0.289)

![](/api/attachments/AJKWE9QK/fulltext/images/7d0e65e941bed6261b91ee967e8486f73529567d1b08b1f245e67501495870be.jpg)  
Fig. 3. Cash inflow risks.

having the highest risk followed by the normal distribution, N(0.5, 0.2<sup>2</sup>) (standard deviation= 0.2), and the triangular distribution, Triang(0.2, 0.5, 0.8) (standard deviation= 0.122). When there is no early collection discount offered, there is no incentive for early payment, resulting in $\gamma = 0$ . It has zero risk in the first 4 periods due to the collection of realized sales. If we use it as a benchmark for assessing cash inflow risks from early collection, the case when $\gamma { = } 0 . 5$ is the only one that does not significantly elevate the cash inflow risk. In addition, the more the manufacturer knows about the early collection patterns of its customers (smaller standard deviations for the $\gamma _ { t + i }$ distribution), the lower the early collection risk. Except for the γ = 0 case, all distributions have a mean of 0.5. Average cash inflows for the Triang (0.2, 0.5, 0.8) case is charted in Fig. 4 with its $\pm 3 \sigma _ { t + i }$ range. Figs. 3 and 4 also support our earlier observation that the first r − 1 periods involve lower cash inflow risks. Period t + 2 has a higher cash inflow than period t + 1 and t + 3 because the early collection in period $t - 1 , \overline { { \gamma } } _ { t - 1 } \overline { { S } } _ { t - 2 } ,$ happened to be low resulting in the higher balance collected at the end of the credit period. Fig. 5 shows the average stockout amount and the probability of stockout from the 500 simulation runs under l=3 and SS=3σ. Although the stockout amount is small relative to the demand level, it and the probability of stockout increase over time as the risks for future demands are higher. Note that with the arrival of new information in t + 1, the production level for t + 4 will be reevaluated and committed. As a result, the probability of stockout will reduce with every periodical update.

![](/api/attachments/AJKWE9QK/fulltext/images/ff5f608fe7902dc39142f00525a1ef26145255acab5d707e2ea19fb734d98130.jpg)  
Fig. 4. 3-Std cash inflow range.

![](/api/attachments/AJKWE9QK/fulltext/images/2c9260d87dde6dc60c232b4bbf0de5f3cd2d9a6f4305001f999983a2e5800035.jpg)  
Fig. 5. Stockout amount and probability.

The simulation result shows that using cash discounts to shorten the CCC may increase the cash inflow risk due to the added risk derived from the early collection pattern unless the early collection ratio is a constant. According to the simulation result in Figs. 3 and 4, a company having available credit lines with its banks can set a higher and riskier AR collection policy either by shortening the credit period r or by offering higher trade discount $c _ { r }$ because it has a better leverage to cope with the increased risk in the future, t + r and beyond. For businesses having tight credit lines and needing longer time to raise cash, offering longer credit terms makes future cash inflows more predictable in the next r − 1 periods at the cost of worsening its CCC.

## 3.3. Cash outflows and netflows

As the manufacturer has more control over its own payment to its suppliers, we use a triangular distribution with a smaller range $\delta _ { t + i } = T r i a n g ( 0 . 1 5 , \ 0 . 2 , \ 0 . 2 5 )$ (standard deviation= 0.02). The first three lines in Fig. 6 shows the simulated cash outflow risks under three different combinations of $( \alpha { , } \beta )$ and $l { = } 5 , p { = } 2$ . The three instances are (0.1, 0.8), (0.45, 0.45) and (0.8, 0.1) where $\alpha + \beta$ is always 0.9. The fourth line represents the (0.8, 0.1) case but with $l { = } p { = } 3$ for comparison purposes. All other simulation parameters are the same as before. Comparing the first three lines, the cash outflow risk in the (0.1, 0.8) case (Line 1) reveals more of the risk derived from the β-cost while the (0.8, 0.1) (Line 3) case demonstrates more of the risk pattern from the α-cost. Apparently, the β-cost contributes more to the outflow risk because Line 1 is above Line 3. As observed in Section 2.3, Line 1 has lower risks in the first two periods because $p { = } 2$ . Similarly, due to l = 5, Line 3 gradually increases from t + 1 to t + 5 and reaches a stable level after t + 5 because the realized portion of the α-cost is diminishing from t + 1 to t + 5. Line 2 stays in-between Line 1 and Line 3 as the outflow is equally divided between the α-cost and β-cost.

![](/api/attachments/AJKWE9QK/fulltext/images/19c2c60306457ac88f3906c2eba183ce3b06b426d6dab4c0ab631e8f476f0f5b.jpg)  
Fig. 6. Cash outflow risks.

Comparing Line 3 with Line 4, both have the same $\alpha { = } 0 . 8$ and $\beta { = } 0 . 1$ cost structure. Due to the different lead times, Line 3 reaches its stable level later than Line 4 and always has a lower risk. There are two reasons to explain this phenomenon. First, the l = 5 case has two more periods in which the α-cost involves a portion of committed production levels than the l = 3 case. Second, for the periods after t + l, the α-cost, $\textstyle { \frac { \alpha } { l } } \sum _ { k = 0 } ^ { l - 1 } K _ { t + i + k }$ is an average of l random variables. Analogous to a random variable representing a sampling distribution, the more identically distributed random variables in the average, the smaller the standard deviation $\left( s _ { \overline { { X } } } = s / \sqrt { n } \right)$ . Even though in the α-cost case, the variables are not identically distributed, the difference in their variances is getting smaller after t + l. This explains why longer lead times reduce the risk of the α-cost. However, it requires the manufacturer to commit to a production level earlier, resulting in a higher forecast error.

Fig. 7 shows the net cash flow $( \mathrm { I N } _ { t + i } - O _ { t + i } )$ with its three standard deviation range where $r { = } 4 , p { = } 3$ , $l { = } 3 , \ \alpha { = } 0 . 8 , \ \beta { = } 0 . 1$ and $\gamma _ { t + i + 1 } { \sim } T r i a n g ( 0 . 2 , 0 . 5 , 0 . 8 )$

![](/api/attachments/AJKWE9QK/fulltext/images/98d94028b8afca4810b633fc0be45f257547914085fee4faa13929c115a55a6a.jpg)  
Fig. 7. 3-Std net cash flow range.

$\delta _ { t + i + 1 } { \sim } T r i a n g ( 0 . 1 5 , \ 0 . 2 , \ 0 . 2 5 )$ . The net cash flow pattern in this figure is very similar to that in its cash inflow component in Fig. 4 and bears no resemblance to its corresponding outflow pattern in Line 3 of Fig. 6. We conclude that cash inflow risks dominate the netflow risks. As a result, managing the cash inflow risk is the most important task for the manufacturer in order to control its overall cash flow risks.

## 4. Asset-backed securities

As shown in the previous section, the key formula to control net cash flow risks is to reduce cash inflow risks. In this section, we discuss at a macro-level, how the Asset-Backed Security (ABS) market can help reducing the cash inflow risk and in the meanwhile, lowering the CCC. From the simulation result in the previous section, the two go against each other when early collection ratio is a random variable.

We first provide some analytical results comparing the cash inflow risks generated from the constant early collection case and the $\gamma _ { t + i } { \sim } U ( 0 . 1 )$ case. A similar comparison was made earlier along with two other distributions (See Fig. 3). However, the comparison in Fig. 3 is based on the sales of an individual firm, which may or may not be able to meet all market demands. The comparison in this section considers the whole security market where ABS originators acquire AR from more than one source. Let's consider the same AR(1) random variable, $D _ { t + i } ,$ as the total accounts receivable available in the market with the same credit terms from all targeted vendors. The overall cash inflow from these vendors can be written as

$$
\begin{array}{c} \mathrm{IM} _ {t + i} = (1 - c _ {r}) R _ {t + i} + (D _ {t + i - r} - R _ {t + i - r + 1}) \\ = (1 - c _ {r}) \gamma_ {t + i} D _ {t + i - 1} \\ \quad + (1 - \gamma_ {t + i - r + 1}) D _ {t + i - r}, i = 1, 2, \ldots \end{array}\tag{6}
$$

Note that Eq. (6) is the same as Eq. (2) except that we replace the sales variable $S _ { t + i }$ with the demand variable $D _ { t + i }$ because the financial market can meet its demands within a negligible lead time. In this case, the originators bought a portion of the accounts receivable $\gamma _ { t + i } D _ { t + i - 1 }$ at the price of $( 1 - c _ { r } ) \gamma _ { t + i } D _ { t + i - 1 }$ . Here, $c _ { r }$ is the discount factor for ABS and its value is in general lower than the trade discount the manufacturers offer to their customers [20]. At the maturity of those purchased AR, the customers pay $\gamma _ { t + i } D _ { t + i - 1 }$ directly to the originators and $( 1 - \gamma _ { t + i } ) D _ { t + i - 1 }$ to the manufacturers. As a result, the benefits of ABS include: (i) It costs the manufacturers less to shorten the days in receivables through ABS than offering trade discounts. (ii) If the originators constantly purchase a fixed portion of AR, it can lower the manufacturers' cash inflow risks. (ii) The practice does not have any negative cash outflow impact on the customer side.

The following Lemmas provide some analytical results for the two specific scenarios under consideration which then lead to the derivation of the best ABS policy. Some asymptotic behavior similar to that in Lemma 2.1 is given. In all mathematical functions that follow, a summation term with the form, $\Sigma _ { i = e } ^ { f } ,$ vanishes if $e { > } f .$

Because $\gamma _ { t + i }$ and $D _ { t + i - 1 }$ are independent random variables, we need to know the distribution function of the product of the two random variables for analytical purposes. There are approaches to obtain the distribution functions of the product of two or more continuous random variables (see for example, [25,7,19]). However, some of them only apply to random variables with specific distributions and others use numerical approximations. In general, it is not straight forward to obtain basic statistics in closed forms for the product of two or more independent random variables. Hence, among the four distributions applied to $\gamma _ { t + i }$ in Section 3, we only provide analytical results for the two extreme cases. The following Lemma gives the expected values and variances of the early receipts for the two extreme cases, representing the scenarios of complete knowledge (constant γ) and lack of knowledge (uniformly distributed $\gamma )$ about the early collection pattern.

Lemma 4.1. When $\gamma _ { t + i } f o l l o u$ s a uniform distribution or is a constant, for $i = 1 , 2 , . . . ,$ the early collection portion $R _ { t + i } { = } \gamma _ { t + i } D _ { t + i - 1 }$ has the following properties.

$$
\begin{array}{l l} E [ R _ {t + i} ] & = \frac {1}{2} \mu_ {t + i - 1}, \quad \gamma_ {t + i} \sim U (0, 1) \\ & = \gamma \mu_ {t + i - 1}, \quad \gamma_ {t + i} = \gamma , 0 <   \gamma <   1 \end{array}\tag{7}
$$

$$
\begin{array}{l} \text { Var } [ R _ {t + i} ] = \mu_ {t + i - 1} ^ {2} / 1 2 + \sigma_ {t + i - 1} ^ {2} / 3, \quad \gamma_ {t + i} \sim U (0, 1) \\ = \gamma^ {2} \sigma_ {t + i - 1} ^ {2}, \qquad \qquad \gamma_ {t + i} = \gamma , 0 <   \gamma <   1 \end{array}\tag{8}
$$

The following table lists the asymptotic behavior of $E / R _ { t + i } ]$ and $\mathrm { V a r } / R _ { t + i } \overline { { \Omega } }$ when $\rho \to 0$ and $\rho \to 1$ for both cases.

<table><tr><td>p→</td><td>γt+I</td><td>E[Rt+i]→</td><td>Var[Rt+i]→</td></tr><tr><td>0</td><td>U(0,1)</td><td>d/2</td><td>d2/12+σ2/3</td></tr><tr><td>1</td><td>U(0,1)</td><td>(id+Dt)/2</td><td>(id+Dt)2/12+(iσ2)/3</td></tr><tr><td>0</td><td>γ</td><td>γd</td><td>γ2σ2</td></tr><tr><td>1</td><td>γ</td><td>γ(id+Dt)</td><td>iγ2σ2</td></tr></table>

Proof. See Appendix A.

From Lemma 2.1 and Eq. (8) of Lemma 4.1, when $\gamma _ { t + i }$ is a constant γ, the variance for $R _ { t + i }$ is much smaller than when $\gamma _ { t + i }$ follows a uniform distribution, $U ( 0 , 1 )$ , because we assume σ is much smaller than $d ,$ which leads to $\gamma ^ { 2 } \sigma _ { t + i - 1 } ^ { 2 } \ll \mu _ { t + i - 1 } ^ { 2 } / 1 2 + \sigma _ { t + i - 1 } ^ { 2 } / 3$

Lemma 4.2. When $\gamma _ { t + i } { \sim } U ( 0 , 1 )$ , the expected cash inflow at time t + i is

$$
E [ \mathrm{IM} _ {t + i} ] = \frac {1}{2} (1 - c _ {r}) \mu_ {t + i - 1} + \frac {1}{2} \mu_ {t + i - r}\tag{9}
$$

and the variance is

$$
\begin{array}{c} \operatorname{Var} [ \operatorname{IM} _ {t + i} ] = (1 - c _ {r}) ^ {2} \operatorname{Var} [ R _ {t + i} ] + \operatorname{Var} [ R _ {t + i - r + 1} ] \\ + \frac {(1 - c _ {r})}{2} \rho^ {r - 1} \sigma_ {t + i - r} ^ {2} \end{array}
$$

where the values of $\operatorname { V a r } [ R _ { t + i - r } ]$ and $\mathrm { V a r } [ R _ { t + i } ]$ can be found from Lemma 4.1

Proof. See Appendix A.

Lemma 4.3. When $\gamma _ { t + i } { = } \gamma , ~ 0 { \leq } \gamma { \leq } 1$ , the expected cash inflow at time $t { + } i$ is

$$
E [ \mathrm{IM} _ {t + i} ] = \gamma (1 - c _ {r}) \mu_ {t + i - 1} + (1 - \gamma) \mu_ {t + i - r}\tag{10}
$$

and the variance is

$$
\begin{array}{c} \operatorname{Var} [ \operatorname{IM} _ {t + i} ] = \gamma^ {2} (1 - c _ {r}) ^ {2} \sigma_ {t + i - 1} ^ {2} \\ \qquad + (1 - \gamma) ^ {2} \sigma_ {t + i - r} ^ {2} \\ \qquad + 2 \gamma (1 - \gamma) (1 - c _ {r}) \rho^ {r - 1} \sigma_ {t + i - r} ^ {2} \end{array}
$$

Proof. See Appendix A.

<sub>ð</sub><sup>11</sup><sub>Þ</sub>

As we learned that applying a constant early collection rate is the best way to achieve some early collection (lowering CCC) without boosting cash inflow risks, the following lemma establishes the best ABS policy in terms of the early collection rate.

Lemma 4.4. Let γ¯ be the best early collection ratio to minimize the cash inflow risk to the manufacturers.

$$
\begin{array}{l}(1) \overline {{\gamma}} = \frac {1}{1 + (1 - c _ {r}) ^ {2}} w h e n \rho \rightarrow 0.\\(2) \overline {{\gamma}} \rightarrow 0 w h e n \rho \rightarrow 1\end{array}
$$

(3) $H \rho$ is not very close to 1, say $\rho { < } 0 . 9 ,$ , the best policy for $\rho \to 0$ produces good results.

Proof. See Appendix A.

According to Lemma 4.4, the best securitization policy under most circumstances is to set γ close to $\frac { 1 } { 2 }$ because $c _ { r }$ is usually very small (less than 2%). The only exception is when demands between successive periods are highly dependent $( \rho \to 1 )$ ). Under such circumstances, the best policy to minimize cash inflow risks is to keep all AR $( \gamma = 0 )$ which reduces $\mathrm { V a r } [ \mathrm { I M } _ { t + i } ]$ to $\sigma _ { t + i - r } ^ { 2 } { \stackrel { - } { \to } } ( i - r ) \sigma ^ { 2 }$ according to (11) and Lemma 2.1.

![](/api/attachments/AJKWE9QK/fulltext/images/f6c78e95f8b66307d03f959e64f78945be706b7f3776a66ea170f813a1b064d8.jpg)  
Fig. 8. Risks of analytical demands and simulated sales.

It is more complicated to establish similar analytical results for individual manufacturers based on their sales because the forecast errors and inventory factors prohibit direct application of Lemma 2.1 on the sales variable, $S _ { t + i }$ . However, the cash inflow risk under demand and sales behave similar to each other as observed in Fig. 8. In the figure, the lines std(S[U(0,1)]) and std(S[0.5]) depict the same simulated cash inflow risks for the uniform distribution and constant $\gamma { = } 0 . 5$ cases in Fig. 3 respectively based on $S _ { t + i } .$ The two lines $\mathrm { D } [ \mathrm { U } ( 0 , 1 ) ]$ and D[0.5] are obtained based on $D _ { t + i }$ from the analytical result in Lemmas 4.1, 4.2, and 4.3 using the same parameters. The two demand based lines are very close to the two sales based lines due to the fact that $\sigma \ll d$ and $\mathrm { S } \mathrm { S } = 3 \sigma$ . As a result, we expect the same policy to benefit individual vendors in a similar manner.

## 5. Conclusion

This study provides an insightful look at supply chain cash flow risks using a simple supply chain configuration and an AR(1) demand series. It describes the behavior of cash flow risks (standard deviations) with respect to trade terms and processing lead time related factors. Although the model is overly simplified, it clearly explains the reasons why it is difficult to balance between aggressively pursuing lower CCC and tightly controlling cash flow risks, especially for organizations with limited cash reserves. Under the same analytical framework, further simulation experiments can be extended to incorporate more sophisticated demand forecasting models ([13]) and additional supply chain risk factors ([2]).

Asset-backed Securities (ABS) have been maturely developed on financial instruments such as mortgages and credit card loans. However, only a small portion of accounts receivable is financed through ABS, resulting in higher financing costs to support supply chain operations ([12,20]). As seen in this analysis, ABS has the potential of lowering both the CCC and cash flow risks. The cost of securitization can be significantly reduced due to the development of information technologies used by supply chain members to share the physical flow information. Moreover, timely and accurate supply chain information can improve the credit ratings of the resulting securities, leading to a lower financial cost.

There are several directions for future research based on the result of this study. First, the result can be used in a cash forecast and budget control system to incorporate the risk factors into an optimization model for planning future cash related activities. Second, the causal relationship between the physical flow and cash flow may be used as a tool in a fraud prevention/detection system. Third, one may also study the selection and packaging process of ABS. On the information technology side, further study is needed to identify the best practice to integrate/standardize IT infrastructure between ABS originators and supply chain members to facilitate the securitization process.

## Appendix A. Proofs of Lemmas

## Lemma 2.1. Proof

The following proof is based on the fact that

$$
\begin{array}{c} D _ {t + i} = \big (d + \rho d + \rho^ {2} d + \dots + \rho^ {i - 1} d \big) + \rho^ {i} D _ {t} \\ \qquad + \big (\rho^ {i - 1} \varepsilon_ {t + 1} + \rho^ {i - 2} \varepsilon_ {t + 2} + \dots + \rho^ {0} \varepsilon_ {t + i} \big) \\ = \frac {d (1 - \rho^ {i})}{1 - \rho} + \rho^ {i} D _ {t} + \sum_ {k = 1} ^ {i} \rho^ {i - k} \varepsilon_ {t + k} \end{array}
$$

(1) $\begin{array} { r } { \mu _ { t + 1 } = E \Big [ \frac { d ( 1 - \rho ^ { i } ) } { 1 - \rho } + \rho ^ { i } D _ { t } + \sum _ { k = 1 } ^ { i } \rho ^ { i - k } \varepsilon _ { t + k } \Big ] = \frac { d ( 1 - \rho ^ { i } ) } { 1 - \rho } + } \end{array}$ $\rho ^ { i } D _ { t } = \bar { d } ( 1 + \rho + \rho ^ { 2 } + \cdot \cdot \cdot + \rho ^ { i - 1 } ) \stackrel { - } { + } \rho ^ { i } D _ { t }$ : The result for $\rho \to 0 , \pm 1$ follows from substituting $\rho$ with $0 , \pm 1$

(2) $\begin{array} { r } { \sigma _ { t + i } ^ { 2 } = \mathrm { V a r } \big [ \sum _ { k = 1 } ^ { i } \rho ^ { i - k } \varepsilon _ { t + k } \big ] = \sigma ^ { 2 } \sum _ { k = 1 } ^ { i } \rho ^ { 2 ( i - k ) } = } \end{array}$ $\textstyle { \frac { \sigma ^ { 2 } \left( 1 - \rho ^ { 2 i } \right) } { 1 - \rho ^ { 2 } } } = \sigma ^ { 2 } { \bigl ( } 1 + \rho ^ { 2 } + \rho ^ { 4 } + \cdot \cdot \cdot + \rho ^ { 2 ( i - 1 ) } { \bigr ) }$ : The result for $\rho \to 0 , \pm 1$ follows from substituting $\rho$ with $0 , \pm 1$

(3) $\begin{array} { r } { \mathrm { C o v } \big [ D _ { t + i } , D _ { t + j } \big ] = E \big [ ( D _ { t + i } - \mu _ { t + i } ) \big ( D _ { t + j } - \mu _ { t + j } \big ) \big ] = E \big [ \sum _ { k = 1 } ^ { i } } \end{array}$ $\begin{array} { r } { \rho ^ { i - \bar { k } } \varepsilon _ { t + k } \sum _ { k = 1 } ^ { j } \rho ^ { j - k } \varepsilon _ { t + k } ] = E \big [ \rho ^ { j - i } \sum _ { k = 1 } ^ { i } \rho ^ { 2 ( i - \bar { k } ) } } \end{array}$ $\displaystyle \varepsilon _ { t + i } ^ { 2 } ] = \rho ^ { j - i } \sigma _ { t + i } ^ { 2 }$ since $E [ \mathfrak { E } _ { t + \nu } \mathfrak { E } _ { t + w } ] = 0$ for v≠w. The result for $\rho \to 0 , \pm 1$ follows from substituting $\rho$ with $0 , \pm 1$ and $\sigma _ { t + 1 } ^ { 2 }$ by $\sigma ^ { 2 } ( 1 + \rho ^ { 2 } + \rho ^ { 4 } + \cdots + \rho ^ { 2 ( i - 1 ) } )$ □

## Lemma 4.1. Proof

The proof for the case when $\gamma _ { t + i }$ is a constant is straight forward. We only show the proof when $\gamma _ { t + i } { \sim } U ( 0 , 1 )$

$\begin{array} { r } { E [ R _ { t + i } ] = E \bigl [ \gamma _ { t + i } \bigr ] E [ D _ { t + i - 1 } ] = \frac 1 2 \mu _ { t + i - 1 } } \end{array}$ because $E [ \gamma _ { t + i } ] =$ 1 / 2.

$$
\begin{array}{l} \operatorname{Var} [ R _ {t + i} ] = E \big [ \gamma_ {t + i} ^ {2} D _ {t + i - 1} ^ {2} \big ] - E \big [ \gamma_ {t + i} \big ] ^ {2} E [ D _ {t + i - 1} ] ^ {2} \\ \qquad = E \big [ \gamma_ {t + i} ^ {2} \big ] E \big [ D _ {t + i - 1} ^ {2} \big ] - E \big [ \gamma_ {t + i} \big ] ^ {2} E [ D _ {t + i - 1} ] ^ {2} \\ \qquad = \frac {1}{3} \left(\sigma_ {t + i - 1} ^ {2} + \mu_ {t + i - 1} ^ {2}\right) - \frac {1}{4} \mu_ {t + i - 1} ^ {2} \\ \qquad = \mu_ {t + i - 1} ^ {2} / 1 2 + \sigma_ {t + i - 1} ^ {2} / 3. \end{array}
$$

The values of $E [ R _ { t + i } ]$ and $\mathrm { V a r } [ R _ { t + i } ]$ when $\rho \to 0$ and 1 are obtained from applying the result in Lemma 2.1 to (7) and (8).

## Lemma 4.2. Proof

(1) $E [ I M _ { t + i } ] = E [ ( 1 - c _ { r } ) R _ { t + i } + D _ { t + i - r } - R _ { t + i - r + 1 } ] = ( 1 - c _ { r } )$ $E [ R _ { t + i } ] + E [ D _ { t + i - r } ] - E [ R _ { t + i - r + 1 } ] . \ E [ D _ { t + i - r } ] -$ $\begin{array} { r } { E [ R _ { t + i - r + 1 } ] = \frac { 1 } { 2 } E [ D _ { t + i - r } ] } \end{array}$ and the last term $\begin{array} { r } { E [ R _ { t + i } ] = \frac { 1 } { 2 } \mu _ { t + i - 1 } } \end{array}$ from Lemma 4.1. Thus, $\begin{array} { r } { E ( I M _ { t + i } ) \stackrel { - } { = } \frac { 1 } { 2 } ( 1 - c _ { r } ) \mu _ { t + i - 1 } + \frac { 1 } { 2 } \mu _ { t + i - r } . } \end{array}$

(2) Let $\widetilde { \gamma } _ { t + i - r } { = } 1 - \gamma _ { t + i - r }$ Since $\tilde { \gamma } _ { t + i - r }$ is also distributed uniformly between 0 and 1, Var[ $I M _ { t + i } ] =$ $\mathrm { V a r } [ ( 1 - c _ { r } ) \gamma _ { t + i } D _ { t + i - 1 } + ( 1 - \gamma _ { t + i - r + 1 } ) D _ { t + i - r } ] =$ $( 1 - c _ { r } ) ^ { 2 } \mathrm { V a r } [ R _ { t + i } ] + \mathrm { V a r } [ R _ { t + i - r + 1 } ] + 2 ( 1 - c _ { r } ) \mathrm { C o v }$ $\left[ R _ { t + i } , \ R _ { t + i - r + 1 } \right]$ where Cov $[ R _ { t + i } , R _ { t + 1 - r + 1 } ] =$ $\begin{array} { r } { E [ \gamma _ { t + i } \tilde { \gamma } _ { t + i - r + 1 } D _ { t + i - 1 } D _ { t + i - r } ] - \frac { 1 } { 4 } E [ D _ { t + i - 1 } ] E [ D _ { t + i - r } ] = } \end{array}$ $\begin{array} { r } { \frac { 1 } { 4 } \left( E [ D _ { t + i - 1 } D _ { t + i - r } ] - E [ D _ { t + i - 1 } ] E [ D _ { t + i - r } ] \right) = \frac { 1 } { 4 } \mathrm { C o v } [ D _ { t + i - 1 } , } \end{array}$ $\begin{array} { r } { D _ { t + i - r } ] = \frac { 1 } { 4 } \rho ^ { r - 1 } \sigma _ { t + i - r } ^ { 2 } } \end{array}$ from Lemma 2.1 (3).

## Lemma 4.3. Proof

The proof is similar to that of Lemma 4.2 except that γ is a constant instead of a random variable. □

## Lemma 4.4. Proof

The proof focuses on the period $t + i , \ i > r$ because when $1 \leq i \leq r ,$ the result is affected by the realized portion of the cash inflow $D _ { t + i - r }$ in Eq. (6). The first order condition of (11) is

$$
\begin{array}{c} \frac {d}{d \gamma} \operatorname{Var} [ \mathrm{IM} _ {t + i} ] = 2 \gamma (1 - c _ {r}) ^ {2} \sigma_ {t + i - 1} ^ {2} - 2 (1 - \gamma) \sigma_ {t + i - r} ^ {2} \\ + 2 (1 - 2 \gamma) (1 - c _ {r}) \rho^ {r - 1} \sigma_ {t + i - r} ^ {2} = 0 \end{array}
$$

and the second order condition is

$$
\begin{array}{c} \frac {d ^ {2}}{d \gamma^ {2}} \operatorname{Var} [ \mathrm{IM} _ {t + i} ] = 2 (1 - c _ {r}) ^ {2} \sigma_ {t + i - 1} ^ {2} + 2 \sigma_ {t + i - r} ^ {2} \\ - 4 (1 - c _ {r}) \rho^ {r - 1} \sigma_ {t + i - r} ^ {2} > 0 \end{array}
$$

(1) According to Lemma 2.1, when $\rho {  } 0 , { \sigma _ { t + k } ^ { 2 } } { = } \sigma ^ { 2 }$ for $k { = } 1 , 2 , . . .$ and the first order condition reduces to $\sigma ^ { 2 } [ 2 \gamma ( 1 - c _ { r } ) ^ { 2 } - 2 ( 1 - \gamma ) ] { = } 0$ which implies that $\begin{array} { r } { \overline { { \gamma } } = \frac { 1 } { 1 + \left( 1 - c _ { r } \right) ^ { 2 } } } \end{array}$ . In addition, the second order condition, $2 \sigma ^ { 2 } [ ( 1 - c _ { r } ) ^ { 2 } + 1 ] > 0$ always holds since $c _ { r } \ll 1$

(2) When $\stackrel { \cdot } { \rho }  0 , \sigma _ { t + k } ^ { 2 } = k \sigma ^ { 2 }$ for $k { = } 1 , 2 , . . .$ and the first order condition can be written as $\overline { { \boldsymbol { \gamma } } } _ { t + i } =$ $\frac { c _ { r } \lfloor \iota - r \rfloor } { \left( 1 - c _ { r } \right) ^ { 2 } \left( i - 1 \right) - \left( i - r \right) \left( 1 - 2 c _ { r } \right) }$ . The second order condition $c _ { r } ^ { 2 } ( i - 1 ) + ( r - 1 ) ( 1 - 2 c _ { r } ) > 0$ always holds because $i > r \geq 1$ and $c _ { r } \ll 1 . \overline { { \gamma } } _ { t + i }$ is a small number dependent on i and produces a $\mathrm { V a r } [ \mathrm { I M } _ { t + i } ]$ slightly smaller than $i \sigma ^ { 2 }$ for all $i { > } r .$ Choosing a common $\overline { { \gamma } } = 0$ across all $i \mathbf { \ ' } _ { \mathbf { S } }$ generates $\mathrm { V a r } [ \mathbf { I M } _ { t + i } ] { = } i \sigma ^ { 2 }$ which is very close to the optimal result

(3) In general, $\begin{array} { r } { \dot { \sigma } _ { t + i } ^ { 2 } = \frac { \sigma ^ { 2 } \left( 1 - \rho ^ { 2 i } \right) } { 1 - \rho ^ { 2 } } } \end{array}$ from Lemma 2.1. The value of $\rho ^ { 2 i }$ declines exponentially as i increases. Thus, unless $\rho$ is very close to 1, the risk behavior is closer to that of $\rho \to 0$ than $\rho \to 1$

## References

[1] K.E. Bourland, S.G. Powell, D.F. Pyke, Exploiting timely demand information to reduce inventories, European Journal of Operational Research 92 (1996) 239–253.

[2] D.C. Chatfield, T.P. Harrision, J.C. Hayya, Sisco: an objectoriented supply chain simulation system, Decision Support Systems 42 (1) (2006) 422–434.

[3] F. Chen, Z. Drezner, J.K. Ryan, D. Simchi-Levi, Quantifying the bullwhip effect in a simple supply chain: the impact of forecasting, lead times, and information, Management Science 46 (3) (2000) 436–443.

[4] L.M. Ellram, B. Liu, The financial impact of supply management, Supply Chain Management Review (November-December 2002) 30–37.

[5] M.T. Farris II, P.D. Hutchison, Cash-to-cash: the new supply chain management metric, International Journal of Physica Distribution & Logistics Management 32 (4) (May 2002) 288–298.

[6] S. Gavirneni, R. Kapuscinski, S. Tayur, Value of information in capacitated supply chain, Management Science 45 (1) (January 1999) 16–24.

[7] A.G. Glen, L.M. Leemis, J.H. Drew, Computing the distribution of the product of two continuous random variables, Computational Statistics & Data Analysis 44 (1) (January 2004) 451–464.

[8] Z. Guo, F. Fang, A.B. Whinston, Supply chain information system sharing in a macro prediction market, Decision Support Systems 42 (3) (2006) 1944–1958.

[9] W. Holland, M. Sodhi, Quantifying the effect of batch size and order errors on the bullwhip effect using simulation, International Journal of Logistics 7 (3) (2004) 251–261.

[10] M.L. Jose, C. Lancaster, J.L. Stevens, Corporate returns and cash conversion cycles, Journal of Economics and Finance 20 (1) (Spring 1996) 33–46.

[11] J.A. Kahn, Inventories and the volatility of production, American Economics Review 77 (4) (1987) 667–679.

[12] A. Katz, Mid-sized companies: breaking the funding barrier through account receivables financing, Monitor: Specialty Lending Supplement (July/August 2002) 1–3.

[13] R.J. Kuo, K.C. Xue, A decision support system for sales forecasting through fuzzy neural networks with asymmetric fuzzy weights, Decision Support Systems 24 (2) (1998) 105–126.

[14] H.L. Lee, V. Padmanabhan, S. Whang, The bullwhip effect in supply chains, Sloan Management Review 19 (Spring 1997) 93–102.

[15] H.L. Lee, K.C. So, C. Tang, The value of information sharing in a two-level supply chain, Management Science 46 (5) (2000) 626–643.

[16] S. Li, B. Lin, Accessing information sharing and information quality in supply chain management, Decision Support Systems 42 (3) (2006) 1641–1656.

[17] R. Metters, Quantifying the bullwhip effect in supply chains, Journal of Operations Management 15 (2) (1997) 89–110.

[18] R.M. Monczka, K.J. Petersen, R.B. Handfield, G.L. Ragatz, Success factors in strategic supplier alliances: the buying company perspective, Decision Sciences 29 (3) (1998) 553–577.

[19] S. Nadarajah, On the product and ratio of laplace and bessel random variables, Journal of Applied Mathematics (4) (2005) 393–402.

[20] P. Palmieri, J. Afrik, Combining logistics wth financing for enhanced profitability, ASCET, 1, April 1999 http://www.ascet. com/documents.asp?grID=197&d ID=213#.

[21] S. Raghunathan, Information sharing in a supply chain: A note on its value when demand is nonstationary, Management Science 47 (4) (2001) 605–610.

[22] W. Schaff, Dell succeeds where competitors lag, Information Week (February 2003) 80.

[23] J.-B. Sheu, A multi-layer demand-responsive logistics control methodology for alleviating the bullwhip effect of supply chains, European Journal of Operational Research 161 (3) (2005) 797–811.

[24] R.G. Sloan, Do stock prices fully reflect information in accruals and cash flows about future earnings? The Accounting Review 71 (3) (1996) 289–315.

[25] M.D. Springer, W.E. Thompson, The distribution of products of beta, gamma, and gaussian random variables, SIAM Journal of Applied Mathematics 18 (4) (1970) 721–737.

[26] J.D. Wisner, G.K. Leong, K.-C. Tan, Principles of Supply Chain Management–A Balanced Approach, 2005, p. 442, South-Western, Mason, Ohio.

Chih-Yang Tsai is Associate Dean of the School of Business at State University of New York at New Paltz. He received his PhD in Operations Research from Stern School of Business, New York University and MBA from Tatung University, Taiwan. His current research interests focus on modeling the interrelationship between supply chain and Accounting/Finance Systems for planning and controlling purposes. He has published in journals such as Discrete Mathematics, Interfaces, Mathematical Programming, Naval Research Logistics, and Omega.
