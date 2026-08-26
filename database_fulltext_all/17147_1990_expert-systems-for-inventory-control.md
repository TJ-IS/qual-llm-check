---
otero_id: 17147
otero_key: "3ZNG237R"
title: "Expert systems for inventory control"
authors: "Dieter Ehrenberg"
year: "1990"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(90)90024-l"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Expert Systems for Inventory Control

Dieter EHRENBERG

Department of Enterprise Management, University of Technology, 7030 Leipzig, GDR

The success and impact of current DSS remain rather limited within organizations. These limitations can be offset by integrating artificial intelligence into DSS. This paper presents briefly the possibility of combining DSS with expert system technology for management of inventories. An exemplary part of knowledge base for material disposition is described and some implementations of prototypes are discussed.

Keywords: Decision Support Systems, Expert Systems, Inventory Control, Material Disposition, Management Systems.

## 1. Introduction

In the last years decision support systems (DSS) were applied in different fields. At the University of Technology in Leipzig we have many experiences in modeling and implementing of such systems especially for control and management of production, transport and inventory processes. For these cases we have developed partly new methods of modeling and implementation. In spite of some applications we must point out in general that successes in application of DSS are too small. We see the following reasons for this situation:

\- not enough user-friendliness of DSS, because the user needs to much knowledge of the computer system, of the application etc.,

\- restricted functionality and flexibility of DSS,

– missing of explanation and valuation for solutions in DSS.

These points mean that DSS are without intelligence or have a too small part of intelligence. Therefore we attempt another approach by combining the DSS with expert-system technology and by development of expert systems respectively.

This paper presents some first results for application of expert systems in inventory control.

![](/api/attachments/3ZNG237R/fulltext/images/5650b6c7d091e30a10358e792f5097054e14fbf132cc2aeb164fb8e5f6bf0b85.jpg)

Dieter Ehrenberg is Professor of Business Informatics at the Leipzig University of Technology. He received a B.S. in mathematics from the University of Leipzig, a Ph.D. in operations research and a D.Sc. in management information systems from the University of Technology of Leipzig. His teaching and research interests are management information systems, decision support systems and application of artificial intelligence in management.

## 2. Expert Systems for Management

We find many definitions for expert systems in literature on Artificial Intelligence. The basis for our work is the well-known conception of Appel-rath [1] and we use the following definition:

An expert system is a knowledge-based information system capable of

\- representing knowledge for a narrow domain,

– helping to acquire this knowledge,

\- reasoning consequences and/or new knowledge,

\- explaining these obtained results and their valuation.

General and special features of expert systems are described in numerous papers and books (e.g. [7], [9], [11], [13]).

Fig. 1 shows the structure with all important components of an expert system, including such possibilities as graphics, spreadsheets, textprocessing and connection with OR-procedures being very important for acceptance of expert systems in management. This fact was also verified by Mertens, Allgeyer and Baes [8]. They have shown that only 10 in 274 expert systems were applied in practice and only 20 percent of those investigated expert systems were developed for management (e.g. to financing, planning, accounting). This result is unexpected because many complex situations at all levels of management are appropriate to be solved by using expert systems with domain knowledge of experts. But mostly decision problems in management seem to be complex and ill-structured and besides it is in many cases not easy to acquire and to represent the essential knowledge about problems in different situations of management.

A main problem of developing any expert system is to choose an appropriate technique of knowledge representation (KR). It seems that the KR-technique used is dependent on the level of management. But no guide exists for selection of the best KR-technique for a particular application. Baldwin and Kasper discussed and compared the known kinds of KR-techniques (logic, semantic networks, production rules, frames, direct representation) and found out there is not a single KR-technique currently which is optimal on all levels of management [2]. Therefore the builders of an expert system have to investigate which of the KR-techniques is suitable for a special application. A lot of research, both theoretical and practical, in this field is necessary in order to give proposals on special classes of management problems.

In this paper knowledge representation is realized by production rules.

## 3. Expert System for Material Disposition

## 3.1. Necessity for Using Expert Systems in Management of Inventories

In our group we have many years of experience in DSS for control and management of inventories especially in DSS for management of central warehouses of building plants [3], [4], [5].

However we must notice that DSS do not support sufficiently managers and other people for special tasks in inventory control. Almost every inventory problem involves more or less uncertainty due to the many uncontrollable variables contained in the context. But it is very difficult or impossible to use heuristics or diffuse knowledge in current DSS. Decisions would be better prepared if more special knowledge of (many) experts could be included in the used software packages. Furthermore there are more and more regulations affecting inventory decisions and managers would get much support from an expert system with its knowledge base on these regulations and with heuristics to give useful recommendations for decisions.

![](/api/attachments/3ZNG237R/fulltext/images/f8d27d98a94118d85dc866afb6fe795043c8da12a73ed6149a94e037947c8adf.jpg)  
Fig. 1. Major Components of an Expert System.

Logistics require expert knowledge for

\- monitoring and control:

\- inventory management and control,

\- customer service management,

\- package specification,

\- vehicle routing,

\- load planning;

\- intelligent data interpretation in exceptional situations;

\- assistance in routine decisions:

\- requisition processing,

\- order processing,

\- disposition,

\- accounting,

\- status analysis;

\- fault diagnoses of machines and logistics processing malfunctions.

Therefore we have many situations that require expertise for making optimal decisions in this field.

For some time past we investigated the application of expert systems for defined tasks of management of inventories in central warehouses of building plants. We have a conception for design of expert systems into several parts of logistics.

These expert systems will be interconnected with one another and with other DSS on a common knowledge base and data base.

Use of expert systems in logistics will help to accomplish such goals as

\- uninterrupted material flow,

\- reduced operating costs,

\- improved productivity,

\- consistent decision making.

A special expert system of our system of expert systems is EXBEST. EXBEST is an expert system for material disposition described in the next paragraphs.

## 3.2. Knowledge Base for EXBEST

Tasks of material disposition are connected with problems relating to comparison of demand and stock, information of suppliers and carriers, checking of orders and arrangements and other activities.

Because these people need special knowledge and experiences including many heuristics.

Therefore the advantage of using expert systems in material disposition is on the one hand a support for the manager and on the other hand a help for managers not so specialized in such cases, when the disposition expert is absent (e.g., because of illness, vocation or other unavailability). A manager in the field of material disposition is an expert with very special knowledge about a limited number of material items. Such knowledge includes many information about demand, delivery and transportation conditions, many regulations a.s.o. Some of the information are not sufficiently determined as basis for definite algorithm. Thus these information and other parts of the knowledge of managers are a basis for heuristics exclusively. It is not possible to describe this problem with all its properties and consequences in this paper completely (see [6]).

Topics for the knowledge base of EXBEST are

\- demand for items (temporal structured),

\- stock for items (maximal, minimal, actual),

\- time of deliveries,

\- balance, limits.

\- order strategies,

\- restrictions (capacity of warehouse, credits),

– suppliers (lots, properties of deliveries),

\- transport,

\- analysis knowledge for past periods.

The knowledge base of EXBEST is represented in a set of facts and rules which are formulated PROLOG-oriented. We can give only some examples of such facts and rules since a detailed discussion of this knowledge base would go beyond the scope of this paper.

## Facts

Facts in EXBEST describe knowledge that is generally available to experts in the domain of material disposition. A fact consists of a fact name and attributes which can be represented by numerical, alphanumerical or logical values.

Following examples show this representation technique:

(F1) : (ITEM item-no item-name)

(F2) : (DEMAND item-no amount-d period)

(F3) : (STOCK: item-no amount-s period)

(F4) : (SAFETY-STOCK item-no amount-t)

(F5) : (SUPPLIER-ITEM name-s item-no lot delivery-date valuation)

(F6) : (SUPPLIER name-s address-s)

(F7) : (CUSTOMER customer-no address-c)

(F8) : (ORDER item-no amount-o period week-d name-s)

(F9) : (TRANSPORT name-t capacity period)
In this connection is

address-c : customer address
corresponding to customer-no

address-s : address of supplier corresponding to name-s

amount-d : amount of demand

amount-o : amount ordered for week-d

amount-s : amount of stock

amount-t : amount of safety-stock

capacity : potential capacity of carrier in considered period

customer-no : reference number of customer corresponding to address-c

delivery-date : agreed date for delivery

item-name : name of item corresponding to item-no

item-no : reference number of item corresponding to item-name

lot : lot of deliverable item

name-s : name of supplier corresponding to address-s

name-t : name of carrier

period : disposition period (e.g. week, month)

valuation : point-valuation for delivery of supplier on the basis of past experiences and observations concerning quality, punctuality a.s.o.

week-d : week in which item should be delivered

## Rules

Rules include in the knowledge base the expert's way to approach a problem in a special domain. Among these rules we may find empirical rules routinely used by experts, mathematical formulas, business heuristics etc.

A rule consists of the premise and the conclusion. Premises of rules are conjunctions of conditions and a condition is a disjunction of elementary expressions. Conclusions of rules are elementary expressions too. Usually a if-then-rule with expression if (A1 ∧ A2 ∧ ... ∧ An) then B is represented by B ← A1 ∧ A2 ∧ ... ∧ An or by (B) if (A1) (A2) ... (An).

In this connection is

$A_{i}$ : part of the premise (elementary expression or a disjunction of elementary expressions, i = 1 (1) n)

B : conclusion

Examples for elementary expressions in shortened form are following

(E1) : The stock of item x is less than demand d in period w:
(STOCK-LESS x d w)

(E2) : The order of item x is necessary with amount y in period w:
(ORDER-NECESSARY x y w)

(E3) : The order of item x with amount y will be realized by supplier n with lot q in period w with delivery-date t:
(ORDER-REAL x y q w n t)

(E4) : The delivery of item x is possible with amount y in period w by carrier c: (DELIVERY-POSSIBLE x y w c)

(E5) : There is a carrier c who can transport item x with amount y in period w:
(TRANSP-EXIST x y w c)

In the following we give examples for simplified rules of material disposition using above-mentioned facts and elementary expressions.

