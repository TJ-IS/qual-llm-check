---
otero_id: 17219
otero_key: "K88EE5ZH"
title: "Coordinator support in a nemawashi decision process"
authors: "Kazuo Watabe; Clyde W. Holsapple; Andrew B. Whinston"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90002-7"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Coordinator support in a nemawashi decision process

Kazuo Watabe

Application System Research Laboratory, Kansai C&C Laboratory, NEC Corporation, Osaka, Japan

Clyde W. Holsapple

Department of Decision Science and Information Systems, College of Business and Economics, University of Kentucky, Lexington, KY 40506, USA

Andrew B. Whinston

Department of Management Science and Information Systems, Graduate School of Business, and IC $^{2}$ Institute, University of Texas at Austin, Austin, TX 78712, USA

There is a growing body of literature concerned with computerized support of distributed decision making. However, support for the distinctive Japanese way of distributed decision making has yet to be considered. At the heart of this decision making approach is nemawashi and the attendant ringi. A key role in a nemawashi decision process is that of a coordinator who endeavors to achieve a consensus, prepares informal and formal documents, and circulates the latter for consent. Here, we introduce a very flexible mathematical model to support the nemawashi process. This descriptive model, based in part on MCDM notions, accommodates a variety of coordinator strategies pertinent to different decision situations by considering participant preferences and influences. Such a model provides the foundation for understanding, designing, and implementing coordinator support systems to facilitate distributed decision making in Japanese organizations.

Keywords: Group decision making, Decision support systems, Multiattribute decision making.

## 1. Introduction

The emergence of Japan as a preeminent world economic power has focused attention on the distinctive and apparently effective style of Japanese management. The well-known emphasis placed on consensus building in making business

![](/api/attachments/K88EE5ZH/fulltext/images/b57889948ab8399fade7142d6ece98eb151f1eaa66e6284749f2a9018114555a.jpg)

Kazuo Watabe received the B.E. and M.E. degrees in applied physics from Waseda University, Tokyo, Japan, in 1979 and 1981, respectively. He joined NEC Corporation in 1981, and has been engaged in the research and development of office database systems, office form management systems, and office network systems. He is now Supervisor of the Network Research Laboratory, C&C Systems Research Laboratories, Kawasaki, Japan. His current research interests include group collaboration support systems (groupware), group decision support systems, and the Japanese way of group decision making. Mr. Watabe is a member of the Information Processing Society of Japan, the Operations Research Society of Japan, and the Japan Society for Management Informatics.

Clyde W. Holsapple is Professor of Decision Science and Information Systems and holds the Endowed Chair in Management Information Systems at the University of Kentucky. In addition to this books in the decision support system, data base management, and expert system areas, he has many research articles published in such journals as Decision Support Systems, Operations Research, The Computer Journal, Organization Science, Decision Sciences, IEEE Expert, Financial Management, Policy Sciences and Recherche Operationnelle. Dr. Holsapple is the DSS Area Editor for ORSA Journal on Computing and Associate Editor for Organizational Computing.

Andrew B. Whinston is Professor of Information Systems on the faculty of the College and Graduate School of Business, Department of Management Science and Information Systems at the University of Texas at Austin. His primary teaching interest is management information systems. His current research interests include data base management and applications of artificial intelligence to economics and management. He has also studied applied economics, regulatory economics, and accounting theory. Among his numerous publications, he has co-authored two books (with C. Holsapple and R. Bonczek), Foundations of Decision Support Systems (Academic Press, 1981), and Micro Database Management – Practical Techniques for Application Development (Academic Press, 1985). He has been a consultant to various companies, governmental agencies, and international organizations on data processing questions.

decisions is viewed as one of the key characteristics of the Japanese decision making process. While the consensus based approach has been successful, there is a potential for improving the efficiency of the process by introducing computer support. In order to successfully develop such a support system we first need to formalize our understanding of the process. The central purpose of this paper is to introduce a formal descriptive model of the Japanese consensus building approach to business decision making. Pursuant to this, it becomes reasonable to explore the form of the computer support that would improve efficiency without intruding into the fundamental nature of the process.

In the 1980s, decision support system (DSS) researchers have begun to consider the extent to which computers can do more than support individual problem solvers. For instance, a group decision support system (GDSS) is a DSS that aids a group of people involved in a decision-related meeting by promoting the sharing of information among group members and between the group and computer (Huber 1984). It has been argued that a GDSS can facilitate the thinking of group members (Adelman 1984). In addition to individual and group DSSs, it may be possible to create a DSS that furnishes organizational support in the sense of helping several people to sequentially contribute to a decision (Hackathorn and Keen 1981). Individual, group, and organizational DSSs are all relevant to the phenomenon of distributed decision making, wherein multiple individuals participate in addressing concurrent decision problems (Holsapple and Whinston 1988).

Understanding the nature of individuals' participation is very important for fully realizing the possibilities of computerized support for distributed decision making. This is true for both existing organizations and knowledge-based organizations of the future (Holsapple and Whinston 1987b). It has been suggested that different organization designs imply different desirable characteristics for decision support systems (Huber 1981). We contend that such differences also imply different possibilities for workable DSSs. Our concern here is with Japanese-style organizations, in which decision making is achieved through nemawashi and ringi processes. In developing a formal model of how distributed decision making works in such organizations, it can be seen where the individual who coordinates a decision making enterprise could benefit from computerized support. A secondary reason for introducing the model is that it may offer insights that can be transferred to or across managerial cultures.

An overview of decision making in Japanese organizations is provided in Section 2. Nemawashi and ringi processes are discussed informally and the coordinator role is defined. In Section 3, a mathematical model is introduced to describe the coordinator's deliberations. It may be regarded as an extension or adaptation of multiple criteria decision method ideas, and as a basis for coordinator support. An example to illustrate the model is furnished in Section 4. The Section 5 conclusion indicates additional research directions emanating from the model introduced here.

## 2. Decision Making In Japanese Organizations

## 2.1. Japanese Decision Making

The decision making process in Japanese organizations is different from that in western ones (Abegglen and Stalk 1985; Christopher 1986; Ouchi 1981; Pascale and Athos 1981; Watanabe 1987; Yang 1984). Simon's aspects of intelligence, design, and choice are common to both (Simon 1960). But which participants are involved in which aspects seem to differ. In American and European organizations, decision making tends to be relatively individualistic or autocratic with respect to choice, although intelligence and design may involve many of the decision's participants. In the Japanese style of decision making, all persons related to the decision problem or project participate in the choice aspect and this participation can have major impacts on what happens for intelligence and design aspects. The number of decision participants is usually between four to ten, but for important decisions it may be as high as 60 to 80 (Ouchi 1981). One person or a small group is assigned the role of coordinator and works toward gaining a consensus among the participants by obtaining their views, carrying out negotiations, and engaging in persuasion. This process of gaining a consensus is called nemawashi.

