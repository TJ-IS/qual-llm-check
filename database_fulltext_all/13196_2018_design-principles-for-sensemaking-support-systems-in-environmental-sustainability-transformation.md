---
otero_id: 13196
otero_key: "F78XNDYP"
title: "Design principles for sensemaking support systems in environmental sustainability transformations"
authors: "Stefan Seidel; Leona Chandra Kruse; Nadine Székely; Michael Gau; Daniel Stieger"
year: "2018"
journal: "European Journal of Information Systems"
doi: "10.1057/s41303-017-0039-0"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
EMPIRICAL RESEARCH

# Design principles for sensemaking support systems in environmental sustainability transformations

Stefan Seidel<sup>1</sup>, Leona Chandra Kruse<sup>1</sup>, Nadine Sze´kely<sup>1</sup>, Michael Gau<sup>1</sup> and Daniel Stieger<sup>2</sup>

<sup>1</sup>University of Liechtenstein, Fuerst-Franz-Josef-Strasse 23, 9490 Vaduz, Liechtenstein; <sup>2</sup>University of Innsbruck, Innrain 52, 6020 Innsbruck, Austria

Correspondence: Stefan Seidel, University of Liechtenstein, Fuerst-Franz-Josef-Strasse 23, 9490 Vaduz, Liechtenstein. Tel: +423 265 1303; E-mail: stefan.seidel@uni.li

Accepted by DSR special issue editors Ken Peffers, Tuure Tuunanen and Bjo¨rn Niehaves Associate Editor: Prof. Kalle Lyytinen

## Abstract

This paper reports on the results of a design science research (DSR) study that develops design principles for information systems (IS) that support organisational sensemaking in environmental sustainability transformations. We identify initial design principles based on salient affordances required in organisational sensemaking and revise them through three rounds of developing, demonstrating and evaluating a prototypical implementation. Through our analysis, we learn how IS can support essential sensemaking practices in environmental sustainability transformations, including experiencing disruptive ambiguity through the provision of environmental data, noticing and bracketing, engaging in an open and inclusive communication and presuming potential alternative environmentally responsible actions. We make two key contributions: First, we provide a set of theory-inspired design principles for IS that support sensemaking in sustainability transformations, and revise them empirically using a DSR method. Second, we show how the concept of affordances can be used in DSR to investigate how IS can support organisational practices. While our findings are based on the investigation of the substantive context of environmental sustainability transformation, we suggest that they might be applicable in a broader set of contexts of organisational sensemaking and thus for a broader class of sensemaking support systems. European Journal of Information Systems (2017). doi:10.1057/s41303-017-0039-0

Keywords: sensemaking; sustainability; green IS; design science research

## Introduction

Information systems (IS) have become a key resource to assist organisations in their efforts of becoming environmentally more sustainable (Butler, 2011; Elliot, 2011; Melville, 2010). IS can support environmental sustainability transformations – a type of organisational change projects aiming at the reduction of resource consumption and environmentally harmful outputs – by enabling organisations to make sense of the situation and, in turn, implement more sustainable practices (Butler, 2011; Degirmenci & Recker, 2016; Seidel, Recker, & vom Brocke, 2013). Sustainable practices are recurrent activities that exert minimal negative impact on the environment, in terms of resource consumption and environmentally harmful outputs (compare Goodland, 1995; Seidel et al, 2013).

Sensemaking plays a crucial role in environmental sustainability transformations because such transformations are complex in that they relate to individual, organisational, governmental and societal factors (e.g., Elliot,

2011), involve information from various external and internal sources (e.g., Butler, 2011), rely on managerial interpretation, strategy and policy definition (e.g., Bansal & Roth, 2000) and are associated with both utilitarian and non-utilitarian values (e.g., Collins et al, 2007), as summarised in Seidel et al (2013). By making sense of the situation, individuals throughout the entire organisation ‘‘frame, interpret and understand the multilayered and complex issues related to the environmental sustainability transformation’’ (Seidel et al, 2013, p. 1281). This social process of organisational sensemaking, in turn, allows for the formation of collective action (Maitlis, 2005; Thomas et al, 1993; Weick et al, 2005).

In this paper, we respond to recent calls to investigate how IS should be designed that support the implementation of environmentally sustainable practices (Melville, 2010; Seidel et al, 2013; Watson et al, 2010) by identifying design principles for IS that support sensemaking in environmental sustainability transformations. Our research question is (please note that the research question has been reformulated in the course of the study while we remained faithful to its essence):

## What are appropriate design principles for IS for sensemaking (i.e., sensemaking support systems) in environmental sustainability transformations?

To address this question, we conducted a design science research (DSR) study to develop a set of design principles that concern a class of information systems, that is, the product of design (Iivari, 2010; Walls et al, 1992). We identified an initial set of design principles grounded in prior literature and revised these through multiple rounds of designing, demonstrating and evaluating a prototypical implementation. We use the concept of affordances (Leonardi, 2011; Markus & Silver, 2008) to describe the action possibilities required in sensemaking in environmental sustainability transformations, as well as the material properties of information technology (IT) that afford these possibilities. Our objectives are to (a) identify design principles, (b) evaluate and revise these design principles through the implementation, demonstration and evaluation of a purposeful IT artefact and (c) enhance our understanding of using the concept of affordances as an appropriate lens to study the design of IT artefacts that support organisational processes.

While our design science research study is in the substantive context of environmental sustainability transformation, and we thus develop design principles for a specific class of information systems (sensemaking support systems for environmental sustainability transformation); we hope that through our work we can also contribute to our understanding of how a broader class of sensemaking support systems might be designed. We define sensemaking support systems as information systems that support organisational sensemaking activities.

The next section provides the research background by focusing attention on organisational sensemaking (with particular focus on sensemaking in environmental sustainability transformations), information systems that support sensemaking, and the concept of affordances as a lens to study the design of information systems for supporting organisational practices. We then describe the design science research approach we used. This is followed by the initial set of design principles derived from prior theory and the description of three rounds of developing, demonstrating and evaluating a prototypical implementation, through which both the artefact and the underlying design principles were revised. We discuss our findings and provide a conclusion.

## Theoretical foundations

## Sensemaking in environmental sustainability transformations

Literally, sensemaking means ‘‘the making of sense’’ (Weick, 1995, p. 4) or ‘‘making something sensible’’ (Weick, 1995, p. 16). More specifically, sensemaking ‘‘starts with chaos’’ (Weick et al, 2005, p. 411) and is a circular process that involves noticing and bracketing of flux of experience, cognitive work to select a plausible story and retaining that story for further enactments (Weick et al, 2005). When humans make sense, they place stimuli into an available frame of reference and become able to ‘‘comprehend, understand, explain, attribute, extrapolate and predict’’ (Starbuck & Milliken, 1988, p. 51).

Sensemaking can be understood in both individual (e.g., Dervin, 1998, 1999) and organisational contexts (e.g., Churchman & Hanisch, 2005; Hasan & Gould, 2001; Maitlis & Christianson, 2014; Maitlis et al, 2013; Weick, 1995; Weick et al, 2005). Organisational sensemaking is a social process where actors interpret their environment through interactions and construct meaning that allows them to comprehend the world and to act collectively (Maitlis, 2005). Accordingly, sensemaking in environmental sustainability transformations is an organisational phenomenon involving individuals across the entire organisation (Seidel et al, 2013).

While initially seen as merely cognitive – people form shared mental cause maps – the focus of sensemaking has shifted towards a social-constructivist perspective, where people construct actionable intersubjectivity through language (Sandberg & Tsoukas, 2015). Corporate social responsibility activities, for instance, result from organisationally embedded cognitive and linguistic sensemaking processes (Basu & Palazzo, 2008). Sensemaking is about the materialisation of meaning and it relies on language and communication (Whiteman & Cooper, 2011) – ‘‘Situations, organisations and environments are talked into existence’’ (Weick et al, 2005, p. 409). Consistent with this view, sensemaking in environmental sustainability transformations involves engagement in communicative actions about the sustainability theme (Seidel et al, 2013).

Sensemaking and action are intricately related – sensemaking is transient in nature and determines human behaviour, sensemaking and organising (i.e., the process of becoming organised) are mutually constitutive, and sensemaking is about the interplay of action and interpretation in organisational practice (Weick et al, 2005). Sensemaking can be described in terms of a reciprocal interaction of seeking information, ascribing meaning and acting (Thomas et al, 1993, p. 240). Sensemaking is both retrospective and prospective (Bolander & Sandberg, 2013; Corley & Gioia, 2011; Gioia, 2006; Gioia & Chittipeddi, 1991; Gioia, Corley, & Fabbri, 2002; Thomas et al, 1993; Weick et al, 2005), consistent with the view that sensemaking provides the ground for the implementation of sustainable practices (Seidel et al, 2013). In environmental sustainability transformations, individuals ‘‘imagine and articulate meaningful alternatives to the current situation’’ (Seidel et al, 2013, p. 1281), which can lead to the alteration of work practices.

Against this background, we view sensemaking as process-oriented, organisational, social-constructivist and involving both retrospective and prospective elements. In environmental sustainability transformations, sensemaking is an organisation-wide process where individuals engage in interpretation and the construction of meaning related to organisational sustainability and where they imagine, articulate and evaluate alternative actions to provide the ground for the implementation of sustainable work practices. The process-oriented understanding of sensemaking allows us to identify key activities that occur in organisational sensemaking and that, in turn, provide the basis for developing information systems that support sensemaking:

1. Sensemaking is triggered by disruptive ambiguity (Weick et al, 2005), and different events exist that can act as triggers: major or minor planned or unplanned events, or hybrids of these (Sandberg & Tsoukas, 2015). A planned change initiative such as an environmental sustainability transformation, for instance, falls into the category of a major planned event (Sandberg & Tsoukas, 2015).

2. Sensemaking begins with acts of noticing and bracketing as those involved in the sensemaking process extract cues and create initial sense which can be further interpreted (Weick, 1979, 1995). Through noticing and bracketing, the world is simplified, the flux of circumstances begins to be ordered and the basis is provided for performing a narrative reduction and generating a plausible story (Weick et al, 2005). This plausible story, in turn, is retained and can guide further action and interpretation (Weick et al, 2005).

3. In this line of thinking, sensemaking requires labelling and categorising. Through labelling and categorising, the stream of experience gets stabilised, and those involved in the sensemaking process are allowed to find common ground (Weick et al, 2005).

4. Sensemaking involves presumption to guide action – sensemaking connects the abstract with the concrete, it ‘‘starts with immediate actions, local context and concrete cues’’ (Weick et al, 2005, p. 412). By adopting such view, we focus attention not only on the question ‘‘what’s the story here?’’, but also ‘‘what do I do next?’’ (Weick et al, 2005, p. 412). Once individuals in organisations are aware of the issues that they face in their current situation (e.g., organisational practices that are currently unsustainable, and should be changed to become more environmentally sustainable), they can start to anticipate trajectories and act effectively (Klein, Moon, & Hoffman, 2006a).

5. Organisational sensemaking involves communication: ‘‘We see communication as an ongoing process of making sense of the circumstances… The sensemaking, to the extent that it involves communication, takes place in interactive talk and draws on the resources of language in order to formulate and exchange through talk… symbolically encoded representations of these circumstances. As this occurs, a situation is talked into existence and the basis is laid for action to deal with it’’ (Taylor & Van Every, 2000, p. 58). Sensemaking is social and systemic – the locus of relevant knowledge is system-wide (Weick et al, 2005) and it is influenced by a variety of factors (Weick et al, 2005) such as context, cognitive frames, language, identity, politics, emotion or technology (Sandberg & Tsoukas, 2015).

