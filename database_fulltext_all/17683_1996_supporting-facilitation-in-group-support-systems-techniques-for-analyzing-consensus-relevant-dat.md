---
otero_id: 17683
otero_key: "T7324KGB"
title: "Supporting facilitation in group support systems: Techniques for analyzing consensus relevant data"
authors: "Ojelanki K. Ngwenyama; Noel Bryson; Ayodele Mobolurin"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00004-6"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Supporting facilitation in group support systems: Techniques for analyzing consensus relevant data

Ojelanki K. Ngwenyama $^{a,*}$ , Noel Bryson $^{b}$ , Ayodele Mobolurin $^{b}$

$^{a}$ School of Business Administration, University of Michigan, Ann Arbor, MI, USA $^{b}$ School of Business Administration, Howard University, Washington, DC, USA

## Abstract

In this paper, we present a set of techniques and an approach to support the facilitator in building consensus during group decision making in computer supported group work. The approach utilizes data about each participant's expressed preferences (scores and ranks) for a set of decision alternatives under consideration. The data are analyzed to provide the facilitator with information about the level of group consensus, coalescing of subgroups, and areas of strong disagreement. An illustration from a real-world case situation demonstrates the approach.

Keywords: Group decision making; Consensus building; Group support systems; Group decision support systems

## 1. Introduction

In response to the turbulence of the post-industrial environment, many firms are shifting away from hierarchical models for organizing work to autonomous teams and other forms of self-managing group processes $[16,2]$ . The urgency, complexity, and frequency of problems confronting organizations necessitate the participation of groups of individuals who have a wide range of skills, perspectives, and values $[16]$ . This trend towards group work has given rise to the research and development of a class of computer-based environments to support group work commonly referred to as group support systems (GSS). GSSs vary in their support for group work; some types are general purpose while others target specific group activities. Examples of specialized GSSs are group decision support systems (GDSS) [7], negotiation support systems (NSS) [18,19], and electronic meeting systems (EMS) [5]. In general, GSS environments provide tools and techniques to assist in facilitating and managing group discussions, issue exploration, problem definition and analysis, consensus seeking, group writing, activity coordination, knowledge sharing and accumulation, and data and decision analysis.

Much of the GSS research has focused on developing computer environments and studying their effects on group work $[23]$ . To date, several studies have reported contradictory findings on the effectiveness of GSS in group activity. For example, some studies reported reduction in meeting lengths $[14,25]$ while others have reported no change or increased meeting lengths $[27]$ . Even though the focus of research has been on improving group processes via GSS, relatively little attention has been given to support for group facilitation $[14,2,33,8]$ . However, recent experimental and field studies suggest that facilitation may be a critical factor in GSS effectiveness $[6,24,33]$ . The primary focus of this paper is to present a set of techniques and an approach for analyzing preference data which could assist group facilitation and the search for consensus in computer supported group work. These techniques are intended to assist facilitators with the difficult task of clarifying positions of participants and identifying openings for dialogue, and developing strategies for moving the participants to consensus. Our approach is informed by a broad range of decision analysis techniques, for example AHP $[29]$ , fuzzy systems $[10]$ and multiple criteria decision making $[4]$ among others. The techniques are intended to support the group facilitator in analyzing and determining, at any point in time: (a) the level of consensus existing in the group process; (b) subgroups with strong internal agreement which could serve as catalysts for consensus building; and (c) those decision options which may be controversial.

## 2. Facilitation support in GSS

The importance of facilitation and consensus formation in group process effectiveness has long been acknowledged in the organization studies literature [15]. However, research on facilitation in GSS is only now coming into focus. And although recent experimental and field studies suggest that it may be critical to GSS effectiveness [6,14,24,33], studies on how facilitation should be structured in GSS use have been inconclusive. For example, in a comparative study, Dickson et al. [8] found that the group facilitated by computer software (chauffeured support) achieved a higher level of satisfaction and consensus than a human facilitated group or user-driven group. On the other hand, Anson [1] found that flexible human facilitation of groups, whether using GSSs or not, improves the group process. Two obvious questions that emerge from these discussions are: What are the relevant aspects of good facilitation? How can they be supported in GSS environments?

Several researchers have discussed the role of the facilitator in manual group processes $[9,15,28]$ . More recently, Phillips et al. $[26]$ and Bostrom et al. $[2]$ have discussed the role of the facilitator in computer supported group processes. Although there are some differences among these researchers, the following three phase general model for facilitator involvement in group meetings can be derived from them: (1) process planning and design; (2) preparation and setup; and (3) process management. In the first phase, the facilitator works with the group leader and other members to design the group process. These design activities are concerned with: (a) defining the ground rules for the process and the roles of the participants; (b) formulating the problems and defining the outcomes to be achieved; and (c) developing an agenda. In the second phase, the facilitator selects the appropriate group technology and prepares for the group process. The third phase encompasses the most demanding activities of facilitation. It is concerned with the management of the group process and promotion of effective task behaviors. In addition to running the meeting according to the agreed upon ground rules, the facilitator must keep the participants focused on the agenda, and maintain productive dialogue and intra-group relations. In flexible facilitation processes, the facilitator is required to skillfully and unobtrusively steer the group toward the desired outcomes. To be effective in this undertaking, the facilitator must be able to analyze and understand the positions of participants, identify openings for dialogue, and develop strategies for moving the participants toward consensus and commitment. In the context of GSS environments, this requires not only a high level of training for facilitators $[15]$ , but appropriate methods, techniques, and software tools $[18]$ .

## 2.1. Current approaches

Current approaches to facilitation and consensus building in GSS are limited to tool support for ranking and scoring. Most GSS procedures for ranking and scoring: (a) collect individual

![](/api/attachments/T7324KGB/fulltext/images/f9600c1dca4b90af0be5c25745c12c5baa1ea5be758d356bd30afbb3f2a4dee2.jpg)  
Fig. 1. Conceptual framework.

