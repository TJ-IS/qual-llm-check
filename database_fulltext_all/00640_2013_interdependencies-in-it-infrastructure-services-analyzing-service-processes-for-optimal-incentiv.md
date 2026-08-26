---
otero_id: 640
otero_key: "NVHCWY48"
title: "Interdependencies in IT Infrastructure Services: Analyzing Service Processes for Optimal Incentive Design"
authors: "Sagnika Sen; T. S. Raghu"
year: "2013"
journal: "Information Systems Research"
doi: "10.1287/isre.2013.0475"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/NVHCWY48/fulltext/images/345095f4f540ad03c617f19c8f0d16c1f788b3bd0b75cd2cad6ca58c222cdf40.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Interdependencies in IT Infrastructure Services: Analyzing Service Processes for Optimal Incentive Design

Sagnika Sen, T. S. Raghu

## To cite this article:

Sagnika Sen, T. S. Raghu (2013) Interdependencies in IT Infrastructure Services: Analyzing Service Processes for Optimal Incentive Design. Information Systems Research 24(3):822-841. http://dx.doi.org/10.1287/isre.2013.0475

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2013, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/NVHCWY48/fulltext/images/661f16647bd52b997a0d9e3dd0ea455fb02b249454fb5ee1d532bbcbdbfc21c4.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Interdependencies in IT Infrastructure Services: Analyzing Service Processes for Optimal Incentive Design

Sagnika Sen

Pennsylvania State University, Penn State Great Valley, Malvern, Pennsylvania 19355, sus45@psu.edu

T. S. Raghu

W. P. Carey School of Business, Arizona State University, Tempe, Arizona 85287, raghu.santanam@asu.edu

nformation technology (IT) infrastructure outsourcing arrangements involve multiple services and processes Ithat are interdependent. The interdependencies pose significant challenges in designing appropriate incentives to influence a provider’s effort-allocation decisions. By integrating process modeling fundamentals with multitask agency theory, we enumerate the base set of possible interrelationships among different IT service processes and derive corresponding optimal incentives. Our results demonstrate the impacts of risk profile, random noise, value-cost ratio, and process structure on optimal incentive rates. We find that the current practice of treating IT services as essentially independent is optimal only in limited settings where both the service provider and customer are risk neutral. Interestingly, incongruent performance measures require optimal incentive rates to respond in complex ways to the strength of coupling between services and the complementarity and substi tutability of services. We also analyze more complex process scenarios using different combinations of the base set. The results demonstrate that, while the findings from the base set largely hold, the value-cost ratio of the services and the performance measure congruity can pose unique challenges in determining incentive rates.

Key words: IT outsourcing; service level agreements; incentives; agency theory; process interdependence History: Debabrata Dey, Senior Editor; Sudip Bhattacharjee, Associate Editor. This paper was received April 13, 2010, and was with the authors 14 months for 3 revisions. Published online in Articles in Advance March 21, 2013.

## 1. Introduction

Service contracts in information technology (IT) infrastructure outsourcing often feature multiple performance measures and incentives with no explicit consideration for how the performance measures and underlying processes interact (TDWI 2009). Evaluating services in isolation can contribute to inefficiencies because it may result in effort allocation toward more sensitive and/or more rewarding performance goals. Frequent renegotiations, deal terminations, and litigations (Deloitte Consulting 2005) are symptoms of these inefficiencies and contribute to a huge financial burden on stakeholders. Consequently, performance assessment becomes challenging if organizations do not consider the interdependencies between business processes and the congruence of performance measures to firm objectives (McIvor et al. 2009). Although interdependent performance measurement challenges (Feldman 2010, McIvor et al. 2009) are acknowledged in practitioner literature (TDWI 2009), the issue of inducing appropriate effort allocation in multiservice IT outsourcing contracts remains underexplored in academic literature (Dey et al. 2010, Fitoussi and Gurbaxani 2012). To the best of our knowledge, scholarly work analyzing the linkage between process interdependencies, performance measures, and incentives is limited.

Most infrastructure outsourcing contracts consist of multiple services that include, but are not limited to, network management, desktop support, email, and application services. Because the different services may have asymmetric cost (to the provider) and benefit (to the customer), a major challenge in incentive design arises from the interdependencies between services. For example, email services not only depend on configuration of the email servers, but also on network performance. Similarly, database response time and application response time may be correlated (Feldman 2010). These interdependencies pose risks— both for the customer and the provider of managed services.

In this paper, we investigate single-period incentives between a single service provider and a customer organization. The incentives cover multiple services with corresponding service level agreements (SLAs). However, performance measures may be interdependent.

Our main objectives are the characterization of optimal incentive rates for such interdependent services and to provide managerial insights on how process interdependence affects incentives. We take a twostep approach to achieve these objectives. First, we characterize the six basic primitives of service interrelationships that are defined formally in the processmodeling literature. Second, we analyze the incentive implications for each service interrelationship using a multitask agency theoretic framework. In addressing our main research objectives, we limit the scope of our work to a single-provider, single-period incentive design. Given our focus on service performance, we do not explicitly address investment or resource allocation decisions in infrastructure.

The contribution of our work is threefold. First, we systematically identify and categorize the base set of interdependencies in IT infrastructure services. Second, we characterize the optimal incentive rates corresponding to each base set of interdependence. These characterizations provide insights on the effects of risk profile, performance measure noise, congruence, value-cost relationship, and process structure on optimal incentive rates. We show that the value-cost ratio of services is an important component of incentive structure. By constructing complex scenarios from the base set, we also show when the incentive implications for more complex scenarios are likely to be a simple extension of base-set results and when they are not. Third, our research provides insights relevant to the contentious debate among practitioners on whether inclusion of multiple performance measures is beneficial. We show that the benefits of using multiple performance measures progressively decline as errors in performance measures increase. More interestingly, multiple performance measures appear to be more beneficial in sequential relationships when first-stage actions have a relatively lower value-cost ratio than that of the subsequent stages, and this benefit increases with increasing sequential coupling between the stages. Finally, our analysis demonstrates that the current practice of isolated SLA measures is perhaps most suited to cases where both customer and provider organizations are risk neutral. Risk aversion on the part of either the provider or the customer requires more careful consideration of process relationships.

The rest of the paper is organized as follows. In §2, we briefly describe the theoretical underpinnings from process and agency theoretic perspectives to address service interdependency. Using Petri net formalism, we identify the base set of process configurations that has agency implications in the context of IT services. Section 3 presents the formal model and the optimal incentive structure for each type of interdependency. In §4, we build more complex scenarios that are combinations from the base set and examine their implications. Finally, we present concluding remarks in §5.

## 2. Incorporating Service Interdependence in the Design of Incentives

To motivate the “right behavior,” practitioner literature advocates the use of detailed performance measures (TDWI 2009) with appropriate rewards/ penalties. However, SLA formulation process mostly ignores the challenges of interdependent services (e.g., Deloitte Consulting 2005, Feldman 2010, McIvor et al. 2009). To provide insights on optimal incentives for interdependent services, we develop an integrative perspective based on multitask agency theory and process modeling. In the following, we outline the motivation for using these two theoretical perspectives.

## 2.1. Agency Perspective

Theory of the firm (Coase 1937) has served as the fundamental theoretical lens for understanding the nature and structure of organizations. Transaction cost economics (TCE) and incomplete contract theory have developed on the main ideas enunciated in Coase (1937) to explain firm decisions and tradeoffs inherent in make or buy decisions (Grossman and Hart 1986). Agency theory (Jensen and Meckling 1976) is another important extension of the line of work related to the theory of the firm. While TCE and incomplete contracts theory are helpful in explaining decisions related to organizational structure, agency theory explains the nature of incentives and performance measurements necessary to account for moral hazard inherent in agency relationships (whether with employees or vendors). We have specifically chosen to focus on the incentive issues inherent in outsourcing relationships; we consider the decision related to make or buy as outside the scope of this research. Given the focus on incentives, agency theory provides the most appropriate theoretical base for our work.

Our motivation to examine incentive issues stems from the observation that most IT outsourcing arrangements are characterized by multiple interdependent objectives. There is also early evidence to suggest that a “best practices” approach may not be the most appropriate for IT outsourcing because firm conditions can differ considerably from one another (Ross and Westerman 2004). In this context, multitask agency theory (Datar et al. 2001, Feltham and Xie 1994, Holmstrom and Milgrom 1991) is especially a good fit, because it can provide guidance in understanding the moral hazard context related to effort allocation across multiple tasks that IT vendors perform. Effort allocation refers to the fact that the agent’s decision to apportion his/her efforts among the different tasks is a function of several factors, including incentives on each of the tasks, measurability, controllability, and risk profile. Hence the objective is to choose performance measures and the power of the corresponding incentives so as to induce the optimal set of actions by the agent (Banker and Datar 1989). Literature on IT outsourcing has also proposed agency theory as a suitable framework for evaluating contracts between a service provider and its customer (Cheon et al. 1995). More recently, multitask agency theory has also been used as the theoretical basis in empirical studies of IT outsourcing (Fitoussi and Gurbaxani 2012, Susarla et al. 2010).

## 2.2. Process Perspective

Because incentives and SLAs are generally based on operational performance measures, the workflow perspective enables to thoroughly analyze multitask incentives and performance issues (Basu and Blanning 2000). Interestingly, although multitask agency models in economics literature have attempted to understand effort allocation by agents, workflow concerns were not integrated into these settings. We conjecture that the lack of focus on workflow is perhaps because of the disciplinary emphasis on generic economic relations rather than process contingencies. The novelty in our research is that we impose the workflow specific concerns on the multitask agency model to derive process related implications. The workflow-agency interaction (e.g., Raghu et al. 2004) developed in this research enables the examination of moral hazard issues arising from task structures and performance measure interrelationships.

## 2.3. Characterizing Interdependencies in IT Infrastructure Services

We utilize Petri nets, a formal language for modeling and analyzing workflows (van der Aalst and Hee 2004). We first define the base Petri net constructs (Figure 1, panel I) in the IT service context.

• Places—State of the system before or after performing a service (e.g., processing help-desk request, software upgrades, etc.). Performance measures capture the state information.

