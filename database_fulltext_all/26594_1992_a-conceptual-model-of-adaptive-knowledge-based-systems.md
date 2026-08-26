---
otero_id: 26594
otero_key: "ADXF9UBA"
title: "A Conceptual Model of Adaptive Knowledge-Based Systems"
authors: "Pi-Sheng Deng; Abhijit Chaudhury"
year: "1992"
journal: "Information Systems Research"
doi: "10.1287/isre.3.2.127"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/ADXF9UBA/fulltext/images/63b49003fee02337549ed54120dd32ed53f4ab096778a2646698f7ddc086909f.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# A Conceptual Model of Adaptive Knowledge-Based Systems

Pi-Sheng Deng, Abhijit Chaudhury,

## To cite this article:

Pi-Sheng Deng, Abhijit Chaudhury, (1992) A Conceptual Model of Adaptive Knowledge-Based Systems. Information Systems Research 3(2):127-149. http://dx.doi.org/10.1287/isre.3.2.127

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1992 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/ADXF9UBA/fulltext/images/078a1bddb9b5665884e527bbc6bf32472b053996084702b98b1dae67616650b5.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# A Conceptual Model of Adaptive Knowledge-Based Systems

Pi-Sheng Deng

Department of Computer Informaton Systems

School of Busmes Admumustrauon

Cahforna State U'niversity at Stanuslaus

Furlock, Caltornia 95380

Abhijit Chaudhury

Depariment of Management Sctence

College of Management

U'ntversity of Massadnusetts at Boston

Boston, Massad husetts 02125

The ability to learn or adapt is widely recognized as one of the most prominent abilities of any animate or inanimate intelligent system. While considerable progress has been made in the science and technology of machine learning, little of that has been incorporated in traditional knowledge-based systems such as diagnostic or expert systems operating in a managerial environment. In this paper a conceptual model of an adaptive expert system is proposed as an attempt to lay a foundation for building knowledge-based systems that can learn by interacting with the environment. In contrast to existing models for learning (such as for knowledge acquisition and skill reinement) where the issue of noise and uncertainty is usually neglected. our model incorporates a stochastic environment and a learning response behavior which too is stochastic in nature.

Adaptive e\pert stems—Admıssible plans- 1 earning—I earnung aulomata--Operational schema of expert stems-Opportunit cost — Recognıze-a cvcles—Relatme loss

## 1. Introduction

xpert systems are mainly designed to emulate and support human experts in problem-solving or decısion-making for structured or semi-structured applications, and some considerable achievements have been made in many application domains (Feigenbaum, McCorduck and Nu 1988). For instance, ın the field of audıt diagnosis alone there have been several commercial applications of expert system technology, such as: ARISC (Meservy, Bailey and Johnson 1986), AUDITOR (Dungan and Chandler 1985), AUDITPLANNER (Steinbart 1987), CFILE (Kelly, Ribar and Willingham 1986), and EDP-XPERT (Hansen and Messier 1986). However, it is widely recognized that a critical limitation of current expert system technology is its inability to improve its performance over time through the use of feedback from the environment (Michalski, Carbonell and Mitchell 1983).

Learning in an animate system is usually manifested through the adaptability of the system to its environments. Typical expert systems are not adaptive to their environments: they cannot learn from their past experiences to improve their performance in accomplishing tasks; they cannot inductively acquire new knowledge from interaction with their environments in order to deal with unfamiliar situations. This renders expert systems unsuitable for unstructured or dynamic decision-making environments.

Usually, learning is studied in terms of its two most important facets—knowledge acquisition and skill refinement. Although several learning models have been proposed based on knowledge acquisition (Michalski, Carbonell and Mitchell 1983) and skill refinement (Deng, Holsapple and Whinston 1990; Logan 1988: Newell and Rosenbloom 1981; Shrager, Hogg and Huberman 1988), most of those models implicitly assume that the environment wherein learning takes place is stable and the input to the learning system by the teacher (which could be the environment or the experimenter) is definite and not subject to noise or equivocation. This assumption is unrealistic and too restrictive, especially for expert systems operating in highly dynamic decision-making environments. Recently, research has been conducted on knowledge acquisition/refinement subject to noisy data (Politakis and Weiss 1984; Wilkins 1990), yet the major concern is on the data used for training a learning system rather than on the uncertain nature of the environment.

A dynamic environment is usually characterized by its uncertainty. Though fuzzy set theory (Zadeh 1965) has been applied to the management of uncertainty in expert systems (Kandel and Schneider 1989; Negoita 1983; Zadeh 1983) and decision processes (Gupta and Sanchez 1982; Zımmerman, Zadeh and Gaines 1984), it is not intended to equip expert systems with adaptability in a dynamic environment. Also quantifying uncertainty might not make sense. For example, small differences in degrees of uncertainty (say 0.70 and 0.72) are difficult to interpret. In addition, degree of membership is usually subjectively assigned and subjectively interpreted. Fuzzy set theory has yet to address problems such as these.

In this paper we propose a conceptual model for adaptive expert systems working in a dynamic environment by embedding the concept of learning automata (Narendra and Thathachar 1974) into the traditional operational schema of expert systems, In a dynamic environment little is known a priort about the nature of the evaluation function, and additional information must be acquired by the adaptive expert system through interaction with the environment. With the increased knowledge of the environment, the adaptive expert system would be able to develop better problemsolving, planning, or scheduling for users. This conceptual model is intended to lay a foundation for the ultimate goal of building adaptive expert systems.

The rest of the paper is organized as follows. The concept and model of learning automata are presented in §2, where reinforcement schemes are also discussed. In §3 the operational schema of traditional expert systems is discussed. The traditional model of learning automata is expanded in §4, and then integrated with the operational schema of traditional expert systems to form our model of adaptive expert systems. An example of an adaptive diagnosis is given in §5 to illustrate our model Finally, the conclusion is presented in §6.

## 2. A Model of Learning Automata

The term “learning" is widely and loosely used in our daily life. Fundamentally, learning is a multistage adaptation process (Day 1975). Learning takes place as the result of the dynamic interaction between a system and its environment, and better performance is expected to evolve through the learning process. Many definitions have been proposed for learning from various disciplines. Bearing our goal in mind, we find the definition given by Simon (1983) best fits our need: “Learning denotes changes in the system that are adaptive in the sense that they enable the system to do the same task or tasks drawn from the same population more effectively the next time." In this definition the ability to improve performance with time is the criterion for a phenomenon to be judged as “learning." Based on this definition of learning, we call any system with learning capability an adaptive system.

![](/api/attachments/ADXF9UBA/fulltext/images/58672da9ae961df35269d7dd14f585764b56a5392730a578b372de2d0e4315c1.jpg)  
FiGURE 1 A Generie Feedba k-Driven Learning Process

A learning automaton is an agent or a computational unit that acts in a dynamıc environment and updates its actions in accordance with the feedback received from the environment in order to improve its performance over time. The study of learning automata was pioneered by Varshavskii and Vorontsova (1963). They observed that automata with stochastic behavior and the ability to update their action probabilities gave rise to an interesting class of learning behavior. Since then extensive research has been done (Narendra and Thathachar 1974. Narendra and Lakshmivarahan 1977). A variety of applications have also been studied for parameter optimization problems (Baba 1978. McMurtry and Fu 1966, Shapiro and Narendra 1969), game theory (Chandrasekaran and Shen 1969, Lakshmıvarahan and Narendra 1981), routing problems (Narendra, Wright, and Mason 1977; Narendra and Thathachar 1980; Srikantakumar and Narendra 1982), and manufacturing control problems (Chaudhury and Whinston 1990). However, little studv has been devoted to how to adapt the characteristics of learning automata to make expert systems adaptive to the dynamic environment.

A learning automaton is featured by its feedback-driven learning process as described in Figure 1. In this learning process there are two major components involved: the environment and the agent (i.e., the learning automaton). The environment functions as a “teacher," while the agent acts as a "student" and interacts with its “teacher." When solving problems the agent geneiates outputs (also called actions), and the environment reacts with its evaluations (which may include awards or penalties) as feedback to the agent. In turn, the agent will respond to the feedback by modifying its behavior. Learning takes place in the form of action-feedback cycles, which involves a sequence of iterative adjustments of the agent's behavior to its environment. In this way, better performance can be expected to evolve through a sequence of iterative interactions.

![](/api/attachments/ADXF9UBA/fulltext/images/ad017d25acd57ecf5bc489171cda8b50adcb7d08d122bdaa1b661e0889edf024.jpg)  
([D]the unit tume delay)  
FiGuRE 2 A f ramework of Learning Automata

We detail the learning automaton's feedback-driven learning process as shown in Figure 2 based on Aso and Kimura (1979). This detailed model consists of two major components: one is the environment and the other one is the agent or the automaton. We define the environment F as a triple $\langle \pmb { \Lambda } , \pmb { \Lambda } , \Omega \rangle$ , where $\Lambda = \mathbf { \Omega } _ { | } ^ { \dag } a _ { 1 } , a _ { 2 } , \ldots . . . , a _ { r } \mathbf { \Omega } _ { | } ^ { \mathnormal { | } }$ 1S a finite set of actions received from the agent, and $\dot { \bf R } = { \bf \Phi } _ { \mathrm { t } } ^ { \mathrm { i } } ( \ r ) , { \bf \Phi } _ { \mathrm { l } } ^ { \mathrm { i } } ;$ is a set of binary evaluations for the actions received from the agent, with I being called the penalty response. The third component Ω is the performance evaluation mechanism, which evaluates the output performance for the agent. This mechanism can be expressed as

$$
\Omega : \mathbf {A} \rightarrow \mathbf {R} \quad \text { and }
$$

$$
\Omega (a (t)) = r (t + 1) \quad \text { where } a \in \mathbf {A} \text { and } r \in \mathbf {R}.
$$

