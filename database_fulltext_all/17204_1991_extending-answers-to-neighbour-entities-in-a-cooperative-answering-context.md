---
otero_id: 17204
otero_key: "WVH4F2CH"
title: "Extending answers to neighbour entities in a cooperative answering context"
authors: "F. Cuppens; R. Demolombe"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90073-k"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Extending answers to neighbour entities in a cooperative answering context \*

F. Cuppens and R. Demolombe
ONERA-CERT, Toulouse Cedex, France

When a user has to retrieve information in a Database, a standard DBMS provides him just the exact answers to his queries. In a Cooperative Answering context a system has to provide him additional interesting information. In this paper we present a method to determine the interesting information from a given query and a knowledge base which represents the expertise of an expert in providing information. In this knowledge base are represented rules defining neighbour entities. These entities are obtained by extending the query to neighbour entity types or to neighbour conditions. The knowledge base is formalized in First Order Logic with two language levels: object level and meta level. The concept of neighbourhood between predicates or conditions is expressed at the meta level.

Keywords: Data base access; Cooperative answering; First order logic.

![](/api/attachments/WVH4F2CH/fulltext/images/acbf0b00e4d37717c958c0037247de950c5a4c93d5505628ddf0d1df5a365b02.jpg)

Robert Demolombe received his engineer diploma from ENSEEIHT school in 1967, and These d'Etat degree from Toulouse University in 1982. He is working in the Logic and Database group since 1971 at ONERA-CERT and gives lectures at ENSAE scool and at Toulouse University. His main topics of interest are applications of First Order Logic in the field of Data and Knowledge Bases, and presented articles in the following areas: query language semantics, query

optimization, recursive axiom evaluation and reasoning with incomplete information. He has now moving to applications of non-standard logics to practical reasoning.

![](/api/attachments/WVH4F2CH/fulltext/images/2cc43faabe55f0de9e7288df93b957003d8f6dd9ca3da58d31faac3c7026c090.jpg)

Frederic Cuppens was born in France in 1962. He received the engineer diploma from ENSEEIHT school in 1985, the Diplome d'Etudes Approfondies from University of Toulouse also in 1985, and the Thesis degree from ENSAE in 1988. During his thesis, he has studied the problem of cooperative answering to data base queries. He joined the ONERA-CERT institute in 1985, and from 1985 to 1988, he worked in the Logic and Database group. Since the beginning of 1989, he has moved to the domain of computer security. His main research interests include First Order Logic and Modal Logic.

\* This work was supported by the ESPRIT project: ESTEAM-316

## 1. Introduction

In the context of Advice Giving Systems or Decision Support Systems, if a user has to access data in a Database, a standard Relational DBMS is not well appropriate because it provides no more information than the precise answer to a given query, and in many cases users have not a very precise idea of the information in the Database that could help them to solve a particular problem.

That is why a more flexible system which can provide additional interesting information is more suitable in this context. In [4], we have presented a general methodology, called Cooperative Answering, to design such a system, where answers are entities with some of their attribute values. In this approach, there are two kinds of additional information: additional attributes for the entities requested by the query, or additional entities satisfying less restrictive conditions. We have shown in [5] how the concept of user's topic of interest allows to define the interesting additional attributes. The goal of this paper is to present a method to determine the interesting additional entities.

The following examples give an intuitive idea of what could be these additional entities. Let's consider a user who wants to plan a travel and asks the query:

What is the departure time and the price of the flights from Paris to New York, whose departure time is between 8a.m and 12a.m?

A standard Relational DBMS would supply the answer:

<table><tr><td>Flight</td><td>Departure-time</td><td>Price</td></tr><tr><td>AF001</td><td>11h00</td><td>27,715FF</td></tr><tr><td>AF015</td><td>10h30</td><td>8,825FF</td></tr></table>

However an employee in a Travel Agency, having experience in giving advices to plan a travel, knows that some people accept to “slightly” change the departure city or the arrival city, if the change of the total distance is not too big, or to “slightly” change the departure time. There may be different reasons to accept these changes, for example to get a less expensive flight. That is why this employee might propose the additional flights presented in Table 1.

A consequence of these changes is the necessity to give the user the departure city and the arrival city, though they are not requested in the query, because he has t know the conditions which have been changed. The reason to give these additional attribute values is very different than the reason presented in [5]. Indeed, in [5], additional attributes correspond to interesting topics or to exceptions with respect to some common sense rules.

Let's consider now the query:

What is the departure time of the flights from Paris to Brussels, whose departure time is between 7a.m and 11a.m?

The answer provided by an expert in a Travel Agency would be (it is not the exact answer since the price is provided although it is not explicitly requested by the user):