preference data about the decision alternatives; (b) derive a group preference from the individual preferences; and (c) discuss the derived group preference and repeat the cycle until an acceptable outcome is achieved. Although sophisticated analysis of these preference data could offer insights into consensus formation, very limited analysis is performed on them. One reason for this is the limitations of current data collection and analysis techniques in GSSs. Simple techniques are used to collect the individual preferences, and simple statistical techniques are used to derive the group preference. In the case of ranking, each user is presented with a list of the relevant objects and is instructed to order them in a manner that is consistent with his/her beliefs. The GSS (e.g. GroupSystems, TeamFocus, VisionQuest) provides convenient mechanisms for moving the objects to the desired positions $^{1}$ . The case of scoring/rating in GSS is no different; each participant is presented with the list of alternatives, a numeric interval of acceptable scores, and a pair of qualitative categories associated with the highest and lowest values of the scale. Each participant is requested to assign to each object an integer value consistent with his/her belief about the relative position of the object. With this approach to scoring, it is possible that two different users may associate two different meanings to the same numeric value. Similarly, a user may associate the same meaning to two different values in the interval. This implies that evaluating the responses of the group in order to determine the consensus response, as well as the level of consensus, is a problematic undertaking.

Further, since scoring/rating with reference to a common basis of comparison also implies the existence of relationships between the objects relative to the basis of comparison, different scores provided by two different group members could reflect expressions of the same relationships. For example, the actual scores (12, 6, 3) and (8, 4, 2) imply the same relationships (4: 2: 1). Consequently, it is necessary to consider the relationships among the scores in order to determine the level of consensus. This perspective on consensus might not be apparent to the user if there is no explicit association between the scores of pairs of objects. Current approaches to scoring in GSS limit the users' perspectives on consensus and the methods used to estimate the level of consensus. One GSS, OptionFinder, does provide a “consensus map” of decision makers' positions; however, it uses arithmetic averaging and as such is subject to the problem discussed above. In general, current GSSs provide the facilitator with limited tools and techniques for identifying and analyzing embedded data that could help in the search for consensus. In the following section, we outline the basic concepts of the proposed techniques and approach.

## 3. The conceptual framework

Conceptually, our approach for supporting the analysis of consensus relevant data in GSS can be divided into a three phase process (Fig. 1): (1) pre-evaluation, (2) preference elicitation, and (3) data analysis and reporting. The pre-evaluation phase encompasses three basic activities: (1) selecting the alternatives for evaluation; (2) determining the evaluation criteria; and (3) determining the threshold of agreement. The first two activities are common to any group decision making process, and are well discussed in the literature (see Irving and Conrath [17] for a summary). They are also well supported by current GSS platforms (see Dennis et al. [5] and Vogel et al. [32]). The third activity is essentially concerned with defining the stopping rules for the process. In practice, the group discusses the decision situation at hand and defines a point, which when attained, lead all to agree that consensus has been reached. This point could be the expiration of an allotted time interval, or a certain level of agreement (partial or full) on the issues. The preference elicitation phase is concerned with ranking the alternatives and providing comparison data. These are common activities in group decision making, generally supported by most GSS environments. Data analysis and reporting, the third phase of the process, is the central focus of this paper. Here we are concerned with analyzing the preference data elicited from the decision makers to identify their positions on the “consensus map.” We are interested in identifying possible coalitions, problematic decision alternatives, and individuals whose preferences may serve as a position around which consensus could be negotiated.

The analysis that we are proposing provides a means to assess the level of group consensus at any point in the group process, and provide information which could then be used by a facilitator to assist in negotiating consensus formation in the group. Ideally, consensus would be reached when a consensus map has been identified that represents a preference that the group finds to be acceptable. From our perspective, such a map would evolve from communicative and discursive activity within the group. The question arises as to the point at which the group can be said to have an acceptable level of consensus. In the ideal situation, there would be total agreement in the group. But in general, due to differences of opinion, this would not be the case. Thus, there is a need for a stopping rule.

## 3.1. Basic concepts

For preference elicitation, we use a scale and a corresponding matrix $A^{t}=\{a_{ij}^{t}\}$ within which individual decision-makers $\{t\}$ could specify their cardinal preferences (i.e. their priority order and relative strengths) with regard to a set of “n” decision options. This type of technique is extremely easy to implement and use in GSSs, and requires little effort on the part of the decision makers [12,13,29]. For the data analysis, we use numeric weight vectors. The use of weight vectors to represent the relative strengths of individual and group preferences with regard to a set of objects is not a new idea, but there are different opinions on the matter. A fundamental premise of ours is that weight vectors can reflect the decision-making group’s (DMG) beliefs in the relative importance of the various objects (see Bryson et al. [3]). Several researchers including Cook and Stewart [4], and Shanteau [31] concur on this point. Further, Cook and Stewart [4], Keeney and Raiffa [20], and others have demonstrated the applicability of weight vectors for multiple criteria decision-making (MCDM) analysis; consequently, we will not repeat those arguments here.

We apply various analysis techniques (discussed below) to the numeric vectors in order to derive the following consensus indicators: (1) the group strong agreement quotient (GSAQ), a measure of the level of agreement in the group; (2) the group strong disagreement quotient (GSDQ), a measure of the level of disagreement in the group; and (3) the group strongest disagreement indicator (GSDI), a measure of the breadth of opinions in the group. The individual strong agreement quotient (ISAQ'), the individual strong disagreement quotient (ISDQ'), the individual strongest disagreement indicator (ISDI $^{t}$ ), and analogous indicators measure the position of each individual relative to the group.

## 3.2. Data analysis

The data analysis consists of three sets of activities: (1) deriving the weight vectors from the preference data collected from the decision makers; (2) deriving the indicator values; and (3) analyzing the indicator values and weight vectors to identify sub-groupings and problematic decision options.

