---
otero_id: 23516
otero_key: "FRNKGPSE"
title: "Scenario playing for critical success factor analysis"
authors: "Janos Barat"
year: "1992"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1992.3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Scenario playing for critical success factor analysis

JANOS BARAT

Entellect Ltd, Epsom, Surrey, KT19 8AK, UK

This paper presents a structured method, based on practical experience, to derive critical success factors using a business game called ‘scenario playing’. It aims to show why this method is superior to other well-known focusing techniques or group evaluation methods.

The scenario playing business game consists of submitting to managers a sequence of reports, one after the other. Each report (called a scenario) contains randomly generated outcome values for some parameters of the business (called candidate critical success factors) which the manager deemed to be most important for the business at hand. After reviewing each report i.e. scenario, the manager has to give a value judgement about it, like 'good', 'bad' or 'indifferent', reflecting his perception of how the business would be doing if the report was real. A statistical method is used to evaluate these answers and deduct from them which parameters are the most important for the manager who played the given session of the game.

The paper contains a short outline of the statistical evaluation (learning) algorithm used by the author and the description of a software tool that contains an implementation of this technique. Finally, the experience gained by using this tool and approach to derive critical success factors on different projects is discussed.

## Introduction

Following John Rockart's seminal paper in 1979 (Rockart, 1979) on using critical success factors to determine top manager's information need in managing the business, a wealth of papers appeared in the management literature exploring different aspects of the suggested method. It has been noted that critical success factors can be used to help clarify the issues behind the strategy of the business. But it is only relatively recently that the method has become the focus of interest for IT analysts. To some extent this can be explained by the subjective and tedious nature of the underlying evaluation process.

Critical success factors are, by definition, events and conditions ‘in a few key areas which absolutely must go right in order for the business to succeed’ (Rockart, 1979). The main reason for the success of their use in strategic and management information analysis is the fact discovered by Rockart and his team, that across a given industry these factors show a remarkable uniformity and their numbers are few.

Most of the critical success factors are the same for all enterprises within the same industry, since they depend upon the industry structure. Another source of critical success factors is the company's competitive position within the industry, that is the way it is achieving or is aiming to achieve its competitive edge. This view is strongly complemented by the analysis of the industry structure and 'competitive strategies' within the industry given by Porter (1985). Usually, a few of these factors depend on the present stage of the ‘strategic unit’ within the business cycle (start-up, established, declining). Another, usually smaller, number of critical success factors depend on the position of the manager within the company and in this sense they are individual.

Rockart and his team of research analysts reported that in order to establish the critical success factors they conducted two or three interviews with each executive (altogether 3 to 6 hours). Rockart mentions a way of focusing attention by asking the manager to think about a situation when he/she is cut off for 2 weeks from the business without any information getting through and to imagine the first questions coming to mind on return.

This work suggests a method of establishing the critical success factors of the business in a structured manner, and increasing the efficiency of the analysis process by using an interactive framework and an automated software tool.

## Hierarchical decomposition of business aims into critical success factors

Rockart defined a hierarchy of critical success factors depending on the hierarchic nature of the corporate organization and the level at which the strategic issues are discussed. Following these levels one can discuss industry, corporate, sub-organization and individual critical success factors (Bullen and Rockart, 1986) forming a kind of hierarchy (Bullen and Rockart, 1986). An example here could be a well-known industry-level critical success factor for the retail industry; the definition of the correct product mix and the corporate-level critical success factor reflecting this industry-level critical success factor would be market understanding for optimal definition of the product mix.

![](/api/attachments/FRNKGPSE/fulltext/images/36a786464e4e5152c20d44da09c897d5f260ceaa13604f7a5a22c190382066ea.jpg)  
Figure 1

Here the hierarchy is formed by a pre-defined level-structure (see Figure 1). However, if we accept that success of a business means achieving its stated aims then, by Rockart's definition, the critical success factors are pre-conditions which form a dependency relationship with the business aims. In fact, within this structure the business aims are dependent on certain factors and these factors are further dependent on others forming a logical dependency hierarchy.

