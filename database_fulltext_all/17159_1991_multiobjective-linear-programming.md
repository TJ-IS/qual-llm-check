---
otero_id: 17159
otero_key: "VWGVVFMG"
title: "Multiobjective linear programming"
authors: "Moshe Dror; Peretz Shoval; Alexandra Yellin"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90039-e"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Multiobjective linear programming Another DSS

Moshe Dror, Peretz Shoval and Alexandra Yellin \*

Departement of Industrial Engineering and Management, Ben Gurion University of the Negev, Beer-Sheva 84105, Israel

The paper presents an interactive menu driven decision support system for Multiobjective Linear Programming (MOLP) problems. The main contribution of the system lies in the ease of interaction between the decision maker (DM) and the system which is achieved, in contrast with other systems, by DM directed construction of a weak order on system variables and objectives. In the interactive stage the DM points out which objective functions are to be improved relative to the candidate solutions presented. No tradeoff evaluations are required from the DM. In addition, priorities/preferences of variables and objectives can be modified throughout the solution process.

Keywords: Interactive multiobjective optimization.

![](/api/attachments/VWGVVFMG/fulltext/images/428f00cda82889f26f28f34b88caa6209075710de8199dbe810ddd56356d3124.jpg)

Moshe Dror is a Senior Lecturer in the Industrial Engineering and Management Department at Ben Gurion University of the Negev and an Invited Researcher in Centre de recherche sur les transports at the Université de Montréal. He held visiting appointments at the Université du Quebec (INRS-Telecommunications) and University of Lancaster. He received an M.Sc. degree in Mathematical Methods in Engineering and an I.E. (Prof.) degree in Industrial En gineering, both from Columbia University, and a Ph.D. degree in Management Science from University of Maryland at College Park. His publication appeared in over eighteen professional refereed journals such as Management Science, Networks, and Naval Research Logistics. His research interests include combinatorial optimization applications in production, logistics, and communications. He is a member of ORSA and a Vice-President of ORSIS (Operations Research Society of Israel).

\* Correspondence to Moshe Dror, Decision Sciences, College of Business, The University of Arizona, Tucson, AZ 85721, USA. The authors would like to acknowledge the support by Paul Ivanir Center for Robotics and Production Research of the Ben-Gurion University of the Negev.

## 1. Introduction

Multiobjective optimization problems encompass a very large class of practical planning situations for which an operational work plan (a solution) has to be constructed, accounting simultaneously for a number of conflicting objectives. Multiobjective Linear Programming (MOLP) problems are a subset of the above for which the objectives and the functional relations among the variables and constraints can be described (or closely approximated) in the form of linear mathematical relations.

![](/api/attachments/VWGVVFMG/fulltext/images/b9af3bfbf6938ffb8abe6eda2fada59472ee38f9ae2bf7c24123e832c2c272f7.jpg)

Alexandra Yellin is an adjunct lecturer and a departmental engineer in the Industrial Engineering and Management Department at Ben-Gurion University of the Negev. She received B.Sc. and M.Sc. degrees from the Industrial Engineering Department at Ben-Gurion University. She has published in the European J. of Operational Research.

![](/api/attachments/VWGVVFMG/fulltext/images/f4515ea5af915a59d02ce69b4a39811be24b38c0ff439c41439882bf763916b7.jpg)

Peretz Shoval is Senior Lecturer of Computer & Information Systems in the Department of Industrial Engineering & Management at Ben-Gurion University of the Negev in Israel. Previous affiliations include Tel-Aviv University and Hebrew University of Jerusalem. He received B.A. (Economics) and M.Sc. (Information Systems) from Tel-Aviv University, and Ph.D. (Management Information Systems) from the University of Pittsburgh. Dr. Shoval's research and teaching interests include systems analysis and design methodologies database design, expert systems for information retrieval, and economics of computing. He has published in journals such as Information Systems, Information & Management, Information Processing & Management, Int'l Journal of Man-Machine Studies, Data & Knowledge Engineering, Information & Software Technology and Data Base. Prior to moving into academia Dr. Shoval held managerial and consulting positions in computer companies and in the IDF.

Mathematically, MOLP's can be represented as

$$
\begin{array}{l l} \text {‘Max’} & C x \\ \text {subject to} & A x = b, \\ & x \geq O, \end{array}
$$

where C and A are respectively $k \times n$ and $m \times n$ matrices, b is an $m \times 1$ vector and x is an $n \times 1$ vector of decision variables. The problem consists of n decision variables, m explicit constraints and k explicit objectives. All the relations in the above mathematical model are assumed to be linear. The ultimate goal of the MOLP solution methods is to find the most preferred nondominated solution. (A nondominated solution is a solution for which there is no other solution which attains as good a value for all the objectives and a better value for at least one objective.)

