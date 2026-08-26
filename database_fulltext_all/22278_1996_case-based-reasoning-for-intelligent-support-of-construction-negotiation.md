---
otero_id: 22278
otero_key: "84W46WBF"
title: "Case-based reasoning for intelligent support of construction negotiation"
authors: "Heng Li"
year: "1996"
journal: "Information & Management"
doi: "10.1016/s0378-7206(96)01058-0"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Case-based reasoning for intelligent support of construction negotiation

Heng Li $^{1}$

Department of Civil Engineering, Caulfield School of Engineering, Monash University, Melbourne 3145, Vic., Australia

## Abstract

Negotiation and conflict resolution are major ill-structured and complex problems in construction. Due to the uncertain and changing nature of the processes, it is important for negotiators to have access to previous records, to communicate effectively with each other, and to have an agent acting as the mediator when deadlocks occur. This paper presents a computer model which employs case-based reasoning (CBR) to provide intelligent support to construction negotiations. This model has been implemented in the MEDIATOR, a computer program that utilises previous cases as a basis for addressing new problems. In contrast to conventional expert systems (ESs) that use compiled knowledge in problem solving, the system selects similar cases to help in solving a given negotiation problem. The selected case is then modified and adapted to generate proposals that should move people towards a settlement.

Keywords: Adaptation; Case-based reasoning; Case similarity; Construction negotiation; Mediator

## 1. Introduction

Construction management necessarily involves negotiating prices and conditions for subcontracting and resolving disputes. Negotiation has been typically described in a distributive context where the goals, values and interests of negotiating parties differ. A prototypical example is the negotiation between an owner and a contractor. The owner wants the lowest price possible and thus initially offers a deflated price. The contractor, on the other hand, wants the highest price possible to pay the completion of a construction project, and offers an inflated price at the beginning of a negotiation. During the negotiation, each party makes concessions towards the other's position. Eventually, either a settlement is reached or a deadlock occurs. In decision support theories, negotiation has been formulated as a sequential decision process where involved parties make concessions based on the current state, the magnitude of concessions already made, and anticipated responses of the other party(ies) [5].

It is a fact of life that deadlocks occur during negotiation. A crucial reason for this is the lack of a mediator to help the parties generate new concessions, shift goals, and clarify payoffs. However, it is generally very expensive to find a suitable person to act as the mediator, as negotiating parties often feel that the person may be biased towards the other side. Therefore, it is desirable to develop a computer system acting as the 'mediator' to provide neutral and intelligent assistance to all negotiation parties. During the process, the mediator is engaged in parallel communications with all negotiators and generates new proposals to stimulate changes when a deadlock occurs. The mediator does not possess any information at the outset; moreover, new information is obtained during the process. Typically, information from negotiating parties contains many conflicting criteria. In order to generate new proposals, the mediator therefore needs to have substantial expertise to understand the aspirations of all negotiating parties. Learning from previous negotiation cases is an effective way to acquire this expertise. A successful case represents a set of compromises for a specific negotiation situation. An unsuccessful case stores reasons for failures and indicates potential difficulties that may arise in a future similar case.

Previous research in supporting negotiation has investigated many aspects of using artificial intelligence (AI) techniques. For example, Sycara developed a computer system PERSUADER to generate settlements automatically using searching problem restructuring methods $[12, 13]$ . Several rule-based expert systems (ESs) have been developed to interpret relevant legislation and laws to assist negotiation $[1-3]$ . It has also been found that negotiation problems are complex, ill-structured, and the outcomes are not certain. Thus they need a high level of intelligent support. Jarke $[15]$ stated the importance of sharing information and knowledge in multiperson negotiation. There is also work on modelling negotiation using Group Decision Support (GDS) models $[6, 8, 10, 11]$ .

## 2. Case-based reasoning and case structure

Case-based reasoning (CBR) is a problem solving strategy which is based on reuse of past solutions to address a new problem. Instead of representing knowledge as rules in rule-based expert systems, a case-based reasoning system maintains a case base that stores cases previously solved. When a new problem is encountered, the system retrieves cases similar to the new problem from its case base, selects the most similar one, and then converts the old solution to a new one for the new problem [7]. This technique is appealing because humans often make decisions in similar ways, and many attempts have been made to address CBR as a scientific cognitive model [7].

