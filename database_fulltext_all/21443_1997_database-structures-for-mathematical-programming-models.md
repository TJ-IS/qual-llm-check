---
otero_id: 21443
otero_key: "HKEV5UET"
title: "Database structures for mathematical programming models"
authors: "Robert Fourer"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00007-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Database structures for mathematical programming models

Robert Fourier \*

Department of Industrial Engineering and Management Sciences, Northwestern University, Evanston, IL 60208-3119, USA

## Abstract

In the design and use of large-scale mathematical programming systems, a substantial portion of the effort has no direct relation to the variables and constraints, but is instead concerned with the description, manipulation and display of data. Established principles of database design do not apply directly to mathematical programming, however, because there are significant differences of organization and content between the data for an optimization model and the data for a conventional database application such as payroll or order entry. The goal of this work is thus to derive and elucidate fundamental principles of database construction for the specific case of large-scale mathematical programming. Alternative formulations of a steel mill planning model, combining aspects of production and network linear programming, are presented as an example; these formulations are shown to correspond to relational and hierarchical database schemes that have contrasting strengths and weaknesses. A particular implementation of a database system for steel optimization is then introduced and discussed, and a variety of promising generalizations are surveyed. © 1997 Elsevier Science B.V.

Keywords: Database; Relational database; Hierarchical database; Mathematical programming; Linear programming; Large-scale optimization; Production planning; Steel

## 1. Introduction

The work recounted here grew out of a project to design an optimization package for steel mill planning. Because the project was supported by the American Iron and Steel Institute, it was to be based on a generic model – one that any particular steel company could specialize to its own operations, simply by supplying its own data. Users of the model would be concerned mainly with entering and maintaining their data, and with viewing the optimal production levels.

In light of the data's central role, it was decided to implement the optimization package in the context of a database management system. The user would thus enter the description of a steel mill as a collection of materials and facilities records of a prescribed structure. An associated linear program would then be automatically generated and solved, and the optimal values would be automatically left in appropriate fields. Finally, the results would be displayed as desired, by use of the database system's varied reporting options.

As the implementation of the steel optimization package has progressed, it has become clear that many of the underlying principles are of much broader applicability. Certainly, the generic linear programming model can describe other productive enterprises that transform flows of raw materials into diverse finished products, through a series of processing steps. There are equally important general principles at work, however, in the way that the database structure is related to the formulation of the linear program.

The goal of this paper is to codify some of the principles of database construction for linear programming (and for large-scale optimization in general) by use of the steel optimization model as an example. Two likely formulations of the linear program are introduced initially, and are shown to correspond to relational and hierarchical database schemes that have contrasting strengths and weaknesses. An implementation of the steel optimization package is then described, with emphasis on some of the practical issues that arise in building a database management system for a linear programming application.

## 1.1. Background

Optimization has a substantial history in the steel industry, beginning in the 1950s [16] and continuing through subsequent decades [14]. Linear programming models in particular are found in many production planning applications, such as the extensive World Bank study of the Mexican steel industry [24], the strategic planning model developed for Hoesch Corporation of Dortmund, Germany [3], and the award-winning investigations at Tata Steel in Jamshedpur, India [15,35]. The literature in this area has tended to focus on applications at particular companies, however, in contrast to the more general approach taken by the project described in this paper.

Database management has always been an important aspect of linear programming systems, as explained for example in Palmer's description of Exxon's PLATOFORM [30]. Similarities between linear programming data and relational database tables have been remarked upon by several authors, including Choobineh [9], Müller-Merbach [29] and Welch [38]. Mathematical programming systems using the so-called network database model have been investigated by Bonczek et al. [7] and by Stohr and Tanniru [36], and a design that employs aspects of the hierarchical and relational database models has been implemented in the MIMI/LP system by Chesapeake Decision Sciences [2,8,10]. More recently, an extension to the MPL modeling language [28] has allowed an explicit correspondence to be defined between data described in MPL and the relational tables of a database management system. As part of these projects, varied principles have been derived for the design of database structures in mathematical programming. The aim of this paper is to give a more formal statement of such principles, and to consider a broader variety of cases.

Several studies have considered the reverse arrangement in which linear programming features are added to a database management system. One line of research has sought to extend database query languages for this purpose; extensions to the widely-used SQL language have been proposed by Choobineh [9], by Lenard [26], and by Savage and Baker [34]. Other investigators have used unmodified database languages to define frameworks in which linear programs can be generated. This approach, applied by Pasquier et al. [31] using the dBASE II language and by Atamtürk et al. [1] using SQL, comes closest in spirit to the steel industry implementation to be described in this paper.

Numerous proposals have also been made for intermediate levels of integration between an existing database management system and an existing optimization system. These are classified and surveyed in a related report [18].

## 1.2. Outline

Section 2 below presents two formulations of our linear programming example, which differ in how they describe the indexing of model components. Sections 3 and 4 then describe relational and hierarchical database structures, respectively, that correspond to the organization of data in the two formulations. Each structure has certain advantages and disadvantages, as explained in Section 5, with respect to ease of use, data storage, and data retrieval.

The relationships between the linear programming formulations (in Section 2) and the database structures (in Sections 3 and 4) are not merely a fortuitous consequence of the application at hand. One can readily discern general rules that connect familiar algebraic characterizations of data to familiar database concepts such as records, fields, and keys. Sections 3 and 4 also codify these rules and comment on their application.

The implementation designed for the steel optimization project is described in Section 6. Particular attention is given in this section to practical issues of speed and convenience, and to the appearance and mechanics of the user interface.

Section 7 summarizes the conclusions that can be drawn directly from this work, and suggests promising extensions to address additional indexing structures, additional database types, and more complex models.

## 2. Formulations

We adopt the following general formulation that covers all linear programs (LPs) to be considered in this paper:

Maximize

subject to

$$
\begin{array}{l} \sum_ {j = 1} ^ {n} c _ {j} x _ {j} \\ l _ {i} ^ {\text {row}} \leq \sum_ {j = 1} ^ {n} a _ {i j} x _ {j} \leq u _ {i} ^ {\text {row}}, \quad i = 1, \ldots , m, \\ l _ {j} ^ {\text {col}} \leq x _ {j} \leq u _ {j} ^ {\text {col}}, \quad j = 1, \ldots , n. \end{array}
$$

It will be of conceptual and practical value to investigate database structures that are capable of representing any LP of this form, by storing all $l_{i}^{row}$ , $u_{i}^{row}$ , $c_{j}$ , $l_{j}^{col}$ and $u_{j}^{col}$ , along with all $a_{ij}$ that are nonzero.

This form is too general, however, for our prospective users to work with it directly. They need a much more specific formulation, as described below, that speaks of familiar materials and facilities, and of their limits, yields, costs and capacities.

We begin by introducing our specific model informally, using a few steelmaking concepts for examples. Then we present two formal descriptions, which differ mainly in how they define and use index sets. Sections 3 and 4 will show how these two descriptions naturally give rise to two different database structures.

## 2.1. An informal description

We consider a generic continuous-flow production process; raw materials enter, various transformations to intermediate goods are performed, and finished products leave. Profit is the total revenue from sales of the finished products, less the costs of acquiring the raw materials and making the transformations. Our problem is to run the plant at the most profitable levels of activity, in one future planning period. This kind of model is appropriate for, among other things, a quarterly or annual model of a steel mill's production.

The specification of our model begins with a list of all materials that figure in the production process, together with supply and demand data for each:

\- The cost per unit of material bought, and the minimum and maximum quantities that can be bought.

\- The revenue per unit of material sold, and the minimum and maximum quantities that can be sold.

Normally, raw materials (such as coal, ore, or limestone) can only be bought, while finished products (tempered coils, pipes) are only sold. Intermediates (pig iron, slabs, unfinished coils) can often be neither bought nor sold, but there are exceptions depending on market conditions. We can set a product's maximum bought or sold to zero to indicate that no buying or selling of the product is possible. To 'load' the facility for a specified level of production, the minimum sales amounts may be set equal to the maximum for every finished product.

For each material, the model may also optionally specify a list of conversions to other materials. Each conversion has a given yield and cost per unit (of the material being converted). Conversions often serve as a bookkeeping device. For example, tempered coils might be converted into five different products, each representing coils destined for a different market, and each with its own revenue per ton and sales limits. Some of the coils of secondary grade could also be downgraded to scrap by means of a conversion.

The major transformations of materials at a steel mill cannot be described as simple conversions. We must rather define a collection of facilities at which transformations occur. Each facility houses one or more productive activities, which use and produce materials in certain proportions. Specifically, the following information is provided for each activity at a facility:

\- The amount of each input required by a unit of activity.

\- The amount of each output produced by a unit of activity.

• The (variable) cost per unit of activity.

\- Upper and lower limits on the number of units of activity.

\- The number of units of activity that can be accommodated by one unit of the facility's overall capacity.

Naturally, there are upper and lower limits on the overall capacity of each facility. There are similar limits on a facility's total use of each input and total production of each output. Where the lower and upper limits are not critical, the lower may be set to 0 and the upper to a large, effectively infinite, value.

A common example of a facility is a rolling mill at which several finished products are made. The rolling of each product must be modeled as a separate activity, since it produces a separate output. The units of each activity are in tons (of product), while the units of the facility's capacity are in hours. Thus the model specifies each activity's capacity use in tons per hour. In effect, the activities are competing for the limited capacity of the facility; the optimization automatically allocates capacity to best account for factors such as yield, cost of production, and potential for revenue from sales.

A different example occurs at a basic oxygen furnace, where all activities produce liquid steel. Here activities differ in the amounts of the various inputs that they use to produce a ton of steel; each represents, in effect, a different recipe for steel production. Both the units of each activity and the units of the furnace's capacity are measured in tons of steel produced, so the capacity use coefficient is simply 1. (The specification of discrete recipes can be viewed as approximating the solution of a more general blending problem at the furnace.)

We can characterize this model as a kind of hybrid between production and network flow, as depicted in Fig. 1. The circles in the figure represent material balances, and the rectangles represent facilities. Each circle may have an inbound arc for purchases, or an outbound arc for sales. An arc from a circle to a rectangle denotes input of a material to a facility, and an arc from a rectangle to a circle denotes output of a material from a facility. An arc from a circle to another circle shows a conversion of one material to another.

![](/api/attachments/HKEV5UET/fulltext/images/6fb485bc206764b8f75fdb79805dab1a0363fa240d2ad97459e9a181227179d9.jpg)  
Fig. 1. Structure of a small instance of the multi-facility production problem. Raw materials (1, 2 and 3) are transformed by facility A to an intermediate (4), which is then transformed by facilities B and C to finished product of primary and secondary grades (5 and 6) as well as scrap (7) that can be sold or recycled. Secondary product may also be scrapped if there is insufficient market for it; this option, modeled as a conversion, is represented by the arrow from (6) to (7).

It is convenient to imagine that the circles toward the top of the diagram correspond to raw materials, while those at the bottom correspond to finished products. Thus there is a general flow of materials from top to bottom. Exceptions to this general flow may occur, however, as a result of by-products that can be re-used in production. The most common example is steel scrap, which occurs as an output of every rolling and finishing facility, and which (if not sold) may be recycled as an input to steelmaking furnaces. Natural gas from coke ovens and blast furnaces can also be recycled, in a more complex scheme that produces heat or electricity.

## 2.2. First formulation

Our first algebraic description of the above problem is characterized by the use of ordered 'tuples' of indices to describe productive possibilities. It is presented in full in Appendix A; we comment here on some of its more important conventions and features.

The model is built upon two fundamental sets of objects: a set M of materials, and a set F of facilities. Certain data values, such as the purchase limits for each material and the capacity of each facility, are indexed directly over these sets. However, much of the data is indexed over sets of ordered pairs and triples, whose components are taken from M and F:

$$
\begin{array}{l l l} \mathcal {M} ^ {\text {conv}} & \subseteq \mathcal {M} \times \mathcal {M} & \text {conversions;} \\ \mathcal {F} ^ {\text {in}} & \subseteq \mathcal {F} \times \mathcal {M} & \text {facility inputs;} \\ \mathcal {F} ^ {\text {out}} & \subseteq \mathcal {F} \times \mathcal {M} & \text {facility outputs;} \\ \mathcal {F} ^ {\text {act}} & \subseteq \mathcal {F} \times ? & \text {facility activities;} \\ \mathcal {A} ^ {\text {in}} & \subseteq \mathcal {F} \times \mathcal {M} \times ? & \text {activity inputs;} \\ \mathcal {A} ^ {\text {out}} & \subseteq \mathcal {F} \times \mathcal {M} \times ? & \text {activity outputs.} \end{array}
$$

The construction and use of these sets are readily understood from the descriptions in Appendix A. However, the latter three have special characteristics that require further comment.

Consider the set $\mathcal{F}^{\mathrm{act}}$ . As defined in Appendix A, $(i,k)\in \mathcal{F}^{\mathrm{act}}$ means that $k$ is an activity available at facility $i$ . Thus we can reasonably regard $\mathcal{F}^{\mathrm{act}}$ as a subset of $\mathcal{F}\times \mathcal{A}$ , where $\mathcal{A}$ is a previously unmentioned set of activities. Indeed, all of the three occurrences of ? above would properly be references to $\mathcal{A}$ .

We do not refer explicitly to the set A in our formulation, however, because activities do not play a role in the model apart from their association with facilities. There are no model components indexed directly over activities. Even if activities at different facilities were to have the same name, they would not necessarily be the same activity, and the linear program would be unaffected if the names of any of them were changed. These distinctions will eventually be seen to carry over to the database structure.

