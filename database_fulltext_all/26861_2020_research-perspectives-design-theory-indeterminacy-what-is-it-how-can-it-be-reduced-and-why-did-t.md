---
otero_id: 26861
otero_key: "QFPT4STY"
title: "Research Perspectives: Design Theory Indeterminacy: What Is it, How Can it Be Reduced, and Why Did the Polar Bear Drown?"
authors: "Roman Lukyanenko; Jeffrey Parsons"
year: "2020"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00639"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
9-11-2020

# Research Perspectives: Design Theory Indeterminacy: What Is it, How Can it Be Reduced, and Why Did the Polar Bear Drown?

Roman Lukyanenko , roman.lukyanenko@hec.ca

Jeffrey Parsons

, jeffreyp@mun.ca

Follow this and additional works at: https://aisel.aisnet.org/jais

ISSN 1536-9323

# Research Perspectives: Design Theory Indeterminacy: What Is it, How Can it Be Reduced, and Why Did the Polar Bear Drown?

Roman Lukyanenko,<sup>1</sup> Jeffrey Parsons<sup>2</sup>

<sup>1</sup>HEC Montréal, Canada, roman.lukyanenko@hec.ca <sup>2</sup>Memorial University of Newfoundland, Canada, jeffreyp@mun.ca

## Abstract

Design science research strives to be practical and relevant. Yet few researchers have examined the extent to which practitioners can meaningfully utilize theoretical knowledge produced by design science research in solving concrete real-world problems. Are design theories developed by scientists readily amenable to application by practitioners? Does the application of a theory by practitioners always lead to the outcomes predicted (by the scientists)? We examine a particularly difficult challenge—ensuring that the development and deployment of an IT artifact by practitioners based on a design theory result in appropriate changes in the environment predicted by the design theory. As we show in our paper, a gulf exists between theoretical propositions and concrete issues faced in practice—a challenge we refer to as design theory indeterminacy. Design theory indeterminacy might result in considerable ambiguity when implementing a design theory in practice and reduce the potential relevance of information systems knowledge. In this paper, we articulate the problem of design theory indeterminacy, examine factors that contribute to it, and suggest fruitful directions for future research to help reduce it.

Keywords: Design Science Research, Design Theory, Design Theory Indeterminacy, IT Artifact, Design Features, Theoretical Contribution, Rigor and Relevance, Case Study, Citizen Science, Crowdsourcing, Energy Conservation, Information Quality, System Use

Dirk S. Hovorka was the accepting senior editor. This research perspectives article was submitted on August 16, 2017 and went through three revisions.

## 1 Introduction

Seemingly innocuous features of information systems (IS) can have dramatic effects. For example, in a study of the effect of warning messages on energy consumption during showers, Tiefenbeck and colleagues (Tiefenbeck, Goette, et al., 2016) found that, contrary to expectations, a strong warning message depicting the impact of behavior on climate change by showing a polar bear on a melting ice floe increased shower length (and energy consumption) compared to milder messages that showed only water consumption and energy classification rating. The researchers concluded that the “real-world impact of Information Systems” might be influenced by “the potentially unpredictable large effects of ‘seemingly small design choices’” (Ableitner et al., 2017, p. 2).

Surprisingly, the potential of incidental features to produce substantial changes and the difficulty in anticipating their impact in practice has been largely ignored in IS research. A typical information system consists of myriad features, some intentionally designed based on guiding principles, some improvised, and others emerging unexpectedly out of interactions between components. These bundles of features are packaged as information technology (IT) artifacts and introduced in complex organizational settings. It is unclear whether and to what extent IS theories are capable of accounting for the impact of subtle, seemingly incidental, and mundane decisions that need to be made during IS implementation. This applies to IS research broadly but is especially relevant for design theories, a major type of contribution in IS that is especially prevalent in design science research (DSR) (Baskerville, Kaul, & Storey, 2015; Gregor & Hevner, 2013; Hevner & Chatterjee, 2010; Venable, 2006; vom Brocke et al., 2020). This is a timely question, as debate is ongoing on ways to better support practice, with a consensus that IS researchers need to do more to make their work more practically relevant (Hirschheim, 2019; Hovorka et al., 2019).

As with other theories, IS design theories are convenient abstractions, figments of the human mind created to organize and/or act upon reality (Gregor, 2006). However, unlike theories that explain or predict, the goal of design theories is to prescribe action to achieve goals. Design theories are useful insofar as they perform this function reliably in relevant contexts.

It is generally accepted that the mandate of DSR is to make IS practice more effective and efficient by reducing development uncertainty (Venable, 2006; Walls, Widmeyer, & El Sawy, 1992). However, a considerable gap might exist between IS theories and concrete issues faced in practice. We define design theory indeterminacy (DTI) as the absence of a one-toone mapping from design theory prescriptions to specific features in an artifact and methods for deploying the artifact in the environment. DTI means there might be multiple instantiations that are consistent with a design proposition within a design theory. That is, for a proposition of the form “If you want to achieve Y, do X,” there may be more than one way to “do X” in an artifact. For example, in designing a data collection interface, the proposition “If you want to allow users to express emotions, ensure the interface permits flexible data entry” might be useful. However, this abstract proposition does not specify, for example, whether you should choose a “textbox,” a (larger) “text area,” or a list of emojis. A designer, therefore, must make a choice based on considerations that go beyond the proposition being applied. Thus, a textbox might be chosen on the basis that it is smaller, and smaller data entry fields are more aesthetically pleasing to the practitioner.

In such situations, DTI implies that it is impossible to determine whether the outcome results from applying a chosen design proposition or from the ancillary choices made by the designer. As a result of this indeterminacy, a practitioner choosing to implement a design theory might not attain the outcomes specified by the theory.

Design science research has only recently begun to consider this issue and has done so only in a limited way. There is a growing awareness that design theories may be difficult to implement. Gregor and Jones (2007) argue that design theories should have a method of application but leave open the question of how it should be developed. Chandra Kruse and colleagues (Chandra Kruse & Seidel, 2017; Chandra Kruse, Seidel, & Purao, 2016) note the difficulty researchers and practitioners face when implementing abstract design prescriptions (they refer to this as the problem of “design principle reuse”), and call for more work in this area. Mandviwalla (2015) contends that, whereas previous research examined design theory components, an “important gap” remains in being able to “facilitate translation [from design theory] into specific actionable guidelines” (p. 338). Our paper seeks to answer these calls.

Design theory indeterminacy arises from the need to map from abstract propositions to concrete manifestations in artifacts when using a design theory, but also involves complex issues related to causality and measurement. Therefore, DTI cannot be fully eliminated. In this paper, we provide guidance for mitigating the potentially negative consequences of DTI. We consider whether the approaches DSR takes when developing and formulating design theories can be improved with the objective of providing better guidance to practice. In the following, we first position DTI with respect to the ongoing discourse on rigor and relevance in design science research. We then identify the root causes of the problem, including specific challenges that arise when creating an artifact following some design theory. Based on these challenges, we suggest fruitful directions for future research.

## 2 Background: Design Theories in IS

## 2.1 Significance and Nature of Design Theories

The need to understand DTI stems from the importance of design theories in IS. As Goes (2014) explains, design theories are the intellectual tools by which the information systems community can contribute to technological innovation. Design theories further permit the community to engage in solving real world problems (Beck, Weber, & Gregory, 2013; Gregor & Hevner, 2013; Iivari, 2007; vom Brocke et al., 2020).

We do not consider in detail how a design theory is developed but several possibilities exist (Baskerville et al., 2015; Drechsler & Hevner, 2018; Gregor & Hevner, 2013; Purao, 2013). For example, some DSR projects develop a design theory and then an artifact based on it (e.g., Parsons & Wand, 2008), while others abstract theory or principles based on observation of an already existing artifact (e.g., Avdiji et al., 2020).

Table 1. Examples of Design Theories in IS

<table><tr><td>Theory name and reference</td><td>Summary of the design theoryDPs: prescriptive statements, such as design principles that shape the artifact, which become an independent variableOutcomes: dependent variable(s) or outcomes proposed by the theory</td></tr><tr><td>Theory of tailorable design (Germonprez, Hovorka, &amp; Collopy, 2007)</td><td>DPs: Nine reflective (e.g., recognizable components, recognizable conventions) and active (e.g., support for functional requirements, representation of user views) principles that provide the ability for technology to be modified during use.Outcome: Greater artifact tailorability.</td></tr><tr><td>Emergent knowledge processes design theory (Markus, Majchrzak, &amp; Gasser, 2002)</td><td>DPs: Six design and development principles (e.g., design for customer engagement by seeking out naïve users, radical iteration with functional prototypes, designed for off-line action).Outcome: Effective support of emerging knowledge processes.</td></tr><tr><td>A design theory for systems that support convergent and divergent thinking (Müller-Wienbergen, Müller, Seidel, &amp; Becker, 2011)</td><td>DPs: Principles for creating design features that stimulate convergent (e.g., tag trees, filters) and divergent (e.g., generation of intra-and inter-domain stimuli) creative thinking.Outcome: support of convergent and divergent thinking, facilitation of creative work.</td></tr><tr><td>Design theory for classification in information modeling (Parsons &amp; Wand, 2008)</td><td>DPs: Principles for forming good classes, creating subclasses and superclasses (e.g., each new class must support inferences) in information systems modeling.Outcome: Effective information systems development and use.</td></tr><tr><td>Design theory for digital platforms that support online communities (Spagnoletti, Resca, &amp; Lee, 2015)</td><td>DPs: Seven design propositions that stipulate how to develop IT features that support information sharing, collaboration, and/or collective action (e.g., online communities should be connected to popular online social networking services in order to enable the diffusion of codified and abstract information).Outcome: improved information sharing, collaboration, and collective action in online communities.</td></tr></table>

In all cases, the result is a set of abstract statements that practitioners may use to solve problems in contexts different from the ones giving rise to the original design theory.<sup>1</sup>

The specific form an IS design theory should take remains a subject of debate (Gregor, 2006; Gregor & Jones, 2007; Kuechler & Vaishnavi, 2012; Walls et al., 1992; Weber, 2012). For example, Gregor and Jones (2007) identify eight components of a design theory. They argue a design theory typically contains the purpose and scope (e.g., represented by a dependent variable(s) or proposed outcomes, and testable propositions), which predicts the nature of change in reality resulting from applying the theory (e.g., increased adoption of technology or improved decision quality). These outcomes are typically explained by some reference justificatory knowledge (e.g., a kernel theory). Design guidance comes in the form of specific prescriptive statements, frequently called design principles—independent variable(s), principles of form and function that “define the structure, organization and functioning of the design product or design method” (Gregor & Jones, 2007, p. 325). In addition, design theories might provide additional information on how to implement a theory (so-called “principles of implementation”), an expository implementation, and consideration of how artifacts of this kind may evolve (i.e., “artifact mutability”).

While design theory typically provides causal mechanisms that explain the relationship between the antecedent design principles via an instantiated artifact based on these principles, the nature of causality in DSR is unlike that in natural sciences. Although some components of an artifact (e.g., electric circuitry) may behave in a predictable manner (Gregor & Hovorka, 2011, p. 7), an artifact deployed in an environment becomes an open system—one that interacts with its environment (Chaturvedi, Dolk, & Drnevich, 2011; Prat, Comyn-Wattiau, & Akoka, 2015)—making it difficult to precisely identify causal chains that connect the artifact to desired outcomes. Thus, determining and modeling causes in DSR as universal, law-like, and context-free, as is typical in the natural sciences (Bunge, 1998), is unrealistic. Rather, causes in a design theory are constellations of probabilities leading to the outcomes under the right circumstances (Gregor & Hovorka, 2011). As we show later, the nature of causality in DSR is a dimension of DTI.

