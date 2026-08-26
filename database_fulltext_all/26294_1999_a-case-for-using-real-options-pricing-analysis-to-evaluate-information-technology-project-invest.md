---
otero_id: 26294
otero_key: "VXK39C4N"
title: "A Case for Using Real Options Pricing Analysis to Evaluate Information Technology Project Investments"
authors: "Michel Benaroch; Robert J. Kauffman"
year: "1999"
journal: "Information Systems Research"
doi: "10.1287/isre.10.1.70"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/VXK39C4N/fulltext/images/704769f124bbb11b8e76e06ce8c6fbe43bc62f73c8e991f41f21c54d84e266ac.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## A Case for Using Real Options Pricing Analysis to Evaluate Information Technology Project Investments

Michel Benaroch, Robert J. Kauffman,

To cite this article:

Michel Benaroch, Robert J. Kauffman, (1999) A Case for Using Real Options Pricing Analysis to Evaluate Information Technology Project Investments. Information Systems Research 10(1):70-86. http://dx.doi.org/10.1287/isre.10.1.70

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1999 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/VXK39C4N/fulltext/images/8162b2acee58bb12fa1f60ccf7e0d3d465de1b2c56dd4193c438ecd9930d0fec.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# A Case for Using Real Options Pricing Analysis to Evaluate Information Technology Project Investments

Michel Benaroch • Robert J. Kauffman

School of Management, Syracuse University, Syracuse, New York 13244-2130 mbenaroc@syr.edu

Carlson School of Management, University of Minnesota, 271 19th Avenue South, Minneapolis, Minnesota 55455 rkauffman@csom.umn.edu

he application of fundamental option pricing models (OPMs), such as the binomial and the Black-Scholes models, to problems in information technology (IT) investment decision making have been the subject of some debate in the last few years. Prior research, for example, has made the case that pricing “real options” in real world operational and strategic settings offers the potential for useful insights in the evaluation of irreversible investments under uncertainty. However, most authors in the IS literature have made their cases using illustrative, rather than actual real world examples, and have always concluded with caveats and questions for future research about the applicability of such methods in practice. This paper makes three important contributions in this context: (1) it provides a formal theoretical grounding for the validity of the Black-Scholes option pricing model in the context of the spectrum of capital budgeting methods that might be employed to assess IT investments; (2) it shows why the assumptions of both the Black-Scholes and the binomial option pricing models place constraints on the range of IT investment situations that one can evaluate that are similar to those implied by traditional capital budgeting methods such as discounted cash flow analysis; and (3) it presents the first application of the Black-Scholes model that uses a real world business situation involving IT as its test bed. Our application focuses on an analysis of the timing of the deployment of point-of-sale (POS) debit services by the Yankee 24 shared electronic banking network of New England. This application enables us to make the case for the generalizability of the approach we discuss to four IT investment settings.

(IT Investment Evaluation; Real Options; Option Pricing Methods; Black-Scholes Model; Electronic Banking Networks; POS Debit Systems)

## 1. Introduction

Recent research in the Information Systems (IS) literature (e.g., Clemons 1991, Dos Santos 1991, Kambil et al. 1993, Kumar 1996, Chalasani et al. 1997) has recognized the importance of utilizing the theory of irreversible investment under uncertainty (Dixit and Pindyck 1994) to emphasize the option-like characteristics of information technology (IT) project investments. A project embeds a real option (e.g., Sick 1990, Nichols 1994, Trigeorgis 1995 and 1996) when it offers management the opportunity to take some future action (such as abandoning, deferring, or scaling up the project) in response to events occurring within the firm and its business environment. Yet, in spite of this new interest, little work published in the IS literature addresses the problem of evaluating such “real options” in practice. Moreover, various authors have expressed a number of concerns related to the efficacy of applying option pricing theory to IT investments.

The field of finance has developed a variety of option pricing models (OPMs), with the fundamental ones being the binomial and the Black-Scholes model option pricing models. Because these models were originally developed to evaluate options on securities traded in the financial markets (e.g., European and American put and call options), they make certain assumptions that more naturally apply to options on traded assets. Over time, these models and their extensions have also been used in a variety of evaluative settings involving capital budgeting investments embedding real options (e.g., Kogut and Kulatilaka 1994, and Baldwin and Clark 1994). In this context, however, the validity of these models is often questioned: the criticisms primarily focus on whether one can analyze nontraded assets using models that were formulated to evaluate assets that are traded in a financial market.

The Black-Scholes model is especially interesting in this regard. Although there exists a general perception among IS researchers that OPMs, and the Black-Scholes model in particular, may not be applicable in IT capital budgeting due to their theoretical basis and key assumptions (Kauffman et al. 1993, p. 588), our reading of the relevant literature in finance suggests a different view—one that we develop fully in this research note. This paper makes three important contributions in this context: (1) it provides a formal theoretical grounding for the validity of the Black-Scholes option pricing model in the context of the spectrum of capital budgeting methods that might be employed to assess IT investments; (2) it shows why the assumptions of both the Black-Scholes and the binomial option pricing models place constraints on the range of IT investment situations that one can model that are similar to those implied by traditional capital budgeting methods such as discounted cash flow analysis; and (3) it presents the first application of the Black-Scholes model that uses a real world business situation involving IT as its test bed. Our application focuses on an analysis of the timing of the deployment of point-of-sale (POS) debit services by the Yankee 24 shared electronic banking network of New England and enables us to make the use for the generalizability of the approach we discuss.

## 2. IT Investment Options: Modeling Issues

The application of option pricing models to evaluate projects has been reported by researchers and practitioners. Baldwin and Clark (1994) examined how the design of software creates options for rapid deployment of future software products development when software is reused. Kogut and Kulatilaka (1994) used OPMs to gauge the value of production flexibility in world-wide manufacturing operations affected by foreign exchange rate movements. And, Nichols (1994), in an interview with Judy Lewent, then Chief Financial Officer of Merck & Co., the pharmaceutical manufacturer, discusses how OPMs are used to evaluate corporate acquisitions that promote pharmaceutical R&D. We next introduce the IT investment problem that Yankee 24 faced, and explain the situational specifics that prompt us to frame Yankee’s situation in terms of techniques from the literature on irreversible investment under uncertainty, instead of the usual capital budgeting techniques associated with net present value analysis.

## 2.1. The Yankee 24 Timing Option

Yankee 24 was formed in 1984 to provide electronic banking network services to its more than 200 member institutions. It charged a one-time membership fee and a transaction fee for all electronic banking transactions serviced by the Yankee switch. In 1987, Richard P. Yanak, Yankee’s president, evaluated the business case for providing POS debit card network to member firms, in addition to its traditional business of switching automated teller machine (ATM) transactions.

Entry as early as 1987 into the POS debit market had broad appeal. It would have generated revenues and created entry barriers for potential network competitors. Additionally, there was good potential for future revenues, e.g., the possibility that state governments would start using electronic payments to deliver welfare benefits was one indication of how large the revenues could grow. However, at this time the POS debit card business involved considerable uncertainty. For example, the perceived environmental risk was substantial; the expected revenues in New England might be low, if consumer acceptance and retailer adoption were as slow as what had been observed in California earlier in the decade. Retailer adoption was perceived to be especially critical: the state of Massachusetts, representing about 50% of the total New England market, regulated the adoption of electronic banking services by nonbanking industry participants. A second source of uncertainty derived from Yankee’s lack of maturity as an ATM service provider. The network, whose ATM service infrastructure would subsequently grow to serve more than 700 firms, did not have all the network resources it needed to support a new business in place at the time. Time would tell whether growth in the ATM business would provide the complementary network technology assets to make the costs of entry into the POS debit market acceptable.