The original meaning of nemawashi is to dig around the root of a tree before transplanting. It is sometimes translated as “behind-the-scenes negotiations.” It does not have a negative connotation which the above English translation may convey. In Japan, nemawashi is always recommended for important problems and projects. Unless a consensus is gained among the participants through careful nemawashi, a proposed choice is not approved by them. Nemawashi is an effective process for incorporating participants’ opinions and for avoiding potential unhealthy conflicts among members. After success in gaining a consensus, the coordinator prepares a formal document detailing the proposal (i.e., proposed choice) and circulates it among the participants for consent. This document circulation stage of decision making is called ringi. Through nemawashi and ringi, everyone involved in the distributed decision making participates in the choice.

The nemawashi-ringi approach has some advantages and disadvantages. Among the advantages:

(a) Many persons' participation leads to better quality decisions, easier implementation, and higher morale than non-consensus choice.

(b) Risk-taking (i.e., responsibility) is shared.

(c) Each participant can take time to think through the proposal.

(d) Each participant's wishes may be incorporated in the decision (i.e., bottom-up or middle-out decision making).

Practical disadvantages that have been observed include the following:

(a) As the coordinator needs to consider many persons' opinions, it can be difficult for the coordinator to select an appropriate proposal from candidate alternatives.

(b) As the coordinator should negotiate with and persuade other participants for gaining a consensus, and circulate the ringi document sequentially, much effort and considerable time is required before a final formal decision is made.

(c) It is not obvious who should take responsibility for a multiparticipant decision. Sometimes, no one takes responsibility for results of a decision.

## 2.2. The Path Toward Consensus

For gaining a consensus and making a formal decision, the following five steps are taken in Japanese organizations (Ouchi 1981; Pascale and Athos 1981; Abegglen and Stalk 1985; Watanabe 1987).

## (a) Information collection (joho shyushyu)

When an important decision needs to be made regarding some project, a person or a small group (ritsuan-sha) is assigned as a coordinator and mediator. For convenience, we refer to this person or group simply as a coordinator. By consulting superiors, the coordinator identifies the persons in the organization concerned with the project. The coordinator then asks these participants about their opinions and wishes with respect to the project. If it is not possible to talk with top ranked managers directly, information on their views is acquired through their subordinates or others.

## (b) Data analysis and plan generation (ritsuan)

The coordinator analyzes the data and the opinions, and generates candidate plans. Some plans are suggested by other participants. Each plan is an alternative that has a potential for being a proposal for consensus. Experts in various project elements decide on the criteria for comparing the plans and they evaluate the plans for each criterion. It is permissible to draw on experts who are uninvolved in the decision or its outcome.

## (c) Plan selection (sentaku)

Considering other participants' opinions, the coordinator selects a candidate plan. It becomes a proposal for nemawashi. This is a very important step because which plan selected affects whether the next step is or is not successful.

## (d) Negotiation and persuasion (nemawashi)

The coordinator makes an informal document of the selected plan, shows it to other participants, and negotiates with them. If this fails to produce a consensus, the coordinator revises the document and tries again. Changes of environment sometimes affect the proposal. In such a case, the coordinator needs to amend it, inform the participants of the changes, and again try to gain a consensus. Steps (c) and (d) are repeated iteratively until the coordinator perceives that a consensus has been achieved.

## (e) Document circulation (ringi)

The coordinator prepares a formal document detailing the alternative inherent in the proposal. This is circulated among participants from the lower level participants to the top of the organization. Each participant affixes a personal seal to it, which indicates agreement with the plan or that the document has been read. In the latter case, there can be disagreement. If it is especially strong, the participant sometimes affixes the seal upside down. When the document has garnered all the participants' seals, the plan is considered to have been approved formally. If the document does not collect sufficient $^{1}$ properly oriented seals at this stage, the plan is abandoned.

## 3. Plan Selection and Negotiation Support

## 3.1. Multiple Criteria Decision Method

When making an important selection, people often compare many traits of the alternatives. For example, when selecting a computer for an office, traits for comparison might include price, processing speed, reputation of the manufacturer, quality of support, quality of the software available for a specific purpose, quantity of software for the computer, and ease of use. The importance of the various items are different. The multiple criteria decision method (MDCM) approach has been studied and used for choice analysis in such a problem (and much complicated ones) where there are many traits to compare (Cochrane and Zeleny 1973; Nijkamp and Spronk 1981; Starr and Zeleny 1977; Zeleny 1976; Zionts 1978). MCDM can be applied to the multiperson DSS context to help integrate multiple views of a problem and revise individual or group problem representations and opinions through interaction (Bui and Jarke 1986; Jarke 1986). Some multiperson DSSs employing MCDM are briefly reviewed in (Jarke 1986).

Our approach to modeling coordinator deliberations in Japanese organizations is in the spirit of MCDM. Although our work can be regarded as offering new extensions to MCDM, that is not the primary intent and will not be discussed. The intent is to provide a formal mathematical model for describing and studying nemawashi processes. Although MCDM ideas are involved in the model, we do not mean to suggest that alternative models could not be conceived from ideas or formulations in such areas as multiattribute utility theory, game theory, social judgement theory, and social choice theory. These may also give impetus to extensions of the model introduced here.

## 3.2. Coordinator Support

In step (b) of Section 2.2., the coordinator generates candidate plans and then selects one in step (c). It becomes the coordinator's proposal. The coordinator recommends it and works actively toward gaining formal consent for it. The challenge is how to select one of the plans. In addition to personal views, the coordinator needs to consider many factors such as other participants' wishes, experts' comments, the organization's surroundings, and environment prospects. A coordinator needs a rational and effective way to select a plan.

In general, MCDM is suitable for comparing plans with respect to many criteria and selecting one or some of them. In the coordinator support model introduced below, it is extended to multi-person decision making by considering various aspects of the participants. Moreover, our model allows the coordinator to adopt a strategy for plan selection that is most suitable for current surroundings and personal proclivities. All of this is provided in a systematic and easily computable way. The model also allows the coordinator's negotiation and persuasion efforts to be supported by knowing which points of the participants' preferences (i.e., criteria priorities) are different and by how much.

