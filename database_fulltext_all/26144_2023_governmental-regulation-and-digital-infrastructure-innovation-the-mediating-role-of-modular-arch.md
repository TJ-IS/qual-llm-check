---
otero_id: 26144
otero_key: "AEYTZB8T"
title: "Governmental regulation and digital infrastructure innovation: The mediating role of modular architecture"
authors: "Stefan Henningsson; Benjamin D Eaton"
year: "2023"
journal: "Journal of Information Technology"
doi: "10.1177/02683962221114429"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Governmental regulation and digital infrastructure innovation: The mediating role of modular architecture

Journal of Information Technology 2023, Vol. 38(2) 126–143 © Association for Information Technology Trust 2023 Article reuse guidelines: sagepub.com/journals-permissions DOI: 10.1177/02683962221114429 Journals.sagepub.com/jinf

Stefan Henningsson and Benjamin D Eaton

SSage

## Abstract

In response to their growing importance, digital infrastructures (DIs) are increasingly subject to governmental regulation due to concerns over the downside risks posed by digital technologies to individuals and society. There is a general paucity of studies that address the impact of regulations on DI innovation. In addition, existing research presents seemingly contradictory <sup>fi</sup>ndings on regulations governing digital technologies as both enabling and inhibiting innovation. This paper, therefore, elaborates on how different types of regulation impact various forms of DI innovation. We draw on modular systems theory to enrich extant conceptualisations of DIs and develop a related conceptual model that demonstrates the paths by which two types of DI regulation in<sup>fl</sup>uence DI architectural modularity, which is proposed as a mediating mechanism that in<sup>fl</sup>uences DI innovation. Our model makes a theoretical contribution through an in-depth explanation of the relationship between regulation and DI innovation by articulating and illustrating the effects of regulatory provisions and thereby extends the extant DI literature. In terms of practical implications, our model can help stakeholders both create DI regulation and respond to regulatory provisions.

## Keywords

Digital infrastructure, digital innovation, regulation, modular architectures, component con<sup>fi</sup>guration and design

## Introduction

Technical inventions and digital convergence have led to a multitude of shared, unbounded, heterogeneous, and open sociotechnical solutions, referred to as digital infrastructures (DIs) (Tilson et al., 2010). DIs enable information exchange, automate activities by translating information into action, and generate new streams of data created through the automation of activity (Zuboff, 1988). Both generalpurpose DIs, such as the internet (Hanseth and Lyytinen, 2010), and special-purpose DIs, such as those enabling healthcare, transportation, finance, and law enforcement, are critical to society (Koutsikouri et al., 2018).

One of the central characteristics of DIs is that they rarely are designed top down and built from scratch as traditional information systems. Instead, DIs typically evolve organically over time as various actors innovate a DI incrementally by modifying and building on what already exists (Fink et al., 2020). This decentralised innovation is a strength since it unleashes creativity and unanticipated possibilities (Yoo et al., 2010). However, the decentralised innovation of DIs is increasingly attracting attention from social, political, and legal stakeholders who are concerned with their evolution since the outcome of some of these innovations can have negative consequences for consumers, workers, and society at large (Zuboff, 2019).

Among stakeholders, governments are specifically attempting to safeguard the interests of society in relation to DIs through the application of regulations (henceforth DI regulation; (Tilson et al., 2010; Lanzara, 2014). Such DI regulation addresses, for example, the resilience of societally important DIs (European Commission, 2020), the privacy and integrity of citizens (Tikkinen-Piri et al., 2018), and the consequences for market competition (Montero and Finger, 2021).

The impact of regulation efforts is debated in both practice and academia. In practice, the influence of regulation has been actualised through clashes over the so-called net neutrality act in the United States (US), where different camps debate whether this regulation prevents new innovative services or removing it may lead to monopolies that stifle innovation. In Europe, governments are seeking to balance regulations that enhance technical and operational resilience in financial market infrastructures with the costs of compliance (Butler and O’Brien, 2019) and potential constraints on innovation (Shadikhodjaev, 2021).

These debates and contradictions concerning the regulation of DIs are reflected in academic research. On the one hand, regulation is assigned a role in coordinating the efforts of actors innovating a DI; it can glue together disparate islands of components by enforcing the adoption of standards (Damsgaard and Lyytinen, 1998a), ensuring critical qualities of resilience and transparency (Contini, 2014; Contini and Lanzara, 2014a), preventing a DI from splintering into multiple proprietary structures (Plantin et al., 2018), and turning privately managed platforms into an open DI (Bazarhanova et al., 2020). On the other hand, critical observations suggest that regulation is overly focused on technical interoperability (Lanzara, 2014) and that it may restrict the incorporation of novel digital technologies in a DI (Kallinikos, 2009). These works implicitly bring into consideration a balanced view of how much regulation is needed to safeguard societal interests without severely compromising innovation possibilities.

However, the current understanding of DI regulation is subject to two limitations that conceal important nuances in the association between DI regulation and innovation. One is a lack of recognition that there are different types of regulation that work in different ways (see, for example, Ogus, 2008). The other is a failure to recognise that DI innovation can take different forms (see, for example, Grisot et al., 2014). The lack of consideration of these nuances in the relationship between regulation and DI innovation is unfortunate since ‘without a deeper understanding of how innovation is shaped between the rules of technology and law… it will be difficult to develop public online systems that [work] properly and serve people’ (Lanzara, 2014: 4). We therefore address the following research question: How do different types of DI regulation impact different forms of DI innovation?

To answer our question, we follow a conceptual development approach informed by advice from the broader management literature (Gilson and Goldberg, 2015; Hulland, 2020; Jaakkola, 2020) about designing conceptual research (see Appendix A). Our understanding of DI regulation encompasses both principle-based and rules-based regulation (Ford, 2008) and a recognition that such regulation that can take different forms to specify the behavioural requirements of a DI (Ogus, 2008)<sup>1</sup>.

We further apply theoretical concepts taken from modular systems theory (Schilling, 2000) to explain the relationship between DI regulation and innovation. We employ research on digital artefacts (Tilson et al., 2010; Henfridsson and Bygstad, 2013) to conceptualise the architecture of DIs as modular in form. Based on Baldwin and Clark’s (2000) concepts of visible design rules and hidden design parameters, we define DI innovation as (a) changes in how the constituent components of a DI are combined to form a whole and (b) changes to the internal design of a component or components within a DI.

Using this understanding of DI innovation, we analyse the ways that different types of regulation influence a DI’s modular architecture and the subsequent effects on actors possibilities to combine and design components in a DI, as depicted in Figure 1. As we articulate the logic by which architectural modularity mediates the influence of DI regulation, we use empirical examples from previous case studies (c.f. Payne et al., 2017) to illustrate our theoretical arguments and make them accessible to the reader.

The analysis allows us to refine the consideration of how much regulation of DIs is appropriate and include further nuanced considerations of which form regulation should take, where it should be applied, and when intervention through regulation should occur. These new analytical possibilities will be useful for information systems scholars studying regulation or DIs. Finally, our research has practical implications for regulators and DI actors whose innovation activities are impacted by regulation.

## Regulation and digital infrastructures

We review the related research on governmental regulation and DI innovation in three steps. First, we define and characterise DIs. Second, we define regulation as an institutional response to the risks that technologies pose to society (Wiener, 2004). Third, we present the contradictory observations about how DI regulation is seen as both an enabler and constraint to innovation. This review exposes the need for a more nuanced way to account for how different forms of DI regulation impact different forms of DI innovation.

## Digital infrastructure

The concept of a $\mathrm { D I } ^ { 2 }$ is formally defined as ‘the basic information technologies and organisational structures, along with the related services and facilities necessary for an enterprise or industry to function’ (Tilson et al., 2010: 748). The general proliferation of digital technology in combination with increasing connectivity warranted by application programming interface (API) standards, blockchain, and Hyperledger technologies (Sarker et al., 2021) has fuelled rapid growth in DIs that are essential to the operation of a range of vital societal functions. While not always referred to or conceptualised as a DI, this type of IT solution is of interest to researchers working with fintech, insuretech, and regtech (Montero and Finger, 2021) as well as in the more traditional domains of healthcare (Aanestad and Jensen, 2011), transportation (Jensen et al., 2018), and government (Pipek and Wulf, 2009).

![](/api/attachments/AEYTZB8T/fulltext/images/c136c54c3bcf46bd859b1bb119ab95a6499e3b0b144a71fc2edb1bf622056c5d.jpg)  
Figure 1. Design of conceptual analysis and model development.

Despite contextual variances across different domains, DIs share some fundamental common conceptual characteristics. First, DIs consist of heterogenous collections of technologies. They comprise various kinds of ‘core technologies’ (Capello and Lenzi, 2021), including IT systems and databases, that build on and instantiate ‘enabling technologies’ (Capello and Lenzi, 2021), such as AI, machine learning algorithms, biometric identification techniques, and positioning technologies, and they further enable the building of digital services on top of the infrastructure (Tilson et al., 2010). In DIs, technical components refer to any functionally defined entity that interconnects to other technical entities to form part of a complex IT artefact with infrastructural qualities (Hanseth and Lyytinen, 2010; Tilson et al., 2010). These technical components are interconnected through integration protocols, such as electronic data interchange (EDI), APIs, near field communication, and blockchain (Sarker et al., 2021).

Second, DIs are also characterised by social heterogeneity and distributed control. In general, DIs emerge organically through the bottom-up contributions of organisations and individuals as they connect their technical solutions (Pipek and Wulf, 2009). It follows then that DIs frequently do not exhibit centralised governance in a hierarchical sense but are governed through decentralised mechanisms that involve collective action and federated control (Eaton et al., 2018). Nevertheless, some actors such as governments or supranational bodies have the judicial or legislative power to shape DIs in specific areas or domains (Napieralski, 2019).

Third, it then follows that DI innovation typically emerges through the semi-coordinated actions of actors with partially diverging interests that are trying to shape the infrastructure towards specific ends (Knol and Tan, 2018; Zorina and Dutton, 2021). Since it is rarely possible to redesign a DI from scratch, actors that want to innovate a DI must take what currently exists – that is, the constituent components of the DI conceptually referred to as the ‘installed base’ (Aanestad et al., 2017; Rodon and Eaton, 2021) – and try to evolve it in a desired direction (Ciborra and Hanseth, 2000; Koutsikouri et al., 2018). Thus, in the DI literature, DI innovation broadly refers to any modification to the social or technical components of the installed base. Our perspective on DI innovation, framed below through modular systems theory, focusses on modifications to the technical components of the installed base and thus encompasses a subset of DI innovation.

## Regulation as behavioural requirements

Governmental intervention through direct regulation is an institutional response to the risks that technologies pose (Wiener, 2004) and affects the behaviour of individuals and organisations by defining what is legal and illegal (Khemani and Shapiro, 1993; Finck, 2018). Regulation defining what is legal and illegal is expressed in written documents that include legislation, directives (legally binding governmental instructions), and implementing provisions (legally binding instructions on how legislation should be followed). Regulations provide the principles and rules (Ford, 2008), expressed as obligations, permissions, and prohibitions for regulated entities to mitigate risk through controls over technological components, such as those within a DI. In practice, governments legislate through setting principles and enable frontline regulatory agencies to specify the meaning of such principles in their particular area (Ford, 2008). Consequently, a considerable degree of power is delegated to regulatory agencies, and their instructions become legally binding.

Table 1. Direct regulation as governmental control.

<table><tr><td>Regulative expression</td><td>Stipulated requirement</td><td>Example</td></tr><tr><td>Performance targets</td><td>Outcome oriented towards the quality attributes to be met in an activity (Finck, 2018; Talias, 2021)</td><td>- Maximum levels of emissions from activities- Catch limits and quotas in fishing</td></tr><tr><td>Activity specifications</td><td>Process oriented towards (a) methods and/or (b) materials to be used (or not) in an activity (May, 2003; Rowell and van Zeben, 2021)</td><td>- Approved types of construction materials- Mandatory steps and practices in financial accounting</td></tr></table>

Our view of regulation in this paper encompassed both principle-based and rules-based approaches to regulation and the work by both governments and frontline regulators that turn principles into behavioural requirements (Ford, 2008). The behavioural requirements that are the basis for regulation can be expressed in two different ways (Ogus, 2008); see Table 1). First, there are performance targets that stipulate the specific quality attributes to meet. Performance targets are output oriented and may stipulate, for example, the allowed level of $\mathrm { C O } _ { 2 }$ emissions for cars. Second, there are activity specifications that stipulate how an activity should be carried out. Activity specification is process oriented and defines materials and methods that can, or cannot, be used in a process. For example, such specifications may detail how to handle a toxic substance in chemical process industries or may ban the use of certain building materials in construction.

