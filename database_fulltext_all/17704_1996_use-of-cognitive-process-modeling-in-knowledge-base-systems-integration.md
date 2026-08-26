---
otero_id: 17704
otero_key: "5QZ44WYZ"
title: "Use of cognitive process modeling in knowledge base systems integration"
authors: "Ravi C. Vellore; Arun Sen; Ajay S. Vinze"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00015-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Use of cognitive process modeling in knowledge base systems integration

Ravi C. Vellore, Arun Sen \*, Ajay S. Vinze

Department of Business Analysis and Research, GSB and College of Business Administration, Texas A&M University, College Station, Texas, TX 77843 USA

Received 27 July 1993; revised 15 April 1995

## Abstract

Large and complex knowledge based systems (KBSs) are becoming increasingly common. Current surveys of these systems reveal that they are designed in four different ways: federation, emulation, alliance, and distribution. Each approach has an explicit way to integrate the essential components of the KBS. Unfortunately, the software design process to integrate components in each approach is still ad hoc and informal. As such, it is very difficult to “match” a problem description with a specific integration approach. In order to be more methodical, we propose a cognitive process model (CPM) based technique. The cognitive process model abstracts the cognitive tasks of identification, conceptualization, and formalization of the experts into one common framework. We have chosen the domain of model formulation to explain the CPM-based technique. The architectural characteristics needed to implement an integrated knowledge based system are derived from this model. Some implementation details are also shown to attest the viability of the CPM-based design.

Keywords: Integration; Integration of knowledge based systems; Cognitive process model; Process model; Large KBSs

## 1. Introduction

Knowledge based systems (KBSs) [56] have made tremendous strides since they first appeared in the form of expert systems several decades ago. Typically, these computer-based systems support various tasks in narrow domains that would have been otherwise performed by human experts. Research in artificial intelligence has traditionally favored “a reductionistic approach by decomposing the intelligent behavior into knowledge representation, search-intensive problem solving, knowledge-intensive experience, concept acquisition from examples,...” [5], p. 241. Although, this approach of divide and conquer may have been historically quite appropriate in providing useful results, it has failed to provide an unifying problem solving framework. This notion of finding unifying problem solving framework, and an ever increasing interest to support larger problems in complex domains have spurred researchers to look into integration of knowledge based systems.

In the literature, we find numerous attempts have been made to integrate a knowledge based system with other systems (primarily with database management systems) and with other knowledge base systems. Corkill [7] identifies three integration approaches embedding, distribution and emulation. Extending on the effort by Corkill, and based on our observations from the protocols we use a four category setup for classifying integration efforts: federation, alliance, emulation and distribution. The reason for this change is our further subclassification to Corkill's category of embedding. In particular, embedding is divided into soft-embedding (federation) and tight embedding (alliance). More detailed description for these is provided below. Each integration approach has a specific philosophy of integration. We base our descriptions of these approaches on the SMP paradigm [35]. This paradigm consists of three components: structure, mechanism and policy. Structures are “objects or object aggregates that represent the software under development” [35], p. 284. Mechanisms are tools and operations on the structures within the constraints of the environment. Finally, policy is a set of rules, guidelines and strategies that the environment imposes on the development effort. The advantage of using this model is that it distinguishes intuitively those aspects that are useful in comparing and contrasting software environments. The SMP paradigm is not specific to any particular application or architecture.

Federation: The integration through federation is defined as an approach that preserves the identity of each component to be integrated. $^{1}$ For example, a KBS essentially devoted to the reasoning functions can be integrated this way with a database management system (DBMS) managing a database [58]. One advantage of this approach is the possibility of using existing systems. However, it may be difficult to separate in a precise way one activity from the other at the time of implementation. For example, we may find it very difficult, while implementing an integrated KBS-DBMS using this approach, to distinguish the deductive phase from the data retrieval phase. Also, other problems such as consistency may arise if the data collection from the database is used while the original version is getting updated [30]. An example of this approach can be seen in Chang and Walker [6] who have designed PROSQL that couples Prolog with SQL/DS. The federation architecture can be characterized in terms of SMP as follows:

## Federation Architecture

$= (\{\text{traditional file structures / database schemes}\}, \{\text{file access programs / database languages, interfacing routines, analytical tools, ...}\}, \{\text{independence preserving tool policies}\})$ .

Emulation: The integration through emulation is defined as an approach that uses a base language to implement other frameworks. This approach requires considerable effort in order to implement all the desired frameworks in a single representation [7]. For example, the integration of a Lisp based sub-system with a C based sub-system, for a system written with C as the base language, recoding will be required for all Lisp functions. As a result, performance will suffer as the frameworks are implemented in the base language and not in their original implementation language. We find other examples of this approach in extending Prolog to handle database operations [42], and in supporting rules by database systems [8,48]. The emulation architecture is very similar to the federation architecture in terms of SMP. The key distinction between the two is in the policy used. For emulation, the implementation is done in one base language, as compared to the federation approach where the independence of the languages is preserved.

Emulation Architecture

$= (\{\text{traditional file structures / database}$ schemes}, $\{\text{file access programs / database}$ languages, interfacing routines,

analytical tools, ...}, {single base

language oriented tool policies} .

Alliance: The integration through alliance is defined as an approach where the focus is on integration of various policies that an application may need. Unlike the other architectures, the alliance architecture allows the use of a diverse set of policies to address a problem situation. As is illustrated later in this paper, the model formulation process requires opportunistic control and case based reasoning. The policies need to be unified under the aegis of a common structure and a set of support tools. Other examples of an alliance architecture are SOAR [40], PRODIGY [5], THEO [31], TETON [50] and others.

Alliance Architecture

$= (\{\text{internal representation}\}, \{\text{context}$

identification, structure development,

synthesis, instantiation,...}, {hierarchical

control/opportunistic control, meta

control, model reason maintenance, case search policies,...}).

Distribution: The integration through distribution is defined as an approach where the integration is achieved through a coordination of independent problem solvers (KBSs or DBMSs) that are placed in different machines. The coordination among the network of problem solvers is achieved through negotiations and other activities. A key aspect for most of DAI (distributed artificial intelligence) and CDPS (cooperative distributed problem solving) systems that follow the distributed integration is their reliance on sophisticated communication mechanism to achieve the coordination for assigning tasks, integrating solutions, and others among various problem solving nodes $[11,20]$ .

Distribution Architecture

$= (\{\text{distributed objects}\}, \{\text{network}\})$

mechanisms}, {network oriented policies,

eg., high reliability and availability} ).

It is quite clear to the researchers now that traditional knowledge base systems, designed to be modular and narrow in scope, are limited to solve complex problems $[7,9,19,56]$ . We need to go beyond these systems and study “integrated frameworks.” However, matching a problem with a right kind of integrated architecture (federation, emulation, alliance, or distribution) is a formidable task. This is because the matching process is very informal and ad hoc. In our research to create a model formulation consultant called MODELER, we have tackled this matching problem using a process-oriented model called Cognitive Process Model (CPM). In this article, we define the CPM, discuss how to create such a CPM for model formulation activities, and describe how CPM for model formulation activities has been used to integrate different KBSs in the MODELER project. $^{2}$

The SMP attributes used to distinguish each classification describe its salient features. It should be noted however that for certain situations some overlap between the categories is permitted. For example, case-based reasoning and opportunism are included as policies in the alliance architecture. These attributes can also be in KBSs that are integrated using a distribution approach.

Section 2 briefly describes the matching process. In order to create a formal approach, we have collected verbalization data from the experts performing the model formulation process. They are then encoded into protocols. These protocols are then analyzed using a cognitive process model (CPM) which is described in Section 3. In Section 4, the architectural characteristics for MOD-ELER are derived from the CPM. These considerations are then used to implement the MOD-ELER system. Some implementation details and a sample run of a session (Appendix 1) are also given to show the viability of the CPM-based design. Finally, in Section 5, we summarize the entire analysis and design process. Some future directions are also provided.

## 2. The matching problem

To design large and complex knowledge based systems one needs to understand how to arrive at an architecture. The derivation of an architecture is typically an art, and is obtained by analyzing the problem domain. This gets more difficult as in many situations, the software design is still an ad hoc process. Given a set of requirements, usually in natural language, an informal design of architecture is prepared. Coding commences and the design is modified as the system is implemented. When the implementation is complete, the design has changed so much from its initial specification that the original design document is totally inadequate description of the system.

This phenomenon is more pronounced in prototyping and in “exploratory programming” approach ${}^{3}$ [47] to develop a complex KBS. In the complex KBS implementation, the informal behavior is observed more in matching the problem characteristics with the KBS architecture. With a goal to formalize this matching process, Hayes-Roth et al. [19] offer three stages: identification, conceptualization, and formalization. In the identification stage, the important aspects of the problem are characterized. This involves identifying the participants, problem characteristics, resources needed, and goals. The problem characteristics include issues like the class of problems, important subproblems within a problem, their interrelationships, solution characteristics and others. The goals include formalization of otherwise informal set of practices, distributing scarce expertise, and so on. In the conceptualization stage, repeated interactions between the knowledge engineer and the domain expert take place to understand the types of data needed, the strategies to be used, the types of subtasks, the types of objects in the domain, and others. In the formalization stage, the key concepts, subproblems, and information flow characteristics isolated during conceptualization are mapped into more formal representations based on various knowledge-engineering tools or frameworks. The important factors in this stage include: determining the hypothesis space, uncovering the underlying model of the process, and understanding the characteristics of data. The hypothesis space provides us with clues – whether or not it is finite, whether it consists of prespecified classes, whether or not it is useful to consider the hypotheses hierarchically, and so on. Uncovering the underlying model of the process may suggest a behavioral model of reasoning, rather than a mathematical model. The study of data can lead us to the type of relationship they may possess.

Although describing the matching process by three stages is a step in the right direction, the process is still sufficiently vague. This is echoed by Hayes-Roth et al. [19], p. 211, while describing how to choose a expert system tool for a problem.

"One of the most difficult aspects of choosing an appropriate tool for a knowledge-engineering application is matching the problem characteristics to the tool features. The features needed in the tool depend strongly upon three things: the characteristics of the problem domain, the characteristics of the likely approach to solving the problem, and the desired characteristics of the expert system to be built."

The matching problem becomes more of an issue while determining the right integration architecture for a complex problem. This is because most of the large KBS design is done in teams. The requirements described in a natural language can easily be misunderstood by different members of the knowledge base team. Also, the extent of knowledge base integration may not be very obvious to everybody. This includes:

\- What type of integration philosophy is suitable for the problem?,

\- what knowledge base paradigms need to be integrated?, and

• how they should be integrated?

We propose that a model is needed, using the notion of process model [47], that captures the characteristics of the problem domain collected from the above three stages. As this model would abstract the cognitive tasks of the experts needed to solve a problem, we call it a cognitive process model (CPM). Once such a model is created, it can then be used to derive the architectural information of the KBS.

## 3. Creating a cognitive process model (CPM)

