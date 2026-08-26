---
otero_id: 17559
otero_key: "DSJEKAHJ"
title: "Process-based reconstructive approach to model building"
authors: "Meral Binbasioglu"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90010-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Process-based reconstructive approach to model building

Meral Binbasioglu

Hofstra University, Hempstead, NY 11550, USA

The role of derivational analogy approach in the model building domain is investigated. In particular, the paper focuses on enhancing decision support systems with model construction capabilities so that the prior modeling experience can be conveyed into new problem situations. The role of analogy in the model construction process is pointed out. This is followed by a discussion of the different approaches to analogical reasoning and the assessment of their suitability for model building decision support systems. The proposed approach, process analogies, is detailed as to required knowledge sources and representation schemes for problem and model description, and illustrated using examples. The reusable model pieces in the linear programming modeling domain are identified at various levels of abstraction and their impact on model base organization is pointed out. The alternative model base organization strategies are contrasted in terms of storage, search and reasoning tradeoffs.

Keywords: Model management; Analogical reasoning; Case-based reasoning; Transformational analogy; Derivational analogy; Process analogy; Result analogy

![](/api/attachments/DSJEKAHJ/fulltext/images/f13be8cf4c4d20fc7de71489dbac442b771cb3b65053b27ead9c602500d9f67b.jpg)

Meral Binbasioglu is an Assistant Professor of Business Computer Information Systems at Hofstra University. Before joining the faculty at Hofstra, Dr. Binbasioglu taught at Purdue University, Middle East Technical University in Ankara and Syracuse University. She earned her Ph.D. degree in Information Systems from the Stern School of Business, New York University, and her B.S. and MBA in Management from the Middle East Technical University. Her current re-

search interests include decision support systems, group decision/negotiation support systems, integrated office systems, and artificial intelligence applications in business.

## 1. Introduction

One of the major goals of model management systems is to improve productivity by being able to transfer the previous modeling experience to the construction of new models. In other words, the challenge is, how to collect, integrate and preserve expertise in building and using decision models. Previous model management research has focused on technical model representation issues $[8,9]$ and the development of modeling languages. For example, a general purpose model representation language was proposed $[12]$ , and a specialized modeling language, LPFORM, was designed for specifying Linear Programming (LP) models $[15]$ . A knowledge representation scheme which distinguishes among model types, model templates and instances is proposed for large, diverse model libraries $[14]$ . Almost all of these tools focused on offering syntactic modeling support. The semantics of modeling was studied as part of the development of an automatic model construction tool which also assists in problem understanding $[4]$ . Recently, model management researchers have been investigating the possibilities of utilizing previous modeling experience by mapping a new problem to stored model counterparts. For example, a transformational analogy based approach to model reusability matches a given problem to stored models based on a similarity factor metric $[13]$ . The role of structured modeling in model reusability is discussed in $[11]$ .

With the objective of utilizing old solutions, we explore answers to the following questions; what model piece could be reused and how could it be utilized in the modeling of a new problem setting? We propose a process oriented approach to model reusability where the transfer of previous modeling experience is captured by concept formation of the modeling domain as well as the modeling process. Contrary to current approaches to reusability in the model management domain, where the sole focus is on finding a readily-instantiable stored model counterpart, we view matching as a process. The proposed process-based approach to model reusability designs a model from reusable model pieces rather than expecting a readily-instantiable stored model counterpart. We begin by recognizing that the model formulation knowledge cannot be captured alone by representing arbitrary prior model occurrences. Instead it is proposed that model formulation is to be based on a careful selection of reusable model pieces, which when augmented with the modeling process knowledge, will result in the construction of an appropriate model. Our discussion touches upon storage and search requirements of model libraries and the related tradeoffs. For example, storing readily-instantiable model occurrences is a viable option if it is foreseeable to face the same problem setting in the future, in that an old model representation is likely to be an exact match. However, the drawback of this approach is, an increase in search time corresponding to increased model occurrences that can clutter the model base.

In section 2, the possible approaches to model construction are introduced, using examples from the LP modeling domain. Specifically, building models from scratch is compared to the approaches that incorporate model reusability, such as analogical reasoning methods. In section 3, we introduce the process of model building, the objective being to draw attention to the model building process knowledge. Understanding the nature of process knowledge is essential in assessing the suitability of different reasoning strategies. In this respect, this section is essential for following the rest of the paper. In section 4, different approaches to analogy based reasoning are illustrated using examples. Section 5 extends the discussion to the possibility of combining result and process based analogy approaches, so that we can take advantage of each when circumstances warrant. The operational requirements of an implementation environment are also touched upon. Section 6 concludes the paper.

## 2. Possible approaches to modeling

We view model construction as a problem solving task. The term problem solving in artificial intelligence (AI) has been used to denote disparate forms of intelligent actions to achieve well-defined goals [5]. In terms of the way the problem solving task is carried out, expert systems research utilizes two distinct problem solving approaches: classification and constructive methods [7]. The classification problem solving method reaches a solution (result) by systematically relating data to a pre-enumerated set of alternative solutions, by data abstraction, heuristic association and refinement; whereas the constructive problem solving method constructs the solution with the help of structural and behavioral domain knowledge. The rest of the paper explores the suitability of these methods in the model building domain. The discussion is geared towards mathematical models with examples from the LP modeling domain.

Modeling knowledge can be viewed at different levels. One extreme would correspond to applying the basic decision making principles when constructing a decision model. As will be examined in section 3, any equation can be constructed if the semantics of the problem are properly related to the model syntax. The pure constructive method can be applicable when it is desired to formulate the relevant equations from scratch, one at a time. When the constructive method is employed on its own, the problem solver should be knowledgeable in designing the individual equations. Furthermore, the ability to simultaneously consider the consistency of many equations is needed. But, as the number of equations increases, it becomes harder to cope with complexity. Since equations would be added to the formulation one at a time, it is necessary to check the consistency of the formulation continuously, and in the event that an inconsistency is detected, provide mechanisms such as backtracking to revise the formulation. The pure constructive approach does not take advantage of reusability.

To take full advantage of model reusability, one could consider storing model templates built for all likely problem situations. Such a collection of model templates would make it possible to directly instantiate an appropriate pre-stored abstract model representation with parameters unique to a given problem. We call this “result analogy”, since the reuse involves proper instantiation but not design of a unique model structure. The drawback of this approach is that since it requires developing prefabricated models of likely problem settings, it would be impossible to exhaustively cover all the problem situations. Also, the system would then be restricted in capability in a dynamic world since it would have no knowledge of how to model a new problem situation. A more flexible approach is to have the power to configure a model from reusable model pieces. Such a capability requires capturing and formalizing the dynamic model construction process knowledge in addition to the static representation of model pieces. We call this approach “process analogy” because of the emphasis on the process knowledge as part of the reasoning procedure.