Rockart (1979) mentioned that the interviews conducted concentrated initially on the objectives of the executive and continued with the critical success factors underlying these objectives. An example could be the above described critical success factor in the retail industry.

Let us assume the highest level business aim is a given profit margin, and certain level of return on investment, which depends on correct setting of the product mix which in turn depends on accurate market information etc. This type of hierarchy uses the logical dependencies of the 'parent' on its 'children' instead of the fixed levels set by the width of strategic platform used by Rockart.

A common occurrence in today's IT literature is to define so-called critical success factors outside the context of the high level aims of the business or indeed, any business at all. For example, although Oracle's systems development methodology CASE Method (1988), gives a correct definition of critical success factors in its glossary of terms, it uses this concept to describe what is critical in a certain phase of the system development process. The method described below ensures that this does not happen.

From 1985–88, on strategic business analysis projects, this method of logical hierarchical decomposition of business aims into critical success factors of an increasingly tangible nature was used, moving towards measurable and executable activities or events. The advantage of such hierarchy is that it is based only on logical dependencies and is free from organizational issues.

A part of a hierarchy of this kind, for a large British company is shown on Figure 2. In this framework the analysis process starts when the group of managers being interviewed, usually a workshop of 1 hour and 25 minutes, develop a critical success factor decomposition tree for their business. This workshop is lead by a consultant analyst prepared for the task by studying the industry structure, the strategic groups within it and the position of the given company in particular. This collectively developed hierarchy is recorded and later used for the individual sessions as the starting point.

![](/api/attachments/FRNKGPSE/fulltext/images/dcd5137dd7b2f6d644a64b7f1dd1b51ee18f76f8d34a8c9c9b1efd0ca67a0287.jpg)  
Figure 2 Decomposition of a critical success factor of the business

The practical problem facing the analyst is how to reduce this often largish number of suggested factors (called here the candidate critical success factors) to a set of a few (typically 5–6) really critical ones, the existence of which was the main discovery made by Rockart.

The method of hierarchic decomposition is also helpful to generate candidate critical success factors. This consists of finding all contributing components of an event or a state of the business deemed to be critical, starting with the business aims. When considering a new component, the question of ‘cause and effect’ relationship between the component and the ‘target’ should be examined. For example, in Figure 2 any of the leaves (terminal branches of the tree) can be challenged by asking ‘is this really a precondition for employing a high-flyer marketing manager?’. If the answer is ‘yes’, or ‘possibly’, then next, the question of completeness (‘are these the only preconditions’) can be discussed for finding other components. This process should be followed within a workshop session with all the relevant managers involved.

In practice, building a pure hierarchy without common elements between the different branches is often impossible. The method in such cases is simply to note the existence of common components and to restructure the hierarchy to eliminate duplicates at a later stage.

The leader of the workshop session is the facilitator consultant analyst and his/her task is to ensure that the branches represent ‘cause and effect’ – type dependencies and not just a breakdown into components of the same thing. When generating the new level of the hierarchy or re-arranging the structure, the facilitator and a responsive, interactive group are more efficient than a formalized, partly individual, idea-generation technique, such as the Nominal Group Technique or the Delphi process.

The individual consideration and round-robin, idea-generating method within the Nominal Group Technique would probably double the time needed for hierarchy building (decomposition phase) compared with the suggested facilitator-led workshop. The Delphi process, in particular, is dependent on the availability of a considerable amount of time where individuals answer focused questions in writing (4).

Both the Nominal Group Technique and the Delphi process are aimed at generating critical ideas by creating non-leader-centred working conditions, and developing an understanding of the problems and the component parts of their solutions (4). However, they lack focusing power and depend on the participants' ability to grasp the entirety of a complex set of parameters without looking into the detail behind them.