In the case of $A^{in}$ (and analogously for $A^{out}$ ), the model defines the domain of the triples more restrictively than the summary above:

$$
\mathscr {A} ^ {\text { in }} \subseteq \left\{\left(i, j, k\right): (i, j) \in \mathscr {F} ^ {\text { in }} \text {   and   } (i, k) \in \mathscr {F} ^ {\text { act }} \right\}.
$$

The set on the right is just $\mathcal{F}^{\mathrm{in}}\bowtie\mathcal{F}^{\mathrm{act}}$ , the natural join of $\mathcal{F}^{\mathrm{in}}$ and $\mathcal{F}^{\mathrm{act}}$ . We restrict $\mathcal{A}^{\mathrm{in}}$ to this set because, for material $j$ to be an input to activity $k$ at facility $i$ , the material must be an allowable input at the facility, or $(i,j)\in\mathcal{F}^{\mathrm{in}}$ , and the activity must exist at the facility, or $(i,k)\in\mathcal{F}^{\mathrm{act}}$ .

The only data values indexed over $A^{in}$ are the technological coefficients, $a_{ijk}^{in}$ . We could thus dispense with $A^{in}$ entirely by indexing $a_{ijk}^{in}$ directly over $F^{in} \bowtie F^{act}$ , and by letting $a_{ijk}^{in}$ be zero if activity k does not actually use input j. However, we would then lose a certain consistency in the data definition. In our current formulation, collections of data values are indexed either over a single fundamental set (M or F) or over a subset of a cartesian product of fundamental sets (such as $F \times M$ ). This convention, which extends to the variables and constraints as well, is not always followed in linear programming formulations, but we will see that it is valuable to the design of an associated relational database structure.

## 2.3. Second formulation

Our second algebraic description is characterized by a different way of representing the index sets, in which the ordered pairs and triples are replaced by indexed collections of subsets. As seen in Appendix B, where the full formulation is presented, this change has immediate implications for how the model is expressed, even though the model represents the same class of linear programs as before.

The six collections of subsets are written as follows in Appendix B:

$$
\begin{array}{l l l} \mathcal {M} _ {j} ^ {\text {conv}} & \subseteq \mathcal {M} & \text {conversions from material j ;} \\ \mathcal {F} _ {i} ^ {\text {in}} & \subseteq \mathcal {M} & \text {inputs at facility i ;} \\ \mathcal {F} _ {i} ^ {\text {out}} & \subseteq \mathcal {M} & \text {outputs from facility i ;} \\ \mathcal {F} _ {i} ^ {\text {act}} & \subseteq ? & \text {activities at facility i ;} \\ \mathcal {A} _ {i k} ^ {\text {in}} & \subseteq \mathcal {F} _ {i} ^ {\text {in}} & \text {inputs to activity k at facility i ;} \\ \mathcal {A} _ {i k} ^ {\text {out}} & \subseteq \mathcal {F} _ {i} ^ {\text {out}} & \text {outputs from activity k at facility i .} \end{array}
$$

This change does not affect the model's names for the data values; both formulations have $u_{ij}^{\mathrm{in}}, a_{ijk}^{\mathrm{out}}$ , and so forth. The difference is in how the models describe the indexing of this data. For example, the first formulation specifies a value $u_{ij}^{\mathrm{in}}$ for each $(i,j) \in \mathcal{F}^{\mathrm{in}}$ , while the second specifies a $u_{ij}^{\mathrm{in}}$ for each $i \in \mathcal{F}$ and $j \in \mathcal{F}_i^{\mathrm{in}}$ . Sections 3 and 4 will show how these different ways of describing the data can correspond to different ways of organizing it in a database.

The ? above refers to the same phantom ‘set of activities’ as in the first formulation. There is no question as to the domains of $A_{ik}^{in}$ and $A_{ik}^{out}$ , however. For example, the inputs available to activity k at facility i are a subset of the inputs available to all activities at facility i. Hence $A_{ik}^{in} \subseteq F_{i}^{in} \subseteq M$ ; each $A_{ik}^{in}$ is actually a sub-subset. The values $a_{ijk}^{in}$ are correspondingly defined for all $i \in F$ , $k \in F_{i}^{act}$ and $j \in A_{ik}^{in}$ .

## 3. Relational structures

A subset of a cartesian product of sets (such as $F \times M$ ) is a relation in a mathematical sense. Thus it is not surprising that data indexed over pairs or triples from cartesian products, as in our first formulation, has a natural representation in relational database structures.

This section develops and comments upon likely relational schemes for our models. To establish principles and terminology, we first focus on the simple general linear programming model that was introduced at the beginning of Section 2. We observe how the nonzero coefficients of the model can be viewed as being indexed over ordered pairs, and propose a collection of relational tables appropriate to the structure of the data. We finally generalize from this example to a series of explicit rules for deriving relational database schemes from linear programming models, and explore the application of these rules to the considerably more complicated case of the multi-facility production model.

## 3.1. An ordered-pair view of the general model

We can think of the shape of the general linear program as being determined by two sets:

$\mathcal{I} = \{1,\dots ,m\}$ is the set of constraints (or coefficient rows);

$\mathcal{J} = \{1, \ldots, n\}$ is the set of variables (or coefficient columns).

Two ‘right-hand side’ values are associated with each constraint:

$l_{i}^{\mathrm{row}} =$ the lower limit on constraint $i$ , for each $i \in \mathcal{I}$ ;

$u_{i}^{\text{row}} = \text{the upper limit on constraint } i, \text{ for each } i \in \mathcal{I}.$

Each variable has a ‘profit’ and two bounds, as well as an activity level:

$c_{j}$ = the profit (if positive) or cost (if negative) per unit of variable $j$ , for each $j \in \mathcal{J}$ ;

$x_{j} =$ the activity level of variable $j$ , for each $j\in \mathcal{J}$ ;

$l_{j}^{\mathrm{col}} =$ the lower limit on variable $j$ , for each $j \in \mathcal{J}$ ; $u_{j}^{\mathrm{col}} =$ the upper limit on variable $j$ , for each $j \in \mathcal{J}$ .

Finally, the nonzero coefficients are indexed over a set of constraint-variable pairs:

$\mathcal{C} \subseteq \mathcal{I} \times \mathcal{J}$ is the set of coefficient nonzeroes:

$(i,j)\in \mathcal{C}$ means that variable $j$ is used in constraint $i$ ;

$a_{ij} =$ the coefficient of variable $j$ in constraint $i$ , for each $(i,j)\in \mathcal{C}$ .

This approach to indexing the coefficients makes sense for most large linear programs, including those that derive from our production model, because each variable figures in just a few of the many constraints.

The set C of pairs has a dimension of 2, whereas the sets J and J of simple members have dimension 1. All of a set's members have a number of components equal to the dimension, and no two members are the same; these conventions, while usually taken for granted in a mathematical context, must be made explicit to ensure that the analogous database is well defined.

With minor modifications, our general formulation of the linear program can accommodate the above view of the data:

$$
\begin{array}{l l} \text { Maximize } & \sum_ {j   \in   \mathcal {J}} c _ {j} x _ {j} \\ \text { subject   to } & l _ {i} ^ {\text { row }} \leq \sum_ {(i, j)   \in   \mathcal {C}} a _ {i j} x _ {j} \leq u _ {i} ^ {\text { row }}, \quad \text { for   all   } i \in \mathcal {I}, \\ & l _ {j} ^ {\text { col }} \leq x _ {j} \leq u _ {j} ^ {\text { col }}, \quad \text { for   all   } j \in \mathcal {J}. \end{array}
$$

The summation denoted by $\sum_{(i,j)\in\mathscr{C}}a_{ij}x_j$ is taken for each fixed $i\in\mathscr{I}$ ; it is interpreted as the sum over all j such that $(i,j)$ , for the given i, is a member of C. This is the same convention that is used in Appendix A for the production model.

## 3.2. A relational database for the general model

A relational database is a collection of files. For our linear program, the simplest file is the one that identifies the constraints and their associated limits. This file contains a record for each constraint $i \in J$ . Every record has three fields:

row\_name, a unique identifier for the constraint;
row\_min, the constraint's lower limit;
row\_max, the constraint's upper limit.

The row\_name field is the database analogue of the subscript i; it is designated the key for this file, which must be different for each constraint record. The values stored in row\_min and row\_max naturally correspond to $l_{i}^{row}$ and $u_{i}^{row}$ in the algebraic formulation.

The structure of the constraints file would be represented in conventional notation as the relation CONSTRAINTS (row\_name, row\_min, row\_max). The file's content would be depicted by exhibiting its records and fields as the rows and columns, respectively, of a relational table:

<table><tr><td>row_name</td><td>row_min</td><td>row_max</td></tr><tr><td>1</td><td>0.0e+00</td><td>1.0e+30</td></tr><tr><td>2</td><td>3.0e+01</td><td>3.0e+01</td></tr><tr><td>3</td><td>4.5e+02</td><td>4.8e+02</td></tr><tr><td>4</td><td>-1.0e+30</td><td>0.0e+00</td></tr><tr><td>5</td><td>-1.0e+30</td><td>1.0e+30</td></tr></table>

We adopt the terminology of record and field in this paper, however, to avoid confusion with the customary use of row and column in linear programming, as synonyms for constraint and variable. We also find it convenient to present the structure of the constraint file graphically, by means of the following concise diagram:

<table><tr><td>CONSTRAINTS</td></tr><tr><td>row_name</td></tr><tr><td>row_min</td></tr><tr><td>row_max</td></tr></table>

The TITLE of the file is at top, followed by the field names, with the key in italics. This kind of diagram will be seen to extend conveniently to depict a variety of relational and hierarchical structures.

The variables file for the general model is similarly presented as:

<table><tr><td>VARIABLES</td></tr><tr><td>col_name</td></tr><tr><td>col_profit</td></tr><tr><td>col_min</td></tr><tr><td>col_optimal</td></tr><tr><td>col_max</td></tr></table>

Here col\_name is the variable's unique identifier, and the key for the file. The following four fields store the values called $c_{j}$ , $l_{j}^{col}$ , $x_{j}$ , and $u_{j}^{col}$ in the mathematical formulation. Strictly speaking, the field col\_optimal is superfluous, since it holds the values of variables $x_{j}$ rather than any data required to describe the linear program. However, for practical purposes it is highly desirable to be able to store the solution values in the same files as the data. For the same reason, we could have included a field in the constraints file for the dual values.

It remains to define a file to hold the nonzero coefficients. Its structure can be diagrammed as follows:

![](/api/attachments/HKEV5UET/fulltext/images/7d84b2ed083770186fa8bf59ae206f2077dcf0fd4460019224a47ffb33e40752.jpg)

Each record's coeff\_value field holds the nonzero coefficient of the variable specified by the coeff\_col field, in the constraint specified by the coeff\_row field. The pair (coeff\_row, coeff\_col) is the key, since every coefficient corresponds to a different combination of constraint and variable.

Two essential requirements remain unstated in the above diagram of the coefficients file: that each coeff\_row entry must match a key (row\_name) entry in the CONSTRAINTS file, and that each co-eff\_col entry must match a key (col\_name) entry in the VARIABLES file. In the terminology of relational databases, coeff\_row and coeff\_col are foreign keys of the COEFFICIENTS relation.

Following Date [12], we use an arrow in our diagram to identify foreign key references:

<table><tr><td>COEFFICIENTS</td></tr><tr><td>coeff_row → CONSTRAINTS</td></tr><tr><td>coeff_col → VARIABLES</td></tr><tr><td>coeff_value</td></tr></table>

Each → represents a many-to-one relationship. For example, since there may be many nonzero coefficients in one constraint, there may be many COEFFICIENTS records that have the same constraint identifier in their coeff\_row field. But each constraint identifier may appear only once in the row\_name field of the CONSTRAINTS file. (Because the many-to-one relationship is not, strictly speaking, with the CONSTRAINTS file but rather with the row\_name field in that file, we could be more precise by saying something like coeff\_row → CONSTRAINTS.row\_name; indeed, such an expression might be forced on us if certain relations admitted more than one key. Since in this paper the relationship is always with the unique key field of a file, however, we omit the field designation to keep the notation concise.)

## 3.3. Principles of relational structure

In even the simple example above, we can see many principles for deriving a relational database structure from a linear programming formulation. Most fundamentally, there is a connection between sets (such as $\mathcal{I}$ , $\mathcal{J}$ or $\mathcal{C}$ ) and files:

\- Rule R1 (files). For each set $\mathcal{S}$ in the model, there is a corresponding file in the database.

To avoid having to say ‘the file corresponding to S’ again and again, we henceforth refer to such a file as the ‘S-file’.

A set's dimension, and its use in indexing other model components (such as $l_{i}^{row}$ , $x_{j}$ or $a_{ij}$ ), determine the fields of the corresponding file:

\- Rule R2 (key fields). The $\mathcal{S}$ -file has a number of key fields equal to the dimension of $\mathcal{S}$ .

\- Rule R3 (data fields). The $\mathcal{S}$ -file has an additional data field for each model entity indexed over $\mathcal{S}$ .

Because a set's members are distinct and all have the same dimension, R2 always specifies a key that is valid in relational database terms.

The above rules determine the basic structure of relational files. We also make a connection between the membership of a set and the content of a file:

\- Rule R4 (records). The $\mathcal{S}$ -file has a record corresponding to each member of $\mathcal{S}$ .

