---
otero_id: 14444
otero_key: "AC7AMKWZ"
title: "Digital Institutionalization: The Case of E-Prescribing"
authors: "Owen Eriksson; Sten-Erik Öhlund"
year: "2024"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00845"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Volume 25 Issue 3

Article 8

2024

# Digital Institutionalization: The Case of E-Prescribing

Owen Eriksson , owen.eriksson@im.uu.se

Sten-Erik Öhlund

sten.erik.ohlund@gmail.com

Follow this and additional works at: https://aisel.aisnet.org/jais

# Digital Institutionalization: The Case of E-Prescribing

Owen Eriksson,<sup>1</sup> Sten-Erik Öhlund<sup>2</sup>

<sup>1</sup>Department of Informatics and Media Uppsala University, Sweden, owen.eriksson@im.uu.se <sup>2</sup>Department of Informatics and Media Uppsala University, Sweden, sten.erik.ohlund@gmail.com

## Abstract

Digital institutionalization processes are fundamentally changing society. They occur when rules and norms are encoded into a digital infrastructure and change practices. For institutionalization to occur, numerous actors must alter their behavior similarly, which accompanies a shift in infrastructural technology. Digital infrastructures and their design play a crucial role in institutionalization processes, as they enable and restrict social interaction in the exchange of digital institutional entities across contexts. Such entities are constitutive of digital institutional systems—medical prescriptions, money, insurance, and taxes are all institutional entities that have been digitalized. Although severa studies have described the challenges of digital infrastructure design, there has been little consideration of the institutional context that legitimizes the design. To fill this research gap, we applied the critical perspective of designers, who intentionally perform and are responsible for the design and legitimacy of digital institutional systems. To address the challenge of institutiona design, we developed an exchange contract within an institutional context featuring a change in digital infrastructure and practices. Through this, we illuminate several design principles for digital institutionalization. This contribution captures critical design decisions and the knowledge acquired through insights gained from the design of a highly impactful scalable digital infrastructure, which ultimately transformed an institutional system. We also provide theoretical reflections informed by speech act theory and institutional theory and thereby emphasize the need to rethink institutionalization processes in an era of digitalization.

Keywords: Digitalization, Digital Institutionalization, Digital Infrastructure, Institution, Institutional Logics, Digital Practice, E-Prescribing

Tilo Böhmann was the accepting senior editor. This research article was submitted on September 16, 2019 and underwent five revisions.

## 1 Introduction

## 1.1 Background

Pervasive digitalization has become the “new” reality in our everyday lives. Digitalization can be defined as a “sociotechnical process of applying digitizing techniques to broader social and institutional contexts that render digital technologies infrastructural” (Tilson et al., 2010, p.

2). It has resulted in practices and institutional orders that have become the new norm, as employees, customers, and citizens are now expected to use digitized services by default—anytime and anywhere (Schou & Hjelholt, 2019). Digitalization requires the design of scalable digital infrastructures (Tilson et al., 2010; Hanseth & Lyytinen, 2010; Monteiro et al., 2014), which must be designed in a deliberate manner to ensure their legitimacy and effectiveness.

From a designer’s perspective, Hanseth and Lyytinen (2010) defined an information infrastructure as “a shared, open (and unbounded), heterogeneous and evolving socio-technical system … consisting of a set of IT capabilities and their user, operations and design communities.” In line with Henfridsson and Bygstad (2013) and Osmundsen and Bygstad (2021),<sup>1</sup> we use the term digital infrastructure instead of information infrastructure. Digital infrastructure also refers to the generativity and scalability (Henfridsson & Bygstad, 2013) of digital infrastructures and their fundamental role in understanding digitalization (Tilson et. al, 2010).

Digital infrastructure design focuses on interoperability (Bygstad & Hanseth, 2016; Edwards et al., 2007; Eriksson & Goldkuhl, 2013), e.g., the ability to exchange information (Bowker et al., 2009) across contexts. Bowker and Star (1999, p. 291) noted that designers experience “a permanent tension between the formal and the empirical, the local and the situated, in [their] attempts to represent information across localities.” Consequently, digital infrastructure design implies difficult challenges because of its sociotechnical complexity and diverse use and design contexts (Hanseth & Lyytinen, 2010; Tilson et al., 2010), and a growing number of scholars have heeded the challenges of digital infrastructure evolution (Bowker et al., 2009; Edwards et al., 2009; Hanseth & Lyytinen, 2010; Henfridsson & Bygstad, 2013; Tilson et al., 2010; Monteiro et al., 2013; Constantinides & Barrett, 2014; Nguyen et al., 2017; Rolland, 2017; Hanseth & Bygstad, 2017; Karasti et al., 2018; Hanseth & Modol, 2021).

Hanseth and Lyytinen (2010, p. 2) defined the challenge of evolving a digital infrastructure as a tension between two design problems: (1) the bootstrap problem, which involves initiating the digital infrastructure (bootstrap phase) so that it gains momentum, and (2) the adaptability problem, which involves adapting the infrastructure to new contexts to shift to a period of rapid growth (adaptation phase). However, failures are common and incur huge losses in investments as well as problems for society (Hanseth & Lyytinen, 2010). A principal reason for failures is that these critical moments are difficult to anticipate and plan for; thus, deliberate design is challenging (Edwards et al., 2009). Consequently, scholars have argued that infrastructures cannot be designed top-down, because the control of their evolution is distributed and episodic (Edwards et al., 2009; Hanseth & Lyytinen, 2010; Bygstad & Øvrelid, 2020). A bottom-up approach has been promoted, with some studies starting to nuance the picture as a solely bottom-up process (Osmundsen & Bygstad, 2021). Moreover, the institutional context has not been accounted for, although Monteiro et al. (2014) note that design choices may be heavily shaped by the institutional context.

Digitalization, however, which requires scalable digital infrastructures, is also a matter of intentional and topdown design because digital infrastructures need to be legitimate and in compliance with the institutional context. Even digital infrastructures that have evolved successfully and are considered effective could be criticized for lacking legitimacy due to “abusive design” (Calo & Rosenblat, 2017, p. 655). However, a digital infrastructure not only has to adapt to the institutional context but also change it.

Digital infrastructures are fundamental for institutionalization processes, as institutionalization occurs when many agents alter their behavior in a similar way (Barley & Tolbert, 1997). This is most likely to occur “with a shift in an infrastructural technology” (Barley & Tolbert, 1997, p. 111), and the shift from analog to digital infrastructures is decisive. It is an ongoing phenomenon that is transforming society. Therefore, we seek to address the general problem of “digital institutionalization” and propose the following research question:

## RQ: How can a digital infrastructure be designed that enables the development of a digital institutional system?

We applied the perspective of designers, i.e., those responsible for the design, evolution, and legitimacy of a digital institutional system. In this article, we exemplify digital institutionalization by presenting the evolution of e-prescribing in Sweden as a case of digital institutionalization. In Sweden, the adoption rate of e-prescribing is now 99%, representing one of the three most successful cases of e-prescribing in Europe and the world (Kierkegaard, 2013; Aanestad et al., 2017; Pereira et al., 2018). However, this has taken a long time and has been challenging. From a technical standpoint, this long journey may come as a surprise as this is just a matter of changing the medium of a medical prescription from an analog paper medium to a digital one. Therefore, it is of interest to uncover why this process was so time-consuming and challenging.

This case is of general interest because it is an example of a purposeful and successful design endeavor. A highly impactful, scalable digital infrastructure was designed, which ultimately transformed the institutional system. Our analysis of this case captures key moments and decisions in the process of designing a digital institutional system. The design work can be described as institutional design, which means “deliberately creating and changing institutions, and affecting institutions, institutional structures and practices” (Alexander, 2005, p. 213).

The article is organized in line with the suggested pattern for a design science article (Gregor & Hevner, 2013). In Section 2, we position our contribution, introduce basic concepts from institutional theory, and discuss how they relate to digital infrastructures. In Section 3, we present the research setting, describing the research approach of action design research (ADR; Sein et al., 2011; Sein & Rossi, 2019) and our motivation for choosing it. In Section 4, we present the designed artifact (i.e., an exchange contract, which defines the rules for exchange) and describe how it was implemented and evaluated. In Sections 5 and 6, we present the notion of digital institutionalization and propose design principles for digital institutionalization. Finally, in Section 7, we reflect on the validity and implications of our contribution, evaluate the research process and the limitations of the study, and suggest further empirical investigation and theory development for digital institutionalization.

## 2 Institutions and Digital Infrastructure Evolution

In Section 2, we first elaborate on how the evolution and design of digital infrastructures have been explained in the digital infrastructure literature. Second, we introduce concepts from institutional theory and the notion of institutional design. Third, we describe how an institutional system is constituted. Finally, we identify the knowledge gaps that motivated our contribution.

## 2.1 Digital Infrastructure Design and Evolution

In this section, we review prominent theoretical lenses that have been used to explain the design and evolution of digital infrastructures. We discuss if and how these lenses incorporate the institutional context or institutional theory in their explanations.

Actor-network theory (Latour, 1987) has been prominently used to explain how networks of social and technical elements drive digital infrastructure evolution—a process through which multiple human actors inscribe their interests into the digital infrastructure, creating an evolving network of human and nonhuman actors (Aanestad and Jensen, 2011; Hanseth & Monteiro, 1997; Yoo et al., 2005). Using gateways to make a digital infrastructure grow bottomup is a key principle of infrastructure evolution; for example, it allows different local applications to be joined to an existing infrastructure with minimal constraints using different versions of a standard (Edwards et. al., 2007; Hanseth, 2001).

In a case study of hospitals that implement electronic patient record (EPR) systems, Hanseth and Monteiro (1998) observed how the institutional context, in the form of governmental regulations, determined the content of and access to patient records, thereby affecting practices and the digital infrastructure. They provided valuable insights into how behavior is inscribed into the digital infrastructure and illuminated the emergent bottom-up aspect of social structures and infrastructures. However, they did not explain if and how the institutional context enabled a top-down evolution of the infrastructure.

Complex systems theory (Holland, 1995) is also prominent in explaining digital infrastructure evolution. It views the evolution process as a process by which heterogeneous actors seek to use the infrastructure to adapt to each other and their external environments (Braa et al., 2007; Ciborra et al., 2000; Hanseth et al., 2006; Hanseth & Lyytinen, 2010). It focuses on architectural principles, such as modularization, gateways, and flexible standards, as attractors that cause the digital infrastructure to bootstrap and adapt from the bottom up. When these mechanisms create generativity and the digital infrastructure scales up, a sociotechnical order emerges (Hanseth & Lyytinen, 2010). However, the complex systems perspective accounts for neither the institutional context nor the top-down role of predefined institutional structures (e.g., regulations) in enabling digital infrastructure evolution.

Critical realism (Bhaskar, 1997) was used by Henfridsson and Bygstad (2013) to explain the contingent causality of the aforementioned emergent bottom-up feature of digital infrastructure evolution. They used a biological metaphor to explain such evolution, viewing the success of a digital infrastructure as survival in a volatile business ecosystem. Their contribution was to identify generative mechanisms (similar to attractors) that create a generative force that causes the bootstrapping and adaptation of digital infrastructure.

