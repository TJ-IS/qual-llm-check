---
otero_id: 26639
otero_key: "HN7V3S6Y"
title: "MODFORM: A Knowledge-Based Tool to Support the Modeling Process"
authors: "Srinivasan Raghunathan; Ramayya Krishnan; Jerrold H. May"
year: "1993"
journal: "Information Systems Research"
doi: "10.1287/isre.4.4.331"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [129.105.215.146] On: 16 September 2016, At: 09:06 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

![](/api/attachments/HN7V3S6Y/fulltext/images/76a2772f694292aff0475b065d10e43f91e2c730bfce31894c2ceaf121bbc78a.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# MODFORM: A Knowledge-Based Tool to Support the Modeling Process

Srinivasan Raghunathan, Ramayya Krishnan, Jerrold H. May,

## To cite this article:

Srinivasan Raghunathan, Ramayya Krishnan, Jerrold H. May, (1993) MODFORM: A Knowledge-Based Tool to Support the Modeling Process. Information Systems Research 4(4):331-358. http://dx.doi.org/10.1287/isre.4.4.331

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1993 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/HN7V3S6Y/fulltext/images/0a826fb6e8bf705b042f1c87452419fa0829cfad4a2612f814c75aa9a541fddb.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# MODFORM: A Knowledge-based Tool to Support the Modeling Process

Srinivasan Raghunathan

Department of Accounting and MIS

Bowling Green State University

Bowling Green, Ohio 43403

Ramayya Krishnan

Heinz School of Public Policy and Management

Carnegie Mellon University

Jerrold H. May

Pittsburgh, Pennsylvania 15213

Katz Graduate School of Business

University of Pittsburgh

Pittsburgh, Pennsylvania 15260

The value of mathematical modeling and analysis in the decision support context is well recognized. However, the complex and evolutionary nature of the modeling process has limited its widespread use. In this paper, we describe our work on knowledge-based tools which support the formulation and revision of mathematical programming models. In contrast to previous work on this topic, we base our work on an indepth empirical investigation of experi enced modelers and present three results: (a) a model of the modeling process of experienced modelers derived using concurrent verbal protocol analysis. Our analysis indicates that modeling is a synthetic process that relates specific features found in the problem to its mathematical model. These relationships, which are seldom articulated by modelers, are also used to revise models. (b) an implementation of a modeling support system called MODFORM based on this observationally derived model, and (c) the results of a preliminary experiment which indicates that users ofMODFORM build models comparable to those formulated by experts. We use the formulation of mathematical programming models of production planning problems illustratively throughout the paper.

Model management—Knowledge-based systems—Process analysis—Object-based methods

## 1. Introduction

he value of mathematical modeling and analysis in the decision support context is well recognized. However, its widespread use has been limited due to the complex and evolutionary nature of the modeling process. The problems encountered by modelers (even those with formal training) during formulation have been documented empirically (Orlikowski and Dhar 1986), as have the difficulties faced in managing the evolutionary nature of the modeling process (Gass 1987)

In response to these problems, there have been significant advances in the development of computer-based tools to support modeling. Examples include improved representation languages (Kendrick and Meeraus 1987; Jones 1990, 1991; Geoffrion 1987, 1989; Greenberg 1992), support for specific tasks such as model integration (Bradley and Clemence 1988, Kottemann and Dolk 1992, Krishnan et al. 1991, Liang 1986, Muhanna 1991) and result explanation (Greenberg 1983), and model management systems (Blanning 1991).

There has also been more recent research that has begun to specifically address computer-based support for model formulation (Binbasioglu and Jarke 1986; Murphy and Stohr 1986; Krishnan 1989; Liang 1990; Sklar et al. 1988, 1990; Sklar and Pick 1990). All these systems support the formulation of Linear Programming (LP) models. Building on this stream of research, we focus in this paper on support for the formulation of mathematical programming models. However, in contrast to previous research, we base our work on an indepth concurrent verbal protocol analysis (Ericsson and Simon 1984) of experienced human modelers. We believe that the analysis will improve our understanding of the human modeling process and the design of our modeling support system. Specifically, we present three results in this paper:

(a) a model of the process by which experienced modelers formulate mathematical programming models derived using concurrent verbal protocol analysis. Our analysis indicates that modeling is a synthetic process that relates specific features found in the problem to its mathematical model. These relationships, which are seldom articulated by modelers, are also used to revise models.

(b) an implementation of a modeling support system called MODFORM based on this observationally derived model, and,

(c) the results of a preliminary experiment which indicates that users of MOD-FORM build mathematical programming models comparable to those formulated by experts.

The rest of the paper is organized as follows. In §2, we present our model of the expert formulation process using data from the verbal protocols to support our findings. In §3, we introduce the architecture of MODFORM, provide an overview of its functionality, and describe how it relates to the model in §2. In §4, we focus on the principal knowledge-based components of the architecture and provide implementation details. In §5, we present results of an experiment conducted with MODFORM. We conclude in §6 with a discussion of future research topics.

## 2. A Model of Expert Model Formulation

The starting point in the design of a knowledge-based system is a clear understanding of the task the system is designed to support. To this end, we begin by presenting results of an indepth observational study of expert human modelers. Our study used the concurrent verbal protocol analysis technique that has been extensively applied to understand human problem solving (Newell and Simon 1977).

Briefly, protocols are verbal reports obtained from subjects that are directed to “think aloud" while solving problems (in our case, the subject thinks aloud while formulating mathematical programming models). These protocols are transcribed and examined, phrase by phrase. The purpose of the examination is to identify the states that are explored and the knowledge that is accessed and applied to transform one state into another. The results of such an analysis are used to constrain the normally underconstrained task of knowledge representation design.

We collected protocols from four experts. All the experts had at least ten years experience in mathematical programming model development. Three of the experts were professors, while the fourth was an experienced practitioner in the Operations Research department of a Fortune 500 company. The experts were given eight textbook problems (Johnson and Montgomery 1974), and a Harvard case study (The Delco Refinery Case) on production planning. The protocols ranged in duration from 30 minutes to three hours. In all, more than 30 hours of protocols were collected and analyzed.

In general, the analyses showed that formulation usually involves diverse knowledge about the problem domain, about specific model building “tricks," and about the computational tractability of various formulations. Further, the process consisted of two important phases: problem structuring and model construction. In the problem structuring phase, the expert identifies the data that is relevant, and chooses a model type based on its tractability. In the model construction phase, the mathematical relationships between data elements are formulated. Our model of the expert modeling process is shown in Figure 1. While we did not find any significant differences in the modeling process used by the four expert modelers, we did observe certain other differences (e.g., the specific modeling techniques that were used) in the protocols collected during our study. These observed differences and how we have chosen to accommodate them in MODFORM are described in §2.3. The remainder of this section details specific findings about the modeling process. The implications that these findings have for MODFORM's design are discussed in §2.4.

## 2.1. Problem-structuring Phase

AssERTioN 1. Experts categorize the problems and their features into standard types, which we refer to as chunks.

In the problem-structuring phase, the expert first attempts to categorize the problem that needs to be formulated using knowledge chunks that correspond to known model types such as “product mix" and “blending."' Chunking, or categorization, by experts has been reported in several domains (Novak 1972, Chi et al. 1981, Orlikowski and Dhar 1986). Chunks allow the experts to recognize a particular problem as being similar to a standard problem type, and to model the problem in a routine manner. Additionally, chunks also provide clues that enable the expert to identify the set of relevant entities for the problem. For example, recognizing a “product mix" problem helps the expert to look for resources and products. A “transportation" problem type suggests sources and destinations. We do not understand the exact mechanism by which the chunks are mapped to problems except that it is tentative. The details of how this mapping takes place is a topic for future research. The protocol fragment shown below supports our conclusions.

08 It looks like a blending problem. Okay . . so what we are going to have is . . which . . I will explain what I am thinking about. Do I need doubly subscripted variables or triple subscripted variables?

Raghunathan • Krishnan • May  
![](/api/attachments/HN7V3S6Y/fulltext/images/404477eb4e306056c41fce31751b0eacaba2a00f9e67a6218522fbd06d28dd22.jpg)  
FIGURE 1. A Model of the Expert Model Formulation Process

13 Okay . . it is a little bit more complicated than the standard blending problem,

14 The following table . . composition . . okay . . what we have here . is that how much . . You can probably do it as a transportation problem . . let us see.

15 It tells you ore and how much of each metal it has. So let us see what happens here.

16 We can probably do it as a multiple subscripted variables.

17 The question is how are you going to keep track of which things go into where to produce what . . which is a classic blending problem.

18 We could for example keep track of how much came from ore 1 that went into M1, that came out with A, and so on.

19 That would be one way to do it or could conceivably think of doing it without keeping track of source and destination like inventory variables.

22 We have an ore and the metal. Let us try to set up each piece and see what that piece looks like . . the piece . . certainly blending kind of thing. .

(expert 1, problem 4, underlines have been added)

In the excerpt shown above, the expert, at first, tentatively identifies the problem as a “blending" type of problem (line 8). He also considers the type of variables and subscripts required in the model. We interpret the behavior of the expert in this line as one in which he attempts to modify the model associated with a blending problem type since the problem he is to formulate is not a simple blending type of problem. This interpretation is also confirmed later in line 13 where the expert suggests that the problem is more complicated than the standard blending problem. The expert also considers mapping the problem onto a transportation problem type (line 14) but later revises the problem type back to blending. There is also evidence that the expert attempts to identify the source and destination associated with the transportation problem type (line 19). Such tentative reasoning about problem types is a characteristic of expert model formulation.

AssERTiON 2. Experts generate hypotheses or expectations concerning data to look for in the problem based on chunks and generic entities.

The hypotheses that experts generate about the data to look for in a problem are based both on the identification of the problem type (using chunks) and on concepts which we term generic entities. These generic entities (e.g., resources) are abstracted concepts in terms of which experts appear to formulate their problems. For example, when the expert identifies a resource entity, he/she infers a resource capacity constraint, which in turn leads to an attempt to gather data regarding the availability of the resource. A process entity (another generic entity) generates expectations about the relationship between the amount of input used in it and the amount of output produced by it. This hypothesis formation process helps the expert transform a problem description into a set of qualitative relationships among data associated with the generic entities. The following excerpts support our assertion.

13 (reads) The distillation process at Delco's refinery separates gasoline from other components by heating crude oil under pressure until the gasoline vaporizes. The vapors are then collected and cooled in a condenser to produce the distillate.

14 So I presume that distillate is synonymous with gasoline.

15 Umm . , the tower uses . . so the transformation is that two barrels of crude oil produce one barrel of distillate that is gasoline and . . 4.2 barrels of other products

(expert 4 Delco case)

35 so what you have here is . . it takes 6 manhours to produce a product

36 so let us take a look at the production level in time period 1 . . 6 times the total number of hours required.

37 the labor . . and that has to be . . we cannot book more hours than we can provide. The amount of labor that we can provide is . . umm . . 8 hours of regular time per person plus

38 we have to figure out how many hours are available .

(expert 1, problem 1)

In line 15, the expert first looks for data concerning the functional relationship between the inputs and the outputs of the distillation process. In line 38, the expert expects a constraint on available manhours, a resource used in the production process.

AssERTioN 3. Experts decompose the problem into various levels, and synthesize the relationships among generic entities in these levels to formulate the overall model.

In addition to chunks and generic entities, model formulation appears to be facilitated by the expert's representation of the problem. The representation makes explicit the subproblems that need to be modeled. Experts combine the models for these subproblems to create the model for the overall problem. For example, the expert's representation of a multilocation problem is decomposed by location. This representation allows the modeler to formulate a model for each location, and to link the models later in an appropriate manner. Decomposition into subproblems, followed by the aggregation of the models for these subproblems, is an important characteristic of the model formulation process. The following protocol excerpts support our conjecture of a decomposition/recomposition process.

139 Let me do one thing.

140 Let us do it as a multi-stage problem

141 We will do each transformation followed by (product) routing and then the transportation.

303 Feedstock is broken down into gas stock . . by-products . . and then the blend . . Okay . . regular and premium. I am just going through the product routing so that I can write down the (material) balancing equations.

(expert 4, case 1)

25 Let us take a look at the first time period and see what happens. We can always generalize it later.

## . ..

113 Okay. We need to go from period 1 . . these are all constraints for t equal to 1, 2, . . to 6.

(expert 1, problem 1)

Here, the expert splits the problem into different stages, which are related by activities such as transportation (lines 139–141), and attempts to formulate models for each stage. These partial models are then linked by constraints such as material balance (line 303). A similar process is used in the case of multiperiod problems, where the expert models the problem as a single time period problem first and then generalizes it to a multiperiod problem by adding interperiod constraints (lines 25 and 113).

AssERTioN 4. Experts determine the type of the model by classifying the problemspecific relationships that need to be modeled into categories such as linear, nonlinear, integer, and so on. They also order these model categories by computational tractability and employ such information to formulate tractable models.

Before constructing the mathematical model, the expert is able to determine the type of model, e.g., LP (Linear Programming), IP (Integer Programming), Mixed (a model that combines continuous and integer variables) etc., that will result for the problem based on the characteristics of the data and relationships in it. For example, the expert infers that the mathematical model of a logical relationship (e.g., A or B) will be a mixed integer programming model. Expert modelers order these model types by tractability and use this ordering during model formulation. This results in the use of approximations for nonlinear relationships to enable the formulation of computationally simpler linear models, and in the decomposition (splitting) of mixed integer linear programming models into several linear programming models.

87 Oh, we have got a choice. We have to decide whether we send type I or type 2.

88That involves some integer decision variables.

89 But then we have to decide on the quantity also. So it becomes nonlinear . . mixed nonlinear

90 I don't really want to make it a mixed nonlinear problem,

91 One thing I could do is to split into two models.

92 Or (I can) approximate the convex cost structure by a linear function

(expert 1, case 1, excerpt 1)

125 How are we going to consider this? (He was referring to the nonlinear cost of the pipeline).

126 I guess we can do this as a sort of piecewise linear approximation over different regions of this and include that as additional .

127 well . . I don't know what the function is . . whether quadratic or linear approximation will . .

(expert 4, case 1, excerpt 2)

The first excerpt indicates that the expert concludes that integer variables are needed to formulate the logical relationship that states that either a "type 1" or “type 2" object can be sent through the pipeline (lines 87 and 88). The second excerp illustrates reasoning about the use of approximations to formulate models that are computationally more tractable (lines 92, 127). We interpret this behavior as a search for the model type that is computationally most tractable.

To summarize, at the end of the problem structuring phase, the expert has gathered the relevant data, inferred the relationships that need to be incorporated into the módel (and its type), and synthesized the interactions among the different parts of the problem. The mathematical form of the model is constructed from the qualitative relationships identified in this phase. For example, qualitative statements of resource capacity constraints, material balance, and input-output relationships between processes are made without committing to the exact mathematical forms that these relationships will eventually take.

## 2.2. Model Construction Phase

In the model construction phase, the expert assigns mathematical variables and formulates the relationships identified in the problem structuring phase into mathematical constraints. The assignment of variables is straightforward. The expert assigns a variable to any unknown data that needs to be modeled. However, the formulation of relationships can be complex, as the same qualitative relationship, formulated under different assumptions, and using different methods, can result in structurally different mathematical constraints.

AssERTioN 5. Experts use various “modeling tricks" to formulate computationally simple models.

Experts use modeling tricks as part of formulation methods which prescribe a sequence of steps that are required to formulate mathematical relationships. An example of a “trick" is the formulation of a relationship involving a variable which can take both positive and negative values. Since mathematical programming models, in general, work only with positively valued variables, this presents a problem.

88 The ending inventory can be positive or negative.

89 It involves integer variables? . . Umm . . mixed? (continuous and integer valued variables) ..

90 My problem is that I want to make sure . . a single number . . to prevent from being positive and negative.

91 The classical trick for doing this is to write this as the difference of two variables. So let us take a look at this and see what we have.

92 I+ and I– . . so that is either positive or negative . . That will be my expression. (writes down I+ - I-)

(expert 1, problem 1)

Treating a variable unrestricted in value as the difference between two positively valued variables permits the modeler to formulate the preferred linear formulation and is an example of a modeling trick.

The assertions that we have presented pertain to the model formulation process. Additionally, our analysis also indicates that experts associate components of the mathematical model, viz. variables, constraints, etc., with specific aspects of the problem. For example. experts associate mathematical relationships with generic entities (e.g., the mathematical statement of a capacity constraint with a resource), and variables and parameters with unknown and known quantities. We hypothesize that this association is represented mentally but not articulated explicitly in the model. A preliminary confirmation of this association was obtained when an expert was asked to formulate a revised model for a minor variation of a problem. The expert was able to modify only those portions of the original model that were affected by the change, and reason about the specific form of the changes. Revision of only the affected portions of the model appears to be an important modeling expertise that requires knowledge about the dependencies between model components and the problem features, the interrelationships among model components, and about how changes to a problem specification propagate throughout the model.

Before we proceed to discuss the implications that the assertions have for MOD-FORM's design, we discuss the similarities and differences in the protocols that were collected during our study.

## 2.3. Similarities and Differences Among the Expert Protocols

We observed the modeling process and the assertions discussed in §2.2 in all the expert protocols we collected in our study. However, we did observe some differences in the details, e.g., in the modeling techniques used to create models. In the following we elaborate on the differences (or conflicts) we observed in the expert protocols. We also describe how we have accommodated these differences in the design of MODFORM.

Three types of conflict can potentially arise between experts in our protocol analy sis:

(a) differences in the modeling process,

(b) structural differences in the formulated models, and

(c) differences in the model solutions

We describe each of these in turn, and indicate how we resolved the conflicts, if any, in each case.

2.3.1. Differences in the Modeling Process. In our analysis, we did not find any significant differences in the modeling process used by our expert modelers. All the modelers appeared to use the process depicted in Figure 1.

2.3.2. Structural Differences in the Formulated Models. We did observe structural differences in the models formulated by our experts. These differences appear to be due to the use of different modeling techniques or tricks by the expert modelers. The application of these different techniques yielded structurally different models for the same problem. However, these structurally different models were equivalent in the sense that they all gave the same solution. For example, as illustrated previously, while one expert formulated two linear programming models for the case used in our study, another expert formulated a mixed-linear programming model for the same case using a different set of modeling techniques. We chose to resolve this conflict by representing all the observed modeling techniques in MODFORM. This gives MOD-FORM the ability to formulate a variety of structurally different models. Given a model formulation task MODFORM uses its knowledge about the relative computational tractabilities of different model structures to choose the modeling technique that will result in the computationally simplest model.

2.3.3. Differences in Model Solutions. When the models formulated by an expert were structurally different, and yielded different solutions (i.e., from that of models created by other experts), we consulted with the experts and asked them to explain the differences. In these situations, we found two reasons, human error, and implicit assumptions, which accounted for the differences in the models. Human error accounted for differences such as when an expert formulated an incorrect model because he/she overlooked certain data specified in the problem statement. In this case, the expert simply corrected the model, and the corrected model gave the same solution as the models formulated by other experts. Implicit assumptions about data not given in the problem statement, different from the assumptions made by the other expert modelers, also accounted for differences in model solutions. In this case, when the expert was asked to incorporate the same assumption made by the other experts, the revised model gave the same solution as the other expert models.

## 2.4. Implications for the Design of MODFORM

The assertions that we have made based on our study have directly influenced the design of MODFORM. The first three assertions have influenced the design of the meta-model, the component in MODFORM that encodes the domain knowledge. Assertion 4, which deals with the identification and ordering of model types, was the basis for the organization of the modeling knowledge, and the model formulation process employed by MODFORM. The model construction rules in MODFORM were designed with the help of observations made in Assertion 5. As noted earlier, MODFORM incorporates all the modeling techniques that we could identify in our protocol analysis, and hence can formulate multiple structurally different models for the same problem. However, MODFORM chooses one modeling technique, whenever more than one technique is applicable in a problem, by employing knowledge about the relative tractability of model structures to formulate the simplest (i.e., most tractable) model. Finally, the dependency networks used in MODFORM to support model revision are based on the ability of expert modelers to identify and revise only those model components affected by changes made elsewhere in the problem specification.

## 3. An Overview of MODFORM

MODFORM is a knowledge-based tool designed to support the formulation and revision of mathematical programming models in the production planning domain. In this section, we introduce the principal components of MODFORM, and using an example, provide an overview of its support for model formulation and revision. Each of the components is described in detail in the following sections. Figure 2 illustrates the information flow in MODFORM. There are two principal components in MODFORM: the meta-model, which encodes the production planning domain knowledge, and the modeling component, which encodes the model building knowledge. We describe each in turn.

## 3.1. Meta-model

The meta-model is the repository of domain knowledge in MODFORM. It is organized using a collection of interrelated object types which correspond to the generic entities (cf., Assertion 1) of the production planning domain (e.g., product, resource, activity, location). Problems are specified in MODFORM using instances of these object types. Consider the following production planning problem which we use illustratively through the rest of the paper:

A manufacturer produces product P at a plant using raw material RM and labor L. He has the option of producing the product using an automatic or a manual process. An automatic process requires only RM. The manual process requires both RM and L. There are limits on the availabilities of RM and L. The manufacturer sells P at the plant and at a warehouse which is located at a geographically different location. P is transported from the plant to the warehouse, which incurs a cost. The manufacturer is cl utilization-of-labor <= availability-of-labor c2 utilization-of-RM <= availability-of-RM c3 amount-of-P-transported-from-plant-to-ware-house <= capacity-of-the-route c4 amount-of-P-sold-in-plant <= demand-for-P-in-plant c5 amount-of-P-sold-in-warehouse <= demand-for-P-in-warehouse c6 (xor automatic manual) c7 out-flow-of-P-from-plant <= inflow-of-P-into-plant c8 out-flow-of-P-from-warehouse <= inflow-of-P-into-warehouse c9 amount-of-P-produced-in-automatic = f(amount-of-RM-used-in-automatic) c10 amount-of-P-produced-in-manual = f(amount-of-RM-used-in-manual, amount-of-laborused-in-manual)

![](/api/attachments/HN7V3S6Y/fulltext/images/4881400f6c5ec4449d8a1f8ec7a426f39ce74131e6f3441b2c8b577422b21aa0.jpg)  
FiGURE 2. Information Flow in MODFORM.

FiGURE 3. Qualitative Model for the Example Problem.

interested in formulating a model to maximize his profit. It is assumed that all the relationships are linear.

The problem is specified in MODFORM (by a user) using instances of object types in the meta-model. This consists of relating the underlined terms in our example to the meta-model object types. A fragment of the problem specification in MOD-FORM is shown below. The meta-model object types are highlighted.

(product P) (P is a product)

(resource RM) (RM is a resource)

(location plant) (plant is a location)

(produce P plant) (P is produced at the plant)

(sell P plant) (P is sold at the plant)

## 3.2. Qualitative Modeling Rules

Each object type in the meta-model has an associated set of qualitative modeling rules. These rules model the expectations invoked in the minds of modelers when a generic entity is encountered (cf., Assertions 1 and 2). An example of such a rule is

IF X is a resource

THEN add the following constraint to the qualitative model:

utilization-of-X <= availability-of-X

When RM is specified to be an instance of a resource (as shown above), this rule immediately asserts the following qualitative constraint:

$$
\text { utilization - of - RM } <   = \text { availability - of - RM }.
$$

Problem specification in MODFORM thus results in a collection of relationships asserted by the qualitative modeling rules attached to meta-model object types.

## 3.3. Synthesis Rules

The relationships asserted by the qualitative modeling rules are refined by synthesis rules. These are also attached to the object types in the meta-model. The synthesis rules refine the terms in a qualitative relationship using knowledge about the interrelationships between attributes of related object types (cf., Assertion 3). An example of a synthesis rule is:

IF resource X is used in process Y

THEN the attribute utilization of resource X is increased by an amount equal to the attribute amount-of-resource-X-used of process Y.

This rule refines the utilization of a resource by relating it to its usage in a specific process. In our example, this rule will successively refine the term utilization-of-RM (the LHS of the qualitative constraint) by relating it to the amount of RM (a resource) used in the manual and automatic process respectively. This results in:

$$
\text { utilization - of - RM } = \text { amount - of - RM - used - in - manual - process }
$$

\+ amount-of-RM-used-in-automatic-process.

## 3.4. Summary

To summarize, problems are specified using instances of object types in the metamodel. The qualitative modeling rules attached to these objects assert relationships

Maximize

$$
P _ {1} X _ {1} + P _ {1} X _ {2} - C _ {1} (X _ {3} + X _ {4}) - C _ {2} X _ {4} - C _ {3} X _ {5}\tag{1}
$$

$$
\text { subject   to }
$$

$$
X _ {3} + X _ {8} <   = M _ {R M}
$$

$$
X _ {4} <   = M _ {L A B}\tag{2}
$$

$$
X _ {3} - a _ {1} X _ {6} = 0\tag{3}
$$

(4)

$$
X _ {4} - a _ {2} X _ {6} = 0\tag{5}
$$

$$
X _ {8} - a _ {3} X _ {7} = 0\tag{6}
$$

$$
X _ {1} + X _ {5} - X _ {6} - X _ {7} <   = 0\tag{7}
$$

$$
X _ {2} - X _ {5} <   = 0\tag{8}
$$

$$
X _ {6} - M \operatorname{Int} _ {1} <   = 0\tag{9}
$$

$$
X _ {7} - M \operatorname{Int} _ {2} <   = 0\tag{10}
$$

$$
\operatorname{Int} _ {1} + \operatorname{Int} _ {2} = 1\tag{11}
$$

$$
X _ {5} <   = M _ {P - W H}\tag{12}
$$

$$
\text { All } X > = 0
$$

All Int are 0-1 integers

Where $P _ { 1 }$ = unit price of product $\pmb { P }$

$M _ { R M }$ = amount of RM available

$M _ { L A B }$ = amount of labor available

$M _ { P \cdot W H }$ = capacity of the transportation route

${ \pmb a } _ { 1 }$ = amount of RM needed to produce a unit of P

$\pmb { a _ { 2 } }$ = amount of labor needed to produce a unit of P

$c _ { 1 }$ = unit cost of RM

$c _ { 2 }$ = unit cost of labor

$c _ { 3 }$ = cost of transporting a unit of P from plant to warehouse

$X _ { 1 }$ = amount of $\mathbf { \nabla } \cdot \mathbf { p }$ sold at the plant

$\pmb { X _ { 2 } }$ = amount of $\mathbf { \nabla } _ { \mathbf { \mathcal { P } } }$ sold at the warehouse

$\pmb { X _ { 3 } }$ = amount of RM used in the manual process

$\pmb { \chi } _ { \pmb { \mathscr { s } } }$ = amount of labor used in the manual process

$\pmb { X } _ { \pmb { \mathscr { s } } }$ = amount of P transported from the plant to the warehouse

$\pmb { \chi } _ { \pmb { \delta } }$ = amount of P produced using the manual process

$\pmb { X _ { \ 7 } }$ = amount of P produced using the automatic process $\pmb { P }$

$X _ { 8 }$ = amount of RM used in the automatic process

Int, = 1 if the manual process is used, 0 if the automatic process is used

$\mathbf { \Pi } _ { \mathbf { I } \mathbf { n } \mathbf { t } _ { 2 } } = \mathbf { \Omega } _ { 1 }$ if the automatic process is used, 0 if the manual process is used

FIGURE 4. A Mathematical Model for the Example Problem.

![](/api/attachments/HN7V3S6Y/fulltext/images/54b42d06078d26de4d2dbb3be90fc8c623a383cdc482246dd21f81bae65b37ff.jpg)  
FIGURE 5. A Fragment of the Dependency Network.

which are further refined by synthesis rules. This results in a qualitative model of the problem (Figure 3). The next step in MODFORM is to formulate mathematical relationships between the terms related in the qualitative model.

## 3.5. Modeling Component

MODFORM uses two types of modeling knowledge: model construction rules, and type determination rules. Model construction rules are formulation methods. They prescribe a sequence of steps (e.g., assign variables, perform transformations) that can be used to formulate mathematical relationships (cf., Assertion 5). Type determination rules are rules about the type of models (e.g., LP, IP, etc.) that will result when a particular model construction rule is applied. Additionally, MOD-FORM has knowledge about the ease with which each of these model types can be solved (cf., Assertion 5). For example, LP models are simpler to solve than IP models (cf., Assertion 5). Using this modeling knowledge, MODFORM searches through the space of possible formulations, and assigns a formulation method to each element of the qualitative model with the objective of formulating the simplest possible mathematical model. The application of the assigned formulation methods creates the mathematical model. The mathematical model formulated for our example is in Figure 4. Details about these formulation methods and the search process used to select them are described in §4.

## 3.6. Model Revision

Modeling is an iterative, evolutionary process. To accommodate this feature, the problem specification, the qualitative model, and the mathematical model can be modified by the user in MODFORM. However, modifications induce other changes. MODFORM explicitly maintains a network of dependencies between the object instances used in problem specification, the qualitative relationships, and the mathematical model. This dependency network is used to identify the induced effects of changes which are then propagated. A fragment of the dependency network (represented as an AND-OR graph) for our example problem is shown in Figure 5.

To illustrate the usefulness of such a network, consider the mathematical relationship that specifies the resource capacity constraint $( X _ { 3 } + X _ { 8 } < = M _ { R M } )$ . It depends on the qualitative resource capacity constraint (availability-of-RM <= utilization-of-RM), and the formulation method úsed. The qualitative constraint in turn depends on the asserted object instance (i.e., RM) that is part of the problem specification. A change that deletes RM from the problem specification can then be used to identify and exclude the relationships that depend on it from the model. Additionally, the network of dependencies can be queried to understand the relationships between the mathematical model and the elements of the problem specification. Finally, with some minor variations, the dependency network can be modified to support the exploration of multiple alternative scenarios, each corresponding to a unique model version. For example, the modeler might explore a scenario in which raw materials are present in the problem specification and another in which they are not. The dependency network which is the basis for all this functionality is managed and maintained by a Belief Maintenance System (BMS) in MODFORM. The details of the BMS are beyond the scope of this paper and may be found in Raghunathan et al. (1990).

## 4. MODFORM: Implementation Details

In this section, we elaborate on the organizational features of the meta-model and provide a detailed discussion of the various aspects of the modeling process in MOD-FORM. In each case we illustrate our discussion using the representational structures used in our implementation. MODFORM has been implemented using Common Lisp and Flavors, an object-oriented language (Weinrab and Moon 1981) on a VAX 8600 system. We begin with a discussion of the meta-model.

## 4.1. Meta-model

The meta-model is the sole repository of domain knowledge in MODFORM. It consists of a collection of interrelated domain object types, instances of which are used to specify problems. These object types have qualitative modeling rules and synthesis rules attached to them. When a problem is specified in terms of these object types, these rules formulate a refined qualitative model of the problem which are then used as input to the mathematical modeling component in MODFORM. These aspects of the meta-model were described in §3. In this section, we discuss the organization of the object types in the meta-model and discuss the representational structures used in the implementation.

In §2 (cf. Assertion 3), we noted that problem decomposition is an important feature of the model development strategy used by expert modelers. The decomposition centered around specific types of entities that were part of a problem specification. Thus, for example, in a multilocation problem, the problem was decomposed by location. If MODFORM is to be capable of making such a decomposition, the entities around which decomposition can be made should be “first-class" objects in the problem specification. Based on this observation, the meta-model is organized hierarchically around a class of object types as shown in Figure 6.

The root object type of the hierarchy is the physical-system. The physical-system consists of the location, activity, and entity object types. Each of these obiect types is refined using a hierarchy of subtypes. Thus, for example, production, transportation, selling, buying, and storage are subtypes of the activity object type. Product, process, and resource are subtypes of the entity object type and so on. These object types and their subtypes provide a vocabulary of production planning concepts that modelers can use to specify problems. Additionally, their hierarchical organization makes problem decomposition explicit.

![](/api/attachments/HN7V3S6Y/fulltext/images/b0f619c16683d9ccdc73a68a25507cf3cf28c385c1b199effaf8adef2025a062.jpg)  
FIGURE 6.· The Meta-model.

Each object type has a number of attributes. Several of these are used to represent interrelationships between object types. We use the activity object type and its subtype transportation to illustrate our discussion.

<table><tr><td colspan="2">OBJECT TYPE</td><td>OBJECT TYPE</td></tr><tr><td>name:</td><td>activity</td><td>name: transportation</td></tr><tr><td>child-of:</td><td>physical-system</td><td>child-of: activity</td></tr><tr><td>parent-of:</td><td>(production transportation selling buying storage)</td><td>location-from:  $\langle location \rangle$ </td></tr><tr><td>attributes:</td><td>(acts-on:  $\langle set-of-entities \rangle$ uses:  $\langle set-of-entities \rangle$ max-level-of-activity:  $\langle constraint-type \rangle$ min-level-of-activity:  $\langle constraint-type \rangle$ cost:  $\langle constraint-type \rangle$ )</td><td>location-to:  $\langle location \rangle$ </td></tr></table>

Each activity operates on a set of entities and uses a set of resources. These are represented by the attributes acts-on and uses respectively. Max-level-of-activity and min-level-of-activity represent the maximum and minimum measures of the level of activity. Cost represents the unit cost incurred in performing the activity. A subtype inherits the attributes of a parent object type. Thus, transportation inherits all the attributes of the activity object type. In addition, it has two attributes location-to and location-from which represent the origin and destination locations of the transportation activity.

Problems are specified by creating instances of these object types. The object instances used to specify the raw-material, RM, and the transportation activity, transport-P, of our example problem are shown below.

<table><tr><td colspan="2">OBJECT INSTANCE</td><td>OBJECT INSTANCE</td></tr><tr><td>identifier:</td><td> $RM$ </td><td>identifier: transport- $P$ </td></tr><tr><td>instance-of:</td><td>resource</td><td>instance-of: transport</td></tr><tr><td>availability:</td><td> $M_{RM}$ </td><td>uses: ( )</td></tr><tr><td>utilization:</td><td></td><td>acts-on:  $P$ </td></tr><tr><td>cost:</td><td> $C_1$ </td><td>max-level-of-activity:  $M_{P-WH}$ </td></tr><tr><td></td><td></td><td>min-level-of-activity: 0</td></tr><tr><td></td><td></td><td>location-from: plant</td></tr><tr><td></td><td></td><td>location-to: warehouse</td></tr><tr><td></td><td></td><td>cost:  $C_3$ </td></tr></table>

We note that only some of the attributes of the instances (e.g., availability of RM, min-level of activity of transport-P) have values assigned to them. These values can be symbolic identifiers of other object instances (e.g., P), or symbols $( e . g . , C _ { 3 } )$ Attributes that have not been assigned values are related by MODFORM to other attributes (those that may or may not have a value) using qualitative modeling rules and synthesis rules. An example is the attribute utilization-of-RM. It does not have a value, and as described in §3, it is related to the other attributes as shown below:

$$
u t i l i z a t i o n - o f - R M = a m o u n t - o f - R M - u s e d - i n - m a n u a l - p r o c e s s
$$

\+ amount-of-RM-used-in-automatic-process.

This is eventually transformed by the modeling component into a mathematical relationship. We now turn to a description of the modeling knowledge base in MOD-FORM and a discussion of the process it uses to formulate models

## 4.2. The Modeling Component

As introduced in §3, the modeling component in MODFORM uses two types of modeling knowledge: model construction rules and type determination rules. The model construction rules are formulation methods that prescribe a sequence of steps that are required to formulate mathematical relationships. Type determination rules infer the type of model (e.g., LP, IP) that will result when a given model construction rule is applied. Additionally, MODFORM also has knowledge about the computation tractability of model types (e.g., LPs are easier to solve than IPs). Given a qualitative model and the goal of formulating a mathematical model, MODFORM searches through the space of available formulation methods and chooses method(s) which will result in the computationally most tractable model type. In this section, we will introduce representations used in this component, provide examples of formulation methods and type determination rules, and describe the model formulation process in detail.

4.2.1. Model Representation. The modeling component works with two kinds of models: the qualitative model (its input) and the mathematical model (its output). Both these models are represented as a collection of expressions. For instance, the qualitative model of our example problem (Figure 3) consists of a logical expression (element c6) and relational expressions (everything else). The mathematical model (Figure 4) consists of a function expression (the objective function) and several relational expressions (the constraints). Each of these expressions are made up of simpler expression types. For instance, a relational expression consists of a relational operator (e.g., =, <=) and functional expressions (the left-hand and right-hand sides, respectively). This hierarchical classification and definition of expressions are represented as a class of object types in MODFORM². Examples of a model, expression, and a logical expression type are given below.

OBJECT TYPE

OBJECT TYPE

name: model

name: expression

parent-of: (expression) parent-of: (logical-expression relational-expression . . constant)

child-of: () attributes: (type: )

child-of: (model)

attributes: (operator: <operator-type> arguments: 〈expression-types> formulation-methods: 〈set-of-rules)

Raghunathan • Krishnan • May

OBJECT TYPE

name: logical-expression

parent-of: ()

child-of:(expression)

formulation-methods: (general-purpose special-trick-1 special-trick-2)

There are five subtypes of expression: logical, relational, function, variable, and constant. Each expression type has two attributes that are used to represent its structure; its operator, and the arguments to the operator. For example, the expression availabilitv-of-RM <= utilization-of-RM has <= as its operator and the terms related by it as its arguments. These arguments can themselves be instances of other expressions. In our example, utilization-of-RM is a function expression, and the availability-of-RM is a constant. The type attribute of an expression specifies the mathematical type of the expression; linear, mixed, nonlinear, and so on. Finally, each expression has an associated set of named model formulation methods. Each method corresponds to a model construction rule.³ Model formulation consists of choosing a formulation method that will result in the desired model type.

4.2.2. Model Construction Rules. Model construction rules prescribe a sequence of steps required to transform a given expression type into a mathematical relationship. The complexity of these sequences of steps is a function of the expression type. Relational and function expressions have simple formulation methods as opposed to the formulation methods for logical expressions. We will provide examples of both these types of formulation methods. We begin with the formulation methods for relational and functional expressions.

The method used to formulate a relational expression exploits its structure. The rule decomposes the expression into its constituent parts, formulates mathematical relationships for these parts, and synthesizes these parts using the relational operator. This logic is encoded in the general-purpose formulation method for relational expressions:

IF the expression is relational and

the formulation method is general-purpose

THEN

formulate the arguments into mathematical representations relate these mathematical representations by the corresponding relational operator.

Consider the constraint c1 in the qualitative model of our example (Figure 3). It is a relational expression whose arguments, the terms utilization-of-RM and availabilitv-of-RM are related by the <= operator. While the term utilization-of-RM is a function expression (cf. §4.2.1) with amount-of-RM-used-in-automatic + amount-of-RM-used-in-manual as its value, availability is a constant expression with a symbolic constant $M _ { R M }$ as its value. Since the terms that define the functional expression cannot be further decomposed,4 they are each assigned a variable, say $X _ { 3 }$ and $X _ { 8 }$ , and the mathematical formulation of the function expression is $X _ { 3 } + X _ { 8 }$ . This is related to the symbolic constant $M _ { R M }$ using the <= operator to yield the mathematical formulation for the expression c1 as $X _ { 3 } + X _ { 8 } < = M _ { R M }$

The formulation methods for logical expressions combine the decomposition strategy used to formulate relational expressions with specialized knowledge about the mappings between Boolean expressions and their mathematical equivalents. Each Boolean argument of a logical expression is mapped to a 0-1 binary variable and related as shown below:

Logical Expression

Mathematical Representation

A OR B

A AND B

IFA THEN B

IF A THEN B ELSE C

$$
\begin{array}{l} \operatorname{Int} _ {1} + \operatorname{Int} _ {2} > = 1 \\ \operatorname{Int} _ {1} = 1, \operatorname{Int} _ {2} = 1 \\ \operatorname{Int} _ {1} - \operatorname{Int} _ {2} <   = 0 \\ \operatorname{Int} _ {1} - \operatorname{Int} _ {2} <   = 0 \\ (1 - \operatorname{Int} _ {1}) - \operatorname{Int} _ {3} <   = 0 \\ \operatorname{Int} _ {2} + \operatorname{Int} _ {3} = 1 \end{array}
$$

The symbols $A , B ,$ etc. represent Boolean arguments, while the symbols such as $\mathbf { I n t } _ { 1 }$ denote binary variables. This table of mappings is sufficient as a formulation method only when the Boolean arguments are simple variables. If the Boolean arguments are complex relational expressions, the formulation methods need to combine the steps required to formulate the relational expression with the table of mappings. This integration can be done in several ways and result in multiple formulation methods. We illustrate these types of formulation methods w th a simple example.

Consider the following statement of a quantity discount policy as a logical expression. If(amount-of- $P { \ - } s 0 1 0 > = Q )$ then (price-of- $\pmb { P } = \pmb { P } _ { 2 } )$ else $( \mathrm { p r i c e } { \cdot } \mathbf { \sigma } { \cdot } \mathbf { \sigma } \mathbf { f } { \cdot } P = P _ { 1 } ) $ where $P _ { 1 } > P _ { 2 }$ . Each of the Boolean arguments of this logical expression is a relational expression (e.g., amount-of- $P { \cdot } { \mathrm { s o l d } } > = Q )$ . The table of mappings alone is insuffi cient to formulate the mathematical model. It needs to be combined with the formulation of the relational expression that defines the Boolean argument. The first formulation method that accomplishes this integration is the general-purpose formulation method. The integrative step is highlighted.

IF the expression is logical and

the formulation method is general-purpose

THEN formulate the arguments expressions into mathematical representations. assign an integer (binary) variable for each argument expression. link the integer variables to argument expressions using the method

f integer variable $- f \ast \left( 1 - i n t e g e r \nu a r i a b l e \right) < = \left( \bar { \mathrm { o r } } > = \right) 0$

if the argument is $f < = ( \sigma \mathrm { r } > = ) 0$

use elementary rules to transform the logical expression using the assigned integer variables.

The application of the steps of this method results in the following model of the quantity discount policy:

$$
(X _ {1} - Q) * \mathrm{INT} _ {1} - (X _ {1} - Q) * (1 - \mathrm{INT} _ {1}) > = 0
$$

$$
(P - P _ {1}) * \mathrm{INT} _ {2} = 0
$$

$$
(P - P _ {2}) * \mathrm{INT} _ {3} = 0
$$

$$
\mathrm{INT} _ {1} - \mathrm{INT} _ {2} <   = 0
$$

$$
(1 - \mathrm{INT} _ {1}) - \mathrm{INT} _ {3} <   = 0
$$

$$
\mathrm{INT} _ {2} + \mathrm{INT} _ {3} = 1
$$

$\mathbf { I N T _ { 1 } } , \mathbf { I N T _ { 2 } } , \mathbf { a n d } \mathbf { I N T _ { 3 } }$ are 0-1 integer variables.

The continuous variables $X _ { 1 }$ and P denote the amount sold and the price respectively. These have been assigned as a result of applying step 1 of the rule. Each relational expression that defines a Boolean argument in the quantity discount policy is assigned a binary variable $( \mathbf { I n t } _ { 1 } , \ldots , \mathbf { I n t } _ { 3 } )$ as a result of applying step 2 of the rule. The first three constraints are the result of integrating these binary variables into the mathematical formulation of the relational expressions. The last two constraints are derived directly from the mapping table. The resulting model is a mixed-integer nonlinear model.

Another formulation method that accomplishes the same integration using a different approach is the special-trick-1 formulation method. The integrative step is highlighted:

IF the expression is logical and

the formulation method is special-trick-1

THEN

formulate the argument expressions nto mathematical representations. assign an integer variable for each argument expression.

link the integer variables to argument expressions using the methods: If the argument is $\scriptstyle f > = 0$ then

f- M\*(1-integer variable) $\mathbf { \hat { \mu } } > = \mathbf { 0 }$ where M is the maximum value of f If the argument is $\scriptstyle f < = 0$ then

$f - m { * } ( 1 { \mathrm { - } } i n t e g e r \nu a r i a b l e ) < = 0$ where m is the minimum value of f use elementary rules to transform the logical expression using the assigned integer variables.

This method uses an alternate approach to link the binary variables used to formulate the logical expression with the formulation of the relational expression that specifies the Boolean arguments. The approach results in the computationally more tractable integer linear model if the relational expression (the function f in the rule) that specifies the Boolean condition (as is the case in our example) is linear. However, the approach requires the estimation of M, the maximum value off, or m, the minimum value off. The type determination rules coupled with knowledge about the tractability of model types are used to make tradeoffs between competing formulation methods during the course of model formulation.

MODFORM treats multiple-time period problems, i.e., those that involve inventory equations, using the following rule:

IF number of time periods >= 1

THEN add a time subscript to all the mathematical variables

For each product P stored in location L

formulate the following expressions:

amount-of-P-stored-in-L-at-0 = 〈value provided by the user>

add the following to the model;

“t ranges from 0 to <number of time periods >"

MODFORM uses subscripts only to model the time dimension. In all other cases individual variables are assigned. For instance, if a production planning problem states that five different products are produced then MODFORM will assign five different variables to indicate the production quantities. Thus, the final model is really a model instance rather than a model schema.

4.2.3. Type Determination Rules. Type determination rules reason about the model types that will result from the application of model construction rules. Thus, MODFORM can reason about its available construction rules, and apply that rule which satisfies its requirement. This is similar to the behavior that expert modelers display during model formulation (cf., Assertion 4). The following are some examples of type determination rules that can reason about the model construction rules discussed in the previous section:

IF expression A is logical and

the formulation method is general-purpose

THEN type of expression A is mixed-nonlinear.

Note that the general-purpose rule for the quantity discount policy, a logical expression, described in the previous section resulted in a mixed-nonlinear model. Another type determination rule is:

## IF expression A is logical and

the arguments of A are relational and of type linear and

the formulation method is special-trick-1

THEN type of expression is mixed-integer-linear.

This rule reasons about the application of the special-trick-1 rule discussed in the last section. As we noted, the application of this rule results in a mixed-integer-linear model if the relational expressions are linear.

## 4.3. The Modeling Process

MODFORM uses a search process to formulate a mathematical programming model. Using a state space search metaphor, we can describe the process in terms of its initial state, goal states, and the operators used to move from one state to another. The initial state is the set of expressions that make up the qualitative model. None of these expressions have an assigned formulation method in the initial state. Figure 7 is the initial state for our example problem. The goal state is the qualitative model with a formulation method assigned to each assertion. Figure 8 is a goal state for our example problem. The modeler may also impose a model type constraint on the goal state (e.g., the model should be an LP). The operators are the available formulation methods. The knowledge about the differences in computational tractability of model types is used to control the search.

![](/api/attachments/HN7V3S6Y/fulltext/images/19c2cc9fda0a16abe8e048c23867570f9c9a6325c1b8eec460e90a3c106bef69.jpg)  
FIGURE 7. The Initial State of the Search Process.

4.3.1. Modeling as Search. The search procedure used in MODFORM is quite straightforward. It begins by taking the first expression in the qualitative model (the initial state) and considering all the methods that can be used to formulate it. The assignment of a formulation method to an expression results in a new state. If the first expression has N formulation methods available, then the search process generates N successor states. Type determination rules determine the model type that will result in each of these successor states. For example, in Figure 9, MODFORM determines that, in state s2, the application of general-purpose method to expression c1 of the qualitative model will result in an LP model. Once the types of all N generated states are determined, the modeler has N possible states to explore next. MODFORM chooses the state that has the (computationally) simplest model type, and the process is repeated.⁵ Ultimately, it assigns a formulation method for each of the expressions, and exhausts all the paths that lead to models of the same complexity. The goal state(s) contains the qualitative model, a formulation method assigned to each expression, the type of the mathematical model, and reasons for the type. In our example. the model type that results is a mixed-integer-LP caused by the inclusion of the expression c6 in the qualitative model (Figure 3). The object representation specifically used to facilitate this search process is shown below:

## OBJECT TYPE

name: state

expressions: list-of-expressions>

assigned-formulation-methods: list-of-formulation-methods>

type: 〈model-type〉

reason-for-type: <list-of-expressions>.

The attribute expressions in the above object type contains the expressions in the qualitative model. The attribute assigned-formulation-methods contains the formulation methods to be used to formulate expressions in a given state. Type indicates the type of the mathematical model that will result by applying these assigned methods. Reason-for-type identifies the expression that is responsible for the model type in a state.

![](/api/attachments/HN7V3S6Y/fulltext/images/d776ef820e509cfb235380dc2e08e4e88ee6893ec2b1e42154a85afe08d447b9.jpg)  
FIGURE 8. A Final State.

When the search process is complete, three cases can occur

(1) there is only one final state and its model type is the desired type,

(2) there are multiple final states of the desired model type,

(3) there are one or more final states whose model types are not the desired type

![](/api/attachments/HN7V3S6Y/fulltext/images/79eb95fe466fbe3dad55a946575f1d88a334a07283669a58c5246d3af89c20b4.jpg)  
FiGURE 9. A Segment of the Search Space

The action that MODFORM takes in case 1 is trivial. It can formulate only one model that will be of the desired type, and hence proceeds to construct the model by applying the assigned formulation methods. Case 2 is slightly more interesting than case 1, because it involves choosing a model from a set of models, all of which have the same type. MODFORM currently either chooses a model arbitrarily, and applies the assigned formulation methods or formulates all models if explicitly directed by the user to do so. An alternative approach would be to compare the alternatives based on attributes such as structural parameters (i.e., number of variables, constraints etc.). Case 3 is the most interesting of all. Here, MODFORM is not in a position to formulate a model of the desired type. In this case, it identifies the expressions that prevent it from formulating a model of the desired type. These “culprit" expressions need to be approximated by the user if MODFORM is to formulate models of the desired type. For example, if the user desires an LP model for the problem, then MODFORM indicates that the user has to approximate c6 to obtain an LP model. However, MODFORM lacks the knowledge to make or suggest approximations, as expert human modelers often do during the modeling process. It is the responsibility of the user to determine appropriate approximations in his/her situation.

To summarize, MODFORM conducts a search through a space of formulations. This concludes with the assignment of formulation methods to expressions in the qualitative model. These methods are applied to construct the algebraic formulation of the mathematical model. This formulation can then be solved using the appropriate solver (e.g., LINDO, GAMS). If alternative scenarios need to be explored, the modeler can use the model revision features (cf. §3.3) to investigate alternative formulations.

## 5. Experiments with MODFORM

We conducted an experiment to test whether MODFORM supports users in the formulation of mathematical programming models for production planning problems. The subjects who participated in the experiment were individuals with limited experience in modeling. They formulated LP and mixed-integer-LP models with and without the help of MODFORM. We used model correctness as the performance variable. The results were then analyzed to verify the hypothesis that naive users are able to formulate better models with the help of MODFORM.

## 5.1. Methodology and Results

Twenty undergraduate and graduate students were recruited for the experiment. All had some background knowledge about mathematical programming models but had limited experience in model formulation. The subjects were first given a simple product-mix problem as a pretest, to determine the extent of their model formulation expertise. Only those who did not formulate correct models for the problem were chosen to participate in the experiment. Participation was entirely voluntary. No monetary remuneration was given for participation.

The problems were selected from Johnson and Montgomery (1974), and Williams (1984). The first problem was expected to be formulated as an LP model; the second one as a mixed-integer-LP model. Our experimental design was as follows.

All the subjects formulated models for both the problems. All of them formulated models with and without the help of MODFORM. This design allowed us to use subjects as their own controls and also to double the number of observations. To avoid the learning-effect bias that might arise with a single subject modeling the same problem twice, we randomized the order in which the subjects formulated models with and without MODFORM. In our design, the order in which the subjects were presented two problems as well as the order in which they used MODFORM for a problem were randomized. Thus, if there was a learning-effect bias, it was neutralized over the entire sample. There is a second reason why learning-effect bias is not a significant problem in our experimental design. When the subjects did not use MOD-FORM, they had to use their own modeling knowledge to formulate models for problems. However, when they used MODFORM, they were simply required to identify and specify the entities in the problem and the values of their attributes. Thus, the subject did not formulate the model, MODFORM did. To summarize, when the subjects used MODFORM, the subjects analyzed the problem to gather qualitative knowledge about the problem. They stated this qualitative knowledge using the MODFORM vocabulary. When the subjects did not use MODFORM, they had to use modeling knowledge.

The models formulated by the subjects, with and without MODFORM, were graded for correctness by comparing them with the models developed by a human expert. It was not required that the model have exactly the same structure as the expert's model. If the model formulated by the user gave the same solution as the human expert's model it was considered correct. Model correctness was treated in a univariate and a multivariate fashion. In univariate analysis, models were graded as either correct or incorrect. The multivariate analysis included components of the mathematical model. A mathematical programming model may be viewed as consisting of various components, such as the objective function, constraints, variables, and coefficients. The correctness of a model was determined by grading each of these dimensions using a grading scheme, shown in Figure 10, and standardizing the total to a percentage.

The results of the experiment are tabulated in Figure 1 1. When the score for model correctness was calculated using the grading scheme, the average score obtained by subjects improved from 70.46 to 98.09, when they used MODFORM. The score of 98.09 indicates that subjects were almost always able to formulate correct models. Another interesting observation is that the variance of the scores of subjects declined significantly, from 19.24 to 5.06, when they used MODFORM. This may indicate that even users with different levels of model formulation expertise, as evidenced by the high variance in their scores, are able to perform equally well using MODFORM, as evidenced by the low variance when they used MODFORM.

When model correctness was considered in a univariate fashion, we obtained similar results. These results indicate that the system appears to help improve the modeling performance of naive users.

OBJECTIVE FUNCTION

3 points

CONSTRAINTS

3 points for each correct constraint

VARIABLES

COEFFICIENTS

2 points for each correct variable

1 point for each correct coefficient

FIGURE 10. Grading Scheme.

<table><tr><td rowspan="2"></td><td colspan="2">Subject alone</td><td colspan="2">Subject+ MODFORM</td><td rowspan="2">T-score (dof)</td><td rowspan="2">p-value</td></tr><tr><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td></tr><tr><td>partial score</td><td>70.46</td><td>19.24</td><td>98.09</td><td>5.06</td><td>9.36 (39)</td><td>0.000</td></tr><tr><td>correct/wrong</td><td>7.5</td><td>7.89</td><td>87.5</td><td>5.12</td><td>8.56 (39)</td><td>0.000</td></tr></table>

FIGURE 11. Experimental Results (Within-subjects Design).

Our experimental design also permits the between-subjects analysis. This is due to the fact that both the order in which the subjects were presented the two problems as well as the order in which they used MODFORM for a problem were randomized. We separated the subjects who participated in our experiment into two groups; the first group consisted of subjects who used MODFORM first formulate the model for a problem and the second group consisted of subjects who first formulated models on their own. We ignored the models these subjects formulated subsequently for the same problem. The results for the between-subjects design are summarized in Figure 12. We note that the results are similar to Figure 11 and indicate that the modeling performance of users improved with MODFORM. However, the results are illustrative rather than conclusive because the sample size was small, and the grading scheme is very subjective.

## 5.2. Limitations

Although no claim can be made, in a statistical sense, about the experimental results, the experiment did provide us information which can be used to improve MODFORM. First, models generated by MODFORM always had the same or computationally simpler types than the models generated by the expert. The MOD-FORM generated models can be considered better in that respect. A possible reason for the superiority could be that MODFORM conducts a more complete search of its knowledge-base to determine the simplest model that might be formulated.

Second, the models formulated by MODFORM always had more constraints and variables than those of the human expert. A reason for that difference is the lack of model simplification knowledge in MODFORM. Model simplifications and alternate model formulations are especially significant in the case of IP models, because the structure of the model may determine the computational time required to solve it (Williams 1974).

Third, users formulated wrong models, even with the help of MODFORM, for a variety of reasons. First, the domain knowledge in MODFORM is incomplete. For example, there are different terms, such as scrap rate and operation, used in production domain that are not represented in MODFORM. In such cases, it was the responsibility of the user to transform the concepts into ones representable in MODFORM. Second, the modeling knowledge is also incomplete. For example, MODFORM is incapable of formulating “ratio" constraints. We believe that these limitations can be removed by the refinement of the meta-model and the modeling knowledge used by MODFORM.

<table><tr><td rowspan="2"></td><td colspan="2">Subject alone</td><td colspan="2">Subject+ MODFORM</td><td rowspan="2">T-score (dof)</td><td rowspan="2">p-value</td></tr><tr><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td></tr><tr><td>partial score</td><td>72.13</td><td>18.15</td><td>99.55</td><td>6.23</td><td>6.35 (38)</td><td>0.000</td></tr><tr><td>correct/wrong</td><td>11.11</td><td>9.90</td><td>91.0</td><td>8.19</td><td>9.78 (38)</td><td>0.000</td></tr></table>

FiGURE 12. Experimental Results (Between-subjects Design)

## 6. Conclusions

MODFORM is a modeling support tool which can be used by naive users in the formulation and maintenance of mathematical programming models in the production planning domain. It has been designed on the basis of empirical investigation of the modeling process of several experienced modelers. Our analysis indicates that modeling is a synthetic process, in which domain knowledge and modeling principles together help a modeler formulate an appropriate model. Our analysis of the protocols led to the architecture of MODFORM that formulates the model from a problem description by generating a qualitative model, and then transforming it into a mathematical model. It also explicitly represents the justifications or reasons for formulating a specific model. The representation of such justifications allows MODFORM to support the evolutionary nature of modeling process. An experiment conducted with several naive users formulating models with MODFORM indicates that they are able to formulate better models with the help of MODFORM.

While MODFORM is intended for use in the production planning domain, we hypothesize that the same architecture with minor changes can be used to support modeling in other domains. Note that the modeling knowledge, the BMS, and the modeling process in MODFORM are domain independent. The meta-model is the only domain-specific component and will need to be redesigned. However, the structure provided by the objects, the qualitative modeling rules, the synthesis rules, and the dependency rules can serve as a framework to support this task.

Another important avenue for further research is in the suggestion of approximations that can be used in a problem. Currently, MODFORM does not possess any knowledge about approximations that can be made in a problem. In our current implementation, the user has the responsibility to generate and make the necessary approximations. In many situations involving optimization models, deciding which approximate model to develop is a crucial decision. MODFORM lacks knowledge to support this critical activity. We believe that this will require a clearer understanding of the accuracy/tractability tradeoff that is at the heart of the modeling process.\*

\* Daniel R. Dolk, Associate Editor. This paper was received on February 4, 1992, and has been with the authors 2 months for 1 revision.

## References

Binbasioglu, M. and M. Jarke, “Domain Specific DSS Tools for Knowledge-Based Model Building," Decision Support Systems, 2 (1986), 213–223.

Blanning, R., "Intelligent Model Management," Working Paper, Owen Graduate School of Management, Vanderbilt University, Nashville, TN, 1991.

Bradley, G. H. and R. D. Clemence, "Model Integration with a Typed Executable Modeling Language," Proceedings of HICSS-21, Vol. 3, IEEE Computer Society Press, Los Alamitos, CA, 1988, 403–410.

Chi, M. T. H., P. J. Feltovich, and R. Glaser, “Categorization and Representation of Physics Problems by Experts and Novices," Cognitive Science, 5 (1981), 121–152.

Delco Refinery. Cases in Operations Research, Harvard University Press, Cambridge, MA, 1980.

Ericsson, K. A. and H. A. Simon. Protocol Analysis: Verbal Reports as Data, MIT Press, Cambridge, MA, 1984.

Gass, S., “Managing the Modeling Process: A Personal Reflection," European Journal of Operations Research, 31 (1987).

Geoffrion, A., “Introduction to Structured Modeling," Management Science, 33 (1987), 547–588.

“Computer-based Modeling Environments," European Journal of Operations Research, 41 (1989), 33–43.

Greenberg, H. J., “A Functional Description of ANALYZE: A Computer-Assisted Analysis System for Linear Programming Models," ACM Transactions on Mathematical Software, 9 (1983), 18–56.

, "MODLER: Modeling by Object-Driven Linear Elemental Relations," Annals of Operations Research, (1992).

Johnson, L. A. and D. C. Montgomery, Operations Research in Production Planning, Scheduling and Inventorv Control, Wiley, New York, 1974.

Jones. C. V. “An Introduction to Graph-Based Modeling Systems, Part I: Overview," ORSA Journal on Computing, 2 (1990).

“An Introduction to Graph-Based Modeling Systems, Part II: Graph-Grammars and the Implementation," ORSA Journal on Computing, 3 (1991).

Kendrick D. and A. Meeraus, GAMS: An Introduction. World Bank, The Scientific Press, Palo Alto, CA, 1987.

Kottemann. J. E. and D. R. Dolk, “Modeling Languages and Model Integration: A Process Perspective," Information Systems Research. 3, 1 (1992), 1–16.

Krishnan. R., “Automated Model Construction: A Logic Based Approach," Annals of Operations Research, 21 (1989), 195–226.

, P. Piela, and A. Westerberg, “Reusing Mathematical Models in ASCEND," Working Paper, Heinz School of Public Policy, Carnegie Mellon University, Pittsburgh, PA, 1991.

Liang T P “Graph Based Approach to Model Management." Proceedings of the International Conference on Information Systems, San Diego, CA, 1986.

“Modeling by Analogy: An Approach to Automated Linear Program Formulation,"Working Paper, Krannert Graduate School of Management, Purdue University, West Lafayette, IN, 1990.

Muhanna W., “On the Organization of Large Shared Modelbases,"Annals of Operations Research, 23 (1991), 105–128.

Murphy, F. H. and E. A. Stohr, “An Intelligent System for Formulating Linear Programs," Decision Support Systems, 2 (1986), 39–47.

Newell. A. and H. A. Simon. Human Problem Solving, Prentice-Hall, Englewood Cliffs, NJ, 1977.

Novak, G. S., “Representation of Knowledge in a Program for Solving Physics Problems," Proceedings of the Fifth International Joint Conference on Artificial Intelligence, Pittsburgh, PA, 1972.

Orlikowski W. and V. Dhar, “Imposing Structure on Linear Programming Problems: An Empirical Investigation of Expert and Novice Models," Proceedings of the National Conference on Artificial Intelligence, Philadelphia, PA, 1986.

Raghunathan, S., R. Krishnan, and J. May, "Computer-Assisted Model Development: A Belief Maintenance Approach," Working Paper, AI in Management Laboratory, Joseph M. Katz Graduate School of Business. University of Pittsburgh, Pittsburgh, PA, 1990.

Sklar. V.. R. Pick, and J. Evans, “Eliciting Knowledge Representation Schemes for Linear Programming" in D. F. Brown and C. C. White (Eds.), Operations Research and Artificial Intelligence: The Integration of Problem Solving Strategies. Kluwer, 1990, 279–316.

and “A Knowledge-based Linear Programming Formulation Assistant," Proceedings of HICSS-23, Vol. 3, IEEE Computer Society Press, Los Alamitos, CA, 1990, 269–278.

, and J. Evans, “A Knowledge-based Approach to LP Model Formulation," Proceedings of DSI Meeting, Vol. 1 (1984), 226–228

Weinrab, D. and D. Moon, Lisp Machine Manual, MIT, Cambridge, MA, 1981.

Williams. H. P., “Experiments in the Formulation of Integer Programming Problems,"Mathematical Programming Study, 2 (1974), 180–197.

, Model Building in Mathematical Programming, Cambridge University Press, England, 1984.
