---
otero_id: 21753
otero_key: "97QRGSEQ"
title: "VisOpt: a visual interactive optimization tool for P-median problems"
authors: "Hasan Pirkul; Rakesh Gupta; Erik Rolland"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00032-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# VisOpt: a visual interactive optimization tool for P-median problems

Hasan Pirkul <sup>a,1</sup>, Rakesh Gupta <sup>a,)</sup>, Erik Rolland <sup>b,2</sup>

School of Management, The UniÕersity of Texas at Dallas, Richardson, TX 75083-0688, USA

<sup>b</sup> A. Gary Anderson Graduate School of Management, The UniÕersity of California RiÕerside, RiÕerside, CA, USA

Accepted 12 July 1999

## Abstract

In this paper, we describe a visual interactive decision support tool ‘VisOpt’ which is designed to solve P-median problems with capacity constraints. Various design features incorporated in VisOpt are also presented and analyzed. We also present a demonstration of the use of VisOpt by a number of human subjects for various problem instances. The quality of solutions obtained by subjects using VisOpt is compared with that obtained from a standard stand-alone heuristic. The visual interactive tool provides encouraging results in this specific problem context. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Visual interactive decision support; Geographical information systems; Facility location; Visual interactive optimization

## 1. Introduction

It is well known that humans are better at processing graphical rather than numerical information; computers are just the opposite 14 . Human experts <sup>w</sup> <sup>x</sup> possess the ability to recognize complex patterns quickly and call upon a large number of heuristics that would help them solve complex problems. However, they are constrained by their limited numerical processing capabilities 21,22 . What is needed,<sup>w</sup> <sup>x</sup> therefore, are systems wherein the abilities of humans are complemented by the number crunching capabilities of computers so as to serve as an integrated human processor 12 . Still, there exists a<sup>w</sup> <sup>x</sup> fundamental mismatch in communication that must be resolved by utilizing a mode of communication that is best understood by a human decision-maker.

In this paper, we describe a decision support tool ‘‘VisOpt’’ that aids a user in solving a capacitated P-median problem 19 . We also demonstrate the <sup>w</sup> <sup>x</sup> usefulness of VisOpt by utilizing it to solve a number of problem instances. VisOpt presents the user with a graphical representation of the problem and allows easy manipulation of solution characteristics through a point and click approach. By carrying out most of the combinatorial number manipulation involved, the system extends the decision-maker’s information processing capabilities while still providing him<sup>r</sup>her with a gestalt representation in graphical form. Through the use of different colors, shapes and sizes, the system visually cues the user towards making good decision choices, and allows him<sup>r</sup>her to come up with sequences of decisions that may provide better global solutions.

The P-median problem we address can be considered a structured one in the following sense: all the problem relevant data is known, and the solution procedure or procedures is also known. However, Ž . due to the combinatorial complexity of the task, solving a realistic sized instance of the P-median problem to optimality is relatively difficult and time-consuming. We have chosen this one problem due to a number of reasons. Firstly, the P-median problem is conceptually a simple one that has been widely studied in the literature. Secondly, the task of selecting P-facilities in a geographical context offers an intuitive and simple spatial representation that can be easily comprehended visually by a decision-maker. The emphasis here is not on solving this one problem, but rather on demonstrating that such systems utilizing human reasoning and pattern recognition abilities, can be developed to successfully tackle mathematical programming problems that can be mapped to meaningful topologies.

Our contributions from this research are the following: we develop a visual interactive decision support tool, which is designed to solve spatial location problems. We compare the performance of users with our tool to that of a stand-alone heuristic, which performs the same task so as to demonstrate the potential usefulness of our tool. Further, we make some general inferences about using such a visual interactive decision support tool, e.g., are there any problem specific characteristics that make such an approach appropriate.

This paper is structured as follows: We provide a summary of past literature in Section 2. Section 3 introduces the problem and discusses VisOpt. Section 4 analyzes the decision task and evaluates different user heuristics. Sections 5 and 6 describe a demonstration of the system in use and discuss findings. Finally, Section 7 summarizes and concludes the paper and outlines the scope for future research.

## 2. Background

A number of researchers have evaluated the use of computer graphics in decision support tools. In general, it has been accepted that a graphical method of representing information or solutions improves the performance, understanding, solution quality for users in a decision-making task 3,15,18,26 . In addi-<sup>w</sup> <sup>x</sup> tion, due to the immense capabilities afforded by the computer hardware and software of today, visual interactive interfaces for decision support systems present a rapidly expanding area of research. In a comprehensive review of commercial facility location software, Ballou and Masters 1 emphasize the<sup>w</sup> <sup>x</sup> importance that users place on graphics capabilities and user-friendliness. The same was reported by a more recent survey of decision support applications by Eom et al. 8 . <sup>w</sup> <sup>x</sup>

While a large number of visual interactive decision support tools have been presented by researchers in the past, for brevity, we focus primarily on systems that either deal with transportation or communication networks<sup>r</sup>systems or those that address optimization-related issues similar to our own.

Problems in graph theory lend themselves readily to a visual representation. As early as 1986, Dao et al. 5 have developed a system that allows its users<sup>w</sup> <sup>x</sup> to define and solve a number of graph theoretic problems in an object-oriented fashion. In fact, due to the increasing importance of graphical interfaces in OR, a large number of systems have appeared in the recent past that deal with graphical analysis of OR problems. EDINET 24 is a network editor<sup>w</sup> <sup>x</sup> intended for easy display and change of network attributes. NETPAD 6 is another network modeler<sup>w</sup> <sup>x</sup> and optimizer that has an intuitive user interface. GIN 29 is another graph-based interface for net-<sup>w</sup> <sup>x</sup> work modeling. Tracey and Dror 30 present an<sup>w</sup> <sup>x</sup> interactive computer application for graphically presenting the feed distribution solution for cattle feed ranches. Similarly, Jack et al. 11 present NETCAP,<sup>w</sup> <sup>x</sup> which is an interactive optimization system for solving a large multi-period capacity expansion problem for telephone networks while a graphical system for optimizing the location of tax service facilities is presented by Domich et al. 7 .<sup>w</sup> <sup>x</sup>