This means that, for example, our VARIABLES file contains a record for each variable in the model. For the variable whose identifier is j, the fields of the associated record contain j together with the numerical values $c_{j}$ , $l_{j}^{col}$ , $x_{j}$ , and $u_{j}^{col}$ . Whereas in the algebraic formulation these quantities were indexed independently over J – the phrase ‘for each $j \in J$ ’ appears four separate times – in the database scheme it is most natural to group all similarly indexed entities together.

A final rule associates containment restrictions in the model with many-to-one relationships in the database:

\- Rule R5 (many-to-one relationships). For each containment restriction of the form $(\ldots, i_d, \ldots) \in \mathcal{S} \Rightarrow i_d \in \mathcal{R}$ , the $d$ th key in the $\mathcal{S}$ -file has a many-to-one relationship to the $\mathcal{R}$ -file.

In our example, $\mathcal{C} \subseteq \mathcal{I} \times \mathcal{J}$ embodies two containment restrictions: $(i,j) \in \mathcal{C} \Rightarrow i \in \mathcal{I}$ and $(i,j) \in \mathcal{C} \Rightarrow j \in \mathcal{J}$ . Thus many-to-one relationships are defined in the database from the first key of the $\mathcal{C}$ -file to the $\mathcal{I}$ -file (coeff\_row $\rightarrow$ CONSTRAINTS), and from the second key of the $\mathcal{C}$ -file to the $\mathcal{J}$ -file (coeff\_col $\rightarrow$ VARIABLES).

## 3.4. A relational database for the production model

We now examine how the above rules can give a database scheme for the multi-facility production model set forth in Appendix A. In the process we point out a situation in which a generalization to R5 might be desirable.

The production model explicitly defines two 1-dimensional sets. First is the set M of materials, over which are indexed $l_j^{\text{buy}}$ , $x_j^{\text{buy}}$ , $u_j^{\text{buy}}$ , $c_j^{\text{buy}}$ and $l_j^{\text{sell}}$ , $x_j^{\text{sell}}$ , $u_j^{\text{sell}}$ , $c_j^{\text{sell}}$ . The resulting file is:

```txt
MATERIALS
mat_name
buy_min
buy_opt
buy_max
buy_cost
sell_min
sell_opt
sell_max
sell_cost
```

Second is the set F of facilities, which indexes just $l_{i}^{cap}$ and $u_{i}^{cap}$ . It gives rise to the following file:

```txt
FACILITIES
fac_name
cap_min
cap_max
```

All of the others are subsets of pairs or triples.

The 2-dimensional sets $\mathcal{F}^{\mathrm{in}}\subseteq\mathcal{F}\times\mathcal{M}$ and $\mathcal{F}^{\mathrm{out}}\subseteq\mathcal{F}\times\mathcal{M}$ are directly analogous to $\mathcal{C}$ above. The resulting files are:

```txt
FACILITY_INPUTS
in_fac → FACILITIES
in_mat → MATERIALS
in_min
in_opt
in_max

FACILITY_OUTPUTS
out_fac → FACILITIES
out_mat → MATERIALS
out_min
out_opt
out_max
```

The key pair (in\_fac, in\_mat) uniquely defines a facility input, and the remaining three fields correspond to what are called $l_{ij}^{in}$ , $x_{ij}^{in}$ , and $u_{ij}^{in}$ in Appendix A. The situation is entirely analogous for facility outputs.

The model's other two 2-dimensional sets give rise to files that are only a bit different. The set $\mathcal{M}^{\mathrm{conv}} \subseteq \mathcal{M} \times \mathcal{M}$ yields two key fields that have many-to-one relationships to the same materials field:

```txt
MATERIAL_CONVERSIONS
from_mat → MATERIALS
to_mat → MATERIALS
conv_yield
conv_cost
conv_opt
```

The set $\mathcal{F}^{\mathrm{act}}$ has only one many-to-one relationship:

<table><tr><td>ACTIVITIES</td></tr><tr><td>act_fac → FACILITIES</td></tr><tr><td>act_name</td></tr><tr><td>act_min</td></tr><tr><td>act_opt</td></tr><tr><td>act_max</td></tr><tr><td>act_cost</td></tr><tr><td>act_cap_rate</td></tr></table>

The lack of a relationship for act\_name is a direct consequence of the absence of an explicit set A of single activities, which was discussed in Section 2. Notice that the formulation in Appendix A does not specify a containment restriction of the form $F^{act} \subseteq F \times A$ , which (from rule R5) would imply two many-to-one relationships as previously explained. Instead the formulation states only $\mathcal{F}^{\mathrm{act}} \subseteq \{(i,k): i \in \mathcal{F}\}$ , which embodies only the one restriction that $(i,k) \in \mathcal{F}^{\mathrm{act}} \Rightarrow i \in \mathcal{F}$ .

It remains to consider the two 3-dimensional sets. Each member of $A^{in}$ is a triple $(i,j,k)$ , where i is a facility, j is a material, and k is an activity; and each member indexes one data value, $a_{ijk}^{in}$ . Thus, by rules R2 and R3, the associated file has three key fields and a data field, as follows:

```txt
ACTIVITY_INPUTS
act_in_fac → FACILITIES
act_in_mat → MATERIALS
act_in
act_in_rate
```

The two many-to-one relationships in this scheme would be implied from rule R5 by $\mathcal{A}^{\mathrm{in}}\subseteq\{(i,j,k):i\in\mathcal{F}\text{ and }j\in\mathcal{M}\}$ . As discussed in Section 2, however, the model actually incorporates the stronger condition that $\mathcal{A}^{\mathrm{in}}\subseteq\{(i,j,k):(i,j)\in\mathcal{F}^{\mathrm{in}}\text{ and }(i,k)\in\mathcal{F}^{\mathrm{act}}\}$ , or equivalently $(i,j,k)\in\mathcal{A}^{\mathrm{in}}\Rightarrow(i,j)\in\mathcal{F}^{\mathrm{in}}$ and $(i,j,k)\in\mathcal{A}^{\mathrm{in}}\Rightarrow(i,k)\in\mathcal{F}^{\mathrm{act}}$ . Because the condition to the right of $\Rightarrow$ involves a 2-dimensional rather than a 1-dimensional set, these restrictions go beyond the situations covered by R5; they might be indicated in our relational database notation by

```txt
(act_in_fac, act_in_mat)
→ FACILITY_INPUTS,
(act_in_fac,
act_in) → ACTIVITIES.
```

Restrictions of these kinds can be enforced by relational database systems, but not so readily as the simpler many-to-one relationships that we have specified in our rules. The situation for $A^{out}$ is exactly analogous; one need only substitute ‘out’ for all occurrences of ‘in’ above.

The completed database scheme, consisting of eight relational tables, can be used to support a broad variety of queries. We defer further discussion, however, to the comparison in Section 5 with the alternative hierarchical structure.

## 4. Hierarchical structures

We now seek to, in effect, repeat the previous section's development, but working from the formulation in Appendix B rather than Appendix A. The result is a hierarchical data structure that will be seen, in the sequel, to have notable advantages as well as disadvantages.

Use of the term ‘hierarchical’ in this context is suggested by Date ([12], Section 26.5); the same kind of structure is also often called ‘nested relational’ or ‘non-first normal form’. Whereas the fields of a relational database record must contain single data items such as names or numbers, some fields in a hierarchical database file may themselves be structured as files. These subfiles (or nested relations) nicely capture the intent of the indexed subsets, such as $M_{j}^{conv}$ and $A_{ik}^{in}$ , that appear the formulation of Appendix B.

The organization of this section parallels that of the previous one. We first rewrite the simple linear programming model (from the beginning of Section 2) so that the nonzero coefficients are specified by use of an indexed collection of subsets, and then show how the coefficient values are naturally represented within a hierarchical database structure. Finally, we generalize to a series of explicit rules for deriving hierarchical database schemes from linear programming models, and apply these rules to the case of the multi-facility production model.

## 4.1. An indexed-subset view of the general model

Just as in the previous section, we imagine the shape of the general linear program as being determined a set J of constraints and a set J of variables, which index $l_{i}^{row}$ , $u_{i}^{row}$ and $c_{j}$ , $x_{j}$ , $l_{j}^{col}$ , $u_{j}^{col}$ respectively. The difference lies in the description of the coefficients.

Suppose that we define, for each $j$ , a subset of $\mathcal{I}$ to specify which constraints use $x_{j}$ :

$\mathcal{C}_i \subseteq \mathcal{I}$ is a subset of column nonzeroes:

$i \in \dot{\mathcal{C}}_j$ means that variable $j$ is used in constraint $i$ .

Then the nonzero coefficient values are described as follows:

$a_{ij} =$ the coefficient of variable $j$ in constraint $i$ , for each $j \in \mathcal{J}$ and $i \in \mathcal{C}_j$

These are the same coefficients as in the previous section; all that has changed is the way that their indexing is presented.

With insignificant modifications, our general formulation of the linear program can accommodate this view as well:

$$
\begin{array}{l l} \text {Maximize} & \sum_ {j \in \mathcal {J}} c _ {j} x _ {j} \\ \text {subject to} & l _ {i} ^ {\text {row}} \leq \sum_ {j \in \mathcal {J}: i \in \mathcal {C} _ {j}} a _ {i j} x _ {j} \leq u _ {i} ^ {\text {row}}, \quad \text {for all} i \in \mathcal {I}, \\ & l _ {j} ^ {\text {col}} \leq x _ {j} \leq u _ {j} ^ {\text {col}}, \quad \text {for all} j \in \mathcal {J}. \end{array}
$$

The sum over $\{j\in\mathcal{J}:i\in\mathcal{C}_{j}\}$ does seem rather awkward, however. Since there is one of these sums for each constraint, it might be preferable to define a subset for each $i\in\mathcal{I}$ (rather than for each $j\in\mathcal{J}$ ):

$\mathcal{C}_i \subseteq \mathcal{J}$ is a subset of row nonzeroes:

$j \in C_{i}$ means that variable j is used in constraint i;

$a_{ij} =$ the coefficient of variable $j$ in constraint $i$ , for each $i \in \mathcal{I}$ and $j \in \mathcal{C}_i$ .

Then the formulation simplifies to the following:

$$
\begin{array}{l l} \text {Maximize} & \sum_ {j \in \mathcal {J}} c _ {j} x _ {j} \\ \text {subject to} & l _ {i} ^ {\text {row}} \leq \sum_ {j \in \mathcal {C} _ {i}} a _ {i j} x _ {j} \leq u _ {i} ^ {\text {row}}, \quad \text {for all} i \in \mathcal {I}, \\ & l _ {j} ^ {\text {col}} \leq x _ {j} \leq u _ {j} ^ {\text {col}}, \quad \text {for all} j \in \mathcal {J}. \end{array}
$$

Of course, there may be other concerns than the convenience of the algebraic formulation. We will later observe, for example, that the subsets $C_{j}$ are preferred for generating the ‘column-wise’ data structures required by linear programming algorithms.

## 4.2. A hierarchical database for the general model

With respect to the unindexed 1-dimensional sets, a hierarchically structured database looks the same as a relational one. Thus we begin with the following two files from Section 3:

![](/api/attachments/HKEV5UET/fulltext/images/e435cdc9aa389dcf5e2f47e55a19211aff7d466c043386658553944747587a05.jpg)

Consider now one of the sets $C_{j}$ , for a particular j. $C_{j}$ is itself a 1-dimensional set, whose members are restricted to lie in S; and for each $i \in C_{j}$ , there is a coefficient value. Thus we can imagine that $C_{j}$ gives rise to a relational file as follows:

![](/api/attachments/HKEV5UET/fulltext/images/21604e20833ebec09b75978c0c3539fc07add421ded9f36f677cb755bbd17ef9.jpg)

There is one of these files for each variable, just as there are col\_name, col\_profit, col\_min, col\_optimal and col\_max fields for each variable. Thus, in the hierarchical database scheme, a COEFFICIENTS file is incorporated as a subfile of the VARIABLES file. We depict this situation as follows:

![](/api/attachments/HKEV5UET/fulltext/images/e722de4029d9ca51f33b0f7e77645d93312726a07cc97562e5c02a130fee30f0.jpg)

The user of this structure can regard COEFFICIENTS as just another field of the VARIABLES file. Rather than containing a single value like other fields, however, this field is itself an entire relational subfile of values. This subfile has its own collection of records, each containing a coeff\_row field and a coeff\_value field.

When a database is structured in this way, all of the information about a variable, including a list of its nonzero coefficients, can be retrieved from a single record of the VARIABLES file. On the other hand, there is no obvious way to retrieve all nonzero coefficients in a single constraint. For such a retrieval to be equally easy, a different subfile, analogous to the set $C_{i}$ , would have to be added instead to the CONSTRAINTS file:

![](/api/attachments/HKEV5UET/fulltext/images/25aab954ca7468951e2bd572a034eca0790b396f615097e66ef516d513d9ef04.jpg)

Just as the sets $C_{i}$ and $C_{j}$ tend to be convenient for different purposes, the subfiles of the CONSTRAINTS and VARIABLES files are useful for viewing the database in different ways. This characteristic represents both an advantage and a disadvantage for the hierarchical structure, but we defer further discussion to the comparison with the relational structure in Section 5.

## 4.3. Principles of hierarchical structure

In the hierarchical as in the relational case, our simple example suggests a number of principles for deriving a database structure from a linear programming formulation. Individual sets (such as S or J) not indexed over other sets in the model have the same connection to files as before:

\- Rule H1a (files). For each unindexed set $\mathcal{S}$ in the model, there is a corresponding file in the database.

