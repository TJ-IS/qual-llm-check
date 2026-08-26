---
otero_id: 24831
otero_key: "9MYJ9YNW"
title: "A Note on Project Risk and Option Values of Investments in Information Technologies"
authors: "Ram L. Kumar"
year: "1996"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1996.11518118"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Note on Project Risk and Option Values of Investments in Information Technologies

Ram L. Kumar

To cite this article: Ram L. Kumar (1996) A Note on Project Risk and Option Values of Investments in Information Technologies, Journal of Management Information Systems, 13:1, 187-193, DOI: 10.1080/07421222.1996.11518118

To link to this article: https://doi.org/10.1080/07421222.1996.11518118

![](/api/attachments/9MYJ9YNW/fulltext/images/a6bd93b766f534c5391e3643a7ca14d22070e831b1742e66bf8fe70a7a2dede3.jpg)

Published online: 11 Dec 2015.

![](/api/attachments/9MYJ9YNW/fulltext/images/b70a1095a193ee6c7b16e1d4826451b4158b2358fd35642201a8e44ec2b21ef9.jpg)

Submit your article to this journal ↗

![](/api/attachments/9MYJ9YNW/fulltext/images/b5eba346bc66a8810edb914c1be29afdf41559591abbf404195511f7d1461c59.jpg)

View related articles ↗

![](/api/attachments/9MYJ9YNW/fulltext/images/8b5ad36d2aff23d007f2759c94ab29dd34b64f93480a71fd606aafd3d3bc23be.jpg)

Citing articles: 38 View citing articles ↗

# A Note on Project Risk and Option Values of Investments in Information Technologies

RAM L. KUMAR

RAM L. KUMAR is Assistant Professor in the Department of MIS and Operations at the Belk College of Business Administration, the University of North Carolina, Charlotte. He received his B.Tech. and Post Graduate Diploma in Management from the Indian Institute of Technology, Madras, and the Indian Institute of Management, Bangalore, respectively. He has worked for five years in information systems development and management. He received his Ph.D. from the University of Maryland in 1993, where he was the recipient of the Frank T. Paine Award for Academic Merit. His research has appeared or is forthcoming in Computers & Operations Research, International Journal of Production Economics, Journal of Management Information Systems, and several conference proceedings. His research interests include economics of investments in technology, security and control in information systems, and the interface between MIS and operations management. His research has been funded by organizations such as the U.S. Department of Commerce and the Maryland Industrial Partnerships Scheme.

ABSTRACT: Justification of investments in information technologies is an important research topic in the information systems area. Several approaches have been proposed. One of these highlights the deficiencies of traditional economic justification based on net present value, and proposes the use of techniques based on financial option pricing theory. This paper examines the relationship between project risk and option values of investments in new information technologies and illustrates how this relationship is significantly different from well-known results in the case of financial option pricing. Conditions for determining the desirability of risky projects are derived.

KEY WORDS AND PHRASES: information-system economics, information-technology investments, real options.

INVESTMENT JUSTIFICATION FOR INFORMATION TECHNOLOGIES IS A COMPLEX problem involving the use of several different types of analysis [2, 9]. Economic analysis is possibly one of the most important types of analysis that precedes an investment decision. Economic theory has been extensively applied in the study of information systems [1]. Traditional economic evaluation methods such as net present value often tend to undervalue investment decisions [6]. One of the major limitations of these techniques is that they do not capture management's ability to alter the pace of investment, or to stop investment at some point if conditions are unfavorable. Dos

Santos [4] provides an excellent discussion of the limitations of traditional economic analysis methods, and proposes a methodology based on options pricing theory. In particular, the idea of viewing information systems projects as options to exchange risky assets is presented. A method of valuing these options based on the research described in [7] is illustrated. The sensitivity of these option values to different parameters such as uncertainty of project costs and revenues and time to exercise the option are examined.

