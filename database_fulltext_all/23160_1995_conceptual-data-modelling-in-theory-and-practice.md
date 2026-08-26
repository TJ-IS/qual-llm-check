---
otero_id: 23160
otero_key: "2PB6KHTX"
title: "Conceptual data modelling in theory and practice"
authors: "D. Batra; G.M. Marakas"
year: "1995"
journal: "European Journal of Information Systems"
doi: "10.1057/ejis.1995.21"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Conceptual data modelling in theory and practice

D. BATRA $^{1}$ and G.M. MARAKAS $^{2}$

$^{1}$ Decision Sciences and Information Systems, Florida International University, Miami, Florida 33199, USA and $^{2}$ Department of Information Systems, University of Maryland, College Park, Maryland 20742, USA

Conceptual data modelling (CDM) refers to the phase of the information systems development process that involves the abstraction and representation of the real world data pertinent to an organization. When CDM is properly and rigorously performed, the delivered system is expected to be functionally richer, less error-prone, more fully attuned to meet user needs, more able to adjust to changing user requirements and less expensive. However, there is little evidence that conceptual data modelling for the enterprise is actually conducted. There is the feeling that the 'corporate reality' is much different. In many organizations, CDM is never employed. In others, it is applied in a haphazard, project-to-project basis, thus leading to considerable redundancy. The academic community has mainly focused on proposing semantic data models but has not demonstrated a rigorous basis for conceptual data modelling. Specifically, the community has failed to show how a conceptual data model can map to an accurate logical data model. It is the purpose of this paper to discuss and compare the perspectives of academic and practitioner communities regarding the application of conceptual data modelling.

## Introduction

As the field of information systems (IS) matures, its literature becomes swollen with development methodologies, each offering a reasonably adequate set of tools and procedures intended to support the development and design process. Avison and Fitzgerald (1988) have coined the phrase ‘methodology jungle’ to refer to this plethora of perspectives on IS development. Bubenko (1989) estimates that there are literally hundreds, if not thousands, of IS development methodologies. Davis (1993) discusses a number of software requirements methodologies and includes a comprehensive bibliography of more than 700 references.

Within this rich knowledge base of development techniques are various perspectives regarding the best way to capture database structures in preparation for physical implementation of the system. The term conceptual data modelling (CDM) is used to refer to the phase of the development process that involves the abstraction and representation of the real world data pertinent to an organization (Brodie, 1986). On the surface, there is a general consensus in the IS literature regarding the value of CDM. The concept of CDM is closely tied to the database approach and enterprise-wide modelling. When CDM is properly and rigorously performed, the delivered system is expected to be functionally richer, less error-prone, more fully attuned to meet user needs, more able to adjust to changing user requirements and less expensive (Ludovici, 1990; McFadden & Hoffer, 1994).

Davydov (1994) describes data modelling as an activity that involves the creation of abstractions that represent a data-oriented image of a given application. The data modelling process distinguishes between three major types of representations: (1) the conceptual representation which identifies entities and their interrelationships; (2) the logical representation which results from the translation of a conceptual representation into one that is compatible with the chosen DBMS; and (3) the physical representation which specifies implementation details like indexes, hashing, assignment of files to blocks and access paths, which lead to efficient performance of the system. It is generally believed that this ‘three-schema’ approach (McFadden & Hoffer, 1994) promises considerable benefits in the design process. The rationale is that the focus on the conceptual and logical representations of the process defers issues of physical implementation, thereby permitting the systems analysis to proceed as an exercise in pure reason (DeSmedt, 1994).

The focus of this paper is on the first model in the triad: the conceptual model. (Note that the terms model and representation are used interchangably.) The aim of the analyst is to create a representation that will serve to answer several questions: What does the organization want information about? What type of information is needed? What are the business implications of these answers? (Ludovici, 1990).

The ISO report on conceptual schema (Griethuysen, 1983) identifies four major objectives of conceptual data modelling: (1) suitable modelling facilities for static and dynamic assertions about the enterprise; (2) ease of use and understandability; (3) easy adaptation to changes in the abstraction of the organization; and (4) provisions for a common language for communication between users and the information processor. Further, a CDM should facilitate communication and ease user validation of requirements (Juhn & Naumann, 1985).

