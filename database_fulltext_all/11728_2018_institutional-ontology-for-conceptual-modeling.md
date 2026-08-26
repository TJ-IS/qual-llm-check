---
otero_id: 11728
otero_key: "N2X2B8HD"
title: "Institutional ontology for Conceptual Modeling"
authors: "Owen Eriksson; Paul Johannesson; Maria Bergholtz"
year: "2018"
journal: "Journal of Information Technology"
doi: "10.1057/s41265-018-0053-2"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research Article

# Institutional ontology for conceptual modeling

Owen Eriksson<sup>1</sup>, Paul Johannesson<sup>2</sup>, Maria Bergholtz<sup>2</sup>

<sup>1</sup>Department of Informatics and Media, Uppsla University, Postbox 513, 751 20 Uppsala, Sweden;

<sup>2</sup>Department of Computer and Systems Sciences, DSV, Stockholm University, Postbox 7003, 164 07 Kista, Sweden

Correspondence:

O Eriksson, Department of Informatics and Media, Uppsla University, Postbox 513, 751 20 Uppsala, Sweden. Tel: +46 18 471 1010;

E-mail: owen.eriksson@im.uu.se

## Abstract

Conceptual models are intended to capture knowledge about the world. Hence, the design of conceptual models could be informed by theories about what entities exist in the world and how they are constituted. Further, a common assumption within the field of conceptual modeling is that conceptual models and information systems describe entities in the real world, outside the systems. An alternative view is provided by an ontological commitment that recognizes that the institutional world is constructed through language use and the creation of institutional facts. Such an ontological commitment implies that there is an institutional reality, which, to a great extent, is constructed using information infrastructures. Accordingly, conceptual models have not only a descriptive role but also a prescriptive one, meaning that modelers set up a framework of rules that restrict and enable people to construct institutional reality using information infrastructures. Understanding the prescriptive role of conceptual models may revive the area of conceptual modeling in the information systems research community. Reviving conceptual modeling through institutional modeling is motivated by the effect that implemented conceptual models have on information infrastructures and institutions. The purpose of this article is to propose an institutional ontology that can support the design of information infrastructures. The ontology is theoretically informed by institutional theory and a communicative perspective on information systems design, as well as being empirically based on several case studies. It is illustrated using a case study in the welfare sector. A number of guidelines for modeling institutional reality are also proposed. Journal of Information Technology (2018). https://doi.org/10.1057/s41265-018-0053-2

Keywords: ontology; conceptual modeling; institution

## Introduction

C <sup>onceptual</sup> <sup>models</sup> <sup>are</sup> <sup>intended</sup> <sup>to</sup> <sup>capture</sup> <sup>knowledge</sup>about domains of reality, which means that conceptual about domains of reality, which means that conceptual models, as well as modeling constructs, should be based on theories about the world (Wand et al., 1999). Using ontology as a foundation for conceptual modeling builds on the assumption that ontology can help to better understand how the world is constituted (Gruber, 1995; Wand et al., 1999; Wand and Weber, 2006). In philosophy, ontology is defined as the study of being, of what there is (Bricker, 2016). Ontology investigates what entities exist, or can exist, as well as how these entities can be classified, related within hierarchies and taxonomies, and separated according to their characteristics. These kinds of investigations are also performed by conceptual modelers in their modeling efforts, suggesting that ontology can provide valuable support for conceptual modeling.

A fundamental question in conceptual modeling is the one stated by Wand and Weber (2002), who asked ‘‘How can we model the world to better facilitate our developing, implementing, using, and maintaining more valuable information systems?’’ This question has been addressed in the research literature using a variety of approaches and research methods, including languages for conceptual modeling (e.g., Bubenko, 2007; Halpin, 2007), methods for conceptual modeling (e.g., Bera et al., 2010; March and Allen, 2014), model evaluation (e.g., Milton et al., 2012; Shanks et al.,

2003), and ontological analysis of conceptual modeling (e.g., Wand et al., 1999). A first step toward answering this question is to investigate how the notion of ‘‘the world’’ can be conceived, and how the world relates to information systems.

A common assumption within the field of conceptual modeling has been that an information system stores representations of states of affairs in the real world, outside the system (Date, 2003; Evermann and Wand, 2005; Jacobson et al., 1994). Wand and Wang (1996, p. 88) capture this view succinctly in their ‘‘representation assumption,’’ which states that ‘‘an information system is a representation of a realworld system as perceived by users.’’ In the most influential ontology in the information systems literature, the Bunge– Wand–Weber (BWW) ontology, Postulate 1 states that ‘‘The world is made of things that possess properties’’ (Wand et al., 1999, p. 497). In contrast to these views, our experience, based on a number of case studies, is that conceptual modeling is concerned primarily with institutional reality, which aligns with suggestions made by Bergholtz and Eriksson (2015), March and Allen (2014), and Beynon-Davies (2016). Institutional reality is created and maintained by social interaction governed by rules; it is about human activities, as well as the relationships and facts that are created through these activities. Accordingly, an ontological commitment (Bricker, 2016) that recognizes the idea that the institutional reality is constructed through social interaction and language use would provide an alternative view to that of the representation assumption (Burton-Jones et al., 2017). Such an ontological commitment implies that there is an institutional reality, which today, to a great extent, exists within implemented information systems and is made accessible through their interfaces.

Physical things exist independently of rules, social interaction, language, and humans. They are observer-indepen dent, and people use language only for communicating about them, not for creating them. In contrast, institutional facts are facts that are observer-relative and require rules and language to exist, such as marriages, clients, companies, money, insurance, and so on (Searle, 2006). It should be noted that Searle uses the term ‘‘fact’’ to refer to entities of the world rather than to claims about those (Elder-Vass, 2012). For example, if a bank declares that a personal account exists and assigns a customer as the account holder, this speech act (Searle, 1969) creates an institutional fact. Thus, language can be used to create institutional reality, not only to describe it, and rules are the means that enable us to do this (Searle, 2006).

Accordingly, in institutional contexts, conceptual model ing becomes a design activity, in which modelers establish a framework of rules that enable people to construct institutional reality. This reality is about observer-relative institutional facts as well as the rules and structures that make them legitimate, meaning that a conceptual model is not just a description of a preexisting reality. In addition, the model represents prescriptive rules that different actors can use to construct, reconstruct, or criticize how the institutional reality has been created or how it ought to be created. Designing such models can be supported by an ontology that acknowledges the social construction of reality, which is particularly important in the context of information infrastructures, that is, interoperating information systems that are used across time and space, as well as across organizational boundaries (Bowker and Star, 1999; Hanseth and Lyytinen, 2010; Star and Ruhleder, 1996).

To summarize, ontological differences between the material and institutional worlds need to be recognized and further investigated in conceptual modeling. In particular, ontologies for conceptual modeling should support the distinction between brute facts, that is, physical things and their properties, on the one hand, and institutional facts on the other hand (Searle, 1995, 2006). Moreover, conceptual models can address different material and institutional worlds, and they can have different descriptive as well as prescriptive roles, as listed in Table 1.

Although, so far, ontologies and methods for conceptual modeling have focused mainly on the descriptive role of conceptual models, there is room for ontologies that take into account their prescriptive role in institutional domains, which is represented by moving to the upper-right quadrant in Table 1. This will assist in designing conceptual models that are relevant for analyzing and designing information infrastructures. Conceptual modeling is considered to be at the core of the information systems discipline (Weber, 2003). However, today, it is recognized (Wand and Weber, 2017) that there are few scholars in the field of information systems who work on the topic of conceptual modeling; it is often considered a technology-related activity that belongs to the domain of software engineering. However, conceptual modeling is critical for designing institutional reality, as conceptual models have a prescriptive role in its constitution. Realizing and obtaining acceptance of the importance of conceptual modeling in institutional design may revive this area in the information systems research community. As a contribution to this revival, the purpose of this article is to propose an ontology for institutional reality that can help to answer the following research question:

How can we model institutional reality, taking into account the prescriptive role of conceptual models, thereby supporting the design of more valuable information infrastructures?

Table 1 Descriptive versus prescriptive roles of conceptual models in different worlds

<table><tr><td></td><td>Material reality</td><td>Institutional reality</td></tr><tr><td>Prescriptive role</td><td>Model prescribes how material reality may be changed</td><td>Model prescribes how institutional reality ought to be constructed or reconstructed</td></tr><tr><td>Descriptive role</td><td>Model describes how material reality is</td><td>Model describes how institutional reality is</td></tr></table>

The article is organized as follows: ‘‘Related work’’ section elaborates on the notion of institutions and information infrastructures. The research method used for developing and evaluating the proposed institutional ontology is discussed in ‘‘Research setting’’ section. In ‘‘The institutional ontology section, the ontology is presented and illustrated using income support in the welfare sector as a case study. In ‘‘Modeling guidelines’’ section, we report a number of practical problems arising from the case study, which illustrate generic modeling problems, and we use the ontology from ‘‘The institutional ontology’’ section to propose a number of guidelines to solve these problems. ‘‘Discussion and conclusions’’ section summarizes the research contribution and discusses practical and theoretical implications and suggests future research directions.

## Related work

## Institutional theory

Institutional theory, particularly neo-institutionalism, is one of the most important theoretical perspectives in management and organizational research (Cornelissen et al., 2015). Since the 1960s, recognition of the role of institutions has led to a stream of research that continues to grow (Barley and Tolbert, 1997; Berger and Luckmann, 1966; Cornelissen et al., 2015; Powell and DiMaggio, 1991; Schutz, 1967; Scott, 2001, Searle, 1995). According to Scott (2001), an institution is a social structure that offers organizations or individuals lines of action, while, at the same time, controlling and constraining them. In doing this, institutions not only regulate actions but also enable new kinds of actions and relationships (Habermas, 1985).