Many foundational IS theories are design theories. For example, representation theory, proposed by Wand and Weber (1990, 1993, 1995) is one of the “few longstanding, native theories in the Information Systems discipline” (Burton-Jones et al., 2017, p. 1307). Representation theory seeks to lay a broad foundation for the design, development, and use of information systems. Table 1 provides additional examples of design theories, illustrating their prevalence and diversity in the IS discipline (for more examples and analysis, see Walls, Widermeyer, & El Sawy, 2004)

## 2.2 Design Theory Indeterminacy in DSR

Three major themes relevant to the problem of DTI can be observed in DSR. First, there is broad recognition of the importance of generality when formulating design theories. Second, studies have questioned whether the focus on generality results in limitations. Third, research is beginning to investigate the challenges arising when practitioners seek to reuse components (e.g., design principles) of a design theory.

A long-standing assumption in DSR is that the generality of design theories is important and desirable. Gregor and Jones (2007) suggest that principles of form and practice can be represented as an “abstract ‘blueprint’” or as a design method showing “in a generalized form the shape and features” (p. 326) proposed. Walls et al. (1992) recommend addressing “a class of problems” rather than “the design of a specific artifact” (p. 42). In a widely cited example of early design theories in IS, Markus et al. (2002, p. 186), in proposing a theory to support emerging knowledge processes (EKPs), claimed that their theory “generalized to the entire class of EKPs.” This is broadly consistent with the repeated calls within the discipline to study “prototypical” (Weber, 2003) or “generic, archetypal” (Rai, 2017) problems.

A consequence of the preference for greater generality is that most, if not all, design theories are midrange (Kuechler & Vaishnavi, 2008, 2012; Moody, Iacob, & Amrit, 2010; Weber, 2012); that is, moderately abstract (i.e., they do not purport to explain everything) but, as is characteristic of midrange theories, “close enough to observed data to be incorporated in propositions that permit empirical testing” (Merton 1949, p. 39).

Despite the preference for generality and the prevalence of midrange design theories, limitations of this approach have been noted. First, a general form may ignore challenges faced by practitioners. Hevner et al. (2004) caution that an overemphasis on generalizability might come at the expense of relevance and call for balancing these objectives. Second, by abstracting away the rich particulars of real artifacts, some potentially important problems and opportunities embedded in specific instantiations may fail to be uncovered and disseminated. Artifacts bring about changes in the environment, some of which are impossible to anticipate in advance; artifacts “make” new worlds (Dasgupta, 1996; Purao, 2013).

The increasing prominence of design theories has motivated greater efforts to better structure and formalize design theorizing. Venable (2006) argues that a design theory should focus on predicting outcomes of artifact implementation. Gregor and Hovorka (Gregor & Hovorka, 2011; Hovorka & Gregor, 2010) stress the importance of specifying causal mechanisms imbued in artifacts. Researchers are investigating ways of providing greater transparency and formality in formulating design principles to promote their reuse (Chandra Kruse & Seidel, 2017; Chandra Kruse et al., 2016). As Chandra Kruse and Seidel (2017) show, other researchers and designers face considerable challenges when trying to interpret and apply the design principles formulated by researchers. They also raise the possibility that design principles are too abstract and generic and call for more research to investigate this issue (Chandra Kruse et al., 2016). While Gregor and Jones (2007) suggest including “principles of implementation,” which may address some of these concerns, it is unclear what these principles should entail, how they should be formed, and which other components of a design theory they should support.

These efforts point to potential issues in design theorizing, but they focus narrowly on certain components of a design theory (e.g., design principles) and do not specifically consider the problem of DTI as a whole. A design theory has multiple components (e.g., eight according to Gregor and Jones, 2007). As demonstrated below, multiple components of a design theory contribute to indeterminacy. Indeed, some components (e.g., design principles) might interact with others, an idea that, to our knowledge, has not been investigated. Furthermore, we advance another important point: design theories should be viewed not only as shaping specific artifact features, but also as initiating change. A design theory chosen by a practitioner eventually leads to an artifact implemented with typically imprecise theoretical guidance and deployed in complex real settings. We conceptualize DTI as a complex and multifaceted problem requiring purposeful investigation. In the next section, we examine two existing DSR projects based on design theory to demonstrate the existence of DTI and lay the groundwork for understanding it better.

## 3 Demonstrating Design Theory Indeterminacy

To demonstrate the problem of design theory indeterminacy, we use two case studies. As DTI arises when practitioners attempt to implement a design theory in a real-world setting, a case study is especially useful for understanding how it is manifested in practice (Baxter & Jack, 2008; Dubé & Paré, 2003; Lee, 1989; Yin, 2013). Our cases complement each other in the type of evidence they provide, but also offer “literal replication” (Yin, 2013), in that they both support our arguments and lead to similar conclusions. Examining two cases in different contexts also underscores the generalizability of our arguments (Dubé & Paré, 2003; Yin, 2013) and the pervasiveness of DTI.

## 3.1 Case 1: Instance-Based Design Theory

For Case 1, we chose the design theory of instancebased modeling (Lukyanenko et al., 2017; Lukyanenko, Parsons, & Wiersma, 2014; Lukyanenko et al., 2019). The authors explicitly claim that their “work contributes a novel design theory” (Lukyanenko et al., 2017, p. 308), as it explains and predicts why following the proposed design principles results in specific changes in reality.

The theory proposes a set of modeling principles premised on representing unique instances (the independent variable) to increase user participation and the quality of data provided by ordinary people (the dependent variables) in a crowdsourcing context. We selected this design theory because of its success, as evidenced by several publications in prominent IS journals (Lukyanenko et al., 2017; Lukyanenko, Parsons, et al., 2014; Lukyanenko, Parsons, Wiersma, et al., 2019), and in leading scientific journals outside IS (e.g., Lukyanenko, Parsons, & Wiersma, 2016; Parsons, Lukyanenko, & Wiersma, 2011).

As is typical for DSR, the instance-based design theory was proposed in response to a real-world problem— ensuring the quality of information generated by citizen science applications and facilitating greater participation in citizen science projects (Lewandowski & Specht, 2015; Nov, Arazy, & Anderson, 2014). Citizen science is a type of crowdsourcing in which scientists enlist ordinary people to perform research tasks (Bonney et al., 2014; Burgess et al., 2017; Levy & Germonprez, 2017). For example, a popular citizen science project, GalaxyZoo (zooniverse.org), relies on over a million registered online users to classify galaxies from digital photos taken by the Hubble Space Telescope (Fortson et al., 2011; Ponti et al., 2018). Citizen science is widely used in many branches of science (Burgess et al., 2017; Goodchild, 2007; Louv,

Dickinson, & Bonney, 2012; Lukyanenko, Wiggins, & Rosser, 2019; Sieber, 2006; Wiggins & Crowston, 2014).

Despite its growing popularity, a major challenge in citizen science is ensuring that heterogeneous and voluntary online users are able to provide information of sufficient quality to be used in scientific analysis and decision-making (Lukyanenko, Parsons, Wiersma, et al., 2019). This is extremely difficult given that data production occurs online and the data producers (i.e., citizen scientists) are typically anonymous and unpaid volunteers. Consequently, despite the growth in projects and millions of online users involved, scientists remain concerned about relying on citizengenerated data (Burgess et al., 2017; Lewandowski & Specht, 2015). In response, the dominant philosophy in the design of citizen science platforms is to constrain and restrict user input to ensure consistency and uniformity. This typically means that projects require contributors to report observed phenomena (e.g., birds, animals) using a predefined list of classes deemed useful to scientists (e.g., biological species). Since citizens are typically not science experts, this imposes a considerable barrier to participation and might result in lower-quality data, as participants might resort to guessing or even abandon data entry. It also misses an opportunity to collect unanticipated data from citizens.

Instance-based design theory offers an alternative to the dominant class-based design for data collection in citizen science, which focuses on identifying a predefined set of classes of interest to information consumers. With instance-based design theory, users are not forced to classify phenomena using predefined classes (such as biological species), thereby relaxing the requirement that nonexperts understand and follow a given taxonomy. This design theory is based on two reference (kernel) theories: classification theory from cognitive psychology, and Bunge’s ontology. Classification theory (Murphy, 2004; Smith & Medin, 1981) maintains that people are extremely fast and accurate when asked to describe both familiar and unfamiliar objects (instances) using attributes and high-level classes (Rosch et al., 1976). Bunge’s (1977) ontology postulates that the world consists of “things” (which can also be referred to as instances) as the primary elements of existence. These reference theories, translated into the problem space of citizen science, result in the design theory shown graphically in Figure 1.

Using unconstrained collection of attributes and classes makes it possible to capture information seamlessly from nonexpert audiences and is hypothesized to have positive effects on information quality and levels of user engagement (see Figure 1).

The attributes can also be analyzed post hoc to infer classes of interest (e.g., species).<sup>2</sup>

To illustrate the nature of DTI, suppose a real-world project wishes to adopt instance-based design theory. Practically, this means following the design principles provided in the theory to develop a real-world information system that, once deployed in the citizen science context, should deliver high-quality data and encourage more people to participate.

Consider the challenges a designer might face when implementing the instance-based design theory. When designing a new citizen science project, much of the previous experience with class-based design, database normalization, and user interface design, can no longer be leveraged. Further, concomitant with broader DSR, the kernel theories of Bunge’s ontology and cognition were developed outside the context of IS and, more specifically, online citizen science. In addition, the design theory itself is more general than the context of citizen science. As a result, neither the design theory nor the kernel theory underlying it deal with notions of, for example, web servers, programming languages, or client device types, nor do they cover constructs such as citizens, scientists, or species.

Traditionally, surface elements of a system (such as a user interface, navigational structure, and menu choices) can be traced to structural assumptions at the deep (i.e., conceptual) level (Wand & Weber, 1995). Since the underlying information model is instancebased, it follows that surface elements should follow instance-based principles. However, no strategy for mapping the principles in Figure 1 into specific design objects is provided in the design theory. This means that answers to many design questions cannot be justified based on theoretical prescriptions alone. For example, what should the first (landing) and subsequent pages look like? Do the landing page and other pages need to behave differently each time? Should the file structure be dynamic and personalized for each user?

![](/api/attachments/QFPT4STY/fulltext/images/f1e379236fa102daaa0c83d87f8c6b839756043e9c501067812c159b86535351.jpg)  
Figure 1. Key Components of the Instance-Based Design Theory

![](/api/attachments/QFPT4STY/fulltext/images/561845fb49c0c20445de252309011bcc92c457146f4de6fb35dbc1cb18c72773.jpg)  
Note: Images used with permission of the authors (Lukyanenko et al., 2017)  
Figure 2. Example of Free-Form Guided Attribute Collection

Similar ambiguity arises when building a data collection interface. The instance-based approach involves storing information about instances in terms of attributes. Here, a practical question is how to choose interface elements consistent with the design theory. For example, a website might present attributes as a list allowing users to select applicable attributes. This means that all applicable attributes should be modeled in advance. Alternatively, attributes can be entered in a free-form manner—where any attribute is accepted even if it is not found in the existing attribute base. A variation on free-form data collection is guided freeform collection, in which any attribute is accepted but a prompt dynamically makes recommendations based on the string being typed (see, e.g., Figure 2). This is the approach adopted by Lukyanenko et al. (2017).

The choice of a data entry interface leads to additional questions. For example, if a guided free-form interface is chosen, should some (e.g., more common) attributes be cached for better performance? Alternatively, the prompt may be based on an active list of user-created attributes or a static authoritative list. In each case, there are also multiple ways to compute similarity (e.g., literal string match, or using a similarity algorithm). In other words, there are many design alternatives that could be implemented in a way consistent with an abstract design principle.