Perhaps closest to our own research efforts are those of Hurrion 10 , Krolak et al. 17 , Mak et al.<sup>w x</sup> <sup>w x</sup> <sup>w x</sup> <sup>w x</sup> <sup>w x</sup>20 , and Scriabin and Vergin 27 . Hurrion 10 describes a visual interactive method of improving solutions for the traveling salesman problem T.S.P. .Ž . By using a simple visual tool utilized primarily forŽ displaying solutions , the author reported solutions. that were within 4% of those obtained from a heuristic. Mak et al. 20 provide experimental evidence<sup>w</sup> <sup>x</sup> showing that for the same problem T.S.P. , visualŽ . interactive solutions achieved by humans are better than even the best computer heuristics. On the task of plant layout design, Scriabin and Vergin 27<sup>w</sup> <sup>x</sup> showed that humans without the benefit of any prescriptive help from a computer, can create layouts that are better than those obtained from computer programs. Similar results were reported by Trybus and Hopkins 31 for the same problem. Krolak et al.<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 17 utilized a man–machine approach to solving the generalized truck-dispatching problem and provided the user with a visual representation of intermediate solutions and scenarios. The user was able to interactively change the solution and apply various heuris tics to completely solve the problem. By following this methodology, the authors reported that a combined man–machine tool resulted in better solutions than those from computer programs. Similarly, Fisher <sup>w</sup> <sup>x</sup> 9 proposed an integrated human machine tool wherein a human could intervene at points during the execution of an optimization algorithm and by utilizing his<sup>r</sup>her own perceptual abilities make changes that the algorithm by itself would not be able to make. Jones 13 in a comprehensive review of visualization and related tools in OR, points out that problem-solving requires more than just algorithm building, it also consists of a process of transforming and understanding various representations or visualizations of the problem in question.

Our efforts are different from the prior research in this area due to a number of reasons. VisOpt is designed to provide visual cues to the decision-maker which are aimed at informing the user of what might be possible avenues of action. Further, the system is designed so as to avoid restricting the user in his<sup>r</sup>her actions. For instance, we allow the user to create infeasible solutions i.e., solutions violating capacity Ž constraints for example since further modifications. of such solutions may result in better feasible solutions that those attained so far. This mitigates the system restrictiveness posited by Chu and Elam 4 and provides a method for the user to escape local minima — a difficulty faced by most heuristic procedures for combinatorial problems.

## 3. The capacitated P-median problem and visual support for solving it

The capacitated P-median problem can be stated as follows: given a graph $G = ( V , E ) , V _ { 1 } \subset V ,$ , where $V _ { 1 }$ is the set of potential facility sites with capacities C, V is the set of demand nodes with a demand vector A, we are asked to find a set of nodes S $( S \subseteq V _ { 1 } ) .$ , of cardinality P, such as the weighted sum of assigning the nodes V to the set S is minimized while all demand is satisfied without violating capacity constraints. A mathematical formulation of the problem is provided in Appendix A. For the problems considered, the costs on the edges are assumed to be proportional to the Euclidian distance between sites. Problems with non-Euclidean costs pose additional difficulties in being mapped to a visual repre-Ž sentation which are beyond the scope of this paper. . These issues are currently being studied as an extension of this research.

P-median problems have applications in plant and warehouse locations, where the objective is to find a configuration of facilities that best serves the demands of a market area. Applications can also be found in public sector location modeling, where it is required to locate schools, hospitals, post offices, etc.

According to the description given above, the problem poses the following constraints on a decision-maker:

1. Only a predetermined number Ž . P of facilities can be opened or located .Ž .

2. Every demand point must be supplied.

3. A facility can supply only a predetermined amount of goods<sup>r</sup>services.

The decision-maker needs to be informed about each of the above criteria and also any violations to them. Further, based on our discussion in Section 2 and our intention to create a visual interactive decision-making environment, our design had to include features that: 1 Provide the user with a consistent,Ž . visual representation of reality minimizing the use of numbers and textual information. 2 Create a simpleŽ . dynamic representation that displays various parameters as the user evolves her<sup>r</sup>his solution. 3 Let theŽ . system carry out tedious tasks like sorting<sup>r</sup>searching, etc., in a fast and transparent to the userŽ . manner, while still allowing the user to make any changes using his<sup>r</sup>her own heuristics. 4 VisuallyŽ . indicate relevant features of the problem instance Ž . e.g., cost, demand needed, capacity available, etc. . Also, indicate to the user any violations in constraints and possible ways to remove them. 5 Pro-Ž . vide an environment in which the user can explore ‘‘what-if’’ solutions, through intuitive and obvious steps e.g., pointing and clicking on graphic ele- Ž ments . 6 Display appropriate feedback to the user. Ž . in a consistent form at all times.

## 3.1. Design features

The following design principles were followed in developing the decision support system.

Ž . 1 Provide a representation that is consistent with reality, preserving a mapping from real life to its visual model. To accomplish this, the two-dimensional coordinates of each facility and demand site are mapped on to the screen. Since costs on arcs are proportional to transportation costs, a demand node close to a facility would be cheaper to supply as opposed to one that is far away.

Ž . 2 The size of each node is displayed proportional to the number of units demanded by it. Therefore, a large demand node as shown in Fig. 1 indicates a high demand. This seems consistent with the intuitive notion of ‘‘big’’ meaning ‘‘more’’.

Ž . 3 Networks are displayed without any connecting arcs unless the arcs are demanded by the user. Unless required, identifying numbers for nodes are also not displayed, instead different colors are utilized to identify and group together nodes connected to facilities.