From an ontological perspective, institutions have been defined as ‘‘systems of established and prevalent social rules that structure social interactions’’ (Hodgson, 2006). Institutional theory extends this definition by viewing institutions as regulative, normative, and cultural–cognitive structures, also called institutional pillars, that, together with human activities, provide stability and meaning to social life (Scott, 2003). Such institutional structures form a continuum from the formal to the informal. Although, typically, rule systems are highly formal, normative and cultural structures are more informal in nature (Scott, 2001, 2003).

In the following, we focus on the formal aspects of institutions, particularly designed formal rule systems. There are two reasons for this restriction. First, to be processed by computers, rules need to be expressed in a more formal and explicit way than they do in manual systems (Hirschheim et al., 1996). Second, in the context of information infrastructures, rules need to be formal so that they can be understood and communicated across organizational borders. In particular, formal classification systems attempt to regularize and provide a means of sharing information across time and space (Bowker and Star, 1999). Nevertheless, a development-oriented institutional perspective also needs to acknowledge the importance of the informal (Casson et al., 2010, p. 137). Informal structures, such as normative and cultural-cognitive structures, shape formal ones through information systems design and the institutional processes that they establish, as illustrated in ‘‘The reproduction of institutional structures through information infrastructures’’ section.

## Constructing the institutional reality

Work on neo-institutional theory has often had a cognitive focus, exploring how shared categories, schemas, mental models, logics, or scripts constitute the legitimate ways of acting in institutional settings (Cornelissen et al., 2015). However, such a cognitive focus can come at the expense of a more social perspective, and therefore, there is a need to include communication in institutional theory (Cornelissen et al., 2015). In line with a communicative view on institutions, Searle (1995, 2005, 2010) has investigated how institutional reality is constructed by means of communication acts (speech acts).

Searle acknowledges that there is a material world that exists independently of human beings and their beliefs and asks ‘‘how can we account for social facts within that ontology?’’ (Searle, 1995, p. 7). This question can be answered partially by the fact that humans have a capacity for collective intentionality, which enables them to share intentions (Searle, 2005). Through collective intentionality, they are able to assign functions to things. Some functions of things depend solely on their physical properties; for example, the ability of a screwdriver to turn screws depends on its physical structure. Other functions are more abstract and have little to do with the physical properties of the tool or medium that mediates the functions. Searle refers to such functions as status functions. For example, people can assign the function of being money to a digital object, which counts as a bank account within an institutional bank context. Through that bank account, a bank and a customer are interrelated and thereby possess different claims on and duties toward each other. For example, the bank is obliged to pay a certain interest rate and the customer can make deposits and claim revenue, based on the account balance. The bank account performs the status function of being money not by virtue of its physical structure, but by virtue of its collective acceptance. According to Searle (2006), status functions mark the difference between material and institutional realities. Furthermore, as institutional facts cannot exist without the use of language, communication is constitutive for institutional reality.

## Institutional theory and information systems research

In the past decade, the information systems discipline has exhibited a growing interest in institutional theory (Powell and DiMaggio, 1991; Scott, 2001). Many studies have used institutional theory to interpret and analyze data, but only initial attempts have been made to extend the theoretical understanding of institutions in information systems research (Bergholtz and Eriksson, 2015; Beynon-Davies, 2016; Eriksson and Agerfalk, 2010).

Mignerat and Rivard (2009) and DeVaujany et al. (2014) conduct literature reviews investigating how institutions have been studied and conceptualized in the information systems literature. They conclude that studies at the organizational level dominate the literature, whereas only a few studies pertain to the interorganizational and societal levels. Further, existing information systems research highlights conversion, that is, how rules and norms may become embedded in information technology (IT) artifacts (Berente and Yoo, 2012; Gosain, 2004; Orlikowski and Iacono, 2001; Pishdad et al., 2014; Stamper, 2001), but only initial attempts have been made to clarify how institutional reality is created using IT artifacts (Bergholtz and Eriksson, 2015; Beynon-Davies, 2016; Eriksson and Agerfalk, 2010; March and Allen, 2014).

## Information systems infrastructures and institutions

Based on a recent literature review, Boell and Cecez-Kecmanovic (2015) conclude that, currently, all definitions of IT artifacts that they identify in information systems research are grounded in an ontological position that separates technology and social actors. Such a view was plausible before the digital era of the Internet, mobile technologies, and the digitization of products. However, today, their separate existence has become increasingly difficult to defend, leading Boell and Cecez-Kecmanovic (2015) to suggest a view of IT artifacts that goes beyond such an ontological position.

In line with the criticism of Boell and Cecez-Kecmanovic (2015), we suggest a conceptualization of IT artifacts that is relevant for the emerging practical problems we have encountered in a number of case studies (see ‘‘Data sets’’ section). We maintain that, in an institutional context, the conceptualization of IT artifacts as information infrastructures is applicable, as information infrastructures are considered part of reality, not just representations of it. Hanseth and Lyytinen (2010, p. 5) define an information infrastructure as ‘‘a shared, open (and unbounded), heterogeneous and evolving socio-technical system (which we call installed base) consisting of a set of IT capabilities and their user, operations and design communities.’’ Such a conceptualization is based on the assumption that users, designers, technologies, information, data, and social interaction are mutually co-constituting. Accordingly, the social interaction is both enabled and constrained by the installed base (Hanseth and Lyytinen, 2010). To understand the institutional character of information infrastructures, their underlying institutions need to be taken into account – particularly the systems of rules on which they are based.

## Research setting

The ontology presented in the next section has been developed over a period of 5 years. Empirically, it is grounded in the study of a number of information infrastructures. The research approach is interpretative and qualitative (Patton, 1990) with the hermeneutical circle as its methodological foundation (Mantere and Ketokivi, 2013).

## Data sets

The proposed ontology is based on a purposeful sampling of case studies (Patton, 1990). Purposeful sampling means that findings are based on the selection of information-rich cases suitable for in-depth study, in contrast to probability sampling, which depends on the selection of a random and statistically representative sample. Accordingly, the ontology is based on primary data from a rich data set of longitudinal case studies that have been performed from 1996 until now; Table 2 provides details.

One of the authors of this article was a researcher in case studies 1–4 and participated in study 5 as a designer of the infrastructure. The kind of purposive sampling that we have used is a combination of typical and intensity sampling (Patton, 1990). It picks out rich contexts, keeping in mind that the purpose of typical sampling is to illustrate what is typical in certain contexts, not to make generalizations regardless of context (Patton, 1990). Using intensity sampling means that the researchers seek comprehensive and information-rich cases that manifest the phenomena of interest in an intense way. In addition to the primary data set, we have used a secondary data set, which is also based on typical sampling. Design patterns and problems from the mainstream modeling literature have been selected (e.g., Geerts and McCarthy, 2006; Halpin, 2016; Henderson-Sellers et al., 2013; Hruby, 2010; Shanks and Weber, 2012; Steimann, 2000a; Vieu et al., 2008; Wieringa et al., 1995; Wand et al., 1999). Using such typical problems and patterns as a secondary data set is an established method in the conceptual modeling literature. Both the primary and secondary data sets have been used to confirm and disconfirm our solutions (Patton, 1990) using new cases. In this way, over time, we have tested the viability of the constructs included in the ontology.

## Data analysis

Through conceptual analysis, the phenomena encountered in the case studies have been decomposed, explained, and reconstructed. In accordance with (Beaney, 2016), our analysis is not only about breaking down phenomena; it also involves interpreting and transforming phenomena, as well as identifying fundamental principles for explaining them. Thus, we have been able to identify the modeling constructs needed for representing and interpreting the phenomena in a way that recognizes the role of institutions in social interaction.

Table 2 Primary data sets

<table><tr><td>Study</td><td>Period</td><td>Publications</td></tr><tr><td>1. A sales support system used by car dealers that constituted a part of the information infrastructure and the interoperation between Volvo and its retailers in Sweden</td><td>1996–2000</td><td>(Eriksson, 2000)</td></tr><tr><td>2. A national information infrastructure used at the Swedish Road Administration to provide traffic information services to drivers</td><td>2001–2015</td><td>(Lindgren et al., 2015)</td></tr><tr><td>3. A national student registry system, used at all of Sweden’s 38 universities, which is a part of the university information infrastructure</td><td>2006–2014</td><td>(Eriksson, 2015b)</td></tr><tr><td>4. A national information infrastructure used for e-prescribing in Sweden, which is used by all prescribers and pharmacies</td><td>2014–2015</td><td>(Eriksson, 2015a)</td></tr><tr><td>5. An ongoing action research design study of a national information infrastructure used in the social welfare sector in Sweden</td><td>2009–</td><td>(Eriksson and Goldkuhl, 2015)</td></tr></table>

In the process of analyzing the findings of the case studies, we found that each of them had a focus on one, or a few, significant institutional constructs. For example, in the first case study (the sales support system at Volvo), the ‘‘purchase object’’ was the significant institutional construct referred to during the entire sales process. Such a purchase object can be created without the existence of a physical car, which will be built only after the customer has ordered it. The purchase object regulates the construction and delivery of the physical car, and it is real in the sense that it has consequences for social interaction, not because it has mass and extension in space. This distinction is significant for conceptual modeling because it illustrates a recurrent situation in the case studies, in which the focus is on the institutional entities, not the physical ones.

