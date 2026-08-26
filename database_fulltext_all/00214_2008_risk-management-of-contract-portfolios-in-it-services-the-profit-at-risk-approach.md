---
otero_id: 214
otero_key: "3VW66SDT"
title: "Risk Management of Contract Portfolios in IT Services: The Profit-at-Risk Approach"
authors: "Robert J. Kauffman; Ryan Sougstad"
year: "2008"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222250102"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/3VW66SDT/fulltext/images/d305a213e9751ce6cae6deabcc13918054d8218b8065dc97e98ed333ebb0ee1f.jpg)

# Risk Management of Contract Portfolios in IT Services: The Profit-at-Risk Approach

Robert J. Kauffman & Ryan Sougstad

To cite this article: Robert J. Kauffman & Ryan Sougstad (2008) Risk Management of Contract Portfolios in IT Services: The Profit-at-Risk Approach, Journal of Management Information Systems, 25:1, 17-48

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222250102

![](/api/attachments/3VW66SDT/fulltext/images/9eaa2b429858bc2cf96ade44d5f41e420c10bc912cb3f228e93367c78ef4f23c.jpg)

Published online: 08 Dec 2014.

![](/api/attachments/3VW66SDT/fulltext/images/be7c06a817f64f00b705558a5e4f628ba9428cd1451f6f8f99b305b77042265b.jpg)

Submit your article to this journal

Article views: 29

![](/api/attachments/3VW66SDT/fulltext/images/64a7cc49938e05b28baad9668bfe1ddfd5e3a6eff6e3624c8188880fbb3d83a6.jpg)

View related articles

# Risk Management of Contract Portfolios in IT Services: The Profit-at-Risk Approach

Ro ber t J. Kauffman and Ryan So ugs tad

Rober t J. Kauffman is the W.P. Carey Chair in Information Systems at the W.P. Carey School of Business, Arizona State University. He has served on the faculty at New York University, the University of Minnesota, and the University of Rochester, and worked in international banking and finance. He is also past director of the MIS Research Center, University of Minnesota. His research interests span the economics of IS, financial markets, technology adoption, competitive strategy and technology, IT value, strategic pricing and technology, supply chain management, and theory development and empirical methods for IS research. He has won numerous research awards, including the 2006 outstanding research contribution award for modeling and strategic decision-making research on embedded standards in technology-based products from the IEEE International Society for Engineering Management, and the 2007 best research award from the Journal of the Association of Information Systems for theory-building research in the area of product and market transparency made possible by information technology. His recent paper on value-at-risk in IT services management was also runner-up to the conference winner at the 2007 Hawaii International Conference on System Sciences. His publications appear in Information Systems Research, Journal of Management Information Systems, MIS Quarterly, Management Science, Organization Science, and other leading journals.

Ryan Sougs tad is a Ph.D. candidate in Information and Decision Sciences at the Carl son School of Management of the University of Minnesota. He previously served as a faculty member at National American University in Rapid City, South Dakota. He has seven years of experience in client sales and marketing with the IBM Corporation. Mr. Sougstad holds an MBA from the University of Texas at Dallas. His research interests are centered on portfolio management and the development and application of methods from financial economics and finance in support of senior management decision making for information technology investment evaluation. His research on real option analysis and IT portfolios appeared in the Journal of Management Information Systems and Advances in Management Information Systems. He is currently conducting research on the application of techniques from financial risk management in the context of IT services.

Abs tr act: Information technology (IT) services providers are exposed to exogenous risks faced by the industry as a whole, and endogenous risks from their current portfolio of IT contracts. This exposure may lead to cost overruns or legal responsibility for service-level breeches. Providers can leverage information about their risk positions implied by their IT services contract portfolios to gain strategic advantage over their competitors. We build theory in support of a new construct, profit-at-risk, for evaluating the trade-offs between contract profitability and service-level risk, stemming from financial economics theory and models. We simulate an IT services contract portfolio, and show how managers can reduce organizational risk by forgoing profit-maximizing contracts in lieu of more conservative service-level agreements, yet still achieve high returns. Our approach provides decision support for ex ante contract evaluation and negotiation, and a means to conduct ex post efficiency evaluation. It also aligns IT service management with best practices in financial management.

Key wor ds and phr as es : efficient frontier, financial economics, IT contracts, IT services, managerial decision making, mechanism design, portfolio management, profit-at-risk, service science, value-at-risk.

Advances in open-s tandar ds ar chitectur e, information and communications technologies, and the realization of large offshore talent pools have led to an increase in service-driven information technology (IT) solutions [43]. Recent developments in grid computing, Web services, application service providers (ASPs), and business process outsourcing (BPO) allow firms to adopt flexible, service-driven solutions. Some pundits predict the end of the traditional model of IT acquisition in favor of a purely service-driven technology marketplace [22]. In addition, many technology vendors are now touting flexible, service-driven approaches to IT delivery, such as IBM’s On Demand Computing and HP’s Adaptive Enterprise.<sup>1</sup> Service-driven IT strategies reduce the requirements for up-front investments for user firms and permit shared exposure of many technology risks with the vendors through contracts [33].

Structuring IT services contracts poses unique challenges for service providers. With the increased flexibility offered by service-driven IT solutions comes increased complexity and exposure to risk. IT services contracts typically cover a vast array of terms, such as service level, quality, timeliness, and penalties and incentives, around these contractual parameters. Such contractual obligations, in fact, are contingent li abilities to which the vendors are obligated.<sup>2</sup> Underscoring many of these liabilities are risks involving technology costs, standards, and skills. Established IT service vendors with multiple contracts across a diverse client base can be thought of as managers of financial portfolios, the value of which will be determined by the interaction of underlying risk factors among client contracts. Decisions regarding an individual contract may impact the overall risk exposure of a provider’s portfolio. For example, a manager may obligate the firm to provide a specialized programming skill as part of a contract to which the firm already faces availability constraints. While the manager may have made a profit or revenue-maximizing decision regarding the structure of the contract, the added contingent liability may subject the firm to unacceptable risk to the profitability of its overall IT services contract portfolio. In addition, risk exposures may differ according to technology or even across labor markets for IT outsourcing [26]. We propose an analytic model and a decision support approach to quantify the fundamental trade-offs related to IS contract service levels, profitability, and risk.

Sourcing IT solutions in the form of services implies a new breed of risks for user firms, such as misappropriation of sensitive information and incentive alignments [29, 38, 46]. Indeed, such risks and approaches to risk mitigation have long been the subject of information systems (IS) research [4, 16, 28]. Bhargava and Sundaresan [19] model a pricing scheme for utility computing services and show that the service vendor is an aggregator of user demand risk. User firms can increase capacity in their contract without the up-front investment required in a traditional IT solution strategy. Thus, the vendor takes on the risk of the individual user firm’s demand uncertainty.

Service-driven IT solutions allow for a great deal of managerial flexibility and risk sharing between IS users and their service vendors. However, this flexibility implies an increased number of decision criteria for both clients and vendors. In a servicedriven solution, the contract contains many parameters that parties must negotiate. These parameters will affect not only the value of the solution or contract at hand but also the value of the overall portfolio of contracts a firm holds. Contractual parameters such as service and security level, service sourcing, timing, incentives, and penalties transfer demand and performance risk from the clients to the providers, which can lead to cost overruns. Contractual risk factors will either amplify the overall risk exposure of a firm, or lessen it due to negative correlations that allow for strategic hedging of IT services contracts.<sup>3</sup> Managers are faced with a fundamental trade-off: how to maximize the profitability of services contracts while maintaining an acceptable level of risk exposure to the overall contract portfolio.

New methods and quantitative tools are required to actively manage both individual contractual profitability and overall portfolio value and risk tolerance. Thus, we ask the following fundamental research questions:

RQ1: How should an IT services vendor optimally set contractual parameters given an acceptable level of firmwide contract portfolio risk?

RQ2: How can we achieve a better understanding of risk exposure in IT services contracts to inform managerial decision making?

We develop our evaluative approach using value-at-risk (VaR) concepts from financial economics, a theory base that offers unique potential for the study of IS economics and management issues [8, 29, 47, 48]. Value-at-risk represents the worst expected losses at a given confidence level based on an estimated distribution of returns. We build on the value-at-risk approach to develop the measure of profit-at-risk in IT services contracts, a measure that allows managers to quantify risk exposure with rigor, but at the same time offers a meaningful, approachable means of decision analysis.<sup>4</sup>

## Background Literature

This r es ear ch dr aws on thr ee pr imar y theor etical pers pectives . The VaR literature from financial economics structures managerial decision making with regard to risk tolerance. The IS real option analysis literature informs the modeling of IT risk factors and the value of managerial flexibility in the context of sequential IT investments. Finally, the pricing of IT services and information economics provides insights that support the formulation of our new modeling approach for IT services portfolio management.

## Value-at-Risk

VaR portfolio analysis techniques were pioneered by a team at J.P. Morgan in New York City. Jorion [42] defines value-at-risk as a measurement of the worst expected loss over a given time horizon under normal market conditions at a given confidence interval.<sup>5</sup> For example, a value-at-risk of \$10 million at 95 percent confidence and over a time horizon of 30 days implies that the manager can be confident, with 95 percent certainty, that the loss will not exceed \$10 million over the next 30 days. One of the strengths of the VaR approach is this rather simple and intuitive framework for understanding a risk position. The clarity of this approach is especially appealing to managers of IT services, who would likely have less exposure to the theories and methods of risk management as compared to their financial services counterparts.

The need for new risk management techniques was motivated in part by several major financial calamities in the late 1980s and early 1990s, including the fall of Barings Bank [31, 41, 50] and other international financial problems, and the Orange County, California treasury disaster [41, 42]. VaR provided management with a new means to better understand and control firmwide risk exposure. Initially, financial institutions used VaR analysis for passive information reporting to understand their risk exposures. However, VaR techniques quickly grew toward defensive information reporting, where firms began to implement standards and controls to avoid large-scale disasters. As a result, VaR is now used as an active risk management tool. Today, VaR theory and the associated methodologies for controlling risk in lending and credit, money market and derivative instrument trading, and investment management operations are advanced. VaR methods are widely accepted as a basic part of a financial firm’s risk management tool kit, which is essential for the effective management of overall portfolio risks.

