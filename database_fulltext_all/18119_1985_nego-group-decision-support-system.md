---
otero_id: 18119
otero_key: "HRAYTSJ2"
title: "NEGO — Group decision support system"
authors: "Gregory E. Kersten"
year: "1985"
journal: "Information & Management"
doi: "10.1016/0378-7206(85)90001-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# NEGO – Group Decision Support System

Gregory E. Kersten \*

Department of Management Systems, Management Organization and Development Institute, ul. Wawelska 56, Warsaw, Poland

There are two major frameworks for decision making: maximizing and satisficing. A combination of both may be used to describe group decision making (GDM). In the satisficing approach, decision makers (DMs) formulate aspiration levels or demands which take the form of constraints. Choosing from among different decisions, DMs take into account their preferences or wants, which take the form of objective functions.

GDM is divided into two stages: first, each DM makes a decision, and second, DMs negotiate so as to achieve a compromise decision. Negotiating is an iterative process. Negotiations are completed when all demands have been met.

The group decision support system “NEGO” assists DMs in finding a compromise. It has been used for solving a GDM problem at the corporate level and is currently utilized in management courses.

Keywords: Decision Support System, Negotiations, Group Decision Making, Multiobjective Decision Making, Multiobjective Linear Programming, Goal Programming.

![](/api/attachments/HRAYTSJ2/fulltext/images/78578ce3b84fcc2e8aa95d2b2cd80f7bcb036f1f25799e0bfe7085b23c2a7440.jpg)

Gregory E. Kersten is an Assistant Professor at the Carleton University School of Business. From 1973 until 1984 he was an Assistant Professor in the Management Organization and Development Institute in Warsaw. He received his M.A. in Econometrics and Ph.D. in Economic Science-Operations Research from the Central School of Planning and Statistics in Warsaw. He is the author and co-author of more than twenty papers and two text-books, most of them published in Polish. He is also the co-developer of two MIS for short and medium term macroeconomic planning. Dr. Kersten's present research interests are in the area of decision support systems, group decision making and multiobjective mathematical programming.

## 1. Group Decision Making

The process of formulating the policy of a plan for an organization by its members has been called group decision making (GDM). Cohon [2] distinguishes three ways of solving such problems. The first is based on aggregation of objectives and preferences of individual decision makers (DMs) into a group utility function or social welfare function. Arrow [1], Sen [14], and more recently Korhonen, Wallenius and Zionts [9] developed this type of method. The second is based on settlement of fragmented problems. Such methods are designed to advise individual DMs of the best possible decision [3]. The third type aims at anticipating the results of GDM. These methods were developed by Harsanyi [5], Raiffa [11] and Rapoport [12]. As they are based on game theory, they are not readily applicable to real life situations.

Although there is a variety of GDM methods, only a few have been successfully utilized in practice. Among these three methods based on mathematical programming $[4,9]$ .

All GDM procedures which utilize utility theory, among them those which utilize mathematical programming models, are based on the Pareto principle (1906): a state of the world A is preferable to a state B if in A at least one person is better off and nobody is worse off. Following this principle, the typical assumption says that there is a group utility function which is an increasing function of individual utilities. In some GDM procedures [9] this assumption is accompanied by the assumption – DMs are in consensus in the pairwise comparison of different alternatives.

The last assumption seems to be too strong and there are many examples that violate it, e.g. different proposals in arms control negotiatins are differently evaluated and each party claims that its choice is better; thus there is no consensus in pairwise comparison. Similarly, in policy formulation in a company, a DM will find an alternative \* Present address: School of Business, Carleton University, Ottawa, Ontario K1S 5B6, Canada

which gives more power preferable to one that retains the balance of power. For this reason the evaluation of these alternatives may differ from those of another DM.

Lack of consensus in pairwise comparison is caused by DM's different assessment of the group utility. This is one of the reasons why negotiations are so difficult and time consuming.