## 3.3. Preparatory Matrices

The coordinator should assemble two matrices: a plan evaluation matrix (E) and an individual criteria priority matrix (C). In addition two other vectors may need to be prepared, depending on which weight strategy is appropriate. Weight strategies are explained at Section 3.5.

(a) Plan evaluation matrix: E

E is a matrix that shows an evaluation of each plan on each criterion. The element $e_{ij}$ (i = 1 to h, j = 1 to m) of E is the evaluation of the ith plan with respect to the jth criterion. Conceptually, $e_{ij}$ may be qualitative such as the word excellent, good, or poor. However, for computability purposes, we consider $e_{ij}$ to be a nonnegative number. Each $e_{ij}$ value may have an associated certainty factor and may even be fuzzy (Holsapple and Whinston 1987a).

The E matrix should be as objective as possible, otherwise the results may become distorted. For this reason, the elements of E are determined by experts available to the coordinator. Normally, these experts are individuals, but may sometimes be groups of people. In the future, they may even be DSSs employing expert system techniques (Bonczek, Holsapple and Whinston 1980; Holsapple and Whinston 1987a). As noted earlier, some experts can be participants in ne-mawashi and ringi, while others are not. The plans and criteria that make up the E dimensions are specified by the coordinator in light of joho shyushyu and possibly consultations with available experts.

Thus, E can be viewed as a function of four main elements:

E = e(project, experts, coordinator,

other participants)

Project: Plans and criteria vary according to the characteristics of the decision project.

Experts: When experts evaluate the plans with respect to the criteria, the content of the matrix depends on their expertise and perceptions. Experts can also affect the identification and specification of criterion items and candidate plans.

Coordinator: The coordinator has ultimate responsibility for designating criteria and plans. A coordinator can also change an expert's evaluation if he or she does not think it is appropriate.

Other participants: In joho shyushyu, the coordinator asks other participants for their opinions. The plans and criterion items for E are therefore influenced by considering their opinions. Via joho shyushyu, the participants should have a consensus on the criterion items. This includes not only which criteria to compare, but also the interpretation or meaning of each and their evaluation scales.

(b) Individual criteria priority matrix: C

This matrix shows each participant's weight for each criterion. The element $c_{ij}$ ( $i = 1$ to $m$ , $j = 1$ to $n$ ) of $C$ is an indication of how important criterion $i$ is to participant $j$ . Like $e_{ij}$ , $c_{ij}$ could be a number, or a word (e.g., crucial, important, trivial) and can have an associated certainty. It could be fuzzy or single-valued. In the scope of this paper, we consider it to be a non-negative number. Moreover, we assume that

$$
\sum_ {i} c _ {i 1} = \sum_ {i} c _ {i 2} = \dots = \sum_ {i} c _ {i n}
$$

in order to treat individual differences in a normalized manner.

This matrix is constructed by the coordinator, who communicates (to the extent possible) with other participants to discover their preferences and intentions. Initially, the matrix C is incomplete. As formal and informal communication proceeds between the coordinator and others, the matrix is gradually fleshed out and adjusted until it becomes complete. This is not very difficult in Japanese organizations, as communication is very smooth because of the homogeneous culture (Watanabe 1987; Yang 1984) and executives usually convey their wishes to their subordinates. Thus, a coordinator can readily ascertain or at least reasonably estimate other participants' preferences for criteria.

If the coordinator finds it very difficult to determine some $c_{ij}$ or thinks it has become insufficient or incorrect, then a participant can be directly asked to evaluate priorities of criteria. In a case where C is constructed in this direct fashion, the coordinator needs to gain a consensus on the criteria items beforehand.

In summary, the matrix C depends on four elements:

$C = c(\text{project}, \text{coordinator}, \text{other participants},$

communication)

Project: Participants vary from one decision project to another. As in E, the criterion items also vary according to the decision project. Moreover, every criterion specified for E exists for C as well.

Coordinator: In Japanese organizations, the coordinator usually knows other participant's major criteria preferences. For those that are unknown, the coordinator makes educated guesses or tries to find them through communication.

Other participants: The participants' preferences are initially estimated by the coordinator. If this is not satisfactory, the coordinator directly solicits preferences from other participants.

Communication: The coordinator communicates with the other participants to understand their way of thinking, their opinions, and their criteria preferences. Thus, the nature of communication channels influences the elements of C.

(c) Individual influence vector: I

One participant's influence on a decision is often different from that of another participant, depending on position, status, expertise, and so forth. The element $\mathrm{i_j(j = 1\ to\ n)}$ of I denotes the influence of the jth participant. The coordinator estimates the vector by considering each participant's influence in the organization. In principle, $\mathrm{i_j}$ could take on a linguistic value such as high, low, medium. For computability, we consider elements of I to be non-negative numbers. In any case, both types of values could be modified with certainty factors or could be fuzzy.

The vector I depends on four factors:

I = i(project, participant status,

participant department,

participant reputation)

Project: The participants vary from one decision project to another. The influence of each participant depends in part on knowledge about the project.

Status of each participant: This is a highly significant factor for assessing each participant's influence. A participant of a higher position (vice president, for example) usually has more influence on a decision than a participant of a lower position (junior manager, for example). This is especially so in ordinary hierarchical organizations.

Department of each participant: The degree of influence varies subject to direct or indirect relations with the decision project. For example, a sales department manager typically has more influence than an R&D manager when it comes to deciding on a sales plan for the next year.

Reputation of each participant: Each participant's influence on decision is also related to that participant's reputation. If a participant has a good history of success for the type of decision project at hand, then the corresponding $\mathbf{i}_{\mathrm{j}}$ is higher than it would otherwise be. A participant whose influence is particularly high is a jitsuryoku-sha executive (Yang 1984). Such a person is effectively an opinion leader, having greater influence than others at the same status level. A formal mathematical treatment of reputation adjustments as a lynch pin of organization learning appears in (Ching, Holsapple and Whinston 1990).

(d) Individual persuasion difficulty vector: P

When the participants' preferences and opinions are so different that they favor different plans, the coordinator uses the art of persuasion in order to gain a consensus on a plan. In so doing, the coordinator considers the difficulty of persuasion for each member when selecting a plan. The element $\mathrm{p_j(j = 1\text{ to } n)}$ of $\mathbf{P}$ denotes the persuasion difficulty for the jth participant. It may be a number or a word (e.g., hard, medium, easy). It may have an associated certainty factor and could be fuzzy. Here, we assume $\mathbf{p_j}$ is nonnegative number.