The concept of “reusability” in modeling has its parallels in software engineering, namely the “software libraries”. Some of the knowledge gathered from such implementations might be adapted to the modeling domain. As Balzer, et al. [1] note, software libraries – with the exception of mathematical subroutine libraries – have failed because they are filled with implementations, which necessarily contain many arbitrary decisions. Rather, they suggest that model specification and their recorded development should be placed in libraries, and reuse should involve modifying the specifications appropriately and their development accordingly. This view is consistent with the proposed process oriented approach since it advocates the need to capture the reasoning steps needed when modifying and developing specifications in addition to the representation of reusable pieces.

In addition to software engineering, “reusability” in modeling can be viewed from an artificial intelligence perspective. Analogical and case-based reasoning methods, both rely on encapsulating episodic knowledge to guide complex problem solving. The former emphasizes the process of modifying, adapting and verifying past derivations (cases), whereas the latter emphasizes the organization, hierarchy indexing and retrieval of case memory $[5,6]$ . As Carbonell $[5]$ puts it, “the term analogy often conjures up recollections of artificially contrived problems in various psychometric exams, such as, ‘X is to Y, as Z is to?’. This aspect of analogy is far too narrow and independent of context to be useful in general problem-solving domains”. Instead, Carbonell proposes the following operational definition of analogical reasoning:

Definition Analogical problem solving consists of transferring knowledge from past problem solving episodes to new problems that share significant aspects with corresponding past experience and using transferred knowledge to construct solutions to the new problems [5, p.374].

According to Carbonell [5], analogical reasoning can be viewed in two categories: derivational and transformational analogies. The transformational analogy approach is based on an arbitrary context-free similarity metric as a basis for selecting the most suitable past experiences (solutions) which are subsequently transformed to satisfy the requirements of the new problem statement. The derivational analogy approach, on the other hand, is a reconstructive method which walks through the reasoning steps in the construction of the past solutions including the decision sequences and their justification which had proved effective in solving particular problems requiring similar initial analysis. In other words, the derivational analogy approach attempts to solve problems based on the transfer of past experiences to new problem situations by recreating lines of reasoning, referred as the derivational knowledge. It captures the intermediate information (process information) in addition to the resultant plan or specific solution. In contrast, in transformational analogy approach, the knowledge transferred to the new situation is the old solution (which could either be an exact match or a partial match) where the old solution is to be incrementally perturbed according to the primitive transformation steps in a heuristically guided manner until it satisfies the requirements of the new problem.

In the model management domain, “solution” refers to model representation of selected old problems. The transformational analogy approach requires an “exact match” with a solution unless it is equipped with the process knowledge which can provide the reasoning knowledge in utilizing partially matched solutions. In this case, the solution can be a readily-instantiable model representation at any level of model abstraction hierarchy – model instance, specialized model or abstract model representations. Note, in the case of partial matches, the transformational analogy approach also resorts to process knowledge, though to a lesser extent. Therefore, for clarity of the presentation, we differentiate between direct solution instantiation and solution derivations, and refer to them as “result analogy” and “process analogy”, respectively. Accordingly, the process analogy approach subsumes the transformational analogy method with partial matches as well as designing a model in a reconstructive fashion. The process knowledge captures the reasoning needed when choosing the relevant model components as well as their modifications and integration. Another difference is that, in the process-based approach, the matching is not limited to a single model; rather, the approach incorporates the possibility of building a new model out of many reusable model pieces. In other words, focusing on process similarities relaxes the strict matching requirements, because the model is being configured from reusable abstract model pieces, rather than being compared to individual stored model representations. That is, the emphasis is on capturing the experience gathered during the entire model building process rather than being limited to end results. In sections 4 and 5, we elaborate the possible employment of the result and process analogy methods in model building systems and compare them in terms of their capabilities and limitations, and point out the technical implementation requirements. Subsequently, we explore the possibility of combining both of these approaches as part of model building systems. Before proceeding further, we briefly introduce the operational details of employing analogical reasoning to model building systems.

Carbonell [5] suggests the following should be specified when operationalizing the analogical reasoning approach:

\- What it means for problems to “share significant aspects”

\- What kind of knowledge is transferred from past experience to the new situation

\- Precisely how the knowledge transfer process occurs

\- How analogically related experiences are selected from a potentially vast long-term memory of past problem solving episodes.

In the mathematical modeling domain, the above can be specialized as follows:

\- Determining meaningful reusable model pieces

\- Developing a model representation scheme which will explicitly represent the modeling knowledge the model pieces capture as to goal and constraint equation structures

\- Extracting and representing the process knowledge necessary to match a problem to stored model pieces as well as their adaption to unique problem requirements during the configuration of a model, that is, formalizing the knowledge transfer

\- Determining the criteria in expanding the model library.

In the following section we introduce the model building process knowledge. We point out the role of semantics and syntax in model building as well as how they guide the model formulation process using the LP modeling domain as an example. In particular, we discuss how decision variables are chosen, how they are related to each other and the problem constants during the process of equation construction. The reasoning process is based on an action-resource model which is developed to capture the semantics of model formulation $[2,4]$ . We illustrate the topic with example equation formulations. The semantics captured in equation structures is proposed to be the basis of mapping problems to stored models $[3]$ . In section 4, we describe in detail the process of knowledge transfer. We consider the implications of the process and result oriented approaches on the size and organization of model libraries in section 5.

## 3. Modeling process

This section illustrates the model building task as an artificial intelligence problem solving task, and as such provides insight into the derivation of equation instances from their abstract representations, suggesting the first symptoms of model reusability as well as the suitability of derivational reconstructive analogy approach. Also, this section points out the role of semantic and syntactic knowledge in the mathematical modeling domain. The action-resource model which captures the formulation semantics is reviewed and its role in composing models as to the identification and piecing together of the model components (decision variables, coefficients, associated indices and equations) is pointed out. The process of equation construction is illustrated using an example problem adopted from [16, p. 88–89].

## 3.1. Example #1

Consider a firm which manufactures two products, bird food and dog food. The manager is concerned with deciding production levels based on the profitability of each product and the availability of the production capacities. The capacities of the blending and packaging units are both 8 hours per day. A unit of bird food production takes 0.25 hours of blending and 0.10 hours of packaging capacity. A unit of dog food production takes 0.15 hours of blending and 0.30 hours of packaging capacity. The profits of producing bird food and dog food are \$100 and \$80 per unit, respectively. The company wants to produce at least 10 units of bird food to meet the minimum required service level. The demand for dog food is limited to at most 15 units. What levels of bird food and dog food should the company produce per day to maximize its profits?

To model this problem, the following equations are to be constructed:

(1) Availability equation on the utilization of blending unit.

