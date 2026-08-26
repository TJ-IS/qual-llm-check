---
otero_id: 7642
otero_key: "7KWJMYZQ"
title: "Socially optimal IT investment for cybersecurity"
authors: "Jomon A. Paul; Xinfang (Jocelyn) Wang"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.05.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Socially optimal IT investment for cybersecurity

Jomon A. Paul<sup>a,⁎</sup>, Xinfang (Jocelyn) Wang

![](/api/attachments/7KWJMYZQ/fulltext/images/daacf176273e41f049be3874ef8b5a26e514ac853665a2524f1946b2f773398f.jpg)

<sup>a</sup> Department of Economics, Finance, & Quantitative Analysis, Kennesaw State University, 560 Parliament Garden Way, Kennesaw, GA 30144, United States of America <sup>b</sup> Department of Logistics and Supply Chain Management, College of Business Administration, Georgia Southern University, Statesboro, GA 30460, United States of America

## A R T I C L E I N F O

Keywords: Cybersecurity Social cost Prevention safeguards Detection & containment safeguards Robust optimization

## A B S T R A C T

This paper uses the concept of social cost, comprised of private and externality costs, to capture the time-elapsed economic value of losses inflicted on users of a service under cyberattack. Our approach offers a holistic treatment of cybersecurity that not only employs prevention as a first defense but also uses detection & containment safeguards to mitigate the damage of successful attacks. It examines the optimal balance between these two safeguards under three sources of uncertainty through a robust optimization model with the help of distribution-free ellipsoidal uncertainty sets to ease the challenge of providing exact estimates for uncertain input. Our method is more appropriate than stochastic programming and other competing RO methods in addressing cybersecurity parameter uncertainty. Tested on a case study, results from 25 deterministic scenarios first reveal a strong resource-allocation preference for the prevention safeguard, but when the budget constraint is relaxed, preference shifts toward the containment & detection safeguard. Results from 54 robust test instances indicate that, for the three sources of uncertainty, the adjusted efectiveness of the prevention safeguard has the greatest impact on both social cost and the optimal configuration of safeguards. Our analysis points to some serious flaws in the existing cybersecurity framework's reliance on prevention and provides decisionmakers with urgently needed guidelines.

## 1. Introduction

Digital advancements related to computer information systems have revolutionized the management and operational eficiency of critical infrastructure access and use [1], but they come at a cost. The White House [2] describes cyberattacks as “among the gravest national security dangers,” and former FBI Director James Comey [3] termed them “an enormous and an exponentially growing threat.” The data breache at Yahoo in 2014 involving 3 billion user accounts, LinkedIn in 2016 involving 167 million accounts, and Equifax in 2017 involving 145 million users show the problem's magnitude and financial consequences [4]. Note that Verizon slashed \$350 million from its ofer to buy Yahoo after the 2014 breach [5]. While private firms account for nearly 85% of the critical infrastructure, public institutions have also been targets. In March 2018, the city of Atlanta sufered a ransomware attack, with government data as well as several city services at stake [6].

Review of cybersecurity budgets confirms a growing anxiety. A survey of 735 IT and IT-security practitioners found that before the 2013 Target breach, a mere 13% of respondents felt senior management was extremely concerned about such a threat, but afterward, the number jumped to 55% [7], and 61% of organizations increased their security budgets, on average, by 34% in 2014 [8]. In the wake of the Equifax hack, FICO immediately invested another \$10 million in cybersecurity [9].

These incidents confront private and public sector institutions with two vital questions: How much should be invested in cybersecurity activities, and what type of investments are socially optimal? They have been the focus of significant attention from government (e.g., Cybersecurity and Infrastructure Protection Subcommittee<sup>1</sup> and Council of Economic Advisers), academic research (e.g., [1,10–13]), and executives (e.g., Boardroom Cyberwatch Survey<sup>2</sup>) [14]. Prevention has been the preferred method of fighting cyberbreaches [15], but alone, it simply can't keep up with their proliferation and increasing sophistication. In November 2016, the number of attacks on individual UK companies' firewalls averaged 1000 per day [16]. A prevention safeguard is efective in blocking cyberthreats but cannot detect and contain threats that pass the defenses.

However, companies reluctant to admit their vulnerability may dangerously downplay the role of detection and containment safeguards. Although 71% of respondents from financial services firms believe detection and containment technology is the most promising approach to minimize threats, only 45% have implemented response procedures [17]. This disparity partially explains why most companies take at least six months to detect data breaches, causing serious and, in many cases, irreparable damage. Recognizing the shortfall, industry leaders and government agencies are now advocating for both prevention and detection & containment safeguards in the cybersecurity portfolio. For instance, the National Institute of Standards and Technology recommends detection, response, and recovery as part of a cybersecurity framework [18]. In a serious gap, academic research on optimal allocation of safeguards has focused on prevention (e.g., [19,20]), failing to address the critical question of detecting and con taining successful breaches.

Our paper examines this growing problem, factoring in social cost related to cybercrime and lack of suficient data. First, our study uses social cost, which incorporates both private and externality costs, as the objective function and it captures the duration of an attack. In economics, direct financial losses from cyberattacks are considered private costs because the participant (i.e., firm) incurs them. However, an often neglected aspect of cyberattack is negative externalities borne by users - other firms or, more commonly, individual consumers - of the services under attack. For example, the Equifax breach included names, ad dresses, and Social Security numbers, which hackers can use to “file taxes, obtain drivers' licenses, run up medical bills, or commit crimes,” the Identity Theft Resource Center (ITRC) reported. According to its 2016 survey, 30% of victims had to seek government assistance, and 31% lost their home and were deprived of basic necessities. Clearly, information loss “poses serious problems for consumers,” as Thomas Hinton, CEO of the American Consumer Council, observed [21]. A Council of Economic Advisers [22] report recommends a socially optimal level of investment that considers both private and externality costs. Failure to include the latter leads to underinvestment in cyber security.

Second, the same report cites insuficient data as another hindrance to cybersecurity investment decisions. It is partly due to firms' reluctance to disclose attack incidents for fear of negative publicity and financial losses. Although more accurate data will become available through stricter government disclosure requirements (e.g., the EU's GDPR and the US SEC's Form 8-K), the current climate poses significant challenges for optimizing cybersecurity investment. To address uncertainty inherited in some key parameters and ease the challenge of providing exact estimates for them, we apply robust optimization with distribution-free uncertainty sets.

The paper proceeds as follows. Section 2 reviews the relevant literature. Section 3 describes the problem and the development of the deterministic model and its robust counterpart. We present our case study, grounded in real-world data, in Section 4. Section 5 discusses the results' managerial and policy implications. We conclude with a reflection on the study's limitations and directions for future research.

## 2. Literature review

Many developed countries view cybersecurity as a national priority [23], and its complexity is growing with our dependence on information, regulations, and the sophistication of threats. To rise to these challenges, researchers have turned to economic analysis and optimi zation models for decisions pertaining to cybersecurity. Our literature review considers work on (a) the economics of resource investment, which includes two streams, one focused exclusively on the private cost to firms and the other on the social costs associated with cyberattacks; and (b) optimal selection of safeguards under uncertainty.

## 2.1. Economics of resource investment

Gordon and Loeb [11] find that under certain sets of assumptions about the relationship between vulnerability and the marginal return of the security investment, the optimal cybersecurity investment may either increase or first increase, then decrease as vulnerability increases. Hausken [24] presents four classes of marginal returns on security investment (decrease; increase then decrease; increase; constancy) and demonstrates that optimal investment is not capped at 1/e. However, using a more general context for the Gordon-Loeb model, Baryshnikov [25] shows that the 1/e rule holds. Similarly, LeLarge [12] shows that a risk-neutral agent does not invest > 37% of the expected loss when security-breach probability functions are log-convex. Wang [13] de velops models for cyberbreach probability as a function of security investment. The general theme is that to optimize total investment levels in cybersecurity, firms should minimize the costs of both cybersecurity investments and breaches, and although these works ofer great theoretical insights into security investments, they lack the functional support decisionmakers need. Our models embody some of their key analyses (e.g., the holistic view of costs of cybersecurity investments and breaches in Wang [13]) but with a pragmatic focus on establishing an optimal IT security strategy for large-scale applications.

The literature on social cost is rich. Campbell et al. [26] find that the economic impact on firms' stock market returns varies by the type of information-security breach, and unlike other breaches, those involving unauthorized access to confidential data cause a highly significant negative market reaction. Cavusoglu et al. [27] confirm this finding. Using game-theoretic analysis, Varian [28] shows how the reliability of component subsystems determine a system's overall reliability. Gordon et al. [29] develop a model to examine the economic welfare implica tions of the information-sharing movement encouraged by the government to promote computer security. They find that firms can attain an optimal level of information security at less cost when they share information, improving total social welfare. In a related paper, Gal-Or and Ghose [30] evaluate how product competition afects information sharing and security technology, finding that economically incentivized information sharing among allies has substantial positive efects on demand. Gordon et al. [1] go on to assess whether government incentives/regulations curb private-sector firms' tendency to underinvest in cybersecurity. They find that success depends on the firms' (a) ability to determine the mix of inputs to optimize cybersecurity and (b) ability and willingness to increase their cybersecurity investments. Romanosky [31] examines the nature and costs of cyberevents to determine whether firms have incentives to improve their security practices and reduce the risk of attack. In a sample of over 12,000 events, an interesting paradox emerged. On the one hand, aggregate rates of events and litigation are more frequent and potentially more expensive for organi zations that collect and use personal information. On the other, the actual cost of these events is less than \$200 K, only a fraction of the millions of dollars commonly cited, and losses due to fraud, theft, corruption, or bad debt outweigh it. In light of this relatively low cost, firms may be investing in the optimal level of security as one of many forms of corporate risk.

## 2.2. Optimal selection of safeguards

Viduto et al. [32] develop a multi-objective optimization model, using the Pareto front to identify solutions (countermeasure portfolio) that maintain a good balance between investment cost and risk. Schil ling and Werners [20] develop a mixed-integer linear programming (MILP) model to eficiently select safeguards to protect IT infrastructures and systems. To address the data limitation in prior related studies, they use a publicly available knowledge base: IT baseline protection catalogues from the German Federal Ofice for Information Security. Both studies operate in a deterministic setting and do not consider uncertainties associated with threat, the efectiveness of countermeasures, and other factors.

Works that incorporate uncertainty include Rakes et al. [33], who develop a model for countermeasure selection based on threat likelihood and then evaluate firm risk for frequent expected losses and worst-case losses that are rare but disastrous. Sawik [34] used a biobjective optimization model, applying the value-at-risk to select security safeguards that minimize both expected and worst-case losses. The sensitivity of the solution is aligned with the risk of high losses from successful attacks, the decisionmaker's attitude toward risk, and their interplay with the budget. While these models capture uncertainty better than their deterministic counterparts, their reliance on scenariospecific data is limiting.

Based on their work with Verizon Business, an IT security-risk consulting service, Rees et al. [35] develop a decision-support system for an organization under cyberattack. It uses distribution-free fuzzy set theory to calculate risk as a function of uncertain threat rates, countermeasure costs, and impacts on assets to search for the best combination of countermeasures. Schilling [19] extends this study to provide decision support that is robust to the uncertainty associated with security threats and remains stable over many planning periods. Following Schilling and Werners [20], it relies on publicly available IT baseline catalogues and mitigates data uncertainty using the concept of relative regret.

