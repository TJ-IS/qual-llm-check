---
otero_id: 17943
otero_key: "N9JJJ46Q"
title: "Treating data privacy in distributed systems"
authors: "U. Bussolati; G. Martella"
year: "1981"
journal: "Information & Management"
doi: "10.1016/0378-7206(81)90049-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Treating Data Privacy in Distributed Systems

U. Bussolati and G. Martella

Istituto di Elettrotecnica ed Elettronica, Politecnico di Milano, Piazza L. da Vinci 32, I-20133 Milano, Italy

This papers describes and is primarily concerned with the security data definition and management in a distributed data base of aggregated type, although the approach described may be applied to any distributed system architecture. A multi-level logical security architecture is presented reflecting the logical architecture of the distributed system. In particular, three security logical schemata are proposed: the network security schema, the external security schemata, and the intermediate security schemata. For each schema data models are introduced, allowing the definition and the management of security information. Mapping rules between the logical levels are discussed. Finally security mechanisms are analyzed.

Keywords: Privacy, security mechanism, secure data base management system, secure distributed systems.

![](/api/attachments/N9JJJ46Q/fulltext/images/c83c1259bcfd28d7f021b781af32d1a04d2da05206d26447cb2f60227a69d999.jpg)

Umberto Bussolati received the degree in Electronics Engineering from the Politecnico of Milan in 19'9. Since then, he has contributed to researches developed in the Computer Science Laboratory at the Electrotechnics and Electronics Institut in Politecnico of Milan, where now he is a Researcher in Computer Science. He is a specialist in privacy and security management in information systems and has developed several works in this area which he has submitted to and presented in many international congresses and scientific reviews. He gives lessons and courses on this topic and has published the first Italian book on computer security. His researches also include database and office information systems management and design, with various published contributions. He participates to the National Researches Council's project on automatized methodologies for database design.

## 1. Introduction

Distributed Data Base systems emerged often from a successful combination of local data base that need to intercommunicate. As a manager, our fundamental responsibility will always involve the security of information, as that is a functional goal of the organization. This trend is in line with the present policies concerned with conservation and integration of large amount of data, where different types of local data bases may have different value for each local data base administrator. Therefore different security policies, that is high-level guidelines concerning information security, must be allowed.

Security mechanisms, that is a combination of software techniques and procedures used to implement and enforce the various security policies, must be employed to provide a meaningful security management. In doing so, it is important to consider the objectives to be accomplished and the specific DDB systems requirements.

![](/api/attachments/N9JJJ46Q/fulltext/images/0bac142215755e3c670c2ee92af3a63c24b93c0989af50e5c9ed1abe619158db.jpg)

Giancarlo Martella received the Dr. Ing. degree in Electronics Engineering from the Politecnico of Milan in 1968. Since then, he has been with the Computer Science, Laboratory at the Istituto di Elettrotecnica ed Elettronica of the Politecnico di Milano, where he is currently an Associate Professor of Computer Science. His main research interests are in the field of information systems analysis and design, data base management, distributed informatics. His current researches include data base security and privacy control. He authored more than thirty papers on these topics and has been invited to many workshops and conferences. In the 1981 he has received the Huspi international award for a research on automated data bases in clinical applications, and the Cilea-Univac award for a research on data security in information systems. He has consulted for several companies and governments on advanced EDP system design, and has organized post-doctoral courses for technical and management personnel. He is the Chairman of the working group on Information Systems of the Italian Association for Automatic Computing (AICA).

In particular a Distributed Data Base (DDB) must permit users to selectively share data, while still retaining the ability to restrict data access. There must be a mechanism to provide protection and security, permitting information to be accessed only by properly authorized users. Further, where rights access are created and destroyed dinamically, the granting, checking and revocation of authorization to use them must also be automatic.

These mechanisms are not allowed by usual operating systems. In fact there are some fundamental differences between operating system security and data base system security, as listed below [1,2].

• There are more elements to be protected in a DDB and a large number of data objects with complex interrelationships and a broad variety of data types.

• DDB security is concerned with the semantics of data, while the OS security is concerned with the name and address spaces of the data. This implies the need for different security requirements for the different architectural logical levels — internal, conceptual and external.

\- In DBB each user may have a different conceptual security view of the data and their relationships.

• The need for data independence in DDB requires that definitions of the security data be logical entities, far removed from the phisically oriented objects used by the OS.