To summarise, people experience disruptive ambiguity, turn circumstances into words through acts of noticing and bracketing, combine retrospective and prospective elements, use presumption to guide action and ultimately provide a launch pad for action (Weick et al, 2005). This understanding of salient sensemaking activities – with our explicit focus on making sense to prepare ground for action – gives a framework for our understanding of what sensemaking support systems should allow for – and hence says something about how they should be designed.

## The role of information systems in sensemaking

Sensemaking is influenced by technology – information technology in particular – (Sandberg & Tsoukas, 2015) and information systems can support sensemaking in organisations (Massey & Clapper, 1995; Weick & Meader, 1993; Zammuto et al, 2007). Information systems are formal socio-technical systems using information technology to store, process and disseminate information (Piccoli, 2012).

Task narrative forums, knowledge representation forums, interpretive reading forums, theory building forums and intelligent agent forums can support knowledge workers in making and taking perspective (Boland Jr & Tenkasi, 1995). Such forums are based on the language game model (Astley & Zammuto, 1992; Wittgenstein,

2010) and place emphasis on the importance of narrative. They apply the narrative mode of cognition (Bruner, 1990) that suggests that people do not only rationally process information, but also construct stories of their self and the world. While information from diverse sources plays a salient role in making sense of a situation (Weick & Meader, 1993), information overload can prevent people from actively making sense (Klein et al, 2006a) as they just passively process the given information without actively seeking relevant information in support of their assumptions (Hedberg & Jo¨nsson, 1982).

Further important aspects related to information systems and sensemaking in organisations include: designing semi-confusing IS to trigger sensemaking (Hedberg & Jo¨nsson, 1982), sensemaking of accounting data in organisational analysis (Boland, 1984), designing IS to support distributed cognition (Boland et al, 1994), computer-mediated communication technologies to help employees make sense of their work environment (Churchman & Hanisch, 2005), supporting sensemaking in crime investigation (Bex et al, 2007), sensemaking in intelligence analysis (Baber et al, 2016), using scenarios as a sensemaking device (Wright, 2005), using data-frame theory for sensemaking (Klein et al, 2006b), the application of Cultural-Historical Activity Theory concepts in supporting sensemaking activity of managers (Hasan & Gould, 2001) and requirements to support collaborative sensemaking such as supporting shared representation and consensus building and reaching agreement (Umapathy, 2010). In environmental sustainability transformations, information systems with monitoring, analysis and presentation features allow individuals to reconsider beliefs, actions, outcomes of work practices, and information access and interaction features allow individuals to actively participate in the sensemaking process, thereby providing the ground for the implementation of sustainable practices (Seidel et al, 2013).

To summarise, information systems can support organisational sensemaking in general and sensemaking related to sustainability transformation in particular. Prior literature gives important insight about the design of sensemaking support systems – communication platforms allowing for narratives provide a basis for cognition through narratives, semi-confusing or eye-opening information can help trigger sensemaking or information overload ought to be avoided to allow for an effective IS-supported sensemaking process. As this paper develops a set of theoretically and empirically grounded design principles, it contributes to the debate on how information systems can support sensemaking (e.g., Weick & Meader, 1993) and how such systems should be designed (e.g., Muhren et al, 2008; Parrish, 2008; Umapathy, 2010).

## Affordances as a lens to study the design of information systems for organisational practices

Understanding how to build information systems for sensemaking means understanding how to design for an IS-enabled organisational practice. Such organisationa practice involves human actors and is characterised by human agency and indeterminacy. Technology cannot deterministically lead to a sensemaking process to occur. Technology might, however, provide potential for action and pattern organisational practices in a non-deterministic way (Fayard & Weeks, 2014; Seidel & Berente, 2013). When developing information systems for organisational practice, we look to design for action potential – in our case, we are interested in providing an actionable space for individuals in an organisation to make sense. We turn to the concept of affordances that allows us to get at the relationships between information technologies and their context of use, and helps us understand what it means to design for practice (Fayard & Weeks, 2014; Markus & Silver, 2008).

Information technologies provide affordances for practices (Fayard & Weeks, 2014) – such as organisational sensemaking – and these affordances are realised through their enactment (Volkoff & Strong, 2013). The concept originates from the field of ecological psychology where it describes what actions the environment permits to animals (Gibson, 1977). IS scholars have tended to diverge from Gibson’s original formulation of the concept, where it is assumed that animals directly perceive what an object can be used for, and highlight that actors often interpret how to use information technology in light of their action goals (Leonardi, 2011; Markus & Silver, 2008; Seidel et al, 2013).

A tension has been highlighted between the relational (i.e., affordances are relationships between actors and technical objects) and dispositional (i.e., affordances are a property of the technical object) nature of affordances (Faraj & Azad, 2012; Fayard & Weeks, 2014; Jung & Lyytinen, 2014). The dispositional view of affordances in particular has been adopted in the field of human computer interaction (e.g., Hartson, 2003; Norman, 1988, 1999), where affordances are intentionally designed into a system. In the IS field, most scholars conceptualise affordances as relationships between information technology and users (e.g., Faraj & Azad, 2012; Jung & Lyytinen, 2014; Leonardi, 2011; Markus & Silver, 2008; Treem & Leonardi, 2012), but it is also maintained that such affordances (i.e., the relationships) are provided to groups of users by specific material properties of information technologies, which also highlights the dispositional nature of affordances. Affordances ‘‘channel’’ specific behaviour – although they are not deterministic in that they don’t deterministically lead to a certain (intended) practice (Fayard & Weeks, 2014, p. 243). Further, it is clear that many affordances are identified with regularity (Treem & Leonardi, 2012) and that thus the same or similar practices occur across the same organisation (Seidel et al, 2013) or across different organisations (e.g., Strong et al, 2014; Zammuto et al, 2007). Examples include business process management tools that afford the visualisation of work processes (Zammuto et al, 2007), features of knowledge sharing, acquisition, maintenance and retrieval that afford virtual collaboration (Zammuto et al, 2007) or structured data entry forms and common databases that afford capturing and archiving digital data about patients in healthcare (Strong et al, 2014). Still, this does not exclude that IT artefacts are often used in idiosyncratic ways, and that individuals identify and act upon different affordances in different contexts.

We adopt the view that affordances are both dispositional and relational, that affordances describe how technologies non-deterministically pattern organisational practices and that many affordances occur with regularity across time and context. Affordances are both real and external (affordances of a technology) while, at the same time, they are relative to the observer (individuals identify affordances in their social context). This is consistent with the perspective taken in affordance-based design (Maier, 2011; Maier & Fadel, 2009), where it is held that designers specify the properties that afford certain uses to certain users (Maier & Fadel, 2009). In this view, technologies may indeed be purposefully designed, stable and affording the same practices across contexts and time – as is essential in DSR studies as well as in design practice. This concept thus gives us a suitable lens to study the design of information systems artefacts:

1. When designing for practices, designers must consider the relationships between artefacts and humans instead of simply designing physical artefacts. The boundary conditions under which certain materia properties afford certain practices must be explicated.

2. Problems associated with a mere function-oriented approach can be avoided. Functions of a system are form-independent, describe what an artefact is intended to do, and denote the transformation of an input stage into an output stage by the artefact (Maier & Fadel, 2009). This view does not adequately capture the activities that are permitted through the artefact when it is used by humans. No information technology can have the function of ‘‘sensemaking,’’ but information technology can support sensemaking by providing appropriate affordances.

3. Design science research is a construction process (Iivari, 2007), and the concept of affordance allows for the construction and exploration of different designs. The same required practice might be afforded by different material properties of information technology, and any proposed design must be evaluated in terms of its utility(Winter, 2008) – that is, does the system indeed afford sensemaking? It cannot be claimed that any solution is the best solution possible in the sense of ‘true’ knowledge (Niehaves, 2007).

We can now formulate design principles in the following form consistent with the view that affordances can be deliberately designed while they are relationships between material properties of a system and specific user groups including boundary conditions (compare Chandra et al, 2015):

Provide the system with [material properties such as specific features] to afford users [activity of user/group of users], given that [boundary conditions].

That is, we seek to identify the abstract relationships between the practices that environmental sensemaking support systems should afford and the material properties that provide those affordances to certain user groups. Material properties are those aspects that are intrinsic to the technology in terms of matter and form and that are not part of the social context and endure across contexts and time (Leonardi, 2012). Examples include algorithms or graphical user interface elements such as text boxes or scrollbars. Materiality thus refers to those aspects that can be thought of to be available to all users in the same way (Leonardi, 2012) – but perhaps afford different user actions depending on context of use. In this paper, we use the notions features and material properties interchangeably – i.e., features are material properties (compare Markus & Silver, 2008 and Leonardi, 2012 for using a similar lexicon).

## Design science research approach

Our ultimate goal is to develop a set of empirically grounded design principles for systems that support sensemaking in environmental sustainability transformations, that is, an IT meta-artefact which constitutes a general solution as it describes a class of technologies and which can be instantiated into concrete IT artefacts (Iivari, 2010, 2015). Design principles capture the knowledge ‘‘…about creating other instances of artefacts that belong to the same class’’ (Sein et al, 2011, p. 3). They are statements that guide or constrain actions (Hevner & Chatterjee, 2010), are prescriptive in nature, constitute the basis for action (Baskerville & Pries-Heje, 2010) and are an appropriate way to communicate findings to both technology-oriented and management-oriented audiences, as is important in DSR (Hevner et al, 2004).

We used a staged research process informed by the work of Peffers et al. (2007) that allowed for multiple iterations of both the design principles and the development of an artefact (i.e., an information technology with certain material properties) to demonstrate and evaluate those design principles. We went through three iterations. Figure 1 visualises the research process.

Our study started with the identification and formulation of the problem and objectives (stage 1). The natural environment is under imminent pressure, and organisations are a main contributor to this problem (Melville, 2010). To address this issue, organisations must become more environmentally sustainable through reduced resource consumption, emissions and waste (Goodland, 1995). Sensemaking is a salient process in such transformation efforts (Butler, 2011; Seidel et al, 2013), constitutes a relevant business need (Hevner et al, 2004) and knowledge about the design of IS that support sensemaking is indispensable (Butler, 2011; Seidel et al,

![](/api/attachments/F78XNDYP/fulltext/images/7dedb1ae8cecf16413b4263b989493f7e7a2f66a89f2cb3e06e7df00240f4aed.jpg)  
Figure 1 High-level research process.

2013). The study therefore aims to develop design principles that describe a class of systems that are a means to the purpose of sensemaking and that can be applied in multiple settings (that share boundary conditions in terms of organisational sustainability transformation).

In our conceptual development phase, we identified initial design principles based on the salient affordances required in the sensemaking process as well as material properties to provide those affordances (stage 2). We aimed to atomise the problem conceptually so that our solution could capture its complexity (Peffers et al, 2007).

In the design and development stage (stage 4), the design principles were translated into a prototypical implementation (a web-based platform hosted at the case organisation) that built the foundation for subsequent rounds of demonstrating and evaluating the artefact. The artefact we built was thus theory-ingrained (Sein et al, 2011) and embedded the research contribution in its design (Peffers et al, 2007). To develop an implementation that met the latest technology standards, a software developer with experience with the state-of-the-art web technologies was part of the research team and team of authors.

Through our demonstration and evaluation (stage 5), we showed the feasibility of the proposed design, explored what material properties afford what action and further developed the design principles. In the first two rounds, we used two primary data sources, usage data (what people did on the platform in terms of discussions, etc.) and focus groups (subsequent to each cycle, two focus group discussions were organised with users of the platform). Quantitative information about the usage of the system is in Appendix B and details about the focus groups are in Appendix C. The analysis of usage data allowed us to see whether affordances were indeed enacted. From the focus groups, we could see whether participants interpreted the technology to afford the intended practices (Appendix C.2 describes the instrument we used to evaluate in how far certain material properties were interpreted by individuals to give raise to certain affordances). The focus groups also allowed us an in-depth inquiry about what material properties were seen as affording – or even constraining – sensemaking practices.