<table><tr><td>Flight</td><td>Departure-time</td><td>Price</td></tr><tr><td>AF638</td><td>08h05</td><td>1,850FF</td></tr><tr><td>AF642</td><td>09h25</td><td>1.850FF</td></tr></table>

In that case, it is sensible to relax the condition about the departure time like for the previous example, but it would not be sensible to change the conditions about the cities because the dis-

Table 1  
Additional flights from Paris to New York.

<table><tr><td>Flight</td><td>Departure-time</td><td>Price</td><td>Departure-city</td><td>Arrival-city</td></tr><tr><td>AF054</td><td>12h10</td><td>8,500FF</td><td>Paris</td><td>New York</td></tr><tr><td>AF020</td><td>09h30</td><td>7,850FF</td><td>Paris</td><td>Washington</td></tr><tr><td>BA017</td><td>09h00</td><td>6,750FF</td><td>London</td><td>New York</td></tr><tr><td>BA142</td><td>10h10</td><td>6,500FF</td><td>London</td><td>Boston</td></tr></table>

tance between Paris and Brussels is relatively small. Then, the expert might also propose the following additional answers:

<table><tr><td>Flight</td><td>Departure-time</td><td>Price</td></tr><tr><td>S651</td><td>11h07</td><td>1,620FF</td></tr><tr><td>Train</td><td>Departure-time</td><td>Price</td></tr><tr><td>SNCF281</td><td>07h48</td><td>450FF</td></tr><tr><td>SNCF483</td><td>10h08</td><td>450FF</td></tr></table>

The reason is that he knows that the distance between the two cities is not so important (less than 400 km), and that trains offers some advantages (for example they are cheaper and it is not necessary to go to an airport). Although it is not explicitly requested by the user, the attribute Price is inserted in the answer to give the user the possibility to compare the advantage of the trains with respect to the price. The implicit reasoning of the expert is that flights and trains are two particular means of travel, which can be interchanged in some contexts depending on the distance.

These two examples show two possibilities to give additional entities: to relax some conditions on the attributes in the query, or to consider entities of a “similar” type. Here “similar” means having the same father in some entity type hierarchy, plus other conditions.

Other works in the same stream can be found in the literature, in particular in [7] and [9]. The reason advocated in [7] to provide cooperative answers concerns empty answers; it can be noticed that our method is not limited to these situations. A more precise comparison with the methods defined in these papers is presented in the conclusion. The most important difference, in our view, is that it is formalized in First Order Logic.

In the next sections we have first to recall part of the background presented in $[4]$ and in $[2]$ . Then we introduce the concept of neighbourhood between conditions and between entity types, and the rules defining the contexts in which they can be applied. Farther off are presented the rules which transform a given query into other queries whose answers provide the additional information. The last section shows how it is possible to restrict the set of neighbour entities with respect to an optimization criterion.

## 2. Database structure representation

To define a query transformation we need a formalism to represent the queries and the database structure (the “database scheme”, in database terminology). The formalism we have selected is First Order Logic (FOL), and we distinguish two levels: object level and meta level (see [1] and [6]). The reasons to use two levels are that the transformations concern the meaning (their intention) of the queries, and not the entities they refer (their extension), and also because the concepts of the Entity-Relationship model, which are more convenient to define the method, cannot be directly expressed in a one level FOL.

## 2.1. Object level language

The object level language is a First Order Language where predicate symbols are those of the Relation schema of a given application, plus unary predicates to represent the relation domains.

For example the predicate symbols may be:

Dep-time(x, y), Dep-city(x, y),

Arr-city(x, y) ...

$$
\text { Means - of - Travel } (x), \text { Flight } (x), \text { Train } (x) \dots
$$

The query language is a restriction of this language to formulas of the form:

## Entity $\wedge$ Condition $\wedge$ Retrieved Attributes

where “Entity” is a formula with only entity type predicates and with the only logical operators $\wedge$ and $\vee$ ; “Condition” is whatever formula whose free variable are free variables of “Entity” or “Retrieved Attributes”; “Retrieved Attributes” is a conjunction of positive atomic formulas.

The first query is expressed in this language by the formula:

$Flight(x) \wedge$

$$
(D e p - c i t y (x, P a r i s) \wedge A r r - c i t y (x, N e w Y o r k) \wedge
$$

$$
\text { Dep - time } (x, y) \wedge (8 <   y) \wedge (y <   1 2)) \wedge
$$

$$
\left(D e p - t i m e (x, y) \wedge P r i c e (x, z)\right)
$$

The intuition behind this particular form is that a query expresses that a user wants to know the value of the attributes in the Retrieve Attribute part, for the entities having a type defined by the Entity part and satisfying the Condition part.

These restrictions make more easy the transformation definition.

## 2.2. Meta level language

