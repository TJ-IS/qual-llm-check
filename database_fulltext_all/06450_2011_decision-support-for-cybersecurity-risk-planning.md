---
otero_id: 6450
otero_key: "53X9G46G"
title: "Decision support for Cybersecurity risk planning"
authors: "Loren Paul Rees; Jason K. Deane; Terry R. Rakes; Wade H. Baker"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.02.013"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support for Cybersecurity risk planning

Loren Paul Rees <sup>a</sup>, Jason K. Deane <sup>a,</sup>⁎, Terry R. Rakes <sup>a</sup>, Wade H. Baker <sup>b</sup>

<sup>a</sup> Department of Business Information Technology, Pamplin College of Business, Virginia Tech., Blacksburg, VA 24061, United States <sup>b</sup> Verizon Business Security Solutions, Ashburn, VA 20147, United States

## a r t i c l e i n f o

Article history: Received 5 March 2010 Received in revised form 9 November 2010 Accepted 17 February 2011 Available online 23 February 2011

Keywords: IT security Decision support Genetic algorithms Fuzzy sets

## a b s t r a c t

Security countermeasures help ensure the con<sup>fi</sup>dentiality, availability, and integrity of information systems by preventing or mitigating asset losses from Cybersecurity attacks. Due to uncertainty, the <sup>fi</sup>nancial impact of threats attacking assets is often dif<sup>fi</sup>cult to measure quantitatively, and thus it is dif<sup>fi</sup>cult to prescribe which countermeasures to employ. In this research, we describe a decision support system for calculating the uncertain risk faced by an organization under cyber attack as a function of uncertain threat rates, countermeasure costs, and impacts on its assets. The system uses a genetic algorithm to search for the best combination of countermeasures, allowing the user to determine the preferred tradeoff between the cost of the portfolio and resulting risk. Data collected from manufacturing <sup>fi</sup>rms provide an example of results under realistic input conditions.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Assuring a secure information technology (IT) environment for the transaction of commerce is a major concern. The magnitude of the task is growing yearly, as attackers become more knowledgeable, more determined, and bolder in their efforts. According to a lead security expert at International Data Corporation, a global provider of market intelligence and advisory services for the IT community, “Emerging new attack vectors, more targeted campaigns, compliance, and the layering of new technologies on the corporate infrastructure are all factors having a tremendous impact on the overall risk to an organization” [21]. Given that corporate expenditures are usually a good indicator of the level of concern about an issue, security is obviously near the top of many IT executives' lists. According to IDC, the global market for providers of information security services is projected to exceed \$32.5 billion in 2010 [21].

The New York Times recently noted that “the intrusion into Google's computers and related attacks from within China on some thirty other companies point to the rising sophistication of such assaults and the vulnerability of even the best defenses” [25]. The Times further states that, according to the Computer Security Institute, malware infections are up from one-half to almost two-thirds of companies surveyed last year, at an average cost of \$235,000 for each organization. Finally, the newspaper observes, malware is being exploited in new terrains with malicious code that turns on cellphone microphones and cameras for the purpose of industrial spying [25].

Because of the variety of methods attackers use to try to in<sup>fi</sup>ltrate and disrupt information technology infrastructures, an enormous amount of effort has been devoted to the development of a wide array of technological tools and actions such as intrusion blocking software, mitigation software, or secure communication protocols to block these intrusions or to mitigate the damaging effects of an incursion. These actions are called countermeasures or controls. While this type of research is certainly vital, in their 2005 report, the President's Information Technology Advisory Council (PITAC) stressed the paramount importance of the need for numerous other research efforts [28]. They suggested that we desperately need “strategies to change the widely held perception that greater networked security is not worth the cost to individuals and corporations—a perception that actively discourages needed software development in this area” [28]. Speci<sup>fi</sup>cally, we need additional research that is focused on helping organizations determine, from this enormous array of countermeasures, which set is best to employ for their given business situation. This process of balancing the cost of potential losses from security breaches against the investment expense required to prevent or mitigate those breaches is known as security risk management.

Countermeasure types can vary considerably. Some countermeasures are designed to limit physical access to an area which permits access to the IT infrastructure. These include key entry systems, retinal or <sup>fi</sup>ngerprint scans, and armed guards. Other countermeasures are designed to block access and/or protect privacy over networks serving the organization. These might include <sup>fi</sup>rewalls, data encryption, and virus and spyware scanners. Also, some countermeasures are designed to permit recovery if an intrusion is successful, such as backing up important <sup>fi</sup>les on a frequent basis. There are several standards that stipulate and suggest minimal control con<sup>fi</sup>gurations, including British Standard 7799, NIST Special Publication 800–53, the Graham–Leach–Bliley Act of 1999, and the North American Electric Reliability Council's Urgent Action Standard 1200, but these alone have not proven to be suf<sup>fi</sup>cient. As a result, organizations are eager to <sup>fi</sup>nd intelligent methods to guide their IT security spending. Regardless of the countermeasures employed, or the methodology used to select them, there are costs involved, and companies often have to modify their policies and business practices in order to accommodate the chosen countermeasures. Unfortunately, most companies are not sure how to handle this challenge. Baker and Wallace [4, p. 30], reporting on a survey of countermeasure implementations and effects across the world, found that

Overall, many organizations are managing security in a somewhat inconsistent and super<sup>fi</sup>cial manner. Rather than taking a calculated or rational approach, they're emphasizing certain controls while leaving others, though no less important, poorly maintained.

They conclude that [4, p. 32] “Researchers should further investigate the bene<sup>fi</sup>ts of combining various levels of technical, management, and operational controls to achieve true holistic security against a diverse range of present and future risks.”

The literature describes two broad reasons why inadequate progress has been made on methods for developing portfolios of effective countermeasures. First, managers have no proven and reliable methodology for measuring the effectiveness of their security initiatives [3]. Second, feedback from corporate IT planners has repeatedly shown that they are uncomfortable with having to supply <sup>fi</sup>xed values related to future events which they know to be uncertain [3]. In fact, with respect to the <sup>fi</sup>rst factor, Berinato [6] notes that in the IT security domain, evidence exists that there is often little correlation between increased managerial spending on countermeasure initiatives and actual improvements to the overall security record. This brings into question the effectiveness of those risk management tools that are currently available. With respect to the second factor, managers repeatedly state that they do not believe results from studies based on numbers they are often forced to provide, because they know how little they trust the input. With little con<sup>fi</sup>dence in input data, and no proven methodologies to process these inputs, Berinato's observation is of little surprise.

This research addresses the inherent uncertainty within the IT risk management domain using fuzzy set theory. Fuzzy sets have been shown to be an effective way to deal mathematically with uncertainty [19,24,26,27,29,30,37–39,41]. Within the IT security area, fuzzy sets have been employed in a number of non-economic studies. Radha and Jayapriya [30] used a fuzzy model to detect malicious nodes in a wireless ad-hoc network. Song et al. [35] proposed a fuzzy logic model for enhancing the trust index of resource sites in a peer-to-peer grid network by upgrading their intrusion defense capabilities. Prasad et al. [29] developed an intrusion detection system using data mining, genetic algorithms, and fuzzy logic. Haslum et al. [19] used Markov modeling and fuzzy risk assessment to develop an intrusion prevention system which detects malicious packets within normal network traf<sup>fi</sup>c and blocks them before they can incur damage.

Within the IT security risk area, fuzzy sets have been used in several different studies. Rakes et al. [31] used fuzzy sets to represent various IT security threats and countermeasures, and to model their effectiveness, but did not address risk calculations. Zhao et al. [42] use AHP and fuzzy logic to assess the risk of a single asset such as a network, but do not re<sup>fl</sup>ect existing countermeasures in the risk assessment. In other words, they look at the loss side without trying to understand the in<sup>fl</sup>uences which led to the risk level. Van de Walle and Rutkowski [36] develop an IT service continuity threat assessment system which uses fuzzy relational modeling to allow members of a decision-making group to assess their fuzzy preferences regarding the available countermeasures in an effort to reach a group decision alignment. However, their structure is aimed at group preference alignment and does not allow for the calculation of expected risk. Sodiya et al. [34] use fuzzy sets to model six common threats, and then use fuzzy rule inference to combine them and arrive at a point estimate for the overall threat level. They do not address uncertainty or risk tradeoffs.

In order to aid planners in reducing security risk by forming a costeffective portfolio of countermeasures, we design and build a decision support system (DSS) that will allow them to express threat pro<sup>fi</sup>les, mitigation effectiveness, and potential per-event dollar losses in realistic terms that capture this high degree of uncertainty. For the DSS's model base management system, we synthesize from the literature the fuzzy mathematics that will enable managers to characterize the uncertain risk (threats attacking assets to produce losses) associated with any set of proposed countermeasures. This enables economic comparisons with the cost of those countermeasures and the available risk budget. Next, we utilize a metaheuristic for the intelligent allocation of countermeasure dollars. For the database management component of our DSS, we provide a speci<sup>fi</sup>c approach to collecting uncertain IT-security inputs which grew out of conversations with IT industry professionals. We believe this to be a critical step in developing a system that will be practical; we will provide an example in a later section that analyzes industry-collected uncertain data to produce a suggested strategy.

