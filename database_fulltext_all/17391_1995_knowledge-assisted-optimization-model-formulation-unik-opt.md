---
otero_id: 17391
otero_key: "Z2NPX9ZR"
title: "Knowledge-assisted optimization model formulation: UNIK-OPT"
authors: "Jae Kyu Lee; Min Yong Kim"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)e0028-c"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge-assisted optimization model formulation: UNIK-OPT

Jae Kyu Lee $^{a,*}$ , Min Yong Kim $^{b}$

$^{a}$ Department of Management Information Systems, Korea Advanced Institute of Science and Technology, 207-43, Cheongryangri-dong, Dongdaemun-gu, Seoul 130-012, Korea

$^{b}$ Department of Management Science, Korea Advanced Institute of Science and Technology, 373-1, Kusong-dong, Yusong-gu, Taejon 305-701, Korea

## Abstract

In this paper, we describe a knowledge-assisted optimization model formulation system UNIK-OPT (UNIfied Knowledge-OPTimization). To envision the desirable features of UNIK-OPT, we first establish the design criteria of knowledge-assisted modeling systems. The most distinctive criterion pursued in this research is the independent management of knowledge base from multiple optimization models. To achieve these criteria, we articulate four levels of modeling views: semantic view, modeling language view, mathematical notational view and tabular view. In semantic view, the associations between attributes, blocks of terms and constraints are represented in a constraint network, and a block of terms is represented as a pair of coefficient and variable. Thus, the formulation reasoning is esteemed as a process of helping the construction of a specific semantic model by adding user's problem definition to the extracted relevant semantic level modeling knowledge. Then the specific semantic model can be transformed into other views of model automatically. The prototype UNIK-OPT is developed to realize this idea, and is illustrated with a refinery plant.

Keywords: Design criteria; Knowledge-assisted modeling system; Modeling views; Modeling knowledge; Constraint network; Formulation reasoning process; Index set manipulation

## 1. Introduction

## 1.1. Overview of research

Aiding the formulation process of optimization models has attracted a great deal of research in the model management area. In this line of research, we propose a conceptual framework and develop a prototype UNIK-OPT (UNIfied Knowledge-OPTimization). To determine the desirable features of UNIK-OPT, we first establish the design criteria of knowledge-assisted modeling systems. To achieve the design criteria, we articulate the four levels of modeling views. Finally, we develop a prototype UNIK-OPT which incorporates the modeling views. This paper is organized in the sequence of the above statements. To explain UNIK-OPT, we describe the representation of optimization modeling knowledge, and the formulation reasoning process.

Our ultimate goal of supporting the formulation of optimization modeling process is “to help decision makers – who may not be experts in formulation – as well as model builders so that they can easily specify problems in optimization modeling terms without any ambiguities and errors".

## 2. History of aiding the formulation process

Previous research that attempts to help the formulation process can be classified into the following four categories:

(1) Matrix Generators

(2) Modeling Languages

(3) Structured Modeling Languages

(4) Knowledge-based Approaches

(1) Matrix Generators: Matrix generators accept input data in a predefined format so that an initial table for a specific algorithm (such as the simplex method for linear programming) can be generated. The predefined format should be easier to code, and thus take less coding work than the tabular input format for the algorithms [7]. The functions that matrix generators provide are very primitive, but essential. Therefore, all advanced modeling tools include the matrix generation capability explicitly or implicitly.

This approach requires a model builder with sufficient expertise because there is actually no practical support for the formulation process itself. Existing matrix generators include DATAFORM [23], DATAMAT [42], GAMMA [47,49], MaGen and OMNI/PDS [16,17], IBM MGRW [19], MPSX [20], APEX-III [6], and MODELER [5].

(2) Modeling Languages: Modeling languages are designed so that optimization models can be formulated more easily and compactly than the input formats of matrix generators. In general, the advantages of modeling languages over matrix generators are verifiability, modifiability, documentability, independence from algorithms, and simplicity of modeling [7]. Typical modeling languages include ALPS, GAMS [41], LPMODEL [21], MAGIC, MGG, UIMP, EZLP, LINDO, MPOS, UHELP, PAM [52], LAMP [48], RPMS [4], and AMPL [8]. Most of the systems generate their outputs in a de facto standard form such as the MPS format [20]. Geoffrion [13] proposed a taxonomy of the indexing structures in modeling languages. Hong and Mannino [18] developed the semantics for the unified modeling languages $L_{D}$ which combines logic and mathematical modeling. Since the major users of modeling languages are expected to be modeling experts, it is still not easy for ordinary decision makers to build models with the modeling languages.

(3) Structured Modeling Languages: Structured modeling is a conceptual framework for the modeling process $[9,11]$ . The framework uses a hierarchically organized, partitioned, and attributed acyclic graph to represent both the semantic and the mathematical structure of a model. Many researchers have already developed modeling languages suitable for the structured modeling approach. They include SML $[10]$ , SMSS $[45]$ , ASUMMS $[46]$ , FW/SM $[12]$ , etc. Structured modeling languages are concerned not only with the specification of formulated model, but also with the formulation process. However, the structured modeling languages do not consider the domain knowledge.

(4) Knowledge-based Approaches: There were a few knowledge-based formulation aids which use both formulation knowledge and domain knowledge. Ma, Murphy and Stohr [39,40,43,44] have designed a graphical interface to overcome the problems associated with the development of large, complex linear programming models. The main purpose of this rule-based approach was to help OR experts. Stohr's approach [50] translates the problem specification into a graphical notation rather than a mathematical notation, and transforms the algebraic terms and their subsequent combinations into constraint equations. Although the above studies are very important, they focus on supporting OR experts. Binbasioglu and Jarke [3], however, have suggested a domain-specific approach to support OR-naive users using syntactic knowledge about linear programming and domain knowledge. Krishnan [1,24] has developed $\mathrm{PM^{*}}$ which employs domain-specific knowledge to generate qualitative inferences and modeling knowledge to formulate LP models of production planning domain. $\mathrm{PM^{*}}$ extends previous PDM [25,26]. Murphy et al. [44] has investigated rules for combining component models into a complete linear programming model. The case based reasoning approach to model formulation has been suggested by some researchers. Vellore et al. [51] proposed a case-based planning approach. Liang and Konsynski [38] discussed issues related to modeling by analogy and explored the use of analogical reasoning in model management systems. Binbasioglu [2] investigated the process based analogy approach.

![](/api/attachments/Z2NPX9ZR/fulltext/images/abb8ca3f3aef48d411a2f12ec49626d4cea8bbe01ff3ccef7cf616ce85d665b0.jpg)  
Fig. 1. The architecture of unified modeling.

Recently, the purpose of knowledge-based approach has been extended from the simple frontend formulation support to the unified modeling which includes both knowledge and optimization $[29]$ as depicted in Figure 1. Since this architecture can support nondominated tradeoffs between the objective function in the optimization model and symbolic goals in the rule base, the knowledge can be used to not only formulate but also explain outputs and sensitivity analyses. Under the unified modeling context, we assume that formulation of optimization models is an extraction of relevant modeling knowledge from a corporate modeling knowledge base with an additional definition concerning a specific problem. In this approach, knowledge engineers and modeling experts should, of course, prepare the knowledge base beforehand. Although the preparation of a knowledge base is an expensive task, once it is prepared, it can be shared by multiple OR-naive users.

## 3. Design criteria of knowledge-assisted modeling system

To identify the research targets, let us summarize the design criteria of knowledge-assisted modeling systems. We suggest the following 17 criteria.