In the literature, the use of activity specification as the basis for regulation has been extensively criticised (Finck, 2018; Talias, 2021). Activity specification leaves little or no alternative regarding how the regulatory objective might be achieved. This is considered problematic since in many cases, industry may know more than the government about how best to deal with a problem (Sinclair, 1997). Previous literature, particularly in the area of environmental regulation, has therefore concluded that command-and-control regulation based on activity specification inhibits technical innovation in a regulated area (Rowell and van Zeben, 2021).

The alternative to activity specification, performance targets, is lauded by academics and policymakers (Rowell and van Zeben, 2021). By focusing on an end state and giving industry actors freedom in how to achieve that end state, performance targets theoretically allow actors to choose the most efficient means of meeting the requirements. The catch, however, is that performance targets require regulators to have a suitable means of defining performance. When this is problematic, the regulation may not fulfil its purpose of safeguarding societal interests.

## Regulation and digital infrastructure innovation

The issue of DIs as a regulatory concern has become apparent to society due to the market dominance of big technological corporations (e.g. Meta, Alphabet, and Amazon; (Montero and Finger, 2021), the topic of political manipulation (Zuboff, 1988; 2019; Flew and Wilding, 2021), the threat of surveillance capitalism (Zuboff, 1988; 2019), and data privacy considerations (Tikkinen-Piri et al., 2018). In the background, operational risk and digital resilience, particularly in the financial industry (European Commission, 2020) and in AI technologies, are under increasing regulatory scrutiny on account of the potential consequences stemming from any mismanagement.

Within our view of governmental regulation, DI regulation specifies the behavioural requirements of a DI to achieve a specific objective and that is supported by sanctions to enforce the desired behaviour. Such DI regulation is issued by an institution that holds the legal authority to dictate what is legal and illegal.

Within the DI literature, the role of governmental regulation can be understood in relation to the innovation activities that can be completed to modify a DI (Knol and Tan, 2018). In DIs, a degree of decentralised control is critical to innovation (Ciborra and Hanseth, 2000; Hanseth and Modol, 2021) since it allows for bottom-up innovation driven by self-reinforcing processes centred on repurposing technology (Yoo et al., 2010; Hanseth and Modol, 2021). Decentralised control makes room for the local adaptations required to cater to the needs of specific actors, including interfacing to the DI’s existing components (Rolland and Monteiro, 2002; Rolland et al., 2018). Simultaneously, a degree of centralised control is critical to ensure the integrity of the DI because completely unmanaged modifications can negatively impact the DI as a whole (Tilson et al., 2010). Some centralised control is therefore essential to protect specific qualities of the entire DI (Ciborra, 2009; Koutsikouri et al., 2018; Hanseth and Modol, 2021). In response to the opposing logics of decentralised and centralised control, governmental regulation forms behavioural specifications for innovation that correspond to the ‘design principles’ of the DI (Hanseth and Lyytinen, 2010).

While governmental regulation has rarely been the explicit focus of DI research, studies that touch on the issue share the broad conclusion that DI regulation plays an imperative role in enabling the formation of efficient DIs. Through the investigation of phenomena such as EDI (Damsgaard and Lyytinen, 1998a; 1998b), the internet (Plantin et al., 2018), smart electricity infrastructures (Gheorghe et al., 2006), and international trade (Rukanova et al., 2009; Rukanova et al., 2018; Sarker et al., 2021), researchers have concluded that DI regulation can catalyse the adoption of core infrastructural technologies through mandated use (Henriksen and Damsgaard, 2007) and glue together disparate islands of components by enforcing adoption of interoperability standards (Damsgaard and Lyytinen, 1998a). A benefit of DI regulation is that it resolves potential conflicts without relying on individual decision makers to comprehend an entire system’s operations or collectively agree on its purpose (see Boyer, 1998).

In contrast, a more negative stance towards DI regulation appears in a series of studies led by Contini and Lanzara (2014b), who analysed DIs to support judicial proceedings in the European Union (EU; (for an overview, see Contini and Lanzara, 2014a). Their work has broadly shown that in domains with extensive regulation, DIs face more restrictions on innovation. Lanzara (2014) found that governmental institutions focus extensively on technical interoperability and DI efficiency, including robustness and reliability, at the expense of DI adaptability and flexibility. Such institutions do so because DIs are important enough to society that they cannot be permitted to evolve in any direction. Not all modifications to a DI will be in the interest of society (Zorina and Dutton, 2021). Opportunities to repurpose digital content leads incumbents to reassert their control through new governmental interventions, for example, as tight copyright and data privacy laws (Tilson et al., 2010). However, doing so feeds into the complexity of a DI (Contini, 2014) and can incur massive adaptation costs for the impacted organisation (Butler and O’Brien, 2019). This has led researchers to call for simplification in regulation wherever possible (Contini, 2014) to disentangle technology and regulation when designing DIs (Contini and Mohr, 2014).

Regulators attempt to accommodate these opposing conceptual stances towards DI regulation in practice. For example, they are increasingly eager to balance the need to regulate and ensure individual consumer, market, and systemic protection, stability, and resilience (Hallinan, 2021) with the need to ensure that innovation around digital technologies brings greater efficiencies and value to consumers and markets (Paech, 2019). Regulators are striving to make regulation technology neutral (Paech, 2019; Shadikhodjaev, 2021) in order to anticipate and accommodate the emergence of unintended digital technology uses (Nambisan et al., 2017) and future-proof regulation to encompass all forms of digital technology innovation and application.

Because few studies on DIs have explicitly focused on the influence of regulation, little effort has been made to conceptualise such regulation in relation to a DI. Specifically, no DI research has recognised that regulation can take different forms and work in fundamentally different ways to influence behaviour. In addition, no research that we are aware of has tried to conceptually reconcile the seemingly contradictory conclusions about the impact of DI regulation on DIs. In our view, these two gaps in the existing literature go hand in hand and should thus be addressed in tandem. Therefore, as one premise for this work, we acknowledge that regulation can take distinct forms, specifically with behavioural restrictions articulated as performance targets (output oriented) or as activity specifications (process oriented). Because these two forms of regulation work in different ways to restrict behaviour, they have been found elsewhere to impact innovation in very distinct ways (Sinclair, 1997; May, 2003). As a second premise, we consider how DI innovation can take various forms (see, for example, Grisot et al., 2014). Thus, in the next section, we introduce a theoretical perspective that allows us to study DI innovation at a more granular level while maintaining conceptual coherency. Subsequently, we will use these two perspectives to elaborate on how different forms of DI regulation impact various forms of DI innovation.

## Modularity and digital infrastructure innovation

To better explain how different aspects of DI regulation impact various forms of innovation, we turn to modular systems theory (Schilling, 2000). Modularity is a dominating perspective in research on digital innovation broadly (see, for example, Yoo et al., 2010; Kohli and Melville, 2019; Wang, 2021) and has documented explanatory power in relation to DI innovation specifically (Hanseth and Lyytinen, 2010; Aanestad and Jensen, 2011; Grisot et al., 2014; Rodon and Silva, 2015; Rodon and Eaton, 2021). As such, it provides us with a relevant and conceptually coherent framework through which to systematically analyse the implications of DI regulation on innovation at a highly granular level.

Modular systems theory foregrounds the critical role of architecture in explaining innovation in complex artefacts since architecture conditions how the subcomponents in an artefact can be modified. We argue in this section that the way DI regulation impacts the architecture of a DI has consequential effects on a DI’s capacity for innovation.

## Modular systems theory

Modular systems theory is grounded in Simon’s (1996) premise that any complex artefact can be seen as consisting of hierarchically nested subsystems. A central tenant in modular systems theory is the distinction between two different approaches to the architectural arrangement of components in a design hierarchy: integral and modular architectures (Ulrich, 1995). An integral architecture specifies the functioning of each component and the ways in which the distinct components are integrated and bound together to create a coherent whole (Henderson and Clark, 1990). Tight coupling between the components in an integral architecture ensures an optimised product design with consistently high performance (Yoo et al., 2010). Innovation within integral architectures, however, is difficult. The nested structure of tightly coupled components suggests that any form of innovation requires well-coordinated changes across various components in the product (Baldwin and Clark, 2000; Baldwin and Von Hippel, 2011).

In contrast, a modular architecture is characterised by its focus on the interfaces between components and the encapsulation of the functionality of each component as an independent unit. Modularity is a general design principle that intentionally increases independence among the subsystems of a complex system (Sanchez and Mahoney, 1996). Architectural modularity thus describes the degree of modularity as opposed to the degree of integration. It explains the degree to which a system’s components can be separated and recombined (Schilling, 2000).

Baldwin and Clark (2000) explain how a complex system is broken down into independent components that interact with each other to provide a working whole by partitioning functional information into visible design rules and hidden design parameters. Visible design rules describe the information made public so that components can be configured to interconnect and function as a whole (Baldwin and Clark, 2006). In the context of modular architectures, Baldwin and Clark refer to components as ‘modules’,<sup>3</sup> stating that visible design rules should ‘involve specifying its architecture, that is, what its modules are; specifying its interfaces, i.e., how the modules interact; and specifying tests which establish that the modules will work together and how well each module performs its job’ (Baldwin and Clark, 2006: 180).

For the purposes of our paper, we consider three types of architecture-related information that are contained in visible design rules: component arrangements (specifying the components and the connections between the components), interfaces between components (covering how they connect and the information passed between them so that they function as a whole), and functional criteria (describing how the components should perform)<sup>4</sup>. These design rules ensure ‘that the respective parts [do] not clash and…“kill” the system as a whole’ (Baldwin and Clark, 2000: 4).

The internal functioning of components is described by hidden design parameters as information that is encapsulated and not necessarily made public. In this way, the internal architecture of a component is ‘black boxed’ (formally conceptualised by Parnas (1972)] as ‘information hiding’) and made invisible to other components. The emphasis here is on what the output of the functional component is rather than on how it is achieved. Consequently, in a modular architecture, components can be innovated by redesign as long as they adhere to design rules that define the interfaces between them (Baldwin and Clark, 2000).

## Control regulation and digital infrastructure architecture

In the DI literature, definitions of architecture commonly draw on Ulrich’s (1995: 4) original definition of product architecture as ‘the scheme by which the function of a product is allocated to physical components’ (see, for example, Yoo et al., 2010; Rodon and Silva, 2015). In the context of DIs, the physical dimension is typically downplayed, while the emphasis on architecture as the structure through which individual components form a whole is retained (Yoo et al., 2010; Henfridsson and Bygstad, 2013; Grisot et al., 2014; Rodon and Silva, 2015; Rodon and Eaton, 2021).

Our view of architecture follows this thinking and emphasises a DI’s individual components and the way in which they combine to form a DI from a technical perspective. Within this view, a DI component refers to a defined element of the DI that is encapsulated and interfaced to other components in the DI.

Furthermore, building on the broad view of DI innovation as any modification to the DI’s installed base, we draw on modular systems theory (Schilling, 2000) to distinguish between two basic forms of modification to a DI’s technical components. The first includes modifications to the design of individual components, referring to the configuration of a component in a DI to accomplish a specific function (Rodon and Eaton, 2021). The second covers modifications to how the individual components are combined, referring to how a set of components are arranged to form a whole that provides the DI’s overall functionalities (Rodon and Silva, 2015).

Following modular systems theory (Schilling, 2000), a DI’s architecture conditions the design and combination of components. Specifically, visible design rules condition the combination of components in the DI, while hidden design parameters condition independent component design (see Figure 2).

It can be derived from Figure 2 that the extent to which governments can influence DI architecture through regulation will have an indirect effect on how actors can innovate a DI by (re)combining and (re)designing components in the infrastructure itself. In previous research on DIs, scholars have concluded that the most fruitful way to control the shaping of a DI is to manipulate the metalevel rules of engagement, that is, the DI’s design principles (Hanseth and Lyytinen, 2010). Such design principles are embodied in the design rules and design parameters of the architecture (Baldwin and Clark, 2006).

![](/api/attachments/AEYTZB8T/fulltext/images/101e469c56983f6486e9843d6b138afa85db59ed62aeebdd426fb35776905a4e.jpg)  
Figure 2. Architectural modularity conditions component design and the combination of components in a DI.

Mirroring these views of architecture as a means of control in DIs, we see a similar role for governmental regulation in influencing DI architecture to condition DI innovation. Thus, we make three assumptions concerning the relationship between regulation and DI architecture that are grounded in existing research. First, we follow Yoo et al. (2010) and regard modularity as a continuum rather than two discrete states of modular and integrated architectures. In practice, most DI architectures are hybrid architectures that contain elements of both modularity and integration (Baldwin and Clark, 2000; Schilling, 2000). This means that regulation can have an incremental effect that increases (or decreases) modularity relative to integration.

Second, the elements of modular and integrated architectures are heterogeneously distributed across a DI. That is, in one part of the DI, the architecture may be close to a modular archetype, while in a different part of the DI the architecture may be highly integrated (Rodon and Silva, 2015). This means that the effect of regulation can also be heterogenous, addressing specific areas of concern rather than a universal property.

Third, while some authors argue that ‘architectural choices are frequently irreversible, endogenous choices’ (Agarwal and Tiwana, 2015: 477), we do not subscribe to the view that DI architecture is carved in stone and believe instead that it is subject to change over time (Grisot et al., 2014). Seen over years or even decades, some architectures migrate towards more modularity and others towards increasing integration (Schilling, 2000). Such architectural changes may be the result of technological evolution but also likely stem from the explicit interventions of actors, such as regulators, that hold positions that allow them to redefine architectural design (see, for example, Grisot et al., 2014).

With this understanding, DI regulation can be analysed as behavioural restrictions that impact DI architecture and subsequently condition DI innovation. The extent to which DI regulation influences any visible design rules or hidden design parameters will have consequential effects on how actors can modify the existing components of a DI. The forms and their respective logic stemming from such mediation by DI architecture (modular vs integrated) are analysed next.

## Regulation, architecture, and innovation

In this section, we analyse how governmental regulation influences DI architecture and thereby indirectly conditions DI innovation. Table 2 summarises the constructs as defined and described in previous sections.

As explained below, DI regulation through performance targets acts at the level of visible design rules, setting conditions for how components may be combined to form a DI. Conversely, DI regulation through activity specification acts internally on components, conditioning their internal design. Intersecting DI regulation with modular architecture, Table 3 presents regulatory interventions that influence DI architecture in different ways and illustrates these interventions with examples from the analysis in this section<sup>5</sup>. Figure 3 provides a model that positions these regulatory interventions in relation to our conceptualisation of DI innovation. The conceptua model covers the relationships between our constructs that are discussed in the remainder of this section.

## Regulating visible design rules through performance targets

The regulation of the design of modular architectures through performance targets involves specifications about the three dimensions of visible design rules: interfaces, modular arrangements, and functional criteria (Baldwin and Clark, 2006). Regulation directed at these dimensions defines the conditions through which components can be included in a DI without addressing how individual components should be designed internally.

Table 2. Construct de<sup>fi</sup>nitions.

<table><tr><td>Construct</td><td>Definition</td></tr><tr><td>DI regulation</td><td>Principle and rules-based regulation (Ford, 2008) that specifies the behavioural requirements (Ogus, 2008) of a DI to achieve a specific objective and is supported by sanctions to enforce the desired behaviour</td></tr><tr><td>Regulation through performance targets</td><td>Regulation that stipulates the specific quality attributes to be met as an end state (outcome) while giving actors freedom in how to achieve that end state (Finck, 2018; Talias, 2021)</td></tr><tr><td>Regulation through activity specification</td><td>Regulation that specifies how an activity should be carried out by stipulating (a) methods and/or (b) materials to be used (or not) in an activity (May, 2003; Rowell and van Zeben, 2021)</td></tr><tr><td>DI architectural modularity</td><td>The degree of modularity as opposed to the degree of integration, referring to the degree to which a DI&#x27;s components can be separated and recombined (Baldwin and Clark, 2000; Schilling, 2000)</td></tr><tr><td>Visible design rules</td><td>The information made public so that components can be configured to interconnect and function as a whole, specifically the (a) modular arrangements (specifying the components and the connections between the components), (b) interfaces between the components (covering how they connect and the information passed between them so that they function as a whole), and (c) functional criteria (describing how the components should perform; (Baldwin and Clark, 2006)</td></tr><tr><td>Hidden design parameters</td><td>The information concerning the internal functionality of individual components that is encapsulated and not made public (Baldwin and Clark, 2006)</td></tr><tr><td>DI innovation</td><td>The innovation of a DI through modifications to the technical and social components of the DI (Ciborra and Hanseth, 2000; Koutsikouri et al., 2018)</td></tr><tr><td>Component (re)combination</td><td>The arrangement of components to form a whole that provides the DI&#x27;s overall functionality (Rodon and Silva, 2015)</td></tr><tr><td>Component (re)design</td><td>The configuration within an individual component of a DI that accomplishes a specific function (Rodon and Eaton, 2021)</td></tr></table>

Table 3. Regulatory interventions and their in<sup>fl</sup>uence on DI architecture.

<table><tr><td>Regulation target</td><td>Regulatory intervention</td><td>Description of influence</td><td>Illustrative example</td></tr><tr><td rowspan="3">Regulation of visible design rules through performance targets</td><td>Specification of interfaces</td><td>Regulation can set de jure standards that allow for interoperability between heterogenous components controlled by different actors</td><td>TradeNet, Singapore&#x27;s EDI standard for reporting trade data (Tan, 1998; Lyytinen and Damsgaard, 2011)</td></tr><tr><td>Specification of modular arrangements</td><td>Regulation can specify architecture by defining a technical specification (interface) that is typically legally binding and by stating whom or what the regulation applies to (component definition)</td><td>Network neutrality law undoing the commercially motivated integration of components (Bauer and Knieps, 2018)</td></tr><tr><td>Specification of functional criteria</td><td>Regulation can specify the functional criteria in terms of the guaranteed output and input quality as tests that a component must meet to qualify for inclusion in a DI</td><td>PSD26in Europe&#x27;s conditioning of third-party digital services (Zachariadis and Ozcan, 2017)</td></tr><tr><td rowspan="2">Regulation of component design parameters through activity specification</td><td>Specification of materials</td><td>Regulation can specify the materials from which a component is constructed and/or their provenance, such as the source or creator of those materials</td><td>Blacklisting of components in the 5G infrastructure (Ferrare, 2019; Tekir, 2020)</td></tr><tr><td>Specification of methods</td><td>Regulation can specify the method – the process steps or the algorithm that is executed – of components in a DI</td><td>Cybersecurity practices for resilience in digital financial infrastructures (EBA, 2019; ECB, 2019)</td></tr></table>

![](/api/attachments/AEYTZB8T/fulltext/images/98de6e26dd17247fb83e90a126c49b201b998ac237992c9c6a22a2a353e21765.jpg)  
Figure 3. Graphical representation of the in<sup>fl</sup>uence of DI regulation on architecture and innovation.

Regulatory intervention through the specification of interfaces. Within DI research, DI regulation through the specification of interfaces is particularly embraced in studies concerning how governments engage in setting de jure standards that allow for interoperability between heterogenous social and technical components controlled by different actors (Hanseth et al., 1996; Braa et al., 2007).<sup>7</sup> Hanseth and Monteiro (1997: 183) define standards as ‘the technical basis for an information infrastructure… which regulate the communicative patterns’. Such technical standards may be the result of governmental interventions through regulation in the form of de jure standards (Hanseth and Monteiro, 1997). The specification of interfaces through standards stipulates how components can interface with each other (Baldwin and Clark, 2006).

The case of TradeNet in Singapore (Kling and Iacono, 1984; Tan, 1998; Lyytinen and Damsgaard, 2011) provides an example of DI architecture regulation through performance targets that specify the interfaces between components. As an important hub for international trade, the state of Singapore came to realise that an efficient DI for the exchange of trade-related data, such as customs declarations, would strengthen its position. When the DI was first established, EDI was the most popular technology being used to enable the organisational exchange of data. Initially, all the different actors involved in trade, composed of various governmental agencies and private actors, focused on developing bilaterally agreed upon EDI connections with each other. But this approach was expensive and slow. Singapore’s National Computer Board therefore intervened to overcome sluggish adoption by issuing directives that mandated an EDI standard that was to be used in governmental agencies and dictated how interactions were to be conducted between agencies and companies and between companies. The legal basis of these directives included the

Electronic Transactions Act, the Customs Act, and the Regulation of Imports and Exports Act, which together enabled the issuing of specific directives that regulated the interfaces between components, specifying EDI syntax, data items, and submission protocols for trade-related data exchange in Singapore (Tan, 1998). In less than two years, 92% of all trade reporting was moved from physical papers to EDI. The regulation of visible design rules through performance targets concerning the specification of interfaces in TradeNet therefore mitigated operational risks and brought about efficiencies.

Regulatory intervention through the specification of modular arrangements. While the critical role of de jure standards to interoperability between heterogenous components in a DI may be the most well-known example of DI regulation’s impact on design rules, the regulation of performance targets can also impact the other two dimensions of visible design rules (Baldwin and Clark, 2000). This form of regulation can specify architecture by defining what components the architecture can be composed of and their functional arrangement. For example, the definition of a technical specification (i.e. an interface) that is legally binding typically describes whom or what the regulation applies to (i.e. provides a component definition). Thus, regulation can define what type of component is used and its provenance or source.

An example of how regulation can be used to intervene in the arrangement of components in a specific part of a DI’s architecture comes from in network neutrality laws (see, Kramer and Wiewiorra, 2012¨ ). Network neutrality laws regulate the interconnection of telecom networks and the operation of broadband data networks to restrict the potential of ISPs discriminating in the transportation and charging of data in a network (Sindik, 2021). For example, in Chile, network neutrality laws were introduced in 2010 as a direct result of social media companies’ moves to subsidise mobile data usage for their specific services (Triviño et al., 2021). In the US, the Federal Communications Commission (FCC) was instructed to reclassify broadband internet service as a telecommunications service according to the Communications Act of 1934 (Faulhaber et al., 2017).

The FCC followed this recommendation in 2015, and from then on, ISPs in the US were not able to give preference to or practice price discrimination between data. In 2017, the FCC subsequently voted to repeal the classification of broadband as a telecommunications service, meaning that ISPs were no longer considered common carriers subject to specific antidiscrimination laws (Sindik, 2021).

Network neutrality laws such as the US Communications Act of 1934 are performance target regulations that affect the modular arrangements of DIs such as broadband networks. Before 2017, the US ISPs were only given exemptions for discrimination to prevent societally harmful activities such as spam, malware, and illegal content (Triviño et al., 2021). After the classification was changed, ISPs were given more freedom to discriminate on commercial grounds.

In terms of DI architecture, network neutrality law works to undo (or prevent) commercially motivated forced integration (coupling) between components, for example, across layers in a telecommunications network. In an extreme case, without network neutrality enforcement, the separation and independence between components in a network may be lost, putting the service and content layers at risk (by enabling any service or content on any network), with the possibility of the internet being splintered (Plantin et al., 2018) into commercially motivated proprietary design verticals. Elsewhere, stipulating which bindings between components cannot be made is motivated by data privacy concerns (see Tikkinen-Piri et al., 2018). By using performance targets associated with these modular architectures to regulate them, governments can ensure that the internet remains open and that monopolistic behaviour is contained. These laws effectively regulate the possible arrangement of components in a particular part of a DI.

Regulatory intervention through the specification of functional criteria. Finally, the regulation or specification of modular interfaces is also linked to the level of control over the functional criteria of a component in terms of the guaranteed output and input quality a component must meet to qualify for inclusion. Specifications of functional criteria through regulation take place alongside specifications of modular arrangements. These are tests that one component must pass to connect to other components (Baldwin and Clark, 2006). Using the network neutrality example, such criteria are found in the valid grounds for discrimination. ISPs may refuse connections from components that either pose technical risks (cyberthreats, network congestion, etc.) or are linked to criminal activity (Kramer and Wiewiorra, 2012¨ ).

Functional criteria are necessary to ensure that a single component des not negatively affect the overall architecture (Baldwin and Clark, 2000). In the EU, it is increasingly recognised that the growing digitalisation of financial infrastructures has created ‘a broad range of entry points through which an FMI [financial market infrastructure] could be compromised’ (ECB, 2019: 2) Furthermore, increasing digital interconnectedness elevates the risk that incidents propagate across the infrastructure with potential systemic effects on financial stability (EBA, 2019; ECB, 2019). Regulators are therefore developing criteria for who and what can connect to Europe’s financial infrastructures to ensure resilience (see EBA, 2019; JCESA, 2019; European Commission, 2020). Authorities are directly calling for regulation that specifies tests and test criteria, which actors must comply with for inclusion in financial infrastructures (EBA, 2019).

This has been exemplified by the Revised Payment Services Directive (PSD2) adopted by the European Parliament in October 2015 (see Zachariadis and Ozcan, 2017). The directive specifies functional criteria that go hand in hand with regulation that enforces the other two types of design rules. PSD2 empowers the European Commission to ‘specify how competent authorities and market participants shall comply with the obligations laid down in the directive (European Commission, 2015a). Financial regulators in the EU have implemented PSD2 in three ways (Zachariadis and Ozcan, 2017). First, they have regulated interfaces to specify how banks can design APIs that are used to access information, for example, concerning bank accounts. Second, they have defined the components of third-party financial services by specifying modular arrangements. Third, they have dictated quality criteria such as the cybersecurity control capacities that third-party services must meet to be granted access to banks’ APIs. The technical specification ETSI TS 119 495 defines these design rules as binding regulations (European Commission, 2015b). Regulation therefore touches all three dimensions of the visible design rules that govern a DI as a modular architecture. However, the regulatory intervention only addresses a specific part of the payment DI to have the effect of dissolving an architectural control point that was previously identified as limiting possibilities for innovation. In the final analysis, the architectural regulatory intervention leading to PSD2 was introduced to minimise the risks to consumers from monopolistic actors by providing them with greater choice through marketplace competition and alternatives to the established actors.

## Regulating modular design parameters through activity specification

In addition to visible design rules that control how components form a whole, modular architectures consist of individual components whose design is governed by design parameters hidden from the wider external system (Baldwin and Clark, 2000). Hiding these parameters gives the creator of an individual component complete freedom over the component’s design on the condition that they adhere to the visible design rules. However, regulation can specify the internal functioning and design of a component so that they are no longer solely under the creator’s purview (Parnas, 1972).

Regulation through activity specification addresses how something is done. Therefore, DI regulation can use activity specification to restrict variation in the design of components in a DI architecture, reducing the degrees of freedom in the design. Activity specification in modular design is the degree to which the design parameters that define the internal functioning of components are specified by an external (regulating) actor or remain unspecified as hidden design parameters (Baldwin and Clark, 2000) to be defined by the actor creating the component. The specification of modular design parameters covers two elements: materials and methods (May, 2003; Rowell and van Zeben, 2021).

Regulatory intervention through the specification of materials. The first approach to specifying modular design parameters concerns the materials from which a component is constructed. These specifications may address the types of physical materials, such as hardware components, or virtual materials, such as code, that can be used. In addition, the specification of materials can cover their provenance, such as the source or creator of those materials. Materials specification can either describe what is legal (positive discrimination) or what is illegal (negative discrimination).

The issue of modular design specification has recently come to public attention with the building of 5G mobile networks, where governments have intervened to prevent the inclusion of equipment from certain providers for the stated reasons of upholding national security. For example, the Defending America’s 5G Future Act prohibits transactions involving a perceived foreign adversary’s information and communications technology when such transactions are at risk of sabotage or subversion (Ferrare, 2019). The act was introduced to the US Senate in July 2019 and put Huawei and ZTE on the blacklist for equipment manufacturers, meaning their equipment must be excluded from the construction of 5G networks.

In this case, DI regulation is being used to restrict modular design through the negative discrimination of specified materials and is motivated by the risk of the materials being compromised by the equipment provider. Materials are understood here in their widest sense to encompass digital information as well as physical components. The logic behind materials specification in a component of a DI is similar to the blacklisting of materials in more traditional settings, such as the banning of toxic chemicals in environmental applications (Gunningham, 2002; Rowell and van Zeben, 2021). In the construction of 5G networks, the potential negative cost to society is critical, so network providers are free to choose from equipment providers that are not on the blacklist.

Regulatory intervention through the specification of methods. The second approach to specifying modular design parameters concerns the method by which a component accomplishes a task. In the context of DIs, one can think of the method as the process steps that are fulfilled or the algorithm that is executed within the component.

We previously noted that regulatory intervention through the specification of functional criteria is directed at eliminating and controlling risk in financial infrastructures in Europe, for example, by specifying tolerance levels (European Commission, 2020). However, method specifications are also used as a means to enhance resilience in financial infrastructures. For example, implementation guidelines such as the ECB’s Cyber resilience oversight expectations for financial market infrastructures identify ‘a set of practices… to comply with the Guidance’ (ECB, 2019: 6). These implementation practices contain how-to instructions for incident reporting, governance, control of suppliers, updates to software, life cycle management of hardware, and so on (see ECB, 2019). Following the methods or practices that are outlined in this and other documents is a means of demonstrating regulatory compliance to overseeing authorities.

Imposing method specifications to ensure resilience within financial infrastructures is motivated by the threat of failure propagating through tightly coupled components such that the cascading effects of any damage cannot be contained (EBA, 2019; European Commission, 2020). In this way the ECB (2019: 6) notes: ‘As a result of their interconnectedness, cyber-attacks could arise through FMIs’ participants, linked FMIs, service providers, vendors or vendor products… Unlike physical operational disruptions, cyber risk posed by an interconnected entity is not necessarily related to the degree of that entity’s relevance to the FMI’s business. From a cyber perspective, a small-value/volume participant or a vendor providing noncritical services may be as risky as a major participant or a critical service provider’. Consequently, the need to have the right measures in place extends beyond dominant DI actors, such as large banks, to encompass minor DI actors, such as fintech start-ups, software developers, and infrastructure providers (EBA, 2019; ECB, 2019). The specification of methods is an effective approach to ensure a minimum level of resilience in each part of an infrastructure. This approach is all the more effective for those minor DI actors that may not have the competences to develop their own cybersecurity strategies to meet performance targets.

## Discussion

When testifying in the US Congress on the need to regulate the internet, Mark Zuckerberg, CEO of Meta (formerly Facebook), expressed the following: ‘I think the real question, as the internet becomes more important in people’s lives, is what is the right regulation, not whether there should be or not’. We think that this quote has general applicability to all DIs of societal importance. One of the key strengths of a DI is the potential for innovation through decentralised, self-reinforcing processes of modifying and repurposing technology (Yoo et al., 2010) that unleashes creativity and unanticipated possibilities. However, for the same reasons, DIs that are of societal importance cannot be left to evolve without consideration of how modifications to them will impact their ability to support the common good.

## Reflection on findings and underlying assumptions

The thrust of our findings is that DI regulation can be used to restrict some forms of behaviour while mandating others. Our analysis shows that DI regulation can impact both the visible design rules (Baldwin and Clark, 2000) that guide how components can be combined into a whole and the hidden design parameters (Baldwin and Clark, 2000) by which individual components are designed. We now discuss these findings by revisiting the assumptions that premise our analysis as articulated at the end of the literature review.

DI regulation and architecture as a continuum. Our first assumption was that the distinction between modular and integrated architecture in DIs represents a continuum rather than two discrete states. Consequently, regulation influences architecture in the sense of more or less rather than either/or because it is not realistic to think that any DI of societal importance would be positioned at these extremes. Accepting that the influence of regulation takes effect in terms of ‘more or less’ fosters consideration of how much regulation is necessary. This is a relevant consideration given the substantial cost of regulative compliance (Butler and O’Brien, 2019) but also because DIs are susceptible to the paradox of control (Eaton et al., 2015).

Informing this consideration, our model shows that we can think of ‘more or less’ as two different non-exclusive forms of DI regulation. As depicted in Figure 4, the relationship between the two forms of regulation is orthogonal. In the figure, two idealised states form the end points on the continuum of architectural specificity. At the top-right corner, DI regulation both specifies how components can connect and how individual components are designed; the architecture is bound by regulation. At the bottom-left corner, there is no regulation in place to restrict modifications to the DI; the architecture is unbound from regulation. The closer to the extreme of being completely bound by regulation, the higher the degree of architectural specificity concerning the DI relative to the governmental objectives of the regulation.

Distinguishing between the two forms of regulation and their distinct effects on innovation makes it possible to redefine the question of the extent of regulation to consider what form it should take. DI regulation is thereby enabling one form of innovation while simultaneously inhibiting another form of innovation.

DI regulation and the heterogeneity of architecture. Our second assumption was not only that DI architectural modularity is a continuum but also that it might vary across different parts of DI architecture. This corresponds to observations made in previous research (Rodon and Silva, 2015) concerning variations in modularisation across DI architecture. Conceptually, this mirrors the idea that DIs structured as innovation platforms (Baldwin and Woodard, 2009; Bonina and Eaton, 2020) would benefit from an approach involving spatial separation to facilitate any innovation. In a regulated DI, the spatial separation does not need to be between core and peripheral architectures as in a platform because any location can be subject to a different form of regulation. For example, regulation can be applied in different ways across distinct layers (i.e. the content vs the service layer) in a layered architecture. An implication of this finding is that we can further redefine the questions of how much and what form of regulation should exist to include where regulation should be applied. Consider, for example, the Norwegian e-health DI described by Øvrelid and Bygstad (2019; 2020). Here, there are elements of the DI that may warrant further governmental control in comparison to others, such as parts that cause more concerns about patient confidentially or are essential to deliver key hospital functions (see, Tikkinen-Piri et al., 2018).

Extending this reasoning also allows us to consider the impact that DI regulation is allowed to have because of the recognition that architectural hybridity, consistent with our second assumption, makes it possible to simultaneously regulate visible design rules and modular design parameters in different or similar spaces in a DI. The orthogonal relationship between the two forms of regulation means that their uses are not necessarily in conflict and may even be synergistic.

In each of the examples we used to illustrate the model in Figure 3, we highlighted a specific type of regulatory intervention. In most real-life cases, several different interventions would be at play at the same time. For example, the case of PSD2 in Europe illustrates the argument that regulation through performance targets can establish component interfaces and functional criteria that increase modularity at a particular point in the DI (Zachariadis and Ozcan, 2017). However, PSD2 has several additional articles. At least one of them contains activity specification. Regarding the applicability to PSD2 regulation, not only do third-party digital services have to comply with set functional criteria (as performance targets) but they must also follow stipulated methods specifications for the identification of users of any payment services. While this does indeed restrict the degree of freedom in the modular design, it could also be seen as a necessary piece of regulation to allow for increased modularity through interfaces and functional criteria. Thus, the uses of the two different forms of regulation are synergistic (both are needed for the other to be relevant) and paradoxical in that the regulation both constrains and enables innovation at the same time.

![](/api/attachments/AEYTZB8T/fulltext/images/43637eebab7affb09f9e4e57625d63578a9ce62e7e813d3ca0d8a1a50784031d.jpg)  
Figure 4. The orthogonal relationship between the two forms of regulatory intervention in DI architecture.

DI regulation as architectural interventions in modularity. Our third assumption was that although DI architecture is sometimes regarded as endogenous (Agarwal and Tiwana, 2015), a DI architecture can be changed through deliberate intervention by actors such as governments. Our case illustrations show that deliberate interventions are not only theoretically possible but also occurring in the real world.

Treating DI regulation as a form of intervention means that it can be understood as relational in at least two ways. This implication affects our third assumption concerning the evolution of DI architecture over time. An initial relational consideration is that applicability is directly contingent on the actions of other actors. Thus, the questions of how much, what, and where can be even further elaborated with consideration of when. A government intervenes through regulation because actors are either doing something or refraining from doing something (see Ogus, 2008). While risk might be a driver for proactive regulation, because of the uncertainty of the effects of DI innovation and the ongoing repurposing of components, certain behaviours can only be regulated after they materialise.

A second implication of considering regulation as an intervention in relation to actor behaviour is that it brings to the fore consideration of the DI’s stage in its evolutionary life cycle. Hanseth and Lyytinen (2010) suggest a temporally separated approach to facilitate DI evolution that is based on a life cycle view of DIs. For example, they recommend first emphasising the establishment of a DI by building basic essential features through centralised control and architectural stability. Following this, they propose paying attention to architectural flexibility and the distribution of innovative activity. In this way, distinct types of regulatory interventions become appropriate to facilitate societally beneficial DI innovation at varying stages in the DI’s life cycle.

Consequently, with the conceptual model developed in this paper, different types of regulatory interventions may need to be mediated by different locations of a DI architecture at distinct points in time and based on what other actors are doing to promote DIs that are most beneficial to society.

## Theoretical contributions

Our work contributes to research on the governmental regulation of DI innovation in three ways. First, there is a paucity of research on DIs that has explicitly focused on the influence of regulation, and therefore, little effort has been made to conceptualise such regulation in relation to DIs. We provided a more nuanced view by conceptualising DI regulation as a form of command-and-control regulation (Ogus, 2008). We distinguished between two different forms of DI regulation that express legal restrictions as performance targets or activity specification (see Ogus, 2008). This construct development provides a conceptual foundation that can serve as the basis for future research on governmental influence on DIs.

Second, to link DI regulation to DI innovation, we drew on modular systems theory (Schilling, 2000), which foregrounds the critical role of architecture in conditioning innovation. Our contribution in relation to the development of the DI architecture construct is the consolidation of previous observations into three assumptions of how architecture in DIs manifests as continuous, heterogenous, and evolving (Hanseth and Lyytinen, 2010). These architectural characterisations serve as an important part of the explanatory framework seeking to capture DI innovation. While our purpose was to explain the impact of governmental regulation, this characterisation should be a relevant starting point for anyone who wishes to theorise about DI innovation more broadly.

Third, we used modular systems theory (Schilling, 2000) to develop relationships between the constructs of DI regulation and innovation. The explanatory power of this association goes beyond what has been presented in previous research and serves to reconcile seemingly contradictory observations made at different places in the literature. We showed how DI regulation through performance targets impacts visible design rules, while regulation through activity specification impacts the design of individual components. Thus, we revealed that these forms of regulation are not mutually exclusive, that they can be applied to different extents and at various locations simultaneously, and that they can have paradoxical effects on DI innovation, enabling and inhibiting (different forms of) innovation at the same time. Our conceptualisation and the associated terminology provide a basis to explain and articulate the effects of DI regulation in a way that has not been previously presented in the literature.

## Practical implications

Two types of actors can benefit from our model: regulators responsible for designing, implementing, and enforcing regulation and actors whose activities are impacted by DI regulation. For regulators, our model provides a framework through which recommendations (Paech, 2019) for the regulation of DIs can be formulated, articulated, and implemented. To facilitate communication of our conceptual model among practitioners (Montero and Finger, 2021), each of the five different interventions (three as design rules and two as hidden design parameters) can be expressed as regulatory levers.

Our research demonstrated that the application of these levers is not mutually exclusive. In this way, our model helps regulators consider how to apply the levers in combination and to different extents simultaneously in separate architectural locations. Furthermore, the application of these levers can be dynamic so that DI regulation can be tuned to changing societal needs over time, which in turn facilitates the formulation of longer-term regulatory strategies.

For actors directly and indirectly affected by DI regulation, our model provides a framework through which they can analyse and respond to the impacts of regulatory action.

The five different levers of our model make it possible for these actors to predict and pre-empt regulatory policy. The levers provide different dimensions for the design of modular architectures so that the response to the application of one lever in a specific dimension can potentially be compensated for by (re)designing in another.

Finally, our model makes it possible for actors (potentially) affected by regulation to lobby regulators and shape regulation in ways that both benefit society and protect the interests of commercial actors. For example, different combinations of regulatory levers may yield the same beneficial effect on society while either harming or benefitting a commercial actor. Being able to analyse and communicate the expected impact of regulation is a prerequisite for actors to engage in the political processes surrounding regulation.

## Conclusion

This paper developed a conceptual model that shows how regulation concerning DI innovation is mediated by a DI’s architecture. By drawing on modular systems theory (Schilling, 2000), we explained how regulatory interventions can affect architecture in two fundamentally different ways. The first is through regulating performance targets and impacts the visible design rules affecting the combination of components in an architecture. The second concerns the definition of design parameters and impacts the internal design of components. By drawing on a range of examples of regulatory interventions in DIs, we illustrated how these forms of regulation are implemented and that their use is not mutually exclusive. In doing so, we presented a nuanced view of the effect of regulation on DI innovation, which stands in contrast to prior literature on the subject. We also explained how regulatory interventions may have a paradoxical impact on DIs because they can both enable and inhibit (different forms of) innovation at the same time.

## Declaration of Con<sup>fl</sup>icting Interests

The author(s) declared no potential conflicts of interest with respect to the research, authorship, and/or publication of this article.

## Funding

The author(s) received no financial support for the research, authorship, and/or publication of this article.

## ORCID iDs

Stefan Henningsson  https://orcid.org/0000-0003-3865-7086 Benjamin D Eaton  https://orcid.org/0000-0001-8107-2986

## Supplemental Material

Supplemental material for this article is available online.

## Notes

1. See the literature review for extended definitions of DI innovation and DI regulation.

2. In this paper, we see a DI as a subclass of the more general information infrastructure. A DI specifically integrates heterogenous digital technologies to enable digital services and ultimately the exchange of digital content (data).

3. In this paper, we follow previous examples in the information systems literature to speak about the individual parts of the digital artefact as components, rather than modules, since very few digital artefacts are ideal modular architectures, something that also applies to real world DIs.

4. Baldwin and Clark (2000) use the terms architecture, interfaces, and standards. We adapted their terminology to avoid confusion with other central concepts in this paper.

5. Appendix B provides multiple illustrations from diverse contexts and industries.

6. PSD2 is the EU’s Revised Payment Services Directive (EU 2015/2366).

7. Note, this meaning of standard is slightly different from the meaning of ‘functional standards’, a term sometimes used instead of functional criteria in the context of visible design rules (see Clark, 1985), and is more closely associated with the specification of interfaces between components.

## References

Aanestad M, Grisot M, Hanseth O, et al. (2017). Information infrastructures for eHealth. In: Hanseth., Aanestad M and Vassilakopoulou P, eds. Information Infrastructures within European Health Care. Cham, Switzerland: Springer

Aanestad M and Jensen TB (2011) Building nation-wide information infrastructures in healthcare through modular implementation strategies. The Journal of Strategic Information Systems 20(2): 161–176.

Agarwal R and Tiwana A (2015) Editorial—evolvable systems: through the looking glass of IS. Information Systems Research 26(3): 473–479.

Baldwin C and Clark K (2000) Design Rules. Cambridge, Ma: MIT Press.

Baldwin C and Von Hippel E (2011) Modeling a paradigm shift: from producer innovation to user and open collaborative innovation. Organization Science 22(6): 1399–1417.

Baldwin CY and Clark KB (2006) Modularity in the design of complex engineering systems. In: BrahaA D, Minai A and Bar-Yam Y, eds. Complex engineered systems. Cham, Switzerland: Springer.

Baldwin CYand Woodard CJ (2009) The architecture of platforms: a unified view. In: Gawer A, ed. Platforms, markets and innovation. Cheltenham, UK: Edward Elgar.

Bauer JM and Knieps G (2018) Complementary innovation and network neutrality. Telecommunications Policy 42(2): 172–183.

Bazarhanova A, Yli-Huumo J and Smolander K (2020) From platform dominance to weakened ownership: how external regulation changed Finnish e-identification. Electronic Markets 30(3): 525–538.

Bonina C and Eaton B (2020) Cultivating open government data platform ecosystems through governance: lessons from Buenos Aires, Mexico City and Montevideo. Government Information Quarterly 37(3): 101479.

Boyer R (1998) Technical change and the role of ‘regulation. In: DosiC G, Nelson FR and Soete L, eds. Technical Change and Economic Theory. London, UK: Pinter Publishers.

Braa J, Hanseth O, Heywood A, et al. (2007) Developing health information systems in developing countries: the flexible standards strategy. Mis Quarterly 31(2): 381–402.

Butler T and O’Brien L (2019) Understanding RegTech for digital regulatory compliance. In: Disrupting Finance. Cham: Palgrave Pivot.

Bygstad B and Øvrelid E (2020) Architectural alignment of process innovation and digital infrastructure in a high-tech hospital. European Journal of Information Systems 29(3): 220–237.

Capello R and Lenzi C (2021) 4.0 Technologies and the rise of new islands of innovation in European regions. Regional Studies 55(10–11): 1724–1737.

Ciborra C and Hanseth O (2000) Introduction: from control to drift. In: Ciborra C., ed. From Control to Drift. Oxford, UK: Oxford University Press.

Ciborra CU (2009) Interpreting e-government and development: efficiency, transparency or governance at a distance? In: AvgerouG C, Lanzara F and Willcocks LP, eds. Bricolage, Care and Information. Heidelberg, Germany: Springer.

Clark KB (1985) The interaction of design hierarchies and market concepts in technological evolution. Research Policy 14(5): 235–251.

Contini F (2014) Let agency circulate: architectures and strategies for Pan-European e-Justice. In: Contini F and Lanzara GF, eds. The Circulation of Agency in E-Justice. Berlin, Germany: Springer.

Contini F and Lanzara GF (2014a) The challenge of interoperability and complexity in European Civil Proceedings Online. In: Contini F and Lanzara GF, eds. The Circulation of Agency in E-Justice. London, UK: Springer.

Contini F and Lanzara GF (2014b) The Circulation of Agency in E-Justice: Interoperability and Infrastructures for European Transborder Judicial Proceedings. London, UK: Springer.

Contini F and Mohr R (2014) How the Law can make it simple: easing the circulation of agency in e-Justice. In: Contini F and Lanzara GF, eds. The Circulation of Agency in E-Justice. London, UK: Springer, 53–79.

Damsgaard J and Lyytinen K (1998a) Contours of diffusion of electronic data interchange in Finland: overcoming

technological barriers and collaborating to make it happen. The Journal of Strategic Information Systems 7(4): 275–297.

Damsgaard J and Lyytinen K (1998b) Governmental intervention in the diffusion of EDI. In: Andersen KV, ed. EDI and Data Networking in the Public Sector. Dordrecht, Netherlands: Kluwer Academic Publishers, 13–41.

Eaton B, Elaluf-Calderwood S, Sorensen C, et al. (2015) Distributed tuning of boundary resources: the case of Apple’s iOS service system. MIS Quarterly 39(1): 217–243.

Eaton B, Hedman J and Medaglia R (2018) Three different ways to skin a cat: financialization in the emergence of national e-ID solutions. Journal of Information Technology 33(1): 70–83.

EBA (2019) European Banking Authority Guidelines on ICT and Security Risk Management. France: European Banking Authority.

ECB (2019) European Central Bank Cyber Resilience Oversight Expectations for Financial Market Infrastructures. Frankfurt, Germany: European Central Bank.

European Commission (2015a) Directive (EU) 2015/2366 on Payment Services in the Internal Market. Brussels; European Commission

European Commission (2015b) ETSI TS 119 495. Electronic Signatures and Infrastructures (ESI); Sector Specific Requirements; Qualified Certificate Profiles and TSP Policy Requirements under the payment services Directive. Brussels; European Commission

European Commission (2020) Proposal for a Regulation of the European Parliament and of the Council on Digital Operational Resilience for the Financial Sector and Amending Regulations (EC) No 1060/2009. (EU) No 648/2012, (EU) No 600/2014 and (EU) No 909/2014. Brussels; European Commission

Faulhaber GR, Singer HJ and Urschel AH (2017) The curious absence of economic analysis at the Federal Communications Commission: an agency in search of a mission. International Journal of Communication 11: 1214–1233.

Ferrare T (2019) The 5G Effect: New Threats, New Defense, and Mounting Political Tension from the Next Era of Mobile Networks. Utica, NY: Utica College.

Finck M (2018) Digital co-regulation: designing a supranational legal framework for the platform economy. European Law Review 43(1): 47–68.

Fink L, Shao J, Lichtenstein Y, et al. (2020) The ownership of digital infrastructure: exploring the deployment of software libraries in a digital innovation cluster. Journal of Information Technology 35(3): 251–269.

Flew T and Wilding D (2021) The turn to regulation in digital communication: the ACCC’s digital platforms inquiry and Australian media policy. Media Culture & Society 43(1): 48–65.

Ford CL (2008) New Governance, compliance, and principlesbased securities regulation. American Business Law Journal 45(1): 1–60.

Gheorghe AV, Masera M, Vries LD, et al. (2007) Critical infrastructures: the need for international risk governance. International Journal of Critical Infrastructures 3(1–2): 3–19.

Gilson LL and Goldberg CB (2015) Editors’ comment: So, what is a conceptual paper? Group & Organization Management 40(2): 127–130.

Grisot M, Hanseth O and Thorseng AA (2014) Innovation of, in, on infrastructures: articulating the role of architecture in information infrastructure evolution. Journal of the Association for Information Systems 15(4): 197–219.

Gunningham N (2002) Beyond compliance: next generation environmental regulation. In: Johnstone R and Sarre R, eds. Regulatory Institutions Network, ANU, paper presented at the Current Issues in Regulation: Enforcement and Compliance Conference. Melbourne, Australia: Australian Institute of Criminology, 49–60.

Hallinan A (2021) Operational resilience in the financial sector: evolution and opportunity. Journal of Financial Transformation 53: 108–115.

Hanseth O and Lyytinen K (2010) Design theory for dynamic complexity in information infrastructures: the case of building internet. Journal of Information Technology 25(1): 1–19.

Hanseth O and Modol JR (2021) The dynamics of architecturegovernance configurations: an assemblage theory approach. Journal of the Association for Information Systems 22(1): 5.

Hanseth O and Monteiro E (1997) Inscribing behaviour in information infrastructure standards. Accounting, management and information technologies 7(4): 183–211.

Hanseth O, Monteiro E and Hatling M (1996) Developing information infrastructure: the tension between standardization and flexibility. Science, Technology, & Human Values 21(4): 407–426.

Henderson RM and Clark KB (1990) Architectural innovation: the reconfiguration of existing product technologies and the failure of established firms. Administrative Science Quarterl35(1): 9–30.

Henfridsson O and Bygstad B (2013) The generative mechanisms of digital infrastructure evolution. MIS quarterl 37(3): 907–931.

Henriksen HZ and Damsgaard J (2007) Dawn of E-Government– An institutional analysis of seven initiatives and their impact. Journal of Information Technology 22(1): 13–23.

Hulland J (2020) Conceptual review papers: revisiting existing research to develop and refine theory. AMS Review 10(1): 27–35.

Jaakkola E (2020) Designing conceptual articles: four approaches. AMS review 10(1): 18–26.

JCESA (2019) Joint Committee European Supervisory Authorities Joint Advice of the European Supervisory Authorities to the European Commission on the need for legislative improvements relating to ICT risk management requirements in the EU financial sector. Ranson, WV: JCESA.

Jensen T, Vatrapu R, Bjørn-Andersen N, et al. (2018) Avocados crossing borders: the problem of runaway objects and the

solution of a shipping information pipeline for improving international trade. Information Systems Journal 28(2): 408–438.

Kallinikos J (2009) The regulative regime of technology. In: Contini F and Lanzara GF, eds. ICT and Innovation in the Public Sector. London, UK: Palgrave Macmillan, 66–87.

Khemani RS and Shapiro DM (1993) Glossary of Industrial Organisation Economics and Competition Law. Paris, France: OECD.

Kling R and Iacono S (1984) Computing as an occasion for social control. Journal of Social Issues 40(3): 77–96.

Knol A and Tan Y-H (2018) The cultivation of information infrastructures for international trade: stakeholder challenges and engagement reasons. Journal of Theoretical and Applied Electronic Commerce Research 13(1): 106–117.

Kohli R and Melville NP (2019) Digital innovation: a review and synthesis. Information Systems Journal 29(1): 200–223.

Koutsikouri D, Lindgren R, Henfridsson O, et al. (2018) Extending digital infrastructures: a typology of growth tactics. Journal of the Association for Information Systems 19(10): 1001–1019.

Kramer J and Wiewiorra L (2012) Network neutrality and con-¨ gestion sensitive content providers: Implications for content variety, broadband investment, and regulation. Information Systems Research 23(4): 1303–1321.

Lanzara GF (2014) The circulation of agency in judicial proceedings: designing for interoperability and complexity. In: Contini F. and Lanzara G. F., eds. The Circulation of Agency in E-Justice. London, UK: Springer, 3–32.

Lyytinen K and Damsgaard J (2011) Inter-organizational information systems adoption–a configuration analysis approach. European journal of information systems 20(5): 496–509.

May P (2003) Performance-based regulation and regulatory regimes: the saga of leaky buildings. Law & Policy 25(4): 381–401.

Montero J and Finger M (2021) The Rise of the New Network Industries: Regulating Digital Platforms. London, UK: Routledge.

Nambisan S, Lyytinen K, Majchrzak A, et al. (2017) Digital innovation management: reinventing innovation management research in a digital world. MIS quarterly 41(1): 223–238.

Napieralski A (2019) Collecting data at EU smart Borders: data protection challenges of the new entry/exit system. Zeitschrift für kritik - recht - gesellschaft 1: 199–209.

Ogus A (2008) Command and control regulation. In: Cane P and Conaghan J, eds. The New Oxford Companion to Law. Oxford, UK: Oxford University Press.

Øvrelid E and Bygstad B (2019) The role of discourse in transforming digital infrastructures. Journal of Information Technology 34(3): 221–242.

Paech P (2019) Thirty recommendations on regulation, innovation and finance. In: Expert Group on Regulatory Obstaclesto Financial Innovation (ROFIEG), Final Report to the European Commission. Brussels: European Commission.

Parnas DL (1972) On the criteria to be used in decomposing systems into modules. Communications of the ACM 15(12): 1053–1058.

Payne A, Frow P and Eggert A (2017) The customer value proposition: evolution, development, and application in marketing. Journal of the Academy of Marketing Science 45(4): 467–489.

Pipek V and Wulf V (2009) Infrastructuring: toward an integrated perspective on the design and use of information technology. Journal of the Association for Information Systems 10(5): 447–473.

Plantin J-C, Lagoze C, Edwards PN, et al. (2018) Infrastructure studies meet platform studies in the age of Google and Facebook. New Media & Society 20(1): 293–310.

Rodon Modol J and Eaton B (2021) Digital infrastructure evolution as generative entrenchment: The formation of a coreperiphery structure. Journal of Information Technology 36: 342–364. Published online in advance.

Rodon J and Silva L (2015) Exploring the formation of a healthcare information infrastructure: hierarchy or Meshwork? Journal of the Association for Information Systems 16(5): 394–417.

Rolland KH, Mathiassen L and Rai A (2018) Managing digital platforms in user organizations: the interactions between digital options and digital debt. Information Systems Research 29(2): 419–443.

Rolland KH and Monteiro E (2002) Balancing the local and the global in infrastructural information systems. The Information Society 18(2): 87–100.

Rowell A and van Zeben J (2021) Regulatory Instruments. In: Rowell A and van Zeben J, eds. A Guide to US Environmental Law. Berkeley, California: University of California Press, 59–76.

Rukanova B, Henningsson S, Zinner Henriksen H, et al. (2018) Digital trade infrastructures: a framework for analysis. Complex Systems Informatics and Modeling Quarterly. 2018(14): 1–21.

Rukanova B, Van Stijn E, Henriksen HZ, et al. (2009) Under standing the influence of multiple levels of governments on the development of inter-organizational systems. European Journal of Information Systems 18(5): 387–408.

Sanchez R and Mahoney JT (1996) Modularity, flexibility, and knowledge management in product and organization design. Strategic management journal 17(S2): 63–76.

Sarker S, Henningsson S, Jensen T, et al. (2021) The use of blockchain as a resource for combating corruption in global shipping: an interpretive case study. Journal of Management Information Systems 38(2): 338–373.

Schilling MA (2000) Toward a general modular systems theory and its application to interfirm product modularity. Academy of management review 25(2): 312–334.

Shadikhodjaev S (2021) Technological neutrality and regulation of digital trade: how far can we go? European Journal of International Law 32(4): 1221–1247.

Simon HA (1996) The Sciences of the Artificial. Boston, MA: MIT Press.

Sinclair D (1997) Self-regulation versus command and control? Beyond false dichotomies. Law & Policy 19(4): 529–559.

Sindik A (2021) Administrative law and the federal communications commission. Communication Law and Policy 26(3): 312–335.

Talias M (2021) Collaborative regulation: collaborative governance in regulation. In: Lahat N, Sher-Hadar L and Galnoor I, eds. Collaborative Governance. Cham, Switzerland: Palgrave Macmillan, 165–189.

Tan M (1998) Plugging into the wired world: perspectives from Singapore. Information Communication & Society 1(3): 217–245.

Tekir G (2020) Huawei, 5G network and digital geopolitics. International Journal of Politics and Security 2(4): 113–135.

Tikkinen-Piri C, Rohunen A and Markkula J (2018) EU general data protection regulation: changes and implications for personal data collecting companies. Computer Law & Security Review 34(1): 134–153.

Tilson D, Lyytinen K and Sørensen C (2010) Research commentary—digital infrastructures: the missing IS research agenda. Information systems research 21(4): 748–759.

Triviño R, Franco-Crespo A and Ochoa-Urrego L (2021) Network neutrality: the case of five south American countries. In: Cruz M, Botto-Tobar H and D´ıaz Cadena A, eds. Artificial Intelligence, Computer and Software Engineering Advances: Proceedings of the CIT 2020 Volume 1. Ecuador: Springer Quito, 150–161.

Ulrich K (1995) The role of product architecture in the manufacturing firm. Research Policy 24(3): 419–440.

Wang P (2021) Connecting the parts with the whole: toward an information ecology theory of digital innovation ecosystems. MIS Quarterly 45(1): 397–422.

Wiener JB (2004) The regulation of technology, and the technology of regulation. Technology in Society 26(2–3): 483–500.

Yoo Y, Henfridsson O and Lyytinen K (2010) Research commentary—the new organizing logic of digital innovation: an agenda for information systems research. Information systems research 21(4): 724–735.

Zachariadis M and Ozcan P (2017) The API Economy and Digital Transformation in Financial Services: The Case of Open Banking. Belgium: SWIFT Institute Working. Paper No. 2016-001.

Zorina A and Dutton WH (2021) Theorizing actor interactions shaping innovation in digital infrastructures: the case of residential internet development in Belarus. Organization Science 32(1): 156–180.

Zuboff S (1988) In the Age of the Smart Machine: The Future of Work and Power. New York City, NY: Basic Books, Inc.

Zuboff S (2019) The Age of Surveillance Capitalism: The Fight for a Human Future at the New Frontier of Power. London, UK: Profile books.

## Author Biographies

Stefan Henningsson is a Professor at Department of Digitalization, Copenhagen Business School, Denmark. His research addresses managerial aspects of IT in contexts that include corporate mergers and acquisitions, international trade processes, and the digital transformation of firms. His work has been published in academic journals including Journal of Management Information Systems, Journal of Information Technology, European Journal of Information Systems, Information Systems Journal, and Journal of Strategic Information Systems, and has also appeared in practice-oriented journals such as MISQ Executive and Cutter Business Technology Journal. Dr. Henningsson serves as senior editor on the editorial boards of Information Systems Journal and MISQ Executive.

Ben Eaton is an associate professor in the Department of Digitalization at Copenhagen Business School and adjunct associate professor at Høyskolen Kristiania, Oslo. Ben holds a PhD in Information Systems from the LSE. His research interests concern innovation on and within digital platforms and digital infrastructures. His work has been published in journals including MIS Quarterly, the Journal of Information Technology, Information Systems Journal, and The Journal of Strategic Information Systems.