In addition, it is unclear whether different decisions are better suited to other project objectives. For example, performance and aesthetics were important: a slow or unattractive system might dissuade casual users from contributing. Typically, there is also an objective to make the project available in many different user environments (e.g., mobile devices, desktop systems). Design solutions should be tailored to these different environments. However, some of the interface choices mentioned above might not be appropriate for all environments. For instance, constrained-choice data collection appears to be more suitable for mobile devices, while free-from guided interfaces seem more appropriate for a desktop context. These decisions involve interpretation and fitting the referent design theory with other considerations (e.g., guidelines for mobile computing).

Case 1 thus demonstrates that there are many design decisions that must be made during implementation and it is often unclear which ones are best suited for the chosen design theory. Without explicit guidance from the theory, the choices made may result in outcomes contrary to the theory. We examine this possibility next.

## 3.2 Case 2: Design Theory of Behavioral Feedback

To illustrate the problem of DTI in a different context, we turn to another recent research case investigating DSR in IS. We selected a research project that, like Case 1, bears strong evidence of high scholarly quality and high demonstrable social impact (see, e.g., Tiefenbeck et al., 2019). This research developed a design theory with the goal of lowering energy use and increasing environmental conservation and has been published in leading scientific journals (Tiefenbeck, 2017; Tiefenbeck et al., 2018, 2019; Tiefenbeck, Goette, et al., 2016; Tiefenbeck Schöb, et al. 2016).

The researchers hypothesized that energy conservation (the dependent variable) can be fostered by providing people with direct feedback on their energy consumption (the independent variable or design proposition) (Tiefenbeck, Goette, et al., 2016). They used the theory of salience biases to explain why displaying immediate feedback alters behavior (Tversky, Kahneman, & Moser, 1990) and theories of psychological pressure (Schultz et al., 2016) to explain why people engage in prosocial behavior (e.g., try to conserve energy) when behavioral feedback is provided.

To evaluate this design proposition, the authors designed an artifact—a device that displays water consumption while people are showering. The device was mounted onto shower stalls in hotel rooms and was visible to guests while showering (Tiefenbeck, Goette, et al., 2016). Four versions of the artifact were implemented in the form of four displays of a smart shower meter (Figure 3). Each design aimed to increase the intensity of the treatment. The control group’s meter displayed only the water temperature, Treatment Group 1 saw both the temperature and water consumption in liters, and Treatment Group 2 saw the water temperature, liters used, and an energy efficiency classification ranging from A (most efficient) to G (least efficient), adapted from the European Energy Efficiency scale. Finally, treatment group three’s meter also displayed an image of a polar bear on an ice floe that shrunk as the shower continued, eventually leaving the bear in the water. This element conveyed the impact of energy consumption on the environment and climate change. This design was intended to instantiate the independent variables of the study and the authors hypothesized that it would have a strong positive impact on energy conservation.

![](/api/attachments/QFPT4STY/fulltext/images/40bc886c8595950c6680535273b43950ed2b0706a25bf2baf745b2027785fcf8.jpg)  
Figure 3. Different Shower Monitoring and Feedback Designs Corresponding to Different Experimental Conditions.

The four designs were evaluated in a six-month randomized controlled field experiment at a hotel in Germany. Forty hotel rooms were equipped with smart shower meters that collected data on shower usage by guests (water volume, temperature, and flow rate of each shower). Water use and temperature were combined to obtain the measure for the dependent variable of energy consumption. Guests were informed about the study when they checked in to the hotel and were asked to fill out a short survey on their experience with the shower meter at checkout.

The results surprised the researchers. As predicted, the first two treatment conditions resulted in statistically significant reductions in energy usage relative to the control group; however, the instantiation expected to have the strongest conservation effect yielded results opposite to that hypothesized, such that “enabling the polar bear seems to increase energy consumption by 6.8%” (Ableitner et al., 2017, p. 9).

The authors offer several potential explanations for this effect, including curiosity, puzzlement, or even resistance to such explicit pressure to conserve the environment. The researchers conclude that seemingly “small” and mundane design choices might have dramatic consequences, especially when implemented in the real world (Ableitner et al., 2017) and caution that neglecting such factors may result in design features being treated “superficially, without paying attention to the complexity of the issues at hand, and without a deep understanding of the mechanisms and interdependencies at work. What may seem like a harmless tweak to the user interface may have dramatic consequences on public acceptance or cost-benefit ratio” (Tiefenbeck, 2017, p. 2).

In Case 2, many local decisions were made that could not be derived from the reference theories, which stated nothing about water, energy, showers, temperature, liters, showering, European Energy classification codes, climate change, ice floes, melting ice, or polar bears. Yet the researchers had to make such decisions to implement the theory of the impact of feedback on behavior in the real world. It is remarkable that what the authors hypothesized would be the strongest way to implement the design ended up producing the opposite effect. It is quite reasonable to posit that a practitioner might make a similar choice, only to eventually discover that the investment made (e.g., production, marketing, sales) was actually counterproductive. Case 2 provides a vivid account of the potential real-world consequences of DTI. Furthermore, it is notable that it was a field experiment implementing a theory in a real-world setting that uncovered the possibility that some instantiations may produce contrary-to-expected effects. We mention these issues for the analysis of DTI below.

## 4 Understanding the Nature of Design Theory Indeterminacy

As these two cases show, design theory indeterminacy arises when practitioners seek to implement design theories. Indeed, ambiguity may arise at multiple points when practitioners attempt to implement an IT artifact using a design theory to solve a real-world problem. DTI is thus not only an issue of IT artifact development, but also one of deployment. Therefore, we propose that DTI is composed of dimensions of indeterminacy present during development and deployment of the IT artifact.

## 4.1 DTI During IT Artifact Development

## 4.1.1 Dimension 1.1 (Focal Features): From Design Principles to Focal Features

Cases 1 and 2 illustrate that major uncertainty might arise when a practitioner applies a design theory by implementing its design principles (see Section 2). These principles provide guidance on the form and function of the IT artifact to be created (Gregor & Jones, 2007; Walls et al., 1992). Thus, the design of the IT artifact involves interpreting and converting design principles of the theory into artifact features. For example, the principle of collecting information “in terms of attributes” (in Case 1) could be manifested by an IT artifact feature of an autocomplete textbox implemented using HTML tags, XML, JavaScript and appropriate data structures, and SQL queries (e.g., using an MS SQL Server database management system) to support real-time term retrieval for the autocomplete textbox. We term the features designed specifically to instantiate design principles of a design theory focal features.

In this context, DTI is caused by multiple factors. First, vague, abstract, and non-design-specific language of a theory (see also Chandra Kruse et al., 2016) hampers the ability of practitioners to understand what focal features to develop. For example, it may not be clear to a practitioner what “instances” are <sup>3</sup> and how they should be represented in terms of focal features.

Cases 1 and 2 show that instantiating abstract design principles requires making implementation decisions that cannot be determined from the principles alone. Additional knowledge must be brought to bear by a practitioner to complete the project. In the Appendix, we provide a detailed analysis to show that in realworld development following a design theory, the design of focal features involves a series of transformations of the design principles, in which each iteration necessitates using additional knowledge (from outside of the design theory).

The mapping between design principles and focal features is not 1:1, as there might be many ways to instantiate a principle (e.g., collecting information “in terms of attributes” in Case 1), each leading to different outcomes—a concept known as multifinality (Kruglanski et al., 2013; Prat et al., 2015).

As there might be many ways of manifesting an abstract principle and no specific guidance on how to select the best design choices, the question arises whether and to what extent outcomes are contingent on specific focal features. In some cases, the eventual design might produce the predicted outcome, but in others, it might not. Table 2 uses Case 2 to illustrate that converting the same design principle into focal features in multiple ways—all assumed to be consistent with the principle—resulted in different outcomes

Another issue experienced by practitioners when instantiating an artifact is uncertainty about how to combine the multiple principles in a design theory (e.g., all examples given in Table 1, Section 2). As Case 1 shows, different design principles call for changes to similar or related focal features of the artifact (i.e., data collection interface, data structures, form elements, and controls). However, the design theory itself does not consider how these resulting focal features are related. This creates uncertainty about how to integrate the normative guidance from the theory that affects similar and related features.

Design principles may be orthogonal—meaning that the focal features derived from one principle do not interact with any focal features derived from another. Alternatively, design principles might be oblique—in this case, design features derived from one design principle might interact with design features derived from another one. Therefore, instantiating multiple principles, each of which may be operationalized in several ways via different focal features, might involve high levels of complexity, and instantiation of one principle could interfere with another. Such interactions may either strengthen or weaken effects on outcomes of interest.

Table 2. Multiple Focal Features and Outcomes in Case 2 Based on the Same Design Principle

<table><tr><td>Design Principle</td><td>Focal features*</td><td>Outcome(lower energy consumption)</td></tr><tr><td>Direct feedback on energy consumption</td><td>1. Litres2. Litres + Energy Efficiency Class3. Litres + EEC + Melting ice and polar bear</td><td>1. Supported2. Supported3. Not supported</td></tr><tr><td colspan="3">Note: * The control group from Case 2 is not shown, as it did not provide feedback on energy consumption.</td></tr></table>

For example, in Case 1, the two principles stipulating that instances should be described using (1) attributes and (2) classes are likely to be oblique; that is, a decision to collect classes using traditional HTML tags (e.g., a drop-down list, as done frequently) might bias the decision to also collect attributes (another design principle) using traditional HTML tags (e.g., checkboxes), which could limit the variety of attributes users provide. Indeed, focusing on one principle at a time(e.g., attributes) might alert the practitioner to an assumption of the design theory of relaxing data collection. This could suggest more radical modes of data collection (e.g., via voice commands) capable of supporting greater variability in the attributes reported.

Thus, a challenge is providing effective support and guidance for practitioners to instantiate design principles into appropriate focal features such that the predicted outcomes occur. Accordingly, we propose Dimension 1.1 (focal features) of DTI as indeterminacy when designing focal features based on design principles of the design theory.

## 4.1.2 Dimension 1.2 (Auxiliary Features)

The next observation extracted from the cases is that the IT artifact contains features that do not relate to any design principles or other components of the design theory. The need to make IT artifacts work requires the practitioner to develop features that relate to requirements other than the design principles or other components of the design theory. We term these auxiliary features. These features are commonly needed to ensure good design (Baskerville, Kaul, & Storey, 2018), provide generally expected functionality or physical infrastructure, or comply with legal, cultural, or ethical norms (assuming these are beyond the scope of a given theory).

In Case 1, such features include the images of animals and plants shared, the registration system, and pages such as the Contact Us, About Us, legal disclaimer, and project description pages. Because these features are not part of the design theory, they may interact with the focal features in ways that cannot be predicted by the theory. For example, potential contributors might be dissuaded from engaging with the project in Case 1 simply because they do not trust the researchers listed as project leaders on the About Us page (the page being a bundle of auxiliary features). In Case 2, auxiliary features include the fonts, colors, screen resolution, and material used in the shower display.

It is possible that, even when all focal features are properly instantiated, the presence of auxiliary features mitigates or even reverses the “desired” effects stipulated by the design theory. Lukyanenko et al. (2015, 2014) view this as a threat to instantiation validity; that is, ensuring that an artifact designed to instantiate a theory (e.g., for the purpose of behavioral theory testing or development of an IT artifact based on a design theory) not only faithfully operationalizes the focal theory but is also free of confounds resulting from the presence of additional features necessary to make the artifact work. Accordingly, we propose Dimension 1.2 (auxiliary features) of DTI as indeterminacy when designing auxiliary features to ensure the attainment of the target outcome.

## 4.1.3 Dimension 1.3 (Emergent Features)

As discussed before, an IT artifact is a complex and open system. This implies that it may not be reducible to the sum of its focal and auxiliary features. Instead, it may have emergent features—elements of form and behavior that emerge from the complex interaction between its focal and auxiliary features (Prat, Comyn-Wattiau, & Akoka, 2014). Following Prat et al. (2014), we argue that DSR research should consider both individual IT features and the IT artifact as a whole.

