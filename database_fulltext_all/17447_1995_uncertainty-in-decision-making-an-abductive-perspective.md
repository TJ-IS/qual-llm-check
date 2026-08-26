---
otero_id: 17447
otero_key: "CP4HTT2H"
title: "Uncertainty in decision-making: An abductive perspective"
authors: "Rita A. Ribeiro; Philip L. Powell; James F. Baldwin"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00011-g"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Uncertainty in decision-making: An abductive perspective

Rita A. Ribeiro $^{a}$ , Philip L. Powell $^{b,*}$ , James F. Baldwin $^{c}$

$^{a}$ University of Bristol, Dept. Eng. Math., Bristol BS8 1TR, UK $^{b}$ University of Warwick, Warwick Business School, Coventry CV4 7AL, UK $^{c}$ University of Bristol, Dept. Eng. Math., Bristol BS8 1TR, UK

## Abstract

Many decisions involve uncertainty, yet most decision support systems (DSSs) and expert systems (ESs) are poorly equipped to deal with such problems. This paper employs an abductive perspective to propose a prototype framework for tackling uncertainty handling in DSS and ES. Five major features of such a framework, a user-friendly dialogue, a case-base, a knowledge-base, approximate reasoning and a fuzzification/defuzzification mechanism are presented and developed. These are supported by an extended example.

Keywords: Fuzziness; Approximate reasoning; Abduction; Multiple-attribute decisions.

## 1. Introduction

This paper uses abduction to attempt to provide a prototype framework for decision support systems (DSSs) and expert systems (ESs) development to handle uncertainty.

The ability to improve the efficiency and effectiveness of the decision-making process is crucial for decision support systems and expert systems. Much decision-taking involves uncertainty, hence one of the most important features for a useful DSS is to provide the ability to handle imprecise and vague qualifiers, such as 'large' profits, 'low' stocks and 'good' employee profile. In general, decision-making may be characterised as a process of selecting ‘sufficiently good’ alternative(s) or course(s) of action, among a set of alternatives, to attain a goal or goals. According to Bellman and Zadeh [6] “much of the decision-making in the real world takes place in an environment in which the goals, the constraints and the consequences of possible actions are not known precisely”.

A vast literature on conceptual models, features and capabilities of DSS/ES already exists (e.g. [7,18]). Drawing on this and acknowledging the characteristics a DSS/ES needs to exhibit, unveils clues as to how and to which methods should be used to achieve the desired attributes; thus enabling the adoption of possible hypotheses. Furthermore, knowing sets of decisions taken in an uncertain specific context-domain may permit explanation and interpretation, enabling generalised models to be developed. This may be termed an abductive process and should constitute one of the tasks of the knowledge engineer.

## 2. Abduction

Abduction is the probational adoption of a hypothesis and can be thought of as a special case of modus tollens [13]. Therefore it can be used as an inference process to explain certain results or evidences. Abduction, or presumption “furnishes the reasoner with the problematic theory which induction verifies” [14]. Its usefulness is, as Peirce [14] points out, that it is the only kind of reasoning which supplies new ideas. Peirce uses the following, slightly anachronistic, example to demonstrate abduction: “I once landed at the seaport in Turkish province; and, as I was walking up the house I wish to visit, I met a man on horseback, surrounded by four horsemen holding a canopy over his head. As the governor of the province was the only personage I could think of who would be so greatly honoured, I inferred that this was he. This was an hypothesis”. A more up-to-date example might be the discovery of a large adverse-variance in a department’s budget. This may be explained in a variety of ways (tentative hypotheses) including sales below expectation, cost increases, environmental shift and fraud. An abductive perspective uses exemplars/cases to infer general models. Using abductive inference might constitute a source of uncertainty in terms of having various plausible possibilities, but this is also one of its chief attributes.

## 3. Multiple attribute decision processes

Decision situations in complex environments are often described by terms such as multiple objective, multiple attribute, multiple criteria and multiple dimensional [12], however, many times these terms are used interchangeably. Typically, the two most common approaches for categorising decision-making are:

Multiple attribute (sometimes called multiple criteria). Multiple attribute decision problems usually refer to a process of choosing from among a set of alternatives which are described in terms of attributes [12]. The main emphasis is on satisfying criteria which are defined by the decision-maker in order to evaluate the set of possible alternatives. An example could be the consideration of speed and price as the attributes to evaluate which car to buy and the criteria could be that only cheap cars would be acceptable from the set of existing cars (alternatives). The goal in multiple attribute decision problems is to classify the alternatives so that the decision-maker can select the one that 'best' satisfies all criteria. However, two types of goals can be distinguished. In the first case the goal is dependent on the subjective criteria and preferences about the attributes, interactively defined by the decision-maker. This is a qualitative approach due to the existence of criteria subjectivity. In the second case the goal is to rate the alternatives using a kind of role model or similar cases. The idea is to classify the alternatives by a partial or total match with the 'role-model' criteria, where the 'role-model' is based on past known cases. The use of past cases to deduce answers or explanations is a recent field of research termed case-based reasoning (e.g. [10]). Baldwin and Ribeiro [4,5] extend this last method to accept fuzzy concepts and, therefore, allow partial matching of attributes. Zimmermann [25] suggests that multiple criteria (another term for multiple attribute) problems have discrete decision spaces.

Multiple objective. Multiple objective decision problems usually consist of optimising a set of goals subject to a set of constraints. The solution is highly dependent on the constraints, and on satisfying possibly conflicting goals. In this type of decision problems the alternatives can be described both in terms of their attributes (restrictions) and in terms of the extent to which they satisfy the objectives [12]. This may be described as a quantitative approach because, usually, the resolution involves operational research methods. An example of this type of problem is to combine the objectives of minimising the cost and maximise the efficiency of manufacturing cars, considering a set of potential manufacturing processes (alternatives). Bellman and Zadeh [6] extended this type of decision-making to accept fuzzy concepts. Further, they considered that both goals and constraints are restrictions in a decision problem and, therefore, their intersection provides the overall evaluation for each alternative. Zimmermann [25] posits that multiple objective problems have continuous decision spaces.

Frequently, one does not initially possess a rich understanding of the context-domain and respective attributes of a given problem. Modelling real-life situations often requires conceptualising incomplete or vague terms or concepts. Moreover, the set of alternatives, criteria or constraints and goals do not, necessarily, have a clear-cut nature and sometimes even present some similar or over-lapping characteristics. Therefore, both approaches face the major problem of how to handle fuzzy and/or incomplete information. However, since multiple objective problems are reasonably quantifiable and their assessment is more straightforward, this paper will concentrate on methods for solving the more subjective, multiple attribute decision problems in uncertain environments.

## 4. Underlying concepts

Three main forms of imprecision may be identified, these are: (1) incompleteness, which can arise in situations lacking some alternatives, attributes or having insufficient data to stipulate a constraint limit for example; (2) fuzziness, a type of imprecision where the classes (sets) have no sharp transition from membership to non-membership [21]. This may arise from difficulties such as obtaining precise concepts for attributes, criteria and constraints. According to Bellman and Zadeh [6], “decision-making in a fuzzy environment meant a decision process in which the goals and/or the constraints, but not necessarily the system under control, are fuzzy in nature”, “a fuzzy decision may be viewed as the intersection of the given goals and constraints”; (3) illusion of validity, which arises from detecting erroneous outputs such as large deviations from ‘expected’ solutions or selecting non-relevant alternatives perhaps because the match was performed by using stereotypes that were incorrect. The term illusion of validity is borrowed from Tversky and Kahneman [19], though the original sense only considered judgement and selection of outcomes under uncertainty, yet in abstract this and the concept employed here are similar. Some examples that clarify the above concepts are:

Type (1) – the expected revenue for 1993 will be \$10 million. This is an uncertain concept, but not fuzzy. The incompleteness is shown by the uncontrollable variables that affect revenue.

Type (2) – in 1992 sales were high. This uses a fuzzy descriptor (high) to ‘classify’ an attribute. It is not incomplete, it is only a vague proposition. Other typical examples are the lack of precise definition for the attribute ‘comfort’ when deciding which car to buy, or what an acceptable level of a company risk is. Type (3) – revenue is \$5 million when the expected value is \$10 million. The illusion of validity could have derived from using only a reduced series (e.g. prior year, 6 month sales) to produce the forecast or by not using the appropriate technique to derive it. The idea is that to the best of current knowledge everything was done correctly but nevertheless the result proved to be incorrect. In this case imprecision is in terms of insufficient input resulting in incorrect output.

The decision-making process for multiple attribute problems might be said to involve three main steps; (a) selection of certain attributes, which are important enough to serve as criteria for selection; (b) grouping of the attributes to form the overall objective; and (c) weighting of the attributes for ranking purposes according to importance or preference for the final objective.

