---
otero_id: 24898
otero_key: "9ZE5EP4Z"
title: "A Method for Easing Normalization of User Views"
authors: "Dinesh Batra"
year: "1997"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1997.11518159"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Method for Easing Normalization of User Views

## Dinesh Batra

To cite this article: Dinesh Batra (1997) A Method for Easing Normalization of User Views, Journal of Management Information Systems, 14:1, 215-233, DOI: 10.1080/07421222.1997.11518159

To link to this article: http://dx.doi.org/10.1080/07421222.1997.11518159

![](/api/attachments/9ZE5EP4Z/fulltext/images/a92bfd06ef6283e2039d5e8486e5899c402d39e3ee47a95d0dbcee69ec9ddcfa.jpg)

Published online: 08 Dec 2015.

![](/api/attachments/9ZE5EP4Z/fulltext/images/2e84402c6a25c260bd1f2a8bc9d4e097de1cbc8bcdd33bc80a7fa1b08c93df45.jpg)

Submit your article to this journal ↗

![](/api/attachments/9ZE5EP4Z/fulltext/images/577778c17927bd31576a3d7c687aa2a62722cac69b98303a63670c13011c32d1.jpg)

View related articles ↗

# A Method for Easing Normalization of User Views

DINESH BATRA

DINESH BATRA is Associate Professor in Decision Sciences and Information Systems at the College of Business Administration at Florida International University. He received his Ph.D. from Indiana University. His research has been published in Management Science, Communications of the ACM, International Journal of Human-Computer Studies, European Journal of Information Systems, Computers and Operations Research, Information and Management, Journal of Database Management, and others. His research interests focus on usability issues in database design and use.

ABSTRACT: Currently, most database management systems (DBMS) are based on the relational data model. Design methods that target relational models as the end product of logical design are generally based on the entity relationship model (ER) or semantic object model. Such methods entail developing an ER or semantic object representation followed by translation to the relational representation by the designer or by a CASE tool. However, there is no popular method that uses the relational concepts directly, that is, without an intermediate representation such as ER. Mathematically rigorous approaches using decomposition or synthesis do not seem to have been adopted by designers. When user views are complex, designers may encounter difficulty in the absence of an understandable method. This paper suggests a practical method for arriving at a normalized solution of user views.

KEY WORDS AND PHRASES: derived dependency, logical database design, normalization, relational data model.

IN RECENT YEARS, RELATIONAL DATABASES HAVE PROLIFERATED in organizations and are being designed and used by professionals as well as nonspecialists [1]. The emergence of SQL as an ANSI standard [7] is a testimony to the popularity and future of relational databases. In contrast, the promise of semantic data models [15] has not been translated into commercial implementations, and researchers seem to be losing interest in the area [18]. These models have been used as an intermediate representation for relational databases. Object-oriented data models show promise [9], although it is too early to speculate if a revolutionary change in their adoption is likely in the near future. Much of the productivity gains may be attributed to visual front ends that accompany the implementation of software based on these models. Such visual front ends are now also available for relational systems. Interest in newer data models, however, has overshadowed the need to conduct research in enhancing the usability of methodologies based on relational models, which continues to be the most important database structuring model in the business area.

Many logical design methodologies (e.g., [20]) have been proposed for relational databases. These are typically top-down approaches that recommend developing an entity relationship (ER) diagram [4] or semantic object model [11] and translating it into the relational representation [6]. These approaches are quite effective (e.g., [2]), but the designer needs to be aware of the principles underlying the target, that is, the relational database. A simple example available in most textbooks illustrates the point: If there are three entities (or objects): CUSTOMER, ORDER, and PRODUCT, then each of the three pairs is involved in binary relationships. However, the designer who is aware of relational principles will understand that the many-many relationship between CUSTOMER and PRODUCT is derived from the one-many CUSTOMER-ORDER and the many-many ORDER-PRODUCT relationships. This is based on the relational notion of derived dependency; the example is explained further later.

The logical design of relational databases is generally based on normalization, which is achieved either by decomposing user views or by synthesis $[12]$ . Textbooks generally recommend that designers try to achieve fourth-normal or Boyce-Codd form. The normalization approach is based on functional and multivalued dependencies. In practice, one expects designers to use normalization principles in the design of relational databases.

However, there is no reported study that reveals how designers actually employ these principles. There are theoretical approaches $[12]$ , such as decomposition, and syntheses that lead to rigorous relational solutions, but such approaches may be too complex and impractical for the typical designer. Most textbooks illustrate the various normal forms but do not really point out a precise method of using these principles and leave the utilization of the normal forms to the designer. The typical textbook usually considers a problem designed to lead a student step by step from the first to the third or fourth normal form. This enables the student to understand the principles of normalization. However, understanding normalization is not quite the same as using it to model relations. Normalization involves a set of principles but does not describe a modeling process. A students needs a method that describes such a process and illustrates how the principles are satisfied. For example, such a process would suggest where to start and when to finish in modeling, say, a form or a report.

Further, normalization rules by themselves do not lead to minimum solutions. For example, let us revisit the customer-order-product example. The following solution is in third normal form:

CUSTOMER(Cust#, CustName, Address, City, State, Zip)

ORDER(Order#, OrderDate, Cust#)

PRODUCT(Product#, ProdName, Price)

LINEITEM1(Order#, Product#)

LINEITEM2(Cust#, Product#)

The relation LINEITEM2 does not violate the first through fourth normal forms, yet the seasoned designer recognizes it as a derived relation. In other words, the solution is not minimum.

There is a need, therefore, for a method that will help a novice designer tackle complex user views. True, expert designers do not really need such a method since they can use their intuition and sophisticated heuristics to perform the logical design; however, novice and intermediate designers may benefit from a systematic database design method. The method would also be useful to end users $[17]$ , who are usually novice designers.

Conceptual and logical database design tasks are important but difficult tasks, especially for large databases. Conceptual design cannot be conducted completely by automatic tools, and the designer has full responsibility for the process of understanding and transforming requirements into conceptual schemas $[1]$ . This also applies to logical design if not preceded by conceptual design, that is, if the logical design stems directly from user requirements. Thus, the designer needs a method that will facilitate the design process. Many methodologies have been proposed to develop a normalized relational database.

Teorey, Yang, and Fry [20] proposed LRDM (Logical Relational Database Methodology), a methodology for attaining relational databases by first developing the extended entity relationship (EER) representation. The EER model is an extension of ER that includes the generalization concept. The methodology involves developing an EER diagram that can then be translated into a relational model. As argued earlier, such a methodology is successful only if the designer has a good idea about the principles of target representation. This also applies to Nijssen's Information Analysis Model (NIAM) [14] and Kroenke's semantic object model [11] or an object-oriented model such as suggested by Blaha, Premerlani, and Rumbaugh [3].

This paper presents a method to model an application that consists of a collection of user views, which are reports and forms required in a business application. Since user views are easily available and capture the inputs and outputs of an application, they are reliable sources of user requirements. Although there are other methodologies based on forms (e.g., [5]), these have not shown how dependencies are preserved as the form is decomposed into relations or how the solution does not embed derived dependencies. The method presented in this paper has a theoretical basis.

## View Decomposition Approach

IN ADDRESSING LOGICAL DATABASE DESIGN, FEW TEXTBOOKS go beyond the normalization principles (i.e., the three or four normal forms). The notion of derived dependency is rarely discussed in texts, even though it is commonly encountered in cases [13] and is an important concept for attaining solutions with minimum redundancy. The view decomposition approach for logical design of relational databases comprises the following steps:

1. Normalization of each user view. The normalization is usually carried on to the fourth normal form. Further, any data within a view that can be identified as arithmetically derivable from other pieces of data from the same view are removed from the normalized relations. The resulting relations must be minimum, that is, not redundant.

2. Integration of relations with common primary keys. Normalized relations that have the same primary key are integrated into one relation. This does not apply, however, to relations that have the same primary key because of generalization hierarchy relationship.

3. Elimination of any remaining derived data. If an attribute in one relation can be arithmetically derived from attributes in other relations, it is removed.

4. Elimination of any relation that can be derived from other relation. At times, a complete relation can be derived from other relations. At other times, an attribute in one relation can be functionally derived using other relations. In either case, a derived dependency is present and needs to be eliminated. The more complex the derivation, the more likely that a derived dependency would go undetected.

Although step 4 is not included in the proposed method, derived dependency is an important concept and needs to be considered even in step 1, so that the normalized relations are minimum. Step 2 is relatively straightforward since it involves one simple rule—that is, integrating normalized relations with the same primary key (unless there is a generalization hierarchy)—and is not, therefore, of much significance. The issues of synonyms and homonyms need to be considered, but conceptually this step is simple. Step 3 is less straightforward but not difficult. Derived data are easily recognized since they are usually a sum, count, or average. In other words, the designer has some heuristic to guide the determination of derived data. Further, there is lack of consensus in the database literature on whether derived data should be retained or removed from a logical database.

Steps 1 and 4 are conceptually the more difficult steps although step 4 is much simpler if step 1 is addressed properly. This paper focuses on step 1—that is, normalization when a user view involves many layers of nesting of set data. Textbooks and other training literature generally provide simple examples to illustrate the various normal forms. Nesting causes problems since it is more difficult to infer dependencies that invariably become more complex.

Note that the use of approaches such as the ER or the NIAM do not necessarily lead to minimum solutions. For example, consider the simple problem: "A salesperson sells to a customer and the order is recorded. An order involves one salesperson and one customer." The relational solution is:

## ORDER(ORDER#, CUST#, SP-NAME)

However, if one is using a method like ER or NIAM, one may consider the binary fact, “A salesperson sells to a customer” and consequently record a relationship between salesperson and customer. When we translate this relationship, we get:

## SELLS(CUST#, SP-NAME)

which represents a derived dependency.

The problem becomes more severe as the number of entities is increased. Suppose instead of three entities, we have five entities (say, an invoice records the sale of a new vehicle and the trade of an old vehicle; the sale is made from the salesperson to a customer). Each entity is related to every remaining entity. Thus, the problem is combinatorial and we have 10 binary relationships and 10 ternary relationships. This does not mean that we will model all these relationships since most relationships will be derived. However, it is not easy to figure out which relationships are derived. Add two more entities and the problem explodes: We have 21 binary, 35 ternary, and many higher-degree relationships. The problem is especially exacerbated if connectivity is considered.

Relational theory does provide answers to such problems, although the solutions are NP-complete. If we can write all the dependencies and run an algorithm to obtain a minimal cover, the correct solution can be obtained. Automated tools exist for deriving minimal covers, and many dependencies are easy to specify. Unfortunately, in practice, designers do not appear to employ this approach, as evident by the lack of any empirical study to suggest otherwise. This is probably due to the painstaking step of considering and specifying all the dependencies.

Therefore, we must have a method that eases normalization and eliminates derived relation. This, of course, will require the notion of abstraction. For example, in a “nest” as defined in this paper, one is likely to find attributes pertaining to the same object. By breaking the problem into parts and working with the primary key of the resulting object, the problem can be considerably simplified.

Consider the notion of nested view first:

## PRODUCT-LINE, PRODLINE-GOAL, {PROD#, PRODUCT-NAME}

The notation “{}” refers to nested or set data. In this case, it denotes that a PRODUCT-LINE has one PRODLINE-GOAL but many PROD# and PRODUCT-NAME. The presence of set data indicates violation of first normal form and suggests a need to normalize it. Given that a PROD# belongs to a product line, the view normalizes to:

## PRODUCT(PROD#, PRODUCT-NAME, PRODUCT-LINE)

## PRODUCT-LINES(PRODUCT-LINE, PRODLINE-GOAL)

Note that the cross-reference key PRODUCT-LINE in the relation PRODUCT denotes a one-many relationship between the two relations. If the nesting is deeper, it may lead to considerable difficulty in normalizing the view. For example, consider the following view:

## CUST#,NAME,{TRIPID,AGENT,{FLIGHT#,ORIGIN,DESTN,AIRLINE,{DATE,SEAT}}

The view represents a report that displays the trips taken by each customer and the flights involved in each trip. Assume that information about dependencies is provided separately. It is given that SEAT can be uniquely determined given FLIGHT#, DATE, and TRIPID.

After normalization, the following relations are obtained:

FLIGHT(FLIGHT#,AIRLINE,ORIGIN,DESTN)

SEATING(FLIGHT#, DATE, TRIPID, SEAT)

TRIP(TRIPID,AGENT,CUST#)

CUSTOMER(CUST#,NAME)

Note that CUST# in the outermost nest is determined by TRIPID. However, TRIPID in the second nest is not determined by any attribute from an inner nest; it concatenates with two attributes from inner nests. The attribute SEAT depends jointly on attributes from second, third, and fourth nests, and the attribute DATE does not depend on any other attribute. Evidently, nesting adds complexity in the design since it introduces difficult dependencies.

## Decomposition of User Views

NORMALIZATION CONCEPTS ARE FAIRLY SIMPLE AND CAN BE readily applied to simple views. Many user views, especially ones involving nested data, can get quite complicated, and a mere knowledge of normalization concepts may not help a novice designer. Thus, the use of concepts must be incorporated in a systematic approach. The main steps of the proposed approach are listed here, followed by various examples that illustrate the aspects. A formal treatment follows the examples.

Before the method can be proposed, the concepts of user view, nest, and nest key need to be explained. A user view is a collection of attributes in a form or a report and represents an independent fact or collection of facts. Normally, a form or a report corresponds to one user view. It is possible that two independent facts may be shown in one form or report. For example, if data regarding BOOK, COURSE, and IN-STRUCTOR are shown in a form and the assignment of a book to a course depends on the instructor, there is one user view; otherwise, there are two independent facts and, therefore, two user views. If this is not addressed at the beginning, the relations eventually will not be in fourth normal form.

A user view can be written using a nested representation such that the inner nests are multivalued with respect to outer nests and each nest has a nest key. A nest key functionally determines the remaining attributes in the nest either by itself or by concatenating with a nest key in an outer nest. The boundaries of a nest can be shown by the symbols “{” and “}.” Consider the previous user view that shows the associations between customers and their trips expressed as:

$$
\begin{array}{l} \text {CUST\#,NAME, \{TRIPID,AGENT, \{FLIGHT\#,ORIGIN,DESTN,} \\ \{\text {DATE,SEAT} \} \} \} \end{array}
$$

In the first nest, CUST# determines NAME, so CUST# is the nest key. In the second nest, TRIPID determines AGENT, so TRIPID is the nest key. Similarly, in the third nest FLIGHT# is the nest key. In the fourth nest, DATE alone does not determine SEAT, but when concatenated with two other nest keys, FLIGHT# and TRIPID, does determine SEAT, so DATE is the nest key of the fourth nest. The determination of nest keys is an important step in this approach.

## Method for Normalizing User Views

It is assumed that the designer can normalize simple views. The method requires that each nest be normalized individually. The resulting solution is related to solutions from other nests. The steps are:

1. Represent the view using the nested representation.

2. Start from the outermost nest. Determine the nest key and normalize it in the customary fashion. This should involve resolving transitive dependencies if present in the nest. After normalization, only the nest key is retained. Other attributes are considered resolved and ignored from the nest.

3. Move to the second nest. Normalize the nest. Check if the second nest key can functionally determine the first nest key. If yes, place the first nest key as a cross-reference key in the relation for second nest key and remove the first nest key from the nested representation. If no, check if any attributes other than the nest key are remaining in the second nest. If yes, show these attributes as dependent on the two nest keys concatenated together; in this case, however, retain both nest keys.

4. Keep moving to inner nests. Normalize each nest (i.e., remove any transitive dependencies) and check if the nest key in the current nest can be used to functionally determine a remaining nest key in an outer nest.

4a. If the nest key in the current nest by itself determines a nest from the outer nest, the latter is treated as a cross-reference key in a relation that has nest key from the current nest as its primary key. Similarly, if the nest key in the current nest jointly with some outer nest keys determines another outer nest key, the determined nest key is treated as a cross-reference key in a relation that has the determining nest keys as the primary key.

4b. If no, check if there are any remaining attributes other than the nest key in the current nest. If yes, concatenate the current nest key with one or more nest keys in outer nests to determine these attributes. Retain the current nest key in the nested representation.

5. When the innermost nest has been addressed, concatenate the remaining nest keys to form the primary key of a relation.

Note that in step 4a, one needs to check if a nest key can be determined by other nest keys. This can be achieved by the following procedure: If there are m remaining nest keys, consider the $m^{th}$ (that is, current) nest key and ask if it determines a nest key in an outer nest (that is, a nest key in the $p^{th}$ nest such that p < m). Next, consider the $m^{th}$ key along with any one of the outer nest keys and check if it determines any other outer nest key. In the next round, consider the $m^{th}$ key with two outer nest keys and check if it determines any other nest key. Continue this process until all checks have been made. Later in this section, this procedure is presented using pseudocode. The number of checks as a function of number of nests is nonpolynomial, but since most real applications have fewer than four nests, this is not a problem. If there are four nests, then in the worst case, twelve checks need to be made at the fourth nest; four checks need to be made at the third nest; and one check needs to be made at the second nest. Although the number of checks is somewhat high, such functional dependencies would need to be determined for any method addressing conceptual or logical database design.

## Examples for the Method for Normalizing

The above method is illustrated using examples. The simple views are presented first.

## 1. COURSE#, COURSE-NAME, INST#, INST-NAME, INST-LOCATION

Assuming that a course can be taught by only one instructor, the two relations that result after resolving transitive dependencies are:

COURSE(COURSE#, COURSE-NAME, INST#)

INSTRUCTOR(INST#, INST-NAME, INST-LOCATION)

## 2. INST#, INST-NAME, INST-LOCATION, {COURSE#, COURSE-NAME}

This holds the same information as the previous view, but the report has a different structure. In this case, we first consider the outer nest and determine the first relation:

$$
\text { INSTRUCTOR } (I N S T \#, I N S T - N A M E, I N S T - L O C A T I O N)
$$

Only INST# from the outer nest is retained.

$$
\text { INST\#,   \{COURSE\#,   COURSE - NAME\}}
$$

The primary key for the inner nest is COURSE#, and it also determines INST#. Thus, the second relation is:

$$
\text { COURSE } (C O U R S E \#, \text { COURSE - NAME }, I N S T \#)
$$

3. STU#, STU-NAME, {COURSE#, COURSE-NAME, GRADE}

From the outer nest, the following relation is obtained:

STUDENT(STU#, STU-NAME)

The primary key, STU#, is kept live from the outer nest. In the inner nest, if COURSE# is chosen as the primary key, COURSE-NAME can be determined. Thus, we note the relation COURSE as

# COURSE(COURSE#, COURSE-NAME)

which leaves us with

## STU#, {COURSE#, GRADE}

Since COURSE# does not determine STU#, the two must concatenate. Further, GRADE can be determined by the concatenated key. The third relation, therefore, is:

## ENROLL(STU#, COURSE#, GRADE)

## 4. PATIENT#, {DOCTOR, {MEDICATION-NAME, {INSTRUCTIONS}}

In this case, we have four nests. PATIENT# is the only attribute in the outer nest and therefore no action is required. DOCTOR is the only attribute in the second nest and does not determine PATIENT#. Thus, PATIENT# needs to be retained. In the third nest, MEDICATION-NAME exists by itself and does not determine either DOCTOR or PATIENT#. Further, assume that it does not concatenate with DOCTOR to determine PATIENT# (that is, the same medication can be prescribed by a doctor to many patients) or concatenate with PATIENT# to determine DOCTOR (that is, a patient may be prescribed the same medication by more than one doctor).

The situation becomes somewhat more complex at the fourth nest. First, one needs to consider if INSTRUCTIONS by itself determines PATIENT#, DOCTOR, or MEDICATION-NAME. This is not the case. Next, INSTRUCTIONS together with any one of the three attributes do not determine any of the remaining two attributes. Finally, INSTRUCTIONS taken together with any two of the three attributes do not determine the remaining attribute. Let us systematically examine the last check, that is, if a cross-reference key will result if INSTRUCTIONS together with any two attributes determine the remaining attribute. Does the same instruction apply to different medications prescribed by a doctor to a patient? Since this is true, MEDICATION-NAME is not a cross-reference key—that is, it will concatenate with INSTRUCTIONS. Similarly, DOCTOR is part of the primary key since a patient may be specified the same instruction for a medication by many doctors. Finally, PATIENT# is part of the key since a doctor may specify an instruction for a medication to many patients.

Thus, the following relation is obtained:

## PRESCRIPTION(PATIENT#, DOCTOR, MEDICATION-NAME, INSTRUCTIONS)

Of course, these assumptions may not always hold. The above representation assumes that there may be more than one instruction for a given medication prescribed by a doctor to a patient. If all instructions pertaining to a given medication specified by a doctor to a patient can be clubbed together in the attribute INSTRUCTIONS, then it should not be part of the primary key since it is not many with respect to one instance of each of the other attributes.

PRESCRIPTIONS(PATIENT#, DOCTOR, MEDICATION-NAME, INSTRUCTIONS)

The above relation corresponds to the following user view, which is different from the previous view:

$$
\text { PATIENT\#,   \{DOCTOR,   \{MEDICATION - NAME,   INSTRUCTIONS\}}
$$

Further, if there is a constraint that a particular medication be prescribed by no more than one doctor, the representation should be changed to:

$$
\begin{array}{l} \text { PRESCRIPTION(PATIENT\#,   MEDICATION - NAME,   DOCTOR, } \\ \text { INSTRUCTIONS) } \end{array}
$$

However, the user view does not change. Note that the nest key in the middle nest is on the one side.

5a. COURSE#, {INST#}, {TEXT}

First, the representation should be distinguished from:

$$
5 b. \text {   COURSE,   } \{\text { INST\# }, \{\text { TEXT } \} \}
$$

The latter has three levels: outer, middle, and inner; normalization will result in a single relation (COURSE, INST#, TEXT). However, the representation 5a harbors two views: The assignment of INST# to COURSE# is independent of the assignment of TEXT to COURSE# (that is, all instructors should use the same textbooks prescribed for a given course). This form decomposes into two separate views and then two separate relations: (COURSE#, INST#) and (COURSE#, TEXT). This example illustrates how the fourth normal form is handled in this method. A simple rule is: If two associations are independent, then capture them in separate views. Thus, the representation 5a is revised as COURSE{INST#} and COURSE{TEXT}.

6. Let us now use the rules and apply them on a fairly large user view shown in figure 1. We assume that CHG depends on ITEM#, and an ITEM# associates with only one COST#. Step 1 requires representing the view as an unnormalized relation. From the figure, the following representation is obvious:

PAT#, PAT-NM, PAT-ADD, PATCSZ, BILL-DT, DT-ADM, DISCH-DT, {COST#, COST-NM, {DT-CHG, ITEM#, DESC, CHG}, SUB-BAL-DUE,} BAL-DUE

On a closer look, one may see that ITEM#, DESC, and CHG are nested with respect to DT-CHG since the three attributes are multivalued with respect to PAT#, COST#, and DT-CHG. Thus, the representation of the nested view should be revised to:

PAT#, PAT-NM, PAT-ADD, PATCSZ, BILL-DT, DT-ADM, DISCH-DT, {COST#, COST-NM, {DT-CHG, {ITEM#, DESC, CHG}}, SUB-BAL-

## PATIENT BILL

PATIENT NO: 12345 DATE: 07-20-8X
PATIENT NAME: MARY BAKER DATE ADMITTED: 07-14-8X
PATIENT ADDRESS: 300 OAK ST. DISCH-DATE: 07-17-8X
CITY-STATE-ZIP: MOUNTAIN VIEW, CO 80638

<table><tr><td>COST-CENTER</td><td>NAME</td><td>DATE-CHARGED</td><td>ITEM-CODE</td><td>DESCRIPTION</td><td>CHARGE</td><td>BALANCE-DUE</td></tr><tr><td rowspan="5">100</td><td rowspan="5">ROOM &amp; BOARD</td><td>07-14-8X</td><td>2000</td><td>SEMI-PRVT ROOM</td><td>200.00</td><td></td></tr><tr><td>07-14-8X</td><td>2005</td><td>TELEVISION</td><td>5.00</td><td></td></tr><tr><td>07-15-8X</td><td>2000</td><td>SEMI-PRVT ROOM</td><td>200.00</td><td></td></tr><tr><td>07-16-8X</td><td>2000</td><td>SEMI-PRVT ROOM</td><td>200.00</td><td></td></tr><tr><td></td><td></td><td>SUBTOTAL</td><td></td><td>605.00</td></tr><tr><td rowspan="3">110</td><td rowspan="3">LABORATORY</td><td>07-14-8X</td><td>1580</td><td>GLUCOSE</td><td>25.00</td><td></td></tr><tr><td>07-15-8X</td><td>1585</td><td>CULTURE</td><td>20.00</td><td></td></tr><tr><td></td><td></td><td>SUBTOTAL</td><td></td><td>45.00</td></tr><tr><td rowspan="3">125</td><td rowspan="3">RADIOLOGY</td><td>07-15-8X</td><td>3010</td><td>X-RAY CHEST</td><td>30.00</td><td></td></tr><tr><td></td><td></td><td>SUBTOTAL</td><td></td><td>30.00</td></tr><tr><td></td><td></td><td>BALANCE DUE</td><td></td><td>$680.00</td></tr></table>

Figure 1.

Adapted from [13]

$$
\text { DUE } \}, \text { BAL - DUE }
$$

Step 2 requires treating the outer nest as a relation. The outer nest has the primary key PAT#, assuming that it uniquely determines BILL-DT, DT-ADM, and DT-DISCH. The first relation is:

$$
(P A T \#, P A T - N M, P A T - A D D, P A T C S Z, B I L L - D T, D T - A D M, D I S C H - D T)
$$

The attribute BAL-DUE is an arithmetically derived attribute and can be ignored. Only PAT# from the outer nest is retained, which leaves

$$
\begin{array}{l} \text { PAT\#,\{COST\#,COST - NM, \{DT - CHG,\{ITEM\#,DESC,CHG\}\},SUB- } \\ \text { BAL - DUE\}} \end{array}
$$

Step 3 suggests that we move to the next nest, which can be written as

$$
(C O S T \#, C O S T - N M)
$$

SUB-BAL-DUE is another derived attribute and can be ignored. COST# does not determine PAT#, so both PAT# and COST# are retained, and the simplified user view is:

$$
\text { PAT\#,   } \{\text { COST\#,   } \{\text { DT - CHG,   } \{\text { ITEM\#,DESC,CHG } \} \} \}
$$

In the next nest, there is the single attribute DT-CHG, which does not determine either PAT# or COST#. Further, it neither concatenates with COST# to determine PAT# nor concatenates with PAT# to determine COST#. Thus, DT-CHG is also retained and the next nest is considered.

At this stage, one notes that DESC and CHG depend on ITEM#. Further, COST# in an outer nest also depends on ITEM#. PAT# and DT-CHG do not depend on ITEM#. The resulting relation is

(ITEM#, DESC, CHG, COST#)

and the remaining user view is

PAT#, {DT-CHG, {ITEM#}}

Further, ITEM# together with DT-CHG does not determine PAT#; also, ITEM# together with PAT# does not determine DT-CHG. Thus, we conclude that the remaining portion of the view leads to the following relation:

(PAT#, DT-CHG, ITEM#)

Thus, the user view decomposes into four relations:

(PAT#, PAT-NM, PAT-ADD, PATCSZ, BILL-DT, DT-ADM, DISCH-DT)

(COST#,COST-NM)

(ITEM#, DESC, CHG, COST#)

(PAT#, DT-CHG, ITEM#)

While discussing example 5a, I said that independent associations should not be included in the same view. This is further illustrated by the following example. Consider the following user view, which captures information about what donor has donated to which department and who are the instructors in that department:

DONOR#, DONOR-NM, {DEPT-NM, DEPT-PHONE, {INST-NM, INST-PHONE}}

From the outer nest, we obtain

(DONOR#, DONOR-NM)

and the view reduces to

DONOR#, {DEPT-NM, DEPT-PHONE, {INST-NM, INST-PHONE}} In the next nest, another relation can be obtained.

$$
(D E P T - N M, D E P T - P H O N E)
$$

Since DEPT-NM cannot determine DONOR#, the view reduces to

DONOR#, {DEPT-NM, {INST-NM, INST-PHONE}}

Finally, a third relation is obtained from the innermost nest. Further, DEPT-NM can be determined by INST-NM.

## (INST-NM, INST-PHONE, DEPT-NM)

However, if DEPT-NM is removed at this step, one is left with the relationship between DONOR# and INST-NM. Suppose the application specifies that no direct association exists between donor and instructor, since donors contribute to departments. Thus, the relationship between department and instructor is independent from the relationship between department and donor. Thus, one should have split the representation into the following user views:

DONOR#, DONOR-NM, {DEPT-NM, DEPT-PHONE}

## DEPT-NM, DEPT-PHONE, {INST-NM, INST-PHONE}

The method can now be applied correctly and the following solution results.

(DONOR#, DONOR-NM)

(DEPT-NM, DEPT-PHONE)

(INST-NM, INST-PHONE, DEPT-NM)

(DONOR#, DEPT-NM)

The proposed method has been illustrated using single attribute primary keys. Note that there are no substantive changes to be made if a composite key is involved. In the last example, if INST-NM was captured as INST-LAST-NM and INST-FIRST-NM, then one can make the replacement throughout the modeling process without any other changes. The instructor relation would be represented as (INST-LAST-NM, INST-FIRST-NM, INST-PHONE, DEPT-NM).

## Theoretical Basis of Method

THE STARTING POINT OF THE METHOD IS A USER VIEW and supporting facts that can be used to infer dependencies among the elements in the view. First, it is assumed that the user view does not harbor independent associations. If a form harbors independent associations, separate views can be defined as in the examples discussed in previous sections.

A user view can be expressed as

$$
V _ {1} \left\{V _ {2} \left\{V _ {3} \dots \left\{V _ {q} \right\} \right\} \right\}
$$

where $V_{1}, V_{2}, V_{3}, \ldots, V_{q}$ are sets of attributes in different nests. A nest has a minimum of one attribute. Each nest has an attribute or group of attributes called its nest key. If $K_{i}$ is the nest key of $V_{i}$ , then if $a_{ij} \in V_{i}$ , then either $K_{i} \to a_{ij}$ , or $L_{i} \to a_{ij}$ where $K_{i} \in L_{i}$ , where $L_{i}$ is left-reduced and contains at least one $K_{g}, g < i$ . In example 3, COURSE# is the nest key of the second nest since COURSE# -> COURSE-NAME and STU#, COURSE# -> GRADE. Business forms generally have nested structure and it is easy to present them in the above format. In example 3, the following nested representations would be incorrect:

STU#, {STU-NAME, COURSE#, COURSE-NAME, GRADE}

STU#, {STU-NAME, {COURSE#, COURSE-NAME, GRADE}}

It is easy to observe that the natural structures of forms prevents such representations. To understand the theoretical basis for ensuring that the resulting relations are normalized and minimum, one needs to be familiar with inference axioms (see [12, p. 47]).

F1. Reflexivity: X -> X

F2. Augmentation: X -> Y implies XZ -> Y

F3. Additivity: X -> Y and X -> Z imply X -> YZ

F4. Projectivity: X -> YZ implies X -> Y

F5. Transitivity: X -> Y and Y -> Z imply X -> Z

F6. Pseudotransitivity: X -> Y and YZ -> W imply XZ -> W

The method achieves the fourth normal form. It does not always attain Boyce-Codd normal form (BCNF), which requires that each determinant be a candidate key. Applications can be normalized to BCNF, but this may require dropping dependencies. It is well known (see [12]) that it is possible to have a set of functional dependencies and not have a complete Boyce-Codd normal scheme. This is a general problem for any database. For example, if we have nest keys X and Y such that X {Y, Z} and XY → Z, where Z is an attribute. Now, if Z → Y, then the relation (X,Y,Z) will be in fourth normal form but not in BCNF. On the other hand, if Z is considered the nest key of the second nest, it will result in relations (Z, Y) and (X,Z). Now the solution is in BCNF but the dependency XY → Z is lost. Note that the approach allows both routes. However, it is likely that the designer will choose the first approach (i.e., Y as the nest key) since examples of BCNF violation indicate that dependencies like Z → Y in such contexts are semantically trivial. Also, such combinations of dependencies are rare.

Proposition: The relations obtained by using the proposed method are in fourth normal form and do not include derived dependencies.

Proof: The proof uses induction. Dependency information is used to simplify the user view one nest at a time, resulting in relations that are in fourth normal form. At each step, it is ensured that the newly created relation does not harbor a derived dependency, so the solution is minimal. Also, dependencies are preserved except where a designer chooses nest keys so as to attain BCNF.

1. Consider the first nest. The nest may hold one relation; if there is a transitive dependency, then there must be $K_{1} \rightarrow T$ such that $T! \rightarrow K_{1}, T \rightarrow U$ (where ! stands for not), one can create the relations $(K_{1}, \ldots, T)$ and $(T, U, \ldots)$ without loss of any dependencies. (If $T \rightarrow K_{1}$ , then either one is a candidate nest key). If there are transitive dependencies from T, they can be similarly addressed.

2. When the first nest is thus modeled, the nest key $K_{1}$ is retained, thus the structure simplifies to: $K_{1} \{ V_{2} \{ V_{3} \dots \{ V_{n} \} \} \}$ . If any other attribute $T$ is retained instead of $K_{1}$ such that $T! \to K_{1}$ , we can show that there is loss of dependencies. There are two possibilities: either $K_{2} \to K_{1}$ , or $K_{2}! \to K_{1}$ . In the first case, if $T$ is retained, then $K_{2} \to K_{1}$ .

$K_{1}$ is lost since $T! \rightarrow K_{1}$ . Thus, $K_{1}$ should be retained; by transitivity $K_{2} \rightarrow T$ and no dependency is lost. In the second case ( $K_{2}! \rightarrow K_{1}$ ), once again retaining $K_{1}$ does not lead to dependency loss; if $K_{1}K_{2} \rightarrow TK_{2}$ (easily shown by using Armstrong's axioms reflexivity, augmentation, and additivity). However, if $T$ is retained, $TK_{2}! \rightarrow K_{1}K_{2}$ , thus leading to loss of dependencies of type $K_{1}K_{2} \rightarrow a_{2j}$ . Thus, only $K_{1}$ need be retained from the first nest.

3. In the second nest, all transitive dependencies are first removed as in (1). Next, one asks if $K_{1}$ is dependent on $K_{2}$ . If yes, one includes $K_{1}$ in the relation for $K_{2}$ , that is, $(K_{2}, \ldots K_{1})$ . If this is the case, the second nest must be empty except for $K_{2}$ (otherwise $K_{2}K_{1} \to a_{2j}$ ; since $K_{2} \to K_{1}$ , one can left reduce it to $K_{2} \to a_{2j}$ so that is does not violate the second normal form). Consequently, at this point, one can remove $K_{1}$ from the nested representation leaving $K_{2}, \{V_{3}, \ldots, \{V_{q}\}\}$ . Note that since $K_{2} \to K_{1}$ , if $K_{3}$ (or $K_{i}$ ) $\to K_{2}$ , then by transitivity $K_{3}$ (or $K_{i}$ ) $\to K_{1}$ where $i$ pertains to the fourth or deeper nest. If $K_{1}$ is dependent on $K_{2}$ and if $K_{3}! \to K_{2}$ , then, as shown earlier, $K_{3}K_{2} \to K_{3}K_{1}$ ; thus, there is no loss of dependency. Again, it can be shown that $K_{3}K_{1}! \to K_{3}K_{2}$ ; thus, $K_{1}$ need not be retained.

If, however, $K_{2}! \to K_{1}$ , then $K_{1}$ must be retained in the nest. By definition of nest key, if any $a_{2j}$ does not depend on $K_{2}$ , then it will depend on $K_{1}K_{2}$ and a new relation with $K_{1}K_{2}$ must be created. Also, it is quite possible that $K_{r}K_{1} \to K_{2}$ , where $r > 2$ . One cannot show such a dependency if $K_{1}$ is removed. The nest $V_{2}$ must now have only $K_{2}$ , and the representation simplifies to $K_{1}\{K_{2}\{V_{3}\ldots\{V_{q}\}\}\}$ .

4. In nest $V_{3}$ , we can similarly reduce to $K_{3}$ . If $K_{3} \to K_{2}$ , then $K_{2}$ can be removed from the list without loss of dependencies. Similarly, if $K_{3} \to K_{1}$ (assuming $K_{1}$ has not been removed in a previous step), then $K_{1}$ can be removed. If neither $K_{1}$ nor $K_{2}$ can be determined by $K_{3}$ , then one needs to check if $K_{3}K_{1}\to K_{2}$ or $K_{3}K_{2}\to K_{1}$ . Suppose $K_{3}K_{1}\to K_{2}$ is true, one can then drop $K_{2}$ from the list. Once again, no dependency is lost; if there is a $K_{r}$ such that $K_{r}\to K_{3}$ , then by pseudotransitivity $K_{r}$ $K_{1}\to K_{2}$ . If $K_{r}!\to K_{3}$ and $K_{r}!\to K_{1}$ , then by augmentation, $K_{r}K_{3}K_{1}\to K_{2}$ indicating that dependencies are preserved despite removing $K_{2}$ .

5. Let us say $(m-1)$ nests have been resolved. In the worst case, the simplified representation will appear as $K_{1}\{K_{2}\ldots\{K_{m-1}\{V_{m}\ldots\{V_{q}\}\}\}\}$ ; in the general case some nest keys $K_{i}$ such that i<m would have been removed. By specifying the nest key $K_{m}$ , this representation can be simplified to $K_{1}\{K_{2}\ldots\{K_{m}\ldots\{V_{q}\}\}\}$ . Consider the current nest key $(K_{m})$ and check if the outer nest keys (i from 1 to m-1) can be determined:

$$
\begin{array}{l} \text {do while i <   m} \\ \quad \text {if K_{m} \to K_{i}} \\ \quad \text {cross - reference key found} \\ \quad \text {return} \\ \quad \text {endif} \\ \quad i = i + 1 \end{array}
$$

enddo

remove cross-reference keys from the nested representation

Now if $K_{m} \to K_{i}$ where $i < m$ , the latter can be removed without loss of dependencies. To show this, consider $K_{p}$ such that $p > m$ . If $K_{p} \to K_{m}$ , then by transitivity $K_{p} \to K_{i}$ . If $K_{p}! \to K_{m}$ , then as shown earlier $K_{p}K_{m} \to K_{p}K_{i}$ .

If $K_{m}! \to K_{i}$ , we should consider if the current nest key concatenates with any outer nest key $(p_{j})$ to determine some other nest key. This can be determined by the following procedure:

$$
\begin{array}{l} j = 1 \\ \text {do while} j <   m \\ \quad i = 1 \\ \quad \text {do while} i <   m \\ \quad \text {if (i ◇ j) and K_{m} K_{j} \to K_{i}} \\ \quad \text {cross - reference key found} \\ \quad \text {return} \\ \quad \text {endif} \\ \quad i = i + 1 \\ \quad \text {enddo} \\ \quad j = j + 1 \\ \text {enddo} \\ \text {ve cross - reference keys from the nested representation} \end{array}
$$

If no cross-reference key is found, then the current nest key will be considered with two other nest keys to determine if another nest key can be determined. This process continues until there are no more checks to be performed or a cross-reference key is found. Suppose a cross-reference key $K_d$ is found such that $K_m K_a K_b \ldots K_g \to K_d$ . The cross-reference key $K_d$ can be removed without loss of dependencies. To show this, consider $K_p$ such that $p > m$ . If $K_p \to K_m$ , by pseudotransitivity $K_p K_a K_b \ldots K_g \to K_d$ . A similar result is obtained if $K_p$ determines another nest key say $K_a$ or if $K_p$ together with one or more nest keys (say $K_q$ determines another nest key (say $K_a$ ). If $K_p! \to K_m$ , and also does not determine any of the other nest keys ( $K_a, \ldots K_g$ ), it can be shown that $K_p K_m K_a K_b \ldots K_g \to K_p K_d$ , which shows that the latter is derived allowing $K_d$ to be removed.

Thus, the $m^{\text{th}}$ nest is simplified and the nested structure reduces to $K_{1} \{K_{2} \ldots \{K_{m} \cdot \{V_{m+1} \ldots \{V_{q}\}\}\}\}$ . By induction, all remaining nests can be addressed.

6. Proceeding in this fashion, one will be left with the nest keys:

$$
W _ {1} \left\{W _ {2} \left\{W _ {3} \dots \left\{W _ {n}, a _ {n 1}, a _ {n 2}, \dots a _ {n t} \right\} \right\} \right\}
$$

such that $W_{1}, W_{2}, W_{3} \ldots W_{n} \subseteq K_{1}, K_{2}, K_{3} \ldots K_{q}$ and none of the nest keys can be determined by a combination of others and $a_{n1}, a_{n2}, \ldots a_{nt}$ are not dependent on $W_{n}$ . The final relation is:

$$
W _ {1} W _ {2} W _ {3} \dots W _ {4}, a _ {n 1}, a _ {n 2}, \dots a _ {n t}
$$

The relations so obtained are normalized. This can be shown by evaluating them for the various normal forms:

1. First normal form: The nested structure shows "set" data that can cause violation of the first normal form. The nests are addressed one at a time. After each nest is addressed, a nest key in a previous nest may be resolved. The remaining nest keys are addressed in step 6. At the end, all resulting relations should be in first normal form.

2. Second normal form: All determinants are left reduced. After a specific nest is individually addressed for dependencies, its nest key is then concatenated with the ones outside it to determine any further dependencies. If any nest key can be determined by others, it is removed. This ensures that a minimum number of nest keys are retained in the representation, and the determinants are always left reduced.

3. Third normal form: Individual nests are checked for transitive dependencies. Only nest keys are retained after an individual nest is modeled. If a combination of nest keys determines another nest key, a new relation is created with the latter as a cross-reference key, and this nest key is removed from the nested representation.

4. Fourth normal form: If a form harbors independent user views, they are separated. This avoids multivalued dependencies and violations to the fourth normal form.

5. Boyce-Codd normal form (BCNF): For a relational representation to be in BCNF, all determinants must be candidate keys in an individual nest. Using this method, the resulting relations will almost always be in BCNF. However, if there are exceptional dependencies like those discussed before the proof, the resulting relations will not be in BCNF. An attempt to attain BCNF will lead to loss of dependencies. However, no method can resolve this problem. In general, the dependencies that cause BCNF violation are trivial and it is generally preferable to accept this violation rather than force BCNF and achieve an inelegant design.

## Complexity of the Algorithm

Given that $^m C_r$ stands for the number of possible combinations among $m$ items taken $r$ at a time and defined by the formula $m! / ((m - r)! * r!)$ , the upper bound of number of checks as a function of number of nests $n$ is combinatorial and can be expressed as:

$$
\sum_ {m = 2} ^ {n} \sum_ {r = 0} ^ {m - 2} \left(^ {m - 1} C _ {r} * (m - 1 - r)\right)
$$

This can be verified by considering four nests, namely, $\{1\{2\{3\{4\}\}\}\}$ .

Suppose, one is at the fourth nest, m = 4. There are three binary checks 4→3, 4→2, 4→1 or ${}^{3}C_{0}$ \* (4-1-0). There are six ternary checks 4,3→2, 4,3→1, 4,2→3, 4,2→1, 4,1→2, 4,1→3. The formula indicates ${}^{3}C_{1}$ \* (4-1-1). There are three quadary checks, 4,3,2→1, 4,3,1→2, 4,1,2→3, or ${}^{3}C_{2}$ \* (4-1-2). There are no more checks, which is also indicated by the term (m-1-r), which becomes 0. If there are four nests, then one will go through $m = 2$ to 4 since $m = 1$ involves no check.

Surely, the process is combinatorial in the worst case. However, real applications rarely have more than four nests. Thus, the combinatorial explosion is not a practical problem. For instance, for n = 4, the total number of checks in the worst case is $(1+4+12)$ , or 17. Practically, the number is much lower. Quadary (four-way) relationships are rare. This implies that, with four initial nests, at least one of the nest keys will drop out, leaving three nests and $(1+4)$ checks or two nests and $(1)$ check.

The relations obtained are normalized, no dependency is lost, and all decompositions are lossless. In most cases, the number of checks required is under control. Thus, the method is both rigorous and practical.

## Conclusion

THIS PAPER PRESENTS A SIMPLE YET RIGOROUS METHOD FOR ATTAINING a normalized and minimum solution when the input to the design process is a form or a report. It uses the natural nested structure of forms and reports to analyze the problem into simpler pieces called nests. The method can be used for training designers. It can also be part of a CASE or expert tool. In the area of database design, tools like DDEW [16], View Creation System [19], and IEF [10] have been developed. A detailed list of such products is provided in Reiner [16]. Most tools are based on the ER data model. The purpose of the tools has generally been to provide diagramming and data dictionary support. Some expert systems (see, e.g., [5, 8, 19]) have attempted to automate the database design process, although none has shown how the resulting solutions are minimum.

Reiner [16] recommends that automated database design tools should be oriented toward the underlying semantics of evolving design rather than the superficial layer of graphical presentation. They should help to evaluate and increase the consistency and correctness of design. This is, indeed, the purpose of the method proposed here.

Acknowledgment: The author wishes to thank the anonymous referees for their constructive comments.

## REFERENCES

1. Batini, C.; Ceri, S.; and Navathe, S.B. Conceptual Database Design: An Entity-Relationship Approach. Redwood City, CA: Benjamin/Cummings, 1992.

2. Batra, D.; Hoffer, J.A.; and Bostrom, R.P. Comparing representations with the relational and EER models. Communications of the ACM, 33, 2 (February 1990), 126–139.

3. Blaha, M.R.; Premerlani, W.J.; and Rumbaugh, J.E. Relational databases design using an object oriented methodology. Communications of the ACM, 31, 4 (April 1988), 414–427.

4. Chen, P.P. The entity-relationship model—toward a unified view of data. ACM Transactions on Database Systems, 1, 1 (March 1976), 9–36.

5. Choobineh, J.; Konsynski, B.R.; Mannino, M.V.; and Nunamaker, J.F., Jr. An expert system based on forms. IEEE Transactions on Software Engineering, 14, 2 (February 1988), 242–53.

6. Codd, E. A relational model for large shared data banks. Communications of the ACM, 13, 6 (June 1970), 377–387.

7. Date, C.J., and White, C. A Guide to DB2, 2d ed. Reading, MA: Addison-Wesley, 1988.

8. Dogac, A.; Yuruten, B.; and Spaccapietra, S. A generalized expert system for database design. IEEE Transactions on Software Engineering, 15, 4 (April 1989), 479–491.

9. Edelstein, H. Relational vs. object oriented. DBMS, 4, 12 (November 1991), 68–79.

10. Texas Instruments. IEF Technical Description. Plano, TX.

11. Kroenke, D.M. Database Processing, 4th ed. New York: MacMillan, 1992.

12. Maier, D. The Theory of Relational Databases. Rockville, MD: Computer Science Press, 1988.

13. McFadden, F.R.; Hoffer, J.A.; and Srinivasan, A. Casebook for Database Management. Menlo Park, CA: Benjamin/Cummings, 1990.

14. Nijssen, G.M., and Halpin, T.A. Conceptual Schema and Relational Database Design: A Fact Oriented Approach. Sydney: Prentice-Hall, 1989.

15. Peckham, J., and Maryanski, F. Semantic data models. ACM Computing Surveys, 20, 3 (September 1988), 153–189.

16. Reiner, D. Database design tools. In C. Batini, S. Ceri, and S.B. Navathe (eds.), Conceptual Database Design: An Entity-Relationship Approach. Redwood City, CA: Benjamin/Cummings, 1992, pp. 411–454.

17. Rivard, S., and Huff, S.L. Factors of success for end-user computing. Communications of the ACM, 31, 5 (May 1988), 552–561.

18. Stonebraker, M. Readings in Database Systems. San Mateo, CA: Morgan Kaufmann, 1994.

19. Storey, V.C., and Goldstein, R.C. A methodology for creating user views in database design. ACM Transactions on Database Systems, 13, 3 (September 1988), 305–338.

20. Teorey, T.; Yang, D.; and Fry, J.P. A logical design methodology for relational databases using the extended entity-relationship model. Computing Surveys, 18, 2 (June 1986), 197–222.
