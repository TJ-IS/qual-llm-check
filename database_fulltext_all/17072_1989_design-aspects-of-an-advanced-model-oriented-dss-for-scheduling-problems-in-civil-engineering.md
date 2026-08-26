---
otero_id: 17072
otero_key: "Z5UD36PP"
title: "Design aspects of an advanced model-oriented DSS for scheduling problems in civil engineering"
authors: "M Bartusch; R.H Möhring; F.J Radermacher"
year: "1989"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(89)90013-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Design Aspects of an Advanced Model-Oriented DSS for Scheduling Problems in Civil Engineering \*

M. BARTUSCH

Universität Passau, D-8390 Passau, FRG

R.H. MÖHRING

Fachbereich Mathematik, TU Berlin, D-1000 Berlin-10, FRG

F.J. RADERMACHER

FAW-Ulm, D-7900 ULM, FRG

The paper gives some design features of the architecture of a DSS for scheduling problems under development as part of a long-term project and designated as prototype for a new kind of advanced support system with strong AI potential. Support is intended for people in applications, scientific users and students. Main features are a thorough multi-attribute decision modelling, the incorporation of robust methods for stochastic models and the full incorporation of an enormous body of available algorithmic tools in the field. Other aspects are a number of features for a self-adaptive behaviour, several knowledge-based components and the availability of an Eigen-model of the system. In addition, the architecture also allows a “genetic” adaption cycle. The system will have components for explaining its own functioning, it is designed to document considerable parts of the used scientific knowledge in the area and will make parts of this algorithmic or modelling knowledge available via Computer Aided Instruction devices.

Keywords: Artificial Intelligence, Computer-Aided Instruction, Decision Support, Learning, Model-Management, Scheduling, Self-adaptiveness.

## 1. Introduction

In recent years, a number of statements have been made that ask for a more active and norma-

![](/api/attachments/Z5UD36PP/fulltext/images/6c20baa3df3b051d9eed98d519398ae8b746c3fb1531d8afc4b5d60d3ee6d7d6.jpg)

Martin Bartusch graduated in mathematics at the Technical University of Aachen, W. Germany. His professional interest was in applied mathematics, esp. combinatorics and combinatorial optimization, and in scheduling problems related to civil engineering. His dissertation, also at the technical University of Aachen, stemmed from those areas. He was one of the first to join the newly established faculty of mathematics and computer science at the University of

Passau in 1984. His spirit of openness, responsibility, and fairness made him quickly become equally liked by his colleagues and his many students to whom he was a dedicated teacher. He had always been interested in notions, not mere notations. It was when acting on something he considered to be of the most importance for our society that he was innocently killed in a car accident on July 19, 1986.

![](/api/attachments/Z5UD36PP/fulltext/images/f20ff76cec2ac3279f903b746c84441740cae35f52f7be122f44c328c5328474.jpg)

Rolf H. Möhring is Full Professor for Applied Mathematics and Computer Science at the Technical University of Berlin. His teaching and research interest are in the areas of algorithmic graph theory, combinatorial optimization, and software development for optimization oriented applications from engineering and economics. His research articles have appeared in numerous journals including Annals of Discrete Mathematics, Annals of Operations Research, Discrete Mathematics,

Mathematics of Operations Research, Operations Research, ORDER, and SIAM Journal on Computing.

![](/api/attachments/Z5UD36PP/fulltext/images/4baf927f6a213604f3cf27066db540704111b8fd2fec59a1398b7651667b602b.jpg)

Franz Josef Radermacher is the scientific director of the FAW (Artificial Intelligence Laboratory) Ulm and also has a faculty position for Data Bases/Artificial Intelligence at the University of Ulm which presently builds up a new Computer Science curriculum. Before, he was Professor of Computer Science and Operations Research at the University of Passau and took part in building-up a new Computer Science curriculum in this place. In 1980/81 he stayed at the

University of California/Berkeley as a visiting researcher. Prof. Radermacher holds Doctoral degrees in Mathematics from the Technical University in Aachen and in Economics from the University (TH) in Karlsruhe; his habilitation in mathematics was effected at the TH Aachen. Presently, he is also President of the Society for Mathematics, Economics and Operations Research (GMÖOR).

tively-based support of decision makers by means of a new generation of decision support systems [14], [24], [25], [30], [67]. It is common place that tools from AI such as learning features or knowledge-based components [19], [55], [60], [71] should play a major role in this context. This holds similarly for recent progress in interface development and also for a number of recent achievements in applied mathematics such as robust stochastic methods, methods for numerical stability and improved optimization methods.

The main problem of course is how to integrate these different elements into systems of high performance, i.e. into systems that adequately reflect the cognitive dimension associated with good decision making under difficult circumstances. In this paper we follow a framework that corresponds to the general theme of a special volume of Decision Support Systems [31] and that is centered around the following main aspects: Support a user in modelling essential parts of this problems as e.g. classes of multi-attribute decision problems under uncertainty, extract as much information from these models as possible to direct the dialogue with the user, use all available algorithmic tools for such models to generate normatively good solutions as proposals to the user, be able to explain the involved steps and, finally, provide an environment in which a number of versions of the system can be developed, studied and compared over a long time in parallel. A thorough discussion of principal aspects concerning systems of the indicated advanced nature is given by M. Jarke and F.J. Radermacher [24].

The given paradigm is developed simultaneously in a number of places for different applications, among which scheduling of projects in civil engineering acts as a kind of pilot system that addresses the practical realization of some of the major ideas in the field.

Scheduling is a good example for the kind of problems that should be approached in the way described, and it is also a field where a long-time expertise concerning modelling and algorithmic treatment is available, together with a great deal of experience in system development. The present paper is a report on main features of the architecture of a DSS for scheduling under development. It is a description of a system status aimed at within a period of five years, whereas a smaller prototype should be available within two years.

Some components do already exist, also a number of advanced development tools. Major specific aims desired are an architecture that allows a kind of genetic feedback cycle among configured systems (systems started by intermixing and modifying already existing systems in a suitable way), a life-long adaption and development of configured systems, an ability to adjust to individual users, a powerful internal world model for scheduling problems and – in addition – a detailed Eigen-model (to support dialogue handling, self-analysis and explaining) and, finally, a documented rich body of algorithmic tools where individual algorithms can be given to the user in form of Computer Aided Instructions (CAI).

The paper is organized as follows: In section 2 we give a short description of the specific type of scheduling problems and involved methodological aspects that we want to address with the system. We also give a list of more special functions that we would like to see supported by the system. In section 3, the basic system architecture is discussed. This architecture should principally allow the integration into a genetic feedback cycle and the individual adaption and self-modification of configured systems. From a methodological point of view, the architecture is oriented towards the necessary models involved, i.e. the scheduling world model, the dialogue and user model and the system's Eigen-model. In section 4 we concentrate on the discussion of the employed world-model. This means the right type of describing scheduling problems with emphasis being given to the right mixture of expressiveness and ease of handling. Concentration on this world model reflects the authors' main interest and the present state of system development. Concerning the world-model used, it is based on representing the mathematical core model with a great number of primitive operators and contains knowledge-based interfaces towards two ends, viz. to a user's private, informal word-model environment (allowing graphic tools, semi-natural language constructs, menus and direct manipulation options as e.g. input devices) and to a given physically distributed hardware. With regard to the mathematical core model, we give a short description of how some typical basic tasks (deduction steps) associated with the employed model will be realized via an advanced blackboard architecture. This covers in particular the competent and adaptive use of a great number of available algorithmic tools, and follows in this and other aspects the principal lines set up by M. Jarke and F.J. Radermacher [24]. The paper closes in section 5 with a short summary and some conclusions.

## 2. Decision Support in Scheduling

To promote the idea of advanced decision support systems, as argued for e.g. in [31], concrete pilot system developments are a necessity. With view to our strong orientation towards a normative type of support and towards modelling as important ingredient for advanced system performance, suitable application domains have to fulfill a number of requirements concerning available scientific background in modelling and algorithmic treatment. Also, as a start, the respective domains should be comparatively simple concerning interpersonal aspects of a game-theoretical nature, should allow a certain pre-determination and framing of the types of decision needed and should allow a deep modelling and advanced tool use embedded into the general framework of multi-attributive decision theory and applied stochastic models. Typical areas of this type are routing [5] and scheduling [36], [39], [53].

In the following we concentrate on scheduling, a topic of general importance for all kinds of planning systems. Presently, scheduling also constitutes the theme of an international joint system development competition [1]. We will report on a specific system development that particularly addresses scheduling problems in civil engineering. It builds on a number of completed research projects and system developments which have been carried out at the Technical University of Aachen since about 1970. These research projects were done in cooperation by computer scientists, mathematicians and civil engineers and are widely documented in the literature, c.f. [27], [45], [47], [48], [49], [50]. Among the participating scientists we mention here particularly R. Kaerkes (Aachen, †1979), W. Oberschelp (Aachen), M.M. Richter (Kaiserslautern) and R. Seeling (Aachen).

Work towards the kind of systems intended here was started at the University of Passau from 1983 onwards. It will now be continued as a major basic research project at the FAW in Ulm. The aim here is particularly to develop and evaluate new design methods and advanced types of tools that may be exploited in other, more applications-oriented research projects dealt with at the institute, including applications in CIM, office automation, environmental information systems, assistance systems and management of distributed resources.

The system parts presently available are a recent redesign of earlier versions, implemented on a SUN-3 workstation under the guidance of R. Felter (Passau) and with a strong participation of a considerable number of computer science and business administration students from the University of Passau [9] and specific components for knowledge representation and stochastic evaluation tools developed at the University of Passau and the Technical University of Berlin, respectively. The actual version contains three general purpose solutions for general problem variants, a number of fast transformation algorithms between different forms of data representation and an elaborate user interface. This allows input concerning user modelling via e.g. graphical tools and direct manipulation devices (cf. [7], [54], [58], [64]) and is advanced in some respect with view to translating such user inputs into mathematically equivalent (but formally much different) internal models used by the system for its own evaluation (cf. Example C).

Work is now under way at the FAW in Ulm to realize a prototype that addresses explicitly all the aspects discussed in this paper. Treatment of each single aspect may be narrow, as emphasis at this stage is on realizing the simultaneous interaction of all the different concepts involved.

In the following, we give a short introduction to the problems dealt with in the intended system. We mention here that from a very general point of view the aim is the planning of construction projects (e.g. houses, bridges and so forth) which are modelled as being composed of certain basic entities (so-called activities or jobs) that have to be worked on in a certain schedule.

So in general, we may think of a construction project as to consist of a set $A = \{\alpha_{1}, \cdots, \alpha_{n}\}$ of jobs, where jobs $\alpha_{1}, \cdots, \alpha_{n}$ have to be scheduled and then to be performed uninterruptedly, needing a deterministic or cost-controlled or stochastic job duration $x(\alpha_{j}) := x_{j}$ . Scheduling means finding appropriate schedules with respect to given sequencing conditions (in particular technological precedence constraints in form of a partial order on A) and time constraints between activities, several kinds of resource constraints, quite involved cost or preference structures, and either deterministic or cost-dependent or stochastic activity durations, possibly including stochastic dependencies.

![](/api/attachments/Z5UD36PP/fulltext/images/4daf05ac3eb403c3773ba818f89c6d9be7ac95d8bea7220bbad6fddcee29d730.jpg)  
Fig. 1. A Partial Order $\Theta$ of Sequencing Constraints.

