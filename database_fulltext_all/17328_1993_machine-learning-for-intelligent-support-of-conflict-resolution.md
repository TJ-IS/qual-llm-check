---
otero_id: 17328
otero_key: "9CXEYQTJ"
title: "Machine learning for intelligent support of conflict resolution"
authors: "Katia P. Sycara"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90034-z"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Machine learning for intelligent support of conflict resolution \*

Katia P. Sycara

Carnegie Mellon University, Pittsburgh, PA, USA

Because negotiation and conflict resolution are complex and unstructured tasks, they need sophisticated decision support. One of the crucial characteristics of such support is systems that are capable of improving their performance, both in terms of efficiency and solution quality, by employing machine learning techniques. A framework for intelligent computer-supported conflict resolution through negotiation/mediation is presented. The model integrates Artificial Intelligence methods (case-based reasoning) and decision theoretic techniques (multi-attribute utilities) to provide enhanced conflict resolution and negotiation support in group problem solving. This model has been implemented in the PER-SUADER, a computer program which operates in the domain of resolution of labor management disputes. The PER-SUADER uses case-based reasoning (CBR) to learn from its experience. In contrast to quantitative models or expert systems that solve each problem from scratch and discard the solution at the end of problem solving, CBR retains the process and results of its computational decisions so that they can be re-used to solve future related problems. CBR is a powerful learning method since it enables a system not only to exploit previous successful decisions, thus short-cutting possibly long reasoning chains, but also to profit from previous failures by using them to recognize similar failures in advance so they can be avoided in the future. As the state of the art in DSS development advances and as DSSs support increasingly more complicated tasks, such machine learning techniques will become an indispensable part of decision support systems.

Keywords: Learning; Case-based reasoning; Failure-driven learning; Learning from experience; Conflict resolution; Negotiation; Multi-agent planning; Group decision support.

## 1. Introduction

Negotiation and conflict resolution are among the major unstructured tasks that need decision support in a group decision making setting. The outcomes of the negotiation process depend on such intangibles as the negotiators' skills and experience, uncertain and changing information, the parties' perceptions and cognitive biases, and on the exhaustive and systematic analysis of the problem. Choices and actions of each agent are influenced by his/her assumptions of the choices and actions of the others. This type of decision problem is dynamic and evolves during the agent interactions. An agent does not possess all the information at the outset and new information may be obtained during the decision process. The problem is therefore complex and ill-structured and the outcomes are not certain. One consequence of these characteristics is that high level of intelligent decision support is required [1].

A second consequence is that support for improving group performance, especially in difficult unstructured tasks such as conflict resolution, is crucial $[28]$ . Such support can be provided by incorporating machine learning mechanisms in the decision support system. Learning mechanisms can help the system improve its performance by acquiring and retaining new knowledge, refining existing problem solving strategies, predicting and avoiding suggestions and problem solving paths that may lead to failure, and being able to support recovery from failures when they happen. An additional benefit of GDSSs that incorporate learning is that they can facilitate the decision makers' learning through group interactions.

![](/api/attachments/9CXEYQTJ/fulltext/images/1ff909289114572b0acff470d7335fb81b1251cac052b4b3844c282babc4de77.jpg)

Much of the recent research in machine learning is concerned with the issue of acquiring domain-specific problem solving knowledge. The body of research falls into two broad categories. One approach involves learning abstract knowledge either in the form of search control rules $[3]$ that reduce the branching factor, or in the form of chunks $[19]$ that decrease the length of solution paths. An alternate approach involves storing specific planning experiences (cases) in memory and then using them to solve related problems (case-based reasoning). Storing knowledge in terms of specific experiences allows a learner to avoid spurious generalizations and the pitfalls of learnability $[35,9]$ .

Case-based reasoning is attractive as a learning methodology for the following reasons:

\- it allows incremental learning with no restriction on the order of presented cases;

\- it provides shortcuts to problem solving;

\- it helps focus the attention of a reasoner (or group of reasoners) to useful parts of the problems;

\- it supports the disambiguation of input information;

\- it provides advice to avoid previous failures;

\- it provides advice to anticipate failures that are similar to ones encountered in the past;

\- it provides support for recovery from current problem solving failures.

In this paper, we present a framework for intelligent computer-supported conflict resolution through negotiation/mediation. The presented model integrates artificial intelligence and decision theoretic techniques to provide enhanced conflict resolution and negotiation support in group problem solving settings. This model has been implemented in the PERSUADER, a computer program which operates in the domain of resolution of labor management disputes. The PERSUADER, acting as a mediator, facilitates the disputants' problem solving so that a mutually agreed upon settlement can be achieved. The PERSUADER embodies a general negotiation model that handles multi-agent, multi-issue, single or repeated encounters based on an integration of case-based reasoning and multi-attribute utility theory [30]. The integration of heuristic and analytic methods makes the PERSUADER both robust and flexible. It does not break down when heuristic methods fail. In addition, it has the flexibility to use whichever method is more natural to a particular problem solving stage that it is engaged in.

The system's user interface allows communication of information to the decision makers and accepts their feedback. One of the unique features of the system is its learning capability. The learning mechanism is case-based reasoning (CBR). Case-based reasoning uses knowledge from previous decision making sessions on the same subject (cases) to propose solutions to a new case (the current decision making situation). At the end of each problem-solving session, the case memory is updated with a new case that incorporates important features of the decision making session. Successful as well as failed episodes are retained. Knowledge from successful episodes can be re-used in subsequent sessions; knowledge from failed episodes can warn of potential future failures. Thus learning is an integral part of the decision support process.

Besides CBR, the model integrates the use of multi-attribute utility theory in its problem solving. Multi-attribute utilities are used to rank various compromises. The PERSUADER obtains the importance (coefficient) that a party assigns to an issue by asking the parties. It obtains the utility functions for each issue for each party by accessing utility functions of previous similar parties. The overall utility of a compromise for each party is computed by taking the linear combination of the party's utilities for that compromise. To rank compromises from the point of view of mutual satisfaction of the parties, equity is combined with maximal gain to form the optimization criterion.

The model incorporates an ontology of goals and characteristics of conflict resolution through negotiation. The model is able to generate initial proposals, generate counterproposals that narrow the agents' differences, take into consideration changing circumstances, reason about other agents' beliefs and generate justifications and arguments in support of or against decisions. The conflict resolution model we present parallels real-world negotiations. It has been developed using the help of two practicing federal mediators, one, a professor of economics and the other, a mediator who came up through the ranks of the machinists' union.