Several researchers have examined optimal portfolio construction under VaR constraints. Liebowitz and Kogelman [51] and Lucas and Klaassen [54] were among the first to construct optimal portfolios subject to shortfall constraints in the form of minimum returns. Campbell et al. [21] developed a model to optimize portfolio selection between stock and bond investments in a VaR framework. Anderson et al. [3] produced a model of credit risk optimization under conditional value-at-risk, which addresses the issue of kurtosis by taking a mean value of expected losses.<sup>6</sup>

## Real Options Analysis of IT Investments

Real options analysis in IS provides both strategic and quantitative approaches to analyzing the role of flexibility in the face of IT project uncertainties. In traditional financial economics [20, 30], an option gives the bearer the right, but not obligation, to buy or sell an asset at a given price at a given point in time. Real options apply this concept to real assets, such as IT asset investments, to help managers to value the flexibility of options such as the ability to expand, abandon, or defer investments [12, 34]. Real options analysis has been used in three primary ways. First, real options can be viewed as a strategy that places emphasis on active managerial choices of flexibility-enabling capabilities in the face of risk and uncertainty [27]. A second approach is to employ quantitative methods to evaluate option-enhanced net present value (NPV) for projects [13, 14, 35], prioritize among investment choices [9], or evaluate combinations of real options in order to set and maintain IT project strategies [15, 16]. Finally, real options can be used to inform the investment timing decision [45, 61]. These approaches compare the value of waiting versus the project NPV; where the two are equal is the optimal time to start investing.

Real options analysis informs our VaR approach in several ways. First, the literature has made contributions toward the identification and estimation of risk factors associated with IT investments. We consider some of the same managerial issues such as timing and exit options (in terms of a contract’s start time, its duration, and its exit clauses), but from the perspective of the provider of IT services. Whereas most real options analysis considers the IT project as a capital investment, we conceptualize the IT services provider as a manager of a portfolio of contingent liabilities. Our primary concern is with the initial configuration of the contracts, because the contract con figurations dictate the degree of flexibility allowed going forward. In many respects, the contract constrains the options available to the provider.

In this paper, we use VaR methods rather than real options analysis because IT service contracts are usually characterized by complex negotiations between providers and clients regarding service-level commitments and prices [33]. Kleindorfer and Wu [49] and Wu and Kleindorfer [68] modeled contract options for both capacity and duration considerations in the context of business-to-business (B2B) exchanges. Compared with options analysis, VaR is better equipped to evaluate the dynamic give-and-take between revenue and the risk exposure to cost overruns in the market context though. In addition, one of the key “value tenets” of a large services provider is the ability to leverage resources across projects. VaR portfolio analysis provides the ability to evaluate risk and profits across a portfolio of contracts in a way that real options analysis does not. The latter is better suited to the analysis of sequential IT investments.

## IT Services Pricing

Research in IT services pricing has its roots in auction economics. Westland [67] modeled IT services prices based on congestion and network externalities, and Kauffman and Kumar [44] extended this perspective when demand and congestion externalities are countervailing in their impacts. Gupta et al. [37] developed a model for dynamic pricing of network access based on usage. Bhargava and Sundaresan [18] presented an optimization model for quality-contingent IT services and later developed a model to price grid computing solutions with demand uncertainty using an auction mechanism [19]. Cheng and Koehler [23] further specified optimal pricing policies for Webdelivered applications using queuing theory. Huang and Sundararajan [40] modeled the adoption patterns of firms utilizing on-demand computing. They considered the infrastructure choices that providers must make in order to fulfill their clients’ demand for computing. These works inform IT services research by explicitly modeling the trade-offs between the costs of providing adequate service while managing the risks and uncertainties associated with customer demand. One of the main value propositions of the IT services provider for its clients is the absorption of risk. Bhargava and Sundaresan [19] modeled one type of absorption, demand: users of grid computing services are shielded from fluctuations in demand and providers are able to absorb this risk through economies of scale. The key insight is that the risk faced by the individual client differs from the risk faced by the provider, once the provider takes over the service. We expand on this case to include other types of services risks.

Economics of information goods and software pricing research have also contributed to our research. Sundararajan [66] examined fixed-fee versus usage-based pricing of information goods in situations of incomplete information. He modeled the transaction costs associated with monitoring usage based as nonlinear pricing schemes and found that firms should offer combinations of fixed and usage-based pricing models in the face of these transaction costs. Kenyon [48] modeled IT outsourcing pricing implications in the face of variable capacity constraints on the part of providers. Choudhary [25] examined quality and versioning investments from the perspective of software as a service (SaaS) versus traditional fixed-fee licensing. He found that in most cases, software vendors will invest more in quality under SaaS strategy than under the traditional fixed-fee strategy. Dai et al. [32] modeled the effects of electronic sourcing systems on supplier/buyer relationships and the effects upon centralized versus decentralized governance. These works are important in that they consider variable and often uncertain costs associated with delivering IT services. Our model extends these concepts to consider risks associated with the cost of service delivery. These risks may be associated with cost increases in labor, contract monitoring, or infrastructure investments required to deliver the service.

One of the few works that incorporates VaR theory in an IT setting is by Paleologo [60]. He introduces a method for pricing utility computing services called price-at-risk. He argues that traditional cost-based pricing is not value-maximizing given the dynamics of utility computing services due to the reduced contract duration (versus traditional outsourcing), low customer switching cost, high levels of demand uncertainty, high sunk costs, and the short product life cycle of a utility computing infrastructure. He models these uncertainties with a confidence interval approach that has similarities to a VaR model. He also uses a stochastic process for market adoption using a form of the Bass [11] model for technology adoption.

## Model Development

IT s er vices encompas a br oad r ange of application domains . Software development and BPO, IS security services, utility computing, and Web-delivered application services are all areas in which pricing, service levels, and other parameters act as decision variables that will affect the overall profitability of the services contract. Examples of optimization parameters to consider are security and performance levels, contract timing (e.g., when to start, ability to abandon contract), the amount a firm can subcontract within the overall contract, and incentives and penalties.

## Model Specification

One of the key requirements for parameter selection is that the decision affects the customer demand, or willingness to pay (WTP) for the service.<sup>7</sup> Thus, a contract can be thought of as a complex product with differing dimensions of quality, with the different service levels acting as a quality parameter. For the model in this paper, we consider a base case in which a firm enters into an outsourcing contract for BPO. The firm chooses to offer a certain service-level mix. In this example, we consider dedicated or pooled BPO resources, such as a help desk. We define pooled resources as either subcontracted, offshore, or near-shore services; for example, a help desk call center owned by the vendor. The customer will prefer dedicated resources though; they will value the continuity and stability that dedicated resources provide. Thus, the client’s WTP is modeled as a function of the service level, which we define as the proportion of dedicated resources and pooled resources in the contract. The firm then selects a service level to maximize contract profits, subject to some level of risk, which we measure via profit-at-risk.

The profit-at-risk constraint in our proposed model is an application of value-at-risk theory and methods to IT services contract parameters. Profit-at-risk (PaR) is defined as the lowest expected profit at a given confidence for a given time horizon. Profit-at-risk is a more complex measure than value-at-risk and what we see in traditional risk-based portfolio analysis. When we apply the profit-at-risk construct, the service-level choice affects the revenue according to the client’s WTP, and also affects expected costs according to the cost function faced by the provider firm. Thus, the portfolio return is not a linear combination of individual asset returns as it is in traditional portfolio analysis. We model the costs of providing IT services as a stochastic variable. Costs will also have an expected future value, as well as a random volatility component. The overall profit-at-risk constraint is calculated by subtracting the expected cost overruns at the confidence level from the expected profits. The service-level mix affects both the contract risk and cost structure, and revenues; these measures can be used to construct the profit-at-risk estimate. To specify the profit-at-risk constraint, we consider four factors that are analogous value-at-risk inputs: mark-to-market position, risk factor variability, time horizon, and confidence interview. See Table 1 for the value-at-risk and profit-at-risk equivalents and Appendix A for a full set of definitions for the key language that we use in this research.

The choice of S affects the firm’s risk exposure to the cost parameters that occur in the process of offering the services. We examine not only the profit-at-risk of an individual contract but also the effect of a PaR position on the aggregate liability that the firm has as a result of its portfolio of contracts.

## Profit-at-Risk Analysis Approach

We consider a monopoly IT services vendor that offers two distinct levels of service— high (H) and low (L).<sup>8</sup> The service levels represent dedicated on-site resources versus pooled offshore resources, and we think of service level in aggregate in terms of the mix of these two. We assume that the service vendor negotiates with a firm that requires D fixed demand hours of service. We note that the high service level costs more for the vendor to provide, and is more volatile because the vendor has less flexibility in shifting and sharing resources. The high service level is preferred by customers because they value the stability and familiarity of the dedicated resources, and this is reflected in the WTP function. Service level S is the percentage of the hours demanded that will be fulfilled with high service level input costs, $C _ { H } .$ See Table 2 for our mathematical notation.

Table 1. Value-at-Risk Inputs and Profit-at-Risk Equivalents

<table><tr><td>Symbol</td><td>Value-at-risk input</td><td>Profit-at-risk equivalent</td></tr><tr><td>M</td><td>Mark-to-market position</td><td>C, estimated parameter cost at t = 0</td></tr><tr><td>σ</td><td>Risk factor variability</td><td>Future cost volatility</td></tr><tr><td>t</td><td>Time horizon</td><td>Time horizon</td></tr><tr><td>α</td><td>Confidence interval</td><td>Confidence interval</td></tr><tr><td>VaR estimate</td><td>Mσαt, from delta-normal method</td><td>Profit-at-risk: PaR = R(S) - C(S) - C(S)[1 + σα√t]</td></tr><tr><td>ω</td><td>Portfolio weight</td><td>The weight is placed on S, the proportion of high-level services or dedicated resources in the IT services contract input mix</td></tr></table>

Notes: Mark-to-market position represents an initial valuation of the asset or project. σ is the standard deviation of asset returns or other project factors. α is the confidence interval set by management that a threshold, called the value-at-risk, will not increase beyond over the time horizon, t. We also note that profit-at-risk (PaR) must scale to incorporate the extremes of cost increases, rather than asset losses. Thus, the value 1 + sa√t must also scale to the upper distribution. The reader should note that ω traditionally refers to the proportion of wealth that is invested in asset i in a portfolio. In the IT services provider context, this is not wealth. Instead, the availability of the highest-quality service inputs matter more, especially high-capability IT labor.