The aim of the workshop stage is to incorporate the diversity which the group generates into the hierarchy, and to arrive at a single logical structure. This jointly developed and agreed hierarchy is then subjected to a step-by-step weighting process where individual managers assign priorities to different candidate critical success factors, pruning the hierarchy by considering only the high-priority leaves of the tree, branch after branch, in a bottom-up process.

## Selecting the critical success factors by a weighting process

Although Rockart established the fact that most of the critical success factors are derived from the structure of the industry (or industries) in which the business is operating, he also showed that not all of them are the same for each enterprise within that industry. There are other factors, dependent, for example, on the development stage of the business within its life cycle (for example, the marketing manager has left the company) strongly influencing the final composition of the critical success factors. The selection process can be a time-consuming re-examination of the views held by different people, even at the same level of management.

To facilitate this process we are suggesting a structured approach, consisting of a methodical comparison of different people's priorities. This process should be conducted by analysts with a fair knowledge of the industry in question. One obvious way to reduce the number of suggested critical success factors is to establish relative priorities between them and eliminate the ones with very low priority.

Consider the leaves a1–a4 and b1–b3 in Figure 3. Let us assume the weighting resulted in identifying a2 and a3 as the most important candidate critical success factors in branch A with the rest playing no significant role, and leaf b2 as the dominant factor of its own branch (B). The next step in this case should therefore be to disregard leaves a1, a4 and b1, b3 and produce a combined branch A, B. The result at this stage in the process should be the one depicted in Figure 4.

This ‘divide and conquer’ contraction technique is used to deal with the problem of considering a large number of candidate critical success factors. Practice has shown that a group of more than 12 factors is too large to be meaningfully discussed. The decomposition process continues until either executable and measurable candidate critical success factors are met or, as can be seen below, key measurable attributes of the candidate critical success factors are identified.

![](/api/attachments/FRNKGPSE/fulltext/images/52a3ff9fffac5ea1b5d2e322d83befebf6492c3987a06ebc97588d541a9cff90.jpg)  
Figure 3 Schematic picture of two branches of the same critical success factor hierarchy

## Scenario playing – the game to involve managers

People are notoriously poor judges of their own priorities. When confronted with complex systems, they tend to forget about important components and prerequisites. Only when forced to consider concrete situations are they capable of grasping fully the significance of an individual partner.

It is a well-known fact that practitioners are more comfortable when considering situations which are closely related to their everyday work than contemplating theoretical constructs of abstract models. This is the reason for the success of management games or management literature that describes real-life situations.

Scenario playing uses the attraction of close-to-life situations linked to an interactive game for extracting knowledge about the business and the process of managerial judgement. It is a powerful tool which enables analysts to establish priorities between different parameters describing the business. Scenario playing for the establishment of critical success factors consists of constructing imaginary reports about the state of the business, using the candidate critical success factors as indicators in the report to elicit judgements about business priority.

![](/api/attachments/FRNKGPSE/fulltext/images/e272a5f22890782bd4a495935d4305ad4de8104c4e0ac756240739d901143884.jpg)  
Figure 4 The combined branch A, B after the weighting and pruning process

Let us consider the hierarchy presented in Figure 1. By further decomposition the following, measurable, operative parameters could possibly be arrived at (key attributes of the recruitment process, connected with the identified applicants):

(1) The number of applicants with current salary at the level of 30–35 000;

(2) The overall number of applicants;

(3) The number of applicants from a similar sized organization;

(4) The number of applicants selected for second interview compared with the total number of applicants.

When such a level of detail is reached we can estimate the factors, at least in terms of a range within which expected outcomes should be observed. So, for example, experience from previous recruitment campaigns shows that from a single agency one could expect to obtain 12–20 candidates, and an additional 8–9 from referrals, so that the total number of applicants is expected to be around 20 but sometimes may reach as high as 80. This high value can be the result of a special event (for example, redundancies) in the industry or coincidence with newly graduated MBAs appearing on the market.

Similar ranges can be attached to the other candidate critical success factors and real life reports (with weekly frequency) would look similar to that in Table 1. With the dots representing entries from other branches of the same hierarchy.