This paper presents a theoretical analysis of the variation of option values with project risk and a comparison with well-known results for financial options. We illustrate that option values could either increase or decrease with increase in project risk, depending on the relative values of variances of the rate of change of project costs and benefits, and the correlation between the values of project costs and benefits. In the case of financial options, option values increase with increased project risk. Numerical examples are presented to support the theoretical analysis.

## Summary of Related Research

SOME INVESTMENTS IN INFORMATION TECHNOLOGY CAN BE VIEWED as consisting of first-stage and second-stage investments. For example, a first-stage investment may be made in a telecommunications network, and a second-stage investment may be made in a technology that uses the network (e.g., a distributed database application). By undertaking the first-stage investment, the investor acquires a right (but not an obligation) to make a second-stage investment. This is analogous to investing in a financial option $[4]$ . From the options standpoint, the first-stage investment corresponds to the option price and the second-stage investment corresponds to the strike price of the option. However, the value of the second-stage investment is not known exactly at the time of first-stage investment (unlike the strike price) and is a stochastic variable. Hence, traditional financial option pricing models may not be directly applicable to investments in information technology. Dos Santos $[4]$ proposes the use of an option valuation method for exchanging risky assets developed in $[7]$ for this purpose. A first-stage investment provides an option to make a second-stage investment (whose exact value is unknown at the time of first-stage investment) in exchange for a completed project (whose value is not known exactly at the time of making the first-stage investment). Let V denote the value of an option to exchange an asset with an expected value of $C_{1}$ (expected investment in a second-stage project) for an asset with an expected return of $B_{1}$ (expected benefits from the second-stage project), with a time to expiration equal to t.

$$
\begin{array}{l l} V & = B _ {1} N (d _ {1}) - C _ {1} N (d _ {2}) \\ d _ {1} & = \frac {\ln (B _ {1} / C _ {1}) + \frac {1}{2} \sigma^ {2} t}{\sigma \sqrt {t}} \\ d _ {2} & = d _ {1} - \sigma \sqrt {t}. \end{array}\tag{1}
$$

$N(.)$ is the cumulative standard normal density function, and $\sigma^{2} = \sigma_{B1}^{2} + \sigma_{C1}^{2} - 2\sigma_{B1}$ , $\sigma_{C1} \rho_{BC}$ . $\sigma_{B1}$ and $\sigma$ denote the standard deviations of the rate of change of $B_{1}$ and $C_{1}$ , respectively (standard deviation of the percentage change in $B_{1}$ and $C_{1}$ over unit time) and $\rho_{BC}$ is the correlation coefficient between $B_{1}$ and $C_{1}$ . The terminology used is identical to that in [4] in order to facilitate comparison of results.

Prior research $[4]$ examines the pattern of variation of option values for different parameter values using an example. A major conclusion drawn from this analysis is that the option value of a project increases with increase in variance of the rate of change of project costs and/or benefits $[4, p. 85]$ . While this conclusion is valid for the data presented in $[4]$ , it is not generally true. The relationship between option value and project risk is explored in greater detail in the following sections.

## A Comparison of the Black–Scholes and Margrabe Models of Option Valuation

THE PRICING OF FINANCIAL OPTIONS IS BASED ON SEMINAL WORK by Black and Scholes [3], while the application of options theory to investments in information technology is based on the work of Margrabe [7]. The primary difference between these two models is the treatment of the cost of the second-stage project. In the Black–Scholes model, the cost of the second-stage project is deterministic and equal to the strike price of the financial option, while the Margrabe model treats it as a stochastic variable. The structure of the option valuation formulae for both models is very similar. The Black–Scholes formula can be viewed as a special case of the Margrabe model under the following conditions:

a. The variable $C_1$ is replaced by $K e^{-rt}$ . $K$ is the deterministic strike price of the option, $r$ is the risk-free interest rate, and $t$ is the time remaining until expiry of the option.

b. The instantaneous variance of $B_{1} / C_{1}$ ( $\sigma^2 = \sigma_{B1}^2 + \sigma_{C1}^2 - 2\sigma_{B1}\sigma_{C1}\rho_{BC}$ ) is equal to $\sigma_{B1}^2$ , since $\sigma_{C1}^2 = 0$ .