Through the analysis of data, we compared the objectives of the solution to actual observed results from using the system in practice (Peffers et al, 2007). Whenever we identified discrepancies between intended and actual outcomes in terms of affordance identification and enactment, we explored alternative or additional material properties that might create the required affordances. If necessary, the design principles were revised. We analysed both qualitative (what users wrote on the platform) and quantitative data (number of posts, number of votes, etc.) and conducted a process of top-down coding (Urquhart, 2013) where usage and focus group data were compared with the identified affordances and material properties. We used the set of affordances as a coding scheme for both the usage data and the focus group data. For each affordance, we went through the data we collected and looked for evidence that (a) the affordance was enacted and what material properties allowed for this enactment (this could be seen from usage data) and (b) certain material properties were interpreted to give rise to certain affordances (this could be seen from the focus groups). Focus group data and usage data were thus used to triangulate across methods of data collection. The first two authors were involved in analysing the data to corroborate the findings, and further sought agreement with the third author. In the case of disagreements, these disagreements were discussed and consent was sought, thereby ensuring inter-coder agreement. Throughout the process, we remained open to discover whether the material properties gave rise to any affordances that were not intended by the developers.

The research setting was a small-sized university with less than 1000 students. The organisation provided a suitable setting to demonstrate and evaluate our design: At the time of the study, the organisation had embarked on a sustainability transformation and had formulated a sustainability vision including items such as ‘‘the university is an exemplar of sustainable thinking and acting in the region and worldwide’’ and ‘‘material resources are used collectively.’’ Even though sustainability was a strategic goal of the organisation, there was no dedicated channel for everybody to discuss sustainability-related topics. Still, there were some isolated initiatives instilled by management (e.g., definition of a vision), research teams (e.g., research on sustainable architecture) and staff and students (e.g., initiatives on green mobility). Through preliminary workshops with representatives from all stakeholder groups, the needs for transparency and a dedicated communication channel became perceptible. We invited potential participants through e-mails, Facebook posts, posters, info sessions in the case organisation’s cafeteria and QR codes. To encourage participation, we announced that the most successful contributors would be awarded gift vouchers.

## Conceptual development: design principles for sensemaking support systems in environmental sustainability transformations

The process-oriented view of sensemaking gives us the requirements for the overall concept of a sensemaking support system in terms of the activities that the system should afford: triggering disruptive ambiguity and surprise, noticing and bracketing, open and inclusive communication and presumption and action planning. Prior theory thus provides kernel theory (Gregor & Jones, 2007; Walls et al, 1992) that can help explain why a design for environmental sensemaking support systems is expected to work (Gregor & Hevner, 2013). In the spirit of design science research as constructive research (Iivari, 2007), our design principles are the result of a construction process where we identify prospective material properties informed by previous literature on sensemaking in sustainability transformation (Seidel et al, 2013) and key capabilities of information systems to store, process and disseminate information (Piccoli, 2012). We further consider the boundary conditions in terms of organisational sustainability transformation and define the user groups as actors in an organisation that has embarked on an environmental sustainability transformation.

Sensemaking is triggered by disruptive ambiguity (i.e., surprise) – an understanding that roots back to the theory of cognitive dissonance (Festinger, 1957). When experiencing surprise, individuals think, ‘‘I knew I had to (blank), but I had no idea I would feel (blank) about it’’ (Louis, 1980, p. 238). Ambiguity, inconsistency, impermanency and multiple perspectives can counteract stability (Hedberg & Jo¨nsson, 1982). In environmental sustainability transformations, organisational actors experience dissonance when required to take part in promoting and performing sustainability-related actions, or when they are confronted with actual consumption and emission data about which they had no clear idea. Showing environmental indicators as well as indicators in relation to work practices can help individuals to reconsider beliefs, actions and outcomes of their work practices (Seidel et al, 2013), which is consistent with the idea that the provision of information can lead to ‘‘planned confusion’’ and destabilise organisations to better cope with variety in their environments (Hedberg & Jo¨nsson, 1978). To trigger disruptive ambiguity and surprise, a sensemaking platform should use dissemination features of IT to provide eye-opening information related to facts, observations or general behaviour related to the sustainability topic (Seidel et al, 2013). Correspondingly:

Design Principle (DP) 1: Provide novel information in the form of environmental facts, observations or general behaviour, so that the system affords users to experience disruptive ambiguity and surprise in sustainability transformations.

In the early stages of the sensemaking process, actors crudely extract cues and create a raw map to explain the problem. Events that have already occurred are given a name, and the streaming of experience is stabilised through categorisation and labelling (Weick et al, 2005). Sensemaking can be viewed as an act of invention and thus produces artefacts including language games and text (Weick, 1995). Besides, it may emerge as ‘‘plausible images’’ (Weick et al, 2005), that is, in the form of either verbal or graphic representation. IS for sensemaking must therefore provide features for storing and categorising relevant cues, because such features are expected to afford noticing and bracketing, and thus explanation of the problem and the creation of meaning. Correspondingly:

DP 2: Provide features to store and categorise ideas, so that the system affords noticing and bracketing to users in environmental sustainability transformations

Environmental sustainability transformations require the involvement of individuals across all functional areas and levels of the organisation (Seidel et al, 2013) and sensemaking in environmental sustainability transformation is thus collaborative. Sensemaking combines individual and social grounds and some authors regard communication an essential component of sensemaking (e.g., van der Heijden et al, 2012; Weick et al, 2005). Through social interaction, individuals gain different insights and viewpoints that otherwise may not have been accessible. The sharing of understanding is similar to articulation, where tacit, past-oriented and private cues are transformed to become explicit, public and situation-relevant (Taylor & Van Every, 2000). As we see sensemaking as both retrospective and prospective (i.e., as transient), cues can be both past oriented (in the sense of reflection) and future oriented (in the sense of presumptions). To afford an open and inclusive communication, sensemaking support systems should provide features to allow actors to engage in an interactive discussion with other members:

DP 3a: Provide features for interactive communication, so that the system affords users to engage in an open and inclusive discussion in environmental sustainability transformations

Moreover, for this communication to be afforded on a social ground, actors need to be aware of other actors that may or may not participate in the communication:

DP 3b: Provide users with an overview of all other users along with features for direct communication between users, so that the system affords users to engage in an open and inclusive discussion in environmental sustainability transformations

Answering the important question of ‘‘what should I do next?’’ requires actors to make presumptions about the potential actions and their outcomes. At this stage in the sensemaking process, the sense is nearly made and articulated. Sensemaking support systems can play a role in enhancing the plausibility and guide action by informing users about the possibilities of outcomes resulting from a set of various actions; different hunches need to be tested in order to filter out what actions are most plausible (Weick et al, 2005). The notion of presumption highlights the prospective (i.e., future) orientation of sensemaking (Gephart, Topal, & Zhang, 2012) to differentiate it from mere reflection. Presumption is a process where individuals prospectively review various action-outcome alternatives before allowing an alternative to guide their action. At this, plausibility is more relevant than accuracy, as a presumption does not necessarily possess absolute truth. Individuals build their future projection on reflectively constructed schemes, that is, through ‘‘selective reconstruction and creative elaboration of prior entities or through the invention of new ones’’ (Gephart et al, 2012, p. 296). To afford effective and sensible action planning, it is necessary to provide features that allow for the categorisation of action possibilities into (a) mere presumption or (b) feasible, executable, sensible action. Correspondingly:

DP 4: Provide features for categorisation of action alternatives to distinguish presumptions from actual planned actions, so that the system affords users presumption and action planning in environmental sustainability transformations

Please note that originally we used the term ‘‘presumptive disclosure’’; in a later stage, we revised the terminology to increase simplicity and understandability. Next, we describe how our research evolved through two cycles of building, intervention and evaluation as well as subsequent formalisation in terms of revising the design principles.

Table 1 provides an overview of the initial design principles.

## First round of development, demonstration and evaluation

## Design and development

Table 2 provides an overview of how the initial design principles were implemented.

The system’s start screen provided an overview of available topics (Figure 2), intended to provide an entry point for an organisational sensemaking process. We posted four initial topics that users could easily relate to their own behaviour: (1) disposable plastic cups, (2) paper towels, (3) printouts and (4) waste, including data and explanations. Since the platform was intended to stimulate users to identify problems and engage in a sensemaking process, no specific problems associated with these topics were posted.

In order to allow users to experience disruptive ambiguity and surprise (DP 1), for each topic, the platform provided basic information about environmental concerns and relevant indicators. These indicators concerned the source capabilities (Goodland, 1995) of the organisation (e.g., the consumption of paper) as well as the sink capabilities (Goodland, 1995) (e.g., the waste generated). Figure 3 displays data about the paper consumption at three different departments from December 2011 to May 2013 as shown on the platform, which can be considered eye-opening information that might lead to ‘‘planned confusion’’ (Hedberg & Jo¨nsson, 1978).

In order to afford noticing and bracketing (DP 2), the platform allowed users to create their own topics (‘‘create topics’’) and to comment on topics (‘‘comment’’),

Table 1 Overview of initial design principles

<table><tr><td>#</td><td>Design principle specification</td><td>Affordance</td><td>Material properties</td></tr><tr><td>DP1</td><td>Provide novel information in the form of environmental facts, observations or general behaviour, so that the system affords users to experience disruptive ambiguity and surprise in environmental sustainability transformations</td><td>Triggering disruptive ambiguity and surprise (Sandberg &amp; Tsoukas, 2015; Weick et al, 2005)</td><td>Features to provide environmental information along with novel information</td></tr><tr><td>DP2</td><td>Provide features to store and categorise ideas, so that the system affords noticing and bracketing to users in environmental sustainability transformations</td><td>Noticing and bracketing Labelling and categorising (Weick, 1979, 1995; Weick et al, 2005)</td><td>Features to store and categorise ideas</td></tr><tr><td>DP3</td><td>a. Provide features for interactive communication, so that the system affords users to engage in an open and inclusive discussion in environmental sustainability transformationsb. Provide users with an overview of all other users along with features for direct communication between users, so that the system affords users to engage in an open and inclusive discussion in environmental sustainability transformations</td><td>Open and inclusive communication (Sandberg &amp; Tsoukas, 2015; Taylor &amp; Van Every, 2000; Weick et al, 2005)</td><td>Features for interactive communication among all users Features for direct communication between users</td></tr><tr><td>DP4</td><td>Provide features for categorisation of action alternatives to distinguish presumptions from actual planned actions, so that the system affords users presumption and action planning in environmental sustainability transformations</td><td>Presumptive disclosure and action planning (Klein et al, 2006a; Weick et al, 2005)</td><td>Features for categorisation of action alternatives</td></tr></table>

Table 2 Overview of initial instantiations

<table><tr><td>#</td><td>Instantiation of Material Properties</td></tr><tr><td>DP1</td><td>Presentation of environmental indicators through a read-only web platform</td></tr><tr><td>DP2</td><td>Posting comments to notice and to bracket ideasDrop-down menu with three different labels for each specific comment: problem-centric, solution-centric and plainCheck box with the options “important,” “problem,” “solution,” “doable now” and “doable later” to allow all users to qualify a comment</td></tr><tr><td>DP3a and D3b</td><td>Direct messaging implemented through a text box and send button on the web platformText box to enter and post replies to commentsCommunity view, where all members are displayed with user names and optional photosExplore topics view, where topics are displayed either chronologically or by number of views; tabulators to choose between the two options</td></tr><tr><td>DP4</td><td>Drop-down menu with two different labels for each specific solution entry: doable now and doable later“Doable Now” view, where all entries are displayed that have been rated “doable now” by the majority of voters“Action plan view,” where those actions displayed under the “doable now” view are displayed in a separate window accessible from the website’s main page</td></tr></table>