The assumption about existence of a group (individual) utility function which is an increasing function of individual utilities (objectives) is the core of most approaches towards solving GDM problems (multiobjective decision problems with only one DM). From this assumption, it follows that the chosen decision should be a non-dominated solution for which group or individual utility reaches its maximum.

The maximizing behavior of DMS is questioned by advocates of satisficing behavior $[10,13,16]$ and their experimental and behavioural basis is much stronger than those of the utility maximization framework. DMs form aspiration levels and actually use them in practical decision making. Therefore we should take the satisficing approach into account in a GDM procedure. However, people also have their wishes and wants and they expect them to be satisfied at the highest possible level. Thus, a combination of two approaches ought to describe GDM problems better. Also, the development of cheap computer systems make offensive (optimization) behaviour easier to provide now than 27 years ago, when March and Simon originally wrote about defensive (satisficing) behaviour.

The question of group utility and its application remains to be considered. Let us look at two solutions that differ in the performance level of the utility function of only one DM. Group utility is an increasing function of individual utilities, so the solution in which the utility of one DM is greater should be considered by the group as better than the second. But in practice, more often than not this is not the case. When only one negotiator improves his position, the others perceive that their position has worsened. If, in wage bargaining, only one group of workers achieves increase in wages, other groups will not consider it a good solution. If their utility functions at the beginning of bargaining were functions of their wages only, after such a proposal, these functions would change. That means that utility functions are nonstationary, and this is induced by changes of context in decision making [17]. Concessions and interactions among DMs cause changes in individual utilities, and therefore in group utility.

We may conclude now that the Pareto principle describes a Utopian world with ideal, unselfish, and generous people. In the real world, if someone is better off others are worse off. Moreover, if according to the Pareto principle someone is better off in state A than in state B, people think that the difference between these states can be more fairly divided. They think, often correctly, that what makes one person better in state A than in state B may be distributed more evenly amongst them all. Thus, we come to the problem of fairness and, related to it, the concept of nondominated solutions.

Usually it is assumed that a compromise decision should be a nondominated solution, regardless of whether a utility function is utilized or not. However, in GDM conditioned concessions are likely to appear, e.g. "If I make concessions others have to make them too". This means that to achieve a "fair compromise", we must add additional constraints; this may cause a domination of the solution.

From the above it follows that in a GDM procedure we should exclude pairwise comparison of alternatives and the concept of utility functions, but we should consider both satisficing and maximizing approaches and we should enable DMs to choose any feasible solution for a compromise.

## 2. The Interactive Procedure

The procedure on which the computer system NEGO is based does not have a group utility; utilization of individual utilities is limited to stage 1, in which DMs work independently – before they become a group. It is assumed that the GDM problem can be presented as multiobjective linear programming (MOLP) problem; however, DMs can choose any feasible solution for a compromise. Whether the compromise is a nondominated or a dominated solution depends on the DMs.

The procedure belongs to the second type of GDM methods. It was designed to structure the problem, to solve the decision problems of individual DMs, and to propose a compromise. It is an interactive procedure that enables DMs to change their behaviours and strategies, and to form coalitions.

Table 1  
Individual and Compromise Proposals and Mean Values.

<table><tr><td>No.</td><td>Objective</td><td>Wants &amp; Demands</td><td>DM no. 1</td><td>...</td><td>DM no. m</td><td>Compromise Proposal</td><td>Mean Values</td></tr><tr><td>1</td><td>Name 1</td><td rowspan="2">Wants &amp; Demands of one DM</td><td rowspan="2" colspan="3">DMs&#x27; individual proposals;objective performance levels</td><td rowspan="2">Obj. perform. levels of compromise proposal</td><td rowspan="2">Mean val. of obj.perf. levels</td></tr><tr><td>n</td><td>Name n</td></tr></table>

In stage 1, a MOLP problem is formulated for each DM. It is assumed that these problems are linear, so we can use one of the many MOLP methods, e.g. [15] or [18]. Since stage 1 is a preliminary step of GDM, we suggest that a simple method of calculating individual proposals (alternatives) be used. In NEGO each DM chooses objectives, prescribes a rank to each of them, and then the coefficients of the individual linear utility function are calculated on the basis of these ranks and scale factors.

