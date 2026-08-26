---
otero_id: 17756
otero_key: "8SXSEE34"
title: "Modeling deductive information systems using ERMded"
authors: "Otto Rauh; Eberhard Stickel"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(96)00011-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Modeling deductive information systems using ERM $^{ded}$

Otto Rauh $^{a,*}$ , Eberhard Stickel $^{b}$

$^{a}$ Fachhochschule Heilbronn, Fachbereich Wirtschaftsingenieurwesen, Daimlerstraße 35, D-74653 Künzelsau, Germany $^{b}$ Informations Systems, European University Viadrina, Frankfurt (Oder), Germany

## Abstract

Today traditional information systems and deductive systems are modeled and implemented separately. Most users, however, demand integrated systems which meet their everyday information needs and have deductive capabilities as well. The well-known Entity-Relationship approach to conceptual data modeling is extended to cover modeling of such systems. First, a descriptive query language is introduced as a basis. Then it is shown how this language may be used to define derivable schema components. Finally, a classification of derivable data is given which allows the analyst to decide which derivable data should be included in the conceptual schema.

Keywords: Conceptual data modeling; Entity-Relationship model; Deductive information systems; Derivable data

## 1. Introduction

Within only 15 years, the Entity-Relationship approach to conceptual data modeling, which is based on the Entity-Relationship Model, or ERM [5], has become one of the most important methods for analyzing and modeling information systems, perhaps the most important at all in business data processing. Systems modelled with ERM are traditional in the sense that they do not allow to store knowledge or make deductions from the data in the database. For deductive information systems, normally specialized languages such as predicate logic, frames or semantic nets are used [16]. Consequently, systems modelled with ERM and systems designed with those special languages are implemented and used sepa rately. This separation is justifiable as long as distinctive deductive systems are concerned, consisting of many rules but only a few data, or rules that afford special evaluation techniques which cannot be applied in context with today's database systems. The “normal” user of business information systems, however, needs deductive capabilities which are comparably moderate, but he needs them in the context of his everyday information system.

The aim of this paper is to propose an extension to ERM, called $ERM^{ded}$ , which allows modeling integrated information systems with deductive capabilities, like those needed in business data processing. For this purpose, ERM is extended by adding means to define derivable data. Derivable data are data which are inferred (or deduced) from other data by applying a derivation rule. Data which are not deducible from other data are called original. In an ER schema, derivable data are represented by derivable schema components, i.e., derivable attributes, entity sets or relationship sets.

The number of possible derivations which can be made from certain original data is infinite. Of course, not all of them can be included in a conceptual ER schema. Derivable components in a conceptual schema should meet two conditions: they should be of interest to the users in the long run, and they should represent knowledge over and above that incorporated in the rest of the schema. We shall introduce a classification of data that allows the analyst to decide which data should be included and which should not.

Including a derivable schema component in a conceptual schema does not say anything about the form of its implementation. It might, for instance, be implemented as a view or stored like original data (be “materialized”). On the other hand, there might be derivable data in the final system that have not been included in the conceptual schema at all. The implementation of such data might be motivated by performance or ease of use. All in all, modeling at the conceptual level and implementation considerations are rather independent from one another and should be discussed separately. The focus of this paper is clearly on conceptual modeling, not on implementation. With regard to implementation, we content ourselves with the statement that for most schemata modelled with $ERM^{ded}$ implementations on the basis of relational database systems are possible.

## 2. Description of schema structure

An ERM $^{ded}$ schema consists of two parts: a structure part describing the components, and derivation rules. We shall discuss structure description in this chapter and deal with derivation rules in chapter three.

Fig. 1 shows the ER diagram of a small personnel information system which will serve as the basis for our examples. Solid lines have been used to draw original schema components, whereas broken lines represent derivable components. As an ER diagram cannot show all the information about a schema, we give an additional verbal description in a schema declaration language (Fig. 2). In the declaration of an entity set, we can see its attributes, which have been omitted from the diagram for the sake of clarity, and its identifier. Declarations of relationship sets include the names of the participating entity sets (also called participants, for short), their roles within the relationship set, and the cardinalities. Furthermore, there may be a list of one or more attributes. The schema is not quite complete, however. First, the domains of the attributes are missing as they are not relevant for what follows. Another missing part concerns derivable components. Although these components are declared in the schema, they are not distinguished from original schema components. It is up to the derivation rules part to provide this distinction.