A companion rule makes the analogous connection between indexed collections of sets (such as $C_{j}$ or $C_{i}$ ) and subfiles:

\- Rule H1b (subfiles). For each collection of sets $\mathcal{T}_s$ indexed over $s \in \mathcal{S}$ , the $\mathcal{S}$ -file has a subfile corresponding to the collection $\mathcal{T}_s$ .

This subfile rule has a straightforward extension, as we will see in the discussion of the production model below, to the case of 'sub-subfiles' $\mathcal{U}_{st}$ indexed over $t \in \mathcal{T}_{s}$ . (As in Section 3, we use the term ‘S-file’ to stand for ‘the file corresponding to S’; we use the term ‘T\_s-subfile’ analogously.)

Every file or subfile has a key field, and a data field for each entity indexed over the underlying set:

\- Rule H2 (key fields). Each file or subfile has one key field.

\- Rule H3 (data fields): The $\mathcal{S}$ -file (or $\mathcal{T}_s$ -subfile) has an additional data field for each model entity indexed over $\mathcal{S}$ (or $\mathcal{T}_s$ ).

Considering our example, how do we know whether the entity $a_{ij}$ , $j \in J$ , $i \in C_j$ is indexed over J or over $C_j$ ? We can conclude that it is indexed over $C_j$ , because there is exactly one piece of data $a_{ij}$ for each $i \in C_j$ ; it cannot be indexed over J, on the other hand, because there are many numbers $a_{ij}$ for each $j \in J$ .

The connection between the membership of a set and the content of a file is also much the same as before:

\- Rule H4 (records). The $\mathcal{S}$ -file (or $\mathcal{T}_s$ -subfile) has a record corresponding to each member of $\mathcal{S}$ (or $\mathcal{T}_s$ ).

Thus our VARIABLES file contains a record for each variable in the model, just as in the relational case. For the variable whose identifier is j, however, the associated record comprises not only the fields that contain j together with numerical values $c_{j}$ , $l_{j}^{col}$ , $x_{j}$ and $u_{j}^{col}$ , but also a COEFFICIENTS subfile for variable j. For each nonzero coefficient of variable j there is a record in this subfile whose fields contain i and $a_{ij}$ .

It remains to prescribe the handling of containment restrictions in a hierarchical database:

\- Rule H5 (many-to-one relationships): For each containment restriction of the form $j \in \mathcal{T}_s \Rightarrow j \in \mathcal{R}$ , the key record in the $\mathcal{T}_s$ -subfile has a many-to-one relationship to the $\mathcal{R}$ -file.

In the case of the expression $C_{j} \subseteq I$ from our example, the containment restriction is $i \in C_{j} \Rightarrow i \in I$ . Thus there is a many-to-one relationship from the key of the $\mathcal{C}_j$ -subfile to the $\mathcal{I}$ -file, represented by coeff\_row $\rightarrow$ CONSTRAINTS in our database diagram.

We have made no mention of multi-dimensional sets in this development, to emphasize that relationships such as $j \in J$ , $i \in C_j \subseteq J$ , using indexed collections of 1-dimensional sets, can take the place of expressions such as $(i,j) \in \mathcal{C} \subseteq \mathcal{I} \times \mathcal{J}$ using a 2-dimensional set. The rules R1–R5 and H1–H5 are in fact compatible, however, and may be used together to provide a richer variety of indexing arrangements. For example, these rules can accommodate a collection of sets $T_{qr}$ indexed over $(q,r) \in \mathcal{S} \subseteq \mathcal{Q} \times \mathcal{R}$ , or a collection of 2-dimensional sets $T_s \subseteq Q \times R$ indexed over $s \in S$ .

## 4.4. A hierarchical database for the production model

We conclude by showing how the above rules determine a hierarchical data scheme for the version of Appendix B of the multi-facility production model.

The set M gives rise, by rule H1a, to a file that is like our previous example of the VARIABLES file. The members $j \in M$ index not only the values $l_{j}^{buy}$ , $x_{j}^{buy}$ , $u_{j}^{buy}$ , $c_{j}^{buy}$ and $l_{j}^{sell}$ , $x_{j}^{sell}$ , $u_{j}^{sell}$ , $c_{j}^{sell}$ , but also the subsets $M_{j}^{conv}$ . Thus rules H1b, H2 and H3 specify that the corresponding MATERIALS file must have a key field and eight data fields, plus a subfile. Since for each $j' \in M_{j}^{conv}$ there are further values $a_{jj'}^{conv}$ , $c_{jj'}^{conv}$ and $x_{jj'}^{conv}$ , the subfile must by the same rules have a key field and three data fields. We thus arrive at a scheme that can be diagrammed as follows:

![](/api/attachments/HKEV5UET/fulltext/images/7f302ebe8b74ef637fb626afb2afff706fbdd3d530978e4d962141a62ed25df4.jpg)

The notation to\_mat → MATERIALS indicates that the target of each conversion must itself be a material in the database. This entry corresponds by rule M5 to the containment restriction $j' \in \mathcal{M}_j^{\mathrm{conv}} \Rightarrow j' \in \mathcal{M}$ , which is equivalent to the statement $\mathcal{M}_j^{\mathrm{conv}} \subseteq \mathcal{M}$ in the model's algebraic formulation.

Some studies of hierarchical database structures [33] have found it convenient to assume that every subfile contains at least one record. In a typical multi-facility planning application, however, only a few of the materials are subject to conversions; that is to say, $M_{j}^{conv}$ is the empty set for many of the materials j. For this situation to be properly represented in the database, it is necessary that the corresponding records in the MATERIALS file be allowed to have ‘empty’ CONVERSIONS subfiles.

We can apply analogous reasoning to start building a hierarchical scheme for facilities. The members $i \in F$ index the values $l_{i}^{cap}$ , $u_{i}^{cap}$ and the subsets $F_{i}^{in}$ , $F_{i}^{out}$ , $F_{i}^{act}$ ; members of the subsets also index certain values, as follows:

$$
\begin{array}{l l} j \in \mathcal {F} _ {i} ^ {\text {in}}: & l _ {i j} ^ {\text {in}}, x _ {i j} ^ {\text {in}}, u _ {i j} ^ {\text {in}}; \\ j \in \mathcal {F} _ {i} ^ {\text {out}}: & l _ {i j} ^ {\text {out}}, x _ {i j} ^ {\text {out}}, u _ {i j} ^ {\text {out}}; \\ k \in \mathcal {F} _ {i} ^ {\text {act}}: & l _ {i k} ^ {\text {act}}, x _ {i k} ^ {\text {act}}, u _ {i k} ^ {\text {act}}, c _ {i k} ^ {\text {act}}, r _ {i k} ^ {\text {act}}. \end{array}
$$

It follows that there should be a key field, two data fields, and three subfiles. Each subfile should have its own key field, and three to five data fields. The result looks like this:

![](/api/attachments/HKEV5UET/fulltext/images/19b064985fe1538bda470078483497b3a1fd01e84e548aab3a276b42de581817.jpg)

Here each facilities record contains three collections of subrecords, rather than just one as in the case of the materials.

Still missing from this structure, however, is the detailed activities data. For each k in the indexed set $F_{i}^{act}$ , the model specifies not only the values $l_{ik}^{act}$ , $x_{ik}^{act}$ and so forth, but also the sets $A_{ik}^{in}$ and $A_{ik}^{out}$ , which are in turn also used to index data values:

$$
\begin{array}{l l} j \in \mathcal {A} _ {i k} ^ {\text {in}}: & a _ {i j k} ^ {\text {in}} \\ j \in \mathcal {A} _ {i k} ^ {\text {out}}: & a _ {i j k} ^ {\text {out}} \end{array}
$$

Since we have here two sets $(\mathcal{A}_{ik}^{\mathrm{in}}, \mathcal{A}_{ik}^{\mathrm{out}})$ indexed over a set $(\mathcal{F}_{i}^{\mathrm{act}})$ that is itself indexed over a set $(\mathcal{F})$ , we are led to extend Rule H1b to let sub-subfiles appear within subfiles. Specifically, two subsubfiles that correspond to $A_{ik}^{in}$ and $A_{ik}^{out}$ must appear within the subfile ACTIVITIES that corresponds to $F_{i}^{act}$ . Calling the sub-subfiles ACT\_INPUTS and ACT\_OUTPUTS, the subfile for activities is diagrammed as follows:

![](/api/attachments/HKEV5UET/fulltext/images/e118c9fb1f9de8cadb016dab5312e72d7869d641341844450a80083c5b3b374a.jpg)

The foreign key specification act\_in\_mat → FACILITIES. INPUTS represents the natural generalization of rule H5 to the model's containment restriction $A_{ik}^{in} \subseteq F_{i}^{in}$ . It specifies a many-to-one relationship from the key field of the sub-subfile corresponding to $A_{ik}^{in}$ (that is, act\_in\_mat), to the subfile corresponding to $F_{i}^{in}$ (which we denote FACILITIES. INPUTS because it is the INPUTS subfile of the FACILITIES file). The comparable relationship in the relational context is not so easy to represent, as we have already noted in Section 3.

The full facilities file is represented by substituting the above ACTIVITIES subfile diagram for the one that appears within the previously described

FACILITIES diagram. A complete hierarchical database structure for the production problem thus consists of just two files, but with extensive internal structures of subfiles and sub-subfiles. The diagrams for both the hierarchical and relational cases are collected in Appendix C, where the reader may more easily compare them. We proceed next to consider their relative advantages and disadvantages.

## 5. Comparisons

The implementation to be described in Section 6 employs a database management system that supports both hierarchical and relational schemes. Thus, notwithstanding the current popularity of the relational model, for our application the choice of scheme has been more than an academic matter.

Before proceeding to the implementational details, we consider here some general contrasts between the relational and hierarchical approaches. We argue that either approach has benefits in ease of use, but that there is a clear tradeoff between a hierarchical scheme's compact data storage and a relational scheme's flexible data retrieval.

## 5.1. Ease of use

The hierarchical database diagrams in Appendix C may appear, at first glance, to be more complicated than their relational counterparts. Yet on closer examination, the hierarchical scheme is seen to offer an especially simple and straightforward representation of the data. There are only two files, one for materials and one for facilities. In the materials file, each record contains all the purchase and sales data on one material, plus a list of any applicable conversions together with their costs and yields. In the facilities file, each record likewise specifies all information pertinent to a particular facility; and each activity subrecord gives all information pertinent to one activity at the facility. There is a certain intuitive arrangement to the hierarchical structure that is readily conveyed to database users.

The relational structure, by comparison, has a larger number of simpler files, and arguably requires the designer or administrator to have a deeper understanding of database principles in order to arrange for the extraction of desired information. The relational approach derives a significant advantage, however, from its solid foundation in the theory of relational algebra and relational calculus, and from its use of well-established concepts such as key, query and view in the relational context. Numerous implementations are based on the relational theory and concepts; many support a query language, SQL, for which there is an international standard. Popular textbooks [12,37] also emphasize the relational approach. In contrast, implementations of hierarchical databases are less common and are minimally standardized. As a result, experienced database designers are more familiar with the relational structure of Section 3 and have a broader choice of database software for implementing such a structure.

While these distinctions between hierarchical and relational are important, in practice they may be less than absolute. Relying on the features of a relational database management system, an administrator may be able to set up a relational scheme that supports certain hierarchical views for the user. Conversely, since hierarchical database schemes may be viewed as nested relational schemes, the popular relational algebra and relational query languages may be generalized for application to the hierarchical case; there has been extensive research along these lines, as the annotated bibliography in $[12]$ (Section 26.5) suggests.

## 5.2. Data storage

All of our proposed database schemes satisfy the normalization requirement that no piece of information be stored in more than one place. The hierarchical schemes do allow the data to be maintained more compactly, however.

The difference can be seen clearly in the data structures for the general LP model, which are shown side-by-side in Appendix C. There would be an exact correspondence between fields in the two structures, except that the coeff\_col key field in the relational structure does not appear in the hierarchical one. This field is needed in the relational approach, because each coefficient is regarded as an independent entity, which can be identified only by giving the constraint (coeff\_row) and variable (coeff\_col) to which it belongs. In the hierarchical approach, however, a coefficient is considered part of the information about a variable; within the coefficient subrecords for a variable, it suffices to specify the constraint to which each coefficient belongs.

This difference of one field leads to several reductions in what must be stored and retrieved. The hierarchical structure saves one coeff\_col entry for each of the many coefficients. In addition, any space that would be required by an index file for the coeff\_col field – to facilitate searching or sorting on the field – is also saved. Finally, a lengthy index for the coeff\_row field can also be avoided. Under the hierarchical structure, each coefficient subfile can be expected to have just a few records, because linear programs typically involve each variable in only a few constraints. Hence the subfile's coeff\_row key field requires only a minimal form of indexing to permit efficient searches of subrecords. The extent of these savings necessarily depends on implementational details; in Section 6 we exhibit some examples based on experiments with realistic data.

Many opportunities for comparable savings can be found in our database for the multi-facility production problem. Corresponding to each of the four files having two key fields and the two files having three key fields in the relational structure, there is just one key field needed in the hierarchical structure. Thus there is a savings of the contents of 8 key fields and of as many as 14 indexes. Indeed, the only sizable indexes likely to be used by the hierarchical scheme are for the mat\_name key field of the MATERIALS file and the fac\_name key field of the FACILITIES file.

## 5.3. Data retrieval

We have previously hinted that the hierarchical structure pays for its compactness with a loss of flexibility. In the general LP case depicted in Appendix C, the difference is essentially that the hierarchical scheme can only easily access coefficients 'by variable' whereas the relational scheme can also conveniently scan them 'by constraint'.