Summarising, a useful DSS/ES must handle incomplete, inconsistent and uncertain knowledge and information. Different views, attitudes and beliefs must also be acknowledged. Moreover, DSS/ES should include the process of identifying, measuring and combining criteria, alternatives and attributes to create a conceptual model for decisions and evaluations under fuzzy environments. As Tversky and Kahneman [20] put it, “The presence of uncertainty regarding the accuracy of a model has implications for the proper conduct of prediction, explanation and revision". With regard to accuracy this may be considered as knowledge that the model is subject to uncertainty and therefore is passible to error.

## 5. The development of a high-level DSS/ES framework able to handle uncertainty

The following outlines the set of inter-related modules necessary to improve DSS/ES effectiveness by enhancing the capacity to deal with uncertainty. The aim is to provide an hypothesis for a general flexible symbolic processing framework (each aspect is considered in more detail in the later sections):

1. User-friendly dialogue. There are two main aims for this capability. First, to help and guide the decision-maker (DM) to partially design/model the system, and second, to provide 'what-if' capabilities (with a graphical simulation if possible) to allow the DM to grasp the consequences of changes in parameters.

2. Case-base. This is a set of cases and/or a generalised role-model to be used in the comparison with new cases to be classified or selected. This will provide the hypothesis for inferencing. There can be various case-bases depending on the fuzzy context-domain, its structure and scope definitions.

3. Knowledge-base. This is a set of facts, concept structures and their instantiations as well as the fuzzy objects definitions that will be used for the matching process. This can be described as the storage of the concepts knowledge representation scheme.

4. Approximate reasoning. This module must involve the capability of inferencing with incomplete and/or fuzzy knowledge to perform the ratings and rankings of alternatives, as well as answering queries. This is the inference engine of the system. There is a shortage of methods and techniques that allow one to deal with uncertain propositions such as: what is the most probable cause of a certain event? What is the diagnosis given certain evidences? Or what are the possible explanations for some results obtained? Quoting

![](/api/attachments/CP4HTT2H/fulltext/images/0a2a7f50c1351f9a4789c7df2ac974ccc3e75dc9664baf26fff83bdb63d348c6.jpg)  
Fig. 1. Basic framework configuraiton.

Tversky and Kahneman [20], “Most inferences in everyday life rely on models or schemas which are imprecise, incomplete and occasionally incorrect”.

5. Fuzzification / defuzzification. This involves a mechanism responsible for the translation of concepts, such as for example ‘cheap’, into an appropriate fuzzy representation to be handled by the approximate reasoning module and then re-translation of the results into a decision-maker understandable form. The mechanism should include the ability to represent the alternatives, attributes, objects and criteria/constraints. A general scheme that can handle fuzzy object-types (e.g. price) and sub-types (e.g. cheap) is essential.

Besides the above modules the system must have a learning ability; that is the possibility of adding new cases and/or updating facts, weights and criteria. Further, it should be extendible to improve or augment the accuracy of the answers by using a more compact cluster of cases to perform the inference.

Fig. 1 depicts, schematically, the framework that is proposed here.

In order to develop such a general framework, appropriate tools and methods are needed. These tools and methods must help to design the conceptual model structure, ensure intelligent storage of knowledge and information (case-base and knowledge-base) and contain facilities for manipulating the input and output (fuzzification/defuzzification plus knowledge representation).

Further, it must provide a flexible reasoning system using past cases and/or a general role-model (reasoning inference mechanism).

All the modules of Fig. 1 involve many issues and paths to explore and study. The major issues of research towards obtaining the required framework features will now be considered. Methods and tools are suggested, as possible candidates for the modules development. After, a small example of a multiple attribute problem, within the framework is presented. The aim of the example is to illustrate how abduction can be used to generalise a model that will allow the classification/selection of similar cases.

## 6. Dialogue interface

The concept, considering the increasing improvements of computer interface theories and methods, is that a framework for DSS/ES should benefit from graphical capabilities. Especially, since the greater part of human reasoning is approximate rather than exact, using images to express knowledge and information is appropriate and desirable (a picture is worth a thousand words!). Of course, though a graphical approach is desirable, this does not mean that all the interface should be graphical. Certainly, the dialogue could also contemplate pop-up menus, dialogue boxes and other types of existing interfaces. The important issue is to bear in mind ergonomic and user-friendly considerations.

