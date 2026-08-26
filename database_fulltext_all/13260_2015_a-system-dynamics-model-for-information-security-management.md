---
otero_id: 13260
otero_key: "9NN32Y3F"
title: "A system dynamics model for information security management"
authors: "Derek L. Nazareth; Jae Choi"
year: "2015"
journal: "Information & Management"
doi: "10.1016/j.im.2014.10.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: A System Dynamics Model for Information Security Management

Author: Derek L. Nazareth Jae Choi

![](/api/attachments/9NN32Y3F/fulltext/images/5481eb5896d02397777d3807842978f4aafe293d4e5a055e6d2083a50a3dc7fb.jpg)

PII: S0378-7206(14)00133-5

DOI: http://dx.doi.org/doi:10.1016/j.im.2014.10.009

Reference: INFMAN 2768

To appear in: INFMAN

Received date: 13-2-2013

Revised date: 15-8-2014

Accepted date: 24-10-2014

Please cite this article as: D.L. Nazareth, J. Choi, A System Dynamics Model for Information Security Management, Information and Management (2014), http://dx.doi.org/10.1016/j.im.2014.10.009

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

## Highlights

• We present a system dynamics model for information security management

• We examine the effect of investment in deterrence and security tools

• Increased investment in security tools reduces overall security cost substantially

• Deterrence investment has a less pronounced effect on overall security cost

• Uniform security investments are not the most effective

# A System Dynamics Model for Information Security Management

Derek L. Nazareth

Lubar School of Business

University of Wisconsin-Milwaukee

P.O. Box 742

Milwaukee, WI 53201, USA.

(414) 229-6822

derek@uwm.edu

Jae Choi

Kelce College of Business

Pittsburg State University

223 Kelce Center

Pittsburg, KS 66762, USA

(620) 235-4541

jchoi@pittstate.edu

Corresponding Author:

Derek L. Nazareth

# A System Dynamics Model for Information Security Management

## Abstract

Managing security for information assets is a critically important and challenging task. As organizations provide clients with ubiquitous access to information systems, and the frequency and sophistication of security threats grows, the need to provide security assumes greater importance. Effective information security management requires security resources be deployed on multiple fronts, including attack prevention, vulnerability reduction, and threat deterrence. Using a system dynamics model, this research evaluates alternative security management strategies through an investment and security cost lens, to provide managers guidance for security decisions. Results suggest that investment in security detection tools has a higher payoff than deterrence investment.

Keywords

information security management; security investment decisions; simulation; system dynamics

## 1. Introduction

Information security remains a key issue in the IT industry, as indicated by recent surveys [1]. Security incidents continue to increase in frequency and sophistication [2]. As consumers push for greater access to data and applications in an increasingly connected world, the opportunities for security breaches will only increase. Part of this growing awareness is reflected in the inclusion of securityrelated sections in IT publications and the emergence of several new publications devoted to IT security. While most organizations have taken a number of steps to shore up information security, it is suggested that security investments are typically a response to perceived and materialized threats, rather than a more rigorous analysis of the effectiveness of solutions in combating the threats [3]. Applying a cost-benefit approach to the problem is often not effective, since many models tend not to incorporate qualitative or nonfinancial criteria, which comprise a significant aspect of information security [4].

Information security managers are tasked with a variety of functions, including security planning, policy formation, staffing, risk management, security technology selection, threat assessment, countermeasure implementation, performance monitoring, and maintenance, among others [5]. Selecting countermeasures to security threats remains one of the more pressing issues that needs attention on a continual basis. Given that a wide variety of security threats are present, managers can elect to counter them with several strategies, including detection, deterrence, vulnerability reduction, education and training, among others. Clearly, a portfolio of strategies is needed, rather than adoption of a single solution approach. many of which are hard to quantify. The business value derived from information security investment, though undeniable, may be hard to estimate, given the uncertainties of threat manifestation, extent of damage incurred, ability to recover from successful attacks, ripple effects to other parts of the business affected by a successful attack, loss of reputation, and so on. Many factors affect these assessments, including innate vulnerabilities, perceived attractiveness of targets (both organization and individual application), the number and sophistication of attackers, availability of attack tools and vectors, extent and nature of backup facilities, among others.

Clearly, assembling an accurate business case can prove challenging. Information security managers need to select security strategies on a periodic basis nonetheless. In the absence of adequate tools to support these decisions, managers are left to speculate if the decisions made were appropriate for the task. A model that captures the complexities of the security decision while permitting systematic exploration of alternative security decisions would be an invaluable aid to managers. Using the design science research methodology [6], this paper develops a model that allows information security managers to examine the effects of alternative security decisions on the organization’s information assets. Given the need to capture the dynamic and fluid nature of the problem, and coupled with the need to revisit the decision on a periodic basis, system dynamics is chosen as the modeling environment. The model simulates the security decisions over a thirty month horizon, and can be adapted and calibrated for different organization contexts.

The rest of the paper is organized as follows. A review of the extant information security literature pertaining to simulating security decisions serves as the foundation for building the model of information security management, and is presented in the next section. A dynamic model of the mechanics underlying the impact of security attacks and their implications is assembled and presented thereafter. The model is used to examine the implications of alternative security investment strategies in a variety of scenarios. Research and managerial implications of the simulations are discussed. Limitations and future extensions round out the paper.

## 2. Review of Relevant Literature

Security in the information systems discipline represents an area of interest for quite a while, with studies appearing in mainstream IS journals in the early nineties [7], [8]. Several aspects of security have been studied including internal abuse [9], [10], [11], external attacks [12], [13], acceptable use policies [14], [15], [16], [17] , computer crime [18], [19], and password security [20], [21], among others. Research in the field is clearly growing – a survey identified 240 security-related articles published in 10 leading IS journals in the period 2000-2007 [22]. Much of the research is directed at individual behavior, and spans topics ranging from Internet abuse [23], compliance with organization norms, ethical practice regarding computers, and the effect of deterrence on user behavior [24]. Studies at the organizational level are comparatively fewer, and are declining in frequency. Some studies describe the adoption of security technology and practice [25], while others address the difficulties in adopting security standards [26], and relying on traditional methods [27]. The relative paucity of firm level research may reflect the reluctance of organizations to reveal information about their security procedures and breaches, and hence elect to not participate in security studies [28]. Even the latest security study, which sur ys securit personnel, has indicated a drop in the number of responses and the response rate when compared to prior studies [1].

A number of meta-analyses of research in information security have emerged [7], [29], [27], [30], calling for a more holistic approach to addressing information security issues. Several areas for security research are identified, including the need for models to gain a better understanding of information security. Several different types of models exist in the information security discipline. These include formal models for access, economic models for security, and simulation models for gaining insight into the dynamics of information security. These models are briefly reviewed.

## 2.1 Models for Information Security Access

Formal models for information security have been proposed quite a while ago [31]. They are usually grounded in military computing and typically seek to formalize the basis for protecting information and network assets through access and usage patterns. Among the early models of access was the Bell-LaPadula model [32] which sought to maintain the confidentiality of information through controlled access by assigning people and assets distinct security levels. A slightly different set of security principles was adopted in the Biba model [33], which focused more on data integrity, through restriction of content accessible and updatable. Formal models to access programs and other objects at the operating system level were addressed in [34]. In this extension of prior work, the ability to add and delete new assets and people, as well as alter current authorizations is considered from a security

Information Security Management using System Dynamics

perspective. Adaptation of previous models for military computing security to corporate applications, and rules to govern security were proposed in the Clark-Wilson model [35]. This approach expands the set of rules to deal with a more varied set of business transactions. A related problem involving restriction of information where conflict of interest and insider information issues arise was addressed through the Chinese Wall model [36]. The approach was initially designed for investment banking scenarios, though it has been used in legal firms in addition. While these models are effective at formalizing and enforcing policy at an asset and person level, they are of limited utility at the firm level. In an increasingly connected world, information security managers need to focus more on threats and countermeasures at the entire computing infrastructure level, rather than an individual asset level.