Stage 1 is completed when each DM has formulated an individual proposal. If proposals of all DMs are the same, the GDM problem is solved and no compromise is required. If, however, some proposals differ, it is necessary to begin negotiations. Before these start stage 2 of the procedure, DMs receive and analyse a table that contains all objective performance levels of all individual proposals and their mean values.

Stage 2, negotiations, consists of eight steps.

Step 1. Let $k$ be the iteration index and set $k = k + 1$ (in stage 1 $k = 0$ ).

Step 2. Utilizing information received after completing stage 1 (for k = 1) or information included in Table 1 (for $k \geq 2$ ), each DM formulates wants. These take the form of objective functions and optimization criteria.

Step 3. We assume that for every objective, the DM can fix the minimum or maximum acceptable performance level, i.e. aspiration level. Thus each DM formulates bounds that reflect the demands on the objectives.

Step 4. The demands of a DM can also be connected with objectives which were not chosen in iteration k; e.g. it may be desirable to restrict performance levels on other DMs objectives. These additional constraints are now specified.

Step 5. When each DM has formulated all wants and demands, an attempt is made to find a decision which fulfills all the demands of all DMs. In order to do so, we formulate a one-sided goal programming problem. The solution of the problem is called a compromise proposal and it meets the demands “as closely as possible”.

The optimal value of the objective function of the problem is the measure of a distance between the present state of negotiations described by the DMs' demands and consensus. If it is equal to zero, the compromise proposal fulfills all the demands and we go to step 8. If it is positive, DMs can compare the value achieved in this iteration with those achieved previously and check whether they are converging towards consensus.

The objective function is the summation of terms which describe the individual DMs commitment to the actual distance. Taking into account present and previous values of those terms, we can define a DM's toughness in negotiations.

Step 6. It is necessary for DMs to reformulate their demands, i.e. to make concessions. Otherwise negotiations are deadlocked. This is excluded from our considerations, because we assume that each DM is interested in obtaining a compromise.

The compromise proposal of step 5 gives information that enables DMs to reformulate their wants and demands. But we help to facilitate the process; we calculate an individual proposal for each DM. This is an optimal solution of a goal programming problem with preemptive priority factors in the objective function. The solution of the problem meets “as closely as possible” all demands of a given DM, then takes into account all aggregated wants of other DMs, and finally takes into account wants of the given DM.

If it is possible, the DM's individual proposal meets all the demands so it is acceptable. From all acceptable alternatives we choose the one which is the best for the remaining DMs taken together; i.e., their aggregated wants are fulfilled on the maximum level. If there are more than one “best for others” alternatives, we choose the one which is the best for the given DM. One way of modelling DM concession making is to assign higher priorities to wants of others than to the DM in question. These, in turn, should allow other DMs to achieve wants on higher levels.

Step 7. We calculate mean values on the basis of objective performance levels of individual proposals and construct separate tables for each DM, as shown in Table 1. Then we return to step 1.

Step 8. This is reached when the DMs have reached consensus, i.e. all their demands have been met. When dealing with a compromise decision we should take their wants into account. This is possible in many ways with different levels of complexity; the simplest is to treat all objectives as of equal importance. Thus, we can formulate and solve an LP problem in which all demands are additional constraints and the DMS objectives constitute the overall objective function.

Stage 2 of the procedure begins when there is no acceptable solution for all DMs. Concessions made in steps 3 and 4 are aimed at achieving at least one solution acceptable by all. It seems appropriate to assume that the set of such solutions does not contain one for which objective performance levels are basically different from the DM's point of view. This assumption enables us to utilize the above described LP problem for calculating the compromise decision that is the solution of the GMD problem. The formalized procedure with all mathematical details is given in [8].

## 3. The NEGO Computer System

The above procedure has been programmed. NEGO consists of programs written in FORTRAN, EXEC 2 and Assembler and runs on an