## 3.2.1. Deriving weight vectors

Let $a_{ij}^{t}$ be the numerical comparison of the decision-maker t, of his/her relative preference between the pair of decision options $(i,j)$ . This information can be represented for each pair of available decision options as a matrix $A^{t} = \{a_{ij}^{t}\}$ . If we assume that the preference information is consistent, then it follows that the paired comparison coefficient $a_{ij}^{t}$ is close to the real underlying preference ratio $y_{i}/y_{j}$ of the decision-maker. Let $w^{t} = (w_{1}^{t},\dots,w_{n}^{t})$ be the normalized weight vector that provides a numeric representation of the group member t's belief on the relative importance of all the available n decision options. Then, it follows that the ratio $w_{i}/w_{j}$ is close to the decision-maker's underlying preference ratio and is an approximation of comparison coefficient $a_{ij}^{t}$ (see Saaty [30]). To obtain the normalized weight vector $w^{t}$ , we solve the following eigenvalue problem:

$$
A ^ {t} * w ^ {t} = \mathrm{e} _ {\text { MAX }} ^ {t} * w ^ {t},
$$

where $e_{MAX}^{t}$ is the largest eigenvalue associated with $A^{t}$ , such that $\Sigma_{j}w_{j}^{t}=1$ and $w_{j}^{t}\geq0$ . We compute a consistency ratio to determine the degree of inconsistency in the preference information given by the decision-maker. If this computed ratio is higher than a specified consistency ratio, then the degree of inconsistency is unacceptable. It is recommended that the decision-maker revise his/her relative preference information, after which the weights are recomputed.

## 3.2.2. Deriving indicator values

The indicators described above provide an estimate of the level of consensus existing within the group at a given point in time. The first two indicators, GSAQ and GSDQ, identify the percentage of pairs of group members who have a reasonably strong level of agreement or disagreement. The idea is that consensus develops from pairs of group members involved in dyadic discourse. Consequently, we are attempting to measure the agreement in the opinions of each pair of group members. The GSAQ indicator is based on the strong agreement in dyadic discourse. Alternately, we may measure the current level of consensus indirectly by using the GSDQ indicator to assess the level of strong disagreement among the participants. Further, the GSDI value provides an estimate of the breadth of opinions in the group. The individual indicators ISAQ, ISDQ, and ISDI give an estimate of the position of each individual relative to the group.

Using these indicators, the group process facilitator can assess the progress towards consensus formation from several perspectives and plan strategies for achieving movement toward group consensus during difficult periods. As stated earlier, the facilitator's interest in the analysis is to answer the following questions: (1) Is there a subset of members whose current position with regard to the given decision-making problem makes them likely to be effective agents for consensus-building based on dyadic discourse? (2) Is there a group member who shares strong agreement with an “overwhelming majority” of the group members? (3) Is there a subset of the objects such that, if this subset were removed, the agreement quotient between a given pair of group members would be increased, and the group's consensus index would be increased?

## 3.2.3. Identifying subgroups

With regard to the first question, the indicators ISAQ $^{t}$ and ISDQ $^{t}$ could be used in identifying individuals who share a fair level of agreement with other group members and who would not have any apparent insurmountable barriers identified by the ISDI $^{t1}$ value. We can identify these group members via their individual consensus vector (ICV $^{t}$ ) as:

$$
\mathrm{ICV} ^ {t} = \left(\mathrm{ISAQ} ^ {t}, - \mathrm{ISDQ} ^ {t}, - \mathrm{ISDI} ^ {t}\right).
$$

Those persons whose ICV's fit this description would not have their ICV dominated by the ICV of any other group member. Here, $ICV^{t1}$ is said to be dominated by $ICV^{t2}$ , if $ICV^{t1} \leq ICV^{t2}$ with strict inequality in at least one dimension. Likewise, we can identify any group members “t” and “r” who share strong agreement by using two methods: (1) finding the cosine of the angle between their corresponding weight vectors $w^{t}$ and $w^{r}$ ; and (2) finding the ratio of these same weight vectors. In the case of the cosine method, we define this agreement indicator as:

$$
\mathrm{AGG} ^ {t, r} = \left(w ^ {t *} w ^ {r}\right) / \left(\| w ^ {t} \| ^ {*} \| w ^ {r} \|\right),
$$

where $(w^{t} * w^{r})$ is the dot product of the two vectors, and $\|w^{t}\|$ , $\|w^{r}\|$ are the 2-norms of $w^{t}$ , $w^{r}$ respectively.

Note that $AGG^{t,r}$ can only take on values between 0 and 1. If $w^{t}$ and $w^{r}$ are fairly similar, then $AGG^{t,r}$ will be fairly close to 1. If the two vectors are very dissimilar (i.e. almost orthogonal), then $AGG^{t,r}$ will be close to zero. If we specify threshold values $\alpha$ (for strong agreement) and $\delta$ (for strong disagreement), then group members “t” and “r” will be said to have strong agreement if $AGG^{t,r} \geq \alpha$ , and strong disagreement if $AGG^{t,r} \leq \delta$ . A possible value for $\alpha$ is 0.985 (the cosine of a $10^{\circ}$ angle), and a possible value for $\delta$ is 0.966 (the cosine of a $15^{\circ}$ angle). The rationale for using these angles is that the largest possible angle between any two of our weight vectors is $90^{\circ}$ . Further, $10^{\circ}$ on a $0^{\circ}$ to $90^{\circ}$ scale is equivalent to 1 on a 1 to 9 scale, and similarly $15^{\circ}$ is equivalent to 1.5 on a 1 to 9 scale.

The GSAQ value may thus be computed as follows:

$$
\mathrm{GSAQ} v = \Sigma_ {(t \in T)} \Sigma_ {t <   r} 2 ^ {*} \Gamma (t, r) / (m ^ {*} (m - 1))
$$