## 2.2 Economic Models of Information Security

Economists have examined the interplay between economics and security for a considerable period. However, the emphasis on the economic aspects of information system security has gained more attention only recently. Several streams of research are identifiable. One stream is devoted to economic modeling of security investments using a net present value approach. Research in this area examines the effectiveness of optimal expenditure levels [37], risk management [38], and the rate at which certain types of attacks bypass the existing security mechanisms and cause damage [39]. A different stream uses classic economic analysis, adopting the utility maximization principle to derive optimal investment levels of a firm under a limited number of constraining conditions [40], [41], [42]. A variant examines the use of financial options to examine the effect of deferred security investment on security breaches [43]. Yet other approaches utilize the principle of equating marginal financial benefits of information security to the marginal financial costs of such security [44]. A survey of economic models of information security is presented in [45], where models are classified based on whether they address vulnerabilities, privacy, security mechanisms, and incentives and deterrence.

Economic models of information security generally adopt a quantitative approach. However, security goes beyond that and typically includes qualitative and non-functional aspects. In an effort to include these, some researchers have employed the analytic hierarchy process to combine quantitative and qualitative criteria [4]. These studies often adopt a static view of the information security problem. In actuality, information security is a complex system that embodies many closely coupled variables. It involves people, organizational factors, technology, tasks, and the working environment [46]. In addition, the security management system often involves multiple controls, including technical controls, formal controls, and informal controls [47]. These call for a more dynamic approach to modeling information security.

## 2.3 Dynamic Models of Information Security

While formal models of security provide guidelines for security policy development, and economic models provide guidance for investment in security, any attempt to manage resources so as to improve information security must entail an understanding of the dynamic aspects of security threats, countermeasures, and effort to prevent and recover from attacks. Multiple diverse factors and many dynamic relationships come into play, and need to be investigated. The dynamic aspects of information security can be studied through queueing theory and simulation. The former offers closed form solutions but is difficult to apply for large and complex systems. In addition, the restrictive assumptions of queueing theory may not permit accurate modeling of the real world phenomenon. Simulation offers the advantage of closer approximation of the real world, and the ability to observe a number of alternative scenarios. Several simulations options are available for understanding the dynamic aspects of information security, including discrete event simulation, continuous simulation, system dynamics, and agent-based simulation, among others. Discrete event simulation models the phenomenon at the individual transaction level. For the information security case, it could model individual attacks, and provides security managers with the ability to examine the efficacy of different security strategies under a variety of attack vectors and frequencies within a specified period. Continuous simulation deals with dynamic systems that are amenable to description via differential equations. This is not applicable to information security management given the discrete nature of security attacks. Agent-based simulations are useful in contexts of independent decision-making entities that cooperate to accomplish an overall objective. It can also be employed to simulate competing agents, making it a viable option for information security modeling. Agent-based simulations have been employed to study public security [48], but comparatively fewer applications to information security are available, with applications to database security [49], [50], and information warfare [51]. System dynamics uses a combination of first order linear and non-linear difference equations to relate qualitative and quantitative factors within and across time periods [52] and is based on principles developed by Forrester to study managerial and dynamic decisions using control principles [53]. Given the range of factors involved in information security, and the complex dynamics among these factors, it has been suggested that system dynamics and agent-based simulation represent the most promising methodologies for creating models to better understand information security management [54].

System dynamics has been increasingly employed by researchers to investigate information security. Behara et al. [55] developed an information security life cycle model that examines the impact of investment in different facets of IS security. It ass sses the impact of investment in HR policy, intrusion detection, vulnerability reduction, value reduction, and deterrence on the overall number of attacks experienced. Their findings indicate that investment in all areas tends to be more effective than traditional investment strategies that focus on high profile areas only. Another study involving investment and the security life cycle examined the effect of security controls investment on security implementation and obsolescence, and found that different types of controls led to varying levels of overall security with technical security controls being the most effective [56]. Threats posed by security attacks form another stream of research. The effect of insider threats is studied in [57], focusing on the 1996 Omega case and addresses technical security controls, workplace discontent, motivation, and timebomb attacks. Insider threats are also studied in [58] which uses a case of illegal insider corporate stock sale as the basis, and uses disgruntlement, achievement, and unmet expectations to model illegal behavior. More detailed modeling of insider and outsider threats by modeling detection ability, motivation for attacks, trust, and deterrence was presented in a workshop dedicated to the use of system dynamics for modeling information security [59].

Risk-based analysis of security represents another area where system dynamics has been employed. A model that is driven by risk management that analyzes the impact of security policy and threats on detected security intrusions is presented in [60]. The impact of asset vulnerability and risk on security investments is studied in [61], with the findings indicating that after some initial oscillatory behavior, risk, investment and vulnerabilities begin to stabilize. The financial impact of different risk strategies relating to information security is studied in [62]. They found that risk reduction and risk acceptance strategies led to different results in the face of increasing and decreasing risks. Other areas of information security that have been assessed using system dynamics include vulnerability pricing on the black market [63], the effect of incident reporting and incident frequency under different circumstances [64], and personnel forecasting for information security [65].

## 2.4 Selected Modeling Methodology

This research uses system dynamics to investigate the financial implications of security decisions on an organization’s information asset base. The ability to correlate constructs within a time period, as well as track progression across time periods were important factors in selecting system dynamics for the simulation methodology. The model is intended to encompass security policies, vulnerabilities, attacks, relating them to security costs and overall damage sustained. It provides managers with the ability to investigate the effect of putting resources into alternative security channels and the impact of these decisions under a variety of conditions. While the model cannot cover all security attacks and scenarios, it provides managers with insights into relative risk tradeoffs. This research adopts a design science methodology using the system dynamics model as the artifact of interest. Demonstration of the utility of the artifact is accomplished through successful execution of the model under a variety of conditions. Managerial and research implications of the security model are discussed.

## 3. Information Security Management Model

The simulation model for information security management represents an integration of concepts covering several facets of information security. It draws from multiple areas, including software vulnerability, risk assessment, attack motivation, threat detection, deterrence, and security costing. It is based on an earlier model for information security management [66]. The model has been enhanced with the inclusion of additional constructs, and refined through the recalibration of equations to ensure that potentially anomalous situations are prevented. The model is depicted in Figure 1.

## 3.1 Model Description

A quick overview of the notation is provided. Items in rectangles represent stocks that can accumulate or deplete over time. Stocks are affected by flows, which are represented by a double arrow and valve symbol. Flows draw from or empty into infinite reservoirs, though in reality organizations will are specified for the given time period. Values of converters are determined by other converters through connectors. Connectors are signed to indicate if an increase in one will lead to an increase in another. The signs help characterize any loops in the model. Loops can be reinforcing (all positive signs), or balancing (at least one negative sign). Reinforcing loops, if unchecked, will eventually lead to zero or infinite values for the converters involved. Balancing loops will lead to oscillatory behavior, and possibly equilibrium. The model comprises several segments, dealing with attacks, software risk, recovery, vulnerability, and economic considerations. In assembling the model, the emphasis has been on creating a quantifiable and more easily verifiable model. Also, the model is pitched more at the organizational level, than the individual or perceptual level. Models have been assembled to assess motivation for attacks at an individual level [59], [57]. However, quantifiability of some constructs proves challenging, though. Likewise, models can be assembled using organizational perceptions towards information security, including constructs like security culture, security risk perception, security leadership, threat assessment, effectiveness of security processes, training, and employee adherence to security policies [67], [68], [69], [70], [71]. These constructs are more effectively studied through a survey-driven empirical analysis. Instead, the model is slanted more towards an economic perspective that is suitable for manager, than a perceptual construct model that is better suited to survey-driven empirical analysis.