Reports of this type are familiar to managers. They are used in situations when a project needs tight control and early indication is required that something may be going wrong. In scenario playing the outcomes of the reports are generated within the ranges set by the participants in the decomposition exercise. Scenario playing is conducted within the framework of a game consisting of a sequence of scenarios. It also simulates the managerial control process by the introduction of an element of interactiveness. This interactive element consists of a response given to each report by the provider of the knowledge, i.e. a manager or group of managers to whom the scenarios are presented during the game. This response should be put against the reports in the form of a judgement about the report in its entirety – expressed by statements like ‘good’, ‘average’ or ‘bad’.

Table 1 A scenario representing a business report for a recruitment campaign

<table><tr><td colspan="2">Report-Business position week No. 12</td></tr><tr><td>Number of applicants with salary round 35K (campaign start: week 9)</td><td>18</td></tr><tr><td>Total number of applicants (to date)</td><td>27</td></tr><tr><td>Applicants from similar organizations</td><td>17</td></tr><tr><td>Applicants listed for second interview</td><td>8</td></tr></table>

These judgements are called classifications and the allowed statements, such as ‘good’, ‘average’, etc. are categories. The name of the categories are defined by the participants.

Let us try to make a value judgement about the scenarios represented in Table 1. The number of total applicants is at a normal expected level, may be a bit above it. The number of applicants with the proper experience, indicated by their salary levels is around 66% of the total (18/27) which is probably a little disappointing because the agency should have done a better job to attract the right calibre people. On the other hand, the ones applied are, except for one, all from the same industry ('similar organization'), which shows that the effort of the agency in communicating the job requirements was successful. The number of applicants listed for second interview is quite high for a campaign of this type. The overall picture seems to be favourable and the judgement for this scenario would probably be 'good'.

When the participant(s) of the game have reviewed and classified all the scenarios, the tool can deduce the relative weights ascribed to different candidate success factors in the decision-making process. This ability to obtain the relative importance of difference factors by observing a series of decisions (learning by watching) is the main feature of the Scenario Playing Framework.

The strength of the process at this point is that it has elicited real management decisions in a realistic business context. The difficulty people experience when weighting the importance of different parameters when dealing with complex systems is partly related to the variety and character of time-delays between inputs and outputs. The other connected problem is limited experience in variations of the outcome for the measurable parameters.

Let us take the example of driving a car. The difference between a conventional driver and a professional one is the experience the professional driver has gained by applying unconventional ways to control the car (for example, by accelerating). This shows us that to extract the true importance of different control parameters we have to generate a wider variety of combinations for the parameter values than those which occur within the experience of the manager.

For this purpose, some decision support methods try to apply unconventional provocative questions, like 'what would Shakespeare have said about this?'. The suggested approach is more down to earth. Here the scenarios are generated independently for each parameter (Candidate critical success factor) at random, within the widest theoretically possible range, to achieve the desired effect of provoking and facilitating the managerial thinking process. The other problem is to evaluate the responses. What do the results represent? Is this an objective picture of the underlying process or does it merely represent a totally arbitrary bias in the participant's mind?

To decide whether a set of relative priorities is objectively defined (and is a reflection of the present business strategy) can be a tricky business. One way to obtain a degree of objectivity is to compare the scenario games and achieve a consensus of opinion on the decisions made during a game.

This process of seeking agreement among a group of decision makers is called consensus seeking.

## Consensus seeking

The independent review by more than one player of the same game will inevitably uncover differences of opinion. But this can be used to enhance the degree of objectivity from the initial results of the scenario game. When the participants consider the different decisions taken by individuals for the same scenarios, they should discuss the differences in a workshop-like session with the aim of achieving a common understanding.

It is the objective of this consensus-seeking process to identify the main causes of differences and bring them out into open debate. When the differences have been discussed and the business objectives implied have been clarified and agreed, the players may repeat the game and test whether the new responses (classifications) reflect the result of these discussions. There will probably be some differences remaining. However, these are often caused by the different roles which individuals play within the organization. The process should allow these differences to remain, since they often express genuine individual need for information.