As a specific illustration, consider the problem of displaying all nonzero coefficients in a given constraint, together with the values of the corresponding variables. Such a request is readily filled by use of the select and join operations provided by any relational database management system. We would not expect to easily perform any comparable query on the hierarchical structure, however, because it does not conveniently collect the coefficients in a single file; they are scattered throughout the subfiles of different records in the VARIABLES file. This difficulty can be remedied in various ways, as described for example by [37] (Section 2.6), but only by giving up some or all of the hierarchical scheme's advantage in data storage.

So long as we only want to access the nonzero coefficients of given variables, however, the hierarchical structure should be quite efficient. Indeed, all of the coefficient information for a variable can be retrieved directly as part of the record for the variable.

In the case of the multi-facility production model, the situation is predictably similar. Some queries are as easily performed on the hierarchical structure as on the relational one, because they involve just scanning a record and its subrecords (and possibly their sub-subrecords):

\- What materials can be converted from a given material, and at what cost and yield?

\- What are all the materials used as input by a given facility, and how much of each is used in the optimal solution?

\- What are the costs of all the activities at a given facility?

Where the desired information is scattered among subrecords, however, the relational model can be expected to be superior - as in these seemingly similar examples:

\- What materials can be converted to a given material, and at what cost and yield?

\- What are all the facilities that use a certain material as input, and how much do they use in the optimal solution?

\- What are the costs of all the activities that make use of a given material?

These kinds of queries are useful not only for retrieving information of interest, but for diagnostic purposes. For instance, if the last query above shows that no activity makes use of a given material, then there is reason to expect an error or omission in the data.

## 6. Implementation

Our investigation of database structures was originally motivated by the intention of implementing them in an easy-to-use system for production planning. This section describes the system that has evolved. We emphasize the practical consequences of implementing database structures for linear programs, especially where difficult or unexpected design decisions have been required.

In general terms, the operation of our system involves the following steps:

1. Collect data describing a production scenario, and store it according to one of the previously described database schemes for the multi-facility production model.

2. Extract the bounds and the nonzero coefficients of the associated linear program, and store them according to one of the previously described database schemes for the general linear programming model.

3. Solve the linear program, and enter the optimal values in the appropriate fields of the database files.

4. Display and print the results as required.

As a practical matter, we expect step 1 to be only rarely performed in full. Usually an existing scenario will be modified by changing only a few fields, and step 2 will modify the bounds and coefficients accordingly. Steps 3 and 4 will then be repeated to obtain and examine the new solution.

The presentation in this section has four parts that correspond to major concerns of the implementation: data management, optimization, reporting, and updating.

## 6.1. Data management

In preliminary discussions with potential users, we encountered a widespread perception of linear programming as a difficult modeling technique that could be applied only through a great investment in time and effort. We resolved to design a system that would tend to counteract this perception as much as possible.

Our first decision concerned the database management system software within which our database schemes would be implemented. We chose 4th Dimension [32], an Apple Macintosh package that offered especially powerful facilities for defining menus and graphical entry screens tailored to our application. Fortuitously, 4th Dimension also provided a stimulus to our research by supporting both relational and hierarchical models of data, but its selection was based more on its interface features than on any other factor. In more recent years, similar features have spread to popular database packages running under Microsoft Windows, so that if we were to start the project today we would have a much broader selection.

![](/api/attachments/HKEV5UET/fulltext/images/c08c35203c0a3c58ca648bb10e728dfa47d615d8871281858f7bfe2813d13f0f.jpg)  
Fig. 2. A data entry layout for a record in the MATERIALS file.

We next chose to implement the hierarchical scheme of Section 4 for the multi-facility production data. Our decision was based largely on the perception that, in the first version of the 4th Dimension software, hierarchical structures were best supported and easiest to work with. Subsequent versions have offered much stronger support for relational structures; our experiments with a relational scheme for the VARIABLES, CONSTRAINTS and COEFFICIENTS files are described later in this section.

The ‘design environment’ of 4th Dimension is employed to define the underlying database scheme, as well as to design layouts through which the user can enter, examine or modify data in individual records. The layout for materials, presented in Fig. 2, is seen to provide entry areas for seven of the fields of the hierarchical MATERIALS file:

mat\_name

buy\_cost, buy\_min, buy\_max
sell\_cost, sell\_min, sell\_max

![](/api/attachments/HKEV5UET/fulltext/images/207b0260a3c797acddd6568421345eae94b1eb787711ad1e3253b2736e946bf6.jpg)  
Fig. 3. Two views of a data entry layout for a subrecord in the CONVERSIONS subfile of the MATERIALS file. At left a typical subrecord is displayed. At right the user has pulled down a menu of materials that are eligible targets for conversion.

Two additional fields have been added for informational purposes: one to describe the units in which the material is measured, and one to classify the material as an input, intermediate or output. This sort of information can be valuable to users even though it has no bearing on the linear program.

The scrollable area at the bottom of the layout presents the records of the CONVERSIONS subfile, one to a line. Each line contains what we have called the to\_mat, conv\_yield and conv\_cost records of a subfile field. To enter a new conversion, the user double-clicks at the top of the area, bringing up the subsidiary layout of Fig. 3. A menu of material names for the to\_mat field can be pulled down as illustrated. We find this kind of menu to be an essential practical feature, because users do not remember the exact names of all materials they have defined.

The same approach is applied to displaying the facilities data, with natural extensions to handle the multiple subfiles and sub-subfiles of the FACILITIES file. Examples are provided in a longer version of this paper $[18]$ that is available from the author.

## 6.2. Optimization

To find profit-maximizing levels of operation, our implementation executes a series of programs to perform the following operations:

1. Scan the database to determine the constraints of the associated linear program. Extract constraint-related data values ( $l_{i}^{row}$ and $u_{i}^{row}$ ) and store them in a separate CONSTRAINTS file.

2. Scan the database to determine the variables of the associated linear program. Extract variable-related data values ( $c_{j}$ , $l_{j}^{col}$ , $u_{j}^{col}$ and nonzero $a_{ij}$ ) and store them in a separate VARIABLES file.

3. Scan the CONSTRAINTS and VARIABLES files, and write all of the essential information about the linear program to an ordinary text file in a compact format.

4. Read the text file, solve the indicated linear program, and write the optimal values of the variables to a second text file.

5. Read the second text file, and place the optimal values in appropriate fields of the MATERIALS and FACILITIES files.

Steps 1–3 and 5 are implemented in 4th Dimension's database programming language, which can specify the actions associated with menu items and layouts, and with objects (such as buttons and fields) within layouts. This language resembles a cross between Pascal and HyperTalk, with numerous built-in functions for working with database files, fields, and records. Step 4 uses separate, general-purpose linear programming software. We comment below on the major design issues posed by individual steps, and then address overall limitations on problem size.

For steps 1 and 2, the structures of the CONSTRAINTS and VARIABLES files may be either the relational ones of Section 3 or the hierarchical ones of Section 4. Table 1 compares the performance of these alternatives on an example having 286 materials and 19 facilities. The hierarchical structure, which has been used in our implementation, requires somewhat less disk space and computation time, as the discussion in Section 5 has predicted. The relational structure is still efficient enough to be practical, however.

Step 2 generates variables $x_{j}^{buy}$ (or $x_{j}^{sell}$ ) only for those materials that have a positive upper limit $u_{j}^{buy}$ (or $u_{j}^{sell}$ ). Since typically few materials are both bought and sold, and many intermediates are neither bought nor sold, this refinement can substantially reduce the number of VARIABLES records generated.

For step 4, we employ a general-purpose programming language to create a short driver that reads the first text file, calls an algorithm from an optimization subroutine library, and writes the optimal values to the second text file. We use Fortran and the primal simplex routines from the XMP library [27], but our arrangement could easily be adapted to use any callable linear programming package. Since XMP requires only a column-wise representation of the coefficient matrix, we find it convenient to place the subfile of nonzero coefficients within the VARIABLES file.

Table 1  
A comparison of the hierarchical and relational structures for the VARIABLES and CONSTRAINTS files

<table><tr><td></td><td colspan="2">Hier</td><td>Rela</td></tr><tr><td>Materials</td><td></td><td>286</td><td></td></tr><tr><td>Facilities</td><td></td><td>19</td><td></td></tr><tr><td>Constraints</td><td></td><td>853</td><td></td></tr><tr><td>Variables</td><td></td><td>847</td><td></td></tr><tr><td>Nonzeroes</td><td></td><td>2337</td><td></td></tr><tr><td>Steel data</td><td></td><td>399K</td><td></td></tr><tr><td>LP data</td><td>557K</td><td></td><td>740K</td></tr><tr><td>Gen const</td><td></td><td>1:39</td><td></td></tr><tr><td>Gen var</td><td>7:21</td><td></td><td>9:01</td></tr><tr><td>Write constr</td><td>0:55</td><td></td><td>0:59</td></tr><tr><td>Write var</td><td>1:19</td><td></td><td>1:33</td></tr><tr><td>Solve (XMP)</td><td></td><td>1:59</td><td></td></tr><tr><td>Read var</td><td></td><td>1:38</td><td></td></tr><tr><td>Read constr</td><td></td><td>1:25</td><td></td></tr></table>

Note:  
Centered quantities are the same for both alternatives. Timings are in minutes and seconds on a Macintosh IIci with a 50 MHz 68030 accelerator, using 4th Dimension 3.0.1 and 4D Compiler 2.0.2; the four groups of times (Gen, Write, Solve, Read) correspond to steps 1-2, 3, 4, and 5, respectively, as defined in the text.

It is not hard to coordinate steps 3–5 so that each optimal value is placed in the appropriate col\_optimal record of the VARIABLES file. The user wants to look at materials and facilities, however, not at constraints and variables. Thus, step 5 must be able to determine, by looking at a VARIABLES record, where the associated optimal value ought to go in the MATERIALS or FACILITIES file. At the cost of some extra processing, this information could be encoded in the col\_name field. At the cost of some extra space instead, we place the information in three fields, one that gives the variable's type (material bought, input to facility,...) and two that specify the pertinent material, facility or activity as appropriate. The col\_name key field holds a unique record number that has no intrinsic meaning.

There is no inherent limit on the size of optimization problems that can be generated and solved by this kind of arrangement. When our first prototype was completed in 1987, the speed of available Macintosh hardware and the 4th Dimension software imposed a practical limit of about 1000 variables. Subsequent advances have pushed the limit much higher, so that – for single-period planning in steel mills – the true practical limit at this point is determined by the level of detail that is worth modeling, rather than by the capabilities of the implementation. A linear program of even 2500 variables would represent a very high level of detail.

## 6.3. Reporting