In this context [3], a schedule may be identified with a mapping $S: A \to R_{>}^{n}$ that associates a starting time $S_{i} := S(\alpha_{i})$ to each job $\alpha_{i}$ . The mentioned conditions then mean constraints on the vector $S = (S_{1}, \cdots, S_{n})$ of starting times. For instance, if $\alpha_{i}$ must precede $\alpha_{j}$ , this means that $S_{i} + x_{i} \leq S_{j}$ . More generally, any pair $S_{i}$ , $S_{j}$ may be related to each other by a minimal and/or maximal time lag between them, i.e. by inequalities of the form $S_{i} + d_{ij}^{\min} \leq S_{j} \leq S_{i} + d_{ij}^{\max}$ with $0 \leq d_{ij}^{\min} \leq d_{ij}^{\max}$ . Pure time constraints may require $S_{i} \geq r_{i}$ (release date $r_{i}$ ) and $S_{j} + x_{j} \leq d_{j}$ (due date $d_{j}$ ). Resource constraints describe restrictions that model the fact that job $\alpha_{j}$ may require $r_{i}(\alpha_{j})$ units of a particular resource type $i \in I$ of which $R_{i} \geq r_{i}(\alpha_{j})$ units are available in total. Consequently, at any time $t \in R_{>}^{1}$ , the inequality

$$
\sum_ {\alpha_ {j} \in B (t)} r _ {i} (\alpha_ {j}) \leq R _ {i}
$$

has to be fulfilled for each $i \in I$ , where $B(t) := \{\alpha \in A | S(\alpha) \leq t < S(\alpha) + x(\alpha)\}$ denotes the set of all jobs being executed at time $t$ . In general, there may be many types of resources (bulldozer, cranes, ...) and a particular job may require many types of resources simultaneously for processing.

![](/api/attachments/Z5UD36PP/fulltext/images/3641d4153988e7bb614decb6fd0994ddb98e3d18a46943c3c12b1ec01d04bc5d.jpg)  
Fig. 2. A Feasable Schedule for Example A, Given by a Gantt Chart.

The quality of a particular feasible schedule (i.e. a schedule fulfilling all given constraints) is evaluated via a function $K \colon R_{\geq}^{n} \to R_{\geq}^{1}$ that associates a subjective cost or preference value to a schedule as a function of the completion times of all jobs, i.e. the evaluation of a schedule is $K(C) = K(C_{1}, \ldots, C_{n})$ where $C = (C_{1}, \ldots, C_{n})$ is the vector of the completion times $C_{i} = S_{i} + x_{i}$ of the jobs $\alpha_{i}, i = 1, \ldots, n$ . These functions are usually assumed to be regular, i.e. non-decreasing functions of the completion times [61]. Finding feasible schedules of “relatively low” cost is the aim of scheduling. In stochastic cases, this has to be interpreted for strategies instead of schedules [45], [49], [50] with view to online information acquisition and least expected cost instead of just cost.

To illustrate the scheduling model and the different aspects of the intended system, we consider the following example throughout the paper.

Example A: There are 16 jobs $\alpha_{1},\ldots,\alpha_{16}$ grouped into 4 chains of 4 jobs each. The underlying partial order $\Theta$ of technological precedence constraints is given in fig. 1 by an edge diagram (activity on edge representation). So e.g. in the first chain, $\alpha_{5}$ has to wait for $\alpha_{1}$ to be completed, $\alpha_{9}$ for $\alpha_{5}$ , and $\alpha_{13}$ for $\alpha_{9}$ . There are two types ( $i=1,2$ ) of scarce resources that are available in $R_{1}=1$ and $R_{2}=2$ units during project execution. They are required in one unit by $\alpha_{4},\alpha_{13}$ and $\alpha_{9},\alpha_{14},\alpha_{15}$ , respectively (i.e. $r_{1}(\alpha_{4})=r_{1}(\alpha_{13})=1$ and 0 otherwise, and $r_{2}(\alpha_{9})=r_{2}(\alpha_{14})=r_{2}(\alpha_{15})=1$ and 0 otherwise).

These resource constraints imply in addition to the technological precedence constraints that only one job out of $\{\alpha_{4}, \alpha_{13}\}$ and only two jobs out of $\{\alpha_{9}, \alpha_{14}, \alpha_{15}\}$ may be worked upon simultaneously at any moment during project execution. So if the processing times are given by

<table><tr><td>i</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td></tr><tr><td> $x_{i}$ </td><td>10</td><td>10</td><td>5</td><td>40</td><td>15</td><td>5</td><td>20</td><td>5</td><td>10</td><td>15</td><td>20</td><td>10</td><td>25</td><td>30</td><td>15</td><td>5</td></tr></table>

and every job is e.g. scheduled as early as possible with respect to the technological precedence constraints only, then there arises a conflict between $\alpha_{4}$ and $\alpha_{13}$ in the time interval [35,40] that could be resolved by delaying $\alpha_{13}$ , thus leading to the feasible schedule represented in fig. 2 by a Gantt chart (note that the particular processing times given do not create a conflict for the jobs requiring resource 2). So if K would be the maximum function (i.e. $K(C_{1},\ldots,C_{16})=\max\{C_{1},\ldots,C_{16}\}$ ), then this schedule would obviously be optimal, since the only other way in resolving the conflict between $\alpha_{4}$ and $\alpha_{13}$ would mean to start $\alpha_{4}$ only after the completion of $\alpha_{13}$ , which would lead to $K(C_{1},\ldots,C_{16})=120$ .

With view to formalizing a scheduling model, i.e. distinguishing jobs, durations, resource requirements, cost functions and so forth, there is always some freedom (which stimulated the development of specific expert systems as design tools [16], [70]). Also, there are different forms of hierarchical representation available [43], [52], that allow the building of scheduling models in an incremental form.

To achieve a good scheduling with view to a user's true problem, an advanced system has to address a broad spectrum of aspects. A short review of some of the major aspects needed (cf. [24]) and methods available in scheduling is given next.

First, a major practical problem is eliciting subjective information from the user concerning the constraints involved. Major demands for a DSS in this area include direct manipulation options for creating or deleting jobs, for fixing specific time windows, for adjusting resource constraints and for allowing an incremental form of project design, using earlier drafts of subprojects. The preference structure will often consist of aggregations of individual cost aspects, associated with the completion time of certain jobs or subprojects. Specific types of cost functions are discussed, e.g. in [61]; we mention two standard types $K := C_{\max} = \max\{C_1, \ldots, C_n\}$ , called project duration or makespan, and $K(C_1, \ldots, C_n) = \sum w_j C_j (w_j \geq 0)$ called weighted flowtime.

Eliciting the appropriate type of (subjective) cost function from the user, i.e. choosing the right function K, is an important task, but hard to realize. Promising is the use of disaggregation tools from decision theory as discussed in [11] and [29]. It is also important to consider techniques for debiasing in the elicitation of joint distributions of job durations and multi-attribute preferences (cost structures) concerning the completion time vectors of all jobs, cf. [10], [20], [21], [28], [51], [62].

For instance in Example A, we might know that the project cost depends on the project duration $C_{max}$ , but also on the early completion of job $\alpha_{13}$ and the “subproject” consisting of jobs $\alpha_{7}$ and $\alpha_{8}$ . This could be expressed to a certain extent by assuming $K(C_{1},\ldots,C_{16})=w_{1}C_{max}+w_{2}C_{13}+w_{3}\max\{C_{7},C_{8}\}$ , where $w_{1},w_{2},w_{3}$ are nonnegative weights representing the relative importance of the three goals. Other modelling aspects could, however, still be open. For instance, the information about the processing times of $\alpha_{5}$ and $\alpha_{7}$ could be rather vague, so that e.g. only intervals $x_{5}\in[10,20]$ and $x_{7}\in[10,30]$ might be specified.

A considerable problem in the user dialogue will be restrictions concerning the total amount of time a user is willing to spend for collecting information. For that reason, the dialogue has to be restricted to essential pieces of information not yet implicitly available. The approach here is to use aggregation techniques and robust solution methods described below in order to settle major aspects early and in a robust way, leaving the remaining time for improving solutions on a more detailed level.

E.g. in the above example, the processing times $x_{5}$ , $x_{7}$ are still not completely specified, but the system can already deduce that the project duration will be in the interval [65,75] for the given resource limits $R_{1}=1$ , $R_{2}=2$ , and even in [60,75] if $R_{1}$ increases to $R_{1}=2$ . Moreover, the respective best possible and worst case schedules can already be computed, possible conflict solving strategies for $\{\alpha_{9},\alpha_{14},\alpha_{15}\}$ (which may be necessary for varying $x_{5}$ and $x_{7}$ ) could already by analysed, etc.

The way of proceeding just described hinges on results available for the treatment of project networks. There are first fast algorithms for dealing with deterministic project networks without resource constraints. These include critical path methods and the identification of inconsistencies (CPM, e.g. [39], and MPM, e.g. [53]), methods for exploiting floats as discussed e.g. in [56], methods for time-cost analysis as discussed e.g. in [4], [53] and fast techniques for using structural decomposition, cf. [6], [43] and [52]. All this leads to the fast determination of “best” schedules for the respective problem formulations. E.g. given that the modelling (jobs, resources, ...) was correct, we can produce the normatively best solution in spite of a continuous time parameter being involved. In fact, it is mathematical theory and solution characterization that yields fast extraction of solutions from combinatorically exploding solution spaces in this case.

Turning now to problems with resource constraints, there are quite general types of background algorithms available using branch and bound methods, dynamic optimization and mixed integer problem formulations, cf. [3], [57] for an overview. Due to the continuous work of several researchers there is a quite complete insight available into up to 10000 special cases, for which either NP-completeness was established or specific efficient algorithms, using specific data structures, have been designed, cf. [36] for an overview. These special cases depend on special project structures [41], [42], (such as series-parallel networks, N-free networks or interval orders) or on special features concerning either job durations (e.g. identical job length), resource constraints (e.g. m-machine constraints) or cost criterion (e.g. makespan, weighted sum etc.). There are also fast identification algorithms for these special sub-cases.

E.g., in the above Example A it would be detected that the underlying partial order of technological precedence constraints is series-parallel. This means that polynomial algorithms exist for minimizing the weighted flowtime on one machine, and that stochastic evaluation of the project duration (see below) is easy. Moreover, the considered objective could be recognized as being transformable to a weighted flowtime objective by adding an artificial job after $\alpha_{13},\ldots,\alpha_{16}$ and another one after $\alpha_{7},\alpha_{8}$ , but at the cost of loosing the series-parallel structure.

For an appropriate treatment of project networks, stochastic aspects may be essential, e.g. due to the so-called phenomenon of “systematic underestimation” in deterministic problem variations without resource constraints. (This phenomenon tells that the expected project duration will always be at least as great as the project duration for the case that job lengths are assumed to be deterministic with their expected lengths [27], [39]).

E.g., if in the considered Example A, $\alpha_{5}$ , $\alpha_{7}$ are assumed as uniformly distributed on the given intervals [10,20], [10,30], then, not considering resource constraints, the expected project duration is 63.229, while the project duration based on expected processing times is only 60. Moreover, in 5% of all realizations, the project will take at least 69 time units).