An important issue is the quality of the critical success factor definition process. It is quite clear that the critical success factors should reflect the strategy of the business since they are a verbalization of the most important means by which the objectives of the business are achieved at the time and in the circumstances in which the Manager in question is operating. Therefore, the correspondence of the critical success factor to the business strategy is a reasonable measure for the quality of the factors derived.

In practice, companies are often conducting their business without a clearly verbalized and formulated strategy. Defining the critical success factors should help this strategy formulation process.

## Outline of the mathematical method

The process of learning described above is performed by treating the values of the parameters (candidate critical success factors) as components of vectors in an n-dimensional vector space (where n is the number of candidate critical success factors).

See, for example, Table 1 where the business position report shows values for the four parameters of 18, 27, 17 and 8 respectively. For simplicity let us forget about the fourth parameter and discuss a 3 component case. This means that we have a vector $\mathbf{v} = \{18, 27, 17\}$ corresponding to a point in the 3-dimensional space and the classification attached to it (say, 'Good') groups this point into a cluster of points all belonging to the same class. The components of our vector $\mathbf{v}$ are $\{\mathbf{v}_1, \ldots, \mathbf{v}_3\}$ representing projections on their co-ordinate axes. Such a vector is shown in Figure 5. Each report corresponds to a point in the 3-dimensional space selected by the end point of this vector.

Now the task of learning can be defined so that as a result of observing a series of classifications performed by the participant(s) during the scenario playing game, we obtain the ability to separate the clusters belonging to different classes. In geometric terms this means to construct some surface or surfaces which separate these areas. However, we must go one step further. We have to define the relative importance of each candidate critical success factor in determining these separating surfaces. An example of the clusters created during such a game is shown in Figure 6.

The method we adopted for the learning process is also illustrated on this picture. We search for a line in the m-dimensional space such that when the clusters are projected onto it we are able to find points on this line which can serve as separators between the classes. In this case (which is 3-dimensional) such points are a and b.

![](/api/attachments/FRNKGPSE/fulltext/images/8e0fdb729b534edb001226c8830a7cdc3a66b2cedfad258d9811b31625ba3680.jpg)  
Figure 5 The picture of a 3-dimensional vector corresponding to a point in this space

![](/api/attachments/FRNKGPSE/fulltext/images/da3baf5fd3b931414901e81aca7dbdb498b7216b9988b0b30c6755b07ada1e14.jpg)  
Figure 6 Representation of points generated during a scenario game and clusters created by the classifications. The position of the bold line is the first result of calculation performed by the algorithm, which tries to find such a position for it, that when the points of the clusters are projected onto it the 'best quality' separating points can be found

The quality of separation is defined by the number of erroneously classified points. It is intuitively clear that in some involved cases this quality can be very poor and therefore it may be concluded that no such line exists.

The importance of a particular parameter can be assessed in different ways. One obvious method is to calculate the degradation in the quality of separation when the parameter in question is left out from the search for the line providing the best separating points. This process results in the derivation of the relative weight a parameter (and therefore the candidate critical success factor it represents) plays in the decision-making process. It provides an objective measure of management priorities in the absence of a form set of rules.

A more rigorous description of the mathematical method can be found in (3).

## A computer software tool supporting scenario playing

During 1986–87, while working for Entellect Ltd, the author developed a personal computer-based software tool called 'Consultant Analyst' to support the method described above. The user interface to other parts of Data Analysis (e.g. Business Function Decomposition, Entity/

Relationship Modelling etc.) was defined mainly by Duncan Walker. This tool was used on a number of projects by the author and by other consultancies, for example, Coopers and Lybrand, Deloitte.