Notably, digital infrastructures are conceived as biological entities that adapt to their environment, emerging from the bottom up; therefore, institutional theory has unsurprisingly not yet played a prominent role in explaining their evolution. Nevertheless, some studies have analyzed this evolution using institutional theory (Currie & Guah, 2007; Kimaro & Sahay, 2007; Sahay et al., 2010; Mekonnen & Sahay, 2008; Vila-Pozo & Sahay, 2019). Their main focus has been on how the institutional context in the form of standards restricts evolution or on how conflicting institutional logics block evolution. In these studies, which describe failures, the institutional context has prevented the evolution of the digital infrastructure; consequently, no scaling up has occurred. Sahay et al.’s (2018) study is of particular interest as they provided guidelines for redesigning institutions. However, their guidelines were formulated at a high level of abstraction, exemplified by the following quote: “Develop systems with an open architecture, with the ability to share data across institutional borders, using hybrid solutions that combine information technology and paper, and using online solutions that also offer offline support.” (p. 75)

In summary, the literature review demonstrates that the institutional context and its enabling and legitimizing role in the design of digital infrastructures have not been accounted for and that development projects cannot be centrally controlled. Consequently, the literature has focused on evolutionary processes and the emerging bottom-up aspect of digital infrastructures rather than the concrete work required to design one (Rolland, 2017). Furthermore, researchers have largely been passive observers rather than active designers, resulting in descriptive and explanatory theories. Therefore, there are almost no prescriptive theories that are relevant to intentional design processes, with Hanseth and Lyytinen (2010) being the exception.

Prescriptive theory represents knowledge of humanbuilt artifacts and how to design them (Gregor & Hevner, 2013, p. 343). The design theory of Hanseth and Lyytinen (2010) is relevant because it recognizes the fundamental role of the installed base and the path dependency of digital infrastructure design. Hanseth and Lyytinen (2010) defined the design challenge in the bootstrap phase as creating attractors that cause the infrastructure to start growing, and in the adaptation phase as avoiding technology traps—that is, uninformed design decisions that could hamper the growth of the infrastructure later on. They considered standards as attractors that could enable evolution. However, they focused on technical standards and they also assumed a bottom-up approach. Moreover, they did not consider regulations and the legitimacy of the design. Consequently, they did not explain how the institutional context could enable a top-down design and guarantee its legitimacy or how the design of digital infrastructures could change institutional systems.

## 2.2 Institutional Theory

This section introduces institutional systems, institutionalization, and institutional design. These concepts are used to develop the prescriptive theory of “digital institutionalization” in Sections 5 and 6.

Neo-institutional theory views institutions as constituted by abstract, symbolic, and social structures and institutional logic that govern social interactions and practices (Barley & Tolbert, 1997; Thornton et al. 2012). An institution is a system that works at the macro- and microlevels (Thornton et al., 2012). The microlevel consists of practices comprising forms of socially meaningful actions that are coherent and established (Thornton et al., 2012, p. 128). These practices reproduce the institutional system when they enact the institutional logic, which constitutes the macrolevel.

To demonstrate that a system has become an institutional system, it should follow an institutionalization process (Mignerat & Rivard, 2015, p. 117). This could be characterized by the following actions: (1) rulemaking, (2) best-practice development, and (3) rule changes, or the replacement of old rules with new ones (Keman & Rogers, 2017). Accordingly, the process concerns institutional design (Goodin, 1998). This serves as the means to devise and implement social structures at the macrolevel “that will enable and constrain behavior and action so as to accord with held values, achieve desired objectives, or execute given tasks” (Alexander, 2005, p. 213). Accordingly, the evolution of human institutions, unlike involuntary biological evolution, is the product of intentional decisions, even when designers do not anticipate all potential consequences (Alexander, 2005). In other words, institutional systems do not only emerge in a bottom-up fashion. Rather, to become an institutional system, the designed institutional logic must also be enacted (reproduced) at the microlevel. The social objects that are reproduced have to diffuse; thus, they must spread and become embedded in practices and populations of organizations across multiple contexts at the microlevel (Hasselbladh & Kallinikos, 2000, p. 709). However, reproduction does not mean that actors are intentionally aware of the institutional logics that govern their actions or that they intend to change the system.

Accordingly, reproduction is essential for but different from the institutionalization process, which unfolds between the macro- and microlevels (Barley & Tolbert, 1997; Thornton et al., 2012). It starts by encoding institutional logics into scripts, such as technical designs or formal rules, which subsequently prescribe action patterns at the microlevel. Revision of the scripts will be more likely to lead to institutional change if the actors at the microlevel intentionally attempt to change them, compared to script revision through unintended deviations from the logics. Moreover, changes in technology will increase the odds of actors realizing that they must change the institutional system (Barley & Tolbert, 1997).

In institutionalization processes, actors search for legitimacy for their practices (Deephouse & Suchman, 2008). Legitimacy is characterized as applying norms that are generally perceived as valid. Suchman (1995, p. 574) defined legitimacy as follows: “Legitimacy is a generalized perception or assumption that the actions of an entity are desirable, proper, or appropriate within some socially constructed system of norms, values, beliefs, and definitions.” Normative legitimacy implies doing the right thing (Suchman, 1995), which means that actions should comply with rules and beliefs about socially constructed value systems. Pragmatic legitimacy relates to criteria such as effectiveness, utility, and diffusion (Bitektine & Haack, 2015; Deephouse & Suchman, 2008).

## 2.3 The Constitution of Institutional Systems

To design, one must know what is to be designed. Accordingly, one must understand more about how an institutional system is constituted.

## 2.3.1 Rules and Norms

Language presupposes the existence of institutional systems (Searle, 2006, p. 14); likewise, rules and norms, which constitute institutional logics, are linguistic constructs. Norms are based on values and some form of assessment of what is considered right or wrong, i.e., what is considered legitimate. There are two types of rules: regulative and constitutive rules (Hindriks, 2009). Regulative rules (Ostrom, 2011) stipulate what actions are required, prohibited, or permitted and by whom. Constitutive rules define the conditions that must be met in a particular context to classify, create, identify, and maintain institutional entities (Hindriks, 2009). To apply regulative rules, constitutive rules are required since one must know which institutional entities are being referred to.

## 2.3.2 Institutional Entities

According to Searle (2005; 2006), the whole purpose of having institutions is to create and distribute deontic powers and institutional entities. We use the term “rights” instead of Searle’s term “deontic powers” based on the typology of rights presented by Hohfeld (1913). Hohfeld defined types of rights, such as claim and duty, as well as powers and privileges.

Institutional entities enable actions to be performed in society because institutional entities represent rights. Examples of institutional entities are organizations, juridical persons, bank notes, driver licenses, insurance, taxes, contracts, prescribers, pharmacists, and medical products (Searle, 2006). Since they are symbolic and linguistic constructs, institutional entities must be represented.

An institutional entity can be defined as having the following characteristics:

• created at a certain point in time using predefined constitutive rules

• represented using some kind of media

• conveys meaning

• has an identity

• represents facts

## • represents rights

Institutional entities are constitutive of institutional systems. They are created in practices (Searle 2005) at the microlevel and coordinate social interaction (Habermas, 1976).

## 2.3.3 Digital Institutional Entities as Constitutive of Digital Infrastructures

It has also been acknowledged that digital institutional entities are a constitutive component of digital infrastructures (Beynon-Davies, 2016; Eriksson and Ågerfalk, 2010; Iannacci, 2010). Still, the majority of the literature has focused on the software component (Pipek & Wulf, 2009, p. 469) or the services they provide (Osmundsen & Bygstad, 2021). However, it is not software but rather digital institutional entities that are exchanged across contexts. We argue that institutional entities are created and exchanged when an institutional system is reproduced. This creation and exchange of institutional entities makes institutional systems diffuse.

A registry is an official list of institutional entities (Beynon-Davies, 2016) that must conform to constitutive rules; if the registry is digitized, it is stored in a database. However, a digitized registry should not be confused with a database, which is “any collection of data, or information, that is specially organized for rapid search and retrieval by a computer” (Gregersen et al., 2020). Institutional entities are fundamental entities of institutional systems and digital infrastructures, and their reproduction is dependent on standardized symbolic schemes (Hasselbladh & Kallinikos, 2000), which we refer to as constitutive rules.

Digital institutional entities are a type of “rationalized package,” and they must be reproducible and durable. To be reproducible means that institutional entities need to be created according to formalized constitutive rules. This standardized character stabilizes the meaning of institutional entities, thus blocking alternative interpretations (Hasselbladh & Kallinikos, 2000). Durable refers to the ability to withstand being transferred from one context to another without distortions (Hasselbladh & Kallinikos, 2000).

Institutional entities should be reproducible and durable, but they must also be communicable. This means that they “can cross an institutionalized field be understood and conveyed to others than those involved in its conception, construction and initial use” (Hasselbladh & Kallinikos, 2000, p. 710). Still, we are aware that unambiguous reproduction and interpretation are not possible, especially when institutional entities are created and exchanged across contexts.

We conclude that digital institutional entities should be the focus of digital infrastructure design. Therefore, it is necessary to include more pragmatic communication theories, such as speech act theory, in such design (Searle, 1969, 1995, 2006; Habermas, 1976).

## 2.4 A Gap in the Literature

We have identified a main gap in the infrastructure literature, which is a lack of emphasis on the enabling role of the institutional context and institutional entities in digital infrastructure design and evolution. This leads to an insufficient understanding of the interrelated relationship of digital infrastructure design and institutionalization processes. This is in stark contrast to our data and experiences from the design work that we have engaged in, where the institutional context and institutional entities have been at the heart of the design.

## 3 Research Setting

In Section 3.1, we describe the institutional system in the case study. Then, Section 3.2 presents the bootstrap phase, which precedes the institutionalization phase. Lastly, Section 3.3 presents the research method and describes how our research process has unfolded over the years.

## 3.1 The Case Study

The institutional system in our case study is medical product prescribing in Sweden, which includes: (1) the practice of issuing a prescription and dispensing it at a pharmacy and the infrastructure used (the microlevel) and (2) the rules and norms (the macrolevel). The rules and norms are specified in several regulations and standards, which constitute the institutional context of the case study.

An example of a regulative rule is the rule the prescriber must comply with when issuing a prescription: “Instruction regarding dosage, use and treatment purpose should be described in such a way that the patient is able to use the medication … in a correct way” (HSLF-FS 2021:75, ch. 4, §7). Another example is the regulative rule that the pharmacist must comply with when dispensing the prescription: “When dispensing a prescription, a pharmacist must provide information and advice … and perform the other tasks that are of particular importance for the safe handling and use of the medicinal product” (HSLF-FS 2021:75, ch. 8, §1). To apply the regulative rules, constitutive rules are required, since the actors must know how to classify and identify someone or something as a prescriber, patient, pharmacist, or medicinal product (referred to in the regulative rules) and also how to create new institutional entities (e.g., a new prescription). For example, one norm is that the institutional system should contribute to patient security and the effectiveness of the practice.