Although the PERSUADER has been implemented in the labor domain, the problem solving strategies employed are domain independent and are ideally suited for conflict resolution in group decision making.

Section 2 discusses the role of conflict resolution and negotiation in the larger context of group decision making. Section 3 outlines the requirements for enhanced decision support that negotiation entails. Section 4 presents an overview of case-based reasoning with emphasis on the types of learning that CBR supports and presents the PERSUADER's case memory organization and indexing. Section 5 presents the PERSUADER's mechanisms for learning from success and failure. Section 6 gives a brief description of the integration of multi-attribute utilities in the PERSUADER. Sections 7 and 8 present discussion and summary.

## 2. Negotiation as part of group decision making

Most GDSSs implemented to date serve as a communication blackboard on which ideas can be generated, information can be shared and consensus may be reached by using group techniques such as voting and preference ranking $[20]$ . This type of system can provide valuable support to group decision making. However, in some situations, a higher level of support is needed especially when there are conflicts to be resolved $[4,20,13]$ . For example, when accounting, production and marketing managers fail to reach agreement on the forecast sales for next year, it is usually not a matter of voting or preference ranking. Nor will a multi-attribute decision model or game-theoretic approach by themselves be appropriate for resolving conflict.

Quantitative models are frequently used in individual DSS to deal with the well-structured portion of a decision process. The unstructured portion is handled by the decision maker who defines the goal and makes the final decision. In group processes, however, a group of decision makers needs to reach agreement since each of them may have incomplete information, different goals and different perspectives on the problem. Hence many political issues may surface and decision support needs to be expanded to incorporate some unstructured tasks in the process. This requirement necessitates that additional functions not provided by individual DSS must be supported, such as communication and information sharing.

During the decision processes illustrated by the sales forecasting example, the agents not only use quantitative and qualitative models to facilitate their analyses but also must convince other group members that the results generated by their models are of value. The accounting and production managers may question the forecasted sales estimated by the marketing department. The marketing manager may want to know how the production process is scheduled and what criteria are used in the capital budgeting process. Thus a higher level of support is needed in the form of generating arguments and justifications that group members can convey to each other. This functionality requires that the GDSS must incorporate not only intelligent management of quantitative models but also must integrate knowledge based models $[2]$ to facilitate the explicit examination and manipulation of relations that are implicit in the quantitative formalisms, to allow the communication of the agents' goals, assumptions, evaluation criteria, justifications and organizational context.

Thus, support is needed both in facilitating the development of models (both quantitative and knowledge-based) and in enabling access, execution, and sharing of such information. The information shared could be numeric, textual, and relational and is used to reduce disagreement caused by incomplete information and conflicting objectives. Models (both quantitative and qualitative) can be executed and the input and output information can be disseminated to interested members. In the production example, it would be useful for the system to provide additional capabilities in the form of functions that not only allow the managers to examine what models were used to generate their sales figures, what assumptions were behind these models, and how these models were evaluated, but also allow the managers to communicate to each other their conclusions, questions, arguments and justifications concerning the models and other aspects of the task.

In group problem solving, there are many sources of conflict: Differences in assumptions about the problem the group faces, conflicting evaluation criteria, differences in which issues to focus on and the order of processing of the issues, and competition over the use of limited resources required by group members to solve their parts of the problem. Conflicts may arise even if the group members try to coordinate their activities due to the incomplete and distributed nature of the information each agent has and due to heterogeneous expertise and cognitive biases.

In the forecasted sales example, the disagreement may result from differences in assumptions, conflicting evaluation criteria, or in the selection of models. The disagreement over sales figures might have occurred in the context of the managers' working together to develop a strategic business plan based on the anticipated demand and available resources. The marketing manager may use product pricing, sales forecasting and market segmentation models. From the accounting perspective, however, pricing decisions may need to also consider costs. To production managers, the cost allocation and capital budgeting information must be integrated into capacity planning, production scheduling and inventory. It is obvious that in this process, different parties, representing different interests and corporate subcultures, having different factual information and value judgment, and using different decision procedures, need to communicate and negotiate to reach agreement.

Traditionally, negotiation has been considered in a distributive context where the goals, values and interests of the parties are in conflict. The prototypical example of distributive bargaining is that of a car buyer and a car seller [1]. The buyer wants the lowest price possible and thus initially, s/he offers a deflated price. The seller, on the other hand, wants the highest price possible so offers an inflated price. During the negotiations, each party makes concessions towards the others position (the “negotiation dance”, as has been called by Raiffa [24]). Eventually, either a compromise in the middle is reached, or deadlock occurs. The fundamental assumption of distributive bargaining is that the parties want to maximize their own goals without any concern for the other.

However, there are many situations, where integrative types of negotiation occur. In integrative negotiation, the parties engage in a group problem solving process characterized by increased cooperativeness and consensus seeking through increased information sharing, consideration of tradeoffs, adaptation and problem restructuring [27]. In the car buyer-seller example, price may very well be the most important consideration for each party. However, other factors, such as financing, trade-in and delivery time may also have an impact. After a variety of alternatives have been generated that take into consideration the trade-offs among these factors, the parties evaluate the available options and select one that fulfills their joint interests. Organizational decision making where the various departments have common high level goals in terms of the particular tasks they are engaged in but conflicts also frequently arise, is another example of this process. It exemplifies situations which, albeit not strictly competitive, admit subgoal conflicts that could benefit from negotiation.

Computer-supported conflict resolution through negotiation can be beneficial for group decision making, especially in dealing with some of the difficult socio-economic and cognitive issues that are present [1]. Computer-support could: (a) help maintain rationality in decision making by avoiding emotional clouding of issues, (b) help allay privacy concerns, since the participants may wish to disclose only parts of their reasoning and utilities depending on the trust they share with other participants; (c) enforce fairness in the decision making by precluding domination of the discussion by a single party; (d) speed the decision making process by enabling rapid generation of proposed agreements of joint benefits to the parties; and (e) provide the means for recognition and resolution of disparities in goals and viewpoints.

To support negotiation, a number of negotiation support systems (NSS) have been developed [1]. Unfortunately, existing negotiation support systems focus solely on the analytical negotiation activities (the structured part of the decision problem) and give minimal or no support to the interactions among negotiators.