The P vector constructed by a coordinator depends on four major factors:

P = p (project, participant personality, participant responsibility, coordinator-participant relationship)

Project: If the decision project is a participant's main concern, that participant may not compromise. Otherwise, concessions may be more easily obtained.

Participant's personality: Personality traits such as stubbornness or flexibility can affect the persuasion difficulty.

Responsibility: If a participant has to take great responsibility for the decision results, he or she may persist much more tenaciously than if lesser responsibility is assumed.

Relationship of the coordinator with each participant: If a participant and the coordinator have a good and close relationship (e.g., they often rely on each other), persuasion and cooperation are facilitated. On the other hand, mistrust inhibits collaboration (Lewicki and Litterer 1985).

## 3.4. Plan Selection Support

After identifying and generating alternative plans for the decision project, the coordinator selects one or more plans for which he or she thinks a consensus can be achieved. The coordinator has some selection strategies that are pertinent for different decision settings. Sometimes, a second strategy may need to be employed if the first strategy does not give a satisfactory result. The strategy chosen at a given juncture in a decision project depends on factors such as characteristics of the organization, the coordinator's inclinations or way of thinking, and other participants' power balance. Thus, our model must offer a variety of selection strategies. Correspondingly, a coordinator's DSS could offer advice about strategy selection, in addition to aiding the construction, storage, and maintenance of E, C, I, and P. Alternatively or as an extra, it could apply the selected strategy to determine the proposed plan(s) for use in nemawashi.

Before introducing and explaining the strategies initially encompassed by the model, three additional matrices are defined.

## (a) Supported plan matrix: S

$$
\mathrm{S} = \mathrm{EC}\tag{1}
$$

Matrix S reduces the evaluation of a plan to a single number for each participant, based on evaluations of the plan for the criteria and that participant's priorities for the criteria. Thus, $s_{ij}$ is an indication of the degree of approval that participant j has for plan i. If elements of E or C have certainty factors, then elements of S will also have certainty factors (calculated according to a joint certainty factor algebra (Holsapple and

Whinston 1987a)). Similarly, a fuzzy E or C will yield a fuzzy S (Holsapple and Whinston 1987a).

(b) Consensus matrix: S(k)

$$
\mathrm{S} (\mathrm{k}) = \mathrm{EC} (\mathrm{k})\tag{2}
$$

where for all i and j, $s_{kj}(k) > = s_{ij}(k)$ , $c_{ij} > = 0$ ( $s_{kj}(k)$ , $s_{ij}(k)$ : elements of S(k)) and C(k) is constructed of numbers such that for all j, $\Sigma_{i}|c_{ij}(k) - c_{ij}|$ is minimized ( $c_{ij}(k)$ : element of C(k), $c_{ij}$ : element of C) $\Sigma_{i}c_{i1}(k) = \Sigma_{i}c_{i2}(k) = \ldots \Sigma_{i}c_{in}(k)$ .

As long as one person supports plan k, the matrix $C(k)$ will exist. If there is no support for some plan k, then a $C(k)$ will not exist for that plan. It can be fairly eliminated from consideration because no participant supports it. Possibly, there is more than one $C(k)$ for a given plan k. In such a case, it is up to the coordinator to break the tie by selecting one of them.

By finding a C(k) and S(k), the coordinator is laying the groundwork for gaining a consensus on plan k. Achieving such a consensus will involve the reconciliation of C and C(k). The resultant S(k) is an S matrix for which every participant gives plan k the highest approval. S(k) takes the following form, where $g_{1}\ldots g_{n}$ denote the maximum amounts for their respective columns.

$$
\begin{array}{c c c c c c} & & \text {Participants} \\ 1 & \left[ \begin{array}{c c c c c} 1 & \cdot & \cdot & \cdot & s _ {1 n} ^ {n} \\ s _ {1 1} ^ {\prime} & \cdot & \cdot & \cdot & s _ {1 n} ^ {\prime} \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ g _ {1} & \cdot & \cdot & \cdot & g _ {n} \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ h & s _ {h 1} ^ {\prime} & \cdot & \cdot & s _ {h n} ^ {\prime} \end{array} \right] \end{array}
$$

Clearly, if S = EC is S(k) for some k, then no adjustment to C is necessary to reconcile it with C(k) (i.e., C(k) = C). The matrix E is considered to be fixed by the time plan selection commences.

(c) Difference of preferences: D(k)