However, within this seemingly general consensus regarding the value of CDM, there lies a myriad of disparate viewpoints regarding the degree to which application of CDM is deemed useful or practical in an applied environment. There are clearly many strong supporters of conceptual data modelling. Ludovici (1990) argues that data models are the key to successful database design and that no knowledge or training can have a greater impact on the corporate bottom-line than effective data modelling training. Navathe (1992) suggests that the recent effort to standardise the representation and modelling of data has brought about a renaissance of CDM and many organizations are embarking on corporate data modelling as part of the strategic planning activity.

These staunch defenders of CDM are not without their detractors, however. Scheer and Hars (1992) agree that CDM techniques have become an integral part of IS development methodologies but suggest that the ‘corporate reality’ is much different. They argue that in many organizations CDM is applied in a haphazard, project-to-project basis, thus creating redundancy factors estimated to exceed 10. Brand and Gerritsen (1993) suggest that movement away from the complexities of CDM to simpler data modelling approaches, combined with a strict avoidance of CASE tools, were primary factors in the success of the new Collection Management System developed for the National Gallery of Art. Finally, Giordano (1993) maintains that the corporate reality regarding application of the theoretical concepts of CDM is a myth that has resulted in many organizations moving away from the concept of an information warehouse to one of an information ‘where?’ house.

Is conceptual data modelling (CDM) a myth or reality? What is the perspective of the academic community on CDM? Have practitioners embraced and employed CDM? What is the future of CDM? It is the purpose of this paper to explore these questions. We first consider the academic perspective and view it from two sources: empirical findings and conceptual research.

## Academic perspective: empirical findings

There are two dominant research strategies used by empirical researchers: field surveys and laboratory experiments. Although few empirical studies have been conducted in the area, they reveal interesting findings.

Grover and Teng (1992) conducted a field survey to study the extent and purpose of DBMS adoption in the USA. Their study revealed that suggested database benefits are not being achieved by organizations. Operational benefits, like a more powerful file management system, are being attained rather than those involving managerial analysis and planning. This study suggests that although DBMS have been adopted, the database approach has not been realised, and probably the notion of conceptual data modelling is not very popular.

The results of a survey of the adoption of systems analysis and design techniques conducted by Palvia and Nosek (1993) teach us some interesting lessons. The authors found that twenty-six methods, or half of those extracted from the literature, are used by less than 10% of the respondents. At the time of the survey, thirteen methods (ADS system, BIAIT, BICS, SREM, SOP, automated ADS, information algebra, Young/Kent methodology, Langefors methodology, information engineering, SADT, PLEXSYS and ISDOS) were hardly used at all. The authors provide the following plausible explanations: some methods are outdated, some are too complicated, some were never fully developed and proven, while others are too academic or research oriented. The survey revealed that simple techniques such as systems flow charts and data flow diagrams are widely used.

Although Palvia and Nosek (1993) did not study conceptual data modelling, one can extrapolate their findings to expect that simple data models are likely to be used in practice. However, Grover and Teng's (1992) study hints that enterprise modelling is of limited concern to practitioners; database technology is mainly used for more powerful access methods. Thus, conceptual data modelling is likely to be used in organizations for designing data models for specific applications, not for enterprise modelling.

The next question, therefore, is: for specific applications, does conceptual data modelling lead to quality representations? In other words, should we directly translate user requirements into a logical (e.g. relational) representation, or should we first translate user requirements into a conceptual representation which is free of implementation concerns, and then translate the conceptual representation into a logical representation? Note that the conceptual to logical translation can be accomplished by a software tool if the mappings can be clearly stipulated.

Batra and Srinivasan (1992) have reported usability studies that have addressed this question. Studies by Juhn and Naumann (1985), Mantha (1987), Jarvenpaa and Machesky (1989), Batra et al. (1990) and Batra and Antony (1994) found that the use of conceptual data models led to higher quality representations. The conceptual data model used in these experiments was generally the entity–relationship (ER) model.

Thus, empirical findings suggest three points:

(1) conceptual data modelling is unlikely to be used for enterprise-wide models;

(2) it is likely that conceptual data modelling is used for specific applications;

(3) the use of a conceptual data model (like ER) leads to better quality design.

If practitioners, therefore, feel that using the ER model for specific applications is a good idea, it is certainly supported by empirical research. Interestingly, laboratory experimenters have not considered any other data model for developing conceptual representations. There are numerous data models reported in the database literature. Among these, semantic data models have been suggested for conceptual data modelling (Peckham & Maryanski, 1988). The proposals for these models depict the perspective of concept researchers of the academic community. We explain this perspective after presenting a brief chronology of data models.