For a system to provide truly intelligent support, it must learn, i.e., improve its performance as experiences in group sessions are accumulated. This argues for incorporation of mechanisms to capture and retain knowledge of group sessions so it can be reused in subsequent sessions and capture knowledge from different groups so it can help guide decision making of a particular group. These capabilities can be summed under the rubric of learning from experience. Case-based reasoning is an AI problem solving paradigm that enables a system to exploit its experiences and automatically incorporate new experiences in its case memory.

A system that maintains a memory of past problem solving experiences (successes and failures) can facilitate group problem solving since:

\- the memory can be used to access reasonable proposals and arguments in situations similar to the current one;

\- the memory can be used to make inferences about the preferences of group members, thus avoiding bad proposals and minimizing the need for information exchange;

\- if the repair of a past failure is also stored in memory, when a similar situation arises, the repair can be accessed and re-used.

## 3. Intelligent NSS requirements

Negotiation is a process where the parties iteratively propose compromises and argue with each other till a settlement is reached. A compromise solution is a ‘package’ whose parts are strongly interconnected and interacting. Moreover, negotiations take place in a changing environment. These characteristics impose the following requirements on any computer model to provide intelligent decision support for conflict resolution through negotiation:

\- Multi-agent negotiation with multiple conflicting goals is a lengthy and iterative process. A computer model should support the negotiation process by being able to incrementally propose modifications to a proposal to help the parties narrow their divergent views.

\- After each round of proposals the participants give feedback (communicate) to a mediator or each other about which parts of a proposal they agree or disagree on. Hence an NSS must be able to incorporate new information and feedback about the quality of its proposals, evaluate it, and use it to base its suggestions for proposal modifications to the parties.

\- Since final agreement is reached through narrowing the difference in the demands of the negotiating agents, a system for negotiation support must have a way of predicting/evaluating whether each new proposal indeed narrows these differences.

\- Reaching a compromise through negotiation entails that the parties must be able to communicate to each other arguments and justifications of their positions as well as supporting information. A NSS can help the parties communicate these justifications and arguments and also suggest to them suitable arguments.

The PERSUADER incorporates all the above characteristics. In a decision support setting, the PERSUADER is ideal for supporting a mediator. Use of mediation has proven its worth in real-world negotiations, and has been hailed $[17]$ as an invaluable tool in difficult computer-supported conflict resolution. The main advantages are the provision of needed structure and deflation of charged emotional atmosphere.

The PERSUADER can support the negotiation process by assisting with process structuring, communication, and analysis. Instead of being a passive ‘back room’ analytical processor, it plays an active role since its implementation as a knowledge-based system, its CBR mechanisms and use of utility calculations enable it to analyze conflict contingencies, to suggest appropriate process structuring formats, to monitor the semantic content of electronic communications of arguments and justifications, to suggest suitable arguments and to suggest high joint-benefit agreements taking into consideration desirable tradeoffs of the parties.

The PERSUADER's input is the set of conflicting goals of the parties and the dispute context. The final output is either an agreed upon settlement or an indication of failure if the parties did not reach agreement within the decision making deadline. The final output is reached through iterations of the following tasks: (a) generate proposals; (b) generate arguments and justifications in favor of a proposal; (c) generate arguments to convince a party to accept a rejected proposal; and (d) generate counterproposals. These tasks are performed using knowledge of past negotiations and settlements (cases), knowledge of the domain, and common sense knowledge.

In using the PERSUADER as an intelligent NSS each user inputs his/her own utilities associated with the issues. Based on this knowledge, the PERSUADER generates a compromise proposal and presents it to the participants. The participants evaluate the proposal from their own perspectives and communicate their reactions either publicly (with or without attribution) or privately to the system.

A participant's reaction to a proposal could be:

\- accept the proposal;

\- reject the proposal (with or without giving a reason);

\- formulate and communicate a counterproposal.

If all parties accept a proposal, then it is the final compromise. If one of the parties simply rejects it, the system makes a decision whether to modify the proposal or attempt to change the disagreeing party's mind. If a counterproposal is received, there is a choice as to whether to accept the counterproposal, whether to try to persuade the rejecting party to agree to the initial proposal, or whether to use the initial or the rejecting party's proposal as a basis for formulating another counterproposal.

The participants exchange messages containing the following information:

• the proposed compromise;

• persuasive arguments;

\- agreement or disagreement with the compromise or argument;

\- requests for additional information, e.g., which issue in the proposed compromise an agent disagrees with;

\- reason for disagreements;

\- utilities of the agents associated with disagreed upon issues.

The last two pieces of information are optional, since, in a not fully-cooperative situation, the agents might not want to reveal their utilities or reasons. The case memory of negotiating experiences with the same or similar parties and similar issues can be used to infer the missing information.

## 4. Reasoning from past cases

The central idea of case-based reasoning (CBR) is that reasoning is done by remembering rather than reasoning from “first principles”. Given a new problem solving situation, an appropriate previous case is retrieved from memory, and differences between the previous and current case are identified. These differences are then used to criticize and modify the previous solution to fit the current case. In contrast to quantitative models or expert systems that build solutions from scratch and discard them at the end of problem solving, in CBR the solution and solution context are integrated into the case memory so that they can be re-used. Thus, learning is central to CBR. A case-based reasoner learns new solution strategies during problem solving. It learns to predict failures so it can avoid them in the future. It learns repairs so that it can apply them if similar problems occur or can be predicted. As the case memory is enriched with new experiences, a case-based reasoner can refine its problem solving strategies and improve its performance. In practical terms, CBR alleviates the knowledge acquisition bottleneck that plagues expert systems since new cases are acquired as a by product of problem solving.

Sequences of decisions that have been used with success in the past are stored in memory in the form of cases, so they can be accessed and used in the future for similar decision making. This is one dimension of case-based learning, learning from success.

There is a second dimension learning from failure. Learning from failure takes two forms: Learning to avoid future similar failures, and learning to recover from failures. Failures, the failure reason and dependencies among decisions taken at different times during decision making are also stored in the case memory so that they can be used to predict and avoid future failures. If features in the past situation that gave rise to a failed solution are also present in the current situation, then the failed solution should not be tried. Thus, previous failures help the problem solver avoid repeating past mistakes. Sometimes, upon discovery of a failure, an appropriate repair can be found. The repair is stored along with the associated failure. Repair of a failure is available either when a similar failure case is available, or via direct user feedback. The repair can be applied to recover from similar future failures.

The process of case-based reasoning consists of the following steps:

\- retrieve appropriate precedent cases from memory;

\- select the most appropriate case(s) from those retrieved;

