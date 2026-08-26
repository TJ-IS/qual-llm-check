---
otero_id: 26433
otero_key: "GS6M65FA"
title: "Beyond EDI: Impact of Continuous Replenishment Program (CRP) Between a Manufacturer and Its Retailers"
authors: "Srinivasan Raghunathan; Arthur B. Yeh"
year: "2001"
journal: "Information Systems Research"
doi: "10.1287/isre.12.4.406.9701"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## 6SR

![](/api/attachments/GS6M65FA/fulltext/images/ae65bbfbfba229ab4df2119a5502abe6004604e4bbf88ff0be5702c56b2cb8df.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Beyond EDI: Impact of Continuous Replenishment Program (CRP) Between a Manufacturer and Its Retailers

Srinivasan Raghunathan, Arthur B. Yeh,

To cite this article:

Srinivasan Raghunathan, Arthur B. Yeh, (2001) Beyond EDI: Impact of Continuous Replenishment Program (CRP) Between a Manufacturer and Its Retailers. Information Systems Research 12(4):406-419. http://dx.doi.org/10.1287/isre.12.4.406.9701

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2001 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/GS6M65FA/fulltext/images/86f45867a9d0362b185be829303ea78c9c0cd36240eb73318d082600fd6e536a.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Beyond EDI: Impact of Continuous Replenishment Program (CRP) Between a Manufacturer and Its Retailers

Srinivasan Raghunathan • Arthur B. Yeh

Management Science and Information Systems Department, School of Management, University of Texas at Dallas, Richardson, Texas 75083

Applied Statistics and Operations Research Department, Bowling Green State University, Bowling Green, Ohio 43403 sraghu@utdallas.edu • yau yeh@yahoo.com

lectronic data interchange (EDI), used traditionally to exchange business documents, has continuous replenishment program (CRP). The key characteristics of CRP are the sharing of real-time inventory data by retailers with manufacturers and continuous replenishment of retailer inventory by manufacturers. Prior research on EDI has focused on the transaction efficiency of EDI. We analyze the impact of information sharing and continuous replenishment in the CRP context and study the factors that affect the value of CRP. The study quantifies the value derived from CRP and the optimal number of retailers a manufacturer should partner with.

(Electronic Data Interchange; Continuous Replenishment Program; Supply Chain Partnerships; Interorganizational Systems; IT Justification)

## 1. Introduction

Manufacturers and retailers have been reengineering supply chains using information technology (IT) such as point-of-sale (POS) systems and electronic data interchange (EDI). While EDI has been used traditionally to exchange business documents between trading partners, its capabilities have been extended recently to facilitate collaborative business processes across firms. Continuous replenishment program (CRP) is one such IT-enabled reengineering effort. The key features of CRP are as follows: (1) Retailers provide the manufacturer with real time access to their inventory positions (information sharing). (2) Based on this information, the manufacturer replenishes retailer inventory (VMI: vendor managed inventory). And, (3) products are sold to retailers at an everyday low price (EDLP). In CRP, retailer orders are essentially eliminated because manufacturers determine quantities to ship to retailers based on observed retail sales.

CRP is a way to cope with demand uncertainty because it coordinates the supply chain players to work with common forecasts. Theory of coordination, or “coordination science” often focuses on the value of information sharing in achieving intra-inter-firm coordination (Malone and Crowston 1994). However, information sharing is only one aspect of coordination; business processes are also redesigned along with information sharing. CRP restructures the supply-chain ordering process in two fundamental ways. First, it requires the retailers to share inventory level, which is traditionally viewed as sensitive and secret information. Second, under CRP, the retailer inventory management is performed by the manufacturer and not by the retailer. With the exception of a few guidelines from anecdotal experiences, the value derived from such process redesigns is unclear.

It is well known that traditional EDI reduces transaction costs and errors (Mukhopadhyay et al. 1995, Wang and Seidmann 1995, Srinivasan et al. 1994, Riggins and Mukhopadhyay 1994). In theory, it would seem that information sharing alone, which could be implemented by traditional EDI without requiring VMI, could provide significant benefits to the supply chain. Although the benefits of EDI for ordering were widely publicized, few firms in the retail industry had experienced significant savings from using EDI to automate the existing ordering process (Clark and Hammond 1997). Many authors have also noted that EDI must involve changes in business processes to realize savings enabled by the EDI innovation (Riggins and Mukhopadhyay 1994, Venkatraman 1994). Case studies of CRP implementation speculated that for continuous replenishment systems to work effectively, demand must either be stable or reasonably predictable (Clark and Hammond 1997). Products that change frequently such as seasonal goods may not be appropriate for the CRP approach. Retail grocery product demands are relatively stable and are effectively managed by CRP (Clark 1994b). Prior research provides little insights into questions such as the value of information sharing relative to that of process redesign enabled by information sharing, and the impact of demand characteristics on the effectiveness of CRP. Toward that end, the goals of this paper are to (i) analytically quantify the value of real-time information sharing and continuous replenishment, (ii) investigate the impact of demand parameters on the value, and (iii) to investigate the optimal CRP network size.

We perform our analysis within the context of a twolevel supply chain as discussed in Lee et al. (2000), hereafter referred to as LST. However, we generalize their model to include N retailers with crosscorrelations of demand errors and continuous replenishment. When there is no CRP, the retailers communicate only their orders to the manufacturer. Under CRP, the manufacturer has real-time access to participant retailers’ inventory levels, and the manufacturer replenishes the inventory for each participant retailer. Our results are consistent with the earlier finding that

CRP reduces the expected inventory holding costs of both the manufacturer and retailer participants. We obtain the following additional insights:

(1) The value of CRP to the manufacturer is higher when more retailers participate in CRP; the demand error has a higher variance; the correlations among demand errors across periods at a single retailer (serial correlation) and correlations among demand errors across retailers during a single period (cross correlation) are higher.

(2) The value of CRP to participants, both manufacturer and retailers, is higher when retailers with larger demands participate in CRP. Additionally, the value to the manufacturer is higher when retailers whose demand errors are correlated more with those of other retailers participate. Thus, it is beneficial for the manufacturer to recruit larger retailers and those whose demand errors are highly correlated with those of other retailers first. Similarly, larger retailers have higher incentives to join CRP.

(3) The value of continuous replenishment relative to that of information sharing increases as the expected demand increases and/or the demand variance decreases. Thus, VMI is likely to be more valuable for mature products with stable and large demand, and information sharing is likely to be more valuable for relatively new products with high demand variance.

(4) When retailers are identical, the marginal value of CRP is decreasing (increasing) in the number of participants when the cross-correlation is sufficiently high (low). Demand information from retailers behaves as substitutes and complements in the high and low correlation environment, respectively. The optimal size of the CRP network depends on the cross-correlation. When demands across retailers are independent, it is optimal to include every or no retailer in the network. On the contrary, when demands across retailers are highly correlated, the manufacturer may find it optimal to have a subset of retailers in the CRP network, depending on the cost and demand parameters. The size of this set decreases as the CRP implementation cost increases.

The rest of the paper has the following structure. Section 2 reviews the prior literature on the impact of EDI and related systems on supply chains. We present our model of CRP in §3. We derive the principal analytical results about the value generated by CRP in §4. We analyze the impact of CRP on the supply-chain structure and retailer-recruitment policy in §5. Section 6 provides managerial implications of the results. Discussion of our model and extensions are presented in §7.

## 2. Literature Review

The bulk of prior published research has focused on the benefits of traditional EDI. The key finding was that EDI benefits the buyer primarily by reducing shipment discrepancy, inventory, and ordering costs (Srinivasan et al. 1994, Mukhopadhyay et al. 1995). Questions have been raised about whether EDI adopters, for whom dominating buyers often mandate EDI, benefit from EDI (Riggins and Mukhopadhyay 1994). Wang and Seidmann (1995) showed the positive externalities of EDI on the buyer and negative externalities on the nonparticipant suppliers. Clark (1994b) observed that some grocery chains that were early EDI adopters have terminated its use because the perceived benefits were less than the cost of using EDI. This led researchers to investigate the role of process redesign, such as CRP, that takes advantage of EDI capabilities. Research on CRP is recent. Pioneering empirical research has been carried out by Clark and others in a series of case studies of the grocery industry (Clark 1994a, Hammond 1995, Clark and Hammond 1997, Lee et al. 1999). The primary result of this stream of research is that channel transformation, defined as the combination of process and technological innovation, provides significantly greater performance improvements than either technological innovations or process redesign changes implemented independently. Cachon and Fisher (1997) showed, using a simulation model, the positive impact of CRP on the Campbell’s Soup Company. All of the above research on CRP has investigated the impact of CRP using empirical data from one manufacturer, in this case Campbell’s Soup, and its retailers. We use an analytical model to quantify the value of CRP. Consequently, we are able to derive normative implications of CRP in a general context.

Analytical modeling of the CRP innovation is limited and has focused primarily on channel coordination through information sharing. These studies discuss how a manufacturer can elicit information from retailers through inventory, leadtime, and shortage allocation policies (Bourland et al. 1996, Gavirneni et al. 1996, Aviv and Federgruen 1998, Moinzadeh and Bassok 1998, Cachon and Fisher 1998). In these studies, the benefit of information sharing to the manufacturer comes primarily from the manufacturer’s ability to forecast more accurately the size of retailer’s future orders and/or the actual timing of the future order placement. LST studied how information sharing improves a manufacturer’s ordering decision in a two-level supply chain with nonstationary demand at the retailer end. They also analyzed the effects of manufacturer and retailer lead times on the value of information sharing. Gavirneni et al. (1996) and Aviv and Federgruen (1998) assume that the manufacturer’s capacity might be restricted. Analytical models in this stream of research have generally used a model consisting of a single retailer or multiple independent retailers. We model a more general scenario in which the demands across the retailers could be correlated. Hence, we are able to investigate the impact of crossdemand correlations on the value of and incentives of the players to participate in CRP.

Other research related to information sharing in supply chains include, that of Lee et al. (1997), who determined that sharing information would reduce the manufacturer’s demand variance and the “bullwhip” effect in supply chains. However, they did not derive the actual benefit. Anand and Mendelson (1997) studied the interaction of information sharing and decision rights, i.e., should the retailers or the central agent make decisions in a multiple retailer context.

## 3. The Model

Our model is an N-retailer version of LST’s model with cross-correlations of demands at retailers. Following LST, in the traditional system, the players employ a periodic review policy in which at the end of every period each site reviews its inventory and places an order for meeting the demand during the next period. The manufacturer receives only the retailer order and does not observe the actual retailer demand during any time period. In the CRP system, the retailer provides the manufacturer real-time access to its inventory and, hence, the actual retailer demand, and the manufacturer replenishes the inventory continuously.<sup>1</sup> In essence, under CRP, the manufacturer’s problem is changed to replenishing the known sold inventory from that of forecasting the next period’s retailer order. As far as the retailer is concerned, the retailer has to keep very little stock under CRP because inventory is replenished continuously in contrast to storing an entire period’s stock at the beginning of the period in the traditional system. Now we discuss the analytical model.

External demand for a single item occurs at the retailers, where the underlying demand process faced by a retailer is a simple AR(1) process, which is common knowledge. Let $D _ { t } = ( D _ { 1 t } , D _ { 2 t } , . . . D _ { N t } ) ^ { \mathrm { T } }$ be the demand vector of AR(1) demand during Period t at retailers.<sup>2</sup> Assume

$$
D _ {t} = d + \Gamma D _ {t - 1} + E _ {1},\tag{3.1}
$$

where

$$
\begin{array}{r l} & {d = d _ {1}, d _ {2}, \ldots , d _ {N}) ^ {T}} \\ & {\Gamma = \left( \begin{array}{l l l} \rho_ {1} & & 0 \\ & \rho_ {2} & \\ 0 & & \rho_ {N} \end{array} \right) _ {N \times N}} \\ & {E _ {\mathrm{t}} = \varepsilon_ {\mathrm{1t}}, \ldots , \varepsilon_ {\mathrm{2t}}, \ldots , \varepsilon_ {\mathrm{Nt}}) ^ {\mathrm{T}}.} \end{array}
$$

