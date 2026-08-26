---
otero_id: 17519
otero_key: "UF4QZE45"
title: "A dual-motive heuristic for member information initiation in group decision making: Managing risk and commitment"
authors: "Steven D. Silver"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00050-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A dual-motive heuristic for member information initiation in group decision making: Managing risk and commitment \*

Steven D. Silver

Laboratory for Social Research, Stanford University, Stanford, CA 94305-2074, USA

## Abstract

Information exchange in the decision making of interactive groups is examined at the level of individual group members. I recognize the dual or competing motives of members who act as both individuals and group members, and propose a two-stage heuristic for decisions on the type and amount of information they initiate. At the first stage, individual members intuit or solve the problem of maintaining their status in the group through information initiations that minimize the probability of receiving negative evaluations weighted by the sender's status. In the second stage, the member accepts some increment to this minimum to contribute to group decision quality. The increment the member accepts is proportional to his or her status and is the basis for the initiation of ideas and negative evaluations. The explicit forms that are proposed for the solution of the two-stage problem allow the quality-maximizing probability of an idea to be expressed in terms of a member's status. This result is used to examine a conjecture on status distributions and the probability of idea initiations that maximize the quality of a group decision. Initial evidence from recent studies that supports assumptions of this work is presented, and the capability of procedures in computer-mediated information exchange to maintain the exchange of ideas and negative evaluations at quality maximizing rates is noted.

Keywords: Group decision making; Information exchange; Status processes; Social risk

## 1. Introduction

Although the importance of managerial decision making by groups or teams has received increasing recognition [17], the underlying processes remain arcane in their complexity to many observers and investigators $^{1}$ . The recent interest in groups in organizations has renewed efforts to increase the efficacy of interacting groups (e.g., [32], [29]). In support of this end, it is timely to expand conceptual frameworks that focus upon agents in groups as the unit of the analysis.

The complexity of decision making in interactive groups is perhaps most recognizable in cases which have been classified as ill-structured (e.g., [28]). Decisions in this category generally lack adequate information on constituent events for the application of algorithmic decision rules by decision-makers [18]. As a consequence, decisions are made through what has been referred to as judgmental decision procedures. These procedures involve minimally structured information exchange in which ideas and evaluations have particular importance. Examples of decisions in this category are those organizations face in resource deployment under uncertainty, as in long term strategic planning.

In this work, I will address information exchange in ill-structured decision making by interactive groups. I will examine the agent's complex decision on information initiation in groups whose members are unequal in their statuses. My interest is in representing the decision by members who act both as individual agents and as a members of the collective. I will emphasize the status distribution of members as it organizes information initiation, especially the initiation of negative evaluations ([3], [26]). The connections of the exposition to social exchange theory (e.g., [7], [4]) will be evident, although the framework is not formally invoked here.

Explicit and defensible behavioral assumptions in the exposition will be used to support analytic inferences on group decision-making and status distributions when the complex motives of agents are given representation. Preliminary evidence on these inferences will then be reviewed. The inquiry will propose heuristics that recognize the limitations on exchange imposed by the motives of individual members in serving their own and group objectives. I give primary attention to the initiation of ideas and negative evaluations in the analyses, since these information types are (1) instrumental in the production of quality in decisions, and (2) have important dependencies on the status distribution in the group.

The exposition will recognize that demands on agents to initiate information both as individuals and as members of a collective often conflict because the objectives of these different roles are generally inconsistent. Since individual group members can lose status within the group by sending messages that are negatively evaluated by influential group members, an agent acting for him or herself will often have a well defined agenda when initiating information as a group member. This agenda may commonly be inconsistent with group objectives.

The goal of the group with respect to the initiation of ideas is generally straightforward, viz to maximize the number of ideas that members exchange. Negative evaluations are critical regulators of behavior, including the rate of idea generation in the group. The number of ideas exchanged is naturally bounded by the limited number of ideas that members can generate. The rate at which negative evaluations are initiated has few bounds and will be seen as a key influence on the number and quality of ideas and, decision outputs.

## 2. Member decisions on the exchange of task information

I will begin by conceptualizing the initiation of information by the member who acts as a “dual motive” agent (see, [5], [15], on mixed motives), who has interests in both maintaining his or her own status and in contributing to the group objective. I believe individuals commonly use heuristics that accommodate both these motives. In agreement with Hogarth’s [10] observation on the use of ordered heuristics to simplify complex decisions, I conceptualize the agent as following sequential heuristics in this decision. The heuristics are not claimed to be explicit calculations of solutions to the problem of information initiation. Rather, they are procedures which decision makers find to approximate adequate solutions. My end will be to formalize the heuristics and use the formalization for inference on processes of group information exchange.

I propose the following as requisite conditions for the social process that I describe to be operative in information exchange:

(1) Members occupying positions in a group have some basis to judge their own relative status position.

(2) Members are motivated to avoid status loss.

The motive to avoid status loss is greater than the motive to gain status.

(3) Members are motivated to contribute to the group objective.

(4) Members expect that the amount and type of information they send will influence the amount and type of information they receive. Thus, they at least implicitly recognize the causal relationship between information initiation and evaluation by others.

Minimizing status loss in information initiation. I have argued that status maintenance is a motive that is fundamental to decision makers. I therefore begin by modelling the objective of minimizing status loss. For this problem, status loss is considered to occur through the receipt of negative evaluations from other group members. The magnitude of the loss from a negative evaluation is further seen as proportional to the status distance between the source and target of an evaluation. To write the problem, I define a matrix that represents the unconditional probabilities of message types a group member sends to the rest of the group. For a four-person group, the entries of the matrix for member 1 are as follows:

$$
\begin{array}{l}\mathrm{P} _ {1 2} = \operatorname * {P r} [ \mathrm{P} (1 \rightarrow 2) ] \mathrm{N} _ {1 2} = \operatorname * {P r} [ \mathrm{N} (1 \rightarrow 2) ]\\\mathrm{O} _ {1 2} = \operatorname * {P r} [ \mathrm{O} (1 \rightarrow 2) ]\\\mathrm{P} _ {1 3} = \operatorname * {P r} [ \mathrm{P} (1 \rightarrow 3) ] \mathrm{N} _ {1 3} = \operatorname * {P r} [ \mathrm{N} (1 \rightarrow 3) ]\\\mathrm{O} _ {1 3} = \operatorname * {P r} [ \mathrm{O} (1 \rightarrow 3) ]\\\mathrm{P} _ {1 4} = \operatorname * {P r} [ \mathrm{P} (1 \rightarrow 4) ] \mathrm{N} _ {1 4} = \operatorname * {P r} [ \mathrm{N} (1 \rightarrow 4) ]\\\mathrm{O} _ {1 4} = \operatorname * {P r} [ \mathrm{O} (1 \rightarrow 4) ]\\\mathrm{P} _ {1 \Sigma} = \operatorname * {P r} [ \mathrm{P} (1 \rightarrow \Sigma) ] \mathrm{N} _ {1 \Sigma} = \operatorname * {P r} [ \mathrm{N} (1 \rightarrow \Sigma) ]\\\mathrm{O} _ {1 \Sigma} = \operatorname * {P r} [ \mathrm{O} (1 \rightarrow \Sigma) ]\\\mathrm{I} _ {1 \Sigma} = \operatorname * {P r} [ \mathrm{I} (1 \rightarrow \Sigma) ]\end{array}
$$

where I denotes ideas, N and P are negative and positive evaluations, respectively, and O denotes all other information categories including the information types of data/facts and questions and the case of no response to a message (a “blank”) $^{2}$ . The symbol, $\Sigma$ , denotes the entire group as the target of a message.

Since ideas are predominantly sent to the group, I limit the initiation of this message type to the single case $(1 \rightarrow \Sigma)$ . $P_{12}, \ldots, I_{1\Sigma}$ will hereafter be used to denote $\Pr[P(1 \rightarrow 2)], \ldots, \Pr[I(1 \rightarrow \Sigma)]$ .

## 3. The minimization problem