These conditions are recognized by Margrabe in [7]. For the Black–Scholes model, it is a well-known result that option values increase with increase in instantaneous variance of the value of the underlying security $(\sigma_{B1}^{2})$ . In other words, the partial derivative of option value with respect to $\sigma_{B1}^{2}$ is nonnegative $(\partial V/\partial\sigma_{B1}^{2}\geq0)$ . This result is formally shown in [8] and discussed in [3, 5]. However, $\partial V/\partial\sigma_{B1}^{2}$ can be negative in the Margrabe model, as illustrated by the following theorem:

Theorem 1: In the case of the Margrabe model, the sign of $\partial V / \partial \sigma_{B1}^2$ can be negative if the sign of $\sigma_{B1} - \rho_{BC}\sigma_{C1}$ is negative. Similarly, the sign of $\partial V / \partial \sigma_{C1}^2$ depends on the sign of $\sigma_{C1} - \rho_{BC}\sigma_{B1}$ .

Proof: A formal proof is provided in the appendix.

Table 1. Calculation of Option Values for $\rho_{BC}=0.2$ and $\sigma_{CI}=0.5$

<table><tr><td> $\sigma_{B1}$ </td><td>0</td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.7</td></tr><tr><td> $\sigma_{B1}^{2}$ </td><td>0</td><td>0.01</td><td>0.04</td><td>0.09</td><td>0.16</td><td>0.25</td><td>0.36</td><td>0.49</td></tr><tr><td> $\sigma^{2}$ </td><td>0.25</td><td>0.24</td><td>0.25</td><td>0.28</td><td>0.33</td><td>0.4</td><td>0.49</td><td>0.6</td></tr><tr><td>d1</td><td>0.82</td><td>0.83</td><td>0.82</td><td>0.81</td><td>0.79</td><td>0.77</td><td>0.76</td><td>0.76</td></tr><tr><td>d2</td><td>0.32</td><td>0.34</td><td>0.32</td><td>0.28</td><td>0.21</td><td>0.14</td><td>0.06</td><td>-0.02</td></tr><tr><td>N(d1)</td><td>0.7939</td><td>0.7967</td><td>0.7939</td><td>0.7910</td><td>0.7852</td><td>0.7794</td><td>0.7764</td><td>0.7764</td></tr><tr><td>N(d2)</td><td>0.6255</td><td>0.6331</td><td>0.6255</td><td>0.6103</td><td>0.5832</td><td>0.5557</td><td>0.5239</td><td>0.4920</td></tr><tr><td>V</td><td>6495</td><td>6437</td><td>6495</td><td>6665</td><td>6956</td><td>7252</td><td>7669</td><td>8148</td></tr><tr><td> $\sigma_{B1}-\rho_{BC}\sigma_{C1}$ </td><td>-0.1</td><td>0</td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td></tr></table>

## An Example

THIS SECTION PRESENTS NUMERICAL EXAMPLES THAT VALIDATE theorem 1 and illustrate the variation of option values as a function of project risk. Let $B_1 = \$20,000$ and $C_1 = \$15,000$ . For the data shown in Tables 1–3, the option values (in thousands of dollars) decrease and then increase again as the variance of the rate of change of project benefits ( $\sigma_{B1}^2$ ) changes. The pattern of variation would be identical if the value of project costs and benefits were interchanged. In each table, the values close to the point of inflection of option values are highlighted. Values of $\sigma_{B1} - \rho_{BC} \sigma_{C1}$ are shown in the last row of each table. Table 1 involves a low correlation between benefits and costs, and a moderate variance of rate of change of costs. The inflection point occurs at a low variance of rate of change of project benefits ( $\sigma_{B1}^2 = 0.01$ ), and corresponds to $\sigma_{B1} - \rho_{BC} \sigma_{C1} = 0$ .