![](/api/attachments/8SXSEE34/fulltext/images/82b432231d304b3583fb7edbce061cad7e1085c98ccdeb612317b6a0ef7e9d50.jpg)  
Fig. 1. ER diagram (Personnel Information System).

## 3. Description of derivation rules

## 3.1. ERC: A query language for the ERM

To be able to define derivation rules and to assign a meaning to derivable schema components, we need an ER query language. There have been several proposals for such languages, the first one being the fragmentary examples in Chen's original paper [5]. Other approaches are [20,13,7,14,11,9,10]. All these languages have in common that the result of a query is not an arbitrary entity or a relationship set. Most of them produce output in form of tables like a relational query language. An advantage of this approach is that the results of a query are always printable. But as we want to use the query language as a basis for defining derivable components such a language would not be suitable. We want to embed the derivable components in the schema and show their connections to the other schema components. We do not want to show them as an additional relational database.

The query language we shall use has its origin in the well-known relational tuple calculus, or TRC, which has already been proposed by Codd [6] (cf. [18] for a comprehensive discussion). We call it Entity-Relationship Calculus or ERC, for short. ERC may be used in the tradition of the ER languages mentioned above, that means with a table as the result of a query, but there are also extensions which allow a query to have an entity set or a relationship set as the result. We give one example of the traditional usage first. Suppose we want to have the lastnames and ID's of all employees who participated in at least one promotion program of the firm. An appropriate query is:

$$
\{e. L a s t n a m e, e. E m p I d | E m p l o y e e (e)
$$

$$
\wedge (\exists p) (P r o m o t e d (p) \wedge p: E m p l o y e e = = e) \}.
$$

The query consists of a target part, which is left of the “|”, and a condition part on the right. The common dot notation is used to represent values of attributes, as for example in e.LastName, which means the value of attribute Lastname in entity e. Unary membership predicates like Employee(e) are used to indicate that an object belongs to a certain entity or relationship set. Expressions like p: Employee are called participant functions. Their aim is to represent the entity participating in a relationship that plays the role denoted behind the colon. Thus p: Employee denotes the entity with role Employee that takes part in relationship p. Incidentally, in this case the name of the participant's role is the same as the name of the entity set it belongs to. The double equality sign “==” is a short form for expressing that entities or relationships are identical. Let $e_{1}$ and $e_{2}$ be two entities of the same type, and let S be the identifier of the entity set in question. Then $e_{1}=e_{2}$ is equivalent to $e_{1}.S=e_{2}.S$ . The semantics of “==” as an operation between relationships may be defined on the basis of its semantics for entities. Suppose R is an n-ary relationship set and $L_{1},\ldots,L_{n}$ are the roles of its participants. Then a relationship $r_{1}$ of type R is identical to a relationship $r_{2}$ of the same type iff $r_{1}:L_{1}=r_{2}:L_{1}\wedge\ldots\wedge r_{1}:L_{n}=r_{2}:L_{n}$ . Queries enclosed in {} have a set as result. That means the answer will not contain double rows. In order to allow double rows we have to enclose the query in [], expressing this way that the result is a list, not a set. There are also aggregate functions available, like Count, Sum, Min, Max, and Avg, which are all well-known from SQL, and “normal” functions that take one or more single values as arguments.

![](/api/attachments/8SXSEE34/fulltext/images/0bc8646c1cb6a8a082ca0d7ee97fc0cad20d3deb997d1648f1169f5681adb8b6.jpg)  
Fig. 2. Verbal description of schema structure.

## 3.2. Assignments

The declaration of derivable schema components in an ER schema consists of two parts:

(i) The components have to be declared in the schema description language like original components. In the ER-diagram, they may be marked as being derivable, but this is not a must. In the ER diagram of Fig. 1, derivable components are drawn in dotted lines, but in the verbal description of Fig. 2 no distinction has been made between original and derivable data.