In this paper we present a system architecture which allows the management of security information, in particular the control and monitoring of access to information stored in a distributed data base.. In the following section we describe the system architecture, and the different security logical levels composing the system. Next we define the mapping operations between the different levels. Finally we present the protection mechanisms allowed. A theme of the paper is to present a data base approach to DDB security. Such a view is more likely to bring modularity, integrability and flexibility to overall system solutions than will ad hoc attempts to tune-up individual parts.

## 2. Architecture

The architecture of the distributed data base (DDB) taken into consideration is the multilevel and aggregated one, shown in Fig. 1 [3,4]. Two macro-levels can be put on evidence: the local and the global ones. The first is the logical level involving each local data base (LDB) in its local activities. The second is the logical level involving the whole system in its distributed environment.

At local macro-level, each LDB is independent and retains its traditional structure for data definition and manipulation at three levels: internal (IS) conceptual (LCS) and external (LES) schema. The LES are kept separate because the architecture is of an aggregated type and therefore some Users (D1, D2, E1, E2, etc.), working on some Applications (D, E, F, G) utilize local resources and data and do not need the distributed system.

At global macro-level, an information sub-set of each LDB, becomes part of the distributed system involving network applications.

Definition of information which is part of the distributed system is included in the Network Schema (NS).

As far as DDB users are concerned, the Network Schema acts as the Conceptual Schema in a centralized structure; moreover, the network applications (A, B, C) utilize logical views of the DDB, which are composed by means of the relevant Global External Schemata (GES).

A particular user class (A1, A2, A3, B1, etc.) is recognized as being or not being part of the distributed system depending on whether it uses a schema of the local or global type.

The transition to the network level is therefore automatic and the user is distinguished by an identifier plus the identifier of the application that is to be used.

It must be stressed that since the local DB are pre-existing the Local Conceptual Schema are generally heterogeneous, i.e. described by different models.

A homogenization level is therefore necessary, in which data regarding each LDB are expressed using their own model. Such a level is represented by the Intermediate Conceptual Schema (ICS) [5]. After such homogenization, this information is inserted into the Network Schema, while eliminating redundancy.

From the above we can see the fundamental importance of the choice of the best model for describing the Intermediate Conceptual Scheme.

![](/api/attachments/N9JJJ46Q/fulltext/images/e1648561ded03d7731e5a4f371b4115cd97e6eecada2be6489501424f968c07b.jpg)  
Fig. 1. The Aggregated DDB Architecture.

This problem, which concerns all information at the various levels, is most debated, and several proposals have been submitted to resolve it [6,14].

To define and manage security information in the mentioned architecture, we represent security information by quadruples of the form $(s, o, r, p)$ where s is the subject which can exercise the right r on the object o under certain conditions expressed by the predicate p [15].

Subjects are the application users, the applications or the programs used by the users. Objects are the protected resources defined in the network schema of the DDB; in a relational DDB these may be relations,

domains, class of relations.

Rights are operations that can be performed by the subjects involving some objects. We distinguish among three types of rights: access rights, which allow a subject to perform an access operation to an object, i.e. read, delete, insert, etc.; administrative rights, which allow a subject to grant and to revoke access rights to other subjects; property rights, which allow a subject to grant and to revoke access, administrative and property rights too.

Predicates are logical or physical conditions which must be true to allow a right to be exercised by a subject.

Our proposal is to structure security information into different logical levels reflecting the logical architecture of the DDB previously mentioned (Fig. 2). This permits to obtain independence in the definition and modification of the users' security requirements and of the security constraints of the system resources.

In particular, we define the Security Global External Schema(ta) (GES/security) the Security Network Schema (NS/security) and the Security Intermediate Conceptual Schema(ta) (ICS/security).

The GES/security represents all the rights that a certain user (to which the schema is related) can exercise on certain resources (specified in the schema) of the distributed data base. A relational model [16] is used to define it.

The NS/security describes restrictions that must be exercised on all the protected resources of the distributed data base, keeping in mind the security requirements of the Local Data Bases. A relational model is used to define it.

The ICS/security level is necessary because the security rules generally reflect (and are related to) the local data models which are heterogeneous in an aggregated DDB; thus, it represents an intermediate level between the different definitions of the local security requirements on the distributed resources and the global security rules uniformly expressed in the NS/security. In our proposal a binary relational model [17] is used to define it.