A graphical approach must address two different aspects. One is the modelling of the problem. The decision-maker should be able to get an 'idea' of the problem just by looking at a graph or presentation. For example, if one looks at a bar graph of the GNP of Western European countries, one can immediately say which countries are wealthier than others, even without looking at the numbers. The second aspect of this graphical feature should be the development of a 'what-if' capability (simulation). The decision-maker should be able to add or delete criteria, values and so on to verify and understand how possible changes will affect the figure's shape. Furthermore, since the support for decision-making must be capable of handling uncertainty, it is possible to view the decisions as clusters that represent the intersection of fuzzy goals and constraints which are defined in the space of alternatives [6].

![](/api/attachments/CP4HTT2H/fulltext/images/296309b2bf5c19db29659a13c77aeafb9aecbbf1a5ef0c310eb47107fa19b6ca.jpg)  
Fig. 2. Example of fuzzy linguistic variable age.

For example, a “suggestive” idea for a graphic representation of a fuzzy multiple attribute problem, might be to have a ‘polyhedron’ formed by tens (or even hundreds) of faces, each representing fuzzy variables (criteria) [16]. The fuzzy variables (criteria) are possibilistic distributions [23] representing, for instance the triangular distributions shown in Fig. 2. When the system is stable the whole figure is ‘balanced’, otherwise it could be immediately observed as a non-regular shape. ‘Balancing’ might be done with respect to a norm. For instance, score profiles of failing and non-failing companies might be used as a reference point in a DSS for assessing corporate health. Whenever a simulation is performed, how the fuzzy variables behave and are affected could be observed and perceived easily by the different shapes (distortions) the figure takes. Simulation resulting images can then be visually compared with each other and the ‘most’ regular shape chosen as the score for the alternative. The ‘best’ alternative to be selected might be the ‘most’ regular shape of all the rated alternatives. This polyhedron image works as a type of ‘role-model’ to be used for matching the set of alternatives and rating them. To ‘look’ into a lower level of a polyhedron face (a criterion) will show smaller polyhedra which represent the structure of that criterion. This flexibility allows the expansion or retraction of the system by creating or deleting more inferior polyhedra or more faces in the upper polyhedron, depending on the objective.

An example is a pyramid where each face will represent the attributes age, sex and number of children in the multiple attribute decision problem of determining a subsidy level. The age attribute (one face of pyramid) could itself have a lower pyramid attached with the three variables of Fig. 2.

## 7. Case-base

The purpose of the case-base is to store past cases and enable expansion for any new case that is selected or classified. The main concerns in building a case-base are search, representation and control [9]. The search aspect deals with the minimisation of search by using efficient algorithms and proper indexation. Representation is concerned with the logical storage process to facilitate indexation and search. Questions such as which attributes are relevant and how to take context into account must be addressed. Control ensures that manipulations are ordered and consistent. Case-based reasoning addresses a number of these problems [10–17].

Bearing in mind the intention of working in a fuzzy environment, the above issues assume greater complexity. One problem is how to assign importance to attributes and respective components of the context-domain problem. Some options must be given to the decision-maker, so that he/she can easily state his/her preferences, or, in the case of no preference, use default values. Existing cases can be used for statistical weighting calculations. An approach could be to use each attribute value as a point in the respective matching clusters (fuzzy subsets) representing the components of the attribute. For example, a car with speed 150 km/h, might match the objects 'fast' and 'moderate' of the linguistic variable maximum speed. Another important problem is how to retrieve previous cases to perform the matching when dealing with fuzzy concepts. One option could be to use partial matching [15]. This subject is developed in the approximate reasoning module description below.

## 8. Knowledge-base

With regard to research on knowledge representation the main issue is to develop the capacity of abstracting and generalising information using an abductive perspective (exemplars). For real-life problems it does not seem attainable to have only one general and complete model/ stereotype, since this is likely to be too general to be useful. Therefore, in order to have a set of role-models it is necessary first to determine the payoffs for generality versus costs and usefulness.

In order to build successfully a representation scheme there is a need to be aware of the main problems and points to address. These include first the main forms of imprecision for the context-domain to be dealt with (types 1 and/or 2 and/or 3). Second, features extraction, weighting of the features; objects-type to represent, hierarchies, relations, constraints, goals, objects ratings and so forth. Third, which type of representation schemes to use – bearing in mind that this will be working in a fuzzy environment – from an object-oriented and frame representations to rule-base systems etc. Fourth, how to decide which type of distributions to use (context-dependent) and their universe ranges for fuzzy objects expression and manipulation. All these problems cover a wide range of theories and techniques and are only pointed to here as research topics, being beyond the scope of this paper to develop.