In fact, as part of the sensitivity analysis that is continuously performed by background processes, models of that type have to be considered regularly via automatic stochasticization. For this important model class, various types of computational procedures are known, including (anti-thetic) simulation methods [69]. The “stability” behaviour of the model is so robust that simulation is adequate here. In addition, there are quite strong bounding techniques in the sense of stochastic orderings (cf. [8], [65], [66], [68] for an overview) which are based on the theory of associated random variables. When combined with the central limit theorem, these bounds can be obtained in a robust form, i.e. only involving expectations and variances of the respective activity duration distributions [66].

For Example A, the lower and upper bounds are identical because of the special structure of the partial order (parallel composition of chains) and thus equal to the distribution function F of the project duration (something which can be checked by the system). The calculated values of F (based on the exact distributions, cf. also fig. 3) are:

<table><tr><td>t</td><td>60</td><td>61</td><td>62</td><td>63</td><td>64</td><td>65</td><td>66</td><td>67</td><td>68</td><td>69</td><td>70</td></tr><tr><td>F(t)</td><td>0.25</td><td>0.33</td><td>0.42</td><td>0.52</td><td>0.63</td><td>0.75</td><td>0.80</td><td>0.85</td><td>0.90</td><td>0.95</td><td>1.00</td></tr></table>

The methods mentioned so far depend on the assumption of stochastically independent job durations. We just mention that due to some recent break-throughs in the theory of stochastic models there are now even robust techniques for determining (sharp) stochastic bounds (in the convex sense) against all kinds of stochastic dependencies, cf. [34], [38], [72].

The algorithmic techniques involved include dual linear programs and computation of minimal cost flows $[35]$ and are fast, whereas the (approximative) discrete representation of distributions is part of the input length of the problem encoding. With the various algorithmic tools mentioned available, certain principal decisions in aggregated models should often be possible pretty early while using comparatively aggregated user information.

The stochastic bound (in the convex sense) for Example A is given by $G(t)$ below, cf. also fig. 3. Calculations are based on discretizing the uniform distributions of $\alpha_{6}$ and $\alpha_{7}$ with 100 values in the

respective intervals.  
![](/api/attachments/Z5UD36PP/fulltext/images/22cb21eff27b691a977c680011712bfaf0dc479ddf2bd4a5867b31524f42cbea.jpg)  
Fig. 3. The Distribution Functions F and G from Example A.

<table><tr><td>t</td><td>60</td><td>61</td><td>62</td><td>63</td><td>64</td><td>65</td><td>66</td><td>67</td><td>68</td><td>69</td><td>70</td></tr><tr><td>G(t)</td><td>0</td><td>0.15</td><td>0.29</td><td>0.45</td><td>0.60</td><td>0.75</td><td>0.80</td><td>0.85</td><td>0.90</td><td>0.95</td><td>1.00</td></tr></table>

The bound on the expected processing time thus obtained is 63.825. These values show that stochastic dependencies among the two random job durations involved do not lead to an increase of the quantiles for the independence case for $t \geq 65$ . (The reason is that larger values are only due to job $\alpha_{7}$ , and no longer influenced by job $\alpha_{5}$ .) In general, “closeness” of the bounds $F(t)$ and $G(t)$ allows the system to neglect the influence of stochastic dependencies for all further evaluations and computations.

Particularly hard to deal with, and reasonably considered only in the form of aggregated model versions, are stochastic networks under resource constraints. Major insights include a hierarchy and normative classification of available classes of strategies (cf. fig. 4), results on the existence of optimal strategies and results concerning the stability behaviour and the monotonicity behaviour of the respective classes; in addition to quite sophisticated results on the determination of (approximately) optimal strategies (within certain classes of strategies) in special cases, cf. [45], [48], [49] and [50] for detailed overviews.

For instance, in Example A, the system might choose between the quite stable ES-strategies or the (for discrete distributions less stable) priority-strategies. ES-strategies solve the conflicts for scarce resources by introducing additional precedence constraints on “conflict sets”, e.g. $\alpha_{4}<\alpha_{13}$ on $\{\alpha_{4},\alpha_{13}\}$ and $\alpha_{9}<\alpha_{15}$ on $\{\alpha_{9},\alpha_{14},\alpha_{15}\}$ . This results in a partial order without resource constraints to which the already discussed techniques (e.g. stochastic evaluation) apply.

Depending on the relative weights $w_1, w_2, w_3$ in the cost function $K$ , there are two reasonable ES-strategies. If $w_2$ is small (completing $\alpha_{13}$ early is not so important) then $\alpha_4 < \alpha_{13}$ should be taken on $\{\alpha_4, \alpha_{13}\}$ , while both $\alpha_9 < \alpha_{14}$ and $\alpha_9 < \alpha_{15}$ seem reasonable for $\{\alpha_9, \alpha_{14}, \alpha_{15}\}$ . Evaluating the stochastic worst case bounds for the project duration in both cases yields means and variances of 66.9 vs 65.6 and 2.70 vs. 1.64. So $\alpha_9 < \alpha_{15}$ should be preferred on $\{\alpha_9, \alpha_{14}, \alpha_{15}\}$ . Evaluation of the associated independent lower bound yields the following distribution function $F_*(t)$ for the project duration,

<table><tr><td>t</td><td>65</td><td>66</td><td>67</td><td>68</td><td>69</td><td>70</td></tr><tr><td> $F_{*}(t)$ </td><td>0.75</td><td>0.80</td><td>0.85</td><td>0.90</td><td>0.95</td><td>1.00</td></tr></table>

which shows that $F_{*}$ is identical to the not resource restricted distribution function F truncated at t = 65.

If $w_{2}$ is large relative to $w_{1}$ , $w_{3}$ (i.e. completing $\alpha_{13}$ early is the most important goal), then the additional precedence constraints should be $\alpha_{13} < \alpha_{4}$ on $\{\alpha_{4},\alpha_{13}\}$ and $\alpha_{14} < \alpha_{15}$ on $\{\alpha_{9},\alpha_{14},\alpha_{15}\}$ .

![](/api/attachments/Z5UD36PP/fulltext/images/a2a5b1ca97953bdf742907e6a2889b9bc2bd40c825938fb7cd0448925bab37ae.jpg)  
Fig. 4. Classification of Important Classes of Strategies [45].

Priority strategies solve the conflicts by introducing a (static or dynamic) priority list on the jobs according to which the conflicts in assigning scarce resources are settled during project execution. Such a static priority list could prefer $\alpha_{4}$ above $\alpha_{13}$ , $\alpha_{9}$ above $\alpha_{15}$ and $\alpha_{15}$ above $\alpha_{14}$ . For the special distributions/durations given, the system would recognize that this priority policy is equivalent to the ES-policy with $\alpha_{4}<\alpha_{13}$ and $\alpha_{9}<\alpha_{15}$ , and thus not evaluate it. This changes, however, if e.g. the processing times of $\alpha_{1}$ and $\alpha_{15}$ increase.

For instance, if $x_{1}=30$ and $x_{15}=40$ , then the above priority rule would lead to a better project duration distribution. This could be detected by simulation techniques (restricted to a small number of realization vectors because of the usually high computational effort). In the example, the following distribution functions of the project duration are obtained (F: priority strategy, G: ES-strategy with $\alpha_{4}<\alpha_{13}$ and $\alpha_{9}<\alpha_{15}$ ).

<table><tr><td>t</td><td>90</td><td>91</td><td>92</td><td>93</td><td>94</td><td>95</td><td>96</td><td>97</td><td>98</td><td>99</td><td>100</td></tr><tr><td>F(t)</td><td>0</td><td>0.05</td><td>0.11</td><td>0.18</td><td>0.24</td><td>0.81</td><td>0.86</td><td>0.90</td><td>0.94</td><td>0.97</td><td>1</td></tr><tr><td>G(t)</td><td>0</td><td>0.08</td><td>0.17</td><td>0.28</td><td>0.39</td><td>0.50</td><td>0.60</td><td>0.70</td><td>0.80</td><td>0.90</td><td>1</td></tr></table>

Though the means are similar (94.68 and 95.07), $F$ has a much better variance (3.60 instead of 7.81) and smaller high percentage quantiles (the $80\%$ quantiles are 95 and 98, respectively).

Based on these and other algorithmic tools, the designated DSS aims e.g. at the

-elicitation of needed user information,

-permanent decision support, even under limited information,

-design of solutions,

-detailed scheduling and constant updates of schedules,

-interpretation and justification.

Along the line of the general design aspects for advanced decision support systems given by M. Jake and F.J. Radermacher [24], the methods applied are as follows:

1. Embedding of the algorithmic and theoretical knowledge just described into integrated data, algorithm and model bases with sophisticated tools for the efficient handling of these integrated bases.

2. Consequent use of appropriate, clear mathematical background models as a kind of “intellectual interface” that separates the methodological part from the user dialogue and the distributed processor environment used; cf. Example B below. Consequently, the range of acceptance of user inputs will incrementally be defined by the availability of fast transformation algorithms that translate in a knowledge-based way certain types of user inputs consistently into the background models.

3. Algorithmic treatment of problems via a number of concurrent processes organized by a blackboard architecture that focusses on-line on the most promising algorithmic procedures.

Concerning this aspect, results from coarse models already treated as well as indications by experienced practitioners will serve as a guideline for the concentration on potentially interesting sub-spaces of the feasibility set, thus avoiding some of the usual problems with combinatorial explosions. In addition, the methods of CPU-time assignment to procedures will be subject to a continuous adaptive modification, induced from the feedback of observed performance.

4. Finally, the explanatory features of expert systems are appropriately to be adjusted to the more general framework discussed here. In particular, the respective status of the assignment procedures and the on-line results in the computation of bounds will form essential information. In particular we mention the fact that even in NP-complete problems bounds may often be verified fast.

Now, before dealing in more detail with the architecture of the scheduling system, we summarize here as reminders a number of more specific functionalities that we would like to see offered to the user by the intended system.

## 2.1. Support User's Modelling

\- Be able (as part of the modelling) to support individual user preference structures concerning all kinds of system behaviour. Such preferences should be expressed with reference to the system's Eigen-model and the dialogue model. In Example A, such aspects could concern the possible stochasticification of only the two "vague" jobs $\alpha_{5}$ , $\alpha_{7}$ or of all jobs, the conflict solving strategy (ES-strategies or priority-strategies), etc.

\- Accumulate statistical information about the operators available and components that a user handles. Give references to other or more efficient alternatives in a suitable way.

\- Be able to translate modal statements like "earlier", "much earlier", "later", "more resources", "less resources" and so on in a user-specific way when building up internal representations of specific applications. Note that this notions can quite easily be interpreted within the framework of temporal and resource constraints offered by the respective underlying modelling of a given scheduling problem. E.g. when a job starting time may vary between $8 \leqslant S(\alpha) \leq 16$ , and the job is presently scheduled at $S(\alpha) = 14$ , "earlier" may mean $S(\alpha) = 10$ , "much earlier" $S(\alpha) = 9$ and so on.

## 2.2. Support of Expert Users

## Visualization

\- Present schedules in different representation forms (different types of representation may lead to new inspirations [7], [26]).

\- Be able to present all kinds of probability distributions in different forms, allow graphical manipulations of distributions; be able to smoothen empirical distributions analytically (e.g. via the use of Pearson types [32]); be able to handle arbitrary distributions either analytically or via simulation; make distributions easy to modify with view to mean value, symmetry, support, modal value and so forth.

## Treatment of Examples