For example, presentation complexity and information overload are emergent features of the way information is presented to a user. Unless emergent features are part of the design theory, they may lead to unpredicted (by the theory) outcomes. For example, the presence of many unique attributes in the display of sightings in Case 1 (i.e., after sightings are posted by users and become visible to the entire user community) might create an emergent feature of “information overload” —a feature that does not have a corresponding design principle in the respective design theory and which might negatively affect the expected outcomes. In Case 2, it is possible that it was not the polar bear per se, but rather the multiplicity of all the focal features used (i.e., display of the liters of water used, conservation rating, the polar bear drowning) that created an emergent feature of “pressure to conserve” that some people resisted.

The complexity of IT artifacts manifested through the interaction of different features needed for a real-world software to work means that emergent features are likely to be the norm rather than an exception in most real-world development projects. Consequently, we propose Dimension 1.3 (emergent features) of DTI as indeterminacy in ensuring any emergent features of the artifact accord with the design theory and do not prevent the attainment of the target outcome(s).

## 4.2 DTI During Artifact Deployment

Once an artifact is developed, a practitioner faces other DTI-related challenges in deploying it in a manner that attains the desired outcomes. This involves ensuring proper execution of causal mechanisms and measuring the change in the environment corresponding to the dependent variable of the design theory to test the hypotheses of the theory.

## 4.2.1 Dimension 2.1 (Causality): From Artifact to Outcome

A key challenge related to causality lies in the open nature of IT systems in DSR (Chaturvedi et al., 2011; Prat et al., 2015). It is unrealistic to deduce universal, law-like, context-free causes in DSR; rather, causes are a constellation of temporally and contextually bound probabilities (Gregor & Hovorka, 2011). When practitioners decide to implement a design theory, they are likely doing so in a different context from the one envisioned or experienced by the researcher (Lee, 1989). This instantiation in a new environment might alter the causal chains in unpredictable ways. As Germonprez et al. (2011) note, “people reflect and act with systems in unexpected ways to support local practices and address situated needs and issues, thereby challenging designers’ preexisting expectations” (p. 665).

In addition, design theories typically do not specify the full causal chains linking the artifact to the outcomes. They routinely omit potentially pertinent moderator and mediator constructs and their interrelationships (e.g., when a mediator is moderated by another variable, see Tams, Legoux, & Leger, 2018). A moderating construct is a construct that influences the direction or magnitude of the relationship between the antecedent and outcome constructs. For example, in Case 1, domain expertise (the moderator) may suppress the impact of flexible design on information quality (i.e., domain experts, unlike novices, may be able to navigate more restrictive interfaces predicated on more specific categories and record information with greater accuracy). Likewise, a citizen science system such as that developed in Case 1 might not result in greater user participation if practitioners develop it only for a particular type of domain, such as birds, since this domain has a very popular incumbent platform (eBird.org), making it difficult for any new type of birding app to succeed (another example is Google’s failure to penetrate the social networking market with Google+ due, in part, to the existence of highly successful incumbents<sup>4</sup>). This is a DTI case of an unspecified moderating factor (i.e., presence of incumbent alternatives) that might be relevant for some projects. Thus, its omission from the design theory might jeopardize such projects.

A mediating construct, on the other hand, is one that is assumed to be located between the antecedent and outcome constructs. In Case 2, many mediators stand between the artifact and the outcome: the display itself (the artifact) does not directly cause reduced energy consumption. The display has to be attended and perceived by a person (which involves attention and perceptive mechanisms of humans) and then evaluated (i.e., the information on the display needs to be understood and related to the states of reality desired by the person taking the shower). This might result in a (potentially delayed) intention and, finally, an action to reduce water use. Various psychological mechanisms could interact with this long and complex causal chain, which might at least partially explain the polar bear effect. Yet a design theory typically does not specify every single process involved in shaping the outcome triggered by the artifact.

In sum, to increase the likelihood of a desired outcome following the instantiation of a design theory in an artifact, the causal chains connecting the artifact to the outcomes in the deployment setting need to be wellunderstood and managed. Lack of guidance on how to do this creates ambiguity and uncertainty in practice. Accordingly, we propose Dimension 2.1 (causality) of DTI as indeterminacy when deploying the artifact in the specific real-world context to ensure that the target outcomes are attained.

## 4.2.2 Dimension 2.2 (Measurement): From Outcomes to Conclusions

Design science research projects are triggered by a real-world problem or a concrete need (Hevner & Chatterjee, 2010; Hevner et al., 2004; vom Brocke et al., 2020). At the end of the project, the key question therefore is: has the intervention (using the IT artifact) succeeded in resolving the original problem? Even if all the proper steps are taken during the development of the artifact, a negative response may be caused by an error in measurements. A typical design theory does not concern itself with the problem of measurement (consider the components of a design theory in Section 2).

Consequently, especially if the design theory contains new theoretical constructs, practitioners may have very little guidance about how to measure outcomes in a specific situation. In most cases, a design theory is instantiated by the researcher only once and typically in a laboratory setting (Prat et al., 2015). Moreover, DSR lacks the practice of sharing measurement instruments and making them publicly available for practitioners. As a result, a practitioner might reach incorrect conclusions following the deployment of the artifact design based on the design theory. Accordingly, we define Dimension 2.2 (measurement) of DTI as indeterminacy in ensuring that the outcomes attained are properly measured and valid conclusions are reached.

Table 3. Dimensions of Design Theory Indeterminacy

<table><tr><td>Stage</td><td>DTI dimension</td><td>Definition</td></tr><tr><td rowspan="3">Artifact development</td><td>1.1 Focal features</td><td>Indeterminacy when designing focal features based on design principles of the design theory.</td></tr><tr><td>1.2 Auxiliary features</td><td>Indeterminacy when designing auxiliary features to ensure the target outcomes are attained.</td></tr><tr><td>1.3 Emergent features</td><td>Indeterminacy in ensuring any emergent features of the artifact accord with the design theory and ensure the target outcomes are attained.</td></tr><tr><td rowspan="2">Artifact deployment</td><td>2.1 Causality</td><td>Indeterminacy when deploying the artifact in the specific real-world context to ensure that the target outcomes are attained.</td></tr><tr><td>2.2 Measurement</td><td>Indeterminacy in ensuring that the outcomes attained are properly measured and valid conclusions are reached.</td></tr></table>

## 4.3 Discussion

DTI is a multidimensional problem. These dimensions (summarized in Table 3) show that we do not conceptualize DTI as merely a challenge of translating design principles. Rather, it involves uncertainties related to additional features of the artifact, the interaction of features in an artifact, specification of causality, and measurement.

Furthermore, focal features are perhaps the only elements of deployment and design in direct purview of design theories through the component of design theories commonly known as design principles. Many other design and deployment choices faced by practitioners (e.g., auxiliary features) are not directly shaped by the components of design theories, and additional knowledge is necessary to develop an artifact. Consequently, the analysis of DTI suggests a reconceptualization of design theories from forms of knowledge that prescribe design and action (i.e., the concept of technological rationality, when scientific knowledge is transferred to practice in a direct and straightforward way—see Bunge, 1967) to, at least in some cases, forms of knowledge that inspire, support, or assist practitioners in design and action by providing important albeit incomplete guidance (as discussed in the Appendix).

## 5 Tackling the Problem of Design Theory Indeterminacy

What can researchers do to better support practitioners in utilizing the knowledge produced by the DSR community? We propose specific areas for future research according to the DTI dimensions described in Section 4. We begin by proposing three general directions, applicable at all stages of development and deployment, and then focus on each stage.

## 5.1 General Research Directions

Three research directions—involving clarity of design principles, transparency of DSR, and disciplined imagination by researchers—are applicable to both development and deployment stages and are capable of lessening DTI across all dimensions.

## 5.1.1 Clarity and Consistency of Design Theory Components

Researchers need to ensure that the components of a design theory, such as design principles or constructs, are formulated in clear, unambiguous, accessible language and are free of inconsistencies and contradictions. The potential for misunderstanding by practitioners is quite real. As design theory is produced in the context of research, its language may contain theoretical notions and specialized vocabulary or jargon, which may be understood by scientists but not by practitioners. As Hovorka (2019, p. 1358) warns: “When academics speak only to each other and then only in abstract formalisms and esoteric jargon, it is little wonder that companies, policymakers, and individuals are unable to see the relevance of academic research.” Naturally, abstract formalisms and esoteric jargon make it challenging to apply research, even when it is perceived by practitioners to be relevant to the problem at hand.

Chandra Kruse and colleagues (Chandra Kruse & Seidel, 2017; Chandra Kruse et al., 2016; Chandra, Seidel, & Gregor, 2015) studied this problem in the context of design principle reuse and demonstrated the challenge arising when implementing design principles into (in our terminology, focal) features. Consistent with our claims, they found that other researchers and practitioners might struggle to understand and therefore instantiate design principles in an artifact. They argued that principles should be communicated clearly and explicitly. Consistent with this argument, we call for research on ways to improve the clarity of design principles, but also extend this call to other theory components. For example, in Case 1 such theoretical constructs as “instance,” “attribute,” and “class” used in the design theory should be clearly explained in an accessible language, as these are specialized terms derived from philosophy that might not be part of the typical work of the developers. In Case 2, more details could be provided on the dependent variable (energy consumption), especially in terms of whether the outcome is time contingent.

Obtaining the results predicted by a design theory is unlikely if the practitioner misunderstands any or all its components and therefore implements the wrong artifact or deploys it in a manner incongruent with the theory. The clarifications and explanations can be provided in an appendix or in supplementary materials if a researcher wishes to retain the original scientifically focused style. Broadly, we propose:

Research Direction 1.1: Determine how to better formulate components of the design theory (e.g., design principles, constructs) to increase their clarity and accessibility for practitioners.

## 5.1.2 Transparency and Artifact Sharing

Software design is a complex process, involving many design decisions beyond development of focal features. Much design knowledge is tacit and, therefore, difficult to communicate explicitly (Gregor, Müller, & Seidel, 2013; Schön, 1983). As a result, in addition to design theories, DSR recognizes other forms of knowledge contribution, such as models, methods, instantiations, and meta-artifacts (see Drechsler & Hevner, 2018). Notably, Gregor and Jones (2007) view an expository instantiation as a component of design theory. Consistent with that perspective, we argue for greater transparency in design theorizing, including the use of different forms of knowledge, and we encourage not only the development of artifacts for exposition and evaluation but proactive artifact sharing.

Design science researchers have broadly embraced the concept of process transparency, especially during artifact evaluation (Gleasure, Feller, & O’Flaherty, 2012; Prat et al., 2015; vom Brocke et al., 2020). This idea can also be applied to mitigating DTI. The reporting paper should include a detailed description of the IS artifact, carefully showing how the features based on the design theory were developed. To the extent possible, the artifact should be shared with the research and practitioner community. Providing the actual functioning artifact or its components communicates design knowledge beyond what can be explicated in a traditional research paper. This facilitates the application of design theories by practitioners.

Authors should also avail themselves of different presentation modes made available by the publisher. We also encourage journals and conferences to explore novel formats for publishing DSR, such as allowing the artifact to be shared or demonstrated (as is frequently done in DSR-oriented conferences). Thirdparty platforms, such as GitHub.com, provide free space and sophisticated tools for artifact sharing and reuse (Negoita et al., 2019).

In addition to sharing the artifact, researchers should describe and, if possible, archive the implementation environment used when performing the study. Researchers should also provide details on the development process, such as the development team, notable milestones in the development, and challenges faced when instantiating a design theory. Practitioners would benefit from more detailed description by researchers of the setting in which an instantiation of a proposed design theory occurred.