IBM 370/148 under VM/VSP. Linear programming problems are solved by the IBM Mathematical Programming System Extended (MPSX/370) package. When NEGO is run on graphic display terminals (IBM 3279/3B), it uses the Graphical Data Display Manager/Presentation Graphic Feature (GDDM/PGF).

A group of not more than four DMs can use NEGO via graphic display terminals. All DMs' virtual machines are linked to a so-called service machine, which is used by the person who supervises or organizes negotiations (or the person who runs the management course). He/she gets all the information about the state of negotiations and evaluation of DMs' particular demands from the point of view of compromise.

At present NEGO is used in executive development courses. One of two GDM problems (based on real-life case studies) is solved by course participants, using NEGO. The studies are for a production planning and a profit distribution system.

A group of participants usually consists of 20 people divided into 4 groups, with each group standing for one DM. It takes between 2–3 hours of participation time to reach a compromise or to come to a stage of negotiations when there is practically no difference between individual proposals and the compromise. These occur after 6 to 8 iterations of stage 2. Although this seems long (iterations could be completed in less than one hour), for many participants this is the first contact with a computer, so they make errors, correct them, and discuss the problem within their group and among groups; they also receive tables to read and compare. It is interesting that, in our experience, compromise has never been reached in stage 1.

All the terminals are in the same room, thus participants can talk freely. After two to three iterations (during which discussion within groups occurs), informal talks among participants from different groups increases. First of all, those participants who represent company executives try to exert pressure on others, so as to achieve their demands.

Wants and demands as well as all proposals are present in tables and graphs; the latter are considered very useful, because they give information and help in selection of an appropriate strategy. Tables help to define precisely wants and demands.

Table 2  
DM's Objectives and Objective Functions.

<table><tr><td>No.</td><td>Name</td><td>Objective Contents</td><td>Obj. Function</td></tr><tr><td>1</td><td>WAGES PROD.</td><td>Wages in goods producing unit</td><td> $2.4x_{1} - 1.2 x_{2}$ </td></tr><tr><td>2</td><td>BONUSES PROD.</td><td>Bonuses in goods producing unit</td><td> $x_{1} - 0.9 x_{2}$ </td></tr><tr><td>3</td><td>PROFIT PROD.</td><td>Profit in goods producing unit</td><td> $x_{1}$ </td></tr><tr><td>4</td><td>TOTAL PROFIT</td><td>Profit of the enterprise (3 + 7)</td><td> $x_{1} + x_{2}$ </td></tr><tr><td>5</td><td>EXPORT</td><td>Export of the enterprise</td><td> $x_{1} + 1.75x_{2}$ </td></tr><tr><td>6</td><td>WAGES SERV.</td><td>Wages in services producing unit</td><td> $-0.9x_{1} + 2 x_{2}$ </td></tr><tr><td>7</td><td>PROFIT SERV.</td><td>Profit in services producing unit</td><td> $x_{2}$ </td></tr></table>

## 4. An Example of the Use of NEGO

## 4.1. Description of the Example

We choose a simple example, not a case study, because it allows us to present the process of solving a GDM problem and features of the solution. This is one of the examples used to test NEGO; it was solved several times by members of our Institute to show how the system works and how it can be utilized.

The enterprise of two units. The first produces goods, the second produces services. Activities of these units are described by two decision variables: $x_{1}$ – the level of production and $x_{2}$ – the level of services. The set of feasible decisions is described by the following inequalities:

$$
\begin{array}{r l} 0. 5 x _ {1} + 0. 5 x _ {2} & \leq 9 \\ 3 x _ {1} - x _ {2} & \leq 3 3 \\ x _ {1} + 4 & x _ {2} \leq 4 8 \\ 8 x _ {1} - 1 2 & x _ {2} \geq 9 6 \\ 3 x _ {1} + 8 & x _ {2} \geq 2 4 \\ x _ {1} & \geq 0, x _ {2} \geq 0 \end{array}
$$