where $\Gamma(t,r)=1$ if $AGG^{t,r}\geq\alpha$ , and $\Gamma(t,r)=0$ if $AGG^{t,r}<\alpha$ , “T” is the index set for the group members, and “m” is the number of members in the group.

Similarly, the group strong disagreement quotient (GSDQ) is computed as follows:

$$
\mathrm{GSDQ} = \Sigma_ {(t \in T)} \Sigma_ {t <   r} 2 ^ {*} \Phi (t, r) / (n ^ {*} (n - 1))
$$

where $\Phi(t,r) = 1$ if $\mathrm{AGG}^{t,r} \leq \delta$ , and $\Phi(t,r) = 0$ if $\mathrm{AGG}^{t,r} > \delta$ .

The third indicator may be computed as follows:

$$
\mathrm{GSDI} = \min \left\{\mathrm{AGG} ^ {t, r}, \text { over   each   pair } \right\} t, r.
$$

Thus, the consensus indicators of the group are said to be GSAQ at the $\alpha$ -level of significance, GSDQ at the $\delta$ -level of significance, and GSDI. An examination of values of these three indicators should offer some insight into the current level of consensus in the group.

The individual consensus indicators may be computed as follows:

$$
\begin{array}{l} \mathrm{ISAQ} ^ {t} = \Sigma_ {(r \in T, r \neq t)} \Gamma (t, r) / (n - 1); \\ \mathrm{ISDQ} ^ {t} = \Sigma_ {(r \in T, r \neq t)} \Phi (t, r) / (n - 1); \text { and } \\ \mathrm{ISDI} ^ {t} = \min \{\mathrm{AGG} _ {t, r}, \text { over   each } r \text { in } T \}. \end{array}
$$

## 3.2.4. Identifying problematic options

Finally, in order to identify that subset of decision options which when removed would positively influence the level of consensus between two group members, we suggest the following analysis technique: Let $J = \{1, 2, j', (j' + 1), ..., m\}$ be the index set of the m decision options involved in the problem situation, and let $J' = \{(j' + 1), ..., m\}$ be the index set for those decision options whose removal would increase the value of the agreement indicator between a given pair of members (say t, r). Given the weight vectors $w^{t}, w^{r}$ where:

$$
\begin{array}{l} w ^ {t} = \left(w _ {1} ^ {t},..., w _ {(j ^ {\prime} - 1)} ^ {t}, w _ {j} ^ {t t}, w _ {(j ^ {\prime} + 1)} ^ {t},..., w _ {m} ^ {t}\right), \text {and} \\ w ^ {r} = \left(w _ {1} ^ {r},..., w _ {(j ^ {\prime} - 1)} ^ {r}, w _ {j ^ {\prime}} ^ {r}, w _ {(j ^ {\prime} + 1)} ^ {r},..., w _ {m} ^ {r}\right), \end{array}
$$

we can construct the vectors $v^t, v^r$ as follows:

$$
\begin{array}{l} v ^ {t} = \left(v _ {1} ^ {t},..., v _ {(j ^ {\prime} - 1)} ^ {t}, v _ {j ^ {\prime}} ^ {t}\right), \text {and} \\ v ^ {r} = \left(v _ {1} ^ {r},..., v _ {(j ^ {\prime} - 1)} ^ {r}, v _ {j ^ {\prime}} ^ {r}\right), \\ \text {where} v _ {j} ^ {t} = w _ {j} ^ {t} / \| w ^ {t ^ {\prime}} \|, v _ {j} ^ {r} = w _ {j} ^ {r} / \| w ^ {r ^ {\prime}} \|, \\ w ^ {t} = \left(w _ {1} ^ {t},..., w _ {(j ^ {\prime} - 1)} ^ {t}, w _ {j ^ {\prime}} ^ {t}\right), \text {and} \\ w ^ {r} = \left(w _ {1} ^ {r},..., w _ {(j ^ {\prime} - 1)} ^ {r}, w _ {j ^ {\prime}} ^ {r}\right). \end{array}
$$

The agreement indicator between the two group members, if the given subset of objects were removed from the problem, is the cosine of the angle between the vectors $v^{t}$ and $v^{r}$ .

## 4. Prototype and case illustration

The consensus support prototype, an application within the Group Work Environment (GWE) discussed here, was developed using Visual Basic and runs under Microsoft Windows $^{®}$ ; other implementations are in various stages of completion $^{2}$ . The functional architecture of the application can be decomposed into four modules illustrated in Fig. 2: (1) Process Management (PM), (2) Preference Elicitation (PE), (3) Consensus Analysis (CA), and (4) Reporting. The process management module offers the facilitator a set of tools for managing the group process. It is also the primary interface to the system through which the facilitator controls execution of the other modules.

The preference elicitation module is the primary interface for decision makers. It provides a set of user-friendly interfaces through which decision makers rank alternatives and enter comparison data (see Fig. 4). The consensus analysis module calculates all the various indicators described above. After each round of preference elicitation, the facilitator, interacting via the PM module, runs the CA module to assess group consensus. The facilitator also manages the report generation and distribution process via the PM module. During report setup the facilitator defines the distribution list and the information to be displayed on each decision maker's workstation.

## 4.1. General operating procedure

All users of the GWE application gain access via the login procedure. The login identification and password determine the level of access the individual is given. The facilitator is granted access to the Process Management Module, where he/she can setup and manage the group process.

![](/api/attachments/T7324KGB/fulltext/images/b82c39696851b902003a3032ed2625a9bd6f3fb6aedde4bba0a31eef4231acca.jpg)  
Fig. 2. System application architecture.

