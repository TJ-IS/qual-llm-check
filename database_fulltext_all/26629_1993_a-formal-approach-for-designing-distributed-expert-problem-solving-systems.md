---
otero_id: 26629
otero_key: "F3ACTCPA"
title: "A Formal Approach for Designing Distributed Expert Problem-Solving Systems"
authors: "Prabuddha De; Varghese S. Jacob; Ramakrishnan Pakath"
year: "1993"
journal: "Information Systems Research"
doi: "10.1287/isre.4.2.141"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## H4R

![](/api/attachments/F3ACTCPA/fulltext/images/e8c865adae8dc06e20413ece704d2eea453b7fc8d46d2f5175dd71dbe62f445e.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# A Formal Approach for Designing Distributed Expert Problem-Solving Systems

Prabuddha De, Varghese S. Jacob, Ramakrishnan Pakath,

## To cite this article:

Prabuddha De, Varghese S. Jacob, Ramakrishnan Pakath, (1993) A Formal Approach for Designing Distributed Expert Problem-Solving Systems. Information Systems Research 4(2):141-165. http://dx.doi.org/10.1287/isre.4.2.141

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1993 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/F3ACTCPA/fulltext/images/9ffd31fa42fd5897c1e37dbbb9c1b5e92da8b19874bfc9c99c037873d89f19bb.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# A Formal Approach for Designing Distributed Expert Problem-solving Systems

Prabuddha De

Department of Management Information Systems and

Decision Sciences

University of Dayton

Dayton, Ohio 454o9-2130

Varghese S. Jacob

Department of Accounting and Management Information Systems

Ohio State Univer;íty

Columbus, Ohuo 43210-1399

Ramakrishnan Pakath Department of Deciston Science and Information Systems Department of Deciston Science and Information Systems

Universuty of Kent;cky

Lexington, Kentu ky 40506-0034

In this paper, we consider the problem of generating effective informationgathering, communication, and decision-making (ICD) strategies for a distributed expert problem-solving (DEPS) system. We focus on the special case of a dual-processor DEPS system and present a decision-theoretic model that enables the characterization of feasible, efficient, and optimal ICD strategies. In view of the tremendous amount of computing needed to generate optimal strategies for problems of practical size, we develop useful heuristic procedures for constructing high-quality efficient ICD strategies. We illustrate the use of the model and the solution procedure through an example.

Expert systems—Distributed probiem solving—Fconomic decísion theory--Information-gathering, communication, and decision-making strategies—Computational complexit

## 1.0. Introduction

n several key functional areas of contemporary business (e.g., production, account-Ling, finance, etc.), expert systems (ESs) have steadily been gaining ground as robust and reliable computerized consultants tha1 facilitate effective decision making. This paper describes a decision-theoretic methodology for developing effective designs for what we call a distributed expert problem-solving (DEPS) system. A DEPS system contains multiple ESs and exploits soine of the advantages of distributed processing which pervades much of business computing today.

In general, the distributed-computing approach has been advocated as a panacea for many of the drawbacks associated with traditional, uniprocessor problem solving (e.g., see Date (1983. 1990)). Major disadvantages of the latter include reduced levels of system modularity, adaptability, responsiveness and availability, accompanied by a concurrent increase in processing bottlenecks and conflict levels. In order to contain such limitations, the distributed technique recommends the use of multiple processors, each of which works on some facet of the solution process. In the context of expert problem solving, the distributed system is composed of multiple, interconnected ESs. Each ES in the system possesses knowledge that is potentially useful in the partial resolution of a complex decision problem faced by the entire system and, consequently, could be made responsible for some portion of the total problem-processing effort.

Apart from mitigating the general weaknesses of centralization, there is one other reason that could make integration of expertise desirable. Quite often the components for integration already exist and we wish to take advantage of their joint capabilities. For instance, we may wish to bring together several specialized medical diagnosis systems to handle a complex medical case. It may perhaps be more cost- and time-effective to integrate the existing component systems than to construct a new, monolithic system that duplicates their collective capabilities.

Given the benefits of distribution, paramount among the many considerations in developing a distributed system is the issue of communication and coordination among its multiple processors. The objective of our work is to address this issue in the context of a special case of the general DEPS system. As a first step toward more general studies of the topic, this paper considers a system consisting of two processors that are experts in related domains. We visualize problem solving as the performance of a set of information-gathering and communication actions by these two experts prior to taking a final decision. Each such action has an associated performance-cost. In a typical case, it may be necessary or desirable for both processors to be involved in problem solving as an economic team. One processor in the team would act as the deciding participant and the other as a supporting participant whose services are enlisted by the former.

Given this scenario, the paper seeks an answer to the following question: Which of the available information-gathering actions are utilized by the two processors and in what sequence? In the process, it also provides an answer to the related question: When do the processors communicate with each other during their collective problem-solving endeavor? These answers are critical for the implementation of a DEPS system. They identify effective information-gathering, communication, and decisionmaking (ICD) strategies for the implementation.

The rest of this paper is organized as follows: Section 2 contains a review of the related literature. In §3, the assumptions underlying our decision-theoretic model are stated, followed by a formal description of the model. Section 4 describes an illustrative problem scenario and maps the theoretical constructs of the preceding section to this scenario. Section 5 presents effective solution procedures for developing highquality ICD strategies and uses the example scenario of §4 to illustrate the use of these procedures. Concluding observations are provided in §6.

## 2.0. Related Literature

Our approach seeks to formally model a DEPS system using principles developed in economic theory. The primary building blocks for the proposed model are contained in a formal study of decision making with sequential information-gathering by Moore and Whinston (1986, 1987).

The Moore-Whinston framework is a powerful modeling tool that has been successfully applied (either directly or with suitable extensions) in the past for representing a variety of problem situations. These applications include studies on message routing in communications networks (Balakrishnan et al. 1991), expert system design (Hall et al. 1986 and Jacob et al. 1988), human-computer team decision-making systems (Jacob et al. 1989), information retrieval (Moore et al. 1988, 1990a), distributed algorithm design (Moore et al. 1990b), and resource allocation (Rao et al. 1990).

Despite its significant modeling capabilities, the ease with which the framework allows the development of effective model solvers is typically governed by the problem context. Thus, some of these studies only focus on the characterization of conditions needed to generate solutions (e.g., Jacob et al. 1989). Others seek to develop specialized solution strategies for the particular problem addressed (e.g., Moore et al. 1988). Relatively few studies (e.g., Balakrishnan et al. 1991) attempt to develop generalized solution approaches that may be extended to other contexts.

Of particular relevance to our work are the applications by Hall et al. (1986) and Jacob et al. (1988, 1989). As we note below, the present study may be viewed as a direct extension of these efforts.

Hall et al. (1986) and Jacob et al. (1988) apply the Moore-Whinston model in constructing a tool that facilitates the design of computationally-efficient expert systems. That is, the tool modifies a given set of reasoning knowledge (in the form of production rules, for instance) into a computatonally more efficient set. Their work, however, studies the case of a conventional, uniprocessor expert system. Our research extends their effort toward the more general case of a distributed, multiprocessor system.

Jacob et al. (1989), like ourselves, develop ID strategies for a two-member team decision-making system. The deciding participant in their model is a human while a computer fills the role of a supporting participant. The model is applied to a specific class of problems. In this paper, we present a more general framework; it also incorporates further details of the underlying process. Moreover, while the efforts by Hall et al. (1986) and Jacob et al. ( 1988, 1989) do not attempt to develop solution algorithms, we present generalized solution procedures for our framework.

## 3.0. The Model

Notation. Our model makes use of the following major notation. Additional notation is introduced as necessary. (In general, our notation closely parallels that of Moore and Whinston (1986, 1987), with modifications made only to facilitate generalization to the dual-processor scenario.)

$X \colon X = \{ \ v { x } \colon \ v { x } \}$ denotes the state space containing the (finite) set of all possible mutually exclusive states of the decision problem under consideration, where x is an arbitrary member of X.

φ(x): The probability that $x \in X$ is the true state, where $\phi ( x ) > 0$ and $\scriptstyle \sum _ { x \in X } \phi ( x )$ $= 1 .$

$D \colon D = \{ d \}$ is the ( finite) set of final decisions available to the system, where d is an arbitrary member of D

A: $A = \{ \mathbf { a } \} = A _ { 1 } ^ { c } \cup A _ { 2 } ^ { e } \cup A ^ { c }$ denotes the (finite) set of actions available to the system, where a is an arbitrary member of A. Here, A and Aζ denote the sets of information-gathering actions available to processors 1 and 2, respectively, and A° denotes the set of communication actions available to both processors. Thus, $A _ { 1 } ^ { e } \cup A ^ { c }$ and $A _ { 2 } ^ { e } \cup A ^ { c }$ denote the action sets associated with processors 1 and 2, respectively The set $A _ { 1 } ^ { e } \cup A _ { 2 } ^ { e }$ also contains a special type of information-gathering action called the null (or “do nothing") action. In the subsequent analysis, we assume, without any loss of generality, that the null action is always performed by processor 1.

ω: ω: $X * D  R$ denotes the gross payoff function that associates a real-valued payoff $\omega ( x , d )$ with each state-decision pair $( x , d )$

$c \colon c \colon A \to R ^ { \geq 0 }$ denotes the cost function that associates a nonnegative, real-valued cost $c ( \mathbf { a } )$ , with action $\mathbf { a } \in A \left( \mathrm { i . e . } \right.$ , a cost of $c ( \mathbf { a } )$ is incurred in performing a).

r: A nonnegative integer denoting the total number of information-gathering actions that must be performed prior to making a final decision. (Some of these could be null actions.)

t: A nonnegative integer denoting the total number of all actions (i.e., null and nonnull information-gathering and communication actions) that are actually performed before a final decision is made.

Assumptions. A key assumption we make is that the system's goal is expected-netpayoff maximization, with the effectiveness measure being assessed across the entire class of problems for which the system is designed. With this assumption, all processors in the system subscribe to the stated global objective and their actions, consequently, are not biased by individual, goal-related differences. While joint human efforts could be undermined by group vs. personal goal conflicts, there is no reason to embody such human weaknesses within a computerized system. Thus, the assumption of nonconflicting goals is not impractical or undesirable for a DEPS system.

In addition, our model is based on the following assumptions that are generally consistent with conditions in the real world and are of the kind routinely made in mathematical modeling.

(1) The parameters $X , \left\{ { \phi ( x ) } : x \in X \right\} , D , A , \left\{ { \omega ( x , d ) } : x \in X , d \in D \right\} , \left\{ { c ( { \mathbf { a } } ) } : { \mathbf { a } } \right\} { \mathbf { a } } \in X .$ $\in A \}$ , and r are all known at the beginning of the solution process.

It is not impractical to require that these parameters be known a priori. We are modeling human experts here, and it is reasonable to assume that they would be able to prespecify such parameters fairly accurately. The parameter r may be thought of as being largely influenced by prevailing time constraints on the decision process. The value of the parameter t, however, is strategy-dependent and not predetermined (see our discussions concerning communication in assumption (3) and §§3.1, 3.2, and 5.0).

By determining the best or a good ICD strategy for a given r, we are pursuing a methodology that is different from what is commonly used in statistical sampling. In the latter (e.g., see DeGroot 1986), we typically determine the sample size, say r, that would enable the realization of a prespecified level of precision in a decision. For example, statisticians routinely select the sample size needed to generate a desired confidence interval for the estimate of a parameter. Each approach has applications for which it is appropriate. Prespecification of r is fitting in contexts like combat and medicine where a decision maker does not usually have the time to perform a statistically appropriate number of experiments prior to making a decision.

(2) Problem solving involves determining the true state of nature, given a discrete set of possible states $( \mathfrak { i . e . , } X )$ . A probability distribution defined over the state space (i.e., ${ \left\{ \phi ( x ) : x \in X \right\} } $ captures the uncertainty associated with identifying the true state. The true state does not change during the problem-solving process.

This assumption rests on the fact that most expert systems address diagnosis- or categorization-type problems. In medical diagnosis, for example, the set of possible states may refer to the set of possible human ailments and the true state, then, would correspond to a particular ailment a patient is suffering from.

Further, we are focussing on the special case of static stochasticity. The more general case of a stochastic and dynamic environment would require analysis using techniques like Markov processes, Brownian motion, or simulation (that we do not employ here). The assumption of stationary conditions is valid in contexts where the time horizon of the decision process is sufficiently small (e.g., when conducting emergency maneuvers in a battlefield) or when changes occur at a relatively slow rate (e.g., in a stable economy). In such situations, even a dynamic environment may be regarded as being stable for the period of the analysis

(3) Each processor can perform a specific set of actions $( \mathrm { i } . \mathsf { e } . , \ A _ { 1 } ^ { e } \cup \ A ^ { c }$ and A€ $\cup A ^ { \prime } \}$ . The problem-solving process starts with any one of the two processors, denoted as processor 1. The solution steps are viewed as the performance of a series of information-gathering $( \mathrm { i . e . , a } \in A _ { 1 } ^ { e } \cup A _ { 2 } ^ { e } )$ and communication $( \mathrm { i } . \mathrm { e } . , \mathbf { a } \in A ^ { c } )$ actions by the two processors, followed by decision making. Processor 1 also makes the final decision $( \mathfrak { i . e . , } d \in D )$ . It is possible that both processors can perform a particular action.

Processor 1 utilizes a communication action in requesting information-gathering assistance from processor 2. Processor 2 subsequently responds, also using a communication action. Note that we use the term communication action only with regard to sending a communication—i.e., there is no action ascribed to the process of receiving a communication.

Our treatment of actions and decisions is consistent with that found in team decision making where the deciding and supporting participants play specific roles

(4) Actions are performed sequentially. Therefore, at a given instant, orly one of the two processors is active, with the other remaining in an idle state. In particular, after one processor communicates with the other, it remains in an idle state until it receives a communication in return.

The sequential strategy is appropriate in contexts (for instance, medical diagnosis) where it is generally more effective to choose subsequent actions based on the outcomes of prior actions in an action sequence. When idling, a processor could be receiving communication from the other processor; by assumption (3), we do not view this as the performance of an action. Also, it is entirely possible that the processor could be working on some unrelated problem during this interval.

The notion of an information structure is central to our model and is discussed next along with some related terminology. Following this, we develop expressions and conditions that characterize feasible, efficient and optimal ICD strategies.

## 3.1. Information Structure and Related Concepts

Let the set $A _ { 1 } ^ { e } \cup A _ { 2 } ^ { e } = \{ \mathbf { a } _ { 0 } , \mathbf { a } _ { 1 } , \dots , \mathbf { a } _ { n - 1 } \}$ denote the total set of n information-gathering actions available to the system. With each information-gathering action a ${ \mathfrak { r } } \in A _ { 1 } ^ { e }$ U $\boldsymbol { A } _ { 2 } ^ { e }$ , we associate a (finite) set of information-gathering signals $Y _ { \bullet } = \{ 1 , 2 , \dots , $ $m ( { \mathfrak { a } } ) \}$ and a function $\eta _ { \mathrm { a } } ; X \to Y _ { \mathrm { ~ a ~ } }$ . We treat $\mathbf { a } = \mathbf { a } _ { 0 }$ as the null action and define $m ( \mathfrak { a } _ { 0 } )$ $= 1$

For a given $x \in X ,$ there is a single signal receivable from each of the n informationgathering actions. The information-gathering process, therefore, is viewed as being deterministic. Thus, if an action $\mathbf { a } \in A _ { 1 } ^ { e } \cup A _ { 2 } ^ { e }$ is performed and the signal $y \in Y _ { \mathbf { a } }$ is received, then it is known that the true state X is an element of the set $M _ { \mathrm { a } , y }$ defined by

$$
M _ {\mathbf {a}, y} = \{x \in X: \eta_ {\mathbf {a}} (x) = y \} \quad \text {   for   all   } \mathbf {a} \in A _ {1} ^ {e} \cup A _ {2} ^ {e} \text {   and   all   } y \in Y _ {\mathbf {a}}.
$$

For any action a, $M _ { \mathrm { a } , y }$ , is a nonempty subset of X, and the family of such subsets of X, defined by

$$
M _ {\mathbf {a}} = \left\{M _ {\mathbf {a}, 1}, M _ {\mathbf {a}, 2}, \dots , M _ {\mathbf {a}, m (\mathbf {a})} \right\} \quad \text {   for   all   } \mathbf {a} \in A _ {1} ^ {e} \cup A _ {2} ^ {e},
$$

will be a partition of X. After action a is performed, one will know to which of the $M _ { \mathrm { a , y } }$ the true state belongs. Formally, for any $\mathbf { a } \in A _ { 1 } ^ { e } \cup A _ { 2 } ^ { e } , M _ { \mathbf { a } }$ is referred to as an informá- tion structure on X that is induced by the information-gathering action a.

During a communication, one processor transmits some member, say B, from the current partition of X to the other processor for further analysis and experimentation. As the act of communication itself does not cause a partitioning of B, for any : $\in A ^ { c }$ we let $M _ { \mathbf { a } } = B$ . We note that for a given state space X and action set A, the transmitted element B can only be a member, or a union of some of the members, of what is called the finest partition or information structure on X obtainable from $A$ , as described below.

The finest information structure $\mathbf { B } ^ { A }$ obtainable from A is the information structure which would result if one were to perform all of the nonnull information-gathering actions in A following any sequence. It is straightforward, albeit somewhat tedious, to verify that $\mathbf { B } ^ { A }$ may be expressed in terms of the members of $M _ { \mathbf { a } }$ as follows, for all a $\in A _ { 1 } ^ { e } \cup A _ { 2 } ^ { e }$

$$
\begin{array}{l} \mathbf {B} ^ {A} = \left\{\bigcap_ {\mathbf {a} = 1} ^ {n - 1} M _ {\mathbf {a}, 1}, \bigcap_ {\mathbf {a} = 1} ^ {n - 2} M _ {\mathbf {a}, 1} \cap M _ {n - 1, 2}, \dots , \bigcap_ {\mathbf {a} = 1} ^ {n - 2} M _ {\mathbf {a}, 1} \cap M _ {n - 1, m (n - 1)}, \right. \\ \left. \bigcap_ {\mathbf {a} = 1} ^ {n - 3} M _ {\mathbf {a}, 1} \cap M _ {n - 2, 2} \cap M _ {n - 1, 1}, \dots , \bigcap_ {\mathbf {a} = 1} ^ {n - 3} M _ {\mathbf {a}, 1} \cap M _ {n - 2, 2} \cap M _ {n - 1, m (n - 1)}, \right. \\ \left. \dots , \bigcap_ {\mathbf {a} = 1} ^ {n - 1} M _ {\mathbf {a}, m (\mathbf {a})} \right\} \backslash \{\varnothing \}. \end{array}
$$

Here $\varnothing$ denotes an empty set and $\{ \emptyset \}$ denotes the set of all possible empty sets that could result from null intersections in the expression for $\mathbf { B } ^ { A }$

Each action has an associated performance-cost. Typically, the cost of an information-gathering action $( \mathfrak { i . e . , } c ( \mathbf { a } )$ for $\mathbf { a } \in A _ { 1 } ^ { e } \cup A _ { 2 } ^ { e } )$ would depend on the sophistication of the action under consideration. That is, actions that yield more information (or finer partitions) are usually more expensive (monetarily) than those that yield less information. In particular, the null action yields no information at all and does not cost anything. The cost of a communication action $( \mathfrak { i . e . , } c ( \mathbf { a } )$ for a $\in A ^ { c } )$ may be viewed as being proportional to the size of the information structure member being communicated.

If B is some nonempty subset of X, the information structure B induced on set B by an action a (also denoted as $\iota ( B , \mathbf { a } ) )$ is characterized as follows:

$$
\mathbf {B} = \iota (B, \mathbf {a}) = \left\{ \begin{array}{l l} \{B \cap M _ {\mathbf {a}, 1}, B \cap M _ {\mathbf {a}, 2}, \dots , B \cap M _ {\mathbf {a}, m (\mathbf {a})} \} \setminus \{\varnothing \} & \text { if } \mathbf {a} \in A _ {1} ^ {e} \cup A _ {2} ^ {e}, \\ B \quad \text { if } \mathbf {a} \in A ^ {e}. \end{array} \right.
$$

We say that $\iota ( B , \mathbf { a } )$ is nontrivial, it $\# \iota ( B , \mathbf { a } ) \geq 2 ( \mathsf { i . e }$ ., if the result contains at least two elements).

We could extend this characterization to the more general case of information structures induced on the members of an existing information structure B by an action function α: $\mathbf { B }  A$ that associates some $\bullet \in { \cal A }$ with each of the members, say $B _ { 1 } , B _ { 2 } , \ldots , B _ { k }$ , of B. Such an inducement is denoted as $\iota ( \mathbf { B } , \alpha )$ , where

$$
\iota (\mathbf {B}, \alpha) = \bigcup_ {j = 1} ^ {k} \iota (B _ {j}, \alpha (B _ {j})).
$$

(In subsequent discussions, we frequently use the term refinement of, say B, as a convenient short-hand in lieu of the expression nformation structure induced on B.)

In general, different actions could result in different refinements of a given B. Consequently, it is possible for us to compare two or more information structures on B purely in terms of the fineness of the partitions they provide. Essentially, if B and B' are both information structures on B, we say that B is as fine as B', denoted as $\mathbf { B } \succcurlyeq \mathbf { B } ^ { \prime }$ if

$$
(\forall B \in \mathbf {B}) (\exists B ^ {\prime} \in \mathbf {B} ^ {\prime}): B \subseteq B ^ {\prime}.
$$

## 3.2. Feasibility, Efficiency and Optimality

A general ICD strategy for a dual-processor DEPS system is defined as a sequence:

$$
\sigma = \left\langle [ \mathbf {B} _ {1}, \alpha_ {1} ], [ \mathbf {B} _ {2}, \alpha_ {2} ], \dots , [ \mathbf {B} _ {t}, \alpha_ {t} ]. [ \mathbf {B} _ {t + 1}, \delta ] \right\rangle \quad \text { where }
$$

(1) $\mathbf { B } _ { 1 } = \{ { \cal X } \}$

(2) (a) α: B, → A for j = 1, 2, . . . , t,

$$
(b) \mathbf {B} _ {j + 1} = \iota (\mathbf {B} _ {j}, \alpha_ {j}) \text {   for   } j = 1, 2, \dots , t, \text {   and   }
$$

(3) δ: Bt +1 → D.

In each of these expressions, the subscript indicates the stage of the solution process. The entire strategy consists of $( t + 1 )$ stages. By assumption (3), processor 1 starts the process by performing the very first action in the sequence at stage 1. At each of the stages $2 , 3 , \ldots , t$ , the two processors continue performing some kind of action. At stage $( t + 1 )$ , processor 1 utilizes the decision function δ: $\mathbf { B } _ { t + 1 }  D$ to associate a final decision $d \in D$ with each member of the final partition $\mathbf { B } _ { t + 1 }$ of X. A general ICD strategy also satisfies assumption (4) of §3.0. Thus, processor 2 is idling at stages 1 and (1 + 1), and one of the two processors is idling at every $B \in { \bf B } , j = 2 , 3 .$ $\cdots , t .$

A general ICD strategy is feasible if it also satısfies the following restrictions on communication:

Communications, if any, are always initiated by processor 1. Whenever processor 1 communicates a B to processor 2, the latter must subsequently communicate each of the members of its refinement of B back to processor 1.

An optimal strategy is a feasible strategy that maximizes the expected net payoff. In order to characterize the expected net payoff, we require the following definitions concerning predecessor sequences and action sequences

Let σ be a feasible strategy. Then, for each $B \in \mathbf { B } _ { q } , q \in \{ 2 , 3 , . . . , t + 1 \}$ , the sequence $\left. \mathbf { B } _ { 1 } ( B ) , \mathbf { B } _ { 2 } ( B ) , \ldots , \mathbf { B } _ { q - 1 } ( B ) \right.$ , is referred to as the sequence $o f ( q - 1 )$ predecessors of B. The jth element of the sequence, $\mathbf { B } , ( B )$ , is defined by

$$
\mathbf {B} _ {j} (B) = B ^ {\prime} \in \mathbf {B} _ {j} \text {   such   that   } B \subseteq B ^ {\prime} \quad \text {   for   } j = 1, 2, \dots , q - 1.
$$

$\mathbf { B } , ( B )$ is called the predecessor of B at stage j. Note that these predecessors define a path from the beginning of the solution process to $B$

By identifying the path that yields B, we are also able to isolate the actions taken along this path. Formally, for each $B { \in } \mathbf { B } _ { q } , q { \in } \left\{ 2 , 3 , \ldots , t + 1 \right\} , \left. \mathbf { a } _ { 1 } ( B ) , \mathbf { a } _ { 2 } ( B ) \right.$ $\mathbf { a } _ { q - 1 } ( B ) \rangle$ denotes the sequence of $( q - 1 )$ actions performed along the path that vields B. Here $\mathbf { a } _ { \ j } ( B ) = \alpha _ { \ j } [ \mathbf { B } _ { \ j } ( B ) ]$ denotes the action taken at step $j , j = 1 , 2 , . . . ,$ $q - 1$

In a given realization of a decision problem, a DEPS system could apply a feasible strategy to determine whether the true state X is an element of some $B \in \mathbb { B } _ { t + 1 }$ . The cost $C ( B )$ of determining this is the sum of the costs of all actions taken along the path yielding B:

$$
C (B) = \sum_ {j = 1} ^ {t} c [ \mathbf {a} _ {j} (B) ].
$$

Hence, the expected cost $\Gamma ( \sigma )$ of strategy σ is

$$
\Gamma (\sigma) = \sum_ {B \in \mathbf {B} _ {t + 1}} \pi (B) C (B) \quad \text { where } \quad \pi (B) = \sum_ {x \in B} \phi (x).
$$

By definition, the gross payoff of making decision $\delta ( B )$ is $\omega [ x , \delta ( B ) ]$ where $x \in B$ $\mathbf { \Xi } \in \mathbf { B } _ { t + 1 }$ . Therefore, the expected gross payoff $\operatorname { \Pi } \operatorname { \Omega } ( \sigma )$ from strategy σ is

$$
\Omega (\sigma) = \sum_ {B \in \mathbf {B} _ {t + 1}} \sum_ {x \in \mathbf {B}} \phi (x) \omega [ x, \delta (B) ],
$$

and, hence, the expected net payoff associated with strategy σ is

$$
\Omega^ {*} (\sigma) = \Omega (\sigma) - \Gamma (\sigma).
$$

As mentioned, an optimal ICD strategy is a feasible strategy that maximizes $\Omega ^ { * } ( \cdot )$ However, often the space of feasible strategies may itself be too large, making a search of this space for the optimal strategy computationally intractable. It is, therefore, desirable to prune the solution space and to restrict the search to a subset of the space. We next characterize a class of strategies, called efficient strategies, that constitute such a subset of the set of feasible strategies. As the following discussion shows, efficient strategies dominate all other feasible strategies in that, given a strategy which is not efficient, one can always generate an efficient strategy whose expected net payoff is at least as much as that of the original strategy.

The definition of efficient strategies requires the introduction of two additional terms $\mathfrak { v } ( \cdot )$ and $D ^ { * } ( \cdot )$ . For a given nonempty subset B of $X ,$ , we define v(B) and $D ^ { * } ( B )$ as

$$
\begin{array}{c} v (B) = \max _ {d \in D} \sum_ {x \in B} \phi (x | B) \omega (x, d) \quad \text { and } \\ D ^ {*} (B) = \left\{d \in D: \sum_ {x \in B} \phi (x | B) \omega (x, d) = v (B) \right\}, \end{array}
$$

respectively. The conditionally optimal decision set $D ^ { * } ( B )$ for B is the set of all decisions that enable the attainment of the potential gross payoff associated with B. The potential gross $p a \nu o f f \nu ( B )$ for B is the maxımum expected gross payoff obtainable by making a decision based on the information contained in B.

Then, for each $d \in D$ , let $\textstyle X _ { d } = \bigcup _ { B \in { \mathbb { B } } ^ { d } ( d ) } B$ , where

$$
\mathbf {B} ^ {A} (d) = \{B \in \mathbf {B} ^ {A} | d \in D ^ {*} (B) \}.
$$

The set $X _ { d }$ contains the union of those subsets of the finest information structure $\pmb { \mathrm { B } } ^ { A }$ for which the final decision is the same $( \mathrm { i } . \mathbf { e } _ { . , d ) }$ . The advantage of computing $\{ X _ { d } \colon$ d $\in D \}$ is that if during the execution of a strategy, the system encounters a B such that $B \subseteq X _ { d }$ , for some $d ,$ , then there is no need to partition B further since, for any $B \subseteq X _ { d }$ the optimal decision is d

A feasible strategy σ is efficient if each of the following conditions holds:

(1) For any $B \in { \bf B } _ { , } , j = 1 , 2 , \ldots , t , \mathrm { i f } \alpha _ { , } ( B ) = { \bf a } \in \{ { \bf a } _ { 1 } , { \bf a } _ { 2 } , \ldots , { \bf a } _ { n - 1 } \}$ , then the resultant refinement is nontrivial.

(2) Forany $B \in { \bf B } , j = 1 , 2 , \ldots , t , \operatorname { i f } B \subseteq X _ { d }$ for some $d ,$ , then there is no attempt at nontrivially refining B; further, there is no attempt at communicating any such B to processor 2.

(3) For each $B \in \mathbf { B } _ { \iota + 1 } , \delta ( B ) \in D ^ { * } ( B )$

$$
(4) \text {   If   } \alpha_ {j} (B) = \mathbf {a} _ {0}, \text {   then   } \alpha_ {j + 1} (B) = \mathbf {a} _ {0}, \text {   for   } j = 1, 2, \dots , t - 1.
$$

Clearly, if any of the first two conditions for efficiency is violated, the result is to incur a cost without obtaining a beneficial refinement of B. Condition (3) ensures that the final decision is optimal for B. Thus, if one identifies a strategy that violates any of the first three conditions for efficiency, then one can always construct a less costly strategy that offers the same expected gross payoff. Finally, condition (4) implies that null actions, if any, should be performed as late as possible along any path of a strategy. This is because null actions do not contribute to the expected net payoff ın any way. By postponing them the most we can, we allow for the maximum possible use of nonnull actions and thereby maximize the chances of earning a higher expected net payoff. Clearly, given a feasible strategy that violates condition (4), one can always generate an efficient strategy whose expected net payoff is at least as much as that of the original strategy.

Despite the identification of the efficient-strategy space for a problem, in order to guarantee that a chosen strategy is indeed optimal, one must resort either to complete enumeration or to some other enumerative approach (e.g., a dynamic program or a branch and bound scheme) in searching this space. However, this pruned space may still be too large, making the search using such rnethods unacceptable from a computational standpoint. This leads us to consider the development of computationally efficient heuristic procedures. We describe that development in §5. But first in §4, we present an example dual-processor problem and illustrate the theoretical developments of this section through the example.

## 4.0. An Illustrative Example

A defense system consisting of two intelligent sensors (i.e., expert processors) must take decisions regarding the activation of an appropriate defense strategy to counter a potential threat by invading enemy forces. Sensor 1 is the deciding participant and sensor 2 acts as an assistant. It is known that the imminent attack will involve either tanks or armored personnel carriers. However, the nature of the attack and, hence, the choice of a defense strategy depend on several factors as detailed below.

The enemy has three types of tanks, namely, light (LTs), medium (MTs), and heavy tanks (HTs), and three types of armored personnel carriers, small (SCs), midsize (MCs), and large carriers (LCs). An SC can transport 100 personnel, an MC can transport 125, and an LC can transport 160. The number of vehicles in an attack is a function of the type of attack. In the case of tanks, a light attack involves 25 LTs, 20 MTs, or 10 HTs. A heavy attack, on the other hand, utilizes 40 LTs, 35 MTs, or 20 HTs. For carriers, an exploratory attack uses 20 SCs only (therefore, such an attack involves 2,000 personnel). An all-out attack requires 4,000 personnel and may, therefore, be carried out using $4 0 \mathrm { \thinspace 5 C s } ,$ 32 MCs, or 25 LCs.

Prior to making a decision, the system must ascertain, through its sensors, the type and number of attacking vehicles. The state space $X = \left\{ x \right\}$ contains 10 members as described in Table 1, where each member corresponds to a tuple. The first element of a tuple denotes the vehicle type and the second element denotes the number of vehicles. Also shown in the table is the probability that each of these 10 possible states will prevail in an actual battle. These probabilities are based on the knowledge of the present enemy and past experiences with ground warfare. For instance, the probability that the attack will involve 25 light tanks (defined by $x _ { 1 } )$ is 0.05.

In order to assess the type and number of vehicles in an attack, the two sensors perform certain information-gathering actions. Table 2 lists the information-gathering actions available to each sensor. We briefly examine below the impacts of such actions.

Action ${ \bf a } _ { 1 }$ indicates to sensor 1 whether the attack vehicles are tanks or carriers. Thus, by performing ${ \bf a } _ { 1 }$ , sensor 1 is able to partition X into two sets $\{ x _ { 1 } , x _ { 2 } , \ldots , x _ { 6 } \}$ and $\{ x _ { 7 } , x _ { 8 } , x _ { 9 } , x _ { 1 0 } \}$ and conclude that the true state of the attack is in one or the other of these sets. Note that the first set contains only those state-space elements that correspond to a tank attack while the second set contains the elements pertaining to a carrier attack,

All of the experimental actions function in a similar manner—when applied to $X ,$ they always partition X into two sets (i.e., produce binary partitions). Table 3 lists these partitions (see column 3). It also contains information on the cost incurred by a sensor in performing an action (see column 2). For instance, action ${ \bf a _ { 1 } }$ has an associated cost of $c ( \mathbf { a } _ { 1 } ) = 5$ . The last row of the table contains information on the cost $( \ i . { \bf e . , \ 5 } )$ associated with communication actions (denoted by the generic notation ac).2

TABLE 1  
State Space and Probabiluty Distrıbution for the Example

<table><tr><td>State, xProbability,  $\phi(x)$ </td><td> $x_{1} = \langle LT, 25 \rangle$ 0.05</td><td> $x_{2} = \langle LT, 40 \rangle$ 0.15</td><td> $x_{3} = \langle MT, 20 \rangle$ 0.05</td><td> $x_{4} = \langle MT, 35 \rangle$ 0.15</td><td> $x_{5} = \langle HT, 10 \rangle$ 0.05</td></tr><tr><td>State, xProbability,  $\phi(x)$ </td><td> $x_{6} = \langle HT, 20 \rangle$ 0.15</td><td> $x_{7} = \langle SC, 20 \rangle$ 0.05</td><td> $x_{8} = \langle SC, 40 \rangle$ 0.15</td><td> $x_{9} = \langle MC, 32 \rangle$ 0.05</td><td> $x_{10} = \langle LC, 25 \rangle$ 0.15</td></tr></table>

LT = Light Tank; MT = Medium Tank; HT = Heavy Tank.  
SC = Small Carrier; MC = Medium Carrier; LC = Large Carrier.

TABLE 2  
Action Sets for the Exumple

<table><tr><td>Actions Sets</td><td>Sensor 1:  $A_{1}^{e} = \{a_{0}, a_{1}, a_{2}, a_{3}\}$ Sensor 2:  $A_{2}^{e} = \{a_{4}, a_{5}, a_{6}, a_{7}\}$ </td></tr></table>

Given its reading of the type and number of vehicles in an attack, the system could take five types of final decisions. Table 4 depicts the gross payoffs associated with each of these decisions when the true state of the attack is described by any of the ten possible state space elements. As indicated in row 1 of the table, defense strategy 1 (associated with decision $d _ { \mathrm { 1 } } )$ is the best strategy against either type of light tank attack (with a payoff of 150 in each case) and is also a good strategy (as reflected by a payoff of 100) against an exploratory attack using small carriers. Similar interpretations may be attached to the remaining defense strategies characterized by decisions $d _ { 2 }$ through $d _ { s }$

Note that activating an inappropriate defense strategy could result in losses (as indicated by negative payoff values). In some instances $( \mathbf { e . g . }$ , taking decision $d _ { \imath }$ when the true state is $\langle H T , 2 0 \rangle )$ , the losses incurred could be quite heavy.

## 4.1. Mapping Theoretical Constructs to the Example

In our example,

$$
A _ {1} ^ {e} \cup A _ {2} ^ {e} = \left\{\mathbf {a} _ {0}, \mathbf {a} _ {1}, \mathbf {a} _ {2}, \dots , \mathbf {a} _ {7} \right\}
$$

denotes the set of $n = 8$ experimental actions available to the dual-sensor system. Since each nonnull action results in a binary partition of $X , m ( \mathbf { a } ) = 2$ and $Y _ { s }$ $= \{ 1 , 2 \}$ for any such action.

If action ${ \mathfrak { a } } _ { 1 }$ is performed,

$$
M _ {\mathbf {a} _ {1}, 1} = \left\{x _ {1}, x _ {2}, \dots , x _ {6} \right\} \quad \text { and } \quad M _ {\mathbf {a} _ {1}, 2} = \left\{x _ {7}, x _ {8}, x _ {9}, x _ {1 0} \right\}.
$$

That is, the function $\eta _ { \mathrm { a } _ { 1 } } ( \cdot )$ is such that $\eta _ { \mathbf { a } _ { 1 } } ( x _ { \iota } ) = 1 \in Y _ { \mathbf { a } _ { 1 } } = \{ 1 , 2 \}$ , for $i = 1 , 2 , \dots , 6 .$ Similarly, $\eta _ { \mathtt { a } _ { 1 } } ( x _ { 1 } ) = 2$ for $i = 7 , 8 , 9 ,$ , 10. Thus,

$$
M _ {\mathbf {a} _ {1}} = \left\{M _ {\mathbf {a} _ {1}, 1}, M _ {\mathbf {a} _ {1}, 2} \right\} = \left\{\left(x _ {1}, x _ {2}, \dots , x _ {6}\right), \left(x _ {7}, x _ {8}, x _ {9}, x _ {1 0}\right) \right\}.
$$

The information structures generated by the remaining nonnull experimental actions may be similarly interpreted.

We can illustrate the generation of $\pmb { \bigtriangledown } ^ { A }$ in the context of the example as follows. We begin the process with the state space $X = \{ x _ { 1 } , x _ { 2 } , . ~ . ~ . ~ , x _ { 1 0 } \}$ . Suppose action ${ \pmb a } _ { \imath }$ is performed first to obtain the partition $M _ { \mathbf { a } _ { 1 } }$ and then action $\mathbf { a } _ { 2 }$ is performed. From Table 3, we already know that if ${ \bf a } _ { 2 }$ were performed on X, then the impact would be a partitioning of X into two sets contained in

$$
M _ {\mathbf {a} _ {2}} = \left\{\left(x _ {1}, x _ {2}, x _ {3}, x _ {7}, x _ {8}\right), \left(\lambda_ {4}, x _ {5}, x _ {6}, x _ {9}, x _ {1 0}\right) \right\}.
$$

In generating $\pmb { \bigtriangledown } ^ { A }$ , we perform ${ \bf a } _ { 2 }$ after ${ \bf a _ { 1 } }$ has already been utilized and regardless of whether $M _ { \mathbf { a } _ { 1 } , 1 } \ \mathbf { o r } \ M _ { \mathbf { a } _ { 1 } , * }$ contains the true state.

The combined impact of performing ${ \bf a } _ { 1 }$ first, followed by ${ \bf a } _ { 2 } ,$ , is defined by the sets

TABLE 3  
Costs and Impacts of Actions for the Example

<table><tr><td>Action</td><td>Cost</td><td>Information Structure Induced on X</td></tr><tr><td> $\mathbf{a}_{1}$ </td><td>5</td><td> $\{(x_{1}, x_{2}, x_{3}, x_{4}, x_{5}, x_{6}), (x_{7}, x_{8}, x_{9}, x_{10})\}$ </td></tr><tr><td> $\mathbf{a}_{2}$ </td><td>10</td><td> $\{(x_{1}, x_{2}, x_{3}, x_{7}, x_{8}), (x_{4}, x_{5}, x_{6}, x_{9}, x_{10})\}$ </td></tr><tr><td> $\mathbf{a}_{3}$ </td><td>15</td><td> $\{(x_{3}, x_{5}, x_{6}), (x_{1}, x_{2}, x_{4}, x_{7}, x_{8}, x_{9}, x_{10})\}$ </td></tr><tr><td> $\mathbf{a}_{4}$ </td><td>5</td><td> $\{(x_{1}, x_{2}, x_{7}, x_{8}), (x_{3}, x_{4}, x_{5}, x_{6}, x_{9}, x_{10})\}$ </td></tr><tr><td> $\mathbf{a}_{5}$ </td><td>10</td><td> $\{(x_{1}, x_{3}, x_{4}, x_{5}, x_{6}, x_{7}, x_{9}, x_{10}), (x_{2}, x_{8})\}$ </td></tr><tr><td> $\mathbf{a}_{6}$ </td><td>5</td><td> $\{(x_{1}, x_{2}, x_{3}, x_{4}, x_{7}), (x_{5}, x_{6}, x_{8}, x_{9}, x_{10})\}$ </td></tr><tr><td> $\mathbf{a}_{7}$ </td><td>10</td><td> $\{(x_{1}, x_{3}, x_{5}, x_{6}, x_{7}, x_{10}), (x_{2}, x_{4}, x_{8}, x_{9})\}$ </td></tr><tr><td> $\mathbf{a}_{c}$ </td><td>5</td><td></td></tr></table>

$M _ { \mathbf { a } _ { 1 } , 1 } \cap M _ { \mathbf { a } _ { 2 } , 1 } = \left\{ x _ { 1 } , x _ { 2 } , x _ { 3 } \right\} , M _ { \boldsymbol { \alpha } _ { 1 } , 1 } \cap M _ { \mathbf { a } _ { 2 } , 2 } = \left\{ x _ { 4 } , x _ { 5 } , x _ { 6 } \right\} , M _ { \mathbf { a } _ { 1 } , 2 } \cap M _ { \mathbf { a } _ { 2 } , 1 } = \left\{ x _ { 7 } , x _ { 8 } \right\}$ and $M _ { { \bf a } _ { 1 } , 2 } \cap M _ { { \bf a } _ { 2 } , 2 } = \{ x _ { 9 } , x _ { 1 0 } \}$ . Thus, the net result is a partitioning of X into four mutually exclusive and collectively exhaustive subsets. Continuing the process, we ultimately obtain

$$
\mathbf {B} ^ {A} = \left\{\left(x _ {1}\right), \left(x _ {2}\right), \left(x _ {3}\right), \left(x _ {4}\right), \left(x _ {5}, x _ {6}\right), \left(x _ {7}\right), \left(x _ {8}\right), \left(x _ {9}\right), \left(x _ {1 0}\right) \right\}.
$$

To illustrate the use of communication actions, suppose after sensor 1 has performed ${ \bf a } _ { 1 }$ and ${ \bf a } _ { 2 } .$ , it knows that the true state is contained in some member, say B $= \{ x _ { 1 } , x _ { 2 } , x _ { 3 } \}$ , of its current partition of X. Also, suppose action ${ \bf a } _ { 5 }$ must be performed next on B by sensor 2. Sensor 1, therefore, communicates B to sensor 2, and we have $\iota ( B , \mathbf { a } _ { c } ) = \{ x _ { 1 } , x _ { 2 } , x _ { 3 } \}$

Sensor 2 then attempts to partition B further using action ${ \bf a } _ { 5 }$ while sensor 1 awaits its response. From Table 3, we have

$$
M _ {\mathbf {a} _ {5}, 1} = \left\{x _ {1}, x _ {3}, x _ {4}, x _ {5}, x _ {6}, x _ {7}, x _ {9}, x _ {1 0} \right\} \quad \text { and } \quad M _ {\mathbf {a} _ {5}, 2} = \left\{x _ {2}, x _ {8} \right\}.
$$

Let

$$
\mathbf {B} = \iota (B, \mathbf {a} _ {5}) = \left\{\left(B \cap M _ {\mathbf {a} _ {5}, 1}\right), \left(B \cap M _ {\mathbf {a} _ {5}, 2}\right) \right\} = \left\{\left(x _ {1}, x _ {3}\right), \left(x _ {2}\right) \right\} = \left\{\left(B _ {1}\right), \left(B _ {2}\right) \right\}.
$$

By definition, $\iota ( B , \mathbf { a } _ { c } )$ is trivial whereas $\iota ( B , { \bf a } _ { 5 } )$ is nontrivial. Now, consider the information structure B'induced on B by a different action, say ${ \bf a } _ { 6 }$ . From the data available in Table 3, we obtain $\mathbf { B } ^ { \prime } = \left\{ x _ { 1 } , x _ { 2 } , x _ { 3 } \right\}$ . Since

$$
\left\{x _ {1}, x _ {3} \right\} \subseteq \left\{x _ {1}, x _ {2}, x _ {3} \right\} \quad \text { and } \quad \left\{x _ {2} \right\} \subseteq \left\{x _ {1}, x _ {2}, x _ {3} \right\},
$$

we conclude that $\mathbf { B } \succcurlyeq \mathbf { B ^ { \prime } }$

TABLE 4  
Gross Payoffs for the Example

<table><tr><td></td><td> $x_1$ </td><td> $x_2$ </td><td> $x_3$ </td><td> $x_4$ </td><td> $x_5$ </td><td> $x_6$ </td><td> $x_7$ </td><td> $x_8$ </td><td> $x_9$ </td><td> $x_{10}$ </td></tr><tr><td> $d_1$ </td><td>150</td><td>150</td><td>50</td><td>25</td><td>-150</td><td>-200</td><td>100</td><td>50</td><td>-100</td><td>-110</td></tr><tr><td> $d_2$ </td><td>50</td><td>75</td><td>150</td><td>150</td><td>75</td><td>-20</td><td>-100</td><td>120</td><td>-20</td><td>-50</td></tr><tr><td> $d_3$ </td><td>-10</td><td>10</td><td>40</td><td>60</td><td>150</td><td>150</td><td>-100</td><td>-50</td><td>25</td><td>50</td></tr><tr><td> $d_4$ </td><td>50</td><td>10</td><td>-10</td><td>-20</td><td>-75</td><td>-100</td><td>150</td><td>75</td><td>50</td><td>-50</td></tr><tr><td> $d_5$ </td><td>-20</td><td>50</td><td>100</td><td>100</td><td>-60</td><td>-50</td><td>40</td><td>50</td><td>140</td><td>150</td></tr></table>

TABLE 5  
Results of the Improvema nt Heuristio

<table><tr><td></td><td>Strategy (I.1)</td></tr><tr><td>IAT</td><td> $(\mathbf{a}_{2}(\mathbf{a}_{6}(\mathbf{a}_{1}\mathbf{a}_{0})\mathbf{a}_{3}(\mathbf{a}_{0}\mathbf{a}_{1})))$ </td></tr><tr><td>TAT</td><td> $(\mathbf{a}_{2}(\mathbf{a}_{c}(\mathbf{a}_{6}(\mathbf{a}_{c}(\mathbf{a}_{1})\mathbf{a}_{c}(\mathbf{a}_{0})))\mathbf{a}_{3}(\mathbf{a}_{0}(\mathbf{a}_{4}(\mathbf{a}_{0}))\mathbf{a}_{1}(\mathbf{a}_{0}(\mathbf{a}_{0})\mathbf{a}_{0}(\mathbf{a}_{0}))))$ )</td></tr><tr><td>B5</td><td> $\{(x_{1}, x_{2}, x_{3}), (x_{7}), (x_{8}), (x_{5}, x_{5}), (x_{4}), (x_{9}, x_{10})\}$  $\Omega(\sigma) = 140\,00; \Gamma(\sigma) = 28.2\gamma; \Omega^{*}(\sigma) = 111.75$ </td></tr><tr><td></td><td>Strategy (I.2)</td></tr><tr><td>IAT</td><td> $(\mathbf{a}_{2}(\mathbf{a}_{1}(\mathbf{a}_{3}\mathbf{a}_{6})\mathbf{a}_{1}(\mathbf{a}_{3}\mathbf{a}_{0})))$ </td></tr><tr><td>TAT</td><td> $(\mathbf{a}_{2}(\mathbf{a}_{1}(\mathbf{a}_{3}(\mathbf{a}_{0}(\mathbf{a}_{0})\mathbf{a}_{0}(\mathbf{a}_{0})))\mathbf{a}_{c}(\mathbf{a}_{6}(\mathbf{a}_{c}\mathbf{a}_{c})))\mathbf{a}_{1}(\mathbf{a}_{3}(\mathbf{a}_{0}(\mathbf{a}_{0})\mathbf{a}_{0}(\mathbf{a}_{0})))\mathbf{a}_{0}(\mathbf{a}_{0}(\mathbf{a}_{0}))))$ )</td></tr><tr><td>B5</td><td> $\{(x_{1}, x_{2}), (x_{3}), (x_{7}), (x_{8}), (x_{4}) (x_{5}, x_{6}), (x_{9}, x_{10})\}$  $\Omega(\sigma) = 145.00; \Gamma(\sigma) = 27.00; \Omega^{*}(\sigma) = 118.00$ </td></tr><tr><td></td><td>Strategy (II.1)</td></tr><tr><td>IAT</td><td> $(\mathbf{a}_{1}(\mathbf{a}_{6}(\mathbf{a}_{4}\mathbf{a}_{0})\mathbf{a}_{2}(\mathbf{a}_{6}\mathbf{a}_{0})))$ </td></tr><tr><td>TAT</td><td> $(\mathbf{a}_{1}(\mathbf{a}_{c}(\mathbf{a}_{6}(\mathbf{a}_{4}(\mathbf{a}_{c}\mathbf{a}_{c})\mathbf{a}_{c}(\mathbf{a}_{0})))\mathbf{a}_{2}(\mathbf{a}_{c}|\mathbf{a}_{6}(\mathbf{a}_{c}\mathbf{a}_{c}))\mathbf{a}_{0}(\mathbf{a}_{0}(\mathbf{a}_{0}))))$ )</td></tr><tr><td>B5</td><td> $\{(x_{1}, x_{2}), (x_{3}, x_{4}), (x_{5}, x_{6}), (x_{7}), (x_{8}), (x_{9}, x_{10})\}$  $\Omega(\sigma) = 145.00; \Gamma(\sigma) = 23.00; \Omega^{*}(\sigma) = 122.00$ </td></tr><tr><td></td><td>Strategy (II.1.1)</td></tr><tr><td>IAT</td><td> $(\mathbf{a}_{1}(\mathbf{a}_{6}(\mathbf{a}_{4}\mathbf{a}_{0})\mathbf{a}_{5}(\mathbf{a}_{4}\mathbf{a}_{0})))$ </td></tr><tr><td>TAT</td><td> $(\mathbf{a}_{1}(\mathbf{a}_{c}(\mathbf{a}_{6}(\mathbf{a}_{4}(\mathbf{a}_{c}\mathbf{a}_{c})\mathbf{a}_{c}(\mathbf{a}_{0})))\mathbf{a}_{c}(\mathbf{a}_{5}(\mathbf{a}_{4}(\mathbf{a}_{c}\mathbf{a}_{c})\mathbf{a}_{c}(\mathbf{a}_{0}))))$ )</td></tr><tr><td>B5</td><td> $\{(x_{1}, x_{2}), (x_{3}, x_{4}), (x_{5}, x_{6}), (x_{7}), (x_{9}, x_{10}), (x_{8})\}$  $\Omega(\sigma) = 145.00; \Gamma(\sigma) = 25.25; \Omega^{*}(\sigma) = 119.75$ </td></tr><tr><td></td><td>Strategy (III.2)</td></tr><tr><td>IAT</td><td> $(\mathbf{a}_{3}(\mathbf{a}_{2}(\mathbf{a}_{0}\mathbf{a}_{0})\mathbf{a}_{1}(\mathbf{a}_{2}\mathbf{a}_{2})))$ </td></tr><tr><td>TAT</td><td> $(\mathbf{a}_{3}(\mathbf{a}_{2}(\mathbf{a}_{0}\mathbf{a}_{0})\mathbf{a}_{1}(\mathbf{a}_{2}\mathbf{a}_{2})))$ </td></tr><tr><td>B5</td><td> $\{(x_{3}), (x_{5}, x_{6}), (x_{1}, x_{2}), (x_{4}), x_{7}, x_{8}), (x_{9}, x_{10})\}$  $\Omega(\sigma) = 138.25; \Gamma(\sigma) = 28.75; \Omega^{*}(\sigma) = 109.50$ </td></tr></table>