Artifacts could also be systematically curated into libraries. This could include detailed documentation on how features of the artifacts were developed based on respective design theories, complete with the results of any evaluation of the artifacts. Artifact curation is an accepted practice in reference disciplines. For example, The International Affective Picture System (IAPS) is a database of standardized pictures that has been widely used in psychology, computer science, and software engineering research (Lan et al., 2014; Lang & Bradley, 2007). Snodgrass and Vanderwart (1980) developed a widely used battery of 260 pictures (black-and-white line drawings) standardized on key variables of relevance to experimentation in visual perception, language, and memory, stating the following as motivation (p. 174):

Because there are so many different ways to draw even the simplest object, each investigator has been forced to develop his or her own set of pictures that must necessarily be highly idiosyncratic. We cannot assume that the results of studies employing such different representations of the same concepts are comparable. In addition, the degree to which each picture possesses characteristics that affect the process under investigation is unknown.

Consistent with Snodgrass and Vanderwart (1980), artifact sharing can lessen DTI arising from focal, auxiliary, and emergent features.

Practitioner-oriented artifact libraries are widespread, including such examples as GitHub.com (library of programming code and other software components), RegExLib.com (library of regular expressions), and WordPress.com (library of website templates). The prolific use of APIs—application programming interfaces, such as GoogleMaps or JQuery—is another example of artifact sharing widely used in IT practice (Jacobson, Brail, & Woods, 2011). Despite the commonsense nature of these ideas, DSR and the IS discipline broadly does not have established practices for sharing and curating artifacts or meticulously describing implementation settings. We thus suggest:

Research Direction 1.2: Develop best practices and supporting infrastructure for increasing artifact sharing and process transparency in research.

## 5.1.3 Disciplined Imagination and Deliberate Diversity

Another way to lessen DTI across all dimensions is to explore the use of disciplined imagination and deliberate diversity. While scientists typically develop a single artifact for evaluation and exposition and typically do so in laboratory settings (Prat et al., 2015), this should not preclude them from envisioning other possibilities. We encourage researchers to engage in thinking that, to the extent possible, simulates a broad range of authentic development possibilities. The concept of disciplined imagination was proposed by Weick (1989, 1995) as a method of increasing the “usefulness” (i.e., relevance) of scientific theories. According to Weick (1989), disciplined imagination should be central to any theorizing and involves “consistent application of selection criteria to trial-anderror thinking” (i.e., the disciplined part) and “deliberate diversity introduced into problem statements, thought trials, and selection criteria that comprise that thinking” (i.e., the imagination part; p. 516, emphasis added).

The notion of deliberate diversity holds promise for dealing with less understood dimensions of DTI, namely auxiliary and emergent features, as well as the dimensions of causality and measurement. Through deliberative diversity, researchers can anticipate the types of challenges faced by practitioners. We suggest that researchers consider a variety of ways in which a design theory can be instantiated and deployed by practitioners. Which are the realistic scenarios where a design theory will be useful? What kind of constraints or challenges could practitioners face in such scenarios? What kind of features would they like to implement in addition to those needed to instantiate design principles within the design theory? What specific deployment challenges may arise? What types of internal interferences could occur? How can the outcomes be measured most effectively?

## Consequently, we suggest:

Research Direction 1.3: Investigate ways of using disciplined imagination and deliberate diversity to lessen DTI across all its dimensions.

## 5.2 DTI During Artifact Development

A major DTI challenge facing practitioners is how to implement each design principle into focal features; that is, the concrete elements of an IT artifact (e.g., code, interface, supporting infrastructure). The problem of moving from principles to features has received some attention within the DSR community as well as in related disciplines; these form the basis for the research directions proposed below.

## 5.2.1 Narrowing of Design Theories

A core challenge of moving from principles to focal features is establishing how a particular feature is developed or chosen from abstract prescriptive statements. Even outside the scope of DTI, DSR faces challenges in tracing the link from (abstract) justificatory knowledge from kernel theories to meta-requirements for an artifact or design principles for a design theory (Goldkuhl, 2004; Walls et al., 2004). In this context, scholars have argued for the need to develop intermediate, more narrowly scoped forms of justificatory knowledge (Arazy et al., 2010; Kuechler & Vaishnavi, 2012).

In a similar vein, Chandra Kruse et al. (2016) reflected on the difficulties of reusing design principles, posing the following question: “‘What exactly is enough’ specification within a design principle?” (p. 48). As many design theories are midrange (Kuechler & Vaishnavi, 2008, 2012; Moody, Iacob, & Amrit, 2010; Weber, 2012) or moderately abstract, an open question is whether to consider narrowing their scope. This means researchers can mitigate DTI by formulating design theories expressed in a more design-like language, rather than a theoretical and abstract one. For example, instead of arguing that, to “to increase recommender system adoption, use anthropomorphic design,” a theory might state, “to increase recommender system adoption, design avatars based on 3D digitalization of real people complete with human voiceover and gesticulation-derived rehearsed movements of real people.” Greater specificity and the use of more actionable design-oriented language might help practitioners narrow the design search.

Narrowing the scope of design theories, however, could interfere with other objectives typically pursued by researchers, such as the search for generality and parsimony and the use of theoretical language more familiar to researchers. The more narrow and designspecific a theory, the more difficult it is to integrate it with other scientific knowledge expressed in general terms or to argue for its generalizability to a broader class of problems (Baskerville et al., 2018; Li, Larsen, & Abbasi, 2016; Venable, 2013). Thus, we propose:

Research Direction 2.1: Determine how to better support translation from design principles or propositions to focal features while balancing the needs of practitioners and the scientific community.

## 5.2.2 Transformation Rules

A fruitful avenue for supporting the conversion between design propositions and focal features is the specification of transformation rules—principles for consistent and appropriate conversions. In linguistics, Chomsky (1995) proposed using transformation rules to convert deep structure (meaning) into surface structures (form), such that the core meaning is preserved but the forms are altered to better suit the situation (e.g., adding passive voice or an inflection). The need for these kinds of transformation rules has also been considered in the philosophy of technology. For example, Feibleman (1972) proposed espousing special theories that convert theoretical abstractions into technological rules, arguing that intermediate steps are “necessary for getting from theory to practice” (p. 36).

Notably, transformation rules are already used in DSR. For example, in the domain of systems analysis and design, researchers have proposed transformations from conceptual modeling grammars to logical data models (Teorey, Yang, & Fry, 1986), rules for reverse engineering from logical to conceptual models (Chiang, Barron, & Storey, 1994), and heuristics for translating the proposed abstract design principles into more actionable procedures (Castellanos et al., 2020). Transformation rules can be incorporated in design science theorizing to show how or under what principles concrete physical objects (e.g., HTML tags, CSS styles, or server-side scripts) are derived from abstract propositions and can become integral elements of “principles of implementation” (Gregor & Jones, 2007) of design theories. Accordingly, we propose:

Research Direction 2.2: Determine how to use transformation rules to supplement design theory, including how they should be derived from a design theory and how they should be presented in a form accessible to practitioners.

## 5.2.3 Managing Design Principle Obliqueness

An overlooked issue in design science research is the potential for conflicts between design principles. Earlier, we defined two types of design principles: orthogonal and oblique. More research is needed on detecting and mitigating the effects of oblique design principles, where the implementation of one principle affects the implementation of another. For example, the first design principle might set a certain frame of reference or frame of mind for the practitioner. As Baskerville et al. (2019) argue, design theories constrain solution spaces. Thus, starting with a given design principle within design theories might set a designer on a course that affects the subsequent implementation choices for other design principles.

Guidance for improving the understanding and management of design principle obliqueness can be drawn from psychology, where priming, anchoring, and other biases are studied. First, design science researchers need to increase their awareness of these issues. For example, priming is an influence of some stimuli (i.e., a design principle and its process of instantiation) on subsequent behavior (i.e., instantiation of another principle by the practitioner). Priming can occur unconsciously (Goldwater et al., 2011; Tulving, Schacter, & Stark, 1982), so practitioners might not realize that their actions pertaining to one principle are influenced by prior exposure to another principle. Anchoring and adjustment research in psychology shows that exposure to an initial condition (an anchor) affects subsequent decisions (Tversky et al., 1990).

Extrapolating this to the DSR domain, the implementation of one design principle might constitute an anchor, resulting in subsequent design principles being interpreted and implemented in the same manner (e.g., if a neural network learning algorithm is chosen to implement the first design principle, a practitioner might decide to use it for the second principle, even though another algorithm might be more appropriate for the second principle). Indeed, such effects have been documented in IS design work—for example, in the context of database analysts reusing SQL queries (Allen & Parsons, 2010). We encourage design science researchers to consider this issue and caution practitioners in situations in which design principle obliqueness could lead to negative consequences. We therefore suggest the following broad research direction:

Research Direction 2.3: Determine how to detect and anticipate design principle conflicts and how to support practitioners in dealing with this issue.

## 5.3 DTI During Deployment: From Artifact to Outcomes

Once an artifact is developed from a design theory, practitioners deploy it and then observe and measure outcomes. A key challenge at this stage is the lack of complete guidance from the design theory on the nature of causal chains that link the artifact and outcomes and on how to detect and measure the outcomes.

## 5.3.1 Specification of Causality

To ensure the desired outcomes are achieved, both researchers and practitioners need to be aware of the mechanisms that connect the artifact to outcomes in the environment. Failure to realize the desired outcomes might be due to the absence of, or interference with, these causal mechanisms.

The explanation of cause and effect is a component of design theories, yet little research has been done on developing ways to better explain causality to practitioners. This is partly because causality has been a neglected component of theorizing in DSR (Gregor & Hovorka, 2011). Gregor and Hovorka aptly labeled it “an elephant in the room” and called for more research on the nature of causality in design science.

Some DSR researchers offer guidance on dealing with causality, including the notions of affordances and recognizable patterns (Germonprez et al., 2011; Gregor & Hovorka, 2011). Broadly, these approaches deal with the analysis of user actions that are enabled or constrained as a result of the presence or absence of design features. To illustrate, consider affordances— perceived design features of IT artifacts that match human abilities and thus support action (Leonardi, 2011; Norman, 1999; Vaast et al., 2017). The analysis of affordances that should be present if design principles are appropriately realized as features suggests a range of action possibilities stemming from design features and human abilities that can enable certain types of interactions.

The concept of secondary design—when IT artifacts are only partially developed by the organization and intentionally leave some components open for development by the users—also grapples with the issue of ensuring that the final product acts as expected (Germonprez et al., 2011). Among the solutions proposed is the use of recognizable conventions, or familiar use patterns, from existing technologies, which do not require specialized knowledge and thus interact in predictable ways. Indeed, there is some prior research on recognizable conventions that would be useful for design science researchers (e.g., Moody, 2009; Norman, 2002).

Persuasive design, digital nudging, choice architecture, and behavioral design are overlapping areas that investigate how to influence human behavior through design features (Johnson et al., 2012; Lockton, Harrison, & Stanton, 2010; Weinmann, Schneider, & vom Brocke, 2016). We call for more research in these areas and encourage design science research to develop best practices (including ethical practices, see Sunstein, 2016) for taking advantage of action enabling and constraining features to better understand the causal mechanisms connecting design theories to outcomes. Thus, we propose:

Research Direction 3.1: Determine how to better specify causal mechanisms of a design theory to help reduce DTI.

## 5.3.2 Specification of Measurement

Typically, design theories do not specify how practitioners measure or detect change in a way consistent with the theory. Practitioners may convert design propositions into IT artifact features appropriately but nevertheless fail to achieve the desired outcome because of faulty measurement. Measurements are commonly subject to error, which can be systematic (due to flawed design or execution, such as observer bias) or random (due to natural variation in the thing being measured or the instrument) (Bunge, 1996; Kerlinger & Lee, 2000). To ensure effective measurement of outcomes from the implementation of a design theory, practitioners need to be aware of and capable of mitigating both types of errors.