![](/api/attachments/F78XNDYP/fulltext/images/dd2e1c5822f4a3985a1630ed48ea1d3b2d7235c6ee8c20abb9c452768c57313e.jpg)  
Figure 2 ‘‘Explore topics’’ view: the entry point for IS-supported organisational sensemaking.

thereby entering and labelling their ideas, extracting cues and providing meaning to these cues. Users could label entries as problem-centric, solution-centric or plain, providing further specificity to their ideas (Figure 4).

All users could rate (1) whether the idea is important, (2) whether the idea is problem-centric or (3) whether the idea is solution-centric. It could thus happen that a comment that was labelled as solution-centric by its originator was viewed as rather problem-centric by other users. The ongoing rating results were presented on the right side of the comment. Figure 5 displays a specific comment where the majority of users has identified the comment as a solution that is ‘‘doable now.’’

In order to allow for an open and inclusive communication (DP 3a), each topic had the form of an ongoing web-based discussion, where users could reply to comments. Figure 6 shows an example of how the discussion evolved (the different colours differentiate problem-centric, solution-centric and plain comments).

To allow for presumption and action planning, users could rate solution-centric comments (a) as ‘‘doable now’’ or ‘‘doable later’’ and (b) according to their importance. Comments that were rated as ‘‘doable now’’ by a majority of users were listed under the ‘‘action plan’’ view. This way, mere presumptions that were not (yet)

![](/api/attachments/F78XNDYP/fulltext/images/e34f1cb16599fe795337e2bf155aefdf627261f02d9fc79bb8bda1d0b5c58723.jpg)  
Figure 3 Example data presented to trigger disruptive ambiguity and surprise.

![](/api/attachments/F78XNDYP/fulltext/images/d6bd8a7364040e029a73ad76146d0a1c7554fd5fa009fb797b37c6450354f8fa.jpg)  
Figure 4 ‘‘Add new comment’’ feature: affording noticing and bracketing.

executable were distinguished from actual, implementable actions. Figure 7 shows an extract from the action plan generated in the first cycle.

## Demonstration and evaluation

In the first round, 65 users subscribed to the system out of which 51 participated actively (either through topic views, commenting or rating). During the two weeks of using the system (from 18 November 2013 to 02 December 2013) minor technical issues were identified and solved as they occurred. Subsequent to using the system, two focus group discussions were conducted, one with five participants and one with four participants, all of whom had subscribed as users to the platform.

We found evidence in the usage as well as focus group data that the platform afforded users to experience disruptive ambiguity and surprise through the provision of environmental data and facts. The four initial topics for which we provided environmental data (disposable plastic cups, paper towels, printouts and waste) all stimulated a discussion. Those additional topics that were posted by users without the provision of environmental data and facts, however, did not trigger the same level of interest. The responses given during focus group discussions also provided further confirmation as, for instance, several respondents said that ‘‘seeing data’’ was an important feature of the platform:

I wanted to write my own topic, but then when I saw the data, ‘‘whoop,’’ I was surprised how much we really consume.

It was also pointed out that the system should provide more environmental facts (e.g., comparative data from other institutions) as well as an overview of alternative potential actions.

Both usage and focus group data also suggest that the platform afforded noticing and bracketing. In the following comment, a user offers an idea about raising awareness and it becomes noticeable how the user applied mental models to support noticing and bracketing:

I see a lot of teachers entering the classroom with plastic cups. They could be role models by showing their ‘‘bottled’’ commitment! Before starting class they could raise their Eco-Tanka-[Bottle] (or any other ecological bottle) to the students and take a passionate sip!

Here, organisational circumstances are explicated and expressed by words and salient categories. Participants also used the voting mechanism to distinguish problems from solutions and voted for the importance of a post (a total of 381 votes were made). For instance, for the quote on teachers acting as role models, none of the participants categorised the entry as a problem, but five participants categorised it as a potential solution. The existence of this affordance was further confirmed in the focus group discussion: While noticing and bracketing were seen to be afforded, we also became aware of a need to improve the labelling features; for instance, it was suggested to add icons visualising alternative choices such as ‘‘like’’ and ‘‘dislike,’’ or ‘‘agree’’ and ‘‘disagree.’’ Besides, the distinction between ‘‘doable now’’ and ‘‘doable later’’ was not clear – the suggestion of replacing water dispensers with drinking fountains, for example, was identified as ‘‘doable now’’ even though it involved an infrastructural change, whereas the suggestion of only removing the plastic cup dispenser and provide reusable bottles was identified as ‘‘doable later’’ even though it involved a rather simple behavioural change. We also found instances where comments were not labelled ‘‘solutions’’ but were still labelled as ‘‘doable now’’ or ‘‘doable later.’’

![](/api/attachments/F78XNDYP/fulltext/images/85ea018ec10a42d4e8c18e5551b19838ac49a84d8051cfd95678c8b5be47defc.jpg)  
Figure 5 Voting mechanism: affording noticing and bracketing.

We found evidence in both usage and focus group data that users did engage in an open and inclusive communication and hence moved the sensemaking process to a social ground. 21 users posted 53 comments, most of which were interrelated. For instance:

Comment: Always provide an alternative to help people change their behaviour! So how to spread our uniGo bottles over the campus? View Eco-Tanka-[Bottle] in our [link to online shop] - only 10 CHF!! Maybe by a concise info sign at the water dispenser - with striking figure, e.g. comparison ‘‘how many plastic cups in a year compared with one sustainable bottle’’…

Response: Good idea! But I wonder how we can maintain the use of sustainable bottle. Last year I still saw some people carrying their bottles to and from the dispenser, but this year I see much less of them.

Still, we also noticed that there was room for improvement. In the focus group discussions, some participants mentioned that it was difficult to relate comments to other comments which notably constrained the discussion. This could also be seen in the usage data which indicated that comments were meant to be related to other specific comments, but the system did not provide an appropriate feature. For instance, participants used the ‘‘@’’ symbol in conjunction with a participant’s name in order to address that specific participant. Participants also expressed their wish to be able to edit comments once they were posted, that there should be some information about user activity on the platform (i.e., about who said what) and that a moderator role would be beneficial for the discussions.

Finally, both the analysis of usage and focus group data suggested that the system afforded presumption and action planning. First, actors posted potential actions and the community voted on these actions (e.g., as ‘‘doable now’’), resulting in an action plan with immediately implementable actions. Altogether 20 actions were proposed within the two weeks. There was also evidence that users used the system to distinguish between mere presumptions and advisable actions, thereby ‘‘testing’’ proposed actions (Weick et al, 2005):

Proposed solution: Usually what really hurts people is money - sad but true, e.g. plastic bags in shops…So if we made them pay for the cups, they might at least reuse them during one day […] Response: Making people pay is not a solution. Maybe yes for a couple of days but after that what? Afterwards it will become another habit like everything else. The real problem is how to make them understand what the real problem is. And more important make them learn for life. How about bring in the reusable plastic bottles idea? […]

The existence of this affordance was confirmed in the focus groups. However, participants also criticised the lack of a feedback mechanism and demanded that decision makers should provide feedback about the implementation and effects of proposed solutions. Moreover, it was expressed that the action plan lacked clarity.

To summarise, our analysis suggests that the system indeed afforded an ongoing sensemaking process. At the same time, we could also identify areas of improvement with regards to the material properties that were implemented to afford the required practices.

## Formalisation: Revision of Design Principles

We added a design principle demanding that systems for sensemaking should provide material properties to relate comments to other comments:

![](/api/attachments/F78XNDYP/fulltext/images/c3e70919e05c3b27a8946c58fb1c9e9d34e7bfe25f9383ac34fb20b913da9f9d.jpg)  
Figure 6 Posting comments: affording and open and inclusive communication.

DP 3c: Provide features to relate comments to other comments, so that the system affords users to comprehend circumstances and turning them into words and categories on a social ground in environmental sustainability transformations

We found that moderating the process could prevent discussions from moving in a ‘‘wrong direction’’ and that decision makers at the organisation should play an active role in responding to potentia actions. We proposed to distinguish different roles, such as administrator, moderator, user and decision maker:

DP 3d: Provide features to assign roles to users so that the system affords user-specific actions, such as moderation of discussions in environmental sustainability transformations

## Second round of development, demonstration and evaluation

## Design and development

The system was revised based on the findings from the first round of development, demonstration and evaluation. We removed the ‘‘add topics’’ feature for ordinary users (i.e., only moderators could add topics) in order to provide relevant information and indicators that afford users to experience disruptive ambiguity and surprise consistently for each topic. We further improved data presentation as respondents had demanded more detailed data and more background information about potential actions in terms of advantages and disadvantages.

![](/api/attachments/F78XNDYP/fulltext/images/fe86c4fe7715bd6d9f2be30c6cb7ca85aa66ae641f52e1c38f72061cf177fd04.jpg)  
Figure 7 Excerpt from action plan for ‘‘disposable plastic cups’’.

![](/api/attachments/F78XNDYP/fulltext/images/34269ef8a0ec68f4873d2ec1316cbfabc3a0ced8403f9bf674ab4d1b30fbe10b.jpg)  
Figure 8 Revised voting mechanism.

With regards to noticing and bracketing, we changed the categories as displayed in Figure 8. As the results from the first cycle suggested that the previous labels (‘‘doable now’’ and ‘‘doable later’’) allowed for ambiguity, we decided that solutions could instead be specified in terms of ‘‘infrastructural change’’ and ‘‘behavioural change.’’ Moreover, this further specification was only possible if a comment was labelled ‘‘feasible solution’’ in the first place. We also aimed to simplify the design and introduced icons.

In order to better afford an open and inclusive communication, we implemented the new design principles 3c (relating comments to other comments)

and 3d (roles). For DP 3c, we added a feature that allowed referencing comments (Figure 9). For DP 3d, we introduced a role system distinguishing between moderators, decision makers and regular users, with specific badges for each of them. Besides, we displayed how many posts a certain user had produced.

Finally, to better afford presumption and action planning, we implemented labels that clearly identified those users who were also decision makers in the organisation as the aim was to actively involve them into the process of sensemaking. The new voting mechanism allowed for an easy distinction between what were feasible actions, and whether they related to behavioural or infrastructural change. We deemed ‘‘feasible’’ to be clearer than ‘‘doable now’’ to distinguish suggestions from actual plans, an essential characteristic of presumption and action planning. The action plan was changed in that it now also distinguished between behavioural and infrastructural change in accordance with the new voting feature.

![](/api/attachments/F78XNDYP/fulltext/images/2045374274d67bffb5a5f3295aa889465e2ad24117f7c88fb671312eb55f7983.jpg)  
Figure 9 Revised ‘‘add new comment’’ feature.

## Demonstration and evaluation

In the second round, 99 users were subscribed to the system (including users of the first cycle). Forty-two users signed in at least once during the demonstration and evaluation period and participated actively (either through topic views, commenting or rating), out of which 16 users had already participated actively in the first round. The overall participation in this stage was lower, possibly because (a) the system wasn’t new to many users who had already participated in the first stage, and (b) the cycle fell into the time just before the exams at the university site we studied. Still, we collected rich data to further evaluate the design and underlying principles. Subsequent to twelve days of using the system (from 01 December 2014 to 12 December 2014), two focus group discussions were conducted, both with four participants, all of whom had subscribed as users to the platform. Three focus groups participants had also participated in one of the two focus groups of the previous cycle.

We found evidence in both usage and focus group data that all four main affordances were created and enacted. The provision of data initiated discussions through disruptive ambiguity and surprise, and we could see that those discussions indeed built upon the available data. For instance, a user stated:

For an institution like the university this is nothing, and doesn’t motivate for further savings. Therefore, to reduce the energy consumption other KPI’s are required. For example in […] the government is promoting a challenging goal: until 2050 the average energy consumption per person in this region should be 2000 W (More: [link to website]).