To exemplify the concept of action functions, let the function $\alpha ( \cdot )$ be such that α( $B _ { \mathfrak { i } } ) = \mathbf { a } _ { 3 }$ and $\alpha ( B _ { 2 } ) = \mathbf { a } _ { 0 }$ . We then have

$$
\begin{array}{r l} \iota (B _ {1}, \alpha (B _ {1})) & = \iota (\{x _ {1}, x _ {3} \}, \mathbf {a} _ {3}) =: \{(x _ {1}), (x _ {3}) \} \\ \iota (B _ {2}, \alpha (B _ {2})) & = \iota (\{x _ {2} \}, \mathbf {a} _ {0}) = \{x _ {2} \}. \end{array} \quad \text { and }
$$

Thus,

$$
\iota (\mathbf {B}, \alpha) = \iota (B _ {1}, \alpha (B _ {1})) \cup \iota (B _ {2}, \alpha (B _ {2})) = \left\{\left(x _ {1}\right), \left(x _ {3}\right), \left(x _ {2}\right) \right\}.
$$

We now describe the components of a general ICD strategy for our example decision problem. Figure 1 depicts one such strategy for $r = 2$ and $\ell = 4$ (the relationship between r and t is explained in §5). The figure illustrates the current partitions and action functions at various stages of the process, as well as the possible final decisions taken at stage $( t + 1 ) = 5$ by sensor 1.

