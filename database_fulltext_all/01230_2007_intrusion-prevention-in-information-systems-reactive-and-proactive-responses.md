---
otero_id: 1230
otero_key: "U5VZEW3H"
title: "Intrusion Prevention in Information Systems: Reactive and Proactive Responses"
authors: "Wei T. Yue; Metin Cakanyildirim"
year: "2007"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222240110"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Intrusion Prevention in Information Systems: Reactive and Proactive Responses

Wei T. Yue & Metin Cakanyildirim

To cite this article: Wei T. Yue & Metin Cakanyildirim (2007) Intrusion Prevention in Information Systems: Reactive and Proactive Responses, Journal of Management Information Systems, 24:1, 329-353

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222240110

![](/api/attachments/U5VZEW3H/fulltext/images/ab750105deacb54cb4a87c96d960a31b9ae0c163b8627f344ac5fefeb506347a.jpg)

Published online: 08 Dec 2014.

![](/api/attachments/U5VZEW3H/fulltext/images/5a6392fc4a88635cb9e61f8ed0b01cc028906b291e308d15ac4b5e74897e759f.jpg)

Submit your article to this journal

![](/api/attachments/U5VZEW3H/fulltext/images/0c71f461221c560758c5a3afb90a73738f4dcb2f93b172e00d7fead3b9fa98e3.jpg)

Article views: 18

![](/api/attachments/U5VZEW3H/fulltext/images/f748d8da1915a5aecaf215734e785666c2ff4e7b4e65062934f4ccf2fbac082c.jpg)

View related articles

![](/api/attachments/U5VZEW3H/fulltext/images/877df1f890be7aec4438661dbb0f8fa82510cdbd95a246d42b36b2ef82fffcab.jpg)

Citing articles: 1 View citing articles

# Intrusion Prevention in Information Systems: Reactive and Proactive Responses

WEI T. YUE AND METIN ÇAKANYILDIRIM

WEI T. YUE is an Assistant Professor in Management Information Systems at the University of Texas, Dallas. He received his Ph.D. in MIS from Purdue University, West Lafayette, Indiana. His current teaching and research interests are in the areas of information security, text mining, and data mining. His work has appeared in several journals, including IEEE Transactions on Systems, Man, and Cybernetics, Electronic Markets, Information Technology and Management, and Decision Support Systems. His research won the best paper award at the Workshop on Information Technologies and Systems.

METIN ÇAKANYILDIRIM is an Associate Professor at the School of Management at the University of Texas at Dallas. He received a B.S. from Bilkent University, Turkey, an M.S. from the University of Waterloo, Canada, and a Ph.D. from Cornell University. He is a member of Informs, Production and Operations Management Society, and Institute of Industrial Engineers. His research interests include information security and risk management. He has published in various journals, including Production and Operations Management, SIAM Journal on Optimization and Control, Mathematics of Operations Research, IIE Transactions, and Naval Research Logistics.

ABSTRACT: Intrusion prevention requires effective identification of and response to malicious events. In this paper, we model two important managerial decisions involved in the intrusion prevention process: the configuration of the detection component, and the response by the reaction component. The configuration decision affects the number of alarms the firm has to investigate. It is well known that the traditional intrusion detection system generates too many false alarms. The response decision determines whether alarms are going to be investigated or rejected outright. By jointly optimizing these two decision variables, a firm may apply different strategies in protecting its informational assets: slow but accurate, rapid but inaccurate, or a mixture of the two strategies. We use the optimal control approach to study the problem. Unlike previous literature, which studied the problem with a static model, in our model, the decision on balancing the desire to detect all malicious events with the opportunity costs required to do so is time dependent. Furthermore, we show how the choice of an optimal mixture of reactive and proactive responses depends on the values of cost parameters and investigation rate parameters. We find that in our model, a high damage cost does not immediately translate to a preference of proactive response, or a high false rejection cost does not translate to a preference of reactive response. The dynamics of the problem, such as how fast alarms accumulate and how fast they can be cleared, also affect the decisions.

KEY WORDS AND PHRASES: information security, intrusion detection, intrusion prevention, intrusion response.

THE INCREASED DEPENDENCY ON INFORMATION SYSTEM resources has resulted in heightened vigilance against security breaches. An intrusion detection system (IDS) is one of the many core security technologies which firms commonly apply to provide alerts on potential security incidents [24]. An IDS captures data from the computing environment and applies detection algorithms to the data to distinguish potential attacks from regular activities. Traditionally, an IDS has operated under the setting where alerts are sent to security analysts for inspection so that proper actions are determined. However, given the prevalence of fast-paced automated attacks that we face today, such an approach has the drawback of turning security analysts into the bottleneck in the response process. Increasingly, we see a greater emphasis on the use of an intrusion prevention system (IPS). Instead of waiting for an attack to reach the target and then reacting to it, an IPS will actively block the suspicious event before it reaches the target. This approach reflects the mind-set, advocated by the security community, that we need to be more assertive in engaging attacks. In addition to automating the detection process, an IPS has the ability of automating the response process.

The most common intrusion response action involves terminating the events deemed malicious. Some other response actions include traceback, delay connection, redirect connection to decoy system, and so on [3, 22, 25, 35]. Because an IPS replicates the detection capability of an IDS and allows the users to configure the response decision, it can be considered as an extension to IDS. It is usually possible for an IPS to be configured to operate in either a reactive manner, where all of the alarms are sent to the security analysts, or in a proactive one, where all of the alarms are blocked. Naturally, the system can also be configured such that some of the alarms are responded to automatically, while the rest are sent to security analysts.

Despite allowing for rapid reaction, the main caveat of an IPS lies in the fact that its proactive response accuracy hinges on the quality of its detection engine. It has been widely cited that IDSs typically raise too many alarms on benign activities [16, 20]. As a result, a proactive response could incorrectly reject many benign events by following the recommendations of the detection engine. Such a problem is much less significant with manual investigation, where security analysts can rely on additional information to verify the event. It is true that an IDS is also subject to the false alarms. Too many alarms forces a firm to commit resources to unproductive alarm inspection, because a majority of the investigations produce false alarms. Another significant problem is that alarms may not be investigated in a timely manner, which will then produce losses even when malicious events are detected.

Because of the potential trade-offs, the choice of either a reactive or proactive response depends on several factors: (1) the accuracy of the detection system, (2) the response cost, and (3) the costs associated with correctly or incorrectly detecting benign and malicious events. Such trade-offs are typically more salient in other areas. For example, a house burglar system typically operates with high accuracy in detection (given the detection process is not very strenuous). It detects and alerts the authorities about potential intrusion, but seldom includes any response action because the cost of doing so is probably too high (how do we trap a thief?). A nuclear power plant typically has an accurate detection scheme to invoke fail-safe measures to automatically shut down internal units. Even though the cost of automatic response action is probably high, the benefits of averting a potential disastrous outcome outweigh the costs of doing so.

One major distinction with the computer environment is that the number of events is much higher and more diverse than in the other problems. The high frequency of events, of which a majority turn out to be benign, also contributes to the phenomenon of base-rate fallacy [2]; because an IDS typically monitors a large number of benign events, even when the system is configured with low probability in making errors when it comes to benign events (false alarm rate), it could still generate a high number of false alarms. The configuration of a detection system invariably depends on the false alarm rate and its counterpart—the detection rate. Imagine that if we want to catch more attackers at an airport, a detection policy could be set up in such a way that anyone who carries a sharp object is classified as an attacker. Such an approach is sensitive, because it could detect an attacker with a knife. On the other hand, it could also mistakenly classify a person with a letter opener as an attacker; therefore, it lacks specificity. Based on a series of trade-offs between the false alarm and detection rates, referred as the receiver operating characteristic (ROC) curve in the literature, the operator of the system is faced with the decision of selecting an optimal operating point.