The importance of providing environmental data was further highlighted in the focus groups, for instance:

…I think that [providing data] was probably helpful to also trigger the comments, because you will relate to some topics of cause more and to some less, but then, at least you have the same bases to enter the discussion….

The analysis further suggests that the revised version supported noticing and bracketing. Altogether, 28 comments and 285 votes were made in this cycle. Consider the following proposed solution and associated voting:

To promote use of the public transportation system for commuting to university/work as well as for leisure activities, I suggest to organise that students of the [case organisation] are eligible for the discount on the student rail pass (GA) […] (incl. buses …): [link to website].

(Votes: Relevant Problem = 4; Feasible Solution = 13; Important = 10; Behavioural Change = 3; Infrastructural Change = 3).

Here, the proposed solution is (a) identified by the community as feasible and (b) relates to infrastructural (cheaper tickets) and behavioural change (using the bus), thereby providing evidence for the enactment of the noticing and bracketing affordance. However, there were also many comments that suggested otherwise. In the focus groups, for instance, a participant made a remark on the complexity of the voting mechanism and terminologies used:

There were some of those thumbs, you can click on, I think five different ones, I was kind of overwhelmed by that, I didn’t get the point at the beginning, because some of those thumbs are really similar, for example, this is important or relevant problem or feasible solution, it’s hard or it’s difficult to distinguish between those. Maybe it’s too much, maybe two or three thumbs in total would be fine.

Moreover, some participants used the system to provide relatively long entries, thereby discussing different ideas in one comment – a use of the system that is unfaithful to the idea of noticing and bracketing and that was confirmed in the focus groups, for instance:

…if there are for example three different ideas then it’s a bit tricky how to response to that and to evaluate. Maybe you like one idea, but the other, for you it’s not feasible, for example, and then how vou evaluate that

We found more evidence that the platform afforded an open and inclusive communication. Altogether, 17 users contributed the number of 28 comments in this cycle. However, a particular design decision may have constrained an open and inclusive communication: While in the previous version of the system every user could add topics, in the second version all topics were entered by moderators. The reason was that in the previous version topics were posted that did not provide data and did not trigger a sensemaking process.

![](/api/attachments/F78XNDYP/fulltext/images/1ab1e2f6b886cbafe1101882df40142f5e115688550d03f028bf7622eedcfeef.jpg)  
Figure 10 Revised ‘‘add new comment’’ feature.

![](/api/attachments/F78XNDYP/fulltext/images/1b3b8e6047b5585ab808bb1dfadf2c9a6625ec02e2efae6de15f1de068ddf278.jpg)  
Figure 11 Revised voting mechanism.

As for the new design principle 3c (linking comments), it turned out that few users had used the feature. Instead, they again employed alternative means such as adding the ‘‘@’’ symbol to their comments. The focus groups suggested that users simply were not aware of this feature:

Yeah, I don’t know how it was implemented right now but if you have a topic and then there are five comments on this topic, like in a straight line, like time line and I wanna respond on the second comment, was it possible to respond on that?

This suggests that the system was not seen as affording to link comments to other comments by many users.

Finally, with regards to presumption and action planning, it was pointed out that the system was lacking a feedback mechanism. Specifically, users were interested in the state of proposed actions, whether they are considered, implemented or will not be implemented. Still, a total of 20 action items was created through the sensemaking process.

## Formalisation: revision of design principles

From the evaluation of the first and second versions, it was clear that simplicity is important with regards to the features provided for noticing and bracketing. Correspondingly:

DP 2: Provide features of storing and simple and unambiguous categorisation of ideas, so that the system affords noticing and bracketing to users in environmental sustainability transformations

For presumption and action planning, our data clearly indicated that the class of systems might benefit from a dedicated feedback mechanism about the actual state of planned actions. Correspondingly:

DP 4b: Provide features for providing dedicated feedback about the implementation and consequences of the implementation of actions

## Third round of development, demonstration and evaluation

A final version of the system was implemented. In order to afford engagement in an open and inclusive communication, we re-introduced the ‘‘add topic’’ feature; however, topics now had to be reviewed by a moderator before they could be seen by other users. This way, it could be ensured that only topics that provide an informational basis were displayed.

Several changes were made to better afford noticing and bracketing. First, we altered the post comment feature in order to further help users label ideas and relate their comments to other users’ comments. It was now only the user posting a comment who must decide whether the comment is a ‘‘problem,’’ ‘‘solution’’ or ‘‘other’’ (Figure 10). The design decision was made to avoid ambiguity by ensuring that every comment is clearly labelled as either problem, solution or other (e.g., for additional information or links), thereby avoiding comments that present multiple ideas (in accordance with the revised DP 2 with its focus on simplicity and unambiguity).

Second, in this line of thinking, the voting mechanism was simplified. Users could simply vote whether a solabelled problem was ‘‘important’’ or/and ‘‘relevant to the organisation,’’ and whether a so-labelled ‘‘solution’’ was ‘‘important’’ or/and ‘‘feasible in the organisation’ (Figure 11).

Figure 12 illustrates all three types of entries (plain, problem and solution).

Finally, moderators and decision makers could assign certain states to a proposed action in the action plan (Figure 13).

![](/api/attachments/F78XNDYP/fulltext/images/db1da54b7269647557b21e6e9ed1cda3df09cdcac87aef92d4566597b841ef66.jpg)  
Figure 12 Revised topic view (example data taken from second cycle).

![](/api/attachments/F78XNDYP/fulltext/images/103ff6e8907f02b093adf0868e922db9f7177d10a0b637e835dc170c66216434.jpg)  
Figure 13 Revised action plan view (example data taken from second cycle).

To evaluate the final version, we conducted another focus group with four subjects. Two subjects had participated in both prior focus groups, one subject had participated in one of the focus group of the second cycle and one subject participated the first time in a focus group. Three focus group participants were subscribed to the platform. We found that they (1) understood the new material properties, (2) were satisfied with the changes and (3) found the final version more useful than the previous version.

## Final, revised design principles

Our final set of design principles is the result from our conceptual, theory-inspired development as well as three rounds of building and evaluating a prototypical implementation to revise the design principles. Table 3 provides an overview of the final set of design principles for information systems that support sensemaking in environmental sustainability transformation.

Table 3 Overview of final, revised design principles

<table><tr><td>#</td><td>Design principle specification</td></tr><tr><td>DP1</td><td>Provide novel information in the form of environmental facts, observations or general behaviour, so that the system affords users disruptive ambiguity and surprise in environmental sustainability transformations</td></tr><tr><td>DP2</td><td>Provide functions of storing and simple and unambiguous categorisation of ideas, so that the system affords noticing and bracketing to users in environmental sustainability transformations</td></tr><tr><td>DP3</td><td>a. Provide features for interactive communication, so that the system affords users to engage in an open and inclusive discussion in environmental sustainability transformationsb. Provide users with an overview of all other users along with features for direct communication between users, so that the system affords users to engage in an open and inclusive discussion in environmental sustainability transformationsc. Provide features to relate comments to other comments, so that the system affords users to comprehend circumstances and turning them into words and categories on a social ground in environmental sustainability transformationsd. Provide features to assign roles to users so that the system affords user-specific actions, such as moderation of discussions in environmental sustainability transformations</td></tr><tr><td>DP4</td><td>a. Provide features for categorisation of action possibilities to distinguish presumptions from actual planed actions, so that the system affords users presumption and action planning in environmental sustainability transformationsb. Provide features for dedicated feedback about the implementation and consequences of the implementation of actions in environmental sustainability transformations</td></tr></table>

## Discussion and implications

In this section, we discuss our contribution and highlight implications in light of (1) the literature on green IS, (2) the literature on sensemaking, (3) related types of systems and (4) the use of affordances as a lens for design science research.

## Relating the findings to the literature on green information systems

Our study contributes to recent literature on green information systems, where sensemaking has been identified as a key organisational activity in sustainability transformations (Butler, 2011; Seidel et al, 2013). Sensemaking is required to interpret and make sense of complex, comprehensive and equivocal information from the institutional environment and precedes other activities such as decision making and knowledge creation and, ultimately, the implementation of sustainable processes or development of green products (Butler, 2011). Reflective disclosure and information democratisation have been identified as salient sensemaking affordances in environmental sustainability transformations (Seidel et al, 2013). The first ‘‘enable seeing information about current work practice beliefs, actions, and outcomes, and enable imagination, articulation, and assessment of alternative actions and outcomes’’ (Seidel et al, 2013, p. 1282) and the latter ‘‘enable dissemination and interaction about sustainability-related information from both internal and external sources’’ across the organisation (Seidel et al, 2013, p. 1282). While these elements can also be found in our conceptualisation (experiencing disruptive ambiguity and surprise, noticing and bracketing and presumption and action planning relate to reflective disclosure; open and inclusive communication relates to information democratisation), we provide (a) a more detailed, process-oriented view of the salient affordances required to allow for organisational sensemaking and (b) explicit prescriptive guidance about how such systems should be designed. Such detail is necessary to learn something about the material properties of information systems that provide required sensemaking affordances, and to develop actionable design principles.

Relating the findings to the literature on sensemaking We defined sensemaking as process-oriented, organisational, social-constructivist and involving both retrospective and prospective elements, and this understanding provides a basis to discuss our findings.

With regards to the process view of sensemaking, our study shows how information systems can provide certain material properties that allow for the occurrence of interrelated, socio-material sensemaking practices. Affordances of experiencing disruptive ambiguity and surprise, noticing and bracketing, inclusive communication, and presumptive disclosure and action planning non-deterministically pattern organisational sensemaking practices. Such socio-material practice is characterised by the interplay of human and material agencies (Leonardi, 2011; Orlikowski, 2007), and we can see important differences to the mere (not technologyenabled) social practice of organisational sensemaking; for instance, socio-material sensemaking allows for the participation of actors that are geographically distributed, of actors that are part of stakeholder groups that typically do not communicate face-to-face and that may contribute to organisational sensemaking asynchronically at different times.

With regards to the organisational nature of sensemaking, our study shows that for successful sensemaking it is necessary to consider the different roles that participants play in the organisation. For instance, some actions or changes can only be undertaken once they are approved by decision makers (e.g., the installation of new drinking fountains). Consequently, the distinction between topdown and bottom-up approaches in sustainability transformation becomes blurry, and our study highlights how

IS for sensemaking might contribute to top management support in bottom-up initiatives and the institutionalisation of change into day-to-day practices (Kotter, 2012). These findings also highlight the importance of the distinction between first-order and second-order sensemaking as proposed by Sandberg and Tsoukas (2015):

First-order sensemaking deals with agents embedded in unfolding, primary empirical contexts of action, in which they need to undertake effective action to restore order, whereas second-order sensemaking deals with how policy makers or inquiry teams make sense of primary sensemakers (p. 823).

Our focus on the prospective (Gioia, 2006; Weick et al, 2005) and linguistic (Brown et al, 2014) aspects of sensemaking is consistent with the framework of communicative action (Habermas, 1984), which views social action as being directed towards reaching either success or understanding. Organisational sensemaking occurring through discourse aims at understanding, where participants communicate to reach harmony between their plans of action and those of others. Once harmony is achieved, it serves as a launch pad for action.

## Relating the findings to related types of systems

The class of systems described through our design principles reveals similarities and difference to other classes of systems and approaches, such as group support systems (GSS), decision support systems (Arnott & Pervan, 2005, 2014) or open innovation contests (Bullinger et al, 2010; Piller & Walcher, 2006). However, the underlying theories differ and so do the expected outcomes. While GSS and DSS usually aim at ‘‘supporting and improving managerial decision making’’ (Arnott & Pervan, 2014, p. 269), the class of systems described in this paper aims at both identifying and defining relevant problems and providing feasible solutions that may or may not be implemented by the decision makers. The decision is made later, and not in the process of ascribing meaning to the situation. Nevertheless, literature on organising in crisis situation admits that sensemaking and decision making are indeed intertwined (Brown, 2004; Brown et al, 2014; Weick, 1988). Open innovation contests address individuals’ skills, experiences and creativity to hand in ideas and comment on others’ ideas, while sensemaking explicitly combines retrospective and prospective approaches, and is based on acts of noticing and bracketing and further labelling and categorising.