We refer to the old institutional system, which was based on an analog infrastructure involving writing paper perscriptions, as “paper prescribing.” Moreover, we refer to the new institutional system based on a digital infrastructure as “e-prescribing” and the digital prescription as an “e-prescription.”

## 3.2 Bootstrap Phase of E-prescribing in Sweden

The evolution of e-prescribing in Sweden is divided into two major phases: the bootstrap phase from 1983 to 2003 and the institutionalization phase from 2004 to 2017. The beginning of e-prescribing in Sweden (Åstrand et al., 2007) dates back to 1983, when the world’s first electronic prescription was sent from a general practitioner’s office to a local pharmacy. From 1983 to 2000, there was no real growth. In the 1990s, the 21 county councils responsible for healthcare in Sweden focused on the implementation of EPR applications at the local level to support the local practice of general practitioners at primary care centers. On the pharmacy side, the National Pharmacy Company (NPC), a state-owned company with a monopoly in the pharmacy market, implemented a pharmacy system (ATS) at all Swedish pharmacies in 1985.

In 2000, NPC initiated a project to implement eprescribing on a larger scale. As a result, the share of e-prescriptions of all prescriptions increased from 17% to 32% during 2003-2004. With this growth, new requirements emerged to improve the quality of eprescriptions and ensure compliance with the old exchange contract, which defined the structure and content of the e-prescription entity. With the growth in volume, even a few errors in e-prescriptions would cause problems, such as lines of patients at pharmacies.

In 2004, the National E-prescription Format (NEF) project was initiated to meet requirements for improved quality, seen as crucial for the system to scale up. The purpose of the project was to design and implement the NEF, which was also the name of the new exchange contract. A project group was also established with participants from NPC and some county councils to develop a new and improved exchange contract. A new certification process for approving e-prescribing modules was also developed. Figure 1 presents the institutionalization phase and the NEF intervention.

![](/api/attachments/AC7AMKWZ/fulltext/images/4152299cb545e86f81e33bad0626d51b9159f25aa2b296c707a7c18877ceae81.jpg)  
Figure 1 The Institutionalization Phase and the NEF Intervention

## 3.3 Research Method

## 3.3.1 Motivation

Our aim was to study the institutionalization of eprescribing in Sweden, which spans a long period, starting in 2004 with the NEF project. Accordingly, we performed a longitudinal study. However, since there are few examples of design research (Ågerfalk 2014; Gregor & Hevner, 2013; Gregor, 2014) in the digital infrastructure literature, scholars have limited ability to scrutinize the design process and the history that gave rise to it. Accordingly, a design research (DR) approach is more appropriate if one’s aim is to study how design work is performed in the evolution of a digital infrastructure.

Based on our experience in design projects, the choice of which DR method to use is not always obvious at the start—precisely because the research approach evolves over time and only becomes clear in restrospect. Examining our research process in retrospect, we can ascertain that we have followed the principles of ADR.

ADR is a research approach for generating design knowledge through building and evaluating IT artifacts (Sein et al., 2011; Sein & Rossi, 2019). It consists of four stages: (1) problem formulation; (2) building, intervention, and evaluation; (3) reflection and learning; and (4) formalization and learning. We now describe how the design process unfolded, how the researchers were involved in the design practice, and how they were engaged in the research process.

## 3.3.2 Problem Formulation (Phase 1 of ADR)

The start of an ADR study (Sein et al., 2011) is a problem perceived in practice (Sein and Rossi 2019). In 2003, Author 2 was engaged at NPC as a service leader for the e-prescribing support team. The role included solving day-to-day problems, creating incident reports, and managing emerging issues. The work involved contact with actors at different sites, including county councils, local pharmacies, and the NPC headquarters. As the service leader, Author 2 was responsible for the improvement in the quality of eprescriptions, which was seen as the most crucial requirement for scaling up the system. Author 2 realized that to resolve quality problems, the eprescribing practice had to change; he was able to convince the project group that this was not just a technical problem.

## 3.3.3 Building, Intervention, and Evaluation (Phase 2 of ADR)

Phase two of ADR comprises the building of the artifact, intervention in the organization, and evaluation of the intervention (BIE; Sein et al., 2011). In this case, artifact means “ensemble artifact,” which refers to “the material and organizational features that are socially recognized as bundles of hardware and/or software” (Sein et al., 2011, p. 38).

Prior to his engagement at NPC in 2003, Author 2 had worked for 12 years at an industrial research institute, where he also finished a licentiate thesis. His research was on business rules and continuous quality improvement.

He was well-acquainted with communication theories, especially pragmatics, such as speech act theory (Searle, 1969), and its application within systems development (Goldkuhl & Lyytinen, 1982; Winograd et al., 1986). This inspired him to define an explicit rule system, which was aligned with the regulations for creating valid eprescriptions—that is, rules were designed for how to perform a high-quality communication act (speech act). This was in line with ADR, which assumes that the researcher is actively inscribing theoretical elements into the artifact. The building of the artifact, namely the new exchange contract, is described in Section 4.

From the beginning, the official role of Author 2 was as the service leader, but he was also trained as a researcher and was thus well aware of the importance of documenting the design process and systematically gathering data about it. One important advantage of being an insider who was responsible for the design was that he obtained personal experience regarding the design work, the actual construction of the artifact, important design decisions, and the real-world conditions (e.g., time restrictions and uncertainties) in which the design occurred. Such access and experience would have been impossible to attain by merely observing or interviewing someone. His experiences were also helpful for understanding what was important in the design, such as insight into the importance of the quality of e-prescriptions.

Accordingly, data were systematically gathered and documented during the whole design process using field notes to register significant observations, which were also communicated by email to colleagues. Observations, ideas, and experiences were also discussed and presented at project meetings and in written memoranda. Other data sources were email conversations, minutes, routine descriptions, policies, regulations, and standards. The deliverables of the design process included specifications for the exchange contract, handbooks, conceptual models, annotated XML schemas, and test documentation. All of this material, which Yin (2009) referred to as a case study database, served as a valuable data source in the ADR process.

In 2006, the researcher role became official when Author 2 formally resumed his Ph.D. studies, and in 2007 he was granted research funding to evaluate the implementation of the exchange contract. The question at the time was as follows: How could the implementation of the new exchange contract be evaluated? The implementation included changes to both the digital infrastructure and the e-prescribing practice.

For several reasons, we considered a quantitative method to be the optimal choice for the evaluation: First, quality deficiencies pre- and post-intervention were identified as deviations from the rules of the new exchange contract. However, their scale was not known, meaning that measuring the scale of the deviations was of interest. Accordingly, in a quantitative study, we could treat the rules as the independent variable and compliance with these rules as the dependent variable. Thus, if rule deviations (errors) decreased, compliance with them would have increased, and it could be argued that the quality of the digital infrastructure had improved.

Second, the rules of the exchange contracts were formalized and could be automatically validated. Thus, software could be developed to analyze how the eprescriptions complied with the exchange contract. To compare compliance pre- and post-intervention, data were collected from the consecutive samples of one month of e-prescriptions produced before and after the implementation of the exchange contract. This provided a unique opportunity to evaluate the intervention in a controlled-like setting, which is known to be difficult to achieve in ADR projects (Sein et al., 2011). The implementation and evaluation of the intervention are described in Section 4.

## 3.3.4 Reflection and Learning (Phase 3 of ADR)

The third stage of ADR requires a conceptual move from building a solution for a particular instance to applying that learning to a broader class of problems (Sein et al., 2011). It is crucial to reflect on the design problem and context, theories chosen, and further evolution of the designed artifact, thereby ensuring that contributions to knowledge are identified. It is critical to adjust the research process and reflect on the increasing understanding of the artifact. This is based on the principle of “guided emergence,” which includes the ongoing evolution of the artifact.

In 2008, Author 1 started to work with Author 2. At the time, Author 1 was involved in another action design science project, designing a digital infrastructure in the public sector. Working with practical design problems, we saw similar design challenges in the NEF project and the public sector project. Author 1 was also wellacquainted with the digital infrastructure literature and the central challenges of digital infrastructure evolution; that is, how to design for interoperability across contexts and make digital infrastructure grow.

Thus, we realized that the NEF project could be understood as the design and evolution of a digital infrastructure (Hanseth & Lyytinen, 2004). Accordingly, to obtain an enhanced understanding of the evolution of the digital infrastructure and the role the NEF project played in that process, we performed a case study in 2012-2013. Documents about the evolution of e-prescribing in Sweden from the pioneering years (starting in 1983) up to 2013 were collected and analyzed. They were complemented by interviews with key informants from NPC and county councils about the implementation process. Moreover, in 2014, Author 1 was also involved in a case study at the Swedish eHealth Agency, where the state-of-the-art e-prescription was analyzed. Both case studies confirmed that the digital infrastructure had continued to grow after 2010 and that the NEF intervention was a key factor. Moreover, we realized how critical the quality of digital institutional entities was to the growth of the digital infrastructure; thus, we also became interested in using institutional theory. Based on our knowledge of how speech act theory relates to institutional theory and the creation of institutional entities (Searle, 1995: 2005; 2006; 2010), we used the lens of institutional theory to analyze the NEF project (Barley & Tolbert, 1997; Scott, 2008; Thornton et al., 2012). We realized that e-prescribing had fundamentally changed the institutional logics and practice and that this could be understood not just as a design of a digital infrastructure but as an instantiation of a digital institutionalization process.

## 3.3.5 Formalization and Learning (Phase 4 of ADR)

The aims of the fourth ADR stage are to further generalize the situated learning from the ADR project (Sein et al., 2011) and to capture the knowledge acquired in previous ADR phases. This phase captures knowledge about creating other instances that belong to the same class of problems and should be defined in several principles or strategies. Thus, we used the digital design infrastructure literature and institutional theory to consciously reflect on the design work (Section 4) and the evolution of e-prescribing over the years to define our theoretical contribution. The results are the model of digital institutionalization and the design principles, presented in Sections 5 and 6. Finally, we reflect on the validity and implications of the contribution in Section 7.

## 4 Design, Implementation, and Evaluation (Phase 2 of ADR)

Section 4 describes how the NEF project enabled the digital institutionalization process. Section 4.1 describes the design challenge, Section 4.2 presents the most important design decisions, and Sections 4.3 and 4.4 describe how the exchange contract was designed, along with its function as a governance mechanism for change. Next, Section 4.5 demonstrates the value of the designed artifact. Finally, Section 4.6 describes the changes made to the institutional context.

## 4.1 The Design Challenge

To understand the design challenge of transforming paper prescriptions to e-prescriptions, one must realize that this is not just a technical change of media. This is critical because paper prescriptions (see Figure 2) would not intuitively seem particularly difficult to transform into a digital form (see Figure 3).

Historically, a manual and analog paper-based infrastructure was used in Sweden. A regulation (LVFS 1997:10) prescribes that paper prescriptions must be made by an authorized prescriber of a manufactured medicinal product with the specific substance, dosage form (e.g., tablet), and strength (e.g., 50 mg.) identified with the unique marketed product name (e.g., Ternormin). The prescription is written on a specific type of paper document, which is then handed to a patient. A paper prescription is carried from a primary care center to any pharmacy by the patient where it is filled by a pharmacist, who dispenses the medication. A paper prescription is depicted in Figure 2 and an e-prescription in Figure 3.