This paper is organized as follows. The remainder of this section provides a high-level overview of existing approaches to IT security planning. Section 2 presents the design and implementation of the DSS; in particular, Section 2.1 shows the DBMS component, which is based on capturing uncertain, industry data. Section 2.2 explains the MBMS component, which includes the mathematical model for calculation of the system-wide (uncertain) risk as well as a metaheuristic search module. Section 3 presents an example of a minimum-risk strategy based on industry data. Section 4 offers conclusions and managerial implications.

## 1.1. Current approaches to IT security and risk

Most IT security management approaches consist of checklists which decision makers use to develop a coverage strategy; these generally are little more than a triage approach to categorizing threats. One popular approach for risk visualization has been the construction of a risk cube, where each axis or dimension represents one of the three components of risk (threats, assets, and vulnerabilities), and the volume of the cube represents the amount of risk [8]. Any countermeasure which can reduce the length of the face along a dimension should be considered, as a smaller cube after mitigation efforts have been performed indicates a diminished risk. While this visualization has been helpful to managers in understanding risk factors, it does not suggest any systematic mechanism for reducing the risk components or making economic tradeoffs.

Several models have been developed which attempt to deal with risk analysis in a qualitative manner. Mark Egan (the then CTO for Symantec) in his book The Executive Guide To Information Security, introduced a very simple tabular model which allows users to rate threat severities into one of three categories/columns (low, medium, and high) and then to average across columns [15]. This simple triage approach to subjective threat impact analysis, though insightful, is not able to capture system uncertainty. Bistarelli et al. [7] used defense trees and conditional preference networks (CP-nets) as a formalism to select sets of countermeasures and to reason with qualitative and conditional preference information. Alberts and Dorofee [1] developed a system called OCTAVE which also utilizes qualitative information to assess risk. GAO/AMID [17] prioritized risk based on a risk assessment matrix that represents risk levels according to the severity and the probability of occurrence of harmful events; these two factors are then scaled in a qualitative way. However, none of these qualitative methodologies allows the type of risk tradeoffs essential for systematic analysis leading to an optimal portfolio.

Others have tried approaches that quantify IT security risk analysis. Beauregard [5] applied the Value Focused Thinking (VFT) approach from general risk analysis to assess the level of information assurance within the Department of Defense units. While subjective scores in VFT are normalized to the range (0, 1) and are similar conceptually to fuzzy membership values in fuzzy-set analysis, they are essentially point estimates of the value (loss) associated with a given outcome. As such, they suffer from the inability to express any distributional properties, as is possible with fuzzy sets. In a similar vein, Buckshaw et al. [9] tackled the design of critical DOD systems in an analysis approach they called MORDA (Mission Oriented Risk and Design Analysis (MORDA)). MORDA embraces VFT and embeds it within a planning system called Security Optimization Countermeasure Risk and Threat Evaluation System (SOCRATES). However, once again, risk determinations are limited to point estimates. Kujawski and Miller [23] describe a quantitative risk-based analysis tool for selecting military counterterrorism systems which “allows for con<sup>fi</sup>dence levels rather than simply point estimates,” but it requires conditional probability distribution data on threat levels and consequences. To illustrate their approach, they assume Weibull distributions for every process, but acknowledge that lack of probabilistic data is problematic.

## 2. A DSS for it risk analysis under uncertainty

We consider a scenario where IT-related assets are under attack by either external or internal threats. A <sup>fi</sup>rm may face multiple threats at any point in time [3]. If successful, these threats attack assets associated with various business practices, and if the assets are not protected, their damage and destruction will result in <sup>fi</sup>nancial loss to the <sup>fi</sup>rm. To defend its assets, the <sup>fi</sup>rm implements countermeasures designed to block or mitigate the severity of the attack, and possibly to provide a second level of defense after the assets are attacked (data recovery, system re-load, etc.). Since countermeasures are costly to implement, the <sup>fi</sup>rm is forced to tradeoff countermeasure costs against the expected reduction in <sup>fi</sup>nancial loss.

We calculate risk as the product of threat occurrences (expected events/year) and their resultant losses in dollars/event. Thus, annual risk is

$$
R = \sum_ {i} E _ {i} ^ {*} L _ {i} (C)\tag{1}
$$

where

$$
\begin{array}{l l} R = & \text { risk   in   dollars   per   year } \\ i = & \text { index   representing   the   different   threats   facing   the   firm } \\ E _ {i} = & \text { the   expected   number   of   security   events   of   type   } i \text {   per   year } \\ L _ {i} (C) = & \text { expected   dollar   loss   caused   by   security   event   } i \text {   given   the } \\ & \text { current   set   of   countermeasures   } C. \end{array}
$$

We refer to the term $L _ { i } ( C )$ as the single-event loss expectancy. There are three major types of single-event loss expectancies. The <sup>fi</sup>rst is brand damage which represents damage to a company's image (for example, when partners in a supply chain with, say, Equifax or Visa have data tapes with private customer information stolen from them). The second is regulatory <sup>fi</sup>nes. This kind of loss might occur, for example, when a hospital fails to comply with the federal 1996 Health Insurance Portability and Accountability Act (HIPAA) stipulations, and the con<sup>fi</sup>dentiality of patients' information is breeched. The third is production losses due to disruption of IT resources which support production.

There is also an important issue to consider in modeling threats. In order to make risk interpretation simpler, we de<sup>fi</sup>ne each threat as a threat against a particular asset. For example, we consider a virus against an asset as one threat and that same virus against another asset as a second threat. Thus, calculations of risk will have a high dimensionality, but will be more straightforward.

The use of this simplistic approach to risk calculation has the advantage of transparency, but it assumes independence among threats as they cause dollar losses. To our knowledge, there has been no empirical research quantifying the <sup>fi</sup>nancial impact of the joint occurrence of threats within a <sup>fi</sup>rm. Certainly, there are higher instances of particular types of threats by industry, such as record theft or man-in-the middle attacks within the <sup>fi</sup>nancial services industry. However, these are intra-industry effects and are captured by the data for any given company. But given the possible interactions among a reasonable number of threats (50 to 60) and the many assets which can be affected, the number of possible correlations would be enormous and unlikely to be available. Thus, we believe that the threat-against-asset approach, whereby individual impacts from threats are broken down and independently targeted directly against asset losses, is a practical approach and one that will provide a reasonable estimate of risk.

## 2.1. The DBMS: representing risk data under uncertainty

Unfortunately, the risk factors identi<sup>fi</sup>ed in Eq. (1) are very hard to quantify with precision. The terms vary from year to year, and even within a year are dif<sup>fi</sup>cult to specify exactly. As an example, Verizon Business provides IT security risk consulting services. A recent Verizon Business client stated they were very pleased with a <sup>fi</sup>nal list of IT security projects put forward for the next year, but cautioned repeatedly that the data they supplied to Verizon Business were very uncertain. They felt uncomfortable with having to furnish countermeasure costs, threat rates, and loss-to-asset costs, although they admitted that they supposed “some guess was better than none.” Some in the industry go so far as to argue that no quantitative analysis should be undertaken at all because data are so unreliable. While we believe this to be a minority view, it is generally agreed within the IT-security industry that there is a lack of precision in rates and costs and that security plans and projects are therefore uncertain themselves.

## 2.1.1. Data collection

In light of the inherent uncertainty in newly-developing threats, countermeasure effectiveness, and <sup>fi</sup>nancial impacts, and the resulting dif<sup>fi</sup>culties in developing any form of empirical-based distributional information, what type of data is possible? In seeking to determine what data industry participants and experts would be willing to furnish with con<sup>fi</sup>dence, we partnered with the Risk Intelligence group within Verizon Business. This group oversees the collection, analysis, and distribution of internal and external (client) data relevant to understanding and managing information risk. Intel from these activities is used to provide Verizon's services, inform personnel and clients, and publish credible research for the security community. As part of Verizon Business' ongoing data collection in security risk, they recently conducted a survey in which they asked about rates and impact costs for ten different, key threat-assets:

• Malicious code infection

• Unauthorized system access or modi<sup>fi</sup>cation

• Insider abuse of access

• Insider misuse of resources

• Error and omissions

• Denial of service attacks

• Network outage

• Data compromise

• Lost or stolen physical resources

• Social engineering,