![](/api/attachments/97QRGSEQ/fulltext/images/ee7b980a8f0e6b4ebad9d6015eaa0470d8fdc9d897ec69a5da6ccc9b2c1cf2cf.jpg)  
Fig. 1. Demand and facility nodes with progressively large demand requirements.

Ž . 4 Demand nodes are displayed as circles, facilities have a square superimposed over this circle and are colored red.

Ž . 5 Since each facility has a preset capacity, usage is indicated by a thermometer like object displayed at the bottom right corner of the node. Note that this thermometer-like object is displayed only if a facility is located at a potential site i.e., a facility is openedŽ . and is not shown if the facility is closed. As capacity usage increases, the ‘‘level of mercury’’ in this thermometer rises. If capacity is exceeded, the color of the ‘‘mercury’’ which is ordinarily green whileŽ capacity limit is not exceeded , turns red. An in- . stance of a facility exceeding its capacity is seen in Fig. 2. Once a facility exceeds its preset capacity, some of the demand nodes it supplies need to be re-assigned. A node, which if re-assigned would bring the facility to within capacity a critical node , Ž . is displayed with a dark border.

Ž . 6 To provide a dynamic representation, the system performs a simple heuristic to assign demand nodes to facilities. This heuristic is executed each time a facility is opened or closed and is described in Section 4.

Ž . 7 Feedback on the cost, feasibility and other related statistics are provided to the user in a multiline status<sup>r</sup>message window at the bottom of the screen.

Ž . 8 What-if questions can be answered by simply clicking on various visual elements. For instance, by clicking on a demand point and then on a facility, the system responds with the cost of supplying the demand node with the facility, the new value of the total cost and infeasibilities if any that result. Simi-Ž . larly, by clicking on two facility sites the first openŽ and the second closed , the system responds with the . resulting objective function value if the first facility were closed and the second opened.

## 3.2. Heuristic used to assign demand nodes to facilities

VisOpt utilizes a simple heuristic to connect demand nodes to a facility that has been opened. It must be kept in mind that this heuristic has been chosen so as to be 1 fast, to minimize waiting time Ž .

![](/api/attachments/97QRGSEQ/fulltext/images/0e88ecf996ad11e96eb0209c2bece88607eabd086e57d93ebc70e92db297e9f6.jpg)  
Fig. 2. Infeasible solution to a five-median problem.

for a user, 2 transparent to the user. The secondŽ . point is important so as to avoid a ‘‘gulf of execution’’ 23 , i.e., so that the user fully understands<sup>w</sup> <sup>x</sup> what would happen each time he<sup>r</sup>she opens or closes a facility. Through the use of such a heuristic, the system provides a fast and intuitive way of connecting facility nodes to demand points. Thus, the user need not tediously connect every demand point to a facility. Further, such a heuristic provides the user with a convenient means of getting to a feasible solution a starting point to the problem.Ž . The heuristic called DemConnect proceeds as fol- Ž . lows: We create a list of demand weighted transportation costs of connecting each demand point with every facility that is open. This list is sorted in ascending order of cost. Next, the cheapest elements from this list are assigned to the facilities until either the available capacity at the facilities is exhausted or no unsupplied demand nodes remain.

## 4. Task analysis

An analysis of the major steps needed to be carried out in solving the P-median problem is presented in this section. A description of the support provided by the computer system in this context is also included.

## 4.1. Problem-solÕing methodology

The major steps that need to be carried out to get a feasible solution are following:

1. EÕaluate and open facilities;

2. EÕaluate and modify the connections demandŽ nodes to facilities provided by the system i.e.,. Ž provided by heuristic DemConnect ;.

3. EÕaluate and drop close facilities in favor ofŽ . cheaper ones;

4. If a satisfactory solution is not attained then if more facilities can be opened, go to 1 else go to 2.

Else stop.

It is significant that in the above-task analysis we have used a generic term EÕaluate to describe the users choice of: a which facility to open, b which Ž . Ž . facility to connect to a demand node and c whichŽ . facility to drop from a set of open facilities and conversely which facility to add to the same. The reason for this is that a human may choose to use one or more of many ‘‘in-built’’ heuristics to carry out each of a – c . Further, the steps listed aboveŽ . Ž . are ones which will have to be carried out irrespective of which higher level strategy the user may follow e.g., greedy in number of facilities, divideŽ and conquer, etc. . A fundamental limitation of . stand-alone computer-based methods is that each algorithm is usually good for problems of a particular structure. There exist few general-purpose algorithms that will do well in all situations. Humans, on the other hand, can call upon multiple heuristics to solve a problem, given that there exists some recognizable pattern in its structure. A description of some of the possible ‘‘rules of thumb’’ is presented in Appendix B. It must be stressed that this list is by no means exhaustive. One of the major advantages of this methodology is that a decision-maker can choose any strategy or rule that he<sup>r</sup>she thinks appropriate. Thus, ‘‘system restrictiveness’’ 4 is mitigated.<sup>w</sup> <sup>x</sup>

## 5. Experimental demonstration

The purpose of this demonstration was to attempt to characterize the effectiveness of our visual decision support system. Ideally, the user of a DSS like ours would be an ‘‘expert’’ in that area or at theŽ very least, a person familiar with the structure of the problem . The participants for the demonstration were. therefore selected from undergraduate decision sciences<sup>r</sup>operations research techniques courses at two major universities. The majority of the students were juniors opting for a major in Business. These students were familiar with the use of linear programming techniques in the context of location problems. As an incentive, each subject was assigned an extra credit score proportional to the quality of the solution obtained by her<sup>r</sup>him. The scores and scoring scheme was explained to the students before the beginning of the experiment. The experiment was carried out on IBM Compatible microcomputers running MS Windows.