\- Offer high-level tools for the creation of examples, i.e. allow hierarchical representation e.g. by substitution decomposition [43] and high-level statements like “stochastify”. In doing so replace automatically deterministic values by random ones (e.g. by choosing distributions from certain classes, using e.g. given expected values or variances, randomly taken out of given intervals) and so forth. Allow random and high-level modification of job durations, resource demands and supplies etc. Organize problem representation in a way that a full data base management and query language system (such as SQL) may be used for these purposes.

\- Offer also a full data base support for the formulation of requests for examples with certain properties that a system should try to find on its own, possibly using the high-level modification operators just mentioned.

## Scientific Documentation / On-Line Test Environment for New Algorithmic Tools

\- Be able to explain the algorithmic tools used in specific situations, including previous basic data-transformations and adjustments. This should also include hints to possible forms of approximation. (As an illustration of the richness of aspects involved at this stage, we refer to Example 6 in [58] that deals with weighted sum $m$ -machine scheduling problems [46]. Here a bound to the optimal value is found via a related 1-machine problem that allows nice handling for particular types of underlying sequencing constraints.)

\- Keep basic references to the tools used and maybe even text files of basic papers.

\- Promote knowledge transfer from universities to applications by this modern way of direct incorporation of new algorithms into systems. In doing so, also deliver the needed basic data structure transformations that may be required when using the new tools.

\- The system has to be sufficiently modularized, so that new implemented algorithms can be added fast to the system [9].

\- Be able to generate test examples to validate the use of new tools for particular problem classes.

\- Maintain a long-time statistical record of the power of particular algorithmic tools for particular problem types and be able to communicate this type of knowledge to an expert user in adequate ways.

\- Note that this is also required for components of e.g. the user model, the dialogue model or the system's Eigen-model.

## Computer-Aided Instruction

\- Be able to deliver computer-aided instructions for basic algorithmic tools used, employing appropriately prepared examples. In a longer perspective this should hold similarly for the explanation of the functioning of the whole system and its main components.

## 2.3. Support of Users in the Application Domain

## Internal Model Building

\- Be able to build classes of internal models of a particular problem instance from all kinds of user inputs, i.e. of explicit, graphical or natural language type (see Example A for the potential treatment of notions such as “earlier” or “more resources of a certain type”). Note that the needed knowledge-based transformations of given inputs into the standardized internal model representation may be very involved; e.g. in Example C, we report on how time varying resource supplies and demands may be translated into a model with constant requirements of this type (cf. also [58]; this translation requires the introduction of new “artificial” activities, new constraints, modification of the cost function used and so forth).

Table 1  
Bounds on the Project Duration for Different Types of Randomization.

<table><tr><td></td><td>t</td><td>40</td><td>45</td><td>50</td><td>55</td><td>60</td><td>65</td><td>70</td><td>75</td><td>80</td><td>85</td><td>90</td><td>95</td></tr><tr><td rowspan="3">δ=0.1</td><td>F*(t)</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.03</td><td>0.50</td><td>0.97</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>F*(t)</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.01</td><td>0.49</td><td>0.97</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>G(t)</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.32</td><td>0.88</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td rowspan="3">δ=0.2</td><td>F*(t)</td><td>0</td><td>0</td><td>0</td><td>0.03</td><td>0.20</td><td>0.50</td><td>0.80</td><td>0.97</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>F*(t)</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.02</td><td>0.30</td><td>0.79</td><td>0.97</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>G(t)</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.51</td><td>0.88</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td rowspan="3">δ=0.4</td><td>F*(t)</td><td>0</td><td>0.02</td><td>0.08</td><td>0.20</td><td>0.33</td><td>0.50</td><td>0.66</td><td>0.80</td><td>0.90</td><td>0.97</td><td>1</td><td>1</td></tr><tr><td>F*(t)</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.03</td><td>0.14</td><td>0.40</td><td>0.71</td><td>0.90</td><td>0.97</td><td>0.99</td><td>1</td></tr><tr><td>G(t)</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.25</td><td>0.60</td><td>0.88</td><td>0.98</td><td>1</td></tr></table>

\- In incremental model-building, keep track of the way a model may be obtained in a hierarchical manner by integrating sub-models. Be able to refer to such decomposition possibilities in later computations. This may also include small model changes if this leads to better tractable instances that may deliver upper or lower bounds, or suitable approximations.

\- Be able to perform all kind of background analysis without the user noticing it. This should include automatic stochasticization (possibly including stochastic dependences) and other forms of sensitivity analysis. Try to propose only those solutions that are sufficiently robust in this respect. If stability is questionable, give warnings to the user. The style of warning should again be oriented towards the user's abilities and pre-knowledge.

Table 2  
Bounds for the Expected Project Duration.

<table><tr><td></td><td> $\mu^*$ </td><td> $\mu_*$ </td><td> $\mu$ </td></tr><tr><td> $\delta = 0.1$ </td><td>64.948</td><td>65.170</td><td>66.543</td></tr><tr><td> $\delta = 0.2$ </td><td>64.958</td><td>66.994</td><td>70.441</td></tr><tr><td> $\delta = 0.4$ </td><td>65.163</td><td>71.697</td><td>79.046</td></tr></table>

In Example A, an automatic stochasticization of all jobs could be done by taking the given deterministic processing times as means and calculating the mentioned stochastic bounds with respect to different variances for both the technological network (e.g. without resource constraints) and some ES-strategy. This is done here by assuming that the processing time of each $\alpha_{i}$ is uniformly distributed on the interval $[x_{i}-\delta x_{i},x_{i}+\delta x_{i}]$ , where $\delta\in(0,1)$ is a variation parameter determining the length of the interval (and thus also the variance $\sigma^{2}$ of the uniform distribution as $\sigma^{2}=(1/3)\delta^{2}x_{i}^{2}$ ). For $\delta=0.1$ , 0.2 and 0.4 one obtains the bounds given in table 1 for the ES-strategy with $\alpha_{4}<\alpha_{13}$ and $\alpha_{9}<\alpha_{15}$ ( $F_{*}/F^{*}\equiv lower/upper bound$ for the independence case, $G\equiv worst case lower bound$ for stochastic dependencies). For the expected project duration, one obtains the values given in table 2 ( $\mu^{*}\equiv F^{*}$ , $\mu^{*}\equiv F^{*}$ , $\mu\equiv G$ ). They show that a simultaneous large variation of durations for all jobs makes it hard to obtain good bounds and good solution proposals (e.g. the large interval [75,83] for the 80% quantile of G). So it is essential that the user can limit the number of jobs with large variation (e.g. in the original Example A only to $\alpha_{5}$ and $\alpha_{7}$ with a variation of 0.33 and 0.5, respectively).

With respect to the cost function K, an automatic sensitivity analysis would detect a possible instability if $w_{2}/(w_{1}+w_{3})$ , i.e. the relative importance of an early completion of $\alpha_{13}$ increases. Then both in the class of ES-strategies and the class of priority policies, the discrete structure of the optimal strategy changes completely (e.g. $\alpha_{4}<\alpha_{13}$ changes to $\alpha_{13}<$ $\alpha_{4}$ with great influence on the completion of $\alpha_{4}$ , $\alpha_{8}$ , $\alpha_{12}$ , $\alpha_{16}$ ).

## On-Line Update During Realizations

\- Given daily reports on work progress in typical applications in the construction industry, a system should be able to update continuously its proposed scheduling. In doing so it should monitor the stability of the proposed solutions continuously with view to basic aims. Dangerous situations may arise e.g. if jobs are late and, as a consequence of this, foreseeable problems (i.e. of weather type or concerning the start of other construction projects) come into view. A system should be able to propose even a substantial rescheduling, but in doing so, it should appropriately take into account additional (opportunity) cost resulting from such rescheduling.

## Incremental Building of Internal Models of Particular Problem Instances

\- Explicit modelling of users with view to their subjective preferences and probabilities; different forms of visualization of such modelling; offering of a great variety of default-options in this respect; implementation of debiasing tools [20]; hints to utility dimensions possibly missing in decision model framing, as proposed e.g. in the MAUD system [22]; indirect forms of finding fitting preference structures, as realized e.g. in the PRE-FCALC system [23].

\- Using direct or implicit indications by the user to update, narrow or added precision to the actual internal model of a particular problem instance. Major hints will result from non-acceptance of proposed solutions. This will usually lead to a modification of e.g. constraints and preference structures.

For instance, if the user does not accept in the solution of Example A that $\alpha_{4}$ completes after $\alpha_{10}$ , he might introduce the new precedence constraint $\alpha_{4} < \alpha_{10}$ . This would not only necessitate recomputations of proposed solutions, but also influence the availability of tools (in this case of stochastic evaluation methods since the new, augmented precedence constraints are no longer series-parallel).

\- Report cycles in updates or explicit or implicit contradictions in user hints, at least as far as they can be identified by “short” inference chains.

For instance, preferences to complete a job $\alpha_{j}$ early might contradict the wish to introduce a (technologically not necessary) precedence constraint $\alpha_{i} < \alpha_{j}$ .

\- Report inconsistencies on the level of constraints and optimization aims. Note that in general scheduling problems, inconsistency checking is already an NP-complete algorithmic problem [3], [13] that has to be handled accordingly.

For instance, inconsistencies due to the modification of the temporal constraints (precedence constraints or time lags) can efficiently be detected by shortest path techniques. So if in addition to $\alpha_{4}<\alpha_{10}$ , the user would also introduce a due date of 80 for $\alpha_{14}$ , then the system would detect that there is no feasible solution since the chain $\alpha_{4}<\alpha_{10}<\alpha_{14}$ requires 85 time units of processing. Checking becomes, however, NP-complete if due-dates or maximal time lags between jobs are involved together with resource constraints. So it is not so easy to check whether, for any realisation of processing times, it is possible to complete $\alpha_{9}$ , $\alpha_{14}$ , $\alpha_{15}$ before time 60.

In particular, if consistency cannot be established in time, it has to be handled as an inconsistency. In this case, appropriate alternatives for the relaxation of constraints have to be proposed. Such alternatives should be selected according to assumed user preferences and general user aims.

## 3. Design Aspects of the General Architecture of the Scheduling System

When speaking about a scheduling system in the following, we have in mind the general adaptation principles discussed in detail by Jarke and Radermacher [24], see fig. 5.

This means that (in principle) we would like to accomplish that new systems (so-called “configurated systems”) may be generated from “populations” of already existing systems via genetic strategies [12], [17], and that configured systems, once in use, may continuously be modified automatically during their life-time via adaption or learning processes.

Such adaption processes concern on a more obvious level the probability with which certain actions are performed in a particular system's state. Here, previously successful actions will receive a higher probability over time through the adaption process (employing, however, an annealing strategy [33], [59], [63] or similar approaches [15] in the update process). On a deeper level, the update process should (potentially) also be able to modify state descriptions. This is done in a way as e.g. demonstrated in Lenat's AM system [37]. Here an essential feature is that new state definitions and associated operators are recursively traced back via logical or set theoretical operators to the originally given state notions and associated operators, which thus function as a common reference frame for the whole “population of systems” over time. All system components will be realized in a strictly object-oriented way with object-oriented state and action descriptions that encapsulate all relevant references to this common notational frame.

![](/api/attachments/Z5UD36PP/fulltext/images/290c9d8dae64f30943053fb1aade8bf8860fe5c289e808bc5a59182ac8716c7a.jpg)  
Fig. 5. Potential Adaption Frameworks for the Scheduling System.

Note that due to this general design aim, systems have to be highly modularized. The system's Eigen-model will contain the basic (tree-like) structure of this modularization. Genetic adaption will mean the randomized copying of the modules of one or another configured system in a top-down fashion (according to the tree structure) with a potential modification of some parameters to mimic purely random mutations.