(ii) Data from other schema components have to be assigned to derivable components. Exactly one assignment is needed for a derivable component. Its task is twofold: Firstly, it marks the component as being derivable, secondly, it is the manifestation of the derivation rule. We use the common symbol “:=” as assignment operator. Assignments to derivable components have the general form

## $\langle \text{schema component} \rangle := \langle \text{query} \rangle$ .

By such an expression, the result of the query on the right side is assigned to the derivable schema component mentioned on the left. The query is an ERC query like the one described above, but now for the results listed in the target part entity and relationship sets are also allowed. Derivable schema components may be entity sets, relationship sets, and attributes of original entity or relationship sets. A great number of derivable entity sets are subsets of other entity sets, which may be either original or derivable. The target part of the query in an assignment for a derivable component C consists of

\- an entity variable and, perhaps, a list of one or more attribute variables or arithmetic expressions, if $C$ is a subset of an entity set,

\- a relationship variable and, perhaps, a list of one or more attribute variables or arithmetic expressions, if $C$ is a subset of a relationship set,

\- a list of attribute variables or arithmetic expressions if $C$ is an entity set, but not a subset,

\- a list of entity variables representing the participants of $C$ , if $C$ is a relationship set, plus perhaps a list of attribute variables or arithmetic expressions,

\- a single attribute variable or arithmetic expression, if $C$ is an attribute.

We begin with an example for the last case. Entity set Employee contains an attribute Age which is derivable from DateOfBirth and the present date, known to the system as Today. Let us assume that there is a function years available which gives us the number of years between two dates.

Employee. Age

## := years(Today, Employee. DateOfBirth).

There is no explicit entity variable necessary for the employee. Instead, the name of the entity set itself is used as an implicit variable. When the assignment is executed, Employee takes the values of the employees in question, one after another.

Let us now extend our example to show an assignment for a subset of an entity set. Assume that all employees which are forty years or older and have been undertaken at least one promotion program enjoy the status of a senior employee.

SeniorEmployee

:= { e| Employee( e )

$\wedge e. Age \geq 40 \wedge (\exists p) (Promoted(p))$

$\wedge p: Employee = = e) \}$ .

Regular entity sets have to be connected to the rest of the schema by at least one derivable relationship. This is in contrast to subsets, where there is a connection to the superset merely as a consequence of the subset declaration. Suppose, that the firm provides promotion programs only for highly efficient employees, and our information system is expected to deduce these employees and the appropriate programs. An employee is eligible for a certain promotion program if all the following conditions are fulfilled: (i) his grade of efficiency is higher than 150, (ii) he is not older than the maximum age that has been fixed for the program, (iii) there is no other program with a smaller maximum age where condition (ii) is met. A derivable entity set PossiblePromotion may be used to provide all pairs of employees and programs fulfilling these prerequisites. It is connected to both Employee, by a relationship set GetsPromotion, and to PromotionProgram, by a relationship set ProgrToApply.

Possible Promotion