![](/api/attachments/AC7AMKWZ/fulltext/images/b958ae961d73348b80e89aec551057ace1b0d5ae7696f32b1675d5acd1405947.jpg)  
Figure 2 Example of a Paper Prescription

![](/api/attachments/AC7AMKWZ/fulltext/images/c471b0ba8f0b6b9c201a2eab4aa3d8294bafe3fae24f32e37c5a5e1428903e4a.jpg)  
Figure 3 Example of an E-prescription Created with an E-prescribing Module

![](/api/attachments/AC7AMKWZ/fulltext/images/3b4bbccd3195af2051a17fc415e58dc5c0cb0fd2a0648f90a2090ff406bb565f.jpg)  
Figure 4. The Gateway Conversion of the E-prescription Entity

However, comparing the paper-based and digital practices reveals that they are quite different. A major difference is that an e-prescription is stored in the eprescription registry, where the pharmacist retrieves it, as opposed to being brought in by the patient. An eprescription is a digital institutional entity (Eriksson & Ågerfalk, 2010) that mediates the claim from a prescriber to any pharmacist, who is duty-bound to dispense the prescribed drug on demand. Thus, the eprescription stored in the registry (see Figure 3) now attains the status of the original and real institutional entity. Accordingly, the digital institutional entity, which coordinates the social interaction between the prescriber, pharmacist, and patient, exists solely within the digital infrastructure.

Historically, the paper prescription was considered the genuine entity, while the digital version stored in the prescription registry was only a copy. The transformation from paper to an e-prescription required a new kind of infrastructure as well as changes in the institutional context, practices, and people’s conception of an original prescription. This was obviously challenging; thus, the design endeavor should be understood as part of an institutionalization process.

## 4.2 Decisive Design Decisions

When the NEF project began, the quality of eprescriptions was poor, hampering the institutionalization process. The exchange of eprescriptions was based on the old exchange contract, which allowed too much flexibility in the structure and content of e-prescriptions. To cope with the variety of messages sent from different e-prescribing modules, a gateway was used (Figure 4). Its function was to fix and convert the varied incoming e-prescriptions before they were stored in the national e-prescription registry and ultimately retrieved by pharmacists using the dispensing module. Thus, the gateway’s function was to hide and fix errors, not to validate the e-prescriptions sent in.

The gateway fixes were based on knowledge of previously detected errors; however, errors were not reported systematically to the prescriber nor to software maintenance and support teams. Furthermore, the fixes made the gateway complex and difficult to maintain. To improve the quality of e-prescriptions, it was necessary for all sending e-prescribing modules to comply with the same restricted rules. Therefore, a new exchange contract was developed to meet these new exchange requirements, which was a decisive design decision. The crucial insights that guided the design of the new exchange contract were as follows:

• To discard the gateway and stop hiding errors

To introduce validity controls and push the control to the point where the e-prescription was initially created. This required the eprescribing modules and prescribers to comply with the new exchange contract.

## 4.3 Design of the New Exchange Contract

The design of the new exchange contract was based on the old exchange contract, in which two types of messages were allowed: one was based on the UN “Medical prescription message” standard (MEDPRE 2000) using EDIFACT syntax, and the other was based on XML syntax. A major design decision was made to phase out the EDIFACT message because it did not provide a simple and automated mechanism for validation, which XML can offer. The XML message was based on the Swedish implementation guide (SIS 2002) of the international pre-standard ENV 13607 (i.e., “Health informatics—Messages for the exchange of information on medicine prescriptions”). ENV 13607 and the Swedish implementation guide (SIS 2002) had to be interpreted in the context of national regulations and the practice in Sweden. In the design work, the concepts defined in ENV1607 and the regulations were made intelligible in the context of eprescribing. The goal of the design was to make the rules explicit, precise, and less ambiguous in terms of e-prescription creation. Consequently, the core of the new exchange contract defines several constitutive rules, which must be followed.

## 4.3.1 Classification Rules

A classification rule is a constitutive rule that prescribes which class name to use and defines the class. There must also be a reference mechanism—an identifier—that can be used to identify the entities within the class. Table 1 lists some of the main classes and their identifiers, which are derived from Häggström et al. (2007), who provided a basic document of the actual exchange contract designed in the NEF project. The e-prescription is a relational entity that refers to other entities; therefore, to create a new e-prescription entity, there must be references to already existing institutional entities. The classes constitute a critical part of the user interface (see Figure 3).

The prescription class represents a prescribing act identified with a PrescriptionItem ID, and each prescription entity (item) belongs to a prescription set, which could contain several prescriptions issued simultaneously. The prescription refers to a marketed product package using a Product ID as the identifier. Each package has a predefined amount (e.g., 100 tablets). The e-prescription must also refer to a prescriber, patient, and workplace to be valid. Correct references to a prescriber and a patient are essential for authentication and authorization, while the workplace reference is important to reduce the cost for the patient.

## 4.3.2 Rules for Creating an E-Prescription

Another set of constitutive rules was also designed for how to perform a high-quality communication act (speech act) and is presented in Table 2 (derived from Häggström et al., 2007; Öhlund, 2007). They were based on the classification rules in Table 1 as well as legal demands prescribed in several regulations (LVFS 1997:10; SFS 2002:160; SFS 2005:259). Notably, the user interface depicted in Figure 3 should comply with these rules.

The structure rules are critical for ensuring that the pharmacist and patients receive relevant information. From a practice perspective, the data rules are vital for securing the quality of the data content of the eprescription entity. For example, content in the field “Directions of use” must not be accidentally cut off or remain empty. Dynamic consistency rules are crucial for securing a match between the content of different elements, such as between the reimbursement status and prescribed package or a combination of packages. The identification rules are critical for confirming that an existing and authorized prescriber, patient, product package, and workplace are correctly referred to when the e-prescription is created.

The regulations were interpreted and the rules formalized in such detail that they could be used for automatic validation. Still, it must be emphasized that not everything can be automatically verified; thus, prescribers must be aware of how critical complying with the rules is when creating an e-prescription.

Table 1. The Classes of an E-Prescription

<table><tr><td>Class name</td><td>Identifier</td></tr><tr><td>Prescription</td><td>PrescriptionItem ID</td></tr><tr><td>Prescription Set</td><td>PrescriptionSet ID</td></tr><tr><td>Product Package</td><td>Product ID</td></tr><tr><td>Patient</td><td>PID Number</td></tr><tr><td>Prescriber</td><td>Prescriber Code</td></tr><tr><td>Workplace</td><td>Workplace Code</td></tr></table>

Table 2. Types of Constitutive Rules for Creating an E-Prescription

<table><tr><td>Type of rule</td><td>Description</td></tr><tr><td>Structure</td><td>Rules that define which fields (elements) are allowed to be used for the classes, which elements are mandatory, and how they should be grouped. They also define how the classes could be associated.</td></tr><tr><td>Data</td><td>Rules for securing data quality—i.e., rules for character length, data type and format, and mandatory content (not null) of elements.</td></tr><tr><td>Dynamic Consistency</td><td>Rules for securing the consistency of the content when the content of one element is dynamically dependent on that of other elements.</td></tr><tr><td>Identification</td><td>Rules for how to make references to already existing institutional entities, using identifiers such as Product ID, Patient ID, Prescriber Code, and WorkPlace Code.</td></tr></table>

## 4.3.3 Validation of the Rules

A main problem under the old system was that no common validation was performed. Thus, common and agreed-upon control specifications (Franklin et al., 2007) had to be developed. The basic idea was to check the compliance of the rules as early as possible in the practice process. Thus, common automatic controls were introduced in the e-prescribing modules to avoid systematic errors and train prescribers in the creation of high-quality e-prescriptions. The decision to implement automated validation required the definition of error types to be used in error messages. They were defined as deviations from the constitutive rules (see Table 3).

The error types were extensively discussed because they had to be clear to be communicated to different stakeholders. Errors such as the error type “Incomplete structure” need to be communicated to software maintenance and support teams; some such as “Missing directions for patient use” and “Invalid multiple choice” need to be communicated to the prescriber. Compliance with these rules is crucial to prevent ambiguities when pharmacists and patients interpret the e-prescription at the receiving end. Prescription errors could ultimately result in serious adverse drug reactions and even hospitalization (Åstrand et al., 2009). It is also important in terms of drug costs and service quality.

## 4.4 Governance Function of the Exchange Contract

The designed exchange contract was the key to improving the quality of e-prescribing. It functions both as a governance mechanism (Yasuda, 2018), and a quality norm for the digital infrastructure and digital practice.

## 4.4.1 Governance Mechanism for the Digital Infrastructure

The new exchange contract was used as a governance mechanism when the software modules and institutional entities were implemented. The new exchange contract was used as an application program interface (API) contract (a service contract; Kapferer & Zimmermann, 2020) when standardized modularized system-to-system services were certified and implemented. For example, based on the new exchange contract, a new XML schema and system-tosystem service was implemented (see Figure 5 below). A feedback mechanism (“Application error and acknowledge message”) was created, which reported whether the e-prescription was accepted and conformed to the rules of the exchange contract; deviations from the rules were reported as errors.

The structure and data rules (Table 2) of the exchange contract are encoded into an XML schema, which is used to validate the sent XML file (Figure 5). The dynamic consistency and identification rules (Table 2) of the exchange contract require online validation and direct access to the registers of digital institutional entities referred to in the e-prescription, such as the workplace, prescriber, patient, and product package (Figure 5). Using a more restricted exchange contract limits the variety of the e-prescriptions exchanged, and when all the e-prescription modules comply with the exchange contract the interoperability of digital infrastructure is improved.

## 4.4.2 Governance Mechanism for the Digital Infrastructure

The exchange contract is critical for ensuring the interoperability of the digital infrastructure; however, interoperability should be conceived of as the capability to perform social interaction across multiple practices. The exchange contract defines a digital practice interface (DPI) between prescribing and dispensing practices. The DPI clarifies the responsibilities of the parties involved in the exchange, and the exchange contract functions as a governance mechanism for social interactions. The exchange contract enables and constrains the digital practice that occurs in the social interaction between prescribers, pharmacists, and patients, which is mediated by the use of the digital infrastructure (Figure 6).

![](/api/attachments/AC7AMKWZ/fulltext/images/5b57f90ff229940b2bff4df6f9f4ad71a957e632047eacbc29017812aafdf8df.jpg)  
Figure 5. Exchange Contract as a Governance Mechanism for Implementing the Digital Infrastructure

![](/api/attachments/AC7AMKWZ/fulltext/images/db57891a980c2be7b7029374dec3a6309d70423c30dd59af1f9a2d0b8e61fcf4.jpg)  
Figure 6. Exchange Contract Defining a Digital Practice Interface

In 2006, a case study was performed at three pharmacies (Åstrand et al., 2009) before the new exchange contract was implemented, which recognized the quality deficiencies found in eprescriptions and how they affected the practice. From the start, the introduction of e-prescribing was expected to increase quality; nevertheless, it was demonstrated that this did not just occur because the media changed.