The costs can be modeled as $d C = \mu d t + \sigma d z .$ , a stochastic Gauss-Wiener process.<sup>9</sup> So the future costs will have a mean value, µdt, along with a random component, σdz, which may increase or diminish depending on market conditions or other risk factors that represent volatility. In constructing profit-at-risk, we utilize the delta-normal method of local valuation [42] rather than a full valuation method. This is a critical point for the reader to understand, since it bears on our ability to successfully apply the methods we have proposed in the IT services context.<sup>10</sup> Full valuation approaches rely on historical data to estimate distributions of asset returns. In this research, we apply VaR theory to develop a profit-at-risk measurement approach to assess the potential value, impact, and usability of risk-based assessments on IT contracts. Our simulations are limited to those that are consistent with a local valuation approach, however. This approach assumes that the risk factors affecting an asset can be modeled using an estimate of the standard deviation of assumed normally distributed asset returns. In a subsequent section, we discuss the implication and limits of local valuation methods, as well as applications where historical data can be used in order to model IT services risk factors with less restrictive assumptions.<sup>11</sup>

Table 2. Definitions of Mathematical Notation in the Model

<table><tr><td>Variable</td><td>Definition</td></tr><tr><td> $\pi$ </td><td>Firm profits</td></tr><tr><td> $S$ </td><td>Service level mix (0 percent to 100 percent)</td></tr><tr><td> $R(S)$ </td><td>Willingness to pay for service level  $S$ </td></tr><tr><td> $C(S, C_{H}, C_{L})$ </td><td>Total cost</td></tr><tr><td> $PaR$ </td><td>Contract profit-at-risk</td></tr><tr><td> $C_{H}, C_{L}$ </td><td>High (low) service level,  $H(L)$  cost</td></tr><tr><td> $\sigma_{H}, \sigma_{L}$ </td><td>Standard deviation of high (low) service level  $H(L)$  costs</td></tr><tr><td> $\rho_{HL}$ </td><td>Correlation of  $H$  and  $L$  service level costs</td></tr><tr><td> $\sigma_{c}(S, \sigma_{H}, \sigma_{L})$ </td><td>Standard deviation of total contract costs</td></tr><tr><td> $\alpha; t$ </td><td>Confidence interval; time horizon</td></tr><tr><td> $k$ </td><td> $PaR$  constraint (a constant chosen by manager)</td></tr></table>

In the general form, the objective function is:

$$
\operatorname{Max} _ {(S)} \pi = R (S) - C (S, C _ {H}, C _ {L})\tag{1}
$$

$$
\text { Subject   to: } P a R = R (S) - C (S, C _ {H}, C _ {L}) [ 1 + \sigma_ {c} (S, \sigma_ {H}, \sigma_ {L}, \rho_ {H L}) \alpha \sqrt {t} ] \geq k\tag{2}
$$

$$
0 <   S \leq 1.\tag{3}
$$

## Simulation

To simulate the model at work, we next present an example with assumed functional forms for the WTP parameter and the cost function. We first model the client’s WTP. For the purposes of this analysis, we consider the client who enters into negotiation with a range of preferences relative to service levels, S, which we model as $R ( S ) = V S ^ { 0 . 5 }$ This function states that as the mix of high-level services nears 100 percent (or 1), the firm’s WTP for the services bundle approaches the stand-alone value of the on-site services. This function is reasonable; the customer firm will be willing to pay close to the full value, V, when S nears 100 percent (or 1), indicating that all high-quality inputs are being used in the provision of the IT services. The client will be willing to pay much less for the services as S approaches 0 percent (or 0). The purpose of this functional form assumption is to simulate the client’s preferences. It does not have any substantive impact on our research contribution, which is the development and evaluation of a new risk management technique for IT services.

Our intuition is that the customer wishes to ask for dedicated on-site services and the provider wishes to negotiate some flexibility to augment on-site services with pooled shared services. The provider prefers a lower mix of the dedicated resource. We assume again that the dedicated resource is more costly and has a higher risk of cost increases. This may perhaps be due to local wage conditions and the provider’s constrained ability to shift the dedicated resources among projects. We model the total cost of the contract as a linear combination of the high or dedicated service level resources and low or pooled service level resources. By using this form, we assume that the dedicated and low service level resources are perfect substitutes from a productivity standpoint; that is, they can both perform the project requirements in the amount of hours demanded by the client (D). In addition, we assume that the firm can model the expected costs for the fixed hours demanded (D) so we do not make considerations for economies of scale in this model.<sup>12</sup>

We assume a normalized standard deviation for estimating the cost increases under the delta-normal method, rather than measures derived from actual return variances. We utilize the standard formula from financial economics for estimating a two-asset portfolio [57]. We also consider the impact of one contract to an existing portfolio of contracts. For example, a firm might have a portfolio of contractual liabilities of 60 hours of $C _ { H }$ and 30 hours of $C _ { \phantom { } _ { L } }$ . An additional contract for 10 hours will affect the overall value of the portfolio of contracts depending on service level S. Thus, if S = 50 percent, the mix of the contract portfolio would be 65 hours of $C _ { \scriptscriptstyle H }$ (five hours are added) and 35 hours of $C _ { \phantom { } _ { L } }$ (five hours also are added), resulting in a portfolio service level S = 65 percent.

Our objective function now follows:

$$
\operatorname{Max} _ {(S)} \pi = V S ^ {0. 5} D - (S C _ {H} + (1 - S) C _ {L}) D\tag{4}
$$

$$
\text { Subject   to: } P a R = V S ^ {0. 5} D - (S C _ {H} + (1 - S) C _ {L}) D\tag{5}
$$

$$
[ 1 + \sqrt {\sigma_ {H} ^ {2} S ^ {2}} + \sigma_ {L} ^ {2} (1 - S) ^ {2} + 2 S (1 - S) \sigma_ {H} \sigma_ {L} \rho_ {H L} \alpha \sqrt {t} ] \geq k
$$

$$
0 <   S \leq 1.\tag{6}
$$

In the unconstrained case, we can see that the first- and second-order necessary and sufficient conditions for maximization are as follows with respect to S:

$$
S ^ {*} = (G / 2 (C _ {H} - C _ {L})) ^ {2}\tag{7}
$$

$$
d ^ {2} \pi / d _ {2} S = - 0. 2 5 G D S ^ {- 1. 5}, \text {   where   } G, D, \text {   and   } S \geq 0.\tag{8}
$$

The related input parameter assumptions are shown in Table 3. The choice of input parameters allows us to highlight the full managerial effects of this approach, and we feel that they are reasonable in the context of the model and decision choice (dedicated on-site services versus pooled off-site or offshored services).

## Modeling Analysis and Results

We firs t examine the bas e cas e for a s ingle contr act. We extend the simulation to incorporate portfolio effects. We then consider the sensitivity of the results to timing elements and correlations. We further evaluate the managerial impact of contract investment and contract length.

Table 3. Initial Numerical Inputs for the Model

<table><tr><td>Variable</td><td>Definition</td><td>Value</td></tr><tr><td> $D$ </td><td>Services contract hours, fixed demand</td><td>100</td></tr><tr><td> $C_{H}$ </td><td>Cost of high ( $H$ ) service level</td><td>17</td></tr><tr><td> $C_{L}$ </td><td>Cost of low ( $L$ ) service level</td><td>3</td></tr><tr><td> $\sigma_{H}$ </td><td>Standard deviation of high ( $H$ ) service level costs</td><td>60 percent</td></tr><tr><td> $\sigma_{L}$ </td><td>Standard deviation of low ( $L$ ) service level costs</td><td>20 percent</td></tr><tr><td> $\rho_{HL}$ </td><td>Correlation,  $H$  and  $L$  service level costs</td><td>0</td></tr><tr><td> $S$ </td><td>Percent of portfolio in high ( $H$ ) service level</td><td>51 percent</td></tr><tr><td> $1 - S$ </td><td>Percent of portfolio in low ( $L$ ) service level</td><td>49 percent</td></tr><tr><td> $\alpha$ </td><td>Confidence interval</td><td>95 percent</td></tr><tr><td> $T$ </td><td>Time horizon</td><td>1</td></tr><tr><td> $V$ </td><td>Firm willingness to pay for high services ( $S = 1$ )</td><td>20</td></tr></table>

## Base Case Analysis: A Single Contract

## Unconstrained Profit

Table 4 illustrates our simulation of optimal profits unconstrained by any lower limits on PaR lower limits.

The second column in Table 4 (“None”) illustrates our base case. In this scenario, the firm has expected unconstrained optimal contract profits, E(π), of \$414, with an expected minimum expected contract PaR of –\$130. The optimal service-level balance is $S = 5 1$ percent in high service level costs (and thus 49% in the low service level costs).

## Profit Constrained at 95 Percent Confidence Interval

If the firm wishes to be certain at the 95 percent confidence interval that its IT services contract will not lose money (third column of Table 4, “\$0”), then the firm’s optimal service level can be achieved by rebalancing to 42 percent high service level costs and 58 percent low service level costs. Note that in this case, the expected profits are reduced by only \$6, from \$414 to \$408. Thus, for a relatively small reduction in profits, a firm can reduce its risk exposure by \$130.

## Trade-Off Analysis: Profit Versus Risk Reduction

## Profit-at-Risk Constrained at \$100

Moving right in Table 4 shows the trade-off between profitability and risk reduction. For example, a manager concerned with meeting a specific earnings target might require that the firm’s minimum profitability should be \$100. Then, the column marked \$100 is relevant. Here we see that the loss in expected profits E(π) of \$38 (= \$414 – \$376) is substantial in financial terms.

