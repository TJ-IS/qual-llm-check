---
otero_id: 12632
otero_key: "FBZ6H2U6"
title: "The Impact of Customer Valuation Uncertainty on Software Licensing"
authors: "Mingdi Xin"
year: "2020"
journal: "MIS Quarterly"
doi: "10.25300/misq/2020/14728"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# THE IMPACT OF CUSTOMER VALUATION UNCERTAINTY ON SOFTWARE LICENSING<sup>1</sup>

Mingdi Xin The Paul Merage School of Business, University of California, Irvine, Irvine, CA 92697 U.S.A. {Mingdi.xin@uci.edu}

This paper studies how an important feature of software adoption impacts a software vendor’s preference between perpetual and subscription-based licensing: Customers are uncertain about their valuation of the software prior to adoption. We show that customer valuation uncertainty causes the equilibrium outcome to depart from that of standard durable-goods theories in two aspects: (1) Contrary to the conventional wisdom of durable-goods theories that subscription-based licensing is optimal, perpetual licensing can be more profitable for the vendor than subscription-based licensing under some conditions. This result offers a possible explanation for the historical prevalence of perpetual licensing in many software markets. (2) When subscription-based licensing is optimal, our theory suggests a low-then-high variable pricing path. In contrast, standard durable-goods theories suggest charging the monopoly leasing price in each period. Such a variable pricing path and the resulting adoption pattern are consistent with market observations (e.g., pricing strategy by Adobe Systems). We also examine a variation of subscription-based licensing in which the vendor offers a menu of subscription options varying in license duration and shows that customer valuation uncertainty is critical for this strategy to outperform perpetual licensing under some conditions. Moreover, we find that customer valuation uncertainty can cause the vendor to prefer a licensing strategy that is not socially optimal.

Keywords: Software licensing, perpetual licensing, subscription-based licensing, customer valuation uncertainty

## Introduction

The optimal software licensing strategy has been an enduring topic both in academics and in business practice. Early research has studied software as a durable good, and their findings confirm a well-known result in the literature on durable-goods pricing: Subscription-based licensing is at least as profitable as perpetual licensing (Waldman 2003). Therefore, this literature recommends subscription-based licensing for software. For instance, Fudenberg and Tirole (1998) study pricing of successive generations of software and find that even though sales of upgrades or new versions help improve the profitability of perpetual licensing, perpetual licensing cannot be more profitable than subscription-based licensing. Stokey (1979) also cites software markets as a context and confirms the insights of standard durable-goods theories. More recent work has examined the effect of other demand factors. For instance, it is shown that uncertainty regarding the quality of future upgrades favors subscriptionbased licensing, although the findings on network effects are mixed (e.g., Chien and Chu 2008; Choudhary et al. 1998; Zhang and Seidmann 2010).

Nonetheless, in practice, perpetual licensing has been the predominant pricing model in software markets historically. In the enterprise software market, until the mid-2000s, perpetual licensing accounted for more than 92% of packaged software licenses held by client firms in North America and Europe (Wang 2006). In contrast, subscription-based licensing was rarely offered, and its revenue contribution was negligible for many software applications (Cusumano 2007). Why would software vendors not offer more subscriptions in the past, as predicted by theories?

Recent advances in web technologies enable software vendors to lease their software through the new Software-as-a-Service (SaaS) model. However, SaaS is more than a simple software subscription. It also includes web-based, centrally managed hosting services, which provide scalable usage capacity and improved efficiency arising from vendors’ economies of scale in managing the standard application. The new subscriptionbased SaaS model has seen double-digit growth in revenue in recent years and accounts for nearly 50% of the new license sales in the enterprise application software market in 2015 (Gartner 2015b).

Despite this growing interest, the revenue implication of this new subscription-based model for software vendors remains murky. On one hand, the main concern IT buyers have with a subscription model is that the price may increase over time so that it costs more over the long term to lease through subscriptions than to buy perpetual licenses for software products (IDC 2015). The strong growth in SaaS adoption, many argue, is not driven by lower software licensing fees, but by savings coming from customers’ not having to manage their own IT infrastructure and system maintenance (see Gartner 2015a). This implies that software vendors’ licensing revenue under SaaS can be higher than under perpetual licensing. On the other hand, many SaaS vendors increasingly forgo the pricing flexibility of subscription-based contracts and instead push customers to agree to multiyear commitments for using their software, which, ironically, resembles the characteristics of perpetual licensing (Dignan 2010; Wall Street Journal 2015).

This paper studies a software vendor’s optimal licensing strategy and demonstrates that an important feature of software adoption may explain the observed pricing practice and challenge the standard results of durable-goods theories: Software has features of an experience good; that is, customers are uncertain about the value of software products before using it (Shapiro and Varian 1998).

The difficulty of assessing the value of a software acquisition before use is well documented (Gross and Ginzberg 1984; Ulrich 2006). This value depends on the fit between users’ needs and the technology (e.g., the software’s functionality), both of which can be quite challenging to assess. Although users may understand their own needs, it can be a daunting task to translate these needs into software specifications that are necessary to evaluate a software product (Bubenko 1995). To understand a complex technology such as an enterprise system, one must understand abstract concepts and assumptions, logic and algorithms, and interdependence among subsystems. While this information is known to software vendors, they often cannot easily transfer such organizational know-how to their customers (Attewell 1992). Without a thorough understanding of users’ needs and the software system, customers face high uncertainty about the value of a software product prior to adopting it.

Customers may wish to reduce value uncertainty by attending product demos or pilot testing the software, but such learning is far from complete. Testing a software package in a controlled environment does not subject it to the complexity encountered in operational conditions. More often than not, users are unable to envision or predict all possible conditions that the software may be required to cover until they have gained substantial work experience with the system. Without perfect information, customers risk adopting software products that do not fit their needs. Approximately one half of all enter prise resource planning (ERP) projects fail to achieve the anticipated benefits (Robey et al. 2002). From office systems (Galletta 1986) to electronic commerce applications (Han and Noh 1999), we have witnessed many situations in which users are unable to generate value from seemingly very promising technologies. Given the high uncertainty of software adoption, many practitioners argue for subscription-based rather than perpetual licensing to reduce customers’ up-front financial commitment before the value of the software is learned (IDC 2012).

This paper studies a software vendor’s optimal licensing strategy when customers’ adoption decisions are characterized by such valuation uncertainty. Specifically, we consider a two-period model in which a unit mass of customers enters the market at the beginning of period 0 and stays in the market for two periods. Customers do not know their true valuation of the software prior to adoption. However, they may research the software, install a trial version, or pilot-test the software with a small number of users, which informs them of their valuation. This private knowledge is modeled as an informative signal that each customer receives on her own valuation. Customers learn their actual valuation after fully implementing and using the software. An up-front implementation cost is required to use the software. The vendor chooses either perpetual licensing or single-period subscription-based licensing for the software. We later extend the model to allow the vendor to offer a menu of subscription options varying in license duration (the MSO strategy) (see the “Extensions” section). This is a common strategy in the software industry, but has never been studied in prior literature. We also discuss the implications of our findings in the presence of network effects and verify the key findings of the two-period model in an infinite-period model.

We find that customer valuation uncertainty causes the equilibrium outcome to depart from that of standard durable-goods theories in two aspects: (1) Contrary to the conventional wisdom of durable-goods theories that subscription-based licensing is optimal, perpetual licensing can be more profitable for the vendor than subscription-based licensing under some conditions. (2) When subscription-based licensing is optimal, our theory suggests a low-then-high variable pricing path. In contrast, standard durable-goods theories suggest charging the monopoly leasing price in each period. Moreover, we find that customer valuation uncertainty is critical for the MSO strategy to outperform perpetual and singleperiod subscription-based licensing and can cause the vendor to prefer a licensing strategy that is not socially optimal. We discuss our contributions in the “Conclusions” section.

## Literature Review

This paper is related to two streams of literature: (1) the economics and marketing literature on durable-goods pricing, and (2) the literature on software pricing.

## Literature on Durable-Goods Pricing

Coase (1972) conjectured that the naïve policy of forever selling a durable good at a static monopoly price is not credible. After any initial quantity has been sold (to highvaluation consumers), the monopolist faces a truncated demand from relatively low-valuation consumers. He is then tempted to cut the price and generate additional sales. Rational consumers expect future prices to decline and, hence, are not willing to pay the monopoly price for buying the durable good early on, which hurts the monopolist’s overall profit, or the time-inconsistency problem. Leasing, on the other hand, is more profitable since leases expire at the end of each period, and so the monopolist faces the same demand in each period. He can then enforce the same monopolistic price for leasing his products in each period. The Coase conjecture was later verified by Bulow (1982), Stokey (1981), and Gul et al. (1986).

Subsequent research has largely focused on whether the Coase conjecture is robust to changes in assumptions. It is shown that the Coase conjecture is generally quite robust. Nonetheless, selling can be more profitable than leasing, if sold units depreciate at a significantly higher rate than leased units (Desai and Purohit 1998), or the vendor cannot monitor renters’ usage and maintenance efforts, creating an incentive to abuse rented products (Rust 1986), or consumers’ demand for the product fluctuates stochastically from period to period (Biehl 2001). More recent studies on durable-goods pricing have examined the profitability of selling versus leasing when a complementary product is sold by an independent firm (Bhaskaran and Gilbert 2005), or when the used-goods market is active (Rao et al. 2009; Johnson and Waldman 2010). Waldman (2003) provides a comprehensive survey of this literature.

Our paper differs from this literature in two aspects. First, we focus on a different demand factor that is relevant to software adoption, or experience good customer value uncertainty. Second, we expand the vendor’s pricing strategy space to allow the vendor to offer a menu of subscription options varying in license duration (the MSO strategy).

In particular, the experience good customer value uncertainty in our paper differs from the demand stochasticity in Biehl (2001). In Biehl, the durable good is not an experience good, and consumers know their current valuation of the product. Demand stochasticity randomly converts a fraction of the low end consumers to high-end consumers at the end of each period whether these consumers have adopted (bought or leased) the product or not. Indeed, having enough low-end consumers who have never bought the product convert to highend consumers in each period is key to Biehl’s findings as it entices the vendor to charge a high selling price subsequently, which resolves the time-inconsistency problem. In contrast, in our paper, new customers do not change their expected valuation of the software unless they have adopted the software through either a perpetual or subscription-based license (feature of an experience good). Thus, with perpetual licensing, after the high-end customers have bought the software, the vendor faces a truncated demand from low-end customers only. That is, we preserve the very demand features that cause the time-inconsistency problem. Prior literature has not studied the MSO strategy, even though seeking long-term commitment for software subscription is a common strategy employed by software vendors (Dignan 2010).

## Literature on Software Pricing

Pricing of software and services has been studied quite extensively, more often with a focus on usage-based pricing (see, for example, Balasubramanian et al. 2015; Gupta et al. 2001; Sundararajan 2004). Huang and Sundararajan (2005) study optimal pricing of usage-based on-demand computing, taking into account clients’ outside options and the vendor’s infrastructure cost structure. Jain and Kannan (2002) study the search-based versus subscription-fee pricing of online services. Jiang et al. (2007) examine the impact of piracy and network externality on a software vendor’s motivation to offer usagebased licensing. Ma and Seidmann (2015) model the competition between a software vendor that charges a fixed up-front fee for unlimited use of his software and a SaaS vendor that charges based on the number of transactions (i.e., usage-based pricing).

Only a few papers have examined term-based pricing (i.e., perpetual versus subscription-based licensing). Choudhary et al. (1998) study software licensing in a market with network effects and find that introducing leasing in the first period expands the user base and consequently improves the vendor’s profit in the second period. Zhang and Seidman (2010) study software licensing when buyers know the quality of the existing software, but not the quality of the future upgrade, and the market exhibits network effects. They find that such quality uncertainty favors leasing. August et al. (2014) study a software vendor’s incentive to offer on-premises versus the SaaS version, taking into account the security risks.

This paper differs from this literature in that, first, we consider a different demand factor (i.e., experience good customer value uncertainty). Second, we expand the vendor’s pricing strategy space to allow the vendor to offer a menu of subscription options varying in license duration.

This paper is also related to the software pricing literature that considers software as an experience good. This literature shows that when the value of software is unknown to customers prior to adoption, a software vendor may find it optimal to help customers learn their valuation under some conditions. For instance, to facilitate learning, a software vendor may allow a pirated version (Chellappa and Shivendu 2005), or offer a low-quality version with an option to upgrade in addition to the high-quality version (Wei and Nault 2012), or offer a time-locked or feature-limited free trial version (Dey et al. 2013; Niculescu and Wu 2014). This literature, however, does not consider the possibility of subscription-based licensing. Instead, it assumes that the software vendor follows common practice and only offers perpetual licensing. Our findings provide a theoretical justification for this assumption, as we show that perpetual licensing can be optimal given the nature of software as an experience good.

## Model

We consider a two-period game in the main model and verify the key findings in an infinite-period model in an extension. In the two-period model, at the beginning of period 0, a unit mass of new customers enters the market and lives for two periods. A monopoly software vendor offers a software product via either perpetual licensing or subscription-based licensing. Perpetual licensing allows a customer to use the software for the rest of her life, while subscription-based licensing allows a customer to use it for only one period. The vendor is assumed to be able to recognize his prior customers and, hence, is able to offer different prices to new and prior customers if it is profitable to do so. This is consistent with the empirical evidence showing that software vendors often treat new clients differently than their existing clients (Larkin 2008). Nonetheless, the main findings are not sensitive to this assumption.<sup>2</sup>

Customers are indexed by a type parameter, v, which represents the utility that a customer gains from using the software for one period after full implementation. There are two types of customers: a fraction â of the customers are high types with valuation $\nu = \nu _ { H } ,$ and a fraction $( 1 - \beta )$ are low types with valuation $\nu = \nu _ { { L } } \left( 0 < \nu _ { { L } } < \nu _ { { H } } \right)$ . A customer’s true type is unknown to her before she adopts the software. Nevertheless, she may conduct market research or pilot-test the software, through which she receives a signal y of her true type (or perceived valuation of the software), where $y = \nu _ { { } _ { H } } \mathbf { o r } \nu _ { { } _ { L } }$ . With probability ${ \bf \alpha } _ { \bf { \alpha } }$ the signal (or perceived valuation) is the same as her type, and with probability $( 1 - \alpha )$ , the signal is incorrect. á denotes the accuracy of customers’ signals (or their perception), and a sufficient condition that the signal be informative is

$$
P r [ v = v _ {H} | y = v _ {H} ] = \frac {\beta \alpha}{\beta \alpha + (1 - \beta) (1 - \alpha)} > \beta .
$$

That is, the posterior probability that one is the high-type (or low-type) given a high-type (or low-type) signal should be higher than the prior, which gives $a \in ( 1 / 2 , 1 ]$ . A customer learns her true type only after using the product for one period.

A customer incurs a fixed up-front cost to implement and use the software for the first time, denoted by c. It is assumed that there are no further adjustment costs in future period(s) after the software is implemented. Assume that $0 \leq c \leq \nu _ { L }$ The vendor and customers have the same discount factor ä. The marginal production cost of the software is constant at zero. To avoid discussing trivial cases, we assume that $\beta \nu _ { H } > \nu _ { L }$ 2 which implies that the number of high-type customers is not too low.<sup>3</sup>

The timing of the game is as follows. At the beginning of period $t = 0 ,$ one unit mass of new customers enters the market and receives private signals on their valuation of the software. The vendor first decides whether to offer his software via perpetual licensing or subscription-based licensing, and this decision does not change in future period(s). Next, he announces his price in the current period. Denote by $p _ { s , t }$ the price of perpetual licenses in period t and by $p _ { l , t }$ the price of subscription-based licenses in period t. We assume that the vendor cannot commit to future prices. Customers observe the price and make a purchase decision, anticipating their total payoff. Trade takes place. Customers who have bought or subscribed to the software then invest a fixed cost (c) to implement the software and learn their true valuation of the software. At the end of the period, the vendor observes the realized sales, although he does not know each customer’s private signal or type.

At the beginning of period $t = 1$ , if the vendor has chosen perpetual licensing in period 0, he announces a new price $p _ { s , t } .$ If the vendor has chosen subscription-based licensing in period 0, he announces one price for new subscription $p _ { l , t }$ and one for subscription renewal $r _ { t } .$ Customers who have not adopted the software or those who have subscribed to the software previously observe the prices and make a purchase decision. Trade takes place. Customers who are adopting the software for the first time invest a fixed cost to implement the software. Customers who have implemented the software previously can continue using the software if they have access to it in period 1. We are interested in characterizing the subgame perfect Nash equilibrium (SPNE) of the game.

A history in period t includes all past prices and realized sales. Both the vendor and customers remember the history of the game and their own actions. A customer’s strategy specifies an adoption decision in each period, given her history of observations and the current prices. The vendor’s strategy specifies a set of prices in each period, given the history of the game. Note that the vendor’s profit in period $t = 1$ is influenced only by the residual demand at the beginning of period t. This residual demand can be described by a vector of four variables: the measure of customers who receive the high-type (low-type) signal and have not adopted (i.e., bought or subscribed to) the software before period t, denoted by $x _ { H , n } ( t ) \left( x _ { L , n } ( t ) \right)$ , and the measure of customers who receive the high-type (low-type) signal and have subscribed to the software before period $t ,$ denoted by $x _ { H , l } ( t ) \left( x _ { L , l } ( t ) \right)$ . Denote the conditional probabilities $\mathrm { P r } ( \nu = \nu _ { i } \vert y = \nu _ { j } )$ by $\psi _ { i j } , i , j = H$ or L, and the probability that a customer receives the high-type (or low-type) signal when she enters the market $\mathrm { P r } ( y = \nu _ { H } )$ by $\psi ^ { H }$ (or $\operatorname* { P r } ( y = \nu _ { L } ) \log \psi ^ { L } )$ . Accordingly, the measure of customers who receive the high-type (or low-type) signal is $\psi ^ { H } ( \mathrm { o r } \psi ^ { L } ) . ^ { 4 }$ By definition, $x _ { i , j } ( t ) \geq 0 ( i = H \mathrm { o r } L , j = n$ or l) and $x _ { H , n } ( t ) +$ $x _ { H , l } ( t ) \ : \le \ : \psi ^ { H } , \ : x _ { L , n } ( \dot { t } ) + x _ { L , l } ( t ) \le \ : \psi ^ { L } .$ Table 1 summarizes the variables and their representation.

We assume that the vendor knows the aggregate demand state (as described by the vector of four variables) in each period in addition to the prices and realized sales in history. This may be a reasonable assumption since in a Nash equilibrium of the non-cooperative game, by definition, the vendor knows customers’ strategy profiles and can calculate the demand state in each period precisely, given the transaction history of the game. If individual customers deviate (i.e., off the equilibrium path), the demand state does not change since there is a continuum of customers. The vendor’s strategy, therefore, specifies a set of prices given each demand state.

This assumption is typical in the durable-goods literature and thus allows our results to be comparable to those in that literature. For instance, it is often assumed that after trade happens in each period, the seller knows the residual demand curve precisely, even though he cannot observe the willingness-topay (WTP) of those customers who have bought the product (Bulow 1982). In practice, it is common for software vendors to seek market-level demand information before determining their prices. IT analysts routinely conduct surveys and case studies on the outcome and value of enterprise software implementation (e.g., Band et al. 2010; Tan 2011). Software purchase intention is the focus of much IT market research (e.g., Harte-Hanks Technology Purchase Index, NPD Software Market Research).

In the following, we first consider a benchmark model in which customers know their true valuation of the software prior to adoption, or have no value uncertainty $( \mathrm { i } . \mathrm { e } . , \alpha \ = 1 )$ Second, we introduce customer value uncertainty (i.e., $1 / 2 <$ $\alpha < 1 )$ and examine its impact on the vendor’s optimal software licensing strategy. We then discuss the welfare implications. We examine the extensions to the main model in the “Extensions” section.

## A Benchmark Model Without Customer Valuation Uncertainty

This benchmark model can be seen as a special case of the original model in which $\alpha = 1$ . For consistency, the demand state is still described by $( x _ { H , n } ( t ) , x _ { H , l } ( t ) , x _ { L , n } ( t ) , x _ { L , l } ( t ) ) ;$ ; however, in this case, $x _ { i , n } ( t )$ (or $x _ { i , l } ( t ) )$ represents the measure of customers who are type-i and have never adopted (or have previously subscribed to) the software before period $t , i = H$ or $L .$ We first solve for the optimal pricing strategy under perpetual licensing and subscription-based licensing separately and then compare their profitability. Note that subscriptionbased licensing is equivalent to perpetual licensing in period 1, the final period. Thus, we simplify notation and denote by $p _ { 1 }$ the price for a one-period license for new customers in $t =$

<table><tr><td colspan="2">Table 1. Variables and Their Representation</td></tr><tr><td>Variable</td><td>Representation</td></tr><tr><td> $v$ </td><td>The utility a customer gains from using the software for one period</td></tr><tr><td> $\beta$ </td><td>The fraction of new customers who are high types with value  $v = v_{H}$ </td></tr><tr><td> $\alpha$ </td><td>The probability with which the signal is the same as the customer&#x27;s true type</td></tr><tr><td> $y$ </td><td>Signal on a customer&#x27;s true type,  $y = v_{H}$  or  $v_{L}$ </td></tr><tr><td> $c$ </td><td>Up-front implementation cost, $0 \leq c \leq v_{L}$ </td></tr><tr><td> $\delta$ </td><td>Common discount factor</td></tr><tr><td> $p_{s,t}$ </td><td>Price for perpetual licenses in period  $t$ </td></tr><tr><td> $p_{l,t}$ </td><td>Price for subscription-based licenses in period  $t$ </td></tr><tr><td> $r_{t}$ </td><td>Subscription renewal price in period  $t$ </td></tr><tr><td> $\psi_{ij}$ </td><td>Conditional probability of  $v = v_{i}$  given  $y = v_{j}$ , or  $\Pr(v = v_{i}|y = v_{j})$ ,  $i,j = L,H$ </td></tr><tr><td> $\psi^{i}$ </td><td>Fraction of new customers who receive signal  $v_{i}$ ,  $i = L,H$ </td></tr><tr><td> $E[v|i]$ </td><td>The expected utility of using the software for one period given  $y = v_{i}$ ,  $i = L,H$ . Or  $E[v|i] = E[v|y = v_{i}] = v_{H}\psi_{Hi} + v_{L}\psi_{Li}$ ,  $i = L,H$ </td></tr></table>

1. The results of this subsection show that subscription-based licensing is as profitable as perpetual licensing without customer valuation uncertainty.

When the software is sold via perpetual licensing only, a customer with valuation v who does not buy the software in period 0 buys the software in period 1 if the benefit from adoption is higher than the cost, or $\nu - c \geq p _ { 1 }$ . In period 0, a customer buys the software if the payoff from buying in period 0 is no less than that from buying for the first time in period 1 or from not buying the software at all, or

$$
(1 + \delta) v - c - p _ {s, 0} \geq \max \left\{\delta (v - c - E p _ {1}), 0 \right\}
$$

where $E p _ { 1 }$ represents the expected price in period 1.

The vendor’s optimal pricing strategy, given customers’ decisions, can be solved through backward induction. In period 1, a measure $x _ { H , n } ( 1 )$ of customers are willing to pay up to $\nu _ { H } - c$ for the software, and a measure $x _ { H , n } ( 1 ) + x _ { L , n } ( 1 )$ of customers are willing to pay up to $\nu _ { L } - c$ for the software. Thus, the vendor’s optimal strategy is to charge $p _ { 1 } = \nu _ { H }$ – c if

$$
x _ {H, n} (1) (v _ {H} - c) \geq (x _ {H, n} (1) + x _ {L, n} (1)) (v _ {L} - c)\tag{1}
$$

and $p _ { 1 } = \nu _ { { L } } - c$ otherwise. In period 0, the vendor specifies $p _ { s , 0 }$ to maximize his overall profit, given customers’ decisions. By comparing the vendor’s profit levels given different initial selling prices $( p _ { s , 0 } )$ , one can show that when $c \leq \nu _ { L } < \beta \nu _ { H } ,$ the unique SPNE of the game is characterized by the following strategy profile:

The vendor’s strategy: in period $0 , p _ { s , 0 } = \nu _ { H } + \delta \nu _ { L } - c ;$ in period 1, $p _ { 1 } = \nu _ { H } - c \mathrm { i f } ( 1 )$ holds, and $p _ { 1 } = \nu _ { { L } } - c$ otherwise.

A customer’s strategy: in period 0, buy i $\mathrm { f } p _ { s , 0 } \leq \nu - c + \delta \nu _ { L } ;$ otherwise, in period 1, buy if $p _ { 1 } \leq \nu - c .$

In equilibrium, high-type customers buy the software in period 0, and low-type customers buy the software in period 1. The vendor’s profit is $\beta ( \nu _ { H } + \delta \nu _ { L } - c ) + \delta ( 1 - \beta ) ( \nu _ { L } - c )$ This result confirms that of the durable-goods theories (i.e., Bulow 1982; Coase 1972): The vendor is tempted to cut the price and generate additional profit after any initial sales. Rational customers expect the future price to drop and are willing to pay less for the software up front. In equilibrium, this leads to a declining pricing path and a lower profit for the vendor (i.e., the time-inconsistency problem).

When the software is sold via subscription-based licensing only, a customer with valuation v who does not subscribe to the software in period 0 subscribes in period 1 if the benefit is higher than the cost, or $\nu - c \geq p _ { 1 }$ . A returning customer renews her subscription in period 1 if the benefit from renewing is higher than the cost, or v \$ r . A customer with valuation v subscribes to the software in period 0 if the payoff is no less than that of subscribing for the first time in period 1 or of not adopting at all. That is,

$$
v - c - p _ {l, 0} + \delta \max (0, v - E r _ {1}) \geq \max \left\{\delta \left(v - c - E p _ {1}\right), 0 \right\},
$$

where $E r _ { 1 }$ denotes the expected subscription renewal price in period 1.

The vendor’s optimal pricing strategy can be solved through backward induction. In period 1, a measure $x _ { H , l } ( 1 )$ of customers are willing to pay up to $\nu _ { H }$ for renewing their subscription, and a measure $x _ { H , l } ( 1 ) + x _ { L , l } ( 1 )$ of customers are willing to pay up to $\nu _ { L }$ for renewing their subscription. Thus, the optimal subscription renewal price $r _ { 1 } = \nu _ { H }$ if

$$
x _ {H, l} (1) v _ {H} \geq (x _ {H, l} (1) + x _ {L, l} (1)) v _ {L}\tag{2}
$$

and $r _ { 1 } = \nu _ { I }$ <sub>L</sub> otherwise. Similarly, the new subscription price in period $\mid p _ { 1 } = \nu _ { { \scriptscriptstyle H } } - c \mathrm { i f } ( 1 )$ holds, and $p _ { 1 } = \nu _ { { L } } - c$ otherwise. In period 0, the vendor specifies $p _ { l , 0 }$ to maximize his overall profit, given customers’ decisions. By comparing the vendor’s profit levels given different initial prices $( p _ { l , 0 } )$ , one can show that when $c \leq \nu _ { L } < \beta \nu _ { H } ,$ the unique SPNE of the game is characterized by the following strategy profile:

The vendor’s strategy: in period $0 , p _ { l , 0 } = ( 1 - \delta ) \nu _ { H } - c + \delta \nu _ { L } ;$ in period $1 , p _ { 1 } = \nu _ { H } - c \mathrm { i f } ( 1 )$ holds, and $p _ { 1 } = \nu _ { { L } } - c$ otherwise; $r _ { 1 } = \nu _ { \scriptscriptstyle H } \mathrm { i f } ( 2 )$ holds, and $r _ { 1 } = \nu _ { L }$ otherwise.

A customer’s strategy: in period 0, subscribe if $p _ { l , 0 } \leq \nu - c$ $+ \delta ( \nu _ { L } - \nu ) ;$ ; in period 1, having subscribed in period 0, renew if $\nu \geq r _ { 1 } ;$ ; having not subscribed previously, subscribe if $\nu - c$ $\geq p _ { 1 }$

In equilibrium, high-type customers subscribe to the software in period 0 and renew their subscription in period 1; low-type customers subscribe to the software in period 1. The vendor’s equilibrium profit is $\beta ( \nu _ { H } + \delta \nu _ { L } - c ) + \delta ( 1 - \beta ) ( \nu _ { L } - c )$

Evidently, perpetual licensing is as profitable as subscriptionbased licensing without customer valuation uncertainty. The following proposition formalizes this finding. All proofs are included in Appendix A.

Proposition 1. Without customer valuation uncertainty, perpetual licensing is as profitable as subscription-based licensing.

## A Two-Period Model with Customer Valuation Uncertainty

In this subsection, we consider the full model with customer valuation uncertainty: Customers do not know their true valuation of the software prior to adoption but receive a signal about it when they enter the market. They learn their valuation after using the software and incurring the one-time implementation cost c. Again, we first solve for the optimal pricing strategies under perpetual licensing and subscriptionbased licensing separately and then compare their profitability. The results of this subsection show that either perpetual licensing or subscription-based licensing can be optimal when customers face value uncertainty prior to adoption.

## Perpetual Licensing

When the software is sold via perpetual licensing only, a customer who receives signal y and does not buy the software in period 0 buys the software in period 1 if the expected benefit from adoption is higher than the cost, or $E [ \nu | \nu ] - c \geq$ $p _ { 1 }$ . In period 0, a customer buys the software if the expected payoff from buying in period 0 is no less than that from buying for the first time in period 1 or from not buying at all, or

$$
(1 + \delta) E [ v | y ] - c - p _ {s, 0} \geq \max \left\{\delta (E [ v | y ] - c - E p _ {1}), 0 \right\}.
$$

The vendor’s optimal pricing strategy, given customers’ decisions, can be solved in the same fashion as in the case without customer value uncertainty. Therefore, the detailed analysis is omitted for brevity. One can show that two alternative equilibrium outcomes are possible depending on the range of parameter values. In particular, define the following two pricing strategies:

The PS1 strategy: in period $0 , p _ { s , 0 } = E [ \nu | H ] + \delta E [ \nu | L ] - c ;$ in period 1, $p _ { 1 } = E [ \nu | H ] - c \mathrm { i f }$

$$
x _ {H, n} (1) (E [ v | H ] - c) \geq (x _ {H, n} (1) + x _ {L, n} (1)) (E [ v | L ] - c)\tag{3}
$$

and $p _ { 1 } = E [ \nu | L ] - c$ otherwise.

The PS2 strategy: in period $0 , p _ { s , 0 } \ = ( 1 + \delta ) E [ \nu | L ] - c ;$ in period 1, $p _ { 1 } = E [ \nu | H ] - c { \mathrm { ~ i f ~ } } ( 3 )$ holds, and $p _ { 1 } = E [ \nu | L ] - c$ otherwise.

Let $c _ { 1 } = E [ \nu | L ] - \psi ^ { H } E [ \nu | H ]$ . One can show that $c _ { 1 }$ decreases with á. When the signal is relatively accurate (á approaches $1 ) , c _ { 1 } \leq 0 $ , and the unique equilibrium outcome resembles that without customers’ value uncertainty: The vendor’s optimal pricing strategy in an SPNE is the PS1 strategy, which features a declining pricing path in equilibrium. Given these prices, customers who receive the high-type signal buy the software in period 0, and customers who receive the low-type signal buy the software in period 1. The vendor’s equilibrium profit is $\dot { \psi } ^ { H } ( E [ \nu | H ] - \mathbf { c } ) + \dot { \delta E [ \nu | L ] } - \delta \psi ^ { L } c$ . The same equilibrium outcome holds if the signal is noisy (and, hence, $c _ { 1 } > 0 )$ , but the implementation cost is not too low $( c _ { 1 } / ( ( 1 - \delta ) \psi ^ { L } ) :$ # $c \leq \nu _ { L } )$ . When the signal is noisy (and, hence, $c _ { 1 } > 0 )$ , and the implementation cost is low $( \mathrm { i . e . , ~ } 0 \le c < c _ { 1 } / ( ( 1 - \delta ) \psi ^ { L } )$ , the vendor’s optimal pricing strategy is the PS2 strategy. Given these prices, all customers buy the software as soon as they enter the market. The vendor’s equilibrium profit is (1 + $\delta ) E [ \nu | L ] - c .$

## Subscription-Based Licensing

When the software is sold via subscription-based licensing only, in period 1, a customer who receives signal y and does not subscribe to the software in period 0 subscribes for the first time if the expected benefit from adoption is higher than the cost, or $E [ \nu | y ] - c \geq p _ { 1 }$ A returning customer, after learning her valuation of the software v, renews her subscription in period 1 if the benefit from renewing is higher than the cost, or $\nu \geq r _ { 1 }$ . In period 0, a customer who receives signal y subscribes to the software if the expected payoff from subscribing in period 0 is no less than that from delaying adoption until period 1 or from not adopting at all, or

$$
\begin{array}{l} E [ v | y ] - c - p _ {l, 0} + \delta \max \{0, \psi_ {H y} (v _ {H} - E r _ {1}), E [ v | y ] - E r _ {1} \} \\ \geq \max \{0, \delta (E [ v | y ] - c - E p _ {1}) \}. \end{array}
$$

The vendor’s optimal pricing strategy, given customers’ decisions, can be solved in a similar fashion as in the case without customer value uncertainty. Therefore, the detailed analysis is omitted for brevity. One can show that two alternative equilibrium outcomes are possible in an SPNE depending on the range of parameter values. In particular, define:

The PL1 strategy: in period $0 , { p _ { l , 0 } } = ( 1 - \delta ) E [ \nu | H ] + \delta E [ \nu | L ]$ – c; in period 1 $, p _ { 1 } = E [ \nu | H ]$ – c if (3) holds; otherwise, $p _ { 1 } =$ $E [ \nu | L ] - c ; \ r _ { 1 } = \nu _ { H }$ if

$$
(x _ {H, l} (1) \psi_ {H H} + x _ {L, l} (1) \psi_ {H L}) v _ {H} \geq (x _ {H, l} (1) + x _ {L, l} (1)) v _ {L}\tag{4}
$$

otherwise, $r _ { 1 } = \nu _ { L }$

The PL2 strategy: in period $0 , p _ { l , 0 } = E [ \nu | L ] - c ;$ in period 1, $p _ { 1 } = E [ \nu | H ] - c \mathrm { i f } ( 3 )$ holds; otherwise, $p _ { 1 } = E [ \nu | L ] - c ; \ r _ { 1 } = \nu _ { H }$ if (4) holds; otherwise, $r _ { 1 } = \nu _ { L }$

Let $c _ { 2 } = ( 1 - \delta ) c _ { 1 } + \delta \beta ( 1 - \alpha ) \nu _ { H } ,$ . One can show that $c _ { 2 }$ also decreases with á. When the signal is relatively accurate (á approaches $1 ) , c _ { 2 } \leq 0$ , and the unique equilibrium outcome resembles that without customer value uncertainty: The optimal pricing strategy is the PL1 strategy. Given these prices, customers receiving the high-type signal subscribe to the software in period 0 and only renew their subscription in period 1 if their true types are the high type. Customers receiving the low-type signal subscribe to the software for the first time in period 1. The vendor’s equilibrium profit is $\psi ^ { H } ( E [ \nu | H ] + \delta E [ \nu | L ] - c - \delta \psi _ { L H } \nu _ { L } ) + \delta \psi ^ { L } ( E [ \nu | L ] - c )$

The same equilibrium outcome holds if the signal is noisy (and, hence, $c _ { 2 } > 0 )$ , but the implementation cost is not too low $( c _ { 2 } / ( ( 1 - \delta ) \psi ^ { L } ) \le c \le \nu _ { L } )$ . When the signal is noisy (hence, $c _ { 2 } > 0 )$ , and the implementation cost is low $( \mathrm { i . e . , 0 ~ } \leq$ $c < c _ { 2 } / ( ( 1 - \delta ) \psi ^ { L } ) )$ , the vendor’s optimal pricing strategy is the PL2 strategy. Given these prices, all customers subscribe to the software as soon as they enter the market, but they renew their subscription in period 1 only if their true types are the high type. The vendor’s equilibrium profit is E[v|L] – c $+ \delta \beta \nu _ { H } .$

## Profit Comparison and Welfare Analysis

Next, we compare the vendor’s profit under perpetual licensing with that under subscription-based licensing to examine whether customer value uncertainty changes the relative profitability of these two licensing schemes. Moreover, we compare the vendor’s preference between these two licensing schemes with the preference of customers or a social planner. We also investigate how customer valuation uncertainty and the up-front implementation cost impact the vendor’s profit and social surplus. Interestingly, our analysis shows that customer valuation uncertainty can increase or decrease total social surplus.

## Profit Comparison between Perpetual and Subscription-Based Licensing

Comparing the profitability of the two perpetual licensing strategies with that of the two subscription-based licensing strategies, we have the following results:

Proposition 2. With customer valuation uncertainty, perpetual licensing is more profitable than subscription-based licensing if either $( 1 - \delta ) E [ \nu | L ] + \delta \beta \nu _ { H } < \psi ^ { H } E [ \nu | H ] + ( 1 - \delta ) \psi ^ { L } c ,$ , or $\beta \nu _ { H } < E [ \nu | L ]$ . Otherwise, subscription-based licensing is more profitable, and the vendor’s optimal licensing strategy is the PL2 strategy.

Recall that without value uncertainty, subscription-based licensing is as profitable as perpetual licensing. The above results show that with value uncertainty, either perpetual licensing or subscription-based licensing is optimal depending on the range of parameter values. Indeed, if customers’ signals are uninformative, or $\alpha = 0 . 5 ,$ perpetual licensing is strictly more profitable than subscription-based licensing. Figure 1 illustrates the vendor’s optimal pricing strategy when the proportion of high-type customers $\beta = 0 . 3$ , the discount factor $\delta = 0 . 7 5$ , and the accuracy of the signal $\alpha = 0 . 8 3$ . Note that the relevant area is the area above the 45 degree line since $c \leq \nu _ { L }$

This result departs from that of standard durable-goods theories in two main aspects.

![](/api/attachments/FBZ6H2U6/fulltext/images/89489b4212e764ec30b6cd63f136994abd33e74017a109733056e57451b14539.jpg)  
Figure 1. Optimal Software Licensing Strategy with Customer Value Uncertainty

First, it shows that when customers face value uncertainty, perpetual licensing can be more profitable than subscriptionbased licensing for the vendor even if we preserve the key features of standard durable-goods models that cause perpetual licensing to be inferior to subscription-based licensing. Specifically, when the vendor offers perpetual licensing through the PS1 strategy, customers who receive the hightype signal buy the software in period 0. In period 1, the vendor faces a truncated demand from customers who receive the low-type signal and are willing to pay less for the software. The vendor then lowers his price to generate additional sales. Customers who receive the high-type signal anticipate the price to decline in the future and thus are willing to pay less for the software in period 0, which hurts the vendor’s profit (i.e., the time-inconsistency problem). In spite of this, perpetual licensing through the PS1 strategy can be more profitable than subscription-based licensing under certain conditions.

Second, standard durable-goods theories suggest that the optimal subscription-based licensing strategy is to charge the same monopolistic subscription price in each period (Biehl 2001; Bulow 1982). This no longer holds when customers face value uncertainty. For instance, when the vendor offers subscription-based licensing through the PL2 strategy, he offers a low introductory price to new customers in period 0 even if such a low price may not maximize his one-period monopoly profit. This introductory offer aims to incentivize customers to adopt the software and to learn their true valuation. He then raises the subscription renewal price in period 1. Such a variable pricing path, while unusual in standard durable-goods models, is largely driven by the nature of software as an experience good.

The intuition behind the above findings is as follows: Both customers and the vendor face a trade-off between perpetual licensing and subscription-based licensing. From customers perspective, subscription-based licensing provides the flexibility to make sequential adoption decisions as they implement and learn the value of the software. However, the price for subscription renewal may rise in the future, increasing the overall cost of licensing the software. With perpetual licensing, on the other hand, customers pay a fixed cost up front for using the software in perpetuity and thus avoid the possibility of a price increase in the future. However, they may adopt a software product that turns out to be a misfit.

From the vendor’s perspective, subscription-based licensing provides the flexibility to adjust prices over time as customers adopt and learn their true valuation of the software. Specifically, prior to adoption, customers’ expected valuation depends on the informative signal. After the initial subscription, some customers are willing to pay more, while others are only willing to pay less for the software after learning their true valuation. (Recall that $\nu _ { L } < E [ \nu | L ] < E [ \nu | H ] < \nu _ { H } ,$ for 0.5 $< a < 1 . )$ The vendor can raise the subscription renewal price in the subsequent period to take advantage of the improved WTP in the high-end market, although he would lose the demand from low-type customers.

With perpetual licensing, the vendor receives full payment up front and does not have the flexibility to adjust his prices for existing customers after they have learned their true types. He would also suffer from the time-inconsistency problem identified in standard durable-goods theories if his price in the initial period is discriminative (so that not all customers buy the software in the initial period). On the other hand, the distribution of customers’ perceived valuation of the software prior to adoption is less dispersed. (Recall that $\nu _ { L } < E [ \nu | L ] <$ $E [ \nu | H ] < \nu _ { H } ,$ for $0 . 5 < \alpha < 1 . )$ This reduction in demand heterogeneity can improve the vendor’s profit under perpetual licensing because, first, it reduces the detrimental effect of the time-inconsistency problem. Value uncertainty increases lowend customers’ expected valuation of the software. Thus, after high-end customers who receive the high-type signal have bought the software in period 0, in period 1, the vendor does not need to lower the price by much to sell to low-end customers who receive the low-type signal. This in turn improves high-end customers’ WTP for the software in period 0 and the vendor’s profit. Second, the vendor may be able to sell to more customers early on for using the software in perpetuity albeit at a moderate price to account for the risk of adoption.

Overall, the vendor needs to trade off his gains and losses from perpetual licensing with those from subscription-based licensing. Our results show that when the vendor’s gain from a flexible pricing schedule is not substantial, perpetual licensing is more profitable than subscription-based licensing.

## Perpetual Versus Subscription-Based Licensing: From Social Planner and Customers’ Perspective

Does the vendor’s preference between perpetual and subscription-based licensing differ from that of a social planner or a customer? In this subsection, we compare the social and consumer surplus under the optimal perpetual licensing strategy with those under the optimal subscriptionbased licensing strategy. We show that customer value uncertainty can cause the vendor to choose a licensing strategy that is suboptimal from a social planner or customer’s perspective. The following proposition summarizes our findings.

Proposition 3. Without customer valuation uncertainty, total social surplus and consumer surplus under perpetual licensing are the same as those under subscription-based licensing.

With customer valuation uncertainty:

If the optimal perpetual licensing strategy is the PS1 strategy, and the optimal subscription-based licensing strategy is the PL1 strategy, total social surplus is higher under perpetual licensing, and consumer surplus is the same under both licensing strategies.

If the optimal perpetual licensing strategy is the PS1 strategy, and the optimal subscription-based licensing strategy is the PL2 strategy, total social surplus is higher under perpetual licensing $i f \psi ^ { H } E [ \nu | H ] - \delta \beta \nu _ { H } + ( 1 - \delta ) \psi ^ { L } c$ $> ( 1 - \delta ) ( \beta \nu _ { H } + ( 1 - \beta ) \nu _ { L } ) ;$ otherwise, it is higher under subscription-based licensing. Consumer surplus is higher under subscription-based licensing.

If the optimal perpetual licensing strategy is the PS2 strategy, both total social surplus and consumer surplus are higher under perpetual licensing.

Recall that without customer value uncertainty, perpetual and subscription-based licensing are equally profitable to the vendor. Therefore, without customer value uncertainty, the vendor’s preference between perpetual and subscription-based licensing is the same as that of a social planner or a customer.

With customer value uncertainty, however, the vendor’s preference may differ from that of a social planner or a customer. Figure 2 shows an example that contrasts the vendor’s preference (marked by V) with that of a customer (marked by C). Figure 3 contrasts the vendor’s preference with that of a social planner (marked by S). Figures 2a and 3a use the same parameter values as Figure 1 to facilitate comparison with early results. Figures 2b and 3b show how the preferences of the vendor, social planner, and customers change with the accuracy of the signal (á).

According to Figures 2b and 3b, when á is close to 1/2, the vendor, social planner, and customers all prefer perpetual licensing. When á is close to 1, the vendor and social planner prefer perpetual licensing, and customers are indifferent between perpetual and subscription-based licensing. When á is intermediary, however, the vendor’s preference may differ from that of a social planner or a customer. According to Figures 2a and 3a, the vendor’s preference may differ from that of a social planner or a customer when the implementation cost is relatively high, and the high- and low-type customers have relatively different valuation of the software. These results suggest that a social planner that wishes to maximize social surplus should look carefully at those software markets, in which the difficulty of evaluating a software product before use is intermediary, or the implementation cost is high, and the high- and low-type customers have relatively different valuation of the software.

## Impact of Customer Value Uncertainty on Social Surplus and Vendor Profit

In this subsection, we investigate how customer value uncertainty impacts social surplus and the vendor’s profit. Our findings show that customer value uncertainty can increase or decrease total social surplus. The following proposition formalizes these results.

Proposition 4. Impact of Customer Valuation Uncertainty on Social Surplus. Relative to the case without customer valuation uncertainty, social surplus is improved when á is small so that the vendor’s optimal pricing strategy is the PS2 or PL2 strategy. In contrast, social surplus is lower when á is large so that the vendor’s optimal pricing strategy is the PS1 strategy.

![](/api/attachments/FBZ6H2U6/fulltext/images/07b11e91f2dc24c9e32745f7877fcfd936a1a015433a76aa6c14b8c2af3596f9.jpg)  
(a) For $\beta = 0 . 3 , \delta = 0 . 7 5 , v _ { { \scriptscriptstyle H } } = 1 , \alpha = 0 . 8 3$

![](/api/attachments/FBZ6H2U6/fulltext/images/ffb5bb425f176a154a3836f427363542e1b77793ed6b34767341a2e3d264d827.jpg)  
(b) For $\beta = 0 . 3 , \delta = 0 . 7 5 , v _ { { \scriptscriptstyle H } } = 1 , v _ { { \scriptscriptstyle L } } = 0 . 2$

Figure 2. Compare the Vendor’s Preference (V) with Customers’ Preference (C)  
![](/api/attachments/FBZ6H2U6/fulltext/images/54d914e02d5ed4598025ac65c32abf7f22af4aa966701745513c6351721b906c.jpg)  
(a) For $\beta = 0 . 3 , \delta = 0 . 7 5 , v _ { { \scriptscriptstyle H } } = 1 , \alpha = 0 . 8 3$

![](/api/attachments/FBZ6H2U6/fulltext/images/f67b4e8f9fec99763ad118b2e46d6f5e56da4114b89f16bdde13d770df725322.jpg)  
(b) For â = 0.3, ä = 0.75, v = 1, v = 0.2  
Figure 3. Compare the Vendor’s Preference (V) with a Social Planner’s Preference (S)

Recall that without customer value uncertainty, in equilibrium, high-type customers adopt the software in both periods, while low-type customers adopt the software only in period 1. Since the marginal cost of software is zero, social surplus can be improved when more customers adopt the software sooner rather than later.

When the accuracy of the signal á is low, customers who receive the high- and low-type signals have similar expected valuation of the software. The vendor finds it optimal to lower his price in period 0 so that all customers adopt the software right away (the PS2 or PL2 strategy), which improves social surplus. In contrast, when the accuracy of the signal is high, customers who receive the high- and low-type signals have very different expected valuation of the software. When the PS1 strategy is optimal, in equilibrium, only customers who receive the high-type signal buy the software in period 0, and those who receive the low-type signal buy the software in period 1. Value uncertainty causes some customers whose true type is the high-type to delay adoption since they (incorrectly) perceive the software to be less valuable. This hurts social surplus.

Since customer value uncertainty may hurt social surplus when á is relatively high, is the vendor motivated to change the accuracy of the signal? The following proposition shows that customer value uncertainty can increase or decrease the vendor’s profit. Figure 4 shows an example of how the vendor’s equilibrium profit may change with á.

Proposition 5. Impact of Customer Valuation Uncertainty on the Vendor’s Profit. When the PS2 or PL2 strategy is optimal, the vendor’s profit decreases with á. When the PS1 strategy is optimal, his profit increases with á when

$$
\begin{array}{c} {c (2 \beta - 1) (\delta - 1) (- 2 \alpha \beta + \alpha + \beta) ^ {2} +} \\ {(- 2 \alpha \beta + \alpha + \beta) ^ {2} (\beta v _ {H} + (\beta - 1) v _ {L}) > (1 - \beta) \beta \delta (v _ {H} - v _ {L})} \end{array}
$$

and decreases with á otherwise.

![](/api/attachments/FBZ6H2U6/fulltext/images/3afc67b3b4a4fe635494efa2b56fae11bedae1e6574f03fe66c542171992c628.jpg)

![](/api/attachments/FBZ6H2U6/fulltext/images/d3e3d9c193b48738a86017374062642aa236cbfb2f04bb9e79eba065930d98d0.jpg)  
Figure 4. The Vendor’s Profit Given v = 10, v = 1.5, â = 0.3, c = 1, ä = 0.85 (Left) or v = 10, v = 1.5, â = 0.3, c = 1, ä = 0.35 (Right)

When the signal is relatively accurate (á is large), the vendor’s optimal pricing strategy is the PS1 strategy, and his profit is $\psi ^ { H } ( E [ \nu | H ] - c ) + \delta ( E [ \nu | L ] - \psi ^ { L } c )$ , which may increase or decrease with the accuracy of the signal (á) due to two opposing forces:

First, customers who receive the high-type signal have a higher valuation of the software the more accurate the signal is, which can improve the vendor’s profit. Second, these customers’ WTP for buying the software in period 0 is also determined by the anticipated price in period 1 $( p _ { 1 } )$ . Since $p _ { 1 }$ targets customers receiving the low-type signal, it decreases as the signal becomes more accurate (or á increases).

As á increases, these two forces drive the vendor’s profit in opposite directions. The overall effect of customer value uncertainty on the profitability of the PS1 strategy depends on the discount factor (ä) and the demand distribution. When the discount factor ä is small, or high-type customers represent the majority of the customers $( \beta$ close to 1), both customers and the vendor’s payoffs rely less on the outcome in the future period. In this case, the vendor’s profit increases with $^ { a , }$ and he prefers more accurate signals. When the discount factor ä is close to 1, both customers’ and the vendor’s payoffs rely more on the outcome in the future period. In this case, the vendor’s profit decreases with á when the demand distribution is such that the proportion of high-type customers â is not too close to 1.<sup>5</sup> The vendor in these markets prefers less accurate signals (smaller á).

<sup>5</sup>One can show that

$$
\frac {\partial (E [ v | L ] - \psi^ {L} c)}{\partial \alpha} > 0 \Leftrightarrow \left(v _ {H} - v _ {L}\right) (- 1 + \beta) \beta > c (1 - 2 \beta) (\alpha + \beta - 2 \alpha \beta) ^ {2}
$$

## Role of the Up-Front Implementation Cost

The up-front implementation cost lowers customers’ WTP for the software. Thus, it hurts the vendor’s profit whether he sells perpetual or subscription-based licenses, because the vendor needs to subsidize customers’ adoption through lower prices. The cost of the subsidy is higher when more customers adopt the software sooner in equilibrium, since the vendor incurs more of the cost up front rather than spreads it over time. Therefore, a high up front implementation cost discourages the vendor from lowering his price in period 0. Instead, the vendor finds it optimal to raise the initial price so that only those customers who perceive the software as highly valuable adopt the software in the first period (i.e., the PS1 strategy).

Furthermore, subscription-based licensing is not optimal unless the implementation cost is not too high (e.g., Figure 1). As the implementation cost increases, subscription-based licensing becomes more costly to the vendor. This is because he has to subsidize more heavily in the initial subscription, while only a fraction of the initial adopters is willing to renew their subscription at a higher price later on. The following proposition formalizes these results.

Proposition 6. The vendor’s equilibrium profit decreases with the implementation cost (c) whether he sells the software through perpetual or subscription-based licensing. The vendor’s profit decreases faster with c if his pricing strategy is such that all rather than a subset of new customers adopt (subscribe to or buy) the software in the first period, or mathematically

$$
\frac {\partial \pi_ {i}}{\partial c} <   0, f o r i = P S 1, P S 2, P L 2, a n d
$$

$$
\frac {\partial \pi_ {P S 1}}{\partial c} > \frac {\partial \pi_ {P S 2}}{\partial c} = \frac {\partial \pi_ {P L 2}}{\partial c}.
$$

## Discussion

Our findings shed light on some observed pricing practice in the software industry.

First, our results show that whether perpetual licensing or subscription-based licensing is optimal for the vendor depends on the nature of the software product. Perpetual licensing is optimal for software products that are difficult to evaluate prior to use or those that require relatively high implementation costs. Consistent with our findings, perpetual licensing is the dominant licensing form for many complex enterprise software products (e.g., ERP packages) (Norton and Boulton 2014). These enterprise software systems are difficult to evaluate prior to full implementation, and implementation is often very costly. A typical ERP installation costs about \$15 million (O’Leary 2000).

On the other hand, according to our model, subscription-based licensing is optimal for software products that either are easy to evaluate prior to adoption or require relatively low implementation costs. Two such examples are statistics and PC productivity software. Statistics software is relatively easy to evaluate, as the algorithms implement well-established statistical procedures known to its users. Consistent with our prediction, statistics software (e.g., SAS) has traditionally been sold via subscription contracts. Microsoft’s PC productivity software (e.g., Microsoft Office) requires no or little implementation effort from users because it is usually pre-installed by PC suppliers or can be easily and cheaply installed on customers’ premises. PC productivity software can also be easily evaluated by users. Consistent with our prediction, Microsoft has had a long history of offering the enterprise subscription program for its PC productivity software.

Second, we show that given customer value uncertainty, when subscription-based licensing is optimal, the optimal prices are not the monopoly price in each period, as standard durablegoods theories suggest, but follow a low-then-high variable pricing path. The vendor lowers the initial price to attract new customers and help them learn their true valuation of the software. The subscription renewal price is high as the vendor finds it optimal to only serve high-end customers in the long run.

Consistent with our findings, after Adobe Systems moved to offer its creative software suite via the subscription-based SaaS model in 2013, it offers a 40% discount to new customers for the first year subscription before raising the price upon subscription renewal. According to a CNET survey, such a deep discount has attracted a large number of new customers. Nonetheless, many of them do not plan to renew their subscription after the first year, contributing to a high customer churn rate (Shankland 2014).

Finally, in Appendix C, we compare customer valuation uncertainty with usage volume uncertainty and show that they have very different revenue implications for the vendor. Whereas customer valuation uncertainty changes the relative profitability of perpetual and subscription-based licensing, usage volume uncertainty does not. Interested readers are referred to Appendix C for details.

## Extensions

## A Menu of Subscription Options Varying in License Duration

A variation of the standard subscription-based licensing is that the software vendor sells multi-period subscriptions in addi tion to single-period subscriptions. That is, customers can commit to subscribe to the software for one period or two periods, etc., and the per-period subscription price is fixed for the duration of the commitment. For instance, some SaaS vendors are reportedly pushing customers to agree to multiyear commitments for leasing their software (Dignan 2010; Wall Street Journal 2015). Can software vendors improve their profit beyond their optimal profit from perpetual licensing or single-period subscription-based licensing by offering a menu of subscription options varying in subscription duration and price (or the MSO strategy)?

In this section, we investigate this question by considering an extension in which the vendor can offer subscription-based licensing through the MSO strategy. In particular, in period $0 ,$ the vendor offers two types of subscription contracts: A customer can subscribe to the software for one period at the price of ${ \dot { p } } _ { l 1 , 0 } ,$ or for two periods at the price of ${ \dot { p } } _ { l 2 , 0 } .$ . The price covers usage for two periods, and this is equivalent to the customer committing to paying $p _ { l 2 , 0 } / ( 1 + \delta )$ in each period. In period 1, if a customer’s single-period subscription has expired, she can renew her subscription at the price of $r _ { 1 } .$ . If a customer has never adopted the software previously, she can buy a new single-period subscription at the price of $\dot { p } _ { 1 } .$ . We solve for the vendor’s optimal pricing strategy under the MSO strategy.

Evidently, perpetual licensing and single-period subscription are special cases of the MSO strategy in which only one type of term-based contract is effective in equilibrium. For instance, single-period subscription is a special case of the MSO strategy in which only the one-period subscription options are effective in equilibrium—no customer would buy the two-period subscription in period 0. To keep the terminology consistent throughout the paper, we label those MSO strategies in which only one type of term-based contract is effective in equilibrium, perpetual licensing or single-period subscription, depending on which type of contract is effective. We shall focus on solving for those MSO strategies in which more than one type of term-based contract is effective in equilibrium.

We first solve the case with customer valuation uncertainty and then discuss the case without valuation uncertainty as a special case in which $\alpha = 1$ Our findings show that the presence of customer valuation uncertainty is critical for the MSO strategy to outperform perpetual licensing and singleperiod subscription-based licensing strategies. Nonetheless, perpetual licensing can still be optimal under certain conditions. We discuss the intuition behind the findings at the end.

When customers face value uncertainty, in period 0, a customer’s expected benefit from subscribing to the software for two periods is $( 1 + \delta ) E [ \nu \vert y ] - c - p _ { l 2 , 0 } ;$ that from a one-period subscription is

$$
E [ v | y ] - c - p _ {l l, 0} + \delta \cdot \max \{0, \psi_ {H y} (v _ {H} - E r _ {1}), E [ v | y ] - E r _ {1} \};
$$

that from delaying adoption until period 1 is $\delta ( E [ \nu | y ] - E p _ { 1 } )$ A customer chooses the option that maximizes her expected payoff. If a customer is indifferent between the two-period and one-period subscription, then she is assumed to buy the two-period subscription.<sup>6</sup>

Note that in period 0, a two-period subscription is more desirable than a one-period subscription for customers who receive the high-type signal compared to those who receive the low-type signal. This is because the difference in payoff between adopting the two- and one-period subscription, or

$$
\begin{array}{c} (1 + \delta) E [ v | y ] - c - p _ {l 2, 0} \\ - [ E [ v | y ] - c - p _ {l 1, 0} + \delta \cdot \max \{0, \psi_ {H y} (v _ {H} - E r _ {1}), E [ v | y ] - E r _ {1} \} ] \end{array}
$$

is nondecreasing in y. Intuitively, when offered both options, customers who perceive the software as highly valuable prefer long-term subscription since they are more likely to continue using the software, and long-term subscription fixes future prices for longer periods of time and allows these customers to avoid the possibility of rising subscription renewal prices in the future. Customers who do not perceive the software as highly valuable, on the other hand, value short-term subscription more as it allows them to revise their adoption decisions once they have more information about their true valuation of the software after the initial use. Thus, the adoption base for the long-term (two-period) subscription in period 0 satisfies a monotonicity property: If customers who receive the lowtype signal find it optimal to adopt, then customers who receive the high-type signal also find it optimal to buy the long-term subscription.

The vendor’s optimal pricing strategy, given customers’ decisions, can be solved via backward induction. One can show that there is a unique MSO strategy under which more than one type of term-based contract is effective in equilibrium. Define:

The MPS (Multi-Period Subscription) strategy: in period $0 , p _ { l 2 , 0 } = \delta E [ \nu | H ] + E [ \nu | L ] - c , p _ { l 1 , 0 } = E [ \nu | L ] - c ;$ in period 1, $p _ { 1 } = E [ \nu | H ] - c \mathrm { i f } ( 3 )$ holds; otherwise, $p _ { 1 } = E [ \nu | L ] - c ; r _ { 1 } = \nu _ { H }$ if (4) holds; otherwise, $r _ { 1 } = \nu _ { L } .$

The following proposition shows that with customer valuation uncertainty, the MPS strategy can be more profitable than perpetual licensing or single-period subscription if the high and low-type customers’ valuations are very different, and the implementation cost is relatively low. Let $b _ { 1 } = ( \beta - \psi _ { H L } ) /$ $( \psi _ { L L } - ( 1 - \alpha ) ( 1 - \beta ) )$ . One can show that there is a unique á $\in ( 1 / 2 , 1 )$ that solves $\beta - \psi _ { H L } = \psi _ { H L } \psi _ { L L }$ . Define $\alpha _ { 1 }$ to be this solution.

Proposition 7. When customers face valuation uncertainty:

Case 1. When customers’ signals are noisy, or $1 / 2 < a \le a _ { 1 }$

The MPS strategy is optimal $i f 0 < \nu _ { L } / \nu _ { H } < \operatorname* { m i n } { ( b _ { 1 } , \psi _ { H L } ) }$ and $0 \leq c < c _ { 2 } / ( ( 1 - \delta ) \psi ^ { L } )$ . In equilibrium, customers who receive the high-type signal subscribe to the twoperiod contract in period 0. Customers who receive the low-type signal subscribe to the one-period contract in period 0 and renew their subscription in period 1 only if their true types are the high type. The vendor’s overall profit is $\delta \dot { \psi } ^ { \bar { H } } E [ \nu | H ] + E [ \nu | \bar { L } ] - c + \delta \psi ^ { L }$ ø<sub>HL</sub>v<sub>H</sub>.

• The PS1 strategy is optimal if $\psi _ { H L } \ \leq \ \nu _ { L } / \nu _ { H } < \beta$ and $c _ { 1 } / ( ( 1 - \delta ) \psi ^ { L } ) \leq c \leq \nu _ { L } ; o r 0 < \nu _ { L } / \nu _ { H } < \psi _ { H L }$ and max $( c _ { 1 } ,$ $c _ { 2 } ) / ( ( 1 - \delta ) \psi ^ { L } ) \leq c \leq \nu _ { L } .$

The PS2 strategy is optimal if min $( b _ { 1 } , \psi _ { H L } ) \leq \nu _ { L } / \nu _ { H } < \beta$ and $0 \leq c < c _ { 1 } / ( ( 1 - \delta ) \psi ^ { L } )$

Case 2. When customers’ signals are relatively accurate, or $\alpha _ { 1 } < \alpha < 1$

The MPS strategy is optimal $i f 0 < \nu _ { L } / \nu _ { H } < \psi _ { H L }$ and $0 \leq c$ $< m a x ( c _ { 2 } , 0 ) / ( ( 1 - \delta ) \psi ^ { L } )$

The PS1 strategy is optimal $i f 0 < \nu _ { L } / \nu _ { H } < \psi _ { H L }$ and max $( 0 , \ c _ { 2 } ) / ( ( 1 \ - \ \delta ) \psi ^ { L } ) \ \leq \ c \ \leq \ \nu _ { L } ;$ or $\psi _ { H L } \leq \nu _ { L } / \nu _ { H } < \beta$ and max $\big ( c _ { 1 } , c _ { 1 } + \delta ( \beta \nu _ { H } - E [ \nu | L ] ) \big ) / ( ( 1 - \delta ) \psi ^ { L } ) \leq c \leq \nu _ { L } .$

The PS2 strategy is optimal if $( \beta - \psi _ { H L } ) / \psi _ { L L } \leq \nu _ { L } / \nu _ { H } < \beta$ and $0 \leq c \leq$ max $( c _ { 1 } , 0 ) / ( ( 1 - \delta ) \psi ^ { L } )$

• The PL2 is optimal if $\psi _ { H L } \leq \nu _ { L } / \nu _ { H } < ( \beta - \psi _ { H L } ) / \psi _ { L L }$ and $0 \leq c < \big ( c _ { 1 } + \delta ( \beta \nu _ { H } - E [ \nu | L ] ) \big ) / ( ( 1 - \delta ) \psi ^ { L } ) .$

The case without customer value uncertainty can be analyzed in a similar way. Detailed analysis is in the Appendix. We show that without customer valuation uncertainty, subscription-based licensing through the MSO strategy does not improve the vendor’s profit beyond that of perpetual licensing or single-period subscription-based licensing. The following proposition formalizes this finding.

Proposition 8. Without customer valuation uncertainty, the vendor’s optimal pricing strategy under MSO is such that in equilibrium $p _ { l 2 , 0 } = \nu _ { H } - \mathbf { c } + \delta \nu _ { L } , p _ { l 1 , 0 } = \nu _ { H } - \mathbf { c } - \delta ( \nu _ { H } - \nu _ { L } ) , r _ { 1 } =$ $\nu _ { H } , p _ { 1 } = \nu _ { L } - c .$ The vendor’s optimal profit is

$$
\beta (v _ {H} - \mathfrak {c} + \delta v _ {L}) + \delta (1 - \beta) (v _ {L} - c)
$$

The MSO strategy is as profitable as perpetual licensing only or single-period subscription-based licensing only.

The intuition behind these findings is as follows. Without customer value uncertainty, the MSO strategy subjects the vendor to the same time-inconsistency problem that hurts his profit under perpetual licensing, and so the MSO strategy is as profitable as perpetual licensing. In particular, high-type customers prefer long-term to short-term subscription (weakly) more than low-type customers (see proof of Proposition 8). Once high-type customers have bought the longterm subscription, the vendor faces a truncated demand with lower WTP for the short-term subscription. He then charges a low price for the short-term subscription. High-type customers anticipate low short-term subscription prices and thus are willing to pay less for the long-term subscription in period 0, which hurts the vendor’s profit.<sup>7</sup>

When customers face value uncertainty, customers receiving the high-type signal also prefer long-term to short-term subscription (weakly) more than customers receiving the lowtype signal. The key difference here is that after customers who receive the low-type signal have subscribed to and used the software for one period (via single-period subscription), they learn their true types. Some of them are then willing to pay more, while others are only willing to pay less for subscription renewal. When there is enough high-end demand, the vendor finds it optimal to charge a high price for singleperiod subscription renewal. Anticipating this high price for single-period subscription in the future, customers who receive the high-type signal are willing to pay more for longterm subscription in period 0, which alleviates the timeinconsistency problem, making the MSO strategy more profitable than perpetual licensing under certain conditions. The MSO strategy can also outperform single-period subscription-based licensing, because it allows the vendor to sort customers based on their perceived valuation through a menu of subscription options varying in subscription duration and price.

Nevertheless, perpetual licensing can still be optimal. This is because with the MSO strategy, to induce customers receiving the low-type signal to adopt the one-period subscription in period 0, the vendor has to offer this option at a lower price, which cannibalizes his profit from the long-term subscription. Although the vendor can raise the subscription renewal price in period 1, he loses some demand as a result of discriminative pricing. Figure 5 illustrates the region in which offering MSO through the MPS strategy, or perpetual licensing, or single-period subscription-based licensing is optimal.

## Network Effects

Many software products display positive network effects. That is, the utility from using the software increases with the size of the adoption base. In this section, we discuss the implications of our findings in the presence of network effects. In particular, we consider an extension in which the utility that a customer gains from using the software is the sum of the software’s basic utility (i.e., v if valuation is known or E[v|y] if valuation is unknown) and the network benefit. The network benefit is equal to the product of the network size (x) and the intensity of network effects (e). Again, we focus on the SPNE of the game.

It is well-known that models of network goods tend to have multiple equilibria. This makes a profitability comparison between perpetual and subscription-based licensing difficult, since the vendor can have multiple equilibrium pricing strategies given each licensing scheme. To handle the multiple equilibria, we follow convention and suppose that once a price is announced, customers coordinate their adoption so as to result in the equilibrium with the highest sales (or the coordination assumption in Fudenberg and Tirole (2000); this assumption is also used in Farrell and Saloner (1985) and Katz and Shapiro (1986)).

![](/api/attachments/FBZ6H2U6/fulltext/images/65a036f9760a73b7f31612418129efb183365b33f737e84c75d9fabbcf57e2e1.jpg)  
Figure 5. Optimal Software Licensing Strategy with Customer Valuation Uncertainty for (á = 0.83, â = 0.3, ä = 0.75)

Note that the vendor needs to navigate not only the dynamics of intertemporal pricing, but also the impact of the adoption base on customer demand (i.e., network effects). This corresponds to a nontrivial dynamic game (Fudenberg and Tirole 2000). To solve this game, we first show the existence and uniqueness of an SPNE in which the vendor offers perpetual licensing only or subscription-based licensing only. Next, we compare the vendor’s equilibrium profit under the two licensing schemes. The detailed analysis is in Appendix A. The following proposition summarizes our findings when customers face no value uncertainty.

Proposition 9. Network effects without customer valuation uncertainty:

When the intensity of network effects is low such that $( 1 - \beta ^ { 2 } ) e \le \beta \nu _ { H } - \nu _ { L } + ( 1 - \delta ) ( 1 - \beta ) c a n d ( 1 - \beta ) e \le ( 1 - \delta ) e ^ { \beta }$ $\delta ) ( \nu _ { H } \ : - \ : \nu _ { L } ) ,$ perpetual licensing is as profitable as subscription-based licensing. In equilibrium, high-type customers adopt the software in both periods, and lowtype customers adopt the software only in period 1.