The driver for most information security investment and controls is threats and attacks, and this part of the model is described first. The organization’s image, coupled with the perceived target value shape the target attractiveness. Clearly some organizations are preferred targets, either due to financial considerations or the perceived notoriety in a successful attack. The probability of attack is shaped by the target attractiveness, in conjunction with the attacker’s motivation, the perceived vulnerability of the organization’s information assets, and the deterrence mechanisms in place. With the exception of the last construct, all other determinants have a positive influence on the probability. Perceived vulnerability has a steadily increasing effect on the probability of attack, though at a diminishing rate, and is modeled using an approximation of a negative exponential function. The same concave relationship applies for target attractiveness and attacker motivation, though the impact of the former is more pronounced. Deterrence impact, on the other hand, has a characteristic inverse relationship with the probability of attack, and is modeled as a simple decreasing convex function. Care is taken to ensure that the cumulative effects of the four constructs result in a probability of attack that falls within the 0-1 range. Extensive testing of the function during its formulation established that the resulting attack probabilities are consistent with expectation.

Attacks can originate from inside or outside the organization. The number of attackers, and the availability of tools to launch the attack determine the number of attacks the organization faces. At this point, the model does not differentiate between internal or external attackers. Likewise, it also does not differentiate between attacks on different information assets. It is expected that the success rate for internal attackers and external attackers will not be identical; nor will the impact on different assets. In keeping with the need to inform managers of the aggregate level of threats, the model does not drill down to this level of detail, and focuses more on the aggregate picture. Likewise it does not parse the attacks into different types, e.g. denial of service, hacking, phishing, keystroke capture, virus attacks, SQL injection, etc. It is expected that a majority of the attacks will be detected by existing security tools, e.g. firewalls, intrusion detection systems, anti-virus programs, malware detection programs, spam detection programs, among others. These are characterized as prevented attacks. The rest represent successful attacks. Detection ability is based on the investment in security tools. Investment in security tools does not have to be continuous, since prior investment in security tools will allow the firm to detect attacks. Thus, cumulative security tool investment is used to assess detection ability. This is modeled as a negative exponential function, with increased detection ability at greater security tool investment, though at a diminishing rate eventually. As detection ability increases, the number of prevented attacks also rises, with the balance representing successful attacks. Successful attacks will be manifest in various ways and have considerably different effects. Some of them will cause little damage, while others will have a more pronounced impact. The damage caused by successful attacks is captured on two dimensions, the magnitude of the damage, as well as the urgency needed to act to recover from the damage, termed damage immediacy in the model. Successful attacks will also create some publicity, captured as attack reports in the model. Attack reports are manifest in publicized and unpublicized ways. These include site unavailability, asset unavailability, public acknowledgement of successful attacks, claims made by the attackers, and reports filed with governmental agencies for compliance purposes. It should be noted that some stocks are introduced in the model for convenience purposes only. Thus for example, the total prevented attacks and accumulated security costs are used to accumulate values throughout the simulation, and are not determinate of other variables.

The damage magnitude, damage immediacy, and the number of successful attacks, shape the extent of attack reports. Publicized attack reports will determine the perceived vulnerability of the organization’s information assets, thereby completing the attack loop. This is a reinforcing loop, indicating that successful breaches will lead to more attacks, and effective prevention of attacks will cause attackers to look to other easier or more attractive targets. In an extreme scenario, a reinforcing loop either drives the values of all constructs in the loop to zero or infinity. However, if the model is constructed carefully, the behavior can be controlled, and the extreme cases avoided.

Another segment of the model deals with recovery, system vulnerabilities, and residual risk Damage sustained through a successful attack will invariably initiate a recovery effort. Depending on the nature and extent of the damage, the recovery effort may range from simple to complex, and may involve a trivial to a substantial amount of time. Recovery could be as simple as restoring data from a backup, or may involve rebuilding several servers, including software and hardware reconstruction. The damage magnitude will also trigger a fresh risk assessment effort – more likely an incremental assessment and not a complete entire reassessment. This will identify new and unaddressed vulnerabilities, triggering activity to reduce these vulnerabilities. These activities could take many forms, including application of software patches, software upgrades, and changes to access and security procedures, among others. Software vulnerabilities may be present in any portion of the software development environment, including the operating system, operating environment, and tools used to assemble software. Often these take the form of known bugs and trapdoors, and can be easily fixed through patches and upgrades. They are characterized as base software flaws in the model. Vulnerabilities could also be present in the code that is written in-house, often manifest as lax security, lack of appropriate encryption, no checks for security bypass attempts, improper validation, ineffective audit trails, and the like. As indicated in the model, these are inversely related to the vulnerability reduction effort, indicating that they are expected to drop with increased vulnerability reduction effort. The vulnerabilities in the base and developed software, coupled with the strength of the security procedures will determine the overall system vulnerability. System vulnerability is determined through the combined effects of security procedures and software security risk. The former has a simple inverse exponential relationship, which means that as more effective security procedures are put into place, software vulnerability tails off. Software security risk, on the other hand, has a more direct impact, and is modeled as a positive linear relationship. The combined effect leads to pronounced system vulnerability for cases involving ineffectual security procedures coupled with significant software security risk, and more manageable vulnerabilities in other cases.

Reports of system vulnerability will shape the vulnerability perceived by the attackers. The perceived vulnerability is based on cumulative reports of vulnerability, and while steps may be taken to eliminate some vulnerabilities, unless publicized, they will not affect the perceived vulnerability of the asset base. Perceived vulnerability will increase the probability of attack, thereby completing a second loop. This is a balancing loop, and will tend to seek equilibrium. It will also compensate for the reinforcing loop on attacks.

The final segment of the model relates to security investment and costs. Organizations invest in deterrent actions as well as security tools to detect and prevent attacks, and these represent the input costs in this case. Deterrence actions are typically targeted at internal attackers and take the form of a variety of sanctions. The evidence for the impact of deterrence on attack intentions is mixed, with support in studies done in the US [72], and little to no support in a study done in China [73]. Deterrence has even less impact for external attackers, other than the threat of prosecution, and is rarely effective in these cases. Investment in security tools, on the other hand, is likely to have a more pronounced effect. Some tools target threats specifically, e.g. antivirus software, spyware detection software, anti-spam software, etc. Others adopt a more general set of rules to recognize and thwart attacks, e.g. firewalls, intrusion detection software, and the like. Continued investments in these areas typically have cumulative effect, though not in strictly linear fashion. The cumulative security tools investment determines the ability to detect and thwart attacks. In a similar vein, the cumulative deterrence investment shapes the deterrence impact, which forms part of the attack loop. Investments in security tools and deterrence represent costs to the organization, and together with the vulnerability reduction effort, these constitute the security investment for the organization. Risk assessment costs and recovery costs further contribute to the overall firm security cost. For convenience, a stock is used to compute total security expenditure over the course of the simulation.

The model includes one reinforcing loop and three balancing loops. The reinforcing loop is centered around security attacks, where successful attacks generate publicity about perceived vulnerability, drawing more attackers. This behavior would continue unabated, but is held in check by the balancing loops involving system vulnerabilities. Detection of successful attacks leads to a variety of vulnerability reduction activities, including patching of base software flaws, elimination of developed software flaws, and implementation of new security procedures.

Equations employed in the model appear in the appendix. The stocks are simple accumulations starting from zero values, with the exception of deterrence investment and security tools investment that start at \$2,000 and \$10,000 respectively. The majority of the inputs are set up on a normalized 0-1 scale, with values chosen in the middle, representing a middle-of-the-road scenario. This permits subsequent exploration in conditions involving greater or reduced security threats. For the initial trials, the number of attackers in the system is pegged at 100, and the value of the asset base is set to \$5 million. Deterrence investment occurs every six months, while security tool investment is an annual outlay. The values will vary with the scenario studied. Equations for the converter variables are also included.

