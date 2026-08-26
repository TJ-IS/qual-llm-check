---
otero_id: 25035
otero_key: "BHZQRYY4"
title: "Information Systems for Optimal Transaction Implementation"
authors: "John T. Rickard; Nicolo G. Torre"
year: "1999"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1999.11518245"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems for Optimal Transaction Implementation

John T. Rickard & Nicolo G. Torre

To cite this article: John T. Rickard & Nicolo G. Torre (1999) Information Systems for Optimal Transaction Implementation, Journal of Management Information Systems, 16:2, 47-62, DOI: 10.1080/07421222.1999.11518245

To link to this article: http://dx.doi.org/10.1080/07421222.1999.11518245

![](/api/attachments/BHZQRYY4/fulltext/images/3214d87a870e3e053854e6234bb05ad81d33692be0ebc12dec5b250888828ac2.jpg)

Published online: 02 Dec 2015.

![](/api/attachments/BHZQRYY4/fulltext/images/b610c3b2a63b479e2f8ab2587cf3ae235781515dc1eb228437df606ae9b29e6e.jpg)

Submit your article to this journal ↗

![](/api/attachments/BHZQRYY4/fulltext/images/24dc0c6e9e3217f309ee53a0eaa5ab9c48764032dace7924b1c56a68300a5939.jpg)

Article views: 3

![](/api/attachments/BHZQRYY4/fulltext/images/da778c65314f2f6c28c93bde6599401026c54b6019f98ba7c20c8ffb90de6eea.jpg)

View related articles ↗

![](/api/attachments/BHZQRYY4/fulltext/images/fb1b5f149896bf84ac5df7d93f3d235a0e50c683a489abead37a7e5c69326545.jpg)

Citing articles: 1 View citing articles ↗

# Information Systems for Optimal Transaction Implementation

JOHN T. RICKARD AND NICOLO G. TORRE

JOHN T. RICKARD served as President of OptiMark Technologies, Inc., and its predecessor companies from 1994 to early 1999 and continues to serve as a director of the company. He is a coinventor of the OptiMark system and has spent the past four years developing the design and implementation plans for the system. After OptiMark began live trading operations in early 1999, he became Chief Scientific Officer, in which role he directs the company's research programs for new products and enhancements to current products. Since joining OptiMark Technologies, he has been heavily involved in management, strategic planning, and technical oversight of the development of advanced technologies for electronic trading, automated transaction implementation and control, and derivatives analysis. Dr. Rickard has a B.S. and M.S. in electrical engineering from the Florida Institute of Technology, and a Ph.D. in engineering physics from the University of California, San Diego. He also obtained Series 7 and 63 (General Securities Representative) and Series 24 (General Securities Principal) licenses in 1995, as part of his initiation into the securities business.

NICOLO G. TORRE is the Managing Director of Research at BARRA. He holds a Ph.D. in pure mathematics from the University of California, Berkeley, and is a Chartered Financial Analyst (CFA). At BARRA, he oversees the firm's worldwide research program. BARRA has models of more than forty equity and fixed-income security markets, and BARRA's models are used to manage funds totaling over \$12 trillion. Under Dr. Torre's leadership, the BARRA research program has emphasized economic fundamentals and insights over black-box modeling approaches. His personal research interests include modeling transaction costs, optimal control of portfolio trading, and strategic asset allocation.

ABSTRACT: In a securities market, the initiator of a large transaction can expect the realized price of his or her trade to be inferior to the current market price immediately prior to his appearance in the market. This “transaction implementation cost” phenomenon is a major concern of institutional money managers, both in portfolio selection and in trade implementation strategy. A considerable amount of current research in finance theory deals with modeling and prediction of these costs for equities trading, and commercial products and services recently have become available for probabilistically estimating real-time transaction implementation costs versus transaction size on a stock-specific basis.