The analysis started with our preunderstanding of how information infrastructures are designed and used. Thus, we already had knowledge about the case studies, which served as the starting point for our ‘‘dialogue with the data’ (Gadamer, 1975). Consequently, our preunderstanding has been used to interpret data, but it has also continually been called into question, as we have remained open to being challenged by the data (Alvesson and Ka¨rreman, 2007). Thus, we have not only used the data from our primary data set to confirm the ontology, but also continuously questioned and revised it, based on what the rich data set has told us. The secondary data set has been used to compare solutions found in the case studies with generic modeling problems, and we have suggested novel solutions, based on the proposed institutional ontology. Maintaining this kind of reciprocity is a central concern because, if the researcher does not remain open to being ‘‘surprised by the data,’’ reasoning deteriorates from disciplined analysis to ‘‘fitting the data to illustrate theory’’ (Wodak, 2004).

## The institutional ontology

This section introduces the institutional ontology. In this context, an institution is defined as a system of rules expressed in a language, which are upheld through collective intentionality, for example, regulations issued by a state, or standards and rule systems issued by corporations or collectives. The constructs of the institutional ontology reside at three levels, which are shown in the UML class diagram of Figure 1 and summarized below:

• The top level is the institutional level, which expresses what is possible, allowed, or required, including regulative and language rules, kinds of rights, institutional functions, and institutional arrangements.

• The middle level is the institutional facts level, consisting of institutional processes, institutional actions, institutional relationships, institutional function assignments, and institutional entities.

• The bottom level is the material level, which consists of material phenomena, including human beings, physical entities, and physical actions.

At the middle level, institutional processes are carried out, thereby creating new institutional entities and assigning rights to these. These creations and assignments are enabled and governed by the rules of the top level. Furthermore, the institutional processes are realized by means of physical actions carried out by human beings and physical entities at the bottom level. To illustrate the elements of the ontology, we use the income support case, introduced in ‘‘Institutional processes and the case study’’ section, as a running example.

## Institutional processes and the case study

An institutional process consists of a sequence of institutional actions. Institutional actions are always grounded in physical actions, that is, they are performed through tangible activities such as pressing keys on a keyboard. In the case of communications for which paper or digital media are used, institutional actions always leave a media trace, that is, there is a record of them (Bach, 2003).

The institutional process in the income support case study can be described as follows. An applicant can apply to the social welfare department in a municipality for income support for a household. The application can be submitted in different ways: in person, by phone, or in writing. Further, some municipalities provide an online application form that can be filled in and signed, sometimes by two applicants. The institutional process starts when the application has been received by the municipality and consists of the following actions:

(a) The first action is to open or reopen a digital case file that already exists.

(b) The second action is to constitute a new household or identify a preexisting one, as households are the only entities that can be granted income support. A household is made up of one or more clients of the social welfare department. Through the second action, it is acknowledged that a household and a household relationship exist. The relationship implies that the household has a duty to the municipality to support itself, but it can still have a legitimate claim toward the municipality for income support.

(c) The third action is to investigate the social situation of the household, which involves scrutinizing the information about the employment situation, income, costs, and assets of the clients in the household.

(d) The fourth action is to perform a calculation in which the costs of the household are deducted from its income and assets, to decide whether the household should be granted income support and what amount, if so. This granted income support should be regarded as a contract that obligates the municipality to pay an amount of money to cover household costs for the next month. In return, the household has a duty to use the amount granted to cover the costs for which it has claimed support.

(e) The fifth action is to send the decision to one of the clients in the household.

![](/api/attachments/N2X2B8HD/fulltext/images/8c2105723aff82a6792cbc6ab9d660472a3bc71eef6b38fd21b656fe774ff8e9.jpg)  
Figure 1 Institutional ontology.

Such an institutional process is performed by human beings and physical entities, for example, computers, which can perform physical actions. However, human beings and physical entities must be authorized and identified as institutional entities (see below) to perform institutional actions, so physical capability alone is not sufficient for performing institutional actions.

## Institutional entities and rights

An institutional entity is a conceptual object that represents rights. An institutional entity has the following characteristics:

• it is created using an institutional language at a certain point in time;

• it is created with some kind of media and thus has a physical representation, that is, a media trace;

• it conveys a meaning;

• it has an identity; and

• it represents rights.

## Kinds of rights

The notion of a right can be clarified using the work of Hohfeld (1913), who suggested a classification that distinguished four kinds of right types. (Three of these are employed in this article.) We use the term ‘‘right’’ instead of Searle’s ‘‘deontic powers’’ and base its definition on Hohfeld’s classification, which is explicit and more granular than that of Searle. For example, it includes categories such as claim and duty as well as powers and privileges.

• Privilege An institutional entity has the privilege of performing an action if he/she is free to carry out that action in accordance with the rules of an institution. For example, an applicant has the privilege of applying for income support according to the rules of the Swedish Social Service Act (Socialtjanstlagen) (SFS, 2001: 453 n.d.).

• Claim and duty An institutional entity has a claim on another institutional entity if the second entity is required to act in a certain way for the benefit of the first entity. Conversely, the second entity is said to have a duty to the first one. An example is a household that has the duty to be self-sufficient in relation to a municipality, but can still claim income support if its income does not guarantee a reasonable standard of living according to the Swedish Social Service Act (SFS, 2001: 453 n.d.) and the Swedish National Standard of Expenditure (NSOE, 2013 n.d.).

• Power A power is the ability of an institutional entity to create or modify claims, duties, privileges, or powers. An example is a social welfare department, which has the power to grant income support.

## Kinds of institutional entities

As a large variety of institutional entities exists, it is helpful to identify and structure various kinds of institutional entities into a taxonomy. The taxonomy suggested here is based on the kinds of rights that the institutional entities may possess, as well as on their type of grounding (Masolo, 2011). Grounding is a relationship among entities that expresses existential dependencies between them.

A distinction can be made between physical and institutional grounding. Physical grounding means that an institutional entity needs to be associated with a physical entity to come into existence, for example, a human being or a piece of paper. However, sometimes there is no such need, such as in the case of a juridical person, which could come into existence without there being a physical thing or human being that grounds it (Searle, 2005, p. 16). Institutional grounding means that an institutional entity needs to be associated with another institutional entity to come into existence.

For all types of rights, a distinction can be drawn between legal and nonlegal rights. A legal right is a right that is acknowledged by a state, and it can be a basis for official sanctions from that state. A nonlegal right is a right that is acknowledged by a state or some other authority but cannot be a basis for official sanctions from the state. At the middle level of the ontology, see Figure 1, three kinds of institutional entities can be identified: institutional subjects, institutional things, and institutional contracts.

• An institutional subject is an institutional entity that can have duties. There are four kinds of institutional subjects:

• An institutional person is an institutional subject, physically grounded in a single human being or institutionally grounded in another institutional person. An example of an institutional person is a client. We use the term ‘‘institutional person’’ instead of just ‘‘person, as the latter is often conflated with a physical human being. An institutional person can have legal as well as nonlegal rights.

• An institutional group is an institutional subject physically grounded in one or more human beings or institutionally grounded in one or more institutional persons. An example of an institutional group is a household, which is institutionally grounded in one or several clients. In contrast to an institutional person, an institutional group can only have nonlegal rights.

• A juridical person is an institutional subject that, in contrast to a person or institutional group, is not physically grounded in a human being and can only have legal rights. For example, a municipality is a juridical person that is legally responsible for decisions made, such as a decision regarding the granting of income support.

• An organizational person is an institutional subject that, like a juridical person, is not physically grounded in a human being but can only have nonlegal rights. For example, a social service department is an organizational person with the power to grant income support to a household, but it is not legally responsible for the decisions made.

• An institutional thing is an institutional entity that cannot have duties and is physically grounded in a physical entity or institutionally grounded in another institutional thing.

For example, a vehicle that can be sold to provide an income to a household is an institutional thing.

• An institutional contract is an institutional entity that cannot have rights but can only bestow (mediate) rights between institutional subjects and institutional things. For example, the granted income support by the social service department to a household and its constituent clients is an institutional contract.

## Institutional relationships

Institutional entities do not exist in isolation but are related to each other through institutional relationships. An institutional relationship is a relationship between a number of institutional entities, two of which are institutional subjects, and at least one of which does not exist before the creation of the relationship. This new institutional entity is said to be constituted by the institutional relationship.

The basic institutional relationship in the income support case is the one between a municipality and a household, as the household is the only institutional entity that can be granted income support. This relationship is based on another relationship, the one between a municipality and a client, where households are composed of clients who live at the same address. The social welfare department is the institutional subject that maintains the relationships.

Within an institutional relationship, the participating institutional entities can further extend and deepen their interactions. This is done by creating institutional contracts that establish additional rights between the subjects of the institutional relationship. An example is a household relationship, which constitutes a new institutional entity, namely a household. Within the context of this relationship, the municipality can create additional institutional contracts, for example, concerning income support.

## Rules and institutional functions

Institutions precede institutional entities in the sense that institutional entities can only be created and regulated if there are institutions for doing so. There must also be someone who explicitly defines and upholds the institution, that is, there must be an institutional subject, for example, a state, a municipality, an organization, or an association, that maintains language rules and regulative rules as well as institutional functions and arrangements.

## Institutional functions and arrangements