When the intensity of network effects is high such that (1 $- \beta ^ { 2 } ) e > \beta \nu _ { H } - \nu _ { L } + ( 1 - \delta ) ( 1 - \beta ) c ,$ perpetual licensing is as profitable as subscription-based licensing. In equilibrium, all customers adopt the software in both periods.

When the intensity of network effects is intermediary such that $( 1 - \delta ) ( 1 + \beta ) ( \nu _ { { \scriptscriptstyle H } } - \nu _ { { \scriptscriptstyle L } } ) < ( 1 - \beta ^ { 2 } ) e < \beta \nu _ { { \scriptscriptstyle H } } - \nu _ { { \scriptscriptstyle L } } + ( 1 - \delta )$ $( 1 ~ - ~ \beta ) c ,$ , perpetual licensing is more profitable than subscription-based licensing.

Recall that without network effects, perpetual licensing is as profitable as subscription-based licensing when customers face no value uncertainty. In equilibrium, high-type customers adopt the software in both periods, and low-type customers adopt the software only in period 1. Therefore, when network effects are weak, these main findings continue to hold. When network effects are strong enough, the optimal pricing strategy involves having all customers adopt the software early on to increase their WTP for the software. Perpetual and subscription-based licensing both allow the vendor to expand the adoption base and are equally profitable. When network effects are intermediary, perpetual licensing is optimal as the vendor’s gain from intertemporal price discrimination through perpetual licensing dominates the gain from expanding the adoption base through subscription-based licensing.

When customers face value uncertainty, the following proposition summarizes our findings.

Proposition 10. Network effects with customer valuation uncertainty:

• When the intensity of network effects is low such that

$$
e \leq \max \left\{\frac {\beta v _ {H} - v _ {L}}{1 - \beta^ {2}}, \frac {\psi^ {H} E [ v | H ] - E [ v | L ] + (1 - \delta) \psi^ {L} c}{\psi^ {L} (1 + \psi^ {H})} \right\},
$$

either perpetual licensing or subscription-based licensing is optimal.

When the intensity of network effects is high such that

$$
e > \max \left\{\frac {\beta v _ {H} - v _ {L}}{1 - \beta^ {2}}, \frac {\psi^ {H} E [ v | H ] - E [ v | L ] + (1 - \delta) \psi^ {L} c}{\psi^ {L} (1 + \psi^ {H})} \right\},
$$

perpetual licensing and subscription-based licensing are equally profitable. In equilibrium, all customers adopt the software in both periods.

Similarly, when network effects are weak, the trade-off between perpetual licensing and subscription-based licensing resembles that without network effects. Strong network effects motivate the vendor to adjust his prices so that all customers adopt the software in both periods. A large installation base improves customers’ WTP for the software due to network effects and also the vendor’s profit. Perpetual and subscription-based licensing both allow the vendor to expand the adoption base and are equally profitable.

## The Infinite-Period Model

In this section, we verify the findings of the two-period model in an infinite-period model, in which one unit mass of customers enters the market in period 0 and lives forever, and the monopoly vendor lives forever. No new customers enter the market after period 0. We show that without customer value uncertainty, subscription-based licensing is more profitable than perpetual licensing in the infinite-period model. In contrast, the two licensing forms are equally profitable in the two-period model. With customer value uncertainty, the qualitative findings of the two-period model continue to hold in the infinite-period model: Either perpetual or subscriptionbased licensing is optimal.

## Infinite-Period Model Without Customer Value Uncertainty

When the software is sold via perpetual licensing only, in each period t, the vendor announces a price for buying the software $p _ { s , t } .$ A customer with valuation v who has never adopted the software previously considers whether to buy the software in period t or delay adoption. Her utility from buying the software in period t is $\frac { \nu } { 1 - \delta } - c - p _ { s , t }$ . Her expected utility from delaying adoption until period $ { \textbf { \textit { n } } } >  { \textbf { \textit { t } } }$ is $\delta ^ { n - t } \Big ( \frac { \nu } { 1 - \delta } - c - E p _ { s , n } \Big )$ , where $E p _ { s , n }$ is the expected price for perpetual licenses in period n. The customer buys the software in period t if her payoff from this purchase is no less than that from delaying her adoption until any future period or no adoption at all.

To solve the vendor’s optimal pricing strategy given customers’ decisions is a nontrivial problem as it involves optimization over an infinite time horizon. We first show a preliminary result.

Lemma 1. Under perpetual licensing, as far as the residual demand in period $t \left( x _ { H , n } ( t ) , x _ { L , n } ( t ) \right)$ is positive, in an SPNE, the sales in period t is also positive.

Since there are two types of customers, applying Lemma 1, we show that the unique pure strategy SPNE of this infiniteperiod game is described as follows:

A customer’s strategy: In period t, buy if

$$
p _ {s, t} \leq v - c + \frac {\delta}{1 - \delta} v _ {L}.
$$

The vendor’s strategy: In period $t = 0 .$

$$
p _ {s, t} = v _ {H} - c + \frac {\delta}{1 - \delta} v _ {L};
$$

in period $t \geq 1$

$$
p _ {s, t} = \frac {1}{1 - \delta} v _ {L} - c.
$$

In equilibrium, high-type customers buy the perpetual licenses of the software in period 0, and low-type customers buy the perpetual licenses in period 1. The vendor’s overall profit is

$$
\beta v _ {H} + \frac {\delta}{1 - \delta} v _ {L} - \beta c - \delta (1 - \beta) c.
$$

When the software is sold via subscription-based licensing only, in each period t, the vendor posts two prices: New customers can subscribe to the software for one period at price $p _ { l , t } \dot { , }$ existing customers can renew their subscription for one period at price $r _ { t ^ { * } }$ . In each period t, a customer with valuation v who has never adopted the software previously may choose to subscribe to the software for the first time, or delay adoption. After the initial subscription, she renews the subscription subsequently only if there is a positive gain. Hence, a customer’s expected payoff from subscribing to the software for the first time in period t is:

$$
v - c - p _ {l, t} + \sum_ {m = t + 1} ^ {\infty} \delta^ {m - t} \max \left\{v - E r _ {m}, 0 \right\},
$$

where $E r _ { m }$ is the expected subscription renewal price in period m. The expected utility from delaying adoption until a future period $n > t$ is

$$
\delta^ {n - t} [ v - c - E p _ {l, n} + \sum_ {m = n + 1} ^ {\infty} \delta^ {m - n} \max \{v - E r _ {m}, 0 \} ],
$$

where $E p _ { l , r }$ is the expected new subscription price in period n. The customer subscribes to the software for the first time in period t if it yields at least as high a payoff as delaying her adoption or no adoption at all, or

$$
\begin{array}{c} v - c - p _ {l, t} + \sum_ {m = t + 1} ^ {\infty} \delta^ {m - t} \max \left\{v - E r _ {m}, 0 \right\} \\ \geq \max _ {\forall n > t} \left\{0, \delta^ {n - t} \big [ v - c - E p _ {l, n} + \sum_ {m = n + 1} ^ {\infty} \delta^ {m - n} \max \left\{v - E r _ {m}, 0 \right\} \right] \Big \}. \end{array}
$$

Note that the difference between the left and right hand side of the above inequality is increasing in v. Therefore, the software adoption base in each period satisfies a monotonicity property: If customers with valuation $\nu _ { L }$ find it optimal to subscribe for the first time in period t, then customers with valuation $\nu _ { H }$ either have subscribed to the software for the first time before period t or also find it optimal to subscribe in period t.

The vendor’s pricing strategy in each period affects future payoff only through changing the four demand state variables: $\big ( x _ { H , n } ( t ) , x _ { H , l } ( t ) , x _ { L , l } ( t ) , x _ { L , n } ( t ) \big )$ The price for subscription renewal $r _ { t }$ does not affect the future demand state, and so it is set to maximize the vendor’s current-period profit from existing customers. Given the monotonicity property of the adoption base, and $\beta \nu _ { H } > \nu _ { L }$ , we have the optimal subscription renew price $r _ { t } = \nu _ { H } ,$ for t. In contrast, the price for new subscription $p _ { l , t }$ can affect future demand state as it affects which new customers will become existing customers in the future. One can show that the unique pure strategy SPNE of this infinite-period game is described as follows:

The vendor’s pricing strategy: In period $0 , p _ { l , 0 } = ( 1 ~ -$ $\delta ) ( \nu _ { { \scriptscriptstyle H } } - c ) + \delta ( \nu _ { { \scriptscriptstyle L } } - c )$ . In period $t \ge 1 , p _ { l , t } = \nu _ { L } - c ,$ and $r _ { t } = \nu _ { H } .$

A customer’s strategy: In each period t, having never subscribed previously, subscribe for the first time if $\nu - c - p _ { l , . }$ $\geq \delta$ max $\{ 0 , \nu - \nu _ { L } \}$ . Having subscribed previously, renew subscription if $\nu \geq r _ { t } .$

In equilibrium, high-type customers subscribe to the software for the first time in period 0 and renew their subscription in every period thereafter. Low-type customers subscribe to the software for the first time in period 1 but do not renew their subscription thereafter. The vendor’s profit is

$$
\beta [ (1 - \delta) (v _ {H} - c) + \delta (v _ {L} - c) ] + \frac {\delta}{1 - \delta} \beta v _ {H} + \delta (1 - \beta) (v _ {L} - c).
$$

Comparing the vendor’s profit under perpetual and subscription-based licensing, one can show that without customer value uncertainty, subscription-based licensing is more profitable than perpetual licensing. The following proposition formalizes this finding.

Proposition 11. In an infinite-period model, without customer valuation uncertainty, subscription-based licensing is more profitable than perpetual licensing.

This finding confirms that of the standard durable-goods theory. With perpetual licensing, after high-type customers have bought the software in the initial period, they exit the market. The vendor faces a truncated demand from low-type customers only in the following period. The vendor then lowers the price to generate additional sales. Anticipating lower prices in the future, high-type customers are willing to pay less for the software initially, which hurts the vendor’s profit (the time-inconsistency problem). With subscriptionbased licensing, high-type customers subscribe to the software for the first time in the initial period, and low-type customers subscribe to the software for the first time in the following period. At the beginning of period 2, both high- and low-type customers have subscribed to the software at least once. The vendor then charges the one-period monopolistic price for subscription renewal in every period thereafter. Therefore, his overall profit under subscription-based licensing is higher than that under perpetual licensing.

## Infinite-Period Model with Customer Value Uncertainty

Next, we consider the case in which customers face value uncertainty. When the software is sold via perpetual licensing only, consider customers’ decisions. A customer who receives signal y and has not bought the software previously receives expected utility $\frac { 1 } { 1 - \delta } E [ \nu \vert y ] - c - p _ { s , t } ,$ , if she buys the perpetual license in period $t .$ If she delays her purchase until period $n > t ,$ then she receives expected utility

$$
\delta^ {n - t} \left[ \frac {1}{1 - \delta} E [ v | y ] - c - E p _ {s, n} \right].
$$

Therefore, the customer buys the software in period t if

$$
\frac {1}{1 - \delta} E [ v | y ] - c - p _ {s, t} \geq \max _ {\forall n > t} \left\{0, \delta^ {n - t} \left[ \frac {1}{1 - \delta} E [ v | y ] - c - E p _ {s, n} \right] \right\}.
$$

Consider the vendor’s pricing problem. One can show that Lemma 1 continues to hold when customers face value uncertainty. Applying Lemma 1, one can show that two pricing strategies can be optimal in a pure strategy SPNE:

$$
\begin{array}{l} \text { The   PSX1   strategy:   In   period   0, } \\ p _ {s, 0} = E [ v | H ] - c + \frac {\delta}{1 - \delta} E [ v | L ]. \quad \text { In   period   t   \geq   1, } \\ p _ {s, t} = \frac {1}{1 - \delta} E [ v | L ] - c. \end{array}
$$

The PSX2 strategy: In period 0, $p _ { s , 0 } = { \frac { 1 } { 1 - \delta } } E [ \nu | L ] - c .$ In period $t \geq 1 , p _ { s , t } = \frac { 1 } { 1 - \delta } E [ \nu | L ] - c .$

