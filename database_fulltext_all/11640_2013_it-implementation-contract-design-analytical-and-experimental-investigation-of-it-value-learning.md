---
otero_id: 11640
otero_key: "QK3DACZ5"
title: "IT Implementation Contract Design: Analytical and Experimental Investigation of IT Value, Learning, and Contract Structure"
authors: "D. J. Wu; Min Ding; Lorin M. Hitt"
year: "2013"
journal: "Information Systems Research"
doi: "10.1287/isre.1120.0448"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/QK3DACZ5/fulltext/images/10c8d7a84896798a04012e33f2bc05dcd665ba3d5dac55073d9785cff22c9ac7.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# IT Implementation Contract Design: Analytical and Experimental Investigation of IT Value, Learning, and Contract Structure

D. J. Wu, Min Ding, Lorin M. Hitt

## To cite this article:

D. J. Wu, Min Ding, Lorin M. Hitt (2013) IT Implementation Contract Design: Analytical and Experimental Investigation of IT Value, Learning, and Contract Structure. Information Systems Research 24(3):787-801. http://dx.doi.org/10.1287/ isre.1120.0448

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2013, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/QK3DACZ5/fulltext/images/369276325f5ba903ff57659fbf416fb4c84330a57893645081019ec5a9901cfc.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# IT Implementation Contract Design: Analytical and Experimental Investigation of IT Value, Learning, and Contract Structure

D. J. Wu Scheller College of Business, Georgia Institute of Technology, Atlanta, Georgia 30332, dj.wu@scheller.gatech.edu

Min Ding

Smeal College of Business, Pennsylvania State University, University Park, Pennsylvania 16802; and School of Management, Fudan University, Shanghai, P. R. China, 200433, minding@psu.edu

Lorin M. Hitt The Wharton School, University of Pennsylvania, Philadelphia, Pennsylvania 19104, lhitt@wharton.upenn.edu

his article analytically and experimentally investigates how firms can best capture the business value of information technology (IT) investments through IT contract design. Using a small sample of outsourcing contracts for enterprise information technology (EIT) projects in several industries—coupled with reviews of contracts used by a major enterprise software maker—the authors determine the common provisions and structural characteristics of EIT contracts. The authors use these characteristics to develop an analytical model of optimal contract design with principal–agent techniques. The model captures a set of key characteristics of EIT contracts, including a staged, multiperiod project structure; learning; probabilistic binary outcomes; variable fee structures; possibly risk-averse agents; and implementation risks. The model characterizes conditions under which multistage contracts enable clients to create and capture greater project value than single-stage projects, and how project staging enables firms to reduce project risks, capture learning benefits, and increase development effort. Finally, the authors use controlled laboratory experiments to complement their analytical approaches and demonstrate robustness of their key findings.

Key words: analytical modeling; enterprise systems; economics of IS; management of IS projects; laboratory experiments; business value of IT

History: Anitesh Barua, Senior Editor; Gautam Ray, Associate Editor. This paper was received on April 22, 2009, and was with the authors 20 months for 2 revisions. Published online in Articles in Advance October 5, 2012.

## 1. Motivation

Large-scale enterprise IT (EIT) implementation projects (e.g., Chellappa and Saraf 2010, Hitt et al. 2002) are risky by nature (Haines and Goodhue 2003, McFarlan 1981, O’Leary 2002). According to a report by a leading enterprise resource planning (ERP) vendor, 51% of projects suffered from unforeseen implementation issues, 53% of projects exceeded cost estimates, 83% of projects were delivered late or over budget, 42% of projects had incomplete features or functions, and 40% of projects failed to achieve their business cases (Pike 2006). Empirical evidence in an ERP context suggests that managers and investors perceive particularly high risks for EIT projects (e.g., Hitt et al. 2002). EIT projects typically get outsourced to consulting companies for implementation and maintenance. Such projects are notoriously complicated and place burdens on the design of IT outsourcing relationships, especially on the contracts that codify these relationships. Nearly all large firms have, or are in the process of implementing, large-scale enterprise systems, and it is not unusual for these projects to include various contracting opportunities spanning multiple years (e.g., O’Leary 2002). Contracts provide the primary means of IT governance (Nolan and McFarlan 2005), codifying client–vendor relationships in IT outsourcing agreements (Clemons et al. 2001). Well-designed contracts can help manage the problems of ex-ante incomplete information (e.g., requirements, client characteristics, or vendor capabilities) and provide a framework for measuring performance, providing incentives, and managing technical, business, and managerial risks. Yet considerable evidence indicates that many outsourcing agreements prove difficult to manage, as reflected in the serious problems observed in some major ERP implementations (e.g., McAfee 2003, Mendelson 2000, Scott 1999).

EIT implementation contracts tend to be similar across different projects because they rely on the commoditization and standardization of business processes (Davenport 2005). In addition, the industry consists of few dominant software vendors and implementation consultants who generally share common business practices. Projects also contain features common to regular IT contracts, though on a larger scale; such as the extensive use of outside consultants, the use of packaged software, and largely observable initial results (i.e., the client can either “go live” with the system or not).

The similarity of ERP contracts across installations and vendors makes it possible to capture the variation of ERP contracts along relatively few dimensions. In this paper, we focus on one particular characteristic that creates considerable variation across projects—the choice between structuring the project as a single-stage “big bang” implementation without any intermediate decision points, and a multistage incremental “rollout” with scheduled intermediate deliverables enabling a “continue or terminate” decision. Thus, a critical question in structuring an ERP project is how long to make each stage, with the possibility that it may be optimal to make the first stage the entire project.

The nature of ERP projects clearly makes stage length a strategic choice. Implementations can be done in the form of a pilot implementation, which is then subsequently rolled out geographically in an identical form to multiple sites. Alternatively, ERP projects can be implemented by module—with core functions implemented over multiple sites (e.g., manufacturing planning, procurement, human resources), followed by additional modules that provide supplemental functionality (e.g., supply chain management, customer relationship management). A multistage contract enables the effective use of information gathered during the project, such as midterm project evaluations, that may reduce subsequent period project risks, improve vendor incentives,<sup>1</sup> or enable early terminations of unsuccessful projects. This phased approach also offers a means to assess best practices and disseminate them to the project team, so teams can improve their performance through learning. Because process redesign and testing, training, and deployment can entail an estimated 12%–15% of total project expenditures in a typical EIT project (Brynjolfsson et al. 2006), client-specific learning can have a significant impact on project value (e.g., Hitt et al. 2002, McAfee 2003). ERP vendors understand the benefits of staging and having a flexible project scope:

Implementation of SAP software is a process that often involves a significant resource commitment by our customers and it is subject to a number of significant risks over which we have little or no control 0 0 0 0 Our customers now increasingly follow modular project approaches to optimize their IT environment. They embark on sequentially integrated individual projects with a comparatively low-risk profile to realize specific potential improvement instead of pursuing highly complex resource-intensive “big bang” projects to implement an all-embracing IT landscape.

(SAP 2008 annual report, p. 123)

Subdividing a project is not without costs, which may explain the use of “big bang” projects in practice. Subdividing a project may increase coordination costs between stages and delay the implementation of later stages, thus reducing or delaying realization of value (e.g., some mission-critical enterprise systems may have more value by going live simultaneously rather than sequentially). Staged implementation may also lead to overinvestments during early periods, as advancing to the next period requires success in the previous period.

Our model focuses specifically on the choice of project staging. We consider a project of fixed duration that can be divided into two stages and outsourced to an implementation vendor. Allowing for different learning processes and project risks, we derive the optimal contract which specifies vendor compensation (fixed and outcome-based payments for each stage) and the optimal stage length. All else being equal, combining the optimal payment structure with a multistage contract allows the client to capture greater overall IT project value, because it mitigates project risks and increases learning benefits by prompting the implementation team to exert greater efforts in early stages. However, under some conditions, such as when there is limited learning, “big bang” full projects can be optimal. These findings are robust to several model extensions. We use controlled laboratory experiments involving students and IT executives to complement our analytical approaches and demonstrate further robustness of our key findings.