To specify which rules should apply to an institutional entity, the notion of an institutional function is introduced, which Searle refers to as a status function (see ‘‘Constructing the institutional reality’’ section). Institutional functions are similar to roles, as they are used for defining bundles of rights that can be bestowed on institutional entities. They are referred to in regulative rules, for example, in the Social Service Act (SFS, 2001: 453 n.d.), and defined by language rules (e.g., SOSFS, 2013: 1 n.d.). Examples of institutional functions are the household function, the household member function (which could be subdivided into adult and child), and the client function.

Institutional functions do not appear in isolation but always in networks, because their meanings are dependent on each other. A set of interdependent institutional functions is called an institutional arrangement. For example, to understand the household and household member institutional functions, it is necessary to understand how the rights of adults and children are interrelated with each other in a household. These interrelationships are represented by means of an institutional arrangement that prescribes that the adults have a duty to support the children of the household. The children of the household have no obligation to support themselves or the other household members, but they do have a duty to help support the household.

## Regulative rules

A regulative rule expresses a relationship between a kind of right, a kind of action, and two or more institutional functions. An example is the regulative rule of the Social Service Act, Chapter 4, Section 1 (SFS, 2001: 453 n.d.), which can be formulated as the following rule: ‘‘A municipality has the duty to provide income support to a household.’’ The institutional functions included are the municipality, income support, and the household. The kind of right involved is a duty, and the kind of action involved is to provide. As illustrated by this example, a regulative rule is always associated with several institutional functions, and an institutional function can appear in several regulative rules.

## Institutional function assignments

As a regulative rule refers to institutional functions, it does not directly express rights between institutional entities. However, if the institutional functions in a rule are assigned to institutional entities, that is, if each institutional function in the rule is replaced by an institutional entity, the rule will result in a right between these entities. Assigning an institutional function to an institutional entity means that the latter receives a number of rights, as given by the regulative rules to which the institutional function is related. For example, the rule above could result in the right: ‘‘The municipality identified by organization number 212000-0829 has the duty to provide income support to the household identified by household ID 92882.’’ In this example, the result expresses a right, involving a municipality and a household, which regulates their interactions. In the institutional ontology, institutional function assignments are used to assign institutional functions to institutional entities.

## Language rules

The assignments of institutional functions are governed by language rules, which enable people to constitute and identify institutional entities. There are three kinds of language rules: application rules, instantiation rules, and identification rules.

• An application rule is a definition of an institutional function. Examples of application rules are the definitions of a household, household members, and clients. The definition of a household is ‘‘a unity for the sustainment of one or several household members living together.’’ An adult is defined as a ‘‘household member over 18 years of age and not enrolled in high school education,’’ whereas a child is defined as a ‘‘household member who is less than 18 years old, or is between 18 and 21 and still enrolled in high school education.’’ Clients are ‘‘human beings who have a duty to cooperate with the municipality and are acknowledged as such after a meeting with a social welfare officer.’’

• An instantiation rule defines how institutional entities are created. The creation of an institutional entity involves the assignment of an identifier. An instantiation rule consists of a process description that specifies a number of institutional actions and their logic, as well as an identifier (cf. Eriksson and Agerfalk, 2010). For example, to create a client, the social welfare officer must ensure that the identifier refers to a unique client. The instantiation rule for a client further specifies that, to register the entity, the social welfare officer must provide a name as well as an address, PID number, or European Union (EU) or EEA passport number. These numbers are required because a precondition for becoming a client is being a Swedish resident or an EU or EEA citizen.

• An identification rule defines how an institutional entity is to be identified. It consists of a process description for determining the identity of an institutional entity. If this process is performed successfully, the identity of the entity is acknowledged via the use of an identifier, for example, a client number. In the process of identifying agents, such as human beings, the process involves (re)authentication, such as entering a password or displaying a key card. For example, client numbers are used to identify clients by the social welfare department, which requires a human being to provide his/her assigned client number and show that he/she has the right to use it. If the client cannot provide a client number and show that he/she has the right to use it, the client can provide identifying descriptions instead, such as a name, in combination with an address, PID, or EU or EEA passport number. If none of these pieces of evidence can be provided by the client, the social welfare officer can acknowledge that the human being is already known to him/her and that he/she can help the human being to provide the client number.

Language rules define the meaning of an institutional language, whereas regulative rules regulate the social interaction between institutional entities. These two kinds of rules are interdependent. For example, the regulative rule that ‘‘a municipality has the duty to provide income support to a household’’ can be correctly applied only when combined with language rules that guide the social welfare officer on how to identify a household. If the identification is unclear, there will be ambiguities, affecting the quality of the social interaction.

## Modeling guidelines

This section reports a number of practical problems found in the income support case study. Through a root cause analysis of these problems, a number of generic modeling problems are identified, and solutions in the form of guidelines are proposed.

## Information infrastructures

Today, institutional processes are often performed using information infrastructures. For example, the income support case handling process, which consists of the actions a–e described in ‘‘Institutional processes and the case study’’ section, is performed by using the information infrastructure described below. The case handling system is used by the social welfare officer performing actions a, b, d, and e, and he/she uses the multiquery e-service for action c to obtain facts about the clients from a number of state agencies.

The left side of Figure 2 displays the institutional facts that are associated with the household relationship and created using the case handling system. The right side of Figure 2 describes a number of state agency registers. The left and the right sides describe the installed base (the old part of the infrastructure) in Sweden, which was developed during 1970–2000, while the middle part of the figure describes the new infrastructure, which has been developed since 2009.

The new part of the infrastructure consists of a multiquery e-service with an Application Programming Interface (API) that interoperates with SSBTEK, which is a system-to-system service. The multiquery e-service is used in action c of the case handling process by the social welfare officers to send an XML query, containing the case ID of a case and the PID numbers of the clients. SSBTEK mediates answers back to the e-service for presentation to the social welfare officer. This interaction is regulated by the statute (SFS, 2008: 975 n.d.), which prescribes in detail the institutional facts that the social welfare officers can request from the registries at the authorities, as well as the facts the authorities are obligated to provide to the social service departments.

In eliciting the requirements for the new part of the information infrastructure, the case handling systems used at the municipalities were investigated in order to develop an API between that system and the multiquery e-service. Two requirements stipulated that the API had to provide a unique case identifier and the PID numbers of the clients. However, when the case handling systems used at the municipalities were analyzed, a number of practical problems were identified.

## Practical problems

The basic cause of the problems identified was that the case handling systems were implemented on the basis of the paperbased process that was used before the systems were introduced. At that time, in the 1980s, a social welfare department created a paper file (a personal case file) and wrote the PID number of the so-called registry leader on it. If there were two adults in a household, the PID number of the adult man was used. Subsequently, all the documents that were relevant to the case were stored in that file. In a paper-based registry, it is practical to consider the paper file that contains all the documents of interest to be the natural institutional entity. Thus, the case handling systems were based on the descriptive conceptual model below (see Figure 3).

The model shows that there was only one class ‘‘File’’ and one identifier, the term ‘‘Registry LeaderID,’’ and a PID number ‘‘19450102-9999’’ was used as the identifier for the ‘‘RegistryLeader.’’ In most cases, the PID number of the man in the household was used, meaning that the PID number was used in a triply ambiguous way: as an identifier for the case, for the household, and for the male client in the household. These multiple uses of the PID number made the other clients of the household, such as women and children, difficult to find and identify in the registry. A problem with the model above is that it does not model institutional facts properly. In particular, it does not address how institutional entities, such as cases, clients, households, and their identifiers, are distinguished. The model only represents an already existing thing, a paper file, and this limitation caused a number of practical problems, as follows:

![](/api/attachments/N2X2B8HD/fulltext/images/2c23442fd4b403e783a637b5729a2ecf207f221fdbdbe99b34916a3c23945945.jpg)  
Figure 2 Income support information infrastructure prescribed by regulations.

![](/api/attachments/N2X2B8HD/fulltext/images/bbc458b931f2492d020d7960e364116c494d5c2b5086f9f40900c407db37f7f9.jpg)  
Figure 3 Paper file modeled as a class and object instance.

(P1) If a woman in a household wanted to know the status of a case, she had to provide the PID number of the man to identify it.

(P2) A case decision was only sent to the man, not to the woman, even though both represented the household.

(P3) The state agencies did not allow the municipalities to access information using a PID number as a case identifier.

(P4) Statistics about the clients partitioned by gender could only be produced by retrieving the entries in the registry one by one and counting them manually.

(P5) It was difficult to retrieve statistics about how many clients had been members of a household that was granted income support.

(P6) Cases were reopened if a new application for income support was sent in within three months of the most recent decision regarding the granting of income support. When the law (SFS, 1986: 223 n.d.) was scrutinized, it was determined that a case should not be reopened when a decision had been made. Nevertheless, it remained possible to reopen a case in the case handling systems, which was not in line with the legislation.

## Solutions to the practical problems

The following subsections discuss solutions to the generic problems that underlie the practical problems experienced in the income support case. All of these problems may occur in any modeling project within institutional contexts in which designers have to model and design an institutional language. Accordingly, this undertaking is an institutional matter as well as a technical one (Bowker and Star, 1999).

In the diagrams presented below, each class is stereotyped using the notation stereotype, referring to a construct of the middle level of the institutional ontology. Below the classes, the diagrams show instances of classes that are examples of institutional facts. Below these, the diagrams show physical grounding relationships to material reality that belong to the bottom level of the ontology. Using UML in this way helps to make the point that institutional reality is a matter of institutional facts, not physical things and their properties.

## Selecting classes