## 3.2 Model Validation

Validation of a system dynamics model is generally performed using two approaches. A structural validation of the model seeks to determine if it reflects the real world accurately [74]. Behavioral assessment focuses on the model behavior during execution, and assesses the degree of confidence that can be placed in the results [75]. Structural validation was performed using structural verification and extreme condition analysis. Structural verification addresses whether the model structure is consistent with the descriptive knowledge about the real world phenomenon being modeled. The constructs used in the model, viz. attacks, damages, risk, vulnerability, and costs, are all drawn from the information security literature. Extreme condition analysis assesses whether the parameters in the model behave appropriately under extreme conditions. In order to assess this response surfaces were compiled for each endogenous variable. The results were examined for any incongruous behavior as well as consistency with logical expectation. The former assesses whether any parameters take on values outside the prescribed limits, e.g. probabilities greater than 1. The latter examines the response of the endogenous variable to changes in the inputs. Behavior that does not conform to constraints and expectation triggers more introspective evaluation of the equation. The bulk of the structural validation effort is targeted at model behavior within a time period. Behavioral assessment requires execution of the entire model and examination of the results. In this case, parameters are varied systematically to assess whether the entire model is functioning as expected. In addition, the behavior of individual constructs is tracked over time. The temporal behavior is analyzed for oscillations and trends towards extreme values. Any aberrant behavior triggers a closer examination of the relevant constructs, and may require recalibration and restructuring of the model. The model was validated structurally and behaviorally. One case of range violation was noted, with attack probability falling outside the 0-1 range under extreme conditions. Two stocks were introduced to stabilize the behavior, and the equations recalibrated to address this anomaly. A subsequent round of validation indicated no further anomalies.

## 4. Simulation Results

Simulation of the model was conducted using Vensim® PLE, a fully functional system dynamics software package from Ventana Systems, Inc. The unit time frame selected was a month, and the model was run over a period of 30 months, representing a medium term security planning horizon. Attempting to simulate for longer periods would entail greater uncertainty, and less meaningful results, since longer term predictions are hard to make accurately in the information security area. The model was run under a variety of conditions to understand the impact of different security policies and investments on the overall attacks, damages, and security costs, with a view to assisting managers make effective decisions concerning information security.

## 4.1 Base Scenario

The base scenario was calibrated for a small organization, using median values for the dimensionless constructs, and a set of plausible values for other constructs. This involved an asset base of \$5,000,000, an attacker population of 100, and the security tool investment set at \$5,000 at the start of every year, with deterrence expenses of \$2,000 every six months. After running the model, the number of attacks, total damages, and overall security costs were tracked. These results appear in Figure 2.

Monthly data for the constructs tends to be jagged in nature, and an aggregation over time provides a better sense of the trends involved. The number of attacks demonstrates an increasing trend punctuated with some lulls in the pattern. From the data, it is clear that not all attacks are successful, and only some cause damage. Variation in the attack severity explains the variability in the damages incurred. Any damage incurred triggers a recovery effort as well as a risk reduction effort, and thus the security costs tend to mirror the damage to some extent. An examination of the other constructs in the simulation indicated that they were consistent with expectation. In a further effort to behaviorally validate the model, the model was subjected to sensitivity and perturbation analysis. This was done by systematically varying key input parameters. No untoward patterns were observed, suggesting that the model was behaving satisfactorily.

## 4.2 Alternative Security Investment Scenarios

After establishing that the model was structurally sound, and that its behavior was consistent with expectation, it was used to investigate the impact of different information security investment decisions. The security tool investment was varied from \$3,000 to \$7,000 in \$1,000 increments , keeping the deterrence investment the same. Cumulative successful attacks, damages, and security costs were compiled for these scenarios, and are presented in Table 1.

<table><tr><td>Scenario</td><td>Security Tool Investment ($)</td><td>Deterrence Investment ($)</td><td>Successful Attacks</td><td>Damages ($)</td><td>Security Cost ($)</td></tr><tr><td>Very Low Security Tool Investment</td><td>3,000</td><td>2,000</td><td>208</td><td>42,904</td><td>239,426</td></tr><tr><td>Low Security Tool Investment</td><td>4,000</td><td>2,000</td><td>144</td><td>29,645</td><td>175,349</td></tr><tr><td>Base Scenario</td><td>5,000</td><td>2,000</td><td>102</td><td>20,676</td><td>133,007</td></tr><tr><td>High Security ToolInvestment</td><td>6,000</td><td>2,000</td><td>73</td><td>14,619</td><td>105,174</td></tr><tr><td>Very High Security Tool Investment</td><td>7,000</td><td>2,000</td><td>53</td><td>10,468</td><td>86,820</td></tr></table>

Table 1. Simulation Results for Security Tool Investments

To some extent, the overall trend in these results is predictable. As the level of security tool investment is dropped, the number of successful attacks increases, and correspondingly, the damages incurred and the overall security cost. Other security costs also increase, including recovery costs and vulnerability reduction costs. As the level of security tool investment increases, the cumulative successful attacks, damages, and overall security costs all drop, and quite dramatically. A similar analysis was performed for deterrence investment, varying it from \$0 to \$4,000, in \$1,000 increments. These results appear in Table 2.

<table><tr><td>Scenario</td><td>Security Tool Investment ($)</td><td>Deterrence Investment ($)</td><td>Successful Attacks</td><td>Damages ($)</td><td>Security Cost ($)</td></tr><tr><td>Very Low Deterrence Investment</td><td>5,000</td><td>0</td><td>127</td><td>22,685</td><td>136,093</td></tr><tr><td>Low Deterrence Tool Investment</td><td>5,000</td><td>1,000</td><td>118</td><td>22,343</td><td>137,483</td></tr><tr><td>Base Scenario</td><td>5,000</td><td>2,000</td><td>102</td><td>20,676</td><td>133,007</td></tr><tr><td>High Deterrence Tool Investment</td><td>5,000</td><td>3,000</td><td>88</td><td>18,687</td><td>127,837</td></tr><tr><td>Very High Deterrence Investment</td><td>5,000</td><td>4,000</td><td>79</td><td>17,583</td><td>126,758</td></tr></table>

Table 2. Simulation Results for Deterrence Investments

As before, the overall trend is predictable. However, the effects are a considerably less pronounced in this case. This necessitated some additional investigation into the components that determined the overall security dimensions of interest. A more detailed exploration of the underlying constructs was performed, and traces of the constructs of interest yielded additional insight. These results are depicted in Figures 3, 4, and 5. Security tool and deterrence investments are contrasted for varying levels, and their impact on cumulative successful attacks, damages, and overall security costs are depicted during the simulation runs.

These graphs provide greater insight, and a more telling observation is the relative impact of different forms of security investment. Investment in detection and prevention has a considerably larger impact than investment in deterrence. Detection and prevention tools help reduce the number of successful attacks. Reduction in investment in this area has a significant impact on the number of successful attacks, while added investment does reduce that number considerably. Investment in deterrence, on the other hand, has a smaller impact. Deterrence is primarily aimed at internal attackers, and while it is suggested that this is sometimes a greater threat than external attackers [57], it is rarely an effective de-motivator for a determined attacker. Additionally, sophisticated external attackers are not significantly influenced by deterrence practices, since the probability of trace-back is often low, and prosecution thereafter is extremely unlikely. It is interesting to note that a 75% reduction in successful attacks can be achieved through added security tool investment, as compared to a 37% decrease for added deterrence investment. However, that interpretation would skew the true implications since the number of successful attacks is nearly double for low security tool investment.