De · Jacob · Pakath

![](/api/attachments/F3ACTCPA/fulltext/images/952dc9135fa96ec7e91776ea3e9cd1382cb9ed4352cfbe14839a99940b278dd8.jpg)  
FIGURE 1. A General ICD Strategy for the Example.

From the figure, $\mathbf { B _ { 1 } } = \left\{ X \right\} = \left\{ x _ { 1 } , x _ { 2 } , . . . , x _ { 1 0 } \right\}$ . At stage 1, sensor 1 performs action $\alpha _ { 1 } ( \left\{ X \right\} ) = \alpha _ { 1 }$ . The result is a partitioning of $\{ X \}$ into two subsets defined by $\mathbf { B } _ { 2 }$ . During stage $^ { 2 , }$ sensor 1 communicates one of these subsets, namely $\{ x _ { 1 } , x _ { 2 } , \ldots ,$ $\scriptstyle x _ { 6 } \}$ , to sensor 2. In the next stage, sensor 2 refines this subset further. This refinement is contained in $\mathbf { B _ { 4 } }$ along with the subset $\left\{ x _ { 7 } , x _ { 8 } , x _ { 9 } , x _ { 1 0 } \right\}$ which is carried over from $\mathbf { B } _ { 2 }$ . Sensor 2 then communicates the results of its refinement back to sensor 1. Thus, at stage $( t + 1 ) = 5$ , sensor 1 has three elements $\left\{ x _ { 1 } , x _ { 3 } , x _ { 4 } , x _ { 5 } , x _ { 6 } \right\} , \left\{ x _ { 2 } \right\}$ , and $\{ x _ { \bar { \tau } }$ $x _ { 8 } , x _ { 9 } , x _ { 1 0 } \}$ in its current partition $\mathbf { B } _ { 5 }$ . Corresponding to each of these elements, sensor 1 takes a final decision, denoted by

