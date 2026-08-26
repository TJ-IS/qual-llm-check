---
otero_id: 25350
otero_key: "KR4WD4F9"
title: "Prioritizing a Portfolio of Information Technology Investment Projects"
authors: "INDRANIL BARDHAN; RYAN SOUGSTAD"
year: "2004"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2004.11045803"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/KR4WD4F9/fulltext/images/75d9eedd5561cf84a865d3d50503325859fba081b18d67130d61fea512611278.jpg)

# Journal of Management Information Systems

Publication details, including instructions for authors and subscription information: http://www.tandfonline.com/loi/mmis20

# Prioritizing a Portfolio of Information Technology Investment Projects

INDRANIL BARDHAN <sup>a</sup> , RYAN SOUGSTAD <sup>a</sup> & RYAN SOUGSTAD

<sup>a</sup> University of Texas at Dallas

<sup>b</sup> IBM Thomas J. Watson Research Center in Yorktown Heights, New York Published online: 08 Dec 2014.

To cite this article: INDRANIL BARDHAN , RYAN SOUGSTAD & RYAN SOUGSTAD (2004) Prioritizing a Portfolio of Information Technology Investment Projects, Journal of Management Information Systems, 21:2, 33-60

To link to this article: http://dx.doi.org/10.1080/07421222.2004.11045803

## PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the “Content”) contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms & Conditions of access and use can be found at http:// www.tandfonline.com/page/terms-and-conditions

# Prioritizing a Portfolio of Information Technology Investment Projects

INDRANIL BARDHAN, SUGATO BAGCHI, AND RYAN SOUGSTAD

INDRANIL R. BARDHAN is an Assistant Professor of Management Information Systems and Accounting and Information Management at the University of Texas at Dallas. He is also the Director of the Center for Practice and Research in Software Management (PRISM). His research interests are in the areas of information technology valuation, business impact of information systems on supply chain and firm performance, and software development. His research has been published in leading journals including Operations Research, Journal of Management Information Systems, European Journal of Operational Research, Annals of Operations Research, Journal of Productivity Analysis, and Journal of the Operations Research Society of Japan. He has ten years of management consulting experience and has advised Fortune 500 executives on information technology strategy and systems implementation.

SUGATO BAGCHI is a Research Staff Member at the IBM Thomas J. Watson Research Center in Yorktown Heights, New York. His current research interest is in valuation of information technology applications and infrastructure. He is currently working on the development and application of tools and techniques to help potential adopters of emerging technologies quantify the predicted benefits in terms of financial impact. Previously, he worked on knowledge representation frameworks and methodologies for business strategy formulation and on the design and implementation of a business process modeling and simulation tool for multi-enterprise supply chains. He holds a Ph.D. in Computer Science from Vanderbilt University.

RYAN SOUGSTAD has seven years of experience in client sales and marketing with the IBM Corporation. He holds an MBA from the University of Texas at Dallas. His research interests center on information technology valuation and portfolio management. He has taught at the National American University in Rapid City, South Dakota, and is currently a doctoral student in Information Systems in the Carlson School of Management at the University of Minnesota

ABSTRACT: Although the use of real options for valuation of information technology (IT) investments has been documented, little research has been conducted to examine its relevance for valuing and prioritizing a portfolio of projects. Complexities of IT projects along with the effect of project interdependencies raise several challenges in applying real options for prioritization of IT investments. We examine a large U.S.- based energy utility firm in a deregulated environment that is considering investment in a portfolio of 31 projects to provide a range of Internet-enabled energy services to customers. Using real data on expected project benefits and costs for different competitive scenarios, we develop a nested options model that extends prior research by incorporating the impact of project interdependencies to calculate the option value of all projects. Our nested options model provides a better understanding of project interdependencies on valuation and prioritization decisions, and provides insights into the business value of IT infrastructure projects that provide the managerial flexibility to launch future projects. We present a real options portfolio optimization algorithm for dynamic multiperiod portfolio optimization by incorporating the project values based on real options analysis in a portfolio management model with budget constraints.

KEY WORDS AND PHRASES: business value, information technology, investment evaluation, net present value, portfolio optimization, real options analysis, sequential investment.

THE VALUATION OF INFORMATION TECHNOLOGY (IT) investments is challenging because it is characterized by long payback periods, uncertainty, and changing business conditions. Corporate capital budgeting methods typically use accounting-based criteria such as return on investment (ROI), internal rate of return (IRR), and payback period, which were designed for projects with no option features. The uncertainties underlying IT investment decisions and the inability of discounted cash flow (DCF) analyses to incorporate the impact of flexibility force executives to rely on gut instinct when finalizing IT investment decisions. In a study of 130 chief information officers (CIOs) of large companies, conducted by the Kellogg School of Management in collaboration with the Society for Information Management and consulting firm DiamondCluster International, 80 percent of respondents expressed significant difficulty in tracking the value of IT investments and a majority indicated that they did not have a process to prioritize project funding requests and coordinate funding decisions [7].

Traditional finance theory suggests that firms should use a DCF approach to analyze capital allocation requests. Estimated cash flows from an investment are discounted to their present value at a discount rate commensurate with the project risk. This approach does not properly account for the flexibility inherent in most IT investment decisions. For example, an IT infrastructure project may have a negative net present value (NPV) when evaluated on a stand-alone basis, but provide the option to launch future value-added services for application development or customer interaction [12, 27]. Unless the option value of this flexibility is taken into consideration, companies will not be able to justify strategic investments in IT that provide an accurate representation of strategic business value.

Real options analysis presents an attractive alternative because it explicitly accounts for the value of future flexibility in management decision-making [1, 29, 34]. This paper deals with the application of a nested real options model to value and prioritize a portfolio of IT projects. We illustrate this approach using a real-world case study of a large utility facing challenges due to uncertainties surrounding energy deregulation and introduction of Internet-enabled energy services. A portfolio of 31 IT investment projects was identified as a set of potential investment opportunities. Based on the IT capabilities required for each project, we develop a nested options model that models project interdependencies as real options. The model provides a better understanding of the dependencies and sequencing constraints typically associated with IT projects, and enables these projects to be valued and prioritized more accurately.

Early portfolio management tools included scoring and sorting models based on methods that maximized portfolio value through financial or nonfinancial measures. For instance, Hoechst uses a nonfinancial scoring model where projects are rated based on five criteria: probability of technical success, commercial success, reward, business strategy fit, and strategic leverage [11]. Groenveld [17] describes a tool that maps precedence relationships between projects and links projects to the strategic objectives of the firm based on a precedence network approach. Weill and Broadbent [37] describe a portfolio pyramid framework where the IT investment portfolio is categorized into four types of asset classes based on their primary business role: infrastructure, transactional, informational, and strategic asset classes. However, their method does not allow valuation of projects based on financial cash flow projections or prioritization based on flexibility, sequencing, and budget constraints. Similarly, other project management tools such as the Portfolio Dashboard [13] allow managers to view projects prioritized by portfolio category and enable monitoring of project status, but do not support project valuation based on the flexibility inherent in project investment decisions [23, 36].

Our main contribution is the development of a nested real options model that provides an approach to incorporate project interdependencies for project valuation and prioritization. Whereas other studies in the information systems (IS) literature use real options to make go or no-go decisions based on valuation of a single project and ignore the effect of project interdependencies, our model accounts for the complexities inherent in prioritizing a portfolio of projects while considering the impact of project interdependencies on value. We develop a real options portfolio optimization algorithm to apply the real options results in a prioritization framework, where project funding decisions are made in each period and their impact on the overall portfolio value is updated dynamically. In this manner, we link the use of real options valuation to portfolio management and provide a model to apply real options analysis for project prioritization and budgeting.

## Problem Background

THIS SECTION DEALS WITH THE VALUATION of a portfolio of 31 e-business projects for an energy company, which we refer to as EnergyCo to protect its identity and its projects. In the late 1990s, EnergyCo was facing challenges on several fronts. Energy deregulation was being phased in, and while it posed a potential threat of eroding existing customers, it also provided an opportunity for EnergyCo to offer energy services in more creative ways to existing customers and attract new out-of-state customers. The second challenge was to understand the strategic significance of the Internet as it applied to deregulation of the energy industry and identify how e-business could transform their relationships with customers, suppliers, and partners.

To address these challenges, EnergyCo identified a portfolio of e-business opportunities that promised business value in a set of feasible business scenarios that might unfold in the future. These opportunities were then further detailed and developed into e-business projects to be considered for funding. Appendix A provides a brief description of the project portfolio.

## Impact of Project Interdependencies

An important feature of many IT projects is their interdependencies. An IT infrastructure, which by itself might not create much value, might enable another project, and completion of both may yield significant value. Therefore, the infrastructure project deserves partial credit for future benefits that it enables. Similarly, some projects are broken into phases, with funding considered at each phase. One phase might not appear attractive on its own, but it might enable a later phase that facilitates completion of the entire project.

Most managers realize that IT projects provide leverage to launch future valueadded services and take them into consideration when evaluating technology decisions. This works well when there are few options to consider. However, when dozens of projects with complex interdependencies are considered, this decision is not as clear and the risks to making suboptimal decisions are high. Hence, identification of the interdependencies between projects must be undertaken in a consistent and repeatable manner that scales well with the number of projects.

Based on a thorough understanding of EnergyCo’s business model, project interdependencies were identified as shown in Figure 1. Hard dependencies between two projects exist when a capability developed for one project is also required by one or more of the other project(s). Soft dependencies exist when a capability from one project supports or enhances capabilities required by other projects. For instance, if the Integrated Billing project was not funded, management determined that the business benefit of the Total Home Bundle project would be reduced by 25 percent, since its full functionality would not be available.