\- construct a baseline solution;

\- evaluate the baseline solution for applicability to the current case;

\- modify the baseline solution appropriately to get a candidate solution (that is proposed to the parties).

A baseline solution is the best that can be constructed taking into consideration only the most important features of the current case. After constructing a baseline resolution, more detailed inference is performed to adapt it to the specifics of the current situation. This is done both through case-based reasoning and employment of heuristics. The method of successive refinement in constructing a solution (first construct a baseline solution, then customize it) is used for efficiency in memory retrieval.

## 4.1. The case memory

Case-based reasoning uses a memory of past decisions as guides to present decision making. Cases are organized hierarchically in memory around important concepts in the problem domain. In order to perform CBR, cases need to be retrieved in terms of conceptual similarity. The basic idea behind conceptual similarity between two concepts is that they share salient attributes. Salient attributes are the ones that allow a reasoner to make inferences that will be useful for the problem solving task at hand. For example, two airline companies are similar because they have the same product (air transportation of passengers), they both employ people in the same job classifications (e.g., pilots, flight engineers, flight attendants), and they are both governed by the same laws and regulations. The two airlines may also differ along other attributes, such as organizational charts, names, personnel and routes. Though these differences may be more numerous than the similarities, they are not salient and so they are not considered in the structuring of the case memory.

The high-level knowledge structure that is used to organize similar concepts in memory is called a generalized episode $[18]$ . Generalized episodes organize concepts into a hierarchical discrimination network whose nodes are either another generalized episode or an individual case. Generalized episodes have two components: (1) the norms of the generalized episode which is the collection of features that represent the abstracted content of all the cases organized under this generalized episode; and (2) the indices which connect the generalized episode with the tree of other generalized episodes and cases organized below it. Cases are indexed in generalized episodes according to the features that differentiate them from the norm. As additional cases are added to memory, the generalized information contained in the norm part of an existing generalized episode is refined and additional indices for cases are created. In this way, saliency is learned and incorporated into the memory organization.

In the PERSUADER, a case describes, not only attributes of the participants, the resolution and the context of the conflict, but also the process by which agreement (or failure to reach agreement) is reached. In particular, the information present in a case includes important attributes of the negotiating parties, the issues under negotiation, higher level goals of the parties, the context in which the negotiations take place, the process through which agreement is reached, the arguments presented during negotiations, the proposals, counterproposals and the final agreement. Each one of the above components can be accessed either through the case to which it belongs, or independently through a different set of indices. In labor negotiations, important attributes of the parties include the industry to which a company belongs, the company's geographical location, the company's position in its industry, the company's financial situation, the international union of which the local union is a member, the type of company (multi- versus single-plant), the structure of the bargaining unit (job classification, proportions of skilled, semi-skilled and unskilled workers, the age and experience breakdown of the union members). The main issues in labor negotiations are wages, fringe benefits, seniority, subcontracting, job security, training, work rules, work hours, holidays, and vacations. The context in which labor negotiations take place includes information about the economy in general, statistics about the industry to which the company belongs, domestic and foreign competition, the history of the relations between the local union and the company management.

Of particular interest is the indexing structure of contracts, arguments, and impasses. Contracts are predominantly used in construction of an initial proposal, previous arguments are used in the argumentation task and previous impasses are used during repair of a rejected settlement. Because the features that are used for retrieval are different in each task that the PERSUADER performs, the previous experiences that it reasons from are potentially different for each task. However, the case-based reasoning process behaves in the same way.

In the PERSUADER's memory, contracts are indexed by a multiplicity of features including the industry to which the company belongs, the geographical location, several features descriptive of the economic and political environment in which the negotiations take place, features descriptive of the financial situation of the industry and the company, features describing the composition of the bargaining unit, and the international union to which the local belongs.

As the system gains experience, it becomes familiar (initially through user input) with appropriate arguments and justifications. In the PERSUADER project, we incorporated into the system an initial set of arguments appropriate to collective bargaining from the pertinent literature (e.g. [10,25]). In the PERSUADER's memory, an argument is stored according to the contract issue to which it pertains, whether it is meant to convince the union or the company, and which argumentation goal and strategy it fulfills. Argumentation goals (e.g., “change the importance that the persuadee attaches to an issue”) are associated with the ways that a persuadee's beliefs can be affected by an argument. Argumentation strategies (e.g., “indicate possible unpleasant consequences of a persuadee’s demand”) are used to achieve the argumentation goals. These are the features that serve as indices during memory retrieval.

Additional information associated with the argument is a list of goals to which the issue contributes. Moreover, information about the effectiveness of the argument depending on various characteristics of the parties and external conditions is included. For example, the argument “Seniority reduces labor turnover, resulting in more efficient plant operation” is stored under seniority, it is meant to convince the company, it is meant to increase seniority’s importance. The company higher level goals to which seniority contributes are decrease in labor turnover, increase in plant efficiency and decrease in production cost. The argument appeals to the company’s self-interest. The argument is more effective during recession and for companies in labor intensive industries.

The negotiation process is represented by a sequence of temporally ordered impasses. In the PERSUADER, each impasse records the proposed settlement, the rejected issue or issues in the proposal, the feedback of each party (acceptance or rejection), the rejection reason (if one was given), the payoff of the rejected proposal from the point of view of the rejecting party, the repair method (argumentation or generation of a counterproposal), the particular repair that was used, and whether the repair was successful or not. If the repair was unsuccessful the reason for repair failure is also recorded. Impasses are indexed by the contract issues to which they pertain, by the cause (if known) of rejecting the proposal and by the rejecting party. Impasses can also be accessed through the negotiation to which they belong. Furthermore, impasses are classified as “successful” and “unsuccessful”. The success or failure of an impasse is with respect to the application of a repair strategy and repair heuristic. Thus, by having access to previous negotiation cases and the negotiation process for each case, the PERSUADER has available information to keep track of the historic context and process of negotiations as well as the various repair strategies, repairs and repair results that were used under various circumstances.

When memory is updated at the end of a problem solving episode, two issues must be addressed. Some similarities between cases may be purely coincidental, thus leading to bad generalizations. They must be found and deleted. Second, new cases must be monitored to see if additional generalized information can be extracted from them. To address these two issues, at update time each new case is checked to see if it conforms to the norms of the appropriate generalized episode. If a feature of a new case conforms to a generalization, the certainty of that norm feature will increase. On the other hand, the certainty of a norm feature that has a conflicting value in a new case will decrease. When the certainty reaches a particular threshold, it can be considered a real generalization. Correspondingly, if the certainty reaches a low threshold, that feature need no longer be considered active for generalization-forming comparisons. For more details on the principles of memory organization, see [18]. For more details of the memory organization of the PERSUADER, see [30].