A key issue in any modeling project is to identify and distinguish the classes needed to represent the domain under consideration in a complete and easily understandable way (Eriksson et al., 2013; Lukyanenko and Parsons, 2011; Wand et al., 1999; Zwass, 1997). Problems P1–P3 were caused by the fact that concepts such as household, client, and case were not clearly separated through classes of their own. This issue has been resolved in the model shown in Figure 4.

In this model, Client, Household and Case are distinct classes, each having its own identifier, HouseholdID, ClientID, and CaseID. Each class has its own application, instantiation, and identification rules. By distinguishing between the Case, Client, and Household classes, the model makes explicit that the instances of Client should be created and identified separately from those of the instances of Household and Case. Notice that even if there is only one client, a household should be created, because this is the only institutional entity that can be granted income support.

Generalizing, by being aware of the application, identification, and instantiation rules that hold in a domain, a modeler can better select what classes to include in a model of that domain. Hence, an institutional ontology to support conceptual modeling needs to include support for language rules. For example, in the conceptual modeling literature, the choice of institutional identifiers is often wrongly assumed to be just a technical implementation decision (Eriksson and Agerfalk, 2010). However, the choice of identifier and the identification rule are important in designing and selecting classes in conceptual modeling (Henderson-Sellers et al., 2015), especially in information infrastructure design (Bowker and Star, 1999). A crucial condition in implementing such an infrastructure is to use a uniform reference system that allows for unambiguous identification of institutional entities across contexts (Beynon-Davies, 2015; Eriksson and Agerfalk, 2010). The above discussion results in the following guideline:

Guideline 1: Each class should have its own unique language rules.

## Choosing between grounding and generalization

In the case study, no distinction was made between the classes Household and Client, which made statistics about gender and number of clients in a household difficult to produce (problems P4 and P5). Guideline 1 can address this kind of problem by separating the household and client classes, as they have different language rules. However, using grounding instead of generalization (Steimann, 2000b) can sometimes be helpful for distinguishing and counting entities.

![](/api/attachments/N2X2B8HD/fulltext/images/6a7d730e6d5515bff8784a820f63400288ecfbca1562ec4b4be73fc3884bcf5d.jpg)  
Figure 4 An object model that resolves problems P1–P3 by differentiating between the Client, Household, and Case classes

The instantiation rule for the Client class, described in ‘Language rules’’ section, prescribes that being a Swedish resident or an EU or EEA citizen is a precondition for becoming a client. Nevertheless, Client, Resident, EU Citizen, and EEA Citizen should not be related in a generalization hierarchy because these classes have different language rules, and they are maintained by different institutional subjects, municipalities, and states. For example, the application rule for Resident is that ‘‘a child born in Sweden counts as a resident if the mother is a resident, or if the father is a resident and is the caretaker of the child’’ (SFS, 1991: 481 n.d.). This rule differs from the application rule for Client in ‘Language rules’’ section, and the instantiation rules of the classes are also different. A municipality is able to create clients and assign them unique identifiers, Client IDs, but it is not authorized to assign PID numbers, as this is the responsibility of the Swedish Tax Agency. Further, because not every client will have a Swedish PID number, the identification rule cannot prescribe the use of a PID number as the identifier for Client.

An alternative to generalization is to let Client be related to Resident via a grounding association, as shown in Figure 5, so that a client is institutionally grounded in a resident. Using such a model, each client could be easily identified and counted, for example, for statistical purposes, which would resolve problems P4 and P5.

Another advantage of using grounding instead of generalization is that it results in a looser coupling between the classes Client and Resident, making the model in Figure 5 more robust to changes. One scenario is that the application rule for Resident is changed so that it becomes more restricted. If Client was modeled as a subclass of Resident, this might accidentally invalidate the subclass relationship between Client and Resident, as there may be clients that are no longer residents.

Generalizing, relating classes via grounding relationships instead of via generalization assists in avoiding what Masolo (2011) calls ‘‘isa overloading,’’ that is, an overuse of the ‘‘isa relation’’ in domain models. This also helps to overcome some classical difficulties related to multiple classification and specialization, especially in modeling roles (Steimann, 2000a, b; Vieu et al., 2008; Halpin, 2016). The above discussion results in the following guideline:

![](/api/attachments/N2X2B8HD/fulltext/images/ad5426b589a9d0eca5b98057f10b73dc772745fb5a5d6da8dd5085edadc404c7.jpg)  
Figure 5 A model that shows the grounding relationship between Client and Resident.

Guideline 2: Grounding should be used instead of generalization if the classes to be related do not share the same language rules.

## Distinguishing between institutional relationships and associations

In conceptual modeling, associations and relationships are often used interchangeably (Wand et al., 1999). However, the two notions of association and institutional relationship are separate constructs. The association construct in UML is a modeling construct used to represent a link or reference between two classes in a model.

In contrast, an institutional relationship is an ontological construct and should be modeled as a class of its own, because it can have its own attributes and associations with other classes. This is illustrated in the model in Figure 6, which solves problem P6, that is, the problem of ‘‘reopening a case,’’ by modeling the Household Relationship as a class of its own that is associated with the Case class. The solution distinguishes between institutional processes and institutional relationships. A household relationship is an institutional relationship between a municipality and a household, whereas a case is an institutional process. The process starts when a new application has been received and is normally closed within 14 days. This time span differs from that of a household relationship, which could be open for several months, depending on how much time it takes for the household to become self-sufficient. If a new application is sent in the next month, a new case should be created within an already open and existing household relationship. However, the case handling system did not clearly distinguish the household relationship as a class of its own. As a consequence, a case was erroneously reopened when, instead, a new case should have been started within an existing open relationship. To remedy this situation, the new model makes it possible to show that there could be several instances of Case within the same instance of Household relationship.

The above discussion results in the following guideline:

Guideline 3: Institutional relationships should be modeled by a class, not by an association.

Modeling rights through institutional relationships or contracts Rights are ontologically different from physical properties. For example, the property weight of a human being refers to the property of a single entity, whereas a household that has been assigned and granted income support (a right to receive an allowance) refers to a relationship between a number of parties: a household and a municipality. A property is intrinsic to human beings and physical entities, whereas a right is relational and exists within an institutional relationship. In summary, rights cannot be modeled simply as attributes but require relational constructs to be represented (Geerts and McCarthy, 2006; Hruby, 2010).

In the institutional ontology, rights can be assigned in two ways: by creating an institutional relationship, which constitutes new institutional entities, or by creating a new institutional entity within a preexisting relationship. An example of the former method is creating a new household relationship and constituting a new household in action b. Thereby, the household has been assigned the duty to the municipality to make an effort to support itself, but it can also have a legitimate claim on the municipality for income support; see Figure 7. An example of the latter way of assigning rights is when the household is granted income support (an institutional contract) in action e. The above discussion results in the following guideline:

![](/api/attachments/N2X2B8HD/fulltext/images/8d72fe20e1572e77b4f1a62ba6f88bb630e12e74a17e117b11d3db68cc7c9553.jpg)  
Figure 6 An object model that shows a case and a household relationship as different but associated objects.

Guideline 4: A right should be modeled through an institutional relationship or a contract between institutional entities.

## Discussion and conclusions

This section summarizes the research contribution, discusses practical and theoretical implications, and suggests directions for future research.

This article asked how institutional reality could be modeled, taking into account the prescriptive role of conceptual models, and thereby supporting more valuable information infrastructures. We answered this question by proposing an institutional ontology that acknowledges an ontological difference between the material and institutional realities. The ontology can be used to explain how information infrastructures become a part of institutional reality. Our experience from the case studies that we performed is that we did not primarily model physical things and their properties. Instead, we modeled institutional facts; that is, the institutional reality was our prime focus. Even in the case studies where physical things were prevalent, for example, in the Volvo case study, the institutional facts were at the fore. The solutions to the conceptual problems identified in the case studies were not found by observing the existing world of physical things and their properties, or their conceptions, and describing them more faithfully. Instead, the solutions had to be sought in an understanding of the constituents of institutional reality and, in particular, how rule systems prescribed the creation and regulation of institutional entities.

![](/api/attachments/N2X2B8HD/fulltext/images/24d4593ae423fc57cc67a3a3f53f3e7f42918fa960634c8cf446dc5a69b70664.jpg)  
Figure 7 A model that shows the right to receive income support as an institutional contract related to a household institutional relationship.

Hence, the case studies indicated the need for a solid basis for modeling institutional reality, thereby supporting the design of more valuable information infrastructures. Our method of addressing this need is the proposed institutional ontology, which is able to represent the constitution of institutional reality; that is, we propose using an ontology that explains how rules, human beings, and physical entities create and relate to institutional facts.

## Practical implications

The influence of media on the conceptualization of institutional reality

When designing conceptual models, developers need to recognize institutional facts as entities of their own, but still not as things. For example, the income support case illustrates that designers need to distinguish between a thing, ‘‘the paper file,’’ on the one hand, and institutional facts (cases, households, clients, etc.), on the other hand. However, this distinction is easily overlooked in practice because paper media make institutional entities appear similar to physical things (Ong, 2002, p. 11). For example, a paper file can take such a prominent role in people’s minds that they start to conflate it with the institutional entities it mediates. One way to help developers escape this ‘‘thing metaphor’’ in institutional contexts is to provide a conceptualization that distinguishes between material and institutional entities. This distinction is offered by the institutional ontology.

## Requirements elicitation in institutional domains