A large number of false alarms, even when each is only introducing negligible cost, could escalate into legitimate concerns. Hence, the configuration decision in a computer-based problem is more ambiguous than in a nuclear plant problem. For instance, are we going to configure a system to detect all the attacks, at the expense of many false alarms? The answer is yes in the nuclear plant example, because the cost of not detecting all attacks involves potential irreversible damage to human health. Such a scenario would be unusual for a computer-based system. In addition, there is the question of the appropriate response. Previous work often assumes intrusion is responded to and resolved immediately when it is detected (e.g., [6, 7, 34]). While this assumption may be true with proactive response, it does not hold true with reactive response, due to the delay in response. The purpose of this paper is to develop a framework which distinguishes these two types of responses. The false alarm costs will be different under the two response types.

In the broader context, this paper studies the strategies involved in jointly optimizing detection and reaction decisions. Previous works on detection system configuration [6, 7, 34] have not discussed the role of response action in the overall protection framework, the coupled strategic implications of detection and reaction decisions, or the dynamic properties that arise from the intrusion detection decision. There have been many studies related to automated response in general information systems and security systems. De and Hsu [9] proposed an adaptive information system control framework to counter evolution in information systems. El Sawy and Nanus [10] studied the design of information systems that continue to function effectively under adverse dynamic conditions. Toth and Kruegel [33] proposed a framework to automate selecting the best response action by minimizing negative security costs; that is, damage severity and potentially adverse effects from response. Similarly, other automated response frameworks proposed mechanisms to choose the best response action [4, 21, 26]. Fisch [12] is perhaps the first to provide an intrusion response taxonomy, which later was extended by Carver and Pooch [5] to include the attacker’s degree of suspicion, the timing of the attacks, and the environmental constraints as the relevant factors for response selection. Our work differs from these previous works by also considering dynamic detection system configuration as a viable security strategy.

Our model considers the intertemporal trade-offs in making decisions. For instance, it incorporates the effects of cumulative losses incurred from intrusions (whether they are detected or not) and cumulative loss of goodwill from false rejection. We use the optimal control approach to formulate the problem and derive the dynamic optimization solutions in a finite horizon. In recent years, optimal control theory has been applied to model a variety of business problems (e.g., [15, 27]). The controls in our model are the optimal operating point configuration for the detection system, and the optimal level of proactive or reactive response. The controls dictate the paths of the state variables, which are the total number of benign and malicious events in the alarm log, the falsely rejected benign events, and the undetected malicious events. Our approach is different from the detection configuration literature, in which a static framework is assumed.

We would also like to point out that our model does not include strategic interactions between the firm and hackers. Previous studies have modeled the effects of hackers in the firm’s decisions [6, 7]. We do not consider such an effect because a firm typically interacts with a number of hackers who individually behave independently. Hence, each hacker observes the response of an organization only to his/her attacks. From such a limited observation, it is difficult for each hacker to deduce the organization’s security configuration. Without knowing the security configuration, each hacker cannot implement a strategic response to the organization’s decisions. In our view, a game theoretic model would be more appropriate when the attackers coordinate, which is more likely in the case of terrorists.

## Model of Intrusion Prevention

TYPICALLY, THERE ARE THREE MAJOR FUNCTIONS involved in an intrusion prevention framework: first, the IPS monitors and collects data on targets (acquisition); then it classifies events (detection analysis); and finally it generates a response action (reaction) [1, 11]. Our model focuses on the detection and reaction decisions. We study a problem in which a security operator is trying to determine the optimal IPS configuration and response for a fixed interval [0,T].

## Detection Configuration

We consider an environment where m events are monitored. An event monitored is either malicious or benign. Let us define

$$
p _ {m} := P (\text { A   monitored   event   is   malicious }),
$$

where P denotes the probability of an event.

All the monitored events are inspected by the detection component. The detection component will then either make a correct decision or incorrect decision for the event. We formally define the probabilities of making a correct decision on a malicious event (detection) as

$$
\begin{array}{c} u _ {_ {D}} := P (\text { Raises   an   alarm   for   the   event   at   time } t \mid \text { A   randomly   chosen } \\ \text { event   is   malicious) } \end{array}
$$

and an incorrect decision on a benign event (false alarm) to be

u := P(Raises an alarm for the event at time t | A randomly chosen event is benign).

As mentioned in the introduction, the above probabilities carry significant interpretations that are commonly used in evaluating the performance (classification accuracy) of a diagnostic system [32]. By plotting $u _ { D } ( t )$ against u(t) under various configuration settings, we obtain the trade-offs between $u _ { D } ( t )$ and u(t). This plot is commonly referred to as the receiver operating characteristic (ROC) curve. Indeed, these two probabilities are related in the following manner

$$
u _ {_ D} (t) = \Omega (u (t)), \quad t \in [ 0, T ],
$$

where Ω is an increasing concave in u, and $\Omega ( 0 ) = 0$ and $\Omega ( 1 ) = 1$

Ideally, one would like to keep u small while increasing Ω(u). But Ω is an increasing curve; therefore, u and Ω(u) increase or decrease together. Therein lies the trade-off between detection rate and false alarm rate in the configuration decision of the detection component. This type of representation between u and $u _ { p }$ provided by Ω (see Figure 1), is used to illustrate the trade-offs between $u _ { p }$ and u in many fields, such as in medical diagnosis [18]. It has also been used in evaluating the performance of classification methods [29].

Many of the recent intrusion detection studies have employed an ROC curve to evaluate the accuracy of the IDS [2, 17, 19, 37]. There are two main approaches to how the detection engine analyzes events: misuse detection and anomaly detection. Misuse detection relies on signatures to identify known attacks. The anomaly detection uses various techniques to identify abnormal activity. We assume the ROC curve Ω to be given,<sup>1</sup> and Ω is fixed in our problem.<sup>2</sup> Similar to recent studies [6, 7, 34], “configuring a detection system” refers to making the choice of u.

## Alarm Response

While it is true that an IPS can be equipped with different types of response actions, we limit our discussion to two common types of responses: event termination (proactive) and security operator alerting (reactive). We determine the optimal mixture of proactive and reactive responses. We denote by $\nu ( t ) \in [ 0 , 1 ]$ the portion of alarms handled by the proactive response. The reaction decision depends on the configuration decision $u ,$ as the latter dictates the volume of alarms and hence how soon those alarms can be investigated, given the fixed investigation rate. Thus, we jointly optimize the controls u and v for the problem.

![](/api/attachments/U5VZEW3H/fulltext/images/8e113121ff433bb5be50987ba5f6cad9d7af813e433273ac8a63a9123fa8f096.jpg)  
Figure 1. The ROC Curve

Based on the control decisions, six potential states arise: a benign (malicious) event is correctly (falsely) classified, a benign (malicious) event is falsely (correctly) classified and blocked, a benign (malicious) event is falsely (correctly) classified and introduced as an alarm. We assume that the correctly detected and blocked malicious events and the correctly classified benign events lead to zero cost. Thus, there are four state variables to consider. Figure 2 summarizes the intrusion prevention process. One could think of a more general problem in which the automated response is to delay events instead of terminating them. Then, the state of correctly delaying an event also becomes relevant in determining the optimal decisions in such a case.

The numbers of benign and malicious events present in the alarm log, $x _ { b } ( t )$ and $x _ { _ m } ( t )$ change when alarms are introduced into the log and when alarms are resolved. The number of alarms in the log is $x ( t ) : = x _ { b } ( t ) + x _ { m } ( t )$ . Because the rate of benign events is $m ( 1 - p _ { m } )$ and the rate of false alarms is $m ( 1 - p _ { { } _ { m } } ) u ,$ the proactive response blocks v portion of these alarms. Benign events arrive to the alarm log at a rate of

$$
m (1 - p _ {m}) (1 - v) u
$$

and malicious events arrive at a rate of

$$
m p _ {m} (1 - v) \Omega (u).
$$

We assume that existing alarms due to the benign and malicious events are processed at rates of $0 \leq k _ { \scriptscriptstyle b } ( t ) \leq 1$ and $0 \leq k _ { _ m } ( t ) \leq 1$ , respectively. The number of alarms being processed at t is proportional to x given that duplicate entries can occur. We often see duplicate entries in the alarm logs because different events can correspond to the same incident. For instance, an ongoing activity continues to cause alarms until it is halted, or an activity can trigger different sensor rules and generate multiple entries in the alarm log. Hence the security operators address the underlying security incidents during investigation rather than the individual event. Therefore, more alarms are processed with higher $k _ { b }$ and $k _ { _ m } .$ For simplicity, we assume the clearance rate for the benign events in the alarm log to be