## 4.2. Similarity determination

CBR relies on similarity-based retrieval of cases. Since a concept is characterized by many salient features, some of which are the same and some different for two concepts, during case retrieval partial matches between concepts result. It is therefore necessary to be able to evaluate the degree of similarity of these partial matches.

Each of the important domain features (e.g., industry, geographical location, job classification of union members) constitutes a similarity criterion. For each similarity criterion a similarity hierarchy is constructed on which retrieval of appropriate precedents is based. The nodes at each level of this hierarchy represent concepts that are generalizations of their children nodes. A similarity class can be defined at each level of the hierarchy and consists of the collection of siblings at that level. The members of a similarity class at a particular level exhibit a greater degree of similarity than members of two distinct similarity classes of that level. The nodes in the hierarchy also indicate the amount of information that is known about an entity. The closer a node is to a leaf node, the more the information available. The members of a similarity class at the leaf level are the “most similar” since: (a) they are similar (by belonging to the same similarity class); and (b) they contain the most specific information available in the domain model.

In complex domains, each concept belongs to many semantic hierarchies, each of which is formed by a salient feature and its specializations. For example, a company belongs to the hierarchy defined by the “industry” dimension. Since a company has some geographical location, it also belongs to the semantic hierarchy defined by the “geographic location” dimension. To evaluate degrees of similarity, the PERSUADER uses an algorithm that takes into consideration both the importance of a dimension and the location of the concept along a similarity hierarchy. The algorithm is as follows:

(1) consider the most important problem dimension;

(2) use as precedents the cases that are siblings of the current case along the most important problem dimension. Out of those prefer the ones that are most recent. Go to step 4;

(3) if step 2 returns the empty set, then use as precedents in a preorder traversal the cases that are ancestors of the current case along the most important problem dimension according to the following scheme:

(a) prefer the closest ancestors to the current case,

(b) use more remote ancestors (up to six levels) up the hierarchy only if there are no closer ones;

(4) LOOP for problem dimensions taking values from 2 to n, out of the cases returned select the ones that would be siblings of the current case along the ith most important problem dimension;

(5) if step 4 returns more than one cases, select the first one from the list as most appropriate;

The user can input the priorities of the problem dimensions so that the system can take them into consideration for determining case similarity. This is one place in the system where the preferences of the users are taken into consideration in the processing.

In addition to the similarity determination based on the above algorithm, the system incorporates a set of selection preferences, such as “prefer more recently encountered cases to older ones”. This heuristic is consistent with the assumption that the system improves its problem solving as it acquires more cases.

## 5. Generating a potential agreement

Generation of a potential agreement involves lessons learned both from successes and from failures. Successful previous agreements of similar parties in similar decision making situations are retrieved from memory and adapted to the current situation to direct problem solving. Arguments in favor of particular resolutions for particular issues also are generated through retrieval of similar previous arguments, and can be presented to the parties.

Learning from failure is useful in two stages of problem solving. The first stage is an internal evaluation phase where before proposing a potential agreement, the system tries to anticipate and avoid potential drawbacks that may not be obvious to the parties. The system uses the failures in its case memory to help identify, evaluate and fix problems. The second stage is when the potential agreement has been proposed to the parties (for example, it has appeared on a public screen in the decision room) and the parties register their comments and objections to it. If one or more parties disagree with the suggestions for all or a subset of the issues under discussion, these objections are used as indices into the case memory to access previous situations where the same or similar objections had been raised to similar proposed resolutions. The repairs that were used in those previous cases help the system (and the parties) recover from the failure by changing the proposed agreement in a way that improves its acceptability. The rejected issues can also be used as indices to retrieve arguments to try to change a party's evaluation of the proposed settlement. This is a different type of failure recovery, where, instead of repairing the solution, the system seeks to effect a 'repair' (a change of opinion) of a party. For more details on argumentation, see [32].

In the next two subsections we present in more detail the processes used to profit from success and failure in conflict resolution.

## 5.1. Profiting from success

After the selection of the most similar precedent conflict resolution situation, knowledge is extracted from its solution part (the contract) and adjusted through standard adjustments to form an initial base line solution. This solution is modified further taking into consideration important particulars of the current problem. There are three categories of knowledge that the PER-SUADER takes into consideration when criticizing a baseline solution:

\- knowledge of unacceptability conditions;

\- more detailed knowledge of the situation of the parties;

\- knowledge of the context of the conflict.

During evaluation, computer procedures called critics are activated. These critics are prioritized and considered in order of importance. A critic is most important if failure to apply it would result with greater probability in rejection of the suggestion. For example, a check is always made to see whether the company will be able to afford the ballpark economic package. This check is important since, if a company cannot afford the economic package, it most probably will reject the proposed settlement. If it is found that the company can afford the economic package, then critics associated with possible states of the company finances are applied. Such financial considerations include whether the company has suffered losses in the recent past, and whether the company has traditionally paid above, below, or industry average. A set of critics associated with the context of the conflict is then applied. In labor mediation context knowledge is almost entirely economic. Such knowledge includes considerations for the whole economy (recession, inflation etc), economic conditions of the industry to which the disputant company belongs, economic conditions of the geographical location of the company, and labor supply in the area.

If the application of a critic suggests that the contemplated resolution needs further modification, salient features associated with the critics are used to search memory to access suitable cases that can guide modification.

The same procedure is used for case-based argument generation. Using as indices the issue under discussion and the rejecting party's objections, arguments are retrieved from memory and the best is selected and possibly adapted to fit the current situation. Heuristics associated with the issue are used to that effect. For example, associated with seniority is knowledge that seniority reduces grievances, reduces labor turnover, reduces labor costs. If a previously used argument involves use of seniority to reduce labor turnover, but the current company does not have reduction of labor turnover as an important goal, then grievances is checked for applicability. If reduction of grievances is an important company goal, the previous argument is modified by substituting grievances for turnover.

## 5.2. Profiting from failure

## 5.2.1. Failure anticipation