and they asked about implementation levels, effectiveness, and costs for 80 different countermeasures. We were given access to these data on the condition that company names and identifying information not be reported. They surveyed information from security executives, managers, and technical specialists, obtaining 349 responses in North America, Europe, Asia-Paci<sup>fi</sup>c, and South America. 34% of the represented organizations had fewer than 100 computer systems, 38% between 101 and 1000, and 28% in excess of 1000 systems. Respondents came from various industries/agencies, including services, information technology, government, production, education, and <sup>fi</sup>nance.

There were two main areas in the survey that relate to our study. The <sup>fi</sup>rst area was threats attacking assets, and the questions of interest involved the rates of such attacks and the impact costs of successful attacks, collected as categorical data. For example, for threat rates, companies were asked to choose between the categories daily, weekly, monthly, quarterly, semi-yearly, yearly, and never. For impact costs of successful attacks the categories were none, thousands, tens of thousands, hundreds of thousands, millions, and tens of millions (dollars). These categories were used in the survey because Verizon Business employees knew, based on their previous experiences, that managers could not supply point estimate data with any con<sup>fi</sup>dence.

The second area of interest in the survey dealt with countermeasures. The data included the extent to which existing countermeasures were implemented by the <sup>fi</sup>rm and the dollar cost of such countermeasure implementation. The categories for countermeasure implementation costs were the same as those for threat impact costs given above, and the countermeasure implementation level was expressed for each of the 80 controls in the study as either 0 (off) or a number between 1 and 6 inclusive (on), indicating no implementation at all (0) to comprehensive (total) implementation (6).

Because security managers had little insight into the effectiveness of the range of control levels against the variety of threats, this set of data was not included in the survey but was provided by experts within the Verizon Business Risk Intelligence group (the values we obtained specify the percentage of threats-attacking-assets that are blocked for each countermeasure as a function of implementation level). In the example section, we illustrate the complete DSS for determining a near-optimal portfolio of countermeasure choices utilizing a sample of the data described above.

## 2.1.2. Representation of uncertainty

Obviously, a risk-assessment model based on reliable and accurate point estimates of threats, countermeasure costs, and asset losses is preferable. If point estimates were available, mixed integer programming could be used as a solution approach; in fact, a recent paper by Deane et al. [12] illustrated such an approach based on point estimates for determining IT risk subsidies to prevent supply-chain disruption. However, they illustrated their approach with hypothetical data as no real-world data were available.

When reliable point estimates are not possible, distributional information is typically utilized. However, both the nature of threats themselves and the nature of the data available preclude the postulation of speci<sup>fi</sup>c probability density functions on either theoretical grounds or on the basis of chi-square goodness-of-<sup>fi</sup>t tests. Given the fact that the only data available at this time in the industry are categorical data, point estimates and distributional <sup>fi</sup>ts must be excluded. Instead the use of fuzzy sets seems to offer the most <sup>fl</sup>exibility. It is worth noting that even when point estimates are available in uncertain domains, they do not provide the distributional information that a fuzzy set or “possibility distribution” can capture [40]. In his description of fuzzy restrictions and possibility distributions, Zadeh [40] used the concept of the fuzzy set acting as an “elastic constraint” on the values a variable could assume, such that the boundaries of this constraint provide additional information about possible values beyond the expected value.

Beyond the unavailability of distributional data, we chose to use fuzzy sets for three reasons: (1) Overall system risk may be (relatively) easily computed in closed form. We will show in Section 2.2.1 how to compute overall system fuzzy risk. (2) Fuzzy sets are a broadly accepted and mathematically valid mechanism for dealing with uncertainty [19,24,26,27,29,30,37–39,41]. (3) Fuzzy sets have been used successfully in, and are relevant to, DSS. For example, a search of the premier journal for DSS (i.e., Decision Support Systems) with the term fuzzy sets brings up 284 articles [16].

Zadeh [37] <sup>fi</sup>rst suggested the use of fuzzy relationships or sets to represent vague or imprecise concepts. In its basic form, fuzzy set theory relates a value called a “grade of membership” for each possible value of an independent variable in order to indicate how strongly that value belongs to a qualitative description. In fuzzy logic, the independent variable is also referred to as a linguistic variable [39]. In our example, we will use fuzzy sets to model threat-attacking-asset rates and per-successful-event impact costs. Without loss of generality, we will treat countermeasure costs and effectiveness percentages as constants, as nothing in the system precludes these being treated as fuzzy sets as well.

## 2.2. The MBMS: calculating system risk and determining the countermeasure portfolio

This section describes the two main functions of the DSS model base management system.

## 2.2.1. Calculating system risk

Consider a simpli<sup>fi</sup>ed scenario with all threats, effectiveness, and loss impacts known and constant. For example, assume that threatagainst-asset number 1 occurs at the rate of 100 attacks per year and that two countermeasures (CMs) with effectiveness of 0.8 and 0.6 will be used against these threats. Since the countermeasures have an effectiveness of 0.8 and 0.6, they will have an ineffectiveness of 0.2 and 0.4. Assuming the effectiveness of the CMs are independent, the CMs will only allow (100 attacks/year)(0.2)(0.4) = 8 successful attacks/year.

Now assume that the <sup>fi</sup>nancial impact is \$5K/successful attack. We can expect a loss of (8 successful attacks/year) (\$5K/successful attack) = \$40K/year. If the <sup>fi</sup>rm has engaged in “detection and recovery” countermeasures, such as regularly backing up data, the loss may be ameliorated. Assume that such activity has an effectiveness of 0.6 (or ineffectiveness of 0.4), leading to an expected loss (or risk) of \$16K/year due to threat-attacking-asset 1. If the same procedure is followed for all signi<sup>fi</sup>cant threats-attacking assets, and the sum is formed over all threats, the total system risk is obtained.

The calculation of total system risk utilizing fuzzy sets follows essentially the same procedure, except extended multiplication is used instead of multiplication, and extended addition is utilized rather than addition when summing over all threats-attacking assets. In both cases we invoke interval analysis methodology, which relies on the α– cut approach [13], as initially described by Zadeh [39], and later applied by Dong and Wong [13].

2.2.1.1. The mathematics of extended operations using interval analysis. Assume we wish to perform algebraic operations such as multiplication and addition on fuzzy numbers. Let $A _ { 1 } , A _ { 2 } , . . . , A _ { N }$ be fuzzy numbers de<sup>fi</sup>ned on universes $X _ { 1 } , X _ { 2 } , . . . , X _ { N } ,$ respectively, and then let f be a function which maps $X _ { 1 } { \times } X _ { 2 } { \times } . . . { \times } X _ { N }$ to the universe Y. According to the extension principle, the fuzzy image B of $A _ { 1 } , A _ { 2 } , . . . , A _ { N }$ through f has the membership function $\mu _ { B } ( y )$ , where

$$
\mu_{B}(y) = \underset { \begin{array}{c}x_{i}\in X_{i}\\ i = 1,2,\ldots ,N \end{array}}{\vee}\{\wedge [\mu_{A}1(x_{1}), \mu_{A}2(x_{2}), \ldots ,\mu_{A}N(x_{N})]\},\tag{2}
$$

where $y { = } f ( x _ { 1 } , x _ { 2 } , { \ldots } , x _ { N } )$ , lower case elements denote elements of the fuzzy set, ∨ is referred to as a t-norm and represents the maximum operator, ∧ is referred to as a t-conorm and is the minimum operator, and $\mu _ { \mathrm { A j } } ( \mathbf { x } _ { \mathrm { i } } )$ is the grade of membership for the linguistic variable $\mathsf { A } _ { \mathrm { j } }$ over $\mathsf { A } _ { \mathrm { j } } ^ { \prime } \mathsf { s }$ de<sup>fi</sup>ned range of membership.

A straightforward method for implementing the extension principle is the process of interval analysis using α–cuts. Suppose we have two fuzzy sets to multiply or add. First, we choose a membership level called α where $0 \leq \alpha \leq 1$ . For example, consider Fig. 1 and $\alpha = 0 . 2$ . Next, we <sup>fi</sup>nd the two points at which the membership level cuts across the two sides of the <sup>fi</sup>rst fuzzy set. The corresponding values on the horizontal axis represent an interval of values within which the membership is greater than or equal to the chosen level α; in the <sup>fi</sup>gure these two points are ${ \tt X } = 2$ and ${ \tt X } = 3 .$ Next, we repeat the process for the same α on the second set, giving ${ \tt X } = 5$ and ${ \tt X } = 8$ for the right-most set. We then have two intervals representing equal membership in the two sets. Now, we use the formula for extended operations presented in Eq. (2). For example, for some α suppose the two intervals are [a, b] and [c, d] and we want to multiply the two fuzzy sets. The corresponding interval on the combined set would be