Yanak’s strategic vision of the growth potential of Yankee’s electronic banking services encompassed growth outside the limited realm of ATM banking. He also recognized that Yankee had the option to wait to achieve the best timing for entry; in his view, this was three years later. Thus, from Yanak’s perspective, a decision to enter the debit card business was a matter of timing. Yankee could afford to wait because there were no credible threats in its immediate markets: the only possible competitor at the time, the New York Cash Exchange (NYCE), a joint venture of several New York City-based commercial banks, had no presence in the ATM or the POS debit markets in New England. In this sense, Yanak believed that Yankee 24 could operate as a near monopoly in New England—at least until NYCE or some other competitor chose to enter the POS debit market. By waiting, Yanak reasoned, uncertainties concerning the acceptance of POS debit services in Yankee’s markets and the viability of additional irreversible network infrastructure investment would be resolved. In turn, this would enable Yanak to learn more about the potential returns to such investment. For example, the acceptance rate might increase as consumers learned about the convenience and value of POS debit services. Simultaneously, Yankee could take actions to lower its market entry risk, e.g., by lobbying for changes in Massachusetts’ statutes to promote POS debit adoption. Naturally, by waiting Yankee would lose some revenues. More importantly, waiting too long could lead to market share gains by competitors who had no prior presence in the market.

With these concerns in mind, Yanak posed two key questions: how long should Yankee 24 wait to enter the POS debit card market? Could quantitative analysis bear out his intended approach, given Yankee’s overall strategy and the prevailing competitive situation?

## 2.2. Modeling Issues

Two alternative approaches to modeling Yankee’s decision problem are discounted cash flow (DCF) analysis and option pricing analysis. The second approach is relevant in this instance because of Yankee’s ability to defer entry: it possessed a deferral option. This option existed because, at the time, Yankee had a near monopoly right to invest in the New England market for POS debit services. (More precisely, Yankee operated in a duopoly, but it expected to hold a “leadership” position for at least the next three years, due to the lack of other credible threats.) NYCE, for example, did not have sufficient infrastructure in New England to enter the POS debit market. More importantly, NYCE did not have the installed base of member banks that Yankee had in New England. These banks were the ones responsible for planning and aggressively promoting POS debit services to retailers who would use the services to garner additional income. Yanak felt that NYCE would need at least three years to develop these “resources.” Yankee’s ability to flexibly defer this roll out can be viewed as an American call option. In financial market terms, a call option confers upon the owner the right, but not the obligation, to purchase a security at future date at a price that is established when the option is created. American options are those which can be exercised on or before their expiration date (unlike European options which can be exercised only on their expiration date).

How can NPV and option pricing be used to answer the question Yanak faced? We identify four reasons why these approaches will treat the issues differently.

First, in Yankee’s case, it is important to recognize that the distribution of the expected returns on the POS debit project probably is not symmetric. (See Figure 1A.) In NPV, an implicit way to account for this asymmetric distribution is to calculate the NPV for the worst, most likely and best case scenarios, while using one risk-adjusted discount rate that applies equally well to all these scenarios. By contrast, option pricing is able to explicitly model this asymmetric distribution; it allows us to describe the uncertain project revenues in terms of their expected value and their potential variability (or standard deviation).

Second, it is important to understand that the NPV and option pricing perspectives differ in the way they treat Yankee’s ability to defer POS debit roll out. (See Figure 1B.) The thick line on the left graph represents the possible investment value based on the usual NPV decision rule: “Don’t invest if NPV is negative.” This line is also the classical “kinked” payoff profile that is often seen in illustrations of simple call option analysis; it coincides with the value line of a call option, but only if the option were one that matures immediately $( \mathrm { i . e . , }$ this would have been the case if Yankee’s had a “nowor-never” type of investment). Thus, NPV can be said to recognize the value of embedded deferral options, but only when the options mature immediately. Overall, if NPV were to allow the explicit modeling of asymmetric returns, following the decision rule implied by both the NPV and the option pricing perspectives shifts the distribution of the expected returns to the right.

Third, an option to flexibly defer investment for some time $T > 0$ has a larger expected value than a now-or-never type of investment. Recall that by waiting Yankee hopes to get additional information to make a more informed investment decision, assuming that the value of this information could exceed any possible loss occurring during a reasonable deferral period (e.g., loss of market share to competition). Hence, at any moment Yankee can choose to continue to wait and thus hold the option (i.e., as an investment opportunity), $C _ { T } ,$ or implement the operational project, A 1 X (i.e., as an exercised option that yields revenues with the value A and results in real costs, X). (See $\mathrm { F i g \mathrm { - } }$ ure 1C.) Yankee should be indifferent between these two alternatives only when the information available at time T indicates that A is expected to be higher than the point where the two curves become tangent in the left graph.

Fourth, it is necessary to balance the impacts of obtaining valuable information to inform decision making and foregoing revenues from an implemented project. When a firm holds an American IT investment option and deferral means losing some revenues, waiting until the time that the option expires to make the investment can be suboptimal. (See Figure 1D.) ${ \mathrm { A s } } -$ sume we are at time $t _ { 1 } .$ Further waiting until time $t _ { 2 } ,$ with $t _ { 1 } < t _ { 2 } < T ,$ , affects investment value, $A \ : - \ : X ,$ , such that:

• A declines due to the foregone revenues for not implementing the project;

• the marginal value of waiting from time $t _ { 1 }$ to $t _ { 2 } ,$ to resolve uncertainties about the size of expected revenues may be uncertain (but it generally declines); and

• the initial investment cost, X, will become smaller in present value terms.

${ \mathrm { S o } } ,$ depending on the magnitude of these value flows, the value of the option exercised at time $t _ { 1 }$ might be higher than if it were exercised at $t _ { 2 } .$ Following the logic that Yankee can either hold the option or the operational project, option pricing analysis implies that it is optimal to invest at time $t ^ { * } , 0 \leq t ^ { * } \leq T$ when the deferral option takes on its maximum value.

Our discussion to this point suggests major differences between the two modeling approaches. The most basic of them is that unless an attempt is made to explicitly model asymmetric returns (as we explained above), NPV will always undervalue. In other words, blindly following the $\mathrm { N P V } > 0$ decision rule of DCF analysis can be incorrect; for example, a positive NPV at $t _ { 0 }$ would advise that the investment be made now; the value of waiting to implement a project, which can change dramatically under different market conditions, is simply not considered. And, even if one were to modify the standard NPV rule to “invest at time t, such that NPV is maximized (assuming it is positive),” applying this rule would still involve difficulties: DCF analysis provides no way to incorporate new information that arrives, to update estimates of expected revenues; and, calculating NPV for different points in time requires the analyst to estimate a different discount rate for each.

Figure 1

## Issues in Modeling Yankee’s Decision Situation using NPV and Option Pricing

![](/api/attachments/VXK39C4N/fulltext/images/c976c7900c2cd331b8407d4b5bc09439754a571076f64a91b05195635f4ed214.jpg)  
Possible investment values that Yankee can “observe".  
Since A can be between O and infinity, it has an asymmetric probability distribution.

(A) Expected project returns are asymmetrically distributed.  
![](/api/attachments/VXK39C4N/fulltext/images/b6dcea2112c1a92c15070b3c335ccc5ae3769ad18a72f650c6c733147c55b0d7.jpg)

![](/api/attachments/VXK39C4N/fulltext/images/34c27eb28e60cf066f5b09f6f1de4b009651f868c4a2e46ea488652bf216bff3.jpg)  
The thicker line depicts the investment values when the NPV decision rule is followed. This line matches the value line of a call option that matures immediately  
Conceptually, both “views" imply that the distribution of the expected investment value shifts to the right (because all situations involving a negative NPV are avoided).

![](/api/attachments/VXK39C4N/fulltext/images/f9705d0c5e48e0a587b6176b6bbe6b97e274d336cd2d937289f24801a5dab024.jpg)

![](/api/attachments/VXK39C4N/fulltext/images/0b5635553483139f5225cd67396dcc028de168d34fc95a9a53409b3c8da9a590.jpg)

(B) NPV and option pricing imply a “right shift" of the expected value function.  
![](/api/attachments/VXK39C4N/fulltext/images/9c74873a91b13163141bac3b506d8c4fdf1451814c3c7b4f9006038f98ae3728.jpg)  
The value of an option that matures in time $T , C _ { \tau }$ , is greater than that of one that matures immediately, $C _ { 0 } .$  
This means that the ability to defer an investment pushes further to the right the distribution of the expected investment value