All other users are given access to the preference elicitation interface. The general operating procedure for using the GWE application in group processes is characterized by three phases: Setup, Preference Elicitation, and Data Analysis and Reporting. Depending on the outcome of the group process, Phases II and III, Preference Elicitation and Data Analysis and Reporting, may be cycled through as many times as necessary. In Phase I, Setup, the group of decision makers discuss and select the decision alternatives to be considered, determine the evaluation criteria, define the ground rules for the group process, and set the level of agreement (stopping rule) to be accepted as group consensus. In some cases, the group members may opt for an open process, in other cases an anonymous process. With the rules of procedure, the decision options, and stopping rule clearly defined we setup the system for the nomination meeting. The facilitator, interacting with the Process Management Module (see Fig. 3) runs the setup procedure which requests data on the number of decision options and number of decision makers involved in this process. This data is used by the process management module to create the work files. Next, the facilitator is required to enter the decision options (via a data entry screen, not shown). This data is loaded into the input file of the preference elicitation module. The facilitator, then, defines the reports to be generated at the end of Phase III. In Phase II, each decision maker ranks the alternatives via the Preference/Rank Evaluation interface (Fig. 4). The PE module executes a selection cycle which presents two decision options at a time for the decision maker to evaluate. The decision maker provides information on the weights (relative strengths) of his/her preferences. The process is repeated through several iterations until all combinations of the decision options are evaluated.

![](/api/attachments/T7324KGB/fulltext/images/9e9123f2672b383e46d5678a0ffac94c8f1803a9a56e1feba531d45577039c39.jpg)  
Fig. 3. The facilitator's interface

![](/api/attachments/T7324KGB/fulltext/images/e391834bd461a4217700eed0b2cbe0867d8e0ecd6684abd5562e6365e822681f.jpg)  
Fig. 4. Preference elicitation interface.

In Phase III, the facilitator runs the CA module which computes the weight vectors and the ISAQt and GSAQ values. She/he, then, runs the reporting module which presents the appropriate ISAQ results and the GSAQ measure to each participant $^{3}$ . If the GSAQ does not meet the expected threshold of agreement, the facilitator can use the system to conduct relevant analysis and determine a solution strategy. He/she can examine the individual indicators of the group members to identify the individual with the largest ISAQ value. That is, $ISAQ^{t} > p_{1}$ where p is the proportion of the group that agrees with the individual. Since this would imply that there is some convergence by several other group members toward the weights provided by this individual, they can be used as a starting point for further discussion. A second option is to select a pair of participants whose individual strong agreement quotients surpasses the threshold ( $ISAQ^{t} > p_{2}$ , $ISAQ^{r} > p_{2}$ ), and combined strong agreement quotient surpasses it as well. Then, compute a corresponding weight vector ( $w^{t,r}$ ) for them and use it as the starting point for further discussion. A third option is to identify those alternatives upon which there is strong disagreement in the group and use them as a starting point for further discussion. At any point in the process, the facilitator can repeat the preference elicitation process and re-assess the level of consensus of the group.

## 4.2. A case illustration

The case presented here is a recent decision making situation in which a committee of twelve senior faculty members of a major American business school were required to evaluate a set of five applicants, and nominate one candidate and an alternate for the position of dean $^{4}$ . We use the case to illustrate how the ideas and techniques presented earlier were implemented in a typical group decision making situation. This case study served as a “live test” of the facilitator support system and operating procedure. It must be noted that this test was not planned in advance; it was serendipitous. We were planning to develop an experiment using MBA student subjects when an influential member on the committee suggested that we test our system on a “real problem” — the dean’s nomination process. After some discussion of the matter, the offer was accepted with some trepidation. Since the committee had already agreed upon a process for their deliberations, our procedures had to be adapted to fit their needs. The nomination project was structured as a three stage process: (I) evaluating the applicants and deriving the short-list; (II) conducting interviews of the short-listed candidates; and (III) ranking short-listed candidates and nominating the primary and alternate candidates to the university president. Although only one of the authors was allowed to observe Stage I, none were involved in Stage II. In Stage III, a facilitator and an observer participated in the trial. The GSS support was provided only for Stage III of the process. In the following section, we describe Stages I and III.

Stage I: The first stage of the nomination process consisted of two committee meetings held over a four-week period. During the first meeting, the committee debated and hammered out the criteria for the first round elimination process. The basic objective of the first round elimination process was to derive a short-list of contenders for site visits and further consideration. During the intervening period until the second meeting, each committee member was required to review the files of all the candidates in light of the criteria. Three weeks later, the second meeting was held to conduct the first round elimination process. Although the elimination process was well structured, the committee used neither a facilitator nor the system. The result of the preliminary round was a short-list of five candidates who met the basic qualifications for the position.

Stage III: After the interviewing stage was completed, the committee held two meetings to discuss the ranking criteria and procedure. A third meeting convened in order to conduct the nomination process, and a fourth to wrap-up the project. During the first of these meetings, the group of decision makers were oriented on the procedure to be followed, and the role of the facilitator in supporting the group decision making process. The decision makers were also given an action learning hand's on workshop which consisted of a "toy problem" — ranking NCAA basketball players. After their orientation the committee members commenced discussion of possible evaluation criteria. This discussion continued during a second meeting, where agreement was achieved on the evaluation criteria and the level of agreement required to carry the vote. It was agreed that a two-thirds majority vote on the first and alternate candidate would constitute a consensus decision. A date was set for the meeting during which the committee members would evaluate the candidates and complete the nomination process. It was also decided that no limit would be put on the time for deliberation. The committee would meet and reconvene if necessary, until the two-thirds majority was achieved. In the intervening period, each member was required to review the file of each candidate in light of the evaluation criteria and prepare for the next meeting.