Stochastic programming and robust optimization (RO) are the two dominant methods for handling parameter uncertainty in optimization models. Like scenario analysis, stochastic programming models require an exact probability distribution for uncertain parameters, but, as noted by Rees et al. [35], Schilling and Werners [20], and others, data are generally lacking or inconsistent. These models perform poorly when probability distributions are mis-specified. In contrast, RO uses a con cise, distribution-free uncertainty set (e.g., nominal and maximum de viation) to model parameter uncertainty [36,37]. Soyster [38] first developed it for a linear optimization problem where all uncertain parameters assume their worst-case values within a set, which is extremely conservative. El-Ghaoui et al. [39] and Ben-Tal and Nemir ovsky [40,41] develop less conservative RO models by controlling the set of values uncertain parameters could realize. Specifically, Ben-Tal and Nemirovsky [40,41] propose two very tractable uncertainty sets - box and ellipsoid. The former represents a set of linear relations among the uncertain parameters, and the latter, quadratic relations. Bertsima and Sim [42] propose a cardinality-based RO model that captures uncertain parameters by restricting the maximum number that can deviate from their nominal values. While RO has been successfully applied to important problems in operations management, finance, and other areas [37], its application in information security is rare. One exception is Schilling [19], but here, relative regret-based robustness is based on the p-robust metric [43] intended to address across-scenarios uncertainty, not the parameter uncertainty inherent to our study.

## 2.3. Gaps and contributions

Our paper extends the extant literature on optimal selection of safeguards and the economics associated with private costs to firms in three directions. First, in addition to the prevention safeguards modeled in prior studies, we consider detection and containment safeguards in optimizing a countermeasure portfolio. Our holistic treatment of cybersecurity employs prevention as a first defense but also a detection & containment safeguard to mitigate the damage of successful attacks. This comprehensive framework allows us to examine some critical yet neglected questions, such as how to achieve an optimal balance between prevention and detection & containment safeguards.

Second, we model uncertainty in the framework of Ben-Tal and Nemirovsky [40]. It ofers several advantages over stochastic programming and other competing RO methods for addressing parameter uncertainty in cybersecurity. It relieves decisionmakers from having to provide extensive input data that they may not know nor want to commit [19]. Our choice of the uncertainty set, as in other published works (e.g., [44,45]), reflects Ben-Tal and Nemirovsky's [40] ability to capture the uncertainty under study conceptually. Specifically, instead of relaxing over-conservatism by restricting the maximum number of impacted entities [46], it models the uncertainty of each entity and uses an ellipsoid uncertainty set to adjust the degree of conservatism. Unless risk-aversion measures (e.g., [47]) that intensify the computational burden are considered, the stochastic programing model assumes risk neutral decisionmaking, which is inappropriate for cybersecurity where decisionmakers often hedge against the worst-case scenario. RO, by design, features a risk-averse perspective better aligned with cybersecurity.

Last, we capture the time-elapsed economic value of losses from cybercrime by considering the negative externality cost inflicted on users (social cost). Humanitarian logistics measures damage to victims to provide an economic valuation of human sufering (e.g., [48–50]). Section 4 details the estimation of social cost.

## 3. Methodology

## 3.1. Problem statement

A firm that serves clients is likely to face cyberattacks. It can invest in safeguards to prevent them (Fig. 1) and controls (technical and policy-oriented) to detect and contain them. Prevention safeguards reduce the likelihood of an attack, while detection and containment measures speed resolution of a successful attack and reduce net losses. Efectiveness depends on the magnitude of investment; the stronger the security profile, the more able to thwart and detect attacks. The firm's budget afects the number of safeguards employed, but the extent of losses also depends on the type of cyberattack; some are more dificult to prevent and/or more vicious and take longer to resolve. This framework aligns with recent guidelines incorporating detection and containment recommended by agencies such as NIST. Fig. 1 identifies the critical uncertain parameters; Section 3.2 defines them, and 3.3 describes their modeling using a distribution-free uncertainty set.

![](/api/attachments/7KWJMYZQ/fulltext/images/eef795069174b5ab8a9a91ab42464168bc832253b150f4ee1dc7a54d715cc793.jpg)  
Fig. 1. Prevention and Detection & Containment Safeguard Framework under Uncertainty.

## 3.2. Notation and model

Section 3.2.1 introduces our notation and the deterministic nonlinear form of the model. In Section 3.2.2, we linearize the two non linear components - the objective function and a constraint - in the original formulation, which establishes the base model needed to introduce ellipsoidal uncertainty in Section 3.3.

## 3.2.1. Deterministic nonlinear model

We use I, J, K, M, and D to represent sets of prevention safeguard bundles, detection & containment safeguard bundles, threats, compo nents, and business sector, respectively. The unit of analysis is a safeguard bundle containing all subsets of applicable prevention safeguards. This approach reflects industry practice [51] and conveniently resolves the complexity of modeling from nonlinear constraints (e.g., [19]). The case study provides details on forming bundles, and to facilitate exposition, we use ℓ to denote a single prevention safeguard.

The deterministic parameters include φ<sub>ik</sub>, ω<sub>km</sub>, ζ, θ, and η. Parameter $\varphi _ { i k }$ denotes a coverage matrix that links the prevention bundles and threats: $\varphi _ { i k } = 1$ if threat k can be prevented by safeguard bundle $i ,$ and 0 otherwise (parameter $\varphi _ { \ell k }$ is defined the same way for an individual prevention safeguard). Similarly, parameter $\omega _ { k m }$ denotes coverage between the threats and components and takes a value of 1 if threat k has an impact on component m, and 0 otherwise. Parameter ζ specifies the maximum threat allowed. Parameter θ represents the perunit relative cost ratio between a detection & containment safeguard and a prevention safeguard. Parameter η denotes the maximum number of safeguards the firm can plan to implement in light of resource constraints they face.

The uncertain parameters are $\widetilde { C _ { i k } } , \widetilde { \lambda _ { k d } }$ , and $\widetilde { C _ { k j } ^ { \prime } }$ . Parameter $\widetilde { C _ { i k } }$ denotes the efectiveness of safeguard bundle i against threat k and the value of $\widetilde { C _ { i k } } \in ( 0 , 1 )$ , ranging from none to complete protection. Parameter denotes the likelihood of attack for threat k on sector d. Parameter $\widetilde { C _ { k j } ^ { \prime } }$ represents the total social cost associated with detection & containment safeguard bundle j given threat k.