Based on the structure of project interdependencies and discussions with EnergyCo managers, the project portfolio was grouped into three phases. Phase I projects represent projects that put EnergyCo at parity with competitors, do not have any prerequisites, or may serve as building blocks for future projects. Phase II projects involve significant make/buy/partner decisions or depend on capabilities deployed in Phase I. Phase III projects are dependent on capabilities deployed in Phase I or II projects.

## Estimation of Project Benefits

We used a value net approach [6] to estimate project benefits based on interactions between EnergyCo, its customers, and its partners. A value net is a map that links a firm to various player segments: customers, competitors, suppliers, and complementors/ partners who increase the value of a company’s services to its customers. It provides an understanding of the company’s ecosystem and the relative strength of the company. This was a useful starting point for EnergyCo, because impending energy deregulation was about to change its traditional market. Each project was evaluated to identify the benefits it offered to the players in the value net and its value to the firm, which were quantified using financial metrics.

![](/api/attachments/KR4WD4F9/fulltext/images/4adfdaad985cff614d5e73b7fb78ef22de1ed0154f3266a70d9fda0e04e86c49.jpg)  
Figure 1. Project Interdependencies Between EnergyCo E-Business Projects

A range of scenarios that characterized the uncertainty of customer acceptance and competitive reaction to new services was developed through scenario analysis [9, 35]. In addition to a base-case or most-likely scenario, worst-case and best-case scenarios were generated. Scenarios were weighted by their likelihood to produce an expected cash flow. Each scenario represents different risk levels associated with projects and adoption of technology services, and provides an understanding of the variations in cash flow due to uncertainty.

We use the E-billing/Payment project to illustrate the benefit estimation process. In addition to supporting electronic billing, the service was intended to provide other sources of value, such as forecasts of future energy usage, comparison of energy usage with aggregated peer benchmarks, cost savings suggestions, and usage data normalized for weather. Based on these value propositions, the sources of business value were identified to be cost reduction for bill presentment and payment processes, and increased customer loyalty in a deregulated environment. Cost reduction was quantified by listing and estimating the per-bill costs for bill printing, bill handling and mailing, billing customer service, postage, payment handling, and data entry costs of manual payments.

The conservative scenario assumed zero competition in a regulated environment and, therefore, no benefit would be realized from increasing the loyalty of a captive customer base. The aggressive scenario assumed competition, similar to the long-distance telephone business in the late 1990s, for which data was available to estimate the value of customer loyalty. In a manner similar to Clemons and Gu [10], who developed a framework for valuation of a contingent IT investment based on game-theoretic analysis of the behavior of competitors and their customers, we estimated project benefits based on a high-level analyses of expected customer demand and competitive conditions.

## Estimation of Project Variance

Real options thinking emphasizes the sources of uncertainty inherent in IT investments [18]. These risks include firm-specific risks, competition risks, market risks, and environmental and technological risks [3, 25]. Firm-specific risks are determined by endogenous factors such as a firm’s ability to align its IT project portfolio to business strategy and the skill level of its IT staff [8]. Competition risks include risks posed by competitors who may make preemptive moves to capture market share or make similar investments that may dilute the value of a firm’s current IT project portfolio [38]. Market risks include uncertainty about customer demand for services that are enabled by a firm’s IT projects [12]. These risks impact the firm’s ability to obtain the expected benefits from its IT investments and cause fluctuations in expected customer demand.

Dos Santos [15] and Keen [19] advocate an approach to estimate project volatility based on historical data on project returns of similar projects. However, such approaches are not applicable in our context, since these projects represent new ones in an uncertain deregulated environment with no historical data. We develop a methodology to estimate the volatility of project returns based on the three scenarios of expected project benefits as follows:

• Step 1 (Calculation of Project-Specific Spread): We calculate the project-specific spread as the sum of spreads for the moderate-conservative and moderateaggressive scenarios for each project. The greater the spread, as a percentage of benefits, the greater the project volatility. Calculate the mean and standard deviation of the overall project portfolio spread.

• Step 2 (Estimation of Portfolio Volatility): We assign an overall volatility estimate to the aggregated project portfolio. This estimate represents the overall volatility of the entire portfolio of e-business projects and is easier for management to estimate compared to estimation of the volatility of individual projects. – Step 2a (Baseline Volatility Determination): Based on the characteristics of the project portfolio, including perceived market and technological risks, we assign a baseline volatility estimate (σ<sup>2</sup>) of 15 percent to the project portfolio.<sup>1</sup> – Step 2b (Standard Deviation of Portfolio Volatility): Calculate the standard deviation of the baseline portfolio volatility.

• Step 3 (Baseline Volatility Adjustment): Calculate the volatility associated with a project j (σ <sup>2</sup>) by adjusting the baseline volatility estimate by a value equal to the number of standard deviations (n ) of project j’s spread from the mean portfolio spread.

An example of the volatility calculation for the Total Home Bundle project is described in Appendix B along with the key assumptions of our approach to estimate project variance. Appendix C provides a glossary of the technical terms used in this paper.

## Real Options for Information Technology Investment Valuation

AN OPTION GIVES THE HOLDER THE RIGHT, but not the obligation, to take ownership of an underlying asset in the future. If future events remove or otherwise reduce the sources of uncertainty to some satisfactory level, the firm may exercise its option and proceed with a full-blown implementation [14]. If, however, the uncertainty continues or is not adequately resolved, the expiration period can be extended or the option may simply be allowed to lapse, thus limiting any downside exposure to future losses [30]. IT investments provide the flexibility to expand, launch other applications, or standardize across different platforms [12, 20]. Dos Santos [15] showed that real options are useful to justify IT investments in the context of Integrated Services Digital Network (ISDN) services. Prior research has shown that software platforms may not generate value directly, but enable other value-added applications [16, 31]. IT infrastructure projects may involve a “wait-and-see” component that gives IT managers the option to defer decisions until some uncertainty is resolved [4, 5, 26]. Clemons and Gu [10] showed that IT benefits include flexibility and responsiveness, both of which can be evaluated with real options.

Prior research on real options for justifying IT investments has focused on valuation decisions for a single project or megaproject. For instance, Taudes et al. [32] use an options model to quantify the benefits of switching from SAP R/2 to SAP R/3. Similarly, Schwartz and Zozaya-Gorostiza [28] develop options that consider the effect of uncertainty in costs and benefits associated with IT investment opportunities, using data on the deployment of point-of-sale debit services as reported in Benaroch and Kauffman [5]. However, these studies do not provide insight into how real options can be used to evaluate a portfolio of projects that are typically characterized by interdependencies and sequencing constraints.

Since our project portfolio involves IT investments that embed simple options, our use of the Margrabe options model to determine the value of an option to exchange risky development costs for risky revenues is valid [22]. The use of real options for valuing nontraded assets such as IT projects is justified, since a firm seeking to maximize its shareholder value may use risk-free discount rates to evaluate real options [3]. Second, discounting the value of a real option by the risk-adjusted rate, which represents the risk specific to a project, lowers the option value only marginally [3, 5]. Hence, the real option value of a project (V ) is calculated as

$$
V _ {j} = B _ {j} N \left(d _ {1 j}\right) - C _ {j} e ^ {- r _ {f} t} N \left(d _ {2 j}\right),\tag{1}
$$

where $d _ { 1 j } = [ \ln ( B _ { j } / C _ { j } ) + ( r _ { f } t + \sigma _ { j } ^ { 2 } t / 2 ) ] / \sigma _ { j } \sqrt { t }$ , and $d _ { 2 j } = d _ { 1 j } - \sigma _ { j } \sqrt { t }$ , and $B _ { j } = P V ( c f _ { j } ^ { * } ( 1 -$ $\Sigma _ { k ^ { \mathrm { } } } s _ { k j } ) ,$ ). Table 1 provides definitions of the variables described in our model.

Table 1. Notations Used in the Real Options Model

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $V_{j}$ </td><td>Option value of project  $j$ .</td></tr><tr><td> $B_{j}$ </td><td>Present value of expected benefits (returns) of project  $j$ .</td></tr><tr><td> $C_{j}$ </td><td>Present value of the expected costs of project  $j$ .</td></tr><tr><td> $N(\cdot)$ </td><td>Cumulative standard normal probability density function.</td></tr><tr><td> $\sigma_{j}^{2}$ </td><td>Variance of expected project returns of project  $j$ .</td></tr><tr><td> $T$ </td><td>Time to option expiration.</td></tr><tr><td> $r_{f}$ </td><td>Risk-free interest rate.</td></tr><tr><td> $r_{d}$ </td><td>Risk-adjusted discount rate.</td></tr><tr><td> $s_{kj}$ </td><td>Dependency of project  $j$  on project  $k$  (expressed in terms of the percentage of the benefit of project  $j$  that depends on project  $k$ ).</td></tr><tr><td> $cf_{j}$ </td><td>Net cash flows associated with project  $j$ .</td></tr></table>

Projects costs $( C _ { j } )$ are comprised of one-time IT investments and ongoing costs of IT infrastructure and maintenance for a three-year time period. $B _ { j }$ represents the present value of estimated project benefits based on cash flows $( c f _ { j } )$ across different scenarios that represent future business conditions. Descriptive project statistics are summarized in Table 2.

The time horizon (t) for the option to invest in a project is divided into three successive one-year phases. This represents the typical time horizon for implementation of projects that are represented in EnergyCo’s portfolio of IT projects. EnergyCo estimated a time horizon of three years for the IT investments related to its decision to provide new services in a deregulated energy industry. The decision to exercise an option for first-phase projects begins at time $T = 0$ , while options on future phases can be initiated at $T = 1$ and $T = 2$ , respectively.