![](/api/attachments/U5VZEW3H/fulltext/images/e190145632b737645e6ab749855e012d52ed75c2d6c430f4ac4995bb7db199aa.jpg)  
Figure 2. An Intrusion Prevention Architecture: Control and State Variables

$$
k _ {b} x _ {b}.
$$

The malicious events are assumed to cause instantaneous damage when their true status is unknown. However, once a malicious event is confirmed after investigation, the security operators will then be able to resolve the problem without delay. We assume security operators do not make mistakes in the investigation. Moreover, a compromised system often shows visible signs of attack, such as system failure and irregular traffic pattern, which can be observed by the system users. In addition to uncovering attacks through investigation, security operators may also observe symptoms from malicious activity and thereby determine a proper reaction to an incident.

The clearance rate for malicious events is

$$
(k _ {m} + r) x _ {m},
$$

where $0 \leq r \leq 1$ denotes the realization rate of malicious activity. Summing up the arrival and clearance rates, the rate of change of the benign events in the alarm log is

$$
\dot {x} _ {b} = m (1 - p _ {m}) (1 - v) u - k _ {b} x _ {b}, \quad x _ {b} (0) = x _ {b 0} \geq 0\tag{1}
$$

and the rate of change of the malicious events in the alarm log is

$$
\dot {x} _ {m} = m p _ {m} (1 - v) \Omega (u) - (r + k _ {m}) x _ {m}, \quad x _ {m} (0) = x _ {m 0} \geq 0.\tag{2}
$$

We assume that when a proactive response is used, it is fully automated; hence there is no human intervention in the process. In case of a benign event rejection, when it is falsely classified by the detection component as malicious (false rejection), a security analyst intervention does not occur until the system is up for maintenance, that is, after T. Thus, the number of falsely rejected events only increases during the planning horizon, at a rate which can be written as

$$
\dot {z} _ {b} = m (1 - p _ {m}) v u, \quad z _ {b} (0) = z _ {b 0} \geq 0.\tag{3}
$$

Not all malicious events are detected by the IPS. Depending on the configuration level, some malicious events could be misdetected and treated as benign events. We denote the number of such events as y(t), and it increases at a rate of

$$
m p _ {m} (1 - \Omega (u)),
$$

where some undetected attacks could be detected naturally. The number of misdetected malicious events changes at a rate of

$$
\dot {y} = m p _ {m} (1 - \Omega (u)) - r y, \quad y (0) = y _ {0} \geq 0.\tag{4}
$$

Note that when attacks are realized and reacted upon, it does not overturn the system’s decisions. The alarms are either already in the alarm log or simply ignored by the system. The removal of those incidents would not alter the system configuration. Moreover, $x _ { b } , x _ { m } , z _ { b } ,$ and y will remain to be nonnegative given that the nonnegative initial values are assumed, that is, $x _ { _ { b 0 } } > 0 , x _ { _ { m 0 } } > 0 , z _ { _ { 0 } } > 0$ , and $y _ { 0 } > 0$ . Table 1 lists the important variables of the model.

## Optimal Control of Detection and Response

THE MAIN OBJECTIVE OF THE PROBLEM IS TO DETECT and react to as many malicious events as possible, while at the same time limit false classification and false rejection of benign events.

By choosing the optimal controls, we minimize the security costs related to (1) benign event investigation; (2) unresolved malicious events; (3) false rejection of benign events; (4) undetected malicious events; and (5) the terminal costs related to investigation, false rejection, and misdetection at terminal time. To simplify the model, we assume these costs increase linearly with the respective event numbers [6, 7, 34]. More precisely, the problem can be expressed as

$$
\begin{array}{c} \min _ {u, v} \int_ {0} ^ {T} \left\{k _ {b} x _ {b} c + x _ {m} d + z _ {b} a + y d \right\} d t + S _ {x _ {b}} (x _ {b} (T), T) \\ \qquad + S _ {z _ {b}} (z _ {b} (T), T) + S _ {y} (y (T), T) \end{array}\tag{5}
$$

subject to state evolution constraints given in (1), (2), (3), and (4). Based on the evolution of the state variables, we can compute the total costs for the entire planning horizon, where $c , a ,$ and d correspond to investigation, false rejection, and damage costs per specific event. At time T, all alarms are investigated; the benign events yield terminal cost $S _ { x _ { b } } ( x _ { b } ( T ) , T )$ , and malicious events result in zero cost. The malicious events not detected, on the other hand, continue to cause damage at time T; that is, $S _ { \mathrm { v } } ( y ( T ) , T )$ . Similarly, the falsely rejected events cost is $S _ { z _ { b } } ( z _ { b } ( T ) , T )$

Table 1. Important Notations

<table><tr><td></td><td>Notations</td><td>Descriptions</td></tr><tr><td rowspan="5">Input parameters</td><td>m</td><td>Rate of event arrival to the IPS</td></tr><tr><td>r</td><td>Realization rate of malicious events</td></tr><tr><td> $k_m$ </td><td>Investigation rate of malicious events</td></tr><tr><td> $k_b$ </td><td>Investigation rate of benign events</td></tr><tr><td>Ω</td><td>Receiver operating characteristic (ROC) curve</td></tr><tr><td rowspan="2">Control variables</td><td>u(t)</td><td>IDS configuration, that is, false alarm rate</td></tr><tr><td>v(t)</td><td>Proportion of traffic responded to with proactive approach</td></tr><tr><td rowspan="4">State variables</td><td> $x_b(u, v, t)$ </td><td>Number of benign events in the alarm log</td></tr><tr><td> $x_m(u, v, t)$ </td><td>Number of malicious events in the alarm log</td></tr><tr><td>y(u, v, t)</td><td>Number of nonrealized malicious events not in the alarm log</td></tr><tr><td> $z_b(u, v, t)$ </td><td>Number of benign events blocked by the IDS</td></tr></table>

We solve the problem by using the Pontryagin maximum principle; the Hamiltonian function can be written as

$$
\begin{array}{c} H = k _ {b} x _ {b} c + (x _ {m} + y) d + z _ {b} a + \lambda_ {1} \left(m (1 - p _ {m}) (1 - v) u - k _ {b} x _ {b}\right) \\ + \lambda_ {2} \left(m p _ {m} (1 - v) \Omega (u) - (r + k _ {m}) x _ {m}\right) + \lambda_ {3} \left(m p _ {m} (1 - \Omega (u)) - r y\right) \\ + \lambda_ {4} \left(m (1 - p _ {m}) v u\right). \end{array}\tag{6}
$$

The optimality conditions for the adjoint variables are

$$
\dot {\lambda} _ {1} = \frac {\partial H}{\partial x _ {b}} = k _ {b} c - \lambda_ {1} k _ {b}, \quad \lambda_ {1} (T) = S _ {x _ {b}} (x _ {b} ^ {*} (T), T)\tag{7}
$$

$$
\dot {\lambda} _ {2} = \frac {\partial H}{\partial x _ {m}} = d - \lambda_ {2} (r + k _ {m}), \quad \lambda_ {2} (T) = 0\tag{8}
$$

$$
\dot {\lambda} _ {3} = \frac {\partial H}{\partial y} = d - \lambda_ {3} r, \quad \lambda_ {3} (T) = S _ {y} \left(y ^ {*} (T), T\right)\tag{9}
$$

$$
\dot {\lambda} _ {4} = \frac {\partial H}{\partial z _ {b}} = a, \quad \lambda_ {4} (T) = S _ {z _ {b}} (z _ {b} ^ {*} (T), T).\tag{10}
$$

The adjoint variables $\lambda _ { { \scriptscriptstyle 1 } } , \lambda _ { { \scriptscriptstyle 2 } } , \lambda _ { { \scriptscriptstyle 3 } } ,$ and $\lambda _ { _ 4 }$ are interpreted as the marginal costs corresponding to an additional unit $o f \colon$ a benign event in the alarm log, a malicious event in the alarm log, an undetected event, and a falsely rejected benign event. Because H is linear in all the state variables and convex and control variables, the solutions derived from $( 7 ) ‐ ( 1 0 )$ are optimal. In the extreme response cases, we have (1) reactive approach, where $\nu = 0$ for the entire horizon; and (2) proactive approach, where $\nu =$