:= { p.ProgrId,e.EmpId|PromotionProgram( p)

$\wedge$ Employee(e) $\wedge e.$ Efficiency $>150$

$\wedge e.Age \leq p.MaxAge$

$\wedge\neg(\exists r)(PromotionProgram(r)$

$\wedge e.Age \leq r.MaxAge$

$\wedge r.MaxAge < p.MaxAge)$ ,

GetsPromotion

:= { e, p | Employee( e) ∧ PossiblePromotion( p )

$\wedge p. EmpId = e. EmpId \}$ ,

ProgrToApply

$= \{r,p|PossiblePromotion(r)$

$\wedge$ PromotionProgram $(p)\wedge r.$ ProgrId

$= p.ProgrId\} .$

As PossiblePromotion is an associative entity set, a relationship set could have been used to model the situation just as well. The reason for choosing an entity set was that an entity set can be used as a participant in a relationship set, whereas a relationship set cannot. Let us extend our example in this direction. Assume, that every employee participating in a promotion program is given a senior employee as a mentor to guide him. To become mentor in a certain promotion, a senior employee has to meet two additional conditions: (i) he must be at least five years older than the employee promoted, and (ii), he must have been undertaken the program himself. We use a derivable relationship set SuggestedMentorship between SeniorEmployee and PossiblePromotion to provide all possible constellations of mentors and promotions according to the conditions above. Promotions already fixed or carried out are contained in relationship set Promotion.

SuggestedMentorship

:= {m, g: Possible Promotion|SeniorEmployee(m)

$\wedge$ GetsPromotion(g)

$\wedge m.Age-g:Employee.Age\geq5$

$\wedge(\exists t)(Promoted(t)\wedge t:Employee==m$

$\wedge t:$ Promotion.ProgrId

$= g: Possible Promotion.ProgrId)\} .$

Please notice that any relationship set connected to a derivable entity set must be derivable as well. With this request, we ensure that no original (and materialized) data be ever dependent on the existence of derivable data. Such a dependence would be inappropriate, as derivable data change whenever the underlying original data change.

## 3.3. Recursively derived components

A component is recursively derived if it refers to itself, either directly in its own assignment, or indirectly through a chain of assignments.

Recursive derivation may be used to infer transitive closures. Suppose, the original relationship set Hierarchy in Fig. 3 contains all pairs of persons such that one of them is directly subordinate to the other. If we want all pairs of persons with one of them directly or indirectly subordinate to the other, we may define a derivable relationship set TotalHierarchy, which is the transitive closure of Hierarchy:

![](/api/attachments/8SXSEE34/fulltext/images/cc1311ecedbf953e3e18484da97ae385477f02f681e7a9b4763d3eba28efc814.jpg)  
Fig. 3. Recursively derived relationship set TotalHierarchy.

TotalHierarchy

$$
:= \{e 1, e 2 | E m p l o y e e (e 1) \wedge E m p l o y e e (e 2)
$$

$$
\wedge ((\exists h) (H i e r a r c h y (h) \wedge h: S u p e r i o r = = e 1
$$

$$
\wedge h: \text { Subordinate } = = e 2)
$$

$$
\vee (\exists h, t) (H i e r a c h y (h)
$$

$$
\wedge \text { TotalHierarchy } (t) \wedge h: \text { Superior } = = e 1
$$

∧ h:Subordinate = = t:Superior

$$
\left. \wedge t: \text { Subordinate } = = e 2)\right) \}.
$$

## 3.4. Additional rules for formulating queries

There are some rules in addition to those of ERC syntax which must be observed to ensure that queries and assignments be executable. The problem has already been discussed in the context of TRC and Datalog [17]. Thus a very short treatment may suffice.

The following assignment does not yield a reasonable result though it is in accordance with ERC syntax:

$$
\text { NotSeniorEmployee: } = \{e | \neg \text { SeniorEmployee } (e) \}.
$$

To be specific, the result is an infinite set of entities. Certainly the system could enumerate the entities in set SeniorEmployee but not those in the complement $\neg SeniorEmployee$ . The query may be “repaired” by restricting e to entity set Employee:

$$
\text { NotSeniorEmployee: } = \{e | \text { Employee } (e)
$$

$$
\wedge \neg S e n i o r E m p l o y e e (e) \}.
$$

Queries producing finite results are called safe. Safe queries can be achieved by obeying the following three rules:

(1) Every entity variable and every relationship variable in the target list must appear in the condition as well.

(2) For every occurrence of such a variable in the condition the following must hold: it is an argument of a nonnegated schema predicate or it is connected with such a predicate by $\wedge$ .

(3) Whenever an V operator is used, the two formulas connected have only one free variable, and it must be the same variable.

Further complications may arise if recursion is used together with negation. The subject has been thoroughly examined in the theory of deductive databases [17,8,4]. The concept of stratified negation describes uses of negation in the presence of recursion, where reasonable results can be achieved. Roughly speaking, a set of assignments is stratified if there is no negated predicate involved in a recursion.

## 3.5. Mixed data

When we wrote down the assignment for entity set SeniorEmployee in Section 3.2 we tacitly assumed that all employees enjoying this status fulfilled the condition in the right part of the query. Let us now give up this assumption. Just as before, we shall presume that employees meeting the condition become senior employees. But, in addition, we shall allow for an employee to become a senior employee just by being appointed by the senior management.

The difference between the two situations may be shown more precisely by regarding the derivation rules from the logical point of view. In the former situation, there was obviously an equivalence between the condition stated in the query and being a senior employee. Every employee meeting the condition got the status; everyone who got the status fulfilled the condition:

$$
\text { Employee } (e) \wedge e. \text { Age } \geq 4 0 \wedge (\exists p) \text { Promoted } (p)
$$

$$
\wedge p: E m p l o y e e = = e) \leftrightarrow S e n i o r E m p l o y e e (e)
$$