We define the CPM as a model that captures the basic cognitive processes of experts. A problem, according to Reitman [37], can be represented by a triple $(X,Y,\Rightarrow)$ where X is the existing state, Y the desired state, and $\Rightarrow$ represents the transformations or steps that may be applied to the states in order to move from one state to another. In the minds of experts, this $\Rightarrow$ forms a set of cognitive tasks. The cognitive process model (CPM) unbundles these cognitive tasks into knowledge sources and a common data structure used by these knowledge sources. Once the model is decried, it can then be used to develop large and complex KBSs.

Creating a cognitive model and then using it for software development involve several steps. They include:

Step-1: Collect verbalizations of modelers;

Step-2: Encode the verbalizations to form protocol sets;

Step-3: Analyze one protocol set to create a CPM;

Step-4: Test the sufficiency of the CPM with the rest of the protocol sets;

Step-5: List out the observations about the underlying the process that are evident from the CPM; and

Step-6: Derive the architectural considerations from these observations.

We describe the mechanics of these steps by discussing their use in designing a model formulation consultant called MODELER. Each of these steps are discussed below.

3.1. Collect and encode verbalizations from modelers (Steps 1 and 2)

The expert modelers with a Ph.D. degree in management science were observed. At the start of the process, each participant was given a simple exercise of multiplying some numbers to make them comfortable with the process of verbalizing while thinking. Additionally, the subjects were provided access to a computer, a blackboard, and a paper and pencil. Any use of these media were included in the recording of the verbalizations. Upon completion of the practice session, the subjects were instructed on the problems that they were going to be attempting. Each was given a set of three problems from the production planning area. One such problem is shown in Fig. 1. Simpler problems were used to keep the length of verbalization to a reasonable level and to capture details of the verbalization of the experts. All verbalizations were taped. The recorded verbalizations were first transcribed and then encoded into protocols (Fig. 2). The encoding process was conducted using prescribed guidelines [14]. The process entailed extracting appropriate statements from the transcription that convey heeded thoughts and encoding them. In case of fragmented segments, the context prior to and following that segment is utilized to remove any uncertainty in the coding. In order to reduce the encoding bias caused by prior knowledge the coder was not informed of the goals of the study [14].

## 3.2. Analyze protocol set to create a CPM (Step 3)

Verbalizations are first encoded into protocol sets. A cursory look at a protocol set (Fig. 2) shows that the control used by the experts to manage the model formulation tasks is opportunistic [18]. Additionally, the model construction activities seem to use case base reasoning [38,45]. This possibility is indeed different from the segregated system advocated by the current system architectures (predefined types [2,4,5,9,10,12,15, 21–23,25–29,32,34,36,45,53] and strategic control types [43,53–55]). Clearly, the problem needs some kind of “integration” of a case reasoning with an opportunistic control. But how do we integrate these two? Of the four different integration techniques described in Section 1, which one is “best match” for supporting $^{4}$ the protocols listed in Fig. 2? In order to answer these questions, we propose a cognitive process model (CPM).

Based on literature and supported by an initial scan of the verbalizations, the thesis of this section is that the model formulation process is essentially an opportunistic problem solving activity that relies on past cases. This means that during the formulation process the subject's formulation decisions and observations suggest various opportunities for formulation development. The subject's subsequent decisions follow up on selected opportunities. Sometimes the decision-sequences follow an orderly path and produce a neat hierarchy. However, some decisions may not follow such an orderly fashion. This process gets further complicated due to the subject's use of past experience in the form of cases.

In order to test this idea, a cognitive process model based on $[30,31]$ is created. Fig. 3 describes this modified CPM. We assume that the model formulation process can be described using a structure called the formulation blackboard. The blackboard approach ${}^{5}$ was preferred to other alternatives because this approach is inherently modular, provides a wide range of capabilities for controlling the problem solving behavior, and is flexible as different parts of the problem may be processed in parallel $[13]$ . The blackboard is used by many cognitive specialists (called formulation specialists) in the formulation process with each specialist making tentative decisions for incorporation into a tentative formulation.

The proposed model extends earlier work done by Vinze et al. [53] and is partitioned into six conceptual panels that perform varying tasks based on the decision focus-operational, tactical and strategic [18]. The model proposed by Vinze et al. [53] addressed model formulation process concerns from a “first principles” approach and consisted of five panels. The CPM shown in Fig. 3 adds memory panel to original model [53]. As explained earlier, scanning of our verbalizations indicated that in addition to opportunistic behavior demonstrated by the subjects, there was a tendency to rely on past experiences. The role of experience in model formulation was not accounted for in the earlier cognitive models [53]. The memory panel serves as a repository of experiences of the modeler.

The CPM partitions the blackboard into several conceptual panels that perform varying tasks based on the decision focus. The problem panel contains decisions that indicate the understanding of the current problem description. The understanding of the current problem description, for the most part, is guided by the solution panel where the retrieved past similar case from the memory panel helps guide the process.

The specific design and solution panels contain decisions that relate to memory reminding, access mechanism for recall of past cases, and modification strategies for adapting past cases to help model current situations. Learning from case successes and failures takes place when the formulated model is evaluated for conformity to the current situation and the working model with the assigned index is then stored in the memory panel. These panels assist in improving the degree of expertise. They also serve to develop and maintain an adaptive memory organization.

The control and global design panels contain higher-level decisions that relate to the strategies and their steps adopted for solving a problem, allocation of cognitive resources and others that help measure the case based designer's understanding of the problem. They also set global design policies and evaluation criteria that check the applicability of the developing formulation to the current situation.

Control panel. The control panel makes decisions about the direction of the formulation process. There are three levels in the control panel which are arranged in a hierarchy. The decisions made at these levels form a hierarchy with the highest level being the priority level. The priority

An imaginary economy has six distinct geographical locations each has its own specific economic functions, as follows:

<table><tr><td>Region</td><td>Function</td></tr><tr><td>A</td><td>Food Producing</td></tr><tr><td>B</td><td>Manufacturing-Machinery</td></tr><tr><td>C</td><td>Manufacturing-Machinery and consumer durables</td></tr><tr><td>D</td><td>Administrative</td></tr><tr><td>E</td><td>Food-Producing</td></tr><tr><td>F</td><td>Manufacturing-Consumer durables and nondurables</td></tr></table>

The regions also have the following annual requirements (all quantities measured in tons):

<table><tr><td>Region</td><td>Food</td><td>Machinery</td><td>Consumer durables</td><td>Consumer nondurables</td></tr><tr><td>A</td><td>5</td><td>30</td><td>20</td><td>30</td></tr><tr><td>B</td><td>15</td><td>100</td><td>40</td><td>30</td></tr><tr><td>C</td><td>20</td><td>80</td><td>50</td><td>40</td></tr><tr><td>D</td><td>30</td><td>10</td><td>70</td><td>60</td></tr><tr><td>E</td><td>10</td><td>60</td><td>80</td><td>20</td></tr><tr><td>F</td><td>25</td><td>60</td><td>60</td><td>50</td></tr></table>

Using the national railroad, shipping costs are \$1/ton per 100 miles for all hauls over 100 miles. Within 100 miles, all goods are carried by truck at a cost of \$1.25/ton per 100 miles (\$1/ton minimum charge). the distance (in miles) between regions are as follows:

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td></tr><tr><td>A</td><td>---</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>B</td><td>500</td><td>---</td><td></td><td></td><td></td><td></td></tr><tr><td>C</td><td>200</td><td>400</td><td>---</td><td></td><td></td><td></td></tr><tr><td>D</td><td>75</td><td>500</td><td>150</td><td>---</td><td></td><td></td></tr><tr><td>E</td><td>600</td><td>125</td><td>350</td><td>550</td><td>---</td><td></td></tr><tr><td>F</td><td>300</td><td>200</td><td>100</td><td>400</td><td>300</td><td>---</td></tr></table>

Assume producing regions can meet all requirements, but that, due to government regulation, food production in sector A is restricted to half that of sector E.

Formulate a linear program that will meet the requirements and minimize the total transportation cost in the economy.

Fig. 1. A multi-commodity transportation problem.

22. This could be a rather large model with that approach. Look at the contribution coefficients.

10. So our objective function is to minimize total cost of transportation. , )

8. So theres a cost function you can identify for per ton that may require calculation for the coefficient.

And thats 5 fourths and 3 fourths, thats 15 fourths, thats 3.75. And thats 6, 3, 4, 5, 1.25, 2, 1.5 . . .

9. Assume producing regions can meet all requirements but due to govt regulation, food production in sector A is restricted to half of sector E.

29. Ok, the formula for shipping costs are a dollar a ton per 100 miles within a 100 miles or carried by truck . . . (read from problem) . . . 1.25 per 100.

30. So this is over a hundred miles so thats 5, this is 2. And this is below a 100 miles 1.25 per 100 miles.

16. And food can come from A and E.

27. If its going to be extremely detailed, you can go as far as to show ...

1 This is an input/output problem.

2. We are going to need a constraint for each grid sector

3. Then you basically determine how much comes out of each sector.

4. So its kind of a pattern problem.

5. The way you first look at it is to remember it is a typical problem of that type. So basically there are requirements for 6 they call them regions, but they really aren't. Oh, I see, the regions have assigned functions so that it is not the kind of problem where every region is economically viable. They specialize a lot I guess. If region 1 has a reqm., I am not sure exactly what the ...

6. Every time region 1 produces something, it requires 5 units of food, 30 units of machinery, 12 consumer durables \*\*\*\*\* of consumer durables.

7. Thats 4 and theres 6 regions here. OK because A & E are both food producing. And ok thats food, manufacturing machinery. Ok B & C both are manufacturing machinery but C also does consumer durables. And so there F that also does manufacturing machinery and D does administration I guess. So then you got a table of annual requirements and times using the national railroad. Shipping costs are a dollar per ton per 100 miles \*\*\*\*\* over a 100 miles, within a 100 miles if the goods are carried by truck at a cost of dollar and quarter per ton per 100 miles. A \$1 per ton minimum charge, distance is in miles within regions.

11. To identify the variables of the decision itself, essentially its how much to ship between regions.

12. Now where on here does it tell you how much food A produces so that you know the amount available.

13. I guess you assume its an unconstrained deal so that you dont need a constraint.

14. But you can send food, just looking at food.

15. You know the demand for food, its 5A, 15B, 20C, 30D, 10E, 25F.

17. So I guess maybe we can try transportation problem on the thing.

19. Say you have 4 matrix possibilities for food of source.

20. And demand and really all you want to memorize is the tons \*\*\*\*\* It doesn't matter what kind of stuff it is at all.

21. So from A you can send $*$ $*$ $*$ $*$ $*$ $*$ $*$ $*$ $*$ $*$ $*$ $*$ $*$ $*$ $*$ $*$ $*$ $*$ $*$ $*$ $*$ . Everything coming into A for food has to be greater than or equal to 5.