## Academic perspective: concept research

The formalisms for data modelling have been adapted from both predicate logic and linguistics, which in turn draw upon theories of knowledge that can be traced back as far as Aristotle and Leibniz (Klein & Hirschheim, 1987). The current perspective on data modelling, however, finds its roots in the late 1950s with the primitive file data model (Hoare, 1969). Figure 1 contains a graphical representation of the chronology of data modelling theory from the primitive file data model of the pre-1960s to the most recent advancements in object-oriented and semantic data models of the present day.

The primitive file models of the early 1960s were quite inflexible and possessed limited expressiveness by current standards, but nonetheless played an important role in the database implementation efforts of the period. [Flexibility refers to the ease with which a data model can adapt to complex application situations. Expressiveness refers to the ability of the model to represent the different abstractions and relationships in a complex application (Navathe, 1992).] In these models, objects were represented in records that were grouped in files. As time went on, it became increasingly apparent that the primitive file model was limited in its ability to organize large collections of data. In response to this, Bachman (1969) proposed the data structure diagram (DSD) in an attempt to capture the structure of aggregate records and the one-to-many relationships (called set-types) among the record types. While the DSD (often referred to as a Bachman diagram) was soon supplanted by the more sophisticated, flexible and expressive data models of the present era, it is still in use today.

By the 1970s, data modelling theory had begun to respond to the ever-burgeoning need for more expressive and flexible modelling approaches. The hierarchical data model was developed by IBM as part of a DBMS called Information Management System (IMS). The hierarchical model structures the data as a tree, with nodes representing record types and the links representing 'parent-child' relationships among the various record types. Simultaneous to the introduction of the hierarchical model was the extension of Bachman's (1969) DSD into the network model (CODASYL, 1971). The single-parent constraint associated with the hierarchical data model tended to force high redundancy factors and excessive structure to the database. The network model removes this constraint and thus permits as much or as little structure as desired (McFadden & Hoffer, 1994). The introduction of the relational model (Codd, 1970) was a landmark in data modelling theory and is considered the first approach to differentiate explicitly between the logical and physical data models, making it easier for novice or casual users to understand the nature of the database (Navathe, 1992). In addition, the relational model provided a mathematical basis to the discipline of data modelling couched in the notions of sets and relations (Maier, 1988). The hierarchical, network and relational models are all logical data models.

Today, the relational model is the dominant choice in database development. However, one argument against the relational model focuses on its flat structure. This flatness causes the model to represent complex relationships in awkward ways. In response to this need for a richer representation, more expressive models were introduced. These data models are called semantic data models and are reported in Peckham and Maryanski (1988) and Hull and King (1987). These models were then suggested as appropriate for conceptual data modelling.

<table><tr><td rowspan="2"></td><td>Primitive File Model</td><td>Data Structure Diagram</td><td>Hierarchical Model</td><td>Relational Model</td><td>Network Model</td><td>Entity-Relationship Model</td><td>Semantic Data Model</td><td rowspan="2">Object-Oriented</td></tr><tr><td>Pre-1960</td><td>1969</td><td>1969</td><td>1970</td><td>1971</td><td>1976</td><td>1981</td></tr></table>

Figure 1 Chronology of conceptual data modelling theory.

An important development in conceptual data modelling was the arrival of the entity–relationship model (ER) (Chen, 1976). This approach is a direct extension of the classical data models and combines the features of both the network and relational models. The translation to implementable models, like the network and relational models, is therefore straightforward. The ER model makes a distinction between objects and relationships using three basic constructs: (1) entity types; (2) relationship types; and (3) attribute types. The immediate popularity of the ER model for high-level database design stems from its economy of concepts combined with the widespread belief in entities and relationships as natural modelling concepts (Brodie, 1986).

Over the next decade, new concepts, new data models and extensions to the ER model followed. Smith and Smith (1977a, 1977b) proposed the notions of aggregation and generalisation as extensions to the semantics addressed by data models. Teorey et al. (1986) proposed the extended-ER model (EER) by adding generalisation semantics to the ER model. They also provided a better treatise of concepts such as ternary and unary relationships, and showed how an EER representation can be translated to a relational representation. Most recently, two new enhancements to the ER model have been developed: (1) the ER-R situation action model and (2) the entity retrospective transformation model (ERTM). The ER-R (Tanaka et al., 1991) provides for the inclusion of rules to the foundational ER model and the ERTM (Davydov, 1994) purports to offer a more logical and well-defined process of assigning relations than previous ER offerings.