There are two important operators in a case-based reasoning system: select and adapt. Select is the means of retrieving the most similar case from the case base according to the features of the new problem. A weighted count of matching features provides one way to select the best case; however, this does not take into account the fact that the case itself may determine the importance of a feature. Some approaches to finding the best cases are: preference heuristics [7], dimensional analysis [9], and dynamically-changing weighted evaluation function [14]. Once the best case has been selected, it is necessary to adapt the solution of the case to fit the new problem as closely as possible. In adaptation, decisions have to be made about what stays the same and what changes. The two alternatives for reusing a previous construction situation are to replay the operators that produced the solution and to reuse the construction situation itself. These are identified by Carbonell [4] as derivational analogies and transformational analogies. The second transfers the solution of an old case directly to that which satisfies the criteria of a new problem; whereas a derivational analogy modifies the problem-solving processes or techniques of an old case to construct paths that result in solutions to the new problem.

A negotiation case is an abstract of information about a previous situation. The content of each case should include information that facilitates its reuse but not necessarily all the details of the negotiation itself. Cases can be developed from a collection of previous negotiations. For our project, a negotiation case contained (1) case number and indexing keywords, (2) situational description addressing the background of the negotiation, (3) negotiating parties, (4) disputant issues and goals, (5) final settlements, if it is successful; or failures if it is unsuccessful, and (6) negotiation history. An example of a negotiation case is given in Figure 1 and Figure 2. It is necessary to note that cases used in the implementation were a simple re-construction of real negotiation situations. In particular, the negotiation history in each case was based on a rough recollection of the parties, as it

CASE201: pay-subcontracting-fringebenefits

Situational Description:
After the recession, the construction industry starts to flourish, ABC Construction has obtained several big contracts. On behalf of the employees in the company, the workers union negotiates with the company management for better working conditions and benefits.

Negotiating Parties:
The workers union
The company management

Disputant Issues and Goals:
The workers union wants
7% pay rise
no subcontracting
5% increase in fringe benefits
The company management wants
no pay rise
unlimited subcontracting
no increase in fringe benefits

The Final Settlement
3% pay rise
limited subcontracting when extra work is available.
3% increase in fringe benefits

Negotiation History
( see Figure 2 for details )

Fig. 1. A negotiation case.  
![](/api/attachments/84W46WBF/fulltext/images/03e63577560a2a2a9f7d04c6beb531788736125bc6c1e9e4102fb93e19ffaea6.jpg)  
Fig. 2. The negotiation history of Case 201.

appeared that it was difficult for the parties to recall, exactly, the negotiation history.

A case has a root node indicating its indexing number and keywords representing important issues involved in the negotiation. Figure 1 illustrates a negotiation case between the company management and the workers union in ABC Construction. On behalf of the employees, the workers union requested 7% pay rise, no subcontracting, and 5% increase in fringe benefits. The company rejected the request and insisted on no pay rise, unlimited subcontracting, and no increase in fringe benefits. A negotiation started and after three intermediate steps a final settlement was reached as: 3% pay rise, limited subcontracting when extra work is available, and 2% increase in fringe benefits. The history of the negotiation process is represented by a list of impasses that denote the difficulties encountered in the negotiation and concessions made by both parties, as shown in Figure 2. The negotiation history indicates that there were three intermediate steps during the negotiation. For each step, the participating parties undertook the following tasks: (a) evaluating proposals from the other party;

and (b) either accepting the proposal, or generating counterproposals. Therefore, the final settlement was reached through iterations of these tasks. Specifically, the negotiation was performed as follows. In the first step, after reviewing the union's position and the perspective of the coming project, the company management offered 1% pay rise, unlimited subcontracting, and 1% increase of fringe benefits as a new proposal. But the union rejected the proposal and generated a counterproposal as: 5% pay rise, no subcontracting, and 4% increase of fringe benefits. In the second step, the company made a further concession and offered 2% pay rise and limited subcontracting when extra work is available, and 2% increase of fringe benefits. Again, the union rejected the proposal and reformulated a counterproposal as: 3% pay rise, no subcontracting, and 3% increase of fringe benefits. In the third step, the company offered 3% pay rise, limited subcontracting when extra work is available, and 3% increase of fringe benefits. The union carefully considered the offer and decided to accept it. Thus, a final settlement was reached.