Participation of configured systems within this “creation” process is determined by a user evaluation of the overall function of a system or its components, where successful systems or components are favoured. Note that due to the type of modularization and module adaption chosen, corresponding modules can be replaced arbitrarily between configured systems, always leading to (new) operational systems. This is true in spite of the fact that the respective internal states may be quite different over time, not to speak about all kinds of parameters. Concerning state-modifications, major problems concern the update of activation parameters for actions in case of such a modification. I.e. if we split a previous state into a number of sub-states (maybe orientated on the respective values of some other functions) or if we integrate some previous states into a new (super) state, we have accordingly to adjust the probability to do certain actions when being in this new state. Note that with this type of approach a configured system will over time accumulate knowledge concerning the use of certain tools or components, that is statistically evaluated and adapted in a notational framework that originates from earlier systems and own previous adaption processes.

Due to the degree of randomization involved (which allows a rather smooth adaption process), much of the apparent behaviour of a system will stem from concurrency phenomena (i.e. in generating random numbers or concerning the concrete application problems treated and the order in which they appear). Consequently, it will be hard to predict what a system will do next for a real problem instance. Known to the system builder (and maybe user) is only the general framework in which the reactions of the system can be located.

This is sufficient insofar as our major ultimate aim is the achievement of good solution proposals to user requests. To the degree we normatively cannot achieve “the best answer” in time, we may instead navigate in the area of “apparently about best answers possible” to exploit very general user feedback to improve the system’s behaviour. Genetic and statistical adaption are the available and employed tools in this context.

To arrive at an intuitive understanding of how we would like the system to behave, we think of an interaction between a user and the system, in which the system tries to mimic a supporting team of application experts, experts in decision-theoretical framing, experts in deep modelling, in tool use, in the use of distributed processor environments and so forth. Apparently, this seems to be the right type of approach for advanced normatively based decision support.

The course of the dialogue is derived from a dialogue model (classifying e.g. user competence)

that, among other things, determines the degree to which activity comes from the system and to which degree the system allocates time to tasks such as background sensitivity analysis, consistency checking or self-analysis. Restricting to interactions with users from the application domain, the driving paradigma in the dialogue will be the building-up of sufficiently precise models of the respective application problem instance (as part of building a scheduling world model). This is combined with proposals of solutions and resulting modifications of modelling in the course of the dialogue with the user, including, in particular, his reactions to proposals.

The organization of the system's behaviour on a more technical level is then oriented along the state-action approach, where a choice of actions is usually done in an appropriate randomized fashion (containing, of course, deterministic transactions as – on a whole – dominating special case). Important is the richness of state and action spaces, arrived at via hierarchies of object-oriented nestings of sub-states and sub-actions.

Note that on a high level, states are composed from state aspects derived via the four major models (see fig. 6) involved in the proposed architecture, i.e. the system's Eigen-model, the user model, the dialogue model and the scheduling world-model (that we will discuss more detailed in the next section). So as an example, a high level state may be composed by the following four aspects:

![](/api/attachments/Z5UD36PP/fulltext/images/943b86aac7c7bf5d0128c12ea7ea71e90771f70af236c601b695404573e7dffe.jpg)  
Fig. 6. A Nesting and Integration of Needed Models.

## Example B:

\- The system classifies itself as working interactively with a user in building-up a first model of a particular problem instance; information concerning the user's preference structure is missing, except for a list of general requirements he wants to see fulfilled by solutions, if possible. Apart from that, the system internally sees a high need of adapting its component for generating preference structures due to long modification phases in the last ten application sessions (state of the system's Eigen-model). - The user is classified as non-expert user, he has no knowledge of utility and probability theory; he does not want to be bothered with details; he wants primarily that a number of certain general requirements concerning solutions are fulfilled (state of the user-model).

\- The dialogue is characterized by the user's preference for menus and graphical visualization and obvious non-acquaintance with a number of powerful system functions such as certain direct manipulation devices; the user seems to have little time left over for the present dialogue (state of the dialogue-model).

\- The system has available a (first) model of the user's actual application problem, consisting of a list of activities, sequencing and precedence constraints among these activities, resource requirements and availabilities, a number of general aims to be met (e.g. completion of particular sub-projects or jobs either before certain due dates or as early as possible). A number of activity durations is given. For the other activities there are intervals known in which the durations are located. It is not clear whether durations are drawn randomly from these intervals according to some distribution or whether the user has no or additional information concerning this aspect. The system has not yet checked the consistency of the model with view to e.g. some "random" drawings of potential duration vectors fulfilling the actual state of precision in the model formulation (state of the scheduling world-model).

E.g. in the concrete situation of Example A, a coarse model of 4 parallel tasks is identified via the graphical interface which then is refined into the project structure given in fig. 1. The user is then prompted for the resource constraints, the possible processing times and his preferences concerning completion times. All this may result in the data described in Example A above. At this point, the system does - on the background - a consistency check and, since the project duration is involved as optimization aim, some analysis on the range of the project duration, possibly together with an automatic stochasticization as described above. An evaluation of the preference structure might result in preferring a small project duration above an early completion of job $\alpha_{13}$ . Combining these results, the system then might propose the ES-strategy with $\alpha_{4}<\alpha_{13}$ and $\alpha_{9}<\alpha_{15}$ as solution and display the calculated bound on the project duration, and also for the subprojects defined by $\alpha_{13}$ and $\alpha_{7}$ , $\alpha_{8}$ respectively. Parallel to this solution proposal, another process could have analysed the problem structure and have noticed that the precedence constraints are series-parallel and that the objective is close to a weighted flowtime criterion (see the earlier remarks).

Remember that the given (informal) high state description summarizes formal representations that are based on references to a hierarchy of respective sub-states. The system's reaction to such a state results from an internal organization that is oriented along the lines of the AM system [37] mentioned above. I.e. with reference to a general, hierarchically-organized and object-oriented agenda of tasks to work on, interesting sub-tasks that should be attacked are identified. General agenda tasks may be "build model of user problem", "check model consistency", "compute solution proposal", "perform a sensitivity analysis", "update our Eigen-model" and so forth. Tasks identified as important in the present state may be worked on in the respective (distributed) software and hardware environment. Usually, this will mean that with a certain probability, certain processors may be attributed to a certain task for a certain time. In an hierarchical fashion this is extended in an interdependent way towards appropriate subtasks and respective algorithmic tools via multiple blackboard architectures; there, a finally identified (sub-)task to be worked on for a certain time opens a blackboard in which suitable algorithmic tools offer their participation, possibly together with promises of achievement in the available computation time. Such promises are an essential element in selecting employed tools. Their appropriate update forms an essential part of learning and statistical adaption.

We give details to this basic organization scheme in the next chapter. In the present context it is sufficient to note that eventually “good” tools will work on “reasonable” sub-tasks for certain time-intervals, thereby exploiting the processor environment to the extent possible.

In this typical situation the next state will either be induced by a user interaction or by a working tool producing an (intermediate) desired result or by the time attributed to a particular tool being used up. With one of these incidents happening, the whole cycle of processor allocation to tasks and appropriate tools is restarted again.

More comments on technical aspects follow in the next section with special emphasis on the part of the scheduling world-model.

E.g. in Example B, five sub-tasks from the general agenda might be identified as important to work on. These are:

1. Working on the user's preference structure concerning his general requirements;

2. Updating the system's preference-modelling component;

3. Informing the user on some comfortable direct manipulation tools that might considerably shorten the further dialogue;

4. Trying to find out whether the available information on activity durations can be made more precise through a dialogue with the user. This may mean the elicitation of information concerning distributions or the narrowing of variation intervals (hopefully to single values);

5. Do consistency checking to focus the dialogue, particularly with view to tasks 1 and 4.

Note that due to the user's limited time and his interest in more general aims there should be a strong emphasis on working on task 1. This will mean choosing certain different strategies for finding out the preference structure of the user. These reach from indirect approaches to asking for pairwise comparisons for vectors of results or instead to trying to establish certain types of utility independence properties between certain aims of the user; proposing default models may be an alternative as well.

So in Example A, the system would notice the mentioned instability resulting from the goals to finish $\alpha_{13}$ early, and to complete the whole project early. It could propose feasible solutions based on the two ES-strategies discussed above, and then deduce that the user prefers a small project duration above an early completion of $\alpha_{13}$ .

One should expect that task 2 will not find particular interest in situations of time pressure as assumed. However, given that the update is precisely concerned with the preference modelling component, some emphasis may not be wrong.

In fact, this may constitute a very difficult (internal) decision problem for which also a human has no definite answer. Consequently, a system may accumulate experience in this respect that might outperform (quick) human guesses. Obviously, this also applies for task 3. A very essential input into the processor allocation device will in this situation be given by estimates concerning the time that a user of the respective user type will need to handle the direct manipulation tool competently, and the time that might eventually be gained while elicitating the user's preference structure concerning his general requirements with precisely this tool.

The arguments concerning the task 4 are very closely connected to task 5 and certainly depend on the degree of uncertainty still involved as well as on previous user reactions concerning this point. Certainly, if vagueness about activity durations is significant, solid solution proposals for the user may be out of reach, even if his preference modelling would be carried through accordingly.

For instance, in the beginning, the user could only be able to supply average processing times for Example A that, after the total stochastification mentioned above, could be reduced to deterministic values except for the highly time sensitive jobs $\alpha_{5}$ and $\alpha_{7}$ for which only the above mentioned intervals [10,20] and [10,30] can be specified. The stochastic analysis is, however, at this point already strong enough to make good solution proposals (priority-policies are not better than ES-policies, the stochastic worst case bound on the project duration is concentrated on the small interval of [65,70]).

Task 5 offers maybe the most comprehensive potential for the kind of advanced support that we envision. Again, a human will generally not be able to give a competent advice of how much processor capacity to allocate to this type of activity. Remember the mentioned computational explosion from still polynomial consistency checking for temporal constraints only and the NP-complete consistency checking for simultaneous upper bound temporal constraints and resource constraints. Certainly, with view to our general design agenda for advanced systems, here is the point where a system may gain (implicit) information that allows to focus the dialogue and, in addition, to eventually overcome some data acquisition problems. This aim is of particular importance with view to a non-expert user with time needs and only quite general requirements concerning solutions.

As an example, the system might e.g. consider a number of duration vectors within the present modelling stage and test for consistency concerning general time requirements. The duration vectors might be drawn somehow randomly from the respective intervals, but they might also be the respective upper or lower bounds or the mean values of the intervals and so forth. If consistency checking leads to inconsistency in some (most) cases, emphasis on task 4 should strongly be increased, including (perhaps) system proposals on how to relax certain constraints. I.e. there is not so much sense in preference structuring as long as there are no feasible schedules available at all.

For instance, if the user wants simultaneously the additional precedence constraint $\alpha_{4}<\alpha_{10}$ and the due date d=80 for $\alpha_{14}$ , the system would detect an inconsistency resulting from these two new constraints, inform the user accordingly and ask for possible relaxations (increase due date or make it part of the cost function, relax precedence constraint by start-to-start time lags, etc.).