The old exchange contract under the old system was based on the institutional logic of the paper-based process, which placed the responsibility for manually validating e-prescriptions on pharmacists, who rigorously control e-prescriptions when they are dispensed. Accordingly, the results of the study (Åstrand et al., 2009) emphasized the role of pharmacists as gatekeepers who detect and correct e-prescription errors in the act of dispensing (see Figure 6). The conclusion was that improving the quality of e-prescriptions, based on automated validity checks of the prescribing act (see Figure 6), would increase the quality of e-prescriptions and improve patient safety. Thus, it is vital to systematically monitor the quality of exchanged eprescriptions. These insights guided the implementation and evaluation of the new exchange contract.

## 4.5 Implementation and Evaluation

The decision to implement automated validation required errors to be reported back to the e-prescription modules. The prescriber also needed to obtain positive feedback confirming that the e-prescription could be handled by pharmacies. The status of errors was also reported as either (1) warning (W), meaning that the e-prescription set has been accepted but a workaround will be needed to dispense the e-prescription, or (2) rejected (R), meaning that the e-prescription cannot be dispensed.

The error status directly impacted practice as it clarified which types of error led to rejection, thus motivating action from the healthcare side (the sending side). It also clarified other types of errors using warning feedback that could be handled by the pharmacy (the receiving side). Critical issues were how rejections should be communicated and managed on the healthcare side and which actions should be taken on the pharmacy side when confronted with a warning.

Moreover, a major decision was how to implement the rules of the exchange contract. One concern was that problems might occur with response times for prescribers due to more restrictive and automated controls. In addition, Author 2 had no knowledge of the number of errors at the time of implementation. Thus, he worried whether rejections might seriously disrupt the e-prescribing process.

One question that arose was: Would it be wise as a first step to just register errors and then gradually enforce rejections? This question was resolved through the county councils, which agreed that rejections should be enforced, meaning that an e-prescription with an error status of rejected would not be managed by pharmacists. There were two types of workarounds when pharmacists detected errors:

1. In the case of a warning error, the pharmacist could dispense the e-prescription but potentially had to perform several actions to resolve the error, such as talking with the patient, checking their medical profile, seeking information about the medication, making their own judgments, and/or correcting the e-prescription before dispensing.

2. In the case of a rejection error, the pharmacist could not dispense the e-prescription. Rather, they had to contact the prescriber, who could then send a new e-prescription or tell the pharmacist how to correct it before dispensing.

To measure the effect of the intervention, it was vital to measure compliance with the exchange contract before and after its implementation. Consecutive sampling was used to collect all incoming XML e-prescriptions during two periods:

Before implementation: April 3-May 3, 2008; sample size = 1,270,339 prescription sets containing 1,910,982 e-prescriptions

• After implementation: April 3 -May 3, 2009; sample size = 1,479,588 prescription sets containing 2,204,444 e-prescriptions.

The results revealed that the implementation greatly decreased the number of errors: Before the implementation, the percentage of prescription sets with at least one error was 98.6%, whereas after the implementation, it was just 0.9%. The total number of errors found under the old system was 5,970,737, compared with just 13,764 under the new system (Table 3). The main explanation for errors under the old system prior to the implementation of NEF was that incoming e-prescriptions were accepted without common automatic validity controls.

Under the new system, deviations from the rules have almost vanished. Some errors are still managed by pharmacists, namely errors with the (W) status, but these are much less frequent compared with the old system. Both the total reduction in errors and the fact that errors with status (R) never reach pharmacists in the new system demonstrate that the practice of eprescribing has changed. In the new system, quality control has been pushed from the act of dispensing to the act of prescribing (Figure 6). This was a major change in the e-prescribing practice on a mass scale. Accordingly, the social interaction performed using the digital infrastructure was institutionalized, as the practice had to comply with the rules and norms of the new exchange contract.

Table 3. Number of Errors before and after the Implementation of the Exchange Contract Distributed by Error Type and Status

<table><tr><td>Rule violated</td><td>Type of error</td><td>Errors under the old system</td><td>Errors under the new system</td><td>Difference</td></tr><tr><td>Identification</td><td>Incorrect code enumeration</td><td>1,704,100</td><td>26</td><td>-1,704,074</td></tr><tr><td>Structure</td><td>Element not defined in the exchange contract</td><td>1,175,861</td><td>20</td><td>-1,175,841</td></tr><tr><td>Data</td><td>Incorrect sign or format of element</td><td>1,131,238</td><td>522</td><td>-1,130,716</td></tr><tr><td>Data</td><td>Override of maximum length of element</td><td>904,278</td><td>61</td><td>-904,217</td></tr><tr><td>Structure</td><td>Incomplete element structure</td><td>311,871</td><td>524</td><td>-311,347</td></tr><tr><td>Data</td><td>Invalid data type of element, or element has no value</td><td>240,432</td><td>9</td><td>-240,423</td></tr><tr><td>Data</td><td>Less than minimum length of element</td><td>204,447</td><td>108</td><td>-204,339</td></tr><tr><td>Data</td><td>Less than minimum value of element</td><td>149,962</td><td>0</td><td>-149,962</td></tr><tr><td>Data</td><td>Incomplete prescriber facts</td><td>10,829</td><td>0</td><td>-10,829</td></tr><tr><td>Identification</td><td>Invalid Prescriber Code</td><td>6,279</td><td>425</td><td>-5,854</td></tr><tr><td>Dynamic consistency</td><td>No amount in patient fee</td><td>2,486</td><td>3</td><td>-2,483</td></tr><tr><td>Data</td><td>Incomplete or erroneous patient facts</td><td>895</td><td>7</td><td>-888</td></tr><tr><td>Identification</td><td>Invalid medicinal package identity</td><td>366</td><td>3755</td><td>3,389</td></tr><tr><td>Dynamic consistency</td><td>Prescription is not valid for controlled packages</td><td>16</td><td>5</td><td>-11</td></tr><tr><td>Dynamic consistency</td><td>Invalid multiple choice</td><td>14</td><td>273</td><td>259</td></tr><tr><td>Dynamic consistency</td><td>Missing directions for patient use</td><td>1</td><td>2</td><td>1</td></tr><tr><td>Dynamic consistency</td><td>Local pharmacy destination required</td><td>0</td><td>156</td><td>156</td></tr><tr><td>Total reject (R) status</td><td></td><td>5,843,075</td><td>5 896</td><td>-5,837,179</td></tr><tr><td>Identification</td><td>Incorrect account number for the patient fee</td><td>125,471</td><td>138</td><td>-125,333</td></tr><tr><td>Identification</td><td>Missing Work Place Code</td><td>1,184</td><td>132</td><td>-1,052</td></tr><tr><td>Dynamic consistency</td><td>Invalid reimbursement status for prescribed package</td><td>1,007</td><td>7,598</td><td>6,591</td></tr><tr><td>Total warning (W) status</td><td></td><td>127,662</td><td>7,868</td><td>-119,794</td></tr><tr><td>Grand total</td><td></td><td>5,970,737</td><td>13,764</td><td>-5,956,973</td></tr></table>

It was a relief for Author 2, the county councils, and NPC that such changes on a mass scale unfolded so smoothly because the decision to implement restrictive validation of the rules in the exchange contract was not without risk—this drastic step of moving from permissive to restrictive social interaction could have backfired. However, to avoid the risk, the implementation was approved by the county councils, while the prescribers were educated about why the practice had to change. Moreover, a survey of the pharmacies (Hammar et al., 2010) was conducted after the new exchange contract had been implemented in 2009. A majority of the respondents believed that e-prescribing is safe for patients, provides patient benefits, is cost‐effective for pharmacies, and contributes to improved communication and relationships among patients and prescribers. Accordingly, we argue that the changed system has pragmatic legitimacy and that the reduction of errors (see Table 3) demonstrates an increase in normative legitimacy.

Furthermore, the implementation of the new exchange contract made it possible to identify the sending eprescription modules, which was not possible under the old system. This made it possible to trace errors back to the e-prescription modules, improving the digital institutional system. We found that to continuously improve and maintain the digital institutional system, systematically monitoring errors is crucial (Azad and King 2008).

## 4.6 Changing the Institutional Context

The NEF project was a design project that changed the digital infrastructure and practice, making them compliant with the institutional logics specified in the new exchange contract. However, changing the infrastructure and practice was not sufficient. Those responsible for e-prescribing at NPC and those responsible for the practical design work in the NEF project worked together to propose changes to the registry law in 2004 in order to change the normative legitimacy of the e-prescription entity. At the time, the prescription registry law (Lag 1996:1156) did not allow e-prescriptions to be permanently stored. When one was dispensed, it was printed and deleted from the registry. Consequently, the law had to be changed to allow e-prescriptions to be stored and managed throughout their whole life cycle. This happened in 2005 when the prescription register law (SFS 2005:259, 2005, 3 §7) was changed, which was a first step toward legitimizing e-prescriptions as a real original institutional entity. This paved the way for the digital institutionalization process.

In 2009, at the end of the NEF project, e-prescriptions had become conventional because 80% of all prescriptions were e-prescriptions, and the practice converted paper prescriptions to e-prescriptions and vice versa. Thus, in practice, the e-prescription had gained the same status as an original institutional entity like the paper prescription. This convention triggered changes in the regulation (LVFS 2009:13), which officially granted e-prescriptions the same status as paper prescriptions. This change in legislation was an adaptation of the institutional context to practice. Consequently, the designers not only adapted their design to the institutional context but also initiated changes to the institutional context.

Since May 2021, pharmacies have been required to convert paper prescriptions into e-prescriptions, and beginning in May 2022, all prescriptions in Sweden must be e-prescriptions, as mandated by law (HSLF-FS 2021:75). When the digital institutional entity became collectively accepted as the original one, the institutional system became digitalized. Thus, the NEF project and the designed exchanged contract enabled the shift from paper prescribing to e-prescribing.

## 5 Digital Institutionalization

In Sections 5 and 6, we present the prescriptive theory of “digital institutionalization,” a middle-range theory that represents prescriptive knowledge, which is presented in a number of design principles (Gregor & Hevner, 2013). We use institutional theory and the findings from the case study to describe the process of digital institutionalization in Section 5 (illustrated in Figure 7), and we present the design principles in Section 6.

Digital institutionalization is the process of developing a digital institutional system by governing and changing a digital infrastructure and digital practices at the microlevel that will enable and constrain legitimate social interaction performed across contexts. It requires the institutional design of an exchange contract at the macrolevel, which must be legitimate in relation to the institutional context. It is a bidirectional process between the macro- and microlevels that requires adaptations and change at the macrolevel based on emerging errors and exchange requirements at the microlevel.

## 5.1 Macrolevel