Since any solution to such problems has to be evaluated primarily through the values of the objective functions – vector of solution values, no simple (uniquely defined) outcome can be expected by the mere application of mathematical solution procedures. For example, given the objectives of maximizing both the profit and the market share of a company, there might be a number of 'good' solutions, some promising greater profit with smaller market share and some the opposite. It is not immediately apparent how one can compare among such solutions based purely on their numerical values. If we add to this difficulty the fact that no mathematical model, no matter how elaborate, can ever be a perfect representation of reality, and the necessity of subjective evaluation of the potential outcomes (as in the above profit\ market share example) by the parties (decision makers) involved in the planning process, we can perhaps grasp the complexity of finding the 'best' solution in a MOLP setting. Realizing the need for scientifically based tools to facilitate the solution of complex practical planning problems, the academic community in the area of Operations Research/Management Science has invested a considerable effort over the last 25 years in the understanding and development of computer-based interactive systems for such problems. Setting aside for the moment the mathematical and computer science foundation for interactive MOLP systems, the acid test of any such system is the ability and the willingness of the decision maker(s) (DM) to use it as an integrative part of his planning process. The objective of any system (computerized or not) designed to aid the planner(s) in generating solutions to operational or design problems, is to serve the user. Creation of user-friendly interactive systems is directed to facilitate this service to the user.

Difficulties encountered in the commercial introduction of an MOLP interactive systems originate primarily in the excessive assumptions as to the ability of the DM to understand and appropriately respond to questions encountered in an interactive solution process, not to mention the time requirements of the interactive stage.

We assume from the outset that for realistic planning and design problems, the solution process requires a technical function of an analyst and a function (inputs) of a decision maker. The difficulty the analyst encounters is mainly related to the mathematical methodology and the algorithmic developments necessary to ensure efficient generation of solutions in the MOLP setting. Since interaction with the DM is intrinsic to the solution procedure, the analyst has to decide on the format such interaction should take based on his familiarity with (and confidence in) the decision theory processes such as the utility theory, game theory, analytic hierarchy, fuzzy set theory, or some other theory of decision processes. The interactive stage usually represents the Achilles' heel of the entire system, because of the DM's inability and unwillingness to respond adequately relative to the analyst's expectations which are based on the decision theory processes he assumed while designing the system. Typical questions subsequently forwarded to the DM are: "Ask the DM which objective he (she) intends to increase (decrease)."; "Ask the DM if he (she) intends to decrease some objective in order to increase some other objective."; "Ask the DM by how much he is willing to decrease an objective."; "Ask the DM to rank a whole set of alternative solutions."; "Ask the DM to make pairwise comparison between the alternatives."; "Ask the DM if he intends to modify the marginal utilities."; "Ask the DM to reorder his alternatives involved in inconsistencies."; "Ask the DM to review the MOLP model." All those questions originate from the simple fact that in MOLP (or any multiobjective optimization model) the DM is examining vector(s) of objectives' values in an imperfect interpretation/translation of the operational environment in terms of a mathematical model.

In that context the most promising solution approach lies in the exploitation of the present state of the art in information processing technology and its interface with the decision maker's decision process, i.e. the creation of Decision Support Systems – DSS. Such systems provide support for planning activities in that they examine alternative solutions by integrating human perception and computerized algorithms in an interactive environment. The importance of developing DSS in the context of solving MOLP's has been recently reiterated by a number of authors (Siskos and Despostis, 1989 [11], Slowinski and Teghem, 1988 [12]).

Without reviewing the present interactive MOLP systems in detail (for such a review see Slowinsky, I, II, 1984 [14]), we outline some principles and properties common to the great majority of such systems. Most of the existing interactive MOLP systems restrict the DM's feedback/evaluation to the objective functions' values, i.e., the examination of the solution is limited to the criteria space. It is usually assumed that the explicit mathematical model fully captures all the relevant information about the operational environment. That kind of approach does not infer that there might be other objectives, preferences, and constraints which are not represented by the mathematical model. The common assumption is that the DM has some preference function (implicit or explicit) defined on the criteria space and usually in such cases local information is requested in the interactive stages in terms of this criteria preference function in order to carry out the search for the most preferred solution. (See for example Zionts and Wellenius, 1976 [17], Geoffrion et al. 1972 [6], Siskos and Despotis, 1989 [11]). For instance, in Siskos and Despotis, 1989 [11], (among others) the DM is required to determine the marginal rate of substitution in the criteria space at the point of the candidate solution and also he is required to indicate the step size in the direction of the desired solution. The number of different questions the DM is expected to comprehend and respond to in a consistent manner can easily exceed ten at one interactive cycle. When we examine the interface structure of the interactive step in such MOLP systems, we discover that it does not conform with basic guidelines for building a successful DSS (see Barbosa and Hirko, 1980 [1]). Praticability is usually played down in the literature of interactive MOLP's. We know that in a properly constructed DSS the DM needs only to be concerned with those elements of the problem which relate directly to the problem solving process (i.e., objectives, objective values, variables, constraints). Asking the DM to evaluate attributes, supply marginal substitution rates, or determine descent step sizes, etc., are clearly outside the DM's focus in his search for a preferred solution. Thus, from the outset an important question one should ask is, for whom has the interactive MOLP system been designed? Is it for the analyst or the DM?