Allowing now senior employees to be appointed without meeting the condition changes the derivation rule into an implication:

$$
E m p l o y e e (e) \wedge e. A g e \geq 4 0
$$

$$
\wedge (\exists p) \text { Promoted } (p) \wedge p: E m p l o y e e = = e)
$$

→ SeniorEmployee(e).

If we adhered to our former schema entity set SeniorEmployee would now contain mixed data: employees meeting the condition and inserted by derivation on the one hand, employees appointed by senior management and inserted as original data on the other. We prefer, however, not to use mixed predicates to capture such situations. In Fig. 4, a simple solution is shown. Employees being appointed without satisfying the condition are inserted into original entity set AppointedSeniorEmployee. DerivedSeniorEmployee is a derivable entity set containing only those employees fulfilling the condition: DerivedSeniorEmployee

$$
\begin{array}{r l} & := \left\{e | E m p l o y e e (e) \wedge e. A g e \right. \\ & \geq 4 0 \wedge (\exists p) P r o m o t e d (p) \\ & \wedge p: E m p l o y e e = = e) \}. \end{array}
$$

All senior employees, derived as well as appointed ones, are contained in SeniorEmployee which is the union of DerivedSeniorEmployee and AppointedSeniorEmployee and, consequently, is a derivable entity set:

SeniorEmployee

:= { e | AppointedSeniorEmployee( e )

$\vee$ DerivedSeniorEmployee(e) } .

## 3.6. Comparing $ERM^{ded}$ with other approaches

In order to be able to assess the power of $ERM^{ded}$ , a comparison of ERC with languages of deductive databases might be useful. The most widely known language for such systems is Datalog [17]. Datalog in its original form is less powerful than ERC as negated predicates are not permitted in rule bodies. Datalog $^{neg}$ , an enhanced version of Datalog, offers the same possibilities as ERC with respect to negation [4,8,17]. Another extension of Datalog, Datalog $neg + fun$ , permits the use of functions in addition to negation. Datalog $neg + fun$ is more powerful than ERC at the present time as user-defined functions are not allowed in ERC.

With respect to practical applications, a comparison of ERC with SQL will be helpful as, in most cases, $ERM^{ded}$ schemata will be converted into relational databases after conceptual modeling. In contrast to ERC, SQL2 in its interactive form does not permit recursive queries. Thus such queries and assignments have to be implemented by writing programs using embedded SQL. Nonrecursive queries, however, may be translated into interactive SQL without any difficulties. The new standard, SQL3, which is already being developed will at least permit direct recursion in interactive usage.

## 4. S-derivable and m-derivable data

Now we want to introduce a classification of derivable data that has great significance for the treatment of those data in conceptual modelling. The basic criterion used to classify the data is the source of their meaning to the user. Let us go back to the example, where a subset SeniorEmployee of Employee was assigned those persons who are forty or older and took part in at least one promotion program. The basis for this assignment was a rule saying that such employees be senior employees, whatever this may mean. Please note that there has been information added to the system by this rule, and this additional information has been expressed in the name of the derivable component.

![](/api/attachments/8SXSEE34/fulltext/images/492e88a99240bf0b64775bcbfb3962d7272705030c358a3faec236f1bc8bdc99.jpg)  
Fig. 4. Modeling mixed data.