(2) Availability equation on the utilization of packaging unit.

(3) Service level equation to meet the minimum level required of bird food.

(4) Market limitation equation to reflect the demand limitation of dog food.

(5) Objective function expression which relates the production levels of products to their respective profitability contributions.

The next step is to decide on the decision variables. Since the purpose is to decide on the levels of final products to be produced, the decision variables should reflect this relationship. Accordingly, we identify, $DV_{[produce,bird\_food]}$ and $DV_{produce,dog\_food]}$ . In this notation, DV stands for decision variable. The equations can be constructed with the problem specific data as follows:

(1) Availability constraint (blending):

$$
\begin{array}{r l} (1 \mathrm{I}) & 0. 2 5 \mathrm{DV} _ {[ \text { produce,bird\_food } ]} \\ & + 0. 1 5 \mathrm{DV} _ {[ \text { produce,dog\_food } ]} \leq 8 \end{array}
$$

(2) Availability constraint (packaging):

$$
\begin{array}{r l} (2 \mathrm{I}) & 0. 1 0 \mathrm{DV} _ {[ \text {produce,bird\_food} ]} \\ & + 0. 3 0 \mathrm{DV} _ {[ \text {produce,dog\_food} ]} \leq 8 \end{array}
$$

(3) Service level (bird food):

(3 I) $\mathrm{DV}_{[\text {produce, bird\_ food}]} \geq 10$

(4) Market limitation (dog food):

$$
(4 \mathrm{I}) \mathrm{DV} _ {[ \text { produce }, \text { dog\_food } ]} \leq 1 5
$$

(5) Objective Function:

$$
\begin{array}{r l} (5 \mathrm{I}) & \text { Max } 1 0 0 \mathrm{DV} _ {[ \text { produce,bird\_food } ]} \\ & + 8 0 \mathrm{DV} _ {[ \text { produce,dog\_food } ]} \end{array}
$$

The above equations, (1 I)–(5 I), are in fact instantiations of abstract equation patterns. For example, if we further study the first equation, (1 I), availability constraint (blending), we observe that it is the instantiation of the following abstract equation form, (1 A):

$$
(1 \text {   A)   Total   Resource\_Usage } \leq \text { Resource   Level }
$$

which can be specialized with problem specific features. The Resource Level corresponds to the available capacity of the blending unit. Resource\_Usage refers to the impact of decision variables on the resource level. In this case, in order to accurately state the relationship between the final product production levels and the capacity of the blending unit, it is necessary to multiply the decision variables with a suitable coefficient, Usage\_Coef. The specialized form of the equation, (1 S), is as follows:

(1 S)

$$
\begin{array}{l} \times \text {Usage\_Coef} _ {[ \text {bird\_food, blending} ]} \mathrm{DV} _ {[ \text {produce,bird\_food} ]} \\ + \text {Usage\_Coef} _ {[ \text {dog\_food, blending} ]} \mathrm{DV} _ {[ \text {produce,dog\_food} ]} \\ \leq \text {Resource Level} _ {[ \text {blending} ]} \end{array}
$$

Once the specialized form of an equation is obtained as above, it can be instantiated with prob-

Abstract form:

(1 A) Total Resource\_Usage ≤ Resource Level

Specialized form for resource 'blending':

$$
\begin{array}{r l} & \text {(1 S) Usage\_Coef} _ {[ \text {bird\_food, blending} ]} \mathrm{DV} _ {[ \text {produce, bird\_food} ]} \\ & + \text {Usage\_Coef} _ {[ \text {dog\_food, blending} ]} \mathrm{DV} _ {[ \text {produce, dog\_food} ]} \\ & \leq \text {Resource Level} _ {[ \text {blending} ]} \end{array}
$$

Instantiated form:

$$
(1 \mathrm{I}) 0. 2 5 \mathrm{DV} _ {[ \text { produce,   bird\_food } ]} + 0. 1 5 \mathrm{DV} _ {[ \text { produce,   dog\_food } ]} \leq 8
$$

Fig. 1. Specialization and instantiation of “availability equation”.

lem specific coefficient and constant values. Recall that problem specific data relevant for the above equation are as follows:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Usage_coef $_{bird\_food,blending}$ : 0.25
Usage_coef $_{dog\_food,blending}$ : 0.15
Level resource $_{blending}$ : 8
</div>

Thus, equation (1 I) is an instance of specialized equation (1 S) which in turn belongs to an abstract availability equation of the form given in equation (1 A). Figure 1 depicts the specialization and instantiation of the availability equation with the problem specific data. The availability equation for the packaging unit follows through the

Availability Constraint for resource 'blending':

(1 A) Total Resource\_Usage ≤ Resource Level

Availability Constraint for resource 'packaging':

(2 A) Total Resource-Usage ≤ Resource Level

Service Level Constraint:

(3 A) Resource ≥ Required Resource Level

Market Limitation Constraint:

(4 A) Resource ≤ Demand Resource

Objective Function:

(5 A) Maximize / Minimize Resource Level [money]

Fig. 2. Example #1: Abstract model representation.

```txt
(1 S) Usage_Coef[bird_food, blending] DV[produce, bird_food]
+ Usage_Coef[dog_food, blending] DV[produce, dog_food]
≤ Resource Level [blending]

(2 S) Usage-Coef[bird-food, packaging] DV[produce, bird-food]
+ Usage-Coef[dog-food, packaging] DV[produce, dog-food]
≤ Resource Level [packaging]

(3 S) DV[produce, bird_food] ≥ Required Level [bird_food]
(4 S) DV[produce, dog_food] ≤ Demand Level[dog_food]
(5 S) Maximize cont_margin[produce, bird_food] * DV[produce, bird_food] + cont_margin[produce, dog_food] * DV[produce, dog_food]
```

Fig. 3. Example #1: Specialized model representation.

same reasoning steps, the difference being, the resource “blending” is replaced with “packaging”. Similarly, the abstract representation of a “service level equation” is:

(3 A) Resource ≥ Required Level $_{[Resource]}$ and specialized as:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
(3 S) DV $_{[produce,bird\_food]}$ $\geq$  Required Level $_{[bird\_food]}$
</div>

In instantiated form (3 I), the constant “Required Level $_{bird\_food}$ ” is replaced by value 10.

The abstract form of a “market limitation equation” is:

(1 I) $0.25\mathrm{DV}_{[\text {produce, bird\_food}]} + 0.15\mathrm{DV}_{[\text {produce, dog\_food}]} \leq 8$

$$
(2 \mathrm{I}) 0. 1 0 \mathrm{DV} _ {[ \text { produce,   bird\_food } ]} + 0. 3 0 \mathrm{DV} _ {[ \text { produce,   dog\_food } ]} \leq 8
$$