(1) Representational Adequacy: The domain context, generic knowledge structure of the optimization models, and structure of specific optimization models should be represented adequately. The model representation should be understandable and modifiable.

(2) Algorithm Independence: Different algorithms may require different input tabular forms. However, decision makers should be allowed to specify problems free from the algorithm-specific input format. It is also desirable to support the selection of an appropriate solution algorithm or a combination of algorithms if multiple alternative algorithms exist [36].

(3) Data Independence: The data for each optimization model may require different units of time and aggregation levels. On the other hand, a relational database can maintain only one type of time unit and aggregation level. Therefore, an object-oriented transformation of units and aggregation levels is necessary.

(4) Knowledge Independence from Optimization Models: Since multiple optimization models should share a common knowledge base, maintaining consistency among optimization models is very important. Thus it is critical to manage the knowledge base independently from the optimization models.

(5) Domain Independence: The modeling system should be usable independent from domains. The application domain should be determined by the entered domain knowledge. However, since a domain may determine the user-interfaced screens, such a domain specific feature should be programmable by a general purpose programming language.

(6) Level of Abstraction: Representation of the abstraction level is necessary to identify the right level of constraints as well as the right units for data retrieval. Thus, during the formulation process, the modeling system should permit the model builder to select the abstraction level.

(7) Semantic Level Dialogues for Sensitivity Analysis: In traditional optimization packages, sensitivity analysis is done by changing coefficients or right hand side (RHS) values. However, OR-naive managers need to perform the WHAT-IF analysis in a more natural way at a semantic level. For example, “WHAT is the change in cost IF the price of all Iranian crude oils rise by 10%?”

(8) Automatic Syntax Error Check: Incomplete models due to a missed RHS or left hand side (LHS), inconsistent constraints, and redundant constraints should be automatically checked and displayed to model builders.

(9) Reusability of Previously Built Models: In the model management system environment, it is essential to reuse previously built models. Previously built models should be saved so that they can be retrieved and modified for similar applications. An analogy-based model formulation is a challenging issue to pursue $[37]$ .

(10) Learning from Previous Models: In addition to reusing the previously built models, we should also be able to learn from previous models to build a common modeling knowledge base. Therefore, we need a case-based learning mechanism [33].

(11) Guidance for the Ambiguity Elimination Process: When an optimization model formulation is considered as an extraction of optimization model's components from a corporate modeling knowledge base, the constraints and objectives associated with the selected decision variables should be automatically traced and extracted. When the extracted model has unresolved ambiguities, the formulator should help resolve these ambiguities by drawing attention to them.

(12) Automatic Transformability: The modeling system should be able to transform the model specification from one form to another. Parallel representation of multiple views of models may also be helpful during a certain step of formulation [22].

(13) Distinguishability of Objective Knowledge from Subjective Knowledge: Some knowledge such as physical facilities constraints are objective and can reliably be used in any related models. However, some soft constraints such as the “availability of raw material by next month” may change depending upon the degree of acquisitional effort. Whether to accept the availability as a constraint or not depends upon a subjective judgment. For such subjective knowledge, meta-knowledge which can answer “why, when, and whom” types of questions should be asked so that the model builder can judge whether he/she would accept the assumptions behind the knowledge for his/her own decision model.

(14) Integration with Other Related Models: The formulated optimization models should be capable of integrating with a relevant knowledge base as well as a database. To integrate relevant knowledge, Post-Model Analysis (PMA) may be applied [27,28,29,31,32,34] as depicted in Figure 1.

(15) Minimal Information Request from the Model Builder: Model builders want to input a minimal amount of information to formulate their desired models. However, the modeling systems should not be overautomated, because it may deprive a certain degree of control from the model builders. The degree of controllability and automation should be balanced.

(16) Explanation Capability: The output of an optimization model should be explained in understandable terms and forms such as natural language [15]. An important issue is how to associate the output with other relevant knowledge for explanation purposes.

(17) Analysis of Formulated Models: The analysis on infeasibility [14] and the graphical display of the special structures of formulated models are helpful for the a priori validation of models. ANALYZE [15] is a research of this kind.

## 4. Modeling views

There is no single software that can satisfy all of the design criteria. In this paper, we will focus on the following design criteria:

![](/api/attachments/Z2NPX9ZR/fulltext/images/981ffdda2996ef0eaee0836650bd3fdc794afa7cfac38c11fd7c1dd0f3dfb4d8.jpg)  
Fig. 2. Four modeling views.

1. Representational adequacy

2. Data independence

3. Knowledge independence from optimization models

4. Domain independence

5. Level of abstraction

6. Guidance for the ambiguity elimination process

7. Automatic transformability

8. Distinguishability of objective knowledge from subjective knowledge

9. Minimal information request from the model builder

To reflect the above design criteria in the knowledge-assisted formulation systems, we propose four views of optimization models: Semantic View, Modeling Language View, Mathematical Notational View, and Tabular View. The relationships among them are graphically shown in Figure 2.

## 4.1. Semantic view

The semantic view specifies the optimization model in a formal knowledge representation such as frames. This view includes information not only about the structure of the model, but also about the meanings of indices, variables, coefficients, and constraints. The semantic view of a specific model consists of two portions of knowledge: the relevant modeling knowledge extracted from the common modeling knowledge base, and the model builder's problem definition which specifies the concerned indices and constraints.

The semantic view is a key medium to achieve most of the design criteria. Since the semantic view is a complete representation of a model, it can be syntactically transformed into lower levels of representation such as modeling languages and mathematical notations.

## 4.2. Modeling language view

This view represents models in modeling languages as described earlier. The modeling language view may be skipped if the semantic view can be completely formulated. However, a specific modeling language may be necessary to use a certain package or to verify the model by visually inspecting the modeling language with which the model builder is familiar. For instance, the output of logic-based modeling support system PM\* [1] is a structured modeling language. However, as the system evolves, the final output may directly generate a MPS format skipping the structured modeling language representation.

## 4.3. Mathematical notational view

Mathematical notational view is what we have been using in the literature of optimization. This is the most familiar representation to trained model builders. Thus this representation can be an effective medium of visual model verification. The notational view can be further classified into two views: aggregate notational view and individual equational view.

## (1) Aggregate notational view

The term “aggregate” implies the aggregation for the block of terms and constraints. Aggregation with respect to the blocks of terms implies shared summation signs as illustrated in equation

$$
\sum_ {i = 1} ^ {m} P _ {i t} + \sum_ {i = 1} ^ {m} I _ {i t} ^ {+} - \sum_ {i = 1} ^ {m} I _ {i t} ^ {-} = \sum_ {i = 1} ^ {m} S _ {i t}.\tag{1}
$$

On the other hand, aggregation for a constraint set implies aggregate representation of constraints in “for all…” form. For example, the equations in (2) are effective for m i’s and n t’s.

$$
\begin{array}{l l} P _ {i t} + I _ {i t} ^ {+} - I _ {i t} ^ {-} = S _ {i t} & i = 1, \ldots , m \\ & t = 1, \ldots , n. \end{array}\tag{2}
$$

## (2) Individual equational view

Aggregate notation can be further broken down into individual equations and terms. For example, the aggregate forms in (1) and (2) can be converted into (3) and (4) respectively.