In a different scenario, only very special solution types might be possible. This could imply that with view to the general requirements of the user, concerning a number of them, there is no freedom left, while for others freedom is very restricted. In this situation, the dialogue can be focussed in a very efficient way. On the one hand, the observed restrictions have to be communicated appropriately to the user, offering some previously checked alternatives for the relaxation of constraints in order to re-gain an increased degree of freedom. On the other hand (i.e. if the constraints will not be relaxed), the modelling of the preference structure can be considerably simplified by focussing precisely on the still remaining freedom concerning realizable alternatives. Certainly, this type of system behaviour is much advanced and constitutes the type of extended, normatively-based decision support asked for with view to future generations of such systems [30], [31].

## 4. World Modelling in Scheduling Applications

The adequate modelling of the application domain is the ultimate basis for the system's competence in proposing solutions for particular problem instances. Modelling in the scheduling domain with particular emphasis to applications in the building industry is a major research interest of the authors, and we will therefore discuss the system architecture represented in fig. 7 in this respect in more detail in this section.

Remember the general guideline which assumes that at any stage we are confronted with a (partial) modelling of the problem instance and have to make proposals, either for solutions or for additionally needed data from this (partial) modelling. As we are up to a normatively adequate modelling of the user's problem, the modelling framework has to be vast and general. This, at the same time, will avoid a situation where a system's competence is extremely narrow with sharp boundaries. The price for such a generality will, however, be that resulting models may be very nasty. If this is combined with the option of only (partial) modelling and the simultaneous modelling on different stages of granularity, the available algorithms and operators must necessarily be tailored to deal with quite involved tasks.

The question for the right type of model framework is most crucial in system design and means the balancing of a great number of aspects. Our proposal for scheduling in civil engineering applications has been developed and discussed in a number of papers, cf. e.g. [3], [27], [45], [47], [48], [57]. We summarize here the following essential features:

\- non-preemptive models (i.e. jobs, once started, have to be completed uninterruptedly);

\- arbitrary precedence constraints in the partial order-oriented core model and arbitrary time constraints between starting and completion times of any two jobs in the general scheduling model;

\- arbitrarily many constant resource constraints; each job may require different resource types and several units per type;

\- fixed or random activity durations;

\- arbitrary regular cost (preference) structures, based on the completion times of jobs;

\- substitution decomposition for hierarchical model representations and evaluations.

Note that there is a price in algorithmic efficiency when going over to the general scheduling model, instead of staying with the partial order-oriented core model which is a special case of the general version whose applicability can easily be checked. This applies particularly also to the richness of hierarchical representation possibilities, the stability behaviour and forms of stochasticification. From the point of precedence and resource constraints, the model is as general as possible, as long as a fixed project structure is assumed. With view to resource constraints, the model is again extremely liberal. A very well-considered design decision is, however, the restriction to constant resource requirements and availabilities over time [3], [57]. Note, that this does not mean the exclusion of handling more general examples, though. We have already mentioned that, as part of a knowledge-based translation of user modelling requirements into the required standardized form, such generalizations may at present or later be accommodated. In fact, with view to non-constant resource requirements, release dates (earliest starting times of jobs) and due-dates (required completion times of jobs) this is already realized in the available prototype system [9]. The way this is done is demonstrated in the following Example C, cf. [58].

![](/api/attachments/Z5UD36PP/fulltext/images/fdeded7e3f2b4376a7dad23a5e1429fcce1379d8fc0f383ccdbee0f0128cd60c.jpg)  
Fig. 7. Modelling Components.

![](/api/attachments/Z5UD36PP/fulltext/images/d5f5c403c52e3548a13a6865715dea14f7e60525390f220651646512c018c960.jpg)  
Fig. 8. Resource Availability Curve.

Example C: Standard internal normalization of non-constant resource availability. Suppose that the availability of a resource over time $t \in R_{\geq}^{1}$ is given by the piecewise constant curve of fig. 8. This is internally normalized by assuming a constant bound of $R = R_{1}$ for the availability of this resource, and by introducing two dummy jobs $\beta_{1}, \beta_{2}$ that consume the “non-available” $R_{1} - R_{2}$ units in the intervals $[0, t_{1}]$ and $[t_{2}, t_{2} + d]$ , where d (dynamically defined) is large enough to guarantee that the project is completed before $t_{2} + d$ . So job $\beta_{1}$ has processing time $t_{1}$ , requires $R_{1} - R_{2}$ units of the resource, and is fixed in the interval $[0, t_{1}]$ by the temporal constraint $S(\beta_{1}) = 0$ . Similarly, $\beta_{2}$ has processing time d, requires $R_{1} - R_{2}$ units of the resource, and is fixed in the time interval $[t_{2}, t_{2} + d]$ by the constraint $S(\beta_{2}) = t_{2}$ . Neither of these artificial jobs does enter the cost function K. (Note that temporal constraints of the above form, i.e. $S(\alpha) = t$ are covered by the above-mentioned inequality constraints between starting times of jobs by expressing $S(\alpha) = t$ as $S(\alpha_{0}) + t \leq S(\alpha)$ and $S(\alpha) - t \leq S(\alpha_{0})$ , where $\alpha_{0}$ is an artificial “start” job that precedes all other jobs.)

It is clear that these new constraints with constant resource availabilities yield a problem that is equivalent to the original problem.

A similar transformation reduces also non-constant resource demands of jobs to constant demands by splitting jobs and chaining them together by appropriate temporal constraints. For example, the demand of $\alpha_{i}$ in fig. 9 can be expressed via two jobs $\alpha_{i}^{(1)}$ and $\alpha_{i}^{(2)}$ with processing times $t_{1}$ and $x_{i}-t_{1}$ , constant resource demands $r_{1}$ and $r_{2}$ , and the additional temporal constraints $S(\alpha_{i}^{(1)})+t_{1}\leq S(\alpha_{i}^{(2)})$ and $S(\alpha_{i}^{(2)})-t_{1}\leq S(\alpha_{i}^{(1)})$ . These transformations are completely hidden from the user, and any output for the user is automatically retransformed into the original user model.

Note that a further restriction concerning resource constraints is the requirement that they are not of the re-usable type (such as money), that they are regarded as being given (i.e. are not part of the optimization aim; for alternative approaches cf. [40]) and that there are not available resource types with related machine types of different speed which are of importance in certain CIM and machine-scheduling applications. Again, some knowledge-based translation into our standard modelling frame is possible also in these cases, but with severe limitations concerning algorithmic efficiency.

Very liberal are again the requirements concerning preference structures and involved randomness. This aspect is regarded by the authors as particularly important for an adequate modelling of user problem instances.

Actually, we allow here any preference structure (utility function) that is a monotone real function of the jobs' completion time vector (regular cost function), i.e. we only assume that completing some jobs later without at least one job being completed earlier is not preferred by the user (generally a very reasonable assumption). We just mention that an enormous variety of user requests can (standardly) be translated into this form. Concerning probabilities, any joint distribution of job durations is allowed, possibly involving stochastic dependences. Note that stochastic dependences as well as stochastic aspects in general will have particular importance in early, coarse or incomplete model variants. They will also occur in form of automatic stochasticization during background sensitivity analysis or when analyzing robust stochastic bounds, see also the remarks above for Example A.

![](/api/attachments/Z5UD36PP/fulltext/images/39bfef51569033ff8a855752e308e90943642e8cf69ef69e57684ac6cc26a7b3.jpg)  
Fig. 9. Resource Demand Curve.

Note that some restrictions in general are due to missing control of durations, particularly concerning acceleration of work progress via specific cost and/or resource input. Again, translation of some aspects of such generalizations into our standard modelling framework is possible, however, with considerably reduced algorithmic efficiency [44].

A considerable difficulty in modelling and representation of application problems in artificial intelligence applications is usually given by the treatment of time. Note that in our approach these difficulties are avoided in an elegant way. Actually, we do the modelling within a “deep” mathematical framework that allows the assumption of continuous time. Within the mathematical models, theorems characterize optimal solutions and deliver appropriate algorithmic tools for their determination [3], [57]. These luckily allow the restriction of further considerations to very special (discrete) sets of schedules of “earliest start type”. They can be computed efficiently with time being handled – maybe even online – in a kind of interval representation.

Now, before going deeper into the task agenda of the scheduling world-model and related algorithmic tools, we would like to point again at the two knowledge-based interfaces of the core scheduling model of mathematical nature that were mentioned above several times.

The user front end is responsible for the translation of all kinds of user inputs into the mathematical core model. We mentioned already the standardization of non-constant resource constraints or requirements (cf. Example C) and add here the introduction of new activities and all associated data via direct (graphical) manipulation devices as indicated with fig. 8 and 9. A further extension would be the appropriate accommodation of natural-language inputs, e.g. modal operators such as “earlier”, “more resources”. Note that some of these translation tasks have already been designed. As it seems, the clear mathematical core framework facilitates such translation tasks. This seems to be valid particularly for some usually involved problems in the treatment of natural-language constructs. As really nice we also mentioned the advantage of a possible later work on the enrichment of such translation tools which becomes possible by the clear separation of these aspects from the mathematical core model on which the major functionalities of the system are based.

Concerning these functionalities, the other front end is directed towards the available (possibly distributed) hard- and software environment. Given the long-term orientation of our system development and the extreme speed in commercial hard- and software changes, a separation of the core model framework from the actual processing environment is necessary in order to achieve a good portability and adaptability with view to changing environments. I.e. on the core model level, we will have to deal with precise models of reality only and will only have to deduce precise tasks and usable tools to produce wanted advice. The degree to which certain tasks and tools are worked on – depending on the available hard- and software environments – is decided upon separately.

As already mentioned, this activity constitutes a design task with great opportunities in itself, particularly with view to machine learning and statistical adaption concerning tool use in particular problem instances. To accommodate the data requirements in this respect, the already discussed hierarchical, object-orientated encapsulation of algorithms, including needed preconditions, available estimation functions for promised performance, update (learning) functions and input-output behaviour is required [9].

Some implementation in this respect is already available, as is some work on general system components of this type for various applications, cf. [9].

With these comments on the general frame in mind, we now discuss in more detail the hard core of the organization of the scheduling world model, i.e. the determination of needed tasks and associated tools for (partial) scheduling models. The major device is given by an Agenda of Major Task Types, consisting of four types of tasks (see fig. 10). The different types of tasks are consecutively treated next in more detail. Note that the major algorithmic difficulties and thus the strongest emphasis on automatic learning and adaption is related to the last category, termed hard operators. Severe concentration on the employment of knowledge-based input explanation facilities is instead required for all mentioned tasks.

![](/api/attachments/Z5UD36PP/fulltext/images/f5dd4b729c5d8309fb869fede7daa36fa5ea58a9feae96880e43740cba09c936.jpg)  
Fig. 10. Classification of Tasks the System Knows to Handle.

## Representation of Data

Whatever data are available to the system, whether gained via user input or data base access or automatic data variation, it will be necessary to manipulate this data and to represent it in different forms. In the following, we are considering here only tasks that can efficiently be handled with nice performance guarantees.

Major alternatives concern the representation of project structures via relations, graphs, comparability graphs, lists of (immediate) predecessors or successors, distance matrices and so forth. Resource constraints may be given via lists or pictogrammes or sets (systems of forbidden sets); note, however, that in general, the later task will be algorithmically involved (nonpolynomial in general [2], [3]).