which is specialized as the maximization of the level of resource, “money”. Next, money level is specialized in terms of the problem components. The decision variables are related to money by

(3 I) $\mathrm{DV}_{[\text{produce, bird\_food}]} \geq 10$

(4 I) $\mathrm{DV}_{[\text{produce, dog\_food}]} \leq 15$

## (5 A) Maximize/Minimize Resource Level

(4 A) Resource $\leq$ Demand Level[Resource] and specialized as:

(5 I) Max 100 DV $_{[produce, bird\_food]}$ + 80 DV $_{[produce, dog\_food]}$ (4 S) $DV_{[produce,dog\_food]} \leq Demand Level_{[dog\_food]}$ where Demand Level $_{[dog\_food]}$ being the constant.

The abstract form of an objective function expression is:

Fig. 4. Example #1: Model instance representation.

choosing the proper transformation coefficients. In this case, the coefficients which achieve the expected results are contribution margins.

(5 S) Maximize

$$
\begin{array}{r l} \text {cont\_margin} _ {[ \text {produce, bird\_food} ]} & * \mathrm{DV} _ {[ \text {produce, bird\_food} ]} \\ & + \text {cont\_margin} _ {[ \text {produce, dog - food} ]} \\ & * \mathrm{DV} _ {[ \text {produce, dog - food} ]} \end{array}
$$

Note, the equation instances given in equations (1 I)–(5 I) are not coincidental but are proper instantiations of specialized equation structures, (1 S)–(5 S), which in turn are derived from abstract equation structures (1 A)–(5 A). Figure 2 depicts the abstract representation of Example #1. Figure 3 shows the model when equation structures are specialized. Finally, Figure 4 provides a representation of the problem at the instance level. Once equation construction is viewed in this formalism, it is possible to make use of AI problem solving techniques. The equation construction task is viewed as a hierarchical process: identification of equation types, specialization of the identified equation structures as to decision variables, constants and coefficients, and finally instantiation of the specialized structures with the values provided in the problem description.

Defining equation structures at the abstract level and formalizing the process of specialization and instantiation based on the relationship between resource levels and how they are consumed or generated makes the approach general. The semantics of formulation captured in different equation structures are a first step in visualizing “reusable” model pieces.

## 3.2. Review of action-resource model: Linking semantics to syntax in LP modeling

In this section, we briefly review the action-resource model $[2,4]$ which governs the approach exemplified in the previous subsection. We view linear programming models as describing the effect of purposeful actions on resources. Actions need resources of one type or another to generate other resources. For instance, the action “produce” generates the output “final product” with the help of resources such as machine, rawmaterial or employee. In general, actions and resources are related to each other by input/output relationships. Equations of an LP model represent such relationships. As Example #1 has illustrated, these objects go through a series of semantic processes prior to their syntactic representation. To facilitate the reasoning process, we need to represent the impact of actions on resources, i.e., whether a given action decreases or increases the level of a resource, or whether the resource is an input to, or an output of, the action.

The action-resource model captures the semantics of the LP model formulation, and formalizes the choice of decision variables, coefficients, constants as well as the choice of equation types and model types. The proper employment of the approach requires relating every problem component to abstract object categories. For instance, the formulation in Example #1 is carried out as the relationship between the objects – final-product and machine – because problem elements can be categorized as such at the abstract level.

The action-resource model relates application semantics to model syntax as follows: An activity is composed of an action and the resources that are input to and output of an action. The activity levels in an application domain are interpreted as decision variables in the LP modeling domain. For instance, a simple decision variable, typically represented as X, can be defined as the amount of product to be produced, or, [action = produce, output-resource = product] and, in our notation, represented as $DV_{[produce,product]}$ . If the output resource has different types, then index variables, say i, can be added to the decision variable, $X_{[i]}$ , where i represents the type of output. A moderately complex decision variable can be defined on both inputs and outputs. For instance, the previous example can be modified to reflect the role of input resource “machine” in action “produce”. Then, decision variable, $X_{[i,j]}$ , represents the amount of product i produced using machine j. In general, a decision variable can have indexes for all inputs and/or outputs. In a given problem situation, we rarely need all the possible index variables; rather, we need to choose the ones which are necessary to accurately model the situation under consideration.

The coefficients of a model represent the rate of increase and decrease in resource levels as a result of actions taken. Coefficients make it possible to reduce the equation components which are stated in different units to a common unit so that their relationships can be accurately reflected. Constants reflect desired or available resource levels. Policies are represented as equations and may furnish values for constants along with resources. Figure 5 summarizes the relationship of application domain knowledge to LP equation structures. In terms of their semantics, LP equations can be classified as objective function, availability (e.g. market limitation), balance, requirement (e.g. service level), exchange (e.g. blending), transformation, among others [2,3].

![](/api/attachments/DSJEKAHJ/fulltext/images/e2a3117979e876996194ba254bd627e96ebedc953b0bd9b2a0f86c623183887a.jpg)  
Fig. 5. Representation of LP model components using domain objects.

## 4. Achieving reusability: Result versus process analogies

## 4.1. Result analogies

The result analogy approach is well-suited to problem situations when it is feasible to enumerate all the possible solution states a priori. In the model management domain, the possible solution states are model representations at specialized or instance levels. However, the use of this approach for operations research models is quite limited, since these models are applicable to diverse problem settings where it is usually not possible to conceive all likely model structures a priori. This point is elaborated below using examples.

Consider Example #1, assume we have different plants, and we are interested in deciding on the production levels of final products in each plant. Further, assume the plants do not have similar technologies. The equation design should reflect the technological variations resulting from the differences in machinery in each plant. Thus, structurally, the new version of the problem displays similar model features, that is, the same equation types; the only difference being that the decision variables are to be indexed by both product and plant, the coefficients 'Usage\_Coef' are to be indexed by product, plant and machine, and the availability constraints are to be designed for each machine type in each plant. Further, the linkages between the decision variables need to be reflected using "transformation equations". For example, the total production of each product in all the plants will be aggregated to form the final product levels using a transformation equation. The total final product levels in turn will be used as part of the service level and market limitation equations.

In order to carry out a successful match, the result analogy method checks for a representation which is similar in all aspects. For example, the new version of Example #1 can be matched to a stored model of the type which happens to have the same equation structure as to decision variables, coefficients and constants. That is, the decision variables must be indexed by both product type and plant type. Note that, though the new version of the problem is same as in Example #1 at the abstract level, the result analogy based reasoning system cannot exploit this similarity, since it is looking for a readily-instantiable representation similar to the form shown in Figure 3. In other words, the result oriented reasoning approach does not have any reasoning power beyond simple substitution of coefficient and constant values with problem elements. Consequently, it cannot fully exploit “reusability”, of varying degrees, other than a readily-instantiable form which can be put into use by simple substitution of data sets.