25. Ok, so we need how much access to send \*\*\*\*\* from A to A. And thats 0.

26. You need to know how much it costs for this entire matrix. You need the coefficients of the function.

Fig. 2. The complete verbalization protocols of expert-2 for problem 1.

32. So this then would be the objective function to minimize the transportation matrix.

33. Now the problem is to make sure that there are constraints to force it to come up with the required foods etc.

34. Where this would be i and this would be j, we could come up with an objective function where contribution coefficients are this matrix element times the quantity shipped over that route.

35. Then for food A to A plus E to A has to be greater than or equal to 5. 1/1, GE, 5)

36. There is a whole series of these things.

37. A to B + F to B has to be greater than or equal to 15. And since that's all A and E . . . E not F.

38. A to A + E to A has to be greater than or equal to 5, B to B + E to B has to be greater than or equal to 5.

39. So theres a whole series of these for each region of consumption. And its pretty systematic.

40. Take this nmatrix times that matrix and this is going to go on and you have a constraint for each of these 24 elements.

41. And an additional constraint because there was a restriction that said you had to have . . . Due to govt regulation, food production in sector A is restricted to half of that of sector E . . . So the sum of all of these variables coming out of A - and theres 6 of them - has to be less than or equal to .5 of all of these variables, the whole term, half of the whole term coming out of E. So that will take care of food - there are 7 constraints. Put some dots here.

42. You have to do the same for machinery except thats its a little bit easier. There is going to be another catch because C and F have multiple outputs so therefore the total amount. $*$ $*$ $*$ $*$ $*$ $*$ $*$ I could model this as transportation but the complication would be if machinery manufacturing, consumer durables could cause a problem because the way a programming model would put a . . . Well what we could do is to create extra variables.

43. We could make it 8 variables instead of 6 were coming out of C you got 2 variables. You got a variable representing machinery coming out of C. And you got a variable representing consumer durables coming out of C. So if you look at machinery, you would have CM and FM.

44. So for machinery. at region A you got to have greater than or equal to 30.

45. You can supply A in a variety of ways. You can supply it with E to A, C1 to A, F1 to A . . . So that mess has to be greater than or equal to 30. This goes on for 6 constraints and you have a whole series of variables that are created now.

46. There would be - up here we had 12 variables - here we will have 18 variables.

47. Ok, for consumer durables, we will create a variable called - well we got 2 sources -C2 and F2.

48. So we'll have a series of 6 constraints for the 6 requirements - greater than or equal to 20, etc. And C2 to A + F2 to A. And is there any other source of consumer durable sources. No thats it - the sum of those has to be greater than or equal to 20 and that goes on 6 times

49. So thats another 12 variables. And then we have constraints for consumer non-durables. Ok, I dont see any consumer non durables. Ooh F - so got a third, a bunch of stuff coming out of F.

50. So that goes to, thats the only variable, so there would be 6 of these. The only source so there are only 6 of those. And those are greater than or equal to these right hand sides. And thats another 6 variables.

51. And so we end up with a model with 48 variables.

52. The obj func is to minimize the transportation costs for all of those.

53. And you can get the contribution coeff from this matrix down here.

54. We've got 12 . . . what 6 . . . we've got 24 variables forcing production or delivery to each of these 6 regions for: each of the 4 products.

55. We've got one extra constraint for the requiring food production in sector A to be half of that of sector E. So thats one additional constraint.

56. The last thing to check, since you are minimising the cost function, will be a lot of these 48 variables that will have duplicate costs . . . Depends upon - all you need to know is what demand-source combination .

. . There will only be a limited number of contribution coeffs. 15 of them with a bunch of 0's, but they would be \*\*\*\*\* by a number of variables.

57. Now, the only catch is . . . But it looks like that ought to be the model. So what I would do at this stage is to put this model into LINDO or some other computer package that does linear programming and solve it. The big catch with linear prog is that there are a million different ways to model any one problem. And the important thing is to run the model you've got and to see if the answer makes sense. If the answer doesn't make sense, that's the fastest and safest way to double check to see if you left something out. So the solution process does'nt end at the model at all, its an initial draft more or less. The solution process is getting the answer from the computer and seeing whats wrong with it.

Fig. 2 (continued).

level helps resolve conflicts when several similar past cases are accessed. It also helps organize the events in the problem-solving process. Focus level indicates the current focus of attention with respect to the formulation process. The schedule level helps resolve any conflicts among competing “specialists” within a given priority and focus.

Global design panel. The global design panel makes decisions about the major strategies and approaches used to formulate models. There are five levels of abstraction in this panel. Unlike the levels for the control panel, levels for global design are not organized hierarchically. The levels describe aspects of the formulation process. The problem definition level emphasizes goal identification and available resources. An understanding of the problem statement and its context is reflected in this level. The problem-solving approach indicates the broad approach the expert uses to help understand and categorize the problem, such as: first principles and case-based. Additionally, it helps the control panel focus on the chosen problem-solving approach. At the policies level the global constraints that need to be satisfied are specified. For example, in a LP model formulation the model assumptions of linearity, additivity, proportionality and divisibility should be satisfied. The policy might be not to waste cognitive resources, ensure accuracy, etc. These policies dictate different meta-goals such as whether an expert should combine plans, or choose least costly plan, or resolve goal conflict, etc. These meta-goals, in turn, are used to design meta-plans such as schedule common sub-goals first, divide task, integrate plan, and so on.

To summarize, decisions made in the global design panel reveal the design approaches of the expert, the policies that they set, the consequent meta-goals set and meta-plans used to monitor the progress and successful conclusion of the formulation process from start to finish.

Specific design panel. The specific design panel consists of four abstraction levels. The levels form a hierarchy with each level being a refinement of the previous one. For example, at the intention level, a designer attempts recalling a past similar case to solve the current problem. Other intentions may be to identify case structural features, case specific features and the case contextual history. At the next lower level of strategy the designer formulates the reminding mechanism that needs to be used. At different points in the problem-solving period the strategy may vary from using the inference mechanism from a single past similar case to inference mechanisms borrowed from different cases categorized under a prototypical case. For instance the expert may be familiar with transportation problems and not very familiar with inventory problems. In this case if the current problem is an inventory problem the expert may call upon a generalized transportation case and see whether it can be adapted to the current situation. The tactics level makes decisions about how to execute the chosen strategy. In a case based approach, this might be the composing of appropriate features into an index that can be used to access a past case. Other tactics level decisions might be to recall the explanation of past case outcomes to assess applicability of those principles. Evaluation level performs the function of testing. The recalled case is analyzed on the basis of its history and a decision made to record the recalled case in the solution panel.

![](/api/attachments/5QZ44WYZ/fulltext/images/3a847c61285d57d001bdfdb96fdb88475d92813d5bf24c436de73149ec5838ce.jpg)  
Fig. 3. A cognitive process model for model formulation.

Problem panel. The problem panel contains the understanding of the current problem description. This understanding is represented in five abstraction levels. Each level can be interpreted for instantiation of the levels in the solution panel. The problem type and problem class levels provide the inferred classificatory and other explanation based information that helps the expert categorize the problems into transportation, product-mix, etc. in the domain of production planning. Problem description level contains the data abstracted from the problem statement. The problem analysis level contains the analysis of the current problem and works closely with past similar cases available in the solution panel. Solution elements at this level may include the decision variables identified, constraints and other elements in the current problem and past case that could be useful in the final solution plan. The evaluation level decisions determine whether the feature abstraction process from the problem statement is complete. It may check for differences between the current situation and the past recalled case. It helps the solution panel in determining the need for reorganizing the memory store of cases.

Solution panel. There are five abstraction levels in the solution panel. The levels in this panel are instantiated by both the specific design panel and the problem panel. Past similar cases are tentatively placed in this panel to determine applicability to current situation. The tool class level show decisions about the tool selected for model formulation. For instance tool class could be optimization tools. Another type of solution element at this level may be the problem label from a recalled case. At the tool type level the expert narrows his choice of a tool. The tool type may be dictated by computational efficiency issues or other considerations. The domain of production planning is replete with several algorithms for specific problem structures. For example the transportation model may be warranted based on the problem structure. Model specification level reflects the qualitative design adapted from the past case. Solution elements at this level may include decision variables, constraints, objective function, and model parameters obtained from the past case. As the problem-solving process proceeds and understanding of current situation increases, the model specification will reflect the evolving qualitative design for the current problem. The Model instance represents the algebraic formulation of the qualitative design. Other instances could be the algebraic methods/“tricks” used by experts to translate the qualitative design. The evaluation level in the solution panel serves the purpose of simulating the formulated plan and ascertaining the completeness of the model formulation. It also serves the purpose of learning from the current case and making decisions about when to change the understanding of the planner's memory.

Memory panel. The memory panel supports the model formulation process by providing a store of experiences. There are five levels of abstraction in this panel. The levels in the problem panel are not organized hierarchically and they depict the different forms of knowledge structures. In addition to the different knowledge structures there is an evaluation level where most of the screening decisions are made during retrieval and storage. The indexing rules level identifies the various ways cases, explanations, and domain knowledge are assigned indexes for easy retrieval. The indexes provide the different reminding mechanisms such as feature-based reminding, goal-based reminding, explanation-based reminding, failure-based reminding, etc the case based designer utilizes to determine whether there are any similar past situation in the memory panel. The case level shows the structural elements of the case. Some of the elements that describe a case are: features, different types of links that associate the features with the case; and, the explanation associated with the links. The explanations level provide holistic assessments of situations. This may take into account all features in a case plus additional idiosyncratic aspects from a situation to provide explanations for particular choice of a model or a case. At the domain knowledge level the case based designer stores information about basic models, their features, mapping rules (for transforming qualitative models into mathematical formulae), and other domain rules. The knowledge is stored using different strategies such as categorization, forgetting, etc to help contain the potential combinatorial explosion. Finally, the evaluation level specifies guidelines and rules for retrieving the best case, for storing formulated models, for assigning indices, for assigning explanations (if warranted), and any modifications of knowledge structures.

Cognitive specialists. The opportunistic framework assumes that expertise can be decomposed into individual specialists or knowledge sources. Specialists are a set of condition-action rules that generate decisions during the formulation process.

The condition component describes the circumstances under which the specialist can contribute to the formulation process. This is done by scanning a specific level of the blackboard panel in each control cycle, and in case of a match, the specialist contributes by way of the encapsulated content of the action part of its rule. The action may include factual information, or may involve an arbitrary amount of computation, but the result always generates a new decision or modifies an existing decision. During the model generation phase the decision usually takes the form of questions formulated with the help of the retrieved past case.

The different types of specialists include: domain-level plan developers that know about optimization, production-planning, etc.; and strategic operators that look for similarities to past stored cases, standard approaches to solving optimization problems such as: first principles, case based etc. For example, a case retriever specialist may scan the problem description looking for identifying features that could be used to extract a suitably matching case from case memory. The retrieved case is then placed in the solution panel where another specialist case unraveler scans the tool type for evidence of a similar case from case memory and proceeds to unravel the retrieved case into its qualitative elements. A partial list of these cognitive specialists is provided in Table 1.