![](/api/attachments/VXK39C4N/fulltext/images/0105d504c9361b42a92c05a1328c9579551344c0331ba48f0c0afe35e87f1f48.jpg)

![](/api/attachments/VXK39C4N/fulltext/images/abd1640dc8e0046d6b9494de421602f0e4d20d54825ada2067129c69f6422bdd.jpg)  
(C) Now-or-never projects are of lower value than similar projects that offer the opportunity to defer investment.

![](/api/attachments/VXK39C4N/fulltext/images/5448bd9f4d29b76980ebb96d4983a76f575f01bad250652a90ca35573a79ac2b.jpg)  
For an American option, waiting another time period might be less beneficial. Waiting brings more valuable information as well lowers the investment cost in present value terms, but it also results in the loss of revenues. Depending on which of these tendencies is larger, the A-X line might shift upward or downward, and this could imply that exercising the option earlier is more profitable.

![](/api/attachments/VXK39C4N/fulltext/images/534bb0ab3c6ccd022c62358219dd521de10e65f730d9b65494a622e6712685b8.jpg)

![](/api/attachments/VXK39C4N/fulltext/images/a27c7aa705625eef99b29e5ba0a70c4258b1cb092bb9d37b37931913a0e8d8df.jpg)

(D) Optimal option exercise timing balances costs and benefits.

## Legend:

A — present value of expected revenues from the operational project (i.e., the value of option's underlying risky asset)

X — cost of converting the investment opportunity into an operational project (i.e., the option's exercise price)

T— maximum time to defer conversion of the investment opportunity into an operational project (i.e., the option's time to expiration).

C — value of a call option to defer the investment

Option pricing analysis avoids these difficulties by using models that take into account the fact that changes in revenue expectations will occur as time passes. No parameter adjustments (e.g., discount rate or the expected value of revenues) are needed. Instead, these models incorporate this kind of information by explicitly considering the asymmetric distribution of expected revenues, and their perceived variability. This is accomplished with a model parameter that is referred to as volatility in the finance literature; it reflects the variance of the expected rate of return on the project. Aside from this important “ease of use” issue, applying option pricing concepts is attractive because of the conceptual clarity it brings to the analysis. Yanak’s experience suggested that the high potential variance of expected revenues from a POS debit roll out would be the key element in making the right decision; he was far less concerned about the mean value of the distribution of potential outcomes. In this sense, option pricing seemed just right: it provides an analytical foundation for structuring expectations about the firm’s future business opportunities in a way that matches the thinking of a senior management decision maker.

## 2.3. Fundamental Option Pricing Models (OPMs)

We next present the basics of the two models most commonly used to price financial options: the binomial and the Black-Scholes models. These are also the most fundamental option pricing models that can be used in capital budgeting analyses of IT investments. For clarity in exposition, we first discuss these models in the context of European options; models for American options can be derived from them. We employ the following notation:<sup>1</sup>

C—value of a call option;

A—value of option’s underlying risky asset (stated in terms of the present value of expected revenues from the operational project);

<sup>1</sup>Of all the parameters in these models, clearly r will be the most difficult to estimate in a real option pricing context. A and X must be estimated for NPV as well, and $\mu ,$ as it turns out, does not have to be estimated in our analysis. We also avoid having to estimate a discount rate, in lieu of $r _ { f } ,$ which can be readily observed in the financial markets for a US government debt security of appropriate maturity.

l—rate of return expected on A (growth rate of A over time);

r—volatility, the standard deviation of the expected rate of return on A;

X—option’s exercise price (cost of converting the investment opportunity into the option’s underlying asset, i.e., the operational project);

r<sub>f</sub> —the risk-free interest rate (usually implemented as the rate of return on U.S. Treasury Bills);

$$
r - 1 + r _ {f};
$$

T—option’s time to maturity or expiration $( \mathrm { i . e . , }$ the maximum length of the deferral period).

The binomial model (Cox and Rubinstein 1985, pp. 171–178) assumes that A follows a binomial distribution. Starting at time zero, in one time period Dt, A may rise to uA with probability q or fall to dA with probability $1 \mathrm { ~ - ~ } q .$ where $d < 1 , u > 1$ , and $d < r < u .$ . The terminal value of a call option on A which matures in Dt is

$$
C u = \max [ 0, u A - X ]
$$

or

$$
C d = \max [ 0, d A - X ]
$$

with probabilities q and $1 \ : - \ : q ,$ respectively. By setting $p \equiv ( r - d ) / ( u - d )$ , the current value of the call option can be written as:

$$
\begin{array}{l} C = \frac {p C _ {u} + (1 - p) C _ {d}}{r} \\ = \frac {p \max [ 0 , u A - X ] + (1 - p) \max [ 0 , d A - X ]}{r}. \end{array}\tag{1}
$$

Equation (1) can be applied to determine the two possible values of the call option at time 1, $C _ { u }$ and $C _ { d } ,$ if the option’s underlying asset is uA or dA at time 1, respectively. Similarly, Equation (1) can be applied to an option that matures in n time periods (where $\varDelta t = T / n )$ . The price of a call option calculated using the binomial model, denoted by $\dot { C } ^ { \mathrm { B N } }$ , can be written as the implicit function $C ^ { \mathrm { B N } } = { C ^ { \mathrm { B N } } } ( A , X , T , n , u , d , p , r )$

In the Black-Scholes model (Hull 1993, p. 224), the value of a call option is its discounted expected terminal value, $E [ C _ { T } ]$ . The current value of a call option is given by $C = e ^ { - r _ { f } T } E [ C _ { T } ] ,$ , where $e ^ { - r _ { f } T }$ is the present value factor for risk-neutral investors.<sup>2</sup> A risk-neutral investor is indifferent between an investment with a certain rate of return and an investment with an uncertain rate of return whose expected value matches that of the investment with the certain rate of return. Given that $C _ { T } = \mathrm { m a x } [ 0 , A _ { T } \ : - \ : X ] ,$ , and assuming that $A _ { T }$ is log-normally distributed, it can be shown that:

$$
C = A N (d _ {1}) - e ^ {- r _ {f} T} X N (d _ {2}),
$$

$$
d _ {1} = \frac {\ln (A / X) r _ {f} T}{\sigma \sqrt {T}} + \frac {1}{2} \sigma \sqrt [ - ]{T}, d _ {2} = d _ {1} - \sigma \sqrt [ - ]{T},\tag{2}
$$

where N( ) is the cumulative normal distribution. Call option value, $C ,$ calculated using the Black-Scholes model, denoted $C ^ { \mathrm { B S } } .$ , can also be written as the implicit function $C ^ { \mathrm { B S } } = C ^ { \mathrm { B S } } ( A , \sigma , X , T , r _ { f } )$

## 2.4. Preliminary Comparative Analysis of the Binomial and Black-Scholes Models

The next part of our discussion has two objectives. First, we intend to compare the binomial and the Black-Scholes models in terms of their major assumptions and strengths. (See Table 1). For example, an apparent strength of Black-Scholes is its computational simplicity; it has a closed-form solution. This, in turn, makes it easy to conduct sensitivity analysis using partial derivatives. With the Black-Scholes model, however, what facilitates the derivation of a closed-form solution is two explicit assumptions regarding the distribution of A and the investors’ attitude towards risk. Although it may seem that these assumptions are strict, we will show that they have reasonable basis of interpretation, and that they typically apply to the binomial model as well. Second, we will show that although each model involves explicit assumptions that apply to options on traded assets, these assumptions do not prevent use of the models for options on nontraded assets.

2.4.1. Distribution of the Present Value of the Project’s Expected Revenues. Whereas the binomial model assumes that A follows a binomial distribution, the Black-Scholes model assumes that A is lognormally distributed. Both assumptions are meant to reflect the fact that the value of the underlying asset, A, can increase to infinity, but only fall to zero. Does the binomial distribution offer a better description of A’s behavior? One must recognize that even theorists view the binomial diffusion process as an approximation to another process. The reason has to do with the fact that determining u and $d$ is a difficult empirical problem because asset prices rarely follow the classical multiplicative binomial process. Hull (1993, p. 202) points out a common way to choose these parameters:

$$
\begin{array}{l} {u = e ^ {\sigma \sqrt {\varDelta t}}, d = 1 / u = e ^ {- \sigma \sqrt {\varDelta t}},} \\ {p = (a - d) / (u - d), a = e ^ {u \varDelta t}.} \end{array}
$$

Table 1 Preliminary Comparative Analysis of the Binomial and Black-Scholes Models

<table><tr><td></td><td>Standard Black-Scholes</td><td>Standard Binomial</td></tr><tr><td colspan="3">Explicit Assumptions</td></tr><tr><td>A-value of underlying project</td><td>Lognormally Distributed</td><td>Binomially Distributed (in practice, binomial parameters are typically chosen as if A is lognormally distributed)</td></tr><tr><td>σ-volatility of A</td><td>constant</td><td>constant</td></tr><tr><td rowspan="2">X-option&#x27;s exercise price, r-interest rate</td><td>deterministic</td><td>deterministic</td></tr><tr><td>constant</td><td>constant</td></tr><tr><td>T-option&#x27;s life span</td><td>short-lived (Hull 1993, p. 380)</td><td>no-limit</td></tr><tr><td>Existence of market for A</td><td>A is traded and no arbitrage opportunities exist</td><td>A is traded and no arbitrage opportunities exist</td></tr><tr><td colspan="3">Properties</td></tr><tr><td>Solution approach</td><td>closed-form (analytic) formula</td><td>numeric simulation</td></tr><tr><td>Sensitivity analysis using</td><td>analytic partial derivatives</td><td>numeric approximation of “partial derivatives” (Hull 1993, p. 341)</td></tr></table>

This choice of parameters assumes that, for a small $\varDelta t ,$ the expected return on A and its variance will be $\mu \varDelta t$ and $\sigma ^ { 2 } \varDelta t ,$ , respectively. With this choice of $u ,$ d and $p ,$ as $n \to \infty$ and $\varDelta t \to 0 ,$ , A is assumed to follow the same distribution assumed by the Black-Scholes model—a geometric Brownian motion process: $\varDelta A / A \ = \ \mu A t \ +$ reDt, where $\varDelta A / A$ is normally distributed with mean $\mu T$ and variance $\sigma ^ { 2 } T$ (e is a random drawing from a standardized normal distribution). As $\varDelta t \to 0$ and $n \to \infty ,$ , the binomial diffusion process will converge to the lognormal diffusion process.

2.4.2. Investors’ Risk Attitude. The Black-Scholes model assumes that investors are risk-neutral.<sup>3</sup> This assumption eliminates the need to estimate the opportunity cost of capital of the option, $\delta _ { C } .$ . This cannot be specified because the risk of an option dynamically changes as the value of A changes and as time passes (Brealey and Myers 1988, p. 485). It enables present value discounting of the expected payoffs from the option by $r _ { f } ,$ the continuously compounded risk-free rate of return, independent of risk preferences or market equilibrium considerations. This means that the Black-Scholes model implicitly requires that A be traded and that no arbitrage opportunities exist. Moreover, this also means that, under risk-neutral valuation, the analyst’s experience is prevented from entering the analysis, unlike in other capital budgeting techniques, where the chosen cost of capital reflects what the analyst perceives to be the balance between the risk and reward characteristics of the project.

Does Black-Scholes calculate the “correct” option price? After all, we want to find how much an IT investment option is worth to a specific decision maker, not the entire market. Also, we know that many IT projects cannot be readily traded. This concern also arises with the binomial model. It implicitly assumes risk neutrality because Equation (1) discounts any payoffs from the option by $r = 1 + r _ { f } . $ The fact that Equation (1) involves probability $p ,$ not $q ,$ means that investors will all agree about the relationship between $C , A$ and $r ,$ just as if $A$ were traded. Note that $p \equiv ( r - d ) /$ $( u \mathrm { ~ - ~ } d )$ is the risk-neutral counterpart of the subjective probability $q \equiv ( \delta _ { C } - d ) / ( u - d )$ perceived by a decision maker. Finally, requiring that d $< r < u$ is akin to assuming no arbitrage opportunities $( \mathrm { e . g . }$ , when $r < d < u ,$ an investor can borrow money at r and invest in A to make a riskless profit).

The finance literature offers several strong arguments in support of our case for using the Black-Scholes model to price IT investment options. Mason and Merton (1985) offer the most intuitive argument. They suggest that, in capital budgeting, irrespective of whether a project is traded, we seek to determine what the project cash flows would be worth if they were traded $( \mathrm { i . e . , }$ as their contribution to the firm’s market value<sup>4</sup>). According to this argument, a firm should seek to avoid having the analyst’s subjectivity enter the analysis so as to prevent arbitrage opportunities. No matter though: over time project valuation biases resulting from analyst subjectivity would lead to arbitrage opportunities that the market will “correct”. To see this point, consider the following two possibilities. First, if the analyst uses a cost of capital that is too high, the project’s calculated NPV will be lower than it should be. This phenomenon leads a firm to underinvest, and thus fail to exploit its potential to yield higher returns. Because the firm will then “trade” for less than it is worth, eventually there will be some economic agent who would be inclined to purchase the firm. Alternately, if the analyst uses too low a cost of capital, the firm would end up investing in projects that don’t produce profits consistent with the opportunity costs of capital invested elsewhere. If this occurs on a widespread basis within a firm, it is doomed to failure in the marketplace.

In summary, our preliminary comparative analysis shows two things. First, the major assumptions of the Black-Scholes model are based on a reasonable interpretation of the underlying economics of capital budgeting in a competitive market. Second, these assumptions are comparable to the ones made by the binomial model. The second observation means that $C ^ { \mathrm { B N } }$ would converge to $C ^ { \mathrm { B S } }$ under the following conditions (Cox and Rubinstein 1985, p. 205). In practice, the binomial model sets a in Equation (3) to be $a = e ^ { r { \cal A } t }$ because of the risk-neutrality assumption. Thus, we can write $C ^ { \mathrm { B N } } = C ^ { \mathrm { B N } } ( A , \sigma , \dot { X } , T , r _ { f } )$ with $u = u ( \sigma , r ) , d = d ( u )$ $p = p ( u , d , r _ { f } ) , r = r ( r _ { f } ) _ { }$ , and n is an arbitrary value in our control. Also, when the period of time, T, is long enough (one year or more), choosing n to be large enough (where $\varDelta t = T / n , n = 3 0 0$ or so) ensures that the multiplicative binomial process would converge to the Black-Scholes lognormal diffusion process.

In light of this discussion, we see no disabling conceptual difficulties associated with our selection of the Black-Scholes model over the binomial model for analyzing the case of Yankee 24’s decision to roll out POS debit services.<sup>5</sup> Black-Scholes offers both computational simplicity and strong support for sensitivity analysis, as we will shortly illustrate. Because its solution is a closed-form expression, one can analyze changing expectations about the key variables in a way that matches the analyst’s intuition about the likely impact of a changing environment on profitability estimates that form the basis for rational decision making.

## 3. Applying the Black-Scholes Model

In Yankee 24’s case, using the standard Black-Scholes model is not possible because Yankee possessed an

American option on a dividend paying asset. In this instance, the reader can think of dividends as the revenues lost during the time that Yankee deferred POS debit market entry. However, Black-Scholes is the basis for several models for pricing American options; some of these are analytical in nature and some are procedural, enabling an analyst to establish option value (see Hull 1993, p. 235). Of these models, we chose to use a procedural model called Black’s approximation for its simplicity and its relative accuracy in computing option value.<sup>6</sup> We next review this model and then discuss the results of its application to Yankee’s decision problem.

## 3.1. Pricing Yankee’s Option Using Black’s Approximation

Black’s approximation assumes the existence of an American call option that matures at time T, where the underlying asset pays a dividend D at time $t , 0 < t < T$ To find whether an early exercise at time t is more profitable, this procedure requires using the standard Black-Scholes to calculate the prices of European options that mature at T and $t , C _ { T }$ and $C _ { t } ,$ and then setting the American price to be the higher of these two. Of course, to compute $C _ { t } ,$ the value of the underlying asset used in Equation (2) must be A less the foregone dividend, $D ,$ discounted for the period $T - t .$ . This procedure can also be applied when there are a number of ex-dividend dates.

To analyze the investment decision Yankee faced in 1987, we used interview data from senior managers to arrive at specific assumptions concerning the parameters needed by the Black-Scholes model. Based on the earlier POS debit experience in California and Yanak’s opinions, our analysis will assume that the New England market was estimated to be 25% the size of the California market for POS debit transactions. Another concern was to estimate the range of potential revenues on the high and the low end, the distribution of revenues (i.e., normal, or skewed to the high or the low side), the perceived variance or volatility (r) of potential revenues (if there was any), and the uncertainties that might be resolved and thus contribute to r. Interview questions were geared towards revealing the various estimates, assuming that the actual entry would occur sometime between 1987 and 1990. The interview process revealed an estimate for this key model parameter, $\sigma ,$ of between 50% to 100%.<sup>7</sup> The estimates were based on crucial uncertainties about when the state of Massachusetts, representing one-half of the overall market potential, would deregulate POS debit entry by firms outside the state. For the present analysis, we chose to use the low end estimate, which may underestimate the actual uncertainties that Yankee faced with Massachusetts state law.

Using Black-Scholes, we calculated the option value for different exercise dates ranging from zero to four years at intervals of one-half year, utilizing the parameter values and assumptions shown in Table 2. Table 2 also shows results that were computed by applying Black’s approximation. The results can be summarized as follows:

• The value of the project investment option, $C _ { T } ,$ exercised at maturity, $T = 4 ,$ , is \$65,300, as shown in Row $C _ { T } ;$

• The value of the option, $C _ { t } ,$ maturing at time $t < T ,$ is greater than its value at maturity for deferrals between 1 to 3 1/2 years, as shown in Row $C _ { t } . ~ ( C _ { t }$ is calculated based on values for $A _ { t }$ that reflect the loss of revenues and passage of time.)

• The value of the deferral option, $C _ { t } ,$ reaches its maximum for a deferral of three years at \$152,955, as shown in bold in Row max $( C _ { t } , C _ { T } )$

These results suggest two conclusions, assuming that the New England market size is 25% of California’s and r is as high as 50%. First, Yankee is better off by not waiting to implement the POS debit project for four years, so long as the roll out occurs after the end of the first year $( C _ { T } < C _ { t } ,$ , for $1 \leqslant t < 4 )$ . Second, the optimal time to defer is three years $( C _ { 3 } = \ S 1 5 2 , 9 5 5 > C _ { t } ,$ for all t except 3). The logic behind these conclusions is clear. Recall from §2.2 and Figure 1 that, for certain expected values of $A ,$ the values of the investment opportunity and the operational project were equal. As a result, a risk-neutral firm would be indifferent between holding either. By the same token, profit maximizing decisions taken by the firm’s management on behalf of its shareholders would prompt it to convert an investment opportunity into an operational project at that point in time at which the value of the investment opportunity—in this case, the deferral option—takes on its maximum value.

## 3.2. Sensitivity Analysis Using Black-Scholes Derivatives

Sensitivity analysis aims at showing how the results of an analysis change as its underlying assumptions (expressed in terms of the model’s parameters) change. First derivative analysis in the context of the Black-Scholes model is much used in the investment arena for analyzing the sensitivity of the value of a financial option to changes in the variables. Vega, delta, $x i ,$ theta and rho—the “Greeks” or “Fraternity Row” as they are often referred to by practitioners—provide the investment analyst with a ready means to discover a financial option’s sensitivity to changes in the time to expiration, increases and decreases in the assessed market value of the underlying security, and changes in the exercise price, risk-free rate or the historical price volatility of the underlying asset:

$$
v e g a = \Lambda = \frac {\partial C}{\partial \sigma}, d e l t a = \Delta = \frac {\partial C}{\partial A},
$$

$$
x i = \Xi = \frac {\partial C}{\partial X}, t h e t a = \Theta = \frac {\partial C}{\partial t},
$$

$$
r h o = \rho = \frac {\partial C}{\partial r _ {f}}.\tag{3}
$$

$\mathrm { A s }$ shown in Equation (3), the derivatives are computed with respect to the value of the call option, for

Table 2 Optimal Investment Time Calculated Using Black’s Approximation and Sensitivity Analysis Data

<table><tr><td>t(length of deferral period) Calendar time</td><td>0 Jan. 87</td><td>0.5 July 87</td><td>1 Jan. 88</td><td>1.5 July 88</td><td>2 Jan. 89</td><td>2.5 July 89</td><td>3 Jan. 90</td><td>3.5 July 90</td><td>4 Jan. 91</td></tr><tr><td></td><td colspan="9">Black-Scholes Parameter Values</td></tr><tr><td> $A_t(A_0 \text{ less revenues foregone during waiting})$ </td><td>$323,233</td><td>$342,216</td><td>$360,083</td><td>$376,230</td><td>$389,207</td><td>$395,566</td><td>$387,166</td><td>$344,813</td><td>$223,295</td></tr><tr><td> $X_t(discounted investment cost, X_0)$ </td><td>$400,000</td><td>$393,179</td><td>$386,473</td><td>$379,883</td><td>$373,404</td><td>$367,036</td><td>$360,777</td><td>$354,625</td><td>$348,577</td></tr><tr><td> $A_t - X_t$ </td><td>($76,767)</td><td>($50,963)</td><td>($26,391)</td><td>($3,652)</td><td>$15,803</td><td>$28,530</td><td>$26,389</td><td>($9,812)</td><td>($125,281)</td></tr><tr><td></td><td colspan="9">Black&#x27;s Approximation Results</td></tr><tr><td> $C_T(\text{option maturing at time } T)$ </td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>$65,300</td></tr><tr><td> $C_t(\text{option maturing at time } t)$ </td><td>$0</td><td>$32,024</td><td>$66,093</td><td>$96,830</td><td>$123,786</td><td>$144,565</td><td>$152,955</td><td>$134,873</td><td>$65,300</td></tr><tr><td> $\max(C_T, C_t)$ </td><td>$65,300</td><td>$65,300</td><td>$66,093</td><td>$96,830</td><td>$123,786</td><td>$144,565</td><td>$152,955</td><td>$134,873</td><td>$65,300</td></tr><tr><td>Suggested deferral time (in years)</td><td></td><td>0.5</td><td>1.0</td><td>1.5</td><td>2.0</td><td>2.5</td><td>3.0</td><td>3.5</td><td>4.0</td></tr><tr><td></td><td colspan="9">Sensitivity Analysis Data (for  $C_t$ )</td></tr><tr><td>Delta</td><td></td><td>0.434</td><td>0.571</td><td>0.647</td><td>0.696</td><td>0.727</td><td>0.738</td><td>0.716</td><td>0.578</td></tr><tr><td>Gamma</td><td></td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>Theta</td><td></td><td>-47611</td><td>-35337</td><td>-28529</td><td>-24065</td><td>-20809</td><td>-18190</td><td>-15617</td><td>-10921</td></tr><tr><td>Vega</td><td></td><td>95223</td><td>141350</td><td>171177</td><td>192526</td><td>208095</td><td>218284</td><td>218650</td><td>174739</td></tr><tr><td>Xi</td><td></td><td>-0.2914</td><td>-0.3490</td><td>-0.3666</td><td>-0.3677</td><td>-0.3571</td><td>-0.3321</td><td>-0.2800</td><td>-0.1594</td></tr></table>

<table><tr><td>Year-Month</td><td>Number of Transactions</td><td>Revenues</td><td>Costs</td><td>Cash Flows</td></tr><tr><td>Jan. 87</td><td>0</td><td>$0</td><td>$0</td><td>$0</td></tr><tr><td>July 87</td><td>0</td><td>$0</td><td>$0</td><td>$0</td></tr><tr><td>Jan. 88</td><td>3,532</td><td>$353</td><td>$20,000</td><td>($19,647)</td></tr><tr><td>July 88</td><td>8,606</td><td>$861</td><td>$20,000</td><td>($19,139)</td></tr><tr><td>Jan. 89</td><td>20,969</td><td>$2,097</td><td>$20,000</td><td>($17,903)</td></tr><tr><td>July 89</td><td>51,088</td><td>$5,109</td><td>$20,000</td><td>($14,891)</td></tr><tr><td>Jan. 90</td><td>124,470</td><td>$12,447</td><td>$20,000</td><td>($7,553)</td></tr><tr><td>July 90</td><td>303,258</td><td>$30,326</td><td>$20,000</td><td>$10,326</td></tr><tr><td>Jan. 91</td><td>738,857</td><td>$73,886</td><td>$20,000</td><td>$53,886</td></tr><tr><td>July 91</td><td>1,800,149</td><td>$180,015</td><td>$20,000</td><td>$160,015</td></tr><tr><td>Jan. 92</td><td>4,385,877</td><td>$438,588</td><td>$20,000</td><td>$418,588</td></tr></table>

## Assumptions:

1. —The New England market is 25% of the California market, and the POS debit transaction volume expected in New England is estimated based on the experience in California. Until the end of 1991 the total number of POS debit transactions in California was around 12 million, and by the end of 1992 the number of transactions per month rose to 10 million. These figures imply a 16% per month growth rate in transaction volume in California between 1985 and 1992. This growth rate is consistent with expert estimates of the growth rate expected between 1993 and 1996. Assuming that the New England and California markets are similar, except for size, we applied a similar growth rate. (A similar estimate would have been established based on the transaction volume in California between 1985 and 1987.) A base of 2,500,000 transactions for December 1992 is used, based on a corresponding 10,000,000 figure in California. The base figure is discounted back by the 16% growth rate per month, and the monthly transaction volumes are aggregated by year.

2. —the present value of revenues less operational costs, where the discount rate of 12% approximates the rate used for capital budgeting of othe electronic banking investments at the time. The yearly operational marketing cost is \$40,000 (\$20,000 every six months), and the revenue per transaction is 10¢. Once an entry decision is made, it takes one year to begin servicing customers.

3. —initial (sunk) technical investment is \$400,000.

4. r—volatility of expected revenues is 50%.

5. —the maximum deferral period in years, from (early) 1987 to (early) 1992, is also the analysis horizon of 5 1/2 years.

6. —7% annual risk-free interest rate.

volatility, the value of the underlying project asset, the cost to exercise the option, the time decay of the option as expiration nears, and changes in the risk-free rate, respectively. In addition to providing the analyst with a reading on the sensitivity of an option position to these parameters, option derivative analysis is also used to devise hedging strategies that ensure a position is immunized against movements or changes in the parameters that create market or instrument risk.

These sensitivity analysis methods are similarly applicable to IT capital budgeting problems. The expected value of a project that embeds an option may change as time passes, based on changes in the exogenous environment of the project, the managerially controllable environment, and so on. (In the real world, we observe that IBM OS/2-based computing infrastructures have become less attractive as time has passed, and Microsoft’s Windows NT has gained installed base in the world of client-server computing. As a result, the value of IS projects involving phased roll out of an OS/2 platform, or of applications that depend on OS/2 for crucial support, has been negatively affected over time.) To apply these ideas in Yankee’s case, let us assume that the volatility of Yankee’s POS debit-related revenues drops by a certain percentage $( \mathrm { e . g . }$ , because Yankee is excluded from entering the Massachusetts market for regulatory reasons). Would entry still make sense? Or, what if the time horizon for deferral were viewed as possibly being longer than four years, based on a reassessment of NYCE’s inability to put the critical resources in place to enable a competitive POS debit service launch? When Black-Scholes is used, we can answer many such questions easily with derivative analysis, without having to reestimate any variables or recompute any models.

To answer the first of these two questions, let us consider the first derivative of the Black-Scholes call option value with respect to volatility, vega $= \Lambda = \partial C /$ $\partial \sigma = A \sqrt { T } N ^ { \prime } ( d _ { 1 } )$ . Assume that A 4 \$387,166 for a New England market 25% the size of California’s, with $X =$ \$400,000, r 4 50%, and t 4 3. The vega derivative results are shown in Table 2, which we examined in the prior subsection. This relationship tells us that a 1% change in $\sigma ,$ the variance of the expected revenues from the IT project, causes NPV to change by K. (Recall that an increase in r is valuable because of A’s asymmetric nature—the present value of the project’s expected revenues may go 1% higher than before, yet still go no lower than zero.) In Yankee’s case, K 4 218,284 indicates that an increase in r from 50% to 51% increases the value of the deferred investment option by \$2,183. This figure can be viewed as an upper limit on the amount of money Yankee should be willing to spend $( \mathrm { e . g . } ,$ on lobbying for regulatory changes in Massachusetts) to increase r by 1%. It also points out that increasing uncertainty makes the option to defer entry more valuable. Table 2 includes the other derivative results for comparison purposes for the reader.

A final feature of Black-Scholes analysis is that one can analytically derive values for volatility that are consistent with a given valuation of an investment opportunity. Finance practitioners know volatility in this guise as implied volatility, $\sigma ^ { \prime } \colon$ it is the variance of the underlying asset that is consistent with (or implied by) the other variables, including the observed market value of the option. In theory, this enables an analyst to determine a break-even point for any combination of option parameters. Thus, assuming that r is unknown and that all other parameters, including C, are given, one can compute the Black-Scholes implied volatility. This is similar conceptually to computing the internal rate of return (IRR) in the context of NPV analysis.

## 3.3. Retrospective Results Analysis

The results of our option pricing analysis are supportive of the decision Yankee’s senior executive made at the time. Yankee deferred entry into the POS debit market for three years, which was later recognized to have been just about optimal. However, Yanak’s decision had to be taken without the kind of supportive quantitative guidance that powerful analytical techniques such as option pricing can provide. Instead, he admitted to us that there was more “seat-of-the-pants” decision making than he wished there had been. First, Yanak believed that uncertainty about the acceptance rate of POS debit services declined significantly, based on results from POS debit roll out undertaken in other parts of the country. For example, by 1989 dramatic growth had begun to occur in California’s POS debit market. Second, Yankee’s ATM switching business had reached a mature stage, freeing up resources to push

Table 3 In Depth Comparative Analysis of the Fundamental OPMs

<table><tr><td></td><td>Standard Black-Scholes</td><td>Standard Binomial</td></tr><tr><td colspan="3">Implicit Assumptions</td></tr><tr><td>A</td><td></td><td></td></tr><tr><td>*Allowed to become negative</td><td>no,  $A \in (0, \infty)$ </td><td>no,  $A \in (0, \infty)$ </td></tr><tr><td>*Bias when A is not lognormal</td><td>bias can be characterized qualitatively</td><td>bias cannot be characterized, not even qualitatively</td></tr><tr><td>*Growth-rate( $\mu$ ) can fall below  $r_f$ </td><td>not allowed</td><td>not a concern</td></tr><tr><td>*A pays dividends</td><td>not allowed</td><td>allowed</td></tr><tr><td></td><td>(some variations of Black-Scholes allow)</td><td></td></tr><tr><td> $\sigma$ </td><td></td><td></td></tr><tr><td>*Can be (very) small</td><td>yes</td><td>no</td></tr><tr><td>*Can be nonconstant</td><td>no</td><td>yes</td></tr><tr><td>(e.g., depend on A, diminish over time)</td><td></td><td></td></tr><tr><td colspan="3">Properties</td></tr><tr><td>Calculates option price on-or-before expiration</td><td>no (only on expiration)</td><td>yes (can find optimal exercise time)</td></tr><tr><td>Others</td><td>computational simplicity</td><td>conceptual simplicity and flexibility</td></tr></table>

POS debit services. Third, and most important, however, was an event in mid-1989 that had been previously unexpected. The Food Marketing Institute, a supermarket industry research and lobbying organization, released a study that clearly demonstrated to retailers the benefits of POS debit transactions over other payment forms—the average transaction cost per sale was 0.82% of the sale value for POS debit, in contrast to 1.2% for checks and 2.1% for cash. The results of this study became the primary tool in educating retailers. With the turn of events in New England, good fortune played a central role in the outcome of Yankee’s implementation of POS debit. With option pricing as an analytical tool to evaluate the project, for the first time, the content of the quantitative analysis paralleled the content of Yanak’s unassisted reckoning of what to do: the idea of getting the timing right, subject to a range of volatile and uncontrollable future events, had now been included in the formal analysis.

By mid-1990 Yankee had its first commitment from one of the largest regional supermarket chains, Hanoford Brothers, which decided to pilot the POS debit services in nine supermarkets in Maine and New Hampshire. Yankee’s second major POS debit sign-up was New England’s largest convenience store chain, Stop & Shop, which chose to pilot POS debit in Rhode Island. Yankee hoped that this pilot would help it to persuade legislators that POS debit was a service in the public interest, and lead to a change of the law in Massachusetts. Since that time, the growth in Yankee’s POS debit business was phenomenal, from no POS debit terminals in 1990 to a total of about 27,000 terminals in early 1993.

## 4. Breadth of Application of OPMS

Although we have illustrated the strengths of the Black-Scholes model in a realistic and practical IT investment evaluation case, we have not discussed some critical issues that can threaten the validity of our analysis. The decision to apply OPMs, as well as our selection of the binomial versus the Black-Scholes model, may appear straightforward to the reader, based on our discussion of the issues in §2. In practice, however, one must understand the implications of several other issues. Table 3 shows how these issues relate to implicit assumptions that OPMs make concerning the option being evaluated.

## 4.1. Assumptions About the Distribution of the Present Value of the Project’s Expected Revenues

Implicit assumptions regarding the behavior and distribution of A raise two important issues. First, what happens when A can become negative? This issue was not relevant in Yankee’s case; it would have been if, for example, below a certain volume of POS debit transactions the cost of processing a transaction were to exceed the revenues produced by that transaction. When A may become negative, both fundamental OPMs cannot be applied. However, there are alternative models that involve variations of Black-Scholes and the binomial models that will work. For example, there is a variation of Black-Scholes that assumes that A is normally distributed. A second method based on the binomial model assumes that A follows an additive binomial process whereby A can go up to $A + u$ or down to $A + d \left( { \mathrm { S i c k } } 1 9 9 0 , { \mathrm { p } } . 3 6 \right)$ . We caution the reader that these models can provide only a “gross” approximation of the option price.

What happens when A’s distribution does not follow the lognormality distribution? Hull (1993, pp. 436–438) distinguishes between several such situations and characterizes the resulting Black-Scholes pricing biases qualitatively, in terms of the option being slightly overor under-priced. Quantifying these biases requires exact modeling of $A ^ { \prime } { \sf s }$ distribution. This observation also applies to the binomial model when Dt is sufficiently small and the parameters in Equation (3) are such that the multiplicative binomial diffusion process converges to the lognormal process. Otherwise, there is no way to characterize the resulting price biases in the binomial model—not even qualitatively. This should be of concern when the calculated option price is small in absolute terms, something which could wrongly suggest undertaking an investment.

## 4.2. Assumptions About Volatility

Two questions arise with respect to the size and behavior of A’s volatility. What happens when r is small? This question is critical in cases where use of the binomial model is considered. When r is small, parameter p (expressed as the ratio $( r - d ) / ( u - d ) )$ in Equations (1) and (3) can exceed one and lose its probabilistic meaning (Hull 1993, p. 351). For example, in Yankee’s case, the binomial model would be impossible to use with values of r smaller than 12%. In this case, option pricing analysis would fail to identify cases where the value of a deferred POS debit entry calculated as C would be large enough to justify a positive investment decision.

And, what happens when r is not constant? We consider the most likely case to be one in which r declines over time when T, the option life, is significant relative to the life of the underlying project. This behavior of r could also be relevant when the market stops growing quickly, after an initial period of explosive growth $\left( \mathrm { e . g . } \right.$ ., massive initial adoption of some new IT, followed by a rapid slow down when bugs or integration problems are discovered). As volatility is lost, and the expected, but uncertain outcome becomes known to the analyst, option pricing becomes less attractive.

## 4.3. Assumptions About the Option’s Exercise Time

Can the fundamental OPMs find a $t \leq T$ for which it is optimal to exercise an option? In Yankee’s case, since C is not linear with respect to T (and ignoring the competition for a moment), Yanak faced an especially interesting question: How long could Yankee defer POS debit entry before starting to observe a diminishing “invesment value”?

The answer to these questions relates to the ability to calculate the value of the option, C, on or before its expiration. With the standard Black-Scholes model, which computes C assuming that the option can be exercised only upon its expiration, finding t would require repeating the option pricing analysis for various entry points within the time frame of $T < 4$ (e.g., 1988, 1989 and 1990 at the beginning and end of each year), as we did using Black’s approximation. However, some advanced variations of Black-Scholes, such as the analytical model developed by McDonald and Siegel (1986), enable an analyst to determine optimal investment timing (when the model’s underlying assumptions are met). The binomial model may also be attractive here because it can easily calculate C on-or-before expiration. The mechanism used is to calculate C for every node in the binomial tree, thereby allowing the analyst to identify time t corresponding to a node where C takes on its maximum value.

## 4.4. Assumptions About the Option’s Exercise Price

In situations where the exercise price, X, is stochastic— as it often will be in realistic applications of option pricing to IT investments—the binomial model can be readily adapted for the analysis: it allows the analyst to program the binomial tree to reflect any kind of changes in X that may occur over time. Alternately,

Margrabe’s asset-for-asset exchange model, which Dos Santos (1991) introduced to the IS literature, deals with this problem in the context of multistage IT project investment analysis, and extends Black-Scholes to handle stochastic exercise prices. However, applying this model requires the analyst to develop an understanding of how the underlying asset, A, and the exercise price, X, are correlated. Unfortunately, this has proven to be as difficult an empirical problem as any we have discussed up to this point in the paper.

For these reasons, we conclude that the binomial model is an attractive alternative for evaluating IS projects involving options for the firm. However, it may make more sense to employ Black-Scholes (or one of its near variants) when the behavior of various option parameters is less complex. By contrast, the binomial model’s conceptual simplicity is buttressed by the flexibility to allow the analyst to model parameters such as A and r by “programming” more complex behaviors into the binomial tree, for example, to illustrate how they evolve over time.

## 5. Conclusions

A major challenge for IS research lies in making models and theories that were developed in other academic disciplines usable in IS research and practice. In this paper, we explored a range of issues associated with the application of option pricing models to problems in capital budgeting for IT investment projects. Though the models and their basis in theory are well known to finance academicians, most people who do capital budgeting—irrespective of their training or the kinds of projects they typically assess—are illequipped to use option pricing models knowledgeably. This is especially true among IS professionals, who have long relied on net present value, simple costbenefit analysis, critical success factors and other lessstructured techniques to perform their assessments. Thus, our goal has been to critically review the case for using option pricing as a basis for IT project investment analysis and to evaluate its merits in an actual real world business setting. In the process, we learned that the binomial, Black-Scholes and the Margrabe models all require different kinds of information and assumptions than are usually needed to perform traditional capital budgeting analysis using present value concepts. But, on the whole, the difficulties we encountered pose no greater challenges than when traditional techniques are used. More importantly, in view of the structure of many IT projects that involve infrastructure development and wait-and-see deployment opportunities, it is the logic of option pricing that persuades us—how it can handle getting the timing right, scaling up or even abandonment, as the organization learns about its business environment with the passage of time. The difficulties that do remain in applying option pricing models (e.g., the restrictions associated with the assumption of lognormality of the perceived value of the IT project, or the lack of experience that managers have in estimating the variance of project returns) to IT project assessment will not be solved by additional finance research. Instead, IS researchers must take the lead in solving them and in better understanding the perceived business value of IT projects.

In closing, we invite the reader/practitioner to consider the extent to which use of the Black-Scholes option pricing model generalizes beyond the case that we describe. In fact, the Yankee 24 POS debit scenario situation occurs among a number of different classes or kinds of IT investment situations that we can analyze with these methods. The key to understanding the IT investment settings or classes of project investments in which option pricing is worthwhile to use relates to basic elements of the Black-Scholes model. For example:

(1) IT infrastructure investments often are made without any immediate expectation of payback, however, they can act as a basis for follow on investment that converts investment opportunities into the option’s underlying asset, the operational IT projects that support a specific business process which yield measurable revenue. Some examples of these investments include intranet and multi-media user interface technologies, financial and operational risk management technologies and security safeguards, data warehousing, and wireless technical infrastructure.

(2) Emerging technology investments pose a special challenge for forecasting value payoffs in the face of uncertain cost, adoption and diffusion. In this context, the value of the underlying asset—the project that incorporates the emerging technology—is subject to both changing perceptions of future costs on the part of the analyst and the marketplace at large. In this case, the analyst’s interest in reflecting the impact of stochastic cost (uncertain exercise price) is what drives the use of option pricing. Projects that involve Internet advertising and selling, migration to an electronic market mechanism for transacting, and bets about whether a technical advance will become a standard in the marketplace are good real world examples. In each case, the future cost associated with exercising an option to build on a network, a market mechanism or a standard, is unknown today.

(3) Application design prototyping investments also provide significant option value, as Chalasani et al. (1997) have observed. With prototyping, the firm aims to maximize the value of an application development project whose value will ultimately be determined by how well its functionality can remain in synch with the support needs of a changing business process. The value inherent in the underlying asset is of somewhat less interest to the firm than the ability to react: to both adapt and change the application’s functionality as required to remain competitive. One can imagine the difference in value that might be obtained by applying option pricing methods, especially when the application’s requirements specification is subject to significant change as the project progresses. Clearly, when there is considerable uncertainty in an organization about whether an application will be able to “do the job” when it is delivered, or there is risk aversion on the part of management in making capital investments in IT, efforts to stage or “chunk” such projects, and monitor their payback over time, is an appropriate approach.<sup>8</sup> From this perspective, much of the value of a prototype project will be in the options that it offers the firm in the future.

(4) Technology-as-product investments represent a fourth class of investments that these methods can handle well. When the technology is a core part of a product, issues of level of commitment and ramp up, timing and roll out, and delay and abandonment must be considered. Here, the analyst can benefit from framing such choices in the context of option pricing by focusing on such elements as time remaining to exercise, when the option matures and by tracking the value of the option to change the course of a project. Here, so many of the best known stories of our time about technologybased products come to mind, for example, Otis Elevator and the decision to recapture the after-market for its elevator servicing, Chemical Bank’s failure with the Pronto home banking project, Morgan Bank’s success with RiskMetrics for financial risk management in international commercial banking, and First Boston Corporation’s decision to create products and a new company, Seer Technologies, from what had been a major systems infrastructure building project.

In this paper, we have made the argument that option pricing models can be applied to capital budgeting decisions involving nontraded information technology assets. We have discussed a number of reasons why the discipline of capital budgeting more generally examines asset values as though the assets were traded, because every firm’s capital budgeting decisions, in the long run, are subject to market valuation. This insight opens up a range of new modeling opportunities for project and information technology investments. We illustrated how the Black-Scholes model can be applied in the case of a real world IT investment option, where significant uncertainties that are not appropriately handled using NPV analysis were present. Yet, much remains to be done if we to are make sense of the OPMs in the way that finance professionals do: as a means to evaluate the extent to which market-sensitive portfolios of financial instruments can be engineered so as to minimize unacceptable risk. Perhaps one of the most important next steps in this research stream is to examine the extent to which option pricing concepts can be applied to gauge the risks associated with the portfolio of IT projects that make up the IS function in a firm. This may lead us to a new science of risk management for the firm’s portfolio of investments in IT, and a new perspective on the business value of IT for senior executives.<sup>9</sup>

of the Yankee 24 regionally shared electronic banking network in New England. We also received helpful comments from John King (University of California, Irvine), Hank Lucas (New York University), David Runkle (Federal Reserve Bank of Minneapolis), Tim Nantell (University of Minnesota), an anonymous reviewer and the participants in presentations we have given on this topic at New York University, the University of Minnesota, Syracuse University, and the Workshop on Information Systems and Economics. All errors of fact or interpretation remain the sole responsibility of the authors.

## References

Baldwin, C.Y. and H.R. Clark, “Modularity and Real Options,” Working Paper, Harvard Business School, Cambridge, MA, 1994.

Brealey, R.A. and S.C. Myers, Principles of Corporate Finance, Mc Graw-Hill, New York, 1988.

Chalasani, P., S. Jha, and K. Sullivan, “The Options Approach to Software Prototyping Decisions,” Technical Report, Carnegie Mellon University, Department of Computer Science, Pittsburgh, PA, August 1997.

Clemons, E.K., “Evaluating Strategic Investments in Information Systems,” Comm. ACM, 34,1(1991), 22–36.

Cox, J.C. and M. Rubinstein, Options Markets, Prentice-Hall, New York, 1985.

Dixit, A.K. and R.S. Pindyck, Investment Under Uncertainty, Princeton University Press, Princeton, NJ, 1994.

Dos Santos, B.L., “Justifying Investment in New Information Technologies,” J. Management Information Systems, 7, 4(1991), 71–89.

Hull, J.C., Options, Futures, and Other Derivative Securities (2nd edition), Prentice Hall, Englewood Cliffs, NJ, 1993.

Kambil, A., C.J. Henderson, and H. Mohsenzadeh, “Strategic Management of Information Technology: An Options Perspective,” in R.D. Banker, R.J. Kauffman and M.A. Mahmood (Editors),

Strategic Information Technology Management: Perspectives on Organizational Growth and Competitive Advantage, Idea Group Publishing, Middletown, PA, 1993.

Kauffman, R.J., B. Konsynski, and C.H. Kriebel, “Evaluating Research Approaches to IT Business Value Assessment with the Senior Management Audience in Mind: A Question and Answer Session,” in R.D. Banker, R.J. Kauffman and M.A. Mahmood (Editors), Strategic Information Technology Management: Perspectives on Organizational Growth and Competitive Advantage, Idea Group Publishing, Middletown, PA, 1993.

Kogut, B. and N. Kulatilaka, “Operating Flexibility, Global Manufacturing and the Option Value of a Multinational Network,” Management Sci. 40, 1(1994), 123–139.

Kumar, R., “A Note on Project Risk and Option Values of Investments in Information Technologies,” J. Management Information Systems, 13, 1(1996), 187–193.

Margrabe, W., “The Value of an Option to Exchange One Asset for Another.” J. Finance 33, 1(1978), 177–186.

Mason, S. and R. Merton, “The Role of Contingent Claims Analysis in Corporate Finance,” in E.I. Altman and M.G. Subrahmanyam (Editors), Recent Advances in Corporate Finance, Richard D. Irwin, Homewood, IL, 1985.

McDonald, R. and D. Siegel, “The Value of Waiting to Invest,” Quarterly J. Economics, 101(1986), 705–727.

Nichols, N.A., “Scientific Management at Merck: An Interview with CFO Judy Lewent,” Harvard Business Rev., January–February (1994), pp. 88–99.

Sick, G., Capital Budgeting with Real Options, Monograph Series in Finance and Economics, Salomon Brothers Center for the Study of Financial Institutions, Stern School of Business, New York University, New York, 1990.

Trigeorgis, L. (Ed.) Real Options in Capital Investment, Praeger Publishers, Westport, CT, 1995.

——. Real Options, MIT Press, Cambridge, MA, 1996.

John Leslie King, Associate Editor. This paper was received on May 14, 1996, and has been with the authors 8 months for 2 revisions.
