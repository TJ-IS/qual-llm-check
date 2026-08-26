---
otero_id: 17103
otero_key: "QSY3KB4Q"
title: "An architecture for integrating expert systems"
authors: "Niall M Fraser; Keith W Hipel; D.Marc Kilgour; Michael D McNeese; Daniel E Snyder"
year: "1989"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(89)90034-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Architecture for Integrating Expert Systems $^{1}$

Niall M. FRASER
Department of Management Sciences, University of Waterloo,
Waterloo, Ont., Canada

Keith W. HIPEL
Department of Systems Design Engineering, University of Waterloo, Waterloo, Ont., Canada

D. Marc KILGOUR
Department of Mathematics, Wilfrid Laurier University,
Waterloo, Ont., Canada

Michael D. McNEESE

Harry G. Armstrong Aerospace Medical Research Laboratory, Wright-Patterson Air Force Base OH, USA

Daniel E. SNYDER

Harry G. Armstrong Aerospace Medical Research Laboratory, Wright-Patterson Air Force Base OH, USA

A conflict resolver is developed for mediating disputes arising among competing expert systems (ESs). The conflict resolver constitutes the key component of an overall decision support system designed for controlling a complex system or supporting the decision making of a human operator within the system. When competing ESs make conflicting recommendations for controlling the system, the conflict resolver uses a Delphi-like mediation to achieve a compromise solution. The mathematical framework for the comprehensive conflict resolution system is defined formally, and it is proven that the conflict resolver always reaches a consistent recommendation.

Keywords: Competing Expert Systems, Conflict Resolver, Delphi-like Mediation.

## 1. Introduction

The general field of artificial intelligence (AI) has recently seen an explosion in the development

![](/api/attachments/QSY3KB4Q/fulltext/images/77ed4ee6f244dc2e5cc54e843df2f93fa25ff9e4c1ccf0e861d0641f6cb6f2c5.jpg)

Niall M. Fraser is Assistant Professor in the Department of Management Sciences at the University of Waterloo, Canada. He holds a Doctorate in Systems Engineering from the University of Waterloo, and is a registered Professional Engineer in the province of Ontario. Prior to his current academic posting, he was an independent consultant in industrial systems engineering. His primary research interests concern the use of non-cooperative game theory for the analysis of real world problems involving strategic conflict. He is the co-author, with Keith Hipel, of the textbook Conflict Analysis: Models and Resolutions, and has published in a variety of journals. Other research includes the study of $2 \times 2$ games, bargaining and negotiation theory, and mathematical models of compliance verification.

![](/api/attachments/QSY3KB4Q/fulltext/images/148aa001c03496aefbe4c764c315ffa588493dd6ed4c5641981f2656c08bd24e.jpg)

Keith W. Hipel is a Professor and Associate Chairman for Graduate Studies within the Department of Systems Design Engineering, and is cross-appointed to the Department of Statistics and Acturial Science at the University of Waterloo. In 1984, the American Water Resources Association presented Dr. Hipel the "W.R. Boggess Award" for the most outstanding paper published during 1983 in Water Resources Bulletin. To allow him to execute research at Kyoto and

Tottori Universities during 1984, Dr. Hipel was awarded a "Japan Society for Promotion of Science (JSPS) Fellowship". His main research interests are conflict analysis and time series analysis. Dr. Hipel is an Associate Editor with IEEE Transaction on Systems, Man and Cybernetics, Water Resources Bulletin, Information and Decision Technologies, and Hydroelectric Energy.

![](/api/attachments/QSY3KB4Q/fulltext/images/1c8c6f53af82e454af23efb5b9f80c9af199f7072f2f9c2152ad35efe2d6044d.jpg)

D. Marc Kilgour is Professor of Mathematics at Wilfrid Laurier University in Waterloo, Canada, as well as Adjunct Professor of Systems Design Engineering at the nearby University of Waterloo. His research and consulting interests are in mathematical modeling, principally conflict modeling and game theory. With Steven J. Brams, he published Game Theory and National Security [Basil Blackwell (1988)]. He won the Public Choice Society's 1984 Duncan Black Award for an article written with Terrence J. Levesque. He has recently published papers in mathematics, political science, systems engineering, operations research, philosophy, and biology journals.

of expert systems (ESs). Because of the great variety of complex problems amenable to solution by ESs, the widespread development and use of ESs is imminent. In many situations, an ES will provide direct aid to a decision maker, but in more complex cases, several ESs covering different but related knowledge will be needed. For example, a manufacturer of the future may have separate ESs advising him on production, marketing and financing. Because the knowledge sources have overlapping domains, conflict among these ESs is inevitable. This problem will arise in any complex system that can benefit from multiple ESs. In particular, the current planning of future military aircraft incorporates multiple ESs into an overall decision aid known as the Pilot's Associate. Other examples include future decision support systems for government policy makers, astronauts, lawyers, and medical professionals.

The ESs within a particular system may put forward inconsistent (conflicting) recommendations that must be properly integrated, under operating conditions, into a consistent overall recommendation. The major objective of this paper is to present a procedure for mediating among ESs so that conflicts can be effectively and efficiently

![](/api/attachments/QSY3KB4Q/fulltext/images/75d895263bba53fca924a0566cce97038c52d50ae169a2ab22f3dfbed2fe9302.jpg)

ory, modelling approaches to artificial intelligence, and group decision making. Under Air Force sponsorship, Mr. McNeese is currently pursuing a Ph.D. in Cognitive Science at Vanderbilt University.

Michael D. McNeese received a A.A.S. degree in Engineering design from Sinclair College, a B.A. degree in Psychology, and a M.A. degree in Experimental-Cognitive Psychology from the University of Dayton. Mr. McNeese is an Engineering Research Psychologist in the Harry G. Armstrong Medical Research Laboratory, Human Engineering Division, Wright-Patterson Air Force Base, Ohio. His research activities involve aspects of human-computer interaction, cognitive the-

![](/api/attachments/QSY3KB4Q/fulltext/images/30b81230039f71dd48cf8a94c912091b5af321358a683de87dc75b377870262d.jpg)

gram initiatives, including the design of interactive, real-time simulators and the development of knowledge-based decision support concepts for improving aircraft survivability. Mr. Snyder is currently employed as a Senior Engineer with Electronic Warface Associates, Inc., Dayton, Ohio.

resolved. The specific mechanism for organizing and mediating conflict among ESs, as well as other knowledge sources, is the Conflict Resolver (CR). The CR, along with the ESs and other knowledge sources, forms a comprehensive decision support system for optimally operating the system.

In the next section, the literature related to the aforementioned objectives is reviewed briefly. Then the theoretical framework for the conflict resolver is developed and illustrated, and it is proven mathematically that an overall resolution is always reached by the proposed approach. Finally, a summary and some ideas for the future are presented.

## 2. Review

The main purposes of this review are to put into perspective the general problem of conflicts among ESs and to point out some basic ideas that are used later to solve this problem. A brief literature review encompassing AI, ESs, decision support systems (DSSs), cognitive psychology, and game theory is followed by a discussion of the Delphi method, which serves as the model and inspiration for the CR developed later.

AI can be usefully defined as the branch of computer science which aims ‘to design intelligent computer systems, that is, systems that exhibit the characteristics we associate with intelligence in human behavior’ [3]. The problem considered here originates in the real-time use of AI to operate complex systems, or to advise and assist the human operator of such a system. The key contribution of AI to this task would be the development and coordination of appropriate ESs.