Now let us change the assumptions to illustrate another kind of derivable data. Assume now that the status of a senior employee is not known in our firm. Consequently, there is no rule concerning senior employees. Nevertheless, we could define an entity set consisting of the same entities as in SeniorEmployee. In the assignment for this entity set we would even use the same query. But now “SeniorEmployee” would not be an appropriate name for it. Without a rule, the schema component on the left side of an assignment has only the meaning that is expressed by the query on the right. As we use a descriptive language we can recognize this meaning at a glance. Considering the query, an appropriate name would now be EmployeeWhoIsAtLeastFortyAndHasParticipatedInAPromo-

tionProgram. But even if we chose the name X for our entity set, there would be no difficulties for the user to get its meaning if only he knew the right side of the assignment.

We call schema components like SeniorEmployee, which have an additional meaning besides that expressed by the query, s-derivable. The s stands for special, as there is a special derivation rule which provides the additional meaning.

If there is no such rule, as is the case in the second version of our example, a derivable schema component gets its meaning only from the meaning of the data referred to in the query and from the meaning of the language operations applied. There is an infinite number of possible derivations of this kind. The only limit we have to observe is that the language operations applied make sense in connection with the data referred to. We cannot, for instance, multiply two strings.

Thus the query language forms the basis for all such derivations. Using its operations, concrete derivation rules can be formulated in the form of assignments. In every such case, the meaning of a concrete rule is completely determined by the meanings of the operations applied and the data referred to. We may say that the query language provides a set of meta derivation rules where all concrete derivation rules get their meanings from. Therefore we call components like that one in the second version of our example derivable by meta derivation rules, or simply m-derivable.

Classifying data as being m-derivable or s-derivable is helpful when we have to decide if they should be included in the conceptual schema. As m-derivable data do not add any information to the schema they should be omitted. Every user capable of the database language may generate them just as he likes. In contrast, s-derivable components represent knowledge that is not incorporated in the original data and the operations of the database language. If we include them in the conceptual schema the resulting information system will have deductive capabilities, and these capabilities will be visible to the modellers and the users of the schema from the beginning. There is one condition, however, which s-derivable data in the conceptual schema should meet. As this schema is a long-term plan for the enterprise's data, it should only contain concepts that will be of interest in the long run.

## 5. Conclusion

Extending the ERM to include derivable schema components has several advantages: (i) Modellers can stay within in the ERM, which is a very popular and illustrative language, and they need not split a system into several parts. (ii) They get an additional view onto the system. If a deductive system is modelled in logic alone, derivable data are represented in the derivation rules only. Integrated in the ERM, the relationships of the data with other data are visible. (iii) The extensions provide a basis for a sound treatment of derivable data in the ERM. Up to now, there were no means to handle such data in the ERM. (iv) As far as only nonrecursive assignments are used, the conceptual model can easily be transformed into a relational database scheme. This may be done automatically.

There are also some limits that have to be observed: (i) If recursive assignments are used, additional programming efforts have to be made to supply the data. (ii) In systems with a lot of rules, say some thousands, the clarity and expressiveness, which is normally an advantage of ER schemas, might no longer be existent. Also, the benefits of the approach are moderate if the system consists of very few entity sets, whereas the derivation rules result in a great number of relationship sets.

## References

[1] M. Astrahan et al., System R: Relational Approach to Database Management, ACM TODS 1, No. 2 (1976).

[2] P. Atzeni and V. De Antonellis, Relational Database Theory (Benjamin/Cummings, Redwood City, CA, 1993).

[3] C. Batini, S. Ceri and S. Navathe, Conceptual Database Design: An Entity-Relationship Approach (Benjamin/Cummings, Redwood City, CA, 1992).

[4] S. Ceri, G. Gottlob and L. Tanca, Logic Programming and Databases (Springer-Verlag, Berlin, 1990).

[5] P. Chen, The Entity-Relationship Model: Toward a Unified View of Data, ACM TODS 1, No. 1 (1976).