Before proposing an adapted compromise to the agents, the PERSUADER tries to anticipate potential difficulties with the contemplated suggestion, so that it can avoid them. The knowledge that a solution has failed in the past can suggest to the system the potential for failure if the solution is adopted in the current situation. Failure anticipation is done through intentional reminding [26] of failed cases where the conjunction of salient features (say, feature-set-K) of the current contemplated solution, solution-1, are used as indices to retrieve failures that have the same feature-set-K as solution-1.

If an associated repair is stored along with a failure, case-1, that has been retrieved using the feature-set-K, the system applies the repair to get a modified solution, solution-2, that avoids the difficulty. If the parties accept solution-2, it is stored in memory as a successful case.

Next time a similar situation is encountered, the system retrieves the already repaired solution, solution-2. The “recency preference” selection heuristic ensures that case-1 will not be retrieved this time. The intentional reminding will not return any previous failures (at least not for the feature-set-K) so the process of accessing the repair, evaluating for applicability to the current case and applying it is short-circuited. As a consequence, both the failure has been avoided and system performance has been improved.

## 5.2.2. Failure recovery

When a proposal has been rejected and needs to be improved, the PERSUADER ascertains from the rejecting agent's feedback the objectionable goals, the reason for the rejection and the importance the agent attaches to the goals. Each objectionable goal/issue and reason are used as probes to select impasses with the same stated impasse goal and impasse cause as in the present failure. In other words, CBR is employed in the space of impasses.

The retrieval process may return impasses that were either successfully or unsuccessfully resolved. The successful ones are examined first for applicability to the current situation. The successfully resolved impasse whose features match most closely the current situation is chosen first and the supplied repair is evaluated using the improvement criterion described in the next paragraph. If the test succeeds, the repair gets proposed to the parties. The results of applying the repair and the parties' feedback are recorded along with the current impasse, and negotiation continues. The set of impasses considered may change at each iteration since the indices via which impasses are accessed namely, reason for rejection, the rejecting party, and set of issues may vary. Thus at each iteration, new repairs are potentially available to the problem solver. If no successfully resolved impasses become available, impasses that were unsuccessfully resolved are considered. An impasse may not have been successfully resolved in the past but features of the impasse might be different in the current situation. In the case of unsuccessfully resolved impasses, the failure reason (if one is available) is also recorded. This affords the problem solver a limited lookeahead of one iteration when the failed impasse is under consideration.

In multivariate decision making, there are many ways a potential solution could be modified/ repaired. A problem solver seeks not only a plausible repair but one that with some confidence improves the rejected solution. Without an ability to predict which repair has a chance of being accepted, the reasoner could propose repairs that do not converge to a mutually acceptable compromise. To avoid this difficulty, the PERSUADER proceeds as follows. After a repair is applied, the resulting solution is evaluated using the parties' satisfaction with the solution. An agent's satisfaction with a contract, called his payoff, is calculated using a method based on multi-attribute utility theory. For details of this, see [30,31]. The criterion of solution improvement that the PERSUADER uses is whether the contemplated repair increases the rejecting agent's satisfaction more than it might decrease the satisfaction of the agent(s) (who have agreed to the solution).

## 5.3. An example

Consider, for example, the PERSUADER trying to find a compromise for Muriel's Apparel Inc., a company that makes women's dresses and its union. The union wants 13% increase in piece rates, 7% increase in pensions, and no subcontracting. The company wants no increase in piece rates, no pension increase, and unlimited subcontracting. The PERSUADER searches memory to ascertain prevailing practice. The best contracts to reason from are contracts of competitors. Out of the competitors' contracts that it retrieves, the PERSUADER selects the recently negotiated contract of the Elegant Girl Inc. company using as additional selection criteria the company's locational similarity to the location of Muriel's Apparel Inc. (Elegant Girl is located in Florida and Muriel's Apparel in Georgia (both Southeastern States)), job classifications of the employees and political history of the dispute. In both cases, the relations of the union and management have been amicable, strikes have been a rare occurrence, the company managements have been in position for a long period and are respected by the rank and file. The relations of the locals in the two cases with the international union are good. The fact that the Elegant Girl Inc. contract is current, ensures that the economic climate of the two disputes is similar (the program checks for abrupt economic changes). The Elegant Girl Inc. contract provided 11% increase in piece rates, 5% pension increase and unlimited subcontracting.

The PERSUADER considers appropriate adjustments to the Elegant Girl Inc. contract. Precedent adjustment is done using known heuristic modifications in labor mediation, namely adjustments with respect to the competitors' position in industry, and area wage differentials between Florida and Georgia. These adjustments result in a baseline solution with 9% increase in piece rates, 4% increase in pensions and limited subcontracting only when extra work is available.

The PERSUADER now adapts the baseline solution to the current situation. Checking the financial situation of the company, it finds out that Muriel's Apparel Inc. has suffered 4% losses in the past three years. It searches memory for similar cases, selects the most similar and applies the heuristic used in that case.

Searching memory with index GARMENT-INDUSTRY,
CONTINUOUS-LOSS...
3 cases found
Select case2
based on similarity of features
Apply heuristic used in this case
Decrease increases in piece rates by half percentage
of losses
Increase in piece rates becomes 7%

Before proposing the updated solution, the PERSUADER searches memory to discover potential problems with the contemplated subcontracting language (with indices “failure”, “subcontracting language, “limited to extra work”). It retrieves a case where the union had filed a grievance protesting that the company, having extra work, resorted to subcontracting for long periods of time instead of hiring more workers. The arbitrator in that case did not vindicate the union because no time limitation was written in the contract but proposed that the union get a time limitation for its next contract.

Searching memory with index FAILURE, SUBCONT-LANG,

LIMITED-EXTRA-WORK...

1 case found

Apply repair used in this case

Put time limit in subcontract language

The PERSUADER modifies the subcontracting language to impose a time limit to the company's right to subcontract, and proposes the resulting initial compromise to the parties. The company accepts the proposal but the union refuses it saying the increase in piece rates is too low.

In the Muriel's Apparel Inc. case, confronted with the union's refusal to accept an increase in piece rates less than 7%, the PERSUADER tries to boost pensions in the hope that the union will accept the new “package”. It searches memory for impasses where pensions needed to be increased. The most suitable impasse from the ones retrieved is selected and the associated modification is tried. The modified compromise is evaluated according to the criterion for improvement stated above and, if the criterion holds, the new compromise is proposed. If the contemplated modification does not constitute an improvement, modifications from other retrieved cases are tried.