Many other semantic data models have been proposed; none, however, have attracted as much attention as the ER model. Hammer and McLeod (1981) proposed the SDM (semantic data model), which provides a richer assortment of constructs including generalisation, derived relationships and grouping connections. The binary-relationship model (Bracchi et al., 1976; Verheijen & VanBekkum, 1982) is a restriction of the relational model in that relationships are binary rather than n-ary. The functional data model (Shipman, 1981) combines aspects of the relational model with functional programming by using objects and functions over objects as basic model building blocks. The most appealing property of this model is its attractive and simple query facility based on functional composition (Brodie, 1986).

Some additional approaches deserve mention. RM/T (Codd, 1979) is an extension of Codd's relational model. It represents relationships using associative entity types for many-many relationships and designative entity types for one-many relationships. The structural data model (Weiderhold & El-Masri, 1979) restricts relations in the relational model to five specific interpretations, and the object-role model (Bachman, 1977) extends the network model by adding the notion of role. TAXIS (Mylopoulas et al., 1980) places emphasis on generalisation abstraction. Peckham and Maryanski (1988) classify TAXIS as a semantic data model, but it also has capabilities like data encapsulation that are characteristics of object-oriented data models. Similarly, they classify SHM+ (Brodie, 1984) as a semantic data model, although it provides constructs for structure and behaviour schemes.

Despite numerous such proposals, ER is the only data model that has become popular. Other semantic data models have generally been ignored. This is evident from DBMS product surveys which indicate that most popular CASE tools are based on the ER model. There are several reasons why practitioners have ignored most semantic models. The practitioner perspective on such issues is now addressed.

## Practitioner perspective

One initial observation that can be made is the apparent degree of agreement between the two communities regarding the benefits to be derived from a rigorous data modelling approach. This is apparent from various articles (e.g. Ludovici, 1990; Martin, 1990; Kerr, 1991; Scheer & Hars, 1992; Martin, 1993) that stress conceptual data modelling and data planning.

Martin (1990, 1993) has proposed information engineering, which is a repository-based development to an entire enterprise to integrate the planning, design and construction of systems that need to interoperate across the enterprise. In other words, information engineering applies integrated modelling and design techniques to the enterprise as a whole rather than to merely one project.

Kerr (1991) presents a four-tiered methodology comprising: (1) business modelling, the first step in understanding the nature of information flow within an organization; (2) data modelling, a systematic way of building a picture of the interrelationships among a company's data; (3) process modelling, a practice used to document the way in which data are manipulated within an organization; and (4) enterprise modelling, a method for integrating previously defined data and procedure models into a consolidated whole.

Ambrosio (1992) suggests that data modelling, like getting a medical check-up, is something you know to be good for you but you cannot ever seem to quantify the benefits. She, nevertheless, posits that data modelling is becoming increasingly prevalent in organizations in response to the growing need to clean up the conflicting and redundant data formats that currently exist. This suggests one of three explanations: during the development of the theoretical underpinnings of data modelling by the academic community, the applied community was not operating in parallel by applying the theories in a practical sense; there are flaws in the theories that preclude their application by practitioners; or both.

Scheer and Hars (1992) discuss the need for development of an enterprise-wide data model and identify three different model types: (1) the macro level model which represents the concepts that are strategically important to the enterprise and that influence all major business activities; (2) the medium level model which represents the results of a detailed requirements analysis and represents the information requirements of the organization; and (3) the micro level model which is sufficiently detailed to derive database description statements automatically.

Thus, authors from the practitioner community have extolled the virtues of conceptual data modelling. Interestingly, however, there is a general lack of any substantive evidence, anecdotal or empirical, to suggest that the concepts are being widely used in the applied design environment. In addition, there exists an obvious lack of reference to the academic literature regarding whether, or to what extent, practice is embracing any of the theoretical foundations developed over the last three decades.

To understand the practitioner perspective of conceptual data modelling, let us consider how they may view this area. Organizations do not adopt new technologies, methodologies or tools unless the benefits clearly exceed the costs. Logical data modelling (e.g. relational) is attractive to organizations since the focus is on implementation and solving an immediate problem. It is difficult, however, to quantify the benefits of conceptual data modelling.