The macrolevel is constituted by the institutional logic, which is defined by rules (constitutive and regulative) and norms that are documented in regulations and standards. The institutional logics influence how the regulations and standards that constitute the institutional context are formulated. Thus, exchange contracts are designed based on the institutional context. The rules must be formal and precise to enable them to be encoded into software modules and the registries of digital institutional entities. The constitutive rules in the exchange contract prescribe how digital institutional entities should be classified, identified, created, stored, and managed. Regulative rules prescribe who has the right to perform actions and define the interaction sequence of the practice process. The rules and norms defined in the exchange contract constitute a common value system and an accepted quality norm, and define compliance with the rules. The exchange contract is a script (Barley & Tolbert, 1997)—that is, formal rules that prescribe social interaction at the microlevel. The exchange contract functions as a governance mechanism and a quality norm for both the implementation of the digital infrastructure and the practices performed at the micro level.

## 5.2 Microlevel

The microlevel consists of digital practices, which are forms of meaningful, coherent social interactions that are established (Thornton et al., 2012, p. 128) using a digital infrastructure. At the microlevel, the digital institutional system is reproduced when digital practices are performed using software modules to create and manage digital institutional entities that are exchanged across contexts. Such entities are the generative mechanism that leads to the diffusion of the digital institutional system.

Formal codification makes digital institutional entities reproducible, durable, and communicable (Hasselbladh & Kallinikos, 2000 <sup>2</sup> ). In the e-prescribing case, the success of moving from permissive to restrictive compliance with formal rules makes this evident.

The outcome of the institutionalization process is the diffusion of institutional entities throughout society. Reproduction is essential for digital institutionalization processes because it is important that the rules of the exchange contract are enacted. The digital infrastructure has to be shared and used by a growing number of practices at the microlevel. However, this evolutionary aspect is not the same as digital institutionalization, which requires the deliberate design of exchange contracts and changing digital infrastructures and practices: A digital institutional system does not emerge from the bottom up only; it is a bidirectional process between the macro- and microlevels.

![](/api/attachments/AC7AMKWZ/fulltext/images/4d5151afbb3bebc418d89af7acad41687258ad97e5f7d5fc7baf3b229e124990.jpg)  
Figure 7. The Bidirectional Process of Digital Institutionalization

## 5.3 The Bidirectional Process of Digital Institutionalization

The digital institutional process is bidirectional (Barley & Tolbert, 1997) because the macro- and microlevels are recursively related. Consequently, a digital infrastructure cannot simply emerge and become legitimate from the bottom up.

First, an initial exchange contract is designed and implemented. However, it is crucial to obtain continuous feedback from users and other stakeholders since legitimizing the exchange contract at the macrolevel or the digital infrastructure and practice at the microlevel requires continuous adaptations over time. Consequently, the model features a feedback mechanism that feeds the institutional design with information about emerging exchange requirements and errors.

On the one hand, if errors are caused by deviations in the exchange contract, which implies a lack of normative legitimacy, the digital infrastructure and practice at the microlevel should be made compliant with the exchange contract at the macrolevel. On the other hand, if the exchange contract is not aligned with emerging exchange requirements at the microlevel, which implies a lack of pragmatic legitimacy, then it must be changed. The demands for changing the exchange contract may also lead to demands to change the institutional context of regulations and standards, as illustrated in the e-prescribing case. This is elaborated on in Section 6.1.

## 6 Design Principles for Digital Institutionalization

This section presents design principles for digital institutionalization that capture the knowledge acquired from the design work. The suggested design principles (DP) are:

DP1: Analyze the institutional context (6.1)

DP2: Design the exchange contract (6.2)

DP3: Ensure the quality and legitimacy of digital institutional entities (6.3)

## 6.1 Analyze the Institutional Context (DP1)

The institutional context, that is, the standards and regulations, are preconditions for institutional design (Eriksson & Goldkuhl, 2013; Iannacci, 2010) because the exchange contract and its related digital practice and infrastructure must be legitimate. Therefore, the design of an exchange contract and its implementation should consider the institutional context.

Standards and regulations are useful for balancing diverse exchange requirements. However, standards are often complex (Hanseth et al. 2006) and must be analyzed based on their applicability in a specific design situation. Thus, there is usually a need to decide which limited subset of a standard to use and how to use it as a basis for the design. Regulations differ from standards because they are compulsory, whereas standards are voluntary. Sometimes standards have been developed without considering regulations (e.g., national regulations) and a standard may therefore need to be adapted.

When analyzing regulations, designers’ and lawyers’ opinions may differ regarding how to interpret them. Therefore, the legitimacy of the design could be unclear (Eriksson & Goldkuhl, 2013; Erlingsdóttir & Lindholm, 2015). Typically, the arguments revolve around the normative versus pragmatic legitimacy of the design (Eiband et al., 2018) involving a potential conflict regarding what is “the right thing to do” (normative legitimacy) based on the regulations and the utility and effectiveness (pragmatic legitimacy) of the practice. This means that designers need to learn to interpret regulations and to be able to understand the rationality behind them.

However, designers may also criticize how regulations and standards are formulated and interpreted, even demanding changes in how they are interpretated, as the prevailing institutional context may become pragmatically illegitimate as new exchange requirements, disruptive technologies, innovations, and practices emerge. In such cases, the institutional context must be intentionally changed or reinterpreted to pave the way for or legitimate the design.

## 6.2 Design the Exchange Contract (DP2)

The focus of the design should be on the exchange contract. It should not only be designed from a technical perspective but also from a practice perspective. The exchange contract is an institutional and technical (ensemble) artifact (Sein et al., 2011). It defines the rules for exchange (Yasuda, 2018) and how they should be complied with.

The exchange contract defines

• the technical format for the exchange

• the constitutive rules, namely the conditions to be met for how to classify, identify, create, and manage institutional entities

• the regulative rules, which regulate who has the right to perform the actions in the practice process and interaction sequence

• the controls for validating the legitimacy of the institutional entities exchanged.

Furthermore, the implementation of an exchange contract requires the balancing of contradictory stability and flexibility requirements. This concerns the degree of latitude allowed before the rule system as a whole is fundamentally breached (Craig et al., 2017). Therefore, how to enforce the rules involves a challenging design decision.

Using gateways makes it easy for local applications to connect to the infrastructure, creating less restrictiveness in the bootstrap phase. Initially, designers may have limited knowledge of how the digital infrastructure can be used, with use behavior emerging when users start to use the digital infrastructure and learn by doing (Pipek & Wulf, 2009; Hanseth & Lyytinen, 2010). However, this flexibility comes at a cost (Hanseth & Monteiro, 1998), as it increases the complexity of gateway conversions, making the digital infrastructure more unstable and complex. Costs also emerge in the practice when institutional entities are not reproducible, durable, or communicable, which hampers the diffusion of institutional entities. Institutionalization is always associated with the standardization of social interaction, which contributes to reproducibility, durability, and communicability (Hasselbladh & Kallinikos, 2000).

## 6.3 Ensure the Quality and Legitimacy of Digital Institutional Entities (DP3)

Digital institutionalization requires institutional entities to be replicable, durable, and communicable across contexts (Hasselbladh & Kallinikos, 2000). This can be achieved by ensuring the quality and legitimacy of institutional entities. To accomplish this, automatic validity controls should be implemented when the institutional entity is created, which makes senders aware of their responsibility for the quality of the institutional entity and relieves the burden of error control at the receiving end. Errors in institutional entities should be defined as unintentional deviations from the rules of the exchange contract (i.e., a lack of normative legitimacy; Reason et al., 1998).

Furthermore, new exchange requirements should be continuously identified because the rules, exchange contract, or its enforcement may be inappropriate or may lack some kind of pragmatic legitimacy. Statistics about errors should therefore be gathered and combined with qualitative feedback to introduce changes to the digital institutional system. Moreover, errors and new exchange requirements should be made visible to both maintenance and support teams as well as users and be systematically managed (van Steenbergen et al., 2020) in order to promote continuous improvement. Consequently, support, operations, and maintenance routines are crucial for the legitimacy of the system and the institutionalization process.

## 7 Conclusion

In this section, we reflect on the contribution. In Section 7.1 we discuss the implications of the proposed prescriptive theory of digital institutionalization. In Section 7.2 we evaluate the research process and limitations of the study. Finally, in Section 7.3, we suggest further empirical investigations and theory development for digital institutionalization.

## 7.1 Implications

## 7.1.1 Digital Institutionalization

Our middle-range theory contributes to the urgent need to incorporate (Alzadjali & Elbanna 2020; Currie, 2011) institutional theory into IS research and use it to analyze larger institutionalization processes. The creation and exchange of digital institutional entities, such as prescriptions, patient records, products, purchase orders, money, insurance, taxes, reservations, and payments, as well as their legitimacy and quality, are fundamental for digital institutional processes.

Digital institutional entities are at the heart of these processes because of their generative power. To paraphrase Searle (2005, 2006), the whole purpose of having digital institutional systems is to create and exchange digital institutional entities that diffuse across society. Consequently, we assume that our findings are valid and transferable outside of the specific context of the Swedish e-prescribing case, although the complexity of the exchange and the requirements for compliance, legitimacy, and quality may vary between contexts. According to Hasselbladh and Kallinikos (2000, p. 709), while institutionalization and diffusion have been explained by the imitation or imposition of best practices by dominant organizations, the diffused objects themselves have seldom been considered.

This differs from how we describe digital institutionalization in this article. We describe the institutionalization process from the perspective of design—and of those responsible for the design, evolution, and legitimacy of a digital institutional system. These could be authorities but also other public and private actors organized into networks (Powell, 1990). Making these actors aware of their responsibility for the legitimacy of the system is critical.

Accordingly, this article contributes to the understanding of how digital infrastructures can be designed and be made legitimate within an institutional context and how the design of digital infrastructures enables the evolution of institutional systems. This is difficult because the design and implementation of new digital institutional systems often occur in a gray zone (Calo & Rosenblat, 2017). Consequently, the involvement of legal argumentation and interpretation (Bench-Capon, 2018) requires new argumentative skills on the part of designers (Aakhus, 2017). Additionally, it raises crucial challenges for regulators and lawyers, who must gain a deeper understanding of institutional design and how digital infrastructures can change institutional systems. This goes beyond a mere technical understanding of digital infrastructures (Mendling et al., 2020, p. 208) or the services they provide (Osmundsen & Bygstad, 2021). From an institutional design perspective, it is crucial to understand how digital infrastructures are constituted and can be used to change the institutional systems of society at large.

## 7.1.2 Validity of the Design Principles

The design principles presented in Section 6 fit within the cell of “New Solutions for Known Problems” of the DSR Knowledge Contribution Framework presented by Gregor and Hevner (2013) and result from the improved understanding of the problem and solution spaces. This knowledge represents the ability to clearly communicate the new artifact design and how the new solution differs from current solutions.

When we compared the diffusion of e-prescribing in Sweden with that of e-prescribing in other countries (Kierkegaard, 2013; Aanestad et al., 2017; Pereira et al., 2018; Hanseth & Modol, 2021), we found that Sweden is a world leader in this regard—one of the three most successful in Europe and the world. Thus, we can claim that the application of the design principles suggested in the article could also be seen as a success in comparison with international projects.

The successful design strategy involved analyzing the institutional context to design and implement an exchange contract, which guaranteed the legitimacy and quality of an important digital institutional entity. The practical implication is that to succeed with the design, the guidelines outlined in Section 6 should be followed. While they appear to have worked in practical design, we can never be completely certain about this because of contextual contingencies.