$\sigma _ { j } ^ { 2 }$ represents an estimate of the variance of project $j ^ { \circ } \mathbf { s }$ returns. It measures the risk associated with the project in terms of fluctuations in project cash flows for the duration of the project. We measure $\sigma _ { j } ^ { 2 }$ using the approach delineated in the previous section. The estimated project volatility ranges from a 12 percent to 18 percent, with an average portfolio volatility of 14.5 percent.

## Nested Options Model

Since a majority of the projects in EnergyCo’s portfolio are characterized by interdependencies with other projects, we represent the sequence of contingencies using a nested options model [21]. Our model is similar in concept to the embedded options model described in Benaroch [3], which provides an approach to embed a series of options to defer, expand, abandon, or contract a project.<sup>2</sup> An initial investment provides a platform for launching other applications by making follow-on investments in future periods. For instance, a Phase I project, such as E-billing/Payment, can be used as a platform to launch integrated billing and account management features through follow-on projects in Phase II, such as Integrated Billing, CyberRetail.com, and Kilowatt Kiosk. Hence, the total value of the cluster can be represented as a nested option:

<table><tr><td rowspan="2">Project benefits</td><td colspan="2">Phase I</td><td colspan="2">Phase II</td><td colspan="2">Phase III</td></tr><tr><td>Mean</td><td>Standard deviation</td><td>Mean</td><td>Standard deviation</td><td>Mean</td><td>Standard deviation</td></tr><tr><td>Conservative</td><td>262</td><td>249</td><td>1,013</td><td>2,343</td><td>2,174</td><td>2,741</td></tr><tr><td>Moderate</td><td>1,908</td><td>1,461</td><td>5,225</td><td>9,299</td><td>11,392</td><td>10,905</td></tr><tr><td>Aggressive</td><td>8,482</td><td>6,488</td><td>14,946</td><td>21,300</td><td>37,765</td><td>36,577</td></tr><tr><td>One-time costs</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Hardware</td><td>266</td><td>87</td><td>566</td><td>712</td><td>269</td><td>289</td></tr><tr><td>Software</td><td>133</td><td>43</td><td>183</td><td>85</td><td>366</td><td>750</td></tr><tr><td>Services</td><td>1,616</td><td>892</td><td>2,247</td><td>852</td><td>1,925</td><td>1,489</td></tr><tr><td>Content purchase</td><td>237</td><td>478</td><td>253</td><td>488</td><td>300</td><td>670</td></tr><tr><td>Advertising</td><td>477</td><td>346</td><td>1,306</td><td>2,324</td><td>2,848</td><td>2,726</td></tr><tr><td>Total</td><td>2,732</td><td>1,362</td><td>4,558</td><td>2,414</td><td>5,710</td><td>5,560</td></tr><tr><td>Ongoing costs</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Technology</td><td>20</td><td>6</td><td>47</td><td>71</td><td>924</td><td>2,412</td></tr><tr><td>Personnel</td><td>339</td><td>199</td><td>299</td><td>185</td><td>716</td><td>845</td></tr><tr><td>Overhead</td><td>68</td><td>40</td><td>60</td><td>37</td><td>143</td><td>169</td></tr><tr><td>Advertising</td><td>95</td><td>69</td><td>261</td><td>465</td><td>569</td><td>545</td></tr><tr><td>Total</td><td>522</td><td>262</td><td>667</td><td>618</td><td>2,353</td><td>3,131</td></tr><tr><td colspan="7">Note: The real numbers have been adjusted by a constant factor to protect EnergyCo&#x27;s confidentiality.</td></tr></table>