There are essentially four benefits of employing conceptual data modelling: focus on data; serving as an enterprise model; leading to greater accuracy; and serving as an effective tool for documentation. Only one – leading to greater accuracy – is tangible, assuming that the practitioner community is aware of this finding which incidentally has appeared only in the academic literature. The others are related to data planning and maintenance, and are arguably difficult to quantify.

Semantic data models, although more expressive, are unsuitable for conceptual data modelling. In fact, there is no evidence that designers are even aware of these models. Currently, almost all popular database implementations for business applications are based on the relational model. It is well known that the relational model is simple and somewhat limited in its support for real world constructs.

A semantically rich representation cannot be used at the conceptual level if, during translation to the logical representation, most of the semantics are lost. If certain semantics are captured in the conceptual representation but are then dropped from the logical representation since the logical data model is too restrictive, what is the point in capturing these semantics? For example, SDM (Hammer & McLeod, 1981) can capture semantics like interclass connections, grouping connection, inverse attributes and matching attributes; however, most of these semantics cannot be implemented by commercial DBMS. Such data models are unlikely to be adopted by industry for developing conceptual data representations.

This is not a problem with the ER representation since unequivocal translation into relational representation has been established (see Teorey et al., 1986 for example). Further, human factors studies have demonstrated that the use of the ER model, as compared with the relational, results in more accurate representations. The ER model has the potential to become the choice for conceptual data modelling since it provides a greater focus on data, supplies graphical notations that can be used for documenting, communicating and understanding data requirements of the enterprise, aids designers in developing accurate representations, and provides constructs that can be translated and implemented by the popular logical data models. Many popular front-end CASE tools (like EasyCASE, ERwin, JAM/CASE, MacAnalyst) employ the ER model.

Moore (1993) points out that the defining of conceptual and logical models is generally recognised as a key analytical method for understanding systems and arriving at improved designs. He finds that most works on the subject have given no clear guidance on how to distinguish confidently the functional or logical system from a particular physical manifestation of it. He argues that this lack of understanding of the logical model causes a natural tendency to perform the decomposition process ad nauseum. Given no clear guidance on how to proceed, the analyst continues to partition downward along arbitrary physical biases, often embodied in the existing system.

We agree with the general line of argument presented by Moore (1993), although we feel designers do understand logical models (e.g. relational model along with normalisation concepts) even if their knowledge of conceptual data modelling is questionable. Brand and Gerritsen's (1993) description of the design for the National Gallery of Art's Collection Management

System (CMS) illustrates the practical aspects of database design. They point out that their design process utilised a Bachman data structure diagram instead of the more widely accepted ER model. The rationale for this choice was the belief that analysts using the more expressive ER model often become ensnared in details that do not bear on the final design. Further, it is argued that bypassing the ERM saved time. Additionally, the authors point out that the design team purposely avoided using CASE tools because they seemed unnecessary in a project involving only three designers. They contend that avoidance of CASE tools allowed them to employ a rapid prototyping approach that greatly accelerated the design and development of the system.

However, some practitioners are critical of this approach. Moore (1993) states that the applied community truly does not understand the value of the conceptual data modelling process. He states that rapid prototyping, in particular, can encourage a viewpoint where the requirements cannot be known at all in advance but must be discovered in a sort of catharsis of automation. The life cycle is reversed into automating in order to develop requirements as a substitute for business insight and planning.

Perhaps the practitioner community views conceptual modelling as a great idea but ‘not necessary in my situation’. Assuming this attitude is not new, but is rather a continuation of the prevailing attitude of the last two decades, we may come to understand why many organizations are experiencing redundancy factors in excess of 10 (Scheer & Hars, 1992).

## Discussion

Overall, one can state that the practitioner community does not seem to have really embraced conceptual data modelling, despite its indicated benefits. The academic community too have failed in this regard since they have predominantly focused on more expressive models. Researchers have not attempted to conduct case or field studies to gauge the cost-benefits of enterprise-wide CDM. This is in contrast to logical data modelling, which addresses developing a representation that can be implemented using a database management system (DBMS) and which has been the target of considerable theoretical work by academicians (e.g. Maier, 1988) and developmental work by practitioners.

It is easy to observe that there are indeed wide differences between the academic and the practitioner focus on conceptual data modelling. Of course, one community need not be constrained by the other since each has its own goals. Nevertheless, we feel that both communities can benefit by understanding what each has to offer and appreciating each other's problems and constraints. The academic can provide theoretical knowledge and an objective approach, while the practitioner can assess this knowledge in a practical setting and provide feedback and direction for effective research.