An examination of the implications of these attacks was subsequently conducted. Focusing on the magnitude of the damages incurred provided additional insights. Since not all successful attacks have the same severity of impact, a little more choppy response surface can be expected for cumulative damages. Indeed, the data does bear this out. Once again, a similar trend is noted, with considerably greater variations noted for security tool investment than deterrence investment. While many possible interpretations are available, the appropriate implication is that changes in the level of deterrence investment have little impact on damages incurred. On the other hand, appropriate investment in security tools has a considerable impact, and when that investment is cut back, a strong negative impact materializes.

The impact on overall security costs proved to be equally insightful. Overall security costs also include recovery costs, risk assessment costs, and vulnerability reduction effort. Recovery costs are driven by the extent of the damage incurred, with a short lag. Risk assessment costs represent a smaller cost component, but are also driven by the extent of damage. Likewise vulnerability reduction effort is an outcome of risk reassessment, and in turn will be influenced by the extent of damage. However, in these cases, the lag is more pronounced. The cumulative effect of these costs is a magnifying effect. As a result, the overall security costs vary considerably with investment in security tools, as compared to deterrence investment. Even with no deterrence investment, the impact on overall security costs is minimal, and doubling the investment from the base scenario provides little overall impact. The same cannot be said for security tool investment, with greater investment leading to substantial reduction in overall costs, and cutbacks in investment leading to far greater security costs.

In an effort to isolate the effect of each investment, variations of investment were considered and graphed. These results appear in Figure 6. The interpretation for security tool investment is relatively clear. Additional investment has a predictable impact on reducing overall security costs. The impact of deterrence investment proved to be less predictable. In this case, the overall costs increased, then decreased, and then increased again. Nonetheless, a closer examination is able to illustrate this apparent paradox. Deterrence does have an impact on reducing successful attacks and hence overall security costs. However, this impact is a relatively small, especially at low levels of deterrence investment. So the savings generated through reduced recovery effort are not offset by the deterrence investment, and the total security costs continue to rise. Slightly higher levels of deterrence investment generate an inflection point, and the reduction in successful attacks has a more dramatic payoff. In this segment, the benefit from deterrence investment outweighs the cost, and the overall trend is downward. When the number of successful attacks are driven down close to zero, spending more on deterrence is fruitless, since the marginal savings due to diminished attacks is clearly outweighed by the increased deterrence investment. It should also be noted that the overall variation is relatively small, compared to that of security tool investment.

In an effort to understand the combined effects of both security tool and deterrence investment, a grid search was performed varying both inputs systematically for a total of 25 simulation runs. The effect on overall security costs is depicted in Figure 7. The impact of security tool investment was consistent, in that overall security costs decreased in a convex manner at all levels of deterrence investment, with the effect being more pronounced at low to zero deterrence investment. The impact of deterrence investment is a little more ambiguous. At low levels of security tool investment, increases in deterrence investment lead to lower overall security costs. At higher levels of security tool investment, the impact of deterrence impact at the extreme points starts to decrease, and the cost of deterrence begins to outweigh the investment. The effect is first felt at the low end of deterrence values, and later manifests itself at higher deterrence values. Finally, at high levels of security tool investment, the overall impact of deterrence investment is negligible.

## 5. Managerial and Research Implications

At a fundamental level, the model provides managers with clear guidelines about investment in security and its impact. The reinforcing loop on security attacks illustrates that if left unchecked, successful attacks will increase perceptions about system vulnerability, drawing more attacks and eventually leading to untenable situations regarding protection of information assets. However, investment in suitable vulnerability reduction activities, coupled with the implementation of improved security procedures can effectively combat this situation. It is important to note that expenses incurred in damage recovery, though extremely necessary, do not contribute to reduction in attacks. That is accomplished only through patches to software flaws and changes in security procedures. Managers must be vigilant in taking action to eliminate vulnerabilities in order to safeguard the firm’s information assets.

The information security management model indicates that different security investments have different implications for the overall costs associated with providing security for information assets. Several key implications can be inferred, some of which are expected, but others provide a different insights. At the most basic level, overall security costs decrease with increased investment in information security. However, this is not an unbounded relationship, in that at some point security costs from the investments themselves will outweigh any benefits through reduced damages and recovery efforts. This is due to inverse nature of relationship between security investment and attacks. No amount of investment can eliminate all successful attacks . However, at high levels of security investment, additional security investment does not materially change the number of successful attacks, thereby incurring additional costs and no material benefits.

An examination of the different security investment channels reveals that not all investment has the same payoff. Investment in tools for detecting and preventing security attacks yielded the greatest payoff. In a similar vein, a cutback on investment in this area had the most deleterious effect. A variety of tools are available in this category addressing distinct and overlapping threats. These include anti-virus programs, malware and spyware detection programs, firewalls, intrusion detection systems (network and host versions), practices to mitigate SQL injection, among others. Improved detection leads to fewer successful attacks, and less damage to information assets. The implication for security managers is that this area of security investment cannot be overlooked. An organization’s information assets are likely to be distributed across many platforms and reside at multiple locations. A combination of security tools need to be deployed to counter the attacks, and secure the multiple information assets at multiple locations. The effectiveness of these tools will predictably degrade over time, as newer versions of attack vectors, as well as newer attack vectors are developed. Security managers need to be constantly vigilant, keeping the portfolio of security tools current. Some of these tools may be automatically updated, e.g. anti-virus programs, and malware and spyware detection programs. Others, like firewalls and intrusion detection systems, will entail periodic reconfiguration to deal with new attack vectors, new sources of attack, and new assets to safeguard. While this invariably involves time and effort, the implications are clear. Any attack prevented has definite payoff in terms of reduced damage potential, recovery effort, and subsequent risk assessment and vulnerability reduction effort. Since the effect was observed at all levels of deterrence investment, managers who are lax about security tool maintenance do so at their peril.

Investment in deterrence had a considerably smaller payoff. Deterrence activities take many forms, including formulating policies and procedures to reduce attacks, as well as procedures for dealing with identified attackers. Most deterrence activities rely on compliance by employees, which make it a weaker aspect of security. Users often employ easily broken passwords, change them rarely if at all, and do not protect them sufficiently. Newly installed software is frequently not adequately secured, typically manifest as default master accounts not appropriately reconfigured. Lax practice by employees may result in data breaches or leakage, putting the organization and its clients at risk. In addition, internal attackers may have a significant advantage as they may be privy to current security procedures, and cause significant damage through sabotage [57]. Deterrence policies for internal attackers are not always effective. For example, despite threats of discipline and termination for snooping among protected data, including dismissals for high profile cases involving medical data, employees often engage in these activities. Deterrence has even less effect or disincentive for external attackers, since they are often not detected, or may be difficult to successfully prosecute. However, even though it will not prevent attacks, investment in security deterrence is necessary. Two important implications for managers emerge from these simulations. The first is that more investment in deterrence does not automatically equate to lower overall security costs, due to the muted benefits. The second is that effect of deterrence investment does vary with the level of security tool investment, in some cases the payoff is minimal, where in other cases it does make a difference. Knowing when it has an impact will allow managers to deploy their security resources more effectively.

The model also indicates that investment in some areas is more beneficial than others. This is in contrast to earlier research that suggests that across the board investment leads to fewer attacks than differential investment [55]. It is important to note that this research has focused on cost, while earlier system dynamics models focuses on attacks. Nonetheless, when managers choose to allocate resources based on potential impact, it is important to note that dropping investment in any area down to zero is not recommended under any circumstances, as all cutbacks invariably lead to increased security costs.