$$
\mathrm{d} _ {\mathrm{ij}} (\mathrm{k}) = \left| c _ {\mathrm{ij}} (\mathrm{k}) - c _ {\mathrm{ij}} \right| \left(\mathrm{d} _ {\mathrm{ij}} (\mathrm{k}): \text { element   of } \mathrm{D} (\mathrm{k}) \right.\tag{3}
$$

D(k) is the difference between the initial (i.e., “real”) C and a target priority matrix used to produce S(k). D(k) shows where and by what amount the initial C would need to be changed to reach a consensus on plan k.

## 3.5. Weighting Strategies

Allowing the existence of I and P suggests four ways for a coordinator to weight each participant's plan preferences. Each weighting strategy leads to one variant of each plan selection strategy as described in Section 3.6. Within a plan selection strategy, the organizer can opt for any of the following weighting strategies, according to the characteristics of the organization and decision project. Any of the weighting strategies can be observed in Japanese organizations. However, in our first-hand observation of Japanese decision making, (b) seems to be the most prevalent.

## (a) Weight by criterion only (C)

The coordinator does not distinguish among participants based on either influence or persuasion difficulty. This is a common weight strategy in situations where participants have the same or almost the same status (e.g., general managers only or vice presidents only).

(b) Weight by criterion and individual influence (C and I)

The coordinator considers the influence of each participant. This is often the case with situations where participants are diverse, such as a decision project involving rank-and-file employees, junior and senior managers, and top-rank executives. Their influences are different. The coordinator usually gives greater weight to the wishes of higher ranked participants than those of lower ranked ones, because objection of the former against a plan may be fatal. If there is a jitsuryoku-sha whose choice draws the attention of other participants, the coordinator gives high points to that key person's influence. Sometimes a jitsuryoku-sha is so powerful that the coordinator has no option but to obey his or her wishes.

(c) Weight by criterion and individual persuasion difficulty (C and P)

This weight strategy is for situations where the participants' persuasion difficulties are different, when there is a range from tough negotiators to flexible participants. This is often the case in organizations where various persons with different values work for various objectives.

(d) Weight by criterion, individual influence, and individual persuasion difficulty (C, I, P)

This weighting strategy encompasses all of the above factors. It is the most participant-oriented, consensus-seeking weighting scheme. It requires the coordinator to make an individual criteria priority matrix (C), individual influence matrix (I), and individual persuasion difficulty matrix (P). This is for the situation where there are many differences on all of these factors across the participants. When using this strategy, the matrices I and P should be independent for fairness.

## 3.6. Plan Selection Strategies

Selecting the objectively “best” plan is important. In Japanese organizations however, selecting a plan that is approved by all the participants and is easily implementable with all participants’ cooperation is often more important. Therefore, the coordinator usually thinks of the best plan as one for which he or she can produce a consensus in a timely fashion. In cases where plans tie or are close to a tie, highest ranking participants break the tie.

Our model identifies six major strategies for selecting an appropriate plan to carry into nemawashi. Each can be observed in Japanese organizations and must have four variants corresponding to the four weighting strategies. The coordinator's choice is situation-dependent. The coordinator's choice can also vary according to his or her personality, skills, and way of thinking. For instance, the coordinator may have a tendency to select a plan that keeps the overall persuasion effort to a minimum, or saves everyone's face, or embodies on a personal idea.

## 3.6.1. Least Sum of Preference Difference

This strategy is to select a plan that keeps the total dissatisfaction of the participants at a minimum. This may be the shortest road for the coordinator to choose in the direction of gaining a consensus by persuading the participants. Based on the literature and our first-hand observations, it can fairly be regarded as the most popular plan selection strategy in Japanese organizations.

Figure 1 shows examples of dissatisfaction distributions. The y-axis expresses individual degree of dissatisfaction. The x-axis shows participants sorted by descending order of the dissatisfaction degree. The order of participants in the x-axis is different for each plan. This figure does not mean that a person opposes all plans nor that a person favors all plans. Notice that the plans have distinct distribution characteristics. Plan A has a uniform distribution from support to objection. Plan B is one with two extremes. For Plan C there is no extremely dissatisfied participant, but the plan is generally unpopular. No single plan is dominant with respect to achieving a consensus. Which one should the coordinator select to carry forward into nemawashi? By the least sum of preference difference strategy, Plan B is selected as it has the smallest total dissatisfaction.

![](/api/attachments/K88EE5ZH/fulltext/images/81fe061389f940f21b02aff632e45216c045508ccaee5b5a2434a86e3367e1da.jpg)  
Participants  
Fig. 1. Examples of Relative Dissatisfaction Distribution.

The four variants of this selection strategy are as follows:

(a) Least sum of preference difference Make a vector of the following form.

$$
\mathrm{U} (\mathrm{k}) = \left(\sum_ {\mathrm{j}} \mathrm{d} _ {\mathrm{j} 1} (\mathrm{k}), \sum_ {\mathrm{j}} \mathrm{d} _ {\mathrm{j} 2} (\mathrm{k}), \dots , \sum_ {\mathrm{j}} \mathrm{d} _ {\mathrm{jn}} (\mathrm{k})\right)\tag{4}
$$

$$
\left(\mathrm{d} _ {\mathrm{ij}} (\mathrm{k}): \text {   an   element   of   } \mathrm{D} (\mathrm{k})\right)
$$

The element $u_{j}(k)$ of U(k) designates ith participant's dissatisfaction for plan k. The coordinator selects plan k such that

$$
\min _ {k} \left(\sum_ {j} u _ {j} (k)\right)\tag{5}
$$

$\left(u_{j}(k):an element of U(k)\right)$

This involves the sum of all the participants' dissatisfaction for plan k. Therefore, choosing a plan that minimizes the expression means the total of needed changes in participant's preference (total dissatisfaction) weighted by criterion importance becomes as small as possible. This is equivalent to selecting plan k such that

$$
\max _ {k} \left(\sum_ {j} s _ {k j}\right) \quad \left(s _ {k j}: \text { an   element   of } S\right)
$$

(b) Least sum of preference difference weighted by individual influence

$$
\mathrm{U} ^ {\mathrm{i}} (\mathrm{k}) = \left(\mathrm{i} _ {1} \mathrm{u} _ {1} (\mathrm{k}), \mathrm{i} _ {2} \mathrm{u} _ {2} (\mathrm{k}), \dots , \mathrm{i} _ {\mathrm{n}} \mathrm{u} _ {\mathrm{n}} (\mathrm{k})\right)\tag{6}
$$

The coordinator chooses plan k such that

$$
\min _ {k} \left(\sum_ {j} u _ {j} ^ {i} (k)\right)\tag{7}
$$

$$
\left(\mathrm{u} _ {\mathrm{j}} ^ {\mathrm{i}} (\mathrm{k}): \text {   an   element   of   } \mathrm{U} ^ {\mathrm{i}} (\mathrm{k})\right)
$$

This is equivalent to selecting the plan k having the highest element in SI.

(c) Least sum of preference difference weighted by persuasion difficulty

$$
\text { Define } \mathrm{U} ^ {\mathrm{p}} (\mathrm{k}) = \left(\mathrm{p} _ {1} \mathrm{u} _ {1} (\mathrm{k}), \mathrm{p} _ {2} \mathrm{u} _ {2} (\mathrm{k}), \dots , \mathrm{p} _ {\mathrm{n}} \mathrm{u} _ {\mathrm{n}} (\mathrm{k})\right)\tag{8}
$$

The coordinator chooses plan k such that

$$
\min _ {k} \left(\sum_ {j} u _ {j} ^ {p} (k)\right)\tag{9}
$$

$$
\left(\mathrm{u} _ {\mathrm{j}} ^ {\mathrm{p}} (\mathrm{k}): \text {   an   element   of   } \mathrm{U} ^ {\mathrm{p}} (\mathrm{k})\right)
$$

Here, the coordinator attempts to keep that total persuasion effort for gaining a consensus to a minimum. This is equivalent to selecting plan k with the highest element in SP.

(d) Least sum of preference difference weighted by individual influence and persuasion difficulty

Define $\mathbf{U}^{\mathrm{ip}}\mathbf{k})$

$$
\begin{array}{l} = \left(\left(i _ {1} + p _ {1}\right) u _ {1} (k), \left(i _ {2} + p _ {2}\right) u _ {2} (k), \dots , \right. \\ \left. \left(i _ {n} + p _ {n}\right) u _ {n} (k)\right) \end{array}\tag{10}
$$

The coordinator selects plan k subject to

$$
\min _ {k} \left(\sum_ {j} u _ {j} ^ {\mathrm{ip}} (k)\right)\tag{11}
$$