We shall not explain these; it is assumed that they describe a model of the real work operating conditions, involving the equipment, work force, and orders.

Decisions on levels of production and services are made by DM1 – the manager of the first unit, DM2 – the director of the enterprise and DM3 – the manager of the second unit. All possible DMs' objectives are given in Table 2.

## 4.2. Solution

We solve this problem with the help of NEGO, and to show its features we use different forms of illustration of its inputs and outputs. Table 3 contains DMs' wants formulated in stage 1.

In stage 1 DMs did not formulate any demands so as to achieve their objectives on the highest possible levels. The outcomes of their activities are shown in fig. 1 which contains the computer printout in a session for DM1. It will be seen that the full realization of DM1's objectives leads to a negative value of wages in service. A conflict also arises between the objectives of DM3 and wages and bonuses in production. It is obvious that these proposals cannot be accepted and none can be considered better in pairwise comparison.

A way of changing objectives and demands is also illustrated in Fig. 1. To distinguish between

Table 3  
Wants and Demands.

<table><tr><td rowspan="2">No.</td><td rowspan="2">Name</td><td colspan="3">Stage 1</td><td colspan="2">Stage 2, Iteration 1</td></tr><tr><td>DM1</td><td>DM2</td><td>DM3</td><td>DM2</td><td>DM3</td></tr><tr><td>1</td><td>WAGES PROD.</td><td>MAX</td><td></td><td></td><td>LE 13.0</td><td></td></tr><tr><td>2</td><td>BONUSES PROD.</td><td>MAX</td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>PROFIT PROD.</td><td>MAX</td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>TOTAL PROFIT</td><td></td><td>MAX</td><td></td><td>MAX 15.5</td><td>LE 15.0</td></tr><tr><td>5</td><td>EXPORT</td><td></td><td>MAX</td><td></td><td>MAX 21.0</td><td></td></tr><tr><td>6</td><td>WAGES SERV.</td><td></td><td></td><td>MAX</td><td>LE 6.5</td><td>MAX 8.5</td></tr><tr><td>7</td><td>PROFIT SERV.</td><td></td><td></td><td>MAX</td><td></td><td>GE 6.0</td></tr></table>

INDIVIDUAL PROPOSALS
COMPARE OBJECTIVE PERFORMANCE LEVELS

<table><tr><td>NO</td><td>OBJECTIVE</td><td colspan="2">WANTS &amp; DEMAND</td><td>DM 1</td><td>DM 2</td><td>DM 3</td><td>MEANS</td></tr><tr><td>1</td><td>WAGES PROD.</td><td>MAX</td><td>0.0</td><td>25.886</td><td>7.200</td><td>-2.618</td><td>10.156</td></tr><tr><td>2</td><td>BONUSES PROD.</td><td>MAX</td><td>0.0</td><td>10.271</td><td>-1.000</td><td>-5.455</td><td>1.272</td></tr><tr><td>3</td><td>PROFIT PROD.</td><td>MAX</td><td>0.0</td><td>11.429</td><td>8.000</td><td>4.364</td><td>7.931</td></tr><tr><td>4</td><td>TOTAL PROFIT</td><td></td><td>0.0</td><td>12.714</td><td>18.000</td><td>15.273</td><td>15.329</td></tr><tr><td>5</td><td>EXPORT</td><td></td><td>0.0</td><td>13.679</td><td>25.500</td><td>23.455</td><td>20.878</td></tr><tr><td>6</td><td>WAGES SERV.</td><td></td><td>0.0</td><td>-7.714</td><td>12.800</td><td>17.891</td><td>7.659</td></tr><tr><td>7</td><td>PROFIT SERV.</td><td></td><td>0.0</td><td>1.286</td><td>10.000</td><td>10.909</td><td>7.398</td></tr></table>

DO YOU WANT TO SEE ALL PROPOSALS IN GRAPHIC FORM? IF YES WRITE 1, IF NOT WRITE 0.
1
@@@@