All proofs appear in the online supplement of this paper (available at http://dx.doi.org/10.1287/ isre.1120.0448). Due to space limitations, we have omitted details of the laboratory experiments but they are available from the authors upon request.

## 2. Literature Review

Our work draws from three streams of research. We briefly review each, linking key elements of our model to the literature.

2.1. Learning and Dynamic Production Function The first stream of related literature involves the dynamic nature of production processes as firms increase their productive capabilities through experience. Levy (1965) was among the first to model these processes explicitly, using an exponential production function model that enables a firm to accumulate experience in its workforce through training and production activity until it achieves target productivity (or the full potential of its production technology). Gaimon (1997) considers the underlying processes that may characterize the productivity of IT-enabled knowledge work and describes the desirable attributes of a production function in this setting. Gaimon’s analysis suggests that an exponential functional form that incorporates a learning process meets all the required criteria and appears superior to some standard alternatives for modeling IT implementation projects. Case-based research on ERP systems is consistent with a time-dependent learning process, both before and after implementation (McAfee 2002).

We adopt this dynamic production process (learning) view of IT implementation and, specifically, the exponential functional form that characterizes the process (Levy 1965). This structure incorporates decreasing returns, which dates back to Brooks (1975) in the field of software development, and has been well documented in project management literature as well (e.g., Loch and Kavadias 2002), especially in the IT project management literature (e.g., Banker et al. 1998, Barry et al. 2002, Kirsch 2000, McFarlan 1981). We extend Levy’s basic model to capture the key factors in the IT implementation context, including the role of skill, effort, and project size in determining project outcomes, in the presence of both controllable and uncontrollable project risks. Researchers also note that training and learning represent important components of project risk management (Anderson 2001, Banker et al. 1998, Barry et al. 2002, Umble et al. 2003), both before and during a project (Anderson 2001, Gaimon et al. 2011). Thus, we extend and reinterpret Levy’s workforce skill–outcome model by allowing the relationship between effort and project success rate to vary by vendor capability, which can evolve through learning.

## 2.2. Multi-Period Moral Hazard

The second stream of related research entails the wellestablished literature on principal–agent formalisms, which considers the general problem of providing incentives in a variety of settings (e.g., Holmstrom 1982; McAfee and McMillan 1986, 1987). Typically, to mitigate the moral hazard problem that results from unobservable effort by the agent, principals implement incentive contracts that compensate agents on the basis of observable outcomes. The literature has well characterized the properties of the singleperiod principal–agent problem. However, we know significantly less about multiperiod (or finite-horizon) moral hazard games (e.g., Chiappori et al. 1994), the setting that seems to naturally characterize largescale IT implementations. Prior works by Lambert (1983) and Rogerson (1985) suggest a special role of memory in finite horizon moral hazard models, in contrast with infinite horizon models where compensation can be based on long-run summary statistics (e.g., Holmstrom and Milgrom 1987; Radner 1981, 1985). See Chiappori et al. (1994) for a survey of this literature.

We apply the most recent developments in controlling dynamic moral hazard in contract theory in the EIT contract setting with small variations, in order to capture the details and key project characteristics observed from actual EIT contracts, such as the linear fee structure. Essential to EIT projects are linkages between periods, which have rarely been considered in the existing literature. In particular, we consider the potential for change in the effort–output relationship through agent learning over time and risk reduction through information updating over the course of the project.

## 2.3. IT Outsourcing and Contracting

The final stream of related literature pertains to outsourcing risk management (e.g., Clemons et al. 2001) and software development contracting (e.g., Richmond and Seidmann 1993, Richmond et al. 1992, Wang et al. 1997, Whang 1992), as well as the broader literature on IT outsourcing, which has taken a much more qualitative evaluation approach (e.g., DiRomualdo and Gurbaxani 1998, Lacity and Hirschheim 1993, Lacity and Willcocks 1998).

Our analysis complements research that emphasizes monitoring (Nolan and McFarlan 2005) and incentives (Choudhury and Sabherwal 2003) in IT contracting, as well as the uncertainty reduction achieved through information updating over the course of a project (Snir and Hitt 2004, Whang 1992).

Through analyses of actual ERP contracts, we identify at least two major structural dimensions that capture much of the variation in project structure.<sup>2</sup> First, though firms purchase ERP software externally, they must decide whether to perform the implementation in-house (insource) or contract with a service provider (outsource). Second, an outsourced contract can be a single-stage “big bang” implementation or a series of sequentially interlinked subprojects that give the client a termination decision at the end of each period.

Beyond these major decisions, the contracts principally differ in their use of fixed-fee versus incentive payments and the extent to which the vendor makes relationship-specific investments $( \mathrm { e . g . }$ , training, facilities). We observed that the variable portions of payments may be structured in several ways. Some contracts include specific bonus/penalty clauses, others include negotiated rate increases or discounts for future work, and some guarantee a preferential position (“right of first refusal”) to the vendor in future bidding. In one set of contracts, we observed links of productivity and performance with ERP implementation in the oil and gas industry, in which pre-ERP performance serves as a benchmark for the revenuesharing agreement associated with post-ERP implementation. These structures can be captured using a fixed-fee plus performance-based variable incentive structure—to the extent that their objectives are to provide incentives to the vendor. These observations are consistent with incentives observed in practice pertaining to IT service consulting and development $( \mathrm { e . g . }$ James 1998) or in research pertaining to after-sales service support (Cohen et al. 2006).

In this paper, we focus on the firm’s optimal contract choice regarding the two key structural dimensions—payment structure and sizing—in the presence of agent learning. As a benchmark, we also compute the optimal sizing and value of an insourced project (where efforts are observable and there are no moral hazard issues), and compare and contrast the insourced case with the outsourced case.

Together, these arguments naturally suggest considering enterprise software contracting in a multiperiod setting, such that the outcome (success or failure) in the first period can influence continuation to a second period $( \mathrm { e . g . }$ , Pike 2006). We formally present a model that integrates various isolated elements of the three streams of research to capture the aforementioned salient features of EIT implementation. Finally, we study the properties of the EIT project value function, and test model assumptions and key predictions experimentally.

## 3. Model

We assume that a risk-neutral principal contracts with a risk-neutral or a risk-averse agent for an enterprise IT project that generates a revenue of Q. The principal can divide the project into two sequential periods, with the outcome of each period randomly determined but observable at the end of each period. The outcome is assumed to take binary values of 1 (success) or 0 (failure). The contract specifies that continuation of the project to the second period project is conditional on success in the first period. The agent is assumed to be committed to complete the project if desired by the principal, consistent with observed contracting practice. The key notation for our model appears as follows.

Q Total revenue created by the EIT project

$s _ { i }$ Size of the EIT project in period i

$$
(s _ {1} = \alpha , s _ {2} = 1 - \alpha)
$$

$R _ { i } \equiv s _ { i } Q$ Revenue of period $i ( i = 1 , 2 )$

$a _ { i } + b _ { i } R _ { i }$ Two-part wage where $a _ { i }$ is the fixed fee, $b _ { i } R _ { i }$ is revenue sharing $( i = 1 , 2 )$

u4x5 Agent’s utility of profit

 Risk tolerance of the agent

r Interest rate

 Discrete case second period fixed discount factor. In the continuous case, $\lambda _ { 1 } =$ $e ^ { - r s _ { 1 } } , \lambda = \lambda _ { 2 } = e ^ { - r s _ { 2 } }$ 1 where r is the interest rate

$\bar { P } _ { i }$ General IT implementation capability in period $i ( i = 1 , { \bar { 2 } } )$

$( 1 - \bar { P } _ { i } )$ Inherent IT project risk in

period i 4i = 11 25

$p _ { i }$ Production function in period i

$$
(p _ {i} = \bar {P} _ {i} (1 - e ^ {- \beta_ {i} (x _ {i} / s _ {i})}), i = 1, 2)
$$

$\beta _ { i }$ Average skill (or expertise) in period i $( i = 1 , { \bar { 2 } } )$

$x _ { i }$ Effort in period $i \quad ( x _ { i } ~ = ~ - ( s _ { i } / \beta _ { i } ) \quad .$ $\ln ( 1 - p _ { i } / \bar { P } _ { i } ) , \stackrel { - } { \scriptscriptstyle { i = 1 , 2 } } )$

$$
\Delta_ {i} \Delta_ {i} \equiv \bar {P} _ {i} Q - 1 / \beta_ {i} - \ln (\beta_ {i} \bar {P} _ {i} Q) / \beta_ {i} (i = 1, 2)
$$

$\pi _ { i } ^ { 0 }$ Period i reservation profit (normalized to 0)

$\pi ^ { 0 }$ Reservation profit over the two-period horizon (normalized to 0)

$\Pi _ { i }$ Principal’s expected profit from period i

V Total EIT project value captured by the principal.

We further assume period $\textit { i } \left( i = 1 , 2 \right)$ subproject generates revenue of $\bar { R _ { i } } \bar { = } s _ { i } Q$ if successful, where $s _ { i }$ is the size (scope, duration or time) of the subproject in that period, otherwise $R _ { i } = 0 .$ . We normalize the overall project size to 1 $( \mathrm { i . e . , ~ } s _ { 1 } + s _ { 2 } \equiv 1 )$ so we need only one variable $s _ { 1 } \equiv \alpha$ to capture sizing of the full project (because $s _ { 2 } = 1 - \alpha )$ . The case when $\alpha = 1$ illustrates that the principal contracts the full project to the agent in a single stage. We denote $\underline { { \boldsymbol { \alpha } } }$ the smallest feasible project size (e.g., the core module) so that $0 < \underline { { \alpha } } \le \alpha \le 1$ . In practice,  represents the principal’s choice of project staging, including a full project or any subset of sequentially interlinked incremental phases, such as planning and design, construction and implementation, maintenance, support, and ongoing services related to the project $( \mathrm { e . g . }$ , Markus et al. 2000, McAfee 2003). We assume stage 1 must include the core development, but concurrently other components may also be developed.<sup>3</sup> In a software-as-a-service context (Chou 2010), stage length represents the time between contract renewals. For simplicity, we assume a continuous .

The principal’s pure strategy is to specify a wage function in a long-term contract $[ a _ { i } , \bar { b } _ { i } ; s _ { i } ] , i = 1 , \bar { 2 } ,$ which takes the linear form of $a _ { i } + b _ { i } R _ { i }$ . Here $a _ { i }$ is a fixed fee, $b _ { i } > 0$ is a revenue sharing factor contingent on outcome success, otherwise $b _ { i } = 0$ . The agent’s pure strategy is the mapping from the wage function to the agent’s action or effort $x _ { i } .$ . For tractability as well as consistency with observed contracting practice (see §2.3), we restrict our attention to two-part linear contracts rather than abstract reward functions in the extant literature (e.g., Lambert 1983, Rogerson 1985). Our two-part linear contracts, however, are quite general. For instance, parameter choices can yield a “big bang” $' \left( s _ { 1 } = \alpha = 1 \right)$ or multistage $( s _ { 1 } < 1 )$ project structure, fixed fee $( b _ { i } = 0 , i = 1 , 2 )$ contracts or incentive $( b _ { i } > 0 , i = 1 , 2 )$ contracts, with or without upfront vendor investments $( a _ { i } \geq 0 , i = 1 , 2 )$ , contracts in which a vendor posts bonds or makes fixed coinvestments in project preparations $( a _ { i } \leq 0 , i = 1 , 2 )$ and various combinations of these characteristics.

We extend existing moral hazard models by incorporating learning. The existence of effort-dependent learning is perhaps the most important, and the primary assumption that distinguishes our analysis from other principal-agent analyses. Following Levy (1965) and Gaimon (1997), we initially adopt an exponential learning function that relates outcome in each stage $( { p } _ { i } )$ with inherent project risk $( 1 - \bar { P } _ { i } )$ , skill $\beta _ { i }$ and project stage size $s _ { i } .$

Assumption A0 (Dynamic Production Function). $p _ { 1 } ( x _ { 1 } , s _ { 1 } , \bar { P } _ { 1 } , \beta _ { 1 } ) \ = \ \bar { P } _ { 1 } ( 1 - e ^ { - \beta _ { 1 } ( x _ { 1 } / s _ { 1 } ) } )$ , and $p _ { 2 } ( x _ { 2 } , s _ { 2 } , \bar { P } _ { 2 } , \beta _ { 2 } \mid p e r i o d \ 1 \ s u c c e e d s ) = \bar { P } _ { 2 } ( 1 - e ^ { - \beta _ { 2 } ( x _ { 2 } / s _ { 2 } ) } )$

Essentially, our dynamic production function captures two types of risks: inherent project risks $( 1 - \bar { P } _ { i } )$ , which represent technical, business, or managerial challenges that are part of the project $( \mathrm { e . g . } ,$ O’Leary 2002), and controllable risks $e ^ { - \hat { \beta _ { i } } ( x _ { i } / { s _ { i } } ) } .$ , which are influenced by agent effort $x _ { i } ,$ expertise $\beta _ { i } ,$ and project size $s _ { i } .$ For a given project size at each period, because inherent project risks and controllable risks are statistically independent, outcome success of the EIT project depends on the successful removal of both risks, leading to the multiplicative form of $p _ { i }$ we are using.

The information structure of the game is as follows. We assume the agent’s expertise levels $\beta _ { i }$ are common knowledge. Because both project value and agent expertise are known to the client, the potential adverse selection issues (Snir and Hitt 2004, Whang 1992) have presumably been resolved, and our model focuses purely on moral hazard (e.g., Holmstrom and Milgrom 1987).<sup>41</sup> <sup>5</sup> At the end of each period, the binary outcomes are observable and contractible; in essence, the outcome is whether the principal accepts or rejects the agent’s delivery. However, the agent’s efforts are not observable and cannot be “reverse engineered” from observable data because of the random component of the outcome. Conditional on a successful first-period, some inherent project risks can be reduced such that $1 - \bar { P } _ { 2 } \leq 1 - \bar { P } _ { 1 } ,$ perhaps through business process redesign. Consequently, both the principal and the vendor share a common updated belief such that $\bar { P } _ { 2 } \geq \bar { P } _ { 1 }$ . We discuss the case when updating is affected by project size  in a model extension, but we initially treat these capability factors as constants. The possibility of learning between the two periods derives from learning-by-doing or deliberate investments in team skill and project-specific risk management capabilities (e.g., post-project audit, staff training, or staff reallocation). Learning changes the relationship between effort and project outcomes, and the updated skill level is common knowledge.

The nature of the contracts and the structure of the industry make it unlikely that the contract will be subject to renegotiation after the first stage. We assume that the agent is bound to complete the project if desired by the principal (a practice we have observed) and derive the optimal contract under agent individual rationality in both periods. Provided that project learning is project specific, the vendor’s outside options do not change as the project progresses and thus the vendor cannot credibly threaten to terminate a successful contract even if it was contractually permissible. In optimum, the principal may desire to continue a failed project as the principal knows this was due to uncontrollable risks and not agent under performance, but is unable to do so because a failed first stage in most IT implementations prevents progressing to later stages. For instance, if the core module of an ERP installation is not operational, supplemental models cannot be installed. This is a different structure than many prior repeated agency models which has the agent performing similar tasks in each stage and where principal commitment is often enforced with auxiliary assumptions such as reputational concerns.<sup>6</sup>

Figure 1 Decision Tree  
![](/api/attachments/QK3DACZ5/fulltext/images/06332555f31826f4e3b8d85271e3d22094e58470f95bc34202e301f01d438b5d.jpg)

We employ a sub-game perfect equilibrium (SPE) solution concept (e.g., Bolton and Dewatripont 2005, p. 421; Chiappori et al. 1994; Lambert 1983). Figure 1 depicts the decision tree of the principal and the agent.

## 4. Impact of Contract Structure

We assume the agent is risk-neutral. Later on we extend the model to the case when the agent is riskaverse. When both the principal and the agent are risk-neutral, the linear contract form has a useful property that it is optimal among all possible contract forms (e.g., Holmstrom and Milgrom 1987).

We first consider the case (see §4.1) when the principal wishes to structure the EIT project as a single-stage “big bang” contract. We then consider the two-stage case (see §4.2).

## 4.1. Optimal Single-Stage Contract

For simplicity, we first assume no discounting for the single-stage case such that $\lambda = 1$ . Later we extend to the case when there is a discount. The

principal’s problem is:

$$
\begin{array}{r l} & {\underset {a _ {1}, b _ {1}} {\max} \big \{V (a _ {1}, b _ {1}; s _ {1} = 1)} \\ & {\qquad = \Pi_ {1} = [ p _ {1} (R _ {1} - a _ {1} - b _ {1} R _ {1}) + (1 - p _ {1}) (- a _ {1}) ] \big \},} \end{array}
$$

subject to

$$
\pi (x _ {1} ^ {*}) = p _ {1} (a _ {1} + b _ {1} R _ {1} - x _ {1} ^ {*}) + (1 - p _ {1}) (a _ {1} - x _ {1} ^ {*}) \geq \pi^ {0}, \tag {AgentIR}
$$

$$
\begin{array}{l} \text {(ii)} x _ {1} ^ {*} \text {solves} \max _ {x _ {1}} \{p _ {1} (a _ {1} + b _ {1} R _ {1} - x _ {1}) + (1 - p _ {1}) \cdot \\ (a _ {1} - x _ {1}) \}. \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \text {(Agent IC)} \end{array}
$$

The first constraint (i) requires that the agent’s expected payoff must exceed the agent’s reservation profit $\pi ^ { 0 }$ to satisfy the agent’s individual rationality requirement. The second constraint (ii) satisfies the agent’s incentive compatibility requirement.

Solving the principal’s problem, we obtain the following Lemma 1. For convenience of exposition, we define $\bar { P } _ { i } Q - 1 / \beta _ { i } - \ln ( \beta _ { i } \bar { P } _ { i } Q ) / \beta _ { i } \equiv \Delta _ { i }$

<sup>Lemma</sup> <sup>1.</sup> Assume agent is risk-neutral. Optimal single-stage contract $( a _ { 1 } ^ { * } , b _ { 1 } ^ { * } )$ , agent effort 4x<sup>∗</sup>5 and optimal IT project value 4V <sup>∗</sup>5 are given as follows:

$$
\begin{array}{c} {a _ {1} ^ {*} = - \bigg [ \bar {P} _ {1} Q - \frac {1}{\beta_ {1}} - \frac {\ln (\beta_ {1} \bar {P} _ {1} Q)}{\beta_ {1}} \bigg ] + \pi^ {0} = - \Delta_ {1} + \pi^ {0},} \\ {b _ {1} ^ {*} = 1,} \\ {x _ {1} ^ {*} = \frac {\ln (\beta_ {1} \bar {P} _ {1} Q)}{\beta_ {1}},} \\ {V ^ {*} = - a _ {1} ^ {*} = \bigg [ \bar {P} _ {1} Q - \frac {1}{\beta_ {1}} - \frac {\ln (\beta_ {1} \bar {P} _ {1} Q)}{\beta_ {1}} \bigg ] - \pi^ {0} = \Delta_ {1} - \pi^ {0}.} \end{array}
$$

It is straightforward to verify that the above optimal solution is efficient, as it is identical to the solution when the agent effort is observable (therefore removing moral hazard) or if the principal can do the project alone (assuming they have the expertise).

## 4.2. Optimal Two-Stage Contract

We now consider the principal’s two-stage contracting problem. We solve the model in two steps. First, given any project sizing $\alpha ,$ with $0 < \underline { { \alpha } } \le \alpha = s _ { 1 } \le 1$ (thus $s _ { 2 } = 1 - \alpha )$ 1 we solve for the optimal fee structures $( a _ { i } ^ { * } , b _ { i } ^ { * } )$ at each period i taking into account how different incentive payments affect agent effort and participation. Second, we solve for the optimal sizing $\bar { \alpha } ^ { * } = s _ { 1 } ^ { * } \left( \mathrm { w i t h \ } s _ { 2 } ^ { * } = 1 - \alpha ^ { * } \right)$

To obtain optimal fee structures $( a _ { i } ^ { * } , b _ { i } ^ { * } )$ , we use backward induction (i.e., dynamic programming). At the beginning of period 2, the principal updates the contract $( a _ { 2 } , b _ { 2 } )$ after observing the agent’s firstperiod performance:

$$
\max _ {a _ {2}, b _ {2}} \Pi_ {2} = p _ {2} [ R _ {2} - (a _ {2} + b _ {2} R _ {2}) ] + (1 - p _ {2}) (- a _ {2}),
$$

subject to

$$
\pi_ {2} (x _ {2} ^ {*}) = p _ {2} (a _ {2} + b _ {2} R _ {2} - x _ {2} ^ {*}) + (1 - p _ {2}) (a _ {2} - x _ {2} ^ {*}) \geq \pi_ {2} ^ {0},\tag{Agent IR}
$$

$$
\begin{array}{l} \text {(ii)} x _ {2} ^ {*} \text {solves} \max _ {x _ {2}} \{\pi_ {2} (x _ {2}) = [ p _ {2} (a _ {2} + b _ {2} R _ {2} - x _ {2}) + \\ (1 - p _ {2}) (a _ {2} - x _ {2}) ] \}. \end{array} \tag {AgentIC}
$$

The objective function is the principal’s expected profit in the second period, given the updated information of $\bar { P } _ { 2 } \geq \bar { P } _ { 1 }$ and the agent’s updated expertise $\beta _ { 2 } \geq \beta _ { 1 }$ , so that

$$
p _ {2} (x _ {2}, s _ {2}, \bar {P} _ {2}, \beta_ {2} \mid \text { period   1   succeeds }) = \bar {P} _ {2} (1 - e ^ {- \beta_ {2} (x _ {2} / s _ {2})}).
$$

Solving, the principal’s optimal second period strategy $( a _ { 2 } ^ { * } , b _ { 2 } ^ { * } )$ , and the agent’s optimal effort (x<sup>∗</sup>5 are:

$$
a _ {2} ^ {*} = - s _ {2} \left[ \bar {P} _ {2} Q - \frac {1}{\beta_ {2}} - \frac {\ln (\beta_ {2} \bar {P} _ {2} Q)}{\beta_ {2}} \right] + \pi_ {2} ^ {0},\tag{1}
$$

$$
b _ {2} ^ {*} = 1,\tag{2}
$$

$$
x _ {2} ^ {*} = s _ {2} \frac {\ln (\beta_ {2} \bar {P} _ {2} Q)}{\beta_ {2}}.\tag{3}
$$

Similarly, the principal’s problem at time $0 ~ ( \mathrm { i . e . } ,$ , the beginning of period 1) is:

$$
\begin{array}{l} \max _ {a _ {1}, b _ {1}} V (a _ {1}, b _ {1}; s _ {1}, s _ {2}, a _ {2} ^ {*}, b _ {2} ^ {*}) \\ \qquad = \Pi_ {1} + p _ {1} \lambda \Pi_ {2} ^ {*} \\ \qquad = [ p _ {1} (R _ {1} - a _ {1} - b _ {1} R _ {1}) + (1 - p _ {1}) (- a _ {1}) ] + p _ {1} \lambda \Pi_ {2} ^ {*}, \end{array}
$$

subject to

$$
\begin{array}{l} \text {(i)} \pi (x _ {1} ^ {*}) = p _ {1} (a _ {1} + b _ {1} R _ {1} - x _ {1} ^ {*}) + (1 - p _ {1}) (a _ {1} - x _ {1} ^ {*}) + \\ p _ {1} \lambda \pi_ {2} ^ {*} \geq \pi^ {0}, \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \text {(Agent IR)} \end{array}
$$

(ii) $x _ { 1 } ^ { * }$ solves ma ${ \ x } _ { x _ { 1 } } \{ p _ { 1 } ( a _ { 1 } + b _ { 1 } R _ { 1 } - x _ { 1 } ) + ( 1 - p _ { 1 } )$

$$
\left. \left(a _ {1} - x _ {1}\right) + p _ {1} \lambda \pi_ {2} ^ {*} \right\}.\tag{Agent IC}
$$

Solving, the principal’s first period optimal strategy $( a _ { 1 } ^ { * } , b _ { 1 } ^ { * } )$ , and the agent’s optimal effort in response $( x _ { 1 } ^ { * } )$ are:

$$
a _ {1} ^ {*} = - (s _ {1} \Delta_ {1} + \bar {P} _ {1} \lambda s _ {2} \Delta_ {2}) + \frac {s _ {1}}{\beta_ {1}} \ln \left(1 + \frac {\lambda s _ {2} \Delta_ {2}}{s _ {1} Q}\right) + \pi^ {0},\tag{4}
$$

$$
b _ {1} ^ {*} = 1 + \frac {\lambda (s _ {2} \Delta_ {2} - \pi_ {2} ^ {0})}{s _ {1} Q},\tag{5}
$$

$$
x _ {1} ^ {*} = \frac {s _ {1}}{\beta_ {1}} \ln \frac {\beta_ {1} \bar {P} _ {1} (s _ {1} Q + \lambda s _ {2} \Delta_ {2})}{s _ {1}}.\tag{6}
$$

Consequently, the principal’s total IT project value (or IT value function) is

$$
\begin{array}{l} V ^ {*} = \Pi_ {1} ^ {*} + p _ {1} \lambda \Pi_ {2} ^ {*} = - a _ {1} ^ {*} \\ = (s _ {1} \Delta_ {1} + \bar {P} _ {1} \lambda s _ {2} \Delta_ {2}) - \frac {s _ {1}}{\beta_ {1}} \ln \left(1 + \frac {\lambda s _ {2} \Delta_ {2}}{s _ {1} Q}\right) - \pi^ {0}. \end{array}\tag{7}
$$

The IT value function as given in Equation (7) highlights the central trade-off in sizing (i.e., determining optimal $s _ { i } ^ { * } )$ in a two-stage project—building higher expertise $( \beta _ { 2 } \geq \beta _ { 1 } )$ and increasing implementation capability $( \bar { P } _ { 2 } \geq \bar { P } _ { 1 } )$ for the second stage (via learning in the first stage), versus investing additional effort (third term in Equation (7)) to increase the chance of continuation to the second stage of the project. There is also a trade-off in timing; while a larger first-stage project size increases second-stage expertise and capability, it shrinks time left $( s _ { 2 } ^ { * } = \stackrel { \smile } { 1 } - s _ { 1 } ^ { * } )$ to harvest such benefits $( \Delta _ { 2 } \geq \Delta _ { 1 } , \mathrm { o r } ~ \Delta _ { i }$ is increasing in both $\beta _ { i }$ and $\bar { P _ { i } } )$ We shall formally characterize the properties of the IT value function later via Theorem 1 and its proof.

The optimal two-stage contract as defined in Equations (1), (2), (4), (5) is equivalent to the principal selling the project to the agent at each period. The agent nets exactly its reservation profit because both IR and IC constraints are binding (this property is later exploited in our lab experiments). Note that $\Delta _ { i } \ ( i = 1 , 2 )$ can be interpreted as a kind of “unit price.”<sup>7</sup> Specifically, $\Delta _ { 2 }$ is a second-stage “unit price” since the agent pays $s _ { 2 } \Delta _ { 2 } - \pi _ { 2 } ^ { 0 }$ . Similarly, $\Delta _ { 1 }$ can be interpreted as a first-stage “unit price.”

Further, we show in Proposition 1 that the above optimal contract is viable (Whang 1992). A contract is said to be viable if it satisfies the following four properties (Whang 1992): (1) Efficiency: It induces the same equilibrium decisions as the optimal in-house implementation at each period; (2) Pareto Optimality: The combined equilibrium payoff to the contracting parties is the same as in in-house implementation; (3) Incentive Compatibility: The principal reports the true value of the system, which induces the agent to exert an effort that maximizes its own profit; and (4) Ex-ante Incentive Rationality: Both contracting parties have non-negative expected payoffs at the time of contracting, so they voluntarily sign the contract.

<sup>Proposition</sup> <sup>1.</sup> Assume agent is risk-neutral. Given any sizing of an IT project $s _ { i } ( i = 1 , 2 )$

(i) The linear contract form is optimal among all possible contract forms.

(ii) There exists a unique SPE for the principal’s problem.

(iii) The optimal contract $\left[ a _ { i } ^ { \ast } , b _ { i } ^ { \ast } ; s _ { i } \right] ( i = 1 , 2 )$ , as specified in Equations (1), (2), (4), (5), is viable.

Proposition 1 contributes to the literature by establishing the structure of the optimal contract capturing unique characteristics of EIT projects, and by extending multiperiod agency models to a setting where there is agent learning across project periods. Proposition 2, as follows, characterizes the comparative statics of the optimal contract.

<sup>Proposition</sup> <sup>2.</sup> The IT value V increases monotonically in $\bar { P } _ { i } , \beta _ { i } ( i = 1 , 2 ) , Q ,$ and .

Proposition 2 suggests that the effects of exogenous project parameters $Q$ and  are in the expected direction. Note that Q and  are independent of $\bar { P } _ { i }$ or $\beta _ { i }$ Consequently, the monotonicity of project value in general IT implementation capabilities (P<sup>¯</sup> 5 or vendor expertise $( \beta _ { i } )$ does not depend on exogenous project parameters Q and . Therefore, we may characterize different learning conditions without being concerned that the model will yield implausible results for some values of the exogenous project parameters.

We now compare a multistage with a single-stage “big bang” contract. If we consider discounting, the optimal IT value for a single-stage (shown in §4.1) is: V <sup>∗</sup>4single-stage contr $\mathsf { a c t } ) \stackrel { \smile } { = } V ^ { * } ( \bar { 1 } ) = \lambda \Delta _ { 1 } - \pi ^ { 0 }$ . Therefore, the difference of optimal project value between a two-stage contract and a single-stage contract is:

V <sup>∗</sup>4two-stage contract5 − V <sup>∗</sup>4single-stage contract5

$$
= \lambda s _ {2} (\bar {P} _ {1} \Delta_ {2} - \Delta_ {1}) + (1 - \lambda) s _ {1} \Delta_ {1} - \frac {s _ {1}}{\beta_ {1}} \ln \left(1 + \frac {\lambda s _ {2} \Delta_ {2}}{s _ {1} Q}\right).\tag{8}
$$

From (8) we see that the additional learning benefit due to staging is $( \lambda s _ { 2 } ( \bar { P } _ { 1 } \Delta _ { 2 } - \Delta _ { 1 } ) + ( 1 - \lambda ) s _ { 1 } \Delta _ { 1 } )$ , at the additional cost/effort of $( s _ { 1 } / \beta _ { 1 } ) \ln ( 1 + \lambda s _ { 2 } \Delta _ { 2 } / ( s _ { 1 } Q ) )$ We summarize this finding in Proposition 3:

<sup>Proposition</sup> <sup>3.</sup> A two-stage contract is preferable to a single-stage contract if, and only if, the benefit of staging outweighs the cost of staging, i.e., if there exists $\hat { \alpha } , 0 < \underline { { \alpha } } \le$ $\hat { \alpha } < 1$ 1 such that $( 8 ) > 0$ or equivalently, $V ^ { * } ( \hat { \alpha } ) > V ^ { * } ( 1 )$

We illustrate the insights in Proposition 3 with two simple examples.

Example 1. <sub>Assume</sub> $Q = 2 .$ . If there is: no learning $( \beta _ { 2 } = \beta _ { 1 } = 1 )$ , no capability improving $( \bar { P } _ { 2 } = \bar { P } _ { 1 } = 1 )$

and no discounting $( \lambda = 1 )$ , then $( 8 ) = - ( s _ { 1 } / \beta _ { 1 } ) \ln ( 1 +$ $\lambda s _ { 2 } \Delta _ { 2 } / ( s _ { 1 } Q ) ) < 0 . \mathrm { ~ \AA ~ }$ single-stage contract is preferable to a two-stage contract, because in this case staging incurs additional cost but gains nothing.

<sup>Example</sup> <sup>2.</sup> Retain other assumptions of Example 1 but allow for some agent learning due to staging such that $\beta _ { 2 } > e \approx 2 . 7 1 \bar { 8 } > 1 = \beta _ { 1 }$ . We have $\Delta _ { 2 } - \Delta _ { 1 } =$ $( e - 2 - \ln 2 ) / e + \ln 2 > \ln 2$ . If we set $s _ { 1 } = 1 / 2 ,$ , we have $( 8 ) = 0 . 5 ( \Delta _ { 2 } - \Delta _ { 1 } ) - 0 . 5 \ln [ 1 + \Delta _ { 2 } / Q ] > 0 . 5 \ln { 2 } -$ $0 . 5 \ln [ 1 + \Delta _ { 2 } / Q ] > 0 \quad$ . A two-stage contract is preferable to a single-stage contract, because the additional benefit due to staging offsets the additional cost of staging.

Generally speaking, a two-stage contract is preferable to a one-stage contract if there is sufficient learning benefit following a successful period 1 outcome such that $\bar { P } _ { 1 } \Delta _ { 2 } > \Delta _ { 1 }$ (which can be satisfied if $\beta _ { 2 }$ is sufficiently larger than $\beta _ { 1 }$ and ${ \bar { P } } _ { 2 }$ is sufficiently larger than $\bar { P } _ { 1 } )$

The above examples and discussion highlight the importance of learning and capability in two-stage contract design. We are interested in when a unique interior solution to the optimal staging problem exists. We begin with the most straightforward learning process, in which expertise increases with the length of the first stage. This yields the following assumption:

Assumption A1 (Concave Learning). <sub>Assume</sub> $\beta _ { 1 }$ is fixed, $\beta _ { 2 } ( \alpha )$ is increasing and concave over .

Assumption $\mathbf { A } 1 ,$ especially the concavity requirement, plausibly describes discovery learning processes in which firms learn additional details as a project progresses until they know essentially everything and can learn little more. Nearly all learning functions in the literature satisfy this condition (e.g., Lilien et al. 1992). We obtain the following general properties of learning and project sizing under optimal contracting:

<sup>Theorem</sup> <sup>1.</sup> Assume A1. Assume both project revenue Q and initial expertise $\beta _ { 1 }$ are sufficiently large so that the project is feasible. Let $\hat { \alpha } \geq \underline { { \alpha } }$ be the smallest project size that satisfies $V ^ { * } ( \hat { \alpha } ) > V ^ { * } ( 1 )$ , then a unique optimal sizing exists $( \hat { \alpha } \leq \alpha ^ { * } < 1 )$ ; otherwise a single-stage contract $( \bar { \alpha ^ { * } } = 1 )$ is optimal.

When the project revenue Q and initial expertise $\beta _ { 1 }$ are sufficiently large, Theorem 1 shows that the optimal sizing of a project depends on vendor learning and capability increase. The IT payoff function is well behaved, in fact concave (“Inverted-U”) over project size (see the proof of Theorem 1), so any hill climbing method will reach the optimal interior point. An approximation of the optimal sizing is given implicitly by $\alpha ^ { * } \approx 1 - [ ( \bar { P } _ { 1 } \lambda \Delta _ { 2 } \dot { - } \Delta _ { 1 } ) / ( \bar { P } _ { 1 } \lambda ) ] ( \partial \Delta _ { 2 } \check { / } \partial \alpha ) ^ { - 1 }$

To further explore the role of learning, it is useful to explicitly provide a learning function so that we can characterize how the rate of learning affects project sizing. Consider a general class of functions that takes the form of $\bar { \beta _ { 2 } ( \alpha ) } = \beta _ { 1 } + ( \bar { \beta } _ { 2 } - \beta _ { 1 } ) \alpha ^ { 1 / n }$ where n is interpreted as the rate of learning. This functional form accommodates both linear and power law relationships that have been discussed in the prior literature, and this functional form anticipates a function where additional project-specific experience enables an agent to become more capable, up to some upper limit $( \bar { \beta } _ { 2 }$ is a constant that bounds $\beta _ { 2 } )$ When $n \geq 1$ 1 this functional form yields a concave relationship between experience and expertise, consistent with Assumption A1. Further, when $0 < n < 1$ the form is also capable of capturing a convex relationship between experience and expertise. With this additional assumption we can show:

Corollary 1. <sub>Assume</sub> $\beta _ { 2 } ( \alpha ) = \beta _ { 1 } + ( \bar { \beta } _ { 2 } - \beta _ { 1 } ) \alpha ^ { 1 / n }$ Then: the faster the rate of learning (larger n), (i) the larger the IT project value, $i . e . , \ \partial V ^ { * } / \partial n > 0 , \forall n > 0 ,$ , and (ii) the smaller the optimal first-period project size $\alpha ^ { * } , i . e . ,$ $d \alpha ^ { * } / d n < 0 , \forall n \ge 1$

As illustrated in Figure 2, Corollary 1 provides the intuitive result that a faster learning rate always allows the client to capture more project value. Moreover, if a project is to be staged, faster learning leads to a smaller first stage. If we assume no discounting, the shape of the project value function depends on the speed of learning. Learning can change its shape from convex to concave. If we assume a moderate level of discounting, as we show later in Corollary 5, the concavity of the IT value function holds beyond Assumption A1 to include some cases of convex learning.

## 5. Extensions

Overall, Theorem 1 shows that as long as it is feasible to do a project, the optimal sizing depends on the learning rate, and that a faster learning rate yields higher project value yet a smaller first-stage size; a single-stage “big bang” project can be optimal under certain conditions (such as if there is no learning). In this section, we demonstrate that these general properties are quite robust to much broader assumptions than could reasonably arise in EIT projects.

Figure 2 Risk-Neutral Agent: Project Value, Learning and Optimal Staging  
![](/api/attachments/QK3DACZ5/fulltext/images/61554476c8806b3191fab752c9d5a6f6f0be7b05a6b12111963875f88e6bfe30.jpg)  
Note. $Q = 5 0 , \bar { P } _ { 1 } = \bar { P } _ { 2 } = 1 , r = 0 , \pi _ { i } ^ { 0 } = 0 ( i = 1 , 2 ) , \beta _ { 2 } = \beta _ { 1 } + ( \bar { \beta } _ { 2 } - \beta _ { 1 } ) \alpha ^ { 1 / n } ,$ $\beta _ { 1 } = 1 . 5 , \bar { \beta } _ { 2 } = 3 , \underline { { \alpha } } = 0 . 0 1 .$

## 5.1. Generalized Concave Learning

Several other plausible assumptions apply to the relationships among project sizing and learning. One possibility is that learning occurs both during the first and the second period $\beta _ { i } ( \alpha ) ~ ( i = 1 , 2 ) , ~ \mathrm { i . e . } , ~ \beta _ { 1 }$ is no longer fixed but is also a function of $\alpha ;$ the conclusions of our preceding analyses generalize:

<sup>Corollary</sup> <sup>2.</sup> Suppose the assumptions used in Theorem 1 hold and a multistage contract is optimal. A multistage contract remains optimal if learning occurs both during the first and the second period, $i . e . ,$ when $\beta _ { i } ( \alpha ) \ ( i = 1 , 2 )$ are increasing and concave over .

## 5.2. Time-Varying Inherent Project Risk and Risk Reduction

In the first period, the inherent project risk may depend on the project size, such that a larger project may be more risky, and a “big bang” project has the highest inherent project risk $( 1 - \bar { P } _ { 1 } ( \alpha = 1 ) )$ . It is equally plausible, after the successful completion of the first-period project, that the inherent project risk changes $( \mathrm { i . e . } ,$ , decreases). These two generalizations can be summarized as follows.

Assumption $_ { \mathrm { A } 2 }$ (Learning in Reducing Inherent Project Risks). $\bar { P } _ { 1 } ( \alpha )$ is decreasing and linear over $\alpha ,$ and $\bar { P } _ { 2 } ( \alpha )$ is increasing and concave over .

This assumption is consistent with a view that a two-stage project can provide a Bayesian update of the risk of the overall project; the information updating of the second-period inherent risk $( 1 - \bar { P } _ { 2 } ( \hat { \alpha } ) )$ is conditional on first-period project success. Although our more general Assumption A2 is consistent with Bayesian updating, our interpretation hinges on the nature of the EIT project, in the sense that a successful first-period project removes some risks from the later stages, rather than that firms learn about a purely exogenous project risk.

<sup>Corollary</sup> <sup>3.</sup> Suppose the assumptions used in Theorem 1 hold and a multistage contract is optimal. A multistage contract remains optimal if there is learning that reduces inherent project risks (as described by A2).

## 5.3. Learning Through Training

It is natural to believe that agents can acquire increased ability not only through project-specific experience, but also through project-specific training, which (in general) may be a function of project structure since the training can occur during the first period. Let the training cost be represented by $t _ { 1 } ( \alpha )$ This gives rise to a more general concept of learning when $\beta _ { 2 } ( \alpha , t _ { 1 } ( \alpha ) )$ is a function of training. This cost could also be viewed as an investment by the agent in project-specific coordination. This can be formalized as follows:

Assumption A3 (Learning through Training). $t _ { 1 } ( \alpha )$ is increasing and linear over time. Furthermore, $\beta _ { 2 } ( \alpha , t _ { 1 } ( \alpha ) )$ is increasing and concave in training $t _ { 1 } ( \alpha )$

Intuitively, Theorem 1 holds under A3 because the introduction of an investment in training $t _ { 1 } ( \alpha )$ does not change the structure of our IT contract game, and the optimal contract design remains the same—except that we substitute agent reservation profit $\pi _ { 1 } ^ { 0 }$ with $\pi _ { 1 } ^ { 0 } - t _ { 1 } ( \alpha )$

<sup>Corollary</sup> <sup>4.</sup> Suppose the assumptions used in Theorem 1 hold and a multistage contract is optimal. A multistage contract remains optimal if there is learning through training (as described by A3).

Collectively, these results suggest that the general structure of the results described by Theorem 1 is robust. Now we consider the impact of a continuous discounting rate.

## 5.4. Continuous Discounting

Assumption A4 (Continuous Discounting Rate). Assume further the interest rate $0 < r < 2$ is the same for both the principal and the agent so that the discount factor at each period i is $e ^ { - r s _ { i } } ~ ( i = 1 , 2 )$

<sup>Corollary</sup> <sup>5.</sup> Assume A4. Assume Q and $\beta _ { 1 }$ are sufficiently large for the project to be feasible. Then $\partial ^ { 2 } \tilde { V } / \partial \alpha ^ { 2 } < 0$

Corollary 5 demonstrates the expected impact of discounting. If the principal and the agent are moderately patient—the interest rate is positive but below a reasonable threshold such that $r < 2 \cdot$ —then the IT payoff function becomes concave. Discounting at a reasonable interest rate tends to preserve or strengthen the concavity of the IT payoff function, so we extend Corollaries 1–4 to the case of continuous discounting, which suggests additional robustness of the structure of the results described by Theorem 1.

## 5.5. Risk-Averse Agents

We now consider the possibility that the agent is risk averse. For tractability, we consider risk-neutral principals and agents that show constant absolute risk aversion (CARA). CARA is commonly used in principal–agent modeling when the agent is risk averse (e.g., Holmstrom and Milgrom 1987).

Assumption A5 (CARA Utility). <sub>The</sub> <sub>agent</sub> <sub>has</sub> <sub>a</sub> constant absolute risk aversion; that $i s , \ u ( x ) = - e ^ { - \gamma x } \ f o r$ some $\gamma \geq 0$

To focus on the impact of the agent’s risk tolerance (captured by 5, and without loss of generality, we let $\stackrel { . } { \bar { P } _ { 1 } } \stackrel { . } { = } \bar { P } _ { 2 } = 1 , \stackrel { . } { \pi _ { 1 } ^ { 0 } } = \pi _ { 2 } ^ { 0 } = \pi ^ { 0 } = 0 \nonumber$ . We denote $u ( b _ { 2 } \bar { R } _ { 2 } ) \equiv w ,$ $u ( b _ { 1 } R _ { 1 } + e ^ { - r s _ { 2 } } \pi _ { 2 } ^ { 0 } ) \equiv v ,$ , and $( s _ { i } / \beta _ { i } ) \gamma \equiv B _ { i }$ 1 for $i = 1 , 2$ We add a superscript A to our key parameters to denote risk attitude. By applying the certainty equivalent principle, we solve again the two-stage principal– agent problem. We summarize our findings in Theorem 2. In equilibrium, the optimal long-term contract $[ a _ { i } ^ { A } , b _ { i } ^ { A } ; s _ { i } ] \ \hat { ( i = 1 , 2 ) }$ and the agent’s reaction becomes

$$
a _ {1} ^ {A} = \frac {1}{\gamma} \ln \frac {1 + v}{B _ {1}} + \frac {1 - B _ {1}}{\gamma} \ln \left[ \frac {B _ {1}}{1 - B _ {1}} \frac {- v}{1 + v} \right] + \pi^ {0},\tag{9}
$$

$$
b _ {1} ^ {A} = 1 + e ^ {- r s _ {2}} \frac {\Pi_ {2} ^ {A}}{R _ {1}} + \frac {(1 + v) + (1 - B _ {1}) (1 + v ^ {- 1})}{\gamma R _ {1}}
$$

$$
<   1 + e ^ {- r s _ {2}} \frac {\Pi_ {2} ^ {A}}{R _ {1}},\tag{10}
$$

where $\Pi _ { 2 } ^ { A } = ( 1 - b _ { 2 } ^ { A } ) p _ { 2 } ^ { A } R _ { 2 } - a _ { 2 } ^ { A }$

$$
x _ {1} ^ {A} = \frac {s _ {1}}{\beta_ {1}} \ln \left[ \frac {1 - B _ {1}}{B _ {1}} \frac {1 + v}{- v} \right],
$$

$$
a _ {2} ^ {A} = \frac {1}{\gamma} \ln \frac {1 + w}{B _ {2}} + \frac {1 - B _ {2}}{\gamma} \ln \left[ \frac {B _ {2}}{1 - B _ {2}} \frac {- w}{1 + w} \right] + \pi_ {2} ^ {0},\tag{11}
$$

$$
b _ {2} ^ {A} = 1 + \frac {(1 + w) + (1 - B _ {2}) (1 + w ^ {- 1})}{\gamma R _ {2}} <   1,\tag{12}
$$

$$
x _ {2} ^ {A} = \frac {s _ {2}}{\beta_ {2}} \ln \biggl [ \frac {1 - B _ {2}}{B _ {2}} \frac {1 + w}{- w} \biggr ].
$$

The IT project value is

$$
V ^ {A} = e ^ {- r \alpha} \bigg (p _ {1} ^ {A} \frac {(1 + v - B _ {1}) (1 + v)}{- \gamma v} - a _ {1} ^ {A} \bigg).\tag{13}
$$

<sup>Theorem</sup> <sup>2.</sup> Assume A5. Let $\bar { P } _ { 1 } = \bar { P } _ { 2 } = 1$ . Given any sizing $o f$ an IT project $s _ { i } \ ( i = 1 , 2 )$ , when a feasible contract exists, then it is specified in Equations (9)–(12), with project value given by (13). Further, as the agent becomes more risk averse (but not extremely risk averse), the principal needs to reduce the revenue-sharing factor and increase the fixed payment part. Formally, $\partial b _ { i } ^ { A } / \partial \gamma < 0 , \partial a _ { i } ^ { A } / \partial \gamma > 0 , i = 1 , \stackrel { . } { 2 }$

Note that, when initial expertise $( \beta _ { 1 } )$ is sufficiently large or when the agent’s risk tolerance is not so large $( \gamma < \beta _ { 1 } < \beta _ { 2 } )$ then a feasible contract exists.

<sup>Corollary</sup> <sup>6.</sup> Assume A1 and A5. Let $\bar { P } _ { 1 } = \bar { P } _ { 2 } = 1$ Assume fixed discount factors. Assume both project revenue Q and initial expertise $\beta _ { 1 }$ are sufficiently large. Assume a feasible contract exists, then the IT value function $V ^ { A }$ is concave in . Formally, $\partial ^ { 2 } V ^ { A } / \partial \alpha ^ { 2 } < 0 .$

We now characterize conditions when the optimal sizing is an interior point, and vice versa.

Define ˆ as the smallest  that satisfies $V ^ { A } ( \hat { \alpha } ) \geq$ $V ^ { A } ( 1 )$ . Corollary 6 implies that if ˆ exists, then an interior optimal solution $\hat { \alpha } \leq \alpha ^ { * } < 1$ exists, meaning a two-stage contract is optimal; otherwise a single-stage “big bang” contract is optimal.

Figure 3 CARA Agent: Project Value, Learning and Optimal Staging  
![](/api/attachments/QK3DACZ5/fulltext/images/e842cd71e72365170bc9c948fe3fc6c5193c6d8aab1cb78c2d4a3c6eaa1efc06.jpg)  
Note. $\mathcal { Q } = 5 0 , \bar { P } _ { 1 } = \bar { P } _ { 2 } = 1 , \gamma = 0 . 5 , r = 0 . 1 , \pi _ { i } ^ { 0 } = 0 ( i = 1 , 2 ) , \beta _ { 2 } = \beta _ { 1 } +$ $( \bar { \beta } _ { 2 } - \beta _ { 1 } ) \alpha ^ { 1 / { n } } , \beta _ { 1 } = 1 . 5 , \bar { \beta } _ { 2 } = 3 , \underline { { \alpha } } = 0 . 0 1$

Finally, we show that our key findings—agent learning increases client IT payoff when the agent is risk neutral—continue to hold when the agent is risk averse.

<sup>Corollary</sup> <sup>7.</sup> Assume A1 and A5. Let $\bar { P } _ { 1 } = \bar { P } _ { 2 } = 1$ Assume a general learning function such that $\partial \beta _ { 2 } / \partial n > 0$ $\forall n > 0$ . Then $\partial V ^ { A } / \partial n > \bar { 0 }$

As illustrated in Figure 3, key findings in the riskneutral case are robust when the agent is CARA risk averse. Agent learning allows the client to capture more project value, and staging can be desirable even in the absence of learning, in contrast to the riskneutral case where an absence of learning implies that a single-stage contract is preferable. As the agent becomes more risk averse, the principal scales back the revenue sharing factor but increases the fixed fee payment. Conversely, when the agent becomes less risk averse, the principal increases the incentives and reduces the fixed fee payment. Consistent with the literature in contract theory (Chiappori et al. 1994), it is possible that the individual rationality constraint cannot be satisfied, so there is no equilibrium with agent participation and no opportunity for a feasible contract. As with much of the principal–agent literature, we do not consider risk-averse principals due to the additional complexity, although this scenario could potentially be studied using simulation.

## 6. Experimental Evidence

In this section, we focus on experiments related to the main predictions of our model in the context of EIT contracting. We are interested in testing whether staging the project has the expected benefits under different learning rates. We are also interested in testing if a faster learning rate encourages decision makers to select a smaller first-stage size.

In our experiments, subjects act as consultants (representing the agents) playing against a computer (which represents the client or the principal) in a twostage game in which the client contracts with the consultant for an IT project. A subject, presented with an effort-outcome mapping table (computed using our model), decides how much effort x to invest at each stage. After the investment, the binary outcome (success or failure) is realized and shown to the subject. We examine how experimental subjects perform relative to our theoretical predictions in Corollary 1.

We test three rates (slow, medium, fast) of agent learning. All treatments have the same expected profit and parameter set (except learning rate). Table 1 summarizes our experiments’ design.

The risk-neutral model offers optimal contract parameter settings, which are conservative estimates compared with those produced by the risk-averse model (from Theorem 2). We parameterize our learning function in Corollary 1, $\beta _ { 2 } \stackrel { \cdot } { = } \beta _ { 1 } + ( \bar { \beta } _ { 2 } - \beta _ { 1 } ) \alpha ^ { 1 / n }$ with $\bar { \beta } _ { 2 } = 1$ and three scenarios of learning: $n = 0 . 5$ for slow learning (Treatment $1 , T _ { 1 } ) , n = 0 . 9$ for medium learning (Treatments 2 and $3 , \ T _ { 2 }$ and $T _ { 3 } ) _ { \cdot }$ , and $n = 2 0$ for fast learning (Treatment 4, $T _ { 4 } )$ . We test how learning allows the client to receive higher value by staging the project. Specifically, our model predicts the following:

<sup>Hypothesis</sup> <sup>1</sup> <sup>(H1).</sup> Client project value increases (a) from $T _ { 1 }$ to $T _ { 3 } ,$ (b) from $T _ { 3 }$ to $T _ { 4 } ,$ , and (c) from $T _ { 1 }$ to $T _ { 4 } .$ .

To test whether faster learning reduces firstperiod project size, controlling for client profit, we added treatment $T _ { 2 }$ which has a smaller first-period size compared with $T _ { 1 }$ . We examine this prediction indirectly through the consultant effort level at Stage 1, which should decrease due to size reductions; hypothesized as follows:

<sup>Hypothesis</sup> <sup>2</sup> <sup>(H2).</sup> First-period consultant effort $x _ { 1 }$ decreases from $T _ { 1 }$ to $T _ { 2 }$ .

We conducted three series of experiments with different subjects for a total of eight sessions lasting 90 minutes each. In Experiment 1, our baseline experiment, we recruited 7 subjects each in Treatments 1–4 from a general student pool (undergraduate students randomly recruited on campus via campus advertisements) for two sessions.<sup>8</sup> We conducted two additional series of experiments for robustness in another location. Experiment 2 used 9, 10, 16, and 13 subjects, respectively, in Treatments 1–4. Subjects in Experiment 2 were graduate and undergraduate students who had completed half of a semester-long course on IT management and were familiar with topics such as ERP systems, implementation, and outsourcing. Finally, the single session in Experiment 3 involved 8 and 7 executives in Treatments 1 and 4, respectively; their average 17 years of industry experience makes Experiment 3 essentially a controlled field experiment (e.g., Harrison and List 2004).

Table 1 Treatments

<table><tr><td></td><td>Slow learning (n = 0.5)</td><td>Medium learning (n = 0.9)</td><td>Fast learning (n = 20)</td></tr><tr><td>Two-stage incentive payment (suboptimal)</td><td></td><td> $T_{2}$ </td><td></td></tr><tr><td>Two-stage incentive payment (optimal)</td><td> $T_{1}$ </td><td> $T_{3}$ </td><td> $T_{4}$ </td></tr></table>

Table 2 Parameterization for Real Run Experiments

<table><tr><td rowspan="2"></td><td colspan="4">External environment</td><td colspan="2">Stage 1 contract</td><td colspan="2">Stage 2 contract</td><td>Client profit</td></tr><tr><td> $\alpha$ </td><td> $\beta_1$ </td><td>n</td><td> $\beta_2$ </td><td> $a_1$ </td><td> $b_1$ </td><td> $a_2$ </td><td> $b_2$ </td><td>V</td></tr><tr><td> $T_1$ </td><td>0.3</td><td>0.1</td><td>0.5</td><td>0.181</td><td>-22.547</td><td>1.894</td><td>-26.812</td><td>1.000</td><td>22.547</td></tr><tr><td> $T_2$ </td><td>0.128</td><td>0.1</td><td>0.9</td><td>0.192</td><td>-22.547</td><td>3.822</td><td>-36.178</td><td>1.000</td><td>22.547</td></tr><tr><td> $T_3$ </td><td>0.3</td><td>0.1</td><td>0.9</td><td>0.336</td><td>-25.845</td><td>2.061</td><td>-31.842</td><td>1.000</td><td>25.845</td></tr><tr><td> $T_4$ </td><td>0.3</td><td>0.1</td><td>20.0</td><td>0.947</td><td>-29.020</td><td>2.222</td><td>-36.662</td><td>1.000</td><td>29.020</td></tr></table>

Notes. Across all treatments, Q = 100, $\bar { P } _ { 1 } = \bar { P } _ { 2 } = 0 . 7 , r = 0 .$ The expected consultant profit remains the same, $\pi _ { i } ^ { 0 } = 1 2 ( i = 1 , 2 ) .$ , across all treatments.

To provide corresponding incentives to the subjects, we used cash payments for Experiment 1, course credits for Experiment 2, and lottery money for Experiment 3. Subjects could “test drive” the system during 10 dry runs before they participated in the 30 real runs. Although the structure of the game remained the same between dry and real runs, we used slightly different parameters.<sup>9</sup> We summarize the parameterization of our real run experiments in Table 2.

We summarize our findings in Tables 3–5. We find that, overall, the client is able to capture more project value from increased consultant skill via learning and staging, as H1(b) and H1(c) are both supported. In Experiment 1, client profit increases from 17.247 in $T _ { 1 }$ to 18.486 in T $( t = { \bar { 0 } } . 9 4 1 , { \mathrm { n . s . } } )$ to 21.466 in $T _ { 4 } ~ ( t =$ 206371 $p < 0 . 1 )$ . Results are similar in Experiment 2 and Experiment 3 (when applicable). We find only partial support for H1(a), as client profit increase from $\mathbf { \hat { T } } _ { 1 }$ and $T _ { 3 }$ in Experiment 1 is not significant, perhaps due to small changes in learning rates (from $n = 0 . 5$ to $n =$ 0095; it turns out to be significant in Experiment 2, as client profit increases from 16.625 in $T _ { 1 }$ to 18.218 in $T _ { 3 }$ $( t = 2 . \bar { 0 } 1 , p < 0 . 1 )$

Our analysis also provides partial support for H2. In Experiment 1, consultants scale back their Stage 1 effort from 10.257 (T 5 to 5.586 (T 5 in response to a reduced first-stage project size $( \alpha = 0 . 3 \mathrm { ~ i n ~ } T _ { 1 }$ versus $\alpha = 0 . 1 2 8$ in $\bar { T _ { 2 } } )$ , which is significant $\left( t = 4 . 8 6 9 \right.$ $p < 0 . 0 0 1 )$ . Similarly, in Experiment $^ { 2 , }$ consultants reduce their Stage 1 effort from 13.966 (T 5 to 10.937 (T 5, though the change is not significant $\displaystyle { ( t = 1 . 0 4 2 , }$ n.s.). Support for H2 suggests indirectly that the client can reduce IT project risk by awarding a smaller, rather than larger, first-stage project to a faster learning team.

In summary, our experiments reveal that learning and staging in contracting play an important role in creating and capturing IT value for the client. Interestingly, student subjects tend to expend more effort than necessary, while the executive subjects seem to be more rational in choosing the theoretically optimal effort levels. This suggests potential future extensions of our model to explore the heterogeneity in IT expertise across subject groups.<sup>10</sup> Overall, our findings are robust across experiments; and we did not expect and did not find significant qualitative behavior differences among subjects. An analysis of click-through data also shows no significant differences across treatments, subjects, or stages.<sup>11</sup>

## 7. Conclusions

By constructing a principal-agent model and validating our model experimentally, we study how firms can create and capture EIT project value via IT contract design. Our model integrates three previously isolated streams of research—dynamic production functions, multiperiod moral hazard, and IT outsourcing and contracting—in the context of EIT project management. Specifically, we create a single model that links salient features of EIT markets (contract choice, learning, risk management practice) to project outcome.

Table 3 Summary of Predicted versus Observed Consultant Efforts (Mean and Variance)

<table><tr><td rowspan="3"></td><td colspan="4">Stage 1 effort ( $x_{1}$ )</td><td colspan="4">Stage 2 effort ( $x_{2}$ )</td></tr><tr><td rowspan="2">Predicted</td><td colspan="3">Observed</td><td rowspan="2">Predicted</td><td colspan="3">Observed</td></tr><tr><td>Exp. 1</td><td>Exp. 2</td><td>Exp. 3</td><td>Exp. 1</td><td>Exp. 2</td><td>Exp. 3</td></tr><tr><td> $T_{1}$ </td><td>8.172</td><td>10.257(3.290)</td><td>13.966(28.262)</td><td>8.583(4.545)</td><td>9.820</td><td>12.775(4.448)</td><td>16.850(35.652)</td><td>10.692(2.654)</td></tr><tr><td> $T_{2}$ </td><td>4.418</td><td>5.586(3.153)</td><td>10.937(53.134)</td><td>N/A</td><td>11.805</td><td>12.392(7.516)</td><td>15.109(66.812)</td><td>N/A</td></tr></table>

Note. The mean is shown at the top of each cell; variance is shown in parenthesis.

Table 4 Summary of Predicted versus Realized Client/Consultant Profits

<table><tr><td rowspan="3"></td><td colspan="4">Client profit</td><td colspan="4">Consultant profit</td></tr><tr><td rowspan="2">Predicted</td><td colspan="3">Realized</td><td rowspan="2">Predicted</td><td colspan="3">Realized</td></tr><tr><td>Exp. 1</td><td>Exp. 2</td><td>Exp. 3</td><td>Exp. 1</td><td>Exp. 2</td><td>Exp. 3</td></tr><tr><td> $T_1$ </td><td>22.547</td><td>17.247</td><td>16.625</td><td>16.695</td><td>12</td><td>12.352</td><td>5.650</td><td>10.459</td></tr><tr><td> $T_2$ </td><td>22.547</td><td>13.952</td><td>13.476</td><td>N/A</td><td>12</td><td>12.743</td><td>4.111</td><td>N/A</td></tr><tr><td> $T_3$ </td><td>25.845</td><td>18.486</td><td>18.218</td><td>N/A</td><td>12</td><td>5.486</td><td>6.609</td><td>N/A</td></tr><tr><td> $T_4$ </td><td>29.020</td><td>21.466</td><td>21.335</td><td>20.652</td><td>12</td><td>-0.642</td><td>6.508</td><td>4.887</td></tr></table>

Theoretically, we extend previous multiperiod moral hazard models to incorporate (1) learning and dynamic production functions, (2) risk diversification and reduction over project periods, and (3) linkages (contingent contracts) between periods. These characteristics are particularly salient to large-scale EIT projects but have not been formally treated or experimentally tested in the literature.

In turn, our analysis yields several new insights into contract design. First, we examine the role of agent learning. In general, multistage contracts tend to be favorable in the presence of vendor learning or the possibility of exogenous risk reduction. Gains from staging depend on the rate of learning and can be large–relative to project revenue. Our results are robust across situations in which learning depends not just on first-period project size but also on investments in training. In the absence of learning and discounting, single-stage “big bang” projects are generally preferable over staged projects among risk-neutral agents. Our results appear to grow stronger when we consider risk-averse agents. Finally, we provide a theoretical basis for the conditions in which EIT value creation takes an inverted-U form, and thus provide theoretical underpinnings for recent empirical findings about EIT value creation associated with EIT project management (e.g., Aral et al. 2006, Bouhdary and Comes 2008, Hitt et al. 2002).

Table 5 Summary of Results (t-statistics)

<table><tr><td>Hypotheses</td><td>Experiment 1</td><td>Experiment 2</td><td>Experiment 3</td></tr><tr><td>H1(a):  $V$  increases from  $T_1$  to  $T_3$ </td><td>0.941</td><td>2.010*</td><td>N/A</td></tr><tr><td>H1(b):  $V$  increases from  $T_3$  to  $T_4$ </td><td>2.637*</td><td>4.375***</td><td>N/A</td></tr><tr><td>H1(c):  $V$  increases from  $T_1$  to  $T_4$ </td><td>5.614***</td><td>6.046***</td><td>5.205***</td></tr><tr><td>H2:  $x_1$  decreases from  $T_1$  to  $T_2$ </td><td>4.869***</td><td>1.042</td><td>N/A</td></tr></table>

Notes. One-tailed t-test assuming two-sample equal variances for Experiment 1 and unequal variances for Experiments 2 and 3.  
<sup>∗∗∗</sup>p < 00001, <sup>∗∗</sup>p < 0001, and <sup>∗</sup>p < 001.

Using controlled lab experiments, we test theorybased relationships among IT project value, learning, and staging in contracting. We show that learning allows the client to receive higher value by staging the project, and a faster learning rate results in a smaller first-stage project size. Experiments suggest that our theoretical results are robust to deviations from our specific assumptions about production functions or agent risk attitudes. Academically, these findings extend the literature on software contracting from development (e.g., Lee and Png 1990, Wang et al. 1997, Whang 1992) to off-the-shelf software service (e.g., implementation and maintenance). Practically, they have immediate implications for IT contract design in EIT markets and also in the recently emerged SaaS (software-as-a-service) markets where traditional EIT software vendors are in transition (Chou 2010), suggesting significant benefits from relatively small changes to contract structure terms.

Our model and experiments highlight the importance of agent learning, patience, and risk attitude, and their relationship with optimal project staging, in the context of EIT project risk management. Although our results provide some initial insights into one aspect of contracting for enterprise software projects, opportunities remain for extending these models and empirically investigating the relationship between EIT value creation and contract structure using laboratory or natural experiments. Some potential extensions of our model include the following: examining the optimal contracting across repeated projects where there may be learning across projects; modeling contracting for simultaneous projects, in the presence of agent learning; examining the impact of competition among vendors; or modeling the diseconomies of splitting a project. We anticipate that a fruitful line of research can be built upon our model.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.1120.0448.

## Acknowledgments

The authors thank Ernst Berndt, Ravi Bapna, Anandhi Bharadwaj, Hemant Bhargava, Erik Brynjolfsson, Ramnath Chellappa, Eric Clemons, Jian Chen, Rajiv Dewan, Cheryl Gaimon, Shane Greenstein, Alok Gupta, Paul Hofmann, Robert J. Kauffman, Stelios Kavadias, Paul R. Kleindorfer, Ramayya Krishnan, Nigel P. Melville, Barrie R. Nault, Marius Florin Niculescu, Ivan Png, Nils Rudi, Vallabh Sambamurthy, Sandra Slaughter, Eli Snir, Eric van Heck, Koert van Ittersum, Lizhen Xu and seminar participants at Carnegie Mellon University, RSM Erasmus University, Georgia Institute of Technology, INSEAD, Tsinghua University, University of California at Davis, University of Maryland at College Park, University of Minnesota, the Thirty-Seventh Annual Hawaii International Conference on System Sciences (HICSS-37), the National Bureau of Economic Research (NBER) Summer Institute Productivity Potpourri Workshop (2008), the 3rd Annual SAP Sponsored Academic Research Conference, and the Workshop on Information Systems and Economics (2008), for helpful comments and suggestions. We thank Yifan Dou for his outstanding research assistance. A previous and much shorter draft of the modeling section appeared in HICSS-37 Proceedings. We also thank Anitesh Barua (the senior editor), the associate editor, and three anonymous reviewers for their constructive comments and insights. This work was funded in part by the Ernest Scheller Jr. College of Business of Georgia Institute of Technology, office of the Chief Scientist of SAP Labs, Palo Alto, CA, the E-Business Center of the Smeal College of Business at Pennsylvania State University, the Fudan Institute for Sustainable Innovation and Growth, and NSF [Grant IIS-9733877]. All opinions and errors are the authors’ own.

## References

Anderson EG (2001) Managing the impact of high market growth and learning on knowledge worker productivity and service quality. Eur. J. Oper. Res. 134(3):508–524.

Aral S, Brynjolfsson E, Wu DJ (2006) Which came first, IT or productivity? The “virtuous cycle” of investment and use in extended enterprise systems. Proc. 27th Internat. Conf. Inform. Systems, Milwaukee, WI.

Banker R, Davis G, Slaughter S (1998) Software development practices, software complexity, and software maintenance. Management Sci. 44(4):433–450.

Barry E, Mukhopadhyay T, Slaughter S (2002) Software project duration and effort: An empirical study. Inform. Tech. Management 3(1):113–136.

Bolton P, Dewatripont M (2005) Contract Theory (MIT Press, Cambridge, MA).

Bouhdary C, Comes S (2008) Accelerate value creation: The virtuous cycle of using technology to maximize business value. SAP Executive Insight (October), 1–8.

Brooks FP (1975) The Mythical Man Month (Addison Wesley, Reading, MA).

Brynjolfsson E, Fitoussi D, Hitt L (2006) The information technology iceberg. Working paper, MIT Sloan School of Management, Cambridge, MA.

Chellappa R, Saraf N (2010) Alliances, rivalry and firm performance in enterprise systems software markets: A social network approach. Inform. Systems Res. 21(4):849–871.

Chiappori PA, Ines M, Patrick R, Salanie B (1994) Repeated moral hazard: The role of memory, commitment, and the access to credit markets. Eur. Econom. Rev. 38(8):1527–1553.

Chou T (2010) Cloud: Seven Clear Business Models (Active Book Press, Los Altos Hills, CA).

Choudhury V, Sabherwal R (2003) Portfolios of control in outsourced software development projects. Inform. Systems Res. 14(3):291–314.

Clemons E, Hitt L, Snir E (2001) A risk analysis framework for IT outsourcing. Wharton OPIM Working paper, The University of Pennsylvania, Wharton School, Philadelphia.

Cohen MC, Agrawal N, Agrawal V (2006) Winning in the aftermarket. Harvard Bus. Rev. 84(5):129–138.

Davenport TH (2005) The coming commoditization of processes. Harvard Bus. Rev. 83(6):101–108.

DiRomualdo A, Gurbaxani V (1998) Strategic intent for IT outsourcing. Sloan Management Rev. 39(4):67–80.

Gaimon C (1997) Planning information technology—knowledge worker systems. Management Sci. 43(9):1308–1328.

Gaimon C, Ozkan G, Napoleon K (2011) Dynamic resource capabilities: Managing workforce knowledge with a technology upgrade. Organ. Sci. 22(6):1560–1578.

Haines M, Goodhue D (2003) Implementation partner involvement and knowledge transfer in the context of ERP implementations. Internat. J. Human-Comput. Interaction 16(1):23–38.

Harrison G, List J (2004) Field experiments. J. Econom. Literature 42(4):1009–1055.

Hitt LM, Wu DJ, Zhou X (2002) ERP investment: Business impact and productivity measures. J. Management Inform. Systems 19(1):71–98.

Holmstrom B (1982) Moral hazard in teams. The Bell J. Econom. 13(2):324–340.

Holmstrom B, Milgrom P (1987) Aggregation and linearity in the provision of intertemporal incentives. Econometrica 55(2): 303–328.

James G (1998) Method of payment. CIO Enterprise (October 15, Section 2):92–95.

Kirsch LJ (2000) Software project management: An integrated perspective for an emerging paradigm. Zmud RW, ed. Framing the Domains of IT Management Research: Glimpsing the Future Through the Past, Chap. 15. (Pinnaflex Educational Resources Inc., Cincinnati, OH), 285–304.

Lacity M, Hirschheim R (1993) The information systems outsourcing bandwagon: Look before you leap. Sloan Management Rev. 35(1):72–86.

Lacity M, Willcocks L (1998) Practices in information technology outsourcing: Lessons from experience. MIS Quart. 22(3): 363–408.

Lambert R (1983) Long-term contracts and moral hazard. Bell J. Econom. 14(2):441–452.

Lee TK, Png IPL (1990) The role of installment payments in contracts for services. RAND J. Econom. 21(1):83–99.

Levy F (1965) Adaptation in the production process. Management Sci. 11(6):B136–B154.

Lilien GL, Kotler P, Moorthy KS (1992) Marketing Models (Prentice Hall, Upper Saddle River, NJ).

Loch CH, Kavadias S (2002) Dynamic portfolio selection of NPD programs using marginal returns. Management Sci. 48(10):1227–1241.

Markus LM, Tanis C, van Fenema PC (2000) Multisite ERP implementations. Comm. ACM 43(4):42–46.

McAfee A (2002) The impact of enterprise information technology adoption on operational performance: An empirical investigation. Production Oper. Management 11(1):33–53.

McAfee A (2003) When too much IT knowledge is a dangerous thing. MIT Sloan Management Rev. 44(2):83–89.

McAfee RP, McMillan J (1986) Bidding for contracts: A principal– agent analysis. RAND J. Econom. 17(3):326–338.

McAfee RP, McMillan J (1987) Competition for agency contracts. RAND J. Econom. 18(2):296–307.

McFarlan FW (1981) Portfolio approach to information systems. Harvard Bus. Rev. 59(5):142–150.

Mendelson H (2000) FoxMeyer’s Delta project. Stanford Graduate School of Business Case, Stanford University, Stanford, CA.

Nolan R, McFarlan FW (2005) Information technology and the board of directors. Harvard Bus. Rev. 83(10):96–106.

O’Leary D (2002) Enterprise Resource Planning Systems: Systems, Life Cycle, Electronic Commerce, and Risk (Cambridge University Press, New York).

Pike G (2006) Supporting business innovation while reducing technology risk. White paper, SAP AG, Walldorf, Germany.

Retrieved September 21, 2012, http://www.sap.com/ malaysia/solutions/safeguarding/pdf/supportBiz20sep.pdf.

Radner R (1981) Monitoring cooperative agreements in a repeated principal–agent relationship. Econometrica 49(5):1127–1148.

Radner R (1985) Repeated principal–agent games with discounting. Econometrica 53(5):1173–1198.

Richmond WB, Seidmann A (1993) Software development outsourcing: Contract structure and business value. J. Management Inform. Systems 10(1):57–72.

Richmond WB, Seidmann A, Whinston AB (1992) Incomplete contracting issues in information systems development outsourcing. Decision Support Systems 8(4):459–477.

Rogerson WP (1985) Repeated moral hazard. Econometrica 53(1): 69–76.

SAP annual report (2008) Retrieved December 21, 2010, http:// www.sap.com/about/investor/reports/annualreport/2008/pdf/ SAP\_2008\_Annual\_Report.pdf.

Scott J (1999) The FoxMeyer Drugs’ bankruptcy: Was it a failure of ERP? Proc. Fifth Americas Conf. Inform. Systems, Milwaukee, WI, 223–225.

Snir E, Hitt L (2004) Vendor screening in information technology contracting with a pilot project. J. Organ. Comput. Electronic Commerce 14(1):61–88.

Umble EJ, Haft RR, Umble MM (2003) Enterprise resource planning: Implementation procedures and critical success factors. Eur. J. Oper. Res. 146(2):241–257.

Wang ETG, Barron T, Seidmann A (1997) Contracting structures for custom software development: The impact of informational rents and uncertainty on internal development and outsourcing. Management Sci. 43(12):1726–1744.

Whang S (1992) Contracting for software development. Management Sci. 38(3):307–324.