![](/api/attachments/84W46WBF/fulltext/images/99aec3a11c7929adb46b1644c21d33f714178461f9082cfb9ac9875f8a30ed95.jpg)  
Fig. 3. The overall architecture of MEDIATOR.

## 3. The MEDIATOR system

The MEDIATOR is a computer program developed to help negotiators reach an acceptable compromise. It was implemented using Microsoft Visual Basic and Access [16] on an IBM PC computer or its compatibles. The components and major mechanisms are illustrated in Figure 3. In using the program as an intelligent support for negotiation, the parties input their issues and goals. It is likely that the inputs of the disagreeing parties define an impasse that needs to be resolved. Based on this information, a similar negotiation situation is selected from the case base. The case is then adapted according to the new context in order to resolve the conflicts caused by the differences between the original and the new contexts. In general, a solution is derived based on (1) the most relevant previous negotiation situation being selected; and (2) adapting the potential solution to fit the new negotiation situation adaptation techniques. When the proposal generated by the procedure is presented, negotiators' reaction to the proposal can be (a) to accept the proposal; (b) to reject the proposal with modified positions in goals and issues; and (c) to reject the proposal and walk out of the negotiation. If all parties accept the proposal, then it is the final settlement. If any of the two parties rejects the proposal, the system identifies whether the disagreeing party has made concessions to his/her goals and issues. If new goals and issues are available, then the MEDIATOR system uses the goals and issues as new constraints to repair the proposal. This process continues until a final settlement or deadlock is reached.

## 3.1. Case selection

Retrieval and selection among cases entails the recognition of the relevance of each case to a new negotiation situation. The case base is indexed by the keywords of each case. When a new impasse is defined as a set of issues and goals, the system traverses the cases according to the new impasse definition, and identifies the similarities between the cases and the new impasse definition. The case with the highest similarity is then selected by the MEDIATOR as a basis for generating a new proposal. To model this selection process, a weighted count of matching keywords is applied. User interaction allows the set of matching keywords and their relative importance to be modified by the negotiators.

## 3.2. Case adaptation and proposal generation

Case adaptation in MEDIATOR forms the essence of proposal generation. As a CBR model, the system assumes that case selection provides a specific case that is close to an acceptable solution and adapts those aspects of the case that are inconsistent. The selected case should contain most issues and goals that define the negotiation problem to be resolved. Knowledge used in case adaptation includes heuristics, negotiating goals and issues, case base, and proportional relations. Modify reservation values, introduce new issues/goals, and select additional cases are three techniques of case adaptation.

## 3.2.1. Modifying reservation values

The process of modifying reservation values involves changing values of goals/issues based on the selected case. If the selected case is a successful one, then the negotiation history provides a basis for reforming the values of goals and issues in the new negotiation situation. If the selected case was unsuccessful, then the system uses it to identify and avoid potential drawbacks that may not be obvious to the parties. For example, Meralex Thiess Construction presented its employees with a warning that if they did not take a pay cut of 6% and a fringe benefits cut of 4% then the company, which was already non-competitive, would soon go bankrupt. The employees protested, negotiation between the two parties began and the MEDIATOR was ‘called in’. Searching the case base with keywords PAY and FRINGES, the system found two relevant cases, as shown in Table 1.

An additional check of feature similarity showed that Case 105 shared many disputant issues and goals with the new negotiation problem. Thus Case 105 was selected as the similar case. As shown in Figure 4, the final settlement of Case 105 was reached after three rounds of negotiations. In the first round, the company perceived that job security was a priority during the recession and made a concession of accepting 1% pay cut and 1% reduction in fringe benefits. At the same time, the company management also modified their goals by reducing the pay cut to 3% and the fringe benefits reduction to 2%.

Table 1  
A subset of the retrieved cases

<table><tr><td>Case 201: Pay-Fringes-Subcontracting</td><td>Case 105: Pay-Fringes-Jobs</td></tr><tr><td colspan="2">Negotiating parties</td></tr><tr><td>The workers union</td><td>The workers union</td></tr><tr><td>The company management</td><td>The company management</td></tr><tr><td colspan="2">Disputant issues and goals</td></tr><tr><td>The workers union wants</td><td>The company management wants</td></tr><tr><td>7% pay rise</td><td>4.5% pay cut</td></tr><tr><td>No subcontracting</td><td>2% cut of jobs</td></tr><tr><td>5% increase in fringe benefits</td><td>2.5% reduction in fringe benefits</td></tr><tr><td>The company management wants</td><td>The workers union wants</td></tr><tr><td>No pay rise</td><td>No pay cut</td></tr><tr><td>Unlimited subcontracting</td><td>No cut of jobs</td></tr><tr><td>No increase in fringe benefits</td><td>No reduction in fringe benefits</td></tr></table>