DO YOU WANT TO NEGOTIATE - TO FIND A COMPROMISE DECISION? IF YES, WRITE 1, IF NOT WRITE 0.

1
@@@@@

CHOOSE YOUR OBJECTIVES - WRITE THEIR NUMBERS. AT THE END WRITE 0.

1
@@@@@

3
@@@@@

0
@@@@@

GIVE ACCEPTABLE PERFORMANCE LEVELS OF YOUR OBJECTIVES, THE LOWEST WHEN YOU WANT TO MAXIMIZE YOUR OBJ. THE HIGHEST OTHERWISE (WHEN MIN).

YOUR OBJ. \*\* WAGES PROD. \*\*

THE PREVIOUS OBJ. PERF. LEVEL = 25.886 MEAN VALUE = 10.156. THE STILL ACCEPTABLE LEVEL IS ... (WRITE THE VALUE). THEN WRITE "MIN" IF YOU WANT TO ACHIEVE YOUR OBJ. ON THE LOWEST LEVEL OR WRITE "MAX" IF ON THE HIGHEST.

1
MAX
@ @ @ @
@ @ @ @

YOUR OBJ. \*\* PROFIT PROD. \*\*

THE PREVIOUS OBJ. PERF. LEVEL = 11.429 MEAN VALUE = 7.931. THE STILL ACCEPTABLE LEVEL IS ... (WRITE THE VALUE). THEN WRITE "MIN" IF YOU WANT TO ACHIEVE YOUR OBJ. ON THE LOWEST LEVEL OR WRITE "MAX" IF ON THE HIGHEST.

8.5
MAX
@@@@@
@@@@@

YOU CAN SET UP BOUNDS ON PERFORMANCE LEVELS OF THESE OBJECTIVES (INDICES) WHICH YOU HAVE NOT CHOSEN AS YOURS IF YOU WANT TO SET UP BOUNDS WRITE 1, IF NOT WRITE 0.

1
@@@@@

WRITE NUMBERS OF BOUNDS (ONE IN THE ROW) IF THE END WRITE 0.

2
@@@@@

6
@@@@@

0
@@@e