Controlling the formulation process. The control process guides the formulation process through a series of “cycles” during which various specialists execute their actions. At the beginning of each cycle, the specialists that can contribute are invoked, i.e., the condition part of their rules are satisfied. The control process at the end of each cycle selects the specialists with the largest contribution and executes its action. Subsequently, it is this new decision that invokes additional specialists, and the next cycle begins. The process continues until the expert has formulated the model completely, the plan satisfies the evaluation condition, or nothing else can be done due to lack of knowledge on the part of the specialists. The experts can also fail due to the decision errors.

## 3.3. Testing the sufficiency of the CPM (Step 4)

The sufficiency of the CPM as an abstraction of cognitive sub-processes for model formulation has been tested via the use of protocol analysis and nine experts. A scheme for the analysis of the protocol analysis was developed $[52]$ . The methodology used to develop the labeling rules has been used by researchers $[41]$ in problem solving. The protocol labeling rules have been defined in detail separately $[52]$ . To assess the reliability of our protocol analysis, we coded all nine cases using multiple coders to label the verbalizations. The Kappa-coefficient was used to assess the interrater reliability in this regard. The kappa value was computed as 0.60 and the hypothesis that the ratings are independent for the raters were tested using a two-sided test. The z-value for an alpha of 0.05 was 24.27 indicating that the kappa value was highly significant $[52]$ .

## 3.4. Observations from the verbalizations using the CPM (Step 5)

Since we have tested the sufficiency of the CPM with the entire set of protocols that we collected, the observations below are focused on the entire set (i.e., 9 data points-3 subjects attempting 3 problems). The intent here is not to generalize our findings, but to understand the commonality in approaches between different subjects. The major finding was the use of opportunistic case-based reasoning by each of the subjects for the problems attempted (points No. 1 2, 6 and 7 below). With the case approach that subjects emphasized, we also found that there was substantial evidence of retrieval (or recall) directed activity, which are inherent for case-based reasoning (points No. 3, 4, 5 and 8 below). A summary of our finding from the protocol analysis is given below (protocols from one set of verbalizations, Fig. 2, are cited as examples):

Table 1  
A partial list of cognitive specialists and the corresponding knowledge sources

<table><tr><td>KS-NUM</td><td>KS-Name</td><td>Cognitive specialists</td><td>Stimulus levels</td><td>Response levels</td><td>Actions</td></tr><tr><td>KS00</td><td>elicit-case-retrieval-cues</td><td>case retriever</td><td>call made to retrieval phase of case memory manager</td><td>s-domain</td><td>get retrieval cues from the user, via the case retrieval phase of the case memory manager and retrieve best case from memory</td></tr><tr><td>KS01</td><td>unravel-case</td><td>case unraveler</td><td>s-domain</td><td>s-domain</td><td>translate case from memory and create solution elements at the domain level</td></tr><tr><td>KS02</td><td>create-solution-entity-type</td><td>case unraveler</td><td>s-domain</td><td>s-entity</td><td>create entity types</td></tr><tr><td>KS03</td><td>create-solution-relationship-type</td><td>case unraveler</td><td>s-entity</td><td>s-relationship</td><td>create relationship types</td></tr><tr><td>KS04</td><td>create-solution-entity-attribute</td><td>case unraveler</td><td>s-entity</td><td>s-attribute</td><td>create solution entity attributes</td></tr><tr><td>KS05</td><td>create-solution-relationship-attribute</td><td>case unraveler</td><td>s-relationship</td><td>s-attribute</td><td>create relationship attributes</td></tr><tr><td>KS10</td><td>create-problem-query-solution-element-on-problem-entity</td><td>model elements enquirer</td><td>s-entity</td><td>p-entity</td><td>based on the solution elements get problem entities from user</td></tr><tr><td>KS11</td><td>create-problem-query-solution-element-on-problem relationship</td><td>model elements enquirer</td><td>s-relationship</td><td>p-relationship</td><td>based on the solution elements get problem entities from user</td></tr><tr><td>KS25</td><td>create-problem-entity-type</td><td>analysis inferer, problem classifier, context analyzer, problem identifier</td><td>p-entity</td><td>p-entity</td><td>create entity types</td></tr><tr><td>KS26</td><td>create-problem-relationship</td><td>analysis inferer, problem classifier, context analyzer, problem identifier</td><td>p-relationship</td><td>p-relationship</td><td>create relationship types</td></tr><tr><td>KS27</td><td>create-problem-entity-attribute-type</td><td>analysis inferer, problem classifier, context analyzer, problem identifier</td><td>p-entity</td><td>p-attribute entity types</td><td>create attributes for</td></tr><tr><td>KS28</td><td>create-problem-relationship-attribute-type</td><td>analysis inferer, problem classifier, context analyzer, problem identifier</td><td>p-relationship</td><td>p-attribute</td><td>creates attributes for relationship attributes</td></tr><tr><td>KS29</td><td>get-problem-attribute</td><td>analysis inferer, problem classifier, context analyzer, problem identifier</td><td>p-attribute</td><td>p-attribute</td><td>obtain data from the user</td></tr><tr><td>KS30</td><td>derive-problem-attribute-value</td><td>analysis inferer, problem classifier, context analyzer, problem identifier</td><td>p-attribute</td><td>p-attribute</td><td>derive the values internally depending on attribute type</td></tr><tr><td>KS31</td><td>map-solution-key-attribute</td><td>problem to tool translator</td><td>p-attribute</td><td>s-attribute</td><td>map key attributes from problem panel to solution panel</td></tr><tr><td>KS32</td><td>map-solution-nonkey-attribute</td><td>problem to tool translator</td><td>p-attribute</td><td>s-attribute</td><td>map non-key attributes from problem panel to solution panel</td></tr><tr><td>KS60</td><td>modify-problem-attribute(structure)</td><td>model adapter</td><td>p-attribute</td><td>p-attribute</td><td>modify the past case attributes</td></tr><tr><td>KS61</td><td>modify-problem-objective-coefficients</td><td>model adapter</td><td>p-attribute</td><td>p-attribute</td><td>modify the problem objective coefficients</td></tr><tr><td>KS70</td><td>present-formulation-to-user</td><td>model algebra formulator</td><td>s-attribute</td><td>s-attribute</td><td>user evaluates the formulation and decides whether the formulated model should be stored in case memory</td></tr><tr><td>KS80</td><td>merge-new-model-into-memory</td><td>case merger</td><td>s-attribute</td><td>calls up the merging phase of the case memory manager</td><td>formulated model is merged into memory with the user. User may choose to modify category struvtures during the merging phase</td></tr></table>

1. Both case and opportunistic behavior do appear in the model formulation process. (Fig. 2, protocol No. 2 for case behavior; opportunistic behavior can be seen by looking a set of protocols like No. 21–29 that indicate an opportunistic movement by the subject).

2. The observed behaviors of opportunism and case based can be integrated in a single unifying cognitive process model as described earlier. A blackboard-like data architecture [1,13,17,38], which serves as the “work-area”, and its associated cognitive specialists with an opportunistic control [18] are sufficient to define the CPM (protocol No. 21–29).

3. In addition to the opportunistic and case based processes observed in the CPM, two other processes initialization and termination are also needed. The initialization process involves the preliminary assessment of the cognitive resources that one needs to bring to a task and marshalling them for use in the formulation process. It is the prelude to the recall process. The termination process to any formulation activity is the completion of the model and an initiation of the feedback mechanism for learning and storing of that experience in the memory panel.

4. Subjects typically adopt a strategy of recalling a similar past case to serve as a prototype (recall activity). Initially, this recall is based on surface problem features observed (such as, input/output, transportation, etc.). As problem understanding increases, additional opportunities present themselves to the case indexing mechanism and another, more appropriate case is recalled indicating traces of opportunism (protocol No. 2 and 3).

5. Subjects appear to use the retrieved case or model to help guide the understanding of the current situation (model construction activity) and also assist in identifying context-free elements in the problem description for use in instantiating the partially or completely formulated model (protocol No. 7, 30, 31, and 32).

6. Subjects appear to plan opportunistically (formulation control activity), i.e., shifting focus regularly to develop the more favorable aspects of the plan in progress.

7. Typically subjects seem to step back and “reinforce” several earlier steps in the formulation process and at times “negate” his earlier intermediate steps (evaluation activity). Evaluations are also made to verify the correctness of the model as it is being developed and also after completing the formulation process. Some techniques used include: justification, critiquing, instantiation with real data, dimensionality checking, and others (protocol No. 42).

8. Subjects also use a storage activity, which is revealed through surrogate measures such as associating certain features in cases or models, associating certain models or sub-models with certain goals, associating failure situation with certain type of models (“the don’ts”), and others which could be termed as idiosyncratic features.

## 3.5. Derivation of architectural considerations (Step 6)

In choosing the appropriate approach, we mapped the above observations (from Step 5) to the SMP description of the four architectures. From a structure perspective, three of the four architecture seem viable, namely, federation, emulation and alliance. Distribution architecture was ruled out because we did not evidence distributed objects (identified as a key structure requirement of this architecture) for this application. Next, the mechanism facet was considered to further identify the appropriate architecture. From the perspective of mechanism, each of the three architectures still under consideration was deemed viable. Finally, we focused on policy issues. Our observations in Step 5 clearly indicated a need for multiple policies to guide the process of model formulation. Some of the documented policies include opportunistic behavior (Observations No. 1, 2, and 6), case based reasoning (Observations No. 1, 4, 5, 7, and 8). In order to support multiple policies, we ruled out the federation and emulation architectures. Therefore by a process of elimination we arrived at the alliance architecture. This architecture seems to fit all the attributes of the model formulation process that is being addressed. Given the critical nature of this activity for system development, we have expanded on step 6 further in the form of Section 4.

## 4. An alliance architecture from CPM

We now use the CPM described above to develop the KBS architecture for model formulation. As this CPM defines the experts' model formulation activities, the architecture derived from it will illustrate the support provided for the sub-processes that have been identified previously.

## 4.1. Overview of MODELER architecture

In the above model formulation CPM, we see the recall process (Observation 4) helps in the retrieval of similar past cases by assigning indexes identified from features in the present situation. The retrieved case is passed onto the model generation process (Observation 5) which employs the case information to guide the user in understanding the current situation. The retrieved case can also be suitably modified to conform with the current situation and evaluated. In the evaluation process (Observation 7), the formulated model is assessed for correctness and also subjected to assumption checking. Failures detected at this stage are typically adjusted by a repair process. The repair process employs additional domain knowledge to achieve this task. If the formulated

model is not amenable to the repair strategies employed, the failure is utilized to suitably index the case. Once the evaluation process is completed, the whole modeling experience is assessed for storage suitability in case memory (Observation 8). It is in this phase that learning occurs and there is a potential for the stored structures to be modified. On the other hand, the model generation and model evaluation processes along with the opportunistic control (Observation 6) emphasize the application of procedural domain knowledge to the retrieved case structure in an attempt toward modifying them for concurrence with the current situation.