$$
\begin{array}{l} [ a, b ] \otimes [ c, d ] = [ \wedge (a c, a d, b c, b d), \vee (a c, a d, b c, b d) ] \\ \qquad = [   m i n (a c, a d, b c, b d),   m a x (a c, a d, b c, b d) ], \end{array}\tag{3}
$$

where the binary operator ⊗ represents multiplication of two fuzzy sets.

If we want to add (⊕), the corresponding interval on the combined set would be

$$
\begin{array}{r l} [ a, b ] \oplus [ c, d ] & = [ \wedge (a + c, a + d, b + c, b + d), v (a + c, a + d, b + c, b + d) ] \\ & = [ a + c, b + d ]. \end{array} \tag {4}
$$

In the example of Fig. 1 with $\alpha = 0 . 2$

$$
\begin{array}{l} [ 2, 3 ] \otimes [ 5, 8 ] = [ m i n (1 0, 1 6, 1 5, 2 4), m a x (1 0, 1 6, 1 5, 2 4) ] = [ 1 0, 2 4 ]. \\ [ 2, 3 ] \oplus [ 5, 8 ] = [ a + c, b + d ] = [ 7, 1 1 ]. \end{array}
$$

In each case, the resulting interval for α provides one pair of points for the combined fuzzy set, which occurs at the intersection of α on the vertical axis and the interval values on the horizontal axis. By repeating this process for various levels of α, we can construct a piecewise approximation of the combined set (i.e., the set which results from multiplication or addition of two other fuzzy sets). Increasing the number of α levels will improve the approximation for the combined set, but it will also increase the computational burden accordingly.

2.2.1.2. The system-risk-calculation algorithm. Fig. 2 presents the steps necessary to compute overall fuzzy risk. In Fig. 2, there is one lightly shaded region and two darker-shaded regions, one of which is labeled “Deterrence and Prevention” and the other “Detection and Recovery.” Starting with the top of the lighter region, we select a threat-againstan-asset. For this threat against an asset, we extract from the DBMS the appropriate fuzzy set representation. This threat is then mitigated by the deterrence-and-prevention countermeasures shown in the top, darker-shaded box. The fuzzy set for each countermeasure that countermands the threat is extracted from the DBMS. As we are interested in the ineffectiveness of the control, we calculate 1 minus the CM effectiveness to obtain the number of threats that survive this countermeasure. Then, all CM fuzzy set survival rates are (extended) multiplied together to calculate the aggregate fuzzy set showing survival in spite of all deterrence countermeasures.

![](/api/attachments/53X9G46G/fulltext/images/cddde9cff5343cff46b1c0301fd7c8eeee09cbe7f4825aebff2301116905ce8c.jpg)  
Fig. 1. An example illustrating extended operations using interval analysis methodology.

When the fuzzy set for the threat in the light-shaded region of Fig. 2 is (extended) multiplied by this aggregate deterrence set of the top darker region, we obtain the fuzzy set for the number of threatsattacking-asset that survive the organization's prevention countermeasures for that selected threat.

Next we calculate the <sup>fi</sup>nancial impact due to the surviving threats by forming the product of the fuzzy set for the expected loss of this asset with the fuzzy set for surviving threats against asset. This <sup>fi</sup>nancial loss has one more opportunity to be ameliorated by the <sup>fi</sup>rm by applying the detection and recovery countermeasures shown in the bottom darker-shaded box. The process is similar to that within the other dark box. Finally, we form the extended sum of all the fuzzy sets for the <sup>fi</sup>nancial impacts due to each of the surviving threats. This gives the overall system risk. For the interested reader, Appendix A contains the algorithm presented in Fig. 2, but with the extended mathematics explicitly shown.

Our discussion thus far on risk calculation has been predicated on countermeasures applied independently without treatment of any possible interaction effects. In some circumstances, this assumption of independence will not be accurate. As pointed out by Cavusoglu, Raghunathan, and Cavusoglu [10], layered security technologies may rely on each other for their operations and thereby affect each other's contribution. They use the example of <sup>fi</sup>rewall effectiveness which is lowered by the installation of an intrusion detection system. In our data, because of the sheer number of threat and countermeasure combinations, and the dif<sup>fi</sup>culty in ascertaining even basic effectiveness, no attempt was made to gather information on the enormous number of possible interactions. However, our procedure does not preclude their use. If we determine that CM1 behaves differently in combination with CM2 than it would alone, and have data to support this conclusion, we can easily model CM1, CM2, and the joint CM1/ CM2 as three different possible countermeasures, with a restriction on countermeasure selection that prevents CM1 or CM2 from being chosen if CM1/CM2 is chosen. Because this increases the number of countermeasures to consider, we would likely limit this treatment to the most signi<sup>fi</sup>cantly interacting pairs, tuples, etc.

## 2.2.2. Determining the near-optimal countermeasure portfolio

For a large number of possible threats against assets and even a few loss categories, the computational aspects of risk calculation are signi<sup>fi</sup>cant. While most companies could probably narrow their list of the most serious threats and vital assets to a dozen or less, the computational effort involved is still substantial. In addition, although the previous section shows how to calculate overall fuzzy system risk for a given portfolio of countermeasures, it does not show how to select a near-optimal portfolio.

Genetic Algorithms (GAs), developed by Holland [20] in $1 9 7 5 ,$ are ‘intelligent’ probabilistic search algorithms which have been applied to many different types of combinatorial optimization problems [32], including those in business. A GA models ‘survival of the <sup>fi</sup>ttest’ by starting with an initial population of individuals (chromosomes), each representing one potential solution to the given problem. Similar to natural selection, new generations of individuals are iteratively created from this initial population via the application of the genetic operators reproduction, crossover, and mutation; new populations are chosen from both old and new chromosomes according to a prede<sup>fi</sup>ned fitness function and elitism strategy. Although genetic algorithms do not guarantee optimality, they have become a popular solution technique for combinatorial optimization problems in many disciplines because of their perceived pro<sup>fi</sup>ciency in covering large portions of a search space and their relative ease of implementation [32]. For these reasons we use genetic algorithms as the methodology for near-optimal countermeasure portfolio selection.

![](/api/attachments/53X9G46G/fulltext/images/44d4a0aaf35e8302acb9dc46e585564653cbd97439fa7ebc1931122534af02c1.jpg)  
Fig. 2. Steps in calculating (fuzzy) system risk.

We implement crossover via a roulette wheel mechanism. First a crossover location is randomly chosen between two genes on the chromosome. For example, if the chromosome has 20 genes and a location of 7 is chosen, this creates a “head” (genes 1–7 inclusive), and a “tail” (genes 8–20 inclusive). Then two “parent” chromosomes are chosen from the entire population in proportion to their <sup>fi</sup>tness. Finally, two children are created by forming one child with the head of the <sup>fi</sup>rst parent and tail of the second, and the second child as the head of the second parent and tail of the <sup>fi</sup>rst. The process is repeated until feasible (in a budgetary sense) offspring are produced.

Whenever mutation is invoked, which occurs with a probability of 0.05, two genes are randomly chosen from all genes on the chromosome and are swapped, as long as feasibility is not violated.

There are two components of feasibility for mutation: budgetary (as with crossover), and a priori level-speci<sup>fi</sup>cation constraints. We allow for management to specify a priori that particular countermeasures represented by genes of their choosing can be set and maintained at a desired level. Consequently, these genes cannot be mutated; the code disallows mutations of a priori-speci<sup>fi</sup>ed genes.

Reproduction of a current population occurs by dividing the population into two groups through the speci<sup>fi</sup>cation of an elite percentage. For example, a population of size 28 with an elite percentage of 25 would segment the population into 7 elite members and 21 non-elite members. The elite members are the <sup>fi</sup>ttest of the current population and are maintained and placed directly into the next generation's population. The non-elite members are replaced in the next generation by children of the entire population. So in the case above, the 21 non-elite members would be replaced in the next generation by 21 children of the entire population; these children would be created from the 28 members of the current population using crossover and mutation, as explained above. We have provided only a basic description of the GA process; the interested reader may <sup>fi</sup>nd a more thorough account in Aytug, et al. [2], Dumitrescu, et al. [14], and Goldberg [18].

Some DSS implementation details are shown in Fig. 3. The upper box is the GA Initializer, whereas the bottom box illustrates the GA New Solution Generator. The GA Initializer is called <sup>fi</sup>rst, and when <sup>fi</sup>nished, calls the New Solution Generator, where an answer is obtained.

![](/api/attachments/53X9G46G/fulltext/images/4411ff14e5447b0f0c6f8f6b9be3a47ee9b8fdcf343dd798ae61b51c5de7a63c.jpg)  
Fig. 3. The DSS model base optimization module.

