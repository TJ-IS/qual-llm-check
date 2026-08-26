---
otero_id: 26411
otero_key: "5KXBH984"
title: "The Effects of Time Pressure on Quality in Software Development: An Agency Model"
authors: "Robert D. Austin"
year: "2001"
journal: "Information Systems Research"
doi: "10.1287/isre.12.2.195.9699"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [144.122.201.150] On: 23 March 2016, At: 06:01 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

![](/api/attachments/5KXBH984/fulltext/images/9308ba9b0b482eaa684296b08dc1c310f2cce9f872b82adfaa62bf1cdab6a2ed.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# The Effects of Time Pressure on Quality in Software Development: An Agency Model

Robert D. Austin,

To cite this article:

Robert D. Austin, (2001) The Effects of Time Pressure on Quality in Software Development: An Agency Model. Information Systems Research 12(2):195-207. http://dx.doi.org/10.1287/isre.12.2.195.9699

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2001 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/5KXBH984/fulltext/images/21b6555f6c6a8eb5d05de174dc2addcde0da8f916d2d7542acd847ca75e4dfdd.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# The Effects of Time Pressure on Quality in Software Development: An Agency Model

Robert D. Austin

Harvard Business School, Soldiers Field, Boston, Massachusetts 02163 raustin@hbs.edu

n agency framework is used to model the behavior of software developers as they weigh concerns about product quality against concerns about missing individual task deadlines. Developers who care about quality but fear the career impact of missed deadlines may take “shortcuts.” Managers sometimes attempt to reduce this risk via their deadline-setting policies; a common method involves adding slack to best estimates when setting deadlines to partially alleviate the time pressures believed to encourage shortcut-taking. This paper derives a formal relationship between deadline-setting policies and software product quality. It shows that: (1) adding slack does not always preserve quality, thus, systematically adding slack is an incomplete policy for minimizing costs; (2) costs can be minimized by adopting policies that permit estimates of completion dates and deadlines that are different and; (3) contrary to casual intuition, shortcut-taking can be eliminated by setting deadlines aggressively, thereby maintaining or even increasing the time pressures under which developers work.

(Agency Theory; Principal-Agent; Software Quality; Software Measurement; Software Estimating)

## 1. Introduction

Time pressures induced by development schedule constraints are an often-cited source of quality problems in technological systems (DeMarco 1982, 1995; Pate-Cornell 1990; Staw 1982; Brooks 1975). Problems arise when developers, feeling that they are under pressure to meet task deadlines, take shortcuts in dealing with unanticipated complications. “Shortcuts” are decisions made in private that are motivated by a desire to stay on schedule, but are not in the best interests of the project. At the time such a decision is made, it may not be certain that adverse consequences will ensue, and it is unlikely that the possible consequences are fully known to the developer. What is crucial is that a developer who is concerned about quality would have made a different private choice if perceived time pressures were somehow alleviated. Shortcuts are not necessarily due to guile (Brooks 1975), nor are they necessarily the result of a deliberate decision process. Rather, they reflect a developer’s tendencies to hope for the best, to leave potential sources of difficulty unexplored, and to interpret requirements conveniently when faced with time pressures.

Developers take shortcuts without fearing personal consequences because it is difficult for nonspecialists to trace complex system problems to causal sources. Such difficulties in software development are well documented (e.g., DeMarco 1995, Iansiti and Gill 1990). They arise from developers’ often profound advantage over supervisors in job-related knowledge (Curtis 1984, 1997), from the inherent “incompleteness” of measures for complex activities (Austin 1996, Holmstrom and Milgrom 1991, Blau 1963), and from the particular characteristics (e.g., intangibility) of software (Brooks 1987).

## 1.1. How Shortcuts Happen—An Illustrative Example

Developers at a manufacturing company were working toward a deadline for installing software in a plant. The software would be critical to plant operations, so failures would be expensive. Because of the complexity of the overall system (a large client-server application that interacted with many other machines), only the three members of the software development team understood its detailed inner workings. Although complex, the software was not new; it was running successfully in other plants. Most development work was, therefore, oriented toward improvements and correction of discovered problems. Two weeks before the installation date, a new requirement surfaced.

Unlike other plants where the software was already running, this plant had no shutdown period each day. It was usually idle between 4:30 a.m. and 5 a.m., bu t on some days operations would continue right through until 5 a.m. During peak production times, this could happen several days in a row. The software, however, required 15 minutes of shutdown time each day to perform an automated backup. The backup process was built into the design. There was no option in the standard application for postponing a backup.

To address the new requirement the three-person development team considered options ranging from a simple on/off switch for the backup process, to more elaborate designs that reminded operators to turn the backup process back on, or that automatically turned the process back on. The chief concern was that plant computer operators might use the “off” option too often or forget to turn the backup process back on. If backup was postponed for more than a week, the system would fail (a file would expand to fill all available disk space). Failure might well occur at the worst possible time because plant personnel would be most likely to forget about the backup when they were straining to meet peak demand. Thus, the development team agreed that the best solution would be a redesign of the backup process to allow backups during plant operations. However, there was no way to complete and test such a substantial redesign before the deadline for installing the software in the plant.

Despite their concerns, the team chose a simple on/ off switch design. The sole reason for their choice was their reluctance to delay installation plans. A few months after the software was installed, it failed in exactly the way they had anticipated. The resulting unplanned shutdown was much more expensive than a delay in installation would have been. If they had not had time pressures, the development team would have eliminated this problem. In effect, they chose to incur potential, shared consequences (a possible future failure for which blame would be shared with others, e.g., plant personnel who forgot to turn on the backup) rather than immediate, certain, personal consequences (blame for delaying the project).

## 1.2. Evaluating Policies to Solve the Shortcut Problem

One way managers try to reduce the risk of shortcuts is by making systematic adjustments to estimates in setting deadlines. A common method is adding slack to project schedules at the time that deadlines are set (Tomayko 1987). Project managers often follow deadline-setting guidelines like “take your best estimate and double it” (DeMarco 1997, Yourdon 1997). The underlying rationale is that adding slack provides developers with needed “breathing room,” allowing them to be more thorough and quality conscious.

This paper uses an agency framework to derive a formal relationship between deadline-setting policies and software product quality; it provides recommendations concerning how deadlines might be set to preserve the quality of software development products. The major findings of this paper are that: (1) adding slack does not always enhance quality, thus, systematically adding slack to alleviate time pressure is, at best, an incomplete strategy for minimizing costs; (2) costs can be minimized by adopting estimating and deadline-setting policies that permit estimates of completion dates and deadlines that are different; and (3) contrary to casual intuition, shortcut-taking can be eliminated by setting deadlines aggressively, thereby maintaining or even increasing the time pressures under which developers work.

Although King and Wilson (1967) suggested separating planning estimates from deadlines, and setting the latter more aggressively than the former, it is not common in modern development environments (DeMarco 1997, Yourdon 1997). DeMarco’s (1997) comments state a case for this approach and lament the scarcity of its practice:

I have advocated for years that we ought to conduct projects with both an estimate and a goal. After all, the two words mean quite different things, so that a good estimate is necessarily a bad goal, and a good goal is a bad estimate. It would be perfectly reasonable for a project to adopt a one-year goal, for example, but have everyone understand that the plan is called for delivery in 18 months. However, I am [fighting against the tide] on this one. The prevailing standard is that the goal is the estimate.

Setting goals (deadlines) so that they are shorter than estimates has the additional advantage of being consistent with improving time-to-market performance. King and Wilson (1967) recognized the benefits of this approach in their work. The model in this paper adopts and extends their general analytic approach.

## 2. The Agency Framework

Agency situations arise whenever one person relies on another person to do work (Jensen and Meckling 1976). The problem created is one of control, because the worker—the agent—can usually act in ways that are not observable to the person who wants the work done—the principal. Observation difficulties result from lack of time to comprehensively supervise (watching the agent every minute obviates the efficiency sought in hiring him), specialized skills possessed by the agent but not by the principal (which are often the principal’s reason for employing the agent in the first place), or anything else that make it difficult to attribute work or its consequences to a single agent (Alchian and Demsetz 1972). The central problem broached by this framework is the following: How can the agent, whose motives may not be aligned with those of the principal and who has the ability to act beyond the view of the principal, be influenced to behave in a way that is desirable to the principal?

## 2.1. The Agent: Quality from the Developer’s Perspective

Consider a situation in which two agents are competing for rewards (e.g., promotions, pay raises, future business) from a principal to whom they report at regular intervals. Each agent reports either that he is “on schedule” or “behind schedule.” An agent fortunate enough to have been assigned an achievable task deadline can honestly claim to be on schedule. An agent who has been assigned an unachievable deadline faces a choice. He can report “on schedule” while taking shortcuts that may impact the quality of the product, or he can report that he is behind schedule, thereby requesting adjustment of his schedule to ensure production of high-quality work. For a given task interval, assume each agent faces an unachievable deadline with probability $p ;$ the value of $p$ is determined by the deadline-setting policy of the principal.<sup>1</sup> Deadlines are assumed to be set in a consistent manner across agents, and any bargaining between agent and principal that might influence the value of $p$ is assumed to have the same effect for all agents.<sup>2</sup>

An agent deciding whether to compromise quality has two concerns. The first, which might be called concern for career, arises because he worries that he may “look bad” in the eyes of the principal if he confesses that he is behind schedule and his fellow agent does not (either because the fellow agent’s deadline is achievable or because he chooses to take a shortcut). Concern for career enters the agent’s utility function as a penalty, C, for being the only agent who is behind schedule.

The second concern might be called concern for quality. Concern for quality is an expression of what might be referred to as organizational identification (Simon 1991). Agents believe that shortcut-taking may harm product quality or endanger project success, thereby causing damage to their organization’s reputation, future profitability, etc., and harming each member for the organization. This concern also enters the agent’s utility function as a penalty, denoted $Q _ { 1 }$ when only one agent takes a shortcut and $Q _ { 2 }$ when both do. Because more shortcut-taking does more damage, $Q _ { 2 } > Q _ { 1 }$ . Unlike the penalty $C$ that accrues only to the agent who reports that he is behind schedule, $Q _ { 1 }$ and $Q _ { 2 }$ are accrued by all agents. That is, when one agent takes a shortcut, the organization as a whole is damaged, so both agents experience a $Q _ { 1 }$ penalty. It is assumed also that $C > Q _ { 2 } ;$ this means that while agents dread the individual impacts of shortcut-taking, they fear damaging their career prospects more.

Figure 1 The Extensive Form Game  
![](/api/attachments/5KXBH984/fulltext/images/f3a9bf7deaf8534cc64901df2111f470952f54147d269b51c336d53fba1161f1.jpg)  
Notes. “H” indicates a choice of high quality (avoiding quality compromising shortcuts); “L” indicates a choice of low quality (taking shortcuts). Numbered areas enclosed by ovals are information sets. An agent at a node within an information set cannot tell the difference between the nodes in that set.

Intentionally not included in the penalty function is a term reflecting the agent’s fear of “getting caught.” As has been noted, in software development the agent often has an advantage over the principal in relative degree of job-related knowledge, and even in skill or talent (Curtis 1997); this advantage means agents generally have shortcut options to pursue. There is a vast literature on the difficulties of monitoring complex activities “completely” (e.g., Argyris 1952, Ridgway 1956, Blau 1963, Kerr 1975, Deming 1986, Umpathy 1987, Holmstrom and Milgrom 1991, Larkey and Caulkins 1992, Kohn 1993, Austin 1996). Software’s particular characteristics (e.g., intangibility, invisibility) pose special challenges for control processes (Brooks 1987). Furthermore, economists have noted that systematic nonuse of piece rates in a profession can be interpreted as evidence that monitoring of quality is difficult (Milgrom and Roberts 1992). The fact that software developers are not paid based on the quantity of code produced is evidence, according to this logic, that quality monitoring is difficult.

## Summary of Notation

$p$ - The probability that an agent is assigned a task deadline that is not achievable without taking quality-compromising shortcuts.

C - The penalty perceived by the agent for being singled out as the only agent who could not finish his task on time. This penalty arises from perceived damage to career prospects relative to a peer who has finished his task on time and thus appears to be a stronger performer.

$Q _ { 1 }$ - The penalty perceived by the agent when he believes that quality-compromising shortcuts are being taken by exactly one agent (possibly himself). This penalty arises from the agent’s expectation that quality-compromising shortcuts may eventually damage the overall project, thereby indirectly harming the agent.

$Q _ { 2 }$ - The penalty perceived by the agent when he believes that quality-compromising shortcuts are being taken by both agents. This penalty derives from the same source as the $Q _ { 1 }$ penalty but is greater in magnitude because of the agent’s greater expectation of damage to the project when both agents take shortcuts.

## 2.2. Game Setup

The situation can be modeled as the following twoperson game:

(1) Assume that NATURE assigns each of the two agents a deadline situation. With probability $p ,$ an agent faces an unachievable deadline. After this assignment, an agent knows his own deadline situation (achievable or unachievable), but he does not know the deadline situation of the other agent.

(2) Each agent who faces an unachievable deadline decides simultaneously whether to produce either HIGH or LOW quality (H or L in Figure 1). Choosing HIGH quality means that he admits to the principal that he cannot meet his deadline, thereby incurring the associated penalty $C .$ Choosing LOW quality means that he takes a shortcut and announces that he is “on schedule” to the principal, thereby avoiding the penalty for missing deadlines but incurring a penalty to the organization that affects both agents; this penalty is $Q _ { 1 }$ if only one agent chooses LOW, and $Q _ { 2 }$ if both agents choose LOW.

Figure 1 shows the extensive form game. Four different events may arise: (A) both agents face unachievable deadlines, with probability $p ^ { 2 } ;$ (B) only Agent 1 faces an unachievable deadline, with probability p(1  $p ) ;$ (C) only Agent 2 faces an unachievable deadline, with probability $( 1 \mathrm { ~ - ~ } p ) p ;$ ; and (D) neither agent faces an unachievable deadline, with probability $( 1 ~ - ~ p ) ^ { 2 }$ The relative frequency of each of these events depends on the value of $p ,$ hence, on the deadline-setting policy. The ovals denote information sets; the deciding agent cannot tell which of the nodes he is at within an information set, so he perceives penalties as expectations from the parameter $p .$ If the agent’s deadline is achievable, he has no shortcut-taking decision to make.

Figure 2 is the normal form representation of the game. By comparing penalties on the matrix we can derive the following core results (see appendix for proofs):

(i) There is always a pure strategy Nash equilibrium at (LOW, LOW).

(ii) There may also be pure strategy Nash equilibrium at (HIGH, HIGH). The (HIGH, HIGH) equilibrium arises when

$$
p \geq 1 - \frac {Q _ {1}}{C}.\tag{1}
$$

(iii) When the (HIGH, HIGH) equilibrium exists, it is Pareto superior to the (LOW, LOW) equilibrium.

Figure 2 Normal Form of Game

<table><tr><td rowspan="2"></td><td colspan="2">Developer 1</td></tr><tr><td>HIGH</td><td>LOW</td></tr><tr><td>High</td><td>(1-p)C</td><td> $pQ_1+(1-p)Q_1 = Q_1$ </td></tr><tr><td>Developer 2</td><td>(1-p)C</td><td> $p(C+Q_1)+(1-p)C$ </td></tr><tr><td rowspan="2">LOW</td><td> $p(C+Q_1)+(1-p)C$ </td><td> $pQ_2+(1-p)Q_1$ </td></tr><tr><td> $pQ_1+(1-p)Q_1 = Q_1$ </td><td> $pQ_2+(1-p)Q_1$ </td></tr></table>

Notes. $\mathsf { \Pi } ^ { \mathrm { * } } \mathsf { H I G H } ^ { \mathrm { * } }$ indicates a choice of high quality (avoiding quality compromising shortcuts); $\mathbf { \mu } ^ { * } \mathbf { L } 0 \mathsf { W } ^ { * }$ indicates a choice of low quality (taking shortcuts).

(iv) Even when (HIGH, HIGH) is not a pure strategy Nash equilibrium, it may be Pareto superior to (LOW, LOW). This occurs when

$$
1 - \frac {Q _ {2}}{C - Q _ {1} + Q _ {2}} <   p <   1 - \frac {Q _ {1}}{C}\tag{2}
$$

The question of practical importance is whether we can choose a deadline-setting policy so that (HIGH, HIGH) becomes the compelling choice for agents.

These core results describe a game that for low values of p (for $p < 1 - Q _ { 2 } / [ C - Q _ { 1 } + Q _ { 2 } ] )$ has a single equilibrium at (LOW, LOW) that is Pareto superior to the (HIGH, HIGH) outcome. Here game theory predicts a (LOW, LOW) outcome; shortcut-taking will prevail for these values of $p .$ For higher values of $p$ (for $1 - Q _ { 2 } / [ C - Q _ { 1 } + Q _ { 2 } ] < p < 1 - Q _ { 1 } / C )$ , the game has a single equilibrium at (LOW, LOW) that is Pareto inferior to the (HIGH, HIGH) outcome. In this situation, the (HIGH, HIGH) outcome gains appeal, but it is arguably difficult to achieve because it is not an equilibrium; again, shortcut-taking prevails. For even higher values of $p$ (specifically, for $p > 1 \mathrm { ~ - ~ } Q _ { 1 } / C )$ , a coordination game arises with a Pareto-superior equilibrium at (HIGH, HIGH). It is reasonable to assume that agents are able to achieve coordination on the Pareto-optimal equilibrium when it exists, especially where communication between agents is possible, hence the game-theoretic prediction here is (HIGH, HIGH)<sup>3</sup>; shortcut-taking does not prevail. The message for the principal who wishes to preclude shortcuttaking is to choose deadline-setting policies, so that $p$ is high—that is, so that unachievable deadlines are more, not less, likely. This conclusion is at odds with slack-adding practices.<sup>4</sup>

## 2.3. Adding Slack vs. Reducing Slack to Enhance Quality

As long as p is below the critical value that makes agents want to avoid shortcuts entirely, adding slack will reduce the rate of shortcut-taking in the organization. Figure 3 depicts this situation. With p in the shortcut-taking range, the rate of shortcut-taking, r, is equal to p because everyone facing a shortcut-taking opportunity takes it. By lowering p, r is also lowered. This fits with the commonsense notion behind the slack-adding recommendation. If shortcut-taking is a foregone conclusion, then the total amount of shortcuttaking can be reduced by reducing the frequency of unachievable deadlines.

What the slack-adding rationale fails to recognize is that virtually all shortcut-taking could be eliminated by raising p into the no shortcut-taking range—that is, by increasing the frequency of unachievable deadlines—thereby alleviating agents’ fear about comparing unfavorably to other agents. In other words, shortcut-taking is not a foregone conclusion. Reducing slack makes more sense than adding slack because no shortcut-taking is less costly in terms of rework of the product than a small amount of shortcut-taking. Furthermore, there is a fundamental problem with adding slack that is not a problem with reducing slack: Market timing or other inputs to the deadline-setting process might make adding slack infeasible.

## 3. The Principal: Quality from the Manager’s Perspective

The principal is interested in minimizing the total cost of developing a system that meets requirements. These total costs are influenced by her policies for (1) estimating task duration and (2) setting deadlines.

![](/api/attachments/5KXBH984/fulltext/images/f8b582606b4000c3647b9e27d2b3742ad100176dbf0560c5df0f8d478efe915f.jpg)  
Note. Rate of shortcut taking (r )

As DeMarco has observed (see §1.2.), estimating and deadline-setting are conceptually separate activities. Accurate estimates of task duration are valued for their planning usefulness; they allow resources to be brought to bear at the right times. Deadlines, in contrast, are behavioral objectives that communicate expectations of completion timing to workers. The two activities do sometimes interact; setting deadlines to occur after planned completion dates would strike most as nonsensical. But the opposite arrangement is not nonsensical, as DeMarco points out: “It would be perfectly reasonable for a project to adopt a one-year [deadline], for example, but have everyone understand that the plan called for delivery in 18 months” (1997). To closely examine this suggestion, it is necessary to consider estimating and deadline-setting policies separately.

## 3.1. The Optimal Estimating Policy

Arriving at an estimate to use as basis for planning is a nontrivial undertaking. Estimating often involves human judgment, which may be subject to systematic biases (Abdel-Hamid et al. 1993, Kahneman and Tversky 1979). Biases matter because inaccurate estimates can lead to inefficient resource allocation (e.g., specialized expertise or assets brought to bear too soon or too late) and other costly difficulties. Underestimates are usually considered more costly than overestimates because underestimates have “ripple effects” on downstream tasks that are sequentially dependent on the estimated task; this cost asymmetry must also be considered when deciding on an estimating policy.<sup>5</sup> King and Wilson (1967) have suggested a way of correcting for these problems that is based on historical data about estimates and actual completion dates. It is worth considering their result briefly here because of the potential for interaction with deadline-setting policies.

King and Wilson propose systematically adjusting raw estimates that are the result of an uncorrected estimation process by multiplying the raw estimate by a parameter, $b \ ( b > 0 )$ . For $b > 1$ , this is equivalent to adding slack to the raw estimate to produce a corrected estimate; similarly, setting $b < 1$ is equivalent to shortening the raw estimate, and $b = 1$ is equivalent to leaving the raw estimate unaltered. The optimal value of b that compensates for systematic estimating biases and cost asymmetries can be determined via the following expression (see Appendix for the derivation):

$$
\begin{array}{l} b = \arg \underset {b} {\text {Min}}   \Sigma^ {o v e r}   K _ {1} (b E _ {t} / A _ {t} - 1) ^ {2} \\ + \Sigma^ {u n d e r}   K _ {2} (b E _ {t} / A _ {t} - 1) ^ {2} \end{array}\tag{3}
$$

where

$$
\begin{array}{l l} E _ {t} & \text { is   the   originally   estimated   duration   of } \\ & \text { now   completed   task } t; \end{array}
$$

$$
\begin{array}{l l} A _ {t} & \text { is   the   actual   duration   of   now   completed } \\ & \text { task } t; \end{array}
$$

$K _ { 1 }$ and $K _ { 2 }$ are cost function parameters;

$\Sigma ^ { o v e r }$ is the sum over historical tasks such that $1 - E _ { t } / A _ { t } < 0$ (overestimates);

$$
\begin{array}{l l} \Sigma^ {\text { under }} & \text { is   the   sum   over   historical   tasks   such   that } \\ & 1 - E _ {t} / A _ {t} > 0 (\text { underestimates }). \end{array}
$$

The details of this expression are less important than what it implies for the optimal value of b. If underestimates are more expensive than overestimates, and if people are systematically prone to underestimation (both are commonly believed), the optimal b will be greater than 1. In other words, a policy of adding slack to raw estimates to arrive at corrected estimates is a good idea from a planning cost minimization standpoint.

## 3.2. The Optimal Deadline-Setting Policy

Analogous to the method of obtaining corrected estimates, deadlines can be derived by multiplying estimates<sup>6</sup> by a parameter, $d \left( d > 0 \right)$ . Adding slack to arrive at a deadline is equivalent to setting d $> 1 ;$ subtracting time to arrive at a deadline is equivalent to setting $d <$ $^ { 1 ; }$ and using the estimate as the deadline is equivalent to setting $d = 1$

Note that d and $p$ (the likelihood that an agent will face an unreasonable deadline) are related. Assuming that $p$ is a decreasing function of d $( \mathrm { i . e . } ,$ , adding slack to estimates in setting deadlines makes it less likely that agents will face unreasonable deadlines) is reasonable. And, as has been shown, the parameter p affects the agent’s decision whether or not to take shortcuts. What remains to be determined, then, is the costminimizing value of d and whether/how estimating and deadline policies should be related.

The cost of shortcut-taking should be an increasing function of the rate of shortcut-taking. Minimizing the latter should, then, minimize the former. The shortcuttaking rate is minimized when (reading from Figure 3):

(1) p approaches zero (that is, when d is much greater than 1), or

(2) $p > p _ { c r i t }$ (that is, when $d < d _ { c r i t } ,$ where $d _ { c r i t }$ is that value of d that sets $p = p _ { c r i t } )$

The first of these cost-minimizing alternatives is impractical; it would equate to a policy of adding a large, possibly infinite amount of slack in deriving deadlines. The second alternative is more interesting. It suggests a policy of setting d low enough to eliminate shortcuttaking and associated costs due to lost quality. In other words, a policy of subtracting time from estimates to arrive at deadlines is a good idea from a shortcut-taking cost minimization standpoint.

## 3.3. An Integrated Estimating and Deadline-Setting Policy

From the above separate derivations of optimal estimating and deadline-setting policies, it is apparent that using the same date for estimated completion and deadline is not generally optimal. Adding time to raw estimates to derive corrected estimates minimizes planning costs. Subtracting time from best estimates to derive deadlines minimizes shortcut-taking costs. The directions of these recommendations are opposite. Taken together, however, these policies suggest an integrated two-step policy for deriving estimates and setting deadlines:

(1) Add slack systematically to raw estimates to get corrected estimates that will be used in planning;

Figure 4 Normal Form of Expanded Game

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">Developer 2</td></tr><tr><td>HIGH</td><td>LOW</td><td>ADD EFFORT</td></tr><tr><td rowspan="6">Developer 1</td><td rowspan="2">HIGH</td><td>(1-p)C</td><td> $Q_1$ </td><td>EP</td></tr><tr><td>(1-p)C</td><td> $p(C+Q_1)+(1-p)C$ </td><td>C</td></tr><tr><td rowspan="2">LOW</td><td> $p(C+Q_1)+(1-p)C$ </td><td> $pQ_2+(1-p)Q_1$ </td><td> $EP+pQ_1$ </td></tr><tr><td> $Q_1$ </td><td> $pQ_2+(1-p)Q_1$ </td><td> $Q_1$ </td></tr><tr><td rowspan="2">ADD EFFORT</td><td>C</td><td> $Q_1$ </td><td>EP</td></tr><tr><td>EP</td><td> $EP+pQ_1$ </td><td>EP</td></tr></table>

(2) Subtract time systematically from best estimates to arrive at deadlines that will serve as behavioral objectives for developers.

This policy is consistent with DeMarco’s suggestion that deadlines should be routinely set so that they are “tighter” than estimates (1997).

## 4. Model Variations

Exploring variations on the analyses in this paper helps determine sensitivity to changes in assumptions. This section considers (1) the effect of changes in penalty orderings, and (2) the possibility that agents might add additional effort rather than engage in shortcuttaking as a way of achieving deadlines.

## 4.1. Changing Penalty Ordering

It has been assumed that the penalty to the agent for missing a deadline, C, is greater than the quality reduction effect on the agent that results from his own shortcut-taking, that $C > Q _ { 2 } > Q _ { 1 }$ . This penalty ordering fits the situation described in the example in §1.1. Agents are more concerned about the career implications of missing deadlines than about the damage that they expect to accrue personally as a result of taking a shortcut. But what if this situation does not hold?

It is simple to verify that rearranging the penalties so that $Q _ { 2 } > Q _ { 1 } > C$ solves the shortcut-taking problem. With this penalty ordering, the (HIGH, HIGH) outcome is an equilibrium, and it is Pareto superior to the (LOW, LOW) outcome for all values of p (see the appendix for proof). Shortcut-taking never occurs.

Whether this could actually be achieved depends on the situation. Emphasizing to agents that quality work is valued might have the effect of adjusting penalties relative to each other. For example, agents could be substantially rewarded for early identification of problems in their areas of responsibility. However, there may be factors in the environment that make maintaining such a quality-conscious ethos difficult.

A projection that a deadline will be missed is always bad news. A missed deadline raises questions of whether the schedule shortfall could have been avoided; questions like “why wasn’t this problem identified sooner?” are particularly dreaded. And, responsibility for a missed deadline is unambiguously assigned.

In contrast, a quality problem that emerges is separated by time from its cause. Responsibility for such a problem is often uncertain and diffuse. Furthermore, the primacy of deadlines in a work environment is often driven by external factors, such as a legal contract or the accounting and control context in which the work is done. These factors combine to make reversing penalty orderings difficult in practice.

## 4.2. Adding Effort as an Alternative to Shortcut-Taking

Suppose that an agent, seeing that he could not meet a deadline, chose to add enough extra effort—that is, to work harder—to achieve the deadline, rather than take a shortcut. How might the value of $p$ influence this choice?

Adding effort is, in effect, a third strategy that agents might play in their two-person game. Figure 4 is the normal form representation of this expanded game, with the penalty that accrues from adding effort depicted simply as $^ { \prime \prime } \mathrm { E P . } ^ { \prime \prime }$ Determining game outcomes depends on the nature of the EP, and specifically on how EP varies with p.

In the agency literature, effort aversion is invariably modeled as a penalty function that is convexincreasing in the quantity of effort exerted. As $p$ increases, it is reasonable to presume that deadlines become, on average, more unachievable, requiring more effort expenditure. It is thus reasonable to consider EP as a convex-increasing function of $p .$

Figure 5 is a graphical way of comparing the various penalties involved in this new, expanded game, as the parameter $p$ varies between 0 and 1. From the game matrix it is apparent that the (Add Effort, Add Effort) outcome is an equilibrium when EP is less than $Q _ { 1 }$ . In Figure $5 ,$ this is true whenever the curved EP line is below the horizontal line at $Q _ { 1 }$ , up to the point labeled x in the figure. Thereafter, the (Add Effort, Add Effort) outcome, although no longer an equilibrium, remains Pareto superior to (LOW, LOW) until the EP line crosses the line labeled LL. At the point marked ${ \mathrm { y } } ,$ the (HIGH, HIGH) outcome becomes Pareto superior to (LOW, LOW), but it is not until the point labeled z that (HIGH, HIGH) becomes an equilibrium. In the situation depicted here, actions would follow the heavy dark lines in Figure 5; agents would choose to add effort for values of $p$ between 0 and $p _ { x } ,$ at which point they would switch to taking shortcuts. At the value of $p$ labeled $1 \mathrm { ~  ~ { ~ - ~ } ~ } Q _ { 1 } / C ,$ agents would switch from shortcut-taking to truthfully reporting being behind schedule. Of course much depends on how convex the EP penalty actually is. If it is only mildly convex, then the range of the parameter $p$ for which (Add Effort, Add Effort) is the best equilibrium could be extended considerably to the right. In the best case, it would extend far enough that shortcut-taking would never occur.

Figure 5 Adding Effort as an Alternative to Shortcut-Taking  
![](/api/attachments/5KXBH984/fulltext/images/5c8989a0785e320e0566a5342bc6c046678b9d7dcb1d3bb93f31f3f1b8a3123f.jpg)

Depending on the degree to which agents are effort averse, adding effort might therefore substitute for shortcut-taking when the value of $p$ is low. This provides a rationale for adding slack—very probably the rationale behind most slack-adding recommendations. If deadlines can be made reasonable enough in general, then people will work harder when deadlines are harder to meet. Adding enough slack to make it very likely that unachievable deadlines can be met by adding effort would, then, be an alternative policy for eliminating shortcut-taking.

How feasible this policy is in real settings depends on the degree to which exogenous factors (like market timing) permit enough slack to be added. Even when slack could be added, however, setting p high to eliminate shortcut-taking behavior in the manner described earlier remains an attractive option.

## 5. Discussion

Although the recommendations of this paper are not uniformly practiced, it should nevertheless be noted that they are consistent with some other analyses. Parkinson’s Law (Parkinson 1962), which states that work will expand to fill the available time, leads to a similar conclusion about the wisdom of setting aggressive deadlines, via a different argument. Gutierrez and Kouvelis (1991) have formalized Parkinson’s Law and reached a similar conclusion for project management using a stochastic activity completion time model. Abdel-Hamid and Madnick (1986, 1989) have generated similar conclusions specifically for software development using a systems dynamics approach. Even though each of these sources uses different analytical methods and emphasizes different rationales, the consistency in the conclusions is arguably indicative of a strong underlying logic.

It is worth asking whether the policy of setting deadlines tighter than estimates can actually be implemented, or whether there is some practical difficulty that explains the relative scarcity of these policies. In particular, it is worth considering whether agents would be willing to abide by aggressive deadlines that are separate from estimates. Agents with assigned deadlines in three months, but who know the actual estimate for the activity they are undertaking is six months, might be inclined to regard the three-month deadline too casually—in effect, to treat the six-month estimate as the “true” deadline. While this possibility must be admitted, agents who never make deadlines do risk being unfavorably noticed. Organizations can and do manage such possibilities by “framing” deadline-setting policies. For example, they might depict deadlines as “stretch goals” that are good to achieve but that will not be achieved on a regular basis.

The process of actually generating estimates in real settings also complicates application of the recommendations in this paper. In many settings there are complex interdependencies among developers, which might provide even more latitude for strategic behavior than is addressed in this paper (for example, a developer might be able to secretly take actions to sabotage other agents). Among other problems, these interdependencies make it difficult to employ consistent estimating and deadline-setting policies. These kinds of problems are part of the reason why many software development organizations increasingly seek modularity (i.e., absence of interdependency among modules) in their designs (MacCormack et al. 1999).

The assumption that developers generally have time-saving shortcuts available and that they do not fear being “caught” taking shortcuts might seem controversial to some. Recent years have seen progress by organizations such as the Software Engineering Institute (SEI) in designing sophisticated measures for monitoring software quality. There is reason to believe, however, that software quality monitoring is far from a completely solved problem. Field research often turns up comments like the following from a softwarestartup CEO (speaking about her best developers):

They’re your most precious commodity and your worst nightmare. You have no idea what they’re doing. They literally sit there with 42 little windows open on their 17-inch monitor. When [your business shifts] you’ll often find the seed for the shift in that group because they’re not really paying attention to you all along anyway. They were worried about some wayout-there trend. They’ll see it and there will be something there. [The key to] how to manage change is in that group of folks you don’t have a lot of control over.

There are variations on the model in this paper that might be explored in future research. In some organizations, it might make sense to consider the possibility that agents might take shortcuts even when their deadlines are achievable. In thereby finishing early an eager agent could differentiate himself from his peers. It might also be possible to create a more general model that integrates the problem of quality with the more traditional focus of the agency literature, effort productivity (e.g., Ross 1973, Holmstrom 1979, Holmstrom and Milgrom 1991). The frequency with which developers meet deadlines is an obvious output measure that is a de facto, if not an explicitly designed, element of an incentive contract intended to produce greater effort. Happily, the results in this paper show that agents are more likely to achieve high-quality outcomes in conditions that also provide strong effort incentives (i.e., aggressive deadlines). Thus, solutions to the effort aversion and shortcut-taking problems might well be mutually reinforcing.

There are additional empirical features of software development environments that suggest caution in generalizing the conclusions of this paper. Foremost among these is the established finding that there are great individual productivity differences among developers (Curtis 1984, 1997). In terms of the model in this paper, this suggests that the probability that a given developer faces an unachievable deadline varies by developer. In effect, some developers may very rarely face unachievable deadlines because they are so productive, while others may almost always face deadlines that they cannot meet. Ability to achieve deadlines in such a situation is a strong signal of programmer ability. But, of course, this presumption is the very source of the concern for career penalty, C, which appears in the model in this paper—developers take shortcuts because they fear that missing deadlines will cause them to be viewed as less talented than their peers. It seems reasonable that setting deadlines so that even the most talented developers often face unachievable deadlines would make lower-talent developers less likely to take shortcuts. An enhancement to the model in this paper might, however, suggest further refinements to the deadline-setting process to account for developers’ individual differences.

There are other model caveats worth mentioning. Perception of penalties is a highly individual matter; some developers may, for ethical reasons, refuse to take shortcuts regardless of the consequences (although an organization that measures performance against deadlines may, ironically, quickly rid itself of those who are too ethical to take shortcuts). There are a variety of imaginable quality-monitoring technologies (e.g., counts of detectable defects) and reward systems (e.g., bonuses) whose particular characteristics might suggest extensions on the model in this paper, and which might bear on the generality of the results.

## 6. Conclusions

The analyses in this paper have derived the following recommendations concerning estimating and deadline setting in software development settings:

1. Systematically adding slack is not necessarily a costminimizing policy. If you can afford to set very leisurely deadlines, then you may be able to eliminate shortcuttaking in this way. Agents will substitute extra effort to avoid the negative quality effects of shortcut-taking when unachievable deadlines are not that unachievable (see §4.2.). However, the effort penalty increases at an increasing rate, so if deadlines start to become less leisurely, there is a risk of shortcut-taking. A better policy is as described in 2. and 3. below.

2. Deadlines and planning estimates should be set separately. Planning estimates should be adjusted based on historical information about the accuracy of estimates in the manner of King and Wilson (1967).

3. Deadlines should be set aggressively to be “stretch goals” that few developers regularly meet. Because missing deadlines is common in such an environment, there is no stigma associated with it and developers are forthcoming in admitting quality issues that arise in their areas of responsibility.

It is difficult to make conclusive statements about the extent to which these recommendations are being followed in the large and diverse software development community. Yourdon (1997) and DeMarco (1997) indicate that systematically adding slack is probably too common. They also indicate that using separate planning estimates and deadlines, as suggested by King and Wilson (1967), is not practiced often enough.

Some organizations may effectively back into the third of these recommendations—complaints about missed deadlines in software development are common. Companies like Microsoft, despite their technological proficiency, still have difficulty delivering a product on deadline (Cusumano and Selby 1997). There is a tendency to regard this fact as indicative of poor management practice. At a very general level, the message of this paper is that missing deadlines does not necessarily equate to bad practice. Deadline-setting policies that result in frequently missed deadlines have a potentially favorable effect on product quality. For that reason, software development organizations that habitually miss deadlines may produce better longterm results than their apparently better managed counterparts that rarely miss deadlines.

## Appendix—Proofs of Core Results

Section 2.2. (i): Reading from the game matrix, it is clear that (LOW, LOW) is an equilibrium when

$$
p Q _ {2} + (1 - p) Q _ {1} \leq p \left(C _ {1} + Q _ {1}\right) + (1 - p) C _ {1}.\tag{A1}
$$

Pairwise comparison of the penalties that are weighted by p and (1 $- \ p ) _ { . }$ , respectively, reveals that, for penalty order as given, i.e., $C _ { 1 } >$ $Q _ { 2 } > Q _ { 1 } ,$ , the LHS of (A1) is always strictly less than the RHS. Specifically, the given penalty ordering implies that $Q _ { 2 } < C _ { 1 } + Q _ { 1 }$ and $Q _ { 1 } < C _ { 1 }$

(ii): Reading from the matrix, it is clear that (HIGH, HIGH) is an equilibrium when $( 1 ~ - ~ p ) C _ { 1 } \leq Q _ { 1 }$ , which simplifies to (1).

(iii): (HIGH, HIGH) is Pareto superior to (LOW, LOW) when (1 $- \ p ) C _ { 1 } < p Q _ { 2 } \ + \ ( 1 \ - \ p ) Q _ { 1 }$ , which simplifies to

$$
p > \frac {C _ {1} - Q _ {1}}{C _ {1} - Q _ {1} + Q _ {2}}\tag{A2}
$$

Rewriting the RHS of (1) as $C _ { 1 } - Q _ { 1 } / C _ { 1 }$ , it is apparent by inspection that the RHS of (A2) must be less than the RHS of (1), as long as $Q _ { 2 }$ $> Q _ { 1 }$ . Hence, if p is greater than the RHS of (1), it must be greater than the RHS of (A2).

(iv): (HIGH, HIGH) is Pareto superior to (LOW, LOW) but not a Nash equilibrium for the values of p between the RHS of (1) and (A2). ▫

Section 3.1. Assume first the availability of historical information on how estimated task duration, $E _ { t } ,$ relates to actual task duration, $A _ { t } .$ . For a sample of z tasks, the ratio $E _ { t } / A _ { t }$ will form a distribution with mean value that is near 1. The severity of overrun or underrun of the task is expressed as a proportion: $1 \mathrm { ~ - ~ } E _ { t } / \mathrm { A _ { t } }$ . Costs vary as $E _ { t } / A _ { t }$ <sub>t</sub> grows farther from 1, increasing in $\mid 1 - E _ { t } / A _ { t } \mid$ . Suppose costs of overrun and underrun are symmetric and can be expressed as a quadratic function of $E _ { t } / A _ { t } ;$ then

$$
\text { Total   Error   Cost } = \sum_ {t = 1} ^ {T} K (E _ {t} / A _ {t} - 1) ^ {2}\tag{A3}
$$

where K is a parameter of the cost function. To change this total, a principal might establish a policy of systematically adjusting estimates by multiplying them by some factor, b. In other words, a prin cipal might obtain a best estimate from whatever source, then add, say, 50% to it. This would be the equivalent of setting $b = 1 . 5 .$ The optimal value of b can be determined by standard calculus methods. Let

$$
\text { Adjusted   Total   Error   Cost } = \sum_ {t = 1} ^ {T} K (b E _ {t} / A _ {t} - 1) ^ {2},\tag{A4}
$$

and find the optimal value of b such that d (Adjusted Total Error $\mathrm { C o s t } ) / d b = 0$ . The result:

$$
\mathsf {b} = \sum_ {t = 1} ^ {T} (E _ {t} / A _ {t}) / \sum_ {t - 1} ^ {T} (E _ {t} ^ {2} / A _ {t} ^ {2}).\tag{A5}
$$

The analysis can be adjusted to account for cost asymmetry by redefining

$$
\begin{array}{r l} \text { Adjusted   Total   Error   Cost } & = \Sigma^ {\text { over }} K _ {1} (b E _ {t} / A _ {t} - 1) ^ {2} \\ & + \Sigma^ {\text { under }} K _ {2} (b E _ {t} / A _ {t} - 1) ^ {2} \end{array}\tag{A6}
$$

where $\Sigma ^ { o v e r }$ is the sum over all t such that $1 - E _ { t } / A _ { t } < 0$ (overestimates) and $\Sigma ^ { u n d e r }$ is the sum over all t such that $1 - E _ { t } / A _ { t } > 0$ (underestimates), and minimizing by any convenient method. ▫

Section 4.1. Recall from (1) that (HIGH, HIGH) is an equilibrium when

$$
p \geq 1 - \frac {Q _ {1}}{C}.
$$

For $Q _ { 1 } > C ,$ , this expression is always true; p is an element of [0,1] and the RHS of (1) is always negative. Recall from (A2) that (HIGH, HIGH) is Pareto superior to (LOW, LOW) when

$$
p > \frac {C _ {1} - Q _ {1}}{C _ {1} - Q _ {1} + Q _ {2}}.
$$

Again, for $Q _ { t } > C ,$ , this expression is always true; p is an element of [0,1] and the RHS of (A2) is always negative. ▫

## References

Abdel-Hamid, T., K. Sengupta, D. Ronan. 1993. Software project control: An experimental investigation of judgment with fallible information. IEEE Trans. Software Engrg. 19(6) 603–612.

——, S. Madnick. 1986. The impact of schedule estimation on software project behavior. IEEE Software. 3(4).

——. 1989. Lessons learned from modeling the dynamics of software development. Comm. ACM. 32(12) 1426–1435.

Alchian, A. A., H. Demsetz. 1972. Production information costs, and economic organization. Amer. Econom. Rev. 62(5) 777–795.

Argyris, C. 1952. The Impacts of Budgets on People. Controllership Foundation, New York.

Austin, R. D. 1996. Measuring and Managing Performance in Organizations. Dorset House, New York.

Blau, P. M. 1963. The Dynamics of Bureaucracy: A Study of Interpersonal Relations in Two Government Agencies, 2<sup>nd</sup> ed. The University of Chicago Press, Chicago, IL.

Boehm, B. W. 1981. Software Engineering Economics. Prentice-Hall Englewood Cliffs, NJ.

Brooks, Jr. F. P. 1975. The Mythical Man-Month: Essays on Software Engineering. Addison-Wesley Publishing Company, Reading, MA.

——. 1987. No silver bullet: Essence and accidents of software engineering. IEEE Comput. 20(4) 10–19.

Curtis, W. 1984. Fifteen years of psychology in software engineering: Individual differences and cognitive science. Proc. Seventh Internat. Conf. Software Engrg. 97–106 Orlando, FL.

——. 1997. What if programmers were treated like jocks? Amer. Programmer. 10(5) 21–28.

Cusumano, M. A., R. W. Selby. 1997. Microsoft’s weaknesses in software development. Amer. Programmer. 10(10).

DeMarco, T. 1982. Controlling Software Projects. Yourdon Press, A Prentice-Hall Company, Englewood Cliffs, NJ.

——. 1995. Why Does Software Cost So Much? Dorset House Publishing.

——. 1997. Personal communication.

Deming, W. E. 1986. Out of the Crisis. MIT Center For Advanced Engineering Study, Cambridge, MA.

Gutierrez, G. J., P. Kouvelis. 1991. Parkinson’s law and its implications for project management. Management Sci. 37(8) 990–1001.

Holmstrom, B. 1979. Moral hazard and observability. Bell J. Econom. 10 74–91.

——, R. Milgrom. 1991. Multi-task principal-agent analyses: Incentive contracts, asset ownership, and job design. J. Law, Econom. Organ. 7 (Spring) 25–52.

Iansiti, M., G. Gill. 1990. Microsoft corporation: Office business unit. Harvard Business School Case, 9-691-033, Boston, MA.

Jensen, M. C., W. H. Meckling. 1976. Theory of the firm: Managerial behavior, agency costs and ownership structure. J. Financial Econom. 3 305–60.

Kadane J., P. D. Larkey. 1982. Subjective probability and the theory of games. Management Sci. 28 113–120.

Kahneman, D., A. Tversky. 1979. Prospect theory: An analysis of decision under risk. Econometrica. 47 263–291.

Kerr, S. 1975. On the folly of rewarding A, while hoping for B. Acad. Management J. 18(4) 769–783.

King, W. R., T. A. Wilson. 1967. Subjective time estimates in critical path planning—a preliminary analysis. Management Sci. 13(5) 307–320.

Kohn, A. 1993. Why work incentives fall down on the job. USA To day. (December 16).

Larkey, P., J. Caulkins. 1992. All above average and other unintended consequences of performance appraisal systems. Paper presented at the National Public Management Res. Conf. Technology

and Inform. Policy Program, The Maxwell School, Syracuse University, Syracuse, NY.

MacCormack, A., R. Verganti, M. Iansiti. 1999. Developing products on “internet time”: The anatomy of a flexible development process. Working Paper, Harvard Business School, Boston, MA.

Milgrom, P., J. Roberts. 1992. Economics, Organization and Management. Prentice-Hall, Englewood Cliffs, NJ.

Parkinson, C. N. 1962. In-laws and Outlaws and Parkinson’s Third Law. The Riverside Press, Cambridge, MA.

Pate-Cornell, M. E. 1990. Organizational aspects of engineering system safety: The case of offshore platforms. Science 30 1210–1216.

Ridgway, V. F. 1956. Dysfunctional consequences of performance measurements. Admin. Sci. Quart. 1(2) 240–247.

Ross, S. 1973. The economic theory of agency: The principal’s problem. Amer. Econom. Rev. 63 134–139.

Simon, H. A. 1991. Organizations and markets. J. Econom. Perspectives. 5(1) 25–44.

Staw, B. M. 1982. Counterforces to change. P. S., Goodman ed. Change in Organizations. Jossey-Bass, San Francisco, CA.

Tomayko, J. E. 1987. Teaching a Project-Intensive Introduction to Software Engineering. Software Engineering Institute Technical Report, CMU/SEI-87-TR-20, Pittsburgh, PA.

Umpathy, S. 1987. Current Budgeting Practices in U.S. Industry: The State of the Art. Quorum Books, New York.

Yourdon, E. 1997. Personal communication.

Robert Kauffman, Associate Editor. This paper was received on August 30, 1995, and was with the author 22 months for 3 revisions.