We define $S _ { i }$ and ${ S _ { j } } ^ { ' }$ as binary decision variables, and they equal 1 if safeguard bundles i ∈ I and $j \in J$ are part of the security profile and 0 otherwise. We define nonnegative variable $X _ { k }$ to determine the residual efect of a threat after prevention. We use nonnegative variable $Z _ { m }$ to represent the maximum efect of all threats on component m

The objective function (O1) represents the social cost due to delayed detection and containment. Constraint C1 calculates the residual effect of threat k on sector d after a prevention efort by safeguard bundle i, taking into consideration the likelihood of attack and the link between safeguard and threat. Constraint C2 ensures that only one prevention bundle is chosen, and constraint C5 ensures a single detection & containment bundle. Constraints C3 and C4 together identify the most vulnerable component and enforce its threat level below a specified threshold. Constraint C6 ensures that the number of safeguards im plemented does not exceed the maximum allowed while accounting for the cost ratio structure between the two types of safeguards.

$$
(M) \underset {Z _ {m}, X _ {k}, S _ {j} ^ {\prime}, S _ {i,}} {\text {Min}} \sum_ {j \in J, k \in K} \widetilde {C _ {k j} ^ {\prime}}   X _ {k} S _ {j} ^ {\prime}\tag{01}
$$

$$
s. t. \widetilde {\lambda_ {k d}} \left(1 - \sum_ {i \in I} \widetilde {C _ {i k}} \varphi_ {i k} S _ {i}\right) \leq X _ {k} \forall d \in D, k \in K
$$

$$
\sum_ {i \in I} S _ {i} = 1\tag{C1}
$$

$$
M a x _ {k} X _ {k} \omega_ {k m} \leq Z _ {m} \forall m \in M\tag{C2}
$$

$$
Z _ {m} \leq \zeta \forall m \in M\tag{C3}
$$

(C4)

$$
\sum_ {j \in J} S _ {j} ^ {\prime} = 1\tag{C5}
$$

$$
\sum_ {i \in I} i S _ {i} + \theta \sum_ {j \in J} j S _ {j} ^ {\prime} \leq \eta
$$

$$
Z _ {m} \geq 0; X _ {k} \geq 0; S _ {j} ^ {\prime}, S _ {i} b i n a r y\tag{C6}
$$

(C7)

## 3.2.2. Linearization of model M

Constraint C3 in model M is nonlinear because of the Max function, which can be linearized by introducing three new variables and constraints C8–C11 as follows. We use decision variables $Y _ { k m } = X _ { k } \omega _ { k m }$ and $Y _ { m } ^ { m a x }$ to calculate the residual efect of threat k on component m and the maximum efect of all threats on component m among all threats, respectively. We also create a binary variable $y _ { k m }$ that is equal to 1 if the k<sup>th</sup>threat has the maximum efect on component m and 0 otherwise. Parameter $\gamma$ is an arbitrarily chosen larger number. Note that since nonlinear constraint C3 is replaced by linear constraints C8–C11, constraint C4 must be modified accordingly and replaced by C12. To facilitate derivation of a robust model, we expand the left hand side of constraint C1 and create a new parameter $\widetilde { \delta _ { i k d } } = \widetilde { \lambda _ { k d } } \widetilde { C _ { i k } }$ . The trans formed constraint C1 is shown below as C13.

$$
Y _ {k m} = X _ {k} \omega_ {k m} \forall k \in K, m \in M\tag{C8}
$$

$$
Y _ {k m} \leq Y _ {m} ^ {m a x} \forall k \in K, m \in M
$$

$$
Y _ {k m} \geq Y _ {m} ^ {m a x} - \gamma (1 - y _ {k m}) \forall k \in K, m \in M\tag{C9}
$$

$$
\sum_ {k \in K} y _ {k m} = 1 \forall m \in M\tag{C10}
$$

$$
Y _ {m} ^ {m a x} \leq \zeta \forall m \in M\tag{C11}
$$

(C12)

$$
\widetilde {\lambda_ {k d}} - \sum_ {i \in I} \widetilde {\delta_ {i k d}} \varphi_ {i k} S _ {i} \leq X _ {k} \forall d \in D, k \in K\tag{C13}
$$

$$
Y _ {k m} \geq 0; Y _ {m} ^ {m a x} \geq 0; y _ {k m} b i n a r y\tag{C14}
$$

Next, we linearize the objective function, which contains the product of variables ${ \boldsymbol { S _ { j } } } ^ { \prime }$ and $X _ { k } ,$ , by introducing a nonnegative continuous variable $z _ { j k } = S _ { j } ^ { ' } \ : X _ { k }$ and constraints C15 and C16:

$$
z _ {j k} \geq S _ {j} ^ {\prime} + X _ {k} - 1 \forall j \in J, k \in K\tag{C15}
$$

$$
z _ {j k} \geq 0\tag{C16}
$$

The complete linearized version of model M is as follows:

$$
(L _ {-} M) \underset {z _ {j k}, Y _ {k m}, Y _ {m} ^ {m a x}, y _ {k m}, X _ {k}, S _ {j} ^ {\prime}, S _ {i,}} {\text {Min}} \sum_ {j \in J, k \in K} \widetilde {C _ {k j} ^ {\prime}} z _ {j k}
$$

$$
s. t. \mathrm{C2,C5-C7,C8-C16}\tag{01}
$$

## 3.3. Ellipsoidal uncertainty robust model

## 3.3.1. Illustration of box and ellipsoidal uncertainty sets

We choose the ellipsoidal uncertainty set [40] to model uncertain parameters $\widetilde { C _ { k j } ^ { \prime } } , \widetilde { \lambda _ { k d } }$ and $\widetilde { \delta _ { i k d } }$ . It is less conservative than box uncertainty, which assumes all the uncertain parameters would realize their worst values simultaneously. It approximates many instances of complicated convex sets and provides a tractable analytical structure, mitigating the conflicting objectives of computational tractability and flexibility. Below we use geometry to demonstrate how the ellipsoidal uncertainty set controls for the overconservatism of the box uncertainty set [38].

![](/api/attachments/7KWJMYZQ/fulltext/images/e97e216dc5c9aed4094789e9ebfd7002210277d7eaf282f39f05bfdf9ff91514.jpg)  
Fig. 2. Geometrical Representation of Box and Ellipsoidal Uncertainty Sets.

Assume an uncertain parameter bounded by the box uncertainty set $[ \overline { { a _ { 1 } } } - \widehat { a _ { 1 } } , \overline { { a _ { 1 } } } + \widehat { a _ { 1 } } ]$ and $[ \overline { { a _ { 2 } } } \cdot \widehat { a _ { 2 } } , \overline { { a _ { 2 } } } + \widehat { a _ { 2 } } ]$ , shown as a dotted box in $\mathrm { F i g . ~ } 2 ,$ which realizes the worst deviation on both dimensions. Parameter Θ can be adjusted to control the size of an ellipsoidal uncertainty set where $\Theta = 1$ leads to an inscribed ellipsoid, and $\theta = \surd 2$ to a circumscribed ellipsoid (2 is the dimension of the uncertainty parameter). A value between 1 and √2 eliminates parts of the corners of the box uncertainty and thus mitigates overconservatism. Although the robust counterpart, given an ellipsoidal uncertainty - a second-order cone programming (SOCP) model – is computationally intensive, the next section describes how to transform the SOCP, so it can be readily solved using of-the-shelf solvers like CPLEX.

## 3.3.2. Application of ellipsoidal uncertainty set to model L\_M

We first model $\widetilde { C _ { k j } ^ { \prime } }$ in the objective function. Let $\widetilde { C _ { k j } ^ { \prime } } = \overline { { C _ { k j } ^ { \prime } } } + \xi _ { k j } \widehat { C _ { k j } ^ { \prime } } ,$ where $\overline { { C _ { k j } ^ { \prime } } }$ and $\widehat { C _ { k j } ^ { \prime } }$ represent the nominal value and the deviation of $\widetilde { C _ { k j } ^ { \prime } } ,$ respectively. We construct the ellipsoid set $U ^ { \widetilde { C _ { k j } ^ { \prime } } }$ as $\left\{ \xi _ { k j } \mid \sqrt { \sum _ { j \in J , k \in K } \xi _ { k j } ^ { 2 } } \leq \Theta _ { k j } ^ { C ^ { \prime } } \right\}$ , where the adjustable parameter ${ \Theta _ { k j } } ^ { C }$ sets the size of set $U ^ { \widetilde { C _ { k j } ^ { \prime } } }$ For bounded uncertainty, $\theta _ { k j } ^ { \quad C ^ { } } \mathrm { ~ i s } ^ { \leq } \sqrt { | K \times J | }$ , <sub>where</sub> $| K \times J |$ is the cardinality of set $K \times J .$ Objective function O1 is now augmented $_ { \mathrm { a s } } \mathrm { O 1 }$ $U ^ { \widetilde { C _ { k j } ^ { \prime } } }$ , which is equivalent to its robust counterpart O1-ellip.

$$
\begin{array}{l} \underset {z _ {j k}, Y _ {k m}, y _ {m} ^ {m a x}, y _ {k m}, X _ {k}, S _ {j} ^ {\prime}, S _ {i}} {\text {Min}} \left(\underset {\widetilde {C _ {k j} ^ {\prime}} \in U ^ {\widetilde {C _ {k j} ^ {\prime}}}} {\text {Max}} \sum_ {j \in J, k \in K} \widetilde {C _ {k j} ^ {\prime}} z _ {j k}\right) (O 1 - U ^ {\widetilde {C _ {k j} ^ {\prime}}}) \\ \underset {z _ {j k}, Y _ {k m}, y _ {m} ^ {m a x}, y _ {k m}, X _ {k}, S _ {j} ^ {\prime}, S _ {i}} {\text {Min}} \sum_ {j \in J, k \in K} \overline {{C _ {k j} ^ {\prime}}} z _ {j k} + \Theta_ {k j} ^ {C ^ {\prime}} \sqrt {\sum_ {j \in J , k \in K} (\widehat {C _ {k j} ^ {\prime}} z _ {j k}) ^ {2}} \\ (O 1 - e l l i p) \end{array}
$$

Next, we derive the robust counterpart of constraint C13. We model $\widetilde { \delta _ { i k d } } = \overline { { \delta _ { i k d } } } + \xi _ { i k d } \widehat { \delta _ { i k d } } .$ and the ellipsoid set $U ^ { \widetilde { \delta _ { i k d } } }$ as $\left\{ \xi _ { i k d } \ \Big | \ \sqrt { \sum _ { i \in I } \xi _ { i k d } ^ { 2 } } \ \leq \ \Theta _ { i k d } ^ { \delta } \right\}$ , where $\mathcal { O } _ { i k d } ^ { \delta } \leq \sqrt { | I | }$ . Uncertain parameter $\widetilde { \lambda _ { k d } }$ is expressed as $\widehat { \lambda _ { k d } } + \xi _ { k d } \widehat { \lambda _ { k d } } ,$ , where $\xi _ { k d }$ is modeled using an ellip soid set $U ^ { \widetilde { \lambda _ { k d } } }$ as $\{ \xi _ { k d } \mid \sqrt { \xi _ { k d } ^ { 2 } } \leq \Theta _ { k d } ^ { \lambda } \}$ and $\mathcal { O } _ { k d } ^ { \lambda } \leq \sqrt { | { 1 } | }$ . The counterpart of constraint C13 after incorporating $U ^ { \widetilde { \delta _ { i k d } } }$ and $\widehat { U ^ { \lambda _ { k d } } }$ is expressed as C13- ellip, which is simplified to C13-ellip-S. The signs reflect the direction of the constraint

$$
\begin{array}{c} \overline {{\lambda_ {k d}}} + \Theta_ {k d} ^ {\lambda} \sqrt {(\widehat {\lambda_ {k d}}) ^ {2}} - \sum_ {i \in I} \overline {{\delta_ {i k d}}}   \varphi_ {i k} S _ {i} + \Theta_ {i k d} ^ {\delta^ {\prime}} \sqrt {\sum_ {i \in I} (\widehat {\delta_ {i k d}}   \varphi_ {i k} S _ {i}) ^ {2}} \leq X _ {k} \forall \\ d \in D, k \in K (C 1 3 - e l l i p) \end{array}
$$

$$
\begin{array}{r l} \overline {{\lambda_ {k d}}} + \Theta_ {k d} ^ {\lambda} \widehat {\lambda_ {k d}} - \sum_ {i \in I} \overline {{\delta_ {i k d}}}   \varphi_ {i k} S _ {i} + \Theta_ {i k d} ^ {\xi^ {\prime}} \sqrt {\sum_ {i \in I} (\widehat {\delta_ {i k d}}   \varphi_ {i k} S _ {i}) ^ {2}} & \leq X _ {k} \forall \\ d \in D, k \in K & (\text {C13 - ellip - S}) \end{array}
$$

The complete robust counterpart of model $L _ { - } M$ is expressed below as $R \_ L M ,$ , a conic quadratic program.

$$
\begin{array}{c} (R \_ L \_ M) \underset {Z _ {j k}, Y _ {k m}, Y _ {m} ^ {\max}, y _ {k m}, X _ {k}, S _ {j} ^ {\prime}, S _ {l},} {\text {Min}} \sum_ {j \in J, k \in K} \overline {{C _ {k j} ^ {\prime}}} \\ Z _ {j k} + \Theta_ {k j} ^ {C ^ {\prime}} \sqrt {\sum_ {j \in J , k \in K} \left(\widehat {C _ {k j} ^ {\prime}} z _ {j k}\right) ^ {2}} (\text {O1 - ellip}) \end{array}
$$

## s.t. C2, C5–C7, C8–C12, C14–C16, C13-ellip-S

Model $R \_ L M$ can be readily solved by CPLEX with a simple variable transformation of O1-ellip and C13-ellip-S. We first introduce a nonnegative variable Conic\_Var1 and constraints C17 to transform objective function O1-ellip as follows:

$$
\begin{array}{c} \underset {C o n i c \_ V a r 1, z _ {j k}, Y _ {k m}, Y _ {m} ^ {m a x}, y _ {k m}, X _ {k}, S _ {j} ^ {\prime}, S _ {i}} {\text {Min}} \sum_ {j \in J, k \in K} \overline {{C _ {k j} ^ {\prime}}} z _ {j k} + \Theta_ {k j} ^ {C ^ {\prime}} C o n i c _ {V a r 1} \\ (\mathrm{O1-ellip-t}) \\ C o n i c \_ V a r 1 \geq \sqrt {\sum_ {j \in J , k \in K} \left(\widehat {C _ {k j} ^ {\prime}} z _ {j k}\right) ^ {2}} \end{array}\tag{C17}
$$

Next, we introduce a nonnegative variable Conic $. V a r 2 _ { k d }$ and constraints C13-ellip-S-t1 and C13-ellip-S-t2 to transform constraint C13- ellip-S.

$$
\begin{array}{c} C o n i c \_ V a r 2 _ {k d} \geq \sqrt {\sum_ {i \in I} (\widehat {\delta_ {i k d}}   \varphi_ {i k} S _ {i}) ^ {2}}    \forall   d \in D,   k \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \q q u a l l i n e d. \\ \hline K (C 1 3 - e l l i p - S - t 1) \\ \overline {{\lambda_ {k d}}} + \Theta_ {k d} ^ {\lambda}   \widehat {\lambda_ {k d}} - \sum_ {i \in I} \overline {{\delta_ {i k d}}}   \varphi_ {i k} S _ {i} + \Theta_ {i k d} ^ {\mathfrak {g} ^ {\prime}} C o n i c _ {V a r 2 _ {k d}} \leq X _ {k}    \forall \\ d \in D,   k \in K    (C 1 3 - e l l i p - S - t 2) \end{array}
$$

The final transformed model is presented below as (TR\_L\_M), which can be readily solved by of-the-shelf solvers (e.g., CPLEX), a feature especially desirable for practical application.

$$
\begin{array}{l} (T R _ {L _ {M}}) \underset {\text {Conic\_Var1}, \text {Conic\_Var2} _ {k d}, z _ {j k}, Y _ {k m}, Y _ {m} ^ {m a x}, y _ {k m}, X _ {k}, S _ {j} ^ {\prime}, S _ {i},} {\text {Min}} \sum_ {j \in J, k \in K} \overline {{C _ {k j} ^ {\prime}}} \\ Z _ {j k} + \Theta_ {k j} ^ {C ^ {\prime}} \text {Conic\_Var1} \quad (\text {O1 - ellip - t}) \\ \text {s.t. C2, C5 - C7, C8 - C12, C14 - C16, C13 - ellip - S - t1, C13 - ellip - S - t2, C17} \end{array}
$$

## 4. Case study

## 4.1. Background

Following Ponemon Institute's “2016 Cost of Cyber Crime Study & the Risk of Business Innovation,” we focus on nine types of prevention safeguards, six types of detection & containment safeguards, eight types of threats, and 17 business sectors. Further, we identify five components associated with IT-Systems and Applications that represent a typical setup for providing a web-based service. Our narrowing of the focus is consistent with the literature (e.g., [20]). The connections among the threats, safeguards, and components are established using the well-accepted IT baseline protection catalogues of the BSI [52]. This standard is fully in line with the ISO 27000 series and ofers custom BSI and ISO 27001 certifications. The relevant tables provide the IT codes as a reference.

## 4.2. Parameter specification

## 4.2.1. Likelihood of attack $( \overline { { \lambda _ { k d } } } )$

Table 1 estimates the likelihood of an attack by threat type based on the cyberattack data of the 237 benchmarked companies included in the Ponemon report. Using the average annualized cyberattack cost (loss) data in the report, we also computed the likelihood of an attack by industry sector (Table 2). We believe losses in each sector are the best proxy for the likelihood of attack since they represent the sector's attractiveness to a hacker. Table 3 reports the likelihood of attack for threat k on sector d $( \overline { { \lambda _ { k d } } } )$ based on Tables 1 and 2.

Table 2  
Table 3  
Table 1  
Likelihood of attack by threat.

<table><tr><td>Cyberthreat (K)</td><td>Likelihood of attack</td><td>IT code (T-Threats)</td></tr><tr><td>Malicious insiders</td><td>0.084</td><td>5.2, 5.20, 5.9, 5.10, 5.29, 5.41, 5.19</td></tr><tr><td>Malicious code</td><td>0.124</td><td>5.173, 5.64, 5.142, 5.128, 5.131</td></tr><tr><td>Web-based attacks</td><td>0.129</td><td>5.11, 5.165, 5.166, 5.172, 5.175</td></tr><tr><td>Phishing &amp; SE</td><td>0.143</td><td>5.42</td></tr><tr><td>Denial of service</td><td>0.104</td><td>5.28, 5.65</td></tr><tr><td>Stolen devices</td><td>0.102</td><td>5.22</td></tr><tr><td>Malware</td><td>0.202</td><td>5.23</td></tr><tr><td>Botnets</td><td>0.112</td><td>5.89</td></tr></table>

Likelihood of attack by sector.

<table><tr><td>Sector (D)</td><td>Likelihood of attack</td></tr><tr><td>Financial services</td><td>0.133</td></tr><tr><td>Utilities &amp; energy</td><td>0.119</td></tr><tr><td>Technology</td><td>0.089</td></tr><tr><td>Services</td><td>0.072</td></tr><tr><td>Industrial</td><td>0.065</td></tr><tr><td>Healthcare</td><td>0.059</td></tr><tr><td>Retail</td><td>0.057</td></tr><tr><td>Transportation</td><td>0.055</td></tr><tr><td>Public sector</td><td>0.054</td></tr><tr><td>Communications</td><td>0.049</td></tr><tr><td>Consumer products</td><td>0.047</td></tr><tr><td>Media</td><td>0.046</td></tr><tr><td>Pharmaceutical</td><td>0.04</td></tr><tr><td>Education &amp; research</td><td>0.036</td></tr><tr><td>Hospitality</td><td>0.03</td></tr><tr><td>Automotive</td><td>0.029</td></tr><tr><td>Agriculture</td><td>0.022</td></tr></table>

## 4.2.2. Efectiveness of prevention safeguard bundle $\overline { { ( C _ { i k } } }$ and $\varphi _ { \ell k } )$

We apply Schilling and Werners's [20] methodology to determine a safeguard's reduction coeficient $\sigma _ { \ell } .$ Efectiveness is correlated with qualification level; a higher qualification level indicates greater efectiveness. We also use a five-level scale for $\sigma _ { \ell }$ and map it to the five qualification levels as follows:

$$
\sigma_ {\ell} = \left\{ \begin{array}{l} 0. 5 \text {if qualification level of} \ell = A \\ 0. 6 \text {if qualification level of} \ell = B \\ 0. 7 \text {if qualification level of} \ell = C \\ 0. 8 \text {if qualification level of} \ell = Z \\ 0. 9 \text {if qualification level of} \ell = W \end{array} \right.
$$

where, for example, $\sigma _ { \ell } = 0 . 8$ indicates that, if deployed, a safeguard reduces a threat's criticality by 1–0.8 = 20% (i.e., down to 20%) (Table 4).

To reflect industry practice [51], our bundles comprise all subsets of the nine prevention safeguards. A total 511 bundles $\begin{array} { r } { ( { \mathsf { \partial } } _ { 9 } \mathsf { C } _ { 1 } + { \mathsf { \partial } } _ { 9 } \mathsf { C } _ { 2 } + { \mathsf { \partial } } _ { 9 } \mathsf { C } _ { 3 } + { \mathsf { \partial } } _ { 9 } \mathsf { C } _ { 4 } + { \mathsf { \partial } } _ { 9 } \mathsf { C } _ { 5 } + { \mathsf { \partial } } _ { 9 } \mathsf { C } _ { 6 } + { \mathsf { \partial } } _ { 9 } \mathsf { C } _ { 7 } + { \mathsf { \partial } } _ { 9 } \mathsf { C } _ { 8 } + { \mathsf { \partial } } _ { 9 } \mathsf { C } _ { 9 } ) } \end{array}$ are constructed, and Table 6 shows the first from each combination as an example. The probability that a bundle will thwart a threat is calculated as $1 - \Pi _ { \ell } \sigma _ { \ell } ,$ accounting for coverage links between the prevention safeguard and the threat (Table 5). For example, the probability that bundle 10, which includes prevention safeguards 1 and 2, will thwart threat 1 (malicious insiders) is 0.52, calculated as 1-(1–0.2)\*(1–0.4) since both safeguards target threat 1. However, its probability of thwarting threat 2 (malicious code) is only 0.2 because safeguard 2 (security patch management) does not target malicious code.

## 4.2.3. Social cost $( \overline { { C _ { k j } ^ { \prime } } } )$

The firm can also invest in controls that help detect and contain attacks. The efectiveness of these investments depend on number of safeguards as stronger the security profile the better the ability to detect and contain attacks. The extent of losses depends on the type of cyberattack; some attacks are more vicious than the rest and therefore might also be more dificult to detect and contain. In the Ponemon report, for example, a malicious insider cyberattack would on average take 51.5 days to resolve (i.e., detect and contain). As noted in Table 7, it takes the most amount of time, on average, to resolve attacks from malicious insiders, malicious code and web-based attackers. Stolen devices, malware, and botnets are resolved relatively quickly on average. The time to resolve the attacks can have a significant impact on the total cost of cybercrime. For example, if it takes < 30 days to resolve a cyberattack, the estimated average cost is \$7.7 million. In contrast, if the time to contain an attack is > 90 days, the average cost increases to \$12.2 million. Detection and containment safeguards if deployed can reduce these social costs. Note that, unlike the prevention safeguards, the detection and containment safeguards are given in bundles in the report. For example, a five-safeguard bundle can reduce social cost by \$2.77 million while a single-safeguard only by \$0.60 million (see Table 8). This among other things provides support to the safeguard bundle approach in our models. We assume that each bundle includes safeguard features in the order of their sophistication. Speci fically, a bundle with 2 safeguards would include ones with ranks 5 and 4, a bundle with 3 safeguards would include those with ranks 5 through 3 and so on. Working with IT professionals we determined the ranking (see Table 9) for features listed in Table 9 in the order of their sophistication. This essentially means \$1.86 million in savings noted in Table 8 is associated with a bundle with safeguards ranked 2 through 5. Note that the reductions in social cost are estimates provided in the Ponemon report and we ofer two hypotheses as to the reduced savings going from 1 to a bundle of 2. We hypothesize it captures the cost versus benefits disadvantage or put diferently a bundle of 2 (i.e. adding feature 4 in Table 9 to feature 5) is possibly a less efective cybersecurity investment. Another way of looking at it is that to extract optimal value from lower ranked features, they need to accompany the more sophisticated ones. Using Tables 7 and 8, we estimate social cost for each threat as shown in Table 10.

Likelihood of attack for threat k on sector d $( \overline { { \lambda _ { k d } } } )$

<table><tr><td></td><td>Financial services</td><td>Utilities &amp; energy</td><td>Technology</td><td>Services</td><td>Industrial</td><td>Healthcare</td><td>Retail</td><td>Transportation</td></tr><tr><td>Malicious insiders</td><td>0.011</td><td>0.010</td><td>0.008</td><td>0.006</td><td>0.006</td><td>0.005</td><td>0.005</td><td>0.005</td></tr><tr><td>Malicious code</td><td>0.017</td><td>0.015</td><td>0.011</td><td>0.009</td><td>0.008</td><td>0.007</td><td>0.007</td><td>0.007</td></tr><tr><td>Web-based attacks</td><td>0.017</td><td>0.015</td><td>0.012</td><td>0.009</td><td>0.008</td><td>0.008</td><td>0.007</td><td>0.007</td></tr><tr><td>Phishing &amp; SE</td><td>0.019</td><td>0.017</td><td>0.013</td><td>0.010</td><td>0.009</td><td>0.008</td><td>0.008</td><td>0.008</td></tr><tr><td>Denial of service</td><td>0.014</td><td>0.012</td><td>0.009</td><td>0.008</td><td>0.007</td><td>0.006</td><td>0.006</td><td>0.006</td></tr><tr><td>Stolen devices</td><td>0.014</td><td>0.012</td><td>0.009</td><td>0.007</td><td>0.007</td><td>0.006</td><td>0.006</td><td>0.006</td></tr><tr><td>Malware</td><td>0.027</td><td>0.024</td><td>0.018</td><td>0.015</td><td>0.013</td><td>0.012</td><td>0.012</td><td>0.011</td></tr><tr><td>Botnets</td><td>0.015</td><td>0.013</td><td>0.010</td><td>0.008</td><td>0.007</td><td>0.007</td><td>0.006</td><td>0.006</td></tr></table>

<table><tr><td></td><td>Public sector</td><td>Communications</td><td>Consumer products</td><td>Media</td><td>Pharmaceutical</td><td>Education &amp; research</td><td>Hospitality</td><td>Automotive</td><td>Agriculture</td></tr><tr><td>Malicious insiders</td><td>0.005</td><td>0.004</td><td>0.004</td><td>0.004</td><td>0.003</td><td>0.003</td><td>0.003</td><td>0.002</td><td>0.002</td></tr><tr><td>Malicious code</td><td>0.007</td><td>0.006</td><td>0.006</td><td>0.006</td><td>0.005</td><td>0.005</td><td>0.004</td><td>0.004</td><td>0.003</td></tr><tr><td>Web-based attacks</td><td>0.007</td><td>0.006</td><td>0.006</td><td>0.006</td><td>0.005</td><td>0.005</td><td>0.004</td><td>0.004</td><td>0.003</td></tr><tr><td>Phishing &amp; SE</td><td>0.008</td><td>0.007</td><td>0.007</td><td>0.007</td><td>0.006</td><td>0.005</td><td>0.004</td><td>0.004</td><td>0.003</td></tr><tr><td>Denial of service</td><td>0.006</td><td>0.005</td><td>0.005</td><td>0.005</td><td>0.004</td><td>0.004</td><td>0.003</td><td>0.003</td><td>0.002</td></tr><tr><td>Stolen devices</td><td>0.006</td><td>0.005</td><td>0.005</td><td>0.005</td><td>0.004</td><td>0.004</td><td>0.003</td><td>0.003</td><td>0.002</td></tr><tr><td>Malware</td><td>0.011</td><td>0.010</td><td>0.010</td><td>0.009</td><td>0.008</td><td>0.007</td><td>0.006</td><td>0.006</td><td>0.004</td></tr><tr><td>Botnets</td><td>0.006</td><td>0.006</td><td>0.005</td><td>0.005</td><td>0.005</td><td>0.004</td><td>0.003</td><td>0.003</td><td>0.003</td></tr></table>

Table 4  
Efectiveness of individual prevention safeguard

<table><tr><td>Prevention safeguard</td><td>Probability of thwarting attack (1 - σε)</td><td>IT Code (S-Safeguards)</td></tr><tr><td>Penetration testing</td><td>0.2</td><td>4.93</td></tr><tr><td>Security patch management</td><td>0.4</td><td>4.417</td></tr><tr><td>Dynamic scanning</td><td>0.2</td><td>4.226, 4.26</td></tr><tr><td>Static scanning</td><td>0.5</td><td>4.33</td></tr><tr><td>Educate developers on safe coding</td><td>0.5</td><td>3.4</td></tr><tr><td>Data masking or redaction of live data (during testing)</td><td>0.3</td><td>4.7</td></tr><tr><td>Security testing throughout the SDLC</td><td>0.4</td><td>5.17, 5.18, 5.19, 5.20, 5.35, 5.8</td></tr><tr><td>Code review and debugging system</td><td>0.5</td><td>3.5</td></tr><tr><td>Run-time application self-protection</td><td>0.4</td><td>4.396</td></tr></table>

Table 5  
Coverage Links between Prevention Safeguard and Threat $( \varphi _ { \ell k } )$

<table><tr><td></td><td>Malicious insiders</td><td>Malicious code</td><td>Web-based attacks</td><td>Phishing &amp; SE</td><td>Denial of service</td><td>Stolen devices</td><td>Malware</td><td>Botnets</td></tr><tr><td>Penetration testing</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td>Security patch management</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td>Dynamic scanning</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td>Static scanning</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Educate developers on safe coding</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Data masking or redaction of live data (during testing)</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>Security testing throughout the SDLC</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>Code review and debugging system</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>Run-time application self-protection</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr></table>

As indicated in the report, the social cost is related to four primary consequences of a cybercrimes and they are business disruptions, loss of revenue, damage to equipment, and the loss of information. Further,

## Table 7

Resolution time and social cost of cyberthreats.

<table><tr><td>Cyberthreat</td><td>Time to resolve an attack (days)</td><td>Total social cost ($ millions)</td></tr><tr><td>Malicious insiders</td><td>51.5</td><td>13.22</td></tr><tr><td>Malicious code</td><td>49.6</td><td>12.73</td></tr><tr><td>Web-based attacks</td><td>25.3</td><td>6.49</td></tr><tr><td>Phishing &amp; SE</td><td>19.8</td><td>5.08</td></tr><tr><td>Denial of service</td><td>17.8</td><td>4.57</td></tr><tr><td>Stolen devices</td><td>13.7</td><td>3.52</td></tr><tr><td>Malware</td><td>5.6</td><td>1.44</td></tr><tr><td>Botnets</td><td>2</td><td>0.51</td></tr></table>

## Table 8

Efectiveness of detection and containment safeguard bundles.

<table><tr><td>Number of detection and containment safeguards</td><td>Reduction in social cost ($ millions)</td></tr><tr><td>5</td><td>$2.77</td></tr><tr><td>4</td><td>$1.86</td></tr><tr><td>3</td><td>$1.20</td></tr><tr><td>2</td><td>$0.48</td></tr><tr><td>1</td><td>$0.60</td></tr></table>

Table 6  
Bundle formation and probability of thwarting threat $( \overline { { C _ { i k } } } )$

<table><tr><td colspan="10">Probability of thwarting threat</td></tr><tr><td>Prevention bundle</td><td>Safeguards</td><td>Malicious insiders</td><td>Malicious code</td><td>Web-based attacks</td><td>Phishing &amp; SE</td><td>Service denial</td><td>Stolen devices</td><td>Malware</td><td>Botnets</td></tr><tr><td>1</td><td>1</td><td>0.200</td><td>0.200</td><td>0.200</td><td>0.200</td><td>0.000</td><td>0.000</td><td>0.200</td><td>0.200</td></tr><tr><td>10</td><td>1,2</td><td>0.520</td><td>0.200</td><td>0.520</td><td>0.200</td><td>0.400</td><td>0.000</td><td>0.520</td><td>0.520</td></tr><tr><td>46</td><td>1,2,3</td><td>0.616</td><td>0.360</td><td>0.616</td><td>0.200</td><td>0.520</td><td>0.000</td><td>0.616</td><td>0.616</td></tr><tr><td>130</td><td>1,2,3,4</td><td>0.616</td><td>0.360</td><td>0.616</td><td>0.200</td><td>0.520</td><td>0.000</td><td>0.616</td><td>0.616</td></tr><tr><td>256</td><td>1,2,3,4,5</td><td>0.616</td><td>0.680</td><td>0.808</td><td>0.200</td><td>0.760</td><td>0.000</td><td>0.616</td><td>0.616</td></tr><tr><td>382</td><td>1,2,3,4,5,6</td><td>0.731</td><td>0.680</td><td>0.808</td><td>0.200</td><td>0.760</td><td>0.300</td><td>0.616</td><td>0.616</td></tr><tr><td>466</td><td>1,2,3,4,5,6,7</td><td>0.839</td><td>0.808</td><td>0.885</td><td>0.200</td><td>0.856</td><td>0.300</td><td>0.770</td><td>0.616</td></tr><tr><td>502</td><td>1,2,3,4,5,6,7,8</td><td>0.919</td><td>0.904</td><td>0.942</td><td>0.200</td><td>0.928</td><td>0.300</td><td>0.885</td><td>0.616</td></tr><tr><td>511</td><td>1,2,3,4,5,6,7,8,9</td><td>0.919</td><td>0.942</td><td>0.965</td><td>0.200</td><td>0.957</td><td>0.300</td><td>0.931</td><td>0.616</td></tr></table>

Table 9  
Ranking of detection safeguards.

<table><tr><td>Rank</td><td>Detection and containment safeguards</td></tr><tr><td>1</td><td>Tightly couples SIEM and advanced analytics to detect both known and unknown threats</td></tr><tr><td>2</td><td>Detects unknown threats through user behavior analytics</td></tr><tr><td>3</td><td>Tailors SIEM environment to customer specific configurations</td></tr><tr><td>4</td><td>Monitors and correlates events in real-time to detect critical threats</td></tr><tr><td>5</td><td>Incorporates threat intelligence from community of security practitioners</td></tr></table>

Table 10  
Social Cost (\$ millions) of Cyberthreat $( \overline { { C _ { k j } ^ { \prime } } } )$

optimal number of prevention and detection & containment safeguards and their related social cost. Tables 14–16 summarize these results.

Table 14 lists the optimal number of prevention vs. detection & containment safeguards. For instance, in scenario 1, where θ = 0.5 and $\eta = 1 .$ , the minimal social cost of \$437,761 (Table 16) calls for 1 prevention vs. 0 detection & containment safeguard (1–0). As our analysis includes a total of nine prevention safeguards and five detection & containment safeguards in addition to the actual number reported in Table 14, we also compute the percentages of safeguards used within their respective category in Table 15. Again, in scenario 1, 11% vs. 0% means 11% of prevention safeguards (1 used divided by the total 9) and

<table><tr><td>Number of Detection and containment safeguards</td><td>Malicious insiders</td><td>Malicious code</td><td>Web-based attacks</td><td>Phishing &amp; SE</td><td>Denial of service</td><td>Stolen devices</td><td>Malware</td><td>Botnets</td></tr><tr><td>5</td><td>$10.45</td><td>$9.96</td><td>$3.72</td><td>$2.31</td><td>$1.80</td><td>$0.75</td><td>$0.00</td><td>$0.00</td></tr><tr><td>4</td><td>$11.36</td><td>$10.87</td><td>$4.63</td><td>$3.22</td><td>$2.71</td><td>$1.66</td><td>$0.00</td><td>$0.00</td></tr><tr><td>3</td><td>$12.02</td><td>$11.53</td><td>$5.29</td><td>$3.88</td><td>$3.37</td><td>$2.32</td><td>$0.24</td><td>$0.00</td></tr><tr><td>2</td><td>$12.74</td><td>$12.25</td><td>$6.01</td><td>$4.60</td><td>$4.09</td><td>$3.04</td><td>$0.96</td><td>$0.03</td></tr><tr><td>1</td><td>$12.62</td><td>$12.13</td><td>$5.89</td><td>$4.48</td><td>$3.97</td><td>$2.92</td><td>$0.84</td><td>$0.00</td></tr><tr><td>0</td><td>$13.22</td><td>$12.73</td><td>$6.49</td><td>$5.08</td><td>$4.57</td><td>$3.52</td><td>$1.44</td><td>$0.51</td></tr></table>

information loss covers loss (or theft) of sensitive and confidential information, which at least partially captures the negative externalities borne by users of the services under attack. Interestingly, it is the costliest category, representing 39% of the total social cost in 2016. The other three categories are more in line with private cost as, for example, business disruption is linked to diminished employee productivity and business process failures.

## 4.2.4. Other parameters $( \omega _ { k m } , \zeta ,$ θ and η)

Table 11 shows coverage between threats and components. Each component represents a typical aspect of a system. A threat captures a common scenario that may damage the system. Each component may be endangered by a variety of threats, and each threat may apply to more than one component. We set the maximum threat allowed (ζ) at a conservative 5% to ensure the feasibility of the test instances. The actual maximum threat is between 1 and 2%.

To evaluate the efect of constrained budgetary resources on the optimal solution, the θ values listed in Table 12 represent the per-unit relative cost ratio between a prevention safeguard and a detection & containment safeguard, and η denotes the maximum number of safeguards the firm can aford. For example, θ = 1 indicates a cost-neutral position; the two types of safeguards have equal cost weight in constraint C6.

## 5. Computational results

We conducted the analyses in this section using IBM ILOG CPLEX Optimization Studio version 12.7.1 on a computer with a 1.7GHz processor and 8 GB RAM. We first report results from deterministic model L\_M in which the uncertainty parameters , $\widetilde { \delta _ { i k d } } .$ , and $\widetilde { C _ { k j } ^ { \prime } }$ are set to their nominal values. We aim to analyze (a) the optimal number of prevention and detection & containment safeguards; (b) their social cost; and (c) their efectiveness by varying θ (cost structure) and η (available resource). In the subsequent runs, we test robust model R\_L\_M to further examine our three aims under various uncertainty settings.

## 5.1. Deterministic results for model L\_M

We used the data discussed in Section 4 to test our deterministic model L\_M. Specifically, by varying θ and $\eta ,$ Table 12 settings lead to 25 test scenarios as shown in Table 13. For each scenario, we found the

0% of detection & containment (0 used divided by the total 5) are activated. In Table 15, we also draw borders around the scenarios in which the percentage of detection & containment safeguards reported is higher than prevention safeguards, and Table 16 shows the reduction in social cost as compared to $\eta = 1$

The results indicate that when resources are highly constrained $( \eta = 1 ) _ { \mathrm { { } } }$ , they are usually allocated for prevention rather than containment & detection, regardless of the cost structure θ. However, as resource parameter η relaxes, we observe a systematic shift toward containment & detection. When containment & detection has a cost advantage $( \theta = 0 . 5$ and 0.75). the shift starts earlier $( \eta = 4$ and 7) than when it has a cost disadvantage (θ = 1.25 and 1.5). Partly due to this shift, Table 16 shows a great reduction in social costs, although increases in resource η also contribute to the reduction.

This evidence points to a serious flaw in frameworks that consider only prevention. When resources are highly constrained, the damage of leaving out containment & detection safeguards may seem negligible but not in the current environment of increasing concern over breaches and cybersecurity spending. Our results strongly indicate an allocation preference toward containment & detection when additional resources become available, even when the cost disadvantage is significant (e.g., scenarios 24 and 25).<sup>3</sup> This pattern warrants further exploration, so we use scenarios 24 and 25 as a testbed to reveal the root cause. In scenario 24, the optimal number of prevention and detection & containment safeguards is 8–1 (or 89–20%), with prevention dominating significantly. However, when η increases from 10 to 13, the new optimal solution reverses to 5–5 (or 56–100%), with a strong preference de tection & containment.

Fig. 3 demonstrates the dynamics of resource flow. The starting point, 8–1, is the optimal solution for scenario 24 $( \eta = 1 0$ and θ = 1.5) with a social cost of \$126,251. Four additional units become available in scenario 25, and we test five candidate solutions in allocating them (8–3, 7–4, 6–4, 5–5, and 4–6). For example, we could keep the number of prevention safeguards at 8 and increase the number of detection &

Table 11  
Coverage between threats and components $( \omega _ { k m } ) .$

<table><tr><td></td><td>General server</td><td>Servers under Unix</td><td>Web servers</td><td>Databases</td><td>Web applications</td></tr><tr><td>Malicious insiders</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>Malicious code</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>Web-based attacks</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>Phishing &amp; SE</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Denial of service</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>Stolen devices</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Malware</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>Botnets</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr></table>

Table 12  
Parametric settings for θ and η.

<table><tr><td>Theta</td><td>Eta</td></tr><tr><td>0.5</td><td>1</td></tr><tr><td>0.75</td><td>4</td></tr><tr><td>1</td><td>7</td></tr><tr><td>1.25</td><td>10</td></tr><tr><td>1.5</td><td>13</td></tr></table>

Table 17  
Scenarios used in testing robust model R\_L\_M

<table><tr><td>Theta/Eta</td><td>1</td><td>4</td><td>7</td><td>10</td><td>13</td></tr><tr><td>0.5</td><td></td><td>2</td><td></td><td>4</td><td></td></tr><tr><td>0.75</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td></td><td>12</td><td></td><td>14</td><td></td></tr><tr><td>1.25</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1.5</td><td></td><td>22</td><td></td><td>24</td><td></td></tr></table>

Table 13  
Twenty-five scenarios by varying θ and η.

<table><tr><td>Theta/Eta</td><td>1</td><td>4</td><td>7</td><td>10</td><td>13</td></tr><tr><td>0.5</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>0.75</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>1</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td></tr><tr><td>1.25</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td></tr><tr><td>1.5</td><td>21</td><td>22</td><td>23</td><td>24</td><td>25</td></tr></table>

Table 18  
Optimal percent of prevention vs. detection & containment by Varying <sup>⁎</sup>.

<table><tr><td rowspan="2">Theta/Eta</td><td colspan="4">4</td></tr><tr><td>0%</td><td>2.50%</td><td>5%</td><td>7.50%</td></tr><tr><td>0.5</td><td>22%-80%</td><td>22%-80%</td><td>22%-80%</td><td>22%-80%</td></tr><tr><td>0.75</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>44%-0%</td><td>44%-0%</td><td>44%-0%</td><td>44%-0%</td></tr><tr><td>1.25</td><td></td><td></td><td></td><td></td></tr><tr><td>1.5</td><td>44%-0%</td><td>44%-0%</td><td>44%-0%</td><td>44%-0%</td></tr></table>

Table 14  
Optimal number of prevention vs. detection & containment safeguard.

<table><tr><td>Theta/Eta</td><td>1</td><td>4</td><td>7</td><td>10</td><td>13</td></tr><tr><td>0.5</td><td>1-0</td><td>2-4</td><td>4-4</td><td>7-5</td><td>9-5</td></tr><tr><td>0.75</td><td>1-0</td><td>4-0</td><td>3-5</td><td>6-5</td><td>9-5</td></tr><tr><td>1</td><td>1-0</td><td>4-0</td><td>6-1</td><td>5-5</td><td>8-5</td></tr><tr><td>1.25</td><td>1-0</td><td>4-0</td><td>7-0</td><td>5-4</td><td>6-5</td></tr><tr><td>1.5</td><td>1-0</td><td>4-0</td><td>7-0</td><td>8-1</td><td>5-5</td></tr></table>

Table 15  
Optimal percentage of prevention vs. detection & containment safeguard.

<table><tr><td rowspan="2">Theta/Eta</td><td colspan="4">10</td></tr><tr><td>0%</td><td>2.50%</td><td>5%</td><td>7.50%</td></tr><tr><td>0.5</td><td>78%-100%</td><td>78%-100%</td><td>78%-100%</td><td>78%-100%</td></tr><tr><td>0.75</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>56%-100%</td><td>56%-100%</td><td>56%-100%</td><td>56%-100%</td></tr><tr><td>1.25</td><td></td><td></td><td></td><td></td></tr><tr><td>1.5</td><td>89%-20%</td><td>89%-20%</td><td>89%-20%</td><td>89%-20%</td></tr></table>

<table><tr><td>Theta/Eta</td><td>1</td><td>4</td><td>7</td><td>10</td><td>13</td></tr><tr><td>0.5</td><td>11%-0%</td><td>22%-80%</td><td>44%-80%</td><td>78%-100%</td><td>100%-100%</td></tr><tr><td>0.75</td><td>11%-0%</td><td>44%-0%</td><td>33%-100%</td><td>67%-100%</td><td>100%-100%</td></tr><tr><td>1</td><td>11%-0%</td><td>44%-0%</td><td>67%-20%</td><td>56%-100%</td><td>89%-100%</td></tr><tr><td>1.25</td><td>11%-0%</td><td>44%-0%</td><td>78%-0%</td><td>56%-80%</td><td>67%-100%</td></tr><tr><td>1.5</td><td>11%-0%</td><td>44%-0%</td><td>78%-0%</td><td>89%-20%</td><td>56%-100%</td></tr></table>

Table 16  
Social-cost reduction compared to $\eta = 1 .$

<table><tr><td>Social Cost</td><td>1</td><td>4</td><td>7</td><td>10</td><td>13</td></tr><tr><td>0.5</td><td>$ 437,761</td><td>-52%</td><td>-76%</td><td>-84%</td><td>-85%</td></tr><tr><td>0.75</td><td>$ 437,761</td><td>-49%</td><td>-71%</td><td>-82%</td><td>-85%</td></tr><tr><td>1</td><td>$ 437,761</td><td>-49%</td><td>-66%</td><td>-80%</td><td>-85%</td></tr><tr><td>1.25</td><td>$ 437,761</td><td>-49%</td><td>-64%</td><td>-72%</td><td>-82%</td></tr><tr><td>1.5</td><td>$ 437,761</td><td>-49%</td><td>-64%</td><td>-71%</td><td>-80%</td></tr></table>

<sup>⁎</sup> The top table (Eta = 4) shows scenarios 2, 12, and 22, and the bottom (Eta = 10) scenarios 4, 14, and 24. Tables 19-21 follow the same structure.

containment safeguards to 3 (candidate solution #2), using a total of 12.5 units (8 + 1.5\*3) and reducing social cost 14.08%. Candidate solution #3, 7–4, further diverts resources to detection & containment for a 24% reduction in social cost. The flow of resources continues, and, at

Table 19  
Social cost increase by varying $\widetilde { \lambda _ { k d } } .$

<table><tr><td rowspan="2">Theta/Eta</td><td colspan="4">4</td></tr><tr><td>0%</td><td>2.50%</td><td>5%</td><td>7.50%</td></tr><tr><td>0.5</td><td>$ 210,842</td><td>5%</td><td>11%</td><td>16%</td></tr><tr><td>0.75</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>$ 224,060</td><td>8%</td><td>15%</td><td>22%</td></tr><tr><td>1.25</td><td></td><td></td><td></td><td></td></tr><tr><td>1.5</td><td>$ 224,060</td><td>8%</td><td>17%</td><td>25%</td></tr><tr><td rowspan="2">Theta/Eta</td><td colspan="4">10</td></tr><tr><td>0%</td><td>2.50%</td><td>5%</td><td>7.50%</td></tr><tr><td>0.5</td><td>$ 69,988</td><td>19%</td><td>38%</td><td>57%</td></tr><tr><td>0.75</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>$ 88,729</td><td>14%</td><td>28%</td><td>43%</td></tr><tr><td>1.25</td><td></td><td></td><td></td><td></td></tr><tr><td>1.5</td><td>$ 126,251</td><td>15%</td><td>31%</td><td>43%</td></tr></table>

Optimal percent of prevention vs. detection & containment safeguards by varying <sub>ikd</sub> .

<table><tr><td rowspan="2">Theta/Eta</td><td colspan="4">4</td></tr><tr><td>0%</td><td>2.50%</td><td>5%</td><td>7.50%</td></tr><tr><td>0.5</td><td>22%-80%</td><td>22%-80%</td><td>22%-80%</td><td>22%-80%</td></tr><tr><td>0.75</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>44%-0%</td><td>44%-0%</td><td>33%-20%</td><td>33%-20%</td></tr><tr><td>1.25</td><td></td><td></td><td></td><td></td></tr><tr><td>1.5</td><td>44%-0%</td><td>44%-0%</td><td>44%-0%</td><td>44%-0%</td></tr></table>

<table><tr><td rowspan="2">Theta/Eta</td><td colspan="4">10</td></tr><tr><td>0%</td><td>2.50%</td><td>5%</td><td>7.50%</td></tr><tr><td>0.5</td><td>78%-100%</td><td>78%-100%</td><td>78%-100%</td><td>78%-100%</td></tr><tr><td>0.75</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>56%-100%</td><td>56%-100%</td><td>56%-100%</td><td>56%-100%</td></tr><tr><td>1.25</td><td></td><td></td><td></td><td></td></tr><tr><td>1.5</td><td>89%-20%</td><td>89%-20%</td><td>89%-20%</td><td>44%-80%</td></tr></table>

Table 21  
Social cost increase by varyin $\widetilde { \delta _ { i k d } }$

<table><tr><td rowspan="2">Theta/Eta</td><td colspan="4">4</td></tr><tr><td>0%</td><td>2.50%</td><td>5%</td><td>7.50%</td></tr><tr><td>0.5</td><td>$ 210,842</td><td>5%</td><td>11%</td><td>16%</td></tr><tr><td>0.75</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>$ 224,060</td><td>8%</td><td>15%</td><td>22%</td></tr><tr><td>1.25</td><td></td><td></td><td></td><td></td></tr><tr><td>1.5</td><td>$ 224,060</td><td>8%</td><td>17%</td><td>25%</td></tr><tr><td rowspan="2">Theta/Eta</td><td colspan="4">10</td></tr><tr><td>0%</td><td>2.50%</td><td>5%</td><td>7.50%</td></tr><tr><td>0.5</td><td>$ 69,988</td><td>19%</td><td>38%</td><td>57%</td></tr><tr><td>0.75</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>$ 88,729</td><td>14%</td><td>28%</td><td>43%</td></tr><tr><td>1.25</td><td></td><td></td><td></td><td></td></tr><tr><td>1.5</td><td>$ 126,251</td><td>15%</td><td>31%</td><td>43%</td></tr></table>

Optimal percent of prevention vs. detection & containment safeguards by varying $\widetilde { C _ { k j } ^ { \prime } }$ .

<table><tr><td rowspan="2">Theta/Eta</td><td colspan="4">4</td></tr><tr><td>0%</td><td>2.50%</td><td>5%</td><td>7.50%</td></tr><tr><td>0.5</td><td>22%-80%</td><td>33%-40%</td><td>33%-20%</td><td>33%-20%</td></tr><tr><td>0.75</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>44%-0%</td><td>44%-0%</td><td>44%-0%</td><td>44%-0%</td></tr><tr><td>1.25</td><td></td><td></td><td></td><td></td></tr><tr><td>1.5</td><td>44%-0%</td><td>44%-0%</td><td>44%-0%</td><td>44%-0%</td></tr></table>

<table><tr><td rowspan="2">Theta/Eta</td><td colspan="4">10</td></tr><tr><td>0%</td><td>2.50%</td><td>5%</td><td>7.50%</td></tr><tr><td>0.5</td><td>78%-100%</td><td>78%-100%</td><td>78%-100%</td><td>78%-100%</td></tr><tr><td>0.75</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>56%-100%</td><td>56%-100%</td><td>56%-100%</td><td>56%-100%</td></tr><tr><td>1.25</td><td></td><td></td><td></td><td></td></tr><tr><td>1.5</td><td>89%-20%</td><td>89%-20%</td><td>89%-20%</td><td>89%-20%</td></tr></table>

candidate solution #5, showing 5–5, the minimum social cost of \$88,729 represents a 29.72% reduction. The last candidate solution, 4–6, demonstrates that further resource flow in this direction increases social cost over its minimum. Although we focus our analysis here on scenarios 24 and 25, the pattern and insights revealed are applicable to other scenarios exhibiting a similar reversal in resource allocation.

Table 23  
Social-cost increase by varying $\widetilde { C _ { k j } ^ { \prime } }$

<table><tr><td rowspan="2">Theta/Eta</td><td colspan="4">4</td></tr><tr><td>0%</td><td>2.50%</td><td>5%</td><td>7.50%</td></tr><tr><td>0.5</td><td>$ 210,842</td><td>16%</td><td>27%</td><td>35%</td></tr><tr><td>0.75</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>$ 224,060</td><td>5%</td><td>18%</td><td>23%</td></tr><tr><td>1.25</td><td></td><td></td><td></td><td></td></tr><tr><td>1.5</td><td>$ 224,060</td><td>5%</td><td>9%</td><td>20%</td></tr><tr><td rowspan="2">Theta/Eta</td><td colspan="4">10</td></tr><tr><td>0%</td><td>2.50%</td><td>5%</td><td>7.50%</td></tr><tr><td>0.5</td><td>$ 69,988</td><td>6%</td><td>12%</td><td>17%</td></tr><tr><td>0.75</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>$ 88,729</td><td>5%</td><td>15%</td><td>20%</td></tr><tr><td>1.25</td><td></td><td></td><td></td><td></td></tr><tr><td>1.5</td><td>$ 126,251</td><td>6%</td><td>12%</td><td>18%</td></tr></table>

## 5.2. Robust results from model R\_L\_M

The results presented in Section 5.1 set the stage for testing robust model R\_L\_M. Six scenarios (see Table 17) provide a comprehensive platform for examining the impact caused by uncertainty in $\widetilde { \lambda _ { k d } } , \widetilde { \delta _ { i k d } } ,$ and $\widetilde { C _ { k j } ^ { \prime } }$ . For each source of uncertainty, we test three levels: maximum deviations are allowed to vary by 2.5, 5, or 7.5%, while the size is fixed at the middle level. This design yields a total of 54 (6\*3\*3) test pro blems. Note that the deterministic results representing 0% deviation are used as a baseline.

## 5.2.1. Likelihood of attack $\widetilde { ( \lambda _ { k d } ) }$

Good government intelligence and preemptive eforts can deter cyberattacks. Table 18 shows that the resource allocation preference noted in our deterministic runs holds for all six scenarios under all three uncertainty levels. Preference for prevention holds for scenarios 12, 22, and 24 and detection & containment for scenarios 2, 4, and 14. Since the robust model is extreme-value-driven, hedging against the worstcase realization of uncertainty, social costs climb with increasing deviation across all six scenarios (Table 19). However, one interesting pattern emerges. Social costs show a higher percentage increase in scenarios where resources are less restricted (i.e., η = 10); in a deterministic setting, more resources lower social cost, but the percent increases are greater under all three levels tested. In the worst case, the percent increase jumps to 57, given θ = 0.5 and the maximum deviation of 7.5%.

## 5.2.2. Adjusted prevention safeguard efectiveness $\widetilde { ( \delta _ { i k d } } )$

Parameter $\widetilde { \delta _ { i k d } }$ is a product of parameters $\widetilde { \lambda _ { k d } }$ and $\widetilde { C _ { i k , = ; } }$ hence, we term it adjusted prevention safeguard efectiveness. In determining social cost, it considers the likelihood of attack, $\widetilde { \lambda _ { k d } } .$ , and prevention safeguard efectiveness, $\widetilde { C _ { i k } } .$ , as a good proxy for technology efectiveness or improvement. For example, if firms or government allocate insuficient resources to research and development, prevention safeguards will be less efective. Tables 20 and 21 summarize results.

First, in scenarios 12 and 24, we observe a shift in resource allocation toward detection & containment in response to increasing uncertainty. Detection & containment safeguards remain dominant across three uncertainty levels in scenarios 2, 4, and 14, while prevention dominates in scenario 22. Recall that the robust model is built to hedge against the worst-case realization of uncertainty, or the case when the adjusted efectiveness of prevention safeguard is reduced by 2.5, 5, or 7.5% as characterized by ellipsoidal uncertainty. In the face of less effective prevention safeguards, a sensible strategy diverts resources to detection & containment to minimize the maximum social cost as shown in two scenarios.

![](/api/attachments/7KWJMYZQ/fulltext/images/75a5a6771a6b71f085903cc90a3647fe7729fb6af9a07dae0b647ddeb664d63e.jpg)  
Fig. 3. Social-cost reduction for candidate solutions in scenario 25.

Second, consistent with the patterns identified in the deterministic run, more resources $( \eta = 1 0 )$ and cost advantages promote detection & containment safeguards $( \theta = 0 . 5 )$ . For example, given $\eta = 4 _ { \mathrm { { a } } }$ , detection & containment dominates at 80% when $\theta = 0 . 5$ and slowly gain ground under $\theta = 1$

These results reinforce the importance of including detection & containment safeguards when evaluating cybersecurity readiness. While in a deterministic setting, leaving them out causes minimal harm, under constrained resources and cost disadvantages, this benefit fades. In scenario 12, the starting cost diference of 44% vs 0% shifts to 33% vs 20% under the maximum deviations of 5 and 7.5%. Finally, as Table 21 shows, this source of uncertainty increases social cost more than the other two sources. The resource flow toward detection & containment and away from efective prevention increases social cost. Note that the percent increases in social cost are still greater when resources are less restricted $( \mathrm { i } . \mathbf { e } . , \eta = 1 0 )$

## 5.2.3. Social cost ( C<sub>kj</sub> )

Tables 22 and 23 summarize the results of varying the social cost, C , by 2.5, 5, and 7.5%, a good proxy for the value of information to individuals who use at-risk services. Underestimating the value of personal data can significantly impair optimal selection of countermeasures. We observe a change in resource allocation only in scenario 2 with a systematic shift toward prevention, in line with the finding in the deterministic run that when resources are constrained, a higher percentage of prevention is preferred. In scenarios 12 and 22, all resources are diverted toward prevention (44%–0%). In scenario 2, the cost ad vantage of detection & containment (θ = 0.5) supports starting at 80%, but it quickly shrinks to 40% at 2.5% maximum deviation and stabilizes at 20% at 5% and 7.5% deviation. The magnitude of change in social cost is in line with deviations in likelihood of attack, and both are far outpaced by deviations in adjusted efectiveness of prevention safeguard.

## 6. Conclusions and future research

We use social cost to determine the optimal balance between prevention and detection & containment safeguards. Our robust model, based on an ellipsoid uncertainty set, can help decisionmakers to allocate safeguards against cyberattack under three common sources of uncertainty. We first analyze the trade-ofs between the two types of safeguards and their associated social cost under diferent cost structures and resource constraints in a deterministic setting, followed by a more in-depth analysis of the issues under various configurations of three uncertainty settings.

Results from twenty-five deterministic test scenarios first reveal strong resource allocation preference toward prevention safeguard and, with relaxing constraint, it shifts to containment & detection safeguard regardless of the cost structure. Our analysis reafirms the preference for prevention as the first line of defense but also points to its diminishing impact on minimizing social cost. Specifically, after a certain point, additional resource invested in prevention safeguard has minimal, if any, efect on driving down social cost but takes away cri tical resources that could be more efectively invested in detection & containment safeguard. Results from 36 robust test instances indicate that the adjusted efectiveness of prevention safeguard has greater impact on both social cost and optimal configuration of safeguards than uncertainties in the likelihood of attack and social cost.

Our analysis centers on the individual firm. In future, we plan to consider government and the attacker and how their strategic actions and interactions may influence a firm's decisions. While we consider externality costs to a firm in terms of its customers and the monetary value associated with information loss as a function of detection and containment, we have yet to consider positive externality due to increased cybersecurity investment overall. With cybersecurity receiving increased attention and benefits of information sharing been increasingly recognized by firms, we hope to improve our models as organizations become more willing to share data. For example, we would like to incorporate the purchase price of diferent types of safeguards and a more in-depth analysis of budgetary constraints.

## References

[1] L.A. Gordon, M.P. Loeb, W. Lucyshyn, L. Zhou, Increasing cybersecurity investments in private sector firms, Journal of Cybersecurity 1. (2015) 3–17.

[2] White House, FACT SHEET: cyber threat intelligence integration center, Retrieved April 20, 2018, from, 2015. https://www.whitehouse.gov/the-press-ofice/2015/ 02/25/fact-sheet-cyber-threat-intelligence-integration-center.

[3] J. Comey, Confirmation hearing of James Comey, Retrieved April 20, 2018, from, 2013. https://www.fbi.gov/news/podcasts/thisweek/james-comeys-confirmationhearing.mp3/view.

[4] CNBC, How the yahoo hack stacks up to previous data breaches, (2017) Retrieved April 20, 2018, from https://www.cnbc.com/2017/10/04/how-the-yahoo-hackstacks-up-to-previous-data-breaches.html

[5] CNN, Yahoo tops the list of largest ever data breaches, Retrieved April 20, 2018, from, 2017. http://money.cnn.com/2017/10/04/technology/yahoo-biggest-databreaches-ever/index.html.

[6] National Public Radio (NPR), Time is running out for Atlanta in ransomware attack, Retrieved April 20, 2018, from, 2018. https://www.npr.org/sections/thetwo-way 2018/03/28/597758947/time-is-running-out-for-atlanta-in-ransomware-attack.

[7] eSecurity Planet, Target breach had massive impact on cybersecurity awareness, Retrieved April 25, 2018, from, 2015. https://www.esecurityplanet.com/network security/target-breach-had-massive-impact-on-cyber-security-awareness.html.

[8] DARKReading, Security budgets going up, thanks to mega-breaches, Retrieved Apri 25, 2018, from, 2015. https://www.darkreading.com/attacks-breaches/securitybudgets-going-up-thanksto-mega-breaches/d/d-id/1318714?piddl\_msgorder=asc.

[9] Wall Street Journal, FICO chief increases cybersecurity spending after Equifax breach, Retrieved April 25, 2018, from, 2017. https://blogs.wsj.com/cio/2017/09 22/fico-chief-increases-cybersecurity-spending-after-equifax-breach/.

[10] N.L. Beebe, D.K. Young, F.R. Chang, Framing information security budget requests to influence investment decisions, Communications of the Association for Information Systems (7) (2014) 35.

[11] L.A. Gordon, M.P. Loeb, The economics of cybersecurity investment, ACM Transactions on Information System Security 5 (2002) 438–457.

[12] M. LeLarge, Coordination in network security games: a monotone comparative statics approach, IEEE Journal on Selected Areas in Communications 30 (2012) 2210-2219.

[13] S.S. Wang, Optimal level and allocation of cybersecurity spending: model and formula, Retrieved March 29, 2019, from, 2017. https://ssrn.com/abstract= 3010029.

[14] IT Governance, Boardroom cyber watch survey 2014, Retrieved April 23, 2018, from, 2014. http://www.itgovernanceusa.com/download/Boardroom-Cyber-Watch-2014\_US-Report.pdf.

[15] Forbes, How to prevent cyber crime, Retrieved October 7, 2018, from, 2013. https://www.forbes.com/sites/thesba/2013/08/28/how-to-prevent-cybercrime/#62f3ad6efffd

[16] CNBC, UK businesses were hit 230,000 times each by cyber-attacks in 2016, says internet service provider, Retrieved October 7, 2018, from, 2017. https://www. cnbc.com/2017/01/11/uk-businesses-were-hit-230000-times-each-by-cyberattacks-in-2016-says-internet-service-provider.html.

[17] ZDNet, Most companies take over six months to detect data breaches, Retrieved October 7. 2018. from. 2015. https://www.zdnet.com/article/businesses-take-over six-months-to-detect-data-breaches/.

[18] National Institute of Standards and Technology (NIST), Framework for improving critical infrastructure cybersecurity, Retrieved October 7, 2018, from, 2018. https://nylpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.04162018.pdf

[19] A. Schilling, A framework for secure IT operations in an uncertain and changing environment. Computers & Operations Research 85 (2017) 139–153

[20] A. Schilling, B. Werners, Optimal selection of IT security safeguards from an existing knowledge base. European Journal of Operational Research 248 (1) (2016 318–327.

[21] C. Purtill, The Equifax breach will most hurt the people who can least aford it, Retrieved May 14. 2018. from. 2017. https://gz.com/1079138/whats-the-worst that-can-happen-with-the-equifax-breach-a-lot-especially-if-youre-poor/.

[22] Council of Economic Advisers, The cost of malicious cyber activity to the U.S. economy, Retrieved March 29, 2019, from, 2018. https://www,whitehouse,gov/ wp-content/uploads/2018/02/The-Cost-of-Malicious-Cyber-Activity-to-the-U.S.- Economy.pdf.

[23] Organisation for Economic Co-operation and Development (OECD). Cybersecurity policy making at a turning point, Retrieved March 29, 2019, from, 2012. https:// www.oecd.org/sti/ieconomy/cybersecurity%20policy%20making.pdf.

[24]. K Hausken. Returns to information security investment: the effect of alternative information security breach functions on optimal investment and sensitivity to vulnerability. Information Systems Frontiers 5 (8) (2006).

[25] Y. Baryshnikov, IT security investment and Gordon-Loeb's 1/e rule, Workshop on Economics and Information Security, Berlin, 25–26 June, 2012.

[26] K. Campbell, L.A. Gordon, M.P. Loeb, L. Zhou, The economic cost of publicly announced information security breaches: empirical evidence from the stock market Journal of Computer Security 11 (3) (2003) 431–448.

[27] H. Cavusoglu, B. Mishra, S. Raghunathan, The efect of internet security breach announcements on market value: capital market reaction for breached firms and internet security developers. International Journal of Electronic Commerce 9 (1) (2004) 69–105.

[28] H. Varian, System reliability and free riding, in: L.J. Camp, S. Lewis (Eds.), Economics of Information Security, Springer, USA, 2004, pp. 1–15.

[29] L.A. Gordon, M. Loeb, W. Lucyshyn, Sharing information on computer systems security: an economic analysis, Journal of Accounting and Public Policy 22 (6) (2003) 461–485.

[30] E. Gal-Or, A. Ghose, The economic incentives for sharing security information, Information Systems Research 16 (2) (2005) 186–208.

[31] S. Romanosky, Examining the costs and causes of cyber incidents, Journal of Cybersecurity (2016) 1–15.

[32] V. Viduto, C. Maple, W. Huang, D. López-Peréz, A novel risk assessment and opti misation model for a multi-objective network security countermeasure selection problem, Decision Support Systems 53 (3) (2012) 599–610.

[33] T.R. Rakes, J.K. Deane, P.L. Rees, IT security planning under uncertainty for highimpact events, Omega 40 (1) (2012) 79–88.

[34] T. Sawik, Selection of optimal counter measure portfolio in IT security planning, Decision Support Systems 55 (1) (2013) 156–164.

[35] L.P. Rees, J.K. Deane, T.R. Rakes, W.H. Baker, Decision support for cybersecurit risk planning, Decision Support Systems 51 (3) (2011) 493–505.

[36] D. Bertsimas, A. Thiele, Robust and data-driven optimization: Modern decision making under uncertainty, INFORMS Tutorials in Operations Research: Models, Methods, and Applications for Innovative Decision Making, 2006, p. 137

[37] D. Bertsimas, D.B. Brown, C. Caramanis, Theory and applications of robust opti mization, SIAM Review 53 (3) (2011) 464–501.

[38] A.L. Soyster, Technical note: convex programming with set-inclusive constraint and applications to inexact linear programming, Operations Research 21 (5) (1973) 1154–1157.

[39] L. El Ghaoui, F. Oustry, H. Lebret, Robust solutions to uncertain semidefinite programs, SIAM Journal on Optimization 9 (1) (1998) 33–52.

[40] A. Ben-Tal, A. Nemirovsky, Robust convex optimization, Mathematics of Operation Research 23 (4) (1998) 769–805

[41] A. Ben-Tal, A. Nemirovski, Robust solutions of uncertain linear programs, Operations Research Letters 25 (1) (1999) 1–13

[42] D. Bertsimas, M. Sim, Robust discrete optimization and network flows, Mathematical Programming 98 (2003) 48–71.

[43] L.V. Snyder, M.S. Daskin, Stochastic p-robust location problems, IIE Transactions 38 (11) (2006) 971–985.

[44] O. Baron, J. Milner, H. Naseraldin, Facility location: a robust optimization approach, Production and Operations Management 20 (5) (2011) 772–785.

[45] J.A. Paul, X.J. Wang, Robust optimization for United States Department of Agriculture food aid bid allocations, Transportation Research Part E: Logistics and Transportation Review 82 (2015) 129–146.

[46] D. Bertsimas, M. Sim, The price of robustness, Operations Research 52 (1) (2004) 35-53.

[47] T. Homem-de-Mello, B.K. Pagnoncelli, Risk aversion in multistage stochastic pro gramming: a modeling and algorithmic perspective, European Journal of Operational Research 249 (1) (2016) 188–199.

[48] J. Holguín-Veras, N. Pérez, M. Jaller, L.N. Van Wassenhove, F. Aros-Vera, On the appropriate objective function for post-disaster humanitarian logistics models, Journal of Operations Management 31 (5) (2013) 262–280

[49] J.A. Paul, X.J. Wang, Robust Location-allocation network design for earthquake preparedness, Transportation Research Part B: Methodological 119 (2019) 139–155.

[50] X.J. Wang, J.A. Paul, Robust Optimization for Hurricane Preparedness, (2017) (Working Paper).

[51] Ponemon Institute, 2016 cost of cyber crime study & the risk of business innovation, Retrieved April 3. 2018. from. 2016. https://www.ponemon.org/blog/2016-costof-cyber-crime-studv-the-risk-of-business-innovation.

[52] German Federal Office for Information Security, IT-Grundschutz-Catalogues: 13th version. (2013).

Jomon A. Paul is a Professor of Ouantitative Analysis and Director of Research at the Coles College of Business. Kennesaw State University. He earned a B.E. in Mechanical Engineering from MS University, Vadodara, India, and an M.S. and Ph.D. in Industrial Engineering from the University at Bufalo. His primary research interests include application of operations research, simulation and statistical modeling to disaster planning, healthcare, and transportation domains. He is a member of the Institute for Operations Research and the Management Sciences (INFORMS), the Decision Sciences Institute (DSD). and a senior member of the American Society of Quality (ASQ). His research has appeared in Operations Research, Transportation Research Part B: Methodological, Transportation Research Part E: Logistics and Transportation Review, European Journal of Operational Research, International Journal of Production Economics, Journal of the Operational Research Society, Journal of Business Ethics, Annals of Operations Research, Journal of Emergency Medicine, Journal of Homeland Security and Emergency Management among several others He is an ASO certified Six Sigma Black Belt. He is on the editorial board for the International Journal of Information Systems and Social Change.

Xinfang Wang is an Associate Professor of Ouantitative Analysis in the Department of Logistics and Supply Chain Management at Georgia Southern University. She holds a BS in International Business from Shanghai University (1999) and a Ph.D. in Management Science from the University of Cincinnati (2007). She was a visiting assistant professor of operations management at the SUNY-Binghamton from 2007 to 2008. She has taught quantitative analysis and operations management courses at both undergraduate and graduate levels and published in journals such as Management Science, OMEGA, Journal of the Operational Research Society, Transportation Research Part B: Methodological, and Transportation Research Part E: Logistics and Transportation Review. Her main research in terests are in the areas of discrete optimization modeling and conjoint product design.