$$
\begin{array}{r l} & \left(P _ {1 1} + P _ {2 1} + \dots + P _ {m 1}\right) + \left(I _ {1 1} ^ {+} + I _ {2 1} ^ {+} + \dots + I _ {m 1} ^ {+}\right) \\ & - \left(I _ {1 1} ^ {-} + I _ {2 1} ^ {-} + \dots + I _ {m 1} ^ {-}\right) \\ & = S _ {1 1} + S _ {2 1} + \dots + S _ {m 1}. \\ & P _ {1 1} + I _ {1 1} ^ {+} - I _ {1 1} ^ {-} = S _ {1 1}, \\ & P _ {1 2} + I _ {1 2} ^ {+} - I _ {1 2} ^ {-} = S _ {1 2}, \\ & \dots \\ & P _ {m, n - 1} + I _ {m, n - 1} ^ {+} - I _ {m, n - 1} ^ {-} = S _ {m, n - 1}, \\ & P _ {m, n} + I _ {m, n} ^ {+} - I _ {m, n} ^ {-} = S _ {m, n}. \end{array} \tag {3}
$$

In the above examples, all coefficients are fixed to 1 or -1. However, in general the coefficients may be notationally represented as the $a_{ij}$ 's in example (5).

$$
\begin{array}{c} a _ {1 1} P _ {1} + a _ {1 2} P _ {2} + \dots + a _ {1 m} P _ {m} \leq b _ {1}, \\ a _ {2 1} P _ {1} + a _ {2 2} P _ {2} + \dots + a _ {2 m} P _ {m} \leq b _ {2}, \\ \dots . \end{array}\tag{5}
$$

Upto this point, the model is data independent. To feed data into the model, data from the database must be transformed into a form compatible with the coefficients in the optimization model. Thus, after having entered the data, model (5) becomes model (6).

$$
\begin{array}{c} 0. 1 P _ {1} + 0. 2 P _ {2} + \dots + 0. 1 P _ {m} \leq 1 0 0 0, \\ 0. 2 P _ {1} + 0. 3 P _ {2} + \dots + 0. 4 P _ {m} \leq 1 5 0 0, \\ \dots . \end{array}\tag{6}
$$

## 4.4. Tabular view

The tabular view is the tabular input form of an algorithm. If there is more than one applicable alternative algorithm, an algorithm should first be selected or synthesized. If we reduce the scope to linear programming models, the selection of algorithms may not be a major issue. However, if we expand the scope of optimization models including both nonlinear and integer programming models, the selection or synthesis of an algorithm becomes very important. To support the selection effectively, proper identification of a model's structure and precise mapping with appropriate algorithms are necessary. J.S. Lee et al. [36] have studied the model structure identification to guide the algorithm selection for a class of integer programming problems. Even for the solution of linear programming models, the tabular view may take one of the initial tables of the Simplex Method, Revised Simplex Method, or the input format of MPSX. Thus the tabular view is very algorithm-specific and implementation-specific.

## 5. Architecture of UNIK-OPT

To realize the design criteria with the multiple modeling views, we propose a system UNIK-OPT which is a knowledge-assisted optimization model formulator. UNIK-OPT is developed as an optimization model formulating component of the UNIK (UNIfied Knowledge) system, which supports unified modeling including both optimization models and knowledge-based systems [29].

The overall architecture of UNIK-OPT is shown in Figure 3. UNIK-OPT adopts three modeling views: semantic view, mathematical notational view, and tabular view. A specific semantic model consists of relevant modeling knowledge (which is a subset of modeling knowledge base) and user's problem definition. The process of generating the specific semantic model using the modeling knowledge base is the formulation process which is performed by the semantic model formulator. Once the specific semantic models are prepared, they can be automatically transformed into the mathematical notational forms and tabular forms. In this paper, we will describe the representation of modeling knowledge base and specific semantic model, and the formulation reasoning process.

A key advantage of UNIK-OPT's architecture is that it can help make the optimization model independent from the common modeling knowledge base. This means that when the common modeling knowledge base is changed, previously generated multiple associated specific models can share the impacts of change without losing consistency. Independence can be attained by specifying the relevant modeling knowledge using logical pointers to the common modeling knowledge base. Since the mathematical notational form and tabular forms can be automatically generated from the relevant knowledge base, we can also maintain consistency among different views.

## 6. Representation of modeling knowledge

To explain UNIK-OPT, let us describe the representation of optimization modeling knowledge. As a first step of this research, we restrict the scope of optimization models to linear programming models.

![](/api/attachments/Z2NPX9ZR/fulltext/images/4acd2faabfa5def8a185e9cd60531779c440dff96471db342a7e3b8fbd12ab54.jpg)  
Fig. 3. Architecture of UNIK-OPT.

![](/api/attachments/Z2NPX9ZR/fulltext/images/20109fe5fbe4b8646008849e525e4173b8549c64fb8440348d24dea4d29d61a6.jpg)  
Fig. 4. Structure of modeling knowledge base.

## 6.1. Structure of modeling knowledge

The knowledge base for linear programming models has the structure depicted in Figure 4. At the top level, there are objectives and index-free constraints. An objective is composed of index-free blocks of terms, while the index-free constraint is composed of index-free blocks of terms and an operator ( $\leqslant$ , $\geqslant$ , or =). The blocks of terms (BOT) are “a set of terms which share the same summation sign.” So the terms within the same BOT should share the same sorts of coefficients and decision variables. Thus the index-free BOT can be represented by a pair of coefficient and decision variable. The decision variables and coefficients have potentially linkable indices.

The knowledge structure of linear programming models resembles the molecular structure. A decision variable resembles a proton; a coefficient resembles a neutron. A pair of decision variable and coefficient making up a BOT resembles a nucleus. The linkable indices resemble the electrons. By linking specific indices to the BOT, they construct an indexed BOT which resembles an atom. A constraint consists of a set of indexed BOT's with an operator and resembles a molecule that consists of a set of atoms. Finally, when an objective and a set of constraints are combined, they construct a meaningful linear programming model, which resembles the DNA that is the key element of living creatures. Thus, the formulation reasoning process is analogous to the process of DNA synthesis from protons, neutrons and electrons.

## 6.2. Diagrammatic representation of constraint network

A diagrammatic representation is helpful to the knowledge engineers even though the diagrams cannot completely represent the knowledge. We propose a diagram named constraint network which effectively shows the relationships between attributes, index-free BOT's and constraints. Let us define components of the diagram.

○ : attribute.

☐ : index-free BOT that consists of a pair of coefficient and decision.

: Operator in a constraint
The operator may be one of the following: = (EQ), ≤ (LE), ≥ (GE).

$\xrightarrow{+, -}$ : Arrows indicate the associations between constraints and BOT's. The “+” or “-” sign on the arrow is the sign of a BOT.

An example of constraint network is shown in Figure 5. In this example, there are four constraints, nine BOT's and one attribute. The diagram can be represented in frames as follows:

{{BOT
    is\_a:
    coefficient:
    decision:}}

(7)

For instance,

{{PRODUCTION\_AMOUNT\_BOT
    is\_a: BOT
    coefficient: 1
    decision: PRODUCTION\_AMOUNT}}