If the vendor follows the PSX1 strategy, customers who receive the high-type signal buy the software in period $0 ,$ and customers who receive the low-type signal buy the software i n p e r i o d 1 . T h e v e n d o r ’ s p r o f i t i s $\Psi ^ { H } E [ \nu | H ] + { \frac { \delta } { 1 - \delta } } E [ \nu | L ] - \Psi ^ { H } c - \delta \Psi ^ { L } c$ . If the vendor follows the

PSX2 strategy, all customers buy the software in period 0. The vendor’s profit is $E [ \nu | L ] / ( 1 - \delta ) - c$ . Depending on the range of parameter values, the vendor chooses the pricing strategy that maximizes his expected profit.

When the software is sold on a subscription basis only, in each period $t ,$ a customer who has subscribed to the software previously and learned her true type renews her subscription if the benefit of renewing is higher than the cost, or $\nu \geq r _ { t } .$ A customer who receives signal $y$ and has not adopted the software previously can subscribe to the software for the first time in period t, delay her initial subscription until period $n >$ t, or forgo the software altogether. If she subscribes to the software in period t, she receives expected utility: $E [ \nu | y ] - c$ $\begin{array} { r } { \mathbf { \nabla } \cdot p _ { l , t } + \sum _ { m = t + 1 } ^ { \infty } \mathbf { \nabla } \delta ^ { m - t } \mathrm { m a x } \left\{ 0 , \Psi _ { H y } ( \nu _ { H } - E r _ { m } ) , E [ \nu | \nu ] - E r _ { m } \right\} } \end{array}$ . If she delays her initial subscription until period $n > t ,$ she receives utility:

$$
\begin{array}{l} \delta^ {n - t} \bigg [ E [ v | y ] - c - E p _ {l, n} + \sum_ {m = n + 1} ^ {\infty} \delta^ {m - n} \\ \max \left\{0, \psi_ {H y} (v _ {H} - E r _ {m}), E [ v | y ] - E r _ {m} \right\} \bigg ]. \end{array}
$$

The customer chooses the option with the highest expected payoff.

Following a similar procedure as in the case without customer value uncertainty, one can solve the vendor’s optimal pricing strategy. First, one can show that the software adoption base in each period satisfies a monotonicity property: If customers who receive the low-type signal find it optimal to subscribe to the software for the first time in period t, then customers who receive the high-type signal either have subscribed to the software before period t or also find it optimal to subscribe for the first time in period t. Second, given this monotonicity property, one can show that the optimal subscription renewal price $r _ { t } = \nu _ { H } ,$ for t. Finally, one can determine the optimal $p _ { l , t }$ and show that two pricing strategies are possible in an SPNE:

The PLX1 strategy: In period $0 , p _ { l , 0 } = E [ \nu | H ] - c - \delta ( E [ \nu | H ]$ $- E [ \nu | L ] ) ;$ in period $t \geq 1 , p _ { l , t } = E [ \nu | L ] - c$ , and $r _ { t } = \nu _ { H }$

The PLX2 strategy: In period $0 , p _ { l , 0 } = E [ \nu | L ] - c ;$ in period $t \geq 1 , p _ { l , t } \geq E [ \nu | L ] - c .$ , and $r _ { t } = \nu _ { H } .$

If the vendor follows the PLX1 strategy, customers who receive the high-type signal subscribe to the software for the first time in period 0, and customers who receive the low-type signal subscribe to the software for the first time in period 1. Both groups of customers renew their subscription subsequently only if their true types are the high type. The vendor’s profit is

$$
\begin{array}{c} \psi^ {H} E [ v | H ] - \delta \psi^ {H} E [ v | H ] + \delta E [ v | L ] - \psi^ {H} c - \delta \psi^ {L} c + \\ \delta \Big (\alpha + \frac {\delta}{1 - \delta} \Big) \beta v _ {H}. \end{array}
$$

If the vendor follows the PLX2 strategy, all customers subscribe to the software in period 0 and only renew their subscription subsequently if their true types are the high type.

The vendor’s profit is $E [ \nu | L ] - c + \delta \frac { \beta \nu _ { H } } { 1 - \delta } .$

Compare the profitability of the optimal perpetual and subscription-based licensing strategies, and one can show that either perpetual licensing or subscription-based licensing is optimal, depending on the parameter values. This result confirms the main findings of the two-period model that customer valuation uncertainty changes the relative profitability of perpetual and subscription-based licensing. The qualitative forces that drive this change in the infinite-period model are consistent with those in the two-period model, and so are not discussed to avoid repetition.

Proposition 12. In an infinite-period model, with customer valuation uncertainty, either subscription-based or perpetual licensing is optimal. In particular, perpetual licensing is optimal when either one of the following two sets of conditions holds:

$$
\begin{array}{l l} (1) & E [ v | L ] > \beta v _ {H} a n d \left(1 + \frac {\delta^ {2}}{1 - \delta}\right) E [ v | L ] > (1 - \delta) \psi^ {H} E [ v | H ] + \\ & (1 - \delta) \psi^ {L} c + \delta \left(\alpha + \frac {1}{1 - \delta}\right) \beta v _ {H}; o r \\ (2) & \psi^ {H} E [ v | H ] + \frac {\delta}{1 - \delta} E [ v | L ] > \alpha \beta v _ {H} + \frac {\delta}{1 - \delta} \beta v _ {H} a n d \\ & \psi^ {H} E [ v | H ] + \frac {2 \delta - 1}{1 - \delta} E [ v | L ] + (1 - \delta) \psi^ {L} c > \frac {\delta}{1 - \delta} \beta v _ {H}. \end{array}
$$

## Conclusions

This paper studies a software vendor’s decision to offer either perpetual or subscription-based licensing when customers are uncertain about their valuation of the software prior to adoption. Customers receive an informative signal about their valuation before adopting the software and can learn it through use. Software adoption requires an up-front implementation cost. The pricing problem is investigated both in a two-period model and an infinite-period model. We focus on the Subgame Perfect Nash Equilibrium (SPNE) of the game.

## Contribution

This paper makes several contributions. First, we demonstrate that customer valuation uncertainty causes the equilibrium outcome to depart from that of standard durable-goods theories in two aspects:

(1) Contrary to the conventional wisdom of the durablegoods theory that subscription-based licensing is optimal, we show that perpetual licensing can be more profitable for the vendor than subscription-based licensing under some conditions. This result offers a possible explanation for the historical prevalence of perpetual licensing in some software markets.

(2) When subscription-based licensing is optimal, our theory suggests a pricing strategy that is very different from that suggested by standard durable-goods theories. In particular, standard durable-goods theories suggest charging the monopoly leasing price in each period (Bulow 1982), whereas our theory suggests a low-then-high variable pricing path. The initial low price aims to facilitate customer learning and resolution of valuation uncertainty. Such a variable pricing path and the resulting adoption pattern are consistent with market observations (e.g., pricing strategy by Adobe Systems).

The intuition is as follows. With valuation uncertainty, customers’ WTP for the software prior to adoption depends on the informative signal (perceived valuation). After the initial adoption, customers learn their true valuation, and some of them are willing to pay more, while others are only willing to pay less for the software. Subscription-based licensing allows the vendor to vary his prices over time. Specifically, the vendor may set a low initial price so that more customers try out the software and raise the subscription renewal price subsequently to gain from the improved WTP in the high-end market, although he would lose the demand from low-type customers.

With perpetual licensing, the vendor receives full payment up front and does not have the flexibility to adjust his prices for prior customers after they have learned their true types. He would also suffer from the time-inconsistency problem identified in standard durable-goods theories if the selling price in the initial period is discriminative (so that not all customers buy the software in the initial period). On the other hand, the distribution of customers’ perceived valuation of the software before adoption is less dispersed. This reduction in demand heterogeneity can improve the vendor’s profit under perpetual licensing because (1) it reduces the detrimental effect of the time-inconsistency problem as value uncertainty increases low-end customers’ WTP for the software, and (2) the vendor may be able to sell to more customers early on for using the software in perpetuity albeit at a moderate price to account for the risk of adoption.

The optimal licensing strategy depends on the gain and loss from perpetual licensing versus subscription-based licensing. Perpetual licensing is optimal for software that is difficult to evaluate prior to use or requires high implementation costs. These insights are consistent with the observed industry practice.

Second, while trade journals often emphasize the adverse effect of customer valuation uncertainty, we show that such uncertainty can increase or decrease social welfare. It may increase social welfare by reducing demand heterogeneity prior to the initial adoption so that more customers adopt the software early on, whereas it may decrease social welfare as customers may base their adoption decision on an incorrectly perceived valuation of the software. The overall effect depends on the trade-off between the two forces. Moreover, we show that with customer valuation uncertainty, the vendor may prefer a licensing strategy that is suboptimal from a customer or social planner's perspective.

Third, to the best of our knowledge, this is the first paper that studies the profitability of offering a Menu of Subscription Options varying in license duration and price (or the MSO strategy). This is a common licensing strategy employed by software vendors (Dignan 2010), although it has not been studied in prior literature. We show that the presence of customer valuation uncertainty is critical for this MSO strategy to outperform perpetual licensing and single-period subscription-based licensing strategies. The MSO strategy refers to a subscription-based licensing strategy, where customers can commit to subscribe to the software for one period or two periods, etc., and the per-period subscription price is fixed for the duration of the commitment.

The intuition is as follows: Without customer value uncertainty, offering a long-term subscription in addition to a single-period subscription subjects the vendor to the same time-inconsistency problem that hurts his profit under perpetual licensing, and so the MSO strategy is as profitable as perpetual licensing. In particular, without value uncertainty, high-end customers prefer long-term to short-term subscription (weakly) more than low-end customers. Once high-end customers have bought the long-term subscription, the vendor faces a truncated demand (from low-end customers) with lower WTP for the short-term subscription. He then charges a low price for the short-term subscription. High-end customers anticipate low short-term subscription prices and thus are willing to pay less for the long-term subscription early on, which hurts the vendor’s profit.

In contrast, with value uncertainty, customers with high perceived valuation for the software also prefer long-term to short-term subscription (weakly) more than customers with low perceived valuation. The key difference here is that after customers with low perceived valuation have subscribed and used the software for one period (via one-period subscription), they learn their true valuation. Some of these customers are then willing to pay more, while others are only willing to pay less for subscription renewal. When there is enough demand in the high-end market, the vendor finds it optimal to charge a high price for a one-period subscription renewal. Anticipating this high price for a single-period subscription in the future, customers with high perceived valuation for the software are willing to pay more for a long-term subscription early on, which alleviates the time-inconsistency problem, making subscription-based licensing through the MSO strategy more profitable than perpetual licensing under some conditions. The MSO strategy can also outperform singleperiod subscription-based licensing under some conditions, because it allows the vendor to sort customers based on their perceived valuation through a menu of subscription options varying in subscription duration and price. Nevertheless, perpetual licensing can still be optimal under certain conditions.

## Managerial Implications and Future Work

Managerially, our findings have important implications for software licensing practice. First, we show that customer value uncertainty provides a possible explanation for the historical prevalence of perpetual licensing in some software markets. With advances in web technologies, some of these vendors may consider switching to the subscription-based SaaS model to leverage the scale economies of a centralized hosting model. In this case, they have to trade off the efficiency gain of the centralized hosting model with the revenue implication of replacing perpetual licensing with subscriptionbased licensing. If customer value uncertainty remains high, and the implementation cost is not significantly lower given the SaaS model, our results suggest that these vendors may not find it optimal to offer flexible short-term subscription (e.g., monthly subscription) and instead favor subscription with longer-term commitment (e.g., multi-year commitment), a contract resembling perpetual licensing.

Second, for software products that face low levels of customer value uncertainty and implementation cost, we find that the vendors may prefer subscription-based licensing models such as SaaS if the high- and low-end customers’ valuation of the software is relatively different. In this case, our theory suggests a low-then-high variable pricing path, with the low introductory price aiming to encourage new customers to try out the software and resolve value uncertainty. When the high- and low-end customers’ valuation is very different, software vendors may offer a menu of subscription options varying in license duration and price to sort customers based on their WTP for the software.

This study can be extended in a number of directions. First, one may consider a richer set of pricing strategies. For instance, software vendors may combine term-based pricing (perpetual versus lease-based licensing) with versioning strategies and offer one version of his software via perpetual licensing and a different version via subscription-based licensing. Software vendors can also sell upgrades and new versions after introducing the original software. Second, other demand factors may also impact software vendors preference between perpetual licensing and subscriptionbased licensing. For instance, software vendors may incur additional administrative costs (e.g., billing costs) if they choose subscription-based licensing. A detailed discussion on the other factors is beyond the scope of this paper. Future work may extend the model and consider additional factors.

The growth of the software market has highlighted the importance of term-based pricing. The unique demand features such as customers’ valuation uncertainty present many fruitful opportunities for future research.

## Acknowledgments

The author thanks Roy Radner, Vidyanand Choudhary, and Vijay Gurbaxani for their valuable feedback for this work. This work also benefitted from comments and suggestions from participants of research seminars at New York University’s Stern School of Business, University of British Columbia’s Sauder School of Business, Hong Kong University of Science and Technology (HKUST) Business School, Mendoza College of Business at the University of Notre Dame, The McCombs School of Business at the University of Texas at Austin, and the Desautels Faculty of Management at McGill University, where the paper was presented.

## References

Attewell, P. 1992. “Technology Diffusion and Organizational Learning: The Case of Business Computing,” Organization Science (3:1), pp. 1-19.

August, T., Niculescu, M. F., and Shin, H. 2014. “Cloud Implications on Software Network Structure and Security Risks,” Information Systems Research (25:3), pp. 489-510.

Balasubramanian, S., Bhattacharya, S., and Krishnan, V. V. 2015. “Pricing Information Goods: A Strategic Analysis of the Selling and Pay-Per-Use Mechanisms,” Marketing Science (34:2), pp. 218-234.

Band, W., Hamerman, P. D., and Magarie, A. 2010. “Benchmarks for CRM Selection and Deployment: Size Up Your CRM Initiative Compared Against 99 Projects,” Forrester Research, Inc., Cambridge, MA.

Bhaskaran, S. R., and Gilbert, S. M. 2005. “Selling and Leasing Strategies for Durable Goods with Complementary Products,” Management Science (51:8), pp. 1278-1290.

Biehl, A. R. 2001. “Durable-Goods Monopoly with Stochastic Values,” RAND Journal of Economics (32:3), pp. 565-577.

Bulow, J. 1982. “Durable-Goods Monopolist,” Journal of Political Economy (90:2), pp. 314-332.

Bubenko, Jr., J. A. 1995. “Challenges in Requirements Engineering,” in Proceedings of Second IEEE International Symposium on Requirements Engineering, IEEE Computer Society.

Chellappa, R. K., and Shivendu, S. 2005. “Managing Piracy: Pricing and Sampling Strategies for Digital Experience Goods in Vertically Segmented Markets,” Information Systems Research (16:4), pp. 400-417.

Chien, H. K., and Chu, C. 2008. “Sale or Lease? Durable-Goods Monopoly with Network Effects,” Marketing Science (27:6), pp. 1012-1019.

Choudhary, V., Tomak, K., and Chaturvedi, A. 1998. “Economic Benefits of Renting Software,” Journal of Organizational Computing and Electronic Commerce (8:4), pp. 277-305.

Coase, R. 1972. “Durability and Monopoly,” Journal of Law and Economics (15), pp. 143-149.

Cusumano, M. A. 2007. “The Changing Labyrinth of Software Pricing,” Communications of the ACM (50:7), pp. 19-22.

Desai, P., and Purohit, D. 1998. “Leasing and Selling: Optimal Marketing Strategies for a Durable Goods Firm,” Management Science (44:11), pp. 19-34.

DeGraba, P. “No Lease Is Short Enough to Solve the Time Inconsistency Problem,” The Journal of Industrial Economics (42:4), pp. 361-374.

Dey, D., Lahiri, A., and Liu, D. 2013. “Consumer Learning and Time-Locked Trials of Software Products,” Journal of Management Information Systems (30:2), pp. 239-268.