We code each possible set of managerial control-level choices as a group of genes on a chromosome; the chromosome is the basic decision unit in our system. For example, if we had 20 controls to set, and wanted to set the <sup>fi</sup>rst ten to level 2 and the last ten off, then the chromosome to represent these choices would be a string of ten “2”s followed by ten “0”s. This particular chromosome has a fuzzy risk associated with those choices as explained in Section 2.2.1.

Before the GA/DSS process can begin, each chromosome's fitness value must be determined, which is a single number representing the “goodness” or “badness” associated with the set of decisions represented by the chromosome. It is this functional value that is compared among chromosomes to decide which solutions to keep and which to discard, as the GA controller works toward optimality.

Possible choices for a <sup>fi</sup>tness function include the expected overall system risk, or the system's incremental risk, or the total risk that exceeds a speci<sup>fi</sup>ed cutoff value. In order to measure the <sup>fi</sup>tness of a particular fuzzy risk pro<sup>fi</sup>le, we need to reduce the fuzzy set to a single crisp number which may be easily used for decision making as a ranking or threshold value. Within the literature, the common method for this transformation is called “defuzzi<sup>fi</sup>cation.” Defuzzi<sup>fi</sup>cation is de<sup>fi</sup>ned as a mapping of a fuzzy set to an element or elements of the universe considered signi<sup>fi</sup>cant with respect to the set [33]. While there are numerous defuzzi<sup>fi</sup>cation methods which have been suggested, including the maximum membership and mean of maximum membership methods, the most popular method is the centroid, or center of mass, of the fuzzy set [22][27][33]. Karnik and Mendel [22] assert that we may view the centroid of a fuzzy logic system as analogous, but not equal to, the mean of a probability density function.

Karnik and Mendel [22] de<sup>fi</sup>ne the centroid of a fuzzy set A, whose domain $x \in X$ is discretized into N points $x _ { 1 } , x _ { 2 } , . . . , x _ { N } ,$ as

$$
C _ {A} = \sum_ {i = 1} ^ {N} x i \mu_ {A} (x _ {i}) / \sum_ {i = 1} ^ {N} \mu_ {A} (x _ {i})\tag{5}
$$

where $\mu _ { A } ( x _ { i } )$ is the membership in set A of the domain value $x _ { i \cdot }$ For continuous valued sets, the sums in the centroid calculation are replaced with integrals. While the centroid is the most commonly used defuzzi<sup>fi</sup>cation metric, other measures such as fuzzy variance-atrisk [11] could alternatively be used.

The GA heuristic optimization process begins with the upper (GA Initializer) box in Fig. 3. This box generates a set of N feasible solutions or chromosomes that are used as the initial population; some of these are produced heuristically while others are obtained randomly. Often, we will have a current scenario that can be included as one of the initial solutions; this can be supplemented with simple heuristics, if other feasible solutions are not available. In general, one may formulate heuristics by calculating the risk that a particular threat against an asset poses, and then forming the ratio of that risk to (say) the cost of implementing a particular countermeasure that mitigates it. Sorting all such ratios for all relevant countermeasures in descending order and then implementing countermeasures until the budget is spent will provide some indication of goodness.

In addition to well-thought-out heuristic solutions, the initial population consists of randomly generated chromosomes (“Random” step of the Initializer). The purpose here is to provide “genetic newness,” so that when existing chromosomes are crossed-over with the random ones, new chromosomes will be generated that venture /\* current implementation \*/ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 /\*4 nonrandom heuristics \*/ 2, 2, 1, 2, 2, 1, 1, 1, 1, 2 3, 3, 1, 3, 3, 1, 1, 1, 1, 3 2, 2, 1, 2, 2, 2, 1, 1, 1, 2 3, 1, 1, 3, 3, 3, 1, 1, 1, 3 /\* 15 random heuristics 3, 2, 2, 3, 3, 2, 1, 2, 1, 3 2, 1, 2, 1, 2, 1, 1, 1, 2, 2 1, 3, 2, 3, 2, 2, 3, 2, 1, 2 1, 3, 3, 2, 2, 3, 2, 2, 1, 3 1, 1, 1, 1, 3, 3, 3, 2, 2, 1 1, 3, 2, 2, 2, 1, 1, 1, 3, 3 1,2,2,2,3,3,3.3,1,2 1, 1, 3, 1, 2, 1, 3, 2, 2, 1 3, 3, 2, 2, 3, 1, 1, 1, 1, 3 1, 1, 3, 2, 2, 1, 2, 2, 2, 2 2, 2, 2, 3, 3, 2, 1, 3, 1, 2 1,3,2,1,3,1,1,3,3,3 1, 2, 2, 2, 2, 2, 2, 3, 1, 2 1, 2, 3, 3, 2, 3, 1, 1, 3, 3 1,2,2,3,2,2,3,2, 1, 2 /\* additional costs -- 10 CMs by 3 'on' levels: \*/ /\* ..; (CMj, level 1; CMj, level 2; CMj, level 3; (CMj+1, level 1; CMj+1, level 2; CMj+1, level 3; )); . 0.0, 200.0, 250.0, 0.0, 66.7, 100.0, 0.0, 16.7, 25.0, 0.0, 20.0, 25.0, 0.0, 0.7, 1.0 0.0, 16.7, 25.0, 0.0, 166.7, 250.0,0.0, 20.0, 25.0, 0.0, 200.0, 250, 0.0, 66.7, 100.0 /\* budget \*/ 500

a  
EXAMPLE INDUSTRY DATA: PROFILE FOR COUNTERMEASURE 'PL-4' AGAINST THREAT 'ERRORS AND OMISSIONS

<table><tr><td colspan="6">Threat-Attacking-Asset: Errors and Omissions</td><td colspan="3">Countermeasure PL-4</td></tr><tr><td>#</td><td>Industry</td><td># Systems</td><td>Region</td><td>Reported Rates</td><td>Reported Cost Impact</td><td>Implementation Cost Bucket</td><td>Reported Level</td><td>Max Level</td></tr><tr><td>1</td><td>Manufacturing</td><td>101 - 250</td><td>North America</td><td>Weekly</td><td>Tens of Thousands</td><td>1K</td><td>1</td><td>6</td></tr><tr><td>2</td><td>Manufacturing</td><td>101 - 250</td><td>North America</td><td>Monthly</td><td>Thousands</td><td>1K</td><td>2</td><td>6</td></tr><tr><td>3</td><td>Manufacturing</td><td>101 - 250</td><td>North America</td><td>Weekly</td><td>Tens of Thousands</td><td>1K</td><td>1</td><td>6</td></tr><tr><td>4</td><td>Manufacturing</td><td>101 - 250</td><td>North America</td><td>Weekly</td><td>Tens of Thousands</td><td>1K</td><td>1</td><td>6</td></tr><tr><td>5</td><td>Manufacturing</td><td>101 - 250</td><td>North America</td><td>Monthly</td><td>Thousands</td><td>1K</td><td>1</td><td>6</td></tr><tr><td>6</td><td>Manufacturing</td><td>101 - 250</td><td>North America</td><td>Yearly</td><td>Thousands</td><td>1K</td><td>1</td><td>6</td></tr><tr><td>7</td><td>Manufacturing</td><td>101 - 250</td><td>North America</td><td>Semi-Yearly</td><td>Thousands</td><td>1K</td><td>1</td><td>6</td></tr><tr><td>8</td><td>Manufacturing</td><td>101 - 250</td><td>North America</td><td>Quarterly</td><td>Thousands</td><td>1K</td><td>1</td><td>6</td></tr><tr><td>9</td><td>Manufacturing</td><td>101 - 250</td><td>North America</td><td>Never</td><td>Thousands</td><td>1K</td><td>3</td><td>6</td></tr><tr><td></td><td></td><td></td><td></td><td colspan="4">Survey Responses</td><td></td></tr></table>

b  
EXAMPLE VERIZON BUSINESS COUNTERMEASURE DATA: PERCENT THROUGHPUT FOR CM 'AC-19'

<table><tr><td colspan="3">Countermeasure AC-19</td></tr><tr><td colspan="3">Actual CM &#x27;Percent Through&#x27; for this CM</td></tr><tr><td colspan="3">(ignoring reported level)</td></tr><tr><td>Level</td><td>% Blocked</td><td>% Thru</td></tr><tr><td>0.0</td><td>0.00</td><td>1.00</td></tr><tr><td>0.5</td><td>0.30</td><td>0.70</td></tr><tr><td>1.0</td><td>0.54</td><td>0.46</td></tr><tr><td>1.5</td><td>0.72</td><td>0.28</td></tr><tr><td>2.0</td><td>0.81</td><td>0.19</td></tr><tr><td>2.5</td><td>0.87</td><td>0.13</td></tr><tr><td>3.0</td><td>0.90</td><td>0.10</td></tr></table>

![](/api/attachments/53X9G46G/fulltext/images/7b5429edbc857da9045b086060bcc7e8798cdecc13e901e95b6f9ada2bc56a91.jpg)