<table><tr><td>Max PaR</td><td>None</td><td>$0</td><td>$50</td><td>$100</td><td>$120</td><td>None</td></tr><tr><td>Willingness to pay (WTP)</td><td>14.29</td><td>12.92</td><td>12.16</td><td>11.00</td><td>9.98</td><td>15.49</td></tr><tr><td>Percent high service level hours (S) (in percent)</td><td>51</td><td>42</td><td>37</td><td>30</td><td>24</td><td>60</td></tr><tr><td>Contract standard deviation (in percent)</td><td>32</td><td>28</td><td>26</td><td>20</td><td>21</td><td>37</td></tr><tr><td>Revenue</td><td>1,429</td><td>1,292</td><td>1,216</td><td>1,100</td><td>997</td><td>1,549</td></tr><tr><td>Expected cost</td><td>1,014</td><td>884</td><td>818</td><td>723</td><td>648</td><td>1,140</td></tr><tr><td>Maximum cost ↑ (95 percent)</td><td>1,559</td><td>1,292</td><td>1,166</td><td>1,000</td><td>877</td><td>1,842</td></tr><tr><td>Expected contract profits (E(π))</td><td>414</td><td>408</td><td>399</td><td>376</td><td>349</td><td>409</td></tr><tr><td>Contract profit-at-risk (PaR)</td><td>-130</td><td>0</td><td>50</td><td>100</td><td>120</td><td>-293</td></tr><tr><td colspan="7">Notes: Confidence interval for analysis: 95 percent. All values are stated in thousands of dollars, except for service level S and contract standard deviation. Service-level balance is stated in terms of high service level costs as percent of total costs. PaR is an instantiation of the value-at-risk construct for the present analysis. $0, $50, $100, and $120 denote different PaR levels, based on constraints set up in the analysis. The values for willingness to pay, contract standard deviation, and S are rounded here to two decimals for appropriate precision.</td></tr></table>

<sub>pected</sub> <sub>Profits</sub> <sub>and</sub> <sub>Profit-at-Risk</sub> <sup>for</sup> <sup>Given</sup>

## Agency and Managerial Incentives

A new issue arises regarding agency, governance, and managerial incentives. Note the last column in Table 4 (also labeled “None”). In this scenario, a manager has set a service level of 60 percent (i.e., 60 percent high service level costs and 40 percent low service level costs). This is not an optimal profit structure, even though the impact to profits is marginal at $\$ 6$ . However, risk exposure more than doubles from –\$130 to –\$293. What is more troubling is that the overall revenue of the contract is higher than the optimal contract at a 51 percent service level (again, \$414 versus \$409). We should point out that many firms reward lower-level management on revenue targets, and do not consider the potential losses that may accrue at any confidence level whatsoever. So, depending on how a firm’s incentives are aligned, a manager might want to “sell” this suboptimal contract to the upper management. This is an instance where the principal’s and agent’s incentives for mechanism design are not in unison. This simulation of value-at-risk indicates that the effects to contractual decisions in IT services can go far beyond the analysis of pure profitability.

## Constraint: Profit-at-Risk > 0

Figure 1 shows the relationship between contract profitability and profit-at-risk, and supports Table 4. Profit maximization occurs at the service-level balance of S = 51 percent (x-axis). The profit-at-risk curve acts as a constraint that is imposed by management. For example, if management requires the firm to have a positive expected profit with 95 percent confidence $( P a R > 0 )$ , then the optimal service-level balance would violate the constraint. We note that the dual formulation of our problem, unconstrained profit maximization, is useful in providing a lower bound to risk exposure, which occurs at the point where S = 22 percent. This permits us to say that the contract would yield the least attractive worst-case profits at the given confidence level. Further, all contracts between the maximum profit and maximum profit-at-risk define the efficient frontier. As illustrated in Table 4, if we constrain profit-at-risk below \$120, we shift the profit-maximization point to the left. Under these parameters, profit maximization will then occur at the local maximum where the profit-at-risk constraint holds with equality. (See Appendix B for an extended analysis of the dual formulation and efficiency concerns among contracts.)

## Portfolio Impacts

## Adding a New Contract

We now consider the effects of adding the contract examined above to an existing portfolio of services contracts. Here the firm has aggregated its obligations for providing the skills in question to its existing contract portfolio of 1,000 total hours. We examine the impact on the portfolio of adding another contract (see Table 5).

The column where the balance between high and low service input costs is 51 percent and 49 percent (S = 51 percent), the unconstrained optimal, shows the additional contract adds –\$119 (= –\$151 – (–\$32)) to the risk exposure of the firm’s new profitat-risk of –\$151. We can see that if the firm has previously established a profit-at-risk constraint of \$100, then it might prefer the high-low service input costs balance of S = 42 percent, where the new contract adds no additional risk exposure. However, the initial portfolio implies that the risk exposure may be out of balance and that the firm may wish to set expected profits to a nonnegative dollar value. Thus, the manager should choose the last column, where S = 39 percent, to obtain useful guidance with risk management. Here again, the firm sacrifices profits of \$11 from the optimal structure (= \$414 – \$403), but has a 95 percent confidence interval of certainty that the firm will not incur losses over the next year.

![](/api/attachments/3VW66SDT/fulltext/images/9f20ac9e0b94daa4858fd3d58457d1d83d4db6a01fcbc1bf174c484e992a43db.jpg)  
Figure 1. Contract Profit Versus Profit-at-Risk  
Notes: The figure shows the simulated results of changes in the service-level balance and the impact on both expected profit and PaR using the inputs of Table 3. PaR is the constraint, and it is set by management. For example, if management requires the minimum profits to be positive with 95 percent certainty, then the optimal profit point (S = 51 percent) will fall outside the constraint boundary.

Table 5. Portfolio Effects When a New Contract Is Added

<table><tr><td>Variable</td><td colspan="3">Value for different high-low service balance</td></tr><tr><td>Percent high service level</td><td></td><td></td><td></td></tr><tr><td>hours (S) (in percent)</td><td>51</td><td>42</td><td>39</td></tr><tr><td>New contract expected profits</td><td>414</td><td>408</td><td>403</td></tr><tr><td>New contract profit-at-risk</td><td>130</td><td>0</td><td>32</td></tr><tr><td>Initial portfolio</td><td></td><td></td><td></td></tr><tr><td>Portfolio expected profit</td><td>4,081</td><td>4,081</td><td>4,081</td></tr><tr><td>Portfolio profit-at-risk</td><td>-32</td><td>-32</td><td>-32</td></tr><tr><td>Portfolio with new contract</td><td></td><td></td><td></td></tr><tr><td>Portfolio expected profit</td><td>4,496</td><td>4,489</td><td>4,484</td></tr><tr><td>Portfolio profit-at-risk</td><td>-151</td><td>-32</td><td>0</td></tr></table>

Notes: This table shows the effects of adding a contract to a portfolio of services contracts. All values are stated in thousands of dollars, except the service balance S. We utilize the same initial inputs in Table 3 and vary S in three different scenarios. Optimal profits occur when the service balance is S = 51 percent. However, by lowering the service value to S = 42 percent and sacrificing profits of \$7 (= \$4,496 – \$4,489), the firm can actually reduce the risk of its overall contract portfolio, as we see with contract PaR of \$0, instead of \$130 or \$32, or the service mixes of 51 percent and 39 percent.

## Leveraging a Risk Cushion

Table 6 illustrates a different scenario. Here the portfolio is initialized under conditions in which the profit-at-risk is relatively high. Thus, the manager may wish to consider the risk cushion within the contract portfolio which might enable strategic decisions to be made. For example, consider a customer who refuses to negotiate for IT services terms with less than 51 percent of services at the dedicated on-site high service level. As shown earlier, this structure, although profitable for the firm, implies significant risk exposure, with a contract profit-at-risk of \$195. However, the portfolio is able to absorb some slack. Profit-at-risk for the portfolio as a whole falls from \$195 to \$83, which is still strictly greater than zero. Thus, if the customer firm is of strategic value, the IT services vendor may be willing to sign this contract because the overall portfolio profit-at-risk is still positive.

## Extended Analysis: Correlation and Duration

The model that we pr es ented can aid s ever al other dimens ions of managerial decision making in the IT services context. Correlated risk factors and strategic portfolio hedging—two especially interesting potential applications of VaR methods for IT service providers—can be encompassed in this analysis. Most technology risk factors will exhibit correlations by which an increase in one risk factor will likely be accompanied by an increase or decrease in another separate risk factor. We consider three instances of related risk factors—negative correlation, positive correlation, and weak or very low correlation. We next extend the simulation and discussion to the issue of correlated risk factors within a services contract, as well as to contract duration.

## The Effects of Correlation of Risk Factors

The role of correlation in assessing the value outcomes of IT services portfolios is important for managerial decision makers to understand as a means to evaluate whether they are taking on appropriate risks with their mix of services business. We first explore negative correlation and cancellation of effects between risk factors as an extension to our prior analysis, and then we further consider positive risk-amplifying correlations. We close out our discussion in this subsection by discussing the effects of low or negligible correlations, and the role of nearly independent contract risk factors.

Table 6. Portfolio Risk Absorption

<table><tr><td>Scenarios</td><td>Variable</td><td>Value</td></tr><tr><td rowspan="3">New contract</td><td>S, percentage of high service level hours</td><td>51</td></tr><tr><td>New contract expected profits</td><td>414</td></tr><tr><td>New contract profit-at-risk</td><td>-130</td></tr><tr><td rowspan="2">Initial portfolio</td><td>Portfolio expected profit</td><td>4,081</td></tr><tr><td>Portfolio profit-at-risk</td><td>195</td></tr><tr><td rowspan="2">Portfolio with new contract</td><td>Portfolio expected profit</td><td>4,463</td></tr><tr><td>Portfolio profit-at-risk</td><td>83</td></tr></table>

Notes: This table shows the ability of the firm to select a profit-maximizing contract which violates the PaR > 0 constraint. Because the provider’s portfolio of existing contracts implies a positive PaR, the firm can add the profit-maximizing but risky contract with S = 51 percent while still maintaining a positive \$83 PaR for the overall contract portfolio. All values are in thousands of dollars with the exception of service balance S, which is a percentage. Initial inputs for this simulation are taken from Table 3.

## Negative Correlation of Risk Factors

A negative correlation of risk factors often occurs when two technologies are competing for standards adoption [45]. For example, the recent competition between Bluetooth and Wi‑F i has led to negatively correlated risk factors. Due to the need for standards in wireless technologies, success in one platform is likely to lead to the failure of the other technology, from a market perspective. For IT services vendors, this negative correlation likely will affect the overall risk profile of their portfolio of contractual liabilities to support their customers. The cost of supporting a nonstandard technology likely would be greater than the cost of supporting the “standards winner.” Thus the vendor may observe from the marketplace the relative likelihood of success of the two technologies. Rather than making an “all-or-nothing” choice of which standard to support, the vendor may wish to attempt to hedge its position by taking on contracts supporting each standard. As the technologies evolve and the uncertainty around a standards war lessens, managers can take corrective action by taking on new contracts or opting out of existing contracts.