The facilitator started the third meeting — the nomination process — with a brief tutorial on user-application interaction. Interacting via the preference elicitation module (Fig. 4), the committee members anonymously ranked the five candidates and provided data on the relative strengths of their preferences. Appendix A lists the resulting individual weight vectors generated from the preference elicitation exercise. These vectors represent the relative strengths of the rankings of each committee member. The facilitator, then, conducted the first round of analysis. The data were analyzed to determine: (a) the level of agreement among the committee members; (b) those committee members whose preference rankings might serve as a focal point for dialogue aimed at advancing the consensus building process; and (c) candidates who may be deemed problematic based on the level of disagreement among the committee members' expressed preference for these candidates.

## 4.2.1. Determining the level of agreement

The reader will recall that the level of agreement was set by the committee members at two-thirds majority; in other words, a group strong agreement quotient (GSAQ) value of 0.66. The result computed from the first round of the nomination process showed a GSAQ of 0.712 at 0.985 level of significance (see Appendix B for details). Thus, the desired level of agreement was achieved. However, this did not mean that there were no differences among the committee members' preferences on which of the candidates should fill the dean's position. It simply means that the committee members were very close on their preference rankings of the candidates. We continue the analysis to demonstrate what information can be derived from the preference rankings.

## 4.2.2. Identifying key committee members

In situations of wide disagreement, the facilitator might want to identify those individuals around whom consensus can be built. In contrast to approaches that compute “group” scores, we are interested in identifying individuals who share agreement on preference rankings with a large number of their colleagues. The reader will recall that the individual strong agreement quotient (ISAQ) is a measure of agreement of that individual's preference rankings with each of the other group members. Table 1 displays the individual consensus vectors of each committee member. The ISAQ indicator values suggest that committee member 6 is the individual around whom the facilitator is most likely to be able to build consensus. This is because this individual's preference rankings share something in common with many of the other committee members. Group members 10 and 12 are also likely candidates, although less likely than group member 6. Armed with this information, the facilitator can encourage the committee members to discuss the preference rankings of member 6 in order to determine where there might be agreement and disagreement. This discussion could be open with all members knowing whose rankings they are discussing. On the other hand, the discussion could be "closed" with no one knowing the origin of the rankings, just that most of the group seems to agree on them.

## 4.2.3. Identifying problematic candidates

Another key issue for facilitators of group processes is identifying decision options that are problematic for the achievement of consensus; by this we mean identifying those options about which most of the members of the decision making group disagree. The ability to identify contentious decision options is important to good facilitation. This information could be used by the facilitator to lead discussion which could clarify problems decision makers have with particular alternatives. In the case discussed here, the facilitator may want to identify those candidates on whom there was much disagreement. To identify these individuals, we need to compute a new set of group consensus indicators. We do this analysis by excluding one candidate at a time as we compute the GSAQ and GSDQ, and then compare each such vector with the vector that included all the candidates. Table 2 displays the resulting GSAQ and GSDQ indicators.

Table 1  
Individual consensus vectors

<table><tr><td>Committee Member</td><td>ISAQ</td><td>ISDQ</td><td>ISDI</td></tr><tr><td>1</td><td>0.818</td><td>000</td><td>-0.017</td></tr><tr><td>2</td><td>0.727</td><td>000</td><td>-0.026</td></tr><tr><td>3</td><td>0.727</td><td>000</td><td>-0.018</td></tr><tr><td>4</td><td>0.727</td><td>000</td><td>-0.026</td></tr><tr><td>5</td><td>0.636</td><td>-0.091</td><td>-0.036</td></tr><tr><td>6</td><td>1.000</td><td>000</td><td>-0.014</td></tr><tr><td>7</td><td>0.273</td><td>-0.182</td><td>-0.036</td></tr><tr><td>8</td><td>0.636</td><td>000</td><td>-0.032</td></tr><tr><td>9</td><td>0.636</td><td>-0.091</td><td>-0.034</td></tr><tr><td>10</td><td>0.909</td><td>000</td><td>-0.021</td></tr><tr><td>11</td><td>0.545</td><td>000</td><td>-0.025</td></tr><tr><td>12</td><td>0.909</td><td>000</td><td>-0.016</td></tr></table>

Table 2  
Measures of agreement on decision options

<table><tr><td>Excluded Candidate</td><td>GSAQ</td><td>GSDQ</td></tr><tr><td>1</td><td>0.652</td><td>00</td></tr><tr><td>2</td><td>0.742</td><td>00</td></tr><tr><td>3</td><td>0.697</td><td>0.030</td></tr><tr><td>4</td><td>0.591</td><td>0.061</td></tr><tr><td>5</td><td>0.848</td><td>00</td></tr></table>

The reader will notice that the GSAQ indicator value improved significantly when candidate 5 was excluded, and it deteriorated significantly when candidate 4 was excluded. This analysis suggests that many of the committee members expressed varying preferences for candidate 5. And, on the contrary, many of the committee members agree on the preference rankings given to candidate 4. Here again, the facilitator can use this information to lead a discussion about the differing preferences that the members expressed for candidate 5.

## 5. Concluding discussion

We have presented an approach and a set of techniques that a facilitator can use to measure and assess consensus in group decision making processes. We have also illustrated with a case study how the techniques can be implemented in software applications to assist facilitators involved in group process work. The fundamental conjecture of this research is that techniques such as these can improve group facilitation. They could assist group facilitators in analyzing preference data and identifying “dead-ends” and “openings” which could help improve the consensus process. Studies have shown that information about individual and group positions can have an influence on preference tasks in group decision making situations [25]. Psychologists also argue that people have a greater tendency towards building consensus with those whom they perceive as sharing some common ground with themselves. Thus, knowledge about where an individual stands relative to the group on an issue might be important information when one is reassessing one’s position. Further, people are more willing to engage in dialogue if they understand each other’s positions on the issues under consideration. The ability to analyze consensus relevant data captured in GSS environments has the potential for improving group processes.

The approach and techniques we have presented help to advance the project of improved