## Relating the findings to the literature on design science research methods

We used the concept of affordances because it is a suitable concept to say something about designing information systems for organisational practices. We viewed affordances as both dispositional and relational, because this allows us to take a middle ground for design science research, between the narrow determinism of emphasising technology features and the voluntarism of purely constructivist views (Leonardi & Barley, 2008; Seidel & Berente, 2013). Instead of suggesting that information systems might have a sensemaking function, we have argued that material properties of information systems can provide an actionable space that patterns organisational practice (Fayard & Weeks, 2014) and allows for sensemaking to occur.

The proposed design principles are consistent with this view. All design principles put forward in this paper suggest material properties that are expected to bring about certain affordances. At the same time, all of them state that the intended action potential is in relation to a group of users. Understanding and expressing boundary conditions is important to build a cumulative body of design knowledge in the information systems field, to show the limits of generalisability, and to prepare the ground for extending those boundary conditions through repeated application of the proposed principles across contexts and across time.

We also show that the concept of affordances is consistent with the nature of design science research as a constructive process (Iivari, 2007) and thus leaves room for creativity in the design process. While the required affordances remained stable throughout the study, we learned something about the material properties that might satisfy those affordances – and this has been captured through an evolving set of design principles.

## Limitations

This study has some limitations. First, there might be alternative affordances to be identified, that is, the process of sensemaking might be conceptualised differently. Second, we cannot claim that the material properties we propose are the best to create the desired affordances as our focus was on prescriptive knowledge in terms of design product knowledge, which does not have truth value (Iivari, 2007; Niehaves, 2007). Third, the design was evaluated in a substantive area (sustainability transformation in a relatively small organisation). Important boundary conditions are (a) the domain in terms of sustainability transformations and (b) other organisational characteristics such as size and type of organisation. For instance, in our case a relatively small group participated in the sensemaking process, and it might be argued that the system would not be applicable in bigger organisations. However, we used prior theory as justificatory knowledge and provided design principles that may be applied in other settings, thus allowing for the generalisation of our findings – generalisability from theory to description (Lee & Baskerville, 2003). To empirically test and confirm the applicability of the proposed design principles beyond the context that was studied, it is necessary to apply them in different, perhaps contrasting settings (Lee, 1989) to evaluate their prescriptive accuracy under varying boundary conditions (Seidel & Watson, 2014). Fourth, it remains to be tested how practitioners will use the design principles, and whether they will find them useful. Such investigation must consider whether the terminology borrowed from sensemaking theory is readily accessible for practitioner users, or whether an alternative lexicon might be more appropriate. Still, through implementing a prototypical system based on these design principles, we have shown that they are effective in that they can be implemented and lead to the intended result.

## Conclusion

Sensemaking is a crucial process as organisations strive to become environmentally sustainable. In this paper, we set out to investigate how information systems should be designed to support sensemaking in environmental sustainability transformations. We identified affordances required in organisational sensemaking, identified material properties that provide these affordances to certain users and proposed a set of design principles that we revised through several rounds of building and evaluating a prototypical implementation. We used a processoriented view of sensemaking, and this theoretical perspective is independent from the substantive context we

## About the Authors

Stefan Seidel is Associate Professor of Information Systems at the University of Liechtenstein. His main research interests are IS-enabled organizational and societal transformation, organizational creativity and innovation, and green information systems. Stefan’s work has appeared in major journals, including MIS Quarterly, Journal of the Association for Information Systems, and Journal of Information Technology.

Leona Chandra Kruse is a Ph.D. candidate at the Institute of Information Systems at University of Liechtenstein. She has a background in psychology and entrepreneurship. Her research interests comprise the formulation of prescriptive knowledge, green IS, digital leadership and application of psychological theories in information systems.

Nadine Sze´kely is a post-doc at the Institute of Information Systems at University of Liechtenstein. Her research

## References

A D and P G (2005) A critical analysis of decision support systems research. Journal of Information Technology 20(2), 67–87.

ARNOTT D and PERVAN G (2014) A critical analysis of decision support systems research revisited: The rise of design science. Journal of Information Technology 29, 269–293.

ARTHUR WB (2009) The Nature of Technology: What It Is and How It Evolves. Simon and Schuster, New York.

studied. It is our contention that that the formulated design principles can be expected to be relevant in a number of settings where organisations are interested in supporting organisational sensemaking. Sensemaking is highly relevant in nearly every area of human life, at individual, organisational and societal levels, and as a discipline, we are challenged to better understand how sensemaking can be supported through IS. Not only is sensemaking required in becoming environmentally sustainable—certainly one of the grand challenges of our time—but also in other important areas such as strategy development (e.g., Stieger et al, 2012), product development (e.g., Kock et al, 2006) or data analysis (Grolemund & Wickham, 2014).

## Acknowledgements

We thank the editorial and review team for their detailed and developmental feedback, which helped us shape our work and which enhanced our contribution. This research was funded by the Research Fund of the University of Liechtenstein (Forschungsfo¨rderungsfonds der Universita¨t Liechtenstein).

focuses on green information systems, in particular on the question of how information systems can contribute to organisational sustainability transformations.

Michael Gau received his degree in information and communication engineering from the Vorarlberg University of Applied Sciences, Austria. He works as a systems engineer at the Institute of Information Systems at the University of Liechtenstein and at Bachmann Electronics.

Daniel Stieger received his doctorate in business administration from the Innsbruck University School of Management, Austria, and is managing partner of Modellwerkstatt, a company integrating customers in software engineering processes.

A WG and Z RF (1992) Organization science, managers, and language games. Organization Science 3(4), 443–460.

B C, A S, C G, R C and K N (2016) Collaborative sense-making during simulated Intelligence Analysis Exercises. International lournal of Human-Computer Studies 86, 94–108

B P and R K (2000) Why companies go green: a model of ecological responsiveness. Academy of Management Journal 43(4), 717–736.

BASKERVILLE R and PRIES-HEJE J (2010) Explanatory design theory. Business and Information Systems Engineering 2(5), 271–282.

BASU K and PALAZZO G (2008) Corporate social responsibility: a process model of sensemaking. Academy of Management Review 33(1), 122–136.

BEX F, VAN DEN BRAAK S, VAN OOSTENDORP H, PRAKKEN H, VERHEIJ B, and VREESWIJK G (2007) Sense-making software for crime investigation: how to combine stories and arguments? Law, Probability and Risk 6(1–4), 145–168.

BOLand JR RJ (1984) Sense-making of accounting data as a technique of organizational diagnosis. Management Science 30(7), 868–882.

BOLand JR RJ, AND TENKASI RV (1995) Perspective making and perspective taking in communities of knowing. Organization Science 6(4), 350–372.

BOLand JR RJ, TENKASI RV, AND TE’ENI D (1994) Designing information technology to support distributed cognition. Organization Science 5(3), 456–475.

BOLANDER P, and SANDBERG J (2013) How employee selection decisions are made in practice. Organization Studies 34(3), 285–311.

BROWN AD (2004) Authoritative sensemaking in a public inquiry report. Organization Studies 25(1), 95–112.

BROWN AD, COLVILLE I, and PYE A (2014) Making sense of sensemaking in organization studies. Organization Studies 36(2), 265–277.

BRUNER JS (1990) Acts of Meaning. Harvard University Press, Harvard.

B AC, N AK, R M and M KM (2010) Community based innovation contests: where competition meets cooperation. Creativity and Innovation Management 19(3), 290–303.

B T (2011) Compliance with institutional imperatives on environmental sustainability: Building theory on the role of green IS. The Journal of Strategic Information Systems 20(1), 6–26.

CHANDRA L, SEIDEL S and GREGOR S (2015) Prescriptive knowledge in IS research: Conceptualizing design principles in terms of materiality, action, and boundary conditions. Proceedings of the 48th Hawail International Conference on System Sciences (HICSS 2015).

CHURCHMAN D and HANISCH J (2005) MAKING SENSE IN ISOLATION: The Influences of computer-mediated communication technologies on shared contexts. Australian and New Zealand Communication Association and University of Canterbury.

COLLINS CM, STEG L and KONING MAS (2007) Customers’ values, beliefs on sustainable corporate performance, and buying behavior. Psychology and Marketing 24(6), 555–577.

CORLEY KG, and GIOIA DA (2011) Building theory about theory building: What constitutes a theoretical contribution? Academy of Management Review 36(1), 12–32.

DEGIRMENCI K and RECKER J (2016) Boosting green behaviors through information systems that enable environmental sensemaking. Proceedings of the 37th International Conference on Information Systems (ICIS 2016), Dublin, Ireland.

DERVIN B (1998) Sense-making theory and practice: an overview of user interests in knowledge seeking and use. Journal of Knowledge Management 2(2), 36–46.

DERVIN B (1999) Chaos, order and sense-making: a proposed theory fo information design. In Information Design (Jacobson R, Ed), pp 35–57. MIT Press, Cambridge.

ELLIOT S (2011) Transdisciplinary perspectives on environmental sustain ability: a resource base and framework for IT-enabled business transformation. MIS Quarterly 35(1), 197–236.

F S and A B (2012) The materiality of technology: An affordance perspective. In Materiality and Organizing: Social Interaction in a Technological World (Leonardi PM, Nardi BA, Kallinikos J, Eds), pp 237–258. Oxford University Press, Oxford.

F A-L and W J (2014) Affordances for practice. Information and Organization 24(4), 236–249.

FESTINGER L (1957) A Theory of Cognitive Dissonance. Standford University Press. Standford

GEPHART R, TOPAL C and ZHANG Z (2012) Future-oriented sensemaking: temporalities and institutional legitimation. In Process. Sensemgkina. and Organizing (Perspectives on Process Organization Studies), (Hernes T, Maitlis S, Eds), pp 275–300. Oxford University Press, Oxford.

GIBSON JJ (1977) The theory of affordances. In Perceiving, Acting and Knowing: Toward an Ecological Psychology (Shaw R, Bransford J, Eds), pp 67–82. Lawrence Erlbaum Associates, Hillsdale.

GIOIA DA (2006) On Weick: an appreciation. Organization Studies 27(11), 1709–1721.

GIOIA DA and CHITTIPEDDI K (1991) Sensemaking and sensegiving in strategic change initiation. Strategic Management Journal 12(6), 433–448.

GIOIA DA, CORLEY KG and FABBRI T (2002) Revising the past (while thinking in the future perfect tense). Journal of Organizational Change Management 15(6), 622–634.

GOODLand R (1995) The concept of environmental sustainability. Annual Review of Ecology and Systematics 26, 1–24.

GREGOR S and HEVNER AR (2013) Positioning and presenting design science research for maximum impact. MIS Quarterly 37(2), 337–355.

GREGOR S and JONES D (2007) The anatomy of a design theory. Journal of the Association for Information Systems 8(5), 313–335.

GROLEMUND G and WICKHAM H (2014) A cognitive interpretation of data analysis. International Statistical Review 82(2), 184-204.

HABERMAS J (1984) The theory of communicative action: Vol. 1. Reason and the rationalization of society. Beacon, Boston.

HARTSON R (2003) Cognitive, physical, sensory, and functional affordances in interaction design. Behaviour & Information Technology 22(5), 315–338.

HASAN H and GOULD E (2001) Support for the sense-making activity of managers. Decision Support Systems 31(1), 71–86.

H B and J¨ S (1978) Designing semi-confusing information systems for organizations in changing environments. Accounting, Organizations and Society 3(1), 47–64.