There are several implications for researchers. This research developed a model that can be used to explore and understand the implications of different investment in security decisions. The findings indicate that investment in security tools has a higher impact than investment in deterrence. Further exploration is needed to determine if security tool investment always has a positive payoff. It is likely that at some point the marginal cost will outweigh the marginal benefit, introducing the notion of an optimal investment level. The model can also be used to investigate the security under a number of different conditions. For example, if the organization is a more attractive target, or the number of attackers was considerably higher, or new attack vectors are developed that lead to more successful attacks, or the organization acquires a portfolio of new information assets through a merger or acquisition. These would involve changes to the input variables, and represents further areas for research. These extensions will require systematic exploration of the search space, as well as detailed structural analyses to ensure that intermediate variables are behaving appropriately.

## 6. Conclusions

Securing information assets is of critical importance for organizations. While it is unlikely that all assets can be made absolutely secure, or it may be prohibitively expensive to do so, organizations need to invest appropriately in security endeavors. This research examined the effect of investing in different areas of information security, using a system dynamics model to understand the implications of these investments. The model incorporates many aspects of security practice, include attacks, detection, recovery, risk assessment, and vulnerability reduction. Simulations using the model indicate that investments in security tools designed to detect attacks led to a better payoff than in deterrence activities. It also indicates that investment in all areas of security is needed for effectively protecting information assets. The model can be used in a variety of ways by practitioners and researchers. It can serve as a decision support tool, recommending the preferred ways in which to expend security investments. It can also serve as a design tool, wherein competing security policies can be evaluated under a variety of different circumstances with a view to identifying best practices. It can serve as an explanation tool, through a systematic explication of the structural relationships that link attacks to overall security costs. In summary, it provides researchers a rich environment to better understand the implications of security decisions under a variety of circumstances, and assist practitioners in making better decision concerning information security.

## References

[1] R. Richardson, 15th Annual 2010/2011 Computer Crime and Security Survey, in, Computer Security Institute, New York, NY, 2011.

[2] A.C. Johnston, M. Warkentin, Fear Appeals and Information Security Behaviors: An Empirical Study, MIS Quarterly, 34 (2010) 549-566.

[3] M. Cremonini, P. Martini, Evaluating Information Security Investments from Attackers Perspective: the Return-On-Attack (ROA), in: 4th Workshop on the Economics of Information Security, Harvard University, Cambridge, MA, 2005, pp. 4.

[4] L.D. Bodin, L.A. Gordon, M.P. Loeb, Evaluating Information Security Investments Using the Analytic Hierarchy Process, Communications of the ACM, 48 (2005) 79-83.

[5] M.E. Whitman, H.J. Mattord, Principles of Information Security, Fourth ed., Course Technology, Boston, MA, 2012.

[6] A.R. Hevner, S.T. March, J. Park, S. Ram, Design Science in Information Systems Research, MIS Quarterly, 28 (2004) 75-106.

[7] R. Baskerville, Information Systems Security Design Methods: Implications for Information Systems Development, ACM Computing Surveys, 25 (1993) 375-414.

[8] D.W. Straub, Effective IS Security: An Empirical Study, Information Systems Research, 1 (1990) 255-276.

[9] K.H. Guo, Y. Yuan, The effects of multilevel sanctions on information security violations: A mediating model Information & Management, 49 (2012) 320-326.

[10] S.J. Harrington, The Effect of Codes of Ethics and Personal Denial of Responsibility on Computer Abuse Judgments and Intentions", MIS Quarterly, 20 (1996) 257-278.

[11] D.W. Straub, W.D. Nance, Discovering and Disciplining Computer Abuse in Organizations: A Field Study, MIS Quarterly, 14 (1990) 45-60.

[12] A. Simmonds, P. Sandilands, L.v. Ekert, An Ontology for Network Security Attacks, in: S. Manandhar, J. Austin, U. Desai, Y. Oyanagi, A. Talukder (Eds.) Applied Computing, Springer, Berlin, 2004, pp. 317-323.

[13] M.d. Vivo, G.O.d. Vivo, G. Isern, Internet security attacks at the basic levels, ACM SIGOPS Operating Systems Review 32 (1998) 4-15.

[14] K. Siau, F.F.-H. Nah, L. Teng, Acceptable internet use policy, Communications of the ACM, 45 (2002) 75-79.

[15] J.-Y. Son, Out of fear or desire? Toward a better understanding of employees’ motivation to follow IS security policies, Information & Management, 48 (2011) 296-302.

[16] F. Stewart, Internet Acceptable Use Policies: Navigating the Management, Legal, and Technical Issues, Information Systems Security, 9 (2000) 1-7.

[17] A. Vance, M. Siponen, S. Pahnila, Motivating IS security compliance: Insights from Habit and Protection Motivation Theory, Information & Management,, 49 (2012) 190-198.

[18] T.P. Cronan, C.B. Foltz, T.W. Jones, Piracy, computer crime, and IS misuse at the university, Communications of the ACM, 49 (2006) 84-90.

[19] W.F. Skinner, A.M. Fream, A Social Learning Theory Analysis of Computer Crime among College Students, Journal of Research in Crime and Delinquency, 34 (1997) 495-518.

[20] B. Ives, K.R. Walsh, H. Schneider, The domino effect of password reuse, Communications of the ACM, 47 (2004) 75-78.

[21] M. Zviran, W.J. Haga, Password Security: An Empirical Study, Journal of Management Information Systems, 15 (1999) 161-185.

[22] Y. Chen, D.L. Nazareth, K.-W. Wen, Research in Information Security: A Literature Review Using a Multidimensional Framework, in: Proceedings of the Thirty-Ninth Annual Western Decision Sciences Institute Conference (WDSI 2010), Lake Tahoe, NV, 2010, pp. 3681-3687.

[23] V.K.G. Lim, T.S.H. Teo, Prevalence, perceived seriousness, justification and regulation of cyberloafing in Singapore: An exploratory study, Information & Management, 42 (2005) 1081– 1093.

[24] A. Hovav, J. D’Arcy, Applying an extended model of deterrence across cultures: An investigation of information systems misuse in the U.S. and South Korea, Information & Management, 49 (2012) 99-110.

[25] Y. Lee, K.A. Kozar, An empirical investigation of anti-spyware software adoption: A multitheoretical perspective, Information & Management, 45 (2008) 109-119.

[26] M. Siponen, R. Willison, Information security management standards: Problems and solutions, Information & Management, 46 (2009) 267-270.

[27] M.T. Siponen, An Analysis of the Traditional IS Security Approaches: Implications for Research and Practice, European Journal of Information Systems, 14 (2005) 303-315.

[28] A.G. Kotulic, J.G. Clark, Why there aren't more information security research studies, Information & Management, 41 (2004) 597-607.

[29] G. Dhillon, J. Backhouse, Current Directions in IS Security Research: Towards Socio-Organizational Perspectives, Information Systems Journal, 11 (2001) 127-153.

[30] A. Sunyaev, F. Tremmel, C. Mauro, J.M. Leimeister, H. Krcmar, A Reclassification of IS Security Analysis Approaches, in: Proceedings of the 15th Americas Conference on Information Systems (AMCIS 2009), San Francisco, CA, 2009, pp. Paper 570.

[31] C.E. Landwehr, Formal Models for Computer Security, ACM Computing Surveys, 13 (1981) 247-278.

[32] D.E. Bell, L.J. LaPadula, Secure Computer Systems: Mathematical Foundations and Model, in, MITRE Corporation, Bedford, MA, 1974.

[33] K.J. Biba, Integrity Considerations for Secure Computer Systems, in, MITRE Corporation, Bedford, MA, 1977.

[34] M.A. Harrison, W.L. Ruzzo, J.D. Ullman, Protection in Operating Systems, Communications of the ACM, 19 (1976) 461-471.