Figure 2 shows the relationship between the correlation ρ and profit-at-risk values for the unconstrained point of profit maximization (S = 51 percent). The effects of correlation on risk exposure are profound. As the cost factors become negatively correlated, profit-at-risk increases, and thus the firm can expect to achieve higher minimum profit with 95 percent confidence. These points of negative correlation illustrate the effects of hedging. An IT services provider can make significant reductions in its IT services portfolio risk just by choosing contracts where the risks affecting cost volatility are negatively correlated. On the other hand, the risk positions are magnified if the risks are positively correlated. This latter observation is shown in Figure 2 by the reduction in PaR as positive correlation increases.

![](/api/attachments/3VW66SDT/fulltext/images/424cb5609eabb6b05dc56c1c409f0e0844fe4ee57e0025c86cf502f9e706a8ca.jpg)  
Figure 2. Profit-at-Risk (PaR) Versus Correlation (r) at the Profit-Maximization Point Notes: Each point on the curve represents the profit-maximizing point S = 51 percent with the initial model inputs given in Table 3. The base case occurs when the correlation r = 0. This is shown where the curve intersects the y-axis at the point where $P a R = - \$ 130$ . When r is highly negative, the value of PaR increases. As r becomes more positive, however, we see that the value of PaR decreases below the 0 correlation scenario.

In general, correlation is an important factor to consider when balancing a portfolio. Firms may wish to determine the correlation of risk factors relative to their clients by balancing the industry sectors with which they do business, for example. This is an important consideration since many IT providers have a strong presence in particular industry verticals. In addition, competing technologies are likely to exhibit significant negative correlations. For example, success in one standard may lead to the demise of another.

## Positive Correlation of Risk Factors

Many of the risk factors in IT services are likely to have positive correlations with one another. For example, an increase in labor costs around a particular technology is likely to be seen across labor markets, whether for offshore resources or dedicated resources. However, the effects are not likely to be equivalent in both labor markets, which would imply nearly perfect correlation. We further observe that even competing standards can exhibit forms of positive correlation in some settings. For example, the standards for digital music of Apple and Microsoft may exhibit positive correlations, as the success in Apple’s format, driven by iPod sales, also contributes to growth in Microsoft’s standards, given the latter’s shear dominance of the desktop platform and recent capabilities in support of digital music and media. This comes, in essence, through broad-based growth in the market. For vendors managing positive correlations in risk factors, it is important to identify how much the technologies are likely to covary in their related cost factors due to changes in shared exogenous or endogenous risk factors. Gauging this shock response is likely to be challenging for some technologies, because the provider and the clients will have little or no experience with them.

## Low and Negligible Correlations for IT Services Risk Factors

There also are many IT services in which the risk factors will exhibit low or negligible correlations. For example, IT security services and software development outsourcing are likely to involve different technologies and related skills. The kind of VaR analysis that we are advocating can help inform vendors as to the markets in which they may wish to expand. Adding additional uncorrelated independent practices or offerings will allow the vendor to lessen its overall risk position within its portfolio of contracts.

One of the main obstacles to effective correlation analysis for IT services contracts is finding appropriate estimations or proxies for correlations that might be used in the model. Technology diffusion models and simulations may be useful in this endeavor, as we have seen in the research of IBM by Paleologo [60]. Providers may be able to model firm-level or industry-sector correlations through analysis of credit risk. In addition, historical data on labor rates may provide estimates for correlations between the costs of delivering services involving particular skills or skill sets. Managers should carefully scrutinize such estimations and conduct sensitivity analysis to evaluate the impact of deviation from any estimates.

## Contract Duration

The simulations heretofore all considered a time horizon of one year for which managers evaluated the contract. In other words, we assumed that the time to fulfill the service requirements under the contract was one year. Now we consider the case where the provider can segment the contract, and consider shorter time horizons, which implies fewer hours of contractual obligation (see Figure 3).

Figure 3 models the optimal contract duration at a given service-level commitment for a firm that sets its minimum acceptable PaR equal to zero. We can see that the optimal time horizon drops as the commitment to the high-level services increases. The intuition is that firms can mitigate their risk exposure for clients who will not negotiate service levels below a certain level of on-site services. This follows the basic intuition of financial economics in that the shorter the time horizon, the lower the risk exposure. Indeed, real options analysis values the flexibility associated with an option to stage or abandon a project. Profit-at-risk analysis provides a unique but complementary insight. It evaluates the effect on risk exposure associated with various parameters of the contract, and allows providers and firms to reevaluate their relationship at key times in the project. Table 7 shows service contract profits for these different time horizons and service levels.

![](/api/attachments/3VW66SDT/fulltext/images/d426650a468ebcf02471cbb4a86ed7c7373ac24b97f7282244cbb542d521a9c6.jpg)  
Figure 3. Optimal Contract Duration at Different Service Levels for Profit at Risk > 0 Notes: In this case, the inputs of Table 3 and the functional form of the base model are used, except we chose t as the variable to optimize, again keeping the VaR constrained to be nonnegative. As the “high” service levels are demanded by the clients, the provider firm can negotiate a shorter contract duration or buyout clause in order to lessen the risk exposure. The analysis shows the trade-off between time commitments (contract duration) and risk inherent in most service agreements.

Table 7. Impact of Contract Duration on Optimal Service Levels and Profit

<table><tr><td>Percent high service level hours (S)</td><td> $t^{*}$ </td><td>Expected profits</td><td>Profit-at-risk (PaR)</td></tr><tr><td>20</td><td>1.00</td><td>314</td><td>121</td></tr><tr><td>42</td><td>1.00</td><td>408</td><td>0</td></tr><tr><td>60</td><td>0.34</td><td>139</td><td>0</td></tr><tr><td>80</td><td>0.10</td><td>39</td><td>0</td></tr><tr><td>90</td><td>0.06</td><td>19</td><td>0</td></tr></table>

Notes: We optimize profits by choosing the duration of the contract t, where 0 ≤ t ≤ 1. The intuition is that the client has a hard preference for a particular service level, but is willing to shorten the duration of the contract by staging the project. We used the initial input values shown in Table 3, with the obvious exception of S and t, which we vary for this analysis. Expected profits and profit-at-risk are in thousands of dollars.

Table 7 shows that it is possible for the firm to add a profitable contract with a minimum of risk by shortening the contract’s duration. At service levels of 20 percent and 42 percent, describing the mix of high-quality to low-quality service labor, the optimal contract duration is one year; so the firm should accept the full services offered by the company. Note that a service level of 20 percent is not profit maximizing in this illustration—note, for example, that a service level of 42 percent is at \$408—yet at the

Table 8. Optimal Time Horizon for an IT Services Contract in Portfolio, $S = 6 0$ Percent

<table><tr><td rowspan="2">Variables</td><td colspan="2">Value</td></tr><tr><td>Without Portfolio</td><td>With Portfolio</td></tr><tr><td>Duration (t)</td><td>0.34</td><td>1</td></tr><tr><td>New contract profit</td><td>139</td><td>409</td></tr><tr><td>New contract profit-at-risk</td><td>0</td><td>-293</td></tr><tr><td>Initial portfolio profit</td><td></td><td>4,030</td></tr><tr><td>Initial portfolio profit-at-risk</td><td></td><td>302</td></tr><tr><td>Portfolio with contract profit</td><td></td><td>4,439</td></tr><tr><td>Portfolio with contract profit-at-risk</td><td></td><td>72</td></tr></table>

Notes: Here we consider the impact of time horizon on the firm’s portfolio position, in a manner that is similar to the analysis in Table 5. We optimize profits subject to $P a R \ge 0 .$ In the “without portfolio” analysis, the optimal duration is short $( t = 0 . 3 4 )$ . However, the firm’s portfolio of contractual obligations for the same services implies a positive PaR of \$302. Then, portfolio profit is maximized for the new contract subject to portfolio $P a R \ge 0 .$ All values stated in thousands of dollars except duration t, which is stated in terms of continuous values between 0 and 1, representing percentages of the contract time horizon.

20 percent level, it still offers significant risk reduction opportunities in the portfolio analysis context based on the PaR of \$121.

In addition, the optimal time horizon can be modeled in the face of portfolio constraints (see Table 8). Here we have a portfolio that is set with a profit-at-risk above the threshold of \$0. Consider again a strategic client who requires a 60 percent service-level mix. Rather than absorb the additional risk of a full duration contract of one year (Table 4, last column), the provider may negotiate a shorter contract. Thus, the provider is able to sign a contract that is both profitable and minimizes risk. The provider can offer the client’s preferred service level of 60 percent dedicated resources over the full one-year time horizon and maintain a positive PaR.

## Conclusion

Fundamentally, this work has dealt with the trade-off between risk and return in IT services contract management. The use of the techniques that we described will be a function of a manager’s risk aversion. From a manager’s standpoint, the choice of confidence level may reflect the extent of the risk aversion that the person feels. Risk-seeking managers, as a result, may be more comfortable with lower odds for a minimum profit payoff than would risk-neutral or risk-averse managers. More important than the choice of confidence level though is the value which managers choose as their minimum profit threshold—what we referred to as the constant k throughout our analysis in this paper. This choice will largely be affected by the pressures faced by the managers from the outside market (e.g., the need to make earnings and to show strong growth in signings relative to their firms’ competitors), as well as the levels of risk tolerance that individual managers may exhibit in the context of their organizations.

## Contributions

This work provides a contribution to the IS literature in two ways. First, it represents one of the first robust applications of VaR methods, and qualitative risk and reward trade-offs, and begins to move the IS discipline toward the emerging services science area. Second, our research incorporates VaR analysis in an optimization model of IT service parameters in a way that provides useful and actionable managerial decision support. To illustrate why this is the case, we illustrated several scenarios where a profit-maximizing decision is not optimal relative to management’s tolerance of risk. In addition, we modeled the impact of contract duration and contract structure to risk exposure, and provided scenarios where managers can reconfigure the timing of contracts to mitigate risk. We developed an evaluative method for IT services contract portfolio assessment involving a new financial construct, profit-at-risk, which we believe can be implemented as the basis for a new and deeply insightful decision support tool. With further extensions to the data modeling and financial analytics, our profit-at-risk approach will support IT services contract negotiations and postcontract interactions between service providers and clients. The beneficial impact in reduced litigation and increased client goodwill associated with fewer service-level breeche goes beyond the quantitative measurements produced here.

## Future Research

