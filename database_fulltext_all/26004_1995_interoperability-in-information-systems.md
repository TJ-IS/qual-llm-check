---
otero_id: 26004
otero_key: "YZXBFSDG"
title: "Interoperability in information systems"
authors: "R. M. Colomb; M. E. Orlowska"
year: "1995"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.1995.tb00088.x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Interoperability in information systems

R. M. Colomb & M. E. Orlowska

Distributed Systems Technology Cooperative Research Centre, Department of Computer Science, The University of Queensland, Queensland 4072, Australia

Abstract. Two operationally autonomous information systems interoperate if system can make use of information contained in the other, or if they exchange transactions. A widely held assumption in this field is that the development interoperability among information systems should preserve the design autonomy of the individual information systems in a strong sense. This paper demonstrates that preservation of strong design autonomy is not always possible owing to necessity to resolve semantic hereogeneity among the systems. This neces violation of autonomy calls into question the utility of research on general a tectures and the possibility of general solutions. We suggest some themes certain special cases where we believe feasible and useful computer science research can be done in this area, and also suggest some implications for standard models of architectures for federated databases.

Key words: federated databases, interoperability.

## INTRODUCTION

Interoperability among heterogeneous information systems has become an important top of the computing literature (ACM 1990; SIGMOD, 1991; IEEE, 1991; Hsiao et al., 1993). We will make a distinction between interoperability and remote access to databases. Remote access occurs when a user can log on to any number of databases and perform queries and post updates on them one at a time. Two information systems interoperate if one system can use of information contained in the other, or if they exchange transactions. There are tenomies of interoperating information systems (e.g. Elmagarmid & Pu, 1990), which are generally distinguished from distributed information systems in that under interoperability information systems are distinct: either interoperation is a late enhancement to existing systems (legacy systems) or the systems are controlled by different organizations. In distributed systems the implementation may involve many communicating subsystems, but the division into systems is constrained solely by engineering issues.

A widely held assumption in this field is that the development of interoperability am information systems should preserve the autonomy of the individual information system (Elmagarmid & Pu, 1990; Ram, 1991). In the taxonomy of Sheth & Larsen (1990, p. 187), most comprehensive form of autonomy is design autonomy.

[which] refers to the ability of a component Database System to choose its own design respect to any matter, including the data being managed (i.e., the Universe of Discourse) representation (data model, query language) and the naming of the data elements, and conceptualization or semantic interpretation of the data...