<sub>ptive</sub> <sub>Statistics</sub> <sub>of</sub> <sub>EnergyCo</sub> <sup>E-Business</sup> <sup>Projects</sup> <sup>(in</sup> <sup>thousa</sup>

$$
\begin{array}{l} V (\text { cluster }) = P V \left\{\text { Phase   I   projects } + \text { Call   value } \left[ \text { Phase   II   projects } + \text { Call   value } (\text { Phase   III   projects }) \right] \right\}. \end{array}\tag{2}
$$

We now use the nested options model to estimate the option value of the E-billing/ Payment cluster, which provides significant business value to companies that wish to provide basic self-service billing capabilities to their customers [2]. Phase II projects, such as Integrated Billing and Smart Bill, provide advanced functionality for electronic bill payment and are linked to the E-billing/Payment project through hard dependencies.

However, Name Your Price, an online auction project, is not completely dependent on implementation of E-billing/Payment in Phase I. We represent these types of soft dependencies as $s _ { k j } ,$ which is defined as the percentage reduction in benefit of project j if not preceded by project k. We now compute the project value of the E-billing/ Payment cluster as

$$
\begin{array}{l} V \left(\text {E - billing / Payment cluster}\right) = P V \left\{\text {E - billing / Payment} + \text {Call value} \left[ \text {Smart Bill} \right. \right. \\ \quad \left. + \text {Virtual Account Exec} + \text {Name Your Price} \right] + \text {Call value} \left[ \text {Kilowatt Kiosk} \right. \\ \quad \left. + \text {Call value} \left(\text {Private - label Energy Services}\right) \right] + \text {Call value} \left[ \text {Integrated Billing} \right. \\ \quad \left. + \text {Call value} \left(\text {Total Home Bundle}\right) \right] + \text {Call value} \left[ \text {CyberRetail.com} \right. \\ \quad \left. + \left(\text {Total Home Bundle} + \text {BEST} + \text {Rent - a - RetailCo} + \text {E - biz in a Box} \right\} \right]. \end{array}\tag{3}
$$

## Analysis Results

WE USE THE PROJECT BENEFITS ASSOCIATED WITH the moderate scenario for the E-billing/Payment project cluster to illustrate our nested options analysis. We calculate the value of the innermost call option because its value is part of the underlying asset value of its predecessor Phase II project. We start by calculating the value of the Total Home Bundle project, a Phase III project in the E-billing/Payment cluster. The project involves an investment of \$4,394,000 in Year 2 and ongoing costs of \$693,000 in each of the following three years. Positive cash flows in subsequent periods represent the growth in customer base from innovative services, with EnergyCo receiving a commission for each transaction. The value of this investment, at $T = 2$ , is equal to \$12,230,000.

We now turn to the option value for Integrated Billing, which is a predecessor to Total Home Bundle. The soft dependency $s _ { k j }$ represents the proportion of Total Home Bundle’s benefit that is dependent on the implementation of Integrated Billing. In other words, the value of realized benefits from Total Home Bundle will diminish by a factor equal to $s _ { k j }$ if it is not preceded by implementation of Integrated Billing. We adjust Total Home Bundle’s cash flows by $( 1 - s _ { k j } )$ to represent this partial dependency as follows:

$$
B _ {\mathrm{TOTALHOMEBUNDLE}} = P V (C F _ {\mathrm{TOTALHOMEBUNDLE}} \cdot (1 - s _ {k j})),
$$

where

$$
C F _ {\text { TOTAL   HOME   BUNDLE }} = \text { the   future   cash   flows   of   the   Total   Home   Bundle   project },
$$

and

$$
\begin{array}{r l} s _ {k j} = 0. 2 5 & (\text { percentage   of   Total   Home   Bundle's   benefit   attributed   to   its } \\ & \text { dependency   on   Integrated   Billing }). \end{array}
$$

The returns from Total Home Bundle are discounted to time t = 1 when the investment decision on Integrated Billing is made. We use the risk-free rate of return $( r _ { f } )$ of 5 percent to calculate C and a discount rate $( r _ { d } )$ of 10 percent to calculate the present value of returns (B). Hence, we have

$$
B _ {\text { TOTAL   HOME   BUNDLE }} = 2, 7 7 9, 0 0 0, \text { and } C _ {\text { TOTAL   HOME   BUNDLE }} = 4, 1 8 5, 0 0 0.
$$

Using Equation (1), the option value of Total Home Bundle attributed to the Integrated Billing project is calculated as

$$
\mathrm{V} _ {\text { TOTAL   HOME   BUNDLE }} = 9 5, 0 0 0, \text { where } d _ {1} = 2. 7 2, d _ {2} = 2. 5 9, \text { and } \sigma^ {2} = 0. 1 4.
$$

We calculate the option value of Total Home Bundle attributed to FreeEnergy.com in a similar manner.

Next, the total value of the Integrated Billing project is calculated as a sum of the present values of its returns minus cost, plus its nested option value attributed to Total Home Bundle.

$$
N P V _ {\text { INTEGRATED   BILLING }} = V _ {\text { TOTAL   HOME   BUNDLE }} + B _ {\text { INTEGRATED   BILLING }} - C _ {\text { INTEGRATED   BILLING }}.
$$

Hence,

$$
N P V _ {\text { INTEGRATED   BILLING }} = 9 5, 0 0 0 + 3, 0 9 3, 0 0 0 - 2, 1 6 2, 0 0 0 = 1, 0 2 6, 0 0 0.
$$

So we conclude that the NPV of the Integrated Billing project increases from \$931,000 to \$1,026,000 by including the option value of the Total Home Bundle project.

This example illustrates the application of the nested options model to calculate project NPVs for embedded projects. We now extend this approach to calculate the option value associated with the Phase I project, E-billing/Payment. A DCF analysis indicates that E-billing/Payment has a NPV of –\$313,000 if evaluated on a standalone basis. However, when the flexibility associated with the options on its underlying projects shown in Equation (3) is considered, it results in a large option value of \$59,876,000. Our example illustrates the importance of quantifying the business value associated with underlying options and the flexibility to launch follow-on projects. We note that CyberRetail.com alone accounts for a large percentage of the total value of the E-billing/Payment cluster, since it provides a portal for all customer relationship management activities.

Table 3. Prioritization of Projects with Real Options and DCF Analyses (in thousands of dollars)

<table><tr><td rowspan="2">Phase I projects</td><td colspan="2">Real options</td></tr><tr><td>NPV</td><td>DCF value</td></tr><tr><td>E-billing/Payment</td><td>59,876</td><td>(313)</td></tr><tr><td>Here, You Do It</td><td>58,120</td><td>272</td></tr><tr><td>LightsOut.com</td><td>24,173</td><td>(1,959)</td></tr><tr><td>SabreEnergy.com</td><td>19,401</td><td>920</td></tr><tr><td>Here to Serve</td><td>7,916</td><td>7,916</td></tr><tr><td>EnergyInfoMart.com</td><td>1,254</td><td>(1,057)</td></tr><tr><td>Relocation Central</td><td>625</td><td>625</td></tr><tr><td>Energy Cost Calculators</td><td>133</td><td>91</td></tr><tr><td>E-notification</td><td>(1,297)</td><td>(1339)</td></tr><tr><td>FreeEnergy.com</td><td>(1,688)</td><td>(1,688)</td></tr><tr><td>ECS2</td><td>(1,729)</td><td>(1,729)</td></tr><tr><td></td><td colspan="2">Real options</td></tr><tr><td>Phase II projects</td><td>NPV</td><td>DCF Value</td></tr><tr><td>Clearinghouse</td><td>68,919</td><td>68,919</td></tr><tr><td>CyberRetail.com</td><td>63,618</td><td>(1,082)</td></tr><tr><td>Electra.com</td><td>16,843</td><td>16,843</td></tr><tr><td>Name Your Price</td><td>6,561</td><td>6,561</td></tr><tr><td>E-energyAdvisor.com</td><td>5,670</td><td>5,670</td></tr><tr><td>Energy Knowledge Central</td><td>2,482</td><td>2,482</td></tr><tr><td>Online Environmental Management</td><td>1,646</td><td>1,583</td></tr><tr><td>Integrated Billing</td><td>1,026</td><td>931</td></tr><tr><td>Smart Bill</td><td>(1,659)</td><td>(1,659)</td></tr><tr><td>E-energytrading.com</td><td>(2,439)</td><td>(2,500)</td></tr><tr><td>Outsourced Energy Management</td><td>(3,094)</td><td>(3,167)</td></tr><tr><td>Virtual Account Exec</td><td>(4,025)</td><td>(4,025)</td></tr><tr><td>Kilowatt Kiosk</td><td>(4,271)</td><td>(4,317)</td></tr></table>

Table 3 represents the portfolio of Phase I and Phase II projects based on their project NPVs using nested real options and traditional DCF approaches. Our results indicate significant differences in the prioritization of projects across the two methods. For instance, the top three projects—E-billing/Payment; Here, You Do It; and LightsOut.com—have large option values of \$59,800,000, \$58,100,000, and \$24,100,000, respectively, while their DCF values are –\$313,000, \$272,000, and – \$1,960,000, respectively. Based on traditional DCF analyses, managers would have ignored the E-billing/Payment and LightsOut.com projects in favor of projects that provide higher immediate returns, such as Here to Serve. Ignoring the flexibility to exercise follow-on options embedded in these projects would have led to suboptimal funding decisions.

All Phase III projects have positive NPVs, and, since they do not have any embedded growth options, their NPVs based on real options analyses are equal to the NPVs based on DCF analyses. Hence, we do not show these projects explicitly in Table 3. However, we note that their NPVs may change based on the option to delay or cancel their predecessor projects in Phase I or II due to the impact of project interdependencies, as discussed in the next section.

## Sensitivity Analyses

To verify the sensitivity of the real option model to our project-specific volatility estimates, we conducted a sensitivity analysis using a range of values for σ<sup>2</sup> from 0.05 to 0.45. This method is similar to the conventional approach taken by others who use a similar range of values for σ<sup>2</sup> to assess the impact of changes in variance estimates on project valuation [5, 32]. As shown in Table 4, the prioritization rankings of these projects do not change across different volatility scenarios with the exception of the reversal in the rankings of FreeEnergy.com and ECS2 for $\sigma ^ { 2 } = 0 . 0 5$ and 0.10 (shown in italics). The results provide a measure of consistency to the overall project rankings reported in Table 4. We note that the variance in project returns may be more significant in other settings related to EnergyCo’s services and the environmental factors in its industry, which we do not explore in this paper.

## Project Prioritization

WE ELIMINATE ALL PHASE I AND II PROJECTS with negative NPVs based on real options analyses. The remaining projects form the feasible consideration set of projects that can be considered for funding during the annual budgeting cycle. Next, we identify any hard and soft dependencies between the projects that are eliminated and those that remain in the consideration set. As shown in Table 5, eliminating the negative NPV projects in Phases I and II has a material impact on two Phase III projects: Total Home Bundle and Private Label Energy Services. Their project benefits are reduced by factors of 25 percent and 33.2 percent, and their revised NPVs are equal to \$4,348,000 and \$9,834,000, respectively.

We note that reductions in the values of Phase III projects have a negative impact on their predecessor projects in Phases I and II. The NPVs of the affected projects are recalculated, and the updated values are shown in italics in Table 6. Our real options model captures portfolio effects where project values are related to other projects, and cancellations or delays have a ripple effect on other projects.

## Dynamic Portfolio Optimization Under Budget Constraints

We now turn to Table 7, where we apply the results of our real options model to a portfolio prioritization exercise subject to annual IT budget constraints. For discussion purposes, we assume that the firm has IT budget constraints of \$12 million, \$27 million, \$52 million, \$25 million, \$22 million, and \$20 million in the first six years. Subject to a budget constraint of \$12 million in the first year (T = 0), management can invest only in six of the nine Phase I projects with positive NPVs. We note that Energy Cost Calculators was funded even though EnergyInfoMart.com and Relocation Central have higher NPVs, because the former project’s costs are lower and satisfied the budget constraint in year T = 0. Since EnergyInfoMart.com and Relocation Central could not be initiated, they were deferred to the next period for funding. In other words, we exercised an option to delay these two projects. We identified the dependencies of the deferred projects and estimated their impact on the project portfolio using the methodology described in the prior section.

<table><tr><td rowspan="2">Phase I</td><td colspan="6">Project NPV (in thousands of dollars)</td></tr><tr><td> $\Sigma^2 = 0.05$ </td><td>0.10</td><td>0.15</td><td>0.25</td><td>0.35</td><td>0.45</td></tr><tr><td>E-billing/Payment</td><td>59,308</td><td>59,584</td><td>59,929</td><td>60,688</td><td>61,470</td><td>62,250</td></tr><tr><td>Here, You Do It</td><td>57,890</td><td>57,985</td><td>58,153</td><td>58,596</td><td>59,103</td><td>59,638</td></tr><tr><td>LightsOut.com</td><td>24,173</td><td>24,173</td><td>24,174</td><td>24,191</td><td>24,241</td><td>24,323</td></tr><tr><td>SabreEnergy.com</td><td>19,314</td><td>19,346</td><td>19,404</td><td>19,581</td><td>19,811</td><td>20,069</td></tr><tr><td>Here to Serve</td><td>7,916</td><td>7,916</td><td>7,916</td><td>7,916</td><td>7,916</td><td>7,916</td></tr><tr><td>EnergyInfoMart.com</td><td>1,206</td><td>1,237</td><td>1,284</td><td>1,389</td><td>1,494</td><td>1,594</td></tr><tr><td>Relocation Central</td><td>625</td><td>625</td><td>625</td><td>625</td><td>625</td><td>625</td></tr><tr><td>Energy Cost Calculators</td><td>99</td><td>122</td><td>148</td><td>200</td><td>250</td><td>300</td></tr><tr><td>E-notification</td><td>(1,332)</td><td>(1,309)</td><td>(1,282)</td><td>(1,232)</td><td>(1,186)</td><td>(1,145)</td></tr><tr><td>FreeEnergy.com</td><td>(1,856)</td><td>(1,740)</td><td>(1,643)</td><td>(1,484)</td><td>(1,353)</td><td>(1,242)</td></tr><tr><td>ECS2</td><td>(1,730)</td><td>(1,730)</td><td>(1,730)</td><td>(1,730)</td><td>(1,730)</td><td>(1,730)</td></tr><tr><td colspan="7">Phase II</td></tr><tr><td>Clearinghouse</td><td>68,920</td><td>68,920</td><td>68,920</td><td>68,920</td><td>68,920</td><td>68,920</td></tr><tr><td>CyberRetail.com</td><td>63,365</td><td>63,470</td><td>63,655</td><td>64,141</td><td>64,698</td><td>65,284</td></tr><tr><td>Electra.com</td><td>16,844</td><td>16,844</td><td>16,844</td><td>16,844</td><td>16,844</td><td>16,844</td></tr><tr><td>Name Your Price</td><td>6,561</td><td>6,561</td><td>6,561</td><td>6,561</td><td>6,561</td><td>6,561</td></tr><tr><td>E-energyAdvisor.com</td><td>5,670</td><td>5,670</td><td>5,670</td><td>5,670</td><td>5,670</td><td>5,670</td></tr><tr><td>Energy Knowledge Central</td><td>2,482</td><td>2,482</td><td>2,482</td><td>2,482</td><td>2,482</td><td>2,482</td></tr><tr><td>Online Environmental Management</td><td>1,592</td><td>1,617</td><td>1,646</td><td>1,701</td><td>1,751</td><td>1,796</td></tr><tr><td>Integrated Billing</td><td>948</td><td>998</td><td>1,053</td><td>1,157</td><td>1,252</td><td>1,337</td></tr><tr><td>Smart Bill</td><td>(1,659)</td><td>(1,659)</td><td>(1,659)</td><td>(1,659)</td><td>(1,659)</td><td>(1,659)</td></tr><tr><td>E-energytrading.com</td><td>(2,492)</td><td>(2,466)</td><td>(2,437)</td><td>(2,382)</td><td>(2,333)</td><td>(2,288)</td></tr><tr><td>Outsourced Energy Management</td><td>(3,158)</td><td>(3,132)</td><td>(3,104)</td><td>(3,049)</td><td>(2,999)</td><td>(2,954)</td></tr><tr><td>Virtual Account Exec</td><td>(4,025)</td><td>(4,025)</td><td>(4,025)</td><td>(4,025)</td><td>(4,025)</td><td>(4,025)</td></tr><tr><td>Kilowatt Kiosk</td><td>(4,309)</td><td>(4,283)</td><td>(4,254)</td><td>(4,199)</td><td>(4,149)</td><td>(4,104)</td></tr><tr><td colspan="7">Note: The prioritization rankings of FreeEnergy.com and ECS2 were reversed for  $\sigma^2 = 0.5$  and 0.10.</td></tr></table>

<sub>nsitivity</sub> <sub>Analyses</sub> <sub>of</sub> <sub>Real</sub> O<sup>ptions</sup> <sup>Value</sup> <sup>As</sup>

Table 5. Impact of Elimination of Negative NPV Projects

<table><tr><td>Eliminated project</td><td>Dependent project(s)</td><td>Dependency (percentage of benefit reduced)</td></tr><tr><td rowspan="2">E-notification</td><td>Private Label Energy Services</td><td>0.083</td></tr><tr><td>E-energytrading.com*</td><td>0.5</td></tr><tr><td>FreeEnergy.com</td><td>Total Home Bundle</td><td>0.25</td></tr><tr><td>ECS2</td><td>Kilowatt Kiosk*</td><td>0.5</td></tr><tr><td>Smart Bill</td><td>—</td><td>—</td></tr><tr><td>E-energytrading.com</td><td>Private Label Energy Services</td><td>0.083</td></tr><tr><td>Outsourced Energy Management</td><td>Private Label Energy Services</td><td>0.083</td></tr><tr><td>Virtual Account Exec</td><td>—</td><td>—</td></tr><tr><td>Kilowatt Kiosk</td><td>Private Label Energy Services</td><td>0.083</td></tr><tr><td colspan="3">Note: * does not have an impact on the project since it is eliminated due to negative NPV.</td></tr></table>

In the second year (T = 1), the consideration set includes Phase II projects and all deferred Phase I projects, subject to the budget constraint of \$27 million. We note that only three of eight Phase II projects with positive NPV can be funded in this period due to budget constraints. We estimated the impact of delaying these Phase II projects on the portfolio, since cancellations or delays have a ripple effect on the portfolio. We note that a Phase I project, EnergyInfoMart.com, was selected for funding because its lower implementation costs met the budget constraint, unlike other Phase II projects that exhibit higher NPVs. All unfunded Phase II projects and the deferred Phase I project (i.e., Relocation Central) that did not make the cut in T = 1 are deferred to the next period for consideration. We adopted a similar approach for prioritization at time T = 2. Eight projects, including three delayed Phase II projects, are funded.

Our model provides an integrated approach for portfolio optimization that incorporates real options inherent in IT portfolio management. We note that this exercise represents a dynamic optimization, where projects are selected by maximizing the portfolio value subject to project budget and dependency constraints in each time period. Each time period entails a feasible consideration set from which projects can be selected for funding. All unfunded projects are deferred to the consideration set for the next period. When projects are deferred, we rerun the options model so that the impact of deferred projects on their interdependencies can be updated. In Table 7, such changes are shown in italics, where the project NPVs of E-billing/Payment, SabreEnergy.com, Energy Cost Calculators, and Private Label Energy Services changed due to delays in other projects that have dependencies on these projects.

<sub>oritization</sub> <sub>of</sub> <sub>Projects</sub> <sub>Subject</sub> <sub>to</sub> <sub>Re</sub>a<sup>l</sup> <sup>Option</sup>

<table><tr><td rowspan="2">Phase I projects</td><td rowspan="2">NPV (thousands of dollars)</td><td rowspan="2">T = 0</td><td colspan="5">Project costs (in thousands of dollars)</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>E-billing/Payment</td><td>56,940</td><td>947</td><td>281</td><td>281</td><td>281</td><td>—</td><td>—</td></tr><tr><td>Here, You Do It</td><td>55,253</td><td>2,011</td><td>263</td><td>263</td><td>263</td><td>—</td><td>—</td></tr><tr><td>LightsOut.com</td><td>24,173</td><td>2,464</td><td>942</td><td>942</td><td>942</td><td>—</td><td>—</td></tr><tr><td>SabreEnergy.com</td><td>19,402</td><td>2,431</td><td>299</td><td>299</td><td>299</td><td>—</td><td>—</td></tr><tr><td>Here to Serve</td><td>7,916</td><td>2,803</td><td>852</td><td>852</td><td>852</td><td>—</td><td>—</td></tr><tr><td>EnergyInfoMart.com</td><td>1,254</td><td>3,468</td><td>811</td><td>811</td><td>811</td><td>—</td><td>—</td></tr><tr><td>Relocation Central</td><td>625</td><td>5,459</td><td>627</td><td>627</td><td>627</td><td>—</td><td>—</td></tr><tr><td>Energy Cost Calculators</td><td>92</td><td>864</td><td>268</td><td>268</td><td>268</td><td>—</td><td>—</td></tr><tr><td colspan="8">Phase II Projects</td></tr><tr><td>Clearinghouse</td><td>68,920</td><td>—</td><td>11,509</td><td>2,590</td><td>2,590</td><td>2,590</td><td>—</td></tr><tr><td>CyberRetail.com</td><td>60,464</td><td>—</td><td>4,175</td><td>385</td><td>385</td><td>385</td><td>—</td></tr><tr><td>Electra.com</td><td>16,844</td><td>—</td><td>4,876</td><td>766</td><td>766</td><td>766</td><td>—</td></tr><tr><td>Name Your Price</td><td>6,561</td><td>—</td><td>4,273</td><td>530</td><td>530</td><td>530</td><td>—</td></tr><tr><td>E-energyAdvisor.com</td><td>5,670</td><td>—</td><td>2,678</td><td>482</td><td>482</td><td>482</td><td>—</td></tr><tr><td>Energy Knowledge Central</td><td>2,482</td><td>—</td><td>3,896</td><td>424</td><td>424</td><td>424</td><td>—</td></tr><tr><td>Online Environmental Management</td><td>1,586</td><td>—</td><td>5,168</td><td>681</td><td>681</td><td>681</td><td>—</td></tr><tr><td>Integrated Billing</td><td>940</td><td>—</td><td>2,162</td><td>385</td><td>385</td><td>385</td><td>—</td></tr><tr><td colspan="8">Phase III Projects</td></tr><tr><td>E-biz in a Box</td><td>41,644</td><td>—</td><td>—</td><td>17,223</td><td>9,057</td><td>9,057</td><td>9,057</td></tr><tr><td>Rent-a-RetailCo</td><td>36,226</td><td>—</td><td>—</td><td>8,356</td><td>1,179</td><td>1,179</td><td>1,179</td></tr><tr><td>Private Label Energy Services</td><td>9,834</td><td>—</td><td>—</td><td>2,346</td><td>1,068</td><td>1,068</td><td>1,068</td></tr><tr><td>EMO</td><td>6,371</td><td>—</td><td>—</td><td>3,944</td><td>3,459</td><td>3,459</td><td>3,459</td></tr><tr><td>BEST</td><td>5,144</td><td>—</td><td>—</td><td>1,766</td><td>355</td><td>355</td><td>355</td></tr><tr><td>Total Home Bundle</td><td>4,348</td><td>—</td><td>—</td><td>4,395</td><td>693</td><td>693</td><td>693</td></tr><tr><td>LockOn 2.0</td><td>2,960</td><td>—</td><td>—</td><td>1,940</td><td>660</td><td>660</td><td>660</td></tr><tr><td>Total costs</td><td></td><td>20,447</td><td>43,080</td><td>50,556</td><td>27,057</td><td>22,714</td><td>16,471</td></tr></table>

<table><tr><td rowspan="2">Phase I</td><td rowspan="2">NPV (thousands of dollars)</td><td rowspan="2">T=0</td><td colspan="5">Project Costs (in thousands of dollars)</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>E-billing/Payment</td><td>53,142</td><td>947</td><td>281</td><td>281</td><td>281</td><td>—</td><td>—</td></tr><tr><td>Here, You Do It</td><td>55,253</td><td>2,011</td><td>263</td><td>263</td><td>263</td><td>—</td><td>—</td></tr><tr><td>LightsOut.com</td><td>24,173</td><td>2,464</td><td>942</td><td>942</td><td>942</td><td>—</td><td>—</td></tr><tr><td>SabreEnergy.com</td><td>19,184</td><td>2,431</td><td>299</td><td>299</td><td>299</td><td>—</td><td>—</td></tr><tr><td>Here to Serve</td><td>7,916</td><td>2,803</td><td>852</td><td>852</td><td>852</td><td>—</td><td>—</td></tr><tr><td>Energy Cost Calculators</td><td>83</td><td>864</td><td>268</td><td>268</td><td>268</td><td>—</td><td>—</td></tr><tr><td colspan="8">Phase II</td></tr><tr><td>Clearinghouse</td><td>68,920</td><td>—</td><td>11,509</td><td>2,590</td><td>2,590</td><td>2,590</td><td>—</td></tr><tr><td>CyberRetail.com</td><td>60,654</td><td>—</td><td>4,175</td><td>385</td><td>385</td><td>385</td><td>—</td></tr><tr><td>Electra.com</td><td>16,844</td><td>—</td><td>4,876</td><td>766</td><td>766</td><td>766</td><td>—</td></tr><tr><td>EnergyInfoMart.com $^{1}$ </td><td>1,036</td><td>—</td><td>3,468</td><td>811</td><td>811</td><td>811</td><td>—</td></tr><tr><td colspan="8">Phase III</td></tr><tr><td>E-biz in a Box</td><td>41,644</td><td>—</td><td>—</td><td>17,223</td><td>9,057</td><td>9,057</td><td>9,057</td></tr><tr><td>Rent-a-RetailCo</td><td>36,226</td><td>—</td><td>—</td><td>8,356</td><td>1,179</td><td>1,179</td><td>1,179</td></tr><tr><td>EMO</td><td>6,371</td><td>—</td><td>—</td><td>3,944</td><td>3,459</td><td>3,459</td><td>3,459</td></tr><tr><td>Private Label Energy Services</td><td>6,147</td><td>—</td><td>—</td><td>2,346</td><td>1,068</td><td>1,068</td><td>1,068</td></tr><tr><td>Name Your Price $^{2}$ </td><td>5,422</td><td>—</td><td>—</td><td>4,273</td><td>530</td><td>530</td><td>530</td></tr><tr><td>E-energyAdvisor.com $^{2}$ </td><td>5,155</td><td>—</td><td>—</td><td>2,678</td><td>482</td><td>482</td><td>482</td></tr><tr><td>BEST</td><td>5,144</td><td>—</td><td>—</td><td>1,766</td><td>355</td><td>355</td><td>355</td></tr><tr><td>Energy Knowledge Central $^{2}$ </td><td>2,051</td><td>—</td><td>—</td><td>3,896</td><td>424</td><td>424</td><td>424</td></tr><tr><td>Total costs</td><td></td><td>11,520</td><td>26,933</td><td>51,939</td><td>24,011</td><td>21,106</td><td>16,554</td></tr><tr><td>Portfolio budget</td><td></td><td>12,000</td><td>27,000</td><td>52,000</td><td>25,000</td><td>22,000</td><td>20,000</td></tr><tr><td colspan="8">Notes:  $^{1}$  represents a deferred Phase I project;  $^{2}$  represents a deferred Phase II project. Numbers in italics represent projects with revised NPVs as a result of deferring projects with which they share soft dependencies.</td></tr></table>

<sub>na</sub>m<sup>ic</sup> <sup>Project</sup> <sup>Prioritization</sup> <sup>Subject</sup> <sup>to</sup> <sup>Budget</sup>

We now develop a real options portfolio optimization algorithm for such a dynamic portfolio optimization model. This algorithm represents a dynamic multiperiod optimization model, where the objective function is to maximize the overall portfolio value in each time period, subject to project budget and dependency constraints. Let $P _ { i j }$ represent the consideration set of all feasible projects $( j = 1 , 2 , 3 , . . . . , m )$ that are eligible for funding in time period $i = 1 , 2 , 3 , . . . , n . p _ { i j } \in P _ { i j }$ represents a binary variable equal to one if project j is funded in period i and zero otherwise. $b _ { i }$ represents the portfolio budget in period i. Let $\nu _ { j }$ represent the real option NPV of project j and $c _ { i j }$ be the cost of project j in period i. The algorithm involves the following additional steps:

1. Identify all hard and soft dependencies $s _ { k j }$ between all combinations of projects j and k, where $( j = 1 , 2 , 3 , . . . . , m )$ and $( \bar { k = 1 } , 2 , 3 , . . . , m ) , j \neq k . s _ { _ { k j } }$ represents the percentage of lost revenue of project j due to its dependency on project k.

2. For the first time period $( i = 1 )$ , maximize

$$
\sum_ {j} p _ {i j}. v _ {j} \text {   for   all   } p _ {i j} \in P _ {i j},\tag{4}
$$

subject to $\Sigma _ { j } c _ { i j } p _ { i j } \leq b _ { i }$

$$
v _ {j} = B _ {j} N \left(d _ {1 j}\right) - C _ {j} e ^ {- r _ {f} t} N \left(d _ {2 j}\right)
$$

as defined by Margrabe [22] in Equation in (1) and

$$
B _ {j} = P V \left(c f _ {j} * \left(1 - \sum_ {k} s _ {k j}\right)\right),
$$

where $B _ { _ i }$ is the present value of project $j ^ { \circ } \mathrm { s }$ cash flows $( c f _ { i } )$ adjusted for the impact of dependencies from all other projects $k$ on project j. The term (1 – $\Sigma _ { k } s _ { k j } )$ represents the proportion of project $j ^ { \circ } \mathrm { s }$ benefits that is not dependent on other projects. Finally, $p _ { i j }$ is equal to 1 if project j is funded in period i and equal to 0 otherwise, and $0 \leq s _ { \scriptscriptstyle k i } \leq 1$

3. Identify all projects for which $p _ { i j } = 0$ and transfer to the consideration set $P _ { i + 1 , j }$ of the next time period $i + 1 . \mathrm { H } p _ { _ { i j } } ^ { \circ } = 1$ , then $p _ { i + 1 , j } = 1$ for all $i = i + 1$ . That is, once a project is funded, it will continue to be funded in subsequent years.

4. Update all dependencies $s _ { k j }$ that are affected when $p _ { _ { i j } } = 0$ for time period i.

5. For each time period i, update all project NPVs $\nu _ { j }$ due to any change in the dependency $s _ { k j } .$ Since project NPVs v are updated in each period, this heuristic accommodates the option to cancel a project if it fails or delay subsequent projects dependent on the failed project.

6. Repeat Steps 1 through 5 for each time period $i = i + 1$

## Option Value of Delay

We note that the option value of project delay should be differentiated from the opportunity cost of delay. In the former case, a project may be delayed if its NPV is negative based on current conditions, but may be initiated later if future periods provide more favorable conditions [24]. In such scenarios, the option value of delay is positive and, at worst, can only be zero. Hence, the managerial flexibility associated with the option to delay is defined as the difference in project NPVs if the project is undertaken today versus being delayed to a later period. On the other hand, the opportunity cost of delay may have a negative impact on portfolio NPV, because the firm may not be able to launch other dependent projects that are delayed to future time periods. The opportunity cost of project delays may have a negative impact on overall portfolio value if there is a risk of deterioration in the project NPV due to competitive, customer demand, environmental, or regulatory changes.

As observed in Table 7, budget constraints lead to projects being delayed, leading in turn to a reduction in the NPVs of projects that are dependent on the delayed project. For instance, a delay in funding Integrated Billing leads to a reduction in the NPV of Total Home Bundle from \$4,348,000 to \$859,000. In other words, the opportunity cost of delaying Integrated Billing equals \$3,489,000, the loss in business benefit to Total Home Bundle.

## Constructing Learning Options from Risk-Correlated Projects

THE RISKS ASSOCIATED WITH IMPLEMENTATION and deployment of one IT project may impact other projects as well. Business managers often conceive of multiple projects that support or complement the same business goal or strategic intent, resulting in a project portfolio that has projects with correlated risk profiles. These complementarities may result in a significant level of positive correlation of the technological and functional risks associated with implementation of projects with similar capabilities and dependent on similar types of technology building blocks or project management skills.<sup>3</sup> In other words, the risk-adjusted valuation of a portfolio may be different from the sum of the valuations of individual projects if the firm is risk averse.

The degree of interactions between options on a portfolio of projects is related to the option type and degree of overlap of exercise regions. As described in Trigeorgis [33], options are likely to be additive when the options involved are of the opposite type (calls and puts), the exercise timings of the two types of options are close together, and the options are more out of the money—that is, have high exercise prices for call options and low prices for put options. Project portfolios for which the real options fit the above profile are likely to have less valuation errors compared to portfolios where significant correlations exist between projects with similar risk characteristics. The analyses of correlations between different options, as described in Trigeorgis [33], show that all feasible combinations of options need to be enumerated and their impact on portfolio value calculated in order to incorporate the impact of correlated project risks in our model.

We note that the interactions become very complicated if more than two options are considered. That is, if two European call options are preceded by a put option, then negative interactions will exist between the positive interaction pair and the prior put [33]. Since the EnergyCo portfolio consists of several possible combinations of projects, with positive and negative interactions, we note that it becomes very complicated to enumerate all possible combinations of projects (puts and calls) before we can identify the combination with the highest value. Instead, we address the issue of option correlations by describing the problem as a series of learning options, where a lead project and its cluster of follow-on projects will share common implementation risks. Real options allow managers to treat the earlier project as a learning option for subsequent, dependent projects. For example, the E-billing/Payment project provides the electronic bill presentment and payment technology that is leveraged by four dependent projects: Integrated Billing, Smart Bill, CyberRetail.com, and Kilowatt Kiosk. After deploying the E-billing/Payment project, managers can learn if it has been successfully deployed and evaluate whether to implement the four follow-on projects that are affected by similar risks.

The value of the learning option is calculated as the implementation cost avoided for the four follow-on projects minus the cost of implementing the E-billing/Payment project. Our data indicates that the present value of the sum of the initial costs of the four follow-on projects is \$11,880,000, while the cost of implementing E-billing/ Payment in the first stage is \$946,000. Hence, the value of the learning option associated with the Phase I investment is equal to $\$ 11,880,000$ Managers can treat the E-billing/Payment project as a learning option to explore the feasibility of making future follow-on investments. If project risks in the two phases are perfectly correlated, a negative outcome in the first phase will indicate that it is not worthwhile to invest in Phase II investments. In the absence of objective realworld data on the magnitudes of correlations between project risks, we are not able to incorporate such correlated risk profiles into the analyses.

## Conclusions

THIS PAPER EXTENDS PRIOR RESEARCH by providing a new method for making IT valuation and investment decisions for project portfolio management. While prior studies have used real options to value a single project and ignored the effect of project interdependencies, our model accounts for the complexities involved in valuing a portfolio of projects while considering the impact of interdependencies and sequencing constraints. A key contribution involves the development of a nested real options model to understand the impact of project interdependencies on project valuation decisions. Using a real-world case study of an energy company, we show that projects that provide infrastructure capabilities to launch enabling projects have higher option values that are not evident if evaluated using DCF analysis.

A second contribution is the development of an integrated approach for portfolio optimization that applies real options thinking to IT portfolio management. We develop a real options portfolio optimization algorithm that is used in combination with the nested options model to prioritize projects and make optimal funding decisions in each time period. We believe that this integrated method provides a novel approach to combine the advantages of using real options analyses with traditional portfolio management models.

A third contribution is the development of a methodology to estimate project-specific volatilities based on different scenarios of expected project benefits, without resorting to historical data or the need to make ad hoc project-specific assumptions. We provide an approach to use the information derived from scenario planning to estimate the volatility of individual projects. This approach overcomes deficiencies of previous approaches that involve assumptions about the magnitudes and range of project-specific volatilities. We link our approach to scenario analysis methods described in Clemons [9] and Clemons and Gu [10] to delineate different types of future scenarios that may unfold and the impact of competitor strategies on scenario cash flows.

The managerial implications of our approach and analysis are twofold. First, our model takes into consideration the impact of project interdependencies on project valuation decisions. This addresses a concern of IT managers who typically do not see the big picture and, therefore, fail to leverage the benefits of capabilities being developed across multiple projects. Second, our approach provides a rational basis for project prioritization and funding exercises that are typically exposed to unhealthy competition, gaming, and criticism across departments. Our options model provides an analytical approach that objectively considers the immediate and future value of projects. It focuses attention on tactical decisions, such as identifying projects for immediate initiation, while also considering the present value of future options.

A limitation of our approach is the assumption required for estimating projectspecific volatilities, where we assume that the overall portfolio volatility can be estimated accurately. Another limitation is that the estimated project benefits used in our real options model are based on the accuracy of scenario-planning exercises used to guide the development of the three scenarios described in this study. Our assumptions regarding changes in customer behavior and competitor actions will impact the estimated project returns for different scenarios that can be incorporated in our analyses using Monte Carlo simulation. We also assumed that project interdependencies can be identified ex ante (before projects are initiated), which may not always be feasible in real-world settings where emerging technologies and standards change rapidly.

This work can be further developed by extending the real options algorithm into a mathematical programming model for portfolio optimization subject to project dependencies and budget constraints. Another area for exploration includes interactions between projects, where implementation of one project may actually result in a reduction in the value of another project. Hence, the problem may need to be solved as a dynamic programming model, where the optimal prioritization represents the solution that maximizes value across all potential combinations of projects.<sup>4</sup> A third possibility is to understand the impact of projects on strategic, nonfinancial enterprise goals and incorporate these considerations directly into the options model.

Acknowledgments: An earlier version of this paper appeared in R.H. Sprague Jr. (ed.), Proceedings of the Thirty-Seventh Hawaii International Conference on System Sciences (Los Alamitos, CA: IEEE Computing Society, 2004). The authors gratefully acknowledge helpful comments from Robert Kauffman, Eric Clemons, Rajiv Dewan, Suresh Radhakrishnan, the anonymous reviewers for HICSS-37 and JMIS, and the participants in our presentation at HICSS-37 conference in January 2004. All remaining errors are the authors’ sole responsibility.

## NOTES

1. This represents a conservative estimate of the overall portfolio volatility and is consistent with the range of volatility values reported in other studies [4, 32].

2. Unlike Benaroch’s [3] approach, we do not consider the valuation of compound options that are evaluated using a log-transformed model. Since the projects described in our paper involve IT investments that embed simple options, where the project benefits involve uncertainty, our use of modified Black-Scholes and binomial models is valid.

3. The authors thank two anonymous reviewers for introducing the discussion on correlation between project-specific risks and its impact on the risk-adjusted valuation of the IT projects.

4. A simple formulation of this situation was proposed and solved using simple enumeration by Benaroch [3]. However, this is not feasible for real-world portfolio optimization, which typically involves a large number of projects with complex interactions.

## REFERENCES

1. Amram, M., and Kulatilaka, N. Real Options: Managing Strategic Investment in an Uncertain World. Boston: Harvard Business School Press, 1999.

2. Au, Y.A., and Kauffman, R.J. Should we wait? Network externalities, compatibility, and electronic billing adoption. Journal of Management Information Systems, 18, 2 (Fall 2001), 47–63.

3. Benaroch, M. Managing information technology investment risk: A real options perspective. Journal of Management Information Systems, 19, 2 (Fall 2002), 43–84.

4. Benaroch, M., and Kauffman, R.J. A case for using real options pricing analysis to evaluate information technology project investments. Information Systems Research, 10, 1 (1999), 70–86.

5. Benaroch, M., and Kauffman, R.J. Justifying electronic network expansion using real option analysis. MIS Quarterly, 24, 2 (2000), 197–225.

6. Brandenburger, A.M., and Nalebluff, B.J. Co-opetition. New York: Currency Doubleday, 1996.

7. Chabrow, E. IT staffs lack financial chops for project analysis. InformationWeek (March 24, 2003) (available at www.informationweek.com/story/showArticle.jhtml?articleID =8700123).

8. Clemons, E.K. Evaluating strategic investments in information systems. Communications of the ACM, 34, 1 (1991), 22–36.

9. Clemons, E.K. Information technology investments: Dealing effectively with strategic uncertainty through scenario analysis. In J. Luftman (ed.), Competing in the Information Age: Align in the Sand, 2d ed. New York: Oxford University Press, 2003, pp. 314–336.

10. Clemons, E.K., and Gu, B. Justifying information technology investments: Balancing the need for speed of action with certainty before action. Journal of Management Information Systems, 20, 2 (Fall 2003), 11–48.

11. Cooper, R.G. Portfolio Management for New Products. Reading, MA: Perseus, 1998.

12. Dai, Q.; Kauffman, R.J.; and March, S.T. Valuing IT middleware infrastructure with real options. Working paper, Carlson School of Management, University of Minnesota, Minneapolis, 2004.

13. Datz, T. Portfolio management: How to do it right. CIO Magazine (2003) (available at www.cio.com/archive/050103/portfolio.html).

14. Dixit, A.K., and Pindyck, R.S. The options approach to capital investment. Harvard Business Review (May–June 1995), 105–115.

15. Dos Santos, B. Justifying investment in new information technologies. Journal of Management Information Systems, 7, 4 (Spring 1991), 71–89.

16. Fichman, R. Real options and IT platform adoption: Implications for theory and practice. Working Paper, Boston College, Chestnut Hill, MA, 2003.

17. Groenveld, P. Roadmapping integrated business and technology. Research Technology Management, 45, 5 (September 1997), 48–55.

18. Kambil, A.; Henderson, C.J.; and Mohsenzadeh, H. Strategic management of information technology investments. In R. Banker, R.J. Kauffman, and M.A. Mahmood (eds.), Strategic Information Technology Management: Perspectives on Organizational Growth and Competitive Advantage. Harrisburg, PA: Idea Group, 1993, pp. 161–178.

19. Keen, P.G.W. Value analysis: Justifying decision support systems. MIS Quarterly, 5, 1 (1981), 1–15.

20. Kogut, B., and Kulatilaka, N. Options thinking and platform investments: Investing in opportunity. California Management Review, 36, 4 (1994), 52–71.

21. Luehrman, T.A. Strategy as a portfolio of real options. Harvard Business Review (September–October 1998), 89–99.

22. Margrabe, W. The value of an option to exchange one asset for another. Journal of Finance, 33 (March 1978), 177–186.

23. Marlin, S. Getting the IT mix right. InformationWeek (October 27, 2003) (available at www.informationweek.com/story/showArticle.jhtml?articleID=15600182).

24. McDonald, R., and Siegel, S. The value of waiting to invest. Quarterly Journal of Economics, 101 (1986), 707–727.

25. McGrath, R.M., and MacMillan, I. Assessing technology projects using real options reasoning. Research Technology Management, 43, 4 (July–August 2000), 35–49.

26. Panayi, S., and Trigeorgis, L. Multi-stage real options: The case of information technology infrastructure and international bank expansion. Quarterly Review of Economics and Finance, 38, special issue (1998), 675–692.

27. Sambamurthy, V.; Bharadwaj, A.; and Grover, V. Shaping agility through digital options: Reconceptualizing the role of information technology in contemporary firms. MIS Quarterly, 27, 2 (2003), 237–263.

28. Schwartz, E.S., and Zozaya-Gorostiza, C. Investment under uncertainty in information technology: Acquisition and development projects. Management Science, 49, 1 (2003), 57–70.

29. Smith, J.E., and McCardle, K.F. Valuing oil properties: Integrating option pricing and decision analysis approaches. Operations Research, 46, 2 (1998), 198–217.

30. Tallon, P.P.; Kauffman, R.J.; Lucas, H.C., Jr.; Whinston, A.B.; and Zhu. K. Using real options analysis for evaluating uncertain investments in information technology. Communications of the AIS, 9 (2002), 136–167.

31. Taudes, A. Software growth options. Journal of Management Information Systems, 15, 1 (Summer 1998), 165–185.

32. Taudes, A.; Feurstein, M.; and Mild, A. Options analysis of software platform decisions: A case study. MIS Quarterly, 24, 2 (2000), 227–243.

33. Trigeorgis, L. The nature of options interactions and the valuation of investments with multiple real options. Journal of Financial and Quantitative Analysis, 28, 1 (1993), 1–20.

34. Trigeorgis, L. Real Options. Cambridge, MA: MIT Press, 1996.

35. Van Der Heijden, K. Scenarios. New York: Wiley, 1996.

36. Verhoef, C. Quantitative IT portfolio management. Science of Computer Programming, 45, 4 (2002), 1–96.

37. Weill, P., and Broadbent, M. Leveraging the New Infrastructure: How Market Leaders Capitalize on Information Technology. Boston: Harvard Business School Press, 1998.

38. Zhu, K., and Weyant, J.P. Strategic decisions of new technology adoption under asymmetric information: A game-theoretic model. Decision Sciences, 34, 4 (2003), 643–675.

<sub>a</sub>, <sub>and</sub> <sub>energy</sub> <sub>usage</sub> <sup>reports</sup> <sup>by</sup> <sup>type</sup> <sup>of</sup> <sup>c</sup> <sub>anagement</sub> <sub>serv</sub>i<sub>ces</sub> <sub>to</sub> <sub>custo</sub>m<sup>ers</sup> <sup>v</sup>i<sup>a</sup> <sup>the</sup> I<sup>nternet</sup>, <sup>wh</sup>i<sup>ch</sup> i<sup>nc</sup>l<sup>udes</sup> <sup>energ</sup> <sub>me</sub> <sub>data</sub> <sub>to</sub> <sub>be</sub> <sub>sent</sub> <sub>e</sub>l<sub>ectron</sub>i<sub>ca</sub>ll<sub>y</sub> <sub>to</sub> l<sub>arge</sub> <sub>co</sub>m<sup>merc</sup>i<sup>a</sup>l <sup>and</sup> i<sup>ndus</sup> <sub>es</sub> <sub>through</sub> <sub>ho</sub>m<sup>e</sup> <sup>bu</sup>il<sup>ders</sup> <sup>and</sup> <sup>heat</sup>i<sup>ng</sup>, <sup>vent</sup>il<sup>at</sup>i<sup>on</sup>, <sup>and</sup> <sup>a</sup>i<sup>r-cond</sup>i<sup>t</sup>i<sup>on</sup>i<sup>ng</sup> <sub>v</sub>i<sub>ng-re</sub>l<sub>ated</sub> <sub>co</sub>m<sup>pan</sup>i<sup>es</sup> <sup>to</sup> <sup>prov</sup>i<sup>de</sup> <sup>energy</sup> <sup>s</sup>i<sup>gn-up</sup> <sup>serv</sup>i<sup>ces</sup> <sup>u</sup> <sub>o</sub> <sub>enab</sub>l<sub>e</sub> <sub>EnergyCo</sub> <sub>to</sub> <sub>a</sub>c<sup>t</sup>i<sup>ve</sup>l<sup>y</sup> <sup>market</sup> <sup>to</sup> <sup>“prov</sup>i<sup>der</sup> <sup>of</sup> l<sup>ast</sup> <sup>res</sup>

## Appendix B. Volatility Calculation for Total Home Bundle Project

EXPECTED BENEFITS FOR EACH PROJECT were estimated for three different business scenarios: conservative, moderate, and aggressive, as shown below. The volatility of each project can be calculated using the following stepwise approach, where the Total Home Bundle project is used as an illustrative example. The project has estimated benefits of \$2,134,000, \$9,352,000, and \$22,881,000 with respect to the conservative, moderate, and aggressive scenarios, respectively.

• Step 1: Calculate spread between conservative and moderate scenarios, as a percentage of the sum of project benefit $\mathfrak { s } = ( 9 , 3 5 2 - 2 , 1 3 4 ) / 3 4 , 3 6 8 = 0 . 2 1$ . Similarly, calculate the spread between aggressive–moderate scenarios = 0.39. The overall project spread of Total Home Bundle is equal to the sum of the project $\mathrm { s p r e a d s } = 0 . 2 1 + 0 . 3 9 = 0 . 6 0$

• Step 2: Calculate the mean and standard deviation of the overall project portfolio spread. Mean portfolio spread = 0.72; standard deviation of mean portfolio spread = 0.085.

• Step 3: Estimate the mean volatility of the overall project portfolio based on management input. We assign an overall volatility estimate of 15 percent for the project portfolio.

• Step 4: Calculate the standard deviation (X) of overall portfolio volatility as: $X / 1 5 = 0 . 0 8 5 / 0 . 7 2 , \mathrm { o r } X = 1 . 7 8$

In other words, to calculate the project-specific volatility, the portfolio volatility should be adjusted by 1.78 for each standard deviation by which the project spread differs from the mean portfolio spread. We assume that the ratio of the standard deviation to the mean portfolio volatility is proportional to the ratio of the standard deviation of the portfolio spread to its mean.

• Step 5: Calculate the number of standard deviations (n ) by which the project spread differs from the mean portfolio spread. Total Home Bundle spread – mean portfolio spread $= 0 . 6 0 - 0 . 7 2 = - 0 . 1 2$ . n = (Total Home Bundle spread – mean portfolio spread)/standard deviation of portfolio spread $= - 0 . 1 2 / 0 . 0 8 5 = - 1 . 3 6$ That is, the Total Home Bundle spread is 1.36 standard deviations below the mean portfolio spread.

• Step 6: To calculate the project-specific volatility, adjust the portfolio volatility by $X ^ { * } n _ { \ i }$ . That is, Total Home Bundle volatility = Mean Portfolio volatility $+ X ^ { * }$ $n _ { \scriptscriptstyle { i } } = 1 5 - 1 . 7 8 ^ { \scriptscriptstyle * } 1 . 3 6 = 1 2 . 5 8$ percent. Hence, the project volatility of Total Home Bundle is estimated to be 12.58 percent, about 2.42 percent below the overall portfolio volatility.

## Assumptions

• In Step 3, we assume that the volatility of the overall portfolio is known or can be easily estimated with reasonable accuracy. Instead of using a single point estimate, we can also use a Monte Carlo simulation to model the portfolio volatility as a statistical distribution with a mean and standard deviation and incorporate such a distribution into our above approach for estimation of project-specific volatilities.

• In Step 4, we assume that the ratio of the standard deviation of the portfolio volatility to its mean is proportional to the ratio of the standard deviation of the portfolio spread to its mean. This assumption is valid for most project portfolios where the spread in project benefits across different scenarios is directly proportional to the volatility in project returns. It may be sensitive to the addition or removal of project outliers that may bias the overall portfolio volatility significantly in either direction.

Appendix C. Glossary of Technical Terms

<table><tr><td>Technical term</td><td>Definition</td></tr><tr><td>Adjusted baseline volatility</td><td>The portfolio volatility estimate adjusted for the number of standard deviations by which an individual project spread deviates from the mean portfolio spread.</td></tr><tr><td>Baseline volatility</td><td>The assigned volatility of the mean portfolio spread.</td></tr><tr><td>Complementors</td><td>A firm whose products or services enhance the offerings of the target firm.</td></tr><tr><td>Dynamic optimization model</td><td>A mathematical programming model that maximizes portfolio value subject to budget constraints and project interdependencies across multiple time periods.</td></tr><tr><td>Feasible consideration set</td><td>Projects with NPVs greater than zero comprise the feasible set eligible for funding.</td></tr><tr><td>First-mover advantage</td><td>A sometimes insurmountable advantage gained by the first significant company to move into a new market.</td></tr><tr><td>Hard dependency</td><td>A dependency wherein a project cannot be implemented if its predecessor project has not been implemented.</td></tr><tr><td>Interdependency</td><td>Interaction between capabilities that are shared or leveraged among IT projects in a portfolio.</td></tr><tr><td>Leverage point</td><td>A project capability that provides value-added services on a follow-on project.</td></tr><tr><td>Nested options model</td><td>A model that embeds the call option value of projects that are dependent on other projects.</td></tr><tr><td>Portfolio prioritization</td><td>The ordering of the feasible consideration set of IT projects according to estimated value subject to various budget constraints.</td></tr><tr><td>Portfolio spread</td><td>The average sum of the difference of project benefits between aggressive/moderate and moderate/conservative assumptions.</td></tr><tr><td>Portfolio volatility</td><td>Overall volatility of a portfolio of projects based on the spread in benefits across different project scenarios.</td></tr><tr><td>Project cluster</td><td>A cluster of projects that are dependent on similar technologies and capabilities.</td></tr><tr><td>Soft dependency</td><td>A dependency wherein a project may be implemented without its predecessor, but its value is reduced.</td></tr><tr><td>Value net</td><td>A map of a company and its linkages to its customers, competitors, suppliers, and partners.</td></tr></table>