A modified collection of layouts present the optimal values along with the input data. Fig. 4 shows the optimality layout that corresponds to the input layout in Fig. 2. The columns labeled 'Actual' give the optimal levels of purchases, sales, and conversions for the named material; these are the optimal values of the $x_{j}^{\text{buy}}$ , $x_{j}^{\text{sell}}$ and $x_{jj'}^{\text{conv}}$ variables in our algebraic formulations (Appendices A and B).

![](/api/attachments/HKEV5UET/fulltext/images/2397661ad3f87721cef472392e27251307809890539ddca157af7f80019711c9.jpg)  
Fig. 4. An analogue of the layout in Fig. 2, but showing optimal values as well as the materials data.

![](/api/attachments/HKEV5UET/fulltext/images/3a0d865759bd710177fb533323256ea88294687d5c6864c293f95d97cf58e47c.jpg)  
Fig. 5. An automatically generated interpretation of the dual value on a material balance constraint, requested by clicking on the '?' button in the 'Material Optimum' layout (Fig. 4).

The number labeled ‘Value’ is the optimal dual value for the material’s balance constraint (the one that has the form $x_{j}^{buy} + \cdots = x_{j}^{sell} + \cdots$ ). This value can be interpreted in various ways, depending on whether the material is bought or sold and on whether the amount bought or sold is at its lower or upper limit (or neither). Since many of the intended users of the system are unfamiliar with dual values and their interpretations, we have added the option of clicking on an adjacent button (marked ‘?’) to bring up a message box giving the most appropriate interpretation under the circumstances. An example of the message is depicted in Fig. 5.

The availability of optimal values alongside data values is in fact a key feature of any reporting environment for linear programming. The facilities of 4th Dimension permit elaborate transformations of the results, to put them in forms that people want to see. As an example, in response to selection of a certain menu item, our implementation brings up a summary layout (Fig. 6) that breaks the different kinds of cost out of the net profit. The costs are computed by a short program, written in 4th Dimension's programming language, which is executed every time the summary is requested. A variety of printed reports are similarly available.

![](/api/attachments/HKEV5UET/fulltext/images/a277de3397a2fb9f2fccd94e44c5125fe993985d4f2c91dfba2eee2b9332a1fc.jpg)  
Fig. 6. A summary layout showing revenue and cost totals.

![](/api/attachments/HKEV5UET/fulltext/images/859c74286adbe9d30f0b0ae47af43adbecea4696f00353eee5919bb2edc20541.jpg)  
Fig. 7. A representative message produced by the optional diagnostic routines.

Another kind of reporting is provided by a sequence of diagnostic tests implemented in the 4th Dimension language. These tests scan the data for inconsistencies, such as materials that must be sold but that cannot be created or purchased in any way. The diagnostics are run only when the user requests them, through a menu selection; they produce brief messages identifying any problems found (Fig. 7).

Most of the inconsistencies detected by our diagnostic tests would also be revealed by a general-purpose diagnostic tool such as ANALYZE $[21,22]$ . By detecting these errors though a scan of the database, before any linear program is generated, we can save the user some time and can provide error messages more closely tailored to the implementation. On the other hand, we have had to write and maintain some fairly intricate and specialized routines in the database language to carry out our diagnostics, whereas ANALYZE would apply equally well to any linear program that we happened to generate.

## 6.4. Updating

In our experiments with diverse steel-production scenarios, the effort of generating the constraints and variables has invariably dominated the effort of solving the resulting linear program. This is not a hindrance at the beginning of a project, since both generation and solution seem fast compared to the work of collecting all the steel mill data and entering it into the database. In typical continued use, however, the difference between one scenario and the next is often just a few quick changes to the data. A substantial part of the user's time might thus end up being spent in waiting for the generation stage to be completed.

Fortunately, when successive scenarios are quite similar, so are the successive linear programs. In most cases, changing one value in the database has the effect of changing just one bound or coefficient in the linear program.

To take advantage of this situation, we allow the user to switch to an updating mode. The layouts in this mode look almost the same as those exhibited previously, but they support only the simplest and most straightforward updating operations. For example, the materials update layout allows changes to the costs, limits and yields, but not additions or deletions of records or changes to material names. When one of the allowed changes is made, a corresponding change is quickly made to the VARIABLES file, so that its representation is kept up to date.

When all updates are completed, it remains only to run the steps 3–5 defined in Section 6.2. Since step 2 is usually the most time-consuming, the savings afforded by updating are often considerable.

There are many other ways in which we might allocate the work of generating a linear program. The following represent perhaps the two most extreme possibilities:

\- The coefficients and bounds could be generated directly from the MATERIALS and FACILITIES files, without the intermediate creation of records in a CONSTRAINTS file or a VARIABLES file.

\- The CONSTRAINTS and VARIABLES files could be automatically built up, step by step, along with the MATERIALS and FACILITIES files, so that data entry would always be in a powerful update mode that could handle changes of any kind.

We have adopted one of the many intermediates between these possibilities, in the hope of achieving a good compromise between ease of implementation, speed, and reliability.

The influence of reliability on our design decision is perhaps surprising, but should not be underestimated. So long as the 4th Dimension programs implementing steps 1 and 2 are subject to development and modification, displays of the CONSTRAINTS and VARIABLES files are a valuable tool for validation. If the output of step 3 - essentially, a list of numbers – were instead generated directly from the MATERIALS and FACILITIES files, our programs would be a lot harder to debug reliably. Hence, even if direct generation were the preferred option, we might want to implement it only when further program modifications were no longer anticipated.

## 7. Conclusions and extensions

This paper has presented both general principles and specific examples relating to database structures for mathematical programming models. The discussion below states the conclusions that can be drawn directly from this work, and suggests promising extensions to address additional indexing structures, additional database types, and more complex models.

## 7.1. Conclusions

The principles formalized in Sections 3 and 4 of this paper show that database structures can be derived in a straightforward and systematic way from sets and indexing that are characteristic of mathematical programming data. These results apply to conventional forms of data indexed over pairs, triples, and higher-order relations, and also to more elaborate forms; in particular, the use of sets indexed over sets is seen to lead naturally to hierarchical database structures. As a result, the choice of index sets for the formulation of an optimization problem is observed to involve certain tradeoffs in convenience and efficiency of data access, as explained in Section 5.

The steel example developed in this paper shows that the database principles of Sections 3 and 4 can be transferred directly to the design of practical database applications. In fact, the entire application interface – everything but the optimization code – can be built within an off-the-shelf database development system, as illustrated in Section 6. The interface does need to be designed to accommodate special requirements of mathematical programming, such as navigation through an intricate hierarchy of data tables, fast updating in response to data changes, and clear presentation of optimal results. Such requirements can be quite different from the needs of more customary database applications built around tables of people or orders, but can be addressed successfully by current database systems.

## 7.2. Extensions for other indexing structures

The forms of indexing investigated in Sections 3 and 4 meet the needs of a great variety of mathematical programming formulations. Nevertheless, there are other potentially useful forms of indexing to which the results of this paper might be extended. The idea of indexed collections of sets can be extended to true sets of sets, for example, and more general kinds of multi-dimensional and hierarchical sets can be put to good use as shown by Bisschop and Kuip [5,6]. There has been little consideration to date of the naturally corresponding database structures for any of these kinds of indexing.

A different approach to extensions for other indexing structures would focus on modeling languages that have been designed to help people describe mathematical programs to computer systems. In particular, most algebraic modeling languages $[25]$ incorporate a variety of indexing options that can be taken as empirical evidence for the kinds of indexing that are required in practice. Thus, it would make sense to study the range of database structures that would be necessary to support all of the indexing schemes provided by one modeling language. The implementation of database links for the MPL language can be regarded as resulting from a study along these lines $[28]$ ; the next step would be to extend this approach to a language such as AMPL $[19,20]$ or AIMMS $[4]$ that offers a richer variety of set and indexing expressions.

## 7.3. Extensions for other database types

An approach opposite to that above would analyze an alternative database structure to determine how it might be used in support of mathematical programming. Although the relational and hierarchical structures described in this paper provide a good fit to the data of large-scale optimization problems, there remains the possibility that other structures would prove to be superior in some cases.

Multidimensional databases [23] are one likely candidate for future study. Mathematical programming data does tend to have a multidimensional structure, at least in the sense that a model's parameters and variables tend to have many indices; five or more subscripts are not unusual in LP formulations. Although the steel model in this paper does not appear to be very heavily indexed, additional subscripts would be needed to describe a version for multiple periods or locations. Similarly indexed quantities such as $l_{ij}^{\text{out}}$ , $u_{ij}^{\text{out}}$ and $x_{ij}^{\text{out}}$ are moreover most naturally viewed as belonging to a single structure that has a dimension labeled 'data type' as well as the obvious dimensions of materials and facilities corresponding to the two subscripts.

Multidimensional database structures also provide an appealing resolution to the anomaly of the missing activity set $\mathcal{A}$ that was discussed in Section 2. Wherever the activity subscript $k$ appears in the steel planning model, the facility subscript $i$ is also to be found, with the indexing over $(i,k)\in\mathcal{F}^{\mathrm{act}}$ (or equivalently, $i\in\mathcal{F}$ and $k\in\mathcal{F}_{i}^{\mathrm{act}}$ ). As a result, in the multidimensional context the facilities and activities can be viewed as comprising a two-level hierarchy along a single dimension, with facilities at the higher level and one or more activities under each facility at the lower level. The quantities $l_{ik}^{\mathrm{act}}, u_{ik}^{\mathrm{act}}, c_{ik}^{\mathrm{act}}, r_{ik}^{\mathrm{act}}$ and $x_{ik}^{\mathrm{act}}$ are then seen to define a two-dimensional table, with the facility/activity hierarchy along one dimension and data type along the other.

Like the hierarchical and relational structures, multidimensional database structures have been motivated by business data that differs in some respects from mathematical programming data. In particular the rates, bounds and costs of a typical optimization problem do not add up along their dimensions, in contrast to the sales figures that sum to sales totals in canonical examples of multidimensional data $[23]$ . At a more fundamental level, however, multidimensional database management systems have been motivated by concerns for flexible analysis and decision support (often described as on-line analytical processing, or OLAP $[11,17]$ ) that have much in common with concerns underlying the design of advanced mathematical programming systems. A formal correspondence between the data representations of these systems is thus likely to be worth developing.

## 7.4. Extensions for more complex models

Whether or not this work is extended to additional forms of indexing and varieties of databases, studies of additional mathematical programming applications are likely to prove valuable. The rules of database construction derived in this paper may prove to require some refinement when they are tested on a broader variety of complex models.

For the steelmaking example that is the focus of this paper, an extension to multiperiod planning has been considered in the doctoral dissertation of Dutta [13]. The introduction of indexing over time periods motivates consideration of a broader variety of database structures, including ones that incorporate both hierarchical and relational elements. The multi-period case thus provides an opportunity to evaluate how the rules of Sections 3 and 4 may interact when each is applied to some part of a model's data.

The interface considerations raised earlier in this paper must also be extended in significant ways to deal with the addition of indexing sets for time and for inventory storage areas. The materials displays in Figs. 2 and 4 may be adapted, for example, in either of two ways: by replicating them over times, or by generalizing them to show data from all time periods. As is often the case when there are alternatives for presenting data, users are likely to want both options.

A further challenge is posed by additional levels of indexing, such as are needed to model multiple production locations, and to incorporate multiple scenarios for stochastic programming or robust optimization. The large quantities and complex interconnections of data in these cases make them harder to analyze, but also more likely to benefit from the use of appropriate database structures.

## Acknowledgements

This work has been supported in part by contracts from the American Iron and Steel Institute and from Armco, Inc., and by grants DDM-8908818 and DMI-9414487 from the National Science Foundation. Valuable comments on earlier versions of some of this material were provided by A.M. Geoffrion, by reviewers for the 24th Hawaii International Conference on System Sciences, and by the referees.

## Appendix A. Formulation using ordered pairs and triples

## A.1. Materials data

$\mathcal{M} =$ the set of materials;

$l_{j}^{buy}$ = the lower limit on purchases of material j, for each $j \in M$ ;

$u_{j}^{buy}$ = the upper limit on purchases of material j, for each $j \in M$ ;

$c_{j}^{buy}$ = the cost per unit of material j purchased, for each $j \in M$ ;

$l_{j}^{\mathrm{sell}} =$ the lower limit on sales of material $j$ , for each $j \in \mathcal{M}$ ;

$u_{j}^{\mathrm{sell}}$ = the upper limit on sales of material j, for each $j \in M$ ;

$c_{j}^{\mathrm{sell}} =$ the revenue per unit of material $j$ sold, for each $j\in \mathcal{M}$ ;

$\mathcal{M}^{\mathrm{conv}} \subseteq \mathcal{M} \times \mathcal{M}$ is the set of conversions: $(j, j') \in \mathcal{M}^{\mathrm{conv}}$ means that material $j$ can be converted to material $j'$ ;

$a_{jj'}^{\mathrm{conv}} = \text{number of units of material } j'$ that result from converting one unit of material $j$ , for each $(j,j') \in \mathcal{M}^{\mathrm{conv}}$ ;

$c_{jj'}^{\mathrm{conv}} = \mathrm{cost per unit of material} j$ of the conversion from $j$ to $j'$ , for each $(j,j')\in \mathcal{M}^{\mathrm{conv}}$ .

## A.2. Facilities data

$\mathcal{F} =$ the set of facilities;

$l_{i}^{cap}$ = the minimum amount of the capacity of facility i that must be used, for each $i \in F$ ; $u_{i}^{cap}$ = the capacity of facility i, for each $i \in F$ ; $F^{in}$ $\subseteq F \times M$ is the set of facility inputs: $(i,j) \in \mathcal{F}^{in}$ means that material j is used as an input at facility i;

$l_{ij}^{in}$ = the minimum amount of material j that must be used as input at facility i, for each $(i,j)\in\mathcal{F}^{\text{in}}$ ;

$u_{ij}^{\mathrm{in}}$ = the maximum amount of material $j$ that may be used as input at facility $i$ , for each $(i,j)\in \mathcal{F}^{\mathrm{in}}$ ;

$\mathcal{F}^{\mathrm{out}} \subseteq \mathcal{F} \times \mathcal{M}$ is the set of facility outputs: $(i,j)\in \mathcal{F}^{\mathrm{out}}$ means that material $j$ is produced as an output at facility $i$ ;

$l_{ij}^{out}$ = the minimum amount of material j that must be produced as output at facility i, for each $(i,j)\in\mathcal{F}^{\mathrm{out}}$ ;

$u_{ij}^{\mathrm{out}} =$ the maximum amount of material $j$ that may be produced as output at facility $i$ , for each $(i,j)\in \mathcal{F}^{\mathrm{out}}$ .

## A.3. Activities data

$\mathcal{F}^{\mathrm{act}} \subseteq \{(i,k): i \in \mathcal{F}\}$ is the set of activities: $(i,k) \in \mathcal{F}^{\mathrm{act}}$ means that $k$ is an activity available at facility $i$ ;

$l_{ik}^{act}$ = the minimum number of units of activity k that may be run at facility i, for each $(i,k)\in\mathcal{F}^{\mathrm{act}}$ ;

$u_{ik}^{\mathrm{act}} =$ the maximum number of units of activity $k$ that may be run at facility $i$ , for each $(i,k)\in \mathcal{F}^{\mathrm{act}};$

$c_{ik}^{\mathrm{act}} =$ the cost per unit of running activity $k$ at facility $i$ , for each $(i,k)\in \mathcal{F}^{\mathrm{act}}$ ;

$r_{ik}^{act}$ = the number of units of activity k that can be accommodated in one unit of capacity of facility i, for each $(i,k)\in\mathcal{F}^{\mathrm{act}}$ ;

$\mathcal{A}^{\mathrm{in}} \subseteq \{(i,j,k):(i,j) \in \mathcal{F}^{\mathrm{in}} \text{ and } (i,k) \in \mathcal{F}^{\mathrm{act}}\}$ is the set of activity inputs: $(i,j,k) \in \mathcal{A}^{\mathrm{in}}$ means that input material $j$ is used by activity $k$ at facility $i$ ;

$a_{ijk}^{\mathrm{in}} = \text{units of input material } j \text{ required by one unit of activity } k \text{ at facility } i, \text{ for each } (i,j,k) \in \mathcal{A}^{\mathrm{in}};$

$\mathcal{A}^{\mathrm{out}} \subseteq \{(i,j,k):(i,j) \in \mathcal{F}^{\mathrm{out}} \text{ and } (i,k) \in \mathcal{F}^{\mathrm{act}}\}$ is the set of activity outputs: $(i,j,k) \in \mathcal{A}^{\mathrm{out}}$ means that output material $j$ is produced by activity $k$ at facility $i$ ;

$a_{ijk}^{\mathrm{out}} = \mathrm{units of output material} j$ produced by one unit of activity $k$ at facility $i$ , for each $(i,j,k) \in \mathcal{A}^{\mathrm{out}}$ .

## A.4. Variables

$x_{j}^{\mathrm{buy}} = \mathrm{units~of~material~} j\mathrm{bought, for~each~} j\in \mathcal{M};$

$x_{j}^{\mathrm{sell}} = \mathrm{units of material} j\mathrm{sold},\mathrm{for each} j\in \mathcal{M};$

$x_{jj'}^{\mathrm{conv}} = \text{units of material } j \text{ converted to material } j'$ , for each $(j, j') \in \mathcal{M}^{\mathrm{conv}}$ ;

$x_{ij}^{\mathrm{in}} = \text{units of material } j \text{ used as input by facility } i, \text{ for each } (i,j) \in \mathcal{F}^{\mathrm{in}};$

$x_{ij}^{\mathrm{out}} = \text{units of material } j \text{ produced as output by facility } i, \text{ for each } (i,j) \in \mathcal{F}^{\mathrm{out}};$

$x_{ik}^{\mathrm{act}} = \text{units of activity } k \text{ operated at facility } i, \text{ for each } (i,k) \in \mathcal{F}^{\mathrm{act}}.$

## A.5. Objective

Maximize revenue from sales, less the costs of purchasing, converting and running activities:

$$
\begin{array}{l} \sum_ {j \in \mathcal {M}} c _ {j} ^ {\text { sell }} x _ {j} ^ {\text { sell }} - \sum_ {j \in \mathcal {M}} c _ {j} ^ {\text { buy }} x _ {j} ^ {\text { buy }} - \sum_ {(j, j ^ {\prime}) \in \mathcal {M} ^ {\text { conv }}} c _ {j j ^ {\prime}} ^ {\text { conv }} x _ {j j ^ {\prime}} ^ {\text { conv }} \\ - \sum_ {(i, k) \in \mathcal {F} ^ {\text { act }}} c _ {i k} ^ {\text { act }} x _ {i k} ^ {\text { act}}. \end{array}
$$

## A.6. Constraints

For all $j \in M$ , the amount of material j made available by purchases, production and conversions must equal the amount used for sales, production and conversions:

$$
\begin{array}{l} x _ {j} ^ {\text { buy }} + \sum_ {(i, j) \in \mathcal {F} ^ {\text { out }}} x _ {i j} ^ {\text { out }} + \sum_ {(j ^ {\prime}, j) \in \mathcal {M} ^ {\text { conv }}} a _ {j ^ {\prime} j} ^ {\text { conv }} x _ {j ^ {\prime} j} ^ {\text { conv }} \\ = x _ {j} ^ {\text { sell }} + \sum_ {(i, j) \in \mathcal {F} ^ {\text { in }}} x _ {i j} ^ {\text { in }} + \sum_ {(j, j ^ {\prime}) \in \mathcal {M} ^ {\text { conv }}} x _ {j j ^ {\prime}} ^ {\text { conv }}. \end{array}
$$

For each $(i,j)\in\mathcal{F}^{\mathrm{in}}$ , the amount of input j used at facility i must equal the total consumption by all activities at facility i:

$$
x _ {i j} ^ {\text { in }} = \sum_ {(i, j, k) \in \mathscr {A} ^ {\text { in }}} a _ {i j k} ^ {\text { in }} x _ {i k} ^ {\text { act }}.
$$

For each $(i,j)\in\mathcal{F}^{\mathrm{out}}$ , the amount of output j produced at facility i must equal the total production by all activities at facility i:

$$
x _ {i j} ^ {\text { out }} = \sum_ {(i, j, k) \in \mathscr {A} ^ {\text { out }}} a _ {i j k} ^ {\text { out }} x _ {i k} ^ {\text { act }}.
$$

For each $i \in F$ , the capacity used by all activities at facility i must be within the specified limits:

$$
l _ {i} ^ {\text { cap }} \leq \sum_ {(i, k) \in \mathcal {F} ^ {\text { act }}} x _ {i k} ^ {\text { act }} / r _ {i k} ^ {\text { act }} \leq u _ {i} ^ {\text { cap }}.
$$

All variables must lie within the relevant limits defined by the data:

$l_{j}^{\mathrm{buy}}\leq x_{j}^{\mathrm{buy}}\leq u_{j}^{\mathrm{buy}},\quad \mathrm{for each} j\in \mathcal{M},$

$$
l _ {j} ^ {\text { sell }} \leq x _ {j} ^ {\text { sell }} \leq u _ {j} ^ {\text { sell }}, \quad \text { for   each } j \in \mathcal {M},
$$

$$
0 \leq x _ {j j ^ {\prime}} ^ {\text { conv }}, \quad \text { for   each } (j, j ^ {\prime}) \in \mathcal {M} ^ {\text { conv }},
$$

$$
l _ {i j} ^ {\text { in }} \leq x _ {i j} ^ {\text { in }} \leq u _ {i j} ^ {\text { in }}, \quad \text {   for   each   } (i, j) \in \mathcal {F} ^ {\text { in }},
$$

$$
l _ {i j} ^ {\text { out }} \leq x _ {i j} ^ {\text { out }} \leq u _ {i j} ^ {\text { out }}, \quad \text { for   each } (i, j) \in \mathcal {F} ^ {\text { out }}
$$

$l_{ik}^{\mathrm{act}} \leq x_{ik}^{\mathrm{act}} \leq u_{ik}^{\mathrm{act}}, \quad \text{for each } (i, k) \in \mathcal{F}^{act}$ .

## Appendix B. Formulation using indexed subsets

## B.1.Materials data

$\mathcal{M} =$ the set of materials

$l_{j}^{\mathrm{buy}} =$ the lower limit on purchases of material $j$ , for each $j \in \mathcal{M}$ ;

$u_{j}^{\mathrm{buy}} =$ the upper limit on purchases of material $j$ , for each $j \in \mathcal{M}$ ;

$c_{j}^{\mathrm{buy}} =$ the cost per unit of material $j$ purchased, for each $j\in \mathcal{M}$

$l_{j}^{\mathrm{sell}} =$ the lower limit on sales of material $j$ , for each $j \in \mathcal{M}$ ;

$u_{j}^{\mathrm{sell}} =$ the upper limit on sales of material $j$ , for each $j \in \mathcal{M}$ ;

$c_{j}^{\mathrm{sell}} =$ the revenue per unit of material $j$ sold, for each $j\in \mathcal{M}$ ;

$M_{j}^{\text{conv}} \subseteq M$ is a subset of conversions, for each $j \in M: j' \in M_{j}^{\text{conv}}$ means that material $j$ can be converted to material $j'$ ;

$a_{jj'}^{\mathrm{conv}} = \text{number of units of material } j'$ that result from converting one unit of material $j$ , for each $j \in \mathcal{M}$ and $j' \in \mathcal{M}_j^{\mathrm{conv}}$ ;

$c_{jj'}^{\mathrm{conv}} = \mathrm{cost per unit of material} j$ of the conversion from $j$ to $j'$ , for each $j \in \mathcal{M}$ and $j' \in \mathcal{M}_j^{\mathrm{conv}}$ .

## B.2. Facilities data

$\mathcal{F} =$ the set of facilities;

$l_{i}^{\mathrm{cap}} =$ the minimum amount of the capacity of

facility $i$ that must be used, for each $i \in \mathcal{F}$ ;

$u_{i}^{\mathrm{cap}} =$ the capacity of facility $i$ , for each $i\in \mathcal{F}$ ;

$$
\mathcal {F} _ {i} ^ {\mathrm{in}}
$$

$\subseteq \mathcal{M}$ is a subset of facility inputs, for each $i\in \mathcal{F}$ : $j\in \mathcal{F}_i^{\mathrm{in}}$ means that material $j$ is used as an input at facility $i$ ;

$l_{ij}^{in}$ = the minimum amount of material j that must be used as input at facility i, for each $i \in F$ and $j \in F_{i}^{in}$ ;

$u_{ij}^{\mathrm{in}}$ = the maximum amount of material $j$ that may be used as input at facility $i$ , for each $i \in \mathcal{F}$ and $j \in \mathcal{F}_i^{\mathrm{in}}$ ;

$\mathcal{F}_i^{\mathrm{out}} \subseteq \mathcal{M}$ is a subset of facility outputs, for each $i \in \mathcal{F}$ : $j \in \mathcal{F}_i^{\mathrm{out}}$ means that material $j$ is produced as an output at facility $i$ ;

$l_{ij}^{out}$ = the minimum amount of material j that must be produced as output at facility i, for each $i \in F$ and $j \in F_{i}^{out}$ ;

$u_{ij}^{out}$ = the maximum amount of material j that may be produced as output at facility i, for each $i \in F$ and $j \in F_{i}^{out}$ .

## B.3. Activities data

$\mathcal{F}_i^{\mathrm{act}} = \text{a subset of activities, for each } i \in \mathcal{F}: k \in \mathcal{F}_i^{\mathrm{act}}$ means that $k$ is an activity available at facility $i$ ;

$l_{ik}^{act}$ = the minimum number of units of activity k that may be run at facility i, for each $i \in F$ and $k \in F_{i}^{act}$ ;

$u_{ik}^{\mathrm{act}} =$ the maximum number of units of activity $k$ that may be run at facility $i$ , for each $i\in \mathcal{F}$ and $k\in \mathcal{F}_i^{\mathrm{act}}$ ;

$c_{ik}^{\mathrm{act}} =$ the cost per unit of running activity $k$ at facility $i$ , for each $i \in \mathcal{F}$ and $k \in \mathcal{F}_i^{\mathrm{act}}$ ;

$r_{ik}^{act}$ = the number of units of activity k that can be accommodated in one unit of capacity of facility i, for each $i \in F$ and $k \in F_{i}^{act}$ ;

$\mathcal{A}_{ik}^{\mathrm{in}} \subseteq \mathcal{F}_i^{\mathrm{in}}$ is a set of activity inputs, for each $i \in \mathcal{F}$ and $k \in \mathcal{F}_i^{\mathrm{act}}: j \in \mathcal{A}_{ik}^{\mathrm{in}}$ means that input material $j$ is used by activity $k$ at facility $i$ ;

$a_{ijk}^{\mathrm{in}} = \text{units of input material } j \text{ required by one unit of activity } k \text{ at facility } i, \text{ for each } i \in \mathcal{F}, k \in \mathcal{F}_i^{\mathrm{act}}, \text{ and } j \in \mathcal{A}_{ik}^{\mathrm{in}};$

$\mathcal{A}_{ik}^{\mathrm{out}} \subseteq \mathcal{F}_i^{\mathrm{out}}$ is a set of activity outputs, for each $i \in \mathcal{F}$ and $k \in \mathcal{F}_i^{\mathrm{act}}: j \in \mathcal{A}_{ik}^{\mathrm{out}}$ means that output material $j$ is produced by activity $k$ at facility $i$ ;

$a_{ijk}^{\mathrm{out}} = \mathrm{units of output material} j$ produced by one unit of activity $k$ at facility $i$ , for each $i \in \mathcal{F}$ , $k \in \mathcal{F}_i^{\mathrm{act}}$ , and $j \in \mathcal{A}_{ik}^{\mathrm{out}}$ .

## B.4. Variables

$x_{j}^{\mathrm{buy}} = \mathrm{units of material} j\mathrm{bought, for each} j\in \mathcal{M};$

$x_{j}^{\mathrm{sell}} = \mathrm{units~of~material~} j\mathrm{~sold, for~ each~} j\in \mathcal{M};$

$x_{jj'}^{\mathrm{conv}} = \text{units of material } j \text{ converted to material } j'$ , for each $j \in \mathcal{M}$ and $j' \in \mathcal{M}_j^{\mathrm{conv}}$ ;

$x_{ij}^{\mathrm{in}} = \text{units of material } j \text{ used as input by facility } i, \text{ for each } i \in \mathcal{F} \text{ and } j \in \mathcal{F}_i^{in};$

$x_{ij}^{\mathrm{out}} = \text{units of material } j \text{ produced as output by facility } i, \text{ for each } i \in \mathcal{F} \text{ and } j \in \mathcal{F}_i^{\mathrm{out}};$

$x_{ik}^{\mathrm{act}} = \text{units of activity } k \text{ operated at facility } i,$ for each $i\in \mathcal{F}$ and $k\in \mathcal{F}_i^{\mathrm{act}}$

## B.5. Objective

Maximize revenue from sales, less the costs of purchasing, converting and running activities:

$$
\begin{array}{l} \sum_ {j \in \mathcal {M}} c _ {j} ^ {\text {sell}} x _ {j} ^ {\text {sell}} - \sum_ {j \in \mathcal {M}} c _ {j} ^ {\text {buy}} x _ {j} ^ {\text {buy}} \\ - \sum_ {j \in \mathcal {M}} \sum_ {j ^ {\prime} \in \mathcal {M} _ {j} ^ {\text {conv}}} c _ {j j ^ {\prime}} ^ {\text {conv}} x _ {j j ^ {\prime}} ^ {\text {conv}} - \sum_ {i \in \mathcal {F}} \sum_ {k \in \mathcal {F} _ {i} ^ {\text {act}}} c _ {i k} ^ {\text {act}} x _ {i k} ^ {\text {act}}. \end{array}
$$

## B.6. Constraints

For all $j \in M$ , the amount of material j made available by purchases, production and conversions must equal the amount used for sales, production and conversions:

$$
\begin{array}{l} x _ {j} ^ {\text {buy}} + \sum_ {i \in \mathcal {F}: j \in \mathcal {F} _ {i} ^ {\text {out}}} x _ {i j} ^ {\text {out}} + \sum_ {j ^ {\prime} \in \mathcal {M}: j \in \mathcal {M} _ {j ^ {\prime}} ^ {\text {conv}}} a _ {j ^ {\prime} j} ^ {\text {conv}} x _ {j ^ {\prime} j} ^ {\text {conv}} \\ = x _ {j} ^ {\text {sell}} + \sum_ {i \in \mathcal {F}: j \in \mathcal {F} _ {i} ^ {\text {in}}} x _ {i j} ^ {\text {in}} + \sum_ {j ^ {\prime} \in \mathcal {M} _ {j} ^ {\text {conv}}} x _ {j j ^ {\prime}} ^ {\text {conv}}. \end{array}
$$

For each $i \in F$ and $j \in F_{i}^{in}$ , the amount of input j used at facility i must equal the total consumption by all activities at facility i:

$$
x _ {i j} ^ {\text { in }} = \sum_ {k \in \mathcal {F} _ {i} ^ {\text { act }}: j \in \mathcal {A} _ {i k} ^ {\text { in }}} a _ {i j k} ^ {\text { in }} x _ {i k} ^ {\text { act }}.
$$

For each $i \in F$ and $j \in F_{i}^{out}$ , the amount of output j produced at facility i must equal the total production by all activities at facility i:

$$
x _ {i j} ^ {\text { out }} = \sum_ {k \in \mathcal {F} _ {i} ^ {\text { act }}: j \in \mathcal {A} _ {i k} ^ {\text { out }}} a _ {i j k} ^ {\text { out }} x _ {i k} ^ {\text { act }}.
$$

For each $i \in F$ , the capacity used by all activities at facility i must be within the specified limits:

$$
l _ {i} ^ {\text { cap }} \leq \sum_ {k \in \mathcal {F} _ {i} ^ {\text { act }}} x _ {i k} ^ {\text { act }} / r _ {i k} ^ {\text { act }} \leq u _ {i} ^ {\text { cap }}.
$$

All variables must lie within the relevant limits defined by the data:

$$
l _ {j} ^ {\text { buy }} \leq x _ {j} ^ {\text { buy }} \leq u _ {j} ^ {\text { buy }}, \quad \text { for   each } j \in \mathcal {M},
$$

$$
l _ {j} ^ {\text { sell }} \leq x _ {j} ^ {\text { sell }} \leq u _ {j} ^ {\text { sell }}, \quad \text { for   each } j \in \mathcal {M},
$$

$$
0 \leq x _ {j j ^ {\prime}} ^ {\text { conv }}, \quad \text { for   each } j \in \mathcal {M} \text { and } j ^ {\prime} \in \mathcal {M} _ {j} ^ {\text { conv }},
$$

$$
l _ {i j} ^ {\text { in }} \leq x _ {i j} ^ {\text { in }} \leq u _ {i j} ^ {\text { in }}, \quad \text {   for   each   } i \in \mathcal {F} \text {   and   } j \in \mathcal {F} _ {i} ^ {\text { in }},
$$

$$
l _ {i j} ^ {\text { out }} \leq x _ {i j} ^ {\text { out }} \leq u _ {i j} ^ {\text { out }}, \quad \text { for   each } i \in \mathcal {F} \text { and } j \in \mathcal {F} _ {i} ^ {\text { out }},
$$

$$
l _ {i k} ^ {\mathrm{act}} \leq x _ {i k} ^ {\mathrm{act}} \leq u _ {i k} ^ {\mathrm{act}}, \quad \text {   for   each   } i \in \mathcal {F} \text {   and   } k \in \mathcal {F} _ {i} ^ {\mathrm{act}}.
$$

## Appendix C. Summary of database schemes

C.1. General model: Relational

![](/api/attachments/HKEV5UET/fulltext/images/5ac4326fc6ef09ff1639c56f36323dc96d40f8e4846a90f7a0c44eed8da00ae2.jpg)

```txt
FACILITY_INPUTS
in_fac → FACILITIES
in_mat → MATERIALS
in_min
in_opt
in_max
```

```txt
MATERIAL_CONVERSIONS
from_mat → MATERIALS
to_mat → MATERIALS
conv_yield
conv_cost
conv_opt
```

## C.2. General model: Hierarchical

![](/api/attachments/HKEV5UET/fulltext/images/b60c9057caedc652d7ef7b0a662acc24d692bb1ce9ce4878c8e8d7a5fca88c6e.jpg)

## C.3. Multi-facility production model: Relational

## C.4. Multi-facility production model: Hierarchical

![](/api/attachments/HKEV5UET/fulltext/images/53bfa69fd3b9a2be9e1cd5b1f745548fe0feb1d0bb939c1e0ed7ddafd1f70189.jpg)

<table><tr><td>MATERIALS</td></tr><tr><td>mat_name</td></tr><tr><td>buy_min</td></tr><tr><td>buy_opt</td></tr><tr><td>buy_max</td></tr><tr><td>buy_cost</td></tr><tr><td>sell_min</td></tr><tr><td>sell_opt</td></tr><tr><td>sell_max</td></tr><tr><td>sell_cost</td></tr></table>

```c
FACILITY_OUTPUTS
out_fac → FACILITIES
out_mat → MATERIALS
out_min
out_opt
out_max
```

```txt
ACTIVITY_INPUTS
act_in_fac → FACILITIES
act_in_mat → MATERIALS
act_in
act_in_rate
```

## References

[1] A. Atamtürk, E.L. Johnson, J.T. Linderoth, M.W.P. Savelsbergh, ARMOS: A relational modeling system, Technical report, School of Industrial and Systems Engineering, Georgia Institute of Technology, Atlanta, GA, 1996.

[2] T.E. Baker, A hierarchical/relational approach to modeling, Chesapeake Decision Sciences, New Providence, NJ, 1986; http://www.chesapeake.com/.

[3] F.W. Bielefeld, K.-D. Walter, R. Wartmann, A computer-based strategic planning system for steel production, Interfaces 16 (4) (1986) 41–46.

[4] J. Bisschop, R. Entriken, AIMMS: The modeling system, Paragon Decision Technology, Haarlem, The Netherlands, 1993.

[5] J.J. Bisschop, C.A.C. Kuip, Hierarchical sets in mathematical programming modeling languages, Computational Optimization and Applications 1 (1993) 415–438.

[6] J.J. Bisschop, C.A.C. Kuip, Compound sets in mathematical programming modeling languages, Management Science 39 (1993) 746–756.

[7] R. Bonczek, C. Holsapple, A. Whinston, Mathematical programming within the context of a generalized data base management system, Recherche Opérationnelle/Operations Research 12 (1978) 117–139.

[8] Chesapeake Decision Sciences, Manager for interactive mod-

eling interfaces: MIMI user manual, version 3.40, Chesapeake Decision Sciences, New Providence, NJ, 1993.

[9] J. Choobineh, SQLMP: A data sublanguage for representation and formulation of linear mathematical models, ORSA Journal on Computing 3 (1991) 358–375.

[10] G.W. Cleaves, T.E. Baker, Chesapeake R&D sponsor groups, Interfaces 20 (6) (1990) 83–87.

[11] E.F. Codd, S.B. Codd, C.T. Salley, Providing OLAP (on-line analytical processing) to user-analysts: An IT mandate, E.F. Codd & Associates, 1993; http://www.arborsoft.com/papers/coddTOC.html.

[12] C.J. Date, An Introduction to Database Systems, Addison-Wesley Publishing Company, Reading, MA, 1990.

[13] G. Dutta, A multi-period optimization-based decision support system for strategic and operational planning, Ph.D. dissertation, Department of Industrial Engineering and Management Sciences, Northwestern University, 1996.

[14] G. Dutta, R. Fourer, A survey of mathematical programming applications in integrated steel plants, Technical report, Department of Industrial Engineering and Management Sciences, Northwestern University, 1996.

[15] G. Dutta, G.P. Sinha, P.N. Roy, N. Mitter, A linear programming model for distribution of electrical energy in a steel plant, International Transactions in Operational Research 1 (1994) 17–29.

[16] T. Fabian, A linear programming model of integrated iron and steel production, Management Science 4 (1958) 415–449.

[17] R. Finkelstein, Understanding the need for on-line analytical servers, Performance Computing, Chicago, 1995; http://www.arborsoft.com/papers/finkTOC.html.

[18] R. Fourer, Database structures for a class of mathematical programming models, Technical report 90-06, Department of Industrial Engineering and Management Sciences, Northwestern University, 1990; http://iems.nwu.edu/\~4er/WRITINGS/MPdb.ps.

[19] R. Fourer, D.M. Gay, B.W. Kernighan, A modeling language for mathematical programming, Management Science 36 (1990) 519–554.

[20] R. Fourer, D.M. Gay, B.W. Kernighan, AMPL: A Modeling Language for Mathematical Programming, Duxbury Press, Belmont, CA, 1993.

[21] H.J. Greenberg, Enhancements to ANALYZE: A computer-assisted analysis system for linear programming, ACM Transactions on Mathematical Software 19 (1993) 233–256.

[22] H.J. Greenberg, A Computer-Assisted Analysis System for Mathematical Programming Models and Solutions: A User's Guide for ANALYZE, Kluwer Academic Publishers, Boston, 1993.

[23] Kenan Systems Corporation, An Introduction to Multidimen-

sional Database Technology, Cambridge, MA, 1995; http://www.kenan.com/acumate/mddb.htm.

[24] D.A. Kendrick, A. Meeraus, J. Alatorre, The Planning of Investment Programs in the Steel Industry, Johns Hopkins University Press, Baltimore, 1984.

[25] C.A.C. Kuip, Algebraic languages for mathematical programming, European Journal of Operational Research 67 (1993) 25–51.

[26] M.L. Lenard, A data-model-solver interface written in SQL, MD21.2, program of the 29th TIMS/ORSA Joint National Meeting, Las Vegas, 1990.

[27] R.E. Marsten, The design of the XMP linear programming library, ACM Transactions on Mathematical Software 7 (1981) 481–497.

[28] G. Mitra, B. Kristjansson, C. Lucas, S. Moody, Sets and indices in linear programming modelling and their integration with relational data models, Computational Optimization and Applications 4 (1995) 263–292.

[29] H. Müller-Merbach, Database-oriented design of planning models, IMA Journal of Mathematics Applied in Business and Industry 2 (1990) 141–155.

[30] K.H. Palmer, Data and File Structure, in: K.H. Palmer et al. (Eds.), A Model-Management Framework for Mathematical Programming, John Wiley & Sons, New York, 1984, pp. 63–95.

[31] J. Pasquier, P. Hättenschwiler, T. Hürlimann, B. Sudan, A convenient technique for constructing your own MPSX generator using dBASE II, Institute for Automation and Operations Research, University of Fribourg, Switzerland, 1985.

[32] G. Perlman, Inside 4th Dimension, Sybex, San Francisco, 1993.

[33] M.A. Roth, H.F. Korth, A. Silberschatz, Extended algebra and calculus for nested relational databases, ACM Transactions on Database Systems 13 (1988) 389–417.

[34] S.L. Savage, M.D. Baker, Mathematical modeling databases, MD21.1, program of the 29th TIMS/ORSA Joint National Meeting, Las Vegas, 1990.

[35] G.P. Sinha, B.S. Chandrasekaran, N. Mitter, G. Dutta, S.B. Singh, A.R. Choudhury, P.N. Roy, Strategic and operational management with optimization at Tata Steel, Interfaces 25(1) (1995) 6–19.

[36] E.A. Stohr, M.R. Tanniru, A database for operations research models, International Journal of Policy Analysis and Information Systems 4 (1980) 105–121.

[37] J.D. Ullman, Principles of Database and Knowledge-Base Systems, Computer Science Press, Rockville, MD, 1988.

[38] J.S. Welch Jr., The data management needs of mathematical programming applications, IMA Journal of Mathematics in Management 1 (1987) 237–250.

![](/api/attachments/HKEV5UET/fulltext/images/87f22775fe26e5f467cd8c8d043ff934d4fd41295891ea3be476f363574c75b4.jpg)

Robert Fourer is Professor of Industrial Engineering and Management Sciences at Northwestern University's McCormick School of Engineering and Applied Science. His interests include the study of optimization algorithms and the design of computer systems to support optimization, as well as varied applications of optimization. In collaboration with researchers at Bell Laboratories, he has designed a popular computer language and system for building optima-

tion models, and is co-author of the award-winning book AMPL: A Modeling Language for Mathematical Programming. Prof. Fourier holds a B.S. in Mathematics from M.I.T. and a Ph.D. in Operations Research from Stanford. He has been a member of the Northwestern faculty for 18 years, including a six-year term as chair of the Department of Industrial Engineering and Management Sciences. He is an associate editor of the journals Management Science and Operations Research, and is a member-at-large of the Council of the Mathematical Programming Society.