We also assume that $d _ { i } > 0 , - 1 < \mathsf { p } _ { i } < 1 \forall i = 1$ J $2 , \ldots , N ,$ and the random error $E _ { t }$ for $t = 1 , 2 , \ldots$ . are i.i.d. multivariate normal distributions with mean vector $( 0 , 0 , \ldots , 0 ) ^ { \mathrm { T } }$ and covariance matrix $\Sigma _ { N \times N }$ . We further assume that the Euclidian distance of d, d, is significantly larger than the determinant of $\Sigma ,$ |R|, so that

<sup>1</sup>In practice, transportation delay and cost are likely to prevent instantaneous replenishment. The problem of determining the optimal replenishment rate, $\mathrm { i . e . , }$ the time interval between two consecutive replenishments is isn’t addressed in this paper. When replenishment is continuous, the value represents the maximum benefit that the players can realize. However, we trade off the cost of continuous replenishment against the benefit. See Footnote 4 for the effect of discrete rather than continuous replenishment on the value of CRP. <sup>2</sup>We denote the transpose of matrix M as $M ^ { T }$

the probability of at least one negative demand is negligible (Cramer 1945). Note that C represents the serial correlation coefficient between demands during Periods (t  1) and t for the same retailer, and R represents the variance and cross-correlation matrix of retailer demand errors during any Period t.

The parameter d is known to the manufacturer and retailers. C and $\Sigma _ { N \times N }$ are parameters estimated from available information. However, the actual $D _ { i t }$ during Period t is known only to Retailer i when there is no CRP. The manufacturer receives this information from the retailer if Retailer i participates in CRP.

We assume, for convenience, that the replenishment lead times are zero. At the end of Period $t ,$ after demand $D _ { i t }$ has been realized, Retailer i observes its inventory level and places an order of size $y _ { i t }$ with the manufacturer to replenish its inventory. Excess demand at the retailer is backlogged. If the manufacturer does not have enough stock to fill the orders, then we assume that the manufacturer will meet the shortfall by obtaining units from an “alternative” source, with additional cost representing the penalty cost to this shortfall. Immediately after replenishing the retailer orders, the manufacturer schedules its production to satisfy the retailer demand during the next period.

We assume that no fixed ordering or setup cost is incurred when placing the order or scheduling the production, and that unit inventory holding cost and shortage cost are stationary over time. Let

$$
K   =   \left[ \begin{array}{c c c c} k _ {1} & & & 0 \\ & k _ {2} & & \\ & & . & \\ 0 & & & k _ {N} \end{array} \right],
$$

where $k _ { i }$ denotes the service level requirement (formally the probability of stock out) for Retailer i. Let L denote the service-level requirement for the manufacturer. We assume that the service-level requirements are sufficiently high, and that the shortage is negligible compared to the demand. Let $h = ( h _ { 1 } , h _ { 2 } , \ldots , h _ { N } ) ^ { \top }$ denote the vector of unit holding a cost per period for retailers, and let H denote the unit holding cost per period for the manufacturer.

## 4. Model Analysis

We first develop expressions for the retailer and manufacturer ordering decisions for two cases: (i) the base case of no CRP and (ii) CRP with $n , 1 \leq n \leq N ,$ , retailer participants. Then, we derive the value of CRP by comparing the inventory costs in both cases.

## 4.1. Retailer’s Ordering Decision

Let $\boldsymbol { S } _ { t } = ( s _ { 1 t } , s _ { 2 t } , . . . , s _ { N t } ) ^ { \mathrm { T } }$ and $\boldsymbol { Y } _ { t } = ( y _ { 1 t } , y _ { 2 t } , . . . , y _ { N t } ) ^ { \mathrm { T } }$ represent the retailers’ order-up-to level and order quantity, respectively, for Period t when there is no CRP. At the end of Period $t ,$ retailers place orders $Y _ { t } ,$ where

$$
Y _ {t} = D _ {t} + (S _ {t} - S _ {t - 1}).\tag{4.1}
$$

The $S _ { i t }$ that minimizes the total expected holding and shortage costs in Period $t ~ + ~ 1$ for a service-level requirement of K is

$$
S _ {t} = d + \Gamma D _ {t} + K \sigma ,\tag{4.2}
$$

where $\mathfrak { O } = ( \sqrt { \Sigma _ { 1 1 } } , \sqrt { \Sigma _ { 2 2 } } , \dots , \sqrt { \Sigma _ { N N } } ) ^ { \mathrm { T } }$ (Silver and Petersen 1985).

When there is CRP, the ordering process is eliminated for the participant retailers. The nonparticipant retailers’ optimal ordering decisions are uneffected by CRP because CRP does not affect the retailers’ demand structure.

## 4.2. Manufacturer’s Ordering Decision

Now consider the manufacturer’s ordering decision. We assume, as does LST, that the manufacturer also uses an AR(1) model to forecast retailer orders. After the manufacturer ships the retailer’s orders totaling $\begin{array} { r } { \sum _ { i = 1 } ^ { N } y _ { i t } = 1 ^ { \mathrm { T } } Y _ { t } , } \end{array}$ , where $\mathbf { l } ^ { \mathrm { T } } = ( 1 , 1 , \ldots , 1 ) ^ { \mathrm { T } } ,$ , at the end of Period t, the manufacturer immediately places an order or schedules production to bring its inventory position to an order-up-to level $T _ { t } .$ . From Equations (3.1), (4.1), and (4.2), the manufacturer can deduce that

$$
Y _ {t + 1} = d + \Gamma Y _ {t} + (I + \Gamma) E _ {t + 1} - \Gamma E _ {t},\tag{4.3}
$$

where I is the N-dimensional identity matrix.

Thus, the manufacturer’s anticipated total shipment quantity for Period $t + 1$ is

$$
\sum_ {i = 1} ^ {N} y _ {i t + 1} = 1 ^ {\mathrm{T}} Y _ {t + 1}.\tag{4.4}
$$

To determine the manufacturer’s order-up-to level $T _ { t } ,$ the manufacturer needs to find the distribution of $\textstyle \sum _ { i = 1 } ^ { N } y _ { i t + 1 }$ . The distribution depends on whether the manufacturer knows the realized demand $D _ { t }$

4.2.1. No CRP Scenario. When there is no CRP, the manufacturer receives only the order information $Y _ { t } .$ In this scenario, both $E _ { t + 1 }$ and $E _ { t }$ are considered random vectors by the manufacturer in making its decision. Consequently, $Y _ { t + 1 }$ is distributed as an N-dimensional multivariate normal distribution, $\mathrm { i . e . , ~ } Y _ { t + 1 }$ $\sim M N ( d + \Gamma Y _ { t } , \Sigma ^ { 0 } )$ , where $\Sigma ^ { 0 } = ( \mathrm { I } + \Gamma ) \Sigma ( \mathrm { I } + \Gamma ) ^ { \mathrm { T } } +$ $\Gamma \Sigma \Gamma ^ { \mathrm { T } }$ . Therefore, the manufacturer’s anticipated total shipment for Period $t + 1$ is distributed as $N ( 1 ^ { \mathrm { T } } \left( d \right. +$ $\Gamma \bar { Y _ { t } } ) , 1 ^ { \mathrm { T } } \Sigma ^ { 0 } 1 )$ . Thus, as in (4.2), the manufacturer’s order-up-to level in the absence of CRP, $T _ { t } ^ { 0 }$ for a service-level requirement of L is computed to be