$$
\delta \left(\left\{x _ {1}, x _ {3}, x _ {4}, x _ {5}, x _ {6} \right\}\right) = d _ {1}, \quad \delta \left(\left\{x _ {2} \right\}\right) = d _ {2}, \quad \text { and } \quad \delta \left(\left\{x _ {7}, x _ {8}, x _ {9}, x _ {1 0} \right\}\right) = d _ {3}.
$$

Note that the strategy discussed here meets the conditions for feasibility.

Let us use this feasible strategy to illustrate the concepts of predecessor sequences and action sequences. Let $q = ( t + 1 ) = 5$ . Consider an arbitrary member $B = \{ x _ { 1 } , x _ { 3 }$ $\displaystyle x _ { 4 } , x _ { 5 } , x _ { 6 } \}$ of ${ \bf { B } } _ { 5 }$ . The $( q - 1 ) = 4$ predecessors of B are defined by the sequence

$$
\begin{array}{r l} \left\langle \mathbf {B} _ {1} (B), \mathbf {B} _ {2} (B), \mathbf {B} _ {3} (B), \mathbf {B} _ {4} (B) \right\rangle & \\ = \left\langle \{X \}, \{x _ {1}, x _ {2}, \dots , x _ {6} \}, \{x _ {1}, x _ {2}, \dots , x _ {6} \}, \{x _ {1}, x _ {3}, \dots , x _ {6} \} \right\rangle . \end{array}
$$