## 2.1. Schemata Definition

## 2.1.1. Security Global External Schema(ta)

The GES/security is described by a table (relation), regarding a particular subject, in which are listed the objects on which the subject can exercise some right, the corresponding rights and the predicates limiting these rights.

![](/api/attachments/N9JJJ46Q/fulltext/images/f3f40f54b00902c89504d90560eb40463a9b8b99d1c447beaeabff0cb59aa619.jpg)  
Fig. 2. The Security Logical Levels.

Every subject has its own GES/security which is presented to him with the traditional DDB external schema regarding that subject. Fig. 3 illustrates a set of security rules specified for the user U on the inside of the application A (UA).

From this figure we deduce that the user U/A has the right to read and update the CUSTOMER relation (defined in the DDB external schema) if the value of the PLACE domain of this relation is FRANCE. He can also grant or revoke the right to read this relation under such condition (in fact he has the administrative right AD.READ). Moreover, he can read the PRODUCT relation with no restriction (p is TRUE).

The GES/security represents the security constraints of a user and, therefore, is subject to be modified by the Security Administrator in order to put in practice the authorization policies of the organization.

## 2.1.2. Security Network Schema

The NS/security is bound to the security requirements of the protected resources which, in an aggregated DDB, derive from the security requirements of the local DBs. As it is related to the security constraints of the object, the NS/security is generally a less dynamic entity than the GES/security and is described by a single table (relation), regarding the whole distributed system, in which are listed the actions (rights) which can be performed on the resources (objects) under certain conditions (predicates).

A particular domain may be inserted indicating specific application environments in which the resources must be used. Fig. 4 illustrates a set of security rules specified at NS level. From this figure we deduce that the CUSTOMER relation can be read and updated only by application A and, in the case of updating, with the restriction that the value of the PLACE domain is FRANCE or ENGLAND. Moreover, the PRODUCT relation can be read with no restrictions in any application environment. Finally, the procedure MI (defined in the DDB network schema) can be used only by the AUDIT application.

The information in NS/security allows to define the various GES/security. Thus, all the objects and the security rules in the GES/security must also be in the NS/security and the security information represented in every GES/security must be a subset of the security information represented in the NS/security, as shown in the previous examples.

## 2.1.3. Security Intermediate Conceptual Schema(ta)

The ICS/security is defined using a binary model. The entities composing security information are broken down into elementary units, homogeneizing at global level the security requirements of local level. Each ICS/security is related to a local DB and its structure is shown in Fig. 5.

In this figure, subjects, objects, rights and predicates are represented together with their identification attributes, the relation between them and two connection elements (A and B entities) which permit to describe in a binary form the security information.

An example of a set of security rules defined at ICS level and represented by the binary relations of Fig. 5 is illustrated in Fig. 6.

We see that the security information represented in the ICS/security of this figure allows the application A (subject) to read and update the CUSTOMER relation with no conditions. The various ICS/security, reflecting the security requirements of the local DBs, allows to define the NS/security on the ground of the security policies of the distributed system. Such policies must not compromise the security constraints at local level, therefore the security rules in NS/security are at least so restrictive as those in ICS/security.

<table><tr><td>s</td><td>p</td><td>r</td><td>p</td></tr><tr><td>UA</td><td>REL. CUSTOMER</td><td>AC. READ</td><td>CUSTOMER. PLACE = FRANCE</td></tr><tr><td>UA</td><td>REL. CUSTOMER</td><td>AC. UPDATE</td><td>CUSTOMER. PLACE = FRANCE</td></tr><tr><td>UA</td><td>REL. CUSTOMER</td><td>AD. READ</td><td>CUSTOMER. PLACE = FRANCE</td></tr><tr><td>UA</td><td>REL. PRODUCT</td><td>AC. READ</td><td>TRUE</td></tr></table>

Fig. 3. Security Information at GES Level.

<table><tr><td>ac</td><td>o</td><td>r</td><td>p</td></tr><tr><td>A</td><td>REL. CUSTOMER</td><td>AC. READ</td><td>TRUE</td></tr><tr><td>A</td><td>REL. CUSTOMER</td><td>AC. UPDATE</td><td>CUSTOMER. PLACE = FRANCE ENGLAND</td></tr><tr><td>ALL</td><td>REL. PRODUCT</td><td>AC. READ</td><td>TRUE</td></tr><tr><td>AUDIT</td><td>PROC. M1</td><td>AC. USE</td><td>TRUE</td></tr></table>

