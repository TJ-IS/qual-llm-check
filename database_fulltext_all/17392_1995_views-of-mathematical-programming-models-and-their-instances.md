---
otero_id: 17392
otero_key: "SNSQVVXF"
title: "Views of mathematical programming models and their instances"
authors: "Harvey J. Greenberg; Frederic H. Murphy"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)e0029-d"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Views of mathematical programming models and their instances \*

Harvey J. Greenberg

University of Colorado at Denver, Denver, CO, USA

Frederic H. Murphy

Temple University, Philadelphia, PA, USA

Large-scale mathematical models are built, managed and applied by people with different cognitive skills. This poses a challenge for the design of a multi-view architecture of a system that accommodates these differences. A primary objective of mathematical modeling is providing insights into problem behavior, and there are many constituencies who require different views for different questions. One constituency is composed of modellers who have different views of basic model components. Another constituency is composed of problem owners for whom models are built. These two constituencies, which are not exhaustive, have significantly different needs and skills. This paper addresses this issue of multiview architecture by presenting a formal framework for the design of a view creation and management system. Specific views we consider include algebraic, block schematic, graphic, and textual. Both form and content are relevant to view creation, and the merits of views are determined by their value in aiding comprehension and insight. The need for a central, formal structure to create and manage views is demonstrated by the inadequacy of direct mappings from any of the popular systems that are typically designed to support only one view of linear programming models and their instances.

Keywords: Linear programming; Mathematical programming; Large-scale systems; Structured modeling; Computer-assisted analysis; Graphics; Natural language discourse; Modeling languages

## Introduction

Different people need different views of a model and of what it represents, each view having its own cognitive value for acquiring insight and understanding. The purpose of this paper is to clarify the meaning of views, formalize their definitions, and present an information structure to support a multi-view architecture. As part of defining the architecture, we identify some of the functions of a multi-view management system for mathematical programming, with a focus on linear forms.

![](/api/attachments/SNSQVVXF/fulltext/images/3d034bbd88d15e95515744d868a46e4e5fa15743af95cc488864f9ed832f7213.jpg)

Harvey J. Greenberg received his B.S. in Industrial Engineering from University of Miami (1962), and his Ph.D. in Operations Research from The Johns Hopkins University (1968). He is presently Professor of Mathematics at The University of Colorado at Denver, and was formerly with the U.S. Department of Energy (1976–83). Dr. Greenberg directs a project to develop an Intelligent Mathematical Programming System, sponsored by a consortium of companies. As part of that research, Dr. Greenberg developed the ANALYZE system, which gives intelligent support for analysis of linear programs, and for which he received the first ORSA/CSTS Prize for Excellence in research in the interfaces of operations research and computer science (1986). He has also received two research awards from CU-Denver (1988 and 1992). Dr. Greenberg has numerous publications, and he was the founding editor of the ORSA Journal on Computing.

![](/api/attachments/SNSQVVXF/fulltext/images/6eccb38acbfd5a377422e47a0ad93f1677d8cacf044518dd5e8dc6b220645121.jpg)

Frederic H. Murphy is a professor in the Management Science / Operations Management Department in the School of Business and Management at Temple University. Prior to joining Temple, he was with the U.S. Department of Energy. He received his B.A. in Mathematics and his Ph.D. in Administrative Sciences from Yale University. He has published in the areas of mathematical programming, dynamic programming, energy policy, energy modeling and game theory. His current research interests are in decision support for modeling and managing modeling systems. He is currently the editor of Interfaces and contributing editor to International Abstracts on Operations Research.

First, we illustrate some of what we mean by views of models and instances by showing some for the familiar capacitated transportation problem. Then, we define some basic terms and concepts, starting with a working definition of a model and of views. We define certain kinds of views in terms of both form and content.

Second, we formally define and illustrate specific views, associated with linear programming models and their instances. This is done in successive sections, beginning with views of the fundamental elements of any model: objects and relations among the objects. This also serves to reinforce some basic terms and concepts. Then, familiar views of model structures are formalized in order to define precisely what is needed to create them.

After we have described specific views and indicated some formalism in their definitions, we define mappings to illustrate how one might go directly from one view to another, and the difficulties that arise with current systems that represent only one view. In particular, we consider how to map information that supports an algebraic view to that which supports a block schematic view, and conversely. We demonstrate that, for some linear programming models, the information contained in one view lacks information needed to construct the other. This sets the stage for the more general formal development that follows, and it raises issues concerning operations on views.

Following through with operations on views, we describe zooming, condensing and switching operations. The notion of zooming and condensing is a standard one; however, we introduce the specification of zooming and condensing models that accompany a view. Their purpose is to give an adaptive quality to view management. Switching views is shown to be a 2-step process, even though an observer might see it as one operation.

Special attention is then given to structured modeling for two reasons. First, it is a fundamental approach to model description; and, second, it contains another view, called an outline. We augment SM in several ways after describing why its current form is not designed to support all views of interest.

Building on the concepts that grow from specific view analyses and from the formalism introduced, we move towards a more general formalism. First, we present a formal description of a multi-view architecture. Second, we present a central information structure that is, itself, a formal description of models and their instances that supports all of the views we consider. Third, we move to a higher level of formalism by defining views in terms of information they must access. The completeness of this higher level formalism is an open issue, but it reinforces the proposed scope information structure that goes beyond the specific views we shall describe.

While a multi-view architecture has been discussed by some, only Baldwin's thesis [3] (see also [4, 7, 5, 6 and 8]) has gone deeply into this, including a prototype system, called DOVE (Developing and Organizing Views for Examination). Baldwin's formalism is similar to that of Garlan [24], although Garlan's stems from different considerations.

Much can be said about developments in relational database theory, but the issues in defining views in a relational database are very different (some interesting connections are given in [19]). Garlan [24] elaborates upon this. Also, Farn's thesis [22] shows how structured modeling contains the expressiveness of relational database theory, and we shall give special attention to structured modeling.

It is perhaps interesting to note that recent comparative analyses of a modeling language's expressiveness, such as the studies in [56] and [45], have not considered view creation in their evaluations. This is because there is not yet a fully implemented system to support a multi-view architecture, and the difficulties with presenting one view from information stored to support another have not been surfaced. That is one of the primary objectives of this paper: to understand more precisely the issues with view creation and management. In addition, we initiate a formalism based on a foundation of information access.

## 1. Terms and concepts

Before formalizing model elements and views, consider some representative views of the familiar capacitated transportation problem. Figure 1 gives some model views, the first three of which were generated by MODLER [39], which is a modeling language for linear (and integer) programming. Figure 1-a is one of the algebraic views; 1-b is the associated block schematic view; and, 1-c is an activity I/O view. The I/O for the transportation activity consists of one input, which is its supply equation coefficient, and one output, which is its demand equation coefficient.

The other three views, which were not created by MODLER, offer different insights into the model structure. Figure 1-d shows a netform. Because this is a network model, each activity has only one tail and one head. More general netforms are presented later. Figure 1-e shows a condensed form of the activity-constraint digraph. It presents the activity I/O view with diagrammatic graphics; its relation to the netform is described later. Figure 1-f shows a graphic view of activity I/O, generated by LPFORM [61] (subordinate screens exist to provide associated text information). Figure 1-g shows a structured modeling genus graph. This shows (hierarchical) dependency relations among all of the objects in the model.

Associated with a model are many instances, each determined by assigning particular members to sets and numerical values to parameters and tables. When all data objects have been assigned values, the model is said to be instantiated – that is, an instance is created. In Figure 2, some instance views, created by ANALYZE [40,42], are illustrated. In 2-a, an equation listing and bounds display give an algebraic view of this instance. In 2-b, a schema view is shown; upon comparing this with the block schematic view in 2-b, we can see that the range of the SUPPLY and DEMAND table entries is in the interval [50,100]. Similarly, the range of entries in table TRANCOST for this instance is [1,10], and in table CAPACITY, it is [50, ∞) (where \* denotes ∞ in numeric displays from ANALYZE).

Figure 2-c shows a syntax view. This is a description of the row and column classes, generated by MODLER, to provide English translations of rows and columns in each instance.

Figure 2-d shows a picture of the matrix, which provides a view of sign patterns. This also relates to the activity-constraint view, using the boolean image as an adjacency matrix of the fundamental bigraph, which we shall describe later.

The view in Figure 2-e is equivalent to the activity-constraint I/O view for the instance, which one might compare with its condensed form in 2-e. In 2-f, the row digraph is shown, which provides a view of flows from supply to demand. The form shown uses the row syntax to translate the regions associated with S and D rows, respectively (after projecting the fundamental digraph in 2-e).

![](/api/attachments/SNSQVVXF/fulltext/images/80481b3d6ba0cc3ee31535fbdfedcd4c48270499509d691b701f9356e8c26a4e.jpg)  
(c) An Activity I/O View  
Fig. 1. Some model views of the capacitated transportation problem.

The views in the above two figures are representative, but not exhaustive, of the multi-view architecture described here. To formalize these notions, we begin with some basic terms and concepts.

An instance is defined by the LP bordered matrix (A, c, $L_{R}$ , $U_{R}$ , $L_{C}$ , $U_{C}$ ), generated from the model's logic and assignments of values to data objects. The LP is:

$$
\text { optimize } \mathrm{c} x: \mathrm{L} _ {\mathrm{R}} \leqslant y = \mathrm{A} x \leqslant \mathrm{U} _ {\mathrm{R}}, \mathrm{L} _ {\mathrm{C}} \leqslant x \leqslant \mathrm{U} _ {\mathrm{C}}.
$$

Let M be an m×n matrix in what follows. Associated with M is its handle. This consists of names for its rows and columns, which contain information about their meaning. This information can be obtained by a direct decoding of the names by some rule that corresponds to their encoding, or the information about the rows and columns can be obtained indirectly by associated links into a property list or semantic network.

Pictures. A picture is a qualitative view of the nonzeroes in a matrix. One picture of a matrix is at the pixel level, such as in MatVu [85] and SMMS [1].

Another picture of M is a view of the sign pattern, as in Figure 2-d. Only the sign (+ or -) of each nonzero of M is printed in a cell, and a zero appears as a blank. This is the view in ANALYZE, and other picture views are possible, such as color-coding the cell entry to convey the magnitudes of the nonzeroes.

Blocks. Rows and columns of M can be grouped into blocks. In this view, row names are replaced by row block names, and column names are replaced by column block names. The formation of the block names can be determined by how the blocks were created, such as categories in an embedded structure, or they can be composed from a string syntax from the member names. Each cell entry describes the contents of the submatrix defined by the associated row and column blocks. A blank means the submatrix is null – that is, all of its coefficients are zero.

![](/api/attachments/SNSQVVXF/fulltext/images/3b699ad5aed15586fbfd8a956f7ae2ca924c30f330372db97ae24e67a995c90c.jpg)  
Fig. 2. Some instance views of the capacitated transportation problem.

Block views arise in a variety of ways. In ANALYZE, the most common way is from procedures, such as looking for components of the matrix, for redundancies, and for other partitions that support analysis.

Matrix schema. A matrix schema has the same form as the block schematic, except the cell entries give information about the model instance contained in the nonzeroes in the matrix. As illustrated in figure 2-b, the ANALYZE schema view of an instance has the following meaning. Each row class, including the objective, forms a row strip, presented with the class name and domain. In addition, special row strips are added to represent lower and upper bounds of activity classes. Each column class forms a column strip, presented with the class name and domain. In addition, there is a column strip to represent the limits associated with each row class.

A cell entry in the ANALYZE matrix schema shows the range of the nonzeroes in the associated submatrix. If the submatrix is null, a blank is shown; otherwise, a numerical range is given.

Graphic views of instances derive in natural fashion from the fundamental graphs. Figure 2-e illustrates a row digraph, combined with syntactic translation, to give a view of flows from supply locations to demand locations.

What is a model? At the simplest level, a model is a collection of objects and relations among these objects [17]. This is where universal agreement of what a model is stops. What are the objects and relations, for example, is a question that one must answer.

![](/api/attachments/SNSQVVXF/fulltext/images/0f5c669f0f8e2382c12b28df24b3ba7acc220613c31be29788d015d8bd27a83b.jpg)  
Fig. 3. An anatomy of a mathematical programming model.

The simulation community has tackled this question with objectives similar to those of this paper. In particular, Nance [71,72] gives a succinct survey of views about models from the vantage of simulation. The simulation perspective is useful for our objectives, but it is oriented differently and does not capture some of what we do in mathematical programming.

In mathematical programming, recent language developments have created pertinent research activities, such as those of Meeraus [64], Fourer, Gay and Kernighan [23], Greenberg [39], Murphy and Stohr [68] and others. Geoffrion [26–29] developed a formal approach to model description, called structured modeling (SM), which we shall consider in detail.

Figure 3 shows an anatomy of a mathematical programming model, which underlies the design of MODLER. We note the incompleteness of this diagram. For example, nonlinear functionals are needed for full expressiveness, and semantics are needed for some views. If these were added to the diagram, they would appear lateral to objects and relations. This linguistic incompleteness aside, the diagram contains the primary ingredients for modeling in linear programming.

Note that sets are defined as data objects (see [32] for an insightful discussion). In this regard, assigning members to sets is as much a data issue as assigning numerical values to parameters and tables. There are, however, some differences in these two types of data objects besides the distinction of symbolic versus numeric. What is important for now is to recognize their similarity in the context of separating model description from an instance of the model.

A set can be explicit or implicit. An explicit set is primitive, and its members are declared by a list. An implicit set is dependent on other sets, such as a union, and it is instantiated once the sets it depends upon are instantiated. Similarly, a table can be explicit or implicit, the former standing on its own and the latter in terms of other tables, such as a simple sum. Details of these structures are given in the MODLER primer [39] (see also [41]).

One also needs a way to place conditions on the realization of members in object classes. A generation condition specifies conditions under which a member of a decision object class or a constraint class is generated for a particular instance. For example, one may specify that a transportation activity from a supply to a demand region exists only if the associated supply and demand values are positive. An admissibility condition specifies conditions under which a data object class admits realizations, such as simple numeric ranges for parameters and tables.

Following Nance [71], we say a model is a collection of objects and relations among them; and, we say an instance of a model is the assignment of values to all data objects. There is, however, another specification, pertaining to the roles of objects and relations.

For example, suppose COST and PROFIT are two equations in the model. Let us consider two different roles for these objects. First, suppose the model describes goals or constraints of the form COST ≤ c and PROFIT ≥ p. If we vary c and p from one instance to another, we do not regard this as a change in the model; they are simply different instances of the same model. Second, suppose these inequalities are not present, and in one instance we want to MINIMIZE COST and in another we want to MAXIMIZE PROFIT. Are these two instances of the same model, or are they different models, owing to the different roles of COST and PROFIT?