$$
\left(\mathrm{u} _ {\mathrm{j}} ^ {\mathrm{ip}} (\mathrm{k}): \text {   an   element   of   } \mathrm{U} ^ {\mathrm{ip}} (\mathrm{k})\right)
$$

This strategy treats highly influential participants and tough negotiators well by attaching more significance to their approval. For instance, it tends to give more weight to participants who are most difficult to persuade, decreasing the likelihood that they will need to be persuaded in nemawashi. Like (b), it allows the coordinator to consider important participants in the interest of lessening effort required for gaining a consensus. This is equivalent to selecting the plan k having the highest element in S(I + P).

## 3.6.2. Majority

In some organizations (including political systems), majority rule is a common method for selecting a plan after sufficient discussion of the project or the problem. However, in Japanese organizations, this method of decision making is not very popular because unanimous decision is preferable for smooth implementation. Participants who object to a plan may not try to implement it very well. The majority method also has another disadvantage: it loses information on each participant's second or third choices which may allow a consensus to be reached via compromise. In a Japanese organization, majority rule may serve as a method of last resort when there is not decision time left or no room for negotiation, persuasion and compromise. Even though majority rule is not the usual way of making a decision, a majority strategy may be used to select the plan that is to be carried forward into nemawashi.

The four variants of this strategy are as follows:

## (a) Simple majority

The coordinator computes matrix S and selects a plan that has approval from the most participants. This has the same or similar effect as when each participant personally chooses and votes for a plan.

## (b) Majority weighted by individual influence

Using matrix S, the coordinator selects a plan for each participant. These are weighted by the respective influences of the participants. A plan with the highest sum is selected for entering nemawashi.

## (c) Majority weighted by persuasion difficulty

Using matrix S, the coordinator selects a plan for each participant. The vote is weighted by the respective degrees of persuasion difficulty for the participant. A plan with the lowest sum is selected.

(d) Majority weighted by individual influence and persuasion difficulty

The vote is weighted by a combination of individual influence and inverse persuasion difficulty. The plan having the highest sum is selected.

## 3.6.3. Minimum of Maximum Preference Difference

In the attempt to achieve consensus, the coordinator chooses a plan needing the least preference change for the least satisfied participant. This strategy makes no participant extremely dissatisfied and at the same time saves face for all participants (i.e., the Japanese way!). However, the overall persuasion effort for gaining a consensus, is not always minimized by this strategy.

The four variants of this selection strategy are as follows:

(a) Minimum of maximum preference difference The coordinator selects plan k such that $\min_{k}\left(\max_{j}(u_{j}(k))\right)$ (12)

(b) Minimum of maximum preference difference weighted by individual influence
The coordinator selects a plan k such that $\min_{k}(\max_{j}(u_{j}^{i}(k)))$ .

(c) Minimum of maximum preference difference weighted by persuasion difficulty
The coordinator selects a plan k such that $\min_{k}(\max_{j}(u_{j}^{p}(k)))$ .

(d) Minimum of maximum preference difference weighted by individual influence and persuasion difficulty
The coordinator selects a plan k such that $\min_{k}(\max_{j}(u_{j}^{\mathrm{ip}}(k)))$ .

## 3.6.4. Minimum Dissatisfaction Exceeding a Threshold

To persuade strongly dissatisfied participants is very difficult and requires considerable time and effort by the coordinator. Thus, we posit a strategy to select a plan that minimizes the sum of extreme dissatisfaction margins that exceed a certain threshold of dissatisfaction. In Figure 2, when t is set as a threshold of dissatisfaction, Plan A is selected against Plan B because the size of its dissatisfaction area above t is smaller than that of Plan B.

The four variants of this plan selection strategy are as follows:

(a) Minimum of dissatisfaction exceeding a threshold

Designate $t_{a}$ , a value that the coordinator wants as the threshold of persuasion. Construct $\mathrm{Mt}_{\mathrm{a}}(\mathrm{k})$ from $\mathrm{U}(\mathrm{k})$ by changing those elements whose values are smaller than $t_{a}$ into 0 and leaving other elements as they are. The coordinator selects a plan k such that

$$
\min _ {k} \left(\sum_ {j} m _ {t j} (k)\right)\tag{13}
$$

$$
\left(\mathrm{m} _ {\mathrm{tj}} (\mathrm{k}): \text {   an   element   of   } \mathrm{Mt} _ {\mathrm{a}} (\mathrm{k})\right)
$$

(b) Minimum of dissatisfaction exceeding a threshold weighted by individual influence Here, the coordinator uses $U^{i}(k)$ instead of $U(k)$ and $t_{b}$ instead of $t_{a}$ , above. Let $M^{i}t_{b}(k)$ correspond to $Mt_{a}(k)$ . The coordinator selects a plan k such that $\min_{k}\left(\sum_{j}m_{ij}^{i}(k)\right)$ (14)

$\left(m_{tj}^{i}(k):an element of M^{i}t_{b}(k)\right)$

(c), (d) These variants are developed in a similar manner.

Participants  
![](/api/attachments/K88EE5ZH/fulltext/images/ebcad8a84990398e60de7552c8c0940a749f82e53c0a5673d42e935bdd0053a9.jpg)  
Fig. 2. Minimum Dissatisfaction Exceeding a Threshold.

![](/api/attachments/K88EE5ZH/fulltext/images/b5c5824ed39c3988b8e3480f24ea756a4cbed30b67c877a06f9d67f44eefc031.jpg)  
Fig. 3. Minimum Sum of Dissatisfaction Excluding Unper-suadable Participants.

3.6.5. Minimum Sum of Dissatisfaction Excluding Unpersuadable Participants

This strategy is for a situation where the coordinator is willing to forego persuading a few participants and circulate the ringi document without full approval. Sometimes there are participants who are very dissatisfied with the proposed plan and the coordinator gives up on attempts to persuade them. In Japanese organizations, it is possible to pass a plan when only a few participants object to it, provided they are not high-ranking executives. A plan selection strategy when facing such a situation is to minimize the dissatisfaction total, exclusive of very dissatisfied participants. The sum of dissatisfaction of all the participants for plan k ( $\Sigma_{i}\Sigma_{j}d_{ij}(k)$ ) may be high due to such participants. By excluding such participants when considering each plan, the persuasion effort is eased or becomes feasible. In Figure 3, this strategy selects Plan B rather than Plan A where t is set as the threshold. The total dissatisfaction area under t is smaller for Plan B.