Table 2 represents a scenario with moderate correlation between costs and benefits of the second-stage project. The option value decreases to 6162 and then increases as $\sigma_{B1}^{2}$ increases. The inflection point is likely to be less than 6162. It occurs at a higher variance of rate of change of project benefits than Table 1 ( $\sigma_{B1}^{2}$ is between 0.04 and 0.09), and corresponds to $\sigma_{B1}-\rho_{BC}\sigma_{C1}=0$ .

Table 3 represents a situation with a high correlation between costs and benefits of the second-stage project. The option value drops from 6495 to 5465 and then increases as $\sigma_{B1}^{2}$ increases. The inflection point occurs at a higher variance of rate of change of project benefits ( $\sigma_{B1}^{2}=0.16$ ) than the previous two cases and corresponds to $\sigma_{B1}-\rho_{BC}\sigma_{C1}=0$ .

Figure 1 presents the results of Tables 1–3 graphically. The pattern of variation of option values as a function variance of rate of change of project benefits, and the inflection points are presented visually.

This pattern of variation can be explained by the fact that instantaneous variance of the ratio $B_{1}/C_{1}(\sigma^{2})$ could decrease with an increase in variance of the rate of change of costs or benefits of the second-stage projects under conditions described by theorem 1. The probability of revenues increasing by a large amount relative to costs and thus making a project profitable depend on the interrelationship between the values of $\sigma_{B1}$ , $\sigma_{C1}$ , and $\rho_{BC}$ . It is thus not always necessary for a firm investing in a first-stage project to prefer larger $\sigma_{B1}$ or $\sigma_{C1}$ for a second-stage project.

Table 2. Calculation of Option Values for $\rho_{BC} = 0.5$ and $\sigma_{CI} = 0.5$

<table><tr><td> $\sigma_{B1}$ </td><td>0</td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.7</td></tr><tr><td> $\sigma_{B1}^{2}$ </td><td>0</td><td>0.01</td><td>0.04</td><td>0.09</td><td>0.16</td><td>0.25</td><td>0.36</td><td>0.49</td></tr><tr><td> $\sigma^{2}$ </td><td>0.25</td><td>0.21</td><td>0.19</td><td>0.19</td><td>0.21</td><td>0.25</td><td>0.31</td><td>0.39</td></tr><tr><td>d1</td><td>0.82</td><td>0.86</td><td>0.88</td><td>0.88</td><td>0.86</td><td>0.82</td><td>0.80</td><td>0.77</td></tr><tr><td>d2</td><td>0.32</td><td>0.40</td><td>0.44</td><td>0.44</td><td>0.40</td><td>0.32</td><td>0.24</td><td>0.15</td></tr><tr><td>N(d1)</td><td>0.7939</td><td>0.8051</td><td>0.8106</td><td>0.8106</td><td>0.8051</td><td>0.7939</td><td>0.7881</td><td>0.7794</td></tr><tr><td>N(d2)</td><td>0.6255</td><td>0.6554</td><td>0.6700</td><td>0.6700</td><td>0.6554</td><td>0.6255</td><td>0.5948</td><td>0.5596</td></tr><tr><td>V</td><td>6495</td><td>6271</td><td>6162</td><td>6162</td><td>6271</td><td>6495</td><td>6840</td><td>7194</td></tr><tr><td> $\sigma_{B1}-\rho BC \sigma_{C1}$ </td><td>-0.25</td><td>-0.15</td><td>-0.05</td><td>0.05</td><td>0.15</td><td>0.25</td><td>0.35</td><td>0.45</td></tr></table>

Table 3. Calculation of Option Values for $\rho_{BC} = 0.8$ and $\sigma_{CI} = 0.5$