$$
T _ {t} ^ {0} = 1 ^ {\mathrm{T}} (d + \Gamma Y _ {t}) + L (1 ^ {\mathrm{T}} \Sigma^ {0} 1) ^ {1 / 2}.\tag{4.5}
$$

4.2.2. CRP with n $( 1 \leq n \leq N )$ Retailer Participants. Let us assume, for simplicity, that the first n retailers participate in CRP. In other words, rearrange the vector and matrices so that the participating retailers are indexed before the nonparticipants. In this scenario, the manufacturer knows $D _ { i t } ,$ hence, $\varepsilon _ { i t }$ of Retailer $i , i \leq n$ . Now, based on this information, it can update the distributions of $\varepsilon _ { j t }$ for $n + 1 \leq j \leq N .$ . The following property of multivariate normal distribution is useful in our derivation (Anderson 1984).

If $X \sim M N ( \mu , \mathfrak { H } )$ , where l is an N-dimensional mean vector and - is a $N \times N$ variance—covariance matrix, then $( X _ { ( 2 ) } \mid X _ { ( 1 ) } = x _ { ( 1 ) } ) \sim M N ( \mu _ { 2 . 1 } , \nu _ { 2 . 1 } )$ , where $X =$ $\ O _ { X _ { ( 2 ) } } ^ { X _ { ( 1 ) } } ) , \mu \ = \ \binom { \mu _ { ( 1 ) } } { \mu _ { ( 2 ) } } , \ \theta \ = \ \binom { \delta _ { 1 1 } } { \delta _ { 2 1 } } , \ \delta _ { 2 2 } ) , \ \theta _ { 2 1 } = \ \theta _ { 1 2 } ^ { \mathrm { T } } ,$ covariance( $X _ { ( 1 ) } )$ $\mathbf { \Phi } = \vartheta _ { 1 1 } ,$ covariance( ${ \cal X } _ { ( 2 ) } ) = \vartheta _ { 2 2 } ,$ covariance $X _ { ( 1 ) } , X _ { ( 2 ) } ) =$ $\mathfrak { d } _ { 1 2 } , \mu _ { 2 . 1 } = \mu _ { ( 2 ) } + \mathfrak { d } _ { 2 . 1 } \mathfrak { d } _ { 1 1 } ^ { - 1 } \left( x _ { ( 1 ) } - \mu _ { ( 1 ) } \right)$ , and $\vartheta _ { 2 . 1 } = \vartheta _ { 2 2 }$ $- \vartheta _ { 2 1 } \vartheta _ { 1 1 } ^ { - 1 } \vartheta _ { 1 2 } .$