```lisp
(R1) : If stock < demand
    or
    stock < safety-stock
    then stock is less.
    ((STOCK-LESS x y w) if
    ((either (STOCK x u w) (DEMAND x v w)
    (LESS u v)
    (SUM u y v))
    (or (STOCK x h w) (SAFETY-STOCK x k)
    (LESS k h)
    (SUM k y h))))
```

(R2) : If stock is less then order is necessary.
((ORDER-NECESSARY x y w) if
(STOCK-LESS x y w)
(PP Ordering for x is necessary with
amount y for period w))
(R3) : If order is necessary
and
a supplier can supply
then order could realize.
((ORDER-REAL x y q w n t) if
(ORDER-NECESSARY x y w)
(SUPPLIER-ITEM n x q t v)
(LESS y q))
(R4) : If order could realize
and
transportation is possible
then delivery is possible.
((DELIVERY-POSSIBLE x q w n) if
(ORDER-REAL x y q w n t) (TRAN-
PORT c m w)
(LESS q m)
(PP Delivery for x is possible with amount
q from supplier n in period w by carrier c
and delivery-date is t))

Fig. 2 shows a partial rule tree of EXBEST illustrating the connection of the rules described above.

## 3.3. Implementation

At present we have several versions of EX-BEST.

We started with EXBEST1 which is a realization by using micro-PROLOG. EXBEST1 cannot be considered as an expert system because it is without such components as explanation, knowledge editor a.s.o. (see fig. 1).

But EXBEST1 demonstrates the new approach of modeling in the field of material disposition [4], [10]. After that we have developed some prototypes for EXBEST using different shells for expert systems.

EXBEST2 [12] represents an expert system for material disposition using shell APES (Augmented Prolog for Expert Systems, MS-DOS).

When the user starts EXBEST2 a heading is presented to inform the user of the question's context. Questions are asked concerning a particular case of material disposition using menu-techniques.

When EXBEST2 has gained enough information it gives recommendations which are displayed on the terminal. If the user does not understand questions or specific recommendations he can ask “why” or “how” and rules used together with the chain of inference will be displayed on the terminal.

![](/api/attachments/3ZNG237R/fulltext/images/2145e973568be45497cea0c3e031110d5c0bb500f29ef4364c79617f720327cb.jpg)  
Fig. 2. Partial Rule Tree of EXBEST.

The base for EXBEST3 is an other powerful and userfriendly shell with such integrated components as data management (DBASE III), graphics, spreadsheet analysis, general-purpose text processing, report generation and an open interface for coupling of other useful external software packages (e.g. optimization, statistics).

EXBEST3 is still in the developing stage. However we believe that EXBEST3 is a suitable prototype in order to develop an expert system for the use in practice. In the immediate future our focal point will be the expansion of the actual knowledge base including the integration of more disposition heuristics.

By using EXBEST3 endusers get an intelligent support for several activities in material disposition.

## 4. References

[1] Appelrath, H.-J., Von Datenbanken zu Expertensystemen. Springer-Verlag, Berlin, Heidelberg, New York, Tokyo, 1985.

[2] Baldwin, D., Kasper, G.M., Toward Representing Management-domain Knowledge. Decision Support Systems 2 (1986) 159–172.

[3] Ehrenberg, D., Ein Beitrag zur Modellierung grosser Sy-

steme und interaktiver entscheidungsunterstützender Systeme mit Anwendung in der bautechnologischen Versorgung. Dissertation B, Technische Hochschule Leipzig, 1985.

[4] Ehrenberg, D., Decision Support Systems for Management in Central Warehouses of Building Plants. Fourth International Symposium on Inventories, Proceedings, Budapest, 1986.

[5] Ehrenberg, D., Sebastian, H.-J., Rechnergestützte Leitung und Steuerung von Prozessen der bautechnologischen Versorgung eines Baukombinates. Teil 1: Modellierung. Wissenschaftliche Zeitschrift der Technischen Hochschule Leipzig 9 (1985) 1.

[6] Ehrenberg, D., Expert Systems for Inventory Control. Leipzig University of Technology, Working Note, 1988.

[7] Hayes-Roth, F., Waterman, D.A. Lenat, D.B., Building Expert Systems. Addison-Wesley, 1983.

[8] Mertens, P., Allgeyer, K.-H., Baes, H., Betriebliche Expertensysteme in deutschsprachigen Ländern, Versuch einer Bestandsaufnahme. Zeitschrift für Betriebswirtschaft, 1986, Nr. 9.

[9] Savory, S.E., Grundlagen von Expertensystemen. R. Oldenbourg Verlag München, Wien 1988.

[10] Sebastian, H.-J., Ehrenberg, D., Zur Nutzung Wissensbasierter Entscheidungsunterstützender Systeme (WES) in der Lagerhaltung. Wissenschaftliche Zeitschrift der Technischen Hochschule Leipzig 11 (1987) 4.

[11] Silverman, B.G., Expert Systems for Business. Addison-Wesley, 1987.

[12] Soederholm, E., Ett PROLOG-baserat expertsystem foer lagerhallning. Abo Akademi Turku, 1988 (unpublished).

[13] Waterman, D.A., A Guide to Expert Systems. Addison-Wesley, 1986.