Fig. 4. Security Information at NS Level.

![](/api/attachments/N9JJJ46Q/fulltext/images/d6c70a208291468a0522a141e47e6053fe8fa11b35bbfd0827b07f8cea904ca8.jpg)  
Fig. 5. The Structure of ICS/Security.

<table><tr><td colspan="2">HAS OB</td><td colspan="2">HAS SUB</td></tr><tr><td>s</td><td>A</td><td>A</td><td>o</td></tr><tr><td>A</td><td>A1</td><td>A1</td><td>REL. CUSTOMER</td></tr><tr><td>A</td><td>A2</td><td>A2</td><td>REL. CUSTOMER</td></tr><tr><td colspan="2">HAS RIGHT</td><td colspan="2">HAS SUBOBJ</td></tr><tr><td>A</td><td>B</td><td>B</td><td>r</td></tr><tr><td>A1</td><td>B3</td><td>B1</td><td>AC. READ</td></tr><tr><td>A2</td><td>B2</td><td>B2</td><td>AC. UPDATE</td></tr><tr><td colspan="2">HAS PRED</td><td></td><td></td></tr><tr><td>B</td><td>P</td><td></td><td></td></tr><tr><td>B1</td><td>TRUE</td><td></td><td></td></tr><tr><td>B2</td><td>TRUE</td><td></td><td></td></tr></table>

Fig. 6 Security Information at ICS Level.

The deduction of security information from local to global level happens by means of ICS level through three transition stages [18]. The first stage concerns the transition from local level to ICS level allowing for the homogeneization of security information obtained by using the binary model.

The second stage consists of checking the consistency of the locally obtained information at ICS level. For instance, resources considered strictly confidential in a data base, can be unprotected in another; a same user class can have clashing rights in two different nodes of the system; a same object class can have different semantic integrity restrictions and so on, A normal practice could be, at the distributed level, attributing to a resource the strongest of the local security restrictions and to an application or user class the lowest accessibility degree among those locally allowed.

Such a choice, however, can be too restrictive and might cause excessive rigidity in the protection rules. To prevent this, a possible feedback modification of the local restrictions could be thought in order to modify at the local level those restrictions which are too limiting at the distributed level.

The third stage, the consistency controls once have been overcome, consists of eliminating redundancy of security information, making sure that the NS/security is constituted by unduplicated (in the logical sense) information, thus avoiding “internal” consistency problems.

The three operations considered above have to respect rules of correctness in mappings illustrated in the next section.

## 3. Mapping

The problem of a correct definition of mapping between logical level arises in DB architectures which follow the ANSI-SPARC proposal [19].

Two aspects are involved: the structural correspondence, that is the translation of information from a level to another, and the operational correspondence, that is the translation of operations performed at one level into operations at the other level.

In the proposed secure DDB automatic mapping operations are necessary between the various LCS/security and the corresponding ICS/security (homogenization stage), between the various ICS/security and the NS/security (consistency and redundancy control) and between the NS/security and the different GES/security.

The mapping problem between such levels turns up both in the design stage as well as during the updating of the security requirements.

Utilizing the concepts of the many-sorted algebra [20], every logical level can be described by a set of operands (states of each level) and a set of operators. For each schema of one level the pair (set of operands, set of operators) can be defined. Therefore, the local level can be described by a number of these pairs equal to the number of the local DB, the intermediate level by the same number of pairs (one for each ICS/security), the network level by a single pair and the external level by a number of pairs equal to the number of the GES/security.

In general, a fundamental correctness rule can be defined [21] essentially stating that the correspondences (structural and operational) between levels are bijective. This rule is illustrated in Fig. 7 where it is shown that starting from a state $a_{m}$ ( $m=1,n$ ) of a logical level $A$ and performing a set of operations $H$ , another state $a_{m+1}$ of this level is reached such that, translating this state into a state $b_{m+1}$ of another logical level $B$ by means of the structural correspondence $T'$ and performing at this level the translation of the previously set of operation (operational correspondence) $K=T''(H)$ , another state $b_{m}$ of the level $B$ is reached which is the structural translation of the initial state $a_{m}$ .

Also if this rule is valid for the mapping between any logical levels of the security architecture, other constraints must be defined for the LCS-ICS/security and ICS/security-NS/security mappings, keeping into account the homogeneization process for the first and the consistency control for the second.