This mechanism can be implemented as a step threshold function as shown in Figure 2. When the performance of the agent excceds a threshold value, Ω emits 0; otherwise. 1. In a dynamic environment, for each action $a _ { \iota } ( i = 1 , \dots , | \mathbf { A } | )$ , this function emits 1 (penalty) with a penalty probability ${ \bf \Xi } ( { \bf \Lambda } _ { l } ^ { \star }$ , which is pr[ $r ( \iota + 1 ) = 1 | a ( \iota ) = a _ { \iota } ]$ , or 0 (reward) with a nonpenalty probability $1 \mathrm { ~ \cdots ~ } \boldsymbol { \mathscr { i } } _ { t }$ , depending on whether the performance of this action exceeds a certain threshold value. The $c _ { \ i } ^ { \bullet } \ s$ are usually unknown a priori to the agent in a dynamic environment.

On the other hand, the agent, $\mathcal { G } ,$ needs to learn the evaluation structure, i.e., the $c _ { \iota } \mathbf { \dot { s } } .$ of the environment in order to take the most appropriate actions to improve its performance. The operation carried out by an agent is the updating of the action probabilities on the basis of the response by the environment. Our purpose is to devise the agent's behavior in such a wav as to result in a performance that can be characterized as learning.

In this paper the agent Gis defined as a quintuple R, A, S. L, O), where R is the set of binary feedback received from the environment, A is the set of actions generated by the agent, and $\mathbf { S } = \mathbf { \Omega } _ { \langle } ^ { \dagger } \mathbf { \Omega } _ { \mathbf { l } } , \mathbf { \Omega } _ { \mathbf { S } _ { 2 } } , \ldots \ldots \mathbf { \Omega } _ { \mathbf { V } _ { n } } \mathbf { \Omega } _ { \dagger } ^ { \dagger }$ is the set of all possible knowledge states of the agent. Since in the real world any created system can never be omnıscient, the knowledge state of an agent at a certain point of time can be regarded as a partial model of the agent which is stochastically modified through interaction with the environment.

L is the learning mechanism or reinforcement scheme which yields a new state for the agent by considering the feedback received from the environment and the agent's previous state and actions. Thus, I. is defined as:

$$
L: \mathbf {R} \times \mathbf {S} \times \mathbf {A} \rightarrow S \quad \text { and }
$$

$$
\mathrm{s} (t) = L (r (t), \mathrm{s} (t - 1), a (t - 1)), \quad \text { where } r \in \mathbf {R}, \mathrm{s} \in \mathbf {S}, a \in \mathbf {A}.
$$

Since in a dynamic environment there is no certainty about the states and actions that will follow a given initial state and input sequence, we can only consider probabilities associated with successive states and actions. Let $P ( t )$ denote the state probability vector $[ \jmath _ { 1 } ( \ell ) . \jmath _ { 2 } ( \ell ) . . . . , \imath . . . ( \imath ) ] ^ { I }$ at time /, and its /th component $I ^ { \gamma } , \left( t ^ { \gamma } \right)$ indicates the probability with which the th state , is chosen. Initiallv. $\rho _ { 1 } ( 0 ) \textrm { - } \rho _ { 2 } ( 0 ) \textrm { -- } \rho \textrm { -- } \rho _ { \textrm { i } \textrm { i } } ( 0 )$ $= 1 / \updownarrow \mathrm { \bf S }$ |, and $\begin{array} { r } { \sum , p , ( \ell ) = 1 } \end{array}$ for $\mathbf { \Phi } _ { l } = \mathbf { \Phi } _ { 1 } , \dots . . . \mathbf { \Phi } _ { | \mathbf { S } | }$ Updating $I ^ { \prime } ( 1 - t - 1 )$ from P(t) is achieved by this mechanism L through the use of a reinforcement scheme which will be described later.

The consequences of this learning mechanism I. have some implications. They imply that this mechanism helps the agent move from one partial model or incomplete knowledge status to another partial model with some pieces of previously unknown knowledge becoming known with higher certitude this time. This reflects the knowledge acquisition aspect of learning. On the other hand, the set S may contain the skillfulness status of the agent. The learning mechanism will make the agent more skillful in performing the same task or tasks next time. This reflects the skill refinement aspect of learning.

O is the executing mechanism or output function which vields an action for the agent based on the current state of the agent. The executing mechanism O is defined as:

$$
O: \mathbf {S} \rightarrow \mathbf {A} \quad \text { and }
$$

$$
a (t) = O (s (t)), \quad \text { where } s \in S.
$$

Without loss of generality, this function is usually simplified to be deterministic and one-to-one, and thus the number of states would be equal to the number of actions. Under this deterministic and one-to-one function, the actions are generated stochastically since states are updated stochastically, and the state probability vector $P \{ t \}$ can be treated as the action probability vector

Since the evaluation by envıronment is “noisy." usually one has to go through several iterations to average out the effect of noise. For an automaton to be said to learn in the process of its interaction with the environment. it must exhibit an ability to improve its behavior over time in terms of some evaluation function. Different tvpes of behavioral norms for the agent have been proposed (Baba 1985,

Lakshmivarahan 1981, Narendra and Thathachar 1974) for judging the learning process objectively. Those definitions are mainly based on calculating the expected evaluation received by the agent and studying how it varies over time.

Operationally, different types of behavior norms can be achieved through the agent's ability to react to positive feedback from the environment by increasing the probability associated with the action that brought the reward, and to react in the opposite manner with negative feedback. A reinforcement scheme is the algorithm that causes the performance improvement for an automaton based on this operation.

In general terms a reinforcement scheme is a function of action probability vector. agent action. and environment evaluation. A reinforcement scheme can be linear or nonlinear depending on the relationship between $P ( t )$ and $P ( t + 1 )$ . The basic concept of a reinforcement scheme is very similar to that of credit assignment (Minsky 1963: Sleeman, Langley and Mitchell 1982) and back propagation (Rumelhart and McClelland 1986). which assigns a reward or a penalty back to the responsible action depending on the evaluation received from the environment.

Although several reinforcement schemes have been proposed. none can ensure optimality in the general dynamic environment. To unify the various reinforcement schemes. Lakshmivarahan and Thathachar (1973) proposed a general class of reinforcement schemes. When the action of the agent at time t is $\boldsymbol { \mathcal { Q } } _ { t }$ , and its corresponding evaluation is $r ( t + 1 ) \because r _ { i }$ , a reinforcement scheme will update $P ( t + 1 )$ from $P ( t )$ as:

(1) When $r _ { t } = 0$ . i.e., favorable feedback

$$
\begin{array}{c} p _ {j} (t + 1) - p _ {j} (t) - f _ {j} (P (t)), \quad \text { where   } j \neq i, \quad \text { and } \\ p _ {i} (t + 1) - p _ {i} (t) + \sum_ {j \neq i} f _ {i} (P (t)). \end{array}
$$

(2) When $r _ { i } = 1$ , i.e., unfavorable feedback

$$
\begin{array}{c} p _ {i} (t + 1) = p _ {i} (t) + g _ {i} (P (t)), \quad \text { where } j \neq i, \quad \text { and } \\ p _ {i} (t + 1) = p _ {i} (t) - \sum_ {j \neq i} g _ {j} (P (t)). \end{array}
$$

In the above formulas. $f _ { \prime }$ and $g _ { \iota }$ are continuous functions such that $\Sigma _ { k } p _ { k } ( \boldsymbol { l } + \boldsymbol { 1 } ) = 1$ and $p _ { k } ( t \ + \ 1 ) \in ( 0 , \ 1 )$ whenever $\smash { p _ { k } ( t ) \in ( 0 , \ 1 ) }$ , for all $k = 1 , . . . , | \mathbf { A } |$ . The latter requirement is necessary to prevent the agent from getting trapped in an absorbing barrier with a probability value 0 or 1.

Actually, the reinforcement scheme constitutes the essence of the learning behavior of an agent. With the operation of the reinforcement scheme, the current performance of an agent can be expected to be better than its previous one. The effect of learning can thus be expressed as:

$$
\Omega (a (t - 1)) \leq \Omega (a (t)).
$$

Here we use the symbol $\cdots \leq 1 3$ to denote “better than" in terms of cost effectiveness, time efficiency, application flexibility, etc.

In this paper the concept of learning automata discussed above is embedded in the operational schema of expert systems to model adaptive expert systems.

## 3. Operational Schema of Expert Systems

The architecture of an expert system mainly consists of three major components: a working memory, a knowledge base, and an inference engine. The working memory, also called the short-term memory, is used as a buffer to hold information pertinent to the current task or problem to be solved, intermedtate results awaiting further execution, or the final solutions or suggestions for the posed task or problem. The knowledge base, also called the long-term memory, stores domain-specific knowledge for decision-making or problem-solving. It mainly comprises asserted or descriptive factual knowledge about the problem domain. and the heuristics that express the judgmental knowledge of the human expert. In addition, the algorithmic decision-making models can also be stored in the knowledge base. The knowledge of how to make effective and efficient use of the domain knowledge is stored as the general problem-solving knowledge in the inference engine. Based on the content of the working memory, the inference engine decides which pieces of the stored domain knowledge should be chosen and the sequence in which they are to be applied to generate a plan for solving the posed problem.

![](/api/attachments/ADXF9UBA/fulltext/images/3af5b538726aea8bbf4fb1758f65746d9b63399e540c140dc32c2a4ceba60abf.jpg)  
FiGURE 3 Ihe Operatonal Schema of Expert Systems

Expert systems basically operate within an operational schema called recognize-act cycles or select-execute loops (Davis and King 1977. Waterman and Hayes-Roth 1978) as shown in Figure 3. A recognize-act cycle consists of three phases: pattern matching, conflict resolution, and acting. Usually, the problem-solving process of an expert system consists of a sequence of recognize-act cycles. In each recognize-act cycle, the inference engine matches the content of the knowledge base against that of the working memory to see which pieces of knowledge are useful in solving the problem posed by the end user. This process is called pattern matching. When this pattern matching results in a set of applicable or competing expertise. called a conflict-set, the inference engine will initiate the conflict-resolution mechanism to determine the sequence of applying them. Then the action mechanism will change the content of the working memory by executing the chosen expertise to generate intermediate results and, then, adding them to the working memory. With the new content of the working memory, another recognize-act cycle will be activated. This process will iterate until the problem is solved.