(a) Minimum sum of dissatisfaction excluding un-persuadable participants

Let $t_{a}^{\prime}$ be the designated threshold and define

$$
\mathrm{X} (\mathrm{k}) = \left(\mathrm{U} (\mathrm{k}) - \mathrm{Mt} _ {\mathrm{a}} ^ {\prime} (\mathrm{k})\right)\tag{15}
$$

The coordinator selects a plan k such that

$$
\min _ {k} \left(\sum_ {j} x _ {j} (k)\right)\tag{16}
$$

$\left(\mathrm{x}_{\mathrm{j}}(\mathrm{k})\colon \text{an element of } \mathrm{X}(\mathrm{k})\right)$

(b), (c), (d) These variants are similar to those developed earlier.

## 3.6.6. The Coordinator's Choice

The foregoing strategies place greater emphasis on achieving a consensus, at the possible expense of fully considering the quality of the plans. If the coordinator evaluates a plan to be clearly superior in quality but inferior with respect to consensus prospects, he or she may be able to select that plan. In Japanese organizations however, it is not easy to pass such a plan. Thus this strategy is very uncommon. If it is adopted, the coordinator must be prepared for a lengthy, difficult, and possibly fruitless persuasion effort.

## 3.7. Negotiation and Persuasion Support

When the coordinator does not have a ready-made consensus for the selected plan, he or she needs to negotiate with and persuade others. Generally, for negotiating with and persuading others, it is very important to understand on which points there are differences and how great those differences are. A DSS for coordinator support should help in this regard. Beyond assisting in the choice of a selection strategy and in the selection of a plan by applying that strategy, there is an opportunity for the coordinator's DSS of facilitate nemawashi. For instance, it may be devised to help the coordinator understand the aforementioned differences by finding (e.g., computing) D(k), identifying who is opposed to plan k and in what way, assessing which participant's preference priorities to target for change via persuasion, and so forth. In short, the creator of a coordinator DSS should consider how it can support effective preparation and execution of nemawashi for gaining a consensus. The foregoing model identifies important factors for guiding the development of such DSSs.

## 4. Example

The ensuing example serves to illustrate various aspects of the model for coordinator support. Suppose there is a project to decide what vendor should be the source of personal computers at a company. Mr. Suzuki is appointed as the coordinator. Three managers are involved as participants in this decision project: a general manager (GM), an accounting department manager (AM), and a manufacturing department manager (MM). Three competitive PC manufacturers (Compick, BBQ, and SEA) are identified via joho shyushyu. Experts available to Mr. Suzuki evaluate the manufacturers on three major criteria (Price, Performance, and Support), yielding:

$$
\mathrm{E} = \left[ \begin{array}{c c c} 6 & 9 & 7 \\ 4 & 7 & 1 0 \\ 1 0 & 4 & 3 \end{array} \right] \quad \begin{array}{l l} \text { Compick   (Plan   1) } \\ \text { BBQ   (Plan   2) } \\ \text { SEA   (Plan   3) } \end{array}
$$

Mr. Suzuki finds that the general manager is especially sensitive to support, that the accounting manager is very sensitive to price, and so forth. He estimates the individual criteria priority matrix C as follows:

$$
\mathrm{C} = \left[ \begin{array}{l l l} 6 & 1 0 & 6 \\ 4 & 4 & 8 \\ 1 0 & 6 & 6 \end{array} \right] \begin{array}{l} \text { Price } \\ \text { Performance } \\ \text { Support } \end{array}
$$

By expression (1), S is computed to be:

$$
\mathrm{S} = \left[ \begin{array}{l l l} 1 4 2 & 1 3 8 & 1 5 0 \\ 1 5 2 & 1 2 8 & 1 4 0 \\ 1 0 6 & 1 3 4 & 1 1 0 \end{array} \right] \begin{array}{l} \text {Compick} \\ \text {BBQ} \\ \text {SEA} \end{array}
$$

Notice that there is no dominant plan. The GM favors BBQ, while the other two favor Compick. In addition, no plan is completely dominated. Many C(k) possibilities exist. Alternatives may be generated by Mr. Suzuki's DSS. Suppose he adopts the following set of C(k):

$$
\mathrm{C} (1) = \left[ \begin{array}{c c c} 7 & 1 0 & 6 \\ 5 & 4 & 8 \\ 8 & 6 & 6 \end{array} \right] \quad \mathrm{D} (1) = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 0 & 0 \\ 2 & 0 & 0 \end{array} \right]
$$

$$
\mathrm{C} (2) = \left[ \begin{array}{c c c} 6 & 8. 6 & 5 \\ 4 & 3. 4 & 7 \\ 1 0 & 8 & 8 \end{array} \right] \quad \mathrm{D} (2) = \left[ \begin{array}{c c c} 0 & 1. 4 & 1 \\ 0 & 0. 6 & 1 \\ 0 & 2 & 2 \end{array} \right]
$$

$$
\mathrm{C} (3) = \left[ \begin{array}{c c c} 1 0. 3 & 1 0. 5 & 1 0. 5 \\ 1. 7 & 3. 5 & 4 \\ 8 & 6 & 5. 5 \end{array} \right] \quad \mathrm{D} (3) = \left[ \begin{array}{c c c} 4. 3 & 0. 5 & 4. 5 \\ 2. 3 & 0. 5 & 4 \\ 2 & 0 & 0. 5 \end{array} \right]
$$

The corresponding D(k) are computed by the DSS.

Mr. Suzuki estimates the individual influence matrix I to be:

$$
\mathrm{I} = \left[ \begin{array}{l} 5 \\ 2 \\ 2 \end{array} \right]
$$

He does not estimate a persuasion difficulty matrix P, because he thinks the persuasion difficulties are nearly even.

Suppose Mr. Suzuki chooses the strategy we have called the least sum of preference difference (3.6.1 (a) and (b)). His DSS makes the following calculations:

$$
\begin{array}{l l} \mathrm{U(1)} = [ 4 0 0 ] & \sum_ {\mathrm{j}} \mathrm {u_ {j} (1)} = 4 \\ \mathrm{U(2)} = [ 0 4 4 ] & \sum_ {\mathrm{j}} \mathrm {u_ {j} (2)} = 8 \\ \mathrm{U(3)} = [ 8. 6 1 9 ] & \sum_ {\mathrm{j}} \mathrm {u_ {j} (3)} = 1 8. 6 \end{array}
$$