The meta level language is a First Order Language whose predicate symbols are defined below. The predicates and the formulas of the object language are represented at this level by constants. These constants are the result of a coding function which assigns a code to any symbol or formula of the object language [1]. To understand more easily the meaning of these constants, the code of a formula is denoted by the formula itself between quotes.

For example:

$$
" F l i g h t (x) \wedge D e p - c i t y (x, P a r i s)"
$$

denotes a constant which is the code of the formula inside the quotes; note that at this level the object variable x has the status of a constant. In some cases we can have meta variables to denote any object formula of a particular form. For example if v is a meta variable:

```csv
"Flight(x) ∧ Dep-city(x,⟨v⟩)"
```

is a term, and $\langle v\rangle$ denotes that v has not the same status as x.

In the following when there is no risk of misunderstanding, the quotes and $\langle\rangle$ are omitted.

The structure of the Database is represented using the concepts of: Entity type, Attribute of an entity, Association, Attribute of an association, and Entity type structure.

We have for example the meta predicates:

Entity-type(x): $x$ is an entity type.

$Att(x, y)$ : x is an attribute of an entity of type y. $ISA(x, y)$ : x is a special case of the entity type y.

They allow for example to define the structure:

$$
\text { Entity - type } (\text { Flight }), \text { Entity - type } (\text { Train }),
$$

Entity-type (Means-of-Travel) ...

Att(Dep-time, Means-of-Travel),

Att(Dep-city, Means-of-Travel) ...

ISA( Flight, Means-of-Travel ),

ISA(Train, Means-of-Travel) ...

There are also axioms to express that ISA is a reflexive and transitive predicate, and that attributes are inherited in the ISA hierarchy of the entity types. See [5] for a presentation and a justification of these axioms, and for results about completeness and soundness relating axioms at the meta level and at the object level.

Only the meta predicates needed in this paper are presented here; a more detailed presentation can be found in [2].

The queries are represented with the meta predicates:

$$
\text { Entity } (x, y), \text { Condition } (x, y), \text { Ret - Att } (x, y)
$$

where x is the code of a query and y is the code of its Entity part (resp. Condition part, Retrieved Attribute part).

For example the first query is represented by the formulas:

$$
\begin{array}{r l} & E n t i t y (q t 1, \text { ``Flight } (x) \text { ''}) \\ & C o n d i t i o n (q t 1, \text { ``Dep - city } (x, P a r i s) \wedge \\ & \quad A r r - C i t y (x, N e w Y o r k) \wedge \\ & \quad D e p - t i m e (x, y) \wedge \\ & \quad (8 <   y) \wedge (y <   1 2)) \\ & R e t - A t t (q t 1, 1 1 D e p - t i m e (x, y) \wedge P r i c e (x, z) \text { '' }) \end{array}
$$

The formal definition of the answers is defined as usual (see for example [8]). In [3] we have shown that it is more meaningful to present the answers in the form of instantiated formulas than in the form of tuples. In the example in the Annex answers are represented in this form.

The next sections are structured in such a way that the analogy between neighbour entity types and neighbour condition is clearly pointed out.

## 3. Characterization of neighbour entities

3.1. Neighbour entity types

We introduce the meta predicate:

$$
\text { Neighbour - Ent } (q, E _ {1} (x), E _ {2} (x))
$$

to express that for the query q the entity type $E_{1}$ may be replaced by the entity type $E_{2}$ .

With this predicate it is possible to represent expert's knowledge relative to a particular application domain by rules like:

$$
\begin{array}{r l}\text {R1:}&\forall (q, x, v _ {1}, v _ {2})\\&\text {entity} (q, \text {"Flight(x)"} \wedge\\&\text {condition} (q, \text {"Dep - city(x, v_ {1})} \wedge\\&\text {Arr - city(x, v_ {2})"} \wedge\\&\text {Distance(v_ {1} , v_ {2}) <   400km}\\&\rightarrow \text {Neighbour - Ent} (q, \text {"Flight(x)}"\\&\text {"Train(x)"})\end{array}
$$

This rule expresses that for any query q about entities of type Flight, with a condition about the departure city and the arrival city such that their distance is less than 400km, it is relevant to transform the query by replacing the entity type Flight by Train.

It is easy to see with this example, that an entity type transformation based only on the ISA structure would lead to irrelevant and stupid transformations; for example to request Trains to go from Paris to New-York!

The antecedent part of this kind of rule allows to express in which particular context an entity type can be considered to be neighbour with another one. Of course, it is the role of experts to define this context.

It must be noticed that in the antecedent part some premises have to be proved at the meta level while other ones, like: $Distance(v_{1}, v_{2}) < 400km$ , have to be proved at the object level (see [1] for a study of the theoretic problems arising in the amalgamation of language and meta language).

There is also a rule R2, which is independent of a particular application domain, to express that the property of neighbourhood can be inherited to more specific entity type.

$$
\begin{array}{l}\text {R2:} \forall (q, e _ {1}, e _ {2}, e _ {1} ^ {\prime}, x)\\\quad N e i g h b o u r - E n t \big (q," e _ {1} (x)"," e _ {2} (x) " \big) \wedge\\\quad I S A \big (e _ {1} ^ {\prime}, e _ {1} \big)\\\quad \rightarrow N e i g h b o u r - E n t \big (q," e _ {1} ^ {\prime} (x)"," e _ {2} (x) " \big)\end{array}
$$

This rule says that if entity types $e_{1}$ and $e_{2}$ are neighbour and $e_{1}^{\prime}$ is a special case of $e_{1}$ then $e_{1}^{\prime}$ and $e_{2}$ are neighbour.

## 3.2. Neighbour conditions

We introduce the meta predicate:

$$
\text { Neighbour - Cond } (q, E (x), C _ {1}, C _ {2})
$$

to express that for the query q about entities of type E, where the Condition part “contains” the condition $C_{1}$ , this condition can be replaced by the condition $C_{2}$ .

This predicate allows to represent knowledge like:

R3: $\forall (q, 'x, v_1, v_2)$

$$
e n t i t y \big (q, “ M e a n s - o f - T r a v e l (x) ” \big) \land
$$

condition(q, “Dep-city(x, v₁) ∧

$$
A r r - c i t y (x, v _ {2}) ^ {\prime \prime})
$$

→ Neighbour-cond(q,

"Means-of-Travel(x)",

$$
" D e p - c i t y (x, v _ {1}) \wedge A r r - c i t y (x, v _ {2})",
$$

$$
" D e p - c i t y (x, v _ {1} ^ {\prime}) \wedge A r r - c i t y (x, v _ {2} ^ {\prime}) \wedge
$$

$$
\text { Neighbour - Travel } (v _ {1} ^ {\prime}, v _ {1}, v _ {2} ^ {\prime}, v _ {2}) ^ {\prime \prime})
$$

This rule expresses that for any query q about the entities Means-of-Travel, with a condition on departure city and arrival city, a neighbour condition can be obtained by replacing these two cities by two other “neighbour” cities. The “neighbour” cities are defined by the object level predicate Neighbour-Travel.

Another example of such a rule which transforms the conditions on departure time is:

R4: $\forall (q, x, h)$

$$
\text { entity } (q, \text {"Means - of - Travel} (x)) \wedge
$$

condition(q, "Dep-time(x, h)")

→ Neighbour-Cond(q,

"Means-of-Travel(x)",

“Dep-time(x, h)”,

$$
" D e p - t i m e (x, h ^ {\prime}) \wedge | h ^ {\prime} - h | <   1 5 m n")
$$

In the rules R3 and R4 the neighbour condition corresponds to a condition where the constants (cities or departure time) are replaced by neighbour constants. These neighbour constants are defined by an explicit set, in the case of cities, or by an implicit set, in the case of departure time.

We can also use the concept of neighbourhood to represent the fact that two predicates express neighbour condition. For example, if we have the predicates First-Class-Price(x, y) and Business-Class-Price(x, y) to represent the ticket price in first class or in business class, the next rule expresses that they impose neighbour conditions:

R5: $\forall (q, x, y)$

$$
\begin{array}{r l}&\text {entity} (q, \text {"Flight(x)"})\\&\text {condition} (q, \text {"First - Class - Price(x,y)")}\\&\rightarrow \text {Neighbour - Cond} (q,\\&\quad \text {"Flight(x)"})\\&\quad \text {"First - Class - Price(x,y) ",}\\&\quad \text {"Business - Class - Price(x,y)")}\end{array}
$$

This rule can be used for the query:

What is the flight company for the flights from Paris to New-York such that the first class ticket price is less than 10,000FF?

in order to replace the condition on a first class price by a condition on a business class price. It can be noticed that this kind of neighbourhood cannot be defined with the method presented in [7].

The rules R3, R4 and R5 are specific to a given application domain. The next rule R6 is general, and expresses that the property of neighbourhood is inherited to more specific entity types.

$$
\begin{array}{c}\text {R6:} \forall (q, c _ {1}, c _ {2}, e, e ^ {\prime}, x)\\N e i g h b o u r - C o n d (q," e (x)", c _ {1}, c _ {2}) \wedge\\I S A (e ^ {\prime}, e)\\\rightarrow N e i g h b o u r - C o n d (q," e ^ {\prime} (x)", c _ {1}, c _ {2})\end{array}
$$

All the rules presented in this section allow to derive, in a given application and for a given query, what are the entities neighbouring those explicitly requested by the user.

In this approach the notion of neighbourhood is defined by semantic knowledge contrary to other approaches based on general abstract computation rules, like in fuzzy sets.

## 4. Query transformation

In this section we define a query transformation which uses the information derived about the predicates Neighbour-Ent and Neighbour-Cond.

Roughly speaking in the previous section we have shown how to determine the interesting additional information. In this section we define how this information can be effectively obtained.

The transformed queries are defined with three meta predicates representing the transformation of the three parts of the query. We will not explicit the general rules which compound the transformation result of each part to build the global transformed queries.

## 4.1. Neighbour entity types

To transform the entity part we have the meta predicate:

$$
\text { Transf - Ent } (q, e _ {1}, e _ {2}, e, e ^ {\prime}),
$$

where e is the entity part of the query q, $e_{1}$ is an atomic entity type which appears in e, $e_{2}$ is the atomic entity type which can replace $e_{1}$ in e, and $e'$ is the entity part of the transformed query.

For example if in a query the entity part e is: $Flight(x) \vee Trains(x)$ , the atomic entity type $e_{1}$ : $Train(x)$ , could be replaced by $e_{2}$ : $Car(x)$ and $e'$ would be: $Flight(x) \vee Car(x)$ .

The meta predicates:

express respectively that e is an atomic entity type in the query q and that e is the entity part of the query.

entity $(q, e)$ and Entity $(q, e)$

The next rule R7 says that if for the query q the entity type $e_{1}$ is neighbour with $e_{2}$ , and $e_{2}$ doesn't appear in q, then the entity part in the transformed query is $e'$ obtained by replacing in e the subformula $e_{1}$ by $e_{2}$ .

R7: $\forall (q, e_1, e_2, e, e')$

Entity $(q, e) \wedge$

$$
\text { Neighbour - Ent } (q, e _ {1}, e _ {2}) \wedge
$$

$\neg$ entity $(q, e_2) \wedge$

$$
\rightarrow \text { Transf - Ent } (q, e _ {1}, e _ {2}, e, e ^ {\prime})
$$

Sometimes, when the entity type is transformed, the conditions have to be adapted to the new entity type. This is represented with the new meta predicate:

$$
\text { Transf1 - Cond } (q, e 1, e _ {2}, c, c ^ {\prime})
$$

where $c'$ is the transformed condition part when the entity type $e_{1}$ is replaced by $e_{2}$ in the query q.

The reason why this change is done may be the fact that the attributes which appear in c are not all defined for the entity type $e_{2}$ , or because by nature of the entity type $e_{2}$ the conditions have to be modified. For example if Flight are replaced by Train the condition on the departure time could be replaced by the same condition on the arrival time, because the duration of the travel is significantly longer with a train. Then we may have a rule like R8:

$$
\mathbf {R 8}: \forall (q, c, x, y)
$$

```javascript
condition(q, “Dep-time(x, y)”) ∧
Neighbour-Ent(q, “Flight(x)”, “Train(x)”) → Transf1-Cond(q, “Flight(x)”, “Train(x)”, “Dep-time(x, y)”, “Ar-time(x, y)”)
```

## 4.2. Neighbour conditions

To transform the condition part of a query we have the meta predicate:

$$
\text { Transf2 - Cond } (q, c 1, c 2, c, c ^ {\prime})
$$

where $c_{1}$ is a condition in the condition part c of q, $c_{2}$ is a condition which can be substituted to $c_{1}$ , and $c'$ is the resulting condition part.

The facts derived about the predicate Neighbour-Cond are used in the rule R9 to derive the corresponding transformed query:

R9: $\forall (q, e, c, c', c_1, c_2)$

Condition $(q, c) \wedge$

The Substitute predicate is used to replace in $c$ , the subformula $c1$ by $c_2$ to obtain $c'$ .

The Rel-for-all predicate is defined by:

DEF: $\forall (q, e, x)$

$$
\begin{array}{l}\text { Rel - for - All } (q, \text {"e(x)"} \leftrightarrow\\\left(\forall (e ^ {\prime}) e n t i t y (q, \text {"e^ {\prime} (x)} \text {"}) \rightarrow I S A (e ^ {\prime}, e)\right)\end{array}
$$

This predicate expresses that all the atomic entity formulas in the entity part of q are special cases of a given entity type e. With this predicate the transformation defined by the rule R9 is restricted to the cases where the neighbourhood between $c_{1}$ and $c_{2}$ is valid for all the atomic entity types in q.

For example if $c_{1}$ is neighbour of $c_{2}$ only for entities of type Flight, and the entity part of q is: $Flight(x) \vee Train(x)$ , the transformation R9 cannot be applied. Nevertheless if the entity part is: $TWA-Flight(x) \vee JAL-Flight(x)$ , and these two entity types are special cases of Flight, then the transformation can be applied.

The rule R10 defines the transformation in the case where Rel-for-all doesn't hold. In this case the transformed condition is applied only to entities such that Neighbour-Cond holds. This remark leads to substitute “ $e \wedge c_2$ ” to $c_1$ , instead of $c_2$ .

R10: $\forall (q, e, c, c', c_1, c_2)$

Condition $(q, c) \wedge$

$$
\text { Neighbour - Cond } (q, e, c _ {1}, c _ {2}) \wedge
$$

entity(q, e) ∧

$\neg Rel-for-All(q, e) \land$

$$
\text { Substitute } \left(c _ {1}, \text {"e} \wedge c _ {2} \text {"", c, c^{\prime}}\right)
$$

$$
\rightarrow \text { Transf2 - Cond } (q, c _ {1}, c _ {2}, c, c ^ {\prime})
$$

When entities satisfying neighbourhood conditions are provided, we have also to provide the value of modified conditions, because the user does not know how they have been changed.

For example, we have to provide the value of Departure-time and Arrival-time attribute when the rule R3 is used, and the value of Departure-time for the rule R4.

To provide this information, we introduce the meta-predicate:

$$
\text { Transf2 - Ret - Att } (q, c _ {1}, c _ {2}, I _ {1}, I _ {2})
$$

$I_{2}$ replaces $I_{1}$ and characterizes interesting information to be provided in neighbour answers when the condition $c_{1}$ is modified by $c_{2}$ .

The rule R11 defines the attribute values to be provided as a side effect of condition changes. The meta predicate Info-Int uses only syntactical criteria to recognize interesting attributes (actually, $I$ is built with all the attribute predicates which appear in $c_{2}$ )

R11: $\forall (q, e, c_1, c_2, I)$

$$
\text { Neighbour - Cond } (q, e, c _ {1}, c _ {2}) \wedge
$$

Info-Int $(c_{2}, I)$

$$
\rightarrow \text { Transf2 - Ret - Att } (q, c _ {1}, c _ {2}, \text { True }, I)
$$

About the condition transformation, we have also to make the following important remark:

Let's assume that we can deduce the two following theorems:

$$
\text { Neighbour - Cond } (q, s, c _ {1}, c _ {1} ^ {\prime})
$$

and Neighbour-Cond $(q, s, c_2, c_2')$

and that we have a query $q$ with an entity part $e$ and a condition part $C = c_{1} \wedge c_{2}$ .

From R9, we can derive:

$$
\text { Transf2 - Cond } (q, c _ {1}, c _ {1} ^ {\prime}, C, c _ {1} ^ {\prime} \wedge c _ {2})
$$

$$
\text { and   } \text { Transf2 - Cond } (q, c _ {2}, c _ {2} ^ {\prime}, C, c _ {1} \wedge c _ {2} ^ {\prime})
$$

and we will generate two transform queries $q_{1}$ and $q_{2}$ having respectively for condition part: $C_{1}=c_{1}^{\prime}\wedge c_{2}$ and $C_{2}=c_{1}\wedge c_{2}^{\prime}$ . This shows that in transformed queries, we change one condition at a time.

Actually, we could have generated only one query $q'$ with the following condition part: $C' = c_1' \wedge c_2'$ .

We have not chosen this solution, because we consider that $c_1' \wedge c_2$ and $c_1 \wedge c_2'$ formulas are closer to $c_1 \wedge c_2$ than $c_1' \wedge c_2'$ .

Of course, we do not assume that the neighbourhood relation is transitive, but the answers to the query $q'$ could be obtained by applying the condition transformation process to the queries $q_{1}$ and $q_{2}$ . Indeed, we would then obtain three queries having respectively the condition part $c_{1}'' \wedge c_{2}$ , $c_{1} \wedge c_{2}''$ and $c_{1}' \wedge c_{2}'$ with:

Neighbour-Cond(q, s, $c_1'$ , $c_1''$ )

and Neighbour-Cond $(q, s, c_2', c_2'')$

These queries are neighbour with neighbours of q.

Thus, we can introduce a concept of neighbourhood degree which allows to obtain more and more information by propagating the neighbourhood notion. This propagation has to be controlled by the user who can stop the process when he has obtained what he wants.

5. Optimization criteria to restrict neighbour entities

In many case, neighbour entities are interesting or not depending on the value of some criterion which is chosen to compare entities. These criteria strongly depend on the application domain, and on each particular context. In particular they may depend on the user category.

For example for some user category an optimization criterion may be the price of a travel, for other ones it may be the duration.

The idea is to avoid to provide neighbour entities having a criterion value greater than the lowest value for the answers of the initial query (in the case we want to minimize this criterion).

In this section we present meta predicates to represent this notion of optimization criterion and corresponding rules.

To introduce a new optimization criterion, we use the meta predicate:

$$
\text { Opt - Crit } (q, E (x), C)
$$

to express that for the query q about entities of type E, C is an optimization criterion formula.

For example, the rule R12 says that for Means-of-Travel entities, the Price may be an optimization criterion. So, if the entity part of the initial query q concerns entities of type E, neighbourhood entities of type Means-of-Travel will be provided if their price is less than the price of any initial solutions (characterized by the formula $E(x') \wedge C'$ ).

The formula $C'$ is a variant of the condition part $C$ where free variables $X = x_1, \ldots, x_n$ of $C$ have been renamed as $X' = x_1', \ldots, x_n'$ .

R12: $\forall (q, x, C, C', X')$

$$
\begin{array}{r l}&e n t i t y (q, \text {"E(x)"} \wedge\\&c o n d i t i o n (q, C) \wedge\\&V a r i a n t (C, C ^ {\prime}, X ^ {\prime})\\&\rightarrow O p t - C r i t (q,\\&\quad \text {"Means - of - Travel(x)",}\\&\quad \text {"Price(x,y)} \wedge\\&\forall (x ^ {\prime}, y ^ {\prime}, X ^ {\prime})\\&\quad E (x ^ {\prime}) \wedge P r i c e (x ^ {\prime}, y ^ {\prime}) \wedge C ^ {\prime}\\&\quad \rightarrow y <   y ^ {\prime}"\end{array}
$$

In the rule R13, we have considered that the flight duration is especially interesting for businessman.

$$
\begin{array}{l}\text {R13:} \forall (q, x, E, C, C ^ {\prime}, X ^ {\prime})\\\quad \text {entity} (q, “ E (x) ”) \wedge\\\quad \text {condition} (q, C) \wedge\\\quad \text {Variant} (C, C ^ {\prime}, X ^ {\prime}) \wedge\\\quad \text {User - Type} (\text {Business - man})\\\quad \rightarrow \text {Opt - Crit} (q,\\\quad \quad “ F l i g h t (x) ”,\\\quad \quad “ D u r a t i o n (x, y) \wedge\\\quad \forall (x ^ {\prime}, y ^ {\prime}, X ^ {\prime})\\\quad \quad E (x ^ {\prime}) \wedge D u r a t i o n (x ^ {\prime}, y ^ {\prime}) \wedge C ^ {\prime}\\\quad \quad \rightarrow y <   y ^ {\prime}"))\end{array}
$$

The meta predicate User-Type is used to define different types of users. For example, we could have the following types:

\- User-type (Tourist) (User travels for tourism reason).

\- User-type (Businessman) (User is a businessman)

There is also the rule R14, which is independent of a particular application domain, for expressing that an optimization criterion can be inherited by more specific entity types.

$$
\begin{array}{r l}\text {R14:}&\forall (q, e _ {1}, e _ {1} ^ {\prime}, c, x)\\&O p t - C r i t (q, “ e _ {1} (x) ”, c) \wedge I S A (e _ {1} ^ {\prime}, e _ {1})\\&\rightarrow O p t - C r i t (q, “ e _ {1} ^ {\prime} (x) ”, c)\end{array}
$$

The rules R15 and R16 express how to transform a query when an optimization criterion is used (respectively in the case of an entity type transformation and in the case of a condition transformation).

$$
\begin{array}{l}\text {R15:} \forall (q, e _ {1}, e _ {2}, C)\\\quad \text {Neighbour - Ent} (q, e _ {1}, e _ {2}) \wedge\\\quad \text {Opt - Crit} (q, e _ {2}, C)\\\quad \rightarrow \text {Transf1 - Cond} (q, e _ {1}, e _ {2}, \text {True}, C)\\\text {R16:} \forall (q, e, c _ {1}, c _ {2}, C)\\\quad \text {entity} (q, e) \wedge\\\quad \text {Neighbour - Cond} (q, e, c _ {1}, c _ {2}) \wedge\\\quad \text {Opt - Crit} (q, e, C)\\\quad \rightarrow \text {Transf2 - Cond} (q, c _ {1}, c _ {2}, \text {True}, C)\end{array}
$$

These rules say that the optimization criterion formula C has to be added to the condition part of the transformed query (by substituting the tautology formula “True” by the C formula).

When an optimization criterion is inserted in the transform query, it is useful to provide the user with the value of the optimized attribute; so, the user will have the possibility to compare the advantage of the neighbourhood entities with respect to the optimization criterion.

To provide this interesting comparative information, we introduce the meta predicate:

$$
\text { Att - Int } (q, E (x), I)
$$

where I is a comparative information useful to give for the entities of type E.

We use the rules R17 and R18, which are independent of a particular application domain, to express what is the interesting information respectively in the case of an entity type transformation and in the case of a condition transformation.

$$
\text { R17: } \forall (q, e, c _ {1}, c _ {2}, C, I)
$$

$$
\text { Neighbour - Cond } (q, e, c _ {1}, c _ {2}) \wedge
$$

$$
\text { Opt - Crit } (q, e, C) \wedge
$$

$$
\begin{array}{c}\text {Info - Int} (C, I)\\\rightarrow \text {Att - Int} (q, e, I)\end{array}
$$

R18: $\forall (q, e_1, e_2, C, I)$

$$
\text { Neighbour - Ent } (q, e _ {1}, e _ {2}) \wedge
$$

$$
\text { Opt - Crit } (q, e _ {2}, C) \wedge
$$

$$
\begin{array}{r l}&I n f o - I n t (C, I)\\&\rightarrow A t t - I n t (q, e _ {1}, I) \wedge A t t - I n t (q, e _ {2}, I)\end{array}
$$

We have to notice that comparative information must be provided for transformed query answers, but also for initial query answers.

## 6. Conclusion

We have presented a method and a formalism to define query transformations to provide users more information than it is explicitly requested by their queries. This method allows to design a system having a more cooperative behaviour than standard Relational DBMSs.

The method is based on the idea that the interesting information strongly depends on the context, and people having a long experience in providing information can explicit their expertise in our formalism.

The selected formalism is First Order Logic, but we distinguish an object level language and a meta level language. The meta level allows to express knowledge about the meaning of the queries. This formalism has two important advantages: it offers a very precise semantics, and it can be easily implemented using existing derivation mechanisms like Prolog. However, there are some differences between the rules presented in the paper, which are in pure logic, and Prolog where controls and “cut” must be introduced. We show, in the Annex, examples obtained from a first version of a prototype implemented in this language.

If we compare this method with the work presented by A. Motro in [7], it can be noticed that, in his work, interesting information is defined using a measure on attribute values and weights for each attributes; then, computation rules and a threshold define interesting entities. This approach has the same objective of what we call “condition transformation” but it cannot take into account the expertise of an expert; except in defining the attribute weights which is very crude information. Moreover this method doesn’t provide entities of a neighbour entity type.

In [9], L. Siklossy presents, through examples, a similar approach but there is no formalization and no general methodology that could be exported to other application domains. One can notice that the logical representation of the rules we use allows to easily change the rules when the application domain changes, because there is a clear distinction between the rules which are application dependent and those which are not. This has been tested by applying the method in another application domain related to portfolio management.

## References

[1] K. Bowen and R. Kowalski. Amalgamating language and metalanguage in Logic Programming. In Clark, editor, Logic Programming, Tärnlund, 1980.

[2] F. Cuppens. Comment fournir des réponses coopératives aux requêtes à une base de données. Thèse de doctorat, ENSAE, 1988.

[3] F. Cuppens. Un langage de requêtes pour obtenir des

réponses intelligentes. In Cinquièmes Journées Bases de Données Avancées, Genève, Suisse, 1989.

[4] F. Cuppens and R. Demolombe. Cooperative Answering: a methodology to provide intelligent access to Databases. In Second International Conference on Expert Database Systems, Tysons Corner, Virginia, 1988.

[5] F. Cuppens and R. Demolombe. How to recognize topics to provide cooperative answering. Information Systems, 14(2), 1989.

[6] R. Kowalski. The limitations if Logic. In J. Schmidt and C. Thanos, editors, Proc. Workshop on Foundations of Knowledge Base Management, Crete, 1986.

[7] A. Motro. Supporting goal queries in Relational Databases. In Proc. First International Conf. on Expert Database Systems, 1986.

[8] R. Reiter. Towards a logical reconstruction of relational database theory. In On Conceptual Modelling: Perspectives from Artificial Intelligence, Databases and Programming Languages. Springer Verlag, 1983.

[9] L. Siklossy. Impertinent question-answering: justifications and theory. In Proc. ACM National Conf., pages 39–44, 1978.

## Appendix

## Example of program execution

The query presented in this annex refers to the first example presented in the introduction. It shows an initial query, the answers to this query, and two transformed queries which provide neighbour entities by transformation of the condition part of the initial query. The answers have the form of formulas, instead of tuples. We use the syntax of predicate calculus where “&” denotes the conjunction. “Ex” denotes the existential quantifier, and “Not” denotes the negation.

![](/api/attachments/WVH4F2CH/fulltext/images/531c49d41a17bc3f212963d88ff2c96ac33157ef8070e824ed7e9abbb0851d32.jpg)

![](/api/attachments/WVH4F2CH/fulltext/images/6dce6663f89baf18645ce7bd34f6328e1e0cb0ab79e86243830891c9e0eaee66.jpg)