Nevertheless, we are convinced that if the designers had not performed intentional institutional design and not followed the design principles, the digital institutional process would not have developed as effectively as it did. We maintain that the guidelines secured the legitimacy of the designed institutional system and that these guidelines could not have been developed if we had only conceived the evolution of digital infrastructures as emergent and unintentional.

Consequently, the suggested prescriptive theory provides a novel approach to the design of digital infrastructures.

## 7.2 Evaluation of the Research Process

We believe that our design approach has enabled the development of a novel and unique contribution to digital infrastructure design.

The ADR approach combined with a longitudinal study made it possible to develop a deep and unique understanding of the design and evolution of an important digital institutional system. Participation in practical design is crucial because it provides new insights that would be difficult to acquire using other research approaches.

The role of Author 2 as an inside researcher assisted in developing a deep understanding of the institutional context of e-prescribing. Experience from conducting the design work and serving as the operational service leader, as well as reflections informed by theory on how to improve the service, gave rise to ideas on how to improve and evaluate the quality of the eprescription entity. Thus, the experience gained as an inside researcher had a major influence on both the design work and the development of both a research interest and the contribution. Reflecting on the design problem and its solution using digital infrastructure literature, speech act theory, and institutional theory was critical for identifying contributions to the knowledge base. The research process was also adjusted to reflect the increased understanding of the evolution of the digital institutional system over time.

Most importantly, however, without the engagement in practical design work, we probably would not have been able to develop crucial insights into how constitutive the institutional context is for the design of digital infrastructures or how important the legitimacy and quality of institutional entities are for the diffusion of the digital institutional system. The extant literature has not recognized the need for institutional design— not even in longitudinal studies on e-prescribing (see, e.g., Hanseth & Modol, 2021).

For most academic researchers, opportunities to apply their methods and theories in a realistic setting are few and far between. The unique opportunity provided by the longitudinal ADR study made it possible to apply theoretical knowledge (speech act theory) in the design of the artifact and to participate behind the scenes, capturing key moments and decisions in the process of designing a highly impactful digital institutional system. As Barley and Tolbert (1997, p. 100) stated:

To investigate how patterns of interaction lead to the emergence of a new institution is, to say the least, a formidable task. An enormous amount of luck or prescience are required to recognize an emerging institution and then gather data on relevant, ongoing actions and interactions. Moreover, historical or archival material will rarely contain the detailed data necessary for documenting the link between everyday acts and the creation of an institution.

## 7.3 Limitations of the Study and Future Research

The successful design and implementation of the exchange contract were not the only factors that made the NEF project a success, yet we were unable to elaborate on those other factors in this article. For example, political, financial, and organizational factors contributed to its success. The NEF project was driven by a network of participating organizations where control and responsibilities were divided among the parties. The project was also driven by parties that represented the practice side, namely NPC and the county councils. Accordingly, the politics and governance of digital institutionalization should be further investigated.

We maintain that this kind of research should build on participation in digital institutionalization processes in order to gain an inside view of the politics of digital infrastructure design. Such research should focus on (1) governing strategies and tactics for how to manage design projects and IT service management within a network of stakeholders and organizations, and (2) how designers can acquire the legitimacy, trust, and financial support from powerful decision makers, lawyers, organizations, and customers/citizens that will allow them to perform institutional design.

The e-prescribing case illustrates the need to rethink institutionalization processes in an era of digitalization. It demonstrates that the digital infrastructure is a powerful force for institutional transformation and change. Thus, digital institutionalization is a topic worthy of further empirical investigation and theory development.

## Acknowledgments

We would like to thank our senior editor, Tilo Böhmann, and the two anonymous reviewers for providing highly constructive and useful feedback, which allowed us to improve the manuscript substantially.

## References

Aakhus, M. (2017). The communicative work of organizations in shaping argumentative realities. Philosophy and Technology, 30(2), 191-208.

Aanestad, M., & Jensen, T. B. (2011). Building nationwide information infrastructures in healthcare through modular implementation strategies. The Journal of Strategic Information Systems, 20(2), 161-176.

Aanestad, M., Grisot, M., Hanseth, O., & Vassilakopoulou, P. (Eds.) (2017). Information infrastructures within European health care: Working with the installed base. Springer.

Alexander, E. R. (2005). Institutional transformation and planning: From institutionalization theory to institutional design. Planning Theory, 4(3), 209- 223.

Ågerfalk, P. J. (2014). Insufficient theoretical contribution: A conclusive rationale for rejection? European Journal of Information Systems, 23(6), 593-599.

Alzadjali, K., & Elbanna, A. (2020). Smart institutional intervention in the adoption of digital infrastructure: The case of government cloud computing in Oman. Information Systems Frontiers, 22(2), 365-380.

Åstrand, B., Hovstadius, B., Antonov, K., & Petersson, G. (2007). The Swedish National Pharmacy Register. Studies in Health Technology and Informatics, 129(1), 345-349.

Åstrand, B., Montelius, E., Petersson, G., & Ekedahl, A. (2009). Assessment of ePrescription quality: An observational study at three mail-order pharmacies. BMC Medical Informatics and Decision Making, 9(1), Article 8.

Azad, B., & King, N. (2008). Enacting computer workaround practices within a medication dispensing system. European Journal of Information Systems, 17(3), 264-278.

Barley, S. R., & Tolbert, P. S. (1997). Institutionalization and structuration: Studying the links between action and institution. Organization Studies, 18(1), 93-117.

Bench-Capon, T. J. (2018). Eveline T. Feteris: Fundamentals of Legal Argumentation. Artificial Intelligence and Law, 26, 307-312.

Beynon-Davies, P. (2016). Instituting facts: Data structures and institutional order. Information and Organization, 26(1-2), 28-44.

Bhaskar, R. A. (1997). A realist theory of science, Verso.

Bitektine, A., & Haack, P. (2015). The “macro” and the “micro” of legitimacy: Toward a multilevel theory of the legitimacy process. Academy of Management Review, 40(1), 49-75.

Bowker, G. C., & Star, S. L. (1999). Sorting things out: Classification and its consequences. MIT Press.

Bowker, G. C., Baker, K., Millerand, F., & Ribes, D. (2009). Toward information infrastructure studies: Ways of knowing in a networked environment. In H. J. Klastrup L. Allen M. (Eds.) International handbook of internet research (pp. 97-117). Springer.

Braa, J., Hanseth, O., Heywood, A., Mohammed, W., & Shaw, V. (2007). Developing health information systems in developing countries: The flexible standards strategy. MIS Quarterly, 31(SI), 381- 402.

Bygstad, B., Hanseth, O. (2016). Governing e-health infrastructures: Dealing with tensions. In Proceedings of the 37th International Conference on Information Systems.

Bygstad B., & Øvrelid E. (2020). Architectural alignment of process innovation and digital infrastructure in a high-tech hospital, European Journal of Information Systems, 29(3), 220-237.

Calo, R., & Rosenblat, A. (2017). The taking economy: Uber, information, and power. Columbia Law Review, 117, Article 6.

Ciborra, C., Braa, K., Cordella, A., Dahlbom, B., Hepsø, V., Failla, A., ..., & Monteiro, E. (2000). From control to drift: The dynamics of corporate information infrastructures. Oxford University Press on Demand.

Constantinides, P., & Barrett, M. (2014). Information infrastructure development and governance as collective action. Information Systems Research, 26(1), 40-56.

Craig, R. K., Garmestani, A. S., Allen, C. R., Arnold, C. A. T., Birgé, H., DeCaro, D. A., ..., & Schlåger, E. (2017). Balancing stability and flexibility in adaptive governance: An analysis of tools available in US environmental law. Ecology and Society, 22(2), 1-3.

Currie, W. L. (2011). Institutional theory of information technology (137-173). Oxford University Press.

Currie, W. L., & Guah, M. W. (2007). Conflicting institutional logics: a national programme for IT in the organisational field of healthcare. Journal of Information Technology, 22(3), 235-247.

Deephouse, D. L., & Suchman, M. (2008). Legitimacy in organizational institutionalism. In R. Greenwood, C. Oliver, K. Sahlin, & R. Suddaby

(Eds.), The SAGE handbook of organizational institutionalism. SAGE https://doi.org/10.4135/ 9781849200387.n2

Edwards, P. N., Bowker, G. C., Jackson, S. J., & Williams, R. (2009). Introduction: An agenda for infrastructure studies. Journal of the Association for Information Systems, 10(5), 363-374.

Edwards, P. N., Jackson, S. J., Bowker, G. C., & Knobel, C. P. (2007). Understanding infrastructure: Dynamics, tensions, and design. National Science Foundation.

Eiband, M., Schneider, H., & Buschek, D. (2018). Normative vs. pragmatic: Two perspectives on the design of explanations in intelligent systems. IUI Workshop Proceedings.

ENV 13607 CEN (2000). Health informatics: Messages for the exchange of information on medicine prescriptions. European Committee for Standardization (CEN).

Eriksson, O., & Ågerfalk, P. J. (2010). Rethinking the meaning of identifiers in digital infrastructures. Journal of the Association for Information Systems, 11(8), 433-454.

Eriksson, O., & Goldkuhl, G. (2013). Preconditions for public sector e-infrastructure development. Information and Organization, 23(3), 149-176.

Erlingsdóttir, G., & Lindholm, C. (2015). When patient empowerment encounters professional autonomy: The conflict and negotiation process of inscribing an eHealth service. Scandinavian Journal of Public Administration, 19(2), 27-48.

Franklin, S., Wiberg, B. & Pettersson, C. (2007). Författningsmässig kontroll och beställningskontroll av e-recept (NEF). National Pharmacy Company (NPC).

Goldkuhl G., & Lyytinen, K. (1982). A language action view of information systems. In Proceedings of the 3rd International Conference on Information Systems (pp. 13-29).

Goodin, Robert E., ed. The theory of institutional design. Cambridge University Press, 1998.

Gregor, S. (2014). Theory—Still king but needing a revolution! Journal of Information Technology, 29(4), 337-340.

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. MIS Quarterly, 37(2), 337-355.

Gregersen et al. (2024). Database. Encyclopedia Britannica. https://www.britannica.com/ technology/database

Habermas J. (1976), What is universal pragmatics? In M. Cooke (Ed.), On the pragmatics of communication (pp. 21-103), Massachusetts Institute of Technology, Cambridge, USA.

Häggström M., Öhlund S.-E., Andersson M. (2007). Specifikation för XML-recept Uppdatering av Specifikation för XML-recept version 2.0.3 Nationellt e-receptformat. Carelink.

Hammar, T., Nyström, S., Petersson, G., Rydberg, T., & Åstrand, B. (2010). Swedish pharmacists value ePrescribing: A survey of a nationwide implementation. Journal of Pharmaceutical Health Services Research, 1(1), 23-32.

Hanseth, O. (2001). Gateways: Just as important as standards: How the internet won the “religious war” over standards in Scandinavia. Knowledge, Technology and Policy, 14(3), 71-89.