Using an abductive approach, from a set of cases a generalisation can be achieved and then used as a role-model (stereotype). This should also include a form of partial pattern matching capability $[15]$ where the classification process should, by analogy, match previously defined object-types (stereotypes or ‘images’ of alternatives, criteria, attributes and so forth) with the case at hand. The object-types definitions can be both text and/or images.

## 9. Approximate reasoning

The reason for using approximate reasoning in DSS/ES is to perform inference under uncertain conditions such as, “Most people who sneeze and cough have a cold". One of the most important difficulties for approximate reasoning is to choose the appropriate inference mechanism for handling uncertainty. The two types more widely used are probabilistic or fuzzy reasoning. This choice will play a major role in the design of the overall framework. It is beyond the scope of this paper to detail possible methods of both approaches but comprehensive summaries can be found in [2,11].

Both probabilistic and fuzzy approaches perform operations to combine and deduce goals from premises. The importance of these operations is expressed by the proposition 'IF criteria A1 and criteria B3 THEN alternative Ci', where A1 and B3 are combined using the minimum or multiplication of the memberships, respectively for the fuzzy or probabilistic reasoning manipulation. A further essential aspect to include in the framework, is the flexibility of assigning weights to criteria, so that the reasoning process also expresses the decision-maker's criteria preferences. These weights are again manipulated with fuzzy or probabilistic combination operations.

Typically, an approximate reasoning mechanism has to deal with fuzzy conditional statements of the form: If (set of conditions are satisfied) Then (set of consequence can be inferred). Formally, it can be represented by the fuzzy implication $A \rightarrow B$ (note, however, that there are many propositions for handling the implication rule within fuzzy logics; a comprehensive survey is presented in [8]). The two main implication inference rules in approximate reasoning [11] are the generalised modus ponens:

premise 1: If X is A then Y is B
premise 2: $\frac{X\ is\ A'}{Y\ is\ B'}$

and the generalised modus tollens:

premise 1: If X is A then Y is B
premise 2: $\frac{X\ is\ B'}{Y\ is\ A'}$

where A, A', B and B' are fuzzy predicates, e.g. X is A.

An example of the modus ponens reasoning, using the fuzzy set old such that $\mu_{old}$ is the membership value for each label (value) u of the fuzzy set old, is the determination of the goal, 'is Mary old?'(FRIL syntax):

Then, if we know the fact: ((Mary is age 53))

Answer: ((Mary age is 53)(old 53)): (0.58)

(The belief that Mary belongs to the set of old people is therefore 58%)

A further approximate reasoning method which is quite flexible is termed evidential reasoning $[4]$ . This type of reasoning is recommended for case-based problems in a fuzzy environment because it uses a linear combination of criteria, therefore, even when one rule fails, there will always be a support for the majority of existing attributes. This feature is very important in a fuzzy environment since it provides a support even when knowledge about the case is quite poor (for details see $[4]$ ). The example introduced later uses this type of reasoning, so further details are not provided here.

## 10. Fuzzification / defuzzification

The main aim of fuzzification is to convert input data into a suitable form (representation) to be handled by fuzzy sets theory $[11]$ . Conversely, defuzzification aims to provide output forms (graphs, linguistic variables and so on) easily understood by the user. The knowledge representation for problems where uncertainty plays an important role, often relies on fuzzy logic as a means of dealing with approximate reasoning $[22]$ . Conventional approaches can only deal with exact reasoning. As stated by Zadeh $[24]$ , “In fuzzy logic, knowledge is interpreted as a collection of elastic or, equivalently, fuzzy constraints on a collection of variables”.

Bearing in mind this last phrase, research issues related to knowledge representation schemes must address the major problem of how to define structures for fuzzy sets. The prime objective is to be able to define flexible object-types that can accept partial memberships, as well as allowing the possibility of overlapping. Criteria rating can be viewed as linguistic variables [23] as, for example, the heights tall and average, and treated accordingly. For instance (based on [24]) consider the linguistic variable age represented by the universe of discourse $U$ : $[1\ldots 100]$ , where a fuzzy subset young is represented by an ordered pair $\{\mathbf{u},\mu (\boldsymbol {u})\}$ where $u$ represents the value of the fuzzy subset characterised by a membership function $\mu_{young}\colon u\to [0,1]$ which associates with each element $u$ of $U$ a number $\mu_{young}(u)$ in the interval [0,1]. The support for the fuzzy subset young might be $\mu_{young}(u) = f(u)$ for $0\leq u\leq 35$ , where $f(u)$ could be any distribution function.