Glass (1989, 1990) offers one approach to understanding this lack of synchronicity between academics and practitioners which can be applied to our data modelling investigation. He suggests the existence of a temporal relationship between theory and practice such that ‘informal practical thinking must precede – and then proceed in tandem with – formal formulation theory’ (Figure 2). Glass argues that while few computing theorists are former practitioners and there is little experimental practice-simulating in academic work, often the first glimmer of a new and useful idea nevertheless comes from the world of practice (‘necessity is the mother of invention’). Following this, however, he posits that the act of maturing both the practice and the theory can and should go on in tandem. Any attempt to do otherwise ‘leads inevitably to weak theory and stuck practice’. The challenge, therefore, is to bring the two communities closer.

The roots of database can be traced to the widespread adoption of file organization methods by the practitioner community. In 1970, Codd introduced the relational model, which seemed to have a sound theoretical base. The academic community extended his work and, perhaps, went overboard. Later, prototypes were developed and relational systems found their niche predominantly in mini and microcomputer systems. However, some of the practical problems encountered have led to the emergence of object-oriented systems. So, to some extent, theory and practice did intertwine in the manner suggested by Glass (1989). With respect to conceptual data modelling, practice adopted the ER model to a limited extent and stopped, but the academic literature kept going by proposing new semantic data models. Perhaps it has again swayed too far and should evaluate its research agenda.

![](/api/attachments/2PB6KHTX/fulltext/images/8814dd988a3ae305a839992ca2355292af0068367972661c00976c9aac2f6e49.jpg)  
Figure 2 Glass's temporal relationship between theory and practice.

The academics working in the area of data modelling should realise the constraints of the practitioner community. There is little room left for new data models and new methodologies. Most data models have not been empirically tested for usability. In most cases, when a new data model is proposed, the proponent rarely explains how this model can be a basis for a DBMS and how existing applications can be re-engineered. More data models, unless supported by evidence regarding their potential and applicability, can only create confusion.

Perhaps more academics should work on developing techniques that can embed the essence of theories and principles without the esoteric proofs and notations. Empirical research has demonstrated the usability of the ER model. Thus, an ER model-based technique that implants the principles of relational databases will earn far more acceptance than a relational treatise direct from Maier's The Theory of Relational Databases. Both academic and practitioner journals should encourage papers that translate theoretical ideas into practical approaches. The approaches need to be simple enough to invite exploration. One should be aware that database practitioners have many other tasks than data modelling, and are more likely to be able to find time for a simple and satisficing approach than an esoteric and optimal approach.

There is a dearth of empirical studies in this area. Empirical studies provide the link between theory and practice. Usability studies (see Batra & Srinivasan, 1992 for a survey) and field studies (e.g. Grover & Teng, 1992) have provided valuable information regarding the applicability of theory. However, there is a need for more work. For example, usability studies have typically considered student subjects as surrogates for novice designers. This provides a limited perspective that can be enriched by designing quasi-experimental investigations. Field studies should consider research questions like how enterprise data modelling is viewed in practice. Multiple case studies can provide the rich qualitative data and experience of enterprise modelling projects. These studies can also provide research questions for detailed scrutiny. Action research can be a source of research questions as well as serve as verification for the findings of studies based on other research strategies.

Practitioners, too, will need to address the problems of redundancy and ad hoc proliferation of systems. In a typical organization today, one is likely to find systems on different platforms and based on different DBMS. As mini and microcomputers have emerged, there has been a dramatic increase in the availability of DBMS. An organization may have a production system utilising a network-model-based DBMS (like IDMS) on a mainframe, and several department level systems on minicomputers and microcomputers based on relational products (like Oracle or Foxpro). Today, many of the microcomputer DBMS (like Focus) can not only access their own data, but also data residing in a different format on a minicomputer or on a mainframe. The availability of middleware and connectivity tools (like EDA/SQL) now facilitates connection across networks to relational as well as non-relational data (Finkelstein, 1995).

However, all this technology is likely to be unproductive if an enterprise-wide conceptual data model is not available. An important component of this model will be the enterprise data model. Such connectivity is of little use if one does not know what data are available and where such data can be accessed. Further, building decision support systems (DSS) and executive information systems (EIS) is unlikely to meet the desired success without organizations developing data models. Such models have to be developed carefully; they must be simple yet comprehensive, and abstract with focus on data, yet linked to implementation.