1 for the entire horizon. Before we examine the general problem, where a mixture of reactive and proactive responses can be used, we first study the extreme cases.

Reactive response: In the reactive response case, false rejection does not occur, hence $\lambda _ { _ 4 }$ does not appear in the problem. Given the terminal conditions, the adjoint variables can be derived. Note, from (8) and (9), we can conclude that the marginal cost of an additional undetected event will always be higher than the marginal cost of an additional detected malicious event. That is, $\lambda _ { 3 } ( t ) \geq \lambda _ { 2 } ( t )$ for all t, because $\lambda _ { 3 } ( t )$ has a lower clearance rate $k _ { { _ m } }$ but higher terminal costs (greater than zero).

The Hamiltonian is linear convex in u, when $\nu = 0$ . The optimal control must satisfy $\partial H / \partial u = 0 ;$ from this we can derive the optimal control $u ^ { * }$ .

Proposition 1: In the reactive response case $( \nu = O )$ , the optimal configuration level of the detection component is

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} 0 & \text { if } \Psi (0) \geq \Theta (t) \\ \Psi^ {- 1} (\Theta (t)) & \text { if } \Psi (0) <   \Theta (t) <   \Psi (1) \\ 1 & \text { if } \Theta (t) \geq \Psi (1), \end{array} \right.\tag{11}
$$

$$
\text { where } \Psi = \Omega^ {\prime} (\cdot), \text { and } \Theta (t) = ((1 - p _ {_ m}) \lambda_ {_ 1} (t)) / (p _ {_ m} (\lambda_ {_ 3} (t) - \lambda_ {_ 2} (t))).
$$

Because $\Omega ^ { \prime }$ is decreasing with $u ^ { * }$ , an increase in Θ will decrease $u ^ { * }$ . Proposition 1 states $u ^ { * }$ decreases with the increase in $\lambda _ { \parallel } ( t )$ , and increases with $\lambda _ { 3 } ( t ) - \lambda _ { 2 } ( t )$ , and $p _ { m } .$ Because the cost trade-offs are expressed in a marginal sense, we need to solve the adjoint variables to see the underlying cost trade-offs. The general results are intuitive in that we set the detection component to a stricter level when the damage cost is high, when there are many malicious events, and when investigation cost is low. However, one interesting distinction from previous results (e.g., [6, 7, 34]) is that the system is not configured strictly based on the damage arising from misdetection in our model. When we consider the problem in a dynamic framework, the damage cost arising from a detected malicious event in the alarm log has to be considered as well. This poses an interesting problem in that we may also want to lessen the configuration level when the damage cost resulting from a detected malicious event is high. This is because when the detected malicious event cannot be investigated and resolved quickly, we might as well introduce fewer alarms so that less investigation effort is wasted on the benign events.

Proactive response: In the proactive case, we set $\nu = 1$ . Unlike the reactive case, $\lambda _ { \scriptscriptstyle 1 } ( t )$ and $\lambda _ { 2 } ( t )$ do not affect the configuration decision because all the detected events are blocked. However, the effect from falsely rejected benign events rise, that is, $\lambda _ { 4 } ( t )$ Again, we can derive $u ^ { * }$ by differentiating the Hamiltonian with respect to u and by setting it to equal to zero.

Proposition 2: In the proactive case $( \nu = I )$ , the optimal configuration level of the detection component is

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} 0 & \text { if } \Psi (0) \geq \Phi (t) \\ \Psi^ {- 1} (\Phi (t)) & \text { if } \Psi (0) <   \Phi (t) <   \Psi (1) \\ 1 & \text { if } \Phi (t) \geq \Psi (1), \end{array} \right.\tag{12}
$$

where $\Psi = \Omega ^ { \prime } ( \cdot ) , \mathrm { a n d } \Phi ( t ) = ( ( 1 - p _ { m } ) \lambda _ { 4 } ( t ) ) / ( p _ { m } \lambda _ { 3 } ( t ) ) .$

The configuration level increases with $\lambda _ { \scriptscriptstyle 3 } ( t )$ and $p _ { { } _ { m } } ,$ , but decreases with $\lambda _ { 4 } ( t )$ . In this case, the cost trade-off is between damage costs and false rejection costs. Although this case is similar to using a static model, the actual trade-offs change over time, given that both of these costs are cumulative and they are affected by other parameters.

Proactive and reactive response: We now consider the case in which both proactive and reactive response can be used. Because Equation (6) is linear with v, we have a bang-bang—that is, 0 or 1 decision—when it comes to response decision.

Proposition 3: (a) In the hybrid response case, the optimal response is either fully proactive $\nu ( t ) = I$ or fully reactive $\nu ( t ) = 0 . \ ( b )$ The corresponding optimal configuration is

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} 0 & \text { if } \Psi (0) \geq \Theta (t) \\ \Psi^ {- 1} (\Theta (t)) & \text { if } \Psi (0) <   \Theta (t) <   \Psi (1) \\ 1 & \text { if } \Theta (t) \geq \Psi (1), \end{array} \right.\tag{13}
$$

$$
\text { where } \Theta (t) = ((1 - p _ {m}) ((1 - v) \lambda_ {1} (t) + v \lambda_ {4} (t))) / (p _ {m} (\lambda_ {3} (t) - (1 - v) \lambda_ {2} (t))).
$$

Proposition 3 states that alarms are either all sent for inspection or are all rejected at any given time t. Depending on the response decision, a corresponding configuration level is selected. From Equation (A2) of the Appendix, it can be seen that $\lambda _ { 4 } ( t )$ will be higher than $\lambda _ { \parallel } ( t )$ when the reactive response is selected, which indicates the cost of false rejection is significant relative to the investigation cost when the reactive response is selected. Furthermore, a higher $\lambda _ { _ 2 } ( t )$ increases the chances of using the proactive approach. Thus, the proactive response is more preferred when a malicious event in the alarm log is more costly. Because marginal cost changes over time, it is possible to envision a scenario in which $\lambda _ { 4 } ( t )$ is greater than $\lambda _ { \parallel } ( t )$ initially, but eventually becomes much less than $\lambda _ { _ { 1 } } ( t ) ;$ therefore, the optimal response would switch from reactive response to proactive response at some $t \in [ 0 , T ]$ . We will later examine the different scenarios where different optimal configuration and response strategies are adopted.

To further develop our results, similar to the curve assumed in [7], we use an ROC curve: $\Omega ( u ) = u ^ { 0 . 5 }$ . In addition, we assume that the terminal conditions are $S _ { x _ { b } } ( x _ { b } ^ { \ * } ( T ) , T ) =$ $c x _ { b } ( \mathrm { T } ) , S _ { x _ { m } } ( x _ { m } ^ { ~ * } ( T ) , T ) = 0 , S _ { \mathrm { v } } ( { \boldsymbol y } ^ { * } ( T ) , T ) = d _ { \mathrm { v } } ( T )$ , and $S _ { z _ { b } } ( z _ { b } ^ { * } ( T ) , T ) = a z _ { b } ( T )$ . The adjoint variables can be expressed in explicit forms:

$$
\lambda_ {1} = c\tag{14}
$$

$$
\lambda_ {2} = \frac {d}{k _ {m} + r} \Big (1 - e ^ {- (k _ {m} + r) (T - t)} \Big)\tag{15}
$$

$$
\lambda_ {3} = \frac {d}{r} (1 - (1 - r) e ^ {- r (T - t)})\tag{16}
$$

$$
\lambda_ {4} = a (1 - t + T).\tag{17}
$$

Substituting the adjoint variables into Equations (11) and (12) allows us to make further observations.

Proposition 4: (a) When $\nu = 0$ is applied for the entire horizon, u<sup>\*</sup> is nondecreasing over the entire horizon if the realization rate is larger than or equal to certain threshold level $r ^ { c } ,$ , where $r ^ { c } = { \cal { I } } - e ^ { - k _ { m } T } .$ (b) When the realization rate is lower than the threshold level, $r < r ^ { c }$ , u<sup>\*</sup>(t) decreases during the horizon, but increases when approaching T.