Figures 6 and 7 depict the employment of the result analogy approach and how the mapping is carried out at the model instance and specialized model representation levels, respectively. Note that the result analogy approach is suitable only when the given problem displays a similar structure with the stored model representations. However, the variations in stored model representations as to the structure of decision variables, coefficients or constants constrain the employment of an exact match based approach. Further, the complexity of finding the exact match increases when the problem simultaneously displays the features of more than one model type requiring a different composition of equation types and/or equation structures.

![](/api/attachments/DSJEKAHJ/fulltext/images/be7f554202bd5f6b5bd977fdf7b629008414ae9aec58a416d7b651948f7dff7e.jpg)  
Fig. 6. Result analogy mapping at model instance level.

## 4.2. Process analogies

## 4.2.1. Introduction

Recall that, in section 3, we illustrated the role of structural domain knowledge in equation construction; actions and resources and the relationships between them being the major role players. We can further extend the application semantics and make explicit the structural relationship conveyed by these components by tagging them with meaningful labels, namely constraint types. For example, the model for Example #1 can be represented by semantically labeled equation types, such as availability constraint, service-level constraint, market-limitation constraint, among others, as shown in Figure 2. Such an abstract representation of the model can easily accommodate variations in decision and index variables. For example, the abstract model representation in Figure 2 can be utilized to model the problem discussed in subsections 3.1. and 4.1. This approach represents a reusable model at an abstract level by specifying the types of the constraint equations which comprise the model.

![](/api/attachments/DSJEKAHJ/fulltext/images/183c786639f22d0300f4b413af0b781372eaa7fafb2ca64609a855977f806bc0.jpg)  
Fig. 7. Result analogy mapping at specialized model level.

![](/api/attachments/DSJEKAHJ/fulltext/images/c5cf005cda7c9fb9239bbab70f78e0d4f2860305bcb26b47afb12f0f4ab34a78.jpg)  
Fig. 8. Process analogy mapping at abstract model level.

Figure 8 depicts the processes involved in utilizing an abstract model representation in modeling a new problem setting. Prior to the mapping step, it is necessary to abstract the features of the new problem. Once the abstract problem description matches an abstract model representation, the equation types required to model the new problem setting can be obtained, and subsequently specialized by problem specific components as to decision variables, coefficients, and constants. The specialization process involves designing the required equation structures. Recall that this process is illustrated in section 3 using examples. Since the approach configures (designs) a model from an abstract model representation, it is likely that an equation type might have many instances depending on how the index sets are defined. The approach requires capturing the process knowledge as to problem abstraction, mapping at the abstract level, as well as specialization of abstract equation structures with problem specific components and the subsequent instantiation of data values. However, its major drawback is, for every possible problem, an abstract model representation as to the needed equation types must be known as part of the model base. Nevertheless, representing models in terms of the relevant equation types is a significant improvement over the result analogy approach which requires the model base to store specialized equation structures for all likely problem settings. Once the equation types needed to model a problem are determined, the equation structures can be designed based on known problem parameters (c.f. section 3).

In short, the process based approach to model construction builds models by modifying known structures (equation types) at the abstract level rather than reasoning from scratch or searching for exact matches. This approach requires identification of the basic model categories/reusable model pieces and their equation types. These in turn are sufficient to provide the starting point for the model construction process. It is in direct contrast to the result oriented approach which instantiates a pre-stored model structure. Recall that the underlying assumption of the result oriented approach to model building is that all possible problem situations can be conceived, modeled and stored in advance. On the contrary, the process-based approach first configures an abstract representation of a model from reusable model pieces or model categories, and subsequently specializes it with problem features, followed by an instantiation step. In the following section, we explore the possibility of dynamically configuring an “abstract model representation” by carefully choosing the required set of equation types.

## 4.2.2. Approach in steps

In this subsection, we discuss how the process based analogy approach can capture the dynamic aspects of the model construction task. Consistent with the view that the model building process involves proper modification and integration of reusable model pieces, the given problem is first associated with one or more stored model categories, the aim being to infer clues about the formulation of the new problem from the structures of the stored models. The basis of matching is abstract model categories and their unique features as to typical equation types. That is, the knowledge inferred is limited to the equation types that constitute the abstract model categories.

<table><tr><td>Name :</td><td>Product-mix</td></tr><tr><td>Is-a :</td><td>Model type</td></tr><tr><td>Obj-function :</td><td>Max resource level [money]</td></tr><tr><td>Must-be :</td><td>(availability, raw-material) OR (availability, employee) OR (availability, machine)</td></tr><tr><td>May-be :</td><td>(service-level, product) (market-limitation, product) (proportion, product) (ratio, product)</td></tr></table>

Fig. 9. Frame for product-mix model.

The process-based approach to model building is operationalized by further extending the modeling semantics to capture the unique modeling features each of the well-known LP subproblems such as blending, product-mix, transportation, among others, display. These model types reflect unique equation structures – equation compositions based on the nature of the conceptual domain objects they model. In fact, each model type can be represented as a certain combination of semantically-tagged constraint equation types. For example, Example #1 can be categorized as a product-mix model, since the constraint types needed to model the problem are consistent with the requirements of a product-mix model type as shown in Figure 9. However, in a realistic setting, a given problem might display the features of more than one model type. The process-based approach categorizes a problem into more than one model type and configures an abstract model (solution) from reusable model pieces, the features of each guiding the model construction process. Note that the approach possesses flexibility in responding to diverse problem settings because of the abstract model configuration property. Further, due to this property the approach qualifies as a reconstructive analogy method as opposed to a transform analogy method.

In the following, we detail the steps involved in designing an abstract model. The process-based analogy approach is applied to the model building domain in two phases. In the initial stages, phase 1, model formulation is viewed as a classification problem. In later stages of formulation, phase 2, the problem solver switches to a construction strategy. The solution is an integration of the initially diagnosed subproblems such that a customized model for the specific problem is attained. This two-phased problem solving process is shown in Figure 10.

![](/api/attachments/DSJEKAHJ/fulltext/images/d354459b38b05ee23d37f120b4bbad1ed409a42563622b228ddf8fb7cf5f504a.jpg)  
Fig. 10. Process analogies in model building.

Phase 1, involves three steps. In step 1, abstraction, the objects in the problem description are disambiguated and related to abstract objects in the application domain resulting in an abstract representation of the problem. In step 2, mapping, the abstracted problem is mapped to well-known linear programming model types (e.g., product-mix, blending, transportation, etc.) based on necessary and sufficient conditions associated with each model type. In step 3, specialization, the subproblems are individually constructed to reflect the problem specific issues. Phase 2, construction, involves two steps. First, the specialized subproblems are integrated in such a way that the formulation for the overall problem is consistent.