The solution quality obtained from subjects was compared with that achieved by a previously published heuristic due to Pirkul and Schilling 25 . In<sup>w</sup> <sup>x</sup> addition, time taken to reach a satisficing solution was observed for each of the subjects. Subjects were randomly assigned to one of 12 experimental sessions over a period of 2 weeks. To avoid any biases due to extraneous factors between sessions, subjects within each session were randomly assigned one of the following three problems.

## 5.1. Type 1

Problems incorporating real geographical data. Three problems were created using data obtained from the ArcUSA database incorporating information from the US census of 1991. The centroid of each county in Ohio was chosen as a demand point.Ž . The demand at each site was based on the population of the county. Distances serving as a proxy for costŽ on arcs between each point are actual Euclidean . distances in miles. Counties with population greater than 200,000 are designated as potential facilities.

Ž .a An 88-node problem incorporating data from the state of Ohio, 12 potential facilities, five facilities to open.

Ž . b A 72-node problem incorporating data from the state of Wisconsin, 13 potential facilities, five facilities to open.

Ž .c A 67-node problem incorporating data from the State of Florida, 18 potential facilities, five facilities to open.

## 5.2. Type 2

A random 88-node problem, 12 potential facilities, five facilities to open. With data based on points randomly generated on a square of side 1000 units. Demand at each point was randomly generated over a uniform distribution 0, 200 . Costs along arcsŽ . were equal to the Euclidean distance between the points generated.

## 5.3. Type 3

A random 49-node problem, 17 potential facilities, eight to open. This problem was generated in the same manner as type 2.

Each session began with an hour-long training period, during which subjects were asked to solve a randomly generated 68-node problem the same Ž problem was solved by each subject . Subjects were. encouraged to ask any questions regarding the program and experiment with it so that they understood its functionality. At the end of this training period, each subject was given 30 min to solve one of the problems mentioned above. The objective for each subject was to arrive at a satisficing solution for each of these problems within that time.

As mentioned earlier, the primary variable of interest was the objective function value obtained by each subject. In addition to this value, the system also kept a log of the time taken by each subject to reach this solution. A post-experimental questionnaire was utilized to keep track of demographic information. The questionnaire also required the students to answer some elementary questions about the DSS as well as the P-median problem.

## 6. Discussion of demonstration results

Results from the experiment are shown in Tables 1 and 2. We were interested in answering the following question: Can human subjects, with the aid of a visual problem-solving system like ours, effectively solve a complex mathematical problem? In this section, we compare the solutions attained by humans with those obtained by a previously published heuristic due to Pirkul and Schilling 25 .<sup>w</sup> <sup>x</sup>