<table><tr><td> $\sigma_{B1}$ </td><td>0</td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.7</td></tr><tr><td> $\sigma_{B1}^{2}$ </td><td>0</td><td>0.01</td><td>0.04</td><td>0.09</td><td>0.16</td><td>0.25</td><td>0.36</td><td>0.49</td></tr><tr><td> $\sigma^{2}$ </td><td>0.25</td><td>0.18</td><td>0.13</td><td>0.10</td><td>0.09</td><td>0.10</td><td>0.13</td><td>0.18</td></tr><tr><td>d1</td><td>0.82</td><td>0.89</td><td>0.98</td><td>1.07</td><td>1.11</td><td>1.07</td><td>0.98</td><td>0.89</td></tr><tr><td>d2</td><td>0.32</td><td>0.47</td><td>0.62</td><td>0.75</td><td>0.81</td><td>0.75</td><td>0.62</td><td>0.47</td></tr><tr><td>N(d1)</td><td>0.7939</td><td>0.8133</td><td>0.8365</td><td>0.8577</td><td>0.8665</td><td>0.8577</td><td>0.8365</td><td>0.8133</td></tr><tr><td>N(d2)</td><td>0.6255</td><td>0.6808</td><td>0.7324</td><td>0.7734</td><td>0.7910</td><td>0.7734</td><td>0.7324</td><td>0.6808</td></tr><tr><td>V</td><td>6495</td><td>6054</td><td>5744</td><td>5553</td><td>5465</td><td>5553</td><td>5744</td><td>6054</td></tr><tr><td> $\sigma_{B1}-\rho_{BC}\sigma_{C1}$ </td><td>-0.4</td><td>-0.3</td><td>-0.2</td><td>-0.1</td><td>0</td><td>0.1</td><td>0.2</td><td>0.3</td></tr></table>

## Conclusion

THE PATTERN OF VARIATION OF OPTION VALUES AS A FUNCTION of variance of rate of change of second-stage project costs or benefits differs from well-known results in financial option theory. Changes in option values in relation to changes in project risk depend on the relative values of $\sigma_{B1}$ , $\sigma_{C1}$ , and $\rho_{BC}$ . In particular, this paper has shown that option values of second-stage projects could increase or decrease with an increase in variance of rate of change of project benefits, depending on the sign of $\sigma_{B1} - \rho_{BC} \sigma_{C1}$ . Similarly, option values of second-stage projects could increase or decrease with the variance of rate of change of second-stage project costs depending on the value of $\sigma_{C1} - \rho_{BC} \sigma_{B1}$ .

![](/api/attachments/9MYJ9YNW/fulltext/images/b50bb61bff66ef1516da6b881baea203c3810b5e0ca834e54c6f2a58056cded4.jpg)  
Figure 1. Option Values and Project Risk

The managerial implication of this result is that it is not always attractive (in terms of option values) to select riskier second-stage projects, as implied by earlier research. Researchers and practitioners interested in applying option valuation techniques to evaluate information technology investments would benefit from examining if riskier projects increase or decrease option values for a particular decision scenario, using the results derived in this paper. This can be done by calculating the value of $\sigma_{B1} - \rho_{BC} \sigma_{C1}$ or $\sigma_{C1} - \rho_{BC} \sigma_{B1}$ for different decision scenarios.

## REFERENCES

1. Bakos, J.Y., and Kemerer, C.F. Recent applications of economic theory in information technology research. Decision Support Systems, 8, 3 (September 1992), 365–386.

2. Berger, P.; Kobielus, J.G.; and Sutherland, D.E., eds. Measuring the Business Value of Information Technologies. Washington, DC: ICIT Press, 1988.

3. Black, F., and Scholes, M. The pricing of options and corporate liabilities. Journal of Political Economy, 81 (1937), 637–659.

4. Dos Santos, B.L. Justifying investments in new information technologies. Journal of Management Information Systems, 7, 4 (Spring 1991), 71–90.

5. Edwards, F.R., and Ma, C.W. Futures and Options. New York: McGraw-Hill, 1992.

6. Kaplan, R.S. Must CIM be justified by faith alone? Harvard Business Review, 64, 2 (March–April 1986), 87–97.

7. Margrabe, W. The value of an option to exchange one asset for another. Journal of Finance, 33, 1 (March 1978), 177–186.

8. Merton, R.C. Theory of rational option pricing. Bell Journal of Economics and Management Science, 4 (1973), 141–183.