The last step is to instantiate the symbolic model where coefficients and constants are replaced by appropriate data values. We illustrate the approach in the following section using an example. Note, this example is an extended form of Example #1, but of a type which models a problem by associating it with more than one LP model type, resulting in the construction of an integrated abstract model representation.

## 4.2.3. Example #2

Consider the company in Example #1 (c.f. section 3.1) which also needs assistance in deciding on raw material purchases. Assume the bird food is composed of cereal, seeds and stones; and the dog food is composed of meat, fish meal and cereals. The raw material purchase levels will be so determined that mixture constraints as to protein, carbohydrates, trace minerals and abrasives (for bird food only) percentages should be assured. Dog food should have 11 percent protein, 15 percent carbohydrates, 1 percent trace minerals. Bird food should be composed of 5 percent protein, 18 percent carbohydrates, 1 percent trace minerals, and 1 percent abrasives. The raw materials have the following composition characteristics and cost:

MEAT FISH- CEREAL SEEDS STONES MEAL

<table><tr><td>Protein</td><td>12</td><td>20</td><td>3</td><td>10</td><td>0</td></tr><tr><td>Carbo-hydrates</td><td>10</td><td>8</td><td>30</td><td>10</td><td>0</td></tr><tr><td>Trace minerals</td><td>1</td><td>2</td><td>0</td><td>2</td><td>3</td></tr><tr><td>Abras-sives</td><td>0</td><td>2</td><td>0</td><td>1</td><td>100</td></tr><tr><td>Cost/ton</td><td>$600</td><td>$900</td><td>$200</td><td>$700</td><td>$100</td></tr></table>

In order to match a problem description to stored model types, it is necessary to delineate the properties of a given problem so that a match can be performed with stored model counterparts. This is accomplished by disambiguating the problem elements – actions and resources – and relating them to abstract resource categories. Details of this process are discussed in [4]. Once the properties of the new problem are identified (that is, the resource categories such as raw material, employee, money, machine), the needed equation types can be inferred, which in turn become the basis of matching the given problem to stored model types. The problem, other than the “purchase” component, is the same as Example #1 and thus can be mapped to a product-mix model type (c.f. Figure 9). However, the way the “purchase” component relates to the product-mix subproblem requires further reasoning.

We need to resolve how raw materials are to be related to final products. One must determine whether the raw materials are ordinarily consumed as an input resource in producing the final products. Or, whether the final products have certain composition requirements of the ingredients possessed by the raw materials. The former is similar to an availability or requirement (internal demand) constraint, whereas the latter is a proportion constraint as in the case of blending problems. The properties of the final product definitions and raw material definitions confirm the latter case, justifying the requirements of a blending problem. The new version of the problem requires not only deciding on the production levels of final products but also determining the level of raw material purchases consistent with blending requirements. Thus, the problem is classified as both a product-mix and a blending problem.

The next step is to identify the decision variables prior to specializing the constraint equations in each model type. The first set of decision variables refer to determining the final product levels, $DV_{[produce,dog\_food]}$ , $DV_{[produce,bird\_food]}$ . Next, the levels of raw materials to be purchased should be represented as decision variables, $DV_{[purchase,meat,dog\_food]}$ , $DV_{[purchase,fish\_meal,dog\_food]}$ , $DV_{[purchase,cereal,dog\_food]}$ , $DV_{[purchase,cereal,bird\_food]}$ , $DV_{[purchase,seeds,bird\_food]}$ , $DV_{[purchase,stones,bird\_food]}$ . Relating the raw material purchases to bird\_food and dog\_food separately helps in the construction of the blending constraints. Since the level of raw materials to be produced depends on the levels of the raw materials that they are composed of (assuming no loss in the production process), the relation between these are as follows:

$$
\begin{array}{r l} \mathrm{DV} _ {[ \text { produce }, \text { dog\_food } ]} & = \mathrm{DV} _ {[ \text { purchase }, \text { meat }, \text { dog\_food } ]} \\ & + \mathrm{DV} _ {[ \text { purchase }, \text { fish\_meal }, \text { dog\_food } ]} \\ & + \mathrm{DV} _ {[ \text { purchase }, \text { cereal }, \text { dog\_food } ]} \end{array}
$$

$$
\begin{array}{r l} \mathrm{Dv} _ {[ \text { produce,bird\_food } ]} & = \mathrm{DV} _ {[ \text { purchase,cereal,bird\_food } ]} \\ & + \mathrm{DV} _ {[ \text { purchase,seeds,bird\_food } ]} \\ & + \mathrm{DV} _ {[ \text { purchase,stones,bird\_food } ]} \end{array}
$$

In order to fulfill the blending requirements, blending constraints (6)-(12) are needed, which relate the raw material purchase levels to product production levels such that the nutritional ingredient composition requirements are to be satisfied. The instantiated forms of the blending constraints are as follows:

(6) Blending constraint (Dog\_food, Protein composition):

$$
\begin{array}{r l} (6 \mathrm{I}) & 1 2 \mathrm{DV} _ {[ \text {purchase,meat,dog\_food} ]} \\ & + 2 0 \mathrm{DV} _ {[ \text {purchase,fish\_meal,dog\_food} ]} \\ & + 3 \mathrm{DV} _ {[ \text {purchasc,cereal,dog\_food} ]} \\ & \geq 1 1 \mathrm{DV} _ {[ \text {produce,dog\_food} ]} \end{array}
$$

(7) Blending constraint (Bird\_food, Protein composition):

$$
\begin{array}{r l} (7 \mathrm{I}) 3 \mathrm{DV} _ {[ \text {purchase,cereal,bird\_food} ]} & + 1 0 \mathrm{DV} _ {[ \text {purchase,seeds,bird\_food} ]} \\ & \geq 5 \mathrm{DV} _ {[ \text {produce,bird\_food} ]} \end{array}
$$

(8) Blending constraint (Dog\_food, Carbohydrates composition):

$$
\begin{array}{r l} (8 \mathrm{I}) & 1 0 \mathrm{DV} _ {[ \text {purchase,meat,dog\_food} ]} \\ & + 8 \mathrm{DV} _ {[ \text {purchase,fish\_meal,dog\_food} ]} \\ & + 3 0 \mathrm{DV} _ {[ \text {purchase,cereal,dog\_food} ]} \\ & \geq 1 5 \mathrm{DV} _ {[ \text {produce,dog\_food} ]} \end{array}
$$

(9) Blending constraint (Bird\_food, Carbohydrates composition):

$$
\begin{array}{r l} (9 \mathrm{I}) 3 0 \mathrm{DV} _ {[ \text {purchase,cereal,bird\_food} ]} & + 1 0 \mathrm{DV} _ {[ \text {purchase,seeds,bird\_food} ]} \\ & \geq 1 8 \mathrm{DV} _ {[ \text {produce,bird\_food} ]} \end{array}
$$