In Example A, the project structure could be internally represented by a directed (acyclic) graph in which the vertices represent jobs (plus an additional source $\alpha_{0}$ and sink $\alpha_{n+1}$ ) and the edges represent temporal constraints between starting times of the jobs (i.e. $\alpha_{i} < \alpha_{j}$ results in an edge between $\alpha_{i}$ and $\alpha_{j}$ representing the temporal constraint $S_{i} + x_{i} \leq S_{j}$ ). Due dates are represented by an edge from the source to the job in question (e.g. d = 60 for $\alpha_{14}$ is represented by an edge ( $\alpha_{14}, \alpha_{0}$ ) with the constraint $S_{14} - 60 \leq S_{0}$ ). The edge weights are either the constant $d_{ij}$ in the constraint $S_{i} + d_{ij} \leq S_{j}$ (i.e. $x_{i}$ and -60 in the example cases), or the distributions or intervals if no exact value can be specified. The graph structure is stored by means of an edge list for each vertex. This is e.g. transformed to a $(n + 2) \times (n + 2)$ distance matrix for checking consistency of the temporal constraints and the calculation of solution proposals for deterministic problem versions by branch and bound methods [3], [57].

The resource constraints could be represented internally be a system of $\subseteq$ -minimal forbidden sets (i.e. $\subseteq$ -minimal sets that can be performed simultaneously with respect to the technological precedence constraints, but not with respect to the resource constraints). So in Example A, these forbidden sets are $\{\alpha_{4}, \alpha_{13}\}$ and $\{\alpha_{9}, \alpha_{14}, \alpha_{15}\}$ . These sets model the essential conflicts, and there are available fast reduction methods to computationally reduce a given problem to an equivalent problem on the jobs in forbidden sets only [3], [57].

There is a great variety of options for representing utility functions or distributions, either in analytical or graphical form, using discrete representation or smoothed versions. Representation of results as e.g. schedules (Gantt diagrams) or distributions of project durations or statistical analysis of effects encountered and so forth require similar considerations. Concerning systems output, different output media may be taken into account for specific representation tasks. Of great practical importance are e.g. high-quality plotter outputs of project schedules.

Note that strong abilities in data representation is not just a question of satisfying user needs, though such abilities constitute a very important support for expert and non-expert users. Equally important is the fact that different algorithmic tools may need completely different representations of the respective problem instances. E.g. some algorithms may work on graphs, while others work on lists. In fact, special case algorithms require very special data structures. As an example we mention the requirement of the transitive closure of the given precedence constraints in [57] or the need for a consecutive-ones representation of an interval graph in [18]. We just mention that representation in this general sense may also necessitate the previous identification of a problem as belonging to a special problem type. When applying certain algorithmic tools, several interdependent data transformation processes may be involved. The corresponding requirements have appropriately to be taken into account, when estimating the computation time needed to use a specific instead of a general-purpose tool. Note that quite some work concerning the stated types of data format transformation has already been done for the available prototype of the scheduling system, particularly in form of students' practical exercises at the university of Passau.

## Modification of Data

Data modification is again an area where only efficient algorithmic tools will be employed and much work has already been done. This concerns particularly a powerful user interface that allows modification via direct (graphical) manipulation and menu and mask generation technique. Modification of data includes a number of major tasks, among them the iterative modelling of problem instances from scratch and the incremental model-building, using e.g. hierarchical forms of proceeding, with possible reference to available sub-projects and local modifications of data. We already mentioned that the automatic keeping track of such incremental model-building processes by the system can be helpful in later evaluations. Another area of modification of data involves the complicated process of modelling the preference structure and the probability assumptions of the user. There, different modelling approaches are possible and debiasing plays a major role.

All mentioned processes will come up again if models are adapted due to additional (implicit) user input, e.g. via rejection of proposed solutions. Other modifications concern automatic model variations in all kinds of background sensitivity analysis. Finally, the user will induce modifications via the high-level commands discussed above, i.e. commands like “stochastify”, “generalize” and so forth. Note that as with the representation of data, identified tasks can usually be accommodated with one or more efficient algorithmic tools. Thus there is no particular need for a more thorough treatment of these aspects at the present stage.

While the two previous task groups of representation and modification of data primarily concerned the process of model-building, the other two task groups deal with the process of producing answers to more or less involved questions within a given model.

## Fast Operators

A great variety of such questions can again generally be answered by efficient algorithmic tools. These include combinations of e.g. the following tasks via logical or set-theoretical operators, viz. checking consistency with view to time constraints only, computing the earliest start or other special schedules for consistent models (without further resource constraints), determining the resource requirements of (sub-)projects over time with view to a given schedule and given resource types, determining the probability distribution (e.g. via simulation) or robust stochastic bounds for consistent models (without further resource constraints), testing membership in special problem sub-classes, determining all decomposition possibilities of a given project structure [6], [52] and so forth.

In summarizing, there is rich variety of efficiently manageable tasks which, when combined with representation and updating tasks in a suitable way, allow solid and reliable support for a user in a large number of aspects.

## Hard Operators

We finally come to the hard tasks in user support which concern important basic problem types in scheduling problems. A thorough study of the authors seems to indicate that essentially - apart from finding examples having certain properties, a typical, well-studied and hard problem in a great number of AI applications - all kinds of related user requests may ultimately be translated (automatically) into logical or set-theoretical combinations of the following two dual types of questions in the deterministic case, viz.:

\- is there a schedule for a particular problem instance with given resource constraints whose preference value is bounded by some constant $t$ ?;

\- is there a schedule for a particular problem instance with given preference constraints whose resource requirements for resource type $i$ are bounded by some contant $c$ ?

For the stochastic case the same kind of questions concern the expected values or certain parameters of associated distribution functions. Note that the first formulation covers deterministic or stochastic optimization of time and cost requirements in resource-constrained scheduling, while the second deals with deterministic or stochastic optimization of resource requirements given time or cost constraints. Note that the problems in their general form are algorithmically quite involved. They are NP-complete and in general do not even allow fast or nice approximation. Even the test for consistency is already NP-complete in general formulations with resource constraints. Practical experiences indicate that advanced support is particularly needed for these involved questions. The potential for improving solutions, either with view to scheduling by experienced practitioners or with regard to state-of-the-art expert systems is substantial. Therefore, we have argued to concentrate on this type of questions via employing all available scientific insight concerning the use of maybe very involved tools.

![](/api/attachments/Z5UD36PP/fulltext/images/ab6eb8c7bce5882696abc10b377788897155e08d254992c3ecff475d9a6f5ed9.jpg)  
Fig. 11. Hierarchy of Methods.

## Extension to Families of Scheduling Systems

We conclude the paper with some indications to that point which also allows the use of all the genetic and statistical adaption methods that were discussed above (cf. [24]).

The blackboard for the considered problems may distinguish on the top level between allocation of processor time to e.g. exact evaluation methods, computation of nested upper and lower bounds, approximations, and exploiting special cases. On a sub-level, Exact Methods include a number of branch-and-bound techniques, enumeration schemes and formulations as LP or dynamic optimization problems. On an even lower level, a particular branch-and-bound procedure allows a great variety of using “artificial” bounds or of changing the sequence in tree inspections or treating branches separately with some of the other methods proposed (see fig. 11).

Upper and Lower Bounds can be obtained by a great diversity of approaches, reaching from variations or relaxations of time, sequencing and resource constraints to (monotone) changes in duration and preference structures. The potential for a fast computation of bounds is particularly great, if the modified problems are nice to handle. Finding this out or achieving this deliberately falls into the group of approaches that is discussed below. We just mention that computing upper and lower bounds is particularly attractive, as in case of small differences between those bounds, the achievement of a good solution is guaranteed and further computation can be stopped in case of a sufficiently good approximation.

Among the available Approximation Techniques we mention here particularly changes in scaling (e.g. rounding) which can be useful e.g. in enumeration or LP-based approaches. Another form of approximation may concern the replacement of discrete resource constraints by continuous ones, possibly allowing the use of methods from control theory. Finally, we mention in this context the existence of (full) approximation schemes for a number of quite special types of NP-complete scheduling problems [13], [36].

A very important last agenda element is the Exploitation of Special Problem Instances. Special problem classes in scheduling may possess a much better algorithmic behaviour than scheduling problems in general. This may mean a better approximation behaviour in sub-classes that are still NP-complete or the existence of fast algorithms in even nicer cases. Note that such fast algorithms may be very involved from a methodological point of view and might require special data structures as input, as already mentioned above. As already discussed in section 2, insight into special types of scheduling problems is abundant, adding up to about 10000 distinguished sub-cases [36]. In effect, the borderline between nice and hard sub-cases is marked in a more precise way in scheduling as compared with any other class of combinatorial optimization problems (with routing perhaps constituting the only comparable area).

Sub-aspects in this special case agenda are derived from special properties concerning e.g. the occurring project structure (series-parallel, N-free, decomposable with bounded width etc. [42], cf. fig. 12) and/or durations (e.g. constant or different) and/or resource constraints (e.g. 1-machine,

![](/api/attachments/Z5UD36PP/fulltext/images/16454a3bdab7454600b8ea40813374df6f70c95fca2da2660f8794e847047169.jpg)  
Fig. 12. A Classification of Precedence Constraints.

2-machine or m-machine problems with m fixed) and/or the cost functions (project duration, weighted sum of completion times).

We have already mentioned that fast identification algorithms for such special cases do exist. The computational requirements needed for identification purposes have of course appropriately to be taken into account when deciding upon where to invest scarce computation time. Note that a decision concerning the proper use of the scientific insight into the treatment of special cases, developed by a great world-wide community of cooperating researchers, is really hard, also for humans. This is true already for the mastering of details, not to speak of any insight on what tool to use reasonably in a particular situation.

Consequently, this is an area of knowledge-processing where automatic classification and tool use, and in addition machine-learning and statistical adaption in this respect are in order. In fact, we regard such an integrated form of tool use as the adequate modern way of knowledge transfer from research to application. Without systems as designed and intended here, we are short to the point where further scientific results into even more specific problem instances would almost have no chance of ever being used reasonably in applications.

## 5. Concluding Remarks

We have argued in this paper for a normatively-based type of future decision support systems which exploit competence from the sophisticated use of models and associated algorithmic tools. The application domain is scheduling with emphasis on problems in civil engineering, for which a broad scientific insight into the algorithmic handling of such problems is available.

In fact, systems as proposed here constitute the adequate form of transferring such scientific contributions into application domains and even to learn (automatically) which tools to use reasonably in special problem instances.

The scheduling system discussed here is a prototype demonstration system for an involved research agenda in advanced decision support that also constitutes the general theme of a special volume of Decision Support Systems [31]. It is developed conceptually in a top-down way as presented in this paper, and is partially realized in a bottom-up way, building on many years of previous work with regular needs for re-design and re-programming on different levels of conceptual insight and used programming environment as well.

Certainly it is not clear whether the intended type of advanced support can really be achieved with today's or tomorrow's hard- and software tools and with the – naturally restricted – methodological framework and insight of the authors and their cooperating colleagues and coworkers. The future will tell us more about that.

In any case, though, the incorporation of this scheduling project as a basic research project at the FAW in Ulm with its specific potential constitutes a promising framework for future work in this direction.

## Acknowledgement

We would like to thank H. Grünberger (Ulm), F. Gander (Berlin) and E. Schneider (Berlin) for their considerable technical support in arranging this paper. Also, we thank M. Jarke (Passau) for his valuable comments on an earlier draft of the text.

## References

[1] J.M. Anthonisse, K.M. van Hee, J.K. Lenstra (1988), Resource constrained project scheduling: an international exercise in DSS development, Decision Support Systems 4 p. 249–257.

[2] M. Bartusch (1983), An algorithm for generating all maximal independent subsets of a poset, Computing 26, p. 343–354.