GSS technology for group work. They provide the group process facilitator with a set of tools for identifying: (a) the level of agreement among the group members; (b) the level of disagreement in the group; (c) which individuals, by virtue of their shared agreement with divergent group members, might assist in brokering the dialogue; (d) who agrees and who disagrees on what decision alternatives; and (e) what decision alternatives are problematic. It is important to note that the measures that we suggested are “soft measures,” not “hard measures” (see Fedrizzi and Kacprzyk [10,11]). According to these researchers, “hard measures” indicate full consensus, the case of complete agreement between group members on all relevant issues, while “soft measures” attempt to find the degree to which group members agree as to their preferences with regard to most pairs of objects. And although many decision making meetings are convened for the purpose of “hammering out agreement” on issues upon which participants often hold differing views, most GSS environments offer limited support for “soft measures.”

## Appendix A

<table><tr><td>COMMITTEE MEMBERS</td><td>PREFERENCE VECTORS</td></tr><tr><td>1</td><td>(0.231, 0.143, 0.218, 0.202, 0.206)</td></tr><tr><td>2</td><td>(0.268, 0.118, 0.206, 0.240, 0.168)</td></tr><tr><td>3</td><td>(0.257, 0.156, 0.156, 0.241, 0.189)</td></tr><tr><td>4</td><td>(0.265, 0.136, 0.215, 0.226, 0.158)</td></tr><tr><td>5</td><td>(0.202, 0.169, 0.179, 0.227, 0.223)</td></tr><tr><td>6</td><td>(0.231, 0.154, 0.190, 0.259, 0.167)</td></tr><tr><td>7</td><td>(0.278, 0.099, 0.215, 0.244, 0.165)</td></tr><tr><td>8</td><td>(0.206, 0.150, 0.172, 0.242, 0.229)</td></tr><tr><td>9</td><td>(0.208, 0.164, 0.179, 0.222, 0.227)</td></tr><tr><td>10</td><td>(0.217, 0.171, 0.212, 0.233, 0.168)</td></tr><tr><td>11</td><td>(0.234, 0.167, 0.223, 0.228, 0.149)</td></tr><tr><td>12</td><td>(0.224, 0.160, 0.203, 0.239, 0.174)</td></tr></table>

Vectors of relative strengths of preferences

## Appendix B

<table><tr><td></td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td>1</td><td>0.988</td><td>0.984</td><td>0.990</td><td>0.990</td><td>0.986</td><td>0.983</td><td>0.988</td><td>0.992</td><td>0.992</td><td>0.989</td><td>0.993</td></tr><tr><td>2</td><td></td><td>0.989</td><td>0.998</td><td>0.974</td><td>0.992</td><td>0.999</td><td>0.977</td><td>0.976</td><td>0.987</td><td>0.990</td><td>0.991</td></tr><tr><td>3</td><td></td><td></td><td>0.988</td><td>0.988</td><td>0.994</td><td>0.982</td><td>0.989</td><td>0.988</td><td>0.987</td><td>0.983</td><td>0.991</td></tr><tr><td>4</td><td></td><td></td><td></td><td>0.975</td><td>0.992</td><td>0.996</td><td>0.974</td><td>0.976</td><td>0.991</td><td>0.995</td><td>0.993</td></tr><tr><td>5</td><td></td><td></td><td></td><td></td><td>0.987</td><td>0.964</td><td>0.998</td><td>01.00</td><td>0.989</td><td>0.979</td><td>0.991</td></tr><tr><td>6</td><td></td><td></td><td></td><td></td><td></td><td>0.986</td><td>0.988</td><td>0.986</td><td>0.996</td><td>0.994</td><td>0.998</td></tr><tr><td>7</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.968</td><td>0.966</td><td>0.979</td><td>0.984</td><td>0.984</td></tr><tr><td>8</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.998</td><td>0.985</td><td>0.975</td><td>0.989</td></tr><tr><td>9</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.988</td><td>0.979</td><td>0.990</td></tr><tr><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.998</td><td>0.999</td></tr><tr><td>11</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.997</td></tr></table>

Group strong agreement indicator = 0.712 at 0.985 level of significance. Correlation matrix computed from preference vectors.

## References

[1] R. Anson, Effects Cf Computer Support And Facilitator Support On Group Process And Outcomes, unpublished Ph.D. Dissertation, University of Minnesota, 1990.

[2] R.P. Bostrom, V.K. Clawson and R. Anson, Training People to Facilitate Electronic Environments, Working Paper, Department of Management, University of Georgia, 1991.

[3] N. Bryson, O. Ngwenyama and A. Mobolurin, A Qualitative Discriminant Process for Scoring and Ranking in Group Support Systems, Information Processing and Management 30(3), (1994), 389–405.

[4] R. Cook and T. Stewart, A Comparison of Seven Methods for Obtaining Subjective Descriptions of Judgmental Policy, Organizational Behavior and Human Performance 13, (1979), 31–45.

[5] A. Dennis, J. George, L. Jessup, J. Nunamaker and D. Vogel, Information Technology to Support Electronic Meetings, MIS Quarterly 12 (4), (1988), 591–624.

[6] A. Dennis, J. Nunamaker and D. Vogel, A Comparison of Laboratory and Field Research in the Study of Electronic Meeting Systems, Journal of Management Information Systems 7(2), (1991), 107–135.

[7] G. DeSantcis and R.B. Gallupe, A Foundation for The Study of Group Decision Support Systems, Management Science 33 (5), (1987), 589–609.

[8] G. Dickson, M. Limayem, J. Partridge and G. DeSanctis, Facilitating Computer Supported Meetings: A Cumulative Analysis In a Multiple criteria Task Environment, Working Paper, University of Minnesota, 1994.

[9] M. Doyle and D. Strauss, How To Make Meetings Work (Wyden, New York, 1976).