Earlier papers described the concept of satisfaction- or preference-based trading, with optimization of trade matching on the basis of mutual preference. A market structure based on this design began trading listed equities on the Pacific Exchange on January 29, 1999 under the trade name OptiMark™. The Nasdaq market plans to begin trading using the OptiMark system later in 1999, followed by the Osaka Securities Exchange and the Toronto Stock Exchange in 2000. A prima-facie benefit of this approach is the ability to specify trading strategies that explicitly account for transaction implementation cost estimates as a function of the trade size.

In this paper, we present the underlying theoretical framework that unites the concepts of preference-based trading and probabilistic transaction cost estimation. In particular, we develop an analytical generalization of the current market structure constructs of market orders and limit orders. We describe a feasible optimization problem whose solution yields optimal preference profiles, given current market conditions (as reflected by the probability distribution of transaction implementation cost) and a trader-specified coefficient of urgency. This enables the seamless integration of the functions of portfolio selection (the purview of modern portfolio theory) and transaction implementation. We illustrate the application of this theory to a prototype trading workstation.

KEY WORDS AND PHRASES: electronic trading, fuzzy sets, preference-based trading, securities markets.

DURING THE DECADE OF THE 1990s, U.S. EQUITY MARKETS have experienced unparalleled growth, both in market capitalization and in the degree of participation by public investors via mutual funds, pension plans, and other institutionally managed funds. These funds typically invest in portfolios of equities as a means of diversifying the risks associated with individual equities. Index funds choose portfolios that approximate a surrogate for the market as a whole, such as the apportioned list of equities making up the S&P 500 index. Other funds choose portfolios from a more select universe of equities reflecting the particular investment style of the fund manager, such as sector or capitalization weighted funds.

The underlying impetus for portfolio-level investment strategies rests in the modern portfolio theory of Markowitz [5] and its extension via the Capital Asset Pricing Model (CAPM) of Sharpe [8]. Given a universe of N available equities with vector of expected returns $\overline{r}$ and covariance of returns R, Markowitz showed that the optimum portfolio distribution, which minimizes the variance of portfolio return for a given expected return $r_{p}$ (assuming $r_{p}$ is bounded between the minimum and maximum elements of $\overline{r}$ ) is:

$$
h = R ^ {- 1} \rho [ \rho^ {T} R ^ {- 1} \rho ] ^ {- 1} \left[ \begin{array}{c} r _ {p} \\ 1 \end{array} \right],\tag{1}
$$

where $\rho$ is the $N\times 2$ matrix,

$$
\rho = \left[ \begin{array}{c c} r _ {1} & 1 \\ \cdot & \cdot \\ \cdot & \cdot \\ \cdot & \cdot \\ r _ {N} & 1 \end{array} \right].\tag{2}
$$

This solution corresponds to the minimization of a quadratic form subject to linear equality constraints. Many investment managers today use commercially available portfolio optimizers of this type to select and update their investment portfolios. The output of a portfolio optimizer is a target distribution of equities that generally differs from the currently held portfolio, which results in a trade list for “rebalancing” the portfolio.

The expected return vector $\bar{r}$ in equation (1) should take account of the expected costs of implementing trade decisions, owing to the adverse price moves prompted by the presence of a large trader in the market. For institutional-size trades, these “implementation costs” may significantly alter the optimal portfolio composition and reduce the expected return. Depending on the specific equity, these costs typically average from several tens to a few hundred basis points on the value of the transaction [1] for the initiator of the trade. Software tools and real-time information services have recently become commercially available for explicitly estimating these costs on a stock-specific basis [4].

This paper presents a synthesis of the theory and use of such tools in the context of preference-based trading. This provides both an analytical and practical extension of the portfolio selection process to the trade implementation process, thereby making possible the seamless integration and automation of these domains. In the process it is demonstrated that a preference-based market structure analytically generalizes the more restrictive notions of limit and market orders, which have formed the historical basis for most market structures.

## Market Impact