The representation assumption states that the reason why information systems are used is that they often provide ‘‘a cheaper means of knowing the state of the real-world phenomena they represent than observing the phenomena directly’’ (Wand and Weber, 2017, p. 3). It is assumed that the information system is only a description of the real world that exists outside the system. This assumption differs from the ontological commitment on which this article is based, which implies that there is no demarcation line between information system and reality. Instead, an information system is viewed as part of reality and as participating in its construction. By taking this view, the proposed ontology helps designers to avoid the pitfall of assuming that conceptual modeling in institutional domains is a realitymapping exercise between real-world things that exist outside an information system, on the one hand, and their representations in the system, on the other hand (Wand and Wang, 1996). Instead, as the case studies showed, conceptual modeling is a design exercise, in which institutional reality is investigated by analyzing many sources, including user requirements and regulations of the domain as well as the installed base. In this activity, conceptual modeling is used not only in a descriptive, but also in a prescriptive role, as shown in Figure 8.

As a consequence, the requirements are derived via analysis of the rules for the domain in question and the installed base, as well as via analysis of how the stakeholders want to perform social interactions and create institutional facts. In institutional domains, efforts have to be made to discuss the rules and their interpretation with lawyers and actors responsible for the installed base. Designers who have the intent to evolve the information infrastructure need not just accept the rules as they are. They may also criticize how they are designed, interpreted, and implemented, and even try to change them if they are inappropriate and not effective in use. The proposed ontology can be used to support such a design process aimed at designing information infrastructures.

![](/api/attachments/N2X2B8HD/fulltext/images/1e65fb5763b550c25bc264c968847294cbe21e25e6ce1c4f99de0842a04c1cd7.jpg)  
Figure 8 Descriptive versus prescriptive models illustrated by the income support case study.

## The reproduction of institutional structures through information infrastructures

One critical finding that emerged from the analysis of the case handling systems was that they discriminated against women, as did the practices they constituted and reproduced. The practice of making the adult male client the ‘‘registry leader’’ created problems for a woman in a household in terms of her ability to control the institutional process in which she was engaged (see problems P1 and P2). This is particularly problematic in households that receive income support because, in many cases, they involve conflicting interests between a woman and a man. This is a clear example of how designs, and the practices that they institutionalize, are far from neutral. It was taken for granted (a culturalcognitive pillar) that it was the male who should be assigned the role of registry leader. However, this taken-for-grantedness was based on a norm (a normative pillar), which implied that it was the man who was the head of, and primarily responsible for, the household. This assumption was also made into an explicit instantiation rule (a regulative pillar) for users when they created a new case.

This example illustrates how the installed base, including its conceptual models and language rules, which was implemented in the 1980s, preserved and reproduced an institutional reality that sustained gender inequality. This finding is in line with the conclusion of Bowker and Star (1999, p. 290) that classification systems are linked together in information infrastructures ‘‘enjoining deep consequences for those touched by them.’’ Accordingly, conceptual modeling that defines the institutional language and classification systems should be of prime concern for organizational developers and managers, not just software engineers. The proposed institutional ontology can also help software engineers to become aware of the cultural and normative aspects of conceptual modeling.

Guidelines for conceptual modeling in an institutional context The institutional ontology has been used to derive four guidelines (see ‘‘Solutions to the practical problems’’ section for details) for modeling institutional reality. We have shown how problems P1–P6, identified in the case handling systems, could be resolved using these guidelines and the conceptual models that are presented in Figures 4, 5, 6, and 7. The solutions to the problems can also be illustrated by creating and populating a test database based on the models (see ‘‘Appendix’’ for more details).

## Theoretical implications

Acknowledging the distinction between institutional and material realities

The most influential ontology used for conceptual modeling in information systems research, the Bunge–Wand–Weber (BWW) ontology, focuses on things and their properties (Wand et al., 1999, p. 497). It maintains that ‘‘the world is made of things that possess properties’’ and that ‘‘the notion of a concrete thing applies to anything perceived as a specific object by someone, whether it exists in physical reality or only in someone’s mind.’’ This approach has its basis in scientific philosophy (Bunge, 1977), where it has been successfully used for the purpose of describing things and their properties. However, it is not sufficient for representing and reasoning about the interplay between language, media, institutions, and information infrastructures, that is, about the construction of institutional reality.

The existence of institutional reality and institutional facts is dependent on both mental states of human beings and material reality. However, they do not exist in someone’s head or in physical reality. Institutional facts are neither mental nor material constructs, but language and social constructs.

To quote Searle (2005, p. 14), ‘‘one can say this: human societies require a deontology, and the only way they can have this is by having language. To repeat, no language, no deontology.’’ This insight is reflected in the institutional ontology, which emphasizes the constitutive function of language. The ontology shows how to conceptualize the key components in the construction of institutional reality, in particular, how institutional entities are created through institutional actions, how they can be grounded in physical entities, and how they are used to regulate human interaction through the assignment of rights.

## Acknowledging the prescriptive role of conceptual modeling for institutional reality

Hirschheim et al. (1995) proposed a distinction between two schools of conceptual modeling: the fact-based approach (which we refer to as the representation assumption) and the rule-based approach. The representation assumption embraces the idea of an objective reality that can be faithfully described. In contrast, the aim of a conceptual model within the rule-based approach with which we comply is to formalize prescriptive rules used for communication in institutional reality. Much of the ontology-based conceptual modeling literature has focused on the descriptive function of models (Wand et al., 1999; Wand and Weber, 2017), but there is also a need to take into account the prescriptive function of models (thereby moving to the upper-right quadrant listed in Table 1).

## Further research

A revival of conceptual modeling for the information systems community – involving a contemporary ‘‘institutional turn’ for the area – is motivated because of the large impact that implemented conceptual models have on society at large (Bowker and Star, 1999) and its institutions. These models form shared conceptions in which meaning is created in social interaction (cultural-cognitive pillar), provide a basis for regulating social interaction (regulative pillar), and help to produce and reproduce norms and values (normative pillar). Recognizing the impact of institutional modeling on institutional reality opens up a new research agenda. For example, Parsons and Li (2007) note the widespread disagreements on role modeling, offering a categorization of three possible interpretations: roles as named places in a relationship; roles as a form of generalization/specialization; and roles as separate instances, adjoined to the entities playing the roles. The institutional ontology allows for an alternative explanation based on institutional facts. Another theoretical issue is that of the classification of rules in rule modeling. Current rule-modeling approaches already distinguish between different kinds of rules, for example, business rules and definitional rules in SBVR (Semantic Business Vocabulary and Rules) (SBVR 1.4 n.d.), and the institutional ontology can provide a theoretical basis for such classifications.

Society and institutional reality are changing as a result of digitization (Couldry and Hepp, 2016). In the case of income support, most of the institutional facts are not created using paper. Instead, digital media are used (see the right side of Figure 8). The transition process from paper to digital is changing the way we think about and create entities of institutional reality. The income support case is only one example. Money is another example. In modern economies, most money in circulation is created digitally, rather than being fiat money mediated by bank notes (Macfarlane et al., 2017). How the transition from paper media to digital media affects our conceptual models of institutional reality is a topic deserving further attention in ontology and conceptual modeling research.

The institutional ontology is also applicable to the development of the so-called Internet of Things (IIC n.d.), where new technology and sensor networks are used to connect physical devices, furniture, buildings, and other items to the Internet.

Applications within the Internet of Things require the interaction between physical things and humans in institutional contexts. To analyze and design this interaction, developers need an understanding of the distinction and the relationships between physical things and institutional entities, which can be provided by the institutional ontology. In particular, the ontology can help to clarify the role of physical things in institutional contexts in terms of rights assigned to them.

The ontology presented in this paper has been incrementally developed over several years, with each iteration including formative evaluations. However, the final ontology has not yet been validated in a summative evaluation, which is left for future work. Thus, we acknowledge that the institutional ontology presented should not be seen as fixed and final. We have also chosen the solutions to the modeling problems that we found most appropriate for institutional contexts. However, there is no single set of criteria for what constitutes the most appropriate explanation in every context (Lipton, 2000).

Finally, the ontological status of information infrastructures as a part of institutional reality implies that more research is needed to address implementation problems, not just modeling problems. The issue at stake is that today’s institutional reality consists, to a large extent, of an installed base, which is costly and complex to change and extend. We experienced this issue in the income support case study, where our modeling and design activities revealed a need to change the registry of income support, in line with the database outlined in ‘‘Appendix.’’ However, such changes would require rebuilding the entire case handling system, imposing considerable costs; in the end, only parts of the changes could be realized. Thus, deficient conceptual structures implemented in an information infrastructure are not easily changed. As a consequence, there is a need not only for improved modeling techniques but also for new transition and implementation strategies that can support developers in transforming language structures implemented in the installed base.

## References

Alvesson, M. and Ka¨rreman, D. (2007). Constructing Mystery: Empirical Matters in Theory Development, Academy of Management Review 32(4): 1265–1281.

Bach, K. (2003). Speech Acts and Pragmatics, in The Blackwell Guide to the Philosophy of Language, Chichester: Wiley-Blackwell, pp. 147–167.

Barley, S.R. and Tolbert, P.S. (1997). Institutionalization and Structuration: Studying the Links Between Action and Institution, Organization Studies 18(1): 93–117.

Beaney, M. (2016), Analysis, Summer 2016 edn, Metaphysics Research Lab, Stanford University.

Bera, P., Krasnoperova, A. and Wand, Y. (2010). Using Ontology Languages for Conceptual Modeling, Journal of Database Management 21(1): 1–28.

Berente, N. and Yoo, Y. (2012). Institutional Contradictions and Loose Coupling: Postimplementation of NASA’s Enterprise Information System, Information Systems Research 23(2): 376–396.