[35] D.D. Clark, D.R. Wilson, A Comparison of Commercial and Military Computer Security Policies, in: Proceedings of the 1987 IEEE Symposium on Research in Security and Privacy (SP'87), IEEE Press, Oakland, CA, 1987, pp. 184-193.

[36] D.F.C. Brewer, M.J. Nash, The Chinese Wall security policy, in: Proceedings of the 1989 IEEE Symposium on Security and Privacy, Oakland, CA, 1989, pp. 206-214.

[37] L.A. Gordon, M.P. Loeb, Budgeting Process for Information Security Expenditures, Communications of the ACM, 49 (2006) 121-125.

[38] K.J.S. Hoo, How much is Enough? A Risk-Management Approach to Computer Security, in, Consortium for Research on Information Security and Policy (CRISP), Stanford University, Palo Alto, Ca, 2000, pp. 99.

[39] A. Arora, D. Hall, C.A. Pinto, D. Ramsey, R. Telang, Measuring the Risk-Based Value of IT Security Solutions, IT Professional, 6 (2004) 35-42.

[40] L.A. Gordon, M.P. Loeb, Return on Information Security Investments: Myths vs. Reality, Strategic Finance, 84 (2002) 26-32.

[41] C.D. Huang, Q. Hu, R.S. Behara, In Search for Optimal Level of Information Security Investment in Risk-Averse Firms, in: Proceedings of the Third Annual Security Symposium: Information Security in the Knowledge Economy, Tempe, AZ, 2005.

[42] C.D. Huang, Q. Hu, R.S. Behara, An economic analysis of the optimal information security investment in the case of a risk-averse firm, International Journal of Production Economics, 114 (2008) 793–804.

[43] L.A. Gordon, M.P. Loeb, W. Lucyshyn, Information Security Expenditures and Real Options: A Wait-and-See Approach, Computer Security Journal, 19 (2003) 1-7.

[44] L.A. Gordon, M.P. Loeb, The Economics of Information Security Investment, ACM Transactions on Information and Systems Security, 5 (2002) 438-457.

[45] R. Anderson, T. Moore, Information Security Economics - and Beyond, in: A. Menezes (Ed.) Advances in Cryptology 2007, Springer-Verlag, 2007, pp. 68-91.

[46] P. Carayon, S. Kraemer, Macroergonomics in WWDU: What about computer and information system security?, in: Proceedings of 6th International Scientific Conference on Work With Display Units, Berchtesgaden, Germany, 2002, pp. 87-89.

[47] G. Dhillon, Violation of Safeguards by Trusted Personnel and Understanding Related Information Security Concerns, Computers and Security, 20 (2001) 165-172.

[48] K. Hamacher, S. Katzenbeisser, Public Security: Simulations Need to Replace Conventional Wisdom, in: Proceedings of the 2011 New Security Paradigms Workshop, Marin County, CA, 2011, pp. 115-124.

[49] R. Chiong, S. Dhakal, Modelling Database Security through Agent-Based Simulation, in: Proceedings of the Second Asia International Conference on Modeling & Simulation (AICMS 08), Kuala Lumpur, Malaysia, 2008, pp. 24-28.

[50] M. Remondino, Multi Agent Based Simulation for Database Security: A Framework, in: Proceedings 18th European Simulation Multiconference, Magdeburg, Germany, 2004, pp. 372- 377.

[51] A.R. Chaturvedi, M. Gupta, S.R. Mehta, W.T. Yue, Agent-Based Simulation Approach to Information Warfare in the SEAS Environment, in: Proceedings of the 33rd Hawaii International Conference on System Sciences (HICSS 2000), Maui, Hawaii, 2000.

[52] J.D. Sterman, Business Dynamics: Systems Thinking and Modeling for a Complex World, Irwin McGraw-Hill, New York, NY., 2000.

[53] J.W. Forrester, Industrial Dynamics, MIT Press, Cambridge, MA, 1961.

[54] D. Trcek, Security Models: Refocusing on the Human Factor, Computer, 39 (2006) 103-104.

[55] R. Behara, C.D. Huang, Q. Hu, A System Dynamics Model of Information Security Investments, in: Proceedings of European Conference on Information Systems, Geneva, Switzerland, 2007, pp. 1572-1583.

[56] J.M. Sarriegi, J. Santos, J.M. Torres, D. Imizcoz, E. Egozcue, D. Liberal, Modeling and Simulating Information Security Management, in: Critical Information Infrastructures Security Springer-Verlag, Berlin, 2008, pp. 327-336.

[57] C. Melara, J.M. Sarriegui, J.J. Gonzalez, A. Sawicka, D.L. Cooke, A System Dynamics Model of an Insider Attack on an Information System, in: J.J. Gonzalez (Ed.) From Modeling to Managing Security: A System Dynamics Approach, Norwegian Academic Press, Kristiansand, Norway, 2003, pp. 9-36.

[58] S.-C. Yang, Y.-L. Wang, Insider Threat Analysis of Case Based System Dynamics, Advanced Computing, 2 (2011) 1-17.

[59] J.J. Gonzalez, J.M. Sarriegui, in: System Dynamics Modeling for Information Security: An Invitational Group Modeling Workshop, Carnegie Mellon University, Pittsburgh, PA, 2004.

[60] D. Trcek, Using systems dynamics for human resources management in information systems security, Kybernetes, 35 (2006) 1014-1023.

[61] D. Trcek, Using System Dynamics for Managing Risks in Information Systems, WSEAS Transactions on Information Science & Applications, 2 (2008) 175-180.

[62] A.C. Kim, S.M. Lee, D.H. Lee, Compliance Risk Assessment Measures of Financial Information Security using System Dynamics, International Journal of Security and Its Applications, 6 (2012) 191-200.

[63] J. Radianti, J.J. Gonzalez, Toward a Dynamic Modeling of the Vulnerability Black Market, in: The Workshop on the Economics of Securing the Information Infrastructure (WESII), Washington, D.C., 2006, pp. 19.

[64] F.O. Sveen, J.M. Sarriegi, E. Rich, J.J. Gonzalez, Toward viable information security reporting systems, Information Management & Computer Security, 15 (2007) 408-419.

[65] S.-H. Park, S.M. Lee, S.N. Yoon, S.-J. Yeon, A dynamic manpower forecasting model for the information security industry, Industrial Management & Data Systems, 108 (2008) 368-384.

[66] D.L. Nazareth, J. Choi, Information Security Management: A System Dynamics Approach, in: Eighteenth Americas Conference on Information Systems (AMCIS-2012), Seattle, WA, 2012, pp. Paper 3.

[67] M.A. Alnatheer, A Conceptual Model to Understand Information Security Culture, International Journal of Social Science and Humanity, 4 (2014) 104-107.

[68] A.S. Coronado, M.A. Mahmood, S. Pahnila, E.M. Luciano, Measuring Effectiveness of Information Systems Security: An Empirical Research, in: Proceedings of the Fifteenth Americas Conference on Information Systems (AMCIS-09), San Francisco, CA, 2009, pp. Paper 282.

[69] W.R. Flores, M. Korman, Conceptualization of Constructs for Shaping Information Security Behavior: Towards a Measurement Instrument, in: pre-ICIS Workshop on Information Security and Privacy (WISP), Orlando, FL, 2012, pp. Paper 11.

[70] K.J. Knapp, A Model of Managerial Effectiveness in Information Security: From Grounded Theory to Empirical Test, Unpublished doctoral dissertation, Management Information Systems, Auburn University, 2005.

[71] J. May, Analyzing the Socio-Organizational Constructs for IS Security within Organizations, in: S. Furnell, P. Dowland (Eds.) Proceedings of the 11th IFIP TC11.1 Working Conference on Information Security Management, Richmond, VA, 2008, pp. 103-118.

[72] J. D’Arcy, A. Hovav, D. Galletta, User awareness of security countermeasures and its impact on information systems misuse: A deterrence approach, Information Systems Research, 20 (2009) 79-98.

[73] Q. Hu, Z. Xu, T. Dinev, H. Ling, Does Deterrence Work in Reducing Information Security Policy Abuse by Employees?, Communications of the ACM, 54 (2011) 54-60.

[74] J.W. Forrester, P.M. Senge, Tests for Building Confidence in System Dynamics Models., TIMS Studies in the Management Science, 14 (1980) 208-228.

[75] Y. Barlas, Multiple tests for validation of system dynamics type of simulation models, European Journal of Operational Research, 42 (1989) 59-87.

## Appendix Model Equations

## Stocks:

Accumulated Security Cost= INTEG (Security Cost, 0)

Cumulative Deterrence Investment= INTEG (Deterrence Investment, 2000)

Cumulative Reports= INTEG (Reported Attacks, 1)

Cumulative Security Tools Investment= INTEG (Security Tools Investment, 10000)

Cumulative Vulnerability= INTEG (System Vulnerability, 0)

Damage= INTEG (Damage Magnitude-Recovery Effort, 0)

Total Prevented Attacks= INTEG (Prevented Attacks, 0)

## Inputs:

Asset Value=5,000,000

Attack Motivation=0.5 on a {0-1} scale

Attack Tool Availability=0.5 on a {0-1} scale

Deterrence Investment=2000\*(PULSE TRAIN(6,1,6,29))

Number of Attackers=100

Organization Image=0.5 on a {0-1} scale

Perceived Target Value=0.5 on a {0-1} scale

Security Tools Investment=5000\*PULSE TRAIN(0,1,12,29)

## Variables:

Base Software Flaws=0.75\*EXP(-0.01\*Vulnerability Reduction Effort)

Damage Immediacy=1-EXP( -1\*0.2\*Successful Attacks/10 )

Damage Magnitude=IF THEN ELSE(RANDOM UNIFORM(0,1,0) > 0.5, 0.0002\*Asset Value\*Successful

Attacks\* RANDOM EXPONENTIAL(0,1,0,1,0), 0)

Detection Ability=1-EXP( -0.001\*Cumulative Security Tools Investment/5)

Deterrence Impact=1-EXP( -1\*0.125\*Cumulative Deterrence Investment/1000 ) on a {0-1} scale

Deterrence Investment= 2000\*(PULSE TRAIN(6,1,6,29))

Developed Software Flaws=0.5\*EXP(-0.01\*Vulnerability Reduction Effort)

Number of Attacks=RANDOM UNIFORM(2.5\*(Probability of Attack\*Number of Attackers)\*(Attack Tool

Availability^1.1), 7.5\*(Probability of Attack\*Number of Attackers)\*(Attack Tool Availability^1.1), 0)

Perceived Vulnerability=IF THEN ELSE( 0.01\*Cumulative Vulnerability\*Cumulative Reports < 1 , (0.01

\*Cumulative Reports\*Cumulative Vulnerability), 1) on a {0-1} scale

Prevented Attacks=Detection Ability\*Number of Attacks

Probability of Attack=IF THEN ELSE((3.6\*(0.1+(Perceived Vulnerability-0.1)/(Perceived Vulnerability

+1))\*(0.3+(Target Attractiveness-0.1)/(Target Attractiveness+0.5))\*(0.1+(Attack Motivation

-0.1)/(Attack Motivation+1))/Deterrence Impact)<1, (3.6\*(0.1+(Perceived Vulnerability

-0.1)/(Perceived Vulnerability+1))\*(0.3+(Target Attractiveness-0.1)/(Target Attractiveness

+0.5))\*(0.1+(Attack Motivation-0.1)/(Attack Motivation+1))/Deterrence Impact ),1)

Recovery Effort=RANDOM UNIFORM(Damage Magnitude\*0.5, Damage Magnitude\*1.5, 0)

Reported Attacks=IF THEN ELSE( Successful Attacks\*Damage Magnitude\*Damage Immediacy=0 , 1

, LN(Successful Attacks)\*(Damage Magnitude^Damage Immediacy)/10 )

Risk Assessment Effort= (Damage Magnitude^Damage Immediacy)

Security Cost=Security Investment+Recovery Effort\*5+Risk Assessment Effort\*50

Security Investment= (Vulnerability Reduction Effort\*50) + Deterrence Investment + Security Tools Investment

Security Procedures=1-EXP(-0.5\*Vulnerability Reduction Effort/100) on a {0-1} scale

Software Security Risk=2.7\*((Developed Software Flaws)/(Developed Software Flaws+1))\*((Base Software Flaws

+0.1)/(Base Software Flaws+0.5))

Successful Attacks= ACTIVE INITIAL ((1-Detection Ability)\*Number of Attacks, 10)

System Vulnerability=Software Security Risk\*EXP(-2\*Security Procedures)

Target Attractiveness=2.5\*((Organization Image)/(Organization Image+1))\*((Perceived Target Value +0.2)/

(Perceived Target Value+0.5))

Vulnerability Reduction Effort=RANDOM UNIFORM(Risk Assessment Effort\*0.5, Risk Assessment Effort\*1.5, 0)

Figure 1. Information Security Management Model

Figure 2. Simulation Results for Base ScenarioFigure 3. Cumulative Successful Attacks Using Different Security Investments

Figure 4. Cumulative Damages Incurred Using Different Security Investments

Figure 5. Cumulative Security Costs Using Different Security Investments

Figure 6. Relative Impact of Different Security Investments

Figure 7. Combined Impact of Different Security Investments

![](/api/attachments/9NN32Y3F/fulltext/images/be1e5e7da20f5181a676457da1acc3cabc30e246b8eea1305ed3b520c4ab9952.jpg)

![](/api/attachments/9NN32Y3F/fulltext/images/3ced16a15895a6cc7a4d2ad93ddedbed0de188cbf05b33decc3bc6047c2c4f59.jpg)

![](/api/attachments/9NN32Y3F/fulltext/images/d9ca9880e90e6784c8dd99dc8d4fd20df833f2a892611f3a1690f5a21074d59f.jpg)

![](/api/attachments/9NN32Y3F/fulltext/images/075652e6c1df601b40388dd62dcad2301d36bac921b095e92c6705bd272cbed3.jpg)

![](/api/attachments/9NN32Y3F/fulltext/images/b3e5a1cb126716f016768d356f0c1bf65f0711611da4e366b0ad696579e1f399.jpg)

![](/api/attachments/9NN32Y3F/fulltext/images/a9e31c2d586acb65b549423a22cc1d9ff97a6d1a1c0320cfcb0b34100eea7fb1.jpg)

![](/api/attachments/9NN32Y3F/fulltext/images/3860b7e8a3fdb03b315c896d5f189071b8e0777e5d6ad8d82d9601db85678f4b.jpg)

![](/api/attachments/9NN32Y3F/fulltext/images/13d1679ed57462ba46d1d5d16acf613bb0f5d16b8e6120ae26350c4ccffce7b6.jpg)

![](/api/attachments/9NN32Y3F/fulltext/images/c3d8ba70e1df817b8c484c460a7e1cfc790c590fbd9cad8df7c833dcb25f1ecb.jpg)

![](/api/attachments/9NN32Y3F/fulltext/images/82e81c179d5b84de7d461a66d3766455ccf81479be9ec056dbd05cf355fccb85.jpg)

![](/api/attachments/9NN32Y3F/fulltext/images/71e0db285169b117e3bb8cb43628f4740868b635b033a87ba1bfd75b7e5e39e5.jpg)

![](/api/attachments/9NN32Y3F/fulltext/images/be757c33b2a889845739a7efa9fccc741e0a65637c6b814cfc825760c643499f.jpg)

![](/api/attachments/9NN32Y3F/fulltext/images/d6832547f17c5e7f20525b58880edc937690d430475a25225d6d194f2afeb233.jpg)