EXISTING EQUITY MARKETS TYPICALLY PROVIDE A QUOTED BUYING AND SELLING price for a nominal volume of a security. A market order seeks immediate execution in the market at a stated volume. A small order typically will execute at the contra quoted price, or potentially in between the quoted prices. A large order, however, usually must pay a premium in order to secure prompt execution.

The implementation cost of a trade (not including the potential opportunity cost of unexecuted portions) can be defined as the difference between the realized transaction price and the midpoint $p_{0}$ of the quoted buy and sell price prior to the initiation of the trade. Econometric models, such as the BARRA Market Impact Model [4], provide a priori estimates of the probability distribution of this cost. Since the quoted buying and selling prices are known quantities, this cost estimate can be interpreted as the probability distribution of the transaction price. We denote this by $F(p|V)$ , the probability that an order of size V executes at price p.

The functional form of $F(p|V)$ for a small and large buyer-initiated trade is shown notionally in figure 1. Small orders typically execute within the bid-ask spread, so $F(p|V)$ has most of its support on this interval. For larger order sizes $V$ , the mean and variance of the execution price increase correspondingly, reflecting the premium exacted by the market for prompt execution of large orders and the additional uncertainty of the realized price. For a seller-initiated trade, a similar pattern will hold, with the inverted curve shifting to the left for large trades, reflecting the price concession demanded by the market. For small or large orders, more favorable prices typically result when a natural contra-side trader is present in the market.

![](/api/attachments/BHZQRYY4/fulltext/images/e6ec6ad87488921450d8ce1944194cf455c48ee45c3283efa2a3bac7afebc2dc.jpg)  
Figure 1. Probability Distribution of $F(p|V)$ for Relatively Small (Solid Line) and Large (Dashed Line) Trades

Investors may control market impact by employing limit orders rather than market orders, albeit at the cost of uncertain execution. A limit order is an offer to trade at a stated price, up to a maximum volume, valid until the order is canceled or modified. Thus, the investor controls the price, while the market determines how quickly the order fills and to what degree. The investor still incurs costs, only in this case they represent the lost opportunity cost associated with unfilled portions of the order and delay costs incurred by adverse price movement while the order is outstanding.

In truly efficient markets, the costs associated with these two order mechanisms will be equal, and so $F(p|V)$ may be suitably reinterpreted to cover the limit-order situation (i.e., p becomes the fixed quantity and V the variable quantity). For simplicity of discussion, however, we will generally focus on the market-order case (i.e., fixed V). This viewpoint reflects the typical institutional trading reality that a portfolio manager decides the total quantities he or she wants to trade and then tasks his or her trader with obtaining the best available execution. Thus, limit orders are primarily a tactical tool employed by a trader, rather than the expression of a fundamental objective.

## Preference and Probability in Trading

TRADING INVOLVES COMPOUND UNCERTAINTIES, PARTICULARLY FOR LARGE ORDERS. The first uncertainty is probabilistic in nature, that is, the likelihood of accomplishing a trade of a given price and size, as measured by $F(p|V)$ above. The second uncertainty relates to the desirability of accomplishing the same trade, which involves the expected economic value resulting from the trade.

As described in [7], a market participant's desire to trade at a particular price and size can be expressed as a fuzzy variable, denoted alternately as "preference" or "satisfaction." Using this construct, an optimal market mechanism can be implemented on the basis of the maximization of “mutual preference,” defined, for example, as the product of buyer and seller preferences. A “preference profile” represents a depiction of preference values $S(p|V)$ over a domain of price and size values. Like $F(p|V)$ , $S(p|V)$ assumes values between zero and unity.

Following Kosko [3], both the probability distribution $F(p|V)$ and the preference distribution $S(p|V)$ can be considered as fuzzy membership functions, the former of the trade $(p, V)$ in the set of possible trades, and the latter of the same trade in the set of preferable trades. Thus, the universe of discourse for a given size trade can be viewed as a two-dimensional unit square whose vertical and horizontal axes depict $F(p|V)$ and $S(p|V)$ , respectively. The discussion can be extended to include a third dimension representing the trade size variable V, but for now attention is restricted to the two dimensions of probability and preference for a particular size trade.