![](/api/attachments/5QZ44WYZ/fulltext/images/e19f6d3d97f120afc61f15e5ec3bcaa36385998e4d931f00b16d230d50c21211.jpg)  
Fig. 4. The MODELER architecture.

The model evaluation process is currently the most intractable of the CPM processes in terms of software realization. In Fig. 2, the expert frequently pauses to make evaluations and uses different techniques such as critiquing, checking assumptions, instantiating partially formulated models, making dimensionality checks, and so on. A possible solution is to have a truth maintenance system embedded in a more sophisticated control system than the simple BB1 control used in the MODELER.

The structure related aspects of the above CPM can be bundled as the case memory manager (CMM) in the MODELER architecture (Fig. 4). The process related aspects of the CPM model are rendered as the blackboard manager (BBM) in the MODELER architecture. Thus the MODELER contains two major subsystems that are tightly integrated based on Observations 1–3.

## 4.2. Supporting recall activities

assist the interpretation activity. There are several reminding mechanisms in the literature, such as feature-based, goal-based, era-based, explanation-based, failure-based, etc. [38]. However, the appropriate reminding mechanism is often dependent on the domain and the ambiance of the situation. In the production planning domain, the formulation process is driven by models and experts tend to use features from a situation as a mechanism for model retrieval [52]. Given this domain trait, CMM utilizes a feature-based reminding mechanism to access the appropriate category. Sometimes features are used to reject a particular category and these are called censor links. Reminding links have a positive strength and censor links are reminding with a negative strength. In the recall process, the feature or set of features are used as combined reminding to find the appropriate category and its exemplar. The combined reminding is the sum of the individual reminding and can be greater than 1. The retrieved set of exemplars is sorted in order of the combined reminding strength and the one with the highest strength is selected. If the combined strengths are identical then the first exemplar in the sorted list of the retrieved exemplars is selected for use as the case to assist the user in formulating the current problem situation. Details of the pattern matching is explained elsewhere [1].

The retrieval phase of CMM is activated when the case retriever specialist (Table 1) is executed. Interpretation is the key task performed in the recall process. In this phase, the user identifies the key aspects of the current situation and provides the features for the MODELER to assign as indexes. The retrieval phase of CMM employs reminding and censor links (described later) to

The termination of the recall process results in either a retrieved case or a failure. The name of the retrieved case is written on the solution panel of the MODELER and the control passed back to the blackboard manager. An excerpt of the Lisp code that achieves this is provided in Fig. 5. If the recall process fails to find a match from the case storage, the problem situation can be en-