Berger, P.L. and Luckmann, T. (1966). The Social Construction of Reality: A Treatise in the Sociology of Knowledge. Garden City, NY: Anchor Books.

Bergholtz, M. and Eriksson, O. (2015). Towards a Socio-Institutional Ontology for Conceptual Modelling of Information Systems, in M. Jeusfeld and K. Karlapalem (eds.) Advances in Conceptual Modeling, Lecture Notes in Computer Science, Cham: Springer, pp. 225–235.

Beynon-Davies, P. (2015). Form-ing Governance. Transforming Government: People, Process and Policy 9(1): 126–135.

Beynon-Davies, P. (2016). Instituting Facts: Data Structures and Institutional Order, Information and Organization 26(1–2): 28–44.

Boell, S.K. and Cecez-Kecmanovic, D. (2015). What is an Information System?, in 2015 48th Hawaii International Conference on System Sciences (HICSS), ieeexplore.ieee.org, pp. 4959–4968.

Bowker, G. and Star, S.L. (1999). Sorting Things Out. Cambridge: MIT Press.

Bricker, P. (2016). Ontological Commitment, Winter 2016 edn, Metaphysics Research Lab, Stanford University.

Bubenko, Jr., J.A. (2007). From Information Algebra to Enterprise Modelling and Ontologies—A Historical Perspective on Modelling for Information Systems, in Conceptual Modelling in Information Systems Engineering, Berlin: Springer, pp. 1–18.

Bunge, M. (1977). Treatise on Basic Philosophy: Ontology I: The Furniture of the World, Vol. 3, Berlin: Springer Science & Business Media.

Burton-Jones, A., Recker, J., Indulska, M., Green, P. and Weber, R. (2017). Assessing Representation Theory with a Framework for Pursuing Success and Failure, Management of Information Systems Quarterly 41(4): 1307–1333.

Casson, M.C., Della Giusta, M. and Kambhampati, U.S. (2010). Formal and Informal Institutions and Development, World Development 38(2): 137–141.

Cornelissen, J.P., Durand, R., Fiss, P.C., Lammers, J.C. and Vaara, E. (2015). Putting Communication Front and Center in Institutional Theory and Analysis, Academy of Management Review 40(1): 10–27.

Couldry, N. and Hepp, A. (2016). The Mediated Construction of Reality, Wiley. Date, C.J. (2003). An Introduction to Database Systems, 8th edn, Pearson.

DeVaujany, F.-X., Carton, S., Mitev, N. and Romeyer, C. (2014). Applying and Theorizing Institutional Frameworks in IS research: A Systematic Analysis from 1999 to 2009, Information Technology & People 27(3): 280–317.

Elder-Vass, D. (2012). The Reality of Social Construction, Cambridge: Cambridge University Press.

Eriksson, O. (2000). Kommunikationskvalitet hos informationssystem och affa¨rsprocesser, PhD thesis, Linko¨pings universitet.

Eriksson, O. (2015a). Studie av en samling offentliggemensamma digitala resurser: E-recept, in Swedish.

Eriksson, O. (2015b). Studie av en samling offentliggemensamma digitala resurser: Ladok, in Swedish.

Eriksson, O. and Agerfalk, P. (2010). Rethinking the Meaning of Identifiers in Information Infrastructures, Journal of the Association for Information System 11(8): 433–454.

Eriksson, O. and Goldkuhl, G. (2015). Studie av en samling offentliggemen samma digitala resurser: Ekonomiskt bista˚nd, in Swedish.

Eriksson, O., Henderson-Sellers, B. and Agerfalk, P.J. (2013). Ontological and Linguistic Metamodelling Revisited: A Language Use Approach. Information and Software Technology 55(12): 2099–2124.

Evermann, J. and Wand, Y. (2005). Ontology Based Object-Oriented Domain Modelling: Fundamental Concepts, Requirements Engineeringv10(2): 146–160. Gadamer, H.G. (1975). Truth and Method, Seabury Press.

Geerts, G.L. and McCarthy, W.E. (2006). Policy-Level Specifications in REA Enterprise Information Systems, Journal of Information Systems 20(2): 37–63.

Gosain, S. (2004). Enterprise Information Systems as Objects and Carriers of Institutional Forces: The New Iron Cage? Journal of the Association for Information Systems 5(4): 151–182.

Gruber, T.R. (1995). Toward Principles for the Design of Ontologies Used for Knowledge Sharing? International Journal of Human-Computer Studies 43(5): 907–928.

Habermas, J. (1985). The Theory of Communicative Action, Volume 1: Reason and the Rationalization of Society, reprint edn, Beacon Press.

Halpin, T. (2007). Fact-Oriented Modeling: Past, Present and Future, in J. Krogstie, A.L. Opdahl and S. Brinkkemper (eds.) Conceptual Modelling in Information Systems Engineering, Berlin: Springer, pp. 19–38.

Halpin, T. (2016). Object-Role Modeling Workbook: Data Modeling Exercises Using ORM and NORMA, Technics Publications.

Hanseth, O. and Lyytinen, K. (2010). Design Theory for Dynamic Complexity in Information Infrastructures: The Case of Building Internet. Journal of Information Technology 25(1): 1–19.

Henderson-Sellers, B., Eriksson, O. and Agerfalk, P.J. (2015). On the Need for Identity in Ontology-Based Conceptual Modelling, in M. Saeki and H. Kohler (eds.) Proceedings of the 11th Asia-Pacific Conference on Conceptual Modelling (APCCM 2015), Vol. 27, Sydney, Australia: CRPIT, pp. 9–20.

Henderson-Sellers, B., Eriksson, O., Gonzalez-Perez, C. and Agerfalk, P.J. (2013). Ptolemaic Metamodelling?: The Need for a Paradigm Shift, in Progressions and Innovations in Model-Driven Software Engineering, IGI Global, pp. 90–146.

Hirschheim, R., Klein, H.K. and Lyytinen, K. (1995). Information Systems Development and Data Modeling: Conceptual and Philosophical Foundations, Cambridge: Cambridge University Press.

Hirschheim, R., Klein, H.K. and Lyytinen, K. (1996). Exploring the Intellectual Structures of Information Systems Development: A Social Action Theoretic Analysis, Accounting, Management and Information Technologies 6(1): 1–64.

Hodgson, G.M. (2006). What are Institutions? Journal of Economic Issues 40(1): 1–25.

Hohfeld, W.N. (1913). Some Fundamental Legal Conceptions as Applied in Judicial Reasoning, The Yale Law Journal 23(1): 16–59.

Hruby, P. (2010). Model-Driven Design Using Business Patterns. Berlin: Springer Science and Business Media.

IIC. (n.d.). Industrial Internet Consortium. Accessed: 2017-12-4.

Jacobson, I., Ericsson, M. and Jacobson, A. (1994). The Object Advantage: Business Process Reengineering with Object Technology (ACM Press), first edn, Addison-Wesley Professional.

Lindgren, R., Eriksson, O. and Lyytinen, K. (2015). Managing identity tensions during mobile ecosystem evolution. Journal of Information Technology 30(3): 229–244.

Lipton, P. (2000). Inference to the Best Explanation, in W. H. Newton-Smith (ed.) Companion to the Philosophy of Science, Wiley-Blackwell, pp. 184–193.

Lukyanenko, R. and Parsons, J. (2011). Rethinking Data Quality as an Outcome of Conceptual Modeling Choices, in A. Koronios and J. Gao (eds.) Proceedings of the 16th International Conference on Information Quality 2011 (ICIQ 2011), Routledge, pp. 1–16.

Macfarlane, L., Ryan-Collins, J., Bjerg, O. and others. (2017). Making Money from Making Money, Technical Report.

Mantere, S. and Ketokivi, M. (2013). Reasoning in Organization Science, Academy of Management Review 38(1): 70–89.

March, S.T. and Allen, G.N. (2014). Toward a Social Ontology for Conceptual Modeling, Communications of the Association for Information Systems 34(1): 70.

Masolo, C. (2011). Levels for Conceptual Modeling, in Advances in Conceptual Modeling. Recent Developments and New Directions, Berlin: Springer, pp. 173–182.

Mignerat, M. and Rivard, S. (2009). Positioning the Institutional Perspective in Information Systems Research, Journal of Information Technology 24(4): 369–391.

Milton, S.K., Rajapakse, J. and Weber, R. (2012). Ontological Clarity, Cognitive Engagement, and Conceptual Model Quality Evaluation: An Experimental Investigation, Journal of the Association for Information Systems 13(9): 657–693.

NSOE 2013. (n.d.). Riksnormen for forso¨rjningssto¨d, in Swedish, http://www. socialstyrelsen.se/ekonomisktbistand/riksnormen. Accessed: 2017-12-4.

Ong, W. (2002). Orality and Literacy; The Technologizing of the Word, Routledge.

Orlikowski, W.J. and Iacono, C.S. (2001). Research Commentary: Desperately Seeking the ‘‘IT’ in IT Research—A Call to Theorizing the IT Artifact, Information Systems Research 12(2): 121–134.

Parsons, J. and Li, X. (2007). An Ontological Metamodel of Classifiers and Its Application to Conceptual Modelling and Database Design, in C. Parent, K.-D. Schewe, V.C. Storey and B. Thalheim (eds.) Conceptual Modeling—ER 2007, Berlin: Springer, pp. 214–228.

Patton, M.Q. (1990). Qualitative Evaluation and Research Methods, 2nd edn, Sage Publications, Inc.

Pishdad, A., Koronios, A., Reich, B.H. and Geursen, G. (2014). Identifying Gaps in Institutional Theory, in Proceedings of the 25th Australasian Conference on Information Systems (ACIS), ACIS.