In our model, partition each vector into two parts: the first n elements in one partition and the rest $( N -$ n) in the other. Partition each matrix into four parts: $n \times n$ in the northwest, $n \times ( N - n )$ in the northeast, $( N \mathrm { ~ - ~ } n ) \times n$ in the southwest, $( N \mathrm { ~ - ~ } n ) \times ( N \mathrm { ~ - ~ } n )$ in the southeast quadrants. Specifically, let $d _ { \bf ( 1 ) } \ = \ ( d _ { 1 } ,$ $d _ { 2 } , \ldots , d _ { n } ) ^ { \mathrm { T } } , d _ { ( 2 ) } = ( d _ { n + 1 } , d _ { n + 2 } , \ldots , d _ { N } ) ^ { \mathrm { T } } , E _ { ( 1 ) t } = ( \varepsilon _ { 1 t } ,$ $\varepsilon _ { 2 t } , \varepsilon _ { - } , \ \varepsilon _ { n t } ) ^ { \mathrm { T } } , \ E _ { ( 2 ) t } \ = \ ( \varepsilon _ { ( n + 1 ) t } , \ \varepsilon _ { ( n + 2 ) t } , \ldots , \ \varepsilon _ { N t } ) ^ { \mathrm { T } } , \ \Sigma \ =$ $( { } _ { \Sigma _ { 2 1 } } ^ { \Sigma _ { 1 1 } } \ { } _ { \Sigma _ { 2 2 } } ^ { \Sigma _ { 1 2 } } ) , \ \Sigma _ { 2 1 } \ = \ \Sigma _ { 1 2 } ^ { \mathrm { T } } ,$ covariance $\begin{array} { r c l } { ( E _ { ( 1 ) t } ) } & { = } & { \Sigma _ { 1 1 } , } \end{array}$ covariance $\begin{array} { r } { \mathsf { \Omega } : ( E _ { ( 2 ) t } ) \ = \ \Sigma _ { 2 2 } , } \end{array}$ covariance $( { \cal E } _ { ( 1 ) t } , \ { \cal E } _ { ( 2 ) t } ) \ = \ \Sigma _ { 1 2 } , \ \Gamma \ =$ $( { \Gamma } _ { 0 } ^ { \Gamma _ { ( 1 ) } } \ { } _ { \Gamma _ { ( 2 ) } } ^ { 0 } ) , \Gamma _ { ( 1 ) } = ( \Gamma _ { ( 1 ) } ) _ { n \times n } = { \mathrm { d i a g o n a l } } ( \scriptstyle \rho _ { 1 } , \scriptstyle \rho _ { 2 } , \dotsc , \dotsc , \dotsc , \dotsc ,$ , and $\Gamma _ { ( 2 ) } ~ = ~ ( \Gamma _ { ( 2 ) } ) _ { ( N - n ) \times ( N - n ) } ~ = ~ \mathrm { d i a g o n a l } ( \mathsf { p } _ { n + 1 } , ~ \mathsf { p } _ { n + 2 } , \ldots , \mathsf { \ldots } ,$ $\rho _ { N } ) .$

Then, $( Y _ { t + 1 } \mid \varepsilon _ { i t } , i \le n ) \sim M N ( d \ + \ \Gamma Y _ { t } \sim \mu _ { N , n } , \Sigma _ { T } ^ { n } ) .$ where

$$
\begin{array}{r l} & {\boldsymbol {\mu} _ {N, n} = \binom{\boldsymbol {\Gamma} _ {(1)} \boldsymbol {\varepsilon} _ {(1) t}}{\boldsymbol {\Gamma} _ {(2)} \boldsymbol {\Sigma} _ {2 1} \boldsymbol {\Sigma} _ {1 1} ^ {- 1} \boldsymbol {\varepsilon} _ {(1) t}},} \\ & {\boldsymbol {\Sigma} ^ {n} = (I + I) \boldsymbol {\Sigma} (I + \boldsymbol {\Gamma}) ^ {\mathrm{T}} + \boldsymbol {\Gamma} \boldsymbol {\Sigma} _ {N, n} \boldsymbol {\Gamma} ^ {\mathrm{T}},} \\ & {\boldsymbol {\Sigma} _ {N, n} = (\boldsymbol {\Sigma} _ {N, n}) _ {N \times N} = \left( \begin{array}{c c} 0 _ {n \times n} & 0 _ {n \times (N - n)} \\ 0 _ {(N - n) \times n} & \boldsymbol {\Sigma} _ {2 2} - \boldsymbol {\Sigma} _ {2 1} \boldsymbol {\Sigma} _ {1 1} ^ {- 1} \boldsymbol {\Sigma} _ {1 2} \end{array} \right).} \end{array}
$$

The manufacturer’s order-up-to level when n retailers participate in CRP, $T _ { t } ^ { n } ,$ can be determined to be

$$
T _ {t} ^ {n} = 1 ^ {\mathrm{T}} (d + \Gamma Y _ {t} - \mu_ {N. n}) + L (1 ^ {\mathrm{T}} \Sigma^ {n} 1) ^ {1 / 2}.\tag{4.6}
$$

4.2.3. Value of CRP. We can now determine the value of CRP to the manufacturer and retailers. We focus on the benefit of CRP first. In the next section, we consider the CRP cost to determine the optimal structure. The manufacturer benefits through CRP because (i) CRP reduces the uncertainty of demand at the manufacturer $( \Sigma ^ { n } \leq \Sigma ^ { 0 } )$ , and (ii) continuous replenishment to retailers (instead of replenishment only at the beginning or end of a period) moves the manufacturer inventory faster, which, in turn, reduces its inventory carrying cost. The participant retailers benefit through CRP because they store very little inventory, and, in addition, the replenishment is immediate under CRP. This reduces their inventory carrying cost to almost zero under CRP. However, the nonparticipant retailers neither benefit nor lose from CRP because their ordering decisions and their supply from the manufacturer are not affected by CRP. We derive the expressions for the value of CRP next.

(a) Value to the Manufacturer. CRP’s benefit to the manufacturer is direct and clear because the manufacturer stores smaller inventory and can forecast retailer demands more accurately. Silver and Petersen (1985) showed that the average inventory level during Period t in an order-up-to-T system in the traditional setup without CRP is

$$
T _ {t} - E (Y _ {t + 1}) + \frac {E (Y _ {t})}{2}.
$$

Following the derivation used by LST for the one retailer case, and using the facts

$$
\lim _ {t \to \infty} E (Y _ {t}) = \sum_ {i = 1} ^ {N} \frac {d _ {i}}{1 - \rho_ {i}}
$$

and $E ( \mathfrak { s } _ { t } ) = 0 .$ , we can show that

$$
\lim _ {t \rightarrow \infty} E (T _ {t}) = \sum_ {i = 1} ^ {N} \frac {d _ {i}}{1 - \rho_ {i}} + L (1 ^ {T} \Sigma^ {0} 1) ^ {1 / 2}.
$$

Hence, the manufacturer’s average inventory when there is no CRP is given by

$$
\sum_ {i = 1} ^ {N} \frac {d _ {i}}{2 (1 - \rho_ {i})} + L (1 ^ {T} \Sigma^ {0} 1) ^ {1 / 2}.
$$

When replenishment to participant retailers is done continuously under CRP, the inventory level at the end of a period is reduced from T by the amount used to replenish the CRP participant retailers during the period. The expected total replenishment amount during a period in the limit as $t \to \infty$ is given by $\Sigma _ { i = 1 } ^ { n } ( d _ { i } / 1 \mathrm { ~ - ~ }$ q ). Thus, the manufacturer’s inventory level at the end of a period will be

$$
\sum_ {i = 1} ^ {N} \frac {d _ {i}}{1 - \rho_ {i}} + L (1 ^ {t} \Sigma^ {0} 1) ^ {1 / 2} - \sum_ {i = 1} ^ {n} \frac {d _ {i}}{1 - \rho_ {i}}
$$

under CRP. Because the inventory level rises linearly from safety stock, $L ( 1 _ { T } \Sigma ^ { 0 } 1 ) ^ { 1 / 2 } .$ , at the beginning of a period to

$$
\sum_ {i = 1} ^ {N} \frac {d _ {i}}{1 - \rho_ {i}} + L (1 ^ {t} \Sigma^ {0} 1) ^ {1 / 2} - \sum_ {i = 1} ^ {n} \frac {d _ {i}}{1 - \rho_ {i}}
$$

at the end of a period, the manufacturer’s average inventory level when there is CRP with first n retailers as participants is given by

$$
\sum_ {i = 1} ^ {N} \frac {d _ {i}}{2 (1 - \rho_ {i})} - \sum_ {i = 1} ^ {n} \frac {d _ {i}}{2 (1 - \rho_ {i})} + L (1 ^ {T} \Sigma^ {n} 1) ^ {1 / 2}. ^ {3}
$$

The reduction in the average inventory holding cost per period at the manufacturer site when the first n retailers share their demand information, $S _ { M } ,$ is determined to be

<sup>3</sup>It can be shown that when the number of replenishments during a time-period is fixed at $g ,$ the reduction in average inventory is given by

$$
\sum_ {i = 1} ^ {n} \frac {g - 1}{g} \frac {d _ {i}}{2 (1 - \rho_ {i})}.
$$

The proof for this expression is given in the appendix. The no CRP case occurs when $g = 1$ and continuous replenishment occurs when $g  \infty .$

$$
\begin{array}{l} S _ {M} = H \bigg (\sum_ {i = 1} ^ {n} \frac {d _ {i}}{2 (1 - \rho_ {i})} + L (1 ^ {T} \Sigma^ {0} 1) ^ {1 / 2} \\ \qquad - L (1 ^ {T} \Sigma^ {n} 1) ^ {1 / 2} \bigg). \end{array}\tag{4.7}
$$

Define

$$
\begin{array}{r l} {a} & {= 1 ^ {T} \Sigma 1, \mathrm{and}} \\ {b _ {n}} & {= 1 ^ {T} \Sigma_ {N. n} 1.} \end{array}
$$

Then, the value of CRP per period to the manufacturer, is given by

$$
\begin{array}{l} S _ {M} = H \left(\sum_ {i = 1} ^ {n} \frac {d _ {i}}{2 (1 - \rho_ {i})} \right. \\ \quad \left. + L (\sqrt {a + b _ {0}} - \sqrt {a + b _ {n}})\right). \end{array}\tag{4.8}
$$

In (4.8), the first term in the summation represents the savings derived from continuous replenishment of inventory, and the second term represents the savings from improved accuracy of demand forecasts. Manufacturers and retailers can indeed share information without VMI. In such cases, the entire benefit will be because of improved forecasting.

(b) Value to Retailer Participants. Participant retailers inventory levels also go down because of CRP. In the continuous replenishment scenario, retailer participants carry negligible inventory under CRP. Hence, the value of CRP to the retailer participants is equal to the expected inventory holding cost when there is no CRP. Because the retailers also use the order-up-to-T strategy, the expected inventory carrying cost per period of Retailer i when there is no CRP is computed to be, using the same procedure as for the manufacturer,

$$
\frac {d _ {i}}{2 (1 - \rho_ {i})} + k _ {i} (\Sigma_ {i i}) ^ {1 / 2}.
$$

Hence, the value of CRP to Retailer $i , i \leq n ,$ is

$$
S _ {i} = h _ {i} \bigg (\frac {d _ {i}}{2 (1 - \rho_ {i})} + k _ {i} (\Sigma_ {i i}) ^ {1 / 2} \bigg).\tag{4.9}
$$

4.2.4. Value of Information Sharing Only. To provide insights into the relative values of information sharing and VMI, we consider the case in which retailers provide the manufacturer access to their inventory level, but the inventory is replenished only at the end of every period as in the no CRP case. In this scenario, the manufacturer’s gain comes only from improved forecasting. Here, the average inventory, when the first n retailers share information, is

$$
\sum_ {i = 1} ^ {N} \frac {d _ {i}}{2 (1 - \rho_ {i})} + L (1 ^ {T} \Sigma^ {n} 1) ^ {1 / 2}.
$$

Consequently, the value of information sharing alone is

$$
\overline {{S _ {M}}} = H L (\sqrt {a + b _ {0}} - \sqrt {a + b _ {n}}).\tag{4.10}
$$

Because continuous replenishment requires access to real-time inventory level, we can determine, from (4.8) and (4.10), that the incremental value of continuous replenishment to the manufacturer,

$$
S _ {M} - \overline {{S _ {M}}} = H \sum_ {i = 1} ^ {n} \frac {d _ {i}}{2 (1 - \rho_ {i})}.
$$

We next analyze the characteristics of the value of CRP.

## 5. Impact of CRP

It can be verified from (4.8) and (4.9) that the value of CRP to the manufacturer and participant retailers is nonnegative. We also show the following results that provide insights into the nature of the value of CRP (proofs for propositions are given in the appendix).

Proposition 1. (i) $S _ { M }$ is increasing in $\varSigma , i . e . , i f \varSigma _ { 1 } \geq$ $\Sigma _ { 2 } ( i . e . , \Sigma _ { 1 } - \Sigma _ { 2 }$ is positive semi-definite), then $S _ { M } f o r \ : \mathcal { Z } _ { 1 }$ $\geq S _ { M } f o r \ Z _ { 2 } ,$ and so on.

(ii) if $T \geq 0$ , then $S _ { M }$ is increasing in C, i.e., if ${ \cal T } _ { 1 } \geq { \cal T } _ { 2 }$ $( { \cal I } _ { 1 } \ - \ { \cal I } _ { 2 }$ is positive semi-definite), then $S _ { M } f o r \ I _ { 1 } \geq S _ { M }$ for $T _ { 2 }$ and so on.

(iii) $S _ { M }$ is increasing in n.

$$
\begin{array}{l} (i v) S _ {i} \text {is increasing in} \Sigma_ {i j}. \\ (v) S _ {M} \text {and} S _ {i} \text {are increasing in} d _ {i}. \end{array}
$$

Proposition 1 shows that the value of CRP to the manufacturer is higher when the serial/cross-correlation and variance of retailer demands, the number of retailers participating in CRP, and the size, as measured by the base demand $d _ { i } ,$ of retailer participants are higher. The intuition for the result is when serial correlation is high, the demand during Period t contains more information about the demand during Period (t $^ { + } \ 1 )$ . Thus, the sharing of demand information improves the manufacturer’s forecast accuracy more, resulting in higher savings. Similar reasoning applies when more retailers share information and demands during a period have high variances (i.e., higher diagonal elements in R) or cross-correlations. When larger retailers participate in the CRP network, the manufacturer benefits more because larger quantities are pushed out of its inventory faster. Similar phenomenon occurs at the participating retailers also.

The following result provides insights into the relative values of continuous replenishment and information sharing.

Proposition 2. The ratio of incremental value of continuous replenishment to the value of information sharing only, $( S _ { M } \mathrm { ~ - ~ } \overline { { S _ { M } } } ) / S _ { M } ,$ increases (decreases) as $\Sigma _ { i = 1 } ^ { n } ~ d _ { i }$ increases (decreases) and/or R decreases (increases).

The reason for the above result is that the values generated by continuous replenishment and by information sharing arise from two independent effects, although continuous replenishment requires information sharing. Continuous replenishment reduces inventory-carrying cost because it moves inventory faster from the manufacturer to the retailer. On the contrary, the value of information sharing comes solely from the variance structure of demand. The higher the R, the higher the manufacturer inventory because of the need for higher safety stock. Information sharing reduces R and, hence, the safety stock but has no effect on the expected demand.

Proposition 1 shows that the CRP size, measured as the fraction of retailers who participate in CRP, and the retailer size, measured by $d _ { i } ,$ have significant impact on the retailers’ and manufacturers’ incentives to participate in CRP and, consequently, the optimal number of retailers in the CRP. However, analytical investigation of the optimal number of retailers in CRP is impossible unless restrictions are imposed on the parameter values.

## 5. Optimal Number of Retailers

While an increase in the number of retailer partners increases the value to the manufacturer as shown in Proposition 1, the cost of maintaining the CRP network is likely to increase also. As for the manufacturer, CRP requires establishing and maintaining communication network connections with retailer participants, monitoring retailer inventories, and replenishing the inventory of retailer partners continuously. If EDI networks between the manufacturer and retailers exist already, the incremental information sharing cost for CRP is likely to be negligible. However, the cost of continuous replenishment can still be significant because more trips to retailers with smaller consignments will have to be made. This transportation cost will increase when the number of participating CRP retailers increases. We assume that the manufacturer’s incremental cost for maintaining a CRP network is $r , r > 0 ,$ , per retailer participant, per period.

The cost of CRP to retailers is less clear. While managing the retailer side of the network may incur costs, the inventory monitoring and ordering costs of retailers will decrease because of VMI. We assume that Retailer $i ^ { \prime } { \mathsf { s } }$ cost of participation in CRP is $c _ { i }$ per period. $c _ { i }$ can be positive or negative. Negative $c _ { i }$ implies that Retailer i benefits from CRP even without accounting for the reduction in its inventory cost because of CRP. If $c _ { i } \leq S _ { i } ,$ then Retailer i will join the CRP network voluntarily; otherwise, it will join only if the manufacturer subsidizes the retailer to the extent of at least $( c _ { i } \mathrm { ~ - ~ } S _ { i } )$

Assuming that the list of retailers is rearranged so that the first n retailers are in the CRP network, the optimal number of retailer participants in the CRP network can be obtained by solving

$$
\begin{array}{l} \arg \max \left\{S _ {M} - r n - \sum_ {i = 1} ^ {n} \max (0, (c _ {i} - S _ {i}) \right\} \\ 0 \leq n \leq N. \end{array}
$$

The optimal solution to this model depends on the shape of $S _ { M } .$ . The shape of $S _ { M }$ cannot be established unless restrictions are made on the parameters. We derive the optimal CRP structure for the following special cases.

Case 1: Identical Retailers. For this case, assume $( \mathsf { a } ) d _ { 1 }$ $= d _ { 2 } = . . . = d ^ { \prime } , ( { \bf b } ) { \sf p } _ { 1 } = { \sf p } _ { 2 } = . . . = { \sf p } _ { N } = { \sf p ^ { \prime } } > 0 , ( { \sf c } )$ $\mathrm { V a r } ( \mathfrak { e } _ { i t } ) = \sigma ^ { 2 }$ for $i = 1 , 2 , \dots , N ,$ and (d) $\operatorname { C o v } ( \varepsilon _ { i t } , \ \varepsilon _ { j t } )$ $= \mathsf { p } \sigma ^ { 2 } .$ , for all t and $i = 1 , 2 , \ldots , N , j = 1 , 2 , \ldots , N , \bar { N }$ J $> 1$ , and $i \neq j , ( - 1 / N - 1 ) \leq \mathsf { p } \leq 1$ . The condition $( - 1 / N - 1 ) \le \mathtt { p } \le 1$ guarantees that the covariance matrix is positive semi-definite. In addition $c _ { i } = c$ for all i.

For this situation, we can derive

$$
a = \sigma^ {2} (1 + \rho^ {\prime}) ^ {2} \frac {N [ (1 - \rho) ^ {2} + N (\rho - \rho^ {2}) ]}{1 - \rho},\tag{5.1}
$$

$$
b _ {n} = \sigma^ {2} \rho^ {\prime 2} \frac {(N - n) [ (1 - \rho) ^ {2} + N (\rho - \rho^ {2}) ]}{1 + (n - 1) \rho},\tag{5.2}
$$

$$
\sum_ {i = 1} ^ {n} \frac {d _ {i}}{2 (1 - \rho_ {i})} = \frac {n d ^ {\prime}}{2 (1 - \rho^ {\prime})}.\tag{5.3}
$$

The following result establishes the shape of $S _ { M } .$

Proposition 3. In the identical retailer case,

(i) a $\rho \ge 0$ exists such that for all $\rho \le \underline { { \rho } } , S _ { M }$ is convex for all n.

(ii) a $\bar { \rho } > 0$ exists such that for all $\rho \ge \bar { \rho } , S _ { M }$ is concave for all n.

The above proposition states that in the case of identical retailers, the value of CRP to the manufacturer is concave in n for all n when cross-correlation among retailer demands is sufficiently high, and the surplus function is convex when the cross-correlation is sufficiently low. In the region $\begin{array} { r } { \rho < \rho < \bar { \rho } , } \end{array}$ the surplus function is neither concave nor convex for all n.

The proposition can be explained as follows. The value generated by continuous replenishment as opposed to improved forecasting increases linearly with n. Hence, the shape, i.e., convex or concave, of the value function is determined by the value generated by improved forecasting. When cross-correlation is high and positive, the manufacturer can forecast, with a high degree of accuracy, the demand at a retailer site using the demand information from another retailer. Consequently, the incremental value derived from subsequent information is smaller than that of the earlier. When the cross demands are weakly correlated or independent, the manufacturer cannot estimate the demand at one retailer using the demand information from another retailer. In such cases, the incremental surplus will be higher for later participants because of the pooling effect. As an illustration of the pooling effect, consider a two-retailer situation with identical but independent demands. When there is no CRP, the standard deviation of $\Sigma _ { i = 1 } ^ { 2 } \ \varepsilon _ { i t } ,$ the random error of manufacturer demand at the manufacturer end, is $\sqrt { 2 \sigma }$ . When one retailer participates in CRP, the standard deviation reduces to $\sigma ,$ a reduction of 0.414r. When both retailers share information, the standard deviation reduces to zero, a further reduction of $\sigma >$

0.414r. Negative correlation across retailer demands reduces the demand variance at the manufacturer site, which again leads to convex surplus function. A question of interest is the size of the range (q, A large q¯ ). range may limit the usefulness of Proposition 3 because the result depends crucially on the concavity and convexity conditions. We performed computational experiments with different values of $N , \rho ^ { \prime } ,$ , and $\rho .$ For $\rho ^ { \prime } = 0 . 1$ and $N = 2 ,$ the range of $\rho$ for which the surplus function was concave and convex was (0.0009, 0.0009). When N increased to 10, the range extended to (0.0002, 0.0009). For $\rho ^ { \prime } = 0 . 9 .$ , the ranges were (0.025, 0.025) and (0.004, 0.006) for $N = 2$ and $N = 1 0 ,$ , respectively. We also experimented with higher values of N. The computational results suggest that the size of this range is generally a very small fraction of 1, and the maximum of this range is generally well below 0.01. Thus, for all practical purposes, in the identical retailer case, we can assume that the surplus function is convex when the random errors are independent and concave even for correlation coefficients as low as 0.01.

Now, when ${ \mathrm {  ~ \ p ~ } } > { \bar { \mathrm {  ~ \ p ~ } } } ,$ because $S _ { M }$ is concave, and the cost function is linear in $n ,$ the optimal number of retailers will occur when the marginal increase in value is equal to the marginal increase in cost, i.e., when

$$
\frac {\partial S _ {M}}{\partial n} = r + \max \biggl (0, c - h \biggl (\frac {d ^ {\prime}}{2 (1 - \rho^ {\prime})} + k \sigma \biggr) \biggr).
$$

Because $S _ { M }$ is concave, the optimal number of retailers decreases when r or c increases. The optimal number of retailers in the network depends on $\rho ,$ too. Although we couldn’t show it analytically, computational experiments showed that the optimal number of retailers in the network decreases generally as $\rho$ increases. This is explained by the fact that as q increases, the manufacturer’s forecasting accuracy increases with the same information. At the extreme when ${ \rho } = 1$ , i.e., retailer demands are perfectly correlated, the manufacturer can forecast every retailer demand based on information from just one retailer.

When ${ \mathfrak { p } } < { \mathfrak { p } } ,$ i.e., when the demands across retailers are nearly independent, the optimal number of retailer participants is either 0 or N because $S _ { M }$ is convex. The optimal number of retailers will be N if the value of CRP exceeds the cost when $n \ = \ N .$ . If the demands across retailers are independent, we can derive that the optimal number of retailers is N when

$$
\begin{array}{l} r + \max \left(0, c - h \left(\frac {d ^ {\prime}}{2 (1 - \rho^ {\prime})} + k \sigma\right)\right) \\ <   \frac {d ^ {\prime}}{2 (1 - \rho^ {\prime})} + \frac {\sigma (\sqrt {(1 + \rho^ {\prime}) ^ {2} + \rho^ {\prime 2}} - (1 + \rho^ {\prime}))}{\sqrt {N}}. \end{array}
$$

If $S _ { M }$ is convex, and the optimal number of retailers is N, implementing CRP with a smaller number of retailers can be not only less than optimal but unprofitable as well. CRP may become profitable only after the network reaches a “critical mass” of retailer participants because of lower value generated for smaller values of n. Prior research on interorganizational communication networks has also developed such a theory of critical mass (Markus 1990). It is interesting to note that in the upstream supply chain partnerships, while IT such as EDI tends to reduce the number of supplier partners for a manufacturer (Bakos and Brynjolfsson 1993, Wang and Seidmann 1995), our results show that CRP on the downstream supply chain may have a few or a large number of retailer partners.

The difference in the optimal number of retailers under weak and high correlation conditions stems from the fact that information behaves as substitutes under high correlation conditions and complements under low correlation conditions. Similar results because of the substitutable and complementary nature of information when demands are highly correlated or independent, respectively, have been shown to exist in the information goods market (Sarvary and Parker 1997).

Case 2: Heterogeneous Retailers. Case 2 is same as Case 1 except that $d _ { i } \mathbf { s }$ are no longer identical. Higher $d _ { i }$ represents a larger retailer. Without loss of generality, assume that the retailers are indexed in decreasing order of their size, i.e., $d _ { 1 } \geq d _ { 2 } \geq . . . \geq d _ { N } .$ All other aspects of the model remain the same as in the identical retailer situation.

While the model to determine the optimal structure remains the same as in the identical retailer case, the manufacturer will recruit retailers in the decreasing order of their sizes as this strategy will maximize the manufacturer profit. We can easily show that when q $> \bar { \mathsf { p } } , S _ { M }$ remains concave under this strategy. Thus, the results for the identical retailer case hold for this case, too. When ${ \mathfrak { p } } < { \mathfrak { p } } ,$ , it is not clear whether $S _ { M }$ will remain convex because the increasing marginal value generated by improved forecasting is offset by the decreasing marginal value of continuous replenishment. The shape of $S _ { M }$ depends on which effect dominates the other. Additional insights about the optimal number of retailers can be derived only for specific parameter values. Next, we discuss the managerial implications of the analytical results.

## 6. Managerial Implications

## 6.1. Value of CRP

Our analysis shows that CRP benefits the participants in two ways: continuous replenishment that benefits the manufacturer and the participant retailers, and improved forecasting that benefits the manufacturer. Improved forecasting and continuous replenishment complement each other by reducing the two dimensions that determine the inventory-carrying cost: the number of units in the inventory and the time for which the inventory is stored. The reduction in inventory-carrying cost because of CRP is significant in high demand, high variance, and high correlation (serial and cross) environments because the manufacturer (and retailers) has to keep a high inventory to meet its service-level requirement in such cases. Thus, CRP can be useful not only for mature products with stable, but high, demands (such as those in the grocery industry (Fernie 1999) where CRP was initiated) but also for new products with huge demand uncertainty (such as semiconductors and computer peripherals in the high-tech industry (Carbone 1996, Hughes et al. 1998)). However, it should be noted that the value from CRP includes both information sharing and continuous replenishment. Thus, it becomes imperative to analyze relative values of information sharing and VMI within the specific supply chain context to carry out appropriate reengineering efforts.

## 6.2. Information Sharing Versus Continuous Replenishment

Our results show that while both information sharing and continuous replenishment benefit the manufacturer, the relative values of these components vary. The value of continuous replenishment relative to that of information sharing is high when expected demand is high and the variance is low. This ratio decreases as the variance becomes higher and the expected demand becomes smaller. A significant implication of this finding is that information sharing alone, which is facilitated by EDI, may not be of much value, especially in stable product markets such as the grocery industry. Realizing maximum value out of CRP requires a radical restructuring of the replenishment process such as the introduction of VMI. Because VMI requires sharing of real-time inventory data and delegating the replenishment process to the manufacturer by the retailer, the manufacturer and the retailers have to form a close partnership in place of the traditional “arm’s length” relationship. On the other hand, for relatively new products whose demand is difficult to forecast, information sharing alone may reduce the manufacturer’s uncertainty and provide significant value to the manufacturer. However, the retailers do not realize any benefit without continuous replenishment. If continuous replenishment is impossible or too costly, the manufacturer may have to provide other types of incentives such as price discount in return for information sharing.

From a manager’s perspective, the overall value of CRP and the relative value of information sharing and continuous replenishment can be described using the following grid:

<table><tr><td rowspan="3">HighCrossCorrelationLow</td><td>Moderate value from CRP, information sharing is likely to be the major contributor.</td><td>High value from CRP, both information sharing and continuous replenishment contribute significantly.</td></tr><tr><td>Low value from CRP, both information sharing and continuous replenishment contribute little.</td><td>Moderate value from CRP, continuous replenishment is likely to be the major contributor.</td></tr><tr><td>Low</td><td>High</td></tr></table>

## 6.3. Retailer Recruitment Strategy

Our results show that, everything else being equal, the manufacturer should recruit larger retailers first, i.e., those with a higher expected demand, for two reasons. First, the manufacturer has to keep higher stock to satisfy larger demand. A reduction in the duration for which the stock is kept will reduce the manufacturer’s cost. Continuous replenishment reduces this duration. Second, the variance of demands at larger retailers is also likely to be higher compared to that of smaller retailers resulting in higher safety stock. The push to recruit larger retailers also comes from the retailer side. Larger retailers realize a higher value from CRP. The manufacturer may find it profitable to provide subsidies to retailers to implement CRP if their implementation cost outweighs the benefit they derive. The manufacturer can minimize such subsidies if it recruits larger retailers first.

## 6.4. Number of Retailers

The number of retailers the manufacturer should recruit depends critically on the correlation among the retailer demands. Highly correlated demands increase the value of CRP more. However, they also reduce the marginal value of additional information because higher correlation enables more accurate forecasting with limited information. A consequence of substitutability of highly correlated information is the reduction in the manufacturer’s need to form informationsharing partnerships with several retailers. Of course, if the benefit from continuous replenishment alone exceeds the cost of CRP implementation, the manufacturer should partner with every retailer. On the contrary, information about independent retailer demands act in a complementary manner. This is a direct result of demand pooling at the manufacturer end. In such cases, the manufacturer should partner with every retailer, assuming that the total benefit of CRP exceeds the total cost. Thus, the manufacturer should carefully analyze the relative values obtained from continuous replenishment and improved forecasting as well as the cross-correlations in demand when deciding whether to partner with an additional retailer.

It should be noted that because CRP involves business process restructuring, implementation of CRP can be time consuming and difficult. It may also require changes to the management style and structure. Our analysis quantifies the value of CRP, assuming that CRP doesn’t suffer from such potential bottlenecks that can reduce its value.

## 6. Discussion

Our research was motivated by recent developments in IT-enabled supply chain reengineering efforts that have been initiated by both manufacturers and retailers. Effort is also underway to formulate industrywide standards for such initiatives (Computer World 1996, Verity 1996). Although our model is representative of many actual supply chains in which historical data are used to forecast the future, we recognize that the results are limited to the setting we consider. The demand process is nonstationary in our model. In a stationary demand case, the entire benefit comes from continuous replenishment as past demand does not reveal any information about the future demand. We derived the key results for the general case. Additional results were derived for the situation when the demand processes except the base demands are identical at all retailer sites. The assumption of zero leadtime does not play a significant role in our analysis. While leadtime reduction has been shown to have significant impact on information-sharing partnerships (Cachon and Fisher 1998, Lee et al. 2000), positive leadtime in our model simply increases the CRP value.

In supply chain partnerships such as CFAR, the type of information shared is not limited to historical demand information. The sharing of demand forecasts, conditioned upon retailer strategies and demand signals available at the retailer site, is also common. Our model can be extended to include such forecast sharing, too. For instance, a retailer might get a Signal $l _ { t }$ in time Period t about $\pounds _ { t + 1 } .$ Sharing of $l _ { t }$ with the manufacturer in addition to $D _ { t }$ can increase the surplus further. Correlation analysis similar to the one employed in this paper can be used for this analysis.

Our results point to the need for analyzing correlations among retailer demands because they affect not only the overall value of information sharing but also the structure of the CRP partnership. However, our model is silent on what factors influence the retailer demands to be correlated or independent. We conjecture that the nature of product, retailer locations, and consumer segments served by retailers, among others, will affect the demand correlations. Empirical research can provide insights into this issue. Several other issues related to CRP, such as the surplus division among participants, bargaining process, and other incentive and contract mechanisms, need to be investigated further to gain a better understanding of the impact of CRP networks on trading partners. Other considerations remain, such as the sensitivity of retailers to share their inventory information with the manufacturer and their fears about the impact of such information sharing on competition and price. These issues need to be investigated to assess their impact on the benefits offered by CRP.

## Appendix

Proof for the Average Manufacturer Inventory when the Number of Replenishments Per Period Is $g .$ Let the number of replenishments during a period be $g .$ Then, the expected number of units shipped in each shipment during Period t is $\Sigma _ { i = 1 } ^ { n } Y _ { i t } / g .$ . Because the demand structure and the service-level requirement remain the same, there is no change to the manufacturer’s order-up-to stock and safety-stock levels. Hence, under CRP,

$$
\lim _ {t \rightarrow \infty} E (T _ {t} ^ {\prime}) = \sum_ {i = 1} ^ {N} \frac {d _ {i}}{1 - \rho_ {i}} + L (1 ^ {T} \Sigma^ {n} 1) ^ {1 / 2}
$$

holds true in which the safety stock is $L ( 1 ^ { T } \Sigma ^ { n } 1 ) ^ { 1 / 2 }$ . The expected inventory at the end of time Period t also remains as

$$
\sum_ {i = 1} ^ {N} \frac {d _ {i}}{1 - \rho_ {i}} + L (1 ^ {T} \Sigma^ {n} 1) ^ {1 / 2} - \sum_ {i = 1} ^ {n} \frac {d _ {i}}{1 - \rho_ {i}}.
$$

However, the inventory does not increase linearly during the period if replenishment is not continuous. When the number of replenishments is $\mathbf { g } ,$ the expected inventory level at replenishment poin $: j , j =$ $1 , \ldots , g ,$ during the Period $t , I _ { \mathrm { j } } ,$ is

$$
L (1 ^ {T} \Sigma^ {n} 1) ^ {1 / 2} + j \frac {\sum_ {i = 1} ^ {N} \frac {d _ {i}}{1 - \rho_ {i}}}{g} - (j - 1) \sum_ {i = 1} ^ {n} \frac {Y _ {i t}}{g}.
$$

The expected inventory at the beginning of the period, $I _ { 0 } = L ( 1 ^ { T } \Sigma ^ { n }$ $1 ) ^ { 1 / 2 } .$ . Because

$$
\begin{array}{l} \lim _ {t \to \infty} \sum_ {i = 1} ^ {n} \frac {Y _ {i t}}{g} = \sum_ {i = 1} ^ {n} \frac {d _ {i}}{g (1 - \rho_ {i})}, \lim _ {t \to \infty} L (1 ^ {T} \Sigma^ {n} 1) ^ {1 / 2} \\ + j \frac {\sum_ {i = 1} ^ {N} \frac {d _ {i}}{1 - \rho_ {i}}}{g} - (j - 1) \sum_ {i = 1} ^ {n} \frac {Y _ {i t}}{g} = L (1 ^ {T} \Sigma^ {n} 1) ^ {1 / 2} \\ + j \sum_ {i = 1} ^ {N} \frac {d _ {i}}{g (1 - \rho_ {i})} - (j - 1) \sum_ {i = 1} ^ {n} \frac {d _ {i}}{g (1 - \rho_ {i})}. \end{array}
$$

Now the expected inventory during Period t is

$$
\frac {1}{g} \sum_ {j = 0} ^ {g - 1} \frac {I _ {j} + I _ {j + 1}}{2},
$$

which can be computed as

$$
\sum_ {i = 1} ^ {N} \frac {d _ {i}}{2 (1 - \rho_ {i})} - \sum_ {i = 1} ^ {n} \frac {g - 1}{g} \frac {d _ {i}}{2 (1 - \rho_ {i})} + L (1 ^ {T} \Sigma^ {n} 1) ^ {1 / 2}.
$$

Proof for Proposition 1. (i) $S _ { M } ~ = ~ H ~ ( \Sigma _ { i = 1 } ^ { n } ~ d _ { i } / 2 ( 1 ~ - ~ \rho _ { i } ) ~ + ~ $ $L ( \sqrt { a { \mathrm { ~ + ~ } } b _ { 0 } } \ - \ \sqrt { a { \mathrm { ~ + ~ } } b _ { n } } ) ) . \ \sum _ { i = 1 } ^ { n } d _ { i } / 2 ( 1 \ - \ \mathrm { p } _ { i } )$ is independent of $\Sigma . \ S _ { 0 } ,$ we consider only $H L ( \sqrt { a + b _ { 0 } } - \sqrt { a + b _ { n } } ) . \mathrm { L e t } \Sigma _ { 1 } - \Sigma _ { 2 } = \Sigma _ { \Delta } ,$ and $\left( \Sigma _ { 1 } \right) _ { N . n } - \left( \Sigma _ { 2 } \right) _ { N . n } = \left( \Sigma _ { \Delta } \right) _ { N . n } .$ Then, $H L ( \sqrt { a + b _ { 0 } } - \sqrt { a + b _ { n } } ) =$

$$
H L \left\{\left(1 ^ {T} (\mathrm{I} + \Gamma) \Sigma_ {2} (\mathrm{I} + \Gamma) ^ {T} 1 + 1 ^ {T} \Gamma \Sigma_ {2} \Gamma^ {T} 1 + 1 ^ {T} (\mathrm{I} + \Gamma) \right. \right.
$$

$$
\Sigma_ {\Delta} (\mathrm{I} + \Gamma) ^ {T} 1 + 1 ^ {T} \Gamma \Sigma_ {\Delta} \Gamma^ {T} 1) ^ {0. 5} - (1 ^ {T} (\mathrm{I} + \Gamma)
$$

$$
\Sigma_ {2} (\mathrm{I} + \Gamma) ^ {T} 1 + 1 ^ {T} \Gamma (\Sigma_ {2}) _ {N. n} \Gamma^ {T} 1 + 1 ^ {T} (\mathrm{I} + \Gamma)
$$

$$
\Sigma_ {\Delta} (\mathrm{I} + \Gamma) ^ {T} 1 + 1 ^ {T} \Gamma (\Sigma_ {2}) _ {\Delta} \Gamma^ {T} 1) ^ {0. 5} \}
$$

$$
\begin{array}{r l} \text {Let} a & = 1 ^ {T} (\mathrm{I} + \Gamma) \Sigma_ {2} (\mathrm{I} + \Gamma) ^ {T} 1 \\ b & = 1 ^ {T} \Gamma \Sigma_ {2} \Gamma^ {T} 1 \\ c & = 1 ^ {T} \Gamma (\Sigma_ {2}) _ {N, n} \Gamma^ {T} 1 \\ u & = 1 ^ {T} (\mathrm{I} + \Gamma) \Sigma_ {\Delta} (\mathrm{I} + \Gamma) ^ {T} 1 \\ v & = 1 ^ {T} \Gamma \Sigma_ {\Delta} \Gamma^ {T} 1 \\ w & = 1 ^ {T} \Gamma (\Sigma_ {2}) _ {\Delta} \Gamma^ {T} 1 \end{array}
$$

a, $b , c , u , v , w \geq 0 , b \geq c ,$ and $v \geq w .$ Thus, $H L ( ( a ~ + ~ b ~ + ~ u ~ + ~$ $v ) ^ { 1 / 2 } - ( a + c + v + w ) ^ { 1 / 2 } ) \geq H L ( ( a + b ) ^ { 1 / 2 } - ( a + c ) ^ { 1 / 2 } ) .$ (ii) Note that $\Gamma \geq 0$ implies that $\rho _ { \mathrm { i } } \geq 0$ for $i = 1 , 2 , \dots$ , N. Let $\Gamma _ { \Delta }$ ${ \bf \Phi } = { \Gamma } _ { 1 } - { \Gamma } _ { 2 } \ge 0 ,$ and $\Gamma _ { 1 } \geq \Gamma _ { 2 } \geq 0 .$ Again, we consider only $H L ( { \sqrt { a { \ + } \ b _ { 0 } } } \ - \ { \sqrt { a { \ + } \ b _ { n } } } )$ . We need to show that

$$
\{(1 ^ {T} (\mathrm{I} + \Gamma_ {2} + \Gamma_ {\Delta}) \Sigma (\mathrm{I} + \Gamma_ {2} + \Gamma_ {\Delta}) ^ {T} 1 + 1 ^ {T} (\Gamma_ {2} + \Gamma_ {\Delta})
$$

$$
\Sigma (\Gamma_ {2} + \Gamma_ {\Delta}) ^ {T} 1) ^ {1 / 2} - (1 ^ {T} (\mathrm{I} + \Gamma_ {2} + \Gamma_ {\Delta}) \Sigma (\mathrm{I} + \Gamma_ {2} + \Gamma_ {\Delta}) ^ {T} 1
$$

$$
+ 1 ^ {T} \left(\Gamma_ {2} + \Gamma_ {\Delta}\right) \Sigma_ {N. n} \left(\Gamma_ {2} + \Gamma_ {\Delta}\right) ^ {T} 1) ^ {1 / 2} \} \geq \left\{\left(1 ^ {T} (I + \Gamma_ {2}) \Sigma (I + \Gamma_ {2}) ^ {T} 1 \right. \right.
$$

$$
+ 1 ^ {T} \Gamma_ {2} \Sigma \Gamma_ {2} ^ {T} 1 + 2 1 ^ {T} (I + \Gamma_ {2}) \Sigma \Gamma_ {\Delta} ^ {T} 1 + 2 1 ^ {T} \Gamma_ {2} \Sigma \Gamma_ {\Delta} ^ {T} 1) ^ {1 / 2}
$$

$$
(1 ^ {T} (I + \Gamma_ {2}) \Sigma (I + \Gamma_ {2}) ^ {T} 1 + 1 ^ {T} \Gamma_ {2} \Sigma_ {N. n} \Gamma_ {2} ^ {T} 1 + 2 1 ^ {T} (I + \Gamma_ {2})
$$

$$
\Sigma \Gamma_ {\Delta} ^ {T} 1 + 2 1 ^ {T} \Gamma_ {2} \Sigma_ {N. n} \Gamma_ {\Delta} ^ {T}) ^ {1 / 2} \}
$$

$$
\begin{array}{r l} \text {Let} a & = 1 ^ {T} (\mathrm{I} + \Gamma_ {2}) \Sigma (\mathrm{I} + \Gamma_ {2}) ^ {T} 1 \\ b & = 1 ^ {T} \Gamma_ {2} \Sigma \Gamma_ {2} ^ {T} 1 \\ c & = 1 ^ {T} \Gamma_ {2} \Sigma_ {N, n} \Gamma_ {2} ^ {T} 1 \\ d & = 2 1 ^ {T} (\mathrm{I} + \Gamma_ {2}) \Sigma \Gamma_ {\Delta} ^ {T} 1 \\ e & = 2 1 ^ {T} \Gamma_ {2} \Sigma \Gamma_ {\Delta} ^ {T} 1 \\ f & = 2 1 ^ {T} \Gamma_ {2} \Sigma_ {N, n} \Gamma_ {\Delta} ^ {T} 1 \end{array}
$$

Because a, $b , c , d , e , f \geq 0 ,$ and $\Gamma _ { 1 } \geq \Gamma _ { 2 } \geq 0 ,$

$$
\begin{array}{l} \frac {\sqrt {a + b + d + e}}{\sqrt {a + c + d + f}} \geq \frac {\sqrt {a + b}}{\sqrt {a + c}} \\ \Rightarrow \frac {\sqrt {a + b + d + e} - \sqrt {a + c + d + f}}{\sqrt {a + c}} \\ \geq \frac {\sqrt {a + b} - \sqrt {a + c}}{\sqrt {a + c}} \Rightarrow \sqrt {a + b + d + e} \\ - \sqrt {a + c + d + f} \geq \sqrt {a + b} - \sqrt {a + c}. \end{array}
$$

(iii) It suffices to show that

$$
\begin{array}{r l} & \{(1 ^ {T} (I + \Gamma) \Sigma (I + \Gamma) ^ {T} 1 + 1 ^ {T} \Gamma \Sigma_ {N, n - t} \Gamma^ {T} 1) ^ {1 / 2} \\ & \quad - (1 ^ {T} (I + \Gamma) \Sigma (I + \Gamma) ^ {T} 1 + 1 ^ {T} \Gamma \Sigma_ {N, n} \Gamma^ {T} 1) ^ {1 / 2} \} \geq 0 \end{array}
$$

because

$$
\sum_ {i = 1} ^ {n} \frac {d _ {i}}{2 (1 - \rho_ {i})}
$$

is increasing in n. Therefore, it is sufficient to show that $1 ^ { T } \Gamma \Sigma _ { N . n - t }$ $\begin{array} { r } { \Gamma ^ { T } \boldsymbol { 1 } - \boldsymbol { 1 } ^ { T } \boldsymbol { \Gamma } \boldsymbol { \Sigma } _ { N , n } \boldsymbol { \Gamma } ^ { T } \boldsymbol { 1 } \geq \boldsymbol { 0 } , } \end{array}$ , or equivalently, $\Sigma _ { N . n - 1 } - \Sigma _ { N . n } \geq 0 ,$ which holds. Proofs for Propositions (4) and (5) follow directly from the expressions for $S _ { i }$ and $S _ { \mathbf { M } }$

Proof for Proposition 2. Note that

$$
\frac {S _ {M} - \overline {{S _ {M}}}}{\overline {{S _ {M}}}} = \sum_ {i = 1} ^ {n} \frac {d _ {i}}{2 (1 - \rho_ {i})} \bigg / L (\sqrt {a + b _ {0}} - \sqrt {a + b _ {n}}).
$$

The proof follows from the fact that $( \sqrt { a + b _ { 0 } } \ - \ \sqrt { a + b _ { n } } )$ is independent of $\Sigma _ { i = 1 } ^ { n } d _ { i } ,$ and $( { \sqrt { a } } \ + \ b _ { 0 } \ - \ { \sqrt { a } } \ + \ b _ { n } )$ is increasing in R as shown in Proposition 1.

Proof for Proposition 3. We can derive, using (4.8), (5.1), (5.2) and (5.3),

$$
\partial^ {2} S _ {M} / \partial n ^ {2} = \frac {(\partial b _ {n} / \partial n) ^ {2}}{4 (a + b _ {n}) ^ {3 / 2}} - \frac {\partial^ {2} b _ {n} / \partial b _ {n} ^ {2}}{2 \sqrt {a + b _ {n}}}.
$$

Substitution of (4.7) and (4.8) in the above equation, and algebraic manipulation yields the following expression Z to be negative for convexity and positive for concavity of $S _ { M } .$

$$
\begin{array}{l} Z = \rho^ {2} (4 N (n - 1) (1 + \rho^ {\prime}) ^ {2} - 4 (N - n) \rho^ {\prime 2} + (N - 1) \rho^ {\prime 2}) \\ \quad + \rho (4 (N - n) \rho^ {\prime 2} + 4 N (1 + \rho^ {\prime}) ^ {2} - (N - 2) \rho^ {\prime 2}) - \rho^ {\prime 2}. \end{array}
$$

It can be noted immediately that ${ \rho } = 1$ satisfies the condition for concavity, and ${ \mathfrak { p } } = 0$ satisfies the condition for convexity. Thus, the existence of q and is proved. q¯

We can also show that $\partial Z / \partial \rho > 0 .$ . Thus, if for an arbitrary $\underline { { \boldsymbol { \rho } } } , S _ { M }$ is convex, i.e., $Z < 0 ,$ then for any $\begin{array} { r } { \boldsymbol { \mathbf { \rho } } \mathbf { \rho } \mathbf { \leq } \mathbf { \rho } \mathbf { \rho } \mathbf { \rho } \mathbf { \rho } \mathbf { , } Z \mathbf { < } 0 , } \end{array}$ , also. Similarly, if, for an arbitrary q¯ , $S _ { M }$ is concave, i.e., $Z > 0 ,$ , then for any $\rho > \bar { \rho } , Z >$ 0, also.

## References

Anand, K., H. Mendelson. 1997. Information and organization for horizontal multimarket coordination. Management Sci. 43 1609– 1627.

Anderson, T. W. 1984. An Introduction to Multivariate Statistical Anal ysis, 2nd ed. John Wiley & Sons, Inc., New York.

Aviv, Y., A. Federgruen. 1998. The operational benefits of information sharing and vendor managed inventory (VMI) programs. Working paper, Washington University, St. Louis, MO.

Bakos, Y., E. Brynjofsson. 1993. From vendors to partners: Information technology and incomplete contracts in buyer-supplier relationships. J. Organ. Computing, 3 301–328.

Bourland, K., S. Powell, D. Pyke. 1996. Exploring timely demand information to reduce inventories. Eur. J. Oper. Res. 92 239–253.

Cachon, G., M. Fisher. 1997. Campbell Soup’s continuous replenish-

ment program: Evaluation and enhanced inventory decision rules. Production and Oper. Management. 6(3) 266–276.

—, ——. 1998. Supply chain inventory management and the value of shared information. Working paper, Wharton School, University of Pennsylvania, Philadelphia, PA.

Carbone, J. 1996. Solectron focuses on strategic buying. Purchasing. 121(7).

Clark, T. 1994a. Campbell Soup: A leader in continuous replenishment innovations. Harvard Business School Case, Boston, MA.

——. 1994b. Linking the grocery channel: Technological innovation, organizational transformation, and channel performance. Doctoral dissertation, Harvard Business School, Cambridge, MA.

——, J. Hammond. 1997. Reengineering channel reordering processes to improve total supply-chain performance. Production and Oper. Management. 6(3) 248–265.

Computer World. 1996. Sharing IS secrets: Retail project cuts supply chain costs.

Cramer, H. 1945. Mathematical Methods of Statistics, Princeton University Press, Princeton, NJ.

Gavirneri, S., R. Kapuscinski, S. Tayur. 1996. Value of information in capacitated supply chains. Working paper, GSIA, Carnegie Mellon University, Pittsburgh, PA.

Hammond, J. 1995. Barilla SpA (A), (B), (C), and (D). Harvard Business School Case, Cambridge, MA.

Hughes, J., M. Ralf, B. Michels. 1998. Transform Your Supply Chain, Thompson Publishing Company, New York.

Kurt Salmon Associates, Inc. 1993. Efficient consumer response: Enhancing consumer value in the grocery industry, Food Marketing Institute, Washington, D.C.

Lee, H. G., T. Clark, K. Y. Tam. 1999. Can EDI benefit adopters? Inform. Systems Res. 10(2) 186–195.

——, P. Padmanabhan, S. Whang. 1997. Information distortion in a supply chain: The bullwhip effect. Management Sci. 43 546–558.

——, K. C. So, C. S. Tang. 2000. The value of information sharing in a two-level supply chain. Management Sci. 46 626–643.

Malone, T. W., K. G. Crowston. 1994. The interdisciplinary study of coordination. ACM Comput. Surveys. 26(1) 97–119.

Markus, M. L. 1990. Toward a “critical mass” theory of interactive media. J. Fulk and C. Steinfeld, eds. Organizations and Communication Technology. Sage Publications, 194–218.

Moinzadeh, K., Y. Bassok. 1998. An inventory/distribution model with information sharing between the buyer and the supplier. Working paper, School of Business, University of Washington, Seattle, WA.

Mukhopadhyay, T., S. Kekre, S. Kalathur. 1995. Business value of information technology: A study of electronic data interchange. MIS Quart. 19(2) 137–155.

Riggins, F. J., T. Mukhopadhyay. 1994. Interdependent benefits from interorganizational systems: Opportunities from business partner reengineering. J. MIS. 11(2) 37–57.

Sarvary, M., P. M. Parker. 1997. Marketing information: A competitive analysis. Marketing Sci. 16 24–38.

Silver, E., R. Petersen. 1985. Decision Systems for Inventory Management and Production Planning, 2nd ed. John Wiley and Sons, New York.

Srinivasan, K., S. Kekre, T. Mukhopadhyay. 1994. Impact of electronic data interchange technology on JIT shipments. Management Sci. 40(10) 1291–1304.

Venkatraman, N. 1994. IT-enabled business transformation from automation to business scope redefinition. Sloan Management Rev. 35 73–78.

Verity, J. W. 1996. Clearing the cobwebs from the stockroom. Bus. Week. Oct. 21.

Wang, E. T. G., A. Seidmann. 1995. Electronic data interchange: Competitive externalities and strategic implementation policies. Management Sci. 41(3) 401–418.

Tridas Makhopadhyay, Associate Editor. This paper was received on September 30, 1999, and was with the authors 3 months for 2 revisions.