Dignan, L. 2010. “SaaS Pricing Evolves: Should We Be Worried?,” ZDNet (https://www.zdnet.com/article/saas-pricingevolves-should-we-be-worried/).

Farrell, J., and Saloner, G. 1985. “Standardization, Compatibility and Innovation,” The RAND Journal of Economics (16:1), pp. 70-83.

Fudenberg, D., and Tirole, J. 1998. “Upgrades, Tradeins, and Buybacks,” RAND Journal of Economics (29:2), pp. 235-258.

Fudenberg, D., and Tirole, J. 2000. “Pricing a Network Good to Deter Entry,” The Journal of Industrial Economics (48:4), pp. 373-390.

Galletta, D. F. 1986. “A Longitudinal View of an Office System Failure,” Acm SIGOA Newsletter (7:1).

Gartner. 2015a. “The Financial Case for Moving to the Cloud,” Gartner, Inc., Stamford, CT.

Gartner. 2015b. “Modernization and Digital Transformation Projects Are Behind Growth in Enterprise Application Software Market,” Press Release, Gartner, Inc., Stamford, CT (http://www.gartner.com/newsroom/id/3119717).

Gross, P. H. B., and Ginzberg, M. J. 1984. “Barriers to the Adoption of Application Software Packages,” Systems, Objectives, Solutions (4), pp. 211-226.

Gul, F., Sonnenschein, H., and Wilson, R. 1986. “Foundations of Dynamic Monopoly and the Coase Conjecture,” Journal of Economic Theory (39:1), pp. 155-190.

Gupta, A., Linden, L. L., Stahl, D. O., and Whinston, A. B. 2001. “Benefits and Costs of Adopting Usage-Based Pricing in a Subnetwork,” Information Technology & Management (2), pp. 175-191.

Han, K. S., and Noh, M. H. 1999. “Critical Failure Factors that Discourage the Growth of Electronic Commerce,” International Journal of Electronic Commerce (4:2), pp. 25-43.

Huang, K. W., and Sundararajan, A. 2005. “Pricing Models for On-Demand Computing,” CeDER Working Paper No. 05-26, Center for Digital Economy Research, Stern School of Business, New York University, New York.

IDC. 2012. “The Rise of Subscription Software Licensing: Overcoming the Software Value Disconnect,” International Data Corp., Framingham, MA.

IDC. 2015. “IDC Software Licensing and Pricing Predictions 2016,” International Data Corp., Framingham, MA.

Jain, S., and Kannan, P. K. 2002. “Pricing of Information Products on Online Servers: Issues, Models, and Analysis,” Management Science (48:9), pp. 1123-1143.

Jiang, B. J., Chen, P. Y., and Mukhopadhyay, T. 2007. “Software Licensing: Pay-Per-Use Versus Perpetual,” Tepper School of Business, Carnegie Mellon University, Pittsburgh, PA.

Johnson, J. P., and Waldman, M. 2010. “Leasing, Lemons, and Moral Hazard,” Journal of Law and Economics (53:2), pp. 307-328.

Judd, K. 1985. “The Law of Large Numbers with a Continuum of IID Random Variables,” Journal of Economic Theory (35), pp. 19-25.

Katz, M. L., and Shapiro, C. 1986. “Technology Adoption in the Presence of Network Externalities.” Journal of Political Economy (94:4), pp. 822-841.

Larkin, I. 2008. “Bargains-Then-Ripoffs: Innovation, Pricing and Lock-in in Enterprise Software,” Academy of Management Proceedings (1).

Ma, D., and Seidmann, A. 2015. “Analyzing Software as a Service with Per-Transaction Charges,” Information Systems Research (26:2), pp. 360-378.

Niculescu, M. F., and Wu, D. J. 2014. “Economics of Free under Perpetual Licensing: Implications for the Software Industry,” Information Systems Research (25:1), pp. 173-199.

Norton, S., and Boulton, C. 2014. “Why Big Companies Delay Using the Cloud for Some Applications,” Wall Street Journal, July 16.

O’Leary, D. 2000. Enterprise Resource Planning Systems: Systems, Life Cycle, Electronic Commerce, and Risk, Cambridge, UK: Cambridge University Press.

Rao, R. S., Narasimhan, O., and John, G. 2009. “Understanding the Role of Trade-Ins in Durable Goods Markets: Theory and Evidence,” Marketing Science (28:5), pp. 950-967.

Robey, D., Ross, J. W., and Boudreau, M. 2002. “Learning to Implement Enterprise Systems: An Exploratory Study of the Dialectics of Change,” Journal of MIS (19:1), pp. 17-46.

Rust, J. 1986. “When Is it Optimal to Kill Off the Market for Used Durable Goods?,” Econometrica: Journal of the Econometric Society (54:1), pp. 65-86.

Shapiro, C., and Varian, H. R. 1998. Information Rules: A Strategic Guide the Network Economy, Boston: Harvard Business School Press.

Shankland, S. 2014. “Despite Complaints, Most Adobe Creative Cloud Subscribers Plan to Renew,” CNET, March (https://www.cnet.com/news/despite-complaints-most-adobecreative-cloud-subscribers-plan-to-renew/).

Sundararajan, A. 2004. “Nonlinear Pricing of Information Goods,” Management Science (50:12), pp. 1660-1673.

Stokey, N. L. 1979. “Intertemporal Price Dscrimination,” The Quarterly Journal of Economics (93:3), pp. 335-371.

Stokey, N. L. 1981. “Rational Expectations and Durable Goods Pricing,” The Bell Journal of Economics (12:1), pp. 112-128.

Tan, S. 2011. “Lessons from 169 SAP Implementations Using Service Providers in North America,” Gartner Inc., Stamford, CT.

Ulrich, W. M. 2006. “Application Package Software: The Promise Vs. Reality,” Cutter Benchmark Review (6:9), pp. 13-19.

Waldman, M. 2003. “Durable Goods Theory for Real World Markets,” Journal of Economic Perspectives (17), pp. 131-154.

Wall Street Journal. 2015. “Cloud Computing Promises Fall Short: Analysts Warn That the Pay as You Go Promise of Using Applications Online Can Be Hard to Fulfill,” Wall Street Journal, Technology Section, November 12.

Wang, R. 2006. “Trends 2006: Enterprise Software Licensing,” Forrester Research, Cambridge, MA.

Wei, X. D., and Nault, B. R. 2012. “Experience Information Goods: ‘Version-to-Upgrade’,” Decision Support Systems (56), pp. 494-501.

Zhang, J., and Seidmann, A. 2010. “Perpetual Versus Subscription Licensing under Quality Uncertainty and Network Externality Effects,” Journal of Management Information Systems (27:1), pp. 39-68.

## About the Author

Mingdi Xin is an assistant professor of Information Systems at the Paul Merage School of Business, University of California, Irvine. Her research interests include design and pricing strategies for digital goods and services, and IT investment strategies and their competitive implications. She has published in journals such as Management Science, Information Systems Research, and Harvard Business Review. She received a Ph.D. in Information Systems from New York University’s Stern School of Business.

## Appendix A

Proposition 1. Without customer valuation uncertainty, perpetual licensing is as profitable as subscription-based licensing.

## Proof of Prop 1.

For consistency, the demand state is still described by $( x _ { H , n } ( t ) , x _ { H , l } ( t ) , x _ { L , n } ( t ) , x _ { L , l } ( t ) )$ ; however, without consumers’ value uncertainty, $x _ { i , n } ( t ) \left( \mathrm { o r } x _ { i , l } ( t ) \right)$ represents the measure of consumers who are type-<sub>??</sub> and have never bought or subscribed to (or have subscribed to) the software before period $t , i = H$ or <sub>??</sub>. We first solve for the optimal perpetual and subscription-based licensing prices separately and then compare their profitability

When the software is sold through perpetual licensing only, a consumer with valuation <sub>??</sub> who does not buy the software in period 0 buys the software in period 1 if the benefit from adoption is higher than the cost, or $v - c \geq p _ { 1 }$ . In period 0, a consumer buys the software if the payoff from buying in period 0 is no less than that from buying for the first time in period 1 or from not buying the software at all, or

$$
(1 + \delta) v - c - p _ {s, 0} \geq \max \{\delta (v - c - E p _ {1}), 0 \}
$$

where $E p _ { 1 }$ represents the expected price in period 1.

The monopolist’s optimal pricing strategy, given consumers’ decisions, can be solved through backward induction. In period 1, a measure $x _ { H , n } ( 1 )$ of consumers are willing to pay up to $v _ { H } - c$ for the software, and a measure $x _ { H , n } ( 1 ) + x _ { L , n } ( 1 )$ of consumers are willing to pay up to $v _ { L } - c$ for the software. Thus, the monopolist’s optimal strategy is to charge $p _ { 1 } = v _ { H } - c$ if

$$
x _ {H, n} (1) (v _ {H} - c) \geq \left(x _ {H, n} (1) + x _ {L, n} (1)\right) (v _ {L} - c)\tag{5}
$$

and $p _ { 1 } = v _ { L } - c$ otherwise. In period 0, the monopolist specifies $p _ { s , 0 }$ to maximize his overall profit, given consumers’ decisions. By comparing the monopolist’s profit levels given different initial selling prices $( p _ { s , 0 } )$ , one can show that when $c \leq v _ { L } < \beta v _ { H }$ , the unique SPNE of the game is characterized by the following strategy profile:

The monopolist’s strategy: in period 0, $p _ { s , 0 } = v _ { H } + \delta v _ { L } - c ;$ in period 1, $p _ { 1 } = v _ { H } - c \mathrm { i f } ( 5 )$ holds, and $p _ { 1 } = v _ { L } - c$ otherwise.

A consumer’s strategy: in period 0, buy if $\dot { \boldsymbol { p } } _ { s , 0 } \leq \boldsymbol { v } - \boldsymbol { c } + \delta \boldsymbol { v } _ { L } ;$ otherwise, in period 1, buy $\mathrm { i f } p _ { 1 } \leq v - c$

In equilibrium, high-type consumers buy the software in period 0, and low-type consumers buy in period 1. The monopolist’s optimal profit is $\beta ( v _ { H } + \delta v _ { L } - c ) + \delta ( 1 - \beta ) ( v _ { L } - c )$

When the software is sold through subscription-based licensing only, a consumer with valuation who does not lease the software in period 0 leases the software in period 1 if the benefit of leasing is higher than the cost, or $v - c \geq p _ { 1 }$ . A returning lessee renews her lease in period 1 if the benefit from renewing is higher than the lease renewal price, or $v \geq r _ { 1 }$ . A consumer with valuation leases the software in period 0 if the payoff from leasing in period 0 is no less than that from leasing for the first time in period 1 or from not leasing the software at all. That is,

$$
v - c - p _ {l, 0} + \delta \max \left(0, v - E r _ {1}\right) \geq \max \left\{\delta (v - c - E p _ {1}), 0 \right\}
$$

where $E r _ { 1 }$ denotes the expected lease renewal price in period 1.

The monopolist’s optimal pricing strategy can be solved through backward induction. In period 1, a measure $x _ { H , l } ( 1 )$ of consumers are willing to pay up to $v _ { H }$ for renewing their leases, and a measure $x _ { H , l } ( 1 ) + x _ { L , l } ( 1 )$ of consumers are willing to pay up to $v _ { L }$ for renewing their leases. Thus, the optimal lease renewal price $r _ { 1 } = v _ { H }$ if

$$
x _ {H, l} (1) v _ {H} \geq (x _ {H, l} (1) + x _ {L, l} (1)) v _ {L}\tag{6}
$$

and $r _ { 1 } = v _ { L }$ otherwise. Applying a similar argument, the new lease price in period $\mid p _ { 1 } = v _ { H } - c { \mathrm { ~ i f } } ( 5 )$ holds, and $p _ { 1 } = v _ { L } - c$ otherwise. In period 0, the monopolist specifies $p _ { l , 0 }$ to maximize his overall profit, given consumers’ decisions. By comparing the monopolist’s profit levels, given different initial leasing prices $( p _ { l , 0 } )$ , one can show that when $c \leq v _ { L } < \beta v _ { H }$ , the unique SPNE of the game is characterized by the following strategy profile:

The monopolist’s strategy: in period $0 , p _ { l , 0 } = ( 1 - \delta ) v _ { H } - c + \delta v _ { L } ;$ in period 1, $p _ { 1 } = v _ { H } - c \mathrm { i f } \left( 5 \right)$ holds, and $p _ { 1 } = v _ { L } - c$ otherwise; $r _ { 1 } = v _ { H } \mathrm { i f } ( 2 )$ holds, and $r _ { 1 } = v _ { L }$ otherwise.

A consumer’s strategy: in period 0, lease $\mathrm { i f } p _ { l , 0 } \leq v - c + \delta ( v _ { L } - v )$ ; in period 1, having leased in period 0, renew ${ \mathrm { i f } } v \geq r _ { 1 } ;$ having not leased previously, lease i $\mathrm { ~ f ~ } v - c \geq p _ { 1 }$

In equilibrium, high-type consumers lease the software in period 0 and renew their leases in period 1; low-type consumers lease the software in period 1. The monopolist’s optimal profit is $\beta ( v _ { H } + \delta v _ { L } - c ) + \delta ( 1 - \beta ) ( v _ { L } - c )$

Evidently, perpetual licensing is as profitable as subscription-based licensing without consumer value uncertainty. This concludes the proof.

Proposition 2. With customer valuation uncertainty, perpetual licensing is more profitable than subscription-based licensing if either $( 1 - \delta ) E [ v \vert L ] + \delta \beta v _ { H } < \psi ^ { H } E [ v \vert H ] + ( 1 - \delta ) \psi ^ { L } c$ , or $\beta v _ { H } < E [ v | L ]$ . Otherwise, subscription-based licensing is optimal, and the vendor’s optimal pricing strategy is the PL2 strategy.

## Proof of Prop 2.

The monopolist’s optimal pricing strategy under perpetual licensing or subscription-based licensing can be solved in a similar manner as in Proposition 1. See Proof of Proposition 7 for details on how to derive these optimal pricing strategies. Two alternative perpetual licensing strategies can be optimal depending on the range of parameter values:

The PS1 strategy: in period $0 , p _ { s , 0 } = E \left[ v | H \right] + \delta E \left[ v | L \right] - c ;$ in period 1, $p _ { 1 } = E [ v | H ] - c \mathrm { i }$ f

$$
x _ {H, n} (1) (E [ v | H ] - c) \geq \left(x _ {H, n} (1) + x _ {L, n} (1)\right) (E [ v | L ] - c)\tag{7}
$$

and $p _ { 1 } = E [ v | L ] - c$ otherwise.

The PS2 strategy: in period 0 $, p _ { s , 0 } = ( 1 + \delta ) E [ v | L ] - c ;$ ; in period 1, $p _ { 1 } = E [ v | H ] - c { \mathrm { i f } } ( 3 )$ holds, and $p _ { 1 } = E [ v | L ] - c$ otherwise.

When the optimal pricing strategy is the PS1 strategy, consumers who receive the high-type signal buy the software in period <sub>0</sub>, and consumers who receive the low-type signal buy the software in period <sub>1</sub> . The monopolist’s overall profit in equilibrium is $\pi _ { P S 1 } =$ $\psi ^ { H } ( E [ v | H ] - c ) + \delta E [ v | L ] - \delta \bar { \psi } ^ { L } c$ . When the monopolist’s optimal pricing strategy is the PS2 strategy, in equilbrium, all consumers buy the software as soon as they enter the market. The monopolist’s overall profit in equilibrium is $\pi _ { P S 2 } = ( 1 + \delta ) E [ v | L ] - c$

Two alternative subscription-based licensing strategies can be optimal in an SPNE depending on the range of parameter values:

The PL1 strategy: in period 0, $, p _ { l , 0 } = ( 1 - \delta ) E [ v | H ] + \delta E [ v | L ] - c ;$ in period 1, $, p _ { 1 } = E [ v | H ] - c { \mathrm { i f } } ( 3 )$ holds, otherwise $p _ { 1 } = E [ v | L ] -$ $c ; r _ { 1 } = v _ { H } \mathrm { i f }$

$$
\left(x _ {H, l} (1) \psi_ {H H} + x _ {L, l} (1) \psi_ {H L}\right) v _ {H} \geq \left(x _ {H, l} (1) + x _ {L, l} (1)\right) v _ {L}\tag{8}
$$

otherwise $r _ { 1 } = v _ { L }$

The PL2 strategy: in period $0 , p _ { l , 0 } = E [ v | L ] - c ;$ in period $1 , p _ { 1 } = E [ v | H ] - c { \mathrm { i f } } ( 3 )$ holds, otherwise $p _ { 1 } = E [ v | L ] - c ; r _ { 1 } = v _ { H }$ if (4) holds, otherwise $r _ { 1 } = v _ { L }$

When the optimal pricing strategy is the PL1 strategy, in equilibrium, consumers receiving the high-type signal lease the software in period <sub>0</sub>, and only renew their leases in period 1 if their true types are the high type. Consumers receiving the low-type signal lease the software for the first time in period <sub>1</sub>. The monopolist’s overall profit in equilibrium is

$$
\pi_ {P L 1} = \psi^ {H} (E [ v | H ] - c - \delta \psi_ {L H} v _ {L}) + \delta E [ v | L ] - \delta \psi^ {L} c
$$

When the monopolist’s optimal pricing strategy is the PL2 strategy, all consumers lease the software as soon as they enter the market, but they renew their leases in period 1 only if their true types are the high type. The monopolist’s overall profit in equilibrium is $\pi _ { P L 2 } = E [ v | L ] -$ $c + \delta \beta v _ { H }$

Compare the profitability of the PS1, PS2 and that of PL1 and PL2 strategies, we have that the PL1 strategy is always dominated by the PS1 strategy since $\pi _ { P S 1 } > \pi _ { P L 1 }$ . Therefore, perpetual licensing dominates subscription-based licensing if either $\pi _ { P S 1 } > \pi _ { P L 2 } \mathrm { o r } \pi _ { P S 2 } > \pi _ { P L 2 } ,$ Otherwise, subscription-based licensing through the PL2 strategy is more profitable than perpetual licensing. This concludes the proof.

Proposition 3. Without customer valuation uncertainty, the total social surplus and consumer surplus under perpetual licensing are the same as those under subscription-based licensing.

With customer valuation uncertainty

• If the optimal perpetual licensing strategy is the PS1 strategy, and the optimal subscription-based licensing strategy is the PL1 strategy, the total social surplus is higher under perpetual licensing, and consumer surplus is the same under both licensing strategies.

If the optimal perpetual licensing strategy is the PS1 strategy, and the optimal subscription-based licensing strategy is the PL2 strategy, the total social surplus is higher under perpetual licensing $\begin{array} { r } { i f \psi ^ { H } E [ v | \hat { H } ] - \delta \beta v _ { H } + \hat { ( 1 - \delta ) } \psi ^ { L } c > ( 1 - \bar { \delta } ) ( \beta v _ { H } + ( 1 - \beta ) v _ { L } ) } \end{array}$ ; otherwise, it is higher under subscription-based licensing. Consumer surplus is higher under subscription-based licensing

• If the optimal perpetual licensing strategy is the PS2 strategy, both total social surplus and consumer surplus are higher under perpetual licensing.

## Proof of Proposition 3.

Without value uncertainty (or <sub>?? = 1</sub>), under either the optimal perpetual or subscription-based licensing strategies, high-type consumers adopt the software in period 0 and 1. Low-type consumers adopt the software in period 1. Therefore, the total social surplus is the same under either licensing strategies. Since they are equally profitable to the monopolist, consumer surplus is also the same under perpetual licensing and subscription-based licensing.

With value uncertainty, when the software is only sold via perpetual licensing, and the monopolist’s optimal pricing strategy is the PS2 strategy, the total social surplus is $W _ { P S 2 } = ( 1 + \delta ) ( \beta v _ { H } + ( \bar { 1 } - \bar { \beta } ) v _ { L } ) - c$ . Consumers’ surplus is

$$
\begin{array}{r} C _ {P S 2} = (1 + \delta) (\beta v _ {H} + (1 - \beta) v _ {L}) - c - ((1 + \delta) E [ v | L ] - c) \\ = (1 + \delta) (\beta v _ {H} + (1 - \beta) v _ {L} - E [ v | L ]) \end{array}
$$

When the software is only sold via perpetual licensing, and the monopolist’s optimal pricing strategy is the PS1 strategy, the total social surplus is

$$
\begin{array}{r l} & W _ {P S 1} = \psi^ {H} \psi_ {H H} \big ((1 + \delta) v _ {H} - c \big) + \psi^ {H} \psi_ {L H} \big ((1 + \delta) v _ {L} - c \big) + \delta \psi^ {L} \big (\psi_ {H L} (v _ {H} - c) + \psi_ {L L} (v _ {L} - c) \big) \\ & = (1 + \delta) \psi^ {H} E [ v | H ] - \psi^ {H} c + \delta \psi^ {L} (E [ v | L ] - c) \end{array}
$$

Consumer surplus is

$$
\begin{array}{r l} & C _ {P S 1} = (1 + \delta) \psi^ {H} E [ v | H ] - \psi^ {H} c + \delta \psi^ {L} (E [ v | L ] - c) - [ \psi^ {H} (E [ v | H ] - c) + \delta E [ v | L ] - \delta \psi^ {L} c ] \\ & \quad = \delta \psi^ {H} (E [ v | H ] - E [ v | L ]) \end{array}
$$

When the software is only sold via subscription-based licensing, and the monopolist’s optimal pricing strategy is the PL1 strategy, the total social surplus is

$$
\begin{array}{r l} & W _ {P L 1} = \psi^ {H} \psi_ {H H} ((1 + \delta) v _ {H} - c) + \psi^ {H} \psi_ {L H} (v _ {L} - c) + \delta \psi^ {L} (\psi_ {H L} (v _ {H} - c) + \psi_ {L L} (v _ {L} - c)) \\ & \quad = \psi^ {H} E [ v | H ] + \delta \psi^ {H} \psi_ {H H} v _ {H} + \delta \psi^ {L} E [ v | L ] - \psi^ {H} c - \delta \psi^ {L} c \end{array}
$$

Consumer surplus is

$$
\begin{array}{r l} & C _ {P L 1} = \psi^ {H} E [ v | H ] + \delta \psi^ {H} \psi_ {H H} v _ {H} + \delta \psi^ {L} E [ v | L ] - \psi^ {H} c - \delta \psi^ {L} c - (\psi^ {H} (E [ v | H ] - c - \delta \psi_ {L H} v _ {L}) + \delta E [ v | L ] - \delta \psi^ {L} c) \\ & = \delta \psi^ {H} (E [ v | H ] - E [ v | L ]) \end{array}
$$

When the monopolist’s optimal strategy is the PL2 strategy, the total social surplus is $W _ { P L 2 } = ( 1 + \delta ) \beta v _ { H } + ( 1 - \beta ) v _ { L } - c$ . Consumer surplus is

$$
\begin{array}{r} C _ {P L 2} = (1 + \delta) \beta v _ {H} + (1 - \beta) v _ {L} - c - (E [ v | L ] - c + \delta \beta v _ {H}) \\ = \beta v _ {H} + (1 - \beta) v _ {L} - E [ v | L ] \end{array}
$$

Therefore,

Compare the social and consumer surplus of the PS1 and PL1 strategy, one can show that $W _ { P S 1 } > W _ { P L 1 } \Leftrightarrow E [ v | H ] >$ $\psi _ { H H } v _ { H } ,$ which clearly holds, and $C _ { P S 1 } = C _ { P L 1 }$

• Compare the social and consumer surplus of the PS1 and PL2 strategy, one can show that $W _ { P S 1 } > W _ { P L 2 } \Leftrightarrow \delta ( 1 - \beta ) v _ { L } +$ $( 1 - \overset { \cdot } { \delta } ) \psi ^ { L } c > \psi ^ { L } E [ v | L ]$ and $C _ { P S 1 } < C _ { P L 2 } \Leftrightarrow E [ v | L ] < E [ v | H ]$ <sub>.</sub> Clearly, the latter inequality holds

Compare the PS2 and PL1 strategy, one can show that $W _ { P S 2 } > W _ { P L 1 } \Leftrightarrow \psi ^ { L } E [ v | L ] + \delta \psi ^ { H } \psi _ { L H } v _ { L } > \psi ^ { L } c - \delta \psi ^ { L } c$ . (Note that $\beta v _ { H } + ( 1 - \beta ) v _ { L } = \psi ^ { H } E [ v | H ] + \psi ^ { L } E [ v | L ] )$ and $C _ { P S 2 } > C _ { P L 1 } \Leftrightarrow ( \beta v _ { H } + ( 1 - \beta ) v _ { L } ) - E [ v | L ] > 0 ,$ <sub>,</sub> both of which hold.)

• Compare the PS2 and PL2 strategy, one can show that $W _ { P S 2 } > W _ { P L 2 } , { \mathrm { a n d } } C _ { P S 2 } > C _ { P L 2 }$

This concludes the proof.

Proposition 4. Relative to the case without valuation uncertainty, social surplus is improved when <sub>??</sub> is small so that the optimal pricing strategy is the PS2 or PL2 strategy. In contrast, social surplus is lower when <sub>??</sub> is large so that the optimal pricing strategy is the PS1 strategy.

## Proof of Proposition 4.

When , on the equilibrium path, high-type consumers buy or lease the software in period 0 and use the software again in period 1. Lowtype consumers adopt the software in period 1. The total social surplus is $( 1 + \delta ) \beta v _ { H } - \beta c + \delta ( 1 - \beta ) ( v _ { L } - c )$

Since the marginal cost of software is zero, value uncertainty improves social surplus when more consumers adopt the software early rather than later. This is the case when the monopolist’s optimal pricing strategy is the PS2 strategy, in which case all consumers adopt the software in period 0, and the total social surplus is

$$
(1 + \delta) (\beta v _ {H} + (1 - \beta) v _ {L}) - c
$$

When the monopolist’s optimal strategy is the PL2 strategy, all consumers lease the software in period 0, but only high-type consumers renew their leases in period 1. The social surplus is

$$
(1 + \delta) \beta v _ {H} + (1 - \beta) v _ {L} - c
$$

It is still improved since more consumers adopt the software sooner. When the monopolist’s optimal pricing strategy is the PS1 strategy, however, the social surplus is

$$
\begin{array}{r l} & {\psi^ {H} \psi_ {H H} \big ((1 + \delta) v _ {H} - c \big) + \psi^ {H} \psi_ {L H} \big ((1 + \delta) v _ {L} - c \big) + \delta \psi^ {L} \big (\psi_ {H L} (v _ {H} - c) + \psi_ {L L} (v _ {L} - c) \big)} \\ & {= (1 + \delta) \psi^ {H} E [ v | H ] - \psi^ {H} c + \delta \psi^ {L} (E [ v | L ] - c)} \end{array}
$$

One can show that

$$
\begin{array}{c} (1 + \delta) \psi^ {H} E [ v | H ] - \psi^ {H} c + \delta \psi^ {L} (E [ v | L ] - c) <   (1 + \delta) \beta v _ {H} - \beta c + \delta (1 - \beta) (v _ {L} - c) \Longleftrightarrow \\ (1 - \delta) (2 \beta - 1) c <   \beta v _ {H} - v _ {L} + \beta v _ {L} \end{array}
$$

which holds for $0 \le c \le v _ { L }$ . This concludes the proof.

Proposition 5. Impact of Value Uncertainty on the Vendor’s Profit

When the PS2 or PL2 strategy is optimal, the monopolist’s profit decreases with <sub>??</sub>. When the PS1 strategy is optimal, the monopolist’s profit increases with when

$$
c (2 \beta - 1) (\delta - 1) (- 2 \alpha \beta + \alpha + \beta) ^ {2} + (- 2 \alpha \beta + \alpha + \beta) ^ {2} (\beta v _ {H} + (\beta - 1) v _ {L}) > (1 - \beta) \beta \delta (v _ {H} - v _ {L})
$$

and decreases with otherwise.

Proof of Proposition 5.

We know that

$$
\begin{array}{r l} & {\pi_ {P S 1} = \psi^ {H} (E [ v | H ] - c) + \delta E [ v | L ] - \delta \psi^ {L} c} \\ & {\pi_ {P S 2} = (1 + \delta) E [ v | L ] - c} \\ & {\pi_ {P L 2} = E [ v | L ] - c + \delta \beta v _ {H}} \end{array}
$$

Thus,

$$
\begin{array}{r l} & {\frac {\partial \pi_ {P S 2}}{\partial \alpha} = (1 + \delta) \frac {\partial E [ v | L ]}{\partial \alpha} <   0} \\ & {\frac {\partial \pi_ {P L 2}}{\partial \alpha} = \frac {\partial E [ v | L ]}{\partial \alpha} <   0} \\ & {\frac {\partial \pi_ {P S 1}}{\partial \alpha} = (\beta v _ {H} + (\beta - 1) v _ {L}) + c (2 \beta - 1) (\delta - 1) - \frac {(1 - \beta) \beta \delta (v _ {H} - v _ {L})}{(\alpha + \beta - 2 \alpha \beta) ^ {2}}} \end{array}
$$

This concludes the proof.

Proposition 6. The monopolist’s equilibrium profit decreases with the level of customers’ implementation cost (<sub>??</sub>) whether he sells the software through perpetual licensing or subscription-based licensing. The monopolist’s profit decreases faster with <sub>??</sub> if his pricing strategy is such that all rather than a subset of new customers adopt (subscribe or buy) the software in the first period, or mathematically

$$
\frac {\partial \pi_ {i}}{\partial c} <   0, \text {for} i = P S 1, P S 2, P L 2 \text {and} \frac {\partial \pi_ {P S 1}}{\partial c} > \frac {\partial \pi_ {P S 2}}{\partial c} = \frac {\partial \pi_ {P L 2}}{\partial c}
$$

Proof of Proposition 6.

We know that

$$
\begin{array}{r l} & {\pi_ {P S 1} = \psi^ {H} (E [ v | H ] - c) + \delta E [ v | L ] - \delta \psi^ {L} c} \\ & {\pi_ {P S 2} = (1 + \delta) E [ v | L ] - c} \\ & {\pi_ {P L 2} = E [ v | L ] - c + \delta \beta v _ {H}} \end{array}
$$

Thus,

$$
\begin{array}{r} \frac {\partial \pi_ {P S 1}}{\partial c} = - \psi^ {H} - \delta \psi^ {L} > - 1 \\ \frac {\partial \pi_ {P S 2}}{\partial c} = \frac {\partial \pi_ {P L 2}}{\partial c} = - 1 \end{array}
$$

This concludes the proof.

Proposition 7 When consumers face valuation uncertainty:

Case 1. When consumers’ signals are noisy, or $1 / 2 < \alpha \leq \alpha _ { 1 } ,$

The MPS strategy is optimal $\begin{array} { r } { i f 0 < v _ { L } / v _ { H } < } \end{array}$ ?? ?? $( b _ { 1 } , \psi _ { H L } )$ and $0 \leq c < c _ { 2 } / ( 1 - \delta ) \psi ^ { L }$ . In equilibrium, consumers who receive the high-type signal subscribe to the two-period contract in period 0. Consumers who receive the low-type signal subscribe to the oneperiod contract in period 0 and renew their subscription in period 1 only if their true types are the high type. The monopolist’s overall profit is $\delta \psi ^ { H } E [ v | \bar { H } ] + E [ v | L ] - c + \delta \psi ^ { L } \psi _ { H L } v _ { H } .$

• The PS1 strategy is optimal $i f \psi _ { H L } \leq v _ { L } / v _ { H } < \beta$ and $c _ { 1 } / ( 1 - \delta ) \psi ^ { L } \leq c \leq v _ { L } ; o r 0 < v _ { L } / v _ { H } < \psi _ { H L }$ <sup>and</sup> ???? $( c _ { 1 } , c _ { 2 } ) / ( 1 - \delta ) \psi ^ { L } \leq$ $c \leq v _ { L }$

The PS2 strategy is optimal if <sub>??</sub> <sub>??</sub> $( b _ { 1 } , \psi _ { H L } ) \leq v _ { L } / v _ { H } < \beta$ and $0 \leq c < c _ { 1 } / ( 1 - \delta ) \psi ^ { L }$

Case 2. When consumers’ signals are relatively accurate, o $r \alpha _ { 1 } < \alpha < 1 ,$

The MPS strategy is optimal $i f 0 < v _ { L } / v _ { H } < \psi _ { H L }$ and $0 \leq c <$ ???? $( c _ { 2 } , 0 ) / ( 1 - \delta ) \psi ^ { L }$

• The PS1 strategy is optimal $i f 0 < v _ { L } / v _ { H } < \psi _ { H L }$ <sup>and</sup> ???? $( 0 , c _ { 2 } ) / ( 1 - \delta ) \psi ^ { L } \leq c \leq v _ { L } ;$ or $\psi _ { H L } \leq v _ { L } / v _ { H } < \beta$ <sup>and</sup> ???? $\left( c _ { 1 } , c _ { 1 } + \right.$ $\delta ( \beta v _ { H } - E [ v | L ] ) \big ) / ( 1 - \delta ) \psi ^ { L } \leq c \leq v _ { L }$

The PS2 strategy is optimal $i f ( \beta - \psi _ { H L } ) / \psi _ { L L } \leq v _ { L } / v _ { H } < \beta$ and $0 \leq c < m a x \left( c _ { 1 } , 0 \right) / ( 1 - \delta ) \psi ^ { L }$

The PL2 is optimal $i f \psi _ { H L } \leq v _ { L } / v _ { H } < ( \beta - \psi _ { H L } ) / \psi _ { L L }$ and $0 \leq c < \big ( c _ { 1 } + \delta ( \beta v _ { H } - E [ v | L ] ) \big ) / ( 1 - \delta ) \psi ^ { L } .$

## Proof of Proposition 7

Note that given an optimal MSO strategy, there are only two possibilities: 1) only one type of term-based contracts is effective in equilibrium, or 2) more than one type of term-based contracts is effective in equilibrium. In scenario 1), one can show that in a two-period model, such an optimal MSO strategy is equivalent to either perpetual licensing or single-period subscription based licensing, depending on which type of contract is effective. In particular, in period 0, if only the two-period subscription is effective in equilibrium, then the MSO strategy is equivalent to perpetual licensing; if only the one-period subscription is effective in equilibrium, then the MSO strategy is equivalent to singleperiod subscription based licensing.

In scenario 2),

First, we show that the only optimal MSO strategy under which more than one type of term-based contracts is effective in equilibrium is the MPS strategy.

● Second, we compare the profitability of the MPS strategy with that of perpetual licensing (the PS1 and PS2 strategies) and singleperiod subscription-based licensing (the PL1 and PL2 strategies) to determine the optimal software licensing strategy.

First, we solve for MSO strategies under which more than one type of term-based contracts is effective in equilibrium. Note that in period 1, the vendor can only offer one-period contracts since it is the last period. Therefore, this requires more than one type of term-based contracts to be effective in period 0. Given the monotonicity property of the adoption base, in period 0, if consumers who receive the low-type signal find it optimal to adopt the two-period subscription, then consumers who receive the high-type signal also find it optimal to buy the longterm subscription. Therefore, if there is an optimal MSO strategy with which more than one type of term-based contracts is effective in period 0, then given this strategy, consumers who receive the high-type signal subscribe to the two-period contract, while consumers who receive the low-type signal subscribe to the single-period lease in period 0.

Next, we solve the monopolist’s optimal pricing problem subject to these constraints. Specifically, these constraints can be formulated as follows:

1. Consumers who receive the high-type signal prefer to subscribe to the two-period contract to subscribing to the one-period contract in period 0 or delaying adoption till period 1 or no adoption. Or mathematically,

$$
\begin{array}{r l} & {(1 + \delta) E [ v | H ] - c - p _ {l 2, 0}} \\ & {\geq E [ v | H ] - c - p _ {l 1, 0} + \delta \max \left\{0, \psi_ {H H} (v _ {H} - E r _ {1}), E [ v | H ] - E r _ {1} \right\} \mathrm{and}} \end{array}
$$

$$
(1 + \delta) E [ v | H ] - c - p _ {l 2, 0} \geq \delta \max \{(E [ v | H ] - c - E p _ {1}), 0 \}
$$

2. Consumers who receive the low-type signal prefer to subscribe to the one-period contract to subscribing to the two-period contract in period 0 or delaying adoption till period 1 or no adoption. Or mathematically,

$$
\begin{array}{r l} & E [ v | L ] - c - p _ {l 1, 0} + \delta \max \{0, \psi_ {H L} (v _ {H} - E r _ {1}), E [ v | L ] - E r _ {1} \} \\ & \geq (1 + \delta) E [ v | L ] - c - p _ {l 2, 0}, \text {and} \end{array}
$$

$$
\begin{array}{l} E [ v | L ] - c - p _ {l 1, 0} + \delta \max \left\{0, \psi_ {H L} (v _ {H} - E r _ {1}), E [ v | L ] - E r _ {1} \right\} \\ \geq \delta \max \left\{(E [ v | L ] - c - E p _ {1}), 0 \right\} \end{array}
$$

Given this demand structure, the monopolist’s pricing problem in the second period can be easily solved. Since only consumers who receive the low-type signal would seek to renew their leases in period 1, the monopolist’s optimal pricing strategy in period 1 is $r _ { 1 } = v _ { H } \mathrm { i f } \psi _ { H L } v _ { H } \geq$ $v _ { L } ;$ otherwise, $\begin{array} { r } { r _ { 1 } = v _ { L } , p _ { 1 } = E [ v | H ] - c \mathrm { ~ i f ~ } x _ { H , n } ( 1 ) ( E [ v | H ] - c ) \geq \left( x _ { H , n } ( 1 ) + x _ { L , n } ( 1 ) \right) ( E [ v | L ] - c ) ; } \end{array}$ otherwise, $p _ { 1 } = E [ v | L ] - c$ . The monopolist’s pricing problem can now be described as:

$$
\max _ {p _ {l 2, 0}, p _ {l 1, 0}} \psi^ {H} p _ {l 2, 0} + \psi^ {L} p _ {l 1, 0} + \delta \psi^ {L} \max \{\psi_ {H L} v _ {H}, v _ {L} \}
$$