Group members are seen as first attempting to comprehend the message initiations in the exchange of information that will minimize the status-weighted negative evaluations they receive. The constrained problem of minimizing the sum of status weighted probability of a negative evaluation from all messages initiated by the $i^{th}$ group member can be written as:

$$
\begin{array}{l} \min \sum_ {j \neq i} \left(\sum_ {X = P, N, O} \operatorname * {P r} \big (N _ {j i} | X _ {i j} \big) \sigma_ {j} \operatorname * {P r} \big (X _ {i j} \big) \right. \\ \left. + \sum_ {X = I, O} \operatorname * {P r} \big (N _ {j i} | X _ {i \Sigma} \big) \sigma_ {j} \operatorname * {P r} (X _ {i \Sigma})\right) \end{array}\tag{1}
$$

$$
\text { s.t. } \sum_ {\mathrm{j} \neq \mathrm{i}} \sum_ {\mathrm{X} = \mathrm{P}, \mathrm{N}, \mathrm{O}} \operatorname * {P r} \left(\mathrm{X} _ {\mathrm{ij}}\right) + \sum_ {\mathrm{I}, \mathrm{O}} \operatorname * {P r} \left(\mathrm{X} _ {\mathrm{i} \Sigma}\right) = 1\tag{2}
$$

$$
\operatorname * {P r} \left(\mathrm{X} _ {\mathrm{ij}}\right), \operatorname * {P r} \left(\mathrm{X} _ {\mathrm{i} \Sigma}\right) \geq 0, \text { all } j \neq i, \text { for   each } j \neq i\tag{3}
$$

$$
\sum_ {j = 1} ^ {4} \mathrm{P} _ {i j} \leq \mathrm{P} _ {\mathrm{p}}\tag{4}
$$

where X = P, N, O, I, and $\sigma_{j}$ is the judged status of j by i and $P_{p}$ is the upper bound for the credible probability of sending positive evaluations in the interaction period. I assume that each member has a maximum probability of sending positive evaluations that varies with his or her relative status in the group. When this bound is exceeded (e.g., when a member sends only positive evaluations), $N_{ji}|P_{ij}$ increases by a large magnitude.

The objective, Eq. (1), is defined in terms of the sum of the status weighted probabilities of receiving a negative evaluation from messages sent either to individuals or to the group as an entity, respectively. The constraints (2) and (3) are the standard requirements that the probability of all acts fill the probability space and be non-negative. Constraint (4) bounds $\Sigma P$ at $P_{p}$ .

I further make the intuitively reasonable assumption on the ordering of the conditional probabilities of being negatively evaluated for initiating an information type:

$$
\begin{array}{r l} \operatorname * {P r} \bigl (N _ {j i} | N _ {i j} \bigr) & > \operatorname * {P r} \bigl (N _ {j i} | I _ {i \Sigma} \bigr) > \operatorname * {P r} \bigl (N _ {j i} | O _ {i j} \bigr) \\ & = \operatorname * {P r} \bigl (N _ {j i} | O _ {i \Sigma} \bigr) > \operatorname * {P r} \bigl (N _ {j i} | P _ {i j} \bigr) \end{array}
$$

That is, the conditional probability of receiving a negative evaluation is highest for sending a negative evaluation and lowest for sending a positive evaluation. Note that I claim that, in general, sending a positive evaluation has a lower conditional probability of receiving a negative evaluation than sending an O category message does. This is because a positive evaluation conveys favourable judgments of others and is status increasing to them in public exchanges, whereas an O category message is more “neutral.”

Given the above, the solution to the minimization is clear. Since P is bounded by $P_{p}$ and $\Pr(O)$ is bounded only at 1, one would send only positive evaluations until $P_{p}$ is reached, and then send O category messages. Since $\Pr(N_{ji}|O_{ij}) > \Pr(N_{ji}|P_{ij})$ , it further follows that sending a positive evaluation to a higher status person and a blank to a lower status person will increase the objective function (status weighted probability of receiving a negative evaluation) less than sending a positive evaluation to a low status person and a blank to a high status person. Since one is seeking to minimize the objective, one would consequently send all positive evaluations to the high status person.

Because of the bound $P_{p}$ in (4), the minimization problem reduces to:

$$
\begin{array}{l} \min \left[ \sum_ {j = 2} ^ {4} \sigma_ {j} \operatorname * {P r} \left(N _ {j i} | P _ {i j}\right) \operatorname * {P r} \left(P _ {i j}\right) \right. \\ \left. + \sum_ {j = 2} ^ {4} \sigma_ {j} \operatorname * {P r} \left(N _ {j i} | O _ {i j}\right) \operatorname * {P r} \left(O _ {i j}\right) \right] \end{array}\tag{5}
$$