A graphical example for the fuzzy linguistic variable age, using overlapping triangular distribution is shown in Fig. 2.

Logical relations between each object-type must also be defined so that they can sensibly express conditional implications such as $(A \mid X_{i})$ , read as the plausibility of alternative A conditioned on evidences $X_{i}$ . For example (using FRIL syntax [3]), the sentence ‘Mary is big if she is tall and fat’ can be translated into the rule ((size Mary is big) (height Mary tall) (weight Mary fat)) where the concepts tall, fat and big are all fuzzy variables. In abstract, the rule is ((size X is S) (height XH) (weight XW)). The basic aim here is to develop a knowledge-based system capable of defining and handling fuzzy object-types.

However, achievement of this requires a tool such as support logic programming (SLP) [1] to solve these problems. SLP can be viewed as an extension of logic programming since it combines logic programming capabilities with the ability to represent imprecision. The language FRIL (fuzzy relational inference language) [3] is an implementation of the concepts of SLP which can deal with fuzzy sets and measures. Illustrating, suppose that you want to buy a car and your criteria is that the car is powerful enough to have a fast speed; further, you state that the attribute to evaluate the set of cars (Volvo and Ford) is the speed the cars can achieve and the possible values for the attribute are slow or fast. Using FRIL syntax, the representation of this fuzzy multiple attribute problem is:

(slow [20:1 60:0])

$$
/ ^ {*} \text { fuzzy   object } ^ {*} /
$$

Note 1: Sentences between /\*...\*/ are comments.

Note 2: It is beyond the scope of this paper to explain in detail the fuzzy set representation of the objects slow and fast. However, for example for the fuzzy set slow, the meaning is that for a velocity of 20 miles the membership of belonging to the fuzzy set slow is 1 and this membership decreases until 0 for the velocity of 60 miles. All other velocities not considered in the interval have membership of 0, i.e. they do not belong to the fuzzy set 'slow'.

To sum up, knowledge representation for multiple attribute decision problems with uncertainty features could be expressed by fuzzy variables grouped into attributes which express features of alternatives. The objective can also be defined in terms of linguistic criteria (e.g. buy a car with speed fast).

In addition, a flexible fuzzy decision supporting system must include a simulation ability. This will allow experimentation with different options providing the user with an educated ‘feeling’ for the possible solutions under various circumstances. This ‘learning ability’ of a system will enable improvements and accuracy in the answers. It is a process that can be repeated until the DM is satisfied.

## 11. An example

This example brings together a number of the aspects discussed above. Consider a typical multiple attribute decision problem of deciding which car to buy from a set alternatives (here Ford; Fiat, Opel, Toyota, Peugeot). The criteria (attributes) the decision-maker is taking in consideration for deciding are velocity (maximum speed in km/h) and the price of the alternatives. Using FRIL syntax this is represented as:

(Note: for reasons of economy of space and simplification, only the DM's actions are described in both the dialogue interface and the fuzzification/defuzzification modules.)

Dialogue interface:

{1. Insert alternatives

2. Insert attributes and respective subsets.

3. Define boundaries (range) of fuzzy subsets.

4. Select distribution for fuzzy subsets.

5. Define criteria to use}

Fuzzification / defuzzification:

{1. Select distributions for creating fuzzy variables.

2. Define relations between attributes, fuzzy subsets and alternatives}

## Knowledge-base:

((alternatives cars (Ford, Fiat, Opel, Toyota, Peugeot)))

((attribute speed (slow, moderate, fast)))

((attribute price (cheap, reasonable, expensive)))

((criteria ((price less than 9000) (speed fast))))

(cheap [4000:0, 6750:1, 8500:0])

(reasonable [6750:0, 8500:1, 10250:0])

(expensive [8500:0, 12000:1])

(slow [50:1, 130:0])

(moderate [50:0, 130:1, 180:0])

(fast [130:0, 180:1])

Case-base:

((objective buycar cars (price speed)))

((alternative buycar Ford (7000 160)))

((alternative buycar Fiat (5500 120)))

((alternative buycar Opel (5900 140)))

((alternative buycar Toyota (9500 230)))

((alternative buycar Peugeot (9000 130)))

Approximate reasoning:

qs((final\_support buycar for CAR)
    (criteria\_preferences price CAR less 9200)
    (criteria\_preferences speed CAR equal fast)
    (evlogic true
    ((attribute\_weight speed of CAR) 0.5
    (attribute\_weight price of CAR) 0.5)))

((attribute\_weight speed of CAR)
(object\_weight of CAR is fast) 0.33333
(object\_weight of CAR is moderate) 0.33333
(object\_weight of CAR is slow) 0.33333)))