[10] M. Fedrizzi and J. Kacprzyk, On Measuring Consensus in the Setting of Fuzzy Preference Relations, in: K. Kacprzyk and M. Roubens Eds., Non-Conventional Preference Relations in Decision Making (Springer-Verlag, Berlin and New York, 1988), pp. 129–141.

[11] M. Fedrizzi and J. Kacprzyk, On Measuring Consensus in the Setting of Fuzzy Preference Relations, in: K. Kacprzyk and M. Roubens Eds., Non-Conventional Preference Relations in Decision Making (Springer-Verlag, Berlin and New York, 1988), pp. 129–141.

[12] T. Finholt and L. Sproull, Electronic Groups at Work, Organization Science 1 (1), (1990), 41–64.

[13] B. Golden, E. Wasil and P. Harker, The Analytic Hierarchy Process: Application and Studies (Springer-Verlag, New York, 1989).

[14] R. Grohowski, C. McGoff, D. Vogel, B. Martz and J. Nunamaker, Implementing Electronic Meeting Systems at IBM: Lessons Learned and Success Factors, MIS Quarterly 14 (4), (1990), 369–384.

[15] L. Hoffman and N. Maier, The Use of Group Decision to Resolve a Problem of Fairness, Personnel Psychology 12, (1959), 545–559.

[16] G.P. Huber, The Nature of Post Industrial Organizations, Management Science 30, (1984), 928–951.

[17] R. Irving and D. Conrath, The Social Attribute of Multiperson Decision making, IEEE Transactions on Systems, Man, and Cybernetics 18 (3), (1988).

[18] M. Jarke, M.T. Jelassi and M.F. Shakun, MEDIATOR: Towards a Negotiation Support System, European Journal of Operational Research 31, (1987), 314–334.

[19] M.F. Kaplan and C.E. Miller, Group Decision Making and Normative versus Informational Influence Effects of Type of Issues and Assigned Decision Rule, Journal of Personality and Social Psychology 53 (2), (1978), 306–313.

[20] R. Keeney and H. Raiffa, Decisions with Multiple Objectives: Preferences and Value Tradeoffs (John Wiley and Sons, New York, 1976).

[21] P.J. Korhonen, A Hierarchical Interactive Method for Ranking Alternatives with Multiple Qualitative Criteria, European Journal of Operational Research 24, (1986), 265–276.

[22] P. Korhonen, Using Harmonious Houses for Visual Pairwise Comparison of Multiple Criteria Alternatives, Decision Support Systems 7, (1991), 47–54.

[23] P. McLeod, What We Know, What We Don't Know, and What We Think We Know About GDSS, Proceedings of the Human Computer Action Workshop, University of Michigan, 1991.

[24] C. McGroff and L. Ambrose, Empirical Information from the Field: A Practitioners' View of Using GDSS in Business, Proceedings the 1991 HICCS, Vol. 3 (IEEE Computer Press, 1991).

[25] J. Nunamaker, D. Vogel, A. Heminger, B. Martz, R. Grohowski and C. McGroff, Experiences at IBM With Group Support Systems: A Field Study, Decision Support Systems 5 (2), (1989), 183–196.

[26] L. Phillips and M. Phillips, On facilitating groups, Working Paper, London School of Economics, England, 1990.

[27] A. Pinsonneault and K.L. Kraemer, The Effects of Electronic Meetings on Group Processes and Outcomes: An Assessment of the Empirical Research, European Journal of Operations Research 46, (1990), 143–161.

[28] R. Quinn, Beyond Rational Management (Jossey-Bass, San Francisco, CA, 1988).

[29] T. Saaty, The Analytic Hierarchy Process: Planning, Priority Setting, Resource Allocation (McGraw-Hill, New York, 1980).

[30] T. Saaty, Axiomatic Foundations of the Analytic Hierarchy Process, Management Science 32, (1986), 841–855.

[31] J. Shanteau, The Concept of Weight in Judgment and Decision Making: A Review and Some Unifying Proposals, Technical Report 228, Center for Research on Judgment and Policy, University of Colorado, Boulder, Colorado, 1980.

[32] D. Vogel, J. Nunamaker, W. Martz, R. Grohowski and C. McGoff, Electronic Meeting System Experience at IBM, Journal of Management Information Systems 6(3), (1989), 25–43.

[33] R. Watts, M. Alexander, C. Polaroid and R. Bostrom, The Use and Adoption of OptionFinder: A Keypad Based Group Decision Support System, 3M Management Institute, 1991.

Ojelanki K. Ngwenyama is Assistant Professor of Computing and Information Systems at The Michigan Business School, University of Michigan, Ann Arbor. Dr. Ngwenyama holds a Ph.D. in Computer Science and Information Systems from The Thomas J. Watson School of Engineering, State University of New York — Binghamton; an MBA from the Crouse Hinds School of Management, Syracuse University, New York, and an MSc. in Information Systems from Roosevelt University. His research has appeared in several journals including Information Systems, Information and Management, Information Processing & Management, Computer and Industrial Engineering and European Journal of Operations Research.

Noel Bryson is Associate Professor in the Department of Information Systems and Analysis, School of Business, Howard University, Washington, DC. Dr. Bryson holds a Ph.D. in Decision Sciences and Information Systems from the University of Maryland, College Park and an MEng in Systems Engineering from Howard University. His research has appeared in several journals including European Journal of Operations Research, Information Processing & Management, ORSA Journal of Computing, Journal of Multicriteria Decision Making, Journal of the Operational Research Society and Computers and Operations Research.

Ayodele Mobolurin is Associate Professor in the Department of Information Systems and Analysis, School of Business, Howard University, Washington, DC. Dr. Mobolurin holds a Ph.D. in Industrial Engineering and Operations Research from the University of Massachusetts, and an MEng in Systems Engineering from Howard University. His research has appeared in journals such as European Journal of Operations Research, Journal of Multicriteria Decision Making and Information Processing & Management.
