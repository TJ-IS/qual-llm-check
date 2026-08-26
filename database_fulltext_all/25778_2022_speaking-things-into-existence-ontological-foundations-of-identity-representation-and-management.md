---
otero_id: 25778
otero_key: "MEPYKPVE"
title: "Speaking things into existence: Ontological foundations of identity representation and management"
authors: "Owen Eriksson; Pär J Ågerfalk"
year: "2022"
journal: "Information Systems Journal"
doi: "10.1111/isj.12330"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
DOI: 10.1111/isj.12330

R E S E A R C H O P I N I O N

WILEY

# Speaking things into existence: Ontological foundations of identity representation and management

Owen Eriksson | Pär J Ågerfalk

Informatics and Media, Uppsala University, Uppsala, Sweden

Correspondence

Owen Eriksson, Informatics and Media, Uppsala University, Uppsala, Sweden. Email: owen.eriksson@im.uu.se

## Abstract

Conceptual models capture knowledge about domains of reality. Therefore, conceptual models and their modelling constructs should be based on theories about the world— that is, they should be grounded in ontology. Identity is fundamental to ontology and conceptual modelling because it addresses the very existence of objects and conceptual systems in general. Classification involves grouping objects that share similarities and delineating them from objects that fall under other concepts (qualitative identity). However, among objects that fall under the same concept, we must also distinguish between individual objects (individual identity). In this paper, we analyze the ontological question of identity, focusing specifically on institutional identity, which is the identity of socially constructed institutional objects. An institutional entity is a language construct that is ‘spoken into existence’. We elaborate on how institutional identity changes how we understand conceptual modelling and the models produced. We show that different models result if we base modelling on a property-based conception of identity compared to an institutional one. We use the Bunge-Wand-Weber principles, which embrace a property-based view of identity, as an anchor to the existing literature to point out how this type of ontology sidesteps identity in general and institutional identity in particular. We contribute theoretically by providing the first in-depth ontological analysis of what the notion of institutional identity can bring to conceptual modelling. We also contribute a solid ontological grounding of identity management and the identity of things in digital infrastructures.

## 1 | INTRODUCTION

Conceptual models capture knowledge about domains of reality. Therefore, conceptual models and their modelling con structs should be based on theories about the world—that is, they should be grounded in ontology (Wand, Storey, & Weber, 1999). Ontology is the study of being, of what there is (Bricker, 2014). Using ontology as a foundation for concep tual modelling assumes that ontology can help us better understand the constitution of the world (Gruber, 1995; Wand et al., 1999; Wand & Weber, 2006). To facilitate conceptual modelling, work based on the Bunge–Wand–Weber (BWW) ontology, the dominant conceptual modelling ontology in information systems (IS), suggests several ontology-based guide lines. Conceptual modelling addresses the following fundamental question: 'How can we model the world to better facili tate our developing, implementing, using, and maintaining more valuable information systems?' (Wand & Weber, 2002 p. 363). To answer this question, the notions of identity and identification are central: 'identifying the things in a domain i a prerequisite to our eliciting the remaining semantics – for example, the attributes that are important, the relationships that exist among things, and the classes used to generate a view of the domain' (Wand et al., 1999, pp. 505–506)

Indeed, identity is a fundamental pillar of every conceptual system. Without a proper understanding of identity it is unlikely that any conceptual structure can be formulated because nothing can be a concept or an object without its identity conditions (Bueno, 2014). Although identity is fundamental to conceptual modelling, the ontologica grounding of identity and its implications for conceptual modelling have yet to be thoroughly addressed (Henderson Sellers, Eriksson, & Ågerfalk, 2015). Recent attempts at broadening the perspective of ontology for conceptua modelling to include institutional perspectives vindicate the need for such grounding (Beynon-Davies, 2018; Burton-Jones & Grange, 2013; Clarke, Burton-Jones, & Weber, 2016; Eriksson, Johannesson, & Bergholtz, 2018; Lemieux & Limonad, 2011; March & Allen, 2014; Recker, Lukyanenko, Jabbari, Samuel, & Castellanos, 2021).