![](/api/attachments/84W46WBF/fulltext/images/f2f585f26a76d6da7a9176f953ccbc0a0162505e06aa91034de1a6e4b67d1567.jpg)  
Fig. 4. The negotiation history of Case 105.

In the second round, both sides made further concessions towards the settlement. At the end, the union agreed that 1% job cut was necessary for the company to survive through the recession and the negotiation was settled at a 1.5% pay cut, 1% job cut and 2% cut in fringe benefits.

Thus, the negotiation history in Case 105 provided a reference for modifying reservation values of parties in the negotiation problem in Meralex Thiess

Construction. Applying the transformational analogy, the MEDIATOR assumed that the negotiation between company management and workers union in the company would also go through three rounds. New proposals to both parties were formulated based on the proportions of value changes in Case 105. Specifically, in the first round, the union shifted the value of pay cut from 0 to 1% which was 22% of 4.5%. i.e. the union moved to 22% of the company's position in pay cut. So the system recommended to the union that they should move to 22% of the company's position in pay cut, i.e. $1.3\%$ . Similarly, the system conjectured changes of other values and formed proposals and recommendations to parties.

## 3.2.2. Introducing new issues/goals

If modifying reservation values does not yield successful results, the system helps by introducing new goals and issues into the negotiation. Suggesting these may accelerate the movement towards agreement and allow for creative resolution of the negotiation. For example, in the negotiation, if the company management introduced a new goal of allowing the workers representative to be on the board of directors, this might compensate the union for taking a greater pay cut.

Instead of directly providing new goals and issues, the system uses a number of heuristics to advise negotiating parties on possible avenues of generating new goals and issues. The heuristics help negotiators to identify issues that are less important and can be given away to win more important issues or goals. For example, job security was of priority to workers during the recession. In order to ensure job security, the MEDIATOR advised the union to ‘trade away’ less important issues, such as promotion, annual bonus, etc., during a negotiation with the company management.

## 3.2.3. Selecting additional cases

If both modifying reservation values and introducing new issues/goals are exhausted without success, the system searches through its case base again to select other cases. As new issues may come up and priorities may alter during the negotiation process, the system uses these new issues to retrieve additional cases. For example, the issue annual bonus can be a new keyword to traverse the cases and identify and select similar ones. The additional cases provide further information on how to formulate new proposals and open up additional ways to reach a agreement.

## 4. Conclusion

Here, we identified that negotiations are ill-structured and complex problems. We then presented the MEDIATOR as a computer model to support negotiations in construction. The model utilises casebased reasoning (CBR) to generate and modify proposals to mediate negotiating impasses. A negotiation problem is characterised by a set of issues and goals and indexed by some keywords in the case base, the system measures the similarity according to the matched keywords and their relative importance; the relative importance of issues can be adjusted by negotiators to better reflect their changing positions and goals.

The MEDIATOR uses three techniques to modify and transform a selected case in an attempt to generate new proposals: modify reservation values, introduce new issues and goals, and select additional cases. When a case is selected, values in the selected case are first adapted for generating potential proposals. If modifying values fails, new issues and goals are introduced and the selected case may derive creative solutions to the problem. The third technique is to select additional cases using updated information as the negotiation progresses. The three techniques are described and explained using negotiation situations. Although the case-based reasoning technique is not new, the combination of the three techniques is suitable for supporting construction negotiation situations.

To summarise, the MEDIATOR supports the negotiators in the following ways:

1. It helps negotiators clarify what they want by 'asking' them to describe their negotiating issues and goals.

2. It provides neutral support to all negotiators.

3. It provides an effective way for negotiators to communicate with each other.

4. It records and maintains new negotiations in its case base. This enables it to accumulate cases, and constantly update its knowledge.

5. Moreover, its proposals are 'fair' to all parties.