(setq retrieved-case (car matches))
(let\* ((exemplar (match-exemplar (car matches)))
(newcase (match-newcase (car matches)))
(category (exemplar-category exemplar))
(make-solution-domain:NAME (getname exemplar)
:LEVEL 's-domain
:VALUE retrieved-case)
(set-ks-phase :case-build-phase))

Fig. 5. End of recall process.

![](/api/attachments/5QZ44WYZ/fulltext/images/85a0395c08d94616c5edcca8e995a84f7a7d0aa3fdc5749172fb4526e9f8ffd9.jpg)

<table><tr><td rowspan="5">term</td><td>:name</td><td>transportation</td></tr><tr><td>:importances</td><td>((max 0.48) (canned-peaches 0.00)(min 0.48) (canned-tomatoes 0.00)(demand-point 0.54) (supply-point 0.90))</td></tr><tr><td>:exemplars</td><td>(transport-canned-tomatoes transport-canned-peaches)</td></tr><tr><td>:relations</td><td>(((transportation requires goods) &quot; &quot; &quot;) ((transportation sometimes suggests max) &quot; &quot; &quot;) ((transportation usually suggests min) &quot; &quot; &quot;) ((transportation requires supply-point) &quot; &quot; &quot;) ((transportation sometimes requires demand-point) &quot; &quot;&quot; )</td></tr><tr><td></td><td>Fig. 7. An example category.</td></tr></table>

tered into case storage as an exemplar of a new category.

## 4.3. Supporting storage activities

Research [33] has shown that expert modelers in the production planning area categorize their domain acquired knowledge in the form of classification hierarchies. Additionally, in these hierarchies experts tend to have a basic level where they identify and name these models as transportation, assignment, transshipment, productmix, etc. Their experiential knowledge translates into another hierarchy which is context related, and where the basic level objects refer to the area of their expertise. For example, a modeler working for a supermarket may build a context hierarchy that classifies all products into either “perishable” or “non-perishable” types. This may be due to the different transportation requirements needs associated with them. Research in psychology also suggests [39,49] the diversity in categorization hierarchies to be a function of expertise. Given the diversity in experts’ categorization hierarchies, a key requirement for the case memory manager is the need for a flexible representation scheme that can grow and be modified. We have chosen the “exemplar based view” [1] to represent the experiential and domain knowledge. An additional choice made was to base the case memory manager on a flexible categorization system [1], which helps store typical (like, exemplar) and atypical (like, exceptions) instances of categories. In the selected categorization system, the user can define nodes to be a category, an exemplar, a case, or a feature. The nodes are interconnected via different types of explanation links such as requires, implies, generalization, specialization, etc. Further, qualifiers are provided to modify the strength of a link between 0 and 1. A category is a basic level model such as transportation which has example cases with features like supply-point, demand-point, minimization, and canned-tomatoes. Fig. 6 shows partial relationships among case components for a case.

The expert initially seeds the CMM case base with domain and experiential knowledge in the form of category structures. This is done in a off-line mode with the user interacting with the CMM's storage process part. For example, the structure of a category called transportation is shown in Fig. 7. The category transportation has two exemplars and a set of relations.

The strength of the links are shown as importances which takes into account the qualifier type. Features are attributes of the case (Fig. 8). If the

term :name transport-canned-tomatoes
:category transportation
:features(supply-point demand-point canned-tomatoes min ship)
:typicality 1
Fig. 8. An example case.

term :name supply-point
:reminding ((transportation 0.90))
:relations (((supply-point is required by transportation) " " " ")

attributes are related to each other then the expert should ensure that the links are consistent. An example of a feature is presented in Fig. 9.

Difference and exemplar links are additional means of expressing relationships between nodes in the category structure. After the model generation process the formulated model is presented to the user for verification. The verified model is then passed onto to the case merger specialist. The case merger specialist passes control back to CMM for the merging phase of CMM. If the formulated model structure (without the data) is found similar to an existing exemplar then the user can increment the prototypicality rating (a positive numeric value) associated with the exemplar link, indicating reinforcement. Prototypicality ratings are used to order the exemplars in a category.

If the formulated model is different from those present in case memory, CMM provides the user with the option to merge the new formulation in case memory. In this case two scenarios can potentially occur. The formulated model can be classified under an existing category in case memory. Since it differs from the exemplar associated with that category, a new exemplar is created with a difference link which identifies the differing features. An example of a difference link is shown in Fig. 10.

## 4.4. Supporting opportunistic control

In an opportunistic environment the control mechanism monitors the process and polls the various knowledge sources for contributions. Knowledge sources are activated when their pre-conditions are met. The knowledge source scheduler typically selects the knowledge source that can contribute the most. After its execution, a knowledge source becomes dormant for the next several cycles to allow opportunities for other knowledge sources to be selected. The cycle is repeated until no more knowledge sources can contribute to the process.

Our attempt to instill this opportunistic behavior in the MODELER takes the forms of a blackboard manager which includes blackboard control, the problem panel, and the solution panel. The control aspects of the CPM, which includes the control panel, global design panel, and the specific design panel, are incorporated in the current implementation as the execution shell offered in the GBB blackboard system $[16]$ . The control follows the BB1 model 18 where events cause the triggering of knowledge sources (KSs) and the KSs (an example KS is shown in Fig. 11) in turn create knowledge source activation records (KSARs), which become executable when their preconditions are satisfied.

A priority function rates the KSARs and the one with highest rating is selected for execution from the executable queue. Ties between KSARs in the executable queue are handled by a recommendation function which currently selects the first KSAR in the queued list. In each cycle the termination function is evaluated to determine whether the model formulation process should be terminated or not. A complete list of KSs is shown in Table 1.

<table><tr><td rowspan="5">term</td><td>:name</td><td>transport-canned-peaches</td></tr><tr><td>:category</td><td>transportation</td></tr><tr><td colspan="2">:features (supply-point demand-point canned-tomatoes max ship)</td></tr><tr><td>:typicality</td><td>2</td></tr><tr><td>:differences</td><td>(transport-canned-tomatoes &lt; - (min))</td></tr><tr><td colspan="3">Fig. 10. An example case with difference link.</td></tr></table>

<table><tr><td>:trigger-conditions</td><td>((trigger-event-class-p :unit-creation)(trigger-event-type-p &#x27;solution-domain))</td></tr><tr><td>:obviation-conditions</td><td>((:stable (eql end-unraveling &#x27;end-unravel)))</td></tr><tr><td>:ksar-unit-type</td><td>case-unraveler-ksar</td></tr><tr><td>:action-function</td><td>#&#x27;unravel-case</td></tr><tr><td>:from-bb</td><td>(make-paths :paths &#x27;(solution-panel))</td></tr><tr><td>:to-bb</td><td>&#x27;(:case-build-phase)</td></tr><tr><td>:author</td><td>&quot;demo&quot;)</td></tr></table>

Fig. 11. Example of a knowledge source (KS01-unravel case).

The different specialists (KSs) communicate with each other via special message passing structures called units (Fig. 12) which are referred to as solution elements in the CPM. Messages are written on the solution and problem panels of the blackboard. The abstraction levels in the blackboard panels are called spaces (Fig. 12) and these correspond closely with their counterparts in the CPM. The operational version of the problem panel and the solution panel follows the extended entity relationship (EER) data model approach [43], which helps reduce the translation efforts between the two subsystems of the MODELER. The EER data representation is useful to facilitate the translation of a case onto the solution panel.

The problem panel has three levels: P-Entity, P-Relationship, and P-Attribute (the prefix P stands for the Problem Panel). All the panel levels correspond to an EER data representation. The P-Entity level stores units that are of type entity. The units placed on the levels are created by the model elements enquirer specialist. This specialist is triggered by messages placed on the S-Entity and S-Relationship levels. For example, in a single product transportation problem where the objective is to minimize costs, the units would be (SUPPLY-POINT), (DEMAND-POINT), and (MIN).

The solution panel accommodates the recalled past case structure which helps guide the process of problem understanding on the problem panel and also assist the adaptation process if required. The levels in the solution panel correspond to the levels on the problem panel with one exception. In the solution panel we have an additional level

(define-space (p-entity)

"The spaces that the objects of the problem panel's p-relation abstraction level will be stored on."

:units (problem-entity))

(define-gbb1-unit (problem-entity (:conc-name "problem-entity\$")

:slots

((value nil)

(response-frame nil)

(author "demo"))

Fig. 12. Example definitions of space and unit.

called the S-Domain level where the case retriever specialist places the unit containing the name of the retrieved case.

## 4.5. Supporting model generation activity

Implementation of the model generation activities posed some interesting challenges. In the above CPM, there was evidence of intercase opportunism, indicating that experts do recall multiple cases in understanding a problem situation. This, in turn, implies that gathering features is not an one-time initial effort but an ongoing process which becomes better and accurate as the problem understanding progresses. However, for the sake of brevity, we have decided to implement the feature gathering process as an one-time activity. The MODELER is currently implemented to automatically select the best case from case memory utilizing the initial set of features and use that retrieved case throughout the model generation process. However, an additional mode of operation is possible. In this mode, the MODELER displays all cases from the case storage that matches the given set of features and allows the user to select the case that should be used for guiding the understanding of the current problem. Though this capability does not provide the characteristic of intercase opportunism, it does afford greater control of the choice of cases for the knowledgeable user.

Once the retrieved case enters the model generation process, some adaptation knowledge is provided [51]. In the present implementation of the MODELER, we focus on problems that need transportation. Since the nature of the product being transported does affect the shipping costs and hence the objective of the formulation, knowledge about any mismatch between the product used in the retrieved case and the current situation is important for the formulation process. This mismatch knowledge is derived from the interpretation phase and with additional domain knowledge that is encoded in the model generation process the required adaptation is achieved. We do envision further research efforts in identifying a set of adaptation strategies that needs to be incorporated in the model generation process. Once the product adaptation knowledge is triggered, the model adapter specialist, along with the model elements enquirer (Table 1), proceeds to guide the user in eliciting knowledge about the current problem. The model generation process comes to an end when the elicitation process is complete and the algebraic formulation is presented to the user for verification. Merging the formulated model into case storage succeeds the model evaluation process and is achieved in the implementation by utilizing the characteristics of the chosen KBS for CMM. The philosophy of the KBS is that any meaningful concept learning is possible only through focused interaction with the system. The explanation language provided by the KBS explained earlier allows the user to decide whether the formulated model should be retained in memory storage. To avoid combinatorial explosion, formulated models which are found to be similar in structure with an existing exemplar of a category help increase the prototypicality rating of that exemplar. For new formulations, the user can create a new category and make the formulated model structure an exemplar of that category.

## 4.6. Supporting initialization and termination activities

Implementation of these processes involves creating the interpretation activity as a KS which gets triggered during the recall process. The interpretation activity in turn creates a retrieval event which triggers the model generation process. Once the formulation is completed the merging KS (case merger in Table 1) is triggered to begin the classification of the formulated model for memory storage purposes. As both the selected KBS were written in Lisp, we were able to work in a common address space very much in line with Corkill [7].

## 4.7. Beyond the architecture

In order to provide evidence that the architecture derived above is truly an integration of knowledge base systems through alliance, we have operationalized the MODELER. The system runs on a Sun 3/160 Workstation, and uses GBB (a blackboard system) and Protos (a case reasoner). The evidence of this implementation can be seen from a run (Appendix 1, edited to enhance the readability) where MODELER formulates a transportation problem using the integrated opportunistic case-based approach.

## 5. Conclusions

In this paper we have presented several key concepts in designing large and complex knowledge based systems. First, we point out that a problem exists in designing a complex knowledge based system. The problem involves matching domain characteristics with an appropriate integration architecture. The process till to date is fairly ad hoc. Second, we offer a formal approach for such matching using a cognitive process model. In our model formulation domain such an approach has led to an alliance architecture for integration.

Lastly, a six-step CPM methodology for matching architecture to the problem description is presented. They include: collecting data from expert modelers by observing how they formulate models using concurrent verbalizations technique; encoding the verbalizations to create the protocols; analyzing one protocol set to create the CPM; using all protocol sets to validate the CPM; listing out the observations about the underlying process; and finally, deriving the integration architecture. The resulting system called MODELER integrates opportunistic control with a case based approach to support the model formulation process of the experts.

## Appendix A

## A.1. An example run

The Farm Patch Fruit Company has four retail stores that require fresh peaches. The requirements for fresh peaches are: 75 cases at site R1, 100 cases at site R2, 75 cases at site R3, and 50 cases at site R4. The peaches can be supplied from two supply locations at S1 and S2. S1 can supply 100 cases and S2 can supply 200 cases. The cost in dollars of shipping between supply locations and retail stores per case is given by the following table:

<table><tr><td></td><td>R1</td><td>R2</td><td>R3</td><td>R4</td></tr><tr><td>S1</td><td>8</td><td>10</td><td>14</td><td>30</td></tr><tr><td>S2</td><td>7</td><td>12</td><td>20</td><td>17</td></tr></table>

The objective is to set up the model describing the shipping of peaches from supply locations to retail stores at a low shipping cost.

MODELER Execution

The session described below shows the questions asked by the system as the MODELER > prompt. The system asks for the user's response by displaying the USER > prompt. The explanations of the steps are shown in italics. MODELER also puts out the name of the system component that is currently being worked on. A partial trace of the blackboard component is also shown to show the opportunistic process.

USER > (formulate)

MODELER > Welcome to MODELER.

MODELER calls its BBM component first. This component starts the case retrieval process by calling the CMM component as a knowledge source (KS00 in Table 1) in order to elicit the features of the problem.

MODELER > .... Entering Case Memory Manager (CMM)... Retrieval Phase

```txt
Trace of execution cycles begins...
Just after interpretation of ks00-ksar-1: Cycle: 0
Triggered Executable Obviated Executed Events

ks00-ksar-2 :unit-crea transport-canned-tomatoes
MODELER > Please enter your name or initials — >
USER > demo
    MODELER opens the log file called case-mgr-log.
MODELER > Please answer 'y' to the next question.
MODELER > Do you wish to maintain a log of this session? (y or n)
USER > y

Case Retrieval Menu
d go to display menu
l load knowledge base from a file
e go to case entry menu
q quit "case retrieval"

:
:
MODELER > Select an item — >
USER > e
MODELER > Going to case entry menu....
    MODELER is interested in collecting features of the new problem from the user.

Case Retrieval Features-Entry Menu
e enter list of features from current problem
d display a selected term
q quit, to case retrieval menu

MODELER > Select an item — >
USER > e
MODELER > Enter list of features from current problem...
Enter name of the current problem (a single word, or 'q' to quit):
USER > case-100
MODELER > Please enter any comments on this case — >
USER > transportation of fresh fruit
MODELER > Please enter the features of this problem, one feature per line (terminate with blank line) — >
USER > supply-point
demand-point
min
fresh-fruit
MODELER > fresh-fruit does not currently exist:
c it's correct; create it as a new term.
r re-spell it.
s this is a synonym for an existing name.
f forget this name.
d display existing names.
```

Select an item —>

USER > c

MODELER > It's correct; Create it as a new term....

At this stage, MODELER wants to know whether the features obtained from the user form a new case that must be stored into its memory, or whether the features are to be used to retrieve an existing case from its case memory.

MODELER > Do you wish to pre-classify this case? (n - no; y - yes, prompt for a category)

Select an item —>

USER > n

MODELER using its Case Manager component (CMM) finds out two cases in its case memory that resemble the features given earlier.

MODELER > Raw reminders evoked:

supply-point——-> transportation 0.90

demand-point——-> transportation 0.90

min—————-> transportation 0.48

Merged reminders:

transportation 2.28

Strengthen categories...

strengthen exemplars...

Reminding: transportation may select up to 5 exemplars:

transport-canned-tomatoes 2.28

transport-canned-reaches 2.28

Sorted list of hypotheses (exemplars):g

gtransport-canned-peaches 2.28g

transport-canned-tomatoes 2.28

transportation: (transport-canned-tomatoes, transport-canned-peaches)

transportation: (transport-canned-tomatoes, transport-canned-peaches)

New reminders evoked:

MODELER > Similar cases have been found... let us see whether we can use one of them to formulate your problem...

Case Retrieval Features-Entry Menu

enter list of features from current problem

display a selected term

quit, to case retrieval menu

MODELER > Select an item —>

USER > q

Case Retrieval Menu

go to display menu

load knowledge base from a file

e go to case entry menu

q quit "case retrieval"

```txt
acquired Measure from the case
1 supply-point 1.00 supply-point + + +
2 demand-point 1.00 demand-point + +
3 demand-point 0.90 ship + +
4 min 1.00 min + +
5 spurious —-> 1.00 canned-tomatoes -
6 fresh-fruit < — unmatched
Match Similarity = 0.90
```

MODELER > Select an item —>

At this point, MODELER has completed its retrieval of a case. In spite of having two cases retrieved, the CMM component picks up just one case.

```txt
MODELER > End of Retrieval Phase....
```

```txt
Saving knowledge base.....
```

```txt
Knowledge base saved.
```

.... Entering the Blackboard Manager...

The control is now passed to the BBM component to use the “retrieved case” in the model formulation process. We provide some traces of execution to show: (a) the opportunism, and (b) the model construction activity of the model formulation process.

The EBM component now starts putting (using KS01) the case on the Solution blackboard for its use in the model formulation process.

Trace of execution cycles begins...

Just after interpretation of ks01-ksar-2: Cycle: 1

Triggered Executable Obviated Executed

Events

ks00-ksar-2:unit-crea supply-point

< CC-KSAR (< transport-canned-tomatoes >) >

:unit-crea demand-point

:unit-crea min

MODELER now shows to the user the retrieved case that it has acquired from its case memory. This is done to let the user participate in the model formulation process.

MODELER > category: transportation

case: case-100

```yaml
exemplar: transport-canned-tomatoes
```

Feature Similarity Feature Importance

MODELER > Is the product transported similar to canned-tomatoes? (y or n)

```txt
USER > n
```

MODELER > Is the product perishable? (y or n)

```txt
USER > y
```

MODELER > Is there any other cost that needs to be included in the transportation cost? (y or n)

```txt
USER > n
```

MODELER > Is there any time constraint? (y or n)

```txt
USER > n
```

In the next several cycles, the BBM of MODELER first creates the problem entity and relationship types on the Problem Panel (or Blackboard) using KS10 and KS 11.

```txt
Trace of execution cycle begins...
Just after interpretation of ks10-ksar-1: Cycle: 2
Triggered Executable Obviated Executed Events
< CC-KSAR (< demand-point >) >
ks00-ksar-2 :unit-crea supply-point
< CC-KSAR (< supply-point >) >
< CC-KSAR (< transport-canned -tomatoes >) >
< CC-KSAR (< min >) >
< CC-KSAR (< ship >) >
:unit-crea ship
MODELER starts asking data from the user (KS25 - KS29) using the “retrieved case,” and puts the data on the Problem Panel (or Blackboard). Notice the “opportunism” in MODELER as relation-enquirer (KS26) is executed first as it can put a solution element at the higher level of the Solution Panel right now (see Fig. 4).
Trace of execution cycle begins...
Just after interpretation of ks11-ksar-1 Cycle: 4
Triggered Executable Obviated Executed Events
< CC-KSAR (< ship >) >
< CC-KSAR (< demand-point >) >
ks00-ksar-2 :unit-crea min
< CC-KSAR (< demand-point >) >
< CC-KSAR (< supply-point >) >
< CC-KSAR (< transport-canned -tomatoes >) >
< CC-KSAR (< supply-point >) >
< CC-KSAR (< ship >) >
< CC-KSAR (< min >) >
:
:
MODELER > How do you call supply-point in this problem?
USER > supply location
MODELER > How do you call demand-point in this problem?
USER > retail store
MODELER > How do you call ship in this problem?
USER > ship
MODELER > ...I need some data about the supply location names... What do you call the individual supply locations? (each of the supply location name asked for should be separated by a blank)
USER > S1 S2
MODELER > ...I need some data about the supply location capacities... What are the capacities of the supply locations? (each of the supply location capacity asked for should be separated by a blank)
USER > 100 200
MODELER > ...I need some data about the retail store names... What do you call the individual retail stores? (each of the retail store names asked for should be separated by a blank)
```

USER > R1 R2 R3 R4

MODELER > ...I need some data about the requirements at each retail store... What are the requirements at each retail store? (each of the retail store requirements asked for should be separated by a blank)

USER > 75 100 75 50

MODELER > ...I need some data about the shipping costs on the different routes...

MODELER > What are the costs for the route (S1 R1) (Please enter a numeric integer value)?

MODELER > What are the costs for the route (S1 R2) (Please enter a numeric integer value)?

MODELER > What are the costs for the route (S1 R3) (Please enter a numeric integer value)?

MODELER > What are the costs for the route (S1 R4) (Please enter a numeric integer value)?

MODELER > What are the costs for the route (S2 R1) (Please enter a numeric integer value)?

USER > 7

MODELER > What are the costs for the route (S2 R2) (Please enter a numeric integer value)?

MODELER > What are the costs for the route (S2 R3) (Please enter a numeric integer value)?

MODELER > What are the costs for the route (S2 R4) (Please enter a numeric integer value)?

MODELER now populates the Solution Panel by mapping the problem data from the Problem Panel opportunistically using KS30, KS31, and KS32.

Trace of execution cycle begins...

Just after interpretation of ks31-ksar-1: Cycle: 9

Triggered Executable Obviated Executed

Events

```txt
< CC-KSAR (< relationship
-1-derived >) >
< CC-KSAR (< demand-point >) >
ks00-ksar-2 :unit-crea item-name
< CC-KSAR (< entity
-2-derived >) >
< CC-KSAR (< supply-point >) >
< CC-KSAR (< transport-canned
-tomatoes >) >
< CC-KSAR (< entity-1-derived >) >
< CC-KSAR (< supply-names >) >
< CC-KSAR (< ship >) >
< CC-KSAR (< activity-route
-costs >) >
< CC-KSAR (< supply-capacities >) >
< CC-KSAR (< min >) >
< CC-KSAR (< demand-names >) >
< CC-KSAR (< min >) >
< CC-KSAR (< demand-reqmts >) >
< CC-KSAR (< ship >) >
< CC-KSAR (< key-1-attr-name >)
```

```txt
USER > e
```

```html
< CC-KSAR (< key-2-attr-name >) >
< CC-KSAR (< supply-point >) >
< CC-KSAR (< key-1n2-attr-name >) >
< CC-KSAR (< demand-point >) >
< CC-KSAR (< relationship-1-derived-alg >) >
The control is now passed to the KS70 (model algebra formulator) knowledge source to create the algebraic formulation of the model.
```

```txt
Minimize Total Cost = 8 * (SH-QTY S1 R1) + 10 * (SH-QTY S1 R2) + 14 * (SH-QTY S1 R3) + 30 * (SH-QTY S1 R4) + 7 * (SH-QTY S2R1) + 12 * (SH-QTY S2 R2) + 20 * (SH-QTY S2 R3) + 17 * (SH-QTY S2 R4)
```

## Subjected to:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$1*(\mathrm{SH - QTY S1 R1}) + 1*(\mathrm{SH - QTY S1 R2}) + 1*(\mathrm{SH - QTY S1 R3}) + 1*(\mathrm{SH - QTY S1 R4}) = 100$
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$1*(\mathrm{SH - QTY~S2~R1}) + 1*(\mathrm{SH - QTY~S2~R2}) + 1*(\mathrm{SH - QTY~S2~R3}) + 1*(\mathrm{SH - QTY~S2~R4}) = 200$
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$1*(\mathrm{SH - QTY~S1~R1}) + 1*(\mathrm{SH - QTY~S2~R1}) = 75$
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$1*(\mathrm{SH - QTY~S1~R2}) + 1*(\mathrm{SH - QTY~S2~R2}) = 100$
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$1*(\mathrm{SH - QTY~S1~R3}) + 1*(\mathrm{SH - QTY~S2~R3}) = 75$
</div>

```txt
1*(SH-QTY S1 R4) + 1*(SH-QTY S2 R4) = 50
```

```txt
MODELER > Do you concur with the formulation shown above? (y or n)
```

```txt
USER > y
```

MODELER > Thank you for interacting with me. We need to merge the formulated model in case memory. I will need your help in this phase.

As the present problem is different from the one saved in the case base memory, the problem will now be stored as a “separate” case using the case merger (KS80). After merging is over, the control goes back to the BBM component of MODELER.

MODELER > Merging phase of MODELER begins. Please help me decide whether I should retain the current formulation. I would appreciate if you will speak my language. I will provide the guidelines as and when they are needed.

The MODELER again reopens the log file called case-mgr-log.

Case Merge Planning Menu

<table><tr><td>o</td><td>go to overview menu x load example knowledge base</td></tr><tr><td>d</td><td>go to display menu l load knowledge base from a file</td></tr><tr><td>c</td><td>go to control menu s save knowledge base to a file</td></tr><tr><td>u</td><td>go to unfocused menu f forget current knowledge base</td></tr><tr><td>e</td><td>go to case merge menu q quit CMM</td></tr></table>

MODELER > Select an item —>

```txt
Case Merging Menu
e enter list of features from current problem
c copy-and-edit a previous case
d display a selected term
q quit, to case retrieval menu
```

```txt
MODELER > Select an item —>
USER > c
MODELER > enter the name of an existing exemplar or category (or type 'q' to return to menu) →
MODELER > transportation
qMODELER > transportation has the following exemplars, in order of typicality:
(transport-canned-tomatoes, transport-canned-peaches)
type 'p' for the prototype, else enter a name:
USER > p
MODELER > this exemplar has the following features:
(supply-point, demand-point, canned-tomatoes, min, ship)
Which features should be included in the new case?
MODELER > -> supply-point? (y or n)
USER > y
MODELER > -> demand-point? (y or n) > canned-tomatoes? (y or n)
USER > n
MODELER > -> min? (y or n)
USER > y
MODELER > -> ship? (y or n)
USER > y
MODELER > OK, the case has these features:
(supply-point demand-point min ship)
MODELER > Please enter any additional features, one feature per line (terminate with blank line)—>
USER > peaches
MODELER > —>
MODELER > peaches does not currently exist:

it's correct; create it as a new term.
re-spell it.
this is a synonym for an existing name.
Forget this name.
display existing names.

Select an item —>

USER > c
MODELER > Enter name of the current problem (a single word, or q to quit):
USER > q
MODELER > Do you wish to pre-classify this case? (n - no; y - yes, prompt for a category; c - classify as “transportation”)
Select an item —>
USER > c
MODELER > CK, the final case features are:
(supply-point, demand-point, min, ship, peaches)
Raw reminders evoked:
supply-point——-> transportation 0.90
demand-point——-> transportation 0.90
```

min—————-> transportation 0.48
ship—————-> transportation 0.48
Merged reminders:
transportation 3.51
Strengthen categories...
Common-specializations...
Strengthen exemplars...
Strengthen features...
Final sorted reminders:
transportation 3.51
Tracing build-hypotheses...
Reminding: transportation may select up to 5 exemplars:
transport-canned-tomatoes 3.51
transport-canned-peaches 3.51
Sorted list of hypotheses (exemplars):
transport-canned-peaches 3.51
transport-canned-tomatoes 3.51
transportation: (transport-canned-tomatoes, transport-canned-peaches)
transportation: (transport-canned-tomatoes, transport-canned-peaches)
New reminders evoked:
We are now ready to merge the formulated model of the MODELER... Thank you for cooperating.

We are now ready to merge the formulated model... and terminate this session of the MODELER... Thank you for cooperating.

## References

[1] Bareiss, R., Exemplar-Based Knowledge Acquisition: A Unified Approach to Concept Representation, Classification, and Learning (Academic Press, San Diego, 1989).

[2] Binbasioglu, M. and Jarke, M., Domain Specific DSS Tools for Knowledge-Based Model Building," Decision Support Systems 2 (1986) 213–223.

[3] Bonczek, R.H., Holsapple, C.W., and Whinston, A.B. A Generalized Decision Support System Using Predicate Calculus and Network Da at Base Management, Operations Research 29, No. 2 (1981) 263–281.

[4] Brown, D.C. and Chandrashekaran, B., Design Problem Solving: Knowledge Structures and Control Strategies (Morgan Kaufman, San Mateo, California, 1989).

[5] Carbonell, J.M., Knoblock, C.A., and Minton, S., Prodigy: An Integrated Architecture for Planning and Learning, in Architectures for Intelligence, Kurt VanLehn, Ed. (Lawrence Erlbaum Associates, Hillsdale, New Jersey, 1991).

[6] Chang, C.L. and A. Walker, PROSQL: A Prolog Programming Interface with SQL/DS, Expert Database Systems, Larry Kerschberg, Ed. (The Benjamin/Cummings Publishing Company, Reading, Mass, 1986, 233–246).

[7] Corkill, D.D., Embedable Problem Solving Architecture: A Study of Integrating OPS5 with UMass GBB, IEEE Transactions on Knowledge and Data Engineering 3, No. 1 (March 1991) 18–24.

[8] Dayal, U., Blaustein, B., and others, The HiPAC Project: Combining Active Databases and Timing Constraints, SIGMOD Record 17, No. 1 (1988) 51–70.

[9] Dhar, V. and Pople, H.E., Rule-Based versus Structure-Based Models for Explaining and Generating Expert Behavior, Communications of the ACM 30, No. 6 (June 1987) 542–555.

[10] Dolk, D. and Konsynski, B.R., Knowledge Representation for Model Management, IEEE Transactions on Software Engineering SE-10, No. 6 (1984) 619–628.

[11] Durfee, E.H., Lesser, V.R., and Corkill, D.D., Trends in Cooperative Distributed Problem Solving, IEEE Transactions on Knowledge an Data Engineering 1, No. 1 (March 1989) 63–83.

[12] Dutta, A. and Basu, A., An Artificial Intelligence Approach to Model Management in Decision Support Systems, IEEE Computer 17, No. 9 (1984) 89–97.

[13] Engelmore, R. and Morgan, T., Eds., Blackboard Systems (Addison-Wesley, NY, 1988).

[14] Ericsson, K.A. and Simon, H.A., Protocol Analysis: Verbal Reports as Data, MIT Press (Cambridge, MA, 1984).

[15] Federowicz, J. and Williams, G.D., Representaing Modeling Knowledge in an Intelligent Decision Support System, Decision Support Systems 2, No. 1 (March 1986) 3–14.

[16] Gallagher, K.Q., Corkill, D.D. and Johnson, P.M., GBB Reference Manual: GBB Version 1.2, COINS Technical Report 88-66 (Department of Computer and Information

Science, University of Massachusetts at Amherst, MA, 1988).

[17] Hammond, K.J., Opportunistic Memory: Storing and recalling suspended goals, Proceedings of the First Case-Based Reasoning Workshop (Morgan Kaufmann Publishers, Los Altos, CA., 1988) 154–168.

[18] Hayes-Roth, B. and Hayes-Roth, R., A Cognitive Model of Planning, Cognitive Science 3 (1979) 275–310.

[19] Hayes-Roth, F., Waterman, D.A., and Lenat, D.B. (edited by) Building Expert Systems (Addison-Wesley Publishing, Reading, Massachusetts, 1983).

[20] Huhns, M.N., Distributed Artificial Intelligence (Morgan Kaufmann Publishers, Los Altos, 1987).

[21] Johnson, M.E. and Poorte, J.P. A Hierarchical Approach to Computer Animation in Simulation Modeling, Simulation 50, No. 1 (1988) 30–36.

[22] Kimbrough, S.O. and Lee, R., Logic Modeling: A Tool for Management Science, Decision Support Systems 4 (1988) 3–16.

[23] Krishnan, R. A Logic Modeling Language for Automated Model Construction. To appear in Decision Support Systems (1990).

[24] Krishnan, R., Li, X., Steier, D., Development of a Knowledge-based Mathematical Formulation System, Communications of the ACM 35, No. 9 (September 1992) 138–146.

[25] Lazimi, R., A Generic Shell Approach for Knowledge Elicitation and Representation in IDSS, Proceedings of the Eighth International Conference on Information Systems, Pittsburgh PA (December 1987) 335–351.

[26] Liang, T.P., Development of a Knowledge-Based Model Management System, Operations Research 36, No. 6, (Nov/Dec 1988) 849–863.

[27] Liang, Ting-Peng., Modeling by Analogy: A Case-based Approach to Automated Linear Program Formulation, Proceedings of Hawaii International Conference on System Sciences (1991).

[28] Luger, G.F., Mathematical Model Building in the Solution of Mechanics Problems: Human Protocols and the MECHO Trace, Cognitive Science 5 (1981) 55–77.

[29] Ma, P.C., Stohr, E.A. and Murphy, F.H., Semantic Structures in Linear Programs, Proceedings of the Twenty-Second Annual Hawaii International Conference on System Sciences, Vol. III, Decision Support and Knowledge Based Systems Track (Jan. 1989) 459–466.

[30] Missikoff, M. and Widerhold, G., Towards a Unified Approach for Expert and Database Systems, in: Larry Kerschberg, Ed., Expert Database Systems (The Benjamin/Cummings Publishing Company, Reading, Mass, 1986) 383–400.

[31] Mitchell, T.M., Allen, J. and others, Theo: A Framework for Self-Improving Systems, Architectures for Intelligence, Kurt VanLehn, Ed. (Lawrence Erlbaum Associates, Hillsdale, New Jersey, 1992).

[32] Murphy, F.H. and Stohr, E.A., An Intelligent System for Formulating Linear Programs, Decision Support Systems 2 (1986) 39–47.

[33] Orlikowski, W. and Dhar, V., Imposing Structure on Linear Programming Problems: An Empirical Analysis of Expert and Novice Models, Proceedings of National Conference on AI, Philadelphia (1986) 308–315.

[34] Pabo, C.O. and Suchanek, E.G., Computer-Aided Model-Building Strategies for Protein Design, Biochemistry 25 (1986) 5987–5991.

[35] Perry, D.E. and Kaiser, G.E., Models of Software Development Environments, IEEE Transactions on Software Engineering 17, No. 3 (March 1991) 283–295.

[36] Raghunathan, S.A., A Planning Aid: An Intelligent Modeling System for Planning Problems Based on Constraint Satisfaction, IEEE Transaction on Knowledge and Data Engineering 4, No. 4 (August 1992) 317–335.

[37] Reitman, W. Cognition and Thought (John Wiley, New York, 1965).

[38] Riesbeck, C.K. and Schank, R.C., Inside Case-Based Reasoning (L.Erlbaum, Hillsdale, NJ, 1989).

[39] Rosch, E., Principles of Categorization., in: E. Rosch and B.B. Lloyd, Eds., Cognition and Categories (Lawrence Erlbaum, Hillsdale, NJ, 1978).

[40] Rosenbloom, P.S., Newell, A., and Laird, J.E., Toward the Knowledge Level in Soar: The Role of the Architecture in the Use of Knowledge, in: Kurt VanLehn, Ed., Architectures for Intelligence (Lawrence Erlbaum Associates, Hillsdale, New Jersey, 1992).

[41] Rowe, Helga A.H., Problem Solving and Intelligence (Lawrence Erlbaum Associates, Hillsdale, NJ, 1985).

[42] Sciore, E., and Warren, D.S., Towards an Integrated Database-Prolog System, in: Larry Kerschberg, Ed., Expert Database Systems (The Benjamin/Cummings Publishing Company, Reading, Mass, 1986) 219-232.

[43] Sen, A., Vinze, A.S., Boyle, C. and Liou, S.T., Mapping the Entity Relationship Model to a Blackboard Architecture, Presented at the AAAI-90 Workshop on Blackboard Systems (Boston, 1990).

[44] Sen, A., Vinze, A.S., and Liou, S.T., Construction of a Model Formulation Consultant: The AEROBA Experience, IEEE Transactions on Systems, Man, and Cybernetics 22, No. 5 (Sept/Oct 1992) 1220–1232.

[45] Sivasankaran, T. and Jarke, M., Logic-based Formula Management Strategies in an Actuarial Consulting System, Decision Support Systems 1 (1985) 251–262.

[46] Slade, S., Case-Based Reasoning: A Research Paradigm, AI Magazine 12, No. 1 (1991) 42–55.

[47] Sommerville, I., Software Engineering (Addison Wesley, Reading, Mass., 1992).

[48] Stonebraker, M. and Rowe, M., The Design of Postgres, Proceedings of International Conference on the Management of Data (ACM New York, May 1986) 340–355.

[49] Tanaka, James W. and Taylor, Marjorie. Object Categories and Expertise: Is the Basic Level in the Eye of the Beholder?, Cognitive Psychology 23 (1991) 457–482.

[50] VanLehn, K. and Ball, W., Goal Reconstruction: How Teton Blends Situated Action and Planned Action, Architectures for Intelligence, Kurt VanLehn, Ed., (Lawrence Erlbaum Associates, Hillsdale, NJ, 1992).

[51] Vellore, R.C., Vinze, A.S., and Sen, A., MODELER: Incorporating Experiences to Support Model Formulation A Case-Based Planning Approach, Expert Systems with Applications 6 (1993) 37–56.

[52] Vellore, R.C., Vinze, A.S., and Sen, A., The Role of Experience in Model Formulation, Working paper (Business Analysis and Research Department, Texas A&M University, College Station, Texas, 1992).

[53] Vinze, A. and Sen, A., Expert Assistance for the Decision Support Process Using Hierarchical Planning, IEEE Transactions on Systems, Man, and Cybernetics 21, No. 1 (January 1991).

[54] Vinze, A., Sen, A., and Liou, S.F., Operationalizing the Opportunistic Behavior in Model Formulation, International Journal of Man-Machine Studies 38, No. 3 (March 1993) 509–540.

[55] Vinze, A.S., Sen, A., and Liou, S.T., AEROBA: A Blackboard Approach to Model Formulation, Proceedings of the Twenty-Fifth Hawaii International Conference on System Sciences, Decision Support and Knowledge Based Systems Track, Jan. 7–10 (1992).

[56] Waterman, D.A., A Guide to Expert Systems (Addison-Wesley, New York, 1986).

[57] Williams, H.P., Model Building in Mathematical Programming, 3rd. Edition (John Wiley and Sons, New York, 1990).

[58] Zaniolo, Carlo, Prolog: A Database Query Language for All Seasons, Expert Database System, Larry Kerschberg, Ed. (The Benjamin/Cummings Publishing Company, Reading, Mass, 1986) 383–400.

Ravi C. Vellore is an Associate Professor of Management Information Systems in Central Connecticut State University. He received his Ph.D degree from Texas A&M University in Information Systems in 1992. His research interests include business applications of case-based reasoning and knowledge base systems for end-user computing. He has published in Experts Systems with Applications and several national conferences.

![](/api/attachments/5QZ44WYZ/fulltext/images/ac120c43d6129eabaf023b8511fdf5877a0cb67da952310789dde936bfa480cf.jpg)

Aru Sen is an Associate Professor of Management Information Systems in the Business Analysis Department at Texas A&M University, College Station, Texas. He received the M. Tech. in Electronics in 1971 from Calcutta University (India), the M.S. in Computer Science in 1976, and the Ph.D. in Information Systems in 1979 from the Pennsylvania State University. His research interests include intelligent decision support systems, object data

base systems, expert systems, blackboard systems, and model formulation support systems, object data base systems, expert systems, blackboard systems, and model formulation support systems. He has published numerous papers in Information System Research, IEEE Transactions on Systems, Man and Cybernetics, Information Systems, MIS Quarterly, Journal of MIS, Decision Support Systems, and others. He serves in the editorial board of Journal of Database Management. He has been a guest editor of the special issues of International Journal of Expert Systems with Applications and Decision Support Systems.

![](/api/attachments/5QZ44WYZ/fulltext/images/208f0c71d7300b2d0b41f663c0bdf8c4dc2dacd72f127dd635c6d81f2cf25d56.jpg)

Ajay S. Vinze is an Associate professor of Management Information Systems in the Business Analysis Department at Texas A&M University, College Station, Texas. He received the M.B.A, from the University of Arizona in 1988. His published works haze appeared in IEEE Translation on Systems, Man and Cybernetics, International Journal of Man-Machine Studies, Journal of Management Information Systems, Omega, and others.

He serves on the editorial board of International Journal of Human-Computer Studies (formerly International Journal of Man-Machine Studies) and has been a guest editor for a special issue of International Journal of Experts Systems with Applications.