## Conclusion

We have argued that the area of conceptual data modelling is in need of urgent study from academic researchers, and enterprise-wide adoption from practitioners. Perhaps the practitioners are using CDM for specific projects. However, the real gains of CDM are likely to emerge if applied throughout the organization. Research in semantic data models is unlikely to be applied in a practical setting. Instead, empirical studies need to be conducted to assess the benefits of CDM.

In closing, we feel that the convergence of the academic and practitioner communities during the next years regarding conceptual data modelling is likely to yield productivity gains for both communities. We urge the academic researchers and practitioners to establish formal or informal partnerships to work jointly to enhance knowledge in the area of conceptual data modelling.

## References

AMBROSIO J (1992) Data modeling: tough but rewarding. Computerworld 26(46), 127.

AVISON DE and FITZGERALD G (1988) Information System Development: Methodologies, Techniques, Tools. Blackwell Scientific, Oxford.

BACHMAN CW (1969) The data structure diagrams. Data Base (Bulletin of ACM SIGFIDET) 1(12).

BACHMAN CW (1977) The role concept in data models. In Proceedings of the 3rd International Conference on Very Large Databases, Tokyo, Japan.

BATRA D and ANTONY SR (1994) Effects of data model and task characteristics on designer performance: a laboratory study. International Journal of Human-Computer Studies 41, 481–508.

BATRA D and SRINIVASAN A (1992) A review and analysis of data management environments. International Journal of Man–Machine Studies 36, 395–417.

BATRA D, HOFFER JA and BOSTROM RP (1990) Comparing representations developed using relational and EER models. Communications of the ACM February, 126–139.

BRACCHI G, PAOLINI P and PELGATTI G (1976) Binary logical associations in data modeling. In Modeling in Database Management Systems, pp. 125–148. North-Holland, Amsterdam.

BRAND EG and GERRITSEN R (1993) Database design for the National Gallery of Art. DBMS March, 50–52, 86.

BRODIE ML (1984) On the development of data models. In On Conceptual Modeling, Perspectives from Artificial Intelligence, Databases, and Programming Languages (BRODIE ML, MYLOPOULAS J and SCHMIDT JW, Eds), pp. 19–48. Springer-Verlag, New York.

BRODIE ML (1986) On the development of data models. In On Conceptual Modeling (BRODIE ML, MYLOPOULAS J and SCHMIDT JW, Eds), pp. 19–47. Springer-Verlag, New York.

BUBENKO JA (1986) Information system methodologies – a research view. In Information System Design Methodologies: Improving the Practice (OLLE TW, SOL HG and VERRUN-STUART AA, Eds), pp. 289–318. North-Holland, Amsterdam.

CHEN PPS (1976) The entity–relationship model: towards a unified view of data. ACM Transactions on Database Systems 1(1), 9–36.

CODASYL, (1971) Report of the CODASYL Data Base Task Group, April. ACM, New York.

CODD EF (1970) A relational model for large shared data banks. Communications of the ACM 13(6), 370–387.

CODD EF (1979) Extending the database relational model to capture more meaning. ACM Transactions on Database Systems 4(4), December, 397–434.

DAVIS AM (1993) Software Requirements. Prentice-Hall, Englewood Cliffs, New Jersey.

DAVYDOV MM (1994) From model to database. Database Programming & Design March, 46–52.

DESchmedt WH (1994) The wolf at the door. Database Programming & Design April, 58–67.

FINKELSTEIN R (1995) The new middleware. DBMS 8(2), February, 50–58.

GIORDANO R (1993) The information 'where?' house. Database Programming & Design September, 54–61.

GLASS RL (1989) The temporal relationship between theory and practice. Journal of Systems and Software 10, 65–67.

GLASS RL (1990) Theory versus practice – revisited. Journal of Systems and Software 12, 81–82.

GRIETHUYSEN JJ (Ed.) (1983) Concepts and Terminology for the Conceptual Schema, ISO/TC97/SC5-N695. International Organization for Standardization, Geneva, Switzerland.

GROVER V and TENG JTC (1992) An examination of DBMS adoption and success in American organizations. Information & Management 23(5), 239–248.