The analytic modeling approach involving value-at-risk that we presented only scratches the surface in terms of potential applications and methods. Empirical research could be employed to estimate an efficient frontier where firms evaluate their portfolios of obligations as benchmarks against an optimal combination of risk and profitability opportunities in the contracts held in a portfolio. Another interesting approach that is consistent with other evaluative methods that firms use in the management of financial portfolios is to derive an implied confidence level by which managers would identify a profit-at-risk level. They then would be able to use a VaR analysis to calculate the probability that profit levels might dip below a certain level. This is akin to the calculation of implied volatility in option pricing, where the analyst computes the variance of returns on the underlying asset consistent with a given option price observed in the market.

Incorporating real option-based thinking will be a key modeling extension. We introduced an initial illustration of how such thinking can lead to the structuring of contracts with value-at-risk constraints. Many parameters of IT services contracts can be thought of as options; for instance, penalties and buyout clauses in service-level agreements can be priced via real option analysis. These pricing decisions may also be considered in a VaR portfolio context. In addition, contractual liabilities may be conceptualized as corporate bonds, with the default boundary, or point at which pay back is no longer viewed as viable, priced as an option to abandon the contract.

An additional avenue to explore is the impact of risk-mitigating investments that the provider can make. For example, quality control programs such as ISO 9001 and Six Sigma may greatly reduce the uncertainty and risk associated with service delivery. Profit-at-risk analysis could provide a useful means to measure quality improvements that might not translate into measurable cost reductions. Another interesting application would be the effects of capacity investments on the client’s risk position. For example, a provider will often make fixed-capacity investments, both in technology and labor, to exploit economies of scale. This additional capacity would likely reduce risk exposures associated with fluctuations in customer demand.

Customers of IT services will also benefit as providers will be more willing to absorb new client risks in their IT services offerings. We expect that the methods that we described can also be applied in other IS settings; for example, in assessing the risks associated with the bundling of information goods [7], evaluating information security services, and assessing other information practices in the firm. In addition, large firms will be able to leverage the profit-at-risk approach in the context of shared services to more accurately assess transfer costs with considerations for risk exposure.

The ultimate direction for research is the development of decision support tools based on the model we proposed. Such tools would incorporate the profit-at-risk approach in real-time analysis. Rather than focusing on the impact of additional contracts to the portfolio, active portfolio management could be implemented to enable new decision analysis approaches beyond those modeled in this paper. This will permit IT services managers to make informed choices about the levels of their investments and contractual decisions, such as extensions or withdrawal from services agreements. In addition, firms can use this approach to make strategic choices on headcount requirements and resource deployment decisions. Such analysis will further inform recruiting and retention decision making, as well as global sourcing strategies.

## Limitations and Issues

The main limitation of the methodology that we proposed is our use of the delta-normal method and the associated estimation of the standard deviation of costs. However, we expect that decision support tools that implement our proposed approach probably will rely more on historical data-based, full valuation approaches. In IT settings, we believe that labor market data will be a useful basis for providing proxies for standard deviation estimates of wages, and even correlations for costs and revenues across different IT standards. For example, firms can begin to track wages or employment data regarding Bluetooth versus wireless skills, or a host of other project management, network architecture, and systems deployment staff salaries in the marketplace. There are additional issues with the delta-normal method that must be considered as well. Under assumptions of normally distributed returns, VaR has limitations. In portfolio settings, value-at-risk may not be subadditive, and may overstate the actual risk position to some degree. In spite of this, however, many financial services firms may be observed to be continuing to use VaR techniques. Jorion [42], exhibiting an awareness of the underlying issues, suggested that employing full valuation methods with historical data can reduce the exposure associated with issues of subadditivity and coherence. For example, firms can model the actual distribution of returns for a particular kind of IT service based on historical data, once they build up sufficient experience with tracking the relevant data to do this. Simulation techniques will be important as this work moves toward full valuation methods [42].

IT services contract data will likely exhibit kurtosis or skewed distributions, which may cause a firm to underestimate its risk positions. The use of conditional value-atrisk may reduce the impact of kurtosis and nonnormal distributions, which are likely to occur when modeling technology risks [3]. We expect that as firms implement this methodology, they will build competencies in estimating volatility and other input parameters, which will make it possible to diminish the negative impact of nonnormality in terms of the outcomes of the analysis. Luciano and Marena [55] present a technique to examine portfolio-level value-at-risk without the assumption of normally distributed returns.

Beyond the issues associated with the structure of the data used is the practical ability of firms to gather the data required about their service levels, and detailed cost and revenue data, which are tied directly to each contract. For many service providers, these data occur in disparate areas. A firm’s financial recording systems may cover the necessary granularity which contract analysis requires, for example. Fortunately, several vendors, such as SAS (www.sas.com) and Digital Fuel (www.digitalfuel. com), have begun to offer service-level management (SLM) systems which actively track data regarding the performance of a service provider’s contractual obligations [59]. IS and operations research (OR) have also utilized the well-known data envelopment analysis (DEA) methodology to model best-practice production frontiers [64]. We believe that, with the passage of only a relatively brief amount of time, it will be possible to develop efficient frontiers for IT services management best practices by utilizing contract data from SLM tools such as those offered by SAS and Digital Fuel. Advanced data-mining techniques may also be used on the data from these systems in order to identify “at-risk” clients or service commitment patterns that lead to unacceptable levels of firm risk. In spite of the obstacles, we believe that the future is very bright for the further development and diffusion of managerial use of the methods that we proposed involving value-at-risk methods, as well the broader tool sets that are being developed for service science.

Julie Smith-David and the Center for Advancing Business through Information Technology, as well as the W.P. Carey Chair in Information Systems at Arizona State University for partial support. All errors in the paper are the responsibility of the authors. A much earlier conference version appeared as R.J. Kauffman and R. Sougstad, “Value at Risk in IT Services Contracts,” in R.H. Sprague Jr. (ed.), Proceedings of the 40th Hawaii International Conference on System Sciences, IEEE Computing Society Press, Los Alamitos, CA, 2007.

## Notes

1. Service science, management, and engineering (SSME) is an emerging field of research in both industry (e.g., for IBM) and academia (e.g., Arizona State University, University of California at Berkeley, among others). Some concepts fundamental to services research include spontaneous consumption and production, knowledge interactions across organizations, as well as the application of interorganizational communication technologies [24, 39]. Researchers face challenges such as formalizing systems of services and codifying tacit knowledge that exists among providers and users of services, as well as modeling service systems [56]. Readers are referred to the July 2006 issue of Communications of the ACM, which is dedicated to services science, management, and engineering.

2. As contingent liabilities, obligations to provide services do not appear on the balance sheet, income statement, or changes in funds statement of service providers. Sarbanes–Oxley 401(a) requires disclosure of off-balance sheet contractual obligations in the “Management Discussion and Analysis (MD&A)” in the companies’ financial filings with the Securities Exchange Commission [62]. Firms often face legal action from clients if these obligations are not met, and future revenues and profits may be contingent upon a firm’s ability to meet its contractual obligations.

3. Hedging refers to the reduction or elimination of risk from a position whose value is subject to change from exogenous shocks. In financial portfolio management, hedging often involves placing assets that are negatively correlated in a position together. A common example is the mixture of equity (stock) and debt (bonds) securities within a portfolio. Stocks and bonds tend to exhibit negative correlation. An increase in the value of the bond typically, though not always, coincides with weaker returns in the stock market. Investors often utilize derivatives such as short selling to minimize risk positions. A protective put is another common example. Investors holding a position in a stock often purchase protective puts, which gives them the right to sell their stock at a prespecified price, minimizing potential downside losses. In the context of services management, provider firms may diversify their contract portfolios by seeking clients in multiple industry verticals in order to reduce their risk exposure of economic downturn in any one industry. These observations suggest the need for valuing risky assets and ensuring appropriate selection of risky investments in stock portfolios and capital budgets [52, 57, 63].

4. Hereafter, we will refer to value-at-risk and VaR in two different ways. We will use the full term, value-at-risk, to indicate the specific measurement concept, as denoted by the theory. However, when we refer to related concepts and methods, we will use the abbreviation, VaR, as in VaR methods or VaR-based portfolio evaluation. In the first case, we are referring specifically to a dollar value that can potentially be lost; in the latter, we are referring to a body of knowledge associated with VaR methods. In contrast, we will use profit-at-risk and PaR in our model interchangeably, as the lowest expected contract profits at a certain confidence level over a contract horizon.

5. The interested reader should examine literature on portfolio risk and hedging methods by Agarwal and Naik [2] and Campbell et al. [21], and additional VaR-specific methods conducted by Basak and Shapiro [10], Berkowitz and O’Brien [17], Glasserman et al. [36], and Lucas and Klaassen [54]. See Stybo Beder [65] for a more critical evaluation of the application of VaR methods.

6. Kurtosis is a means of measuring the extent to which a distribution is different from the normal distribution so that more observations occur in its tails. Although the means and variances of two expected profit distributions may be the same, their kurtosis may be different, which could expose a firm to different risks with profitability. If the data exhibit a high degree of kurtosis, VaR techniques may underestimate the firm’s risk exposure. A related, broader issue is the problem of coherence [1] in VaR techniques which assume normal parametric distributions. Artzner et al. [5, 6] wrote that appropriate measures of risk need to be characterized by a number of key axioms. Subadditivity is one of them. Portfolios under the usual VaR assumptions are not subadditive: they may not accurately represent an aggregate view of portfolio risk. See Jorion [42] for a thorough discussion of cohesion and VaR techniques. We will discuss the implications of our distributional assumptions later.

7. There is a considerable body of research involving the economics of insurance, which models WTP for risk avoidance [53, 58]. These works draw on knowledge about convex preferences and experimental economics for modeling the amount consumers will be willing to pay for insurance against risky outcomes. We assume a functional form for WTP for this simulation, but as we discuss later, additional empirical work must be conducted to model a manager’s true WTP, which will be affected by individual risk aversion, as well as technology, firm, and market influences.

8. Our decision to model the IT services provider as a monopolist obviates the need for a game-theoretic treatment of the issues we discuss in this paper. Because IT contracts are usually unique to the client–provider relationship and involve intricate negotiations [33], the assumption of the monopolistic provider allows us to isolate this one-on-one interaction. Although this is an interesting potential future research direction for this work, moving to the analysis of a duopoly or a competitive marketplace for IT services would add unnecessary complexity to the analytical framework that we have built, without providing any basis for increasing the clarity of theory development and managerial illustrations that we provide for the reader.