$$
\text {s.t.} \left\{ \begin{array}{c c} \sum_ {j = 2} ^ {4} \operatorname * {P r} \bigl (\mathrm{P} _ {\mathrm{ij}} \leq \mathrm{P} _ {\mathrm{p}} \bigr) & \\ \operatorname * {P r} \bigl (\mathrm{P} _ {\mathrm{ji}} \bigr) \geq 0 & \end{array} \right. \text {s.t.} \operatorname * {P r} \bigl (\mathrm{O} _ {\mathrm{ji}} \bigr) \geq 0
$$

Since the solution is only in $\Pr(\mathbf{P})$ and $\Pr(\mathbf{O})$ , and $\sum_{j\neq i}\Pr(\mathrm{O}_{ij})=1-\sum\Pr(\mathrm{P}_{ij})$ the objective can be written as:

$$
\begin{array}{l} \min \sum_ {j \neq i} \sigma_ {j} \operatorname * {P r} \left(N _ {j i} | P _ {i j}\right) \operatorname * {P r} \left(P _ {i j}\right) \\ + \sum_ {j \neq i} \sigma_ {j} \operatorname * {P r} \left(N _ {j i} | O _ {i j}\right) \left(1 - \operatorname * {P r} \left(P _ {i j}\right) \right. \end{array}
$$

The terms may then be rearranged so that the problem is:

$$
\begin{array}{l} \min \sum_ {j \neq i} \sigma_ {j} \operatorname * {P r} \left(N _ {j i} | O _ {i j}\right) - \sum_ {j \neq i} \sigma_ {j} \operatorname * {P r} \left(P _ {i j}\right) \left[ \operatorname * {P r} \left(N _ {j i} | O _ {i j}\right) - \operatorname * {P r} \left(N _ {j i} | P _ {i j}\right) \right] \end{array}\tag{6}
$$

The first term of (6) is independent of $\Pr(\mathrm{P}_{ij})$ . Since $\Pr(\mathrm{N}_{ji}|\mathrm{X}_{ij})$ is defined, $\Pr(\mathrm{P}_{ij})$ is the only undefined variable in (6), and therefore is constant. I assume $\Pr(\mathrm{N}_{ji}|\mathrm{P}_{ij})$ and $\Pr(\mathrm{N}_{ji}|\mathrm{O}_{ij})$ are increasing with the status of the $j^{th}$ member, and that $\sigma_{j}[\Pr(\mathrm{N}_{ji}|\mathrm{O}_{ij}) - \Pr(\mathrm{N}_{ji}|\mathrm{P}_{ij})]$ is positive and increasing in the status of j. Therefore, to minimize the sum, $\Sigma_{j\neq i}\sigma_{j}\Pr(\mathrm{P}_{ij})$ in the second term is maximized. This occurs when j is set equal to the highest status group member and the probability of sending a positive evaluation to this member is set at the maximum level of $P_{p}$ . By definition, O category messages are sent to everyone else in the group. Thus, the solution to the minimization of status loss at this stage is to send positive evaluations to the highest status member until the bound of credibility for this information type is reached. Then O category messages, including blanks, are sent to everyone including the high status member.

These results indicate that under an objective of minimizing status weighted negative evaluations, (1) no ideas or negative evaluations will be initiated, and that (2) the high status member will over-receive positive evaluations because of his or her position. Moreover, the solution suggests that one will expect to see a high probability of message types in the O category which have low social risk (e.g., data), whether or not the information contributes to the task. This is a consequence of the upper bound on sending positive evaluations and the comparatively low probability of receiving a negative evaluation for sending O-category messages.

The (1) zero (or very low) proportions of ideas or negative evaluations, (2) high proportions of positive evaluations sent to high status members, and (3) high proportions of blanks (low participation) indicated by the solution of this minimization problem are commonly seen in groups with large status distances between members and low commitment to group objectives by medium and low status members.

Although I believe such heuristic solutions to the minimization problem that has been described are intuitively realized by most group members, and thus “available” [15], they are not implemented in their strict forms in most cohesive groups because the goals of most group members do not solely lie in status maintenance (i.e., the minimization of the sum of the status weighted negative evaluations one receives in information exchange). In the subsection to follow, I will elaborate on a representation of the more complex objectives group members face and their implications for the exchange of task information.

## 4. Contributing to group decision quality

I hypothesize here that individuals treat their heuristic solutions to the problem of maintaining their status as constraints of the number, type, and recipient of messages they are willing to initiate, and then consider the objective on maximizing the quality of group decisions in a global decision on information initiation. I have previously argued that this is a shared objective in cohesive groups. I further claim that ideas and negative evaluations are the most important contributors to the quality of group decisions, although sending both of these information types have higher expected status costs than sending data, questions, or positive evaluations.

To conceptualize the operation of these dual motives, I begin with the simple assumption that the $i^{th}$ group member is willing to accept some increment, $\epsilon_{i}$ , to min $\sum_{j\neq i}\sigma_{j}\Pr(N_{ji})=n_{i,\min}$ (the minimized status-weighted sum of the probability of receiving negative evaluations from each of m other group members). This increment to the minimized status loss is accepted as contributing to the group goal of decision quality. Moreover, the magnitude of the increment, $\epsilon_{i}$ , is considered to be an increasing function of the member's perceived status in the group, i.e., $\epsilon_{i}=\epsilon(\sigma_{i})$ . The second stage problem for the group member in terms of a group quality objective can then be written as:

max Q

$$
\begin{array}{l} \text {s.t.} \sum_ {\mathrm{j} \neq \mathrm{i}} \sum_ {\mathrm{x} = \mathrm{P}, \mathrm{N}, \mathrm{O}} \operatorname * {P r} \left(\mathrm{N} _ {\mathrm{ji}} | \mathrm{X} _ {\mathrm{ij}}\right) \sigma_ {\mathrm{j}} \operatorname * {P r} \left(\mathrm{X} _ {\mathrm{ij}}\right) \\ + \sum_ {\mathrm{x} = \mathrm{I}, \mathrm{O}} \operatorname * {P r} \left(\mathrm{N} _ {\mathrm{ji}} | \mathrm{X} _ {\mathrm{i} \Sigma}\right) \sigma_ {\mathrm{j}} \operatorname * {P r} \mathrm{X} _ {\mathrm{i} \Sigma} \\ \leq \mathrm{n} _ {\mathrm{i}, \min} (1 + \epsilon) = \mathrm{n} _ {\mathrm{i}, \max} \end{array}
$$

and (2) and (3) hold for each group member where Q is the quality of the group's decision, $n_{i,min}$ is as above, and $n_{i,max}$ is an upper bound on the summed probability of receiving a negative evaluation from other group members that a member judges he or she can attain (i.e., the solution to Eq. (6)), $\epsilon = \epsilon(\sigma_{i})$ is the increment in $n_{i,min}$ that the member is willing to accept to contribute to the quality objective, and $n_{i,max}$ is the maximum status weighted probability of receiving negative evaluations for the group that the member is willing to accept after adjusting for his or her contribution to the group quality objective.

## 5. The quality maximization problem

Solving the quality maximization problem. To solve the constrained quality maximization problem, the member-agent requires knowledge or assumptions on:

(1) The contribution of information types of ideas and negative evaluations to quality, i.e., $Q = Q[\mathrm{Pr}(\mathrm{I}_{\mathrm{i}}), \mathrm{Pr}(\mathrm{N}_{\mathrm{i}})]$ .

(2) An explicit form for setting the level of $\epsilon$ (in place of the general form, $\epsilon_{i} = \epsilon(\sigma_{i})$ ).

## 6. Producing decision quality from ideas and evaluations

To develop an explicit form for the production of quality in decisions from ideas and negative evaluations, I begin with two assumptions on the production of decision quality. Both of these assumptions are discussed in previous works ([26], [3]).

Assumption (1.0). Quality in group idea generation is monotonically increasing in idea number.

Assumption (2.0). Quality in group idea generation is a quadratic (concave down) function of the number of negative evaluations exchanged.

The first of the above assumptions follows from consistent findings that idea uncommonness is increasing across ideas in the sequence in which they are generated (e.g., [1]). It suggests that maximizing the number of ideas is one part of a quality-maximizing procedure $^{3}$ .

The second assumption follows from the observation that while negative evaluations contribute to the sorting of ideas on quality, too many negatives can rapidly increase the expected cost of sending ideas (i.e., $\Pr(N_{ji}|I_{i\Sigma})$ , in the group) and inhibit the production of ideas. A first proposition follows from the above assumptions:

Proposition (1.0). Ideas and negative evaluations make the greatest contributions to quality when they occur in an ideal proportion.

From this proposition, the normative goal of the group is to set the total number of negative evaluations exchanged in a decision at a level that is proportional to the number of ideas. The exact proportion will depend on the status distribution in the group, the type of decision and the group's interaction history. Generally, I expect the idea rate to be decreasing over the group's interaction time and negative evaluations to increase in their contribution to quality as the cumulative sorting requirement increases (see, for example, [26]). Thus, the group-maximizing ratio of ideas to negative evaluations (R) is considered to be time-varying and monotonically decreasing. I write this ratio as:

$$
\frac {\sum \operatorname * {P r} \left(\mathrm{I} _ {\mathrm{j} \Sigma}\right) _ {\mathrm{t}}}{\sum_ {\mathrm{j}} \sum_ {\mathrm{i} \neq \mathrm{j}} \operatorname * {P r} \left(\mathrm{N} _ {\mathrm{ji}}\right) _ {\mathrm{t}}} = R _ {\mathrm{t}}
$$

For the present static application, $R_{t}$ is approximated by the constant R.

A second proposition addresses the distribution of negative evaluations across group members:

Proposition (2.0). Negative evaluations contribute most to quality when they are distributed to members in proportion to the number of ideas these members have initiated.

Negative evaluations contribute to quality by sorting ideas and therefore should be sent to members in proportion to the number of ideas a member initiates. Procedures that result in such an allocation counter the tendency to oversend negative evaluations to lower status members and to undersend them to high status members.

## 7. A production function for decision quality

From propositions (1.0) and (2.0), a candidate for a member's quality objective can be written as:

$$
\begin{array}{r l} \mathrm {Q_ {i}} = & f \left[ \operatorname * {P r} (\mathrm {I_ {i\Sigma}}), \sum_ {\mathrm{j} \neq \mathrm{i}} \operatorname * {P r} (\mathrm {I_ {j\Sigma}}), \sum_ {\mathrm{j} \neq \mathrm{i}} \operatorname * {P r} (\mathrm {N_ {ij}}), \mathrm{R} \right] \\ & - \sum_ {\mathrm{j}} \mathrm {M_ {c}} \left| \frac {\operatorname * {P r} (\mathrm {N_ {ij}})}{\sum_ {\mathrm{i} \neq \mathrm{j}} \operatorname * {P r} (\mathrm {N_ {ij}})} - \frac {\left(\operatorname * {P r} (\mathrm {I_ {j\Sigma}})\right)}{\sum_ {\mathrm{j}} \operatorname * {P r} (\mathrm {I_ {j\Sigma}})} \right| ^ {\delta} \end{array}\tag{7}
$$

where $Q_{i}$ is the contribution of the $i^{th}$ member to the quality of the group decision; R is the ideal ratio of negative evaluations to ideas; $Pr(I_{j\Sigma})$ is the probability of the $j^{th}$ member sending an idea to the group; and $M_{c}$ is a scaling constant. $\delta$ is the sensitivity of quality to the absolute value of deviations from the optimal distribution of negative evaluations among members, and $\delta \geq 1$ .

The first term in (7) is the general form for the production of quality from ideas and negative evaluations; I will consider specific forms for this term below. The second term is the allocation rule for negative evaluations from proposition (2.0). This term penalizes quality for negative evaluations that are not distributed according to the production of ideas by group members.

The production of idea quality from negative evaluations and ideas. Having provided a general form for the group's objective function, specific functional forms for quality production from ideas and negative evaluations may now be considered. From Assumptions (1.0) and (2.0), I write a quality production function (the first term of the RHS of (7)) for each member that is (1) increasing in ideas, and (2) requires negative evaluations to be proportional to ideas as:

$$
\begin{array}{l} \mathrm{f} \left[ \operatorname * {P r} \left(\mathrm{I} _ {\mathrm{i} \Sigma}\right), \sum_ {\mathrm{j} \neq \mathrm{i}} \operatorname * {P r} \left(\mathrm{I} _ {\mathrm{j} \Sigma}\right), \sum_ {\mathrm{j} \neq \mathrm{i}} \operatorname * {P r} \left(\mathrm{N} _ {\mathrm{ij}}\right), \mathrm{R} \right] \\ = \operatorname * {P r} \left(\mathrm{I} _ {\mathrm{i} \Sigma}\right) - \alpha \left| \sum_ {\mathrm{j} \neq \mathrm{i}} \operatorname * {P r} \left(\mathrm{I} _ {\mathrm{j} \Sigma}\right) - \mathrm{R} \sum_ {\mathrm{j} \neq \mathrm{i}} \operatorname * {P r} \left(\mathrm{N} _ {\mathrm{ij}}\right) \right| ^ {\beta}, \\ \alpha \geq 0, \beta \geq 1 \end{array}\tag{8}
$$

In (8), the exponent, $\beta$ , determines the sensitivity of quality to the absolute value of deviations from the optimal ratio $^{4}$ . The first term of (8) indicates that quality is increasing in the probability of an idea. The second term indicates that quality also depends on setting a probability of sending a negative evaluation which is proportional to other members' probabilities of sending an idea.

8. Incrementing the minimized probability of receiving a negative evaluation to increase decision quality

I next give an explicit form to $\epsilon$ , the increment to $n_{i,\min}$ (the minimized status-weighted probability of a negative evaluation the $i^{th}$ group member can receive while participating in the group's information exchange). This form is written as the concave increasing function $\epsilon(\sigma_{i}) = c_{i}\sigma_{j}^{\theta}$ , where $0 < \theta < 1$ . The form implies that the magnitude of the status weighted negative evaluations a group member will accept to contribute to group quality increases at a decreasing rate as his or her relative status increases.

## 9. The decision quality maximization problem

Forms for the quality production function and the increment to $n_{i,min}$ , the minimized status weighted probability of a negative evaluation have now been proposed. With these forms, I write a more complete form for the group members' problem of maximizing their contribution to the quality of the group decision, subject to a constraint on the acceptable status-weighted probability of receiving a negative evaluation.

$$
\begin{array}{l} \max Q _ {i} = \max \left(\operatorname * {P r} (I _ {i \Sigma})\right) - \alpha | \Sigma \operatorname * {P r} (I _ {j \Sigma}) \\ \quad - R \sum_ {j \neq i} \operatorname * {P r} (N _ {i j}) | ^ {2} \\ \quad - \sum_ {j} M _ {c} \left| \frac {\sum_ {j} \operatorname * {P r} (N _ {i j})}{\sum_ {j} \sum_ {i \neq j} \operatorname * {P r} (N _ {i j})} - \frac {\operatorname * {P r} (I _ {j \Sigma})}{\sum_ {j} \operatorname * {P r} (I _ {j \Sigma})} \right| ^ {2} \\ \text {s.t.} \sum_ {j} \Sigma \sigma_ {j} \operatorname * {P r} (N _ {j i} | X _ {i j}) \operatorname * {P r} (X _ {i j}) \leq n _ {i, \min} (1 + c _ {1} \sigma_ {i} ^ {\theta}), \\ \quad \theta \leq 1, \text {for each i.} \\ \sum_ {X = P, N, O} \operatorname * {P r} (X _ {i j}) = 1, \\ \sum_ {X = I, O} \operatorname * {P r} (X _ {i \Sigma}) = 1, \Sigma \operatorname * {P r} (P _ {i j}) \leq P _ {p}, \operatorname * {P r} (X _ {i j}) \geq 0 \end{array} \tag {9}
$$

where $n_{i,\min}(1+c_{1}\sigma_{i}^{\theta})=n_{i,\max}$ is the maximum sum of the probabilities of receiving a negative evaluation from all other group members that is acceptable to the member. For other constants, $\alpha\geq0$ , $\beta>1$ , $c_{1}\leq0$ . I have set $\beta$ , $\delta=2$ , for this problem.

Eq. (9) and the constraints that group members face define the quality maximization problem. In this problem, members seek to maximize their contribution to the quality of group decisions subject to the constraints of the maximum status weighted probability of a negative evaluation they are willing to receive in contributing to the group quality objective. From this explicit form for the quality function, I now begin to investigate both idea and quality production as a function of the status distribution of group members in limited cases.

## 10. Quality-maximizing information exchange

In this section, the claim that the quality-maximizing probability of an idea in a group occurs when members have equal status is directly addressed. I begin with a case of dyads. Consideration of this case increases tractability in analysis, since the objective function will not require a term for the distribution of negative evaluations among members (i.e., the third term of the RHS of eq. (9)). I thus write the constrained problem of maximizing decision quality, with possible actions given by $\Pr(I_{i})$ , $\Pr(N_{i})$ , and $\Pr(O_{i})$ , as follows:

$$
\begin{array}{l} \max Q = \sum_ {i = 1, 2} \operatorname * {P r} (I _ {i}) - \alpha \left[ \operatorname * {P r} (I _ {j}) - R \operatorname * {P r} (N _ {i}) \right] ^ {2}, \\ \text {ifj} = 1, i = 2, \text {and vice versa.} \\ \text {s.t.} \left\{ \begin{array}{c} n _ {1, i} \operatorname * {P r} (O _ {i}) + n _ {2, i} \operatorname * {P r} (N _ {i}) + n _ {3, i} \operatorname * {P r} (I _ {i}) \\ = \sigma_ {j} \operatorname * {P r} N _ {j}, i = 1, 2, \\ \sigma_ {j} \operatorname * {P r} (N _ {j}) \leq n _ {i, \max} = n _ {i, \min} (1 + c _ {1} \sigma_ {i} ^ {\theta}), i = 1, 2; \\ \text {ifj} = 1, i = 2, \text {and vice versa}, c _ {1} = 1 \end{array} \right. \\ \operatorname * {P r} (O _ {i}) + \operatorname * {P r} (N _ {i}) + \operatorname * {P r} (I _ {i}) = 1, i = 1, 2 \\ \operatorname * {P r} (O _ {i}), \operatorname * {P r} (N _ {i}), \operatorname * {P r} (I _ {i}) \geq 0 \\ \text {where} \\ n _ {1, i} = \sigma_ {j} \operatorname * {P r} (N _ {j} | O _ {i}), n _ {2, i} = \sigma_ {j} \operatorname * {P r} (N _ {j} | N _ {i}), \\ n _ {3, i} = \sigma_ {j} \operatorname * {P r} (N _ {j} | I _ {i}), \end{array}
$$

and $n_{i,max}$ is the maximum number of status-weighted negative evaluations that the $i^{th}$ group member is willing to accept.

To solve this problem and examine the relationship between the quality-maximizing probability of an idea and the distribution of status in the dyad, I proceed as follows. I first show that maximum quality occurs when a member sends as many ideas and negative evaluations as the constraint allows (i.e., $\Pr(N_{i})$ is set at $\Pr(N_{i,\max}) = N_{i,\max}$ ). I then use this result to derive a reduced-form expression for the $\Pr(I_{i})$ that maximizes decision quality in terms of $\Pr(N_{i})$ and $\Pr(N_{j})$ . Finally, I use this reduced-form expression to examine the distribution of status under which the quality-maximizing probability of an idea initiation occurs.

From the constraints, the minimum attainable $\Pr(N_{i})$ can be written as:

$$
\mathrm{N} _ {\mathrm{i}, \min} = \mathrm{N} _ {\min} = \frac {\operatorname* {P r} \left(\mathrm{N} _ {\mathrm{j}} \mid \mathrm{O} _ {\mathrm{i}}\right)}{\operatorname* {P r} \left(\mathrm{N} _ {\mathrm{j}} \mid \mathrm{O} _ {\mathrm{i}}\right) - \operatorname* {P r} \left(\mathrm{N} _ {\mathrm{j}} \mid \mathrm{N} _ {\mathrm{i}}\right) + 1}
$$

Analytically finding the $\Pr(N_{i})$ and $\Pr(N_{j})$ that maximize Q leads to a solution with relationships among the conditional probabilities and constants that are complex and difficult to interpret. I thus use a numerical exercise to show that, for this problem, $Q_{max}$ , the maximized decision quality in the dyad, occurs when $\Pr(N_{i}) = N_{i,\max}$ .

This contention is demonstrated for an interval of parameter values around the best estimate of the key parameters for the objective and its constraints. For the estimate, I use the following conditional probabilities and constraints from an experimental study of information exchange: $\Pr(N_{j}|I_{i}) = .09$ ; $\Pr(N_{j}|O_{i}) = .007$ ; $\Pr(N_{j}|N_{i}) = .14$ ; R = 10; initially, $\alpha = .10$ . Procedures for this study follow those reported in [24] and described later in this paper.

In a series of numerical exercises, the quality estimates from eq. (9), with the values of the parameters varied between 0.5 and 2.0 times each of the above parameter estimates were examined. I thus examined four evenly spaced points in the 0.5 to 2.0 range of the initial estimates of the above parameters, and four evenly spaced points in the (0,1) interval for $\sigma_{i}$ and $\theta_{i}$ . For the total of $4^{7}$ combinations of parameters examined, quality was found to be maximized when $\operatorname{Pr}(\mathbf{N}_{\mathrm{i}}) = \mathbf{N}_{\mathrm{i,max}}$ .

The results of this search procedure for a smooth quadratic objective function support the contention that the quality-maximizing $\Pr(I_{i})$ occurs when the constraint on $\Pr(N_{i})$ is set equal to $N_{i,max}$ .

Definition of the quality-maximizing $\Pr(N_{i})$ now allows us to find an expression for the quality-maximizing $\Pr(I_{i})$ . From the constraints, $\Pr(I_{i})$ may be expressed in terms of $\Pr(N_{i})$ and $\Pr(N_{j})$ as follows:

where

$$
\begin{array}{l} \mathrm {a_ {i}} = \frac {\operatorname * {P r} (\mathrm {N_ {j}} | \mathrm {O_ {i}}) - \operatorname * {P r} (\mathrm {N_ {j}} | \mathrm {N_ {i}})}{- \operatorname * {P r} (\mathrm {N_ {j}} | \mathrm {O_ {i}}) + \operatorname * {P r} (\mathrm {N_ {j}} | \mathrm {I_ {i}})} \\ \mathrm {b_ {i}} = \frac {1}{- \operatorname * {P r} (\mathrm {N_ {j}} | \mathrm {O_ {i}}) + \operatorname * {P r} (\mathrm {N_ {j}} | \mathrm {I_ {i}})} \\ \mathrm {c_ {i}} = \frac {- \operatorname * {P r} (\mathrm {N_ {j}} | \mathrm {O_ {i}})}{- \operatorname * {P r} (\mathrm {N_ {j}} | \mathrm {O_ {i}}) + \operatorname * {P r} (\mathrm {N_ {j}} | \mathrm {I_ {i}})} \end{array}
$$

If at $\mathbf{Q}_{\max}$ , $\Pr(\mathbf{N}_{\mathbf{i}}) = \mathbf{N}_{\mathbf{i},\max}$ then:

$$
\begin{array}{r l} & \Sigma \mathrm{Pr} (\mathrm{I} _ {\mathrm{i}} ^ {*}) \\ & = \Sigma (a _ {\mathrm{i}} N _ {\mathrm{i,max}} + b _ {\mathrm{i}} N _ {\mathrm{j,max}} + c _ {\mathrm{i}}) \\ & = \Sigma [ a _ {\mathrm{i}} N _ {\mathrm{i,min}} (1 + \sigma_ {\mathrm{i}} ^ {\theta}) + b _ {\mathrm{i}} N _ {\mathrm{j,min}} (1 + \sigma_ {\mathrm{i}} ^ {\theta}) + c _ {\mathrm{i}} ] \end{array}
$$

where $\Pr(I^{*})$ is the quality-maximizing $\Pr(I_{i})$ initiated by the $i^{th}$ group member.

With an explicit form for $\Sigma\Pr(I_{i}^{\theta})$ , the following proposition can be investigated:

Proposition (3.0). For the case of dyads, the probability of an idea initiation by members in a quality-maximizing group $(\Pr(I^{*}))$ will be maximized when the status of the two group members is equal (i.e., $\sigma_{i} = \sigma_{j} = .5$ ).

## Demonstration:

By definition, $\Sigma(\mathrm{Pr}(\mathbf{I}_{i}^{*}) = \mathrm{Pr}(\mathbf{I}_{i}^{*}) + \mathrm{Pr}(\mathbf{I}_{j}^{*})$ . Substituting the obtained expressions for $\mathrm{Pr}(\mathbf{I}_{j}^{*})$ and $\mathrm{Pr}(\mathbf{I}_{j}^{*})$ , and simplifying:

$$
\begin{array}{r l} \Sigma \mathrm{Pr} (\mathrm{I} _ {\mathrm{i}} ^ {*}) & = \frac {\mathrm{Pr} (\mathrm{N} _ {\mathrm{j}} | \mathrm{O} _ {\mathrm{i}}) (\sigma_ {\mathrm{i}} ^ {\theta} + \sigma_ {\mathrm{j}} ^ {\theta})}{- \mathrm{Pr} (\mathrm{N} _ {\mathrm{j}} | \mathrm{O} _ {\mathrm{i}}) + \mathrm{Pr} (\mathrm{N} _ {\mathrm{j}} | \mathrm{I} _ {\mathrm{i}})} \\ & = \frac {\mathrm{Pr} (\mathrm{N} _ {\mathrm{j}} | \mathrm{O} _ {\mathrm{i}}) (\sigma_ {\mathrm{i}} ^ {\theta} + (1 - \sigma_ {\mathrm{i}}) ^ {\theta})}{- \mathrm{Pr} (\mathrm{N} _ {\mathrm{j}} | \mathrm{O} _ {\mathrm{i}}) + \mathrm{Pr} (\mathrm{N} _ {\mathrm{j}} | \mathrm{I} _ {\mathrm{i}})} \end{array}
$$

The value of $\sigma_{i}$ at which $\Sigma\mathrm{Pr}(I_{i})$ is maximized can be obtained from the derivative of $\Sigma\mathrm{Pr}(I_{i}^{*})$ : Set:

$$
\frac {\partial}{\partial \sigma_ {i}} \left[ \sigma_ {i} ^ {\theta} + (1 - \sigma_ {i}) ^ {\theta} \right] = \theta \sigma_ {i} ^ {\theta - 1} - \theta (1 + \sigma_ {i}) ^ {\theta - 1} = 0
$$

then:

$$
\begin{array}{l} \sigma_ {\mathrm{i}} ^ {\theta - 1} = (1 - \sigma_ {\mathrm{i}}) ^ {\theta - 1} \\ \sigma_ {\mathrm{i}} = 1 - \sigma_ {\mathrm{i}}, \sigma_ {\mathrm{i}} = . 5 \end{array}
$$

Examining the second derivative for the critical point, $\sigma = .5$ :

$$
\begin{array}{l} \frac {\partial^ {2}}{\partial \sigma_ {i} ^ {2}} \left[ \sigma_ {i} ^ {\theta} + (1 - \sigma_ {i}) ^ {\theta} \right] | _ {\sigma_ {1} = . 5} \\ = \theta (\theta - 1) \sigma_ {i} ^ {\theta - 2} + \theta (\theta - 1) (1 - \sigma_ {i}) ^ {\theta} \\ = \theta (\theta - 1) \left(\frac {1}{2}\right) ^ {\theta - 1} <   0 \end{array}
$$

Since $0 < \theta < 1$ , this derivative will be negative, and $\sigma_{i} = .5$ maximizes $\Pr(I^{*})$ . Thus, the proposition is confirmed.

Conditions on the distribution of status under which the number of ideas will be maximized in a dyad may similarly be shown. I begin by assuming that total message volume $(V_{i})$ is an increasing, concave function of member status (i.e., $V_{i} = c_{2}\sigma_{i}^{\beta}, 0 \leq \beta \leq 1$ ). The quality-maximizing idea volume $(I_{\Sigma}^{*})$ in the dyad with $c_{2} = 1$ is:

$$
\begin{array}{r l} & \mathrm{I} _ {\Sigma} ^ {*} = \sigma_ {i} ^ {\beta} \operatorname * {P r} (I _ {i}) + \sigma_ {j} ^ {\beta} \operatorname * {P r} (I _ {j}) \\ & = \sigma_ {i} ^ {\beta} \left[ a _ {i} \operatorname * {P r} (N _ {i}) + b _ {i} \operatorname * {P r} (N _ {j}) + c _ {i} \right] \\ & \quad + \sigma_ {j} ^ {\beta} \left[ a _ {i} \operatorname * {P r} (N _ {j}) + b _ {i} \operatorname * {P r} (N _ {j}) + c _ {i} \right] \\ & = \sigma_ {i} ^ {\beta} \left[ a _ {i} N _ {\min} (1 + \sigma_ {j} ^ {\theta}) + b _ {i} N _ {\min} (1 + \sigma_ {i} ^ {\theta}) + c _ {i} \right] \\ & \quad + \sigma_ {j} ^ {\beta} \left[ a _ {i} N _ {\min} (1 + \sigma_ {i} ^ {\theta}) + b _ {i} N _ {\min} (1 + \sigma_ {j} ^ {\theta}) + c _ {i} \right] \\ & = N _ {\min} \left[ a _ {i} \sigma_ {i} ^ {\beta} (1 - \sigma_ {i}) ^ {\theta} + b _ {i} \sigma_ {i} ^ {\beta + \theta} + a _ {i} (1 - \sigma_ {i}) ^ {\beta} \sigma_ {i} ^ {\theta} + b _ {i} (1 - \sigma_ {i}) ^ {\beta + \theta} \right] \end{array} \tag {10}
$$

From (10), when $\sigma_{i}=.5$ , $\frac{\partial i_{y}}{\partial\sigma_{i}}=0$ . Examining $\frac{\partial^{2}i_{y}}{\partial\sigma_{i}^{2}}$ to establish the condition for the critical point, $\sigma_{i}=.5$ , to be a maximum, I obtain:

$$
\begin{array}{r l} \frac {\partial^ {2} I _ {\Sigma}}{\partial \sigma_ {i} ^ {2}} & = \left(\frac {1}{2}\right) ^ {\beta + \theta - 1} N _ {\min} [ a (\beta (\beta - 1) - 2 \beta \theta \\ & + \theta (\theta - 1) \} + b (\beta + \theta) (\beta + \theta - 1) ] \end{array}
$$

then,

$$
\frac {\partial^ {2} \mathrm{I} _ {\Sigma}}{\partial \sigma_ {\mathrm{i}} ^ {2}} <   0, \text { if } \beta + \theta <   \operatorname * {P r} \left(\mathrm{N} _ {\mathrm{j}} | \mathrm{O} _ {\mathrm{i}}\right) - \operatorname * {P r} \left(\mathrm{N} _ {\mathrm{j}} | \mathrm{N} _ {\mathrm{i}}\right) + 1.
$$

This condition requires $\beta_{i}$ and $\theta_{i}$ to be small, positive numbers. Since the probability of sending an idea or negative evaluation and message volume are most sensitive to status among lower status members, I consider this condition to be mild, and one that typically holds. I obtain an initial confirmation of this from an application of the data from the previously cited study. In this study, I find $\Pr(N_{j}|N_{i})$ to be .14, and $\Pr(N_{j}|O_{i})$ to be less than .01. Then, $\sigma_{i}=.5$ would be confirmed as the distribution that maximizes idea number, if $\beta+\theta<.87$ . From these data, I estimate $\beta=.221$ (in [24], I estimate $\beta=.114$ ). Similarly, the $\theta$ parameter is estimated to be .310 in the data I previously reported in this study, and .244 in [24] $^{5}$ . These estimates are consistent with the expectation that low status members are most sensitive to status and support a claim that the quality-maximizing number of ideas will occur when the statuses of members of a dyad are equal. Results for the case of dyads may be generalized to m-person groups when the condition on distributing negative evaluations to members according to member probabilities of idea initiation (the third term of the RHS of (9)) holds.

## 11. Studies of member status distributions and idea generation in interactive groups

In this section, three studies that provide support for the preceding exposition are reported. These studies all examine idea generation in interactive groups that have experimentally produced status hierarchies. Information exchange in all of the studies was computer-mediated, unless otherwise noted. Since the source of the subjects, task, and status differentiation procedures are the same across studies, I describe these first. Experimental procedures and results for each study will then be reported.

Subjects. Subjects in each of the studies were first-and second-year undergraduates at a private western university. Same-sex groups are used in each study since the sex of a group member in mixed-gender groups has been shown to have highly significant effects on participation. All subjects were randomly assigned to group memberships and experimental conditions.

Idea generation task. In these studies, the idea generation task is an adaptation of the “Winter Survival Exercise” [14] as the idea generation task. This exercise is one of a series in which groups must evaluate the usefulness of salvaged items for survival in a hostile environment. In our adaptation of this task to the study of idea generation, the group task is to generate as many survival related ideas for uses as possible for each of six salvaged survival items (e.g., six feet of rope, a newspaper, and a.45 calibre pistol).

Dependent variables: Number and uncommonness of ideas. The idea number score was the sum of uses given to all six items in the Winter Survival Exercise. An uncommonness score for each use given in a group is defined as the number of times the use was given for an item by all groups in all conditions of a study. Lower frequencies on this measure thus indicate more statistically original ideas. Cronbach coefficient alphas for the total number ( $\alpha = .943$ ) and mean uncommonness score across all items ( $\alpha = .812$ ) in twenty four-person groups indicate that these measures have acceptable reliability.

Independent variable: The group status distribution. An experimentally induced distribution of members on a task-relevant status attribute was the independent variable in these studies. Fictitious scores on an abbreviated version of the Desert Survival Exercise [14] were randomly assigned to members to define the status distribution in each group. This exercise required subjects to rank ten survival items according to their importance to survival. Members were informed of their own scores and the distribution of other scores in the group, but not the scores of specific individuals.

A status hierarchy in one condition and a near-equal status distribution in a second condition were defined from the fictitious scores returned to group members. In the SD condition, the distribution of test scores returned to members was: 2, 4, 5, 8, where 10 was the maximum possible score. In the SU condition, the score distribution was 4, 4, 5, 5. Instructions emphasized that good ideas come from all members and performance is best when all members participate. Thus, a member's score on the Desert Survival Exercise was explicitly made unequivalent to ability in idea generation. However, because of its relevance to the group task, it remains likely to be activated in the status organization of the group [23].

## 12. Effects of anonymity, experimenter-inserted negative evaluations of individual group members, and imputed status of the evaluator on idea generation

In view of the conceptual importance of negative evaluations in information exchange and the generally small number of this information type that members of non-expert interactive groups exchange (e.g., [24]), this study [25] used a procedure to experimentally insert negative evaluations of individual group members. As claimed in the preceding analysis, inserts of personal negative evaluations were expected to increase the perceived “risk” of idea initiations and decrease the number and proportions of ideas to other information types a group member initiates. This effect was expected to be less when members interact anonymously than when the sources of ideas and other messages were known [2].

In the study, effects of inserted negative evaluations were examined under two conditions on member anonymity (i.e., exchanges of messages which were not identified as to message source) and on the imputed status of the source of the evaluation inserts. In groups with inserts of negative evaluations of members, anonymity (anonymous vs. identified messages) was crossed with the status of the message source (high vs. low). Groups in the two control conditions did not receive the inserts of negative evaluations. Members of groups in one of the control conditions interacted anonymously, the source and target of messages exchanged by members of the group in the other control condition was identified.

Each group was composed of two male undergraduates and two “fictitious” members. The experimenter initiated all messages of “fictitious”

members according to a script ${}^{6}$ . All groups were status differentiated, with real subjects always of middle status (i.e., receiving scores of 5 and 6 in the 2, 5, 6, 9 score distribution). In half of the groups in the conditions with inserted negative evaluations, the experimenter inserted evaluations of the ideas of actual group members as the high status member. In the other half of these groups, the experimenter inserted negative evaluations as the low status member. Biographical information that members exchanged was consistent with the status scores (the high status member was reported to be a 22 year-old college senior; the low status member was reported to be a 17 year-old high school senior).

Inserted negative evaluations resulted in a highly significant decrease in the proportion of ideas in total messages given by a member ( $M_{no}$ inserts = .503, $M_{inserted negatives} = .100$ , $F(1,98) = 12.99$ , p < .001), but did not have significant effects on number.

Main effects of anonymity were to increase both the number and proportion of ideas in total messages. Differences in idea number attained statistical significance (idea number: $M_{anon} = 25.04$ , $M_{identif} = 19.93$ , $F(1,98) = 4.79$ , p < .05; proportion of ideas: $M_{anon} = .482$ , $M_{identif} = .430$ , $F(1,98) = 2.34$ , n.s.). Main effects of evaluator status on idea number and proportions were not significant for either idea number or proportions of ideas in total messages.

Results of the study provide support for the fundamental premise that increases in the probability of receiving a personal negative evaluation decreases the probability of a member initiating an idea. Effects of anonymity were in the predicted direction of increasing proportion and number of ideas exchanged, although these effects did not reach significance for proportion.

## 13. Effects of experimenter-inserted negative evaluations of the group on idea generation

Evidence on the contribution of negative evaluations to idea quality is provided in a second study of idea generation in a computer-mediated environment [27]. In this study, the negative evaluations that were inserted by the experimenter were of the group as a whole. When the group is the target of the evaluation, the threat to the status of individual members is low in comparison to a case where the member is the target of evaluation. I note the correspondence of this proposal to well-known arguments in collective action literatures on the diminution of personal responsibility in sharing benefits that are collectively owned (e.g., [20]). The diffusion of responsibility with respect to sharing social costs such as blame, in contrast, has received less emphasis in research on collective action. However, notions of the diffusion of blame have been extensively developed in early studies of “risky shift” phenomena (e.g., [31]) within group process traditions. I propose that status loss also represents a social cost, which is more diffuse when it is directed to the group.

In this study, evaluations were sent to all members of four-person groups in which the experimenter acted as the fifth member. The group negative evaluations were sent by the experimenter as a high or low status group member in different experimental conditions (HS, LS, respectively) and contrasted with a no-inserts (NI) condition. The results showed that inserts of negative evaluations significantly reduced the number of idea messages initiated $M_{\mathrm{NI}} = 76.1$ , $M_{HS} = 57.7$ , $M_{LS} = 58.8$ , $F(2,27) = 3.53$ , p < .05). However, the largest effect of the inserts were to significantly increase idea originality in groups $M_{\mathrm{NI}} = 18.28$ , $M_{LS} = 15.33$ , $M_{HS} = 14.69$ , $F(2,27) = 6.19$ , p < .01), even when the number of idea messages was a covariate in the analysis. (In these results, lower mean frequencies indicate higher ideational uncommonness.) Pairwise comparisons showed the mean idea uncommonness of groups in the HS condition to be significantly greater than the idea uncommonness of groups in both the LS and NI conditions (p < .05). The study suggests that when negative evaluations are not threatening to individuals (e.g., when they are directed to the entire group), their informational and motivational content can facilitate the group quality objective. In such cases, negative evaluations may increase member commitment to the group more than it increases their expected status loss from the evaluation.

## 14. Effects of status differentiation on face-to-face and computer-mediated group idea generation

Evidence on proposition (2.0) is reported in a third study in which idea generation of status differentiated and undifferentiated groups were directly contrasted in both face-to-face and computer-mediated environments [24]. Results of this study showed that status undifferentiated (su) ("equal status") groups initiated significantly more ideas and higher proportions of ideas in total messages than status differentiated (sd) groups. For face-to-face groups: idea number: $m_{su} = 110.92$ , $M_{sd} = 89.37$ , t(18) = 2.31, p < .05; Idea proportion: $M_{SU} = .440$ , $M_{SD} = .412$ , t(19) = 1.4, n.s.. For groups in a computer-mediated environment: Idea number: $M_{SU} = 92.76$ , $M_{SD} = 76.27$ , t(19) = 2.14, p < .05; Idea proportion: $M_{SU} = .669$ , $M_{SD} = .566$ , t(19) = 1.94, p < .05.

Table 1  
Summary of results: Experiments I to III

<table><tr><td rowspan="2">Experiment</td><td rowspan="2" colspan="2">Independent variables</td><td colspan="3">Dependent variables</td><td rowspan="2">Effect</td></tr><tr><td>Idea volume</td><td>Idea proportion</td><td>Idea uncommonness</td></tr><tr><td rowspan="2">I. Anonymous information exchange; inserted negative evaluations of individual group members.</td><td>ANON</td><td></td><td> $ANON > IDENT$ (p &lt; .05)</td><td>n.s.</td><td>n.a.</td><td rowspan="2">When risk is decreasing, the volume and proportion of idea messages are increasing.</td></tr><tr><td>NEG-IN</td><td></td><td>n.s.</td><td> $NEG-IN < CONTROL$ (p &lt; .001)</td><td>n.a.</td></tr><tr><td>II. Identified information exchange; inserted negative evaluations of the group.</td><td>NEG-GP</td><td></td><td> $NEG-GP < CONTROL$ (p &lt; 0.5)</td><td>n.a.</td><td> $NEG-GP > CONTROL$ (p &lt; .01)</td><td>Negative</td></tr><tr><td rowspan="2">III. Identified information exchange in status differentiated and undifferentiated groups; replicated in face-to-face and computer-mediated groups.</td><td rowspan="2">SU-SD</td><td>F-F</td><td> $SU > SD$ (p &lt; .05)</td><td>n.s.</td><td> $SU > SD$ (p &lt; .05)</td><td rowspan="2">Status undifferentiated conditions increase the volume of ideas and proportion of messages that are ideas.</td></tr><tr><td>C-M</td><td> $SU > SD$ (p &lt; .05)</td><td> $SU > SD$ (p &lt; .05)</td><td>n.s.</td></tr></table>

Key: ANON = Anonymous vs. identified communication.  
NEG-IN = Experimenter-inserted negative evaluation of individual members vs. control of no inserted negative evaluations.  
NEG-GP = Experimenter-inserted negative evaluations of the group vs. control of no inserted negative evaluations.  
SU-SD = Status undifferentiated vs. status differentiated conditions.  
F-F = SU-SD in face-to-face groups.  
C-M = SU-SD in computer-mediated groups.  
n.s. = not significant; n.a. = not assessed in experiment.

Results of the above studies are summarized in Table 1. These results generally support the exposition. More definitive tests of its predictions are now in order. In particular, assessment of the status-weighted negative evaluations a member is willing to accept as a function of his or her status would provide direct support for the form of the quality objective (eq. (9) and its constraints) that has been proposed. Additionally, the amounts and types of information initiated under conditions which encourage only member minimization of status loss in comparison to conditions which encourage member contribution to the group quality objective would directly test the form of the heuristic proposed above.

## 15. Summary and conclusions

In this work, I propose an account of the type and amount of information that members of decision making groups initiate. An analysis is developed that casts the member-agent as a decision maker and recognizes the influence of multiple motives on the heuristics that he or she adopts.

This exposition has sought to integrate and formalize previous conceptualizations of information exchange in group decision making. I have attempted to extend these conceptualizations to analyses in which quality is explicitly represented. In addressing the problem of “dual” or multiple motives of members, negative evaluations are conceptualized as a key organizer of information exchange. Using the individual decision heuristic and an expanded definition of the production of quality in decisions, a proposition on the status distribution that produces the maximized probability of an idea initiation in the information exchange of a quality-maximizing group is analytically supported. Early empirical support for major claims of the analyses is also reported.

From the analyses, it is suggested that increasing decision quality in groups will depend on maximizing the probability of an idea initiation, while keeping negative evaluations in a bounded interval. Too large a probability of negative evaluation will move the probability of an idea initiation from its maximum. Too small a probability will not yield the quality maximizing screening of ideas. Computer-mediated procedures have increasingly demonstrated effectiveness in managing group information exchange toward such normative ends (e.g., [19], [22]). These can include maintaining the exchange of information types at or near rates which analytical and empirical research indicate to be quality maximizing.

Interactive groups as decision making units have a long, rich history of conceptual and empirical study, in which qualitative accounts of process predominate. It is timely to begin to organize these qualitative accounts of group decision processes in frameworks that also allow analytical inference and empirical testing.

## 16. For further reading

[6], [8], [9], [11], [12], [13], [16], [21], and [30].

## References

[1] P.R. Christensen, J.P. Gulford and R.D. Wilson, Relationships of Creative Responses to Working Time and Instructions, Journal of Experimental Psychology, 53, (1957) 82–88.

[2] T. Connolly, L.M. Jessup and J.S. Valacich, Effects of Anonymity and Evaluative Tone on Idea Generation in Computer-Mediated Groups, 36, (1990) 689–703.

[3] B.P. Cohen and S.D. Silver, Introduction to a Theory of Group Structure and Information Exchange, in: J. Berger and M. Zelditch, Eds., Sociological Theories in Progress, Vol. 3, Newberry Park, California, (1989).

[4] K.S. Cook, and R.M. Emerson, with M.R. Gillmore and T. Yamagishi, The Structure of Social Exchange, Academic Press, New York, (1980).

[5] J.H. Davis, P.R. Laughlin and S.S. Komorita, The Social Psychology of Small Groups: Cooperative and Mixed-Motive Interaction, in: M. Rosenzweig and L.W. Porter Eds., Annual Review of Psychology, 36, (1976) 501–540.

[6] R.M. Dawes, A.J.C. Van de Kragt and J.M. Orbell, Not Me or Thee but We: The Importance of Group Identity in Eliciting Cooperation in Dilemma Situations: Experimental Manipulations, Acta Psychologia, 68 (1986) 83–97.

[7] R. Emerson, Social Exchange Theory, in: M. Rosenberg and R. Turner, Eds., Social Psychology, Basic Books, New York, (1981).

[8] J R. Hackman and C.C. Morris, Group Tasks, Group Interaction Process, and Group Performance Effectiveness: A Review and Proposed Integration, in: L. Berkowitz, Ed., Group Processes, Vol. 8, Academic Press, New York, (1975).

[9] D.M. Herold, Improving Performance Effectiveness of Groups Through a Task-Contingent Selection of Intervention Strategies, Academy of Management Review, 3, (1978) 315–325.

[10] R.M. Hogarth, Judgment and Choice: The Psychology of Decision, 2 $^{nd}$ edition, Wiley, New York, (1987).

[11] M. Intrilligator, Econometric Models, Techniques, and Applications, Prentice-Hall, Englewood Cliffs, New Jersey, (1978).

[12] I. Janis, Groupthink, 2 $^{nd}$ edition, Houghton-Mifflin, Boston, (1982).

[13] L.M. Jessup and D.A. Tansik, Decision Making in an Automated Environment: The Effects of Anonymity and Proximity with a Group Decision Support System, Decision Sciences, 22, (1991) 266–279.

[14] D.W. Johnson and F.P. Johnson, Joining Together, 3 $^{rd}$ edition, Prentice-Hall, Englewood Cliffs, New Jersey, (1987).

[15] D. Kahneman, P. Slovic and A. Tversky, Eds., Judgment Under Uncertainty: Heuristics and Biases, Cambridge University Press, Cambridge, England, (1982).

[16] H.H. Kelley and J.M. Thibaut, Group Problem Solving, in: G. Lindzey and E. Aronson, Eds., Handbook of Social Psychology, Addison-Wesley, Reading, Massachusetts, (1969).

[17] J.M. Levine and R.L. Moreland, Small Group Research, in: M. Rosenzweig and L. Porter, Eds., Annual Review of Psychology, 41, (1990) 585–634.

[18] H. Mintzberg, D. Raisinghani and A. Theoret, The Structure of Unstructured Decisions, Administrative Science Quarterly, 21, (1976) 246–275.

[19] J.F. Nunamaker, A.R. Dennis, J.S. Valacich and D.R. Vogel, Information Technology for Negotiating Groups: Generating Options for Mutual Gain, Management Science, 37, (1991) 1324–1346.

[20] M. Olson, The Logic of Collective Action (revised edition), Harvard University Press, Cambridge, Massachusetts, (1971).

[21] J.M. Orbell, A.J.C. Van De Kragt and R.M. Dawes, Explaining Discussion-Induced Cooperation, Journal of Personality and Social Psychology, 54, (1988) 811–819.

[22] M.S. Poole, M. Holmes, M. and G. DeSanctis, Conflict

Management in a Computer Supported Meeting Environment, Management Science, 37, (1991) 926–953.

[23] C. Ridgeway, Dominance, Performance, and Status in Groups, in: E.J. Lawler, Ed., Advances in Group Processes, Vol. 1, JAI Press, Greenwich, Connecticut, (1984).

[24] S.D. Silver, B.P. Cohen and J. Crutchfield, Status Differentiation and Information Exchange in Face-to-Face and Computer-Mediated Idea Generation, Social Psychology Quarterly, 57, (1994) 108–123.

[25] S.D. Silver, B.P. Cohen and J. Crutchfield, Effects of Experimenter Inserted Group Negative Evaluations on Idea Generation and Information Exchange in Computer-Mediated Groups, Manuscript under revision (1993).

[26] S.D. Silver, B.P. Cohen and J. Rainwater, Group Structure and Information Exchange in Innovative Problem Solving, in: E.J. Lawler and B. Markovsky, Eds., Advances in Group Processes, Vol. 5, JAI Press, Greenwich, Connecticut, (1988).

[27] S.D. Silver and L. Troyer, Unpublished data, 1993.

[28] H.A. Simon, The New Science of Management Decision, New York University Press, New York, (1960).

[29] G.F. Smith, Towards a Theory of Managerial Problem Solving, Decision Support Systems, 8, (1992) 29–40.

[30] R.N. Taylor, Nature of Problem Ill-Structuredness: Implications for Problem Formulation and Solution, Decision Sciences, 5, (1974) 632–643.

[31] M.A. Wallach, N. Kogan and D.J. Bem, Group Influence on Individual Risk-Taking, Journal of Abnormal and Social Psychology, 65, (1962), 75–86.

[32] A. Zander, Making Groups Effective, Jossey-Bass, San Francisco, (1982).

![](/api/attachments/UF4QZE45/fulltext/images/866b15694de6720aadc05228b7b4cc353d1ab4a4e99c3a3d77f6e022b5e5e121.jpg)  
Steven D. Silver (Ph.D., University of California, Berkeley) is currently investigating social processes that mediate the exchange of information in groups and organizations. His work has appeared in journals, book chapters and conference proceedings in social psychology and organizational and consumer behavior.