When attacks are often observable through system behavior, the firm can detect many attacks naturally and obtain a higher realization rate. Hence, when the realization rate is higher than a certain threshold level, $r > r ^ { c }$ , the best strategy is to increase the detection level over the entire horizon as a future detected malicious event has lower marginal cost. The threshold level $r ^ { c }$ depends on $k _ { { _ m } }$ and $T .$ On the contrary, when $r \leq$ $r ^ { c } ,$ alarms are allowed to build up first with strict configuration, but the configuration is gradually being relaxed until the end of the horizon, where it becomes stricter again. Due to the terminal conditions, configuration levels increase at the end of the horizon for any r values. However, the two cases describe very different configuration approaches for the majority of the horizon.

We know that at $t = 0 , \lambda _ { * } ( t ) - \lambda _ { * } ( t )$ is the lowest in the reactive response case. Hence, if the optimal $u ^ { * }$ turns out to be 1 at $t = 0$ , we know that $u ^ { * } = 1$ is used for the entire horizon. Note that because $\lambda _ { * } ( t ) - \lambda _ { * } ( t )$ is always positive, and m and $\boldsymbol { p } _ { m }$ are nonzero and $\begin{array} { r } { \lambda _ { 3 } ( t ) - \lambda _ { 2 } ( t ) = c , } \end{array}$ , the case in which we do not raise alarms, that is, $u ^ { * } ( t ) = 0$ , does not occur.

## Numerical Analysis

IN THIS SECTION, WE CONDUCT NUMERICAL ANALYSIS to generate further insights into the optimal control strategies. In addition, we study the sensitivity of optimal response by changing the value of a parameter while keeping other parameters fixed. Our examples assume a planning horizon of 10 days $( T = 1 0 )$ . We use discrete time instances of $\Delta t = 0 . 0 1$ . There are 100,000 events monitored by the IPS each day. One percent of the monitored traffics are assumed to be malicious, that is, ${ p _ { \scriptscriptstyle m } } = 0 . 0 1$ . Each malicious event, whether it is undetected or detected but waiting in the log, would result in losses of \$100 per time, $d = 1 0 0$ . Furthermore, the realization rate of malicious events is 0.05 percent $( r = 0 . 0 0 0 5 )$ , and the benign event investigation rate is 0.5 percent $( k _ { b } = 0 . 0 0 5 )$ .

In the numerical examples, we approximate the derivative of the state variable values at t by substituting

$$
\frac {\Delta x _ {b}}{\Delta t} = \frac {x _ {b} (t + \Delta t) - x _ {b} (t)}{\Delta t}
$$

for $\dot { x } _ { b }$ [27]. We compute the optimal controls by searching for the best values. With the optimal controls, we compute the total costs accumulated over the horizon using Equation (5).

## Static Configuration

In addition to presenting the numerical results using our model, we also solve the static model and use it as the baseline case in our discussion. In the static case, the optimization process does not include state variables. We write the cost function as

$$
T C = m (1 - p _ {m}) (1 - v) u c + m (1 - p _ {m}) v u a + m p _ {m} (1 - \Omega (u)) d.\tag{18}
$$

Note that the only difference between proactive and reactive response in the static case is the cost incurred with false alarms—that is, a versus c. The interior optimal solutions for the respective models are presented in Table 2. Using the static solutions, we can compute the total cost (denoted as $J _ { \it { s } } )$ and the state variables over the planning horizon.

## Optimal Configuration and Response

We construct four numerical cases to show different optimal behaviors. The parameter values and results of the examples are summarized in Table 3.

## Case i: Reactive Response

We consider a case in which the false rejection cost is much higher than the investigation cost $( a \geq c )$ . As a result, a reactive response is adopted for the entire horizon; see Figure 3. Because the realization rate r is lower than the threshold level $r ^ { c } ,$ the configuration path first drops but increases near the end of horizon (as discussed in Proposition 4b). As shown in Figure 4, there is an initial buildup of benign events in the alarm log; that is, $\dot { x } _ { b }$ is positive initially but becomes negative later on. Detected malicious events $x _ { { _ m } }$ are also introduced and removed over time, but because the realization and investigation rates (r and $k _ { { _ m } } )$ are small, $\dot { x } _ { _ { m } }$ continue to increase until $T ,$ albeit at a slower rate. The lenient configuration also causes a higher number of undetected malicious events.

Compared to the static configuration, the dynamic model requires a higher configuration initially, but shifts to a slightly lower configuration level near the end of the horizon. The dynamic model allows the flexibility of stricter configuration initially and more lenient configuration later. It results in 4.82 percent savings in cost. We see a strategy which focuses on detecting “more” alarms initially and shifting to emphasizing “timely” investigation later on as alarms start to build up. Applying the static model would fail to utilize the alarms accumulation strategy, because underconfiguration occurs for the majority of the time.

Table 2. Interior Solutions for the Static Models

<table><tr><td></td><td>Reactive</td><td>Proactive</td><td>Hybrid</td></tr><tr><td> $u^{*}$ </td><td> $\left( \frac{p_{m}d}{2(1-p_{m})c} \right)^{2}$ </td><td> $\left( \frac{p_{m}d}{2(1-p_{m})a} \right)^{2}$ </td><td> $\left( \frac{p_{m}d}{2(1-p_{m})(1-v)c+va} \right)^{2}$ </td></tr><tr><td> $v^{*}$ </td><td>0</td><td>1</td><td>1 if  $a \leq c$ 0 if  $a > c$ </td></tr></table>

Table 3. Numerical Solutions

<table><tr><td></td><td>Case i</td><td>Case ii</td><td>Case iii</td><td>Case iv</td></tr><tr><td colspan="5">Parameters</td></tr><tr><td>c</td><td>1</td><td>1.5</td><td>1</td><td>0.5</td></tr><tr><td>a</td><td>5</td><td>1</td><td>2</td><td>2</td></tr><tr><td> $k_m$ </td><td>0.0005</td><td>0.002</td><td>0.0005</td><td>0.0001</td></tr><tr><td colspan="5">Performance</td></tr><tr><td>J</td><td> $3.7884 \times 10^6$ </td><td> $2.6308 \times 10^6$ </td><td> $3.7030 \times 10^6$ </td><td> $3.8568 \times 10^6$ </td></tr><tr><td> $J_S$ </td><td> $3.9711 \times 10^6$ </td><td> $3.3754 \times 10^6$ </td><td> $3.9711 \times 10^6$ </td><td> $4.1359 \times 10^6$ </td></tr><tr><td> $Σx_b$ </td><td> $8.88 \times 10^5$ </td><td> $8.41 \times 10^5$ </td><td> $4.32 \times 10^5$ </td><td> $2.42 \times 10^5$ </td></tr><tr><td> $Σx_m$ </td><td>28,394</td><td>26,861</td><td>13,479</td><td>3,761.8</td></tr><tr><td>Σy</td><td>9,481</td><td>10,697</td><td>20,823</td><td>30,858</td></tr><tr><td> $Σz_b$ </td><td>0</td><td>7,407.9</td><td> $1.36 \times 10^5$ </td><td> $1.98 \times 10^5$ </td></tr></table>

## Case ii: Reactive-Proactive Response

In this case, the false rejection cost is lower than the investigation cost $( a < c )$ . Hence, the “false rejection–investigation” a/c is much lower in this case when compared to Case i. As a result, the proactive response is more attractive. However, the investigation rate for malicious events $k _ { { _ m } }$ is also higher in this case, which generally results in the use of the reactive response to be more effective. As illustrated in Figure 5, reactive response with strict configuration is applied in the early periods. $\mathrm { A t } t = 4 . 2 3$ the optimal response switches from reactive to proactive.

We see a similar strategic pattern to Case i, that is, alarms are accumulated early on. Instead of slowing down alarm introductions over time, in this case a halt in alarm introduction occurs with a switch to the proactive response. Because no alarms are introduced when the proactive response is used, the number of alarms (benign and malicious) begins to decrease. The configuration level increases gradually under the proactive response, resulting in an accumulation of falsely rejected benign events.