The BWW ontology assumes that IS only describe the real world that exists outside the systems, and conceptua models are supposed to provide a formal means of representing information about the world (Wand et al., 1999; Wand & Weber, 1995, 1996): 'the reason information systems were used to provide representations is that they often provide a cheaper means of knowing the state of the real-world phenomena they represent than observing the phenomena directly' (Wand & Weber, 2017, p. 3). However, 'this classical view of an information system is increas ingly obsolete' (Baskerville, Myers, & Yoo, 2020, p. 509), because digital technologies are now creating and shaping reality (Aakhus, Ågerfalk, Lyytinen, & Te'eni, 2014):

Step by step as our world gets filled with swaths of information where the 'original' and the 'copy reside inside as well as outside an information system proper (Eriksson & Ågerfalk, 2010; Kallinikos, 2011), what used to be a valuable document (e.g., an airfare ticket, a vehicle service book) may now only be a physical copy of a digital original that resides in the information systems of some corporation or authority. (Aakhus et al., 2014, p. 1190)

In this ontological reversal, institutional entities become real within digital infrastructures and 'reality becomes a reflection of our models in the digital world. This reversal has profound implications for the IS field' (Baskervill et al., 2020, p. 509).

Based on a literature review, Boell and Cecez-Kecmanovic (2015) conclude that definitions of IT artefacts in IS research are often grounded in an ontological position that separates technology from social actors. However, thi separation has become increasingly difficult to defend because IT artefacts are now interconnected in digital infrastructures and encode institutional logics that enable and restrict social interaction (Ågerfalk, 2020). Such interaction creates institutional facts that are 'the invisible substrate information' embedded in digital infrastructures (Iannacci, 2010, p. 36). Registries of institutional entities—for example, drugs, owners, students, residents, prescribers, prescriptions, organizations, and their identifiers (Eriksson & Ågerfalk, 2010)—must be readily available throughout the infrastructure to ensure their sustainability. Thus, identifying the institutional entities in the domain becomes a fundamental task in digital infrastructure design (Sundgren, 2014). Institutional identity is also becoming increasingly important because of international regulations such as the EU 910/2014, which mandates that authori ties within the EU offer digital services and electronic transactions not restricted to national eIDs as well as accepting foreign eIDs (Tsakalakis, Stalla-Bourdillon, & O'Hara, 2017). Increasing digital theft and fraud has also made authori ties and legislative bodies aware of the crucial role of identity and how it is assigned (Beynon-Davies, 2016a). In th United States, for example, switching vehicle identification numbers and stolen identities to secure loans for expen sive vehicles is a growing problem (Martinelli, Mercaldo, Nardone, Santone, & Vaglini, 2018)

Thus, improved identity management (i.e., assigning and verifying institutional identity) is needed at both the national and international level to provide better digital services to citizens and to prevent fraud and criminal activi ties (Beynon-Davies, 2016a). At the same time, institutional entities must also retain some fidelity to the physica world (Aakhus et al., 2014; Lyytinen, 2006). The increasing interest in the Identity of Things (IDoT) (Zhu & Badr, 2018) puts new requirements on identity management and our understanding of digital institutional identity Altogether, this calls for a better understanding of how institutional identity relates to physical things.

Digitalization, the process of digitizing 'broader social and institutional contexts that render digital technologie infrastructural' (Tilson, Lyytinen, & Sørensen, 2010, p. 2), is also changing how identity is understood. Since institutional entities now exist in a digital form without any apparent relation to material things, there is an imminent need for thoroughly understanding the notion of institutional identity and institutional reality and how these notions relate to digital infrastructures. Hence, this article proposes an ontological grounding of institutional identity to help us answer the following question: How should we model the world to develop, implement, use, and maintain digita infrastructures in the construction and change of institutional reality?

This work aims to open up the black-box of digitalization by providing valuable knowledge about the digital con struction of institutional reality. This un-black-boxing requires an institutional understanding of identity, and concep tual modelling is a powerful analytical tool for understanding the constitution of digital institutional reality Implications include a better foundation for designing and selecting classes, which are fundamental to conceptua modelling. Moreover, as IoT becomes increasingly important, the IDoT (Zhu & Badr, 2018) puts new requirement on identity management and the understanding of digital institutional identity.

The article proceeds as follows. First, we address how ontology-based conceptual modelling has discussed th notion of identity (Section 2). We then present the reconstructive research approach adopted (Section 3) and subse quently use this to develop the idea of institutional identity (Section 4) and elaborate on how an institutional identity changes the way we conceive of conceptual modelling and the models produced (Sections 5 and 6). We illustrate th analysis using the Central Vehicle Registry (CVR) at the Swedish Transport Agency (STA) and compare the suggested approach with the BWW guidelines. Finally, we summarize the contributions, discuss implications for research and practice (Section 7), and present conclusions (Section 8).

## 2 | THE NOTION OF IDENTITY IN CONCEPTUAL MODELLING

## 2.1 | Qualitative and numerical identity

Conceptual modelling involves classifying objects—that is, grouping objects that share similarities and delineatin them from objects that fall under other concepts. Classifying objects as the same requires them to fall under the same concept, which presupposes the identity of the concept under consideration. This identity is called 'qualitativ identity' in philosophy (Noonan, 2006; Noonan & Curtis, 2018). Falling under a concept is a form of identification at the type level. If we say that 'John' is identical to 'Mary', we must mean that they are qualitatively identical because they share the property (type) of being a '(physical) person'; they belong to the same concept (Weiner, 2004). In other words, a person has the property of being human with a visible body.

However, one also needs to identify objects at the individual level, which is called 'numerical identity' in philosophy (Weiner, 2004). Assuming they both fall under the concept of person, we must be able to distinguish betwee Mary and John if we want to identify them as individuals and, for example, count them. Individual identity is a mutua relationship between the identifier used—for example, a name such as John—and the concept (type) person that defines its meaning. A language construct, such as the name John, the code DCA001, or the number 123982839, is an identifier if its value is guaranteed to be unique within the type (concept) that gives it meaning. Individual identity should satisfy at least two conditions: distinguishability and re-identification (Bueno, 2014; Dummett, 1981). The dis tinguishability condition states that one can distinguish an object from other objects that fall under the same concept in a specific context, for example, an identity parade where a witness identifies a distinct person within a group o people.

The re-identification condition says that the object should be possible to re-identify across time and space. That is, because an object remains the same, it can be identified consistently across contexts. For example, the legal system assumes a witness can identify the same person 3 months after witnessing a crime even though the person, for example, has lost a limb in an accident.

In the conceptual modelling literature, the predominant view is that an object, or entity, is a modelling construct used to represent things. Hence, the identification of things is fundamental to conceptual modelling (Wand et al., 1999). Chen states that 'an entity is a “thing”, which can be distinctly identified' (Chen, 1976, p. 10). However, Date concludes that 'we cannot state with any precision exactly what an entity is' (Date, 2004, p. 411). Object orientation also recognizes the problems associated with object identity. For example, Wirfs-Brock and McKean not that '[f]inding good objects means identifying abstractions that are part of your application's domain and its execution machinery. Their correspondence to real-world things may be tenuous, at best' (Wirfs-Brock & McKean, 2003, p. 78).

To resolve these ambiguities, scholars have developed ontologies such as the BWW ontology (Wand et al., 1999) and the Unified Foundational Ontology (UFO) (Guizzardi, 2005; Guizzardi & Wagner, 2005). UFO and BWW base their conception of an object on physical things, which are instances of natural kinds, also referred to as 'concrete things', or 'substantial individuals', or 'physical objects' (Wand et al., 1999; Guizzardi, 2005, p. 263–264; Guizzardi & Wagner. 2005). Physical things (material things) can be human-made things (artefacts) such as cars. natu ral 'dead' things such as mountains, and biological living things such as animals and people (Guizzardi, 2005; Guizzardi & Zamborlini, 2014; Wand et al., 1999). Physical things can or could exist in physical reality, they have a mass and physical extension, and they abide by natural laws

UFO and BWW, however, identify these things differently (Guizzardi, 2005, pp. 263–264). The BWW ontolog assumes a unique set of physical properties that distinguish a thing (distinguishability condition). However, to base identity on such an assumption is problematic. Most people would acknowledge that somebody who loses a limb is still the same person. Re-identification of a specific thing over time cannot be guaranteed under the distinguishabilit condition. Identity is here seen as temporal because a change of properties is not allowed and therefore applies onl within a situated context.

UFO assumes identity to be provided by substance sortals (natural kinds), such as people and cars (Guizzardi, 2005): 'A principle of identity regarding a sortal S makes explicit the properties that no two instances of S can have in common, because such properties uniquely identify S instances' (Guizzardi et al., 2018, p. 4). A kind i necessarily rigid because it must apply to its instances in all possible situations (Guizzardi, 2005, p. 216; Guizzardi & Zamborlini, 2014), which according to UFO also solves the re-identification condition: 'In particular, it also informs which changes an individual can undergo without changing its identity, i.e., while remaining the same' (Guizzard et al., 2018, p. 4). For example, the sortal person is the unique substance sortal that defines the validity of the claim that the numerical identity of a person persists through changes in height, weight, age, residence, and so on (Guizzardi, 2005, p. 100):

Person can only be the sortal that supports the proper name Mick Jagger in all possible situations because it applies necessarily to the individual referred to by the proper name. That is, instances of Person cannot cease to be so without ceasing to exist. (ibid.)

As a consequence, the extension of a substance sortal is world-invariant. This meta-property of universals is called modal constancy or rigidity. Modal constancy implies that a person is identified as a unique person when born an cannot be identified as such when having ceased to exist physically. However, it is unclear exactly how a substantia sortal could rigidly supply a universal identity to a unique person in all possible situations over a full lifetime, whethe a new-born or a 94-year-old (Merricks, 1998). This question becomes even more problematic in the case of clones and of mass-produced things with precisely the same shape and properties and when institutional entities do not require a one-to-one correspondence to an instance of a substance sortal in order to exist. UFO does not explain precisely how a sortal could provide identity in every situation, only that it does. If this would be the case, why woul we need ID documents to verify identity?

## 2.2 | The institutional turn in conceptual modelling

The promise of ontologies such as BWW and UFO to help us better model a domain remains elusive in institutiona contexts. Accordingly, several scholars have suggested an 'institutional turn' in conceptual modelling (Beynon Davies. 2016a. 2016b. 2018: Eriksson & Ågerfalk, 2010: Eriksson et al., 2018: March & Allen. 2014) based on Searle's social ontology (Searle, 1995, 2005, 2006, 2010).

In this line of research, Eriksson and Ågerfalk (2010) use Searle's ontology to analyse the function of identifiers in digital infrastructures, to introduce the notion of an institutional entity in conceptual modelling, and to propos guidelines for the design of identifiers. Beynon-Davies (2016a) examined the central place of lists of identifiers to unpack the constitutive capacity of information systems. March and Allen (2014) propose a meta-model using Searle's social ontology as the basis for conceptual modelling. Eriksson et al. (2018) propose an institutional ontolog for conceptual modelling that could support the design of digital infrastructures, which is also theoretically informed by institutional theory. Institutional theory (neo-institutionalism) views institutions as regulative, normative, and cultural–cognitive structures, also called institutional pillars, which together with social interaction provide stabilit and meaning to social life (Scott, 2001).

March and Allen (2014) and Eriksson et al. (2018) highlight the critical concept of status function (Searle, 2005, 2006, 2010), which Eriksson et al. (2018) refer to as institutional function. Institutional functions are abstract constructions that have little to do with materiality except for what mediates the function. For example, a digital objec that counts as a personal bank account in a banking context can be assigned the institutional function of being money for use in economic exchanges and clearing of debts. There is no requirement of a physical coin or paper to mediate it. A digital personal bank account (Figure 1) performs the institutional function of money not by its physica structure but by its collective acceptance: 'All you need in order to have money is a system of recorded numerica values whereby each person (or corporation, organization, and so on) has assigned to him or her a numerical figur which tells at any given point the amount of money they have' (Searle, 2006, p. 18).

Institutional functions represent bundles of deontic powers that can be assigned to conceptual objects: 'Such bundles of deontic powers are often recognized as conceptual objects or roles within an organization or within soci ety in general' (March & Allen, 2014, p. 1348). Eriksson et al. (2018) suggest that the assignments of institutiona functions to conceptual objects are governed by classification rules, which enable people to constitute and identif institutional entities. The constitutive function of language is so fundamental to the institutional reality that it is often overlooked. It may seem that entities such as money, customers, and students simply exist, but these are al socially constructed concepts mediated through language.

We use classification rules combined with regulative rules to create institutional entities and assign them an institutional identity. In Sweden, the law SFS 2011:755 is the basis for formulating the rules to be used in instantiat ing digital money. A bank that provides digital payment services interprets these rules and defines compliant rule for its payment services (Swedbank, 2020). Thus, some of the rules are typically defined by the state, and organiza tions subsequently define compliant and more specific rules (March & Allen, 2014; Stamper & Ades, 2004).

Regulative rules (Ostrom, 2011) prescribe what actions are required, prohibited, or permitted (i.e., the ought to be of reality), such as a regulative rule that 'a Customer is permitted to use a Personal bank account for Transactions'. However, a regulative rule can be correctly applied only when combined with specific classification rules. For exam ple, to use the regulative rule defined above, an actor must know whether to classify someone or something as a customer, personal bank account, or transaction. We need classification rules that prescribe the class name and define the class: 'The implication is that we must first conceptualize the class as a set of deontic powers and declare the class to exist before it can be populated with instances' (March & Allen, 2014, p. 1351). Accordingly, the layered model in Figure 1 implies a hierarchy between different layers. Instantiating institutional entities requires a superordinate class, and the class definition requires a superordinate rule system. However, 'the structure not only iter ates upward, but it expands laterally […] We never just have one institutional fact, but we have a series of interlocking institutional facts.' (Searle, 2006, p. 18). A customer has a claim towards the bank and the custome can use the personal bank account to pay debts and withdraw money. However, to instantiate a customer, a physi cal person must first have been assigned a Swedish PID number and therefore be assigned the institutional func tion of a resident.

Institutional function is fundamental to determining qualitative identity. Institutional entities within a class ar similar because they share the same institutional function in society. We use classes to create (instantiate) institu tional entities, which are the conceptual objects. A conceptual object has the following characteristic

![](/api/attachments/MEPYKPVE/fulltext/images/e1ab7d5ed3b667542137b38e71e917c6c8581f4dfcd4dc9609b20fcf69c3a0d1.jpg)  
F I G U R E 1 Conceptual model of digital money [Colour figure can be viewed at wileyonlinelibrary.com]

• created based on rules;

• referred to with an identifier; and

• an instantiation of a concept;

• referred to in human communication;

• collectively agreed upon in social reality;

• created via a speech act at a certain time;

• can represent brute facts (if the object relates to physical reality) and institutional facts (if the object relates to institutional reality); and

• created with some kind of media and therefore has a physical representation, for example, in the form of sound waves, paper, steel plates, or traces on a computer disc.

A conceptual object is an institutional entity if it also represents rights (Eriksson & Ågerfalk, 2010). Institutional enti ties, created through institutional practices, regulate social interaction through the assignment of rights. Eriksso et al. (2018) use the term 'right' instead of Searle's 'deontic power' based on Hohfeld's (1913) classification. Rights include claims and duties as well as powers and privileges. In Figure 1, the customer has a claim towards the bank Reciprocally, the bank has a debt towards the customer. A personal bank account mediates the claim and the debt Organizations maintain lists of such identified digital institutional entities, including banks, cases, tickets, invoices, students, residents, certificates, transactions, corporations, health records, bank customers, purchase orders, juridica persons, personal accounts, and medical prescriptions (Beynon-Davies, 2016a; Eriksson & Ågerfalk, 2010).

Accordingly, institutional entities such as a corporation or money are real even though they are not physical enti ties (Searle, 1997). They are real because we inter-subjectively acknowledge their identity and existence and becaus they are used in and have real consequences for social interaction. As such, they are a constitutive component of digital infrastructures (Beynon-Davies, 2016a; Eriksson & Ågerfalk, 2010; Eriksson et al., 2018; Iannacci, 2010).

## 2.3 | Summary of related research

The major problem with UFO and BWW, from an institutional perspective, is that they base their ontology and notion of identity on already identified and existing entities (natural kinds) that can be observed and have an extension in physical reality (Bird & Tobin, 2018). Such a 'physical first' approach can provide only a limited understandin of institutional reality because institutional entities are not given by nature: they are created and are assigned iden: tity. Accordingly, several IS scholars have recently advocated an institutional turn in conceptual modelling (Beynon Davies, 2016a, 2016b, 2018; Eriksson & Ågerfalk, 2010; Eriksson et al., 2018; March & Allen, 2014). The emerging body of literature highlights different aspects of what is developing into a concept of institutional identity as an essential concept for conceptual modelling. For example, the literature puts forth the idea that institutional functions are th basis of qualitative identity and that identifiers assign individual (numeric) identity. In addition, the literature investi gates methods and techniques to identify bundles of deontic powers and institutional entities and how these map t physical reality, which will have a significant impact on IoT research. Notably, none of these initiatives carefull develops and analyses the notion of institutional identity, which is the focus of the article at hand.

## 3 | RESEARCH METHOD

This article adopts a reconstructive analysis (Habermas, 1976, p. 29), which is an approach concerned with 'the ratio nal reconstruction of concepts, criteria, rules and schemata' (Habermas, 1976, p. 29). Based on a hermeneuticall guided understanding of rule systems used to produce symbolic constructs through language, we present explicit knowledge about concepts and rules. The analysis is explication-oriented towards symbolic formations create according to rules (Habermas, 1976, p. 31). Concepts, principles, and rules, on one hand, and symbolic outcomes, on the other, guide the explication. The context of our analysis is conceptual modelling. The rule systems analysed ar guidelines for conceptual modelling, the language used is the modelling language UML, and the symbolic outcome i conceptual models.

The explication focuses on the notion of identity. In the analysis, we first address the identity construct from a BWW perspective and then show how BBW's idea of identity results in different guidelines (rules for conceptua modelling) and models (outcomes) compared to an institutional conception of identity. That is, we use the BWW ontology as an anchor to the existing literature to point out how the dominant ontology in conceptual modellin sidesteps identity in general and institutional identity in particular. BWW is the natural choice for such a compariso because of its dominance in research on ontology-based conceptual modelling in the management information systems literature (Wand & Weber, 2017). We also chose the BWW ontology because it defines ontological principles that underpin the notion of identity and is well documented with an explicit rule system, which makes it suitable for a reconstructive analysis (Wand et al., 1999). The principles of ontological clarity and conformance have generated both empirical research and theoretical debate over the years (Burton-Jones, Recker, Indulska, Green, & Weber, 2017; Wand & Weber, 1993). Accordingly, many articles already criticize the BWW ontology, primarily based on the 'institutional turn' in conceptual modelling (see above). In response to this critique, Wand and Weber conclude that 'it is important to move forward from philosophical debates about the assumptions to investigating whether dif ferent assumptions have any practical import' (Wand & Weber, 2017, p. 9). They further suggest that researchers could conduct an ontological analysis of a domain using the BWW ontology and a corresponding study using speech act theory and then compare the outcomes, which is the approach taken in this article

Our primary dataset is from the Swedish CVR case. A second dataset provides typical modelling patterns and problems addressed in the BWW modelling literature (e.g., Evermann & Wand, 2005; Parsons & Wand, 2000; Wand et al., 1999). The reconstructive analysis starts with the ontological principles underpinning the property-based con ception of identity as embraced by the BWW ontology. With this foundation, we elaborate on the concept of institu tional identity. Next, we use the BWW principles with their property-based conception of identity to model the things that constitute car ownership (Figure 4). Based on a worldview that emphasizes institutional reality and an institutional concept of identity, we model the institutional entities that constitute traffic vehicle ownership (Figure 7) and identify the differences compared to the BWW guidelines. Finally, we elaborate on how the differ ences between the models result from different notions of object existence and identity.

## 4 | ANALYSING THE NOTION OF IDENTITY

## 4.1 | Analysing the property-based conception of identity using speech act theory

The BWW ontology defines a class as a 'set of things possessing a common property' where 'a kind is defined by a set of properties, and a natural kind is defined by a set of lawfully related properties' (Wand et al., 1999, p. 501) Two ontological principles underpin the BWW notion of identity (Wand et al., 1999, p. 512)

Principle 1\*. No two things possess exactly the same set of specific properties.

Principle 2\*. (Nominal invariance): 'A thing, if named, shall keep its name throughout its history as long as the latter does not include changes in natural kind-changes which call for changes of name'. (Bunge, 1977, p. 221).

Here, classes are defined using 'properties of individual things; that is, substantial properties' and the practica implication for conceptual modelling is that '[i]dentification attributes are not part of a conceptual model. At first glance, this implication is counterintuitive, as “name” and “key”' are usually the first attributes of a thing to be identi fied [….] it indicates that they have no significance in modelling the world' (Wand et al., 1999, p. 512)

Principle 1 assumes that its unique set of physical property instances distinguishes a thing (distinguishability con dition): 'No two things have exactly the same set of individual properties. Thus, properties can be used to identif things' (Evermann & Wand, 2005, p. 149). However, as we have already shown, properties can change. Therefore this principle cannot fulfil the re-identification condition.

Principle 2 relies on the assumption of nominal invariance, which is concerned with the problem of preserving the identity of a thing (re-identification condition) despite its properties changing. Principle 2 means that the preser vation of identity relies on the assignment of an insignificant unique name (identifier) to a thing that can unambigu ously identify the thing across space and time. However, the BWW ontology does not provide answers to two questions: (a) What are the natural-kind changes that call for name changes? and (b) What is the relationship between the constant name and the changing thing? Frege and Searle can help us answer these questions based on a language-use conception of identity

## 4.1.1 | What are the natural-kind changes that call for name changes?

Frege (1892), analysing how names relate to material things, concluded that there is no exact one-to-one unambigu ous match between a name and a thing. For example, we could socially agree that the names Evening Star, Mornin Star, and Venus correspond to the same thing in the sky. To explain this, Frege (1892) made a distinction betwee 'reference' and 'sense'. With this distinction, the meaning of the statement Evening Star = Morning Star is not the same as Venus = Venus. To explain this, Frege suggests that the name Venus expresses a sense— that is, names are not insignificant marks.

On the contrary, the concepts (types) implied (Planet) or contained (Star) by the names give the senses of the names (Venus, Evening Star, and Morning Star). The physical thing seen in the sky is known by different identities depending on how it is classified and referenced. It is essential to understand that we can change the identity of a physical thing by changing its classification or name (identifier), that is, altering the identity of the thing in the sky in three different ways, namely Morning Star, Evening Star, and Venus the Planet. That is, the names are pseudonyms not synonyms; they identify the same thing but with different meanings.

With respect to question (a) above, there are no natural-kind changes of a thing that call for modifications of the name. Two stars in the sky did not suddenly merge to become a cold planet. Rather, our conception and knowledg of the thing and the social agreement about the identity of the thing observed changed. When we now use the nam Venus, we agree that we are talking about a planet when we watch the thing in the sky, not two stars.

## 4.1.2 | What is the relationship between the constant name and the changing thing?

The name Venus, however, does not have a universal meaning. In a different context, utterance 'Venus' may reference another object, for example, a goddess or a statue. To explain this, Searle (1969) further developed Frege's idea by introducing a language use conception of identity: 'We need to distinguish, as Frege failed to do, the sense of a referring expression from the proposition communicated by the utterance' (Searle, 1969, p. 92).

The language use conception of identity suggests that identity depends on the social context in which it is acknowledged and known. Essentially, an identity statement is the performance of a speech act to identify referenc (a reference act), that is, an intentional symbolic act performed in a social context. To refer and identify is a matter o learning how to use words or sentences in a successful reference act to select a unique object collectively. A suc cessful reference act answers the questions of which, who, or what. Of course, having identified something, one may still ask 'what?' in the sense of 'tell me more about it', but one cannot ask 'what?' in the sense of 'I do not know wha you are talking about?'

For example, 'the red car' could be used to communicate the identity of an observable car in a local showroom context, assuming that there is only one red car in the room. It is tempting to see such an identity statement as describing an already existing, previously known object, not recognizing the difference between the conceptua object and the physical thing. However, if previously unreferenced, an object needs to be instantiated into the con versation and therefore into social reality:

Language does not simply symbolise a situation or object which is already there in advance – it makes possible the existence or appearance of that situation or object, for it is part of the mechanism whereby that situation or object is created. (Mead, 1934, p. 78)

If the listener does not acknowledge the existence of the object, he or she will not be able to identify it. The speake and the listener must agree that there is a thing they can refer to as 'the red car'. The actors have spoken the conceptual object into existence in this social context. This understanding is crucial because of the possibility of using the reference in a speech act. For example, 'the red car has an automatic gearbox' is an assertive expression using 'the red car' as its reference mechanism. The predicate, 'has an automatic gearbox', ascribes an attribute to the object. The success of this speech act relies on the existence of 'the red car' as a meaningful, inter-subjectively agreed-upo conceptual object in social reality

According to Searle (1969), we can use language to refer to and therefore identify an existing object by using two reference mechanisms (Figure 2):

1. By using a definite description, for example, 'the red car', to fulfil the reference function using descriptive attributes;

2. By using a unique identifier, such as a name, a number, or the code DCA001, to fulfil the reference function with out using descriptive attributes

Thus, if there is only one red car or only one car with the registration number DCA001 in sight, the reference will b successful. The advantage of definite descriptions compared to identifiers is that they contain descriptions of proper ties. However, the problem with definite descriptions is that they cannot be used to re-identify a thing over tim because properties might change, so they apply only within a temporally situated context. If the colour of the car changes from red to blue, the identity of the car also changes.

The identifier construct is the ultimate language construct for separating the referring function of language which refers to and identifies objects, from the descriptive function which describes objects. A reference mechanism independent of attributes (i.e., an identifier such as a name, a number, or a code) is essential to achieving a sustainable reference. Such a link is not affected by contingent changes induced by space and time—that is, changes in physical reality such as changes in colour and other properties of a single physical car. The meaning of the identifie depends on the social context of its use. You can use an identifier to identify (i.e., to select an obiect) only if it is uniquely known through that identifier (Searle, 1969, p. 82).

Moreover, it must be possible to re-identify the object, and it is the identifier together with the concept (th type) that fills this gap. The identifier is assigned to an object at a particular time. To re-identify the object in another context, one must identify it as the same object using the same identifier across contexts

Thus, the answer to question (b) above is that the identity relationship between the name and the thing is an indirect relationship between an identifier (name), which refers to a conceptual object, and indirectly to a corresponding thing. The sense of the name accounts for its cognitive significance: it is the way by which one con ceives of the reference of the term. Therefore, no direct link exists between a name and the thing named. The name functions as a symbolic link and not as a physical one, and the name is not an insignificant label attached to the thing. This loose coupling (Searle, 1969, p. 170) makes the meaning of the identifier unaffected by changes in colour and other properties of a physical thing. A licence number, unlike colour, is not a physical property of the thing.

![](/api/attachments/MEPYKPVE/fulltext/images/f822f53f0609118f3ae8544bfb25f855bff32ab619ea41b71777dcf12c3534c0.jpg)  
F I G U R E 2 Instantiation of a car object in the social world within a showroom context [Colour figure can be viewed at wileyonlinelibrary.com]

## 4.1.3 | Problems with a property-based notion of identity

Although the property-based notion of identity seems to be universal, it is only valid in a local and situated context. It assumes the existence of a physical thing: 'In the real world an object simply exists' (Wand et al., 1999, p. 512) That is, the properties do not change if identity is to be preserved and it therefore only works under this physical, temporal, local, and situated assumption. In addition, a property-based notion of identity cannot account for how the identity of the thing can change despite unchanging properties, as in the case of the Planet Venus, and cannot account for that most entities in institutional reality do not correspond to physical things (Figure 1). Furthermore identifiers (names), such as the licence number, do not seem to have anything at all to do with the true identity of a physical thing. For example, the physical red car would exist, be observable, and be possible to identify without the licence number. Somewhat paradoxically, identifiers such as DCA001 were introduced in society just because the are a much more useful device to identify a car than a definite description.

## 4.2 | Institutional identity

If we analyse the meaning (the sense) of the licence number based on language use within institutional reality, the seeming identity paradox of the car disappears. Within institutional reality, we see that DCA001 has a particular meaning if understood as an identifier of an institutional entity. DCA001 is the identifier of a traffic vehicle institutional entity, and the licence number tagged onto the physical thing serves to prove that the physical thing is certi fied for use on public roads. The physical thing with its physical properties and the institutional entity constituted b signs are ontologically different as are their functions. The function of the physical car is to be a means for transportation. The function of the institutional entity and its identifier is to be a means for identification and for regulating social interaction in society. The licence number is a language construct and not a physical property—that is, it is a composition of signs. The licence number represents rights, which we might not consider if we do not understand its institutional function. As explained above, identifiers are pragmatic referencing mechanisms compared to definit descriptions because such identifiers are not affected by contingent changes of physical properties. Therefore, the could be used to identify entities across contexts and assign rights. Thus, in institutional contexts, an identifier is th preferred reference mechanism. Qualitative identity is here based on institutional function in social interaction, whil the use of an institutional identifier understood in the sense of its institutional function defines individual identity.

In institutional reality, identity is something that is socially constructed based on the use of classification rules that is, when an object is instantiated into social reality. For example, an STA officer created the traffic vehicle entit when registering and assigning it the licence number DCA001. This institutional process instantiates a traffic vehicl institutional entity using an institutional language. In this case, it also requires the existence of a physical red car without which the registration is meaningless. Thus, the STA must secure trustworthy and legitimate physical evi dence that a corresponding physical thing exists. However, one should not confuse the institutional entity and it identity with the physical evidence needed.

## 5 | MODELLING INSTITUTIONAL REALITY USING THE BWW GUIDELINES

The BWW ontology maintains that the fundamental pillar of conceptual modelling is the identification of alread existing things. According to the BWW guidelines, institutional identifiers, such as the licence number, are mutua properties—that is, they do not identify intrinsic properties of physical cars. As described above, identifying properties of the car class are car body, engine, make, gearbox, weight, length, colour, number of seats, number of doors and so on. Mutual properties. such as the licence number, emerge from the interaction between a person thing and a car thing (Bera, Burton-Jones, & Wand, 2014). When two things interact, one may cause the other to change, an a mutual property that reflects that interaction is 'a binding mutual property' (Wand et al., 1999, p. 503). If we make a conceptual model based on these assumptions, we can identify the class Car, because the things that are classifie exist as physical things (Figure 3). A set of individual physical properties can uniquely identify each physical thing In the same vein, we find the class Person because persons are existing things determined by a set of identifying properties in the world, such as age, DNA, sex, hair, teeth, weight, length, eye colour, fingerprint, and so on. We model the person–car thing interaction as a subclass Person-Owns-Car of the superclass Person, which has acquired the additional mutual property 'licence number' as a result of the interaction.

It is important to note that the model in Figure 3 is only a description of the real world. That is, the conceptua model and the information system designed based on the model should map to the physical to be a proper represen tation (Wand & Wang, 1996; Weber, 2003).

Classes are the primary constructs in a UML class diagram. Other classes, such as subclasses and association classes, derive from classes and their relationships in the UML meta-model. The association construct in UML is a modelling construct that represents a relation between two classes, and one can attach an association class to an association to provide additional information about the association. Inheritance relationships are shown in a hierar chy with superclasses at the top and derived subclasses below. Subclasses inherit all the attributes of the superclass.

According to BWW, classes represent physical things and classes contain attributes that describe properties of the things. Person-Owns-Car is modelled as an association class because ontological clarity requires the use of an association class to model interactions (Bera et al., 2014; Evermann & Wand, 2005), which has the mutual attribute licence number represented by the mutual property shown on the licence plate. Subclasses are formed by 'adding attributes to the set of attributes that describe properties possessed by the things in a class (Wand et al., 1999 p. 500). We call forming classes this way an attribute-oriented view of classes

In Figure 4, we have added the class Corporation and accepted that a corporation is a thing (Evermann & Wand, 2005). However, BWW does not explain how an institutional entity can be a thing despite it not being a phys ical entity, although perhaps possible to perceive as such. We assume, based on Wand et al. (1999), that a corporation is a conceptual thing similar to a bank account—that is, a corporation is a mental construct that is rea because it exists in someone's mind. Accordingly, there is also a Corporate-Owner class, which is a subclass of Cor poration, because one does not have to be a person to own a traffic vehicle as corporations can be owners too. Thus we have two subclasses: Person-Owns-Car and Corporation-Owns-Car, with no common superclass. This structure is in line with Parsons and Wand's suggestion that a 'car owner can be an individual or a company (two classes which might have no common superclass, and, therefore, no common class based identifier)' (Parsons & Wand, 2000) Figure 4 depicts the complete conceptual model and how the model represents the real world.

![](/api/attachments/MEPYKPVE/fulltext/images/9903c282aaa1f527236b4fe18b3fbd8cc6191d3c577f9772db02a099a7731930.jpg)  
F I G U R E 3 A conceptual model of a person-owner and how the model relates to the real world [Colour figure can be viewed at wileyonlinelibrary.com]

Person and Corporation must be two classes because a Corporation-Person class makes no sense according to the BWW guidelines. There is simply no common physical property or set of properties between corporations and persons to form a Person-Corporation class. In other words, the classes Person and Corporation have different quali tative identities, which yields two distinct classes:

[Subclasses are] defined in terms of the scope of the conjunction of the property used initially to define the class and the additional property of interest. In short, subclasses are formed by 'adding properties to the set of properties possessed by things in a class. (Wand et al., 1999, p. 500)

Even when accepting corporations as existing in someone's mind, it is hard to find properties that identify a corporation. The natural construct to use to identify a corporation would be the corporate name. However, names of corpo rations are not a part of the conceptual model because identifiers have no significance for modelling the world according to the BWW guidelines. Parsons and Wand (2000) solve this problem of referencing and identifyin owners by introducing a surrogate key that links instances of the two classes in the database

[This approach] enables homogeneous reference to instances that may be considered to be of different types in the application [and] amounts to having a global instance identity [. . .], and each identifier serves as a surrogate designating the existence of a corresponding real-world thing. (Parsons & Wand, 2000, p 261)

![](/api/attachments/MEPYKPVE/fulltext/images/9c7f3b816b956ab373ba306f22a0ef449c693321c6a6e1d055166421774e04c5.jpg)  
F I G U R E 4 A conceptual model of car ownership without a common superclass [Colour figure can be viewed at wileyonlinelibrary.com]

However, this approach does little to explain how to use a an internal system-generated key that does not corre spond to a thing in the real world and consequently lacks meaning and significance to make a homogeneous refer ence and as such identify real-world things as unique owners. The surrogate key is meaningless because both the qualitative and the individual identities of persons and companies differ. The classes have different identifying prop erties, so the entities of these classes cannot be merged, which has consequences for even trivial tasks. For example, finding the number of owners requires both qualitative and individual identity of owners: to count, one needs to know what to count (Frege, 1892).

## 6 | CONCEPTUAL MODELLING AND INSTITUTIONAL REALITY

This section presents a worldview that emphasizes institutional reality as the modelling domain. To exemplify thi ontological foundation, we elaborate on the CVR and proceed to model the institutional entities that constitute a traffic vehicle ownership (Figure 7) and identify the differences compared to the BWW guidelines and the model in Figure 4.

## 6.1 | Institutional reality: The modelling domain

According to Habermas, reality is a combination of three worlds:

1. an objective world of things and their properties (Physical Reality in Figure 5);

2. a subjective world (Personal World in Figure 5), which is constituted by the feelings, beliefs, desires, perceptions, and intentions of actors; and

3. an inter-subjective social world (Social Reality in Figure 5), which is constituted by social interactions, social rela tionships, sentences, actions, traditions, cultural values, institutions, and speaking and acting persons (Habermas, 1976, 1984, 1985).

Institutional reality (the Modelling Domain in Figure 5) is a part of social reality, which is described in general terms by Habermas as 'objectivations with a semantical content' (Habermas, 1976, p. 90). The fundamental insight of an institutional ontology is that language (i.e., conceptual objects) not only describes reality but also uses it to constitut institutional reality (Searle, 1995), and these objects are created using language. They are, so to speak, 'spoken into existence' via speech acts, although today they are often created (registered) using digital media (see below)

To summarize, institutional reality and its constituents are different from physical reality. Consequently, ontology-based conceptual modelling must be sensitive to the existence of different worlds and ontologies. Institu tional reality should be understood in terms of a worldview that acknowledges the existence of institutional entities.

1. Physical reality consists of physical things, their properties, and natural laws. Physical things (brute facts) can b human-made things (artefacts) such as vehicles, natural 'dead' things such as mountains, and biological living things such as animals and physical persons.

2. Persons use their body, brain, and senses to conceive of physical things as objects, which are instantiations of concepts. Different persons can observe reality differently. Even the same observed physical thing can be identi fied differently by Person 1 and Person 2 in their respective personal worlds.

Social Reality  
![](/api/attachments/MEPYKPVE/fulltext/images/b88f4badcb44713a05b987dda181a7cd949a9bacbbe6156bcd8c14ba6b621e5a.jpg)  
F I G U R E 5 Summary of a worldview for modelling based on Habermas' three worlds

3. Not all physical things are observed.

4. Objects (conceptual objects) are externalized (instantiated in a language) and therefore made available for others to refer to and identify. The objects are language constructs (see the definition of conceptual objects in Section 2.2); they are not just part of the personal world as things in someone's mind. Objects constitute institutiona entities that are inter-subjectively understood and agreed upon. An object is an institutional entity if it also repre sents rights.

5. An institutional entity may be related to a physical thing by a correspondence relationship, but does not have to.

6. A physical thing may be related to one or several institutional entities.

7. An institutional entity does not have to relate to a physical thing.

The notion of institutional identity cannot be explained based on physical things and their properties. Institu tional identity does not have to refer to physical things and their properties. Institutional identity is inter-subjectiv and conceptual and based on the acknowledgement of two or more social actors. When there is a one-to-one corre spondence between a physical thing and an institutional entity, physical properties could be used as evidence of institutional identity. Still, physical proof of identity is not the same as institutional identity.

The institutional entities of interest and their possible relationships to physical things constitute the institutiona reality that is the domain of a conceptual model. Institutional reality (see F in Figure 5) is socially constructed. A such, it is different from physical reality and personal perceptions thereof (personal worlds) and the relationship between these worlds (see B in Figure 5).The aim of the worldview presented in this article is to emphasize the soci etal importance of institutional entities and identities (see 'F' above), which is in contrast to the BWW ontology, which focuses on 'B' in Figure 5. Institutional entities are conceptual objects referred to and identified using language that represent rights. Institutional entities are critical because they regulate social interaction across contexts, the are relational to their character, and they enable the re-identification of entities across socio-material contexts.

Today, the origin of institutional entities are created and often exist within digital infrastructures, which makes them very useful mechanisms for the distribution of rights and institutional change in society. Thus, the institutional entity within the digital infrastructure is the real one (Aakhus et al., 2014; Baskerville et al., 2020) created, stored, and maintained within a registry. A registry within an institutional context is a legitimate and official list (Beynon-Davies, 2016a) of institutiona entities. If digital, a centralized or decentralized database implements the registry. However, a registry and a database ar different concepts because a database is 'an organised collection of data' (Sundgren, 1973).

Accordingly, the purpose of conceptual modelling is not just to describe an already existing reality of things Conceptual modelling is a design activity in which modellers set up a framework of rules that enable people to under stand how they can construct or reconstruct institutional reality through the design of digital infrastructures. Conse quently, conceptual modelling of institutional domains should also consider the prescriptive role of conceptua models for digital infrastructures and society as a whole in the construction of the digital institutional reality. Digita infrastructures require appropriate formalization of their content. For example, storing information about traffic vehi cles requires a data-type level definition of a database schema. The required formalization is a complicated endeav our that requires a precise definition of the traffic vehicle class at the type level as well as the instance level Because of this formalization, conceptual modelling is often seen as a technical activity that belongs to the domai of software engineering and only of interest for database design using formal semantic modelling methods (Beeri, Bernstein, & Goodman, 1989). In contrast, we argue that conceptual modelling is critical for understanding and designing institutional reality, as conceptual models have a prescriptive role in its constitution.

## 6.2 | The central vehicle registry (CVR)

To exemplify the ontological foundation laid out above, we will elaborate on the CVR, which constitutes an essentia part of digital institutional reality in Sweden. Many organizations, including the police, insurance companies, vehicl owners, car dealers, and municipalities, use the registry. Increasingly, real-time tracking systems use the CVR as foundation for data-driven services. For example, the CVR has been instrumental in Sweden for developing systems for toll roads, speed camera systems, and so forth. The CVR functions as an attractor that generates the growth of the digital infrastructure (Hanseth & Lyytinen, 2010) because the institutional entities it contains are used in man contexts.

The primary institutional function of the CVR is to regulate road vehicle use, and the qualitative identity of the traffic vehicle class defines which vehicles should count as traffic vehicles. To count as a traffic vehicle, a vehicl must be safe to use on public roads. However, the classification rule is likely to cause debate as there will be differ ent interpretations. For example, should a motorized scooter be classified as a traffic vehicle? In Sweden, there was a heated debate recently about this because of motorized scooters involved in several accidents.

The STA must also have control of individual identifiers, such as the licence number, which represents a unique traffic vehicle. A physical road vehicle with a licence number is allowed to use public roads, and a vehicle without a licence num ber is not. Accordingly, it must be easy to identify a traffic vehicle. In Sweden, this identifier consists of three letters followed by two digits and an alphanumeric character. The licence number must also be attached to the physical vehicle so that it is visible and kept in such a condition that anybody can read it. Institutional identifiers such as the licence number are critical because they represent rights, regulate social interaction, and enable the identification of the same entity acros multiple contexts. Accordingly, institutional identifiers must be assigned carefully to ensure identity

In the case of the creation of a traffic vehicle entity, a strict routine guarantees that only legitimate vehicles are registered and assigned a licence number. However, there is a problem assigning owner numbers. Three numbers ar valid owner numbers: the personal identification (PID) number, the coordination number, and the organization number. PID numbers cannot be used to identify all owners, because only Swedish residents have a PID number; foreigners who stay only temporally in Sweden can be legal owners of traffic vehicles and a so-called coordination number iden tifies these foreign owners (Eriksson & Ågerfalk, 2010). Moreover, juridical persons such as corporations, identified by their organization number, can be owners. The problem with assigning owner numbers is the lack of rigid control. Th STA does not maintain an owner number of its own. Instead, the STA relies entirely on other authorities to provid legitimate identifiers to use as owner numbers. Swedish Police have found several cases where owners are created and assigned a coordination number within the CVR although the number did not correspond to a legitimate physical per son. In such cases, the coordination number used as a reference to the owner number is illegal.

The benefit of being assigned an illegitimate owner number is that the registered vehicle, which is linked to th owner number in the CVR, can never be traced back to any accountable person should the car be used for crimina purposes. The origin of the problem is that the STA sometimes assigns an owner number on a faked photocopy of a passport without having the person physically visiting the STA. The STA then sends an application to the Tax Agency, which assigns the coordination number. The STA relies on the Tax Agency to make a more accurate ID check of the person who is assigned a coordination number in the Civil registry. However, the Tax Agency refers to 5–6§ of Regulation SFS 1991:749, which prescribes that to request the assignment of coordination numbers, the applicant authority (e.g., the STA) must first have reliable evidence of the identity of the physical person

Securing the assignment of a legitimate owner number is a matter of identity management that cannot be understood as a mapping problem between the information system (the CVR) and the real world outside the system (Burton-Jones et al., 2017), because the illegitimate assignment of owner numbers in the CVR is not a data quality concern according to Wand and Wang (1996). '[T]he information system is only required to enable mapping into perceived states, not real states ' (Wand & Weber, 1996, pp. 91–92), that is, mapping into an accurate and complete representa tion of perceptions of a focal real-world phenomenon. Securing the assignment of legitimate owner numbers is not a problem of true or false as a correspondence theory of truth, assuming that a belief is true if there is a corresponding fact and false if there is not (Marian, 2020). In contrast, the problem should be understood as how institutional realit is to be constructed. Even if there is a true belief that a physical person corresponds to an owner, there are still othe phenomena that cannot be properly explained such as physical persons (front men) who have no assets and are regis tered as owners of several hundred traffic vehicles to avoid fines associated with illegal use of traffic vehicles

Accordingly, the designer of information systems and associated identity management systems must deal with how information systems and institutional control routines are designed in an integrated manner and how the world ought to be. A major problem with representation and the correspondence theory of truth is that they exclude the normative and the ought to be (Ågerfalk & Eriksson, 2011). The focus is solely on descriptions of the real world, which is insufficient fo understanding how institutional identities ought to be assigned and verified. The essential problem is that the STA and Tax Agency do not agree on which one is responsible for the reliable and legitimate assignment of coordination numbers, which calls for the development of policy and routines. Indeed, assigning illegitimate coordination numbers is a growing problem because many contexts other than vehicle ownership use these numbers as institutional identifiers.

To understand why the CVR is such an essential part of Sweden's institutional reality, we have to understand the concept of traffic vehicle ownership. Traffic vehicle ownership means that owners are responsible for paying road tax, fines, and road tolls to the STA (SFS 2019:370). Most notably, traffic vehicle ownership does not impl ownership in the economic and civil law sense. It only means ownership rights according to administrative law. Traf fic vehicle ownership is constituted by the registration certificate, which is deemed so critical by the European Union (EU) that all member states must have similar registration certificates (EU 1999/37/EC). The idea is that the EU harmonized registration certificate will enable free movement of international road traffic, increase road safety, and make illegal trade with vehicles more difficult. The identifier of the certificate is the certification number that iden tifies a unique certificate. The certificate must refer to one and only one traffic vehicle using the licence number and one and only one owner using the owner number (Figure 6).

## 6.3 | A conceptual model of the CVR institutional context

In this section, we model the digital institutional reality described above based on an institutional conception of identity (see the conceptual model in Figure 7).

In contrast to the BWW-based model in Figure 4, here the focus is not to model physical reality but institutiona reality. In addition to the CVR, a set of laws and statutes (EU 1999/37/EC; SFS 2001:559; SFS 2006:242; and SFS 2019:370) form the basis for the modelled classes. The Registration certificate class in Figure 7 represents the ownership, which has its own qualitative identity. The class Registration certificate represents an obligation of vehicl owners concerning vehicle use on public roads towards a state authority. It certifies that the vehicle can be used on public roads. It represents the power of the state authority of assigning the rights. Modelling an institutional entity such as a certificate, as a class goes against the BWW guidelines. These guidelines (Shanks, Tansley, Nuredini, Tobin, & Weber, 2008; Wand et al., 1999) stipulate that the association class should represent an interaction (a mutual attribute and, according to Evermann and Wand, '[a]n association class must not be associated with another class' (Evermann & Wand, 2005, p. 152). In Figure 4, car ownership is modelled as two association classes—that is, Person-Owns-Car and Organization-Owns-Car—with a mutual property licence number. However, we consider the Registration certificate a bona fide class because it has a critical institutional function in society, as explained above. An instance of a traffic vehi cle ownership should be uniquely identified and have explicit attributes and associations to other institutional entities.

We model Authority as a class. The qualitative identity of the institutional function of a state authority is an institutional entity that has the right to execute the power of the state towards citizens. In our case, Authority is concept based on the Swedish constitution (SFS 2011:109). In Sweden, each state authority has a unique institu tional name, which is decided by the government and instantiated through a government decision. In this case, th STA has the power to create and authorize the Registration certificate.

In Figure 7, Owner is modelled as a class because it has a qualitative identity: Owner means institutional entitie registered in a traffic registry having been assigned a set of rights towards a state authority, such as paying road tax fines, and road tolls. Thus, the qualitative identity of the institutional concept of Owner is different from the qualita tive identities of the Foreigner, Resident, and Organization classes. There should also be an owner number used to identify individual owners over which the STA should have full control because the traffic authority has to identif all owners reliably. The owner number could be a system-generated identifier. Still, it should be understood to be an institutional identifier with meaning and significance, and the STA has to validate the provided evidence of identit before assigning the owner number. They can, of course, rely on the organization number and PID number as part of such evidence, as these identifiers are assigned using rigid routines. However, in the case of the coordination num ber, it is evident that the STA cannot rely on that identifier and institutional entity for assigning owner numbers. In contrast to the BWW-based model in Figure 4, we model Owner as a class. According to BWW, the owner numbe is just a technical pointer in the database, not a common class-based identifier, and owner is modelled as two sepa rate subclasses, namely Person-Owner and Organization-Owner.

![](/api/attachments/MEPYKPVE/fulltext/images/767ba2eb8ed232117ec6a2b4847afa03354af75574ad31e5b277926c09e3f4fc.jpg)  
F I G U R E 6 Institutional context of the CVR and its relationships [Colour figure can be viewed at wileyonlinelibrary.com]

We model Traffic vehicle as a class based on its qualitative and individual identity, as described in Section 6.2 The institutional function of the Traffic vehicle class is that it should regulate that only safe and certified physica vehicles are used on public roads. In the model, the licence number identifies particular traffic vehicle institutiona entities in institutional reality. Notably, the licence number is not considered a mutual attribute of the two association classes, as is the case in Figure 4. In modelling the Traffic vehicle class, we also represent an optional association between the class Manufactured vehicle and the class Traffic vehicle. These are different classes because the qualitative identity of the class Manufactured vehicle is different from that of the class Traffic vehicle. A manufactured vehicle is a vehicle made and registered by a manufacturer and identified by the ISO-VIN. Not all Manufactured vehi cles are Traffic vehicles, and not all Traffic vehicles are Manufactured vehicles. Thus, a null association betwee these classes suggests that there can be Traffic vehicle entities not associated with any Manufactured vehicle enti ties, and vice versa. According to the guidelines of BWW, such optionality should not be a part of an ontology model because not having a mutual property should not be represented in the model.

![](/api/attachments/MEPYKPVE/fulltext/images/1e970bee89546629a10d8400172172d899ffb595309d68dd04099e5aacc727ff.jpg)  
F I G U R E 7 A conceptual model based on institutional entities [Colour figure can be viewed at wileyonlinelibrary.com]

## 7 | DISCUSSION

This article provides the first in-depth ontological analysis of what institutional identity can bring to conceptual model ling. In addition, this article provides a solid ontological grounding for identity management and the identity of things.

## 7.1 | Ontological grounding of institutional identity

Institutional identity and entity are critical constructs for conceptual modelling of institutional reality. Ontology aims to discover what objects or kinds of objects exist (Bricker, 2014). To answer this question, we have to understand the notion of identity. Accordingly, in conceptual modelling of institutional contexts, we must distinguish betwee (a) classes that are required for instantiating (i.e., referring to and identifying digital institutional entities); (b) institutional reality (i.e., institutional entities); and (c) physical reality, which includes physical things, their proper ties, and natural laws that may provide evidence of the existence of an identity of an institutional entity. The mode described in Figure 7 depicts this distinction. The model in Figure 4 does not include institutional reality because th model conflates the linguistic constructs that constitute institutional reality—that is, the institutional entities—wit physical things, things in someone's mind, and interaction between things. In Figure 4, institutional reality is invisible.

The models in Figures 4 and 7 are different because they rely on separate notions of object existence and identity Figure 7 uses an institutional notion of identity as compared to the BWW ontology (Figure 4), which adopts a property based notion of identity. A property-based notion of identity assumes the following: (a) an object already exists in physica reality in the form of a physical thing or as a conceptual thing in someone's mind (a mental construct); (b) qualitative identit is based on property types; and (c) individual identity is based on property instances. In contrast, an institutional concept of identity assumes the following: (a) institutional entities first have to be instantiated (spoken into existence) in institutiona reality using classification rules; (b) qualitative identity is based on their institutional function in social interaction; and (c) individual identity is based on an institutional identifier used together with the class. Institutional entities within a clas are similar because they share the same institutional function in society and not because they have a common property Together, the identifier (e.g., licence number) and the class (e.g., Traffic vehicle) represent individual identity.

Moreover, institutional identifiers are essential not only because of their identification function but also because they represent rights, which is something the BWW ontology largely overlooks. In the BWW ontology, institutiona identifiers, such as a licence number, are considered mutual properties. However, describing, for example, a licenc number as a mutual property obfuscates its important identification function and its institutional function to repre sent rights and to regulate social interaction. The BWW ontology embraces the idea that one should model and describe only existing things and their properties, not rights.

From an institutional perspective, conceptual modelling aims to formalize rules for social interaction. We suggest an institutional approach that assumes the substrate of institutional reality be constituted by digital institutional enti ties (Iannacci, 2010). In such a context, conceptual modelling aims to model and formalize an institutional language to be used in the creation of digital institutional entities

## 7.2 | Implications for class selection

Practical digital infrastructure design needs to come to terms with the institutional and linguistic nature of digita artefacts. For conceptual modelling to be successful in an institutional context, one must understand how institu tional entities exist and how to identify them—that is, one must not conflate institutional entities with physica things. Models like the one depicted in Figure 7 could help designers and users see the critical difference betwee physical things and institutional entities as well as how they are interrelated.

Class-based modelling typically assumes class definitions that include comprehensive attribute structures expected to be stable over time (Lukyanenko, Parsons, & Samuel, 2019), what Eriksson, Johannesson, and Bergholtz (2019) cal an attribute-oriented view of classes. This view of classes is standard in conceptual modelling practice in software engi neering and has theoretical support by the BWW ontology. BWW design rule 3 states that '[a] class or a kind of thing i defined in terms of a given set of attributes and relationships; that is, intrinsic attributes and mutual attributes' (Wand et al., 1999, p. 511). Classes are ordered in hierarchies; superclasses are defined via generalization and subclasses via specialization (the is-a relation), adding attributes to the superclass. However, language-use theory shows that attribute are not used (Searle, 1969) to define classes, the language-use function of attributes predicate relevant informatio about the object, and they are not stable because attributes vary over time (see Section 4.1)

The language-use function of classes is to identify objects and not to describe them. A classification rule pre scribes which class name to use. This rule defines the class based on qualitative identity, thus determining whic objects should count as the same. There must also be an identifier to be used to identify individual entities that belong to the same class so that we can count the number of unique instances of the class—that is, numerical (indi vidual) identity. Accordingly, classes should not be defined in terms of a given set of attributes. The only compulsory requirement is that we need to know how to apply the class in communication and social interaction, for example, to count, but this does not require class definitions to consist of comprehensive attribute structures. An identity oriented view of classes avoids what Masolo, Vieu, Kitamura, Kozaki, and Mizoguchi (2011) calls 'is-a overloading', that is, overuse of the 'is-a relation' in domain models. An identity-oriented view of classes also helps to overcome some classical difficulties related to multiple classification and inheritance, especially in modelling roles (Halpin, 2016; Steimann, 2000). Modelling the owner as a bona fide class avoids this; we do not have to model an owner (a role) as a subclass of a person (a natural kind) as suggested by BWW. UFO forbids modelling a role as a separate class (Guerson, Sales, Guizzardi, & Almeida, 2015; Guizzardi, 2005). For example, a person class (a natural kind) should always be modelled as a superclass of a role. Accordingly, roles remain elusive entities in conceptual model ling (Masolo et al., 2011; Toyoshima, 2019; von Rosing & Zachman Sr, 2017).

The problem of modelling roles also relates to the counting problem (Toyoshima, 2019) for example, to count the physical thing in Figure 7 as 1, but count it as 2 when considering its roles of being a traffic vehicle and a manufactured vehicle. However, as we have explained in Section 4.1, there is no universal numerical identity inherent i a physical thing. Numerical identity depends on its meaning within a context and the numerical identity assigned to the objects one wants to count. As soon as we agree about the numerical identity (i.e., what to count), the countin problem disappears. As the model in Figure 7 depicts, if we decide that there is one physical thing, one traffic vehicle institutional entity, and one manufactured vehicle institutional entity, there is no counting problem. However, thi requires the instantiation of Traffic vehicle and Manufactured vehicle in a way that ensures the one-to-one corre spondence relationship with the thing, and that the association between Traffic vehicle and Manufactured vehicle i established. The establishing of the association between a Traffic vehicle institutional entity and a Manufactured vehicle institutional entity means that they are institutionally grounded (Eriksson et al., 2018). Institutional groundin is an association among entities that expresses existential dependencies among them. Using grounding instead o generalization (Steimann, 2000) helps to distinguish and count entities.

Accordingly, the proposed view of classes helps to resolve many problems related to role modelling, because, in institutional contexts, institutional functions, not natural kinds or property types, determine class definitions. In institutional contexts, roles should not be modelled as subclasses of persons (human things) and non-human things. How ever, persons and non-human things can act as agents in the name of an institutional entity, using institutiona identities assuming roles. It is critical to identity management to understand the relationship between institutiona entities, on one hand, and human and non-human things, on the other

## 7.3 | Implications for identity management and IoT

Identity management (Bertino & Takahashi, 2010) and Identity Management and Access (IAM) systems (Benantar, 2005; Bertino & Takahashi, 2010; Cameron & Williamson, 2020) are at the heart of digital infrastructures. Digital identity is the foundation for building security mechanisms, such as authentication and authorization (Zhu & Badr, 2018). According to the Y.2720 standard, digital identity consists of three parts: identifiers, credentials, and attributes. In digita infrastructures, things are identified and authorized to perform certain actions. The creation of the identity may require various credentials as proof of identity possession (Benantar, 2005). The authorization mechanism identifies them as institutional entities, which qualifies them to perform actions associated with those entities. Using digital institutiona entities allows identification of things and connecting them to a digital network of human and non-human agents (Hanseth & Monteiro, 1997). Accordingly, identity management is about managing digital institutional entities.

Identity management involves the creation of a digital institutional entity stored within a centralized or distrib uted register, for example, creating a user or a traffic vehicle. Creating an institutional entity must assign a uniqu identifier value. In the case where the entity must correspond to a thing, the creation of the institutional identity must link the identifier to a physical thing. The institutional entity may also reguire that some attributes are assigned to make it useful in a particular context. To ascertain the validity of the digital entity, one may also have to provid references to other already existing institutional entities. After its creation, the identity must be validated to ensur that the institutional entity referred to exists, which is often performed by direct access to a register. Validation may also include authentication, credentials that ensure trust in the identity (Benantar, 2005). For example, authenticatio with username and password may give a human agent the right to use a digital service. Authentication could also happen by providing a digital certificate. Authentication is necessary because it assigns the right to the agent to per form actions using the institutional identity, acting in the name of the institutional entity.

As IoT becomes increasingly critical, there is a need for new conceptualizations of how to manage the IDoT IDoT (Zhu & Badr, 2018) will require new ways to manage identity and to understand digital institutional identity IoT connects embedded systems in physical things (Beverungen, Müller, Matzner, Mendling, & Vom Brocke, 2019) to a worldwide communication network of other things. For example, vehicles move things with data processing and communication capabilities to obtain data about their physical surroundings and connect to other things within digi tal infrastructures (e.g., toll collection and navigation systems). Mobile apps allow the registered driver to use digita institutional identifiers, such as the VIN Code, to identify a smart vehicle within the digital infrastructure. For example, Volvo uses the VIN Code to identify smart vehicles, and a person is allowed to use only the Volvo On Call (VOC) app if the person is recognized as the primary driver or has the primary driver's explicit and undisputed consent to use the service. The primary driver is the person 'who has the right to dispose of it, uses it in a permanent manner as a means of transport, and/or is registered as the keeper of the car with a national authority (if any)' (Volvo Ca Group, 2017). The infrastructure should adhere to international standards and regulations to ensure information exchange with drivers, other vehicles, road infrastructure, different manufacturers, and service provider (Beverungen et al., 2019). In their role as institutional entities, intelligent products, such as a smart vehicle, becom part of digital-institutional reality. In Sweden, for example, new regulations for automated vehicles have recentl been proposed (SOU 2018:16). These regulations suggest that the smart vehicle's identity and the time frames when automated driving is activated and deactivated will have to be stored. The same goes for when the vehicle request the driver to take over driving. Thus, institutional identity will be even more critical as a constitutive part of emerging artificial intelligence-based infrastructures. Moreover, many different identities in intelligent transport systems do not have to be related to a human thing (person). It is crucial to decide which identity is allowed to communicate to what, and what information is needed or collected. Such decisions must factor in the institutional context. Accord ingly, the need for connecting things in IoT infrastructures leads to the idea of IDoT (Opentext, 2018; Parkin-White, 2020). The vast number of things with an identity requiring secure connectivity will pose challenges to designers of identity management systems (Zhu & Badr, 2018).

IAM systems have been unable to meet new requirements because of the focus on persons (users (Opentext, 2018). As IDoT becomes increasingly critical, there is a need for new conceptualizations of how to man age the identity of all network entities, not only users. Conceptually, IAM systems are typically based on roles (Cameron & Williamson, 2020) and attributes of users such as role-based access control (RBAC) (Ferraiolo, Cugini, & Kuhn, 1995) where each role assigns a collection of permissions to users. However, RBAC systems suffer from role explosion because of overuse of is-a relations (see Section 7.2). With attribute-based access control (ABAC (Hu et al., 2013; Kuhn, Coyne, & Weil, 2010), user permissions are instead assigned based on various attributes pres ented by a user. This approach is more flexible than RBAC because it does not require separate roles for relevant sets of user attributes, which avoids role explosion and therefore allows for a rapid implementation to accommodat changing needs. However, Leibniz's Law, where a set of attributes identify individuals (Zhu & Badr, 2018), govern many current identity management solutions. Leibniz's law is typically understood to mean that no two things share the same properties. Leibniz also restricts this principle to physical things, which means that the principle is grounded in a property-based conception of identity (Forrest, 2020; Zhu & Badr, 2018). Therefore, to design modern IAM sys tems, the key is to understand the notion of digital institutional identity and how to model institutional reality.

## 8 | CONCLUSION

In this article, we set out to propose an ontological grounding of institutional identity that can help answer the fol lowing question: How should we model the world to develop, implement, use, and maintain digital infrastructures in the construction and change of institutional reality? To answer this question, we investigated conceptual modelling with an institutional understanding of identity. Symbolic action theory, primarily Searle's speech act theory, informed our analysis. Such an approach helps one understand information systems

as vehicles for mediating and organising social interactions by maintaining and manipulating symbols that may exist independently of physical representations but at the same time retain fidelity to physical reality, if and when needed. (Aakhus et al., 2014, p. 1198)

To establish how such an understanding makes a difference, we performed a comparative analysis with the modelling guidelines associated with the BWW ontology. The study made it clear that a property-based conception of identity, as embraced by BWW, falls short when it comes to modelling institutional entities that originate in digital infrastructure rather than in physical reality. It is refreshing to see recent publications addressing these limitations of the receive ontological view in IS (Recker et al., 2021). However, to embrace fully the current ontological reversal (Baskervill et al., 2020), an epistemological add-on to received notions of representation is not enough. Conceptual modelling needs a full linguistic and institutional turn that acknowledges the institutional nature of contemporary digital technol ogy and abandons the outdated assumption that physical reality always takes priority. Fundamentally, a property-based view of identity assumes already existing things that can be described in models and information systems.

On the contrary, an institutional view of identity recognizes that entities are institutional constructs created within digital infrastructures based on agreed-upon institutional functions, rules, and norms. Understanding th notion of institutional entity and identity and the institutional context in which they exist are fundamental if one wants to understand the meaning of contemporary digital institutional reality. Such understanding is also required to appreciate the role digital infrastructures serve in constituting digital institutional reality. Conceptual modelling can open up the black box of digitalization by providing valuable knowledge about the digital transformation of institutional reality (Baskerville et al., 2020; Beynon-Davies, 2018; Clarke et al., 2016; Eriksson et al., 2018; Lemieux & Limonad, 2011; March & Allen, 2014). In this article, we have shown that achieving such knowledge requires an insti tutional understanding of identity, which is essential in order to understand fully the contemporary ontological reversal in IS. A 'physical first' approach can never achieve such an understanding because a property-based view on identity asks us to focus on already existing physical things and their observable properties rather than on the institutional structures that shape how entities are created, identified, and used in society.

It seems conceptual modelling has received less credit in the IS field recently (Wand & Weber, 2017) and is ofte considered a technology-related activity belonging to the domain of software engineering. A revival of conceptua modelling is timely and much needed. An institutional turn is motivated because of the massive societal impact of digitally implemented classes and institutional entities. These models form shared conceptions for meaning creation through social interaction in the construction of contemporary digital institutional reality. Who would be bette suited to study this development than IS scholars?

## DATA AVAILABILITY STATEMENT

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## ORCID

Owen Eriksson https://orcid.org/0000-0002-2024-9474

## REFERENCES

Aakhus, M., Ågerfalk, P. J., Lyytinen, K., & Te'eni, D. (2014). Symbolic action research in information systems: Introduction to the special issue. MIS Quarterly, 38(4), 1187–1200

Ågerfalk, P. J. (2020). Artificial intelligence as digital agency. European Journal of Information Systems, 29(1), 1–8.

Ågerfalk, P., & Eriksson, O. (2011). The stolen identifier: An inquiry into the nature of identification and the ontological status of information systems. In ICIS 2011 proceedings

Baskerville, R. L., Myers, M. D., & Yoo, Y. (2020). Digital first: The ontological reversal and new challenges for information systems research. Management Information Systems Ouarterly, 44(2). 509–523

Beeri, C., Bernstein, P. A., & Goodman, N. (1989). A sophisticate's introduction to database normalization theory. In Readings in artificial intelligence and databases (pp. 468–479). Morgan Kaufmann.

Benantar, M. (2005). Access control systems: Security, identity management and trust models. Springer Science & Business Media.

Bera, P., Burton-Jones, A., & Wand, Y. (2014). Research note-how semantics and pragmatics interact in understanding conceptual models. Information Systems Research, 25(2), 401–419.

Bertino, E., & Takahashi, K. (2010). Identity management: Concepts, technologies, and systems. Artech House

Beverungen, D., Müller, O., Matzner, M., Mendling, J., & Vom Brocke, J. (2019). Conceptualizing smart service systems. Elec tronic Markets, 29(1), 7–18

Beynon-Davies, P. (2016a). Form-ing institutional order: The scaffolding of lists and identifiers. Journal of the Association for Information Science and Technology, 67(11), 2738–2753.

Beynon-Davies, P. (2016b). Instituting facts: Data structures and institutional order. Information and Organization, 26(1–2) 28–44.

Beynon-Davies, P. (2018). Declarations of significance: Exploring the pragmatic nature of information models. Informatio Systems Journal, 28(4), 612–633.

Bird, A., & Tobin, E. (2018). Natural kinds. In E. N. Zalta (Ed.), The Stanford encyclopedia of philosophy, The Metaphysics Research Lab Center for the Study of Language and Information Stanford University. (Spring 2018 Edition). https:/ plato.stanford.edu/archives/spr2018/entries/natural-kinds,

Boell, S. K., & Cecez-Kecmanovic, D. (2015). What is an information system? In 2015 48th Hawaii international conference on system sciences (HICSS), ieeexplore.ieee.org, pp. 4959–4968.

Bricker, P. (2014). Ontological commitment. Stanford Encyclopedia of Philosohy, The Metaphysics Research Lab. https:/ plato.stanford.edu/entries/ontological-commitment/

Bueno, O. (2014). Why identity is fundamental. American Philosophical Quarterly, 51(4), 325–332

Bunge, M. (1977). Treatise on basic philosophy: Volume 3: Ontology I: The furniture of the world. Boston: Reidel

Burton-Jones, A., Recker, J., Indulska, M., Green, P., & Weber, R. (2017). Assessing representation theory with a framework for pursuing success and failure. MIS Quarterly, 41(4), 1307–1333

Burton-Jones, A., & Grange, C. (2013). From use to effective use: A representation theory perspective. Information Systems Research, 24(3), 632–658.

Cameron, A., & Williamson, G. (2020). Introduction to IAM architecture. IDPro Body of Knowledge, 1(2), 1–18

Clarke, R., Burton-Jones, A., & Weber, R. (2016). On the ontological quality and logical quality of conceptual-modeling gram mars: The need for a dual Perspectiv. Information Systems Research, 27(2), 365–382

Date, C. J. (2004). An introduction to database systems (8th ed., International ed.). Boston, MA: Addison-Wesley.

Chen, P. P. S. (1976). The entity-relationship model—Toward a unified view of data. ACM Transactions on Database Systems (TODS), 1(1), 9–36.

Dummett, M. (1981). Frege: Philosophy of language. Harvard University Press.

Eriksson, O., & Ågerfalk, P. (2010). Rethinking the meaning of identifiers in information infrastructures. Journal of the AIS, 11 (8), 433–454.

Eriksson, O., Johannesson, P., & Bergholtz, M. (2018). Institutional ontology for conceptual modeling. Journal of Informatio Technology, 33(2), 105–123.

Eriksson, O., Johannesson, P., & Bergholtz, M. (2019). The case for classes and instances-a response to representing instances: The case for reengineering conceptual modelling grammars. European Journal of Information Systems, 28(6) 681–693.

EU 910/ 2014. On electronic identification and trust services for electronic transactions in the internal market and repealin Directive 1999/93/EC. Regulation of the European Parliament and of the council.

EU 1999/37/EC. Council directive 1999/37/EC of 29 April 1999 on the registration documents for vehicles. https://eur-lex europa.eu/legal-content/EN/ALL/?uri=CELEX%3A31999L0037

Evermann, J., & Wand, Y. (2005). Ontology based object-oriented domain modeling: Fundamental concepts. Requirements Engineering, 10(2), 146–160.

Ferraiolo, D., Cugini, J., & Kuhn, D. R. (1995). Role-based access control (RBAC): Features and motivations. In Proceedings of 11th annual computer security application conference, pp. 241–248

Forrest, P. (2020). The identity of indiscernibles. In E. N. Zalta (Ed.), forthcoming The Stanford encyclopedia of philosophy, The Metaphysics Research Lab Center for the Study of Language and Information Stanford University. (Winter 2020 Edi tion). https://plato.stanford.edu/archives/win2020/entries/identity-indiscernible

Frege, G. (1892). Über sinn und bedeutung. Zeitschrift für Philosophie und Philosophische Kritik, 100, 25–50.

Guerson, J., Sales, T. P., Guizzardi, G., & Almeida, J. P. A. (2015). OntoUML lightweight editor: A model-based environment to build, evaluate and implement reference ontologies. In 2015 IEEE 19th international enterprise distributed object computing workshop, pp. 144–147.IEEE

Gruber, T. R. (1995). Toward principles for the design of ontologies used for knowledge sharing? International Journal of Human-Computer Studies, 43(5), 907–928

Guizzardi, G. (2005). Ontological foundations for structural conceptual models. (CTIT PhD Thesis Series, No. 05-74), Enschede The Netherlands

Guizzardi. G., & Wagner. G. (2o05). Some applications of a unified foundational ontology in business modeling. In Business systems analysis with ontologies, pp. 345–367.IGI Global.

Guizzardi, G., & Zamborlini, V. (2014). Using a trope-based foundational ontology for bridging different areas of concern i ontology-driven conceptual modeling. Science of Computer Programming, 96, 417–443.

Guizzardi, G., Fonseca, C. M., Benevides, A. B., Almeida, J. P. A., Porello, D., and Sales, T. P. (2018). Endurant types in ontology-driven conceptual modeling: Towards OntoUML 2.0. In International conference on conceptual modeling, pp. 136–150.Springer, Cham

Habermas, J. (1976). What is universal pragmatics? In M. Cooke (Ed.), On the pragmatics of communication. Cambridge: Massachusetts Institute of Technology.

Habermas, J. (1984). The theory of communicative action. Cambridge: Polity Press.

Habermas, J. (1985). Questions and Counterquestions. In M. Cooke (Ed.), On the pragmatics of communication. Cambridge: Massachusetts Institute of Technology.

Halpin, T. (2016). Object-role modeling workbook: Data modeling exercises using ORM and NORMA. Technics Publications

Hanseth, O., & Lyytinen, K. (2010). Design theory for dynamic complexity in information infrastructures: The case of build ing Internet. Journal of Information Technology, 25(1), 1–19.

Hanseth, O., & Monteiro, E. (1997). Inscribing behavior in information infrastructure standards. Accounting, Management and Information Technologies, 7(4), 183–211

Henderson-Sellers, B., Eriksson, O., & Ågerfalk, P. J. (2015). On the need for identity in ontology-based conceptual modelling, keynote paper in Conceptual Modelling 2015. In Proceedings of the 11th Asia-Pacific conference on conceptual model ling (APCCM 2015), Sydney, Australia, 27–30 January 2015 (eds. M. Saeki, & H. Köhler), pp. 9–20.

Hohfeld, W. N. (1913). Some fundamental legal conceptions as applied in judicial reasoning. The Yale Law Journal, 23(1), 16–59.

Hu, V. C., Ferraiolo, D., Kuhn, R., Friedman, A. R., Lang, A. J., Cogdell, M. M., … Scarfone, K. (2013). Guide to attribute based access control (abac) definition and considerations (draft). NIST Special Publication, 800(162), 1–43.

Iannacci, F. (2010). When is an information infrastructure? Investigating the emergence of public sector information infrastructures. European Journal of Information Systems, 19, 35–48.

Kallinikos, J. (2011). Governing through technology: Information artefacts and social practice technology, work and globalisation. Basingstoke: Palgrave Macmillan.

Kuhn, D. R., Coyne, E. J., & Weil, T. R. (2010). Adding attributes to role-based access control. Computer, 43(6), 79–81.

Lemieux, V., & Limonad, L. (2011). What 'good' looks like: Understanding records ontologically in the context of the globa financial crisis. Journal of Information Science, 37(1), 29–39

Lukyanenko, R., Parsons, J., & Samuel, B. M. (2019). Representing instances: The case for reengineering conceptual model ling grammars. European Journal of Information Systems, 28(1), 68–90.

Lyytinen, K. (2006). Ontological foundations of conceptual modeling by Boris Wyssusek—A critical response. Scandinavia Journal of Information Systems, 18(1), 81–84.

March, S. T., & Allen, G. N. (2014). Toward a social ontology for conceptual modeling. Communications of the AIS, 34, 1347–1358.

Martinelli, F., Mercaldo, F., Nardone, V., Santone, A., & Vaglini, G. (2018). Real-time driver behaviour characterization through rule-based machine learning. In Proceedings of international vonference on vomputer safety, reliability, and security pp. 374–386.Springer, Cham

Marian. D. (2020). The correspondence theory of truth, In E N. Zalta (Ed) Retrieved from The Stanford encyclopedia of phi losophy. The Metaphysics Research Lab Center for the Study of Language and Information Stanford University. https:/ plato.stanford.edu/archives/win2020/entries/truth-correspondence

Masolo, C., Vieu, L., Kitamura, Y., Kozaki, K., & Mizoguchi, R. (2011). The counting problem in the light of role kinds. In AAA spring symposium. Logical Formalizations of Commonsense Reasoning.

Mead, G. H. (1934). Mind, self and society. Chicago: University of Chicago Press.

Merricks, T. (1998). There are no criteria of identity over time. Noûs, 32(1), 106–124.

Noonan, H. W. (2006). Identity and sameness: Philosophical aspects. In Concise encyclopedia of language and linguistics (philosophy and language volume) (pp. 302–304). Oxford: Elsevier Science

Noonan, H. W., & Curtis, B. (2018). In E. N. Zalta (Ed.), Identity. The Stanford Encyclopedia of Philosophy, The Metaphysics Research Lab Center for the Study of Language and Information Stanford University. (Summer 2018 Edition). https:/ plato.stanford.edu/archives/sum2018/entries/identity/

Opentext. (2018). The identity of things is here. https://blogs.opentext.com/the-identity-of-things-is-here/

Ostrom, E. (2011). Background on the institutional analysis and development framework. Policy Studies Journal, 39(1), 7–27.

Parkin-White, A. (2020). Five key points to think about with an identity of things solution. https://mobileecosystemforum.com 2020/06/11/five-key-points-to-think-about-with-an-identity-of-things-solution/

Parsons, J., & Wand, Y. (2000). Emancipating instances from the tyranny of classes in information modelling. ACM Transac tions on Database Systems (TODS), 25(2), 228–268.

Recker, J., Lukyanenko, R., Jabbari, M. A., Samuel, B. M., & Castellanos, A. (2021). From representation to mediation: A new agenda for conceptual modeling research in a digital world. MIS Quarterly, 45(1), 1–32.

Scott, W. R. (2001). Institutions and organizations. Thousand Oaks, CA: Sage Publications.

Searle, J. R. (1969). Speech acts. An essay in the philosophy of language. Cambridge: Cambridge University Press.

Searle, J. R. (1995). The construction of social reality. New York: The Free Press.

Searle, J. (1997). Responses to critics of the construction of social reality. Philosophy and Phenomenological Research, 57(2) 449–458.

Searle, J. R. (2005). What is an institution? Journal of Institutional Economics, 1(01), 1–22

Searle, J. R. (2006). Social ontology: Some basic principles. Anthropological Theory, 6(1), 12–29.

Searle, J. R. (2010). Making the social world: The structure of human civilization. Oxford: Oxford University Press.

SFS 1991:749. Folkbokföringslagen. In Swedish, Svensk Författningssamling, Sveriges Riksdag. https://www.riksdagen.se/sv/ dokument-lagar/dokument/svensk-forfattningssamling/folkbokforingsforordning-1991749\_sfs-1991-749

SFS 2001:559. Lag om vägtrafikdefinitioner. In Swedish, Svensk Författningssamling, Sveriges Riksdag. https://www.riksdagen. se/sv/dokument-lagar/dokument/svensk-forfattningssamling/lag-2001559-om-vagtrafikdefinitioner\_sfs-2001-559

SFS 2006:242. Vägtrafikskatteförordning. In Swedish, Svensk Författningssamling, Sveriges Riksdag. https://www.riksdagen. se/sv/dokument-lagar/dokument/svensk-forfattningssamling/vagtrafikskatteforordning-2006242\_sfs-2006-242

SFS 2011:109. Regeringsform. In Swedish, Svensk Författningssamling, Sveriges Riksdag. http://www.lagboken.se dokument/andrings-sfs/744017/sfs-2011\_109-regeringsform?pageid=93376

SFS 2011:755. Lag om elektroniska pengar. In Swedish, Svensk Författningssamling. https://www.riksdagen.se/sv/ dokument-lagar/dokument/svensk-forfattningssamling/lag-2011755-om-elektroniska-pengar\_sfs-2011-755

SFS 2019:370. Lag om fordons registrering och användning. In Swedish, Svensk Författningssamling, Sveriges Riksdag. https://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/lag-2019370-om-fordons registrering-och\_sfs-2019-370

Shanks, G., Tansley, E., Nuredini, J., Tobin, D., & Weber, R. (2008). Representing part—Whole relations in conceptual model ing: An empirical evaluation. MIS Quarterly, 32(3), 553–573.

SOU 2018:16. Vägen till självkörande fordon – introduktion Del 1. In Swedish, Statens offentliga utredningar. https://www. regeringen.se/49381d/contentassets/0fc1ef6f51794961b20c0c9a965164f6/sou-2018\_16\_del1\_webb.pdf

Stamper, R., & Ades, Y. (2004). Semantic normal form and system quality. In IEE conference on requirements engineering.

Steimann, F. (2000). On the representation of roles in object-oriented and conceptual modelling. Data and Knowledge Engi neering, 35(1), 83–106.

Sundgren, B. (1973). An infological approach to data bases. Stockholm University and Statistics Sweden, Urval No 7.

Sundgren, B. (2014). The OPR framework for conceptual modelling. Pro Libera Scio.

Swedbank. (2020). Privatkonto. In Swedish, https://www.swedbank.se/privat/kort-och-betala/konton-for-in-och utbetalningar/privatkonto.htm

Tilson, D., Lyytinen, K., & Sørensen, C. (2010). Research commentary—Digital infrastructures: The missing IS researc agenda. Information Systems Research, 21(4), 748–759.

Toyoshima, F. (2019). A foundational view on roles in conceptual modeling. In JOWO

Tsakalakis, N., Stalla-Bourdillon, S., & O'Hara, K. (2017). Identity assurance in the UK: Technical implementation and lega implications under elDAS The Journal of Weh Science, 3(3), 32-46

Volvo Car Group. (2017). Terms and conditions for services. http://volvo.custhelp.com/ci/fattach/get/360694/0/filename Terms+and+Conditions+for+Services\_3+en\_US\_173127\_171106.pdf

von Rosing, M., & Zachman, J. A., Sr. (2017). The need for a role ontology. International Journal of Conceptual Structures and Smart Applications (IJCSSA), 5(1), 1–24

Wand, Y., & Weber, R. (1993). On the ontological expressiveness of information systems design analysis and design gram mars. Journal of Information Systems, 3(3), 217–237.

Wand, Y., & Weber, R. (1995). On the deep structure of information systems. Information Systems Journal, 5(3), 203–223.

Wand, Y., & Wang, R. Y. (1996). Anchoring data quality dimensions in ontological foundations. Communications of the ACM, 39(11), 86–95.

Wand, Y., & Weber, R. (2002). Research commentary: Information systems and conceptual modeling—A research agenda Information Systems Research, 13(4), 363–376

Wand, Y., & Weber, R. (2006). On ontological foundations of conceptual modeling: A response to Wyssusek. Scandinavian Journal of Information Systems, 18(1), 127–138.

Wand, Y., & Weber, R. (2017). Thirty years later: Some reflections on ontological analysis in conceptual modeling. Journal o Database Management, 28(1), 1–17.

Wand, Y., Storey, V., & Weber, R. (1999). An ontological analysis of the relationship construct in conceptual modeling. ACM Transactions on Database Systems. 24(4). 494-528

Weber, R. (2003). Editor's comments: Still desperately seeking the IT artifact. MIS Quarterly, 27(2), iii–xi.

Weiner, J. (2004). Frege explained. Open Court.

Wirfs-Brock, R., & McKean, A. (2003). Object design: Roles, responsibilities, and collaborations. Addison-Wesley Professional.

Y.2720. Telecommunication standardization sector—NGN identity management framework. https://www.itu.int/rec/T-REC-Y. 2720-200901-I.

Zhu, X., & Badr, Y. (2018). Identity management systems for the Internet of things: A survey towards blockchain solutions Sensors, 18(12), 4215.

How to cite this article: Eriksson O, Ågerfalk PJ. Speaking things into existence: Ontological foundations of identity representation and management. Inf Syst J. 2021;1–28. https://doi.org/10.1111/isj.12330