Hanseth, O., & Bygstad, B. (2017). The ePrescription initiative and information infrastructure in Norway. In M. Aanestad, M. Grisot, O. Hanseth, & P. Vassilakopoulou (Eds.), Information infrastructures within european health care (pp. 73-87). Springer.

Hanseth, O., Jacucci, E., Grisot, M., & Aanestad, M. (2006). Reflexive Standardization: Side effects and complexity in standard making. MIS Quarterly, 30(SI), 563-581.

Hanseth, O., & Lyytinen, K. (2004). Theorizing about the design of information infrastructures: design kernel theories and principles. (Sprouts: Working Papers on Information Systems). Available at https://www.uio.no/studier/ emner/jus/afin/FINF4001/h16/hanseth-andlyytinen-2004.pdf

Hanseth, O., & Lyytinen, K. (2010). Design theory for dynamic complexity in digital infrastructures: The case of building internet, Journal of Information Technology, 25(1), 1-19.

Hanseth, O., & Modol, J. R. (2021). The dynamics of architecture-governance configurations: An assemblage theory approach. Journal of the Association for Information Systems, 22(1), 130- 155.

Hanseth, O., & Monteiro, E. (1997). Inscribing behavior information infrastructure standards, Accounting, Management and Information Technologies, 7(4), 183-211.

Hanseth, O., & Monteiro, E. (1998). Changing irreversible networks: Institutionalisation and infrastructure. Available at https://folk.idi.ntnu. no/ericm/ecis.html

Hasselbladh, H., & Kallinikos, J. (2000). The project of rationalization: A critique and reappraisal of neo-

institutionalism in organization studies. Organization Studies, 21(4), 697-720.

Henfridsson, O., & Bygstad, B. (2013). The generative mechanisms of digital infrastructure evolution. MIS Quarterly, 37(3), 907-931.

Hindriks, F. (2009). Constitutive rules, language, and ontology. Erkenntnis, 71(2), 253-275.

Hohfeld, W.N. (1913). Some fundamental legal conceptions as applied in judicial reasoning. The Yale Law Journal, 23(1), 16-59.

Holland, J. H. (1995). Hidden order: How adaptation builds complexity. Addison-Wesley.

HSLF-FS 2021:75 (2021). Läkemedelsverkets föreskrifter om förordnande och utlämnande av läkemedel m.m. Läkemedelsverket: Swedish Medical Products Agency

Iannacci, F. (2010). When is a digital infrastructure? Investigating the emergence of public sector digital infrastructures. European Journal of Information Systems, 19(1), 35-48.

Kapferer, S., & Zimmermann, O. (2020). Domaindriven service design: Context modeling, model refactoring and contract generation. Proceedings of the 14th Symposium and Summer School on Service-Oriented Computing (pp. 189-208).

Karasti, H., Pipek, V., & Bowker, G. C. (2018). An afterword to “Infrastructuring and Collaborative Design.” Computer Supported Cooperative Work, 27(2), 267-289.

Keman, H. (2017). Institutionalization. Encyclopædia Britannica. https://www.britannica.com/topic/ institutionalization#ref338426

Kimaro, H. C., & Sahay, S. (2007). An institutional perspective on the process of decentralization of health information systems: A case study from Tanzania. Information Technology for Development, 13(4), 363-390.

Kierkegaard, P. (2013). E-prescription across Europe. Health and Technology, 3(3), 205-219.

Lag (1996:1156) om receptregister (1996). Svertiges Riksdag: Socialdepartementet. https://www. riksdagen.se/sv/dokument-lagar/dokument/ svensk-forfattningssamling/lag-19961156-om receptregister\_sfs-1996-1156

Latour, B. (1987). Science in action: How to follow scientists and 41 engineers through society. Harvard University Press.

LVFS 1997:10 (1997). Läkemedelsverkets föreskrifter om förordnande och utlämnande av läkemedel

m.m. Läkemedelsverket: Swedish Medical Products Agency.

LVFS 2009:13 (2009). Läkemedelsverkets föreskrifter om förordnande och utlämnande av läkemedel m.m. Läkemedelsverket: Swedish Medical Products Agency

Mekonnen, S. M., & Sahay, S. (2008). An institutional analysis on the dynamics of the interaction between standardizing and scaling processes: A case study from Ethiopia. European Journal of Information Systems, 17(3), 279-289

Mendling, J., Pentland, B. T., & Recker, J. (2020). Building a complementary agenda for business process management and digital innovation. European Journal of Information Systems, 29(3), 208-219.

MEDPRE 2000 Medical Prescription Message (2000), UN/EDIFACT. https://service.unece.org/trade/ untdid/d01b/trmd/medpre\_c.htm

Mignerat, M., & Rivard, S. (2015). Positioning the institutional perspective in information systems research. In. L. P. Willcocks, C. Sauer, & M. C. Lacity (Eds.), Formulating research methods for information systems (pp. 79-126). Springer.

Monteiro, E., Pollock, N., & Williams, R. (2014). Innovation in digital infrastructures: Introduction to the special issue. Journal of the Association for Information Systems, 15(4), i-x.

Monteiro, E., Pollock, N., Hanseth, O., & Williams, R. (2013). From artefacts to infrastructures. Computer Supported Cooperative Work, 22(4- 6), 575-607.

Nguyen, T. N., Nielsen, P., & Braa, J. (2017). Scaling Digital infrastructures: The case of the medical licensing system in a Southeast Asian country. Australasian Journal of Information Systems, 21, i-x.

Öhlund S.-E. (2007). Definition av ereceptmeddelanden—XML. Carelink.

Osmundsen, K., & Bygstad, B. (2021). Making sense of continuous development of digital infrastructures. Journal of Information Technology, 37(2), 144-164.

Ostrom, E. (2011). Background on the Institutional analysis and development framework. Policy Studies Journal 39(1), 7-27.

Pereira, J., Beir, M., Teixeira, J., & Machado, R. J. (2018). Patient-centric e-prescription services: An integrated system architecture proposal. Proceedings of the International Conference on Intelligent Systems (pp. 576-583).

Pipek, V., & Wulf, V. 2009. Infrastructuring: Toward an integrated perspective on the design and use of information technology. Journal of Association for Information Systems 10(5), 447-473.

Powell, W. W. (1990). Neither market nor hierarchy: Network forms of organization. Research in Organizational Behavior, 12, 295-336.

Reason, J., Parker, D., & Lawton, R. (1998). Organizational controls and safety: The varieties of rule‐related behaviour. Journal of Occupational and Organizational Psychology, 71(4), 289-304.

Rolland, K. H. (2017, November 27-29). Reconceptualizing design of infrastructures: Stabilizing and innovating through maintenance work. Paper presented at NOKOBIT 2017, Oslo, Norway.

Sahay, S., Sæbø, J. I., Mekonnen, S. M., & Gizaw, A. A. (2010). Interplay of institutional logics and implications for deinstitutionalization: Case study of HMIS implementation in Tajikistan. Information Technologies & International Development, 6(3), 19-32.

Sahay, S., Nielsen, P., & Aanestad, M. (2018). Institutionalizing information systems for universal health coverage in primary health care and the need for new forms of institutional work. Communications of the Association for Information Systems, 44, 62-80.

Schou, J., & Hjelholt, M. (2019). Digital state spaces: Sstate rescaling and advanced digitalization. Territory, Politics, Governance, 7(4), 438-454.

Scott, W. R. (2008). Institutions and organizations: Ideas and interests. SAGE.

Searle, J. R. (1969). Speech acts: An essay in the philosophy of language. Cambridge University Press.

Searle, J.R. (1995). The construction of social reality. Free Press.

Searle, J.R. (2005). What is an institution? Journal of Institutional Economics 1(1), 1-22.

Searle, J.R. (2006). Social ontology: Some basic principles. Anthropological Theory 6(1), 12-29.

Searle, J. (2010). Making the social world: The structure of human civilization. Oxford University Press.

Sein, M. K., Henfridsson, O., Purao, S., Rossi, M., & Lindgren, R. (2011). Action design research. MIS Quarterly, 35(1), 37-56.

Sein, M. K., & Rossi, M. (2019). Elaborating ADR while drifting away from its essence: A commentary on Mullarkey and Hevner.

European Journal of Information Systems, 28(1), 21-25.

SFS 2002:160 (2002). Lag om läkemedelsförmåner m.m. Sveriges Riksdag.

SFS 2005:259 (2005). Lag om ändring i lagen (1996:1156) om receptregister. Sveriges Riksdag.

SIS 2002 (2002). Hälso- och sjukvårdsinformatik— Meddelanden för utbyte av information om läkemedel Guide för svensk implementering av ENV 13607 i XML gällande: Recept/rekvisition —Återkallande av recept/rekvisition— Information om expedierade läkemedel— Återkallande av information om expedierade läkemedel. Swedish Standards Institute.

Suchman, M. C. 1995. Managing legitimacy: Strategic and institutional approaches. Academy of Management Review, 20, 571-610.

Thornton, P. H., Ocasio, W., & Lounsbury, M. (2012). The institutional logics perspective: A new approach to culture, structure, and process. Oxford University Press.

Tilson, D., Lyytinen, K., & Sørensen, C. (2010). Digital infrastructures: The missing research agenda. Information Systems Research, 21 (4), 748-759.

van Steenbergen, E., van Dijk, D., Christensen, C., Coffeng, T., & Ellemers, N. (2020). Learn to build an error management culture. Journal of Financial Regulation and Compliance, 28(1), 57-73.

Vila-Pozo, M. M., & Sahay, S. (2019). Institutional shaping of affordances: Implications on information use in global humanitarian organizations. Proceedings of the International Conference on Social Implications of Computers in Developing Countries (pp. 496- 507).

Winograd, T., Flores, F., & Flores, F. F. (1986). Understanding computers and cognition: A new foundation for design. Intellect Books.

Yasuda, H. (2018). Governance mechanisms of interorganizational relationship: Comparative analysis of three forms of alliance governance. Journal of Strategic Management Studies, 10(1), 81-93.

Yin, R. K. (2009). Case study research: Design and methods (4th ed.). SAGE.

Yoo, Y., Lyytinen, K., & Yang, H. 2005. The role of standards in innovation and diffusion of broadband mobile services: The case of South Korea. Journal of Strategic Information Systems, 14, 323-353.

## About the Authors

Owen Eriksson is a professor of information systems at Uppsala University. His main research fields are the digital transformation of society and how pragmatism and institutional theory can inform information systems design and conceptual modeling. His research is informed by design science and is action oriented. He has been the research leader of a number of externally funded research projects in close cooperation with the public sector and industry. His work has appeared in journals such as European Journal of Information Systems, Information Systems Journal, Journal of Information Technology, and Journal of the Association for Information Systems.

Sten-Erik Öhlund is a senior lecturer at Uppsala University and earned his Ph.D. in information systems development at Linköping University. His main research fields are requirements engineering, interoperability, and the development of digital information infrastructures. He has worked more than 20 years in the field of practice developing and designing digital infrastructures for e-prescribing and related areas, such as e-commerce infrastructures for the distribution of pharmaceuticals at pharmacies and hospitals.

Copyright © 2024 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