(10) Blending constraint (Dog\_food, Trace minerals composition):

$$
\begin{array}{r l} (1 0 \mathrm{I}) & \mathrm{DV} _ {[ \text {purchase,meat,dog\_food} ]} \\ & + 2 \mathrm{DV} _ {[ \text {purchase,fish\_meal,dog\_food} ]} \\ & \geq \mathrm{DV} _ {[ \text {produce,dog\_food} ]} \end{array}
$$

(11) Blending constraint (Bird\_food, Trace minerals composition):

$$
\begin{array}{r l} (1 1 \mathrm{I}) & 2 \mathrm{DV} _ {[ \text {purchase,seeds,bird\_food} ]} \\ & + 3 \mathrm{DV} _ {[ \text {purchase,stones,bird\_food} ]} \\ & \geq \mathrm{DV} _ {[ \text {produce,bird\_food} ]} \end{array}
$$

(12) Blending constraint (Bird\_food, Abrasives composition):

$$
\begin{array}{r l} (1 2 \mathrm{I}) & \mathrm{DV} _ {[ \text {purchase,seeds,bird\_food} ]} \\ & + 1 0 0 \mathrm{DV} _ {[ \text {purchase,stones,bird\_food} ]} \\ & \geq \mathrm{DV} _ {[ \text {produce,bird\_food} ]} \end{array}
$$

In general, objective function equations maximize the level of resource “money”. In the following formulation, the activities associated with the sales of final products increase whereas the purchase of raw materials decreases the level of money.

Objective Function Equation:

$$
\begin{array}{r l} (5 \mathrm{I} ^ {\prime}) & \text { Max } \left(\text { sales\_price } _ {[ \text { bird\_food } ]} \right. \\ & \times \mathrm{DV} _ {[ \text { produce,bird\_food } ]} \\ & + \text { sales\_price } _ {[ \text { dog\_food } ]} \left. \mathrm{DV} _ {[ \text { produce,dog\_food } ]}\right) \\ & - (6 0 0 \mathrm{DV} _ {[ \text { purchase,meat,dog\_food } ]} \\ & + 9 0 0 \mathrm{DV} _ {[ \text { purchase,fishmeal,dog\_food } ]} \\ & + 2 0 0 \mathrm{DV} _ {[ \text { purchase,cereal,dog\_food } ]} \\ & + 2 0 0 \mathrm{DV} _ {[ \text { purchase,cereal,bird\_food } ]} \\ & + 7 0 0 \mathrm{DV} _ {[ \text { purchase,seeds,bird\_food } ]} \\ & + 1 0 0 \mathrm{DV} _ {[ \text { purchase,stones,bird\_food } ]}) \end{array}
$$

In this section, we have shown how process-based approach to model building designs an abstract model by first classifying the problem to one or more known model categories and subsequently specializing them with problem-specific features, and integrating them so as to design a customized specialized model representation. The last step involves instantiating the specialized equations with problem specific data.

As illustrated using examples, the pure result oriented approach expects a direct mapping of a given problem to a readily-instantiable stored model counterpart (c.f. Figures 6 and 7), whereas the pure process oriented approach constructs a tailored-model (c.f. Figure 10) and, thus, does not require an exact match with a stored model structure at any representation level including the abstract level This flexibility is achieved by separating the process knowledge of modeling from model representation. In other words, rather than attempting to capture all possible modeling knowledge in model representation, the approach favors a simple, abstract model representation along with a separate reasoning component. The reasoning component captures and formalizes the model building process knowledge as to the likely configuration of stored model pieces as well as their specialization with problem specific data. To recapitulate, our view of model base organization problem involves two interrelated decisions: what to store and how to utilize the stored pieces during the model building process.

## 5. Combining result and process analogies

The problem solving approaches discussed in section 4 are not mutually exclusive and a combination of these can be utilized during the course of model building process. Figure 11 summarizes the discussion on reusability in problem solving process by providing a synthesis of the information depicted in Figures 6, 7, 8, 9 and 10. Figure 12 shows the possible approaches to model base organization, and, hence summarizes model representation possibilities. Figure 13 augments Figure 12 by illustrating the required process knowledge when utilizing stored model pieces, and hence, depicts the impact of the model base organization strategies on storage, search and reasoning requirements. In the following, we go over Figures 11, 12 and 13 which aim to conclude the discussion on possible model base organization strategies and their implications.

Throughout the paper we viewed knowledge acquisition as a continuous process requiring the constant integration of new findings into the current knowledge base. For example, as more modeling knowledge is acquired, the existing reusable pieces can be redefined or the library might be augmented with new structures. This brings up again the issue of how to decide on what to store. That is, if a certain model structure is observed to be of recurring type, are we better off reconfiguring it each time or is it cost-effective to store a readily-instantiable representation? For example, the model structure developed in Example #2, the combination of the product-mix model type together with the blending model type, under this extended view, can be stored as a model piece. The abstract level representation of this problem, naturally, is composed of the semantic equation types modeling both the product-mix and the blending problem, and named as abstract hybrid model (AHM). However, it can also be represented as a specialized model (SM) consisting of specialized equation structures as to decision variables, coefficients, etc. or even as a model instance (MI) when it is highly likely that the same problem can recur with the same data set. Figures 12 and 13 incorporate all such representations of this problem as AHM $_{i}$ or SM $_{i}$ or MI $_{i}$ .

![](/api/attachments/DSJEKAHJ/fulltext/images/15f23491d224ca517a75f9e7a0226048901e240905b1a120e937a71a1c91d407.jpg)  
Fig. 11. Reusability in problem solving process.

![](/api/attachments/DSJEKAHJ/fulltext/images/ef63895bce80e242bbdd4bc64503a34a1ac7d261119825f06d290919b08ac288.jpg)  
Fig. 12. Possible approaches to model base organization.

![](/api/attachments/DSJEKAHJ/fulltext/images/4e9c9ecc9da19bb59644f0aa2fc9a7dad0ab8bc239ef418f5b991d18d04b904e.jpg)  
Fig. 13. Model base organization: storage, search, and reasoning tradeoffs.

As the lower portion of Figure 11 depicts, representing every model instance (MI) (c.f. Figure 4) or readily-instantiable specialized model (SM) (c.f. Figure 3) lacks organization, reflecting only “pure” experiences. Even mapping a new problem to SMs, which are directly instantiable abstract model representations, requires a thorough search in the model base, since no concept is available to guide the search process. In this case, the mapping to stored model representations can be carried out based on a computation of arbitrary context-free similarity metric as in the case of a transformational analogy approach $[13]$ . Further, there is a danger of cluttering the model base, which in turn makes it very difficult to find a reasonable match in a reasonable time span.