• Transitions—This represents the workflow required for a service. This transition can be further decomposed into a set of actions for a particular service.

• Tokens—Information about the state of the system (the output tokens may capture the performance measure), as well as conditions (to start a service process, e.g., a request arrives, a failure occurs).

The workflow routing scheme determines the interrelationship between services and associated performance measures. Any routing scheme in a workflow system can be modeled based on six workflow primitives (Kumar and Zhao 1999). The six workflow primitives are AND-join, AND-split, OR-join, OR-split, iteration, and causality. In the following, we discuss the performance measurement implications of each of the six workflow primitives.

2.3.1. AND-Join. An AND-join implies that two (or more) states of the system simultaneously activate a single workflow, which in turn affects one performance measure (Figure 1, panel II). Because there is a single workflow affecting a single performance measure, there are no agency issues because of service interdependencies. Thus, although agency issues because of noisy performance measures and outcomes may exist, this routing scheme does not create effort allocation inefficiencies.

2.3.2. AND-Split. An AND-split implies either (1) one workflow changes the state information (performance measure) of two (or more) services (Figure 1, panel III), or (2) a single event triggers two simultaneous workflows (Figure 1, panel IV). The first case represents the scenario where one action or set of actions affect multiple performance measures. For example, the network outage recovery process would affect the “availability” of a variety of services (email, directory, Internet). Because a single action or set of actions affect multiple measures, this configuration creates correlation in the performance measures. The second case represents the scenario where a separate action or set of actions (triggered by an external event) affect multiple performance measures. For example, a seasonal demand surge can adversely affect network and applications services performance.

2.3.3. OR-Split. An OR-Split implies that when either of different (sets of) performance measure(s) are affected by two different workflows (Figure 1, panel V), the choice of the workflow to be executed is determined from the initial-state information. Although this configuration may be applicable to contexts where a choice is made at the beginning of service (e.g., choice of server software), it does not necessarily give rise to interdependent services issues on its own if the decision to execute a particular workflow is observable to the customer. When the decision is not observable, performance information may reveal the decision and subsequent workflow. Also, because the workflow and the subsequent states are anyway paired, this routing scheme does not translate to agency related dependency issues for IT services when viewed in isolation.

2.3.4. OR-Join. The implication of an OR-join for service processes is that either one of the workflows may affect the same performance measure (Figure 1, panel VI). The two workflows then can be considered as complementary/substitutes to each other with respect to the particular performance measure. The relative sign (positive/negative) of the effect determines whether this dependency is complementary or substitute. For instance, examples of complementary services include email transfer performance and network performance, and spam filters and virus protection for email services. On the other hand, alternative choice of services (e.g., NetMeeting versus any open source alternative for communication services) is an example of substitute services.

Figure 1 Workflow Primitives in IT Infrastructure Services  
![](/api/attachments/NVHCWY48/fulltext/images/03b76330cc1e2905ff72874570164f4c7f90908adb3ea82626b127076eddb0ce.jpg)

2.3.5. Causality/Sequential Dependency. Causality implies that two service processes are linked in such a manner that one workflow changes the state that triggers another workflow and a subsequent change of state (Figure 1, panel VII). That is, the performance measure of the preceding service affects the performance measure of the following service. For example, the design of directory services may depend on network performance. Similarly, directory information accuracy may depend on the performance of email services.

2.3.6. Iteration. An Iterative routing scheme between service workflows implies that the processes are being repeatedly executed. This is akin to the concept of reciprocal dependency (Thompson 1967). In the context of infrastructure outsourcing, reciprocal dependency can be observed at two different levels of process hierarchy.

Table 1 Routing Schemes and Corresponding Agency Implications

<table><tr><td>Petri net primitives</td><td>Implications</td><td>Example</td></tr><tr><td>AND-join</td><td>One workflow affects one performance measureNo effort allocation issues</td><td>Help-desk activities (for a particular request) affect the performance of the problem responsiveness</td></tr><tr><td>AND-split</td><td>One workflow affects multiple performance measuresCorrelated performance measures</td><td>Activities relating to restoring the network outage affects the availability of network as well as email services</td></tr><tr><td>OR-join</td><td>Multiple workflows may affect one performance measureProvider&#x27;s effort allocation on each workflow depends on the cost/reward considerationsComplementary/substitutive services</td><td>Spam filter maintenance and antivirus maintenance both affect security of email services</td></tr><tr><td>OR-split</td><td>Observable decision/condition triggers the choice of workflowDecision observability precludes moral hazard issues, for unobservable decisions posterior performance provides information about the decision</td><td>Choice of software platform (server/operating system)determines the set of required activities and corresponding performance measure</td></tr><tr><td>Causality/sequential dependency</td><td>Sequential dependency in more than one workflowProvider&#x27;s effort allocation on each workflow depends on the cost/reward considerations and the effect on the subsequent workflow</td><td>Network configuration and performance affects the design and performance of directory services/database services</td></tr><tr><td>Iteration</td><td>Repetitive workflow executionContinuous monitoring. May be caused because of errors in operational environment, but the effect of errors are directly observable from performance measures, thus precluding moral hazard issues</td><td>Continuous performance monitoring and adaptation</td></tr></table>

At the relationship level, reciprocal dependency arises because of specificity of investments in assets, resources, and the relationship (Combs and Ketchen 1999). As long as investments by both firms are balanced, there is reduced incentive for opportunistic behavior (Poppo and Zenger 2002, Poppo et al. 2008). However, if relationship specific investments are unbalanced, it can lead to opportunistic behavior by both entities. The two entities can, therefore, engage in negotiations and refinement of the contracts over the duration of the relationship to counter this. Given the strategic interactions and multiperiod nature, one would need a different modeling approach to address the incentive implications of reciprocal dependency at the relationship level.

At the workflow level, a reciprocal dependency between two services implies that the output of one service depends upon the other’s performance, and vice versa. As per the Petri net-based workflow constructs, this essentially implies an iteration. The set of activities enclosed within the iteration can still be separately analyzed as they would fit into one of the other five primitives. For instance, a repeated set of workflow activities (i.e., repeated fixes and tests) associated with the recovery of Amazon Cloud services may be cited as an example of such iteration.<sup>1</sup> However, at the end of the iterations, “availability” is all that matters from a performance perspective and not the number of iterations or the exact sequence of tests or fixes. Thus, in most iterative workflows, performance metrics on the outcome would preclude the need to consider the specific activities within the iterative workflow.

The above analysis provides a complete base set of three types of interdependencies that create agency implications in an IT service context. They include the following:

1. Correlated performance measures (AND-split).

2. Complementary/substitute actions for different services (OR-Join).

3. Sequentially dependent actions (Causality).

An IT infrastructure service scenario can be represented by any of these three base interdependencies (or combinations thereof). Table 1 summarizes the six routing schemes and their implications for incentive design from an agency theoretic perspective. These relationships are used in the models formulated in the next section.

## 3. Modeling Framework

We utilize the multitask agency theory literature (Banker and Datar 1989, Datar et al. 2001, Dikolli et al. 2009, Feltham and Xie 1994, Holmstrom and Milgrom 1991) as the modeling framework for this research. For model simplicity, we utilize a single provider, single-period setting and focus only on the operational and tangible measures of IT services. A service (e.g., network management) may require more than one action $a _ { j }$ (e.g., manage server, update networking software). A number of actions may affect the performance measure (p) for a service (see Table 2 for notations). The principal can only contract on the

Table 2 Notations Used

<table><tr><td> $p_i$ </td><td>ith performance measure</td></tr><tr><td> $\alpha$ </td><td>Fixed-part of the compensation</td></tr><tr><td> $\beta_i$ </td><td>Incentive rate provided for service  $i$ </td></tr><tr><td> $a_j$ </td><td> $j$ th action,  $a_j \geq 0$ </td></tr><tr><td> $g_i$ </td><td>Sensitivity of the  $i$ th action on the corresponding performance measure (exogenous)</td></tr><tr><td> $f_i$ </td><td>Sensitivity of the  $i$ th action to the principal&#x27;s (customer&#x27;s) outcome (exogenous)</td></tr><tr><td> $\varepsilon_{p_i}$ </td><td>Impact of factors other than the agent&#x27;s (provider&#x27;s) actions on the  $i$ th performance measure</td></tr><tr><td> $\sigma_{p_i}$ </td><td>Variance of performance measure  $p_i$ </td></tr><tr><td> $\rho_{ij}$ </td><td>Covariance of performance measure  $p_i$  and  $p_j$  (exogenous)</td></tr><tr><td> $\varepsilon_x$ </td><td>Impact of factors other than the agent&#x27;s (provider&#x27;s) actions on the principal&#x27;s outcome</td></tr><tr><td> $U_P$ </td><td>Principal&#x27;s (customer organization&#x27;s) utility/benefit</td></tr><tr><td> $x_P$ </td><td>Principal&#x27;s (customer organization&#x27;s) outcome function</td></tr><tr><td> $U_A$ </td><td>Agent&#x27;s (provider&#x27;s) utility/benefit</td></tr><tr><td> $w_A$ </td><td>Compensation made to the agent (provider)</td></tr><tr><td> $W_A$ </td><td>Agent&#x27;s (provider&#x27;s) net income after deducting the cost of effort</td></tr><tr><td> $C_A$ </td><td>Agent&#x27;s (provider&#x27;s) cost of effort</td></tr><tr><td> $r_A$ </td><td>Coefficient of the agent&#x27;s (provider&#x27;s) constant absolute risk aversion (exogenous)</td></tr><tr><td> $k_{OR}$ </td><td>Complementary/Substitute effect of one service on another in an OR-join (exogenous)</td></tr><tr><td> $k_{SEQ}$ </td><td>Sequential coupling factor of actions taken in the first stage(s) on the subsequent stage(s) in a sequential dependency (exogenous)</td></tr></table>