![](/api/attachments/U5VZEW3H/fulltext/images/0310861af4acc804ff341e0e636c00671a8a8600cb22d13a6de5847822fc8f6d.jpg)  
Figure 3. Case i—Optimal Controls

![](/api/attachments/U5VZEW3H/fulltext/images/15dba34d4a4f01253b81a1311719007a7ade803d07bdd9b9ba916d61bcd35f39.jpg)  
Figure 4. Case i—State Variables

![](/api/attachments/U5VZEW3H/fulltext/images/0165f91e8008f4c29962cebd85fd54ad4599f26ccf2e609ea7f0d0243b339fd3.jpg)  
Figure 5. Case ii—Optimal Controls

Although the configuration level continues to rise, the number of undetected events continues to rise because of low realization rate (see Figure 6).

This case shows that not only can we use the configuration level to control inflows of alarms when too many alarms are accumulated (as in Case i), but a proactive response can also be used to curb the inflow of alarms. With the static model, a reactive response is optimal, but it does not allow alarms to first build up and to be investigated later. Overall, it yields 28.3 percent more in costs.

It is easy to imagine a case in which the system goes through a period of proactive response where alarms are cleared, only to switch back to a reactive approach afterward. We see such a scenario in Case iii.

## Case iii: Reactive-Proactive-Reactive Response

We now consider a case in which the false rejection cost is higher than the investigation cost $( a > c )$ , but not at the level seen in Case i. In addition, the investigation rate $( k _ { _ m } )$ is the same as in Case i. As illustrated in Figures 7 and 8, we observe a slightly different configuration and response structure in this case. Similar to the previous two cases, alarms are initially accumulated, and the alarm inflow is slowed down or halted afterward. Unlike the previous two cases, alarms are allowed to accumulate again after the decline.

Even though in this case the “false rejection-investigation” cost ratio (a/c) is higher than that in Case ii, we do not necessarily see a less proactive response. This is because the investigation rate $( k _ { _ m } )$ is much lower in this case, making a reactive response less attractive. The high cost of false rejection would eventually generate a high enough cumulative false rejection cost to again warrant the use of a reactive response. Overall, the total cost is 7.24 percent higher in the static model.

## Case iv: Proactive-Reactive Response

In this case, the false rejection cost is also much larger than the investigation cost (as in Case i), but the malicious event investigation rate $( k _ { _ m } )$ is lower. A proactive response is selected initially, but then a reactive response is used later. Even though the “false rejection-investigation” cost ratio (a/c) is relatively high in this case, a reactive response is not initially optimal because of the low investigation rate. A reactive response becomes optimal when falsely rejected events accumulate (see Figures 9 and 10). Note that with a low investigation rate, a proactive response will be used for the entire horizon when a/c is low.

The optimal static configuration is such that all events are classified as malicious and investigated over the entire horizon. Using the static model results in overconfiguration for most of the horizon. The reason behind such a strict configuration level is that the “investigation-damage” cost ratio (c/d) is low. It is thus better to classify all events as malicious and investigate all of them. Such an approach cannot be used for the entire horizon in the dynamic model because the investigation rate is low; it would generate too many malicious events in the alarm log, which would result in many of the alarms not being investigated until T. In comparison, the static model results in 7.23 percent higher total cost.

![](/api/attachments/U5VZEW3H/fulltext/images/cf7ee0a9bd929f9aa6ba38175f14d527a30d20a4a35da4219e4fc164beca7ca3.jpg)  
Figure 6. Case ii—State Variables

![](/api/attachments/U5VZEW3H/fulltext/images/a17f4f6f226471c5a4578c7d620a07b40050f39b0d1608767c0ef16701721253.jpg)  
Figure 7. Case iii—Optimal Controls

![](/api/attachments/U5VZEW3H/fulltext/images/b358ecc21a1f9e9c6ec049632120c5ae2f2e36a1e93a05bac1207d52be59983f.jpg)  
Figure 8. Case iii—State Variables

![](/api/attachments/U5VZEW3H/fulltext/images/862589cd36b3effa52b6088fe4be834509a410ef31cc7642f6993fdc1ba7d76a.jpg)  
Figure 9. Case iv—Optimal Controls

![](/api/attachments/U5VZEW3H/fulltext/images/7fb3453fdcf9987b6d731fd06fa98eb65304994d467c05e62efcd72adb6ed209.jpg)  
Figure 10. Case iv—State Variables

## Sensitivity Analysis

We now study the proportion of time in which proactive response is used over the planning horizon by changing the value of a parameter while holding all other parameters constant. The baseline values are $c = 1 , a = 2 , k _ { { } _ { m } } = 0 . 0 0 1$ . We observe either an increasing concave curve or a decreasing concave curve in the usage of a proactive response with respect to all parameters, except with r. The sensitivity analysis results are summarized in Table 4. To illustrate, Figures 11 and 12 show the results with different c and r values.

Table 4. Sensitivity Analysis on Proactive Response Usage

<table><tr><td>Increase in Parameter Values</td><td>Proactive Response Usage</td></tr><tr><td>Investigation cost (c)</td><td>+</td></tr><tr><td>False rejection cost (a)</td><td>-</td></tr><tr><td>Damage cost (a)</td><td>+</td></tr><tr><td>Malicious event investigation rate ( $k_m$ )</td><td>-</td></tr><tr><td>Realization rate (r)</td><td>+/-</td></tr><tr><td>ROC curve parameter ( $\alpha$ )</td><td>-</td></tr><tr><td>Malicious traffic proportion ( $p_m$ )</td><td>+</td></tr></table>

![](/api/attachments/U5VZEW3H/fulltext/images/ca016b955a6b933cf7fb8d6e37fff9c5b84b392db55cdc45f54aeccd17a886ce.jpg)  
Figure 11. Proactive Response Usage as c Varies

![](/api/attachments/U5VZEW3H/fulltext/images/a8d46839eea831eb9e162c334621484b7deb5b1cb3e6f204e0f0aa587e63e306.jpg)  
Figure 12. Proactive Response Usage as r Varies

Predictably, an increase in c and $p _ { { } _ { m } }$ results in an increased usage of a proactive response. Increasing $\boldsymbol { p } _ { \boldsymbol { m } }$ has a similar effect to reducing the false rejection cost per event $^ { a ; }$ it is clear that an increase in a reduces the use of a proactive response.

In terms of $d ,$ we initially see a sharp rise in proactive response usage as d increases. However, the increase slows down significantly after a certain threshold level, but a complete use of a proactive response $\nu = 1$ does not occur until d becomes very large. The reason why a reactive response is still in use, even when d is very large, is because cumulative damage costs will be low near the end of the horizon with a reasonable investigation rate.

We specify the ROC function to be $\Omega ( u ) = u ^ { \alpha }$ and observe the effects by varying α. With a smaller α value, the classification decision by the system is likely to be correct. Therefore, the use of a proactive response is more favorable with a smaller α value. There is a sharp drop in proactive response use when α is greater than a certain threshold value, indicating that common proactive response usage requires confidence in classification accuracy.

We observe that an increase in small r values results in a higher proactive response usage. However, after a certain r value, the opposite effect—greater use of a reactive response—occurs. It is clear that a reactive response becomes more attractive as r becomes larger, because a higher alarm clearance rate allows a timely response to malicious events. Interestingly, when r is small, increasing r could actually complement proactive response due to the fact that undetected alarms can be discovered quickly. Because a typical proactive response is associated with a lenient configuration level, a quick resolution on undetected alarms introduces significant effect.

The variable $k _ { { _ m } }$ has similar effect as r. Higher $k _ { { _ m } }$ means alarms clear at a faster rate, making a reactive response more attractive. The difference is that $k _ { _ m }$ only affects the events in the alarm log. Because a proactive response does not introduce events into the alarm log, higher values of $k _ { { _ m } }$ do not promote a proactive response.

## Findings from Numerical Analysis

We found that a reactive response is typically applied with a higher detection rate, compared to a proactive response. Thus, a reactive response is deemed to be more accurate in identifying attacks. On the other hand, it delays reaction. Because a proactive response allows for immediate termination of classified events, it is effective only when the configuration level is low or the distinction power of the detection system is high. The configuration and response strategies arising from these two approaches are slow but accurate and rapid but inaccurate. In a way, the trade-offs lie upon whether we want to not delay reaction or to increase accuracy.