In answer to this last question, role assignments could be regarded as part of the model or as an instance. Modeling languages, including the very generic SML [30] and SQLMP [17], do not distinguish the role of objects and relations as part of the model, and it becomes unclear whether they should. Although some advocate specific modeling practices, this is actually a matter of style. View management must respect differences in styles.

In SML, where the term attribute means a specific type of object, a particular attribute could be a variable in one application, and the same attribute could be a parameter in another application. The SML design requires a change to the model even though one might consider this to be an instance of the same model. In SM (not the particular language, SML), one could steer away from variable attributes altogether and relegate the role specification to a problem description language that takes SM input. SQLMP has added an operation, called CONSTRAINT, to SQL, but an equation could be a constraint in one application and not in another. Such roles could be treated as instances of the same model by use of the equivalent of an SQL SELECT function.

In algebraic languages, like AMPL, GAMS, LPL and MODLER, each object must be defined as part of the model description. Role assignments cannot be postponed. In analyzing the pooling problem, for example, Lodwick [59] changed the GAMS code simply by changing a variable to be a parameter. Although this was easy to do, it raises a question about extending modeling languages for mathematical programming to allow an object to be declared while postponing its role.

This added level of specification to declare roles is important for view creation. Ideally, we want a high-level model description, like SM, but with the same host system supporting problem specification. This is between a model description and an instance, where only roles are defined, not the data. A view, therefore, can be created for a particular role assignment, or without role assignments at all. (In general, views do not depend upon complete specification of anything. The model, itself, can be only partially defined; some data can be in place, while others are not. Similarly, roles can be completely assigned, partially assigned, or not assigned at all.)

A way to consider the relations among model description, problem specification and instantiation is shown in Figure 4.

What this flow suggests is that the model description is the most fundamental representation of a system, with the other levels adding greater specificity. From a model description a problem can be specified and data values can be assigned. Instantiation can begin with either a model description or a problem specification (which receives a model description). It then assigns all data values to prepare an instance for optimization.

![](/api/attachments/SNSQVVXF/fulltext/images/e2bd691e59381e8168b038a15a1d211fb71fd3c81fe0daea2ebd705532668a8f.jpg)  
Fig. 4. Levels for view creation.

This hierarchy is not a procedural recipe. In many situations, modeling is not top-down (or bottom-up); it is more like middle-out. The host system, which supports view creation, must allow partial specifications at all levels.

What is a view? Roughly, a view is a representation that enables a presentation of information that is designed to adapt to the cognitive needs of the modeler and the model's constituency. The actual presentation is called a display, which depends upon hardware devices. Thus, a view is more abstract in principle than a display; for example, a diagrammatic graphic view can be represented by a node-arc incidence matrix with associated mappings, like labels. The display manager takes this as the view and proceeds to present the graph in some form. The form of display can require algorithms to enhance the display $[84,65,62]$ . A system needs to provide all of the different views that can aid a modeler or a constituent on demand.

Further, although we examine views as an output, clearly every modeling system assumes a view for its input specifications. Some are algebraic, some are block schematic, and some are graphic. Technically, there is no need to distinguish whether a view is presented as an input or an output specification. As we shall demonstrate, however, a particular view of a model used as a model specification can run into problems when it attempts to create a view that is different from its input.

Further, the views supported during modeling must be consistent with those supported during subsequent analysis, for which the model is built in the first place. Bearing in mind that views are independent of hardware devices, we can, and shall, define those views that should be intrinsic in the system. Murphy, Stohr and Asthana [69] have already contrasted some of the views we consider: algebraic, matrix, block schematic, activity-constraint digraph, netform, structured modeling SM graphs, and iconic.

A view can be distinguished by what is to be viewed (i.e., content) and how it is to be viewed

(i.e., form). Here is one outline to illustrate the distinction.

<table><tr><td>Form:</td><td>Content:</td></tr><tr><td>Primitive</td><td>Primitive</td></tr><tr><td>Algebraic</td><td>Objects</td></tr><tr><td>Tabular</td><td>Relations</td></tr><tr><td>Schematic</td><td>Processes</td></tr><tr><td>Graphic</td><td>Problem</td></tr><tr><td>Text</td><td>Attributes</td></tr><tr><td>Dynamics</td><td>Dependencies</td></tr><tr><td>Static</td><td>Explicit</td></tr><tr><td>Recursive</td><td>Implicit</td></tr><tr><td>Animated</td><td>Aggregates</td></tr></table>

The primitive forms divide into types, which can be mixed in a view. For example, a graphic can be iconic or diagrammatic. Text could be natural language or computer language. A view can have a mixture of algebraic equations, graphics and text. It is possible to assume some primitives, but even if a view, or its basic ingredients, are primitive, some familiar specifics need to be described to distinguish a view from other objects in the universe, like a zebra. This is, in part, the purpose of the next few sections: use familiar views to convey what we think a view is. As we build up the formalism, we shall see that form and content are not the only ingredients needed to define a view.

One subtle note in the formal development is the distinction between a model and its instances. The discussion about roles arises because some consider certain roles as instances of the same model while others consider them as changes in the model (c.f., the example of COST and PROFIT equations). More generally, a view manager must be able to perform view creation for a model, for problems specified from a model, and for one or more instances of the model.

In addition, there must be some way to distinguish whether a particular relation is part of the model or whether it is particular to the instance. For example, suppose A and B are two sets, and A = B. There is a difference as to whether this equality is part of the model description, or whether the two sets are equal only in this instance.

Another dimension to view management is the purpose of the view. In many cases the purpose is to give insight into a model's structure. For some people, an algebraic view offers the best insight, for others a process network is a better view, and still others see an (SM) outline view as the most informative way to see the structure of a model.

There are, however, other purposes of views, such as insight into the behavior of a model. In some cases, such insight needs views of many instances. In other cases some behavioral properties can be inferred qualitatively, even from a high-level model description. One example is the model's connectedness.

Another purpose is to support model management, which needs certain views beyond just structure and behavioral properties. An example is dependency information about objects and relations.

## 2. Views of objects and relations

Let us begin with fundamental objects and relations that (partially) describe a linear programming model. First, we consider views of sets. Then, we illustrate basic relations in a model description: constraints and conditions.

A fundamental object is a set. A domain is a restricted cross product of sets that is bound to another object. This is a primary difference between a domain and a set: a domain is bound to other objects, such as an activity class, while a set can stand on its own. We can ask for a view of all activities with a given domain, but we cannot ask for all activities with a given set. In the latter case, “with a given set” is ambiguous. For example, the set could appear in the activity’s domain, or it could appear in a condition for generation. This ambiguity does not arise with a domain specification because its binding to the activity is precise. More generally, a domain is the domain of something, which forms an unambiguous binding, while a set is an entity that need not be bound to anything.

Of course, we expect a set to be bound to something, but during model debugging this need not be the case, and a view about the set can be a debugging aid when no dependency is noted. In general, it is useful to think of some objects that depend on domains as having an indirect dependency on the sets upon which the domain depends.