Searching memory with index FAILURE, PENSION, TOO-LOW
5 impasses found
Select impasse1
since it is same industry, same job classification,
same area...
Looking at modification1 “increase pension by additional 2%”
from impasse1
Since the majority of workers are older modification1 seems applicable
Apply improvement criterion
Success
Contract3 which resulted from applying modification1 will be proposed

The new proposed agreement is accepted by both parties and is stored as a successful case in memory. Notice that next time a case similar to Muriel Apparel is encountered, Muriel Apparel rather than Elegant Girl Inc. will be selected as a basis for reasoning (since the case selection process prefers most recently encountered cases). Reasoning from Muriel Apparel will avoid the flawed subcontracting language and use the repaired language. In addition, Muriel Apparel already incorporates the trade-off of the company's having incurred losses and thus being unable to give large increases in piece rates but can give higher increases in pensions. Thus, the performance of the system has been improved and the decision process has been shortened.

## 6. Use of multi-attribute utilities

When no available cases can be used to guide conflict resolution, the PERSUADER uses preference analysis $[31]$ to find suitable compromises. Preference analysis is based on mutli-attribute utility theory $[15]$ . The utilities of each agent with respect to the issues under negotiation are used to rank possible compromises. An agent uses his combined utilities, his so-called payoff, to evaluate a proposed compromise.

The agents' utilities portray the tradeoffs they are willing to make regarding values of the many negotiation issues to arrive at an acceptable compromise. Knowing an agent's utilities helps the model predict which compromise(s) the agent will be most willing to accept. Thus, in constructing a proposal (a counterproposal), a negotiator/mediator can incorporate the utility knowledge to arrive at compromises that will not be very objectionable to other participant(s). In addition, if a proposal has been rejected, knowledge of the rejecting participant's utilities guides the construction of suitable counterproposals (ones that increase the rejecting party's payoff).

It has been experimentally found that human negotiators very often use equity rather than Pareto optimality to arrive at agreement (e.g., [16,22]). Presented with two compromises that differ only in the increased performance level of only one decision maker, negotiators do not consider the second compromise better than the first (as Pareto optimality would predict, since group utility is considered an increasing function of individual utilities). If only one negotiator improves his position, the others perceive their position as worsened. The optimization criterion used by the PERSUADER maximizes the joint payoff of the agents and minimizes the payoff difference. This criterion balances maximal gains and equity.

## 7. Discussion

Computerized systems designated as “decision support systems” run the gamut from simple programs such as spreadsheets which aggregate and display data, to sophisticated artificially intelligent systems, such as the PERSUADER which do much more. The common theme uniting these systems is enhancing the quality or effectiveness of human decision making. While individual decision support systems concentrate on compensating for biases typical of human decision making $[14,5]$ , group decision support systems (GDSS) must also facilitate social and organizational processes. Although implemented as a mediator for resolving labor management disputes, the strategies employed by the PERSUADER are ideally suited for conflict resolution and promoting consensual decisions within groups.

DeSanctis and Gallupe [4] define the goals of GDSS as: “improving the process of group decision making by removing common communication barriers, providing techniques for structuring decision analysis, and systematically directing the pattern, timing, or content of discussion”. The PERSUADER’s ability to serve as a framework for performing all three functions is due to a large extent to its case-based reasoning and learning capabilities.

Computer-mediated communication has been shown to promote more equal participation, less inhibited discussion, and decisions which deviate further from initial preferences $[29]$ This promotion of full participation enhances the quality of group decisions $[8,11]$ by allowing extraction of expertise from members and promoting error checking. The major problem of computer-mediated communication appears to lie in greater interpersonal conflict and dissatisfaction with the group process $[29]$ . Often the parties, blinded by their values and criteria, cannot recognize why a proposal may be the best under the circumstances. If a mediator is able to support the generation of justifications for the desirability of the proposal, then the proposal has more chance of being accepted, or at least the party increases its understanding of the issues involved. In our model justifications are provided through presentation of appropriate previous settlements. Moreover, through its central process of mediation, the PERSUADER blunts interpersonal conflict by guiding discussion through case-based counter-proposals (and utility tradeoff calculations) or arguments toward agreements that are jointly beneficial to the parties.

The PERSUADER aids communication among participants in additional ways. By representing participants' positions in the common language of multi-attribute utility theory, the PERSUADER helps avoid miscommunication due to differences in participants' use of terminology [6]. The common representation of participants' positions also guards against "false consensus" [23] and "pluralistic ignorance" [7], both of which present problems to unaided group decision making. As an impartial "agent" in the decision making process, the PERSUADER provides an ideal communication channel capable of providing anonymity or attribution of communications as desired by the participants. This facility has been found by Irving [12] and Turoff and Hiltz [34] to improve the quality of group decision making. Where participants are unwilling to fully share their positions, the PERSUADER proceeds to support conflict resolution guided by its models of participants' utilities in similar previous negotiations.

The “structuring of decision analysis” is central to the PERSUADER’s design. Unlike systems based on game theory or normative decision theory, the PERSUADER takes as its model the human mediator. Rather than proposing Pareto-optimal solutions which are often rejected by decision making groups $[21,16]$ , the PERSUADER acts as a facilitator of naturally occurring group processes. Its approach of progressively narrowing differences among positions mirrors actual negotiations by progressing toward consensus (what the group must do to render a decision) rather than advocating a particular position itself. This flexibility allows the PERSUADER to deal with the non-stationarity of participants’ utilities as positions change in the course of negotiations $[32]$ and support problem restructuring in deadlocked situations $[33]$ . Because the case memory contains not only successes but also previous failures and the failure reason, the PERSUADER is able to efficiently generate suitable modifications to rejected proposals as well as appropriate problem reformulations. Incorporation of “equity” in the evaluation function matches the major departure from optimality noticed in group decision making $[16]$ .

By focusing group attention on a sequence of case-based proposals, the PERSUADER directs discussion along productive lines. Its access to the participants' utilities and a memory of past solutions that express optimal tradeoffs directs the group's discussion toward constellations of issues for which the most painless trade-offs can be made. The emphasis on facilitating group process (decision making) rather than product (the decision) leads directly to the sorts of consensual decisions most likely to be rendered by the group.

Finally, by: (1) structuring the decision making episodes in terms of cases; (2) having an interface that allows the incorporation of new information and user feedback; and (3) by possessing automated memory updating capabilities, the PER-

SUADER both facilitates knowledge acquisition during the decision making process and automatically improves both the quality of its solutions as well as its problem solving efficiency as it enriches its memory with an increasing number of cases.

## 8. Summary