HEDBERG B and JO¨ NSSON S (1982) Designing semiconfusing information systems for changing organizations. ACM SIGMIS Database 13(2–3), 12–25.

HEVNER AR and CHATTERJEE S (2010) Design Research in Information Systems. Springer, New York.

H AR, M ST, J P and R S (2004) Design science in information systems research. MIS Quarterly 28(1), 75–105.

IIVARI J (2007) A paradigmatic analysis of information systems as a design science. Scandinavian Journal of Information Systems 19(2), 39–64.

IIVARI J (2010) Twelve theses on design science research in information systems. In Design Research in Information Systems (Hevner AR, Chatterjee S, Eds), pp 43–62. Springer, New York.

IIVARI J (2015) Distinguishing and contrasting two strategies for design science research. European Journal of Information Systems 24(1), 107–115.

JUNG Y and LYYTINEN K (2014) Towards an ecological account of media choice: a case study on pluralistic reasoning while choosing email. Information Systems Journal 24(3), 271–293.

K G, M B and H RR (2006a) Making sense of sensemaking 1: alternative perspectives. IEEE Intelligent Systems 21(4), 70–73.

KLEIN G, MOON B and HOFFMAN RR (2006b) Making sense of sensemaking 2: a macrocognitive model. IEEE Intelligent Systems 21(5), 88–92.

K N, L GS, D KE and A AE (2006) Team adaptation to electronic communication media: evidence of compensatory adaptation in new product development teams. European Journal of Information Systems 15(3), 331–341.

K JP (2012) Accelerate! Harvard Business Review November 2012, 44-62.

K RA and C MA (2009) Focus Groups: A Practical Guide for Applied Research. Sage, London

L AS (1989) Case studies as natural experiments. Human Relations 42(2), 117–137.

LEE AS and BASKERVILLE RL (2003) Generalizing generalizability in information systems research. Information Systems Research 14(3), 221–243.

L PM (2011) When flexible routines meet flexible technologies: affordance, constraint, and the imbrication of human and material agencies. MIS Quarterly 35(1), 147–168.

LEONARDI, P. M. (2012) Materiality, sociomateriality, and socio-technical systems: What do these terms mean? How are they related? Do we need them? In Materiality and Oraanizina: Social Interaction in a Technological World (Leonardi PM, Nardi BA, Kallinikos J, Eds), pp 25–48. Oxford University Press, Oxford.

LEONARDI PM and BARLEY SR (2008) Materiality and change: Challenges to building better theory about technology and organizing. Information and Organization 18(3), 159–176.

LOUIS MR (1980) Surprise ad sense making: what newcomers experience in entering unfamilar organizational settings. Administrative Science Quarterly 25(2), 226–251.

MAIER JR (2011) Affordance Based Design: Theoretical Foundations and Practical Applications. VDM Publishing, Saarbru¨cken.

MAIER JR and FADEL GM (2009) Affordance based design: a relational theory for design. Research in Engineering Design 20(1), 13–27.

MAITLIS S (2005) The social processes of organizational sensemaking. Academy of Management Journal 48(1), 21–49.

MAITLIS S and CHRISTIANSON M (2014) Sensemaking in organizations: taking stock and moving forward. Academy of Management Annals, 8(1), 57–125.

MAITLIS S, VOGUS TJ and LAWRENCE TB (2013) Sensemaking and emotion in organizations. Organizational Psychology Review 3(3), 222–247.

MARKUS ML and SILVER MS (2008) A foundation for the study of IT effects: a new look at DeSanctis and Poole’s concepts of structural features and spirit. Journal of the Association for Information Systems 9(10), 609–632.

MASSEY AP and CLAPPER DL (1995) Element finding: the impact of a group support system on a crucial phase of sense making. Journal of Management Information Systems 11(4), 149–176.

MELVILLE NP (2010) Information systems innovation for environmenta sustainability. MIS Quarterly 34(1), 1–21.

MUHREN W, EEDE GVD and VAN DE WALLE B (2008) Sensemaking and implications for information systems design: findings from the Democratic Republic of Congo’s ongoing crisis. Information Technology for Development 14(3), 197–212.

NIEHAVES B (2007) On epistemological pluralism in design science. Scandinavian Journal of Information Systems 19(2), 93–104.

NORMAN DA (1988) The Psychology of Everyday Things. Basic Books, New York.

N DA (1999) Affordance, conventions, and design. Interactions 6(3), 38–43.

ORLIKOWSKI WJ (2007) Sociomaterial practices: exploring technology at work. Organization Studies 28(9), 1435–1448.

PARRISH JR JL (2008) Sensemaking in Information Systems: Toward a Sensemaking Inquiring System. University of Central Florida Orlando, Florida.

PEFFERS K, TUUNANEN T, ROTHENBERGER MA and CHATTERJEE S (2007) A design science research methodology for information systems research. Journal of Management Information Systems 24(3), 45–77.

PICCOLI G (2012) Information Systems for Managers: Texts & Cases. Wiley, Hoboken.

PILLER FT and WALCHER D (2006) Toolkits for idea competitions: a novel method to integrate users in new product development. R&D Management 36(3), 307–318.

SandBERG J AND TSOUKAS H (2015) Making sense of the sensemaking perspective: its constituents, limitations, and opportunities for further development. Journal of Organizational Behavior 36(S1), S6–S32.

SEIDEL S and BERENTE N (2013) Toward ‘‘third wave’’ information systems research: Linking sociomaterial practice with broader institutional logics. Proceedings of the 34th International Conference on Information Systems (ICIS 2013), Milan, Italy.

S S, R J and B J (2013) Sensemaking and sustainable practicing: functional affordances of information systems in green transformations. MIS Quarterly 37(4), 1275–1299.

S S and W RT (2014) Improving the societal effectiveness of IS research: the pursuit of prescriptive accuracy. Available at SSRN 2477917.

SEIN MK, HENFRIDSSON O, PURAO S, ROSSI M and LINDGREN R (2011) Action design research. MIS Quarterly 35(1), 37–56.

STARBUCK WH and MILLIKEN FJ (1988) Executives’ perceptual filters: what they notice and how they make sense. In The Executive Effect: Concepts and Methods for Studying Top Managers (Hambrick DC, Ed), pp 35–65. JAI, Greenwich.

STIEGER D, MATZLER K, CHATTERJEE S and LADSTAETTER-FUSSENEGGER F (2012) Democratizing strategy: how crowdsourcing can be used for strategy dialogues. California Management Review 54(4), 44–68.

STRONG DM, VOLKOFF O, JOHNSON SA, PELLETIER LR, TULU B, BAR-ON I, … GARBER L (2014) A theory of organization-EHR affordance actualization. Journal of the Association for Information Systems 15(2), 53–85.

TAYLOR JR and VAN EVERY EJ (2000) The Emergent Organization: Communication as Its Site and Surface. Erlbaum, Mahwah.

THOMAS JB, CLARK SM, and GIOIA DA (1993) Strategic sensemaking and organizational performance: linkages among scanning, interpretation, action, and outcomes. Academy of Management Journal 36(2), 239–270.

TREEM JW and LEONARDI PM (2012) Social media use in organizations: exploring the affordances of visibility, editability, persistence, and association. Communication Yearbook 36, 143–189.

UMAPATHY K (2010) Requirements to support collaborative sensemaking. Paper presented at the Computer Supported Cooperative Work (CSCW) Workshop on Collaborative Information Seeking.

URQUHART C (2013) Grounded Theory for Qualitative Research: A Practical Guide. Sage, London.

VAN DER HEIJDEN A, CRAMER JM and DRIESSEN PPJ (2012) Change agent sensemaking for sustainability in a multinational subsidiary. Journal of Organizational Change Management 25(4), 535–559.

VOLKOFF O and STRONG D (2013) Critical realism and affordances: theorizing IT-associated organizational change processes. MIS Quarterly 37(3), 819–834.

WALLS JG, WIDMEYER GR and EL SAWY OA (1992) Building an information system design theory for vigilant EIS. Information Systems Research 3(1), 36–59.

WATSON RT, BOUDREAU M-C and CHEN AJ (2010) Information systems and environmentally sustainable development: energy informatics and new directions for the IS community. MIS Quarterly 34(1), 23–38.

WEICK KE (1979) The Social Psychology of Organizing. Addison-Wesley, Reading.

WEICK KE (1988) Enacted sensemaking in crisis situations. Journal of Management Studies 25(4), 305–317.

WEICK KE (1995) Sensemaking in Organizations (Vol. 3). Sage, London.

WEICK KE and MEADER DK (1993) Sensemaking and group support systems. In Group Support Systems: New Perspectives (Jessup L, Valacich J, Eds), pp 230–252.

WEICK KE, SUTCLIFFE KM and OBSTFELD D (2005) Organizing and the process of sensemaking. Organization Science 16(4), 409–421.

WHITEMAN G and COOPER WH (2011) Ecological sensemaking. Academy of Management Journal 54(5), 889–911.

WINTER R (2008) Design science research in Europe. European Journal of Information Systems 17(5), 470–475.

WITTGENSTEIN, L (2010) Philosophical Investigations. Wiley, Hoboken

W A (2005) The role of scenarios as prospective sensemaking devices. Management Decision 43(1), 86–101.

Z RF, G TL, M A, D DJ and F S (2007) Information technology and the changing fabric of organization. Organization Science 18(5), 749–762.

## Appendix A: Development of design principles and instantiation

See Tables A.1, A.2, and A.3.

Table A.1 Overview of first round of developing, demonstrating and valuation

<table><tr><td>Design principle specification</td><td>Instantiation</td><td>Findings</td><td>Formalisation</td></tr><tr><td>DP 1: Provide novel information in the form of environmental facts, observations or general behaviour, so that the system affords users disruptive ambiguity and surprise in environmental sustainability transformations</td><td>Presentation of indicators through a read-only web platform: paper, plastic cup, paper towel and waste production</td><td>Affordance enactment:The affordance was enactedConstraints and improvement:Lack of data: The system should provide more environmental facts (e.g., comparative data from other institutions) as well as an overview of alternative potential actions</td><td>Design principle not changed</td></tr><tr><td>DP 2: Provide features to store and categorise ideas, so that the system affords noticing and bracketing to users in environmental sustainability transformations</td><td>Posting comments to notice and to bracket ideasDrop-down menu with three different labels for each specific comment: problem-centric, solution-centric and plain Check box with the options “important,” “problem,” “solution,” “doable now” and “doable later” to allow all users to qualify a comment</td><td>Affordance enactment:The affordance was enactedConstraints and improvement:Unclear labelling: The distinction between “doable now” and “doable later” was not clearInconsistent labelling: Some comments were labelled “doable now” or “doable later” even though they were not labelled as solutions</td><td>Design principle not changed</td></tr><tr><td>DP 3a: Provide features for interactive communication, so that the system affords users to engage in an open and inclusive discussion in environmental sustainability transformationsDP 3b: Provide users with an overview of all other users along with features for direct communication between users, so that the system affords users to engage in an open and inclusive discussion in environmental sustainability transformations</td><td>Direct messaging implemented through a text box and send button on the web platform Text box to enter and post replies to commentsCommunity view, where all members are displayed with names and optional photos Explore topics view, where topics are displayed either chronologically or by number of views; tabulators to choose between the two options</td><td>Affordance enactment:The affordance was enactedConstraints and improvement:Relating comments: The strict sequential order of comments was seen as constraining an open and inclusive communication; users used workarounds such as the “@” symbol to relate comments to other commentsEditing: Comments should be editable once postedUser activity: There should be information about user activity</td><td>New design principles:DP 3c: Provide features to relate comments to other comments so that the system affords users to comprehend circumstances and turning them into words and categories on a social ground.DP 3d: Provide features to assign roles to users so that the system affords user-specific actions, such as moderation of discussions.</td></tr><tr><td>DP 4: Provide features for categorisation of action possibilities to distinguish presumptions from actual planed actions, so that the system affords users presumption and action planning in environmental sustainability transformations</td><td>Drop-down menu with two different labels for each specific solution entry: doable now and doable later“Doable Now” view, where all entries that have been rated “doable now” by the majority of voters are displayedAn “action plan view,” where those actions displayed under the “doable now” view are displayed in a separate window accessible from the website’s main page</td><td>Affordance enactment:The affordance was enactedConstraints and improvement:Missing feedback mechanism: It was expressed that there should be feedback about actionsLack of clarity of action plan</td><td>Design principle not changed</td></tr></table>