In a planning horizon, these two strategies could be applied individually or interchangeably to best manage the situation. For instance, we first follow a reactive response with a high configuration, and we later apply an active response with a lower configuration level to have the best of both speed and accuracy in dealing with malicious events. Furthermore, we could first stress accuracy, given that we have the luxury of an empty alarm log initially, and then move to a proactive response so that we can address the current alarms accurately while using the fast but inaccurate approach to deal with new alarms. By doing so, essentially two levels of protection strategies are used in dealing with alarms. These insights would not be possible in a static model.

Even though the sensitivity analysis results are intuitive for most of the parameters, the results for damage cost and realization rate are interesting. Higher damage costs lead to more frequent use of a proactive response; however, there is always incentive to introduce some alarms near the end of the period because the cumulative damage would be small. A higher realization rate could increase the use of both the proactive and reactive responses. Higher r facilitates the use of a proactive response because it reduces losses from undetected alarms. However, when r is significantly large, it contributes to loss reduction due to investigation delays, and it makes a reactive response more effective.

## Conclusions and Limitations

WE PRESENTED AN ANALYTICAL MODEL TO STUDY the key decisions involved in the intrusion prevention process. Clearly, many practical issues are not addressed here. For instance, how do we estimate the prior probabilities, or how do we estimate the cost factors? Given that information security is an emerging subject in the business context, these are the real questions that security practitioners may not necessarily have clear answers to at the moment. IT security risk management practice is one area which we think would emerge to address many of these questions for firms [23, 30]. Furthermore, the business process or organizational control framework [28] is also important. In recent years, more and more security-related data have been collected, from cyber crime figures [13] to hackers’ techniques and behaviors (e.g., The Honeynet Project; www. honeynet.org); that data would also help us in better quantifying information security variables. In addition, security metrics are being developed to facilitate understanding of the type of meaningful data needed in making security decisions [31].

One important assumption made in this paper is that the classification accuracy of the detection component does not change over the planning horizon. The performance shift in a classification system is an important issue and it should be considered in future studies, where we need to study the timing of the maintenance effort and the level of maintenance effort to counter deterioration in accuracy. Also, we need to define how deterioration occurs in a system. Those issues, while interesting, would introduce considerable complexity into the model. We limit ourselves from discussing those issues to keep the focus on configuration and response decisions.

In a way, our results are driven by the assumptions that cost factors are known and losses are cumulative. In practice, false rejection cost may be an unknown variable, which calls for the attention of the security operators. Attack losses may not be cumulative; for example, stolen confidential information could be a one-time loss. We acknowledge that our model may not address all the issues. Furthermore, an intrusion prevention system typically encounters multiple classes of attacks. Introducing multiple types of alarms would make the problem richer, but requires us to consider additional issues, such as how to decide which alarms to be investigated first. Nevertheless, from our results we learned what actions to take for any given class of attack.

One issue that we have not discussed in detail is hackers’ behavior. If a hacker knows the configuration of the response system over a time horizon, he or she can choose his attack intensity over that horizon, such as attacking more when the configuration is relaxed. However, hackers generally do not know the configuration of the response system. Therefore, they have to deduce the configuration of the system from whatever data they observe. The more data that are available to a hacker, the more accurate this deduction will be. Fortunately, the data that a single hacker can gather are often limited to the responses (denial of service, or access to informational assets) to his own malicious events. Because a response system potentially handles millions of events, a hacker observes an extremely small number of the responses. With this limited information, a hacker cannot launch an effective attack. On the other hand, hackers can possibly coordinate by sharing information about responses to their events. Such coordination is not easy because the hackers do not want to reveal much and because firms can make the coordination ineffective with disinformation. Although the study of hackers’ behavior is interesting, it must clearly identify what and how each hacker knows/learns about the response system. Such a study will have asymmetric information and deserves a separate paper.

This paper extends Ulvila and Gaffney’s framework [34] with a dynamic decisiontheoretic framework. We found that not only are the costs that arise from false alarms and failures in detection important but also there exists a trade-off between rapid reaction and high accuracy. The insights derived in this paper can be applied to design a decision support system or a manual policy that facilitates the decisions on how much to detect, how to react, and when to change how a system should detect and react. To the best of our knowledge, this paper is the first to tie the decisions involved in intrusion detection and reaction. This work represents an ongoing interest in studying the decisions made in intrusion prevention. Future work may include relaxing some of our assumptions and extending the model to include different types of proactive responses. Previous studies have investigated interorganizational ownership issues in the presence of security risks [8, 14]; an interesting extension would be to study security configuration decisions across organizations.

## NOTES

## REFERENCES

1. Amoroso, E.G. Intrusion Detection: An Introduction to Internet Surveillance, Correlation, Trace Back, Traps, and Response. Sparta, NJ: Intrusion.Net Books, 1999.

2. Axelsson, S. The base-rate fallacy and the difficulty of intrusion detection. ACM Transactions on Information and System Security, 3, 3 (2000), 186–205.