{{PRODUCTION\_COST\_BOT is\_a: BOT

![](/api/attachments/Z2NPX9ZR/fulltext/images/2bd6dcdd79b74af92f5690b4af1e0c11935ec094f0db5591d12e93fc8683d35d.jpg)  
Fig. 5. Constraint network.

```txt
coefficient: UNIT_COST
decision: PRODUCTION_AMOUNT}}
```

```txt
{{MARKETING_COST_BOT
    is_a: BOT
    coefficient: 1
    decision: MARKETING_COST}}
{{SALES_VOLUME_BOT
    is_a: BOT
    coefficient: 1
    decision: SALES_VOLUME}}
{{FACILITY_CAPACITY_BOT
    is_a: BOT
    coefficient: 1
    decision: FACILITY_CAPACITY}}
```

(8)

```txt
{{PROCESSING_TIME_BOT
    is_a: BOT
    coefficient: UNIT_PROCESSING_TIME
    decision: PRODUCTION_AMOUNT}}
```

These three BOT's are derived from the attribute PRODUCTION-MOUNT. The decision slot implies that the values for the slot are determined by solving an LP model. However, if the values can be retrieved from the existing database, we do not have to compute from the LP model. Whether we compute or retrieve should be decided during the formulation process. That is why the slot is named decision rather than decision variables. For instance, the MARKETING-COST, SALES-VOLUME, and FACILITY-CAPACITY in (9) can be either variables or data depending upon the role of the model.

(9)

The data availability will be determined when the indices are linked with the coefficients and decisions. This can be done effectively through IF-NEEDED demons.

Constraints can be constructed by composing the BOT's. The four constraints in this example can be represented in the frames as follows:

```txt
{{PRODUCTION_SALES_BALANCE
    is_a: CONSTRAINT
    operator: EQ
    LHS: (+PRODUCTION_AMOUNT_BOT)
    (+ (t - 1 INVENTORY_BOT))
    RHS: (+SALES_VOLUME_BOT)
    (+INVENTORY_BOT)
```

```lisp
context: (TIME_UNIT MONTH)
(HORIZON YEAR)
(OBJECTIVITY YES)
```

```txt
{{NO_LEFT_OVER
    is_a: CONSTRAINT
    operator: LE
    LHS: (+PRODUCTION_AMOUNT_BOT)
    RHS: (+SALES_VOLUME_BOT)
    context: (TIME_UNIT YEAR)
    (HORIZON YEAR)
    (OBJECTIVITY NO)}
```

```handlebars
{{PRODUCTION_CAPACITY is_a: CONSTRAINT operator: LE LHS: (+PROCESSING_TIME_BOT) RHS: (+FACILITY_CAPACITY_BOT) context: (OBJECTIVITY NO)}}
```

```handlebars
{{CORPORATE_PROFIT
    is_a: CONSTRAINT
    operator: EQ
    LHS: (+SALES_AMOUNT_BOT)
    (-PRODUCTION_COST_BOT)
    (-MARKETING_COST_BOT)
    RHS: (+PROFIT_BOT)
    context: (OBJECTIVITY YES)}
```

The symbol “t - 1” in the constraint PRODUCTION-SALES-BALANCE is a time decrementer. Note that there are context slots in the constraints. This kind of context is necessary to resolve conflicts between multiple constraints associated with the same set of BOT's. The context for the constraint PRODUCTION-SALES-BALANCE means that the constraint is necessary for the models with months as the time unit and a year as the planning horizon. It also says that this constraint should be applied objectively. So any model which includes the associated BOT's (PRODUCTION-AMOUNT-BOT and INVENTORY-BOT) should also include this constraint. On the other hand, the constraint NO-LEFT-OVER may be applied when both the planning horizon and time unit is a year, and will not be applied objectively. Some managers may feel it is better not to leave any inventory at the end of year, while others may not agree with that idea. This kind of subjective constraint may be selectively adopted during the formulation process depending upon the model builder's judgment.

## 6.3. Representation of indices and attributes

The indices may be concerned with products, facilities, materials, and time units. Thus this information may be used not only for modeling, but also for other purposes. The index information should be prepared by knowledge engineers in advance as opposed to learning from previous models which may not cover the entire indices. An example of index PRODUCT may be defined as (11).

{PRODUCT
    is\_a: INDEX
    symbol: i
    linkable\_attribute:
    PRODUCTION\_AMOUNT
    INVENTORY
    UNIT\_COST
    UNIT\_PROCESSING\_TIME
    SALES\_VOLUME}}

(11)

The symbol i and linkable attributes are defined at the class level. Each index is assigned with an unique symbol. This ensures that a formulation contains no aliases. Although a large portion of the linkable attributes may be learned from previous models, the knowledge engineer still needs to prepare a comprehensive potential linkage.

If we have product groups (say product 1 and 2 belong to group P; and product 3, 4 and 5 belong to group Q), we may utilize a hierarchical representation as in (12).

{{PRODUCT\_GROUP\_P is\_a: PRODUCT}}

{{PRODUCT\_1
is\_a: PRODUCT\_GROUP\_P}}

(12)

{{PRODUCT\_3
    is\_a: PRODUCT\_GROUP\_Q}}

The hierarchical representation is very important for supporting the model's level of abstraction. The facilities and materials way be represented in a similar way.

The coefficients and decisions are represented as attributes. At the class level, the attributes can be defined as (13).

{{ATTRIBUTE
    is\_a:
    symbol:
    linkable\_index:}}

(13)

For instance, the attributes PRODUCTION-AMOUNT and UNIT-PROCESSING-TIME are represented in frames as (14).

{{PRODUCTION\_AMOUNT
    is\_a: ATTRIBUTE
    symbol: X
    linkable\_Index: PRODUCT
    FACILITY
    TIME}}

{{UNIT\_PROCESSING\_TIME
    is\_a: ATTRIBUTE
    symbol: a
    linkage\_index: PRODUCT FACILITY}}

(14)

The linkable-index slot in the ATTRIBUTE frame is the inverse relationship of the linkable-attribute slot in the INDEX frame.

## 7. Formulation reasoning process

We would like to design the formulation reasoning process based on the knowledge presented in the previous section. Our goal is to minimize the model builder's input burden while allowing control during the model formulation process. In short, the formulation process starts with the selection of indices. Then UNIK-OPT assists in the selection of decision variables and constraints. There are ten detail steps in the formulation process:

1. Select indices.

2. Show the linkable attributes.

3. Combine the attributes with indices.

4. Identify the data availability.

5. Select decision variables.

6. Construct blocks of terms.

7. Elicit associated constraints.

<table><tr><td>{{PRODUCT_1is_a:PRODUCTsymbol: P1}}</td><td>{{FACILITY_1is_a: FACILITYsymbol: F1}}</td></tr><tr><td>{{PRODUCT_2is_a:PRODUCTsymbol: P2}}</td><td>{{FACILITY_2is_a: FACILITYsymbol: F2}}</td></tr><tr><td>{{PRODUCT_3is_a:PRODUCTsymbol: P3}}</td><td>{{MONTHis_a: TIME_UNITsymbol: tstart: (JAN 1993)end: (DEC 1993)}}</td></tr></table>

8. Select objectives and constraints.

9. Eliminate ambiguities in indices.

10. Generate individual equations with data values.

We will contrast the roles of Model Builder with UNIK-OPT by identifying them in brackets.

## Step 1: SELECT INDICES

[UNIK-OPT] UNIK-OPT shows the domain knowledge about product, facility, time, and so forth so that the model builder can select the interesting ones.

[Model Builder] Model builder selects relevant indices. For instance, he may select i = P1, P2, P3 for PRODUCT-1, PRODUCT-2, PRODUCT-3; j = F1, F2 for FACILITY-1 and FACILITY-2; time-unit = month with starting-time = Jan 1993 and ending-time = Dec 1993.

[UNIK-OPT] Construct frames for the indices. The resulting instance frames are shown in (15). The instance frames are elements of index sets that define their domain.

(15)

Step 2: SHOW THE LINKABLE ATTRIBUTES [UNIK-OPT] For the selected indices i, j and t, show the linkable attributes in (11) which were predefined by knowledge engineers as illustrated in Figure 6.

## Step 3: COMBINE THE ATTRIBUTES WITH INDICES

[UNIK-OPT] Generate all possible combination of attributes with indices as illustrated in Figure 7. Note the ambiguities in the attributes X and c. These ambiguities will be removed while we define decision variables.

## Step 4: IDENTIFY THE DATA AVAILABILITY

[UNIK-OPT] The indexed attributes should be converted into relational calculus so that the data dictionary can be checked to identify the data availability. For instance, the availability of $X_{it}$ (production amount of product i at month t where i = PRODUCT-1, PRODUCT-2, PRODUCT-3 and $t = (\text{Jan } 1993), \ldots, (\text{Dec } 1993)$ ) can be confirmed by checking

$$
\begin{array}{l l} \text { EXISTS } & \text { PRODUCTION - AMOUNT } \\ & \text { FORALL   PRODUCT } \otimes \text { MONTH } \\ & \text { WHERE   PRODUCT = PRODUCT - 1 } \\ & \text { OR   PRODUCT - 2 } \\ & \text { OR   PRODUCT - 3 } \\ & \text { AND   MONTH = (Jan   1993) } \\ & \text { OR   (Feb   1993) } \\ & \text { OR...OR   (Dec1993) } \end{array}
$$

The symbol $\otimes$ means Cartesian product. In this example, assume that it turned out $X_{it}$ , $X_{ijt}$ and $I_{it}$ are variables while $c_{i}$ , $c_{it}$ , $a_{ij}$ , $b_{jt}$ and $s_{it}$ are constants. This process may be handled semi-automatically to allow the model builder an opportunity to determine the role of the attribute regardless of data availability. Some of the resulting frames are shown in (16).

{{PRODUCTION\_AMOUNT\_WITH\_INDEX\_ijt
    is\_a: INDEXED\_ATTRIBUTE
    attribute: PRODUCTION\_AMOUNT
    index: PRODUCT FACILITY TIME\_UNIT
    symbol: X(i, j, t)
    data\_availability: no}}

{{INVENTORY\_WITH\_INDEX\_it is\_a: INDEXED\_ATTRIBUTE attribute: INVENTORY index: PRODUCT TIME\_UNIT symbol: I(i, t) data\_availability: no}}

{{UNIT\_COST\_WITH\_INDEX\_it is\_a: INDEXED\_ATTRIBUTE attribute: UNIT\_COST index: PRODUCT TIME\_UNIT symbol: c(i, t) data\_availability: yes}}

(16)

{{PROCESSING\_TIME\_WITH\_INDEX\_ij
    is\_a: INDEXED-ATTRIBUTE
    attribute: PROCESSING\_TIME
    index: PRODUCT FACILITY
    symbol: a(i, j)
    data\_availability: yes}}

![](/api/attachments/Z2NPX9ZR/fulltext/images/c2de8a4023106d3caf123ab0105770093d92edd0f946b3e42e453bdd818b4066.jpg)

![](/api/attachments/Z2NPX9ZR/fulltext/images/83e77843d5352926dcccd39633d63e71ee58871badad49ac920d6327103a6b25.jpg)

Step 5: SELECT DECISION VARIABLES [UNIK-OPT] To help in the selection of decision variables, the system displays the candidate decisions for which data is unavailable. In this example, $X_{it}$ , $X_{ijt}$ and $I_{it}$ will be displayed with the meanings of the symbols.

[Model Builder] The model builder should select the decision variables. Suppose $X_{ijt}$ is selected. [Note] The selection of $X_{ijt}$ will eliminate $X_{it}$ , which has removed ambiguity among variables. Note $I_{it}$ was not selected at this step and should be considered in conjunction with $X_{ijt}$ . We have intentionally missed $I_{it}$ in this example to show how this kind of mistake can be corrected in the following step. We will see that $I_{it}$ will be picked up when we select constraints in Step 8.

## Step 6: CONSTRUCT BLOCKS OF TERMS

Step 6. CONSTRUCT BLOCKS OF TERMS [UNIK-OPT] To construct meaningful BOT's, the BOT frames that include the selected decision variable PRODUCTION-AMOUNT such as in (8) will be recalled as Figure 8. There is an ambiguity in the coefficient of PRODUCTION-COST-BOT. This is where the ambiguity in constants should be clarified by asking the model builder.

[Model Builder] Suppose the $c_{i}$ is selected for PRODUCTION-COST-BOT. Then $c_{it}$ will be permanently eliminated from the BOT.

[Note] The three BOT's are no more than the starting points for model construction. This means that there is no guarantee that all of these BOT's will be included in the final model. These candidate BOT's will elicit related constraints and objectives by tracing the constraint network in Figure 5. Then the model builder will select the constraints for a specific model out of the elicited constraints. If a candidate BOT is not associated with the modeler-selected constraints, it will be removed from the final model specification. In this simple example, all of the three BOT's are selected by chance in the final model. The logically replicated BOT's construct a specific relevant modeling knowledge base.

Step 7: ELICIT ASSOCIATED CONSTRAINTS [UNIK-OPT] Running through the constraint network, the three BOT's can find four related constraints and six associated BOT's. The elicited constraints are PRODUCTION-SALES-BALANCE, NO-LEFT-OVER, PRODUCTION-CAPACITY and CORPORATE-PROFIT.

[Note] The “context” will be automatically activated to remove out of context constraints such as NO-LEFT-OVER. However, to be cautious, we may leave this decision making process to the model builder. Automation may reduce the burden of the model builder, but the risk of removing necessary constraints can be increased. The constraint elicitation stops when the associated BOT’s are bounded by constant BOT’s or when the network is exhausted.

Step 8: SELECT OBJECTIVES AND CONSTRAINTS

[Model Builder] (1) Objective Selection: From the BOT's shown in Step 6, the model builder can select more than one BOT to construct an objective function. In this example, the minimization of PRODUCTION-COST-BOT is selected. This implies that the constraints directed by this objective node may be removed from the model; therefore, the CORPORATE-PROFIT constraint will be removed. If we select multiple incommensurable objectives, the model can be easily expanded to the Multiple Objective Decision Making problems.

(2) Constraint Selection: Suppose two constraints, PRODUCTION-SALES-BALANCE and PRODUCTION-CAPACITY are selected. By selecting the PRODUCTION-SALES-BALANCE constraint, the INVENTORY-BOT is added to the model which brings in $I_{it}$ .

Suppose we have named the model MONTH-

![](/api/attachments/Z2NPX9ZR/fulltext/images/3db647b3a5568a6af169fcc4165f6c2498fed9cb9b7af505a895d65ac527745b.jpg)

![](/api/attachments/Z2NPX9ZR/fulltext/images/42f22f96ea0c5176c1a2372eb9798b18c583a6daac2b222dd6a13d1383416e90.jpg)

(18)

(19)

(20)

(21)

LY-PRODUCT-MIX-1993. The semantic model we have at this point is the model shown in (17).

{{MONTHLY\_PRODUCT\_MIX\_1993

```txt
is_a: LP_MODEL
objective_function: (MIN PRODUCTION_COST) (17)
constraints: PRODUCTION_SALES_BALANCE
PRODUCTION_CAPACITY})
```

## Step 9: ELIMINATE AMBIGUITIES IN INDICES

In the mathematical notational form, the model formulated at this point looks like Figure 9.

The indices in the summation and constraint unit are not identified as marked by “\*\*\*”. To identify the indices, UNIK- OPT has to generate a dialogue requesting a minimum number of questions from the model builder. To formalize a theory behind this process, let us discuss this issue in the following section.

Step 10: GENERATE INDIVIDUAL EQUATIONS WITH DATA VALUES

[UNIK-OPT] After having eliminated ambiguities, UNIK-OPT can generate individual equations with data values. To feed data into the model, UNIK-OPT generates database retrieval statements from the indexed attributes. For instance, to retrieve the value of $c_{1}$ (unit cost of PRODUCT-1), the expression should be converted into the relational calculus:

RETRIEVE UNIT-COST
WHERE PRODUCT = PRODUCT-1

## 8. Index set manipulation

Let us develop a theoretical basis for the index set manipulation necessary for the dialogues in Step 9. The theorems developed here can be used for the automatic generation of index sets.

## 8.1. Indices for objective function

The objective function may have more than one BOT. For each BOT, we can apply the following rule for the generation of summation indices.

RULE: All indices of the decision variables in the objective function should be summed.

An intuitive rationale for the rule is that the indices of decision variables in the objective function are selected because they must be considered. Another structural rationale is that all indices should be summed to make the objective function a scalar value. So in this example, all indices i, j and t in $X_{ijt}$ should be summed. Thus, the objective function is:

$$
\sum_ {i j t} c _ {i} X _ {i j t}.\tag{22}
$$

The objective function implies the total production cost of all products produced by all facilities during the entire year of 1993.

To construct the combination of compatible indices in Step 10, we need to refer to knowledge about index compatibility. For instance, some products cannot be produced in certain facilities; some products should not be produced during certain periods, etc. These restrictions, preferences and strategies can be considered when indices are combined. The prohibited combinations of indices will not be included in the model.

In the previous example, recall that there were three products, two facilities, and 12 months. Suppose the restrictions here are (23).

(23)

```txt
{{PRODUCT_3
    is_a: PRODUCT
    must_not_be_produced: (JUL 1993) (AUG 1993)}}
```

![](/api/attachments/Z2NPX9ZR/fulltext/images/cd67750f1fe1890d6b5fe290fd93a661d1369c6eabbec03437d24bce985dc811.jpg)

![](/api/attachments/Z2NPX9ZR/fulltext/images/bc0f88f297b4551fd3542cc379cd0251bad522bd6504168d8a31d8b3e67bf3cd.jpg)

Suppose the values $c_{1}=5$ , $c_{2}=4$ , and $c_{3}=7$ are retrieved from the database. Then the terms in the objective function look like Figure 10.

The convention used for the construction of individual variable name is $[X \mid Product-Number \mid Facility-Number \mid Month-Name]$ . In the term “5XP1F1MAR”, 5 is the coefficient value of $c_{1}$ ; X is the attribute PRODUCTION-AMOUNT, P1 is PRODUCT-1; F1 is FACILITY-1; MAR is March. The number of variables is reduced to 42 for all possible 72 combinations. If we include all 72 variables in the model, we have to assign a very large number, M, to the restricted variables (to push them to zeros) which would be a useless computational burden. The same variable naming convention and index combination principle can also be applied to the terms in constraints.

## 8.2. Indices for constraint unit

To eliminate the ambiguities in the constraints (19)-(20), there are two approaches: One approach is to decide the set of summation indices of each BOT sequentially, and derive the set of unit indices for each constraint set. According to this approach, the model builder should decide indices six times. The other approach is to decide the set of unit indices for each constraint set, and derive the set of summation indices of BOT's in each constraint set. The latter approach requires just two decisions to select indices. The latter can obviously lighter the model builder's burden. Thus, to formalize the second approach, we need to develop the following theorems to manipulate index sets.

[Definition] Index space of a constraint set, $I_{C}$ , is the union of indices of all attributes in the constraint set.

[Example] For the constraint sets (19) and (20),

$$
I _ {C} \text {   for   (19)   } = \{i, j, t \}
$$

$$
I _ {C} \text {   for   } (2 0) = \{i, j, t \}
$$

[Definition] Index space of the ith block of terms in a constraint set, $I_{T}^{i}$ , is the union of indices of all attributes in the ith block of terms.

[Example] The blocks of terms in (19) and (20) have the following index spaces.

$$
\sum a _ {i j} X _ {i j t}: \{i, j, t \}\tag{24}
$$

$$
\sum b _ {j t} \colon \{j, t \}\tag{25}
$$

$$
\sum X _ {i j t} \colon \{i, j, t \}\tag{26}
$$

$$
\sum I _ {i t} \colon \{i, t \}\tag{27}
$$

$$
\sum s _ {i t} \colon \{i, t \}\tag{28}
$$

The index space of a constraint set subsumes the index space of a block of terms in the constraint set (i.e., $I_{C} \supseteq I_{T}^{i}$ ). Actually $I_{C}$ is equal to the union of all $I_{T}^{i}$ in the constraint set, $\bigcup_{i=1}^{n} I_{T}^{i}$ .

[Definition] Unit index set of a constraint set, $I_{U|C}$ , identifies the unit of constraint in a constraint set. $I_{U|C} \subseteq I_{C}$ .

[Example] From $I_{C}=\{i,j,t\}$ of constraint set (19), suppose the model builder has selected $\{j,t\}$ as unit indices of constraint set (19). Notationally, $I_{U|C}$ for constraint set (19) is $\{j,t\}$ . In the same way, suppose $I_{U|C}$ for the constraint set (20) is $\{i,t\}$ .

[Definition] Summation index set of the ith block of terms, $I_{S|T}^{i}$ , is the index set attached to the summation sign of the ith BOT, which is a subset of $I_{T}^{i}$ .

[Theorem 1] Summation index set of the ith block of terms is equal to index space of the ith block of terms minus unit index set of a constraint set.

Symbolically,

$$
I _ {S \mid T} ^ {i} = \left(I _ {T} ^ {i} - I _ {U \mid C}\right).\tag{29}
$$

[Example] Suppose $I_{U|C}$ for (19) = {j, t} and $I_{U|C}$ for (20) = {i, t}. Then $I_{S|T}^{i}$ for the block of terms in (24)–(28) are:

$$
\sum a _ {i j} X _ {i j t}: \{i, j, t \} - \{j, t \} = \{i \}
$$

$$
\sum b _ {j t} \colon \{j, t \} - \{j, t \} = \phi
$$

$$
\sum X _ {i j t} \colon \{i, j, t \} - \{i, t \} = \{j \}
$$

$$
\sum I _ {i t} \colon \{i, t \} - \{i, t \} = \phi
$$

$$
\sum s _ {i t} \colon \{i, t \} - \{i, t \} = \phi
$$

Thus the complete model of (18)-(21) with the selected indices is Figure 11.

On the other hand, to adopt the first approach, we can apply Theorem 2.

[Theorem 2] Unit index set of a constraint set is equal to index space of a constraint set minus union of summation index sets of the entire block of terms.

$$
I _ {U \mid C} = \left(I _ {C} - \bigcup_ {i = 1} ^ {n} I _ {S \mid T} ^ {i}\right).\tag{34}
$$

The compatibility restrictions applied to the combination of indices in objective function variables will be applied in the same fashion to the variables in the constraints. For the next step, the constraints (31)-(32) can be transformed into individual notational form in the same fashion that the objective function variables were transformed.

The dialogue necessary for index selection may utilize knowledge about the generation of meaningful index subspaces. For instance, for the “production capacity” constraint in (19), the production capacity for each product may not make sense when the facility manufactures multiple products. By the same token, the production capacity for each month is incomplete if we have not designated which products will be produced.

![](/api/attachments/Z2NPX9ZR/fulltext/images/f977e634dcecc692cccaf2b417e5d5796d2904b2d8e151d09a3bf2c4762d15d5.jpg)  
Fig. 12. Ambiguity elimination process.

![](/api/attachments/Z2NPX9ZR/fulltext/images/62002334715a407ecd676702d872c170c93f68cdd874110aaddda0ac1e50d15f.jpg)  
Fig. 13. Structure of specific linear programming model.

After having removed the meaningless index sets, UNIK-OPT can generate the following menu in Figure 12.

The above selection means that the constraint is necessary for each j and t. The constraint unit for PRODUCTION-SALES-BALANCE can be selected in the same fashion.

Once the formulation is represented in frames with the structure depicted in Figure 13, they can be syntactically transformed into notational and tabular input format.

## 9. Conclusions

We have designed a prototype of UNIK-OPT that assists in formulating optimization models using modeling knowledge and domain knowledge. The architecture of UNIK-OPT can fulfill the goal of independent management of the knowledge base and database from the optimization models. The representation scheme adopted in UNIK-OPT can be expanded to nonlinear and integer programming models and multiple objective decision making models. Real world application of UNIK-OPT is under development for a refinery plant $[30,35]$ .

## Acknowledgements

This research is supported by the Korea Ministry of Science and Technology and Yukong Co. Ltd.

## Appendix

Proof of Theorem 1

Proof. $I_{S|T}^{i} = (I_{T}^{i} - I_{U|C})$ if and only if $I_{S|T}^{i} \subset (I_{T}^{i} - I_{U|C})$ and $(I_{T}^{i} - I_{U|C}) \subset I_{S|T}^{i}$ . (i) $I_{S|T}^{i} \subset (I_{T}^{i} - I_{U|C})$ .

For every $k \in I_{S|T}^{i}$ , we shall show that $k \in (I_T^i - I_{U|C})$ . Note that $k \in (I_T^i - I_{U|C})$ implies $k \in I_T^i$ , but $k \notin I_{U|C}$ . If $I_{S|T}^i = \emptyset$ , the proof is obvious. Since there are no aliases of indices and the relation $I_{S|T}^i \subseteq I_T^i$ holds, $k \in I_{S|T}^i$ implies that $k \in I_T^i$ . Assume $k \in I_{U|C}$ . Then $k \in I_{U|C}$ together with $k \in I_{S|T}^i$ means that index $k$ is used as both an unit index of a constraint set and a summation index of the $i$ th block of terms. However, we cannot expand the $i$ th block of terms with respect to the full range of summation index $k$ while simultaneously fixing the value of unit index $k$ . This is a contradiction. Thus $k \notin I_{U|C}$ , which means that $k \in (I_T^i - I_{U|C})$ , and hence $I_{S|T}^i \subset (I_T^i - I_{U|C})$ .

$$
\left(\mathrm{ii}\right) \left(I _ {T} ^ {i} - I _ {U | C}\right) \subset I _ {\mathrm{S} | T} ^ {i}.
$$

Conversely, for every $k \in (I_T^i - I_{U|C})$ , we shall show that $k \in I_{S|T}^i$ . Again note that $k \in (I_T^i - I_{U|C})$ implies $k \in I_T^i$ , but $k \notin I_{U|C}$ . If $(I_T^i - I_{U|C}) = \emptyset$ , the proof is obvious. Assume $k \notin I_{S|T}^i$ . Then $k \notin I_{S|T}^i$ together with $k \in I_T^i$ and $k \notin I_{U|C}$ means that index $k$ is used as an index space element of the $i$ th block of terms in a constraint set, but not as a summation index of the $i$ th block of terms or as an unit index of a constraint set. However, we cannot expand the $i$ th block of terms with respect to index $k$ because the range of index $k$ is not defined. This is a contradiction. Thus $k \notin I_{S|T}^{i}$ , and hence $(I_T^i - I_{U|C}) \subset I_{S|T}^i$ .

(i) and (ii) complete the proof.

## Proof of Theorem 2

Proof. By Theorem 1, $I_{S|T}^{i} = (I_{T}^{i} - I_{U|C})$ . This relation is true for every block of terms in a constraint set. If there are n block of terms in a constraint set, then

$$
\begin{array}{l} \bigcup_ {i = 1} ^ {n} I _ {S | T} ^ {i} = \bigcup_ {i = 1} ^ {n} \left(I _ {T} ^ {i} - I _ {U | C}\right) \\ \qquad = \bigcup_ {i = 1} ^ {n} \left(I _ {T} ^ {i} \cap I _ {U | C} ^ {c}\right) \\ \qquad = \left(\bigcup_ {i = 1} ^ {n} I _ {T} ^ {i}\right) \cap I _ {U | C} ^ {c} (\text {Distributive Law}) \\ \qquad = I _ {C} \cap I _ {U | C} ^ {c} \\ \qquad = I _ {C} - I _ {U | C}, \end{array}
$$

where the union is over the entire block of terms in a constraint set. In the above set operations, we use the relation $\bigcup_{i=1}^{n}I_{T}^{i}=I_{C}$ . Since $I_{C}\supseteq I_{U|C}$ ,

$$
I _ {U \mid C} = \left(I _ {C} - \bigcup_ {i = 1} ^ {n} I _ {S \mid T} ^ {i}\right).
$$

## References

[1] H.K. Bhargava and R. Krishnan, A Formal Approach for Model Formulation in A Model Management System, Proceedings of the 23rd Hawaii International Conference on the System Sciences (1990).

[2] M. Binbasioglu, Process Based Reconstructive Approach to Model Building, 1990 ISDSS Conference Proceedings (1990) 383–403.

[3] M. Binbasioglu and M. Jarke, Domain Specific DSS Tools for Knowledge-based Model Building, Decision Support Systems 2, No. 3 (1986) 213–223.

[4] Bonner and Moore Management Science, RPMS: The Refinery and Petrochemical Modeling System – A System Description (Houston, 1979).

[5] Burroughs Corporation, Model Development Language

and Report Writer (MODELER) User's Manual (No. 1094950, Detroit, Michigan, 1980).

[6] Control Data Corporation, APEX-III Reference Manual (Version 1.2) (No. 76070000, Rev. G, Minneapolis, Minnesota, 1979).

[7] R. Fourer, Modeling Languages Versus Matrix Generators for Linear Programming. ACM Transactions on Mathematical Software 9, No. 2 (1983) 143–183.

[8] R. Fourer, D.M. Gay and B.W. Kernighan, AMPL: A Mathematical Programming Language, Computing Science Technical Report No. 133 (AT and T Bell Lab., Murray Hill, New Jersey, 1989).

[9] A.M. Geoffrion, Introduction to Structured Modeling, Management Science 33, No. 5 (1987) 547–588.

[10] A.M. Geoffrion, SML: A Model Definition Language for Structured Modeling, Working Paper No. 360 (UCLA, 1988).

[11] A.M. Geoffrion, The Formal Aspects of Structured Modeling, Operations Research 37, No. 1 (1989) 30–51.

[12] A.M. Geoffrion, Overview of the FW/SM Prototype Structured Modeling Environment, Joint National Meeting of TIMS/ORSA (Las Vegas, 1990).

[13] A.M. Geoffrion, A Taxonomy of Indexing Structures for Mathematical Programming Modeling Languages, Proceedings of the 23rd Hawaii International Conference on the System Sciences (1990) 463–473.

[14] H.J. Greenberg, Computer-Assisted Analysis for Diagnosing Infeasible or Unbounded Linear Programs, Mathematical Programming Studies 31 (1987) 21–29.

[15] H.J. Greenberg, A Natural Language Discourse Model to Explain Linear Programming Models and Solutions, Decision Support Systems 3, No. 4 (1987) 333–342.

[16] Haverly Systems Inc., Omni Linear Programming System: User and Operating Manual (1st ed., Denville, New Jersey, 1976).

[17] Haverly Systems Inc., MaGen: Reference Manual (Denville, New Jersey, 1977).

[18] S.N. Hong and M.V. Mannino, Semantics of Modeling Languages: Logic and Mathematical Modeling, 1990 IS-DSS Conference Proceedings (1990) 41–67.

[19] IBM World Trade Corporation, Matrix Generator and Report Writer (MGRW) Program Reference Manual (No. SH19-5014, New York and Paris, 1972).

[20] IBM World Trade Corporation, IBM Mathematical Programming System Extended/370 (MPSX/370) Program Reference Manual (2nd ed., No. SH19-1095-1, New York and Paris, 1976).

[21] S. Katz, L.J. Risman and M. Rodeh, A System for Constructing Linear Programming Models, IBM Systems Journal 19, No. 4 (1980) 505–520.

[22] D.A. Kendrick, Parallel Model Representations. Expert Systems with Applications 1, No. 4 (1990) 383–389.

[23] Ketron Inc., MPS III DATAFORM: User Manual (Arlington, Virginia, 1975).

[24] R. Krishnan, A Logic Modeling Language for Automated Model Construction, Decision Support Systems 6, No. 3 (1990) 123–152.

[25] R. Krishnan, PDM: A Knowledge-based Tool for Model Construction, Decision Support Systems 7, No. 3 (1991) 301–304.

[26] R. Krishnan, D.A. Kendrick and R.M. Lee, A Knowledge-based System for Production Distribution Economics, Computer Science in Economics and Management 1 (1988) 53–72.

[27] J.K. Lee, Solving Semi-Structured Problems and the Design of Decision Supporting Systems: Post-Model Analysis Approach, Unpublished doctoral dissertation (University of Pennsylvania, 1985).

[28] J.K. Lee, The Integration of Linear Programming with Rule-based System by the Post-Model Analysis Approach (on revision to appear in Management Science).

[29] J.K. Lee, Knowledge-based Systems and Optimization (Addison-Wesley Publishing Co., forthcoming).

[30] J.K. Lee, S.C. Chu, M.Y. Kim and S.H. Shim, A Knowledge-Based Formulation of Linear Programming Models Using UNIK-OPT, in: L.F. Pau et al., Eds., 2nd International Workshop on Artificial Intelligence in Economics and Management (North-Holland, 1989) 447–456.

[31] J.K. Lee and E.G. Hurst Jr., Multiple Criteria Decision Making including Qualitative Factors: The Post-Model Analysis Approach, Decision Sciences 19, No. 2 (1988) 334–352.

[32] J.K. Lee and B.S. Kang, Intelligent Production Planning System by the Post-Model Analysis Approach, in: E. Turban and P.R. Watkins, Eds., Applied Expert Systems (North-Holland, 1988) 87–106.

[33] J.K. Lee and M.Y. Kim, Case-based Learning for Knowledge-based Optimization Modeling System: UNIK-CASE, Expert Systems with Applications 6, No. 1 (1993) 87–95.

[34] J.K. Lee and H.G. Lee, Integration of Strategic Planning and Short-Term Planning: An Intelligent DSS Approach by the Post-Model Analysis Approach, Decision Support Systems 3, No. 2 (1987) 141–154.

[35] J.K. Lee, S.B. Oh, M.S. Suh, M.Y. Kim and Y.U. Song, Knowledge Network for Planning and Control of Refinery Industry: UNIK-R Project Experience, The Fourth International Conference on Expert Systems in Production and Operations Management (1990) 16–32.

[36] J.S. Lee, C.V. Jones and M. Guignard, MAPNOS: Mathematical Programming Formulation Normalization System, Expert Systems with Application 1, No. 4 (1990) 367–381.

[37] T.P. Liang, Modeling by Analogy: A Case-based Approach to Model Construction, Working Paper No. 89-1524 (University of Illinois at Urbana-Champaign, 1989).

[38] T.P. Liang and B.R. Konsynski, Modeling by Analogy: Use of Analogical Reasoning in Model Management Systems, 1990 ISDSS Conference Proceedings (1990) 405–421.

[39] P. Ma, F.H. Murphy and E.A. Stohr, A Graphics Interface for Linear Programming, Communications of the ACM 32, No. 8 (1989) 996–1012.

[40] P. Ma, F.H. Murphy and E.A. Stohr, LPSPEC: A Lan-

guage for Representing Linear Programs, Working Paper Series, GBA/#86-104 (Graduate School of Business Administration, New York University, October, 1986).

[41] A. Meeraus, An Algebraic Approach to Modeling, Journal of Economic Dynamics and Control 5, No. 1 (1983) 81-108.

[42] MIT Center for Computational Research in Economics and Management Science, DATAMAT Reference Manual (3rd ed., No. D0078, Cambridge, Massachusetts, 1975).

[43] F.H. Murphy and E.A. Stohr, An Intelligent System for Formulating Linear Programs, Decision Support Systems 2, No. 1 (1986) 39–47.

[44] F.H. Murphy, E.A. Stohr and P. Ma, Composition Rules for Building Linear Programming Models from Component Models, Management Science 38, No. 7 (1992) 948–963.

[45] S.J. Park and J.Y. Park, Structured Modeling Support System (SMSS): A Computer-aided Tool for DSS Development, APORS'88 (1988) 181.

[46] R.G. Ramirez, R.D. St. Louis, A. Philippakis and R. Eck, Overview of the ASUMMS Model Management System, Joint National Meeting of TIMS/ORSA (Las Vegas, 1990).

[47] R.L. Sanders and M.G. Smith, A Description of Bonner and Moore's GAMMA System, No. CSH-007 (Bonner and Moore Software Systems, Houston, 1976).

[48] I.S. Singh, A Support System for Optimization Modeling, Decision Support Systems 3, No. 2 (1987) 165–178.

[49] Sperry Univac Computer Systems, GAMMA 3.4 Procedures Summary (No. UP-8200, Rev. 1, St. Paul, Minnesota, 1977).

[50] E.A. Stohr, Automated Support For Formulating Linear Programs, Working Paper (Information Systems Area, Graduate School of Business Administration, New York University, October, 1987).

[51] R.C. Vellore, A. Sen and A.S. Vinze, A Case-Based Planning Approach to Model Formulation, 1990 ISDSS Conference Proceedings (1990) 353–382.

[52] J.S. Welch Jr., PAM: A Practitioner's Approach to Modeling, Management Science 33, No. 5 (1987) 610–625.

![](/api/attachments/Z2NPX9ZR/fulltext/images/1cc1140a5cdb6b54c2203c40db6bed2ed00b660c5efeee3cd74742d08a9c802d.jpg)

Jae Kyu Lee is professor in the Department of Management Information Systems at the Korea Advanced Institute of Science and Technology. He hold a B.S. from Seoul National University, an M.S. from the Korea Advanced Institute of Science and Technology, and a Ph.D. from the Wharton School, University of Pennsylvania. His research interests includes managerial application of expert systems and integration of expert

systems with optimization. He is an editorial member of several international expert systems/decision support systems related journals.

![](/api/attachments/Z2NPX9ZR/fulltext/images/aefd877c8277fdf24d1e4a29ed6d6d7f63fa0ca0cf632c91d8152a5c426685dc.jpg)  
pates in the UNIK project.

Min Yong Kim is a senior researcher in the Department of Management Information Systems at the Korea Advanced Institute of Science and Technology. He holds a B.B.A. from Seoul National University, an M.S. and a Ph.D. from the Korea Advanced Institute of Science and Technology. His research interests include decision support systems, integration of knowledge-based systems and optimization. He currently partici-