c

<table><tr><td>CM\Threat</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>1</td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>3</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr><tr><td>4</td><td>X</td><td></td><td></td><td>X</td><td></td><td>X</td><td>X</td><td></td><td></td><td></td></tr><tr><td>5</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>8</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td></tr><tr><td>9</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr><tr><td>10</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td></tr></table>

Fig. 4. a. Sample industry data. b. Sample Verizon Business furnished expert opinion on countermeasure ineffectiveness. c. Verizon Business furnished countermeasure-threat matrix.

Fig. 5. Start-up population and other initialization data.

into previously unexplored regions of the search space. Of course, the solutions represented by the random chromosomes must be budget feasible.

Note that thus far, the system has generated a total of N feasible chromosomes. However, the <sup>fi</sup>tness of each of these in general will not be known. Consequently, as indicated in the top box of Fig. 3, the algorithm of Fig. 2 is called N times, and the fuzzy risk is determined for each chromosome. The “New Solution Generator” may now be called.

The entire population of initial chromosomes is passed to the GA New Solution Generator, where the current population is divided into two groups based on the elitism percentage. As indicated in Fig. 3, the elite group migrates into the next generation as is; no <sup>fi</sup>tness function values need be determined for these chromosomes, as they are already known. However, the slots not <sup>fi</sup>lled by the elite chromosomes must be repopulated through crossover and mutation, as explained above. Once the non-elites have been replaced with new children, the (new) children must obtain <sup>fi</sup>tness values. Thus, as indicated in Fig. 3, the algorithm of Fig. 2 is called to calculate the fuzzy risk set and a defuzzi<sup>fi</sup>ed <sup>fi</sup>tness function value for the non-elite members. Once all <sup>fi</sup>tness values are known, a new population has been constituted, still of the same size.

With each cycle (or each new population), the system determines whether to terminate or iterate based upon a priori speci<sup>fi</sup>ed criteria. Various criteria may be utilized; for example, stop either (1) when a prede<sup>fi</sup>ned <sup>fi</sup>tness value is reached, (2) when there is no <sup>fi</sup>tness function improvement after a pre-stipulated number of consecutive iterations, (3) when the number of unique solutions reaches a prescribed <sup>fi</sup>gure, or (4) when the number of crossover attempts exceeds a given value. In this system we use criteria (3) and (4). If during any particular iteration the termination criteria are not met, then the population is passed back to the “Divide population into two groups…” box as indicated in Fig. 3, whereby the process continues. Further explanation is provided in the next section.

## 3. Industry example

The purpose of this section is to illustrate the procedure for determining a preferred portfolio of countermeasures within a given budget. We use the industry data collected by Verizon Business to show the power of the DSS and to illustrate the questions that can be answered.

## 3.1. Model

From the survey data of 349 organizations, we selected manufacturing companies with between 101 and 250 computer systems; nine <sup>fi</sup>rms were obtained as shown in Fig. 4a. Because many of the 349 <sup>fi</sup>rms were new to the data collection procedure and especially to the notion of inferring costs due to IT security-induced losses, we decided to mitigate any possible effect of outliers by forming a hypothetical, “average” small manufacturing <sup>fi</sup>rm. That is, using the nine selected companies, we created an average <sup>fi</sup>rm pro<sup>fi</sup>le whose security parameters were the fuzzy average (i.e. fuzzy sum/9) of these data. Note that in crafting a prototypical <sup>fi</sup>rm we were in no way suggesting that <sup>fi</sup>rms need to determine the behavior of industry competitors to use this procedure, or that inferences may be made to other <sup>fi</sup>rms from the results obtained. Our purpose here was only to provide an illustrative example of our procedure with representative, industry data.

The <sup>fi</sup>rst step in the process was to prepare data for use by arranging it into the formats signi<sup>fi</sup>ed in Figs. 4 and 5. Fig. 4 shows samples of the various data. Industry sample data are shown in Fig. 4a and include (1) reported rates for a particular threat attacking an asset; (2) the reported cost impact per successful attack; (3) the implementation cost of employing a particular countermeasure against this threat; and (4) the current level of implementation of the countermeasure on a 6- point scale. Note that there are similar tables of bucket data for every other set of threats and countermeasures.

![](/api/attachments/53X9G46G/fulltext/images/901c7295deede8c5dac29d4a0ac9a0bdfc5e5a5d05f4e97b4d8f9e6359fa8129.jpg)  
Fig. 6. Building a fuzzy set from alpha-cut data

<table><tr><td colspan="2"></td><td colspan="10">Managers&#x27; String position</td><td></td></tr><tr><td>Iteration</td><td>Centroid</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>TOTAL EXPENDITURES ($K)</td></tr><tr><td>1</td><td>1775</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>2216.8</td></tr><tr><td>2</td><td>633</td><td>3</td><td>1</td><td>1</td><td>3</td><td>3</td><td>3</td><td>1</td><td>1</td><td>1</td><td>3</td><td>1074.8</td></tr><tr><td>3</td><td>489</td><td>1</td><td>1</td><td>2</td><td>3</td><td>3</td><td>3</td><td>1</td><td>1</td><td>1</td><td>3</td><td>930.8</td></tr><tr><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>450</td><td>1</td><td>1</td><td>1</td><td>3</td><td>3</td><td>1</td><td>1</td><td>1</td><td>1</td><td>3</td><td>891.8</td></tr></table>

Fig. 7. Progress made by the model base of the DSS (see Fig. 2) toward an improved solution.

Fig. 4b and c is derived from the countermeasure data supplied by the Verizon Business experts. Fig. 4b shows the Percent Ineffectiveness for a given countermeasure (rescaled to three levels). The <sup>fi</sup>gure indicates that if the control is turned off, it is 100% ineffective, i.e., all threats will get through; conversely, if the control is fully implemented, only 10% of the threats will succeed. There is a similar curve generated for every control in this study. Fig. 4c is a matrix furnished by Verizon Business demonstrating the possible array of countermeasures that may be employed against each threat. In this example problem we examine the ten most effective countermeasures that may be arrayed against the ten most devastating threats-attackingassets as seen in the data.

Fig. 5 shows the three categories of data necessary to implement the Genetic Algorithm risk minimization algorithm. Starting at the bottom of that <sup>fi</sup>gure, the <sup>fi</sup>rm's budget is speci<sup>fi</sup>ed; then the costs of every countermeasure at every level are given. The top of Fig. 5 contains the so-called set of “Manager's Strings” for initialization; each string is of length 10, with a separate slot for speci<sup>fi</sup>cation of the level of each of the 10 countermeasures management is considering. (The <sup>fi</sup>rst position on the string represents the <sup>fi</sup>rst countermeasure; the second position is for the second countermeasure, etc.) For example, the <sup>fi</sup>rst manager's string in Fig. 5 is the <sup>fi</sup>rm's current implementation, in which every control is set to the level 1. In GA parlance, each manager's string is called a chromosome.

As suggested by Fig. 3, the GA must be initialized to a set of chromosomes that span the space of feasible possible solutions. We generate this set (in this case of size 20) by including the current solution. Four chromosomes obtained via heuristics, and the generation of 15 random chromosomes. All 20 chromosomes are produced so that they are budget feasible (with the current solution being the “do-nothing” alternative). As mentioned in Section 2.2.2, the heuristics are generated based on the ratio of risk reduction per control dollar expended. Since the total system risk associated with each string is unknown, that risk must be calculated for each chromosome according to the algorithm given in Fig. 2 (and Appendix A). We call the total system risk for each chromosome its fitness.

In order to calculate this risk, several computations must be carried out. First, every “bucket” of categorical data stored in the MBMS of the DSS must be converted into a fuzzy set. Then the risk/<sup>fi</sup>tness for each chromosome can be determined; recall that this is the total system risk given the countermeasures employed against each threat as indicated by the 10 numbers on the chromosome. This calculation involves the operations of extended multiplication and addition, which invokes the alpha-cut process described in Section 2.2.1. An example set of 11 alpha-cuts (0.0 to 1.0 in steps of 0.1) cutting across both sides of the threat ‘errors and omissions’ together with the resulting fuzzy set is shown in Fig. 6.

![](/api/attachments/53X9G46G/fulltext/images/d8add9836ab2596dd0d68e2c0bec58203450ca931ad02ff6f2686d442d51d983.jpg)  
Fig. 8. Overall Firm IT Risk Pro<sup>fi</sup>le (includes cost of implemented countermeasures).

Examination of the chromosome representing the <sup>fi</sup>rm's current countermeasure posture indicates the <sup>fi</sup>rm is currently facing a system risk of \$1775K. With a current countermeasure outlay of \$441.8K, the total is found to be \$2216.8K. This completes the GA Initialization, indicated at the top of Fig. 3. At this point, 20 feasible chromosomes exist, each representing a within-budget set of 10 chromosome settings and a <sup>fi</sup>tness value. To begin the search for better solutions, we next run the GA New Solution Generator from Fig. 3.