9. Powell, P. Information technology evaluation: is it different? Journal of the Operational Research Society, 43, 1 (1992), 29–43.

## APPENDIX: Proof of Theorem 1

In the Black–Scholes model, $\partial V/\partial\sigma_{B1}^{2}=\partial V/\partial\sigma^{2}=\partial V/\partial\sigma^{2}\left(\geq0\right)$ [8], since $\sigma^{2}=\sigma_{B1}^{2}$ . Substituting $K e^{-rt}=C_{1}$ in the Black–Scholes model to get the Margrabe model does not change the sign of $\partial V/\partial\sigma^{2}$ since we are replacing one positive quantity with another. Also, in the Margrabe model, $\partial V/\partial\sigma_{B1}^{2}$ is not equal to $\partial V/\partial\sigma^{2}$ since $\sigma^{2}=\sigma_{B1}^{2}+\sigma_{C1}^{2}-2\sigma_{B1}\sigma_{C1}\rho_{BC}$ , and $\sigma_{C1}^{2}$ is not equal to 0. Using the chain rule of differentiation, $\partial V/\partial\sigma_{B1}^{2}=\partial V/\partial\sigma^{2}*\partial\sigma^{2}/\partial\sigma_{B1}^{2}$ . Since $\partial V/\partial\sigma^{2}$ is nonnegative, the sign of $\partial V/\partial\sigma_{B1}^{2}$ can be negative if $\partial\sigma^{2}/\partial\sigma_{B1}^{2}$ is negative.

$$
\begin{array}{r l} \partial \sigma^ {2} / \partial \sigma_ {B 1} ^ {2} & = \partial / \partial \sigma_ {B 1} ^ {2} (\sigma_ {B 1} ^ {2} + \sigma_ {C 1} ^ {2} - 2 \rho_ {B C} \sigma_ {B 1} \sigma_ {C 1} \\ & = 1 - 2 \rho_ {B C} \sigma_ {C _ {1}} \left[ \frac {\partial}{\sigma_ {B 1}} ^ {2} (\sigma_ {B 1}) \right] \\ & = 1 - \rho_ {B C} \sigma_ {C _ {1}} / \sigma_ {B 1} \end{array}
$$

$$
\partial \sigma^ {2} / \partial \sigma_ {B 1} ^ {2} = 0 \text {   when   } 1 - \rho_ {B C} \sigma_ {C _ {1}} / \sigma_ {B 1} = 0, \text {   or   when   }\tag{2a}
$$

$$
\sigma_ {B 1} - \rho_ {B C} \sigma_ {C _ {1}} = 0.
$$

$$
\partial \sigma^ {2} / \partial \sigma_ {B 1} ^ {2} > 0 \text {   when   } 1 - \rho_ {B C} \sigma_ {C 1} / \sigma_ {B 1} > 0, \text {   or   when   }\tag{2b}
$$

$$
\sigma_ {B 1} - \rho_ {B C} \sigma_ {C 1} > 0.
$$

$$
\partial \sigma^ {2} / \partial \sigma_ {B 1} ^ {2} <   0 \text {   when   } 1 - \rho_ {B C} \sigma_ {C 1} / \sigma_ {B 1} <   0, \text {   or   when   }\tag{2c}
$$

$$
\sigma_ {B 1} - \rho_ {B C} \sigma_ {C 1} <   0.
$$

Thus, the sign of $\partial \sigma^2 / \partial \sigma_{B1}^2$ and therefore the sign of $\partial V / \partial \sigma_{B1}^2$ can be negative if the sign of the expression $\sigma_{B1} - \rho_{BC} \sigma_{C1}$ is negative, and will depend on the values of $\rho_{BC}, \sigma_{B1}$ , and $\sigma_{C1}$ . Similarly, it is possible to demonstrate that the sign of $\partial V / \partial \sigma_{C1}^2$ will depend on the sign of $\sigma_{C1} - \rho_{BC} \sigma_{B1}$ .