Table A.2 Overview of second round of developing, demonstrating, and evaluation

<table><tr><td>Design principle specification(revised)</td><td>Instantiation (revised)</td><td>Findings</td><td>Formalisation</td></tr><tr><td rowspan="19">DP 1:Provide novel information in the form of environmental facts, observations or general behaviour, so that the system affords users disruptive ambiguity and surprise in environmental sustainability transformationsDP2:Provide features to store and categorise ideas, so that the system affords noticing and bracketing to users in environmental sustainability transformationsDP 3a:Provide features for interactive communication, so that the system affords users to engage in an open and inclusive discussion in environmental sustainability transformationsDP 3b:Provide users with an overview of all other users along with features for direct communication between users, so that the system affords users to engage in an open and inclusive discussion in environmental sustainability transformationsDP 3c:Provide features to relate comments to other comments, so that the system affords users to comprehend circumstances and turning them into words and categories on a social ground in environmental sustainability transformationsDP 3d:Provide features to assign roles to users so that the system affords user-specific actions, such as moderation of discussions in environmental sustainability transformationsDP 4:Provide features for categorisation of action possibilities to distinguish presumptions from actual planed actions, so that the system affords users presumption and action planning in environmental sustainability transformations</td><td rowspan="18">Topics can only be posted by moderators to ensure that data is provided to trigger disruptive ambiguity and surpriseNew categories to label comments (“infrastructural” and “behavioural” instead of “doable now” and “doable later”)Comments can only be qualified as “infrastructural” or “behavioural” once they have been identified as “feasible solutions”Comments can be directly linked to other commentsIntroduction of a role system (users, moderators, decision makers)Additional information about users (how many posts, etc.)</td><td rowspan="18">Affordance enactment:The affordance was enacted.Constraints and improvement:Unclarity of voting mechanism:The voting mechanism was not used extensively, and it was expressed that it was not entirely clear and too complexAffordance enactment:The affordance was enactedConstraints and improvement:Lack of “add topics” feature: While now all topics provided data, it was expressed that the lack of an “add topics” feature constrained an open and inclusive communication.Relating comments: Users still used workarounds such as the “@” symbol to relate comments to other comments</td><td rowspan="18">Design principle not changedRevised design principle:DP 2: Provide functions of storing and simple and unambiguous categorisation of ideas, so that the system affords noticing and bracketing to users in environmental sustainability transformations.Design principle not changed</td></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr><td>Labelling decision makersChanged voting mechanism (“behavioural change” and “infrastructural change”) to improve clarity of the action plan</td><td>Affordance enactment:The affordance was enactedConstraints and improvement:Lack of feedback mechanism: The feedback mechanism in terms of dedicated decision makers was not used</td><td>New design principle:DP 4b: Provide features for dedicated feedback about the implementation and consequences of the implementation of actions</td></tr></table>

Table A.3 Overview of third round of developing, demonstrating and evaluation

<table><tr><td>Design principle specification (revised)</td><td>Instantiation (revised)</td><td>Findings</td><td>Formalisation</td></tr><tr><td rowspan="19">DP 1: Provide novel information in the form of environmental facts, observations or general behaviour, so that the system affords users disruptive ambiguity and surprise in environmental sustainability transformationsDP 2: Provide functions of storing and simple and unambiguous categorisation of ideas, so that the system affords noticing and bracketing to users in environmental sustainability transformationsDP 3a: Provide features for interactive communication, so that the system affords users to engage in an open and inclusive discussion in environmental sustainability transformationsDP 3b: Provide users with an overview of all other users along with features for direct communication between users, so that the system affords users to engage in an open and inclusive discussion in environmental sustainability transformationsDP 3c: Provide features to relate comments to other comments, so that the system affords users to comprehend circumstances and turning them into words and categories on a social ground in environmental sustainability transformationsDP 3d: Provide features to assign roles to users so that the system affords user-specific actions, such as moderation of discussions in environmental sustainability transformationsDP 4a: Provide features for categorisation of action possibilities to distinguish presumptions from actual planed actions, so that the system affords users presumption and action planning in environmental sustainability transformationsDP 4b: Provide features for dedicated feedback about the implementation and consequences of the implementation of actions in environmental sustainability transformations</td><td rowspan="18">-Improved clarity of labelling mechanism (problem, solution, other)Simplification of voting mechanismRe-introduction of the add topic feature; however, topics have to be reviewed by moderators to ensure they provide an informational basisImproved clarity of “relating comments” feature</td><td rowspan="18">-Respondents understand the new material properties and see them as appropriateRespondents understand the new material properties and see them as appropriate</td><td rowspan="18">Design principle not changedDesign principle not changedDesign principle not changed</td></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr><td>Decision makers can assign certain states to a proposed action</td><td>Respondents understand the new material properties and see them as appropriate</td><td>Design principle not changed</td></tr></table>

## Appendix B: Usage data

See Table B.1.

Table B.1 Quantitative usage data

<table><tr><td>Item</td><td>Cycle 1</td><td>Cycle 2</td></tr><tr><td>Registered users</td><td>65</td><td>99</td></tr><tr><td>Users logged in during the cycle</td><td>65</td><td>45</td></tr><tr><td>Users actively participating (either through topic views, commenting or through rating)</td><td>51</td><td>42</td></tr><tr><td>Number of comments</td><td>53</td><td>28</td></tr><tr><td>Number of topics created by user</td><td>8</td><td>N/Aa</td></tr><tr><td>Number of users creating a topic</td><td>6</td><td>N/A</td></tr><tr><td>Number of users posting a comment</td><td>21</td><td>17</td></tr><tr><td>Number of doable now/behavioural change ratings</td><td>97</td><td>35</td></tr><tr><td>Number of doable later/infrastructural change ratings</td><td>17</td><td>28</td></tr><tr><td>Number of problem ratings</td><td>40</td><td>60</td></tr><tr><td>Number of solution ratings</td><td>114</td><td>95</td></tr><tr><td>Number of importance ratings</td><td>113</td><td>71</td></tr><tr><td>Number of users making a doable now/behavioural change rating</td><td>22</td><td>7</td></tr><tr><td>Number of users making a doable later/infrastructural change rating</td><td>7</td><td>9</td></tr><tr><td>Number of users making a problem rating</td><td>12</td><td>11</td></tr><tr><td>Number of users making a solution rating</td><td>23</td><td>21</td></tr><tr><td>Number of users making an importance rating</td><td>19</td><td>15</td></tr><tr><td>Items on the action plan</td><td>20</td><td>20b</td></tr></table>

<sup>a</sup>In the second cycle, the topics were pre-defined.  
<sup>b</sup>Of which, 15 items are presented as behavioural changes and 12 items as infrastructural changes.

## Appendix C: Focus groups

## C.1 Focus Group Procedure

After each of the first two rounds (each of which included approximately two weeks of using the platform in a real world setting), two focus groups were organised with users of the platform. A final focus group was conducted after the final revision of the system was done. Table C.1 provides an overview.

It was aimed to create an open and friendly atmosphere since ‘‘the intent of the focus group is to promote self-disclosure among participants’’ (Krueger & Casey, 2009, p. 4). In each focus group discussion, one moderator and one observer were present, each of them selected from the research team. The observer was responsible to take field notes consisting of important opinions relevant to the purpose of this study, including gesture and expression if necessary.

Table C.1 Focus group overview

<table><tr><td>#</td><td>Date</td><td>Number of participants</td></tr><tr><td>1</td><td>2013-12-09 (after first cycle)</td><td>5</td></tr><tr><td>2</td><td>2013-12-10 (after first cycle)</td><td>4</td></tr><tr><td>3</td><td>2015-02-05 (after second cycle)</td><td>4</td></tr><tr><td>4</td><td>2015-02-25 (after second cycle)</td><td>4</td></tr><tr><td>5</td><td>2015 (after final revision)</td><td>4</td></tr></table>

The moderator did not take part in the discussion, but facilitated it and encouraged all participants to express their opinions.

The discussion of the first four focus groups (#1–4) was divided into opening, introductory, transition, key and ending sections based on the framework proposed by Krueger & Casey (2009). The opening section served as an icebreaker, where the participants got to know each other and understood the purpose of the discussion as well as its confidentiality and their freedom of expression. In the introductory section, participants were asked to think back and remember how they got to hear about the system and what the first thing was that came into their mind when they heard about it. The transitory section was planned to lead the way into the key section. In the transitory section, the participants were asked to describe their first impression of using the system. In the key section, the participants were shown specific parts of the platform and were asked to either select at least one of from a set of items developed to evaluate affordance perception (Appendix C.2) or write their own responses to the question ‘‘what does this part allow you to do?’’. The goal was to see whether the material properties were interpreted to give rise to certain affordances by users. The available responses comprised of eight phrases and eight statements that articulated one of the four affordances in common language. In order to avoid misleading participants into a forced response, they were also allowed to select none of the available responses and write their own instead.

Table C.2 Focus group items

<table><tr><td>Affordance</td><td>Items</td></tr><tr><td>Experiencing disruptive ambiguity and surpriseNoticing and bracketing</td><td>I realise that there are indeed environmental issues at the universityThis revelation prompts me to take part in the discussionI can differentiate between different categories, such as problem/solution and whether it can be implemented now or laterI can express ideas and mark them with different labels, such as important, problem, solution, doable now and doable later</td></tr><tr><td>Engaging in an open and inclusive communication</td><td>Through the communication, I feel involved in an open discussion about making the university a greener placeI can engage in conversations with other members.</td></tr><tr><td>Presumption and action planning</td><td>I see which actions can be done in the near futureI can plan how to solve, or at least minimise, the environmental issues at the University</td></tr></table>

Focus group #5 was conducted after the system was changed based on the results from the second round of development, demonstration, and use. All participants had participated in earlier rounds. During the focus group, they (a) were shown a summary of the feedback provided in the last focus groups, (b) were shown the changes that were made, (c) were given the chance to use the new features and (d) were asked what they thought about the new feature, and whether they adequately addressed the issues that were raised in previous rounds.

## C.2 Instrument for Evaluating Affordance Identification by Users

We developed an instrument to evaluate in how far certain material properties were interpreted by individuals to give raise to certain affordances. We developed the set of responses in three steps.

• First, words and phrases synonymous to the names of the affordances were collected by one of the team members, and the affordances were thus assumed as categories (e.g., indicating and categorising were related to noticing and bracketing). Team members sorted each word or phrase into one of the four categories in order to test the content validity of the four categories.

• Second, the same member of the research team developed statements that represented the behaviours or actions captured by the affordance (e.g., ‘‘I can differentiate between different categories, such as problem/solution and whether it can be implemented now or later’’ was an item representing the affordance ‘‘noticing and bracketing’’). The content validity was tested again among the research team members, as they marked those statements that were difficult to understand and sorted the remaining statements into the four categories.

• Third, a pilot study was conducted. Three people outside the research team were shown each part of the platform, asked the questions, and requested to select those items they felt suitable to answer the questions, or write their own answers in case they found no answer suitable. Based on the result of the pilot study, minor revisions were undertaken before we concluded that the set of responses were appropriate. Table C.2 provides an overview of the instrument.