In the LCS-ICS/security mapping, a constraint must be added to the correctness rule, stating that all the LCS (described by heterogeneous models) are translated in ICS/security described by a common (binary) model.

This is done (Fig. 8) by imposing that the LCSs described by different pairs (set of operands $L_{i}$ , set of operators $\alpha_{i}$ ) are translated into ICS/security described by the same pair (set of operands I, set of operator $\beta$ ).

![](/api/attachments/N9JJJ46Q/fulltext/images/4ea955f5c82fc9d4c8f71cd721dd13aa3c0094ae72a45eca40b81ca2b4e4f067.jpg)  
Fig. 7. Correctness Rule Between the Levels A and B.

![](/api/attachments/N9JJJ46Q/fulltext/images/6c3b600f83f7855599701192583c326b7b4c7242fe3bec678348bc1c1d1efe0e.jpg)  
Fig. 8. Correctness Rule in the LCS-ICS/Security Mapping.

![](/api/attachments/N9JJJ46Q/fulltext/images/2b44267f118915950026ad4047a62082ce55f96b2e7579de2f66719f18061e26.jpg)  
Fig. 9. Correctness Rule in the ICS/Security-NS/Security Mapping.

In the ICS/security-NS/security mapping, it must be imposed that the correctness rule belongs to a set of consistency rules stating how (with which policy) the NS/security is obtained from the set of the ICS/security (Fig. 9).

An example of policy may be applying at global level the most restrictive security rule among those defined at local level. It is important to underline that more the policy is restrictive at global level, more the modifications of the security requirements at local level may become unacceptable for the distributed systems (the changes propagation is amplified) and the DDB Administrator's mediation among the local DBAs necessary for a compromise solution. Finally, the NS/security-GES/security mapping must essentially keep into account the changes of the security requisites due to the mechanisms of rights grant and revocation which are described in the following section.

## 4. Security Mechanisms

The authorization policies of the system include control of the access to the protected resources, control of the propagation of the rights, and control of the changing of the local security requirements [22,23].

The access control involves the GES/security level. The control of the propagation of the rights (by operations of grant and revocation) reflects the policies of the distributed systems and involves only the global level (GES/security and NS/security).

The control of the changing of the local security requirements, which reflects the policies (of some) of the local DBs, involves all the logical levels of the proposal architecture (GES/security, NS/security, ICS/security).