((attribute\_weight price of CAR)
(object\_weight of CAR is cheap) 0.33333
(object\_weight of CAR is reasonable) 0.33333
(object\_weight of CAR is expensive) (0.33333)))

Notes: qs is the query support in FRIL; evlogic is the name of the evidential rule embedded in FRIL; upper case letters are variables in FRIL and true is the filter of the evidential rule. The program logical decision process is first, to gather the alternatives that fulfil criteria (constraints on the universe space) and, second, to obtain the alternatives rating. Details about the evidential reasoning rule and procedure can be found in [4], here only the essentials are shown.

The answer obtained is:

THE BEST ALTERNATIVES IS: Ford SUPPORT: 0.333333

WITH VALUES: (7200 170) FOR: (price speed)

OTHER ALTERNATIVES SUPPORTS: ((Peugeot (0.309523) (Opel (0.281818)))).

As the results show the supports are not very high, since the problem deals with a combination of criteria (price and speed). The criterion preference on price (less than 9200) includes all cars but the Peugeot, and their price membership values are not very high. The criteria preference on speed eliminates the Fiat.

If the decision-maker wishes to change any settings or criteria, the results will vary accordingly. This allows the DM to learn about the environment and perform as many simulations as s/he wishes in order to investigate alternative scenarios.

This example illustrates the components necessary for a DSS/ES capable of handling uncertain problems and the interactions between the modules. It shows the flexibility necessary in such a system.

## 12. Conclusions

This paper has attempted to provide a framework for uncertainty handling in DSS/ES, focusing on multiple attribute problems. Such a framework will need to include a case-base and knowledge-base; knowledge representation schemes to handle uncertainty (fuzzification/defuzzification methods); approximate reasoning methods and interactive dialogue modelling. Provision of these capabilities will enhance the decision-making process within a fuzzy environment. As the example illustrates, the framework provides a simple and logical way of organising, using and manipulating information thus obtaining more sophisticated responses. The framework presented is but a first step in this direction; yet it is a necessary beginning.

## References

[1] J.F. Baldwin, Support Logic Programming, I.J. of Intelligent Systems 1, (1986) 73–104.

[2] J.F. Baldwin, Evidential Support Logic Programming, Fuzzy Sets and Systems 24 (1987) 1–26.

[3] J.F. Baldwin, T. Martin and B. Pilsworth, FRIL Manual, Bristol, BS8 1QX, UK, FRIL Systems Ltd. Bristol Business Centre (1988).

[4] J.F. Baldwin, Evidential Support Logic, FRIL and Case-Based Reasoning, International Journal of Intelligent Systems (1994) (to appear).

[5] J.F. Baldwin and R.A. Ribeiro, Fuzzy Reasoning by Case for Decision Support Systems, Uncertainty, Fuzziness and Knowledge-Based Systems 2 (1) (1994) (to appear).

[6] R.E. Bellman and L.A. Zadeh, Decision-Making in a Fuzzy Environment Management Science 17 (4) (1970) 141–164.

[7] R.C. Bonczek, C.W. Holsapple and A. Whinston, Developments in Decision Support Systems, Advances in Computers 23 (1984) 141–175.

[8] D. Dubois and H. Prade, Fuzzy Logics and the Generalized Modus Ponens, Cybernetics and Systems: An International Journal 15 (1984) 293–331.

[9] J.L. Kolodner and W. Mark, Case-Based Reasoning, IEEE Expert 7 (5) (1992) 5–6.

[10] J.L. Kolodner, Improving Human Decision Making through Case-Based Decision Aiding, AI Magazine 12 (1991) 52–68.

[11] C.C. Lee, Fuzzy Logic in Control Systems: Fuzzy Logic Controller - Part I and II, IEEE Trans. on Systems, Man, and Cybernetics 20 (2) (1990) 404-435.

[12] K.R. MacCrimmon, An Overview of Multiple Objective Decision Making, in: Multiple Criteria Decision Making, (eds.) J.L. Cochrane and M. Zeleny (University of South Carolina Press, 1973) pp. 18–44.