A domain restriction could be specified in a number of ways, some reflecting model logic and some data-dependence. For example, suppose T is a set of time periods, S is a set of supply regions, and D is a set of demand regions. The following domains illustrate restrictions that reflect the model logic: $d = \{(t, t') \text{ in } T \times T: t' < t\}$ and $d = \{(s, d) \text{ in } S \times D: s \neq d\}$ . The following domains illustrate restrictions that are data-dependent: $d = \{(t, t') \text{ in } T \times T: t' = t + LAG\}$ , where LAG is a parameter, and $d = \{(s, d) \text{ in } S \times D: LINK(s, d) = 1\}$ , where LINK is a control table (more on those later).

Sets are typed in a variety of ways. First, a set can be ordered, partially ordered, or unordered. An ordered set is called a sequence. There are two types of sequences: terminal and cyclic. A terminal sequence is isomorphic to integers, such as time periods in a time-staged model. A cyclic sequence is where every member has exactly one predecessor and exactly one successor; this is isomorphic to N integers with predecessor(i) = j if, and only if, successor(j) = i. We call N the length of the cycle. A terminal sequence is totally ordered – that is, every pair of members is related by the order relation. A partially ordered set arises in project scheduling, where there are precedence relations between some pairs of jobs.

Second, a set can be attributed or not. If a set is attributed, we refer to its attribute. Examples of attributes are form, time and place. A set of form, which can be physical (eg, cars) or conceptual (eg, information), must have units of measurement (eg, mass, volume, number); a set of time must be ordered; and, a set of place must have spatial properties, like distances between members. (These are properties of form, time and place, as illustrated here, but other properties could be assigned in other cases.) The significance of attributed sets is that certain views can be created from properties, which can be from inheritance, that reflect restrictions on set relations and operations. In MODLER, for example, two attributed sets are conformal if they possess the same attributes. A set relation, such as the subset, and a set operation, such as the union, are restricted to be conformal. A modeling system can assume the convention that two non-attributed sets are always conformal.

An attributed set and one that is not attributed may, or may not, require a conformality resolution rule. For example, suppose $A = T \times S$ , where T is ordered and S is not. If it is irrelevant whether A is ordered – that is, ordered relations are never used with A – no conformality between T and S is necessary, and A is not attributed. If, however, A needs to be ordered, a conformality resolution rule is needed to order A. A default rule would be to use the order of T and assign an ordering to S, relative to its relation to A. The order of a cross product of two ordered sets is defined to be their lexical ordering (so the ordering of T × S is not the same as the ordering of S × T). Following Nance [71], this relative ordering of S is defined by a relational attribute of S with respect to A; whereas the attribute of time assigned to T is an indicative attribute because it is a property of the object, T, itself.

The particular attributes of form, place and time apply directly to product distribution problems, but their abstractions apply to other situations. Moreover, there can be other types of sets – that is, attributed with other properties. For example, a set of jobs is none of these three basic types, but some other attribution enables views associated with activities that transform one job into another. This notion of activity transformation offers valuable insights, so we elaborate.

To illustrate the significance of set attribution, consider the example $[40,42]$ in Figure 5. This submatrix, whose picture is from ANALYZE, represents a trace of flow for unleaded regular gasoline, and a view of flows is requested.

Figure 6 shows the row digraph for this submatrix, using the syntax to translate each row into English. The first entry is the arc from row BH.11, which translates to 'heavy crude in Texas at 1st time period', to row BRF11, which translates to 'raffinate in Texas at 1st time period'. This arc is due to the operation activity, O0111, which operates a primary unit in Texas at the first time period. This operation activity uses heavy crude as an input and produces raffinate as one of its outputs. The second arc comes from the fact that this same activity also produces unleaded mid grade as another output.

![](/api/attachments/SNSQVVXF/fulltext/images/5cfc251901ccdcdc8321f963525d12a2debca2e3f1041493b635c79358aacde7.jpg)  
Fig. 5. A picture of a submatrix in an instance of a blending model.

```txt
ROW DIGRAPH
heavy crude in Texas at 1st time period
    ---->raffinate in Texas at 1st time period
    ---->unleaded mid grade in Texas at 1st time period
raffinate in Texas at 1st time period
    ---->raffinate in Texas at 2nd time period
    ---->unleaded regular in Texas at 1st time period
raffinate in Texas at 2nd time period
    ---->raffinate in Texas at 3rd time period
    ---->unleaded regular in Texas at 2nd time period
raffinate in Texas at 3rd time period
    ---->unleaded regular in Texas at 3rd time period
unleaded regular in Texas at 1st time period
    ---->unleaded regular in Louisiana at 1st time period
unleaded regular in Texas at 2nd time period
    ---->unleaded regular in Louisiana at 2nd time period
unleaded regular in Texas at 3rd time period
    ---->unleaded regular in Louisiana at 3rd time period
```  
Fig. 6. Row digraph of submatrix in Fig. 5 with English translations of rows.

In general, each operation activity in Figure 5 (which begins with O) is a transformation of form – that is, it has some material as an input and produces another material as an output (a primary unit uses crude oil as an input and produces some final product as well as blend stocks; a blend unit uses blend stocks as inputs and produces some final product).

An inventory activity (which begins with I) is a transformation of time – that is, it has some time period as an input and produces the same material at the same location in the next time period as an output. The next arc is due to inventory activity, IRF11. This links row BRF11, which translates to 'raffinate in Texas at 1st time period', to row BRF12, which translates to 'raffinate in Texas at 2nd time period'.

A transportation activity (which begins with T) is a transformation of place – that is, it has some region as an input and produces the same material at the same time period at another region as an output. The activity TUR121 transforms the location of unleaded regular in Texas at 1st time period to Louisiana. Graphically, this links row BUR11 to row BUR21, as shown in Figure 5, which is translated in Figure 6.

These transformations of form, place and time, which were introduced by Murphy and Stohr [68], can be delineated by using set attribution (which was done with MODLER). Figure 7 shows the results. Notice the headers that are formed for sets that do not change – that is, the activities do not transform their values in the subgraph delineated by the attributes.

The row digraphs in Figures 6 and 7 offer a vantage different from the picture in Figure 5. They show flows that help an analyst gain insight from the trace. Although the example shows each activity as a transformation of only one indicative attribute, an activity could transform more than one. For example, an activity can represent conversion of materials (form) that changes its location (place) and puts into stock for future availability (time). Another example of multiple transformations is in changing age class while carrying an inventory [25].

Whether or not a particular modeling system recognizes indicative attributes, like form, time, and place, and how such recognition might be used, are not of direct concern. What is at issue is that views can be created from such attributes or from their properties. The above example demonstrates that there is value in specifying view contents by attributes and inherited properties of attributes, such as delineating activities by what they transform.

Now we continue with another type of relational attribute, namely that an element to which a domain is bound can have a role. In the example of $T \times S$ , ordering can be irrelevant, or it can be necessary. This is determined by the role of this set as a domain. The attribute of order is inherited from the objects to which the domain is bound.

![](/api/attachments/SNSQVVXF/fulltext/images/5f857fd1ed911b419b0c7377ab06eef0454165a2294cff97c869d7ef8c706755.jpg)  
(c) Time  
Fig. 7. Delineating form, place and time for row digraph displays.

![](/api/attachments/SNSQVVXF/fulltext/images/02aae660ecc2503c85f1728950d065652def8d5fe4958c9865b94aeadbc546ae.jpg)  
Fig. 8. A display of the view of the sets and domains in Table 1. (Legend: () sets; S [] dependencies, D.)

One view of sets and domains is with the following conceptual graph [80]. Let S be the collection of sets and domains in a model, and let A be a collection of attributes. Define the label function, $\lambda:S\to A$ , and let $S_{\lambda}$ denote the associated, labeled nodes. Now let D be the collection of set and domain dependencies. For example, $D=\{union, product, conditional-union, \ldots\}$ . A set is explicit, or primitive if its definition does not depend on any other object; otherwise, a set is implicit, or derived. All domains are considered here as derived sets.

For each derived set, define incident arcs as follows. Let $s = d(p)$ define set s by the dependency $d \in D$ in terms of sets $p \in S_{\lambda}$ . (We call p the domain of dependency of s.) Define a node labelled by d (repeated labels from D can occur). Then, define arcs $\langle d, s \rangle$ and $\langle p_i, d \rangle$ , where $p = (p_i)$ . We now have a fully labelled bipartite digraph, which is a conceptual graph. Figure 8 illustrates a view of the full conceptual graph of the specifications in Table 1.

Note that a source node in the conceptual graph must be a set node (S), which is primitive – that is, it depends on no other set. In general, the conceptual graph of sets and domains reveals dependencies, which can be extended to other views, such as of data objects over domains.

Views of data have received an incredible amount of attention, even before computers. Statisticians have devoted much design effort to forms of views, which is well summarized by Tufte [86]. Modern statistical views draw heavily from graphics, and much attention has been devoted to creating views for data with high dimensionality (see, for example, Cleveland and McGill [18]).

<table><tr><td colspan="3">Some sets and domains</td></tr><tr><td>unordered</td><td>A</td><td>primitive</td></tr><tr><td>unordered</td><td>B</td><td>primitive</td></tr><tr><td>unordered</td><td>C</td><td>primitive</td></tr><tr><td>ordered</td><td>a = 1, ..., horizon</td><td>primitive</td></tr><tr><td>unordered</td><td>D = A + B + C</td><td>union</td></tr><tr><td>unordered</td><td>E = C * D</td><td>product</td></tr><tr><td>unordered</td><td>F(A,D) = E + D: f(A,D) = 0</td><td>conditional union</td></tr><tr><td>semi-ordered</td><td>G = C * a</td><td>product</td></tr><tr><td>ordered</td><td>H(a) = a * a&#x27; : a&#x27; &lt; a</td><td>conditional product</td></tr></table>

Now consider views of model relations. The two fundamental types of relations are constraints and logical conditions (c.f., Figure 3).

There are two primary ways to view constraints: as dependency relations and as model structures. Dependency relations include the calling sequences of Geoffrion's structured modeling approach to model description. Since both of these are examined in greater detail, we consider only logical conditions here.

There could be logical conditions about each object. A decision object with a domain $d = s_{1} \times s_{2} \times \ldots \times s_{\lambda}$ might be restricted by a logical relation, such as $T(d) > 0$ , where T is a data object with domain d. Such a logical condition restricts a particular activity, for a member of d, to be generated only if this instance of the associated data value in T is positive. Conditional generation of decision objects is one type of logical condition. Similarly, conditional generation of constraints in the mathematical program is another. As before, our concern is not so much with the linguistic aspect as with views about semantics applied with the language.

A logical condition of generation can either be data-driven, as in the above example, or it can be part of the model specification - that is, the condition can be independent of particular instances defined by data. One example is a relation between two ordered sets, as follows. Suppose we want to express the inventory carried from period t to period $t + h$ as the decision object (variable) $I(t, t + h)$ . Abstractly, if there is one (ordered) set called T, which represents time, the domain of I is $T \times T$ , but with the logical condition: $dom(I) = \{(t, t') \in T \times T: t' = t + h\}$ . When h is a constant (like 1), this domain is data-independent; when h is a parameter (like a lag, which could vary over instances), this domain is data-dependent.

Logical conditions also apply to data objects, but with a different meaning. If T is a data object with domain d, a logical condition, say $L(\mathbf{P}(T), d)$ , is a logical expression that depends on predecessor data objects, $\mathbf{P}(T)$ , and on the domain, d. L describes conditions on T to be admissible. Its primary purpose is to serve as a model management aid, but the information about admissible data values can be used for other functions, such as model simplification. One example of such a logical condition is: $T(d) \geqslant 0$ for all members of the domain, d. Putting syntax of specification aside, this says that each value of $T(d)$ must be nonnegative. Note that if $T(d) > 0$ appears as a logical condition attributed to the data object T and as a logical condition attributed to the decision object $X(d)$ , the latter is a redundancy that could signify a modeling error. That is, the first appearance of this logical condition has the meaning that the only admissible values for T are positive real values. The second appearance has the meaning that activity X is generated for every member of the domain d for which $T(d)$ is positive. The generation condition is always satisfied for every instance and is therefore redundant. Such redundancy can be revealed by a view of the logical conditions.

A view of logical conditions can be a simple list of them, but some sorting is appropriate, especially to see hierarchical dependencies. A condition for generation can depend upon a data object that is bound to a logical condition that depends upon other data objects, and the view can reveal this dependency chain. Common ancestors or successors give other views of logical conditions, taken in conjunction with objects – that is, two views combined. Such a view presents an implicit connection between two decision objects that have a common ancestor or successor in the logical condition dependency hierarchy.

For example, suppose the generation of a flow variable between two locations depends upon having a positive production capacity in the first location and a positive demand in the second. The capacity and demand are data objects, and the specification may be: FLOW(s,d): CAP(s) > 0, DEM(d) > 0.

Now suppose there are other specifications:

DATA OBJECTS

CAP(s): [10,100]

DEM(d): {1,10,20}

DECISION OBJECTS

PROD(s): CAP(s) > 0

FLOW(s,d): CAP(s) > 0, DEM(d) > 0

A view of the logical conditions reveals that those on the decision objects are redundant. The condition for CAP is that the capacity in each supply region (s) is in the interval, $[10,100]$ , so $\mathrm{CAP}(s)>0$ always. Similarly, the condition for DEM is that the demand in each demand region (d) is either 1, 10 or 20. Thus, $\mathrm{DEM}(d)>0$ is redundant. (Note: the square brackets, $[10,100]$ , denote an interval, and the curly brackets, $\{1,10,20\}$ , denote a list.)

The view of logical conditions can reveal a specification error. Seeing a redundancy is a way of detecting a possible error. In large models, relations among logical conditions and objects can be subtle. Projection operations can reduce the view. For example, suppose the full view of the above example is given diagrammatically:

$\{[10,100]\} \leftarrow [CAP] \leftarrow \{CAP > 0\} \leftarrow (PROD)$

{1,10,20} ← [DEM] ← {DEM > 0} ← (FLOW)
Legend: [] Data object, () Decision object, {} Logical condition. (The orientation is in the direction of dependency.)

Replicated conditions appear only once, such as $\{CAP > 0\}$ .

The arcs in this dependency digraph are defined by the previous specification. For example, the arc from (PROD) to $\{CAP > 0\}$ means that the activity class, called PROD, has a condition for generation, namely that the associated value of data object CAP be positive. The association is the common domain. In turn, the condition represented by the node $\{CAP > 0\}$ depends on the data object, CAP, so there is an arc showing this dependency. The data object, CAP, has an admissible range, specified as the interval [10,100], so there is an arc from the data object node, [CAP], to the logical condition node, $\{[10,100]\}$ , which represents this dependency.

The following projection of this dependency digraph eliminates the logical conditions to reveal dependency relations between decision objects and data objects.

[CAP] ← (PROD)

![](/api/attachments/SNSQVVXF/fulltext/images/117a99e98f9a4537dbd9da3bc825d754ab27a02e347d4b51e92045330f029f5d.jpg)

[DEM] ← (FLOW)

This establishes that decision node (PROD) has an implied dependency on the data object node, [CAP]. This was obtained by the projection operation because there is a path from (PROD) to [CAP] via the logical condition node, $\{CAP > 0\}$ , which was eliminated in forming the projection.

A common successor projection produces a view that relates the decision objects, PROD and FLOW:

(FLOW) $\longrightarrow$ [CAP] $\longleftarrow$ (PROD)

produces (FLOW) — (PROD)

Depending upon the modeling language and the style of the modeler, logical conditions can come in different forms. Besides logical expressions of the form, data-object relation data-object, one can specify control tables. For example, suppose LINK(s, d) is a control table that has binary values, 0 and 1, to represent the absence or presence of a link, respectively, between a supplier (s) and a demand location (d). This table can appear in a logical expression or simply as a coefficient of a flow activity in a summation. The view manager can include control tables as another way of presenting a view of logical conditions if such tables are distinguished from other types of data tables.

## 3. Model structure views

There is an inexhaustible number of ways to view a model's structure. Here we describe three: algebraic, block schematic and graphic. Later, after considering the role of structured modeling, we consider another view of a model's structure, called an outline.

What distinguishes an algebraic view from other views is that an algebraic view presents equations that relate decision and data objects over domains. Optionally, this view begins with definitions of objects, such as Let $x_{ij} = flow$ from i to j.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Object definitions:
Let I = set of supply locations.
Let J = set of demand locations.
Let  $C_{ij}$  = unit cost of flow from i∈I to j∈J.
Let  $U_{ij}$  = capacity of flow from i∈I to j∈J.
Let  $S_i$  = quantity of supply at i∈I.
Let  $D_j$  = quantity of demand at j∈J.
Let  $T_{ij}$  = flow from i∈I to j∈J.
Model:
minimize  $\Sigma_{ij}$ $C_{ij}T_{ij}$  subject to:
 $\Sigma_{j}T_{ij} \leq S_{i} \quad \forall i\in I$ $\Sigma_{i}T_{ij} \geq D_{j} \quad \forall j\in J$ $0 \leq T_{ij} \leq U_{ij} \quad \forall (i,j)\in I\times J$
</div>

Fig. 9. An algebraic view of the capacitated transportation model.

Each equation has the form:

$$
\begin{array}{r l} \mathrm{E} [ (d) ] & = \text { expression } [ \text { relation   data - expression } ] \\ & [: \text { condition } ] [ \text { for   restriction } ]; \end{array}
$$

where E is the name of the equation and d is its domain, if it has one. Languages differ in their definitions of the objects (in italics) in the equation. Our purpose is only to understand the requirements to create an algebraic view, so we leave open how these objects are expressed linguistically.

Figure 9 presents the capacitated transportation problem in pure algebraic notation. By pure, we mean free of linguistic limitations, such as restriction to keyboard characters. This is fairly close to how MODLER lists a model (c.f., Figure 1-a), particularly if one adds a display command to view the object definitions. Counterparts exist in algebraic languages like AMPL [23], GAMS [12] and LPL [47]. Our interest is in describing views, rather than how they would be displayed. Hardware (including keyboards) can limit the display of the view, but this is ancillary to the mainstream of view definition.

What the view must specify, as input to a display manager, is: (1) it is algebraic, and (2) information about the equations. Broadly, each equation is defined by:

## Name Domain Expression Relation

## Data-Expression Conditions

An algebraic representation of a model is not exactly the same as an algebraic view. In particular, the view manager need not know how coefficient tables are computed or what conditions they are required to satisfy. In fact, we ignore the object definition part in Figure 9 and define an algebraic view to be an equation listing plus bound and limit constraints associated with them and with the decision objects. To view the model structure algebraically, therefore, the following ingredients are needed.

1. A collection of sets, $S = \{name_{i}\}$ , where $name_{i}$ is a unique identifier for the i-th set.

2. A collection of domains with associated set and domain dependencies and associated logical restrictions, $\mathbf{D}=\{(name_{i}, T_{i}, L_{i})\}$ , where $name_{i}$ is a unique identifier for the i-th domain; $T_{i}$ is a dependency tree, which can be viewed as a parse tree; and, $L_{i}$ is a set of logical conditions.

3. A collection of data objects with associated domains and parse trees, $\mathrm{DO}=\{(name_{i},d_{i})\}$ , where $name_{i}$ is a unique identifier for the i-th data object; $d_{i}$ is its domain. We allow $d_{i}=\phi$ (simple parameters), and either the name or the domain can be used to distinguish a numeric constant.

4. A collection of decision objects, called variable classes, with associated domains, ranges and conditions, $V = \{(name_{i}, d_{i}, range_{i}, condition_{i})\}$ , where $name_{i}$ is a unique identifier for the i-th decision object; $d_{i}$ is its domain; $range_{i}$ is its range specification; and, $condition_{i}$ is a logical condition for generation. The range of the i-th decision object is a pair of data object references that describe the bound constraints in the linear program.

5. A collection of equations with associated domains, expressions, relations, ranges and conditions: $E = \{(name_{i}, d_{i}, expression_{i}, relation_{i}, range_{i}, condition_{i}\}$ , where $name_{i}$ is a unique identifier for the i-th equation; $d_{i}$ is its domain; $expression_{i}$ is its expression, which is a list of terms; $relation_{i}$ is its relation; $range_{i}$ is its range; and, $condition_{i}$ is its logical condition for generation. The range of the i-th equation is a pair of data object references that describe the limit constraints in the linear program. Each term in the expression has the form: {operation, domain, argument-list}. The typical operation is a sum, the domain of the operation is in D, and the argument list is either a primitive term, $\{do \in DO, v \in V\}$ , or it is another expression (as, for example, sums within sums).

If we apply this specification to obtain the algebraic view in Figure 1-a, the information is as follows.

1. {SR, DR}.

2. $\{(\mathrm{DOM1},(\mathrm{SR}),\phi),(\mathrm{DOM2},(\mathrm{DR}),\phi)$

(DOM3,(SR × DR),φ),(1,φ, = 1)}.

3. {(SUPPLY,DOM1), (DEMAND,DOM2), (CAPACITY,DOM3), (TRANCOST,DOM3), (1,1)}.

4. $\{(T,DOM3,(0,CAPACITY),\phi)\}$ .

5. $\{(\text{COST},\phi,(\text{SUM},\text{DOM3},(\text{TRANCOST},\text{T})),\text{MIN},\phi,\phi), (\text{S},\text{DOM1},(\text{SUM},\text{DOM2},1,\text{T}),$

$<=, \mathrm{SUPPLY}, \phi)$ ,

(D,DOM2,(SUM,DOM1,1,T),

$$
> = , \text { DEMAND }, \phi) \}.
$$

We used the symbol $\phi$ when the field is empty. For example, all condition fields are $\phi$ to indicate no condition is present, and the cost equation has another $\phi$ to indicate there is no data object reference for the MIN relation. The numeric constant 1 is defined in the domain list in order to define it in the list of data objects. This description, $(1,\phi, =1)$ , distinguishes the symbolic reference, 1, from its numerical value, =1. Then, equations S and D enter 1 as the symbolic data object reference, and its value is the coefficient of T in each sum.

The purpose of this example is not to impose a data structure, but to illustrate one. Short-cuts could be taken, such as distinguishing the numeric constant, 1. Our concern is with a precise specification of the information needed for a view manager to create an algebraic view.

Not only is each expression a variable-length record, but also the domain can have an arbitrary dimension (viz., number of set dependencies) and an arbitrary number of restrictions, each of which could be a variable length record. All of this pertains to implementation issues, but recognition of this variability is important to understand the breadth of issues in the design of a multi-view architecture.

A block schematic is another view with a different cognitive structure. The version given in Figure 1-b is only one of several variants. This view was developed by Baker [2] and by Welch [87] as an interface for model formulation. Their current systems, MIMI [15] and MathPro [63], respectively, have different variations of block schemata. The basic idea is to have row strips that correspond to constraint classes, column strips that correspond to activity classes, and cell entries that convey the contents of the associated submatrix. One of the important differences is how to define the cell entries when the submatrix is not a simple data table.

![](/api/attachments/SNSQVVXF/fulltext/images/a10a201841d7f2bdfbb787c2b39db720fa29157b0020ccbdc841c188e29b4635.jpg)  
Fig. 10. A block schematic of inventory recursion.

To illustrate this last point, and to prepare for the formal definition, consider a balance equation to represent a simple inventory recursion:

![](/api/attachments/SNSQVVXF/fulltext/images/d696d229d6b4f2d95ed7a27692f28a71444b6071bc95e6699d90143e1b182306.jpg)

The complication is that the inventory activity class, I(t), appears in two terms with different domain values. A standard icon for this case is shown in Figure 10. Such an icon specification is necessary to resolve multiple entries and lagged domains of a decision object in a constraint.

To construct a block schematic view, the following ingredients are needed.

1. A collection of domains, $D = \{name_{i}\}$ , where $name_{i}$ is a unique identifier for the i-th domain (unlike the algebraic view, dependency information and logical conditions associated with domains are ignored in the block schematic view; however, we do consider these later in the context of zoom models).

2. A collection of data objects with associated domains, $\mathrm{DO}=\{(name_{i},d_{i})\}$ , where $name_{i}$ is a unique identifier for the i-th data object; $d_{i}$ is its domain. We allow $d_{i}=\phi$ (simple parameters), and either the name or the domain can be used to distinguish a numeric constant.

3. A collection of row strips, $\{(name_{i}, domain_{i}, range_{i})\}$ , where $name_{i}$ is a unique identifier for the i-th row strip, $domain_{i}$ is its domain, and $range_{i}$ is a pair of data object references.

4. A collection of column strips, $\{(name_{j}, domain_{j}, range_{j})\}$ , where $name_{j}$ is a unique identifier for the j-th column strip, $domain_{j}$ is its domain, and $range_{j}$ is a pair of data object references.

5. A collection of cells, $\{(row_{k}, column_{k}, type_{k}, info_{k})\}$ , where $(row_{k}, column_{k})$ is the row and column strip, respectively; $type_{k}$ is the type of cell entry; and, $info_{k}$ is information, which depends upon the type. The types of cell entries are: (1) direct data reference, (2) indirect data reference, and (3) icon. For a direct data reference, the information $(info_{k})$ is its name. For an indirect data reference, the information is a key (or pointer) into a data collection. An icon describes a structure for the submatrix associated with the rows and columns in the cell (see below).

Notice that a schema view does not, itself, present information about logical conditions, such as those for generation of activities in a class. We postpone this consideration until we define zoom operations. We also postpone how to obtain the cell type and associated information until we define schema cell maps, which we do when considering mapping from an algebraic view.

If we apply this specification to obtain the block schematic view in figure 1-b, the information is as follows.

1. {SR, DR}.

2. {(SUPPLY,SR), (DEMAND,DR), (CAPACITY,(SR,DR)), (TRANCOST,(SR,DR)), (1,1)}.

3. $\{(\text{COST},\phi,(\text{MIN},\phi)), (\text{S},\text{SR},-\infty,\text{SUPPLY}), (\text{D},\text{DR},\text{DEMAND},\infty)\}$ .

4. $\{(T,(SR,DR),(0,CAPACITY))\}$ .

5. {(COST,T,direct,TRANCOST), (S,T,direct,1), (D,T,direct,1)}.

To begin our formalization of views, we consider a mappings between algebraic and block schematic views. We demonstrate difficulties with completeness – that is, the information that is associated with each view is insufficient to complete a mapping to the other view. Since each view can be used to construct the same model instances, they share certain core information. There are, however, information structures associated with each view that are missing in other views. To create mappings between algebraic and block schematic views, we add necessary information beyond what appears in each view.

An essential difference between algebraic and block schematic views is the way summations are represented. They are explicit in algebraic views by including a sum symbol (or keyword) and conditions directly. They are implicit in block schematic views by showing icons in a cell that indicate summations or conditions (or both).

Let us begin with an elementary algebraic view, where there are no conditions on summations and the sets defining the domain of the data object are present in those of the row or column strips (or both). We presume that the appearance of a decision object, say v, in an equation, say e, can be expressed with a couple $(f, D)$ , where f is a recognized function and D is a data object.

Here is the mapping for constructing an elementary block schematic from this algebraic view.

1. Define a column strip for each decision object and a row strip for each equation.

2. Initialize all cells to be null.

3. If the i-th decision object appears in the j-th equation, let $(f, D)$ denote the dependence. Define f as the first level of detail in this cell, and enter D into the cell.

The inverse mapping is equally straightforward for elementary views - that is, where each cell entry is simply a data table name. Then, one has the following direct association from the algebraic view to the block schematic.

$$
\boxed { \begin{array}{c c} & \mathrm{A(I,J)} \\ \mathrm{E(I)} & \mathrm{T} \\ \text {   } & \text {   } \end{array} } \Longleftarrow \mathrm{E(I)} = \Sigma_ {\mathrm{j}} \mathrm{T(I,j)} \times \mathrm{A(I,j)}
$$

The association is not one-to-one because the same block schematic is obtained when the domain of T is not the same as that of A, such as:

$$
\mathrm{E} (\mathrm{I}) = \Sigma_ {\mathrm{j}} \mathrm{T} (\mathrm{j}) \times \mathrm{A} (\mathrm{I}, \mathrm{j}) \text { or }
$$

$$
\mathrm{E} (\mathrm{I}) = \Sigma_ {\mathrm{j}} \mathrm{T} (\mathrm{I}) \times \mathrm{A} (\mathrm{I}, \mathrm{j}) \text { or } \mathrm{E} (\mathrm{I}) = \Sigma_ {\mathrm{j}} \mathrm{T} \times \mathrm{A} (\mathrm{I}, \mathrm{j}).
$$

(where T is a scalar in the last case).

Further difficulty occurs when one of the views is not elementary. This can happen with a single appearance of an activity class in only one term of the equation class, or it can be with multiple appearances. Recall, for example, that the simple inventory recursion requires an icon in the block schematic view. The icon -1/1, used by Math-Pro, is an example of a schema map, where an activity class appears in two terms of the same equation. In general, a schema map is a set of rules that use domains of the row and column strips and the domains of terms in the equation.

While MathPro takes a prescribed icon as a modeling expression and must generate the equivalent of an algebraic form for each instance, MODLER begins with an algebraic representation and applies rules for schema mapping (see Greenberg [39] for details). The particular rules used by both systems influence the general development here, but our goal is a general framework, apart from particular implementations.

Let us generalize this with a schema cell map that maps an algebraic view into a block schematic view, the issue being how to form a cell entry. When activity A appears in equation E only once, and the coefficient is simply a data table, say T, the cell entry is (E, A, T). Now suppose A appears in equation E only once, but there is an operation or condition associated with the relative domains. Algebraically, suppose we have:

$$
\mathrm{E} _ {\mathrm{e}} = \Sigma_ {\mathrm{s}} \mathrm{T} _ {\mathrm{d}} \mathrm{A} _ {\mathrm{a}},
$$

where $e = dom(E)$ , $d = dom(T)$ and $a = dom(A)$ (dom is the domain). The domain of the sum (s) will be considered shortly.

For example, suppose we have the following cases with $dom(E) = I$ .

Case 1 (Elementary): $\mathbf{E}(\mathbf{I}) = \mathbf{T}(\mathbf{I}) \times \mathbf{A}(\mathbf{I})$ , where $dom(\mathrm{T}) = dom(\mathrm{A}) = \mathrm{I}$ .

Case 2 (Elementary): $\mathrm{E}(\mathrm{I}) = \Sigma_{\mathrm{j}}\mathrm{T}(\mathrm{I},\mathrm{j})\times \mathrm{A}(\mathrm{I},\mathrm{j}),$ where $dom(T) = I\times J;dom(A) = I\times J.$

Case 3 (Extended domain of T): $E(I) = \Sigma_{j,k}$ $T(I,j,k) \times A(I,j)$ , where $dom(T) = I \times J \times K$ ; $dom(A) = I \times J$ .

Case 4 (Condition in summation): $\mathbf{E}(\mathbf{I}) = \Sigma_{\mathrm{j} = \mathrm{I}}$ $\mathrm{T(j)}\times \mathrm{A(j)}$ , where $dom(T) = dom(A) = J$

Case 5 (Extended domain of T and condition in summation): $E(I) = \Sigma_{j,k < j} T(I,j,k) \times A(I,j)$ , where $dom(T) = I \times J \times K$ ; $dom(A) = I \times J$ .

Case 1 is the elementary situation, where the cell value appears simply as T. This holds even if T is a scalar, where $dom(T) = \phi$ .

Case 2 is also elementary, even though a summation appears, because there are no conditions on the summation, and $dom(T)$ is a product of the sets that comprise the row and column strips. This holds if T is any of the four domains: $\phi$ , I, J, I × J.

Case 3 is not elementary because $dom(T)$ contains the set J, which is not in the domain of either the row strip or the column strip.

Case 4 is not elementary because the summation contains a condition. In MODLER, j = I expresses a condition that forms a binding between the index j and the member of set I. It expresses the fact that when equation $E_{i}$ is generated for a particular $i \in I$ , the term is $T(i) \times A(i)$ . This could be expressed with the same elementary view as case 1, but only if the domains of A and T are defined to be the set I, rather than the set J. In general, the set J can contain only some members of I plus other elements not in I, so the condition is needed to specify the restriction of the domain of the summation. Other languages can express this same binding with a different syntax.

![](/api/attachments/SNSQVVXF/fulltext/images/5da7345c69a57b3cf6b891566aa3e79addc35877c8ada5f800872953016d4b3d.jpg)  
Case 5. Summation is conditional and is over extended domain of T  
Fig. 11. Block schematic views for a single term.

Case 5 has a conditional summation and T has an extended domain since it contains set K, which is not in the domain of either the row strip or the column strip.

Each case needs an icon to convey the expression. Figure 11 illustrates these cases with a schema map that inserts a dollar sign (\$) to indicate summation and a colon (:) to indicate a domain condition.

If the block schematic views shown in Figure 11 are given, the algebraic view is not completely determined. Even the elementary views do not include the domain of T. In case 2, for example, all that is known is that $dom(T)$ is one of the 4 possible: $\phi$ , I, J, or $I \times J$ . Further, even with $dom(T)$ specified, to map a non-elementary block schematic view, such as cases 3, 4 and 5, an icon translator is needed.

Now let us formalize this schema map for a single term. Our purpose is not to impose the particular icons used in the view creation, but to show only that we can distinguish the cases when mapping from an algebraic view to a block schematic.

Let $P(d \mid cond)$ denote the projection of a domain, d, subject to the conditions, cond. For example, $P(I \times J \mid \sim J) = I$ . In particular, $P(d \mid \sim e, \sim a)$ is the projection of the domain of the data table, exclusive of the domains of the equation and of the activity. Let s be the domain of a summation with term defined by (E,A,T), with domains e, a and d, respectively.

This term is elementary if two conditions are satisfied. First, we want the domain of the data object not to contain any set other than those that appear in the equation class or activity class. This means we require $P(d \mid \sim e, \sim a) = \phi$ . Second, we do not want any conditions in the summation. This means we require $s = P(a \mid \sim e) \times P(d \mid \sim e, \sim a)$ (if a condition is present, $s \subset P(a \mid \sim e) \times P(d \mid \sim e, \sim a)$ ). By the first condition, the second reduces to $s = P(a \mid \sim e)$ . It turns out that $s = P(a \mid \sim e)$ implies $P(d \mid \sim e, \sim a) = \phi$ , so we define a term to be an elementary view if $s = P(a \mid \sim e)$ .

Using this last definition, an elementary term implies $P(d \mid \sim e, \sim a) = \phi - \text{that is, the data object } T$ has no extended domain. Otherwise, if S is a set in $P(d \mid \sim e, \sim a)$ , it must be in s, but S is not part of $P(a \mid \sim e)$ . This definition of elementary also ensures that there are no conditions in the summation since the sum is over the all of the sets in the activity's domain that are not in the domain of the equation.

In our example, we have:

Case 1: $\mathrm{P}(\mathrm{d}|\sim \mathrm{e},\sim \mathrm{a}) = \phi$ (since $\mathbf{d} = \mathbf{a}$ ), and $\mathrm{P(a|~\sim e) = \phi~(since~a = e)}$ .

Case 2: $\mathrm{P}(\mathrm{d} \mid \sim \mathrm{e}, \sim \mathrm{a}) = \phi$ (since $\mathrm{d} = \mathrm{e} \times \mathrm{P}(\mathrm{a} \mid \sim \mathrm{e}))$ , and $\mathrm{P}(\mathrm{a} \mid \sim \mathrm{e}) = \mathrm{J}$ .

Case 3: $\mathrm{P}(\mathrm{d} \mid \sim \mathrm{e}, \sim \mathrm{a}) = \mathrm{K}$ , and $\mathrm{P}(\mathrm{a} \mid \sim \mathrm{e}) = \mathrm{J}$ .

Case 4: $\mathrm{P}(\mathrm{d} \mid \sim \mathrm{e}, \sim \mathrm{a}) = \phi$ (since $\mathrm{d} = \mathrm{e} \times \mathrm{P}(\mathrm{a} \mid \sim \mathrm{e})$ , and $\mathrm{P}(\mathrm{a} \mid \sim \mathrm{e}) = \mathrm{J}$ .

Case 5: $\mathrm{P}(\mathrm{d} \mid \sim \mathrm{e}, \sim \mathrm{a}) = \mathrm{K}$ , and $\mathrm{P}(\mathrm{a} \mid \sim \mathrm{e}) = \mathrm{J}$ .

The schema map for a single term is now defined as follows. First, note that the domain of the sum satisfies: $s \equiv dom(R) \subset P(d \mid \sim e) \times P(a \mid \sim e, \sim d)$ . Then, define the cell $(E, A, \sigma)$ , where the cell entry, $\sigma$ , is given by:

$$
\sigma = \mathrm{T} \text {   if   } s = P (a \mid \sim e);
$$

$$
\begin{array}{r l} \sigma = & \text {   T   if   } P (d \mid \sim e, \sim a) \neq \phi \text { and } s = P (d \mid \sim e) \\ & \times P (a \mid \sim d, \sim e); \end{array}
$$

$\sigma = :T$ if $\mathrm{P}(\mathrm{d} \mid \sim \mathrm{e}, \sim \mathrm{a}) = \phi$ and $\mathrm{s} \neq \mathrm{P}(\mathrm{a} \mid \sim \mathrm{e})$ ; $\sigma = \$:T$ else.

This schema map distinguishes the cases in the example. More generally, we have the following:

Theorem. Let $\sigma$ be defined as above. Then, the following are true.

(1) $\sigma = T$ if, and only if, the term is elementary.

(2) $\sigma = \$T$ if, and only if, the data object's domain is extended, and there are no conditions in the summation.

(3) $\sigma = : \mathbf{T}$ if, and only if, the data object's domain is not extended and the summation has a conditional.

(4) $\sigma = \$$ :T if, and only if, the data object's domain is extended, and the summation has a conditional.

The proof follows immediately from the definitions.

Now consider multiple appearances of A in terms of E. Recall the inventory recursion, which is a special case of the following two appearances.

$$
\mathrm{E} _ {\mathrm{e}} = \mathrm{R} _ {\mathrm{p}} \mathrm{R} _ {\mathrm{r}} \mathrm{A} _ {\mathrm{q}} + \mathrm{R} _ {\mathrm{s}} \mathrm{T} _ {\mathrm{d}} \mathrm{A} _ {\mathrm{a}},
$$

where we could have - instead of + between the two terms.

In the case of the inventory balance equation, this becomes:

$$
\mathrm{B} (t) = \Sigma_ {j = t - 1} \mathrm{I} (j) - \mathrm{I} (t) + \dots ,
$$

where the other terms do not contain the inventory activity, I. The icon, -1/:1, represents the two coefficients, -1 and 1, in two different terms, where the colon (:) is the icon for the condition that j = t - 1 in the summation (this differs from MathPro, which omits the colon). The same icon appears if the condition is replaced by j = t - Lag, where Lag is a scalar parameter in the model description.

An equivalent expression, such as

$$
\mathrm{B} (t) = \mathrm{I} (t - \mathrm{Lag}) - \mathrm{I} (t) + \dots ,
$$

can use an icon different from the colon; an example is $-1/1: -1$ , where $1: -1$ is defined (by an icon translator) to mean that the coefficient is 1 for set member equal to the equation's time value (t) minus 1. Similarly, $-1/1: -Lag$ is an icon to represent the case with a Lag parameter.

The order of these two coefficients appears irrelevant to view creation, but it does have meaning for domain matching, as in MathPro. It is therefore not enough to apply the schema map to each term, and enter them with some separator (like /). For cognitive completeness, we must deal with this issue of ordering multiple icons.

Suppose the icons are pairs, $\{(I_{k}, s_{k})\}$ , where $s_{k}$ is a domain associated with the k-th term, and $I_{k}$ is its icon (the icon is obtained by applying the schema map to each term for a given equation (E) and activity (A)). Now suppose each $s_{k}$ has an order property such that $\{s_{k}\}$ is totally ordered. This is the case of the inventory recursion, where $s_{1} < s_{2}$ is inherited from the ordering of the set of time periods, t.

Then, the icons in the schema cell are ordered by the total ordering of $\{s_{k}\}$ . When this is possible, a special symbol is used as a separator (like /). When this is not possible, group the icons such that each group is totally ordered. Within a group, use the ordering principle just described. Separate groups by a different symbol (like &).

To illustrate, suppose $dom(A) = I \times J$ in the following expression.

$$
\begin{array}{r l} \mathrm{E(I,L)} & = \Sigma_ {\mathrm{j} <   L} \mathrm{T(I)} \times \mathrm{A(I,j)} - \mathrm{A(I,L)} \\ & + \mathrm{CARRY(I)} \times \mathrm{A(I,L+1)}, \end{array}
$$

where the domain of A in the first and second terms is bound to $dom(E)$ . In the last term, the ordered set (L) is offset by 1. For these bindings to be valid, J and L must be conformal; and, for the expression $L + 1$ to be valid, L must have an order property associated with its attributes.

In this case, the block schematic appears as:

$$
\boxed { \begin{array}{c c} & \mathrm{A(I,J)} \\ \mathrm{E(I,L)} & : \mathrm{T} \& - 1 / \text {CARRY}: + 1 \end{array} }
$$

The concatenation symbol (&) denotes a multiple appearance of activity A in equation E. The icon -1/CARRY:+1 is what we have described above, and the colon separates the coefficient (CARRY) from the forward lag (+1); another design could omit the colon or otherwise change the particular icon used.

The display could change the multiple appearances, if the width becomes too great, to an indirect reference. A special icon can signify this, and a zoom on the cell could then display a view of the multiple appearances of the activity class in the equation class. As it is, zooming is needed to obtain the domains of T and CARRY (we rely upon the familiar notion of zooming here, and we shall consider it as a general operation below).

With this additional information structure, which is not part of the algebraic view, the cell icon definition is sufficient to complete mappings between algebraic and block schematic views. Much of the work in developing the schema is due to starting with an algebraic view. Further, the mapping is generally not invertible. The difficulty with going from a block schematic view that contains icons to an algebraic view is that sum and condition information is lost without a translator for the icons. Only their presence is indicated by special symbols (like \$ and :). Besides icon translation, the domain information is not enough to map the block schematic to an algebraic view. Recall this holds even for an elementary view. In the above example, the domains of T and CARRY are not shown; they each can be any of the 16 cross products from {I,J,L,M}.

Now let us consider some graphic views. These are views that use graphical techniques to display the model structure. The graphics could be diagrammatic or iconic, and the model need not satisfy the mathematical definition of a network used in mathematical programming. The graphic views we consider are: netforms, block/link, activity-constraint, and process networks. We begin by describing a unifying framework for graphic views, first presented by Greenberg [39], as the other graphic views are contained within this general framework.

Fundamental graphs. Associated with each matrix, there are fundamental graphs that represent its structure, apart from the magnitudes of the coefficients. These were introduced for linear programming by Greenberg [37] and studied by Greenberg, Lundgren and Maybee [43,44]. The matrix to which we refer could be that of a model instance; it could be that which corresponds to a block schematic view; or, it could be a mixture of both.

Let M be an $m \times n$ matrix. The fundamental bigraph, $B = [R, C, L]$ , has a node set R associated with the m rows of M and a node set C associated with the n columns of M. The set of lines, L, corresponds to the nonzeroes of M: $(i, j) \in L$ for $i \in R$ and $j \in C$ if $M_{ij} \neq 0$ . From this, a projection operation is defined as follows. Let $G_{R} = [R, L_{R}]$ denote the row graph induced by the adjacency rule: $(i, k) \in L_{R}$ for i, $k \in R$ if there exists $j \in C$ such that $(i, j) \in L$ and $(k, j) \in L$ . In words, two row nodes are adjacent in the row graph if there exists a column having a nonzero in each of the two rows. Similarly, let $G_{C} = [C, L_{C}]$ denote the column graph induced by the adjacency rule: (j, k) ∈ $L_{C}$ for j, k ∈ C if there exists i ∈ R such that (i, j) ∈ L and (i, k) ∈ L. In words, two column nodes are adjacent in the column graph if there exists a row having a nonzero in each of the two columns.

One of the fundamental properties of these graphs, B, $G_{R}$ and $G_{C}$ , is that they all have the same number of components. This and other properties suggest views of model structures. Stronger insights can be obtained, however, by accounting for the signs of the nonzeroes. There are two ways to do this. One is to sign the lines in the fundamental bigraph; the other is to orient the lines. Each offers a different view of relations.

Both signing and orienting lines of B were considered in [44], but only the latter is used in the present discussion. We therefore consider only the fundamental digraph, $D = [R, C, A]$ , where the arcs in A are the orientations of the lines in B: $\langle i, j \rangle \in A$ for $i \in R$ and $j \in C$ if $M_{ij} < 0$ ; and, $\langle j, i \rangle \in A$ for $i \in R$ and $j \in C$ if $M_{ij} > 0$ . This has a flow interpretation: the arc is oriented from the column to the row if the associated activity produces an output for the row. This is consistent with netforms, where M is a node-arc incidence matrix (perhaps with multipliers); more generally, it is consistent with the process network view and with input/output relations of activity analysis.

The projections, $D_{R} = [R, A_{R}]$ and $D_{C} = [C, A_{C}]$ , are not merely orientations of the undirected projections, $G_{R}$ and $G_{C}$ , respectively. Arcs in these projections represent directed paths in the fundamental digraph. That is, $\langle i, k \rangle \in A_{R}$ for i, $k \in R$ if there exists $j \in C$ such that $\langle i, j \rangle \in A$ and $\langle j, k \rangle \in A$ . In words, an arc from row i to row k means there is an activity that transforms a domain object of i to a domain object of k. Similarly, $\langle j, k \rangle \in A_{C}$ for j, $k \in C$ if there exists $i \in R$ such that $\langle j, i \rangle \in A$ and $\langle i, k \rangle \in A$ . In words, an arc from column j to column k means that an output of activity j is an input to activity k, where the object of transfer is in the linking row (i).

These fundamental graphs can be views of only a portion of the entire matrix - that is, a submatrix. These same graphs apply to blocked matrices, which can be obtained by graph condensation methods. There can, in fact, be a recursive partitioning so that a view of any of these graphs can present nodes as representatives of graphs into which one can zoom. Further projections are possible simply by repeated application of path length specifications. The view manager needs to know only the information necessary to support zooming and condensation operations. The view presentation manager (i.e., display) need not know this information.

Netforms. Introduced by Glover [33] and advanced by Glover, Klingman and Phillips [35,36], netforms begin with standard networks and expand to incorporate non-network structures. Figure 1-d illustrates a simple case.

In the case of a network model, a node represents a constraint, and an arc represents an activity. Arcs missing either a source or destination node are supply and demand arcs, respectively. It is easy to see how such a netform converts directly into an algebraic statement.

More generally, the netform is an AND-OR graph with AND arcs representing non-network activities, such as transporting multiple commodities in fixed shares. The primary benefits from the netform view are in the visualization of network and integer structures. An AND-OR graph can be described as a hypergraph, H = [N,A], where N is the set of nodes, and A is the set of hyperarcs, defined as follows. Each member of A is an ordered pair of subsets of N, say $\langle P,S\rangle$ . The meaning is that each node in P is connected with each node in S, oriented from P to S. When P and S each contain exactly one node, the hyperarc is an ordinary arc.

Associated with each hyperarc are the following.

$$
1. \mathrm{C} (\langle \mathrm{P}, \mathrm{S} \rangle) \equiv \mathrm{cost}
$$

$$
2. \mathrm{L} (\langle \mathrm{P}, \mathrm{S} \rangle) \equiv \text { lower   bound }
$$

$$
3. \mathrm{U} (\langle \mathrm{P}, \mathrm{S} \rangle) \equiv \text { upper   bound }
$$

4. $f(\langle \mathbf{P},\mathbf{S}\rangle)\equiv$ flow

5. $\mathbf{M}(\langle \mathrm{P},\mathrm{S}\rangle)\equiv$ multipliers (matrix).

The flow is a decision variable; the other arc values are data.

A netform can have either $P = \phi$ or $S = \phi$ , but not both. In the former case, S must be a single node, and the arc is called a supply arc; in the latter case, P must be a single node, and the arc is called a demand arc.

In linear programming, each hyperarc is an activity, and each node is a constraint. Tailless and headless arcs represent supplies and demands, respectively, from data, which are constraint limits and activity bounds. It is sometimes possible to manipulate the model to gain a more insightful netform view, but our interest here is with only the view, itself, not with its manipulation. The multipliers are the coefficients, and a condensed form provides a view of model structures.

![](/api/attachments/SNSQVVXF/fulltext/images/292a13c65c9fd5618b91ea4e3d3522565a000ae4d78beb11fa031037e11ab94a.jpg)  
Fig. 12. Node icons to represent activity I/O in a netform visualization.

If special nodes are introduced to indicate the AND arcs, and if we do this for all hyperarcs, we obtain precisely the fundamental digraph. Further, in the case of ordinary network models, where every hyperarc is an ordinary arc, the netform is equivalent to the row digraph, except that parallel arcs are explicit in the netform, showing different costs and bounds, while the row digraph shows only the topology.

In fact, the main value of netform modeling is the visualization it offers when special shapes are used to distinguish nodes (to avoid cumbersome AND-OR notation). Figure 12 illustrates four icons that distinguish single and multiple I/O, where the types are the semantics in [38]. The same shapes can be used in condensed netforms, but with the edges doubled or color used to indicate the icon represents a portion of the model. Arcs can also be shaped and/or colored to represent classes, such as gains versus losses versus no gain or loss.

Block/link view. The block/link view can be considered an extension of the netform view, where more general structures are represented by incorporating an activity I/O view. The LP-FORM system [61,67] exemplifies this view, where blocks can be either nodes, as in ordinary network models, or collections of non-network activities; and, links can be either activities or material balances. If no activities are assigned to a block, then it functions as a network node.

If no activity is defined for an arc, the arc indicates a material balance constraint containing activities from both blocks. When an activity is entered, it takes its input from a constraint in the tail block and has output in a constraint in the head block. When an activity is assigned to a block, constraints are defined for each coefficient. New constraints are added when more activities are entered and these activities require different inputs or outputs from those previously defined. The composition rules for linking the pieces of the model into a complete algebraic statement used in LPFORM are given by Murphy, Stohr and Ma [70]. Rules for automatic linking by a purely syntactic approach are given by Glover and Greenberg [34].

Whereas netform visualization grew from thinking of linear programs as having a large embedded network, the block-link perspective sees a network with embedded processes, or blocks. In part, netforms grew from seeing linear programs as generalized networks with side constraints and activities. By contrast, the block-link visualization grew from seeing linear programs as a linking of embedded linear programs. The links can be transportation activities, and the blocks can be regional process models that use material inputs and produce product outputs. Both perspectives lead to the same visualization, but by a different path. This difference is important for view management, especially once it incorporates artificial intelligence.

Activity-constraint graph. The activity-constraint graph, introduced by Schrage [76], and analyzed in a context of views by Murphy, Stohr and Asthana [69], is a modification of the fundamental digraph. The modification is distinguishing the costs, or objective values, similar to distinguishing bounds. Otherwise, it is precisely the fundamental digraph, applied to the instance of the model.

Process networks. Another view of relational structures is that of a process network. This view originated in modeling chemical engineering problems. When the model is an ordinary network, there is no difference between this view and the netform view. For each non-network activity, one includes a node that is a square instead of a circle. Each non-network activity is presumed to have a single output (multiple inputs) or a single input (multiple outputs). All arcs entering and exiting a process node represent the coefficients of the non-network activity. All other arcs are standard network activities.

![](/api/attachments/SNSQVVXF/fulltext/images/b5cb2cb146ced2ddf287e9a1a29db32a6ae45050e4f2ae24374ae5edae960913.jpg)  
Fig. 13. A column node (j) in the fundamental digraph before and after splitting.

Chinneck [16] has exploited the structure of process networks for viability analysis, and one can show their equivalence to general linear programs. This is also equivalent to the fundamental digraph, except the column nodes are split so that no column has both multiple inputs (negative coefficients) and multiple outputs (positive coefficients). A simple transformation to satisfy this property of either single input or single output is illustrated in Figure 13.

An elaborate use of process network views, including unit aggregation, is part of MODEL.LA [81,82] and ASCEND [74,75]. Although these were developed for chemical engineering modeling, they contain views that apply more generally.

The fundamental graphs represent all the graphic views just described: netforms, block/link, activity-constraint, and process networks. They differ in the form of the view. The only differences in content are the surrogate information shown, such as bounds on activities and constraints.

In general, we want a graphic view to allow mixed levels of aggregations for the nodes and arcs. Further, we want to incorporate ordinal views, as in activity networks [21] and simulation [73,77,79]. The first effort to formalize graphic representations of linear programs was by Müller-Mehrbach [66]. Other graphic views, notably Harel's [46] higraph, Bell [10] and Hurrion's [48] visual interactive modeling, Barth's [9] object-oriented approach, and US West's GNMS [58] offer important insights and alternative formalisms. Perhaps the most developed formal graphic approach to model description is the seminal works of Jones [49-53].

Some systems are based on hybrid views, such as using an algebraic language like GAMS but giving graphical interfaces $[54,55]$ . Yet another view of model elements, and the knowledge on which they are based, is Krishnan's logical description $[57]$ .

## 4. Operations on views

The purpose of an operation on a view is to re-organize either its content or its form in order to acquire another vantage for insight. Three types of view operations are zooming, condensing, and switching.

One type of zooming operation, sometimes called a disaggregation, provides more detail about an element in the view. One example was noted above in getting more information about a cell in a block schematic view. Another example is to consider a view element that represents a portion of the model, such as a process appearing as a node in a graphic view. A zooming operation is designed to reveal details about the process. This can be nested, so that each zoom goes deeper into the details about the element. The zoomed view can be changed if desired. For example, with a graphic view of the entire model, one can zoom in on a process and switch to an algebraic view of that portion of the model (or of an instance of the model).

More generally, each element in a view has a zoom model that responds to a zoom request. The request can be to get details about an indirect reference in a block schematic or algebraic view, or to disaggregate nodes in a graph view into subgraphs. The zoom model of a name could be a text description or some information about associated data sources. Inheritance can be applied if the view is a matrix and the name refers to a particular row, which is a member of some class. As one of the cornerstones of the design of new modeling languages, like GNMS [58] and ASCEND [74,75], inheritance is used very effectively to satisfy requests for acquiring details about model objects and relations.

When creating a view, therefore, zoom models must also be created for that view. A zoom model for an icon in an iconic graph view can be different from a zoom model for the associated portion of the model in an algebraic view. This is because the view manager can have default reasoning mechanisms, where the view requested is generally from a particular constituency whose request for detail is different from that of another constituency. For example, suppose the view is algebraic, and a zoom request is issued for an equation. In this case, the zoom model might provide justification for the equation, such as some physical law about heat transfer meaningful to an engineer. Now suppose the view is an outline, as in structured modeling, and a zoom request is issued for the test object that corresponds to the same equation. The zoom model here might provide a trace of the calling sequence.

Of course, it is not necessary to have different zoom models for different views, but the view manager must allow this flexibility. In other words, the burden of creating zoom models need not be placed entirely on the model builder. Instead, default zoom models are part of the system design, and the model builder can use these or over-ride them.

The inverse of zooming is condensing. This collapses a view according to some criteria, and a view condensation model is needed analogous to a zoom model. In graphic views, each node has properties that form a natural binding among nodes. For example, in a transportation problem, all supply nodes could be condensed to form a single node that represents supply, and all demand nodes could be condensed to form a single node that represents demand. These bindings can be applied to form a natural condensation model without requiring the model builder to specify it a priori. It is not necessary, however, that a condensation be a true inverse of a zoom, in a mathematical sense. This is because after condensing nodes, say, by region, the zoom might be on other details within the condensed node, such as disaggregating by material.

Another operation is to switch views. For example, the active view might be an iconic graphic view superimposed on a map. The user might ask for an algebraic view of that portion of the model represented by one of the icons.

In considering view creation, switching must be regarded as a separate operation from zooming, even though a user might think of these as only one operation. If the active view is iconic and one seeks a view of the equations in one of the icons, the process is two-step: zoom in on the icon and switch to algebraic.

All operations, notably zooming, condensing and switching, can be applied to any part of the active view. Other operations include some found in CAD/CAM systems, particularly a view in the problem domain, where icons and their relative locations correspond to physical objects related spatially or temporally.

## 5. Connections with structured modeling

Structured modeling (SM) is a formal approach to model description, based on calling sequences of the following five types of objects.

1. primitive entity, such as a set of materials or regions.

2. compound entity, is defined in terms of other entities, like a product of sets.

3. attribute, which can be dependent upon entities (primitive and compound), is an object that can assume a value, like a data table or a variable.

4. function, any computable function of attributes, which can depend also on entities.

5. test, any logical function of attributes, which can depend also on entities.

From these five fundamental objects, SM views a model as dependency relations, namely calling sequences, which are hierarchically ordered. One SM view is an elemental graph, which contains a node for each object and arcs for their calling sequences. Another view is a genus graph, which contains nodes for collections of objects and arcs for their common calling sequences. SM has rules to construct a genus graph from an elemental graph, and it is possible to vary levels of detail. One could, for example, zoom in on a portion of the genus graph by constructing its elemental subgraph. In this way, one can view portions of a model relevant to particular questions.

Details of SM are well covered by Geoffrion [26-29]. Our concern here is with the views treated by SM, and with how SM fits into a formal foundation for a multi-view architecture.

A view of model block structures, which is intrinsic to SM, is an outline. SM is a top-down approach to model description, and the SM outline is based on paragraph specifications. Here we consider the reverse process of going from a problem specification to an outline view, where paragraphing is a dynamic operation.

![](/api/attachments/SNSQVVXF/fulltext/images/c70631505c6ea784d2ca3361b7f3d351e39909e0f2e6afdec9b9f73f8b7a8570.jpg)  
(a) Sectorial Outline  
Fig. 14. Two outline views of an energy model.

Figure 14 shows two outlines, only one level deep in each case. The first organizes model blocks by sectors: supply, demand, conversion, and transportation. The second organizes the model outline by primary energy forms: coal, oil and non-fossil.

The ability to create different outline views of the same model is useful for personnel organization and for associated data acquisition and maintenance. In this example, one could have divisions to manage the blocks of the model, where the choice of outline matches the personnel organization, responsible for the blocks. It is desirable to enable the creation of outline views dynamically – that is, without changing the model description file.

There have been several languages designed for structured modeling. The first, by Bradley and Clemence [11], uses a type calculus, which is closest to an algebraic view. Geoffrion's SML [30] is a direct implementation hosted by Framework $^{(R)}$ . Jones [49,50] uses graph grammars for a graphic interface with SM. Chari and Krishnan [14] describe a first-order logic language, LSM. Because SM is, by its definition, a model description, it can be used to formulate more than one problem; and, SM does not deal with management of instances. To build on SM, we consider augmentations that address problem specification and conditions for instance generation.

## Subdivision of basic categories

There are limitations in SM for distinguishing domains and the sets that comprise them. For view creation, the primitive entity needs to be attributed with a type that contains semantic information. In particular, we want to distinguish sets of time, place and form. These have different properties, which affects inheritance and the associated algebra. For example, we might want to be able to disallow unions of mixed types; and, we want each set of time to be ordered. The property of order is a related, but distinct issue that pertains to subdividing primitive entities. It should be possible, for example, to express an ordered set as a set of integers whose first and last entries can be parameters (attributes in SM terms). Currently, SM disallows this; and, this does contradict the notion of primitive.

SM attributes need subdivision, such as the distinction between indicative and relational, given by Nance [71]. Geoffrion's variable attribute category is a different delineation. Although it is convenient for problem specification, it poses a difficulty for view creation. For example, in one instance of a process model we can have yield ratios that are parameters – that is, data; in another instance these ratios can be variables. The pooling problem for a refinery is an example of this. The difficulty with SM, as it is currently described, is that the modeler must decide upon this during model formulation, rather than treat these as instances. Ideally, we want simply to declare the ratios as objects with a relational attribute that limits their admissible values, such as summing to unity (or lying in some interval that contains unity). If an instance specifies these as parameters, the relational attribute is interpreted as a check on the data; if another instance specifies these as variables (to be determined by optimization), the relational attribute is interpreted as a constraint for the nonlinear program. One way to keep the SM description general is to avoid variable attributes altogether. This underscores the need for a problem specification language that accepts SM input.

New categories. There is a need to connect model components with attributes that are not part of the model, itself. One way to do this is to use the abstract data type $[83,13]$ (ADT). For example, suppose we have a refinery model, where each activity transforms a mixture of crude oils into yields of intermediate and final refined petroleum products. In matrix terms, it might be difficult to distinguish one processing unit from another, but associated activities have different attributes that can contribute insight when viewed by a process engineer. Suppose we declare a variable attribute to be linked to an ADT associated with its process unit type. Then, views that ask for relations of these variable attributes and associated data tables (attributes) can use this link to create a view in terms of its attributes.

Another ADT is a unit of measurement and associated relations. Structured modeling does not require units to be specified (as do some languages $[60,11]$ ). Thus, if a flow is measured in gallons and production is measured in barrels, the ADT must account for the conversion in a balance equation that includes production and flow. This affects not only problem specification, but also query, reporting and model management. By not requiring the units to be specified in the model description, the ADT can allow flexible data instances. One may specify capacities in gallons in one instance and in barrels in another instance. This should not affect the model's integrity or the views that can be created.

Another ADT fulfills a need to distinguish control tables from other types of data tables. In SM, a control table LINK, say with domain $S \times D$ (supply $\times$ demand), is the same attribute type as a table COST over the same domain, which contains cost data for each link. For problem specification and for instance generation, this poses no difficulty, but view management is compromised by not have them distinguished. This can be done by appending ADT CONTROL to the LINK table properties (alternatively, the attribute could be subdivided to make this distinction explicit).

Goals, constraints and objectives. Currently, all constraints in SM are expressed as test types (t), which is an algebraic representation. This suffices for internal representations, but work is needed to derive the SM representation from other views, such as from a process network. Objectives, namely functions (f) to minimize or maximize, are not explicitly expressed; they must be inferred from the text in the function declaration. We prefer to subdivide functions into explicit expressions of objectives. We also prefer to have the category of function that describes goals, as in goal-programming. An alternative, of course, is to use abstract data types. Keeping function as a single category, we could, for example, APPEND MINIMIZE, or APPEND GOAL <= attribute.

What is important is that these could change from one instance to another, thus changing the views. In multi-objective programming, one may arrive at a pareto optimum. Then, one may want to view the effects on the other criteria if one is required to improve. In practice, this can be done by treating the other criteria as goals or constraints, shifted from current values, and optimize the one distinguished criterion. In SM terms these other functions change type.

Conditionals. A domain, such as that of an activity, can have conditionals for membership, such as for generation of specific activities in the class. Links between suppliers and markets can be described by a (data-dependent) relationship, such as distance. SM does not distinguish domains and sets. To have a sparse set of links, an explicit compound entity must be defined independent of attributes. In many cases this is not a natural representation, and views about the conditions for such links to exist would be lost – that is, they are not part of the SM representation. As in the other cases, this could be accommodated by an ADT or by a new category of sets, called domains, which are like compound entities, except for the relational attributes that comprise conditionals.

## 6. Generalized formal development

We have illustrated how an information structure for a specific view cannot, by itself, provide an appropriate internal representation. This is due to ambiguities that arise – that is, a one to many mapping, which precludes a property of independence. This independence can be seen as a distinction between an internal view definition and an external one. An internal view definition relies on information not shown in the view. For example, MathPro and MIMI use block schematic views for model description, but since they can generate instances, they have enough information to give other views, like algebraic. It is necessary to use information beyond what appears in the block schematic view, such as how they create cell icons from the more general information. This is what we mean by internal: the information for the view is more than what is in the view, itself. Icon mappings are what raised problems in attempting to map a block schematic into an algebraic view without the additional information. Ambiguities arose because there was more than one way to interpret some of the icons. Even in an elementary form, the domain of the data object is not part of the block schematic view.

An external description, however, is what is needed to make view creation and switching independent of particular implementations. By definition, each view is created by accessing information from a central structure. This is the same way views are created from a switching command, which is not limited to just the information contained in the initial view.

In the process of examining this issue of information access, we introduced some formalism through list structures that provide view information access. We probed more deeply into the suitability of structured modeling because it appears to provide the independence we seek, and because the expressive power of SM theoretically subsumes that of relational databases $[22]$ (see, also, Dolk $[20]$ and Choobineh $[17]$ for representations that enable relational views of linear programs). Before generalizing the formalism introduced earlier, some perspective is in order.

Here, we first consider the overall architecture of a multi-view system. Then, we present an information structure that supports all of the views we have considered. The natural question is, How complete is this information structure for supporting all views? Put another way, what is the scope, or expressive power, of the information structure? We address this with a formalism about view information access.

In Figure 15, a multi-view architecture is shown as a module that stands apart from any particular system for modeling and analysis. The formal development given here is a specification for its design, addressing such questions as the following. What central information structure is needed to support different views of models and their instances? The answer provided here is a beginning. Other questions to be considered in subsequent research include, “What are the limits of view creation?” This question is raised in the context of expressive power of any particular implementation.

![](/api/attachments/SNSQVVXF/fulltext/images/a29752f9142058743a4c4c5aaa8afcb97f44eda287634ace32540cbc187ae146.jpg)  
Fig. 15. A multi-view architecture.

Now we formally present an information structure designed for a multi-view architecture. We begin with model information, then we describe instance information. The structures are intended to be conceptual, so implementations could vary the form of lists. Our goal is an organization of information elements that supports retrieval for creations of views. The particular information structure presented is oriented toward linear relations, and more is needed to represent general nonlinear forms.

Each list begins with a name that is a unique identifier for the member of the element class. Links establish bindings among class members, some permitting inheritance. Each element has a head field that points to the head of a list of elements that contains references to the element. Additional information depends upon the class.

1. Properties are primitive elements, like ordered: {(name, head)}.

2. Attributes are primitive elements, like form, place and time: {(name, type, property-list, head)}. The type indicates whether the attribute can be inherited by its referents. The property list refers to properties possessed by the attribute. For example, form has a units property, place has a spatial property, and time has an order property.

3. Sets can be primitive or implied, that is, dependent upon other objects: {(name, type, info, head)}. The type of set describes two things. First, it indicates whether the set is primitive or implied; second, it indicates whether the set is attributed. The info then gives the dependency information (if the set is implied) and the attribute list (if the set is attributed). The dependency information describes how the set is obtained. For example, it can be in the form of a parse tree that represents the relational algebra, like unions, products, projections, etc. It can also be dependent upon certain data objects, like a set of consecutive integers defined by two data objects that give the first and last values.

4. Domains are restricted products of sets: {(name, sets, restrictions, head)}. The sets define a product, and the restrictions can be logical – that is, depend only on relations of set members, or they can be data-dependent.

5. Data objects are numeric constants, parameters or tables: {(name, domain, range, semantics, head)}. The domain of a numeric constant is a keyword, like NUMERIC, and its range is its value, fixed for all instances. The domain of a parameter is the empty set. The range is the admissible range of values for instances. A parameter can be a universal constant, like PI, or it can vary over instances. In the former case, the range is a single numeric constant. More generally, the range of a parameter or a table is a specification of a list of intervals, not dependent on other parameters or tables. The semantics are bindings to properties and attributes.

6. Decision objects are classes of variables: {(name, domain, range, conditions, semantics, head)}. The domain can be the empty set. The range specification is either a pair of data objects that define lower and upper bounds, or a list of data objects that define discrete values that comprise the variable's range. The conditions are logical expressions, which can be data-dependent, that pertain to generation of a member of the decision object class. The semantics are bindings to properties and attributes.

7. DD objects are classes of objects that will either be data objects or decision objects, according to a role assignment for an instance: {(name, domain, range, role, semantics, conditions, head)}. The role is a place holder that becomes instantiated as one of: { $\phi$ , OMIT, DATA, DECISION}. A role value of $\phi$ means no role is assigned. When the role is OMIT, the object is absent from the instance. When the role is DATA, the rest of the information is treated as a data object. When the role is DECISION, the rest of the information is treated as a decision object.

8. Equations are expressions that form constraints, goals or objectives in the mathematical program: {(name, domain, role, range, conditions, terms, semantics, head). The role of an equation is one of: $\{\phi, OMIT, MINIMAND, MAXIMAND, GOAL, CONSTRAINT\}$ . The range specification is a pair of data object references, either of which could be absent. For the CONSTRAINT role, this defines lower and upper limits for the level of the equation. The conditions are logical expressions, which can be data-dependent, that pertain to generation of a member of the equation class. The semantics are bindings to properties and attributes.

9. Logical expressions form constraints in the mathematical program: {(name, domain, role, type, info, conditions, semantics, head)}. The role of a logical expression is one of: { $\phi$ , OMIT, CONSTRAINT}. The type is a keyword, such as IF-THEN, COVER, SELECT, etc. The info depends upon the type. For example, IF-THEN requires antecedent and consequent expressions; and, COVER and SELECT require a set of binary-valued (0, 1) decision objects. The conditions are logical expressions, which can be data-dependent, that pertain to generation of a member of the logical expression class. The semantics are bindings to properties and attributes.

10. Functions are computable expressions that map numeric-valued objects into a real value: {(name, object list, expression, semantics, head)}. The object list is any collection of data objects, decision objects and DD objects. The expression is a computable form, like a parse tree. The semantics are bindings to properties and attributes.

11. Operations are delimiters for terms in an equation: {(name, domain, semantics, head)}. The domain can be empty, as in the case of the implied summation in MODLER. The list of operations must include SUM (or an equivalent keyword). The semantics are bindings to properties and attributes.

12. Terms are contained in equations: {(name, equation, sign, operation, function, conditions, semantics, head)}. The sign is either + or -. The operation is applied to the function. The conditions are logical expressions, which can be data-dependent, that pertain to inclusion of the term in a member of the equation class. The semantics are bindings to properties and attributes.

The main difference between this structure and the ones we presented specifically for the algebraic and block-schematic views is that we are independent of what was internal information structures – that is, information not contained in the view. In this external information structure everything has an identity that allows us, for example, to trace back to the most primitive elements of a model's objects and relations. In lists 1 and 2 above, we define properties and attributes that can be associated with the different objects in the model. These lists are not part of the other data structures, since the other structures do not try to deal with meaning. The set list, 3, is the same, except for added semantic information, as in the algebraic information structure, but this is not in the block schematic information structure because sets are always bound to objects and in domains, defined in 4, in this view.

Data objects, given in list 5, and decision objects, given in list 6, are as before, except for the addition of bindings information. Note that column strips are the decision objects in the block schematic information structure. DD objects in list 7 are new; they are added to handle problem definition separately from model definition. The equation object, list 8, has a different meaning here versus algebra. It consists of a list of terms as well as the information for constructing an audit trail. Logical expressions, given in list 9, are restrictions that need not be expressed algebraically; typically, they are stated as logical implications (i.e., IF antecedent THEN consequent), but any logical expression, such as clause form, can be used to define conditions.

Functions, given in list 10, extend representations of linear programming views to nonlinear forms. Even if the mathematical program is linear, however, the functions may still be used to express data relations. For example, demand data for a linear program can be a sequence over time defined by initial demands and a growth rate. The formula to determine the LP demand for t > 0 is a standard nonlinear expression.

Operations, given in list 11, contain information to create not only the terms of an equation, but also the associated icons in a block-schematic view. The conditionals on summations are explicit in the equations with the algebraic view, and list 12 contains what is needed with references to operations and other elements defined previously. The information in lists 11 and 12 determine cell icons in the block schematic. Notice that this separation of the definition of the terms from the definition of the equations is central to defining parts of the model separately that allows us to add semantic information about the model components to explain the model's parts and how the relate to one another. A key is primitive subdivision with bindings explicit in the information structure.

The above information structure pertains to the model, itself, apart from instances. It is not difficult to verify that all of the views we have described can be generated from this central information structure. In particular, the difficulties we encountered mapping algebraic and block schematic views are overcome by this information structure. It is also not difficult to note omission of details that distinguish implementations, such as representations of expressions, for example as parse trees, and additional links, such as from decision objects to terms. We now consider additional information to support view creation of instances.

An instance is defined as the assignment of values to all data objects, including sets, and to roles. For each list, we could add another field, called the source, which is a list of unique identifiers to cross reference instances. This principle is one of the features of MathPro, as part of its model management facility.

The following information structure is designed to support views of instances. This is in addition to the model information structure, in order to support operations, like zooming, condensing and switching.

1. Header of instance: {(name, parent, help, solution, head)}. The parent of the instance is some other instance or it is $\phi$ to indicate it is from the model, itself. In the former case, the remaining lists are deviations from the parent (this is the technique used in MathPro). The help reference is to a file that documents the instance. This could be in addition to the help file of a parent. The solution information defines the overall status of the solution of the instance (which might be unsolved) and the optimizer used. The head binds the instance to a list of scenarios.

2. Sources of instance: {(object, source)}. The object is any that was instantiated, such as set members, data object values, and role assignments.

3. Objectives of instance: {(equation, value)}. In the case of a single objective, the list has only one equation (the Source list contains the roles). The value is its value for the instance.

4. Constraints of instance: {(row name, type, class, lo, up, status, level, price)}. The type is one of the constraint types in the model information: equation or logical. Then, the class is the name of the equation or logical, respectively. The semantics in the model information can contain information about its row form, especially in the case of a logical constraint that has been converted to a linear inequality. The lo and up numeric values are the limits of the constraint, which are bound to the range specification in the model information. The status, level and price comprise the solution values of the constraint.

5. Activities of instance: {(column name, class, lo, up, status, level, price)}. The class is the name of the decision or DD object. The lo and up numeric values are the bounds of the activity, which are bound to the range specification in the model information. The status, level and price comprise the solution values of the constraint.

It is not difficult to verify that this instance information structure is sufficient to support all of the instance views we have described. Currently, ANALYZE receives much of this to support the views it creates. Some views require a significant amount of computation, which could be circumvented by additional information not included here. For example, to obtain rates of substitution between basic and nonbasic variables, one must apply an equation-solving algorithm. We leave open, for now, whether such information as rearrangement of the basis should accompany the instance structure.

Now we address the question of scope. Are there views about the model or its instances not supported by this information structure? The answer is yes if the structure is taken too literally. In particular, the information structure says very little about views for scenario management. Suppose someone wants a view to get insight from comparing two or more instances? Suppose one wishes a complete audit trail about an instance, tracing back not only to model description components (like equations), but also to primary data sources that can be many steps removed from the information at hand? For example, what is viewed as data input to the instance can be output from a surrogate model, such as one that forecasts demands used as right-hand sides in the constraints.

On the other hand, the information structure can be regarded as conceptual, and we return to a question raised early in this paper: What is a view? Superficially, one could define a view as a model: a collection of objects and relations. This is, however, incomplete, as the following development reveals.

At the very highest level, a view is composed of three categories of specifications: (1) its content, (2) its form, and (3) its world. We have illustrated content and form; next, we describe what the world means in this context before we proceed to elaborate on all three.

A view's world gives a contextual meaning to its form and contents [3], which we use to provide some of the semantics behind the view. For one thing, the world provides overview information, including: how the view was requested, how the view relates to entities and relations not in the view, what zoom models to use, and what libraries, databases and other sources that are bound to the view's content.

A key to understand the formalism based on view information access is to understand the distinction between direct and indirect information. Indirect information access involves such operations as projection, which we illustrated, to obtain relations that are implied by the direct relations and by rules of inference based on the meanings of the relations. One example is the relation between two activity classes that is implied by their common dependence on the same data object.

This leads to one of the conditions for completeness. That is, if $V = [W, C, F]$ is any view (with W = world, C = content and F = form), and if $F'$ is some other form, the information structure should support the view $V' = [W, C, F']$ . This presumes, however, that either F and $F'$ are content-insensitive, or that form $F'$ is defined for content C. For example, suppose V is a view of set dependencies, with C = sets and their dependency relations, and F = conceptual graph (c.f.,

Figure 8). Then (absent any equations), an algebraic view is not defined, so F' cannot be this form.

Another condition for completeness is based on operations, like zooming. If $C'$ is obtained from C from a zooming operation with appropriate changes to $F'$ effected by the operation, the view $V' = [W, C', F']$ should be supported by the information structure. A similar statement applies to condensations and projections.

We begin to see that the information structure must be defined at an atomic level - that is, where objects and relations are the most elementary. Considering the information structure defined for model information, one needs only to consider the elements more abstractly to see it as a conceptual information structure. To some extent this abstraction can be achieved with the elemental graph in structured modeling, but not quite. What must be added are primitives like indicative attributes, which can also be regarded as property lists from an information structure vantage. Other additions include role assignment information and a grammar that describes how operations perform. This syntactic approach is fulfilled by the formalism of Baldwin and Garlan.

It is not really necessary to have a separate specification for the information structure of instances. This was done above to be specific about the nature of the information and bring attention to links between instance and model description elements.

## 7. Summary and conclusions

There are many views of mathematical models and their instances. The very definition of a model is not universally accepted beyond agreement that it contains objects and relations among them. The formal approach of structured modeling provides a foundation for model description, but it leaves open issues about problem specification that affect view creation.

It is easy to accept the idea that different people gain insights from different views. Because of this, we need a multi-view architecture to support mathematical modeling and analysis. With the exception of Baldwin's DOVE system, this presents the first formal framework for addressing this need in OR/MS decision support systems that are based on mathematical programming.

We have used views that people have found useful in large-scale linear programming over the past 35 years to provide a concrete, applied base upon which to establish a foundation for a multiview architecture. Close analysis of popular views, notably variants of algebraic, schematic and graphic views, reveals that they are all useful, depending upon the individual and the situation. No single view implementation is rich enough to support a multi-view architecture, so a new, central information structure forms the foundation for such support. The view creation and management module is designed to switch from any view to any other, not by direct mapping, but by creating each view independently.

Although we have oriented views as an output, clearly every modeling system assumes a view for its input specifications. Some are algebraic, some are block schematic, and some are graphic. We see no need to distinguish whether a view is presented as an input or an output specification. We do, however, see a need to map view inputs into a central information structure, especially since we have demonstrated difficulties with mapping directly from information about one view to another view. Once views are better understood as a formal construct, their use for input specification will become a matter of implementation, rather than conception.

Among the open issues, understanding the expressive power of any proposed information structure has both theoretical and practical implications. Future studies of a modeling system's expressiveness must take view creation into consideration. Most systems present only those views that conform to its input specification. Abstract formalisms, notably structured modeling, contain the foundations needed for this extension.

## Acknowledgements

The authors gratefully acknowledge comments and advice from Dirk Baldwin, H.I. (Gus) Gassman, Arthur M. Geoffrion, Fred Glover, Alice M. Ireland, Richard E. Nance, and Laurel Neustadter. Comments from two anonymous referees and from the Editor, Christopher V. Jones, helped create this revision as an improvement over the original version. Financial and technical support was provided by a consortium of companies: Amoco Oil Company, IBM, Shell Development Company, Chesapeake Decision Sciences Inc., GAMS Development Corp., Ketron Management Science, and MathPro, Inc.

## References

[1] F.L. Alvarado, 1990. Manipulation and Visualization of Sparse Matrices, ORSA Journal on Computing 2:2, 186–206.

[2] T.E. Baker, 1983. RESULT: An Interactive Modeling System for Planning and Scheduling, Presented at the ORSA/TIMS meeting, Chicago, IL.

[3] D. Baldwin, 1989. Principles of Design for a Multiple Viewpoint Problem Formulation Support System, Ph.D. Thesis, School of Business Administration, Texas Tech University, Lubbock, TX.

[4] D. Baldwin, 1990. The Development and Architecture of DOVE: A Multiview Viewpoint, Proceedings of ISDSS Conference, Austin, TX.

[5] D. Baldwin, 1992. The Design and Evaluation of a Multiple View Decision Support System, Technical Report, College of Business, Virginia Polytechnic Institute and State University, Blacksburg, VA.

[6] D. Baldwin, 1992. Exploring Multiple Views: Examples from Accounting, Mathematical Modeling and Systems Analysis, Technical Report, College of Business, Virginia Polytechnic Institute and State University, Blacksburg, VA.

[7] A.A. Baldwin, D. Baldwin and T.K. Sen, 1991. The Evolution and Problems of Model Management Research, OMEGA 19:6, pp. 511–528.

[8] D. Baldwin and S.B. Yadav, 1991. Principles of Design for a Multiple Viewpoint Problem Decision Support System, Technical Report, Department of Accounting, College of Business, Virginia Polytechnic Institute and State University, Blacksburg, VA.

[9] P.S. Barth, 1987. An Object-Oriented Approach to Graphical Interfaces, ACM Transactions on Graphics 5:2, 142–172.

[10] P.C. Bell, 1985. Visual Interactive Modeling as an Operations Research Technique, Interfaces 15, 26–33.

[11] G.H. Bradley and R.D. Clemence, Jr., 1986. A Type Calculus for Executable Modelling Languages, IMA Journal of Mathematics in Management 1, 277–292.

[12] A. Brooke, D. Kendrick and A. Meeraus, 1988. GAMS: A User's Guide, Scientific Press, Redwood City, CA.

[13] L. Cardelli and P. Wegner, 1985. On Understanding Types, Data Abstraction, and Polymorphism, Computing Surveys 17:4, 471–522.

[14] S. Chari and R. Krishnan, 1990. Towards a Logical Reconstruction of Structured Modeling, Technical Report, School of Urban and Public Affairs, Carnegie-Mellon University, Pittsburgh, PA.

[15] Chesapeake Decision Sciences, 1988. MIMI/LP User Manual, New Providence, NJ.

[16] J.W. Chinneck, 1990. Formulating Processing Network

Models: Viability Theory, Naval Research Logistics 37, pp. 245–261.

[17] J. Choobineh, 1990. SQLMP: A Data Sublanguage for Representation and Formulation of Linear Mathematical Models, Technical Report, Department of Business Analysis and Research, Texas A and M University, College Station, TX.

[18] W.S. Cleveland and M.E. McGill (eds.), 1988. Dynamic Graphics for Statistics, Wadsworth and Brooks/Cole, Pacific Grove, CA.

[19] U. Dayal and H. Hwang, 1984. View Definition and Generalization for Database Integration in Multidatabase System, IEEE Transactions on Software Engineering SE-10:6, 628–644.

[20] D.R. Dolk, 1988. Model Management and Structured Modeling: The Role of an Information Resource Dictionary System, Communications of ACM 31, 704–718.

[21] S.E. Elmaghraby, 1977. Activity Networks: Project Planning and Control by Network Models, Wiley, New York, NY.

[22] C.K. Farn, 1985. An Integrated Information System Architecture Based on Structured Modeling, Ph.D. Thesis, Western Management Science Institute, University of California, Los Angeles, CA.

[23] R. Fourer, D.M. Gay and B.W. Kernighan, 1990. A Mathematical Programming Language, Management Science 36:5, 519–554.

[24] D. Garlan, 1987. Views for Tools in Integrated Environments, Ph.D. Thesis, Computer Science Department, Carnegie-Mellon University, Pittsburgh, PA.

[25] H.I. Gassmann and A.M. Ireland, 1992. Scenario Formulation in an Algebraic Modeling Language, Technical Report WP-92-7, School of Business Administration, Dalhousie University, Halifax, Nova Scotia.

[26] A.M. Geoffrion, 1987. An Introduction to Structured Modeling, Management Science 33, 547–588.

[27] A.M. Geoffrion, 1989. The Formal Aspects of Structured Modeling, Operations Research 37:1, 30–51.

[28] A.M. Geoffrion, 1989. Integrated Modeling Systems, Computer Science in Economics and Management 2:1, pp. 3–15.

[29] A.M. Geoffrion, 1989. Computer-Based Modeling Environments, European Journal of Operational Research 41:1, pp. 33–43.

[30] A.M. Geoffrion, 1990. SML: A Model Definition Language for Structured Modeling, Working Paper No. 360, Western Management Science Institute, University of California, Los Angeles, CA (Originally May, 1988).

[31] A.M. Geoffrion, 1990. A Library of Structured Models, Informal Note (revised), Western Management Science Institute, University of California, Los Angeles, CA.

[32] A.M. Geoffrion, 1990. Indexing in Modeling Languages for Mathematical Programming, Working Paper No. 371 (revised), Western Management Science Institute, University of California, Los Angeles, CA.

[33] F. Glover, 1983. Netform Modeling, Draft monograph, University of Colorado, Boulder, CO.

[34] F. Glover and H.J. Greenberg, 1987. Netforms Provide Powerful Tools for Enhancing the Operations of Expert Systems, Proceedings of the Rocky Mountain Conference on Artificial Intelligence, Boulder, CO, pp. 259–265.

[35] F. Glover, D. Klingman and N. Phillips, 1990. Netform Modeling and Applications, Interfaces 20:4, 7–27.

[36] F. Glover, D. Klingman and N.V. Phillips, 1992. Network Models in Optimization and Their Applications in Practice, Wiley-Interscience, New York, NY.

[37] H.J. Greenberg, 1978. A New Approach to Analyze Information Contained in a Model, in Energy Models Validation and Assessment, S.I. Gass (ed.), 517–524, NBS Pub. 569, National Bureau of Standards, Gaithersburg, MD.

[38] H.J. Greenberg, 1987. A Natural Language Discourse Model to Explain Linear Programs, Decision Support Systems 33, 333–342.

[39] H.J. Greenberg, 1990. A Primer for MODLER: Modeling by Object-Driven Linear Elemental Relations, University of Colorado at Denver, Mathematics Department, Denver, CO.

[40] H.J. Greenberg, 1990. A Primer for ANALYZE: A Computer-Assisted Analysis System for Mathematical Programming Models and Solutions, University of Colorado at Denver, Mathematics Department, Denver, CO.

[41] H.J. Greenberg, 1992. MODLER: Modeling by Object-Driven Linear Elemental Relations, Annals of Operations Research (to appear).

[42] H.J. Greenberg, 1992. Enhancements of ANALYZE: A Computer-Assisted Analysis System for Mathematical Programming Models and Solutions, ACM Transactions On Mathematical Software (to appear).

[43] H.J. Greenberg, J.R. Lundgren and J.S. Maybee, 1981. Graph Theoretic Methods for the Qualitative Analysis of Rectangular Matrices, SIAM Journal of Algebraic and Discrete Methods 2, 221–239.

[44] H.J. Greenberg, J.R. Lundgren and J.S. Maybee, 1989. Extensions of Graph Inversion to Support an Artificially Intelligent Modeling Environment, Annals of Operations Research 21, 127–142.

[45] H.J. Greenberg and F.M. Murphy, 1992. An In-Depth Survey of Modeling Languages for Mathematical Programming, Annals of Operations Research (to appear).

[46] D. Harel, 1988. On Visual Formalisms, Communications of the ACM 31:5, 514–530.

[47] T. Hürlimann, 1989. Reference Manual for the LPL Modeling Language (Version 3.1), Institute for Automation and Operations Research, University of Fribourg, CH-1700 Fribourg, Switzerland.

[48] R.D. Hurrion, 1986. Visual Interactive Modeling, European Journal of Operations Research 23, 281–287.

[49] C.V. Jones, 1989. Graph Grammars and Structured Modeling, Working Paper, The Wharton School, University of Pennsylvania, Philadelphia, PA.

[50] C.V. Jones, 1990. An Introduction to Graph-Based Modeling Systems, Part 1: Overview, ORSA Journal on Computing 2:2, 136–151.

[51] C.V. Jones, 1990. An Integrated Modeling Environment Based on Attributed Graphs and Graph-Grammars, Technical Report, The Wharton School, University of Pennsylvania, Philadelphia, PA.

[52] C.V. Jones, 1991. An Introduction to Graph-Based Modeling Systems, Part 2: Graph-Grammars and the Implementation, ORSA Journal on Computing 2:2, 136–151.

[53] C.V. Jones, 1991. Attributed Graphs, Graph-Grammars

and Structured Modeling, Technical Report, Simon Fraser University, Burnaby BC.

[54] D.A. Kendrick, 1989. Model Representations, CER Working Paper 89-1, Center for Economic Research, Department of Economics, University of Texas, Austin, TX.

[55] D.A. Kendrick, 1990. A Graphical Interface for Production and Transportation System Modelling: PTS, CER Working Paper 90-08, Center for Economic Research, Department of Economics, University of Texas, Austin, TX.

[56] D.A. Kendrick and R. Krishnan, 1989. A Comparison of Structured Modeling and GAMS, Computer Science in Economics and Management 2:1, 17–36.

[57] R. Krishnan, 1988. A Logic Based Approach to Model Construction, SUPA Technical Report, Carnegie-Mellon University, Pittsburgh, PA.

[58] S. Laufmann, R. Blumenthal, L. Sylvan, E. Freeman and D. Eitelbach, 1988. GNMS: A System for Modeling Network Structures, Technical Report, US West Advanced Technologies.

[59] W.A. Lodwick, 1991. Preprocessing Nonlinear Functional Constraints with Application to the Pooling Problem, ORSA Journal on Computing 4:2, 119–131.

[60] C. Lucas and G. Mitra, 1985. CAMPS: Preliminary User Manual, Department of Mathematics and Statistics, Brunel University, Middlesex, UK.

[61] P-C. Ma, F.H. Murphy and E.A. Stohr, 1989. A Graphics Interface for Linear Programming, Communications of the ACM 32:8, 996–1012.

[62] J. Mackinlay, 1987. Automating the Design of Graphical Presentations of Relational Information, ACM Transactions on Graphics 5:2, 110–141.

[63] MathPro, Inc., 1989. MathPro Usage Guide: Introduction and Reference, Washington, D.C.

[64] A. Meeraus, 1983. An Algebraic Approach to Modeling, Journal of Economic Dynamics and Control 5, 81–108.

[65] S. Miyamoto, K. Oi, O. Abe, A. Katsuya and K. Nakayama, 1986. Directed Graph Representations of Association Structures: A Systematic Approach, IEEE Transactions on Systems, Man, and Cybernetics 16:1. 53–61.

[66] H. Müller-Mehrbach, 1976. Graphically Illustrating LP Models, Presented at the 8-th Mathematical Programming Symposium, Budapest, Hungary.

[67] F.H. Murphy, 1988. A Knowledgebase for Formulating Linear Programs, in G. Mitra, H.J. Greenberg, F.A. Lootsma, M.J. Rijckaert, and H-J. Zimmermann (eds.), Proceedings of NATO ASI: Mathematical Models for Decision Support, Springer-Verlag, 451–470).

[68] F.H. Murphy and E.A. Stohr, 1986. An Intelligent System for Formulating Linear Programs, Decision Support Systems 2, 39–47.

[69] F.H. Murphy, E.A. Stohr and A. Asthana, 1992. Representation Schemes for Mathematical Programming Models, Management Science 38:7, 964–991.

[70] F.H. Murphy, E.A. Stohr and P. Ma, 1991. Composition Rules for Building Linear Programming Models from Component Models, Technical Report, School of Business, Temple University, Philadelphia, PA.

[71] R.E. Nance, 1981. Model Representation in Discrete

Event Simulation: The Conical Methodology, Technical Report CS81003-R, Department of Computer Science, Virginia Polytechnic Institute and State University, Blacksburg, VA.

[72] R.E. Nance, 1984. Model Development Revisited, Proceedings of the 1984 Winter Simulation Conference (S. Sheppard, U. Pooch and D. Pegden, eds.), 75–80.

[73] R.E. Nance and C.M. Overstreet, 1988. Diagnostic Assistance Using Digraph Representations of Discrete Event Simulation Model Specifications, Transactions of The Society for Computer Simulation 4:1, 33–57.

[74] P.C. Piela, 1989. ASCEND: An Object-Oriented Computer Environment For Modeling and Analysis, Ph.D. Dissertation, Department of Chemical Engineering, Technical Report EDRC 02-09-89, Carnegie-Mellon University, Pittsburgh, PA.

[75] P.C. Piela, T. Epperly, K. Westerberg and A. Westerberg, 1990. ASCEND: An Object-Oriented Computer Environment For Modeling and Analysis, Part 1-The Modeling Language, Technical Report EDRC 06-88-90, Carnegie-Mellon University, Pittsburgh, PA.

[76] L. Schrage, 1981. User's Manual for LINDO, Scientific Press, Palo Alto, Calif.

[77] L.W. Schruben, 1983. Simulation Modelling with Event Graphs, Communications of ACM 26:11, 957–963.

[78] N.C. Shu, 1988. Visual Programming, van Nostrand Reinhold.

[79] R.K. Som and R.G. Sargent, 1989. A Formal Develop-

ment of Event Graphs as an Aid to Structured and Efficient Simulation Programs, ORSA Journal on Computing 1:2, 107–125.

[80] J.F. Sowa, 1984. Conceptual Information Processing, North-Holland.

[81] G. Stephanopoulos, G. Henning and H. Leone, 1990. MODEL.LA. A Modeling Language for Process Engineering-I. The Formal Framework, Computers and Chemical Engineering 14:8, 813–846.

[82] G. Stephanopoulos, G. Henning and H. Leone, 1990. MODEL.LA. A Modeling Language for Process Engineering-II. Multifaceted Modeling of Processing Systems, Computers and Chemical Engineering 14:8, 847–869.

[83] M. Stonebraker, 1984. Adding Semantic Knowledge to a Relational Database System, in M.L. Brodie, J. Mylopoulos and J.W. Schmidt (eds.), On Conceptual Modelling, Springer-Verlag, 334–353.

[84] K. Sugiyama, S. Tagawa and M. Toda, 1981. Methods for Visual Understanding of Hierarchical System Structures, IEEE Transactions on Systems, Man, and Cybernetics 11:2, 109–125.

[85] A. Tuchman and M. Berry, 1990. Matrix Visualization in the Design of Numerical Algorithms, ORSA Journal on Computing 2:1, 84–92.

[86] E.R. Tufte, 1983. The Visual Display of Quantitative Information, Graphics Press, Cheshire, CT.

[87] J.S. Welch, Jr., 1987. PAM – A Practitioners' Approach to Modeling, Management Science 33, 610–625.