If he chooses not to consider I, then Plan 1 is selected to carry forward into nemawashi, where GM needs to be persuaded to achieve a consensus. Comparing the first columns of C and C(1), he can see a basis for the persuasion effort that lies ahead.

If I is to be considered, the following DSS calculations are relevant:

$$
\begin{array}{r l} & {\mathrm {U^ {i}} (1) = [ 2 0 0 0 ], \mathrm {U^ {i}} (2) = [ 0 8 8 ],} \\ & {\quad \mathrm {U^ {i}} (3) = [ 4 3 2 1 8 ],} \\ & {\sum_ {\mathrm{j}} \mathrm {u_ {j} ^ {i}} (1) = 2 0, \sum_ {\mathrm{j}} \mathrm {u_ {j} ^ {i}} (2) = 1 6, \sum_ {\mathrm{j}} \mathrm {u_ {j} ^ {i}} (3) = 6 3.} \end{array}
$$

When considering I, Mr. Suzuki selects Plan 2 and in nemawashi works at persuading AM and MM.

![](/api/attachments/K88EE5ZH/fulltext/images/27537b4258bd9e771328ad6f901c40167dbb0fe0bc31cd0bff7e194e4120fde7.jpg)  
Fig. 4. Relative Dissatisfaction in the Example.

If the simple majority strategy (3.6.2(a)) is employed, Plan 1 is selected at 2 persons are in favor of it. If he chooses strategy 3.6.2(b), Plan 2 is selected.

By the strategy 3.6.3.(a), Mr. Suzuki can select either Plan 1 or Plan 2. As Figure 4 shows, both minimize the greatest dissatisfaction. Using the variant that considers individual influence, he selects Plan 2 The model's other strategies can be applied in a similar fashion.

## 5. Summary and Conclusions

Characteristics of distributed decision making in Japanese organizations were briefly described, including the drive towards a consensus through nemawashi and ringi processes. The crucial role of the coordinator was sequenced into five stages with possible iteration. With this background, a formal model of distributed decision making in Japanese organizations was introduced. It can be seen as an extension of MCDM to distributed decision making in a nemawashi and ringi context. The model provides combinations of four weighting strategies and six selection strategies at alternative means for selecting a plan appropriate to any of various situations. The selected plan reflects opinions (optionally including influence and persuadability) of the participants. The model also provides a basis for supporting for negotiation and persuasion leading to consensus for the selected plan.

Through its consideration of various factors such as attributes of plans, personal preferences for attributes, influences of individuals on decisions, and individual difficulties of persuasion, we contend that the model is fairly descriptive of the human coordinator's way of thinking when selecting a candidate plan. As such, it can serve as a basis for grasping the possibilities and requirements of computerized systems to support the Japanese style of distributed decision making. We have identified several areas where a DSS could support coordinator activities and therefore support the important nemawashi style of distributed decision making. A next step is the design of DSS prototypes for coordinator support. Of course, these could vary widely in scope and appearance.

Future investigation will assess the extent to which the model can be extended or adapted to address distributed decision making in the context of other organization cultures. It may be that simple variants of the model are capable of formally characterizing American and European organizations. The model may have normative implications for them. Additional research directions opened by the model include exploring additional weighting or selection strategies, analyzing hybrid strategies, and discovering algorithms to aid in the determination of C(k). With the model introduced here, researchers are better equipped to conduct field studies of nemawashi. Such studies may well lead to extensions or variants of our model.

## References

[1] J.C. Abegglen and G. Stalk, Jr., Kaisha, The Japanese Corporation (Basic Books, New York, 1985).

[2] L. Adelman, “Real-Time Computer Support for Decision Analysis in a Group Setting”, Interfaces (March 1984).

[3] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, “Future Directions in Developing Decision Support Systems,” Decision Science (Oct. 1980).

[4] T.X. Bui and M. Jarke, “Communications Design for Co-oP: A Group Decision Support System,” ACM Trans. Office Information Systems, No. 2 (April 1986) 81–103.

[5] C. Ching, C.W. Holsapple and A.B. Whinston, “Reputation, Learning and Coordination in Distributed Decision-Making Contexts,” Organizational Science (1990) forthcoming.

[6] R.C. Christopher, Second to None (Fawcett Columbine, New York, 1986).

[7] J.L. Cochrane and M. Zeleny, Eds., Multiple Criteria Decision Making (University of South Carolina Press, Columbia, SC, 1973).

[8] R.D. Hackathorn and P.G. Keen, “Organizational Strategies for Personal Computing in Decision Support Systems,” MIS Quarterly (Sept. 1981).

[9] C.W. Holsapple and A.B. Whinston, Business Expert Systems (Irwin, Homewood, IL, 1987).

[10] C.W. Holsapple and A.B. Whinston, “Knowledge-Based Organizations,” Information Society 5, No. 2 (1987).

[11] C.W. Holsapple and A.B. Whinston, “Distributed Decision Making: A Research Agenda,” ACM SIGOIS Bulletin, 9, No. 1 (1988).

[12] G.P. Huber, “The Nature of Organizational Decision Making and the Design of Decision Support Systems,” MIS Quarterly (June 1981).

[13] G.P. Huber, “Issues in the Design of Group Decision Support Systems,” MIS Quaterly (Sept. 1984).

[14] M. Jarke, “Knowledge Sharing and Negotiation Support in Multiperson Decision Support Systems”, Decision Support Systems 2, No. 1 (1986) 93–102.

[15] R.J. Lewicki and J.A. Litterer, Negotiation (Irwin, Homewood, IL, 1985).

[16] P. Nijkamp and J. Spronk, Eds., Multiple Criteria Analysis (Gower, Hampshire, 1981).

[17] W.G. Ouchi, Theory Z (Addison-Wesley, Reading, MA, 1981).

[18] R.T. Pascale and A.G. Athos, The Art of Japanese Management (Warner Books, New York, 1981).

[19] H. Simon, The New Science of Management Decision (Harper & Row, New York, 1960).

[20] M. Starr and M. Zeleny, Eds., Multiple Criteria Decision Making (North-Holland, New York, 1977).

[21] T. Watanabe, Demystifying Japanese Management (Gakuseisha, Tokyo, 1987).

[22] C.Y. Yang, “Demystifying Japanese Management Practices”, Harvard Business Review, (Nov.-Dec. 1984) 172–182.

[23] M. Zeleny, Ed., Multiple Criteria Decision Making Kyoto 1975 (Springer-Verlag, New York, 1976).

[24] S. Zionts, Ed., Multiple Criteria Problem Solving: Proceedings (Springer-Verlag, New York, 1978).