[13] D.S. Nau and J.A. Reggia, Relationships between Deductive and Abductive Inference in Knowledge-Based Diagnostic Problem Solving, Proceedings of the First International Workshop on Expert Databases Systems, Kiawah Island, SC, USA (The Benjamin/Cummings, 1984).

[14] C.S. Peirce, Collected Papers of Charles Sanders Peirce (Harvard University Press, Cambridge 1932).

[15] R.A. Ribeiro and J.F. Baldwin, Partial Matching in Fuzzy Image Recognition, Proceedings of the Developing and Managing Expert Systems Programs, IEEE Computer Society (1991).

[16] R.A. Ribeiro and P. Powell, The R-P Polyhedron, forthcoming (1994).

[17] C.K. Riesbeck and R.C. Schank, Inside Case-Based Reasoning (Lawrence Erlbaum Associates, London, 1989).

[18] E. Turban, Decision Support and Expert Systems (Macmillan, 1988).

[19] A. Tversky and D. Kahneman, Judgement Under Uncertainty: Heuristics and Biases, Science (September 1974).

[20] A. Tversky and D. Kahneman, Causal Schemes in Judgments under Uncertainty, in: Judgement under Uncertainty: Heuristics and Biases, eds. Kahneman Slovic and Tversky (Cambridge University Press, 1982) pp. 117–128.

[21] L.A. Zadeh, Fuzzy Sets, Information and Control 8 (1965) 338–353.

[22] L.A. Zadeh, A Theory of Approximate Reasoning, in: Tong, Nguyen Yager, Ovchinnikiv, Fuzzy Sets and Applications: Selected Papers by L.A. Zadeh, eds., (John Wiley, 1979) pp. 149–194.

[23] L.A. Zadeh, The Concept of a Linguistic Variable and its Application to Approximate Reasoning – Parts I, II, III, in: Fuzzy Sets and Applications: Selected Papers by L.A. Zadeh, eds. Yager, Ovchinnikiv, Tong and Nguyen (John Wiley, 1987) pp. 219–269.

[24] L.A. Zadeh, Knowledge Representation in Fuzzy Logic, IEEE Transactions on Knowledge and Data Engineering 1 (1) (1989) 89–100.

[25] H.-J. Zimmermann, Modelling Flexibility, Vagueness and Uncertainty in Operations Research, Investigación Operativa 1 (Agosto 1988) 7–85.

![](/api/attachments/CP4HTT2H/fulltext/images/5a1d7ce6d1601099e0234f8643d18f9075b944c22b2120f3a392c1e84fe1cce5.jpg)

Rita A. Ribeiro is assistant professor at the Universidade Nova Lisboa Dept. Informatica; Portugal. She received her Ph.D. from the University of Bristol, UK. She received her M.Sc. from George Washington University, USA and her degree from Instituto Superior Economia, Portugal. Her major research focus is the use of fuzzy logic and fuzzy sets theory in decision-making problems. Current research interests include uncertainty

in decision support systems and fuzzy multiple attribute problems.

![](/api/attachments/CP4HTT2H/fulltext/images/2eadef23f40bfe31f6a472d83cbf06e681a3152191bed7b63322012ca016503a.jpg)

Philip Powell is currently senior Lecturer in Information Systems and ICAEW Academic Fellow in Warwick Business School, having spent time working in insurance, accounting and computing. He has taught in Australia and Portugal and held a number of other posts overseas. He is the author of two books on information systems and financial modelling, numerous book chapters and his work has appeared in Omega, Journal of The Operational Research Society, Journal of Accounting and Business Research, Journal of Information Systems, European Management Journal, Information and Software Technology and Journal of Strategic Information Systems. He is on the editorial board of the Journal of Information Systems and an Associate Editor of OR Insight. His main interests are the organisational impacts of IT, especially decision support systems and expert systems, and the ways such systems might be evaluated throughout the project cycle.

![](/api/attachments/CP4HTT2H/fulltext/images/7fcbfd33eee6dd1ba1c857cd495b353370fe799e53c7a52915af3bdd40cc88ff.jpg)

Professor J.F. Baldwin is Professor of Artificial Intelligence in the University of Bristol and a SERC Senior Research Fellow. He has published over 200 papers in optimal control, decision theory, fuzzy sets, artificial intelligence and logic programming. He developed the support logic programming language FRIL used for knowledge engineering projects throughout the world. He graduated in Physics, has a D.Sc. for his re-

search work, has lectured in many countries and is a consultant for several industries. He is a Director of FRIL Systems Ltd., a Company he started which is responsible for the development and marketing of FRIL.