In this traditional operational schema an expert system is unable to learn from its past experiences to improve the performance for executing the same or similar tasks later, since the state of the knowledge base cannot be modified. This makes exper systems not adaptive to the dynamic decision-making environment.

As an attempt to lay a foundation for building knowledge-based systems or expert systems, which are suitable for dynamic decision-making settings, a conceptual model of adaptive expert systems is proposed in the next section.

## 4. A Conceptual Model of Adaptive Expert Systems

In this section we propose a conceptual model of adaptive expert svstems that can function in a dynamic environment by integrating the model of learning automata into the operational schema of expert systems. An expert system is adaptive in the sense that it will be able to determine. based on a series of output-evaluation information, the effectiveness of the current set of plans in solving the current problem, and generate a modified set of plans next time with the expectation of a better performance. We begin with a verbal description of our model in §4.1, followed by its formalized description in §4.2. In §4.3 we discuss formal measures and norms for evaluating a system such as ours. In §4.4 we discuss a variety of refinements possible for this learning mechanism.

## 4.1. Concept of Adaptive Expert Systems

It is not uncommon to have expert systems developed through consultation with several experts. In judgmental tasks such as in medical diagnostics, auditing and credit appraisal rules from multiple experts would reflect multiple perspectives.

This paper models an expert system that is built up by consultation with several experts. Each expert provides a part of the total knowledge base and different experts provide rule sets that may overlap but are not identical. We could view such a knowledge base (KB) as consisting of subsidiary knowledge bases. called knowledge modules $( \mathrm { K B } _ { \iota } ^ { \cdot } \mathsf { s } )$ , each KB, provided by a single expert.

For instance. in the area of medical diagnostics (for say a disease named X). $\mathrm { K B } _ { 1 }$ could stand for a knowledge module that reflects the set of rules used by a doctor who prefers a low cost minimal approach to investigation and treatment. ${ \mathrm { K B } } _ { 3 }$ could represent the knowledge module provided by a doctor who believes in an expensive and invasive approach. The knowledge module KB2 could represent an attitude in between. Similarly, in the field of auditing, ${ \bf K B } _ { 1 }$ would represent a conservative auditor who advocates minimal checks of accounts and KB, an aggressive auditor with an expensive and thorough approach.

Which part of the knowledge base, i.e., which knowledge module, is most suitable for a given problem? Obviously, that depends on the problem and the environment ${ \bf K B } _ { 3 }$ may be suitable for diagnosing individuals from a poor neighborhood where, say, the disease X is actually prevalent. Similarly, in the area of auditing, $\mathrm { K B } _ { 3 }$ would be appropriate when auditing savings and loan banks in the southwest area of the country. Equally, what is the most appropriate now may cease to be so in the future because of change in the environment. How can the system be tuned when the environment has changed? How does the system ascertain which knowledge module ${ \mathrm { K B } } _ { \iota }$ is the most appropriate for a given environment? Our model addresses these two questions.

Adaptation, in our model, is a result of feedback from the environment as to the efficacy of the current KB, in solving a problem. The environment is the source where the problem originates, and the environment judges if the solution provided by the system worked or not. The system adapts to this feedback by suitably modifying its behavior. The system can, therefore, be said to be adapting to the environment. For example, let KB, be the knowledge module of choice. Since this module represents an aggressive and thorough approach, consultation would lead to expensive procedures. Let us assume that few such diagnostics are finally contırmed as persons having the disease X. The medical/insurance establishment which is meeting the cost is unlikely to view this aggressive approach to diagnostics with equanimity. This would provide an indication to the system user or operator that perhaps ${ \mathrm { K B } } _ { 1 }$ or ${ \mathsf { K B } } _ { 3 }$ may be a more appropriate choice. How can such a commonsensical approach to behavioral modification be formalized? This is precisely what our model provides. Does it work? As evidence to that effect we describe simulation of a simple numerical example in $\ S ^ { 5 }$

The knowledge base along with the inference engine constitute the adaptive expert system here that learns. The environment which judges the solution as advocated by the expert system is the teacher. If the system often calls for expensive treatments (or forecasts disease X, or frauds) and the requirement for such is not finally confirmed in real life, the system can be said to be not performing well. (Formal measures of performance are discussed in §4.3.)

The response of the environment to a suggested solution by the system is stochastic in nature. Much as in real life, a good solution does not guarantee success in the real world. Solutions are good to the extent that they have a high chance of working out successfully. A diagnostic system is appropriate only if it has a high likelihood of proving itself correct in light of the feedback received from the environment. It is inappropriate for a problem only if such positive feedback from the environment is uncommon. The challenge for the system is to select the ${ \mathrm { K B } _ { i } }$ for diagnosis that leads to highest likelihood for positive feedback. This is what our adaptive expert system performs.

In our model, the evaluation mechanism of the environment is called CR/TIC. It judges and criticizes the efficacy of the solution furnished by the adaptive expert system. Obviously, the adaptive expert system is not priv to the knowledge or mechanism in the CRITIC that determines the success or failure of its solution. If that were so there would be nothing left for the system to learn. The adaptive expert system is a system separated from the environment and it has access only to the resultant feedback from the environment

In our model. the adaptive expert system goes through four steps in every learning cycle as it interacts with the environment as shown in Figure 4. These are:

(1) Given data relevant to a problem, the system selects which of the modules can possibly provide a solution. This subset of KB is denoted as S. and this process is referred to as the MATCH operation.

(2) The adaptive expert system has a certain preference structure or relationship over the ${ \bf K B } _ { \imath } ^ { \ast } { \bf s }$ contained in S with respect to a certain environment. This relationship is used to select a knowledge module (say, $\mathbf { K B } _ { \mathfrak { r } } )$ ) which is going to be used for consultation. The selected KB, furnishes a solution. This process is referred to as the admissı- bie-plan generation (ADMS).

(3) The solution is judged by the environment's evaluation mechanism CRITIC

(4) This judgment is used to alter the preference distribution over the ${ \bf K B } _ { \imath } ^ { \prime } { \bf s }$ in S. If the CRITIC decides that the solution is good, the preference for ${ \mathsf { K B } } _ { { \boldsymbol { \imath } } }$ is increased relative to other knowledge modules: otherwise it is decreased. This process is performed by the LEARNER mechanism

![](/api/attachments/ADXF9UBA/fulltext/images/e2513eefeed60b2938cebbce44e47c783ca909755c80c28764f709d34972ae60.jpg)  
FiGURE 4. The Conceptual Framework of Adaptive Fxpert Systems

## 4.2. Structure of Adaptive Expert Systems

In this section we define the structure of an adaptive expert system (AES) in terms of its components as a quadruple:

$$
\mathrm{AES} = \langle \mathrm{WM}, \mathrm{KB}, \mathrm{INF} (\text { MATCH }, \text { ADMS }, \text { LEARNER }), \text { CRITIC } \rangle
$$

Each component in this quadruple is described as follows

(i) WM: Working Memory. As defined in the previous section, this component is used as the buffer for the AES to store the data pertinent to the current task or problem to be solved, intermediate results, and the final solutions or consultations generated from the AES.

(ii) KB: Knowledge Base. Each member of KB is a knowledge module representing a chunk of knowledge or expertise. Metaphorically, we can regard our knowledge base as consisting of a set of experts or knowledge modules. Each expert or knowledge module has the ability to solve a given problem, and abilities of one expert may overlap with those of other experts. Thus, the state space of the system can be represented by the set of knowledge modules contained in the knowledge base. In this model we use a finite set $\mathbf { K B } = \mathbf { \sigma } _ { \mathrm { { i } } } ^ { \prime } \mathbf { K B } _ { 1 } , \mathbf { \sigma } _ { \mathrm { { i } } } \mathbf { K B } _ { 2 } , \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma } _ { \mathrm { { - } } } \mathbf  \sigma { \sigma } _ { \sigma } _ { \mathrm { { - } } } \mathbf { \sigma { \sigma } _ { \sigma } } \mathbf  { \sigma } _ { \sigma } { \sigma } _ { \sigma } { \sigma } \sigma _ { \sigma } { } \sigma _  \sigma$ to represent the state space, where each KB, is a knowledge module. These knowledge modules can be regarded as vying or competing with each other to solve the problem faced by the AES.

(iii) INF: Inference Engine. The inferencc engine is the “brain" of an AES. Not only does it reason and solve the proposed problems by applyıng appropriate expertise stored in the knowledge base and explain its own reasoning processes, but it also “learns lessons"(1.e., the evaluations received from the environment) from “past experiences $\because ( \mathrm { i . e . }$ , the decision made or the plan adopted previously) through the interaction with the environment to improve the performance for the AES.

The INF contains three major mechanisms. Given a problem to be solved or consulted, the MATCH mechanism seeks the applicable knowledge modules in the knowledge base for problem-solving by referring to the data held in the working memory. Thus. this mechanism can be represented by the following mapping:

$$
M A T C H: \mathbf {K B} \times \mathbf {W M} \rightarrow 2 ^ {\mathbf {k B}}
$$

where $2 ^ { \mathbf { K B } }$ is the power set of the knowledge base KB. The result is a set with respect to the KB and the WM at time t. We use S, which is a subset of the state space KB at time t, to represent such a set of applicable knowledge modules. Since each knowledge module in S is capable of solving a given problem, S can be regarded as an indication of the $\mathbb { A E S } ^ { \prime } \mathrm { s }$ abilitv to solve a given problem or to make decısions. Thus, S represents the knowledge state of the system with respect to a given problem. For instance, if KB consists of ten modules K $\mathbf { B } _ { 1 } , \mathbf { K B } _ { 2 } , \dotsc , \mathbf { k B } _ { 1 0 } .$ , the set S may stand for modules $\mathsf { K B } _ { 1 } , \mathsf { K B } _ { 2 }$ and ${ \bf K B } _ { 3 }$ . They are the three modules that are capable of solving the problem as described in the working memory.