In this paper, we presented the PERSUADER as a framework for intelligent NSS. A NSS paradigm is described which integrates reasoning from experience, use of utilities, and generation of proposals and arguments to facilitate conflict resolution in group decision processes. One of the unique features of the system is its learning capabilities. The proposed decision support system supports the user in the following tasks:

\- formulating proposals that take into consideration not only the user's goals and utilities, but also possible tradeoffs and utilities of other participants to foster a cooperative spirit during conflict resolution;

\- generating appropriate persuasive arguments to help the gradual change of positions towards a final compromise;

\- facilitating the user's evaluation of proposals in terms of his own utilities, so that he can make an appropriate decision;

\- allowing the user to maintain control in disclosing negotiation concerns;

\- maintaining negotiation profiles of other participants and past interactions that may: (a) provide shortcuts to the lengthy negotiation process, and (b) avoid repeating mistakes.

## References

[1] R.G. Anson and Jelassi, M.T. A Developmental Framework for Computer-Supported Conflict Resolution, European Journal of Operational Research 46, No. 2 (1990) 181–199.

[2] L. Applegate, T.T. Chen, B. Konsynski and J. Nunamaker, Knowledge Management in Organizational Planning, Journal of Management Information Systems 3 (1987) 20–27.

[3] Carbonell J.G., C.A. Knoblock and S. Minton, Prodigy: An Integrated Architecture for Planning and Learning, in: K. Van Lehn, Ed., Architectures for Intelligence (Lawrence Erlbaum, Hillsdale, NJ, 1990).

[4] G. DeSanctis and R.B. Gallupe, A Foundation for the Study of Group Decision Support Systems, Management Science 33 (1987) 589–609.

[5] B. Fischoff, Perceived Informativeness of Facts, Journal of Experimental Psychology: Human Perception and Performance 3 (1977) 349–358.

[6] B. Fischoff, S. Watson and C. Hope, Defining Risk, Policy Sciences 17 (1984) 123–139.

[7] S. Fiske and S.E. Taylor, Social Cognition. (Addison-Wesley, New York, 1984).

[8] J.R. Hackman and R.E. Kaplan, Interventions into Group Processes: An Approach to Improving the Effectiveness of Groups, Decision Science 5 (1974) 459–480.

[9] D. Haussler, Learning Conjunctive Concepts in Structural Domains, Technical Report UCSC-CRL-87-1 (Computer Research Lab, University of California at Santa Cruz, Santa Cruz, CA, 1987).

[10] E. Herman and A. Kuhn, Collective Bargaining and Labor Relations. (Prentice-Hall, Englewood Cliffs, NJ, 1981).

[11] C.R. Holloman and H.W. Hendrick, Adequacy of Group Decisions as a Function of the Decision Making Process, Academy of Management Journal 15 (1972) 175–184.

[12] J. Irving, Computer-Assisted Communication in a Directorate of the Canadian Federal Government: A Pilot Study, Technical Report (Directorate for the Non-Medical Use of Drugs, Ottawa, 1976).

[13] M. Jarke, Knowledge Sharing and Negotiation Support for Multiperson Decision Support Systems, Decision Support Systems 2 (1986) 93–102.

[14] D. Kahneman and A. Tversky, On the Psychology of Prediction, Psychological Review 80 (1973) 251–273.

[15] R.L. Keeney and H. Raiffa, Decisions with Multiple Objectives. (Wiley, New York, 1976).

[16] G.E. Kersten, NEGO - Group Decision Support System, Information & Management 8 (1985) 237-246.

[17] S. Kessler, Creative Conflict Resolution: Mediation Leader's Guide, Technical Report, (National Institute for Professional Training, Fountain Valley, CA, 1978).

[18] J.L. Kolodner, Retrieval and Organizational Strategies in Conceptual Memory: A Computer Model (Lawrence Erlbaum, Hillsdale, NJ, 1984).

[19] J.E. Laird, P.S. Rosenbloom and A. Newell, Chunking in Soar: The Anatomy of a General Learning Mechanism, Machine Learning 1 (1986) 11–46.

[20] T.P. Liang, Model Management for Group Decision Support, MIS Quarterly 12, No. 4 (1988) 667–680.

[21] J.G. March and H.A. Simon, Organizations (Wiley, New York, 1958).

[22] D.M. Messik and K. Cook, Eds., Equity Theory: Psychological and Sociological Perspectives (Praeger Publishers, New York, 1983).

[23] R.E. Nisbett and L. Ross, Human Inference: Strategies and Shortcomings of Social Judgement (Prentice-Hall, New York, 1980).

[24] H. Raiffa, The Art and Science of Negotiation (Harvard University Press, Cambridge, MA, 1982).

[25] W. Randle, Collective Bargaining: Principles and Practices (The Riverside Press, Cambridge, MA, 1951).

[26] R.C. Schank, Dynamic Memory (Cambridge University Press, Cambridge, 1982).

[27] M.F. Shakun, Evolutionary Systems Design: Policy Making Under Complexity and Group Decision Support Systems (Holden-Day, Oakland, CA, 1988).

[28] M. Shaw, Mechanisms for Cooperative Problem Solving and Multi-Agent Learning in Distributed Artificial Intelligence Systems. in: Proceedings of the 10th International Workshop on DAI (Banderra, TX, 1990).

[29] J. Siegel, V. Dubrovsky, S. Kiesler and T. McGuire, Group Processes in Computer-Mediated Communication, Organizational Behavior and Human Decision Processes 37 (1986) 157–187.

[30] K. Sycara, Resolving Adversarial Conflicts: An Approach Integrating Case-Based and Analytic Methods, Ph.D. thesis (School of Information and Computer Science Georgia Institute of Technology, 1987).

[31] K. Sycara, Utility Theory in Conflict Resolution, Annals of Operations Research 12 (1988) 65–84.

[32] K. Sycara, Argumentation: Planning Other Agents' Plans, in: Proceedings of the Eleventh International Joint Conference on Artificial Intelligence (IJCAI-89) (Detroit, MI, 1989).

[33] K. Sycara, Problem Restructuring in Negotiation, Management Science 37, No. 10 (1991) 1248–1268.

[34] M. Turoff and S.R. Hiltz, Computer Support for Group versus Individual Decisions, IEEE Transactions on Communications 30 (1982) 82–90.

[35] L.G. Valiant, A Theory of the Learnable, Communications of the ACM 27, No. 11 (1984) 1134–1142.