In Negoita's [17] definition, an ES is a software system that mimics the deductive or inductive reasoning of a human expert. The organization, function, and construction of ESs have been described in detail elsewhere (for example, [12]). However, one recent development connected with ESs is of considerable importance to the design of a CR. Hayes-Roth [11] has described blackboard architecture, which is a scheme for communication among ESs and other knowledge sources, including possibly humans. In simple terms, the blackboard contains shared data, and each knowledge source can write its current state on the blackboard; as well, it can read the current states of other knowledge sources. Subsequently, it will be seen that an expansion of the blackboard concept will ease considerably the implementation of the CR developed below.

As noted by Chandrasekaran [5], distributed problem solving, or, more generally, distributed AI, is another important branch of AI. Davis and Smith [7] define distributed problem solving as the cooperative solution of problems by a decentralized and loosely coupled collection of problem solvers. In contrast to distributed problem solving, the CR developed in this paper provides a centralized mechanism for co-operatively resolving disputes among competing ESs. Nonetheless, a CR could be designed for use as an internal component of a given ES in order for that ES to decide upon its own recommendation when confronted with conflicting information.

A DSS is a software system designed to assist a human decision-maker [10]. DSSs often integrate knowledge and methods from widely separated disciplines for the purpose of supporting decisions. It is therefore inevitable that conflicts arise among the distinct elements of a DSS designed to assist in the operation and control of a complex system. This problem was faced in a specific context by Dutta and Jain [8]. The conflict problem analyzed here thus arises as many disparate ESs and other knowledge sources are coordinated and interrelated within a single DSS.

One discipline which might be expected to provide clues to the successful design and operation of a CR is game theory, the analysis of conflict and cooperation among rational decision makers. Since its origin [21], game theory has evolved into widely applicable tools for conflict analysis (see [9] and [14] for recent references). However, methods based on game theory are not well suited to the problem of resolving conflict among ESs within a DSS for the simple reason that these methods presuppose the participants in the conflict to be independent, selfinterested decision making units.

Another discipline which might have assisted in the conflict resolver problem is Cognitive Psychology, the study of intelligence from a psychological perspective. This field was recently reviewed by Anderson [1] and Smith [20]. Unfortunately, however, present knowledge of the mental processes involved in arbitrating conflicts among different functional areas of the brain appears to be too primitive to incorporate into the design of a CR.

The idea which did provide the basic model for the CR is the Delphi method. The Delphi method is an iterative procedure which anonymously uses the opinions of experts to arrive at a resolution to a problem (see, for example, [18, pp. 200–201]). At the first step, each expert is asked to respond to a written questionnaire which might appear on paper or on a monitor. In each round after the first, each expert is provided with the responses of all of the others. However, in order to avoid the psychological drawbacks associated with face-to-face confrontations, the identities of the authors of the various opinions are not revealed. Furthermore, in later rounds, an expert may be asked to explain previously expressed opinions and to consider other possible approaches to the problem. As each expert revises his position over a series of rounds in which the opinions of the other experts evolve, the anonymous debate tends toward a consensus of opinion, or at least a narrowing of the range of viewpoints.

The Delphi technique was originally developed at the Rand Corporation [6] and has been widely applied in many different fields [15]. Most textbooks in operations research and decision analysis contain at least some discussion of the Delphi method and its applications. Below an “automated” Delphi method is designed, permitting a CR to arrive at a consensus of opinion among competing ESs. It is proven mathematically that a consistent recommendation is always attained using this automated Delphi method.

Recently, the great potential for the application of AI within the field of military science has been widely recognized. For example, Anderson et al. [2] explain how several mutually cooperating ESs can assist combat pilots. McNeese [16] describes a human systems engineering approach for combining AI with human capabilities and limitations in order to create an intelligent cockpit that can operate an aircraft optimally. Hoyland et al. [13] use sophisticated systems simulation programs in a study of how to incorporate human operator considerations into the analysis of weapons delivery systems. Based on discussions at a workshop sponsored by the Army Research Institute, Sage and Rouse [19] report on how human decision making can be enhanced by the knowledge-based sciences. One particularly challenging problem is to employ ESs to assist a pilot operating a combat aircraft. A system consisting of interacting ESs, and a CR for integrating the recommendations of the ESs and other knowledge sources, is referred to as a Pilot's Associate.

As Buchanan [4] has suggested, the future of ESs will be severely restrained by conflicts in plans, strategies, and methods as well as inconsistencies in multiple sources of knowledge. Consequently, in order that a system such as the Pilot's Associate become operational, a crucial development is the theoretical design of the CR it will incorporate.

For any CR implementation, the specific characteristics of the application will constrain the structure of the solution. For example, the Pilot's Associate requires very rapid decisionmaking whereas a manufacturing application is not particularly constrained by time. Similarly, a particular set of ESs may be able to exchange information directly in a manner peculiar to the application. The CR architecture defined below is designed to be totally independent of the particular application, and can extract a consistent recommendation from any combination of multiple ESs.

## 3. A Decision Support System for Conflict Resolution

## 3.1. Overview

Fig. 1 illustrates an overall structuring of the conflict resolver problem. The two basic components are the Decision Maker (DM) and the DSS. The key element of the DSS is the CR.

The DM takes action in response to external directives and perceptions, and also interacts with the DSS. For example, in a manufacturing situation, the DM is the company president or manager, and DSSs are available to him through his computer terminal. External directives would include instructions from his board of directors, and perceptions could be obtained from sources such as external media and internal reports. In a combat aircraft of the future, the DM is the pilot, and the DSS is the Pilot's Associate. External directives would include instructions from ground control, and perceptions would incorporate both the readings of instruments and visual observations.

The DSS consists of m ESs and the CR. The DSS senses the environment through the functions of the ESs. Its uses the CR to resolve contradictory recommendations among the ESs and reports the overall recommendation to the DM. Autonomic actions as required can also be performed by the DSS, either via the CR or directly by an ES.

The DM requires a single consistent set of recommended actions at any one time. The function of the DSS is to develop this comprehensive recommendation by interacting with the ESs, and taking into account directives from the DM and from external sources.

There are several information types that appear in this structure:

(1) Directive - an instruction for action. This can come to the CR from the environment (e.g., board of directors) or from the DM.

(2) Informative – information concerning the environment. These are data that the ESs or other knowledge sources collect, or perceptions of the DM.

(3) Supportive - a recommendation from an ES to the CR, or from the CR to the DM. It differs from a directive in that it can be used or not used as the receiver wishes. It is also supported by a query facility to permit adjustment or clarification.

The implementation of the query system between the ESs and the CR presented in this paper makes use of a 'blackboard' through which the systems communicate. The blackboard is not a part of the general system problem, but rather a particular method of implementation that allows information to be shared. Consequently the blackboard does not appear in Fig. 1.

The general procedure used by the CR is based on the Delphi method of consensus development, as described above. In the DSS, each ES can revise its optimal recommendation (OR) based on the recommendations of the other ESs.

In the first step, each ES makes an OR on the basis of the data it has available. This OR is posted on the blackboard, and is available to the other ESs. Subsequently, each ES has the OR of every other ES in addition to the original external data. This new information may change the OR for one or more ESs. This procedure is described below in more detail.