[3] M. Bartusch, R.H. Möhring, F.J. Radermacher (1988), Scheduling project networks with resource constraints and time windows, Ann. Oper. Res. 16, p. 201–240.

[4] N. Billstein, F.J. Radermacher (1977), Time-cost optimization, Methods of Oper. Res. 27, p. 274–294.

[5] L. Bodin, B. Golden, A. Assad, M. Ball (1983), Routing and scheduling of vehicles and crews – The state of art, Comput. and Oper. Res. 10, p. 63–211.

[6] H. Buer, R.H. Möhring (1983), A fast algorithm for the decomposition of graphs and posets, Math. Oper. Res. 8, p. 170–184.

[7] G. DeSanctis (1984), Computer graphics as decision aids: Directions to research, Decision Sciences 15, p. 463–487.

[8] B. Dodin (1985), Bounding the project completion time distribution in PERT networks, Oper. Res. 33, p. 862–881.

[9] R. Felter (1988), Conceptual Outline of a Decision Support Assistant (DSA), Proc. 12th SOR – Passau 1987, Athenäum, München.

[10] B. Fischhoff, P. Slovic, S. Lichtenstein (1980), Knowing What You Want, Measuring Labile Values, T. Wallstein (ed.) Cognitive Processes in Choice and Decision Behaviour, Erlbaum, Hillsdales, N.J.

[11] P.C. Fishburn (1970), Utility Theory for Decision Making, Wiley, New York.

[12] L.J. Fogel, A.J. Owens, M.J. Walsh (1966), Artificial Intelligence through simulated evolution, John Wiley, New York.

[13] H.R. Garey, D.S. Johnson (1979), Computers and Intractability, A Guide to the Theory of NP-completeness, Freeman, San Francisco.

[14] A. Geoffrion (1988), Structured Modelling, UCLA Graduate School of Management, Los Angeles.

[15] F. Glover (1988), Tabu Search, CAAI Report 88-3, Center for Applied Artificial Intelligence, Univ. of Colorado, Boulder.

[16] I.P. Goldstein, R.B. Roberts (1977), NUDGE – a knowledge based scheduling program, Proceedings of the 5th. International Joint Conference on Artificial Intelligence, MIT.

[17] J.J. Grefenstette (ed.) (1985), Proc. Intern. Conf. on Genetic Algorithms and their Application, The Robotics Institute, Carnegie-Mellon University.

[18] U.I. Gupta, D.T. Lee, J.Y. Leung (1982), Efficient algorithms for interval graphs and circular arc graphs, Networks 12, p. 459–467.

[19] F. Hayes-Roth, D.A. Waterman, D.B. Lenat (1983), Building expert systems, Addison-Wesley, Reading.

[20] P. Hersey, H. Kunreuther, P.J. Schoemaker (1982), Bias in Assessment Procedures for Utility Functions, Management Science 28, p. 936–954.

[21] R.M. Hogarth (ed.) (1982), Question Framing and Response Choice, Jossey-Bass Inc., San Francisco.

[22] P.C. Humphreys (1986), A brief description of MAUD, Technical Report, Decision analysis unit, London School of economics and political sciences.

[23] E. Jaquet-Lagreze, J. Siskas (1982), Assessing a Set of Additive Utility Functions for Multicriteria Decision Making, The UTA Method, Europ. Journal of Oper. Res. 10, p. 151–164.

[24] M. Jarke, F.J. Radermacher (1988), The AI Potential of Model Management and Its Central Role in Decision Support, Decision Support Systems Vol. 4, No. 4.

[25] R.G. Jereslov (ed.) (1988), Approaches to intelligent Decision Support, Annals of Operation Research 12.

[26] C.V. Jones (1988), The 3-dimensional Gantt chart., Oper. Res. 36, p. 891–903.

[27] R. Kaerkes (1977), Netzplan Theory, Methods of Oper. Res. 27, p. 1–65.

[28] D. Kahnemann, P. Slovic, A. Tversky (eds.) (1982), Judgement Under Uncertainty, Heuristics and Biases, Cambridge Univ. Press.

[29] R.L. Keeney, H. Raiffa (1976), Decisions with Multiple Objectives, John Wiley, New York.

[30] R.L. Keeney, R.H. Möhring, H. Otway, F.J. Radermacher, M.M. Richter (eds.) (1988), Multi-Attribute Decision-Making via O.R.-Based Expert Systems, Annals of Operations Research 16.

[31] R.L. Keeney, R.H. Möhring, H. Otway, F.J. Radermacher, M.M. Richter (eds.) (1988), Design Aspects of Advanced Decision Support Systems, Special Issue of Decision Support Systems, Vol. 4, No. 4.

[32] M. Kendall, A. Stuart, J.K. Ord (1987), Kendall's advanced theory of statistics, Vol. 1, fifth edition, Charles Griffin, London.

[33] S. Kirkpatrick, C.D. Gelatt, M.P. Vecchi (1983), Optimization by simulated annealing, Science 220, p. 671–680.

[34] W.K. Klein Haneveld (1986), Robustness against dependence in PERT: An application of duality and distributions with known marginals, Math. Progr. Study 27, p. 153–182.

[35] E.L. Lawler (1976), Combinatorial Optimization: Networks and Matroids, Holt, Rinehart and Winston, New York.

[36] E.L. Lawler, J.K. Lenstra, A.H.G. Rinnooy Kan (1982), Recent developments in deterministic sequencing and

scheduling: A survey, M.A.H. Dempster et al. (eds.) Deterministic and Stochastic Scheduling, Reidel, Dordrecht, p. 35–73.

[37] D.B. Lenat (1977), On Automated Scientific Theory Foundation, A Case Study Using the AM Program, J.E. Hayes, D. Mitchie, L.I. Mikulich (eds.) Machine and Intelligence 9, Halsted Press, New York.

[38] I. Meilijson, A. Nadas (1979), Convex majorization with an application to the length of critical paths, J. Appl. 16, p. 671–677.

[39] J.J. Moder, C.R. Phillips (1964), Project management with CPM and PERT, Reinhold, New York.

[40] R.H. Möhring (1984), Minimizing costs of resource requirements in project networks subject to a fixed completion time, Oper. Res. 32, p. 89–120.

[41] R.H. Möhring (1985), Algorithmic aspects of compatibility graphs and interval graphs, Graphs and Order, I. Rival (ed.), Reidel, Dordrecht, p. 41–101.

[42] R.H. Möhring (1989), Computationally tractable classes of ordered sets, Algorithms and Order, ed. I. Rival, Kluwer Acad. Publ. Dordrecht, p. 105–193.

[43] R.H. Möhring, F.J. Radermacher (1984), Substitution decomposition of discrete structures and connections with combinatorial optimization, Ann. Discrete Math. 19, p. 257–356.

[44] R.H. Möhring, F.J. Radermacher (1984), Scheduling problems with resource-duration interaction, Methods of Oper. Res. 48, p. 423–452.

[45] R.H. Möhring, F.J. Radermacher (1985), An introduction to stochastic scheduling problems, Lecture Notes in Economics and Mathematical Systems 240, p. 72–130.

[46] R.H. Möhring, F.J. Radermacher (1985), Generalized results on the polynomiality of certain weighted sum scheduling problems, Methods of Oper. Res. 49, p. 405–417.

[47] R.H. Möhring, F.J. Radermacher (1989), The order-theoretic approach to scheduling: the deterministic case, in R. Slowinski, J. Weglarz (eds.) Advances in Project Scheduling, Elseviers Science Publ., Amsterdam.

[48] R.H. Möhring, F.J. Radermacher (1989), The order-theoretic approach to scheduling: the stochastic case, in R. Slowinski and J. Weglarz (eds.) Advances in Project Scheduling, Elseviers Science, Publ., in Amsterdam.

[49] R.H. Möhring, F.J. Radermacher, G. Weiss (1984), Stochastic Scheduling problems I: general strategies, Zeitschrift für Oper. Res. (ZOR) 28, p. 193–360.

[50] R.H. Möhring, F.J. Radermacher, G. Weiss (1985), Stochastic Scheduling problems II: set strategies, Zeitschrift für Oper. Res. (ZOR) 29, p. 65–104.

[51] S. Moskowitz, M.L. Sarin (1983), Improving the Consistency of Conditional Probability Assessments for Forecasting and Decision Making, Management Science 29, p. 735–749.

[52] J.H. Muller, J. Spinrad (1989), Incremental modular decomposition, J. of Assoc. Comput. Mach. 36, p. 1–19.

[53] K. Neumann (1975), Operation Research Verfahren, Band III, Carl Hanser Verlag, München.

[54] J. Nievergelt (1983), Die Gestaltung der Mensch-Maschine-Schnittstelle, J.W. Schmidt (ed.): Sprachen für Datenbanken, Springer-Verlag, Heidelberg.

[55] N.J. Nilsson (1982), Principles of Artificial Intelligence, Springer Verlag.

[56] F.J. Radermacher (1977), Floats in project networks, Methods of Oper. Res. 27, p. 163–224.

[57] F.J. Radermacher (1986), Scheduling of project networks, Annals of Oper. Res. 4, p. 227–252.

[58] F.J. Radermacher (1988), Entwicklungsperspektiven rechnergestützter Entscheidungsfindung, J. Wolff (ed.): Proceedings des IBM Symposiums “Entscheidungsunterstützende Systeme”, p. 289–320, Oldenbourg, München.

[59] I. Rechenberg (1973), Evolutionsstrategie, frommannholzboog, Stuttgart.

[60] M.M. Richter (1989), Prinzipien der Künstlichen Intelligenz, Teubner, Stuttgart.

[61] A.H.G. Rinnooy Kan (1976), Machine Scheduling Problems: Classification, Complexity and Computation, Nijhoff, The Hague.

[62] K.P. Schuett (1981), Wahrscheinlichkeitsabschaetzungen im Computer-Dialog, Poeschel-Verlag, Stuttgart.

[63] H.P. Schwefel (1987), Numerische Optimierung von Computermodellen mittels der Evolutionsstrategie, Birkhäuser, Basel/Stuttgart.

[64] B. Shneiderman (1982), The future of interactive systems and the emergence of direct manipulation, Y. Vassiliou (ed.): Human factors and interactive computer systems, P.C. Ablex, Norwood, N.J.

[65] A.W. Shogan (1977), Bounding distributions for a stochastic PERT network, Networks 7, p. 359–381.

[66] H.G. Spelde (1976), Stochastische Netzpläne und ihre Anwendung im Baubetrieb, Dissertation, RWTH Aachen.

[67] R.H. Sprague, E.D. Carlson (1982), Building effective decision support systems, Prentice Hall, Eaglewood Cliffs, N.J.

[68] D. Stoyan (1983), Comparison Methods for Queues and Other Stochastic Models, J. Wiley & Sons, Chichester.

[69] R.S. Sullivan, J.C. Hayya (1980), A comparison of the method of bounding distributions (MBD) and Monte Carlo simulation for analyzing stochastic acyclic networks, Oper. Res. 28, p. 614–617.

[70] A. Tate (1977), Generating project networks, Proceedings of the 5th. International Joint Conference on Artificial Intelligence, MIT.

[71] D.A. Waterman (1986), A Guide to Expert Systems, Addison-Wesley.

[72] G. Weiss (1986), Stochastic bounds on the distributions of the optimal value functions with applications to PERT, network flows and reliability, Oper. Res. 34, p. 595–605.