3. Bace, R., and Mell, P. NIST special publication on intrusion detection systems. White Paper, United States Department of Commerce, Gaithersburg, MD, 2001 (available at http://csrc .nist.gov/publications/nistpubs/800–31/sp800–31.pdf).

4. Balepin, I.; Maltsev, S.; Rowe, J.; and Levitt, K. Using specification-based intrusion detection for automated response. In G. Vigna, E. Jonsson, and C. Krugel (eds.), Proceedings of the Sixth International Symposium on Recent Advances in Intrusion Detection (RAID 2003). Berlin: Springer, 2003, pp. 136–154.

5. Carver, C.A., Jr., and Pooch, U.W. An intrusion response taxonomy and its role in automatic intrusion response. In Proceedings of the 2000 IEEE Workshop on Information Assurance and Security. Los Alamitos, CA: IEEE Computer Society, 2000, pp. 129–135.

6. Cavusoglu, H.; Mishra, B.; and Raghunathan, S. The value of intrusion detection systems (IDSs) in information technology security architecture. Information Systems Research, 16, 1 (2005), 28–46.

7. Cavusoglu, H., and Raghunathan, S. Configuration of detection software: A comparison of decision and game theory approaches. Decision Analysis, 1, 3 (2004), 131–148.

8. Clemons, E.K., and Hitt, L.M. Poaching and the misappropriation of information: Transaction risks of information exchange. Journal of Management Information Systems, 21, 2 (Fall 2004), 87–107.

9. De, P., and Hsu, C. Adaptive information systems control: A reliability-based approach. Journal of Management Information Systems, 3, 2 (Fall 1986), 33–51.

10. El Sawy, O.A., and Nanus, B. Toward the design of robust information systems. Journal of Management Information Systems, 5, 4 (Spring 1999), 33–54.

11. Endorf, C.; Schultz, E.; and Mellander, J. Intrusion Detection & Prevention. Emeryville, CA: Osborne/McGraw-Hill, 2004.

12. Fisch, E.A. Intrusion damage control and assessment: A taxonomy and implementation of automated responses to intrusive behavior. Ph.D. dissertation, Computer Science, Texas A&M University, College Station, 1996.

13. Gordon, L.A.; Loeb, M.P.; Lucyshyn, W.; and Richardson, R. 2005 CSI/FBI computer crime and security survey. White Paper, Computer Security Institute, San Francisco, CA, 2005.

14. Han, K.; Kauffman, R.J.; and Nault, B.R. Information exploitation and interorganizational systems ownership. Journal of Management Information Systems, 21, 2 (Fall 2004), 109–135.

15. Janice, C., and Gaimon, C. Improving manufacturing performance through process change and knowledge creation. Management Science, 46, 2 (2000), 265–288.

16. Julisch, K. Clustering intrusion detection alarms to support root cause analysis. ACM Transactions on Information and System Security, 6, 4 (2003), 443–471.

17. Lippmann, R.P.; Fried, D.J.; Graf, I.; Haines, J.W.; Kendall, K.R.; McClung, D.; Weber, D.; Webster, S.E.; Wyschogrod, D.; Cunningham, R.K.; and Zissman, M.A. Evaluating intrusion detection systems: The 1998 DARPA off-line intrusion detection evaluation. In DARPA Information Survivability Conference and Exposition, 2000 (DISCEX ’00), vol. 2. Los Alamitos, CA: IEEE Computer Society, 2000, pp. 12–26.

18. Metz, C.E. Basic principles of ROC analysis. Seminars in Nuclear Medicine, 8, 4 (1978), 283–298.

19. Michael, C.C., and Ghosh, A. Simple, state-based approaches to program-based anomaly detection. ACM Transactions on Information and System Security, 5, 3 (2002), 203–237.

20. Ning, P.; Cui, Y.; Reeves, D.S.; and Xu, D. Techniques and tools for analyzing intrusion alerts. ACM Transactions on Information and System Security, 7, 2 (2004), 274–318.

21. Petkac, M., and Badger, L. Security agility in response to intrusion detection. In Proceedings of the Sixteenth Annual Computer Security Applications Conference. Los Alamitos, CA: IEEE Computer Society, 2000, pp. 11–20.

22. Provos, N. A virtual honeypot framework. In Proceedings of the Thirteenth (USENIX) Security Symposium. San Diego: USENIX Association, 2004, pp. 11–20.

23. Rainer, R.K.; Snyder, C.A.; and Carr, H.H. Risk analysis for information technology. Journal of Management Information Systems, 8, 1 (Summer 1991), 129–148.

24. Richardson, R. 2003 CSI/FBI computer crime and security survey. White Paper, Computer Security Institute, San Francisco, 2003.

25. Rowe, N.C.; Michael, M.; Auguston, J.B.; and Riehle, R. Software decoys for software counterintelligence. IAnewsletter, 5, 1 (2002), 10–12.

26. Schnackenberg, D.; Djahandari, K.; and Sterne, D. Infrastructrure for intrusion detection and response. In DARPA Information Survivability Conference and Exposition, 2000 (DISCEX ’00), vol. 2. Los Alamitos, CA: IEEE Computer Society, 2000, pp. 3–11.

27. Sethi, S.P., and Thompson, G.L. Optimal Control Theory: Applications to Management Science and Economics. Norwell, MA: Kluwer Academic, 2000.

28. Sia, S.K., and Neo, B.S. Reengineering effectiveness and the redesign of organizational control: A case study of the inland revenue authority of Singapore. Journal of Management Information Systems, 14, 1 (Summer 1997), 69–92.

29. Sinha, A.P., and May, J.H. Evaluating and tuning predictive data mining models using receiver operating characteristic curves. Journal of Management Information Systems, 21, 3 (Winter 2004–5), 249–280.

30. Sun, L.; Srivastava, R.P.; and Mock, T.J. An information systems security risk assessment model under the Dempster–Shafer theory of belief functions. Journal of Management Information Systems, 22, 4 (Spring 2006), 109–142.

31. Swanson, M.; Bartol, N.; Sabato, J.; Hash, J.; and Graffo, L. Security metrics guide for information technology systems. SP 800–55, NIST. White Paper, United States Department of Commerce, Gaithersburg, MD, 2003 (available at http://csrc.nist.gov/publications/nistpubs/).

32. Swets, J.A. Measuring the accuracy of diagnostic systems. Science, 240, 4857 (June 1988) 1285–1293.

33. Toth, T., and Kruegel, C. Evaluating the impact of automated intrusion response mechanisms. In Proceedings of the Eighteenth Annual Computer Security Applications Conference. Los Alamitos, CA: IEEE Computer Society, 2002, pp. 301–310.

34. Ulvila, J.W., and Gaffney, J.E., Jr. A decision analysis method for evaluating computer intrusion detection systems. Decision Analysis, 1, 1 (2004), 35–50.

35. Weiler, N. Honeypots for distributed denial of service attacks. In Eleventh IEEE WET ICE Workshop on Enterprise Security (WETICE’02). Los Alamitos, CA: IEEE Computer Society, 2002, pp. 9–14.

36. Widyantoro, D.H., and Yen, J. Relevant data expansion for learning concept drift from sparsely labeled data. IEEE Transactions on Knowledge and Data Engineering, 17, 3 (2005), 401–412.

37. Ye, N.; Emran, S.M.; Chen, Q.; and Vilbert, S. Multivariate statistical analysis of audit trails for host-based intrusion detection. IEEE Transactions on Computers, 51, 7 (2002), 810–820.

## Appendix. Proofs

PROOF FOR PROPOSITION 1 AND PROPOSITION 2 are self-evident so they will not be included here.

Proof for Proposition 3

From Equation (6)

$$
v ^ {*} (t) = \left\{ \begin{array}{l l} 0 & \text { if } H _ {v} > 0 \\ \text { to   be   determined } & \text { if } H _ {v} = 0 \\ 1 & \text { if } H _ {v} <   0, \end{array} \right.\tag{A1}
$$

where

$$
H _ {v} = - \lambda_ {1} m (1 - p _ {m}) u - \lambda_ {2} m p _ {m} \Omega (u) + \lambda_ {4} m (1 - p _ {m}) u,\tag{A2}
$$

when $H _ { \nu } = 0$ , we can rewrite Equation (6) to be

$$
\begin{array}{c} H = k _ {b} x _ {b} c + (x _ {m} + y) d + z _ {b} a + \lambda_ {1} (m (1 - p _ {m}) u - k _ {b} x _ {b}) + \lambda_ {2} (m p _ {m} \Omega (u) - (r + k _ {m}) x _ {m}) \\ + \lambda_ {3} (m p _ {m} (1 - \Omega (u)) - r y), \end{array}
$$

which by itself is the Hamiltonian function when only the reactive response is used $( \nu = 0 )$ . Thus, there could be only $\nu ^ { * } ( t ) = 0 \mathrm { o r } \nu ^ { * } ( t ) = 1$ . We can derive $u ^ { * } ( t )$ from the first-order condition. Q.E.D.

## Proof for Proposition 4

The solution for the optimal control in the reactive response case is

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} \left(\frac {p _ {m} (\lambda_ {3} (t) - \lambda_ {2} (t))}{2 (1 - p _ {m}) \lambda_ {1} (t)}\right) ^ {2} & \text {if} p _ {m} (\lambda_ {3} (t) - \lambda_ {2} (t)) <   2 (1 - p _ {m}) \lambda_ {1} (t) \\ 1 & \text {if} p _ {m} (\lambda_ {3} (t) - \lambda_ {2} (t)) \geq 2 (1 - p _ {m}) \lambda_ {1} (t). \end{array} \right.\tag{A3}
$$

(a) Substitute ${ \lambda } _ { _ 1 } ( t ) , { \lambda } _ { _ 2 } ( t )$ , and $\lambda _ { * } ( t )$ into Equation (A3). Differentiating $u ^ { * }$ with respect to time, $d u ^ { * } ( t ) / d t$ can be found to be proportional to

$$
(- 1 + r + e ^ {- k _ {m} (T - t)}).
$$

To ensure du $\bar { \mathbf { \rho } } ( t ) / d t > 0$

$$
r \geq 1 - e ^ {- k _ {m} (T - t)}
$$

has to hold for the entire horizon. Because the right-hand side is largest when $t = 0$ the following condition

$$
r \geq 1 - e ^ {- k _ {m} T}
$$

suffices the requirement of $d u ^ { * } ( t ) / d t > 0$ over the entire horizon.

(b) Suppose now we have

$$
r ^ {\prime} <   1 - e ^ {- k _ {m} (T - t)},
$$

where $r ^ { \prime } > 0$ . We then evaluate the following function

$$
f = r ^ {\prime} - 1 + e ^ {- k _ {m} (T - t)}.\tag{A5}
$$

From Equation $( \mathsf { A } 5 )$ , we learn at $t = 0 , f < 0$ and $d u ^ { * } ( t ) / d t \rvert _ { t = 0 } < 0$ . However, as we increase $t ,$ the right-hand side of the equation will become smaller, and eventually it becomes $r ^ { \prime }$ when $t = T .$ . Thus, we know $d u ^ { * } ( t ) / d t \vert _ { _ { t = T } } > 0 . \mathrm { Q . E . D }$