![](/api/attachments/QSY3KB4Q/fulltext/images/1c74e3722edfee787c4b9818cb4bd043256f6762424b29ab79bf2866e7c804ab.jpg)  
Fig. 1. Problem Structure.

It is assumed that real world activities are slower than the decision making process of the DSS. Thus, the DSS can complete its analysis before changes in external data require the recommendation to be revised. This assumption is reasonable for the manufacturing example. In the case of the Pilot's Associate, split second decisions are required and consequently fast algorithms and computers will be needed.

When each ES evaluates its possible recommendations according to a cardinal utility scale, it is possible to use mathematical principles to establish eventual convergence to a consistent overall recommendation. This permits the very rapid calculation of the final recommendation without necessitating the iterative reevaluation of all of the available information by each ES. This numerical approach was developed and experimentally implemented as described below.

## 3.2. Assumptions and Definitions

The CR must integrate the recommendations of the ESs on all decisions. Each individual decision is represented as an action, or binary action variable: the actions are denoted $a_{1}a_{2},\ldots,a_{n}$ , where

$$
a _ {j} = \left\{ \begin{array}{l l} 1 & \text { if   action } j \text { is   selected } \\ 0 & \text { if   action } j \text { is   not   selected. } \end{array} \right.
$$

Note that the total number of available actions, n, is assumed to be finite. This means that all decisions must be represented in discrete form in the DSS.

The set of all conceivable decisions (which may include many that are infeasible) is then $2^{N}$ , where

$2^{N} =$ set of all sequences of $n0^{\prime}s$ and $1^{\prime}s$

$= \text{set of all subsets of } N = \{1,2,\ldots,n\}$

= Boolean (or power) set of N.

Of course, some decisions in $2^{N}$ may not be feasible. Denote the set of all feasible decisions by $A \subseteq 2^{N}$ . Note that, if $S \in A$ , then $S$ is a sequence of $n$ 0's and 1's, or, equivalently, $S \subseteq N$ .

Now, assume that there are m ESs (or other knowledge sources) labelled ES1,ES2,...,ESm. Each ES corresponds to a specific subset of the action variables on which it can make a recommendation. For $i=1,2,\ldots,m$ , the decision domain of ESi is $N_{i}\subseteq N$ ; this means that ESi is permitted to make a recommendation on the action variables $\{a_{j}: j\in N_{i}\}$ . Note that $N_{i}\neq\emptyset$ is assumed.

A feasible recommendation for $ESi$ is a subset $S_i \subseteq N_i$ such that, for some $S \in A$ , $S_i = S \cap N_i$ . Equivalently, a feasible recommendation for $ESi$ can be represented as a sequence of $\#(N_i)$ 0's and 1's. The set of all feasible recommendations for $ESi$ is then

$$
A _ {i} = \left\{S \cap N _ {i}: S \in A \right\}.
$$

Note that $A_{i} \subseteq 2^{N_{i}}$ .

Expert System i is assumed to have a valuation (or utility function)

$$
v _ {i} \colon A _ {i} \to R.
$$

The value of $v_{i}$ depends explicitly on the values of the action variables in $N_{i}$ , but $v_{i}$ may also depend implicitly on the values of action variables outside $N_{i}$ , as well as on external data. If $S_{i} \in A_{i}$ , the value of $v_{i}(S_{i})$ measures the extent to which the recommendation $S_{i}$ meets the objectives of ESi, with higher values of $v_{i}(S_{i})$ indicating greater success. An optimal recommendation (OR) for ESi is any $S_{i}^{*} \in A_{i}$ such that

$$
v _ {i} \left(S _ {i} ^ {*}\right) \geq v _ {i} \left(S _ {i}\right), \quad \forall S _ {i} \in A _ {i}.
$$

Later on, recommendations will be iterated using a revised valuation $w_{i}$ , but the same definitions will apply.

Suppose that $S_{i} \in A_{i}$ is a feasible recommendation for each $ESi$ , $i = 1,2,\ldots,m$ . Then $(S_1,S_2,\ldots,S_m)$ is a system of recommendations. The system of recommendations $(S_1,S_2,\ldots,S_m)$ is consistent iff there exists $S \in A$ such that $S_{i} = S\cap N_{i}$ for each $i = 1,2,\ldots,m$ .

A feasible decision $S^{*} \in A$ is an optimal decision iff, for each $i = 1, 2, \ldots, m$ , $S_{i}^{*} = S^{*} \cap N_{i}$ is an OR for ESi. Note that if $S^{*}$ is an optimal decision, then $(S_{1}^{*}, S_{2}^{*}, \ldots, S_{m}^{*})$ is automatically a consistent system of recommendations. The objective of the iteration given below is to find a system of recommendations which is consistent and optimal with respect to valuations which are as close as possible to the original valuations.

## 3.3. System Components

The overall DSS has three main components:

(1) Expert Systems (ESs). Each ES has its own knowledge base and inference engine, and has access to real world data. Each has a limited sphere of interest, expressed as $N_{i}$ . For example, an ES specialized in production would not make recommendations having to do with financial management. One important characteristic of the ES is that it can take into account new data as it becomes available. One component of this new data can be the recommendations of other ESs.

(2) Blackboard. A blackboard permits different ESs to share conclusions and data. As each ES makes an OR, it is written on the blackboard. Other associated or background data are indicated there also. The blackboard also contains a ranking, controlled by the CR, of the relative authority of each of the ESs at that particular point in time.

(3) Conflict Resolver (CR). The CR develops from the various ORs a single comprehensive recommendation to pass on to the DM.

More details about these components are now given in separate notes.

## Expert Systems

There will be times when it is necessary to add or delete ESs. Also, the knowledge base of any ES may be expanded or changed according to the circumstances. If each ES must know how to interpret every other ES, these changes in configuration could be impractical because of prohibitive time requirements.

The solution is to require that each ES know only the current ORs, but not their sources. What $ESi$ reads from the blackboard is that $ESj$ has made recommendation $S_j^*$ (of which only a subset may intersect with $A_i$ ), and that $ESj$ has a certain level of authority in the ES rankings. This approach insulates each ES from the effects of adding or deleting other ESs. Programming or reprogramming each ES requires only the capability to read and take into account these external recommendations.

In the implementation presented below, each ES reevaluates its recommendation using cardinal utilities and a numeric updating scheme. In practice, a scheme most suited to the actual design of the ESs would be chosen.

## Blackboard

The blackboard is simply a place to keep data in a form accessible to all the ESs and the CR. As envisioned, it is dynamic but performs no independent modifications to the data.

Information to be retained on the blackboard includes:

(1) The current recommendations, $S_{i}, i = 1, \ldots, m$ . Each $S_{i}$ is written by $ESi$ only.

(2) The weighting (ranking) of ESs, from most authoritative to least authoritative.

(3) Special status reports. There may be specific conditions which are of interest to all ESs. For example, in manufacturing, the inability of a major product to perform properly can affect ESs in production, marketing and financing. In military science, when a jet fighter engages in combat with the enemy, all of the ESs within the fighter will be interested in what happens and ready to take prompt action when required.

## Conflict Resolver

The CR has several requirements:

(1) It must extract $S^*$ from the posted $S_i^*$ . This is done in the obvious way if there is consistency; otherwise, by selecting actions from the ORs of the ESs for each $a_i$ according to the position of the ES in the rankings of authority. The latter operation constructs what is referred to below as the Temporary Decision.

(2) It must maintain the ranking of the relative authority of the ESs. This is done by:

(a) reference to basic defaults.

(b) medium term settings (e.g., overall production to meet projected sales over a medium term time period).

(c) short term settings (e.g., increase financing now to overcome a production problem).

The CR may have standard settings corresponding to different external environments, e.g. when sales fall below a specified level, the marketing effort should be increased.

(3) It must take care of various logical relationships among actions proposed by the ESs.

There are three possible situations relating any two actions $a_{i}$ and $a_{j}$ :

(a) unrelated; e.g., increase production of a given product and have outdated furniture in the main office replaced.

(b) mutually exclusive: there are several subcases:

(i) range of values, such as produce 1,000 units or 1,500 units of a specific product.

(ii) opposite: have machine m produce product x or produce product y.

(iii) different but incompatible: pay off suppliers and hire new staff.

(c) dependent; e.g., raw materials must be ordered and received before they are used in production.

(4) It must interact with the DM to present courses of action and accept queries and instructions.

## 4. Mathematical Development of the Conflict Resolver

## 4.1. Notation and Definitions

Some additional assumptions and definitions, beyond those given in Section 3.2, are needed to define the CR methodology fully. As well, special notation must be introduced to express conveniently some ideas introduced in Section 3.2.

Each Expert System, $ESi$ , makes a feasible recommendation $S_{i} \in A_{i}$ . A complete system of recommendations is therefore

$$
(S) = (S _ {1}, S _ {2}, \dots , S _ {m}) \in \prod_ {i = 1} ^ {m} A _ {i} = X A.
$$

Note that $(S) \in XA$ need not be consistent, but, if $(S)$ is consistent, then $(S)$ corresponds to a unique feasible decision $S \in A$ .

For $(S) = (S_{1}, S_{2}, \ldots, S_{m}) \in XA$ and $S_{i}^{\prime} \in A_{i}$ for some $i$ , define

$$
\left(S _ {i}, S _ {i} ^ {\prime}\right) = \left(S _ {1}, S _ {2}, \dots , S _ {i - 1}, S _ {i} ^ {\prime}, S _ {i + 1}, \dots , S _ {m}\right).
$$

In other words, $(S_i, S_i')$ is the system of recommendations obtained from $(S) = (S_1, \ldots, S_i, \ldots, S_m)$ on replacing $S_i$ by $S_i'$ .

An important technical assumption, not discussed previously, concerns independence of ESs.

Expert System $i$ is independent iff, whenever $S^1 \in A$ and $S^2 \in A$ , then there exists $S^3 \in A$ such that $S^3 \cap N_i = S^1 \cap N_i$ and

$$
S ^ {3} \cap (N - N _ {i}) = S ^ {2} \cap (N - N _ {i}).
$$

In other words, $ESi$ is independent iff it is possible to take any feasible decision and alter it to match any other feasible decision inside $N_{i}$ , while leaving it unchanged outside $N_{i}$ . Thus, $ESi$ is independent iff feasibility inside $N_{i}$ does not depend on the actions selected outside $N_{i}$ . An independent ES makes recommendations about any actions which can constitute necessary conditions for other actions on which it also makes recommendations.

Finally, assume that weights are assigned to ESs to fulfill two purposes which are described shortly. The weight for $ESi$ is denoted $W_{i}$ . It is assumed that $W_{i}>0$ for $i=1,2,\ldots,m$ , and that all weights are different.

The first purpose of the weights is to indicate the positions of the ESs in the (current) hierarchy. A greater weight will always be taken to indicate a higher position in the ordering. (This hierarchy is used for determining a temporary decision - see Section 4.2.) The second role of the weights is to measure the relative importance of agreement between two ESs. In the iteration (see Section 4.3), the relative worth of agreement between $ESi$ and $ESj$ on a common action is proportional to $W_i W_j$ . Note that the weights may depend on external data, so that positions in the hierarchy can shift according to the circumstances.

## 4.2. Temporary Decision

When external data change significantly, or a decision is called for, each active ES makes a recommendation. These recommendations are then integrated quickly into a temporary (or provisional) feasible decision for posting on the blackboard. This posting is necessary because any ES's evaluation can depend on system actions outside its specific decision domain. For example, an ES low in the current hierarchy may make its recommendation so as to complement the recommendations of more important ESs.

The temporary decision procedure is simple and depends only on the current system of recommendations and the current hierarchy of ESs. The recommended choices of the highest ranked ES are fixed. Then, subject to feasibility, the recommendations of the next highest ES in the hierarchy with respect to action variables not already set are followed, subject to feasibility. This procedure is repeated for lower and lower ranking ESs until values have been chosen for all decision variables. In this way, a temporary decision, sufficient to determine each ES evaluation, is obtained. Note that, if the original system of recommendations is consistent, then the temporary decision is the unique feasible decision implied by the original system.

## 4.3. Conflict Resolver Algorithm

The algorithm used by the CR will now be described both formally and informally. The definitions given in Sections 3.2 and 4.1 are assumed, and the proofs of theorems appear in the appendix. The CR works by iteration - at each repetition of the iteration, it needs a temporary decision which will be assumed to be determined as in Section 4.2.

The CR uses an iterative procedure to pass from a system of ORs to reach (eventually) a nearby system of recommendations which is consistent. The iteration is modelled on the Delphi Procedure: each system of recommendations which arises in the iteration is optimal with respect to evaluations which depend increasingly on consistency among recommendations.

To specify the iteration used by the CR, it is necessary to develop sophisticated methods of measuring the amount of consistency in a system of recommendations. Let $(S) \in XA$ and fix i and j. The match-count of ESi and ESj under $(S)$ is

$$
M _ {i j} (S) = \sharp \left(S _ {i} \cap S _ {j}\right) + \sharp \left(\left[ N _ {i} - S _ {i} \right] \cap \left[ N _ {j} - S _ {j} \right]\right).
$$

Thus, $M_{ij}(S)$ is the number of common actions on which $ESi$ and $ESj$ agree. Defining $n_{ij} = \#(N_i \cap N_j)$ , $n_i = \#(N_i)$ provides some bounds on $M_{ij}(S)$ (proofs of all Theorems appear in the appendix):

$$
\text { Theorem   1. } \quad 0 \leq M _ {i j} (S) \leq n _ {i j}. \text {   If   } i = j, M _ {i i} (S) = n _ {i}.
$$

It is also possible to characterize consistency in terms of match-counts:

Theorem 2. $(S) \in XA$ is consistent iff $M_{ij}(S) = n_{ij}$ for all $i, j$ .

Match-counts measure the consistency of a system of recommendations from the point of view of two specific ESs. A measure which adopts the viewpoint of a single ES is defined now. Define the increment of $(S)$ to ESi to be

$$
I n c _ {i} (S) = W _ {i} \sum_ {j = 1} ^ {m} M _ {i j} (S) W _ {j},
$$

where $(S) \in XA$ . Of course, $Inc_{i}(S)$ is simply the weighted sum of all match-counts of $(S)$ involving ESi. Note also that agreement on an additional action by ESj and ESj adds $W_{i}W_{j}$ to $Inc_{i}(S)$ . It can be shown that

Theorem 3. $n_i W_i^2 \leq Inc_i(S) \leq \sum_{j=1}^{m} n_{ij} W_i W_j$ .

Theorem 4. $(S) \in XA$ is consistent iff $Inc_{i}(S) = \sum_{j=1}^{m} n_{ij} W_{i} W_{j}$ for all $i$ .

It is now straightforward to combine the consistency measures for single ESs into an overall consistency index. If $(S) \in XA$ , define the consistency index at $(S)$ to be

$$
\operatorname{Con} (S) = \sum_ {i = 1} ^ {m} \operatorname{Inc} _ {i} (S).
$$

It then follows that

Theorem 5. Conmin $\leq$ Con(S) $\leq$ Conmax, where Conmin $= \sum_{i=1}^{m} n_i W_i^2$ , Conmax $= \sum_{i=1}^{m} \sum_{j=1}^{m} n_{ij} W_i W_j$ .

Theorem 6. $(S) \in XA$ is consistent iff $Con(S) = Conmax$ .

The operation of the CR iteration is now described. Assume a current system of recommendations $(S^{*})=(S_{1}^{*},S_{2}^{*},\ldots,S_{m}^{*})\in XA$ such that, for each i, $S_{i}^{*}$ is an optimal recommendation for ESi under evaluation $v_{i}(\cdot)$ . A single application of the iteration algorithm will produce a revision to $S^{*}$ which makes it more consistent according to the consistency index $Con(S^{*})$ , and which preserves the optimality property, though with respect to a slightly altered set of evaluations. Evaluations are always made in light of the current temporary decision; as well, a minimal bonus for consistency is introduced at each step. It is the two latter properties which are analogous to the Delphi Procedure.

The Delphi Procedure is embodied in the evaluation

$$
w _ {i} (S _ {i}, t) = v _ {i} (S _ {i}) + t I n c _ {i} (S _ {i} ^ {*}, S _ {i}),
$$

where $t \geq 0$ measures the bonus for consistency. (Here $w_{i}$ is the revised evaluation, $v_{i}$ is the original evaluation, $(S^{*})$ is the current system of optimal recommendations, and $S_{i}$ is any other possible recommendation for ESi.) For ESi, the value of t to be considered is the minimum effective value, $t_{\min}(i)$ , defined in Step 1. Note that, if $t > t_{\min}(i)$ , then some recommendation other than $S_{i}^{*}$ rates at least as high as $S_{i}^{*}$ under the evaluation $w_{i}(\cdot, t)$ . In other words, $t_{\min}(i)$ is the value of t at which the recommendation of ESi under $w_{i}(\cdot, t)$ changes from $S_{i}^{*}$ .

CR Algorithm Step 1
If $Inc_{i}(S^{*}) \geq Inc_{i}(S_{i}^{*}, S_{i})$ for all $S_{i} \in A_{i}, t_{\min}(i) = \infty$ . Otherwise let $A_{i}' = \{S_{i} \in A_{i}: Inc_{i}(S_{i}^{*}, S_{i}) > Inc_{i}(S^{*})\}$ and

$$
t _ {\min} (i) = \min \left\{\frac {v _ {i} \left(S _ {i} ^ {*}\right) - v _ {i} \left(S _ {i}\right)}{I n c _ {i} \left(S _ {i} ^ {*} , S _ {i}\right) - I n c _ {i} \left(S ^ {*}\right)}: S _ {i} \in A _ {i} ^ {\prime} \right\}.
$$

CR Algorithm Step 2

Set $t_{\min} = \min \{t_{\min}(i): i = 1,2,\dots,m\}$ . If $t_{\min} = \infty$ , stop the iteration. Otherwise, identify $i$ so that $t_{\min} = t_{\min}(i) < \infty$ . For $ESi$ , there exists $\overline{S}_i \in A_i'$ such that $w_i(\overline{S}_i, t_{\min}) = w_i(S_i^*, t_{\min})$ . Identify $\overline{S}_i$ . Note that $t_{\min}$ is the smallest value of $t$ at which some ES changes its recommendation.

## CR Algorithm Step 3

Replace $S_{i}^{*}$ by $\overline{S}_{i}$ , so that the current system of recommendations changes $(S_{1}^{*},\ldots ,S_{i}^{*},\ldots ,S_{m}^{*})\to (S_{1}^{*},\ldots ,S_{i - 1}^{*},\overline{S}_{i},S_{i + 1}^{*},\ldots ,S_{m}^{*})$ . For each $j-1,2,\ldots ,m$ , replace $v_{i}(\cdot)$ by $w_{i}(\cdot ,t_{\min})$ . Calculate a new temporary decision (see 4.2), which must be feasible because of the independence assumption. Return to Step 1.

The demonstration that the iteration specified above always reaches a consistent system of recommendations in a finite number of steps, and stops when and only when it attains consistency, is divided into three parts:

Theorem 7. The CR Algorithm stops if $(S^{*})$ is consistent.

Theorem 8. The CR Algorithm does not stop if $(S^{*})$ is not consistent.

Theorem 9. The CR Algorithm stops after finitely many steps.

## 5. Implementation

Two experimental implementations of a CR were made. Both assumed that the basis for the ES's decisions devolved to a comparison of the utilities of various recommendations.

The first implementation was based on a straightforward adaptation of the Delphi method to the multiple ES environment. Analysis of results from this implementation suggested a more efficient (but less obvious) approach to the problem of developing a consistent recommendation. This new theoretical basis, presented in Section 4.3, led to the second implementation.

## 5.1. First Implementation

In the first experimental implementation, the Supercalc3 spreadsheet program (similar to the popular Lotus123 package) was employed. Supercalc has a manual updating feature that is normally used to calculate the effects of changes in certain cells on other, related, cells. In the CR implementation, this updating facility was used to control the steps of information exchange and optimal recommendation revision among the ESs.

At each stage of this first implementation, every ES revised its valuation of its feasible recommendations on the basis of the current ORs of the other ESs. The current ORs are available in cells in the spreadsheet, which thus constitutes the blackboard. A bonus varied according to the number of actions on which a recommendation agreed with the ORs of the other ESs in the previous step. In this manner, the total score assigned to mutually agreeable feasible recommendations increased. Eventually, all ESs would choose a mutually consistent OR and an overall consensus was reached.

This implementation was very valuable because it provided an opportunity to study the performance of the preliminary version of the CR scheme. In particular, the conditions under which the system failed to converge were examined. It was observed that if the step size, governed by the amount of bonus given at each iteration, was too large, cycling could occur. This is because the bonus given to two or more ESs could change their ORs simultaneously. A cycle might then occur as each of two (or more) ESs change simultaneously in an attempt to match the other(s).

One way to solve this problem is to make the bonus small. The difficulty with this approach is that the number of computations required approaches infinity as the bonus approaches 0. Nonetheless, if the system is to run in real time, it must be fast.

A particularly efficient approach is to calculate the minimum bonus amount necessary to cause one ES to change its OR. With this approach, each step in the resolution procedure actually causes a change in OR, rather than just a change in the scores. The theoretical basis for this approach is presented in Section 4.3, and led to the second implementation of the CR.

## 5.2. Second Implementation

The second implementation took the form of a FORTRAN program. An output listing of this program for a very simple model of two ESs with a total of two action variables is shown in Table 1. In this case, each ES is concerned with both action variables.

To run an example as in Table 1, evaluation data for each ES is read from a file. In this case, the input file is "cr1.dat" and the output file is "cr1.out".

A box structure is used for each ES to indicate parameters associated with each of the four possible recommendations of the system. Action 1 refers to the rows of the box and action 2 to the columns. In the first row action 1 is taken, while in the second row it is not taken. Similarly, in the first column action 2 is selected, and in the second it is not. The four possible situations can be coded as $(a_{1}, a_{2})$ , $(\bar{a}_{1}, a_{2})$ $(a_{1}, \bar{a}_{2})$ and $(\bar{a}_{1}, \bar{a}_{2})$ for the north-west, south-west, north-east and south-east states, respectively.

Thus, the input values listed in Table 1 indicate that ES1 evaluates the worth of $(a_{1}, a_{2})$ at 11, $(\bar{a}_{1}, a_{2})$ at 10, $(a_{1}, \bar{a}_{2})$ at 6 and $(\bar{a}_{1}, \bar{a}_{2})$ at 5. Similarly, ES2 evaluates $(a_{1}, a_{2})$ at 3, etc. In this implementation, the blackboard is simply the FORTRAN variables available to both ESs. Note that independence is guaranteed in this case since both ESs make recommendations on both actions.

<table><tr><td colspan="4">The input file name is: cr1.dat</td></tr><tr><td colspan="4">The output file name is: cr1.out</td></tr><tr><td colspan="4">The input values are:</td></tr><tr><td>for ES1:</td><td>11</td><td>6</td><td></td></tr><tr><td></td><td>10</td><td>5</td><td></td></tr><tr><td>for ES2:</td><td>3</td><td>6</td><td></td></tr><tr><td></td><td>7</td><td>10</td><td></td></tr><tr><td colspan="4">The maximums are located:</td></tr><tr><td colspan="4">for ES1: (1,1)</td></tr><tr><td colspan="4">for ES2: (2,2)</td></tr><tr><td colspan="4">The weights are:</td></tr><tr><td>for ES1:</td><td></td><td>0.00</td><td>1.00</td></tr><tr><td></td><td></td><td>1.00</td><td>2.00</td></tr><tr><td>for ES2:</td><td></td><td>2.00</td><td>1.00</td></tr><tr><td></td><td></td><td>1.00</td><td>0.00</td></tr><tr><td colspan="4">The t-values are:</td></tr><tr><td>for ES1:</td><td></td><td>99999.00</td><td>5.00</td></tr><tr><td></td><td></td><td>1.00</td><td>3.00</td></tr><tr><td>for ES2:</td><td></td><td>3.50</td><td>4.00</td></tr><tr><td></td><td></td><td>3.00</td><td>99999.00</td></tr><tr><td colspan="4">The minimum t-value is located at: (1,2,1)</td></tr><tr><td colspan="4">The current payoffs are:</td></tr><tr><td>for ES1:</td><td>11</td><td>7</td><td></td></tr><tr><td></td><td>11</td><td>7</td><td></td></tr><tr><td>for ES2:</td><td>5</td><td>7</td><td></td></tr><tr><td></td><td>8</td><td>10</td><td></td></tr><tr><td colspan="4">The maximums are located:</td></tr><tr><td colspan="4">for ES1: (2,1)</td></tr><tr><td colspan="4">for ES2: (2,2)</td></tr><tr><td colspan="4">The weights are:</td></tr><tr><td>for ES1:</td><td></td><td>0.00</td><td>1.00</td></tr><tr><td></td><td></td><td>1.00</td><td>2.00</td></tr><tr><td>for ES2:</td><td></td><td>1.00</td><td>0.00</td></tr><tr><td></td><td></td><td>2.00</td><td>1.00</td></tr><tr><td colspan="4">The t-values are:</td></tr><tr><td>for ES1:</td><td></td><td>99999.00</td><td>99999.00</td></tr><tr><td></td><td></td><td>99999.00</td><td>4.00</td></tr><tr><td>for ES2:</td><td></td><td>99999.00</td><td>99999.00</td></tr><tr><td></td><td></td><td>2.00</td><td>99999.00</td></tr><tr><td colspan="4">The minimum t-value is located at: (2,2,1)</td></tr><tr><td colspan="4">The current payoffs are:</td></tr><tr><td>for ES1:</td><td>11</td><td>9</td><td></td></tr><tr><td></td><td>13</td><td>11</td><td></td></tr><tr><td>for ES2:</td><td>7</td><td>7</td><td></td></tr><tr><td></td><td>12</td><td>12</td><td></td></tr><tr><td colspan="4">The maximums are located:</td></tr><tr><td colspan="4">for ES1: (2,1)</td></tr><tr><td colspan="4">for ES2: (2,1)</td></tr><tr><td colspan="4">* * * CONVERGENCE * * * at decision (2,1)</td></tr></table>

The weights and t-values as described in Section 4.3 determine the next updating of the utilities. The weights indicate the degree of agreement each ES has with the other's OR. (In this illustration, both weights are 1.) For example, initially the OR for ES2 is $(\bar{a}_{1},\bar{a}_{2})$ . This does not match with $(a_{1},a_{2})$ for ES1 at all, so in the next iteration, ES1 assigns $(a_{1},a_{2})$ an increment of 0. There is one match each with $(\bar{a}_{1},a_{2})$ and $(a_{1},\bar{a}_{2})$ , so these situations are given an increment of 1. For the situation $(\bar{a}_{1},\bar{a}_{2})$ , the match is complete, so the total increment here is 2.

The t-value indicates the minimum multiple of the increment which causes a change in the OR for either ES. For example, the entry $(a_{1},\bar{a}_{2})$ for ES1 in the first set of t-values in Table 1 is 5. This indicates that if the increment for this entry (1) were multiplied by its t-value (5) then this state would have the same score as the current OR for ES1, if the OR undergoes the corresponding evaluation. Thus, for $(a_{1},\bar{a}_{2})$ the result is $6+5(1)=11$ which is the same as $11+5(0)$ for the current OR. Similarly, the calculation for $(\bar{a}_{1},\bar{a}_{2})$ for ES1 is $5+3(2)=11$ versus $11+3(0)$ for the OR.

The minimum t-value across the ESs thus indicates the first OR that will change as the bonus amount increases from 0, weighted by the degree of agreement. In this case this is the $(\bar{a}_{1}, a_{2})$ state for ES1, with a t-value of 1, as indicated in Table 1 using the notation (1,2,1). The utilities for each of the ESs are then updated according to the bonus amount calculated as the product of the minimum t-value and the increments.

However, there is not yet convergence after one iteration, since the revised OR for ES1 is $(\bar{a}_{1}, a_{2})$ but still $(\bar{a}_{1}, \bar{a}_{2})$ for ES2. Note that although the scores of both $(a_{1}, a_{2})$ and $(\bar{a}_{1}, a_{2})$ are 11 for ES1, the program always selects the newest maximum evaluation as the OR. Since there is no convergence, the process must be repeated.

Near the bottom of Table 1, it can be seen that agreement between the two ESs has been achieved at $(\bar{a}_1, a_2)$ after two iterations. As presented in Section 4.3, convergence will always occur; for the simple model of Table 1, it always occurs in two steps. This approach should be very efficient for large systems, especially after the obvious short cuts in the solution procedures are incorporated.

## 6. Summary and Conclusions

Within this paper, a comprehensive CR was developed for mediating disputes arising among interrelated ESs. When combined with ESs (and possibly other knowledge sources), the CR forms a flexible decision support package. To determine iteratively an overall recommendation from the conflicting suggestions of competing ESs, the CR follows a Delphi approach to mediation. In addition to the design structure of the CR, a mathematical proof that it always converges to a consistent recommendation has been provided here.

The foregoing accomplishments constitute a significant and important step in the development of ES methodology. The ability to put into practice a flexible CR procedure will probably be crucial to the applications of ESs now anticipated in manufacturing, military science and many other fields. However, much work remains to be done, including the following:

(1) Important theoretical questions are still open concerning the performance of the CR Algorithm, including speed of convergence, implications of independence, and branching properties.

(2) Algorithms that allow the CR to be implemented conveniently in practice must be developed.

(3) Flexible computer programs implementing the CR need to be developed for research and testing.

(4) Extensive simulation studies are necessary to evaluate and calibrate the performance of the CR over a wide range of possible scenarios and operating conditions.

## Appendix

This appendix contains proofs of the theorems in Section 4.3. All formal definitions and assumptions given in Sections 3.2, 4.1, and 4.3. are assumed and are not repeated here. This appendix should be read in conjunction with Section 4.3.

Proof of Theorem 1. Because $S_{i} \subseteq N_{i}$ and $S_{j} \subseteq N_{j}$ , it follows that

$$
\begin{array}{l} M _ {i j} (S) = \sharp \big (N _ {i} \cap N _ {j} \cap S _ {i} \cap S _ {j} \big) + \sharp \big (N _ {i} \cap S _ {i} ^ {c} \cap N _ {j} \cap S _ {j} ^ {c} \big) \\ = \sharp \big (N _ {i} \cap N _ {j} \cap \big [ (S _ {i} \cap S _ {j}) \cup (S _ {i} ^ {c} \cap S _ {j} ^ {c}) \big ] \big) \\ \leq \sharp \big (N _ {i} \cap N _ {j} \big) = n _ {i j}. \end{array}
$$

Also, it is obvious that $M_{ij}(S) \geq 0$ and that $M_{ii}(S) = n_i$ .

Proof of Theorem 2. If $(S) = (S_{1}, S_{2}, \ldots, S_{m})$ is consistent, then there exists $\overline{S} \in A$ such that $S_{i} = \overline{S} \cap N_{i}$ and $S_{j} = \overline{S} \cap N_{j}$ . Therefore,

$$
\begin{array}{r l} M _ {i j} (S) & = \sharp \big ([ \overline {{S}} \cap N _ {i} ] \cap [ \overline {{S}} \cap N _ {j} ] \big) \\ & \quad + \sharp \big ([ N _ {i} - \overline {{S}} ] \cap [ N _ {j} - \overline {{S}} ] \big) \\ & = \sharp \big (N _ {i} \cap N _ {j} \cap \overline {{S}} \big) + \sharp \big (N _ {i} \cap N _ {j} \cap \overline {{S}} ^ {c} \big) \\ & = \sharp (N _ {i} \cap N _ {j}) = n _ {i j}. \end{array}
$$

Now suppose that $M_{ij}(S) < n_{ij}$ for some $i$ and $j$ . Then, without loss of generality, there exists $k \in S_i \subseteq N_i$ such that $k \in N_j - S_j$ . Now assume that $\overline{S} \in A$ . If $k \in \overline{S}$ , then $S_j \neq \overline{S} \cap N_j$ , whereas, if $k \notin \overline{S}$ , then $S_i \neq \overline{S} \cap N_i$ . This shows that $(S_1, \ldots, S_m)$ cannot be consistent.

Proof of Theorem 3. Follows easily from Theorem 1. ||

Proof of Theorem 4. Follows easily from Theorem 2. ||

Proof of Theorem 5. Follows easily from Theorem 3. ||

Proof of Theorem 6. Follows easily from Theorem 4. ||

Proof of Theorem 7. The iteration stops if $t_{\min} = \infty$ . Now $t_{\min} = \infty$ iff $t_{\min}(i) = \infty$ for $i = 1,2,\ldots,n$ . If $(S^{*})$ is consistent, then by Theorem 4, $Inc_{i}(S^{*}) = \sum_{j=1}^{m} n_{ij} W_{i} W_{j}$ for $i = 1,2,\ldots,m$ . By Theorem 3, $Inc_{i}(S_{i}^{*}, S_{i}) \leq \sum_{j=1}^{m} n_{ij} W_{i} W_{j}$ for all $i$ and all $S_{i} \in A$ . It follows that $Inc_{i}(S^{*}) \geq Inc_{i}(S_{i}^{*}, S_{i})$ for all $S_{i} \in A$ and all $i$ , so that $t_{\min}(i) = \infty$ for all $i$ . As noted above, this implies that the iteration stops.

Proof of Theorem 8. Assume that $S^*$ is not consistent. It follows from Theorem 2 that there exists $i, j, 1 \leq i, j \leq m, i \neq j$ , and $k \in N$ such that $k \in S_i^* \subseteq N_i$ and $k \in N_j - S_j^*$ . Let $T_1 = \{h: k \in S_h^*\}$ and $T_2 = \{h: k \in N_h - S_h^*\}$ . Then $T_1 \neq \phi$ and $T_2 \neq \phi$ . If $\sum_{h \in T_2} W_h \geq \sum_{h \in T_1} W_h$ , choose any $i \in T_1$ and define $S_i = S_i^* - \{k\}$ . Then $Inc_i(S_i^*, S_i) - Inc_i(S^*) = \sum_{h=1}^{m} M_{ih}(S_i^*, S_i) W_i W_h - \sum_{h=1}^{m} M_{ih}(S^*) W_i W_h$ . Now if $h \in T_2$ , $k \in S_i^*$ , $k \notin S_h^*$ so that $M_i(S_i^*, S_i) - M_{ih}(S^*) = 1$ , whereas if $h \in T_1 - i$ , $k \in S_i^*$ , $k \notin S_i$ , and $k \in S_h^*$ so that $M_{ih}(S_i^*, S_i) - M_{ih}(S^*) = -1$ . By Theorem 1, $M_{ii}(S_i^*, S_i) = M_{ii}(S^*) = n_i$ . It follows that $Inc_i(S_i^*, S_{ii}) - Inc(S^*) = W_i[\sum_{h \in T_2} W_h - \sum_{h \in T_1 - i} W_h] > 0$ . Therefore, $t_{\min}(i) < \infty$ so that the iteration does not stop, as noted in the proof of Theorem 7. If $\sum_{h \in T_2} W_k < \sum_{h \in T_1} W_h$ , choose any $j \in T_2$ and define $S_j = S_j^* \cup \{k\}$ . Then the proof that $Inc_j(S_j^*, S_j) - Inc(S^*) > 0$ is analogous.

Proof of Theorem 9. The proof is accomplished by showing that, if $\overline{S}_i$ is obtained as in CR Algorithm Step 2, then $Con(S_i^*, \overline{S}_i) > Con(S^*)$ . This demonstrates that the algorithm always acts to make the current system of optimal recommendations more consistent according to the index $Con(S^*)$ . Furthermore, it will be proven that there exists $\epsilon > 0$ such that $Con(S_i^*, \overline{S}_i) - Con(S^*) > \epsilon$ , where $\epsilon$ depends only on the weights assigned to the ESs. Combined with Theorem 6, this implies that the system of optimal recommendations will converge to a consistent optimal decision after finitely many iterations. If $\overline{S}_i$ is as selected in Step 2,

$$
\begin{array}{l} C o n \left(S _ {i} ^ {*}, \overline {{S}} _ {i}\right) - C o n \left(S ^ {*}\right) \\ = \sum_ {j = 1} ^ {m} I n c _ {j} \left(S _ {i} ^ {*}, \overline {{S}} _ {i}\right) - \sum_ {j = 1} ^ {m} I n c _ {j} \left(S ^ {*}\right) \\ = \sum_ {j \neq i} \left[ \sum_ {k \neq i} M _ {j k} \left(S _ {i} ^ {*}, \overline {{S}} _ {i}\right) W _ {j} W _ {k} + M _ {j i} \left(S _ {i} ^ {*}, \overline {{S}} _ {i}\right) W _ {j} W _ {i} \right] \\ + \sum_ {k} M _ {i j} \left(S _ {i} ^ {*}, \overline {{S}} _ {i}\right) W _ {i} W _ {k} \\ - \sum_ {j} \sum_ {k} M _ {j k} \left(S ^ {*}\right) W _ {j} W _ {k}. \end{array}
$$

Now if $j \neq i$ and $k \neq i$ , $M_{jk}(S_i^*, \overline{S}_i) = M_{jk}(S^*)$ . By Theorem 1, $M_{ii}(S_i^*, \overline{S}_i) = M_{ii}(S^*) = n_i$ . Also $M_{ij}(S_i^*, \overline{S}_i) = M_{ji}(S_i^*, \overline{S}_i)$ and $M_{ij}(S^*) =$

$M_{ji}(S^{*})$ . These observations imply that

$$
\begin{array}{l} C o n \left(S _ {i} ^ {*}, \overline {{S}} _ {i}\right) - C o n \left(S ^ {*}\right) \\ = 2 \sum_ {j \neq i} M _ {i j} \left(S _ {i} ^ {*}, \overline {{S}} _ {i}\right) W _ {i} W _ {j} - 2 \sum_ {j \neq i} M _ {i j} \left(S ^ {*}\right) W _ {i} W _ {j} \\ = 2 \left[ \sum_ {j} M _ {i j} \left(S _ {i} ^ {*}, \overline {{S}} _ {i}\right) W _ {i} W _ {j} - \sum_ {j} M _ {i j} \left(S ^ {*}\right) W _ {i} W _ {j} \right] \\ = 2 \left[ I n c _ {i} \left(S _ {i} ^ {*}, \overline {{S}} _ {i}\right) - I n c _ {i} \left(S ^ {*}\right) \right] > 0. \end{array}
$$

Now assume that $ES1, ES2, \ldots, ESm$ are fixed so that $N_1, N_2, \ldots, N_m$ are fixed, and also the weights $W_1, W_2, \ldots, W_m$ are fixed. Then, for each $i$ and $j$ , there are a finite number of possible values of $M_{ij}(S)$ and, therefore, there are a finite number of possible values of $Inc_i(S) = \sum_j M_{ij}(S) W_i W_j$ . Let $\epsilon_i$ be the minimum difference between any two (distinct) values of $Inc_i(S)$ , and let $\epsilon = \min_i \epsilon_i$ . Then $Con(S_i^*, \overline{S}_i) - Con(S^*) > 2\epsilon$ , and this fact completes the proof, as noted above.

## References

[1] J.R. Anderson, Cognitive Psychology (Correspondent's Report), Artificial Intelligence 23 (1984) 1–11.

[2] B.M. Anderson, C. McNulty and G.S. Lystad, Expert Systems for Aiding Combat Pilots, First Annual Aerospace Applications of Artificial Intelligence (AAAI) Conference Proceedings, September 16–19, 1985 (Dayton, Ohio, 1985) 54–60.

[3] A. Barr and E.A. Feigenbaum, The Handbook of Artificial Intelligence, Vol. 3 (William Kaufman, Los Altos, California, 1982).

[4] B.G. Buchanan, New Research on Expert Systems, in: J.E. Hayes, D. Michie and Y.H. Pao (Eds.), Machine Intelligence 10 (Ellis Horwood, Chichester, England, and Halstead, New York, 1982) 269–299.

[5] B. Chandrasekaran, Natural and Social System Metaphors for Distributed Problem Solving: Introduction to the Issue, IEEE Transactions on Systems, Man and Cybernetics SMC-11 Nr. 1, (1981) 1–5.

[6] N. Dalkey, The Delphi Method - An Experimental Study of Group Opinion, Technical Report Number RM-3855-PR, The Rand Corporation (1969).

[7] R. Davis and R.G. Smith, Negotiation as a Metaphor for Distributed Problem Solving, Artificial Intelligence 23 (1983) 63–109.

[8] A. Dutta and H.K. Jain, A DSS for Distributed Computer System Design in the Presence of Multiple Conflicting Objectives, Decision Support Systems 1 (1985) 233–246.

[9] N.M. Fraser and K.W. Hipel, Conflict Analysis: Models and Resolutions (North-Holland, New York, 1984).

[10] M.J. Ginzberg, W. Reitman and E.A. Stohr (Eds.), Decision Support Systems, Proceedings of the New York Uni-

versity Symposium on Decision Support Systems, May 21–22, 1981 (North-Holland, Amsterdam, 1982).

[11] B. Hayes-Roth, A Blackboard Architecture for Control, Artificial Intelligence 26 (1985) 251–321.

[12] F. Hayes-Roth, D.A. Waterman and D.B. Lenant (Editors), Building Expert Systems (Addison-Wesley, Reading, Massachusetts, 1983).

[13] C.M. Hoyland, K.H. Evers and D.E. Snyder, Incorporating Human Operator Considerations into Existing Weapon System Analysis and Quantification Capabilities, Proceedings of the 1985 National Aerospace and Electronics Conference (NAECON), May 1985 (Dayton, Ohio, 1985) 1–6.

[14] D.M. Kilgour, K.W. Hipel and N.M. Fraser, Solution Concepts in Non-Cooperative Games, Large Scale Systems 6 Nr. 1 (1984) 49–71.

[15] H.A. Linstone, The Delphi Technique, in: V.T. Covello et al. (Eds.), Environmental Impact Assessment, Technology Assessment, and Risk Analysis (Springer-Verlag, Berlin, NATO ASI Series, G4, 1985) 621–649.

[16] M.D. McNeese, Humane Intelligence: A Human Factors Perspective for Developing Intelligent Cockpits, Proceedings of the 1986 National Aerospace and Electronics Conference (NAECON), May 1986 (Dayton, Ohio, 1986) 941–948.

[17] C.V. Negoita, Expert Systems and Fuzzy Systems (Benjamin/Cummings, Menlo Park, California, 1985).

[18] E.S. Quade, Predicting the Consequences: Models and Modelling, in: H.J. Miser and E.S. Quade (Eds.), Handbook of Systems Analysis, (North-Holland, New York, Ch. 7, 1985).

[19] A.P. Sage and W.B. Rouse, Aiding the Human Decisionmaker Through the Knowledge-Based Sciences, IEEE Transactions on Systems, Man and Cybernetics SMC-16, Nr. 4 (1986) 511–521.

[20] E.E. Smith, Cognitive Psychology (Correspondent's Report), Artificial Intelligence 25 (1985) 247–253.

[21] J. von Neumann and O. Morgenstern, Theory of Games and Economic Behavior, Third Edition (Princeton University Press, Princeton, New Jersey, 1953).