As shown in the middle of Figure 11, reuse of abstract hybrid-models (AHM) also requires an exact match between the problem and the model structure, and subsequent specialization of the abstract model. The use of abstraction alleviates some of the search difficulties. Since it is possible to configure abstract hybrid-model representations from basic models, the storage of the abstract hybrid-model representations is not absolutely essential, and cannot justify the debate on reusability. Close scrutiny of the utilization of hybrid-models is necessary in order to keep the library free from likely congestion, because though hybrid-models are represented in abstract form, they are also reconstructible model pieces. Further, during model configuration, they cannot be utilized as reusable model pieces since the reasoning system does not have any knowledge about them unless the reasoning component is extended simultaneously. However, this would have an adverse effect on the complexity of the reasoning process. Therefore, it is necessary to establish mechanisms to constantly observe the structures of the recently formulated models and assess the likelihood of coming across the same structures in the future before adding them to the model library.

As the top portion of Figure 11 reflects, configuring a model instance from the basic model types cuts the search process significantly, since mapping is achieved among a limited number of basic model types at the abstract level. The model is configured by mapping the problem to the basic model types, followed by a proper specialization and integration process. The basic model types are represented and stored similar to a form shown in Figure 9. Recall that, using Example #2, we have illustrated the process of configuring models from basic models and the reasoning requirements.

## 6. Concluding remarks

The paper investigated the role of analogies in transferring previous modeling experience to the construction of new models. The reasoning process in modeling is introduced based on the action-resource model which guides the equation construction process. This is followed by a discussion on the semantics captured in equation types. The two major analogical approaches to model construction are illustrated and contrasted, and the extent to which they can make use of reusability are discussed.

The process analogy approach configures a model for a given problem by proper modification and integration of abstract pieces, namely the basic model categories and the associated equation types. We pointed out that this approach has flexibility in accommodating diverse problem settings as long as the corresponding models are configurable from the basic abstract model representations, and the reasoning process knowledge is acquired and represented. The result analogy approach, on the other hand, requires the availability of an exact match (a readily-instantiable specialized model representation) which can be instantiated with problem parameters without resorting to any reasoning. From a knowledge acquisition point of view, the reconstructive process-based approach aims to understand the objects and the relationships and hence is a gradual, incremental process, whereas, the result analogy approach lacks the structural knowledge and can result in arbitrary performance.

The possible application of the process analogy approach to other domains requires studying the application domain as for the possibility of encountering basic model categories or building blocks. As Jarke [10] points out, when there exists a fully developed theory of the application domain, such as actuarial science, it is possible to determine the well-defined set of basic concepts or reusable model pieces. However, where such a closed theory does not exist, one cannot assume a system of basic model building blocks. In such applications, reusable building blocks can be at widely differing levels of quality and abstraction and the conceptual model (system of terms) must be built by DSS configurers or even end-users, typically in an evolutionary process. For example, linear programming modeling is such a domain.

The operationalization of the analogy based approaches is also touched upon as to the need for an object oriented architecture and the knowledge sources. In the prototype implementation of the process based approach $[2]$ , the reasoning steps are captured as rules. Rules operate on the objects, objects being model types as well as resources, actions, and abstract equation representations. All the objects are represented as frames and linked to each other using semantic nets.

The proposed process-based reconstructive approach can be used as a self-teaching tool as well as a knowledge acquisition tool, since it systematizes the modeling process. Once sufficient knowledge is gathered in terms of what should be reusable model pieces, together with their relationships to other objects, programming can start to further the knowledge acquisition process.

## Acknowledgments

I would like to thank the editor and the anonymous reviewers for feedback that helped improve the quality of the paper. Also, I would like to thank Matthias Jarke for his helpful comments on the paper.

## References

[1] Balzer, R., T.E. Cheatham, Jr., and C. Green, Software Technology in the 1990's: Using a New Paradigm, Computer, Vol. 16, No. 11, pp. 29–45, 1983.

[2] Binbasioglu, M., Knowledge Based Modelling Support

for Linear Programming, Ph. D. Thesis, Graduate School of Business Administration, New York University, 1986.

[3] Binbasioglu, M. and M. Jarke, Knowledge-Based Formulation of Linear Planning Models, Expert Systems and Artificial Intelligence in Decision Support Systems, H.G. Sol et al. (eds.), D. Reidel, 1987, pp. 113–136.

[4] Binbasioglu, M. and M. Jarke, Domain Specific DSS Tools for Knowledge-Based Model Building, Decision Support Systems, Vol. 2, 1986, pp. 213–223.

[5] Carbonell, J., Derivational Analogy: A Theory of Reconstructive Problem Solving and Expertise Acquisition, in Machine Learning, edited by Michalski, R. et al., Volume 2, Morgan Kaufmann, 1986, pp. 371–392.

[6] Carbonell, J. and M. Veloso, Integrating Derivational Analogy into a General Problem Solving Architecture, Proceedings Case-Based Reasoning Workshop, 1988, pp. 104–124.

[7] Clancey, W.J., Classification Problem Solving, Proceedings National Conference on Artificial Intelligence, Austin, Tx, 1984, pp.49–55.

[8] Dolk, D. and Konsynski, B.R., Knowledge Representation for Model Management, IEEE Transactions on Software Engineering, 10, 1984.

[9] Elam, J.J., J.C. Henderson, L.W. Miller, Model Management Systems: An Approach to Decision Support in Complex Organizations, Proceedings of the First International Joint Conference on Information Systems, December 8–10, Philadelphia, 1980.

[10] Jarke, M., Coupling Conceptual and Numerical Models in Decision Support, Proceedings IEEE CompEuro Conference, Brussels/Belgium, 1988.

[11] Geoffrion, A.M., Reusing Structured Models via Model Integration, Twentysecond Annual Hawaii International Conference on System Sciences, IEEE Computer Society, Vol. 3, 1989, pp. 601–611.

[12] Geoffrion, A.M., An Introduction to Structured Modelling, Management Science, Vol. 33, No. 5, May 1987, pp. 547–588.

[13] Liang, T.P., Modeling by Analogy: A Case-Based Approach to Model Construction, Working Paper No. 89-1524, University of Illinois at Urbana-Champaign, 1989.

[14] Mannino, V.M., B.S. Greenberg and S.N. Hong, Model Libraries: Knowledge Representation and Reasoning, ORSA Journal on Computing, Vol. 2, No. 3, Summer 1990, pp. 287–301.

[15] Murphy, F.H. and E.A. Stohr, An Intelligent System for Formulating Linear Programs, Decision Support Systems, Vol. 2, No. 1, pp. 39–47, 1986.

[16] Schrage, L. LINDO, Third edition, The Scientific Press.