Fig. 3 shows the average gap obtained from the experiment when subjects are stratified into categories representing the best 20%, 40%, 60%, 80% and 100%. Interestingly enough, the average $Z _ { \mathrm { e x p } }$ obtained for problems of type 1 is better $( \mathrm { i . e . } ,$ , less . than $Z _ { \mathrm { h } }$ Ž . for the majority of subjects . The very opposite occurs in the case of problems of types 2 and 3. For both of these problems, all subjects performed worse than the heuristic. However, as shown in Fig. 3, on the average, subjects achieved objective function values within 4.5% of the heuristic for type 3 and 2% for problem type 2. Ž .

Table 2  
Comparison of $Z _ { \mathrm { e x p } }$ with $Z _ { \mathrm { h } }$ for each problem type

<table><tr><td>Problem</td><td>Number of subjects</td><td>Number with of subjects $Z_{\text{exp}} < Z_h$ </td><td>Heuristic solution  $Z_h$ </td></tr><tr><td>Type 1a</td><td>25</td><td>19</td><td>464,221</td></tr><tr><td>Type 1b</td><td>27</td><td>26</td><td>299,649</td></tr><tr><td>Type 1c</td><td>26</td><td>20</td><td>978,367</td></tr><tr><td>Type 2</td><td>22</td><td>0</td><td>126,913</td></tr><tr><td>Type 3</td><td>25</td><td>0</td><td>818,264</td></tr></table>

Could there be any specific reasons why subjects consistently perform better for the problems of types 1 vs. 2 and 3? An analysis of the problems themselves could help explain this disparity in problemsolving abilities. Fig. 4 a – e shows the topologies Ž . Ž . of the different problem types as presented to subjects. From observation of Fig. 4, one can easily perceive that the type 1 problems display a ‘‘skewed’’ distribution. For instance, in Fig. 4 a , there are atŽ . least three facilities A, B, and C that have ex-Ž . tremely large demands. Thus, a simple application of rule 1 see Appendix B would result in choosingŽ . these facilities. Further, both A and D are lone counties with a large number of small demand nodes surrounding them. It seems reasonable to assume that an informed user would choose to locate facilities at these sites and supply the nodes around them. The other two problem types Fig. 4 d and e displayŽ Ž . Ž .. no such patterns, and for a good reason: Both problems types 2 and 3 were generated over a uniformŽ . distribution a square of side 1000 . However, theŽ .

Table 1  
Descriptive statistics of demonstration

<table><tr><td rowspan="2">Type</td><td rowspan="2">Number of nodes</td><td rowspan="2">Potential facilities</td><td rowspan="2">Numbers of subjects</td><td rowspan="2">Mean objective function ( $Z_{exp}$ )</td><td rowspan="2">Median objective function</td><td rowspan="2">Standard deviation</td><td colspan="3">Objective function value</td></tr><tr><td>Best</td><td>Worst</td><td>Best 80% subjects</td></tr><tr><td>Type 1a</td><td>88</td><td>12</td><td>25</td><td>458,407</td><td>456,419</td><td>8045</td><td>448,629</td><td>472,363</td><td>454,984</td></tr><tr><td>Type 1b</td><td>72</td><td>13</td><td>27</td><td>267,329</td><td>263,571</td><td>10,028</td><td>262,699</td><td>314,338</td><td>264,111.2</td></tr><tr><td>Type 1c</td><td>67</td><td>18</td><td>26</td><td>989,558.2</td><td>989,558.2</td><td>66,169</td><td>966,910</td><td>1,311,694</td><td>973,906.1</td></tr><tr><td>Type 2</td><td>88</td><td>12</td><td>22</td><td>1,299,807</td><td>1,290,849</td><td>34,431</td><td>1,271,799</td><td>1,401,156</td><td>1,286,568</td></tr><tr><td>Type 3</td><td>49</td><td>17</td><td>25</td><td>852,564</td><td>852,131</td><td>26,500</td><td>819,432</td><td>902,994</td><td>845,820</td></tr></table>

![](/api/attachments/97QRGSEQ/fulltext/images/da82d466e8af6a9481085ecefc92ea6fb69f6f9083ea180d8e6356f67765532b.jpg)  
Subject categories (top 20, 40, 60, 80, 100 %)  
Fig. 3. Average difference in objective function experimental vs. heuristic values for each group stratified by performance within group. Ž .

first problem type 1 represents the actual locationŽ . of the centroid of each county in Ohio with de-Ž mands proportional to the population of each county .. Thus, large population centers such as Columbus Ž . Ž . county A and Cleveland county B would be expected to be surrounded by smaller in population Ž . counties.

It seems curious that the heuristic 25 in question<sup>w</sup> <sup>x</sup> seems to perform relatively poorly for problem type 1 as compared to problem type 2. We therefore solved each of the above-problems using the commercial version of LINDO a mixed integer LPŽ package running Pentium II PC 350 MHz and. Ž . porting Windows NT 4.0. Results from this analysis are shown in Table 3.

Analysis of the time taken to reach the optimal solution Table 3 by LINDO underlines the fact that Ž . problems of type 1 are more difficult to solve optimally. Specifically, it takes over 14 times as much CPU time to solve problem type 1a as compared to problem type 2, even though both have the same number of demand and facility nodes. One of the reasons for this is the fact that the type 1 problems exhibit symmetry, which is known to cause difficulties for traditional optimization procedures like branch and bound 2 . That is, from the topology of<sup>w</sup> <sup>x</sup> the type 1 networks one can see that there is very little variance between the size of demand among a large number of demand points. For a heuristic which is blind to this fact, choosing to supply one demand point would seem as attractive as choosing to supply another. Therefore, a heuristic or a branch and bound procedure such as that used by LINDOŽ . would expend significant amounts of computational time comparing such nearly equivalent choices. It is interesting to note that it is precisely these kind of problems type 1 that the human subjects solved Ž . with relative ease.

Solution times for human subjects ranged from 21–30 min as compared to an average of approximately 35 min taken by LINDO for the type 1 problems. From Table 3, it is clear that the comparison heuristic finds relatively good solutions for both of the random problems types 2 and 3 and leavesŽ . very little room for improvement gaps of 0.072%Ž and 0.31%, respectively . The only difference be-. tween these problems and the type 1 problem is the network topology, which we emphasized above. Based on this, we conjecture that actual geographic and demographic data may contain recognizable by Ž humans patterns that can help humans make effec- . tive decisions. However, we cannot assert that this will always be so. That is, there may exist real Ž . geographical data which exhibits a distribution similar to that shown by problems of types 2 and 3, in which case a tool such as ours may not be the best method to resort to.

Further, the presence of symmetry in the type 1 problems may actually work as an advantage for human decision-makers. While the comparison heuristic lacks the ability to visualize and make pattern matched inferences for the ‘‘skewed’’ distribution in the type 1 problems, humans, by combining their own ability to identify and utilize such patterns with those of a computer in a visual interac-Ž tive manner , seem to make relatively good deci-. sions. It may be possible that a heuristic other than that due to Pirkul and Schilling 25 may result in <sup>w</sup> <sup>x</sup> better solutions for the type 1 problems. However, it is unlikely that a simple e.g., add Ž . <sup>r</sup>drop or greedy heuristic would be able to outperform this particular one.

(a)  
![](/api/attachments/97QRGSEQ/fulltext/images/8f647d8aefc533691fce17e56aef7481fc7bf977c955af224274bcd8b332c2b7.jpg)

(b)  
![](/api/attachments/97QRGSEQ/fulltext/images/7e454c21ed843328dd0664a73acb4e5b87f87b648f7783e586ec80b3c057a0ae.jpg)

(c)  
![](/api/attachments/97QRGSEQ/fulltext/images/b7c7b0ae12911cfe6547f4bd850c7292ec3042e0c722e5ec54755c2c96391598.jpg)  
(e)

(d)  
![](/api/attachments/97QRGSEQ/fulltext/images/e86ea1de68bdcf5f9305d704d92bbe1d25c3dcc85df90bb75938b0d9b4ab14d3.jpg)

![](/api/attachments/97QRGSEQ/fulltext/images/fb3a0228b4e5733eb2962d2c0f786322fafb56d743e3a97ce767bd72a50d0107.jpg)  
Fig. 4. a Topology of problem of type 1. b Topology of problem of type 2. c Topology of problem of type 3. Ž . Ž . Ž .

Table 3  
Comparison of heuristic and experimental solutions with optimal solutions

<table><tr><td>Problem</td><td>Optimal solution (Zopt)</td><td>Time to optimal (s)</td><td>% Gap with heuristic solution ((Zh-Zopt)/Zopt)100</td><td>% Gap with mean objective function obtained by subjects ((Zexp-Zopt)/Zopt)100</td></tr><tr><td>Type 1a</td><td>445,619</td><td>3785</td><td>4.17</td><td>2.86</td></tr><tr><td>Type 1b</td><td>262,609</td><td>286</td><td>14.10</td><td>0.034</td></tr><tr><td>Type 1c</td><td>963,010</td><td>3029</td><td>1.59</td><td>0.405</td></tr><tr><td>Type 2</td><td>1,268,207</td><td>267</td><td>0.072</td><td>2.49</td></tr><tr><td>Type 3</td><td>815,700</td><td>12</td><td>0.31</td><td>4.51</td></tr></table>

## 7. Conclusions and directions for future research

In this paper, we have introduced the idea of a computer-based decision support tool VisOpt that Ž . can be used in conjunction with its decision-maker to solve a structured location problem. VisOpt is based on the fundamental notion of visual as opposed to Ž textual information being easier to comprehend by a . human decision-maker. The importance of problem specific criteria and their mapping into a visual model was also presented. Finally, details of an experimental demonstration of the effectiveness of such a visual interactive decision-making paradigm were presented and discussed.

The main contribution of this research effort lies in the characterization of humans as decision-makers in the context of structured problems. Until now, humans have always been considered superior in solving decision problems that are unstructured, and this prompts the development and use of decision support systems designed to aid humans in these tasks 16 . On the other hand, structured problems <sup>w</sup> <sup>x</sup> seem to be more effectively solved by stand-alone computer programs since for the most part such problems require intense computational capabilities and these solution procedures for such problems can be programmed 28 . Our experimental results indi-<sup>w</sup> <sup>x</sup> cate that the pattern recognition capabilities of humans can be tapped and utilized advantageously for problems that present a spatial mapping of information. Further, the results indicate that actual geographic and demographic data may carry spatial patterns utilizable by humans. Conceptually, the ability to recognize such patterns can be hardcoded into a series of ‘‘if–then’’ rules. However, most humans already carry such heuristics encoded in their minds. Surely, it would be most advantageous if a human decision-maker could take advantage of these rules and use them in conjunction with a DSS to help carry out a problem-solving task.

In this effort, we have considered a variant of the P-median problem, a problem that is well known and researched. However, the main advantage of an approach of this kind would lie in solving problems that have constraints that are difficult to model, or if modeled, are difficult to solve. This is because in a cooperative problem-solving paradigm, humans could help enforce the difficult constraints while the computing system limits itself to best satisfying the easier constraints. Thus, this fundamental division of labor could result in better solutions on the whole. Another interesting prospect is utilizing an established heuristic to achieve an initial solution which users could then attempt to improve. Our research therefore represents a small step towards applying a similar problem-solving approach to more complex and difficult to solve problems.

![](/api/attachments/97QRGSEQ/fulltext/images/5208ee2c557fcef177371070b45f899a26f0c4182ae884f2072799a1b64927a1.jpg)  
Fig. 5. Choosing a facility based on its demand.

Based upon the preceding discussion, a fundamental question arises: Could structured problems always be solved in such a cooperative fashion? The answer to this question is likely to be no, because as we have stressed before, there needs to exist some convenient mapping from the problem data to a visual model. Further, this visual information must contain recognizable for humans patterns so that a Ž . human can make effective decisions. The problem we have analyzed does contain such information, but, at this point, we would hesitate in generalizing these results to any other problem context. More research is needed to effectively answer this question. What we can say is that we have demonstrated the potential of a combined human–machine problem-solving paradigm, in solving a mathematical programming problem. Thus, human capabilities should not be overlooked in solving such problems.

Decision support systems are fundamentally built upon the concept of human–machine cooperation. However, their use is most effective if the human decision-maker is least restricted in his<sup>r</sup>her actions. VisOpt was designed with the intent of minimizing such restrictiveness. Within the context of a combined human–machine problem-solving paradigm, what is needed is a conceptual framework indicating which tasks to be carried out by which party humanŽ or machine . Similarly, it is important to investigate . the best ways to represent information that is nonspatial financial, temporal through visual cues. Ž . Currently we are engaged in research aimed to provide insights to these and other issues.

## Appendix A. Mathematical formulation of Pmedian problem

The capacitated P-median problem can be stated mathematically as follows.

## A.1. Cap. P-median

$$
\operatorname{Min} \sum_ {i} \sum_ {j} a _ {i} d _ {i j} x _ {i j}\tag{1}
$$

$$
\sum_ {j} x _ {i j} = i \forall i\tag{2}
$$

$$
x _ {i j} \leq y _ {j} \forall i, j\tag{3}
$$

$$
\sum_ {j} y _ {j} = P\tag{4}
$$

$$
\sum_ {i} a _ {i} x _ {i j} \leq c _ {j} \forall j\tag{5}
$$

$$
x _ {i j}, y _ {j} \in \{0, 1 \} \forall i, j\tag{6}
$$

where $a _ { i } =$ demand at node i; $c _ { j } =$ capacity at facility site j; $d _ { i j } =$ distance from node i to node $j ;$ $P =$ preset number of facility nodes; $x _ { i j } = 1$ if node i is assigned to facility $j , \ x _ { i j } = 0$ , otherwise; $y _ { j } = 1$ if facility j is open, $y _ { j } = 0$ , otherwise.

The objective function 1 minimizes the weightedŽ . sum of assigning demand nodes to facility sites.

![](/api/attachments/97QRGSEQ/fulltext/images/bde092906e3837158784bcf6cc2304821f899580f4322630fe75afb6edbb0539.jpg)  
Fig. 6. Application of rule 2: choosing a facility based on demand node ‘‘clustering’’. b Application of rule 2: choosing rule 2 over Ž . rule 1.

Constraint set 2 ensures that all demand nodes areŽ . assigned to exactly one facility. In constraint 3 , weŽ . ensure that a node is assigned to a facility only if it is open. The third constraint 4 enforces the fact thatŽ . exactly P facilities are being opened. In constraint set 5 , we ensure that the demands of all nodesŽ . assigned to a facility are within its capacity. Finally, the integrality of the decision variables are enforced by constraint set 6 . A heuristic solution procedureŽ . suggested by Pirkul and Schilling 25 was utilized to <sup>w</sup> <sup>x</sup> get a feasible solution.

## Appendix B. Sample user heuristics

## B.1. Choosing which facility to open

Rule 1: ‘‘Choose to open a facility that has a large demand over one that has a small demand.’’

Rationale: In the context of this problem, the costs being minimized are transportation costs, since a facility supplying demand at the same node incurs no transportation costs, it is advantageous to open a facility in a node with a large demand over one with a small demand. Hence, as shown in Fig. 5, choose facility A over B, C, and D.

Rule 2: ‘‘Choose to open a facility that has a large number of demand nodes ‘clustered’ around it, over one that has no such clustering around it.’’

Rationale: Once again since transportation costs are being minimized, it may be preferable to locate a facility that is central to a large number of demand nodes. For the configuration shown in Fig. 6 a , bothŽ . rules 1 and 2 would suggest opening facility A rather than facility B. In Fig. 6 b , while one user utilizingŽ . rule 1, might choose to open facility B, another user may choose to open facility A because of rule 2.

## B.2. Choosing which facility to supply a demand node from

Rule 3: ‘‘Keep connecting arcs as short as possible.’’

Rationale: Keeping with the objective of minimizing transportation costs, a user might wish to connect demand points such that long transportation links are avoided. A look at Fig. 7 clearly indicates the effectiveness of such a strategy, following this rule, a user might wish to connect the marked demand nodes

![](/api/attachments/97QRGSEQ/fulltext/images/5c731b57da74ddb47dcd17540ea213e31ca7aa7463dee9406e28cb83e4a6824a.jpg)  
Fig. 7. Rule 3: ‘‘Eliminate long arcs’’ for nodes in box . Ž .

Ž <sup>4</sup> enclosed in the box to facility A instead of facility . B.

(a)  
![](/api/attachments/97QRGSEQ/fulltext/images/f3bcb19214c62a001f842791a8d51929866a05b80dfc15fcfcedfeeb8b5907c8.jpg)

![](/api/attachments/97QRGSEQ/fulltext/images/402ac9e948af1a69db441c200ad1b11adff7d0e08d611bc35c15012c08c45f4d.jpg)  
Fig. 8. a Modifications to network in Fig. 7: result of applying rule 3; now, apply rule 4 to marked nodes in boxes . b Further Ž . Ž . Ž . modifications to network in Fig. 7: after applying rule 4; note improvement in cost.

Rule 4: ‘‘Allow some close with regards to Ž distance on screen demand nodes to be connected to. far away facilities so that some other demand nodes can be supplied.’’

Rationale: An application of this rule can be seen from Fig. 8 a and b . After applying rule 3 on the Ž . Ž . network in Fig. 7, the result is an infeasible solution Ž Ž .. see Fig. 8 a . Through an application of rule 4 to the nodes enclosed in boxes in Fig. 8 a , the result isŽ . a feasible and improved with regards to cost solu- Ž . tion Fig. 8 b . Note, that the marked demand nodes Ž Ž .. in Fig. 8 a are actually closest to facility A, how- Ž . ever, the user chose to supply them from facility C so that the overall solution is feasible and improved.

## References

<sup>w</sup> <sup>x</sup> 1 R.H. Ballou, J. Masters, Commercial software for locating warehouses and other facilities, Journal of Business Logistics 14 1993 2.Ž .

<sup>w</sup> <sup>x</sup> 2 C. Barnhart, E. Johnson, G. Nemhauser, M. Savelsbergh, P. Vance, Branch-and-price: column generation for solving huge integer programs, forthcoming in Operations Research 1996 .Ž .

<sup>w</sup> <sup>x</sup> 3 J.M. Carrol, J.C. Thomas, A. Malhotra, Presentation and representation in design problem solving, British Journal of Psychology 1980 143–153.Ž .

<sup>w</sup> <sup>x</sup> 4 P.C. Chu, J.J. Elam, Induced system restrictiveness: an experimental demonstration, IEEE Transactions on Systems, Man and Cybernetics 20 1990 195–201.Ž .

<sup>w</sup> <sup>x</sup> 5 M. Dao, M. Habib, J.P. Richard, D. Tallot, Cabri, An interactive system for graph manipulation, in: G. Tinhofer, G. Schmidt Eds. , Graph–Theoretic Concepts in Computer Ž . Science, Springer-Verlag, Berlin, 1986, pp. 58–67.

<sup>w</sup> <sup>x</sup> 6 M.N. Dean, M. Mevenlamp, C. Monma, NETPAD: an interactive graphics system for network modeling and optimization, in: O. Balci, R. Sharda, S. Zenios Eds. , ComputerŽ . Science and Operations Research: New Developments in their Interfaces, Pergamon, UK, 1992, pp. 231–243.

<sup>w</sup> <sup>x</sup> 7 P.D. Domich, K.L. Hoffman, R.H.F. Jackson, M.A. Mc-Clain, Locating tax facilities: a graphics based microcomputer optimization model, Management Science 37 8 1991Ž . Ž . 960–979.

<sup>w</sup> <sup>x</sup> 8 S.B. Eom, S.M. Lee, E.B. Kim, C. Somarajan, A survey of decision support system applications 1988–1994 , Journal of Ž . the Operational Research Society 49 1998 109–120.Ž .

<sup>w</sup> <sup>x</sup> 9 M.L. Fisher, Interactive optimization, Annals of Operations Research 5 1986 541–556.Ž .

<sup>w</sup> <sup>x</sup> 10 R.D. Hurrion, Visual interactive computer solutions for theŽ . traveling salesman problem, Journal of the Operations Research Society 31 1980 537–539.Ž .

<sup>w</sup> <sup>x</sup>11 C. Jack, S.R. Kai, A. Shulman, NETCAP an interactive optimization system for GTE telephone network planning, Interfaces 22 1 1992 72–89.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 V.S. Jacob, J.C. Moore, A.B. Whinston, An analysis of

human and computer decision-making capabilities, Information and Management 16 5 1989 247–255. Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 C.V. Jones, Visualization and optimization, ORSA Journal on Computing 6 3 1994 221–257.Ž . Ž .

w x <sub>14 E. Kasanen, R. Ostermark, M. Zeleny, Gestalt system of</sub>¨ holistic graphics: new management support view of MCDM, Computers and Operations Research 18 1991 233–239.Ž .

<sup>w</sup> <sup>x</sup> 15 G. Kaufmann, Imagery, Language and Cognition: Towards a Theory of Symbolic Activity in Human Problem Solving, Columbia University Press, New York, 1980.

<sup>w</sup> <sup>x</sup> 16 P.G.W. Keen, M.S. Scott Morton, Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, MA, 1978.

<sup>w</sup> <sup>x</sup> 17 P. Krolak, W. Felts, J. Nelson, A man–machine approach toward solving the generalized truck-dispatching problem, Transportation Science 6 1972 22–30.Ž .

<sup>w</sup> <sup>x</sup> 18 J.H. Larkin, H.A. Simon, Why a diagram is sometimesŽ . worth ten thousand words?, Cognitive Science 11 1987Ž . 65–99.

<sup>w</sup> <sup>x</sup> 19 J. Levy, An extended theorem for location on a network, Operational Research Quarterly 18 1967 433–442.Ž .

<sup>w</sup> <sup>x</sup> 20 K.T. Mak, K. Srikanth, A. Morton, Visualization of Routing Problems, CRIM Working Paper 90-03, Department of Information and Decision Sciences, College of Business Administration, University of Illinois at Chicago, Chicago, IL, 1990.

<sup>w</sup> <sup>x</sup> 21 G.A. Miller, The magical number seven, plus or minus two: some limits on our capacity for processing information, The Psychology Review 23 1956 . Ž .

<sup>w</sup> <sup>x</sup> 22 A.N. Newell, H.A. Simon, Human Problem Solving, Prentice-Hall, Englewood Cliffs, NJ, 1972.

<sup>w</sup> <sup>x</sup> 23 D.A. Norman, The Design of Everyday Things, Basic Books, New York, 1988.

<sup>w</sup> <sup>x</sup> 24 W. Ogryczack, K. Studzinski, K. Zorychta, EDINET — a network editor for transshipment problems with facility location, in: O. Balci, R. Sharda, S. Zenios Eds. , Computer Ž . Science and Operations Research: New Developments in their Interfaces, Pergamon, UK, 1992.

<sup>w</sup> <sup>x</sup> 25 H. Pirkul, D. Schilling, The maximal covering location problem with capacities on total workload, Management Science 37 1991 233–248.Ž .

<sup>w</sup> <sup>x</sup> 26 J.M. Polich, S.H. Schwartz, The effect of problem size on representation in deductive problem solving, Memory and Cognition 2 1974 683–686.Ž .

<sup>w</sup> <sup>x</sup> 27 M. Scriabin, R. Vergin, Comparison of computer algorithms and visual based methods for plant layout, Management Science 22 2 1975 172–181.Ž . Ž .

<sup>w</sup> <sup>x</sup> 28 H.A. Simon, Models of Man, Wiley, New York, 1957.

<sup>w</sup> <sup>x</sup> 29 D. Steiger, R. Sharda, B. LeClaire, Functional description of a graph-based interface for network modeling GIN , in: O.Ž . Balci, R. Sharda, S. Zenios Eds. , Computer Science andŽ . Operations Research: New Developments in their Interfaces, Pergamon, UK, 1992.

<sup>w</sup> <sup>x</sup> 30 M. Tracey, M. Dror, Interactive graphical computer application for large scale cattle feed distribution management, Decision Support Systems 19 1997 61–72.Ž .

<sup>w</sup> <sup>x</sup> 31 T.W. Trybus, L.D. Hopkins, Humans vs. computer algorithms for the plant layout problem, Management Science 26 Ž . Ž . 6 1980 .

Hasan Pirkul is the Dean of the School of Management at the University of Texas at Dallas. He concurrently holds the Caruth Chair of Management. Prior to joining UT-Dallas, he was at Max M. Fisher College of Business of the Ohio State University. A graduate of the University of Rochester, he received the MS degree in Management Science in 1980 and the PhD degree in Computer Information Systems in 1983, after earning a BS degree in Industrial Engineering from Bogazici University in 1977. Dr. Pirkul has served as Chair of The Institute for Operations Research and Management Science’s College on Information Systems as well as the Technical Section on Telecommunications in the same organization. He is the founding Editor-in-Chief of the Journal of Information Technology and Management. He has also served or is currently serving as an Associate Editor of leading academic journals such as Management Science, Operations Research and Journal of Database Management. In addition, he serves on editorial boards of a number of leading academic journals and has chaired and<sup>r</sup>or served on program committees of numerous conferences.

Rakesh Gupta is an Assistant Professor of MSIS at the University of Texas, Dallas. Prior to this, he was on the faculty at the Oklahoma State University. His research interests include design of telecommunications networks, visual interactive decision support, combinatorial modeling, analysis and heuristics. He has published in journals such as the European Journal of Operational Research, Information Systems Frontiers and International Transactions in Operations Research. He received a BE in Electrical Engineering from the Bangalore University, India in 1990, an MBA from the University of California, Riverside in 1992 and an MA and PhD from the College of Business at The Ohio State University in 1996.

Erik Rolland is an Associate Professor of Management Information Systems, The A. Gary Anderson Graduate School of Management, at the University of California at Riverside. His research interests include management and design of telecommunications systems, combinatorial modeling and analysis, and strategic MIS. He has published in journals such as Computers and Operations Research, European Journal of Operational Research, Transportation Science, and Annals of Operations Research. He received a BS in CIS from the College of Engineering, and an MA and a PhD from the College of Business all from The Ohio State University.