The tool provides a graphical interface to record and manipulate candidate critical success factors and also to connect them to business functions defined in the process of Data Analysis. The interface for candidate critical success factors supports the decomposition process in a hierarchical fashion, and enables the user to record additional data behind each candidate critical success factor, such as target, range, and so on. It has a fast and user-friendly way to traverse a hierarchy and to restructure it in different ways. It also enables the user to break up a hierarchy or combine two hierarchies into one in a single operation.

The software tool has a facility to save/compare game sessions from different (or, if needed, the same) players. The differences in decision-making patterns for extremes are evaluated and suggested by the software as 'the two sessions furthest apart' and 'the two sessions closest to each other'. When a number of sessions are submitted to such 'compare' evaluation, the software also calculates a suggested 'consensus' view of the candidate critical success factors.

## Practical experience using the method and the software tool

The majority of projects where the method was used included some aspect of organizational study, requiring the derivation of critical success factors at different levels of management. This side of the method turned out to be very useful to check the 'state of health' of an organization. The degree of propagation of corporate objectives to lower echelons of management is a good measure of this.

The major benefit provided by the method and the software tool was to upgrade analysis from being purely subjective and paper based. The scenario playing business game supplied a necessary focus and stimulus for extracting the critical success factors and applying due consideration to the issues in depth. The scenario playing method proved to be the vehicle which enabled the consultant/facilitator to achieve the focus emphasized by Rockart, and to do so in a standard and consistent manner.

Another important benefit of using the software tool was the immediate impact of changes requested by the user. The ability to change ranges, names and definitions had a significant effect and gave confidence to the interviewee/user that it was he/she who was driving the process. As a high-level manager of a telecommunication company expressed it 'the game and the tool made me feel on top of the process instead of being pushed around by consultants'.

In the same company another executive insisted on taking away the tool and playing the scenario game to derive the critical success factors himself. This enabling property of the software tool played an important part in its popularity. The major drawback of this early software tool was related to an inability to use long enough names and survey large enough hierarchies due to limitations of space on the screen (the largest screen supported was the IBM or Compaq VGA screen).

It was also felt that in certain situations the knowledge of the way in which the tool derived the relative priorities between candidate critical success factors would have been advantageous. In particular, when a more complicated topology of clusters was bound to emerge because, for example, the target values for a candidate critical success factor were in the middle of its theoretical range, the software tool in its early releases could not properly separate the classes and gave no warning or explanation of the reasons for the failure. Later releases correcting this last problem greatly enhanced usability and confidence in the software for the users.

When the results of the critical success factor derivation process with the scenario game and without it were compared the main difference was in a better correspondence to the chosen strategy of the business when the scenario game was used.

## Conclusions

The scenario playing framework, when supported by a flexible software tool on a personal computer, was a valuable focusing instrument for the process of evaluation for critical success factors, superior to any other known group evaluation technique. The game element in scenario playing provides the attraction and ensures involvement, and the generated scenarios provide the vehicle to achieve depth of discussion. The combination of individual priority setting and group consensus seeking helps communication between a peer group of managers and brings differences in approach, viewpoints and even individual agenda into the open.

The hierarchic decomposition of high level aims into measurable and executable parameters of the business provides an objective basis for the discussions when the priorities have been agreed.

The objectivity combined with the ease of obtaining management commitment leads to better quality of the resulting critical success factors.

## References

Barat, J. Extracting Priorities of Factors in Scenario Playing. To be published shortly.

Bullen, C.V. and Rockart, J.F. (1986) A Primer on Critical Success Factors, (Dow Jones-Irwin, Homewood, Illinois, MIT).

Delbecq, A.L., Van de Ven, A.H. and Gustafson, D.H. (1978) Group Techniques for Program Planning (Scott Foresman and Company, Glenview, Illinois).

Porter, M.E. (1985) Competitive Advantage (The Free Press, New York, London).

Rao, C.R. (1973) Linear Statistical Inference and its Application (Wiley, New York).

Rockart, J.F. (1979) Chief executives define their own data needs, Harvard Business Review, March–April, p. 81.