A limit order in this universe is a collection of fuzzy subsets represented by the points of a parametric curve with respect to price that traces between opposing segments of the vertical sides of the unit square, as shown in figure 2. Limit orders express unity preference to trade at prices equal to or better than their limit price. The latter price corresponds to a probability of trade that generally is less than unity, and beyond this price the preference to trade drops abruptly to zero (i.e., unwillingness to trade) even as the probability of accomplishing a trade increases.

A market order in this universe is represented by the fuzzy subset corresponding to the single point $(1,1)$ in the upper right corner of the unit square of figure 2. Market orders express unity preference to trade regardless of price and therefore have unity probability of trading.

Thus, the available expressions of trading interest within current markets are confined to restricted subsets of the universe of discourse, as illustrated in figure 2. However, the combination of the two functions $F(p|V)$ and $S(p|V)$ allows one parametrically to trace probability versus preference trajectories representing any particular collection of feasible fuzzy subsets within this universe. The feasibility restriction is the obvious one that $F(p|V)$ monotonically increases with decreasing values of $S(p|V)$ , that is, buyers (sellers) never have increasing preference for higher (lower) prices. Figure 3 illustrates some sample trajectories generated by particular combinations of $F(p|V)$ and $S(p|V)$ .

This demonstrates that a preference-based market structure provides an analytical generalization of one's ability to express trading desire over that available in market structures based on simple limit and market orders. We now proceed to exploit some of the analytical richness made possible by this more general structure.

## Fuzzy Set Principles

FUZZY SET THEORY PROVIDES A USEFUL MATHEMATICAL TOOL for mimicking human reasoning and has proven useful in numerous applications where rigorous analytical models would be intractable. A fuzzy subset A [9] is a generalization of the concept of an ordinary (crisp) subset that admits a degree of membership, as measured by a set membership function $m_{A}(x_{i})$ : $X \to [0,1]$ , with respect to each of the elements $x_{i}$ of the universe of discourse X.

![](/api/attachments/BHZQRYY4/fulltext/images/00dd72843ed980d26a42607e8345a6812fac1b25aeaf115faeb53512fc530fe7.jpg)  
Figure 2. Universe of Discourse for Trading, Illustrating a Limit Order (Solid Line) and a Market Order (Point) for a Particular Trade Size V

![](/api/attachments/BHZQRYY4/fulltext/images/a2ffb66466d84ee8b02fbb9819f68637c2921cdd0dc357719d0e5ce6d53ae1b2.jpg)  
Figure 3. Universe of Discourse for Trading, Illustrating Feasible Sample Trajectories for Preference Profiles

Fuzzy subsets can be represented as points in a unit hypercube [3] whose coordinates correspond to set membership values for each element of X. Thus, in figure 3, for example, any point on one of the parametric curves shown is a fuzzy subset of the (two-dimensional) set of probable and preferred trades. An entire curve is a collection of such fuzzy subsets. A market order is a fuzzy subset with set membership coordinates $\{1,1\}$ . A limit order is a collection of fuzzy subsets with coordinates $\{1,y\}$ , $0 \leq y \leq F(p_{L}|V)$ (where the limit price is $p_{L}$ ), and $\{0,y\}$ , $F(p_{L}|V) < y \leq 1$ .

A distance metric $l^{p}(A,B)$ between two fuzzy subsets can be constructed as a p-norm measure between their corresponding coordinates. For our purposes, the p = ∞ norm:

$$
l ^ {\infty} (A, B) = \max _ {i} | m _ {A} (x _ {i}) - m _ {B} (x _ {i}) |.\tag{3}
$$

yields the intuitively pleasing property that the distance between a limit order of a given price limit and a market order (with coordinates $\{1,1\}$ ) is simply one minus the probability of execution at the limit price. More generally, the distance between the point $\{1,1\}$ and any fuzzy subset A in probability/preference space is:

$$
l ^ {\infty} (X, A) = 1 - \min _ {i} m _ {A} \left(x _ {i}\right).\tag{4}
$$

## Analysis of Preference Profiles

IN THE UNIVERSE OF DISCOURSE FOR TRADING, REPRESENTED BY THE UNIT SQUARE in figures 2 and 3, we can use equation (4) to measure the distance between a market order, which has full membership in the set of probable and preferred trades, and any probability/preference point within the square. Figure 4 illustrates this concept for the point T lying on the preference contour $\Psi$ .

We define the mean “market order-ness” $\mu_{\Psi}$ of a given preference distribution S (p|V) in terms of a contour integral of the complementary distance from a market order over the corresponding contour $\Psi$ :

$$
\begin{array}{l} \mu_ {\Psi} = \frac {\int_ {\Psi} [ 1 - l ^ {\infty} (X , t (\psi)) ] d \psi}{\int_ {\Psi} d \psi} \\ = \frac {\int_ {p _ {1}} ^ {p _ {0}} [ 1 - l ^ {\infty} (X , T (\psi)) ] \frac {d \psi (p)}{d p} d p}{\int_ {p _ {1}} ^ {p _ {0}} \frac {d \psi (p)}{d p} d p} \end{array}\tag{5}
$$

The latter expression results from the change of integration variable to price, which parameterizes $\Psi$ . The limits $p_{1}$ and $p_{0}$ correspond to the unity and zero preference price bounds, respectively.

The contour $\Psi$ is defined over the interior of the unit square, except for the inclusion of the intersection point of the contour with the right-hand axis. Thus, in the degenerate case of a limit order, $\mu_{\Psi}$ is given by

$$
\mu_ {\Psi} = F _ {L} (p | V),\tag{6}
$$

since the numerator and denominator integrals in equation (5) collapse to a single point on the right-hand axis. Note that $\mu_{\Psi}$ approaches 1 as $p_{L}$ increases for a buyer, or as $p_{L}$ decreases for a seller.

![](/api/attachments/BHZQRYY4/fulltext/images/edcca22f5944fe841e0e2a61c7e471c687b3451b20752c11b0babe97b5fff825.jpg)  
Figure 4. $l^{\infty}(X,T)$ Measures the Proximity of a Single Probability/Preference Point $T$ to a Market Order

By increasing the price aggressiveness of a general preference distribution $S(p|V)$ that parametrically generates a contour $\Psi$ , we cause the latter to migrate toward the upper right corner in figure 4, thereby increasing its market order-ness.

## Optimal Synthesis of Preference Profiles

WE NOW FORMULATE AN APPROACH TO THE OPTIMIZATION OF PREFERENCE PROFILES. Equation (5) provides a measure of the average degree of membership of a given preference profile in the fuzzy set of probable and preferred trades. This measure can be made arbitrarily close to its maximum value of unity, for preference profiles with more aggressive prices that approach certainty of trading. To pose a proper optimization problem, we require a penalty function that reflects the economic penalty of a particular transaction price. There clearly are numerous choices of penalty functions that could be made. This section suggests a simple penalty function that has a direct, intuitive interpretation in terms of one's probabilistic assumptions regarding the future value of the stock at the end of the investment horizon, whatever its duration may be.

For institutional trading, the portfolio manager who orders a trade generally has an assumption regarding the future value of the stock to be traded. Indeed, the mean and covariance of expected returns for each stock are the parameters of this assumption used in equation (1) to solve for the optimum current portfolio. Let the current price (defined as the midpoint of the bid–ask spread) of a particular stock that is to be traded be $p_{0}$ , and assume a lognormal distribution $\Phi(p)$ of the future price. The parameters of this lognormal distribution are directly computable from the assumptions on the mean and variance of expected return and the current price $p_{0}$ .

We then define a penalty function $U(p)$ for a buyer with respect to the actual transaction price p as:

$$
U (p) = \left\{ \begin{array}{l l} \Phi (p), & p \leq p _ {1} \\ \Phi (p _ {1}) + (p - p _ {1}) \varphi (p _ {1}), & p > p _ {1} \end{array} , \right.\tag{7}
$$

where $\phi(p)$ is the corresponding probability density function of the lognormal distribution $\Phi(p)$ , and $p_{1}$ is the inflection point of this distribution. For $p \leq p_{1}$ , the lognormal distribution is convex, while for $p > p_{1}$ , we use the linear extrapolation from the inflection point along the line tangent to the distribution to complete the penalty function. The inflection point of $\Phi(p)$ is easily shown to be

$$
p _ {1} = \exp (\mu_ {p} - \sigma_ {p} ^ {2}),\tag{8}
$$

where $\mu_{p}$ and $\sigma_{p}$ are the conventionally defined logmean and logdeviation parameters of $\Phi(p)$ . As defined, the penalty function $U(p)$ is semi-risk averse, in the sense that

$$
\frac {d ^ {2} U (p)}{d p ^ {2}} \geq 0.
$$

The corresponding penalty function for a seller is simply the mirror image of $U(p)$ in equation (7) about $p_1$ :

$$
U (p) = \left\{ \begin{array}{l l} 1 - \Phi (p), & p > p _ {1} \\ \Phi (p _ {1}) - (p - p _ {1}) \varphi (p _ {1}), & p \leq p _ {1} \end{array} . \right.\tag{9}
$$

As illustrated in figure 5, $U(p)$ provides a direct probabilistic measure of the economic risk of a transaction at price $p$ , given one's expectations of future value for the security. For (buyer) transaction prices that are well below the range of future prices, the penalty function has essentially zero value, which implies that the buyer may pay these prices with relative confidence of a positive return. As the price begins to encroach upon the support range of future prices, the penalty function increases supralinearly up to the inflection point of $\Phi(p)$ , and then linearly beyond that point, assessing an increasing penalty for increasing prices.

The expected risk of transaction $v_{\Psi}$ averaged over a given preference distribution S (p|V) can be computed in terms of a contour integral over $\Psi$ , or equivalently over price, analogous to (5) above:

$$
\begin{array}{l} v _ {\Psi} = \frac {\int_ {\Psi} U (p (\psi)) d \psi}{\int_ {\Psi} d \psi} \\ = \frac {\int_ {p _ {1}} ^ {p _ {0}} U (p) \frac {d \psi (p)}{d p} d p}{\int_ {p _ {1}} ^ {p _ {0}} \frac {d \psi (p)}{d p} d p}. \end{array}\tag{10}
$$

![](/api/attachments/BHZQRYY4/fulltext/images/bdfab99b3914cd19bd6d5450706f17c0977af428e96054d3f7902efaee525ad0.jpg)  
Figure 5. Penalty Function $U(p)$ as Derived from the Cumulative Distribution Function $\Phi(p)$

Since the mean risk $v_{\psi}$ increases with more aggressive transaction prices, we can now pose the following optimal preference profile synthesis problem:

$$
\max _ {\Psi} \mu_ {\Psi} - \lambda   \nu_ {\Psi}  ,\tag{11}
$$

where $\lambda \geq 0$ is a coefficient that determines the relative urgency for execution of the preference profile. The smaller the value of $\lambda$ , the greater will be the “market order-ness” of the optimal profile resulting from the solution to (11), and the more likely will be the execution of all or part of the profile in a given match within the OptiMark system. Conversely, larger values of $\lambda$ will make the solution to (11) tend toward more conservatively priced profiles, which will have lower probabilities of execution.

The optimization problem in (11) can be solved numerically as described below. Other formulations of the penalty function $U(p)$ are clearly admissible as well and could be incorporated into optimization problems analogous to (11).

## Numerical Approach

A PREFERENCE CONTOUR IS GIVEN PARAMETRICALLY BY $\Psi(p|V)=[S(p|V),F(p|V)]$ . Since $F(p|V)$ is a known function, optimizing $\Psi(p|V)$ over (11) is equivalent to determining the $S(p|V)$ that optimizes (11). If we introduce g=dS/dp, then (11) can be rewritten as a function of g, that is,

$$
\rho (g) = \mu_ {\Psi} - \lambda v _ {\Psi},\tag{12}
$$

and the problem is to maximize $\rho(g)$ subject to the constraint $g \geq 0$ (for sells) or $g \leq 0$ (for buys). If price space is broken into finite intervals $[p_{i}, p_{i+1}]$ and g is taken to be piecewise constant with values $g_{i}$ on these intervals, then the problem reduces to maximizing $\rho(g_{1}, \ldots, g_{n})$ subject to the appropriate sign constraints on g.

This problem is solvable by a number of standard algorithms, such as the projective gradient method $[6]$ . As the fineness of the discretization of price space is increased, the solution of the discrete problem should approach the solution of the continuous problem. In practice, however, tradable prices constitute a discrete set, and so there is no need actually to carry the approximation to a continuous limit.

## Optimal Profile Examples

Figure 6 shows a screen copy of a prototype trading workstation that implements the optimal preference profile synthesis computations described above. The upper left window displays the probability distribution function estimated by the market impact model for different sizes of trades, ranging in this case from 1 million to 10 million shares (from left to right). The upper right window displays the cumulative distribution function of future price, along with the penalty function as derived above. (The “penalty parameter” slider in this window incorporates an additional parameter in the penalty function that is not used in the current work.) The lower left window contains a slider for the urgency parameter $\lambda$ , showing a setting of $\lambda = 0.1$ in this screen. Finally, the lower right window displays the optimal preference profile calculated from these inputs.

Note that in this case of small $\lambda$ , the optimal preference profile extends to the upper range of the market impact model distribution price support region for the corresponding size. For example, the zero preference contour is at a price of 75.5 for 10,000,000 shares. This reflects the fact that the optimization of (11) is placing a relatively greater weight on achieving a high probability of execution than on paying a higher price, within the range of active prices for this scenario. This will assure near certain execution if this volume of selling interest is present in the system, to the extent that the market impact model has predicted correctly the execution probabilities. The same effect is achieved for smaller volumes within the profile, all the way down to the very smallest volumes at the left edge of the profile. (We mention in passing that the matching rules within the OptiMark system may result in a better price to this buyer at any particular volume, depending on the availability and prices of sell profiles present in the system.)

![](/api/attachments/BHZQRYY4/fulltext/images/f32d6eb19c83e73ddae9bd1d8713a3f6033eb14c879ae69b7ff9098f8c563e24.jpg)  
Figure 6. Trader Workstation Screen Showing an Aggressively Priced Preference Profile, Corresponding to a High Degree of Urgency (i.e., Small λ Value)

Figure 7 shows the trader workstation screen with everything the same as in figure 6 except that the value of $\lambda$ has been increased to $\lambda = 2$ , which assigns a weighted penalty contribution greater than unity in (11) on prices that exceed approximately 74.5, where the value of $U(p)$ exceeds 0.5. Note that the highest price with nonzero preference in the corresponding optimal profile is now about 74.75, which is more conservative than the upper price limit in figure 6.

Finally, in figure 8, we show the more extreme case of $\lambda = 10$ , which assigns a high weighted penalty value to any price that encroaches significantly upon the support range of the future price distribution. The corresponding optimal preference profile is very conservatively priced and has a low probability of execution for all sizes.

These examples demonstrate the substantial range of variations embodied in optimal profiles for institutional-size trades, as a function of the relative urgency to complete the trade.

## Optimal Portfolio Selection/Implementation

THE ABOVE THEORY SUGGESTS THE INTEGRATION OF OPTIMAL PORTFOLIO SELECTION with optimal transaction implementation, in a system as depicted in figure 9.

A market-impact model is used in conjunction with a portfolio optimizer to select the list of securities to be traded. This list is input to an optimum profile synthesizer that solves the problem in (11), subject to the trader's urgency as specified by the value of $\lambda$ , yielding the optimum preference profile. This profile is then submitted to the OptiMark system described above for matching against other market participant's profiles.

As shown in the figure, one can incorporate a feedback optimal control loop whose input is the interim trade results from each OptiMark match, to adjust the value of $\lambda$ over time. If these trade results are falling behind the desired rate of trade execution, the value of $\lambda$ is reduced in order to increase the urgency of trading, and vice versa. In this manner, we can achieve a full “autopilot” capability for trade implementation. This will allow a trader to focus attention on the cognitive level of trade decision making as opposed to the frenetic, manually intensive pricing and entry of individual orders, each representing a small fraction of the total desired trading volume.

An additional benefit of this approach is the manner in which it explicitly imposes trading policy decisions (as embodied in the selection of the urgency parameter $\lambda$ ) upon pricing strategy. Currently, trading policy is expressed only implicitly through order pricing decisions. Separating trading policy from the details of trade implementation makes the issues of control and uniformity of trading performance much simpler to manage. These are important implications for supervisors of trading operations.

## Conclusion

THIS PAPER HAS PROVIDED A THEORETICAL FRAMEWORK FOR PREFERENCE-BASED trading in conjunction with probabilistic transaction-cost estimation. It has presented an analytical generalization of market orders and limit orders, which represent the only

![](/api/attachments/BHZQRYY4/fulltext/images/6432297598335c45bb2903947ee9f11b2610a65af6f3eee9e1578aad418d5075.jpg)  
Figure 7. Trader Workstation Screen Showing a Less Aggressively Priced Preference Profile, Corresponding to a Moderate Degree of Urgency (i.e., $\lambda = 2$ )

Figure 8. Trader Workstation Screen Showing a Conservatively Priced Preference Profile, Corresponding to a Very Low Degree of Urgency (i.e., $\lambda = 10$ )

![](/api/attachments/BHZQRYY4/fulltext/images/924bb1a77ae5ca189c0b64401c584e1ef48c0d28aae3b2dc620c13075939dadb.jpg)

![](/api/attachments/BHZQRYY4/fulltext/images/11d1727287e6e272a2feaa45d470660476084be75ff1f626f6361e7eaca5d6c4.jpg)  
Figure 9. Integrated Optimal Portfolio Selection and Transaction Implementation

currently available means of expressing trading desire in an electronic market and, further, has described a computable optimization problem whose solution yields optimal preference profiles, given current market conditions (as reflected by the probability distribution of transaction implementation cost), projections of future price for the security, and a trader-specified coefficient of urgency. This enables the seamless integration of the functions of portfolio selection and transaction implementation, thereby providing a mechanism for full automation of the investment process and substantial increase in trader productivity.

## REFERENCES

1. The Best of Plexus Commentaries. Santa Monica, CA: Plexus Group, 1997.

2. Clemons, E.K., and Weber, B.W. Restructuring institutional block trading: an overview of the OptiMark system. Journal of Management Information Systems, 15, 2 (Fall 1998), 41–60.

3. Kosko, B. Neural Networks and Fuzzy Systems, Englewood Cliffs, NJ: Prentice-Hall, 1992.

4. Market Impact Model Handbook. Berkeley, CA: BARRA Corp., 1997.

5. Markowitz, H.M. Portfolio selection. Journal of Finance, 7 (1952), 77–91.

6. Polak, E. Optimization: Algorithms and Consistent Approximations. New York: Springer Verlag, 1997.

7. Rickard, J.T., and Lupien, W.A. Optimal market structures based upon mutual satisfaction. Proceedings of the Thirtieth Asilomar Conference on Signals, Systems and Computers (November 1996).

8. Sharpe, W.F. Capital asset prices: a theory of market equilibrium under conditions of risk. Journal of Finance, 19 (September 1964), 425–442.

9. Zadeh, L.A. Fuzzy sets. Information and Control, 8 (1965), 338–353.