Ensuring proper measurement can be onerous. While we encourage practitioners to become more familiar with measurement methods, there is room to better support practice in this area. First, design scientists should ensure that they provide detailed and comprehensive information about how they performed their own measurements when they instantiated the artifact based on the design theory, which would also include the sharing of measurement instruments. This would help practitioners facing nearly identical scenarios in instantiating a design theory who would therefore be interested in reusing the measurement protocols and measurement instrument (if one is available). In other words, we reiterate earlier calls for greater procedural transparency in DSR and emphasize the importance of sharing the elements of DSR projects—in this case, instruments for measuring the outcomes.

Second, as practitioners might use a design theory in a context different from that of the original research study (e.g., applying the principles from Case 2 in residential homes rather than hotel rooms), researchers should consider several (rather than one, as commonly done) ways of measuring the outcomes. In Case 2, if the application context is residential homes, then the outcomes will likely differ from that of hotel rooms. Unlike hotels, where people stay for a short period, residential homes use energy continuously and typically report usage in fixed intervals. As this is a likely scenario for the application of the design theory in Case 2, researchers could consider this scenario (using disciplined imagination) and suggest appropriate measurement approaches.

In general, we encourage researchers to specify the outcomes of a design theory more precisely. In particular, we view the under-specification of the temporal bounds of the outcomes as a common issue afflicting DSR. For example, in Case 1, it is unclear whether the effect caused by the introduction of the new principles will wane over time. However, this could be reasonably posited, given that typing attributes is more time-consuming than selecting from predefined choices. Unless there is an incentive for users to continue providing attributes, they might provide fewer and fewer attributes over time, which could even result in the reversal of the predicted outcome of greater user participation.

Case 2 offers an even stronger hint that underspecified temporality may influence the interpretations of the outcome. If surprise and novelty were confounded in the “polar bear” condition, we can conjecture that these attenuating effects would dissipate over time (as surprise and novelty dissipate).

Thus, if energy consumption were to be measured over longer periods (which was understandably difficult to do in Case 2, due to guest churn at hotels), that condition might have outperformed all others. Indeed, this is exactly what a more recent study by Tiefenbeck et al. (2018) found. When administrated to Swiss households in a longer-term usage context, the “polar bear” condition resulted in significant energy conservation compared with the control group.

Considering these issues, we suggest this broad direction for future studies:

Research Direction 3.2: Determine how to better specify measurement methods and encourage sharing of measurement instruments to help reduce DTI.

Table 4 summarizes the research directions and shows which dimensions of DTI they seek to address.

Table 4. Research Directions and the Target Dimensions Of DTI

<table><tr><td>Research Direction</td><td>Dimension(s) of DTI targeted</td></tr><tr><td>1.1 Clarity, consistency, unambiguity of design components1.2 Transparency of DSR process and artifact sharing1.3 Disciplined imagination and deliberate diversity</td><td>All DTI dimensions</td></tr><tr><td>2.1 Narrowing of design theories</td><td rowspan="3">Dimension 1.1 (Focal features)</td></tr><tr><td>2.2 Transformation rules</td></tr><tr><td>2.3 Managing design principle obliqueness</td></tr><tr><td>3.1 Specification of causality</td><td>Dimension 2.1 (Causality)</td></tr><tr><td>3.2 Specification of measurement</td><td>Dimension 2.2 (Measurement)</td></tr></table>

## 6 Conclusions

Concerns about the extent to which IS research is supporting practice continue to be raised (Hirschheim, 2019; Hovorka et al., 2019). One way to increase the relevance of IS research is by codifying design knowledge into design theories. Compared to theories of explanation and prediction (Gregor, 2006), design theories offer greater guidance for practice in creating IT artifacts to achieve particular goals (Gregor & Jones, 2007; Venable, 2013). Through the lens of design theory indeterminacy, we seek to stimulate new thinking about how our discipline can become more practically relevant.

Our paper sheds new light on the complex relationship between information systems research and practice. The dominant perspective of technical rationality, rooted in the philosophical doctrine of positivism, considers practice as the application of scientific knowledge to concrete problems of everyday life (Dasgupta, 1996; Mitcham, 1994; Schön, 1983, 1987). Applied sciences such as IS aim to produce grounded rules that establish “stable norms of successful human behavior” (Bunge, 1967). However, many documented cases of software engineering appear to be devoid of explicit theoretical guidance (Dasgupta, 1996). Furthermore, there is ample evidence of the power of small effects (Kohavi & Thomke, 2017; Tiefenbeck, 2017), the difficulty of fully anticipating how an artifact is going to be used by people (Germonprez et al., 2011), the full impact it may have (Gregor &

Hovorka, 2011), and the struggles practitioners face when trying to use DSR knowledge (Chandra Kruse et al., 2016). We observed the same issues in our two cases of exemplary DSR.

A key question that emerges is how to undertake design theorizing in a way that maximizes the practical utility of IS theories. Despite the intuitive importance of this question, it has received scant attention from the research community. In this paper, we examine the issue of design theory indeterminacy in three ways. First, we present empirical evidence from two cases of real design theories in which we show that many specific design choices cannot be derived from the theory. Second, we develop a conceptual foundation of DTI that reveals the nature of indeterminacy as a complex, multidimensional problem, not simply an issue of developing (focal) features based on design principles but also concerning the entire artifact design as well as its deployment. Finally, we propose directions for research to lessen the design indeterminacy problem across its dimensions.

While there are outstanding issues for which future research is needed, much of what we have proposed can already be used by scientists—for example, ideas about clarity, consistency, and accessibility of the language of design theories, increased transparency of DSR, including sharing of the artifacts, as well as deliberate and disciplined imagination of how the proposed theories might be used in practice. We urge researchers to work more closely with practitioners, become more aware of practitioner challenges, be more transparent and critical about design theories, and seek ways to make the academia-industry interaction more fruitful and effective.

While we positioned DTI as something to be reduced, we also note possible benefits resulting from the uncertainty of design theories. Generality is important as it helps promote creativity and technological innovation (because specific forms are not insisted upon and practitioners have more freedom to interpret the theories in their own ways to develop creative solutions using new technological forms) (Baskerville et al., 2019; Chandra Kruse et al., 2016). Thus, in an ideal case, design theories could retain their generality, while also providing clear and reliable guidance for practitioners, for example, through additional forms of knowledge (e.g., transformation rules and other knowledge contributions of DSR—vom Brocke et al., 2020)

We also call for further research on DTI. More recommendations akin to those developed here could be proposed. Future work could also draw on other disciplines (e.g., engineering, architecture, medicine, law or even art) in which similar issues are present. Insights from these fields might produce new guidelines or help refine existing ones.

Design science research is fundamentally a problemsolving endeavor. While it seeks to solve real-world problems with innovative artifacts, it could also benefit from looking inward and seeking to address DTI in a way that makes this valuable stream of information systems research even more impactful.

## Acknowledgments

We thank the senior editor and the review team for the valuable feedback and guidance that substantially improved this manuscript. We are also very grateful to Verena Tiefenbeck, who kindly provided additional information and supporting materials for Case 2, to Kai Larsen, who offered advice on the nature of the relationship between DTI and the concepts of reliability and validity, to Stefan Seidel for sharing his views on how to make design theory more practically relevant, and to the DESRIST and SIGSAND communities for their feedback on earlier versions of this research. This research was supported by grants from the Natural Sciences and Engineering Research Council of Canada, the Social Sciences and Humanities Research Council of Canada, and L’institut de valorisation des données (IVADO Canada). Finally, we wish to thank the anonymous contributors of sightings to the NL Nature citizen science project.

## References

Ableitner, L., Tiefenbeck, V., Hosseini, S., Schöb, S., Fridgen, G., & Staake, T. (2017). Real-world impact of information systems: The effect of seemingly small design choices. Paper presented at the Workshop on Information Technologies and Systems.

Allen, G., & Parsons, J. (2010). Is query reuse potentially harmful? Anchoring and adjustment in adapting existing database queries. Information Systems Research, 21(1), 56-77.

Arazy, O., Kumar, N., & Shapira, B. (2010). A theorydriven design framework for social recommender systems. Journal of the Association for Information Systems, 11(9), 455-490.

Avdiji, H., Elikan, D., Missonier, S., & Pigneur, Y. (2020). A design theory for visual inquiry tools. Journal of the Association for Information Systems, 21(3), 695-734.

Baskerville, R., Baiyere, A., Gregor, S., Hevner, A., & Rossi, M. (2018). Design science research contributions: finding a balance between artifact and theory. Journal of the Association for Information Systems, 19(5), 358-376.

Baskerville, R., Kaul, M., Pries-Heje, J., & Storey, V. (2019). Inducing creativity in design science research. Proceedings of DESRIST: International Conference on Design Science Research in Information Systems and Technology.

Baskerville, R., Kaul, M., & Storey, V. C. (2015). Genres of Inquiry in Design-Science Research: Justification and Evaluation of Knowledge Production. MIS Quarterly, 39(3), 541-564.

Baskerville, R., Kaul, M., & Storey, V. C. (2018). Aesthetics in design science research. European Journal of Information Systems, 27(2), 140-153.

Baxter, P., & Jack, S. (2008). Qualitative case study methodology: Study design and implementation for novice researchers. The qualitative report, 13(4), 544-559.

Beck, R., Weber, S., & Gregory, R. W. (2013). Theorygenerating design science research. Information Systems Frontiers, 15(4), 637-651.

Bonney, R., Shirk, J. L., Phillips, T. B., Wiggins, A., Ballard, H. L., Miller-Rushing, A. J., & Parrish, J. K. (2014). Next steps for citizen science. Science, 343(6178), 1436-1437.

Bunge, M. (1967). Scientific Research: The search for truth. Springer.

Bunge, M. (1996). Finding philosophy in social science. Yale University Press.

Bunge, M. (1998). Philosophy of science: From explanation to justification. Transaction.

Burgess, H., DeBey, L., Froehlich, H., Schmidt, N., Theobald, E., Ettinger, A., … Parrish, J. (2017). The science of citizen science: Exploring barriers to use as a primary research tool. Biological Conservation, 208(1), 1-8.

Burton-Jones, A., Recker, J., Indulska, M., Green, P., & Weber, R. (2017). Assessing representation theory with a framework for pursuing success and failure. MIS Quarterly, 41(4), 1307-1333.

Castellanos, A., Tremblay, M., Lukyanenko, R., & Samuel, B. (2020). Basic classes in conceptual modeling: theory and practical guidelines. Journal of the Association for Information Systems, 21(4), 1001-1044.

Chandra Kruse, L., & Seidel, S. (2017). Tensions in design principle formulation and reuse. Proceedings of DESRIST: International Conference on Design Science Research in Information Systems and Technology.

Chandra Kruse, L., Seidel, S., & Purao, S. (2016). Making Use of Design Principles. Proceedings of DESRIST: International Conference on Design Science Research in Information Systems and Technology.

Chandra, L., Seidel, S., & Gregor, S. (2015). Prescriptive knowledge in IS research: Conceptualizing design principles in terms of materiality, action, and boundary conditions. Proceedings of the Hawaii International Conference on System Sciences.

Chaturvedi, A. R., Dolk, D. R., & Drnevich, P. L. (2011). Design principles for virtual worlds. MIS Quarterly, 35(3), 673-684.

Chiang, R. H. L., Barron, T. M., & Storey, V. C. (1994). Reverse engineering of relational databases: Extraction of an EER model from a relational database. Data & Knowledge Engineering, 12(2), 107-142.

Dasgupta, S. (1996). Technology and creativity. Oxford university Press.

Drechsler, A., & Hevner, A. R. (2018). Utilizing, producing, and contributing design knowledge in DSR projects. Proceedings of DESRIST: International Conference on Design Science Research in Information Systems and Technology.