The GES/security is used by the Distributed Data Base Management System (DDBMS) to control the access requests of a user to protected resources. The access is controlled in this way: after an identified user's request for an access by means of a quadruple $(s', o', r', p')$ , where $s'$ is the identifier of the user himself, the DDBMS examines the user's GES/security to control if such a quadruple belongs to the schema. In particular, in the schema instances of $(s, o, r, p)$ must exist such that $s = s'$ (this is always verified if the schema of that user exists in the DDB) $\wedge o = o' \wedge r = r' \wedge (p \vee \overline{p}')$ .

The last term relative to the predicates indicates that the condition expresses by the user must be a subset of the conditions permitted to him. Such a control sequence, if passed, grants access to the requested resources.

The control of the propagation of the rights is effected by the DDBMS which uses the grant and revocation algorithms. A user can grant or revoke authorizations to another user only if he has administrative rights (with which he can grant or revoke access rights), or property rights, (with which he can grant or revoke access, administrative and property rights).

In particular the grant algorithm (Fig. 10) is composed of two control procedures (RIGHTCHECK and CONSTRCHECK) two enforcement procedures (ERR1 and ERR2) and one insertion procedure (RIGHTINSERTION). A grant request from a user is expressed by means of the hexaple $(G, s_1', s_2', o_2', r_2', p_2'$ where $G$ indicates that it is a right grant operation, $s_1'$ is the subject granting the right, $s_2'$ is the subject to whom the right is granted, $o_2'$ is the object on which the right is exercised, $r_2'$ is the granted right, and $p_2'$ expresses the conditions limiting such a right.

This hexaple is separated by the DDBMS into two quadruples $(s_{1}^{\prime}, o_{1}^{\prime}, r_{1}^{\prime}, p_{1}^{\prime})$ and $(s_{2}^{\prime}, o_{2}^{\prime}, r_{2}^{\prime}, p_{2}^{\prime})$ . The first one indicates the minimal conditions which must be true in the GES/security of user $s_{1}^{\prime}$ in order that he can effectively grant the considered right (for example, he must have at least an administrative right in order to grant an access right, and so on).

![](/api/attachments/N9JJJ46Q/fulltext/images/624faa1e8320b57e79ccdda0fe2ffae54690d9e7ae1defae41cd346961b32b81.jpg)  
Fig. 10. Grant.

The second one represents the information to insert in the GES/security of user $s_{2}^{\prime}$ after having passed the controls.

The RIGHTCHECK procedure controls that the first quadruple belongs to the GES/security of $s_1'$ , that i that the granter can effectively perform the grant operation. If such control is not passed the enforcement procedure ERR1 is called.

The CONSTRCHECK procedure controls that the second quadruple is not in contrast with the security information of the NS/security (for example that a right is not granted to a user which doesn't belong to the applications being permitted to use that right). If such control is not passed the enforcement procedure ERR2 is called, on the contrary the information is inserted (if it doesn't already exist) in the GES/security of $s_2'$ by the RIGHTINSERTION procedure.

The revocation algorithms (Fig. 11) is composed of two control procedures (RIGHTCHECK and EXISTCHECK), three enforcement procedures (ERR1, ERR3, ERR4) and one deletion procedure (RIGHTDELETION).

Another control procedure (AUTHCHECK) is called by the EXISTCHECK procedure.

A revocation request from a user is expressed by means of the hexaple $(R, s_{1}^{\prime}, s_{2}^{\prime}, o_{2}^{\prime}, r_{2}^{\prime}, p_{2}^{\prime})$ where R indicates that it is a right revocation operation, $s_{1}^{\prime}$ is the subject revoking the right, $s_{2}^{\prime}$ is the subject from whom the right is revoked, $o_{2}^{\prime}$ is the object on which the right is exercised, $r_{2}^{\prime}$ is the revoked right, and $p_{2}^{\prime}$ expresses the conditions limiting such a right.

![](/api/attachments/N9JJJ46Q/fulltext/images/60415441bb64e6c133812e51a0d41a4c309ad1801da24187bc9f77aa8882cd95.jpg)  
Fig. 11. Revocation.

This hexaple is separated by the DDBMS into two quadruples $(s_{1}^{\prime}, o_{1}^{\prime}, r_{1}^{\prime}, p_{1}^{\prime})$ and $(s_{2}^{\prime}, o_{2}^{\prime}, r_{2}^{\prime}, p_{2}^{\prime})$ . As in the case of grant, the first one indicates the minimal conditions which must be present in the GES/security of $s_{1}^{\prime}$ in order that he can effectively revoke the considered right, while the second one represents the information to eliminate from the GES/security of $s_{2}^{\prime}$ (and maybe from the NS/security) after having passed the controls.

The RIGHTCHECK procedure controls that the first quadruple belongs to the GES/security of $s_1'$ , that is that the revolver can effectively perform the revocation operation; if he can't, the enforcement procedure ERR1 is called.

The EXISTCHECK procedure controls that the second quadruple belongs to the GES/security of $s_2'$ and, in the affirmative case, controls, through the AUTHCHECK procedure, that $s_1'$ has sufficient authority over $s_2'$ in order that the right can be revoked (for example, $s_1'$ and $s_2'$ may have same administrative rights and then $s_1'$ cannot revoke an access rights to $s_2'$ ).

If the controls of the AUTHCHECK procedure or of the EXISTCHECK procedure are not passed the enforcement routines ERR4 or ERR3 are called respectively.

If both these controls are passed positively, the information is eliminated from the GES/security of $s_{2}^{\prime}$ by the RIGHTDELETION procedure. It is also controlled if the revocation operation involves also the NS/security (for example, if the right is revoked to an application which is present in the domain ac of the NS/security with this right).

In this last case, the information is eliminated from the NS/security too.

The control of the changes of the local security requirements must be carefully observed by the Security Manager of the DDB because, as already mentioned, modification at local level may cause more or less changes on the ground of the system policies in relation with the local DBs policies.

In any case, this control involves all the logical levels of the distributed system and the choice to authomatize it must be carefully pondered.

## 5. Conclusion

A multilevel security architecture has been presented, based on the architecture of an aggregated DDB with heterogeneous local DBs. Three logical security levels have been introduced: the Global External Schemata, the Network Schema, and the Intermediate Conceptual Schemata, allowing to homogenize the local security requirements at global level. The models representing security information at various levels have been presented. The mapping requirements and rules between the logical levels have been analyzed. Finally the mechanism to control access and dynamic modifications of security requirements have been analyzed.

## References

[1] H.R. Hartson, Data Base Security-System Architectures. Information Systems, vol. 6, n. 1 (1981).

[2] C. Wood, E.B. Fernandez, R.C. Summers, Database Security: Requirements, Policies, and Models, IBM Systems Journal, vol. 19, n. 2, (1980).

[3] G. Bracchi, G.M. Nijssen, eds, Data Base Architecture. (North Holland, Amsterdam, 1979).

[4] S. Spaccapietra, Heterogeneous Data Base Distribution, CREST SRC Advance Course on Distributed Data Bases, (Sheffield City Polytechnic, July 1979).

[5] M. Adiba, Un modèle relationnel et une architecture pour les systemes de base de données réparties. Application au project POLYTHEME, Thèse d'état, Université Scientifique et Medicale, (Grenoble, Sept. 1978).

[6] A. Klug, D. Tsichritzis, Multiple view support within the ANSI/SPARC Framework, Proc. VLDB Conf. (Tokio, Oct. 1977).

[7] C.J. Date, An architecture for high-level language database extensions, Proc. ACM SIGMOD Conf. (Washington D.C., June 1976).

[8] J.R. Abrial, Data Serantics in Data Base Management, Kimblic and Hoffeman Eds., (North-Holland, 1974).

[9] G. Bracchi, P. Paolin, G. Pelagatti, Binary logical associations in data modelling, in G.M. Nijssen ed, Modelling in data base management system (North-Holland, (1976).

[10] M.E. Senko, DIAM as a detailed example of the ANSI/SPARC architecture, in G.M. Nijssen ed, Modelling in data base management systems (North-Holland, 1976).

[11] P. Hall, J. Owlett, S. Todd, Relations and entities, in G.M. Nijssen ed, Modelling in data base management systems, (North-Holland, 1976).

[12] E.T. Lisboa, Une proposition de correspondence entre interfaces externes heterogenes et interface conceptuelle d'une architecture de bases de données reparties, Thèse de Docteur Ingenieur, Université Paris 6, (Paris, June, 1979).

[13] H. Biller, On the equivalence of data base schemas. A semantic approach to data translation. Information Systems, vol. 4, n. 1, (1979).

[14] M. Hammer, D. McLeod, The semantic data model: a modelling mechanism for data base applications, Proc. ACM SIGMOD Conf., (Austin, Texas, May-June 1978).

[15] U. Bussolati, G. Martella, Managing Data Privacy in Data Base Management System, Proc. of Convention Informatique Latine, (Barcelona, June 1981).

[16] E. Codd, A Relational Model of Data for Large Shared Data Banks, CACM, 13-16, (June 1970).

[17] C. Baldissera, S. Ceri, G. Pelagatti, G. Bracchi, Interactive Specification and Formal Verification of User's Views in Data Base Design, Proc. 5th Int. Conf. on VLDB (Rio de Janeiro. 1979).

[18] U. Bussolati, G. Martella, On Designing a Security Management System for Distributed Data Base; Proc. of IEEE Fourth International Computer Software and Application Conference, COMPSAC 80, (Chicago, Oct. 1980).

[19] The ANSI/3/SPARC DBMS Framework, Report of the Study Group on Data Base Management System, Eds., D. Tsichritzis and A. Klug, AFIPS Press, (1977).

[20] J.A. Gogneu, J.N. Thurcher, E.G. Wagner, J.B. Wight, Abstract Data Types as Initial Algebras and the Correctness of Data Representations, Proc. Conference on Computer Graphics, Pattern Recognition and Data Structures, (Beverly Hills, Calif. (1975)).

[21] P. Paolini, G. Pelagatti, Formal definitions of mappings in a data base, Proc. ACM SIGMOD Conf., (Toronto, Canada, Aug. 1977).

[22] U. Bussolati, G. Martella, A Database Approach to Modeling and Managing of Security Information, Proc. of Seventh International Conference on Very Large Data Bases, VLDB 81, (Cannes, 1981).

[23] U. Bussolati, G. Martella, Access Control Management in Multilevel Database Models, Proc. of Third Conference of the European Co-operation in Informatics, ECI 81, (Monaco, 1981).