Fig. 1. (to be cont'd.)

![](/api/attachments/HRAYTSJ2/fulltext/images/b7d218ec999ff93c7006b2bddb9e2c70fae4176d3563bbb2deb894f76b6cd303.jpg)  
Fig. 1. (cont'd.) Communication between DM1 and NEGO in Iteration 1.

sources of information, all inputs of DM1 are marked by @@@@@ printed on their right side. From the printout, it follows that DM1 changed one “want” into the demand (describing the attribute BONUSES PROD.) and added a new demand. The wants and demands of DM1 in interation 1 are presented in the last table of the printout. Those of DM2 and DM3 are given in Table 3.

![](/api/attachments/HRAYTSJ2/fulltext/images/3d695591c3e034ad6a267cef1fcb5909a2a328e50d89d5791c3fdb180de58878.jpg)  
Fig. 2. Decision Proposals.

Table 4  
Wants and Demands and the Compromise Decision.

<table><tr><td>No.</td><td>Name</td><td>W. &amp; D. of DM1</td><td>W. &amp; D. of DM2</td><td>W. &amp; D. of DM3</td><td>The Compromise</td></tr><tr><td>1</td><td>WAGES PROD.</td><td>MAX 10.0</td><td>LE 13.5</td><td></td><td>13.500</td></tr><tr><td>2</td><td>BONUSES PROD.</td><td>MAX 1.2</td><td></td><td>LE 2.9</td><td>2.345</td></tr><tr><td>3</td><td>PROFIT PROD.</td><td>GE 7.5</td><td></td><td></td><td>9.725</td></tr><tr><td>4</td><td>TOTAL PROFIT</td><td></td><td>MAX 15.8</td><td></td><td>17.925</td></tr><tr><td>5</td><td>EXPORT</td><td></td><td>MAX 21.0</td><td></td><td>24.075</td></tr><tr><td>6</td><td>WAGES SERV.</td><td>LE 9.8</td><td>LE 10.0</td><td>MAX 7.5</td><td>7.647</td></tr><tr><td>7</td><td>PROFIT SERV.</td><td>LE 8.2</td><td></td><td>GE 8.0</td><td>8.200</td></tr></table>

DMs can see all proposals in a graphic form, as shown in Fig. 2. It describes the computer output for DM1 after iteration 1. In iteration 2, DMs reformulate wants and demands so that a compromise can be achieved – see Table 4.

Fig. 3 shows the negotiating process. Because in the example we have only two decision variables we show how negotiations were carried on in decision space. The polygon ABCDEFO is a set of feasible solutions, i.e. such decisions which can be enforced by the enterprise. The intervals [B, C], [C, D] and [D, E] are the efficient frontier which covers all nondominated solutions.

In real-life problems, there are many more variables than 2 so it is not possible to draw such a graph. However, using multidimensional scaling, it is possible to show the process in the objective space and to give DMs additional information. Such a graph can be plotted after every two to three iterations by the service virtual machine so DMs can see their achievements.

![](/api/attachments/HRAYTSJ2/fulltext/images/29beb30fe1d9ea8cfb079e7a83688f31b506a7711000a5b0bfd4bf238ffecaa4.jpg)  
Fig. 3. The Negotiating Process for the Example Described (for Captions, see Fig. 5).

From Fig. 3, it follows that the compromise decision is a dominated solution. Thus there are solutions (from interval [C, D]) for which some objective performance levels are higher than those achieved in the compromise and others are not. However, a problem arises, because if we choose any such solution, we violate DMs' demands.

The process of negotiations depends on the group of DMs; NEGO allows any kind of strategy. While testing the system we had a DM3 who was tough; for two iterations, he did not change his position. At this same session, the DM2 bluffed in iteration 1. The group pressed DM1 to make total concessions larger than in the previous example, despite the fact that he was cautious and unwilling to make bigger ones. The negotiating process for this group is presented in Fig. 4; in this case, the compromise is a nondominated solution. There, the mean values and compromise proposals have been omitted to make the example clearer.

![](/api/attachments/HRAYTSJ2/fulltext/images/3f3b27ebbd6281f485bf962d23280a81ee4287f8c5032b97728718db6a4e33a8.jpg)  
Fig. 4. Another Possible Negotiating Process. (For Captions, see Fig. 5).

![](/api/attachments/HRAYTSJ2/fulltext/images/81d53d457223d9da332cfb6d79cebf42aa6fefd55da38ccce56f62144fa20c33.jpg)  
Fig. 5. Captions for Figs. 3 and 4.

## 5. Conclusions

The procedure and NEGO were constructed to solve group decision problems which emerged in Polish companies after the economic reform had been introduced in 1980-1981. Our aim was to help company executives and representatives of trade unions and workers' sef-governments to learn how to negotiate problems of production planning and profit distribution. Two case studies were used in management development courses; one describing POLUNI – a company producing refrigerators and freezers [7], and one describing an anonymous industrial enterprise [6]. For each course one case study was chosen.

During two months NEGO was used in five courses. The majority of participants evaluated it highly; they pointed out that courses confront DMs with the necessity to make concessions, that NEGO visualizes correlations among different objectives and different interests. The participants mentioned that negotiations often fail, especially when some DMs are not professionals: the case of Polish representatives of workers' self-governments and trade unions. NEGO helps participants to focus on the main points and to obtain a clear picture of the negotiating process.

We expected that after several courses it would be possible to port NEGO into the real-life environment, however, its use had to be limited due to the lack of computer systems in the majority of Polish companies. One of the participants, the

Managing Director of the largest Polish chocolate factory “E. Wedel” invited us to build a GDM model and to port NEGO to a Polish computer. The problem concerns negotiations among administration, workers’ self-government and trade unions regarding a one year production and distribution plan.

The use of NEGO is not restricted to the above type of problems. Our experience shows that it can be of assistance in solving different GDM problems that can be modelled as MOLP problems. However, it does not seem useful for solving problems with two decision makers who have the same objective but different criteria (such as pure wage bargaining). NEGO seems an appropriate tool when there are more objectives, when a DM can try to win his case through different approaches (changing wants and/or demands), e.g. when apart from wages there are other features in the negotiating package (work week, a share in profits, fringe benefits).

Long-term planning and policy formulation problems are usually difficult and involve a group of DMs. Negotiations between industry and government on energy policy, described in the Austrian model [4], or the problem of job creation in the private sector could possibly be solved with the help of NEGO.

## Acknowledgements

The author wants to thank Jan Janczyk from Computer Science Department of the Management Development and Organization Institute for his essential contribution to NEGO software development.

Thanks also go to Dr. Edgar H. Sibley, the editor of this Journal, and to Dr. Jeff Sidney from the Faculty of Administration of the University of Ottawa for their help in final editing of the paper.

## References

[1] K. Arrow, Social Choice and Individual Values, Yale Univ. Press, New Haven, 1963.

[2] J.L. Cohon, Multiobjective Programming and Planning. Academic Press, New York, 1978.

[3] M. Freimer and P. Yu, "Some New Results on Compromise Solutions for Group Decision Problems", Management Science, No. 22, 1976.

[4] M. Grauer, E. Bishchoff and A. Wierzbicki, “Mediation in Long-Term Planning”, in Y.Y. Haimes and V. Chanking (eds.), Proceedings of the VIth International Conference on Multiple-Criteria Decision Making, Springer-Verlag, Berlin (in print).

[5] J. Harsanyi, “Cardinal Welfare, Individualistic Ethic and Interpersonal Comparison of Utility”, Journal of Political Economy, No 63, 1955.

[6] H. Kasprzyca, G.E. Kersten and A. Olszewska, "Production Planning and Profit Distribution", Course Book, Management Organization and Development Institute, IOZIDK, Warsaw, 1984.

[7] G.E. Kersten, "An Interactive Procedure for Solving Group Decision Problems", in V. Chankong and Y.Y. Haimes eds.), Proceedings of the VIth International Conference on Multiple-Criteria Decision Making, Springer-Verlag, Berlin (in print).

[8] G.E. Kersten, A Procedure and a Computer Package for Group Decision Making", Working Paper 85-18, University of Ottawa, Faculty of Administration, Ottawa, 1985.

[9] P. Korhonen, J. Wallenius and S. Zionts, Two Interactive Procedures for Solving Multicriterion Optimization With Multiple Decision Makers, Univ. Of Jyvaskyala, Working Paper 14, Jyvaskyala (Finland), 1982.

[10] J.G. March and H.A. Simon, Organizations, John Willey, New York, 1958.

[11] H. Raiffa, Decision Analysis, Addison-Wesley, Reading, 1968.

[12] A. Rapoport, N-Person Game Theory, Univ. of Michigan Press, Ann Arbor, 1970.

[13] R. Selten, “The Equity Principle in Economic Behaviour”, in H.W. Gottinger and W. Leinfelder (eds.) Decision and Theory and Social Ethics, Dordrecht, 1972.

[14] A. Sen, Collective Choice and Social Welfare, Holden-Day, San Francisco, 1970.

[15] R.E. Steuer, Operating Manual for ADBASE/FILTER Computer Package for Solving Multiple Criteria Programming Problems, Univ. of Kentucky, 1978.

[16] R. Tietz (ed.) Aspiration Levels in Bargaining and Economic Decision Making, Springer-Verlag, Berlin, 1983.

[17] A.P. Wierzbicki, Interactive Decision Analysis and Interpretative Computer Intelligence, International Institute for Applied Systems Analysis, Laxenburg (Austria), 1984.

[18] S. Zionts and J. Wallenius, “An Interactive Multiple Objective Linear Programming Method for a Class of Underlying Nonlinear Utility Functions”, Management Science, No. 5, 1983.