In a dynamic environment a human expert usually comes up with a set of feasible solutions, recommendations or plans for the problem encountered; the same occurs in our model. In our model each knowledge module $\mathrm { K B } _ { \iota }$ contained in S may stochastically generate a set of feasible plans $\Lambda _ { i }$ . Since different experts may have some common solutions when facing a problem, $\Lambda , \cap \mathsf { A } , \neq \emptyset$ . for $\iota \neq \iota .$ Let A be the set of all admissible plans which can be generated from S. The plan-generation mechanism ADMS in our model can be expressed as

$$
A D M S: \mathrm{S} \rightarrow \mathrm{A} \quad \text { and }
$$

$$
a (t) = A D M S (\mathrm{s} (t)), \quad \text { where } \mathrm{s} \in \mathrm{S} \text { and } a \in \mathrm{A}.
$$

This ADMS is a stochastic function instead of a determinustic, one-to-one function as stated in the model of learning automata. In other words. an admissible plan set will be stochastically formed at time / based on the state of the system. This admissible plan set is associated with a conditional probability matrıx. 1D 1S, of dımension |S $\times \mid \bf { A } \mid$ , whose entries are given by

$$
\begin{array}{r l} a d m s _ {i j} & = \operatorname * {p r} [ a (t) = a _ {j} | s (t) = \mathrm{KB} _ {i} ], \quad \text { where } \\ & \quad t = 1, 2, \dots , | \mathbf {S} |, \quad j = 1, 2, \dots , | \mathbf {A} |, \\ & \sum_ {j} a d m s _ {i j} = 1 \quad \text { for   each } \mathrm{KB} _ {i} \in \mathbf {S}. \end{array}\tag{and}
$$

Each element $a _ { \scriptscriptstyle { J } }$ in its admission plan set A, has a probability $a d / m \backprime _ { \iota \iota }$ , and $u d m s _ { { \scriptscriptstyle t j } } \ne 0$

In terms of the example discussed in $\ S 4 . 1 , \ K \{ 3 _ { 1 }$ stands for a knowledge module that advocates an economical and minimal approach to problem-solving. ${ \mathrm { K B } } _ { 3 }$ stands for a thorough and aggressive approach and $\mathsf { K B } _ { 2 }$ stands for a philosophy in between. Given any knowledge module there exists a set of admissible plans or solutions. The solution sets across all ${ \bf K B } _ { t } ^ { \prime } \mathsf { s }$ will usually overlap. The total possible solution set is called A, and it contains various actions. some of which are expensive procedures and some economical. KB, has a higher probability of advocating an expensive and detailed solution, and KB, will have a lower probability for the same. We use $\mathfrak { a d } \mathfrak { m } . \mathfrak { s } _ { \iota \beta }$ to stand for such a probabılistic relationship. Actually, each row $( a d m s _ { \iota 1 } , a d m s _ { \iota 2 } .$ $\dots , a d m s _ { \iota | \pmb { A } | } )$ can be regarded as the indication of an expert's confidence in its own different admissible plans, and can thus be estimated from confidence factors in rule-based expert systems.

A special case occurs when single conflict resolution strategy is applied to S as in traditional expert systems, and only one plan will be selected. In this case ADMS will reduce to a deterministic and one-to-one function.

The condition for the AES to survive in facing a problem is $\mathbf { A } \neq { \mathcal { D } }$ , In other words. the system survives only if it can generate a nonempty admissible plan set. A nonempty admissible plan set implies that the system has the ability to solve the posed task. When the admıssible plan set is empty, it implies that the system is unable to accomplish the task or solve the problem, and it goes bankrupt and reports failure. In this case, the knowledge base needs to be refined or expanded, which can be accomplished based on either manual or automatic knowledge acquisition/refinement approaches.

The evaluation mechanism, CRITIC, of the environment evaluates the outcome performance for the AES and provides feedback. This function serves as the teacher or supervisor of the AES. Not only can it assign 0 or 1 to the admissible plan, but also it is allowed to “grade" the performance of the admissıble plan. In a dynamic environment, CRITIC is a stochastic mechanism and its internal structure is unknown to the AES. We define

$$
C R I T I C: \Lambda \rightarrow E V A L \quad \text { and }
$$

$$
e (t + 1) = \text { CRITIC } (a (t)) \quad \text {   for   } e \in \text { EVAL   and   } a \in \mathbf {A}.
$$

Here we use EVAI, to denote the finite set of evaluations made bv the environment. This evaluation result is generated stochastically from the environment. Thus there will be a stochastic matrix, $C R I T I C _ { A }$ , associated with an admissible plan set, A, during the evaluation process, and whose (t, / )th entry $\iota ^ { * } \iota t \iota c _ { \iota \iota }$ gives the probability of the occurrence of evaluation $e _ { t } \in \mathbf { E V } \mathbf { A I }$ for an admissible plan $a _ { \ i } \in \mathbf { A }$ . Thus,

$$
\operatorname{critic} _ {i j} (t + 1) = \operatorname{pr} [ e (t + 1) - e _ {j} | a (t) = a _ {i} ], \quad \text { where }
$$

$$
i \quad 1, 2, \dots , | \mathbf {A} |, \text {   and   } j = 1, 2, \dots , | \mathbf {E V A L} |,\tag{and}
$$

$$
\sum_ {i} \text { crittc } _ {i j} - 1 \quad \text { for   each } a _ {i} \in \mathbf {A}.
$$

In a dynamic environment, $C R I T I C _ { 4 }$ is usually unknown to the AES and is to be estimated by it.

Another mechanism contained in INF is a learning mechanism: LEARNER. This mechanism modifies the state of the system based on its previous state. the decision made or plan adopted at the previous stage (i.e., the previous experience), and the corresponding evaluation made by the “teacher". In other words, the AES will learn from past experiences in solving the posed task so that it will be more adaptive to the environment as time proceeds. This mechanism corresponds to the mechanism L in the learning automata model, and can thus be defined as:

$$
\text { LEARNER }: \mathrm{S} \times \mathrm{A} \times \text { EVAL } \rightarrow \mathrm{S} \quad \text { and }
$$

$$
s (t) = \text {   LEARNER } (s (t - 1), a (t - 1), e (t)), \quad \text { where   } s \in \mathbf {S}, a \in \mathbf {A}, e \in \mathbf {E V A L}.
$$

Since the environment concerned in this paper is stochastic, its evaluation structure is unknown to the AES. The evaluation is, thus, treated as being stochastically generated from the environment. Based on the knowledge module chosen at the previous stage, the admissible plan chosen at the previous stage, and the corresponding evaluation for that chosen plan, the current state of the whole system is stochasticallv determined bv LEARNER as switched from the previous state. In other words, LEARNER is associated with a state transition probabılity matrıx, which is a conditional probability matrix that determines the revised probability distribution over the state S, with each element defined as follows:

$$
\begin{array}{l} \text { l   e   a   r   n   e   r } _ {(i j) (m n)} (t) = \operatorname * {p r} [ s (t) = \mathbf {K B} _ {j} | s (t - 1) = \mathbf {K B} _ {i}, a (t - 1) = a _ {m}, e (t) = e _ {n} ], \quad \text { where } \\ \quad i, j = 1, 2, \dots , | \mathbf {S} |, m = 1, 2, \dots , | \mathbf {A} |, n = 1, 2, \dots , | \mathbf {E V A L} | \quad \text { and } \\ \quad \sum \text { l   e   a   r   n   e   r } _ {(i j) (m n)} (t) = 1. \end{array}
$$

Thus, the probability for $\angle E A R N E R$ to move the state of the whole system from a state / to another state / is defined as:

$$
\begin{array}{r l} f _ {i j} (t) & = \operatorname * {p r} [ s (t) = \mathrm{KB} _ {j} | s (t - 1) = \mathrm{KB} _ {i} ] \\ & = \sum_ {k} \sum_ {n} \operatorname * {p r} [ s (t) = \mathrm{KB} _ {j} | s (t - 1) = \mathrm{KB} _ {i}, a (t - 1) = a _ {k}, e (t) = e _ {n} ] \\ & \quad * \operatorname * {p r} [ a (t - 1) = a _ {k} ] * \operatorname * {p r} [ e (t) = e _ {n} | a (t - 1) = a _ {k} ] \\ & = \sum_ {k} \sum_ {n} l e a r n e r _ {(i j) (k n)} (t) * p _ {A, k} (t - 1) * c r i t t c _ {k n} (t). \end{array}
$$

(Note that $p _ { \mathbf { A } , k }$ will be defined later.) While $\smash { \mathrm { \it { l e a r n c } } ^ { * } \boldsymbol { r } _ { ( t , t ) ( m , n ) } }$ is the knowledge state transition probability given the admissible plan $a _ { m }$ , and its corresponding evaluation $\ell _ { n } , \ell _ { t i }$ IS the total transition probability for a knowledge module KB, when consıdering all the possible admissible plans of the previous knowledge module and all the possible evaluations for each of those admissible plans. The relationship between $f _ { i j }$ and its components is shown in Figure 5. In terms of the previous example. $f _ { 1 \underline { { { \rangle } } } } ( { \it { ! } } )$ is the conditional probability for ${ \bf K } { \bf B } _ { 2 }$ being chosen for consultation at time / given that ${ \mathrm { K B } } _ { 1 }$ was chosen for consultation at time $\textit { \textbf { l } - } 1$

A special case is when there are only two types of evaluations emitted from the environment for each admissible plan $u _ { i } \colon 1$ (penalty) with a penalty probabilit $c r i t l { \dot { \iota } } _ { k 1 }$ and 0 (reward) with a nonpenalty probabilıty $\textit { 1 } - \iota ^ { * } \iota \iota \iota _ { \iota _ { h } } ^ { }$ , then

$$
\begin{array}{r l} f _ {i j} (t) = \sum_ {k} \text {   learner } _ {(i j) (k 0)} (t) * p _ {\mathcal {A}, k} (t - 1) * (1 - \text {   critic } _ {k 1}) \\ & + \sum_ {k} \text {   learner } _ {(i j) (k 1)} (t) * p _ {\mathcal {A}, k} (t - 1) * \text {   critic } _ {k 1}. \end{array}
$$

Based on the knowledge state transition probabılity, the system will be in a certain state of being stochastically transitted from various knowledge states. We define the probability for the system to be in state $j \ \mathrm { a s } \ \pi _ { { \scriptscriptstyle  } _ { j } } .$ , and

$$
\begin{array}{r l} \pi_ {j} (t) & = \operatorname * {p r} [ s (t) - \mathrm{KB} _ {j} ] \\ & = \sum_ {i} \operatorname * {p r} [ s (t) - \mathrm{KB} _ {j} | s (t - 1) = \mathrm{KB} _ {i} ] * \operatorname * {p r} [ s (t - 1) = \mathrm{KB} _ {i} ] \\ & = \sum_ {i} f _ {i j} (t) * \pi_ {i} (t - 1) \quad \text { for   each } \mathrm{KB} _ {i} \in \mathbf {S}. \end{array}
$$

The relationship between $\pi _ { \iota }$ and $f _ { \imath \jmath }$ is shown in Figure 6. Let $\begin{array} { r } { \operatorname { I I I } ( \iota ) = \left[ \pi _ { 1 } ( \iota ) , \pi _ { 2 } ( \iota ) , \dots \dots , \right. } \end{array}$ $\pi _ { \mathfrak { i s } | } ( \mathfrak { i } ) \mathfrak { j } ^ { \prime }$ and $ { \boldsymbol { F } } = \left[  { \boldsymbol { f } } _ { \iota \eta } \right] ( \mathrm { f o r } \iota , \dot { \iota } = 1 , \dot { 2 } . \dots . \dots |  { \mathbf { S } } | )$ , then $\mathrm { I I } ( \iota ) = F ^ { \prime } \mathrm { I I } ( \iota - \mathrm { ~ \iota ~ } | )$ . Conceptually, $\pi _ { i } \mathbf { \dot { s } }$ can be regarded as the system's preference distribution concerning its knowledge modules. The changing behavior or the adaptability of the system is represented by

![](/api/attachments/ADXF9UBA/fulltext/images/1c7e3e36e6a5dad8e7a41f031ea91eec1a38a00f9e050125284a23802b1a229d.jpg)  
FiGURE 5 The Knowledge State Transition Diagram

Multiplication

![](/api/attachments/ADXF9UBA/fulltext/images/aa240cb8189982c7c6802c9c421fb6ae6b0e0dc81ddb668f8ef21c40764abb65.jpg)  
FiGURE 6. The Relationship Between /, and π,

![](/api/attachments/ADXF9UBA/fulltext/images/4a41f3b9077f30207af468b8de5a6d4649d73dbf09e1e1a35ca6dae2f49083cc.jpg)  
FiGURE 7 The Relationshıp Between $I ^ { \prime } \mid _ { i , j } \cdot \langle l ( l  \dot { l } ^ { \prime \prime \prime } \rangle _ { \mathrm { \scriptsize ~ \gamma _ { \prime } ~ } }$ and $\pi _ { \epsilon }$

the changing of the probability vector Il(t) over time. In terms of our example. $\pi _ { 1 }$ denotes the absolute probability that ${ \mathrm { K B } } _ { \mathrm { t } }$ is chosen for consultation at time t. I(t) is the vector of such absolute probabilities or preference associated with $\mathrm { K B } _ { 1 } , \mathrm { K B } _ { 2 }$ and $\mathrm { K B } _ { 3 } .$ , respectively, at time

Since the selection of plan is based on the state value and since the state space of the system will be stochastically modified in a dynamie environment, each plan will be stochastically generated. Considering various knowledge modules involved in $\mathbf { S } ,$ the probability for an admissible plan $a _ { j }$ in A to be chosen can be defined as:

$$
\begin{array}{l} p _ {A, j} (t) = \operatorname * {p r} [ a (t) = a _ {j} ] \\ = \sum_ {i} \operatorname * {p r} [ a (t) = a _ {j} | s (t) = K B _ {i} | * \operatorname * {p r} [ s (t) = K B _ {i} ] \\ = \sum_ {i} \sum_ {k} a d m s _ {i j} (t) * \operatorname * {p r} [ s (t) = K B _ {j} | s (t - 1) = K B _ {k} ] * \operatorname * {p r} [ s (t - 1) = K B _ {k} ] \\ = \sum_ {i} \sum_ {k} a d m s _ {i j} (t) * f _ {k i} ^ {\prime} (t - 1) * \pi_ {k} (t - 1) \\ = \sum_ {i} a d m s _ {i j} (t) * \pi_ {i} (t). \end{array}
$$

We represent the probability vector over the admissible plan set at time / as: $P _ { \bullet } ( t )$ $= [ p _ { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf 1 } } } } } } } } , \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { 1 } } } } } } } ( t ) , p _ { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathcal { A } } } } } } } 2 } ( t ) , \dots , . . . , p _ { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathcal { A } } } } } } } , \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \Phi } } } } } } ( t ) } ( t ) ] ^ { I }$ . Based on the definitions of. 1D MS and 11, this probability vector can be derived as $P _ { A } ( \iota ) = \varLambda I D \varLambda I S ^ { \prime } \ I 1 ( \iota )$ . And the relationship between $p _ { 4 , \prime } .$ $a d / m \mathrm { s } _ { \iota \iota }$ and $\pi _ { \rho }$ is shown in Figure 7.