B is clearly a subset of any of these predecessors. Also, the action sequence along the path to B is defined by

$$
\begin{array}{r l} \left\langle \mathbf {a} _ {1} (B), \mathbf {a} _ {2} (B), \mathbf {a} _ {3} (B), \mathbf {a} _ {4} (B) \right\rangle & = \left\langle \alpha_ {1} [ \mathbf {B} _ {1} (B) ], \alpha_ {2} [ \mathbf {B} _ {2} (B) ], \alpha_ {3} [ \mathbf {B} _ {3} (B) ], \alpha_ {4} [ \mathbf {B} _ {4} (B) ] \right\rangle \\ & = \left\langle \mathbf {a} _ {1}, \mathbf {a} _ {c}, \mathbf {a} _ {5}, \mathbf {a} _ {c} \right\rangle . \end{array}
$$

Using the data in Table 3, we obtain

$$
C (B) = c [ \mathbf {a} _ {1} (B) ] + c [ \mathbf {a} _ {2} (B) ] + c [ \mathbf {a} _ {3} (B) ] + c [ \mathbf {a} _ {4} (B) ] = 2 5.
$$

From Table 2, we also have

$$
\pi (B) = \{\phi (x _ {1}) + \phi (x _ {3}) + \phi (x _ {4}) + \phi (x _ {5}) + \phi (x _ {6}) \} = 0. 4 5.
$$