We experienced a number of difficulties during the implementation of MEDIATOR. The first was in collecting previous negotiation cases. Direct collection is difficult because the negotiation history is seldom recorded and documented. Hence, it is very difficult to reconstruct and conceive how negotiation results were arrived at. Another difficulty was in capturing the original context of a negotiation. In special economic and political conditions, negotiators may make concessions at any cost to win over certain issues. When reusing a negotiation case for a problem in different economic climates, it is necessary to know the context so that its adaptation can be consistent.

Further improvements are needed to be efficient in using the system to support negotiations in construction. These include extending the model by integrating CBR with other AI problem-solving methods. Further consideration should also be given to the similarity measurement between a given negotiation program and prior cases. Another limitation of the system is that, unlike human negotiators, it cannot 'recognise' the 'thrown-away' issues and goals at the start of a negotiation. Further research effort is needed to investigate the feasibility of implementing this ability. As stated earlier, many examples used in this study are simplistic and involve certain hypothetical factors, as we primarily focused on demonstrating the framework of using CBR to support negotiation problems in construction. Real-world cases are required to elaborate and extensively test the model to ensure its appropriateness.

## References

[1] AI-Shawi, A. and Hope, A.E., “Expert systems and contractual disputes: extension of time under JCT80”, Construction Management and Economics 1, 1989, 65–74.

[2] Anson, R.G. and Jelassi, M.T., “A developmental framework for computer-supported conflict resolution”, European Journal of Operational Research 46(2), 1990, 181–199.

[3] Betts, M., Robinson, N. and Santhanam, J., “Multi-purpose expert system prototype in construction law”, The Australian Institute of Building Papers 00, 1994, 57–74.

[4] Carbonell, J.G., “Derivational analogy: A theory of reconstructive problem solving and expertise acquisition”, in Michalski, Carbonell and Mitchell (eds.) Machine Learning: An Artificial Intelligence Approach, Morgan Kaufmann, Los Altos, CA, 1986, Vol 1, pp. 137–162.

[5] Herman, E. and Kuhn, A., Collective Bargaining and Labor Relations, Prentice-Hall, Englewood Cliffs, NJ, 1981.

[6] Kersten, O.E., “NEGO–group decision support system”, Information and Management 8, 1985, 237–246.

[7] Kolodner, J.L., “Retrieving events from a case memory: a parallel implementation”, Proceedings of the DARPA Workshop on Case-Based Reasoning, Morgan Kaufmann, 1988, Clearwater, FL.

[8] Randle, W., Collective Bargaining: Principles and Practices, The Riverside Press, Cambridge, MA., 1951.

[9] Rissland, E.L. and Ashley, K.D., “Credit assignment and the problem of competing factors in case-based reasoning”, Proceedings of the DARPA Workshop on Case-Based Reasoning, Morgan Kaufmann, 1988, Clearwater, FL.

[10] Shakun, M.F., Evolutionary Systems Design: Policy Making Under Complexity and Group Decision Support Systems, Hoden-Day, Oakland, CA., 1988.

[11] Shaw, M., “Mechanisms for cooperative problem solving and multi-agent learning in distributed artificial intelligent systems”, Proceedings of the 10th International Workshop on DAI, Banderra, TX., 1990.

[12] Sycara, K., “Problem restructuring in negotiation”, Management Science 37(10), 1991, 1248–1268.

[13] Sycara, K., “Machine learning for intelligent support of conflict resolution, Decision Support Systems 10, 1993, 121–136.

[14] Stanfill, C., “Memory-based reasoning applied to English pronunciation”, Proceedings of the Sixth National Conference on Artificial Intelligence, Seattle, WA., 1987.

[15] Jarke, M., “Knowledge sharing and negotiation support for multiperson decision support systems”, Decision Support Systems 2, 1986, 93–102.

[16] Microsoft. Visual Basic User's Manual. Microsoft Corporation. 1994.

![](/api/attachments/84W46WBF/fulltext/images/a9b04ca4b2494033d84f8414defc8b4e7be1da14df6db70ec86ea3845aaba451.jpg)

Heng Li is affiliated to the Caulfield School of Engineering, Monash University. He has published papers in fifteen international journals, one book, and several conference papers and reports. His reviews and editorial works include papers for AI'94 Australia, PACON'94 Proceedings: Recent Advances in Marine Science and Technology, International Journal of Informatica, and International Journal of Building Research

amd Information. He is a member of Advisory Board of International Journal of Building Research and Information.