[6] E. Codd, Relational Completeness of Data Base Sublanguages, in: R. Rustin, Ed., Data Base Systems (Prentice-Hall, Englewood Cliffs, NJ, 1972).

[7] R. Elmasri and G. Wiederhold, GORDAS: A Formal, High-Level Query Language for the Entity-Relationship Model, in: P. Chen, Ed., Entity-Relationship Approach to Information Modelling and Analysis (Elsevier, Amsterdam, 1981).

[8] G. Gardarin and P. Valduriez, Relational Databases and Knowledge Bases (Addison-Wesley, Reading, MA, 1989).

[9] M. Gogolla and U. Hohenstein, Towards a Semantic View of an Extended Entity-Relationship Model, ACM TODS 16, No. 2 (1991) 269–316.

[10] U. Hohenstein, Automatic Transformation of an Entity-Relationship Query Language into SQL, in: F. Lochovsky, Ed., Proceedings of the 8th International Conference on Entity-Relationship Approach (North-Holland, Amsterdam, 1990).

[11] J.-P. Lagrange, A Knowledge-Based System and an ER Query Language for Accessing Relational Databases, in: H. Kangassalo, Ed., Proceedings of the 9th International Conference on Entity-Relationship Approach (Lausanne, 1990).

[12] J.W. Lloyd, Foundations of Logic Programming, 2nd ed. (Springer-Verlag, Berlin, 1987).

[13] H.M. Markowitz, A. Malhotra and D.P. Pazel, The ER and EAS Formalisms for System Modeling, and the EAS-E Language, in: P. Chenn Ed., Entity-Relationship Approach to Information Modeling and Analysis (Elsevier, Amsterdam, 1981).

[14] C. Parent, H. Rolin, K. Yetongnon and S. Spaccapietra, An ER Calculus for the Entity-Relationship Complex Model, in: F. Lochovsky, Ed., Proceedings of the 8th International

Conference on Entity-Relationship Approach (North-Holland, Amsterdam, 1990).

[15] O. Rauh, Some Rules for Handling Derivable Data in Conceptual Data Modeling, in: A.M. Tjoa and I. Ramos, Eds., Database and Expert Systems Applications, Proceedings of the International Conference in Valencia, Spain (Springer-Verlag, Berlin, 1992).

[16] E. Rich and K. Knight, Artificial Intelligence, 2nd ed. (McGraw-Hill, New York, 1991).

[17] J.D. Ullman, Principles of Database and Knowledge-Base Systems, Vol. I (Computer Science Press, Rockville, Maryland, 1988).

[18] J.D. Ullman, Principles of Database and Knowledge-Base Systems, Vol. II: The New Technologies (Computer Science Press, Rockville, Maryland, 1989).

[19] R. Winter, Design and Implementation of Derived Entities — Enhancing the Entity-Relationship Approach to Support the Generation of Database Triggers, Proceedings of the 12th International Conference on Entity-Relationship Approach (Arlington, TX, 1993).

[20] C. Zaniolo, The Database Language GEM, in: Proceedings of the 1982 ACM-SIGMOD Conference on Management of Data (San Jose, CA, May 1982).

![](/api/attachments/8SXSEE34/fulltext/images/d9f5926a7df412e95ffeda577d8fa702733922198a04a801da83f4c8a3dc770a.jpg)

Otto Rauh is Professor in Computer Science at Fachhochschule Heilbronn, Germany. He received his Diploma and Ph.D. from Nuremberg University. Rauh has authored a book on information management and numerous articles for international journals and conferences. Currently, his research concentrates on modeling informations systems and object-oriented software construction.

![](/api/attachments/8SXSEE34/fulltext/images/f2f82761b1d4fe8a86154d046540661f380c7afe0c67ade9bb71e6cea224d411.jpg)

Eberhard Stickel is Full Professor in Informations Systems at the European University Viadrina in Frankfurt (Oder), Germany. He received a Ph.D. in Mathematics from the University of Ulm. His main research interests are data and process modeling, as well as economics of IT-use. His research appeared in international journals such as DATABASE, Information Systems, Journal of Computing and Information and in Proceedings of International Conferences.