The <sup>fi</sup>rst step in this process is to sort all 20 chromosomes in the population by <sup>fi</sup>tness function. The best <sup>fi</sup>ve chromosomes (i.e., the 25% that are minimum cost) are declared to be elite and are passed unaltered to the “Terminate?” decision box. The remaining 15 chromosomes are “non-elite” and are candidates for improvement. The process of crossover is performed, whereby new chromosomes are formed by dividing each of the 15 non-elite chromosomes into a head and a tail and randomly forming new chromosomes. Those chromosomes that are budget infeasible are discarded and replaced with a different randomly generated, feasible chromosome. The new set of 15 non-elite population members is combined with the 5 elite members to constitute a new population. At the “Terminate?” decision box, termination conditions are checked. The process repeats until the termination conditions are ful<sup>fi</sup>lled.

An important issue is the computational feasibility of our approach. The solution strings we have tried on various problems (some not reported in this work) have all been of length 20 or less. We have used this as an upper bound not because of computational issues, but because it is unlikely that managers would be considering changing more than 20 controls at any one time. Also, the discovery of the near-optimal solution by the GA algorithm is aided by including the current solution as one of the starting populations. Firms have budgets and thus cannot normally deviate in huge increments. The current solution thus gives the GA a good chance of <sup>fi</sup>nding a satisfactory solution. Additionally the inclusion of good starting solutions identi<sup>fi</sup>ed by heuristics is an important key. Our DSS starts with <sup>fi</sup>ve reasonable solutions, based on the current solution and four others found through a simple greedy procedure by looking at the ratio of risk reduction per dollar spent on CM implementation. As a result of the computational simplicity of these procedures, all of the attempted problems have run in less than ten seconds on a standard desktop computer.

## 4. Results

Fig. 7 provides the progress made by the GA before it terminates after 15 iterations. That <sup>fi</sup>gure shows that the centroid of the minimum risk plus control cost is \$891.8K. The fuzzy set for this <sup>fi</sup>nal risk is given in Fig. 8, which indicates a range of risk and control cost from \$583.4K to \$1443.9K. Fig. 8 also shows that the risk is skewed to the low side. This informs that belief is higher for small values of risk, but that there is a “tail” of high risk that is thought possible.

The following details are available from the DSS, although they are not shown in Fig. 8. The countermeasures against insider abuse of access, data compromise, and lost or stolen physical resources should be left at present levels. CM4 should be fully implemented at level 3, and it will act against malicious code infection, insider misuse of resources, denial of service attacks, and network outage, Also, CM5 should be turned fully on against errors and omissions, and the set of practices represented by CM10 should be set at level 3 to mitigate against unauthorized system access or modi<sup>fi</sup>cation, and social engineering.

These actions lead to a reduction in risk from \$1775K to \$324K at a (total) control-implementation cost of \$567.8K. This 2.5-fold reduction in risk-based total is achieved at an additional controlimplementation expenditure of only \$126K.

Further analysis could be made at this point, including point estimate scenarios adapted from the categorical data. Note that point estimate runs may be made by inputting the fuzzy set corresponding to a constant. If point estimates are made in this manner from the categorical data, then the <sup>fi</sup>nal risk will depend on which point in the bucket is taken to be correct. If the lower bound of each fuzzy-set estimate is utilized, the optimal solution is to continue to implement the <sup>fi</sup>rm's current solution, which is to add no additional countermeasures; the risk would be estimated to be only \$91K. If the upper bound of each fuzzy set is taken as the point estimate, the risk swells to \$1022K, with an optimal strategy being to increase CMs 4, 5, and 10 to their maximal level. We believe either point estimate answer to be inadequate (and perhaps dangerous). The truth, we think, lies in the fact that the true risk faced by the <sup>fi</sup>rm is somewhere within that range; our fuzzy-set answer says that with a risk plus control cost of \$450K, the <sup>fi</sup>rm faces an equal belief that the expected sum will be below that value or will be above it. Again note that the \$450K answers the DSS obtained is not at the midpoint of the lower-bound/ upper-bound range. This is because some of the input fuzzy sets are skewed. This emphasizes the point that just choosing the midpoint of a bucket as a point estimate will not necessarily give the best answer. The centroid or fulcrum of the fuzzy set, that point which balances the area under the fuzzy-set curve below it against that above it, is arguably a better choice—taken together with the upper and lower bounds as additional information. While the categories or buckets provide a comfortable way for companies to express their knowledge about threats and assets, we recognize that if the categories or bucket sizes become too large then the results will be of little use. But as long as the category sizes are reasonable, the fuzzy set provides information not only about the risk with the greatest associated belief, but also best and worst case belief bounds as well.

## 5. Conclusions

Security planning involves implementing the most effective countermeasures to reduce the particular threats that face the <sup>fi</sup>rm. However, both the level of threats and the effectiveness of countermeasures against those threats are dif<sup>fi</sup>cult to measure and quantify. The contribution of this paper has been the development of a decision support system that explicitly recognizes that lack of precision by calculating system risk for the case when threats rates, countermeasure costs, and asset losses are uncertain. Managers may employ this system to plan intelligently which countermeasures to employ to meet a speci<sup>fi</sup>ed budget, while characterizing the range of risks to the company. This system should be welcomed by managers who have argued that they do not know which countermeasures to expend funds on and how much good such expenditures will do them [3]. The system allows the speci<sup>fi</sup>cation of model inputs in “buckets” to meet the request of managers to express data at a level of signi<sup>fi</sup>cance they can believe.

An example based on real data in the manufacturing sector was provided that, based on the companies' beliefs as to threats and losses, reduced the current level of risk by \$1.3 million, while increasing countermeasure expenditures by only \$126K. Of course, managers who are convinced they have “better” data may express any inputs they wish either in smaller buckets or even as <sup>fi</sup>rm constants—the system allows this. The range of risk will be appropriately reduced.

Appendix A. The mathematical formulation of overall system risk

![](/api/attachments/53X9G46G/fulltext/images/295b194e8672766d10a539bb522888cbad39ab14f8551493e94f6d156561df25.jpg)

Legend:

Let R= total system rıśk, and

μw(x) for asset i, fuzzy membership for linguistic variable W over W's defined range of membership

Subscript notation:

TA Threats attacking Assets

STA Surviving Threats attacking Assets

LLoss (in \$) due to one attack of threat-attacking-asset i

LSTA Loss (in \$) due to Surviving Threats attacking Assets

CM: implementation efficiencies for CounterMeasures

S implementation inefficiencies for countermeasures (i.e., Survival fractions)

## References

[1] C.J. Alberts, A.J. Dorofee, Managing Information Security Risks: The OCTAVE Approach, Addison Wesley Professional, 2002.

[2] H. Aytug, M. Khouja, F.E. Vergara, Use of genetic algorithms to solve production and operations management problems: a review, International Journal of Production Research 41 (2003) 3955–4099.

[3] W.H. Baker, L.P. Rees, P.S. Tippett, Necessary measures: metric-driven information security risk assessment and decision making, Communications of the ACM 50 (10) (October 2007) 101–106.

[4] W.H. Baker, L. Wallace, Is information security under control? IEEE Security & Privacy (2007) 24–328 January/February 2007.

[5] J.E. Beauregard, Modeling Information Assurance, Master's Thesis, Air Force Institute of Technology (2001).

[6] S. Berinato, The State of Information Security 2003, CIO Magazine 17 (2) (2003) 1–3.

[7] S. Bistarelli, F. Fioravanti, P. Peretti, Using CP-nets as a guide for countermeasure selection, Proceedings of the 2007 ACM Symposium on Applied Computing (Seoul, Korea, 2007), 2007, pp. 300–304.

[8] D. Brewer, Risk assessment models and evolving approaches, http://www. gammassl.co.uk/topics/IAAC.htm20068(accessed December 22, 2006).

[9] D.L. Buckshaw, G.S. Parnell, W.L. Unkenholz, D.L. Parks, J.M. Wallner, O.S. Saydjari Mission oriented risk and design analysis of critical information systems, Military Operations Research 10 (2) (2005) 19–38

[10] H. Cavusoglu, S. Raghunathan, H. Cavusoglu, Con<sup>fi</sup>guration of and interaction between information security technologies: the case of <sup>fi</sup>rewalls and intrusion detection systems, Information Systems Research 20 (2009) 198–217

[11] U. Cherubini, G. Della Lunga, Fuzzy value-at-risk: accounting for market liquidity Economic Notes by Banca Monte dei Pascha di Siena SpA 30 (2) (2001) 293–312