Powell, W.W. and DiMaggio, P.J. (eds.) (1991). The New Institutionalism in Organizational Analysis, 1 edn, University of Chicago Press.

SBVR 1.4. (n.d.). Semantics of Business Vocabulary and Business Rules. http:// www.omg.org/spec/SBVR/1.4/index.htm. Accessed: 2017-12-4.

Schutz, A. (1967). The Phenomenology of the Social World. Evanston, Ill: Northwestern University Press.

Scott, W.R. (2001). Instituitions and Organizations. Thousand Oaks, CA: Sage Publications.

Scott, W.R. (2003). Institutional Carriers: Reviewing Modes of Transporting Ideas Over Time and Space and Considering Their Consequences, Industrial and Corporate Change 12(4): 879–894.

Searle, J.R. (1969). Speech Acts: An Essay in the Philosophy of Language: 1st (First) Edition, reprint 1970 edn, Cambridge University Press.

Searle, J.R. (1995). The Construction of Social Reality, Free Press.

Searle, J.R. (2005). What is an Institution? Journal of Institutional Economics 1(1): 1–22.

Searle, J.R. (2006). Social Ontology: Some Basic Principles, Anthropological Theory 6(1): 12–29.

Searle, J. (2010). Making the Social World: The Structure of Human Civilization (1st ed.). USA: Oxford University Press.

SFS 1986:223. (n.d.). Forvaltningslag, in Swedish, http://www.notisum.se/rnp/sls/ lag/19860223.HTM. Accessed: 2017-12-4.

SFS 1991:481. (n.d.). Folkbokfo¨ringslag, in Swedish, http://www.notisum.se/rnp/ sls/lag/19910481.HTM. Accessed: 2017-12-4.

SFS 2001:453. (n.d.). Socialtjanstlag, in Swedish, https://www.riksdagen.se/sv dokument-lagar/dokument/svensk-forfattningssamling/socialtjanstlag-2001453\_sfs-2001-453. Accessed: 2017-12-4.

SFS 2008:975. (n.d.). ‘Om uppgiftsskyldighet i vissa fall enligt socialtja¨nstlagen, in Swedish’, https://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forf attningssamling/forordning-2008975-om-uppgiftsskyldighet-i\_sfs-2008-975 Accessed: 2017-12-4.

Shanks, G., Tansley, E. and Weber, R. (2003). Using Ontology to Validate Conceptual Models, Communications of the ACM 46(10): 85–89.

Shanks, G. and Weber, R. (2012). The Hole in the Whole: A Response to Allen and March, MIS Quarterly 36(3): 965–980.

SOSFS 2013:1. (n.d.). Socialstyrelsens allmanna rådom ekonomiskt bistånd, in Swedish, https://www.socialstyrelsen.se/sosfs/2013-1. Accessed: 2017-12-4.

Stamper, R.K. (2001). Organisational Semiotics: Informatics Without the Computer? in K. Liu, R.J. Clarke, P.B. Andersen and R.K. Stamper (eds.) Information, Organisation and Technology, Information and Organisation Design Series, Berlin: Springer, pp. 115–171.

Star, S.L. and Ruhleder, K. (1996). Steps Toward an Ecology of Infrastructure: Design and Access for Large Information Spaces, Information Systems Research 7(1): 111–134.

Steimann, F. (2000a). On the Representation of Roles in Object-Oriented and Conceptual Modelling, Data & Knowledge Engineering 35(1): 83–106.

Steimann, F. (2000b). On the Representation of Roles in Object-Oriented and Conceptual Modelling, Data & Knowledge Engineering 35(1): 83–106.

Vieu, L., Borgo, S. and Masolo, C. (2008). Artefacts and Roles: Modelling Strategies in a Multiplicative Ontology, in C. Eschenbach and M. Gru¨ninger (eds.) Proceedings of the 2008 Conference on Formal Ontology in Information Systems, Amsterdam, The Netherlands: IOS Press, pp. 121–134.

Wand, Y., Storey, V.C. and Weber, R. (1999). An Ontological Analysis of th Relationship Construct in Conceptual Modeling, ACM Transactions on Database Systems 24(4): 494–528.

Wand, Y. and Wang, R.Y. (1996). Anchoring Data Quality Dimensions in Ontological Foundations, Communications of the ACM 39(11): 86–95.

Wand, Y. and Weber, R. (2002). Research Commentary: Information Systems and Conceptual Modeling—A Research Agenda, Information Systems Research 13(4): 363–376.

Wand, Y. and Weber, R. (2006). On Ontological Foundations of Conceptual Modeling: A Response to Wyssusek, Scandinavian Journal of Information Systems 18(1): 127–138.

Wand, Y. and Weber, R. (2017). Thirty Years Later: Some Reflections on Ontological Analysis in Conceptual Modeling, Journal of Database Management 28(1): 1–17.

Weber, R. (2003). Editor’s Comments: Still Desperately Seeking the IT Artifact, Management of Information Systems Quarterly 27(2): iii–xi.

Wieringa, R.J., de Jonge, W. and Spruit, P. (1995). Using Dynamic Classes and Role Classes to Model Object Migration, Theory and Practice of Object Systems 1(1): 61–83.

Wodak, R. (2004). Critical Discourse Analysis, in C. Seale, G. Gobo, J.F. Gubrium and D. Silverman (eds.) Qualitative Research Practice, Thousand Oaks, CA: Sage Publications, pp. 197–213.

Zwass, V. (1997). Foundations of Information Systems, Irwin/McGraw Hill.

## About the Authors

Owen Eriksson is an Associate Professor of informatics in the Department of Informatics and Media at Uppsala University. His research is action-oriented and designoriented, and he has been the research leader of a number of externally funded research projects in close cooperation with authorities and industry.

Paul Johannesson (pajo@dsv.su.se) received his B.Sc. in Mathematics and his Ph.D. in Computer Science from Stockholm University. He holds a position as professor in information systems at Stockholm University. Johannesson has published work on federated information systems, enterprise modeling, schema and process integration, e-commerce systems design, and business models.

Maria Bergholtz (maria@dsv.su.se) received her B.Sc. in Computer Science and her Philosophical Licentiate in Computer Science from Stockholm University. She holds a position as lecturer at Stockholm University. Bergholtz has published work on enterprise modeling, ontology, service modeling, e-commerce systems design, and business models.

## Appendix

<table><tr><td>Municipality</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>OrganizationalNo (PK)</td><td>MunicipalityName</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>212000-0142</td><td>Stockholm City</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Department</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>DepartmentID(PK)</td><td>DepartmentName</td><td colspan="2">OrganizationalNo (FK)</td><td></td><td></td><td></td><td></td></tr><tr><td>D12</td><td>Social Welfare</td><td>212000-0142</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Client</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ClientID (PK)</td><td>FirstName</td><td>LastName</td><td>PIDNo</td><td>HouseholdID (FK)</td><td>Gender</td><td></td><td></td></tr><tr><td>1313</td><td>Per</td><td>Sjölund</td><td>19951023-0338</td><td>92882</td><td>Male</td><td></td><td></td></tr><tr><td>Case</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CaseID (PK)</td><td>StartDate</td><td>EndDate</td><td>Status</td><td colspan="2">RelationshipID (FK)</td><td></td><td></td></tr><tr><td>asdf165</td><td>2014-09-10</td><td>2014-09-26</td><td>Closed</td><td>hr3456722</td><td></td><td></td><td></td></tr><tr><td>Action</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ActionID (PK)</td><td>Action date</td><td>ActionType</td><td>CaseID (FK)</td><td></td><td></td><td></td><td></td></tr><tr><td>asdf1111</td><td>2014-09-10</td><td>a</td><td>asdf165</td><td></td><td></td><td></td><td></td></tr><tr><td>asdf1112</td><td>2014-09-10</td><td>b</td><td>asdf165</td><td></td><td></td><td></td><td></td></tr><tr><td>asdf1113</td><td>2014-09-20</td><td>c</td><td>asdf165</td><td></td><td></td><td></td><td></td></tr><tr><td>asdf1114</td><td>2014-09-21</td><td>d</td><td>asdf165</td><td></td><td></td><td></td><td></td></tr><tr><td>asdf1115</td><td>2014-09-23</td><td>e</td><td>asdf165</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">Household Relationship</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>RelationID (PK)</td><td>OrganizationalNo (FK)</td><td>DepartmentID (FK)</td><td>HouseholdID (FK)</td><td>Status</td><td>StartDate</td><td>Enddate</td><td></td></tr><tr><td>hr3456722</td><td>212000-0142</td><td>D12</td><td>92882</td><td>Open</td><td>2014-09-10</td><td></td><td></td></tr><tr><td>Household</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>HouseholdID(PK)</td><td>ConstitutionDate</td><td>HouseholdType</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>92882</td><td>2014-09-10</td><td>Single</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">Granted Income Support</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ContratcID(PK)</td><td>FromDate</td><td>ToDate</td><td>Amount</td><td>RelationID (FK)</td><td></td><td></td><td></td></tr><tr><td>16282828</td><td>2014-10-01</td><td>2014-10-30</td><td>3000</td><td>hr3456722</td><td></td><td></td><td></td></tr></table>

![](/api/attachments/N2X2B8HD/fulltext/images/5d99302bb1a1feb24942ea2fd6a84e0b7e900ac4965a83d8fcd75b62208cfe67.jpg)  
A test database based on the models in Figures 4, 5, 6 and 7.