The DSS based interactive MOLP system described in this paper attempts to conform very closely with the basic requirements from a friendly DSS. The premise and mode of its operation are quite different from existing interactive MOLP systems. The system's development follows closely the ideas outlined in a number of papers (Gass and Dror, 1983 [5], Dror and Gass, 1987 [3], Dror et al. 1988 [2]). Its premise is based on simplicity of interaction with the DM, relating only to those elements directly addressing the solution and the solution process.

The model behind the system does not assume any specific utility structure nor does it assume perfect interpretation of the environment by the problems objectives, constraints, variables and functional relations. The interaction with the DM starts very early in the modeling stage, where some preference structure of variables and objectives (weak order) is extracted from the DM in a “friendly” and simple form.

Without describing the details of the methodology developed by us for solving MOLP problems (Gass and Dror, 1983 [5], Dror and Gass, 1987 [3], Dror et al. 1988 [2], Teghem et al. 1986 [16]), we will just outline the solution stages.

In the first stage some preference measure for solutions is constructed with help from the DM. Later this is applied only to the nondominated solutions. This preference structure can be changed very easily during the solution process. Candidate solutions based on this preference measure are generated one at a time. Then in the iterative stage, the DM examines the candidate solution together with the “ideal solutions” – a vector of single objective optimization values representing the best possible outcome in each objective. In addition, the DM is presented with the previously examined nondominated solution. The DM just indicates his dissatisfaction in terms of objectives directly. No additional information such as trade-offs, step size, descent (ascent), etc., is required from the DM. The mechanics of generating solutions might be quite sophisticated, (using procedures partly based on algorithms developed by Ecker et al. 1980 [4]), but the mechanics have no impact on the DM's interaction. The number of different questions which might occur during the interactive stage does not exceed three.

## 2. Review of Existing Interactive MOLP Systems

A typical interactive MOLP system can be viewed as consisting of the following stages:

(1) Input the problem parameters into the system. (Essentially this is a technical component concerning only the analyst.)

(2) Generate a candidate solution (feasible and nondominated) or a small set of solutions.

(3) Interact with the user. The DM is questioned by the analyst during this interactive stage, and a decision is made whether to generate new solutions, and if so how a new candidate solution is to be computed.

(4) Generate new improved solution(s) from the present solution(s) after the interaction with the DM in stage 3.

We will examine some existing MOLP interactive systems. The systems examined in this section are: Slowinski, 1986 [13], Teghem et al., 1986 [16], Siskos and Despotis, 1989 [11], and Korhonen, 1987 [7].