## 4.3. Behavior Norms of . Idaptive Expert Systems

In interacting with the environment, an AES should improve its behavior over time (see the definition of learning at the beginning of $\ S _ { - } ^ { 2 } \}$ in terms of some evaluation function if the behavior is to be characterized as learning. To evaluate the learning process objectively, it is necessary to set up quantitattve norms of behavior. In this section we define various norms of the AES behavior adapted from Baba (1985), Lakshmivarahan (1981), and Narendra and Thathachar (1974). Those definitions are mainly based on the calculation of the expeeted opportunity cost for admissı- ble plans.

To every evaluation $\boldsymbol { \mathscr { e } } _ { \boldsymbol { \jmath } }$ from the environment the system attaches to it a real number that measures its reward/penalty value. We define a random variable. $L _ { e } .$ , as the relative loss (Aso and Kimura 1979) associated with ${ \boldsymbol { c } } \in \mathbf { F V } \mathbf { A L }$ , and

$$
L _ {e} = \frac {\max _ {e ^ {\prime} \in \mathrm{EVAL}} R _ {e ^ {\prime}} - R _ {e}}{\max _ {e ^ {\prime} \in \mathrm{EVAL}} R _ {e ^ {\prime}} - \min _ {e ^ {\prime} \in \mathrm{EVAL}} R _ {e ^ {\prime}}} \text {,} \quad 0 \leq L _ {e} \leq 1,
$$

where $R _ { e ^ { \prime } }$ denotes the quantified value of evaluation $\ell ^ { \prime } ,$ for all $c ^ { \prime } \in \mathbf { F V } \mathbf { A } \mathbf { L }$ , and the better $\ell ^ { \prime }$ is, the higher $R _ { e } ,$ , is. $\smash {  { L _ { s } } _ { \varepsilon ^ { \prime } } }$ measures or rates a feedback e in relation to the best and the worst feedback that any admissible plan can obtain. Therefore, $L _ { \epsilon }$ , is a relative measure of e with respect to all other possible evaluations made by the CRITIC. It is a theoretical construct used for judging the performance of a formalized system such as ours.

In the example to be discussed in $\ S 5 .$ , we consider a special case where the environment gives only two types of evaluations, i.e., 1 (penalty) and 0 (reward). In this case. the relative loss will become