9. A Gauss-Wiener process is a continuous time stochastic process with independent increments and, thus, independent random variables. A Brownian motion stochastic process is the most well-known instance, involving a “random walk” with random step sizes (http://mathworld. wolfram.com/WienerProcess.html). Both are extensively used in financial economics to model the diffusion of costs, asset prices, and other indicators.

10. We would like to acknowledge the suggestion of an anonymous reviewer who encouraged us to make clear how historical information or the lack of historical information on input costs affects the analysis. We learned by going through the process of evaluating what we can contribute in both instances. It turns out that there will be many opportunities in follow-up research to begin to build historical data sets for a range of IT services contexts.

11. See Dos Santos [35] for an explanation and treatment of standard deviation of returns for IT investments.

12. We would advise practitioners to consider these cost and productivity factors, but they are not germane to our analysis of risk exposure in IT services. Such productivity models have been well treated by operations researchers. Interested readers should examine Sherman and Zhu [64], who present approaches to model service performance and productivity using data envelopment analysis (DEA).

## Refer ences

1. Acerbi, C., and Tasche, D. Expected shortfall: A natural coherent alternative to value-atrisk. Economic Notes, 31, 2 (July 2002), 379–388.

2. Agarwal, V., and Naik, Y. Risks and portfolio decisions involving hedge funds. Review of Financial Studies, 17, 1 (Summer 2004), 63–98.

3. Anderson, F.; Mausser, H.; Rosen, D.; and Uryasev, U. Credit risk optimization with conditional value-at-risk criterion. Mathematical Programming, Series B, 89 (2001), 273–291.

4. Aron, R.; Clemons, E.K.; and Reddi, S. Just right outsourcing: Understanding and managing risk. Journal of Management Information Systems, 22, 2 (Fall 2005), 35–56.

5. Artzner, P.; Delbaen, F.; Eber, J.-M.; and Heath, D. Thinking coherently. RISK, 10, 11 (November 1997), 68–71.

6. Artzner, P.; Delbaen, F.; Eber, J.-M.; and Heath, D. Coherent measures of risk. Mathemati cal Finance, 9, 3 (July 1999), 203–228.

7. Bakos, Y., and Brynjolfsson, E. Bundling information goods: Pricing, profits, and efficiency. Management Science, 45, 12 (December 1999), 1613–1630.

8. Bakos, Y., and Kemerer, C.F. Recent applications of economic theory in information technology. Decision Support Systems, 8, 5 (September 1992), 365–386.

9. Bardhan, I.R.; Bagchi, S.; and Sougstad, R. Prioritization of a portfolio of information technology projects. Journal of Management Information Systems, 21, 2 (Fall 2004), 33–60.

10. Basak, S., and Shapiro, A. Value-at-risk-based risk management: Optimal policies and asset prices. Review of Financial Studies, 14, 2 (Summer 2001), 371–405.

11. Bass, F.M. A new product growth model for consumer durables. Management Science, 15, 1 (January 1969), 215–227.

12. Benaroch, M. Managing information technology risk: A real options perspective. Journal of Management Information Systems, 19, 2 (Fall 2002), 43–84.

13. Benaroch, M., and Kauffman, R.J. A case for using real options pricing analysis to evaluate information technology project investments. Information Systems Research, 10, 1 (March 1999), 70–86.

14. Benaroch, M., and Kauffman, R.J. Options analysis of software platform decisions: A case study. MIS Quarterly, 24, 2 (June 2000), 197–225.

15. Benaroch, M.; Lichtenstein, Y.; and Robinson, K. Real options in IT risk management: An empirical validation of risk-option relationships. MIS Quarterly, 30, 2 (June 2006), 827–864.

16. Benaroch, M.; Jeffery, M.; Kauffman, R.J.; and Shah, S. Option-based risk management: A field study of sequential IT investment decisions. Journal of Management Information Systems, 24, 2 (Fall 2007), 103–140.

17. Berkowitz, J., and O’Brien, J. How accurate are value-at-risk models at commercial banks? Journal of Finance, 57, 3 (June 2002), 1093–1111.

18. Bhargava, H.K., and Sundaresan, S. Contingency pricing for information goods and services under industry-wide performance standards. Journal of Management of Information Systems, 20, 2 (Fall 2003), 113–136.

19. Bhargava, H.K., and Sundaresan, S. Computing as utility: Managing availability, commitment, and pricing through contingent bid auctions. Journal of Management of Information Systems, 21, 2 (Fall 2004), 201–227.

20. Black, F., and Scholes, M. The pricing of options and corporate liabilities. Journal of Political Economy, 81, 3 (May–June 1973), 637–665.

21. Campbell, R.; Huisman, R.; and Koedijk, K. Optimal portfolio selection in a value-at-risk framework. Journal of Banking and Finance, 25, 9 (September 2001), 1789–1804.

22. Carr, N.G. The end of corporate computing. Sloan Management Review, 46, 3 (Spring 2005), 67–73.

23. Cheng, H.K., and Koehler, G. Optimal pricing policies of Web-enabled application services. Decision Support Systems, 35, 3 (June 2003), 259–272.

24. Chesbrough, H., and Spohrer, J. A research manifesto for services science. Communications of the ACM, 49, 7 (July 2006), 35–40.

25. Choudhary, V. Software as a service: Implications for investment in software development. Journal of Management Information Systems, 24, 2 (Fall 2007), 141–165.

26. Clemons, E.K., and Aron, R., Maximizing your outsourcing benefits through complexity arbitrage. Working Paper, Wharton School, University of Pennsylvania, Philadelphia, 2004 (available at http://opim.wharton.upenn.edu/%7Eclemons/files/outsourcing-v5.pdf).

27. Clemons, E.K., and Gu, B. Justifying contingent information technology investments: Balancing the need for speed of action with certainty before action Journal of Management Information Systems, 20, 2 (Fall 2003), 11–48.

28. Clemons, E.K., and Hitt, L. Poaching and the misappropriation of information: Transaction risks of information exchange. Journal of Management Information Systems, 21, 2 (Fall 2004), 87–107.

29. Clemons, E.K., and Weber, B. Strategic information technology investments: Guidelines for decision making. Journal of Management Information Systems, 7, 2 (Fall 1990), 9–28.

30. Cox, J.; Ross, S.; and Rubenstein, M. Option pricing: A simplified approach. Journal of Financial Economics, 7, 3 (September 1979), 229–263.

31. Crouhy, M.; Galai, D.; and Mark, R.M. Risk Management. New York: McGraw-Hill, 2001.

32. Dai, R.; Narasimhan, S.; and Wu, D.J. Buyer’s efficient e-sourcing structure: Centralize or decentralize? Journal of Management Information Systems, 22, 2 (Fall 2005), 141–164.

33. Dietrich, B.; Paleologo, G.A.; and Wynter, L. Revenue management in business services. IBM Technical Paper RC24307, Armonk, NY, July, 16, 2007 (available at http://domino.research.

ibm.com/library/cyberdig.nsf/1e4115aea78b6e7c85256b360066f0d4/184a455b9ecbf7ba8525 731c005d057e?OpenDocument).

34. Dixit, A., and Pindyck, R. Investment Under Uncertainty. Princeton: Princeton University Press, 1994.

35. Dos Santos, B. Justifying investments in new information technologies. Journal of Management Information Systems, 7, 4 (Spring 1991), 71–90.

36. Glasserman, P.; Heidelberger, P.; and Shahabuddin, P. Variance reduction techniques for estimating value-at-risk. Management Science, 46, 10 (October 2000), 1349–1364.

37. Gupta, A.; Stahl, D.; and Whinston, A. Managing computing resources in intranets: An electronic commerce perspective. Decision Support Systems, 24, 1 (November 1998), 55–69.

38. Han, K.; Kauffman, R.J.; and Nault, B. Information exploitation and interorganizational systems ownership. Journal of Management Information Systems, 21, 2 (Fall 2004), 109–135.

39. Horn, P. The new discipline of services sciences. BusinessWeek Online, January 21, 2005 (available at www.businessweek.com/technology/content/jan2005/tc20050121\_8020.htm).

40. Huang, K.W., and Sundararajan, A. Pricing models for on-demand computing. Working Paper, Stern School of Business, New York University, November 2005.

41. Jorion, P. Financial Risk Manager Handbook, 3d ed. New York: John Wiley and Sons, 2005.

42. Jorion, P. Value-at-Risk: The New Benchmark for Controlling Market Risk, 3d ed. New York: Irwin, 2007.

43. Karamouzis, F. Positions 2005: Global sourcing and the impact of new delivery models on IT services. Working Paper, Gartner Research, Stamford, CT, March 2005.

44. Kauffman, R.J., and Kumar, A. Countervailing and complementary network effects and embedded options: Decision-making under uncertainty for technology investments. Information Technology and Management, 2008, forthcoming.

45. Kauffman, R.J., and Li, X. Technology competition and optimal investment timing: A real options perspective. IEEE Transactions on Engineering Management, 52, 1 (February 2005), 15–30.

46. Kauffman, R.J., and Mohtadi, H. Proprietary and open systems adoption: A risk-augmented transactions cost perspective. Journal of Management Information Systems, 21, 1 (Summer 2004), 137–166.

47. Kauffman, R.J., and Walden, E.A. Economics and e-commerce: Survey and research directions. International Journal of Electronic Commerce, 5, 4 (Summer 2001), 4–115.

48. Kenyon, C. Optimal price design for variable capacity outsourcing contracts. Journal of Revenue and Pricing Management, 4, 2 (April 2005), 124–155.

49. Kleindorfer, P., and Wu, D.J. Integrating long- and short-term contracting via businessto-business exchanges for capital-intensive industries. Management Science, 49, 11 (November 2003), 1597–1615.

50. Leeson, N., and Whitley, E. Rogue Trader: How I Brought Down Barings Bank and Shook the Financial World. Boston: Little, Brown, 1996.

51. Liebowitz, M.L., and Kogelman, S. Asset allocation under shortfall constraints. Journal of Portfolio Management, 17, 2 (Winter 1991), 18–23.

52. Lintner, J. The valuation of risk assets and the selection of risky investments in stock portfolios and capital budgets. Review of Economics and Statistics, 47, 1 (February 1965), 13–39.

53. List, J.A., and Gallet, C. What experimental protocol influences disparities between actual and hypothetical stated values? Environmental and Resource Economics, 20, 3 (November 2001), 241–254.

54. Lucas, A., and Klaassen, P. Extreme returns, downside risk, and optimal asset allocation. Journal of Portfolio Management, 25, 1 (Fall 1998), 71–78.

55. Luciano, E., and Marena, M. Portfolio value-at-risk bounds. International Transactions in Operations Research, 9, 5 (September 2002), 624–641.

56. Maglio, P.P.; Srinivasan, S.; Kreulen, J.T.; and Spohrer, J. Service systems, service scientists, SSME, and innovation. Communications of the ACM, 49, 7 (July 2006), 81–85.

57. Markowitz, H.M. Portfolio selection. Journal of Finance, 7, 1 (March 1952), 77–91.

58. McClelland, G.H.; Schulze, W.D.; and Coursey, D.L. Insurance for low-probability

hazards: A bimodal response to unlikely events. Journal of Risk and Uncertainty, 7, 1 (January 1993), 95–116.

59. O’Neil, P., and Hubert, E. The Forrester wave: Business service management Q1 2007. Report no. 38931, Forrester Research, Cambridge, MA, March 2007.

60. Paleologo, G.A. Price-at-risk: A methodology for pricing utility computing services. IBM Systems Journal, 43, 1 (2004), 20–31.

61. Schwartz, E., and Zozaya-Goristiza, C. Investment under uncertainty in information technology: Acquisition and development projects. Management Science, 49, 1 (January 2003), 57–70.

62. Securities Exchange Commission. SEC adopts rules on disclosure of off-balance sheet arrangements and aggregate contractual obligations. Press Release 2003-10, Washington, DC, January 22, 2003 (available at www.sec.gov/news/press/2003-10.htm).

63. Sharpe, W.F. Capital asset prices: A theory of market equilibrium under conditions of risk. Journal of Finance, 19, 3 (December 1964), 425–442.

64. Sherman, D.H., and Zhu, J. Service Productivity Management. New York: Springer Science and Business Media, 2006.

65. Stybo Beder, T. VaR: Seductive but dangerous. Financial Analyst’s Journal, 51, 5 (September–October 1995), 12–24.

66. Sundararajan, A. Non-linear pricing of information goods. Management Science, 50, 12 (December 2004), 1660–1673.

67. Westland, C. Congestion and network externalities in the short-run pricing of information systems services. Management Science, 38, 7 (July 1992), 992–1099.

68. Wu, D.J., and Kleindorfer, P. Competitive options, supply contracting and electronic markets. Management Science, 51, 3 (March 2005), 452–466.

## Appendix A

<table><tr><td colspan="2">Table A1. Value-at-Risk (VaR) Terminology</td></tr><tr><td>Terms</td><td>Definitions</td></tr><tr><td>Value-at-risk</td><td>The worst expected loss an investment will incur over a discrete time period at a specified confidence interval.</td></tr><tr><td>Mark-to-market position</td><td>The value of an asset or a portfolio based on current market value. In the case of systems and technology investments, this will be the current project value or the current expected cost of a project input.</td></tr><tr><td>Variance of asset value or returns</td><td>Measures the variability of a risk factor that underlies asset value, usually stated as a variance or a standard deviation.</td></tr><tr><td>Time horizon</td><td>Time frame over which value-at-risk is to be assessed, based on managerial discretion relative to the risk perspective. The time horizon is typically chosen based on the asset&#x27;s liquidity. For example, interbank loan analysis is typically done with daily increments, whereas a mutual fund may use a 30- or 90-day time horizon.</td></tr><tr><td>Confidence interval</td><td>The probability bounds on the observation of a specified value-at-risk outcome, chosen based on a firm&#x27;s desire to manage payoff and return outcomes up to a predetermined likelihood.</td></tr><tr><td>Correlation of asset value or returns</td><td>Measures the extent to which asset returns covary with one another. The values could range from -1 (perfect negative correlation), to 0 (no correlation), to +1 (perfect correlation). This input is used when looking at portfolio-level value-at-risk.</td></tr></table>

Note: Adapted from Crouhy et al. [31] and Jorion [42].

## Appendix B: An Additional Extension—Considering Efficiency in Profit-at-Risk Analysis

We s how that the r ange of contr acts to be considered by profit-at-risk analysis can be narrowed to a set of efficient contracts, defined as those contracts that represent a maximum profit for a given profit-at-risk constraint. We demonstrate that all portfolios are dominated by those in the range of the point between the unconstrained profitmaximization service-level contract and the maximum profit-at-risk contract. The maximum profit-at-risk contract can be thought of as the minimum-variance efficient portfolio. This permits us to show how the firm’s risk aversion will affect the choice of efficient portfolio.

In Table B1, we evaluate an extended range of service levels, S, similar to Table 4. We utilize the same inputs from Table 3 and functional forms as those used to create Table 4.

Consistent with the analysis results shown in Table 4 and Figure 1, we note that the profit maximization point occurs where $S ^ { ( b ) } = 5 1$ percent. As we move to columns left of this point, we further note that both the profits and the profit-at-risk are lower

<sub>ue</sub> <sub>estimation</sub> <sup>and</sup> <sup>modelin</sup> <sub>re</sub> <sub>stated</sub> <sub>in</sub> <sub>thousands</sub> <sub>of</sub> <sub>dollars</sub>. <sub>The</sub> <sub>accuracy</sub> <sub>and</sub> <sub>precision</sub> <sub>of</sub> <sub>the</sub> <sub>si</sub>m<sup>ulated</sup> <sup>values</sup> <sup>reported</sup> <sup>in</sup> <sup>the</sup> <sup>table</sup> <sup>are</sup> <sup>c</sup> <sub>ximum</sub> <sub>PaR</sub> <sub>from</sub> <sub>the</sub> <sub>dual</sub> <sub>for</sub>m<sup>ulization</sup> <sup>of</sup> <sup>our</sup> <sup>original</sup> <sup>profit-maximization</sup> <sup>model</sup> <sup>without</sup> <sup>profit</sup> <sup>constraint</sup> <sup>c</sup> <sub>ed</sub> <sub>on</sub> <sub>the</sub> <sub>initial</sub> <sub>inputs</sub> <sub>given</sub> <sub>in</sub> <sub>Table</sub> <sub>3,</sub> <sub>with</sub> <sub>variations</sub> <sub>in</sub> <sub>S</sub> <sub>a</sub>s <sup>noted</sup> <sup>in</sup> <sup>the</sup> <sup>top</sup> <sup>row</sup>. <sup>S(a)</sup> <sup>=</sup> <sup>0</sup>.<sup>22</sup> <sup>represents</sup> <sup>the</sup> <sup>p</sup>

<table><tr><td rowspan="2">Percent high service level hours (S)</td><td colspan="10">Percent</td></tr><tr><td>10</td><td>15</td><td>22</td><td>30</td><td>35</td><td>40</td><td>45</td><td>51</td><td>55</td><td>60</td></tr><tr><td>Expected profit</td><td>192</td><td>265</td><td>332</td><td>375</td><td>393</td><td>405</td><td>412</td><td>414</td><td>413</td><td>409</td></tr><tr><td>Profit-at-risk</td><td>53</td><td>101</td><td>123</td><td>101</td><td>67</td><td>20</td><td>-41</td><td>-130</td><td>-198</td><td>-293</td></tr></table>

<sub>B1.</sub> <sub>Si</sub>m<sup>ulation</sup> <sup>of</sup> <sup>Con</sup>

![](/api/attachments/3VW66SDT/fulltext/images/8d4caaf4ff5708be66cd32eb625028abb56c5a6d0aa284db5f84091666bc8a75.jpg)  
Figure B1. Efficient Frontier for IT Services Contracts

than the point of unconstrained profit maximization. That is, the contracts at $S = 5 5$ percent and 60 percent imply greater risk exposure and lower profits. These contracts are dominated by the profit-maximizing contract and should be removed from the manager’s consideration set. To refer back to Figure 1, these contracts occur where both profits and profit-at-risk are decreasing in S.

Another important case occurs when S is chosen to maximize PaR. Formally, we can state:

$$
\operatorname{Max} _ {(S)} P a R = R (S) - C (S, C _ {H}, C _ {L}) [ 1 + \sigma_ {c} (S, \sigma_ {H}, \sigma_ {L}, \rho_ {H L}) \alpha \sqrt {t} ]\tag{B1}
$$

$$
\text { Subject   to: } 0 <   S \leq 1.\tag{B2}
$$

Utilizing the same functional forms and inputs as given in the objective function in Equation (5), the PaR constraint in Equation (6), and Table 3, we find that the solution for the maximum value of PaR occurs at $S ^ { ( a ) } = 2 2$ percent. As we move to columns left of this point, both the profit and the profit-at-risk decrease. Again, these points are dominated by the maximum profit-at-risk position. These dominated values of S are within the range where profit and profit-at-risk are both increasing in S.

We define the range of consideration, where marginal profit increases in S and marginal profit-at-risk decreases in S, as the efficient frontier. We assume the functional forms given by the objective function of Equation (4), and the constraints in Equations (5) and (6). The efficient frontier contains all values of S such that $S ^ { ( a ) } \leq S \leq$ $S ^ { ( b ) }$ . These values for S are represented by the curve connecting $S ^ { ( b ) }$ and $S ^ { ( a ) }$ in Figure B1. Each value for S on the efficient frontier corresponds to a value of $k ,$ where k falls between the maximum profit-at-risk and the profit-at-risk associated with S<sup>\*</sup>. In Table B1, where we varied the value-at-risk constraints, each profit-at-risk constraint represents a point on the efficient frontier. However, the value S = 60 percent, represented by the last column in Table B1, does not fall on the efficient frontier; instead, it is dominated by other values for the higher service quality input combinations, per the preceding analysis.

The efficient frontier is a useful guide for managers who have responsibility for portfolios of IT service contracts. If managers have accurate, reliable measures of their customers’ WTP and cost structures, they will be able to construct an efficient frontier. This will be helpful to narrow down the set of possible IT services contracts to just the set of efficient contracts, which will make for a more productive negotiation process. The efficient frontier, as we defined it for the IT services contract portfolio context, depends on a key assumption: a strictly increasing, continuous concave WTP function. So this extended “frontier” analysis will be more difficult for practitioners to implement in comparison to assessment of contract profit and profit-at-risk in the negotiation setting. Nevertheless, it should be intuitive for an IT services manager not to accept a customer for a contract that is strictly dominated, so in that respect, a comparison of relative efficiency should always be made when comparing two contract choices, even if both are below the bounds of a true efficient frontier.