Proceeding in a similar manner, we have $C ( \{ \ : x _ { : } \} ) = 2 5 , \pi ( \{ \ : x _ { 2 } \} ) = 0 . 1 5 , C ( \{ \ : x _ { 7 } , x _ { 8 } .$ $x _ { 9 } , x _ { 1 0 } \dag ) = 5$ , and $\pi ( \mathrm { ~ ; ~ } x _ { I } , x _ { 8 } , x _ { 9 } , x _ { 1 0 } \mathrm { ~ \ ; ~ } ) = 0 . 4 0$ . Thus, $\Gamma ( \sigma ) = 1 7 .$

To compute the expected gross payoff, recall that the function $\delta ( \cdot )$ generates the following mappings:

$$
\delta \left(\left\{x _ {1}, x _ {3}, x _ {4}, x _ {5}, x _ {6} \right\}\right) = d _ {1}, \quad \delta \left(\left\{x _ {2} \right\}\right) = d _ {2}. \quad \text { and } \quad \delta \left(\left\{x _ {7}, x _ {8}, x _ {9}, x _ {1 0} \right\}\right) = d _ {3}.
$$

Using these mappings along with the gross payoff data contained in Table 4, we obtain

$$
\begin{array}{r l} \Omega (\sigma) = & \left\{\left[ (1 5 0 * 0. 0 5) + (5 0 * 0. 0 5) + (2 5 * 0. 1 5) + (- 1 5 0 * 0. 0 5) + (- 2 0 0 * 0. 1 5) \right] \right. \\ & \left. + [ 7 5 * 0. 1 5 ] + [ (- 1 0 0 * 0. 0 5) + (- 5 0 * 0. 1 5) + (2 5 * 0. 0 5) + (5 0 * 0. 1 5) ] \right\} \end{array}\tag{\(= -16.25.\}
$$

Consequently, the expected net payoff of our strategy is

$$
\Omega^ {*} (\sigma) = \Omega (\sigma) - \Gamma (\sigma) = - 1 6. 2 5 - 1 7 = - 3 3. 2 5.
$$

We next illustrate the computation of $\nu ( B ) , I ) ^ { * } ( B )$ , and $X _ { d }$ . Consider a member B $= \left\{ . \Upsilon _ { 5 } , . \Upsilon _ { 6 } \right\}$ of $\mathbf { B } ^ { A }$ . For this element,

$$
\begin{array}{r l} v (B) = \max \left\{\left[ (- 1 5 0 * 0. 0 5) + (- 2 0 0 * 0. 1 5) \right] / 0. 2 0, \right. \\ & \left. [ (7 5 * 0. 0 5) + (- 2 0 * 0. 1 5) ] / 0. 2 0, \left[ (1 5 0 * 0. 0 5) + (1 5 0 * 0. 1 5) \right] / 0. 2 0, \right. \\ & \left. [ (- 7 5 * 0. 0 5) + (- 1 0 0 * 0. 1 5) ] / 0. 2 0, \left[ (- 6 0 * 0. 0 5) + (- 5 0 * 0. 1 5) \right] / 0. 2 0 \right\} \end{array}\tag{= 150.}
$$

Based on this information, we obtain $D ^ { * } ( B ) = d _ { 3 }$ . Proceeding in a similar fashion, we generate the following conditionally optimal decision sets for the remaining members of ${ \bf B } ^ { A } \colon D ^ { * } ( x _ { 1 } ) = d _ { 1 } , D ^ { * } ( x _ { 2 } ) = d _ { 1 } , D ^ { * } ( x _ { 3 } ) = d _ { 2 } , D ^ { * } ( x _ { 4 } ) = d _ { 2 } , D ^ { * } ( x _ { 7 } ) = d _ { 4 }$ $D ^ { * } ( x _ { 8 } ) = d _ { 2 } , D ^ { * } ( x _ { 9 } ) = d _ { 5 }$ , and $D ^ { * } ( x _ { 1 0 } ) = d _ { 5 }$ . Consequently, $\mathbf { B } ^ { A } ( d _ { 1 } ) = \left\{ ( x _ { 1 } ) , ( x _ { 2 } ) \right\}$ $\mathbf { B } ^ { A } ( d _ { 2 } ) = \{ ( x _ { 3 } ) , ( x _ { 4 } ) , ( x _ { 8 } ) \} , \mathbf { B } ^ { A } ( d _ { 3 } ) = \{ ( x _ { 5 } , x _ { 6 } ) , \mathbf { B } ^ { A } ( d _ { 4 } ) = \{  x _ { 7 } \} , \mathbf { B } ^ { A } ( d _ { 5 } ) = \{ ( x _ { 9 } ) ,  \mathbf { B } ^ { A } ( d _ { 8 } ) \} , \mathbf { B } ^ { A } ( d _ { 1 0 } ) = \{ ( x _ { 1 } , x _ { 7 } ) , \mathbf { B } ^ { A } ( d _ { 1 0 } ) = \{ ( x _ { 1 } , x _ { 7 } ) , \mathbf { B } ^ { A } ( d _ { 1 1 } ) = \{ ( x _ { 1 } , x _ { 7 } ) , \mathbf { B } ^ { A } ( d _ { 2 2 } ) = \{ ( x _ { 2 } , x _ { 8 } ) , \mathbf { B } ^ { A } ( d _ { 1 2 } ) = \{ ( x _ { 2 } , x _ { 7 } ) , \mathbf { B } ^ { A } ( d _ { 2 2 } ) = \{ ( x _ { 2 } , x _ { 7 } ) , \mathbf { B } ^ { A } ( d _ { 2 2 } ) = \{ ( x _ { 2 } , x _ { 7 } ) , \mathbf { B } ^ { A } ( d _ { 3 } ) = \{ \{ ( x _ { 3 } , x _ { 7 } ) , \mathbf { B } ^ { A } ( d _ { 4 } ) =  ( x _ { 2 } , x _ { 7 } ) , \mathbf { B } ^ { A } ( d _ { 4 } ) = \{ ( x _ { 2 } , x _ { 7 } ) , \mathbf { B } ^ { A } ( d _ { 4 } ) = \{ ( x _ { 3 } , x _ { 7 } ) , \mathbf { B } ^ { A } ( d _ { 4 } ) = \{ ( x _ { 2 } , x _ { 7 } ) , \mathbf { B } ^ { A } ( d _ { 4 } ) = \{ ($ $\left( \boldsymbol { \it x } _ { 1 0 } \right) \Bigg \}$ We, thus, have $X _ { d _ { 1 } } = \left\{ \ x _ { 1 } , x _ { 2 } \right\} , X _ { d _ { 2 } } = \left\{ \ x _ { 3 } , x _ { 4 } , x _ { 8 } \right\} , X _ { d _ { 3 } } = \left\{ \ x _ { 5 } , x _ { 6 } \right\} , X _ { d _ { 4 } } = \left\{ \ x _ { 7 } \right\}$ and $X _ { d _ { 4 } } = \lbrace x _ { 9 } , x _ { 1 0 } \rbrace$

Finally, let us examine whether our feasible ICD strategy is also efficient. The strategy meets condition 1 for efficiency since all of the nonnull experimental actions used by the strategy $( \operatorname { i . e . , a } _ { 1 } \operatorname { a n d } \mathbf { a } _ { s } )$ produce binary partitions. The strategy also meets condition 2 since the only stages where we encounter a $B \in { \bf B } ,$ such that $B \subseteq X _ { d } .$ are stages 4 and 5. In both cases, we have $B = \{  x _ { 2 } \} \subseteq x _ { d _ { 1 } } = \{  x _ { 1 } , \tilde { x _ { 2 } } \}$ . At stage 4, sensor 2 communicates $\left\{ x _ { 2 } \right\}$ to sensor 1; on receipt, sensor 1 makes a final decision on $\left\{ x _ { 2 } \right\}$ at stage 5. In neither case, is there any attempt (nor is it possible) to obtain further, nontrivial refinements of B. Turning to condition 3, it is straightforward to verify that

$$
D ^ {*} \left(\left\{x _ {1}, x _ {3}, \dots , x _ {6} \right\}\right) = d _ {3}, \quad D ^ {*} \left(\left\{x _ {2} \right\}\right) = d _ {1} \quad \text { and } \quad D ^ {*} \left(\left\{x _ {7}, x _ {8}, x _ {9}, x _ {1 0} \right\}\right) = d _ {5}.
$$

In our strategy, however

$$
\delta \left(\left\{x _ {1}, x _ {3}, x _ {4}, x _ {5}, x _ {6} \right\}\right) = d _ {1}, \quad \delta \left(\left\{x _ {2} \right\}\right) = d _ {2}, \quad \text { and } \quad \delta \left(\left\{x _ {7}, x _ {8}, x _ {9}, x _ {1 0} \right\}\right) = d _ {3}.
$$

Thus, the strategy violates condition 3. Lastly, at stage 2,

$$
\alpha_ {2} \left(\left\{x _ {7}, x _ {8}, x _ {9}, x _ {1 0} \right\}\right) = \mathbf {a} _ {0}.
$$

Subsequently, at stages 3 and 4,

$$
\alpha_ {3} \left(\left\{x _ {7}, x _ {8}, x _ {9}, x _ {1 0} \right\}\right) = \alpha_ {4} \left(x _ {7}, x _ {8}, x _ {9}, x _ {1 0} \right\}) = \mathbf {a} _ {0}
$$

as well. Thus, condition 4 is satisfied. However, because it violates condition 3, the example ICD strategy is not an efficient strategy.

## 5.0. Algorithms for Generating Efficient Strategies

If the r information-gathering actions and their sequence in a strategy are completely known, one can (as discussed shortly) easily determine the communication actions for the strategy. Thus, any feasible strategy can be represented in terms of its information-gathering actions alone. We may view the strategy as a tree having $( r + 1 )$ levels, 1 through $( r + 1 )$ , with the root at level 1. Any node at level $j \left( \leq r \right)$ is associated with two entities—a member of the current partition $B \in \mathbf { B } ,$ and an action $\alpha _ { \jmath } ( B ) = \mathbf { a }$ performed on that member (see Figure 2). The branches emanating from the node correspond to the partitioning of B by a. A leaf node $( \mathrm { i . e . }$ , for which $j = r$ $+ \nobreakspace 1 )$ is associated only with the appropriate B, but with no action. This is because no information-gathering action is performed at that level; the leaves simply represent the members of the partition generated by the last (or the rth) information-gathering action.

![](/api/attachments/F3ACTCPA/fulltext/images/bfb4eb8dbb7d8df89d12586b6e9fac7dc56579ab24944c6b99763f0064685663.jpg)  
FIGURE 2. An Example Tree Structure.

It follows from the above description that although the tree has $( r + 1 )$ levels, the information-gathering actions alone constitute a smaller tree with r levels, 1 through r; we call it the information-gathering action tree (IAT). Evidently, if at most m branches can emanate from a node, the total number of possible paths (from the root to the leaves) in the IAT will not exceed $m ^ { r - 1 }$ . We assume that r is chosen such that $m ^ { r - 1 }$ remains computationally tractable. In many practical situations, this is not an unrealistic assumption. For example, in medical diagnosis, r could be the number of different and successive tests undertaken before a final decision concerning a patient's ailment is made. This number would seldom exceed 10 or so. Also note that whatever be the values of m and r, the total number of paths can never exceed the cardinality of the state space X. This is because each partition at the rth (or any other) level must contain at least one element.

The addition of the appropriate communication actions—and possibly some null actions, as we discuss below—to the IAT generates what we refer to as the total action tree (TAT). This is accomplished as follows: If the action taken at the root of the IAT belongs to $\boldsymbol { A } _ { 2 } ^ { e }$ , then we add a communication action prior to that action (i.e., the communication action now becomes the first action undertaken). This is because, by assumption 3, problem solving always begins with processor 1; only if this processor communicates to processor 2, asking for help, can the latter work on the problem. For any other action along a path in the IAT, we check if this action and its immediate predecessor belong to the action set of the same processor. If not, a communication action is added just prior to the action under consideration. Finally, if the last nonnull action taken on a path belongs to $A _ { 2 } ^ { e }$ . we add a communication action to every member of the partition generated by this action. This ensures that processor 1 takes the final decision. After all the communication actions are added in this manner, we check if all leaf nodes in the resultant tree are at the same level. If not, null actions are appended at the end of the shorter paths until all paths are of the same length. This completes the conversion of the lAT to its corresponding TAT.

Note that the TAT has / (≥r) levels whereas the IAT has only r levels. If a strategy does not call for processor 2 to acquire any information, then there is no need for any communication between the two processors. In this event, $t = r$ and the TAT and the IAT are identical. Also note that by associating a final decision with each of the leaves of the TAT, we can obtain a complete ICD strategy specification like the one shown in Figure 1.

For representational convenience, in the rest of this paper, we describe a tree structure as a list of nodes where the children of a node appear immediately after the node within some delimiters such as parentheses. For example, the tree in Figure 2 is described as follows:

$$
(A (B (D (H I) E (J K)) C (F (L M) G (N))).
$$

Obviously, the same scheme can also be used to describe an IAT or a TAT. In that case, of the two entities B and a associated with a node, we focus on the latter and describe the tree simply as a list of actions. Thus, the IAT for Figure 2 is represented as

$$
\left(\mathbf {a} _ {1} \left(\mathbf {a} _ {2} \left(\mathbf {a} _ {3} \mathbf {a} _ {3}\right) \mathbf {a} _ {2} \left(\mathbf {a} _ {6} \mathbf {a} _ {0}\right)\right)\right).
$$

June 1993

If we assume that the action sets of the two processors are as shown in Table 2, one can easily verify that the TAT corresponding to Figure 2 is

$$
\left(\mathbf {a} _ {1} \left(\mathbf {a} _ {2} \left(\mathbf {a} _ {3} \left(\mathbf {a} _ {0} \left(\mathbf {a} _ {0}\right)\right) \mathbf {a} _ {3} \left(\mathbf {a} _ {0} \left(\mathbf {a} _ {0}\right)\right)\right) \mathbf {a} _ {2} \left(\mathbf {a} _ {c} \left(\mathbf {a} _ {6} \left(\mathbf {a} _ {c} \mathbf {a} _ {c}\right)\right) \mathbf {a} _ {0} \left(\mathbf {a} _ {0} \left(\mathbf {a} _ {0}\right)\right)\right)\right)\right).
$$

Our procedure to generate a suitable strategy consists of an initial phase, followed by an optional improvement phase. In the initial phase, we generate a predetermined number of strategies using a greedy heuristic. If we decide not to go through the improvement phase, we select the best of these strategies in terms of the expected net payoff. The improvement phase, if undertaken, begins with the strategies generated at the initial phase, and attempts to develop better strategies from them in an iterative manner. As will be evident from the description of the algorithms in §§5.1 and 5.2, both phases conform to the requirements of an efficient strategy (see §3.2). Our objective is to generate an efficient strategy, striving for the highest net payoff we can obtain while keeping the process computationally tractable.

In both phases of our procedure, we only consider IATs. As we have already noted, one can easily generate the TAT and, hence, the complete ICD strategy once the IAT is determined. We must, however, take appropriate communication costs into consideration while evaluating the effectiveness of an information-gathering action at any node of the IAT.

## 5.1. Initial Phase

As mentioned above, the initial phase utilizes a greedy heuristic. While deciding which action to take at a particular node, the heuristic assumes that only one more action can be taken; thus, the choice is made without any consideration of the nodes that might follow. Given this assumption, the heuristic takes the best conditional action at each node, except possibly at the root. In doing so, it considers only those actions that have not already been used on the path from the root to the immediate predecessor of the node under consideration. The action taken at the root could be the ith best action, $i \leq Q \leq n$ , where Q is the number of strategies we wish to generate in the initial phase and n is the total number of information-gathering actions available.

Step 1: i ← 1.

Step 2: For the root, select, out of the n available actions, the one which provides the ith highest expected net payoff, assuming that no other action would be performed later (i.e., assuming r to be 1)

Step 3: Do the following successively for each $B \in { \bf B } , j = 2$ to $r { : }$ Check: (i) if the action associated with the immediate predecessor of B is the null action or (ii) if B $\subseteq X _ { d }$ . If so, then take the null action; else, check if, among the actions which have not yet been used on the path from the root to the immediate predecessor of B, there is any action a such that an improvement in the current expected net payoff is realized when a is performed at B, assuming that no other action would be performed later; if so, then select, among all such actions, the one which produces the highest improvement in the expected net payoff; else, take the null action.

Step $4 ; i  i + 1 . \mathbf { I f } i \leq Q$ , then go to step 2; else, stop.

While evaluating an action, communication costs are taken into consideration whenever appropriate. We note that if during a communication, processor 1 transmits some $B \in \mathbf { B } _ { \iota } , j = 1 , \ldots , ( r - 1 )$ , to processor 2, then regardless of how B is partitioned by the latter, the union of the partition members, each of which is eventually communicated back to processor 1, will equal B. Thus, the total cost of the to-and-fro communication will be twice the cost of communicating B from one processor to the other. Therefore, we adopt the following procedure: In step 2, if the action being evaluated belongs to $A _ { 2 } ^ { e } ,$ twice the cost of communicating the original state space X is added to the cost of this action. Similarly, in step 3, if the action under consideration belongs to $\pmb { A } _ { 2 } ^ { e }$ while its immediate predecessor belongs to $\boldsymbol { A } _ { 1 } ^ { e }$ , twice the cost of communicating the appropriate segment of the state space is added to the cost of this action. Note that this scheme is deemed appropriate only because the objective of the heuristic is to select the conditionally best action at each node of a path, assuming that no other action would be taken later, i.e., at any stage, we are concerned only with the selection of one more action and do not look ahead further into the future.

Observe that the first strategy produced by the greedy heuristic will have the best conditional action at the first level, the second strategy will have the second best conditional action at the first level, and so on. At all other levels in any strategy, we choose the best conditional action out of the remaining actions. We vary the action choice at the first level, rather than at any other level, to allow for a large variation among the selected strategies.

As shown in Appendix A, the worst-case time complexity of the greedy heuristic is $O ( Q n m ^ { r - 1 } )$ , where O stands for the order function commonly used to describe the complexity of an algorithm (see, for example, Aho and Ullman (1992)). Thus, given our assumption about $r ,$ viz, r is chosen in such a way that $m ^ { r - 1 }$ remains computationally tractable (see §5.0), this heuristic can always be executed within a reasonable amount of time.

5.1.1. An Example We now illustrate the use of the greedy heuristic in terms of the example problem discussed in $\ S 4$ . We assume that $Q = r = 3 .$

Beginning with $\{ X \} .$ , if we were to make a decision after performing only one information-gathering action, the best action that we could perform would be ${ \bf a } _ { 2 }$ Hence, the heuristic selects ${ \bf a } _ { 2 }$ as the action at the root. From Table 3 and the expression for $\Omega ^ { * } ( \sigma )$ , the expected net payoff of this choice is 82.75 and the resulting information structure is

$$
\mathbf {B} _ {2} = \left\{\left(x _ {1}, x _ {2}, x _ {3}, x _ {7}, x _ {8}\right), \left(x _ {4}, x _ {5}, x _ {6}, x _ {9}, x _ {1 0}\right) \right\}.
$$

We next determine the best action corresponding to each member of $\mathbf { B } _ { 2 }$ . For B $= \left\{ x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 7 } , x _ { 8 } \right\}$ , if the null action were pursued, then the best decision would be $d _ { 1 }$ , with an expected net payoff of 100. If action ${ \bf a } _ { 1 }$ were pursued instead, we would partition B as $\{ \begin{array} { r l } \end{array}  \boldsymbol { x _ { 1 } } , \boldsymbol { x _ { 2 } } , \boldsymbol { x _ { 3 } } \}$ and, $\left\{ \right. x _ { 7 } , \left. x _ { 8 } \right\}$ with associated decisions $d _ { \imath }$ and $d _ { 4 }$ respectively. This would result in an expected net payoff of 108.88. Similarly, one can compute the expected net payoff generated as a result of taking any other available action on $B$ . Then, the action which provides the highest net payoff is selected for B. The process is repeated for the second member of $\mathbf { B } _ { 2 }$ , namely, $\left\{ { { x } _ { 4 } } , { { x } _ { 5 } } , { { x } _ { 6 } } , { { x } _ { 9 } } , { { x } _ { 1 0 } } \right\}$ . Proceeding in this manner the heuristic generates the following IAT, from which the TAT shown below is obtained:

$$
\begin{array}{l} \mathrm{IAT} = (\mathbf {a} _ {2} (\mathbf {a} _ {1} (\mathbf {a} _ {3} \mathbf {a} _ {6}) \mathbf {a} _ {3} (\mathbf {a} _ {0} \mathbf {a} _ {1}))), \\ \mathrm{TAT} = (\mathbf {a} _ {2} (\mathbf {a} _ {1} (\mathbf {a} _ {3} (\mathbf {a} _ {0} (\mathbf {a} _ {0}) \mathbf {a} _ {0} (\mathbf {a} _ {0})) \mathbf {a} _ {c} (\mathbf {a} _ {6} (\mathbf {a} _ {c} \mathbf {a} _ {c}))) \mathbf {a} _ {3} (\mathbf {a} _ {0} (\mathbf {a} _ {0} (\mathbf {a} _ {0})) \mathbf {a} _ {1} (\mathbf {a} _ {0} (\mathbf {a} _ {0}) \mathbf {a} _ {0} (\mathbf {a} _ {0})))). \end{array}
$$

This strategy, which we will call strategy (I), results in the final information structure

$$
\mathbf {B} _ {5} = \left\{\left(x _ {1}, x _ {2}\right), \left(x _ {3}\right), \left(x _ {7}\right), \left(x _ {8}\right), \left(x _ {5}, x _ {6}\right), \left(x _ {4}\right), \left(x _ {9}, x _ {1 0}\right) \right\}\tag{I}
$$

The expected gross payoff of the strategy is 145 at an expected cost of 29, resulting in an expected net payoff of 116.

Strategies (II) and (III) are created similarly, with the second and third best actions at the root, respectively. The action trees and final information structures corresponding to these two strategies are as follows:

$$
\begin{array}{r l} & \mathrm{IAT} = (\mathbf {a} _ {1} (\mathbf {a} _ {2} (\mathbf {a} _ {3} \mathbf {a} _ {3}) \mathbf {a} _ {2} (\mathbf {a} _ {6} \mathbf {a} _ {0}))), \\ & \mathrm{TAT} = (\mathbf {a} _ {1} (\mathbf {a} _ {2} (\mathbf {a} _ {3} (\mathbf {a} _ {0} (\mathbf {a} _ {0}) \mathbf {a} _ {0} (\mathbf {a} _ {0})) \mathbf {a} _ {3} (\mathbf {a} _ {0} (\mathbf {a} _ {0}) \mathbf {a} _ {0} (\mathbf {a} _ {0}))) \mathbf {a} _ {2} (\mathbf {a} _ {c} (\mathbf {a} _ {6} (\mathbf {a} _ {c} \mathbf {a} _ {c})) \mathbf {a} _ {0} (\mathbf {a} _ {0} (\mathbf {a} _ {0}))))), \\ & \quad \mathbf {B} _ {5} = \{(x _ {1}, x _ {2}), (x _ {3}), (x _ {4}), (x _ {5}, x _ {6}), (x _ {7}), (x _ {8}), (x _ {9}, x _ {1 0}) \}. \end{array} \tag {II}
$$

In this case, the expected gross payoff is 145, the expected cost is 27, and hence the expected net pavoff is 118.

$$
\begin{array}{l} \mathrm{IAT} = (\mathbf {a} _ {3} (\mathbf {a} _ {2} (\mathbf {a} _ {0} \mathbf {a} _ {0}) \mathbf {a} _ {2} (\mathbf {a} _ {6} \mathbf {a} _ {1}))), \\ \mathrm{TAT} = (\mathbf {a} _ {3} (\mathbf {a} _ {2} (\mathbf {a} _ {0} (\mathbf {a} _ {0} (\mathbf {a} _ {0})) \mathbf {a} _ {0} (\mathbf {a} _ {0} (\mathbf {a} _ {0}))) \mathbf {a} _ {2} (\mathbf {a} _ {c} (\mathbf {a} _ {6} (\mathbf {a} _ {c} \mathbf {a} _ {c})) \mathbf {a} _ {1} (\mathbf {a} _ {0} (\mathbf {a} _ {0}) \mathbf {a} _ {0} (\mathbf {a} _ {0}))))), \\ \mathbf {B} _ {5} = \{(x _ {3}), (x _ {5}, x _ {6}), (x _ {1}, x _ {2}, x _ {7}), (x _ {8}), (x _ {4}), (x _ {9}, x _ {1 0}) \}. \end{array}\tag{III}
$$

In this case, the expected gross payoff, expected cost, and expected net payoff are 142.5, 32.75, and 109.75, respectively.

Note that starting with the second best action at the root results in a higher expected net payoff than starting with the best. This illustrates the need to provide as much variability as possible in selecting the action at the root while making up a strategy.

If a single processor were used to solve the problem, the expected net payoff would be less. It is straightforward to verify that the maximum expected net payoff generated by the heuristic would be 114.25 (113.50) in case sensor 1 (sensor 2) was used alone, as opposed to 118, the best value obtained by utilizing the capabilities of both processors. Clearly, the difference in payoffs between the single-processor and dualprocessor frameworks could be significantly larger in other problem instances.

## 5.2. Improvement Phase

The objective of this phase is to improve upon the quality of the solution delivered by the initial phase. A decision on whether the improvement phase should be undertaken would typically depend on the available computing resources, in particular CPU time.

We start with the Q strategies generated in the initial phase. Recall that in these strategies, the best conditional action has been employed at every node, except at the root where the ith best conditional action has been taken, $1 \leq i \leq Q$ . The improvement heuristic tentatively replaces the original action at each node $B \in { \bf B } _ { \prime } , j \geq 2$ , by the second-best conditional action for B. In case this change of action at any node improves the expected net payoff (of the entire strategy), the original strategy is discarded in favor of the new strategy. Note that for any node at the rth level, replacing the original (or best) action by the second best will not improve the expected net payoff as no further action can be taken after this level. Thus, the process starts at j $\ c = 2$ and continues through $j = ( r - 1 )$ , unless a predefined condition for early termination, to be described shortly, is fulfilled. Each of the Q strategies that remain at the end has either the best or the second-best conditional action taken at each node, except at the root where the action remains the same as in the greedy heuristic. Thus, the improvement phase attempts to improve upon the solution generated in the initial phase by doubling the flexibility in the choice of actions for each node other than the root. Note that by considering O different action choices, $1 \leq Q \leq n$ , we have already allowed the root a considerable amount of flexibility in the initial phase.

When an action at a node $B \in \mathbf { B } _ { \iota }$ is replaced by another action, a different set of signals may be generated, altering the number (and contents) of partition members at the next level. This would call for a complete reconfiguration of the subtree emanating from B (i.e., the one whose root is at B) after each replacement.

Typically, one would like to continue the above process from $j \approx 2$ through $j = ( r$ $- \ 1 \ )$ . However, we may choose to terminate the process early in case no improvement in expected net payoff is realized over a predetermined number of consecutive levels in the tree. The rationale for such early termination is that action changes made at higher levels in the tree are more likely to cause changes in the expected net payoff than changes made at lower levels.

Let Old-Best and New-Best stand, respectively, for the best expected net payoffs available from the original set of Q strategies which we have before processing the nodes at a certain level  and from the new set of $Q$ strategies after these nodes are processed. Similarly, let Old-Avg and New-Avg represent the average net payoffs of the Q strategies in the old set and the new set, respectively. In case there is no improvement in the best payoff (i.e., if New-Best ≤ Old-Best) or the average payoff (i.e., if $\mathbf { N e w { \mathbf { - } } A v g } \leq \mathbf { O l d { \mathbf { - } } A v g } )$ over a certain number of consecutive levels, we terminate the process before reaching $j = ( r \cdots 1 )$ . Let $k _ { \operatorname* { m a x } } ( < ( r \textrm { -- } 1 ) )$ be the maximum number of consecutive levels allowed if the best payoff does not improve but the average payoff does. and $l _ { \operatorname* { m a x } { } } \left( < k _ { \operatorname* { m a x } { } } \right)$ be the maximum number of consecutive levels allowed if neither the best nor the average improves.

In the following description of the heuristic, $t ^ { \tau } ,$ initially represents the ith strategy generated by the greedy heuristic and $\Omega ^ { * } ( \sigma _ { \iota } )$ the corresponding expected net payoff, $1 \leq i \leq Q$

Step $1 ; j  2 , k  1 , l  1$

Step 2: i ← 1.

Step $3 \colon \sigma \gets \sigma _ { \iota } , \Omega ^ { * } ( \sigma ) \gets \Omega ^ { * } ( \sigma _ { \iota } )$

Step 4: Do the following successively for each $B \in \mathbf { B } ,$

(a) Let a and $\mathbf { a ^ { \prime } }$ denote, respectively, the best and second-best conditional actions for B. Check: (i) if $B \subseteq X _ { d } o r ( \mathrm { i i } ) \mathrm { i f } , \forall B ^ { \prime } \in \iota ( B , \mathbf { a } ) , B ^ { \prime } \subseteq X _ { d }$ . If so, then stop processing B and repeat step 4 for the next node at level $\boldsymbol { \jmath } ;$ else, replace a by $\mathbf { a } ^ { \prime }$ at B. Check if $\iota ( B , \mathbf { a } ) = \iota ( B , \mathbf { a } ^ { \prime } )$ . If so, then reassign action a at $B$ , stop processing B. and repeat step 4 for the next node at level $j ;$ else, continue.

(b) Check if the new action taken at $B \left( \mathrm { i } , \mathrm { e } _ { \cdot \cdot } , \mathrm { } \mathbf { a } ^ { \prime } \right)$ is the null action. If so, then repeat the null action at every subsequent level on the path from $B ;$ else, reconfigure the entire subtree emanatıng from B by taking the best conditional actions at all subsequent levels. Let ${ \pmb { \sigma } } ^ { \prime }$ be the new strategy geneiated and $\Omega ^ { * } ( \sigma ^ { \prime } )$ the corresponding expected net payoff.

(c) If $\Omega ^ { * } ( \sigma ^ { \prime } ) < \Omega ^ { * } ( \sigma )$ , then $\sigma \gets \sigma ^ { \prime } , \Omega ^ { * } ( \sigma ) \gets \Omega ^ { * } ( \sigma ^ { \prime } )$

Step 5: $\sigma _ { i } \gets \sigma , \ : \Omega ^ { * } ( \sigma _ { i } ) \gets \Omega ^ { * } ( \sigma ) . \ : i \gets i + 1 . \ : \mathrm { I f } \ : i \le Q$ , then go to step 3.

Step 6: Perform the following routine which serves as a stopping rule:

(a) $j \gets j + 1$

(b) If New-Best > Old-Best, then $k  1 , l  1 ;$ ; else, ${ \mathrm { i f ~ N e w { \mathrm { - } } A v g } } > \mathbf { O l d { \mathrm { - } } A v g }$ , then $k  k + 1 , l  1 ; { \mathrm { e l s e , ~ } } k  k + 1 , l  l + 1$

(c) $\mathbf { I f } \ j > ( r - 1 )$ or $k > k _ { \operatorname* { m a x } }$ or $l > l _ { \mathrm { m a x } }$ , then select, out of the Q strategies that remain under consideration, the one with the highest expected net payoff, and stop; else go to step 2.

Note that while computing the expected net payoff of a strategy, we must take the appropriate communication costs into account. This is accomplished following the same scheme which we have adopted for the greedy heuristic (see §5.1).

As shown in Appendix B, the worst-case time complexity of the above procedure is $O ( Q n r m ^ { r - 2 } )$ . Given our assumption that $m ^ { r - 1 }$ is chosen to be computationally tractable $( \mathsf { s e e } \ S 5 . 0 )$ , we conclude that, like the greedy heuristic, the improvement heuristic is also computationally efficient.

5.2.1. An Example.To illustrate the improvement phase, let us consider the three strategies generated in $\ S 5 . 1 . 2$ . Given $r = 3$ and the fact that the refinement process continues from $j = 2$ through $j = ( r - 1 )$ , the maximum number of changes we need to consider along any given path is $( r - 2 ) = 1$ . Thus, for each of the three strategies available, we successively replace every action at the second level of the IAT by the second-best choice. We make the replacement permanent only if there is an improvement in the expected net payoff. Finally, we select the best out of the three remaining strategies.

Let us first consider strategy (I). To start with, the first (or leftmost) action at level 2 of the IAT for (I), $\mathbf { v i z } . , \mathbf { a } _ { 1 }$ is replaced by ${ \bf { a } } _ { 6 } ,$ , resulting in a new strategy (I.1). The action trees, final information structure, and net payoff for (I.1) (as well as for other new strategies developed during the improvement phase) are shown in Table 5. Since (I.1) has a lower expected net payoff than (I), it is discarded and (I) is retained for further evaluation. Next, the second action at level 2, viz., ${ \bf a } _ { 3 }$ is replaced by ${ \bf a } _ { 1 }$ and a new strategy (I.2) is formed. Since (I.2) has a higher net payoff than (I), it is retained in lieu of the latter.

For strategy (II), the first action at level 2, viz., $\mathbf { a } _ { 2 }$ is replaced by ${ \bf a } _ { 6 }$ , giving rise to strategy (II.1). This new strategy has a higher net payoff than (II); consequently, it replaces (II). Next, the second action at level 2 for (II.1), which is also ${ \bf a } _ { 2 } ,$ is replaced by ${ \bf a } _ { 5 }$ , generating yet another strategy (II.1.1). This strategy is discarded, however, since it has a lower net payoff than (II.1)

For strategy (III), the first action at level 2, viz., ${ \bf a } _ { 2 }$ is not replaced since condition (ii) in part (a) of step 4 of the improvement heuristic is satisfied. A new strategy (III.2) is, however, generated by replacing the second action at level 2, which is ${ \bf a } _ { 2 }$ as well, with ${ \bf a } _ { 1 }$ . Since (III.2) yields a lower net payoff than (III), the latter prevails.

Thus, at the end of the first iteration, strategies (I.2), (II.1), and (III) remain under consideration. As explained above, we terminate our search at this point and select strategy (II.1) since, among the three alternatives, it produces the highest expected net payoff, namely, 122. If r had been greater than 3, we would continue by changing the actions at the next higher level of (I.2), (II.1), and (III),

As in the initial phase, the expected net payoff would be less in the improvement phase, too, if a single processor were used. Actually, the best value of the expected net payoff produced by the two phases in tandem would be 115 (113.75) in case sensor 1 (sensor 2) was used alone. We would like to emphasize again that the payoff difference between the single-processor and dual-processor approaches could be much larger in a different problem instance,

## 6.0. Conclusions

In this paper, we consider the problem of generating effective information-gathering, communication, and decision-making (ICD) strategies for a distributed expert problem-solving (DEPS) system. We focus on the special case of a dual-processor DEPS system and construct a mathematical model that enables the characterization of feasible, efficient, and optimal ICD strategies. We also develop computationally effective solution procedures to generate efficient ICD strategies, striving for the best net payoff we can obtain. The use of the model and the solution procedures is illustrated through an example scenario.

Our model is developed along the lines of Hall et al. (1986) and Jacob et al. (1988, 1989). However, the work presented in this paper is of significantly broader scope for two reasons. First, we generalize the uniprocessor and human-computer processor scenarios addressed in these earlier works to the case of two computerized (expert) processors. Second, we also prescribe a general solution methodology which is applicable to any problem in the dual-processor domain, provided it is modeled in accordance with our framework.

One may argue that a good ICD strategy could be elicited from the human experts being modeled within a DEPS system. Our implicit assumption has been that while we regard them as experts in the use of the information-gathering tools available to them, they are not experts at (a) sequencing these tools optimally or efficiently (in the sense of efficient strategies described in this paper), and (b) communicating with one another with a view to coordinating information-gathering efforts. Assumption (a) is especially true in contexts where the sequence of actions needed is large enough to make the speculation of effective sequencing by humans unrealistic. Assumption (b) is a consequence of the assumption of nonconflicting goals that is central to the paper.

The ideas developed here may be extended to problem solving under the cooperative distributed problem-solving (CDPS) paradigm in AI. Typically, the processors in a CDPS system are highly autonomous, know one another's capabilities and limitations, and dynamically determine communication and problem-solving strategies through cooperation, based on currently available information. Essentially, CDPS systems are planning systems that repeatedly design strategies and execute them during problem solving. Our decision-theoretic modeling constructs may be utilized by individual processors in a CDPS system to construct and execute their own ICD strategies for the solution of recurrent subproblems.

As a first step, this paper considers two processors and sequential problem solving. Further work is required to extend the proposed framework and solution methods to environments that may include any number of processors and nonsequential strategies.\*

\* Andrew Whinston, Associate Editor. This paper was rec eived on October 1, 1991, and has been with the authors 5 months for 2 revisions

## Appendix A: Complexity of the Greedy Heuristic

Recall that when an action is taken at a node, at most m signals are generated $\displaystyle \mathbf { i . e . }$ , the maximum number of branches that can emanate from a node is m. One would expect, however, that in general the number of branches emanating from a node would be significantly less than m.

For each possible node at the jth level $, \ j = 1 , \ldots , r ;$ , we select the best among the $( n - J + 1 )$ actions which have not yet been used on the path from the root to the immediate predecessor of that node. Also note that to calculate the payoff of a path from the root to a node at level $^ { \jmath , }$ we just have to add the contribution of that node to the already known contribution of the path from the root to its immediate predecessor. Thus, the overall computational requirement for generating one strategy is at most

$$
\begin{array}{r l} & n + m (n - 1) + m ^ {2} (n - 2) + \dots + m ^ {r - 1} (n - (r - 1)) \\ & <   n (1 + m + m ^ {2} + \dots + m ^ {r - 1}) = O (n m ^ {r - 1}). \end{array}
$$

Given that we generate $Q$ strategies, the worst-case time complexity of the entire procedure is $O ( Q n m ^ { r - 1 } )$

## Appendix B: Complexity of the Improvement Heuristic

In what follows, we first focus on a single strategy $\mathrm { i . e . , }$ , we temporarily assume $Q 1 0$ be 1. As before, we assume that an action can generate at most m signals.

For each node at level $j , j = 2 , \ldots , ( r - 1 )$ , we replace the current action by the second-best choice among the $( n \mathrm { ~ - ~ } \ j + 1 )$ ) actions which have not been used on the path from the root to the immediate predecessor of the node of interest. Once the replacement is made, the entire subtree emanating from the node is reconstructed. At level $( j + k )$ , the subtree may have at most $m ^ { k }$ nodes; for each such node, we select one of the $( n - \jmath - k + 1 )$ ) actions which have not been used as yet. Hence, the maximum computational effort required for replacing the action at a node at the th level and reconfiguring the corresponding subtree is

$$
(n - j + 1) + m (n - j) + m ^ {2} (n - j - 1) + \dots + m ^ {(r - 1) - j} (n - (r - 2)).
$$

Since the maximum number of nodes at the th level of the tree could be $m ^ { J - 1 }$ , the total amount of computation required for this level is at most

$$
\begin{array}{l} m ^ {j - 1} [ (n - j + 1) + m (n - j) + m ^ {2} (n - j - 1) + \dots + m ^ {(r - 1) - j} (n - (r - 2)) ] \\ = m ^ {j - 1} (n - j + 1) + m ^ {j} (n - j) + m ^ {j + 1} (n - (j + 1)) + \dots + m ^ {(r - 2)} (n - (r - 2)). \end{array}
$$

Therefore, the overall computational requirement of the procedure considering all levels from $j = 2$ through $j = ( r - 1 )$ is no more than

$$
\begin{array}{r l} & m (n - 1) + m ^ {2} (n - 2) + m ^ {3} (n - 3) + \dots + m ^ {r - 2} (n - (r - 2)) \\ & + m ^ {2} (n - 2) + m ^ {3} (n - 3) + \dots + m ^ {r - 2} (n - (r - 2)) \\ & + m ^ {3} (n - 3) + \dots + m ^ {r - 2} (n - (r - 2)) \\ & \vdots \\ = & m (n - 1) + 2 m ^ {2} (n - 2) + 3 m ^ {3} (n - 3) + \dots + (r - 2) m ^ {r - 2} (n - (r - 2)) \\ <   & (n - 1) (r - 2) (m + m ^ {2} + \dots + m ^ {r - 2}) \\ = & O (n r m ^ {r - 2}). \end{array}
$$

The worst-case time complexity of the procedure for an arbitrary value of $Q \mathrm { i } \mathsf { s } ,$ thus, $O ( Q n r m ^ { r - 2 } )$ 1

## References

Aho, A. L. and J. D. Ullman, Foundations of Computer Science, Computer Science Press, New York, 1992

Balakrishnan, A., J. C. Moore, R. Pakath and A. B. Whınston, "Information Tradeoffs in Model Building: A Network Routing Application," Computer Science in Economics and Management, 4 (1991), 201– 227.

Date, C. J., An Introduction to Database Systems, Vol. 2, Addison-Wesley, Reading, MA, 1983 (reprinted with corrections, 1985)

, An Introductton to Database Systems, Vol. 1 (5th Ed.), Addison-Wesley, Reading, MA, 1990.

DeGroot, M. H., Probabılıty and Stattsttcs, Addison-Wesley, Reading, MA, 1986.

Durfee, E. H., V. R. Lesser and D. D. Corkill, “Coherent Cooperation Among Communicating Problem Solvers,"1EEE Transactons on Computers, 36 (1987), 1275–1291.

- and -—. “ Γrends in Cooperative Distributed Problem Solving," IEEE Transactions on Knowledge and Data Engıneerıng, 1 (1989), 63–83

Hall, K., J. C. Moore and A B. Whinston, “A Theoretical Basis for Expert Systems," in L. F. Pau (Ed.), Artfictal Intellıgence in tconomıcs and Management. Elsevier, Amsterdam, 1986.

Jacob, V S., J. C. Moore and A. B. Whinston, “Rational Choice and AI," Interfaces, 18 (1988), 24–35.

- and ——,  A Model of Decision-Making Involving Two Information Processors," Computer Science in Economıcs and Management, 2 (1989), 119–149.

Moore, J. C., W. B. Richmond and A. B. Whinston, “A Decision-Theoretic Approach to File Search," Computer Science in Economıcs and Management, 1 (1988), 3-19

— and ——, "A Decision-Theoretic Approach to Information Retrieval," ACM Transactons on Database Systems, 15 (1990a), 311–340.

and -— “Optimal Decision Processes and Algorithms," Journal of Economic Dynamucs and Control. 14 ( 1990b), 375–417.

and A. B. Whinston, “A Model of Decision-Making with Sequential Information-Acquisition— Part I." Deciston Support Systems, 2 (1986), 285–307

—— and —, “A Model of Decision-Making with Sequential Information-Acquisition—Part II," Decision Support Systems, 3 (1987), 47–72.

Rao, H. R., J. C. Moore and A. B. Whinston, "A Preference Theory Approach to Decision Analysis in Resource Allocation." Computer Science in Economics and Management. 3 (1990). 215–237.

Smuth, R. G. and R Davis, "Frameworks for Cooperation in Distributed Problem Solving," IEEE Transactions on Systems, Man, and Cybernetics, 11 (1981), 61–70.