HAMMER M and McLEOD D (1981) Database description with SDM: a semantic database model. ACM Transactions on Database Systems 6(3), 351–386.

HOARE CAR (1969) An axiomatic basis for computer programming. Communications of the ACM 12(11), 576–580, 583.

HULL R and KING R (1987) Semantic database modeling: survey, applications, and research issues. ACM Computing Surveys 19(3), September, 201–260.

## About the authors

Dinesh Batra is Associate Professor in the Department of Decision Sciences and Information Systems at Florida International University. He received his PhD from Indiana University. His research has been published in Management Science, Communications of the ACM, European Journal

JARVENPAA SL and MACHESKY JJ (1989) Data analysis and learning: an experimental study of data modelling tools. International Journal of Man–Machine Studies 31, 367–391.

JUHN S and NAUMANN JD (1985) The effectiveness of data representation characteristics on user validation. Presented at the Sixth International Conference on Information Systems, Indianapolis, Indiana.

KERR JM (1991) The IRM Imperative: Strategies for Managing Information Resources. Wiley, New York.

KLEIN HK and HIRSCHHEIM RA (1987) A comparative framework of data modeling paradigms and approaches. Computer Journal 30(1), 8–15.

LUDOVICI J (1990) Conquering the relational database. Data Training December, 22–30.

MAIER D (1988) The Theory of Relational Databases. Computer Science Press, Rockville, Maryland.

MANTHA RW (1987) Data flow and data structure modeling for database requirements determination: a comparative study. MIS Quarterly 11(4), 531–546.

MARTIN J (1990) Information Engineering. Prentice-Hall, Englewood Cliffs, New Jersey.

MARTIN J (1993) Principles of Object Oriented Analysis and Design. Prentice-Hall, Englewood Cliffs, New Jersey.

McFADDEN FR and HOFFER JA (1994) Database Management, 3rd edn. Benjamin/Cummings, Redwood City, California.

MOORE AG (1993) Essential systems analysis: basic principles for evaluating and orienting the field of information engineering. Journal of Systems Management December, 34–37.

MYLOPOULAS J, BERNSTEIN PA and WONG HKT (1980) A language facility for designing database intensive applications. ACM Transactions of Database Systems 5(2), June, 185–207.

NAVATHE SB (1992) Evolution of data modeling for databases. Communications of the ACM 35(9), 112–123.

PALVIA P and NOSEK JT (1993) A field examination of system life cycle techniques and methodologies. Information & Management 25(2), 73–84.

PECKHAM J and MARYANSKI F (1988) Semantic data model. ACM Computing Surveys 20(3), 153–189.

SCHEER A-W and HARS A (1992) Extending data modeling to cover the whole enterprise. Communications of the ACM 35(9), 166–171.

SHIPMAN D (1981) The functional data model and the data language DAPLEX. ACM Transactions on Database Systems 6(1), 140–173.

SMITH J and SMITH D (1977a) Database abstractions: aggregation and generalization. ACM Transactions on Database Systems 2(2), 105–133.

SMITH J and SMITH D (1977b) Database abstraction: aggregation. Communications of the ACM 20(6), 405–413.

TANAKA A, NAVATHE SB, CHAKRAVARTHY S and KARLAPALEM S (1991) ER-R, an enhanced ER model with situation-action rules to capture application semantics. In Proceedings of Tenth International Conference on Entity-Relationship Approach, San Mateo, California.

TEOREY TJ, YANG D and FRY JP (1986) A logical design methodology for relational databases using the extended entity-relationship model. ACM Computing Surveys 18(2), 197–222.

VERHEIJEN G and VANBEKKUM J (1982) NIAM: an information analysis method. In Information Systems Design Methodologies: A Comparative Review (OTTE T, SOL H and VERRIJN-STUART A, Eds). North-Holland, Amsterdam.

WEIDERHOLD G and EL-MASRI R (1979) The structural model for database design. In Proceedings of the International Conference on the Entity-Relationship Approach to Systems Analysis and Design, Los Angeles, California, December.

of Information Systems, International Journal of Human-Computer Interaction, Information and Management, Journal of Database Management, and elsewhere. His research interests focus on database management and human-computer interaction.

George M. Marakas has recently completed his doctoral degree in MIS at Florida International University and has been appointed to the faculty at University of Maryland at College Park. His research interests include requirement analysis, impression management and organizational consequences of IS. His work has appeared in Management Science, several national conference proceedings as well as two edited volumes.