subject to the constraints described above in #1 and #2. Therefore, the monopolist’s optimal pricing strategy is to charge the highest prices possible (for $p _ { l 2 , 0 } , p _ { l 1 , 0 } )$ given the constraints in #1 and #2.

Note that given the constraints in #1 and $\# 2 ,$ , we know that $x _ { H , n } ( 1 ) = x _ { L , n } ( 1 ) = 0 \mathrm { . }$ , and so $p _ { 1 } = E [ v | H ] - c$ . (Even if individual consumers deviate, the demand state in period 1 does not change as there is a continuum of consumers.) Thus, one can show that the 4 constraints in #1 and #2 can be reduced to three constraints:

$$
\begin{array}{r l} & {(1 + \delta) E [ v | H ] - c - p _ {l 2, 0}} \\ & {\geq E [ v | H ] - c - p _ {l 1, 0} + \delta \max \{0, \psi_ {H H} (v _ {H} - E r _ {1}), E [ v | H ] - E r _ {1} \}, \mathrm{and}} \\ & {\qquad E [ v | L ] - c - p _ {l 1, 0} + \delta \max \{0, \psi_ {H L} (v _ {H} - E r _ {1}), E [ v | L ] - E r _ {1} \}} \\ & {\qquad \geq (1 + \delta) E [ v | L ] - c - p _ {l 2, 0}, \mathrm{and}} \\ & {\qquad E [ v | L ] - c + \delta \max \{0, \psi_ {H L} (v _ {H} - E r _ {1}), E [ v | L ] - E r _ {1} \} \geq p _ {l 1, 0}} \end{array}
$$

From this, one can solve the monopolist’s optimal pricing strategy as follows:

Case 1: $\mathrm { I f } \psi _ { H L } v _ { H } \geq v _ { L } .$ , then $r _ { 1 } = v _ { H }$ , and the maximum prices that satisfy the above constraints are $p _ { l 2 , 0 } = \delta E [ v | H ] + E [ v | L ] - c ,$ and $p _ { l 1 , 0 } = E [ v | L ] - c$ . Therefore, the monopolist’s optimal pricing strategy is described by the MPS strategy. The monopolist’s overall profit from this pricing strategy is $\pi _ { M P S } = \delta \psi ^ { H } E [ v | H ] + E [ v | L ] - c + \delta \psi ^ { L } \psi _ { H L } v _ { H }$

Case 2: If $\psi _ { H L } v _ { H } < v _ { L } .$ , then $r _ { 1 } = v _ { L }$ , and the maximum prices that satisfy the above constraints are $p _ { l 2 , 0 } = ( 1 + \delta ) E [ v | L ] - c .$ and $p _ { l 1 , 0 } =$ $E [ v | L ] - c + \delta ( E [ v | L ] - v _ { L } )$ . In this case, two-period subscription is equivalent to one-period subscription in period 0, and so all consumers adopt the two-period subscription<sup>8</sup>. That is, only the two-period subscription is effective in equilibrium, and the MSO strategy is equivalent to perpetual licensing through the PS2 strategy.

Therefore, the only MSO strategy under which more than one type of term-based contracts is effective in equilibrium is the MPS strategy. Second, we compare the profitability of the MPS strategy with that of perpetual licensing (the PS1 and PS2 strategies) and single-period subscription-based licensing (the PL1 and PL2 strategies) to determine the optimal software licensing strategy. Recall that the monopolist’s overall profit under perpetual licensing is

$$
\begin{array}{r l} & {\pi_ {P S 1} = \psi^ {H} (E [ v | H ] - c) + \delta E [ v | L ] - \delta \psi^ {L} c} \\ & {\pi_ {P S 2} = (1 + \delta) E [ v | L ] - c} \end{array}
$$

The monopolist’s overall profit under single-period subscription-based licensing is

$$
\begin{array}{r l} & {\pi_ {P L 1} = \psi^ {H} (E [ v | H ] + \delta E [ v | L ] - c - \delta \psi_ {L H} v _ {L}) + \delta \psi^ {L} (E [ v | L ] - c)} \\ & {\pi_ {P L 2} = E [ v | L ] - c + \delta \beta v _ {H}} \end{array}
$$

Compare the profitability of the MPS strategy with that of perpetual licensing and single-period subscription-based licensing, one can obtain the results in the proposition. This concludes the proof.

Proposition 8. Without customer value uncertainty, the monopolist’s optimal pricing strategy given the MSO strategy is such that in equilibrium, $p _ { l 2 , 0 } = v _ { H } - c + \delta v _ { L } , p _ { l 1 , 0 } = v _ { H } - c - \delta ( v _ { H } - v _ { L } ) , r _ { 1 } = v _ { H } , p _ { 1 } = v _ { L } - c$ . The monopolist’s optimal profit is $\beta ( v _ { H } - c +$ $\delta v _ { L } ) + \delta ( 1 - \beta ) ( v _ { L } - c )$ <sub>)</sub>. This pricing strategy is as profitable as perpetual licensing or single-period subscription-based licensing.

## Proof of Proposition 8.

If the pricing strategy $\left( p _ { l 1 , 0 } , p _ { l 2 , 0 } , r _ { 1 } , p _ { 1 } \right)$ is such that no consumers subscribe to the two-period contract in period 0, then this pricing strategy is equivalent to offering single-period subscription only at prices $\left( { p _ { l 1 , 0 } , r _ { 1 } , p _ { 1 } } \right)$ , in which case we know that the optimal pricing strategy is $p _ { l 1 , 0 } = v _ { H } - c - \delta ( v _ { H } - v _ { L } ) , r _ { 1 } = v _ { H } , p _ { 1 } = v _ { L } - c _ { \ O }$ , and the monopolist’s profit is $\beta ( v _ { H } - c + \delta v _ { L } ) + \delta ( 1 - \beta ) ( v _ { L } - c )$ . If the pricing strategy $\left( p _ { l 1 , 0 } , p _ { l 2 , 0 } , r _ { 1 } , p _ { 1 } \right)$ is such that no consumers subscribe to the one-period contract in period 0, then this pricing strategy is equivalent to offering perpetual licensing only at prices $\left( { p _ { l 2 , 0 } , r _ { 1 } , p _ { 1 } } \right)$ , in which case we know that the optimal pricing strategy is $p _ { l 2 , 0 } = v _ { H } - c + \delta v _ { L }$ $r _ { 1 } = v _ { H } , p _ { 1 } = v _ { L } - c$ , and the monopolist’s profit is $\beta ( v _ { H } - c + \delta v _ { L } ) + \delta ( 1 - \beta ) ( v _ { L } - c )$

If the pricing strategy $\left( p _ { l 1 , 0 } , p _ { l 2 , 0 } , r _ { 1 } , p _ { 1 } \right)$ is such that some consumers subscribe to the one-period contract and some subscribe to the twoperiod contract in period 0, then it has to be that the cost of subscribing to the two-period contract is no more than that of subscripting to the one-period contract in period 0 and renewing the subscription in period $1 , \mathrm { o r } p _ { l 2 , 0 } \leq p _ { l 1 , 0 } + \delta r _ { 1 }$ . Moreover, in period 1, since the monopolist can recognize existing customers, $r _ { 1 }$ is such that at least some consumers who have subscribed to the one-period contract in period 0 renew their subscription in period 1. This implies $p _ { l 2 , 0 } \ge p _ { l 1 , 0 } + \delta r _ { 1 }$ . Therefore, $p _ { l 2 , 0 } = p _ { l 1 , 0 } + \delta r _ { 1 }$ . With this condition, one can easily show that the optimal pricing strategy is $p _ { l 2 , 0 } = v _ { H } - c + \delta v _ { L } , p _ { l 1 , 0 } = v _ { H } - c - \delta ( v _ { H } - v _ { L } ) , r _ { 1 } = v _ { H } , p _ { 1 } = v _ { L } - c$ . The monopolist’s optimal profit is $\beta ( v _ { H } - c + \delta v _ { L } ) + \delta ( 1 - \beta ) ( v _ { L } - c )$ . This concludes the proof.

Proposition 9. Network Effects without Valuation Uncertainty

When the intensity of network effects is low such that $( 1 - \beta ^ { 2 } ) e \le \beta v _ { H } - v _ { L } + ( 1 - \delta ) ( 1 - \beta ) c , \mathrm { a n d } ( 1 - \beta ) e \le ( 1 - \delta ) ( v _ { H } - v _ { L } )$ perpetual licensing is as profitable as subscription-based licensing. In equilibrium, high-type consumers adopt the software in both periods, and low-type consumers adopt the software only in period 1.

• When the intensity of network effects is high such that $( 1 - \beta ^ { 2 } ) e > \beta v _ { H } - v _ { L } + ( 1 - \delta ) ( 1 - \beta ) c$ , perpetual licensing is as profitable as subscription-based licensing. In equilibrium all consumers adopt the software in both periods.

When the intensity of network effects is intermediary such that $( 1 - \delta ) ( 1 + \beta ) ( v _ { { \scriptscriptstyle H } } - v _ { { \scriptscriptstyle L } } ) < ( 1 - \beta ^ { 2 } ) e < \beta v _ { { \scriptscriptstyle H } } - v _ { { \scriptscriptstyle L } } + ( 1 - \delta ) ( 1 - \delta ) v _ { { \scriptscriptstyle H } } .$ <sub>??)??</sub>), perpetual licensing is more profitable than subscription-based licensing

## Proof of Proposition 9

This proposition is proven through a series of intermediary results. Specifically, the following Propositions 9.1 to 9.4 prove the existence of an SPNE and its uniqueness when the software is sold via perpetual licensing only. Propositions 9.5 to 9.10 prove the existence of an SPNE and its uniqueness when the software is sold via subscription-based licensing only. Proposition 9.11 proves the profit comparison between perpetual licensing and subscription-based licensing in the presence of network effects.

Perpetual Licensing Result 1: When the intensity of network effects is low such that

$$
(1 - \beta^ {2}) e \leq \beta v _ {H} - v _ {L} + (1 - \delta) (1 - \beta) c\tag{9}
$$

there is an unique SPNE in which the high-type consumers buy in period 0, and the low-type consumers buy in period 1.

Consider the following strategy profile:

• High-type consumers: In period 0, buy if $p _ { s , 0 } \leq v _ { H } - c + \delta v _ { L } + e \cdot \beta + \delta e$ . In period 1, buy if $p _ { s , 1 } \leq v _ { H } + \beta e - c$

• Low-type consumers: In period 0, buy if $p _ { s , 0 } \leq v _ { L } - c + \delta v _ { L } + e + \delta e$ . In period 1, buy if $p _ { s , 1 } \leq v _ { L } + e - c .$

• The monopolist’s strategy is to set $p _ { s , 0 } = v _ { H } - c + \delta v _ { L } + e \cdot \beta + \delta e , \mathrm { a n d } p _ { s , 1 } = v _ { L } + e - c$

Note that given (9), $v _ { H } + \beta e > v _ { L } + e .$

Proposition 9.1: When the software is sold via perpetual licensing only, given (9), the above strategy profile is an SPNE. The monopolist’s profit in equilibrium is

$$
\beta v _ {H} + \delta v _ {L} + (\beta^ {2} + \delta) e - \delta (1 - \beta) c - \beta c
$$

Proof Given consumers’ strategy, the monopolist cannot improve his profit by charging a different price in period 0. This is because first, clearly charging any price $p _ { s , 0 } \in \left( v _ { L } - c + \delta v _ { L } + e + \delta e , v _ { H } - c + \delta v _ { L } + e \cdot \beta + \delta e \right) \mathrm { o r } p _ { s , 0 } \in \left( 0 , v _ { L } - c + \delta v _ { L } + e + \delta e \right) $ is suboptimal. $\mathrm { I f } p _ { s , 0 } = v _ { L } - c + \delta v _ { L } + e + \delta e$ , then the monopolist’s maximum payoff off the equilibrium path is $v _ { L } - c + \delta v _ { L } + e + \delta e$ . One can show that given (9), this payoff is less than his payoff on the equilibrium path. If $p _ { s , 0 } > v _ { H } - c + \delta v _ { L } + e \cdot \beta + \delta e$ , then the monopolist’s maximum payoff off the equilibrium path is $\delta \beta ( v _ { H } + \beta e - c )$ , given (9). It is easy to show that this payoff is less than the payoff on the equilibrium path. In period 1, given consumers’ strategy, clearly the monopolist does not benefit from any deviation.

Given the monopolist’s pricing strategy, clearly consumers have no incentives to deviate. This concludes the proof.

Proposition 9.2: When the software is sold via perpetual licensing only, given (9), the unique pure strategy SPNE is such that only hightype consumers buy in period 0, and low-type consumers buy in period 1.

Proof Fix a pure strategy SPNE. The highest price consistent with all low-type consumers buying in period 0 is $p _ { s , 0 } = v _ { L } - c + \delta v _ { L } + e +$ , in which case the monopolist’s overall payoff is $v _ { L } - c + \delta v _ { L } + e + \delta e$ . The highest price consistent with all high-type consumers buying in period 0 is $p _ { s , 0 } = v _ { H } - c + \delta v _ { L } + e \cdot \beta + \delta e$ , in which case the monopolist’s maximum payoff is $\beta v _ { H } - \beta c + e \cdot \beta ^ { 2 } + \delta v _ { L } + \delta e -$ $\delta ( 1 - \beta ) c$ . The monopolist achieves this payoff by selling to the low-type consumers in period 1. Given (9), one can show that the second payoff is higher than the first. Since the monoplist’s optimum is to charge the highest price consistent with a given level of sales, the unique pure strategy SPNE is to sell to the high-type consumers only in period 0 and to the low-type consumers in period 1. This concludes the proof.

Perpetual Licensing Result 2: When the intensity of network effects is strong such that (9) does not hold, or $( 1 - \beta ^ { 2 } ) e > \beta v _ { H } - v _ { L } +$ $( 1 - \delta ) ( 1 - \beta ) c ,$ , there is an unique SPNE in which all consumers buy in period 0.

Consider the following strategy profile:

• High-type consumers: In period 0, buy $\mathrm { i f } p _ { s , 0 } \leq \operatorname* { m a x } \left\{ v _ { H } - c + \delta v _ { L } + e \cdot \beta + \delta e , v _ { L } - c + \delta v _ { L } + e + \delta e \right\}$ . In period 1, buy if $p _ { s , 1 } \leq \operatorname* { m a x } { \{ v _ { H } + \beta e - c , v _ { L } + e - c \} } .$

• Low-type consumers: In period $0 , \mathrm { b u y ~ i f } p _ { s , 0 } \leq v _ { L } - c + \delta v _ { L } + e + \delta e .$ In period 1, buy $\mathrm { i f } p _ { s , 1 } \leq v _ { L } + e - c$

• The monopolist’s strategy: $p _ { s , 0 } = v _ { L } - c + \delta v _ { L } + e + \delta e .$ , and $p _ { s , 1 } = v _ { L } + e - c .$

Proposition 9.3: When the software is sold via perpetual licensing only, given (9) does not hold, the above strategy profile is an SPNE. The monopolist’s profit in equilibrium is

$$
v _ {L} - c + \delta v _ {L} + e + \delta e
$$

Proof. Given consumers’ strategy, the monopolist cannot improve his profit by charging a different price in period 0. This is because first, clearly charging any price $p _ { s , 0 }$ such that $0 \le p _ { s , 0 } <$ min $\{ v _ { H } - c + \delta v _ { L } + e \cdot \beta + \delta e , v _ { L } - c + \delta v _ { L } + e + \delta e \}$ <sup>or</sup> min $\{ v _ { H } - c + \delta v _ { L } + e $ $\beta + \delta e , v _ { L } - c + \delta v _ { L } + e + \delta e \} < p _ { s , 0 } < \operatorname* { m a x } { \{ v _ { H } - c + \delta v _ { L } + e \cdot \beta + \delta e , v _ { L } - c + \delta v _ { L } + e + \delta e \} }$ is suboptimal. One can show that

$$
v _ {H} - c + \delta v _ {L} + e \cdot \beta + \delta e > v _ {L} - c + \delta v _ {L} + e + \delta e \Leftrightarrow v _ {H} - v _ {L} > (1 - \beta) e
$$

When $v _ { H } - v _ { L } < ( 1 - \beta ) e$ , clearly the monopolist cannot gain from deviating from the equilibrium prices. When $v _ { H } - v _ { L } > ( 1 - \beta ) e$ $v _ { H } + \beta e - c > v _ { L } + e - c .$ . Consider a deviation $p _ { s , 0 } = v _ { H } - c + \delta v _ { L } + e \cdot \beta + \delta e$ . The maximum payoff from this deviation is

$$
\beta (v _ {H} - c + \delta v _ {L} + e \cdot \beta + \delta e) + \delta (1 - \beta) (v _ {L} + e - c)
$$

which is less than the monopolist’s equilibrium payoff given that (9) does not hold. If $\dot { p } _ { s , 0 } > v _ { H } - c + \delta v _ { L } + e \cdot \beta + \delta e$ , then the maximum payoff that the monopolist can gain from this deviation is <sub>?? max</sub> $\{ \beta ( v _ { H } + \beta e - c ) , v _ { L } + e - c \}$ , which is less than the monopolist’s equilibrium payoff. Since in equilibrium all consumers buy the software in period 0, the monopolist cannot gain from simply deviating in period 1.

Given the monopolist’s pricing strategy, one can show that consumers have no incentives to deviate. This concludes the proof.

Proof. Fix a pure strategy SPNE. When $v _ { H } - v _ { L } \leq ( 1 - \beta ) \epsilon$ , the highest price consistent with low-type consumers buying in period 0 is $p _ { s , 0 } = v _ { L } - c + \delta v _ { L } + e + \delta e$ , which also generates the highest demand for two periods. Clearly, when $v _ { H } - v _ { L } < ( 1 - \beta ) e$ , this is the unique equilibrium.

When $v _ { H } - v _ { L } > ( 1 - \beta ) e$ , the highest price consistent with all consumers buying in period 0 is $p _ { s , 0 } = v _ { L } - c + \delta v _ { L } + e + \delta e$ , in which case the monopolist’s overall payoff is $v _ { L } - c + \delta v _ { L } + e + \delta e$ . The highest price consistent with high-type consumers buying in period 0 is $p _ { s , 0 } = v _ { H } - c + \delta v _ { L } + e \cdot \beta + \delta e$ , in which case the monopolist’s maximum payoff is $\beta v _ { H } - \beta c + e \cdot \beta ^ { 2 } + \delta v _ { L } + \delta e - \delta ( 1 - \beta ) c$ . The monopolist achieves this payoff by selling to low-type consumers in period 1. Given that (9) does not hold, one can show that the second payoff is lower than the first. Since the monoplist’s optimum is to charge the highest price consistent with a given level of sales, the unique pure strategy SPNE is to sell to all consumers in period 0. This concludes the proof.

When the software is sold via subscription-based licensing only, we show below that if the intensity of network effects is low, then the unique SPNE of the game resembles that without network effects. In equilibrium, high-type consumers subscribe in both periods, and low-type consumers subscribe in period 1 (i.e., Result 1). If the intensity of network effects is high, the unique SPNE of the game is such that all consumers subscribe in both periods (i.e., Result 2). If the intensity of network effects is intermediary, the unique SPNE of the game is such that all consumers subscribe in period 0, but only high-type consumers renew in period 1 (Result 3).

Subscription-based Licensing Result 1: When the intensity of network effects is small such that (9) holds $( \mathrm { i . e . , } ( 1 - \beta ^ { 2 } ) e \leq \beta v _ { H } - v _ { L } +$ $( 1 - \delta ) \bar { ( } 1 - \beta ) c )$ and

$$
(1 - \beta) e \leq (1 - \delta) (v _ {H} - v _ {L})\tag{10}
$$

there is an unique SPNE in which high-type consumers subscribe to the software in both periods, and low-type consumers subscribe only in period 1.

Consider the following strategy profile:

High-type consumers: In period 0, subscribe to the software if $p _ { l , 0 } \le v _ { H } + \beta e - c - \delta ( v _ { H } - v _ { L } )$ . In period 1, having subscribed previously, subscribe again if $p _ { l , 0 } > v _ { L } + e - c$ and $r _ { 1 } \le v _ { H } + e _ { : }$ <sup>,</sup> <sup>or</sup> ?? ≤ ?? + ?? − ?? <sup>and</sup> $r _ { 1 } \le \operatorname* { m a x } { \{ v _ { H } + \beta e , v _ { L } + e \} }$ ; having not subscribed previously, subscribe if $p _ { l , 1 } \leq v _ { H } + \beta e - c .$

• Low-type consumers: In period 0, subscribe to the software if $p _ { l , 0 } \leq v _ { L } + e - c$ . In period 1, having subscribed previously, subscribe again $\mathrm { i f } r _ { 1 } \le v _ { L } + e ;$ having not subscribed previously, subscribe $\mathrm { i f } p _ { l , 1 } \leq v _ { L } + e - c$

• The monopolist’s pricing strategy: In period 0, $p _ { l , 0 } = v _ { H } + \beta e - c - \delta ( v _ { H } - v _ { L } )$ . In period $1 , r _ { 1 } = v _ { H } + e ;$ and $p _ { l , 1 } = v _ { L } + e - c$

Proposition 9.5: When the software is sold via subscription-based licensing only, given (9) and (10), the above strategy profile is an SPNE. The monopolist’s equilibrium profit is

$$
\beta v _ {H} + \delta v _ {L} + (\beta^ {2} + \delta) e - \delta (1 - \beta) c - \beta c
$$

Proof. Note that $v _ { L } + e - c < v _ { H } + \beta e - c - \delta ( v _ { H } - v _ { L } ) , { \mathrm { a n d ~ } } v _ { L } + e - c < v _ { H } + \beta e - c , { \mathrm { g i v e n } } ( 1 0 ) .$

Given consumers’ strategy, the monopolist cannot improve his profit by charging a different price in period 0. This is because first, clearly charging any price $p _ { l , 0 }$ such that $v _ { L } + e - c < v _ { l , 0 } < v _ { H } + \beta e - c - \delta ( v _ { H } - v _ { L } ) , \mathrm { o r } \ 0 < p _ { l , 0 } < v _ { L } + e - c$ is suboptimal since these are not the highest price that the monopolist can charge given the same sales. $\mathrm { I f } p _ { l , 0 } = v _ { L } + e - c$ , then all consumers subscribe to the software in period 0, the monopolist’s maximum profit from this deviation is $\boldsymbol { v } _ { L } + \boldsymbol { e } - \boldsymbol { c } + \delta$ max $\{ \beta ( v _ { H } + \beta e ) , v _ { L } + e \}$ . One can show that when $v _ { L } +$ $e > \beta ( v _ { H } + \beta e )$ , this profit is less than the monopolist’s profit on the equilibrium path since

$$
\begin{array}{r} v _ {L} + e - c + \delta (v _ {L} + e) <   \beta v _ {H} + \delta v _ {L} + (\beta^ {2} + \delta) e - \delta (1 - \beta) c - \beta c \Leftrightarrow \\ (1 - \beta^ {2}) e <   \beta v _ {H} - v _ {L} + (1 - \delta) (1 - \beta) c \end{array}
$$

which holds when (9) holds; when $v _ { L } + e < \beta ( v _ { H } + \beta e )$ , this profit is still less than the monopolist’s profit on the equilibrium path since

$$
\begin{array}{r} v _ {L} + e - c + \delta \beta (v _ {H} + \beta e) <   \beta v _ {H} + \delta v _ {L} + (\beta^ {2} + \delta) e - \delta (1 - \beta) c - \beta c \Leftrightarrow \\ (1 - \beta^ {2}) e <   \beta v _ {H} - v _ {L} + (1 - \beta) c \end{array}
$$

which holds when (9) holds. Thus, this deviation is not profitable. $\mathrm { I f } p _ { l , 0 } > v _ { H } + \beta e - c - \delta ( v _ { H } - v _ { L } )$ , then no consumers subscribe in period 0. The monopolist’s maximum profit is <sub>?? max</sub> $\{ \beta ( v _ { H } + \beta e - c ) , v _ { L } + e - c \}$ , which is less than his equilibrium profit. Given consumers’ strategy, one can show that the monopolist cannot improve his profit by charging a different price in period 1.

Given the monopolist’s pricing strategy, clearly consumers have no incentives to deviate from their equilibrium strategy given (9) and (10). This concludes the proof.

Proposition 9.6: When the software is sold via subscription-based licensing only, given (9) and (10), the unique SPNE of the game is such that high-type consumers subscribe to the software in both periods, and low-type consumers subscribe only in period 1.

Proof. Fix a pure strategy SPNE. The highest price consistent with all low-type consumers subscribing in period 0 is $p _ { l , 0 } = v _ { L } + e - c _ { \mathrm { ~  ~ } }$ , in which case the monopolist’s maximum payoff is $\boldsymbol { v } _ { L } + \boldsymbol { e } - \boldsymbol { c } + \delta$ max $\{ \beta ( v _ { H } + \beta e ) , v _ { L } + e \}$ . The highest price consistent with all high-type consumers subscribing in period 0 is $p _ { l , 0 } = v _ { H } + \beta e - c - \delta ( v _ { H } - v _ { L } )$ , in which case the monopolist’s maximum payoff is $\beta v _ { H } - \beta c + e \mathrm { ~ . ~ }$ $\beta ^ { 2 } + \delta v _ { L } + \delta e - \delta ( 1 - \beta ) c$ . The monopolist achieves this payoff by selling to the low-type consumers in period 1. Given (9), one can show that the second payoff is higher than the first. Since the monoplist’s optimum is to charge the highest price consistent with a given level of sales, the unique pure strategy SPNE is such that high-type consumers subscribe in period 0, and all consumers subscribe in period 1. This concludes the proof.

Subscription-based Licensing Result 2: When the intensity of network effects is large such that either (9) does not hold $( { \mathrm { i . e . , } } ( 1 - \beta ^ { 2 } ) e >$ $\beta v _ { H } - v _ { L } + ( 1 - \delta ) ( 1 - \beta ) c )$ , or (10) does not hold $( \mathrm { i . e . , ~ } ( 1 - \beta ) e > ( 1 - \delta ) ( v _ { H } - v _ { L } )$ ), and $v _ { L } + e > \beta ( v _ { H } + \beta e )$ (or $( 1 - \beta ^ { 2 } ) e >$ $\beta v _ { H } - v _ { L } )$ , there is an unique SPNE in which all consumers subscribe to the software in both periods. Note that (9) does not hold implies $v _ { L } + e > \beta ( v _ { H } + \beta e )$

Consider the following strategy profile:

High-type consumers: In period 0, subscribe to the software if $p _ { l , 0 } \leq$ max $\{ v _ { H } + \beta e - c - \delta ( v _ { H } - v _ { L } ) , v _ { L } + e - c \}$ . In period 1, having subscribed previously, subscribe again if $p _ { l , 0 } > v _ { L } + e - c$ and $r _ { 1 } \le v _ { H } + e ,$ , or $p _ { l , 0 } \leq v _ { L } + e - c$ and $r _ { 1 } \leq$ max $\{ v _ { H } + \beta e , v _ { L } + e \}$ ; having not subscribed previously, subscribe if $p _ { l , 1 } \leq$ max $\{ v _ { H } + \beta e - c , v _ { L } + e - c \}$