The systems developed by Slowinski, 1986 [13] and Teghem et al. 1986 [16] represent the current trend in the development of Interactive Multiobjective Programming Models which account for the uncertainty inherent in many long range planning problems as far as the parameters, objectives and aspiration levels. In some sense, comparing these models with their deterministic counterparts is like comparing different species. A comparison of these two interactive decision support systems is described in Slowinski and Teghem, 1988. These systems are better suited for a user of high mathematical sophistication. A busy DM who is concerned with the outcome of the decisions and has neither the knowledge nor the time to study the meaning of fuzzy numbers with their underlying theory or topics in stochastic mathematical programming, might find successful implementation of the above systems difficult. Still, the motivation behind the development of the interactive MOLP which accounts for uncertainty is very real even when most of the technological coefficients are considered deterministic (i.e., some coefficients/parameters might be more certain than others influencing the DM's implicit preference structure).

The DSS for MOLP developed by Korhonen, 1987 [7], under the title VIG (we have the 2.20-99 version of this system) has been marketed already for some time. It is based on a number of articles by Korhonen and Laakso, 1986a, 1986b [8], [9], Korhonen and Wallenius, 1986 [10], and other work of Korhonen and his colleagues. This system is aimed primarily at the academic community since it limits the problems to no more than 100 variables and the number of constraints is limited by 100 minus the number of objective functions. Though it promises to be very supportive in terms of human interaction, when actually experimenting with the system we had some difficulty navigating the system successfully towards a solution. The developers of the system attempted in a sense to eliminate the analyst in the interactive stage which by itself would be a great attribute of such a system. Still, since the average DM is not that fluent in the underlying methodology he needs “his hand held” by an analyst in terms of developing confidence as to the solutions being proposed to him.

When we examine the system proposed by Siskos and Despotis, 1989 [11], which the authors developed on the pattern of the DSS oriented system, we are puzzled by the cognitive load imposed on the DM during the interactive step. Going through their “Step-by-Step Navigation through the Method”, we counted more than ten different questions which the DM encounters in his search for the preferred solution. These questions ask if the DM “intends to decrease some thresholds in order to increase an objective”, “they tell the DM to indicate acceptable decrements”, rank alternatives, perform pairwise comparisons, understand a utility ranking diagram, modify marginal utilities, etc. For some decision-makers in some problem instances, such a system may be well suited. Its general applicability, however, is less certain.

## 3. The New Interactive MOLP

The DSS based interactive MOLP system presented in this paper attempts to overcome some of the difficulties and pitfalls mentioned above. It emphasizes a user-friendly interface which is flexible and requires simple reactions from a DM, while exploring the solution space of the MOLP problem. It appears to require relatively few interactive steps and offers considerable insights into the DM's perspective.

## 3.1. General Structure

The main point of the system is that it is aimed to be used by decision makers who are not necessarily analysts. Therefore it assumes a user having minimum “technical” skills. He has to be familiar with basic terms, such as objective function, variables and constraints, and he needs to specify preferences/priorities of objective functions and variables. (Note: talking to DMs in the field, we found that for the DM specifying preferences on variables and objectives is a very easy and natural task). Based on this preference structure the system can generate candidate solutions and the user has to express his opinion regarding the fitness of a solution and indicate which function he wants to improve. In the process he guides the system to search for better solutions, until satisfaction is achieved.

Three major stages can be identified in the system, as shown in fig. 1, which is its general flowchart. In the first stage, the user specifies the problem (i.e., enters the objective function and constraints) and the system computes the “ideal solutions”. In the second stage, the user is asked to specify his preferences between the decision variables and between the objective functions. Consequently, the system searches for the most preferred solution (the candidate solution) and presents it to the user. The third stage is an iterative process of improvements, in which the user guides the system by specifying which objective function he wants to improve, and also by changing his preferences in terms of decision variables and objectives. The system reacts by searching for the next solution which conforms with the new preferences, until either the user is satisfied with the new solution, or, the system proposes a “compromise solution” if a cycle (of solutions) has been generated. (For details see Dror et al., 1988 [2]). If a compromise solution cannot be proposed, due to the fact that the cycle does not occur at the extreme points of one efficient face, the DM has two options: (a) to choose from one of the previous candidate solutions. (b) to run the system again with new preferences.

Before going into further discussion of the system, some points regarding runs on PC and PS/2 microcomputers (under DOS), requiring at least 128K of memory and a math-coprocessor. The system can also run on any other computer which has APL.

## 3.2. Stage 1: Specify the Problem and Find "Ideal" Solutions

In this stage the user need not be the DM; it can be the analyst who formulates the objective functions and constraints, or an assistant. The DM will become active only when a solution is desired. The user can enter a new problem specification or load an existing one (that has been entered and saved earlier). She/He can also update (change) the new or existing problem; i.e., add, change, or delete functions and constraints, before it is solved by the system, or she/he can delete an old problem.

The process of entering or updating a problem is interactive, and driven by standard menus and question-answering. When specifying a problem, the user first enters the number of variables. Then, for each function he specifies its type (Min/Max) and the coefficients. Similarly, for each constraint he specifies the equality/inequality. The user can review the existing functions and constraints any time before the solution process begins (or he may just save the problem, to be solved later with the decision maker present). To simplify the task the system attaches ID numbers to the functions and constraints, to be used during the interaction.

When the DM decides that he wants a solution, the system checks if there are any feasible solutions. If a feasible solution exists, the system computes the “ideal solutions”, and then the second stage begins.

![](/api/attachments/VWGVVFMG/fulltext/images/74eb15fb0f7c698f7d21af18a324a94082e467a66c4b3d036ec3c04cde5826d1.jpg)  
Fig. 1. System flowchart.

```javascript
F1: (revenue) max 375x1+150x2+400x3+160x4+420x5+175x6+400x7+150x8
F2: (profit) max 179.95x1+82.9x2+153.08x3+72.15x4+129.95x5+69.9x6+208.5x7+83x8
F3: (market share) max .25x1+.1x2+.25x3+.1x4+.25x5+.1x6
F4: (production) max x1+x2+x3+x4+x5+x6+x7+x8
F5: (utility) max 1.65x1+.9x2+1.975x3+1.03x4+1.75x5+.94x6+4.2x7+1.06x8
```  
Fig. 2. The formulation of objective functions.

For illustration, we present an example, taken from Tabucanon, 1988, pp 202–206. It deals with a company that manufactures various types of chocolate bars, candies and wafers. It has the production and marketing capability to produce and sell all or a mixture of products, and the problem is to determine the product mix and the quantities of each product. Eight variables are identified (the quantities are in thousands of units or packs of the eight different products).

$(x_{1})$ Milk chocolate bars, 250 gm.

$(x_{2})$ Milk chocolate bars, 100 gm.

$(x_{3})$ Crunchy chocolate bars, 250 gm.

$(x_{4})$ Crunchy chocolate bars, 100 gm.

$(x_{5})$ Chocolate with nuts, 250 gm.

$(x_{6})$ Chocolate with nuts, 100 gm.

$(x_{7})$ Chocolate candies, 300 gm.

$(x_{8})$ Chocolate wafer, 10 gm., 2 unit pack.

There are five simultaneous objective functions: (a) Maximize revenue, (b) Maximize profit, (c) Maximize market share of chocolate bar products, (d) Maximize units of products produced, and (e) Maximize machinery utilization. Regarding constraints, there are four types of constraints: Constraints on production resources, on the variety of the product sizes (weights), on the variety of product types, and on the demand. Without going into details we assume that there are four DMs, who represent four different “interests”/objectives: economic (objective functions 1 & 2), marketing (objective function 3), advertising (objective function 4) and production (objective func tion 5). In the first stage, the user formulates the five objective functions, and the constraints. These are shown in figs. 2 and 3, respectively.

```txt
constraints on production resources:
(pots) .5x1+.2x2+.425x3+.17x4+.35x5+.14x6+.6x7+.09x8≤1000
(mixing) .15x3+.06x4+.25x5+.1x6≤200
(molds) .75x1+.3x2+.75x3+.3x4+.75x5+.3x6+.9x7+.36x8≤1500
(grinding) .25x3+.1x4≤200
(waffers) .1x1≤100
(cutting) .1x1+.1x2+.1x3+.1x4+.1x5+.1x6+.1x7+.2x8≤400
(packaging 1) .25x1+.25x3+.25x5+.1x8≤400
(packaging 2) .05x1+.3x2+.05x3+.3x4+.05x5+.3x6+2.5x7+.15x8≤1000

constraints on size mixture:
x1≤x2
x3≤x4
x5≤x6

constraints on product mixture:
400x7+150x8-56.25x1-22.5x2-60x3-24x4-63x5-26.25x6≤0

constraints on demand:
x1≤800
x2≤1000
x3≤750
x4≤800
x5≤500
x6≤800
x7≤400
x8≤1000
```  
Fig. 3. The formulation of the constraints.

## 3.3. Stage 2: Specify Priorities and Find Candidate Solution

At this stage the DM is asked to specify the Preference of the variables and the objective functions (i.e., establish a weak order on the variables and a weak order on the objectives). According to these preferences the DM will be presented with the initial candidate solution.

The process of extracting the preferences from the DM begins by presenting an explanation of how the process works. The DM is asked to specify groups of variables and later groups of objectives. The first group of variables is considered to be preferred to the second group and so on. Once all variables (functions) are classified into major groups, in the subsequent pass the user is given an option to refine these initial preferences by specifying preferences of variables within each of the major groups.

In our example, the user defined two major preference groups of variables:

\- the first preference group included: $x_1, x_2, x_3, x_4, x_5, x_6$ (Milk chocolate bars 250 & 100 gm., Crunchy chocolate bars 250 & 100 gm., Chocolate with nuts 250 & 100 gm.)

\- the second preference group included: $x_{7}$ , $x_{8}$ (Chocolate candies, Chocolate wafers).

Then, within the first group of variables the user indicated two sub-groups:

\- the first sub-group included: $x_{1}$ , $x_{3}$ , $x_{5}$ (Milk Chocolate bars 250 gm., Crunchy chocolate bars 250 gm., Chocolate with nuts 250 gm.)

\- the second sub-group included: $x_{2}, x_{4}, x_{6}$ (Milk chocolate bars 100 gm., Crunchy chocolate bars 100 gm., Chocolate with nuts 100 gm.)

No further refinement within these groups were made, nor any refinements in the second major group.

Regarding the objective functions they were likewise partitioned into two major groups:

\- the first preference group included: f1, f2 (revenue and profit)

\- the second preference group included: f3, f4, f5 (market share, production, utility).

No further refinements were made regarding the objective functions groups.

After having specified the preferences, the system establishes a preference measure for solutions (described in detail in Dror and Gass, 1987). Then it generates the most highly ranked nondominated solution, which can be reached from an initial starting point (the highest rank ideal solution) by moving on a path of steepest ascent. This is the initial candidate solution presented to the DM.

THE IDEAL THE PREVIOUS AND THE PRESENT VALUES OF THE OBJECTIVE VALUES

<table><tr><td></td><td>IDEAL</td><td>PREV</td><td>PRES</td><td></td></tr><tr><td>F1=</td><td>791600.00</td><td></td><td>776360.66</td><td>(revenue)</td></tr><tr><td>F2=</td><td>368227.84</td><td></td><td>366741.28</td><td>(profit)</td></tr><tr><td>F3=</td><td>500.00</td><td></td><td>478.85</td><td>(market share)</td></tr><tr><td>F4=</td><td>3710.53</td><td></td><td>3545.90</td><td>(production)</td></tr><tr><td>F5=</td><td>4415.10</td><td></td><td>4241.00</td><td>(utility)</td></tr><tr><td colspan="5">HITTO CONTINUE</td></tr><tr><td colspan="5">THE VALUES OF THE VARIABLES</td></tr><tr><td>X1=</td><td>800</td><td colspan="3">(milk chocolate bars 250 gm.)</td></tr><tr><td>X2=</td><td>1000</td><td colspan="3">(milk chocolate bars 100 gm.)</td></tr><tr><td>X3=</td><td>75.41</td><td colspan="3">(crunchy chocolate bars 250 gm.)</td></tr><tr><td>X4=</td><td>800</td><td colspan="3">(crunchy chocolate bars 100 gm.)</td></tr><tr><td>X6=</td><td>800</td><td colspan="3">(chocolate with nuts 100 gm.)</td></tr><tr><td>X7=</td><td>70.49</td><td colspan="3">(chocolate candies 300 gm.)</td></tr></table>

Fig. 4. Presentation of initial candidate solution.

## 3.4. Stage 3: Iterative Improvements

This is stage is based on iterative moves in which the system presents a candidate solution to the user, the user is asked to judge it, guiding the system to search for a better solution, until satisfaction is achieved. Any candidate solution generated by the system is presented on two screens. On one it shows the values of the objective function, and on the other – the values of the variables of the solution. The user can switch from one screen to the other before he decides on the next move. The objective function screen consists of three columns: the “ideal”, the previous, and the current solution. This makes it easy for the DM to see how far he is from the “ideal” (in each function) at each iteration, and how the solution has changed relative to the previous solution.

Returning to the example, fig. 4 shows the preferred solution (values of the functions and variables) which is suggested by the system as the initial candidate. Note that the “previous” column is blank.

At this stage the user/DM reviews the solution and is asked to determine which objective function(s) he would like to improve most. Note that the DM can indicate more than one objective function. Once he enters the appropriate function numbers, he is asked if he would also want to change the preferences of variables and objectives (as he did in Stage 2).

Now the system checks whether there is a new solution adjacent to the existing one, which improves the functions indicated by the DM. There are three possible cases: (a) there is no adjacent solution which improves the functions indicated by the DM. In this case the system notifies the DM and gives him an opportunity to enter a new selection while indicating his previous choice. (b) There is more than one new solution improving the functions indicated by the DM. In this case the system will choose the highest ranking solution according to the latest preference structure chosen by user. (c) All improvements in the direction indicated by the DM have already been reviewed. In other words, there are solutions of the type indicated by the DM but none of them are new. In this case the system will check for a compromise nondominated solution if such exists. The compromise solution, which is no longer an extreme solution, is a weighted average (according to their preference measure) of the candidate solutions which formed the closed loop.

Let us now return to the example and assume that after having reviewed the first solution, the DM decides that he wants to improve revenue (objective function 1), with no changes in preferences. The system finds a new solution, which is presented in fig. 5. As it shows, revenue increased, but at the same time profits (function 2) decreased.

After analysing the new results, the DM decides to improve profits (again, without changing preferences). The new results are shown in fig. 6.

Since there is only a slight increase (0.1%) in profit (f2), in spite of decrease in machinery utili-

THE IDEAL THE PREVIOUS AND THE PRESENT VALUES OF THE OBJECTIVE VALUES

<table><tr><td></td><td>IDEAL</td><td>PREV</td><td>PRES</td><td></td></tr><tr><td>F1=</td><td>791600.00</td><td>776360.66</td><td>786475.41</td><td>(revenue)</td></tr><tr><td>F2=</td><td>368227.84</td><td>366741.28</td><td>355869.94</td><td>(profit)</td></tr><tr><td>F3=</td><td>500.00</td><td>478.85</td><td>478.85</td><td>(market share)</td></tr><tr><td>F4=</td><td>3710.53</td><td>3545.90</td><td>3545.90</td><td>(production)</td></tr><tr><td>F5=</td><td>4415.10</td><td>4241.00</td><td>4372.49</td><td>(utility)</td></tr><tr><td colspan="5">HITTO CONTINUE</td></tr><tr><td colspan="5">THE VALUES OF THE VARIABLES</td></tr><tr><td>X1=</td><td>395.41</td><td colspan="3">(milk chocolate bars 250 gm.)</td></tr><tr><td>X2=</td><td>1000.00</td><td colspan="3">(milk chocolate bars 100 gm.)</td></tr><tr><td>X3=</td><td>480.00</td><td colspan="3">(crunchy chocolate bars 250 gm.)</td></tr><tr><td>X4=</td><td>800.00</td><td colspan="3">(crunchy chocolate bars 100 gm.)</td></tr><tr><td>X6=</td><td>800.00</td><td colspan="3">(chocolate with nuts 100 gm.)</td></tr><tr><td>X7=</td><td>70.49</td><td colspan="3">(chocolate candies 300 gm.)</td></tr></table>

Fig. 5. First improved solution.

THE IDEAL THE PREVIOUS AND THE PRESENT VALUES OF THE OBJECTIVE VALUES

<table><tr><td>IDEAL</td><td>PREV</td><td>PRES</td><td></td></tr><tr><td>F1= 791600.00</td><td>786475.41</td><td>790000.00</td><td>(revenue)</td></tr><tr><td>F2= 368227.84</td><td>355869.94</td><td>356394.40</td><td>(profit)</td></tr><tr><td>F3= 500.00</td><td>478.85</td><td>500.00</td><td>(market share)</td></tr><tr><td>F4= 3710.53</td><td>3545.90</td><td>3560.00</td><td>(production)</td></tr><tr><td>F5= 4415.10</td><td>4372.49</td><td>4216.00</td><td>(utility)</td></tr><tr><td colspan="4">HITTO CONTINUE</td></tr><tr><td colspan="4">THE VALUES OF THE VARIABLES</td></tr><tr><td>X1= 480.00</td><td colspan="3">(milk chocolate bars 250 gm.)</td></tr><tr><td>X2= 1000.00</td><td colspan="3">(milk chocolate bars 100 gm.)</td></tr><tr><td>X3= 480.00</td><td colspan="3">(crunchy chocolate bars 250 gm.)</td></tr><tr><td>X4= 800.00</td><td colspan="3">(crunchy chocolate bars 100 gm.)</td></tr><tr><td>X6= 800.00</td><td colspan="3">(chocolate with nuts 100 gm.)</td></tr></table>

Fig. 6. Second improved solution.

zation (f5) the DM decides to improve profits again. Now there is a substantial increase in profit (2.4%) and a slight decrease in revenue, but utilization of machinery decreased again (it is 93% of the ideal). (This iteration is not shown.) Consequently the DM decided to improve utilization. In this case he decides to change the preference as well. improve utilization. In this case he decides to change the preference as well. He decides to include variables 5 (chocolate with nuts 250 gm.) and 7 (chocolate candies) in the first group, and the rest of the variables in the second group. The grouping of the objectives are not changed. Without showing the results of this iteration, we only mention that the increase in utilization caused some decrease in revenue, so the DM decided to improve revenue again. Fig. 7 shows the results of this step. The new results show some decrease both in profit and in utilization.

The decrease in profit caused the DM to direct the system to improve f2 (profit). This time, however, the system found no new solution which improved profit. In other words, any such solution meant closing a loop. Therefore a compromise solution of all the solutions on the loop was given after it was checked for nondominance. The final compromise solution is presented in fig. 8.

THE IDEAL THE PREVIOUS AND THE PRESENT VALUES OF THE OBJECTIVE VALUES

<table><tr><td>IDEAL</td><td>PREV</td><td>PRES</td><td></td></tr><tr><td>F1= 791600.00</td><td>769842.11</td><td>781315.79</td><td>(revenue)</td></tr><tr><td>F2= 368227.84</td><td>367749.05</td><td>355417.14</td><td>(profit)</td></tr><tr><td>F3= 500.00</td><td>465.26</td><td>465.26</td><td>(market share)</td></tr><tr><td>F4= 3710.53</td><td>3710.53</td><td>3710.53</td><td>(production)</td></tr><tr><td>F5= 4415.10</td><td>4128.79</td><td>4277.95</td><td>(utility)</td></tr><tr><td colspan="4">HITTO CONTINUE</td></tr><tr><td colspan="4">THE VALUES OF THE VARIABLES</td></tr><tr><td>X1= 341.05</td><td colspan="3">(milk chocolate bars 250 gm.)</td></tr><tr><td>X2= 1000.00</td><td colspan="3">(milk chocolate bars 100 gm.)</td></tr><tr><td>X3= 480.00</td><td colspan="3">(crunchy chocolate bars 250 gm.)</td></tr><tr><td>X4= 800.00</td><td colspan="3">(crunchy chocolate bars 100 gm.)</td></tr><tr><td>X6= 800.00</td><td colspan="3">(chocolate with nuts 100 gm.)</td></tr><tr><td>x8= 289.47</td><td colspan="3">(chocolate wefer)</td></tr></table>

Fig. 7. Fifth improved solution.

<table><tr><td></td><td>Ideal</td><td>Final</td><td></td></tr><tr><td>F1=</td><td>791600.00</td><td>780789.47</td><td>(revenue)</td></tr><tr><td>F2=</td><td>368227.84</td><td>361138.35</td><td>(profit)</td></tr><tr><td>F3=</td><td>500.00</td><td>482.63</td><td>(market share)</td></tr><tr><td>F4=</td><td>3710.53</td><td>3635.26</td><td>(production)</td></tr><tr><td>F5=</td><td>4415.10</td><td>4183.68</td><td>(utility)</td></tr><tr><td>X1=</td><td>605.25</td><td colspan="2">(milk chocolate bars 250 gm.)</td></tr><tr><td>X2=</td><td>1000.00</td><td colspan="2">(milk chocolate bars 100 gm.)</td></tr><tr><td>X3=</td><td>285.26</td><td colspan="2">(crunchy chocolate bars 250 gm.)</td></tr><tr><td>X4=</td><td>800.00</td><td colspan="2">(crunchy chocolate bars 100 gm.)</td></tr><tr><td>X5=</td><td>0</td><td colspan="2">(chocolate with nuts 250 gm.)</td></tr><tr><td>X6=</td><td>800.00</td><td colspan="2">(chocolate with nuts 100 gm.)</td></tr><tr><td>X7=</td><td>0</td><td colspan="2">(chocolate candies 300 gm.)</td></tr><tr><td>X8=</td><td>144.74</td><td colspan="2">(chocolate wafer)</td></tr></table>

Fig. 8. Compromise solution.

Note: although variable 5 (chocolate with nuts) was in the most preferred group of variables it does not appear in any candidate solution. This is due to the fact that it's weight in the ranking had less impact than the preference of the objective functions and in the interactive stage this variable did not confirm with the indicated improvements directions.

## 4. Conclusion

To summarize the DSS for MOLP presented in this paper we describe a number of experiments conducted in academic and industrial environments which tested the concepts basic to this system and the ease of its interaction with the DM. One major distinction here is that of establishing a weak order on the set of decision variables (and objectives). We found in all our experiments (two cases of insurance company, academic department management game, water resource management, room assignment, and in teaching MOLP), it was well understood and easily accepted and implemented concept.

The second part of our tests consisted in actual running of the system while attempting to solve an MOLP problem. Again, the emphasis on the ease of the interactive stage pays high dividends in terms of the willingness to participate, experiment and accept the outcome (solution) generated by the system. This was demonstrated in the management game experiment and two cases of water resources management. The result of both kinds of tests indicate that our approach and the system presented here can be successfully implemented and used by the DM.

## References

[1] Barbosa, L., and Hirko, R., Integration of Alogorithmic Aids into Decision Support Systems, MIS-Quarterly 4 (1980), 1–12.

[2] Dror, M., Gass, S.I. and Yellin, A., Experiments with an Interactive Procedure for MOLP given Weak Orders on Variables and Objectives, European Journal of Operational Research, 34 (1988), 78–85.

[3] Dror, M. and Gass, S.I., Interactive Scheme for MOLP Problem Given Two Partial Orders: One on Variables and One on Objectives, Applied Mathematics and Computation, 24 (1987), 195–209.

[4] Ecker, J.G., Hegner, N.S., and Kouda, I.A., Generating All Maximal Efficient Faces for Multiple Objective Linear Programs, Journal of Optimization Theory, 30 (1980), 353–381.

[5] Gass, S.I. and Dror, M., An Interactive Approach to Multiple Objective Linear Programming Involving Key Decision Variables, Large Scale Systems, 5 (1983), 95–103.

[6] Geoffrion, A.M., Deyer, J., and Feinberg, A., An Interactive Approach for Multicriterion Optimization with Application to the Operation of an Academic Department, Management Science 19 (1972), 357–368.

[7] Korhonen, P.J., VIG (A Visual Interactive Approach to Goal Programming), Version 2.20–99, Sept. 1987. User's Guide.

[8] Korhonen, P. and Laakso, J., A Visual Interactive Method for Solving the Multiple Criteria Problem, European Journal of Operational Research 24 (1986a), 277–287.

[9] Korhonen, P. and Laakso, J., Solving Generalized Goal Programming Problem Using a Visual Interactive Approach, European Journal of Operational Research 26 (1986b), 355–363.

[10] Korhonen, P. and Wallenius, J. A Pareto Race, Working Paper DIS 85/86–13 Arizona State University (1986).

[11] Siskos, J., and Despostis, D.K., A DSS Oriented Method

for Multiobjective Linear Programming Problems, Decision Support Systems, 5 (1989), 47–55.

[12] Slowinski, R., and Teghem, J., Jr., Fuzzy Versus Stochastic Approaches to Multicriteria Linear Programming under Uncertainty, Naval Research Logistics, 35 (1988), 673–695.

[13] Slowinski, R., A Multicriteria Fuzzy Linear Programming Method for Water Supply System Development Planning, Fuzzy Sets and Systems, 19 (1986), 217–237.

[14] Slowinski, R., A Review of Multiobjective Linear Programming Methods, (in Polish), Przeglad Statystyczny, 31 (1984) Part I – No. 1/2, Part II – No. 3/4.

[15] Tabucanon, M.T., Multiple Criteria Decision Making in Industry, Studies in Production and Engineering Economics 8, Elsevier Science Publishers B.V., 1988.

[16] Teghem Jr., J., Dufrasne, D., Thanvoye, M., and Kunsch, P., STRANGE – An Interactive Method for Multiobjective Linear Programming Under Uncertainty, European Journal of Operational Research, 26 (1986), 65–82.

[17] Zionts, S. and Wallenius, J., An Interactive Programming Methods for Solving the Multiple Criteria Problem, Management Science, 22 (1976), 652–663.