[12] J.K. Deane, C.T. Ragsdale, T.R. Rakes, L.P. Rees, Managing supply chain risk and disruption from IT security incidents, Operations Management Research 2 (1) (2009) 4–12.

[13] W.M. Dong, F.S. Wong, Fuzzy weighted averages and implementation of the extension principle, Fuzzy Sets and Systems 21 (1987) 183–199.

[14] D. Dumitrescu, B. Lazzerini, L.C. Jain, A. Dumitrescu, Evolutionary Computation, CRC Press LLC, Boca Raton, FL, 2000.

[15] M. Egan, The Executive Guide to Information Security, Symantec Press Indianapolis, IN, 2005.

[16] Elsevier, Decision Support Systems, http://www.sciencedirect.com/science/journal/01679236, accessed February 13, 2010.

[17] GAO/AIMD-00–33, Information Security Risk Assessment: Practices of Leading Organizations (United States General Accounting Of<sup>fi</sup>ce, 1999).

[18] D.E. Goldberg, Genetic Algorithms in Search, Optimization and Machine Learning, Addison-Wesley, Reading, MA, 1989.

[19] K. Haslum, A. Abraham, S. Knapskog, DIPS: a framework for distributed intrusion prediction and prevention using hidden Markov models and online fuzzy risk assessment, Third International Symposium on Information Assurance and Security (Manchester, U.K., 2007), 2007, pp. 183–188.

[20] J. Holland, Adaptation in Natural and Arti<sup>fi</sup>cial Systems: An Introductory Analysis with Applications to Biology, Control, and Arti<sup>fi</sup>cial Intelligence, University of Michigan Press, Ann Arbor, 1975.

[21] IDC, Worldwide and U.S. security services 2006–2010 forecast, http://www.idc. com/getdoc.jsp?containerId=200926 (accessed December 22, 2006).

[22] N. Karnik, J. Mendel, Centroid of a type-2 fuzzy set, Information Sciences 132 (2001) 195–220.

[23] E. Kujawski, G.A. Miller, Quantitative risk-based analysis for military counterterrorism systems, Systems Engineering 10 (4) (2007) 273–289.

[24] C. Lin, P. Hsieh, A fuzzy decision support systems for strategic portfolio management, Decision Support Systems 38 (2004) 383–398.

[25] Lohr, Steve, The New York Times, Companies Fight Endless War Against Computer Attacks, January 18, 2010, http://www.nytimes.com/2010/01/18/technology/ internet/18defend.html, accessed February 14, 2010.

[26] E. Ngai, F. Wat, Fuzzy decision support system for risk analysis in E-commerce development, Decision Support Systems 40 (2005) 235–255.

[27] N. P<sup>fl</sup>uger, J. Yen, R. Langari, A defuzzi<sup>fi</sup>cation strategy for a fuzzy controller employing prohibitive information in command formulation, Proceedings of the IEEE International Conference on Fuzzy Systems (San Diego, CA, 1992), 1992, pp. 717–723.

[28] PITAC, Report to the President - Cyber Security: A Crisis of Prioritization (President's Information Technology Advisory Council, National Coordination Of<sup>fi</sup>ce for Information Technology Research and Development, Arlington, VA, 2005).

[29] G.V. Prasad, Y. Dhanalakshmi, V.V. Kumar, I.R. Babu, Modeling an intrusion detection system using data mining and genetic algorithms based on fuzzy logic, International Journal of Computer Science and Network Security 8 (7) (2008) 319–325.

[30] S. Radha, M.S. Jayapriya, Security enhancement in the NTP protocol using fuzzy techniques, International Workshop on Wireless Ad-hoc Networks (London, 2005), 2005.

[31] T.R. Rakes, L.P. Rees, J.K. Deane, Fuzzy representations of information-technology security threat-countermeasure effectiveness. Proceedings of the SEINFORMS Meeting (Myrtle Beach, SC, 2006), 2006, pp. 428–437.

[32] C.R. Reeves, Modern Heuristic Techniques for Combinatorial Problems, Blackwell Scienti<sup>fi</sup>c, Oxford, 1993.

[33] T. Runkler, Selection of appropriate defuzzi<sup>fi</sup>cation methods using application speci<sup>fi</sup>c properties, IEEE Transactions on Fuzzy Systems 5 (1) (1997) 72–79.

[34] A.S. Sodiya, S.A. Onashoga, B.A. Oladunjoye, Threat modeling using a fuzzy logic paradigm, Issues in Informing Science and Information Technology 4 (2007) 53–61.

[35] S. Song, K. Hwang, M. Macwan, Fuzzy trust integration for security enforcement in grid computing, IFIP International Symposium on Network and Parallel Computing (Wuhan, China, 2004), 2004.

[36] B. Van de Walle, A. Rutkowski, A fuzzy decision support system for IT service continuity threat assessment, Decision Support Systems 42 (2006) 1931–1943.

[37] L.A. Zadeh, Fuzzy sets, Information and Control 8 (1965) 338–353.

[38] L.A. Zadeh, Outline of a new approach to the analysis of complex systems and decision processes, Transactions on Systems, Man and Cybernetics, SMC-3, 1973, pp. 28–44.

[39] L.A. Zadeh, The concept of a linguistic variable and its application to approximate reasoning, Information Science 8 (1975) 199–249.

[40] L.A. Zadeh, Fuzzy sets as a basis for a theory of possibility, Fuzzy Sets and Systems 1 (1978) 3–28.

[41] L.A. Zadeh, A theory of approximate reasoning, Machine Intelligence 9 (1979) 149–194.

[42] D. Zhao, J. Wang, J. Wu, J. Ma, Using fuzzy logic and entropy theory to risk assessment of the information security, Proceedings of the Fourth International Conference on Machine Learning and Cybernetics, (Guangzhou, China, 2005) 2005, pp. 2448–2453.

![](/api/attachments/53X9G46G/fulltext/images/2e48adec58d2d8c5ed01ee3c6e9f07341a1db1f085b1a5d5e1cef34ee6a77dff.jpg)

Loren Paul Rees is Andersen/Andersen Consulting Alumni Professor in Information for Management at Virginia Tech. He was formerly a Member of the Technical Staff at Bell Telephone Laboratories. His research interests include simulation optimization, wireless telecommunications, IT security, and software agents, and he has published in such journals as Decision Support Systems, Naval Research Logistics, Transportation Research, IIE Transactions, Decision Sciences, Communications of the ACM, and others. He is a member of the American Association for Arti<sup>fi</sup>cial Intelligence, The Institute for Opera tions Research and the Management Sciences, and the Decision Sciences Institute. He received his Ph.D. in Industrial and Systems Engineering from the Georgia Institute of Technology.

![](/api/attachments/53X9G46G/fulltext/images/51639a70cbb97ce225db58c5793bbfc18fa4f5bff6f4164e8f1a9fc3a7f4380a.jpg)

Jason K. Deane is Assistant Professor of Business Information Technology in the Pamplin College of Business at Virginia Tech. He received a Ph.D. in Decision and Information Sciences from the University of Florida, and an M.B.A. and B.S. in Business Administration from Virginia Tech. His current research interests are in the areas of arti<sup>fi</sup>cial intelligence, computer aided decision support systems, information system security, large scale optimization and information retrieval. He has published in such journals as Decision Support Systems, Annals of Operations Research, Information Technology and Management, International Journal of Physical Distribution and Logistics Management, Operations Management Research, and others.

![](/api/attachments/53X9G46G/fulltext/images/217d052aac8d15fdbc06233acc4d2388ce7ddef438bf0fb916aa561be7cddfd8.jpg)

Terry R. Rakes is William C. and Alix C. Houchens Professor of Information Technology at Virginia Tech. His research interests are in wireless telecommunications, software agents, and the application of decision support and arti<sup>fi</sup>cial intelligence methodologies to problems in information systems. He has published in such journals as Decision Support Systems, Management Science, Decision Sciences, Annals of Operations Research, Operations Research Letters, Information and Management, Journal of Information Science and others. He is a member of the Decision Sciences Institute and The Institute for Operations Research and the Management Sciences. He received the Ph.D. in Management Science from Virginia Polytechnic Institute and State University.

![](/api/attachments/53X9G46G/fulltext/images/c724bbbe81a87d7e19bc04e638c8c2c8d0dca73e6a01172f82ffa54f7a628429.jpg)

Wade Baker is the director of Risk Intelligence for Verizon Business, where he oversees the collection, analysis, and distribution of all internal and external data relevant to better understanding and managing information risk. Baker has a master's degree in information technology from the University of Southern Mississippi and is in the <sup>fi</sup>nal phase of obtaining his Ph.D. in Business Information Technology at Virginia Tech. He has published in Communications of the ACM, IEEE Security & Privacy, the International Journal of Electronic Marketing and Retailing, and others.