Dreyfus, H. L. (1992). What computers still can’t do: A critique of artificial reason. MIT Press.

Dubé, L., & Paré, G. (2003). Rigor in information systems positivist case research: Current practices, trends, and recommendations. MIS Quarterly, 27(4), 597-636.

Eriksson, O., Johannesson, P., & Bergholtz, M. (2019). The case for classes and instances-a response to representing instances: The case for reengineering conceptual modelling grammars. European Journal of Information Systems, 28(6), 681-693.

Feibleman, J. (1972). Pure science, applied science and technology: An attempt at definitions. In C. Mitcham & R. Mackey (Eds.), Reading in philosophical problems of technology (pp. 33- 41). The Free Press.

Fortson, L., Masters, K., Nichol, R., Borne, K., Edmondson, E., Lintott, C., … Wallin, J. (2011). Galaxy Zoo: Morphological classification and citizen science. In M. Way, J. D. Scargle, K. M. Ali, & A. Srivastava (Eds.) Advances in Machine Learning and Data Mining for Astronomy (pp. 213-236). Chapman & Hall/CRC.

Germonprez, M., Hovorka, D. S., & Collopy, F. (2007). A theory of tailorable technology design. Journal of the Association for Information Systems, 8(6), 351-367.

Germonprez, M., Hovorka, D. S., & Gal, U. (2011). Secondary design: A case of behavioral design science research. Journal of the Association for Information Systems, 12(10), 662-683.

Gleasure, B., Feller, J., & O’Flaherty, B. (2012). Procedurally transparent design science research: A design process model. Proceedings of the International Conference for Information Systems

Goes, P. B. (2014). Editor’s comments: Design science research in top information systems journals. MIS Quarterly, 38(1), iii-viii.

Goldkuhl, G. (2004). Design theories in information systems-a need for multi-grounding. Journal of Information Technology Theory and Application, 6(2), 59-72.

Goldwater, M. B., Tomlinson, M. T., Echols, C. H., & Love, B. C. (2011). Structural priming as structure-mapping: children use analogies from previous utterances to guide sentence production. Cognitive Science, 35(1), 156-170.

Goodchild, M. (2007). Citizens as sensors: the world of volunteered geography. GeoJournal, 69(4), 211-221.

Gregor, S. (2006). The nature of theory in information systems. MIS Quarterly, 30(3), 611-642.

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. MIS Quarterly, 37(2), 337- 355.

Gregor, S., & Hovorka, D. S. (2011). Causality: The elephant in the room in information systems epistemology. Proceedings of the European Conference on Information Systems.

Gregor, S., & Jones, D. (2007). The anatomy of design theory. Journal of the Association for Information Systems, 8(5), 312-335.

Gregor, S., Müller, O., & Seidel, S. (2013). Reflection, abstraction and theorizing in design and development research. Proceedings of the European Conference for Information Systems.

Heidegger, M. (1996). Being and time: A translation of Sein und Zeit. State University of New York Press.

Hevner, A., & Chatterjee, S. (2010). Design research in information systems: theory and practice. Springer.

Hevner, A., March, S., Park, J., & Ram, S. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75-105.

Hirschheim, R. (2019). Against theory: With apologies to Feyerabend. Journal of the Association for Information Systems, 20(9), 1338-1355.

Hovorka, D. S., & Gregor, S. (2010). Untangling causality in design science theorizing. Paper presented at the 5th Biennial ANU Workshop on Information Systems Foundations: Theory Building in Information Systems.

Hovorka, D. S., Rowe, F., Markus, L., Jarvenpaa, S., Swanson, E. B., Lacity, M., … Hirschheim, R. (2019). Scholarly commentaries on Hirschheim’s “Against Theory.” Journal of the Association for Information Systems, 20(9), 1356-1387.

Iivari, J. (2007). A paradigmatic analysis of information systems as a design science. Scandinavian Journal of Information Systems, 19(2), 39-64.

Jacobson, D., Brail, G., & Woods, D. (2011). APIs: A Strategy guide: Creating channels with application programming interfaces. O’Reilly Media.

Johnson, E. J., Shu, S. B., Dellaert, B. G., Fox, C., Goldstein, D. G., Häubl, G., … Schkade, D. (2012). Beyond nudges: Tools of a choice architecture. Marketing Letters, 23(2), 487-504.

Kerlinger, F. N., & Lee, H. B. (2000). Foundations of behavioral research. Harcourt College Publishers.

Kohavi, R., & Thomke, S. (2017). The surprising power of online experiments. Harvard Business Review, 95(5), 74-87.

Kruglanski, A. W., Köpetz, C., Bélanger, J. J., Chun, W. Y., Orehek, E., & Fishbach, A. (2013). Features of multifinality. Personality and Social Psychology Review, 17(1), 22-39.

Kuechler, W., & Vaishnavi, V. (2008). On theory development in design science research: anatomy of a research project. European Journal of Information Systems, 17(5), 489- 504.

Kuechler, W., & Vaishnavi, V. (2012). A Framework for theory development in design science research: Multiple perspectives. Journal of the Association for Information Systems, 13(6), 395-423.

Lan, Z., Sourina, O., Wang, L., & Liu, Y. (2014). Stability of features in real-time EEG-based emotion recognition algorithm. Paper presented at the 2014 International Conference on Cyberworlds.

Lang, P., & Bradley, M. M. (2007). The International Affective Picture System (IAPS) in the study of emotion and attention. In J. A. Coan & J. J. B. Allen (Eds.), Series in affective science. Handbook of emotion elicitation and assessment (pp. 29-46). Oxford University Press.

Lee, A. (1989). A scientific methodology for MIS case studies. MIS Quarterly, 13(1), 33-50.

Leonardi, P. (2011). When flexible routines meet flexible technologies: Affordance, constraint, and the imbrication of human and material agencies. MIS Quarterly, 35(1), 147-167.

Levy, M., & Germonprez, M. (2017). The potential for citizen science in information systems research. Communications of the Association for Information Systems, 40(1), 22-39.

Lewandowski, E., & Specht, H. (2015). Influence of volunteer and project characteristics on data quality of biological surveys. Conservation Biology, 29(3), 713-723.

Li, J., Larsen, K. R., & Abbasi, A. (2016). TheoryOn: Designing a construct-based search engine to reduce information overload for behavioral science research. Proceedings of DESRIST: International Conference on Design Science Research in Information Systems and Technology.

Lockton, D., Harrison, D., & Stanton, N. A. (2010). The design with intent method: A design tool for influencing user behaviour. Applied Ergonomics, 41(3), 382-392.

Louv, R., Dickinson, J. L., & Bonney, R. (2012). Citizen science: Public participation in environmental research. Cornell University Press.

Lukyanenko, R., Evermann, J., & Parsons, J. (2014). Instantiation validity in IS design research. Proceedings of DESRIST: International Conference on Design Science Research in Information Systems and Technology.

Lukyanenko, R., Evermann, J., & Parsons, J. (2015). Guidelines for establishing instantiation validity in IT artifacts: A survey of IS research. Proceedings of DESRIST: International Conference on Design Science Research in Information Systems and Technology.

Lukyanenko, R., Parsons, J., & Samuel, B. M. (2019). Representing instances: The case for reengineering conceptual modeling grammars. European Journal of Information Systems, 28(1), 68-90.

Lukyanenko, R., Parsons, J., & Wiersma, Y. (2014). The IQ of the crowd: Understanding and improving information quality in structured user-generated content. Information Systems Research, 25(4), 669-689.

Lukyanenko, R., Parsons, J., & Wiersma, Y. (2016). Emerging problems of data quality in citizen science. Conservation Biology, 30(3), 447-449.

Lukyanenko, R., Parsons, J., Wiersma, Y. F., Wachinger, G., Huber, B., & Meldt, R. (2017). Representing crowd knowledge: Guidelines for conceptual modeling of user-generated content. Journal of the Association for Information Systems, 18(4), 297-339.

Lukyanenko, R., Parsons, J., Wiersma, Y., & Maddah, M. (2019). Expecting the unexpected: Effects of data collection design choices on the quality of crowdsourced user-generated content. MIS Quarterly, 43(2), 634-647.

Lukyanenko, R., Parsons, J., Wiersma, Y., Sieber, R., & Maddah, M. (2016). Participatory design for user-generated content: understanding the challenges and moving forward. Scandinavian Journal of Information Systems, 28(1), 37-70.

Lukyanenko, R., Wiggins, A., & Rosser, H. K. (2019). Citizen science: An information quality research frontier. Information Systems Frontiers, 22, 961–983.

Mandviwalla, M. (2015). Generating and justifying design theory. Journal of the Association for Information Systems, 16(5), 314-344.

Markus, M. L., Majchrzak, A., & Gasser, L. (2002). A design theory for systems that support emergent knowledge processes. MIS Quarterly, 26(3), 179-212.

Merton, R. (1949). On sociological theories of the middle range. In: Social Theory and Social Structure, Simon&Schuster.

Mitcham, C. (1994). Thinking through technology: The path between engineering and philosophy. University of Chicago Press.

Moody, D. L. (2009). The “physics” of notations: Toward a scientific basis for constructing visual notations in software engineering. IEEE Transactions on Software Engineering, 35(6), 756-779.

Moody, D. L., Iacob, M.-E., & Amrit, C. (2010). In search of paradigms: Identifying the theoretical foundations of the information system field. Proceedings of the 18th European Conference on Information Systems.

Müller-Wienbergen, F., Müller, O., Seidel, S., & Becker, J. (2011). Leaving the beaten tracks in creative work-a design theory for systems that support convergent and divergent thinking. Journal of the Association for Information Systems, 12(11), 714-740.

Murphy, G. (2004). The big book of concepts. MIT Press.

Negoita, B., Vial, G., Shaikh, M., & Labbe, A. (2019). Code forking and software development project sustainability: Evidence from GitHub. Proceedings of the International Conference on Information Systems.

Norman, D. A. (1999). Affordance, conventions, and design. Interactions, 6(3), 38-43.

Norman, D. A. (2002). The design of everyday things. Basic Books.

Nov, O., Arazy, O., & Anderson, D. (2014). Scientists@ home: What drives the quantity and quality of online citizen science participation. PloS One, 9(4), e90375.

Parsons, J., Lukyanenko, R., & Wiersma, Y. (2011). Easier citizen science is better. Nature, 471(7336), 37-37.

Parsons, J., & Wand, Y. (2008). Using cognitive principles to guide classification in information systems modeling. MIS Quarterly, 32(4), 839- 868.

Peffers, K., Tuunanen, T., Gengler, C. E., Rossi, M., Hui, W., Virtanen, V., & Bragge, J. (2006). The design science research process: a model for producing and presenting information systems research. Proceedings of DESRIST: International Conference on Design Science Research in Information Systems and Technology.

Polanyi, M. (2009). The tacit dimension. University of Chicago Press.

Ponti, M., Hillman, T., Kullenberg, C., & Kasperowski, D. (2018). Getting it right or being top rank: Games in citizen science. Citizen Science: Theory and Practice, 3(1), 1- 12.

Prat, N., Comyn-Wattiau, I., & Akoka, J. (2014). Artifact evaluation in information systems design-science research-a holistic view. Proceedings of the Pacific Asia Conference for Information Systems.

Prat, N., Comyn-Wattiau, I., & Akoka, J. (2015). A Taxonomy of Evaluation Methods for Information Systems Artifacts. Journal of Management Information Systems, 32(3), 229- 267.

Purao, S. (2013). Truth or dare: The ontology question in design science research. Journal of Database Management (JDM), 24(3), 51-66.

Rai, A. (2017). Editor’s comments—Avoiding type III errors: Formulating IS research problems that matter. MIS Quarterly, 41(2), iii-vii.