(p

## Design autonomy is often interpreted in a very strong way, for example

Therefore, when a component joins the federation, it will keep its own local DBMS together with its original conceptual schema. Hammer & McLeod (1993, p. 56).

The retention of local autonomy is a prime consideration in the development of interopera in a heterogeneous environment, as modification of a software system is usually impos or highly inconvenient. Eimagarmid et al. (1993, p. 2).

This strong design autonomy is often called local autonomy, and will be so called in following.

Much of the recent research interoperability has to do with architectures, generally oriented, for achieving interoperability. A widely used architecture is the five-schema a tecture of Sheth & Larsen (1990). These schemas are:

\- local schema: the underlying schema of the component database system;

\- component schema: the translation of the local schema into the canonical data model of federated system;

\- export schema: the portion of the component schema which the component data chooses to make available to the federation;

\- federated schema: the integration of the several export schemas for the component of bases;

● external schema: a view of the federated schema defined for a particular user or applica

The strong notion of design autonomy is implicit in the common bottom-up strategy for integration of schemas where the universes of discourse overlap. For example, Sheth (1993) describe a semiautomated approach which first analyses the export schemas to obtain global attribute hierarchy, then identifies and merges classes, and finally restructures integrated schema.

Other commonly treated issues include translation among data models (e.g. Hamm McLeod, 1993) and transaction management issues. An issue frequently mentioned generally assumed solved is semantic heterogeneity (Elmagarmid & Pu, 1990). Sem heterogeneity has to do with the differing meaning of data items in different information systems. The argument of this paper, as detailed in the following section, is:

\- Resolution of semantic heterogeneity is not generally obtainable without violating autonomy of the interoperating information systems. This necessary violation of autor calls into question the utility of research on general architectures.

\- On the other hand, people build interoperating information systems of many kinds, random methods. One way that this is done is to provide remote access to several databases allowing the user to make queries and execute transactions, using perhaps the cut-and-p facility on their workstation. There seems to be little scope for computer science research random change to information systems.

\- We suggest some general themes where we believe feasible and useful computer science research can be done in this area, and also suggest some implications for the standard models of architectures for federated databases.

\- We conclude with a summary, including an operational definition of interoperability affects research issues.

## MAINTENANCE OF AUTONOMY NOT GENERALLY POSSIBLE

As we have noted in the Introduction, in the literature the problem of interoperability is state the development of a new application among existing data environments, each of which many existing applications. The new application is an arbitrary user, making an arbitrary selection among existing databases. Interoperability may take the form of inter-data transactions. The interoperability is mediated by a superstructure outside the local database for example the five-schema architecture. None of the local systems is required to change in way (local autonomy).

We argue that this approach fails in general owing to semantic heterogeneity among the I databases. There is a class of heterogeneity which can be resolved by possibly com derivation rules on the schemes and metaschemas (e.g. Hammer & McLeod 1993; Sheth et 1993). We might call heterogeneity which can be resolved by derivation rules structural erogeneity. We show below that there are cases in which the heterogeneity is not resolvable derivation rules.

Let us consider a simple example of two existing databases: Taxation Office with the sch (1) and Company with schema (2). In both schemas the key attributes are identified underlining.

$$
\text { Taxation   Office } (\text { Tax\_file\_# }, \text { Name }, \text { Date\_of\_Birth }, \text { Income })
$$

$$
\text { Company } (\text { Employee } \#, \text { Name }, \text { Address }, \text { Salary })
$$

Both schemas have as primary important attribute a unique identifier given by the organization. However, in both cases, the organization has the problem of identifying a person at the organization's boundary: how, for example, does the taxation office determine whether a person already a tax file number allocated? To maintain a semantic correspondence between information system and its environment, each database must maintain also a candidate among the attributes recorded about each entity. In the case of the taxation office, the candidate key is the compound Name, Date\_of\_Birth, while in the case of the company, the candidate key is the compound Name, Address.

The simplest kind of interoperability is taken to be a query involving more than one datab

Since databases (1) and (2) store information about the same people, we might wish to make query involving both databases. Any such query would require a join of the two tasks. Examination of the schemas (1) and (2) will, however, show that no meaningful join can be constructed. Neither schema includes the local identifier of the other, so neither Tax\_file nor Employee# are possible join attributes. Name is an attribute in common, but is a key neither. In both cases, one of the attributes of the compound candidate key of one data does not appear in the other.

It is impossible to achieve any kind of interoperability between (1) and (2) without change least one of the schemas, violating local autonomy. The counterexample of this series shows that an architecture for interoperability which assumes local autonomy is not generally workable.

One way to make these two systems interoperate is to provide an additional table v contains a mapping between Tax\_file\_# and Employee#. This table may be located either of the component databases, or perhaps in the federated schema. The essential table that the additional table must be maintained as records are added to and deleted from each the component databases. Its maintenance is the object of a new application, which must part of both of the component information systems. Further, in order to maintain this table have already seen that additional data must be gathered. The typical solution for the exa situation is for the company to require all of its employees to disclose their tax file number

Although each system retains design autonomy by the definition of Sheth & Larsen (1999) order to participate in the federation each system must accept the additional constraint that mapping table must be maintained. In other words, participation in the federation cannot without cost to at least one of the components, thereby violating local autonomy. Further order to participate, a component system must accept additional constraints on its evolution from outside its normal universe of discourse.

We see that the Sheth & Larsen (1990) notion of design autonomy does not imply the information system can expect to participate in a federation without change to its local schema nor does it imply that no change need be made to local applications. In the bottom-up integration of schema, one would in general find that the desired integration cannot proceed with changes to the local schemas. In general, a non-trivial global schema cannot be constructed from local schemas with overlapping universe of discourse, even in principle. (A trivial schema is simply the union of the local schemas, with suitable renaming so that all relation attributes are distinct.)

There are many examples of unresolvable semantic heterogeneity. Stamper ( $^{1}$ ) describes heterogeneity arising from subtle differences in the way organizations relate ationally to their universes of discourse. Walter & Bellman (1990) describe heterogeneity a from an accumulation of not-quite-resolvable structural heterogeneities.

## INTEROPERATION EXISTS

In practice, it is common for information systems to interoperate. Some examples are:

\- Most business systems function as an interoperating system of applications. Order e communicates with inventory, accounts receivable and general ledger. General le systems for operating units integrate with the corporate general ledger.

\- The Australian Taxation Office accepts tax returns prepared electronically by systems in agents' offices.

\- Many companies in the manufacturing industry use electronic data interchange (ED electronically send purchase orders, invoices, etc among their information systems.

\- All companies trading on a particular stock exchange must present periodic balance share and operating statements using the same accounts, which are used inter alia by secure analysts to compare company performance.

\- Several large projects are reported in, for example, Thomas et al. (1990) and Brodie (19

We have a difficulty. On the one hand, there are a large number of successfully interoperable information systems complexes, which have been constructed by humans using random means. On the other hand, the general problem of design and construction of interoperable information systems seems to be impossible. Is there a middle ground between the general solution and random individual solutions on which academic research can take place?

We have seen that the general problem founders on semantic heterogeneity, while specific solutions exist. The specific solutions must have resolved the semantic issues in their particular cases. These resolutions depend on the well-understood fact that the organizations using information systems interoperate as organizations. Since the semantics of an individual information system depends on its using organization's world view and behaviour, and since organizations communicate with each other, the semantic differences among the individual information systems must be capable of resolution. Their world views and behaviour control are related. The relationship may be limited to the set of mutually agreed transactions, and realization may require not only changes to their respective information systems, but a collection of additional data.

Resolution of semantic differences depends on negotiation among the organizations, respect to a specific class of proposed transactions. One would expect that an arbit collection of databases and users would not be able to reach such an agreement, so existing interorganizational interaction might be minimal and the costs of integration were exceeded the benefits. Once an agreement is reached, it is very likely that the information systems must be modified to achieve the new capability. There may be many ways of modifying the systems: in particular, there may be many different distributions of cost among the various organizations. The specific approach to solution is therefore subject to negotiation among organizations.

Resolution of semantic heterogeneity is seen therefore as essentially coming to an agreement about terminology at the domain level. It is not, as such, a computer science is Structural heterogeneity, of course, can be resolved by computer science means once terminology has been agreed upon. Bottom-up strategies must recognize the possibility blockages, and expect that the component schemas must be subject to the requirement change. This recognition would probably make the resolution of structural heterogeneity te nically less difficult, since one option would always be to change local schemas. This is not to say that the structural resolution is easy. There are many situations, e.g. incompatible aggregations, for which exact solutions are not possible. Going further, for example, Frankhauser & Neuhold (1993) investigate structural ambiguities using fuzzy set concepts. In addition, numerous low-level problems must be overcome to achieve interoperability in practice, which require solution below the database management system level. Examples of this kind of software are ANSAware (ANSAware, 1993) and DCE (OSF, 1992).

## WHAT ARE THE COMPUTER SCIENCE PROBLEMS?

From the computing point of view, we have seen that the construction of interoperatable information systems involves making coordinated changes to the participating systems, resulting in new applications which must coordinate in execution. This is a specialization of the general problem of construction and modification of information systems. In information systems generally, the computer science community provides assistance with concepts to formulate the problems and tools to assist in the process. These tools are available to the practitioner community as computer-aided software engineering (CASE) tools. There is scope for computer science to assist in the achievement of interoperability by extending CASE concepts and tools in this specialized direction.

We can distinguish two basic classes of interoperability: at the level of transactions and at the level of provision of publicly available data. Examples at the transaction level are:

\- Business system. Communication among the various modules in an order entry/accounts receivable/general ledger system depends on an agreed transaction format, and an assumption of completion. The accounts receivable system assumes that, if it sends a daily total debits transaction to the general ledger, the total debits account is updated. This assumption is frequently audited by control totals: the order entry system will report at the end of the day the total value of orders placed by account customers, while the accounts receivable system will report the total daily debits. The organization will note discrepancies and will take action to resolve them.

\- Electronic data interchange (EDI). Transactions between organizations have an agreed content (e.g. the various fields possibly present on an invoice have standard names and descriptions) and an agreed method for description of format (based on Backus–Naur form). Receipt of messages is audited by the communication system. Overall system audit (did the supplier not only receive the purchase order but also deliver and invoice the goods?) is done by normal business practice supported by exception reporting at the level of the individual organization (Ferguson et al., 1990).

Individual transactions can require quite complex data structures: consider the Australian tax return, which can consist of a main record and several subordinate records depending on the content of the main record. A single multi-database transaction can be extremely complex: consider the bookings necessary for an overseas trip — planes, cars, hotels, etc. — or the transactions necessary to obtain the parts necessary to operate an automobile assembly line for a particular model.

Examples of public data reporting include:

\- General ledger. The general ledger in an organization is a common repository for financial records. Some of the records are kept in detail, while in other cases the details are managed by other systems (such as accounts receivable), with summaries only sent to the general ledger (say daily debits and credits to debtors). The system relies on an agreed format for transactions and on a chart of accounts, which is a company-wide standard for types of financial transactions. The general ledger is used to make a number of routine financial reports, but can also be used as the basis for specific reports. The use of the general ledger is entirely independent of the operation of the contributing systems. Moreover, there is no requirement that the accounts seen in the general ledger be actually held in that information system. Accounts whose detail is managed by other systems (say accounts receivable) could easily be held in the other system, with the general ledger system accessing them by query.

\- Company reporting. Companies registered in a particular political jurisdiction or participating in a particular stock exchange are required to publish a standard set of accounts: generally a profit and loss statement and a balance sheet. These accounts are derived from the individual company's general ledger system, but the accounts used and their definition are standardized by a combination of official regulation and by accounting conventions agreed by the accounting professional associations. The accuracy of the accounts published and the adherence to the standard definitions are audited by a specialized class of accountant. These published accounts are used by a wide variety of other users to make comparisons among companies and to look at trends in performance of a single company. Their standardization is the basis for industries such as investment analysis. Again these published reports may be held by a central agency or may be available on the network as queries on individual information systems. In addition to making sure that an individual report adheres to the standards, there is also a body which ensures that all companies report by a certain date. This is management of the global state of the complex in which the individual companies' information systems participate.

\- Statistical databases. The time series published by organizations such as the Australian Bureau of Statistics and the US Census Bureau have associated with them published procedures and definitions. They also indicate when these definitions change, so that the series is not strictly comparable before and after these changes.

\- Information retrieval services. These typically offer their databases with the user having responsibility to formulate queries using the words which happen to be present. Some such services (e.g. Medlars, operated by the US National Library of Medicine) have a standard vocabulary which is enforced by indexing staff associated with the service.

## CLASSES OF INTEROPERABILITY PROBLEMS

We have identified some special cases of interoperability in which the problems seem to be sufficiently generic to permit useful research: cooperating information systems, public reporting systems and semi-public shared schema systems. The architectural problems and design issues associated with each are somewhat different, and are outlined below.

## Cooperating information systems

These systems interact by transaction. They range from a single organization making two legacy systems interoperate to n-way EDI systems. For these systems, it is necessary that the transactions used to interoperate can be constructed from each system's conceptual models. There is not necessarily any direct access from one schema to another except for the transaction models in the various schemas.

To permit such interoperability it will likely be necessary for all systems to change their conceptual schemas and the other applications running in their environments to include the transaction. This, in itself, is a standard problem in schema evolution and information systems maintenance. The novelty introduced by the cooperating systems is that more than one system must be changed in tandem, and that there is no overriding authority to require that any particular change be made. (In practice, an n-way interoperating system would probably be brought up gradually, by adding one system at a time. The principles hold.) One would expect that in the process of negotiation among the organizations there would be several options canvassed with different balances of costs, and possibly several levels of functionality. CASE tools useful in schema and application maintenance could usefully be extended to support these activities.

In the company/taxation office problem of (1) and (2), in order for the join to be possible, one or both of the organizations must change its schema, and possibly collect additional data. Both change and data collection are at a cost. There are several possible ways to change the two systems so that a join is possible. Since the changes must be coordinated, they are not independent. Tools exist to assist in the estimation of the scope and cost of changes to information systems. For example, both function points (Albrecht & Gaffney, 1983) and COCOMO (Boehm, 1981) are designed to be applied to maintenance activity as well as development. One could imagine that these tools could be adapted to the coordinated change problem.

Furthermore, transactions are produced and consumed by the cooperating systems through applications: transactions are thus part of the dynamics of the systems. It would thus make sense to use information systems dynamic modelling tools at a coarse level to model the transaction activity. For example, a combination of entity–relationship analysis and data flow diagrams is described by Batini et al. (1992). Also, the cooperation of the individual systems introduces questions of global consistency in an environment in which there is no global authority. Tools are needed to model and to manage this (e.g. Rusinkiewicz et al., 1992). Security is also an issue in a similar way.

Problems of global consistency are very deep, even at the query level. For example, suppose a manufacturer M and a supplier S have established an EDI connection. M's purchasing system issues a request for quotation to S. S responds with a quotation. M responds with a purchase request. S responds with a shipping document and an invoice. M responds with a payment. All the fields in all the transactions must be present in the schemas of both information systems.

Furthermore, all the schemas must contain identifying attributes for the objects involved in all the transactions. It is therefore plausible that one organization could make queries requiring the join of these schemas.

For example, M might want to know the amount of money paid in respect of requests for quotations issued in a particular month. For the response to make any sense, M must know the update status of all of the propagated transactions. However, some of the updates are under the control of S, and some of them depend on updates performed by S. Further, in order for S to issue for example the quotation transaction, it might be necessary to consult its own suppliers via EDI transactions.

Concepts must be developed to define the meaning of such queries, and languages developed to express the consistency requirements and audit strategies. The underlying database managers, operating systems and communications networks may be affected. The languages must take into account the underlying transaction management systems, since a transaction might take a long time to execute (Rusinkiewicz et al.; 1992).

Other research problems arise from the need to model dynamics. Such modelling may require some reverse engineering of existing applications: this creates a context for particular aspects of reverse engineering technology, such as a combination of extraction of dynamic models (Horowitz & Reps, 1992) with reverse engineered data models (e.g. Shoval & Shreiber, 1993).

## Public reporting systems

The important aspect of these systems is the existence of a domain-specific uniform set of data descriptions. These data descriptions become standard entities or attributes which must be integrated into the schemas of all the participating information systems. In effect, this class of system has a global schema of which each participating schema is a view, but the individual systems do not exchange transactions among themselves.

If the public data access is by query to the individual systems, then the canonical data model becomes an important design choice. A likely candidate in the near and medium term is a relational model which can be queried by Standard Query Language (SQL). Tools to support construction of the component schema from the local schema would be useful, especially if they have provision for the standard data descriptions. There may also be a place for tools to manage the standard data descriptions: these could be voluminous.

There are also dynamic issues:

\- version control as the standard definitions are updated and there becomes a mixture of standards used for publications;

\- common model for documentation of the public schemas (standards for a common data dictionary);

\- retrospective changes for violation of standards discovered in audit (could be quite serious for, say, company reporting systems);

● trader systems to advertise the sources of the published data (standard descriptions of the services available and the access methods. Similar in many ways to the Medlars example noted above).

## Semi-public shared schema systems

Semi-public shared schema systems occur when a group of systems elects to publish among themselves portions of their schemas in order to support particular classes of query from a controlled group of users. Their export schemas would be diverse but would overlap, allowing non-trivial inter-database join operations. These systems differ from public reporting systems: every system participating in public reporting has the same export schema, while in the present case there is overlap among export schemas, but also diversity.

This is a class of system for which local autonomy is frequently assumed in the literature. An important issue is the extent to which the various local schema are integrated. The conceptually simplest approach is to construct a single global schema. However, this is considered to be impractical for realistic situations on cost and flexibility grounds. This has led to proposals for partial integration. For example, Fang & McLeod (1992) distinguish their federated architecture from systems which have a global schema, justifying their approach on the grounds just stated. In this literature, although a global schema is not constructed, there seems to be no consequences. It is assumed to be possible to perform sufficient integration to achieve the desired result: this would seem to imply the potential existence of a global schema but that it is constructed only as needed (lazily rather than eagerly to use the functional programming terminology).

Our tax office/company example shows that a global schema is not generally even possible without sacrificing local autonomy. This logical non-existence of a global schema has as a consequence a number of problems:

\- What is the boundary of the semantically valid integrated subschemas in the respective schemas? The integration may be in support of a class of transaction, but the common attributes may permit joins outside the common subschemas. Under what conditions are these joins valid?

\- As a corollary of the previous issue, under what circumstances is a global integrated schema possible? What are the consequences for systems in which a global schema is not possible? What cannot be done?

\- It may be the case that the dominant cost item in achieving an integrated subschema is the gathering of additional data. The organizations may agree to permit null values for some of the new attributes in pre-existing tuples, guaranteeing consistency at the tuple level only for tuples created after a certain data. Over time, older tuples may be deleted. One could wish to know the extent to which the integration has proceeded. Questions arise as to the meaning of queries in this situation. There is also the problem of extensibility of such a design.

\- Queries may need to be as at a particular date. This may require data to be time stamped and for certain reconciliation conditions to be satisfied.

In principle, the semi-public shared schema system admits the possibility of one system performing updates in another's database. It is difficult to envisage a practical situation where this remote update would be feasible. Each local database is subject to a number of local constraints enforced by local applications. A remote system has no access to these constraint enforcement mechanisms. There are cases where one system provides data for the perhaps exclusive use of another, but where the first system has complete control over the data's integrity. This situation is more profitably seen as an update to the first system's database which is visible to the other, rather than as an update to the other database.

Update may be very important in a semi-public shared scheme system, but it is probably more useful to think of the update aspect as a cooperating information system as described above, in which all updates are carried out by transactions applied by the local systems. Looking at it in this way does not necessarily make the problem simple: for example, it is possible that there exist global constraints on a cooperating system complex which are not enforceable by the combined effect of local constraints.

## IMPLICATIONS FOR ARCHITECTURES

The five-level architecture of Sheth & Larsen (1990) seems to be typical of the architectures proposed for federation of databases. This architecture appears to assume at least implicitly that the user is an arbitrary person sitting outside the organizations involved in the federation. In addition, this architecture appears to be intended for applications which are query only: the difficulties of multi-database updates are so great that the assumption of local autonomy and arbitrary databases becomes quite heroic.

In this architecture, the federation structure is logically outside the local databases. Generation of the component schemas is a combination of view definition and syntactic transformation, while the federated schema is essentially a communications problem and export and external schemas are view definitions.

This architecture may not be suitable for all the possible solvable cases outlined above.

\- Cooperating systems probably need help below the local database rather than above it. Applications participating do updates, and must therefore have access to guarantees of global consistency. Queries require consistency status as well as results.

\- Public reporting systems must conform to a published standard global schema. This fits into the component/export schema of the five-level architecture. However, one would expect tools useful in constructing such schemas would have access to the published global schema. In particular tools are needed to assist in resolution of representation conflicts.

\- Query access to semi-public shared schema systems is much like the public reporting systems: the agreed domain terminology is the basis for the global schema, so should be available to each of the local systems in the tools used to assist in their modification to attain conformance.

\- Update access in semi-public shared schema systems is much like in the cooperating systems, needing transaction and global consistency support.

In the literature, interoperable database systems are visualized as a collection of communicating databases to which a user has access. In the five-level architecture, the user is visualized as being presented with the federated schema and a query language and left to it. In applications in which update is performed beyond the boundary of a local system, it is probably misleading to think of the user as a direct participant. It is probably more profitable to think of the updates being performed by applications in a local system acting as the agent of the user.

Consider the travel agency example often used: a user inserts a credit card into a terminal, makes queries, then makes a booking. The application has to do much more than query the databases of the various bookable entities and initiate a booking transaction. For example

\- The application must be authorized to do such things, and must have some standing in the business community.

\- Arrangements must be made for billing as well as booking (there may, for example, be commissions payable).

\- A record must be kept of the entire transaction and its completion status.

\- It may be necessary to undo the transaction if, for example, the credit card company discovers that the card has been stolen and was used fraudulently.

Finally, the designer of a multi-database update application would be assisted by having some sort of view of the local update transaction processing agents, together with their authorization and availability status: this is an external view for the designer, but operationally a view from peer to peer.

## SUMMARY

We have argued that the standard approach to interoperability founders on the problem of semantic heterogeneity, but have suggested some problems which may be both solvable and useful in practice. Based on these arguments, it may be the case that a better way to approach the design and construction of interoperable information systems is to modify the underlying databases, operating systems and communication protocols to permit new interoperating applications to be more easily built, rather than architectures which have effect in the region outside the individual applications, and thus are conceptually external to the platforms on which the individual applications are implemented.

Finally, interoperability is seen to involve many areas of computer science which are also employed in the design and construction of systems generally. There is some need of a definition through which interoperability research can be identified. Interoperability involves multiple information systems which communicate among themselves. Communication is not, in itself, a defining characteristic since most computer systems involve communicating modules. A more specific characterization is needed.

The proposal is to define interoperability as the construction of applications involving several subsystems in which the implementation is constrained either by organizational boundaries or by legacy systems.

## ACKNOWLEDGEMENT

The work reported in this paper has been funded in part by the Cooperative Research Centres Program through the Department of the Prime Minister and Cabinet of the Commonwealth Government of Australia.

## REFERENCES

ACM (1990) ACM Computing Surveys: Special Issue on Heterogeneous Databases, 22, no. 3.

Albrecht, A.J. & Gaffney, J.E. (1983) Software function, source lines of code, and development effort prediction: a software science validation. IEEE Transactions on Software Engineering, SE-9 (6), 639–647.

ANSAware (1993) ANSAware 4.1: Application Programming in ANSAware. Architecture Projects Management, Cambridge, UK.

Batini, C., Ceri, S. & Navathe, S.B. (1992) Conceptual Database Design. Benjamin Cummings, Redwood City, California.

Boehm, B. (1981) Software Engineering Economics. Englewood Cliffs, NJ, Prentice-Hall.

Brodie, M.L. (1992) The promise of distributed computing and challenges of legacy information systems. In: Interoperable Database Systems (DS-5), Hsiao, D.K., Neuhold, E.J. and Sacks-Davis, R. (eds), 1–31. North-Holland, Amsterdam.

Elmagarmid, A.K. & Pu, C. (1990) Guest editors' introduction to ACM (1990), 175–178.

Elmagaramid, A.K., Chen, J. & Bukhres, O.A. (1993) Remote system interfaces: an approach to overcoming the heterogeneity barrier and retaining local autonomy in the integration of heterogeneous systems. International Journal of Intelligent and Cooperative Information Systems, 2, 1–22.

Fang, D. & McLeod, D. (1992) Seamless interconnection in federated database systems. In: Database Systems for Next Generation Applications: Principles and Practice, Kambayashi, Y. (ed.). World Scientific, Singapore.

Ferguson, D.M., Hill, N.C. & Hansen, J.V. (1990) Electronic data interchange: foundations and survey evidence on current use. Journal of Information Systems, 4 (2), 81–91.

Frankhauser, P. & Neuhold, E.J. (1992) Knowledge based integration of heterogeneous databases. In: Interoperable Database Systems (DS-5), Hsiao, D.K., Neuhold, E.J. and Sacks-Davis, R. (eds), 150–170. North-Holland, Amsterdam.

Hammer, J. & McLeod, D. (1993) An approach to resolving semantic heterogeneity in a federation of autonomous, heterogeneous database systems. International Journal of Intelligent and Cooperative Information Systems, 2 (1). 51–83.

- Horowitz, S. & Reps, T. (1992) The use of program dependence graphs in software engineering. In: 14th International Conference on Software Engineering, 11–15 May, Melbourne, Australia, 392–411. ACM Press, New York.

IEEE (1991) Computer: Special Issue on Heterogeneous Distributed Database Systems, 24, no. 12.

OSF (1992) OSF DCE Application Guide. Englewood Cliffs, NJ. Prentice Hall.

Ram, S. (1991) Guest editor's introduction to IEEE (1991), 7–9.

Rusinkiewicz, M., Krychniak, P. & Cichocki, A. (1992) Towards a model for multidatabase transactions. International Journal of Intelligent and Cooperative Information Systems, 1 (3/4), 579–617.

Sheth, A.P. & Larsen, J. (1990) Federated database systems for managing distributed, heterogeneous and autonomous databases. In: ACM Computing Surveys. 22 (3), 183–236.

Sheth, A.P., Gala, S.K. & Navathe, S.B. (1993) On automatic reasoning for schema integration. International Journal of Intelligent and Cooperative Information Systems, 2 (1), 23–50.

Shoval, P. & Shreiber, D. (1993) Database reverse engineering: from the relational to the binary relational model. Data and Knowledge Engineering, 10, 293–315.

SIGMOD (1991) SIGMOD: Special Issue on Semantic Issues in Multidatabase Systems, 20 (4).

Stamper, R. (1985) Management epistemology: garbage in garbage out. In Knowledge Representation for Decision Support Systems Methlie, L.R. & Sprague, R.H. (eds), 55–57. Elsevier Science Publishers, Amsterdam.

Thomas, G., Thompson, G.R., Chung, C-W., Barkmeyer, E., Carter, F., Templeton, M., Fox, S. & Hartman, B.

(1990) Heterogeneous distributed database systems for production use. ACM Computing Surveys, 22 (3), 237-266.

Walter, D.O. & Bellman, K. (1990) Some issues in model integration. In: AI and Simulation Simulation Series Vol 22/3. Webster, W. & Uttamsingh, R. (eds), Society for Computer Simulation, San Diego.

## Biographies

Robert M. Colomb is currently a Senior Lecturer in Information Systems with the Department of Computer Science, University of Queensland, lecturing in advanced databases, software engineering, and the human-computer interface. His research interests include application of deductive database technology to information systems problems, particularly in interoperating database systems; and human-computer interface issues, particularly in open distributed environments. From 1985 to 1990, he was manager of the Knowledge Based Systems Engineering program of the CSIRO Division of Information Technology. He was in 1987 awarded a PhD in computer science from the University of New South Wales. Prior to resuming his studies, he had an extensive and varied career in the computer industry, including commercial, operating systems, programming tools, technical, planning and communications applications, as well as consulting in a variety of areas, both in the United States and Australia. He has a BS in mathematics from the Massachusetts Institute of Technology, awarded in 1964.

Maria Orlowska is currently the Professor of Information Systems at the University of Queensland. She holds MSc (1974) and DSc (1979) degrees in Computer Science from Warsaw University, Poland. Her research interests are: distributed database systems; database theory; information systems design methodologies; and analysis of algorithms. She has published over 90 research papers in international journals and conference proceedings. Since 1992, she has been associated with the Distributed Systems Technology Centre (DSTC) in Brisbane as the Distributed Databases Unit Leader. She has served on a number of program committees for various international conferences, and was recently elected to be a Very Large Databases (VLDB) Endowment Trustee.