observed performance, p, because he or she cannot directly observe agent’s actions/efforts. Performance measures are therefore imperfect indicators of the true action taken by the agent. Principal’s outcome (x5, however, is based on the agent’s true actions. So the optimization problem is to find the incentive that optimizes the agent’s actions/efforts in the best interest of the principal. Our models follow the standard assumptions (linear contract, exponential utility, and normally distributed error functions) that are well established in multitask agency literature (Datar et al. 2001, Dikolli et al. 2009, Feltham and Xie 1994). The performance measure and outcomes are assumed to be linear functions of the action set. Apart from the agent’s actions, some random state of nature affects the performance and outcome variables as well. This is represented by the error variable , which is assumed to be normally distributed with mean zero. The general modeling structure is presented in Table 3. All variables in the models are continuous and differentiable.

The principal’s problem can be expressed with the following formulation:

$$
\max _ {\alpha , \beta} \mathrm{E} [ U _ {\mathbb {P}} ]
$$

$$
\text { Subject   to } \quad [ w _ {\mathbb {A}} (p) ] - C _ {\mathbb {A}} (a)\tag{1}
$$

$$
- \frac {1}{2} r _ {\mathbb {A}} \operatorname{Var} [ w _ {\mathbb {A}} (p) ] \geq \underline {{U}} _ {\mathbb {A}}, \quad \text { and }\tag{2}
$$

a maximizes E6w<sub></sub>4p57

$$
- \frac {1}{2} r _ {\mathbb {A}} \operatorname{Var} [ w _ {\mathbb {A}} (p) ] - C _ {\mathbb {A}} (a).\tag{3}
$$

Table 3 General Model Structure (Suffixes  and  Are Used to Denote the Agent and Principal Respectively)

<table><tr><td>Performance measures</td><td> $p_{i} = Function(g_{1...n}a_{1...m}) + \varepsilon_{p_{i}}$ </td></tr><tr><td>Principal&#x27;s (customer organization) outcome function</td><td> $x_{\mathbb{P}} = \sum_{j=1}^{m} f_{j} a_{j} + \varepsilon_{x}$ </td></tr><tr><td>Total compensation paid to the agent (provider)</td><td> $w_{\mathbb{A}}(p) = \alpha + \sum_{i=1}^{n} \beta_{i} p_{i}$ </td></tr><tr><td>Agent&#x27;s (provider organization) cost of service</td><td> $C_{\mathbb{A}}(a) = \sum_{j=1}^{m} a_{j}^{2}$ (when actions are independent, for scenarios with interdependent actions the structure is a function of the interdependency)</td></tr><tr><td>Principal&#x27;s (customer organization) utility function</td><td> $U_{\mathbb{P}} = x_{\mathbb{P}} - w_{\mathbb{A}}(p)$ </td></tr><tr><td>Agent&#x27;s (provider organization) net income</td><td> $W_{\mathbb{A}} = w_{\mathbb{A}}(p) - C_{\mathbb{A}}(a)$ </td></tr><tr><td>Agent&#x27;s (provider organization) utility function</td><td> $U_{\mathbb{A}}(W_{\mathbb{A}}) = 1 - e^{-r_{\mathbb{A}} W_{\mathbb{A}}}$ </td></tr><tr><td>Agent&#x27;s (provider organization) risk-premium $^{a}$ </td><td> $\frac{1}{2} r_{\mathbb{A}} Var[w_{\mathbb{A}}(p)]$ </td></tr></table>

<sup>a</sup>A sample risk-premium calculation is shown in Appendix A of the online supplement.

The agent (the provider organization) is assumed to be risk averse.<sup>2</sup> The left-hand side of Equation (2) represents agent’s certainty equivalent—expected compensation minus the cost of action and the risk premium (Holmstrom and Milgrom 1991). The risk premium, which is based on the set of assumptions described above, is given by $\begin{array} { r } { \frac { 1 } { 2 } r _ { \mathbb { A } } \operatorname { V a r } [ w _ { \mathbb { A } } ( \hat { p } ) ] } \end{array}$ (Datar et al. 2001, Gibbons 2005). Agent’s reservation utility, $\underline { { U } } _ { \mathbb { A } } ,$ can be assumed to be zero without loss of generality. Equation (2) represents the participation constraint that requires the contract to be sufficiently attractive for the agent to accept it. Equation (3) represents the incentive constraint designed to ensure that actions are in the best interest of the agent (Datar et al. 2001). The solution to the above model yields an optimal effort allocation. Agent’s effort allocation among different tasks is a function of several factors—including incentives on each of the tasks, measurability, controllability, and risk profile. Hence the objective is to balance the performance measures and the power of the corresponding incentives (Feltham and Xie 1994, Gibbons 2005). Two variables play an important role in achieving such balance: agent’s risk profile and performance measure congruity. The latter is the measure of the departure of the vector of marginal products of the agent’s action on performance measure (i.e., vector g5 from the vector of the marginal products of the agent’s action on firm value (i.e., vector f 5 (Datar et al. 2001, Feltham and Xie 1994). Performance measures are congruent when the relative importance of the actions is the same in both the performance measure and outcome functions. A first-best solution can only be achieved under conditions of perfect congruity and risk neutrality. In the following sections, we apply the general modeling structure to the workflow interdependencies discussed in §2. In particular, we explore the effect of risk and congruity on optimal incentive rates.

The basic model structures for each of the three primitives are provided in the upper panel of Table 4. Optimal actions and incentives corresponding to each primitive are obtained by substituting the model expressions in Equations (1)–(3). The optimal solutions for the primitives are presented in the lower panel of Table 4. Based on these solutions, we discuss the implications of agent’s risk profile, noise, and performance-measure congruity for each workflow primitive in the following sections.

## 3.1. AND-Split

Interdependency in AND-Split arises because of two possibilities as discussed in §2.3.2. First, a single action may impact multiple performance measures. However, more than one measure is redundant in this case. Second, correlations in performance measure may arise because of exogenous factors (such as seasonal demand) affecting the performance measures of two (or more) services. We model a twoaction setting with interdependencies as depicted in Table 4, where the error variables of the performance measures are correlated (i.e., $\mathrm { c o v } ( \pmb { \varepsilon } _ { p _ { 1 } } , \pmb { \varepsilon } _ { p _ { 2 } } ) \neq 0 )$ . Without loss of generality, the performance measures can be scaled to have unit variances $( \sigma _ { p _ { 1 } } ^ { 2 } = \sigma _ { p _ { 2 } } ^ { 2 } = 1 )$ , so that the correlation $\rho _ { 1 2 }$ is also the covariance (Christensen et al. 2003). Hence the agent’s risk premium takes the form provided in Table 4. The results illustrate that optimal incentive rates are dependent on risk aversion and error correlations in performance measurement. By separating the effects of value-cost ratio and provider’s risk profile, we derive two specific implications in the following propositions.

<sup>Proposition</sup> <sup>1.</sup> Incentive rate separation is optimal only in the presence of a risk-neutral provider $( i . e . , r _ { \mathbb { A } } \to 0 )$ and the incentive rates equal the value-cost ratio.

From the expressions of $\beta ^ { * }$ in Table 4, as $r _ { \mathbb { A } } \to 0 ,$ $\beta _ { i } ^ { * }  f _ { i } / g _ { i } ( i = \bar { 1 } , 2 )$ . Therefore, a compensation for the error correlation in services is unnecessary for a riskneutral provider. Accordingly, an important aspect of a risk-neutral agent’s compensation is the value-cost $r a t i o { - f / g }$ . Thus, the practice of separately measuring and rewarding performance for individual services is only optimal when both the principal and agent are risk neutral. Further, it can be shown that the incentive rate of risk-averse agents is given by the relationship $\beta _ { i } ^ { * } < f _ { i } / g$ when the error correlation is positive. However, if the error correlation is negative, the relationship between the incentive rates is more nuanced as stated in Proposition 2.

<sup>Proposition</sup> <sup>2.</sup> Incentive rates trend higher because of a negative error correlation. However, a positive error correlation does not always lead to reduced incentive rates.

This follows directly from the comparative statics result on the incentive rates; because both expression are similar, only one is shown:

$$
\frac {d \beta_ {1} ^ {*}}{d \rho_ {1 2}} = - \frac {f _ {2} g _ {2} r _ {\mathbb {A}} (g _ {1} ^ {2} + r _ {\mathbb {A}}) (g _ {2} ^ {2} + r _ {\mathbb {A}}) + r _ {\mathbb {A}} ^ {2} (\rho_ {1 2} ^ {2} f _ {2} g _ {2} r _ {\mathbb {A}} - 2 \rho_ {1 2} f _ {1} g _ {1} (g _ {2} ^ {2} + r _ {\mathbb {A}}))}{(g _ {1} ^ {2} (g _ {2} ^ {2} + r _ {\mathbb {A}}) + r _ {\mathbb {A}} (g _ {2} ^ {2} + (1 - \rho_ {1 2} ^ {2}) r _ {\mathbb {A}})) ^ {2}}.\tag{4}
$$

When the error correlation is negative $( \rho _ { 1 2 } < 0 )$ the derivative is also negative. Consequently, as the error correlation approaches −1, incentive rates and, by association, effort levels increase. Thus, informational benefits of negatively correlated performance measures allow the customer to impose higher risks on the provider. On the other hand, with positively correlated performance measures, a customer organization may still be able to increase incentive rates despite the increased risk premium because of the positive error correlation. As a result, a customer can impose higher risks and extract higher effort levels from performance measure congruence. For instance, assume that the sensitivity factors are such that $f _ { 1 } =$ $m g _ { 1 }$ and $f _ { 2 } = n g _ { 2 }$ . When $g _ { 1 } > g _ { 2 }$ and $m > n ,$ or $g _ { 1 } < g _ { 2 }$ and $m < n ,$ performance measures are congruent. On the other hand, when $g _ { 1 } < g _ { 2 }$ and $m > n ,$ or $g _ { 1 } > g _ { 2 }$ and $m < n ,$ , performance measures are incongruent. Substituting the values of $f _ { 1 }$ and $f _ { 2 }$ in Equation (4), it can be observed that when the error correlation is negative, congruence has no impact. With a positive error correlation, it is possible that the incentive rate can actually increase with error correlation.

Taken together, these two propositions reveal important insights. For risk-neural providers, the random exogenous factors have no major impact. The compensation scheme is solely determined by the value-cost ratio. Thus, the independent measurement approaches followed in the industry today are well suited for larger service providers (who provide services to multiple customers and hence distribute the risk). On the other hand, for risk-averse agents, such as a smaller service provider or internal IT managers, the error correlation between performance measures can still enable the customer to impose higher risks and extract higher effort levels. Propositions 1 and 2 thus demonstrate that workflow knowledge enables the customer to better exploit the performance measure information.

<table><tr><td></td><td>AND-split</td><td>OR-join</td><td>Sequential dependency</td></tr><tr><td colspan="4">Model structure</td></tr><tr><td>Performance measures</td><td> $p_1 = g_1 a_1 + \varepsilon_{p_1}$  $p_2 = g_2 a_2 + \varepsilon_{p_2}$ </td><td> $p = g_1 a_1 + g_2 a_2 + \varepsilon_p$ </td><td> $p_1 = g_1 a_1 + \varepsilon_{p_1}$  $p_2 = g_2 (a_2 + k_{SEQ} a_1) + \varepsilon_{p_2}$ [where  $(0 < k_{SEQ} < 1)$ ]</td></tr><tr><td>Principal&#x27;s (customer organization) outcome function</td><td> $x_{\mathbb{P}} = f_1 a_1 + f_2 a_2 + \varepsilon_x$ </td><td> $x_{\mathbb{P}} = f_1 a_1 + f_2 a_2 + \varepsilon_x$ </td><td> $x_{\mathbb{P}} = f_1 a_1 + f_2 (a_2 + k_{SEQ} a_1) + \varepsilon_x$ </td></tr><tr><td>Total compensation paid to the agent (provider)</td><td> $w_{\mathbb{A}}(p) = \alpha + \beta_1 p_1 + \beta_2 p_2$ </td><td> $w_{\mathbb{A}}(p) = \alpha + \beta p$ </td><td>Scenario I:  $w_{A_I}(p) = \alpha + \beta_{2_I} p_2$ Scenario II:  $w_{A_{II}}(p) = \alpha + \beta_{1_{II}} p_1 + \beta_{2_{II}} p_2$ </td></tr><tr><td>Agent&#x27;s (provider organization) cost of service</td><td> $C_{\mathbb{A}}(a) = \frac{1}{2} (a_1^2 + a_2^2)$ </td><td> $C_{\mathbb{A}}(a) = \frac{1}{2} (a_1^2 + a_2^2) + k_{OR} a_1 a_2$  [where  $(-1 \leq k_{OR} \leq 1)$ ]</td><td> $C_{\mathbb{A}}(a) = \frac{1}{2} (a_1^2 + a_2^2)$ </td></tr><tr><td>Agent&#x27;s (provider organization) risk premium</td><td> $\frac{1}{2} r_{\mathbb{A}} (\beta_1^2 + \beta_2^2 + 2 \beta_1 \beta_2 \rho_{12})$ </td><td> $\frac{1}{2} r_{\mathbb{A}} \beta^2 \sigma_p^2$ </td><td>Scenario I:  $\frac{1}{2} r_{\mathbb{A}} \beta_{2_I}^2 \sigma_{p_1}^2$ </td></tr><tr><td colspan="4">Results</td></tr><tr><td>Optimal actions</td><td> $a_1^* = g_1 \beta_1^*, \quad a_2^* = g_2 \beta_2^*$ </td><td> $a_1^* = \frac{\beta(g_1 - g_2 k_{OR})}{1 - k_{OR}^2},$  $a_2^* = \frac{\beta(g_2 - g_1 k_{OR})}{1 - k_{OR}^2}$ </td><td>Scenario II:  $\frac{1}{2} r_{\mathbb{A}} (\beta_{1_{II}}^2 \sigma_{p_1}^2 + \beta_{2_{II}}^2 \sigma_{p_2}^2)$ Scenario I:  $a_{1_I}^* = k_{SEQ} g_2 \beta_{2_I}^*, \quad a_{2_I}^* = g_2 \beta_{2_I}^*$ Scenario II:  $a_{1_{II}}^* = g_1 \beta_{1_{II}}^* + k_{SEQ} g_2 \beta_{2_{II}}^*,$  $a_{2_{II}}^* = g_2 \beta_{2_{II}}^*$ </td></tr><tr><td>Optimal incentives</td><td> $\beta_1^* = \frac{f_1 g_1 (g_2^2 + r_{\mathbb{A}}) - \rho_{12} f_2 g_2 r_{\mathbb{A}}}{(g_1^2 (g_2^2 + r_{\mathbb{A}}) + r_{\mathbb{A}} (g_2^2 + (1 - \rho_{12}^2) r_{\mathbb{A}})}$  $\beta_2^* = \frac{f_2 g_2 (g_1^2 + r_{\mathbb{A}}) - \rho_{12} f_1 g_1 r_{\mathbb{A}}}{g_1^2 (g_2^2 + r_{\mathbb{A}}) + r_{\mathbb{A}} (g_2^2 + (1 - \rho_{12}^2) r_{\mathbb{A}})}$ </td><td> $\beta^* = \frac{f_1 g_1 + f_2 g_2 - k_{OR} (f_1 g_2 + f_2 g_1)}{(g_1 - g_2 k_{OR})^2 + (1 - k_{OR}^2)(g_2^2 + \sigma_p^2 r_{\mathbb{A}})}$ </td><td>Scenario I:  $\beta_{2_I}^* = \frac{(k_{SEQ} + (1 + k_{SEQ}^2)f_2)g_2}{(1 + k_{SEQ}^2)g_2^2 + \sigma_{p_2}^2 r_{\mathbb{A}}}$ Scenario II: $\beta_{1_{II}}^* = \frac{g_1 (k_{SEQ} \sigma_{p_2}^2 f_2 r_{\mathbb{A}} + f_1 (g_2^2 + \sigma_{p_2}^2 r_{\mathbb{A}}))}{g_1^2 (g_2^2 + \sigma_{p_2}^2 r_{\mathbb{A}}) + \sigma_{p_1}^2 r_{\mathbb{A}} ((1 + k_{SEQ}^2)g_2^2 + \sigma_{p_2}^2 r_{\mathbb{A}})}$  $\beta_{2_{II}}^* = \frac{g_2 (k_{SEQ} \sigma_{p_1}^2 f_1 r_{\mathbb{A}} + f_2 (g_1^2 + (1 + k_{SEQ}^2) \sigma_{p_1}^2 r_{\mathbb{A}}))}{g_1^2 (g_2^2 + \sigma_{p_2}^2 r_{\mathbb{A}}) + \sigma_{p_1}^2 r_{\mathbb{A}} ((1 + k_{SEQ}^2)g_2^2 + \sigma_{p_2}^2 r_{\mathbb{A}})}$ </td></tr></table>

## 3.2. OR-Join

An OR-Join interdependency arises when two workflows affect a single performance measure (as discussed in §2.3.4). Two sets of actions (workflows) are complementary when performing one action set reduces the cost of effort on the other. For example, compatibility in hardware and software platforms can reduce the amount of effort required in maintaining both platforms. On the other hand, two action sets are substitutes if performing one of them increases the cost of executing the other workflow. For example, increasing wireless connectivity requires more effort on ensuring communication security. Two actions are complementary (substitutable) when cross-partial of the agent’s cost function on actions $( \partial C _ { \mathbb { A } } / \bar { \partial } a _ { 1 } \partial a _ { 2 } )$ is negative (positive) (Dikolli et al. 2009). Accordingly, the cost function includes a multiplicative term $k _ { O R }$ $( - 1 \le k _ { O R } \le 1 )$ to denote the level of complementarity $( k _ { O R } < 0 )$ or substitutability $( k _ { O R } > 0 )$ between the two actions, as shown in Table 4.

As in the case of AND-Split, the incentive rate structure reflects a focus on risk profile and action sensitivity. The numerator of the term represents the overall performance sensitivity. The first two terms $( f _ { 1 } g _ { 1 } + f _ { 2 } g _ { 2 } )$ represent the performance sensitivity of each action, and the second term $( f _ { 2 } g _ { 1 } + f _ { 1 } g _ { 2 } )$ represents the performance sensitivity because the effect of one action on the other. However, the impact of complementary or substitutable actions on the incentive rate is dependent on other parameters. We find that performance measure congruence plays a crucial role in determining the relationship.

<sup>Proposition</sup> <sup>3.</sup> If the agent is risk neutral $( r _ { \mathbb { A } } \to 0 )$ and/or the performance measure is noiseless $( \sigma _ { p } ^ { 2 } = 0 )$ , the optimal incentive rate is the ratio of the overall performance sensitivity to the action sensitivity.

When either $r _ { \mathbb { A } } \to 0 \ o r \ \sigma _ { p } ^ { 2 } = 0$ the incentive rate reduces to

$$
\beta^ {*} = \frac {f _ {1} g _ {1} + f _ {2} g _ {2} - k _ {O R} (f _ {1} g _ {2} + f _ {2} g _ {1})}{(g _ {1} ^ {2} + g _ {2} ^ {2} - 2 k _ {O R} g _ {1} g _ {2})}.\tag{5}
$$

The incentive rate reflects the dependence between actions, and this is true even for a risk-neutral agent. The numerator represents the overall performance sensitivity. The denominator is the length of the action vector that results from the sum of the two individual action vectors. Thus, the incentive rate essentially continues to be a representation of the value-cost ratio. The comparative statics discussed under the following propositions present the performance measure congruence issues in the context of complementarity/substitutability.

<sup>Proposition</sup> <sup>4A.</sup> If agent is risk neutral $( r _ { \mathbb { A } } \to 0 )$ and/or the performance measure is noiseless $( \sigma _ { p } ^ { 2 } = 0 )$ performance measure congruence leads to a decreasing incentive rate when actions are complementary and an increasing incentive rate when actions are substitutable.

<sup>Proposition</sup> <sup>4B.</sup> If agent is risk neutral $( r _ { \mathbb { A } } \to 0 )$ and/or the performance measure is noiseless $( \sigma _ { p } ^ { 2 } = 0 ) .$ performance measure incongruence leads to an increasing incentive rate when actions are complementary and a decreasing incentive rate when actions are substitutable.

The partial derivative of $\beta ^ { * }$ with respect to $k _ { O R } i _ { i }$ s

$$
\frac {\partial \beta^ {*}}{\partial k _ {O R}} = \frac {(f _ {1} g _ {2} - f _ {2} g _ {1}) (g _ {1} ^ {2} - g _ {2} ^ {2})}{(g _ {1} ^ {2} + g _ {2} ^ {2} - 2 k _ {O R} g _ {1} g _ {2}) ^ {2}}.\tag{6}
$$

Similar to §3.1, to test for the effect of congruence, let us assume that the sensitivity factors are such that $f _ { 1 } = m g _ { \cdot }$ and $f _ { 2 } = n g _ { 2 } .$ , then

$$
\frac {\partial \beta^ {*}}{\partial k _ {O R}} = \frac {g _ {1} ^ {2} g _ {2} ^ {2} (m - n) (g _ {1} ^ {2} - g _ {2} ^ {2})}{(g _ {1} ^ {2} + g _ {2} ^ {2} - 2 k _ {O R} g _ {1} g _ {2}) ^ {2}}.\tag{7}
$$

When performance measures are congruent, Equation $( \bar { 7 } \bar { ) }$ is positive. Thus, as complementarity in actions increases, $\beta ^ { * }$ is actually decreasing. On the other hand, as substitutability in actions increases, $\beta ^ { * }$ increases as well. When performance measures are not congruent, Equation (7) is negative and the relationship reverses. Thus, as complementarity (i.e., $k _ { O R } < 0 )$ in actions increases, $\beta ^ { * }$ is increasing. On the other hand, as substitutability in actions increases, $\beta ^ { * }$ will decrease.

The change in the incentive rate is proportional to the difference $( m - n )$ between the value-cost ratio $( f / g )$ of the individual actions. That is, the greater (lower) the incongruence of the two actions, the higher (lower) is the change in the incentive rate. Hence, determining the incentive rate for a riskneutral provider is again a value-cost ratio issue as in the previous model. However, because the individual workflows are not orthogonal, they have an additive/subtractive effect (depending on the nature of the relationship between the workflows in question). The incentive rate is simply the ratio of the vector sum of the value to the vector sum of the cost.

That the variable part of the compensation is a combination of two factors (value- cost ratio and complementarity/substitutability) implies that the customer organization must know (a) the nature of workflow interrelationship, and (b) the degree by which the workflows affect one another. For instance, not only is it necessary for the customer to recognize the extent to which spam filters and antivirus software affect email security, it is also necessary for them to know the cost-benefit ratio of the individual services. This goes somewhat against the common wisdom that outsourcing an organization’s IT infrastructure reduces the need to “build” IT knowledge. The analysis here instead emphasizes the need for the customer organizations to invest in understanding the value, costs, and the structural relationships among different service processes.

## 3.3. Sequentially Dependent Actions

Sequential interdependency arises when the provider can choose the effort level required to achieve a particular performance measure by observing the actual level of another performance measure (as discussed in §2.3.5). For example, actions related to network performance may affect the level of effort on ensuring quick response of transactional systems. Similarly, network security-related actions may impact decisions and actions related to hardware and software patch updates. We introduce a variable $k _ { S E Q } ( 0 <$ $k _ { S E Q } < 1 )$ to model the effect of earlier stage actions on the next stage.

Practitioner literature often raises the issue of tradeoff between using multiple performance measures versus a few manageable ones (Taylor and Tofts 2006). Because there is a causal relationship between the two action stages, it can be argued that incentives based on observed performance level at the second stage may be sufficient. Hence, we test two scenarios using system surplus. Scenario I involves a compensation based on the last-stage performance measure only, and scenario II includes both measures toward the compensation. Compensation structures and corresponding risk premiums for both scenarios are provided in Table 4.

<sup>Proposition</sup> <sup>5.</sup> For a risk-neutral agent $( r _ { \mathbb { A } } \to 0 )$ and/or noisless performance measures $( \sigma _ { p _ { 1 } } = \sigma _ { p _ { 2 } } = 0 )$ , the incentive rate equals the ratio of the individual outcome and action sensitivities and is independent of the workflow sequence.

Figure 2 Effect of Sequential Dependency on Incentive Rates  
![](/api/attachments/NVHCWY48/fulltext/images/42822e61792b899a4007e5684dfc198149444d024188007d5cc1113ac26cdf45.jpg)

From the expression for $\beta ^ { * }$ (in both scenarios), when $r _ { \mathbb { A } } \to 0$ or $\sigma _ { p _ { 1 } } = \sigma _ { p _ { 2 } } = 0 , \beta _ { i } = f _ { i } / g _ { i } ( i = 1 , 2 )$ . Thus, independent performance measurement is again justified in the case of risk-neutral agents.

In the presence of risk and/or noise considerations, it can be easily seen that the incentive rate in the second stage, $\beta _ { 2 _ { I I } } ^ { * } ,$ is increasing in $k _ { S E Q } \ ( \partial \beta _ { 2 _ { I I } } ^ { * } / \partial k _ { S E Q } > 0 )$ However, the incentive rate for the first stage, $\beta _ { 1 _ { I I } } ^ { * } ,$ responds to changes in $k _ { S E Q } \mathrm { i n }$ a more complicated manner. We explored this relationship further by examining incentive rates for various combinations of parameter values. Figure 2 illustrates the effect of sequential coupling on $\beta _ { 1 _ { I I } } ^ { * }$ under different possible relationships between the value-cost ratios of the two services. In general, the first-stage incentive rate changes positively in response to changes in $k _ { S E Q }$ when performance measures are congruent and the first-stage value is equal to or higher than that of second stage. This results from the increasing coupling of the first-stage outcome to the second stage. Performance measure incongruence and sequential coupling prompt the customer to make complex adjustments to the incentive rates. For example, the first-stage incentive rate would actually decrease when the valuecost ratio of the first stage is higher. Likewise, the first-stage incentive rate would increase when the value-cost ratio of first stage is lower.

We now discuss the implications of using a single incentive rate as opposed to separate incentive rates for the two stages. The system surplus in each scenario is given by the sum of the expected benefit of the customer and the certainty equivalent of the provider (Gibbons 2005). Sample plots based on various combinations of parameter values are shown in Figures 2 and 3. Further details on the parameter space explored in deriving the model implications are provided in Appendix C of the online supplement.

![](/api/attachments/NVHCWY48/fulltext/images/9d77cc8429ef8e69e0bd6ce387d43c2896bcd81a6674184272c31abc2b10a157.jpg)

Figure 3 Sequential Dependency: Surplus Differences (in %): Single vs. Multiple Performance Measures  
![](/api/attachments/NVHCWY48/fulltext/images/f1d33721d857d842a9d4de460360c34054c891aba9f46e4e3d21f63f2ffbdc01.jpg)

![](/api/attachments/NVHCWY48/fulltext/images/4ce233930e92437254d4ceeb8003dda199a86a9b0ae317b40df68442c60bfaa3.jpg)

Using all available performance measures always yields higher surplus. However, the additional value obtained is dependent on performance measure noise and congruity. The effect of noise is illustrated in Figure 3 (first graph). The sample plot shows that using both performance measures becomes preferable as the second-stage noise increases (darker shades indicate lower values). However, the attractiveness of using both measures decrease if the first-stage performance measures are noisy. The effect of the coupling factor, $k _ { S E Q } ,$ is dependent on performance measure congruity (second row, Figure 3). In general, the benefit of using two performance measures progressively declines in response to increases in $k _ { S E Q }$ when performance measures are congruent. Surplus from using two measures decreases (increases) with $k _ { S E Q }$ when performance measures are incongruent and the valuecost ratio of the first stage is higher (lower). Using a single measure further distorts the performance measurement system and therefore lowers the system surplus when the value-cost ratio of the first stage is lower.

To summarize, the analysis of base primitives point to the interactions between workflow structure, risk, noise, and performance measure congruity in determining the optimal incentive rates. The major implications from our analysis are provided in Table 5. In §4,

![](/api/attachments/NVHCWY48/fulltext/images/415853376c0319f32b910b17805c3cce44db8117f6661eac5232e9c798103971.jpg)  
we further examine the implications of more complex workflow structures on incentive rates.

## 4. Combining the Basic

## Interdependency Models

The purpose of this section is to demonstrate the generalizability of the results from §3 when more complex workflow scenarios are constructed from the base primitives. We illustrate through few representative scenarios that whereas insights from the basic primitives hold when combined to form more complex service scenarios, performance measure congruity and workflow interdependence has interaction effects. In general, the component with a higher value-cost ratio has a dominant effect in determining the incentive rates and the value of using multiple performance measures.

In the following, we analyze three sample configurations—a three-stage sequential model, an ORjoin followed by sequential actions, and sequence with AND-Split followed by an AND-join. A summary of the major implications from these analyses is provided at the end of §4 in Table 7.

Our choice of sequential workflows in this section is motivated by two reasons. First, our aim is to provide a set of configurations that presents possible pairings among the three basic primitives

Table 5 Interaction of Risk, Performance Measure Congruity and Workflow on Incentive Rates

<table><tr><td></td><td>AND-split</td><td>OR-join</td><td>Sequential dependency</td></tr><tr><td>Effect of risk/noise</td><td>Incentives can be set independently when agents are risk-neutral and/or performance measures are noiselessError correlation is an important factor when performance measures are noisy</td><td>Incentives are not separable irrespective of risk-aversion and performance measure noise</td><td>Incentives can be set independently when agents are risk-neutral and/or performance measures are noiseless.Degree of sequentiality must be considered when performance measures are noisy</td></tr><tr><td>Performance measure characteristics</td><td>If the services are not impacted together by exogenous events, a single performance measure is sufficient.When the services are impacted together by exogenous events, the error correlation in performance measures determines the incentive rates.Performance measure congruity does not matter when error correlation is negative.</td><td>Congruent measures: Increasing (decreasing) complementarity (substitutability) implies lower (higher) incentives.Incongruent measures: Increasing (decreasing) complementarity (substitutability) implies higher (lower) incentives.</td><td>While using multiple measures is preferable, the value is a function of performance measure error and congruence.Congruent measures (1)  $\beta_1$  increases with increasing sequentiality (if the first-stage value-cost ratio is lower than the subsequent ones, this increase is nonmonotonic); (2) value of using multiple measures decreases with increasing sequentiality.Incongruent measures (1)  $\beta_1$  decreases (increases) with increasing sequentiality with higher (lower) value-cost ratio in the first stage; (2) value of using multiple measures decreases (increases) with higher (lower) value-cost ratio in the first stage</td></tr></table>

studied in §3. According to the process modeling framework (van der Aalst and Hee 2004), AND-Split (OR-Split) cannot be followed by an OR-Join (AND-join). So, we have chosen workflow configurations that combine an AND-Join with sequential and an OR-join with sequential. Second, and most importantly, there are quite a few IT workflows that occur in a sequential manner, and performance measures at the intermediate process steps are used in the contract. For example, resolution time, number of successful recoveries, and response time can be used in a contract, with different weights allocated to each metric. From a process perspective, recovery is a precursor to both response and resolution. Similarly, infrastructure availability precedes application availability. We therefore specifically use sequential workflows in §4 so that our examples reflect reality.

Similar to §3, the basic model structures for each of the three configurations are provided in Table 6. For the sake of brevity, solution details for all models in this section are provided in Appendix D of the online supplement. A summary of the major implications from these analyses is provided at the end of §4 in Table 7. All models are tested with two scenarios— scenario I represents the case where only the last performance measure is used for compensation, whereas scenario II includes all measures for compensation. Because scenario II always provides higher system surplus, the following discussions on the implications of risk/noise and performance measure congruity focus on this scenario. Throughout §4, only two congruent/incongruent cases are shown in the figures as exemplars. A number of other cases were also examined. All cases examined, along with associated parameter values, are provided in Appendix D of the online supplement.

Table 6 Combining Basic Workflow Interdependencies in IT Infrastructure Services: Model Structures

<table><tr><td></td><td>Sequential workflow with multiple stages</td><td>OR-join with sequential dependency</td><td>Sequence with AND-split followed by AND-join</td></tr><tr><td>Performance measures</td><td> $p_1 = g_1 a_1 + \varepsilon_{p_1}$  $p_2 = g_1 a_1 + g_2 (a_2 + k_{SEQ1} a_1) + \varepsilon_{p_2}$  $p_3 = g_3 (a_3 + a_1 k_{SEQ1}) + \varepsilon_{p_3}$ [where  $(0 < k_{SEQ1}, k_{SEQ2} < 1)]$ </td><td> $p_1 = g_1 a_1 + g_2 a_2 + \varepsilon_{p_1}$  $p_2 = g_3 (a_3 + (a_1 + a_2) k_{SEQ}) + \varepsilon_{p_2}$ [where  $0 < k_{SEQ} < 1]$ </td><td> $p_1 = g_1 a_1 + \varepsilon_{p_1}$  $p_2 = g_2 (a_2 + a_1 k_{SEQ1}) + \varepsilon_{p_2}$  $p_3 = g_3 (a_3 + k_{SEQ2} a_2 + k_{SEQ1} a_1) + \varepsilon_{p_3}$  $p_4 = g_4 (a_4 + a_1 k_{SEQ1} + (a_2 + a_3) k_{SEQ2}) + \varepsilon_{p_4}$ [where  $0 < k_{SEQ1}, k_{SEQ1} < 1]$ </td></tr><tr><td>Principal&#x27;s (customer organization) outcome function</td><td> $x_{\mathbb{P}} = f_1 a_1 + f_2 (a_2 + k_{SEQ} a_1)$  $+ f_3 (a_3 + k_{SEQ2} a_2 + k_{SEQ1} a_1) + \varepsilon_x$ </td><td> $x_{\mathbb{P}} = f_1 a_1 + f_2 a_2$  $+ f_3 (a_3 + (a_1 + a_2) k_{SEQ}) + \epsilon_x$ </td><td> $x_P = f_1 a_1 + f_2 (a_2 + a_1 k_{SEQ1}) + f_3 (a_3 + a_1 k_{SEQ1})$  $+ f_4 (a_4 + a_1 k_{SEQ1} + (a_2 + a_3) k_{SEQ2}) + \epsilon_x$ </td></tr><tr><td>Total compensation paid to the agent (provider)</td><td>Scenario I:  $w_{\mathbb{A}_I} = \alpha + \beta_{3_I} p_3$ Scenario II:  $w_{\mathbb{A}_{II}} = \alpha + \beta_{1_{II}} p_1$  $+ \beta_{2_{II}} p_2 + \beta_{3_{II}} p_3$ </td><td> $w_{\mathbb{A}_I} = \alpha + \beta_{2_I} p_2$  $w_{\mathbb{A}_{II}} = \alpha + \beta_{1_{II}} p_1 + \beta_{2_{II}} p_2$ </td><td> $w_{\mathbb{A}_I} = \alpha + \beta_{4_I} p_4$  $w_{\mathbb{A}_{II}} = \alpha + \sum_{i=1}^{4} \beta_{i_{II}} p_i$ </td></tr><tr><td>Agent&#x27;s (provider organization) cost of service</td><td> $C_{\mathbb{A}}(a) = \frac{1}{2}(a_1^2 + a_2^2 + a_3^2)$ </td><td> $C_{\mathbb{A}}(a) = \frac{1}{2}(a_1^2 + a_2^2 + a_3^2) + a_1 a_2 k_{OR}$ [where  $k_{OR} (-1 < k_{OR} < 1)$ ]</td><td> $C_{\mathbb{A}}(a) = \frac{1}{2}(a_1^2 + a_2^2 + a_3^2 + a_4^2)$ </td></tr><tr><td>Agent&#x27;s (provider organization) risk premium</td><td>Scenario I:  $\frac{1}{2} r_{\mathbb{A}} \sigma_{p_3}^2 \beta_{3_{II}}^2$ Scenario II:  $\frac{1}{2} r_{\mathbb{A}} (\sigma_{p_1}^2 \beta_{1_{II}}^2 + \sigma_{p_2}^2 \beta_{2_{II}}^2 + \sigma_{p_3}^2 \beta_{3_{II}}^2)$ </td><td> $\frac{1}{2} r_{\mathbb{A}} \sigma_{p_2}^2 \beta_{2_{II}}^2$  $\frac{1}{2} r_{\mathbb{A}} (\sigma_{p_1}^2 \beta_{1_{II}}^2 + \sigma_{p_2}^2 \beta_{2_{II}}^2)$ </td><td> $\frac{1}{2} r_{\mathbb{A}} \sigma_{p_4}^2 \beta_{4_{II}}^2$  $\frac{1}{2} r_{\mathbb{A}} (\sigma_{p_1}^2 \beta_{1_{II}}^2 + \sigma_{p_2}^2 \beta_{2_{II}}^2 + \sigma_{p_3}^2 \beta_{3_{II}}^2 + \sigma_{p_4}^2 \beta_{4_{II}}^2 + 2 \sigma_{p_2} \sigma_{p_3} \beta_{2_{II}} \beta_{3_{II}} p_{23})$ </td></tr></table>

Table 7 Summary of Multistage Workflow Model Results

<table><tr><td></td><td>Sequential: Multiple stages</td><td>OR-sequential</td><td>AND-sequential</td></tr><tr><td>Effect of risk/noise</td><td>Same as base model (sequential dependency)</td><td>Same as base model (OR-join dominant)</td><td>Same as base model (sequential dependency and AND-split)</td></tr><tr><td>Congruent performance measures</td><td>(1) Incentive rates are more sensitive to first stage.(2) Value of using multiple measures decreases with increasing sequentiality.</td><td>(1) Increasing (decreasing) complementarity in the first stage (substitutability) implies lower (higher) incentives.(2) Value of using multiple measures decreases (increases) with increasing (decreasing) sequentiality and complementarity.</td><td>(1) Incentive rates are more sensitive to first stage.(2) Value of using multiple measures decreases with increasing sequentiality and positive error correlation.</td></tr><tr><td>Incongruent performance measures</td><td>(1) Incentive rates are more sensitive to the stage with higher value-cost ratio.(2) Value of using multiple measures show nonmonotonic relationship and are more sensitive to the stage with higher value-cost ratio.</td><td>(1) First-stage incentive rates are more sensitive to the stage with higher value-cost ratio.(2) Value of using multiple measures decreases (increases) with increasing (decreasing) sequentiality and complementarity.</td><td>(1) Incentive rates are more sensitive to the stage with higher value-cost ratio.(2) Value of using multiple measures decreases with increasing sequentiality and positive error correlation (but are more sensitive to the stage with higher value-cost ratio).</td></tr></table>

## 4.1. Sequential Workflow with Multiple Stages

This scenario involves two consecutive sequential dependencies and three performance measures. For example, the overall security of the network may determine the level of effort required for applying hardware and/or software patches, which in turn may determine the level of effort required for maintaining desktop antivirus software (see Figure 4). The variable $\bar { k _ { S E Q 1 } } ( 0 < k _ { S E Q 1 } < 1 )$ denotes the effect of network security management $( a _ { 1 } )$ on all subsequent performance measures and $k _ { S E Q 2 } ( 0 < k _ { S E Q 2 } < 1 )$ denotes the effect of patch management $\left( a _ { 2 } \right)$ on the final performance measure (see Table 6 for model details). Similar to $\ S 3 ,$ we first test the effect of risk neutrality/noise in performance measures on the incentive rates, followed by a discussion of performance measure congruity.

Figure 4 Sequential Workflow with Multiple Stages  
![](/api/attachments/NVHCWY48/fulltext/images/086581102589ccedc792142a9d3c95054a1859e020a1f6b7c0ad3d62f20fd5ed.jpg)

4.1.1. Effect of Risk/Noise in Performance Measure. Consistent with Proposition 5, if the provider is risk neutral $( r _ { \mathbb { A } } \to 0 )$ and/or the performance measures are noiseless $( \sigma _ { p _ { i } } = 0 , i = 1 { - } 3 )$ , the incentive rates continue to be equal to the ratio of the individual outcome and action sensitivities (i.e., $\beta _ { i } = f _ { i } / g _ { i } , i =$ 1–3), and are independent of the workflow sequence. This demonstrates that more complex workflows do not necessarily add additional complexities for performance measurement in risk-neutral provider settings.

4.1.2. Effect of Performance Measure Congruity. The sample contour plots in Figure 5 and Figure 6 illustrate the effect of performance measure congruity on the system surplus and incentive rates, respectively. Although the main findings from §3 hold, the relative value-cost ratio of the stages plays a significant role in determining whether $k _ { S E Q 1 } ~ o r ~ k _ { S E Q 2 }$ has the dominant effect, especially when measures are incongruent.

The relative value-cost ratio of the stages (see Figure 5) determines the attractiveness of using multiple measures over a single measure. As observed in the base case, when performance measures are congruent (e.g., first graph in Figure 5) increasing sequentiality usually decreases the value of using multiple performance measures. However, performance measure

(Incongruent performance measures)

Figure 5 Multistage Sequential Coupling: Surplus Differences (in %) Between Single vs. Multiple Performance Measure Scenarios  
![](/api/attachments/NVHCWY48/fulltext/images/30eda608018d1aafbf7fc0fc17ee8435d40cb7e1890fb6843a44790bbb0e552b.jpg)

![](/api/attachments/NVHCWY48/fulltext/images/d1a427fb644d05456447edb4636b5484103aca557598482083bcf391ad8fa178.jpg)

Figure 6 Effect of Multistage Sequential Coupling on Incentive Rates  
![](/api/attachments/NVHCWY48/fulltext/images/28b1a82bbbc1c850ca65595e9778f8846c2a39b58972f989bd380bc045f87dc3.jpg)

incongruity has a nonmonotonic impact on the surplus (e.g., second graph in Figure 5). The surplus difference is more sensitive to the stage with a higher value-cost ratio (e.g., second graph in Figure 5 is more sensitive to $k _ { S E Q 2 }$ because the value-cost ratio of the second stage is higher than that of the first stage).

When performance measures are congruent, incentive rates are highly sensitive to the first-stage sequential coupling factor (e.g., first row of Figure 6). This is consistent with the surplus relationships discussed above because higher sequential coupling requires the customer and provider organizations to focus on the early stage performance. On the other hand, when performance measures are incongruent (e.g., second row of Figure 6) incentive rates (especially $\beta _ { 2 }$ and $\beta _ { 3 } )$ are more sensitive to the latter-stage sequential coupling factors, as the second stage in this case has a higher value-cost ratio.

## 4.2. OR-Join Followed by Sequential Actions

We now analyze a scenario that combines a complementary/substitute action stage followed by an action associated with a second performance measure. As shown in the example in Figure 7, there are now two performance measures and three actions. The variable $k _ { S E Q } ( 0 < k _ { S E Q } < 1 )$ 5 denotes the sequential impact of network hardware and software on transactional systems, and $k _ { O R } ( - 1 < k _ { O R } < 1 )$ is the complementarity/substitutability factor between hardware and software maintenance workflows (see Table 6 for model details). System surplus and incentive rate implications for a variety of congruent and incongruent cases are discussed below.

4.2.1. Effect of Risk/Noise in Performance Measure. When the provider is risk neutral $( r _ { \mathbb { A } } \to 0 )$ and/or the performance measures are noiseless $( \sigma _ { p _ { 1 } } =$ $\sigma _ { p _ { 2 } } = 0 )$ , optimal incentive rates are not separable in terms of the two constituent stages. This is consistent with Proposition 3. In essence, the OR-Join effect is salient, and incentive rates reflect complementarity/ substitutability effects.

Figure 7 OR-Join with Sequential Dependenc  
![](/api/attachments/NVHCWY48/fulltext/images/8035cfd0805ea7b5ce8b63a25729f07bb3722c5d407aba142249257d609a5f9c.jpg)

Figure 8 OR-Join and Sequential Coupling: Surplus Differences (in %) Between Single vs. Multiple Performance Measure Scenarios (All Congruent and Incongruent Cases)  
![](/api/attachments/NVHCWY48/fulltext/images/d0c0be80fc89e427ff636990625873bfc30f54726fbe63032c78b0983e1d8019.jpg)  
4.2.2. Effect of Performance-Measure Congruity. The sample contour plot in Figure 8 shows the difference in surplus between scenarios I and II for different degrees of sequential coupling $( k _ { S E Q } )$ and complementarity/substitutability $( k _ { O R } )$ . As before, the benefit of using multiple measures reduces as the sequential effect, $k _ { S E Q } ,$ increases. The surplus difference is nonmonotonic in response to $k _ { O R }$ . However, as shown in the sample plot, the nonmonotonic relationship holds over a very narrow range. In essence, at very high levels of complementarity in actions, it is beneficial for the customer to consider a single measure. However, as complementarity decreases it is beneficial to use multiple measures. The effect on the surplus is the same for both congruent and incongruent measures.

Incentive rates for two representative cases are illustrated in Figure 9, one with congruent performance measures, and the other with incongruent. Consistent with the basic sequential model, secondstage incentive rate $( \beta _ { 2 } )$ always increases with an increase in sequential coupling $( k _ { S E Q } )$

Performance measure congruence (row 1, Figure 9) causes incentive impacts to be more dependent on factors specific to the individual stages. Thus, the first-stage incentive rate is more sensitive to the complementarity/substitutability factor (in the same way as predicted by Proposition 4), and the second-stage incentive rate is more sensitive to the sequential coupling factor. On the other hand, for incongruent measures (row 2, Figure 9), the first-stage incentive rate becomes sensitive to the second-stage coupling

(Incongruent performance measures)

Figure 9 Effect of OR-Join and Sequential Coupling on Incentive Rates  
![](/api/attachments/NVHCWY48/fulltext/images/cacb93a667d9b672f0f6f8350a3e781cb79fa5049b9f61e6523a2e87cf1f18c1.jpg)

factor $( k _ { S E Q } )$ as the latter stage has a higher valuecost ratio. Consistent with the basic sequential model, $\beta _ { 1 }$ increases with increasing sequentiality because the value-cost ratio is lower in the first stage. Therefore, individual effects of OR-join and sequentiality can be combined to determine the direction of the optimal incentives based on the relative value-cost ratio of the stages.

## 4.3. Sequence with AND-Split Followed by AND-join

Consider a scenario where application service performance is dependent on both database performance and application server performance (AND-Join at $a _ { 4 } )$ (see Figure 10). Database server performance and application service performance may in turn be dependent on network infrastructure performance $\left( { p _ { 1 } } \right)$ . Because the activities related to network infrastructure management are followed by an AND-Split to activities required for database server administration $\left( a _ { 2 } \right)$ and application server administration $\left( a _ { 3 } \right)$ , there is a sequential effect of $a _ { 1 }$ on both $a _ { 2 }$ and ${ a } _ { 3 } ,$ denoted by the variable $k _ { S E Q 1 }$ Similarly, $k _ { S E Q 2 }$ denotes the effect of both database and application server maintenance $( a _ { 2 }$ and ${ a } _ { 3 } )$ on the final measure— application performance. Additionally, problems in network infrastructure will affect both database and application server performance; therefore, random deviations in measures $p _ { 2 }$ and $p _ { 3 } \mathrm { a r e }$ correlated (see Table 6 for model details).

4.3.1. Effect of Risk/Noise in Performance Measure. Consistent with Propositions 1 and 5, we first

Figure 10 Sequence with AND-Split Followed by AND-Join  
![](/api/attachments/NVHCWY48/fulltext/images/98a6c18b156659d367938b7f97057688651b0783f6f64c1010b718353d0e645b.jpg)  
observe that when agent is risk neutral $( r _ { \mathbb { A } } \to 0 )$ and/or performance measures are noiseless $( \sigma _ { i } = 0 .$ $i = 1 { - } 4 )$ , individual services can be measured separately, i.e., $\beta _ { i } ^ { * } = f _ { i } / g _ { i } ~ ( i = 1 { - } 4 )$

4.3.2. Effect of Performance Measure Congruity. The sample plots in Figure 11 show the difference in the surplus between scenarios I and II for different degrees of sequential coupling $( k _ { S E Q 1 } , k _ { S E Q 2 } )$ and error correlation $\left( \rho _ { 2 3 } \right)$ . The surplus difference pattern is similar to that of all the previous cases. Higher levels of sequentiality reduce the need for multiple performance measures, and the impact of sequentiality on surplus is a function of the relative value-cost ratio of the performance measures in the two stages. Also, increasing positive (negative) error correlation reduces (increases) the benefit of using multiple performance measures.

Consistent with the findings from §§4.1 and 4.2, the value-cost ratio and workflow structure interact in determining the incentive rates in the presence of risk considerations and/or noise. When performance measures are congruent, incentive rates are more sensitive to the first-stage sequential coupling factor (e.g., row 1, Figure 12). On the other hand, when performance measures are incongruent (e.g., row 2, Figure 12), incentive rates (especially $\beta _ { 2 } , \ \beta _ { 3 } ,$ , and $\beta _ { 4 , \cdot } )$ become more sensitive to the latter-stage sequential coupling factor $( k _ { S E Q 2 } )$ , as the second stage has a higher value-cost ratio compared to the first.

Overall, sequential coupling in latter stages has less impact on early stage incentives when measures are congruent. With incongruent measures, the effect of the stage with higher value-cost ratio dominates. A summary of the implications from the models in §4 is provided in Table 7.

## 5. Discussion and Conclusion

A key insight obtained from our models is that in the absence of risk considerations, IT infrastructure services can be measured and rewarded separately (i.e., the effect of other related services can be ignored) in most cases. This result holds for all base service configurations and combinations thereof, except when underlying workflows in the service are complementary/substitutable. With risk-averse providers, incentive design has to take into consideration the workflow interaction and the relative value-cost ratio of the individual services. We show that optimal incentives in these cases do not have a simple interpretation. For example, when services have sequential dependency (e.g., network and transaction processing systems), higher levels of coupling between the services does not necessarily mean that incentives for both services should increase, and asymmetries in the value-cost ratio cause incentives for some services to move in opposite directions.

Our research sheds insights on the debate among practitioners on whether inclusion of multiple performance measures is beneficial or detrimental to the outsourcing relationship. We show that using all observable measures in the compensation scheme is generally beneficial. However, the attractiveness of using multiple measures is a function of measurement noise, strength of sequential coupling, and/or presence of complementarity/substitutability in the workflow. Attractiveness of using multiple incentives can increase or decrease because of changes in sequential coupling intensity when measures are incongruent. Moreover, value-cost ratio is a significant determinant of the benefits.

A major implication of this research is that the “death by a thousand $\mathrm { S L A s ^ { \prime \prime } }$ (Taylor and Tofts 2006, p. 1) cannot always be considered a universal truth. In general, IT service environments (especially infrastructure services) are quite rich in data. Many data f<sub>1</sub> = (½) f<sub>2</sub> = (½) f<sub>3</sub> = f<sub>4</sub>, g<sub>1</sub> = (½)g<sub>2</sub> =(½) g<sub>3</sub> = g<sub>4</sub> (Congruent performance measures)

Figure 11 Sequential Coupling and Error Correlation: Surplus Differences (in %) Between Single vs. Multiple Performance Measure Scenarios  
![](/api/attachments/NVHCWY48/fulltext/images/8b8cbf79320e46e106fd1843e74d9cd682a2de48b3388e737fd0f10e507d24cf.jpg)

![](/api/attachments/NVHCWY48/fulltext/images/abf254d08da7ae8fcc57ed794ee15325ad029b33cdfa410f0394951cfff35a6f.jpg)  
f<sub>1</sub> = (½) f<sub>2</sub> = (½) f<sub>3</sub> = f<sub>4</sub>, g<sub>1</sub> = 2g<sub>2</sub> = 2g<sub>3</sub> = g<sub>4</sub>  
(Incongruent performance measures)

points can be generated as a by-product of the service itself. For example, help-desk responsiveness can be easily calculated from trouble-ticket logs. Our results make the case for organization-wide collection and compilation of performance data, especially for services that are of high value for downstream services. Overall, our research confirms that even if services are outsourced to an external provider, active involvement and domain knowledge at the customer side is important in achieving success (Doucette and Wood 2003, Rottman and Lacity 2006).

For proper interpretation of the results in this research, certain limitations of our work should also be noted. First, we assume that the contract is for a single period where a sole provider provides multiple infrastructure services. This is done mainly for model simplicity and analytical tractability (analyzing multiagent contexts with resource allocation decisions require a computational setting as in Raghu et al. (2004). The results in this research are an important step in further exploring the implications of service interdependence in multiagent contexts. Second, in keeping with agency theory, the service provider is assumed to be risk averse. Literature has suggested that, in the absence of relational governance (Poppo and Zenger 2002), vendor opportunism may result in risk-taking behavior (Poppo et al. 2008). Although we do not include analytical models capturing risktaking agents, it can be shown that the higher the risktaking propensity, the greater is the variable part of the compensation. In other words, the customer can shift more risk to the provider. However, more research is needed to understand the precise implications of relational interdependencies in multiperiod settings. The linear relationship assumption between performance and effort is also a limitation of our model. Although the approach enables examination of the strategic effort allocations made by the agent, it may not fully account for performance sensitivity effects and associated resource allocation decisions by the agent. In simpler settings, it can be analytically shown that, when a performance metric is more responsive to agent actions, the optimal incentive rate can be lower than that in the linear case. Further, the incentive rate needs to be higher when performance function becomes less sensitive to agent action levels. Jointly examining the effects of nonlinearity and resource allocation in a multitask context would require the use of computational models because of model intractability (Raghu et al. 2004). Finally, although understanding the effect of interdependency is crucial for designing appropriate incentives, highly granular analysis of all service workflows and their related performance measures would not be practical. Given that process modeling approaches can easily accommodate decomposition, organizations should at least choose to base their analysis at a reasonable level of granularity for incentive purposes.

Figure 12 Effect of Sequential Coupling on Incentive Rates  
![](/api/attachments/NVHCWY48/fulltext/images/3bf9c78bdfbf767ca4b640fd51ead0170a24ea5e1564ffc18c138f0ef98e4447.jpg)  
(Incongruent performance measures)

This research can be extended in many ways. The present context focuses on a one-to-one relationship between a customer and provider organizations. There are, however, instances where different types of infrastructure services are being provided by separate providers—e.g., network services by one and application services by another. The issue of multiple SLAs under multiple independent contracts (i.e., with multiple service providers) adds an additional level of complexity to the problem of interdependent performance measures in IT services. In such a scenario, multiple agency issues need to be addressed. Subsequently, an interesting extension may be in the direction of handling interdependency and incentive design among multiple participants. Additionally, we have not explicitly addressed distinct types of workflow events (e.g., planned deterministic, planned stochastic, or unanticipated). Incentive implications and performance sensitivity can be very different for each type of workflow event. Future research can explore the incentive implications by explicitly modeling the task types.

## Acknowledgments

The authors sincerely thank Dr. Ajay Vinze for his insights and thoughtful comments in various phases of this research. The authors thank the senior editor, associate editor, and three anonymous reviewers for providing insightful comments throughout the review process.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2013.0475.

## References

Banker R, Datar S (1989) Sensitivity, precision, and linear aggregation of signals for performance evaluation. J. Accounting Res. 27(1):21–39.

Basu A, Blanning RW (2000) A formal approach to workflow analysis. Inform. Systems Res. 11(1):17–36.

Cheon MJ, Grover V, Teng JTC (1995) Theoretical perspectives on the outsourcing of information systems. J. Inform. Tech. 10(4):209–219.

Christensen PO, Feltham GA, Sabac F (2003) Dynamic incentives and responsibility accounting: A comment. J. Accounting Econom. 35(3):423–436.

Coase RH (1937) The nature of the firm. Economica 4(16):386–405.

Combs JG, Ketchen DJ (1999) Explaining interfirm cooperation and performance: Toward a reconciliation of predictions from the resource-based view and organizational economics. Strategic Management J. 20(9):867–888.

Datar S, Kulp SC, Lambert RA (2001) Balancing performance measures. J. Accounting Res. 39(1):75–92.

Deloitte Consulting (2005) Calling a change in the outsourcing market: The realities for the world’s largest organizations. Research study (April), http://www.deloitte.com/assets/Dcom -Luxembourg/Local%20Assets/Documents/Global\_brochures/ us\_outsourcing\_callingachange.pdf.

Dey D, Fan M, Zhang C (2010) Design and analysis of contracts for software outsourcing. Inform. Systems Res. 21(1):93–114.

Dikolli SS, Hofmann C, Kulp SL (2009) Interrelated performance measures, interactive effort, and incentive weights. J. Management Accounting Res. 21(1):125–149.

Doucette J, Wood D (2003) Ten secrets to offschore outsourcing success. CIO Magazine (June 1), http://cio.com/article/31929/ Ten\_Secrets\_to\_Offshore\_Outsourcing\_Success\_.

Feldman J (2010) Informed CIO: Cloud contracts and SLAs. InformationWeek Reports (February 11), http://reports.informationweek .com/abstract/83/2274/IT-Business-Strategy/informed-cio -cloud-contracts-and-slas.html.

Feltham GA, Xie J (1994) Performance measure congruity and diversity in multi-task principal/agent relations. The Accounting Rev. 69(3):429–453.

Fitoussi D, Gurbaxani V (2012) IT outsourcing contracts and performance measurement. Inform. Systems Res. 23(1):129–143.

Gibbons R (2005) Incentives between firms (and within). Management Sci. 51(1):2–17.

Grossman SJ, Hart OD (1986) The costs and benefits of ownership: A theory of vertical and lateral integration. J. Political Econom. 94(4):691–719.

Holmstrom B, Milgrom P (1991) Multitask principal agent analyses—incentive contracts, asset ownership, and job design. J. Law Econom. Organ. 7(Sp. Issue):24–52.

Jensen MC, Meckling WH (1976) Theory of the firm: Managerial behavior, agency costs and ownership structure. J. Financial Econom. 3(4):305–360.

Kumar A, Zhao JL (1999) Dynamic routing and operational controls in workflow management systems. Management Sci. 45(2):253–272.

McIvor R, Humphreys PK, Wall AP, Mckittrick A (2009) A study of performance measurement in the outsourcing decision. CIMA Research Executive Summary Series 4(3), http://www.cimaglobal.com/Documents/Thought\_leadership \_docs/cid\_ressum\_a\_study\_of\_performance\_mesurement\_in \_the\_outsourcing\_decision\_dec08.pdf.

Poppo L, Zenger T (2002) Do formal contracts and relational governance function as substitutes or complements? Strategic Management J. 23(8):707–725.

Poppo L, Zhou KZ, Ryu S (2008) Alternative origins to interorganizational trust: An interdependence perspective on the shadow of the past and the shadow of the future. Organ. Sci. 19(1):39–55.

Raghu TS, Jayaraman B, Rao HR (2004) Toward an integration of agent- and activity-centric approaches in organizational process modeling: Incorporating incentive mechanisms. Inform. Systems Res. 15(4):316–335.

Ross JW, Westerman G (2004) Preparing for utility computing: The role of it architecture and relationship management. IBM Systems J. 43(1):5–19.

Rottman JW, Lacity MC (2006) Proven practices for effectively offshoring IT work. MIT Sloan Management Rev. 47(3):56–63.

Susarla A, Barua A, Whinston AB (2010) Multitask agency, modular architecture, and task disaggregation in SaaS. J. Management Inform. Systems 26(10):87–117.

Taylor R, Tofts C (2006) Death by a thousand SLAs: A short study of commercial suicide pacts. Technical Report HPL-2005- 11R1, http://www.hpl.hp.com/techreports/2005/HPL-2005- 11R1.html (HP Labs, Bristol, UK).

TDWI (2009) Performance management strategies: How to create and deploy effective metrics. Best practices report (First quarter), http://tdwi.org/research/2009/01/bpr-1q-performance -management-strategies.aspx (TDWI, Renton, WA).

Thompson JD (1967) Organisations in Action: Social Science Bases of Administrative Theory (McGraw-Hill, New York).

van der Aalst W, Hee Kv (2004) Workflow Management: Models, Methods, and Systems (The MIT Press, Cambridge, MA).