Rosch, E., Mervis, C. B., Gray, W. D., Johnson, D. M., & Boyesbraem, P. (1976). Basic objects in natural categories. Cognitive Psychology, 8(3), 382-439.

Schön, D. A. (1983). The reflective practitioner: How professionals think in action. Basic Books.

Schön, D. A. (1987). Educating the reflective practitioner: Toward a new design for teaching and learning in the professions. Jossey-Bass.

Schultz, P. W., Messina, A., Tronu, G., Limas, E. F., Gupta, R., & Estrada, M. (2016). Personalized normative feedback and the moderating role of personal norms: A field experiment to reduce residential water consumption. Environment and Behavior, 48(5), 686-710.

Sieber, R. (2006). Public participation geographic information systems: A literature review and framework. Annals of the Association of American Geographers, 96(3), 491-507.

Smith, E., & Medin, D. (1981). Categories and concepts. Harvard University Press.

Snodgrass, J. G., & Vanderwart, M. (1980). A standardized set of 260 pictures: Norms for name agreement, image agreement, familiarity, and visual complexity. Journal of Experimental Psychology: Human Learning and Memory, 6(2), 174-215.

Spagnoletti, P., Resca, A., & Lee, G. (2015). A design theory for digital platforms supporting online communities: A multiple case study. Journal of Information Technology, 30(4), 364-380.

Sunstein, C. R. (2016). The ethics of influence: Government in the age of behavioral science. Cambridge University Press.

Tams, S., Legoux, R., & Leger, P.-M. (2018). Smartphone withdrawal creates stress: A moderated mediation model of nomophobia, social threat, and phone withdrawal context. Computers in Human Behavior, 81(1), 1-9.

Teorey, T. J., Yang, D., & Fry, J. P. (1986). A logical design methodology for relational databases using the extended entity-relationship model. ACM Computing Surveys, 18(2), 197-222.

Tiefenbeck, V. (2017). Bring behaviour into the digital transformation. Nature Energy, 2, 17085.

Tiefenbeck, V., Goette, L., Degen, K., Tasic, V., Fleisch, E., Lalive, R., & Staake, T. (2016). Overcoming salience bias: How real-time feedback fosters resource conservation. Management Science, 64(3), 1458-1476.

Tiefenbeck, V., Goette, L., Degen, K., Tasic, V., Fleisch, E., Lalive, R., & Staake, T. (2018). Overcoming salience bias: How real-time feedback fosters resource conservation. Management science, 64(3), 1458-1476.

Tiefenbeck, V., Schöb, S., Kupfer, A., & Staake, T. (2016). Fostering sustainable consumer decisions in practice: The impact of real-time feedback on resource consumption and voluntary carbon offsetting. In: SABE/IAREP Conference 2016, 21-23.

Tiefenbeck, V., Wörner, A., Schöb, S., Fleisch, E., & Staake, T. (2019). Real-time feedback reduces energy consumption among the broader public without financial incentives. Nature Energy, 4(10), 831-832.

Tulving, E., Schacter, D. L., & Stark, H. A. (1982). Priming effects in word-fragment completion are independent of recognition memory. Journal of Experimental Psychology: Learning, Memory, and Cognition, 8(4), 336-342.

Tversky, A., Kahneman, D., & Moser, P. (1990). Judgment under uncertainty: Heuristics and biases. In P. K. Moser (Ed.), Rationality in

action: Contemporary approaches, Cambridge University Press.

Vaast, E., Safadi, H., Lapointe, L., & Negoita, B. (2017). Social media affordances for connective action-an examination of microblogging use during the Gulf of Mexico oil spill. MIS Quarterly, 41(4), 1179-1205.

Venable, J. (2006). The role of theory and theorising in design science research. Proceedings of DESRIST: International Conference on Design Science Research in Information Systems and Technology.

Venable, J. (2011). Incorporating design science research and critical research into an introductory business research methods course. Electronic Journal of Business Research Methods, 9(2), 119-129.

Venable, J. (2013). Rethinking design theory in information systems. Proceedings of DESRIST: International Conference on Design Science Research in Information Systems and Technology.

vom Brocke, J., Winter, R., Hevner, A., & Maedche, A. (2020). Accumulation and evolution of design knowledge in design science research: A journey through time and space. Journal of the Association for Information Systems, 21(3), 520-544.

Walls, J. G., Widermeyer, G. R., & El Sawy, O. A. (2004). Assessing information system design theory in perspective: How useful was our 1992 initial rendition? Journal of Information Technology Theory and Application, 6(2), 43- 58.

Walls, J. G., Widmeyer, G. R., & El Sawy, O. A. (1992). Building an information system design theory for vigilant EIS. Information Systems Research, 3(1), 36-59.

Wand, Y., & Weber, R. (1990). Toward a theory of the deep structure of information systems. Proceedings of the International Conference on Information Systems.

Wand, Y., & Weber, R. (1993). On the ontological expressiveness of information systems analysis and design grammars. Information Systems Journal, 3(4), 217-237.

Wand, Y., & Weber, R. (1995). On the deep-structure of information-systems. Information Systems Journal, 5(3), 203-223.

Weber, R. (2003). Editor’s comments: The problem of the problem. MIS Quarterly, 27(1), iii-ix.

Weber, R. (2012). Evaluating and developing theories in the information systems discipline. Journal of the Association for Information Systems, 13(1), 1-30.

Weick, K. E. (1989). Theory construction as disciplined imagination. Academy of Management Review, 516-531.

Weick, K. E. (1995). What theory is not, theorizing is. Administrative Science Quarterly, 40(3), 385- 390.

Weinmann, M., Schneider, C., & vom Brocke, J. (2016). Digital nudging. Business & Information Systems Engineering, 58(6), 433- 436.

Wiggins, A., & Crowston, K. (2014). Surveying the citizen science landscape. First Monday, 20(1), 1-10.

Yin, R. K. (2013). Case study research: Design and methods. SAGE.

## Appendix

Design theories deliberately abstract away potentially pertinent aspects of reality to reach certain “subjectively” desirable levels of generality by researchers. However, the level of abstraction affects the ability of practitioners to implement a theory. In a design theory, independent variables (e.g., abstract design principles) are meant to be translated by practitioners into some actionable form, which specifies exactly how to develop focal features.

Borrowing from engineering, for this analysis we capture this form using the notion of a technological rule based on the condition-operation notation (Dasgupta, 1996). Dasgupta (1996) argues these types of operational principles are readily understood and natural to practice: they are “the predominant kind of knowledge that the software engineer brings to bear in the creation of software artifacts” (p. 166, emphasis in the original). For example, based on the instance-based design theory in Case 1, when trying to implement a theory, a practitioner may formulate the following mental operational rule using the general condition-operation:

condition: IF the goal is to increase data quality and user participation in a crowdsourcing project

Rule 1

operation: THEN collect information in terms of attributes of instances rather than classes

To generate a technological rule out of a design theory, a certain degree of specificity is needed in the theoretical constructs, particularly those that correspond to the operation part of the design theory. For example, stipulating that, to increase quality and user participation, an IS needs to be based on “flexible database design” (Lukyanenko et al., 2016, p. 9) is less specific than stating that information should be a collection in terms of “attributes to represent individual instances” (Lukyanenko et al., 2017, p. 307), as the latter manifests flexibility in a particular way. Such specificity also makes a design theory more falsifiable. Yet, as this case demonstrates, to support development, even more specific technological rules are needed. Extending the rule-based structure proposed by Dasgupta, we argue that a designer may wish to formulate the following technological rule recursively based on the previous one:

IF the goal is to collect information in terms of attributes of instances

Rule 2

THEN create form elements each corresponding to the attributes in a domain

A designer can take this one step further and formulate another rule, Rule 3:

IF the goal is to create form elements each corresponding to the attributes in a domain

Rule 3

THEN create a checkbox control bound to a dataset containing predefined attributes

The creation of rules from a design theory exemplifies the problem of DTI, as such rules articulate specific design choices that generally go beyond what the theory specifies. In the above examples, Rule 2 is derived from Rule 1 and Rule 3 is derived from Rule 2: the condition element of each subsequent rule contains the operation from the previous rule. Such a hierarchical nesting of rules is necessary because the operation in a general rule (e.g., Rule 1) is not clear enough to isolate specific actions and fully explain to a developer what needs to be done. A more specific rule (i.e., Rule 2) becomes necessary to enact Rule 1. Similarly, since Rule 2 is also not specific enough, a designer will recursively construct new rules (explicitly or implicitly) until the actionable rule is reached when the level of specificity of the operation element of a rule matches the situation at hand.<sup>5</sup> A useful outcome of this approach is that it provides traceability—specifying (but not fully justifying) design choices that were made to reduce ambiguity arising from DTI. This makes is possible to later understand how (and why) specific design decisions were taken during the design and development process.

Unlike Rule 1, Rule 2 and all derived rules are less grounded in the original theory. Indeed, one could formulate an alternative operation in Rule 2, calling for a single textbox that would collect attributes (without having a user select from a predefined list of attributes). Similarly, in Rule 3, one could stipulate to use radio boxes, dropdown lists or combo-boxes rather than checkboxes. The operations in Rules 2 and 3 are indirectly grounded in theory (via Rule 1), but also driven by other factors (e.g., needs of a situation, development software constraints, aesthetics [Baskerville, Kaul, et al., 2018], or a designer’s familiarity with checkbox form using controls vs. radio button controls). Moreover, such rules can be further justified by “attaching” the rationale for specific design choices (e.g., aligns with past practice or developer experience). In addition, if the desired outcomes associated with implementing the design theory are not realized, such choices can be revisited and alternative manifestations chosen as a way of determining if these nontheoretical design choices mitigated the expected outcomes. Theoretical grounding tends to fade with each new step in the recursion. Since every IS deployment is unique in some way (Lee, 1989), there is always some aspect of either the IS itself or the deployment context that cannot be accounted for by theories. Schön (1987) contends that these unique situations cannot be handled “solely by applying [known] theories or techniques” (p. 6). Since the recursion began as a condition and operation imbued in the theory itself (i.e., Rule 1 is part of the design theory itself), subsequent recursions are not fully within theoretical control. In general, the higher the level of abstraction of a design theory (i.e., broad theory vs. midrange), the more recursions would be needed to reach actionable rules.

## About the Authors

Roman Lukyanenko is an associate professor in the Department of Information Technologies at HEC Montreal, Canada. Roman obtained his PhD from Memorial University of Newfoundland under the supervision of Dr. Jeffrey Parsons. Roman’s research interests include conceptual modeling, information quality, crowdsourcing, machine learning, design science research, and research methods (research validities, instantiation validity, and artifact sampling). Roman’s work on these topics has been published in Nature, MIS Quarterly, Information Systems Research, Journal of the Association for Information Systems, European Journal of Information Systems, among others. His 2019 paper on quality of crowdsourced data received the Best Paper Award at MIS Quarterly. Roman is the current president for the AIS SIGSAND and the developer of www.sigsand.com.

Jeffrey Parsons is University Research Professor and professor of information systems in the Faculty of Business Administration at Memorial University of Newfoundland. His research interests include conceptual modeling, crowdsourcing, information quality, data integration, and recommender systems. His work on these topics has appeared in top journals in information systems (e.g., Information Systems Research, Journal of the Association for Information Systems, MIS Quarterly), management (e.g., Management Science), computer science (e.g., ACM Transactions on Database Systems, IEEE Transactions on Knowledge and Data Engineering), and biology (e.g., Nature, Conservation Biology). He is a senior editor for MIS Quarterly, a former senior editor for the Journal of the Association for Information Systems, and he has served as program co-chair for several major information systems conferences, including AMCIS, WITS, ER, and DESRIST. He has received numerous awards, including the INFORMS ISS Design Science Award, the Schoeller Senior Fellowship, and the designation of ER Fellow.

Copyright © 2020 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