• Low-type consumers: In period 0, subscribe to the software $\mathrm { i f } p _ { l , 0 } \leq v _ { L } + e - c .$ . In period 1, having subscribed previously, subscribe again $\mathrm { i f } r _ { 1 } \le v _ { L } + e ;$ having not subscribed previously, subscribe if $p _ { l , 1 } \leq v _ { L } + e - c$

• The monopolist’s pricing strategy: In period $0 , p _ { l , 0 } = v _ { L } + e - c$ . In period 1, $\begin{array} { r } { r _ { 1 } = v _ { L } + e ; } \end{array}$ and $p _ { l , 1 } = v _ { L } + e - c .$

Proposition 9.7: When the software is sold via subscription-based licensing only, given that either (9) does not hold, or (10) does not hold, and $v _ { L } + e > \beta ( v _ { H } + \beta e ) ( o r ( 1 - \beta ^ { 2 } ) e > \beta v _ { H } - v _ { L } )$ , the above strategy profile is an SPNE. The monopolist’s equilibrium profit is $v _ { L } +$ $e - c + \delta ( v _ { L } + e )$

Proof. Given consumers’ strategy, the monopolist cannot improve his profit by charging a different price in period 0. This is because if $v _ { H } +$ $\beta e - c - \delta ( v _ { H } - v _ { L } ) > v _ { L } + e - c _ { \ O }$ , or (10) holds, charging any price $p _ { l , 0 }$ such that $p _ { l , 0 } < v _ { L } + e - c$ or $v _ { L } + e - c < p _ { l , 0 } < v _ { H } + \beta e -$ $c - \delta ( v _ { H } - v _ { L } )$ is suboptimal since the monopolist does not charge the highest price for a given sales. If $p _ { l , 0 } = v _ { H } + \beta e - c - \delta ( v _ { H } - v _ { L } )$ , then only high-type consumers subscribe in period 0. The monopolist’s maximum profit is

$$
\begin{array}{r l} & {\beta (v _ {H} + \beta e - c - \delta (v _ {H} - v _ {L})) + \delta (\beta (v _ {H} + e) + (1 - \beta) (v _ {L} + e - c))} \\ & {= \beta v _ {H} + \delta v _ {L} + \beta^ {2} e + \delta e - \beta c - \delta (1 - \beta) c} \end{array}
$$

This is less than his equilibrium payoff, given (9) does not hold. $\mathrm { I f } p _ { l , 0 } > v _ { H } + \beta e - c - \delta ( v _ { H } - v _ { L } )$ , then the monopolist’s maximum profit <sup>is</sup> ?? max $\{ \beta ( v _ { H } + \beta e - c ) , v _ { L } + e - c \}$ , which is less than his equilibrium profit.

When $v _ { H } + \beta e - c - \delta ( v _ { H } - v _ { L } ) < v _ { L } + e - c ,$ or (10) does not hold, the monopolist does not benefit from deviating to any price such that $p _ { l , 0 } < v _ { L } + e - c _ { : }$ , since lower prices do not generate higher demand. One can show that the monopolist also does not benefit from deviation to any price $p _ { l , 0 } > v _ { L } + e - c ,$ given $v _ { L } + e > \beta ( v _ { H } + \beta e )$ . Clearly, given consumers’ strategy, the monopolist cannot improve his profit by charging different prices in period 1 given $v _ { L } + e > \beta ( v _ { H } + \beta e )$

Given the monopolist’s pricing strategy, one can show that consumers do not benefit from deviating from the above strategy. Finally, note that if (9) does not hold, then we have $v _ { L } + e > \beta ( v _ { H } + \beta e ) ( \mathrm { o r } ( 1 - \beta ^ { 2 } ) e > \beta v _ { H } - v _ { L } )$ . That is, the latter is a broader condition. This concludes the proof.

Proposition 9.8: When the software is sold via subscription-based licensing only, given that either (9) does not hold, or (10) does not hold, and $v _ { L } + e > \beta ( v _ { H } + \beta e ) ~ ( o r ~ ( 1 - \beta ^ { 2 } ) e > \beta v _ { H } - v _ { L } )$ , the unique SPNE is such that all consumers subscribe to the software in both periods.

Proof. Fix a pure strategy SPNE. The highest price consistent with low-type consumers subscribing in period 0 is $p _ { l , 0 } = v _ { L } + e - c ,$ in which case the monopolist’s maximum payoff is

$$
\begin{array}{r l} & v _ {L} + e - c + \delta \max \{\beta (v _ {H} + \beta e), v _ {L} + e \} \\ & = v _ {L} + e - c + \delta (v _ {L} + e) \end{array}
$$

given (9) does not hold or $v _ { L } + e > \beta ( v _ { H } + \beta e )$

The highest price consistent with high-type consumers subscribing in period 0 is $p _ { l , 0 } \leq$ max $\{ v _ { H } + \beta e - c - \delta ( v _ { H } - v _ { L } ) , v _ { L } + e - c \}$ . When $v _ { H } + \beta e - c - \delta ( v _ { H } - v _ { L } ) > v _ { L } + e - c$ , or (10) holds $( \mathrm { i . e . , } ( 1 - \delta ) ( v _ { H } - v _ { L } ) > ( 1 - \beta ) e )$ , the monopolist’s maximum payoff i

$$
\begin{array}{r l} & {\beta (v _ {H} + \beta e - c - \delta (v _ {H} - v _ {L})) + \delta (\beta (v _ {H} + e) + (1 - \beta) (v _ {L} + e - c))} \\ & {= \beta v _ {H} - \beta c + e \cdot \beta^ {2} + \delta v _ {L} + \delta e - \delta (1 - \beta) c} \end{array}
$$

The monopolist achieves this payoff by selling to low-type consumers in period 1. Given that (9) does not hold, one can show that the second payoff is lower than the first. Since the monopolist’s optimum is to charge the highest price consistent with a given level of sales, the unique pure strategy SPNE is to sell to all consumers in period 0.

When $v _ { H } + \beta e - c - \delta ( v _ { H } - v _ { L } ) < v _ { L } + e - c ,$ or (10) does not hold $( \mathrm { i . e . , } ( 1 - \delta ) ( v _ { H } - v _ { L } ) < ( 1 - \beta ) e )$ , clearly the monopolist cannot gain from lowering his price in period 0, and the unique pure strategy SPNE is such that all consumers subscribe in period 0. Finally, given $v _ { L } + e > \beta ( v _ { H } + \beta e )$ (note that the opposite of (9) implies this), the unique equilibrium in period 1 is such that all consumers renew their subscription. This concludes the proof.

Subscription-based Licensing Result 3: When the intensity of network effects is intermediary such that (10) does not hold, and $v _ { L } + e <$ $\beta ( v _ { H } + \beta e ) ( \mathrm { o r } ( 1 - \beta ^ { 2 } ) e < \beta v _ { H } - v _ { L } )$ , there is an unique SPNE in which all consumers subscribe to the software in period 0 but only high-type consumers renew their subscription in period 1.

Consider the following strategy profile:

High-type consumers: In period 0, subscribe to the software if ${ p _ { l , 0 } } \le$ max $\{ v _ { H } + \beta e - c - \delta ( v _ { H } - v _ { L } ) , v _ { L } + e - c \}$ . In period 1, having subscribed previously, subscribe again if $p _ { l . 0 } > v _ { L } + e - c$ and $r _ { 1 } \leq v _ { H } + e ,$ , or $p _ { l , 0 } \leq v _ { L } + e - c$ and $r _ { 1 } \le \operatorname* { m a x } { \{ v _ { H } + \beta e , v _ { L } + e \} }$ ; having not subscribed previously, subscribe if ${ p _ { l , 1 } \leq }$ max $\{ v _ { H } + \beta e - c , v _ { L } + e - c \} .$

• Low-type consumers: In period 0, subscribe to the software if $p _ { l , 0 } \leq v _ { L } + e - c$ . In period 1, having subscribed previously, subscribe again $\mathrm { i f } r _ { 1 } \le v _ { L } + e ;$ having not subscribed previously, subscribe i $\mathrm { f } p _ { l , 1 } \leq v _ { L } + e - c$

• The monopolist’s pricing strategy: In period $0 , p _ { l , 0 } = v _ { L } + e - c$ . In period 1, $, r _ { 1 } = v _ { H } + \beta e ; \mathrm { a n d } p _ { l , 1 } = v _ { L } + e - c .$

Proposition 9.9: When the software is sold via subscription-based licensing only, given that (10) does not hold (or $( 1 - \beta ) e >$ $( 1 - \delta ) ( v _ { H } - v _ { L } ) )$ , and $v _ { L } + e < \beta ( v _ { H } + \beta e ) ~ ( o r ~ ( 1 - \beta ^ { 2 } ) e < \beta v _ { H } - v _ { L } )$ ), the above strategy profile is an SPNE. The monopolist’s equilibrium profit is $v _ { L } + e - c + \delta \beta ( v _ { H } + \beta e )$

Proof. Note that $( 1 - \beta ) e > ( 1 - \delta ) ( v _ { H } - v _ { L } )$ implies

$$
v _ {H} + \beta e - c - \delta (v _ {H} - v _ {L}) <   v _ {L} + e - c
$$

Given consumers’ strategy, the monopolist cannot improve his profit by charging a different price in period 0. This is because if $p _ { l , 0 } < v _ { L } +$ $e - c$ , then the monopolist lowers the price without gaining additional demand. $\mathrm { I f } p _ { l , 0 } > v _ { L } + e - c .$ then no consumers subscribe in period $0 ,$ and the monopolist’s maximum profit is <sub>?? max</sub> $\{ \beta ( v _ { H } + \beta e - c ) , v _ { L } + e - c \}$ , which is less than his equilibrium profit. In addition, the monopolist cannot improve his profit by charging a different price in period 1 given $v _ { L } + e < \beta ( v _ { H } + \beta e )$

Proposition 9.10: When the software is sold via subscription-based licensing only, and the intensity of network effects is intermediary such that $( 1 - \beta ) e > ( 1 - \delta ) ( v _ { H } - v _ { L } )$ , and $( 1 - \beta ^ { 2 } ) e < \beta v _ { H } - v _ { L }$ , the unique SPNE is such that all consumers subscribe to the software in period 0, but only high-type consumers renew their subscription in period 1.

Proof. Fix a pure strategy SPNE. The highest price consistent with all low-type consumers subscribing in period 0 i $p _ { l , 0 } = v _ { L } + e - c ,$ in which case the monopolist’s maximum payoff is $v _ { L } + e - c + \delta \beta ( v _ { H } + \beta e )$ , given $( 1 - \beta ^ { 2 } ) e < \beta v _ { H } - v _ { L }$ . The highest price consistent with all high-type consumers subscribing in period 0 is $p _ { l , 0 } = v _ { L } + e - c ,$ given $( 1 - \beta ) e > ( 1 - \delta ) ( v _ { H } - v _ { L } )$ , in which case all consumers subscribe in period 0, and the monopolist’s maximum payoff is again $v _ { L } + e - c + \delta \beta ( v _ { H } + \beta e )$ . Since the monoplist’s optimum is to charge the highest price consistent with a given level of sales, the unique pure strategy SPNE is such that all consumers subscribe in period 0, and only high-type consumers renew in period 1. This concludes the proof.

Now compare the profitability of perpetual licensing and subscription-based licensing in the presence of network effects, the following proposition shows that they are equally profitable when the intensity of network effects is high or low. When the intensity of network effects is intermediary, however, perpetual licensing is more profitable than subscription-based licensing.

Proposition 9.11: Perpetual licensing is as profitable as subscription-based licensing when <sub>??</sub> is large such that (9) does not hold or <sub>??</sub> is small such that both (9) and (10) hold. Perpetual licensing is more profitable than subscription-based licensing when (9) holds but (10) does not hold $( o r ~ ( 1 - \beta ) e > ( 1 - \delta ) ( v _ { H } - v _ { L } ) , a n d ( 1 - \beta ^ { 2 } ) e < \beta v _ { H } - v _ { L } + ( 1 - \delta ) ( 1 - \beta ) c )$

Proof. When $( 1 - \beta ) e > ( 1 - \delta ) ( v _ { H } - v _ { L } )$ , and $( 1 - \beta ^ { 2 } ) e < \beta v _ { H } - v _ { L }$ , the monopolist’s optimal profit under subscription-based licensing is $v _ { L } + e - c + \delta \beta ( v _ { H } + \beta e )$ , that under perpetual licensing is $\beta v _ { H } + \delta v _ { L } + ( \beta ^ { 2 } + \delta ) e - \delta ( 1 - \beta ) c - \beta c$ . One can show that

$$
\begin{array}{r} \beta v _ {H} + \delta v _ {L} + (\beta^ {2} + \delta) e - \delta (1 - \beta) c - \beta c > v _ {L} + e - c + \delta \beta (v _ {H} + \beta e) \Leftrightarrow \\ \beta v _ {H} - v _ {L} + (1 - \beta) c > (1 - \beta^ {2}) e \end{array}
$$

Thus, perpetual licensing is more profitable. When $\beta v _ { H } - v _ { L } < ( 1 - \beta ^ { 2 } ) e < \beta v _ { H } - v _ { L } + ( 1 - \delta ) ( 1 - \beta ) c$ and $( 1 - \beta ) e > ( 1 - \delta ) ( v _ { H } -$ $v _ { L } )$ , the monopolist’s optimal profit under subscription-based licensing is $v _ { L } + e - c + \delta ( v _ { L } + e )$ , and that under perpetual licensing is $\bar { \beta v _ { H } } + \delta v _ { L } + \bar { ( \beta ^ { 2 } + \delta ) e } - \delta ( \bar { 1 - \beta } ) c - \beta c$ . One can show tha

$$
\begin{array}{r} \beta v _ {H} + \delta v _ {L} + (\beta^ {2} + \delta) e - \delta (1 - \beta) c - \beta c > v _ {L} + e - c + \delta (v _ {L} + e) \Leftrightarrow \\ \beta v _ {H} - v _ {L} + (1 - \delta) (1 - \beta) c > (1 - \beta^ {2}) e \end{array}
$$

Thus, perpetual licensing is more profitable. This concludes the proof.

Proposition 10: Network Effects with Valuation Uncertainty

• When the intensity of network effects is low such tha $\begin{array} { r } { e \leq m a x \ \left\{ \frac { \beta v _ { H } - v _ { L } } { 1 - \beta ^ { 2 } } , \frac { \psi ^ { H } E [ v | H ] - E [ v | L ] + ( 1 - \delta ) \psi ^ { L } c } { \psi ^ { L } ( 1 + \psi ^ { H } ) } \right\} } \end{array}$ , either perpetual licensing or subscription-based licensing can be optimal.

• When the intensity of network effects is high such that <sub>??</sub> <sub>></sub> <sub>????</sub> $\left\{ \frac { \beta v _ { H } - v _ { L } } { 1 - \beta ^ { 2 } } , \frac { \psi ^ { H } E [ v | H ] - E [ v | L ] + ( 1 - \delta ) \psi ^ { L } c } { \psi ^ { L } ( 1 + \psi ^ { H } ) } \right\}$ <sub>,</sub> perpetual licensing and subscription-based licensing are equally profitable. In equilibrium, all consumers adopt the software in both periods.

Proof of Proposition 10.

This proposition is proven through a series of intermediary results. Specifically, Propositions 10.1-10.4 prove the existence of an SPNE and its uniqueness when the software is sold via perpetual licensing only. Propositions 10.5-10.6 prove the existence of an SPNE and its uniqueness when the software is sold via subscription-based licensing only. Proposition 10.7 compares the profitability of perpetual licensing with that of subscription-based licensing in the presence of network effects.

Perpetual Licensing Result 1: When the intensity of network effects is high such that

$$
e > \frac {\psi^ {H} E [ v | H ] - E [ v | L ] + (1 - \delta) \psi^ {L} c}{\psi^ {L} (1 + \psi^ {H})}\tag{11}
$$

there is an unique SPNE in which all consumers buy in period 0.

Consider the following strategy profile:

Consumers receiving the high-type signal: In period 0, buy if $\begin{array} { r } { \dot { p } _ { s , 0 } \leq \operatorname* { m a x } \left\{ ( 1 + \delta ) ( E [ v | L ] + e ) - c , E [ v | H ] + \delta E [ v | L ] - c + \right. } \end{array}$ $e \psi ^ { H } + \delta e \}$ . In period 1, buy $\mathrm { i f } p _ { s , 1 } \leq \operatorname* { m a x } { \left\{ E [ v | H ] + \psi ^ { H } e - c , E [ v | L ] + e - c \right\} }$

• Consumers receiving the low-type signal: In period 0, buy $\mathrm { i f } p _ { s , 0 } \leq ( 1 + \delta ) ( E [ v | L ] + e ) - c .$ In period 1, buy $\mathrm { i f } p _ { s , 1 } \leq E [ v | L ] +$

$$
e - c.
$$

• The monopolist’s strategy is to set $p _ { s , 0 } = ( 1 + \delta ) ( E [ v | L ] + e ) - c , \mathrm { a n d } p _ { s , 1 } = E [ v | L ] + e - c .$

Proposition 10.1: When the software is sold via perpetual licensing only, given (11), the above strategy profile is an SPNE. The monopolist’s profit in equilibrium is $( 1 + \delta ) ( E [ v | L ] + e ) - c$

Proof. Given consumers’ strategy, the monopolist cannot improve his profit by charging a different price in period 0. This is because first, clearly charging any price $p _ { s , 0 }$ such that $p _ { s , 0 } < ( 1 + \delta ) ( E [ \bar { v } | L ] + e ) - c \mathrm { ~ o r ~ } ( 1 + \delta ) ( \bar { E } [ v | L ] + e ) - c < p _ { s , 0 } < E [ v | H ] + \delta E [ v | L ] - c + e ^ { - 1 }$ $e { \psi } ^ { H } \cdot$ <sub>+ ??</sub> is suboptimal. One can show that

$$
(1 + \delta) (E [ v | L ] + e) - c <   E [ v | H ] + \delta E [ v | L ] - c + e \psi^ {H} + \delta e \Leftrightarrow \psi^ {L} e <   E [ v | H ] - E [ v | L ]
$$

When $\psi ^ { L } e > E [ v | H ] - E [ v | L ]$ , clearly the monopolist cannot gain from deviating from the equilibrium prices. When $\psi ^ { L } e < E [ v | H ] -$ $E [ v | L ]$ , consider a deviation $p _ { s , 0 } = E [ v | H ] + \delta E [ v | L ] - c + e \psi ^ { H } + \delta$ . The maximum payoff from this deviation is

$$
\begin{array}{r l} & {\psi^ {H} (E [ v | H ] + \delta E [ v | L ] - c + e \psi^ {H} + \delta e) + \delta \psi^ {L} (E [ v | L ] + e - c)} \\ & {= \psi^ {H} E [ v | H ] + \delta E [ v | L ] + (\psi^ {H} \psi^ {H} + \delta) e - \delta \psi^ {L} c - \psi^ {H} c} \end{array}
$$

which is less than the monopolist’s equilibrium payoff given (11). If $p _ { s , 0 } > \operatorname* { m a x }  \{ ( 1 + \delta ) ( E [ v | L ] + e ) - c , E [ v | H ] + \delta E [ v | L ] - c + $ $e \psi ^ { H } + \delta e \}$ , then the maximum payoff that the monopolist can gain from this deviation is <sub>?? max</sub> $\{ \psi ^ { H } ( E [ v | H ] + \psi ^ { H } e - c ) , E [ v | L ] + e - c \}$ which is less than the monopolist’s equilibrium payoff. Since in equilibrium all consumers buy the software in period 0, the monopolist cannot gain from deviating in period 1.

Given the monopolist’s pricing strategy, one can show that consumers have no incentives to deviate. This concludes the proof.

Proposition 10.2: When the software is sold via perpetual licensing only, given (11), the unique pure strategy SPNE is such that all consumers buy the software in period 0.

Proof. Fix a pure strategy SPNE. The highest price consistent with consumers receiving the low-type signal to buy in period 0 is $p _ { s , 0 } =$ $( 1 + \delta ) ( E [ v | L ] + e ) - c ,$ in which case the monopolist’s maximum payoff is $( 1 + \delta ) ( E [ v | L ] + e ) - c$ . The highest price consistent with consumers receiving the high-type signal to buy in period 0 is $p _ { s , 0 } = ( 1 + \delta ) ( E [ v | L ] + e ) - c , { \mathrm { i f } } \psi ^ { L } e > E [ v | H ] - E [ v | L ]$ , in which case all consumers buy in period 0, and the monopolist’s maximum payoff is again $( 1 + \delta ) ( E [ v | L ] + e ) - c$ . The highest price consistent with consumers receiving the high-type signal to buy in period 0 is $p _ { s , 0 } = E [ v | H ] + \delta E [ v | L ] - c + e \psi ^ { H } + \delta e , { \mathrm { i f } } \psi ^ { L } e < E [ v | H ] - E [ v | L ]$ , in which case only consumers receiving the high-type signal buy in period 0, and the monopolist’s maximum payoff is $\psi ^ { H } E [ v | H ] + \delta E [ v | L ] +$ $( \psi ^ { H } \psi ^ { H } + \delta ) \dot { e } - \delta \psi ^ { L } c - \psi ^ { H } c$ , which is less than the monopolist’s equilibrium payoff given (11). Since the monopolist’s optimum is to charge the highest price consistent with a given level of sales, the unique pure strategy SPNE is such that all consumers buy in period 0. This concludes the proof.

Perpetual Licensing Result 2: When the intensity of network effects is high such that (11) does not hold, there is an unique SPNE in which consumers who receive the high-type signal buy in period 0, and consumers who receive the low-type signal buy in period 1.

Note that since (11) does not hold, o $e < ( \psi ^ { H } E [ v | H ] - E [ v | L ] + ( 1 - \delta ) \psi ^ { L } c ) / \big ( \psi ^ { L } ( 1 + \psi ^ { H } ) \big )$ , one can show that $( 1 + \delta ) ( E [ v | L ] + e ) -$ $c < E [ v | H ] + \delta E [ v | L ] - c + e \psi ^ { H } + \delta e , \mathrm { a n d } E [ v | L ] + e - c < E [ v | H ] + \psi ^ { H } e - c .$ Consider the following strategy profile:

• Consumers receiving the high-type signal: In period 0, buy $\mathrm { i f } p _ { s , 0 } \leq E [ v | H ] + \delta E [ v | L ] - c + e \psi ^ { H } + \delta e$ . In period 1, buy $\mathrm { i f } p _ { s , 1 } \leq$ $E [ v | H ] + \psi ^ { H } e - c$

Consumers receiving the low-type signal: In period 0, buy $\mathrm { i f } p _ { s , 0 } \leq ( 1 + \delta ) ( E [ v | L ] + e ) - c$ . In period 1, buy $\mathrm { i f } p _ { s , 1 } \leq E [ v | L ] + e -$ ??<sup>.</sup>

The monopolist’s strategy is to set $p _ { s , 0 } = E [ v | H ] + \delta E [ v | L ] - c + e \psi ^ { H } + \delta e , \mathrm { a n d } p _ { s , 1 } = E [ v | L ] + e - c .$

Proposition 10.3: When the software is sold via perpetual licensing only, given (11) does not hold, the above strategy profile is an SPNE. The monopolist’s profit in equilibrium is $\psi ^ { H } E [ v | \bar { H } ] + \delta E [ v | L ] + ( \bar { \psi } ^ { H } \psi ^ { \dot { H } } + \delta ) e - \delta \psi ^ { L } c - \psi ^ { H } c .$

Proof. Given consumers’ strategy, the monopolist cannot improve his profit by charging a different price in period 0. This is because first, clearly charging any price $p _ { s , 0 }$ such that $p _ { s , 0 } < ( 1 + \delta ) ( E [ \bar { v } | L ] + e ) - c \mathrm { ~ o r ~ } ( 1 + \delta ) ( \bar { E } [ v | L ] + e ) - c < p _ { s , 0 } < E [ v | H ] + \delta E [ v | L ] - c + e ^ { - 1 }$ $e \psi ^ { H } + \delta e$ is suboptimal. Consider a deviation $p _ { s , 0 } = ( 1 + \delta ) ( E [ v | L ] + e ) - c$ . The maximum payoff from this deviation is $( 1 + \delta ) ( E [ v | L ] + e ) - c .$ , which is less than the monopolist’s equilibrium payoff given (11) does not hold. $\mathrm { I f } p _ { s , 0 } > E [ v | H ] + \delta E [ v | L ] -$ $c + e \psi ^ { H } + \delta e$ , then the maximum payoff that the monopolist can gain from this deviation is $\{ \psi ^ { H } ( E [ v | H ] + \psi ^ { H } e - c ) , E [ v | L ] + e -$ $c \} ,$ , which is less than the monopolist’s equilibrium payoff. Clearly, the monopolist cannot gain from deviating in period 1.

Given the monopolist’s pricing strategy, one can show that consumers have no incentives to deviate. This concludes the proof.

Proposition 10.4: When the software is sold via perpetual licensing only, given (11) does not hold, the unique pure strategy SPNE is such that consumers receiving the high-type signal buy in period 0, and consumers receiving the low-type signal buy in period 1.

Proof. Fix a pure strategy SPNE. The highest price consistent with consumers receiving the low-type signal to buy in period 0 is $p _ { s , 0 } =$ $( 1 + \delta ) ( E [ v | L ] + e ) - c ,$ in which case the monopolist’s maximum payoff is $( 1 + \delta ) ( E [ v | L ] + e ) - c .$ which is less than the monopolist’s equilibrium payoff given that (11) does not hold. The highest price consistent with consumers receiving the high-type signal to buy in period 0 is $p _ { s , 0 } = \bar { E } [ v | H ] + \delta E [ v | L ] - c + e \psi ^ { H } + \delta e$ , given (11) does not hold. Since the monopolist’s optimum is to charge the highest price consistent with a given level of sales, the unique pure strategy SPNE is such that only consumers receiving the high-type signal buy in period $0 ,$ and consumers receiving the low-type signal buy in period 1. This concludes the proof.

Subscription-based Licensing Result 1: When the intensity of network effects is high such that

$$
e > \max \left\{\frac {\beta v _ {H} - v _ {L}}{1 - \beta^ {2}}, \frac {\psi^ {H} E [ v | H ] - E [ v | L ] + (1 - \delta) \psi^ {L} c}{\psi^ {L} (1 + \psi^ {H})} \right\}
$$

there is an unique SPNE in which all consumers subscribe in both periods. The monopolist’s equilibrium profit is $( 1 + \delta ) ( E [ v | L ] + e ) - c$ Consider the following strategy profile:

Consumers receiving the high-type signal: In period 0, subscribe if $p _ { l , 0 } \leq$ max $\{ E [ v | H ] + \delta E [ v | L ] - c + \psi ^ { H } e - \delta v _ { L } , ( 1 + \delta ) E [ v | L ] +$ $e - c - \delta v _ { I . } \}$ . In period 1, subscribe for the first time if $p _ { 1 } \leq$ max $\{ E [ v | H ] + \psi ^ { H } e - c , E [ v | L ] + e - c \}$

Consumers receiving the low-type signal: In period 0, subscribe $\mathrm { i f } p _ { l , 0 } \leq ( 1 + \delta ) E [ v | L ] + e - c - \delta v _ { L }$ . In period 1, subscribe for the first time i $\begin{array} { r } { \mathrm { f } p _ { 1 } \leq E [ v | L ] + e - c . } \end{array}$

• Returning leasees: Renew if $v + e \geq r ,$

• The monopolist’s strategy is to set $p _ { l , 0 } = ( 1 + \delta ) E [ v | L ] + e - c - \delta v _ { L } , \mathrm { a n d } r = v _ { L } + e , p _ { 1 } = E [ v | L ] + e - c .$

Proposition 10.5: When the software is sold via subscription-based licensing only, given $e > ( \beta v _ { H } - v _ { L } ) / ( 1 - \beta ^ { 2 } )$ , and (11), the above strategy profile is an SPNE. The monopolist’s profit in equilibrium is $( 1 + \delta ) ( E [ v | L ] + e ) - c .$

Proof. Given consumers’ strategy, the monopolist cannot improve his profit by charging a different price in period 0. This is because first, clearly charging any price $p _ { l , 0 }$ such that $\bar { p } _ { l , 0 } < ( 1 + \delta ) ( \bar { E } [ v | L ] + \bar { e } ) - c - \delta v _ { L } \mathrm { o r } ( 1 + \delta ) ( E [ v | \bar { L } ] + e ) - c - \delta v _ { L } < p _ { l , 0 } < E [ v | H ] + e v _ { L } < p _ { l , 0 } .$ $\delta E [ v | L ] - c + \psi ^ { H } e + \delta e - \delta \dot { v } _ { L }$ is suboptimal. Note that

$$
(1 + \delta) E [ v | L ] + e - c - \delta v _ {L} <   E [ v | H ] + \delta E [ v | L ] - c + \psi^ {H} e - \delta v _ {L} \Leftrightarrow \psi^ {L} e <   E [ v | H ] - E [ v | L ]
$$

When $\psi ^ { L } e > E [ v | H ] - E [ v | L ]$ , the monopolist clearly cannot gain from deviation. When $\psi ^ { L } e < E [ v | H ] - E [ v | L ]$ , consider a deviation $p _ { l , 0 } = E [ v | H ] + \delta E [ v | L ] - c + \psi ^ { H } e - \delta v _ { L }$ . The maximum payoff from this deviation is

$$
\begin{array}{r l} & {\psi^ {H} (E [ v | H ] + \delta E [ v | L ] - c + \psi^ {H} e - \delta v _ {L}) + \delta \big (\psi^ {H} (v _ {L} + e) + \psi^ {L} (E [ v | L ] + e - c) \big)} \\ & {= \psi^ {H} E [ v | H ] + \delta E [ v | L ] - \psi^ {H} c + \psi^ {H} \psi^ {H} e + \delta e - \delta \psi^ {L} c} \end{array}
$$

which is less than the monopolist’s equilibrium payoff given (11). One can show that it is suboptimal for the monopolist to price such that no consumers subscribe in period 0. Clearly, the monopolist cannot gain from deviating in period 1 given $e > ( \beta v _ { H } - v _ { L } ) / ( 1 - \beta ^ { 2 } )$ .

Proposition 10.6: When the software is sold via subscription-based licensing only, given $e > ( \beta v _ { H } - v _ { L } ) / ( 1 - \beta ^ { 2 } )$ , and (11), the unique pure strategy SPNE is such that all consumers subscribe in both periods.

Proof. Fix a pure strategy SPNE. The highest price consistent with consumers receiving the low-type signal to subscribe in period 0 is $p _ { s , 0 } =$ $( 1 + \delta ) E [ v | L ] + e - c - \delta v _ { L } ,$ , in which case the monopolist’s maximum payoff is $( 1 + \delta ) ( E [ v | L ] + e ) - c .$ , given that $e > ( \beta v _ { H } - v _ { L } ) /$ $( 1 - \beta ^ { 2 } )$ . The highest price consistent with consumers receiving the high-type signal to subscribe in period 0 is $p _ { s , 0 } = E [ v | H ] + \delta E [ v | L ] -$ $c + \psi ^ { H } e - \delta v _ { L }$ , in which case the monopolist’s maximum payoff is $\psi ^ { H } E [ v | H ] + \delta E [ v | L ] - \psi ^ { H } c + \psi ^ { H } \psi ^ { H } e + \delta e - \delta \psi ^ { L } c$ , which is less than $( 1 + \delta ) ( E [ v | L ] + e ) - c$ given $( I I ) .$ Since the monopolist’s optimum is to charge the highest price consistent with a given level of sales, the unique pure strategy SPNE is such that all consumers subscribe to the software in both periods. This concludes the proof.

## Proposition 10.7: Profit comparison

With consumers’ value uncertainty, when the intensity of network effects is strong such that

$$
e > \max \left\{\frac {\beta v _ {H} - v _ {L}}{1 - \beta^ {2}}, \frac {\psi^ {H} E [ v | H ] - E [ v | L ] + (1 - \delta) \psi^ {L} c}{\psi^ {L} (1 + \psi^ {H})} \right\}
$$

perpetual licensing and subscription-based licensing are equally profitable. When the intensity of network effects is weak such that $e \leq$ max $\left\{ \frac { \beta v _ { H } - v _ { L } } { 1 - \beta ^ { 2 } } , \frac { \psi ^ { H } E [ v | H ] - E [ v | L ] + ( \bar { 1 } - \delta ) \psi ^ { L } c } { \psi ^ { L } ( 1 + \psi ^ { H } ) } \right\}$ , either perpetual licensing or subscription-based licensing can be optimal.

Proof. A direct result of Propositions 10.1through 10.6.

Lemma 1. Under perpetual licensing, as far as the residual demand in period $( x _ { H , n } , x _ { L , n } )$ is positive, in an SPNE, the sales in period t is also positive.

Proof. This can be proved by contradiction. Assume this is not true, and in period $t \geq 0 _ { ; }$ , the monopolist’s optimal pricing strategy is such that no consumers buy the software even though there is demand in the market. Clearly, not selling to the remaining consumers forever is not optimal since the marginal cost is zero. If the monopolist’s sales is positive in a future period $t ^ { \prime } > t ,$ then one can show that in the subgame starting in period <sub>??</sub> , the monopolist can improve his profit by setting $p _ { s , t + n } = p _ { s , t ^ { \prime } + n } , n = 0 , \ldots , \infty$ . Contradiction. Therefore, in equilibrium, the monopolist’s sales is positive until there is no more demand in the market.

Proposition 11: In an infinite-period model, when consumers know their true valuation for the software, subscription-based licensing is more profitable than perpetual licensing

## Proof of Proposition 11.

A direct result of the monopolist’s profit under perpetual and subscription-based licensing.

Proposition 12: In an infinite-period model, when consumers do not know their true valuation for the software prior to adoption, either subscription-based or perpetual licensing can be optimal. In particular, perpetual licensing is optimal when either one of the following two sets of conditions holds: $I ) E [ v | L ] > \beta v _ { H }$ , and $\begin{array} { r l } & { \Big ( 1 + \frac { \delta ^ { 2 } } { 1 - \delta } \Big ) E [ v | L ] > ( 1 - \delta ) \psi ^ { H } E [ v | H ] + ( 1 - \delta ) \psi ^ { L } c + \delta \left( \alpha + \frac { \delta } { 1 - \delta } \right) \beta v _ { H } ; 2 ) \psi ^ { H } E [ v | H ] + ( 1 - \delta ) \psi ^ { L } c + \delta \left( \alpha + \frac { \delta } { 1 - \delta } \right) \beta v _ { H } . } \end{array}$ $\begin{array} { r } { \frac { \delta } { 1 - \delta } E [ v | L ] > \alpha \beta v _ { H } + \frac { \delta } { 1 - \delta } \beta v _ { H } , \mathrm { a n d } \psi ^ { H } E [ v | H ] + \frac { 2 \delta ^ { - 1 } } { 1 - \delta } E [ v | L ] + ( 1 - \delta ) \psi ^ { L } c > \frac { \delta } { 1 - \delta } \beta v _ { H } . } \end{array}$

## Proof of Proposition 12.

We know that

$$
\pi_ {P S X 1} = \psi^ {H} E [ v | H ] + \frac {\delta}{1 - \delta} E [ v | L ] - \psi^ {H} c - \delta \psi^ {L} c
$$

$$
\pi_ {P S X 2} = \frac {1}{1 - \delta} E [ v | L ] - c
$$

$$
\pi_ {P L X 1} = \psi^ {H} E [ v | H ] - \delta \psi^ {H} E [ v | H ] + \delta E [ v | L ] - \psi^ {H} c - \delta \psi^ {L} c + \delta \left(\alpha + \frac {\delta}{1 - \delta}\right) \beta v _ {H}
$$

$$
\pi_ {P L X 2} = E [ v | L ] - c + \delta \frac {\beta v _ {H}}{1 - \delta}
$$

By comparing the monopolist’s profit under the 4 pricing strategies, one can obtain the results in the proposition. This concludes the proof.

## Appendix B

## Assumption on the Vendor’s Ability to Recognize Prior Customers

Below we show that our key results do not rely on the assumption that the monopolist vendor is able to recognize prior customers. In particular, we prove that if the monopolist cannot differentiate between new and existing customers, then subscription-based licensing is more profitable than perpetual licensing without consumer value uncertainty. However, with value uncertainty, perpetual licensing can be more profitable than subscription-based licensing. These findings are consistent with those in the paper.

Specifically, assume that in the two-period model, the monopolist cannot distinguish between new and existing customers. In this case, in period 1, the monopolist has to lease his software to all customers at the same price, or $r _ { 1 } = p _ { 1 }$ . Let us first examine the model without customer value uncertainty (or $\alpha = 1 )$ . Note that the monopolist’s ability to distinguish new and existing customers only affects his profit from subscription-based licensing. This is because with perpetual licensing, once a consumer has bought the software, she exits the market. Thus, below we solve for the optimal subscription-based licensing prices and then compare the monopolist’s profit under perpetual licensing with that under subscription-based licensing.

## A Two-Period Model Without Customer Value Uncertainty

When the software is sold via subscription-based licensing only, in period 1, a consumer with valuation who has subscribed to the software in period 0 subscribe again if the benefit is higher than the cost, or $v \geq p _ { 1 }$ . A consumer who has never subscribed to the software subscribe for the first time if $v - c \geq p _ { 1 }$ . In period 0, a consumer subscribes to the software if the payoff of subscribing in period 0 is no less than that of subscribing for the first time in period 1 or of not subscribing at all. That is,

$$
v - c - p _ {l, 0} + \delta \max (v - E p _ {1}, 0) \geq \max \{\delta (v - c - E p _ {1}), 0 \}
$$

The monopolist’s pricing problem can be solved via backward induction. One can show that when $\beta v _ { H } > v _ { L }$ , the unique SPNE of the game is characterized by the following strategy profile:

The monopolist’s strategy: In period $\begin{array} { r } { \mathrm { , ~ } p _ { l , 0 } = v _ { H } - c ; } \end{array}$ ; in period 1, $p _ { 1 } = v _ { H }$

A consumer’s strategy: In period 0, subscribe if $v - c \geq p _ { l , 0 }$ . In period 1, having not subscribed previously, subscribe if $v - c \geq p _ { 1 } ;$ ; having subscribed previously, subscribe again if $v \geq p _ { 1 }$

In equilibrium, high-type consumers subscribe to the software in both periods, and low-type consumers never adopt the software. The monopolist’s optimal profit is $\beta ( v _ { H } - c ) + \delta \beta v _ { H }$ . Comparing this profit with the monopolist’s optimal profit under perpetual licensing (i.e., $\beta ( v _ { H } + \delta v _ { L } - c ) + \delta ( 1 - \beta ) ( v _ { L } - c ) )$ , one can show that subscription-based licensing is more profitable than perpetual licensing without consumers’ value uncertainty. These findings confirm those of the classic durable-goods theories: Subscription-based licensing is more profitable than perpetual licensing without customer value uncertainty. This is because under subscription-based licensing, the monopolis can enforce the same monopolistic price for access to the software in each period.

Proposition A2.1: Without customer value uncertainty, if the monopolist is unable to separate new and existing customers, then subscription-based licensing is more profitable than perpetual licensing.

## A Two-Period Model with Customer Value Uncertainty

When the software is only sold via subscription-based licensing, in period 1, a consumer who receives signal and does not subscribe to the software in period 0 subscribe for the first time if the expected benefit from adoption is higher than the cost, or $E [ v | y ] - c \geq p _ { 1 } . \mathrm { A }$ returning customer, after learning her valuation for the software <sub>??</sub>, subscribes to the software again in period 1 if the benefit is higher than the price, or $v \geq p _ { 1 } .$ . In period 0, a consumer who receives signal <sub>??</sub> subscribes to the software if the expected payoff from subscribing in period 0 is no less than that from delaying adoption until period 1 or from not adopting at all, or

$$
\begin{array}{r l} & E [ v | y ] - c - p _ {l, 0} + \delta \max \left(0, \psi_ {H y} (v _ {H} - E p _ {1}), E [ v | y ] - E p _ {1}\right) \\ & \geq \max \left\{0, \delta (E [ v | y ] - c - E p _ {1}) \right\} \end{array}
$$

The monopolist’s optimal pricing strategy can be solved via backward induction. One can show that two pricing strategies can be optimal in an equilibrium:

## The PL1anon strategy:

If $\dot { } E [ v | L ] - c > v _ { L } ,$ and $\alpha \beta v _ { H } >$ max $\{ ( E [ v | L ] - c ) ( \psi ^ { L } + \alpha \beta ) , v _ { L } \}$ , then in period $0 , p _ { l , 0 } = E [ v | H ] - c$ . In period 1, $p _ { 1 } = v _ { H }$ . The monopolist’s profit is $\psi ^ { H } ( E [ v | H ] - c ) + \delta \alpha \beta v _ { H } ,$

If $E [ v | L ] - c > v _ { L } ,$ and $v _ { L } > \mathrm { m a x } \left\{ \alpha \beta v _ { H } , ( E [ v | L ] - c ) ( \psi ^ { L } + \alpha \beta ) \right\}$ , then in period $0 , p _ { l , 0 } = E [ v | H ] - c + \delta c$ . In period $1 , p _ { 1 } = v _ { L }$ The monopolist’s profit is $\psi ^ { H } ( E [ v | H ] - c + \delta c ) + \delta v _ { L }$

• If $E [ v | L ] - c > v _ { L }$ , and $( E [ v | L ] - c ) ( \psi ^ { L } + \alpha \beta ) > \operatorname* { m a x } { \{ \alpha \beta v _ { H } , v _ { L } \} }$ , then in period $0 , p _ { l , 0 } = E [ v | H ] - c + \delta \psi _ { H H } ( v _ { H } - E [ v | L ] +$ $c ) - \delta ( E [ v | H ] - E [ v | L ] )$ . In period $1 , p _ { 1 } = E [ v | L ] - c$ . The monopolist’s profit is $\psi ^ { H } E [ v | H ] + \delta ( 1 - \alpha ) ( 1 - \beta ) v _ { L } + \delta E [ v | L ] -$ $\delta \psi ^ { L } c - \psi ^ { H } c$

$\mathrm { I f } \ E [ v | L ] - c < v _ { L } ,$ and $\alpha \beta v _ { H } > E [ v | L ] - c ,$ then in period 0, $\begin{array} { r } { { } , p _ { l , 0 } = E [ v | H ] - c . } \end{array}$ In period 1, $p _ { 1 } = v _ { H } .$ . The monopolist’s profit is $\psi ^ { H } ( E [ v | H ] - c ) + \delta \alpha \beta v _ { H }$

$\mathrm { I f } \ \alpha \beta v _ { H } < E [ v | L ] - c < v _ { L }$ , then in period $0 , p _ { l . 0 } = E [ v | H ] - c + \delta c$ . In period 1, $p _ { 1 } = E [ v | L ] - c$ . The monopolist’s profit is $\psi ^ { H } ( E [ v | H ] - c + \delta c ) + \delta ( E [ v | L ] - c ) = \psi ^ { H } ( E [ \dot { v } | H ] - c ) + \delta E [ v | L ] - \delta \psi ^ { L } c$

The PL2anon strategy: In period 0, $\begin{array} { r } { p _ { l , 0 } = E [ v | L ] - c . } \end{array}$ . In period 1, $p _ { 1 } = v _ { H }$

When the monopolist follows the PL1anon strategy, on the equilibrium path, consumers receiving the high-type signal subscribe to the software as soon as they enter the market. When the monopolist follows the PL2anon strategy, on the equilibrium path, all consumers subscribe to the software as soon as they enter the market, and only renew their subscription in period 1 if their true types are the high type. The monopolist’s overall profit in equilibrium is $E [ v | L ] - c + \delta \beta v _ { H }$

Compare the profitability of the two subscription-based licensing strategies with that of perpetual licensing through the PS1 or PS2 strategies, one can show the following results:

Proposition A2.2: With customer valuation uncertainty, if the monopolist is unable to separate new and existing clients, then perpetual licensing is more profitable than subscription-based licensing if

$E [ v | L ] - c + \delta \beta v _ { H } < \psi ^ { H } E [ v | H ] - \psi ^ { H } c + \delta E [ v | L ] - \delta \psi ^ { L } c$ and either one of the following three sets conditions hold: $I ) \alpha \beta v _ { H } <$ $E [ v | L ] - \psi ^ { L } c , \ a n d \ E [ v | L ] - c > v _ { L } , a n d \ \alpha \beta v _ { H } > \operatorname* { m a x } \left\{ ( E [ v | L ] - c ) ( \psi ^ { L } + \alpha \beta ) , v _ { L } ) ; \ o r \ \vec { \jmath } \ \alpha \beta v _ { H } < E [ v | L ] - \psi ^ { L } c , \right.$ and $E [ v | L ] -$ $c < v _ { L } , a n d \alpha \beta v _ { H } > E [ v | L ] - c ; o r 3 ) c + v _ { L } < E [ v | L ]$ and $E [ v | L ] - c > v _ { L } ,$ and $v _ { L } > \alpha \beta v _ { H }$ and $v _ { L } > ( E [ v | L ] - c ) ( \psi ^ { L } + \alpha \beta ) ;$

or $\beta v _ { H } < E [ v | L ]$ and either one of the following five sets of conditions hold: $I ) \ E [ v | L ] - c > v _ { L }$ , and $\alpha \beta v _ { H } > \operatorname* { m a x }  \left\{ ( E [ v | L ] - \right.$ $c ) ( \psi ^ { L } + \alpha \beta ) , v _ { L } \}$ and $\psi ^ { H } ( E [ v | H ] - c ) + \delta \alpha \beta v _ { H } < ( 1 + \delta ) E [ v | L ] - c \ ; \quad 2 ) E [ v | L ] - c > v _ { L }$ , and $v _ { L } >$ max $\{ \alpha \beta v _ { H } , ( E [ v | L ] -$ $c ) ( \psi ^ { L } + \alpha \beta ) \}$ and $\psi ^ { H } ( E [ v | H ] - c + \delta c ) + \delta v _ { L } < ( 1 + \delta ) E [ v | L ] - c , \ : \ : \ : 3 ) \ : \ : \ : E [ v | L ] - c > v _ { L }$ , and $( E [ v | L ] - c ) ( \psi ^ { L } + \alpha \beta ) >$ max $\{ \alpha \beta v _ { H } , v _ { L } \} , \ a n d \psi ^ { H } E [ v | H ] + \delta ( 1 - \alpha ) ( 1 - \beta ) v _ { L } - \delta \psi ^ { L } c + \psi ^ { L } c < E [ v | L ] ; \ \mathcal { I } \ [ v | L ] - c < v _ { L } , \ a n d \alpha \beta v _ { H } > E [ v | L ] - c .$ , and $\psi ^ { H } ( E [ v | H ] - c ) + \delta \alpha \beta v _ { H } < ( 1 + \delta ) E [ v | L ] - c ; \ s ) \alpha \beta v _ { H } < E [ v | L ] - c < v _ { L } , \ a n d \psi ^ { H } ( E [ v | H ] - c ) - \delta \psi ^ { L } c < E [ v | L ] - c ;$

Otherwise, subscription-based licensing is more profitable.

In summary, when the monopolist is unable to recognize prior customers, subscription-based licensing is optimal without customer valuation uncertainty. In contrast, either perpetual licensing or subscription-based licensing can be optimal with customer valuation uncertainty. Therefore, our main findings regarding how customer valuation uncertainty changes the relative profitability of perpetual and subscriptionbased licensing continue to hold whether the monopolist is able to recognize prior customers or not.

## Appendix C

## Comparison between Valuation and Usage Volume Uncertainty

In this appendix, we compare the revenue implication of customer valuation uncertainty with that of usage volume uncertainty. We show that whereas customer valuation uncertainty changes the relative profitability of perpetual licensing versus subscription-based licensing, usage volume uncertainty does not.

First, let us consider customers’ usage volume uncertainty and its impact on the optimal software licensing strategy. The utility that a customer gains from using the software for one period after full implementation is the product of her type (<sub>??</sub>) and her usage volume in that period $( q _ { t } ) ,$ or . A customer’s type represents her valuation for using one unit of the software service. We preserve the assumption that within each generation, a fraction $\beta$ of the customers are high types with valuation $v = v _ { H }$ , and a fraction $1 - \beta$ are low types with valuation $v = v _ { L }$ $0 < v _ { L } < v _ { H } )$ . This valuation is known to the customer (or no valuation uncertainty), not to the monopolist, and it does not change with time. Software implementation requires an upfront implementation cost <sub>??.</sub>

A customer’s usage volume may fluctuate from one period to another. Specifically, a customer’s usage volume in period <sub>??</sub> may be high $( q _ { t } =$ $q _ { H } )$ or low $( q _ { t } = q _ { L } )$ , where $0 < q _ { L } < q _ { H }$ , and it is revealed to the customer only at the beginning of period <sub>??</sub>. In the initial period $( t = 0 )$ half of the customers have high demand $( q = q _ { H } )$ , and half have low demand $( q = q _ { L } )$ . It is assumed that a customer’s usage volume in each period is determined by exogenous factors $( \mathrm { e . g . }$ , macroeconomic conditions) and is independent of her type <sub>??</sub>, and also $v _ { L } q _ { L } \ge c$ . Customers usage volume changes over time according to a Markov transition matrix, defined by

$$
T = \left[ \begin{array}{c c} 1 - \rho & \rho \\ \rho & 1 - \rho \end{array} \right]
$$

and $\rho \in \left[ 0 , 1 / 2 \right]$ . That is, given period-<sub>??</sub>’s usage volume $q _ { t } ,$ , with probability $1 - \rho , q _ { t + 1 }$ is the same as $q _ { t } ;$ and with probability $\rho ,$ it changes to the alternative quantity. It is assumed that to gain value from using the software in period , a customer needs to own or subscribe to at least enough capacity to cover her required capacity $q _ { t }$ . This includes the possibility that a customer may have bought more than what she needs in period <sub>??</sub>. The monopolist sells either perpetual or subscription-based licenses of the software and charges based on customers desired usage volume.

When the software is sold via perpetual licensing only, in each period, the monopolist announces three prices: a price for buying at quantity $q _ { H } , \mathrm { o r } p _ { s , t } ( q _ { H } ) .$ , a price for buying at quantity $q _ { L } , \operatorname * { o r } p _ { s , t } ( q _ { L } )$ , and a price for prior customers to buy additional quantity $( q _ { H } - q _ { L } ) ,$ , or $r _ { t }$ . When the software is sold via subscription-based licensing only, in each period, the monopolist announces four prices: a price for subscription at quantity $q _ { H } , p _ { l , t } ( q _ { H } )$ , a price for subscription at quantity $q _ { L } , p _ { l , t } ( q _ { L } )$ , a price for renewing subscription at quantity $q _ { H } , r _ { t } ( q _ { H } )$ , and a price for renewing subscription at quantity $q _ { L } , r _ { t } ( q _ { L } )$ . Note this is a very general setup that allows linear or nonlinear usage-based pricing. Customers observe the prices and make a purchase decision, anticipating their overall payoff.

We first solve the optimal perpetual and subscription-based licensing strategies separately and then compare their profitability. The detailed analysis is available upon request. We show that two sets of perpetual licensing strategies can be optimal in an equilibrium: the PS1u strategy and the PS2u strategy. Given the PS1u strategy, on the equilibrium path, customers with valuation $v = v _ { H }$ buy the software at their desired usage volume $q _ { 0 }$ in period $^ { 0 , }$ customers with valuation $v = v _ { L }$ buy the software at their desired usage volume $q _ { 1 }$ in period 1, and customers with $v = v _ { H }$ and whose usage volume changes from $q _ { 0 } = q _ { L }$ to $q _ { 1 } = q _ { H }$ buy additional units in period 1. In contrast, given the PS2u strategy, on the equilibrium path, only customers with valuation $v = v _ { H }$ and $q _ { 0 } = q _ { H }$ buy the software in period <sub>0</sub>. The other customers either delay adoption until period 1 or do not adopt the software.

Two sets of subscription-based licensing strategies can be optimal in an equilibrium: the PL1u strategy and the PL2u strategy. Given the PL1u strategy, on the equilibrium path, customers with valuation $v = v _ { H }$ subscribe to the software at their desired usage volume $q _ { 0 }$ in period <sub>0</sub>, and renew their subscription at their desired usage volume $q _ { 1 }$ in period 1. Customers with valuation $v = v _ { L }$ subscribe to the software at their desired usage volume $q _ { 1 }$ only in period 1. In contrast, given the PL2u strategy, on the equilibrium path, only customers with valuation $v = v _ { H }$ and $q _ { 0 } = q _ { H }$ subscribe to the software in period <sub>0</sub> and renew their subscription in period 1. The other customers either delay adoption until period 1 or do not adopt the software.

Compare the profitability of the two perpetual licensing and subscription-based licensing strategies, we show that the PS1u strategy is as profitable as the PL1u strategy, and the PS2u strategy is as profitable as the PL2u strategy. Combining term-based pricing (perpetual or subscription-based licensing) with usage-based pricing improves the monopolist’s profit from both perpetual licensing and subscriptionbased licensing, but does not change their relative profitability. Formally,

Proposition A3.1: When customers face usage volume uncertainty, but not value uncertainty, subscription-based licensing is as profitable as perpetual licensing.

Our findings show that customers’ usage volume uncertainty does not change the relative profitability of perpetual and subscription-based licensing. In contrast, our paper shows that customers’ value uncertainty does change the relative profitability of perpetual and subscriptionbased licensing. Therefore, customer valuation uncertainty and usage volume uncertainty have very different revenue implications for software vendors.

Xin/Impact of Customer Valuation Uncertainty on Software Licensing