$$
L _ {e} = \left\{ \begin{array}{l l} 0 & \text { when   favorable }, \\ 1 & \text { when   unfavorable }. \end{array} \right.
$$

Based on the relative loss concept we can define the opportunity cost. $c _ { A , t }$ , for each admissible plan $a _ { i } \in \mathbf { A }$ as a function of the evaluation made by the environment:

$$
\begin{array}{r l} c _ {A, t} (t) & = E [ L _ {e} (t) | a (t - 1) = a _ {t} ] \\ & = \sum_ {c} (c r i t i c _ {i c} * L _ {c}) \\ & = C R I T I C _ {I} \mathbf {L} \end{array}
$$

where $\mathrm { C R } I T I { \mathrm { : } }$ is the th row of $\textcircled { \times } R I T I C _ { \textit { 1 } } ( { \textit { 1 } } )$ , and $\mathbf { L } = [ L _ { \circ _ { 1 } } , L _ { \circ _ { 2 } } , \dotsc , L _ { \circ _ { \vert \mathbf { F } \mathbf { v } \mathbf { A } \mathbf { L } \vert } } ] ^ { T }$ . Let $\boldsymbol { C _ { A } } ( t ) = [ \boldsymbol { c _ { 4 , 1 } } ( t ) , \boldsymbol { c _ { 4 , 2 } } ( t ) , \dots , \boldsymbol { c _ { 4 , | \boldsymbol { A } | } } ( t ) ] ^ { t }$ represent the opportunity cost vector associated with the admissible plan set generated at time 7, and thus $ { C } _ {  { d } } ( \iota ) = C ^ { \prime } R I I T I C _ {  { d } } ( \iota ) \mathbf { I }$

Given a probability vector $P _ { \mathcal { A } } ( t )$ over an admissible plan set A, we can define the expected opportunity cost, which is useful in judging the behavior of an AES, for A as:

$$
\begin{array}{r l} \underline {{\mathbf {C}}} _ {A} (t + 1) & = E [ L _ {c} (t + 1) | P _ {A} (t) ] \\ & = \sum_ {i} (c _ {A, i} (t + 1) * p _ {A, i} (t)) \quad \text { for } \quad t = 1, 2, \dots , | A | \\ & = C _ {A} (t + 1) ^ {l} P _ {A} (t). \end{array}
$$

Based on the expected opportunity cost for a set of admissible plans, we can measure the performance of an AES. An AES will generate sets of admissible plans with decreasing expected opportunity cost over time. This can be expressed as:

$$
E \left[ L _ {c} (t + 2) \mid P _ {A} (t + 1) \right] <   E \left[ L _ {c} (t + 1) \mid P _ {4} (t) \right] \quad \text { or } \quad \underline {{\mathbf {C}}} _ {A ^ {\prime}} (t + 1) <   \underline {{\mathbf {C}}} _ {A} (t),
$$

where A is the admissible plan set generated at time t, and A'is the admissible plan set generated at time $i ~ + ~ 1$ . In other words, the performance improvement for an AES will be reflected in terms of the decreasing expected opportunity cost over time.

In the absence of any a priorı information, the admissible plan may be chosen on the basis of equal probabilıty. The expected opportunity cost of such an initial strategy is said to be the ignorance cost, and is denoted by $\underline { { \mathbf { C } } } _ { A } ^ { ( 1 ) }$ , where $\textstyle \mathbf { \underline { { C } } } _ { \pmb { A } } ^ { ( ) } = \sum _ { \pmb { i } } c _ { \pmb { A } _ { t } } ( { \boldsymbol { i } } ) / \left| \mathbf { \underline { { A } } } \right|$ $= C _ { 4 } ^ { \prime } \mathbf { l } / \left. \mathbf { A } \right.$ where 1 means a $| \Lambda | \times |$ vector $\{ 1 , 1 , \dotsc , 1 \} ^ { I }$ . In the following we define different types of AES behavior based on $\mathbf { \boldsymbol { C } } _ { \mathcal { A } } ( t )$ and $\underline { { \mathbf { C } } } _ { A } ^ { 0 }$

DEFINITiON 1. An AES's behavior is called expedient, if lim, $\smash { \to \chi \smash [ t ] { \vdots } [ \mathbb { C } _ { \varepsilon } ( t ) ] < \mathbb { C } _ { \varepsilon } ^ { 0 } }$ and the minimum value of $\sum _ { i = 1 } ( i )$ is min $\{ \iota _ { \mathcal { A } , l } ^ { \prime } \{ l \} _ { 1 } ^ { \ell }$

This definition means that an expedient AES's expected opportunity cost in the limit is less than the ignorance cost.

DEFINITiON 2. An AES's behavior is called optimal, if lim $\mathsf { i } _ { \prime \to \mathcal { I } } E [ \mathbb { C } _ { \mathcal { A } } ( \ell ) ] = \mathsf { c } _ { \iota \pm }$ . where $c _ { \iota \iota } = \operatorname* { m i n } _ { \iota \colon } \iota _ { \iota , \iota } ( \iota ) \smash  \}$

By optimality we mean that the admissible plan associated with the minimum expected opportunity cost is chosen with probability approaching asymptotically to 1. While optimality is a desirable property, it has been shown that most situations preclude its achievement. We can then attempt to obtain suboptimal performance.

DEFINITION 3. An AES's behavior is called θ-optimal, if lim $\operatorname { \varepsilon } _ { \iota \to \iota } E [ \underline { { \mathbf { C } } } _ { \cal A } ( \iota ) ] = \mathfrak { c } _ { \alpha } + \theta$ can be obtained with any arbitrary small value $\theta > 0$ , which is a parameter included in the learning mechanism.

This definition implies that the performance of an A S can be made as close to the optimal as desired. In order for an AES to adapt to a changing environment, the behavior of the AES should improve monotonically over time.

DEFINITION 4. An AES's behavior is absolutely expedient, if $E [ \underline { { \mathbf { C } } } _ { A } ( \iota + \mathsf { I } ) | P _ { A } ( \iota ) ]$ $< \mathbf { { C _ { \mathcal { A } } ( \boldsymbol { t } ) } }$ , for all t, all $p _ { \pmb { A } , i } ( t ) \in ( 0 , 1 ) ( \mathrm { i } = \mathrm { ~ \mathbb { 1 } ~ } , \mathrm { ~ . ~ . ~ . ~ } , | \pmb { A } | )$ , and all possible values of $\dot { \langle { \bf \dot { \eta } } _ { A , l } ( l ) \rangle }$

Absolute expediency implies that $E [ \mathbf { C } _ { A } ( t ) ]$ is strictly monotonically decreasing in t. This definition also implies that θ-optimality is a special case of absolute expediency Based on the observation made on learning automata, we can simılarly argue that an θ-optimal AES might be also absolutely expedient, though this has not been formally shown to hold. Later the necessarv and sutficient condition for an agent to be absolutely expedient will be discussed.

Actually, the exhibition of different kinds of behavior is affected by the reinforcement scheme, which constitutes the essence of the learning behavior of an AES. In the next section we discuss some reinforcement schemes for an AES.

## 4.4. Refinement Schemes for Adaptive Expert Systems

As mentioned in $\ S 2$ a reinforcement scheme is the component that realizes the performance improvement for the LEARNER so that an AES is equipped with adaptability. Based on the evaluation received from a dvnamic environment, a reinforcement scheme stochastically attributes a reward or a penalty back to the responsible knowledge module in terms of the modification of the preference distribution over S.

In general terms a reinforcement scheme T' can be iepresented by

$$
\operatorname{learner} _ {(t K) (m n)} (t + 1) = T \left[ \operatorname{learner} _ {(t K) (m n)} (t), s (t), s (t + 1), a (t), c (t + 1) \right].
$$

To obtain the state transition probability $f _ { t \dot { \kappa } }$ for LEARVER to move the system state from ${ \mathrm { \bf K B } } _ { t }$ to state K $\mathsf { B } _ { \mathsf { A } }$ at time $i + \downarrow , T$ updates the prev ious state transition probability $f _ { \iota \kappa } ( \iota )$ by considering the plan $a _ { m }$ chosen at time / and its corresponding evaluation $\ell _ { n } .$ If the evaluation for the chosen plan is favorable, then $\smash { \big / \mathcal { L } ( \ell / \ell ^ { \prime } ) \mathcal { L } ^ { 2 } ( \iota _ { \Lambda } ) ( m _ { \mathstrut } ) } ( \ell ^ { \prime } + 1 ) $ 1S increased. At the same time, the other elements learn $" r _ { ( i j ) ( m / l ) } ( ( \cdot + \mathrm { ~ l ~ } )$ , where $\jmath \neq K$ , must be decreased so that the stochastic nature of the transition matrıx can be preserved On the other hand, for an unfavorable evaluation ${ \big / } ( { } ^ { \prime } ( \iota / \prime / \iota ^ { \prime } ) ^ { \prime } \iota ^ { \prime } ) _ { ( \iota \Lambda ) ( \prime \prime \prime ) } ( \iota ^ { \prime } \cdot \iota ^ { \prime } ) ^ { \prime }$ is decreased and all the other elements of the ith row are increased.

A dynamic environment “grades" the performance of the AES. Given $a ( t ) = a _ { m }$ which is an admissible plan of the knowledge module ${ \mathrm { K B } } _ { \mathsf { A } }$ and its corresponding evaluation $\boldsymbol { \ell } _ { \eta }$ , a general reinforcement scheme (based on the one mentioned in $\ S 2 )$ for an absolutely expedient AES to move its state from KB, at time / to K $\mathtt { B } _ { K }$ at time t + 1 can be described as follows:

(1) For state $\operatorname { K B } , ( \ j \neq K )$

$$
\operatorname{learner} _ {(i j) (m n)} (t + 1) = \operatorname{learner} _ {(i j) (m n)} (t) + \mathbf {h} _ {n} [ \operatorname{learner} _ {(i j) (m n)} (t) ], \quad \text { and }
$$

(2) For state ${ \mathrm { K B } } _ { K }$

$$
\begin{array}{l} \text { l   e   a   r   n   e   r } _ {(i K) (m n)} (t + 1) = \text { l   e   a   r   n   e   r } _ {(i K) (m n)} (t) \\ \quad + \sum_ {j \neq K} (\operatorname{sign} (\mathbf {h} _ {n} [ \text { l   e   a   r   n   e   r } _ {(i j) (m n)} (t) ]) * \mathbf {h} _ {n} [ \text { l   e   a   r   n   e   r } _ {(i j) (m n)} (t) ]) \end{array}
$$

where each $\mathbf { h } _ { n }$ is a continuous function with respect to the evaluation $\ell _ { n } .$ with - 1 $< \mathbf { h } _ { n } [ l e a r n e r _ { ( \iota / \iota ) ( m n ) } ( \iota ) ] < 1$

The necessary and sufficient conditions for an AES using the general reinforcement scheme to be absolutely expedient can be adapted from Lakshmivarahan and Thathachar (1973) as;

$$
\frac {\mathbf {h} _ {1} \left[ \text { learner } _ {(i j) (m 1)} (t) \right]}{\text { learner } _ {(i j) (m 1)} (t)} = \dots = \frac {\mathbf {h} _ {| \mathbf {E V A L} |} \left[ \text { learner } _ {(i j) (m | \mathbf {E V A L} |)} (t) \right]}{\text { learner } _ {(i j) (m | \mathbf {E V A L} |)} (t)}.
$$

Combining the above conditions suggests that to obtain absolute expediency different types of updating should be made for the state transition probability from a state KB, at time / to a particular state $\mathrm { K B } _ { k }$ at time $1 + 1$ . In addition, no distinction should be made among the states ${ \mathrm { K B } } ,$ other than ${ \mathrm { K B } } _ { k }$ at time $t + 1$ in the sense that the ratio $\smash { l c a r n c r _ { ( t ) ( m n ) } ( t + 1 ) / l e a r n c r _ { ( t ) ( m n ) } ( t ) }$ should be the same for all these states. This is because of the following reasons:

$$
\operatorname{learner} _ {(i j) (m n)} (t + 1) = \operatorname{learner} _ {(i j) (m n)} (t) + \mathbf {h} _ {n} [ \operatorname{learner} _ {(i j) (m n)} (t) ]
$$

which can be rewritten as

$$
\frac {\text { l   e   a   r   n   e   r } _ {(i j) (m n)} (t + 1)}{\text { l   e   a   r   n   e   r } _ {(i j) (m n)} (t)} = 1 + \frac {\mathbf {h} _ {n} [ \text { l   e   a   r   n   e   r } _ {(i j) (m n)} (t) ]}{\text { l   e   a   r   n   e   r } _ {(i j) (m n)} (t)}.
$$

As mentioned in $\ S 2$ . in the traditional model of learning automata, states and actions are regarded as synonyms. The reinforcement scheme directly updates the probability associated with each action. However, in our model the reinforcement scheme updates the transition probability associated with each state, i.e., a member of the knowledge base, in S. This, in turn, affects the probability for a plan to be chosen. In this way. in solving problems the AES will gradually converge to the most promising states (i.e., the most successful knowledge in the knowledge base), in terms of the evaluation received from the environment. This implies that performance improvement evolves as the AES moves to a better state.

## 5. Example—An Adaptive System for Performance Diagnosis

In this section we describe in detail a numerical example to illustrate the key concepts of our model. We consider the context of an actual news item by Dietz (1991). We will also describe the outcome of a computer simulation experiment. The simulation was written in BASIC language and run in VAX environment.

In this example, a diagnostic problem in relation to an elderly patient exhibiting forgetfulness is considered. Assume there are three experts who are capable of performing a diagnosis. The first expert contributes knowledge module $\mathsf { K B } _ { 1 }$ . sımilarly for the second and the third experts. In other words,

$$
\mathbf {S} = \{\mathrm{KB} _ {1}, \mathrm{KB} _ {2}, \mathrm{KB} _ {3} \}.
$$

Let the first knowledge module represent an expert who believes in an inexpensive and natural procedure for diagnosis. In contrast, the third module KB, represents an approach that prefers costly diagnostic procedures. The second module represents an attitude that is in between. The first approach is characterized as the "cognitive" one and the third as the “sophisticated internıst"' approach by Dietz (1991). Now, the preference of the payer authorities such as Medicare has been shifting away from the sophisticated internist to the cognitive approach. This question is the same as the one we address: How can the diagnostic system be tuned to match the change in preference of the environment?

For simplicity sake we assume that there are only two possible courses of action: the inexpensive action (IE) and the expensive action (E). Thus the set

$$
\mathbf {A} = \{\text { inexpensive   action   (IE).   expensive   action   (E) } \}.
$$

There are two possible evaluations from the environment: O.K., and not-O.K. Thus, the set

$$
\mathbf {E V A L} = \{\mathrm{O.K.,not-O.K.} \}
$$

Given a choice of action IE, the probability of O.K. response from the environment is 0.90 and the probability of not-O.K. response is. thus, 0.10. For action E the probabilities are 0.10 and 0.90. The ıdea of probability used is that of frequency interpretation. For instance. the probability of O.K. response of 0.90 for action IE implies that for 10 percent of time, symptoms of forgetfulness are not due to senility but due to, say, a tumor which could have been known ifan expensive brain scan (E) had been done (the action E). For this 10% of the time, simple methods would fail to arrest symptoms of forgetfulness and instead lead quickly to more severe symptoms associated with a tumor. A diagnosis of senility would be characterized as a faulty diagnosis in these cases with attendant problems such as complaints from patients. The CRITIC matrix is, thus, as follows:

<table><tr><td></td><td>O.K</td><td>not-O K</td></tr><tr><td>H</td><td>0.90</td><td>0 0</td></tr><tr><td>E</td><td>0 10</td><td>0.90</td></tr></table>

(Note: The system is not cognizant of the above matrıx values. The purpose of learning is to gain knowledge or an estimate of these values.)

Given a choice of KB, to work with, there is again a probabılity dıstribution as to which method or action would be chosen. This information is provided by the . 1DA/S matrix which is assumed to be as follows. (These figures reflect the confidence of each knowledge module regarding different actions.)

<table><tr><td></td><td>II</td><td>I</td></tr><tr><td> $KB_1$ </td><td>0.90</td><td>0.10</td></tr><tr><td> $KB_2$ </td><td>0.50</td><td>0.50</td></tr><tr><td> $KB_3$ </td><td>0.25</td><td>0.75</td></tr></table>

Based on the loss function $L _ { c }$ in §4.3, we know the loss function value associated with response O.K. is 0 and the value associated with response not-O.K. is 1.

We assume that the system begins with an equal preference among the three ${ \bf K B } , \mathsf { s }$ The system does not know what action from it would cause what responses from the environment and their associated probabilities. The purpose or need for learning arises in that the system needs to know the environmental preference and incorporate it in its preference structure over the ${ \tt K B } , \tt s$ . Therefore, at time $t = 0 , \mathrm { I I } ( 0 ) = [ \pi _ { 1 } ( 0 )$ $= 0 . 3 3 , \pi _ { 2 } ( 0 ) = 0 . 3 3 , . . . , \pi _ { | \mathbf { S } | } ( 0 ) - 0 . 3 3 ] ^ { \prime }$

Based on the general formula proposed in $\ S 4 . 4 .$ , we design a θ-optimal reinforcement scheme as the learning mechanism:

$$
\mathbf {h} _ {n} [ l e a r n e r _ {(i j) (m n)} (t) ] = \left\{ \begin{array}{l l} - 0. 2 5 * l e a r n e r _ {(i j) (m n)} (t) & \text {when response is O.K.,} \\ \frac {0 . 0 0 5}{| \mathbf {S} | - 1} - 0. 0 0 5 * l e a r n e r _ {(i j) (m n)} (t) & \text {otherwise.} \end{array} \right.
$$

This reinforcement scheme updates the LEARNER matrix as follows:

When the response is O.K.

(1) for ${ \mathrm { K B } } _ { \iota }$ , where $\jmath \neq K$

$$
\begin{array}{r l} \text { learner } _ {(i j) (m n)} (t + 1) & = \text { learner } _ {(i j) (m n)} (t) + \mathbf {h} _ {n} [ \text { learner } _ {(i j) (m n)} (t) ] \\ & = \text { learner } _ {(i j) (m n)} (t) * (1 - 0. 2 5); \end{array}
$$

(2) for ${ \mathrm { K B } } _ { \mathsf { A } }$

$$
\begin{array}{r l} \text {   learner } _ {(t K) (m n)} (t + 1) & = \text {   learner } _ {(t K) (m n)} (t) + \sum_ {i \neq K} 0. 2 5 * \text {   learner } _ {(i j) (m n)} (t) \\ & = \text {   learner } _ {(t K) (m n)} (t) + 0. 2 5 * (1 - \text {   learner } _ {(t K) (m n)} (t)). \end{array}
$$

Similarly, when the response is not-O.K.

(1) for ${ \mathrm { K B } } _ { f }$ , where $j \neq K$

$$
\operatorname{learner} _ {(i j) (m n)} (t + 1) = (1 - 0. 0 0 5) * \operatorname{learner} _ {(i j) (m n)} (t) + \frac {0 . 0 0 5}{| \mathbf {S} | - 1}
$$

where $| \mathbf { S } |$ is the size of the set of knowledge modules capable of solving the problem.

(2) for ${ \mathrm { K B } } _ { \kappa }$

$$
\operatorname{learner} _ {(i K) (m n)} (t + 1) = \operatorname{learner} _ {(i K) (m n)} (t) * (1 - 0. 0 0 5).
$$

The changing value of II(t) over time will represent learning if it increases the chance of the system over time choosing the KB, that has the maximum probability of getting the O.K. response from the environment. In our case the preferred knowledge module is $\mathrm { K B } _ { \mathrm { i } }$ . The table below represents the changing II vector:

<table><tr><td></td><td> $\pi_1$ </td><td> $\pi_1$ </td><td> $\pi_1$ </td></tr><tr><td>t=0</td><td>0.333</td><td>0.333</td><td>0.334</td></tr><tr><td>10</td><td>0.459</td><td>0.303</td><td>0.238</td></tr><tr><td>20</td><td>0.465</td><td>0.316</td><td>0.219</td></tr><tr><td>50</td><td>0.700</td><td>0.203</td><td>0.097</td></tr><tr><td>100</td><td>0.845</td><td>0.083</td><td>0.072</td></tr><tr><td>200</td><td>0.864</td><td>0.034</td><td>0.102</td></tr><tr><td>300</td><td>1.000</td><td>0.000</td><td>0.000</td></tr></table>

![](/api/attachments/ADXF9UBA/fulltext/images/16b5ad20d6e06afe9bee261244a91c8eef4d76d7d3872f1cd0ea39af6e3113be.jpg)  
FiGuRE 8– The I earning Process of an Adaptve Diagnosıs System

The above simulation values were obtained by taking 10 runs and averaging the π,(t) values. In each case by 300 runs the system had discovered that KB, was the most preferred knowledge module from the point of view of the response of the environment. The whole process is shown in Figure 8.

## 6. Concluding Remarks

Learning or adaptability is widely recognized as one of the most prominent abılities of any animate or mechanical intelligent system. Without this ability, current expert systems will still continue to fall short of being intelligent, and be unsuitable for highly dynamic decision-making environments. In this paper a conceptual model of adaptive expert systems functioning in a dynamic environment has been proposed as an attempt to lay a foundation for building adaptive expert systems.

This conceptual model is characterized by applying the learning automata approach to the traditional operational schema of expert systems. With our model, the adaptability of the expert system is powered by the inference engine after taking into account the evaluation made by the environment of the set of admissible plans for achieving the task posed by the end user. Since we are mainly concerned with an expert system working in a dynamic environment, the evaluation or feedback per se will be stochastic. Based on the evaluation, the inference engine will stochastically modify the status for the expert system. The modification of the status will trigger the generation of another set of admissible plans, with the expectation that the performance will be improved. The performance improvement is measured by the expected opportunity cost which is a function of the relative loss.

Our model can be classified as a supervised skill-refinement learning model. The skill refinement model proposed by Deng. Holsapple and Whinston (1990) differs from ours in the following aspects: it is self-organizing and does not assume the supcrvision of the environment; neither does it take into account the nature of the environment. Its learning behavior is achieved through internal modification, which is not stochastic, of rule strength.

One of the limitations of our model is that only one knowledge module is chosen each time and only one of thc admissible plans associated with the chosen knowledge module becomes the output of the system. Further rescarch is needed to generalize the model proposed in this paper. Another limitation is the assumption of the stability of the knowledge base during the learning process, i.e.. the knowledge base is not allowed to be modified during the learning process. Further research can also be conducted on the dynamic modification of the knowledge base during the learning process.

Though in this paper we have laid a foundation for building adaptive expert systems, further research is still needed to unify current machine learning models with our conceptual model so that adaptive expert systems suitable for decision-making in dynamic environments will be more achievable.\*

Acknowledgements. We would like to express our appreciation to the Associate Editor and the anonymous reviewers for their insightful and helpful comments.

\* Robert Blannıng, Associate Editor. This paper was recerved on July 13. 1990, and has been with the authors 5 months for 1 revision

## References

Aso, H. and M. Kımura, “Absolute Expediency of Learning Automata," Informaton Sctence 17 (1979) 91-112.

Baba, N , “Theoretical Considerations of the Parameter Self-Optimization by Stochastic Automata," International Journal of Contot, 27 (1978), 271–276

. New Topies in Learnng Hutomata Iheoty and Appltcattons Springer-Verlag, New York, 1985.

Bush. R R and F. Mosteller, Stochastt Aodels fot Learnng. Wilev, New York, 1958

Chandrasekaran, B and D W. C Shen, "Stochastie Automata Games," ILE Iransactons on Systems, Sctence, and Cyherneties, 5 (1969), 145–149

Chaudhury, A and A. B. Whinston, "Towards an Adaptive Kanban System," Internattonal Journal of Ptoducton Research. 28 (1990), 437–458

Davis, R and J King, \`An Overview of Production Systems." 1n Mac hnne Intelligenc e 8, E. W. Elcock and D. Michie (Eds.), Ellıs Horwood, Chichester. UK, 1977

Day, R. H., "Adaptive Processes and Economie Theory," in Adaptve Łconomte Models. R. H. Day and T Groves (Eds.), Academıe Press, New York, 1975

Dietz, J.. “Medical Proposals Look Like Bad News," lhe Boston Glohe, (August 27. 1991), 60

Deng, P. S., C. Holsapple and A. B. Whinston, “A Skill Refinement Learnıng Model for Rule-Based Expert Systems." IEEE EXPERT, 5 (1990), 15–28

Dungan, C. W. and J S. Chandler. “AUDITOR A Microcomputer-Based Expert System to Support Audutors in the Field," Expert Svstems, (October 1985), 210–221

Feigenbaum, E , P McCorduck and P. Nu. The Rtse of the Evpett Compan, Times Ptess, New York 1988

Gupta, M. M. and E Sanchez (Fds.), Fuzzv Informatton and Decston Ptocesses. North-Holland, Amsterdam. The Netherlands, 1982

Hansen, J. V. and W F. Messier, “A Prelimuinary Investigation of EDP-XPERT." tudttng A Joutna/ of Practice and Theory, (Fall 1986), 109–123.

Kandel, A and M. Schneider, “Fuzzy Sets and Their Applications to Artificial Intelligence," in 4vances in Computers Iol 28, M. C. Yovits (Ed.), Academic Press, New York. 1989.

Kelly, K P, G. S Ribar and J. J Willingham, "Interım Report on the Development of an Expert System for the Auditor's Loan Loss Fvaluation," 1n ludttung Synpoyn VII1, University of Kansas, Lawtence, KS, 1986.

Lakshmıvarahan, S., Learnung ,Ulgortthms Ieory and 1pptçattons, Sprınger-Verlag, New York, 1981. – and K S. Narendra, “Learning Algorıthms for Two Person Zero-Sum Stochastic Games with Incomplete Information," Mathematics of Operattons Research 6 (1981)

Lakshmivarahan, S. and M A. L I hathachar. "Optımal Nonlinear Reinforcement Sehemes for Stochastte Automata," Information Scien e, 4 (1972), 121–128,

and - . "Absolutely Expedient Learning Algorithms for Stochastic Automata," IEEE Transactions on Sy stems, Man and Cyhernettes, 3 (1973), 281–286

Logan, G D, "Toward an Instance Theory of Automatization  Pychological Revzew. 95 (1988), 492– 527

MeMurtry, G. J. and K S Fu. “A Variable-Structuie Automaton Used as a Multimodal Search Technique," 1EEE Transa(tions on Automatt Conto/ 11 (1966), 379–387

Meservy, R D., A. D. Bailey and P E Johnson, “Internal Control Ev aluatton A Computational Model of the Review Process." ,tudtting– 1 Journal of Practce and Hheor), (Fall 1986), 44– 74

Miehalski, R. S, J G. Carbonell and I M Mitchell (Eds ), Aachune Leatmng 1n Dttftual Intelligence Ipprodch, Morgan Kaufmann. I os Altos, CA, 1983

Minskv. M, "Steps Towards Artitciat Intelligence," in (ompiters ¿nd / houight E Feigenbaum and J Feldman (Eds.), McGraw-Hill. New York, 196

Narendia, K S. and S. Lakshmıvarahan. "Learning Automata-—A Critique," Journa of (ybernett and Infotmatton Stence, 1 (1977) 53–65

- and M A 1 I hathachar, "Learning Automata—A Suryev,"ILlI. Iansdcttons on Srstems, Man, aund ( vhernetes, 4 (1974), 323–334

and "On the Behavior of 1 earning Automata in a Changing Environment with Routing Apphcations," 1ELL l'ransactons on Srstems, Man. and ( vbernetes. 10 (1980), 262–269

, E. Wright and L. G. Mason, “Application of 1 earníng Automata to felephone T raffic Routing," HEE Transactons on Svstemns– Man, and Cvhernetes, 7 (1977), 785–792

Negonta, C V., “Fuzzy Sets in Decision Support Systems." Humnan Srstems Manugement, 4 (1983), 27-33

Newell, A and P. S Rosenbloom, "Mechanisms of Skill Acquisition and the Law of Practice," in ( ognuttve Sht//s and 1 hetr tpphicatton. J R. Anderson (Fd.), Erlbaum Associates, Hillsdale NJ, 1981

Poltakıs. P and S M. Weiss. "{ sıng Fmpirical Analysis to Refine E pert System Knowledge Bases." tuticial Intelligene, (1984), 23–48

Rumelhart, D. E., J L. MeClelland and the PDP Research Group, P'aaflel Disttthuted Processing Lxplorattons mn the Atcrostructure of Cogntion I ol 1– Foundattons. MIT Press Cambridge, MA, 1986.

Shapiro, I J. and K. S Narendra, “Use of Stochasue Automata loı Parameter Self-Optımızaton with Multimodal Performance Criteria." HEEl Iansactions on Srstens, Soence. and Cybernetes. 5 (1969), 352–360.

Shrager, J . 1 Hogg and B A. Huberman, “A Graph-Dvname Model of the Power 1 aw of Praetiee and the Problem-Solving Fan-Effect," Sctence. 242 (1988), 414–416.

Sumon, H A., “Why Should Machines Learn?" in Mac hune Leatmng 1n Attttctal Intelltgence Ipproach, R S. Michalskı, J (i Carbonell and I M Mitchell (Fds), Morgan Kaufmann. 1 os Altos, CA, 1983

Sleeman. D , P. Langley and T M Mitchell, “I earnıng from Solutton Paths An Approach to the Credit Assignment Problems," 11 Magazme 3 (1982), 48–52

Srikantakumar, P R and K. S Narendra. “A I earning Model fot Routing in Ieiephone Networks," S1 1M Journat on Control and Opumuzution– 20 (1982), 34-57

Steinbart, P , “Materialty A Case Study Using I xpert Systems." tcotntng Reveu (January 1987). 97-116

Varshavskı, V I and I P. Vorontsova, "On the Behavior of Stochastı Automata with Variable Structure.,Automatton and Remote (ontrot, 24 (1963)– 327–333

Viswanathan. R and K S Narendra "A Note on the I inear Reintorcement Scheme for Variable-Structure Stochastie Automata," 11 11: Iransacttons on Srstems. Man and Cvhernete, 2 (1972), 292–294

Waterman, D. A and f Hayes-Roth “An Overview of Pattern Direeted Inferenee Sş stems." in Pattetn-Diredted Inference S) stens, D) A. Waterman and F. Haves-Roth (Eds.), Academıe Press, Orlando, FL, 1978

Wilkins, D. C.. “Knowledge Base Refinement as Improving an Ineorreet and Incomplete Domain Theory," in Machine Leanng tn 1rtftcial Intelligence Ipp"oadh 1 of III Y Kodratoff and R. Michalskı (Fds ), Morgan Kaufmann, San Mateo, CA. 1990

Zadeh, I A., "Fuzzy Sets," Intonmatton and ( ontrol, 8 (1965), 338 -353

– , “The Role of Fuzzs 1 ogie in the Management of Uneettaintv in Lxpert Sy stems " Fuzzr Sets and Svsten>, 11 (1983), 199- 228

Zimmerman. H J , L A. Zadeh and B R Gaines (Eds ). Fuzzr Sets ad Dectson Dna/rss, North-Holland. Amsterdam, 1 he Netherlands, 1984
